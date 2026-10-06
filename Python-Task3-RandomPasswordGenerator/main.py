"""Generate a password that follows the user's character choices."""

import secrets
import string


MINIMUM_LENGTH = 8
CHARACTER_GROUPS = {
    "uppercase letters": string.ascii_uppercase,
    "lowercase letters": string.ascii_lowercase,
    "numbers": string.digits,
    "symbols": "!@#$%^&*()-_=+[]{};:,.?/",
}


def ask_yes_no(prompt: str) -> bool:
    """Ask for a yes/no answer, repeating until the input is valid."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no"}:
            return False
        print("Please enter y or n.")


def read_password_length() -> int:
    """Read a whole-number password length of at least eight characters."""
    while True:
        entered = input(f"Password length (minimum {MINIMUM_LENGTH}): ").strip()
        try:
            length = int(entered)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if length < MINIMUM_LENGTH:
            print(f"The password must be at least {MINIMUM_LENGTH} characters long.")
        else:
            return length


def choose_character_groups() -> list[str]:
    """Return the selected groups, requiring at least two types."""
    while True:
        selected = [
            characters
            for label, characters in CHARACTER_GROUPS.items()
            if ask_yes_no(f"Include {label}? (y/n): ")
        ]
        if len(selected) >= 2:
            return selected
        print("Choose at least two character types. Please select again.")


def generate_password(length: int, selected_groups: list[str]) -> str:
    """Create a secure password containing each selected character type."""
    if length < MINIMUM_LENGTH:
        raise ValueError(f"Length must be at least {MINIMUM_LENGTH}.")
    if len(selected_groups) < 2:
        raise ValueError("Select at least two character types.")
    if length < len(selected_groups):
        raise ValueError("Length is too short for the selected character types.")

    password_characters = [secrets.choice(group) for group in selected_groups]
    available_characters = "".join(selected_groups)
    password_characters.extend(
        secrets.choice(available_characters)
        for _ in range(length - len(password_characters))
    )
    secrets.SystemRandom().shuffle(password_characters)
    return "".join(password_characters)


def main() -> None:
    print("Random Password Generator")
    print("Generated passwords are shown only in this session; they are not saved.\n")

    while True:
        length = read_password_length()
        selected_groups = choose_character_groups()
        password = generate_password(length, selected_groups)
        print(f"\nGenerated password: {password}")
        if not ask_yes_no("Generate another password? (y/n): "):
            print("Goodbye.")
            return
        print()


if __name__ == "__main__":
    main()
