#!/bin/bash

if [ "$#" -lt 2 ]; then
    echo "Error: Wrong arguments. Run the script as follows: ./kollision.sh -f <file>"
    exit 1
fi

if [ ! -e "$2" ] || [ ! -f "$2" ]; then
    echo "Error: $2 does not exist or is not a regular file. Aborting."
    exit 1
fi

while [[ "$#" -gt 0 ]]; do
    case $1 in
        -f) FILE="$2"; shift ;;
        *) echo "Unknown parameter: $1"; exit 1 ;;
    esac
    shift
done

ALGORITHMS="md5 sha1 sha256 sha512 whirlpool"

echo -e "🔗 Calculating hashes for: \033[1m$FILE\033[0m"

for algo in $ALGORITHMS; do
    HASH=$(openssl dgst -"$algo" "$FILE" | cut -d ' ' -f2)
    ALGO=$(echo "$algo" | tr '[:lower:]' '[:upper:]')

    if [ "${#algo}" -gt 6 ]; then
        echo -e "\033[1m$ALGO:\033[0m\t\033[32m$HASH\033[0m"
    else
        echo -e "\033[1m$ALGO:\033[0m\t\t\033[32m$HASH\033[0m"
    fi
done