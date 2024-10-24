@echo off
:: Define the paths
set "source_file=%~dp0main.py"
set "autostart_folder=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"
set "target_file=%autostart_folder%\main.pyw"
set "launcher_file=%autostart_folder%\launch_main.bat"

:: Copy and rename the main.py to main.pyw in the autostart folder
copy "%source_file%" "%target_file%" /Y

:: Create a launcher batch file that starts the main.pyw
echo @echo off > "%launcher_file%"
echo start "" "%target_file%" >> "%launcher_file%"

echo Files have been copied and launcher created in the autostart folder.
