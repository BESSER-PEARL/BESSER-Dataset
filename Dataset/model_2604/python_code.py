from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class project_Project:

    def __init__(self, shortname: str, longname: str, devmail: str, homepage: str, start: date, end: date, project_Project: "project_Foundation" = None, Project: "project_Project" = None, parent: set["project_Project"] = None, Project13: "project_CommitterShip" = None, project: set["project_CommitterShip"] = None, Project8: "project_Project" = None, subprojects: "project_Project" = None, project_Project10: set["project_Person"] = None):
        self.shortname = shortname
        self.longname = longname
        self.devmail = devmail
        self.homepage = homepage
        self.start = start
        self.end = end
        self.project_Project = project_Project
        self.Project = Project
        self.parent = parent if parent is not None else set()
        self.Project13 = Project13
        self.project = project if project is not None else set()
        self.Project8 = Project8
        self.subprojects = subprojects
        self.project_Project10 = project_Project10 if project_Project10 is not None else set()
        
    @property
    def start(self) -> date:
        return self.__start

    @start.setter
    def start(self, start: date):
        self.__start = start

    @property
    def longname(self) -> str:
        return self.__longname

    @longname.setter
    def longname(self, longname: str):
        self.__longname = longname

    @property
    def devmail(self) -> str:
        return self.__devmail

    @devmail.setter
    def devmail(self, devmail: str):
        self.__devmail = devmail

    @property
    def end(self) -> date:
        return self.__end

    @end.setter
    def end(self, end: date):
        self.__end = end

    @property
    def homepage(self) -> str:
        return self.__homepage

    @homepage.setter
    def homepage(self, homepage: str):
        self.__homepage = homepage

    @property
    def shortname(self) -> str:
        return self.__shortname

    @shortname.setter
    def shortname(self, shortname: str):
        self.__shortname = shortname

    @property
    def Project13(self):
        return self.__Project13

    @Project13.setter
    def Project13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Project__Project13", None)
        self.__Project13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "committers"):
                opp_val = getattr(old_value, "committers", None)
                if opp_val == self:
                    setattr(old_value, "committers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "committers"):
                opp_val = getattr(value, "committers", None)
                setattr(value, "committers", self)

    @property
    def Project8(self):
        return self.__Project8

    @Project8.setter
    def Project8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Project__Project8", None)
        self.__Project8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subprojects"):
                opp_val = getattr(old_value, "subprojects", None)
                if opp_val == self:
                    setattr(old_value, "subprojects", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subprojects"):
                opp_val = getattr(value, "subprojects", None)
                setattr(value, "subprojects", self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Project__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Project"):
                    opp_val = getattr(item, "Project", None)
                    
                    if opp_val == self:
                        setattr(item, "Project", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Project"):
                    opp_val = getattr(item, "Project", None)
                    
                    setattr(item, "Project", self)
                    

    @property
    def project(self):
        return self.__project

    @project.setter
    def project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Project__project", None)
        self.__project = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CommitterShip"):
                    opp_val = getattr(item, "CommitterShip", None)
                    
                    if opp_val == self:
                        setattr(item, "CommitterShip", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CommitterShip"):
                    opp_val = getattr(item, "CommitterShip", None)
                    
                    setattr(item, "CommitterShip", self)
                    

    @property
    def Project(self):
        return self.__Project

    @Project.setter
    def Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Project__Project", None)
        self.__Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                if opp_val is None:
                    setattr(value, "parent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def project_Project(self):
        return self.__project_Project

    @project_Project.setter
    def project_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Project__project_Project", None)
        self.__project_Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Foundation"):
                opp_val = getattr(old_value, "project_Foundation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Foundation"):
                opp_val = getattr(value, "project_Foundation", None)
                if opp_val is None:
                    setattr(value, "project_Foundation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def project_Project10(self):
        return self.__project_Project10

    @project_Project10.setter
    def project_Project10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Project__project_Project10", None)
        self.__project_Project10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "project_Person11"):
                    opp_val = getattr(item, "project_Person11", None)
                    
                    if opp_val == self:
                        setattr(item, "project_Person11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "project_Person11"):
                    opp_val = getattr(item, "project_Person11", None)
                    
                    setattr(item, "project_Person11", self)
                    

    @property
    def subprojects(self):
        return self.__subprojects

    @subprojects.setter
    def subprojects(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Project__subprojects", None)
        self.__subprojects = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Project8"):
                opp_val = getattr(old_value, "Project8", None)
                if opp_val == self:
                    setattr(old_value, "Project8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Project8"):
                opp_val = getattr(value, "Project8", None)
                setattr(value, "Project8", self)

class project_Foundation:

    pass
class project_CommitterShip:

    def __init__(self, start: date, end: date, CommitterShip: "project_Project" = None, committers: "project_Project" = None, committerships: "project_Person" = None, CommitterShip16: "project_Person" = None):
        self.start = start
        self.end = end
        self.CommitterShip = CommitterShip
        self.committers = committers
        self.committerships = committerships
        self.CommitterShip16 = CommitterShip16
        
    @property
    def start(self) -> date:
        return self.__start

    @start.setter
    def start(self, start: date):
        self.__start = start

    @property
    def end(self) -> date:
        return self.__end

    @end.setter
    def end(self, end: date):
        self.__end = end

    @property
    def CommitterShip16(self):
        return self.__CommitterShip16

    @CommitterShip16.setter
    def CommitterShip16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_CommitterShip__CommitterShip16", None)
        self.__CommitterShip16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "person"):
                opp_val = getattr(old_value, "person", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "person"):
                opp_val = getattr(value, "person", None)
                if opp_val is None:
                    setattr(value, "person", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def committerships(self):
        return self.__committerships

    @committerships.setter
    def committerships(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_CommitterShip__committerships", None)
        self.__committerships = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Person"):
                opp_val = getattr(old_value, "Person", None)
                if opp_val == self:
                    setattr(old_value, "Person", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Person"):
                opp_val = getattr(value, "Person", None)
                setattr(value, "Person", self)

    @property
    def committers(self):
        return self.__committers

    @committers.setter
    def committers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_CommitterShip__committers", None)
        self.__committers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Project13"):
                opp_val = getattr(old_value, "Project13", None)
                if opp_val == self:
                    setattr(old_value, "Project13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Project13"):
                opp_val = getattr(value, "Project13", None)
                setattr(value, "Project13", self)

    @property
    def CommitterShip(self):
        return self.__CommitterShip

    @CommitterShip.setter
    def CommitterShip(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_CommitterShip__CommitterShip", None)
        self.__CommitterShip = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project"):
                opp_val = getattr(old_value, "project", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project"):
                opp_val = getattr(value, "project", None)
                if opp_val is None:
                    setattr(value, "project", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class project_Person:

    def __init__(self, lastname: str, firstname: str, email: str, image: str, project_Person: "project_Foundation" = None, Person: "project_CommitterShip" = None, project_Person11: "project_Project" = None, person: set["project_CommitterShip"] = None):
        self.lastname = lastname
        self.firstname = firstname
        self.email = email
        self.image = image
        self.project_Person = project_Person
        self.Person = Person
        self.project_Person11 = project_Person11
        self.person = person if person is not None else set()
        
    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def image(self) -> str:
        return self.__image

    @image.setter
    def image(self, image: str):
        self.__image = image

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Person__Person", None)
        self.__Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "committerships"):
                opp_val = getattr(old_value, "committerships", None)
                if opp_val == self:
                    setattr(old_value, "committerships", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "committerships"):
                opp_val = getattr(value, "committerships", None)
                setattr(value, "committerships", self)

    @property
    def project_Person11(self):
        return self.__project_Person11

    @project_Person11.setter
    def project_Person11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Person__project_Person11", None)
        self.__project_Person11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Project10"):
                opp_val = getattr(old_value, "project_Project10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Project10"):
                opp_val = getattr(value, "project_Project10", None)
                if opp_val is None:
                    setattr(value, "project_Project10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def project_Person(self):
        return self.__project_Person

    @project_Person.setter
    def project_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Person__project_Person", None)
        self.__project_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project_Foundation2"):
                opp_val = getattr(old_value, "project_Foundation2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project_Foundation2"):
                opp_val = getattr(value, "project_Foundation2", None)
                if opp_val is None:
                    setattr(value, "project_Foundation2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def person(self):
        return self.__person

    @person.setter
    def person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_project_Person__person", None)
        self.__person = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CommitterShip16"):
                    opp_val = getattr(item, "CommitterShip16", None)
                    
                    if opp_val == self:
                        setattr(item, "CommitterShip16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CommitterShip16"):
                    opp_val = getattr(item, "CommitterShip16", None)
                    
                    setattr(item, "CommitterShip16", self)
                    
