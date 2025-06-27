import pprint

def odata_api():
	#Http client
	client = system.net.httpClient() 
	headers = {"Authorization": "Basic TUxTRkZJX1JGQzo4aGpramhrdyU3OFQ="}
	url = "https://v41ixp00.na.ko.com:4300/sap/opu/odata4/sap/api_whse_availablestock/srvd_a2x/sap/warehouseavailablestock/0001/WarehouseAvailableStock?sap-client=030"
	response = client.get(url=url, headers=headers)
	results = response.getText()
	decodedDict = system.util.jsonDecode(results)
	pprint.pprint(decodedDict)
	return decodedDict
	
	
#check api response
#	if response.isGood:
#		print ("API Call Success with Code "+ str(response.getStatusCode()))
#		pprint.pprint (decodedDict)
#	else:
#		print "API Call Failed"