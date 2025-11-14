@echo off
chcp 65001
title Raid Boyy
echo Downloading Libs
pip install discord.py python-dotenv psutil
echo.
echo Starting
python bot.py
pause