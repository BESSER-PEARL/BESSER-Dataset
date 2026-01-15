from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class NavigationPathCS:

    pass
class miniOCL_NavigationPathElementCS(NavigationPathCS):

    pass
class miniOCL_NavigationPathVariableCS(NavigationPathCS):

    def __init__(self, varName: str):
        self.varName = varName
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

class miniOCL_NavigationPathCS:

    pass
class miniOCL_NavigationPathNameCS:

    pass
class BooleanLiteralExpCS:

    pass
class miniOCL_BooleanExpCS(BooleanLiteralExpCS):

    def __init__(self, boolSymbol: bool):
        self.boolSymbol = boolSymbol
        
    @property
    def boolSymbol(self) -> bool:
        return self.__boolSymbol

    @boolSymbol.setter
    def boolSymbol(self, boolSymbol: bool):
        self.__boolSymbol = boolSymbol

class miniOCL_EStructuralFeature:

    pass
class PathCS:

    pass
class miniOCL_PathElementCS(PathCS):

    pass
class miniOCL_PathVariableCS(PathCS):

    def __init__(self, varName: str):
        self.varName = varName
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

class miniOCL_PathCS:

    pass
class LiteralExpCS:

    pass
class miniOCL_BooleanLiteralExpCS(LiteralExpCS):

    pass
class miniOCL_StringLiteralExpCS(LiteralExpCS):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
    @property
    def stringSymbol(self) -> str:
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol

class miniOCL_IntLiteralExpCS(LiteralExpCS):

    def __init__(self, intSymbol: int):
        self.intSymbol = intSymbol
        
    @property
    def intSymbol(self) -> int:
        return self.__intSymbol

    @intSymbol.setter
    def intSymbol(self, intSymbol: int):
        self.__intSymbol = intSymbol

