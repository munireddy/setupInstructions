import urllib
import time
import datetime, threading
from bs4 import BeautifulSoup
import subprocess
import socket
url_args = "https://www.google.com/"
import requests
import sys
import re
from  dP import preocessFile, findTheIPTakingMoreTime

fp2=open("output.txt",'w')
fH1 =open('tR1.txt', 'w')
def Traceroute_wget():
    try:
        r= requests.get(url_args)
        print("################### URL content #####################")
        #print(r.text)
        print("################### Response code ###################")
        print("Response Code:  "+ str(r.status_code))
        print("Elapsed Time:  "+ str(r.elapsed.total_seconds()))
        if (r.elapsed.total_seconds() > 0.1):
            print("Time taken is more than 5 seconds")
            traceRouteMethod(r)
            return "TraceRouteCalled"
            # Call traceroute method
        else:
            print ("No Action needed as the time taken is less than 5 seconds")
            return "NOTRACEROUTE"

    except:
        # Call Traceroute method
        traceRouteMethod(r)
        return "TraceRouteCalled"

    if (r.elapsed.total_seconds() > 5):
        # Call Traceroute
        traceRouteMethod()
        return "TraceRouteCalled"


      def traceRouteMethod(r):
    # Detect a situation when Error is detected from response of get call.
    hostname="9.47.85.23"
    fp2.write("Status code:          "+str(r.status_code)+"\n")
    fp2.write(hostname+"    :   \n")
    subprocess.call(['traceroute',hostname])
    #traceroute = subprocess.Popen(["traceroute", '-w', '100',hostname],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #traceroute = subprocess.Popen(["traceroute", '-w', '5', '-m', '19', '-n', hostname],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    fileHandle = open ('traceout.txt', 'w')
    traceroute = subprocess.Popen(["traceroute", '-w', '4', '-m', '19', '-n', hostname],stdout=fileHandle)
    #while (True):
    #   hop = traceroute.stdout.readline()
    #   print(hop)
    #   if not hop:
    #       break
    #   fp2.write(str(hop))
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    fileHandle.close()
    fHr = open ('traceout.txt', 'r')
    #print(fHr.readlines())
    for item in fHr.readlines():
        print(item)
        item = re.sub('ms','', item.rstrip())
        fH1.write(item)
    fHr.close()
    time.sleep(5)
    #threading.Timer(5, Traceroute_wget).start() #Ensures periodic execution of TraceRoute( ) x=60*50 seconds

if __name__ == "__main__":
    rV = Traceroute_wget()
    if (rV == "TraceRouteCalled"):
        print("TraceRoute is called execute further steps in the algorithm")
        # Preprocess the file to remove unwanted characters in the file
        preocessFile()
        # Conver the date to to dict to find the faulting ips.
        processedDict = findTheIPTakingMoreTime()
        print(list(processedDict.items())[0])
        # find the faulting IP  by checking the

        # If a faulting IP is found run trace route on that
        
