import PySimpleGUI as gui
import datetime
import time
import task
import calendar

print("****Welcome To Python Scheduler****\n")


 # converts a list to string
def listToString(s):
    """Convert list s and return a string."""
    str1 = " "
    return (str1.join(s))


 # updates currentDate to the current date
def currentDateUpdate():
    """Update the currentDate to the Local datetime now function."""
    currentDate = datetime.datetime.now()
    return currentDate

 # initial variables
t = time.time()


currentDate = currentDateUpdate()


 # main clock loop function
def clockLoop():
    """Repeating loop for the main clock.
    This will constantly update the current time and datetime objects
    to the current local time
    
    t : current time variable

    Returns
    -------
    t : the currently updated time

    """
    t = time.time()
    currentDateUpdate()
    compareLoop()
    return t

 # creates a new task and adds it to taskList
def createTask(name, desc, startDate, endDate):
    """Create a new task.py object from args and add it to taskList.

    Args:
        name (str): name for the task
        desc (str): description for the task
        startDate (datetime.obj): start date for the task
        endDate (datetime.obj): end date for the task
    """
    task.taskList.append(task.Task(name, desc, t, startDate, endDate))

 # loops through all tasks if timeCompare == true Deletes task
def compareLoop():
    """Loop through all the tasks in taskList.
    if timeCompare() returns true then the end date has passed
    and the task from taskList will be removed
    """
    for item in task.taskList:
        if timeCompare(item):
            print('Removing ', item)
            task.taskList.remove(item)
        
 # compares task end time to current time
def timeCompare(timeInput):
    """Compare a task end time to the current time if the end date has passed it will return true.

    Args:
        timeInput (datetime.obj): date time object input for comparison

    Returns:
        boolean: returns true if currentDateUpdate() > timeInput.endDate
    """
    if currentDateUpdate() > timeInput.endDate:
        return True
    else:
        return False

 # prints all tasks
def printTasks():
    """Output all the tasks in the taskList."""
    for item in task.taskList:
        print(item.__repr__()+"\n")
        

 # main layout constructor
gui.theme('dark grey 11')
layout = [[gui.Text('', size=(15, 0), font=('Helvetica', 20), justification='center', key='-timer-')],
[gui.Text('', size=(15, 0), font=('Helvetica', 20), justification='center', key='-date-')],
[gui.Text('', size=(4, 0), justification= 'center'), gui.Button("Exit"), gui.Button('Create'),
gui.Button('Manage')]]


 # name and description buttons
