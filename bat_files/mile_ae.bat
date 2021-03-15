@echo off
call init.bat
python "%PY_DIR%\installer.py" ae "%BUILDS_DIR%" m %1 %2
