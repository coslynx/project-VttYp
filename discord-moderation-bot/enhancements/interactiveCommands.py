enhancements/interactiveCommands.py:

# interactiveCommands.py

class InteractiveCommands:
    def __init__(self, user_id, command):
        self.user_id = user_id
        self.command = command

    def prompt_user(self):
        if self.command == "kick":
            reason = input("Please provide a reason for kicking the user: ")
            return f"Kicking user {self.user_id} for {reason}"
        elif self.command == "ban":
            duration = input("Please specify the ban duration: ")
            return f"Banning user {self.user_id} for {duration}"
        elif self.command == "mute":
            time = input("Please specify the mute duration: ")
            return f"Muting user {self.user_id} for {time}"
        else:
            return "Invalid command, please try again."

    def execute_command(self):
        if self.command in ["kick", "ban", "mute"]:
            return self.prompt_user()
        else:
            return "Command not supported."

# End of interactiveCommands.py