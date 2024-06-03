import pyautogui as p
from constants.state_constants import STATE
from threading import Timer

def detect_side(region, client, heroes: list):
    try:
        radiant = p.locateCenterOnScreen('images/game/detect-radiant.png', confidence = 0.87, region=region)
        if(radiant):
            print('radiant found')
            
            p.moveTo(radiant)
            client.side = 'radiant'
            
            pick_hero(client, region, heroes)
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
            
            pick_hero(client, region, heroes)
            client.state = STATE.PLAYING
            # Timer(70, set_start_buying, [client]).start()
            return
    except:
        pass

def pick_hero(client, region, heroes: list):
    hero = heroes.pop(0)
    print(hero)
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
            except:
                pass
    except:
        pick_hero(client, region, heroes)

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