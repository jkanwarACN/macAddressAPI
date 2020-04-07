import requests
import json
import re

macAddrRegexPattern="^([0-9a-f]{2}[:-]){5}([0-9a-f]{2})$"

def main():
    print("Please specify inputs that will be used to query https://macaddress.io/.")
    #Get MAC Address from STDIN
    macAddress = input("Mac Address: ")
    #Pattern match to confirm that a valid Mac Address is passed in
    searchResult = re.search(macAddrRegexPattern, macAddress.lower())
    if( searchResult is None):
        print("Input Mac Address does not match defined hexadecimal standard.  Please enter a Mac Address with pattern similar to the following: 01:23:45:67:89:AB")
        exit(-1)

    # Get API Key from STDIN
    apiKey = input("API Key: ")

    #Query https://api.macaddress.io using the passed API Key and Mac Address
    url = 'https://api.macaddress.io/v1?apiKey={}&output=json&search={}'.format(apiKey,macAddress)
    resp = requests.get(url)
    if(resp.status_code != 200):
        print("{} response received from https://api.macaddress.io, please confirm that you have specified a valid API Key".format(resp.status_code))
        exit(-1)

    #Handle Response and Extract Company Details
    jsonResp = resp.json()
    companyName = jsonResp['vendorDetails']['companyName']

    #Output Message
    outputMsg = '{} is the company name associated with the input MAC address; {}'.format(companyName, macAddress)
    print(outputMsg)



if __name__ == '__main__':
   main()