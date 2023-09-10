from modules import Json
from asyncio import run
from random import randint

ignore_place = ["釣魚臺", "南海島", "連江縣", "嘉義市"]

async def capture():

    City = {}

    Data = Json.load_nowait("AllData.json")
    idx = 0
    for i in range(len(Data)):
        flag = False

        for ignore in range(len(ignore_place)):
            
            if Data[i]["CityName"] == ignore_place[ignore]:
                flag = True        
                break
        
        if flag:
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
