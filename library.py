# Task 3:
# Your task is to write a computer program that asks the user if they are looking for a fiction or a non fiction book.Based on the user answer the program will ask the user to choose genre from a list a list available geres.Finally the program will return the location from a to i of books of this genre.
fiction = {
    "A" : "COMEDY",
    "B" :  "COMIC/GRAPHIC NOVEL",
    "C" : "SCIENCE FICTION",
    "D" : "FANTASY",
    "E" : "HISTORICAL FICTION"
}
non_fiction ={
    "F" : "HISTORY & GEOGRAPHY",
    "G" : "ARTS",
    "H" : "SCIENCE & TECHNOLOGY",
    "I" :  "OTHER"
}
print("SELECT ANY ONE OPTION!")
print("ENTER 1 FOR 'FICTION'")
print("ENTER 2 FOR 'NON FICTION'")
c = int(input("Enter your choice here:"))
if c == 1:
    print("============FICTION=================")
    print("Choose the genre from the below list!!")
    print("'COMEDY'")
    print("'COMIC/GRAPHIC NOVEL'")
    print("'SCIENCE FICTION'")
    print("'FANTASY'")
    print("'HISTORICAL FICTION'")
    genre = input("Enter your choice here:")
    genre = genre.upper()
    for i,j in fiction.items():
        if genre == j:
            print("the location of this book is,",i,"shelf")
if c == 2:
    print("==========NON FICTION================") 
    print("Choose the genre from the below list!!")
    print("'HISTORY & GEOGRAPHY")
    print("'ARTS'")
    print("'SCIENCE & TECHNOLOGY")
    print("'HISTORY & GEOGRAPHY")
    genre = input("Enter your choice here:")
    genre = genre.upper()
    for i,j in non_fiction.items():
        if genre == j:
            print("the location of this book is",i,"shelf")
       




