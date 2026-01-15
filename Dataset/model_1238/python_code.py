from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SeverityKind(Enum):
    error = "error"
    warning = "warning"
    fatal = "fatal"


############################################
# Definition of Classes
############################################

class CatchExp:

    pass
class AltExp:

    pass
class Operation:

    pass
class Class:

    pass
class ImperativeOCL_Typedef(Class):

    pass
class OperationCallExp:

    pass
class DictLiteralExp:

    pass
class Element:

    pass
class ImperativeOCL_DictLiteralPart(Element):

    pass
class DictLiteralPart:

    pass
class LiteralExp:

    pass
class ImperativeOCL_ListLiteralExp(LiteralExp):

    pass
class ImperativeOCL_DictLiteralExp(LiteralExp):

    pass
class LoopExp:

    pass
class ImperativeLoopExp:

    pass
class ImperativeOCL_ImperativeIterateExp(ImperativeLoopExp):

    pass
class ImperativeOCL_ForExp(ImperativeLoopExp):

    pass
class CollectionType:

    pass
class ImperativeOCL_ListType(CollectionType):

    pass
class ImperativeOCL_DictionaryType(CollectionType):

    pass
class Variable:

    pass
class Type:

    pass
class OclExpression:

    pass
class ImperativeOCL_ImperativeExpression(OclExpression):

    pass
class ImperativeExpression:

    pass
class ImperativeOCL_LogExp(ImperativeExpression, OperationCallExp):

    pass
class ImperativeOCL_TryExp(ImperativeExpression):

    pass
class ImperativeOCL_CatchExp(ImperativeExpression):

    pass
class ImperativeOCL_WhileExp(ImperativeExpression):

    pass
class ImperativeOCL_InstantiationExp(ImperativeExpression):

    pass
class ImperativeOCL_BreakExp(ImperativeExpression):

    pass
class ImperativeOCL_VariableInitExp(ImperativeExpression):

    def __init__(self, withResult: str, ImperativeOCL_VariableInitExp: "Variable" = None):
        self.withResult = withResult
        self.ImperativeOCL_VariableInitExp = ImperativeOCL_VariableInitExp
        
    @property
    def withResult(self) -> str:
        return self.__withResult

    @withResult.setter
    def withResult(self, withResult: str):
        self.__withResult = withResult

    @property
    def ImperativeOCL_VariableInitExp(self):
        return self.__ImperativeOCL_VariableInitExp

    @ImperativeOCL_VariableInitExp.setter
    def ImperativeOCL_VariableInitExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ImperativeOCL_VariableInitExp__ImperativeOCL_VariableInitExp", None)
        self.__ImperativeOCL_VariableInitExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable82"):
                opp_val = getattr(old_value, "Variable82", None)
                if opp_val == self:
                    setattr(old_value, "Variable82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable82"):
                opp_val = getattr(value, "Variable82", None)
                setattr(value, "Variable82", self)

class ImperativeOCL_UnlinkExp(ImperativeExpression):

    pass
class ImperativeOCL_ImperativeLoopExp(LoopExp, ImperativeExpression):

    pass
class ImperativeOCL_RaiseExp(ImperativeExpression):

    pass
class ImperativeOCL_SwitchExp(ImperativeExpression):

    pass
class ImperativeOCL_ReturnExp(ImperativeExpression):

    pass
class ImperativeOCL_BlockExp(ImperativeExpression):

    pass
class ImperativeOCL_ComputeExp(ImperativeExpression):

    pass
class ImperativeOCL_ContinueExp(ImperativeExpression):

    pass
