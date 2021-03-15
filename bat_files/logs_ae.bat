@echo off
echo.
call init.bat
set BUILDDIR=%BUILDS_BIR%\%1\AdventNet\ME\AssetExplorer\logs
REM call code %BUILDDIR%
explorer %BUILDDIR%
exit
