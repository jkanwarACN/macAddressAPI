import requests
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('--macAddress', default="44:38:39:ff:ef:57")
parser.add_argument('--APIKey',default="at_bjTuKmrOPxMtZiEsduCPwLbAVheqU")

args = parser.parse_args()

def main():
    url = 'https://api.macaddress.io/v1?apiKey={}&output=json&search={}'.format(args.APIKey,args.macAddress)
    resp = requests.get(url)
    jsonResp = resp.json()
    companyName = jsonResp['vendorDetails']['companyName']
    outputMsg = '{} is the company name associated with the input MAC address; {}'.format(companyName, args.macAddress)
    print outputMsg
    # if(resp == 200){
    #     print resp.text
    # }else{
    #     print "Non-200 code returned.  Received code {}".format(response)
    # }



if __name__ == '__main__':
   main()