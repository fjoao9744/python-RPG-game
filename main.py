class World:
    def __init__(self):
        self.fase = 1
        
    def __next__(self):
        while self.fase < 100:
            self.fase += 1
            yield self.fase
        
        

