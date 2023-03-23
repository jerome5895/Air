import sys
import os

if len(sys.argv) < 2:
    print("Usage: python " + sys.argv[0] + " FILENAME")
    sys.exit()


filename = sys.argv[1]
try:
    with open(filename, 'r') as file:
        data = file.read()
    print(data)
except IOError as e:
    print("Error reading file:", e)
    sys.exit(1)
