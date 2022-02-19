# by Kami Bigdely
# Extract class

class Actor:
    def __init__(self, first_name, last_name, birth_year, movies, email) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.movies = movies
        self.email = email
    
    def send_hiring_email(self):
        print("Email sent to: ", self.email)


elizabeth_debicki = Actor("Elizabeth", "Debicki", 1990, \
    ['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'], 'deb@makeschool.com')

jim_carrey = Actor("Jim", "Carrey", 1962, \
    ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man'], 'jim@makeschool.com')

actors = [elizabeth_debicki, jim_carrey]
    
for actor in actors:
    if actor.birth_year > 1985:
        print(actor.first_name, actor.last_name)
        print('Movies Played: ', end='')
        for m in actor.movies:
            print(m, end=', ')
        print()
        actor.send_hiring_email()
