"""
Task class that creates task objects with all variables necessary.

"""


from datetime import datetime as dt

class Task:
    # Task constructor that initializes a class object
    def __init__(self, task_id: int, date: dt, starttime: dt, endtime: dt, content: str, status: bool):            
        self.task_id = task_id
        self.date = date
        self.starttime = starttime
        self.endtime = endtime
        self.content = content
        self.status = status       
    
    
    # print function that tells about task deadlines
    def __str__(self):
        return f"Task {self.task_id} is due on {self.date.strftime("%d/%m/%Y")} at {self.endtime.strftime("%H:%M")}."
    
    # Task ID getter and setter
    @property
    def task_id(self):
        return self._task_id
   
    @task_id.setter
    def task_id(self, task_id):
        # makes sure task_id is integer
        if isinstance(task_id, str):
            self._task_id = int(task_id)
        else:
            self._task_id = task_id

    # date getter and setter
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        # makes sure date is in date format
        if isinstance(date, str):
            self._date = dt.strptime(date, "%d/%m/%Y")
        else:
            self._date = date

    # start time getter and setter
    @property
    def starttime(self):
        return self._starttime
    
    @starttime.setter
    def starttime(self, starttime):
        # makes sure it is in time format
        if isinstance(starttime, str):
            self._starttime = dt.strptime(starttime, "%H:%M")
        else:
            self._starttime = starttime

    # end time getter and setter
    @property
    def endtime(self):
        return self._endtime
    
    @endtime.setter
    def endtime(self, endtime):
        # makes sure it is in time format
        if isinstance(endtime, str):
            self._endtime = dt.strptime(endtime, "%H:%M")
        else:
            self._endtime = endtime
    
    # content getter and setter
    @property
    def content(self):
        return self._content
    
    @content.setter
    def content(self, content):
        self._content = content

    # status getter and setter
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, status):
        # makes sure status is boolean
        if isinstance(status, str):
            self._status = status == "True"
        else:
            self._status = status

    