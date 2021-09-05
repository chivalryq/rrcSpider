#!/usr/bin/env bash
source ./venv/bin/activate
PYTHONPATH=.:$PYTHONPATH python ./service/service_main.py