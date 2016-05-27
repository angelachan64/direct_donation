import subprocess


script="""shell=true
curl https://api-3t.sandbox.paypal.com/nvp \
  -s \
  --insecure \
  -d USER=%s \
  -d PWD=%s \
  -d SIGNATURE=%s \
  -d METHOD=TransactionSearch \
  -d VERSION=78 \
  -d TRXTYPE=Q \
  -d STARTDATE=%s \
  -d ENDDATE=%s
""" 
USER="57leonardo-business_api1.gmail.com"
PWD="QKQPM775NKL7K3T7"
SIGNATURE="AgW.b-MmQ57G6jhdeFUMgx5wzIAbAiuDgpPYcm2mdI-X34PSFLi4DI9M"
STARTDATE="2015-01-01T0:0:0"
ENDDATE="2017-01-03T24:0:0"



print "start"
call = subprocess.check_output(script % (USER, PWD, SIGNATURE, STARTDATE, ENDDATE), shell=True)
print "end"

def parse_call(call):
    d = {}
    for x in call.split("&"):
        data = x.split("=")
        d[ data[0] ] = data[1]
    return d

print parse_call(call)
