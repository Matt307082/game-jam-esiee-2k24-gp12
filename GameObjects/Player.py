import pygame
from Tools.utils import ChargeSerieSprites, WINDOW_SIZE
from GameObjects.Skull import Skull

class Player:
    def __init__(self, spritesheet, GAME_STATE):
        self.x = GAME_STATE["winAndStart"]['start']["rect"].x
        self.y = GAME_STATE["winAndStart"]['start']["rect"].y
        self.vx = 1
        self.vy = 1
        self.spritesheet = spritesheet
        self.width = 200 // 4
        self.height = 261 // 4
        self.cell_width = 25
        self.cell_height = 32
        self.down_anim = ChargeSerieSprites(0, spritesheet, (self.width,self.height), 4)
        self.right_anim = ChargeSerieSprites(1, spritesheet, (self.width,self.height), 4)
        self.left_anim = ChargeSerieSprites(2, spritesheet, (self.width,self.height), 4)
        self.up_anim = ChargeSerieSprites(3, spritesheet, (self.width,self.height), 4)
        self.current_anim = self.down_anim # default value
        self.animation_index = 0         
        self.animation_speed = 10
        self.frame_counter = 0

    def update(self, GAME_STATE):
        # initialize KeyPressed
        KeysPressed = GAME_STATE["keyPressed"]
        active_layer = GAME_STATE["active_layer"]
        layer_obj = GAME_STATE["layer_obj"]

        test = self.getHitbox()
        if(KeysPressed == pygame.K_DOWN and self.y<WINDOW_SIZE[1]-self.cell_height):
            test.y += self.vy
            self.current_anim = self.down_anim
        elif(KeysPressed == pygame.K_UP and self.y>0):
            test.y -= self.vy
            self.current_anim = self.up_anim
        elif(KeysPressed == pygame.K_LEFT and self.x>0):
            test.x -= self.vx
            self.current_anim = self.left_anim
        elif(KeysPressed == pygame.K_RIGHT and self.x<WINDOW_SIZE[0]-self.cell_width):
            test.x += self.vx
            self.current_anim = self.right_anim
        
        print(test)
        print(active_layer)
        print(layer_obj)
        if not self.check_collision(test, active_layer, layer_obj):
            self.x = test.x
            self.y = test.y

        self.frame_counter += 1
        if self.frame_counter >= self.animation_speed:
            self.frame_counter = 0
            self.animation_index += 1
            if self.animation_index >= len(self.current_anim):
                self.animation_index = 0

    def draw(self, GAME_STATE):
        GAME_STATE["screen"].blit(pygame.transform.scale(
            self.current_anim[self.animation_index if GAME_STATE["keyPressed"] != None else (0 if self.current_anim == self.left_anim else 1)]
        ,(25,32)),(self.x,self.y))

    def reset(self, GAME_STATE):
        GAME_STATE["gameObject"].append(Skull((self.x,self.y),GAME_STATE["skullSprite"]))
        self.x = GAME_STATE["winAndStart"]['start']["rect"].x
        self.y = GAME_STATE["winAndStart"]['start']["rect"].y
        

    def getHitbox(self):
        return pygame.Rect(self.x,self.y,self.cell_width,self.cell_height)
    
    
    def check_collision(self,new_player_pos, active_layer, newColide):

        def collides_with_layer(layer_name):
            return any(new_player_pos.colliderect(obj["rect"]) for obj in newColide.get(layer_name, []))

        if collides_with_layer(active_layer):
            return True
        if collides_with_layer(active_layer + "Decor"):
            return True
        if collides_with_layer(active_layer + "Obj"):
            return True
        if collides_with_layer("mapObj"):
            return True
        if "win" in newColide and new_player_pos.colliderect(newColide["win"]["rect"]):
            print("win")
            return True
        return False



    