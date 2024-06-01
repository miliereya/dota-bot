import pyautogui as p

def search_games(regions: list):
    print("Searching games")
    p.sleep(2)
    for region in regions:
        try:
            p.moveTo(p.locateCenterOnScreen('images/lobby/test.png', confidence =  0.7, region=region))
            p.leftClick()
            p.sleep(0.5)
            p.leftClick()
        except:
            print('not found')
            pass
    print("Waiting for games")
    while True:
        try:
            p.sleep(1)
            print('here')
            if(list(p.locateAllOnScreen('images/lobby/accept.png', confidence = 0.87)).__len__() == regions.__len__()):
                break
        except:
            pass
    print('Accepting games')
    p.sleep(3)
    for region in regions:
        try:
            accept = p.locateCenterOnScreen('images/lobby/accept.png', confidence =  0.87, region=region)
            p.moveTo(accept)
            p.sleep(0.2)
            p.leftClick()
            p.sleep(0.2)
        except:
            pass