import sys
import pyautogui as p
import services.setup_service as setup_service
import services.lobby_service as lobby_service
import services.game_service as game_service
from constants.state_constants import STATE
from constants.game_constants import heroes

import threading

class Bot:
    regions = []
    clients = []
    
    is_game_active = False
    
    screenHeight = p.size().height
    
    def __init__(self):
        self.setup()
        if not ('-radiant' in sys.argv or '-dire' in sys.argv):
            should_make_party = True if '-party' in sys.argv else False
            self.search(should_make_party)
        self.is_game_active = True
        # self.gg()
        print('Running game loop')
        self.game_loop()
        

    def setup(self):
        print('Starting Dota 100 hour bot...')
        self.regions = setup_service.get_regions()
        
        side = 'NONE'
        
        if '-radiant' in sys.argv:
            side = 'radiant'
        
        if '-dire' in sys.argv:
            side = 'dire'
        
        setup_service.set_initial_states(self.regions, self.clients, side)

    def gg(self):
        threading.Timer(60 * 10, game_service.type_gg, [self]).start()

    def set_clients_state(self, state: STATE):
        for client in self.clients:
            client.state = state

    def search(self, should_make_party = False):
        lobby_service.search_games(self.regions, should_make_party)
        self.set_clients_state(STATE.DETECTING_SIDE_AND_PICKING_HERO)
        self.reset_heroes()
        
    
    def reset_heroes(self):
        self.heroes = heroes.copy()
    
    def game_end_detector(self):
        afk_count = 0
        for client in self.clients:
            if client.state == STATE.DID_NOT_RUN_MID:
                afk_count+=1
        if(afk_count == 10):
            self.is_game_active = False
            p.sleep(30)
            lobby_service.skip_rewards(self.regions)
            self.search()
            self.game_loop()
    
    def reset_window(self):
        p.hotkey('ctrl', 'escape')
        p.moveTo(0, self.screenHeight / 2)
        p.leftClick()
        p.sleep(4)
    
    def game_loop(self):
        i = 0
        self.game_end_detector()
        for client in self.clients:
            self.reset_window()
            state = client.state
            print('Player ' + str(i+1) + ' state: ' + state)
            try:
                match state:
                    case STATE.DETECTING_SIDE_AND_PICKING_HERO:
                        try:
                            game_service.detect_side(self.regions[i], client, self.heroes, i)
                        except:
                            pass
                        
                        
                    case STATE.PLAYING:
                        try:
                            game_service.run_mid(self.regions[i], client, i)
                        except:
                            pass
                        
                    case STATE.DID_NOT_RUN_MID:
                        try:
                            game_service.run_mid(self.regions[i], client, i)
                        except:
                            pass
                        
                    case STATE.START_BUY:
                        try:
                            game_service.start_buy(self.regions[i], client)
                        except:
                            pass
                i+=1
            except:
                pass
            
        print('Game loop done')
        
        if self.is_game_active:
            threading.Timer(2, self.game_loop).start()
                
bot = Bot()