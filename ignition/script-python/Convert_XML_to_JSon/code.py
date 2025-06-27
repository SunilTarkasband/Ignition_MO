import xml.etree.ElementTree as ET
import json
	
	
def xml_to_dict(element):
	# Convert an ElementTree element into a dictionary
	node = dict()
	
	# If the element has attributes, add them to the dictionary
	if element.attrib:
	    node.update(element.attrib)
	
	# If the element has text content, add it to the dictionary
	if element.text and element.text.strip():
	    node['text'] = element.text.strip()
	
	# Recursively convert child elements to dictionary
	for child in element:
	    child_dict = xml_to_dict(child)
	    if child.tag not in node:
	        node[child.tag] = child_dict
	    else:
	        if not isinstance(node[child.tag], list):
	            node[child.tag] = [node[child.tag]]
	        node[child.tag].append(child_dict)
	
	return node






def XML_to_Json(xml_str):
	# Parse the XML string into an ElementTree object
	root = ET.fromstring(xml_str)
	
	# Convert the ElementTree object to a dictionary
	xml_dict = {root.tag: xml_to_dict(root)}
	
	# Convert the dictionary to a JSON string
	json_str = json.dumps(xml_dict, indent=4)
	
	return json_str