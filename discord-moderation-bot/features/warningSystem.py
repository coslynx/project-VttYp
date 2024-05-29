class WarningSystem:
    def __init__(self):
        self.warnings = {}

    def issue_warning(self, user_id, reason):
        if user_id in self.warnings:
            self.warnings[user_id].append(reason)
        else:
            self.warnings[user_id] = [reason]

    def get_warnings(self, user_id):
        if user_id in self.warnings:
            return self.warnings[user_id]
        else:
            return []

    def clear_warnings(self, user_id):
        if user_id in self.warnings:
            del self.warnings[user_id]