import sys

if len(sys.argv) == 1:
	print("USAGE: Python3 app.py <PASSWORD>")
else:
	password = sys.argv[1]
	print("Password", password)