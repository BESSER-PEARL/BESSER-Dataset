from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class personRoleType(Enum):
    Lecture = "Lecture"
    CourseCordinator = "CourseCordinator"
class CourseWorkType(Enum):
    Lecture = "Lecture"
    Lab = "Lab"
    Exercise = "Exercise"
class PrecondistionType(Enum):
    Required = "Required"
    Recommended = "Recommended"
class TermType(Enum):
    Spring = "Spring"
    Summer = "Summer"
    Fall = "Fall"
class EvaluationType(Enum):
    WrittenExam = "WrittenExam"
    OralExam = "OralExam"
    Assignments = "Assignments"
    PracticalExam = "PracticalExam"
    Participated = "Participated"


############################################
# Definition of Classes
############################################

class coursePages_Reduction:

    def __init__(self, creditReduction: float, coursePages_Reduction38: "coursePages_Course" = None, coursePages_Reduction: "coursePages_Course" = None):
        self.creditReduction = creditReduction
        self.coursePages_Reduction38 = coursePages_Reduction38
        self.coursePages_Reduction = coursePages_Reduction
        
    @property
    def creditReduction(self) -> float:
        return self.__creditReduction

    @creditReduction.setter
    def creditReduction(self, creditReduction: float):
        self.__creditReduction = creditReduction

    @property
    def coursePages_Reduction38(self):
        return self.__coursePages_Reduction38

    @coursePages_Reduction38.setter
    def coursePages_Reduction38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_Reduction__coursePages_Reduction38", None)
        self.__coursePages_Reduction38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coursePages_Course39"):
                opp_val = getattr(old_value, "coursePages_Course39", None)
                if opp_val == self:
                    setattr(old_value, "coursePages_Course39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coursePages_Course39"):
                opp_val = getattr(value, "coursePages_Course39", None)
                setattr(value, "coursePages_Course39", self)

    @property
    def coursePages_Reduction(self):
        return self.__coursePages_Reduction

    @coursePages_Reduction.setter
    def coursePages_Reduction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_Reduction__coursePages_Reduction", None)
        self.__coursePages_Reduction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coursePages_Course25"):
                opp_val = getattr(old_value, "coursePages_Course25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coursePages_Course25"):
                opp_val = getattr(value, "coursePages_Course25", None)
                if opp_val is None:
                    setattr(value, "coursePages_Course25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class coursePages_CourseWork:

    pass
class coursePages_CourseWorkObject:

    def __init__(self, courseWorkType: str, room: str, day: str, start: date, end: date, coursePages_CourseWorkObject: "coursePages_CourseWork" = None):
        self.courseWorkType = courseWorkType
        self.room = room
        self.day = day
        self.start = start
        self.end = end
        self.coursePages_CourseWorkObject = coursePages_CourseWorkObject
        
    @property
    def start(self) -> date:
        return self.__start

    @start.setter
    def start(self, start: date):
        self.__start = start

    @property
    def end(self) -> date:
        return self.__end

    @end.setter
    def end(self, end: date):
        self.__end = end

    @property
    def room(self) -> str:
        return self.__room

    @room.setter
    def room(self, room: str):
        self.__room = room

    @property
    def courseWorkType(self) -> str:
        return self.__courseWorkType

    @courseWorkType.setter
    def courseWorkType(self, courseWorkType: str):
        self.__courseWorkType = courseWorkType

    @property
    def day(self) -> str:
        return self.__day

    @day.setter
    def day(self, day: str):
        self.__day = day

    @property
    def coursePages_CourseWorkObject(self):
        return self.__coursePages_CourseWorkObject

    @coursePages_CourseWorkObject.setter
    def coursePages_CourseWorkObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_CourseWorkObject__coursePages_CourseWorkObject", None)
        self.__coursePages_CourseWorkObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coursePages_CourseWork"):
                opp_val = getattr(old_value, "coursePages_CourseWork", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coursePages_CourseWork"):
                opp_val = getattr(value, "coursePages_CourseWork", None)
                if opp_val is None:
                    setattr(value, "coursePages_CourseWork", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class coursePages_Precondition:

    def __init__(self, preconditionStatus: str, coursePages_Precondition: "coursePages_Course" = None, coursePages_Precondition35: "coursePages_Course" = None):
        self.preconditionStatus = preconditionStatus
        self.coursePages_Precondition = coursePages_Precondition
        self.coursePages_Precondition35 = coursePages_Precondition35
        
    @property
    def preconditionStatus(self) -> str:
        return self.__preconditionStatus

    @preconditionStatus.setter
    def preconditionStatus(self, preconditionStatus: str):
        self.__preconditionStatus = preconditionStatus

    @property
    def coursePages_Precondition(self):
        return self.__coursePages_Precondition

    @coursePages_Precondition.setter
    def coursePages_Precondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_Precondition__coursePages_Precondition", None)
        self.__coursePages_Precondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coursePages_Course23"):
                opp_val = getattr(old_value, "coursePages_Course23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coursePages_Course23"):
                opp_val = getattr(value, "coursePages_Course23", None)
                if opp_val is None:
                    setattr(value, "coursePages_Course23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def coursePages_Precondition35(self):
        return self.__coursePages_Precondition35

    @coursePages_Precondition35.setter
    def coursePages_Precondition35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_Precondition__coursePages_Precondition35", None)
        self.__coursePages_Precondition35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coursePages_Course36"):
                opp_val = getattr(old_value, "coursePages_Course36", None)
                if opp_val == self:
                    setattr(old_value, "coursePages_Course36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coursePages_Course36"):
                opp_val = getattr(value, "coursePages_Course36", None)
                setattr(value, "coursePages_Course36", self)

class coursePages_CourseWorker:

    def __init__(self, courseRole: str, coursePages_CourseWorker: "coursePages_Course" = None, coursePages_CourseWorker33: "coursePages_Employee" = None):
        self.courseRole = courseRole
        self.coursePages_CourseWorker = coursePages_CourseWorker
        self.coursePages_CourseWorker33 = coursePages_CourseWorker33
        
    @property
    def courseRole(self) -> str:
        return self.__courseRole

    @courseRole.setter
    def courseRole(self, courseRole: str):
        self.__courseRole = courseRole

    @property
    def coursePages_CourseWorker(self):
        return self.__coursePages_CourseWorker

    @coursePages_CourseWorker.setter
    def coursePages_CourseWorker(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_CourseWorker__coursePages_CourseWorker", None)
        self.__coursePages_CourseWorker = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coursePages_Course21"):
                opp_val = getattr(old_value, "coursePages_Course21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coursePages_Course21"):
                opp_val = getattr(value, "coursePages_Course21", None)
                if opp_val is None:
                    setattr(value, "coursePages_Course21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def coursePages_CourseWorker33(self):
        return self.__coursePages_CourseWorker33

    @coursePages_CourseWorker33.setter
    def coursePages_CourseWorker33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_CourseWorker__coursePages_CourseWorker33", None)
        self.__coursePages_CourseWorker33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coursePages_Employee"):
                opp_val = getattr(old_value, "coursePages_Employee", None)
                if opp_val == self:
                    setattr(old_value, "coursePages_Employee", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coursePages_Employee"):
                opp_val = getattr(value, "coursePages_Employee", None)
                setattr(value, "coursePages_Employee", self)

class coursePages_CourseInstance:

    def __init__(self, courseYear: str, term: str, coursePages_CourseInstance: "coursePages_Course" = None, coursePages_CourseInstance27: "coursePages_CourseWork" = None, coursePages_CourseInstance30: "coursePages_Evaluations" = None):
        self.courseYear = courseYear
        self.term = term
        self.coursePages_CourseInstance = coursePages_CourseInstance
        self.coursePages_CourseInstance27 = coursePages_CourseInstance27
        self.coursePages_CourseInstance30 = coursePages_CourseInstance30
        
    @property
    def courseYear(self) -> str:
        return self.__courseYear

    @courseYear.setter
    def courseYear(self, courseYear: str):
        self.__courseYear = courseYear

    @property
    def term(self) -> str:
        return self.__term

    @term.setter
    def term(self, term: str):
        self.__term = term

    @property
    def coursePages_CourseInstance27(self):
        return self.__coursePages_CourseInstance27

    @coursePages_CourseInstance27.setter
    def coursePages_CourseInstance27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_CourseInstance__coursePages_CourseInstance27", None)
        self.__coursePages_CourseInstance27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coursePages_CourseWork28"):
                opp_val = getattr(old_value, "coursePages_CourseWork28", None)
                if opp_val == self:
                    setattr(old_value, "coursePages_CourseWork28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coursePages_CourseWork28"):
                opp_val = getattr(value, "coursePages_CourseWork28", None)
                setattr(value, "coursePages_CourseWork28", self)

    @property
    def coursePages_CourseInstance(self):
        return self.__coursePages_CourseInstance

    @coursePages_CourseInstance.setter
    def coursePages_CourseInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_CourseInstance__coursePages_CourseInstance", None)
        self.__coursePages_CourseInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coursePages_Course17"):
                opp_val = getattr(old_value, "coursePages_Course17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coursePages_Course17"):
                opp_val = getattr(value, "coursePages_Course17", None)
                if opp_val is None:
                    setattr(value, "coursePages_Course17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def coursePages_CourseInstance30(self):
        return self.__coursePages_CourseInstance30

    @coursePages_CourseInstance30.setter
    def coursePages_CourseInstance30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_CourseInstance__coursePages_CourseInstance30", None)
        self.__coursePages_CourseInstance30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coursePages_Evaluations31"):
                opp_val = getattr(old_value, "coursePages_Evaluations31", None)
                if opp_val == self:
                    setattr(old_value, "coursePages_Evaluations31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coursePages_Evaluations31"):
                opp_val = getattr(value, "coursePages_Evaluations31", None)
                setattr(value, "coursePages_Evaluations31", self)

class coursePages_Evaluations:

    pass
class coursePages_EvaluationObject:

    def __init__(self, evaluationsForm: str, term: str, credits: int, date: date, coursePages_EvaluationObject: "coursePages_Evaluations" = None):
        self.evaluationsForm = evaluationsForm
        self.term = term
        self.credits = credits
        self.date = date
        self.coursePages_EvaluationObject = coursePages_EvaluationObject
        
    @property
    def evaluationsForm(self) -> str:
        return self.__evaluationsForm

    @evaluationsForm.setter
    def evaluationsForm(self, evaluationsForm: str):
        self.__evaluationsForm = evaluationsForm

    @property
    def term(self) -> str:
        return self.__term

    @term.setter
    def term(self, term: str):
        self.__term = term

    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def credits(self) -> int:
        return self.__credits

    @credits.setter
    def credits(self, credits: int):
        self.__credits = credits

    @property
    def coursePages_EvaluationObject(self):
        return self.__coursePages_EvaluationObject

    @coursePages_EvaluationObject.setter
    def coursePages_EvaluationObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_EvaluationObject__coursePages_EvaluationObject", None)
        self.__coursePages_EvaluationObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coursePages_Evaluations"):
                opp_val = getattr(old_value, "coursePages_Evaluations", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coursePages_Evaluations"):
                opp_val = getattr(value, "coursePages_Evaluations", None)
                if opp_val is None:
                    setattr(value, "coursePages_Evaluations", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class coursePages_Course:

    def __init__(self, courseCredits: float, courseContent: str, courseCode: str, courseName: str, coursePages_Course: "coursePages_Student" = None, Course: "coursePages_StudyPrograms" = None, coursePages_Course7: "coursePages_Department" = None, coursePages_Course17: set["coursePages_CourseInstance"] = None, course: set["coursePages_StudyPrograms"] = None, coursePages_Course21: set["coursePages_CourseWorker"] = None, coursePages_Course23: set["coursePages_Precondition"] = None, coursePages_Course36: "coursePages_Precondition" = None, coursePages_Course39: "coursePages_Reduction" = None, coursePages_Course25: set["coursePages_Reduction"] = None):
        self.courseCredits = courseCredits
        self.courseContent = courseContent
        self.courseCode = courseCode
        self.courseName = courseName
        self.coursePages_Course = coursePages_Course
        self.Course = Course
        self.coursePages_Course7 = coursePages_Course7
        self.coursePages_Course17 = coursePages_Course17 if coursePages_Course17 is not None else set()
        self.course = course if course is not None else set()
        self.coursePages_Course21 = coursePages_Course21 if coursePages_Course21 is not None else set()
        self.coursePages_Course23 = coursePages_Course23 if coursePages_Course23 is not None else set()
        self.coursePages_Course36 = coursePages_Course36
        self.coursePages_Course39 = coursePages_Course39
        self.coursePages_Course25 = coursePages_Course25 if coursePages_Course25 is not None else set()
        
    @property
    def courseName(self) -> str:
        return self.__courseName

    @courseName.setter
    def courseName(self, courseName: str):
        self.__courseName = courseName

    @property
    def courseContent(self) -> str:
        return self.__courseContent

    @courseContent.setter
    def courseContent(self, courseContent: str):
        self.__courseContent = courseContent

    @property
    def courseCode(self) -> str:
        return self.__courseCode

    @courseCode.setter
    def courseCode(self, courseCode: str):
        self.__courseCode = courseCode

    @property
    def courseCredits(self) -> float:
        return self.__courseCredits

    @courseCredits.setter
    def courseCredits(self, courseCredits: float):
        self.__courseCredits = courseCredits

    @property
    def coursePages_Course21(self):
        return self.__coursePages_Course21

    @coursePages_Course21.setter
    def coursePages_Course21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_Course__coursePages_Course21", None)
        self.__coursePages_Course21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coursePages_CourseWorker"):
                    opp_val = getattr(item, "coursePages_CourseWorker", None)
                    
                    if opp_val == self:
                        setattr(item, "coursePages_CourseWorker", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coursePages_CourseWorker"):
                    opp_val = getattr(item, "coursePages_CourseWorker", None)
                    
                    setattr(item, "coursePages_CourseWorker", self)
                    

    @property
    def coursePages_Course36(self):
        return self.__coursePages_Course36

    @coursePages_Course36.setter
    def coursePages_Course36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_Course__coursePages_Course36", None)
        self.__coursePages_Course36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coursePages_Precondition35"):
                opp_val = getattr(old_value, "coursePages_Precondition35", None)
                if opp_val == self:
                    setattr(old_value, "coursePages_Precondition35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coursePages_Precondition35"):
                opp_val = getattr(value, "coursePages_Precondition35", None)
                setattr(value, "coursePages_Precondition35", self)

    @property
    def coursePages_Course25(self):
        return self.__coursePages_Course25

    @coursePages_Course25.setter
    def coursePages_Course25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_Course__coursePages_Course25", None)
        self.__coursePages_Course25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coursePages_Reduction"):
                    opp_val = getattr(item, "coursePages_Reduction", None)
                    
                    if opp_val == self:
                        setattr(item, "coursePages_Reduction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coursePages_Reduction"):
                    opp_val = getattr(item, "coursePages_Reduction", None)
                    
                    setattr(item, "coursePages_Reduction", self)
                    

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_Course__course", None)
        self.__course = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StudyPrograms19"):
                    opp_val = getattr(item, "StudyPrograms19", None)
                    
                    if opp_val == self:
                        setattr(item, "StudyPrograms19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StudyPrograms19"):
                    opp_val = getattr(item, "StudyPrograms19", None)
                    
                    setattr(item, "StudyPrograms19", self)
                    

    @property
    def coursePages_Course17(self):
        return self.__coursePages_Course17

    @coursePages_Course17.setter
    def coursePages_Course17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_Course__coursePages_Course17", None)
        self.__coursePages_Course17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coursePages_CourseInstance"):
                    opp_val = getattr(item, "coursePages_CourseInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "coursePages_CourseInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coursePages_CourseInstance"):
                    opp_val = getattr(item, "coursePages_CourseInstance", None)
                    
                    setattr(item, "coursePages_CourseInstance", self)
                    

    @property
    def coursePages_Course23(self):
        return self.__coursePages_Course23

    @coursePages_Course23.setter
    def coursePages_Course23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_Course__coursePages_Course23", None)
        self.__coursePages_Course23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coursePages_Precondition"):
                    opp_val = getattr(item, "coursePages_Precondition", None)
                    
                    if opp_val == self:
                        setattr(item, "coursePages_Precondition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coursePages_Precondition"):
                    opp_val = getattr(item, "coursePages_Precondition", None)
                    
                    setattr(item, "coursePages_Precondition", self)
                    

    @property
    def coursePages_Course(self):
        return self.__coursePages_Course

    @coursePages_Course.setter
    def coursePages_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_Course__coursePages_Course", None)
        self.__coursePages_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coursePages_Student"):
                opp_val = getattr(old_value, "coursePages_Student", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coursePages_Student"):
                opp_val = getattr(value, "coursePages_Student", None)
                if opp_val is None:
                    setattr(value, "coursePages_Student", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Course(self):
        return self.__Course

    @Course.setter
    def Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_Course__Course", None)
        self.__Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprograms13"):
                opp_val = getattr(old_value, "studyprograms13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprograms13"):
                opp_val = getattr(value, "studyprograms13", None)
                if opp_val is None:
                    setattr(value, "studyprograms13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def coursePages_Course7(self):
        return self.__coursePages_Course7

    @coursePages_Course7.setter
    def coursePages_Course7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_Course__coursePages_Course7", None)
        self.__coursePages_Course7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coursePages_Department"):
                opp_val = getattr(old_value, "coursePages_Department", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coursePages_Department"):
                opp_val = getattr(value, "coursePages_Department", None)
                if opp_val is None:
                    setattr(value, "coursePages_Department", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def coursePages_Course39(self):
        return self.__coursePages_Course39

    @coursePages_Course39.setter
    def coursePages_Course39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_Course__coursePages_Course39", None)
        self.__coursePages_Course39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coursePages_Reduction38"):
                opp_val = getattr(old_value, "coursePages_Reduction38", None)
                if opp_val == self:
                    setattr(old_value, "coursePages_Reduction38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coursePages_Reduction38"):
                opp_val = getattr(value, "coursePages_Reduction38", None)
                setattr(value, "coursePages_Reduction38", self)

class coursePages_StudyPrograms:

    def __init__(self, studyProgramCode: str, studyProgramName: str, StudyPrograms: "coursePages_Student" = None, studyprograms13: set["coursePages_Course"] = None, StudyPrograms5: "coursePages_Department" = None, studyprograms: "coursePages_Department" = None, studyprograms11: set["coursePages_Student"] = None, StudyPrograms19: "coursePages_Course" = None):
        self.studyProgramCode = studyProgramCode
        self.studyProgramName = studyProgramName
        self.StudyPrograms = StudyPrograms
        self.studyprograms13 = studyprograms13 if studyprograms13 is not None else set()
        self.StudyPrograms5 = StudyPrograms5
        self.studyprograms = studyprograms
        self.studyprograms11 = studyprograms11 if studyprograms11 is not None else set()
        self.StudyPrograms19 = StudyPrograms19
        
    @property
    def studyProgramCode(self) -> str:
        return self.__studyProgramCode

    @studyProgramCode.setter
    def studyProgramCode(self, studyProgramCode: str):
        self.__studyProgramCode = studyProgramCode

    @property
    def studyProgramName(self) -> str:
        return self.__studyProgramName

    @studyProgramName.setter
    def studyProgramName(self, studyProgramName: str):
        self.__studyProgramName = studyProgramName

    @property
    def studyprograms13(self):
        return self.__studyprograms13

    @studyprograms13.setter
    def studyprograms13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_StudyPrograms__studyprograms13", None)
        self.__studyprograms13 = value if value is not None else set()
        
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
    def studyprograms(self):
        return self.__studyprograms

    @studyprograms.setter
    def studyprograms(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_StudyPrograms__studyprograms", None)
        self.__studyprograms = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Department9"):
                opp_val = getattr(old_value, "Department9", None)
                if opp_val == self:
                    setattr(old_value, "Department9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Department9"):
                opp_val = getattr(value, "Department9", None)
                setattr(value, "Department9", self)

    @property
    def StudyPrograms5(self):
        return self.__StudyPrograms5

    @StudyPrograms5.setter
    def StudyPrograms5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_StudyPrograms__StudyPrograms5", None)
        self.__StudyPrograms5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "belongsToDepartment"):
                opp_val = getattr(old_value, "belongsToDepartment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "belongsToDepartment"):
                opp_val = getattr(value, "belongsToDepartment", None)
                if opp_val is None:
                    setattr(value, "belongsToDepartment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StudyPrograms(self):
        return self.__StudyPrograms

    @StudyPrograms.setter
    def StudyPrograms(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_StudyPrograms__StudyPrograms", None)
        self.__StudyPrograms = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student"):
                opp_val = getattr(old_value, "student", None)
                if opp_val == self:
                    setattr(old_value, "student", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student"):
                opp_val = getattr(value, "student", None)
                setattr(value, "student", self)

    @property
    def StudyPrograms19(self):
        return self.__StudyPrograms19

    @StudyPrograms19.setter
    def StudyPrograms19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_StudyPrograms__StudyPrograms19", None)
        self.__StudyPrograms19 = value
        
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
    def studyprograms11(self):
        return self.__studyprograms11

    @studyprograms11.setter
    def studyprograms11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_StudyPrograms__studyprograms11", None)
        self.__studyprograms11 = value if value is not None else set()
        
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
                    

class Person:

    pass
class coursePages_Student(Person):

    def __init__(self, studentID: str, coursePages_Student: set["coursePages_Course"] = None, student: "coursePages_StudyPrograms" = None, Student: "coursePages_StudyPrograms" = None):
        self.studentID = studentID
        self.coursePages_Student = coursePages_Student if coursePages_Student is not None else set()
        self.student = student
        self.Student = Student
        
    @property
    def studentID(self) -> str:
        return self.__studentID

    @studentID.setter
    def studentID(self, studentID: str):
        self.__studentID = studentID

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_Student__student", None)
        self.__student = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyPrograms"):
                opp_val = getattr(old_value, "StudyPrograms", None)
                if opp_val == self:
                    setattr(old_value, "StudyPrograms", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyPrograms"):
                opp_val = getattr(value, "StudyPrograms", None)
                setattr(value, "StudyPrograms", self)

    @property
    def coursePages_Student(self):
        return self.__coursePages_Student

    @coursePages_Student.setter
    def coursePages_Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_Student__coursePages_Student", None)
        self.__coursePages_Student = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coursePages_Course"):
                    opp_val = getattr(item, "coursePages_Course", None)
                    
                    if opp_val == self:
                        setattr(item, "coursePages_Course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coursePages_Course"):
                    opp_val = getattr(item, "coursePages_Course", None)
                    
                    setattr(item, "coursePages_Course", self)
                    

    @property
    def Student(self):
        return self.__Student

    @Student.setter
    def Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_Student__Student", None)
        self.__Student = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprograms11"):
                opp_val = getattr(old_value, "studyprograms11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprograms11"):
                opp_val = getattr(value, "studyprograms11", None)
                if opp_val is None:
                    setattr(value, "studyprograms11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class coursePages_Department:

    def __init__(self, departmentName: str, phoneNummber: str, email: str, Department: "coursePages_Employee" = None, department: set["coursePages_Employee"] = None, belongsToDepartment: set["coursePages_StudyPrograms"] = None, coursePages_Department: set["coursePages_Course"] = None, Department9: "coursePages_StudyPrograms" = None):
        self.departmentName = departmentName
        self.phoneNummber = phoneNummber
        self.email = email
        self.Department = Department
        self.department = department if department is not None else set()
        self.belongsToDepartment = belongsToDepartment if belongsToDepartment is not None else set()
        self.coursePages_Department = coursePages_Department if coursePages_Department is not None else set()
        self.Department9 = Department9
        
    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def departmentName(self) -> str:
        return self.__departmentName

    @departmentName.setter
    def departmentName(self, departmentName: str):
        self.__departmentName = departmentName

    @property
    def phoneNummber(self) -> str:
        return self.__phoneNummber

    @phoneNummber.setter
    def phoneNummber(self, phoneNummber: str):
        self.__phoneNummber = phoneNummber

    @property
    def belongsToDepartment(self):
        return self.__belongsToDepartment

    @belongsToDepartment.setter
    def belongsToDepartment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_Department__belongsToDepartment", None)
        self.__belongsToDepartment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StudyPrograms5"):
                    opp_val = getattr(item, "StudyPrograms5", None)
                    
                    if opp_val == self:
                        setattr(item, "StudyPrograms5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StudyPrograms5"):
                    opp_val = getattr(item, "StudyPrograms5", None)
                    
                    setattr(item, "StudyPrograms5", self)
                    

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_Department__department", None)
        self.__department = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee"):
                    opp_val = getattr(item, "Employee", None)
                    
                    if opp_val == self:
                        setattr(item, "Employee", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee"):
                    opp_val = getattr(item, "Employee", None)
                    
                    setattr(item, "Employee", self)
                    

    @property
    def Department(self):
        return self.__Department

    @Department.setter
    def Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_Department__Department", None)
        self.__Department = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee"):
                opp_val = getattr(old_value, "employee", None)
                if opp_val == self:
                    setattr(old_value, "employee", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee"):
                opp_val = getattr(value, "employee", None)
                setattr(value, "employee", self)

    @property
    def coursePages_Department(self):
        return self.__coursePages_Department

    @coursePages_Department.setter
    def coursePages_Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_Department__coursePages_Department", None)
        self.__coursePages_Department = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coursePages_Course7"):
                    opp_val = getattr(item, "coursePages_Course7", None)
                    
                    if opp_val == self:
                        setattr(item, "coursePages_Course7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coursePages_Course7"):
                    opp_val = getattr(item, "coursePages_Course7", None)
                    
                    setattr(item, "coursePages_Course7", self)
                    

    @property
    def Department9(self):
        return self.__Department9

    @Department9.setter
    def Department9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_Department__Department9", None)
        self.__Department9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprograms"):
                opp_val = getattr(old_value, "studyprograms", None)
                if opp_val == self:
                    setattr(old_value, "studyprograms", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprograms"):
                opp_val = getattr(value, "studyprograms", None)
                setattr(value, "studyprograms", self)

class coursePages_Employee(Person):

    def __init__(self, position: str, employee: "coursePages_Department" = None, Employee: "coursePages_Department" = None, coursePages_Employee: "coursePages_CourseWorker" = None):
        self.position = position
        self.employee = employee
        self.Employee = Employee
        self.coursePages_Employee = coursePages_Employee
        
    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def coursePages_Employee(self):
        return self.__coursePages_Employee

    @coursePages_Employee.setter
    def coursePages_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_Employee__coursePages_Employee", None)
        self.__coursePages_Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coursePages_CourseWorker33"):
                opp_val = getattr(old_value, "coursePages_CourseWorker33", None)
                if opp_val == self:
                    setattr(old_value, "coursePages_CourseWorker33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coursePages_CourseWorker33"):
                opp_val = getattr(value, "coursePages_CourseWorker33", None)
                setattr(value, "coursePages_CourseWorker33", self)

    @property
    def Employee(self):
        return self.__Employee

    @Employee.setter
    def Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_Employee__Employee", None)
        self.__Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department"):
                opp_val = getattr(old_value, "department", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department"):
                opp_val = getattr(value, "department", None)
                if opp_val is None:
                    setattr(value, "department", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def employee(self):
        return self.__employee

    @employee.setter
    def employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coursePages_Employee__employee", None)
        self.__employee = value
        
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

class coursePages_Person:

    def __init__(self, firstName: str, surName: str, phoneNummber: str, email: str):
        self.firstName = firstName
        self.surName = surName
        self.phoneNummber = phoneNummber
        self.email = email
        
    @property
    def phoneNummber(self) -> str:
        return self.__phoneNummber

    @phoneNummber.setter
    def phoneNummber(self, phoneNummber: str):
        self.__phoneNummber = phoneNummber

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def surName(self) -> str:
        return self.__surName

    @surName.setter
    def surName(self, surName: str):
        self.__surName = surName
