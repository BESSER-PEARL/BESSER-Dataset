from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class tdt4250case_ScheduledActivity:

    def __init__(self, room: str, timeslot: str, activity: str, tdt4250case_ScheduledActivity32: set["tdt4250case_Studyprogram"] = None, tdt4250case_ScheduledActivity: "tdt4250case_Timetable" = None):
        self.room = room
        self.timeslot = timeslot
        self.activity = activity
        self.tdt4250case_ScheduledActivity32 = tdt4250case_ScheduledActivity32 if tdt4250case_ScheduledActivity32 is not None else set()
        self.tdt4250case_ScheduledActivity = tdt4250case_ScheduledActivity
        
    @property
    def timeslot(self) -> str:
        return self.__timeslot

    @timeslot.setter
    def timeslot(self, timeslot: str):
        self.__timeslot = timeslot

    @property
    def room(self) -> str:
        return self.__room

    @room.setter
    def room(self, room: str):
        self.__room = room

    @property
    def activity(self) -> str:
        return self.__activity

    @activity.setter
    def activity(self, activity: str):
        self.__activity = activity

    @property
    def tdt4250case_ScheduledActivity(self):
        return self.__tdt4250case_ScheduledActivity

    @tdt4250case_ScheduledActivity.setter
    def tdt4250case_ScheduledActivity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_ScheduledActivity__tdt4250case_ScheduledActivity", None)
        self.__tdt4250case_ScheduledActivity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250case_Timetable30"):
                opp_val = getattr(old_value, "tdt4250case_Timetable30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250case_Timetable30"):
                opp_val = getattr(value, "tdt4250case_Timetable30", None)
                if opp_val is None:
                    setattr(value, "tdt4250case_Timetable30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tdt4250case_ScheduledActivity32(self):
        return self.__tdt4250case_ScheduledActivity32

    @tdt4250case_ScheduledActivity32.setter
    def tdt4250case_ScheduledActivity32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_ScheduledActivity__tdt4250case_ScheduledActivity32", None)
        self.__tdt4250case_ScheduledActivity32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tdt4250case_Studyprogram"):
                    opp_val = getattr(item, "tdt4250case_Studyprogram", None)
                    
                    if opp_val == self:
                        setattr(item, "tdt4250case_Studyprogram", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tdt4250case_Studyprogram"):
                    opp_val = getattr(item, "tdt4250case_Studyprogram", None)
                    
                    setattr(item, "tdt4250case_Studyprogram", self)
                    

class tdt4250case_ExaminationActivity:

    def __init__(self, evaluationForm: str, weighting: str, tdt4250case_ExaminationActivity: "tdt4250case_Examination" = None):
        self.evaluationForm = evaluationForm
        self.weighting = weighting
        self.tdt4250case_ExaminationActivity = tdt4250case_ExaminationActivity
        
    @property
    def weighting(self) -> str:
        return self.__weighting

    @weighting.setter
    def weighting(self, weighting: str):
        self.__weighting = weighting

    @property
    def evaluationForm(self) -> str:
        return self.__evaluationForm

    @evaluationForm.setter
    def evaluationForm(self, evaluationForm: str):
        self.__evaluationForm = evaluationForm

    @property
    def tdt4250case_ExaminationActivity(self):
        return self.__tdt4250case_ExaminationActivity

    @tdt4250case_ExaminationActivity.setter
    def tdt4250case_ExaminationActivity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_ExaminationActivity__tdt4250case_ExaminationActivity", None)
        self.__tdt4250case_ExaminationActivity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250case_Examination28"):
                opp_val = getattr(old_value, "tdt4250case_Examination28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250case_Examination28"):
                opp_val = getattr(value, "tdt4250case_Examination28", None)
                if opp_val is None:
                    setattr(value, "tdt4250case_Examination28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tdt4250case_CourseRole:

    def __init__(self, name: str, tdt4250case_CourseRole: "tdt4250case_CourseInstance" = None, CourseRole: "tdt4250case_Person" = None, role: set["tdt4250case_Person"] = None):
        self.name = name
        self.tdt4250case_CourseRole = tdt4250case_CourseRole
        self.CourseRole = CourseRole
        self.role = role if role is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tdt4250case_CourseRole(self):
        return self.__tdt4250case_CourseRole

    @tdt4250case_CourseRole.setter
    def tdt4250case_CourseRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_CourseRole__tdt4250case_CourseRole", None)
        self.__tdt4250case_CourseRole = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250case_CourseInstance22"):
                opp_val = getattr(old_value, "tdt4250case_CourseInstance22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250case_CourseInstance22"):
                opp_val = getattr(value, "tdt4250case_CourseInstance22", None)
                if opp_val is None:
                    setattr(value, "tdt4250case_CourseInstance22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_CourseRole__role", None)
        self.__role = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    if opp_val == self:
                        setattr(item, "Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    setattr(item, "Person", self)
                    

    @property
    def CourseRole(self):
        return self.__CourseRole

    @CourseRole.setter
    def CourseRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_CourseRole__CourseRole", None)
        self.__CourseRole = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "person"):
                opp_val = getattr(old_value, "person", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "person"):
                opp_val = getattr(value, "person", None)
                if opp_val is None:
                    setattr(value, "person", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tdt4250case_Department:

    def __init__(self, code: str, name: str, tdt4250case_Department: "tdt4250case_CourseInstance" = None, tdt4250case_Department34: set["tdt4250case_Person"] = None):
        self.code = code
        self.name = name
        self.tdt4250case_Department = tdt4250case_Department
        self.tdt4250case_Department34 = tdt4250case_Department34 if tdt4250case_Department34 is not None else set()
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tdt4250case_Department(self):
        return self.__tdt4250case_Department

    @tdt4250case_Department.setter
    def tdt4250case_Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_Department__tdt4250case_Department", None)
        self.__tdt4250case_Department = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250case_CourseInstance20"):
                opp_val = getattr(old_value, "tdt4250case_CourseInstance20", None)
                if opp_val == self:
                    setattr(old_value, "tdt4250case_CourseInstance20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250case_CourseInstance20"):
                opp_val = getattr(value, "tdt4250case_CourseInstance20", None)
                setattr(value, "tdt4250case_CourseInstance20", self)

    @property
    def tdt4250case_Department34(self):
        return self.__tdt4250case_Department34

    @tdt4250case_Department34.setter
    def tdt4250case_Department34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_Department__tdt4250case_Department34", None)
        self.__tdt4250case_Department34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tdt4250case_Person35"):
                    opp_val = getattr(item, "tdt4250case_Person35", None)
                    
                    if opp_val == self:
                        setattr(item, "tdt4250case_Person35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tdt4250case_Person35"):
                    opp_val = getattr(item, "tdt4250case_Person35", None)
                    
                    setattr(item, "tdt4250case_Person35", self)
                    

class tdt4250case_Timetable:

    pass
class tdt4250case_Examination:

    pass
class tdt4250case_Person:

    def __init__(self, name: str, username: str, tdt4250case_Person: "tdt4250case_CourseInstance" = None, person: set["tdt4250case_CourseRole"] = None, tdt4250case_Person35: "tdt4250case_Department" = None, Person: "tdt4250case_CourseRole" = None):
        self.name = name
        self.username = username
        self.tdt4250case_Person = tdt4250case_Person
        self.person = person if person is not None else set()
        self.tdt4250case_Person35 = tdt4250case_Person35
        self.Person = Person
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_Person__Person", None)
        self.__Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "role"):
                opp_val = getattr(old_value, "role", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "role"):
                opp_val = getattr(value, "role", None)
                if opp_val is None:
                    setattr(value, "role", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tdt4250case_Person35(self):
        return self.__tdt4250case_Person35

    @tdt4250case_Person35.setter
    def tdt4250case_Person35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_Person__tdt4250case_Person35", None)
        self.__tdt4250case_Person35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250case_Department34"):
                opp_val = getattr(old_value, "tdt4250case_Department34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250case_Department34"):
                opp_val = getattr(value, "tdt4250case_Department34", None)
                if opp_val is None:
                    setattr(value, "tdt4250case_Department34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def person(self):
        return self.__person

    @person.setter
    def person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_Person__person", None)
        self.__person = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CourseRole"):
                    opp_val = getattr(item, "CourseRole", None)
                    
                    if opp_val == self:
                        setattr(item, "CourseRole", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CourseRole"):
                    opp_val = getattr(item, "CourseRole", None)
                    
                    setattr(item, "CourseRole", self)
                    

    @property
    def tdt4250case_Person(self):
        return self.__tdt4250case_Person

    @tdt4250case_Person.setter
    def tdt4250case_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_Person__tdt4250case_Person", None)
        self.__tdt4250case_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250case_CourseInstance24"):
                opp_val = getattr(old_value, "tdt4250case_CourseInstance24", None)
                if opp_val == self:
                    setattr(old_value, "tdt4250case_CourseInstance24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250case_CourseInstance24"):
                opp_val = getattr(value, "tdt4250case_CourseInstance24", None)
                setattr(value, "tdt4250case_CourseInstance24", self)

class tdt4250case_CourseWork:

    def __init__(self, type: str, hours: int, tdt4250case_CourseWork: "tdt4250case_Course" = None):
        self.type = type
        self.hours = hours
        self.tdt4250case_CourseWork = tdt4250case_CourseWork
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def hours(self) -> int:
        return self.__hours

    @hours.setter
    def hours(self, hours: int):
        self.__hours = hours

    @property
    def tdt4250case_CourseWork(self):
        return self.__tdt4250case_CourseWork

    @tdt4250case_CourseWork.setter
    def tdt4250case_CourseWork(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_CourseWork__tdt4250case_CourseWork", None)
        self.__tdt4250case_CourseWork = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250case_Course11"):
                opp_val = getattr(old_value, "tdt4250case_Course11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250case_Course11"):
                opp_val = getattr(value, "tdt4250case_Course11", None)
                if opp_val is None:
                    setattr(value, "tdt4250case_Course11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tdt4250case_CourseInstance:

    def __init__(self, semester: str, CourseInstance: "tdt4250case_Course" = None, tdt4250case_CourseInstance: "tdt4250case_Examination" = None, tdt4250case_CourseInstance18: "tdt4250case_Timetable" = None, tdt4250case_CourseInstance20: "tdt4250case_Department" = None, tdt4250case_CourseInstance22: set["tdt4250case_CourseRole"] = None, tdt4250case_CourseInstance24: "tdt4250case_Person" = None, instance: "tdt4250case_Course" = None):
        self.semester = semester
        self.CourseInstance = CourseInstance
        self.tdt4250case_CourseInstance = tdt4250case_CourseInstance
        self.tdt4250case_CourseInstance18 = tdt4250case_CourseInstance18
        self.tdt4250case_CourseInstance20 = tdt4250case_CourseInstance20
        self.tdt4250case_CourseInstance22 = tdt4250case_CourseInstance22 if tdt4250case_CourseInstance22 is not None else set()
        self.tdt4250case_CourseInstance24 = tdt4250case_CourseInstance24
        self.instance = instance
        
    @property
    def semester(self) -> str:
        return self.__semester

    @semester.setter
    def semester(self, semester: str):
        self.__semester = semester

    @property
    def instance(self):
        return self.__instance

    @instance.setter
    def instance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_CourseInstance__instance", None)
        self.__instance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Course26"):
                opp_val = getattr(old_value, "Course26", None)
                if opp_val == self:
                    setattr(old_value, "Course26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Course26"):
                opp_val = getattr(value, "Course26", None)
                setattr(value, "Course26", self)

    @property
    def tdt4250case_CourseInstance20(self):
        return self.__tdt4250case_CourseInstance20

    @tdt4250case_CourseInstance20.setter
    def tdt4250case_CourseInstance20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_CourseInstance__tdt4250case_CourseInstance20", None)
        self.__tdt4250case_CourseInstance20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250case_Department"):
                opp_val = getattr(old_value, "tdt4250case_Department", None)
                if opp_val == self:
                    setattr(old_value, "tdt4250case_Department", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250case_Department"):
                opp_val = getattr(value, "tdt4250case_Department", None)
                setattr(value, "tdt4250case_Department", self)

    @property
    def CourseInstance(self):
        return self.__CourseInstance

    @CourseInstance.setter
    def CourseInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_CourseInstance__CourseInstance", None)
        self.__CourseInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course9"):
                opp_val = getattr(old_value, "course9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course9"):
                opp_val = getattr(value, "course9", None)
                if opp_val is None:
                    setattr(value, "course9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tdt4250case_CourseInstance22(self):
        return self.__tdt4250case_CourseInstance22

    @tdt4250case_CourseInstance22.setter
    def tdt4250case_CourseInstance22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_CourseInstance__tdt4250case_CourseInstance22", None)
        self.__tdt4250case_CourseInstance22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tdt4250case_CourseRole"):
                    opp_val = getattr(item, "tdt4250case_CourseRole", None)
                    
                    if opp_val == self:
                        setattr(item, "tdt4250case_CourseRole", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tdt4250case_CourseRole"):
                    opp_val = getattr(item, "tdt4250case_CourseRole", None)
                    
                    setattr(item, "tdt4250case_CourseRole", self)
                    

    @property
    def tdt4250case_CourseInstance(self):
        return self.__tdt4250case_CourseInstance

    @tdt4250case_CourseInstance.setter
    def tdt4250case_CourseInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_CourseInstance__tdt4250case_CourseInstance", None)
        self.__tdt4250case_CourseInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250case_Examination"):
                opp_val = getattr(old_value, "tdt4250case_Examination", None)
                if opp_val == self:
                    setattr(old_value, "tdt4250case_Examination", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250case_Examination"):
                opp_val = getattr(value, "tdt4250case_Examination", None)
                setattr(value, "tdt4250case_Examination", self)

    @property
    def tdt4250case_CourseInstance24(self):
        return self.__tdt4250case_CourseInstance24

    @tdt4250case_CourseInstance24.setter
    def tdt4250case_CourseInstance24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_CourseInstance__tdt4250case_CourseInstance24", None)
        self.__tdt4250case_CourseInstance24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250case_Person"):
                opp_val = getattr(old_value, "tdt4250case_Person", None)
                if opp_val == self:
                    setattr(old_value, "tdt4250case_Person", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250case_Person"):
                opp_val = getattr(value, "tdt4250case_Person", None)
                setattr(value, "tdt4250case_Person", self)

    @property
    def tdt4250case_CourseInstance18(self):
        return self.__tdt4250case_CourseInstance18

    @tdt4250case_CourseInstance18.setter
    def tdt4250case_CourseInstance18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_CourseInstance__tdt4250case_CourseInstance18", None)
        self.__tdt4250case_CourseInstance18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250case_Timetable"):
                opp_val = getattr(old_value, "tdt4250case_Timetable", None)
                if opp_val == self:
                    setattr(old_value, "tdt4250case_Timetable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250case_Timetable"):
                opp_val = getattr(value, "tdt4250case_Timetable", None)
                setattr(value, "tdt4250case_Timetable", self)

class tdt4250case_CreditReductionCourse:

    def __init__(self, reduction: float, from: date, to: date, tdt4250case_CreditReductionCourse: "tdt4250case_Course" = None, tdt4250case_CreditReductionCourse13: "tdt4250case_Course" = None):
        self.reduction = reduction
        self.from = from
        self.to = to
        self.tdt4250case_CreditReductionCourse = tdt4250case_CreditReductionCourse
        self.tdt4250case_CreditReductionCourse13 = tdt4250case_CreditReductionCourse13
        
    @property
    def reduction(self) -> float:
        return self.__reduction

    @reduction.setter
    def reduction(self, reduction: float):
        self.__reduction = reduction

    @property
    def from(self) -> date:
        return self.__from

    @from.setter
    def from(self, from: date):
        self.__from = from

    @property
    def to(self) -> date:
        return self.__to

    @to.setter
    def to(self, to: date):
        self.__to = to

    @property
    def tdt4250case_CreditReductionCourse13(self):
        return self.__tdt4250case_CreditReductionCourse13

    @tdt4250case_CreditReductionCourse13.setter
    def tdt4250case_CreditReductionCourse13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_CreditReductionCourse__tdt4250case_CreditReductionCourse13", None)
        self.__tdt4250case_CreditReductionCourse13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250case_Course14"):
                opp_val = getattr(old_value, "tdt4250case_Course14", None)
                if opp_val == self:
                    setattr(old_value, "tdt4250case_Course14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250case_Course14"):
                opp_val = getattr(value, "tdt4250case_Course14", None)
                setattr(value, "tdt4250case_Course14", self)

    @property
    def tdt4250case_CreditReductionCourse(self):
        return self.__tdt4250case_CreditReductionCourse

    @tdt4250case_CreditReductionCourse.setter
    def tdt4250case_CreditReductionCourse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_CreditReductionCourse__tdt4250case_CreditReductionCourse", None)
        self.__tdt4250case_CreditReductionCourse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250case_Course7"):
                opp_val = getattr(old_value, "tdt4250case_Course7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250case_Course7"):
                opp_val = getattr(value, "tdt4250case_Course7", None)
                if opp_val is None:
                    setattr(value, "tdt4250case_Course7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tdt4250case_Course:

    def __init__(self, code: str, name: str, content: str, credits: float, course: set["tdt4250case_Studyprogram"] = None, tdt4250case_Course5: "tdt4250case_Course" = None, tdt4250case_Course3: set["tdt4250case_Course"] = None, tdt4250case_Course: "tdt4250case_Course" = None, tdt4250case_Course1: set["tdt4250case_Course"] = None, tdt4250case_Course7: set["tdt4250case_CreditReductionCourse"] = None, course9: set["tdt4250case_CourseInstance"] = None, tdt4250case_Course11: set["tdt4250case_CourseWork"] = None, tdt4250case_Course14: "tdt4250case_CreditReductionCourse" = None, Course: "tdt4250case_Studyprogram" = None, Course26: "tdt4250case_CourseInstance" = None):
        self.code = code
        self.name = name
        self.content = content
        self.credits = credits
        self.course = course if course is not None else set()
        self.tdt4250case_Course5 = tdt4250case_Course5
        self.tdt4250case_Course3 = tdt4250case_Course3 if tdt4250case_Course3 is not None else set()
        self.tdt4250case_Course = tdt4250case_Course
        self.tdt4250case_Course1 = tdt4250case_Course1 if tdt4250case_Course1 is not None else set()
        self.tdt4250case_Course7 = tdt4250case_Course7 if tdt4250case_Course7 is not None else set()
        self.course9 = course9 if course9 is not None else set()
        self.tdt4250case_Course11 = tdt4250case_Course11 if tdt4250case_Course11 is not None else set()
        self.tdt4250case_Course14 = tdt4250case_Course14
        self.Course = Course
        self.Course26 = Course26
        
    @property
    def credits(self) -> float:
        return self.__credits

    @credits.setter
    def credits(self, credits: float):
        self.__credits = credits

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tdt4250case_Course11(self):
        return self.__tdt4250case_Course11

    @tdt4250case_Course11.setter
    def tdt4250case_Course11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_Course__tdt4250case_Course11", None)
        self.__tdt4250case_Course11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tdt4250case_CourseWork"):
                    opp_val = getattr(item, "tdt4250case_CourseWork", None)
                    
                    if opp_val == self:
                        setattr(item, "tdt4250case_CourseWork", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tdt4250case_CourseWork"):
                    opp_val = getattr(item, "tdt4250case_CourseWork", None)
                    
                    setattr(item, "tdt4250case_CourseWork", self)
                    

    @property
    def tdt4250case_Course1(self):
        return self.__tdt4250case_Course1

    @tdt4250case_Course1.setter
    def tdt4250case_Course1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_Course__tdt4250case_Course1", None)
        self.__tdt4250case_Course1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tdt4250case_Course"):
                    opp_val = getattr(item, "tdt4250case_Course", None)
                    
                    if opp_val == self:
                        setattr(item, "tdt4250case_Course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tdt4250case_Course"):
                    opp_val = getattr(item, "tdt4250case_Course", None)
                    
                    setattr(item, "tdt4250case_Course", self)
                    

    @property
    def tdt4250case_Course(self):
        return self.__tdt4250case_Course

    @tdt4250case_Course.setter
    def tdt4250case_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_Course__tdt4250case_Course", None)
        self.__tdt4250case_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250case_Course1"):
                opp_val = getattr(old_value, "tdt4250case_Course1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250case_Course1"):
                opp_val = getattr(value, "tdt4250case_Course1", None)
                if opp_val is None:
                    setattr(value, "tdt4250case_Course1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Course(self):
        return self.__Course

    @Course.setter
    def Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_Course__Course", None)
        self.__Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprogram"):
                opp_val = getattr(old_value, "studyprogram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprogram"):
                opp_val = getattr(value, "studyprogram", None)
                if opp_val is None:
                    setattr(value, "studyprogram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tdt4250case_Course7(self):
        return self.__tdt4250case_Course7

    @tdt4250case_Course7.setter
    def tdt4250case_Course7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_Course__tdt4250case_Course7", None)
        self.__tdt4250case_Course7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tdt4250case_CreditReductionCourse"):
                    opp_val = getattr(item, "tdt4250case_CreditReductionCourse", None)
                    
                    if opp_val == self:
                        setattr(item, "tdt4250case_CreditReductionCourse", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tdt4250case_CreditReductionCourse"):
                    opp_val = getattr(item, "tdt4250case_CreditReductionCourse", None)
                    
                    setattr(item, "tdt4250case_CreditReductionCourse", self)
                    

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_Course__course", None)
        self.__course = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Studyprogram"):
                    opp_val = getattr(item, "Studyprogram", None)
                    
                    if opp_val == self:
                        setattr(item, "Studyprogram", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Studyprogram"):
                    opp_val = getattr(item, "Studyprogram", None)
                    
                    setattr(item, "Studyprogram", self)
                    

    @property
    def tdt4250case_Course5(self):
        return self.__tdt4250case_Course5

    @tdt4250case_Course5.setter
    def tdt4250case_Course5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_Course__tdt4250case_Course5", None)
        self.__tdt4250case_Course5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250case_Course3"):
                opp_val = getattr(old_value, "tdt4250case_Course3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250case_Course3"):
                opp_val = getattr(value, "tdt4250case_Course3", None)
                if opp_val is None:
                    setattr(value, "tdt4250case_Course3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def course9(self):
        return self.__course9

    @course9.setter
    def course9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_Course__course9", None)
        self.__course9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CourseInstance"):
                    opp_val = getattr(item, "CourseInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "CourseInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CourseInstance"):
                    opp_val = getattr(item, "CourseInstance", None)
                    
                    setattr(item, "CourseInstance", self)
                    

    @property
    def tdt4250case_Course14(self):
        return self.__tdt4250case_Course14

    @tdt4250case_Course14.setter
    def tdt4250case_Course14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_Course__tdt4250case_Course14", None)
        self.__tdt4250case_Course14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250case_CreditReductionCourse13"):
                opp_val = getattr(old_value, "tdt4250case_CreditReductionCourse13", None)
                if opp_val == self:
                    setattr(old_value, "tdt4250case_CreditReductionCourse13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250case_CreditReductionCourse13"):
                opp_val = getattr(value, "tdt4250case_CreditReductionCourse13", None)
                setattr(value, "tdt4250case_CreditReductionCourse13", self)

    @property
    def tdt4250case_Course3(self):
        return self.__tdt4250case_Course3

    @tdt4250case_Course3.setter
    def tdt4250case_Course3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_Course__tdt4250case_Course3", None)
        self.__tdt4250case_Course3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tdt4250case_Course5"):
                    opp_val = getattr(item, "tdt4250case_Course5", None)
                    
                    if opp_val == self:
                        setattr(item, "tdt4250case_Course5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tdt4250case_Course5"):
                    opp_val = getattr(item, "tdt4250case_Course5", None)
                    
                    setattr(item, "tdt4250case_Course5", self)
                    

    @property
    def Course26(self):
        return self.__Course26

    @Course26.setter
    def Course26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_Course__Course26", None)
        self.__Course26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "instance"):
                opp_val = getattr(old_value, "instance", None)
                if opp_val == self:
                    setattr(old_value, "instance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "instance"):
                opp_val = getattr(value, "instance", None)
                setattr(value, "instance", self)

class tdt4250case_Studyprogram:

    def __init__(self, code: str, Studyprogram: "tdt4250case_Course" = None, studyprogram: set["tdt4250case_Course"] = None, tdt4250case_Studyprogram: "tdt4250case_ScheduledActivity" = None):
        self.code = code
        self.Studyprogram = Studyprogram
        self.studyprogram = studyprogram if studyprogram is not None else set()
        self.tdt4250case_Studyprogram = tdt4250case_Studyprogram
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def Studyprogram(self):
        return self.__Studyprogram

    @Studyprogram.setter
    def Studyprogram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_Studyprogram__Studyprogram", None)
        self.__Studyprogram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course"):
                opp_val = getattr(old_value, "course", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course"):
                opp_val = getattr(value, "course", None)
                if opp_val is None:
                    setattr(value, "course", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def studyprogram(self):
        return self.__studyprogram

    @studyprogram.setter
    def studyprogram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_Studyprogram__studyprogram", None)
        self.__studyprogram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Course"):
                    opp_val = getattr(item, "Course", None)
                    
                    if opp_val == self:
                        setattr(item, "Course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Course"):
                    opp_val = getattr(item, "Course", None)
                    
                    setattr(item, "Course", self)
                    

    @property
    def tdt4250case_Studyprogram(self):
        return self.__tdt4250case_Studyprogram

    @tdt4250case_Studyprogram.setter
    def tdt4250case_Studyprogram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250case_Studyprogram__tdt4250case_Studyprogram", None)
        self.__tdt4250case_Studyprogram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250case_ScheduledActivity32"):
                opp_val = getattr(old_value, "tdt4250case_ScheduledActivity32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250case_ScheduledActivity32"):
                opp_val = getattr(value, "tdt4250case_ScheduledActivity32", None)
                if opp_val is None:
                    setattr(value, "tdt4250case_ScheduledActivity32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
