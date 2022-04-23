import random
import time
otstatus = ["fails","succedes"]
piloti = ["LECLERC","RUSSEL","SAINZ","PEREZ","HAMILTON","VERSTAPPEN","OCON","NORRIS","MAGNUSEN","BOTTAS"]
numbers = [1,2,3,4,5,6,7,8,9]
starting_grid = (random.sample(piloti, 10))
starting_grid[1]
allpen = []
def fcy():
        yellow_flag()
def yellow_flag():
        print("###     fcy fcy - safety car is out     ###")
        time.sleep(0.5)
        print("###                                     ")
        time.sleep(10)
        print("###     safety car     ")
        time.sleep(0.5)
        print("###                    ")
        time.sleep(10)
        print("###     safety car     ")
        time.sleep(0.5)
        print("###                    ")
        time.sleep(10)
        print("###     safety car in this lap all debris are clear     ")
        time.sleep(0.5)
        print("###                                                     ")
        time.sleep(5)
        green_flag()
def green_flag():
        print("###     resume racing     ###")
def eventrandomizer():
        events = [crash,overtake,closing,causing_an_accident]
        random.choice(events)()
def crash():
        x = (random.choice(numbers))
        print(starting_grid[x]," crashes and he is out of the race")
        del starting_grid[x]
        del numbers[-1]
        print("now we just have ",len(starting_grid)," cars on the grids ")
def overtake():
        succes = "succedes"
        fail = "fails"
        otstatus = [succes,fail]
        state = random.choice(otstatus)
        x = random.choice(numbers)
        y = x-1
        z = x+1
        cars = [starting_grid[x],starting_grid[y]]
        print (cars[0]," tries to overtake ", cars[1]," and ", state )
        if state == succes:
                temp = starting_grid[x]
                temp1 = starting_grid[y]
                starting_grid[x] = starting_grid[y]
                starting_grid[y] = temp
def closing():
        x = random.choice(numbers)
        y = x-1
        z = x+1
        print (starting_grid[x]," is closing up on ", starting_grid[y],)
def illegal_overtake():
        seconds = [2,3,5,10]
        x = random.choice(numbers)
        y = x-1
        z = x+1
        time = seconds[2]
        print ("and here is a",time," seconds penalty for an illegal overtake by ",starting_grid[x]," on ",starting_grid[y])
        allpen_message =(starting_grid[x]," 5 seconds illegal overtake    -    ")
        allpen.append(starting_grid[x])
        allpen.append("( 5 seconds - illegal overtake )")
def waving():
        seconds = [2,3,5,10]
        x = random.choice(numbers)
        y = x-1
        z = x+1
        print ("here comes a 5 seconds penalty to ",starting_grid[x]," for waving on a straight line")
        allpen.append(starting_grid[x])
        allpen.append("( 5 seconds - waving )")
def track_limits():
        seconds = [2,3,5,10]
        time = random.choice(seconds)
        x = random.choice(numbers)
        y = x-1
        z = x+1
        print (starting_grid[x], " has now a  ", time," seconds penalty for trepassing track limits ")
        append2 =(time," seconds - trepassing track limits ")
        allpen.append(starting_grid[x])
        allpen.append(append2)
def causing_an_accident():
        seconds = [5,10,20]
        time = random.choice(seconds)
        x = random.choice(numbers)
        y = x-1
        z = x+1
        print (starting_grid[x], " has now a  ", time," seconds penalty for causing an accident with", starting_grid[y])
        append2 =(time," seconds - causing an accident ")
        allpen.append(starting_grid[x])
        allpen.append(append2)
def penalty():
        penalties = [illegal_overtake,waving,track_limits,causing_an_accident]
        random.choice(penalties)()                
def start():
    print("here is the starting grid:        ",starting_grid)
    time.sleep(1)
    print("10")
    time.sleep(1)
    print("9")
    time.sleep(1)
    print("8")
    time.sleep(1)
    print("7")
    time.sleep(1)
    print("6")
    time.sleep(1)
    print("5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    print(" ")
    well = ("get's away well from pole")
    not_so_well = ("doesn't get away well from pole so ",starting_grid[1]," easily overtakes him and puts himself in first place ")
    wellstart = [well,not_so_well]
    state = random.choice(wellstart)
    if state == not_so_well:
            temp = starting_grid[0]
            temp1 = starting_grid[1]
            starting_grid[0] = starting_grid[1]
            starting_grid[1] = temp
            print("AND IT IS LIGHTS OUT AND AWAY WE GO", starting_grid[1], state)
    else:
            print("AND IT IS LIGHT'S OUT AND AWAY WE GO ", starting_grid[0], state)
    overtake()
    time.sleep(5)
    overtake()
    closing()
    time.sleep(5)
    eventrandomizer()
    time.sleep(5)
    eventrandomizer()
    time.sleep(5)
    eventrandomizer()
    time.sleep(5)
    eventrandomizer()
    time.sleep(5)
    eventrandomizer()
    time.sleep(5)
    eventrandomizer()
    time.sleep(5)
    eventrandomizer()
    time.sleep(5)
    eventrandomizer()
    time.sleep(5)
    eventrandomizer()
    time.sleep(5)
    endrace()
def race():
    start()
def endrace():
        time.sleep(1)
        print(" ")
        print("###########################################")
        print(" ")
        print("race ended here is the final grid   - ", starting_grid)
