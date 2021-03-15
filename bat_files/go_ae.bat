@echo off
echo.
call init.bat
set BUILDDIR=%BUILDS_DIR%\%1\AdventNet\ME\AssetExplorer
explorer.exe %BUILDDIR%
exit
