import time
import sys
import select
import termios
import tty
import os


class Engine:

    class Backend:

        @staticmethod
        def cls_term():
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')

        @staticmethod
        def input_handler():
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            input_data = ""
            try:
                tty.setraw(fd)
                while True:
                    Engine.Backend.cls_term()
                    if select.select([sys.stdin], [], [], 0.1)[0]:
                        input_data = sys.stdin.read(1)
                        break
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

            return input_data

        @staticmethod
        def generate_level(number=None, difficulty=None, type=None):
            data = {
                "level_number": number,
                "difficulty": difficulty,
                "puzzle_type": type
            }
            return data

    class Frontend:
        pass


class Game:

    class Backend:

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
    Engine.Backend.cls_term()
    input("Maximize your window and press enter.")
    Engine.Backend.cls_term()