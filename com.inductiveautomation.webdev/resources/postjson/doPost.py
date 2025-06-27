def doPost(request, session):
	# take in some JSON data and print it
	# expecting 'names' and 'values' that are of the same length
	
##	# get the incoming parameters
#	logger = system.util.getLogger("webdev.postjson")
##	some_value = request['params']["some"]
#	logger.infof("This is params.some: %s", some_value)
#	
#	return {"json": {some_value: "good"}}
	data = request['postData']
	names = data['names']
	values = data['values']
	# this will print to the wrapper.log file
	print names, values
	
	# format the string into HTML
	formattedString = "<html><body>"
	# loop through and add names and values
	for i in range(len(names)):
	    formattedString += "%s: %s, " %(names[i], values[i])
	# remove the last ', ' and add closing html
	formattedString = formattedString[:-2]+"</body></html>"
	# this will print to the wrapper.log file
	print formattedString
	
	# return the value string
	return {'html': formattedString}