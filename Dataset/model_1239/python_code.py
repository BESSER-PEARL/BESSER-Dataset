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

class OclExpression:

    pass
class imperativeocl_ImperativeExpression(OclExpression):

    pass
class LoopExp:

    pass
class OperationCallExp:

    pass
class Type:

    pass
class imperativeocl_TemplateParameterType(Type):

    def __init__(self, specification: str):
        self.specification = specification
        
    @property
    def specification(self) -> str:
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification

class Element:

    pass
class imperativeocl_OrderedTupleLiteralPart(Element):

    pass
class imperativeocl_DictLiteralPart(Element):

    pass
class LiteralExp:

    pass
class imperativeocl_OrderedTupleLiteralExp(LiteralExp):

    pass
class imperativeocl_DictLiteralExp(LiteralExp):

    pass
class CollectionType:

    pass
class imperativeocl_ListType(CollectionType):

    pass
class imperativeocl_DictionaryType(CollectionType):

    pass
class imperativeocl_Class:

    pass
class Class:

    pass
class imperativeocl_OrderedTupleType(Class):

    pass
class imperativeocl_Typedef(Class):

    pass
class ImperativeLoopExp:

    pass
class imperativeocl_ImperativeIterateExp(ImperativeLoopExp):

    pass
class imperativeocl_ForExp(ImperativeLoopExp):

    pass
class imperativeocl_Type:

    pass
class imperativeocl_OclExpression:

    pass
class imperativeocl_Variable:

    pass
class CallExp:

    pass
class ImperativeExpression:

    pass
class imperativeocl_UnlinkExp(ImperativeExpression):

    pass
class imperativeocl_BreakExp(ImperativeExpression):

    pass
class imperativeocl_UnpackExp(ImperativeExpression):

    pass
class imperativeocl_ComputeExp(ImperativeExpression):

    pass
class imperativeocl_SwitchExp(CallExp, ImperativeExpression):

    pass
class imperativeocl_BlockExp(ImperativeExpression):

    pass
class imperativeocl_VariableInitExp(ImperativeExpression):

    def __init__(self, withResult: str, imperativeocl_VariableInitExp: "imperativeocl_Variable" = None):
        self.withResult = withResult
        self.imperativeocl_VariableInitExp = imperativeocl_VariableInitExp
        
    @property
    def withResult(self) -> str:
        return self.__withResult

    @withResult.setter
    def withResult(self, withResult: str):
        self.__withResult = withResult

    @property
    def imperativeocl_VariableInitExp(self):
        return self.__imperativeocl_VariableInitExp

    @imperativeocl_VariableInitExp.setter
    def imperativeocl_VariableInitExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imperativeocl_VariableInitExp__imperativeocl_VariableInitExp", None)
        self.__imperativeocl_VariableInitExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imperativeocl_Variable"):
                opp_val = getattr(old_value, "imperativeocl_Variable", None)
                if opp_val == self:
                    setattr(old_value, "imperativeocl_Variable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imperativeocl_Variable"):
                opp_val = getattr(value, "imperativeocl_Variable", None)
                setattr(value, "imperativeocl_Variable", self)

class imperativeocl_InstantiationExp(ImperativeExpression):

    pass
class imperativeocl_RaiseExp(ImperativeExpression):

    pass
class imperativeocl_AssertExp(ImperativeExpression):

    def __init__(self, severity: str, imperativeocl_AssertExp: "imperativeocl_LogExp" = None, imperativeocl_AssertExp71: "imperativeocl_OclExpression" = None):
        self.severity = severity
        self.imperativeocl_AssertExp = imperativeocl_AssertExp
        self.imperativeocl_AssertExp71 = imperativeocl_AssertExp71
        
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
            if hasattr(old_value, "imperativeocl_LogExp69"):
                opp_val = getattr(old_value, "imperativeocl_LogExp69", None)
                if opp_val == self:
                    setattr(old_value, "imperativeocl_LogExp69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imperativeocl_LogExp69"):
                opp_val = getattr(value, "imperativeocl_LogExp69", None)
                setattr(value, "imperativeocl_LogExp69", self)

    @property
    def imperativeocl_AssertExp71(self):
        return self.__imperativeocl_AssertExp71

    @imperativeocl_AssertExp71.setter
    def imperativeocl_AssertExp71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imperativeocl_AssertExp__imperativeocl_AssertExp71", None)
        self.__imperativeocl_AssertExp71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imperativeocl_OclExpression72"):
                opp_val = getattr(old_value, "imperativeocl_OclExpression72", None)
                if opp_val == self:
                    setattr(old_value, "imperativeocl_OclExpression72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imperativeocl_OclExpression72"):
                opp_val = getattr(value, "imperativeocl_OclExpression72", None)
                setattr(value, "imperativeocl_OclExpression72", self)

