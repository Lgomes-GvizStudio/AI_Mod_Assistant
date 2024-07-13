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


#function to clear powershell----------------------------------------
function clear-ps{

#Set the foreground color (text color)
$host.UI.RawUI.ForegroundColor = 'Yellow'

#Set the background color
$host.UI.RawUI.BackgroundColor =  'Black'

#Clear the screen to apply the background color change
Clear-Host

}

clear-ps

#function to display banner----------------------------------------------------------

function display-banner{

# Define the banner text
$bannerText = @"
--------------------------------------------------------------------------------
   ___   ____  __  _______  ___    ___   _________________________   _  ________
  / _ | /  _/ /  |/  / __ \/ _ \  / _ | / __/ __/  _/ __/_  __/ _ | / |/ /_  __/
 / __ |_/ /  / /|_/ / /_/ / // / / __ |_\ \_\ \_/ /_\ \  / / / __ |/    / / /   
/_/ |_/___/ /_/  /_/\____/____/ /_/ |_/___/___/___/___/ /_/ /_/ |_/_/|_/ /_/  
--------------------------------------------------------------------------------                                                                                
Game : CYBERPUNK2077
AI Model : LLama3
Version : 1.0.0
Author : Lgomes_GvizStudio
--------------------------------------------------------------------------------                                                                                                                                                                                                                                                                        
"@
# Display the banner
Write-Host $bannerText -ForegroundColor Cyan
Write-Host "*"
Write-Host "This script is running with administrative privileges!" -ForegroundColor Cyan
Write-Host "*"

}

# Function to display the menu
function Show-Menu {
    Write-Host "Select an option:" -ForegroundColor Cyan
    Write-Host "1. Run Model" -ForegroundColor Red
    Write-Host "2. GitRepo " -ForegroundColor Red
    Write-Host "3. System " -ForegroundColor Red
    Write-Host "4. Exit" -ForegroundColor Red
}

# Function to handle menu selection
function Handle-Selection {
    param (
        [string]$selection
    )

    switch ($selection) {
        "1" {
             Write-Host "*"
            Write-Host "Starting Lamma3.cyberpunk2077modAssistant" -ForegroundColor Yellow
            

            ollama create Lamma3.cyberpunk2077modAssistant -f Lamma3.cyberpunk2077modAssistantFile 
            ollama run Lamma3.cyberpunk2077modAssistant

            Write-Host "*"
            clear-ps
        }
        "2" {
            Write-Host "Opening GitRepository" -ForegroundColor Yellow
        }
        "3" {
            clear-ps

            Write-Host "System Info" -ForegroundColor Yellow
            Write-Host "*"
            python --version
            ollama --version
            Write-Host "*"
            
        }
        "4" {
            Write-Host "Exiting..." -ForegroundColor Red
            exit
        }

        
        
        default {
            Write-Host "Invalid selection. Please try again." -ForegroundColor Red
        }
    }
}

# Main script loop
while ($true) {
    display-banner
    Show-Menu
    $userInput = Read-Host "----------->"
    Handle-Selection -selection $userInput
    Write-Host ""
}

# Prevent the script from closing automatically
Write-Host "Press Enter to exit" -ForegroundColor Cyan
Read-Host -Prompt ""
'''

# Define the path where the PowerShell script will be saved
powershell_script_path = os.path.join(os.getcwd(), 'script.ps1')

# Create the PowerShell script
create_powershell_script(powershell_script_content, powershell_script_path)

# Run the PowerShell script with administrative privileges
run_powershell_script_as_admin(powershell_script_path)
