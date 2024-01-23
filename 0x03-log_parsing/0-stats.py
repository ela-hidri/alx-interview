#!/usr/bin/python3
""" solving Log Parsing """
import sys
import re
def addCodes(code):
    if code is not None or isinstance(code, int):
        for nb, (stCode, count) in enumerate(StatusCodes):
            if stCode == code:
                StatusCodes[nb] = (stCode, count + 1)
                return
        StatusCodes.append((code, 1))
pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[([^\]]+)\] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$'
i = 0
TotalFileSize = 0
StatusCodes = []
for x in sys.stdin:
    i += 1
    match = re.match(pattern, x)
    if (match):
        FileSize = match.group(4)
        addCodes(match.group(3))
        TotalFileSize += int(FileSize)

    if i == 10:
        print(f'File size: {TotalFileSize}')
        for code,nb in sorted(StatusCodes):
            print(f'{code}: {nb}')
        i = 0




    
    
