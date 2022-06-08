import sys
from datetime import datetime
from pymarc import map_xml

def print_isbn(r):
    filedate = datetime.now().strftime("%Y%m%d")
    f = open("isbn"+filedate+".txt", "a")
    tempISBN=r.isbn()
    if tempISBN:
        f.write(tempISBN+"\n")

map_xml(print_isbn, sys.argv[1])