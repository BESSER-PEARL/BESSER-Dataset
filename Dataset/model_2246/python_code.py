from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Day(Enum):
    Monday = "Monday"
    Tuesday = "Tuesday"
    Wednesday = "Wednesday"
    Thursday = "Thursday"
    Friday = "Friday"
class Location(Enum):
    Trondheim = "Trondheim"
class Department(Enum):
    DepartmentofComputerScience = "DepartmentofComputerScience"
    DepartmentofMathematicalSciences = "DepartmentofMathematicalSciences"
class Semester(Enum):
    Spring2011 = "Spring2011"
    Autumn2011 = "Autumn2011"
    Spring2012 = "Spring2012"
    Autumn2012 = "Autumn2012"
    Spring2013 = "Spring2013"
    Autumn2013 = "Autumn2013"
    Spring2014 = "Spring2014"
    Autumn2014 = "Autumn2014"
    Spring2015 = "Spring2015"
    Autumn2015 = "Autumn2015"
    Spring2016 = "Spring2016"
    Autumn2016 = "Autumn2016"
    Spring2017 = "Spring2017"
    Autumn2017 = "Autumn2017"
    Autumn2010 = "Autumn2010"
    Spring2018 = "Spring2018"
class HourEnd(Enum):
    h0800 = "h0800"
    h0900 = "h0900"
    h1000 = "h1000"
    h1100 = "h1100"
    h1200 = "h1200"
    h1300 = "h1300"
    h1400 = "h1400"
    h1500 = "h1500"
    h1600 = "h1600"
    h1700 = "h1700"
    h1800 = "h1800"
    h1900 = "h1900"
    h2000 = "h2000"
class TeachingLanguage(Enum):
    English = "English"
    Norwegian = "Norwegian"
class HourStart(Enum):
    h0815 = "h0815"
    h0915 = "h0915"
    h1015 = "h1015"
    h1715 = "h1715"
    h1815 = "h1815"
    h1915 = "h1915"
    h1115 = "h1115"
    h1215 = "h1215"
    h1315 = "h1315"
    h1415 = "h1415"
    h1515 = "h1515"
    h1615 = "h1615"


############################################
# Definition of Classes
############################################

