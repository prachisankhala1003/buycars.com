@echo off

:: Set the desired Python version
SET "PYTHON_VERSION=3.12.4"

:: Check if the specified Python version is installed
for /f "tokens=* USEBACKQ" %%F in (`py -%PYTHON_VERSION:~0,4% -V 2^>^&1`) do (
    SET var=%%F
)
if not "%var%"=="Python %PYTHON_VERSION%" (
    echo Python %PYTHON_VERSION% is not installed
  
  echo Installing Python %PYTHON_VERSION%...
    powershell -Command "Invoke-WebRequest https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe -OutFile python-%PYTHON_VERSION%-amd64.exe"
   
python-%PYTHON_VERSION%-amd64.exe /quiet InstallAllUsers=1 PrependPath=1
    del python-%PYTHON_VERSION%-amd64.exe
) else (
    echo Python %PYTHON_VERSION% is installed
)

echo Creating virtual environment in parent directory...
:: Create the virtual environment in the repository root (script's parent)
echo Creating virtual environment in repository root...
pushd "%~dp0.."

:: Create the virtual environment
py -%PYTHON_VERSION:~0,4% -m venv env
echo Virtual environment created successfully

:: Activate the virtual environment and ensure distutils is installed
call env\Scripts\activate
python -m pip install --upgrade pip
python -m pip install setuptools
python -m pip install distlib

:: Ensure repository main directory can be imported
echo Configuring import paths...
SET var=%cd%
ECHO %var% > env/Lib/site-packages/localpackages.pth
echo Import paths configured successfully

:: Install required packages (from this script's folder)
echo Installing required packages from setup\requirements.txt...
:: %~dp0 expands to the script directory (with trailing backslash)
pip install -r "%~dp0requirements.txt"
echo Required packages installed successfully

echo Setup Complete
:: Return to original directory
popd
pause
cmd /k
