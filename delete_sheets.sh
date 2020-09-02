#!/bin/bash
echo -n "Removing bingo sheets in BINGO/ folder and merged_bingo_sheets.pdf"
cd BINGO/ && rm -rf * && cd .. && rm merged_bingo_sheets.pdf
echo "  ....Done"

echo -n "Removing formatted_playlist.txt"
rm formatted_playlist.txt
echo "  ....Done"

