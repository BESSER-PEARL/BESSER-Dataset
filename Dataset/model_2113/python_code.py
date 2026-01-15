from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ESeverity(Enum):
    Medium = "Medium"
    Low = "Low"
    High = "High"
class EAttackMethod(Enum):
    SQLInjection = "SQLInjection"
    XSS = "XSS"
    Authentication = "Authentication"
    Authorization = "Authorization"
    PrivilegeScalation = "PrivilegeScalation"


############################################
# Definition of Classes
############################################

class securityTest_WebComponent:

    def __init__(self, path: str, securityTest_WebComponent13: set["securityTest_Input"] = None, securityTest_WebComponent: "securityTest_TargetOfEvaluation" = None, securityTest_WebComponent11: "securityTest_WebComponent" = None, securityTest_WebComponent9: set["securityTest_WebComponent"] = None):
        self.path = path
        self.securityTest_WebComponent13 = securityTest_WebComponent13 if securityTest_WebComponent13 is not None else set()
        self.securityTest_WebComponent = securityTest_WebComponent
        self.securityTest_WebComponent11 = securityTest_WebComponent11
        self.securityTest_WebComponent9 = securityTest_WebComponent9 if securityTest_WebComponent9 is not None else set()
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def securityTest_WebComponent11(self):
        return self.__securityTest_WebComponent11

    @securityTest_WebComponent11.setter
    def securityTest_WebComponent11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_securityTest_WebComponent__securityTest_WebComponent11", None)
        self.__securityTest_WebComponent11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "securityTest_WebComponent9"):
                opp_val = getattr(old_value, "securityTest_WebComponent9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "securityTest_WebComponent9"):
                opp_val = getattr(value, "securityTest_WebComponent9", None)
                if opp_val is None:
                    setattr(value, "securityTest_WebComponent9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def securityTest_WebComponent9(self):
        return self.__securityTest_WebComponent9

    @securityTest_WebComponent9.setter
    def securityTest_WebComponent9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_securityTest_WebComponent__securityTest_WebComponent9", None)
        self.__securityTest_WebComponent9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "securityTest_WebComponent11"):
                    opp_val = getattr(item, "securityTest_WebComponent11", None)
                    
                    if opp_val == self:
                        setattr(item, "securityTest_WebComponent11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "securityTest_WebComponent11"):
                    opp_val = getattr(item, "securityTest_WebComponent11", None)
                    
                    setattr(item, "securityTest_WebComponent11", self)
                    

    @property
    def securityTest_WebComponent(self):
        return self.__securityTest_WebComponent

    @securityTest_WebComponent.setter
    def securityTest_WebComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_securityTest_WebComponent__securityTest_WebComponent", None)
        self.__securityTest_WebComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "securityTest_TargetOfEvaluation8"):
                opp_val = getattr(old_value, "securityTest_TargetOfEvaluation8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "securityTest_TargetOfEvaluation8"):
                opp_val = getattr(value, "securityTest_TargetOfEvaluation8", None)
                if opp_val is None:
                    setattr(value, "securityTest_TargetOfEvaluation8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def securityTest_WebComponent13(self):
        return self.__securityTest_WebComponent13

    @securityTest_WebComponent13.setter
    def securityTest_WebComponent13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_securityTest_WebComponent__securityTest_WebComponent13", None)
        self.__securityTest_WebComponent13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "securityTest_Input"):
                    opp_val = getattr(item, "securityTest_Input", None)
                    
                    if opp_val == self:
                        setattr(item, "securityTest_Input", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "securityTest_Input"):
                    opp_val = getattr(item, "securityTest_Input", None)
                    
                    setattr(item, "securityTest_Input", self)
                    

class securityTest_AuthSetting:

    def __init__(self, roles: str, usernameParam: str, passwordParam: str, loginTargetURL: str, loginMessagePattern: str, logoutMessagePattern: str, securityTest_AuthSetting: "securityTest_Test" = None):
        self.roles = roles
        self.usernameParam = usernameParam
        self.passwordParam = passwordParam
        self.loginTargetURL = loginTargetURL
        self.loginMessagePattern = loginMessagePattern
        self.logoutMessagePattern = logoutMessagePattern
        self.securityTest_AuthSetting = securityTest_AuthSetting
        
    @property
    def loginTargetURL(self) -> str:
        return self.__loginTargetURL

    @loginTargetURL.setter
    def loginTargetURL(self, loginTargetURL: str):
        self.__loginTargetURL = loginTargetURL

    @property
    def passwordParam(self) -> str:
        return self.__passwordParam

    @passwordParam.setter
    def passwordParam(self, passwordParam: str):
        self.__passwordParam = passwordParam

    @property
    def loginMessagePattern(self) -> str:
        return self.__loginMessagePattern

    @loginMessagePattern.setter
    def loginMessagePattern(self, loginMessagePattern: str):
        self.__loginMessagePattern = loginMessagePattern

    @property
    def logoutMessagePattern(self) -> str:
        return self.__logoutMessagePattern

    @logoutMessagePattern.setter
    def logoutMessagePattern(self, logoutMessagePattern: str):
        self.__logoutMessagePattern = logoutMessagePattern

    @property
    def roles(self) -> str:
        return self.__roles

    @roles.setter
    def roles(self, roles: str):
        self.__roles = roles

    @property
    def usernameParam(self) -> str:
        return self.__usernameParam

    @usernameParam.setter
    def usernameParam(self, usernameParam: str):
        self.__usernameParam = usernameParam

    @property
    def securityTest_AuthSetting(self):
        return self.__securityTest_AuthSetting

    @securityTest_AuthSetting.setter
    def securityTest_AuthSetting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_securityTest_AuthSetting__securityTest_AuthSetting", None)
        self.__securityTest_AuthSetting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "securityTest_Test6"):
                opp_val = getattr(old_value, "securityTest_Test6", None)
                if opp_val == self:
                    setattr(old_value, "securityTest_Test6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "securityTest_Test6"):
                opp_val = getattr(value, "securityTest_Test6", None)
                setattr(value, "securityTest_Test6", self)

class securityTest_Input:

    def __init__(self, name: str, securityTest_Input: "securityTest_WebComponent" = None, securityTest_Input15: set["securityTest_Attack"] = None):
        self.name = name
        self.securityTest_Input = securityTest_Input
        self.securityTest_Input15 = securityTest_Input15 if securityTest_Input15 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def securityTest_Input15(self):
        return self.__securityTest_Input15

    @securityTest_Input15.setter
    def securityTest_Input15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_securityTest_Input__securityTest_Input15", None)
        self.__securityTest_Input15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "securityTest_Attack16"):
                    opp_val = getattr(item, "securityTest_Attack16", None)
                    
                    if opp_val == self:
                        setattr(item, "securityTest_Attack16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "securityTest_Attack16"):
                    opp_val = getattr(item, "securityTest_Attack16", None)
                    
                    setattr(item, "securityTest_Attack16", self)
                    

    @property
    def securityTest_Input(self):
        return self.__securityTest_Input

    @securityTest_Input.setter
    def securityTest_Input(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_securityTest_Input__securityTest_Input", None)
        self.__securityTest_Input = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "securityTest_WebComponent13"):
                opp_val = getattr(old_value, "securityTest_WebComponent13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "securityTest_WebComponent13"):
                opp_val = getattr(value, "securityTest_WebComponent13", None)
                if opp_val is None:
                    setattr(value, "securityTest_WebComponent13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class securityTest_Attack:

    def __init__(self, name: str, severity: str, securityTest_Attack: "securityTest_Test" = None, securityTest_Attack16: "securityTest_Input" = None):
        self.name = name
        self.severity = severity
        self.securityTest_Attack = securityTest_Attack
        self.securityTest_Attack16 = securityTest_Attack16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def severity(self) -> str:
        return self.__severity

    @severity.setter
    def severity(self, severity: str):
        self.__severity = severity

    @property
    def securityTest_Attack(self):
        return self.__securityTest_Attack

    @securityTest_Attack.setter
    def securityTest_Attack(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_securityTest_Attack__securityTest_Attack", None)
        self.__securityTest_Attack = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "securityTest_Test2"):
                opp_val = getattr(old_value, "securityTest_Test2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "securityTest_Test2"):
                opp_val = getattr(value, "securityTest_Test2", None)
                if opp_val is None:
                    setattr(value, "securityTest_Test2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def securityTest_Attack16(self):
        return self.__securityTest_Attack16

    @securityTest_Attack16.setter
    def securityTest_Attack16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_securityTest_Attack__securityTest_Attack16", None)
        self.__securityTest_Attack16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "securityTest_Input15"):
                opp_val = getattr(old_value, "securityTest_Input15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "securityTest_Input15"):
                opp_val = getattr(value, "securityTest_Input15", None)
                if opp_val is None:
                    setattr(value, "securityTest_Input15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class securityTest_TargetOfEvaluation:

    def __init__(self, domain: str, ip: str, protocol: str, port: str, securityTest_TargetOfEvaluation: "securityTest_Test" = None, securityTest_TargetOfEvaluation8: set["securityTest_WebComponent"] = None):
        self.domain = domain
        self.ip = ip
        self.protocol = protocol
        self.port = port
        self.securityTest_TargetOfEvaluation = securityTest_TargetOfEvaluation
        self.securityTest_TargetOfEvaluation8 = securityTest_TargetOfEvaluation8 if securityTest_TargetOfEvaluation8 is not None else set()
        
    @property
    def protocol(self) -> str:
        return self.__protocol

    @protocol.setter
    def protocol(self, protocol: str):
        self.__protocol = protocol

    @property
    def port(self) -> str:
        return self.__port

    @port.setter
    def port(self, port: str):
        self.__port = port

    @property
    def domain(self) -> str:
        return self.__domain

    @domain.setter
    def domain(self, domain: str):
        self.__domain = domain

    @property
    def ip(self) -> str:
        return self.__ip

    @ip.setter
    def ip(self, ip: str):
        self.__ip = ip

    @property
    def securityTest_TargetOfEvaluation8(self):
        return self.__securityTest_TargetOfEvaluation8

    @securityTest_TargetOfEvaluation8.setter
    def securityTest_TargetOfEvaluation8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_securityTest_TargetOfEvaluation__securityTest_TargetOfEvaluation8", None)
        self.__securityTest_TargetOfEvaluation8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "securityTest_WebComponent"):
                    opp_val = getattr(item, "securityTest_WebComponent", None)
                    
                    if opp_val == self:
                        setattr(item, "securityTest_WebComponent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "securityTest_WebComponent"):
                    opp_val = getattr(item, "securityTest_WebComponent", None)
                    
                    setattr(item, "securityTest_WebComponent", self)
                    

    @property
    def securityTest_TargetOfEvaluation(self):
        return self.__securityTest_TargetOfEvaluation

    @securityTest_TargetOfEvaluation.setter
    def securityTest_TargetOfEvaluation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_securityTest_TargetOfEvaluation__securityTest_TargetOfEvaluation", None)
        self.__securityTest_TargetOfEvaluation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "securityTest_Test"):
                opp_val = getattr(old_value, "securityTest_Test", None)
                if opp_val == self:
                    setattr(old_value, "securityTest_Test", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "securityTest_Test"):
                opp_val = getattr(value, "securityTest_Test", None)
                setattr(value, "securityTest_Test", self)

class securityTest_Test:

    def __init__(self, date: date, name: str, severity: str, id: str, securityTest_Test4: "securityTest_Note" = None, securityTest_Test: "securityTest_TargetOfEvaluation" = None, securityTest_Test2: set["securityTest_Attack"] = None, securityTest_Test6: "securityTest_AuthSetting" = None):
        self.date = date
        self.name = name
        self.severity = severity
        self.id = id
        self.securityTest_Test4 = securityTest_Test4
        self.securityTest_Test = securityTest_Test
        self.securityTest_Test2 = securityTest_Test2 if securityTest_Test2 is not None else set()
        self.securityTest_Test6 = securityTest_Test6
        
    @property
    def severity(self) -> str:
        return self.__severity

    @severity.setter
    def severity(self, severity: str):
        self.__severity = severity

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def securityTest_Test(self):
        return self.__securityTest_Test

    @securityTest_Test.setter
    def securityTest_Test(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_securityTest_Test__securityTest_Test", None)
        self.__securityTest_Test = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "securityTest_TargetOfEvaluation"):
                opp_val = getattr(old_value, "securityTest_TargetOfEvaluation", None)
                if opp_val == self:
                    setattr(old_value, "securityTest_TargetOfEvaluation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "securityTest_TargetOfEvaluation"):
                opp_val = getattr(value, "securityTest_TargetOfEvaluation", None)
                setattr(value, "securityTest_TargetOfEvaluation", self)

    @property
    def securityTest_Test4(self):
        return self.__securityTest_Test4

    @securityTest_Test4.setter
    def securityTest_Test4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_securityTest_Test__securityTest_Test4", None)
        self.__securityTest_Test4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "securityTest_Note"):
                opp_val = getattr(old_value, "securityTest_Note", None)
                if opp_val == self:
                    setattr(old_value, "securityTest_Note", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "securityTest_Note"):
                opp_val = getattr(value, "securityTest_Note", None)
                setattr(value, "securityTest_Note", self)

    @property
    def securityTest_Test6(self):
        return self.__securityTest_Test6

    @securityTest_Test6.setter
    def securityTest_Test6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_securityTest_Test__securityTest_Test6", None)
        self.__securityTest_Test6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "securityTest_AuthSetting"):
                opp_val = getattr(old_value, "securityTest_AuthSetting", None)
                if opp_val == self:
                    setattr(old_value, "securityTest_AuthSetting", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "securityTest_AuthSetting"):
                opp_val = getattr(value, "securityTest_AuthSetting", None)
                setattr(value, "securityTest_AuthSetting", self)

    @property
    def securityTest_Test2(self):
        return self.__securityTest_Test2

    @securityTest_Test2.setter
    def securityTest_Test2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_securityTest_Test__securityTest_Test2", None)
        self.__securityTest_Test2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "securityTest_Attack"):
                    opp_val = getattr(item, "securityTest_Attack", None)
                    
                    if opp_val == self:
                        setattr(item, "securityTest_Attack", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "securityTest_Attack"):
                    opp_val = getattr(item, "securityTest_Attack", None)
                    
                    setattr(item, "securityTest_Attack", self)
                    

class securityTest_Note:

    def __init__(self, noteText: str, securityTest_Note: "securityTest_Test" = None):
        self.noteText = noteText
        self.securityTest_Note = securityTest_Note
        
    @property
    def noteText(self) -> str:
        return self.__noteText

    @noteText.setter
    def noteText(self, noteText: str):
        self.__noteText = noteText

    @property
    def securityTest_Note(self):
        return self.__securityTest_Note

    @securityTest_Note.setter
    def securityTest_Note(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_securityTest_Note__securityTest_Note", None)
        self.__securityTest_Note = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "securityTest_Test4"):
                opp_val = getattr(old_value, "securityTest_Test4", None)
                if opp_val == self:
                    setattr(old_value, "securityTest_Test4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "securityTest_Test4"):
                opp_val = getattr(value, "securityTest_Test4", None)
                setattr(value, "securityTest_Test4", self)
