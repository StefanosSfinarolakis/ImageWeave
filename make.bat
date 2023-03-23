@echo off

REM Define variables
set VENV_NAME=env
set REQUIREMENTS=requirements.txt
set DOCKER_COMPOSE=docker-compose.yml

REM Display help message
if [%1]==[/?] goto :Help
if [%1]==[--help] goto :Help
goto :Start

:Help
echo Usage: make [COMMAND]
echo.
echo Commands:
echo   install         Installs dependencies
echo   setup           Sets up a new virtual environment and activates it
echo   update          Updates the virtual environment and requirements
echo   add             Adds new dependency to requirements.txt
echo   clean           Cleans the virtual environment and removes Docker containers
echo   start           Starts the Django server
echo   stop            Stops the Django server
echo   restart         Restarts the Django server
echo.
echo Example usage:
echo   make install
echo   make setup
echo   make start
echo   make stop
echo   make restart
echo.
goto :End

:Start
REM Check command
if [%1]==[] goto :Help
if [%1]==[install] goto :Install
if [%1]==[activate] goto :Activate
if [%1]==[setup] goto :Setup
if [%1]==[update] goto :Update
if [%1]==[add] goto :AddDependency
if [%1]==[clean] goto :Clean
if [%1]==[start] goto :StartServer
if [%1]==[stop] goto :StopServer
if [%1]==[restart] goto :RestartServer
if [%1]==[migrate] goto :Migrate
if [%1]==[migrations] goto :Makemigrations
goto :Help

:Install
echo Installing dependencies...
python -m venv %VENV_NAME%
call %VENV_NAME%\Scripts\activate.bat
pip install -r %REQUIREMENTS%
echo Install complete.
goto :End

:Activate
call %VENV_NAME%\Scripts\activate.bat
echo Venv Activated.
goto :End

:Setup
echo Setting up virtual environment...
python -m venv %VENV_NAME%
call %VENV_NAME%\Scripts\activate.bat
echo Setup complete.
goto :End

:Update
echo Updating virtual environment...
call %VENV_NAME%\Scripts\activate.bat
pip install -r %REQUIREMENTS%
echo Update complete.
goto :End

:AddDependency
if [%2]==[] goto :HelpAdd
echo Adding dependency %2 to requirements.txt...
echo %2 >> %REQUIREMENTS%
echo Dependency added.
goto :End

:HelpAdd
echo Usage: make add [DEPENDENCY]
echo.
echo Example usage:
echo   make add django
echo   make add requests
echo.
goto :End

:Clean
echo Cleaning virtual environment and Docker containers...
call %VENV_NAME%\Scripts\deactivate.bat
rmdir /s /q %VENV_NAME%
docker-compose -f %DOCKER_COMPOSE% down
echo Clean complete.
goto :End

:StartServer
echo Starting Django server...
call %VENV_NAME%\Scripts\activate.bat
docker-compose -f %DOCKER_COMPOSE% up -d
python manage.py runserver
goto :End

:StopServer
echo Stopping Django server...
call %VENV_NAME%\Scripts\activate.bat
docker-compose -f %DOCKER_COMPOSE% down
goto :End

:RestartServer
echo Restarting Django server...
call %VENV_NAME%\Scripts\activate.bat
docker-compose -f %DOCKER_COMPOSE% restart
goto :End

:Migrate
echo Running Django migrations...
call %VENV_NAME%\Scripts\activate.bat
python manage.py migrate
echo Migrations complete.
goto :End

:Makemigrations
python manage.py makemigrations
echo new migration created
goto:End

:End
