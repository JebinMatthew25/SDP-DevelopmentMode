@echo off
echo.
call init.bat
set BUILD_DIR=%BUILDS_DIR%\%1
robocopy %BUILD_DIR% %BUILD_DIR%! /e /mt