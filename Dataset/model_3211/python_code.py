from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class MembershipOp(Enum):
    in = "in"
    not_in = "not_in"
    or = "or"
    and = "and"
    conjunction = "conjunction"
class AggOp(Enum):
    sum = "sum"
    min = "min"
    max = "max"
    prod = "prod"
    inter = "inter"
    union = "union"
    or = "or"
    and = "and"
class OptimizationMode(Enum):
    minimize = "minimize"
    maximize = "maximize"
    solve = "solve"
class RelationalOp(Enum):
    greaterThan = "greaterThan"
    greaterThanOrEqualTo = "greaterThanOrEqualTo"
    lessThan = "lessThan"
    lessThanOrEqualTo = "lessThanOrEqualTo"
    equalTo = "equalTo"
    notEqualTo = "notEqualTo"
class SetOp(Enum):
    symdiff = "symdiff"
    diff = "diff"
    union = "union"
    inter = "inter"
class Quantifier(Enum):
    forAll = "forAll"
class BinaryOp(Enum):
    add = "add"
    subtract = "subtract"
    multiply = "multiply"
    divide = "divide"
    percent = "percent"
    mod = "mod"
    inter = "inter"
    union = "union"
    diff = "diff"
    symdiff = "symdiff"
    power = "power"
class LogicalOp(Enum):
    negation = "negation"
    disjunction = "disjunction"
    or = "or"
    and = "and"
    conjunction = "conjunction"
class UnaryOp(Enum):
    unaryMinus = "unaryMinus"
    negate = "negate"


############################################
# Definition of Classes
############################################

class ScriptStatement:

    pass
class OPLmetamodel_Writeln(ScriptStatement):

    def __init__(self, string: str, arg: str):
        self.string = string
        self.arg = arg
        
    @property
    def arg(self) -> str:
        return self.__arg

    @arg.setter
    def arg(self, arg: str):
        self.__arg = arg

    @property
    def string(self) -> str:
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string

class OPLmetamodel_Sequence:

    pass
class OPLmetamodel_ScriptStatement(ABC):

    pass
class OPLmetamodel_TupleBinding:

    pass
class PiecewiseLinearFunction:

    pass
