from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class EducationLevel(Enum):
    bachelor = "bachelor"
    master = "master"
    phd = "phd"
    oneYear = "oneYear"
class WorkForm(Enum):
    oral = "oral"
    written = "written"
    home = "home"
class Campus(Enum):
    Trondheim = "Trondheim"
    Gjøvik = "Gjøvik"
    Web = "Web"
    Ålesund = "Ålesund"
class EvaluationType(Enum):
    grade = "grade"
    approved = "approved"
class Semester(Enum):
    autumn = "autumn"
    spring = "spring"


############################################
# Definition of Classes
############################################

class courceList_StudyCourceRelation:

    def __init__(self, status: str, year: int, cource25: "courceList_Specialisation" = None, StudyCourceRelation: "courceList_Specialisation" = None, courceList_StudyCourceRelation: "courceList_CourceSpecification" = None):
        self.status = status
        self.year = year
        self.cource25 = cource25
        self.StudyCourceRelation = StudyCourceRelation
        self.courceList_StudyCourceRelation = courceList_StudyCourceRelation
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def courceList_StudyCourceRelation(self):
        return self.__courceList_StudyCourceRelation

    @courceList_StudyCourceRelation.setter
    def courceList_StudyCourceRelation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_StudyCourceRelation__courceList_StudyCourceRelation", None)
        self.__courceList_StudyCourceRelation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courceList_CourceSpecification"):
                opp_val = getattr(old_value, "courceList_CourceSpecification", None)
                if opp_val == self:
                    setattr(old_value, "courceList_CourceSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courceList_CourceSpecification"):
                opp_val = getattr(value, "courceList_CourceSpecification", None)
                setattr(value, "courceList_CourceSpecification", self)

    @property
    def StudyCourceRelation(self):
        return self.__StudyCourceRelation

    @StudyCourceRelation.setter
    def StudyCourceRelation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_StudyCourceRelation__StudyCourceRelation", None)
        self.__StudyCourceRelation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specialisation"):
                opp_val = getattr(old_value, "specialisation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specialisation"):
                opp_val = getattr(value, "specialisation", None)
                if opp_val is None:
                    setattr(value, "specialisation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cource25(self):
        return self.__cource25

    @cource25.setter
    def cource25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_StudyCourceRelation__cource25", None)
        self.__cource25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Specialisation26"):
                opp_val = getattr(old_value, "Specialisation26", None)
                if opp_val == self:
                    setattr(old_value, "Specialisation26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Specialisation26"):
                opp_val = getattr(value, "Specialisation26", None)
                setattr(value, "Specialisation26", self)

class courceList_EvaluationForm:

    def __init__(self, evaluationType: str, evaluationForm: "courceList_Exam" = None, evaluationForm17: "courceList_Work" = None, evaluationForm19: "courceList_CourceSpecification" = None, EvaluationForm: "courceList_Exam" = None, EvaluationForm22: "courceList_Work" = None, EvaluationForm45: "courceList_CourceSpecification" = None):
        self.evaluationType = evaluationType
        self.evaluationForm = evaluationForm
        self.evaluationForm17 = evaluationForm17
        self.evaluationForm19 = evaluationForm19
        self.EvaluationForm = EvaluationForm
        self.EvaluationForm22 = EvaluationForm22
        self.EvaluationForm45 = EvaluationForm45
        
    @property
    def evaluationType(self) -> str:
        return self.__evaluationType

    @evaluationType.setter
    def evaluationType(self, evaluationType: str):
        self.__evaluationType = evaluationType

    @property
    def EvaluationForm22(self):
        return self.__EvaluationForm22

    @EvaluationForm22.setter
    def EvaluationForm22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_EvaluationForm__EvaluationForm22", None)
        self.__EvaluationForm22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "work"):
                opp_val = getattr(old_value, "work", None)
                if opp_val == self:
                    setattr(old_value, "work", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "work"):
                opp_val = getattr(value, "work", None)
                setattr(value, "work", self)

    @property
    def evaluationForm17(self):
        return self.__evaluationForm17

    @evaluationForm17.setter
    def evaluationForm17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_EvaluationForm__evaluationForm17", None)
        self.__evaluationForm17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Work"):
                opp_val = getattr(old_value, "Work", None)
                if opp_val == self:
                    setattr(old_value, "Work", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Work"):
                opp_val = getattr(value, "Work", None)
                setattr(value, "Work", self)

    @property
    def EvaluationForm45(self):
        return self.__EvaluationForm45

    @EvaluationForm45.setter
    def EvaluationForm45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_EvaluationForm__EvaluationForm45", None)
        self.__EvaluationForm45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cource44"):
                opp_val = getattr(old_value, "cource44", None)
                if opp_val == self:
                    setattr(old_value, "cource44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cource44"):
                opp_val = getattr(value, "cource44", None)
                setattr(value, "cource44", self)

    @property
    def evaluationForm(self):
        return self.__evaluationForm

    @evaluationForm.setter
    def evaluationForm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_EvaluationForm__evaluationForm", None)
        self.__evaluationForm = value
        
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
    def EvaluationForm(self):
        return self.__EvaluationForm

    @EvaluationForm.setter
    def EvaluationForm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_EvaluationForm__EvaluationForm", None)
        self.__EvaluationForm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exam"):
                opp_val = getattr(old_value, "exam", None)
                if opp_val == self:
                    setattr(old_value, "exam", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exam"):
                opp_val = getattr(value, "exam", None)
                setattr(value, "exam", self)

    @property
    def evaluationForm19(self):
        return self.__evaluationForm19

    @evaluationForm19.setter
    def evaluationForm19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_EvaluationForm__evaluationForm19", None)
        self.__evaluationForm19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CourceSpecification20"):
                opp_val = getattr(old_value, "CourceSpecification20", None)
                if opp_val == self:
                    setattr(old_value, "CourceSpecification20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CourceSpecification20"):
                opp_val = getattr(value, "CourceSpecification20", None)
                setattr(value, "CourceSpecification20", self)

class courceList_Exam:

    def __init__(self, form: str, lenght: int, date: date, weight: int, Exam: "courceList_EvaluationForm" = None, exam: "courceList_EvaluationForm" = None):
        self.form = form
        self.lenght = lenght
        self.date = date
        self.weight = weight
        self.Exam = Exam
        self.exam = exam
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def form(self) -> str:
        return self.__form

    @form.setter
    def form(self, form: str):
        self.__form = form

    @property
    def lenght(self) -> int:
        return self.__lenght

    @lenght.setter
    def lenght(self, lenght: int):
        self.__lenght = lenght

    @property
    def exam(self):
        return self.__exam

    @exam.setter
    def exam(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_Exam__exam", None)
        self.__exam = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EvaluationForm"):
                opp_val = getattr(old_value, "EvaluationForm", None)
                if opp_val == self:
                    setattr(old_value, "EvaluationForm", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EvaluationForm"):
                opp_val = getattr(value, "EvaluationForm", None)
                setattr(value, "EvaluationForm", self)

    @property
    def Exam(self):
        return self.__Exam

    @Exam.setter
    def Exam(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_Exam__Exam", None)
        self.__Exam = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "evaluationForm"):
                opp_val = getattr(old_value, "evaluationForm", None)
                if opp_val == self:
                    setattr(old_value, "evaluationForm", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "evaluationForm"):
                opp_val = getattr(value, "evaluationForm", None)
                setattr(value, "evaluationForm", self)

class courceList_Work:

    def __init__(self, weight: int, Work: "courceList_EvaluationForm" = None, work: "courceList_EvaluationForm" = None):
        self.weight = weight
        self.Work = Work
        self.work = work
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def Work(self):
        return self.__Work

    @Work.setter
    def Work(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_Work__Work", None)
        self.__Work = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "evaluationForm17"):
                opp_val = getattr(old_value, "evaluationForm17", None)
                if opp_val == self:
                    setattr(old_value, "evaluationForm17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "evaluationForm17"):
                opp_val = getattr(value, "evaluationForm17", None)
                setattr(value, "evaluationForm17", self)

    @property
    def work(self):
        return self.__work

    @work.setter
    def work(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_Work__work", None)
        self.__work = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EvaluationForm22"):
                opp_val = getattr(old_value, "EvaluationForm22", None)
                if opp_val == self:
                    setattr(old_value, "EvaluationForm22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EvaluationForm22"):
                opp_val = getattr(value, "EvaluationForm22", None)
                setattr(value, "EvaluationForm22", self)

class courceList_Specialisation:

    def __init__(self, name: str, startSemester: int, Specialisation: "courceList_StudyProgram" = None, Specialisation26: "courceList_StudyCourceRelation" = None, specialisation: set["courceList_StudyCourceRelation"] = None, cource31: "courceList_StudyProgram" = None, Specialisation35: "courceList_Specialisation" = None, hostSpecialisation: set["courceList_Specialisation"] = None, Specialisation38: "courceList_Specialisation" = None, furtherSpecialisation: "courceList_Specialisation" = None):
        self.name = name
        self.startSemester = startSemester
        self.Specialisation = Specialisation
        self.Specialisation26 = Specialisation26
        self.specialisation = specialisation if specialisation is not None else set()
        self.cource31 = cource31
        self.Specialisation35 = Specialisation35
        self.hostSpecialisation = hostSpecialisation if hostSpecialisation is not None else set()
        self.Specialisation38 = Specialisation38
        self.furtherSpecialisation = furtherSpecialisation
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def startSemester(self) -> int:
        return self.__startSemester

    @startSemester.setter
    def startSemester(self, startSemester: int):
        self.__startSemester = startSemester

    @property
    def hostSpecialisation(self):
        return self.__hostSpecialisation

    @hostSpecialisation.setter
    def hostSpecialisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_Specialisation__hostSpecialisation", None)
        self.__hostSpecialisation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Specialisation35"):
                    opp_val = getattr(item, "Specialisation35", None)
                    
                    if opp_val == self:
                        setattr(item, "Specialisation35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Specialisation35"):
                    opp_val = getattr(item, "Specialisation35", None)
                    
                    setattr(item, "Specialisation35", self)
                    

    @property
    def Specialisation35(self):
        return self.__Specialisation35

    @Specialisation35.setter
    def Specialisation35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_Specialisation__Specialisation35", None)
        self.__Specialisation35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hostSpecialisation"):
                opp_val = getattr(old_value, "hostSpecialisation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hostSpecialisation"):
                opp_val = getattr(value, "hostSpecialisation", None)
                if opp_val is None:
                    setattr(value, "hostSpecialisation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def specialisation(self):
        return self.__specialisation

    @specialisation.setter
    def specialisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_Specialisation__specialisation", None)
        self.__specialisation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StudyCourceRelation"):
                    opp_val = getattr(item, "StudyCourceRelation", None)
                    
                    if opp_val == self:
                        setattr(item, "StudyCourceRelation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StudyCourceRelation"):
                    opp_val = getattr(item, "StudyCourceRelation", None)
                    
                    setattr(item, "StudyCourceRelation", self)
                    

    @property
    def Specialisation38(self):
        return self.__Specialisation38

    @Specialisation38.setter
    def Specialisation38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_Specialisation__Specialisation38", None)
        self.__Specialisation38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "furtherSpecialisation"):
                opp_val = getattr(old_value, "furtherSpecialisation", None)
                if opp_val == self:
                    setattr(old_value, "furtherSpecialisation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "furtherSpecialisation"):
                opp_val = getattr(value, "furtherSpecialisation", None)
                setattr(value, "furtherSpecialisation", self)

    @property
    def furtherSpecialisation(self):
        return self.__furtherSpecialisation

    @furtherSpecialisation.setter
    def furtherSpecialisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_Specialisation__furtherSpecialisation", None)
        self.__furtherSpecialisation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Specialisation38"):
                opp_val = getattr(old_value, "Specialisation38", None)
                if opp_val == self:
                    setattr(old_value, "Specialisation38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Specialisation38"):
                opp_val = getattr(value, "Specialisation38", None)
                setattr(value, "Specialisation38", self)

    @property
    def Specialisation(self):
        return self.__Specialisation

    @Specialisation.setter
    def Specialisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_Specialisation__Specialisation", None)
        self.__Specialisation = value
        
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
    def Specialisation26(self):
        return self.__Specialisation26

    @Specialisation26.setter
    def Specialisation26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_Specialisation__Specialisation26", None)
        self.__Specialisation26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cource25"):
                opp_val = getattr(old_value, "cource25", None)
                if opp_val == self:
                    setattr(old_value, "cource25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cource25"):
                opp_val = getattr(value, "cource25", None)
                setattr(value, "cource25", self)

    @property
    def cource31(self):
        return self.__cource31

    @cource31.setter
    def cource31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_Specialisation__cource31", None)
        self.__cource31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyProgram32"):
                opp_val = getattr(old_value, "StudyProgram32", None)
                if opp_val == self:
                    setattr(old_value, "StudyProgram32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyProgram32"):
                opp_val = getattr(value, "StudyProgram32", None)
                setattr(value, "StudyProgram32", self)

class courceList_StudyProgram:

    def __init__(self, year: int, StudyProgram: "courceList_Student" = None, studyProgram: set["courceList_Specialisation"] = None, studyProgram10: "courceList_StudyGeneralization" = None, studyProgram13: set["courceList_Student"] = None, StudyProgram32: "courceList_Specialisation" = None, StudyProgram47: "courceList_StudyGeneralization" = None):
        self.year = year
        self.StudyProgram = StudyProgram
        self.studyProgram = studyProgram if studyProgram is not None else set()
        self.studyProgram10 = studyProgram10
        self.studyProgram13 = studyProgram13 if studyProgram13 is not None else set()
        self.StudyProgram32 = StudyProgram32
        self.StudyProgram47 = StudyProgram47
        
    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def StudyProgram47(self):
        return self.__StudyProgram47

    @StudyProgram47.setter
    def StudyProgram47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_StudyProgram__StudyProgram47", None)
        self.__StudyProgram47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generalization"):
                opp_val = getattr(old_value, "generalization", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generalization"):
                opp_val = getattr(value, "generalization", None)
                if opp_val is None:
                    setattr(value, "generalization", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StudyProgram32(self):
        return self.__StudyProgram32

    @StudyProgram32.setter
    def StudyProgram32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_StudyProgram__StudyProgram32", None)
        self.__StudyProgram32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cource31"):
                opp_val = getattr(old_value, "cource31", None)
                if opp_val == self:
                    setattr(old_value, "cource31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cource31"):
                opp_val = getattr(value, "cource31", None)
                setattr(value, "cource31", self)

    @property
    def studyProgram10(self):
        return self.__studyProgram10

    @studyProgram10.setter
    def studyProgram10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_StudyProgram__studyProgram10", None)
        self.__studyProgram10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyGeneralization11"):
                opp_val = getattr(old_value, "StudyGeneralization11", None)
                if opp_val == self:
                    setattr(old_value, "StudyGeneralization11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyGeneralization11"):
                opp_val = getattr(value, "StudyGeneralization11", None)
                setattr(value, "StudyGeneralization11", self)

    @property
    def studyProgram13(self):
        return self.__studyProgram13

    @studyProgram13.setter
    def studyProgram13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_StudyProgram__studyProgram13", None)
        self.__studyProgram13 = value if value is not None else set()
        
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
                    

    @property
    def studyProgram(self):
        return self.__studyProgram

    @studyProgram.setter
    def studyProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_StudyProgram__studyProgram", None)
        self.__studyProgram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Specialisation"):
                    opp_val = getattr(item, "Specialisation", None)
                    
                    if opp_val == self:
                        setattr(item, "Specialisation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Specialisation"):
                    opp_val = getattr(item, "Specialisation", None)
                    
                    setattr(item, "Specialisation", self)
                    

    @property
    def StudyProgram(self):
        return self.__StudyProgram

    @StudyProgram.setter
    def StudyProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_StudyProgram__StudyProgram", None)
        self.__StudyProgram = value
        
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

class courceList_Student:

    def __init__(self, nr: int, student: "courceList_StudyProgram" = None, Student: "courceList_StudyProgram" = None):
        self.nr = nr
        self.student = student
        self.Student = Student
        
    @property
    def nr(self) -> int:
        return self.__nr

    @nr.setter
    def nr(self, nr: int):
        self.__nr = nr

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_Student__student", None)
        self.__student = value
        
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
    def Student(self):
        return self.__Student

    @Student.setter
    def Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_Student__Student", None)
        self.__Student = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyProgram13"):
                opp_val = getattr(old_value, "studyProgram13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyProgram13"):
                opp_val = getattr(value, "studyProgram13", None)
                if opp_val is None:
                    setattr(value, "studyProgram13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class courceList_CourceSpecification:

    def __init__(self, specificationYear: int, semester: str, language: str, version: str, credits: float, name: str, CourceSpecification: "courceList_Cource" = None, CourceSpecification20: "courceList_EvaluationForm" = None, courceList_CourceSpecification: "courceList_StudyCourceRelation" = None, corseSpecifications: "courceList_Cource" = None, courceList_CourceSpecification42: "courceList_Professor" = None, cource44: "courceList_EvaluationForm" = None):
        self.specificationYear = specificationYear
        self.semester = semester
        self.language = language
        self.version = version
        self.credits = credits
        self.name = name
        self.CourceSpecification = CourceSpecification
        self.CourceSpecification20 = CourceSpecification20
        self.courceList_CourceSpecification = courceList_CourceSpecification
        self.corseSpecifications = corseSpecifications
        self.courceList_CourceSpecification42 = courceList_CourceSpecification42
        self.cource44 = cource44
        
    @property
    def semester(self) -> str:
        return self.__semester

    @semester.setter
    def semester(self, semester: str):
        self.__semester = semester

    @property
    def credits(self) -> float:
        return self.__credits

    @credits.setter
    def credits(self, credits: float):
        self.__credits = credits

    @property
    def specificationYear(self) -> int:
        return self.__specificationYear

    @specificationYear.setter
    def specificationYear(self, specificationYear: int):
        self.__specificationYear = specificationYear

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def courceList_CourceSpecification42(self):
        return self.__courceList_CourceSpecification42

    @courceList_CourceSpecification42.setter
    def courceList_CourceSpecification42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_CourceSpecification__courceList_CourceSpecification42", None)
        self.__courceList_CourceSpecification42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courceList_Professor"):
                opp_val = getattr(old_value, "courceList_Professor", None)
                if opp_val == self:
                    setattr(old_value, "courceList_Professor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courceList_Professor"):
                opp_val = getattr(value, "courceList_Professor", None)
                setattr(value, "courceList_Professor", self)

    @property
    def CourceSpecification(self):
        return self.__CourceSpecification

    @CourceSpecification.setter
    def CourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_CourceSpecification__CourceSpecification", None)
        self.__CourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cource"):
                opp_val = getattr(old_value, "cource", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cource"):
                opp_val = getattr(value, "cource", None)
                if opp_val is None:
                    setattr(value, "cource", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cource44(self):
        return self.__cource44

    @cource44.setter
    def cource44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_CourceSpecification__cource44", None)
        self.__cource44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EvaluationForm45"):
                opp_val = getattr(old_value, "EvaluationForm45", None)
                if opp_val == self:
                    setattr(old_value, "EvaluationForm45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EvaluationForm45"):
                opp_val = getattr(value, "EvaluationForm45", None)
                setattr(value, "EvaluationForm45", self)

    @property
    def corseSpecifications(self):
        return self.__corseSpecifications

    @corseSpecifications.setter
    def corseSpecifications(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_CourceSpecification__corseSpecifications", None)
        self.__corseSpecifications = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Cource40"):
                opp_val = getattr(old_value, "Cource40", None)
                if opp_val == self:
                    setattr(old_value, "Cource40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Cource40"):
                opp_val = getattr(value, "Cource40", None)
                setattr(value, "Cource40", self)

    @property
    def CourceSpecification20(self):
        return self.__CourceSpecification20

    @CourceSpecification20.setter
    def CourceSpecification20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_CourceSpecification__CourceSpecification20", None)
        self.__CourceSpecification20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "evaluationForm19"):
                opp_val = getattr(old_value, "evaluationForm19", None)
                if opp_val == self:
                    setattr(old_value, "evaluationForm19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "evaluationForm19"):
                opp_val = getattr(value, "evaluationForm19", None)
                setattr(value, "evaluationForm19", self)

    @property
    def courceList_CourceSpecification(self):
        return self.__courceList_CourceSpecification

    @courceList_CourceSpecification.setter
    def courceList_CourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_CourceSpecification__courceList_CourceSpecification", None)
        self.__courceList_CourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courceList_StudyCourceRelation"):
                opp_val = getattr(old_value, "courceList_StudyCourceRelation", None)
                if opp_val == self:
                    setattr(old_value, "courceList_StudyCourceRelation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courceList_StudyCourceRelation"):
                opp_val = getattr(value, "courceList_StudyCourceRelation", None)
                setattr(value, "courceList_StudyCourceRelation", self)

class courceList_Professor:

    def __init__(self, name: str, title: str, Professor: "courceList_Department" = None, professor: "courceList_Department" = None, courceList_Professor: "courceList_CourceSpecification" = None):
        self.name = name
        self.title = title
        self.Professor = Professor
        self.professor = professor
        self.courceList_Professor = courceList_Professor
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def professor(self):
        return self.__professor

    @professor.setter
    def professor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_Professor__professor", None)
        self.__professor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Department28"):
                opp_val = getattr(old_value, "Department28", None)
                if opp_val == self:
                    setattr(old_value, "Department28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Department28"):
                opp_val = getattr(value, "Department28", None)
                setattr(value, "Department28", self)

    @property
    def courceList_Professor(self):
        return self.__courceList_Professor

    @courceList_Professor.setter
    def courceList_Professor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_Professor__courceList_Professor", None)
        self.__courceList_Professor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courceList_CourceSpecification42"):
                opp_val = getattr(old_value, "courceList_CourceSpecification42", None)
                if opp_val == self:
                    setattr(old_value, "courceList_CourceSpecification42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courceList_CourceSpecification42"):
                opp_val = getattr(value, "courceList_CourceSpecification42", None)
                setattr(value, "courceList_CourceSpecification42", self)

    @property
    def Professor(self):
        return self.__Professor

    @Professor.setter
    def Professor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_Professor__Professor", None)
        self.__Professor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department4"):
                opp_val = getattr(old_value, "department4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department4"):
                opp_val = getattr(value, "department4", None)
                if opp_val is None:
                    setattr(value, "department4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class courceList_Cource:

    def __init__(self, code: str, name: str, location: str, Cource: "courceList_Department" = None, cource: set["courceList_CourceSpecification"] = None, course: "courceList_Department" = None, Cource40: "courceList_CourceSpecification" = None):
        self.code = code
        self.name = name
        self.location = location
        self.Cource = Cource
        self.cource = cource if cource is not None else set()
        self.course = course
        self.Cource40 = Cource40
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Cource40(self):
        return self.__Cource40

    @Cource40.setter
    def Cource40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_Cource__Cource40", None)
        self.__Cource40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "corseSpecifications"):
                opp_val = getattr(old_value, "corseSpecifications", None)
                if opp_val == self:
                    setattr(old_value, "corseSpecifications", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "corseSpecifications"):
                opp_val = getattr(value, "corseSpecifications", None)
                setattr(value, "corseSpecifications", self)

    @property
    def Cource(self):
        return self.__Cource

    @Cource.setter
    def Cource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_Cource__Cource", None)
        self.__Cource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department2"):
                opp_val = getattr(old_value, "department2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department2"):
                opp_val = getattr(value, "department2", None)
                if opp_val is None:
                    setattr(value, "department2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_Cource__course", None)
        self.__course = value
        
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
    def cource(self):
        return self.__cource

    @cource.setter
    def cource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_Cource__cource", None)
        self.__cource = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CourceSpecification"):
                    opp_val = getattr(item, "CourceSpecification", None)
                    
                    if opp_val == self:
                        setattr(item, "CourceSpecification", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CourceSpecification"):
                    opp_val = getattr(item, "CourceSpecification", None)
                    
                    setattr(item, "CourceSpecification", self)
                    

class courceList_StudyGeneralization:

    def __init__(self, name: str, educationLevel: str, nrOfYears: int, campus: str, abbreviation: str, StudyGeneralization: "courceList_Department" = None, StudyGeneralization11: "courceList_StudyProgram" = None, generalization: set["courceList_StudyProgram"] = None, studyProgram49: "courceList_Department" = None):
        self.name = name
        self.educationLevel = educationLevel
        self.nrOfYears = nrOfYears
        self.campus = campus
        self.abbreviation = abbreviation
        self.StudyGeneralization = StudyGeneralization
        self.StudyGeneralization11 = StudyGeneralization11
        self.generalization = generalization if generalization is not None else set()
        self.studyProgram49 = studyProgram49
        
    @property
    def campus(self) -> str:
        return self.__campus

    @campus.setter
    def campus(self, campus: str):
        self.__campus = campus

    @property
    def educationLevel(self) -> str:
        return self.__educationLevel

    @educationLevel.setter
    def educationLevel(self, educationLevel: str):
        self.__educationLevel = educationLevel

    @property
    def abbreviation(self) -> str:
        return self.__abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation: str):
        self.__abbreviation = abbreviation

    @property
    def nrOfYears(self) -> int:
        return self.__nrOfYears

    @nrOfYears.setter
    def nrOfYears(self, nrOfYears: int):
        self.__nrOfYears = nrOfYears

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def StudyGeneralization(self):
        return self.__StudyGeneralization

    @StudyGeneralization.setter
    def StudyGeneralization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_StudyGeneralization__StudyGeneralization", None)
        self.__StudyGeneralization = value
        
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
    def generalization(self):
        return self.__generalization

    @generalization.setter
    def generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_StudyGeneralization__generalization", None)
        self.__generalization = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StudyProgram47"):
                    opp_val = getattr(item, "StudyProgram47", None)
                    
                    if opp_val == self:
                        setattr(item, "StudyProgram47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StudyProgram47"):
                    opp_val = getattr(item, "StudyProgram47", None)
                    
                    setattr(item, "StudyProgram47", self)
                    

    @property
    def StudyGeneralization11(self):
        return self.__StudyGeneralization11

    @StudyGeneralization11.setter
    def StudyGeneralization11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_StudyGeneralization__StudyGeneralization11", None)
        self.__StudyGeneralization11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyProgram10"):
                opp_val = getattr(old_value, "studyProgram10", None)
                if opp_val == self:
                    setattr(old_value, "studyProgram10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyProgram10"):
                opp_val = getattr(value, "studyProgram10", None)
                setattr(value, "studyProgram10", self)

    @property
    def studyProgram49(self):
        return self.__studyProgram49

    @studyProgram49.setter
    def studyProgram49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_StudyGeneralization__studyProgram49", None)
        self.__studyProgram49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Department50"):
                opp_val = getattr(old_value, "Department50", None)
                if opp_val == self:
                    setattr(old_value, "Department50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Department50"):
                opp_val = getattr(value, "Department50", None)
                setattr(value, "Department50", self)

class courceList_Department:

    def __init__(self, name: str, abbreviation: str, department: set["courceList_StudyGeneralization"] = None, department2: set["courceList_Cource"] = None, department4: set["courceList_Professor"] = None, Department: "courceList_Cource" = None, Department28: "courceList_Professor" = None, Department50: "courceList_StudyGeneralization" = None):
        self.name = name
        self.abbreviation = abbreviation
        self.department = department if department is not None else set()
        self.department2 = department2 if department2 is not None else set()
        self.department4 = department4 if department4 is not None else set()
        self.Department = Department
        self.Department28 = Department28
        self.Department50 = Department50
        
    @property
    def abbreviation(self) -> str:
        return self.__abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation: str):
        self.__abbreviation = abbreviation

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_Department__department", None)
        self.__department = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StudyGeneralization"):
                    opp_val = getattr(item, "StudyGeneralization", None)
                    
                    if opp_val == self:
                        setattr(item, "StudyGeneralization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StudyGeneralization"):
                    opp_val = getattr(item, "StudyGeneralization", None)
                    
                    setattr(item, "StudyGeneralization", self)
                    

    @property
    def Department28(self):
        return self.__Department28

    @Department28.setter
    def Department28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_Department__Department28", None)
        self.__Department28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "professor"):
                opp_val = getattr(old_value, "professor", None)
                if opp_val == self:
                    setattr(old_value, "professor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "professor"):
                opp_val = getattr(value, "professor", None)
                setattr(value, "professor", self)

    @property
    def department4(self):
        return self.__department4

    @department4.setter
    def department4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_Department__department4", None)
        self.__department4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Professor"):
                    opp_val = getattr(item, "Professor", None)
                    
                    if opp_val == self:
                        setattr(item, "Professor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Professor"):
                    opp_val = getattr(item, "Professor", None)
                    
                    setattr(item, "Professor", self)
                    

    @property
    def Department(self):
        return self.__Department

    @Department.setter
    def Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_Department__Department", None)
        self.__Department = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course"):
                opp_val = getattr(old_value, "course", None)
                if opp_val == self:
                    setattr(old_value, "course", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course"):
                opp_val = getattr(value, "course", None)
                setattr(value, "course", self)

    @property
    def department2(self):
        return self.__department2

    @department2.setter
    def department2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_Department__department2", None)
        self.__department2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Cource"):
                    opp_val = getattr(item, "Cource", None)
                    
                    if opp_val == self:
                        setattr(item, "Cource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Cource"):
                    opp_val = getattr(item, "Cource", None)
                    
                    setattr(item, "Cource", self)
                    

    @property
    def Department50(self):
        return self.__Department50

    @Department50.setter
    def Department50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_courceList_Department__Department50", None)
        self.__Department50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyProgram49"):
                opp_val = getattr(old_value, "studyProgram49", None)
                if opp_val == self:
                    setattr(old_value, "studyProgram49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyProgram49"):
                opp_val = getattr(value, "studyProgram49", None)
                setattr(value, "studyProgram49", self)
