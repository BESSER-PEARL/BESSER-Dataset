from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AsmType(Enum):
    function = "function"
    subasm = "subasm"
class AccessUpdateType(Enum):
    access = "access"
    update = "update"


############################################
# Definition of Classes
############################################

class Extension:

    pass
class ElseIf:

    pass
class FunctionOrVariableTerm:

    pass
class Constant:

    pass
class ASM_IntegerConstant(Constant):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class ASM_UndefConstant(Constant):

    pass
class ASM_StringConstant(Constant):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class ASM_BooleanConstant(Constant):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class Universe:

    pass
class Term:

    pass
class ASM_OperatorTerm(Term):

    def __init__(self, opName: str, ASM_OperatorTerm: "Term" = None, ASM_OperatorTerm30: "Term" = None, Term63: "ASM_ConditionalRule" = None, Term93: "ASM_ReturnRule" = None, Term73: "ASM_ElseIf" = None, Term58: "ASM_DoForallRule" = None, Term44: "ASM_ChooseRule" = None, Term33: "ASM_AsmInvocation" = None, Term37: "ASM_UpdateRule" = None, Term28: "ASM_OperatorTerm" = None, Term26: "ASM_FunctionOrVariableTerm" = None, Term: "ASM_Function" = None, Term31: "ASM_OperatorTerm" = None):
        self.opName = opName
        self.ASM_OperatorTerm = ASM_OperatorTerm
        self.ASM_OperatorTerm30 = ASM_OperatorTerm30
        
        pass
    @property
    def opName(self):
        return self.__opName

    @opName.setter
    def opName(self, opName: str):
        self.__opName = opName


    @property
    def ASM_OperatorTerm30(self):
        return self.__ASM_OperatorTerm30

    @ASM_OperatorTerm30.setter
    def ASM_OperatorTerm30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASM_OperatorTerm__ASM_OperatorTerm30", None)
        self.__ASM_OperatorTerm30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Term31"):
                opp_val = getattr(old_value, "Term31", None)
                if opp_val == self:
                    setattr(old_value, "Term31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Term31"):
                opp_val = getattr(value, "Term31", None)
                setattr(value, "Term31", self)

    @property
    def ASM_OperatorTerm(self):
        return self.__ASM_OperatorTerm

    @ASM_OperatorTerm.setter
    def ASM_OperatorTerm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASM_OperatorTerm__ASM_OperatorTerm", None)
        self.__ASM_OperatorTerm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Term28"):
                opp_val = getattr(old_value, "Term28", None)
                if opp_val == self:
                    setattr(old_value, "Term28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Term28"):
                opp_val = getattr(value, "Term28", None)
                setattr(value, "Term28", self)

class ASM_FunctionOrVariableTerm(Term):

    pass
class ASM_Constant(Term):

    pass
class Parameter:

    pass
class ElementDecl:

    pass
class ASM_VariableDecl(ElementDecl):

    pass
class Function:

    pass
class VariableDecl:

    pass
class ASM_Argument(VariableDecl):

    def __init__(self, type: str, VariableDecl88: "ASM_Extension" = None, VariableDecl: "ASM_ChooseRule" = None, VariableDecl52: "ASM_DoForallRule" = None):
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class AccessUpdateFunction:

    pass
class Rule:

    pass
class ASM_AsmInvocation(Rule):

    def __init__(self, asmName: str, ASM_AsmInvocation: set["Term"] = None, Rule22: "ASM_Initialization" = None, Rule79: "ASM_ElseIf" = None, Rule69: "ASM_ConditionalRule" = None, Rule76: "ASM_ElseIf" = None, Rule66: "ASM_ConditionalRule" = None, Rule: "ASM_Body" = None, Rule50: "ASM_ChooseRule" = None, Rule86: "ASM_ExtendRule" = None, Rule47: "ASM_ChooseRule" = None, Rule61: "ASM_DoForallRule" = None):
        self.asmName = asmName
        self.ASM_AsmInvocation = ASM_AsmInvocation if ASM_AsmInvocation is not None else set()
        
        pass
    @property
    def asmName(self):
        return self.__asmName

    @asmName.setter
    def asmName(self, asmName: str):
        self.__asmName = asmName


    @property
    def ASM_AsmInvocation(self):
        return self.__ASM_AsmInvocation

    @ASM_AsmInvocation.setter
    def ASM_AsmInvocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASM_AsmInvocation__ASM_AsmInvocation", None)
        self.__ASM_AsmInvocation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Term33"):
                    opp_val = getattr(item, "Term33", None)
                    
                    if opp_val == self:
                        setattr(item, "Term33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Term33"):
                    opp_val = getattr(item, "Term33", None)
                    
                    setattr(item, "Term33", self)
                    

