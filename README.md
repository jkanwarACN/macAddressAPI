# macAddressAPI

===Security===

One of the biggest security concerns that I saw with this was leaving my API key embedded in the code.  Doing this in a Production environment could be a major security breach as you are leaving your keys available to anyone that has access to your source code repository.  Because of this, I created another commandline parameter prompt, such that it has to be passed at time of execution.  Another way to handle this would be to leverage some type of secure parameter storage and dynamically pull the values at runtime.


===Docker-Commands===

Feel free to use these docker build and run commands for building and running the container:

	Build
		docker build -t macaddressapi .
	Run
		docker run -it --rm macaddressapi


===Description===

macAddressAPI is used to query https://macaddress.io/ for the company name associated with a MAC Address.  It takes two command line arguemnts before it can execute:

	Mac Adress:
		valid MAC address.  6 bytes are hexadecimal and separated by semi colon or dash characters.

	API Key 
		An API key that allows you to interface with https://macaddress.io/


Complete source can be found [here](https://github.com/jkanwarACN/macAddressAPI).

