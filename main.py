class User:# creating a class
    #constructor
    def __init__(self, user_id, username):
        #define attributes
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    #method, self param needed for identifying objects
    def follow(self, user):
        user.followers += 1
        self.following += 1

#create object
user_1 = User("001", "stick")
user_2 = User("002", "o")
user_3 = User("003", "king")

user_1.follow(user_2)

print(user_1.followers)
print(user_2.followers)
print(user_1.following)
print(user_2.following)

