class UserReputationSystem:
    def __init__(self):
        self.user_reputation = {}

    def add_reputation(self, user_id, points):
        if user_id in self.user_reputation:
            self.user_reputation[user_id] += points
        else:
            self.user_reputation[user_id] = points

    def remove_reputation(self, user_id, points):
        if user_id in self.user_reputation:
            self.user_reputation[user_id] -= points
            if self.user_reputation[user_id] < 0:
                self.user_reputation[user_id] = 0

    def get_reputation(self, user_id):
        return self.user_reputation.get(user_id, 0)

    def reset_reputation(self, user_id):
        if user_id in self.user_reputation:
            self.user_reputation[user_id] = 0

    def update_reputation(self, user_id, action):
        if action == 'positive':
            self.add_reputation(user_id, 1)
        elif action == 'negative':
            self.remove_reputation(user_id, 1)
        elif action == 'bonus':
            self.add_reputation(user_id, 5)
        elif action == 'penalty':
            self.remove_reputation(user_id, 5)
        else:
            print("Invalid action for updating reputation.")

# Instantiate the UserReputationSystem
user_rep_system = UserReputationSystem()