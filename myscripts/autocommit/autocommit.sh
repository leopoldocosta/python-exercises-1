# Sobe duas pastas para acessar a raiz do repositório
$repoDir = (Resolve-Path ..\..\).Path
Set-Location $repoDir

# Verifica arquivos novos (não trackeados) e realiza commit
$files = git ls-files --others --exclude-standard
foreach ($file in $files) {
    # Conta o número de linhas do arquivo
    $lineCount = (Get-Content $file | Measure-Object -Line).Lines
    if ($lineCount -ge 20) {
        # Adiciona o arquivo ao tracking do Git
        git add $file
        # Commita o novo arquivo
        git commit -m "Adicionando novo arquivo $file com $lineCount linhas"
    }
}

# Commita alterações em arquivos já trackeados
if ((git status --porcelain) -ne "") {
    git commit -am "Commit automático das mudanças salvas"
}

# Opcional: Descomente essa linha se quiser fazer push automático
# git push
