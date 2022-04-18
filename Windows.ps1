# ChocoInstallBase.ps1 by Q (forked from atwork.at)
# Get Chocolatey
Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

# See packages at https://chocolatey.org/packages/
# Comment (add #) or uncomment (remove #) to include or exclude from your base install
# Use according to your own needs...

# Essentials
choco install firefox -y


