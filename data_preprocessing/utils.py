import json
def dump_user_data(filepath,data):
    try:
        # Use 'with' statement for automatic file closing
        with open(filepath, 'w', encoding='utf-8') as f:  # Specify encoding
            json.dump(data, f, indent=4)  # Use json.dump, and add indent for readability
        return True
    except (IOError, OSError) as e:
        print(f"Error occurred during dumping user data to {filepath}: {e}")
        return False
    except json.JSONEncodeError as e:
        print(f"Error: Data is not JSON serializable: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

        