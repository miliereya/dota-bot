import pyautogui as p
from constants.state_constants import STATE
from threading import Timer

def detect_side(region, client):
    try:
        radiant = p.locateCenterOnScreen('images/game/detect-radiant.png', confidence = 0.87, region=region)
        if(radiant):
            print('radiant found')
            p.moveTo(radiant)
            client.side = 'radiant'
            pick_hero(client)
            client.state = STATE.SPAWN
            return
    except:
        pass
    try:
        dire = p.locateCenterOnScreen('images/game/detect-dire.png', confidence = 0.87, region=region)
        if(dire):
            print('dire found')
            p.moveTo(dire)
            client.side = 'dire'
            pick_hero(client)
            client.state = STATE.SPAWN
            return
    except:
        pass

def pick_hero(client):
    try:
        print('picking hero')
        if(client.side == 'radiant'):
            p.move(10, -335)
            p.sleep(0.1)
            p.leftClick()
            p.sleep(0.1)
            p.move(400, 265)
            p.leftClick()
            p.sleep(1)
        else:
            p.move(-60, -315)
            p.sleep(0.1)
            p.leftClick()
            p.sleep(0.1)
            p.move(400, 265)
            p.leftClick()
            p.sleep(1)
        print('hero picked')
    except:
        pass
    
def run_mid(region, client):
    try:
        inventory = p.locateCenterOnScreen('images/game/inventory.png', confidence = 0.87, region=region)
        p.moveTo(inventory)
        p.leftClick()
        if(client.side == 'radiant'):
            p.move(182, -45)
            p.press('a')
            p.leftClick()
            client.state = STATE.WAITING
            Timer(10, set_playing, [client]).start()
        if(client.side == 'dire'):
            p.move(112, 17)
            p.press('a')
            p.leftClick()
            client.state = STATE.WAITING
            Timer(10, set_playing, [client]).start()
    except:
        pass

def set_playing(client):
    client.state = STATE.PLAYING
    
def type_gg(bot):
    bot.is_game_active = False
    p.sleep(15)
    p.moveTo(200, 200)
    p.leftClick()
    p.sleep(1)
    p.press('enter')
    p.sleep(1)
    p.press('tab')
    p.sleep(1)
    p.press('g')
    p.sleep(1)
    p.press('g')
    p.sleep(1)
    p.press('enter')
    p.sleep(1)