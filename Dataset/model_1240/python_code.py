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

class imperativeocl_Typedef:

    pass
class CatchExp:

    pass
class imperativeocl_TemplateParameterType:

    def __init__(self, specification: str):
        self.specification = specification
        
    @property
    def specification(self) -> str:
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification

class AltExp:

    pass
class imperativeocl_SwitchExp:

    pass
class imperativeocl_OrderedTupleType:

    pass
class imperativeocl_OrderedTupleLiteralPart:

    pass
class OrderedTupleLiteralPart:

    pass
class imperativeocl_OrderedTupleLiteralExp:

    pass
class imperativeocl_ImperativeLoopExp(ABC):

    pass
class imperativeocl_ImperativeExpression(ABC):

    pass
class ImperativeLoopExp:

    pass
class imperativeocl_ImperativeIterateExp(ImperativeLoopExp):

    pass
class imperativeocl_ForExp(ImperativeLoopExp):

    pass
class imperativeocl_DictionaryType:

    pass
class imperativeocl_DictLiteralPart:

    pass
class DictLiteralPart:

    pass
class imperativeocl_DictLiteralExp:

    pass
class imperativeocl_LogExp:

    pass
class imperativeocl_ListType:

    pass
class LogExp:

    pass
class ImperativeExpression:

    pass
class imperativeocl_WhileExp(ImperativeExpression):

    pass
class imperativeocl_ComputeExp(ImperativeExpression):

    pass
class imperativeocl_UnpackExp(ImperativeExpression):

    pass
class imperativeocl_UnlinkExp(ImperativeExpression):

    pass
class imperativeocl_TryExp(ImperativeExpression):

    pass
class imperativeocl_ReturnExp(ImperativeExpression):

    pass
class imperativeocl_VariableInitExp(ImperativeExpression):

    def __init__(self, withResult: str):
        self.withResult = withResult
        
    @property
    def withResult(self) -> str:
        return self.__withResult

    @withResult.setter
    def withResult(self, withResult: str):
        self.__withResult = withResult

class imperativeocl_InstantiationExp(ImperativeExpression):

    pass
class imperativeocl_ContinueExp(ImperativeExpression):

    pass
class imperativeocl_BlockExp(ImperativeExpression):

    pass
class imperativeocl_RaiseExp(ImperativeExpression):

    pass
class imperativeocl_BreakExp(ImperativeExpression):

    pass
class imperativeocl_AssignExp(ImperativeExpression):

    def __init__(self, isReset: str):
        self.isReset = isReset
        
    @property
    def isReset(self) -> str:
        return self.__isReset

    @isReset.setter
    def isReset(self, isReset: str):
        self.__isReset = isReset

class imperativeocl_CatchExp(ImperativeExpression):

    pass
class imperativeocl_AltExp(ImperativeExpression):

    pass
class imperativeocl_AssertExp(ImperativeExpression):

    def __init__(self, severity: str, imperativeocl_AssertExp: "LogExp" = None):
        self.severity = severity
        self.imperativeocl_AssertExp = imperativeocl_AssertExp
        
    @property
    def severity(self) -> str:
        return self.__severity

    @severity.setter
    def severity(self, severity: str):
        self.__severity = severity

    @property
    def imperativeocl_AssertExp(self):
        return self.__imperativeocl_AssertExp

    @imperativeocl_AssertExp.setter
    def imperativeocl_AssertExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imperativeocl_AssertExp__imperativeocl_AssertExp", None)
        self.__imperativeocl_AssertExp = value
        
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
