@echo off
set PGPASSWORD=Stonebraker
set HOST=127.0.0.1
set USER=postgres
set PORT=65432
set DB=assetexplorer

shift

:here
if not "%0" == "" (
    if "%0" == "-p" (
        set PORT=%1
    )
    if "%0" == "-db" (
        set DB=%1
    )
    if "%0" == "-h" (
        set HOST=%1
    )
    shift
    shift
    goto :here
)
echo.
psql.exe -h %HOST% -U %USER% -p %PORT% %DB%
