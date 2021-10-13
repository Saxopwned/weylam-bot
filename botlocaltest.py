import requests
import bs4

def main():

    poeInfoReq = input("Please enter a Path of Exile information request ") # !geminfo pulls gem information from poedb
    print(poeInfoReq)

    def geminfo():
        gemName = (poeInfoReq.split().pop(1))
        print("Alright, here's some information about ", str(gemName))


    if poeInfoReq.startswith("!geminfo"):
        geminfo;

if __name__ == "__main__":
    main()