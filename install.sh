#!/bin/bash

echo "Installing pip..."
echo "-------------------------------------------------"
python -m install pip
echo "pip installed successfully"
echo "-------------------------------------------------"
echo "Installing dependencies from requirements.txt"
pip install -r requirements.txt