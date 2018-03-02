import os
import os.path
import shutil
import  re
pwd=os.getcwd()
print("now locate is :{}".format(pwd))
print("we want to copy topdesk/*.py to github/python/")
os.chdir(r"C:\Users\SH-NB-0012\Desktop\源码")
pwdparent=os.getcwd()
#listdir=os.listdir(pwdparent)
listdir=os.walk(pwdparent)

for path,dirs,files in listdir:
    #print(file)
   for filename in files:
        if re.match("\S+.py",filename):
            print(filename)


        #if x.endswith('.py'):
 #           print(i)
#shutil.copyfile(pwd+"\\"+"11.JPEG",pwdparent+"\\"+"22.JPEG")