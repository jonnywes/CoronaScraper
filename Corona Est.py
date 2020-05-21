#rate 4% death
#11 days to show symptoms
#19 to death
#days to double 3

deathRate = .05
infected = 0
days_to_double = 3
population = 327200000
print("How many have died?")
dead = int(input())
def calcCase(deathRate, deaths, days_to_double, infected, population):
    deathNum = [dead,]
    counter = 19
    infected = deaths / deathRate
    print("estimated infected 19 days prior is", infected)
    #takes estimated time from infection to death (19 days)
    #and devides it by how many days it takes to double
    doubleRate = 19 / days_to_double
    #finds how many people could have been infected since the people who died where infect
    #also keeps track of how many people are projected to die in assosiation with the current infected count.
    print("-----------------PAST-----------------")
    for i in range(int(doubleRate)):
        counter -= days_to_double
        infected *= 2
        print("estimated infected {} days ago is {}".format(counter, int(infected)))
        deathNum.append(int(deathRate * infected))
    print("-----------------PRESENT-------------")
    print("Current estimated infected is", int(infected))

    percent = int(infected) / population
    print("which is {} percent of the population".format(round(percent, 5)))
    #future est
    counter = 0
    num = 0
    print("---------------------FUTURE---------------")
    while True:
        print("future estimations. Day", (counter + 1), "infected", infected, "population", population, "dead:",deathNum[num])
        counter += days_to_double
        #just so we can use the death numbers from the previous count
        if len(deathNum) <= num:
            break
        if int(infected) >= population:
            break
        infected *= 2
        num += 1
        
    print("it would take {} days for the virus to overtake the US at the current spread rate".format(counter))
print("How many have died?")
calcCase(deathRate, dead, days_to_double, infected, population)

#Taken from Scraper.py
#20 march: 282?
#23 march, 2020 AM: 483, PM 553.
#24 march,2020 667
#27 march, 2020: 1,382
#31 mar, 2020: 3,392
#Total cases: 163,539 Total deaths: 2,860 
#Total cases: 186,101 Total deaths: 3,603
#Total cases: 239,279 Total deaths: 5,443
#Total cases:277,205 Total deaths: 6,593
#Total cases: 427,460 Total deaths: 14,696
#14 APR 2020 1200: Total cases: 525,704 Total deaths: 20,486 estimated infected 26,222,080
#15 APR 2020: Total cases: 605,390 Total deaths: 24,582, estimated infected 31,464,960 
