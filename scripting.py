import os
from time import time

def current_directory():
    cwd = os.getcwd()
    print(f"Current working directory: {cwd}")
def file_path(filename):
    path = os.path.abspath(filename)
    print(f"Absolute path of {filename}: {path}")

current_directory()
file_path("example.txt")

epc=time.time()
print("Current epoch time:",epc)
local_time=time.localtime(epc)
print("Local time:",local_time)