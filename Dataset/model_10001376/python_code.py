from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Receptionist:

    pass


class Surgeon:

    pass


class Nurse:

    pass


class Doctor:

    def __init__(self, Speciality: str, Location: str):
        self.Speciality = Speciality
        self.Location = Location
        
        pass
    @property
    def Location(self):
        return self.__Location
    @Location.setter
    def Location(self, Location: str):
        self.__Location = Location

    @property
    def Speciality(self):
        return self.__Speciality
    @Speciality.setter
    def Speciality(self, Speciality: str):
        self.__Speciality = Speciality



class Technical_Staff:

    pass


class Administrative_Staff:

    pass


class Operation_Staff:

    pass


class Staff:

    def __init__(self, Education: str, Certification: str, Languages: str, department3: "Department" = None):
        self.Education = Education
        self.Certification = Certification
        self.Languages = Languages
        self.department3 = department3
        
        pass
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
    def department3(self):
        return self.__department3
    @department3.setter
    def department3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Staff__department3", None)
        self.__department3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "staff2"):
                opp_val = getattr(old_value, "staff2", None)
                if opp_val == self:
                    setattr(old_value, "staff2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "staff2"):
                opp_val = getattr(value, "staff2", None)
                setattr(value, "staff2", self)



class Department:

    pass


class Patient:

    def __init__(self, name: str, Sickness: str, Prescription: str, Allergy: str):
        self.name = name
        self.Sickness = Sickness
        self.Prescription = Prescription
        self.Allergy = Allergy
        
        pass
    @property
    def Prescription(self):
        return self.__Prescription
    @Prescription.setter
    def Prescription(self, Prescription: str):
        self.__Prescription = Prescription

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Sickness(self):
        return self.__Sickness
    @Sickness.setter
    def Sickness(self, Sickness: str):
        self.__Sickness = Sickness

    @property
    def Allergy(self):
        return self.__Allergy
    @Allergy.setter
    def Allergy(self, Allergy: str):
        self.__Allergy = Allergy



class Person:

    def __init__(self, name: str, father_s_name: str, Birth_date: str, Age: int, Gender: str, hospital4: "Hospital" = None):
        self.name = name
        self.father_s_name = father_s_name
        self.Birth_date = Birth_date
        self.Age = Age
        self.Gender = Gender
        self.hospital4 = hospital4
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Birth_date(self):
        return self.__Birth_date
    @Birth_date.setter
    def Birth_date(self, Birth_date: str):
        self.__Birth_date = Birth_date

    @property
    def Age(self):
        return self.__Age
    @Age.setter
    def Age(self, Age: int):
        self.__Age = Age

    @property
    def father_s_name(self):
        return self.__father_s_name
    @father_s_name.setter
    def father_s_name(self, father_s_name: str):
        self.__father_s_name = father_s_name

    @property
    def Gender(self):
        return self.__Gender
    @Gender.setter
    def Gender(self, Gender: str):
        self.__Gender = Gender

    @property
    def hospital4(self):
        return self.__hospital4
    @hospital4.setter
    def hospital4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Person__hospital4", None)
        self.__hospital4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "person5"):
                opp_val = getattr(old_value, "person5", None)
                if opp_val == self:
                    setattr(old_value, "person5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "person5"):
                opp_val = getattr(value, "person5", None)
                setattr(value, "person5", self)



class Hospital:

    def __init__(self, name: str, Address: str, phone_no: str, department0: "Department" = None, person5: "Person" = None):
        self.name = name
        self.Address = Address
        self.phone_no = phone_no
        self.department0 = department0
        self.person5 = person5
        
        pass
    @property
    def phone_no(self):
        return self.__phone_no
    @phone_no.setter
    def phone_no(self, phone_no: str):
        self.__phone_no = phone_no

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def person5(self):
        return self.__person5
    @person5.setter
    def person5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hospital__person5", None)
        self.__person5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hospital4"):
                opp_val = getattr(old_value, "hospital4", None)
                if opp_val == self:
                    setattr(old_value, "hospital4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hospital4"):
                opp_val = getattr(value, "hospital4", None)
                setattr(value, "hospital4", self)

    @property
    def department0(self):
        return self.__department0
    @department0.setter
    def department0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hospital__department0", None)
        self.__department0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hospital1"):
                opp_val = getattr(old_value, "hospital1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hospital1"):
                opp_val = getattr(value, "hospital1", None)
                if opp_val is None:
                    setattr(value, "hospital1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

