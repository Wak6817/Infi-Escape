import random
import time

class Backend:
    
    @staticmethod
    def level():
        data = {
            "level_number": 1,
            "difficulty": random.choice(["easy", "medium", "hard"]),
        }
        return data
    
    @staticmethod
    def user(username="default_user"):
        data = {
            "name": username,
            "score": 0,
            "level": 1,
            "start_time": time.time(),
            "time_left": 60,
        }
        return data

    @staticmethod
    def time_remaining(user_data):
        elapsed = time.time() - user_data["start_time"]
        remaining = user_data["time_left"] - int(elapsed)
        return max(remaining, 0)


class Frontend:
    username = "default_user"


if __name__ == "__main__":
    pass