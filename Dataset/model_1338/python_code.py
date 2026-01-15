from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SampleClause(Enum):
    equals = "equals"
    distinct = "distinct"
class Repeat(Enum):
    yes = "yes"
    no = "no"
class Operator(Enum):
    equals = "equals"
    different = "different"
    in = "in"
    is = "is"
    not = "not"
    gt = "gt"
    gte = "gte"
    lt = "lt"
    lte = "lte"
class LogicOperator(Enum):
    and = "and"
    or = "or"
class ArithmeticOperator(Enum):
    module = "module"
    add = "add"
    subtract = "subtract"
    multiply = "multiply"
    divide = "divide"


############################################
# Definition of Classes
############################################

class BooleanLiteralExpCS:

    pass
class mutatorenvironment_miniOCL_BooleanExpCS(BooleanLiteralExpCS):

    def __init__(self, boolSymbol: bool):
        self.boolSymbol = boolSymbol
        
    @property
    def boolSymbol(self) -> bool:
        return self.__boolSymbol

    @boolSymbol.setter
    def boolSymbol(self, boolSymbol: bool):
        self.__boolSymbol = boolSymbol

class miniOCL_mutatorenvironment_EStructuralFeature:

    pass
class mutatorenvironment_miniOCL_NavigationPathCS:

    pass
class NavigationPathCS:

    pass
class mutatorenvironment_miniOCL_NavigationPathVariableCS(NavigationPathCS):

    def __init__(self, varName: str, NavigationPathCS: "mutatorenvironment_miniOCL_NavigationPathNameCS"):
        self.varName = varName
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

class mutatorenvironment_miniOCL_NavigationPathElementCS(NavigationPathCS):

    pass
class mutatorenvironment_miniOCL_NavigationPathNameCS:

    pass
class NavigationPathNameCS:

    pass
