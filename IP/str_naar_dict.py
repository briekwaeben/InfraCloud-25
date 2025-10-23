import json
print(type(net_prefix))
print(type(netmask_prefixes))

###Maak van een dict een str
netmask_pref_str = json.dumps(netmask_prefixes)
print(type(netmask_pref_str))
print(netmask_pref_str)

###Maak van een str een dict
netmask_pref_dict = json.loads(netmask_pref_str)
print(type(netmask_pref_dict))
print(netmask_pref_dict)