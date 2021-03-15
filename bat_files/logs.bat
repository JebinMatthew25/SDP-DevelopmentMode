@echo off
echo.
call init.bat
set BUILDDIR=%BUILDS_BIR%\%1\AdventNet\ME\ServiceDesk\logs
REM call code %BUILDDIR%
explorer %BUILDDIR%
exit