#!/usr/bin/env bash

set -euo pipefail

clean() {
  # Remove build artifacts and temporary files
  rm -rf build dist __pycache__ *.egg-info **/*.egg-info *.pyc **/*.pyc reports 2>/dev/null || true
}

qa() {
  # Run static analysis tools
  if command -v flake8 >/dev/null 2>&1; then
    flake8 .
  fi
  python run_pylint.py
}

style() {
  # Format code
  isort .
  black --exclude=".*/*(dist|venv|.venv|test-results)/*.*" .
}

if [[ "$@" == *"clean"* ]]; then
  printf 'Removing build artifacts and temporary files...\n'
  clean
elif [[ "$@" == *"qa"* ]]; then
  printf 'Running static analysis tools...\n'
  qa
elif [[ "$@" == *"style"* ]]; then
  printf 'Running code formatters...\n'
  style
else
  printf 'Usage: %s [clean|qa|style]\n' "$0"
  exit 1
fi

printf 'Done!\n\n'
exit 0