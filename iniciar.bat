@echo off
setlocal
cd /d "%~dp0"
title Sonora - Servidor local
where py >nul 2>nul
if %errorlevel%==0 (
  py -3 local_server.py
  goto :eof
)
where python >nul 2>nul
if %errorlevel%==0 (
  python local_server.py
  goto :eof
)
echo Python 3 nao foi encontrado.
echo Instale Python 3 em https://www.python.org/downloads/ e marque "Add Python to PATH".
echo Depois execute este arquivo novamente.
pause
