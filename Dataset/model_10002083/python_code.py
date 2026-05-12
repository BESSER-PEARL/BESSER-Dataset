from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Class:

    pass


class mypackage_Exceptions:

    pass


class mypackage_Book:

    def __init__(self, BName: str, BId: str, Price: str, course15: "mypackage_Course" = None, fileManager16: "mypackage_FileManager" = None):
        self.BName = BName
        self.BId = BId
        self.Price = Price
        self.course15 = course15
        self.fileManager16 = fileManager16
        
        pass
    @property
    def BName(self):
        return self.__BName
    @BName.setter
    def BName(self, BName: str):
        self.__BName = BName

    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, Price: str):
        self.__Price = Price

    @property
    def BId(self):
        return self.__BId
    @BId.setter
    def BId(self, BId: str):
        self.__BId = BId

    @property
    def fileManager16(self):
        return self.__fileManager16
    @fileManager16.setter
    def fileManager16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mypackage_Book__fileManager16", None)
        self.__fileManager16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book17"):
                opp_val = getattr(old_value, "book17", None)
                if opp_val == self:
                    setattr(old_value, "book17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book17"):
                opp_val = getattr(value, "book17", None)
                setattr(value, "book17", self)

    @property
    def course15(self):
        return self.__course15
    @course15.setter
    def course15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mypackage_Book__course15", None)
        self.__course15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book14"):
                opp_val = getattr(old_value, "book14", None)
                if opp_val == self:
                    setattr(old_value, "book14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book14"):
                opp_val = getattr(value, "book14", None)
                setattr(value, "book14", self)



class mypackage_Assignment:

    def __init__(self, number: int, StrartDate: str, Deadline: str, course9: "mypackage_Course" = None, tutor11: "mypackage_Tutor" = None, student13: "mypackage_Student" = None):
        self.number = number
        self.StrartDate = StrartDate
        self.Deadline = Deadline
        self.course9 = course9
        self.tutor11 = tutor11
        self.student13 = student13
        
        pass
    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def StrartDate(self):
        return self.__StrartDate
    @StrartDate.setter
    def StrartDate(self, StrartDate: str):
        self.__StrartDate = StrartDate

    @property
    def Deadline(self):
        return self.__Deadline
    @Deadline.setter
    def Deadline(self, Deadline: str):
        self.__Deadline = Deadline

    @property
    def course9(self):
        return self.__course9
    @course9.setter
    def course9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mypackage_Assignment__course9", None)
        self.__course9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assignment8"):
                opp_val = getattr(old_value, "assignment8", None)
                if opp_val == self:
                    setattr(old_value, "assignment8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assignment8"):
                opp_val = getattr(value, "assignment8", None)
                setattr(value, "assignment8", self)

    @property
    def tutor11(self):
        return self.__tutor11
    @tutor11.setter
    def tutor11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mypackage_Assignment__tutor11", None)
        self.__tutor11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assignment10"):
                opp_val = getattr(old_value, "assignment10", None)
                if opp_val == self:
                    setattr(old_value, "assignment10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assignment10"):
                opp_val = getattr(value, "assignment10", None)
                setattr(value, "assignment10", self)

    @property
    def student13(self):
        return self.__student13
    @student13.setter
    def student13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mypackage_Assignment__student13", None)
        self.__student13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assignment12"):
                opp_val = getattr(old_value, "assignment12", None)
                if opp_val == self:
                    setattr(old_value, "assignment12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assignment12"):
                opp_val = getattr(value, "assignment12", None)
                setattr(value, "assignment12", self)



class mypackage_FileManager:

    pass


class mypackage_Exam:

    def __init__(self, EName: str, EId: str, MaxGrade: str, ExamsFileName: str, course1: "mypackage_Course" = None, fileManager7: "mypackage_FileManager" = None):
        self.EName = EName
        self.EId = EId
        self.MaxGrade = MaxGrade
        self.ExamsFileName = ExamsFileName
        self.course1 = course1
        self.fileManager7 = fileManager7
        
        pass
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
    def EId(self):
        return self.__EId
    @EId.setter
    def EId(self, EId: str):
        self.__EId = EId

    @property
    def EName(self):
        return self.__EName
    @EName.setter
    def EName(self, EName: str):
        self.__EName = EName

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