class OPLmetamodel_RecordField:

    def __init__(self, name: str, OPLmetamodel_RecordField: "OPLmetamodel_Record" = None, OPLmetamodel_RecordField147: "OPLmetamodel_AbstractType" = None):
        self.name = name
        self.OPLmetamodel_RecordField = OPLmetamodel_RecordField
        self.OPLmetamodel_RecordField147 = OPLmetamodel_RecordField147
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def OPLmetamodel_RecordField(self):
        return self.__OPLmetamodel_RecordField

    @OPLmetamodel_RecordField.setter
    def OPLmetamodel_RecordField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_RecordField__OPLmetamodel_RecordField", None)
        self.__OPLmetamodel_RecordField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_Record"):
                opp_val = getattr(old_value, "OPLmetamodel_Record", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_Record"):
                opp_val = getattr(value, "OPLmetamodel_Record", None)
                if opp_val is None:
                    setattr(value, "OPLmetamodel_Record", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OPLmetamodel_RecordField147(self):
        return self.__OPLmetamodel_RecordField147

    @OPLmetamodel_RecordField147.setter
    def OPLmetamodel_RecordField147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_RecordField__OPLmetamodel_RecordField147", None)
        self.__OPLmetamodel_RecordField147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_AbstractType148"):
                opp_val = getattr(old_value, "OPLmetamodel_AbstractType148", None)
                if opp_val == self:
                    setattr(old_value, "OPLmetamodel_AbstractType148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_AbstractType148"):
                opp_val = getattr(value, "OPLmetamodel_AbstractType148", None)
                setattr(value, "OPLmetamodel_AbstractType148", self)

class ParameterDomain:

    pass
class OPLmetamodel_VariableBinding:

    pass
class BooleanExpression:

    pass
class BinaryExpression:

    pass
class OPLmetamodel_RelationalExpression(BooleanExpression, BinaryExpression):

    def __init__(self, redefinedOp: str, OPLmetamodel_RelationalExpression: "OPLmetamodel_RelationalInit" = None):
        self.redefinedOp = redefinedOp
        self.OPLmetamodel_RelationalExpression = OPLmetamodel_RelationalExpression
        
    @property
    def redefinedOp(self) -> str:
        return self.__redefinedOp

    @redefinedOp.setter
    def redefinedOp(self, redefinedOp: str):
        self.__redefinedOp = redefinedOp

    @property
    def OPLmetamodel_RelationalExpression(self):
        return self.__OPLmetamodel_RelationalExpression

    @OPLmetamodel_RelationalExpression.setter
    def OPLmetamodel_RelationalExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_RelationalExpression__OPLmetamodel_RelationalExpression", None)
        self.__OPLmetamodel_RelationalExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_RelationalInit156"):
                opp_val = getattr(old_value, "OPLmetamodel_RelationalInit156", None)
                if opp_val == self:
                    setattr(old_value, "OPLmetamodel_RelationalInit156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_RelationalInit156"):
                opp_val = getattr(value, "OPLmetamodel_RelationalInit156", None)
                setattr(value, "OPLmetamodel_RelationalInit156", self)

class BuiltInFunction:

    pass
class OPLmetamodel_ReflectiveFunction(BuiltInFunction):

    pass
class DataInitMethods:

    pass
class OPLmetamodel_QueryUser(DataInitMethods):

    def __init__(self, ask: str):
        self.ask = ask
        
    @property
    def ask(self) -> str:
        return self.__ask

    @ask.setter
    def ask(self, ask: str):
        self.__ask = ask

class OPLmetamodel_ReadFile(DataInitMethods):

    def __init__(self, path: str):
        self.path = path
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

class OPLmetamodel_Operator:

    pass
class OPLmetamodel_SearchProcedure:

    pass
class OPLmetamodel_PiecewiseExpression:

    pass
class OPLmetamodel_Model:

    def __init__(self, id: str, isConstraintProblem: bool, OPLmetamodel_Model110: "OPLmetamodel_ResourceDeclaration" = None, OPLmetamodel_Model112: set["OPLmetamodel_Constraint"] = None, OPLmetamodel_Model: set["OPLmetamodel_DefinedType"] = None, OPLmetamodel_Model96: set["OPLmetamodel_DataDeclaration"] = None, OPLmetamodel_Model99: set["OPLmetamodel_Constraint"] = None, OPLmetamodel_Model102: "OPLmetamodel_Objective" = None, OPLmetamodel_Model104: set["OPLmetamodel_Function"] = None, OPLmetamodel_Model107: set["OPLmetamodel_ActivityDeclaration"] = None, OPLmetamodel_Model115: set["OPLmetamodel_ScheduleInitialization"] = None, OPLmetamodel_Model117: set["OPLmetamodel_Script"] = None, OPLmetamodel_Model119: set["OPLmetamodel_Setting"] = None, OPLmetamodel_Model121: set["OPLmetamodel_Declaration"] = None, OPLmetamodel_Model123: "OPLmetamodel_SearchProcedure" = None):
        self.id = id
        self.isConstraintProblem = isConstraintProblem
        self.OPLmetamodel_Model110 = OPLmetamodel_Model110
        self.OPLmetamodel_Model112 = OPLmetamodel_Model112 if OPLmetamodel_Model112 is not None else set()
        self.OPLmetamodel_Model = OPLmetamodel_Model if OPLmetamodel_Model is not None else set()
        self.OPLmetamodel_Model96 = OPLmetamodel_Model96 if OPLmetamodel_Model96 is not None else set()
        self.OPLmetamodel_Model99 = OPLmetamodel_Model99 if OPLmetamodel_Model99 is not None else set()
        self.OPLmetamodel_Model102 = OPLmetamodel_Model102
        self.OPLmetamodel_Model104 = OPLmetamodel_Model104 if OPLmetamodel_Model104 is not None else set()
        self.OPLmetamodel_Model107 = OPLmetamodel_Model107 if OPLmetamodel_Model107 is not None else set()
        self.OPLmetamodel_Model115 = OPLmetamodel_Model115 if OPLmetamodel_Model115 is not None else set()
        self.OPLmetamodel_Model117 = OPLmetamodel_Model117 if OPLmetamodel_Model117 is not None else set()
        self.OPLmetamodel_Model119 = OPLmetamodel_Model119 if OPLmetamodel_Model119 is not None else set()
        self.OPLmetamodel_Model121 = OPLmetamodel_Model121 if OPLmetamodel_Model121 is not None else set()
        self.OPLmetamodel_Model123 = OPLmetamodel_Model123
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def isConstraintProblem(self) -> bool:
        return self.__isConstraintProblem

    @isConstraintProblem.setter
    def isConstraintProblem(self, isConstraintProblem: bool):
        self.__isConstraintProblem = isConstraintProblem

    @property
    def OPLmetamodel_Model99(self):
        return self.__OPLmetamodel_Model99

    @OPLmetamodel_Model99.setter
    def OPLmetamodel_Model99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Model__OPLmetamodel_Model99", None)
        self.__OPLmetamodel_Model99 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OPLmetamodel_Constraint100"):
                    opp_val = getattr(item, "OPLmetamodel_Constraint100", None)
                    
                    if opp_val == self:
                        setattr(item, "OPLmetamodel_Constraint100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OPLmetamodel_Constraint100"):
                    opp_val = getattr(item, "OPLmetamodel_Constraint100", None)
                    
                    setattr(item, "OPLmetamodel_Constraint100", self)
                    

    @property
    def OPLmetamodel_Model107(self):
        return self.__OPLmetamodel_Model107

    @OPLmetamodel_Model107.setter
    def OPLmetamodel_Model107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Model__OPLmetamodel_Model107", None)
        self.__OPLmetamodel_Model107 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OPLmetamodel_ActivityDeclaration108"):
                    opp_val = getattr(item, "OPLmetamodel_ActivityDeclaration108", None)
                    
                    if opp_val == self:
                        setattr(item, "OPLmetamodel_ActivityDeclaration108", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OPLmetamodel_ActivityDeclaration108"):
                    opp_val = getattr(item, "OPLmetamodel_ActivityDeclaration108", None)
                    
                    setattr(item, "OPLmetamodel_ActivityDeclaration108", self)
                    

    @property
    def OPLmetamodel_Model123(self):
        return self.__OPLmetamodel_Model123

    @OPLmetamodel_Model123.setter
    def OPLmetamodel_Model123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Model__OPLmetamodel_Model123", None)
        self.__OPLmetamodel_Model123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_SearchProcedure"):
                opp_val = getattr(old_value, "OPLmetamodel_SearchProcedure", None)
                if opp_val == self:
                    setattr(old_value, "OPLmetamodel_SearchProcedure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_SearchProcedure"):
                opp_val = getattr(value, "OPLmetamodel_SearchProcedure", None)
                setattr(value, "OPLmetamodel_SearchProcedure", self)

    @property
    def OPLmetamodel_Model112(self):
        return self.__OPLmetamodel_Model112

    @OPLmetamodel_Model112.setter
    def OPLmetamodel_Model112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Model__OPLmetamodel_Model112", None)
        self.__OPLmetamodel_Model112 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OPLmetamodel_Constraint113"):
                    opp_val = getattr(item, "OPLmetamodel_Constraint113", None)
                    
                    if opp_val == self:
                        setattr(item, "OPLmetamodel_Constraint113", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OPLmetamodel_Constraint113"):
                    opp_val = getattr(item, "OPLmetamodel_Constraint113", None)
                    
                    setattr(item, "OPLmetamodel_Constraint113", self)
                    

    @property
    def OPLmetamodel_Model115(self):
        return self.__OPLmetamodel_Model115

    @OPLmetamodel_Model115.setter
    def OPLmetamodel_Model115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Model__OPLmetamodel_Model115", None)
        self.__OPLmetamodel_Model115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OPLmetamodel_ScheduleInitialization"):
                    opp_val = getattr(item, "OPLmetamodel_ScheduleInitialization", None)
                    
                    if opp_val == self:
                        setattr(item, "OPLmetamodel_ScheduleInitialization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OPLmetamodel_ScheduleInitialization"):
                    opp_val = getattr(item, "OPLmetamodel_ScheduleInitialization", None)
                    
                    setattr(item, "OPLmetamodel_ScheduleInitialization", self)
                    

    @property
    def OPLmetamodel_Model(self):
        return self.__OPLmetamodel_Model

    @OPLmetamodel_Model.setter
    def OPLmetamodel_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Model__OPLmetamodel_Model", None)
        self.__OPLmetamodel_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OPLmetamodel_DefinedType"):
                    opp_val = getattr(item, "OPLmetamodel_DefinedType", None)
                    
                    if opp_val == self:
                        setattr(item, "OPLmetamodel_DefinedType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OPLmetamodel_DefinedType"):
                    opp_val = getattr(item, "OPLmetamodel_DefinedType", None)
                    
                    setattr(item, "OPLmetamodel_DefinedType", self)
                    

    @property
    def OPLmetamodel_Model119(self):
        return self.__OPLmetamodel_Model119

    @OPLmetamodel_Model119.setter
    def OPLmetamodel_Model119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Model__OPLmetamodel_Model119", None)
        self.__OPLmetamodel_Model119 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OPLmetamodel_Setting"):
                    opp_val = getattr(item, "OPLmetamodel_Setting", None)
                    
                    if opp_val == self:
                        setattr(item, "OPLmetamodel_Setting", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OPLmetamodel_Setting"):
                    opp_val = getattr(item, "OPLmetamodel_Setting", None)
                    
                    setattr(item, "OPLmetamodel_Setting", self)
                    

    @property
    def OPLmetamodel_Model96(self):
        return self.__OPLmetamodel_Model96

    @OPLmetamodel_Model96.setter
    def OPLmetamodel_Model96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Model__OPLmetamodel_Model96", None)
        self.__OPLmetamodel_Model96 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OPLmetamodel_DataDeclaration97"):
                    opp_val = getattr(item, "OPLmetamodel_DataDeclaration97", None)
                    
                    if opp_val == self:
                        setattr(item, "OPLmetamodel_DataDeclaration97", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OPLmetamodel_DataDeclaration97"):
                    opp_val = getattr(item, "OPLmetamodel_DataDeclaration97", None)
                    
                    setattr(item, "OPLmetamodel_DataDeclaration97", self)
                    

    @property
    def OPLmetamodel_Model110(self):
        return self.__OPLmetamodel_Model110

    @OPLmetamodel_Model110.setter
    def OPLmetamodel_Model110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Model__OPLmetamodel_Model110", None)
        self.__OPLmetamodel_Model110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_ResourceDeclaration"):
                opp_val = getattr(old_value, "OPLmetamodel_ResourceDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "OPLmetamodel_ResourceDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_ResourceDeclaration"):
                opp_val = getattr(value, "OPLmetamodel_ResourceDeclaration", None)
                setattr(value, "OPLmetamodel_ResourceDeclaration", self)

    @property
    def OPLmetamodel_Model102(self):
        return self.__OPLmetamodel_Model102

    @OPLmetamodel_Model102.setter
    def OPLmetamodel_Model102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Model__OPLmetamodel_Model102", None)
        self.__OPLmetamodel_Model102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_Objective"):
                opp_val = getattr(old_value, "OPLmetamodel_Objective", None)
                if opp_val == self:
                    setattr(old_value, "OPLmetamodel_Objective", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_Objective"):
                opp_val = getattr(value, "OPLmetamodel_Objective", None)
                setattr(value, "OPLmetamodel_Objective", self)

    @property
    def OPLmetamodel_Model121(self):
        return self.__OPLmetamodel_Model121

    @OPLmetamodel_Model121.setter
    def OPLmetamodel_Model121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Model__OPLmetamodel_Model121", None)
        self.__OPLmetamodel_Model121 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OPLmetamodel_Declaration"):
                    opp_val = getattr(item, "OPLmetamodel_Declaration", None)
                    
                    if opp_val == self:
                        setattr(item, "OPLmetamodel_Declaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OPLmetamodel_Declaration"):
                    opp_val = getattr(item, "OPLmetamodel_Declaration", None)
                    
                    setattr(item, "OPLmetamodel_Declaration", self)
                    

    @property
    def OPLmetamodel_Model117(self):
        return self.__OPLmetamodel_Model117

    @OPLmetamodel_Model117.setter
    def OPLmetamodel_Model117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Model__OPLmetamodel_Model117", None)
        self.__OPLmetamodel_Model117 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OPLmetamodel_Script"):
                    opp_val = getattr(item, "OPLmetamodel_Script", None)
                    
                    if opp_val == self:
                        setattr(item, "OPLmetamodel_Script", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OPLmetamodel_Script"):
                    opp_val = getattr(item, "OPLmetamodel_Script", None)
                    
                    setattr(item, "OPLmetamodel_Script", self)
                    

    @property
    def OPLmetamodel_Model104(self):
        return self.__OPLmetamodel_Model104

    @OPLmetamodel_Model104.setter
    def OPLmetamodel_Model104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Model__OPLmetamodel_Model104", None)
        self.__OPLmetamodel_Model104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OPLmetamodel_Function105"):
                    opp_val = getattr(item, "OPLmetamodel_Function105", None)
                    
                    if opp_val == self:
                        setattr(item, "OPLmetamodel_Function105", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OPLmetamodel_Function105"):
                    opp_val = getattr(item, "OPLmetamodel_Function105", None)
                    
                    setattr(item, "OPLmetamodel_Function105", self)
                    

class IntegerType:

    pass
class OPLmetamodel_PositiveIntegerType(IntegerType):

    pass
class OPLmetamodel_Interval:

    def __init__(self, isOptional: bool, OPLmetamodel_Interval: "OPLmetamodel_RangeType" = None, OPLmetamodel_Interval86: "OPLmetamodel_NumericType" = None, OPLmetamodel_Interval88: "OPLmetamodel_StepFunction" = None, OPLmetamodel_Interval163: "OPLmetamodel_Sequence" = None):
        self.isOptional = isOptional
        self.OPLmetamodel_Interval = OPLmetamodel_Interval
        self.OPLmetamodel_Interval86 = OPLmetamodel_Interval86
        self.OPLmetamodel_Interval88 = OPLmetamodel_Interval88
        self.OPLmetamodel_Interval163 = OPLmetamodel_Interval163
        
    @property
    def isOptional(self) -> bool:
        return self.__isOptional

    @isOptional.setter
    def isOptional(self, isOptional: bool):
        self.__isOptional = isOptional

    @property
    def OPLmetamodel_Interval163(self):
        return self.__OPLmetamodel_Interval163

    @OPLmetamodel_Interval163.setter
    def OPLmetamodel_Interval163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Interval__OPLmetamodel_Interval163", None)
        self.__OPLmetamodel_Interval163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_Sequence"):
                opp_val = getattr(old_value, "OPLmetamodel_Sequence", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_Sequence"):
                opp_val = getattr(value, "OPLmetamodel_Sequence", None)
                if opp_val is None:
                    setattr(value, "OPLmetamodel_Sequence", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OPLmetamodel_Interval88(self):
        return self.__OPLmetamodel_Interval88

    @OPLmetamodel_Interval88.setter
    def OPLmetamodel_Interval88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Interval__OPLmetamodel_Interval88", None)
        self.__OPLmetamodel_Interval88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_StepFunction"):
                opp_val = getattr(old_value, "OPLmetamodel_StepFunction", None)
                if opp_val == self:
                    setattr(old_value, "OPLmetamodel_StepFunction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_StepFunction"):
                opp_val = getattr(value, "OPLmetamodel_StepFunction", None)
                setattr(value, "OPLmetamodel_StepFunction", self)

    @property
    def OPLmetamodel_Interval(self):
        return self.__OPLmetamodel_Interval

    @OPLmetamodel_Interval.setter
    def OPLmetamodel_Interval(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Interval__OPLmetamodel_Interval", None)
        self.__OPLmetamodel_Interval = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_RangeType"):
                opp_val = getattr(old_value, "OPLmetamodel_RangeType", None)
                if opp_val == self:
                    setattr(old_value, "OPLmetamodel_RangeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_RangeType"):
                opp_val = getattr(value, "OPLmetamodel_RangeType", None)
                setattr(value, "OPLmetamodel_RangeType", self)

    @property
    def OPLmetamodel_Interval86(self):
        return self.__OPLmetamodel_Interval86

    @OPLmetamodel_Interval86.setter
    def OPLmetamodel_Interval86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Interval__OPLmetamodel_Interval86", None)
        self.__OPLmetamodel_Interval86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_NumericType"):
                opp_val = getattr(old_value, "OPLmetamodel_NumericType", None)
                if opp_val == self:
                    setattr(old_value, "OPLmetamodel_NumericType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_NumericType"):
                opp_val = getattr(value, "OPLmetamodel_NumericType", None)
                setattr(value, "OPLmetamodel_NumericType", self)

class OPLmetamodel_In:

    pass
class OPLmetamodel_FunctionRef:

    def __init__(self, name: str, OPLmetamodel_FunctionRef: "OPLmetamodel_Function" = None):
        self.name = name
        self.OPLmetamodel_FunctionRef = OPLmetamodel_FunctionRef
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def OPLmetamodel_FunctionRef(self):
        return self.__OPLmetamodel_FunctionRef

    @OPLmetamodel_FunctionRef.setter
    def OPLmetamodel_FunctionRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_FunctionRef__OPLmetamodel_FunctionRef", None)
        self.__OPLmetamodel_FunctionRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_Function"):
                opp_val = getattr(old_value, "OPLmetamodel_Function", None)
                if opp_val == self:
                    setattr(old_value, "OPLmetamodel_Function", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_Function"):
                opp_val = getattr(value, "OPLmetamodel_Function", None)
                setattr(value, "OPLmetamodel_Function", self)

class OPLmetamodel_StepFunction(PiecewiseLinearFunction):

    pass
class Constraint:

    pass
class OPLmetamodel_IfConstraint(Constraint):

    pass
class OPLmetamodel_ForAllConstraint(Constraint):

    pass
class NumericExpression:

    pass
class OPLmetamodel_IntegerExpression(NumericExpression):

    def __init__(self, body: str):
        self.body = body
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

class OPLmetamodel_RangeExpression(NumericExpression):

    pass
class OPLmetamodel_FloatExpression(NumericExpression):

    def __init__(self, body: str):
        self.body = body
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

class OPLmetamodel_ParameterDomain(ABC):

    pass
class NumericType:

    pass
class OPLmetamodel_IntegerType(NumericType):

    pass
class OPLmetamodel_FloatType(NumericType):

    pass
class RangeType:

    pass
class OPLmetamodel_IntegerRangeType(RangeType, IntegerType):

    pass
class FloatType:

    pass
class OPLmetamodel_PositiveFloatType(FloatType):

    pass
class OPLmetamodel_FloatRangeType(RangeType, FloatType):

    pass
class OPLmetamodel_Error:

    pass
class OPLmetamodel_Entity:

    pass
class SetType:

    pass
class OPLmetamodel_RangeType(SetType):

    pass
class OPLmetamodel_EnumerationType(SetType):

    pass
class OPLmetamodel_DisplayInstruction:

    pass
class AbstractType:

    pass
class OPLmetamodel_PrimitiveType(AbstractType):

    pass
class OPLmetamodel_DeferredInit:

    pass
class OPLmetamodel_Declaration(ABC):

    def __init__(self, order: int, OPLmetamodel_Declaration: "OPLmetamodel_Model" = None):
        self.order = order
        self.OPLmetamodel_Declaration = OPLmetamodel_Declaration
        
    @property
    def order(self) -> int:
        return self.__order

    @order.setter
    def order(self, order: int):
        self.__order = order

    @property
    def OPLmetamodel_Declaration(self):
        return self.__OPLmetamodel_Declaration

    @OPLmetamodel_Declaration.setter
    def OPLmetamodel_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Declaration__OPLmetamodel_Declaration", None)
        self.__OPLmetamodel_Declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_Model121"):
                opp_val = getattr(old_value, "OPLmetamodel_Model121", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_Model121"):
                opp_val = getattr(value, "OPLmetamodel_Model121", None)
                if opp_val is None:
                    setattr(value, "OPLmetamodel_Model121", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Initialization:

    pass
class OPLmetamodel_RelationalInit(Initialization):

    pass
class OPLmetamodel_DataObject(Initialization):

    def __init__(self, body: str):
        self.body = body
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

class OPLmetamodel_DataInitMethods(ABC):

    pass
class OPLmetamodel_ParameterDeclaration:

    pass
class CollectionExpression:

    pass
class OPLmetamodel_Extension(CollectionExpression):

    pass
class OPLmetamodel_Comprehension(CollectionExpression):

    pass
class Function:

    pass
class OPLmetamodel_StateFunction(Function):

    pass
class OPLmetamodel_PiecewiseLinearFunction(Function):

    pass
class OPLmetamodel_CumulativeFunction(Function):

    pass
class OPLmetamodel_BuiltInFunction(Function):

    pass
class PrimitiveType:

    pass
class OPLmetamodel_StringType(PrimitiveType):

    pass
class OPLmetamodel_NumericType(PrimitiveType):

    pass
class OPLmetamodel_BooleanType(PrimitiveType):

    pass
class OPLmetamodel_Initialization(ABC):

    pass
class OPLmetamodel_BooleanBlock:

    pass
class Reference:

    pass
class OPLmetamodel_ParameterRef(Reference):

    pass
class OPLmetamodel_BindingRef(Reference):

    pass
class AbstractBinaryOperator:

    pass
class OPLmetamodel_RelationalOperator(AbstractBinaryOperator):

    def __init__(self, op: str):
        self.op = op
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

class OPLmetamodel_BinaryOperator(AbstractBinaryOperator):

    def __init__(self, op: str):
        self.op = op
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

class PrimitiveExpression:

    pass
class OPLmetamodel_EnumLiteral(PrimitiveType, PrimitiveExpression):

    pass
class OPLmetamodel_NumericExpression(PrimitiveExpression):

    pass
class OPLmetamodel_StringExpression(PrimitiveExpression):

    def __init__(self, body: str):
        self.body = body
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

class OPLmetamodel_BooleanExpression(PrimitiveExpression):

    def __init__(self, body: str, OPLmetamodel_BooleanExpression: "OPLmetamodel_IfConstraint" = None, OPLmetamodel_BooleanExpression77: "OPLmetamodel_IfExpression" = None):
        self.body = body
        self.OPLmetamodel_BooleanExpression = OPLmetamodel_BooleanExpression
        self.OPLmetamodel_BooleanExpression77 = OPLmetamodel_BooleanExpression77
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def OPLmetamodel_BooleanExpression77(self):
        return self.__OPLmetamodel_BooleanExpression77

    @OPLmetamodel_BooleanExpression77.setter
    def OPLmetamodel_BooleanExpression77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_BooleanExpression__OPLmetamodel_BooleanExpression77", None)
        self.__OPLmetamodel_BooleanExpression77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_IfExpression"):
                opp_val = getattr(old_value, "OPLmetamodel_IfExpression", None)
                if opp_val == self:
                    setattr(old_value, "OPLmetamodel_IfExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_IfExpression"):
                opp_val = getattr(value, "OPLmetamodel_IfExpression", None)
                setattr(value, "OPLmetamodel_IfExpression", self)

    @property
    def OPLmetamodel_BooleanExpression(self):
        return self.__OPLmetamodel_BooleanExpression

    @OPLmetamodel_BooleanExpression.setter
    def OPLmetamodel_BooleanExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_BooleanExpression__OPLmetamodel_BooleanExpression", None)
        self.__OPLmetamodel_BooleanExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_IfConstraint"):
                opp_val = getattr(old_value, "OPLmetamodel_IfConstraint", None)
                if opp_val == self:
                    setattr(old_value, "OPLmetamodel_IfConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_IfConstraint"):
                opp_val = getattr(value, "OPLmetamodel_IfConstraint", None)
                setattr(value, "OPLmetamodel_IfConstraint", self)

class OPLmetamodel_DataRef(Reference):

    pass
class DefinedType:

    pass
class OPLmetamodel_Record(ParameterDomain, DefinedType):

    def __init__(self, name: str, isTuple: bool, OPLmetamodel_Record: set["OPLmetamodel_RecordField"] = None):
        self.name = name
        self.isTuple = isTuple
        self.OPLmetamodel_Record = OPLmetamodel_Record if OPLmetamodel_Record is not None else set()
        
    @property
    def isTuple(self) -> bool:
        return self.__isTuple

    @isTuple.setter
    def isTuple(self, isTuple: bool):
        self.__isTuple = isTuple

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def OPLmetamodel_Record(self):
        return self.__OPLmetamodel_Record

    @OPLmetamodel_Record.setter
    def OPLmetamodel_Record(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Record__OPLmetamodel_Record", None)
        self.__OPLmetamodel_Record = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OPLmetamodel_RecordField"):
                    opp_val = getattr(item, "OPLmetamodel_RecordField", None)
                    
                    if opp_val == self:
                        setattr(item, "OPLmetamodel_RecordField", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OPLmetamodel_RecordField"):
                    opp_val = getattr(item, "OPLmetamodel_RecordField", None)
                    
                    setattr(item, "OPLmetamodel_RecordField", self)
                    

class OPLmetamodel_SetType(ParameterDomain, DefinedType):

    def __init__(self, name: str, OPLmetamodel_SetType: "OPLmetamodel_AbstractType" = None, OPLmetamodel_SetType170: set["OPLmetamodel_Entity"] = None, OPLmetamodel_SetType174: "OPLmetamodel_StateFunction" = None):
        self.name = name
        self.OPLmetamodel_SetType = OPLmetamodel_SetType
        self.OPLmetamodel_SetType170 = OPLmetamodel_SetType170 if OPLmetamodel_SetType170 is not None else set()
        self.OPLmetamodel_SetType174 = OPLmetamodel_SetType174
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def OPLmetamodel_SetType(self):
        return self.__OPLmetamodel_SetType

    @OPLmetamodel_SetType.setter
    def OPLmetamodel_SetType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_SetType__OPLmetamodel_SetType", None)
        self.__OPLmetamodel_SetType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_AbstractType168"):
                opp_val = getattr(old_value, "OPLmetamodel_AbstractType168", None)
                if opp_val == self:
                    setattr(old_value, "OPLmetamodel_AbstractType168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_AbstractType168"):
                opp_val = getattr(value, "OPLmetamodel_AbstractType168", None)
                setattr(value, "OPLmetamodel_AbstractType168", self)

    @property
    def OPLmetamodel_SetType170(self):
        return self.__OPLmetamodel_SetType170

    @OPLmetamodel_SetType170.setter
    def OPLmetamodel_SetType170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_SetType__OPLmetamodel_SetType170", None)
        self.__OPLmetamodel_SetType170 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OPLmetamodel_Entity"):
                    opp_val = getattr(item, "OPLmetamodel_Entity", None)
                    
                    if opp_val == self:
                        setattr(item, "OPLmetamodel_Entity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OPLmetamodel_Entity"):
                    opp_val = getattr(item, "OPLmetamodel_Entity", None)
                    
                    setattr(item, "OPLmetamodel_Entity", self)
                    

    @property
    def OPLmetamodel_SetType174(self):
        return self.__OPLmetamodel_SetType174

    @OPLmetamodel_SetType174.setter
    def OPLmetamodel_SetType174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_SetType__OPLmetamodel_SetType174", None)
        self.__OPLmetamodel_SetType174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_StateFunction"):
                opp_val = getattr(old_value, "OPLmetamodel_StateFunction", None)
                if opp_val == self:
                    setattr(old_value, "OPLmetamodel_StateFunction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_StateFunction"):
                opp_val = getattr(value, "OPLmetamodel_StateFunction", None)
                setattr(value, "OPLmetamodel_StateFunction", self)

class OPLmetamodel_ArrayType(DefinedType):

    pass
class PathExpression:

    pass
class OPLmetamodel_FunctionCall(PathExpression):

    def __init__(self, functionName: str, OPLmetamodel_FunctionCall: set["OPLmetamodel_Expression"] = None):
        self.functionName = functionName
        self.OPLmetamodel_FunctionCall = OPLmetamodel_FunctionCall if OPLmetamodel_FunctionCall is not None else set()
        
    @property
    def functionName(self) -> str:
        return self.__functionName

    @functionName.setter
    def functionName(self, functionName: str):
        self.__functionName = functionName

    @property
    def OPLmetamodel_FunctionCall(self):
        return self.__OPLmetamodel_FunctionCall

    @OPLmetamodel_FunctionCall.setter
    def OPLmetamodel_FunctionCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_FunctionCall__OPLmetamodel_FunctionCall", None)
        self.__OPLmetamodel_FunctionCall = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OPLmetamodel_Expression68"):
                    opp_val = getattr(item, "OPLmetamodel_Expression68", None)
                    
                    if opp_val == self:
                        setattr(item, "OPLmetamodel_Expression68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OPLmetamodel_Expression68"):
                    opp_val = getattr(item, "OPLmetamodel_Expression68", None)
                    
                    setattr(item, "OPLmetamodel_Expression68", self)
                    

class OPLmetamodel_PathDereference(PathExpression):

    pass
class OPLmetamodel_ArrayDereference(PathExpression):

    pass
class OPLmetamodel_FormalParameter:

    def __init__(self, isOrdered: bool, OPLmetamodel_FormalParameter5: "OPLmetamodel_AllExpression" = None, OPLmetamodel_FormalParameter: "OPLmetamodel_AggregateExp" = None, OPLmetamodel_FormalParameter48: "OPLmetamodel_ParameterDomain" = None, OPLmetamodel_FormalParameter50: set["OPLmetamodel_BindingRef"] = None, OPLmetamodel_FormalParameter52: "OPLmetamodel_Expression" = None, OPLmetamodel_FormalParameter57: "OPLmetamodel_ForAllConstraint" = None):
        self.isOrdered = isOrdered
        self.OPLmetamodel_FormalParameter5 = OPLmetamodel_FormalParameter5
        self.OPLmetamodel_FormalParameter = OPLmetamodel_FormalParameter
        self.OPLmetamodel_FormalParameter48 = OPLmetamodel_FormalParameter48
        self.OPLmetamodel_FormalParameter50 = OPLmetamodel_FormalParameter50 if OPLmetamodel_FormalParameter50 is not None else set()
        self.OPLmetamodel_FormalParameter52 = OPLmetamodel_FormalParameter52
        self.OPLmetamodel_FormalParameter57 = OPLmetamodel_FormalParameter57
        
    @property
    def isOrdered(self) -> bool:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: bool):
        self.__isOrdered = isOrdered

    @property
    def OPLmetamodel_FormalParameter5(self):
        return self.__OPLmetamodel_FormalParameter5

    @OPLmetamodel_FormalParameter5.setter
    def OPLmetamodel_FormalParameter5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_FormalParameter__OPLmetamodel_FormalParameter5", None)
        self.__OPLmetamodel_FormalParameter5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_AllExpression"):
                opp_val = getattr(old_value, "OPLmetamodel_AllExpression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_AllExpression"):
                opp_val = getattr(value, "OPLmetamodel_AllExpression", None)
                if opp_val is None:
                    setattr(value, "OPLmetamodel_AllExpression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OPLmetamodel_FormalParameter50(self):
        return self.__OPLmetamodel_FormalParameter50

    @OPLmetamodel_FormalParameter50.setter
    def OPLmetamodel_FormalParameter50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_FormalParameter__OPLmetamodel_FormalParameter50", None)
        self.__OPLmetamodel_FormalParameter50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OPLmetamodel_BindingRef"):
                    opp_val = getattr(item, "OPLmetamodel_BindingRef", None)
                    
                    if opp_val == self:
                        setattr(item, "OPLmetamodel_BindingRef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OPLmetamodel_BindingRef"):
                    opp_val = getattr(item, "OPLmetamodel_BindingRef", None)
                    
                    setattr(item, "OPLmetamodel_BindingRef", self)
                    

    @property
    def OPLmetamodel_FormalParameter57(self):
        return self.__OPLmetamodel_FormalParameter57

    @OPLmetamodel_FormalParameter57.setter
    def OPLmetamodel_FormalParameter57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_FormalParameter__OPLmetamodel_FormalParameter57", None)
        self.__OPLmetamodel_FormalParameter57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_ForAllConstraint"):
                opp_val = getattr(old_value, "OPLmetamodel_ForAllConstraint", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_ForAllConstraint"):
                opp_val = getattr(value, "OPLmetamodel_ForAllConstraint", None)
                if opp_val is None:
                    setattr(value, "OPLmetamodel_ForAllConstraint", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OPLmetamodel_FormalParameter(self):
        return self.__OPLmetamodel_FormalParameter

    @OPLmetamodel_FormalParameter.setter
    def OPLmetamodel_FormalParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_FormalParameter__OPLmetamodel_FormalParameter", None)
        self.__OPLmetamodel_FormalParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_AggregateExp"):
                opp_val = getattr(old_value, "OPLmetamodel_AggregateExp", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_AggregateExp"):
                opp_val = getattr(value, "OPLmetamodel_AggregateExp", None)
                if opp_val is None:
                    setattr(value, "OPLmetamodel_AggregateExp", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OPLmetamodel_FormalParameter48(self):
        return self.__OPLmetamodel_FormalParameter48

    @OPLmetamodel_FormalParameter48.setter
    def OPLmetamodel_FormalParameter48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_FormalParameter__OPLmetamodel_FormalParameter48", None)
        self.__OPLmetamodel_FormalParameter48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_ParameterDomain"):
                opp_val = getattr(old_value, "OPLmetamodel_ParameterDomain", None)
                if opp_val == self:
                    setattr(old_value, "OPLmetamodel_ParameterDomain", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_ParameterDomain"):
                opp_val = getattr(value, "OPLmetamodel_ParameterDomain", None)
                setattr(value, "OPLmetamodel_ParameterDomain", self)

    @property
    def OPLmetamodel_FormalParameter52(self):
        return self.__OPLmetamodel_FormalParameter52

    @OPLmetamodel_FormalParameter52.setter
    def OPLmetamodel_FormalParameter52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_FormalParameter__OPLmetamodel_FormalParameter52", None)
        self.__OPLmetamodel_FormalParameter52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_Expression53"):
                opp_val = getattr(old_value, "OPLmetamodel_Expression53", None)
                if opp_val == self:
                    setattr(old_value, "OPLmetamodel_Expression53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_Expression53"):
                opp_val = getattr(value, "OPLmetamodel_Expression53", None)
                setattr(value, "OPLmetamodel_Expression53", self)

class Expression:

    pass
class OPLmetamodel_PrimitiveExpression(Expression):

    pass
class OPLmetamodel_IndexValuePair(Expression):

    pass
class OPLmetamodel_CollectionExpression(Expression):

    def __init__(self, isUnique: bool):
        self.isUnique = isUnique
        
    @property
    def isUnique(self) -> bool:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: bool):
        self.__isUnique = isUnique

class OPLmetamodel_RecordValue(Expression):

    pass
class OPLmetamodel_ArrayValue(Expression):

    pass
class OPLmetamodel_Reference(Expression):

    def __init__(self, name: str, OPLmetamodel_Reference: "OPLmetamodel_Function" = None, OPLmetamodel_Reference128: "OPLmetamodel_PathDereference" = None, OPLmetamodel_Reference159: "OPLmetamodel_Script" = None):
        self.name = name
        self.OPLmetamodel_Reference = OPLmetamodel_Reference
        self.OPLmetamodel_Reference128 = OPLmetamodel_Reference128
        self.OPLmetamodel_Reference159 = OPLmetamodel_Reference159
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def OPLmetamodel_Reference128(self):
        return self.__OPLmetamodel_Reference128

    @OPLmetamodel_Reference128.setter
    def OPLmetamodel_Reference128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Reference__OPLmetamodel_Reference128", None)
        self.__OPLmetamodel_Reference128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_PathDereference"):
                opp_val = getattr(old_value, "OPLmetamodel_PathDereference", None)
                if opp_val == self:
                    setattr(old_value, "OPLmetamodel_PathDereference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_PathDereference"):
                opp_val = getattr(value, "OPLmetamodel_PathDereference", None)
                setattr(value, "OPLmetamodel_PathDereference", self)

    @property
    def OPLmetamodel_Reference159(self):
        return self.__OPLmetamodel_Reference159

    @OPLmetamodel_Reference159.setter
    def OPLmetamodel_Reference159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Reference__OPLmetamodel_Reference159", None)
        self.__OPLmetamodel_Reference159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_Script158"):
                opp_val = getattr(old_value, "OPLmetamodel_Script158", None)
                if opp_val == self:
                    setattr(old_value, "OPLmetamodel_Script158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_Script158"):
                opp_val = getattr(value, "OPLmetamodel_Script158", None)
                setattr(value, "OPLmetamodel_Script158", self)

    @property
    def OPLmetamodel_Reference(self):
        return self.__OPLmetamodel_Reference

    @OPLmetamodel_Reference.setter
    def OPLmetamodel_Reference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Reference__OPLmetamodel_Reference", None)
        self.__OPLmetamodel_Reference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_Function66"):
                opp_val = getattr(old_value, "OPLmetamodel_Function66", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_Function66"):
                opp_val = getattr(value, "OPLmetamodel_Function66", None)
                if opp_val is None:
                    setattr(value, "OPLmetamodel_Function66", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class OPLmetamodel_SetValue(Expression):

    pass
class OPLmetamodel_BlockExpression(Expression):

    pass
class OPLmetamodel_IfExpression(Expression):

    pass
class OPLmetamodel_BinaryExpression(Expression):

    pass
class OPLmetamodel_ArraySlotConstraint(Expression):

    pass
class OPLmetamodel_UnaryExpression(Expression):

    def __init__(self, op: str, OPLmetamodel_UnaryExpression: "OPLmetamodel_Expression" = None):
        self.op = op
        self.OPLmetamodel_UnaryExpression = OPLmetamodel_UnaryExpression
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def OPLmetamodel_UnaryExpression(self):
        return self.__OPLmetamodel_UnaryExpression

    @OPLmetamodel_UnaryExpression.setter
    def OPLmetamodel_UnaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_UnaryExpression__OPLmetamodel_UnaryExpression", None)
        self.__OPLmetamodel_UnaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_Expression178"):
                opp_val = getattr(old_value, "OPLmetamodel_Expression178", None)
                if opp_val == self:
                    setattr(old_value, "OPLmetamodel_Expression178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_Expression178"):
                opp_val = getattr(value, "OPLmetamodel_Expression178", None)
                setattr(value, "OPLmetamodel_Expression178", self)

class OPLmetamodel_PathExpression(Expression):

    pass
class OPLmetamodel_AggregateExp(Expression):

    def __init__(self, op: str, OPLmetamodel_AggregateExp3: "OPLmetamodel_Expression" = None, OPLmetamodel_AggregateExp: set["OPLmetamodel_FormalParameter"] = None):
        self.op = op
        self.OPLmetamodel_AggregateExp3 = OPLmetamodel_AggregateExp3
        self.OPLmetamodel_AggregateExp = OPLmetamodel_AggregateExp if OPLmetamodel_AggregateExp is not None else set()
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def OPLmetamodel_AggregateExp3(self):
        return self.__OPLmetamodel_AggregateExp3

    @OPLmetamodel_AggregateExp3.setter
    def OPLmetamodel_AggregateExp3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_AggregateExp__OPLmetamodel_AggregateExp3", None)
        self.__OPLmetamodel_AggregateExp3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_Expression"):
                opp_val = getattr(old_value, "OPLmetamodel_Expression", None)
                if opp_val == self:
                    setattr(old_value, "OPLmetamodel_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_Expression"):
                opp_val = getattr(value, "OPLmetamodel_Expression", None)
                setattr(value, "OPLmetamodel_Expression", self)

    @property
    def OPLmetamodel_AggregateExp(self):
        return self.__OPLmetamodel_AggregateExp

    @OPLmetamodel_AggregateExp.setter
    def OPLmetamodel_AggregateExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_AggregateExp__OPLmetamodel_AggregateExp", None)
        self.__OPLmetamodel_AggregateExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OPLmetamodel_FormalParameter"):
                    opp_val = getattr(item, "OPLmetamodel_FormalParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "OPLmetamodel_FormalParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OPLmetamodel_FormalParameter"):
                    opp_val = getattr(item, "OPLmetamodel_FormalParameter", None)
                    
                    setattr(item, "OPLmetamodel_FormalParameter", self)
                    

class OPLmetamodel_Number:

    pass
class Declaration:

    pass
class OPLmetamodel_ResourceDeclaration(Declaration):

    pass
class OPLmetamodel_Function(Declaration):

    pass
class OPLmetamodel_DefinedType(Declaration, AbstractType):

    pass
class OPLmetamodel_DataDeclaration(Declaration):

    def __init__(self, isDecisionVar: bool, isDecisionExpr: bool, OPLmetamodel_DataDeclaration35: "OPLmetamodel_AbstractType" = None, OPLmetamodel_DataDeclaration38: "OPLmetamodel_Initialization" = None, OPLmetamodel_DataDeclaration: "OPLmetamodel_DataRef" = None, OPLmetamodel_DataDeclaration40: "OPLmetamodel_Expression" = None, OPLmetamodel_DataDeclaration97: "OPLmetamodel_Model" = None):
        self.isDecisionVar = isDecisionVar
        self.isDecisionExpr = isDecisionExpr
        self.OPLmetamodel_DataDeclaration35 = OPLmetamodel_DataDeclaration35
        self.OPLmetamodel_DataDeclaration38 = OPLmetamodel_DataDeclaration38
        self.OPLmetamodel_DataDeclaration = OPLmetamodel_DataDeclaration
        self.OPLmetamodel_DataDeclaration40 = OPLmetamodel_DataDeclaration40
        self.OPLmetamodel_DataDeclaration97 = OPLmetamodel_DataDeclaration97
        
    @property
    def isDecisionExpr(self) -> bool:
        return self.__isDecisionExpr

    @isDecisionExpr.setter
    def isDecisionExpr(self, isDecisionExpr: bool):
        self.__isDecisionExpr = isDecisionExpr

    @property
    def isDecisionVar(self) -> bool:
        return self.__isDecisionVar

    @isDecisionVar.setter
    def isDecisionVar(self, isDecisionVar: bool):
        self.__isDecisionVar = isDecisionVar

    @property
    def OPLmetamodel_DataDeclaration38(self):
        return self.__OPLmetamodel_DataDeclaration38

    @OPLmetamodel_DataDeclaration38.setter
    def OPLmetamodel_DataDeclaration38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_DataDeclaration__OPLmetamodel_DataDeclaration38", None)
        self.__OPLmetamodel_DataDeclaration38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_Initialization"):
                opp_val = getattr(old_value, "OPLmetamodel_Initialization", None)
                if opp_val == self:
                    setattr(old_value, "OPLmetamodel_Initialization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_Initialization"):
                opp_val = getattr(value, "OPLmetamodel_Initialization", None)
                setattr(value, "OPLmetamodel_Initialization", self)

    @property
    def OPLmetamodel_DataDeclaration40(self):
        return self.__OPLmetamodel_DataDeclaration40

    @OPLmetamodel_DataDeclaration40.setter
    def OPLmetamodel_DataDeclaration40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_DataDeclaration__OPLmetamodel_DataDeclaration40", None)
        self.__OPLmetamodel_DataDeclaration40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_Expression41"):
                opp_val = getattr(old_value, "OPLmetamodel_Expression41", None)
                if opp_val == self:
                    setattr(old_value, "OPLmetamodel_Expression41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_Expression41"):
                opp_val = getattr(value, "OPLmetamodel_Expression41", None)
                setattr(value, "OPLmetamodel_Expression41", self)

    @property
    def OPLmetamodel_DataDeclaration35(self):
        return self.__OPLmetamodel_DataDeclaration35

    @OPLmetamodel_DataDeclaration35.setter
    def OPLmetamodel_DataDeclaration35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_DataDeclaration__OPLmetamodel_DataDeclaration35", None)
        self.__OPLmetamodel_DataDeclaration35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_AbstractType36"):
                opp_val = getattr(old_value, "OPLmetamodel_AbstractType36", None)
                if opp_val == self:
                    setattr(old_value, "OPLmetamodel_AbstractType36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_AbstractType36"):
                opp_val = getattr(value, "OPLmetamodel_AbstractType36", None)
                setattr(value, "OPLmetamodel_AbstractType36", self)

    @property
    def OPLmetamodel_DataDeclaration97(self):
        return self.__OPLmetamodel_DataDeclaration97

    @OPLmetamodel_DataDeclaration97.setter
    def OPLmetamodel_DataDeclaration97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_DataDeclaration__OPLmetamodel_DataDeclaration97", None)
        self.__OPLmetamodel_DataDeclaration97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_Model96"):
                opp_val = getattr(old_value, "OPLmetamodel_Model96", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_Model96"):
                opp_val = getattr(value, "OPLmetamodel_Model96", None)
                if opp_val is None:
                    setattr(value, "OPLmetamodel_Model96", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OPLmetamodel_DataDeclaration(self):
        return self.__OPLmetamodel_DataDeclaration

    @OPLmetamodel_DataDeclaration.setter
    def OPLmetamodel_DataDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_DataDeclaration__OPLmetamodel_DataDeclaration", None)
        self.__OPLmetamodel_DataDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_DataRef33"):
                opp_val = getattr(old_value, "OPLmetamodel_DataRef33", None)
                if opp_val == self:
                    setattr(old_value, "OPLmetamodel_DataRef33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_DataRef33"):
                opp_val = getattr(value, "OPLmetamodel_DataRef33", None)
                setattr(value, "OPLmetamodel_DataRef33", self)

class OPLmetamodel_Script(Declaration):

    def __init__(self, isMain: bool, OPLmetamodel_Script: "OPLmetamodel_Model" = None, OPLmetamodel_Script158: "OPLmetamodel_Reference" = None, OPLmetamodel_Script161: set["OPLmetamodel_ScriptStatement"] = None):
        self.isMain = isMain
        self.OPLmetamodel_Script = OPLmetamodel_Script
        self.OPLmetamodel_Script158 = OPLmetamodel_Script158
        self.OPLmetamodel_Script161 = OPLmetamodel_Script161 if OPLmetamodel_Script161 is not None else set()
        
    @property
    def isMain(self) -> bool:
        return self.__isMain

    @isMain.setter
    def isMain(self, isMain: bool):
        self.__isMain = isMain

    @property
    def OPLmetamodel_Script(self):
        return self.__OPLmetamodel_Script

    @OPLmetamodel_Script.setter
    def OPLmetamodel_Script(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Script__OPLmetamodel_Script", None)
        self.__OPLmetamodel_Script = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_Model117"):
                opp_val = getattr(old_value, "OPLmetamodel_Model117", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_Model117"):
                opp_val = getattr(value, "OPLmetamodel_Model117", None)
                if opp_val is None:
                    setattr(value, "OPLmetamodel_Model117", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OPLmetamodel_Script158(self):
        return self.__OPLmetamodel_Script158

    @OPLmetamodel_Script158.setter
    def OPLmetamodel_Script158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Script__OPLmetamodel_Script158", None)
        self.__OPLmetamodel_Script158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_Reference159"):
                opp_val = getattr(old_value, "OPLmetamodel_Reference159", None)
                if opp_val == self:
                    setattr(old_value, "OPLmetamodel_Reference159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_Reference159"):
                opp_val = getattr(value, "OPLmetamodel_Reference159", None)
                setattr(value, "OPLmetamodel_Reference159", self)

    @property
    def OPLmetamodel_Script161(self):
        return self.__OPLmetamodel_Script161

    @OPLmetamodel_Script161.setter
    def OPLmetamodel_Script161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Script__OPLmetamodel_Script161", None)
        self.__OPLmetamodel_Script161 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OPLmetamodel_ScriptStatement"):
                    opp_val = getattr(item, "OPLmetamodel_ScriptStatement", None)
                    
                    if opp_val == self:
                        setattr(item, "OPLmetamodel_ScriptStatement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OPLmetamodel_ScriptStatement"):
                    opp_val = getattr(item, "OPLmetamodel_ScriptStatement", None)
                    
                    setattr(item, "OPLmetamodel_ScriptStatement", self)
                    

class OPLmetamodel_ScheduleInitialization(Declaration):

    pass
class OPLmetamodel_Setting(Declaration):

    pass
class OPLmetamodel_Assertion(Declaration):

    pass
class OPLmetamodel_Constraint(Declaration):

    def __init__(self, name: str, OPLmetamodel_Constraint: "OPLmetamodel_Assertion" = None, OPLmetamodel_Constraint30: "OPLmetamodel_Expression" = None, OPLmetamodel_Constraint60: "OPLmetamodel_ForAllConstraint" = None, OPLmetamodel_Constraint72: "OPLmetamodel_IfConstraint" = None, OPLmetamodel_Constraint75: "OPLmetamodel_IfConstraint" = None, OPLmetamodel_Constraint113: "OPLmetamodel_Model" = None, OPLmetamodel_Constraint100: "OPLmetamodel_Model" = None):
        self.name = name
        self.OPLmetamodel_Constraint = OPLmetamodel_Constraint
        self.OPLmetamodel_Constraint30 = OPLmetamodel_Constraint30
        self.OPLmetamodel_Constraint60 = OPLmetamodel_Constraint60
        self.OPLmetamodel_Constraint72 = OPLmetamodel_Constraint72
        self.OPLmetamodel_Constraint75 = OPLmetamodel_Constraint75
        self.OPLmetamodel_Constraint113 = OPLmetamodel_Constraint113
        self.OPLmetamodel_Constraint100 = OPLmetamodel_Constraint100
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def OPLmetamodel_Constraint30(self):
        return self.__OPLmetamodel_Constraint30

    @OPLmetamodel_Constraint30.setter
    def OPLmetamodel_Constraint30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Constraint__OPLmetamodel_Constraint30", None)
        self.__OPLmetamodel_Constraint30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_Expression31"):
                opp_val = getattr(old_value, "OPLmetamodel_Expression31", None)
                if opp_val == self:
                    setattr(old_value, "OPLmetamodel_Expression31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_Expression31"):
                opp_val = getattr(value, "OPLmetamodel_Expression31", None)
                setattr(value, "OPLmetamodel_Expression31", self)

    @property
    def OPLmetamodel_Constraint113(self):
        return self.__OPLmetamodel_Constraint113

    @OPLmetamodel_Constraint113.setter
    def OPLmetamodel_Constraint113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Constraint__OPLmetamodel_Constraint113", None)
        self.__OPLmetamodel_Constraint113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_Model112"):
                opp_val = getattr(old_value, "OPLmetamodel_Model112", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_Model112"):
                opp_val = getattr(value, "OPLmetamodel_Model112", None)
                if opp_val is None:
                    setattr(value, "OPLmetamodel_Model112", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OPLmetamodel_Constraint60(self):
        return self.__OPLmetamodel_Constraint60

    @OPLmetamodel_Constraint60.setter
    def OPLmetamodel_Constraint60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Constraint__OPLmetamodel_Constraint60", None)
        self.__OPLmetamodel_Constraint60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_ForAllConstraint59"):
                opp_val = getattr(old_value, "OPLmetamodel_ForAllConstraint59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_ForAllConstraint59"):
                opp_val = getattr(value, "OPLmetamodel_ForAllConstraint59", None)
                if opp_val is None:
                    setattr(value, "OPLmetamodel_ForAllConstraint59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OPLmetamodel_Constraint100(self):
        return self.__OPLmetamodel_Constraint100

    @OPLmetamodel_Constraint100.setter
    def OPLmetamodel_Constraint100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Constraint__OPLmetamodel_Constraint100", None)
        self.__OPLmetamodel_Constraint100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_Model99"):
                opp_val = getattr(old_value, "OPLmetamodel_Model99", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_Model99"):
                opp_val = getattr(value, "OPLmetamodel_Model99", None)
                if opp_val is None:
                    setattr(value, "OPLmetamodel_Model99", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OPLmetamodel_Constraint(self):
        return self.__OPLmetamodel_Constraint

    @OPLmetamodel_Constraint.setter
    def OPLmetamodel_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Constraint__OPLmetamodel_Constraint", None)
        self.__OPLmetamodel_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_Assertion"):
                opp_val = getattr(old_value, "OPLmetamodel_Assertion", None)
                if opp_val == self:
                    setattr(old_value, "OPLmetamodel_Assertion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_Assertion"):
                opp_val = getattr(value, "OPLmetamodel_Assertion", None)
                setattr(value, "OPLmetamodel_Assertion", self)

    @property
    def OPLmetamodel_Constraint72(self):
        return self.__OPLmetamodel_Constraint72

    @OPLmetamodel_Constraint72.setter
    def OPLmetamodel_Constraint72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Constraint__OPLmetamodel_Constraint72", None)
        self.__OPLmetamodel_Constraint72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_IfConstraint71"):
                opp_val = getattr(old_value, "OPLmetamodel_IfConstraint71", None)
                if opp_val == self:
                    setattr(old_value, "OPLmetamodel_IfConstraint71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_IfConstraint71"):
                opp_val = getattr(value, "OPLmetamodel_IfConstraint71", None)
                setattr(value, "OPLmetamodel_IfConstraint71", self)

    @property
    def OPLmetamodel_Constraint75(self):
        return self.__OPLmetamodel_Constraint75

    @OPLmetamodel_Constraint75.setter
    def OPLmetamodel_Constraint75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Constraint__OPLmetamodel_Constraint75", None)
        self.__OPLmetamodel_Constraint75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_IfConstraint74"):
                opp_val = getattr(old_value, "OPLmetamodel_IfConstraint74", None)
                if opp_val == self:
                    setattr(old_value, "OPLmetamodel_IfConstraint74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_IfConstraint74"):
                opp_val = getattr(value, "OPLmetamodel_IfConstraint74", None)
                setattr(value, "OPLmetamodel_IfConstraint74", self)

class OPLmetamodel_Objective(Declaration):

    def __init__(self, action: str, isLinearRelaxation: bool, OPLmetamodel_Objective: "OPLmetamodel_Model" = None, OPLmetamodel_Objective125: "OPLmetamodel_Expression" = None):
        self.action = action
        self.isLinearRelaxation = isLinearRelaxation
        self.OPLmetamodel_Objective = OPLmetamodel_Objective
        self.OPLmetamodel_Objective125 = OPLmetamodel_Objective125
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def isLinearRelaxation(self) -> bool:
        return self.__isLinearRelaxation

    @isLinearRelaxation.setter
    def isLinearRelaxation(self, isLinearRelaxation: bool):
        self.__isLinearRelaxation = isLinearRelaxation

    @property
    def OPLmetamodel_Objective125(self):
        return self.__OPLmetamodel_Objective125

    @OPLmetamodel_Objective125.setter
    def OPLmetamodel_Objective125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Objective__OPLmetamodel_Objective125", None)
        self.__OPLmetamodel_Objective125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_Expression126"):
                opp_val = getattr(old_value, "OPLmetamodel_Expression126", None)
                if opp_val == self:
                    setattr(old_value, "OPLmetamodel_Expression126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_Expression126"):
                opp_val = getattr(value, "OPLmetamodel_Expression126", None)
                setattr(value, "OPLmetamodel_Expression126", self)

    @property
    def OPLmetamodel_Objective(self):
        return self.__OPLmetamodel_Objective

    @OPLmetamodel_Objective.setter
    def OPLmetamodel_Objective(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_Objective__OPLmetamodel_Objective", None)
        self.__OPLmetamodel_Objective = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_Model102"):
                opp_val = getattr(old_value, "OPLmetamodel_Model102", None)
                if opp_val == self:
                    setattr(old_value, "OPLmetamodel_Model102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_Model102"):
                opp_val = getattr(value, "OPLmetamodel_Model102", None)
                setattr(value, "OPLmetamodel_Model102", self)

class OPLmetamodel_ActivityDeclaration(Declaration):

    def __init__(self, earliestStartTime: str, latestEndTime: str, OPLmetamodel_ActivityDeclaration: "OPLmetamodel_Number" = None, OPLmetamodel_ActivityDeclaration108: "OPLmetamodel_Model" = None):
        self.earliestStartTime = earliestStartTime
        self.latestEndTime = latestEndTime
        self.OPLmetamodel_ActivityDeclaration = OPLmetamodel_ActivityDeclaration
        self.OPLmetamodel_ActivityDeclaration108 = OPLmetamodel_ActivityDeclaration108
        
    @property
    def latestEndTime(self) -> str:
        return self.__latestEndTime

    @latestEndTime.setter
    def latestEndTime(self, latestEndTime: str):
        self.__latestEndTime = latestEndTime

    @property
    def earliestStartTime(self) -> str:
        return self.__earliestStartTime

    @earliestStartTime.setter
    def earliestStartTime(self, earliestStartTime: str):
        self.__earliestStartTime = earliestStartTime

    @property
    def OPLmetamodel_ActivityDeclaration108(self):
        return self.__OPLmetamodel_ActivityDeclaration108

    @OPLmetamodel_ActivityDeclaration108.setter
    def OPLmetamodel_ActivityDeclaration108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_ActivityDeclaration__OPLmetamodel_ActivityDeclaration108", None)
        self.__OPLmetamodel_ActivityDeclaration108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_Model107"):
                opp_val = getattr(old_value, "OPLmetamodel_Model107", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_Model107"):
                opp_val = getattr(value, "OPLmetamodel_Model107", None)
                if opp_val is None:
                    setattr(value, "OPLmetamodel_Model107", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OPLmetamodel_ActivityDeclaration(self):
        return self.__OPLmetamodel_ActivityDeclaration

    @OPLmetamodel_ActivityDeclaration.setter
    def OPLmetamodel_ActivityDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OPLmetamodel_ActivityDeclaration__OPLmetamodel_ActivityDeclaration", None)
        self.__OPLmetamodel_ActivityDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OPLmetamodel_Number"):
                opp_val = getattr(old_value, "OPLmetamodel_Number", None)
                if opp_val == self:
                    setattr(old_value, "OPLmetamodel_Number", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OPLmetamodel_Number"):
                opp_val = getattr(value, "OPLmetamodel_Number", None)
                setattr(value, "OPLmetamodel_Number", self)

class OPLmetamodel_AbstractType(ABC):

    pass
class OPLmetamodel_AbstractBinaryOperator(ABC):

    pass
class OPLmetamodel_AllExpression:

    pass
class OPLmetamodel_Expression(ABC):

    pass