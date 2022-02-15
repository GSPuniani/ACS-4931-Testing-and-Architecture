# By Kami Bigdely
# Split temp variable

def save_into_db(info):
    print("Saved into database.")


username_input = input('Please enter your username: ')
save_into_db(username_input)
age_input = int(input('Please enter your birth year: '))
age = 2022 - age_input
print("You turn", age, "years old this year.")
