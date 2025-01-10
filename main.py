import random
print("Welcome to your public library chat-bot! I can answer many questions you may have, but first...")
name = input("What's your name? ")
age = input("Hello " + name + ", How old are you? ")
print("It's very nice to meet you " + name + "! So, how can I help you?")
def display_menu():
    print("\n **Book Store**")
    print("1: Find a book")
    print("2: Check out a book")
    print("3: Return a book")
    print("4: Recommend a book")
    print("5: exit")
    
class Book: 
    def __init__(self, title, location, stock):
        self.title = title
        self.location = location
        self.stock = stock

def user_selection():
    while(True):
        display_menu()
        number = str(input("\nEnter a number 1-5: "))
        if(number == "1"):
            print("\nLets find your book!")
            while(True):    
                genre = input("Enter the genre first, is it fiction or non-fiction: ")
                if(genre == "fiction" or "non-fiction"):
                    break
                else:
                    print("Check your spelling!")
            author = input("Now enter the first letter of the authors last name: ")
            if(genre == "fiction"):
                print("Go to the second story and find the '" + author + "' section, then search the shelves for your book!")
            elif(genre == "non-fiction"):
                print("Go to the first story and find the '" + author + "' section, then search the shelves for your book!")

        elif(number == "2"):
            print("\nCheck out a book")
            input("What book are you checking out? ")
            print("Great choice! Go to the front desk, scan your card and the book, then it's all yours... for a month!")
        elif(number == "3"):
            print("\nReturn a book")
            print("I hope you loved it! Go to the front desk, there they will scan the book and clear your name.")
        elif(number == "4"):
            if(int(age) < 8):
                print("Based on your age, I recommend the book 'Captain Underpants'!")
            if(int(age) < 12):
                print("Based on your age, I recommend the book 'Eragon'!")
            if(int(age) < 16):
                print("Based on your age, I recommend the series 'The Lord of the Rings'!")
            if(int(age) < 25):
                print("Based on your age, I recommend the series 'A Game of Thrones'!")
            else:
                print("Based on your age, I recommend the book 'Romeo and Juliet'!")
            
        elif(number == "5"):
            print("\nend")
            print("Thank you for chatting, see you next time!")
            break
        else:
            print("\nnot valid input, enter number 1-4")
user_selection()
