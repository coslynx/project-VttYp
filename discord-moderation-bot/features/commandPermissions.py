filename: commandPermissions.py

class CommandPermissions:
    def __init__(self):
        self.permissions = {}

    def set_permission(self, command, role):
        self.permissions[command] = role

    def check_permission(self, command, user_roles):
        if command in self.permissions:
            required_role = self.permissions[command]
            if required_role in user_roles:
                return True
        return False