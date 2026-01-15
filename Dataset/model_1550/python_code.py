from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class conf101_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class conf101_RevisionNote:

    pass
class Person:

    pass
class conf101_Researcher(Person):

    pass
class conf101_RevisionProcess:

    pass
class NamedElement:

    pass
class conf101_Location(NamedElement):

    pass
class conf101_Publication(NamedElement):

    pass
class conf101_Evaluation(NamedElement):

    pass
class conf101_Admin(NamedElement):

    pass
class conf101_ProgramComitee(NamedElement):

    pass
class conf101_SteeringComitee(NamedElement):

    pass
class conf101_Contribution(NamedElement):

    pass
class conf101_Person(NamedElement):

    pass
class conf101_Conference(NamedElement):

    pass
class conf101_Laboratory(NamedElement):

    pass
class conf101_Session(NamedElement):

    def __init__(self, year: str, conf101_Session19: "conf101_Conference" = None, conf101_Session: "conf101_Location" = None, conf101_Session9: "conf101_ProgramComitee" = None, conf101_Session11: "conf101_SteeringComitee" = None, conf101_Session13: "conf101_Contribution" = None):
        self.year = year
        self.conf101_Session19 = conf101_Session19
        self.conf101_Session = conf101_Session
        self.conf101_Session9 = conf101_Session9
        self.conf101_Session11 = conf101_Session11
        self.conf101_Session13 = conf101_Session13
        
    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

    @property
    def conf101_Session13(self):
        return self.__conf101_Session13

    @conf101_Session13.setter
    def conf101_Session13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conf101_Session__conf101_Session13", None)
        self.__conf101_Session13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conf101_Contribution"):
                opp_val = getattr(old_value, "conf101_Contribution", None)
                if opp_val == self:
                    setattr(old_value, "conf101_Contribution", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conf101_Contribution"):
                opp_val = getattr(value, "conf101_Contribution", None)
                setattr(value, "conf101_Contribution", self)

    @property
    def conf101_Session9(self):
        return self.__conf101_Session9

    @conf101_Session9.setter
    def conf101_Session9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conf101_Session__conf101_Session9", None)
        self.__conf101_Session9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conf101_ProgramComitee"):
                opp_val = getattr(old_value, "conf101_ProgramComitee", None)
                if opp_val == self:
                    setattr(old_value, "conf101_ProgramComitee", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conf101_ProgramComitee"):
                opp_val = getattr(value, "conf101_ProgramComitee", None)
                setattr(value, "conf101_ProgramComitee", self)

    @property
    def conf101_Session19(self):
        return self.__conf101_Session19

    @conf101_Session19.setter
    def conf101_Session19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conf101_Session__conf101_Session19", None)
        self.__conf101_Session19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conf101_Conference18"):
                opp_val = getattr(old_value, "conf101_Conference18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conf101_Conference18"):
                opp_val = getattr(value, "conf101_Conference18", None)
                if opp_val is None:
                    setattr(value, "conf101_Conference18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def conf101_Session(self):
        return self.__conf101_Session

    @conf101_Session.setter
    def conf101_Session(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conf101_Session__conf101_Session", None)
        self.__conf101_Session = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conf101_Location"):
                opp_val = getattr(old_value, "conf101_Location", None)
                if opp_val == self:
                    setattr(old_value, "conf101_Location", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conf101_Location"):
                opp_val = getattr(value, "conf101_Location", None)
                setattr(value, "conf101_Location", self)

    @property
    def conf101_Session11(self):
        return self.__conf101_Session11

    @conf101_Session11.setter
    def conf101_Session11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conf101_Session__conf101_Session11", None)
        self.__conf101_Session11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conf101_SteeringComitee"):
                opp_val = getattr(old_value, "conf101_SteeringComitee", None)
                if opp_val == self:
                    setattr(old_value, "conf101_SteeringComitee", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conf101_SteeringComitee"):
                opp_val = getattr(value, "conf101_SteeringComitee", None)
                setattr(value, "conf101_SteeringComitee", self)

class conf101_Chapter(NamedElement):

    pass
class conf101_System(NamedElement):

    pass