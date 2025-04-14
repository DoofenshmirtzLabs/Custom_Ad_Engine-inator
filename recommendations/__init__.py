import pandas as pd
import numpy as np
from ad_topic_modeling import ad_topic_df
from topic_modeling import user_topics_df
from utils import visualize




# 1. Get just the topic vectors
user_topic_matrix = user_topics_df.drop(columns=["user_id"]).values  # shape: (num_users, num_topics)
ad_topic_matrix = ad_topic_df.drop(columns=["ad_id", "ad_text"]).values  # shape: (num_ads, num_topics)

# 2. Compute similarity: (num_users x num_ads) matrix
similarity_scores = np.dot(user_topic_matrix, ad_topic_matrix.T)  # shape: (num_users, num_ads)

# 3. For each user, get top N ads
top_n = 3
top_ads_per_user = np.argsort(-similarity_scores, axis=1)[:, :top_n]  # indices of top N ads per user

# 4. Store recommendations as a DataFrame
user_recommendations = []

for user_idx, ad_indices in enumerate(top_ads_per_user):
    user_id = user_topics_df.loc[user_idx, "user_id"]
    for rank, ad_idx in enumerate(ad_indices):
        user_recommendations.append({
            "user_id": user_id,
            "ad_id": ad_topic_df.loc[ad_idx, "ad_id"],
            "ad_text": ad_topic_df.loc[ad_idx, "ad_text"],
            "score": similarity_scores[user_idx, ad_idx],
            "rank": rank + 1
        })

recommendation_df = pd.DataFrame(user_recommendations)
visualize(user_topics_df,recommendation_df)
