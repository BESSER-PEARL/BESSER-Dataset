from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class VisibilityKind(Enum):
    Private = "Private"
    Protected = "Protected"
    Public = "Public"
class OpenModeKind(Enum):
    Append = "Append"
    OverWrite = "OverWrite"


############################################
# Definition of Classes
############################################

class Comment:

    pass
class TemplateExpression:

    pass
class cst_TextExpression(TemplateExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cst_Block(TemplateExpression):

    pass
class ModuleElement:

    pass
class cst_Query(ModuleElement):

    def __init__(self, type: str, cst_Query: set["cst_Variable"] = None, cst_Query87: "cst_ModelExpression" = None):
        self.type = type
        self.cst_Query = cst_Query if cst_Query is not None else set()
        self.cst_Query87 = cst_Query87
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def cst_Query87(self):
        return self.__cst_Query87

    @cst_Query87.setter
    def cst_Query87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_Query__cst_Query87", None)
        self.__cst_Query87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_ModelExpression88"):
                opp_val = getattr(old_value, "cst_ModelExpression88", None)
                if opp_val == self:
                    setattr(old_value, "cst_ModelExpression88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_ModelExpression88"):
                opp_val = getattr(value, "cst_ModelExpression88", None)
                setattr(value, "cst_ModelExpression88", self)

    @property
    def cst_Query(self):
        return self.__cst_Query

    @cst_Query.setter
    def cst_Query(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_Query__cst_Query", None)
        self.__cst_Query = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cst_Variable85"):
                    opp_val = getattr(item, "cst_Variable85", None)
                    
                    if opp_val == self:
                        setattr(item, "cst_Variable85", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cst_Variable85"):
                    opp_val = getattr(item, "cst_Variable85", None)
                    
                    setattr(item, "cst_Variable85", self)
                    

class cst_Comment(TemplateExpression, ModuleElement):

    def __init__(self, body: str):
        self.body = body
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

class cst_EPackage:

    pass
class cst_ModelExpression(TemplateExpression):

    def __init__(self, body: str, cst_ModelExpression: "cst_Template" = None, cst_ModelExpression18: "cst_Template" = None, cst_ModelExpression21: "cst_Variable" = None, cst_ModelExpression24: "cst_ModelExpression" = None, cst_ModelExpression22: "cst_ModelExpression" = None, cst_ModelExpression38: "cst_ProtectedAreaBlock" = None, cst_ModelExpression76: "cst_FileBlock" = None, cst_ModelExpression79: "cst_FileBlock" = None, cst_ModelExpression27: "cst_ModelExpression" = None, cst_ModelExpression25: "cst_ModelExpression" = None, cst_ModelExpression30: "cst_ModelExpression" = None, cst_ModelExpression28: "cst_ModelExpression" = None, cst_ModelExpression43: "cst_ForBlock" = None, cst_ModelExpression46: "cst_ForBlock" = None, cst_ModelExpression49: "cst_ForBlock" = None, cst_ModelExpression52: "cst_ForBlock" = None, cst_ModelExpression55: "cst_ForBlock" = None, cst_ModelExpression57: "cst_IfBlock" = None, cst_ModelExpression73: "cst_FileBlock" = None, cst_ModelExpression81: "cst_TraceBlock" = None, cst_ModelExpression88: "cst_Query" = None):
        self.body = body
        self.cst_ModelExpression = cst_ModelExpression
        self.cst_ModelExpression18 = cst_ModelExpression18
        self.cst_ModelExpression21 = cst_ModelExpression21
        self.cst_ModelExpression24 = cst_ModelExpression24
        self.cst_ModelExpression22 = cst_ModelExpression22
        self.cst_ModelExpression38 = cst_ModelExpression38
        self.cst_ModelExpression76 = cst_ModelExpression76
        self.cst_ModelExpression79 = cst_ModelExpression79
        self.cst_ModelExpression27 = cst_ModelExpression27
        self.cst_ModelExpression25 = cst_ModelExpression25
        self.cst_ModelExpression30 = cst_ModelExpression30
        self.cst_ModelExpression28 = cst_ModelExpression28
        self.cst_ModelExpression43 = cst_ModelExpression43
        self.cst_ModelExpression46 = cst_ModelExpression46
        self.cst_ModelExpression49 = cst_ModelExpression49
        self.cst_ModelExpression52 = cst_ModelExpression52
        self.cst_ModelExpression55 = cst_ModelExpression55
        self.cst_ModelExpression57 = cst_ModelExpression57
        self.cst_ModelExpression73 = cst_ModelExpression73
        self.cst_ModelExpression81 = cst_ModelExpression81
        self.cst_ModelExpression88 = cst_ModelExpression88
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def cst_ModelExpression73(self):
        return self.__cst_ModelExpression73

    @cst_ModelExpression73.setter
    def cst_ModelExpression73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_ModelExpression__cst_ModelExpression73", None)
        self.__cst_ModelExpression73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_FileBlock"):
                opp_val = getattr(old_value, "cst_FileBlock", None)
                if opp_val == self:
                    setattr(old_value, "cst_FileBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_FileBlock"):
                opp_val = getattr(value, "cst_FileBlock", None)
                setattr(value, "cst_FileBlock", self)

    @property
    def cst_ModelExpression79(self):
        return self.__cst_ModelExpression79

    @cst_ModelExpression79.setter
    def cst_ModelExpression79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_ModelExpression__cst_ModelExpression79", None)
        self.__cst_ModelExpression79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_FileBlock78"):
                opp_val = getattr(old_value, "cst_FileBlock78", None)
                if opp_val == self:
                    setattr(old_value, "cst_FileBlock78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_FileBlock78"):
                opp_val = getattr(value, "cst_FileBlock78", None)
                setattr(value, "cst_FileBlock78", self)

    @property
    def cst_ModelExpression52(self):
        return self.__cst_ModelExpression52

    @cst_ModelExpression52.setter
    def cst_ModelExpression52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_ModelExpression__cst_ModelExpression52", None)
        self.__cst_ModelExpression52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_ForBlock51"):
                opp_val = getattr(old_value, "cst_ForBlock51", None)
                if opp_val == self:
                    setattr(old_value, "cst_ForBlock51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_ForBlock51"):
                opp_val = getattr(value, "cst_ForBlock51", None)
                setattr(value, "cst_ForBlock51", self)

    @property
    def cst_ModelExpression22(self):
        return self.__cst_ModelExpression22

    @cst_ModelExpression22.setter
    def cst_ModelExpression22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_ModelExpression__cst_ModelExpression22", None)
        self.__cst_ModelExpression22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_ModelExpression24"):
                opp_val = getattr(old_value, "cst_ModelExpression24", None)
                if opp_val == self:
                    setattr(old_value, "cst_ModelExpression24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_ModelExpression24"):
                opp_val = getattr(value, "cst_ModelExpression24", None)
                setattr(value, "cst_ModelExpression24", self)

    @property
    def cst_ModelExpression24(self):
        return self.__cst_ModelExpression24

    @cst_ModelExpression24.setter
    def cst_ModelExpression24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_ModelExpression__cst_ModelExpression24", None)
        self.__cst_ModelExpression24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_ModelExpression22"):
                opp_val = getattr(old_value, "cst_ModelExpression22", None)
                if opp_val == self:
                    setattr(old_value, "cst_ModelExpression22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_ModelExpression22"):
                opp_val = getattr(value, "cst_ModelExpression22", None)
                setattr(value, "cst_ModelExpression22", self)

    @property
    def cst_ModelExpression88(self):
        return self.__cst_ModelExpression88

    @cst_ModelExpression88.setter
    def cst_ModelExpression88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_ModelExpression__cst_ModelExpression88", None)
        self.__cst_ModelExpression88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_Query87"):
                opp_val = getattr(old_value, "cst_Query87", None)
                if opp_val == self:
                    setattr(old_value, "cst_Query87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_Query87"):
                opp_val = getattr(value, "cst_Query87", None)
                setattr(value, "cst_Query87", self)

    @property
    def cst_ModelExpression30(self):
        return self.__cst_ModelExpression30

    @cst_ModelExpression30.setter
    def cst_ModelExpression30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_ModelExpression__cst_ModelExpression30", None)
        self.__cst_ModelExpression30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_ModelExpression28"):
                opp_val = getattr(old_value, "cst_ModelExpression28", None)
                if opp_val == self:
                    setattr(old_value, "cst_ModelExpression28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_ModelExpression28"):
                opp_val = getattr(value, "cst_ModelExpression28", None)
                setattr(value, "cst_ModelExpression28", self)

    @property
    def cst_ModelExpression28(self):
        return self.__cst_ModelExpression28

    @cst_ModelExpression28.setter
    def cst_ModelExpression28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_ModelExpression__cst_ModelExpression28", None)
        self.__cst_ModelExpression28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_ModelExpression30"):
                opp_val = getattr(old_value, "cst_ModelExpression30", None)
                if opp_val == self:
                    setattr(old_value, "cst_ModelExpression30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_ModelExpression30"):
                opp_val = getattr(value, "cst_ModelExpression30", None)
                setattr(value, "cst_ModelExpression30", self)

    @property
    def cst_ModelExpression25(self):
        return self.__cst_ModelExpression25

    @cst_ModelExpression25.setter
    def cst_ModelExpression25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_ModelExpression__cst_ModelExpression25", None)
        self.__cst_ModelExpression25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_ModelExpression27"):
                opp_val = getattr(old_value, "cst_ModelExpression27", None)
                if opp_val == self:
                    setattr(old_value, "cst_ModelExpression27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_ModelExpression27"):
                opp_val = getattr(value, "cst_ModelExpression27", None)
                setattr(value, "cst_ModelExpression27", self)

    @property
    def cst_ModelExpression27(self):
        return self.__cst_ModelExpression27

    @cst_ModelExpression27.setter
    def cst_ModelExpression27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_ModelExpression__cst_ModelExpression27", None)
        self.__cst_ModelExpression27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_ModelExpression25"):
                opp_val = getattr(old_value, "cst_ModelExpression25", None)
                if opp_val == self:
                    setattr(old_value, "cst_ModelExpression25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_ModelExpression25"):
                opp_val = getattr(value, "cst_ModelExpression25", None)
                setattr(value, "cst_ModelExpression25", self)

    @property
    def cst_ModelExpression46(self):
        return self.__cst_ModelExpression46

    @cst_ModelExpression46.setter
    def cst_ModelExpression46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_ModelExpression__cst_ModelExpression46", None)
        self.__cst_ModelExpression46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_ForBlock45"):
                opp_val = getattr(old_value, "cst_ForBlock45", None)
                if opp_val == self:
                    setattr(old_value, "cst_ForBlock45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_ForBlock45"):
                opp_val = getattr(value, "cst_ForBlock45", None)
                setattr(value, "cst_ForBlock45", self)

    @property
    def cst_ModelExpression57(self):
        return self.__cst_ModelExpression57

    @cst_ModelExpression57.setter
    def cst_ModelExpression57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_ModelExpression__cst_ModelExpression57", None)
        self.__cst_ModelExpression57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_IfBlock"):
                opp_val = getattr(old_value, "cst_IfBlock", None)
                if opp_val == self:
                    setattr(old_value, "cst_IfBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_IfBlock"):
                opp_val = getattr(value, "cst_IfBlock", None)
                setattr(value, "cst_IfBlock", self)

    @property
    def cst_ModelExpression76(self):
        return self.__cst_ModelExpression76

    @cst_ModelExpression76.setter
    def cst_ModelExpression76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_ModelExpression__cst_ModelExpression76", None)
        self.__cst_ModelExpression76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_FileBlock75"):
                opp_val = getattr(old_value, "cst_FileBlock75", None)
                if opp_val == self:
                    setattr(old_value, "cst_FileBlock75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_FileBlock75"):
                opp_val = getattr(value, "cst_FileBlock75", None)
                setattr(value, "cst_FileBlock75", self)

    @property
    def cst_ModelExpression38(self):
        return self.__cst_ModelExpression38

    @cst_ModelExpression38.setter
    def cst_ModelExpression38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_ModelExpression__cst_ModelExpression38", None)
        self.__cst_ModelExpression38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_ProtectedAreaBlock"):
                opp_val = getattr(old_value, "cst_ProtectedAreaBlock", None)
                if opp_val == self:
                    setattr(old_value, "cst_ProtectedAreaBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_ProtectedAreaBlock"):
                opp_val = getattr(value, "cst_ProtectedAreaBlock", None)
                setattr(value, "cst_ProtectedAreaBlock", self)

    @property
    def cst_ModelExpression21(self):
        return self.__cst_ModelExpression21

    @cst_ModelExpression21.setter
    def cst_ModelExpression21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_ModelExpression__cst_ModelExpression21", None)
        self.__cst_ModelExpression21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_Variable20"):
                opp_val = getattr(old_value, "cst_Variable20", None)
                if opp_val == self:
                    setattr(old_value, "cst_Variable20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_Variable20"):
                opp_val = getattr(value, "cst_Variable20", None)
                setattr(value, "cst_Variable20", self)

    @property
    def cst_ModelExpression43(self):
        return self.__cst_ModelExpression43

    @cst_ModelExpression43.setter
    def cst_ModelExpression43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_ModelExpression__cst_ModelExpression43", None)
        self.__cst_ModelExpression43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_ForBlock42"):
                opp_val = getattr(old_value, "cst_ForBlock42", None)
                if opp_val == self:
                    setattr(old_value, "cst_ForBlock42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_ForBlock42"):
                opp_val = getattr(value, "cst_ForBlock42", None)
                setattr(value, "cst_ForBlock42", self)

    @property
    def cst_ModelExpression55(self):
        return self.__cst_ModelExpression55

    @cst_ModelExpression55.setter
    def cst_ModelExpression55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_ModelExpression__cst_ModelExpression55", None)
        self.__cst_ModelExpression55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_ForBlock54"):
                opp_val = getattr(old_value, "cst_ForBlock54", None)
                if opp_val == self:
                    setattr(old_value, "cst_ForBlock54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_ForBlock54"):
                opp_val = getattr(value, "cst_ForBlock54", None)
                setattr(value, "cst_ForBlock54", self)

    @property
    def cst_ModelExpression(self):
        return self.__cst_ModelExpression

    @cst_ModelExpression.setter
    def cst_ModelExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_ModelExpression__cst_ModelExpression", None)
        self.__cst_ModelExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_Template15"):
                opp_val = getattr(old_value, "cst_Template15", None)
                if opp_val == self:
                    setattr(old_value, "cst_Template15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_Template15"):
                opp_val = getattr(value, "cst_Template15", None)
                setattr(value, "cst_Template15", self)

    @property
    def cst_ModelExpression49(self):
        return self.__cst_ModelExpression49

    @cst_ModelExpression49.setter
    def cst_ModelExpression49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_ModelExpression__cst_ModelExpression49", None)
        self.__cst_ModelExpression49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_ForBlock48"):
                opp_val = getattr(old_value, "cst_ForBlock48", None)
                if opp_val == self:
                    setattr(old_value, "cst_ForBlock48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_ForBlock48"):
                opp_val = getattr(value, "cst_ForBlock48", None)
                setattr(value, "cst_ForBlock48", self)

    @property
    def cst_ModelExpression81(self):
        return self.__cst_ModelExpression81

    @cst_ModelExpression81.setter
    def cst_ModelExpression81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_ModelExpression__cst_ModelExpression81", None)
        self.__cst_ModelExpression81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_TraceBlock"):
                opp_val = getattr(old_value, "cst_TraceBlock", None)
                if opp_val == self:
                    setattr(old_value, "cst_TraceBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_TraceBlock"):
                opp_val = getattr(value, "cst_TraceBlock", None)
                setattr(value, "cst_TraceBlock", self)

    @property
    def cst_ModelExpression18(self):
        return self.__cst_ModelExpression18

    @cst_ModelExpression18.setter
    def cst_ModelExpression18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_ModelExpression__cst_ModelExpression18", None)
        self.__cst_ModelExpression18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_Template17"):
                opp_val = getattr(old_value, "cst_Template17", None)
                if opp_val == self:
                    setattr(old_value, "cst_Template17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_Template17"):
                opp_val = getattr(value, "cst_Template17", None)
                setattr(value, "cst_Template17", self)

class Block:

    pass
class cst_LetBlock(Block):

    pass
class cst_FileBlock(Block):

    def __init__(self, openMode: str, cst_FileBlock75: "cst_ModelExpression" = None, cst_FileBlock78: "cst_ModelExpression" = None, cst_FileBlock: "cst_ModelExpression" = None):
        self.openMode = openMode
        self.cst_FileBlock75 = cst_FileBlock75
        self.cst_FileBlock78 = cst_FileBlock78
        self.cst_FileBlock = cst_FileBlock
        
    @property
    def openMode(self) -> str:
        return self.__openMode

    @openMode.setter
    def openMode(self, openMode: str):
        self.__openMode = openMode

    @property
    def cst_FileBlock(self):
        return self.__cst_FileBlock

    @cst_FileBlock.setter
    def cst_FileBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_FileBlock__cst_FileBlock", None)
        self.__cst_FileBlock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_ModelExpression73"):
                opp_val = getattr(old_value, "cst_ModelExpression73", None)
                if opp_val == self:
                    setattr(old_value, "cst_ModelExpression73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_ModelExpression73"):
                opp_val = getattr(value, "cst_ModelExpression73", None)
                setattr(value, "cst_ModelExpression73", self)

    @property
    def cst_FileBlock78(self):
        return self.__cst_FileBlock78

    @cst_FileBlock78.setter
    def cst_FileBlock78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_FileBlock__cst_FileBlock78", None)
        self.__cst_FileBlock78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_ModelExpression79"):
                opp_val = getattr(old_value, "cst_ModelExpression79", None)
                if opp_val == self:
                    setattr(old_value, "cst_ModelExpression79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_ModelExpression79"):
                opp_val = getattr(value, "cst_ModelExpression79", None)
                setattr(value, "cst_ModelExpression79", self)

    @property
    def cst_FileBlock75(self):
        return self.__cst_FileBlock75

    @cst_FileBlock75.setter
    def cst_FileBlock75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_FileBlock__cst_FileBlock75", None)
        self.__cst_FileBlock75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_ModelExpression76"):
                opp_val = getattr(old_value, "cst_ModelExpression76", None)
                if opp_val == self:
                    setattr(old_value, "cst_ModelExpression76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_ModelExpression76"):
                opp_val = getattr(value, "cst_ModelExpression76", None)
                setattr(value, "cst_ModelExpression76", self)

class cst_Macro(ModuleElement, Block):

    def __init__(self, type: str, cst_Macro: set["cst_Variable"] = None):
        self.type = type
        self.cst_Macro = cst_Macro if cst_Macro is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def cst_Macro(self):
        return self.__cst_Macro

    @cst_Macro.setter
    def cst_Macro(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_Macro__cst_Macro", None)
        self.__cst_Macro = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cst_Variable83"):
                    opp_val = getattr(item, "cst_Variable83", None)
                    
                    if opp_val == self:
                        setattr(item, "cst_Variable83", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cst_Variable83"):
                    opp_val = getattr(item, "cst_Variable83", None)
                    
                    setattr(item, "cst_Variable83", self)
                    

class cst_ProtectedAreaBlock(Block):

    pass
class cst_TraceBlock(Block):

    pass
class cst_IfBlock(Block):

    pass
class cst_ForBlock(Block):

    pass
class cst_Template(ModuleElement, Block):

    pass
class CSTNode:

    pass
class cst_InitSection(CSTNode):

    pass
class cst_TemplateOverridesValue(CSTNode):

    def __init__(self, name: str, cst_TemplateOverridesValue: "cst_Template" = None):
        self.name = name
        self.cst_TemplateOverridesValue = cst_TemplateOverridesValue
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cst_TemplateOverridesValue(self):
        return self.__cst_TemplateOverridesValue

    @cst_TemplateOverridesValue.setter
    def cst_TemplateOverridesValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_TemplateOverridesValue__cst_TemplateOverridesValue", None)
        self.__cst_TemplateOverridesValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_Template"):
                opp_val = getattr(old_value, "cst_Template", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_Template"):
                opp_val = getattr(value, "cst_Template", None)
                if opp_val is None:
                    setattr(value, "cst_Template", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cst_Variable(CSTNode):

    def __init__(self, name: str, type: str, cst_Variable: "cst_Template" = None, cst_Variable20: "cst_ModelExpression" = None, cst_Variable36: "cst_InitSection" = None, cst_Variable40: "cst_ForBlock" = None, cst_Variable71: "cst_LetBlock" = None, cst_Variable83: "cst_Macro" = None, cst_Variable85: "cst_Query" = None):
        self.name = name
        self.type = type
        self.cst_Variable = cst_Variable
        self.cst_Variable20 = cst_Variable20
        self.cst_Variable36 = cst_Variable36
        self.cst_Variable40 = cst_Variable40
        self.cst_Variable71 = cst_Variable71
        self.cst_Variable83 = cst_Variable83
        self.cst_Variable85 = cst_Variable85
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cst_Variable36(self):
        return self.__cst_Variable36

    @cst_Variable36.setter
    def cst_Variable36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_Variable__cst_Variable36", None)
        self.__cst_Variable36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_InitSection35"):
                opp_val = getattr(old_value, "cst_InitSection35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_InitSection35"):
                opp_val = getattr(value, "cst_InitSection35", None)
                if opp_val is None:
                    setattr(value, "cst_InitSection35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cst_Variable83(self):
        return self.__cst_Variable83

    @cst_Variable83.setter
    def cst_Variable83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_Variable__cst_Variable83", None)
        self.__cst_Variable83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_Macro"):
                opp_val = getattr(old_value, "cst_Macro", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_Macro"):
                opp_val = getattr(value, "cst_Macro", None)
                if opp_val is None:
                    setattr(value, "cst_Macro", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cst_Variable(self):
        return self.__cst_Variable

    @cst_Variable.setter
    def cst_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_Variable__cst_Variable", None)
        self.__cst_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_Template13"):
                opp_val = getattr(old_value, "cst_Template13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_Template13"):
                opp_val = getattr(value, "cst_Template13", None)
                if opp_val is None:
                    setattr(value, "cst_Template13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cst_Variable40(self):
        return self.__cst_Variable40

    @cst_Variable40.setter
    def cst_Variable40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_Variable__cst_Variable40", None)
        self.__cst_Variable40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_ForBlock"):
                opp_val = getattr(old_value, "cst_ForBlock", None)
                if opp_val == self:
                    setattr(old_value, "cst_ForBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_ForBlock"):
                opp_val = getattr(value, "cst_ForBlock", None)
                setattr(value, "cst_ForBlock", self)

    @property
    def cst_Variable85(self):
        return self.__cst_Variable85

    @cst_Variable85.setter
    def cst_Variable85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_Variable__cst_Variable85", None)
        self.__cst_Variable85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_Query"):
                opp_val = getattr(old_value, "cst_Query", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_Query"):
                opp_val = getattr(value, "cst_Query", None)
                if opp_val is None:
                    setattr(value, "cst_Query", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cst_Variable71(self):
        return self.__cst_Variable71

    @cst_Variable71.setter
    def cst_Variable71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_Variable__cst_Variable71", None)
        self.__cst_Variable71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_LetBlock70"):
                opp_val = getattr(old_value, "cst_LetBlock70", None)
                if opp_val == self:
                    setattr(old_value, "cst_LetBlock70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_LetBlock70"):
                opp_val = getattr(value, "cst_LetBlock70", None)
                setattr(value, "cst_LetBlock70", self)

    @property
    def cst_Variable20(self):
        return self.__cst_Variable20

    @cst_Variable20.setter
    def cst_Variable20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_Variable__cst_Variable20", None)
        self.__cst_Variable20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_ModelExpression21"):
                opp_val = getattr(old_value, "cst_ModelExpression21", None)
                if opp_val == self:
                    setattr(old_value, "cst_ModelExpression21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_ModelExpression21"):
                opp_val = getattr(value, "cst_ModelExpression21", None)
                setattr(value, "cst_ModelExpression21", self)

class cst_TemplateExpression(CSTNode):

    pass
class EPackage:

    pass
class cst_Module(CSTNode, EPackage):

    pass
class cst_CSTNode(ABC):

    def __init__(self, startPosition: int, endPosition: int):
        self.startPosition = startPosition
        self.endPosition = endPosition
        
    @property
    def endPosition(self) -> int:
        return self.__endPosition

    @endPosition.setter
    def endPosition(self, endPosition: int):
        self.__endPosition = endPosition

    @property
    def startPosition(self) -> int:
        return self.__startPosition

    @startPosition.setter
    def startPosition(self, startPosition: int):
        self.__startPosition = startPosition

class cst_Documentation(Comment):

    pass
class cst_ModuleImportsValue(CSTNode):

    def __init__(self, name: str, cst_ModuleImportsValue: "cst_Module" = None):
        self.name = name
        self.cst_ModuleImportsValue = cst_ModuleImportsValue
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cst_ModuleImportsValue(self):
        return self.__cst_ModuleImportsValue

    @cst_ModuleImportsValue.setter
    def cst_ModuleImportsValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_ModuleImportsValue__cst_ModuleImportsValue", None)
        self.__cst_ModuleImportsValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_Module6"):
                opp_val = getattr(old_value, "cst_Module6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_Module6"):
                opp_val = getattr(value, "cst_Module6", None)
                if opp_val is None:
                    setattr(value, "cst_Module6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cst_ModuleExtendsValue(CSTNode):

    def __init__(self, name: str, cst_ModuleExtendsValue: "cst_Module" = None):
        self.name = name
        self.cst_ModuleExtendsValue = cst_ModuleExtendsValue
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cst_ModuleExtendsValue(self):
        return self.__cst_ModuleExtendsValue

    @cst_ModuleExtendsValue.setter
    def cst_ModuleExtendsValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_ModuleExtendsValue__cst_ModuleExtendsValue", None)
        self.__cst_ModuleExtendsValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_Module4"):
                opp_val = getattr(old_value, "cst_Module4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_Module4"):
                opp_val = getattr(value, "cst_Module4", None)
                if opp_val is None:
                    setattr(value, "cst_Module4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cst_ModuleElement(CSTNode):

    def __init__(self, name: str, visibility: str, cst_ModuleElement: "cst_Module" = None):
        self.name = name
        self.visibility = visibility
        self.cst_ModuleElement = cst_ModuleElement
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cst_ModuleElement(self):
        return self.__cst_ModuleElement

    @cst_ModuleElement.setter
    def cst_ModuleElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cst_ModuleElement__cst_ModuleElement", None)
        self.__cst_ModuleElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_Module2"):
                opp_val = getattr(old_value, "cst_Module2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_Module2"):
                opp_val = getattr(value, "cst_Module2", None)
                if opp_val is None:
                    setattr(value, "cst_Module2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cst_TypedModel(CSTNode):

    pass