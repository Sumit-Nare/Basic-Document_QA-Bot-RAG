@echo off
py -m pip install -r requirements.txt
py src\ingest.py
py main.py
pause
