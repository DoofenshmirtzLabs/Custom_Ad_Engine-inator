from datetime import datetime, timedelta
import json
from collections import defaultdict


def groupby_data(messages):
   

    grouped = defaultdict(list)

    for message in messages:
        ts = message.get("timestamp")
       
        text = message.get("message")
       
        if not ts or not text:
            continue
        
    
        grouped[ts].append(text)
    return grouped
def filter_last_n_days(grouped, output_file):
    

        cutoff_date = datetime.now()
        result = {}
        
        for date_str, messages in grouped.items():
           
                date_obj = datetime.strptime(date_str, "%Y-%m-%d")
                
                result[date_str] = messages
        
        print("filtering succesful")

        with open(output_file, 'w') as f:
            json.dump(result, f, indent=4)
        return True
    