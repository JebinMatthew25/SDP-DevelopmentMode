@echo off
call init.bat
python "%PY_DIR%\portChanger.py" ae "%BUILDS_DIR%" %1 %2 %3 %4
