import diary

# Yksinkertainen alkusivu
# numeroa 1-3 syötetään ja se vie sivuille if-lauseella,
# while-loop loppuu jos syötetään 0.

def main():
    number = 1
    while number != 0:
        print('')
        print("------------------------------")
        print("Welcome to my sports diary!")
        print("------------------------------")
        print("#1 \t New entry")
        print("#2 \t Diary")
        print("#3 \t Running")
        number = int(input("Enter a number, 1 to 3. Enter 0 to exit: "))
        if number == 1:
            diary.new_entry()
        if number == 2:
            diary.diary()
        if number == 3:
            print("running.running()")
    print(number)
main()
