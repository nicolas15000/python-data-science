print("Yo ! T’as pas un 06 ?")
quotes = ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", "On doit pouvoir choisir entre s'écouter parler et se faire entendre."]

characters = ["alvin et les Chipmunks", "Babar", "betty boop", "calimero", "casper", "le chat potté", "Kirikou"]

def get_random_item_in(my_list):
    # get a random number
    item = my_list[0] # get a quote from a list
    return item # return the item

user_answer = "A"

while user_answer != "B":
    print(get_random_item_in(quotes))