# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

def make_alert_sound():
    print('made alert sound.')

def make_accept_sound():
    print('made acceptance sound')

def has_harmful_ingredient(food_list):
    return 'sodium nitrate' in food_list or 'sodium benzoate' in food_list\
or 'sodium oxide' in food_list

ingredients = ['sodium benzoate']
if has_harmful_ingredient(ingredients):
    print('!!!')
    print('there is a toxin in the food!')    
    print('!!!')
    make_alert_sound()
else:
    print('***')
    print('Toxin Free')
    print('***')
    make_accept_sound()
