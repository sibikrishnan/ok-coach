# OK Coach - Sports Video Analyzer

A learning project to explore Anthropic's Advanced Tool Use beta by building a practical sports video analysis tool.

## 🎯 Project Goals

1. **Learn Advanced Tool Use** - Experience tool chaining, multi-step workflows, and vision API integration
2. **Keep It Simple** - Build an MVP that works end-to-end without over-engineering
3. **Create Real Value** - Get actionable insights from table tennis gameplay videos

## 🏗️ Architecture

This project demonstrates Anthropic's advanced tool use patterns through a sequential tool chain:

```
YouTube URL
    ↓
[Tool 1] download_youtube_video
    ↓
[Tool 2] extract_video_frames (5 frames at 20%, 35%, 50%, 65%, 80%)
    ↓
[Tool 3] analyze_sport_technique (Claude Vision API)
    ↓
5 Specific Technique Observations
```

## 📁 Project Structure

```
ok-coach/
├── video_analyzer/          # Main application code
│   ├── tools.py            # Tool definitions and implementations
│   ├── agent.py            # Advanced tool use agent loop
│   ├── main.py             # CLI entry point
│   └── requirements.txt    # Python dependencies
├── CLAUDE.md               # Project-specific instructions for Claude
├── USER_STORIES.md         # Detailed user stories and acceptance criteria
└── README.md               # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- ffmpeg installed on your system:
  ```bash
  # macOS
  brew install ffmpeg

  # Ubuntu/Debian
  sudo apt-get install ffmpeg
  ```
- Anthropic API key with access to `advanced-tool-use-2025-11-20` beta

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sibikrishnan/ok-coach.git
   cd ok-coach
   ```

2. Set up Python environment:
   ```bash
   cd video_analyzer
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set your Anthropic API key:
   ```bash
   export ANTHROPIC_API_KEY="your-api-key-here"
   ```

### Usage

```bash
python main.py
```

The script will analyze the default video (https://www.youtube.com/watch?v=O59GbYOCBpY) and provide 5 specific observations about table tennis technique.

## 🎓 Learning Objectives

This project helps you understand:

1. **Tool Schema Design** - How to define tools that Claude can reason about
2. **Sequential Execution** - How Claude chains tools with dependencies
3. **Multi-modal Reasoning** - Vision API + tool use integration
4. **Error Recovery** - How Claude handles tool failures
5. **Conversation Flow** - Message structure with tool_use and tool_result blocks
6. **Cost Optimization** - Token usage monitoring and cost management

## 💰 Cost Estimation

Per video analysis:
- 5 frames @ ~2,000 tokens each = 10,000 tokens (input)
- Tool definitions + conversation = ~2,000 tokens
- Analysis response = ~2,000 tokens (output)
- **Total: ~14,000 tokens ≈ $0.05 per video**

Very affordable for learning!

## 📊 Current Status

### Phase 1: Project Setup ✅
- [x] Repository created and linked
- [x] Project structure established
- [x] Dependencies defined
- [x] Tool schemas designed
- [ ] Ready for implementation

### Phase 2: Tool Implementation (In Progress)
- [ ] download_youtube_video
- [ ] extract_video_frames
- [ ] analyze_sport_technique

### Phase 3: Agent Loop (Pending)
- [ ] Advanced tool use loop
- [ ] Message handling
- [ ] Error recovery

### Phase 4: CLI Interface (Pending)
- [ ] User interface
- [ ] Logging and progress indicators
- [ ] Token usage tracking

### Phase 5: Testing & Documentation (Pending)
- [ ] End-to-end testing
- [ ] Learning documentation
- [ ] Performance analysis

## 🔍 Advanced Features Being Explored

From the [Anthropic Engineering Blog](https://www.anthropic.com/engineering/advanced-tool-use):

- ✅ **Tool Chaining** - Sequential execution with dependencies
- ✅ **Multi-modal Integration** - Vision API with tool use
- ⏳ **Error Handling** - Graceful failure recovery
- ⏳ **Resource Management** - Cleanup and optimization
- 🔮 **Parallel Tool Execution** - Future enhancement
- 🔮 **Prompt Caching** - Cost optimization (future)

## 📖 Documentation

- See [USER_STORIES.md](USER_STORIES.md) for detailed user stories and acceptance criteria
- See [CLAUDE.md](CLAUDE.md) for development guidelines and patterns
- See [Implementation Plan](/.claude/plans/dapper-painting-breeze.md) for detailed implementation roadmap

## 🤝 Contributing

This is a personal learning project, but feedback and suggestions are welcome! Feel free to open issues or submit PRs.

## 📝 License

MIT License - feel free to use this code for your own learning projects.

## 🙏 Acknowledgments

- Built using [Anthropic's Claude API](https://www.anthropic.com/)
- Inspired by the [Advanced Tool Use Engineering Blog](https://www.anthropic.com/engineering/advanced-tool-use)
- Developed with [Claude Code](https://claude.com/claude-code)

---

**Target Video:** Table Tennis POV - https://www.youtube.com/watch?v=O59GbYOCBpY

**Last Updated:** 2025-11-29