class courses_CourseHour:

    def __init__(self, day: str, startHour: str, endHour: str, type: str, room: str, courses_CourseHour: "courses_Timetable" = None, courses_CourseHour46: set["courses_StudyProgram"] = None):
        self.day = day
        self.startHour = startHour
        self.endHour = endHour
        self.type = type
        self.room = room
        self.courses_CourseHour = courses_CourseHour
        self.courses_CourseHour46 = courses_CourseHour46 if courses_CourseHour46 is not None else set()
        
    @property
    def endHour(self) -> str:
        return self.__endHour

    @endHour.setter
    def endHour(self, endHour: str):
        self.__endHour = endHour

    @property
    def room(self) -> str:
        return self.__room

    @room.setter
    def room(self, room: str):
        self.__room = room

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def day(self) -> str:
        return self.__day

    @day.setter
    def day(self, day: str):
        self.__day = day

    @property
    def startHour(self) -> str:
        return self.__startHour

    @startHour.setter
    def startHour(self, startHour: str):
        self.__startHour = startHour

    @property
    def courses_CourseHour(self):
        return self.__courses_CourseHour

    @courses_CourseHour.setter
    def courses_CourseHour(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_CourseHour__courses_CourseHour", None)
        self.__courses_CourseHour = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courses_Timetable44"):
                opp_val = getattr(old_value, "courses_Timetable44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courses_Timetable44"):
                opp_val = getattr(value, "courses_Timetable44", None)
                if opp_val is None:
                    setattr(value, "courses_Timetable44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def courses_CourseHour46(self):
        return self.__courses_CourseHour46

    @courses_CourseHour46.setter
    def courses_CourseHour46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_CourseHour__courses_CourseHour46", None)
        self.__courses_CourseHour46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "courses_StudyProgram47"):
                    opp_val = getattr(item, "courses_StudyProgram47", None)
                    
                    if opp_val == self:
                        setattr(item, "courses_StudyProgram47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "courses_StudyProgram47"):
                    opp_val = getattr(item, "courses_StudyProgram47", None)
                    
                    setattr(item, "courses_StudyProgram47", self)
                    

class courses_CreditsReduction:

    def __init__(self, reduction: float, courses_CreditsReduction: "courses_CourseInstance" = None, courses_CreditsReduction60: "courses_Course" = None):
        self.reduction = reduction
        self.courses_CreditsReduction = courses_CreditsReduction
        self.courses_CreditsReduction60 = courses_CreditsReduction60
        
    @property
    def reduction(self) -> float:
        return self.__reduction

    @reduction.setter
    def reduction(self, reduction: float):
        self.__reduction = reduction

    @property
    def courses_CreditsReduction60(self):
        return self.__courses_CreditsReduction60

    @courses_CreditsReduction60.setter
    def courses_CreditsReduction60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_CreditsReduction__courses_CreditsReduction60", None)
        self.__courses_CreditsReduction60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courses_Course61"):
                opp_val = getattr(old_value, "courses_Course61", None)
                if opp_val == self:
                    setattr(old_value, "courses_Course61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courses_Course61"):
                opp_val = getattr(value, "courses_Course61", None)
                setattr(value, "courses_Course61", self)

    @property
    def courses_CreditsReduction(self):
        return self.__courses_CreditsReduction

    @courses_CreditsReduction.setter
    def courses_CreditsReduction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_CreditsReduction__courses_CreditsReduction", None)
        self.__courses_CreditsReduction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courses_CourseInstance33"):
                opp_val = getattr(old_value, "courses_CourseInstance33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courses_CourseInstance33"):
                opp_val = getattr(value, "courses_CourseInstance33", None)
                if opp_val is None:
                    setattr(value, "courses_CourseInstance33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class courses_EvaluationForm:

    def __init__(self, type: str, weighting: str, duration: str, examAids: str, courses_EvaluationForm: "courses_ExaminationPanel" = None):
        self.type = type
        self.weighting = weighting
        self.duration = duration
        self.examAids = examAids
        self.courses_EvaluationForm = courses_EvaluationForm
        
    @property
    def weighting(self) -> str:
        return self.__weighting

    @weighting.setter
    def weighting(self, weighting: str):
        self.__weighting = weighting

    @property
    def examAids(self) -> str:
        return self.__examAids

    @examAids.setter
    def examAids(self, examAids: str):
        self.__examAids = examAids

    @property
    def duration(self) -> str:
        return self.__duration

    @duration.setter
    def duration(self, duration: str):
        self.__duration = duration

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def courses_EvaluationForm(self):
        return self.__courses_EvaluationForm

    @courses_EvaluationForm.setter
    def courses_EvaluationForm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_EvaluationForm__courses_EvaluationForm", None)
        self.__courses_EvaluationForm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courses_ExaminationPanel49"):
                opp_val = getattr(old_value, "courses_ExaminationPanel49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courses_ExaminationPanel49"):
                opp_val = getattr(value, "courses_ExaminationPanel49", None)
                if opp_val is None:
                    setattr(value, "courses_ExaminationPanel49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class courses_Timetable:

    pass
class courses_Coursework:

    def __init__(self, termNumber: int, teachingSemester: str, numLectHour: int, numLabHour: int, numSpecHour: int, instructionLanguage: str, location: str, courses_Coursework: "courses_CourseInstance" = None):
        self.termNumber = termNumber
        self.teachingSemester = teachingSemester
        self.numLectHour = numLectHour
        self.numLabHour = numLabHour
        self.numSpecHour = numSpecHour
        self.instructionLanguage = instructionLanguage
        self.location = location
        self.courses_Coursework = courses_Coursework
        
    @property
    def teachingSemester(self) -> str:
        return self.__teachingSemester

    @teachingSemester.setter
    def teachingSemester(self, teachingSemester: str):
        self.__teachingSemester = teachingSemester

    @property
    def termNumber(self) -> int:
        return self.__termNumber

    @termNumber.setter
    def termNumber(self, termNumber: int):
        self.__termNumber = termNumber

    @property
    def numLabHour(self) -> int:
        return self.__numLabHour

    @numLabHour.setter
    def numLabHour(self, numLabHour: int):
        self.__numLabHour = numLabHour

    @property
    def instructionLanguage(self) -> str:
        return self.__instructionLanguage

    @instructionLanguage.setter
    def instructionLanguage(self, instructionLanguage: str):
        self.__instructionLanguage = instructionLanguage

    @property
    def numSpecHour(self) -> int:
        return self.__numSpecHour

    @numSpecHour.setter
    def numSpecHour(self, numSpecHour: int):
        self.__numSpecHour = numSpecHour

    @property
    def numLectHour(self) -> int:
        return self.__numLectHour

    @numLectHour.setter
    def numLectHour(self, numLectHour: int):
        self.__numLectHour = numLectHour

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def courses_Coursework(self):
        return self.__courses_Coursework

    @courses_Coursework.setter
    def courses_Coursework(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_Coursework__courses_Coursework", None)
        self.__courses_Coursework = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courses_CourseInstance21"):
                opp_val = getattr(old_value, "courses_CourseInstance21", None)
                if opp_val == self:
                    setattr(old_value, "courses_CourseInstance21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courses_CourseInstance21"):
                opp_val = getattr(value, "courses_CourseInstance21", None)
                setattr(value, "courses_CourseInstance21", self)

class courses_ContactInfo:

    def __init__(self, department: str, phone: str, courses_ContactInfo: "courses_CourseInstance" = None, courses_ContactInfo38: "courses_Person" = None, courses_ContactInfo41: set["courses_Person"] = None):
        self.department = department
        self.phone = phone
        self.courses_ContactInfo = courses_ContactInfo
        self.courses_ContactInfo38 = courses_ContactInfo38
        self.courses_ContactInfo41 = courses_ContactInfo41 if courses_ContactInfo41 is not None else set()
        
    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def department(self) -> str:
        return self.__department

    @department.setter
    def department(self, department: str):
        self.__department = department

    @property
    def courses_ContactInfo38(self):
        return self.__courses_ContactInfo38

    @courses_ContactInfo38.setter
    def courses_ContactInfo38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_ContactInfo__courses_ContactInfo38", None)
        self.__courses_ContactInfo38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courses_Person39"):
                opp_val = getattr(old_value, "courses_Person39", None)
                if opp_val == self:
                    setattr(old_value, "courses_Person39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courses_Person39"):
                opp_val = getattr(value, "courses_Person39", None)
                setattr(value, "courses_Person39", self)

    @property
    def courses_ContactInfo41(self):
        return self.__courses_ContactInfo41

    @courses_ContactInfo41.setter
    def courses_ContactInfo41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_ContactInfo__courses_ContactInfo41", None)
        self.__courses_ContactInfo41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "courses_Person42"):
                    opp_val = getattr(item, "courses_Person42", None)
                    
                    if opp_val == self:
                        setattr(item, "courses_Person42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "courses_Person42"):
                    opp_val = getattr(item, "courses_Person42", None)
                    
                    setattr(item, "courses_Person42", self)
                    

    @property
    def courses_ContactInfo(self):
        return self.__courses_ContactInfo

    @courses_ContactInfo.setter
    def courses_ContactInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_ContactInfo__courses_ContactInfo", None)
        self.__courses_ContactInfo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courses_CourseInstance16"):
                opp_val = getattr(old_value, "courses_CourseInstance16", None)
                if opp_val == self:
                    setattr(old_value, "courses_CourseInstance16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courses_CourseInstance16"):
                opp_val = getattr(value, "courses_CourseInstance16", None)
                setattr(value, "courses_CourseInstance16", self)

class courses_ExaminationPanel:

    def __init__(self, date: str, time: str, room: str, courses_ExaminationPanel: "courses_CourseInstance" = None, courses_ExaminationPanel36: "courses_ExaminationArrangement" = None, courses_ExaminationPanel49: set["courses_EvaluationForm"] = None):
        self.date = date
        self.time = time
        self.room = room
        self.courses_ExaminationPanel = courses_ExaminationPanel
        self.courses_ExaminationPanel36 = courses_ExaminationPanel36
        self.courses_ExaminationPanel49 = courses_ExaminationPanel49 if courses_ExaminationPanel49 is not None else set()
        
    @property
    def room(self) -> str:
        return self.__room

    @room.setter
    def room(self, room: str):
        self.__room = room

    @property
    def date(self) -> str:
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def time(self) -> str:
        return self.__time

    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def courses_ExaminationPanel49(self):
        return self.__courses_ExaminationPanel49

    @courses_ExaminationPanel49.setter
    def courses_ExaminationPanel49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_ExaminationPanel__courses_ExaminationPanel49", None)
        self.__courses_ExaminationPanel49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "courses_EvaluationForm"):
                    opp_val = getattr(item, "courses_EvaluationForm", None)
                    
                    if opp_val == self:
                        setattr(item, "courses_EvaluationForm", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "courses_EvaluationForm"):
                    opp_val = getattr(item, "courses_EvaluationForm", None)
                    
                    setattr(item, "courses_EvaluationForm", self)
                    

    @property
    def courses_ExaminationPanel36(self):
        return self.__courses_ExaminationPanel36

    @courses_ExaminationPanel36.setter
    def courses_ExaminationPanel36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_ExaminationPanel__courses_ExaminationPanel36", None)
        self.__courses_ExaminationPanel36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courses_ExaminationArrangement35"):
                opp_val = getattr(old_value, "courses_ExaminationArrangement35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courses_ExaminationArrangement35"):
                opp_val = getattr(value, "courses_ExaminationArrangement35", None)
                if opp_val is None:
                    setattr(value, "courses_ExaminationArrangement35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def courses_ExaminationPanel(self):
        return self.__courses_ExaminationPanel

    @courses_ExaminationPanel.setter
    def courses_ExaminationPanel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_ExaminationPanel__courses_ExaminationPanel", None)
        self.__courses_ExaminationPanel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courses_CourseInstance25"):
                opp_val = getattr(old_value, "courses_CourseInstance25", None)
                if opp_val == self:
                    setattr(old_value, "courses_CourseInstance25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courses_CourseInstance25"):
                opp_val = getattr(value, "courses_CourseInstance25", None)
                setattr(value, "courses_CourseInstance25", self)

class courses_CourseInstance:

    pass
class courses_StudyProgram:

    def __init__(self, code: str, StudyProgram: "courses_Course" = None, courses_StudyProgram: "courses_University" = None, courses_StudyProgram47: "courses_CourseHour" = None, StudyProgram58: "courses_Person" = None, studyProgram: set["courses_Course"] = None, studyProgram52: set["courses_Person"] = None):
        self.code = code
        self.StudyProgram = StudyProgram
        self.courses_StudyProgram = courses_StudyProgram
        self.courses_StudyProgram47 = courses_StudyProgram47
        self.StudyProgram58 = StudyProgram58
        self.studyProgram = studyProgram if studyProgram is not None else set()
        self.studyProgram52 = studyProgram52 if studyProgram52 is not None else set()
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def studyProgram(self):
        return self.__studyProgram

    @studyProgram.setter
    def studyProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_StudyProgram__studyProgram", None)
        self.__studyProgram = value if value is not None else set()
        
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
    def courses_StudyProgram47(self):
        return self.__courses_StudyProgram47

    @courses_StudyProgram47.setter
    def courses_StudyProgram47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_StudyProgram__courses_StudyProgram47", None)
        self.__courses_StudyProgram47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courses_CourseHour46"):
                opp_val = getattr(old_value, "courses_CourseHour46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courses_CourseHour46"):
                opp_val = getattr(value, "courses_CourseHour46", None)
                if opp_val is None:
                    setattr(value, "courses_CourseHour46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StudyProgram(self):
        return self.__StudyProgram

    @StudyProgram.setter
    def StudyProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_StudyProgram__StudyProgram", None)
        self.__StudyProgram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courses"):
                opp_val = getattr(old_value, "courses", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courses"):
                opp_val = getattr(value, "courses", None)
                if opp_val is None:
                    setattr(value, "courses", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def studyProgram52(self):
        return self.__studyProgram52

    @studyProgram52.setter
    def studyProgram52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_StudyProgram__studyProgram52", None)
        self.__studyProgram52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person53"):
                    opp_val = getattr(item, "Person53", None)
                    
                    if opp_val == self:
                        setattr(item, "Person53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person53"):
                    opp_val = getattr(item, "Person53", None)
                    
                    setattr(item, "Person53", self)
                    

    @property
    def courses_StudyProgram(self):
        return self.__courses_StudyProgram

    @courses_StudyProgram.setter
    def courses_StudyProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_StudyProgram__courses_StudyProgram", None)
        self.__courses_StudyProgram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courses_University4"):
                opp_val = getattr(old_value, "courses_University4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courses_University4"):
                opp_val = getattr(value, "courses_University4", None)
                if opp_val is None:
                    setattr(value, "courses_University4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StudyProgram58(self):
        return self.__StudyProgram58

    @StudyProgram58.setter
    def StudyProgram58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_StudyProgram__StudyProgram58", None)
        self.__StudyProgram58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student57"):
                opp_val = getattr(old_value, "student57", None)
                if opp_val == self:
                    setattr(old_value, "student57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student57"):
                opp_val = getattr(value, "student57", None)
                setattr(value, "student57", self)

class courses_Paragraph:

    def __init__(self, name: str, description: str, courses_Paragraph: "courses_Content" = None):
        self.name = name
        self.description = description
        self.courses_Paragraph = courses_Paragraph
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def courses_Paragraph(self):
        return self.__courses_Paragraph

    @courses_Paragraph.setter
    def courses_Paragraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_Paragraph__courses_Paragraph", None)
        self.__courses_Paragraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courses_Content14"):
                opp_val = getattr(old_value, "courses_Content14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courses_Content14"):
                opp_val = getattr(value, "courses_Content14", None)
                if opp_val is None:
                    setattr(value, "courses_Content14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class courses_ExaminationArrangement:

    def __init__(self, type: str, grade: str, courses_ExaminationArrangement: "courses_Content" = None, courses_ExaminationArrangement35: set["courses_ExaminationPanel"] = None):
        self.type = type
        self.grade = grade
        self.courses_ExaminationArrangement = courses_ExaminationArrangement
        self.courses_ExaminationArrangement35 = courses_ExaminationArrangement35 if courses_ExaminationArrangement35 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def grade(self) -> str:
        return self.__grade

    @grade.setter
    def grade(self, grade: str):
        self.__grade = grade

    @property
    def courses_ExaminationArrangement35(self):
        return self.__courses_ExaminationArrangement35

    @courses_ExaminationArrangement35.setter
    def courses_ExaminationArrangement35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_ExaminationArrangement__courses_ExaminationArrangement35", None)
        self.__courses_ExaminationArrangement35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "courses_ExaminationPanel36"):
                    opp_val = getattr(item, "courses_ExaminationPanel36", None)
                    
                    if opp_val == self:
                        setattr(item, "courses_ExaminationPanel36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "courses_ExaminationPanel36"):
                    opp_val = getattr(item, "courses_ExaminationPanel36", None)
                    
                    setattr(item, "courses_ExaminationPanel36", self)
                    

    @property
    def courses_ExaminationArrangement(self):
        return self.__courses_ExaminationArrangement

    @courses_ExaminationArrangement.setter
    def courses_ExaminationArrangement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_ExaminationArrangement__courses_ExaminationArrangement", None)
        self.__courses_ExaminationArrangement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courses_Content"):
                opp_val = getattr(old_value, "courses_Content", None)
                if opp_val == self:
                    setattr(old_value, "courses_Content", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courses_Content"):
                opp_val = getattr(value, "courses_Content", None)
                setattr(value, "courses_Content", self)

class courses_Content:

    pass
class courses_Person:

    def __init__(self, name: str, Credits: float, courses_Person: "courses_University" = None, Person: "courses_Course" = None, courses_Person7: "courses_University" = None, courses_Person39: "courses_ContactInfo" = None, courses_Person42: "courses_ContactInfo" = None, student: set["courses_Course"] = None, student57: "courses_StudyProgram" = None, Person53: "courses_StudyProgram" = None):
        self.name = name
        self.Credits = Credits
        self.courses_Person = courses_Person
        self.Person = Person
        self.courses_Person7 = courses_Person7
        self.courses_Person39 = courses_Person39
        self.courses_Person42 = courses_Person42
        self.student = student if student is not None else set()
        self.student57 = student57
        self.Person53 = Person53
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Credits(self) -> float:
        return self.__Credits

    @Credits.setter
    def Credits(self, Credits: float):
        self.__Credits = Credits

    @property
    def courses_Person39(self):
        return self.__courses_Person39

    @courses_Person39.setter
    def courses_Person39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_Person__courses_Person39", None)
        self.__courses_Person39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courses_ContactInfo38"):
                opp_val = getattr(old_value, "courses_ContactInfo38", None)
                if opp_val == self:
                    setattr(old_value, "courses_ContactInfo38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courses_ContactInfo38"):
                opp_val = getattr(value, "courses_ContactInfo38", None)
                setattr(value, "courses_ContactInfo38", self)

    @property
    def Person53(self):
        return self.__Person53

    @Person53.setter
    def Person53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_Person__Person53", None)
        self.__Person53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyProgram52"):
                opp_val = getattr(old_value, "studyProgram52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyProgram52"):
                opp_val = getattr(value, "studyProgram52", None)
                if opp_val is None:
                    setattr(value, "studyProgram52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_Person__Person", None)
        self.__Person = value
        
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
    def courses_Person42(self):
        return self.__courses_Person42

    @courses_Person42.setter
    def courses_Person42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_Person__courses_Person42", None)
        self.__courses_Person42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courses_ContactInfo41"):
                opp_val = getattr(old_value, "courses_ContactInfo41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courses_ContactInfo41"):
                opp_val = getattr(value, "courses_ContactInfo41", None)
                if opp_val is None:
                    setattr(value, "courses_ContactInfo41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def student57(self):
        return self.__student57

    @student57.setter
    def student57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_Person__student57", None)
        self.__student57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyProgram58"):
                opp_val = getattr(old_value, "StudyProgram58", None)
                if opp_val == self:
                    setattr(old_value, "StudyProgram58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyProgram58"):
                opp_val = getattr(value, "StudyProgram58", None)
                setattr(value, "StudyProgram58", self)

    @property
    def courses_Person(self):
        return self.__courses_Person

    @courses_Person.setter
    def courses_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_Person__courses_Person", None)
        self.__courses_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courses_University2"):
                opp_val = getattr(old_value, "courses_University2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courses_University2"):
                opp_val = getattr(value, "courses_University2", None)
                if opp_val is None:
                    setattr(value, "courses_University2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def courses_Person7(self):
        return self.__courses_Person7

    @courses_Person7.setter
    def courses_Person7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_Person__courses_Person7", None)
        self.__courses_Person7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courses_University6"):
                opp_val = getattr(old_value, "courses_University6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courses_University6"):
                opp_val = getattr(value, "courses_University6", None)
                if opp_val is None:
                    setattr(value, "courses_University6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_Person__student", None)
        self.__student = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Course55"):
                    opp_val = getattr(item, "Course55", None)
                    
                    if opp_val == self:
                        setattr(item, "Course55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Course55"):
                    opp_val = getattr(item, "Course55", None)
                    
                    setattr(item, "Course55", self)
                    

    def SignUpExam(self, course: str):
        # TODO: Implement SignUpExam method
        pass

    def CancelExam(self, course: str):
        # TODO: Implement CancelExam method
        pass

    def PassingExam(self, course: str):
        # TODO: Implement PassingExam method
        pass

class courses_Course:

    def __init__(self, name: str, credit: float, code: str, courses_Course: "courses_University" = None, courses: set["courses_StudyProgram"] = None, course: set["courses_Person"] = None, courses_Course9: set["courses_CourseInstance"] = None, courses_Course28: "courses_CourseInstance" = None, courses_Course31: "courses_CourseInstance" = None, Course55: "courses_Person" = None, Course: "courses_StudyProgram" = None, courses_Course61: "courses_CreditsReduction" = None):
        self.name = name
        self.credit = credit
        self.code = code
        self.courses_Course = courses_Course
        self.courses = courses if courses is not None else set()
        self.course = course if course is not None else set()
        self.courses_Course9 = courses_Course9 if courses_Course9 is not None else set()
        self.courses_Course28 = courses_Course28
        self.courses_Course31 = courses_Course31
        self.Course55 = Course55
        self.Course = Course
        self.courses_Course61 = courses_Course61
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def credit(self) -> float:
        return self.__credit

    @credit.setter
    def credit(self, credit: float):
        self.__credit = credit

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def courses_Course28(self):
        return self.__courses_Course28

    @courses_Course28.setter
    def courses_Course28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_Course__courses_Course28", None)
        self.__courses_Course28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courses_CourseInstance27"):
                opp_val = getattr(old_value, "courses_CourseInstance27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courses_CourseInstance27"):
                opp_val = getattr(value, "courses_CourseInstance27", None)
                if opp_val is None:
                    setattr(value, "courses_CourseInstance27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Course55(self):
        return self.__Course55

    @Course55.setter
    def Course55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_Course__Course55", None)
        self.__Course55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student"):
                opp_val = getattr(old_value, "student", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student"):
                opp_val = getattr(value, "student", None)
                if opp_val is None:
                    setattr(value, "student", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def courses_Course(self):
        return self.__courses_Course

    @courses_Course.setter
    def courses_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_Course__courses_Course", None)
        self.__courses_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courses_University"):
                opp_val = getattr(old_value, "courses_University", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courses_University"):
                opp_val = getattr(value, "courses_University", None)
                if opp_val is None:
                    setattr(value, "courses_University", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_Course__course", None)
        self.__course = value if value is not None else set()
        
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
    def courses_Course61(self):
        return self.__courses_Course61

    @courses_Course61.setter
    def courses_Course61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_Course__courses_Course61", None)
        self.__courses_Course61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courses_CreditsReduction60"):
                opp_val = getattr(old_value, "courses_CreditsReduction60", None)
                if opp_val == self:
                    setattr(old_value, "courses_CreditsReduction60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courses_CreditsReduction60"):
                opp_val = getattr(value, "courses_CreditsReduction60", None)
                setattr(value, "courses_CreditsReduction60", self)

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_Course__courses", None)
        self.__courses = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StudyProgram"):
                    opp_val = getattr(item, "StudyProgram", None)
                    
                    if opp_val == self:
                        setattr(item, "StudyProgram", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StudyProgram"):
                    opp_val = getattr(item, "StudyProgram", None)
                    
                    setattr(item, "StudyProgram", self)
                    

    @property
    def Course(self):
        return self.__Course

    @Course.setter
    def Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_Course__Course", None)
        self.__Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyProgram"):
                opp_val = getattr(old_value, "studyProgram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyProgram"):
                opp_val = getattr(value, "studyProgram", None)
                if opp_val is None:
                    setattr(value, "studyProgram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def courses_Course31(self):
        return self.__courses_Course31

    @courses_Course31.setter
    def courses_Course31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_Course__courses_Course31", None)
        self.__courses_Course31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courses_CourseInstance30"):
                opp_val = getattr(old_value, "courses_CourseInstance30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courses_CourseInstance30"):
                opp_val = getattr(value, "courses_CourseInstance30", None)
                if opp_val is None:
                    setattr(value, "courses_CourseInstance30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def courses_Course9(self):
        return self.__courses_Course9

    @courses_Course9.setter
    def courses_Course9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_Course__courses_Course9", None)
        self.__courses_Course9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "courses_CourseInstance"):
                    opp_val = getattr(item, "courses_CourseInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "courses_CourseInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "courses_CourseInstance"):
                    opp_val = getattr(item, "courses_CourseInstance", None)
                    
                    setattr(item, "courses_CourseInstance", self)
                    

class courses_University:

    def __init__(self, name: str, courses_University: set["courses_Course"] = None, courses_University2: set["courses_Person"] = None, courses_University4: set["courses_StudyProgram"] = None, courses_University6: set["courses_Person"] = None):
        self.name = name
        self.courses_University = courses_University if courses_University is not None else set()
        self.courses_University2 = courses_University2 if courses_University2 is not None else set()
        self.courses_University4 = courses_University4 if courses_University4 is not None else set()
        self.courses_University6 = courses_University6 if courses_University6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def courses_University6(self):
        return self.__courses_University6

    @courses_University6.setter
    def courses_University6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_University__courses_University6", None)
        self.__courses_University6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "courses_Person7"):
                    opp_val = getattr(item, "courses_Person7", None)
                    
                    if opp_val == self:
                        setattr(item, "courses_Person7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "courses_Person7"):
                    opp_val = getattr(item, "courses_Person7", None)
                    
                    setattr(item, "courses_Person7", self)
                    

    @property
    def courses_University4(self):
        return self.__courses_University4

    @courses_University4.setter
    def courses_University4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_University__courses_University4", None)
        self.__courses_University4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "courses_StudyProgram"):
                    opp_val = getattr(item, "courses_StudyProgram", None)
                    
                    if opp_val == self:
                        setattr(item, "courses_StudyProgram", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "courses_StudyProgram"):
                    opp_val = getattr(item, "courses_StudyProgram", None)
                    
                    setattr(item, "courses_StudyProgram", self)
                    

    @property
    def courses_University(self):
        return self.__courses_University

    @courses_University.setter
    def courses_University(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_University__courses_University", None)
        self.__courses_University = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "courses_Course"):
                    opp_val = getattr(item, "courses_Course", None)
                    
                    if opp_val == self:
                        setattr(item, "courses_Course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "courses_Course"):
                    opp_val = getattr(item, "courses_Course", None)
                    
                    setattr(item, "courses_Course", self)
                    

    @property
    def courses_University2(self):
        return self.__courses_University2

    @courses_University2.setter
    def courses_University2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courses_University__courses_University2", None)
        self.__courses_University2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "courses_Person"):
                    opp_val = getattr(item, "courses_Person", None)
                    
                    if opp_val == self:
                        setattr(item, "courses_Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "courses_Person"):
                    opp_val = getattr(item, "courses_Person", None)
                    
                    setattr(item, "courses_Person", self)
                    

    def StaffInscription(self, name: str):
        # TODO: Implement StaffInscription method
        pass

    def StudentInscription(self, name: str):
        # TODO: Implement StudentInscription method
        pass