class mypackage_Course:

    def __init__(self, CreditHours: int, CName: str, CourseFileName: str, CId: str, exam0: "mypackage_Exam" = None, assignment8: "mypackage_Assignment" = None, book14: "mypackage_Book" = None, fileManager5: "mypackage_FileManager" = None):
        self.CreditHours = CreditHours
        self.CName = CName
        self.CourseFileName = CourseFileName
        self.CId = CId
        self.exam0 = exam0
        self.assignment8 = assignment8
        self.book14 = book14
        self.fileManager5 = fileManager5
        
        pass
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
    def CourseFileName(self):
        return self.__CourseFileName
    @CourseFileName.setter
    def CourseFileName(self, CourseFileName: str):
        self.__CourseFileName = CourseFileName

    @property
    def CId(self):
        return self.__CId
    @CId.setter
    def CId(self, CId: str):
        self.__CId = CId

    @property
    def book14(self):
        return self.__book14
    @book14.setter
    def book14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mypackage_Course__book14", None)
        self.__book14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course15"):
                opp_val = getattr(old_value, "course15", None)
                if opp_val == self:
                    setattr(old_value, "course15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course15"):
                opp_val = getattr(value, "course15", None)
                setattr(value, "course15", self)

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
    def assignment8(self):
        return self.__assignment8
    @assignment8.setter
    def assignment8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mypackage_Course__assignment8", None)
        self.__assignment8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course9"):
                opp_val = getattr(old_value, "course9", None)
                if opp_val == self:
                    setattr(old_value, "course9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course9"):
                opp_val = getattr(value, "course9", None)
                setattr(value, "course9", self)



class mypackage_Admin:

    pass


class mypackage_Tutor:

    def __init__(self, TutorFileName: str, WorkingHours: str, assignment10: "mypackage_Assignment" = None):
        self.TutorFileName = TutorFileName
        self.WorkingHours = WorkingHours
        self.assignment10 = assignment10
        
        pass
    @property
    def WorkingHours(self):
        return self.__WorkingHours
    @WorkingHours.setter
    def WorkingHours(self, WorkingHours: str):
        self.__WorkingHours = WorkingHours

    @property
    def TutorFileName(self):
        return self.__TutorFileName
    @TutorFileName.setter
    def TutorFileName(self, TutorFileName: str):
        self.__TutorFileName = TutorFileName

    @property
    def assignment10(self):
        return self.__assignment10
    @assignment10.setter
    def assignment10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mypackage_Tutor__assignment10", None)
        self.__assignment10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tutor11"):
                opp_val = getattr(old_value, "tutor11", None)
                if opp_val == self:
                    setattr(old_value, "tutor11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tutor11"):
                opp_val = getattr(value, "tutor11", None)
                setattr(value, "tutor11", self)



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

    def __init__(self, level: int, grade: str, studentFileName: str, assignment12: "mypackage_Assignment" = None):
        self.level = level
        self.grade = grade
        self.studentFileName = studentFileName
        self.assignment12 = assignment12
        
        pass
    @property
    def grade(self):
        return self.__grade
    @grade.setter
    def grade(self, grade: str):
        self.__grade = grade

    @property
    def level(self):
        return self.__level
    @level.setter
    def level(self, level: int):
        self.__level = level

    @property
    def studentFileName(self):
        return self.__studentFileName
    @studentFileName.setter
    def studentFileName(self, studentFileName: str):
        self.__studentFileName = studentFileName

    @property
    def assignment12(self):
        return self.__assignment12
    @assignment12.setter
    def assignment12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mypackage_Student__assignment12", None)
        self.__assignment12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student13"):
                opp_val = getattr(old_value, "student13", None)
                if opp_val == self:
                    setattr(old_value, "student13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student13"):
                opp_val = getattr(value, "student13", None)
                setattr(value, "student13", self)



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

    def __init__(self, id: int, UserName: str, fName: str, lname: str, age: int, Pass: str, fileManager3: "mypackage_FileManager" = None):
        self.id = id
        self.UserName = UserName
        self.fName = fName
        self.lname = lname
        self.age = age
        self.Pass = Pass
        self.fileManager3 = fileManager3
        
        pass
    @property
    def lname(self):
        return self.__lname
    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

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
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def Pass(self):
        return self.__Pass
    @Pass.setter
    def Pass(self, Pass: str):
        self.__Pass = Pass

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

