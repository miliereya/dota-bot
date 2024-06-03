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
        self.search()
        self.is_game_active = True
        # self.gg()
        self.game_loop()
        

    def setup(self):
        self.regions = setup_service.get_regions()
        setup_service.set_initial_states(self.regions, self.clients)

    def gg(self):
        threading.Timer(60 * 10, game_service.type_gg, [self]).start()

    def set_clients_state(self, state: STATE):
        for client in self.clients:
            client.state = state

    def search(self):
        lobby_service.search_games(self.regions)
        self.set_clients_state(STATE.DETECTING_SIDE_AND_PICKING_HERO)
        self.reset_heroes()
    
    def reset_heroes(self):
        self.heroes = heroes.copy()
    
    def reset_window(self):
        p.hotkey('ctrl', 'escape')
        p.moveTo(0, self.screenHeight / 2)
        p.leftClick()
        p.sleep(4)
    
    def game_loop(self):
        print('looped')
        i = 0
        for client in self.clients:
            self.reset_window()
            state = client.state
            try:
                match state:
                    case STATE.DETECTING_SIDE_AND_PICKING_HERO:
                        try:
                            game_service.detect_side(self.regions[i], client, self.heroes)
                        except:
                            pass
                        
                        
                    case STATE.PLAYING:
                        try:
                            game_service.run_mid(self.regions[i], client)
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
        if self.is_game_active:
            threading.Timer(2, self.game_loop).start()
                
bot = Bot()