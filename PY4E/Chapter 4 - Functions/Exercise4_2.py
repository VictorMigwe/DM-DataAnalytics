# Exercise 4.2:  Move the last line of this program to the top, so the function call appears before the definitions. Run the program and see what error message you get.
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')


def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()


##########
#This is the error: NameError: name 'repeat_lyrics' is not defined
        
#repeat_lyrics()
#def print_lyrics():
#    print("I'm a lumberjack, and I'm okay.")
#    print('I sleep all night and I work all day.')


#def repeat_lyrics():
#   print_lyrics()
#    print_lyrics()