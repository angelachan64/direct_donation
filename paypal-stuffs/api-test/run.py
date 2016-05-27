import subprocess

TransactionSearch="""shell=true
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
SearchCall = subprocess.check_output(
    TransactionSearch % (USER, PWD, SIGNATURE, STARTDATE, ENDDATE),
    shell=True)
print "end"

def parse_call(call):
    d = {}
    d["transactionids"] = []
    for x in call.split("&"):
        data = x.split("=")
        if ("TRANSACTIONID" in data[0]):
            d["transactionids"].append( data[1] )
        d[ data[0] ] = data[1]
    return d

#print parse_call(SearchCall)
#print parse_call(SearchCall)["transactionids"]


GetTransactionDetails="""shell=true
curl https://api-3t.sandbox.paypal.com/nvp \
  -s \
  --insecure \
  -d USER=%s \
  -d PWD=%s \
  -d SIGNATURE=%s \
  -d METHOD=GetTransactionDetails \
  -d VERSION=78 \
  -d TRANSACTIONID=%s  
""" 
#USER="57leonardo-business_api1.gmail.com"
#PWD="QKQPM775NKL7K3T7"
#SIGNATURE="AgW.b-MmQ57G6jhdeFUMgx5wzIAbAiuDgpPYcm2mdI-X34PSFLi4DI9M"
TRANSACTIONID=parse_call(call)["transactionids"][0]

DetailCall = subprocess.check_output(
    GetTransactionDetails % (USER, PWD, SIGNATURE, TRANSACTIONID),
    shell=True)

#print parse_call(DetailCall)

for x in parse_call(DetailCall):
    print str(x) + ": " + str(parse_call(DetailCall)[x])


    
    
#First Name, Last Name, Email, Amount, Currency Code, TimeStamp, PAYMENT STATUS
