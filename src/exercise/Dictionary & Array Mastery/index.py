raw_data = [
    {"user_id": 1, "name": "Alice", "tags": ["admin", "active"], "score": [85, 90, 92]},
    {"user_id": 2, "name": "Bob", "tags": ["user"], "score": 92},
    {"user_id": 3, "name": "Charlie", "tags": ["admin", "inactive"], "score": 78},
]

# Function to filter users by tag
def filter_users_by_tag(data, tag=[]):
    filtered_users = []
    if not tag or not data or len(tag) == 0:
        return filtered_users
    for user in data:
        list_arr = user["tags"]
        if list_arr == tag:
            filtered_users.append(user)
            break
    return filtered_users




# Function to calculate the average score of filtered users
def calculate_average_score(data):
    scoreTotal = 0
    if not data:
        return 0
    for cuser in data:

        print(f"User: {cuser['name']}, Score: {cuser['score']}")

        total_sum = sum(score for score in cuser['score'])

        # for score in cuser['score']:
        #     print (f"Adding score: {score}")

        # total_sum = sum(score for user in data for score in user['score'])

        return total_sum


if __name__ == "__main__":

    admin_users = filter_users_by_tag(raw_data, ["admin", "active"])

    print("Filtered Admin Users-------------------------------------")


    print(calculate_average_score(admin_users))
