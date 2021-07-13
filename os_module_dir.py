import os

os.chdir("C:/Users/jiho3/PycharmProjects/jumptopython")
os.system("dir")
f = os.popen("dir")
print(f.read())