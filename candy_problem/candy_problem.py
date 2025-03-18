def get_friends_favorite_candy_count(friend_favorites):
    dict_count = {}

    for friend in friend_favorites:
        name,candies = friend
        
        for candy in candies:
            if candy in dict_count:
                dict_count[candy] += 1
            else:
                dict_count[candy] = 1

    return dict_count
# -------------------------
def create_new_candy_data_structure(friends_favorite):
    
    # candy_name_dict = {}
    # for i in range(len(friend_favorites)):
    #     # friends_favorite[i] = ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]]
    #     for candy in friends_favorite[i][1]:

    #         if candy not in candy_name_dict:
    #                 candy_name_dict[candy] = []
    #                 candy_name_dict[candy].append(friends_favorite[i][0])

    #         else:
    #             candy_name_dict[candy].append(friends_favorite[i][0])

    # return candy_name_dict
    
    # second option:
    candy_name_dict = {}

    for friend in friend_favorites:
        name,candies = friend
        
        for candy in candies:
            if candy in candy_name_dict:
                candy_name_dict[candy] = []
                candy_name_dict[candy].append(name)
            else:
                candy_name_dict[candy].append(name)

    return candy_name_dict

# -----------------------------
def get_friends_who_like_specific_candy(data, candy_name):
    pass

def create_candy_set(data):
    pass 
# ------------------------------
friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]

# print(get_friends_favorite_candy_count(friend_favorites))
print(create_new_candy_data_structure(friend_favorites))