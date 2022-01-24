from time import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        print("==== TIMING ====")
        self.start_time = time()

    def __exit__(self, exc_type, exc_value, exc_trace):
        self.end_time = time()
        print("==== TIMER FINISHED ====")
        print(f"The code took {self.end_time - self.start_time} seconds to execute.")
