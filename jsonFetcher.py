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
	level1 = {}
	level2 = {}
	level3 = {}
	f = open("projectLog.txt","w")
	for i in range(0,len(['VPC'])):
		for k,v in jsonInfos.items():
			for m in range(0, len(v)):
				level1 = v[m]
				for k,x in level1.items():
					if type(x[m]) != str:
						print("-------------------------------")
						for t in range(0, len(x)):
							level2 = x[t]
							for k,g in level2.items():
								if type(g) != str:
									for p in range(0, len(g)):
										level3 = g[p]
										for k,s in level3.items():
											print(k+" : "+s)
								else:
									print(k+" : "+g)
					else:
						print(k+" : "+x)
