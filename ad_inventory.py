import pandas as pd

ads_data = [
    {"ad_id": "ad_1", "ad_title": "Running Shoes", "ad_description": "Comfortable and lightweight running shoes for daily joggers."},
    {"ad_id": "ad_2", "ad_title": "Yoga Mat", "ad_description": "Eco-friendly yoga mat with extra grip and cushioning."},
    {"ad_id": "ad_3", "ad_title": "AI Learning Platform", "ad_description": "Master AI with practical coding challenges and expert videos."},
    {"ad_id": "ad_4", "ad_title": "Netflix Subscription", "ad_description": "Unlimited movies and TV shows on all your devices."},
    {"ad_id": "ad_5", "ad_title": "Financial Planning App", "ad_description": "Smart budgeting and financial tracking app for young professionals."},
    {"ad_id": "ad_6", "ad_title": "Gaming Headset", "ad_description": "Immersive surround sound headset with noise-cancellation."},
    {"ad_id": "ad_7", "ad_title": "Coding Bootcamp", "ad_description": "Join our intensive bootcamp and become a full-stack developer."},
    {"ad_id": "ad_8", "ad_title": "algorithms Bootcamp", "ad_description": "Join our intensive bootcamp and become a algorithms developer."}
]

ads_df = pd.DataFrame(ads_data)
