from top2vec import Top2Vec
import json


def load_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def dump_data(file_path, data):
    with open(file_path + '.json', 'w') as f:
        json.dump(data, f, indent=2)


def create_per_user_docs(file_path):
    all_users_docs = load_data(file_path)

    # Convert dict values to list for slicing (if necessary)
    doc_values = list(all_users_docs.values())  # or .items() if you want keys too

    # Split the first 140 documents into 10 users (14 docs each)
    num_users = 10
    docs_per_user = 14
    user_docs = {}

    for user_id in range(1, num_users + 1):
        start = (user_id - 1) * docs_per_user
        end = user_id * docs_per_user
        user_docs[f"user_{user_id}"] = doc_values[start:end]
    return user_docs

# Save this split if needed

def create_all_user_docs(file_path):
    """combines all user entries .
    returns list of strings"""
    with open(file_path, 'r') as f:
        user_docs = json.load(f)

    # Inverse mapping from user_docs to flat doc list
    user_ids = []
    
    per_user_docs=[]
    result=""
    for user_id, docs in user_docs.items():
        user_ids.append([user_id] * len(docs))
        for doc in docs:
            result=""
            
            for x in doc:
                for y in x:
                    result+=y
            per_user_docs.append(result)
    return per_user_docs
    

            
        
        

