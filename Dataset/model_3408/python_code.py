from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Subject(Enum):
    CES = "CES"
    BusinessEngineering = "BusinessEngineering"
    ComputerScience = "ComputerScience"
    MechanicalEngineering = "MechanicalEngineering"
    Physics = "Physics"
    Mathematics = "Mathematics"
    AppliedGeographics = "AppliedGeographics"
class OperatingSystem(Enum):
    Windows = "Windows"
    Linux_Unix = "Linux_Unix"
    MacOS = "MacOS"
    other = "other"
class Gender(Enum):
    Male = "Male"
    Female = "Female"
class Nationality(Enum):
    French = "French"
    German = "German"
    Spanish = "Spanish"
    English = "English"
    other = "other"
class ProgrammingLanguage(Enum):
    other = "other"
    C_CPP = "C_CPP"
    Java = "Java"
    Pascal_Delphi = "Pascal_Delphi"


############################################
# Definition of Classes
############################################

class VorkursModel_Room:

    def __init__(self, roomNr: int, sockets: bool, seats: int, hasComputers: bool, VorkursModel_Room: "VorkursModel_TeachingAssistant" = None):
        self.roomNr = roomNr
        self.sockets = sockets
        self.seats = seats
        self.hasComputers = hasComputers
        self.VorkursModel_Room = VorkursModel_Room
        
    @property
    def seats(self) -> int:
        return self.__seats

    @seats.setter
    def seats(self, seats: int):
        self.__seats = seats

    @property
    def hasComputers(self) -> bool:
        return self.__hasComputers

    @hasComputers.setter
    def hasComputers(self, hasComputers: bool):
        self.__hasComputers = hasComputers

    @property
    def sockets(self) -> bool:
        return self.__sockets

    @sockets.setter
    def sockets(self, sockets: bool):
        self.__sockets = sockets

    @property
    def roomNr(self) -> int:
        return self.__roomNr

    @roomNr.setter
    def roomNr(self, roomNr: int):
        self.__roomNr = roomNr

    @property
    def VorkursModel_Room(self):
        return self.__VorkursModel_Room

    @VorkursModel_Room.setter
    def VorkursModel_Room(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VorkursModel_Room__VorkursModel_Room", None)
        self.__VorkursModel_Room = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VorkursModel_TeachingAssistant11"):
                opp_val = getattr(old_value, "VorkursModel_TeachingAssistant11", None)
                if opp_val == self:
                    setattr(old_value, "VorkursModel_TeachingAssistant11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VorkursModel_TeachingAssistant11"):
                opp_val = getattr(value, "VorkursModel_TeachingAssistant11", None)
                setattr(value, "VorkursModel_TeachingAssistant11", self)

class Person:

    pass
class VorkursModel_Qualification:

    def __init__(self, hasPCExperience: bool, hasProgrammingExperience: bool, Language: str, programminLanguage: str, VorkursModel_Qualification: "VorkursModel_Person" = None):
        self.hasPCExperience = hasPCExperience
        self.hasProgrammingExperience = hasProgrammingExperience
        self.Language = Language
        self.programminLanguage = programminLanguage
        self.VorkursModel_Qualification = VorkursModel_Qualification
        
    @property
    def hasPCExperience(self) -> bool:
        return self.__hasPCExperience

    @hasPCExperience.setter
    def hasPCExperience(self, hasPCExperience: bool):
        self.__hasPCExperience = hasPCExperience

    @property
    def hasProgrammingExperience(self) -> bool:
        return self.__hasProgrammingExperience

    @hasProgrammingExperience.setter
    def hasProgrammingExperience(self, hasProgrammingExperience: bool):
        self.__hasProgrammingExperience = hasProgrammingExperience

    @property
    def programminLanguage(self) -> str:
        return self.__programminLanguage

    @programminLanguage.setter
    def programminLanguage(self, programminLanguage: str):
        self.__programminLanguage = programminLanguage

    @property
    def Language(self) -> str:
        return self.__Language

    @Language.setter
    def Language(self, Language: str):
        self.__Language = Language

    @property
    def VorkursModel_Qualification(self):
        return self.__VorkursModel_Qualification

    @VorkursModel_Qualification.setter
    def VorkursModel_Qualification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VorkursModel_Qualification__VorkursModel_Qualification", None)
        self.__VorkursModel_Qualification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VorkursModel_Person7"):
                opp_val = getattr(old_value, "VorkursModel_Person7", None)
                if opp_val == self:
                    setattr(old_value, "VorkursModel_Person7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VorkursModel_Person7"):
                opp_val = getattr(value, "VorkursModel_Person7", None)
                setattr(value, "VorkursModel_Person7", self)

class VorkursModel_Address:

    def __init__(self, city: str, state: str, zip: str, street: str, VorkursModel_Address: "VorkursModel_Contact" = None):
        self.city = city
        self.state = state
        self.zip = zip
        self.street = street
        self.VorkursModel_Address = VorkursModel_Address
        
    @property
    def zip(self) -> str:
        return self.__zip

    @zip.setter
    def zip(self, zip: str):
        self.__zip = zip

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def VorkursModel_Address(self):
        return self.__VorkursModel_Address

    @VorkursModel_Address.setter
    def VorkursModel_Address(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VorkursModel_Address__VorkursModel_Address", None)
        self.__VorkursModel_Address = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VorkursModel_Contact9"):
                opp_val = getattr(old_value, "VorkursModel_Contact9", None)
                if opp_val == self:
                    setattr(old_value, "VorkursModel_Contact9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VorkursModel_Contact9"):
                opp_val = getattr(value, "VorkursModel_Contact9", None)
                setattr(value, "VorkursModel_Contact9", self)

class VorkursModel_TeachingAssistant(Person):

    pass
class VorkursModel_Student(Person):

    pass
class VorkursModel_Notebook:

    def __init__(self, OperatingSystem: str, hasWLAN: bool, VorkursModel_Notebook: "VorkursModel_Person" = None):
        self.OperatingSystem = OperatingSystem
        self.hasWLAN = hasWLAN
        self.VorkursModel_Notebook = VorkursModel_Notebook
        
    @property
    def OperatingSystem(self) -> str:
        return self.__OperatingSystem

    @OperatingSystem.setter
    def OperatingSystem(self, OperatingSystem: str):
        self.__OperatingSystem = OperatingSystem

    @property
    def hasWLAN(self) -> bool:
        return self.__hasWLAN

    @hasWLAN.setter
    def hasWLAN(self, hasWLAN: bool):
        self.__hasWLAN = hasWLAN

    @property
    def VorkursModel_Notebook(self):
        return self.__VorkursModel_Notebook

    @VorkursModel_Notebook.setter
    def VorkursModel_Notebook(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VorkursModel_Notebook__VorkursModel_Notebook", None)
        self.__VorkursModel_Notebook = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VorkursModel_Person5"):
                opp_val = getattr(old_value, "VorkursModel_Person5", None)
                if opp_val == self:
                    setattr(old_value, "VorkursModel_Person5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VorkursModel_Person5"):
                opp_val = getattr(value, "VorkursModel_Person5", None)
                setattr(value, "VorkursModel_Person5", self)

class VorkursModel_Contact:

    def __init__(self, phonenumber: str, Email: str, VorkursModel_Contact: "VorkursModel_Person" = None, VorkursModel_Contact9: "VorkursModel_Address" = None):
        self.phonenumber = phonenumber
        self.Email = Email
        self.VorkursModel_Contact = VorkursModel_Contact
        self.VorkursModel_Contact9 = VorkursModel_Contact9
        
    @property
    def Email(self) -> str:
        return self.__Email

    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def phonenumber(self) -> str:
        return self.__phonenumber

    @phonenumber.setter
    def phonenumber(self, phonenumber: str):
        self.__phonenumber = phonenumber

    @property
    def VorkursModel_Contact(self):
        return self.__VorkursModel_Contact

    @VorkursModel_Contact.setter
    def VorkursModel_Contact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VorkursModel_Contact__VorkursModel_Contact", None)
        self.__VorkursModel_Contact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VorkursModel_Person"):
                opp_val = getattr(old_value, "VorkursModel_Person", None)
                if opp_val == self:
                    setattr(old_value, "VorkursModel_Person", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VorkursModel_Person"):
                opp_val = getattr(value, "VorkursModel_Person", None)
                setattr(value, "VorkursModel_Person", self)

    @property
    def VorkursModel_Contact9(self):
        return self.__VorkursModel_Contact9

    @VorkursModel_Contact9.setter
    def VorkursModel_Contact9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VorkursModel_Contact__VorkursModel_Contact9", None)
        self.__VorkursModel_Contact9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VorkursModel_Address"):
                opp_val = getattr(old_value, "VorkursModel_Address", None)
                if opp_val == self:
                    setattr(old_value, "VorkursModel_Address", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VorkursModel_Address"):
                opp_val = getattr(value, "VorkursModel_Address", None)
                setattr(value, "VorkursModel_Address", self)

class VorkursModel_Person(ABC):

    def __init__(self, firstname: str, lastname: str, subject: str, gender: str, VorkursModel_Person: "VorkursModel_Contact" = None, VorkursModel_Person5: "VorkursModel_Notebook" = None, VorkursModel_Person7: "VorkursModel_Qualification" = None):
        self.firstname = firstname
        self.lastname = lastname
        self.subject = subject
        self.gender = gender
        self.VorkursModel_Person = VorkursModel_Person
        self.VorkursModel_Person5 = VorkursModel_Person5
        self.VorkursModel_Person7 = VorkursModel_Person7
        
    @property
    def gender(self) -> str:
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def subject(self) -> str:
        return self.__subject

    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject

    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def VorkursModel_Person7(self):
        return self.__VorkursModel_Person7

    @VorkursModel_Person7.setter
    def VorkursModel_Person7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VorkursModel_Person__VorkursModel_Person7", None)
        self.__VorkursModel_Person7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VorkursModel_Qualification"):
                opp_val = getattr(old_value, "VorkursModel_Qualification", None)
                if opp_val == self:
                    setattr(old_value, "VorkursModel_Qualification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VorkursModel_Qualification"):
                opp_val = getattr(value, "VorkursModel_Qualification", None)
                setattr(value, "VorkursModel_Qualification", self)

    @property
    def VorkursModel_Person(self):
        return self.__VorkursModel_Person

    @VorkursModel_Person.setter
    def VorkursModel_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VorkursModel_Person__VorkursModel_Person", None)
        self.__VorkursModel_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VorkursModel_Contact"):
                opp_val = getattr(old_value, "VorkursModel_Contact", None)
                if opp_val == self:
                    setattr(old_value, "VorkursModel_Contact", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VorkursModel_Contact"):
                opp_val = getattr(value, "VorkursModel_Contact", None)
                setattr(value, "VorkursModel_Contact", self)

    @property
    def VorkursModel_Person5(self):
        return self.__VorkursModel_Person5

    @VorkursModel_Person5.setter
    def VorkursModel_Person5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VorkursModel_Person__VorkursModel_Person5", None)
        self.__VorkursModel_Person5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VorkursModel_Notebook"):
                opp_val = getattr(old_value, "VorkursModel_Notebook", None)
                if opp_val == self:
                    setattr(old_value, "VorkursModel_Notebook", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VorkursModel_Notebook"):
                opp_val = getattr(value, "VorkursModel_Notebook", None)
                setattr(value, "VorkursModel_Notebook", self)

class VorkursModel_RegistrationSystem:

    pass