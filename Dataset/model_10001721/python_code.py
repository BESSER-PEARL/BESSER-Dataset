from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class HospitalSystem:

    def __init__(self, Patients: str, Doctors: str, admin: SystemAdministrator, systemAdministrator0: "SystemAdministrator" = None):
        self.Patients = Patients
        self.Doctors = Doctors
        self.admin = admin
        self.systemAdministrator0 = systemAdministrator0
        
        pass
    @property
    def admin(self):
        return self.__admin
    @admin.setter
    def admin(self, admin: SystemAdministrator):
        self.__admin = admin

    @property
    def Patients(self):
        return self.__Patients
    @Patients.setter
    def Patients(self, Patients: str):
        self.__Patients = Patients

    @property
    def Doctors(self):
        return self.__Doctors
    @Doctors.setter
    def Doctors(self, Doctors: str):
        self.__Doctors = Doctors

    @property
    def systemAdministrator0(self):
        return self.__systemAdministrator0
    @systemAdministrator0.setter
    def systemAdministrator0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HospitalSystem__systemAdministrator0", None)
        self.__systemAdministrator0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hospitalSystem1"):
                opp_val = getattr(old_value, "hospitalSystem1", None)
                if opp_val == self:
                    setattr(old_value, "hospitalSystem1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hospitalSystem1"):
                opp_val = getattr(value, "hospitalSystem1", None)
                setattr(value, "hospitalSystem1", self)



class SystemAdministrator:

    def __init__(self, Patients: str, Doctors: str, hospitalSystem1: "HospitalSystem" = None):
        self.Patients = Patients
        self.Doctors = Doctors
        self.hospitalSystem1 = hospitalSystem1
        
        pass
    @property
    def Patients(self):
        return self.__Patients
    @Patients.setter
    def Patients(self, Patients: str):
        self.__Patients = Patients

    @property
    def Doctors(self):
        return self.__Doctors
    @Doctors.setter
    def Doctors(self, Doctors: str):
        self.__Doctors = Doctors

    @property
    def hospitalSystem1(self):
        return self.__hospitalSystem1
    @hospitalSystem1.setter
    def hospitalSystem1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SystemAdministrator__hospitalSystem1", None)
        self.__hospitalSystem1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "systemAdministrator0"):
                opp_val = getattr(old_value, "systemAdministrator0", None)
                if opp_val == self:
                    setattr(old_value, "systemAdministrator0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "systemAdministrator0"):
                opp_val = getattr(value, "systemAdministrator0", None)
                setattr(value, "systemAdministrator0", self)



class Doctor:

    def __init__(self, Shedule: str, Specialization: str):
        self.Shedule = Shedule
        self.Specialization = Specialization
        
        pass
    @property
    def Specialization(self):
        return self.__Specialization
    @Specialization.setter
    def Specialization(self, Specialization: str):
        self.__Specialization = Specialization

    @property
    def Shedule(self):
        return self.__Shedule
    @Shedule.setter
    def Shedule(self, Shedule: str):
        self.__Shedule = Shedule



class Patient:

    def __init__(self, Age: int, Address: str, Phone: str, DiseaseHistory: str, Prescriptions: str):
        self.Age = Age
        self.Address = Address
        self.Phone = Phone
        self.DiseaseHistory = DiseaseHistory
        self.Prescriptions = Prescriptions
        
        pass
    @property
    def DiseaseHistory(self):
        return self.__DiseaseHistory
    @DiseaseHistory.setter
    def DiseaseHistory(self, DiseaseHistory: str):
        self.__DiseaseHistory = DiseaseHistory

    @property
    def Phone(self):
        return self.__Phone
    @Phone.setter
    def Phone(self, Phone: str):
        self.__Phone = Phone

    @property
    def Prescriptions(self):
        return self.__Prescriptions
    @Prescriptions.setter
    def Prescriptions(self, Prescriptions: str):
        self.__Prescriptions = Prescriptions

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Age(self):
        return self.__Age
    @Age.setter
    def Age(self, Age: int):
        self.__Age = Age



class Person:

    def __init__(self, FullName: str, BirthDate: str, Gender: str, ID: int, AccessLevel: str):
        self.FullName = FullName
        self.BirthDate = BirthDate
        self.Gender = Gender
        self.ID = ID
        self.AccessLevel = AccessLevel
        
        pass
    @property
    def FullName(self):
        return self.__FullName
    @FullName.setter
    def FullName(self, FullName: str):
        self.__FullName = FullName

    @property
    def AccessLevel(self):
        return self.__AccessLevel
    @AccessLevel.setter
    def AccessLevel(self, AccessLevel: str):
        self.__AccessLevel = AccessLevel

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def Gender(self):
        return self.__Gender
    @Gender.setter
    def Gender(self, Gender: str):
        self.__Gender = Gender

    @property
    def BirthDate(self):
        return self.__BirthDate
    @BirthDate.setter
    def BirthDate(self, BirthDate: str):
        self.__BirthDate = BirthDate



class Staff:

    def __init__(self, Status: str, Joined: str, Education: str, Certification: str, Languages: str):
        self.Status = Status
        self.Joined = Joined
        self.Education = Education
        self.Certification = Certification
        self.Languages = Languages
        
        pass
    @property
    def Joined(self):
        return self.__Joined
    @Joined.setter
    def Joined(self, Joined: str):
        self.__Joined = Joined

    @property
    def Certification(self):
        return self.__Certification
    @Certification.setter
    def Certification(self, Certification: str):
        self.__Certification = Certification

    @property
    def Languages(self):
        return self.__Languages
    @Languages.setter
    def Languages(self, Languages: str):
        self.__Languages = Languages

    @property
    def Education(self):
        return self.__Education
    @Education.setter
    def Education(self, Education: str):
        self.__Education = Education

    @property
    def Status(self):
        return self.__Status
    @Status.setter
    def Status(self, Status: str):
        self.__Status = Status

