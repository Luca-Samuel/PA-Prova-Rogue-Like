class stage_counter:
    def __init__(self) -> None:
        self.counter = 1

    def next_stage(self):
        self.counter += 1
    
    def current_stage(self):
        return self.counter