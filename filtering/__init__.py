from utils import load_data,groupby_data
from contextmanager.Manager import userContext
from filter import filter_last_n_days

def filtering_pipeline():
    file_path=f"{userContext.username}_user_data"
    data=load_data(file_path)
    grouped_data=groupby_data(data)
    output_file_path=f"{userContext.username}_filtered_data"
    if not filter_last_n_days(groupby_data,output_file_path):
        pass


    