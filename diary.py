import os
# Importataan "os" väline jolla voidaan
# muokata tiedoston nimiä ja poistaa tiedostoja


def new_entry():

# Avataan "temp_diary.txt" muokattavaksi ja "diary.txt" luettavaksi
    temp_entry = open('temp_diary.txt','w')
    read_diary = open('diary.txt','r')
    
# Perus syötöt, käyttäjä voi syöttää kenttiin mitä vaan
    date = input("Add date: ")
    topic = input("Add a topic: ")
    note = input("Add a note: ")

# Syötöt tallennetaan tässä muodossa esim: 12.12.2019~aihe~viesti
    diary_log = date + "~" + topic + "~" + note
    
# old_entries lukee "diary.txt" while-loopissa rivi kerrallaan
# .rstrip("\n") poistaa rivinvaihdon rivistä
# temp_entry syöttää old_entries rivin 'temp_diary.txt' sisään
    old_entries = read_diary.readline().rstrip("\n")
    while old_entries !='':
        temp_entry.write(old_entries + "\n")
        old_entries = read_diary.readline().rstrip("\n")

# temp_entry kirjoittaa uusimman syötön ja molemmat tiedostot suljetaan        
    temp_entry.write(diary_log + "\n")
    temp_entry.close()
    read_diary.close()
    print("Saved new entry to diary.")
    input("Press enter continue...")
    
# os.remove komento poistaa "diary.txt" tiedoston ja
# os.rename muuttaa "temp_diary.txt" tiedoston nimen "diary.txt"
    os.remove("diary.txt")
    os.rename("temp_diary.txt","diary.txt")
    
# edellinen funktio loppuu ja diary funktio alkaa
def diary():
    index =  1
    print("")
    print("----------------------------------------")
    print("****************DIARY*******************")
    print("----------------------------------------")
    
# diary.txt avataan uudelleen luettavaksi ja read_diary
# toimii loopissa samalla tavalla kuin aiemmin
    read_diary = open('diary.txt','r')
    line = read_diary.readline().rstrip("\n")
    while line !='':

# .split("~") erottaa rivin array listaan ja
# "~" merkillä erotetaan stringit toisistaan ja tulostetaan ne
        entry = line.split("~")
        print("Entry #{}:\t ".format(index) +entry[0] + "\t" +entry[1])
        index +=1
        number = 1
        line = read_diary.readline().rstrip("\n")

# uusi while-loop jossa read_diary avaa 'diary.txt' uudelleen
# index edellisestä loopista kertoo montako riviä on tiedostossa esim "Enter 1 to 5"
    while number != 0:
        read_diary = open('diary.txt','r')
        row = 1
        print("")
        print("Enter 1 to {} to read the entry ".format(index - 1))
        number = int(input("Or enter 0 to go back: "))
        
# toinen while-loop loopin sisällä, .readline() käy 'diary.txt' rivit alusta
# ja siiryy ulos tulostamaan sen rivin, kun "row" on suurempi kuin syötetty numero
        while row <= number:
            line = read_diary.readline().rstrip("\n")
            entry = line.split("~")
            row += 1
            
# if lause ei tulosta mitään riviä kun syötetty numero on 0
        if number != 0 and number < index:
            print("----------------------------------------")
            print("DATE: " + entry[0] + " \tTOPIC: " + entry[1])
            print("----------------------------------------")
            print(entry[2])
    
# lopuksi diary.txt tiedostoa suljetaan
    read_diary.close()
