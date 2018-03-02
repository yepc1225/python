import os
import shutil
pwd=os.getcwd()
print("now locate is :{}".format(pwd))
print("we want to copy 11.JPEG to parentfile")
os.chdir("../")
pwdparent=os.getcwd()
shutil.copyfile(pwd+"\\"+"11.JPEG",pwdparent+"\\"+"22.JPEG")