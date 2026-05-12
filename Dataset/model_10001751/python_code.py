from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Techinal_Staff:

    def __init__(self, Technician: str, Technologist: str):
        self.Technician = Technician
        self.Technologist = Technologist
        
        pass
    @property
    def Technician(self):
        return self.__Technician
    @Technician.setter
    def Technician(self, Technician: str):
        self.__Technician = Technician

    @property
    def Technologist(self):
        return self.__Technologist
    @Technologist.setter
    def Technologist(self, Technologist: str):
        self.__Technologist = Technologist



class Administrative_Staff:

    def __init__(self, FrontDeskStaffName: str, ReceptionistName: str):
        self.FrontDeskStaffName = FrontDeskStaffName
        self.ReceptionistName = ReceptionistName
        
        pass
    @property
    def FrontDeskStaffName(self):
        return self.__FrontDeskStaffName
    @FrontDeskStaffName.setter
    def FrontDeskStaffName(self, FrontDeskStaffName: str):
        self.__FrontDeskStaffName = FrontDeskStaffName

    @property
    def ReceptionistName(self):
        return self.__ReceptionistName
    @ReceptionistName.setter
    def ReceptionistName(self, ReceptionistName: str):
        self.__ReceptionistName = ReceptionistName



class Operation_Staff:

    def __init__(self, DoctorSpeciality: str, DoctorLocation: str, NurseName: str, patient4: set["Patient"] = None):
        self.DoctorSpeciality = DoctorSpeciality
        self.DoctorLocation = DoctorLocation
        self.NurseName = NurseName
        self.patient4 = patient4 if patient4 is not None else set()
        
        pass
    @property
    def DoctorLocation(self):
        return self.__DoctorLocation
    @DoctorLocation.setter
    def DoctorLocation(self, DoctorLocation: str):
        self.__DoctorLocation = DoctorLocation

    @property
    def NurseName(self):
        return self.__NurseName
    @NurseName.setter
    def NurseName(self, NurseName: str):
        self.__NurseName = NurseName

    @property
    def DoctorSpeciality(self):
        return self.__DoctorSpeciality
    @DoctorSpeciality.setter
    def DoctorSpeciality(self, DoctorSpeciality: str):
        self.__DoctorSpeciality = DoctorSpeciality

    @property
    def patient4(self):
        return self.__patient4
    @patient4.setter
    def patient4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Operation_Staff__patient4", None)
        self.__patient4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operation_Staff5"):
                    opp_val = getattr(item, "operation_Staff5", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operation_Staff5"):
                    opp_val = getattr(item, "operation_Staff5", None)
                    
                    if opp_val is None:
                        setattr(item, "operation_Staff5", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Staff:

    def __init__(self, Joined: str, Education: str, Certification: str, Languages: str, hospital2: set["Hospital"] = None):
        self.Joined = Joined
        self.Education = Education
        self.Certification = Certification
        self.Languages = Languages
        self.hospital2 = hospital2 if hospital2 is not None else set()
        
        pass
    @property
    def Education(self):
        return self.__Education
    @Education.setter
    def Education(self, Education: str):
        self.__Education = Education

    @property
    def Joined(self):
        return self.__Joined
    @Joined.setter
    def Joined(self, Joined: str):
        self.__Joined = Joined

    @property
    def Languages(self):
        return self.__Languages
    @Languages.setter
    def Languages(self, Languages: str):
        self.__Languages = Languages

    @property
    def Certification(self):
        return self.__Certification
    @Certification.setter
    def Certification(self, Certification: str):
        self.__Certification = Certification

    @property
    def hospital2(self):
        return self.__hospital2
    @hospital2.setter
    def hospital2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Staff__hospital2", None)
        self.__hospital2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "staff3"):
                    opp_val = getattr(item, "staff3", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "staff3"):
                    opp_val = getattr(item, "staff3", None)
                    
                    if opp_val is None:
                        setattr(item, "staff3", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Patient:

    def __init__(self, PatientId: int, Name: str, Gender: str, Birthdate: str, Age: int, DateOfEntry: str, Sickness: str, operation_Staff5: set["Operation_Staff"] = None):
        self.PatientId = PatientId
        self.Name = Name
        self.Gender = Gender
        self.Birthdate = Birthdate
        self.Age = Age
        self.DateOfEntry = DateOfEntry
        self.Sickness = Sickness
        self.operation_Staff5 = operation_Staff5 if operation_Staff5 is not None else set()
        
        pass
    @property
    def Sickness(self):
        return self.__Sickness
    @Sickness.setter
    def Sickness(self, Sickness: str):
        self.__Sickness = Sickness

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

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
    def PatientId(self):
        return self.__PatientId
    @PatientId.setter
    def PatientId(self, PatientId: int):
        self.__PatientId = PatientId

    @property
    def DateOfEntry(self):
        return self.__DateOfEntry
    @DateOfEntry.setter
    def DateOfEntry(self, DateOfEntry: str):
        self.__DateOfEntry = DateOfEntry

    @property
    def Birthdate(self):
        return self.__Birthdate
    @Birthdate.setter
    def Birthdate(self, Birthdate: str):
        self.__Birthdate = Birthdate

    @property
    def operation_Staff5(self):
        return self.__operation_Staff5
    @operation_Staff5.setter
    def operation_Staff5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__operation_Staff5", None)
        self.__operation_Staff5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patient4"):
                    opp_val = getattr(item, "patient4", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patient4"):
                    opp_val = getattr(item, "patient4", None)
                    
                    if opp_val is None:
                        setattr(item, "patient4", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Hospital:

    def __init__(self, Address: str, Phone: int, HospitalId: int, Name: str, person1: set["Person"] = None, staff3: set["Staff"] = None):
        self.Address = Address
        self.Phone = Phone
        self.HospitalId = HospitalId
        self.Name = Name
        self.person1 = person1 if person1 is not None else set()
        self.staff3 = staff3 if staff3 is not None else set()
        
        pass
    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Phone(self):
        return self.__Phone
    @Phone.setter
    def Phone(self, Phone: int):
        self.__Phone = Phone

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def HospitalId(self):
        return self.__HospitalId
    @HospitalId.setter
    def HospitalId(self, HospitalId: int):
        self.__HospitalId = HospitalId

    @property
    def staff3(self):
        return self.__staff3
    @staff3.setter
    def staff3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hospital__staff3", None)
        self.__staff3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hospital2"):
                    opp_val = getattr(item, "hospital2", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hospital2"):
                    opp_val = getattr(item, "hospital2", None)
                    
                    if opp_val is None:
                        setattr(item, "hospital2", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def person1(self):
        return self.__person1
    @person1.setter
    def person1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hospital__person1", None)
        self.__person1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hospital0"):
                    opp_val = getattr(item, "hospital0", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hospital0"):
                    opp_val = getattr(item, "hospital0", None)
                    
                    if opp_val is None:
                        setattr(item, "hospital0", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Person:

    def __init__(self, Title: str, FirstName: str, MiddleName: str, LastName: str, PersonHospitalId: int, BirthDate: str, Gender: str, Address: str, Phone: int, PersonPatientId: int, hospital0: set["Hospital"] = None):
        self.Title = Title
        self.FirstName = FirstName
        self.MiddleName = MiddleName
        self.LastName = LastName
        self.PersonHospitalId = PersonHospitalId
        self.BirthDate = BirthDate
        self.Gender = Gender
        self.Address = Address
        self.Phone = Phone
        self.PersonPatientId = PersonPatientId
        self.hospital0 = hospital0 if hospital0 is not None else set()
        
        pass
    @property
    def MiddleName(self):
        return self.__MiddleName
    @MiddleName.setter
    def MiddleName(self, MiddleName: str):
        self.__MiddleName = MiddleName

    @property
    def BirthDate(self):
        return self.__BirthDate
    @BirthDate.setter
    def BirthDate(self, BirthDate: str):
        self.__BirthDate = BirthDate

    @property
    def FirstName(self):
        return self.__FirstName
    @FirstName.setter
    def FirstName(self, FirstName: str):
        self.__FirstName = FirstName

    @property
    def Title(self):
        return self.__Title
    @Title.setter
    def Title(self, Title: str):
        self.__Title = Title

    @property
    def LastName(self):
        return self.__LastName
    @LastName.setter
    def LastName(self, LastName: str):
        self.__LastName = LastName

    @property
    def Gender(self):
        return self.__Gender
    @Gender.setter
    def Gender(self, Gender: str):
        self.__Gender = Gender

    @property
    def Phone(self):
        return self.__Phone
    @Phone.setter
    def Phone(self, Phone: int):
        self.__Phone = Phone

    @property
    def PersonPatientId(self):
        return self.__PersonPatientId
    @PersonPatientId.setter
    def PersonPatientId(self, PersonPatientId: int):
        self.__PersonPatientId = PersonPatientId

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def PersonHospitalId(self):
        return self.__PersonHospitalId
    @PersonHospitalId.setter
    def PersonHospitalId(self, PersonHospitalId: int):
        self.__PersonHospitalId = PersonHospitalId

    @property
    def hospital0(self):
        return self.__hospital0
    @hospital0.setter
    def hospital0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Person__hospital0", None)
        self.__hospital0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "person1"):
                    opp_val = getattr(item, "person1", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "person1"):
                    opp_val = getattr(item, "person1", None)
                    
                    if opp_val is None:
                        setattr(item, "person1", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

