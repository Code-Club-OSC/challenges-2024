noOfDucks = int(input())
noOfDucksDaily = int(input())
dailyCasualties = int(input())
humanPopulation = int(input())

days = 0
while True:
    if (noOfDucks + noOfDucksDaily - dailyCasualties) > humanPopulation:
        print(days)
        break
    noOfDucks += noOfDucksDaily
    noOfDucks -= dailyCasualties
    days+=1