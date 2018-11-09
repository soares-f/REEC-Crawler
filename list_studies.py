import json

with open('reec.json') as f:
    data = json.load(f)


codes = []
for estudio in data['estudio']:
    codes.append(estudio['identificador'])