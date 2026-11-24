@echo off
title Personal Finance Tracker

cd /d "%~dp0"

echo =========================================
echo       PERSONAL FINANCE TRACKER
echo =========================================
echo.

where py >nul 2>&1
if not errorlevel 1 goto use_py

where python >nul 2>&1
if not errorlevel 1 goto use_python

echo Python tidak ditemukan!
echo Pastikan Python sudah terinstal.

:use_py
py -3 main.py
goto selesai

:use_python
python main.py

:selesai
echo.
echo Program telah berhenti.
pause