class miniOCL_AccVarCS:

    def __init__(self, accVarName: str, miniOCL_AccVarCS: "miniOCL_IterateExpCS" = None, miniOCL_AccVarCS60: "miniOCL_PathNameCS" = None, miniOCL_AccVarCS63: "miniOCL_ExpCS" = None, miniOCL_AccVarCS72: "miniOCL_ExistsExpCS" = None, miniOCL_AccVarCS85: "miniOCL_ForAllExpCS" = None):
        self.accVarName = accVarName
        self.miniOCL_AccVarCS = miniOCL_AccVarCS
        self.miniOCL_AccVarCS60 = miniOCL_AccVarCS60
        self.miniOCL_AccVarCS63 = miniOCL_AccVarCS63
        self.miniOCL_AccVarCS72 = miniOCL_AccVarCS72
        self.miniOCL_AccVarCS85 = miniOCL_AccVarCS85
        
    @property
    def accVarName(self) -> str:
        return self.__accVarName

    @accVarName.setter
    def accVarName(self, accVarName: str):
        self.__accVarName = accVarName

    @property
    def miniOCL_AccVarCS(self):
        return self.__miniOCL_AccVarCS

    @miniOCL_AccVarCS.setter
    def miniOCL_AccVarCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniOCL_AccVarCS__miniOCL_AccVarCS", None)
        self.__miniOCL_AccVarCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniOCL_IterateExpCS"):
                opp_val = getattr(old_value, "miniOCL_IterateExpCS", None)
                if opp_val == self:
                    setattr(old_value, "miniOCL_IterateExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniOCL_IterateExpCS"):
                opp_val = getattr(value, "miniOCL_IterateExpCS", None)
                setattr(value, "miniOCL_IterateExpCS", self)

    @property
    def miniOCL_AccVarCS63(self):
        return self.__miniOCL_AccVarCS63

    @miniOCL_AccVarCS63.setter
    def miniOCL_AccVarCS63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniOCL_AccVarCS__miniOCL_AccVarCS63", None)
        self.__miniOCL_AccVarCS63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniOCL_ExpCS64"):
                opp_val = getattr(old_value, "miniOCL_ExpCS64", None)
                if opp_val == self:
                    setattr(old_value, "miniOCL_ExpCS64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniOCL_ExpCS64"):
                opp_val = getattr(value, "miniOCL_ExpCS64", None)
                setattr(value, "miniOCL_ExpCS64", self)

    @property
    def miniOCL_AccVarCS85(self):
        return self.__miniOCL_AccVarCS85

    @miniOCL_AccVarCS85.setter
    def miniOCL_AccVarCS85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniOCL_AccVarCS__miniOCL_AccVarCS85", None)
        self.__miniOCL_AccVarCS85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniOCL_ForAllExpCS"):
                opp_val = getattr(old_value, "miniOCL_ForAllExpCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniOCL_ForAllExpCS"):
                opp_val = getattr(value, "miniOCL_ForAllExpCS", None)
                if opp_val is None:
                    setattr(value, "miniOCL_ForAllExpCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def miniOCL_AccVarCS60(self):
        return self.__miniOCL_AccVarCS60

    @miniOCL_AccVarCS60.setter
    def miniOCL_AccVarCS60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniOCL_AccVarCS__miniOCL_AccVarCS60", None)
        self.__miniOCL_AccVarCS60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniOCL_PathNameCS61"):
                opp_val = getattr(old_value, "miniOCL_PathNameCS61", None)
                if opp_val == self:
                    setattr(old_value, "miniOCL_PathNameCS61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniOCL_PathNameCS61"):
                opp_val = getattr(value, "miniOCL_PathNameCS61", None)
                setattr(value, "miniOCL_PathNameCS61", self)

    @property
    def miniOCL_AccVarCS72(self):
        return self.__miniOCL_AccVarCS72

    @miniOCL_AccVarCS72.setter
    def miniOCL_AccVarCS72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniOCL_AccVarCS__miniOCL_AccVarCS72", None)
        self.__miniOCL_AccVarCS72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniOCL_ExistsExpCS"):
                opp_val = getattr(old_value, "miniOCL_ExistsExpCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniOCL_ExistsExpCS"):
                opp_val = getattr(value, "miniOCL_ExistsExpCS", None)
                if opp_val is None:
                    setattr(value, "miniOCL_ExistsExpCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class LoopExpCS:

    pass
class miniOCL_IterateExpCS(LoopExpCS):

    pass
class miniOCL_ForAllExpCS(LoopExpCS):

    pass
class miniOCL_ExistsExpCS(LoopExpCS):

    pass
class miniOCL_CollectExpCS(LoopExpCS):

    pass
class miniOCL_IteratorVarCS:

    def __init__(self, itName: str, miniOCL_IteratorVarCS: "miniOCL_LoopExpCS" = None, miniOCL_IteratorVarCS56: "miniOCL_PathNameCS" = None):
        self.itName = itName
        self.miniOCL_IteratorVarCS = miniOCL_IteratorVarCS
        self.miniOCL_IteratorVarCS56 = miniOCL_IteratorVarCS56
        
    @property
    def itName(self) -> str:
        return self.__itName

    @itName.setter
    def itName(self, itName: str):
        self.__itName = itName

    @property
    def miniOCL_IteratorVarCS(self):
        return self.__miniOCL_IteratorVarCS

    @miniOCL_IteratorVarCS.setter
    def miniOCL_IteratorVarCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniOCL_IteratorVarCS__miniOCL_IteratorVarCS", None)
        self.__miniOCL_IteratorVarCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniOCL_LoopExpCS"):
                opp_val = getattr(old_value, "miniOCL_LoopExpCS", None)
                if opp_val == self:
                    setattr(old_value, "miniOCL_LoopExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniOCL_LoopExpCS"):
                opp_val = getattr(value, "miniOCL_LoopExpCS", None)
                setattr(value, "miniOCL_LoopExpCS", self)

    @property
    def miniOCL_IteratorVarCS56(self):
        return self.__miniOCL_IteratorVarCS56

    @miniOCL_IteratorVarCS56.setter
    def miniOCL_IteratorVarCS56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniOCL_IteratorVarCS__miniOCL_IteratorVarCS56", None)
        self.__miniOCL_IteratorVarCS56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniOCL_PathNameCS57"):
                opp_val = getattr(old_value, "miniOCL_PathNameCS57", None)
                if opp_val == self:
                    setattr(old_value, "miniOCL_PathNameCS57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniOCL_PathNameCS57"):
                opp_val = getattr(value, "miniOCL_PathNameCS57", None)
                setattr(value, "miniOCL_PathNameCS57", self)

class miniOCL_RoundedBracketClauseCS:

    pass
class NavigationExpCS:

    pass
class miniOCL_NavigationNameExpCS(NavigationExpCS):

    pass
class miniOCL_LoopExpCS(NavigationExpCS):

    def __init__(self, logicOp: str, miniOCL_LoopExpCS: "miniOCL_IteratorVarCS" = None, miniOCL_LoopExpCS53: set["miniOCL_ExpCS"] = None):
        self.logicOp = logicOp
        self.miniOCL_LoopExpCS = miniOCL_LoopExpCS
        self.miniOCL_LoopExpCS53 = miniOCL_LoopExpCS53 if miniOCL_LoopExpCS53 is not None else set()
        
    @property
    def logicOp(self) -> str:
        return self.__logicOp

    @logicOp.setter
    def logicOp(self, logicOp: str):
        self.__logicOp = logicOp

    @property
    def miniOCL_LoopExpCS(self):
        return self.__miniOCL_LoopExpCS

    @miniOCL_LoopExpCS.setter
    def miniOCL_LoopExpCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniOCL_LoopExpCS__miniOCL_LoopExpCS", None)
        self.__miniOCL_LoopExpCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniOCL_IteratorVarCS"):
                opp_val = getattr(old_value, "miniOCL_IteratorVarCS", None)
                if opp_val == self:
                    setattr(old_value, "miniOCL_IteratorVarCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniOCL_IteratorVarCS"):
                opp_val = getattr(value, "miniOCL_IteratorVarCS", None)
                setattr(value, "miniOCL_IteratorVarCS", self)

    @property
    def miniOCL_LoopExpCS53(self):
        return self.__miniOCL_LoopExpCS53

    @miniOCL_LoopExpCS53.setter
    def miniOCL_LoopExpCS53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniOCL_LoopExpCS__miniOCL_LoopExpCS53", None)
        self.__miniOCL_LoopExpCS53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "miniOCL_ExpCS54"):
                    opp_val = getattr(item, "miniOCL_ExpCS54", None)
                    
                    if opp_val == self:
                        setattr(item, "miniOCL_ExpCS54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "miniOCL_ExpCS54"):
                    opp_val = getattr(item, "miniOCL_ExpCS54", None)
                    
                    setattr(item, "miniOCL_ExpCS54", self)
                    

class miniOCL_NameExpCS(NavigationExpCS):

    pass
class PrimaryExpCS:

    pass
class miniOCL_LiteralExpCS(PrimaryExpCS):

    pass
class CallExpCS:

    pass
class miniOCL_PrimaryExpCS(CallExpCS):

    pass
class miniOCL_NavigationExpCS(PrimaryExpCS):

    pass
class LogicExpCS:

    pass
class miniOCL_CallExpCS(LogicExpCS):

    pass
class ExpCS:

    pass
class miniOCL_LogicExpCS(ExpCS):

    def __init__(self, op: str, miniOCL_LogicExpCS: "miniOCL_LogicExpCS" = None, miniOCL_LogicExpCS35: "miniOCL_LogicExpCS" = None, miniOCL_LogicExpCS38: "miniOCL_CallExpCS" = None):
        self.op = op
        self.miniOCL_LogicExpCS = miniOCL_LogicExpCS
        self.miniOCL_LogicExpCS35 = miniOCL_LogicExpCS35
        self.miniOCL_LogicExpCS38 = miniOCL_LogicExpCS38
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def miniOCL_LogicExpCS(self):
        return self.__miniOCL_LogicExpCS

    @miniOCL_LogicExpCS.setter
    def miniOCL_LogicExpCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniOCL_LogicExpCS__miniOCL_LogicExpCS", None)
        self.__miniOCL_LogicExpCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniOCL_LogicExpCS35"):
                opp_val = getattr(old_value, "miniOCL_LogicExpCS35", None)
                if opp_val == self:
                    setattr(old_value, "miniOCL_LogicExpCS35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniOCL_LogicExpCS35"):
                opp_val = getattr(value, "miniOCL_LogicExpCS35", None)
                setattr(value, "miniOCL_LogicExpCS35", self)

    @property
    def miniOCL_LogicExpCS38(self):
        return self.__miniOCL_LogicExpCS38

    @miniOCL_LogicExpCS38.setter
    def miniOCL_LogicExpCS38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniOCL_LogicExpCS__miniOCL_LogicExpCS38", None)
        self.__miniOCL_LogicExpCS38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniOCL_CallExpCS"):
                opp_val = getattr(old_value, "miniOCL_CallExpCS", None)
                if opp_val == self:
                    setattr(old_value, "miniOCL_CallExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniOCL_CallExpCS"):
                opp_val = getattr(value, "miniOCL_CallExpCS", None)
                setattr(value, "miniOCL_CallExpCS", self)

    @property
    def miniOCL_LogicExpCS35(self):
        return self.__miniOCL_LogicExpCS35

    @miniOCL_LogicExpCS35.setter
    def miniOCL_LogicExpCS35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniOCL_LogicExpCS__miniOCL_LogicExpCS35", None)
        self.__miniOCL_LogicExpCS35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniOCL_LogicExpCS"):
                opp_val = getattr(old_value, "miniOCL_LogicExpCS", None)
                if opp_val == self:
                    setattr(old_value, "miniOCL_LogicExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniOCL_LogicExpCS"):
                opp_val = getattr(value, "miniOCL_LogicExpCS", None)
                setattr(value, "miniOCL_LogicExpCS", self)

class miniOCL_InvariantCS:

    pass
class miniOCL_ExpCS:

    pass
class miniOCL_ParameterCS:

    def __init__(self, name: str, miniOCL_ParameterCS: "miniOCL_OperationCS" = None, miniOCL_ParameterCS25: "miniOCL_PathNameCS" = None):
        self.name = name
        self.miniOCL_ParameterCS = miniOCL_ParameterCS
        self.miniOCL_ParameterCS25 = miniOCL_ParameterCS25
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def miniOCL_ParameterCS(self):
        return self.__miniOCL_ParameterCS

    @miniOCL_ParameterCS.setter
    def miniOCL_ParameterCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniOCL_ParameterCS__miniOCL_ParameterCS", None)
        self.__miniOCL_ParameterCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniOCL_OperationCS18"):
                opp_val = getattr(old_value, "miniOCL_OperationCS18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniOCL_OperationCS18"):
                opp_val = getattr(value, "miniOCL_OperationCS18", None)
                if opp_val is None:
                    setattr(value, "miniOCL_OperationCS18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def miniOCL_ParameterCS25(self):
        return self.__miniOCL_ParameterCS25

    @miniOCL_ParameterCS25.setter
    def miniOCL_ParameterCS25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniOCL_ParameterCS__miniOCL_ParameterCS25", None)
        self.__miniOCL_ParameterCS25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniOCL_PathNameCS26"):
                opp_val = getattr(old_value, "miniOCL_PathNameCS26", None)
                if opp_val == self:
                    setattr(old_value, "miniOCL_PathNameCS26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniOCL_PathNameCS26"):
                opp_val = getattr(value, "miniOCL_PathNameCS26", None)
                setattr(value, "miniOCL_PathNameCS26", self)

class miniOCL_OperationCS:

    def __init__(self, name: str, miniOCL_OperationCS: "miniOCL_ClassCS" = None, miniOCL_OperationCS18: set["miniOCL_ParameterCS"] = None, miniOCL_OperationCS20: "miniOCL_PathNameCS" = None, miniOCL_OperationCS23: "miniOCL_ExpCS" = None):
        self.name = name
        self.miniOCL_OperationCS = miniOCL_OperationCS
        self.miniOCL_OperationCS18 = miniOCL_OperationCS18 if miniOCL_OperationCS18 is not None else set()
        self.miniOCL_OperationCS20 = miniOCL_OperationCS20
        self.miniOCL_OperationCS23 = miniOCL_OperationCS23
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def miniOCL_OperationCS(self):
        return self.__miniOCL_OperationCS

    @miniOCL_OperationCS.setter
    def miniOCL_OperationCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniOCL_OperationCS__miniOCL_OperationCS", None)
        self.__miniOCL_OperationCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniOCL_ClassCS13"):
                opp_val = getattr(old_value, "miniOCL_ClassCS13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniOCL_ClassCS13"):
                opp_val = getattr(value, "miniOCL_ClassCS13", None)
                if opp_val is None:
                    setattr(value, "miniOCL_ClassCS13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def miniOCL_OperationCS18(self):
        return self.__miniOCL_OperationCS18

    @miniOCL_OperationCS18.setter
    def miniOCL_OperationCS18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniOCL_OperationCS__miniOCL_OperationCS18", None)
        self.__miniOCL_OperationCS18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "miniOCL_ParameterCS"):
                    opp_val = getattr(item, "miniOCL_ParameterCS", None)
                    
                    if opp_val == self:
                        setattr(item, "miniOCL_ParameterCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "miniOCL_ParameterCS"):
                    opp_val = getattr(item, "miniOCL_ParameterCS", None)
                    
                    setattr(item, "miniOCL_ParameterCS", self)
                    

    @property
    def miniOCL_OperationCS23(self):
        return self.__miniOCL_OperationCS23

    @miniOCL_OperationCS23.setter
    def miniOCL_OperationCS23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniOCL_OperationCS__miniOCL_OperationCS23", None)
        self.__miniOCL_OperationCS23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniOCL_ExpCS"):
                opp_val = getattr(old_value, "miniOCL_ExpCS", None)
                if opp_val == self:
                    setattr(old_value, "miniOCL_ExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniOCL_ExpCS"):
                opp_val = getattr(value, "miniOCL_ExpCS", None)
                setattr(value, "miniOCL_ExpCS", self)

    @property
    def miniOCL_OperationCS20(self):
        return self.__miniOCL_OperationCS20

    @miniOCL_OperationCS20.setter
    def miniOCL_OperationCS20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniOCL_OperationCS__miniOCL_OperationCS20", None)
        self.__miniOCL_OperationCS20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniOCL_PathNameCS21"):
                opp_val = getattr(old_value, "miniOCL_PathNameCS21", None)
                if opp_val == self:
                    setattr(old_value, "miniOCL_PathNameCS21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniOCL_PathNameCS21"):
                opp_val = getattr(value, "miniOCL_PathNameCS21", None)
                setattr(value, "miniOCL_PathNameCS21", self)

class miniOCL_PropertyCS:

    def __init__(self, name: str, miniOCL_PropertyCS: "miniOCL_ClassCS" = None, miniOCL_PropertyCS15: "miniOCL_PathNameCS" = None):
        self.name = name
        self.miniOCL_PropertyCS = miniOCL_PropertyCS
        self.miniOCL_PropertyCS15 = miniOCL_PropertyCS15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def miniOCL_PropertyCS15(self):
        return self.__miniOCL_PropertyCS15

    @miniOCL_PropertyCS15.setter
    def miniOCL_PropertyCS15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniOCL_PropertyCS__miniOCL_PropertyCS15", None)
        self.__miniOCL_PropertyCS15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniOCL_PathNameCS16"):
                opp_val = getattr(old_value, "miniOCL_PathNameCS16", None)
                if opp_val == self:
                    setattr(old_value, "miniOCL_PathNameCS16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniOCL_PathNameCS16"):
                opp_val = getattr(value, "miniOCL_PathNameCS16", None)
                setattr(value, "miniOCL_PathNameCS16", self)

    @property
    def miniOCL_PropertyCS(self):
        return self.__miniOCL_PropertyCS

    @miniOCL_PropertyCS.setter
    def miniOCL_PropertyCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniOCL_PropertyCS__miniOCL_PropertyCS", None)
        self.__miniOCL_PropertyCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniOCL_ClassCS11"):
                opp_val = getattr(old_value, "miniOCL_ClassCS11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniOCL_ClassCS11"):
                opp_val = getattr(value, "miniOCL_ClassCS11", None)
                if opp_val is None:
                    setattr(value, "miniOCL_ClassCS11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class miniOCL_PathNameCS:

    pass
class miniOCL_ClassCS:

    def __init__(self, name: str, miniOCL_ClassCS: "miniOCL_PackageCS" = None, miniOCL_ClassCS9: "miniOCL_PathNameCS" = None, miniOCL_ClassCS11: set["miniOCL_PropertyCS"] = None, miniOCL_ClassCS13: set["miniOCL_OperationCS"] = None):
        self.name = name
        self.miniOCL_ClassCS = miniOCL_ClassCS
        self.miniOCL_ClassCS9 = miniOCL_ClassCS9
        self.miniOCL_ClassCS11 = miniOCL_ClassCS11 if miniOCL_ClassCS11 is not None else set()
        self.miniOCL_ClassCS13 = miniOCL_ClassCS13 if miniOCL_ClassCS13 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def miniOCL_ClassCS13(self):
        return self.__miniOCL_ClassCS13

    @miniOCL_ClassCS13.setter
    def miniOCL_ClassCS13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniOCL_ClassCS__miniOCL_ClassCS13", None)
        self.__miniOCL_ClassCS13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "miniOCL_OperationCS"):
                    opp_val = getattr(item, "miniOCL_OperationCS", None)
                    
                    if opp_val == self:
                        setattr(item, "miniOCL_OperationCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "miniOCL_OperationCS"):
                    opp_val = getattr(item, "miniOCL_OperationCS", None)
                    
                    setattr(item, "miniOCL_OperationCS", self)
                    

    @property
    def miniOCL_ClassCS(self):
        return self.__miniOCL_ClassCS

    @miniOCL_ClassCS.setter
    def miniOCL_ClassCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniOCL_ClassCS__miniOCL_ClassCS", None)
        self.__miniOCL_ClassCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniOCL_PackageCS7"):
                opp_val = getattr(old_value, "miniOCL_PackageCS7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniOCL_PackageCS7"):
                opp_val = getattr(value, "miniOCL_PackageCS7", None)
                if opp_val is None:
                    setattr(value, "miniOCL_PackageCS7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def miniOCL_ClassCS11(self):
        return self.__miniOCL_ClassCS11

    @miniOCL_ClassCS11.setter
    def miniOCL_ClassCS11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniOCL_ClassCS__miniOCL_ClassCS11", None)
        self.__miniOCL_ClassCS11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "miniOCL_PropertyCS"):
                    opp_val = getattr(item, "miniOCL_PropertyCS", None)
                    
                    if opp_val == self:
                        setattr(item, "miniOCL_PropertyCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "miniOCL_PropertyCS"):
                    opp_val = getattr(item, "miniOCL_PropertyCS", None)
                    
                    setattr(item, "miniOCL_PropertyCS", self)
                    

    @property
    def miniOCL_ClassCS9(self):
        return self.__miniOCL_ClassCS9

    @miniOCL_ClassCS9.setter
    def miniOCL_ClassCS9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniOCL_ClassCS__miniOCL_ClassCS9", None)
        self.__miniOCL_ClassCS9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniOCL_PathNameCS"):
                opp_val = getattr(old_value, "miniOCL_PathNameCS", None)
                if opp_val == self:
                    setattr(old_value, "miniOCL_PathNameCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniOCL_PathNameCS"):
                opp_val = getattr(value, "miniOCL_PathNameCS", None)
                setattr(value, "miniOCL_PathNameCS", self)

class miniOCL_ConstraintCS:

    pass
class miniOCL_PackageCS:

    def __init__(self, name: str, miniOCL_PackageCS: "miniOCL_RootCS" = None, miniOCL_PackageCS5: "miniOCL_PackageCS" = None, miniOCL_PackageCS3: set["miniOCL_PackageCS"] = None, miniOCL_PackageCS7: set["miniOCL_ClassCS"] = None):
        self.name = name
        self.miniOCL_PackageCS = miniOCL_PackageCS
        self.miniOCL_PackageCS5 = miniOCL_PackageCS5
        self.miniOCL_PackageCS3 = miniOCL_PackageCS3 if miniOCL_PackageCS3 is not None else set()
        self.miniOCL_PackageCS7 = miniOCL_PackageCS7 if miniOCL_PackageCS7 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def miniOCL_PackageCS5(self):
        return self.__miniOCL_PackageCS5

    @miniOCL_PackageCS5.setter
    def miniOCL_PackageCS5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniOCL_PackageCS__miniOCL_PackageCS5", None)
        self.__miniOCL_PackageCS5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniOCL_PackageCS3"):
                opp_val = getattr(old_value, "miniOCL_PackageCS3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniOCL_PackageCS3"):
                opp_val = getattr(value, "miniOCL_PackageCS3", None)
                if opp_val is None:
                    setattr(value, "miniOCL_PackageCS3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def miniOCL_PackageCS(self):
        return self.__miniOCL_PackageCS

    @miniOCL_PackageCS.setter
    def miniOCL_PackageCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniOCL_PackageCS__miniOCL_PackageCS", None)
        self.__miniOCL_PackageCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniOCL_RootCS"):
                opp_val = getattr(old_value, "miniOCL_RootCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniOCL_RootCS"):
                opp_val = getattr(value, "miniOCL_RootCS", None)
                if opp_val is None:
                    setattr(value, "miniOCL_RootCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def miniOCL_PackageCS7(self):
        return self.__miniOCL_PackageCS7

    @miniOCL_PackageCS7.setter
    def miniOCL_PackageCS7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniOCL_PackageCS__miniOCL_PackageCS7", None)
        self.__miniOCL_PackageCS7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "miniOCL_ClassCS"):
                    opp_val = getattr(item, "miniOCL_ClassCS", None)
                    
                    if opp_val == self:
                        setattr(item, "miniOCL_ClassCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "miniOCL_ClassCS"):
                    opp_val = getattr(item, "miniOCL_ClassCS", None)
                    
                    setattr(item, "miniOCL_ClassCS", self)
                    

    @property
    def miniOCL_PackageCS3(self):
        return self.__miniOCL_PackageCS3

    @miniOCL_PackageCS3.setter
    def miniOCL_PackageCS3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniOCL_PackageCS__miniOCL_PackageCS3", None)
        self.__miniOCL_PackageCS3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "miniOCL_PackageCS5"):
                    opp_val = getattr(item, "miniOCL_PackageCS5", None)
                    
                    if opp_val == self:
                        setattr(item, "miniOCL_PackageCS5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "miniOCL_PackageCS5"):
                    opp_val = getattr(item, "miniOCL_PackageCS5", None)
                    
                    setattr(item, "miniOCL_PackageCS5", self)
                    

class miniOCL_RootCS:

    pass