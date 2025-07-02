class Hero:
    def __init__(self, movimento_maximo=3):
        self.x = 0
        self.y = 0
        self.movimento_maximo = movimento_maximo

    def coordenada(self):
        return (self.x, self.y)
