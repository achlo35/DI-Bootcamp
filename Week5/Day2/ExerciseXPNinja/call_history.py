class Phone():
    def __init__(self, phone_number):
        self.number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        call_str = f'{self.number} called {other_phone.number}'
        print(call_str)
        self.call_history.append(call_str)

    def show_call_history(self):
        print(f'Call History : {self.call_history}')

    def send_message(self, other_phone,content):
        message = {
            'to' : other_phone.number,
            'from' : self.number,
            'content' : content
        }
        self.messages.append(message)
        print(f"Message sent from {self.number} to {other_phone.number}: {content}")

    def show_outgoing_messages(self):
        print(f'Outgoing Messages from {self.number}:')
        for message in self.messages:
            if message['from'] == self.number:
                print(f"To: {message['to']}, Content: {message['content']}")
    
    def show_incoming_messages(self):
        print(f'Incoming Messages to {self.number}:')
        for message in self.messages:
            if message['to'] == self.number:
                print(f"From: {message['from']}, Content: {message['content']}")
    
    def show_message_from(self):
        print(f'Messages sent to {self.number}:')
        for message in self.messages:
            if message['to'] == self.number:
                print(f"From: {message['from']}, Content: {message['content']}")
    
# Create two phone objects
phone1 = Phone("123-456-7890")
phone2 = Phone("987-654-3210")

# Test calling
phone1.call(phone2)
phone2.call(phone1)

# Show call history
phone1.show_call_history()
phone2.show_call_history()

# Test sending messages
phone1.send_message(phone2, "Hello from phone1!")
phone2.send_message(phone1, "Hi, phone1! This is phone2.")

# Show outgoing messages
phone1.show_outgoing_messages()
phone2.show_outgoing_messages()

# Show incoming messages
phone1.show_incoming_messages()
phone2.show_incoming_messages()

# Show messages from a specific sender (for phone1)
phone1.show_message_from()
phone2.show_message_from()
