import json
from collections import defaultdict
import datetime

def load_data(file_path):
    return json.load(file_path)

def groupby_data(messages):
   

    grouped = defaultdict(list)

    for message in messages:
        ts = message.get("timestamp")
        text = message.get("text")
        if not ts or not text:
            continue

        date_str = datetime.date.fromtimestamp(ts).strftime("%Y-%m-%d")
        grouped[date_str].append(text)
    return grouped
