import pyautogui as p
from constants.state_constants import STATE
from threading import Timer

def detect_side(region, client, heroes: list, i: int):
    try:
        radiant = p.locateCenterOnScreen('images/game/detect-radiant.png', confidence = 0.87, region=region)
        if(radiant):
            print('Player ' + str(i+1) + ' side: Radiant')
            
            p.moveTo(radiant)
            client.side = 'radiant'
            
            pick_hero(client, region, heroes, i)
            client.state = STATE.WAITING
            Timer(80, set_playing, [client]).start()
            return
    except:
        pass
    try:
        dire = p.locateCenterOnScreen('images/game/detect-dire.png', confidence = 0.87, region=region)
        if(dire):
            print('Player ' + str(i+1) + ' side: Dire')
            
            p.moveTo(dire)
            client.side = 'dire'
            
            pick_hero(client, region, heroes, i)
            client.state = STATE.WAITING
            Timer(80, set_playing, [client]).start()
            return
    except:
        pass

def pick_hero(client, region, heroes: list, i: int):
    if(heroes.__len__() == 0):
        print('No heroes left. Pick by yourself please')
        return
    hero = heroes.pop(0)
    
    try:
        hero_icon = p.locateCenterOnScreen('images/heroes/'+ hero + '.png', confidence = 0.87, region=region)
        if(hero_icon):
            p.moveTo(hero_icon)
            p.sleep(0.2)
            p.leftClick()
            
            try:
                lock_in = p.locateCenterOnScreen('images/game/lock-in.png', confidence = 0.87, region=region)
                if(lock_in):
                    p.moveTo(lock_in)
                    p.sleep(0.2)
                    p.leftClick()
                    print('Player ' + str(i+1) + ' hero: ' + hero)
            except:
                print('Player ' + str(i+1) + ' failed to pick ' + hero)
                pass
    except:
        print('Hero "' + hero + '" is banned')
        pick_hero(client, region, heroes, i)

def start_buy(region, client):
    try:
        inventory = p.locateCenterOnScreen('images/game/inventory.png', confidence = 0.87, region=region)
        p.moveTo(inventory)
        p.leftClick()
        p.press('f4')
        p.sleep(0.5)
        shop_search = p.locateCenterOnScreen('images/game/shop-search.png', confidence = 0.87, region=region)
        p.moveTo(shop_search)
        p.leftClick()
        p.press('m')
        p.press('a')
        p.press('e')
        p.press('l')
        p.press('s')
        p.press('t')
        p.press('r')
        p.press('o')
        p.press('m')
        p.keyDown('shift')
        p.keyDown('ctrl')
        p.move(0, 20)
        p.leftClick()
        client.state = STATE.PLAYING
        p.keyUp('shift')
        p.keyUp('ctrl')
    except:
        pass

def run_mid(region, client, i: int):
    try:
        inventory = p.locateCenterOnScreen('images/game/inventory.png', confidence = 0.87, region=region)
        p.moveTo(inventory)
        p.leftClick()
        if(client.side == 'radiant'):
            p.move(182, -45)
            p.press('a')
            p.leftClick()
            print('Player ' + str(i+1) + ' is attacking Dire Throne')
            client.state = STATE.WAITING
            Timer(10, set_playing, [client]).start()
        if(client.side == 'dire'):
            p.move(112, 17)
            p.press('a')
            p.leftClick()
            print('Player ' + str(i+1) + ' is attacking Radiant Throne')
            client.state = STATE.WAITING
            Timer(10, set_playing, [client]).start()
    except:
        print('Player ' + str(i+1) + ' attacking failed')
        client.state = STATE.DID_NOT_RUN_MID
        pass

def set_playing(client):
    client.state = STATE.PLAYING
    
def set_start_buying(client):
    client.state = STATE.START_BUY
    
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