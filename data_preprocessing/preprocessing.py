import re
#cleaning the data
import spacy
nlp = spacy.load("en_core_web_sm")
def preprocess(text):
    processed = []
    
    doc = nlp(text)
    processed_tokens = [token.lemma_.lower().strip() for token in doc if not token.is_stop and not token.is_punct]
    processed.append(" ".join(processed_tokens))
    return processed
def clean_data(text):
    if str(type(text))=="<class 'str'>":
    
        text = text.strip()
        #text = re.sub(r"\s+", " ", text)
        text = re.sub(r"http\S+", "", text)  # remove URLs
        return text
    else:
        return ""
if __name__=="__main__":
    cleaned_timestamp_messages = []
    timestamp_messages=[]
    for item in timestamp_messages:
        cleaned_message = clean_data(item['message'])
        cleaned_message=preprocess(str(cleaned_message))
        cleaned_item = {'message': cleaned_message, 'timestamp': item['timestamp']}
        cleaned_timestamp_messages.append(cleaned_item)
