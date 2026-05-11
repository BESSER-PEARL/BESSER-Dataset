from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class TeamPersonKind(Enum):
    captain = "captain"
    member = "member"
class Gender(Enum):
    male = "male"
    female = "female"
    unknown = "unknown"


############################################
# Definition of Classes
############################################

class grudi_TeamLine:

    def __init__(self, id: str, kind: str, versionNumber: str, lines: "grudi_Team" = None, grudi_TeamLine: "grudi_PersonInfo" = None, TeamLine: "grudi_Team" = None):
        self.id = id
        self.kind = kind
        self.versionNumber = versionNumber
        self.lines = lines
        self.grudi_TeamLine = grudi_TeamLine
        self.TeamLine = TeamLine
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def versionNumber(self):
        return self.__versionNumber

    @versionNumber.setter
    def versionNumber(self, versionNumber: str):
        self.__versionNumber = versionNumber


    @property
    def TeamLine(self):
        return self.__TeamLine

    @TeamLine.setter
    def TeamLine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grudi_TeamLine__TeamLine", None)
        self.__TeamLine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "team"):
                opp_val = getattr(old_value, "team", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "team"):
                opp_val = getattr(value, "team", None)
                if opp_val is None:
                    setattr(value, "team", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lines(self):
        return self.__lines

    @lines.setter
    def lines(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grudi_TeamLine__lines", None)
        self.__lines = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Team"):
                opp_val = getattr(old_value, "Team", None)
                if opp_val == self:
                    setattr(old_value, "Team", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Team"):
                opp_val = getattr(value, "Team", None)
                setattr(value, "Team", self)

    @property
    def grudi_TeamLine(self):
        return self.__grudi_TeamLine

    @grudi_TeamLine.setter
    def grudi_TeamLine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grudi_TeamLine__grudi_TeamLine", None)
        self.__grudi_TeamLine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grudi_PersonInfo"):
                opp_val = getattr(old_value, "grudi_PersonInfo", None)
                if opp_val == self:
                    setattr(old_value, "grudi_PersonInfo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grudi_PersonInfo"):
                opp_val = getattr(value, "grudi_PersonInfo", None)
                setattr(value, "grudi_PersonInfo", self)

class grudi_Team:

    def __init__(self, id: str, name: str, versionNumber: str, Team: "grudi_TeamLine" = None, team: set["grudi_TeamLine"] = None):
        self.id = id
        self.name = name
        self.versionNumber = versionNumber
        self.Team = Team
        self.team = team if team is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def versionNumber(self):
        return self.__versionNumber

    @versionNumber.setter
    def versionNumber(self, versionNumber: str):
        self.__versionNumber = versionNumber


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def Team(self):
        return self.__Team

    @Team.setter
    def Team(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grudi_Team__Team", None)
        self.__Team = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lines"):
                opp_val = getattr(old_value, "lines", None)
                if opp_val == self:
                    setattr(old_value, "lines", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lines"):
                opp_val = getattr(value, "lines", None)
                setattr(value, "lines", self)

    @property
    def team(self):
        return self.__team

    @team.setter
    def team(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grudi_Team__team", None)
        self.__team = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TeamLine"):
                    opp_val = getattr(item, "TeamLine", None)
                    
                    if opp_val == self:
                        setattr(item, "TeamLine", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TeamLine"):
                    opp_val = getattr(item, "TeamLine", None)
                    
                    setattr(item, "TeamLine", self)
                    

class grudi_PersonInfo:

    def __init__(self, id: str, userName: str, name: str, phoneNumber: str, gender: str, grudi_PersonInfo: "grudi_TeamLine" = None):
        self.id = id
        self.userName = userName
        self.name = name
        self.phoneNumber = phoneNumber
        self.gender = gender
        self.grudi_PersonInfo = grudi_PersonInfo
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def phoneNumber(self):
        return self.__phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: str):
        self.__phoneNumber = phoneNumber


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender


    @property
    def userName(self):
        return self.__userName

    @userName.setter
    def userName(self, userName: str):
        self.__userName = userName


    @property
    def grudi_PersonInfo(self):
        return self.__grudi_PersonInfo

    @grudi_PersonInfo.setter
    def grudi_PersonInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grudi_PersonInfo__grudi_PersonInfo", None)
        self.__grudi_PersonInfo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grudi_TeamLine"):
                opp_val = getattr(old_value, "grudi_TeamLine", None)
                if opp_val == self:
                    setattr(old_value, "grudi_TeamLine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grudi_TeamLine"):
                opp_val = getattr(value, "grudi_TeamLine", None)
                setattr(value, "grudi_TeamLine", self)

class grudi_Person:

    def __init__(self, email: str, password: str, name: str, phoneNumber: str, id: str, username: str, gender: str, address: str, versionNumber: str):
        self.email = email
        self.password = password
        self.name = name
        self.phoneNumber = phoneNumber
        self.id = id
        self.username = username
        self.gender = gender
        self.address = address
        self.versionNumber = versionNumber
        
        pass
    @property
    def phoneNumber(self):
        return self.__phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: str):
        self.__phoneNumber = phoneNumber


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def versionNumber(self):
        return self.__versionNumber

    @versionNumber.setter
    def versionNumber(self, versionNumber: str):
        self.__versionNumber = versionNumber


    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username


    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address


    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password


    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

