import colorama
from colorama import Fore, Style

colorama.init()

class Print:
    def error(self, errorName: str, message: str):
        if errorName and message:
            print(Fore.RED + Style.BRIGHT + f"ERROR: {errorName}" + Style.RESET_ALL + f" {message}")

    def warning(self, warningName: str, message: str):
        if warningName and message:
            print(Fore.YELLOW + Style.BRIGHT + f"WARNING: {warningName}" + Style.RESET_ALL + f" {message}")

    def message(self, message: str):
        if message:
            print(message)
