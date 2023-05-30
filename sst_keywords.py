import json

sst_list = []
with open('sst_keywords.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line.isupper():
            line = line.title()
        if line != '':
            sst_list.append(line)

with open('sst_keywords.json', 'w') as f:
    json.dump(sst_list, f)
