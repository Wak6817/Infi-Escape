import time

class Engine:

    class Backend:
        pass

    class Frontend:
        pass

class Game:

    class Backend:

        @staticmethod
        def level(difficulty=None):
            data = {
                "level_number": 1,
                "difficulty": difficulty
            }
            return data
        
        @staticmethod
        def user(username=None):
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
        pass

    if __name__ == "__main__":
        pass