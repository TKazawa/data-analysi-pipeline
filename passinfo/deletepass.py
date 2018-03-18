# coding: UTF-8
import sys
import os
import shutil
import re
psbkpath=r'../../passbk'
pscandidates=['pass=','password=','pswd=','passwd=','passwd=']
def checkarg(num):
 
 args=sys.argv
 if len(args)==1:
#  print '因数はありません'
  print " type python deletepass.py pass-file"
  return False
 for n in range(1,num+1):
  print args[n]
 return args


if not os.path.isdir(psbkpath):
 os.mkdir(psbkpath)
args=checkarg(1)
if not os.path.isfile(args[1]):
 print 'This is not a  file'
 sys.exit()
shutil.copy(args[1],psbkpath)
f=open(args[1],'r+')
texts=f.readlines()
for num in range(0,len(texts)-1):
# split(f[num],'=')
 for pscand in pscandidates:

  pat=r'^.*'+pscand+r'(.*)$'
#  print pat
  r=re.compile(pat)
  m=r.search(texts[num])
#  m=re.search(pat,texts[num])
  if m is not None: 
   texts[num]=texts[num].replace(m.group(1),'xxx')
f.writelines(texts)
f.close()




