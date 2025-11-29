# Claude Instructions for Sports Video Analyzer Project

## Project Context
This is a learning project to understand Anthropic's Advanced Tool Use beta by building a practical sports video analyzer for table tennis gameplay.

**Primary Goal:** Learn advanced tool use patterns while creating real value
**Target Video:** https://www.youtube.com/watch?v=O59GbYOCBpY

---

## Development Principles

### 1. Incremental Development
- Build one component at a time
- Test each tool independently before integration
- Do NOT one-shot the entire implementation
- Get user approval before moving to next component

### 2. Learning-Focused Implementation
- Add detailed logging at every step
- Document WHY decisions are made, not just WHAT
- Include comments explaining advanced tool use patterns
- Track token usage and costs

### 3. Keep It Simple
- MVP first, enhancements later
- No over-engineering
- Hardcoded values are fine for learning (video URL, frame count, etc.)
- Avoid premature abstractions

### 4. Git Hygiene
- Commit after each major component is working
- Follow commit message template from ~/.claude/CLAUDE.md
- Always include what was learned in commit message body

---

## Architecture Overview

```
video_analyzer/
├── tools.py          # Tool schemas + implementations
├── agent.py          # Advanced tool use agent loop
├── main.py           # CLI entry point
├── requirements.txt  # Python dependencies
└── README.md         # Learning documentation
```

### Tool Chain Flow
```
User Request
    ↓
download_youtube_video (Tool 1)
    ↓
extract_video_frames (Tool 2)
    ↓
analyze_sport_technique (Tool 3)
    ↓
Final Analysis
```

---

## Implementation Guidelines

### Tool Implementation (`tools.py`)

Each tool must have:
1. **Tool Schema** - JSON schema for Anthropic API
2. **Implementation Function** - Actual Python function
3. **Error Handling** - Graceful failures with clear messages
4. **Logging** - What's happening at each step

**Tool Schema Template:**
```python
{
    "name": "tool_name",
    "description": "Clear description of what the tool does and when to use it",
    "input_schema": {
        "type": "object",
        "properties": {
            "param_name": {
                "type": "string",
                "description": "What this parameter is for"
            }
        },
        "required": ["param_name"]
    }
}
```

**Implementation Requirements:**
- Use type hints
- Add docstrings
- Log inputs and outputs
- Return structured data (dicts/lists, not just strings)
- Clean up temporary files

### Agent Loop (`agent.py`)

Must implement:
1. **Message preparation** with tool definitions
2. **Response parsing** to detect tool_use blocks
3. **Tool execution** by calling functions from tools.py
4. **Result formatting** as tool_result blocks
5. **Continuation** until final text response
6. **Token tracking** throughout conversation

**Critical Pattern:**
```python
while not done:
    response = client.beta.messages.create(...)

    if has_tool_use(response):
        results = execute_tools(response)
        add_tool_results_to_conversation(results)
    else:
        return final_text_response
```

### CLI Interface (`main.py`)

Requirements:
- Simple, clear output
- Progress indicators for long operations
- Display token usage and cost
- Show tool execution flow
- Error messages in red (if possible)

---

## Key Learning Objectives

As you implement, pay attention to:

1. **Tool Schema Design**
   - How descriptions affect Claude's reasoning
   - What parameters are needed vs optional
   - How to make tools composable

2. **Sequential Execution**
   - How Claude determines execution order
   - Dependency management between tools
   - Error propagation through chain

3. **Multi-modal Integration**
   - How to structure image data for vision API
   - Token costs for images vs text
   - Analyzing multiple images together

4. **Message Structure**
   - Format of tool_use blocks
   - Format of tool_result blocks
   - Maintaining conversation history

5. **Error Handling**
   - Tool execution failures
   - API errors
   - Invalid inputs
   - Resource cleanup

6. **Cost Optimization**
   - Token usage per frame
   - Impact of frame count on analysis quality
   - Prompt efficiency

---

## Testing Strategy

### Unit Testing
Test each tool function independently:
- `download_youtube_video`: Use test video URL
- `extract_video_frames`: Use small test video file
- `analyze_sport_technique`: Use sample frames

### Integration Testing
Test full flow:
1. Run with target video URL
2. Verify all 3 tools execute in order
3. Confirm analysis quality
4. Check token usage is reasonable (<15k tokens)

### Error Testing
Test failure scenarios:
- Invalid YouTube URL
- Network failure during download
- Corrupted video file
- Vision API rate limits

---

## Common Patterns to Follow

### Logging Pattern
```python
print(f"[Tool: {tool_name}] {action}...")
# ... do work ...
print(f"✓ {result_summary}")
```

### Error Handling Pattern
```python
try:
    result = risky_operation()
    return {"success": True, "data": result}
except SpecificError as e:
    return {"success": False, "error": str(e)}
```

### Resource Cleanup Pattern
```python
temp_files = []
try:
    # ... create temp files ...
    temp_files.append(file_path)
    # ... use files ...
finally:
    for f in temp_files:
        if os.path.exists(f):
            os.remove(f)
```

---

## Dependencies & Setup

### System Requirements
- Python 3.9 or higher
- ffmpeg installed (`brew install ffmpeg` on macOS)
- Anthropic API key in environment variable

### Python Packages
```
anthropic>=0.39.0     # Anthropic API client
yt-dlp>=2024.0.0      # YouTube downloader
opencv-python>=4.8.0  # Video frame extraction
pillow>=10.0.0        # Image processing
```

### Environment Variables
```bash
export ANTHROPIC_API_KEY="your-api-key"
```

---

## Commit Message Template

When committing code:

```
<type>: <short description>

<detailed explanation of what was done>

Learning notes:
- <what you learned from implementing this>
- <patterns observed>
- <any challenges faced>

🤖 Generated with Claude Code

Co-Authored-By: Claude <noreply@anthropic.com>
```

Types: `feat`, `fix`, `refactor`, `docs`, `test`

---

## Cost & Token Budgets

### Per-Analysis Budget
- Max tokens: 20,000 (input + output)
- Target tokens: 12,000
- Max cost per run: $0.10

### Token Breakdown
- System prompt: ~500 tokens
- Tool definitions: ~1,000 tokens
- 5 frames × 2,000 tokens/frame: 10,000 tokens
- Analysis response: ~2,000 tokens
- **Total: ~13,500 tokens** ✓ Within budget

---

## Future Enhancements (Document, Don't Build)

As you discover improvements, add them to README.md:
- Variable frame counts
- Different analysis prompts
- Parallel frame extraction
- Prompt caching integration
- Local video file support
- Web interface

Don't implement these yet - focus on MVP.

---

## Questions to Ask User

Before implementing each phase:
1. "Ready to implement [component]?"
2. "Should I proceed with [approach]?"
3. "Want to review [code] before testing?"

Never assume - always confirm before major steps.

---

## Success Criteria

You'll know the project is successful when:
- ✅ Can analyze target video end-to-end
- ✅ See clear tool execution chain in logs
- ✅ Understand how advanced tool use differs from basic approach
- ✅ Can explain token costs and optimization opportunities
- ✅ Have documented learnings in README
- ✅ User feels confident building similar agents

---

## Remember

This is a **learning project**, not a production system. Prioritize:
1. Understanding over optimization
2. Clarity over cleverness
3. Documentation over features
4. Experimentation over perfection

The goal is to internalize advanced tool use patterns that apply to any agentic system.
