def doPost(request, session):
	import xml.etree.ElementTree as ET
	# Define logger
	logger = system.util.getLogger('Live ERP_Integration')
	logger.info('Live Inbound API request received')

# Get the incoming payload
	data = request['postData']
	xml_data= request['postData']
	try:
	    # Parse the XML data
	    root = ET.fromstring(xml_data)
	    
	    # Extract data from XML
	    """edi_dc40 = root.find('.//EDI_DC40')
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
	    }"""
	    e1afkol = root.find('.//E1AFKOL')
	    edi_dc40 = root.find('.//EDI_DC40')
	    e1maram = root.find('.//E1MARAM')
	    
	    if e1afkol is not None:
	    		
	    		identifier=e1afkol.find('AUFNR').text
	    		idoctype= edi_dc40.find('IDOCTYP').text
	    elif e1maram is not None:
	    		
	    		identifier=e1maram.find('MATNR').text
	    		idoctype= edi_dc40.find('IDOCTYP').text
	    else:
	    	return { 'json': 'Message received but incorrect message format. Please retry' }
	  
	    
	    
	    # Log extracted values
	    logger.info('Extracted values:'+ idoctype)
	    jsonstr = Convert_XML_to_JSon.XML_to_Json(xml_data)
	    logger.info('Extracted values:'+ str(jsonstr))
	    # Generate db insert query
	    db_insert = """
	        INSERT INTO POC_PAYLOAD (PAYLOAD2)
	        VALUES (?,?) 
	    """
	    docType=idoctype #str(payload_data['IDOCTYP'])
	    params ={'messageIdentifier':identifier,'docType':docType,'status':'NEW','message':'Success','step':'NEW','payload':xml_data}
	    #params2 ={'messageIdentifier':identifier,'step':'NEW','payload':xml_data}
		
		# Print the result to the consol
		
	    # Handle incoming payload
	    args = [str(data),str(jsonstr)]
	    # Parse the XML data
	    
	    # Insert data to database and send response to client
	    if len(data)>0:
	    	# Run the query with explicit database connection
	    	#result = system.db.runNamedQuery("PO_XML/insert_process_order_data", params)
	    	result = system.db.runNamedQuery("InsertPayloadIntoInboundQueue",params)
	    	#result2 = system.db.runNamedQuery("InsertPayloadIntoInboundPayload",params2)
	    	#print(result)
	    	#row_count = system.db.runPrepUpdate(db_insert,jsonstr, 'GlobalTemplateDB')
	    	logger.info('Row count: '+str(result)+'Data length : '+str(len(data)))
	    	if result == -1 :
		        request['servletResponse'].status = 201
		        logger.info('Data saved to database')
		        return { 'json': 'data successfully saved'+ identifier}
		    
	    else:
	        request['servletResponse'].status = 503
	        logger.info('Message received but data not saved in DB. Please retry')
	        return { 'json': 'Message received but data not saved in DB. Please retry' }
	        
	except Exception as e:
	    request['servletResponse'].status = 501
	    logger.error(str(e))
	    logger.warn('Data not saved to database')
	    return { 'json': 'failed to save data' }
	    