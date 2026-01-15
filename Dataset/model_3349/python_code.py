from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class SJAccessLevel(Enum):
    PRIVATE = "PRIVATE"
    PUBLIC = "PUBLIC"
    PROTECTED = "PROTECTED"


############################################
# Definition of Classes
############################################

class smallJava_SJSymbol:

    def __init__(self, name: str, smallJava_SJSymbol: "smallJava_SJClass" = None, smallJava_SJSymbol41: "smallJava_SJSymbolRef" = None):
        self.name = name
        self.smallJava_SJSymbol = smallJava_SJSymbol
        self.smallJava_SJSymbol41 = smallJava_SJSymbol41
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def smallJava_SJSymbol41(self):
        return self.__smallJava_SJSymbol41

    @smallJava_SJSymbol41.setter
    def smallJava_SJSymbol41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smallJava_SJSymbol__smallJava_SJSymbol41", None)
        self.__smallJava_SJSymbol41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smallJava_SJSymbolRef"):
                opp_val = getattr(old_value, "smallJava_SJSymbolRef", None)
                if opp_val == self:
                    setattr(old_value, "smallJava_SJSymbolRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smallJava_SJSymbolRef"):
                opp_val = getattr(value, "smallJava_SJSymbolRef", None)
                setattr(value, "smallJava_SJSymbolRef", self)

    @property
    def smallJava_SJSymbol(self):
        return self.__smallJava_SJSymbol

    @smallJava_SJSymbol.setter
    def smallJava_SJSymbol(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smallJava_SJSymbol__smallJava_SJSymbol", None)
        self.__smallJava_SJSymbol = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smallJava_SJClass26"):
                opp_val = getattr(old_value, "smallJava_SJClass26", None)
                if opp_val == self:
                    setattr(old_value, "smallJava_SJClass26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smallJava_SJClass26"):
                opp_val = getattr(value, "smallJava_SJClass26", None)
                setattr(value, "smallJava_SJClass26", self)

class smallJava_SJBlock:

    pass
class SJExpression:

    pass
class smallJava_SJIntConstant(SJExpression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class smallJava_SJThis(SJExpression):

    pass
class smallJava_SJNew(SJExpression):

    pass
class smallJava_SJMemberSelection(SJExpression):

    def __init__(self, methodinvocation: bool, smallJava_SJMemberSelection: "smallJava_SJExpression" = None, smallJava_SJMemberSelection35: "smallJava_SJMember" = None, smallJava_SJMemberSelection38: set["smallJava_SJExpression"] = None):
        self.methodinvocation = methodinvocation
        self.smallJava_SJMemberSelection = smallJava_SJMemberSelection
        self.smallJava_SJMemberSelection35 = smallJava_SJMemberSelection35
        self.smallJava_SJMemberSelection38 = smallJava_SJMemberSelection38 if smallJava_SJMemberSelection38 is not None else set()
        
    @property
    def methodinvocation(self) -> bool:
        return self.__methodinvocation

    @methodinvocation.setter
    def methodinvocation(self, methodinvocation: bool):
        self.__methodinvocation = methodinvocation

    @property
    def smallJava_SJMemberSelection(self):
        return self.__smallJava_SJMemberSelection

    @smallJava_SJMemberSelection.setter
    def smallJava_SJMemberSelection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smallJava_SJMemberSelection__smallJava_SJMemberSelection", None)
        self.__smallJava_SJMemberSelection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smallJava_SJExpression33"):
                opp_val = getattr(old_value, "smallJava_SJExpression33", None)
                if opp_val == self:
                    setattr(old_value, "smallJava_SJExpression33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smallJava_SJExpression33"):
                opp_val = getattr(value, "smallJava_SJExpression33", None)
                setattr(value, "smallJava_SJExpression33", self)

    @property
    def smallJava_SJMemberSelection35(self):
        return self.__smallJava_SJMemberSelection35

    @smallJava_SJMemberSelection35.setter
    def smallJava_SJMemberSelection35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smallJava_SJMemberSelection__smallJava_SJMemberSelection35", None)
        self.__smallJava_SJMemberSelection35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smallJava_SJMember36"):
                opp_val = getattr(old_value, "smallJava_SJMember36", None)
                if opp_val == self:
                    setattr(old_value, "smallJava_SJMember36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smallJava_SJMember36"):
                opp_val = getattr(value, "smallJava_SJMember36", None)
                setattr(value, "smallJava_SJMember36", self)

    @property
    def smallJava_SJMemberSelection38(self):
        return self.__smallJava_SJMemberSelection38

    @smallJava_SJMemberSelection38.setter
    def smallJava_SJMemberSelection38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smallJava_SJMemberSelection__smallJava_SJMemberSelection38", None)
        self.__smallJava_SJMemberSelection38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smallJava_SJExpression39"):
                    opp_val = getattr(item, "smallJava_SJExpression39", None)
                    
                    if opp_val == self:
                        setattr(item, "smallJava_SJExpression39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smallJava_SJExpression39"):
                    opp_val = getattr(item, "smallJava_SJExpression39", None)
                    
                    setattr(item, "smallJava_SJExpression39", self)
                    

class smallJava_SJBoolConstant(SJExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class smallJava_SJStringConstant(SJExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class smallJava_SJSymbolRef(SJExpression):

    pass
class smallJava_SJNull(SJExpression):

    pass
class smallJava_SJSuper(SJExpression):

    pass
class smallJava_SJAssignment(SJExpression):

    pass
class SJBlock:

    pass
class smallJava_SJIfBlock(SJBlock):

    pass
class SJSymbol:

    pass
class smallJava_SJMethodBody(SJBlock):

    pass
class smallJava_SJParameter(SJSymbol):

    pass
class SJStatement:

    pass
class smallJava_SJIfStatement(SJStatement):

    pass
class smallJava_SJVariableDeclaration(SJSymbol, SJStatement):

    pass
class smallJava_SJExpression(SJStatement):

    pass
class smallJava_SJReturn(SJStatement):

    pass
class smallJava_SJStatement:

    pass
class SJMember:

    pass
class smallJava_SJMethod(SJMember):

    pass
class smallJava_SJField(SJMember):

    pass
class smallJava_SJMember:

    def __init__(self, access: str, name: str, smallJava_SJMember: "smallJava_SJClass" = None, smallJava_SJMember9: "smallJava_SJClass" = None, smallJava_SJMember36: "smallJava_SJMemberSelection" = None):
        self.access = access
        self.name = name
        self.smallJava_SJMember = smallJava_SJMember
        self.smallJava_SJMember9 = smallJava_SJMember9
        self.smallJava_SJMember36 = smallJava_SJMember36
        
    @property
    def access(self) -> str:
        return self.__access

    @access.setter
    def access(self, access: str):
        self.__access = access

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def smallJava_SJMember(self):
        return self.__smallJava_SJMember

    @smallJava_SJMember.setter
    def smallJava_SJMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smallJava_SJMember__smallJava_SJMember", None)
        self.__smallJava_SJMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smallJava_SJClass7"):
                opp_val = getattr(old_value, "smallJava_SJClass7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smallJava_SJClass7"):
                opp_val = getattr(value, "smallJava_SJClass7", None)
                if opp_val is None:
                    setattr(value, "smallJava_SJClass7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smallJava_SJMember9(self):
        return self.__smallJava_SJMember9

    @smallJava_SJMember9.setter
    def smallJava_SJMember9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smallJava_SJMember__smallJava_SJMember9", None)
        self.__smallJava_SJMember9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smallJava_SJClass10"):
                opp_val = getattr(old_value, "smallJava_SJClass10", None)
                if opp_val == self:
                    setattr(old_value, "smallJava_SJClass10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smallJava_SJClass10"):
                opp_val = getattr(value, "smallJava_SJClass10", None)
                setattr(value, "smallJava_SJClass10", self)

    @property
    def smallJava_SJMember36(self):
        return self.__smallJava_SJMember36

    @smallJava_SJMember36.setter
    def smallJava_SJMember36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smallJava_SJMember__smallJava_SJMember36", None)
        self.__smallJava_SJMember36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smallJava_SJMemberSelection35"):
                opp_val = getattr(old_value, "smallJava_SJMemberSelection35", None)
                if opp_val == self:
                    setattr(old_value, "smallJava_SJMemberSelection35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smallJava_SJMemberSelection35"):
                opp_val = getattr(value, "smallJava_SJMemberSelection35", None)
                setattr(value, "smallJava_SJMemberSelection35", self)

class smallJava_SJClass:

    def __init__(self, name: str, smallJava_SJClass: "smallJava_SJProgram" = None, smallJava_SJClass5: "smallJava_SJClass" = None, smallJava_SJClass3: "smallJava_SJClass" = None, smallJava_SJClass7: set["smallJava_SJMember"] = None, smallJava_SJClass10: "smallJava_SJMember" = None, smallJava_SJClass26: "smallJava_SJSymbol" = None, smallJava_SJClass43: "smallJava_SJNew" = None):
        self.name = name
        self.smallJava_SJClass = smallJava_SJClass
        self.smallJava_SJClass5 = smallJava_SJClass5
        self.smallJava_SJClass3 = smallJava_SJClass3
        self.smallJava_SJClass7 = smallJava_SJClass7 if smallJava_SJClass7 is not None else set()
        self.smallJava_SJClass10 = smallJava_SJClass10
        self.smallJava_SJClass26 = smallJava_SJClass26
        self.smallJava_SJClass43 = smallJava_SJClass43
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def smallJava_SJClass3(self):
        return self.__smallJava_SJClass3

    @smallJava_SJClass3.setter
    def smallJava_SJClass3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smallJava_SJClass__smallJava_SJClass3", None)
        self.__smallJava_SJClass3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smallJava_SJClass5"):
                opp_val = getattr(old_value, "smallJava_SJClass5", None)
                if opp_val == self:
                    setattr(old_value, "smallJava_SJClass5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smallJava_SJClass5"):
                opp_val = getattr(value, "smallJava_SJClass5", None)
                setattr(value, "smallJava_SJClass5", self)

    @property
    def smallJava_SJClass(self):
        return self.__smallJava_SJClass

    @smallJava_SJClass.setter
    def smallJava_SJClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smallJava_SJClass__smallJava_SJClass", None)
        self.__smallJava_SJClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smallJava_SJProgram2"):
                opp_val = getattr(old_value, "smallJava_SJProgram2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smallJava_SJProgram2"):
                opp_val = getattr(value, "smallJava_SJProgram2", None)
                if opp_val is None:
                    setattr(value, "smallJava_SJProgram2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smallJava_SJClass10(self):
        return self.__smallJava_SJClass10

    @smallJava_SJClass10.setter
    def smallJava_SJClass10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smallJava_SJClass__smallJava_SJClass10", None)
        self.__smallJava_SJClass10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smallJava_SJMember9"):
                opp_val = getattr(old_value, "smallJava_SJMember9", None)
                if opp_val == self:
                    setattr(old_value, "smallJava_SJMember9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smallJava_SJMember9"):
                opp_val = getattr(value, "smallJava_SJMember9", None)
                setattr(value, "smallJava_SJMember9", self)

    @property
    def smallJava_SJClass7(self):
        return self.__smallJava_SJClass7

    @smallJava_SJClass7.setter
    def smallJava_SJClass7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smallJava_SJClass__smallJava_SJClass7", None)
        self.__smallJava_SJClass7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smallJava_SJMember"):
                    opp_val = getattr(item, "smallJava_SJMember", None)
                    
                    if opp_val == self:
                        setattr(item, "smallJava_SJMember", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smallJava_SJMember"):
                    opp_val = getattr(item, "smallJava_SJMember", None)
                    
                    setattr(item, "smallJava_SJMember", self)
                    

    @property
    def smallJava_SJClass5(self):
        return self.__smallJava_SJClass5

    @smallJava_SJClass5.setter
    def smallJava_SJClass5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smallJava_SJClass__smallJava_SJClass5", None)
        self.__smallJava_SJClass5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smallJava_SJClass3"):
                opp_val = getattr(old_value, "smallJava_SJClass3", None)
                if opp_val == self:
                    setattr(old_value, "smallJava_SJClass3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smallJava_SJClass3"):
                opp_val = getattr(value, "smallJava_SJClass3", None)
                setattr(value, "smallJava_SJClass3", self)

    @property
    def smallJava_SJClass26(self):
        return self.__smallJava_SJClass26

    @smallJava_SJClass26.setter
    def smallJava_SJClass26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smallJava_SJClass__smallJava_SJClass26", None)
        self.__smallJava_SJClass26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smallJava_SJSymbol"):
                opp_val = getattr(old_value, "smallJava_SJSymbol", None)
                if opp_val == self:
                    setattr(old_value, "smallJava_SJSymbol", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smallJava_SJSymbol"):
                opp_val = getattr(value, "smallJava_SJSymbol", None)
                setattr(value, "smallJava_SJSymbol", self)

    @property
    def smallJava_SJClass43(self):
        return self.__smallJava_SJClass43

    @smallJava_SJClass43.setter
    def smallJava_SJClass43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smallJava_SJClass__smallJava_SJClass43", None)
        self.__smallJava_SJClass43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smallJava_SJNew"):
                opp_val = getattr(old_value, "smallJava_SJNew", None)
                if opp_val == self:
                    setattr(old_value, "smallJava_SJNew", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smallJava_SJNew"):
                opp_val = getattr(value, "smallJava_SJNew", None)
                setattr(value, "smallJava_SJNew", self)

class smallJava_SJImport:

    def __init__(self, importedNamespace: str, smallJava_SJImport: "smallJava_SJProgram" = None):
        self.importedNamespace = importedNamespace
        self.smallJava_SJImport = smallJava_SJImport
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

    @property
    def smallJava_SJImport(self):
        return self.__smallJava_SJImport

    @smallJava_SJImport.setter
    def smallJava_SJImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smallJava_SJImport__smallJava_SJImport", None)
        self.__smallJava_SJImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smallJava_SJProgram"):
                opp_val = getattr(old_value, "smallJava_SJProgram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smallJava_SJProgram"):
                opp_val = getattr(value, "smallJava_SJProgram", None)
                if opp_val is None:
                    setattr(value, "smallJava_SJProgram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class smallJava_SJProgram:

    def __init__(self, name: str, smallJava_SJProgram: set["smallJava_SJImport"] = None, smallJava_SJProgram2: set["smallJava_SJClass"] = None):
        self.name = name
        self.smallJava_SJProgram = smallJava_SJProgram if smallJava_SJProgram is not None else set()
        self.smallJava_SJProgram2 = smallJava_SJProgram2 if smallJava_SJProgram2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def smallJava_SJProgram(self):
        return self.__smallJava_SJProgram

    @smallJava_SJProgram.setter
    def smallJava_SJProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smallJava_SJProgram__smallJava_SJProgram", None)
        self.__smallJava_SJProgram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smallJava_SJImport"):
                    opp_val = getattr(item, "smallJava_SJImport", None)
                    
                    if opp_val == self:
                        setattr(item, "smallJava_SJImport", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smallJava_SJImport"):
                    opp_val = getattr(item, "smallJava_SJImport", None)
                    
                    setattr(item, "smallJava_SJImport", self)
                    

    @property
    def smallJava_SJProgram2(self):
        return self.__smallJava_SJProgram2

    @smallJava_SJProgram2.setter
    def smallJava_SJProgram2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smallJava_SJProgram__smallJava_SJProgram2", None)
        self.__smallJava_SJProgram2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smallJava_SJClass"):
                    opp_val = getattr(item, "smallJava_SJClass", None)
                    
                    if opp_val == self:
                        setattr(item, "smallJava_SJClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smallJava_SJClass"):
                    opp_val = getattr(item, "smallJava_SJClass", None)
                    
                    setattr(item, "smallJava_SJClass", self)
                    
