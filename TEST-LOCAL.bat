@echo off
title Escape Room Review Tracker v2.2.1 - SINGLE FILE TEST
cd /d "%~dp0"
py server.py
if errorlevel 1 python server.py
pause
