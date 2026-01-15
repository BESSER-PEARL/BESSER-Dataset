from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class conf_Person:

    pass
class conf_RevisionNote:

    pass
class conf_Chapter:

    pass
class conf_Evaluation:

    pass
class Person:

    pass
class conf_Publication:

    pass
class conf_Researcher(Person):

    pass
class conf_Contribution:

    pass
class conf_SteeringComitee:

    pass
class conf_ProgramComitee:

    pass
class conf_Location:

    def __init__(self, name: str, conf_Location: "conf_Session" = None, conf_Location16: "conf_Admin" = None):
        self.name = name
        self.conf_Location = conf_Location
        self.conf_Location16 = conf_Location16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def conf_Location16(self):
        return self.__conf_Location16

    @conf_Location16.setter
    def conf_Location16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conf_Location__conf_Location16", None)
        self.__conf_Location16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conf_Admin15"):
                opp_val = getattr(old_value, "conf_Admin15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conf_Admin15"):
                opp_val = getattr(value, "conf_Admin15", None)
                if opp_val is None:
                    setattr(value, "conf_Admin15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def conf_Location(self):
        return self.__conf_Location

    @conf_Location.setter
    def conf_Location(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conf_Location__conf_Location", None)
        self.__conf_Location = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conf_Session"):
                opp_val = getattr(old_value, "conf_Session", None)
                if opp_val == self:
                    setattr(old_value, "conf_Session", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conf_Session"):
                opp_val = getattr(value, "conf_Session", None)
                setattr(value, "conf_Session", self)

class conf_Session:

    def __init__(self, year: str, conf_Session: "conf_Location" = None, conf_Session9: "conf_ProgramComitee" = None, conf_Session11: "conf_SteeringComitee" = None, conf_Session13: "conf_Contribution" = None, conf_Session19: "conf_Conference" = None):
        self.year = year
        self.conf_Session = conf_Session
        self.conf_Session9 = conf_Session9
        self.conf_Session11 = conf_Session11
        self.conf_Session13 = conf_Session13
        self.conf_Session19 = conf_Session19
        
    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

    @property
    def conf_Session9(self):
        return self.__conf_Session9

    @conf_Session9.setter
    def conf_Session9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conf_Session__conf_Session9", None)
        self.__conf_Session9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conf_ProgramComitee"):
                opp_val = getattr(old_value, "conf_ProgramComitee", None)
                if opp_val == self:
                    setattr(old_value, "conf_ProgramComitee", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conf_ProgramComitee"):
                opp_val = getattr(value, "conf_ProgramComitee", None)
                setattr(value, "conf_ProgramComitee", self)

    @property
    def conf_Session19(self):
        return self.__conf_Session19

    @conf_Session19.setter
    def conf_Session19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conf_Session__conf_Session19", None)
        self.__conf_Session19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conf_Conference18"):
                opp_val = getattr(old_value, "conf_Conference18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conf_Conference18"):
                opp_val = getattr(value, "conf_Conference18", None)
                if opp_val is None:
                    setattr(value, "conf_Conference18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def conf_Session13(self):
        return self.__conf_Session13

    @conf_Session13.setter
    def conf_Session13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conf_Session__conf_Session13", None)
        self.__conf_Session13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conf_Contribution"):
                opp_val = getattr(old_value, "conf_Contribution", None)
                if opp_val == self:
                    setattr(old_value, "conf_Contribution", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conf_Contribution"):
                opp_val = getattr(value, "conf_Contribution", None)
                setattr(value, "conf_Contribution", self)

    @property
    def conf_Session(self):
        return self.__conf_Session

    @conf_Session.setter
    def conf_Session(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conf_Session__conf_Session", None)
        self.__conf_Session = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conf_Location"):
                opp_val = getattr(old_value, "conf_Location", None)
                if opp_val == self:
                    setattr(old_value, "conf_Location", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conf_Location"):
                opp_val = getattr(value, "conf_Location", None)
                setattr(value, "conf_Location", self)

    @property
    def conf_Session11(self):
        return self.__conf_Session11

    @conf_Session11.setter
    def conf_Session11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conf_Session__conf_Session11", None)
        self.__conf_Session11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conf_SteeringComitee"):
                opp_val = getattr(old_value, "conf_SteeringComitee", None)
                if opp_val == self:
                    setattr(old_value, "conf_SteeringComitee", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conf_SteeringComitee"):
                opp_val = getattr(value, "conf_SteeringComitee", None)
                setattr(value, "conf_SteeringComitee", self)

class conf_RevisionProcess:

    pass
class conf_Conference:

    pass
class conf_Laboratory:

    pass
class conf_Admin:

    pass
class conf_System:

    pass