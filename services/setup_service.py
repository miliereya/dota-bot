import pyautogui as p

from constants.state_constants import STATE

def show_windows_locations():
    screenWidth, screenHeight = p.size()
    i = 0
    wFifth = screenWidth / 5
    hHalf = screenHeight / 2
    p.FAILSAFE = False
    while (i < 10):
        p.moveTo(wFifth * i if i < 5 else wFifth * (i - 5), 0 if i < 5 else hHalf, 0.3)
        p.sleep(1)
        i+=1

def get_regions():
    regions = []
    screenWidth, screenHeight = p.size()
    i = 0
    wFifth = screenWidth / 5
    hHalf = screenHeight / 2
    while (i < 10):
        regions.append((int(i * wFifth if i < 5 else (i - 5) * wFifth), int(0 if i < 5 else hHalf), int(wFifth), int(hHalf)))
        i+=1
    return regions

def set_initial_states(regions: list, clients, initSide):

    i = 0
    for region in regions:
        class CLIENT:
            state = STATE.MAIN_MENU if initSide == 'NONE' else STATE.PLAYING
            side = 'NONE' if initSide == 'NONE' else 'radiant' if i < 5 and initSide == 'radiant' or i > 4 and initSide == 'dire' else 'dire'
            num = i
        clients.append(CLIENT())
        i+=1
        
    l = 0
    if initSide != 'NONE':
        for client in clients:
           print('Player '+ str(l+1) + ' side: ' + client.side)
           l+=1