@echo off

rem Check if pip is installed
where /Q pip > nul
if %errorlevel% neq 0 (
echo Error: pip is not installed. Please install it and try again.
exit /b 1
)

rem Install pygame and PyOpenGL
pip install pygame PyOpenGL

rem Check if the modules were installed successfully
python -c "import pygame" > nul 2>&1
if %errorlevel% neq 0 (
echo Error: pygame could not be installed. Please try again.
exit /b 1
)

python -c "import OpenGL" > nul 2>&1
if %errorlevel% neq 0 (
echo Error: PyOpenGL could not be installed. Please try again.
exit /b 1
)

echo All required modules have been installed successfully.