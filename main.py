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
    print("4: exit")
    
class Book: 
    def __init__(self, title, location, stock):
        self.title = title
        self.location = location
        self.stock = stock

def user_selection():
    while(True):
        display_menu()
        number = str(input("\nEnter a number 1-4: "))
        if(number == "1"):
            print("\nLets find your book!")
            while():    
                genre = input("Enter the genre first, is it fiction or non-fiction: ")
                if(genre != fiction or non-fiction):
                    print("check you spelling!")
            input("Now enter the authors name: ")

        elif(number == "2"):
            print("\nCheck out a book")
            input("What book are you checking out? ")
            print("Great choice! Go to the front desk, scan your card and the book, then it's all yours... for a month!")
        elif(number == "3"):
            print("\nReturn a book")
            print("I hope you loved it! Go to the front desk, there they will scan the book and clear your name.")
        elif(number == "4"):
            print("\nend")
            print("Thank you for chatting, see you next time!")
            break
        else:
            print("\nnot valid input, enter number 1-4")
user_selection()
