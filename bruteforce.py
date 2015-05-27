import rarfile
from threading import Thread
import optparse


rarfile.UNRAR_TOOL="unrar.exe"


def extractFile(rFile,password):
    try:
        rFile.extractall(pwd=password)
        print "Password found! password is %s"%password
    except:
        pass


def main():
    parser = optparse.OptionParser("usage%prog -f <rarfile> -d <dictionary>")
    parser.add_option('-f', dest='rname', type='string', help='specify rar file')
    parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
    (options, args) = parser.parse_args()
    if (options.rname == None) or (options.dname == None):
        print parser.usage
        exit(0)
    else:
        rname = options.rname
        dname = options.dname
    rFile = rarfile.RarFile(rname)
    passFile = open(dname)
    for line in passFile.readlines():
        password = line.strip('\n')
        extractFile(rFile,password)
        #uncomment below lines if you want to use multiple threads
        #t = Thread(target=extractFile, args=(rFile,password))
        #t.start()


if __name__=='__main__':
    main()
    
