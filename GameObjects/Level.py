import pytmx
import pygame

def get_collision_objects_by_layer(tmx_data):
        layers = {}
        for layer in tmx_data.layers:
            if isinstance(layer, pytmx.TiledObjectGroup):  # Si c'est un layer d'objets
                collision_objects = []
                for obj in layer:
                    # On cherche les objets ayant la propriété 'class' == 'block' ou un type 'block'
                    if obj.type == 'block' or obj.properties.get('class') == 'block':
                        # Stocker le nom de l'objet et son rectangle
                        collision_objects.append({
                            "name": obj.name,
                            "rect": pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                        })
                layers[layer.name] = collision_objects
        return layers
    

class Level :

    layer_obj = {}
    tmx_data = None

    def __init__(self,level_path,GAME_STATE) :
        self.tmx_data = pytmx.load_pygame(level_path)
        self.layer_obj = get_collision_objects_by_layer(self.tmx_data)
        GAME_STATE["active_layer"] = "ete"
        GAME_STATE["layer_obj"] = self.layer_obj


    def debugColide(self,active_layer,screen):
        font = pygame.font.Font(None, 24)
        realActiveLayer = active_layer + "Obj"

        debugText = {
            "DEBUG": "COLLISION",
            "active_layer": active_layer,
            "Object": realActiveLayer
        }
        pygame.draw.rect(screen, (255, 255, 255), (0, 0, 200, debugText.__len__() * 20))
        debugTextY = 0
        for key, value in debugText.items():
            textDebug = font.render(key + ": " + value, True, (0, 0, 0))
            screen.blit(textDebug, (0, debugTextY))
            debugTextY += 20

        if realActiveLayer in self.layer_obj:
            for obj in self.layer_obj[realActiveLayer]:
                pygame.draw.rect(screen, (0, 255, 0), obj["rect"], 2)
                if obj["name"]:
                    text_surface = font.render(obj["name"], True, (0, 0, 0))
                    screen.blit(text_surface, (obj["rect"].x, obj["rect"].y - 20))

    def draw(self, GAME_STATE):
        for layer in self.tmx_data.layers:
            if isinstance(layer, pytmx.TiledTileLayer) and layer.name == GAME_STATE["active_layer"]:
                for x, y, gid in layer:
                    tile = self.tmx_data.get_tile_image_by_gid(gid)
                    if tile:
                        GAME_STATE["screen"].blit(tile, (x * self.tmx_data.tilewidth, y * self.tmx_data.tileheight))

        self.debugColide(GAME_STATE["active_layer"],GAME_STATE["screen"])

    def update(self,GAME_STATE):
        pass
