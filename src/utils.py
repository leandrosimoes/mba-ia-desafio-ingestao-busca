# Basic color codes
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RESET = "\033[0m"  # This resets the color back to default


def print_colored(text: str, color: str = None) -> None:
    if not text:
        return

    if not color in ["red", "green", "blue", "yellow"]:
        print(text)
        return

    color_map = {
        "red": RED,
        "green": GREEN,
        "blue": BLUE,
        "yellow": YELLOW,
        "reset": RESET,
    }

    print(f"{color_map.get(color.lower(), RESET)}{text}{RESET}")


def input_colored(prompt: str, color: str = None) -> str:
    if not prompt:
        return input()

    if not color in ["red", "green", "blue", "yellow"]:
        return input(prompt)

    color_map = {
        "red": RED,
        "green": GREEN,
        "blue": BLUE,
        "yellow": YELLOW,
        "reset": RESET,
    }

    return input(f"{color_map.get(color.lower(), RESET)}{prompt}{RESET}")
