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
            ret+=str(player)+", "
        ret+="\t\tOff:\t"
        for player in self.off:
            ret+=str(player)+","
        return ret

def print_schedule(schedule:list):
    i=1
    for week in schedule:
        print('Week {0}:'.format(i))
        print(week)
        i+=1

def main():

    players = {Player("Nathan"), Player("Frank"), Player("Gabriel"), Player("Adam"),Player("Nolan"),Player("Steven"),Player("Heather")}
    schedule = list()

    num_weeks = 52
    l = len(schedule)
    while l < num_weeks:
        print(l)
        if(l < 1):
            on = set()
            i = 0
            for player in players:
                if(i<5):
                    on.add(player)
                    player.weeks+=1
                else:
                    break
                i+=1
            off = players.difference(on)
            week = Week(on,off)
            schedule.append(week)
        elif(l < 2):
            first = schedule[0]
            on = first.off.copy()
            the_rest = players.difference(on)
            for player in the_rest:
                if(len(on) < 5):
                    on.add(player)
                    player.weeks+=1
                else:
                    break
            schedule.append(Week(on,players.difference(on)))
            pass
        else:
            break
        l = len(schedule)
    print_schedule(schedule)
    pass

if __name__ == "__main__":
    main()