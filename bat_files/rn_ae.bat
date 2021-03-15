@echo off
echo.
call init.bat
set BUILD=%1
set BUILDDIR=%BUILDS_DIR%\%BUILD%\AdventNet\ME\AssetExplorer\bin
cd /D %BUILDDIR%
call %BUILDDIR%\run.bat
