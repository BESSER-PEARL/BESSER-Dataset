from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class imperativeoclcs_CollectionLiteralPartCS:

    pass
class imperativeoclcs_Type:

    pass
class imperativeoclcs_TypeCS:

    pass
class CallExpCS:

    pass
class ImperativeLoopExpCS:

    pass
class imperativeoclcs_ForExpCS(ImperativeLoopExpCS):

    pass
class imperativeoclcs_ImperativeIterateExpCS(ImperativeLoopExpCS):

    pass
class imperativeoclcs_VariableCS:

    pass
class ExpressionBlockCS:

    pass
class imperativeoclcs_TryExpCS(ExpressionBlockCS):

    pass
class imperativeoclcs_DoExpCS(ExpressionBlockCS):

    pass
class imperativeoclcs_WhileExpCS(ExpressionBlockCS):

    pass
class imperativeoclcs_ComputeExpCS(ExpressionBlockCS):

    pass
class imperativeoclcs_TypedRefCS:

    pass
class TypedRefCS:

    pass
class imperativeoclcs_ListTypeCS(TypedRefCS):

    pass
class imperativeoclcs_DictTypeCS(TypedRefCS):

    pass
class imperativeoclcs_PrimitiveLiteralExpCS:

    pass
class ElementCS:

    pass
class imperativeoclcs_ExceptCS(ElementCS):

    pass
class imperativeoclcs_DictLiteralPartCS(ElementCS):

    pass
class ExpCS:

    pass
class imperativeoclcs_ReturnExpCS(ExpCS):

    pass
class imperativeoclcs_ExpressionBlockCS(ExpCS):

    pass
class imperativeoclcs_ListLiteralExpCS(ExpCS):

    pass
class imperativeoclcs_StatementCS(ExpCS):

    pass
class imperativeoclcs_DictLiteralExpCS(ExpCS):

    pass
class imperativeoclcs_LogExpCS(CallExpCS):

    pass
class imperativeoclcs_ExpCS:

    pass
class StatementCS:

    pass
class imperativeoclcs_ImperativeLoopExpCS(CallExpCS, StatementCS):

    pass
class imperativeoclcs_InstantiationExpCS(StatementCS):

    pass
class imperativeoclcs_RaiseExpCS(StatementCS):

    pass
class imperativeoclcs_VariableInitializationCS(StatementCS):

    def __init__(self, simpleNameCS: str, withResult: bool, imperativeoclcs_VariableInitializationCS: "imperativeoclcs_ExpCS" = None, imperativeoclcs_VariableInitializationCS64: "imperativeoclcs_TypeCS" = None):
        self.simpleNameCS = simpleNameCS
        self.withResult = withResult
        self.imperativeoclcs_VariableInitializationCS = imperativeoclcs_VariableInitializationCS
        self.imperativeoclcs_VariableInitializationCS64 = imperativeoclcs_VariableInitializationCS64
        
    @property
    def withResult(self) -> bool:
        return self.__withResult

    @withResult.setter
    def withResult(self, withResult: bool):
        self.__withResult = withResult

    @property
    def simpleNameCS(self) -> str:
        return self.__simpleNameCS

    @simpleNameCS.setter
    def simpleNameCS(self, simpleNameCS: str):
        self.__simpleNameCS = simpleNameCS

    @property
    def imperativeoclcs_VariableInitializationCS64(self):
        return self.__imperativeoclcs_VariableInitializationCS64

    @imperativeoclcs_VariableInitializationCS64.setter
    def imperativeoclcs_VariableInitializationCS64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imperativeoclcs_VariableInitializationCS__imperativeoclcs_VariableInitializationCS64", None)
        self.__imperativeoclcs_VariableInitializationCS64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imperativeoclcs_TypeCS65"):
                opp_val = getattr(old_value, "imperativeoclcs_TypeCS65", None)
                if opp_val == self:
                    setattr(old_value, "imperativeoclcs_TypeCS65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imperativeoclcs_TypeCS65"):
                opp_val = getattr(value, "imperativeoclcs_TypeCS65", None)
                setattr(value, "imperativeoclcs_TypeCS65", self)

    @property
    def imperativeoclcs_VariableInitializationCS(self):
        return self.__imperativeoclcs_VariableInitializationCS

    @imperativeoclcs_VariableInitializationCS.setter
    def imperativeoclcs_VariableInitializationCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imperativeoclcs_VariableInitializationCS__imperativeoclcs_VariableInitializationCS", None)
        self.__imperativeoclcs_VariableInitializationCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imperativeoclcs_ExpCS62"):
                opp_val = getattr(old_value, "imperativeoclcs_ExpCS62", None)
                if opp_val == self:
                    setattr(old_value, "imperativeoclcs_ExpCS62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imperativeoclcs_ExpCS62"):
                opp_val = getattr(value, "imperativeoclcs_ExpCS62", None)
                setattr(value, "imperativeoclcs_ExpCS62", self)

