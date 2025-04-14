from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from top2vec import Top2Vec
from ad_inventory import ads_data
ad_texts=ads_data
model=Top2Vec.load("top2vec_h_allusers_ad_model")

# Step 1: Embed ad texts
ad_vectors = model._embed_documents(ad_texts, batch_size=32)

# Step 2: Compare each ad to all topic vectors
topic_vectors = model.topic_vectors  # shape: (num_topics, embedding_dim)
cos_sim = cosine_similarity(ad_vectors, topic_vectors)  # shape: (num_ads, num_topics)

# Step 3: For each ad, pick top topic and score
ad_topics = cos_sim.argmax(axis=1)
ad_scores = cos_sim.max(axis=1)

# Step 4: Create ad-topic matrix
num_topics = len(topic_vectors)
ad_topic_matrix = np.zeros((len(ad_texts), num_topics))

for i, topic in enumerate(ad_topics):
    ad_topic_matrix[i][topic] = ad_scores[i]  # or just 1 for binary match

# Step 5: Final DataFrame
import pandas as pd

ad_topic_df = pd.DataFrame(ad_topic_matrix, columns=[f"topic_{i}" for i in range(num_topics)])
ad_topic_df["ad_id"] = range(len(ad_texts))
ad_topic_df["ad_text"] = ad_texts
ad_topic_df.to_excel("ad_score_df.xlsx")
