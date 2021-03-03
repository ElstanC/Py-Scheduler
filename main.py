import PySimpleGUI as gui
import datetime
import time
import task
import calendar

print("****Welcome To Python Scheduler****\n")


#converts a list to string
def listToString(s):  
    # initialize an empty string 
    str1 = " " 
    return (str1.join(s)) 


#updates currentDate to the current date
def currentDateUpdate():
    currentDate = datetime.datetime.now()
    return currentDate

#initial variables
t = time.time()
currentDate = currentDateUpdate()

#main clock loop function
def clockLoop():
    t = time.time()
    currentDateUpdate()
    compareLoop()
    return t

#creates a new task and adds it to taskList
def createTask(name, desc, startDate, endDate):
    task.taskList.append(task.Task(name, desc, t, startDate, endDate))

#loops through all tasks if timeCompare == true Deletes task
def compareLoop():
    for item in task.taskList:
        if timeCompare(item):
            print('Removing ', item)
            task.taskList.remove(item)
        
#compares task end time to current time  
def timeCompare(time2):
    if currentDateUpdate() > time2.endDate:
        return True
    else:
        return False

#prints all tasks
def printTasks():
    for item in task.taskList:
        print(item.__repr__()+"\n")
        

#main layout constructor
gui.theme('dark grey 11')
layout = [[gui.Text('', size=(15,0), font=('Helvetica', 20), justification='center', key='-timer-')],
[gui.Text('', size=(15,0), font=('Helvetica', 20), justification='center', key='-date-')],
[gui.Text('',size=(4,0), justification= 'center'), gui.Button("Exit"), gui.Button('Create'),
gui.Button('Manage')]]


#name and description buttons
def deployCreateLayout():
    createLayout = [[gui.Text('Name:'), gui.Input(size=(20,1), key='-name-')],
    [gui.Text('Desc: '), gui.Multiline(size=(47,4), key='-desc-')],
    #start Date buttons
    [gui.Text('Start Date:'), gui.Spin(values=list(range(1,32)), initial_value=str.strip(time.strftime('%d').strip('0')), size=(5, 1), key='-sday-'),
    gui.InputCombo(('January','February','March','April','May','June','July','August','September','November','December'), default_value=time.strftime('%B', time.localtime(t)), size=(10,1), key='-smonth-'),
    gui.Spin(values=list(range(int(time.strftime('%Y')), int(time.strftime('%Y'))+20)), initial_value=time.strftime('%Y').strip('0'), size=(4, 1), key='-syear-'),gui.Text(':', size=(0,0)),
    gui.Spin(values=list(range(0, 13)), initial_value=time.strftime('%I'), size=(2, 1), key='-shours-'),gui.Text(':', size=(0,0)),
    gui.Spin(values=list(range(0, 60)), initial_value=time.strftime('%M'), size=(2, 1), key='-sminutes-'),
    gui.Spin(('AM','PM'), initial_value=time.strftime('%p'), size=(3, 1), key='-smer-')],
    #End Date Buttons
    [gui.Text('End Date: '),  gui.Spin(values=list(range(1,32)), initial_value=str.strip(time.strftime('%d').strip('0')), size=(5, 1), key='-eday-'),
    gui.InputCombo(('January','February','March','April','May','June','July','August','September','November','December'), default_value=time.strftime('%B'), size=(10,1), key='-emonth-'),
    gui.Spin(values=list(range(int(time.strftime('%Y')), int(time.strftime('%Y'))+20)), initial_value=time.strftime('%Y').strip('0'), size=(4, 1), key='-eyear-'),gui.Text(':', size=(0,0)),
    gui.Spin(values=list(range(0, 13)), initial_value=time.strftime('%I'), size=(2, 1), key='-ehours-'),gui.Text(':', size=(0,0)),
    gui.Spin(values=list(range(0, 60)), initial_value=time.strftime('%M'), size=(2, 1), key='-eminutes-'),
    gui.Spin(('AM','PM'), initial_value=time.strftime('%p'), size=(3, 1), key='-emer-')],
    [gui.Button("Cancel", pad=((20,20),(20,20)),size=(5,2)), gui.Button('Done', size=(5,2))]]
    return createLayout

#Task creation window
createWindow = gui.Window('Task Creation', deployCreateLayout())

#checks if the days correspond with the correct month range 
def taskConfirmation():
    if values['-sday-'] in range(1,(calendar.monthrange(values['-syear-'], time.strptime(values['-smonth-'],'%B').tm_mon))[1]+1):
        if values['-eday-'] in range(1,(calendar.monthrange(values['-eyear-'], time.strptime(values['-emonth-'],'%B').tm_mon))[1]+1):
            #print('your dates work correctly')
            return True
        else:
            print("your end date is wrong")
    else:
        print('your start date is wrong')
        return False

window = gui.Window("Py Scheduler", layout, alpha_channel=0.7)

#window event loop
while True:
    event, values = window.read(timeout=100)
    if event == "Exit" or event == gui.WIN_CLOSED:
        break
    if event == "Create":
        while True:
            event, values = createWindow.read()
            if event == "Cancel" or event == gui.WIN_CLOSED:
                createWindow.close()
                print('close')
                createWindow = gui.Window('Task Creation', deployCreateLayout())
                break
            if event == "Done":
                if taskConfirmation():
                    sdate = str(values['-syear-']),values['-smonth-'],str(values['-sday-']),str(values['-shours-']),str(values['-sminutes-']),str(values['-smer-'])
                    sdateobj = datetime.datetime.strptime(listToString(sdate), '%Y %B %d %I %M %p')
                    edate = str(values['-eyear-']),values['-emonth-'],str(values['-eday-']),str(values['-ehours-']),str(values['-eminutes-']),str(values['-emer-'])
                    edateobj = datetime.datetime.strptime(listToString(edate), '%Y %B %d %I %M %p')
                    createTask(values['-name-'],values['-desc-'],sdateobj,edateobj)
                    print('New Task:', values['-name-'],'Created', 'Start: ', sdateobj.strftime('%Y-%m-%d %H:%M%p %Z'), 'End: ', edateobj.strftime('%Y-%m-%d %H:%M%p %Z'))
                    
                    createWindow.close()
                    createWindow = gui.Window('Task Creation', deployCreateLayout())
                    #printTasks()
                    break
                else:
                    print('Retry date')
                
    if event == "Manage":
        break

    #windup loop updates
    window['-timer-'].update(time.strftime('%I:%M:%S %p', time.localtime(clockLoop())))
    window['-date-'].update(time.strftime('%b %d %Y', time.localtime(clockLoop())))

window.close()