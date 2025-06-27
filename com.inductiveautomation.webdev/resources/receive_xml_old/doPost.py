def doPost(request, session):
	# Define logger
	logger = system.util.getLogger('ERP_Integration')
	logger.info('Inbound API request received')
#	logger.info(str(request.keys()))
	
	# get the incoming payload
	data = request['postData']
	
	try:
	
		#generate db insert query
		db_insert = """
			INSERT INTO POC_PAYLOAD (PAYLOAD)
			VALUES (?) 
		"""
		#handle incoming payload
		args = [data]
		
		#insert data to databse and send response to client
		
		row_count = system.db.runPrepUpdate(db_insert, args, 'GlobalTemplateDB')
		print row_count
		if row_count == 1:
			request['servletResponse'].status = 201
			logger.info('Data saved to database')
			
			return { 'json': 'data successully saved'}
			
		else:
			request['servletResponse'].status = 503
			logger.info('Message received but data not saved in DB. Please retry')
			
			return { 'json': 'Message received but data not saved in DB. Please retry'}
			
	except Exception as e:
		request['servletResponse'].status = 501
		
		logger.warn('Data not saved to database')
		logger.error(stre(e))
		
		return { 'json': 'failed to save data'}
		
	