class ImperativeOCL_AssignExp(ImperativeExpression):

    def __init__(self, isReset: str, ImperativeOCL_AssignExp: "OclExpression" = None, ImperativeOCL_AssignExp11: "OclExpression" = None, ImperativeOCL_AssignExp14: set["OclExpression"] = None):
        self.isReset = isReset
        self.ImperativeOCL_AssignExp = ImperativeOCL_AssignExp
        self.ImperativeOCL_AssignExp11 = ImperativeOCL_AssignExp11
        self.ImperativeOCL_AssignExp14 = ImperativeOCL_AssignExp14 if ImperativeOCL_AssignExp14 is not None else set()
        
    @property
    def isReset(self) -> str:
        return self.__isReset

    @isReset.setter
    def isReset(self, isReset: str):
        self.__isReset = isReset

    @property
    def ImperativeOCL_AssignExp(self):
        return self.__ImperativeOCL_AssignExp

    @ImperativeOCL_AssignExp.setter
    def ImperativeOCL_AssignExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ImperativeOCL_AssignExp__ImperativeOCL_AssignExp", None)
        self.__ImperativeOCL_AssignExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression9"):
                opp_val = getattr(old_value, "OclExpression9", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression9"):
                opp_val = getattr(value, "OclExpression9", None)
                setattr(value, "OclExpression9", self)

    @property
    def ImperativeOCL_AssignExp14(self):
        return self.__ImperativeOCL_AssignExp14

    @ImperativeOCL_AssignExp14.setter
    def ImperativeOCL_AssignExp14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ImperativeOCL_AssignExp__ImperativeOCL_AssignExp14", None)
        self.__ImperativeOCL_AssignExp14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression15"):
                    opp_val = getattr(item, "OclExpression15", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression15"):
                    opp_val = getattr(item, "OclExpression15", None)
                    
                    setattr(item, "OclExpression15", self)
                    

    @property
    def ImperativeOCL_AssignExp11(self):
        return self.__ImperativeOCL_AssignExp11

    @ImperativeOCL_AssignExp11.setter
    def ImperativeOCL_AssignExp11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ImperativeOCL_AssignExp__ImperativeOCL_AssignExp11", None)
        self.__ImperativeOCL_AssignExp11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression12"):
                opp_val = getattr(old_value, "OclExpression12", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression12"):
                opp_val = getattr(value, "OclExpression12", None)
                setattr(value, "OclExpression12", self)

class ImperativeOCL_AltExp(ImperativeExpression):

    pass
class LogExp:

    pass
class ImperativeOCL_AssertExp(ImperativeExpression):

    def __init__(self, severity: str, ImperativeOCL_AssertExp: "OclExpression" = None, ImperativeOCL_AssertExp7: "LogExp" = None):
        self.severity = severity
        self.ImperativeOCL_AssertExp = ImperativeOCL_AssertExp
        self.ImperativeOCL_AssertExp7 = ImperativeOCL_AssertExp7
        
    @property
    def severity(self) -> str:
        return self.__severity

    @severity.setter
    def severity(self, severity: str):
        self.__severity = severity

    @property
    def ImperativeOCL_AssertExp(self):
        return self.__ImperativeOCL_AssertExp

    @ImperativeOCL_AssertExp.setter
    def ImperativeOCL_AssertExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ImperativeOCL_AssertExp__ImperativeOCL_AssertExp", None)
        self.__ImperativeOCL_AssertExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression5"):
                opp_val = getattr(old_value, "OclExpression5", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression5"):
                opp_val = getattr(value, "OclExpression5", None)
                setattr(value, "OclExpression5", self)

    @property
    def ImperativeOCL_AssertExp7(self):
        return self.__ImperativeOCL_AssertExp7

    @ImperativeOCL_AssertExp7.setter
    def ImperativeOCL_AssertExp7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ImperativeOCL_AssertExp__ImperativeOCL_AssertExp7", None)
        self.__ImperativeOCL_AssertExp7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LogExp"):
                opp_val = getattr(old_value, "LogExp", None)
                if opp_val == self:
                    setattr(old_value, "LogExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LogExp"):
                opp_val = getattr(value, "LogExp", None)
                setattr(value, "LogExp", self)
