from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Topic:

    pass
class SWRC_ResearchTopic(Topic):

    pass
class SWRC_Topic:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class SWRC_Product:

    def __init__(self, name: str, develops: "Organization" = None):
        self.name = name
        self.develops = develops
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def develops(self):
        return self.__develops

    @develops.setter
    def develops(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_Product__develops", None)
        self.__develops = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Organization136"):
                opp_val = getattr(old_value, "Organization136", None)
                if opp_val == self:
                    setattr(old_value, "Organization136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Organization136"):
                opp_val = getattr(value, "Organization136", None)
                setattr(value, "Organization136", self)

class ProjectReport:

    pass
class Department:

    pass
class SWRC_Project(ABC):

    def __init__(self, name: str, carriesOut: "Organization" = None, finances: "Organization" = None, dealWithIn: set["ResearchTopic"] = None, SWRC_Project: set["Person"] = None, describesProject: set["ProjectReport"] = None, headOf: "AcademicStaff" = None):
        self.name = name
        self.carriesOut = carriesOut
        self.finances = finances
        self.dealWithIn = dealWithIn if dealWithIn is not None else set()
        self.SWRC_Project = SWRC_Project if SWRC_Project is not None else set()
        self.describesProject = describesProject if describesProject is not None else set()
        self.headOf = headOf
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def SWRC_Project(self):
        return self.__SWRC_Project

    @SWRC_Project.setter
    def SWRC_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_Project__SWRC_Project", None)
        self.__SWRC_Project = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person131"):
                    opp_val = getattr(item, "Person131", None)
                    
                    if opp_val == self:
                        setattr(item, "Person131", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person131"):
                    opp_val = getattr(item, "Person131", None)
                    
                    setattr(item, "Person131", self)
                    

    @property
    def finances(self):
        return self.__finances

    @finances.setter
    def finances(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_Project__finances", None)
        self.__finances = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Organization125"):
                opp_val = getattr(old_value, "Organization125", None)
                if opp_val == self:
                    setattr(old_value, "Organization125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Organization125"):
                opp_val = getattr(value, "Organization125", None)
                setattr(value, "Organization125", self)

    @property
    def headOf(self):
        return self.__headOf

    @headOf.setter
    def headOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_Project__headOf", None)
        self.__headOf = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AcademicStaff127"):
                opp_val = getattr(old_value, "AcademicStaff127", None)
                if opp_val == self:
                    setattr(old_value, "AcademicStaff127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AcademicStaff127"):
                opp_val = getattr(value, "AcademicStaff127", None)
                setattr(value, "AcademicStaff127", self)

    @property
    def carriesOut(self):
        return self.__carriesOut

    @carriesOut.setter
    def carriesOut(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_Project__carriesOut", None)
        self.__carriesOut = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Organization123"):
                opp_val = getattr(old_value, "Organization123", None)
                if opp_val == self:
                    setattr(old_value, "Organization123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Organization123"):
                opp_val = getattr(value, "Organization123", None)
                setattr(value, "Organization123", self)

    @property
    def dealWithIn(self):
        return self.__dealWithIn

    @dealWithIn.setter
    def dealWithIn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_Project__dealWithIn", None)
        self.__dealWithIn = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ResearchTopic129"):
                    opp_val = getattr(item, "ResearchTopic129", None)
                    
                    if opp_val == self:
                        setattr(item, "ResearchTopic129", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ResearchTopic129"):
                    opp_val = getattr(item, "ResearchTopic129", None)
                    
                    setattr(item, "ResearchTopic129", self)
                    

    @property
    def describesProject(self):
        return self.__describesProject

    @describesProject.setter
    def describesProject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_Project__describesProject", None)
        self.__describesProject = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ProjectReport"):
                    opp_val = getattr(item, "ProjectReport", None)
                    
                    if opp_val == self:
                        setattr(item, "ProjectReport", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProjectReport"):
                    opp_val = getattr(item, "ProjectReport", None)
                    
                    setattr(item, "ProjectReport", self)
                    

class Institute:

    pass
class Product:

    pass
class SWRC_SoftwareComponent(Product):

    def __init__(self, hasPrice: str, Product: "SWRC_Organization" = None, Product134: "SWRC_SoftwareProject" = None):
        self.hasPrice = hasPrice
        
        pass
    @property
    def hasPrice(self):
        return self.__hasPrice

    @hasPrice.setter
    def hasPrice(self, hasPrice: str):
        self.__hasPrice = hasPrice


class TechnicalReport:

    pass
class SWRC_Organization:

    def __init__(self, location: str, name: str, financedBy: set["Project"] = None, SWRC_Organization: set["Publication"] = None, SWRC_Organization108: set["TechnicalReport"] = None, carriedOutBy: set["Project"] = None, developedBy: set["Product"] = None, affiliation: set["Employee"] = None):
        self.location = location
        self.name = name
        self.financedBy = financedBy if financedBy is not None else set()
        self.SWRC_Organization = SWRC_Organization if SWRC_Organization is not None else set()
        self.SWRC_Organization108 = SWRC_Organization108 if SWRC_Organization108 is not None else set()
        self.carriedOutBy = carriedOutBy if carriedOutBy is not None else set()
        self.developedBy = developedBy if developedBy is not None else set()
        self.affiliation = affiliation if affiliation is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


    @property
    def developedBy(self):
        return self.__developedBy

    @developedBy.setter
    def developedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_Organization__developedBy", None)
        self.__developedBy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Product"):
                    opp_val = getattr(item, "Product", None)
                    
                    if opp_val == self:
                        setattr(item, "Product", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Product"):
                    opp_val = getattr(item, "Product", None)
                    
                    setattr(item, "Product", self)
                    

    @property
    def SWRC_Organization(self):
        return self.__SWRC_Organization

    @SWRC_Organization.setter
    def SWRC_Organization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_Organization__SWRC_Organization", None)
        self.__SWRC_Organization = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Publication106"):
                    opp_val = getattr(item, "Publication106", None)
                    
                    if opp_val == self:
                        setattr(item, "Publication106", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Publication106"):
                    opp_val = getattr(item, "Publication106", None)
                    
                    setattr(item, "Publication106", self)
                    

    @property
    def carriedOutBy(self):
        return self.__carriedOutBy

    @carriedOutBy.setter
    def carriedOutBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_Organization__carriedOutBy", None)
        self.__carriedOutBy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Project100"):
                    opp_val = getattr(item, "Project100", None)
                    
                    if opp_val == self:
                        setattr(item, "Project100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Project100"):
                    opp_val = getattr(item, "Project100", None)
                    
                    setattr(item, "Project100", self)
                    

    @property
    def affiliation(self):
        return self.__affiliation

    @affiliation.setter
    def affiliation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_Organization__affiliation", None)
        self.__affiliation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee"):
                    opp_val = getattr(item, "Employee", None)
                    
                    if opp_val == self:
                        setattr(item, "Employee", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee"):
                    opp_val = getattr(item, "Employee", None)
                    
                    setattr(item, "Employee", self)
                    

    @property
    def financedBy(self):
        return self.__financedBy

    @financedBy.setter
    def financedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_Organization__financedBy", None)
        self.__financedBy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Project104"):
                    opp_val = getattr(item, "Project104", None)
                    
                    if opp_val == self:
                        setattr(item, "Project104", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Project104"):
                    opp_val = getattr(item, "Project104", None)
                    
                    setattr(item, "Project104", self)
                    

    @property
    def SWRC_Organization108(self):
        return self.__SWRC_Organization108

    @SWRC_Organization108.setter
    def SWRC_Organization108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_Organization__SWRC_Organization108", None)
        self.__SWRC_Organization108 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TechnicalReport"):
                    opp_val = getattr(item, "TechnicalReport", None)
                    
                    if opp_val == self:
                        setattr(item, "TechnicalReport", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TechnicalReport"):
                    opp_val = getattr(item, "TechnicalReport", None)
                    
                    setattr(item, "TechnicalReport", self)
                    

class Graduate:

    pass
class SWRC_PhDStudent(Graduate):

    pass
class Student:

    pass
class SWRC_Graduate(Student):

    pass
class SWRC_Undergraduate(Student):

    pass
class FacultyMember:

    pass
class SWRC_AssistantProfessor(FacultyMember):

    pass
class SWRC_AssociateProfessor(FacultyMember):

    pass
class SWRC_FullProfessor(FacultyMember):

    pass
class ResearchTopic:

    pass
class PhDStudent:

    pass
class ResearchGroup:

    pass
class Employee:

    pass
class SWRC_TechnicalStaff(Employee):

    pass
class SWRC_AdministrativeStaff(Employee):

    pass
class SWRC_Manager(Employee):

    pass
class AcademicStaff:

    pass
class SWRC_Lecturer(AcademicStaff):

    pass
class SWRC_FacultyMember(AcademicStaff):

    pass
class SWRC_Person:

    def __init__(self, address: str, name: str, email: str, fax: str, homepage: str, phone: str, photo: str):
        self.address = address
        self.name = name
        self.email = email
        self.fax = fax
        self.homepage = homepage
        self.phone = phone
        self.photo = photo
        
        pass
    @property
    def photo(self):
        return self.__photo

    @photo.setter
    def photo(self, photo: str):
        self.__photo = photo


    @property
    def homepage(self):
        return self.__homepage

    @homepage.setter
    def homepage(self, homepage: str):
        self.__homepage = homepage


    @property
    def fax(self):
        return self.__fax

    @fax.setter
    def fax(self, fax: str):
        self.__fax = fax


    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone


    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email


    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Meeting:

    pass
class SWRC_ProjectMeeting(Meeting):

    pass
class Event:

    pass
class SWRC_Meeting(Event):

    def __init__(self, title: str, SWRC_Meeting: set["Person"] = None, Event: "SWRC_Event" = None, Event64: "SWRC_Event" = None, Event84: "SWRC_AcademicStaff" = None, Event81: "SWRC_AcademicStaff" = None):
        self.title = title
        self.SWRC_Meeting = SWRC_Meeting if SWRC_Meeting is not None else set()
        
        pass
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def SWRC_Meeting(self):
        return self.__SWRC_Meeting

    @SWRC_Meeting.setter
    def SWRC_Meeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_Meeting__SWRC_Meeting", None)
        self.__SWRC_Meeting = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person68"):
                    opp_val = getattr(item, "Person68", None)
                    
                    if opp_val == self:
                        setattr(item, "Person68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person68"):
                    opp_val = getattr(item, "Person68", None)
                    
                    setattr(item, "Person68", self)
                    

class SWRC_Exhibition(Event):

    pass
class SWRC_Conference(Event):

    def __init__(self, series: str, Event: "SWRC_Event" = None, Event64: "SWRC_Event" = None, Event84: "SWRC_AcademicStaff" = None, Event81: "SWRC_AcademicStaff" = None):
        self.series = series
        
        pass
    @property
    def series(self):
        return self.__series

    @series.setter
    def series(self, series: str):
        self.__series = series


class SWRC_Workshop(Event):

    def __init__(self, series: str, Event: "SWRC_Event" = None, Event64: "SWRC_Event" = None, Event84: "SWRC_AcademicStaff" = None, Event81: "SWRC_AcademicStaff" = None):
        self.series = series
        
        pass
    @property
    def series(self):
        return self.__series

    @series.setter
    def series(self, series: str):
        self.__series = series


class SWRC_Lecture(Event):

    pass
class SWRC_Event:

    def __init__(self, name: str, date: str, eventTitle: str, location: str, hasPartEvent: "Event" = None, atEvent: "Event" = None):
        self.name = name
        self.date = date
        self.eventTitle = eventTitle
        self.location = location
        self.hasPartEvent = hasPartEvent
        self.atEvent = atEvent
        
        pass
    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date = date


    @property
    def eventTitle(self):
        return self.__eventTitle

    @eventTitle.setter
    def eventTitle(self, eventTitle: str):
        self.__eventTitle = eventTitle


    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def hasPartEvent(self):
        return self.__hasPartEvent

    @hasPartEvent.setter
    def hasPartEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_Event__hasPartEvent", None)
        self.__hasPartEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Event"):
                opp_val = getattr(old_value, "Event", None)
                if opp_val == self:
                    setattr(old_value, "Event", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Event"):
                opp_val = getattr(value, "Event", None)
                setattr(value, "Event", self)

    @property
    def atEvent(self):
        return self.__atEvent

    @atEvent.setter
    def atEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_Event__atEvent", None)
        self.__atEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Event64"):
                opp_val = getattr(old_value, "Event64", None)
                if opp_val == self:
                    setattr(old_value, "Event64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Event64"):
                opp_val = getattr(value, "Event64", None)
                setattr(value, "Event64", self)

class Project:

    pass
class SWRC_DevelopmentProject(Project):

    pass
class SWRC_SoftwareProject(Project):

    pass
class SWRC_ResearchProject(Project):

    pass
class Report:

    pass
class SWRC_TechnicalReport(Report):

    def __init__(self, series: str, SWRC_TechnicalReport: "Organization" = None):
        self.series = series
        self.SWRC_TechnicalReport = SWRC_TechnicalReport
        
        pass
    @property
    def series(self):
        return self.__series

    @series.setter
    def series(self, series: str):
        self.__series = series


    @property
    def SWRC_TechnicalReport(self):
        return self.__SWRC_TechnicalReport

    @SWRC_TechnicalReport.setter
    def SWRC_TechnicalReport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_TechnicalReport__SWRC_TechnicalReport", None)
        self.__SWRC_TechnicalReport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Organization61"):
                opp_val = getattr(old_value, "Organization61", None)
                if opp_val == self:
                    setattr(old_value, "Organization61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Organization61"):
                opp_val = getattr(value, "Organization61", None)
                setattr(value, "Organization61", self)

class SWRC_ProjectReport(Report):

    pass
class Thesis:

    pass
class SWRC_PhDThesis(Thesis):

    pass
class SWRC_MasterThesis(Thesis):

    pass
class University:

    pass
class Organization:

    pass
class SWRC_Institute(Organization):

    pass
class SWRC_Enterprise(Organization):

    pass
class SWRC_University(Organization):

    pass
class SWRC_Association(Organization):

    pass
class SWRC_ResearchGroup(Organization):

    pass
class SWRC_Department(Organization):

    pass
class Person:

    pass
class SWRC_AcademicStaff(Person):

    pass
class SWRC_Employee(Person):

    pass
class SWRC_Student(Person):

    pass
class Publication:

    pass
class SWRC_Booklet(Publication):

    def __init__(self, edition: str, month: str, address: str, howpublished: str, SWRC_Booklet: set["Person"] = None, Publication93: "SWRC_PhDStudent" = None, Publication87: "SWRC_AcademicStaff" = None, Publication74: "SWRC_AcademicStaff" = None, Publication106: "SWRC_Organization" = None, Publication: "SWRC_Bibliography" = None):
        self.edition = edition
        self.month = month
        self.address = address
        self.howpublished = howpublished
        self.SWRC_Booklet = SWRC_Booklet if SWRC_Booklet is not None else set()
        
        pass
    @property
    def edition(self):
        return self.__edition

    @edition.setter
    def edition(self, edition: str):
        self.__edition = edition


    @property
    def howpublished(self):
        return self.__howpublished

    @howpublished.setter
    def howpublished(self, howpublished: str):
        self.__howpublished = howpublished


    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address


    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month


    @property
    def SWRC_Booklet(self):
        return self.__SWRC_Booklet

    @SWRC_Booklet.setter
    def SWRC_Booklet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_Booklet__SWRC_Booklet", None)
        self.__SWRC_Booklet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person18"):
                    opp_val = getattr(item, "Person18", None)
                    
                    if opp_val == self:
                        setattr(item, "Person18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person18"):
                    opp_val = getattr(item, "Person18", None)
                    
                    setattr(item, "Person18", self)
                    

class SWRC_Unpublished(Publication):

    def __init__(self, month: str, SWRC_Unpublished: set["Person"] = None, Publication93: "SWRC_PhDStudent" = None, Publication87: "SWRC_AcademicStaff" = None, Publication74: "SWRC_AcademicStaff" = None, Publication106: "SWRC_Organization" = None, Publication: "SWRC_Bibliography" = None):
        self.month = month
        self.SWRC_Unpublished = SWRC_Unpublished if SWRC_Unpublished is not None else set()
        
        pass
    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month


    @property
    def SWRC_Unpublished(self):
        return self.__SWRC_Unpublished

    @SWRC_Unpublished.setter
    def SWRC_Unpublished(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_Unpublished__SWRC_Unpublished", None)
        self.__SWRC_Unpublished = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person52"):
                    opp_val = getattr(item, "Person52", None)
                    
                    if opp_val == self:
                        setattr(item, "Person52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person52"):
                    opp_val = getattr(item, "Person52", None)
                    
                    setattr(item, "Person52", self)
                    

class SWRC_Report(Publication):

    pass
class SWRC_InBook(Publication):

    def __init__(self, pages: str, volume: str, month: str, number: str, series: str, chapter: str, type: str, address: str, SWRC_InBook: set["Person"] = None, SWRC_InBook12: "Organization" = None, SWRC_InBook15: "Person" = None, Publication93: "SWRC_PhDStudent" = None, Publication87: "SWRC_AcademicStaff" = None, Publication74: "SWRC_AcademicStaff" = None, Publication106: "SWRC_Organization" = None, Publication: "SWRC_Bibliography" = None):
        self.pages = pages
        self.volume = volume
        self.month = month
        self.number = number
        self.series = series
        self.chapter = chapter
        self.type = type
        self.address = address
        self.SWRC_InBook = SWRC_InBook if SWRC_InBook is not None else set()
        self.SWRC_InBook12 = SWRC_InBook12
        self.SWRC_InBook15 = SWRC_InBook15
        
        pass
    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages: str):
        self.__pages = pages


    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address


    @property
    def series(self):
        return self.__series

    @series.setter
    def series(self, series: str):
        self.__series = series


    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number


    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month


    @property
    def chapter(self):
        return self.__chapter

    @chapter.setter
    def chapter(self, chapter: str):
        self.__chapter = chapter


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume: str):
        self.__volume = volume


    @property
    def SWRC_InBook15(self):
        return self.__SWRC_InBook15

    @SWRC_InBook15.setter
    def SWRC_InBook15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_InBook__SWRC_InBook15", None)
        self.__SWRC_InBook15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Person16"):
                opp_val = getattr(old_value, "Person16", None)
                if opp_val == self:
                    setattr(old_value, "Person16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Person16"):
                opp_val = getattr(value, "Person16", None)
                setattr(value, "Person16", self)

    @property
    def SWRC_InBook(self):
        return self.__SWRC_InBook

    @SWRC_InBook.setter
    def SWRC_InBook(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_InBook__SWRC_InBook", None)
        self.__SWRC_InBook = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person10"):
                    opp_val = getattr(item, "Person10", None)
                    
                    if opp_val == self:
                        setattr(item, "Person10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person10"):
                    opp_val = getattr(item, "Person10", None)
                    
                    setattr(item, "Person10", self)
                    

    @property
    def SWRC_InBook12(self):
        return self.__SWRC_InBook12

    @SWRC_InBook12.setter
    def SWRC_InBook12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_InBook__SWRC_InBook12", None)
        self.__SWRC_InBook12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Organization13"):
                opp_val = getattr(old_value, "Organization13", None)
                if opp_val == self:
                    setattr(old_value, "Organization13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Organization13"):
                opp_val = getattr(value, "Organization13", None)
                setattr(value, "Organization13", self)

class SWRC_Proceedings(Publication):

    def __init__(self, month: str, number: str, volume: str, address: str, series: str, SWRC_Proceedings: "Person" = None, SWRC_Proceedings41: "Organization" = None, SWRC_Proceedings44: "Organization" = None, Publication93: "SWRC_PhDStudent" = None, Publication87: "SWRC_AcademicStaff" = None, Publication74: "SWRC_AcademicStaff" = None, Publication106: "SWRC_Organization" = None, Publication: "SWRC_Bibliography" = None):
        self.month = month
        self.number = number
        self.volume = volume
        self.address = address
        self.series = series
        self.SWRC_Proceedings = SWRC_Proceedings
        self.SWRC_Proceedings41 = SWRC_Proceedings41
        self.SWRC_Proceedings44 = SWRC_Proceedings44
        
        pass
    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month


    @property
    def series(self):
        return self.__series

    @series.setter
    def series(self, series: str):
        self.__series = series


    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address


    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume: str):
        self.__volume = volume


    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number


    @property
    def SWRC_Proceedings44(self):
        return self.__SWRC_Proceedings44

    @SWRC_Proceedings44.setter
    def SWRC_Proceedings44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_Proceedings__SWRC_Proceedings44", None)
        self.__SWRC_Proceedings44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Organization45"):
                opp_val = getattr(old_value, "Organization45", None)
                if opp_val == self:
                    setattr(old_value, "Organization45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Organization45"):
                opp_val = getattr(value, "Organization45", None)
                setattr(value, "Organization45", self)

    @property
    def SWRC_Proceedings41(self):
        return self.__SWRC_Proceedings41

    @SWRC_Proceedings41.setter
    def SWRC_Proceedings41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_Proceedings__SWRC_Proceedings41", None)
        self.__SWRC_Proceedings41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Organization42"):
                opp_val = getattr(old_value, "Organization42", None)
                if opp_val == self:
                    setattr(old_value, "Organization42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Organization42"):
                opp_val = getattr(value, "Organization42", None)
                setattr(value, "Organization42", self)

    @property
    def SWRC_Proceedings(self):
        return self.__SWRC_Proceedings

    @SWRC_Proceedings.setter
    def SWRC_Proceedings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_Proceedings__SWRC_Proceedings", None)
        self.__SWRC_Proceedings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Person39"):
                opp_val = getattr(old_value, "Person39", None)
                if opp_val == self:
                    setattr(old_value, "Person39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Person39"):
                opp_val = getattr(value, "Person39", None)
                setattr(value, "Person39", self)

class SWRC_InProceedings(Publication):

    def __init__(self, month: str, number: str, pages: str, address: str, volume: str, series: str, booktitle: str, SWRC_InProceedings: "Person" = None, SWRC_InProceedings33: "Organization" = None, SWRC_InProceedings36: "Organization" = None, SWRC_InProceedings30: set["Person"] = None, Publication93: "SWRC_PhDStudent" = None, Publication87: "SWRC_AcademicStaff" = None, Publication74: "SWRC_AcademicStaff" = None, Publication106: "SWRC_Organization" = None, Publication: "SWRC_Bibliography" = None):
        self.month = month
        self.number = number
        self.pages = pages
        self.address = address
        self.volume = volume
        self.series = series
        self.booktitle = booktitle
        self.SWRC_InProceedings = SWRC_InProceedings
        self.SWRC_InProceedings33 = SWRC_InProceedings33
        self.SWRC_InProceedings36 = SWRC_InProceedings36
        self.SWRC_InProceedings30 = SWRC_InProceedings30 if SWRC_InProceedings30 is not None else set()
        
        pass
    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume: str):
        self.__volume = volume


    @property
    def series(self):
        return self.__series

    @series.setter
    def series(self, series: str):
        self.__series = series


    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages: str):
        self.__pages = pages


    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address


    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month


    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number


    @property
    def booktitle(self):
        return self.__booktitle

    @booktitle.setter
    def booktitle(self, booktitle: str):
        self.__booktitle = booktitle


    @property
    def SWRC_InProceedings33(self):
        return self.__SWRC_InProceedings33

    @SWRC_InProceedings33.setter
    def SWRC_InProceedings33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_InProceedings__SWRC_InProceedings33", None)
        self.__SWRC_InProceedings33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Organization34"):
                opp_val = getattr(old_value, "Organization34", None)
                if opp_val == self:
                    setattr(old_value, "Organization34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Organization34"):
                opp_val = getattr(value, "Organization34", None)
                setattr(value, "Organization34", self)

    @property
    def SWRC_InProceedings30(self):
        return self.__SWRC_InProceedings30

    @SWRC_InProceedings30.setter
    def SWRC_InProceedings30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_InProceedings__SWRC_InProceedings30", None)
        self.__SWRC_InProceedings30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person31"):
                    opp_val = getattr(item, "Person31", None)
                    
                    if opp_val == self:
                        setattr(item, "Person31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person31"):
                    opp_val = getattr(item, "Person31", None)
                    
                    setattr(item, "Person31", self)
                    

    @property
    def SWRC_InProceedings(self):
        return self.__SWRC_InProceedings

    @SWRC_InProceedings.setter
    def SWRC_InProceedings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_InProceedings__SWRC_InProceedings", None)
        self.__SWRC_InProceedings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Person28"):
                opp_val = getattr(old_value, "Person28", None)
                if opp_val == self:
                    setattr(old_value, "Person28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Person28"):
                opp_val = getattr(value, "Person28", None)
                setattr(value, "Person28", self)

    @property
    def SWRC_InProceedings36(self):
        return self.__SWRC_InProceedings36

    @SWRC_InProceedings36.setter
    def SWRC_InProceedings36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_InProceedings__SWRC_InProceedings36", None)
        self.__SWRC_InProceedings36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Organization37"):
                opp_val = getattr(old_value, "Organization37", None)
                if opp_val == self:
                    setattr(old_value, "Organization37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Organization37"):
                opp_val = getattr(value, "Organization37", None)
                setattr(value, "Organization37", self)

class SWRC_Manual(Publication):

    def __init__(self, month: str, address: str, edition: str, SWRC_Manual: set["Person"] = None, SWRC_Manual49: "Organization" = None, Publication93: "SWRC_PhDStudent" = None, Publication87: "SWRC_AcademicStaff" = None, Publication74: "SWRC_AcademicStaff" = None, Publication106: "SWRC_Organization" = None, Publication: "SWRC_Bibliography" = None):
        self.month = month
        self.address = address
        self.edition = edition
        self.SWRC_Manual = SWRC_Manual if SWRC_Manual is not None else set()
        self.SWRC_Manual49 = SWRC_Manual49
        
        pass
    @property
    def edition(self):
        return self.__edition

    @edition.setter
    def edition(self, edition: str):
        self.__edition = edition


    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month


    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address


    @property
    def SWRC_Manual(self):
        return self.__SWRC_Manual

    @SWRC_Manual.setter
    def SWRC_Manual(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_Manual__SWRC_Manual", None)
        self.__SWRC_Manual = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person47"):
                    opp_val = getattr(item, "Person47", None)
                    
                    if opp_val == self:
                        setattr(item, "Person47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person47"):
                    opp_val = getattr(item, "Person47", None)
                    
                    setattr(item, "Person47", self)
                    

    @property
    def SWRC_Manual49(self):
        return self.__SWRC_Manual49

    @SWRC_Manual49.setter
    def SWRC_Manual49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_Manual__SWRC_Manual49", None)
        self.__SWRC_Manual49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Organization50"):
                opp_val = getattr(old_value, "Organization50", None)
                if opp_val == self:
                    setattr(old_value, "Organization50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Organization50"):
                opp_val = getattr(value, "Organization50", None)
                setattr(value, "Organization50", self)

class SWRC_Misc(Publication):

    def __init__(self, month: str, howpublished: str, Publication93: "SWRC_PhDStudent" = None, Publication87: "SWRC_AcademicStaff" = None, Publication74: "SWRC_AcademicStaff" = None, Publication106: "SWRC_Organization" = None, Publication: "SWRC_Bibliography" = None):
        self.month = month
        self.howpublished = howpublished
        
        pass
    @property
    def howpublished(self):
        return self.__howpublished

    @howpublished.setter
    def howpublished(self, howpublished: str):
        self.__howpublished = howpublished


    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month


class SWRC_Book(Publication):

    def __init__(self, address: str, month: str, number: str, volume: str, series: str, source: str, edition: str, isbn: str, price: str, SWRC_Book5: "Organization" = None, SWRC_Book: "Person" = None, SWRC_Book7: set["Person"] = None, Publication93: "SWRC_PhDStudent" = None, Publication87: "SWRC_AcademicStaff" = None, Publication74: "SWRC_AcademicStaff" = None, Publication106: "SWRC_Organization" = None, Publication: "SWRC_Bibliography" = None):
        self.address = address
        self.month = month
        self.number = number
        self.volume = volume
        self.series = series
        self.source = source
        self.edition = edition
        self.isbn = isbn
        self.price = price
        self.SWRC_Book5 = SWRC_Book5
        self.SWRC_Book = SWRC_Book
        self.SWRC_Book7 = SWRC_Book7 if SWRC_Book7 is not None else set()
        
        pass
    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: str):
        self.__price = price


    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume: str):
        self.__volume = volume


    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month


    @property
    def edition(self):
        return self.__edition

    @edition.setter
    def edition(self, edition: str):
        self.__edition = edition


    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source


    @property
    def series(self):
        return self.__series

    @series.setter
    def series(self, series: str):
        self.__series = series


    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn: str):
        self.__isbn = isbn


    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address


    @property
    def SWRC_Book7(self):
        return self.__SWRC_Book7

    @SWRC_Book7.setter
    def SWRC_Book7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_Book__SWRC_Book7", None)
        self.__SWRC_Book7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person8"):
                    opp_val = getattr(item, "Person8", None)
                    
                    if opp_val == self:
                        setattr(item, "Person8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person8"):
                    opp_val = getattr(item, "Person8", None)
                    
                    setattr(item, "Person8", self)
                    

    @property
    def SWRC_Book5(self):
        return self.__SWRC_Book5

    @SWRC_Book5.setter
    def SWRC_Book5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_Book__SWRC_Book5", None)
        self.__SWRC_Book5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Organization"):
                opp_val = getattr(old_value, "Organization", None)
                if opp_val == self:
                    setattr(old_value, "Organization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Organization"):
                opp_val = getattr(value, "Organization", None)
                setattr(value, "Organization", self)

    @property
    def SWRC_Book(self):
        return self.__SWRC_Book

    @SWRC_Book.setter
    def SWRC_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_Book__SWRC_Book", None)
        self.__SWRC_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Person3"):
                opp_val = getattr(old_value, "Person3", None)
                if opp_val == self:
                    setattr(old_value, "Person3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Person3"):
                opp_val = getattr(value, "Person3", None)
                setattr(value, "Person3", self)

class SWRC_InCollection(Publication):

    def __init__(self, month: str, number: str, pages: str, address: str, edition: str, volume: str, series: str, chapter: str, type: str, booktitle: str, SWRC_InCollection22: set["Person"] = None, SWRC_InCollection: "Person" = None, SWRC_InCollection25: "Organization" = None, Publication93: "SWRC_PhDStudent" = None, Publication87: "SWRC_AcademicStaff" = None, Publication74: "SWRC_AcademicStaff" = None, Publication106: "SWRC_Organization" = None, Publication: "SWRC_Bibliography" = None):
        self.month = month
        self.number = number
        self.pages = pages
        self.address = address
        self.edition = edition
        self.volume = volume
        self.series = series
        self.chapter = chapter
        self.type = type
        self.booktitle = booktitle
        self.SWRC_InCollection22 = SWRC_InCollection22 if SWRC_InCollection22 is not None else set()
        self.SWRC_InCollection = SWRC_InCollection
        self.SWRC_InCollection25 = SWRC_InCollection25
        
        pass
    @property
    def edition(self):
        return self.__edition

    @edition.setter
    def edition(self, edition: str):
        self.__edition = edition


    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume: str):
        self.__volume = volume


    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month


    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address


    @property
    def chapter(self):
        return self.__chapter

    @chapter.setter
    def chapter(self, chapter: str):
        self.__chapter = chapter


    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages: str):
        self.__pages = pages


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def booktitle(self):
        return self.__booktitle

    @booktitle.setter
    def booktitle(self, booktitle: str):
        self.__booktitle = booktitle


    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number


    @property
    def series(self):
        return self.__series

    @series.setter
    def series(self, series: str):
        self.__series = series


    @property
    def SWRC_InCollection25(self):
        return self.__SWRC_InCollection25

    @SWRC_InCollection25.setter
    def SWRC_InCollection25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_InCollection__SWRC_InCollection25", None)
        self.__SWRC_InCollection25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Organization26"):
                opp_val = getattr(old_value, "Organization26", None)
                if opp_val == self:
                    setattr(old_value, "Organization26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Organization26"):
                opp_val = getattr(value, "Organization26", None)
                setattr(value, "Organization26", self)

    @property
    def SWRC_InCollection22(self):
        return self.__SWRC_InCollection22

    @SWRC_InCollection22.setter
    def SWRC_InCollection22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_InCollection__SWRC_InCollection22", None)
        self.__SWRC_InCollection22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person23"):
                    opp_val = getattr(item, "Person23", None)
                    
                    if opp_val == self:
                        setattr(item, "Person23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person23"):
                    opp_val = getattr(item, "Person23", None)
                    
                    setattr(item, "Person23", self)
                    

    @property
    def SWRC_InCollection(self):
        return self.__SWRC_InCollection

    @SWRC_InCollection.setter
    def SWRC_InCollection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_InCollection__SWRC_InCollection", None)
        self.__SWRC_InCollection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Person20"):
                opp_val = getattr(old_value, "Person20", None)
                if opp_val == self:
                    setattr(old_value, "Person20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Person20"):
                opp_val = getattr(value, "Person20", None)
                setattr(value, "Person20", self)

class SWRC_Article(Publication):

    def __init__(self, journal: str, month: str, number: str, pages: str, volume: str, SWRC_Article: set["Person"] = None, Publication93: "SWRC_PhDStudent" = None, Publication87: "SWRC_AcademicStaff" = None, Publication74: "SWRC_AcademicStaff" = None, Publication106: "SWRC_Organization" = None, Publication: "SWRC_Bibliography" = None):
        self.journal = journal
        self.month = month
        self.number = number
        self.pages = pages
        self.volume = volume
        self.SWRC_Article = SWRC_Article if SWRC_Article is not None else set()
        
        pass
    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages: str):
        self.__pages = pages


    @property
    def journal(self):
        return self.__journal

    @journal.setter
    def journal(self, journal: str):
        self.__journal = journal


    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume: str):
        self.__volume = volume


    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number


    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month


    @property
    def SWRC_Article(self):
        return self.__SWRC_Article

    @SWRC_Article.setter
    def SWRC_Article(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_Article__SWRC_Article", None)
        self.__SWRC_Article = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    if opp_val == self:
                        setattr(item, "Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    setattr(item, "Person", self)
                    

class SWRC_Thesis(Publication):

    def __init__(self, month: str, address: str, type: str, SWRC_Thesis: set["Person"] = None, SWRC_Thesis56: "University" = None, Publication93: "SWRC_PhDStudent" = None, Publication87: "SWRC_AcademicStaff" = None, Publication74: "SWRC_AcademicStaff" = None, Publication106: "SWRC_Organization" = None, Publication: "SWRC_Bibliography" = None):
        self.month = month
        self.address = address
        self.type = type
        self.SWRC_Thesis = SWRC_Thesis if SWRC_Thesis is not None else set()
        self.SWRC_Thesis56 = SWRC_Thesis56
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month


    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address


    @property
    def SWRC_Thesis56(self):
        return self.__SWRC_Thesis56

    @SWRC_Thesis56.setter
    def SWRC_Thesis56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_Thesis__SWRC_Thesis56", None)
        self.__SWRC_Thesis56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "University"):
                opp_val = getattr(old_value, "University", None)
                if opp_val == self:
                    setattr(old_value, "University", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "University"):
                opp_val = getattr(value, "University", None)
                setattr(value, "University", self)

    @property
    def SWRC_Thesis(self):
        return self.__SWRC_Thesis

    @SWRC_Thesis.setter
    def SWRC_Thesis(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SWRC_Thesis__SWRC_Thesis", None)
        self.__SWRC_Thesis = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person54"):
                    opp_val = getattr(item, "Person54", None)
                    
                    if opp_val == self:
                        setattr(item, "Person54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person54"):
                    opp_val = getattr(item, "Person54", None)
                    
                    setattr(item, "Person54", self)
                    

class SWRC_Publication(ABC):

    def __init__(self, title: str, abstract: str, keywords: str, note: str, year: str):
        self.title = title
        self.abstract = abstract
        self.keywords = keywords
        self.note = note
        self.year = year
        
        pass
    @property
    def keywords(self):
        return self.__keywords

    @keywords.setter
    def keywords(self, keywords: str):
        self.__keywords = keywords


    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def abstract(self):
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: str):
        self.__abstract = abstract


    @property
    def note(self):
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note


class SWRC_Bibliography:

    pass