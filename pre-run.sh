#!/bin/bash

# Check if pip is installed
if ! [ -x "$(command -v pip)" ]; then
  echo "Error: pip is not installed. Please install it and try again." >&2
  exit 1
fi

# Install pygame and PyOpenGL
pip install pygame PyOpenGL

# Check if the modules were installed successfully
if ! python -c "import pygame" &> /dev/null; then
  echo "Error: pygame could not be installed. Please try again." >&2
  exit 1
fi

if ! python -c "import OpenGL" &> /dev/null; then
  echo "Error: PyOpenGL could not be installed. Please try again." >&2
  exit 1
fi

echo "All required modules have been installed successfully."
