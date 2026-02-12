import json


def process_seed_data():
    print("Starting background seed...")
    try:
        with open("users_with_posts.json", "r") as f:
            users = json.load(f)
            for user in users:
                try:
                    value = json.dumps(user).encode("utf-8")
                    send_user(producer, value)
                    print(f"Sent user: {user.get('email')}")
                    sleep(5)
                except Exception as e:
                    print(f"Error sending user: {e}")
    except Exception as e:
        print(f"File error: {e}")