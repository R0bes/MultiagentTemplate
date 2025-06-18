#!/bin/bash
set -e

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

echo "Environment setup complete. To start the initial agent, read agents/InitAgent.md"
