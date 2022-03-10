#!/usr/bin/python3

import sys, getopt


def printUsernames(name0, name1, domain):

    lenName0 = len(name0)
    lenName1 = len(name1)

    for i in range(1,lenName0):
        for j in range(1,lenName1):
            print('{0}{1}{2}'.format(domain,name0[:i], name1[:j]))
    print('{0}{1}{2}'.format(domain,name0, name1))

    for i in range(1,lenName1):
        for j in range(1,lenName0):
            print('{0}{1}{2}'.format(domain,name1[:i], name0[:j]))
    print('{0}{1}{2}'.format(domain,name1, name0))        
    
    for i in range(1,lenName0):
        for j in range(1,lenName1):
            print('{0}{1}.{2}'.format(domain,name0[:i], name1[:j]))
    print('{0}{1}.{2}'.format(domain,name0, name1))

    for i in range(1,lenName1):
        for j in range(1,lenName0):
            print('{0}{1}.{2}'.format(domain,name1[:i], name0[:j]))
    print('{0}{1}.{2}'.format(domain,name1, name0)) 
    

def formatUsernames(user, domain):

    if "@" in user:
        user = user.split("@")[0]

        if "." in user:
            name0 = user.split(".")[0]
            name1 = user.split(".")[1]

    elif "." in user and not "@" in user:
        name0 = user.split(".")[0]
        name1 = user.split(".")[1]
    
    elif " " in user:
        name0 = user.split(" ")[0]
        name1 = user.split(" ")[1]

    printUsernames(name0, name1, domain)
            

def main(argv):
    domain = ''
    username = ''
    
    if len(sys.argv) == 1:
        print('dname.py [-d <domain>] -u <username>')
        sys.exit(2)
    
    try:
        opts, args = getopt.getopt(argv,"hd:u:",["domain=","username="])
    except getopt.GetoptError:
        print('dname.py [-d <domain>] -u username')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('\ndname.py [-d <domain>] -u <username>\n')
            print('Example: dname.py -u "bob.buster"\n', end = '')
            print('Example: dname.py -d contoso -u "bob.buster"\n', end = '')
            print('Example: dname.py -d contoso -u "bob buster"\n', end = '')
            print('Example: dname.py -d contoso -u "bob.buster@contos.com"\n')
            sys.exit()
        elif opt in ("-d", "--domain"):
            domain = arg+"\\"
        elif opt in ("-u", "--username"):
            username = arg
     
    formatUsernames(username, domain)

    
if __name__ == "__main__":
   main(sys.argv[1:])





