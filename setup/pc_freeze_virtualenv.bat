@echo off

:: Change directory to the repository root (script's parent)
pushd "%~dp0.."

:: Activate the virtual environment
call env\Scripts\activate

:: Write all currently installed packages to setup\requirements.txt
echo Writing current packages to setup\requirements.txt...
:: %~dp0 expands to the script directory (with trailing backslash)
pip freeze > "%~dp0requirements.txt"
echo Current packages written to setup\requirements.txt successfully

:: Return to original directory
popd
pause
cmd /k
