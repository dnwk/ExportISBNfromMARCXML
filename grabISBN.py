# /usr/bin/python3

import sys
import zipfile
from datetime import datetime
from pymarc import map_xml

filedate = datetime.now().strftime("%Y%m%d")
f = open("isbn"+filedate+".txt", "a")

def print_isbn(r):
    tempISBN=r.isbn()
    print('processing record '+tempISBN, end='\r')
    if tempISBN:
        f.write(tempISBN+"\n")

map_xml(print_isbn, sys.argv[1])
f.close()
print('zipping records', end='\r')
with zipfile.ZipFile("isbn"+filedate+".zip", "w") as myzip:
    myzip.write("isbn"+filedate+".txt")
myzip.close()
print("Done")
# End of grabISBN.py
