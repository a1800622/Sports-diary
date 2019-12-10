import os
import matplotlib.pyplot as chart

# importataan matplotlib.pyplot ja kutsutaan sitä kirjoittamalla "chart."
# samantapainen eka funktio kuin urheilupäiväkirja.py:ssä
def running():
    number = 1
    while number != 0:
        print("")
        print("-----------------")
        print("*******RUN*******")
        print("#1: \t New run")
        print("#2: \t Statistics")
        number = int(input("Enter 1 or 2. Enter 0 to go back: "))
        if number == 1:
            new_run()
        if number == 2:
            print("")
            print("----------STATISTICS-----------")
            stats()

def new_run():

# Syötetään lenkin pituus kilometreinä ja aika mm:ss tyyliin
    distance = float(input("Enter running distance in kilometers: "))
    time =(input("Enter time in MM:SS format: "))
    time = time.split(":") 
    minutes = int(time[0])
    seconds = int(time[1])
    
# Juoksunopeutta lasketaan
    running_pace = (minutes + (seconds/60)) / distance
    print("")
    print("------------------------------------")
    print("Your running pace was: "+ format(running_pace, ".1f") +" minutes/km" )
    print("------------------------------------")

# Kutsutaan compare() funktiota ja viedään juoksunopeus mukaan
    compare(running_pace)
    save = input("Type yes to save result: ")
    print(save)
    if save == "yes":
          print("Saving...")
          
# Kutsutaan save_run() johon juoksunopeutta viedään ja tallennetaan
          save_run(running_pace)

def save_run(running_pace):

# save_run() tallennus toimii samalla tavalla kuin tallennus diary.py:ssä
      temp_run = open('temp_run.txt','w')
      read_run = open('run_logs.txt','r')
      old_run = read_run.readline().rstrip("\n")
      while old_run !='':
            temp_run.write(old_run + "\n")
            print(old_run)
            old_run = read_run.readline().rstrip("\n")

      temp_run.write(str(running_pace) + "\n")
      temp_run.close()
      read_run.close()
      print("Saved run to log.")

      os.remove("run_logs.txt")
      os.rename("temp_run.txt", "run_logs.txt")

# Funktioon tulee juoksunopeus "running_pace" mukana
# Tämä funktio vertaa syötetyn tuloksen edelliseen tulokseen ja keskiarvoon
def compare(running_pace):

# While loop käy läpi 'run_logs.txt' ja vertaa viimeisen tuloksen if ja else lauseilla
      read_run = open('run_logs.txt','r')
      old_run = read_run.readline().rstrip("\n")
      while old_run !='':
            last_run = float(old_run)
            old_run = read_run.readline().rstrip("\n")
      if running_pace < last_run:
            status = last_run - running_pace
            print("Your run improved by " + format(status,".1f") +
                  " compared to your last run " + format(last_run,".1f"))
            print("------------------------------------")
      else:
            if running_pace > last_run:
                  status = running_pace - last_run
                  print("Your running pace was slower by " + format(status, ".1f") +
                  " compared to your last run " + format(last_run, ".1f"))
                  print("------------------------------------")
            else:
                  print("Your running pace (" + format(running_pace,".1f") +
                  ") is the same as your last run (" + format(last_run,".1f") + ")")
                  print("------------------------------------")

# Keskiarvo
# 'run_logs.txt' avataan uudestaan keskiarvon laskemista varten
      index = 0
      run_sum = 0
      read_run = open('run_logs.txt','r')
      old_run = read_run.readline().rstrip("\n")
      while old_run != '':
            index += 1
            run = float(old_run)
            run_sum += run
            avg = run_sum / index
            old_run = read_run.readline().rstrip("\n")

# omaa tulosta verrataan keskiarvoon if ja else lauseilla
      if running_pace < avg:
            status = avg - running_pace
            print("Your run " + format(running_pace,".1f") +
                  " was better than your average " + format(avg,".1f"))
            print("------------------------------------")
      else:
            if running_pace > avg:
                  status = running_pace - avg
                  print("Your run " + format(running_pace,".1f") +
                        " was worse than your average " + format(avg,".1f"))
                  print("------------------------------------")
            else:
                  print("Your running pace is the same as your average "
                        + format(avg,".1f"))
                  print("------------------------------------")
      read_run.close()

def stats():

# Eka while loop lause lukee ja tulostaa rivit. Samalla loop laskee
# montako riviä eli syöttöä on 'run_logs.txt':ssä indexin avulla
      read_run = open('run_logs.txt','r')
      old_run = read_run.readline().rstrip("\n")
      index = 0
      while old_run !='':
            print("{}: \t".format(index + 1) + old_run)
            index += 1
            old_run = read_run.readline().rstrip("\n")

# Tämän jälkeen 'run_logs.txt' avataan uudestaan ja luodaan
# tyhjä "runlist" array jossa on edellisen index:in määrä paikkoja
      read_run = open('run_logs.txt','r')
      runlist = [0] * index
      indexlist = 0

# While loop syöttää rivit "runlist":iin
      old_run = read_run.readline().rstrip("\n")
      while old_run !='':
            runlist[indexlist] = float(old_run)
            indexlist += 1
            old_run = read_run.readline().rstrip("\n")

# Tämän avulla pystytään tulostaa paras ja huonoin juoksunopeus.
      print("-------------------------------")
      print("Your best running pace is  " + str(min(runlist)))
      print("-------------------------------")
      print("Your worst running pace is " + str(max(runlist)))

# run_logs.txt avataan uudestaan jossa lasketaan
# keskiarvoa samalla tavalla kuin compare()funktiossa
      read_run = open('run_logs.txt','r')
      old_run = read_run.readline().rstrip("\n")
      index = 0
      run_sum = 0
      while old_run != '':
            index += 1
            run = float(old_run)
            run_sum += run
            avg = run_sum / index
            old_run = read_run.readline().rstrip("\n")
      print("-------------------------------")
      print("Your average running pace is " + format(avg,".1f"))
      print("-------------------------------")
      print("")

      chart = input("Type yes to see chart: ")
      if chart == "yes":

# Kutsutaan run_chart() funktio johon viedään "index" ja "runlist" array
            run_chart(index,runlist)
            input("Press enter to continue...")
      
def run_chart(index,runlist):

# Entries tekee array:n joka alkaa 1 ja loppuu indexin seuraavalla luvulla
# Esim: [1, ..., index + 1]
      entries = list(range(1, index + 1))

# .plot X suunta kertoo mikä tulos
# ja .plot Y suunta kertoo tuloksen arvosta
# .axis laittaa taulun pienimmät ja korkeimmat arvot
      chart.plot(entries,runlist,'bo')
      chart.ylabel("Running pace (minutes)")
      chart.xlabel("Run 1 to " + str(index))
      chart.axis([0,index + 1,0,20])
      chart.show()



