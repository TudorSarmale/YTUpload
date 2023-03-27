import os
import sys
import glob
import threading

threads = []

def up(filename):
	os.system("python3 " + sys.argv[1] + " --file=" + filename + " --title=" + filename + " --privacyStatus=" + sys.argv[3])

os.chdir(sys.argv[2])
for file in glob.glob("*.*"):
	t = threading.Thread(target=up(file))
	threads.append(t)
	t.start()

for thread in threads:
	thread.join()
