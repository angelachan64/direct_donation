import subprocess
import urllib

print "start"


#######################################################
# CHANGE THE FOLLOWING INFO FOR EVERY INDIVIDUAL USER #
#######################################################

USER=""
PWD=""
SIGNATURE=""

STARTDATE="2015-01-01T0:0:0"
ENDDATE="2017-01-03T24:0:0"

def setParams(user, pwd, signature):
    global USER
    USER = user
    global PWD
    PWD = pwd
    global SIGNATURE
    SIGNATURE = signature



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

SearchCall = subprocess.check_output(
    TransactionSearch % (USER, PWD, SIGNATURE, STARTDATE, ENDDATE),
    shell=True)

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



def getStats():
    ret = []
    for i in parse_call(SearchCall)["transactionids"]:
        TRANSACTIONID=i
        DetailCall = subprocess.check_output(
            GetTransactionDetails%(USER, PWD, SIGNATURE, TRANSACTIONID),
            shell=True)
        results = parse_call(DetailCall)
        #for x in results:
        #     print str(x) + ": " + str(results[x])
        #print results
    
        #We Want: First Name, Last Name, Email, Amount, Currency Code, TimeStamp, Payment Status
        if (results["ACK"] == "Success"):
            output = {}
            output["firstname"] = results["FIRSTNAME"]
            output["lastname"] = results["LASTNAME"]
            output["email"] = results["EMAIL"]
            output["amount"] = results["AMT"]
            output["currencycode"] = results["CURRENCYCODE"]
            output["timestamp"] = results["TIMESTAMP"]
            output["paymentstatus"] = results["PAYMENTSTATUS"]
            output["ack"] = results["ACK"]
            output["addstatus"] = results["ADDRESSSTATUS"]
            output["addowner"] = results["ADDRESSOWNER"]
            ret.append(output)
            #for x in output:
            #    print str(x) + ": " + str(output[x])
            #print
        else:
            ret.append({"Error": "Transaction %s has failed (ACK result: %s)" % (i, results["ACK"])})
    return ret


#print getStats()

def getStatsHTMLTable():
    data = getStats()
    ret = ""
    ret += "<table>"
    labels = ["First Name",
              "Last Name",
              "ACK",
              "Currency Code",
              "Payment Status",
              "Address Status",
              "Amount",
              "Address Owner",
              "Timestamp",
              "Email"]
    ret += "<tr>"
    for l in labels:
        ret += "<th>"
        ret += l
        ret += "</th>"
    ret += "</tr>"
    for a in data:
        #ret += str(a) + "\n\n"
        ret += "<tr>"
        ret += "\n"
        for b in a:
            if (b != "Error"):
                #ret += str(b) + " : " + str( a[b] ) + "\n"
                ret += "<td>"
                ret += str( urllib.unquote(a[b]).decode('utf8') )
                ret += "</td>"
                ret += "\n"
        ret += "</tr>"
        ret += "\n"
    ret += "</table>"
    return ret

print getStatsHTMLTable()

print "end"
