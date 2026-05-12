from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Insturctor:

    def __init__(self, INfilename: str):
        self.INfilename = INfilename
        
        pass
    @property
    def INfilename(self):
        return self.__INfilename
    @INfilename.setter
    def INfilename(self, INfilename: str):
        self.__INfilename = INfilename



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



class Exceptions:

    pass


class ILogin_Interface:

    pass


class FileBinary:

    pass


class Email:

    def __init__(self, Email: str):
        self.Email = Email
        
        pass
    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email



class Exam:

    def __init__(self, EID: str, EName: str, ETIME: str, Exam_File_Name: str, MaxGrade: str):
        self.EID = EID
        self.EName = EName
        self.ETIME = ETIME
        self.Exam_File_Name = Exam_File_Name
        self.MaxGrade = MaxGrade
        
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



class Course:

    def __init__(self, CTutor: str, Cid: str, Cname: str, Course_File_Name: str, Course_REG: str, Cprice: str):
        self.CTutor = CTutor
        self.Cid = Cid
        self.Cname = Cname
        self.Course_File_Name = Course_File_Name
        self.Course_REG = Course_REG
        self.Cprice = Cprice
        
        pass
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
    def Cid(self):
        return self.__Cid
    @Cid.setter
    def Cid(self, Cid: str):
        self.__Cid = Cid

    @property
    def Course_REG(self):
        return self.__Course_REG
    @Course_REG.setter
    def Course_REG(self, Course_REG: str):
        self.__Course_REG = Course_REG

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

