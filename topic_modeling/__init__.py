from utils import create_all_user_docs,create_per_user_docs,load_data,dump_data
from top2vec import Top2Vec
import pandas as pd
import numpy as np
from collections import defaultdict
num_users:int=10
docs_per_user:int=14
file_path = "C:\\Users\\user\\top2vec_all_filtered_data"
user_docs=create_per_user_docs(file_path)

dump_data("user_docs_per_user", user_docs)
user_docs_file_path="C:\\Users\\user\\user_docs_per_user"
docs_values=create_all_user_docs(user_docs_file_path)

# Remaining 7 documents
leftover_docs = docs_values[num_users * docs_per_user:]
dump_data("leftover_user_docs", leftover_docs)

# Verify
print(f"Created user_docs for {len(user_docs)} users")
print(f"Leftover docs: {len(leftover_docs)}")


model = Top2Vec(
    documents=docs_values,
 
    speed="deep-learn",
    hdbscan_args={
        'min_cluster_size': 2,    # try lowering this to get more topics
        'min_samples': 2,          # controls density sensitivity
        'cluster_selection_epsilon': 0.5  # 0.0 means default, raise to get more/finer clusters
    },
    verbose=True
)
num_topics=model.get_num_topics()
model.save("top2vec_h_allusers_ad_model")
num_docs=len(model.documents)
doc_ids=[num for num in range(num_docs)]
####creating USER_TOPIC_DF#####
topic_nums, topic_scores, topic_words, topic_word_scores =model.get_documents_topics(doc_ids)


num_docs_per_user = 14
num_users = len(topic_nums) // num_docs_per_user

# This will store one row per user
user_topic_distributions = []

for user_id in range(num_users):
    start = user_id * num_docs_per_user
    end = start + num_docs_per_user

    user_topics = topic_nums[start:end]
    user_scores = topic_scores[start:end]

    topic_score_map = defaultdict(list)

    for topic, score in zip(user_topics, user_scores):
        topic_score_map[topic].append(score)

    # Average topic scores
    avg_topic_scores = {f'topic_{k}': np.mean(v) for k, v in topic_score_map.items()}
    avg_topic_scores['user_id'] = f'user_{user_id}'

    user_topic_distributions.append(avg_topic_scores)

# Convert to DataFrame
user_topics_df = pd.DataFrame(user_topic_distributions)

# Fill missing topic columns with 0.0
user_topics_df = user_topics_df.fillna(0.0)

# Optional: Move user_id to first column
cols = ['user_id'] + [col for col in user_topics_df.columns if col != 'user_id']
user_topics_df = user_topics_df[cols]


user_topics_df.to_excel("user_topic_df.xlsx")


