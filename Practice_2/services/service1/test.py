import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())
protobufs_path = os.path.abspath("../protobufs")

print(protobufs_path)
# print(os.path.realpath(__file__))
# print(os.getcwd())