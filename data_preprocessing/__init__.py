from data_preprocessing.exctration import load_data,extract_user_messages
from data_preprocessing.preprocessing import clean_data,preprocess
from data_preprocessing.utils import dump_user_data
from contextmanager.Manager import userContext
def data_preprocessing_pipeline():
    file_path=f"{userContext.username}_conversation.py"
    user_data=load_data(file_path)
    user_messages=extract_user_messages(user_data)
    cleaned_timestamp_messages = []
    for item in user_messages:
        cleaned_message = preprocess(item['message'])
        cleaned_item = {'message': cleaned_message, 'timestamp': item['timestamp']}
        cleaned_timestamp_messages.append(cleaned_item)
    file_path=f"{userContext.user_name}_user_data"
    dump_user_data(file_path,cleaned_timestamp_messages)