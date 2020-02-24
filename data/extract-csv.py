#!/usr/bin/env python3

import sys

chunks = []

state = 'space'
buff = ''
for line in sys.stdin:
    line_type = 'words'
    if line.strip() == '':
        line_type = 'space'

    if state == 'space' and line_type == 'space':
        pass
    elif state == 'words' and line_type == 'space':
        state = 'space'
        chunks.append(buff.strip())
        buff = ''
    elif state in ('words', 'space') and line_type == 'words':
        state = 'words'
        buff += ' ' + line.strip()


plastics = set()

for chunk in chunks:
    # Don't need the row numbers, page numbers, or table headers
    if chunk.isnumeric() or chunk in ('No.', 'Polymer', 'Source'):
        continue

    # Don't need the source column
    if 'ECHA' in chunk or 'UNEP' in chunk:
        continue

    # This should just be the plastics column

    for plastic in chunk.split("/"):
        plastics.add(plastic.strip())

for plastic in plastics:
    print("%s" % plastic)
