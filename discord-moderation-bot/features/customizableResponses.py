class CustomizableResponses:
    def __init__(self):
        self.responses = {}

    def add_response(self, trigger, response):
        self.responses[trigger] = response

    def remove_response(self, trigger):
        if trigger in self.responses:
            del self.responses[trigger]

    def get_response(self, trigger):
        return self.responses.get(trigger, None)

    def get_all_responses(self):
        return self.responses

    def clear_all_responses(self):
        self.responses = {}