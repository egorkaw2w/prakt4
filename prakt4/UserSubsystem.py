class UserSubsystem:
    def __init__(self):
        self.users = []

    def register_user(self, name, email, password):
        user = User(name, email, password)
        self.users.append(user)

    def authenticate_user(self, email, password):
        for user in self.users:
            if user.email == email and user.password == password:
                return True
        return False