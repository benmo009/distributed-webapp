import time

class Counter:
    def __init__(self, max_count: int, current_count: int = 0):
        self.max_count = max_count
        self.current_count = current_count

    def run(self):
        print(self.current_count)
        while (self.current_count < self.max_count):
            self.current_count += 1
            print(self.current_count)
            time.sleep(0.5)