class mutatorenvironment_miniOCL_AccVarCS:

    def __init__(self, accVarName: str, mutatorenvironment_miniOCL_AccVarCS: "PathNameCS" = None, mutatorenvironment_miniOCL_AccVarCS255: "ExpCS" = None):
        self.accVarName = accVarName
        self.mutatorenvironment_miniOCL_AccVarCS = mutatorenvironment_miniOCL_AccVarCS
        self.mutatorenvironment_miniOCL_AccVarCS255 = mutatorenvironment_miniOCL_AccVarCS255
        
    @property
    def accVarName(self) -> str:
        return self.__accVarName

    @accVarName.setter
    def accVarName(self, accVarName: str):
        self.__accVarName = accVarName

    @property
    def mutatorenvironment_miniOCL_AccVarCS(self):
        return self.__mutatorenvironment_miniOCL_AccVarCS

    @mutatorenvironment_miniOCL_AccVarCS.setter
    def mutatorenvironment_miniOCL_AccVarCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_miniOCL_AccVarCS__mutatorenvironment_miniOCL_AccVarCS", None)
        self.__mutatorenvironment_miniOCL_AccVarCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PathNameCS253"):
                opp_val = getattr(old_value, "PathNameCS253", None)
                if opp_val == self:
                    setattr(old_value, "PathNameCS253", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PathNameCS253"):
                opp_val = getattr(value, "PathNameCS253", None)
                setattr(value, "PathNameCS253", self)

    @property
    def mutatorenvironment_miniOCL_AccVarCS255(self):
        return self.__mutatorenvironment_miniOCL_AccVarCS255

    @mutatorenvironment_miniOCL_AccVarCS255.setter
    def mutatorenvironment_miniOCL_AccVarCS255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_miniOCL_AccVarCS__mutatorenvironment_miniOCL_AccVarCS255", None)
        self.__mutatorenvironment_miniOCL_AccVarCS255 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ExpCS256"):
                opp_val = getattr(old_value, "ExpCS256", None)
                if opp_val == self:
                    setattr(old_value, "ExpCS256", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ExpCS256"):
                opp_val = getattr(value, "ExpCS256", None)
                setattr(value, "ExpCS256", self)

class AccVarCS:

    pass
class mutatorenvironment_miniOCL_IteratorVarCS:

    def __init__(self, itName: str, mutatorenvironment_miniOCL_IteratorVarCS: "PathNameCS" = None):
        self.itName = itName
        self.mutatorenvironment_miniOCL_IteratorVarCS = mutatorenvironment_miniOCL_IteratorVarCS
        
    @property
    def itName(self) -> str:
        return self.__itName

    @itName.setter
    def itName(self, itName: str):
        self.__itName = itName

    @property
    def mutatorenvironment_miniOCL_IteratorVarCS(self):
        return self.__mutatorenvironment_miniOCL_IteratorVarCS

    @mutatorenvironment_miniOCL_IteratorVarCS.setter
    def mutatorenvironment_miniOCL_IteratorVarCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_miniOCL_IteratorVarCS__mutatorenvironment_miniOCL_IteratorVarCS", None)
        self.__mutatorenvironment_miniOCL_IteratorVarCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PathNameCS250"):
                opp_val = getattr(old_value, "PathNameCS250", None)
                if opp_val == self:
                    setattr(old_value, "PathNameCS250", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PathNameCS250"):
                opp_val = getattr(value, "PathNameCS250", None)
                setattr(value, "PathNameCS250", self)

class LoopExpCS:

    pass
class mutatorenvironment_miniOCL_ExistsExpCS(LoopExpCS):

    pass
class mutatorenvironment_miniOCL_ForAllExpCS(LoopExpCS):

    pass
class mutatorenvironment_miniOCL_IterateExpCS(LoopExpCS):

    pass
class mutatorenvironment_miniOCL_CollectExpCS(LoopExpCS):

    pass
class IteratorVarCS:

    pass
class mutatorenvironment_miniOCL_PathCS:

    pass
class PathCS:

    pass
class mutatorenvironment_miniOCL_PathElementCS(PathCS):

    pass
class mutatorenvironment_miniOCL_PathVariableCS(PathCS):

    def __init__(self, varName: str, PathCS: "mutatorenvironment_miniOCL_PathNameCS"):
        self.varName = varName
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

class mutatorenvironment_miniOCL_PathNameCS:

    pass
class LiteralExpCS:

    pass
class mutatorenvironment_miniOCL_BooleanLiteralExpCS(LiteralExpCS):

    pass
class mutatorenvironment_miniOCL_StringLiteralExpCS(LiteralExpCS):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
    @property
    def stringSymbol(self) -> str:
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol

class mutatorenvironment_miniOCL_IntLiteralExpCS(LiteralExpCS):

    def __init__(self, intSymbol: int):
        self.intSymbol = intSymbol
        
    @property
    def intSymbol(self) -> int:
        return self.__intSymbol

    @intSymbol.setter
    def intSymbol(self, intSymbol: int):
        self.__intSymbol = intSymbol

class mutatorenvironment_miniOCL_RoundedBracketClauseCS:

    pass
class OperationCS:

    pass
class LogicExpCS:

    pass
class mutatorenvironment_miniOCL_ExpCS:

    pass
class mutatorenvironment_miniOCL_InvariantCS:

    pass
class mutatorenvironment_miniOCL_ConstraintCS:

    pass
class RoundedBracketClauseCS:

    pass
class mutatorenvironment_miniOCL_ParameterCS:

    def __init__(self, name: str, mutatorenvironment_miniOCL_ParameterCS: "PathNameCS" = None):
        self.name = name
        self.mutatorenvironment_miniOCL_ParameterCS = mutatorenvironment_miniOCL_ParameterCS
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mutatorenvironment_miniOCL_ParameterCS(self):
        return self.__mutatorenvironment_miniOCL_ParameterCS

    @mutatorenvironment_miniOCL_ParameterCS.setter
    def mutatorenvironment_miniOCL_ParameterCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_miniOCL_ParameterCS__mutatorenvironment_miniOCL_ParameterCS", None)
        self.__mutatorenvironment_miniOCL_ParameterCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PathNameCS223"):
                opp_val = getattr(old_value, "PathNameCS223", None)
                if opp_val == self:
                    setattr(old_value, "PathNameCS223", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PathNameCS223"):
                opp_val = getattr(value, "PathNameCS223", None)
                setattr(value, "PathNameCS223", self)

class ExpCS:

    pass
class mutatorenvironment_miniOCL_LogicExpCS(ExpCS):

    def __init__(self, op: str, mutatorenvironment_miniOCL_LogicExpCS233: "CallExpCS" = None, mutatorenvironment_miniOCL_LogicExpCS: "LogicExpCS" = None, ExpCS248: "mutatorenvironment_miniOCL_LoopExpCS", ExpCS: "mutatorenvironment_miniOCL_OperationCS", ExpCS256: "mutatorenvironment_miniOCL_AccVarCS", ExpCS258: "mutatorenvironment_miniOCL_RoundedBracketClauseCS", ExpCS230: "mutatorenvironment_miniOCL_InvariantCS"):
        self.op = op
        self.mutatorenvironment_miniOCL_LogicExpCS233 = mutatorenvironment_miniOCL_LogicExpCS233
        self.mutatorenvironment_miniOCL_LogicExpCS = mutatorenvironment_miniOCL_LogicExpCS
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def mutatorenvironment_miniOCL_LogicExpCS233(self):
        return self.__mutatorenvironment_miniOCL_LogicExpCS233

    @mutatorenvironment_miniOCL_LogicExpCS233.setter
    def mutatorenvironment_miniOCL_LogicExpCS233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_miniOCL_LogicExpCS__mutatorenvironment_miniOCL_LogicExpCS233", None)
        self.__mutatorenvironment_miniOCL_LogicExpCS233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CallExpCS"):
                opp_val = getattr(old_value, "CallExpCS", None)
                if opp_val == self:
                    setattr(old_value, "CallExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CallExpCS"):
                opp_val = getattr(value, "CallExpCS", None)
                setattr(value, "CallExpCS", self)

    @property
    def mutatorenvironment_miniOCL_LogicExpCS(self):
        return self.__mutatorenvironment_miniOCL_LogicExpCS

    @mutatorenvironment_miniOCL_LogicExpCS.setter
    def mutatorenvironment_miniOCL_LogicExpCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_miniOCL_LogicExpCS__mutatorenvironment_miniOCL_LogicExpCS", None)
        self.__mutatorenvironment_miniOCL_LogicExpCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LogicExpCS"):
                opp_val = getattr(old_value, "LogicExpCS", None)
                if opp_val == self:
                    setattr(old_value, "LogicExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LogicExpCS"):
                opp_val = getattr(value, "LogicExpCS", None)
                setattr(value, "LogicExpCS", self)

class PrimaryExpCS:

    pass
class mutatorenvironment_miniOCL_LiteralExpCS(PrimaryExpCS):

    pass
class mutatorenvironment_miniOCL_NavigationExpCS(PrimaryExpCS):

    pass
class NavigationExpCS:

    pass
class mutatorenvironment_miniOCL_NavigationNameExpCS(NavigationExpCS):

    pass
class mutatorenvironment_miniOCL_LoopExpCS(NavigationExpCS):

    def __init__(self, logicOp: str, mutatorenvironment_miniOCL_LoopExpCS: "IteratorVarCS" = None, mutatorenvironment_miniOCL_LoopExpCS247: set["ExpCS"] = None, NavigationExpCS: "mutatorenvironment_miniOCL_CallExpCS"):
        self.logicOp = logicOp
        self.mutatorenvironment_miniOCL_LoopExpCS = mutatorenvironment_miniOCL_LoopExpCS
        self.mutatorenvironment_miniOCL_LoopExpCS247 = mutatorenvironment_miniOCL_LoopExpCS247 if mutatorenvironment_miniOCL_LoopExpCS247 is not None else set()
        
    @property
    def logicOp(self) -> str:
        return self.__logicOp

    @logicOp.setter
    def logicOp(self, logicOp: str):
        self.__logicOp = logicOp

    @property
    def mutatorenvironment_miniOCL_LoopExpCS(self):
        return self.__mutatorenvironment_miniOCL_LoopExpCS

    @mutatorenvironment_miniOCL_LoopExpCS.setter
    def mutatorenvironment_miniOCL_LoopExpCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_miniOCL_LoopExpCS__mutatorenvironment_miniOCL_LoopExpCS", None)
        self.__mutatorenvironment_miniOCL_LoopExpCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IteratorVarCS"):
                opp_val = getattr(old_value, "IteratorVarCS", None)
                if opp_val == self:
                    setattr(old_value, "IteratorVarCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IteratorVarCS"):
                opp_val = getattr(value, "IteratorVarCS", None)
                setattr(value, "IteratorVarCS", self)

    @property
    def mutatorenvironment_miniOCL_LoopExpCS247(self):
        return self.__mutatorenvironment_miniOCL_LoopExpCS247

    @mutatorenvironment_miniOCL_LoopExpCS247.setter
    def mutatorenvironment_miniOCL_LoopExpCS247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_miniOCL_LoopExpCS__mutatorenvironment_miniOCL_LoopExpCS247", None)
        self.__mutatorenvironment_miniOCL_LoopExpCS247 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExpCS248"):
                    opp_val = getattr(item, "ExpCS248", None)
                    
                    if opp_val == self:
                        setattr(item, "ExpCS248", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExpCS248"):
                    opp_val = getattr(item, "ExpCS248", None)
                    
                    setattr(item, "ExpCS248", self)
                    

class mutatorenvironment_miniOCL_NameExpCS(NavigationExpCS):

    pass
class ParameterCS:

    pass
class mutatorenvironment_miniOCL_OperationCS:

    def __init__(self, name: str, mutatorenvironment_miniOCL_OperationCS: set["ParameterCS"] = None, mutatorenvironment_miniOCL_OperationCS218: "PathNameCS" = None, mutatorenvironment_miniOCL_OperationCS221: "ExpCS" = None):
        self.name = name
        self.mutatorenvironment_miniOCL_OperationCS = mutatorenvironment_miniOCL_OperationCS if mutatorenvironment_miniOCL_OperationCS is not None else set()
        self.mutatorenvironment_miniOCL_OperationCS218 = mutatorenvironment_miniOCL_OperationCS218
        self.mutatorenvironment_miniOCL_OperationCS221 = mutatorenvironment_miniOCL_OperationCS221
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mutatorenvironment_miniOCL_OperationCS218(self):
        return self.__mutatorenvironment_miniOCL_OperationCS218

    @mutatorenvironment_miniOCL_OperationCS218.setter
    def mutatorenvironment_miniOCL_OperationCS218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_miniOCL_OperationCS__mutatorenvironment_miniOCL_OperationCS218", None)
        self.__mutatorenvironment_miniOCL_OperationCS218 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PathNameCS219"):
                opp_val = getattr(old_value, "PathNameCS219", None)
                if opp_val == self:
                    setattr(old_value, "PathNameCS219", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PathNameCS219"):
                opp_val = getattr(value, "PathNameCS219", None)
                setattr(value, "PathNameCS219", self)

    @property
    def mutatorenvironment_miniOCL_OperationCS(self):
        return self.__mutatorenvironment_miniOCL_OperationCS

    @mutatorenvironment_miniOCL_OperationCS.setter
    def mutatorenvironment_miniOCL_OperationCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_miniOCL_OperationCS__mutatorenvironment_miniOCL_OperationCS", None)
        self.__mutatorenvironment_miniOCL_OperationCS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ParameterCS"):
                    opp_val = getattr(item, "ParameterCS", None)
                    
                    if opp_val == self:
                        setattr(item, "ParameterCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ParameterCS"):
                    opp_val = getattr(item, "ParameterCS", None)
                    
                    setattr(item, "ParameterCS", self)
                    

    @property
    def mutatorenvironment_miniOCL_OperationCS221(self):
        return self.__mutatorenvironment_miniOCL_OperationCS221

    @mutatorenvironment_miniOCL_OperationCS221.setter
    def mutatorenvironment_miniOCL_OperationCS221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_miniOCL_OperationCS__mutatorenvironment_miniOCL_OperationCS221", None)
        self.__mutatorenvironment_miniOCL_OperationCS221 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ExpCS"):
                opp_val = getattr(old_value, "ExpCS", None)
                if opp_val == self:
                    setattr(old_value, "ExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ExpCS"):
                opp_val = getattr(value, "ExpCS", None)
                setattr(value, "ExpCS", self)

class mutatorenvironment_miniOCL_CallExpCS(LogicExpCS):

    pass
class CallExpCS:

    pass
class mutatorenvironment_miniOCL_PrimaryExpCS(CallExpCS):

    pass
class mutatorenvironment_miniOCL_PropertyCS:

    def __init__(self, name: str, mutatorenvironment_miniOCL_PropertyCS: "PathNameCS" = None):
        self.name = name
        self.mutatorenvironment_miniOCL_PropertyCS = mutatorenvironment_miniOCL_PropertyCS
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mutatorenvironment_miniOCL_PropertyCS(self):
        return self.__mutatorenvironment_miniOCL_PropertyCS

    @mutatorenvironment_miniOCL_PropertyCS.setter
    def mutatorenvironment_miniOCL_PropertyCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_miniOCL_PropertyCS__mutatorenvironment_miniOCL_PropertyCS", None)
        self.__mutatorenvironment_miniOCL_PropertyCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PathNameCS215"):
                opp_val = getattr(old_value, "PathNameCS215", None)
                if opp_val == self:
                    setattr(old_value, "PathNameCS215", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PathNameCS215"):
                opp_val = getattr(value, "PathNameCS215", None)
                setattr(value, "PathNameCS215", self)

class PropertyCS:

    pass
class PathNameCS:

    pass
class mutatorenvironment_miniOCL_ClassCS:

    def __init__(self, name: str, mutatorenvironment_miniOCL_ClassCS: "PathNameCS" = None, mutatorenvironment_miniOCL_ClassCS211: set["PropertyCS"] = None, mutatorenvironment_miniOCL_ClassCS213: set["OperationCS"] = None):
        self.name = name
        self.mutatorenvironment_miniOCL_ClassCS = mutatorenvironment_miniOCL_ClassCS
        self.mutatorenvironment_miniOCL_ClassCS211 = mutatorenvironment_miniOCL_ClassCS211 if mutatorenvironment_miniOCL_ClassCS211 is not None else set()
        self.mutatorenvironment_miniOCL_ClassCS213 = mutatorenvironment_miniOCL_ClassCS213 if mutatorenvironment_miniOCL_ClassCS213 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mutatorenvironment_miniOCL_ClassCS211(self):
        return self.__mutatorenvironment_miniOCL_ClassCS211

    @mutatorenvironment_miniOCL_ClassCS211.setter
    def mutatorenvironment_miniOCL_ClassCS211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_miniOCL_ClassCS__mutatorenvironment_miniOCL_ClassCS211", None)
        self.__mutatorenvironment_miniOCL_ClassCS211 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PropertyCS"):
                    opp_val = getattr(item, "PropertyCS", None)
                    
                    if opp_val == self:
                        setattr(item, "PropertyCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PropertyCS"):
                    opp_val = getattr(item, "PropertyCS", None)
                    
                    setattr(item, "PropertyCS", self)
                    

    @property
    def mutatorenvironment_miniOCL_ClassCS(self):
        return self.__mutatorenvironment_miniOCL_ClassCS

    @mutatorenvironment_miniOCL_ClassCS.setter
    def mutatorenvironment_miniOCL_ClassCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_miniOCL_ClassCS__mutatorenvironment_miniOCL_ClassCS", None)
        self.__mutatorenvironment_miniOCL_ClassCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PathNameCS"):
                opp_val = getattr(old_value, "PathNameCS", None)
                if opp_val == self:
                    setattr(old_value, "PathNameCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PathNameCS"):
                opp_val = getattr(value, "PathNameCS", None)
                setattr(value, "PathNameCS", self)

    @property
    def mutatorenvironment_miniOCL_ClassCS213(self):
        return self.__mutatorenvironment_miniOCL_ClassCS213

    @mutatorenvironment_miniOCL_ClassCS213.setter
    def mutatorenvironment_miniOCL_ClassCS213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_miniOCL_ClassCS__mutatorenvironment_miniOCL_ClassCS213", None)
        self.__mutatorenvironment_miniOCL_ClassCS213 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OperationCS"):
                    opp_val = getattr(item, "OperationCS", None)
                    
                    if opp_val == self:
                        setattr(item, "OperationCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OperationCS"):
                    opp_val = getattr(item, "OperationCS", None)
                    
                    setattr(item, "OperationCS", self)
                    

class ClassCS:

    pass
class mutatorenvironment_miniOCL_PackageCS:

    def __init__(self, name: str, mutatorenvironment_miniOCL_PackageCS: set["PackageCS"] = None, mutatorenvironment_miniOCL_PackageCS208: set["ClassCS"] = None):
        self.name = name
        self.mutatorenvironment_miniOCL_PackageCS = mutatorenvironment_miniOCL_PackageCS if mutatorenvironment_miniOCL_PackageCS is not None else set()
        self.mutatorenvironment_miniOCL_PackageCS208 = mutatorenvironment_miniOCL_PackageCS208 if mutatorenvironment_miniOCL_PackageCS208 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mutatorenvironment_miniOCL_PackageCS(self):
        return self.__mutatorenvironment_miniOCL_PackageCS

    @mutatorenvironment_miniOCL_PackageCS.setter
    def mutatorenvironment_miniOCL_PackageCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_miniOCL_PackageCS__mutatorenvironment_miniOCL_PackageCS", None)
        self.__mutatorenvironment_miniOCL_PackageCS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PackageCS206"):
                    opp_val = getattr(item, "PackageCS206", None)
                    
                    if opp_val == self:
                        setattr(item, "PackageCS206", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PackageCS206"):
                    opp_val = getattr(item, "PackageCS206", None)
                    
                    setattr(item, "PackageCS206", self)
                    

    @property
    def mutatorenvironment_miniOCL_PackageCS208(self):
        return self.__mutatorenvironment_miniOCL_PackageCS208

    @mutatorenvironment_miniOCL_PackageCS208.setter
    def mutatorenvironment_miniOCL_PackageCS208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_miniOCL_PackageCS__mutatorenvironment_miniOCL_PackageCS208", None)
        self.__mutatorenvironment_miniOCL_PackageCS208 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassCS"):
                    opp_val = getattr(item, "ClassCS", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassCS"):
                    opp_val = getattr(item, "ClassCS", None)
                    
                    setattr(item, "ClassCS", self)
                    

class ConstraintCS:

    pass
class PackageCS:

    pass
class mutatorenvironment_miniOCL_RootCS:

    pass
class mutatorenvironment_EStructuralFeature:

    pass
class RandomNumberType:

    pass
class mutatorenvironment_RandomIntegerNumberType(RandomNumberType):

    def __init__(self, min: int):
        self.min = min
        
    @property
    def min(self) -> int:
        return self.__min

    @min.setter
    def min(self, min: int):
        self.__min = min

class mutatorenvironment_RandomDoubleNumberType(RandomNumberType):

    def __init__(self, min: float):
        self.min = min
        
    @property
    def min(self) -> float:
        return self.__min

    @min.setter
    def min(self, min: float):
        self.__min = min

class mutatorenvironment_EObject:

    pass
class InvariantCS:

    pass
class ReferenceSet:

    pass
class mutatorenvironment_ReferenceSwap(ReferenceSet):

    pass
class mutatorenvironment_ReferenceAtt(ReferenceSet):

    pass
class mutatorenvironment_ReferenceRemove(ReferenceSet):

    pass
class mutatorenvironment_ReferenceAdd(ReferenceSet):

    pass
class mutatorenvironment_ReferenceInit(ReferenceSet):

    pass
class mutatorenvironment_BinaryOperator:

    def __init__(self, type: str, mutatorenvironment_BinaryOperator: "mutatorenvironment_Expression" = None):
        self.type = type
        self.mutatorenvironment_BinaryOperator = mutatorenvironment_BinaryOperator
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def mutatorenvironment_BinaryOperator(self):
        return self.__mutatorenvironment_BinaryOperator

    @mutatorenvironment_BinaryOperator.setter
    def mutatorenvironment_BinaryOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_BinaryOperator__mutatorenvironment_BinaryOperator", None)
        self.__mutatorenvironment_BinaryOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_Expression133"):
                opp_val = getattr(old_value, "mutatorenvironment_Expression133", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_Expression133"):
                opp_val = getattr(value, "mutatorenvironment_Expression133", None)
                if opp_val is None:
                    setattr(value, "mutatorenvironment_Expression133", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mutatorenvironment_Evaluation(ABC):

    pass
class mutatorenvironment_AttributeEvaluationType(ABC):

    pass
class Evaluation:

    pass
class mutatorenvironment_ReferenceEvaluation(Evaluation):

    def __init__(self, operator: str, container: bool, mutatorenvironment_ReferenceEvaluation: "mutatorenvironment_EReference" = None, mutatorenvironment_ReferenceEvaluation113: "mutatorenvironment_EReference" = None, mutatorenvironment_ReferenceEvaluation116: "mutatorenvironment_EReference" = None, mutatorenvironment_ReferenceEvaluation119: "mutatorenvironment_ObSelectionStrategy" = None, mutatorenvironment_ReferenceEvaluation122: "mutatorenvironment_EReference" = None, mutatorenvironment_ReferenceEvaluation125: "mutatorenvironment_EAttribute" = None, mutatorenvironment_ReferenceEvaluation128: "mutatorenvironment_AttributeEvaluationType" = None):
        self.operator = operator
        self.container = container
        self.mutatorenvironment_ReferenceEvaluation = mutatorenvironment_ReferenceEvaluation
        self.mutatorenvironment_ReferenceEvaluation113 = mutatorenvironment_ReferenceEvaluation113
        self.mutatorenvironment_ReferenceEvaluation116 = mutatorenvironment_ReferenceEvaluation116
        self.mutatorenvironment_ReferenceEvaluation119 = mutatorenvironment_ReferenceEvaluation119
        self.mutatorenvironment_ReferenceEvaluation122 = mutatorenvironment_ReferenceEvaluation122
        self.mutatorenvironment_ReferenceEvaluation125 = mutatorenvironment_ReferenceEvaluation125
        self.mutatorenvironment_ReferenceEvaluation128 = mutatorenvironment_ReferenceEvaluation128
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def container(self) -> bool:
        return self.__container

    @container.setter
    def container(self, container: bool):
        self.__container = container

    @property
    def mutatorenvironment_ReferenceEvaluation116(self):
        return self.__mutatorenvironment_ReferenceEvaluation116

    @mutatorenvironment_ReferenceEvaluation116.setter
    def mutatorenvironment_ReferenceEvaluation116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ReferenceEvaluation__mutatorenvironment_ReferenceEvaluation116", None)
        self.__mutatorenvironment_ReferenceEvaluation116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_EReference117"):
                opp_val = getattr(old_value, "mutatorenvironment_EReference117", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_EReference117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_EReference117"):
                opp_val = getattr(value, "mutatorenvironment_EReference117", None)
                setattr(value, "mutatorenvironment_EReference117", self)

    @property
    def mutatorenvironment_ReferenceEvaluation113(self):
        return self.__mutatorenvironment_ReferenceEvaluation113

    @mutatorenvironment_ReferenceEvaluation113.setter
    def mutatorenvironment_ReferenceEvaluation113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ReferenceEvaluation__mutatorenvironment_ReferenceEvaluation113", None)
        self.__mutatorenvironment_ReferenceEvaluation113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_EReference114"):
                opp_val = getattr(old_value, "mutatorenvironment_EReference114", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_EReference114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_EReference114"):
                opp_val = getattr(value, "mutatorenvironment_EReference114", None)
                setattr(value, "mutatorenvironment_EReference114", self)

    @property
    def mutatorenvironment_ReferenceEvaluation128(self):
        return self.__mutatorenvironment_ReferenceEvaluation128

    @mutatorenvironment_ReferenceEvaluation128.setter
    def mutatorenvironment_ReferenceEvaluation128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ReferenceEvaluation__mutatorenvironment_ReferenceEvaluation128", None)
        self.__mutatorenvironment_ReferenceEvaluation128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_AttributeEvaluationType129"):
                opp_val = getattr(old_value, "mutatorenvironment_AttributeEvaluationType129", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_AttributeEvaluationType129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_AttributeEvaluationType129"):
                opp_val = getattr(value, "mutatorenvironment_AttributeEvaluationType129", None)
                setattr(value, "mutatorenvironment_AttributeEvaluationType129", self)

    @property
    def mutatorenvironment_ReferenceEvaluation122(self):
        return self.__mutatorenvironment_ReferenceEvaluation122

    @mutatorenvironment_ReferenceEvaluation122.setter
    def mutatorenvironment_ReferenceEvaluation122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ReferenceEvaluation__mutatorenvironment_ReferenceEvaluation122", None)
        self.__mutatorenvironment_ReferenceEvaluation122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_EReference123"):
                opp_val = getattr(old_value, "mutatorenvironment_EReference123", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_EReference123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_EReference123"):
                opp_val = getattr(value, "mutatorenvironment_EReference123", None)
                setattr(value, "mutatorenvironment_EReference123", self)

    @property
    def mutatorenvironment_ReferenceEvaluation125(self):
        return self.__mutatorenvironment_ReferenceEvaluation125

    @mutatorenvironment_ReferenceEvaluation125.setter
    def mutatorenvironment_ReferenceEvaluation125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ReferenceEvaluation__mutatorenvironment_ReferenceEvaluation125", None)
        self.__mutatorenvironment_ReferenceEvaluation125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_EAttribute126"):
                opp_val = getattr(old_value, "mutatorenvironment_EAttribute126", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_EAttribute126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_EAttribute126"):
                opp_val = getattr(value, "mutatorenvironment_EAttribute126", None)
                setattr(value, "mutatorenvironment_EAttribute126", self)

    @property
    def mutatorenvironment_ReferenceEvaluation119(self):
        return self.__mutatorenvironment_ReferenceEvaluation119

    @mutatorenvironment_ReferenceEvaluation119.setter
    def mutatorenvironment_ReferenceEvaluation119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ReferenceEvaluation__mutatorenvironment_ReferenceEvaluation119", None)
        self.__mutatorenvironment_ReferenceEvaluation119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_ObSelectionStrategy120"):
                opp_val = getattr(old_value, "mutatorenvironment_ObSelectionStrategy120", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_ObSelectionStrategy120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_ObSelectionStrategy120"):
                opp_val = getattr(value, "mutatorenvironment_ObSelectionStrategy120", None)
                setattr(value, "mutatorenvironment_ObSelectionStrategy120", self)

    @property
    def mutatorenvironment_ReferenceEvaluation(self):
        return self.__mutatorenvironment_ReferenceEvaluation

    @mutatorenvironment_ReferenceEvaluation.setter
    def mutatorenvironment_ReferenceEvaluation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ReferenceEvaluation__mutatorenvironment_ReferenceEvaluation", None)
        self.__mutatorenvironment_ReferenceEvaluation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_EReference111"):
                opp_val = getattr(old_value, "mutatorenvironment_EReference111", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_EReference111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_EReference111"):
                opp_val = getattr(value, "mutatorenvironment_EReference111", None)
                setattr(value, "mutatorenvironment_EReference111", self)

class mutatorenvironment_AttributeEvaluation(Evaluation):

    pass
class OtherSelection:

    pass
class mutatorenvironment_OtherTypeSelection(OtherSelection):

    pass
class CompleteSelection:

    pass
class mutatorenvironment_CompleteTypeSelection(CompleteSelection):

    pass
class RemoveReferenceMutator:

    pass
class mutatorenvironment_RemoveSpecificReferenceMutator(RemoveReferenceMutator):

    pass
class mutatorenvironment_RemoveCompleteReferenceMutator(RemoveReferenceMutator):

    pass
class mutatorenvironment_RemoveRandomReferenceMutator(RemoveReferenceMutator):

    pass
class mutatorenvironment_EAttribute:

    pass
class DoubleType:

    pass
class mutatorenvironment_RandomDoubleType(DoubleType):

    def __init__(self, max: float, allowsNull: bool, min: float):
        self.max = max
        self.allowsNull = allowsNull
        self.min = min
        
    @property
    def allowsNull(self) -> bool:
        return self.__allowsNull

    @allowsNull.setter
    def allowsNull(self, allowsNull: bool):
        self.__allowsNull = allowsNull

    @property
    def max(self) -> float:
        return self.__max

    @max.setter
    def max(self, max: float):
        self.__max = max

    @property
    def min(self) -> float:
        return self.__min

    @min.setter
    def min(self, min: float):
        self.__min = min

class mutatorenvironment_SpecificDoubleType(DoubleType):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class RandomSelection:

    pass
class mutatorenvironment_RandomTypeSelection(RandomSelection):

    pass
class ObSelectionStrategy:

    pass
class mutatorenvironment_OtherSelection(ObSelectionStrategy):

    pass
class mutatorenvironment_TypedSelection(ObSelectionStrategy):

    pass
class mutatorenvironment_SpecificSelection(ObSelectionStrategy):

    pass
class mutatorenvironment_CompleteSelection(ObSelectionStrategy):

    pass
class mutatorenvironment_RandomSelection(ObSelectionStrategy):

    pass
class IntegerType:

    pass
class mutatorenvironment_RandomIntegerType(IntegerType):

    def __init__(self, min: int, max: int, allowsNull: bool):
        self.min = min
        self.max = max
        self.allowsNull = allowsNull
        
    @property
    def min(self) -> int:
        return self.__min

    @min.setter
    def min(self, min: int):
        self.__min = min

    @property
    def allowsNull(self) -> bool:
        return self.__allowsNull

    @allowsNull.setter
    def allowsNull(self, allowsNull: bool):
        self.__allowsNull = allowsNull

    @property
    def max(self) -> int:
        return self.__max

    @max.setter
    def max(self, max: int):
        self.__max = max

class mutatorenvironment_SpecificIntegerType(IntegerType):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class NumberType:

    pass
class mutatorenvironment_DoubleType(NumberType):

    pass
class mutatorenvironment_MinValueType(NumberType):

    pass
class mutatorenvironment_RandomNumberType(NumberType):

    pass
class mutatorenvironment_MaxValueType(NumberType):

    pass
class mutatorenvironment_IntegerType(NumberType):

    pass
class StringType:

    pass
class mutatorenvironment_ReplaceStringType(StringType):

    def __init__(self, newstring: str, oldstring: str):
        self.newstring = newstring
        self.oldstring = oldstring
        
    @property
    def newstring(self) -> str:
        return self.__newstring

    @newstring.setter
    def newstring(self, newstring: str):
        self.__newstring = newstring

    @property
    def oldstring(self) -> str:
        return self.__oldstring

    @oldstring.setter
    def oldstring(self, oldstring: str):
        self.__oldstring = oldstring

class mutatorenvironment_RandomStringType(StringType):

    def __init__(self, min: int, max: int, allowsNull: bool):
        self.min = min
        self.max = max
        self.allowsNull = allowsNull
        
    @property
    def max(self) -> int:
        return self.__max

    @max.setter
    def max(self, max: int):
        self.__max = max

    @property
    def allowsNull(self) -> bool:
        return self.__allowsNull

    @allowsNull.setter
    def allowsNull(self, allowsNull: bool):
        self.__allowsNull = allowsNull

    @property
    def min(self) -> int:
        return self.__min

    @min.setter
    def min(self, min: int):
        self.__min = min

class mutatorenvironment_LowerStringType(StringType):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class mutatorenvironment_CatStartStringType(StringType):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class mutatorenvironment_CatEndStringType(StringType):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class mutatorenvironment_RandomStringNumberType(StringType):

    def __init__(self, min: int, max: int, allowsNull: bool):
        self.min = min
        self.max = max
        self.allowsNull = allowsNull
        
    @property
    def allowsNull(self) -> bool:
        return self.__allowsNull

    @allowsNull.setter
    def allowsNull(self, allowsNull: bool):
        self.__allowsNull = allowsNull

    @property
    def min(self) -> int:
        return self.__min

    @min.setter
    def min(self, min: int):
        self.__min = min

    @property
    def max(self) -> int:
        return self.__max

    @max.setter
    def max(self, max: int):
        self.__max = max

class mutatorenvironment_UpperStringType(StringType):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class mutatorenvironment_SpecificStringType(StringType):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class BooleanType:

    pass
class mutatorenvironment_RandomBooleanType(BooleanType):

    def __init__(self, allowsNull: bool):
        self.allowsNull = allowsNull
        
    @property
    def allowsNull(self) -> bool:
        return self.__allowsNull

    @allowsNull.setter
    def allowsNull(self, allowsNull: bool):
        self.__allowsNull = allowsNull

class mutatorenvironment_SpecificBooleanType(BooleanType):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class AttributeType:

    pass
class mutatorenvironment_ListStringType(AttributeType):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class mutatorenvironment_RandomType(AttributeType):

    pass
class mutatorenvironment_ListType(AttributeType):

    pass
class mutatorenvironment_StringType(AttributeType):

    pass
class mutatorenvironment_NumberType(AttributeType):

    pass
class mutatorenvironment_BooleanType(AttributeType):

    pass
class AttributeEvaluationType:

    pass
class mutatorenvironment_ObjectAttributeType(AttributeEvaluationType):

    def __init__(self, operator: str, mutatorenvironment_ObjectAttributeType: "mutatorenvironment_ObjectEmitter" = None, mutatorenvironment_ObjectAttributeType166: "mutatorenvironment_EAttribute" = None):
        self.operator = operator
        self.mutatorenvironment_ObjectAttributeType = mutatorenvironment_ObjectAttributeType
        self.mutatorenvironment_ObjectAttributeType166 = mutatorenvironment_ObjectAttributeType166
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def mutatorenvironment_ObjectAttributeType166(self):
        return self.__mutatorenvironment_ObjectAttributeType166

    @mutatorenvironment_ObjectAttributeType166.setter
    def mutatorenvironment_ObjectAttributeType166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObjectAttributeType__mutatorenvironment_ObjectAttributeType166", None)
        self.__mutatorenvironment_ObjectAttributeType166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_EAttribute167"):
                opp_val = getattr(old_value, "mutatorenvironment_EAttribute167", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_EAttribute167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_EAttribute167"):
                opp_val = getattr(value, "mutatorenvironment_EAttribute167", None)
                setattr(value, "mutatorenvironment_EAttribute167", self)

    @property
    def mutatorenvironment_ObjectAttributeType(self):
        return self.__mutatorenvironment_ObjectAttributeType

    @mutatorenvironment_ObjectAttributeType.setter
    def mutatorenvironment_ObjectAttributeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObjectAttributeType__mutatorenvironment_ObjectAttributeType", None)
        self.__mutatorenvironment_ObjectAttributeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_ObjectEmitter164"):
                opp_val = getattr(old_value, "mutatorenvironment_ObjectEmitter164", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_ObjectEmitter164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_ObjectEmitter164"):
                opp_val = getattr(value, "mutatorenvironment_ObjectEmitter164", None)
                setattr(value, "mutatorenvironment_ObjectEmitter164", self)

class mutatorenvironment_AttributeType(AttributeEvaluationType):

    def __init__(self, operator: str, mutatorenvironment_AttributeType: "mutatorenvironment_AttributeScalar" = None, mutatorenvironment_AttributeType109: "mutatorenvironment_ReferenceAtt" = None):
        self.operator = operator
        self.mutatorenvironment_AttributeType = mutatorenvironment_AttributeType
        self.mutatorenvironment_AttributeType109 = mutatorenvironment_AttributeType109
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def mutatorenvironment_AttributeType109(self):
        return self.__mutatorenvironment_AttributeType109

    @mutatorenvironment_AttributeType109.setter
    def mutatorenvironment_AttributeType109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_AttributeType__mutatorenvironment_AttributeType109", None)
        self.__mutatorenvironment_AttributeType109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_ReferenceAtt108"):
                opp_val = getattr(old_value, "mutatorenvironment_ReferenceAtt108", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_ReferenceAtt108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_ReferenceAtt108"):
                opp_val = getattr(value, "mutatorenvironment_ReferenceAtt108", None)
                setattr(value, "mutatorenvironment_ReferenceAtt108", self)

    @property
    def mutatorenvironment_AttributeType(self):
        return self.__mutatorenvironment_AttributeType

    @mutatorenvironment_AttributeType.setter
    def mutatorenvironment_AttributeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_AttributeType__mutatorenvironment_AttributeType", None)
        self.__mutatorenvironment_AttributeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_AttributeScalar"):
                opp_val = getattr(old_value, "mutatorenvironment_AttributeScalar", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_AttributeScalar", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_AttributeScalar"):
                opp_val = getattr(value, "mutatorenvironment_AttributeScalar", None)
                setattr(value, "mutatorenvironment_AttributeScalar", self)

class AttributeSet:

    pass
class mutatorenvironment_AttributeReverse(AttributeSet):

    pass
class mutatorenvironment_AttributeSwap(AttributeSet):

    pass
class mutatorenvironment_AttributeOperation(AttributeSet):

    def __init__(self, operator: str, mutatorenvironment_AttributeOperation: "mutatorenvironment_AttributeEvaluationType" = None):
        self.operator = operator
        self.mutatorenvironment_AttributeOperation = mutatorenvironment_AttributeOperation
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def mutatorenvironment_AttributeOperation(self):
        return self.__mutatorenvironment_AttributeOperation

    @mutatorenvironment_AttributeOperation.setter
    def mutatorenvironment_AttributeOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_AttributeOperation__mutatorenvironment_AttributeOperation", None)
        self.__mutatorenvironment_AttributeOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_AttributeEvaluationType173"):
                opp_val = getattr(old_value, "mutatorenvironment_AttributeEvaluationType173", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_AttributeEvaluationType173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_AttributeEvaluationType173"):
                opp_val = getattr(value, "mutatorenvironment_AttributeEvaluationType173", None)
                setattr(value, "mutatorenvironment_AttributeEvaluationType173", self)

class mutatorenvironment_AttributeUnset(AttributeSet):

    pass
class mutatorenvironment_AttributeCopy(AttributeSet):

    pass
class mutatorenvironment_AttributeScalar(AttributeSet):

    pass
class SpecificSelection:

    pass
class mutatorenvironment_SpecificClosureSelection(SpecificSelection):

    pass
class mutatorenvironment_SpecificReferenceSelection(SpecificSelection):

    pass
class mutatorenvironment_SpecificObjectSelection(SpecificSelection):

    pass
class mutatorenvironment_Source:

    def __init__(self, path: str, mutatorenvironment_Source: "mutatorenvironment_Program" = None, mutatorenvironment_Source201: "mutatorenvironment_Resource" = None):
        self.path = path
        self.mutatorenvironment_Source = mutatorenvironment_Source
        self.mutatorenvironment_Source201 = mutatorenvironment_Source201
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def mutatorenvironment_Source(self):
        return self.__mutatorenvironment_Source

    @mutatorenvironment_Source.setter
    def mutatorenvironment_Source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_Source__mutatorenvironment_Source", None)
        self.__mutatorenvironment_Source = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_Program"):
                opp_val = getattr(old_value, "mutatorenvironment_Program", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_Program", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_Program"):
                opp_val = getattr(value, "mutatorenvironment_Program", None)
                setattr(value, "mutatorenvironment_Program", self)

    @property
    def mutatorenvironment_Source201(self):
        return self.__mutatorenvironment_Source201

    @mutatorenvironment_Source201.setter
    def mutatorenvironment_Source201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_Source__mutatorenvironment_Source201", None)
        self.__mutatorenvironment_Source201 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_Resource200"):
                opp_val = getattr(old_value, "mutatorenvironment_Resource200", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_Resource200", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_Resource200"):
                opp_val = getattr(value, "mutatorenvironment_Resource200", None)
                setattr(value, "mutatorenvironment_Resource200", self)

class mutatorenvironment_Expression:

    pass
class mutatorenvironment_EReference:

    pass
class mutatorenvironment_ReferenceSet:

    pass
class mutatorenvironment_AttributeSet:

    pass
class Mutator:

    pass
class mutatorenvironment_SelectObjectMutator(Mutator):

    pass
class mutatorenvironment_CreateReferenceMutator(Mutator):

    pass
class mutatorenvironment_ModifyTargetReferenceMutator(Mutator):

    pass
class mutatorenvironment_RemoveObjectMutator(Mutator):

    pass
class mutatorenvironment_SelectSampleMutator(Mutator):

    def __init__(self, clause: str, mutatorenvironment_SelectSampleMutator: "mutatorenvironment_ObSelectionStrategy" = None, mutatorenvironment_SelectSampleMutator184: set["mutatorenvironment_EStructuralFeature"] = None):
        self.clause = clause
        self.mutatorenvironment_SelectSampleMutator = mutatorenvironment_SelectSampleMutator
        self.mutatorenvironment_SelectSampleMutator184 = mutatorenvironment_SelectSampleMutator184 if mutatorenvironment_SelectSampleMutator184 is not None else set()
        
    @property
    def clause(self) -> str:
        return self.__clause

    @clause.setter
    def clause(self, clause: str):
        self.__clause = clause

    @property
    def mutatorenvironment_SelectSampleMutator184(self):
        return self.__mutatorenvironment_SelectSampleMutator184

    @mutatorenvironment_SelectSampleMutator184.setter
    def mutatorenvironment_SelectSampleMutator184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_SelectSampleMutator__mutatorenvironment_SelectSampleMutator184", None)
        self.__mutatorenvironment_SelectSampleMutator184 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mutatorenvironment_EStructuralFeature"):
                    opp_val = getattr(item, "mutatorenvironment_EStructuralFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "mutatorenvironment_EStructuralFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mutatorenvironment_EStructuralFeature"):
                    opp_val = getattr(item, "mutatorenvironment_EStructuralFeature", None)
                    
                    setattr(item, "mutatorenvironment_EStructuralFeature", self)
                    

    @property
    def mutatorenvironment_SelectSampleMutator(self):
        return self.__mutatorenvironment_SelectSampleMutator

    @mutatorenvironment_SelectSampleMutator.setter
    def mutatorenvironment_SelectSampleMutator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_SelectSampleMutator__mutatorenvironment_SelectSampleMutator", None)
        self.__mutatorenvironment_SelectSampleMutator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_ObSelectionStrategy182"):
                opp_val = getattr(old_value, "mutatorenvironment_ObSelectionStrategy182", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_ObSelectionStrategy182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_ObSelectionStrategy182"):
                opp_val = getattr(value, "mutatorenvironment_ObSelectionStrategy182", None)
                setattr(value, "mutatorenvironment_ObSelectionStrategy182", self)

class mutatorenvironment_ModifyInformationMutator(Mutator):

    pass
class mutatorenvironment_CloneObjectMutator(Mutator):

    def __init__(self, contents: bool, mutatorenvironment_CloneObjectMutator151: "mutatorenvironment_ObSelectionStrategy" = None, mutatorenvironment_CloneObjectMutator154: "mutatorenvironment_EReference" = None, mutatorenvironment_CloneObjectMutator157: set["mutatorenvironment_AttributeSet"] = None, mutatorenvironment_CloneObjectMutator160: set["mutatorenvironment_ReferenceSet"] = None, mutatorenvironment_CloneObjectMutator: "mutatorenvironment_ObSelectionStrategy" = None):
        self.contents = contents
        self.mutatorenvironment_CloneObjectMutator151 = mutatorenvironment_CloneObjectMutator151
        self.mutatorenvironment_CloneObjectMutator154 = mutatorenvironment_CloneObjectMutator154
        self.mutatorenvironment_CloneObjectMutator157 = mutatorenvironment_CloneObjectMutator157 if mutatorenvironment_CloneObjectMutator157 is not None else set()
        self.mutatorenvironment_CloneObjectMutator160 = mutatorenvironment_CloneObjectMutator160 if mutatorenvironment_CloneObjectMutator160 is not None else set()
        self.mutatorenvironment_CloneObjectMutator = mutatorenvironment_CloneObjectMutator
        
    @property
    def contents(self) -> bool:
        return self.__contents

    @contents.setter
    def contents(self, contents: bool):
        self.__contents = contents

    @property
    def mutatorenvironment_CloneObjectMutator154(self):
        return self.__mutatorenvironment_CloneObjectMutator154

    @mutatorenvironment_CloneObjectMutator154.setter
    def mutatorenvironment_CloneObjectMutator154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_CloneObjectMutator__mutatorenvironment_CloneObjectMutator154", None)
        self.__mutatorenvironment_CloneObjectMutator154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_EReference155"):
                opp_val = getattr(old_value, "mutatorenvironment_EReference155", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_EReference155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_EReference155"):
                opp_val = getattr(value, "mutatorenvironment_EReference155", None)
                setattr(value, "mutatorenvironment_EReference155", self)

    @property
    def mutatorenvironment_CloneObjectMutator(self):
        return self.__mutatorenvironment_CloneObjectMutator

    @mutatorenvironment_CloneObjectMutator.setter
    def mutatorenvironment_CloneObjectMutator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_CloneObjectMutator__mutatorenvironment_CloneObjectMutator", None)
        self.__mutatorenvironment_CloneObjectMutator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_ObSelectionStrategy149"):
                opp_val = getattr(old_value, "mutatorenvironment_ObSelectionStrategy149", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_ObSelectionStrategy149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_ObSelectionStrategy149"):
                opp_val = getattr(value, "mutatorenvironment_ObSelectionStrategy149", None)
                setattr(value, "mutatorenvironment_ObSelectionStrategy149", self)

    @property
    def mutatorenvironment_CloneObjectMutator160(self):
        return self.__mutatorenvironment_CloneObjectMutator160

    @mutatorenvironment_CloneObjectMutator160.setter
    def mutatorenvironment_CloneObjectMutator160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_CloneObjectMutator__mutatorenvironment_CloneObjectMutator160", None)
        self.__mutatorenvironment_CloneObjectMutator160 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mutatorenvironment_ReferenceSet161"):
                    opp_val = getattr(item, "mutatorenvironment_ReferenceSet161", None)
                    
                    if opp_val == self:
                        setattr(item, "mutatorenvironment_ReferenceSet161", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mutatorenvironment_ReferenceSet161"):
                    opp_val = getattr(item, "mutatorenvironment_ReferenceSet161", None)
                    
                    setattr(item, "mutatorenvironment_ReferenceSet161", self)
                    

    @property
    def mutatorenvironment_CloneObjectMutator157(self):
        return self.__mutatorenvironment_CloneObjectMutator157

    @mutatorenvironment_CloneObjectMutator157.setter
    def mutatorenvironment_CloneObjectMutator157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_CloneObjectMutator__mutatorenvironment_CloneObjectMutator157", None)
        self.__mutatorenvironment_CloneObjectMutator157 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mutatorenvironment_AttributeSet158"):
                    opp_val = getattr(item, "mutatorenvironment_AttributeSet158", None)
                    
                    if opp_val == self:
                        setattr(item, "mutatorenvironment_AttributeSet158", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mutatorenvironment_AttributeSet158"):
                    opp_val = getattr(item, "mutatorenvironment_AttributeSet158", None)
                    
                    setattr(item, "mutatorenvironment_AttributeSet158", self)
                    

    @property
    def mutatorenvironment_CloneObjectMutator151(self):
        return self.__mutatorenvironment_CloneObjectMutator151

    @mutatorenvironment_CloneObjectMutator151.setter
    def mutatorenvironment_CloneObjectMutator151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_CloneObjectMutator__mutatorenvironment_CloneObjectMutator151", None)
        self.__mutatorenvironment_CloneObjectMutator151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_ObSelectionStrategy152"):
                opp_val = getattr(old_value, "mutatorenvironment_ObSelectionStrategy152", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_ObSelectionStrategy152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_ObSelectionStrategy152"):
                opp_val = getattr(value, "mutatorenvironment_ObSelectionStrategy152", None)
                setattr(value, "mutatorenvironment_ObSelectionStrategy152", self)

class mutatorenvironment_ModifySourceReferenceMutator(Mutator):

    pass
class mutatorenvironment_RetypeObjectMutator(Mutator):

    pass
class mutatorenvironment_RemoveReferenceMutator(Mutator):

    pass
class mutatorenvironment_CreateObjectMutator(Mutator):

    pass
class mutatorenvironment_CompositeMutator(Mutator):

    pass
class ObjectEmitter:

    pass
class mutatorenvironment_ObSelectionStrategy(ObjectEmitter):

    def __init__(self, resource: str, mutatorenvironment_ObSelectionStrategy: "mutatorenvironment_CreateObjectMutator" = None, mutatorenvironment_ObSelectionStrategy24: "mutatorenvironment_EReference" = None, mutatorenvironment_ObSelectionStrategy26: "mutatorenvironment_Expression" = None, mutatorenvironment_ObSelectionStrategy28: "mutatorenvironment_EReference" = None, mutatorenvironment_ObSelectionStrategy31: "mutatorenvironment_EReference" = None, mutatorenvironment_ObSelectionStrategy40: "mutatorenvironment_ModifySourceReferenceMutator" = None, mutatorenvironment_ObSelectionStrategy43: "mutatorenvironment_ModifySourceReferenceMutator" = None, mutatorenvironment_ObSelectionStrategy50: "mutatorenvironment_ModifyTargetReferenceMutator" = None, mutatorenvironment_ObSelectionStrategy53: "mutatorenvironment_ModifyTargetReferenceMutator" = None, mutatorenvironment_ObSelectionStrategy55: "mutatorenvironment_CreateReferenceMutator" = None, mutatorenvironment_ObSelectionStrategy58: "mutatorenvironment_CreateReferenceMutator" = None, mutatorenvironment_ObSelectionStrategy63: "mutatorenvironment_RemoveObjectMutator" = None, mutatorenvironment_ObSelectionStrategy68: "mutatorenvironment_ModifyInformationMutator" = None, mutatorenvironment_ObSelectionStrategy78: "mutatorenvironment_AttributeSwap" = None, mutatorenvironment_ObSelectionStrategy66: "mutatorenvironment_RemoveObjectMutator" = None, mutatorenvironment_ObSelectionStrategy80: "mutatorenvironment_AttributeCopy" = None, mutatorenvironment_ObSelectionStrategy87: "mutatorenvironment_RemoveSpecificReferenceMutator" = None, mutatorenvironment_ObSelectionStrategy91: "mutatorenvironment_SelectObjectMutator" = None, mutatorenvironment_ObSelectionStrategy94: "mutatorenvironment_SelectObjectMutator" = None, mutatorenvironment_ObSelectionStrategy104: "mutatorenvironment_ReferenceSet" = None, mutatorenvironment_ObSelectionStrategy120: "mutatorenvironment_ReferenceEvaluation" = None, mutatorenvironment_ObSelectionStrategy152: "mutatorenvironment_CloneObjectMutator" = None, mutatorenvironment_ObSelectionStrategy149: "mutatorenvironment_CloneObjectMutator" = None, mutatorenvironment_ObSelectionStrategy175: "mutatorenvironment_RandomNumberType" = None, mutatorenvironment_ObSelectionStrategy182: "mutatorenvironment_SelectSampleMutator" = None, mutatorenvironment_ObSelectionStrategy186: "mutatorenvironment_RetypeObjectMutator" = None, mutatorenvironment_ObSelectionStrategy189: "mutatorenvironment_RetypeObjectMutator" = None):
        self.resource = resource
        self.mutatorenvironment_ObSelectionStrategy = mutatorenvironment_ObSelectionStrategy
        self.mutatorenvironment_ObSelectionStrategy24 = mutatorenvironment_ObSelectionStrategy24
        self.mutatorenvironment_ObSelectionStrategy26 = mutatorenvironment_ObSelectionStrategy26
        self.mutatorenvironment_ObSelectionStrategy28 = mutatorenvironment_ObSelectionStrategy28
        self.mutatorenvironment_ObSelectionStrategy31 = mutatorenvironment_ObSelectionStrategy31
        self.mutatorenvironment_ObSelectionStrategy40 = mutatorenvironment_ObSelectionStrategy40
        self.mutatorenvironment_ObSelectionStrategy43 = mutatorenvironment_ObSelectionStrategy43
        self.mutatorenvironment_ObSelectionStrategy50 = mutatorenvironment_ObSelectionStrategy50
        self.mutatorenvironment_ObSelectionStrategy53 = mutatorenvironment_ObSelectionStrategy53
        self.mutatorenvironment_ObSelectionStrategy55 = mutatorenvironment_ObSelectionStrategy55
        self.mutatorenvironment_ObSelectionStrategy58 = mutatorenvironment_ObSelectionStrategy58
        self.mutatorenvironment_ObSelectionStrategy63 = mutatorenvironment_ObSelectionStrategy63
        self.mutatorenvironment_ObSelectionStrategy68 = mutatorenvironment_ObSelectionStrategy68
        self.mutatorenvironment_ObSelectionStrategy78 = mutatorenvironment_ObSelectionStrategy78
        self.mutatorenvironment_ObSelectionStrategy66 = mutatorenvironment_ObSelectionStrategy66
        self.mutatorenvironment_ObSelectionStrategy80 = mutatorenvironment_ObSelectionStrategy80
        self.mutatorenvironment_ObSelectionStrategy87 = mutatorenvironment_ObSelectionStrategy87
        self.mutatorenvironment_ObSelectionStrategy91 = mutatorenvironment_ObSelectionStrategy91
        self.mutatorenvironment_ObSelectionStrategy94 = mutatorenvironment_ObSelectionStrategy94
        self.mutatorenvironment_ObSelectionStrategy104 = mutatorenvironment_ObSelectionStrategy104
        self.mutatorenvironment_ObSelectionStrategy120 = mutatorenvironment_ObSelectionStrategy120
        self.mutatorenvironment_ObSelectionStrategy152 = mutatorenvironment_ObSelectionStrategy152
        self.mutatorenvironment_ObSelectionStrategy149 = mutatorenvironment_ObSelectionStrategy149
        self.mutatorenvironment_ObSelectionStrategy175 = mutatorenvironment_ObSelectionStrategy175
        self.mutatorenvironment_ObSelectionStrategy182 = mutatorenvironment_ObSelectionStrategy182
        self.mutatorenvironment_ObSelectionStrategy186 = mutatorenvironment_ObSelectionStrategy186
        self.mutatorenvironment_ObSelectionStrategy189 = mutatorenvironment_ObSelectionStrategy189
        
    @property
    def resource(self) -> str:
        return self.__resource

    @resource.setter
    def resource(self, resource: str):
        self.__resource = resource

    @property
    def mutatorenvironment_ObSelectionStrategy24(self):
        return self.__mutatorenvironment_ObSelectionStrategy24

    @mutatorenvironment_ObSelectionStrategy24.setter
    def mutatorenvironment_ObSelectionStrategy24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObSelectionStrategy__mutatorenvironment_ObSelectionStrategy24", None)
        self.__mutatorenvironment_ObSelectionStrategy24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_EReference"):
                opp_val = getattr(old_value, "mutatorenvironment_EReference", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_EReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_EReference"):
                opp_val = getattr(value, "mutatorenvironment_EReference", None)
                setattr(value, "mutatorenvironment_EReference", self)

    @property
    def mutatorenvironment_ObSelectionStrategy149(self):
        return self.__mutatorenvironment_ObSelectionStrategy149

    @mutatorenvironment_ObSelectionStrategy149.setter
    def mutatorenvironment_ObSelectionStrategy149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObSelectionStrategy__mutatorenvironment_ObSelectionStrategy149", None)
        self.__mutatorenvironment_ObSelectionStrategy149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_CloneObjectMutator"):
                opp_val = getattr(old_value, "mutatorenvironment_CloneObjectMutator", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_CloneObjectMutator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_CloneObjectMutator"):
                opp_val = getattr(value, "mutatorenvironment_CloneObjectMutator", None)
                setattr(value, "mutatorenvironment_CloneObjectMutator", self)

    @property
    def mutatorenvironment_ObSelectionStrategy63(self):
        return self.__mutatorenvironment_ObSelectionStrategy63

    @mutatorenvironment_ObSelectionStrategy63.setter
    def mutatorenvironment_ObSelectionStrategy63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObSelectionStrategy__mutatorenvironment_ObSelectionStrategy63", None)
        self.__mutatorenvironment_ObSelectionStrategy63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_RemoveObjectMutator"):
                opp_val = getattr(old_value, "mutatorenvironment_RemoveObjectMutator", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_RemoveObjectMutator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_RemoveObjectMutator"):
                opp_val = getattr(value, "mutatorenvironment_RemoveObjectMutator", None)
                setattr(value, "mutatorenvironment_RemoveObjectMutator", self)

    @property
    def mutatorenvironment_ObSelectionStrategy80(self):
        return self.__mutatorenvironment_ObSelectionStrategy80

    @mutatorenvironment_ObSelectionStrategy80.setter
    def mutatorenvironment_ObSelectionStrategy80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObSelectionStrategy__mutatorenvironment_ObSelectionStrategy80", None)
        self.__mutatorenvironment_ObSelectionStrategy80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_AttributeCopy"):
                opp_val = getattr(old_value, "mutatorenvironment_AttributeCopy", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_AttributeCopy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_AttributeCopy"):
                opp_val = getattr(value, "mutatorenvironment_AttributeCopy", None)
                setattr(value, "mutatorenvironment_AttributeCopy", self)

    @property
    def mutatorenvironment_ObSelectionStrategy120(self):
        return self.__mutatorenvironment_ObSelectionStrategy120

    @mutatorenvironment_ObSelectionStrategy120.setter
    def mutatorenvironment_ObSelectionStrategy120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObSelectionStrategy__mutatorenvironment_ObSelectionStrategy120", None)
        self.__mutatorenvironment_ObSelectionStrategy120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_ReferenceEvaluation119"):
                opp_val = getattr(old_value, "mutatorenvironment_ReferenceEvaluation119", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_ReferenceEvaluation119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_ReferenceEvaluation119"):
                opp_val = getattr(value, "mutatorenvironment_ReferenceEvaluation119", None)
                setattr(value, "mutatorenvironment_ReferenceEvaluation119", self)

    @property
    def mutatorenvironment_ObSelectionStrategy186(self):
        return self.__mutatorenvironment_ObSelectionStrategy186

    @mutatorenvironment_ObSelectionStrategy186.setter
    def mutatorenvironment_ObSelectionStrategy186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObSelectionStrategy__mutatorenvironment_ObSelectionStrategy186", None)
        self.__mutatorenvironment_ObSelectionStrategy186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_RetypeObjectMutator"):
                opp_val = getattr(old_value, "mutatorenvironment_RetypeObjectMutator", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_RetypeObjectMutator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_RetypeObjectMutator"):
                opp_val = getattr(value, "mutatorenvironment_RetypeObjectMutator", None)
                setattr(value, "mutatorenvironment_RetypeObjectMutator", self)

    @property
    def mutatorenvironment_ObSelectionStrategy68(self):
        return self.__mutatorenvironment_ObSelectionStrategy68

    @mutatorenvironment_ObSelectionStrategy68.setter
    def mutatorenvironment_ObSelectionStrategy68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObSelectionStrategy__mutatorenvironment_ObSelectionStrategy68", None)
        self.__mutatorenvironment_ObSelectionStrategy68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_ModifyInformationMutator"):
                opp_val = getattr(old_value, "mutatorenvironment_ModifyInformationMutator", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_ModifyInformationMutator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_ModifyInformationMutator"):
                opp_val = getattr(value, "mutatorenvironment_ModifyInformationMutator", None)
                setattr(value, "mutatorenvironment_ModifyInformationMutator", self)

    @property
    def mutatorenvironment_ObSelectionStrategy87(self):
        return self.__mutatorenvironment_ObSelectionStrategy87

    @mutatorenvironment_ObSelectionStrategy87.setter
    def mutatorenvironment_ObSelectionStrategy87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObSelectionStrategy__mutatorenvironment_ObSelectionStrategy87", None)
        self.__mutatorenvironment_ObSelectionStrategy87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_RemoveSpecificReferenceMutator86"):
                opp_val = getattr(old_value, "mutatorenvironment_RemoveSpecificReferenceMutator86", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_RemoveSpecificReferenceMutator86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_RemoveSpecificReferenceMutator86"):
                opp_val = getattr(value, "mutatorenvironment_RemoveSpecificReferenceMutator86", None)
                setattr(value, "mutatorenvironment_RemoveSpecificReferenceMutator86", self)

    @property
    def mutatorenvironment_ObSelectionStrategy78(self):
        return self.__mutatorenvironment_ObSelectionStrategy78

    @mutatorenvironment_ObSelectionStrategy78.setter
    def mutatorenvironment_ObSelectionStrategy78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObSelectionStrategy__mutatorenvironment_ObSelectionStrategy78", None)
        self.__mutatorenvironment_ObSelectionStrategy78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_AttributeSwap"):
                opp_val = getattr(old_value, "mutatorenvironment_AttributeSwap", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_AttributeSwap", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_AttributeSwap"):
                opp_val = getattr(value, "mutatorenvironment_AttributeSwap", None)
                setattr(value, "mutatorenvironment_AttributeSwap", self)

    @property
    def mutatorenvironment_ObSelectionStrategy26(self):
        return self.__mutatorenvironment_ObSelectionStrategy26

    @mutatorenvironment_ObSelectionStrategy26.setter
    def mutatorenvironment_ObSelectionStrategy26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObSelectionStrategy__mutatorenvironment_ObSelectionStrategy26", None)
        self.__mutatorenvironment_ObSelectionStrategy26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_Expression"):
                opp_val = getattr(old_value, "mutatorenvironment_Expression", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_Expression"):
                opp_val = getattr(value, "mutatorenvironment_Expression", None)
                setattr(value, "mutatorenvironment_Expression", self)

    @property
    def mutatorenvironment_ObSelectionStrategy152(self):
        return self.__mutatorenvironment_ObSelectionStrategy152

    @mutatorenvironment_ObSelectionStrategy152.setter
    def mutatorenvironment_ObSelectionStrategy152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObSelectionStrategy__mutatorenvironment_ObSelectionStrategy152", None)
        self.__mutatorenvironment_ObSelectionStrategy152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_CloneObjectMutator151"):
                opp_val = getattr(old_value, "mutatorenvironment_CloneObjectMutator151", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_CloneObjectMutator151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_CloneObjectMutator151"):
                opp_val = getattr(value, "mutatorenvironment_CloneObjectMutator151", None)
                setattr(value, "mutatorenvironment_CloneObjectMutator151", self)

    @property
    def mutatorenvironment_ObSelectionStrategy58(self):
        return self.__mutatorenvironment_ObSelectionStrategy58

    @mutatorenvironment_ObSelectionStrategy58.setter
    def mutatorenvironment_ObSelectionStrategy58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObSelectionStrategy__mutatorenvironment_ObSelectionStrategy58", None)
        self.__mutatorenvironment_ObSelectionStrategy58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_CreateReferenceMutator57"):
                opp_val = getattr(old_value, "mutatorenvironment_CreateReferenceMutator57", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_CreateReferenceMutator57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_CreateReferenceMutator57"):
                opp_val = getattr(value, "mutatorenvironment_CreateReferenceMutator57", None)
                setattr(value, "mutatorenvironment_CreateReferenceMutator57", self)

    @property
    def mutatorenvironment_ObSelectionStrategy104(self):
        return self.__mutatorenvironment_ObSelectionStrategy104

    @mutatorenvironment_ObSelectionStrategy104.setter
    def mutatorenvironment_ObSelectionStrategy104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObSelectionStrategy__mutatorenvironment_ObSelectionStrategy104", None)
        self.__mutatorenvironment_ObSelectionStrategy104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_ReferenceSet103"):
                opp_val = getattr(old_value, "mutatorenvironment_ReferenceSet103", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_ReferenceSet103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_ReferenceSet103"):
                opp_val = getattr(value, "mutatorenvironment_ReferenceSet103", None)
                setattr(value, "mutatorenvironment_ReferenceSet103", self)

    @property
    def mutatorenvironment_ObSelectionStrategy55(self):
        return self.__mutatorenvironment_ObSelectionStrategy55

    @mutatorenvironment_ObSelectionStrategy55.setter
    def mutatorenvironment_ObSelectionStrategy55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObSelectionStrategy__mutatorenvironment_ObSelectionStrategy55", None)
        self.__mutatorenvironment_ObSelectionStrategy55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_CreateReferenceMutator"):
                opp_val = getattr(old_value, "mutatorenvironment_CreateReferenceMutator", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_CreateReferenceMutator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_CreateReferenceMutator"):
                opp_val = getattr(value, "mutatorenvironment_CreateReferenceMutator", None)
                setattr(value, "mutatorenvironment_CreateReferenceMutator", self)

    @property
    def mutatorenvironment_ObSelectionStrategy66(self):
        return self.__mutatorenvironment_ObSelectionStrategy66

    @mutatorenvironment_ObSelectionStrategy66.setter
    def mutatorenvironment_ObSelectionStrategy66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObSelectionStrategy__mutatorenvironment_ObSelectionStrategy66", None)
        self.__mutatorenvironment_ObSelectionStrategy66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_RemoveObjectMutator65"):
                opp_val = getattr(old_value, "mutatorenvironment_RemoveObjectMutator65", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_RemoveObjectMutator65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_RemoveObjectMutator65"):
                opp_val = getattr(value, "mutatorenvironment_RemoveObjectMutator65", None)
                setattr(value, "mutatorenvironment_RemoveObjectMutator65", self)

    @property
    def mutatorenvironment_ObSelectionStrategy28(self):
        return self.__mutatorenvironment_ObSelectionStrategy28

    @mutatorenvironment_ObSelectionStrategy28.setter
    def mutatorenvironment_ObSelectionStrategy28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObSelectionStrategy__mutatorenvironment_ObSelectionStrategy28", None)
        self.__mutatorenvironment_ObSelectionStrategy28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_EReference29"):
                opp_val = getattr(old_value, "mutatorenvironment_EReference29", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_EReference29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_EReference29"):
                opp_val = getattr(value, "mutatorenvironment_EReference29", None)
                setattr(value, "mutatorenvironment_EReference29", self)

    @property
    def mutatorenvironment_ObSelectionStrategy(self):
        return self.__mutatorenvironment_ObSelectionStrategy

    @mutatorenvironment_ObSelectionStrategy.setter
    def mutatorenvironment_ObSelectionStrategy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObSelectionStrategy__mutatorenvironment_ObSelectionStrategy", None)
        self.__mutatorenvironment_ObSelectionStrategy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_CreateObjectMutator"):
                opp_val = getattr(old_value, "mutatorenvironment_CreateObjectMutator", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_CreateObjectMutator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_CreateObjectMutator"):
                opp_val = getattr(value, "mutatorenvironment_CreateObjectMutator", None)
                setattr(value, "mutatorenvironment_CreateObjectMutator", self)

    @property
    def mutatorenvironment_ObSelectionStrategy40(self):
        return self.__mutatorenvironment_ObSelectionStrategy40

    @mutatorenvironment_ObSelectionStrategy40.setter
    def mutatorenvironment_ObSelectionStrategy40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObSelectionStrategy__mutatorenvironment_ObSelectionStrategy40", None)
        self.__mutatorenvironment_ObSelectionStrategy40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_ModifySourceReferenceMutator39"):
                opp_val = getattr(old_value, "mutatorenvironment_ModifySourceReferenceMutator39", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_ModifySourceReferenceMutator39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_ModifySourceReferenceMutator39"):
                opp_val = getattr(value, "mutatorenvironment_ModifySourceReferenceMutator39", None)
                setattr(value, "mutatorenvironment_ModifySourceReferenceMutator39", self)

    @property
    def mutatorenvironment_ObSelectionStrategy50(self):
        return self.__mutatorenvironment_ObSelectionStrategy50

    @mutatorenvironment_ObSelectionStrategy50.setter
    def mutatorenvironment_ObSelectionStrategy50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObSelectionStrategy__mutatorenvironment_ObSelectionStrategy50", None)
        self.__mutatorenvironment_ObSelectionStrategy50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_ModifyTargetReferenceMutator49"):
                opp_val = getattr(old_value, "mutatorenvironment_ModifyTargetReferenceMutator49", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_ModifyTargetReferenceMutator49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_ModifyTargetReferenceMutator49"):
                opp_val = getattr(value, "mutatorenvironment_ModifyTargetReferenceMutator49", None)
                setattr(value, "mutatorenvironment_ModifyTargetReferenceMutator49", self)

    @property
    def mutatorenvironment_ObSelectionStrategy43(self):
        return self.__mutatorenvironment_ObSelectionStrategy43

    @mutatorenvironment_ObSelectionStrategy43.setter
    def mutatorenvironment_ObSelectionStrategy43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObSelectionStrategy__mutatorenvironment_ObSelectionStrategy43", None)
        self.__mutatorenvironment_ObSelectionStrategy43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_ModifySourceReferenceMutator42"):
                opp_val = getattr(old_value, "mutatorenvironment_ModifySourceReferenceMutator42", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_ModifySourceReferenceMutator42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_ModifySourceReferenceMutator42"):
                opp_val = getattr(value, "mutatorenvironment_ModifySourceReferenceMutator42", None)
                setattr(value, "mutatorenvironment_ModifySourceReferenceMutator42", self)

    @property
    def mutatorenvironment_ObSelectionStrategy53(self):
        return self.__mutatorenvironment_ObSelectionStrategy53

    @mutatorenvironment_ObSelectionStrategy53.setter
    def mutatorenvironment_ObSelectionStrategy53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObSelectionStrategy__mutatorenvironment_ObSelectionStrategy53", None)
        self.__mutatorenvironment_ObSelectionStrategy53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_ModifyTargetReferenceMutator52"):
                opp_val = getattr(old_value, "mutatorenvironment_ModifyTargetReferenceMutator52", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_ModifyTargetReferenceMutator52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_ModifyTargetReferenceMutator52"):
                opp_val = getattr(value, "mutatorenvironment_ModifyTargetReferenceMutator52", None)
                setattr(value, "mutatorenvironment_ModifyTargetReferenceMutator52", self)

    @property
    def mutatorenvironment_ObSelectionStrategy31(self):
        return self.__mutatorenvironment_ObSelectionStrategy31

    @mutatorenvironment_ObSelectionStrategy31.setter
    def mutatorenvironment_ObSelectionStrategy31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObSelectionStrategy__mutatorenvironment_ObSelectionStrategy31", None)
        self.__mutatorenvironment_ObSelectionStrategy31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_EReference32"):
                opp_val = getattr(old_value, "mutatorenvironment_EReference32", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_EReference32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_EReference32"):
                opp_val = getattr(value, "mutatorenvironment_EReference32", None)
                setattr(value, "mutatorenvironment_EReference32", self)

    @property
    def mutatorenvironment_ObSelectionStrategy189(self):
        return self.__mutatorenvironment_ObSelectionStrategy189

    @mutatorenvironment_ObSelectionStrategy189.setter
    def mutatorenvironment_ObSelectionStrategy189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObSelectionStrategy__mutatorenvironment_ObSelectionStrategy189", None)
        self.__mutatorenvironment_ObSelectionStrategy189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_RetypeObjectMutator188"):
                opp_val = getattr(old_value, "mutatorenvironment_RetypeObjectMutator188", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_RetypeObjectMutator188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_RetypeObjectMutator188"):
                opp_val = getattr(value, "mutatorenvironment_RetypeObjectMutator188", None)
                setattr(value, "mutatorenvironment_RetypeObjectMutator188", self)

    @property
    def mutatorenvironment_ObSelectionStrategy94(self):
        return self.__mutatorenvironment_ObSelectionStrategy94

    @mutatorenvironment_ObSelectionStrategy94.setter
    def mutatorenvironment_ObSelectionStrategy94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObSelectionStrategy__mutatorenvironment_ObSelectionStrategy94", None)
        self.__mutatorenvironment_ObSelectionStrategy94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_SelectObjectMutator93"):
                opp_val = getattr(old_value, "mutatorenvironment_SelectObjectMutator93", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_SelectObjectMutator93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_SelectObjectMutator93"):
                opp_val = getattr(value, "mutatorenvironment_SelectObjectMutator93", None)
                setattr(value, "mutatorenvironment_SelectObjectMutator93", self)

    @property
    def mutatorenvironment_ObSelectionStrategy175(self):
        return self.__mutatorenvironment_ObSelectionStrategy175

    @mutatorenvironment_ObSelectionStrategy175.setter
    def mutatorenvironment_ObSelectionStrategy175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObSelectionStrategy__mutatorenvironment_ObSelectionStrategy175", None)
        self.__mutatorenvironment_ObSelectionStrategy175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_RandomNumberType"):
                opp_val = getattr(old_value, "mutatorenvironment_RandomNumberType", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_RandomNumberType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_RandomNumberType"):
                opp_val = getattr(value, "mutatorenvironment_RandomNumberType", None)
                setattr(value, "mutatorenvironment_RandomNumberType", self)

    @property
    def mutatorenvironment_ObSelectionStrategy182(self):
        return self.__mutatorenvironment_ObSelectionStrategy182

    @mutatorenvironment_ObSelectionStrategy182.setter
    def mutatorenvironment_ObSelectionStrategy182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObSelectionStrategy__mutatorenvironment_ObSelectionStrategy182", None)
        self.__mutatorenvironment_ObSelectionStrategy182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_SelectSampleMutator"):
                opp_val = getattr(old_value, "mutatorenvironment_SelectSampleMutator", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_SelectSampleMutator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_SelectSampleMutator"):
                opp_val = getattr(value, "mutatorenvironment_SelectSampleMutator", None)
                setattr(value, "mutatorenvironment_SelectSampleMutator", self)

    @property
    def mutatorenvironment_ObSelectionStrategy91(self):
        return self.__mutatorenvironment_ObSelectionStrategy91

    @mutatorenvironment_ObSelectionStrategy91.setter
    def mutatorenvironment_ObSelectionStrategy91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObSelectionStrategy__mutatorenvironment_ObSelectionStrategy91", None)
        self.__mutatorenvironment_ObSelectionStrategy91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_SelectObjectMutator"):
                opp_val = getattr(old_value, "mutatorenvironment_SelectObjectMutator", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_SelectObjectMutator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_SelectObjectMutator"):
                opp_val = getattr(value, "mutatorenvironment_SelectObjectMutator", None)
                setattr(value, "mutatorenvironment_SelectObjectMutator", self)

class mutatorenvironment_EClass:

    pass
class mutatorenvironment_ObjectEmitter(ABC):

    def __init__(self, name: str, mutatorenvironment_ObjectEmitter: "mutatorenvironment_EClass" = None, mutatorenvironment_ObjectEmitter14: set["mutatorenvironment_EClass"] = None, mutatorenvironment_ObjectEmitter34: "mutatorenvironment_SpecificObjectSelection" = None, mutatorenvironment_ObjectEmitter45: "mutatorenvironment_SpecificReferenceSelection" = None, mutatorenvironment_ObjectEmitter164: "mutatorenvironment_ObjectAttributeType" = None, mutatorenvironment_ObjectEmitter180: "mutatorenvironment_SpecificClosureSelection" = None):
        self.name = name
        self.mutatorenvironment_ObjectEmitter = mutatorenvironment_ObjectEmitter
        self.mutatorenvironment_ObjectEmitter14 = mutatorenvironment_ObjectEmitter14 if mutatorenvironment_ObjectEmitter14 is not None else set()
        self.mutatorenvironment_ObjectEmitter34 = mutatorenvironment_ObjectEmitter34
        self.mutatorenvironment_ObjectEmitter45 = mutatorenvironment_ObjectEmitter45
        self.mutatorenvironment_ObjectEmitter164 = mutatorenvironment_ObjectEmitter164
        self.mutatorenvironment_ObjectEmitter180 = mutatorenvironment_ObjectEmitter180
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mutatorenvironment_ObjectEmitter34(self):
        return self.__mutatorenvironment_ObjectEmitter34

    @mutatorenvironment_ObjectEmitter34.setter
    def mutatorenvironment_ObjectEmitter34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObjectEmitter__mutatorenvironment_ObjectEmitter34", None)
        self.__mutatorenvironment_ObjectEmitter34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_SpecificObjectSelection"):
                opp_val = getattr(old_value, "mutatorenvironment_SpecificObjectSelection", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_SpecificObjectSelection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_SpecificObjectSelection"):
                opp_val = getattr(value, "mutatorenvironment_SpecificObjectSelection", None)
                setattr(value, "mutatorenvironment_SpecificObjectSelection", self)

    @property
    def mutatorenvironment_ObjectEmitter45(self):
        return self.__mutatorenvironment_ObjectEmitter45

    @mutatorenvironment_ObjectEmitter45.setter
    def mutatorenvironment_ObjectEmitter45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObjectEmitter__mutatorenvironment_ObjectEmitter45", None)
        self.__mutatorenvironment_ObjectEmitter45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_SpecificReferenceSelection"):
                opp_val = getattr(old_value, "mutatorenvironment_SpecificReferenceSelection", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_SpecificReferenceSelection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_SpecificReferenceSelection"):
                opp_val = getattr(value, "mutatorenvironment_SpecificReferenceSelection", None)
                setattr(value, "mutatorenvironment_SpecificReferenceSelection", self)

    @property
    def mutatorenvironment_ObjectEmitter164(self):
        return self.__mutatorenvironment_ObjectEmitter164

    @mutatorenvironment_ObjectEmitter164.setter
    def mutatorenvironment_ObjectEmitter164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObjectEmitter__mutatorenvironment_ObjectEmitter164", None)
        self.__mutatorenvironment_ObjectEmitter164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_ObjectAttributeType"):
                opp_val = getattr(old_value, "mutatorenvironment_ObjectAttributeType", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_ObjectAttributeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_ObjectAttributeType"):
                opp_val = getattr(value, "mutatorenvironment_ObjectAttributeType", None)
                setattr(value, "mutatorenvironment_ObjectAttributeType", self)

    @property
    def mutatorenvironment_ObjectEmitter180(self):
        return self.__mutatorenvironment_ObjectEmitter180

    @mutatorenvironment_ObjectEmitter180.setter
    def mutatorenvironment_ObjectEmitter180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObjectEmitter__mutatorenvironment_ObjectEmitter180", None)
        self.__mutatorenvironment_ObjectEmitter180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_SpecificClosureSelection"):
                opp_val = getattr(old_value, "mutatorenvironment_SpecificClosureSelection", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_SpecificClosureSelection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_SpecificClosureSelection"):
                opp_val = getattr(value, "mutatorenvironment_SpecificClosureSelection", None)
                setattr(value, "mutatorenvironment_SpecificClosureSelection", self)

    @property
    def mutatorenvironment_ObjectEmitter14(self):
        return self.__mutatorenvironment_ObjectEmitter14

    @mutatorenvironment_ObjectEmitter14.setter
    def mutatorenvironment_ObjectEmitter14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObjectEmitter__mutatorenvironment_ObjectEmitter14", None)
        self.__mutatorenvironment_ObjectEmitter14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mutatorenvironment_EClass15"):
                    opp_val = getattr(item, "mutatorenvironment_EClass15", None)
                    
                    if opp_val == self:
                        setattr(item, "mutatorenvironment_EClass15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mutatorenvironment_EClass15"):
                    opp_val = getattr(item, "mutatorenvironment_EClass15", None)
                    
                    setattr(item, "mutatorenvironment_EClass15", self)
                    

    @property
    def mutatorenvironment_ObjectEmitter(self):
        return self.__mutatorenvironment_ObjectEmitter

    @mutatorenvironment_ObjectEmitter.setter
    def mutatorenvironment_ObjectEmitter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_ObjectEmitter__mutatorenvironment_ObjectEmitter", None)
        self.__mutatorenvironment_ObjectEmitter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_EClass"):
                opp_val = getattr(old_value, "mutatorenvironment_EClass", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_EClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_EClass"):
                opp_val = getattr(value, "mutatorenvironment_EClass", None)
                setattr(value, "mutatorenvironment_EClass", self)

class Definition:

    pass
class mutatorenvironment_Program(Definition):

    def __init__(self, output: str, num: int, description: str, exhaustive: bool, mutatorenvironment_Program11: set["mutatorenvironment_Resource"] = None, mutatorenvironment_Program: "mutatorenvironment_Source" = None):
        self.output = output
        self.num = num
        self.description = description
        self.exhaustive = exhaustive
        self.mutatorenvironment_Program11 = mutatorenvironment_Program11 if mutatorenvironment_Program11 is not None else set()
        self.mutatorenvironment_Program = mutatorenvironment_Program
        
    @property
    def num(self) -> int:
        return self.__num

    @num.setter
    def num(self, num: int):
        self.__num = num

    @property
    def exhaustive(self) -> bool:
        return self.__exhaustive

    @exhaustive.setter
    def exhaustive(self, exhaustive: bool):
        self.__exhaustive = exhaustive

    @property
    def output(self) -> str:
        return self.__output

    @output.setter
    def output(self, output: str):
        self.__output = output

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def mutatorenvironment_Program(self):
        return self.__mutatorenvironment_Program

    @mutatorenvironment_Program.setter
    def mutatorenvironment_Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_Program__mutatorenvironment_Program", None)
        self.__mutatorenvironment_Program = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_Source"):
                opp_val = getattr(old_value, "mutatorenvironment_Source", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_Source", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_Source"):
                opp_val = getattr(value, "mutatorenvironment_Source", None)
                setattr(value, "mutatorenvironment_Source", self)

    @property
    def mutatorenvironment_Program11(self):
        return self.__mutatorenvironment_Program11

    @mutatorenvironment_Program11.setter
    def mutatorenvironment_Program11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_Program__mutatorenvironment_Program11", None)
        self.__mutatorenvironment_Program11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mutatorenvironment_Resource"):
                    opp_val = getattr(item, "mutatorenvironment_Resource", None)
                    
                    if opp_val == self:
                        setattr(item, "mutatorenvironment_Resource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mutatorenvironment_Resource"):
                    opp_val = getattr(item, "mutatorenvironment_Resource", None)
                    
                    setattr(item, "mutatorenvironment_Resource", self)
                    

class mutatorenvironment_Resource(Definition):

    def __init__(self, name: str, mutatorenvironment_Resource: "mutatorenvironment_Program" = None, mutatorenvironment_Resource200: "mutatorenvironment_Source" = None):
        self.name = name
        self.mutatorenvironment_Resource = mutatorenvironment_Resource
        self.mutatorenvironment_Resource200 = mutatorenvironment_Resource200
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mutatorenvironment_Resource(self):
        return self.__mutatorenvironment_Resource

    @mutatorenvironment_Resource.setter
    def mutatorenvironment_Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_Resource__mutatorenvironment_Resource", None)
        self.__mutatorenvironment_Resource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_Program11"):
                opp_val = getattr(old_value, "mutatorenvironment_Program11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_Program11"):
                opp_val = getattr(value, "mutatorenvironment_Program11", None)
                if opp_val is None:
                    setattr(value, "mutatorenvironment_Program11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mutatorenvironment_Resource200(self):
        return self.__mutatorenvironment_Resource200

    @mutatorenvironment_Resource200.setter
    def mutatorenvironment_Resource200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_Resource__mutatorenvironment_Resource200", None)
        self.__mutatorenvironment_Resource200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_Source201"):
                opp_val = getattr(old_value, "mutatorenvironment_Source201", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_Source201", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_Source201"):
                opp_val = getattr(value, "mutatorenvironment_Source201", None)
                setattr(value, "mutatorenvironment_Source201", self)

class mutatorenvironment_Library(Definition):

    pass
class mutatorenvironment_Constraint:

    def __init__(self, id: str, rules: str, mutatorenvironment_Constraint: "mutatorenvironment_MutatorEnvironment" = None, mutatorenvironment_Constraint144: "mutatorenvironment_EClass" = None, mutatorenvironment_Constraint147: set["InvariantCS"] = None):
        self.id = id
        self.rules = rules
        self.mutatorenvironment_Constraint = mutatorenvironment_Constraint
        self.mutatorenvironment_Constraint144 = mutatorenvironment_Constraint144
        self.mutatorenvironment_Constraint147 = mutatorenvironment_Constraint147 if mutatorenvironment_Constraint147 is not None else set()
        
    @property
    def rules(self) -> str:
        return self.__rules

    @rules.setter
    def rules(self, rules: str):
        self.__rules = rules

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def mutatorenvironment_Constraint144(self):
        return self.__mutatorenvironment_Constraint144

    @mutatorenvironment_Constraint144.setter
    def mutatorenvironment_Constraint144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_Constraint__mutatorenvironment_Constraint144", None)
        self.__mutatorenvironment_Constraint144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_EClass145"):
                opp_val = getattr(old_value, "mutatorenvironment_EClass145", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_EClass145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_EClass145"):
                opp_val = getattr(value, "mutatorenvironment_EClass145", None)
                setattr(value, "mutatorenvironment_EClass145", self)

    @property
    def mutatorenvironment_Constraint(self):
        return self.__mutatorenvironment_Constraint

    @mutatorenvironment_Constraint.setter
    def mutatorenvironment_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_Constraint__mutatorenvironment_Constraint", None)
        self.__mutatorenvironment_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_MutatorEnvironment8"):
                opp_val = getattr(old_value, "mutatorenvironment_MutatorEnvironment8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_MutatorEnvironment8"):
                opp_val = getattr(value, "mutatorenvironment_MutatorEnvironment8", None)
                if opp_val is None:
                    setattr(value, "mutatorenvironment_MutatorEnvironment8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mutatorenvironment_Constraint147(self):
        return self.__mutatorenvironment_Constraint147

    @mutatorenvironment_Constraint147.setter
    def mutatorenvironment_Constraint147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_Constraint__mutatorenvironment_Constraint147", None)
        self.__mutatorenvironment_Constraint147 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InvariantCS"):
                    opp_val = getattr(item, "InvariantCS", None)
                    
                    if opp_val == self:
                        setattr(item, "InvariantCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InvariantCS"):
                    opp_val = getattr(item, "InvariantCS", None)
                    
                    setattr(item, "InvariantCS", self)
                    

class mutatorenvironment_Block:

    def __init__(self, name: str, repeat: str, min: int, max: int, fixed: int, description: str, mutatorenvironment_Block: "mutatorenvironment_MutatorEnvironment" = None, mutatorenvironment_Block138: set["mutatorenvironment_Mutator"] = None, mutatorenvironment_Block142: "mutatorenvironment_Block" = None, mutatorenvironment_Block140: set["mutatorenvironment_Block"] = None):
        self.name = name
        self.repeat = repeat
        self.min = min
        self.max = max
        self.fixed = fixed
        self.description = description
        self.mutatorenvironment_Block = mutatorenvironment_Block
        self.mutatorenvironment_Block138 = mutatorenvironment_Block138 if mutatorenvironment_Block138 is not None else set()
        self.mutatorenvironment_Block142 = mutatorenvironment_Block142
        self.mutatorenvironment_Block140 = mutatorenvironment_Block140 if mutatorenvironment_Block140 is not None else set()
        
    @property
    def max(self) -> int:
        return self.__max

    @max.setter
    def max(self, max: int):
        self.__max = max

    @property
    def fixed(self) -> int:
        return self.__fixed

    @fixed.setter
    def fixed(self, fixed: int):
        self.__fixed = fixed

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def min(self) -> int:
        return self.__min

    @min.setter
    def min(self, min: int):
        self.__min = min

    @property
    def repeat(self) -> str:
        return self.__repeat

    @repeat.setter
    def repeat(self, repeat: str):
        self.__repeat = repeat

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mutatorenvironment_Block138(self):
        return self.__mutatorenvironment_Block138

    @mutatorenvironment_Block138.setter
    def mutatorenvironment_Block138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_Block__mutatorenvironment_Block138", None)
        self.__mutatorenvironment_Block138 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mutatorenvironment_Mutator139"):
                    opp_val = getattr(item, "mutatorenvironment_Mutator139", None)
                    
                    if opp_val == self:
                        setattr(item, "mutatorenvironment_Mutator139", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mutatorenvironment_Mutator139"):
                    opp_val = getattr(item, "mutatorenvironment_Mutator139", None)
                    
                    setattr(item, "mutatorenvironment_Mutator139", self)
                    

    @property
    def mutatorenvironment_Block(self):
        return self.__mutatorenvironment_Block

    @mutatorenvironment_Block.setter
    def mutatorenvironment_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_Block__mutatorenvironment_Block", None)
        self.__mutatorenvironment_Block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_MutatorEnvironment6"):
                opp_val = getattr(old_value, "mutatorenvironment_MutatorEnvironment6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_MutatorEnvironment6"):
                opp_val = getattr(value, "mutatorenvironment_MutatorEnvironment6", None)
                if opp_val is None:
                    setattr(value, "mutatorenvironment_MutatorEnvironment6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mutatorenvironment_Block140(self):
        return self.__mutatorenvironment_Block140

    @mutatorenvironment_Block140.setter
    def mutatorenvironment_Block140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_Block__mutatorenvironment_Block140", None)
        self.__mutatorenvironment_Block140 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mutatorenvironment_Block142"):
                    opp_val = getattr(item, "mutatorenvironment_Block142", None)
                    
                    if opp_val == self:
                        setattr(item, "mutatorenvironment_Block142", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mutatorenvironment_Block142"):
                    opp_val = getattr(item, "mutatorenvironment_Block142", None)
                    
                    setattr(item, "mutatorenvironment_Block142", self)
                    

    @property
    def mutatorenvironment_Block142(self):
        return self.__mutatorenvironment_Block142

    @mutatorenvironment_Block142.setter
    def mutatorenvironment_Block142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_Block__mutatorenvironment_Block142", None)
        self.__mutatorenvironment_Block142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_Block140"):
                opp_val = getattr(old_value, "mutatorenvironment_Block140", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_Block140"):
                opp_val = getattr(value, "mutatorenvironment_Block140", None)
                if opp_val is None:
                    setattr(value, "mutatorenvironment_Block140", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mutatorenvironment_Load:

    def __init__(self, file: str, mutatorenvironment_Load: "mutatorenvironment_MutatorEnvironment" = None):
        self.file = file
        self.mutatorenvironment_Load = mutatorenvironment_Load
        
    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

    @property
    def mutatorenvironment_Load(self):
        return self.__mutatorenvironment_Load

    @mutatorenvironment_Load.setter
    def mutatorenvironment_Load(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_Load__mutatorenvironment_Load", None)
        self.__mutatorenvironment_Load = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_MutatorEnvironment4"):
                opp_val = getattr(old_value, "mutatorenvironment_MutatorEnvironment4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_MutatorEnvironment4"):
                opp_val = getattr(value, "mutatorenvironment_MutatorEnvironment4", None)
                if opp_val is None:
                    setattr(value, "mutatorenvironment_MutatorEnvironment4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mutatorenvironment_Mutator(ObjectEmitter):

    def __init__(self, min: int, max: int, fixed: int, mutatorenvironment_Mutator: "mutatorenvironment_MutatorEnvironment" = None, mutatorenvironment_Mutator17: "mutatorenvironment_CompositeMutator" = None, mutatorenvironment_Mutator139: "mutatorenvironment_Block" = None):
        self.min = min
        self.max = max
        self.fixed = fixed
        self.mutatorenvironment_Mutator = mutatorenvironment_Mutator
        self.mutatorenvironment_Mutator17 = mutatorenvironment_Mutator17
        self.mutatorenvironment_Mutator139 = mutatorenvironment_Mutator139
        
    @property
    def max(self) -> int:
        return self.__max

    @max.setter
    def max(self, max: int):
        self.__max = max

    @property
    def fixed(self) -> int:
        return self.__fixed

    @fixed.setter
    def fixed(self, fixed: int):
        self.__fixed = fixed

    @property
    def min(self) -> int:
        return self.__min

    @min.setter
    def min(self, min: int):
        self.__min = min

    @property
    def mutatorenvironment_Mutator17(self):
        return self.__mutatorenvironment_Mutator17

    @mutatorenvironment_Mutator17.setter
    def mutatorenvironment_Mutator17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_Mutator__mutatorenvironment_Mutator17", None)
        self.__mutatorenvironment_Mutator17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_CompositeMutator"):
                opp_val = getattr(old_value, "mutatorenvironment_CompositeMutator", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_CompositeMutator"):
                opp_val = getattr(value, "mutatorenvironment_CompositeMutator", None)
                if opp_val is None:
                    setattr(value, "mutatorenvironment_CompositeMutator", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mutatorenvironment_Mutator139(self):
        return self.__mutatorenvironment_Mutator139

    @mutatorenvironment_Mutator139.setter
    def mutatorenvironment_Mutator139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_Mutator__mutatorenvironment_Mutator139", None)
        self.__mutatorenvironment_Mutator139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_Block138"):
                opp_val = getattr(old_value, "mutatorenvironment_Block138", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_Block138"):
                opp_val = getattr(value, "mutatorenvironment_Block138", None)
                if opp_val is None:
                    setattr(value, "mutatorenvironment_Block138", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mutatorenvironment_Mutator(self):
        return self.__mutatorenvironment_Mutator

    @mutatorenvironment_Mutator.setter
    def mutatorenvironment_Mutator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_Mutator__mutatorenvironment_Mutator", None)
        self.__mutatorenvironment_Mutator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_MutatorEnvironment2"):
                opp_val = getattr(old_value, "mutatorenvironment_MutatorEnvironment2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_MutatorEnvironment2"):
                opp_val = getattr(value, "mutatorenvironment_MutatorEnvironment2", None)
                if opp_val is None:
                    setattr(value, "mutatorenvironment_MutatorEnvironment2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mutatorenvironment_Definition(ABC):

    def __init__(self, metamodel: str, mutatorenvironment_Definition: "mutatorenvironment_MutatorEnvironment" = None):
        self.metamodel = metamodel
        self.mutatorenvironment_Definition = mutatorenvironment_Definition
        
    @property
    def metamodel(self) -> str:
        return self.__metamodel

    @metamodel.setter
    def metamodel(self, metamodel: str):
        self.__metamodel = metamodel

    @property
    def mutatorenvironment_Definition(self):
        return self.__mutatorenvironment_Definition

    @mutatorenvironment_Definition.setter
    def mutatorenvironment_Definition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mutatorenvironment_Definition__mutatorenvironment_Definition", None)
        self.__mutatorenvironment_Definition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mutatorenvironment_MutatorEnvironment"):
                opp_val = getattr(old_value, "mutatorenvironment_MutatorEnvironment", None)
                if opp_val == self:
                    setattr(old_value, "mutatorenvironment_MutatorEnvironment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mutatorenvironment_MutatorEnvironment"):
                opp_val = getattr(value, "mutatorenvironment_MutatorEnvironment", None)
                setattr(value, "mutatorenvironment_MutatorEnvironment", self)

class mutatorenvironment_MutatorEnvironment:

    pass