from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class SJExpression:

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

class smallJava_SJThis(SJExpression):

    pass
class smallJava_BoolConstant(SJExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class smallJava_SJNull(SJExpression):

    pass
class smallJava_SJNew(SJExpression):

    pass
class smallJava_SJSymbolRef(SJExpression):

    pass
class smallJava_SJAssignment(SJExpression):

    pass
class smallJava_SJNamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class SJStatement:

    pass
class smallJava_SJIfStatement(SJStatement):

    pass
class smallJava_SJReturn(SJStatement):

    pass
class smallJava_SJStatement:

    pass
class SJSymbol:

    pass
class smallJava_SJBlock:

    pass
class smallJava_SJParameter(SJSymbol):

    pass
class SJMember:

    pass
class smallJava_SJMethod(SJMember):

    pass
class smallJava_SJField(SJMember):

    pass
class smallJava_SJVariableDeclaration(SJSymbol, SJStatement):

    pass
class smallJava_SJExpression(SJStatement):

    pass
class SJNamedElement:

    pass
class smallJava_SJSymbol(SJNamedElement):

    pass
class smallJava_SJClass(SJNamedElement):

    pass
class smallJava_SJProgram:

    pass
class smallJava_SJMember(SJNamedElement):

    pass