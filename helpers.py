class MusicManager:
    files = dict()

    def loadFiles(this, *args):
        for musicName in args:
            this.files[musicName] = open(f"soundtrack/{musicName}.mp3")

    def play(this, musicName):
        pygame.mixer.music.load(this.files[musicName])
        pygame.mixer.music.play(-1, random.uniform(0, 300))