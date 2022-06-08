# /usr/bin/python3

import sys
from zipfile import ZipFile, ZIP_DEFLATED
from datetime import datetime
from pymarc import map_xml

filedate = datetime.now().strftime("%Y%m%d")
f = open("isbn"+filedate+".txt", "a")

def print_isbn(r):
    tempISBN=r.isbn()
    print(tempISBN, end='\r')
    if tempISBN:
        f.write(tempISBN+"\n")

map_xml(print_isbn, sys.argv[1])
f.close()
print('zipping records', end='\r')
with ZipFile("isbn"+filedate+".zip", "w", ZIP_DEFLATED, compresslevel=5) as myzip:
    myzip.write("isbn"+filedate+".txt")
myzip.close()
print("Done")
# End of grabISBN.py
