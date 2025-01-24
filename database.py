import pandas as pd

class Database:
    def __init__(self):
        self.posts = pd.read_csv('data/posts.csv')
        self.interactions = pd.read_csv('data/interactions.csv')
        self.users = pd.read_csv('data/users.csv')

    def get_posts(self):
        return self.posts

    def get_interactions(self):
        return self.interactions

    def get_users(self):
        return self.users
