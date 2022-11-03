import json
import csv

with open ("NFT Naming csv - All Teams.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    data = {"NFTs": []}
    
    for row in reader:
        data["NFTs"].append({"Serial Number":row[0], "Filename":row[1], "UUID":row[2]})
        
with open ("Hng.json","w") as f:
    json.dump(data, f, indent=4)