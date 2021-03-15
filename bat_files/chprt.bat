@echo off
call init.bat
python "%PY_DIR%\portChanger.py" sdp "%BUILDS_DIR%" %1 %2 %3 %4
