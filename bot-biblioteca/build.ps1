$exclude = @("venv", "bot-biblioteca.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot-biblioteca.zip" -Force