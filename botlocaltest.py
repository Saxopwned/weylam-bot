import requests
import bs4

def main():
    
    poedbURL = str("https://poedb.tw/us/")
    infoReqInput = input("Please enter a Path of Exile information request ") 
    infoReqRaw = (infoReqInput.split(" ", 1))
    infoReq = str(infoReqRaw[1])
    infoReqTypeRaw = str(infoReqRaw[0])

    if infoReqTypeRaw.startswith("!"):
        infoReqType = infoReqTypeRaw.strip("!")
    else:
        print("I'm sorry, that is not a valid input. Please begin the response with !")
    
    if " " in infoReq:
        info_Req = infoReq.replace(" ", "_")
    else:
        info_Req = infoReq

    poedbReqURL = (poedbURL + info_Req)

    if infoReqType == "gem" or "unique" or "mod":
        print("Searching PoE.DB for", info_Req)
    else:
        print("Could not identify the object type of your request")

    print(poedbReqURL)

    
if __name__ == "__main__":
    main();