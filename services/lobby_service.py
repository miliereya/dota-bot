import pyautogui as p

def search_games(regions: list, should_make_party: bool = False):
    if should_make_party:
        make_parties(regions)
    
    p.sleep(2)
    print("Starting search")

    start_game(regions[0])
    start_game(regions[5])

    print("Waiting for games")

    while True:
        try:
            p.sleep(1)
            founded_games = list(p.locateAllOnScreen('images/lobby/accept.png', confidence = 0.87)).__len__()

            if(founded_games == 5):
                print('5 player found the game')
                print('Waiting for another 5 players')
                
                p.sleep(1.5)
                
                if(list(p.locateAllOnScreen('images/lobby/accept.png', confidence = 0.87)).__len__() == 5):
                    print("Another 5 players didn't find the game")
                    
                    queue_again(regions[0])
                    queue_again(regions[5])
                    
                    print("Searching again")

                    
            if(founded_games == 10):
                print("Game is found")
                break
        except:
            pass
        
    print('Accepting games')
    p.sleep(1)
    
    for region in regions:
        try:
            accept = p.locateCenterOnScreen('images/lobby/accept.png', confidence =  0.87, region=region)
            p.moveTo(accept)
            p.sleep(0.3)
            p.leftClick()
            p.sleep(0.3)
        except:
            pass
        
    print('Games accepted')
    print('Waiting for players to load')
    while True:
        try:
            p.sleep(1)
            radiant_count = list(p.locateAllOnScreen('images/game/detect-radiant.png', confidence = 0.87)).__len__()
            dire_count = list(p.locateAllOnScreen('images/game/detect-dire.png', confidence = 0.87)).__len__()

            if(radiant_count == 5 and dire_count == 5):
                break
        except:
            pass
    print('All players are loaded')

def accept_rewards(regions):
    for region in regions:
        try:
            reward = p.locateCenterOnScreen('images/lobby/accept-reward.png', confidence =  0.87, region=region)
            p.moveTo(reward)
            p.leftClick()
            p.sleep(0.3)
        except:
            pass
        try:
            ok = p.locateCenterOnScreen('images/lobby/ok.png', confidence =  0.87, region=region)
            p.moveTo(ok)
            p.leftClick()
            p.sleep(0.3)
        except:
            pass

def skip_rewards(regions: list):
    accept_rewards(regions)
    p.sleep(1)
    
    accept_rewards(regions)
    p.sleep(1)
    
    accept_rewards(regions)
    p.sleep(1)
    
    accept_rewards(regions)
    p.sleep(1)
    

def make_parties(regions):
    print('Making parties')

    print('Inviting players for stack 1')
    
    invite_to_party(regions[0], regions[1])
    invite_to_party(regions[0], regions[2])
    invite_to_party(regions[0], regions[3])
    invite_to_party(regions[0], regions[4])

    print('Inviting players for stack 2')

    invite_to_party(regions[5], regions[6])
    invite_to_party(regions[5], regions[7])
    invite_to_party(regions[5], regions[8])
    invite_to_party(regions[5], regions[9])

    print('Accepting invitations')
    
    for region in regions:
        try:
            accept_invite = p.locateCenterOnScreen('images/lobby/accept-invite.png', confidence =  0.87, region=region)
            p.moveTo(accept_invite)
            p.sleep(0.3)
            p.leftClick()
            p.sleep(0.3)
        except:
            pass

def start_game(region):
    try:
        play = p.locateCenterOnScreen('images/lobby/play.png', confidence =  0.87, region=region)
        p.moveTo(play)
        p.leftClick()
        p.sleep(0.5)
        p.leftClick()
        p.sleep(0.8)
        try:
            continue_button = p.locateCenterOnScreen('images/lobby/continue.png', confidence = 0.87, region=region)
            if(continue_button):
                p.moveTo(continue_button)
                p.leftClick()
        except:
            pass
    except:
        pass
        
def queue_again(region):
    try:
        queue_again = p.locateCenterOnScreen('images/lobby/queue.png', confidence =  0.87, region=region)
        p.moveTo(queue_again)
        p.sleep(0.2)
        p.leftClick()
        p.sleep(0.2)
    except:
        pass
    
def invite_to_party(leader, player):
    print('Copying id')
    get_id(player)

    print('Inviting player')
    try:
        add_party = p.locateCenterOnScreen('images/lobby/add-party.png', confidence =  0.87, region=leader)
        p.moveTo(add_party)
        p.sleep(0.2)
        p.leftClick()
        p.sleep(0.2)
        
        id_field = p.locateCenterOnScreen('images/lobby/id-field.png', confidence =  0.87, region=leader)
        p.moveTo(id_field)
        p.sleep(0.2)
        p.leftClick()
        p.sleep(0.2)
        
        p.rightClick()
        p.move(25, 0)
        p.leftClick()
        
        search = p.locateCenterOnScreen('images/lobby/search.png', confidence =  0.87, region=leader)
        p.moveTo(search)
        p.sleep(0.2)
        p.leftClick()
        p.sleep(0.5)
        
        add = p.locateCenterOnScreen('images/lobby/add.png', confidence =  0.87, region=leader)
        p.moveTo(add)
        p.sleep(0.2)
        p.leftClick()
        p.sleep(0.5)
        
        dota = p.locateCenterOnScreen('images/lobby/dota.png', confidence =  0.87, region=leader)
        p.moveTo(dota)
        p.sleep(0.2)
        p.leftClick()
        p.sleep(1)
        
    except:
        pass
    print('Player invited')
    
    
def get_id(region):
    try:
        rank= p.locateCenterOnScreen('images/lobby/rank.png', confidence =  0.87, region=region)
        p.moveTo(rank)
        p.move(-100, 0)
        p.sleep(0.2)
        p.leftClick()
        p.sleep(1)
        
        friend_id = p.locateCenterOnScreen('images/lobby/friend-id.png', confidence =  0.87, region=region)
        p.moveTo(friend_id)
        p.move(22, 0)
        p.drag(36, 0, 0.5, button='left')
        
        p.move(-13, 0)
        p.rightClick()
        p.move(25, 0)
        p.leftClick() 
        
        p.sleep(0.5)
    except:
        pass
