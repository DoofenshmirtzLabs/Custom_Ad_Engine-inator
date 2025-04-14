from data_preprocessing import data_preprocessing_pipeline
from filtering import filtering_pipeline
from topic_modeling import topic_modeling_pipeline
from ad_topic_modeling import ad_topic_modeling_pipeline
from recommendations import recommendations_pipeline
from contextmanager.Manager import ContextManager



if __name__=="__main__":
    userContext=ContextManager('abc')
    data_preprocessing_pipeline()
    filtering_pipeline()
    topic_modeling_pipeline()
    ad_topic_modeling_pipeline()
    recommendations_pipeline()