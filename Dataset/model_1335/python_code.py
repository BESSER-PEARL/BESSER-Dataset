from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class LiteralExpCS:

    pass
class miniOCL_IntLiteralExpCS(LiteralExpCS):

    def __init__(self, intSymbol: int):
        self.intSymbol = intSymbol
        
    @property
    def intSymbol(self) -> int:
        return self.__intSymbol

    @intSymbol.setter
    def intSymbol(self, intSymbol: int):
        self.__intSymbol = intSymbol

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

class miniOCL_PathElementCS:

    def __init__(self, pathName: str, miniOCL_PathElementCS: "miniOCL_PathNameCS" = None):
        self.pathName = pathName
        self.miniOCL_PathElementCS = miniOCL_PathElementCS
        
    @property
    def pathName(self) -> str:
        return self.__pathName

    @pathName.setter
    def pathName(self, pathName: str):
        self.__pathName = pathName

    @property
    def miniOCL_PathElementCS(self):
        return self.__miniOCL_PathElementCS

    @miniOCL_PathElementCS.setter
    def miniOCL_PathElementCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniOCL_PathElementCS__miniOCL_PathElementCS", None)
        self.__miniOCL_PathElementCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniOCL_PathNameCS56"):
                opp_val = getattr(old_value, "miniOCL_PathNameCS56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniOCL_PathNameCS56"):
                opp_val = getattr(value, "miniOCL_PathNameCS56", None)
                if opp_val is None:
                    setattr(value, "miniOCL_PathNameCS56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

class miniOCL_RoundedBracketClauseCS:

    pass
class PrimaryExpCS:

    pass
class miniOCL_LiteralExpCS(PrimaryExpCS):

    pass
class CallExpCS:

    pass
class miniOCL_PrimaryExpCS(CallExpCS):

    pass
class miniOCL_NameExpCS(PrimaryExpCS):

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

class miniOCL_InvariantCS:

    pass
class miniOCL_ConstraintCS:

    pass
class miniOCL_PackageCS:

    def __init__(self, name: str, miniOCL_PackageCS5: "miniOCL_PackageCS" = None, miniOCL_PackageCS3: set["miniOCL_PackageCS"] = None, miniOCL_PackageCS7: set["miniOCL_ClassCS"] = None, miniOCL_PackageCS: "miniOCL_RootCS" = None):
        self.name = name
        self.miniOCL_PackageCS5 = miniOCL_PackageCS5
        self.miniOCL_PackageCS3 = miniOCL_PackageCS3 if miniOCL_PackageCS3 is not None else set()
        self.miniOCL_PackageCS7 = miniOCL_PackageCS7 if miniOCL_PackageCS7 is not None else set()
        self.miniOCL_PackageCS = miniOCL_PackageCS
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
                    

class miniOCL_RootCS:

    pass