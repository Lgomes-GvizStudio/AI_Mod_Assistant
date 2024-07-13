import os
import subprocess


def create_powershell_script(script_content, script_path):
    with open(script_path, 'w') as file:
        file.write(script_content)

def run_powershell_script_as_admin(script_path):
    # Create a batch file to run PowerShell with administrative privileges
    batch_file_content = f'''
@echo off
PowerShell -Command "Start-Process PowerShell -ArgumentList '-NoProfile -ExecutionPolicy Bypass -File \"{script_path}\"' -Verb RunAs"
    '''
    batch_file_path = os.path.join(os.getcwd(), 'run_as_admin.bat')

    with open(batch_file_path, 'w') as file:
        file.write(batch_file_content)

    # Run the batch file
    subprocess.run(['cmd', '/c', batch_file_path])

# Define the PowerShell script content
powershell_script_content = '''
#  PowerShell script

# Get the current date and time
$currentDateTime = Get-Date

function spacer {
Write-Host "*" -ForegroundColor yellow
}

function Set-ps{
#Set the foreground color (text color)
$host.UI.RawUI.ForegroundColor = 'Cyan'

#Set the background color
$host.UI.RawUI.BackgroundColor =  'Black'
}



function display-banner{
# Define the banner text
$bannerText = 
@"
--------------------------------------------------------------------------------
# # # # # # # # ╔═╗╦  ╔╦╗╔═╗╔╦╗  ╔═╗╔═╗╔═╗╦╔═╗╔╦╗╔═╗╔╗╔╔╦╗# # # # # # # # # # # 
# # # # # # # # ╠═╣║  ║║║║ ║ ║║  ╠═╣╚═╗╚═╗║╚═╗ ║ ╠═╣║║║ ║ # # # # # # # # # # # 
# # # # # # # # ╩ ╩╩  ╩ ╩╚═╝═╩╝  ╩ ╩╚═╝╚═╝╩╚═╝ ╩ ╩ ╩╝╚╝ ╩ # # # # # # # # # # #
--------------------------------------------------------------------------------
Version : 1.0.0 --------------------------------------Author : Lgomes_GvizStudio
--------------------------------------------------------------------------------
"@
# Display the banner
Write-Host $bannerText -ForegroundColor yellow
Write-Host "AI Mod Assistant is running with administrative privileges!" -ForegroundColor Cyan
spacer
}

# Function to display the menu
function Show-Menu {
    Write-Host "Select :" -ForegroundColor Cyan
    Write-Host "1. Create  " -ForegroundColor Red
    Write-Host "2. Start " -ForegroundColor Red
    Write-Host "3. GitRepository " -ForegroundColor Red
    Write-Host "4. Info " -ForegroundColor Red
    Write-Host "5. Exit" -ForegroundColor Red
}

# Function to handle menu selection
function Handle-Selection {
    param (
        [string]$selection
    )

    switch ($selection) {
        "1" {
            Clear-Host

             spacer
             
            Write-Host "> Creating Lamma3.cyberpunk2077modAssistant" -ForegroundColor Yellow

            spacer
            

            ollama create Lamma3.cyberpunk2077modAssistant -f Lamma3.cyberpunk2077modAssistantFile 

            spacer


            Write-Host "> Created Lamma3.cyberpunk2077modAssistant at $currentDateTime" -ForegroundColor Yellow
            


            spacer



        }
        "2" {
             spacer
            Write-Host "> Starting Lamma3.cyberpunk2077modAssistant" -ForegroundColor Yellow
            spacer
            


            ollama run Lamma3.cyberpunk2077modAssistant

            set-ps


            Write-Host "> closed Lamma3.cyberpunk2077modAssistant at $currentDateTime " -ForegroundColor Yellow
            
            

        }
        "3" {
            Write-Host "> Opening GitRepository" -ForegroundColor Yellow

            Start-Process "https://github.com/Lgomes-GvizStudio/AI_Mod_Assistant"
            
            Write-Host "> Opened GitRepository at $currentDateTime  "

            
        }
        "4" {
            

            Write-Host "> System Info" -ForegroundColor Yellow
            spacer
            python --version
            spacer
            ollama --version
            spacer
            Write-Host "Game : CYBERPUNK2077" -ForegroundColor Cyan
            spacer
            Write-Host "AI Model : LLama3" -ForegroundColor Cyan
            
            
            spacer
            
        }
        "5" {
            Write-Host "Exiting..." -ForegroundColor Red
            exit
        }

        
        
        default {
            Write-Host "Invalid selection. Please try again." -ForegroundColor Red
        }
    }
}

# Main script loop

set-ps
Clear-Host

while ($true) {
    
    display-banner
    Show-Menu

    $userInput = Read-Host "----------->"
 
    Handle-Selection -selection $userInput
    Write-Host ""
}

# Prevent the script from closing automatically
Write-Host "Press Enter to exit" -ForegroundColor Red
Read-Host -Prompt ""
'''

# Define the path where the PowerShell script will be saved
powershell_script_path = os.path.join(os.getcwd(), 'script.ps1')

# Create the PowerShell script
create_powershell_script(powershell_script_content, powershell_script_path)

# Run the PowerShell script with administrative privileges
run_powershell_script_as_admin(powershell_script_path)
