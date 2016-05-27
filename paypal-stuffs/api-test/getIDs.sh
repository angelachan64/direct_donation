shell=true
curl https://api-3t.sandbox.paypal.com/nvp \
  -s \
  --insecure \
  -d USER=57leonardo-business_api1.gmail.com \
  -d PWD=QKQPM775NKL7K3T7 \
  -d SIGNATURE=AgW.b-MmQ57G6jhdeFUMgx5wzIAbAiuDgpPYcm2mdI-X34PSFLi4DI9M \
  -d METHOD=TransactionSearch \
  -d VERSION=78 \
  -d TRXTYPE=Q \
  -d STARTDATE=2015-01-01T0:0:0 \
  -d ENDDATE=2017-01-03T24:0:0
