@echo off
call init.bat
python "%PY_DIR%\installer.py" sdp "%BUILDS_DIR%" m %1 %2