class imperativeoclcs_SwitchAltCS(StatementCS):

    def __init__(self, keyword: str, imperativeoclcs_SwitchAltCS: "imperativeoclcs_ExpCS" = None, imperativeoclcs_SwitchAltCS52: "imperativeoclcs_ExpCS" = None, imperativeoclcs_SwitchAltCS55: "imperativeoclcs_SwitchExpCS" = None):
        self.keyword = keyword
        self.imperativeoclcs_SwitchAltCS = imperativeoclcs_SwitchAltCS
        self.imperativeoclcs_SwitchAltCS52 = imperativeoclcs_SwitchAltCS52
        self.imperativeoclcs_SwitchAltCS55 = imperativeoclcs_SwitchAltCS55
        
    @property
    def keyword(self) -> str:
        return self.__keyword

    @keyword.setter
    def keyword(self, keyword: str):
        self.__keyword = keyword

    @property
    def imperativeoclcs_SwitchAltCS52(self):
        return self.__imperativeoclcs_SwitchAltCS52

    @imperativeoclcs_SwitchAltCS52.setter
    def imperativeoclcs_SwitchAltCS52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imperativeoclcs_SwitchAltCS__imperativeoclcs_SwitchAltCS52", None)
        self.__imperativeoclcs_SwitchAltCS52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imperativeoclcs_ExpCS53"):
                opp_val = getattr(old_value, "imperativeoclcs_ExpCS53", None)
                if opp_val == self:
                    setattr(old_value, "imperativeoclcs_ExpCS53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imperativeoclcs_ExpCS53"):
                opp_val = getattr(value, "imperativeoclcs_ExpCS53", None)
                setattr(value, "imperativeoclcs_ExpCS53", self)

    @property
    def imperativeoclcs_SwitchAltCS(self):
        return self.__imperativeoclcs_SwitchAltCS

    @imperativeoclcs_SwitchAltCS.setter
    def imperativeoclcs_SwitchAltCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imperativeoclcs_SwitchAltCS__imperativeoclcs_SwitchAltCS", None)
        self.__imperativeoclcs_SwitchAltCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imperativeoclcs_ExpCS50"):
                opp_val = getattr(old_value, "imperativeoclcs_ExpCS50", None)
                if opp_val == self:
                    setattr(old_value, "imperativeoclcs_ExpCS50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imperativeoclcs_ExpCS50"):
                opp_val = getattr(value, "imperativeoclcs_ExpCS50", None)
                setattr(value, "imperativeoclcs_ExpCS50", self)

    @property
    def imperativeoclcs_SwitchAltCS55(self):
        return self.__imperativeoclcs_SwitchAltCS55

    @imperativeoclcs_SwitchAltCS55.setter
    def imperativeoclcs_SwitchAltCS55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imperativeoclcs_SwitchAltCS__imperativeoclcs_SwitchAltCS55", None)
        self.__imperativeoclcs_SwitchAltCS55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imperativeoclcs_SwitchExpCS"):
                opp_val = getattr(old_value, "imperativeoclcs_SwitchExpCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imperativeoclcs_SwitchExpCS"):
                opp_val = getattr(value, "imperativeoclcs_SwitchExpCS", None)
                if opp_val is None:
                    setattr(value, "imperativeoclcs_SwitchExpCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class imperativeoclcs_ExpressionStatementCS(StatementCS):

    pass
class imperativeoclcs_BlockExpCS(StatementCS):

    pass
class imperativeoclcs_SwitchExpCS(StatementCS):

    pass
class imperativeoclcs_QuitExpCS(StatementCS):

    def __init__(self, keyword: str, imperativeoclcs_QuitExpCS: "imperativeoclcs_ExpCS" = None):
        self.keyword = keyword
        self.imperativeoclcs_QuitExpCS = imperativeoclcs_QuitExpCS
        
    @property
    def keyword(self) -> str:
        return self.__keyword

    @keyword.setter
    def keyword(self, keyword: str):
        self.__keyword = keyword

    @property
    def imperativeoclcs_QuitExpCS(self):
        return self.__imperativeoclcs_QuitExpCS

    @imperativeoclcs_QuitExpCS.setter
    def imperativeoclcs_QuitExpCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imperativeoclcs_QuitExpCS__imperativeoclcs_QuitExpCS", None)
        self.__imperativeoclcs_QuitExpCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imperativeoclcs_ExpCS46"):
                opp_val = getattr(old_value, "imperativeoclcs_ExpCS46", None)
                if opp_val == self:
                    setattr(old_value, "imperativeoclcs_ExpCS46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imperativeoclcs_ExpCS46"):
                opp_val = getattr(value, "imperativeoclcs_ExpCS46", None)
                setattr(value, "imperativeoclcs_ExpCS46", self)

class imperativeoclcs_AssertExpCS(StatementCS):

    def __init__(self, severity: str, imperativeoclcs_AssertExpCS: "imperativeoclcs_ExpCS" = None, imperativeoclcs_AssertExpCS2: "imperativeoclcs_LogExpCS" = None):
        self.severity = severity
        self.imperativeoclcs_AssertExpCS = imperativeoclcs_AssertExpCS
        self.imperativeoclcs_AssertExpCS2 = imperativeoclcs_AssertExpCS2
        
    @property
    def severity(self) -> str:
        return self.__severity

    @severity.setter
    def severity(self, severity: str):
        self.__severity = severity

    @property
    def imperativeoclcs_AssertExpCS(self):
        return self.__imperativeoclcs_AssertExpCS

    @imperativeoclcs_AssertExpCS.setter
    def imperativeoclcs_AssertExpCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imperativeoclcs_AssertExpCS__imperativeoclcs_AssertExpCS", None)
        self.__imperativeoclcs_AssertExpCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imperativeoclcs_ExpCS"):
                opp_val = getattr(old_value, "imperativeoclcs_ExpCS", None)
                if opp_val == self:
                    setattr(old_value, "imperativeoclcs_ExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imperativeoclcs_ExpCS"):
                opp_val = getattr(value, "imperativeoclcs_ExpCS", None)
                setattr(value, "imperativeoclcs_ExpCS", self)

    @property
    def imperativeoclcs_AssertExpCS2(self):
        return self.__imperativeoclcs_AssertExpCS2

    @imperativeoclcs_AssertExpCS2.setter
    def imperativeoclcs_AssertExpCS2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imperativeoclcs_AssertExpCS__imperativeoclcs_AssertExpCS2", None)
        self.__imperativeoclcs_AssertExpCS2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imperativeoclcs_LogExpCS"):
                opp_val = getattr(old_value, "imperativeoclcs_LogExpCS", None)
                if opp_val == self:
                    setattr(old_value, "imperativeoclcs_LogExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imperativeoclcs_LogExpCS"):
                opp_val = getattr(value, "imperativeoclcs_LogExpCS", None)
                setattr(value, "imperativeoclcs_LogExpCS", self)

class imperativeoclcs_AssignStatementCS(StatementCS):

    def __init__(self, incremental: bool, imperativeoclcs_AssignStatementCS: "imperativeoclcs_ExpCS" = None, imperativeoclcs_AssignStatementCS6: "imperativeoclcs_ExpCS" = None):
        self.incremental = incremental
        self.imperativeoclcs_AssignStatementCS = imperativeoclcs_AssignStatementCS
        self.imperativeoclcs_AssignStatementCS6 = imperativeoclcs_AssignStatementCS6
        
    @property
    def incremental(self) -> bool:
        return self.__incremental

    @incremental.setter
    def incremental(self, incremental: bool):
        self.__incremental = incremental

    @property
    def imperativeoclcs_AssignStatementCS(self):
        return self.__imperativeoclcs_AssignStatementCS

    @imperativeoclcs_AssignStatementCS.setter
    def imperativeoclcs_AssignStatementCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imperativeoclcs_AssignStatementCS__imperativeoclcs_AssignStatementCS", None)
        self.__imperativeoclcs_AssignStatementCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imperativeoclcs_ExpCS4"):
                opp_val = getattr(old_value, "imperativeoclcs_ExpCS4", None)
                if opp_val == self:
                    setattr(old_value, "imperativeoclcs_ExpCS4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imperativeoclcs_ExpCS4"):
                opp_val = getattr(value, "imperativeoclcs_ExpCS4", None)
                setattr(value, "imperativeoclcs_ExpCS4", self)

    @property
    def imperativeoclcs_AssignStatementCS6(self):
        return self.__imperativeoclcs_AssignStatementCS6

    @imperativeoclcs_AssignStatementCS6.setter
    def imperativeoclcs_AssignStatementCS6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imperativeoclcs_AssignStatementCS__imperativeoclcs_AssignStatementCS6", None)
        self.__imperativeoclcs_AssignStatementCS6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imperativeoclcs_ExpCS7"):
                opp_val = getattr(old_value, "imperativeoclcs_ExpCS7", None)
                if opp_val == self:
                    setattr(old_value, "imperativeoclcs_ExpCS7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imperativeoclcs_ExpCS7"):
                opp_val = getattr(value, "imperativeoclcs_ExpCS7", None)
                setattr(value, "imperativeoclcs_ExpCS7", self)
