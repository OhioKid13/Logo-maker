@echo off

rem Check if Python is installed from the Microsoft Store
python -c "import sys; sys.exit('Microsoft Store' in sys.version)"

rem If Python is installed from the Microsoft Store, update it
if %ERRORLEVEL% EQU 0 (
    echo Python is installed from the Microsoft Store. Updating...
    python -m pip install --upgrade pip
    python -m pip install --upgrade setuptools
    python -m pip install --upgrade wheel
    python -m pip install --upgrade -r requirements.txt
    echo Python updated successfully.
) else (
    rem If Python is not installed from the Microsoft Store, prompt the user to install it
    echo Seems like Python is not installed from the Microsoft Store.
    set /p choice=Would you like to install it from the Microsoft Store? (y/n): 
    if /i "%choice%" EQU "y" (
        start ms-windows-store://pdp/?productid=9p7qfqmjrfp7
    ) else (
        echo Python installation skipped.
    )
)
