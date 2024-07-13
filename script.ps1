
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
Version : 1.0.0
Author : Lgomes_GvizStudio
--------------------------------------------------------------------------------                                                                                                                                                                                                                                                                        
"@
# Display the banner
Write-Host $bannerText -ForegroundColor Cyan
Write-Host "*"
Write-Host "AI Mod Assistant is running with administrative privileges!" -ForegroundColor Cyan
Write-Host "*"

}

# Function to display the menu
function Show-Menu {
    Write-Host "Select :" -ForegroundColor Cyan
    Write-Host "1. Run Model" -ForegroundColor Red
    Write-Host "2. GitRepository " -ForegroundColor Red
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
            Start-Process "https://github.com/Lgomes-GvizStudio/AI_Mod_Assistant"
            clear-ps
            
        }
        "3" {
            clear-ps

            Write-Host "System Info" -ForegroundColor Yellow
            Write-Host "*"
            python --version
            ollama --version
            Write-Host "Game : CYBERPUNK2077" -ForegroundColor Red
            Write-Host "AI Model : LLama3" -ForegroundColor Red
            
            
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
