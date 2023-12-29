#!/bin/bash

cd ~/Documenten/program/food/recipe-book

source .venv/bin/activate
export FLASK_APP=./backend/src/main.py
python3 -m flask run
deactivate

