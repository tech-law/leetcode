class User:
    def __init__(self, username:str, name:str, email:str) -> None:
        self.username = username
        self.name = name
        self.email = email

    def __str__(self):
        return f"User(username='{self.username}', name='{self.name}', email='{self.email}')"

    def __repr__(self) -> str:
        return self.__str__()




class UserDatabase:
    def __init__(self) -> None:
        self.users = []

    def insert(self, user:User):

        i=0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i+=1
        self.users.insert(i, user)

    def find(self, username: str):
        for user in self.users:
            if user.username == username:
                return user    

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email    

    def list_all(self):
        return self.users

krupakar = User("kmanukon", "Krupakar", "kmanukon@sscinc.com")
ayaansh = User("amanukon", "Ayaansh", "amanukon@gmail.com")
nivansh = User("nmanukon", "Nivansh", "nmanukon@gmail.com")

database = UserDatabase()
database.insert(krupakar)
database.insert(ayaansh)
database.insert(nivansh)

print(database.list_all())
