from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class EvaluationType(Enum):
    Exam = "Exam"
    Project = "Project"
    Assignment = "Assignment"
class CourseWorkType(Enum):
    InDepth = "InDepth"
    Lecture = "Lecture"
    Exercise = "Exercise"
class RoleType(Enum):
    Lecturer = "Lecturer"
    Student = "Student"
    Supervisor = "Supervisor"
class StudyProgramType(Enum):
    MTDT = "MTDT"
    MTMART = "MTMART"


############################################
# Definition of Classes
############################################

class oving4_Assignment:

    def __init__(self, deadline: str, Assignment: "oving4_EvaluationElement" = None, containsAssignment: "oving4_EvaluationElement" = None):
        self.deadline = deadline
        self.Assignment = Assignment
        self.containsAssignment = containsAssignment
        
    @property
    def deadline(self) -> str:
        return self.__deadline

    @deadline.setter
    def deadline(self, deadline: str):
        self.__deadline = deadline

    @property
    def containsAssignment(self):
        return self.__containsAssignment

    @containsAssignment.setter
    def containsAssignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_Assignment__containsAssignment", None)
        self.__containsAssignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EvaluationElement62"):
                opp_val = getattr(old_value, "EvaluationElement62", None)
                if opp_val == self:
                    setattr(old_value, "EvaluationElement62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EvaluationElement62"):
                opp_val = getattr(value, "EvaluationElement62", None)
                setattr(value, "EvaluationElement62", self)

    @property
    def Assignment(self):
        return self.__Assignment

    @Assignment.setter
    def Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_Assignment__Assignment", None)
        self.__Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "belongToEvEl"):
                opp_val = getattr(old_value, "belongToEvEl", None)
                if opp_val == self:
                    setattr(old_value, "belongToEvEl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "belongToEvEl"):
                opp_val = getattr(value, "belongToEvEl", None)
                setattr(value, "belongToEvEl", self)

class oving4_Exam:

    def __init__(self, endDate: str, previousStartDate: str, previousEndDate: str, startDate: str, Exam: "oving4_EvaluationElement" = None, containsExam: "oving4_EvaluationElement" = None):
        self.endDate = endDate
        self.previousStartDate = previousStartDate
        self.previousEndDate = previousEndDate
        self.startDate = startDate
        self.Exam = Exam
        self.containsExam = containsExam
        
    @property
    def endDate(self) -> str:
        return self.__endDate

    @endDate.setter
    def endDate(self, endDate: str):
        self.__endDate = endDate

    @property
    def startDate(self) -> str:
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: str):
        self.__startDate = startDate

    @property
    def previousEndDate(self) -> str:
        return self.__previousEndDate

    @previousEndDate.setter
    def previousEndDate(self, previousEndDate: str):
        self.__previousEndDate = previousEndDate

    @property
    def previousStartDate(self) -> str:
        return self.__previousStartDate

    @previousStartDate.setter
    def previousStartDate(self, previousStartDate: str):
        self.__previousStartDate = previousStartDate

    @property
    def Exam(self):
        return self.__Exam

    @Exam.setter
    def Exam(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_Exam__Exam", None)
        self.__Exam = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "belongsToEvaluationElement"):
                opp_val = getattr(old_value, "belongsToEvaluationElement", None)
                if opp_val == self:
                    setattr(old_value, "belongsToEvaluationElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "belongsToEvaluationElement"):
                opp_val = getattr(value, "belongsToEvaluationElement", None)
                setattr(value, "belongsToEvaluationElement", self)

    @property
    def containsExam(self):
        return self.__containsExam

    @containsExam.setter
    def containsExam(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_Exam__containsExam", None)
        self.__containsExam = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EvaluationElement"):
                opp_val = getattr(old_value, "EvaluationElement", None)
                if opp_val == self:
                    setattr(old_value, "EvaluationElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EvaluationElement"):
                opp_val = getattr(value, "EvaluationElement", None)
                setattr(value, "EvaluationElement", self)

class oving4_CourseWork:

    def __init__(self, isMandatory: bool, type: str, name: str, oving4_CourseWork: "oving4_CourseInstance" = None, oving4_CourseWork52: "oving4_TimeTableElement" = None):
        self.isMandatory = isMandatory
        self.type = type
        self.name = name
        self.oving4_CourseWork = oving4_CourseWork
        self.oving4_CourseWork52 = oving4_CourseWork52
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def isMandatory(self) -> bool:
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: bool):
        self.__isMandatory = isMandatory

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def oving4_CourseWork52(self):
        return self.__oving4_CourseWork52

    @oving4_CourseWork52.setter
    def oving4_CourseWork52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_CourseWork__oving4_CourseWork52", None)
        self.__oving4_CourseWork52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oving4_TimeTableElement51"):
                opp_val = getattr(old_value, "oving4_TimeTableElement51", None)
                if opp_val == self:
                    setattr(old_value, "oving4_TimeTableElement51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oving4_TimeTableElement51"):
                opp_val = getattr(value, "oving4_TimeTableElement51", None)
                setattr(value, "oving4_TimeTableElement51", self)

    @property
    def oving4_CourseWork(self):
        return self.__oving4_CourseWork

    @oving4_CourseWork.setter
    def oving4_CourseWork(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_CourseWork__oving4_CourseWork", None)
        self.__oving4_CourseWork = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oving4_CourseInstance"):
                opp_val = getattr(old_value, "oving4_CourseInstance", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oving4_CourseInstance"):
                opp_val = getattr(value, "oving4_CourseInstance", None)
                if opp_val is None:
                    setattr(value, "oving4_CourseInstance", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class oving4_EvaluationElement:

    def __init__(self, percentageResult: float, weight: float, type: str, attended: bool, oving4_EvaluationElement: "oving4_Evaluation" = None, belongsToEvaluationElement: "oving4_Exam" = None, belongsToEvaluationel: "oving4_Project" = None, belongToEvEl: "oving4_Assignment" = None, EvaluationElement: "oving4_Exam" = None, EvaluationElement58: "oving4_Project" = None, EvaluationElement62: "oving4_Assignment" = None):
        self.percentageResult = percentageResult
        self.weight = weight
        self.type = type
        self.attended = attended
        self.oving4_EvaluationElement = oving4_EvaluationElement
        self.belongsToEvaluationElement = belongsToEvaluationElement
        self.belongsToEvaluationel = belongsToEvaluationel
        self.belongToEvEl = belongToEvEl
        self.EvaluationElement = EvaluationElement
        self.EvaluationElement58 = EvaluationElement58
        self.EvaluationElement62 = EvaluationElement62
        
    @property
    def attended(self) -> bool:
        return self.__attended

    @attended.setter
    def attended(self, attended: bool):
        self.__attended = attended

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def percentageResult(self) -> float:
        return self.__percentageResult

    @percentageResult.setter
    def percentageResult(self, percentageResult: float):
        self.__percentageResult = percentageResult

    @property
    def weight(self) -> float:
        return self.__weight

    @weight.setter
    def weight(self, weight: float):
        self.__weight = weight

    @property
    def belongToEvEl(self):
        return self.__belongToEvEl

    @belongToEvEl.setter
    def belongToEvEl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_EvaluationElement__belongToEvEl", None)
        self.__belongToEvEl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Assignment"):
                opp_val = getattr(old_value, "Assignment", None)
                if opp_val == self:
                    setattr(old_value, "Assignment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Assignment"):
                opp_val = getattr(value, "Assignment", None)
                setattr(value, "Assignment", self)

    @property
    def EvaluationElement58(self):
        return self.__EvaluationElement58

    @EvaluationElement58.setter
    def EvaluationElement58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_EvaluationElement__EvaluationElement58", None)
        self.__EvaluationElement58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containsProject"):
                opp_val = getattr(old_value, "containsProject", None)
                if opp_val == self:
                    setattr(old_value, "containsProject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containsProject"):
                opp_val = getattr(value, "containsProject", None)
                setattr(value, "containsProject", self)

    @property
    def belongsToEvaluationElement(self):
        return self.__belongsToEvaluationElement

    @belongsToEvaluationElement.setter
    def belongsToEvaluationElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_EvaluationElement__belongsToEvaluationElement", None)
        self.__belongsToEvaluationElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Exam"):
                opp_val = getattr(old_value, "Exam", None)
                if opp_val == self:
                    setattr(old_value, "Exam", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Exam"):
                opp_val = getattr(value, "Exam", None)
                setattr(value, "Exam", self)

    @property
    def EvaluationElement(self):
        return self.__EvaluationElement

    @EvaluationElement.setter
    def EvaluationElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_EvaluationElement__EvaluationElement", None)
        self.__EvaluationElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containsExam"):
                opp_val = getattr(old_value, "containsExam", None)
                if opp_val == self:
                    setattr(old_value, "containsExam", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containsExam"):
                opp_val = getattr(value, "containsExam", None)
                setattr(value, "containsExam", self)

    @property
    def belongsToEvaluationel(self):
        return self.__belongsToEvaluationel

    @belongsToEvaluationel.setter
    def belongsToEvaluationel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_EvaluationElement__belongsToEvaluationel", None)
        self.__belongsToEvaluationel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Project"):
                opp_val = getattr(old_value, "Project", None)
                if opp_val == self:
                    setattr(old_value, "Project", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Project"):
                opp_val = getattr(value, "Project", None)
                setattr(value, "Project", self)

    @property
    def oving4_EvaluationElement(self):
        return self.__oving4_EvaluationElement

    @oving4_EvaluationElement.setter
    def oving4_EvaluationElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_EvaluationElement__oving4_EvaluationElement", None)
        self.__oving4_EvaluationElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oving4_Evaluation"):
                opp_val = getattr(old_value, "oving4_Evaluation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oving4_Evaluation"):
                opp_val = getattr(value, "oving4_Evaluation", None)
                if opp_val is None:
                    setattr(value, "oving4_Evaluation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def EvaluationElement62(self):
        return self.__EvaluationElement62

    @EvaluationElement62.setter
    def EvaluationElement62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_EvaluationElement__EvaluationElement62", None)
        self.__EvaluationElement62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containsAssignment"):
                opp_val = getattr(old_value, "containsAssignment", None)
                if opp_val == self:
                    setattr(old_value, "containsAssignment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containsAssignment"):
                opp_val = getattr(value, "containsAssignment", None)
                setattr(value, "containsAssignment", self)

class oving4_TimeTableElement:

    def __init__(self, date: str, room: str, durationInMinutes: int, oving4_TimeTableElement: "oving4_TimeTable" = None, oving4_TimeTableElement51: "oving4_CourseWork" = None):
        self.date = date
        self.room = room
        self.durationInMinutes = durationInMinutes
        self.oving4_TimeTableElement = oving4_TimeTableElement
        self.oving4_TimeTableElement51 = oving4_TimeTableElement51
        
    @property
    def date(self) -> str:
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def room(self) -> str:
        return self.__room

    @room.setter
    def room(self, room: str):
        self.__room = room

    @property
    def durationInMinutes(self) -> int:
        return self.__durationInMinutes

    @durationInMinutes.setter
    def durationInMinutes(self, durationInMinutes: int):
        self.__durationInMinutes = durationInMinutes

    @property
    def oving4_TimeTableElement51(self):
        return self.__oving4_TimeTableElement51

    @oving4_TimeTableElement51.setter
    def oving4_TimeTableElement51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_TimeTableElement__oving4_TimeTableElement51", None)
        self.__oving4_TimeTableElement51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oving4_CourseWork52"):
                opp_val = getattr(old_value, "oving4_CourseWork52", None)
                if opp_val == self:
                    setattr(old_value, "oving4_CourseWork52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oving4_CourseWork52"):
                opp_val = getattr(value, "oving4_CourseWork52", None)
                setattr(value, "oving4_CourseWork52", self)

    @property
    def oving4_TimeTableElement(self):
        return self.__oving4_TimeTableElement

    @oving4_TimeTableElement.setter
    def oving4_TimeTableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_TimeTableElement__oving4_TimeTableElement", None)
        self.__oving4_TimeTableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oving4_TimeTable"):
                opp_val = getattr(old_value, "oving4_TimeTable", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oving4_TimeTable"):
                opp_val = getattr(value, "oving4_TimeTable", None)
                if opp_val is None:
                    setattr(value, "oving4_TimeTable", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class oving4_TimeTable:

    def __init__(self, isRestrictedToProgramsInParallell: bool, TimeTable: "oving4_CourseInstance" = None, oving4_TimeTable: set["oving4_TimeTableElement"] = None, oving4_TimeTable38: "oving4_StudyProgram" = None, hasTimeTable: "oving4_CourseInstance" = None):
        self.isRestrictedToProgramsInParallell = isRestrictedToProgramsInParallell
        self.TimeTable = TimeTable
        self.oving4_TimeTable = oving4_TimeTable if oving4_TimeTable is not None else set()
        self.oving4_TimeTable38 = oving4_TimeTable38
        self.hasTimeTable = hasTimeTable
        
    @property
    def isRestrictedToProgramsInParallell(self) -> bool:
        return self.__isRestrictedToProgramsInParallell

    @isRestrictedToProgramsInParallell.setter
    def isRestrictedToProgramsInParallell(self, isRestrictedToProgramsInParallell: bool):
        self.__isRestrictedToProgramsInParallell = isRestrictedToProgramsInParallell

    @property
    def TimeTable(self):
        return self.__TimeTable

    @TimeTable.setter
    def TimeTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_TimeTable__TimeTable", None)
        self.__TimeTable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedByCourseInstance"):
                opp_val = getattr(old_value, "ownedByCourseInstance", None)
                if opp_val == self:
                    setattr(old_value, "ownedByCourseInstance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedByCourseInstance"):
                opp_val = getattr(value, "ownedByCourseInstance", None)
                setattr(value, "ownedByCourseInstance", self)

    @property
    def oving4_TimeTable38(self):
        return self.__oving4_TimeTable38

    @oving4_TimeTable38.setter
    def oving4_TimeTable38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_TimeTable__oving4_TimeTable38", None)
        self.__oving4_TimeTable38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oving4_StudyProgram39"):
                opp_val = getattr(old_value, "oving4_StudyProgram39", None)
                if opp_val == self:
                    setattr(old_value, "oving4_StudyProgram39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oving4_StudyProgram39"):
                opp_val = getattr(value, "oving4_StudyProgram39", None)
                setattr(value, "oving4_StudyProgram39", self)

    @property
    def oving4_TimeTable(self):
        return self.__oving4_TimeTable

    @oving4_TimeTable.setter
    def oving4_TimeTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_TimeTable__oving4_TimeTable", None)
        self.__oving4_TimeTable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oving4_TimeTableElement"):
                    opp_val = getattr(item, "oving4_TimeTableElement", None)
                    
                    if opp_val == self:
                        setattr(item, "oving4_TimeTableElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oving4_TimeTableElement"):
                    opp_val = getattr(item, "oving4_TimeTableElement", None)
                    
                    setattr(item, "oving4_TimeTableElement", self)
                    

    @property
    def hasTimeTable(self):
        return self.__hasTimeTable

    @hasTimeTable.setter
    def hasTimeTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_TimeTable__hasTimeTable", None)
        self.__hasTimeTable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CourseInstance41"):
                opp_val = getattr(old_value, "CourseInstance41", None)
                if opp_val == self:
                    setattr(old_value, "CourseInstance41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CourseInstance41"):
                opp_val = getattr(value, "CourseInstance41", None)
                setattr(value, "CourseInstance41", self)

class oving4_Precondition:

    def __init__(self, isMandatory: bool, creditReduction: float, oving4_Precondition: "oving4_Course" = None, oving4_Precondition48: "oving4_Course" = None):
        self.isMandatory = isMandatory
        self.creditReduction = creditReduction
        self.oving4_Precondition = oving4_Precondition
        self.oving4_Precondition48 = oving4_Precondition48
        
    @property
    def creditReduction(self) -> float:
        return self.__creditReduction

    @creditReduction.setter
    def creditReduction(self, creditReduction: float):
        self.__creditReduction = creditReduction

    @property
    def isMandatory(self) -> bool:
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: bool):
        self.__isMandatory = isMandatory

    @property
    def oving4_Precondition48(self):
        return self.__oving4_Precondition48

    @oving4_Precondition48.setter
    def oving4_Precondition48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_Precondition__oving4_Precondition48", None)
        self.__oving4_Precondition48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oving4_Course49"):
                opp_val = getattr(old_value, "oving4_Course49", None)
                if opp_val == self:
                    setattr(old_value, "oving4_Course49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oving4_Course49"):
                opp_val = getattr(value, "oving4_Course49", None)
                setattr(value, "oving4_Course49", self)

    @property
    def oving4_Precondition(self):
        return self.__oving4_Precondition

    @oving4_Precondition.setter
    def oving4_Precondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_Precondition__oving4_Precondition", None)
        self.__oving4_Precondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oving4_Course19"):
                opp_val = getattr(old_value, "oving4_Course19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oving4_Course19"):
                opp_val = getattr(value, "oving4_Course19", None)
                if opp_val is None:
                    setattr(value, "oving4_Course19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class oving4_CourseInstance:

    def __init__(self, sumLectureHours: int, sumInDepthHours: int, sumExerciseHours: int, CourseInstance: "oving4_Course" = None, ownedByCourseInstance: "oving4_TimeTable" = None, memberOfCourse: set["oving4_PersonRole"] = None, courseInstance27: set["oving4_Evaluation"] = None, CourseInstance33: "oving4_PersonRole" = None, CourseInstance41: "oving4_TimeTable" = None, courseInstance: "oving4_Course" = None, oving4_CourseInstance: set["oving4_CourseWork"] = None, CourseInstance46: "oving4_Evaluation" = None):
        self.sumLectureHours = sumLectureHours
        self.sumInDepthHours = sumInDepthHours
        self.sumExerciseHours = sumExerciseHours
        self.CourseInstance = CourseInstance
        self.ownedByCourseInstance = ownedByCourseInstance
        self.memberOfCourse = memberOfCourse if memberOfCourse is not None else set()
        self.courseInstance27 = courseInstance27 if courseInstance27 is not None else set()
        self.CourseInstance33 = CourseInstance33
        self.CourseInstance41 = CourseInstance41
        self.courseInstance = courseInstance
        self.oving4_CourseInstance = oving4_CourseInstance if oving4_CourseInstance is not None else set()
        self.CourseInstance46 = CourseInstance46
        
    @property
    def sumExerciseHours(self) -> int:
        return self.__sumExerciseHours

    @sumExerciseHours.setter
    def sumExerciseHours(self, sumExerciseHours: int):
        self.__sumExerciseHours = sumExerciseHours

    @property
    def sumInDepthHours(self) -> int:
        return self.__sumInDepthHours

    @sumInDepthHours.setter
    def sumInDepthHours(self, sumInDepthHours: int):
        self.__sumInDepthHours = sumInDepthHours

    @property
    def sumLectureHours(self) -> int:
        return self.__sumLectureHours

    @sumLectureHours.setter
    def sumLectureHours(self, sumLectureHours: int):
        self.__sumLectureHours = sumLectureHours

    @property
    def memberOfCourse(self):
        return self.__memberOfCourse

    @memberOfCourse.setter
    def memberOfCourse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_CourseInstance__memberOfCourse", None)
        self.__memberOfCourse = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PersonRole25"):
                    opp_val = getattr(item, "PersonRole25", None)
                    
                    if opp_val == self:
                        setattr(item, "PersonRole25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PersonRole25"):
                    opp_val = getattr(item, "PersonRole25", None)
                    
                    setattr(item, "PersonRole25", self)
                    

    @property
    def ownedByCourseInstance(self):
        return self.__ownedByCourseInstance

    @ownedByCourseInstance.setter
    def ownedByCourseInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_CourseInstance__ownedByCourseInstance", None)
        self.__ownedByCourseInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TimeTable"):
                opp_val = getattr(old_value, "TimeTable", None)
                if opp_val == self:
                    setattr(old_value, "TimeTable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TimeTable"):
                opp_val = getattr(value, "TimeTable", None)
                setattr(value, "TimeTable", self)

    @property
    def CourseInstance41(self):
        return self.__CourseInstance41

    @CourseInstance41.setter
    def CourseInstance41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_CourseInstance__CourseInstance41", None)
        self.__CourseInstance41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hasTimeTable"):
                opp_val = getattr(old_value, "hasTimeTable", None)
                if opp_val == self:
                    setattr(old_value, "hasTimeTable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hasTimeTable"):
                opp_val = getattr(value, "hasTimeTable", None)
                setattr(value, "hasTimeTable", self)

    @property
    def CourseInstance(self):
        return self.__CourseInstance

    @CourseInstance.setter
    def CourseInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_CourseInstance__CourseInstance", None)
        self.__CourseInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedBy"):
                opp_val = getattr(old_value, "ownedBy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedBy"):
                opp_val = getattr(value, "ownedBy", None)
                if opp_val is None:
                    setattr(value, "ownedBy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def courseInstance27(self):
        return self.__courseInstance27

    @courseInstance27.setter
    def courseInstance27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_CourseInstance__courseInstance27", None)
        self.__courseInstance27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Evaluation28"):
                    opp_val = getattr(item, "Evaluation28", None)
                    
                    if opp_val == self:
                        setattr(item, "Evaluation28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Evaluation28"):
                    opp_val = getattr(item, "Evaluation28", None)
                    
                    setattr(item, "Evaluation28", self)
                    

    @property
    def courseInstance(self):
        return self.__courseInstance

    @courseInstance.setter
    def courseInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_CourseInstance__courseInstance", None)
        self.__courseInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Course22"):
                opp_val = getattr(old_value, "Course22", None)
                if opp_val == self:
                    setattr(old_value, "Course22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Course22"):
                opp_val = getattr(value, "Course22", None)
                setattr(value, "Course22", self)

    @property
    def oving4_CourseInstance(self):
        return self.__oving4_CourseInstance

    @oving4_CourseInstance.setter
    def oving4_CourseInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_CourseInstance__oving4_CourseInstance", None)
        self.__oving4_CourseInstance = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oving4_CourseWork"):
                    opp_val = getattr(item, "oving4_CourseWork", None)
                    
                    if opp_val == self:
                        setattr(item, "oving4_CourseWork", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oving4_CourseWork"):
                    opp_val = getattr(item, "oving4_CourseWork", None)
                    
                    setattr(item, "oving4_CourseWork", self)
                    

    @property
    def CourseInstance33(self):
        return self.__CourseInstance33

    @CourseInstance33.setter
    def CourseInstance33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_CourseInstance__CourseInstance33", None)
        self.__CourseInstance33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hasMember"):
                opp_val = getattr(old_value, "hasMember", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hasMember"):
                opp_val = getattr(value, "hasMember", None)
                if opp_val is None:
                    setattr(value, "hasMember", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CourseInstance46(self):
        return self.__CourseInstance46

    @CourseInstance46.setter
    def CourseInstance46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_CourseInstance__CourseInstance46", None)
        self.__CourseInstance46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containsEvaluation"):
                opp_val = getattr(old_value, "containsEvaluation", None)
                if opp_val == self:
                    setattr(old_value, "containsEvaluation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containsEvaluation"):
                opp_val = getattr(value, "containsEvaluation", None)
                setattr(value, "containsEvaluation", self)

class oving4_Evaluation:

    def __init__(self, creditsReceived: float, description: str, totalPercentageResult: float, completed: bool, Evaluation: "oving4_Person" = None, Evaluation28: "oving4_CourseInstance" = None, hasEvaluation: "oving4_Person" = None, oving4_Evaluation: set["oving4_EvaluationElement"] = None, containsEvaluation: "oving4_CourseInstance" = None):
        self.creditsReceived = creditsReceived
        self.description = description
        self.totalPercentageResult = totalPercentageResult
        self.completed = completed
        self.Evaluation = Evaluation
        self.Evaluation28 = Evaluation28
        self.hasEvaluation = hasEvaluation
        self.oving4_Evaluation = oving4_Evaluation if oving4_Evaluation is not None else set()
        self.containsEvaluation = containsEvaluation
        
    @property
    def totalPercentageResult(self) -> float:
        return self.__totalPercentageResult

    @totalPercentageResult.setter
    def totalPercentageResult(self, totalPercentageResult: float):
        self.__totalPercentageResult = totalPercentageResult

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def creditsReceived(self) -> float:
        return self.__creditsReceived

    @creditsReceived.setter
    def creditsReceived(self, creditsReceived: float):
        self.__creditsReceived = creditsReceived

    @property
    def completed(self) -> bool:
        return self.__completed

    @completed.setter
    def completed(self, completed: bool):
        self.__completed = completed

    @property
    def Evaluation(self):
        return self.__Evaluation

    @Evaluation.setter
    def Evaluation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_Evaluation__Evaluation", None)
        self.__Evaluation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "personEvaluated"):
                opp_val = getattr(old_value, "personEvaluated", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "personEvaluated"):
                opp_val = getattr(value, "personEvaluated", None)
                if opp_val is None:
                    setattr(value, "personEvaluated", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Evaluation28(self):
        return self.__Evaluation28

    @Evaluation28.setter
    def Evaluation28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_Evaluation__Evaluation28", None)
        self.__Evaluation28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courseInstance27"):
                opp_val = getattr(old_value, "courseInstance27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courseInstance27"):
                opp_val = getattr(value, "courseInstance27", None)
                if opp_val is None:
                    setattr(value, "courseInstance27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def containsEvaluation(self):
        return self.__containsEvaluation

    @containsEvaluation.setter
    def containsEvaluation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_Evaluation__containsEvaluation", None)
        self.__containsEvaluation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CourseInstance46"):
                opp_val = getattr(old_value, "CourseInstance46", None)
                if opp_val == self:
                    setattr(old_value, "CourseInstance46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CourseInstance46"):
                opp_val = getattr(value, "CourseInstance46", None)
                setattr(value, "CourseInstance46", self)

    @property
    def oving4_Evaluation(self):
        return self.__oving4_Evaluation

    @oving4_Evaluation.setter
    def oving4_Evaluation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_Evaluation__oving4_Evaluation", None)
        self.__oving4_Evaluation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oving4_EvaluationElement"):
                    opp_val = getattr(item, "oving4_EvaluationElement", None)
                    
                    if opp_val == self:
                        setattr(item, "oving4_EvaluationElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oving4_EvaluationElement"):
                    opp_val = getattr(item, "oving4_EvaluationElement", None)
                    
                    setattr(item, "oving4_EvaluationElement", self)
                    

    @property
    def hasEvaluation(self):
        return self.__hasEvaluation

    @hasEvaluation.setter
    def hasEvaluation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_Evaluation__hasEvaluation", None)
        self.__hasEvaluation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Person43"):
                opp_val = getattr(old_value, "Person43", None)
                if opp_val == self:
                    setattr(old_value, "Person43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Person43"):
                opp_val = getattr(value, "Person43", None)
                setattr(value, "Person43", self)

class oving4_PersonRole:

    def __init__(self, type: str, PersonRole: "oving4_Department" = None, PersonRole12: "oving4_StudyProgram" = None, PersonRole14: "oving4_Person" = None, PersonRole25: "oving4_CourseInstance" = None, hasRole: "oving4_Person" = None, hasEmployee: "oving4_StudyProgram" = None, hasMember: set["oving4_CourseInstance"] = None, hasEmployee35: "oving4_Department" = None, oving4_PersonRole: "oving4_Project" = None):
        self.type = type
        self.PersonRole = PersonRole
        self.PersonRole12 = PersonRole12
        self.PersonRole14 = PersonRole14
        self.PersonRole25 = PersonRole25
        self.hasRole = hasRole
        self.hasEmployee = hasEmployee
        self.hasMember = hasMember if hasMember is not None else set()
        self.hasEmployee35 = hasEmployee35
        self.oving4_PersonRole = oving4_PersonRole
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def PersonRole(self):
        return self.__PersonRole

    @PersonRole.setter
    def PersonRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_PersonRole__PersonRole", None)
        self.__PersonRole = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employedByDepartment"):
                opp_val = getattr(old_value, "employedByDepartment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employedByDepartment"):
                opp_val = getattr(value, "employedByDepartment", None)
                if opp_val is None:
                    setattr(value, "employedByDepartment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PersonRole25(self):
        return self.__PersonRole25

    @PersonRole25.setter
    def PersonRole25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_PersonRole__PersonRole25", None)
        self.__PersonRole25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "memberOfCourse"):
                opp_val = getattr(old_value, "memberOfCourse", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "memberOfCourse"):
                opp_val = getattr(value, "memberOfCourse", None)
                if opp_val is None:
                    setattr(value, "memberOfCourse", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hasMember(self):
        return self.__hasMember

    @hasMember.setter
    def hasMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_PersonRole__hasMember", None)
        self.__hasMember = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CourseInstance33"):
                    opp_val = getattr(item, "CourseInstance33", None)
                    
                    if opp_val == self:
                        setattr(item, "CourseInstance33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CourseInstance33"):
                    opp_val = getattr(item, "CourseInstance33", None)
                    
                    setattr(item, "CourseInstance33", self)
                    

    @property
    def hasRole(self):
        return self.__hasRole

    @hasRole.setter
    def hasRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_PersonRole__hasRole", None)
        self.__hasRole = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Person"):
                opp_val = getattr(old_value, "Person", None)
                if opp_val == self:
                    setattr(old_value, "Person", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Person"):
                opp_val = getattr(value, "Person", None)
                setattr(value, "Person", self)

    @property
    def PersonRole14(self):
        return self.__PersonRole14

    @PersonRole14.setter
    def PersonRole14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_PersonRole__PersonRole14", None)
        self.__PersonRole14 = value
        
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

    @property
    def PersonRole12(self):
        return self.__PersonRole12

    @PersonRole12.setter
    def PersonRole12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_PersonRole__PersonRole12", None)
        self.__PersonRole12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employedOfStudyProgram"):
                opp_val = getattr(old_value, "employedOfStudyProgram", None)
                if opp_val == self:
                    setattr(old_value, "employedOfStudyProgram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employedOfStudyProgram"):
                opp_val = getattr(value, "employedOfStudyProgram", None)
                setattr(value, "employedOfStudyProgram", self)

    @property
    def oving4_PersonRole(self):
        return self.__oving4_PersonRole

    @oving4_PersonRole.setter
    def oving4_PersonRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_PersonRole__oving4_PersonRole", None)
        self.__oving4_PersonRole = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oving4_Project60"):
                opp_val = getattr(old_value, "oving4_Project60", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oving4_Project60"):
                opp_val = getattr(value, "oving4_Project60", None)
                if opp_val is None:
                    setattr(value, "oving4_Project60", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hasEmployee(self):
        return self.__hasEmployee

    @hasEmployee.setter
    def hasEmployee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_PersonRole__hasEmployee", None)
        self.__hasEmployee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyProgram31"):
                opp_val = getattr(old_value, "StudyProgram31", None)
                if opp_val == self:
                    setattr(old_value, "StudyProgram31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyProgram31"):
                opp_val = getattr(value, "StudyProgram31", None)
                setattr(value, "StudyProgram31", self)

    @property
    def hasEmployee35(self):
        return self.__hasEmployee35

    @hasEmployee35.setter
    def hasEmployee35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_PersonRole__hasEmployee35", None)
        self.__hasEmployee35 = value
        
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

class oving4_Course:

    def __init__(self, name: str, code: str, credits: float, content: str, examStartDate: str, examEndDate: str, oving4_Course: "oving4_Department" = None, Course: "oving4_StudyProgram" = None, ownedBy: set["oving4_CourseInstance"] = None, containsCourse: "oving4_StudyProgram" = None, oving4_Course19: set["oving4_Precondition"] = None, Course22: "oving4_CourseInstance" = None, oving4_Course49: "oving4_Precondition" = None):
        self.name = name
        self.code = code
        self.credits = credits
        self.content = content
        self.examStartDate = examStartDate
        self.examEndDate = examEndDate
        self.oving4_Course = oving4_Course
        self.Course = Course
        self.ownedBy = ownedBy if ownedBy is not None else set()
        self.containsCourse = containsCourse
        self.oving4_Course19 = oving4_Course19 if oving4_Course19 is not None else set()
        self.Course22 = Course22
        self.oving4_Course49 = oving4_Course49
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def credits(self) -> float:
        return self.__credits

    @credits.setter
    def credits(self, credits: float):
        self.__credits = credits

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def examStartDate(self) -> str:
        return self.__examStartDate

    @examStartDate.setter
    def examStartDate(self, examStartDate: str):
        self.__examStartDate = examStartDate

    @property
    def examEndDate(self) -> str:
        return self.__examEndDate

    @examEndDate.setter
    def examEndDate(self, examEndDate: str):
        self.__examEndDate = examEndDate

    @property
    def Course22(self):
        return self.__Course22

    @Course22.setter
    def Course22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_Course__Course22", None)
        self.__Course22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courseInstance"):
                opp_val = getattr(old_value, "courseInstance", None)
                if opp_val == self:
                    setattr(old_value, "courseInstance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courseInstance"):
                opp_val = getattr(value, "courseInstance", None)
                setattr(value, "courseInstance", self)

    @property
    def oving4_Course(self):
        return self.__oving4_Course

    @oving4_Course.setter
    def oving4_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_Course__oving4_Course", None)
        self.__oving4_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oving4_Department8"):
                opp_val = getattr(old_value, "oving4_Department8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oving4_Department8"):
                opp_val = getattr(value, "oving4_Department8", None)
                if opp_val is None:
                    setattr(value, "oving4_Department8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def oving4_Course49(self):
        return self.__oving4_Course49

    @oving4_Course49.setter
    def oving4_Course49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_Course__oving4_Course49", None)
        self.__oving4_Course49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oving4_Precondition48"):
                opp_val = getattr(old_value, "oving4_Precondition48", None)
                if opp_val == self:
                    setattr(old_value, "oving4_Precondition48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oving4_Precondition48"):
                opp_val = getattr(value, "oving4_Precondition48", None)
                setattr(value, "oving4_Precondition48", self)

    @property
    def ownedBy(self):
        return self.__ownedBy

    @ownedBy.setter
    def ownedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_Course__ownedBy", None)
        self.__ownedBy = value if value is not None else set()
        
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
    def Course(self):
        return self.__Course

    @Course.setter
    def Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_Course__Course", None)
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
    def containsCourse(self):
        return self.__containsCourse

    @containsCourse.setter
    def containsCourse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_Course__containsCourse", None)
        self.__containsCourse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyProgram"):
                opp_val = getattr(old_value, "StudyProgram", None)
                if opp_val == self:
                    setattr(old_value, "StudyProgram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyProgram"):
                opp_val = getattr(value, "StudyProgram", None)
                setattr(value, "StudyProgram", self)

    @property
    def oving4_Course19(self):
        return self.__oving4_Course19

    @oving4_Course19.setter
    def oving4_Course19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_Course__oving4_Course19", None)
        self.__oving4_Course19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oving4_Precondition"):
                    opp_val = getattr(item, "oving4_Precondition", None)
                    
                    if opp_val == self:
                        setattr(item, "oving4_Precondition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oving4_Precondition"):
                    opp_val = getattr(item, "oving4_Precondition", None)
                    
                    setattr(item, "oving4_Precondition", self)
                    

class oving4_Project:

    def __init__(self, deadline: str, oving4_Project: "oving4_Root" = None, Project: "oving4_EvaluationElement" = None, containsProject: "oving4_EvaluationElement" = None, oving4_Project60: set["oving4_PersonRole"] = None):
        self.deadline = deadline
        self.oving4_Project = oving4_Project
        self.Project = Project
        self.containsProject = containsProject
        self.oving4_Project60 = oving4_Project60 if oving4_Project60 is not None else set()
        
    @property
    def deadline(self) -> str:
        return self.__deadline

    @deadline.setter
    def deadline(self, deadline: str):
        self.__deadline = deadline

    @property
    def Project(self):
        return self.__Project

    @Project.setter
    def Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_Project__Project", None)
        self.__Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "belongsToEvaluationel"):
                opp_val = getattr(old_value, "belongsToEvaluationel", None)
                if opp_val == self:
                    setattr(old_value, "belongsToEvaluationel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "belongsToEvaluationel"):
                opp_val = getattr(value, "belongsToEvaluationel", None)
                setattr(value, "belongsToEvaluationel", self)

    @property
    def oving4_Project(self):
        return self.__oving4_Project

    @oving4_Project.setter
    def oving4_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_Project__oving4_Project", None)
        self.__oving4_Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oving4_Root6"):
                opp_val = getattr(old_value, "oving4_Root6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oving4_Root6"):
                opp_val = getattr(value, "oving4_Root6", None)
                if opp_val is None:
                    setattr(value, "oving4_Root6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def oving4_Project60(self):
        return self.__oving4_Project60

    @oving4_Project60.setter
    def oving4_Project60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_Project__oving4_Project60", None)
        self.__oving4_Project60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oving4_PersonRole"):
                    opp_val = getattr(item, "oving4_PersonRole", None)
                    
                    if opp_val == self:
                        setattr(item, "oving4_PersonRole", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oving4_PersonRole"):
                    opp_val = getattr(item, "oving4_PersonRole", None)
                    
                    setattr(item, "oving4_PersonRole", self)
                    

    @property
    def containsProject(self):
        return self.__containsProject

    @containsProject.setter
    def containsProject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_Project__containsProject", None)
        self.__containsProject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EvaluationElement58"):
                opp_val = getattr(old_value, "EvaluationElement58", None)
                if opp_val == self:
                    setattr(old_value, "EvaluationElement58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EvaluationElement58"):
                opp_val = getattr(value, "EvaluationElement58", None)
                setattr(value, "EvaluationElement58", self)

class oving4_StudyProgram:

    def __init__(self, type: str, oving4_StudyProgram: "oving4_Root" = None, studyprogram: set["oving4_Course"] = None, employedOfStudyProgram: "oving4_PersonRole" = None, StudyProgram: "oving4_Course" = None, StudyProgram31: "oving4_PersonRole" = None, oving4_StudyProgram39: "oving4_TimeTable" = None):
        self.type = type
        self.oving4_StudyProgram = oving4_StudyProgram
        self.studyprogram = studyprogram if studyprogram is not None else set()
        self.employedOfStudyProgram = employedOfStudyProgram
        self.StudyProgram = StudyProgram
        self.StudyProgram31 = StudyProgram31
        self.oving4_StudyProgram39 = oving4_StudyProgram39
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def oving4_StudyProgram(self):
        return self.__oving4_StudyProgram

    @oving4_StudyProgram.setter
    def oving4_StudyProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_StudyProgram__oving4_StudyProgram", None)
        self.__oving4_StudyProgram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oving4_Root4"):
                opp_val = getattr(old_value, "oving4_Root4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oving4_Root4"):
                opp_val = getattr(value, "oving4_Root4", None)
                if opp_val is None:
                    setattr(value, "oving4_Root4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def studyprogram(self):
        return self.__studyprogram

    @studyprogram.setter
    def studyprogram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_StudyProgram__studyprogram", None)
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
    def StudyProgram(self):
        return self.__StudyProgram

    @StudyProgram.setter
    def StudyProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_StudyProgram__StudyProgram", None)
        self.__StudyProgram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containsCourse"):
                opp_val = getattr(old_value, "containsCourse", None)
                if opp_val == self:
                    setattr(old_value, "containsCourse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containsCourse"):
                opp_val = getattr(value, "containsCourse", None)
                setattr(value, "containsCourse", self)

    @property
    def employedOfStudyProgram(self):
        return self.__employedOfStudyProgram

    @employedOfStudyProgram.setter
    def employedOfStudyProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_StudyProgram__employedOfStudyProgram", None)
        self.__employedOfStudyProgram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PersonRole12"):
                opp_val = getattr(old_value, "PersonRole12", None)
                if opp_val == self:
                    setattr(old_value, "PersonRole12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PersonRole12"):
                opp_val = getattr(value, "PersonRole12", None)
                setattr(value, "PersonRole12", self)

    @property
    def StudyProgram31(self):
        return self.__StudyProgram31

    @StudyProgram31.setter
    def StudyProgram31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_StudyProgram__StudyProgram31", None)
        self.__StudyProgram31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hasEmployee"):
                opp_val = getattr(old_value, "hasEmployee", None)
                if opp_val == self:
                    setattr(old_value, "hasEmployee", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hasEmployee"):
                opp_val = getattr(value, "hasEmployee", None)
                setattr(value, "hasEmployee", self)

    @property
    def oving4_StudyProgram39(self):
        return self.__oving4_StudyProgram39

    @oving4_StudyProgram39.setter
    def oving4_StudyProgram39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_StudyProgram__oving4_StudyProgram39", None)
        self.__oving4_StudyProgram39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oving4_TimeTable38"):
                opp_val = getattr(old_value, "oving4_TimeTable38", None)
                if opp_val == self:
                    setattr(old_value, "oving4_TimeTable38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oving4_TimeTable38"):
                opp_val = getattr(value, "oving4_TimeTable38", None)
                setattr(value, "oving4_TimeTable38", self)

class oving4_Person:

    def __init__(self, first_name: str, last_name: str, name: str, studyCredits: float, oving4_Person: "oving4_Root" = None, person: set["oving4_PersonRole"] = None, personEvaluated: set["oving4_Evaluation"] = None, Person: "oving4_PersonRole" = None, Person43: "oving4_Evaluation" = None):
        self.first_name = first_name
        self.last_name = last_name
        self.name = name
        self.studyCredits = studyCredits
        self.oving4_Person = oving4_Person
        self.person = person if person is not None else set()
        self.personEvaluated = personEvaluated if personEvaluated is not None else set()
        self.Person = Person
        self.Person43 = Person43
        
    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name: str):
        self.__first_name = first_name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name: str):
        self.__last_name = last_name

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def studyCredits(self) -> float:
        return self.__studyCredits

    @studyCredits.setter
    def studyCredits(self, studyCredits: float):
        self.__studyCredits = studyCredits

    @property
    def person(self):
        return self.__person

    @person.setter
    def person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_Person__person", None)
        self.__person = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PersonRole14"):
                    opp_val = getattr(item, "PersonRole14", None)
                    
                    if opp_val == self:
                        setattr(item, "PersonRole14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PersonRole14"):
                    opp_val = getattr(item, "PersonRole14", None)
                    
                    setattr(item, "PersonRole14", self)
                    

    @property
    def personEvaluated(self):
        return self.__personEvaluated

    @personEvaluated.setter
    def personEvaluated(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_Person__personEvaluated", None)
        self.__personEvaluated = value if value is not None else set()
        
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
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_Person__Person", None)
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
    def Person43(self):
        return self.__Person43

    @Person43.setter
    def Person43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_Person__Person43", None)
        self.__Person43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hasEvaluation"):
                opp_val = getattr(old_value, "hasEvaluation", None)
                if opp_val == self:
                    setattr(old_value, "hasEvaluation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hasEvaluation"):
                opp_val = getattr(value, "hasEvaluation", None)
                setattr(value, "hasEvaluation", self)

    @property
    def oving4_Person(self):
        return self.__oving4_Person

    @oving4_Person.setter
    def oving4_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_Person__oving4_Person", None)
        self.__oving4_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oving4_Root2"):
                opp_val = getattr(old_value, "oving4_Root2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oving4_Root2"):
                opp_val = getattr(value, "oving4_Root2", None)
                if opp_val is None:
                    setattr(value, "oving4_Root2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def takeExam(self, course: str, percentageResult: float) -> bool:
        # TODO: Implement takeExam method
        pass

    def cancelExam(self, course: str) -> bool:
        # TODO: Implement cancelExam method
        pass

    def signUpForExam(self, course: str) -> bool:
        # TODO: Implement signUpForExam method
        pass

class oving4_Department:

    def __init__(self, name: str, oving4_Department: "oving4_Root" = None, oving4_Department8: set["oving4_Course"] = None, employedByDepartment: set["oving4_PersonRole"] = None, Department: "oving4_PersonRole" = None):
        self.name = name
        self.oving4_Department = oving4_Department
        self.oving4_Department8 = oving4_Department8 if oving4_Department8 is not None else set()
        self.employedByDepartment = employedByDepartment if employedByDepartment is not None else set()
        self.Department = Department
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def oving4_Department(self):
        return self.__oving4_Department

    @oving4_Department.setter
    def oving4_Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_Department__oving4_Department", None)
        self.__oving4_Department = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oving4_Root"):
                opp_val = getattr(old_value, "oving4_Root", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oving4_Root"):
                opp_val = getattr(value, "oving4_Root", None)
                if opp_val is None:
                    setattr(value, "oving4_Root", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def employedByDepartment(self):
        return self.__employedByDepartment

    @employedByDepartment.setter
    def employedByDepartment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_Department__employedByDepartment", None)
        self.__employedByDepartment = value if value is not None else set()
        
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
                    

    @property
    def Department(self):
        return self.__Department

    @Department.setter
    def Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_Department__Department", None)
        self.__Department = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hasEmployee35"):
                opp_val = getattr(old_value, "hasEmployee35", None)
                if opp_val == self:
                    setattr(old_value, "hasEmployee35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hasEmployee35"):
                opp_val = getattr(value, "hasEmployee35", None)
                setattr(value, "hasEmployee35", self)

    @property
    def oving4_Department8(self):
        return self.__oving4_Department8

    @oving4_Department8.setter
    def oving4_Department8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving4_Department__oving4_Department8", None)
        self.__oving4_Department8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oving4_Course"):
                    opp_val = getattr(item, "oving4_Course", None)
                    
                    if opp_val == self:
                        setattr(item, "oving4_Course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oving4_Course"):
                    opp_val = getattr(item, "oving4_Course", None)
                    
                    setattr(item, "oving4_Course", self)
                    

class oving4_Root:

    pass