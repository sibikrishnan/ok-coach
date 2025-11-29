"""
Tool definitions and implementations for Sports Video Analyzer

This module demonstrates Anthropic's Advanced Tool Use patterns:
1. Sequential tool chaining (download -> extract -> analyze)
2. Multi-modal integration (vision API)
3. Error handling in tool execution
"""

import os
import json
import base64
from typing import Dict, List, Any
from pathlib import Path

# ============================================================================
# TOOL SCHEMAS - Definitions that Claude uses to reason about tools
# ============================================================================

TOOL_SCHEMAS = [
    {
        "name": "download_youtube_video",
        "description": (
            "Downloads a video from YouTube and saves it to a local file. "
            "Use this tool when you need to get a video file from a YouTube URL. "
            "This must be called BEFORE extract_video_frames."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "The full YouTube URL (e.g., https://www.youtube.com/watch?v=VIDEO_ID)"
                },
                "output_dir": {
                    "type": "string",
                    "description": "Directory to save the downloaded video (optional, defaults to /tmp)"
                }
            },
            "required": ["url"]
        }
    },
    {
        "name": "extract_video_frames",
        "description": (
            "Extracts frames from a video file at specified timestamps. "
            "Frames are extracted as evenly-spaced samples throughout the video duration. "
            "Use this tool AFTER download_youtube_video and BEFORE analyze_sport_technique. "
            "Returns base64-encoded images ready for vision API."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "video_path": {
                    "type": "string",
                    "description": "Full path to the video file (returned from download_youtube_video)"
                },
                "num_frames": {
                    "type": "integer",
                    "description": "Number of frames to extract (default: 5, recommended: 3-10 for cost efficiency)"
                },
                "positions": {
                    "type": "array",
                    "items": {"type": "number"},
                    "description": "Optional: specific positions to extract frames at (0.0-1.0, where 0.0=start, 1.0=end)"
                }
            },
            "required": ["video_path"]
        }
    },
    {
        "name": "analyze_sport_technique",
        "description": (
            "Analyzes sports technique from video frames using Claude's vision capabilities. "
            "Takes multiple frames and provides detailed observations about technique, form, positioning, etc. "
            "Use this tool AFTER extract_video_frames. This is the final step in the analysis chain."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "frames_data": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Array of base64-encoded frame images (from extract_video_frames)"
                },
                "analysis_prompt": {
                    "type": "string",
                    "description": "Specific analysis request (e.g., 'analyze table tennis technique and list 5 observations')"
                },
                "sport_type": {
                    "type": "string",
                    "description": "Type of sport being analyzed (optional, helps context)"
                }
            },
            "required": ["frames_data", "analysis_prompt"]
        }
    }
]


# ============================================================================
# TOOL IMPLEMENTATIONS - Actual functions that execute tool logic
# ============================================================================

def download_youtube_video(url: str, output_dir: str = "/tmp") -> Dict[str, Any]:
    """
    Downloads a YouTube video using yt-dlp.

    Args:
        url: YouTube video URL
        output_dir: Directory to save video (default: /tmp)

    Returns:
        Dict with:
            - success: bool
            - video_path: str (path to downloaded file) if success
            - error: str (error message) if failure

    Learning Notes:
        - This demonstrates tool implementation that can fail gracefully
        - Return structured data that Claude can reason about
        - Include file path in response so next tool can use it
    """
    print(f"[Tool: download_youtube_video] Downloading from {url}...")

    # TODO: Implement using yt-dlp
    # - Use yt-dlp library to download video
    # - Handle errors (invalid URL, network issues, etc.)
    # - Return video file path for next tool
    # - Clean up on failure

    raise NotImplementedError("Tool implementation pending")


