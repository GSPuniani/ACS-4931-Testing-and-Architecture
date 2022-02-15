# by Kami Bigdely
# Rename Method
# Reference: https://parade.com/1039985/marynliles/pick-up-lines/

def calculate_area_under_graph(graph):   # DONE: Rename this function to reflect what it's doing.
    """Calculate the area under the input graph."""
    # bla bla bla.
    pass

#####################

def get_max_value(li):  # DONE: Rename this function to reflect what it's doing.
    max = li[0]
    for value in li:
        if value > max:
            max = value
    return max


li = [5, -1, 43, 32, 87, -100]
print(get_max_value(li))

############################
def split_sentence_into_list(sentence):  # DONE: Rename this function to reflect what it's doing.
    words = sentence[:].split(' ')
    return words

print(split_sentence_into_list('If you were a vegetable, you’d be a ‘cute-cumber.'))
