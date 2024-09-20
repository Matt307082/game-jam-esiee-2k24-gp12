import pygame
from Tools.utils import ChargeSerieSprites, WINDOW_SIZE
from GameObjects.Skull import Skull

class Player:
    def __init__(self, spritesheet, GAME_STATE):
        self.x = GAME_STATE["winAndStart"]['start'][0]["rect"].x
        self.y = GAME_STATE["winAndStart"]['start'][0]["rect"].y
        self.vx = 2
        self.vy = 2
        self.spritesheet = spritesheet
        self.width = 200 // 4
        self.height = 285 // 4
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
        self.inFog = False
        self.changeAlpha = False
        self.alpha = 255
        self.changeSpeed = 20
        self.moved = False

    def update(self, GAME_STATE):
        # initialize KeyPressed
        KeysPressed = pygame.key.get_pressed()
        active_layer = GAME_STATE["active_layer"]
        layer_obj = GAME_STATE["layer_obj"]

        hitbox = self.getHitbox()
        hitbox.y += 5
        hitbox.x += 5
        hitbox.width -= 10
        hitbox.height -= 10
        if self.check_collision(hitbox,False,active_layer, layer_obj, GAME_STATE) :
            self.reset(GAME_STATE)
            return

        self.moved = True
        test = self.getHitbox()
        if(KeysPressed[pygame.K_DOWN] and self.y<WINDOW_SIZE[1]-self.cell_height):
            test.y += self.vy
            self.current_anim = self.down_anim
        elif(KeysPressed[pygame.K_UP] and self.y>0):
            test.y -= self.vy
            self.current_anim = self.up_anim
        elif(KeysPressed[pygame.K_LEFT] and self.x>0):
            test.x -= self.vx
            self.current_anim = self.left_anim
        elif(KeysPressed[pygame.K_RIGHT] and self.x<WINDOW_SIZE[0]-self.cell_width):
            test.x += self.vx
            self.current_anim = self.right_anim
        else: self.moved = False

        if not self.check_collision(test, True, active_layer, layer_obj, GAME_STATE):
            self.x = test.x
            self.y = test.y

        if self.moved :
            self.frame_counter += 1
            if self.frame_counter >= self.animation_speed:
                self.frame_counter = 0
                self.animation_index += 1
                if self.animation_index >= len(self.current_anim):
                    self.animation_index = 0
        else:
            self.animation_index = 0 if self.current_anim == self.left_anim else 1

        if self.changeAlpha :
            if self.inFog :
                if self.alpha <= 0 :
                    self.changeAlpha = False
                else :
                    self.alpha -= self.changeSpeed
                    self.changeAlphaPlayer(self.alpha)
            else :
                if self.alpha >= 255 :
                    self.changeAlpha = False
                else :
                    self.alpha += self.changeSpeed
                    self.changeAlphaPlayer(self.alpha)



    def draw(self, GAME_STATE):
        GAME_STATE["screen"].blit(pygame.transform.scale(
            self.current_anim[self.animation_index]
        ,(25,32)),(self.x,self.y))

    def reset(self, GAME_STATE):
        GAME_STATE["gameObject"].append(Skull((self.x,self.y),GAME_STATE["skullSprite"]))
        GAME_STATE['music_manager'].use_effect("criWilhelm")
        self.x = GAME_STATE["winAndStart"]['start'][0]["rect"].x
        self.y = GAME_STATE["winAndStart"]['start'][0]["rect"].y

        GAME_STATE["menu"].current_season = GAME_STATE["startingSeason"]
        GAME_STATE["menu"].change_season(GAME_STATE)
        GAME_STATE["menu"].season_counter = 0

    def getHitbox(self):
        return pygame.Rect(self.x,self.y,self.cell_width,self.cell_height)
    
    def changeAlphaPlayer(self, alpha):
        anims = [self.down_anim,self.up_anim,self.left_anim,self.right_anim]
        for anim in anims :
            for img in  anim :
                img.set_alpha(alpha)
    
    def check_collision(self, new_player_pos, check_fog, active_layer, newColide, GAME_STATE):
        
        inFogNow = False
        collide = False

        def collides_with_layer(layer_name):
            return any(new_player_pos.colliderect(obj["rect"]) for obj in newColide.get(layer_name, []))

        if collides_with_layer(active_layer):
            collide = True
        elif collides_with_layer(active_layer + "Decor"):
            collide =  True
        elif collides_with_layer(active_layer + "Obj"):
            collide = True
        elif collides_with_layer("mapObj"):
            collide = True
        elif "win" in newColide and (
                    any(win_rect["layer"] == active_layer + "Obj" for win_rect in newColide["win"]) or any(
                win_rect["layer"] == "mapObj" for win_rect in newColide["win"])):
            for win_rect in newColide["win"]:
                if new_player_pos.colliderect(win_rect["rect"]):
                    GAME_STATE['music_manager'].use_effect("success")
                    GAME_STATE["nextLevel"] = True
                    collide = True

        if collides_with_layer(active_layer + "Decor1"):
            inFogNow = True
            
        if check_fog and self.inFog != inFogNow :
            self.changeAlpha = True
            self.inFog = inFogNow


        return collide



    