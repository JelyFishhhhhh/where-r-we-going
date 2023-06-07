from modules import Json
from asyncio import run
from random import randint

async def capture():

    City = {}

    Data = Json.load_nowait("AllData.json")
    idx = 0
    for i in range(len(Data)):

        if Data[i]["CityName"] == "釣魚臺":
            
            continue
        
        City[idx] = Data[i]["CityName"]
        
        idx +=1

    return City

if __name__ == "__main__":

    City = run(capture())
    rd = {}

    for i in range(100):

        rd[i] = City[randint(0, len(City)-1)]
        print(rd[i])

    print(">>>>>\nThe Final Answer is\n")
    print(rd[randint(0, len(rd)-1)])
    print("\n>>>>>")