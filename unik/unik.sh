#!/bin/bash
# run: ./unik.sh a.txt b.txt
# takes a list a and list b and returns a list of all elements in a that are not in b

list_a="$1"
list_b="$2"

sort "$list_a" -o "$list_a.sorted"
sort "$list_b" -o "$list_b.sorted"
comm -23 "$list_a.sorted" "$list_b.sorted" > "$list_a.unik"

rm "$list_a.sorted" "$list_b.sorted"