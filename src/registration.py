BANNED_WORDS = ["admin", "root", "moderator", "mod", "null"]


def check_username():
    username = input("Enter username: ")

    if username == "":
        return False
    if " " in username:
        return False
    if username.lower() in BANNED_WORDS:
        return False

    return True


def check_email():
    email = input("Enter email: ")

    if "@" in email and "." in email:
        return True
    return False


def check_display_name(username):
    display_name = input("Enter display name: ")

    # If left empty, default to the provided username
    if display_name == "":
        display_name = username

    # Between 3 and 20 characters long
    if len(display_name) < 3 or len(display_name) > 20:
        return False

    # Must start with a letter
    if not display_name[0].isalpha():
        return False

    # Only alphanumeric characters and underscores
    for char in display_name:
        if not (char.isalnum() or char == "_"):
            return False

    # Cannot be from banned wordlist
    if display_name.lower() in BANNED_WORDS:
        return False

    return display_name