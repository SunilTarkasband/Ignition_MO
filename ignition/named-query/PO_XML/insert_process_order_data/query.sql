EXEC [dbo].[usp_Insert_SAPAPI_PROCESS_ORDER_DATA]
--INSERT INTO SAPAPI_PROCESS_ORDER_DATA (Client,
  	:Client,
    :Plant,
    :Process_Order,
    :PO_Data_XML,
    :INSPLOT,
    :COLLECTIVE_LEADER,
    :COLLECTIVE_DEPENDENT,
    :COL_ORDER,
    :PO_Data_JSon