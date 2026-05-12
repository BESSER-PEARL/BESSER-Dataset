from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Student:

    def __init__(self, s_age: int, grade: str, studentfname: str, fileBinary10: "FileBinary" = None):
        self.s_age = s_age
        self.grade = grade
        self.studentfname = studentfname
        self.fileBinary10 = fileBinary10
        
        pass
    @property
    def grade(self):
        return self.__grade
    @grade.setter
    def grade(self, grade: str):
        self.__grade = grade

    @property
    def s_age(self):
        return self.__s_age
    @s_age.setter
    def s_age(self, s_age: int):
        self.__s_age = s_age

    @property
    def studentfname(self):
        return self.__studentfname
    @studentfname.setter
    def studentfname(self, studentfname: str):
        self.__studentfname = studentfname

    @property
    def fileBinary10(self):
        return self.__fileBinary10
    @fileBinary10.setter
    def fileBinary10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__fileBinary10", None)
        self.__fileBinary10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student11"):
                opp_val = getattr(old_value, "student11", None)
                if opp_val == self:
                    setattr(old_value, "student11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student11"):
                opp_val = getattr(value, "student11", None)
                setattr(value, "student11", self)



class Person:

    def __init__(self, id: str, phNum: str, PersonFName: str):
        self.id = id
        self.phNum = phNum
        self.PersonFName = PersonFName
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def PersonFName(self):
        return self.__PersonFName
    @PersonFName.setter
    def PersonFName(self, PersonFName: str):
        self.__PersonFName = PersonFName

    @property
    def phNum(self):
        return self.__phNum
    @phNum.setter
    def phNum(self, phNum: str):
        self.__phNum = phNum



