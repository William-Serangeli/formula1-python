## 1.2 beta
# randomized attack attempt when closing the gap
# random dialogs
# reduced probability of crash and penalties instead of overtakes and other events
# estetic adjustements
# save final grid and race report added
import random
import time
from datetime import datetime
from datetime import date
sectors = [1,2,3]
otstatus = ["fails","succedes"]
piloti = ["LECLERC","RUSSEL","SAINZ","PEREZ","HAMILTON","VERSTAPPEN","OCON","NORRIS","MAGNUSEN","BOTTAS"]
numbers = [1,2,3,4,5,6,7,8,9]
starting_grid = (random.sample(piloti, 10))
allpen = []
race_report = []
def fcy():
        yellow_flag()
def yellow_flag():
        now = datetime.now()
        today = date.today()
        current_time = now.strftime("%H:%M:%S")
        today1 = str(today)
        race_report.append(today1)
        race_report.append(current_time)
        race_report.append("safety car is out")
        race_report.append('    -    ')
        print ("          yellow flag sector ",random.choice(sectors))
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
        print(" ")
        time.sleep(5)
        green_flag()
        
def green_flag():
        now = datetime.now()
        today = date.today()
        current_time = now.strftime("%H:%M:%S")
        today1 = str(today)
        race_report.append(today1)
        race_report.append(current_time)
        race_report.append("green_flag")
        race_report.append('    -    ')
        print("###      GREEN FLAG       ###")
        print("###     resume racing     ###")
def eventrandomizer():
        events = [crash,overtake,closing,penalty,overtake,closing,overtake,closing]
        random.choice(events)()
def crash():
        x = (random.choice(numbers))
        message1 = " crashes and he is out of the race"
        message2 = " goes wide in the gravel, and, he is stuck in there"
        message3 = " touches the wall! what a big crash and he is now out of the race"
        message4 = " what a huge accident! he is now out of the race"
        messages = [message1,message2,message3,message4]
        displaymsg = random.choice(messages)
        print(starting_grid[x],displaymsg)
        del starting_grid[x]
        del numbers[-1]
        print("now we just have ",len(starting_grid)," cars on the grids ")
        now = datetime.now()
        today = date.today()
        current_time = now.strftime("%H:%M:%S")
        today1 = str(today)
        race_report.append(today1)
        race_report.append(current_time)
        race_report.append(starting_grid[x])
        race_report.append("crashes")
        race_report.append('    -    ')
        fcy()
def overtake():
        succes = " and succedes taking up the position"
        fail = " but fails"
        succes1 = "and he takes the position!"
        fail1 = "but he stays back"
        otstatus = [succes,fail,succes1,fail1]
        state = random.choice(otstatus)
        x = random.choice(numbers)
        y = x-1
        z = x+1
        cars = [starting_grid[x],starting_grid[y]]
        message1 = " tries to overtake "
        message2 = " launches down the inside of"
        message3 = " he is now "
        message4 = "th "
        message5 = "and he stays "
        messages = [message1,message2]
        displaymsg = random.choice(messages)
        if state == succes:
                temp = starting_grid[x]
                temp1 = starting_grid[y]
                starting_grid[x] = starting_grid[y]
                starting_grid[y] = temp
                newpos = x
                if newpos == 3:
                        message4 = "rd"
                elif newpos == 2:
                        message4 = "nd"
                elif newpos == 1:
                        message4 = "st"
                print (cars[0],displaymsg, cars[1], state,message3,newpos,message4 )
                now = datetime.now()
                today = date.today()
                current_time = now.strftime("%H:%M:%S")
                today1 = str(today)
                race_report.append(today1)
                race_report.append(current_time)
                race_report.append(starting_grid[x])
                race_report.append("overtakes")
                race_report.append(starting_grid[y])
                race_report.append('    -    ')
        elif state == succes1:
                temp = starting_grid[x]
                temp1 = starting_grid[y]
                starting_grid[x] = starting_grid[y]
                starting_grid[y] = temp
                newpos = x
                if newpos == 3:
                        message4 = "rd"
                elif newpos == 2:
                        message4 = "nd"
                elif newpos == 1:
                        message4 = "st"
                print (cars[0],displaymsg, cars[1], state,message3,newpos,message4 )
                now = datetime.now()
                today = date.today()
                current_time = now.strftime("%H:%M:%S")
                today1 = str(today)
                race_report.append(today1)
                race_report.append(current_time)
                race_report.append(starting_grid[x])
                race_report.append("overtakes")
                race_report.append(starting_grid[y])
                race_report.append('    -    ')
        elif state == fail1:
                oldpos = x+1
                if oldpos == 3:
                        message4 = "rd"
                elif oldpos == 2:
                        message4 = "nd"
                elif oldpos == 1:
                        message4 = "st"
                print (cars[0],displaymsg, cars[1], state,message5,oldpos,message4 )
        else: 
                oldpos = x+1
                if oldpos == 3:
                        message4 = "rd"
                elif oldpos == 2:
                        message4 = "nd"
                elif oldpos == 1:
                        message4 = "st"
                print (cars[0],displaymsg, cars[1], state,message5,oldpos,message4 )
