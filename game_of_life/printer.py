# Contains methods for printing.
class Printer:

    @staticmethod
    def reprint(string = ''):
        print("\033[0K" + string)

    @staticmethod
    def clear_screen():
        print("\033[2J")

    @staticmethod
    def move_to_home():
        print("\033[H")
