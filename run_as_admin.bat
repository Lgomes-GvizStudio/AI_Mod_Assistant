
@echo off
PowerShell -Command "Start-Process PowerShell -ArgumentList '-NoProfile -ExecutionPolicy Bypass -File "C:\Users\gomes\AppData\Local\Programs\Ollama\llm\script.ps1"' -Verb RunAs"
    