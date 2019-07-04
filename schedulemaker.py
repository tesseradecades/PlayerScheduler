class Player:
    def __init__(self,name:str):
        self.name = name
        self.weeks = 0
    def __str__(self)->str:
        return self.name
class Week:
    def __init__(self,on:set,off:set):
        self.on=on
        self.off=off
    def __str__(self)->str:
        ret = "On:\t"
        for player in self.on:
            ret+='{0}({1}),'.format(player,player.weeks)
        ret+="\t\tOff:\t"
        for player in self.off:
            ret+='{0}({1}),'.format(player,player.weeks)
        return ret

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

def main():

    players = {Player("Nathan"), Player("Frank"), Player("Gabriel"), Player("Adam"),Player("Nolan"),Player("Steven"),Player("Heather")}
    schedule = list()

    num_weeks = 52
    l = len(schedule)
    while l <= num_weeks:
        print(l)
        if(l < 1):
            on = set()
            i = 0
            for player in players:
                if(i<5):
                    on.add(player)
                else:
                    break
                i+=1
        elif(l < 2):
            first = schedule[0]
            on = first.off.copy()
            the_rest = players.difference(on)
            for player in the_rest:
                if(len(on) < 5):
                    on.add(player)
                else:
                    break
            pass
        else:
            last_week = schedule[l-1].off.copy()
            week_before = schedule[l-2].off.copy()

            on = last_week.union(week_before)
            on.add(get_least_played(players.difference(on)))
        for player in on:
            player.weeks+=1
        week=Week(on,players.difference(on))
        print(week)
        schedule.append(week)
        l = len(schedule)
    #print_schedule(schedule)
    pass

if __name__ == "__main__":
    main()