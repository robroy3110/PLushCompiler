#!/bin/bash

# Verifica se pelo menos um argumento foi passado
if [ $# -eq 0 ]; then
    echo "Uso: plush.sh [--tree] <arquivo.pl>"
    exit 1
fi

# Caminho para o diretório src
SRC_DIR="$(dirname "$0")/src"

# Verifica se a flag --tree foi passada
TREE_FLAG=false
for arg in "$@"; do
    if [ "$arg" == "--tree" ]; then
        TREE_FLAG=true
    fi
done

# Arquivo PLush (assume que é o último argumento)
PLUSH_FILE="${!#}"

# Executa o compilador
if [ "$TREE_FLAG" = true ]; then
    python3 "$SRC_DIR/main.py" --tree "$PLUSH_FILE"
else
    python3 "$SRC_DIR/main.py" "$PLUSH_FILE"
fi