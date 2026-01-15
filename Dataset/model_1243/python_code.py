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

class ImperativeOCL_Typedef:

    pass
class CatchExp:

    pass
class ImperativeOCL_OrderedTupleType:

    pass
class ImperativeOCL_OrderedTupleLiteralPart:

    pass
class OrderedTupleLiteralPart:

    pass
class ImperativeOCL_OrderedTupleLiteralExp:

    pass
class ImperativeOCL_LogExp:

    pass
class ImperativeOCL_ListType:

    pass
class ImperativeOCL_ListLiteralExp:

    pass
class AltExp:

    pass
class ImperativeOCL_ImperativeExpression(ABC):

    pass
class ImperativeLoopExp:

    pass
class ImperativeOCL_ImperativeIterateExp(ImperativeLoopExp):

    pass
class ImperativeOCL_ForExp(ImperativeLoopExp):

    pass
class ImperativeOCL_DictionaryType:

    pass
class ImperativeOCL_DictLiteralPart:

    pass
class DictLiteralPart:

    pass
class ImperativeOCL_DictLiteralExp:

    pass
class ImperativeOCL_ImperativeLoopExp(ABC):

    pass
class LogExp:

    pass
class ImperativeExpression:

    pass
class ImperativeOCL_ComputeExp(ImperativeExpression):

    pass
class ImperativeOCL_CatchExp(ImperativeExpression):

    pass
class ImperativeOCL_InstantiationExp(ImperativeExpression):

    pass
class ImperativeOCL_BreakExp(ImperativeExpression):

    pass
class ImperativeOCL_TryExp(ImperativeExpression):

    pass
class ImperativeOCL_SwitchExp(ImperativeExpression):

    pass
class ImperativeOCL_AssignExp(ImperativeExpression):

    def __init__(self, isReset: str):
        self.isReset = isReset
        
    @property
    def isReset(self) -> str:
        return self.__isReset

    @isReset.setter
    def isReset(self, isReset: str):
        self.__isReset = isReset

class ImperativeOCL_ReturnExp(ImperativeExpression):

    pass
class ImperativeOCL_WhileExp(ImperativeExpression):

    pass
class ImperativeOCL_UnlinkExp(ImperativeExpression):

    pass
class ImperativeOCL_BlockExp(ImperativeExpression):

    pass
class ImperativeOCL_UnpackExp(ImperativeExpression):

    pass
class ImperativeOCL_VariableInitExp(ImperativeExpression):

    def __init__(self, withResult: str):
        self.withResult = withResult
        
    @property
    def withResult(self) -> str:
        return self.__withResult

    @withResult.setter
    def withResult(self, withResult: str):
        self.__withResult = withResult

class ImperativeOCL_AssertExp(ImperativeExpression):

    def __init__(self, severity: str, ImperativeOCL_AssertExp: "LogExp" = None):
        self.severity = severity
        self.ImperativeOCL_AssertExp = ImperativeOCL_AssertExp
        
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
            if hasattr(old_value, "LogExp"):
                opp_val = getattr(old_value, "LogExp", None)
                if opp_val == self:
                    setattr(old_value, "LogExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LogExp"):
                opp_val = getattr(value, "LogExp", None)
                setattr(value, "LogExp", self)

class ImperativeOCL_RaiseExp(ImperativeExpression):

    pass
class ImperativeOCL_ContinueExp(ImperativeExpression):

    pass
class ImperativeOCL_AltExp(ImperativeExpression):

    pass