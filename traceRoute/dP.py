import re
from collections import OrderedDict
def preocessFile():
  fH1 =open('tR1.txt', 'w')

  fHr = open ('traceout.txt', 'r')
  #print(fHr.readlines())
  for item in fHr.readlines():
#    print(item)
    item = re.sub('ms','', item.rstrip())
    item = re.sub('^\s*\d+\s','', item.rstrip())
    item = re.sub('^ ','', item.rstrip())
    if 'trace'  not in item:
      fH1.write(item+ "\n")
  fHr.close()

def findTheIPTakingMoreTime():
  myDict = {}
  fHu = open ('tR1.txt', 'r')
  for item in fHu.readlines():
    item = item.rstrip()  
    v = item.split(' ')
    myList = []
    values = item.split(' ')
    for i1 in values:
      if(i1):
        myList.append(i1)
 #   print(myList)
    for j in range(0,len(myList),2):
      #myDict[myList[j]] = myList[j+1]
      myDict[myList[j]] = float(myList[j+1])
  fHu.close() 
  #print(myDict)      
  #print (max(myDict, key=myDict.get))
  #print (myDict[max(myDict, key=myDict.get)])
  sortedMyDict = dict(sorted(myDict.items(), key=lambda t: t[1], reverse=True))
  #print(sortedMyDict)
  return sortedMyDict

if __name__ == "__main__": 
  # Preprocess the file to remove unwanted characters in the file  
  preocessFile()
  #Conver the date to to dict to find the faulting ips.
  processedDict = findTheIPTakingMoreTime()
  print(list(processedDict.items())[0])
  # find the faulting IP  by checking the

  # If a faulting IP is found run trace route on that.
