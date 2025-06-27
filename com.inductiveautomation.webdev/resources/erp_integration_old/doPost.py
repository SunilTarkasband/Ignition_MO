def doPost(request, session):
	# NOT WORKING
	logger = system.util.getLogger('ERP_Integration')
	logger.info('Inbound API request received')
#	logger.info(str(request.keys()))
	
	data = request['postData']
	
	db_insert = """
		INSERT INTO POC_PAYLOAD (PAYLOAD)
		VALUES (?) 
	"""
	args = [data]
	try:
		row_count = system.db.runPrepUpdate(db_insert, args, 'GlobalTemplateDB')
		print row_count
		if row_count == 1:
#			request['servletResponse'].status = 200
#			return { 'json': 'failed to save data'}
			request['status'] = 200
			request['json'] = {'message': 'Operation successful!'}
			logger.info('Data saved to database')
#		else:
			
	except Exception as e:
		request['status'] = 500
        request['json'] = {'error': str(e)}
#		request['servletResponse'].status = 400
#		return { 'json': 'failed to save data'}
#		logger.warn('Data not saved to database')
#		logger.error(stre(e))
	return response	
	