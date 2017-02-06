#Filename: finally.py

import time

try:
    f = file('poem.txt')
    while True: #our usual file-reading idiom
        line = f.readline()
        if len(line) == 0:
            break
        time.sleep(2)
        print line,
finally:
    f.close()
    print '\nCleaning up...closed the file'