# Required libs 'flask', 'flask_cors', 'colorama', 'requests'
# this script will install necessary libraries
Write-Host 'Installing python library: Flask' -ForegroundColor Green
Invoke-Expression "pip install flask"

Write-Host 'Installing python library: flask_cors' -ForegroundColor Green
Invoke-Expression "pip install flask_cors"

Write-Host 'Installing python library: colorama' -ForegroundColor Green
Invoke-Expression "pip install colorama"

Write-Host 'Installing python library: requests' -ForegroundColor Green
Invoke-Expression "pip install requests"
