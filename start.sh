# Start health server in background
python3 health.py &

# Start your main scripts
uv run update.py && uv run -m Backend
