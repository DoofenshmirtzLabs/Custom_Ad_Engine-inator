import json
import datetime
def load_data(file_path):
    with open(file_path,'r') as f:
       return json.load(f)
def extract_user_messages_with_timestamps(data):
    conversations = data.get("conversations", [])
    user_data = []

    for convo in conversations:
        mapping = convo.get("mapping", {})
        for _, node in mapping.items():
            msg = node.get("message")
            if not msg:
                continue

            author = msg.get("author", {})
            if author.get("role") == "user" or author.get("role") == "assistant" :
                content_parts = msg.get("content", {}).get("parts", [])
                timestamp = msg.get("create_time")

                if content_parts:
                    # Convert Unix timestamp to readable datetime
                    readable_time = None
                    if timestamp:
                        readable_time = datetime.date.fromtimestamp(timestamp).isoformat()

                    for part in content_parts:
                        user_data.append({
                            "message": part,
                            "timestamp": readable_time
                        })

    return user_data

    return user_data
if __name__=="__main__":
    file_path='conversations.json'
    dummy=load_data(file_path)

    messages=extract_user_messages_with_timestamps(dummy)
