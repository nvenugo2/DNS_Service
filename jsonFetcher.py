import json

def _byteify(data, ignore_dicts = False):
    # if this is a unicode string, return its string representation
    if isinstance(data, unicode):
        return data.encode('utf-8')
    # if this is a dictionary, return dictionary of byteified keys and values
    # but only if we haven't already byteified it
    if isinstance(data, dict) and not ignore_dicts:
        return {
            _byteify(key, ignore_dicts=True): _byteify(value, ignore_dicts=True)
            for key, value in data.iteritems()
        }
    # if it's anything else, return it in its original form
    return data

	
with open('customer.json', 'r') as f:
	jsonInfos = _byteify(
        json.load(f, object_hook=_byteify),
        ignore_dicts=True
    )
	#print json.dumps(jsonInfos['VPC'][0]['VPC-name'], sort_keys=True, indent=4)
	for i in range(0, len(['VPC'])+1):
		print(jsonInfos['VPC'][i]['VPC-name'])
		
		
https://stackoverflow.com/questions/35403769/how-to-read-json-file-using-ansible
https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html#json-query-filter
