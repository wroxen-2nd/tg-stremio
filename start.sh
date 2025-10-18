#!/bin/bash

# Activate uv virtual environment
source /app/.venv/bin/activate

# Start Flask health server in the background
python3 health.py &

# Start your main scripts
uv run update.py && uv run -m Backend
