a_friends = {"Rahim", "Karim", "Sakib", "Jamal"}
b_friends = {"Sakib", "Jamal", "Rafiq", "Nadim"}

mutual_friend = a_friends.intersection(b_friends)
# print(mutual_friend)
unique_to_A = a_friends - mutual_friend
unique_to_B = b_friends - mutual_friend

total_unique_friends = a_friends.union(b_friends)

print(f"Mutual friends: {mutual_friend}")
print(f"Unique to A: {unique_to_A}")
print(f"Unique to B: {unique_to_B}")
print(f"Total unique friends: {len(total_unique_friends)}")