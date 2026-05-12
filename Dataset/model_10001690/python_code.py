from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Doctor_Actor:

    pass


class Patient_Actor:

    pass





class Show_to_Doctor_external:

    pass


class Admin_Office_Component:

    pass


class Doctor:

    def __init__(self, Doctor_id: int, Dept: str, Specialization: str):
        self.Doctor_id = Doctor_id
        self.Dept = Dept
        self.Specialization = Specialization
        
        pass
    @property
    def Doctor_id(self):
        return self.__Doctor_id
    @Doctor_id.setter
    def Doctor_id(self, Doctor_id: int):
        self.__Doctor_id = Doctor_id

    @property
    def Specialization(self):
        return self.__Specialization
    @Specialization.setter
    def Specialization(self, Specialization: str):
        self.__Specialization = Specialization

    @property
    def Dept(self):
        return self.__Dept
    @Dept.setter
    def Dept(self, Dept: str):
        self.__Dept = Dept



class prescription:

    pass


class Patient:

    def __init__(self, Patient_id: int, Admit_date: str, Sickness: str):
        self.Patient_id = Patient_id
        self.Admit_date = Admit_date
        self.Sickness = Sickness
        
        pass
    @property
    def Patient_id(self):
        return self.__Patient_id
    @Patient_id.setter
    def Patient_id(self, Patient_id: int):
        self.__Patient_id = Patient_id

    @property
    def Sickness(self):
        return self.__Sickness
    @Sickness.setter
    def Sickness(self, Sickness: str):
        self.__Sickness = Sickness

    @property
    def Admit_date(self):
        return self.__Admit_date
    @Admit_date.setter
    def Admit_date(self, Admit_date: str):
        self.__Admit_date = Admit_date



class Person:

    def __init__(self, Name: str, Phone_no: str, Name1: str, Id: str, Gender: str, Birth_date: str, Age: int):
        self.Name = Name
        self.Phone_no = Phone_no
        self.Name1 = Name1
        self.Id = Id
        self.Gender = Gender
        self.Birth_date = Birth_date
        self.Age = Age
        
        pass
    @property
    def Gender(self):
        return self.__Gender
    @Gender.setter
    def Gender(self, Gender: str):
        self.__Gender = Gender

    @property
    def Age(self):
        return self.__Age
    @Age.setter
    def Age(self, Age: int):
        self.__Age = Age

    @property
    def Phone_no(self):
        return self.__Phone_no
    @Phone_no.setter
    def Phone_no(self, Phone_no: str):
        self.__Phone_no = Phone_no

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: str):
        self.__Id = Id

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Name1(self):
        return self.__Name1
    @Name1.setter
    def Name1(self, Name1: str):
        self.__Name1 = Name1

    @property
    def Birth_date(self):
        return self.__Birth_date
    @Birth_date.setter
    def Birth_date(self, Birth_date: str):
        self.__Birth_date = Birth_date



class Check_Patient_external:

    pass


class Give_Prescription_external:

    pass


class Take_Appointment_external:

    pass
