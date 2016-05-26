import subprocess
print "start"
call = subprocess.check_output("./getIDs.sh", shell=True)
print call
print "end"