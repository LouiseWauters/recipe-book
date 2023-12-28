#!/bin/bash

cd ~/Documenten/program/food/recipe-book

source .venv/bin/activate
python3 backend/src/main.py
export FLASK_APP=./backend/src/main.py
python3 -m flask run
deactivate

