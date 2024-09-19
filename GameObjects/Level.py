import pytmx
import pygame

def get_collision_data(tmx_data):
    collision_data = {}
    for layer in tmx_data.layers:
        if isinstance(layer, pytmx.TiledObjectGroup):
            collision_objects = []
            for obj in layer:
                if obj.type == 'block' or obj.properties.get('class') == 'block':
                    collision_objects.append({
                        "name": obj.name,
                        "rect": pygame.Rect(obj.x, obj.y, obj.width, obj.height),
                        "layer": layer.name,
                        "other": False
                    })
                elif obj.type == 'other' or obj.properties.get('class') == 'other':
                    if obj.name not in collision_data:
                        collision_data[obj.name] = []
                    collision_data[obj.name].append({
                        "name": obj.name,
                        "rect": pygame.Rect(obj.x, obj.y, obj.width, obj.height),
                        "layer": layer.name,
                        "other": True
                    })
            collision_data[layer.name] = collision_objects

        elif isinstance(layer, pytmx.TiledTileLayer):
            layer_colliders = []
            for x, y, gid in layer:
                tile = tmx_data.get_tile_properties_by_gid(gid)
                if tile:
                    colliders = tile.get('colliders')
                    if colliders:
                        for collider in colliders:
                            collision_rect = pygame.Rect(
                                x * tmx_data.tilewidth + collider.x,
                                y * tmx_data.tileheight + collider.y,
                                collider.width,
                                collider.height
                            )

                            layer_colliders.append({
                                "name": tile.get('name', ''),
                                "rect": collision_rect,
                                "layer": layer.name,
                                "other": False
                            })
            collision_data[layer.name] = layer_colliders  # Stocker les colliders pour chaque layer

    return collision_data
    

class Level :

    layer_obj = {}
    tmx_data = None

    def __init__(self,level_path,GAME_STATE) :
        self.tmx_data = pytmx.load_pygame(level_path)
        self.layer_obj = get_collision_data(self.tmx_data)
        GAME_STATE["active_layer"] = "ete"
        GAME_STATE["layer_obj"] = self.layer_obj
        GAME_STATE["winAndStart"] = {
            "win" : self.layer_obj["win"],
            "start" : self.layer_obj["start"]
        }

    def debugColide(self,active_layer, screen, newColide, player ,name="COLLISION"):
        font = pygame.font.Font(None, 24)
        debugText = {"DEBUG": name, "active_layer": active_layer}
        debugColor = {"Layer": (0, 255, 0), "Decor": (212, 0, 255), "Obj": (0, 0, 255), "Map": (255, 0, 0), "Other": (0,255,212), "DecorOther": (255, 212, 0)}
        textColor = (0, 0, 0)

        def draw_named_rects(objects, color):
            for obj in objects:
                pygame.draw.rect(screen, color, obj["rect"], 2)
                if obj["name"]:
                    text_surface = font.render(obj["name"], True, textColor)
                    screen.blit(text_surface, (obj["rect"].x, obj["rect"].y - 20))

        if active_layer in newColide:
            draw_named_rects(newColide[active_layer], debugColor['Layer'])

        if active_layer + "Decor" in newColide:
            draw_named_rects(newColide[active_layer + "Decor"], debugColor['Decor'])

        if active_layer + "Decor1" in newColide:
            draw_named_rects(newColide[active_layer + "Decor1"], debugColor['DecorOther'])

        if active_layer + "Obj" in newColide:
            draw_named_rects(newColide[active_layer + "Obj"], debugColor['Obj'])

        if "mapObj" in newColide:
            draw_named_rects(newColide["mapObj"], debugColor['Map'])

        for layer_name, objects in newColide.items():
            if objects:
                for obj in objects:
                    if obj["other"]:
                        draw_named_rects([obj], debugColor['Other'])

        pygame.draw.rect(screen, (255, 255, 255), (0, 0, 200, (len(debugText) + len(debugColor)) * 20))

        debugTextY = 0
        for key, value in debugText.items():
            textDebug = font.render(f"{key}: {value}", True, textColor)
            screen.blit(textDebug, (0, debugTextY))
            debugTextY += 20

        for key, value in debugColor.items():
            pygame.draw.rect(screen, value, (0, debugTextY, 20, 20))
            textDebug = font.render(key, True, textColor)
            screen.blit(textDebug, (25, debugTextY))
            debugTextY += 20

        pygame.draw.rect(screen, debugColor['DecorOther'], player.getHitbox(), 2)

    def draw(self,GAME_STATE):
        def blit_tile(layer):
            for x, y, gid in layer:
                tile = self.tmx_data.get_tile_image_by_gid(gid)
                if tile:
                    GAME_STATE["screen"].blit(tile, (x * self.tmx_data.tilewidth, y * self.tmx_data.tileheight))

        for layer in self.tmx_data.layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                if layer.name in [GAME_STATE["active_layer"], GAME_STATE["active_layer"] + 'Decor', 'mapDecor']:
                    blit_tile(layer)

        decor_index = 1
        while True:
            decor_layer_name = GAME_STATE["active_layer"] + f'Decor{decor_index}'
            if any(layer.name == decor_layer_name for layer in self.tmx_data.layers):
                for layer in self.tmx_data.layers:
                    if isinstance(layer, pytmx.TiledTileLayer) and layer.name == decor_layer_name:
                        blit_tile(layer)
                decor_index += 1
            else:
                break

        if(GAME_STATE["debug"]):
            self.debugColide(GAME_STATE["active_layer"],GAME_STATE["screen"],self.layer_obj,GAME_STATE["player"])



    def update(self,GAME_STATE):
        pass
