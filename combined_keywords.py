import json

combined_list = []
with open('osra_keywords.json', 'r') as f:
    osra_dict = json.load(f)
    osra_list = list(osra_dict.keys())
with open('sst_keywords.json', 'r') as f:
    sst_list = json.load(f)

for sst in sst_list:
    if sst not in combined_list:
        combined_list.append(sst)

for osra in osra_list:
    if osra not in combined_list:
        combined_list.append(osra)

with open('keywords.json', 'w') as f:
    combined_list.sort()
    json.dump(combined_list, f)
