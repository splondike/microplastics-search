#!/bin/bash

wget -O plastic-table.pdf https://www.beatthemicrobead.org/wp-content/uploads/2019/07/Red-List_new_ECHA.pdf
pdftotext plastic-table.pdf
# Delete leading text
echo -e "No.\n" > plastic-table-modified.txt
sed '0,/^No.$/d' < plastic-table.txt >> plastic-table-modified.txt

# Extract the lines from the table
./extract-csv.py < plastic-table-modified.txt > plastics.txt
