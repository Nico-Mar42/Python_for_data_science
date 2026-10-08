#!/usr/bin/env bash
set -e

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$PROJECT_DIR/.venv"

python3 -m venv "$VENV_DIR"
"$VENV_DIR/bin/python" -m pip install tqdm
"$VENV_DIR/bin/python" -m pip install numpy
"$VENV_DIR/bin/python" -m pip install Pillow
"$VENV_DIR/bin/python" -m pip install matplotlib


source "$VENV_DIR/bin/activate"
echo "Environnement virtuel active."