#!/bin/bash
# Run update.py first
uv run update.py

# Run Backend and app.py concurrently
uv run -m Backend & uv run app.py &

# Wait for either process to exit
wait -n
