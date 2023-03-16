@echo off
setlocal

if "%1" == "activate" (
    .\venv\Scripts\activate
) else if "%1" == "install" (
    .\venv\Scripts\activate
    pip install -r requirements.txt
) else if "%1" == "add" (
    .\venv\Scripts\activate
    set /p package="Enter package name (e.g. django==3.2.9): "
    pip install %package%
    pip freeze > requirements.txt
) else if "%1" == "update" (
    .\venv\Scripts\activate
    pip freeze --exclude-editable > requirements.txt
) else if "%1" == "clean" (
    rmdir /s /q venv
) else (
    echo Usage: venv.bat [command]
    echo.
    echo Commands:
    echo   activate      Activate virtual environment
    echo   install       Install dependencies from requirements.txt
    echo   add           Add a package to requirements.txt
    echo   update        Update requirements.txt with latest package versions
    echo   clean         Delete virtual environment
)

endlocal
