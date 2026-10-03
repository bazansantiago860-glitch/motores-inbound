while ($true) {
    Write-Host "[$(Get-Date)] Iniciando barrido diario del Motor de Adquisición..."
    $env:PYTHONIOENCODING="utf8"
    python orchestrator.py
    Write-Host "[$(Get-Date)] Barrido finalizado. Durmiendo hasta el próximo ciclo (24 horas)..."
    Start-Sleep -Seconds 86400
}
