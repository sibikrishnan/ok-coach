# Sports Video Analyzer - User Stories

## Primary User: Amateur Table Tennis Player
**Goal:** Improve technique by getting AI-powered analysis of gameplay videos

---

## Epic: Video Analysis for Skill Improvement

### User Story 1: Analyze YouTube Video
**As a** table tennis player
**I want to** provide a YouTube URL of my gameplay
**So that** I can get automated analysis of my technique

**Acceptance Criteria:**
- User provides a valid YouTube URL
- System downloads the video successfully
- System extracts key frames from the video
- System analyzes frames using Claude Vision API
- User receives 5 specific observations about technique

**Technical Notes:**
- Use yt-dlp for reliable YouTube downloads
- Extract 5 frames at 20%, 35%, 50%, 65%, 80% of video duration
- Frames avoid intro/outro to focus on actual gameplay

---

### User Story 2: Understand Tool Execution Flow
**As a** developer learning advanced tool use
**I want to** see clear logging of each tool execution step
**So that** I can understand how Claude chains tools together

**Acceptance Criteria:**
- Each tool execution is logged with clear timestamps
- Tool inputs and outputs are visible
- Sequential vs parallel execution is observable
- Token usage is tracked and displayed

**Learning Objectives:**
- Observe tool chaining (download → extract → analyze)
- See how Claude reasons about tool dependencies
- Understand message structure with tool_use and tool_result blocks

---

### User Story 3: Get Actionable Technique Feedback
**As a** table tennis player
**I want to** receive specific, actionable observations
**So that** I can focus my practice on concrete improvements

**Acceptance Criteria:**
- Analysis provides 5 distinct observations
- Each observation is specific (not generic)
- Observations cover different aspects: technique, positioning, form, footwork
- Observations are based on actual visual analysis of frames

**Example Output:**
1. "Paddle angle during backhand stroke is too open (>45°), causing ball to lift"
2. "Weight distribution favors back foot, limiting forward momentum"
3. "Elbow drops below table level during forehand preparation"
4. "Ready position stance is too narrow (~shoulder width vs recommended 1.5x)"
5. "Follow-through on serves stops abruptly instead of continuing across body"

---

## Epic: Learn Advanced Tool Use Patterns

### User Story 4: Experience Sequential Tool Chaining
**As a** developer
**I want to** implement tools with clear dependencies
**So that** I can see how Claude manages multi-step workflows

**Acceptance Criteria:**
- Tool 1 (download) must complete before Tool 2 (extract) starts
- Tool 2 must complete before Tool 3 (analyze) starts
- Claude automatically determines execution order
- Error in any step prevents subsequent tools from running

**Learning Goal:** Understand dependency management in agentic systems

---

### User Story 5: Handle Errors Gracefully
**As a** user
**I want to** receive clear error messages when something fails
**So that** I can understand what went wrong and how to fix it

**Acceptance Criteria:**
- Invalid YouTube URL: "Could not download video. Please check the URL."
- Download failure: "YouTube download failed: [specific reason]"
- Frame extraction failure: "Could not extract frames from video file"
- Vision API error: "Analysis failed: [API error details]"

**Learning Goal:** Error handling in tool execution loops

---

### User Story 6: Monitor Resource Usage
**As a** developer
**I want to** track token usage and costs
**So that** I can optimize my prompts and frame counts

**Acceptance Criteria:**
- Display estimated token count before analysis
- Show actual token usage after completion
- Display approximate cost in USD
- Log frame sizes and processing time

**Learning Goal:** Cost optimization in multi-modal AI applications

---

## Epic: Future Enhancements (Out of Scope for MVP)

### User Story 7: Analyze Local Video Files
**As a** user
**I want to** upload video files from my device
**So that** I can analyze videos not on YouTube

**Status:** Future enhancement

---

### User Story 8: Customize Analysis Focus
**As a** player
**I want to** specify what aspect to analyze (serve, footwork, positioning)
**So that** I can get targeted feedback on specific skills

**Status:** Future enhancement

---

### User Story 9: Use Prompt Caching for Cost Savings
**As a** developer
**I want to** implement prompt caching
**So that** I can reduce costs when analyzing multiple videos

**Status:** Future enhancement (requires prompt caching beta)

---

## Success Metrics

### MVP Success Criteria
- ✅ Successfully analyzes target video: https://www.youtube.com/watch?v=O59GbYOCBpY
- ✅ Extracts exactly 5 frames
- ✅ Claude executes all 3 tools in correct sequence
- ✅ Receives 5 specific technique observations
- ✅ Complete execution in under 60 seconds
- ✅ Total cost per analysis < $0.10

### Learning Success Criteria
- ✅ Understand tool schema design
- ✅ Observe sequential tool execution
- ✅ Experience vision API integration
- ✅ Monitor token usage patterns
- ✅ Document key learnings in README

---

## Technical Requirements

### System Requirements
- Python 3.9+
- ffmpeg installed on system
- Anthropic API key with access to advanced-tool-use-2025-11-20 beta
- Internet connection for YouTube downloads

### Dependencies
- anthropic >= 0.39.0
- yt-dlp >= 2024.0.0
- opencv-python >= 4.8.0
- pillow >= 10.0.0

### API Requirements
- Advanced Tool Use Beta: `advanced-tool-use-2025-11-20`
- Model: `claude-sonnet-4-5-20250929`
- Vision API support for multi-image analysis

---

## Definition of Done

A user story is complete when:
1. Code is implemented and working
2. Manual testing passes all acceptance criteria
3. Error handling is in place
4. Logging provides visibility into execution
5. Learning objectives are documented
6. Git commit follows project template
