import json
from io import StringIO
from RePoE import load_json
from RePoE import gems, gem_tags, cost_types, base_items, item_classes, tags

# let's get this shit started

def main():

    infoReqInput = input("Please enter your PoE info request here: ")
    infoReqInputRaw = infoReqInput.split(" ", 1)
    objectTypeReq = str(infoReqInputRaw[0])
    objectReq = str(infoReqInputRaw[1])
    poeTypeJson = open(str("C:\Users\75JWHEELER\Documents\GitHub\RePoE\RePoE\data" + objectTypeReq + ".json"))
    print(poeTypeJson)

if __name__ == "__main__":
    main();