def extract_video_frames(
    video_path: str,
    num_frames: int = 5,
    positions: List[float] = None
) -> Dict[str, Any]:
    """
    Extracts frames from video at specified positions.

    Args:
        video_path: Path to video file
        num_frames: Number of frames to extract (default: 5)
        positions: Optional specific positions (0.0-1.0) to extract at

    Returns:
        Dict with:
            - success: bool
            - frames: List[str] (base64-encoded images) if success
            - frame_count: int
            - error: str if failure

    Learning Notes:
        - This tool depends on output from download_youtube_video
        - Demonstrates data transformation (video -> images -> base64)
        - Frame selection strategy affects analysis quality and cost
    """
    print(f"[Tool: extract_video_frames] Extracting {num_frames} frames from {video_path}...")

    # TODO: Implement using opencv or ffmpeg
    # - Get video duration
    # - Calculate frame positions (default: 20%, 35%, 50%, 65%, 80%)
    # - Extract frames at those positions
    # - Convert frames to base64-encoded images
    # - Return array of base64 strings

    raise NotImplementedError("Tool implementation pending")


def analyze_sport_technique(
    frames_data: List[str],
    analysis_prompt: str,
    sport_type: str = "table tennis"
) -> Dict[str, Any]:
    """
    Analyzes sport technique using Claude Vision API.

    Args:
        frames_data: List of base64-encoded frame images
        analysis_prompt: What to analyze
        sport_type: Type of sport (for context)

    Returns:
        Dict with:
            - success: bool
            - analysis: str (Claude's analysis) if success
            - token_usage: dict with input/output token counts
            - error: str if failure

    Learning Notes:
        - This demonstrates multi-modal API usage (images + text)
        - Shows how to structure vision API requests
        - Token usage tracking is critical for cost management
        - This is NOT using advanced tool use beta - it's the final analysis step
    """
    print(f"[Tool: analyze_sport_technique] Analyzing {len(frames_data)} frames for {sport_type}...")

    # TODO: Implement using Anthropic Messages API with vision
    # - Create message with multiple image content blocks
    # - Include analysis_prompt as text
    # - Use claude-sonnet-4-5 (supports vision)
    # - Track token usage from response
    # - Return analysis text + token counts

    raise NotImplementedError("Tool implementation pending")


# ============================================================================
# TOOL REGISTRY - Maps tool names to implementation functions
# ============================================================================

TOOL_FUNCTIONS = {
    "download_youtube_video": download_youtube_video,
    "extract_video_frames": extract_video_frames,
    "analyze_sport_technique": analyze_sport_technique,
}


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def execute_tool(tool_name: str, tool_input: Dict[str, Any]) -> Dict[str, Any]:
    """
    Executes a tool by name with given input.

    This is called by the agent loop when Claude requests a tool.

    Args:
        tool_name: Name of tool to execute
        tool_input: Parameters for the tool

    Returns:
        Tool execution result (structure depends on tool)

    Learning Notes:
        - This is the bridge between Claude's tool requests and actual execution
        - Error handling here prevents agent loop crashes
        - Logging helps understand tool execution flow
    """
    if tool_name not in TOOL_FUNCTIONS:
        return {
            "success": False,
            "error": f"Unknown tool: {tool_name}"
        }

    try:
        tool_func = TOOL_FUNCTIONS[tool_name]
        result = tool_func(**tool_input)
        return result
    except Exception as e:
        return {
            "success": False,
            "error": f"Tool execution failed: {str(e)}"
        }


def get_tool_schemas() -> List[Dict[str, Any]]:
    """Returns tool schemas for Anthropic API."""
    return TOOL_SCHEMAS


# ============================================================================
# VALIDATION & TESTING
# ============================================================================

if __name__ == "__main__":
    """Quick validation that tool schemas are correct."""
    print("Tool Schemas Validation")
    print("=" * 50)

    for i, schema in enumerate(TOOL_SCHEMAS, 1):
        print(f"\n{i}. {schema['name']}")
        print(f"   Description: {schema['description'][:80]}...")
        print(f"   Required params: {schema['input_schema'].get('required', [])}")

    print("\n✓ All tool schemas loaded successfully")
    print(f"✓ {len(TOOL_SCHEMAS)} tools defined")
    print(f"✓ {len(TOOL_FUNCTIONS)} implementations registered")
