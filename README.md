# AI Agent

A small Python coding agent powered by OpenRouter. It can explore files, read and
edit code, and run Python scripts in the included `calculator/` project.

## Quick start

Requires Python 3.13+ and [uv](https://docs.astral.sh/uv/).

1. Run `uv sync` to install dependencies.
2. Add `OPENROUTER_API_KEY=your_key_here` to a `.env` file.
3. Try it:

   ```bash
   uv run main.py "Explain how the calculator works"
   ```

Add `--verbose` to see tool details and token usage.

**Note:** The agent can modify files and execute code. Use it only with code you
trust, and never commit your `.env` file.