class imperativeocl_WhileExp(ImperativeExpression):

    pass
class imperativeocl_ImperativeLoopExp(ImperativeExpression, LoopExp):

    pass
class imperativeocl_ContinueExp(ImperativeExpression):

    pass
class imperativeocl_ReturnExp(ImperativeExpression):

    pass
class imperativeocl_CatchExp(ImperativeExpression):

    pass
class imperativeocl_TryExp(ImperativeExpression):

    pass
class imperativeocl_AltExp(ImperativeExpression):

    pass
class imperativeocl_LogExp(OperationCallExp, ImperativeExpression):

    pass
class imperativeocl_AssignExp(ImperativeExpression):

    def __init__(self, isReset: str, imperativeocl_AssignExp2: "imperativeocl_OclExpression" = None, imperativeocl_AssignExp5: "imperativeocl_OclExpression" = None, imperativeocl_AssignExp: set["imperativeocl_OclExpression"] = None):
        self.isReset = isReset
        self.imperativeocl_AssignExp2 = imperativeocl_AssignExp2
        self.imperativeocl_AssignExp5 = imperativeocl_AssignExp5
        self.imperativeocl_AssignExp = imperativeocl_AssignExp if imperativeocl_AssignExp is not None else set()
        
    @property
    def isReset(self) -> str:
        return self.__isReset

    @isReset.setter
    def isReset(self, isReset: str):
        self.__isReset = isReset

    @property
    def imperativeocl_AssignExp(self):
        return self.__imperativeocl_AssignExp

    @imperativeocl_AssignExp.setter
    def imperativeocl_AssignExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imperativeocl_AssignExp__imperativeocl_AssignExp", None)
        self.__imperativeocl_AssignExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "imperativeocl_OclExpression"):
                    opp_val = getattr(item, "imperativeocl_OclExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "imperativeocl_OclExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "imperativeocl_OclExpression"):
                    opp_val = getattr(item, "imperativeocl_OclExpression", None)
                    
                    setattr(item, "imperativeocl_OclExpression", self)
                    

    @property
    def imperativeocl_AssignExp5(self):
        return self.__imperativeocl_AssignExp5

    @imperativeocl_AssignExp5.setter
    def imperativeocl_AssignExp5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imperativeocl_AssignExp__imperativeocl_AssignExp5", None)
        self.__imperativeocl_AssignExp5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imperativeocl_OclExpression6"):
                opp_val = getattr(old_value, "imperativeocl_OclExpression6", None)
                if opp_val == self:
                    setattr(old_value, "imperativeocl_OclExpression6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imperativeocl_OclExpression6"):
                opp_val = getattr(value, "imperativeocl_OclExpression6", None)
                setattr(value, "imperativeocl_OclExpression6", self)

    @property
    def imperativeocl_AssignExp2(self):
        return self.__imperativeocl_AssignExp2

    @imperativeocl_AssignExp2.setter
    def imperativeocl_AssignExp2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imperativeocl_AssignExp__imperativeocl_AssignExp2", None)
        self.__imperativeocl_AssignExp2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imperativeocl_OclExpression3"):
                opp_val = getattr(old_value, "imperativeocl_OclExpression3", None)
                if opp_val == self:
                    setattr(old_value, "imperativeocl_OclExpression3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imperativeocl_OclExpression3"):
                opp_val = getattr(value, "imperativeocl_OclExpression3", None)
                setattr(value, "imperativeocl_OclExpression3", self)
