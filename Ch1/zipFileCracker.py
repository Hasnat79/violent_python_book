#!usr/bin/env python3
import zipfile
import argparse
from threading import Thread
def extractFile(zFile,password):
    try:
        zFile.extractall(pwd=password.encode('utf-8'))
        print(f'[+] Found password: {password}\n')
    except:
        pass
def main(zname, dname):
    z_file=zipfile.ZipFile(zname)
    with open(dname) as pass_file:
        for line in pass_file.readlines():
            password=line.strip('\n')
            t=Thread(target=extractFile,args=(z_file,password))
            t.start()

if __name__ == "__main__":
    parser=argparse.ArgumentParser(usage='zipFileCracker.py ZIPFILE DICTFILE')
    parser.add_argument('zipfile',type=str,metavar='ZIPFILE',help='specify zip file')
    parser.add_argument('dictfile',type=str,metavar='DICTFILE',help='specify dictionary file')
    args=parser.parse_args()
    main(args.zipfile,args.dictfile)