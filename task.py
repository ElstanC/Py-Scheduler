import datetime
import time
taskList = []
class Task:
    def __init__(self, name, desc, createdDate, startDate, endDate):
        self.name = name
        self.desc = desc
        self.createdDate = createdDate
        self.startDate = startDate
        self.endDate = endDate
    def __repr__(self):
        return f'Task name: {self.name} Description: {self.desc}Created Date: {self.created()} \nStart Date: {self.start()} End Date: {self.end()}'
    def getEnd(self):
        return self.endDate
    def getStart(self):
        return self.startDate
    def created(self):
        return time.strftime('%Y-%m-%d %H:%M %Z', time.localtime(self.createdDate))
    def start(self):
        return self.startDate.strftime('%Y-%m-%d %H:%M %Z')
    def end(self):
        return self.endDate.strftime('%Y-%m-%d %H:%M %Z')    
    def pcreated(self):
        print(time.strftime('%Y-%m-%d %H:%M %Z', time.localtime(self.createdDate)))
    def pstart(self):
        print(time.strftime('%Y-%m-%d %H:%M %Z', time.localtime(self.startDate)))
    def pend(self):
        print(time.strftime('%Y-%m-%d %H:%M %Z', time.localtime(self.endDate)))


def timeFormat(input):
    out =  time.strftime('%Y-%m-%d %H:%M %Z', time.localtime(input))
    return out