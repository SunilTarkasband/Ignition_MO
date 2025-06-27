def doPost(request, session):
	import xml.etree.ElementTree as ET
	# Define logger
	logger = system.util.getLogger('ERP_Integration')
	logger.info('Inbound API request received')

# Get the incoming payload
	data = request['postData']
	xml_data= request['postData']
	try:
	    # Parse the XML data
	    root = ET.fromstring(xml_data)
	    
	    # Extract data from XML
	    edi_dc40 = root.find('.//EDI_DC40')
	    payload_data = {
	        'TABNAM': edi_dc40.find('TABNAM').text,
	        'MANDT': edi_dc40.find('MANDT').text,
	        'DOCNUM': edi_dc40.find('DOCNUM').text,
	        'DOCREL': edi_dc40.find('DOCREL').text,
	        'STATUS': edi_dc40.find('STATUS').text,
	        'DIRECT': edi_dc40.find('DIRECT').text,
	        'OUTMOD': edi_dc40.find('OUTMOD').text,
	        'IDOCTYP': edi_dc40.find('IDOCTYP').text,
	        'MESTYP': edi_dc40.find('MESTYP').text,
	        'SNDPOR': edi_dc40.find('SNDPOR').text,
	        'SNDPRT': edi_dc40.find('SNDPRT').text,
	        'SNDPRN': edi_dc40.find('SNDPRN').text,
	        'RCVPOR': edi_dc40.find('RCVPOR').text,
	        'RCVPRT': edi_dc40.find('RCVPRT').text,
	        'RCVPRN': edi_dc40.find('RCVPRN').text,
	        'CREDAT': edi_dc40.find('CREDAT').text,
	        'CRETIM': edi_dc40.find('CRETIM').text,
	        'SERIAL': edi_dc40.find('SERIAL').text
	    }
	    e1afkol = root.find('.//E1AFKOL')
	    e1afkol_data= {
	    'PRUEFLOS': e1afkol.find('PRUEFLOS').text
	    }
	    # Log extracted values
	    logger.info('Extracted values:'+ str(payload_data['IDOCTYP']))
	    jsonstr = Convert_XML_to_JSon.XML_to_Json(xml_data)
	    logger.info('Extracted values:'+ str(jsonstr))
	    # Generate db insert query
	    db_insert = """
	        INSERT INTO POC_PAYLOAD (PAYLOAD2)
	        VALUES (?,?) 
	    """
	    params = {
    'Client': str(payload_data['MANDT']),
    'Plant': '0384',
    'Process_Order': '0010114',
    'PO_Data_XML': xml_data,
    'INSPLOT': str(e1afkol_data['PRUEFLOS']),
    'COLLECTIVE_LEADER': '',
    'COLLECTIVE_DEPENDENT': '',
    'COL_ORDER': '',
    'PO_Data_JSon': jsonstr
			}
	    
		
		# Print the result to the consol
		
	    # Handle incoming payload
	    args = [str(data),str(jsonstr)]
	    # Parse the XML data
	    
	    # Insert data to database and send response to client
	    if len(data)>0:
	    	# Run the query with explicit database connection
	    	result = system.db.runNamedQuery("PO_XML/insert_process_order_data", params)
	    	#print(result)
	    	#row_count = system.db.runPrepUpdate(db_insert,jsonstr, 'GlobalTemplateDB')
	    	logger.info('Row count: '+str(result)+'Data length : '+str(len(data)))
	    	if result == -1 :
		        request['servletResponse'].status = 201
		        logger.info('Data saved to database')
		        return { 'json': 'data successfully saved'+ jsonstr}
		    
	    else:
	        request['servletResponse'].status = 503
	        logger.info('Message received but data not saved in DB. Please retry')
	        return { 'json': 'Message received but data not saved in DB. Please retry' }
	        
	except Exception as e:
	    request['servletResponse'].status = 501
	    logger.error(str(e))
	    logger.warn('Data not saved to database')
	    return { 'json': 'failed to save data' }
	    