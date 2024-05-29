import datetime

class LoggingSystem:
    def __init__(self):
        self.log_file = "moderation_log.txt"

    def log_action(self, action, user, reason):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {action} by {user}: {reason}\n"
        
        with open(self.log_file, "a") as file:
            file.write(log_entry)

    def view_log(self):
        try:
            with open(self.log_file, "r") as file:
                log_contents = file.read()
                return log_contents
        except FileNotFoundError:
            return "Log file not found."

# Example of how to use the LoggingSystem class
# logger = LoggingSystem()
# logger.log_action("Kick", "User123", "Spamming in chat")
# print(logger.view_log())