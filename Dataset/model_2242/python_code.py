from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class StudyProgramCode(Enum):
    MTDT = "MTDT"
    BIT = "BIT"
    MIT = "MIT"
    MTIØT = "MTIØT"
class CourseWorkType(Enum):
    LABHOUR = "LABHOUR"
    LECTURE = "LECTURE"
class DeadlineEvaluation(Enum):
    ASSIGNMENT = "ASSIGNMENT"
    PROJECT = "PROJECT"


############################################
# Definition of Classes
############################################

class course_desc_Univ:

    pass
class course_desc_PersonRole(ABC):

    pass
class course_desc_Person:

    def __init__(self, fullName: str, lastName: str, personNr: str, name: str, Person: "course_desc_PersonRole" = None, linkedTo: set["course_desc_PersonRole"] = None, course_desc_Person: "course_desc_Univ" = None):
        self.fullName = fullName
        self.lastName = lastName
        self.personNr = personNr
        self.name = name
        self.Person = Person
        self.linkedTo = linkedTo if linkedTo is not None else set()
        self.course_desc_Person = course_desc_Person
        
    @property
    def personNr(self) -> str:
        return self.__personNr

    @personNr.setter
    def personNr(self, personNr: str):
        self.__personNr = personNr

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fullName(self) -> str:
        return self.__fullName

    @fullName.setter
    def fullName(self, fullName: str):
        self.__fullName = fullName

    @property
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_Person__Person", None)
        self.__Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hasRole"):
                opp_val = getattr(old_value, "hasRole", None)
                if opp_val == self:
                    setattr(old_value, "hasRole", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hasRole"):
                opp_val = getattr(value, "hasRole", None)
                setattr(value, "hasRole", self)

    @property
    def course_desc_Person(self):
        return self.__course_desc_Person

    @course_desc_Person.setter
    def course_desc_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_Person__course_desc_Person", None)
        self.__course_desc_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course_desc_Univ43"):
                opp_val = getattr(old_value, "course_desc_Univ43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course_desc_Univ43"):
                opp_val = getattr(value, "course_desc_Univ43", None)
                if opp_val is None:
                    setattr(value, "course_desc_Univ43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def linkedTo(self):
        return self.__linkedTo

    @linkedTo.setter
    def linkedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_Person__linkedTo", None)
        self.__linkedTo = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PersonRole"):
                    opp_val = getattr(item, "PersonRole", None)
                    
                    if opp_val == self:
                        setattr(item, "PersonRole", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PersonRole"):
                    opp_val = getattr(item, "PersonRole", None)
                    
                    setattr(item, "PersonRole", self)
                    

class PersonRole:

    pass
class course_desc_CourseWork:

    def __init__(self, Duration: int, Room: str, isMandatory: bool, isRestricted: bool, Type: str, course_desc_CourseWork: "course_desc_Timetable" = None):
        self.Duration = Duration
        self.Room = Room
        self.isMandatory = isMandatory
        self.isRestricted = isRestricted
        self.Type = Type
        self.course_desc_CourseWork = course_desc_CourseWork
        
    @property
    def Duration(self) -> int:
        return self.__Duration

    @Duration.setter
    def Duration(self, Duration: int):
        self.__Duration = Duration

    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def Room(self) -> str:
        return self.__Room

    @Room.setter
    def Room(self, Room: str):
        self.__Room = Room

    @property
    def isMandatory(self) -> bool:
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: bool):
        self.__isMandatory = isMandatory

    @property
    def isRestricted(self) -> bool:
        return self.__isRestricted

    @isRestricted.setter
    def isRestricted(self, isRestricted: bool):
        self.__isRestricted = isRestricted

    @property
    def course_desc_CourseWork(self):
        return self.__course_desc_CourseWork

    @course_desc_CourseWork.setter
    def course_desc_CourseWork(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_CourseWork__course_desc_CourseWork", None)
        self.__course_desc_CourseWork = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course_desc_Timetable17"):
                opp_val = getattr(old_value, "course_desc_Timetable17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course_desc_Timetable17"):
                opp_val = getattr(value, "course_desc_Timetable17", None)
                if opp_val is None:
                    setattr(value, "course_desc_Timetable17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class course_desc_StudyProgram:

    def __init__(self, studyCode: str, StudyProgram: "course_desc_Department" = None, course_desc_StudyProgram: "course_desc_Timetable" = None, manages: "course_desc_Department" = None, course_desc_StudyProgram24: set["course_desc_Course"] = None):
        self.studyCode = studyCode
        self.StudyProgram = StudyProgram
        self.course_desc_StudyProgram = course_desc_StudyProgram
        self.manages = manages
        self.course_desc_StudyProgram24 = course_desc_StudyProgram24 if course_desc_StudyProgram24 is not None else set()
        
    @property
    def studyCode(self) -> str:
        return self.__studyCode

    @studyCode.setter
    def studyCode(self, studyCode: str):
        self.__studyCode = studyCode

    @property
    def course_desc_StudyProgram(self):
        return self.__course_desc_StudyProgram

    @course_desc_StudyProgram.setter
    def course_desc_StudyProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_StudyProgram__course_desc_StudyProgram", None)
        self.__course_desc_StudyProgram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course_desc_Timetable19"):
                opp_val = getattr(old_value, "course_desc_Timetable19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course_desc_Timetable19"):
                opp_val = getattr(value, "course_desc_Timetable19", None)
                if opp_val is None:
                    setattr(value, "course_desc_Timetable19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def manages(self):
        return self.__manages

    @manages.setter
    def manages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_StudyProgram__manages", None)
        self.__manages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Department27"):
                opp_val = getattr(old_value, "Department27", None)
                if opp_val == self:
                    setattr(old_value, "Department27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Department27"):
                opp_val = getattr(value, "Department27", None)
                setattr(value, "Department27", self)

    @property
    def course_desc_StudyProgram24(self):
        return self.__course_desc_StudyProgram24

    @course_desc_StudyProgram24.setter
    def course_desc_StudyProgram24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_StudyProgram__course_desc_StudyProgram24", None)
        self.__course_desc_StudyProgram24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "course_desc_Course25"):
                    opp_val = getattr(item, "course_desc_Course25", None)
                    
                    if opp_val == self:
                        setattr(item, "course_desc_Course25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "course_desc_Course25"):
                    opp_val = getattr(item, "course_desc_Course25", None)
                    
                    setattr(item, "course_desc_Course25", self)
                    

    @property
    def StudyProgram(self):
        return self.__StudyProgram

    @StudyProgram.setter
    def StudyProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_StudyProgram__StudyProgram", None)
        self.__StudyProgram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "belongs"):
                opp_val = getattr(old_value, "belongs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "belongs"):
                opp_val = getattr(value, "belongs", None)
                if opp_val is None:
                    setattr(value, "belongs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class course_desc_Student(PersonRole):

    def __init__(self, totalStudyPoints: float, Student: "course_desc_Exam" = None, hasRegisteredStudents: set["course_desc_Exam"] = None, course_desc_Student: set["course_desc_Exam"] = None, course_desc_Student49: "course_desc_Univ" = None):
        self.totalStudyPoints = totalStudyPoints
        self.Student = Student
        self.hasRegisteredStudents = hasRegisteredStudents if hasRegisteredStudents is not None else set()
        self.course_desc_Student = course_desc_Student if course_desc_Student is not None else set()
        self.course_desc_Student49 = course_desc_Student49
        
    @property
    def totalStudyPoints(self) -> float:
        return self.__totalStudyPoints

    @totalStudyPoints.setter
    def totalStudyPoints(self, totalStudyPoints: float):
        self.__totalStudyPoints = totalStudyPoints

    @property
    def hasRegisteredStudents(self):
        return self.__hasRegisteredStudents

    @hasRegisteredStudents.setter
    def hasRegisteredStudents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_Student__hasRegisteredStudents", None)
        self.__hasRegisteredStudents = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Exam"):
                    opp_val = getattr(item, "Exam", None)
                    
                    if opp_val == self:
                        setattr(item, "Exam", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Exam"):
                    opp_val = getattr(item, "Exam", None)
                    
                    setattr(item, "Exam", self)
                    

    @property
    def Student(self):
        return self.__Student

    @Student.setter
    def Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_Student__Student", None)
        self.__Student = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hasExams"):
                opp_val = getattr(old_value, "hasExams", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hasExams"):
                opp_val = getattr(value, "hasExams", None)
                if opp_val is None:
                    setattr(value, "hasExams", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def course_desc_Student(self):
        return self.__course_desc_Student

    @course_desc_Student.setter
    def course_desc_Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_Student__course_desc_Student", None)
        self.__course_desc_Student = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "course_desc_Exam"):
                    opp_val = getattr(item, "course_desc_Exam", None)
                    
                    if opp_val == self:
                        setattr(item, "course_desc_Exam", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "course_desc_Exam"):
                    opp_val = getattr(item, "course_desc_Exam", None)
                    
                    setattr(item, "course_desc_Exam", self)
                    

    @property
    def course_desc_Student49(self):
        return self.__course_desc_Student49

    @course_desc_Student49.setter
    def course_desc_Student49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_Student__course_desc_Student49", None)
        self.__course_desc_Student49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course_desc_Univ48"):
                opp_val = getattr(old_value, "course_desc_Univ48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course_desc_Univ48"):
                opp_val = getattr(value, "course_desc_Univ48", None)
                if opp_val is None:
                    setattr(value, "course_desc_Univ48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def takeExam(self, exam: str) -> bool:
        # TODO: Implement takeExam method
        pass

    def cancelExam(self, exam: str) -> bool:
        # TODO: Implement cancelExam method
        pass

    def signUpForExam(self, exam: str) -> bool:
        # TODO: Implement signUpForExam method
        pass

class Evaluation:

    pass
class course_desc_EvaluationWithDeadline(Evaluation):

    def __init__(self, deadlineEvaluation: str):
        self.deadlineEvaluation = deadlineEvaluation
        
    @property
    def deadlineEvaluation(self) -> str:
        return self.__deadlineEvaluation

    @deadlineEvaluation.setter
    def deadlineEvaluation(self, deadlineEvaluation: str):
        self.__deadlineEvaluation = deadlineEvaluation

class course_desc_Exam(Evaluation):

    def __init__(self, date: date, place: str, duration: float, hasExams: set["course_desc_Student"] = None, Exam: "course_desc_Student" = None, course_desc_Exam: "course_desc_Student" = None):
        self.date = date
        self.place = place
        self.duration = duration
        self.hasExams = hasExams if hasExams is not None else set()
        self.Exam = Exam
        self.course_desc_Exam = course_desc_Exam
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def place(self) -> str:
        return self.__place

    @place.setter
    def place(self, place: str):
        self.__place = place

    @property
    def duration(self) -> float:
        return self.__duration

    @duration.setter
    def duration(self, duration: float):
        self.__duration = duration

    @property
    def course_desc_Exam(self):
        return self.__course_desc_Exam

    @course_desc_Exam.setter
    def course_desc_Exam(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_Exam__course_desc_Exam", None)
        self.__course_desc_Exam = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course_desc_Student"):
                opp_val = getattr(old_value, "course_desc_Student", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course_desc_Student"):
                opp_val = getattr(value, "course_desc_Student", None)
                if opp_val is None:
                    setattr(value, "course_desc_Student", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Exam(self):
        return self.__Exam

    @Exam.setter
    def Exam(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_Exam__Exam", None)
        self.__Exam = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hasRegisteredStudents"):
                opp_val = getattr(old_value, "hasRegisteredStudents", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hasRegisteredStudents"):
                opp_val = getattr(value, "hasRegisteredStudents", None)
                if opp_val is None:
                    setattr(value, "hasRegisteredStudents", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hasExams(self):
        return self.__hasExams

    @hasExams.setter
    def hasExams(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_Exam__hasExams", None)
        self.__hasExams = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Student"):
                    opp_val = getattr(item, "Student", None)
                    
                    if opp_val == self:
                        setattr(item, "Student", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Student"):
                    opp_val = getattr(item, "Student", None)
                    
                    setattr(item, "Student", self)
                    

class course_desc_Department:

    def __init__(self, name: str, Department: "course_desc_CourseInstance" = None, isInstanceOf: set["course_desc_CourseInstance"] = None, belongs: set["course_desc_StudyProgram"] = None, Department27: "course_desc_StudyProgram" = None, course_desc_Department: "course_desc_Univ" = None):
        self.name = name
        self.Department = Department
        self.isInstanceOf = isInstanceOf if isInstanceOf is not None else set()
        self.belongs = belongs if belongs is not None else set()
        self.Department27 = Department27
        self.course_desc_Department = course_desc_Department
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def course_desc_Department(self):
        return self.__course_desc_Department

    @course_desc_Department.setter
    def course_desc_Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_Department__course_desc_Department", None)
        self.__course_desc_Department = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course_desc_Univ"):
                opp_val = getattr(old_value, "course_desc_Univ", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course_desc_Univ"):
                opp_val = getattr(value, "course_desc_Univ", None)
                if opp_val is None:
                    setattr(value, "course_desc_Univ", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def isInstanceOf(self):
        return self.__isInstanceOf

    @isInstanceOf.setter
    def isInstanceOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_Department__isInstanceOf", None)
        self.__isInstanceOf = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CourseInstance11"):
                    opp_val = getattr(item, "CourseInstance11", None)
                    
                    if opp_val == self:
                        setattr(item, "CourseInstance11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CourseInstance11"):
                    opp_val = getattr(item, "CourseInstance11", None)
                    
                    setattr(item, "CourseInstance11", self)
                    

    @property
    def Department27(self):
        return self.__Department27

    @Department27.setter
    def Department27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_Department__Department27", None)
        self.__Department27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "manages"):
                opp_val = getattr(old_value, "manages", None)
                if opp_val == self:
                    setattr(old_value, "manages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "manages"):
                opp_val = getattr(value, "manages", None)
                setattr(value, "manages", self)

    @property
    def belongs(self):
        return self.__belongs

    @belongs.setter
    def belongs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_Department__belongs", None)
        self.__belongs = value if value is not None else set()
        
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
    def Department(self):
        return self.__Department

    @Department.setter
    def Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_Department__Department", None)
        self.__Department = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "responsible"):
                opp_val = getattr(old_value, "responsible", None)
                if opp_val == self:
                    setattr(old_value, "responsible", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "responsible"):
                opp_val = getattr(value, "responsible", None)
                setattr(value, "responsible", self)

class course_desc_Evaluation(ABC):

    def __init__(self, Percentage: float, Evaluation: "course_desc_CourseInstance" = None, hasEvaluations: "course_desc_CourseInstance" = None):
        self.Percentage = Percentage
        self.Evaluation = Evaluation
        self.hasEvaluations = hasEvaluations
        
    @property
    def Percentage(self) -> float:
        return self.__Percentage

    @Percentage.setter
    def Percentage(self, Percentage: float):
        self.__Percentage = Percentage

    @property
    def hasEvaluations(self):
        return self.__hasEvaluations

    @hasEvaluations.setter
    def hasEvaluations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_Evaluation__hasEvaluations", None)
        self.__hasEvaluations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CourseInstance14"):
                opp_val = getattr(old_value, "CourseInstance14", None)
                if opp_val == self:
                    setattr(old_value, "CourseInstance14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CourseInstance14"):
                opp_val = getattr(value, "CourseInstance14", None)
                setattr(value, "CourseInstance14", self)

    @property
    def Evaluation(self):
        return self.__Evaluation

    @Evaluation.setter
    def Evaluation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_Evaluation__Evaluation", None)
        self.__Evaluation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "belongsTo"):
                opp_val = getattr(old_value, "belongsTo", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "belongsTo"):
                opp_val = getattr(value, "belongsTo", None)
                if opp_val is None:
                    setattr(value, "belongsTo", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class course_desc_CourseInstance:

    def __init__(self, Year: int, LectureHours: float, LabHours: float, course_desc_CourseInstance: set["course_desc_Timetable"] = None, course_desc_CourseInstance7: set["course_desc_Lecturer"] = None, course_desc_CourseInstance9: set["course_desc_CourseCoordinator"] = None, CourseInstance: "course_desc_Course" = None, hasInstance: "course_desc_Course" = None, belongsTo: set["course_desc_Evaluation"] = None, responsible: "course_desc_Department" = None, CourseInstance11: "course_desc_Department" = None, CourseInstance14: "course_desc_Evaluation" = None, course_desc_CourseInstance37: "course_desc_CourseCoordinator" = None, course_desc_CourseInstance34: "course_desc_Lecturer" = None):
        self.Year = Year
        self.LectureHours = LectureHours
        self.LabHours = LabHours
        self.course_desc_CourseInstance = course_desc_CourseInstance if course_desc_CourseInstance is not None else set()
        self.course_desc_CourseInstance7 = course_desc_CourseInstance7 if course_desc_CourseInstance7 is not None else set()
        self.course_desc_CourseInstance9 = course_desc_CourseInstance9 if course_desc_CourseInstance9 is not None else set()
        self.CourseInstance = CourseInstance
        self.hasInstance = hasInstance
        self.belongsTo = belongsTo if belongsTo is not None else set()
        self.responsible = responsible
        self.CourseInstance11 = CourseInstance11
        self.CourseInstance14 = CourseInstance14
        self.course_desc_CourseInstance37 = course_desc_CourseInstance37
        self.course_desc_CourseInstance34 = course_desc_CourseInstance34
        
    @property
    def LabHours(self) -> float:
        return self.__LabHours

    @LabHours.setter
    def LabHours(self, LabHours: float):
        self.__LabHours = LabHours

    @property
    def Year(self) -> int:
        return self.__Year

    @Year.setter
    def Year(self, Year: int):
        self.__Year = Year

    @property
    def LectureHours(self) -> float:
        return self.__LectureHours

    @LectureHours.setter
    def LectureHours(self, LectureHours: float):
        self.__LectureHours = LectureHours

    @property
    def responsible(self):
        return self.__responsible

    @responsible.setter
    def responsible(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_CourseInstance__responsible", None)
        self.__responsible = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Department"):
                opp_val = getattr(old_value, "Department", None)
                if opp_val == self:
                    setattr(old_value, "Department", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Department"):
                opp_val = getattr(value, "Department", None)
                setattr(value, "Department", self)

    @property
    def course_desc_CourseInstance9(self):
        return self.__course_desc_CourseInstance9

    @course_desc_CourseInstance9.setter
    def course_desc_CourseInstance9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_CourseInstance__course_desc_CourseInstance9", None)
        self.__course_desc_CourseInstance9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "course_desc_CourseCoordinator"):
                    opp_val = getattr(item, "course_desc_CourseCoordinator", None)
                    
                    if opp_val == self:
                        setattr(item, "course_desc_CourseCoordinator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "course_desc_CourseCoordinator"):
                    opp_val = getattr(item, "course_desc_CourseCoordinator", None)
                    
                    setattr(item, "course_desc_CourseCoordinator", self)
                    

    @property
    def CourseInstance(self):
        return self.__CourseInstance

    @CourseInstance.setter
    def CourseInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_CourseInstance__CourseInstance", None)
        self.__CourseInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "instanceOfCourse"):
                opp_val = getattr(old_value, "instanceOfCourse", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "instanceOfCourse"):
                opp_val = getattr(value, "instanceOfCourse", None)
                if opp_val is None:
                    setattr(value, "instanceOfCourse", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def course_desc_CourseInstance(self):
        return self.__course_desc_CourseInstance

    @course_desc_CourseInstance.setter
    def course_desc_CourseInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_CourseInstance__course_desc_CourseInstance", None)
        self.__course_desc_CourseInstance = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "course_desc_Timetable"):
                    opp_val = getattr(item, "course_desc_Timetable", None)
                    
                    if opp_val == self:
                        setattr(item, "course_desc_Timetable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "course_desc_Timetable"):
                    opp_val = getattr(item, "course_desc_Timetable", None)
                    
                    setattr(item, "course_desc_Timetable", self)
                    

    @property
    def course_desc_CourseInstance7(self):
        return self.__course_desc_CourseInstance7

    @course_desc_CourseInstance7.setter
    def course_desc_CourseInstance7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_CourseInstance__course_desc_CourseInstance7", None)
        self.__course_desc_CourseInstance7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "course_desc_Lecturer"):
                    opp_val = getattr(item, "course_desc_Lecturer", None)
                    
                    if opp_val == self:
                        setattr(item, "course_desc_Lecturer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "course_desc_Lecturer"):
                    opp_val = getattr(item, "course_desc_Lecturer", None)
                    
                    setattr(item, "course_desc_Lecturer", self)
                    

    @property
    def belongsTo(self):
        return self.__belongsTo

    @belongsTo.setter
    def belongsTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_CourseInstance__belongsTo", None)
        self.__belongsTo = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Evaluation"):
                    opp_val = getattr(item, "Evaluation", None)
                    
                    if opp_val == self:
                        setattr(item, "Evaluation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Evaluation"):
                    opp_val = getattr(item, "Evaluation", None)
                    
                    setattr(item, "Evaluation", self)
                    

    @property
    def hasInstance(self):
        return self.__hasInstance

    @hasInstance.setter
    def hasInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_CourseInstance__hasInstance", None)
        self.__hasInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Course"):
                opp_val = getattr(old_value, "Course", None)
                if opp_val == self:
                    setattr(old_value, "Course", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Course"):
                opp_val = getattr(value, "Course", None)
                setattr(value, "Course", self)

    @property
    def course_desc_CourseInstance34(self):
        return self.__course_desc_CourseInstance34

    @course_desc_CourseInstance34.setter
    def course_desc_CourseInstance34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_CourseInstance__course_desc_CourseInstance34", None)
        self.__course_desc_CourseInstance34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course_desc_Lecturer33"):
                opp_val = getattr(old_value, "course_desc_Lecturer33", None)
                if opp_val == self:
                    setattr(old_value, "course_desc_Lecturer33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course_desc_Lecturer33"):
                opp_val = getattr(value, "course_desc_Lecturer33", None)
                setattr(value, "course_desc_Lecturer33", self)

    @property
    def course_desc_CourseInstance37(self):
        return self.__course_desc_CourseInstance37

    @course_desc_CourseInstance37.setter
    def course_desc_CourseInstance37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_CourseInstance__course_desc_CourseInstance37", None)
        self.__course_desc_CourseInstance37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course_desc_CourseCoordinator36"):
                opp_val = getattr(old_value, "course_desc_CourseCoordinator36", None)
                if opp_val == self:
                    setattr(old_value, "course_desc_CourseCoordinator36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course_desc_CourseCoordinator36"):
                opp_val = getattr(value, "course_desc_CourseCoordinator36", None)
                setattr(value, "course_desc_CourseCoordinator36", self)

    @property
    def CourseInstance11(self):
        return self.__CourseInstance11

    @CourseInstance11.setter
    def CourseInstance11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_CourseInstance__CourseInstance11", None)
        self.__CourseInstance11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isInstanceOf"):
                opp_val = getattr(old_value, "isInstanceOf", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isInstanceOf"):
                opp_val = getattr(value, "isInstanceOf", None)
                if opp_val is None:
                    setattr(value, "isInstanceOf", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CourseInstance14(self):
        return self.__CourseInstance14

    @CourseInstance14.setter
    def CourseInstance14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_CourseInstance__CourseInstance14", None)
        self.__CourseInstance14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hasEvaluations"):
                opp_val = getattr(old_value, "hasEvaluations", None)
                if opp_val == self:
                    setattr(old_value, "hasEvaluations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hasEvaluations"):
                opp_val = getattr(value, "hasEvaluations", None)
                setattr(value, "hasEvaluations", self)

class course_desc_CourseCoordinator(PersonRole):

    pass
class course_desc_Lecturer(PersonRole):

    pass
class course_desc_Timetable:

    pass
class course_desc_CoursePreconditions:

    def __init__(self, isRecommended: bool, isRequired: bool, reductionPoints: float, course_desc_CoursePreconditions: "course_desc_Course" = None, course_desc_CoursePreconditions21: "course_desc_Course" = None, course_desc_CoursePreconditions46: "course_desc_Univ" = None):
        self.isRecommended = isRecommended
        self.isRequired = isRequired
        self.reductionPoints = reductionPoints
        self.course_desc_CoursePreconditions = course_desc_CoursePreconditions
        self.course_desc_CoursePreconditions21 = course_desc_CoursePreconditions21
        self.course_desc_CoursePreconditions46 = course_desc_CoursePreconditions46
        
    @property
    def isRecommended(self) -> bool:
        return self.__isRecommended

    @isRecommended.setter
    def isRecommended(self, isRecommended: bool):
        self.__isRecommended = isRecommended

    @property
    def isRequired(self) -> bool:
        return self.__isRequired

    @isRequired.setter
    def isRequired(self, isRequired: bool):
        self.__isRequired = isRequired

    @property
    def reductionPoints(self) -> float:
        return self.__reductionPoints

    @reductionPoints.setter
    def reductionPoints(self, reductionPoints: float):
        self.__reductionPoints = reductionPoints

    @property
    def course_desc_CoursePreconditions21(self):
        return self.__course_desc_CoursePreconditions21

    @course_desc_CoursePreconditions21.setter
    def course_desc_CoursePreconditions21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_CoursePreconditions__course_desc_CoursePreconditions21", None)
        self.__course_desc_CoursePreconditions21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course_desc_Course22"):
                opp_val = getattr(old_value, "course_desc_Course22", None)
                if opp_val == self:
                    setattr(old_value, "course_desc_Course22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course_desc_Course22"):
                opp_val = getattr(value, "course_desc_Course22", None)
                setattr(value, "course_desc_Course22", self)

    @property
    def course_desc_CoursePreconditions46(self):
        return self.__course_desc_CoursePreconditions46

    @course_desc_CoursePreconditions46.setter
    def course_desc_CoursePreconditions46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_CoursePreconditions__course_desc_CoursePreconditions46", None)
        self.__course_desc_CoursePreconditions46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course_desc_Univ45"):
                opp_val = getattr(old_value, "course_desc_Univ45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course_desc_Univ45"):
                opp_val = getattr(value, "course_desc_Univ45", None)
                if opp_val is None:
                    setattr(value, "course_desc_Univ45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def course_desc_CoursePreconditions(self):
        return self.__course_desc_CoursePreconditions

    @course_desc_CoursePreconditions.setter
    def course_desc_CoursePreconditions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_CoursePreconditions__course_desc_CoursePreconditions", None)
        self.__course_desc_CoursePreconditions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course_desc_Course"):
                opp_val = getattr(old_value, "course_desc_Course", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course_desc_Course"):
                opp_val = getattr(value, "course_desc_Course", None)
                if opp_val is None:
                    setattr(value, "course_desc_Course", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class course_desc_Course:

    def __init__(self, Code: str, name: str, Content: str, Credits: str, course_desc_Course: set["course_desc_CoursePreconditions"] = None, instanceOfCourse: set["course_desc_CourseInstance"] = None, Course: "course_desc_CourseInstance" = None, course_desc_Course22: "course_desc_CoursePreconditions" = None, course_desc_Course25: "course_desc_StudyProgram" = None, course_desc_Course41: "course_desc_Univ" = None):
        self.Code = Code
        self.name = name
        self.Content = Content
        self.Credits = Credits
        self.course_desc_Course = course_desc_Course if course_desc_Course is not None else set()
        self.instanceOfCourse = instanceOfCourse if instanceOfCourse is not None else set()
        self.Course = Course
        self.course_desc_Course22 = course_desc_Course22
        self.course_desc_Course25 = course_desc_Course25
        self.course_desc_Course41 = course_desc_Course41
        
    @property
    def Content(self) -> str:
        return self.__Content

    @Content.setter
    def Content(self, Content: str):
        self.__Content = Content

    @property
    def Code(self) -> str:
        return self.__Code

    @Code.setter
    def Code(self, Code: str):
        self.__Code = Code

    @property
    def Credits(self) -> str:
        return self.__Credits

    @Credits.setter
    def Credits(self, Credits: str):
        self.__Credits = Credits

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def course_desc_Course22(self):
        return self.__course_desc_Course22

    @course_desc_Course22.setter
    def course_desc_Course22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_Course__course_desc_Course22", None)
        self.__course_desc_Course22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course_desc_CoursePreconditions21"):
                opp_val = getattr(old_value, "course_desc_CoursePreconditions21", None)
                if opp_val == self:
                    setattr(old_value, "course_desc_CoursePreconditions21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course_desc_CoursePreconditions21"):
                opp_val = getattr(value, "course_desc_CoursePreconditions21", None)
                setattr(value, "course_desc_CoursePreconditions21", self)

    @property
    def course_desc_Course41(self):
        return self.__course_desc_Course41

    @course_desc_Course41.setter
    def course_desc_Course41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_Course__course_desc_Course41", None)
        self.__course_desc_Course41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course_desc_Univ40"):
                opp_val = getattr(old_value, "course_desc_Univ40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course_desc_Univ40"):
                opp_val = getattr(value, "course_desc_Univ40", None)
                if opp_val is None:
                    setattr(value, "course_desc_Univ40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Course(self):
        return self.__Course

    @Course.setter
    def Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_Course__Course", None)
        self.__Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hasInstance"):
                opp_val = getattr(old_value, "hasInstance", None)
                if opp_val == self:
                    setattr(old_value, "hasInstance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hasInstance"):
                opp_val = getattr(value, "hasInstance", None)
                setattr(value, "hasInstance", self)

    @property
    def course_desc_Course(self):
        return self.__course_desc_Course

    @course_desc_Course.setter
    def course_desc_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_Course__course_desc_Course", None)
        self.__course_desc_Course = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "course_desc_CoursePreconditions"):
                    opp_val = getattr(item, "course_desc_CoursePreconditions", None)
                    
                    if opp_val == self:
                        setattr(item, "course_desc_CoursePreconditions", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "course_desc_CoursePreconditions"):
                    opp_val = getattr(item, "course_desc_CoursePreconditions", None)
                    
                    setattr(item, "course_desc_CoursePreconditions", self)
                    

    @property
    def course_desc_Course25(self):
        return self.__course_desc_Course25

    @course_desc_Course25.setter
    def course_desc_Course25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_Course__course_desc_Course25", None)
        self.__course_desc_Course25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course_desc_StudyProgram24"):
                opp_val = getattr(old_value, "course_desc_StudyProgram24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course_desc_StudyProgram24"):
                opp_val = getattr(value, "course_desc_StudyProgram24", None)
                if opp_val is None:
                    setattr(value, "course_desc_StudyProgram24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def instanceOfCourse(self):
        return self.__instanceOfCourse

    @instanceOfCourse.setter
    def instanceOfCourse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_desc_Course__instanceOfCourse", None)
        self.__instanceOfCourse = value if value is not None else set()
        
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
                    
