from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class mypackage_FileManager:

    pass


class mypackage_Exam:

    def __init__(self, EName: str, MaxGrade: str, ExamsFileName: str, EId: str, course1: "mypackage_Course" = None, fileManager7: "mypackage_FileManager" = None):
        self.EName = EName
        self.MaxGrade = MaxGrade
        self.ExamsFileName = ExamsFileName
        self.EId = EId
        self.course1 = course1
        self.fileManager7 = fileManager7
        
        pass
    @property
    def EName(self):
        return self.__EName
    @EName.setter
    def EName(self, EName: str):
        self.__EName = EName

    @property
    def EId(self):
        return self.__EId
    @EId.setter
    def EId(self, EId: str):
        self.__EId = EId

    @property
    def ExamsFileName(self):
        return self.__ExamsFileName
    @ExamsFileName.setter
    def ExamsFileName(self, ExamsFileName: str):
        self.__ExamsFileName = ExamsFileName

    @property
    def MaxGrade(self):
        return self.__MaxGrade
    @MaxGrade.setter
    def MaxGrade(self, MaxGrade: str):
        self.__MaxGrade = MaxGrade

    @property
    def fileManager7(self):
        return self.__fileManager7
    @fileManager7.setter
    def fileManager7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mypackage_Exam__fileManager7", None)
        self.__fileManager7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exam6"):
                opp_val = getattr(old_value, "exam6", None)
                if opp_val == self:
                    setattr(old_value, "exam6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exam6"):
                opp_val = getattr(value, "exam6", None)
                setattr(value, "exam6", self)

    @property
    def course1(self):
        return self.__course1
    @course1.setter
    def course1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mypackage_Exam__course1", None)
        self.__course1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exam0"):
                opp_val = getattr(old_value, "exam0", None)
                if opp_val == self:
                    setattr(old_value, "exam0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exam0"):
                opp_val = getattr(value, "exam0", None)
                setattr(value, "exam0", self)



class mypackage_Course:

    def __init__(self, CreditHours: int, CName: str, CourseFileName: str, CId: str, exam0: "mypackage_Exam" = None, fileManager5: "mypackage_FileManager" = None):
        self.CreditHours = CreditHours
        self.CName = CName
        self.CourseFileName = CourseFileName
        self.CId = CId
        self.exam0 = exam0
        self.fileManager5 = fileManager5
        
        pass
    @property
    def CId(self):
        return self.__CId
    @CId.setter
    def CId(self, CId: str):
        self.__CId = CId

    @property
    def CourseFileName(self):
        return self.__CourseFileName
    @CourseFileName.setter
    def CourseFileName(self, CourseFileName: str):
        self.__CourseFileName = CourseFileName

    @property
    def CreditHours(self):
        return self.__CreditHours
    @CreditHours.setter
    def CreditHours(self, CreditHours: int):
        self.__CreditHours = CreditHours

    @property
    def CName(self):
        return self.__CName
    @CName.setter
    def CName(self, CName: str):
        self.__CName = CName

    @property
    def exam0(self):
        return self.__exam0
    @exam0.setter
    def exam0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mypackage_Course__exam0", None)
        self.__exam0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course1"):
                opp_val = getattr(old_value, "course1", None)
                if opp_val == self:
                    setattr(old_value, "course1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course1"):
                opp_val = getattr(value, "course1", None)
                setattr(value, "course1", self)

    @property
    def fileManager5(self):
        return self.__fileManager5
    @fileManager5.setter
    def fileManager5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mypackage_Course__fileManager5", None)
        self.__fileManager5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course4"):
                opp_val = getattr(old_value, "course4", None)
                if opp_val == self:
                    setattr(old_value, "course4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course4"):
                opp_val = getattr(value, "course4", None)
                setattr(value, "course4", self)



class mypackage_Admin:

    pass


class mypackage_Tutor:

    def __init__(self, TutorFileName: str, academicalHours: str):
        self.TutorFileName = TutorFileName
        self.academicalHours = academicalHours
        
        pass
    @property
    def academicalHours(self):
        return self.__academicalHours
    @academicalHours.setter
    def academicalHours(self, academicalHours: str):
        self.__academicalHours = academicalHours

    @property
    def TutorFileName(self):
        return self.__TutorFileName
    @TutorFileName.setter
    def TutorFileName(self, TutorFileName: str):
        self.__TutorFileName = TutorFileName



class mypackage_studentAffairsEmp:

    def __init__(self, EmpFileName: str):
        self.EmpFileName = EmpFileName
        
        pass
    @property
    def EmpFileName(self):
        return self.__EmpFileName
    @EmpFileName.setter
    def EmpFileName(self, EmpFileName: str):
        self.__EmpFileName = EmpFileName



class mypackage_Student:

    def __init__(self, level: int, grade: str, studentFileName: str):
        self.level = level
        self.grade = grade
        self.studentFileName = studentFileName
        
        pass
    @property
    def studentFileName(self):
        return self.__studentFileName
    @studentFileName.setter
    def studentFileName(self, studentFileName: str):
        self.__studentFileName = studentFileName

    @property
    def level(self):
        return self.__level
    @level.setter
    def level(self, level: int):
        self.__level = level

    @property
    def grade(self):
        return self.__grade
    @grade.setter
    def grade(self, grade: str):
        self.__grade = grade



class mypackage_Staff:

    def __init__(self, salary: str):
        self.salary = salary
        
        pass
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, salary: str):
        self.__salary = salary



class mypackage_Perosn:

    def __init__(self, id: int, UserName: str, fName: str, lname: str, age: int, fileManager3: "mypackage_FileManager" = None):
        self.id = id
        self.UserName = UserName
        self.fName = fName
        self.lname = lname
        self.age = age
        self.fileManager3 = fileManager3
        
        pass
    @property
    def lname(self):
        return self.__lname
    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def fName(self):
        return self.__fName
    @fName.setter
    def fName(self, fName: str):
        self.__fName = fName

    @property
    def UserName(self):
        return self.__UserName
    @UserName.setter
    def UserName(self, UserName: str):
        self.__UserName = UserName

    @property
    def fileManager3(self):
        return self.__fileManager3
    @fileManager3.setter
    def fileManager3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mypackage_Perosn__fileManager3", None)
        self.__fileManager3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "perosn2"):
                opp_val = getattr(old_value, "perosn2", None)
                if opp_val == self:
                    setattr(old_value, "perosn2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "perosn2"):
                opp_val = getattr(value, "perosn2", None)
                setattr(value, "perosn2", self)

