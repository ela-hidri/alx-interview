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


codes = ['200', '301', '400', '401', '403', '404', '405', '500']
try:
    pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (.{3}) (\d+)'
    i = 0
    TotalFileSize = 0
    StatusCodes = []

    for x in sys.stdin:
        i += 1
        match = re.match(pattern, x)
        if (match):
            if match.group(1) in codes:
                FileSize = match.group(2)
                addCodes(match.group(1))
                TotalFileSize += int(FileSize)

        if i % 10 == 0:
            print(f'File size: {TotalFileSize}')
            for code, nb in sorted(StatusCodes):
                print(f'{code}: {nb}')
finally:
    print(f'File size: {TotalFileSize}')
    for code, nb in sorted(StatusCodes):
        print(f'{code}: {nb}')
