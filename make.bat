@echo off
setlocal

SET PYTHON=python3.9
SET VENV_NAME=venv

if "%1" == "activate" (
    .\%VENV_NAME%\Scripts\activate
) else if "%1" == "install" (
    .\%VENV_NAME%\Scripts\activate
    pip install -r requirements.txt
) else if "%1" == "add" (
    .\%VENV_NAME%\Scripts\activate
    set /p package="Enter package name (e.g. django==3.2.9): "
    pip install %package%
    pip freeze > requirements.txt
) else if "%1" == "update" (
    .\%VENV_NAME%\Scripts\activate
    pip freeze --exclude-editable > requirements.txt
) else if "%1" == "clean" (
    rmdir /s /q %VENV_NAME%
) else if "%1" == "setup" (
    %PYTHON% -m venv %VENV_NAME%
    .\%VENV_NAME%\Scripts\activate
    pip install --upgrade pip
) else if "%1" == "run" (
    .\%VENV_NAME%\Scripts\activate
    start "Django Server" /B cmd /C "python manage.py runserver"
) else if "%1" == "stop" (
    taskkill /IM "python.exe" /FI "WINDOWTITLE eq Django Server*"
) else (
    echo Usage: venv.bat [command]
    echo.
    echo Commands:
    echo   activate      Activate virtual environment
    echo   install       Install dependencies from requirements.txt
    echo   add           Add a package to requirements.txt
    echo   update        Update requirements.txt with latest package versions
    echo   clean         Delete virtual environment
    echo   setup         Create virtual environment with Python 3.9 and install pip
    echo   run           Run Django server in the background
    echo   stop          Stop Django server
)

endlocal

