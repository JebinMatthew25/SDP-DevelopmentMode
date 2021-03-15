@echo off
call init.bat
python "%PY_DIR%\installer.py" ae "%BUILDS_DIR%" wh %1 %2
