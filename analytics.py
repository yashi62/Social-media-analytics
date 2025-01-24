import pandas as pd
from database import Database

class Analytics:
    def __init__(self):
        self.db = Database()

    def get_summary_metrics(self):
        posts = self.db.get_posts()
        interactions = self.db.get_interactions()
        total_posts = posts.shape[0]
        total_interactions = interactions.shape[0]
        unique_users = interactions['user_id'].nunique()

        return {
            'total_posts': total_posts,
            'total_interactions': total_interactions,
            'unique_users': unique_users
        }

    def get_engagement_metrics(self):
        interactions = self.db.get_interactions()
        engagement_by_type = interactions.groupby('interaction_type').size().reset_index(name='count')
        return engagement_by_type.to_dict(orient='records')

    def get_content_performance(self):
        posts = self.db.get_posts()
        interactions = self.db.get_interactions()

        performance = interactions.groupby('post_id').size().reset_index(name='interaction_count')
        performance = performance.merge(posts, on='post_id', how='left')
        performance = performance[['post_id', 'title', 'interaction_count']].sort_values(by='interaction_count', ascending=False)
        return performance.to_dict(orient='records')

    def get_user_activity(self):
        interactions = self.db.get_interactions()
        activity = interactions.groupby('user_id').size().reset_index(name='interaction_count')
        return activity.to_dict(orient='records')
