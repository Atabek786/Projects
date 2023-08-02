import art
import random

responses = ['Oookay', 'Good choice!', 'Gotchaaa', 'Alright then!', "You don't need me :( "]

study_list = {
    'math': ['Algebra', 'Calculus', 'Geometry', 'Statistics', 'Trigonometry', 'Number Theory'],
    'geography': ['Continents', 'Countries', 'Capital Cities', 'Physical Features', 'Oceans', 'Mountains'],
    'history': ['Ancient Civilizations', 'World Wars', 'Renaissance', 'Industrial Revolution', 'Middle Ages', 'American Revolution'],
    'biology': ['Cell Biology', 'Genetics', 'Ecology', 'Anatomy', 'Evolution', 'Botany'],
    'computer science': ['Programming', 'Data Structures', 'Algorithms', 'Web Development', 'Machine Learning', 'Artificial Intelligence'],
}

book_list = {
    'horror': [
        'The Shining',
        'It',
        'Dracula',
        'Frankenstein',
        'Bird Box',
        'The Exorcist',
        'House of Leaves',
    ],
    'fantasy': [
        'The Hobbit',
        "Harry Potter and the Sorcerer's Stone",
        'The Name of the Wind',
        'Mistborn: The Final Empire',
        'The Way of Kings',
        'The Lord of the Rings Trilogy',
        'Game of Thrones',
    ],
    'science fiction': [
        'The Blazing World and Other Writings by Margaret Cavendish (1666)',
        'Frankenstein by Mary Wollstonecraft Shelley',
        'The Time Machine by H.G. Wells (1895)',
        'The War of the Worlds by H.G. Wells (1897)',
        'Dune by Frank Herbert',
        'Neuromancer by William Gibson',
    ],
    'romance': [
        'Pride and Prejudice, by Jane Austen (1813)',
        'Jane Eyre, by Charlotte Brontë (1847)',
        'Shanna, by Kathleen E. Woodiwiss (1977)',
        'Morning Glory, by Lavyrle Spencer (1993)',
        'The Viscount Who Loved Me, by Julia Quinn (2000)',
        'Outlander by Diana Gabaldon',
        'The Notebook by Nicholas Sparks',
    ],
}

sport_list = {
    'active sports': ['Baseball', 'Football', 'Soccer', 'Skiing', 'Boxing', 'Basketball', 'Tennis'],
    'passive sports': ['Camping', 'Hiking', 'Walking', 'Fishing', 'Swimming', 'Yoga', 'Pilates'],
}

game_list = {
    'action': ['Call of Duty', "Assassin's Creed", 'GTA V', 'Red Dead Redemption', 'Battlefield', 'Halo'],
    'adventure': ['The Legend of Zelda', 'Uncharted', 'Tomb Raider', 'God of War', 'Far Cry', 'Assassin’s Creed Valhalla'],
    'puzzle': ['Portal', 'Candy Crush', 'Tetris', 'Portal 2', 'Sudoku', 'Minesweeper'],
    'horror': ['Outlast', 'Outlast 2', 'Amnesia', 'Resident Evil 2', 'Silent Hill', 'Dead Space'],
}

cook_list = {
    'italian': ['Pasta Carbonara', 'Margherita Pizza', 'Tiramisu', 'Lasagna', 'Risotto', 'Panna Cotta'],
    'indian': ['Chicken Tikka Masala', 'Palak Paneer', 'Biryani', 'Gulab Jamun', 'Butter Chicken', 'Samosa'],
    'mexican': ['Tacos', 'Enchiladas', 'Guacamole', 'Churros', 'Quesadillas', 'Mole'],
    'turkish': ['Şiş Kebap', 'Döner', 'Köfte', 'Manti', 'Baklava', 'Lahmacun'],
    'arabic': ['Falafel', 'Baba Ganoush', 'Hummus', 'Tabbouleh', 'Shawarma', 'Kabsa'],
}

def main():
    print(art.text2art("What do you wanna do today?", font="ogre", chr_ignore=True))
    option = options()
    if option == 1:
        study()
    elif option == 2:
        sports()
    elif option == 3:
        books()
    elif option == 4:
        game()
    elif option == 5:
        cook()
    else:
        print("That's it for today, good luck!")



def options():
    try:
        n = input("P.S if you don't know what to do, press 1 so that I could help you :) | ")
        if n != '1':
            print(random.choice(responses))
        else:
            options = int(input("Select an activity to do today: \n 1 study \n 2 sport \n 3 read \n 4 game \n 5 cook\n Answer: "))
            if options not in [1,2,3,4,5]:
                raise Exception()
            else:
                return options
    except (ValueError, Exception):
        print("Please don't prompt weird symbols :(")

def study():
    print("Select a subject to study:")
    for i, subject in enumerate(study_list, 1):
        print(f"{i}. {subject.capitalize()}")
    choice = int(input("Enter the number of the subject you want to study: "))
    if 1 <= choice <= len(study_list):
        subject = list(study_list.keys())[choice - 1]
        print(f"Great choice! Here are some topics in {subject.capitalize()}:")
        for topic in study_list[subject]:
            print(f"- {topic}")
    else:
        print("Invalid choice. Please try again.")

def sports():
    print("Select a type of sport:")
    for i, sport_type in enumerate(sport_list, 1):
        print(f"{i}. {sport_type.capitalize()}")
    choice = int(input("Enter the number of the sport type you want to do: "))
    if 1 <= choice <= len(sport_list):
        sport_type = list(sport_list.keys())[choice - 1]
        print(f"Enjoy your {sport_type} activities! Here are some options:")
        for sport in sport_list[sport_type]:
            print(f"- {sport}")
    else:
        print("Invalid choice. Please try again.")

def books():
    print("Select a genre:")
    for i, genre in enumerate(book_list, 1):
        print(f"{i}. {genre.capitalize()}")
    choice = int(input("Enter the number of the genre you want to read: "))
    if 1 <= choice <= len(book_list):
        genre = list(book_list.keys())[choice - 1]
        print(f"Happy reading! Here are some books in the {genre.capitalize()} genre:")
        for book in book_list[genre]:
            print(f"- {book}")
    else:
        print("Invalid choice. Please try again.")

def game():
    print("Select a game genre:")
    for i, genre in enumerate(game_list, 1):
        print(f"{i}. {genre.capitalize()}")
    choice = int(input("Enter the number of the game genre you want to play: "))
    if 1 <= choice <= len(game_list):
        genre = list(game_list.keys())[choice - 1]
        print(f"Have fun gaming! Here are some {genre.capitalize()} games:")
        for game in game_list[genre]:
            print(f"- {game}")
    else:
        print("Invalid choice. Please try again.")

def cook():
    print("Select a cuisine:")
    for i, cuisine in enumerate(cook_list, 1):
        print(f"{i}. {cuisine.capitalize()}")
    choice = int(input("Enter the number of the cuisine you want to cook: "))
    if 1 <= choice <= len(cook_list):
        cuisine = list(cook_list.keys())[choice - 1]
        print(f"Enjoy cooking some delicious {cuisine.capitalize()} dishes!")
        print("Here are some popular dishes:")
        for dish in cook_list[cuisine]:
            print(f"- {dish}")
    else:
        print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