class ASM_ExtendRule(Rule):

    pass
class ASM_UpdateRule(Rule):

    pass
class ASM_DoForallRule(Rule):

    pass
class ASM_SkipRule(Rule):

    pass
class ASM_ChooseRule(Rule):

    pass
class ASM_ReturnRule(Rule):

    pass
class ASM_ConditionalRule(Rule):

    pass
class Initialization:

    pass
class Declaration:

    pass
class ASM_Function(ElementDecl, Declaration):

    def __init__(self, returnType: str, isExternal: str, ASM_Function: set["Parameter"] = None, ASM_Function19: "Term" = None, Declaration: "ASM_Body" = None, ElementDecl: "ASM_FunctionOrVariableTerm" = None):
        self.returnType = returnType
        self.isExternal = isExternal
        self.ASM_Function = ASM_Function if ASM_Function is not None else set()
        self.ASM_Function19 = ASM_Function19
        
        pass
    @property
    def returnType(self):
        return self.__returnType

    @returnType.setter
    def returnType(self, returnType: str):
        self.__returnType = returnType


    @property
    def isExternal(self):
        return self.__isExternal

    @isExternal.setter
    def isExternal(self, isExternal: str):
        self.__isExternal = isExternal


    @property
    def ASM_Function19(self):
        return self.__ASM_Function19

    @ASM_Function19.setter
    def ASM_Function19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASM_Function__ASM_Function19", None)
        self.__ASM_Function19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Term"):
                opp_val = getattr(old_value, "Term", None)
                if opp_val == self:
                    setattr(old_value, "Term", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Term"):
                opp_val = getattr(value, "Term", None)
                setattr(value, "Term", self)

    @property
    def ASM_Function(self):
        return self.__ASM_Function

    @ASM_Function.setter
    def ASM_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASM_Function__ASM_Function", None)
        self.__ASM_Function = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    setattr(item, "Parameter", self)
                    

class ASM_Universe(Declaration):

    def __init__(self, name: str, contents: str, ASM_Universe: set["Universe"] = None, Declaration: "ASM_Body" = None):
        self.name = name
        self.contents = contents
        self.ASM_Universe = ASM_Universe if ASM_Universe is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def contents(self):
        return self.__contents

    @contents.setter
    def contents(self, contents: str):
        self.__contents = contents


    @property
    def ASM_Universe(self):
        return self.__ASM_Universe

    @ASM_Universe.setter
    def ASM_Universe(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASM_Universe__ASM_Universe", None)
        self.__ASM_Universe = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Universe"):
                    opp_val = getattr(item, "Universe", None)
                    
                    if opp_val == self:
                        setattr(item, "Universe", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Universe"):
                    opp_val = getattr(item, "Universe", None)
                    
                    setattr(item, "Universe", self)
                    

class Argument:

    pass
class Body:

    pass
class MetaInformation:

    pass
class Signature:

    pass
class Asm:

    pass
class XAsmFile:

    pass
class ASM_Body(XAsmFile):

    pass
class ASM_XAsmSpec(XAsmFile):

    pass
class LocatedElement:

    pass
class ASM_Parameter(LocatedElement):

    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class ASM_Signature(LocatedElement):

    def __init__(self, isMain: str, name: str, ASM_Signature: set["Argument"] = None):
        self.isMain = isMain
        self.name = name
        self.ASM_Signature = ASM_Signature if ASM_Signature is not None else set()
        
        pass
    @property
    def isMain(self):
        return self.__isMain

    @isMain.setter
    def isMain(self, isMain: str):
        self.__isMain = isMain


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def ASM_Signature(self):
        return self.__ASM_Signature

    @ASM_Signature.setter
    def ASM_Signature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASM_Signature__ASM_Signature", None)
        self.__ASM_Signature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Argument"):
                    opp_val = getattr(item, "Argument", None)
                    
                    if opp_val == self:
                        setattr(item, "Argument", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Argument"):
                    opp_val = getattr(item, "Argument", None)
                    
                    setattr(item, "Argument", self)
                    

class ASM_Initialization(LocatedElement):

    pass
class ASM_AccessUpdateFunction(LocatedElement):

    def __init__(self, type: str, ASM_AccessUpdateFunction: set["Function"] = None):
        self.type = type
        self.ASM_AccessUpdateFunction = ASM_AccessUpdateFunction if ASM_AccessUpdateFunction is not None else set()
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def ASM_AccessUpdateFunction(self):
        return self.__ASM_AccessUpdateFunction

    @ASM_AccessUpdateFunction.setter
    def ASM_AccessUpdateFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASM_AccessUpdateFunction__ASM_AccessUpdateFunction", None)
        self.__ASM_AccessUpdateFunction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Function"):
                    opp_val = getattr(item, "Function", None)
                    
                    if opp_val == self:
                        setattr(item, "Function", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function"):
                    opp_val = getattr(item, "Function", None)
                    
                    setattr(item, "Function", self)
                    

class ASM_ElementDecl(LocatedElement):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class ASM_Rule(LocatedElement):

    def __init__(self, inSequence: str):
        self.inSequence = inSequence
        
        pass
    @property
    def inSequence(self):
        return self.__inSequence

    @inSequence.setter
    def inSequence(self, inSequence: str):
        self.__inSequence = inSequence


class ASM_Extension(LocatedElement):

    pass
class ASM_Declaration(LocatedElement):

    pass
class ASM_MetaInformation(LocatedElement):

    def __init__(self, usedAs: str, ASM_MetaInformation: set["Signature"] = None, ASM_MetaInformation15: set["AccessUpdateFunction"] = None):
        self.usedAs = usedAs
        self.ASM_MetaInformation = ASM_MetaInformation if ASM_MetaInformation is not None else set()
        self.ASM_MetaInformation15 = ASM_MetaInformation15 if ASM_MetaInformation15 is not None else set()
        
        pass
    @property
    def usedAs(self):
        return self.__usedAs

    @usedAs.setter
    def usedAs(self, usedAs: str):
        self.__usedAs = usedAs


    @property
    def ASM_MetaInformation15(self):
        return self.__ASM_MetaInformation15

    @ASM_MetaInformation15.setter
    def ASM_MetaInformation15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASM_MetaInformation__ASM_MetaInformation15", None)
        self.__ASM_MetaInformation15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AccessUpdateFunction"):
                    opp_val = getattr(item, "AccessUpdateFunction", None)
                    
                    if opp_val == self:
                        setattr(item, "AccessUpdateFunction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AccessUpdateFunction"):
                    opp_val = getattr(item, "AccessUpdateFunction", None)
                    
                    setattr(item, "AccessUpdateFunction", self)
                    

    @property
    def ASM_MetaInformation(self):
        return self.__ASM_MetaInformation

    @ASM_MetaInformation.setter
    def ASM_MetaInformation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASM_MetaInformation__ASM_MetaInformation", None)
        self.__ASM_MetaInformation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Signature13"):
                    opp_val = getattr(item, "Signature13", None)
                    
                    if opp_val == self:
                        setattr(item, "Signature13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Signature13"):
                    opp_val = getattr(item, "Signature13", None)
                    
                    setattr(item, "Signature13", self)
                    

class ASM_ElseIf(LocatedElement):

    pass
class ASM_Asm(LocatedElement):

    def __init__(self, returnType: str, ASM_Asm: "Signature" = None, ASM_Asm3: "MetaInformation" = None, ASM_Asm5: "Body" = None):
        self.returnType = returnType
        self.ASM_Asm = ASM_Asm
        self.ASM_Asm3 = ASM_Asm3
        self.ASM_Asm5 = ASM_Asm5
        
        pass
    @property
    def returnType(self):
        return self.__returnType

    @returnType.setter
    def returnType(self, returnType: str):
        self.__returnType = returnType


    @property
    def ASM_Asm3(self):
        return self.__ASM_Asm3

    @ASM_Asm3.setter
    def ASM_Asm3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASM_Asm__ASM_Asm3", None)
        self.__ASM_Asm3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetaInformation"):
                opp_val = getattr(old_value, "MetaInformation", None)
                if opp_val == self:
                    setattr(old_value, "MetaInformation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetaInformation"):
                opp_val = getattr(value, "MetaInformation", None)
                setattr(value, "MetaInformation", self)

    @property
    def ASM_Asm5(self):
        return self.__ASM_Asm5

    @ASM_Asm5.setter
    def ASM_Asm5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASM_Asm__ASM_Asm5", None)
        self.__ASM_Asm5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Body"):
                opp_val = getattr(old_value, "Body", None)
                if opp_val == self:
                    setattr(old_value, "Body", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Body"):
                opp_val = getattr(value, "Body", None)
                setattr(value, "Body", self)

    @property
    def ASM_Asm(self):
        return self.__ASM_Asm

    @ASM_Asm.setter
    def ASM_Asm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASM_Asm__ASM_Asm", None)
        self.__ASM_Asm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Signature"):
                opp_val = getattr(old_value, "Signature", None)
                if opp_val == self:
                    setattr(old_value, "Signature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Signature"):
                opp_val = getattr(value, "Signature", None)
                setattr(value, "Signature", self)

class ASM_Term(LocatedElement):

    pass
class ASM_XAsmFile(LocatedElement):

    pass
class ASM_LocatedElement(ABC):

    def __init__(self, location: str):
        self.location = location
        
        pass
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