def closing_ot():
        yes = "tries to overtake"
        no = "but not enough"
        options = [yes,no]
        tries= random.choice(options)
        if tries == yes:
                print(yes)
        else:
                print(no)
def closing():
        msg1 = "is closing up on"
        msg2 = "is closing the gap with the car of "
        msg3 = "is closing the gap between him and "
        msg4 = "is getting closer to"
        msgs = [msg1,msg2,msg3,msg4]
        displaymsg = random.choice(msgs)
        yes = "tries to overtake"
        no = "but not enough to try to overtake"
        options = [yes,no]
        tries= random.choice(options)
        succes = "succedes"
        fail = "fails"
        succes1 = "and he takes the position!"
        fail1 = "but he stays back"
        otstatus = [succes,fail,succes1,fail1]
        state = random.choice(otstatus)
        x = random.choice(numbers)
        y = x-1
        z = x+1
        print (starting_grid[x],displaymsg, starting_grid[y],)
        if tries == yes:
                cars = [starting_grid[x],starting_grid[y]]
                print (cars[0],"tries to overtake ", cars[1]," and ", state )
                if state == succes:
                        temp = starting_grid[x]
                        temp1 = starting_grid[y]
                        starting_grid[x] = starting_grid[y]
                        starting_grid[y] = temp
        else:
                print(no)       
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
        append2=(starting_grid[x],"5 seconds - illegal overtake")
        now = datetime.now()
        today = date.today()
        current_time = now.strftime("%H:%M:%S")
        today1 = str(today)
        race_report.append(today1)
        race_report.append(current_time)
        race_report.append(append2)
def waving():
        seconds = [2,3,5,10]
        x = random.choice(numbers)
        y = x-1
        z = x+1
        print ("here comes a 5 seconds penalty to ",starting_grid[x]," for waving on a straight line")
        append2=(starting_grid[x],"5 seconds - waving")
        allpen.append(starting_grid[x])
        allpen.append("( 5 seconds - waving )")
        now = datetime.now()
        today = date.today()
        current_time = now.strftime("%H:%M:%S")
        today1 = str(today)
        race_report.append(today1)
        race_report.append(current_time)
        race_report.append(append2)
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
        now = datetime.now()
        today = date.today()
        current_time = now.strftime("%H:%M:%S")
        today1 = str(today)
        race_report.append(today1)
        race_report.append(current_time)
        race_report.append(append2)
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
        now = datetime.now()
        today = date.today()
        current_time = now.strftime("%H:%M:%S")
        today1 = str(today)
        race_report.append(today1)
        race_report.append(current_time)
        race_report.append(append2)
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
    not_so_well = ("")
    wellstart = [well,not_so_well]
    state = random.choice(wellstart)
    if state == not_so_well:
            temp = starting_grid[0]
            temp1 = starting_grid[1]
            starting_grid[0] = starting_grid[1]
            starting_grid[1] = temp
            print("AND IT IS LIGHTS OUT AND AWAY WE GO", starting_grid[1], "doesn't get away well from pole so ", starting_grid[0], " easily overtakes him and puts himself in first place ")
    else:
            print("AND IT IS LIGHT'S OUT AND AWAY WE GO ", starting_grid[0], state)
def race():
    start()
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
def endrace():
        final_grid=(starting_grid)
        time.sleep(1)
        print(" ")
        print("###########################################")
        print(" ")
        print(" race ended here is the final grid   - ", starting_grid)
        print(" ")
        print("###########################################")
        save = input('do you want to save the final grid on text file?\n type YES in capital letters to save it; type NO in capital latters to ignore\n')
        if save == "YES":
                saverace()
def saverace():
        
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        today = date.today()
        today1 = str(today)
        final_grid=(starting_grid)
        final_grid_str = str (final_grid)
        with open("races final grid.txt", "a+") as file_object:
            # Move read cursor to the start of file.
            file_object.seek(0)
            # If file is not empty then append '\n'
            data = file_object.read(100)
            if len(data) > 0 :
                file_object.write("\n")
            # Append text at the end of file
            file_text=(today1,current_time,"           ",final_grid_str)
            file_text_str = str(file_text)
            file_object.write(file_text_str)
        file_object.close()
        print(" ")
        print("###########################################")
        print("race saved")
        saverace_report()
def saverace_report():
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        today = date.today()
        today1 = str(today)
        text_msg = (today1,current_time,"       ",race_report,)
        text_msg_str = str(text_msg)
        with open("race report.txt", "a+") as file_object:
            # Move read cursor to the start of file.
            file_object.seek(0)
            # If file is not empty then append '\n'
            data = file_object.read(100)
            if len(data) > 0 :
                file_object.write("\n")
            # Append text at the end of file
            file_object.write(text_msg_str)
        file_object.close()
        print(" ")
        print("###########################################")
        print("race report saved") 
