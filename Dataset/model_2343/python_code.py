from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Gender(Enum):
    male = "male"
    female = "female"
    unknown = "unknown"
class TeamPersonKind(Enum):
    captain = "captain"
    member = "member"


############################################
# Definition of Classes
############################################

class grudi_PersonInfo:

    def __init__(self, gender: str, id: str, userName: str, name: str, phoneNumber: str, grudi_PersonInfo: "grudi_TeamLine" = None):
        self.gender = gender
        self.id = id
        self.userName = userName
        self.name = name
        self.phoneNumber = phoneNumber
        self.grudi_PersonInfo = grudi_PersonInfo
        
    @property
    def gender(self) -> str:
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def userName(self) -> str:
        return self.__userName

    @userName.setter
    def userName(self, userName: str):
        self.__userName = userName

    @property
    def phoneNumber(self) -> str:
        return self.__phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: str):
        self.__phoneNumber = phoneNumber

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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

class grudi_TeamLine:

    def __init__(self, id: str, kind: str, versionNumber: str, TeamLine: "grudi_Team" = None, lines: "grudi_Team" = None, grudi_TeamLine: "grudi_PersonInfo" = None):
        self.id = id
        self.kind = kind
        self.versionNumber = versionNumber
        self.TeamLine = TeamLine
        self.lines = lines
        self.grudi_TeamLine = grudi_TeamLine
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def versionNumber(self) -> str:
        return self.__versionNumber

    @versionNumber.setter
    def versionNumber(self, versionNumber: str):
        self.__versionNumber = versionNumber

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

class grudi_Team:

    def __init__(self, versionNumber: str, id: str, name: str, team: set["grudi_TeamLine"] = None, Team: "grudi_TeamLine" = None):
        self.versionNumber = versionNumber
        self.id = id
        self.name = name
        self.team = team if team is not None else set()
        self.Team = Team
        
    @property
    def versionNumber(self) -> str:
        return self.__versionNumber

    @versionNumber.setter
    def versionNumber(self, versionNumber: str):
        self.__versionNumber = versionNumber

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
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
                    

class grudi_Person:

    def __init__(self, id: str, username: str, email: str, password: str, name: str, phoneNumber: str, gender: str, address: str, versionNumber: str):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.name = name
        self.phoneNumber = phoneNumber
        self.gender = gender
        self.address = address
        self.versionNumber = versionNumber
        
    @property
    def gender(self) -> str:
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def versionNumber(self) -> str:
        return self.__versionNumber

    @versionNumber.setter
    def versionNumber(self, versionNumber: str):
        self.__versionNumber = versionNumber

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def phoneNumber(self) -> str:
        return self.__phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: str):
        self.__phoneNumber = phoneNumber

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id
