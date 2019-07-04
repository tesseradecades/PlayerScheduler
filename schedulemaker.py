from datetime import datetime, timedelta
from math import factorial

class Player:
    def __init__(self,name:str):
        self.name = name
        self.weeks = 0
    def __str__(self)->str:
        return self.name
class Week:
    def __init__(self,date,on:set,off:set):
        self.date=date
        self.on=on
        self.off=off
    def __str__(self)->str:
        ret = "Week of {0}:\t\tOn:\t".format(self.date.strftime('%b-%d-%Y'))
        for player in self.on:
            ret+='{0},'.format(player)
        ret+="\t\tOff:\t"
        for player in self.off:
            ret+='{0},'.format(player)
        return ret

def ncr(n,r):
    return factorial(n)//factorial(r)//factorial(n-r)

def print_schedule(schedule:list):
    i=1
    for week in schedule:
        print('Week {0}:'.format(i))
        print(week)
        i+=1

def get_least_played(players:set)->Player:
    ret = None
    for player in players:
        if(ret == None):
            ret = player
        elif(ret.weeks > player.weeks):
            ret = player
    return ret

def get_most_played(players:set)->Player:
    ret = None
    for player in players:
        if(ret == None):
            ret = player
        elif(ret.weeks < player.weeks):
            ret = player
    return ret

def generate_schedule(players:set,num_on:int,num_weeks:int,start_date:datetime=datetime.now())->list:
    schedule = list()
    l = len(schedule)
    while l < num_weeks:
        if(l < 1):
            """
            If no weeks have been added yet, just pick players until there are enough
            """
            on = set()
            i = 0
            for player in players:
                if(i<num_on):
                    on.add(player)
                else:
                    break
                i+=1
            date = start_date
        elif(l < 2):
            """
            If there has been only 1 week added, ensure those who didn't play 
            last week, play this week. Then just add more until there are enough 
            players
            """
            first = schedule[0]
            on = first.off.copy()
            the_rest = players.difference(on)
            for player in the_rest:
                if(len(on) < num_on):
                    on.add(player)
                else:
                    break
            pass
            date=first.date+timedelta(days=7)
        else:
            """
            If there are at least 2 weeks, make sure everyone who has been off 
            at least once in the past two weeks gets to play this week. Of the 
            remaining players pick the player who has played the least, until 
            there are enough players.
            """
            week_ago = schedule[l-1]
            last_week = week_ago.off.copy()
            week_before = schedule[l-2].off.copy()

            on = last_week.union(week_before)
            while len(on) < num_on:
                on.add(get_least_played(players.difference(on)))
            #In case 2*|off| > |on| the picked players who've played the most will nit play this week
            while len(on) > num_on:
                on.remove(get_most_played(on))

            date = week_ago.date+timedelta(days=7)
        for player in on:
            player.weeks+=1
        week=Week(date,on,players.difference(on))
        schedule.append(week)
        l = len(schedule)
    return schedule

def main():

    players = {Player("Nathan"), Player("Frank"), Player("Gabriel"), Player("Adam"),Player("Nolan"),Player("Steven"),Player('Alex'),Player("Heather")}
    num_on=5
    num_weeks = ncr(len(players),num_on)#compute the number of unique combinations
    print_schedule(generate_schedule(players,num_on=num_on,num_weeks=num_weeks))
    #print(type(datetime.now()))
    pass

if __name__ == "__main__":
    main()