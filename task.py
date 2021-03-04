import datetime
import time
taskList = []
class Task:
    """A class that represents a Task."""

    def __init__(self, name, desc, createdDate, startDate, endDate):
        """Constructor for tasks.

        Args:
            name (str): name of the task
            desc (str): description of the task
            createdDate (datetime.obj): date the task object was created
            startDate (datetime.obj): date the task will start
            endDate (datetime.obj): date the task will end
        """        
        self.name = name
        self.desc = desc
        self.createdDate = createdDate
        self.startDate = startDate
        self.endDate = endDate
    def __repr__(self):
        return f'Task name: {self.name} Description: {self.desc}Created Date: {self.created()} \nStart Date: {self.start()} End Date: {self.end()}'
    def getEnd(self):
        """Return the end date of the self obj."""
        return self.endDate
    def getStart(self):
        """Return the Start Date of the self obj."""
        return self.startDate
    def created(self):
        """Return the Created Date of the self obj as a string."""
        return time.strftime('%Y-%m-%d %H:%M %Z', time.localtime(self.createdDate))
    def start(self):
        """Return the start date of the self obj as a string."""
        return self.startDate.strftime('%Y-%m-%d %H:%M %Z')
    def end(self):
        """Return the end date of the self obj as a string."""
        return self.endDate.strftime('%Y-%m-%d %H:%M %Z')    

def timeFormat(input):
    """Format the inputed datetime.obj to a string.

    Args:
        input (datetime.obj): inputed datetime.obj

    Returns:
        str: returns the datetime.obj as a string
    """    
    out =  time.strftime('%Y-%m-%d %H:%M %Z', time.localtime(input))
    return out