class Insturctor:

    def __init__(self, INfilename: str, fileBinary8: "FileBinary" = None):
        self.INfilename = INfilename
        self.fileBinary8 = fileBinary8
        
        pass
    @property
    def INfilename(self):
        return self.__INfilename
    @INfilename.setter
    def INfilename(self, INfilename: str):
        self.__INfilename = INfilename

    @property
    def fileBinary8(self):
        return self.__fileBinary8
    @fileBinary8.setter
    def fileBinary8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Insturctor__fileBinary8", None)
        self.__fileBinary8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "insturctor9"):
                opp_val = getattr(old_value, "insturctor9", None)
                if opp_val == self:
                    setattr(old_value, "insturctor9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "insturctor9"):
                opp_val = getattr(value, "insturctor9", None)
                setattr(value, "insturctor9", self)



class Finance:

    def __init__(self, Cname: str, coast: str):
        self.Cname = Cname
        self.coast = coast
        
        pass
    @property
    def coast(self):
        return self.__coast
    @coast.setter
    def coast(self, coast: str):
        self.__coast = coast

    @property
    def Cname(self):
        return self.__Cname
    @Cname.setter
    def Cname(self, Cname: str):
        self.__Cname = Cname



class ILogin_Interface:

    pass


class FileBinary:

    pass


class Email:

    def __init__(self, Email: str, fileBinary6: "FileBinary" = None):
        self.Email = Email
        self.fileBinary6 = fileBinary6
        
        pass
    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def fileBinary6(self):
        return self.__fileBinary6
    @fileBinary6.setter
    def fileBinary6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Email__fileBinary6", None)
        self.__fileBinary6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "email7"):
                opp_val = getattr(old_value, "email7", None)
                if opp_val == self:
                    setattr(old_value, "email7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "email7"):
                opp_val = getattr(value, "email7", None)
                setattr(value, "email7", self)



class Exam:

    def __init__(self, EID: str, EName: str, ETIME: str, Exam_File_Name: str, MaxGrade: str, course0: "Course" = None, fileBinary2: "FileBinary" = None):
        self.EID = EID
        self.EName = EName
        self.ETIME = ETIME
        self.Exam_File_Name = Exam_File_Name
        self.MaxGrade = MaxGrade
        self.course0 = course0
        self.fileBinary2 = fileBinary2
        
        pass
    @property
    def Exam_File_Name(self):
        return self.__Exam_File_Name
    @Exam_File_Name.setter
    def Exam_File_Name(self, Exam_File_Name: str):
        self.__Exam_File_Name = Exam_File_Name

    @property
    def ETIME(self):
        return self.__ETIME
    @ETIME.setter
    def ETIME(self, ETIME: str):
        self.__ETIME = ETIME

    @property
    def EID(self):
        return self.__EID
    @EID.setter
    def EID(self, EID: str):
        self.__EID = EID

    @property
    def MaxGrade(self):
        return self.__MaxGrade
    @MaxGrade.setter
    def MaxGrade(self, MaxGrade: str):
        self.__MaxGrade = MaxGrade

    @property
    def EName(self):
        return self.__EName
    @EName.setter
    def EName(self, EName: str):
        self.__EName = EName

    @property
    def fileBinary2(self):
        return self.__fileBinary2
    @fileBinary2.setter
    def fileBinary2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Exam__fileBinary2", None)
        self.__fileBinary2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exam3"):
                opp_val = getattr(old_value, "exam3", None)
                if opp_val == self:
                    setattr(old_value, "exam3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exam3"):
                opp_val = getattr(value, "exam3", None)
                setattr(value, "exam3", self)

    @property
    def course0(self):
        return self.__course0
    @course0.setter
    def course0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Exam__course0", None)
        self.__course0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exam1"):
                opp_val = getattr(old_value, "exam1", None)
                if opp_val == self:
                    setattr(old_value, "exam1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exam1"):
                opp_val = getattr(value, "exam1", None)
                setattr(value, "exam1", self)



class Course:

    def __init__(self, Course_File_Name: str, Course_REG: str, Cprice: str, CTutor: str, Cid: str, Cname: str, fileBinary4: "FileBinary" = None, exam1: "Exam" = None):
        self.Course_File_Name = Course_File_Name
        self.Course_REG = Course_REG
        self.Cprice = Cprice
        self.CTutor = CTutor
        self.Cid = Cid
        self.Cname = Cname
        self.fileBinary4 = fileBinary4
        self.exam1 = exam1
        
        pass
    @property
    def Cid(self):
        return self.__Cid
    @Cid.setter
    def Cid(self, Cid: str):
        self.__Cid = Cid

    @property
    def CTutor(self):
        return self.__CTutor
    @CTutor.setter
    def CTutor(self, CTutor: str):
        self.__CTutor = CTutor

    @property
    def Cname(self):
        return self.__Cname
    @Cname.setter
    def Cname(self, Cname: str):
        self.__Cname = Cname

    @property
    def Course_File_Name(self):
        return self.__Course_File_Name
    @Course_File_Name.setter
    def Course_File_Name(self, Course_File_Name: str):
        self.__Course_File_Name = Course_File_Name

    @property
    def Cprice(self):
        return self.__Cprice
    @Cprice.setter
    def Cprice(self, Cprice: str):
        self.__Cprice = Cprice

    @property
    def Course_REG(self):
        return self.__Course_REG
    @Course_REG.setter
    def Course_REG(self, Course_REG: str):
        self.__Course_REG = Course_REG

    @property
    def exam1(self):
        return self.__exam1
    @exam1.setter
    def exam1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Course__exam1", None)
        self.__exam1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course0"):
                opp_val = getattr(old_value, "course0", None)
                if opp_val == self:
                    setattr(old_value, "course0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course0"):
                opp_val = getattr(value, "course0", None)
                setattr(value, "course0", self)

    @property
    def fileBinary4(self):
        return self.__fileBinary4
    @fileBinary4.setter
    def fileBinary4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Course__fileBinary4", None)
        self.__fileBinary4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course5"):
                opp_val = getattr(old_value, "course5", None)
                if opp_val == self:
                    setattr(old_value, "course5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course5"):
                opp_val = getattr(value, "course5", None)
                setattr(value, "course5", self)



class Admin:

    def __init__(self, AdminFileName: str):
        self.AdminFileName = AdminFileName
        
        pass
    @property
    def AdminFileName(self):
        return self.__AdminFileName
    @AdminFileName.setter
    def AdminFileName(self, AdminFileName: str):
        self.__AdminFileName = AdminFileName