def deployCreateLayout():
    """Layout for the Create Task Window.

    Returns:
        pysimpleGuiLayout: layout
    """    
    createLayout = [[gui.Text('Name:'), gui.Input(size=(20, 1), key='-name-')],
    [gui.Text('Desc: '), gui.Multiline(size=(47, 4), key='-desc-')],
     # start Date buttons
    [gui.Text('Start Date:'), gui.Spin(values=list(range(1, 32)), initial_value=str.strip(time.strftime('%d').strip('0')), size=(5, 1), key='-sday-'),
    gui.InputCombo(('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'November', 'December'), default_value=time.strftime('%B', time.localtime(t)), size=(10, 1), key='-smonth-'),
    gui.Spin(values=list(range(int(time.strftime('%Y')), int(time.strftime('%Y'))+20)), initial_value=time.strftime('%Y').strip('0'), size=(4, 1), key='-syear-'), gui.Text(':', size=(0, 0)),
    gui.Spin(values=list(range(0, 13)), initial_value=time.strftime('%I'), size=(2, 1), key='-shours-'), gui.Text(':', size=(0, 0)),
    gui.Spin(values=list(range(0, 60)), initial_value=time.strftime('%M'), size=(2, 1), key='-sminutes-'),
    gui.Spin(('AM', 'PM'), initial_value=time.strftime('%p'), size=(3, 1), key='-smer-')],
     # End Date Buttons
    [gui.Text('End Date: '),  gui.Spin(values=list(range(1, 32)), initial_value=str.strip(time.strftime('%d').strip('0')), size=(5, 1), key='-eday-'),
    gui.InputCombo(('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'November', 'December'), default_value=time.strftime('%B'), size=(10, 1), key='-emonth-'),
    gui.Spin(values=list(range(int(time.strftime('%Y')), int(time.strftime('%Y'))+20)), initial_value=time.strftime('%Y').strip('0'), size=(4, 1), key='-eyear-'), gui.Text(':', size=(0, 0)),
    gui.Spin(values=list(range(0, 13)), initial_value=time.strftime('%I'), size=(2, 1), key='-ehours-'), gui.Text(':', size=(0, 0)),
    gui.Spin(values=list(range(0, 60)), initial_value=time.strftime('%M'), size=(2, 1), key='-eminutes-'),
    gui.Spin(('AM', 'PM'), initial_value=time.strftime('%p'), size=(3, 1), key='-emer-')],
    [gui.Button("Cancel", pad=((20, 20),(20, 20)),size=(5, 2)), gui.Button('Done', size=(5, 2))]]
    return createLayout

 # Task creation createWindow
createWindow = gui.Window('Task Creation', deployCreateLayout())


 # checks if the days correspond with the correct month range
def taskConfirmation():
    """If start day is in range of calendar month for the start year check the end day.
    Returns: True
    """
    if values['-sday-'] in range(1, (calendar.monthrange(values['-syear-'], time.strptime(values['-smonth-'], '%B').tm_mon))[1]+1):
        """if end day is in the range of calendar month for the end year
        Returns: True
        """
        if values['-eday-'] in range(1, (calendar.monthrange(values['-eyear-'], time.strptime(values['-emonth-'], '%B').tm_mon))[1]+1):
             # print('your dates work correctly')
            return True
        else:
            print("your end date is wrong")
    else:
        print('your start date is wrong')
        return False
 # main mainWindow creation for Py Scheduler
mainWindow = gui.Window("Py Scheduler", layout)


 # mainWindow event loop
while True:
    """Main mainWindow event loop
    Reads mainWindow event values every 100ms
    on event Exit or Window Closes: break loop and close program
    on event Create: Open createWindow
        on event Done: create a task using inputed data values from user
        on event Cancel or Window Closes: stop task creation and close createWindow
    on event Manage: View all tasks and allow Editing
    """
    event, values = mainWindow.read(timeout=100)
    if event in ("Exit", gui.WIN_CLOSED):
        break
    if event == "Create":
        while True:
            event, values = createWindow.read()
            if event in ("Cancel", gui.WIN_CLOSED):
                createWindow.close()
                createWindow = gui.Window('Task Creation', deployCreateLayout())
                break
            if event == "Done":
                if taskConfirmation():
                    sdate = str(values['-syear-']), values['-smonth-'], str(values['-sday-']), str(values['-shours-']), str(values['-sminutes-']), str(values['-smer-'])
                    sdateobj = datetime.datetime.strptime(listToString(sdate), '%Y %B %d %I %M %p')
                    edate = str(values['-eyear-']), values['-emonth-'], str(values['-eday-']), str(values['-ehours-']), str(values['-eminutes-']), str(values['-emer-'])
                    edateobj = datetime.datetime.strptime(listToString(edate), '%Y %B %d %I %M %p')
                    createTask(values['-name-'], values['-desc-'], sdateobj, edateobj)
                    print('New Task: ', values['-name-'], 'Created', 'Start: ', sdateobj.strftime('%Y-%m-%d %H:%M%p %Z'), 'End: ', edateobj.strftime('%Y-%m-%d %H:%M%p %Z'))
                    
                    createWindow.close()
                    createWindow = gui.Window('Task Creation', deployCreateLayout())
                    break
                else:
                    print('Retry date')
                
    if event == "Manage":
        break

     # windup loop updates
    mainWindow['-timer-'].update(time.strftime('%I:%M:%S %p', time.localtime(clockLoop())))
    mainWindow['-date-'].update(time.strftime('%b %d %Y', time.localtime(clockLoop())))

mainWindow.close()