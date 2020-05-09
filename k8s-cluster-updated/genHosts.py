# This program generates hosts file, which will be used by ansible to 
# create K8S. In fact this program can be used prepare hosts file from the Terrafrom output.
# Input file : hostsIn
# Output file : hosts
# Based on your program you may need to chage the path of the input and output files
# I assumed current directory as path for input and output files.

from string import Template
from os import path
masterHdr = "[masters]"+"\n"
masterTemplate = Template('master ansible_host=$ip ansible_user=ubuntu')
workerTemplate = Template('worker$num ansible_host=$ip ansible_user=ubuntu')
workerHdr = "[workers]"+"\n"

genericString1 = "[all:vars]"
genericString2 = "ansible_python_interpreter=/usr/bin/python3"
def genHosts():
    if (path.isfile('hostsIn')):
       print("host file exists")
    else:
       print("hosts file deos not exists!!!")
       return
    
    ifh = open ("hostsIn", "r")
    ofh = open ("hosts", "w")
    count = 0;
    for ips in ifh:
        #print (ips)
        if count == 0:
            print (masterHdr)
            ofh.write(masterHdr)
            ofh.write(masterTemplate.substitute(ip=ips.rstrip())+"\n")
            #print(masterTemplate)
            ofh.write (workerHdr)
        else:
            ofh.write (workerTemplate.substitute(num=count, ip=ips.rstrip())+"\n")
            #print (workerTemplate)
        count = count + 1   

    ofh.write (genericString1+ "\n")
    ofh.write (genericString2+ "\n")
    ofh.close () 
if __name__== "__main__":
    genHosts()
