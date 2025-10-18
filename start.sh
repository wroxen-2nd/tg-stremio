#!/bin/bash

# Activate uv virtual environment
source /app/.venv/bin/activate

# Start your main scripts
uv run update.py && uv run -m Backend
