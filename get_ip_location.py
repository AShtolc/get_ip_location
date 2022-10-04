import requests
import os
import subprocess
import time
import pandas as pd
import numpy as np

df = pd.DataFrame()
df.insert(0, 'ripe','')
df.insert(1, 'apnic','')
df.insert(2, 'arin','')
df.insert(3, 'lacnic','')
df.insert(4, 'afrinic','')
f_obj=open("ip.txt")
n=0
for line in open('ip.txt', 'r'):
	n += 1
print(n)
x=range(n)
print(df.head())
n+=1
k=0
list_ripe=list(x)
list_apnic=list(x)
list_arin=list(x)
list_lacnic=list(x)
list_afrinic=list(x)
for i in range (1,n):
	ip=f_obj.readline()[:-1]
	arg=('whois -B --sources RIPE ' +ip+' | grep country | sort |uniq') 
	result=subprocess.Popen(arg,shell=True, stdout=subprocess.PIPE)
	out=result.stdout.readlines()
	print (out)
	list_ripe[k]=out
	arg=('whois -h wq.apnic.net ' +ip+' | grep country|sort |uniq')
	result=subprocess.Popen(arg,shell=True, stdout=subprocess.PIPE)
	out=result.stdout.readlines()
	list_apnic[k]=out
	arg=('whois -h whois.arin.net ' +ip+' | grep country | sort |uniq')
	result=subprocess.Popen(arg,shell=True, stdout=subprocess.PIPE)
	out=result.stdout.readlines()
	list_arin[k]=out
	arg=('whois -h whois.lacnic.net ' +ip+' | grep country | sort |uniq')
	result=subprocess.Popen(arg,shell=True, stdout=subprocess.PIPE)
	out=result.stdout.readlines()
	list_lacnic[k]=out
	arg=('whois -h whois.afrinic.net ' +ip+' | grep country | sort |uniq')
	result=subprocess.Popen(arg,shell=True, stdout=subprocess.PIPE)
	out=result.stdout.readlines()
	list_afrinic[k]=out
	k=k+1
	time.sleep(0)
df.ripe = list_ripe
df.apnic = list_apnic
df.arin = list_arin
df.lacnic= list_lacnic
df.afrinic= list_afrinic
with open('lonew.txt', "w") as new:
		df.to_csv(new, sep='\t',index=False)