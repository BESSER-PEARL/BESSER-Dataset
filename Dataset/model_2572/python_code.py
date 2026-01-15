from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class XFunction(Enum):
    xin = "xin"
    xnotin = "xnotin"
    xeq = "xeq"
    xnoteq = "xnoteq"
    xls = "xls"
    xgt = "xgt"
    xlsr = "xlsr"
    xgtl = "xgtl"
    xbwn = "xbwn"
    xbwnc = "xbwnc"
    xbwnl = "xbwnl"
    xbwnr = "xbwnr"
class EXTRACT_VALUES(Enum):
    hms = "hms"
    hs = "hs"
    ms = "ms"
    s = "s"
    m = "m"
    h = "h"
    day = "day"
    week = "week"
    month = "month"
    quart = "quart"
    year = "year"
    micros = "micros"
    minMicro = "minMicro"
    minSec = "minSec"
    hmin = "hmin"
    dms = "dms"
    ds = "ds"
    daymin = "daymin"
    dayh = "dayh"
    yearMonth = "yearMonth"


############################################
# Definition of Classes
############################################

class Operands:

    pass
class sql_Minus(Operands):

    pass
class sql_Star(Operands):

    pass
class sql_Div(Operands):

    pass
class sql_Concat(Operands):

    pass
class sql_Plus(Operands):

    pass
class UnpivotInClause:

    pass
class sql_UnipivotInClause(UnpivotInClause):

    def __init__(self, op: str, sql_UnipivotInClause: "sql_UnpivotInClauseArgs" = None):
        self.op = op
        self.sql_UnipivotInClause = sql_UnipivotInClause
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def sql_UnipivotInClause(self):
        return self.__sql_UnipivotInClause

    @sql_UnipivotInClause.setter
    def sql_UnipivotInClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_UnipivotInClause__sql_UnipivotInClause", None)
        self.__sql_UnipivotInClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_UnpivotInClauseArgs254"):
                opp_val = getattr(old_value, "sql_UnpivotInClauseArgs254", None)
                if opp_val == self:
                    setattr(old_value, "sql_UnpivotInClauseArgs254", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_UnpivotInClauseArgs254"):
                opp_val = getattr(value, "sql_UnpivotInClauseArgs254", None)
                setattr(value, "sql_UnpivotInClauseArgs254", self)

class SQLCaseWhens:

    pass
class sql_WhenList(SQLCaseWhens):

    pass
class sql_SqlCaseWhen(SQLCaseWhens):

    pass
class sql_SQLCaseWhens:

    pass
class OperandList:

    pass
class sql_OpList(OperandList):

    pass
class sql_OpFunctionArgAgregate:

    pass
class OpFunctionArg:

    pass
class sql_OpFList(OpFunctionArg):

    pass
class sql_OpFunctionArgOperand(OpFunctionArg):

    pass
class AnalyticExprArgs:

    pass
class sql_AExpArgs(AnalyticExprArgs):

    pass
class QueryPartitionClause:

    pass
class sql_AnalyticExprArgs(QueryPartitionClause):

    pass
class OrderByClauseArgs:

    pass
class sql_OBCArgs(OrderByClauseArgs):

    pass
class sql_OrderByClauseArg(OrderByClauseArgs):

    pass
class sql_AnalyticExprArg(AnalyticExprArgs):

    pass
class sql_WindowingClauseOperandFollowing:

    pass
class WindowingClause:

    pass
class sql_WindowingClauseOperandPreceding(WindowingClause):

    pass
class sql_WindowingClauseBetween(WindowingClause):

    pass
class sql_WindowingClause:

    pass
class sql_OrderByClause:

    pass
class sql_QueryPartitionClause:

    pass
class sql_OrderByClauseArgs:

    pass
class sql_FunctionAnalytical:

    pass
class sql_OpFunctionArg:

    pass
class sql_FunctionExtract:

    def __init__(self, v: str, sql_FunctionExtract198: "sql_Operands" = None, sql_FunctionExtract: "sql_Operand" = None):
        self.v = v
        self.sql_FunctionExtract198 = sql_FunctionExtract198
        self.sql_FunctionExtract = sql_FunctionExtract
        
    @property
    def v(self) -> str:
        return self.__v

    @v.setter
    def v(self, v: str):
        self.__v = v

    @property
    def sql_FunctionExtract(self):
        return self.__sql_FunctionExtract

    @sql_FunctionExtract.setter
    def sql_FunctionExtract(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FunctionExtract__sql_FunctionExtract", None)
        self.__sql_FunctionExtract = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operand180"):
                opp_val = getattr(old_value, "sql_Operand180", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operand180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operand180"):
                opp_val = getattr(value, "sql_Operand180", None)
                setattr(value, "sql_Operand180", self)

    @property
    def sql_FunctionExtract198(self):
        return self.__sql_FunctionExtract198

    @sql_FunctionExtract198.setter
    def sql_FunctionExtract198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FunctionExtract__sql_FunctionExtract198", None)
        self.__sql_FunctionExtract198 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operands199"):
                opp_val = getattr(old_value, "sql_Operands199", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operands199", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operands199"):
                opp_val = getattr(value, "sql_Operands199", None)
                setattr(value, "sql_Operands199", self)

class sql_ScalarOperand(OperandList):

    def __init__(self, soint: int, sostr: str, sodbl: str, sodate: date, sotime: date, sodt: date, sql_ScalarOperand: "sql_Operand" = None, sql_ScalarOperand263: "sql_OpList" = None):
        self.soint = soint
        self.sostr = sostr
        self.sodbl = sodbl
        self.sodate = sodate
        self.sotime = sotime
        self.sodt = sodt
        self.sql_ScalarOperand = sql_ScalarOperand
        self.sql_ScalarOperand263 = sql_ScalarOperand263
        
    @property
    def sodate(self) -> date:
        return self.__sodate

    @sodate.setter
    def sodate(self, sodate: date):
        self.__sodate = sodate

    @property
    def sotime(self) -> date:
        return self.__sotime

    @sotime.setter
    def sotime(self, sotime: date):
        self.__sotime = sotime

    @property
    def sodt(self) -> date:
        return self.__sodt

    @sodt.setter
    def sodt(self, sodt: date):
        self.__sodt = sodt

    @property
    def sostr(self) -> str:
        return self.__sostr

    @sostr.setter
    def sostr(self, sostr: str):
        self.__sostr = sostr

    @property
    def sodbl(self) -> str:
        return self.__sodbl

    @sodbl.setter
    def sodbl(self, sodbl: str):
        self.__sodbl = sodbl

    @property
    def soint(self) -> int:
        return self.__soint

    @soint.setter
    def soint(self, soint: int):
        self.__soint = soint

    @property
    def sql_ScalarOperand263(self):
        return self.__sql_ScalarOperand263

    @sql_ScalarOperand263.setter
    def sql_ScalarOperand263(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ScalarOperand__sql_ScalarOperand263", None)
        self.__sql_ScalarOperand263 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_OpList"):
                opp_val = getattr(old_value, "sql_OpList", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OpList"):
                opp_val = getattr(value, "sql_OpList", None)
                if opp_val is None:
                    setattr(value, "sql_OpList", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sql_ScalarOperand(self):
        return self.__sql_ScalarOperand

    @sql_ScalarOperand.setter
    def sql_ScalarOperand(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ScalarOperand__sql_ScalarOperand", None)
        self.__sql_ScalarOperand = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operand192"):
                opp_val = getattr(old_value, "sql_Operand192", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operand192", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operand192"):
                opp_val = getattr(value, "sql_Operand192", None)
                setattr(value, "sql_Operand192", self)

class sql_ExpOperand:

    def __init__(self, prm: str, sql_ExpOperand: "sql_Operand" = None):
        self.prm = prm
        self.sql_ExpOperand = sql_ExpOperand
        
    @property
    def prm(self) -> str:
        return self.__prm

    @prm.setter
    def prm(self, prm: str):
        self.__prm = prm

    @property
    def sql_ExpOperand(self):
        return self.__sql_ExpOperand

    @sql_ExpOperand.setter
    def sql_ExpOperand(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ExpOperand__sql_ExpOperand", None)
        self.__sql_ExpOperand = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operand190"):
                opp_val = getattr(old_value, "sql_Operand190", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operand190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operand190"):
                opp_val = getattr(value, "sql_Operand190", None)
                setattr(value, "sql_Operand190", self)

class sql_SQLCaseOperand:

    pass
class sql_ColumnOperand:

    def __init__(self, ora: str, sql_ColumnOperand: "sql_Operand" = None, sql_ColumnOperand233: "sql_ColumnFull" = None):
        self.ora = ora
        self.sql_ColumnOperand = sql_ColumnOperand
        self.sql_ColumnOperand233 = sql_ColumnOperand233
        
    @property
    def ora(self) -> str:
        return self.__ora

    @ora.setter
    def ora(self, ora: str):
        self.__ora = ora

    @property
    def sql_ColumnOperand233(self):
        return self.__sql_ColumnOperand233

    @sql_ColumnOperand233.setter
    def sql_ColumnOperand233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ColumnOperand__sql_ColumnOperand233", None)
        self.__sql_ColumnOperand233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_ColumnFull234"):
                opp_val = getattr(old_value, "sql_ColumnFull234", None)
                if opp_val == self:
                    setattr(old_value, "sql_ColumnFull234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_ColumnFull234"):
                opp_val = getattr(value, "sql_ColumnFull234", None)
                setattr(value, "sql_ColumnFull234", self)

    @property
    def sql_ColumnOperand(self):
        return self.__sql_ColumnOperand

    @sql_ColumnOperand.setter
    def sql_ColumnOperand(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ColumnOperand__sql_ColumnOperand", None)
        self.__sql_ColumnOperand = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operand169"):
                opp_val = getattr(old_value, "sql_Operand169", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operand169", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operand169"):
                opp_val = getattr(value, "sql_Operand169", None)
                setattr(value, "sql_Operand169", self)

class sql_AnalyticClause:

    pass
class sql_OperandList:

    pass
class sql_OperandListGroup:

    pass
class sql_Operand:

    pass
class OpFunctionArgAgregate:

    pass
class sql_OpFunctionCast:

    def __init__(self, type: str, p: int, p2: int, sql_OpFunctionCast: "sql_LikeOperand" = None, sql_OpFunctionCast178: "sql_Operand" = None, sql_OpFunctionCast230: "sql_Operands" = None):
        self.type = type
        self.p = p
        self.p2 = p2
        self.sql_OpFunctionCast = sql_OpFunctionCast
        self.sql_OpFunctionCast178 = sql_OpFunctionCast178
        self.sql_OpFunctionCast230 = sql_OpFunctionCast230
        
    @property
    def p2(self) -> int:
        return self.__p2

    @p2.setter
    def p2(self, p2: int):
        self.__p2 = p2

    @property
    def p(self) -> int:
        return self.__p

    @p.setter
    def p(self, p: int):
        self.__p = p

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def sql_OpFunctionCast230(self):
        return self.__sql_OpFunctionCast230

    @sql_OpFunctionCast230.setter
    def sql_OpFunctionCast230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_OpFunctionCast__sql_OpFunctionCast230", None)
        self.__sql_OpFunctionCast230 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operands231"):
                opp_val = getattr(old_value, "sql_Operands231", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operands231", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operands231"):
                opp_val = getattr(value, "sql_Operands231", None)
                setattr(value, "sql_Operands231", self)

    @property
    def sql_OpFunctionCast(self):
        return self.__sql_OpFunctionCast

    @sql_OpFunctionCast.setter
    def sql_OpFunctionCast(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_OpFunctionCast__sql_OpFunctionCast", None)
        self.__sql_OpFunctionCast = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_LikeOperand138"):
                opp_val = getattr(old_value, "sql_LikeOperand138", None)
                if opp_val == self:
                    setattr(old_value, "sql_LikeOperand138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_LikeOperand138"):
                opp_val = getattr(value, "sql_LikeOperand138", None)
                setattr(value, "sql_LikeOperand138", self)

    @property
    def sql_OpFunctionCast178(self):
        return self.__sql_OpFunctionCast178

    @sql_OpFunctionCast178.setter
    def sql_OpFunctionCast178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_OpFunctionCast__sql_OpFunctionCast178", None)
        self.__sql_OpFunctionCast178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operand177"):
                opp_val = getattr(old_value, "sql_Operand177", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operand177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operand177"):
                opp_val = getattr(value, "sql_Operand177", None)
                setattr(value, "sql_Operand177", self)

class sql_LikeOperand:

    def __init__(self, op2: str, sql_LikeOperand140: "sql_POperand" = None, sql_LikeOperand: "sql_Like" = None, sql_LikeOperand135: "sql_OpFunction" = None, sql_LikeOperand138: "sql_OpFunctionCast" = None):
        self.op2 = op2
        self.sql_LikeOperand140 = sql_LikeOperand140
        self.sql_LikeOperand = sql_LikeOperand
        self.sql_LikeOperand135 = sql_LikeOperand135
        self.sql_LikeOperand138 = sql_LikeOperand138
        
    @property
    def op2(self) -> str:
        return self.__op2

    @op2.setter
    def op2(self, op2: str):
        self.__op2 = op2

    @property
    def sql_LikeOperand140(self):
        return self.__sql_LikeOperand140

    @sql_LikeOperand140.setter
    def sql_LikeOperand140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_LikeOperand__sql_LikeOperand140", None)
        self.__sql_LikeOperand140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_POperand"):
                opp_val = getattr(old_value, "sql_POperand", None)
                if opp_val == self:
                    setattr(old_value, "sql_POperand", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_POperand"):
                opp_val = getattr(value, "sql_POperand", None)
                setattr(value, "sql_POperand", self)

    @property
    def sql_LikeOperand138(self):
        return self.__sql_LikeOperand138

    @sql_LikeOperand138.setter
    def sql_LikeOperand138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_LikeOperand__sql_LikeOperand138", None)
        self.__sql_LikeOperand138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_OpFunctionCast"):
                opp_val = getattr(old_value, "sql_OpFunctionCast", None)
                if opp_val == self:
                    setattr(old_value, "sql_OpFunctionCast", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OpFunctionCast"):
                opp_val = getattr(value, "sql_OpFunctionCast", None)
                setattr(value, "sql_OpFunctionCast", self)

    @property
    def sql_LikeOperand(self):
        return self.__sql_LikeOperand

    @sql_LikeOperand.setter
    def sql_LikeOperand(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_LikeOperand__sql_LikeOperand", None)
        self.__sql_LikeOperand = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Like133"):
                opp_val = getattr(old_value, "sql_Like133", None)
                if opp_val == self:
                    setattr(old_value, "sql_Like133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Like133"):
                opp_val = getattr(value, "sql_Like133", None)
                setattr(value, "sql_Like133", self)

    @property
    def sql_LikeOperand135(self):
        return self.__sql_LikeOperand135

    @sql_LikeOperand135.setter
    def sql_LikeOperand135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_LikeOperand__sql_LikeOperand135", None)
        self.__sql_LikeOperand135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_OpFunction136"):
                opp_val = getattr(old_value, "sql_OpFunction136", None)
                if opp_val == self:
                    setattr(old_value, "sql_OpFunction136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OpFunction136"):
                opp_val = getattr(value, "sql_OpFunction136", None)
                setattr(value, "sql_OpFunction136", self)

class sql_POperand:

    def __init__(self, prm: str, sql_POperand: "sql_LikeOperand" = None, sql_POperand188: "sql_Operand" = None):
        self.prm = prm
        self.sql_POperand = sql_POperand
        self.sql_POperand188 = sql_POperand188
        
    @property
    def prm(self) -> str:
        return self.__prm

    @prm.setter
    def prm(self, prm: str):
        self.__prm = prm

    @property
    def sql_POperand(self):
        return self.__sql_POperand

    @sql_POperand.setter
    def sql_POperand(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_POperand__sql_POperand", None)
        self.__sql_POperand = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_LikeOperand140"):
                opp_val = getattr(old_value, "sql_LikeOperand140", None)
                if opp_val == self:
                    setattr(old_value, "sql_LikeOperand140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_LikeOperand140"):
                opp_val = getattr(value, "sql_LikeOperand140", None)
                setattr(value, "sql_LikeOperand140", self)

    @property
    def sql_POperand188(self):
        return self.__sql_POperand188

    @sql_POperand188.setter
    def sql_POperand188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_POperand__sql_POperand188", None)
        self.__sql_POperand188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operand187"):
                opp_val = getattr(old_value, "sql_Operand187", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operand187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operand187"):
                opp_val = getattr(value, "sql_Operand187", None)
                setattr(value, "sql_Operand187", self)

class sql_Comparison:

    def __init__(self, operator: str, subOperator: str, sql_Comparison: "sql_FullExpression" = None, sql_Comparison130: "sql_Operands" = None):
        self.operator = operator
        self.subOperator = subOperator
        self.sql_Comparison = sql_Comparison
        self.sql_Comparison130 = sql_Comparison130
        
    @property
    def subOperator(self) -> str:
        return self.__subOperator

    @subOperator.setter
    def subOperator(self, subOperator: str):
        self.__subOperator = subOperator

    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def sql_Comparison130(self):
        return self.__sql_Comparison130

    @sql_Comparison130.setter
    def sql_Comparison130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Comparison__sql_Comparison130", None)
        self.__sql_Comparison130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operands131"):
                opp_val = getattr(old_value, "sql_Operands131", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operands131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operands131"):
                opp_val = getattr(value, "sql_Operands131", None)
                setattr(value, "sql_Operands131", self)

    @property
    def sql_Comparison(self):
        return self.__sql_Comparison

    @sql_Comparison.setter
    def sql_Comparison(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Comparison__sql_Comparison", None)
        self.__sql_Comparison = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FullExpression118"):
                opp_val = getattr(old_value, "sql_FullExpression118", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression118"):
                opp_val = getattr(value, "sql_FullExpression118", None)
                setattr(value, "sql_FullExpression118", self)

class sql_Like:

    def __init__(self, opLike: str, sql_Like: "sql_FullExpression" = None, sql_Like133: "sql_LikeOperand" = None):
        self.opLike = opLike
        self.sql_Like = sql_Like
        self.sql_Like133 = sql_Like133
        
    @property
    def opLike(self) -> str:
        return self.__opLike

    @opLike.setter
    def opLike(self, opLike: str):
        self.__opLike = opLike

    @property
    def sql_Like(self):
        return self.__sql_Like

    @sql_Like.setter
    def sql_Like(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Like__sql_Like", None)
        self.__sql_Like = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FullExpression116"):
                opp_val = getattr(old_value, "sql_FullExpression116", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression116"):
                opp_val = getattr(value, "sql_FullExpression116", None)
                setattr(value, "sql_FullExpression116", self)

    @property
    def sql_Like133(self):
        return self.__sql_Like133

    @sql_Like133.setter
    def sql_Like133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Like__sql_Like133", None)
        self.__sql_Like133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_LikeOperand"):
                opp_val = getattr(old_value, "sql_LikeOperand", None)
                if opp_val == self:
                    setattr(old_value, "sql_LikeOperand", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_LikeOperand"):
                opp_val = getattr(value, "sql_LikeOperand", None)
                setattr(value, "sql_LikeOperand", self)

class Prms:

    pass
class sql_JRParameter(Prms):

    def __init__(self, jrprm: str, sql_JRParameter: "sql_Prms" = None):
        self.jrprm = jrprm
        self.sql_JRParameter = sql_JRParameter
        
    @property
    def jrprm(self) -> str:
        return self.__jrprm

    @jrprm.setter
    def jrprm(self, jrprm: str):
        self.__jrprm = jrprm

    @property
    def sql_JRParameter(self):
        return self.__sql_JRParameter

    @sql_JRParameter.setter
    def sql_JRParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_JRParameter__sql_JRParameter", None)
        self.__sql_JRParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Prms128"):
                opp_val = getattr(old_value, "sql_Prms128", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Prms128"):
                opp_val = getattr(value, "sql_Prms128", None)
                if opp_val is None:
                    setattr(value, "sql_Prms128", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sql_Prms:

    pass
class sql_ExprGroup:

    def __init__(self, isnot: str, sql_ExprGroup: "sql_FullExpression" = None, sql_ExprGroup120: "sql_OrExpr" = None):
        self.isnot = isnot
        self.sql_ExprGroup = sql_ExprGroup
        self.sql_ExprGroup120 = sql_ExprGroup120
        
    @property
    def isnot(self) -> str:
        return self.__isnot

    @isnot.setter
    def isnot(self, isnot: str):
        self.__isnot = isnot

    @property
    def sql_ExprGroup(self):
        return self.__sql_ExprGroup

    @sql_ExprGroup.setter
    def sql_ExprGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ExprGroup__sql_ExprGroup", None)
        self.__sql_ExprGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FullExpression100"):
                opp_val = getattr(old_value, "sql_FullExpression100", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression100"):
                opp_val = getattr(value, "sql_FullExpression100", None)
                setattr(value, "sql_FullExpression100", self)

    @property
    def sql_ExprGroup120(self):
        return self.__sql_ExprGroup120

    @sql_ExprGroup120.setter
    def sql_ExprGroup120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ExprGroup__sql_ExprGroup120", None)
        self.__sql_ExprGroup120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_OrExpr121"):
                opp_val = getattr(old_value, "sql_OrExpr121", None)
                if opp_val == self:
                    setattr(old_value, "sql_OrExpr121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OrExpr121"):
                opp_val = getattr(value, "sql_OrExpr121", None)
                setattr(value, "sql_OrExpr121", self)

class OrExpr:

    pass
class sql_FullExpression(OrExpr):

    def __init__(self, isnull: str, c: str, notPrm: str, sql_FullExpression105: "sql_XExpr" = None, sql_FullExpression107: "sql_InOper" = None, sql_FullExpression109: "sql_ExistsOper" = None, sql_FullExpression111: "sql_Operands" = None, sql_FullExpression114: "sql_Between" = None, sql_FullExpression: "sql_OrExpr" = None, sql_FullExpression98: "sql_FullExpression" = None, sql_FullExpression96: "sql_FullExpression" = None, sql_FullExpression100: "sql_ExprGroup" = None, sql_FullExpression103: "sql_FullExpression" = None, sql_FullExpression101: "sql_FullExpression" = None, sql_FullExpression116: "sql_Like" = None, sql_FullExpression118: "sql_Comparison" = None):
        self.isnull = isnull
        self.c = c
        self.notPrm = notPrm
        self.sql_FullExpression105 = sql_FullExpression105
        self.sql_FullExpression107 = sql_FullExpression107
        self.sql_FullExpression109 = sql_FullExpression109
        self.sql_FullExpression111 = sql_FullExpression111
        self.sql_FullExpression114 = sql_FullExpression114
        self.sql_FullExpression = sql_FullExpression
        self.sql_FullExpression98 = sql_FullExpression98
        self.sql_FullExpression96 = sql_FullExpression96
        self.sql_FullExpression100 = sql_FullExpression100
        self.sql_FullExpression103 = sql_FullExpression103
        self.sql_FullExpression101 = sql_FullExpression101
        self.sql_FullExpression116 = sql_FullExpression116
        self.sql_FullExpression118 = sql_FullExpression118
        
    @property
    def isnull(self) -> str:
        return self.__isnull

    @isnull.setter
    def isnull(self, isnull: str):
        self.__isnull = isnull

    @property
    def c(self) -> str:
        return self.__c

    @c.setter
    def c(self, c: str):
        self.__c = c

    @property
    def notPrm(self) -> str:
        return self.__notPrm

    @notPrm.setter
    def notPrm(self, notPrm: str):
        self.__notPrm = notPrm

    @property
    def sql_FullExpression100(self):
        return self.__sql_FullExpression100

    @sql_FullExpression100.setter
    def sql_FullExpression100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression100", None)
        self.__sql_FullExpression100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_ExprGroup"):
                opp_val = getattr(old_value, "sql_ExprGroup", None)
                if opp_val == self:
                    setattr(old_value, "sql_ExprGroup", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_ExprGroup"):
                opp_val = getattr(value, "sql_ExprGroup", None)
                setattr(value, "sql_ExprGroup", self)

    @property
    def sql_FullExpression101(self):
        return self.__sql_FullExpression101

    @sql_FullExpression101.setter
    def sql_FullExpression101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression101", None)
        self.__sql_FullExpression101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FullExpression103"):
                opp_val = getattr(old_value, "sql_FullExpression103", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression103"):
                opp_val = getattr(value, "sql_FullExpression103", None)
                setattr(value, "sql_FullExpression103", self)

    @property
    def sql_FullExpression(self):
        return self.__sql_FullExpression

    @sql_FullExpression.setter
    def sql_FullExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression", None)
        self.__sql_FullExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_OrExpr95"):
                opp_val = getattr(old_value, "sql_OrExpr95", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OrExpr95"):
                opp_val = getattr(value, "sql_OrExpr95", None)
                if opp_val is None:
                    setattr(value, "sql_OrExpr95", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sql_FullExpression114(self):
        return self.__sql_FullExpression114

    @sql_FullExpression114.setter
    def sql_FullExpression114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression114", None)
        self.__sql_FullExpression114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Between"):
                opp_val = getattr(old_value, "sql_Between", None)
                if opp_val == self:
                    setattr(old_value, "sql_Between", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Between"):
                opp_val = getattr(value, "sql_Between", None)
                setattr(value, "sql_Between", self)

    @property
    def sql_FullExpression109(self):
        return self.__sql_FullExpression109

    @sql_FullExpression109.setter
    def sql_FullExpression109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression109", None)
        self.__sql_FullExpression109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_ExistsOper"):
                opp_val = getattr(old_value, "sql_ExistsOper", None)
                if opp_val == self:
                    setattr(old_value, "sql_ExistsOper", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_ExistsOper"):
                opp_val = getattr(value, "sql_ExistsOper", None)
                setattr(value, "sql_ExistsOper", self)

    @property
    def sql_FullExpression98(self):
        return self.__sql_FullExpression98

    @sql_FullExpression98.setter
    def sql_FullExpression98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression98", None)
        self.__sql_FullExpression98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FullExpression96"):
                opp_val = getattr(old_value, "sql_FullExpression96", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression96"):
                opp_val = getattr(value, "sql_FullExpression96", None)
                setattr(value, "sql_FullExpression96", self)

    @property
    def sql_FullExpression107(self):
        return self.__sql_FullExpression107

    @sql_FullExpression107.setter
    def sql_FullExpression107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression107", None)
        self.__sql_FullExpression107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_InOper"):
                opp_val = getattr(old_value, "sql_InOper", None)
                if opp_val == self:
                    setattr(old_value, "sql_InOper", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_InOper"):
                opp_val = getattr(value, "sql_InOper", None)
                setattr(value, "sql_InOper", self)

    @property
    def sql_FullExpression96(self):
        return self.__sql_FullExpression96

    @sql_FullExpression96.setter
    def sql_FullExpression96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression96", None)
        self.__sql_FullExpression96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FullExpression98"):
                opp_val = getattr(old_value, "sql_FullExpression98", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression98"):
                opp_val = getattr(value, "sql_FullExpression98", None)
                setattr(value, "sql_FullExpression98", self)

    @property
    def sql_FullExpression116(self):
        return self.__sql_FullExpression116

    @sql_FullExpression116.setter
    def sql_FullExpression116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression116", None)
        self.__sql_FullExpression116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Like"):
                opp_val = getattr(old_value, "sql_Like", None)
                if opp_val == self:
                    setattr(old_value, "sql_Like", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Like"):
                opp_val = getattr(value, "sql_Like", None)
                setattr(value, "sql_Like", self)

    @property
    def sql_FullExpression111(self):
        return self.__sql_FullExpression111

    @sql_FullExpression111.setter
    def sql_FullExpression111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression111", None)
        self.__sql_FullExpression111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operands112"):
                opp_val = getattr(old_value, "sql_Operands112", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operands112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operands112"):
                opp_val = getattr(value, "sql_Operands112", None)
                setattr(value, "sql_Operands112", self)

    @property
    def sql_FullExpression105(self):
        return self.__sql_FullExpression105

    @sql_FullExpression105.setter
    def sql_FullExpression105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression105", None)
        self.__sql_FullExpression105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_XExpr"):
                opp_val = getattr(old_value, "sql_XExpr", None)
                if opp_val == self:
                    setattr(old_value, "sql_XExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_XExpr"):
                opp_val = getattr(value, "sql_XExpr", None)
                setattr(value, "sql_XExpr", self)

    @property
    def sql_FullExpression103(self):
        return self.__sql_FullExpression103

    @sql_FullExpression103.setter
    def sql_FullExpression103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression103", None)
        self.__sql_FullExpression103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FullExpression101"):
                opp_val = getattr(old_value, "sql_FullExpression101", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression101"):
                opp_val = getattr(value, "sql_FullExpression101", None)
                setattr(value, "sql_FullExpression101", self)

    @property
    def sql_FullExpression118(self):
        return self.__sql_FullExpression118

    @sql_FullExpression118.setter
    def sql_FullExpression118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression118", None)
        self.__sql_FullExpression118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Comparison"):
                opp_val = getattr(old_value, "sql_Comparison", None)
                if opp_val == self:
                    setattr(old_value, "sql_Comparison", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Comparison"):
                opp_val = getattr(value, "sql_Comparison", None)
                setattr(value, "sql_Comparison", self)

class sql_Between:

    def __init__(self, opBetween: str, sql_Between: "sql_FullExpression" = None, sql_Between142: "sql_Operands" = None, sql_Between145: "sql_Operands" = None):
        self.opBetween = opBetween
        self.sql_Between = sql_Between
        self.sql_Between142 = sql_Between142
        self.sql_Between145 = sql_Between145
        
    @property
    def opBetween(self) -> str:
        return self.__opBetween

    @opBetween.setter
    def opBetween(self, opBetween: str):
        self.__opBetween = opBetween

    @property
    def sql_Between(self):
        return self.__sql_Between

    @sql_Between.setter
    def sql_Between(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Between__sql_Between", None)
        self.__sql_Between = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FullExpression114"):
                opp_val = getattr(old_value, "sql_FullExpression114", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression114"):
                opp_val = getattr(value, "sql_FullExpression114", None)
                setattr(value, "sql_FullExpression114", self)

    @property
    def sql_Between142(self):
        return self.__sql_Between142

    @sql_Between142.setter
    def sql_Between142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Between__sql_Between142", None)
        self.__sql_Between142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operands143"):
                opp_val = getattr(old_value, "sql_Operands143", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operands143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operands143"):
                opp_val = getattr(value, "sql_Operands143", None)
                setattr(value, "sql_Operands143", self)

    @property
    def sql_Between145(self):
        return self.__sql_Between145

    @sql_Between145.setter
    def sql_Between145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Between__sql_Between145", None)
        self.__sql_Between145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operands146"):
                opp_val = getattr(old_value, "sql_Operands146", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operands146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operands146"):
                opp_val = getattr(value, "sql_Operands146", None)
                setattr(value, "sql_Operands146", self)

class sql_ExistsOper:

    def __init__(self, op: str, sql_ExistsOper: "sql_FullExpression" = None, sql_ExistsOper153: "sql_SubQueryOperand" = None, sql_ExistsOper156: "sql_OperandListGroup" = None):
        self.op = op
        self.sql_ExistsOper = sql_ExistsOper
        self.sql_ExistsOper153 = sql_ExistsOper153
        self.sql_ExistsOper156 = sql_ExistsOper156
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def sql_ExistsOper153(self):
        return self.__sql_ExistsOper153

    @sql_ExistsOper153.setter
    def sql_ExistsOper153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ExistsOper__sql_ExistsOper153", None)
        self.__sql_ExistsOper153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_SubQueryOperand154"):
                opp_val = getattr(old_value, "sql_SubQueryOperand154", None)
                if opp_val == self:
                    setattr(old_value, "sql_SubQueryOperand154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_SubQueryOperand154"):
                opp_val = getattr(value, "sql_SubQueryOperand154", None)
                setattr(value, "sql_SubQueryOperand154", self)

    @property
    def sql_ExistsOper(self):
        return self.__sql_ExistsOper

    @sql_ExistsOper.setter
    def sql_ExistsOper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ExistsOper__sql_ExistsOper", None)
        self.__sql_ExistsOper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FullExpression109"):
                opp_val = getattr(old_value, "sql_FullExpression109", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression109"):
                opp_val = getattr(value, "sql_FullExpression109", None)
                setattr(value, "sql_FullExpression109", self)

    @property
    def sql_ExistsOper156(self):
        return self.__sql_ExistsOper156

    @sql_ExistsOper156.setter
    def sql_ExistsOper156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ExistsOper__sql_ExistsOper156", None)
        self.__sql_ExistsOper156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_OperandListGroup157"):
                opp_val = getattr(old_value, "sql_OperandListGroup157", None)
                if opp_val == self:
                    setattr(old_value, "sql_OperandListGroup157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OperandListGroup157"):
                opp_val = getattr(value, "sql_OperandListGroup157", None)
                setattr(value, "sql_OperandListGroup157", self)

class sql_InOper:

    def __init__(self, op: str, sql_InOper: "sql_FullExpression" = None, sql_InOper148: "sql_SubQueryOperand" = None, sql_InOper151: "sql_OperandListGroup" = None):
        self.op = op
        self.sql_InOper = sql_InOper
        self.sql_InOper148 = sql_InOper148
        self.sql_InOper151 = sql_InOper151
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def sql_InOper151(self):
        return self.__sql_InOper151

    @sql_InOper151.setter
    def sql_InOper151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_InOper__sql_InOper151", None)
        self.__sql_InOper151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_OperandListGroup"):
                opp_val = getattr(old_value, "sql_OperandListGroup", None)
                if opp_val == self:
                    setattr(old_value, "sql_OperandListGroup", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OperandListGroup"):
                opp_val = getattr(value, "sql_OperandListGroup", None)
                setattr(value, "sql_OperandListGroup", self)

    @property
    def sql_InOper(self):
        return self.__sql_InOper

    @sql_InOper.setter
    def sql_InOper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_InOper__sql_InOper", None)
        self.__sql_InOper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FullExpression107"):
                opp_val = getattr(old_value, "sql_FullExpression107", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression107"):
                opp_val = getattr(value, "sql_FullExpression107", None)
                setattr(value, "sql_FullExpression107", self)

    @property
    def sql_InOper148(self):
        return self.__sql_InOper148

    @sql_InOper148.setter
    def sql_InOper148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_InOper__sql_InOper148", None)
        self.__sql_InOper148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_SubQueryOperand149"):
                opp_val = getattr(old_value, "sql_SubQueryOperand149", None)
                if opp_val == self:
                    setattr(old_value, "sql_SubQueryOperand149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_SubQueryOperand149"):
                opp_val = getattr(value, "sql_SubQueryOperand149", None)
                setattr(value, "sql_SubQueryOperand149", self)

class sql_XExpr:

    def __init__(self, xf: str, sql_XExpr: "sql_FullExpression" = None, sql_XExpr123: "sql_Operands" = None, sql_XExpr126: "sql_Prms" = None):
        self.xf = xf
        self.sql_XExpr = sql_XExpr
        self.sql_XExpr123 = sql_XExpr123
        self.sql_XExpr126 = sql_XExpr126
        
    @property
    def xf(self) -> str:
        return self.__xf

    @xf.setter
    def xf(self, xf: str):
        self.__xf = xf

    @property
    def sql_XExpr126(self):
        return self.__sql_XExpr126

    @sql_XExpr126.setter
    def sql_XExpr126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_XExpr__sql_XExpr126", None)
        self.__sql_XExpr126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Prms"):
                opp_val = getattr(old_value, "sql_Prms", None)
                if opp_val == self:
                    setattr(old_value, "sql_Prms", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Prms"):
                opp_val = getattr(value, "sql_Prms", None)
                setattr(value, "sql_Prms", self)

    @property
    def sql_XExpr(self):
        return self.__sql_XExpr

    @sql_XExpr.setter
    def sql_XExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_XExpr__sql_XExpr", None)
        self.__sql_XExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FullExpression105"):
                opp_val = getattr(old_value, "sql_FullExpression105", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression105"):
                opp_val = getattr(value, "sql_FullExpression105", None)
                setattr(value, "sql_FullExpression105", self)

    @property
    def sql_XExpr123(self):
        return self.__sql_XExpr123

    @sql_XExpr123.setter
    def sql_XExpr123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_XExpr__sql_XExpr123", None)
        self.__sql_XExpr123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operands124"):
                opp_val = getattr(old_value, "sql_Operands124", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operands124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operands124"):
                opp_val = getattr(value, "sql_Operands124", None)
                setattr(value, "sql_Operands124", self)

class OrOrderByColumn:

    pass
class sql_OrderByColumnFull(OrOrderByColumn):

    def __init__(self, colOrderInt: int, direction: str, sql_OrderByColumnFull86: "sql_ColumnFull" = None, sql_OrderByColumnFull: "sql_OrOrderByColumn" = None):
        self.colOrderInt = colOrderInt
        self.direction = direction
        self.sql_OrderByColumnFull86 = sql_OrderByColumnFull86
        self.sql_OrderByColumnFull = sql_OrderByColumnFull
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def colOrderInt(self) -> int:
        return self.__colOrderInt

    @colOrderInt.setter
    def colOrderInt(self, colOrderInt: int):
        self.__colOrderInt = colOrderInt

    @property
    def sql_OrderByColumnFull(self):
        return self.__sql_OrderByColumnFull

    @sql_OrderByColumnFull.setter
    def sql_OrderByColumnFull(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_OrderByColumnFull__sql_OrderByColumnFull", None)
        self.__sql_OrderByColumnFull = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_OrOrderByColumn84"):
                opp_val = getattr(old_value, "sql_OrOrderByColumn84", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OrOrderByColumn84"):
                opp_val = getattr(value, "sql_OrOrderByColumn84", None)
                if opp_val is None:
                    setattr(value, "sql_OrOrderByColumn84", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sql_OrderByColumnFull86(self):
        return self.__sql_OrderByColumnFull86

    @sql_OrderByColumnFull86.setter
    def sql_OrderByColumnFull86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_OrderByColumnFull__sql_OrderByColumnFull86", None)
        self.__sql_OrderByColumnFull86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_ColumnFull"):
                opp_val = getattr(old_value, "sql_ColumnFull", None)
                if opp_val == self:
                    setattr(old_value, "sql_ColumnFull", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_ColumnFull"):
                opp_val = getattr(value, "sql_ColumnFull", None)
                setattr(value, "sql_ColumnFull", self)

class TableFull:

    pass
class sql_tbls(TableFull):

    pass
class PivotCol:

    pass
class sql_pcols(PivotCol):

    pass
class ColumnFull:

    pass
class sql_Col(ColumnFull):

    pass
class Pivots:

    pass
class sql_pvcs(Pivots):

    pass
class sql_OpFunction:

    def __init__(self, fname: str, sql_OpFunction: "sql_GroupByColumnFull" = None, sql_OpFunction136: "sql_LikeOperand" = None, sql_OpFunction183: "sql_Operand" = None, sql_OpFunction194: "sql_OpFunctionArg" = None, sql_OpFunction196: "sql_FunctionAnalytical" = None):
        self.fname = fname
        self.sql_OpFunction = sql_OpFunction
        self.sql_OpFunction136 = sql_OpFunction136
        self.sql_OpFunction183 = sql_OpFunction183
        self.sql_OpFunction194 = sql_OpFunction194
        self.sql_OpFunction196 = sql_OpFunction196
        
    @property
    def fname(self) -> str:
        return self.__fname

    @fname.setter
    def fname(self, fname: str):
        self.__fname = fname

    @property
    def sql_OpFunction196(self):
        return self.__sql_OpFunction196

    @sql_OpFunction196.setter
    def sql_OpFunction196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_OpFunction__sql_OpFunction196", None)
        self.__sql_OpFunction196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FunctionAnalytical"):
                opp_val = getattr(old_value, "sql_FunctionAnalytical", None)
                if opp_val == self:
                    setattr(old_value, "sql_FunctionAnalytical", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FunctionAnalytical"):
                opp_val = getattr(value, "sql_FunctionAnalytical", None)
                setattr(value, "sql_FunctionAnalytical", self)

    @property
    def sql_OpFunction194(self):
        return self.__sql_OpFunction194

    @sql_OpFunction194.setter
    def sql_OpFunction194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_OpFunction__sql_OpFunction194", None)
        self.__sql_OpFunction194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_OpFunctionArg"):
                opp_val = getattr(old_value, "sql_OpFunctionArg", None)
                if opp_val == self:
                    setattr(old_value, "sql_OpFunctionArg", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OpFunctionArg"):
                opp_val = getattr(value, "sql_OpFunctionArg", None)
                setattr(value, "sql_OpFunctionArg", self)

    @property
    def sql_OpFunction(self):
        return self.__sql_OpFunction

    @sql_OpFunction.setter
    def sql_OpFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_OpFunction__sql_OpFunction", None)
        self.__sql_OpFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_GroupByColumnFull93"):
                opp_val = getattr(old_value, "sql_GroupByColumnFull93", None)
                if opp_val == self:
                    setattr(old_value, "sql_GroupByColumnFull93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_GroupByColumnFull93"):
                opp_val = getattr(value, "sql_GroupByColumnFull93", None)
                setattr(value, "sql_GroupByColumnFull93", self)

    @property
    def sql_OpFunction183(self):
        return self.__sql_OpFunction183

    @sql_OpFunction183.setter
    def sql_OpFunction183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_OpFunction__sql_OpFunction183", None)
        self.__sql_OpFunction183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operand182"):
                opp_val = getattr(old_value, "sql_Operand182", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operand182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operand182"):
                opp_val = getattr(value, "sql_Operand182", None)
                setattr(value, "sql_Operand182", self)

    @property
    def sql_OpFunction136(self):
        return self.__sql_OpFunction136

    @sql_OpFunction136.setter
    def sql_OpFunction136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_OpFunction__sql_OpFunction136", None)
        self.__sql_OpFunction136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_LikeOperand135"):
                opp_val = getattr(old_value, "sql_LikeOperand135", None)
                if opp_val == self:
                    setattr(old_value, "sql_LikeOperand135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_LikeOperand135"):
                opp_val = getattr(value, "sql_LikeOperand135", None)
                setattr(value, "sql_LikeOperand135", self)

class OrGroupByColumn:

    pass
class sql_GroupByColumnFull(OrGroupByColumn):

    pass
class sql_UnpivotInClause:

    pass
class sql_PivotColumns:

    pass
class sql_UnpivotInClauseArgs:

    pass
class sql_PivotFunction:

    pass
class PivotFunction:

    pass
class PivotColumns:

    pass
class sql_PivotCol(PivotColumns, Pivots, PivotFunction):

    pass
class sql_Pivots(PivotColumns):

    pass
class UnpivotInClauseArgs:

    pass
class sql_uicargs(UnpivotInClauseArgs):

    pass
class sql_UnpivotInClauseArg(UnpivotInClauseArgs):

    pass
class sql_UnpivotTable:

    pass
class sql_PivotTable:

    pass
class sql_SubQueryOperand:

    pass
class sql_TableFull:

    pass
class sql_PivotInClause:

    def __init__(self, pinany: str, sql_PivotInClause: "sql_PivotTable" = None, sql_PivotInClause67: "sql_SubQueryOperand" = None, sql_PivotInClause70: "sql_UnpivotInClauseArgs" = None):
        self.pinany = pinany
        self.sql_PivotInClause = sql_PivotInClause
        self.sql_PivotInClause67 = sql_PivotInClause67
        self.sql_PivotInClause70 = sql_PivotInClause70
        
    @property
    def pinany(self) -> str:
        return self.__pinany

    @pinany.setter
    def pinany(self, pinany: str):
        self.__pinany = pinany

    @property
    def sql_PivotInClause67(self):
        return self.__sql_PivotInClause67

    @sql_PivotInClause67.setter
    def sql_PivotInClause67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_PivotInClause__sql_PivotInClause67", None)
        self.__sql_PivotInClause67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_SubQueryOperand68"):
                opp_val = getattr(old_value, "sql_SubQueryOperand68", None)
                if opp_val == self:
                    setattr(old_value, "sql_SubQueryOperand68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_SubQueryOperand68"):
                opp_val = getattr(value, "sql_SubQueryOperand68", None)
                setattr(value, "sql_SubQueryOperand68", self)

    @property
    def sql_PivotInClause70(self):
        return self.__sql_PivotInClause70

    @sql_PivotInClause70.setter
    def sql_PivotInClause70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_PivotInClause__sql_PivotInClause70", None)
        self.__sql_PivotInClause70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_UnpivotInClauseArgs"):
                opp_val = getattr(old_value, "sql_UnpivotInClauseArgs", None)
                if opp_val == self:
                    setattr(old_value, "sql_UnpivotInClauseArgs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_UnpivotInClauseArgs"):
                opp_val = getattr(value, "sql_UnpivotInClauseArgs", None)
                setattr(value, "sql_UnpivotInClauseArgs", self)

    @property
    def sql_PivotInClause(self):
        return self.__sql_PivotInClause

    @sql_PivotInClause.setter
    def sql_PivotInClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_PivotInClause__sql_PivotInClause", None)
        self.__sql_PivotInClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_PivotTable65"):
                opp_val = getattr(old_value, "sql_PivotTable65", None)
                if opp_val == self:
                    setattr(old_value, "sql_PivotTable65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_PivotTable65"):
                opp_val = getattr(value, "sql_PivotTable65", None)
                setattr(value, "sql_PivotTable65", self)

class sql_PivotForClause:

    pass
class sql_PivotFunctions:

    def __init__(self, abc: str, sql_PivotFunctions: "sql_PivotTable" = None):
        self.abc = abc
        self.sql_PivotFunctions = sql_PivotFunctions
        
    @property
    def abc(self) -> str:
        return self.__abc

    @abc.setter
    def abc(self, abc: str):
        self.__abc = abc

    @property
    def sql_PivotFunctions(self):
        return self.__sql_PivotFunctions

    @sql_PivotFunctions.setter
    def sql_PivotFunctions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_PivotFunctions__sql_PivotFunctions", None)
        self.__sql_PivotFunctions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_PivotTable61"):
                opp_val = getattr(old_value, "sql_PivotTable61", None)
                if opp_val == self:
                    setattr(old_value, "sql_PivotTable61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_PivotTable61"):
                opp_val = getattr(value, "sql_PivotTable61", None)
                setattr(value, "sql_PivotTable61", self)

class sql_DbObjectNameAll:

    def __init__(self, dbname: str, sql_DbObjectNameAll: "sql_ColumnOrAlias" = None):
        self.dbname = dbname
        self.sql_DbObjectNameAll = sql_DbObjectNameAll
        
    @property
    def dbname(self) -> str:
        return self.__dbname

    @dbname.setter
    def dbname(self, dbname: str):
        self.__dbname = dbname

    @property
    def sql_DbObjectNameAll(self):
        return self.__sql_DbObjectNameAll

    @sql_DbObjectNameAll.setter
    def sql_DbObjectNameAll(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_DbObjectNameAll__sql_DbObjectNameAll", None)
        self.__sql_DbObjectNameAll = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_ColumnOrAlias36"):
                opp_val = getattr(old_value, "sql_ColumnOrAlias36", None)
                if opp_val == self:
                    setattr(old_value, "sql_ColumnOrAlias36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_ColumnOrAlias36"):
                opp_val = getattr(value, "sql_ColumnOrAlias36", None)
                setattr(value, "sql_ColumnOrAlias36", self)

class sql_DbObjectName(PivotCol, ColumnFull, TableFull):

    def __init__(self, dbname: str, sql_DbObjectName: "sql_ColumnOrAlias" = None, sql_DbObjectName59: "sql_TableOrAlias" = None, sql_DbObjectName227: "sql_AnalyticExprArg" = None, sql_DbObjectName252: "sql_Col" = None, sql_DbObjectName259: "sql_pcols" = None, sql_DbObjectName261: "sql_tbls" = None):
        self.dbname = dbname
        self.sql_DbObjectName = sql_DbObjectName
        self.sql_DbObjectName59 = sql_DbObjectName59
        self.sql_DbObjectName227 = sql_DbObjectName227
        self.sql_DbObjectName252 = sql_DbObjectName252
        self.sql_DbObjectName259 = sql_DbObjectName259
        self.sql_DbObjectName261 = sql_DbObjectName261
        
    @property
    def dbname(self) -> str:
        return self.__dbname

    @dbname.setter
    def dbname(self, dbname: str):
        self.__dbname = dbname

    @property
    def sql_DbObjectName259(self):
        return self.__sql_DbObjectName259

    @sql_DbObjectName259.setter
    def sql_DbObjectName259(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_DbObjectName__sql_DbObjectName259", None)
        self.__sql_DbObjectName259 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_pcols"):
                opp_val = getattr(old_value, "sql_pcols", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_pcols"):
                opp_val = getattr(value, "sql_pcols", None)
                if opp_val is None:
                    setattr(value, "sql_pcols", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sql_DbObjectName(self):
        return self.__sql_DbObjectName

    @sql_DbObjectName.setter
    def sql_DbObjectName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_DbObjectName__sql_DbObjectName", None)
        self.__sql_DbObjectName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_ColumnOrAlias34"):
                opp_val = getattr(old_value, "sql_ColumnOrAlias34", None)
                if opp_val == self:
                    setattr(old_value, "sql_ColumnOrAlias34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_ColumnOrAlias34"):
                opp_val = getattr(value, "sql_ColumnOrAlias34", None)
                setattr(value, "sql_ColumnOrAlias34", self)

    @property
    def sql_DbObjectName59(self):
        return self.__sql_DbObjectName59

    @sql_DbObjectName59.setter
    def sql_DbObjectName59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_DbObjectName__sql_DbObjectName59", None)
        self.__sql_DbObjectName59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_TableOrAlias58"):
                opp_val = getattr(old_value, "sql_TableOrAlias58", None)
                if opp_val == self:
                    setattr(old_value, "sql_TableOrAlias58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_TableOrAlias58"):
                opp_val = getattr(value, "sql_TableOrAlias58", None)
                setattr(value, "sql_TableOrAlias58", self)

    @property
    def sql_DbObjectName261(self):
        return self.__sql_DbObjectName261

    @sql_DbObjectName261.setter
    def sql_DbObjectName261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_DbObjectName__sql_DbObjectName261", None)
        self.__sql_DbObjectName261 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_tbls"):
                opp_val = getattr(old_value, "sql_tbls", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_tbls"):
                opp_val = getattr(value, "sql_tbls", None)
                if opp_val is None:
                    setattr(value, "sql_tbls", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sql_DbObjectName227(self):
        return self.__sql_DbObjectName227

    @sql_DbObjectName227.setter
    def sql_DbObjectName227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_DbObjectName__sql_DbObjectName227", None)
        self.__sql_DbObjectName227 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_AnalyticExprArg226"):
                opp_val = getattr(old_value, "sql_AnalyticExprArg226", None)
                if opp_val == self:
                    setattr(old_value, "sql_AnalyticExprArg226", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_AnalyticExprArg226"):
                opp_val = getattr(value, "sql_AnalyticExprArg226", None)
                setattr(value, "sql_AnalyticExprArg226", self)

    @property
    def sql_DbObjectName252(self):
        return self.__sql_DbObjectName252

    @sql_DbObjectName252.setter
    def sql_DbObjectName252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_DbObjectName__sql_DbObjectName252", None)
        self.__sql_DbObjectName252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Col"):
                opp_val = getattr(old_value, "sql_Col", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Col"):
                opp_val = getattr(value, "sql_Col", None)
                if opp_val is None:
                    setattr(value, "sql_Col", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sql_Operands(OpFunctionArgAgregate):

    pass
class OrColumn:

    pass
class sql_ColumnOrAlias(OrColumn):

    def __init__(self, alias: str, allCols: str, sql_ColumnOrAlias: "sql_OrColumn" = None, sql_ColumnOrAlias32: "sql_Operands" = None, sql_ColumnOrAlias34: "sql_DbObjectName" = None, sql_ColumnOrAlias36: "sql_DbObjectNameAll" = None):
        self.alias = alias
        self.allCols = allCols
        self.sql_ColumnOrAlias = sql_ColumnOrAlias
        self.sql_ColumnOrAlias32 = sql_ColumnOrAlias32
        self.sql_ColumnOrAlias34 = sql_ColumnOrAlias34
        self.sql_ColumnOrAlias36 = sql_ColumnOrAlias36
        
    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def allCols(self) -> str:
        return self.__allCols

    @allCols.setter
    def allCols(self, allCols: str):
        self.__allCols = allCols

    @property
    def sql_ColumnOrAlias34(self):
        return self.__sql_ColumnOrAlias34

    @sql_ColumnOrAlias34.setter
    def sql_ColumnOrAlias34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ColumnOrAlias__sql_ColumnOrAlias34", None)
        self.__sql_ColumnOrAlias34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_DbObjectName"):
                opp_val = getattr(old_value, "sql_DbObjectName", None)
                if opp_val == self:
                    setattr(old_value, "sql_DbObjectName", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_DbObjectName"):
                opp_val = getattr(value, "sql_DbObjectName", None)
                setattr(value, "sql_DbObjectName", self)

    @property
    def sql_ColumnOrAlias32(self):
        return self.__sql_ColumnOrAlias32

    @sql_ColumnOrAlias32.setter
    def sql_ColumnOrAlias32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ColumnOrAlias__sql_ColumnOrAlias32", None)
        self.__sql_ColumnOrAlias32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operands"):
                opp_val = getattr(old_value, "sql_Operands", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operands", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operands"):
                opp_val = getattr(value, "sql_Operands", None)
                setattr(value, "sql_Operands", self)

    @property
    def sql_ColumnOrAlias(self):
        return self.__sql_ColumnOrAlias

    @sql_ColumnOrAlias.setter
    def sql_ColumnOrAlias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ColumnOrAlias__sql_ColumnOrAlias", None)
        self.__sql_ColumnOrAlias = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_OrColumn30"):
                opp_val = getattr(old_value, "sql_OrColumn30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OrColumn30"):
                opp_val = getattr(value, "sql_OrColumn30", None)
                if opp_val is None:
                    setattr(value, "sql_OrColumn30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sql_ColumnOrAlias36(self):
        return self.__sql_ColumnOrAlias36

    @sql_ColumnOrAlias36.setter
    def sql_ColumnOrAlias36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ColumnOrAlias__sql_ColumnOrAlias36", None)
        self.__sql_ColumnOrAlias36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_DbObjectNameAll"):
                opp_val = getattr(old_value, "sql_DbObjectNameAll", None)
                if opp_val == self:
                    setattr(old_value, "sql_DbObjectNameAll", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_DbObjectNameAll"):
                opp_val = getattr(value, "sql_DbObjectNameAll", None)
                setattr(value, "sql_DbObjectNameAll", self)

class sql_FromTableJoin:

    def __init__(self, join: str, sql_FromTableJoin: "sql_FromTable" = None, sql_FromTableJoin44: "sql_TableOrAlias" = None, sql_FromTableJoin47: "sql_OrExpr" = None):
        self.join = join
        self.sql_FromTableJoin = sql_FromTableJoin
        self.sql_FromTableJoin44 = sql_FromTableJoin44
        self.sql_FromTableJoin47 = sql_FromTableJoin47
        
    @property
    def join(self) -> str:
        return self.__join

    @join.setter
    def join(self, join: str):
        self.__join = join

    @property
    def sql_FromTableJoin(self):
        return self.__sql_FromTableJoin

    @sql_FromTableJoin.setter
    def sql_FromTableJoin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FromTableJoin__sql_FromTableJoin", None)
        self.__sql_FromTableJoin = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FromTable42"):
                opp_val = getattr(old_value, "sql_FromTable42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FromTable42"):
                opp_val = getattr(value, "sql_FromTable42", None)
                if opp_val is None:
                    setattr(value, "sql_FromTable42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sql_FromTableJoin44(self):
        return self.__sql_FromTableJoin44

    @sql_FromTableJoin44.setter
    def sql_FromTableJoin44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FromTableJoin__sql_FromTableJoin44", None)
        self.__sql_FromTableJoin44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_TableOrAlias45"):
                opp_val = getattr(old_value, "sql_TableOrAlias45", None)
                if opp_val == self:
                    setattr(old_value, "sql_TableOrAlias45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_TableOrAlias45"):
                opp_val = getattr(value, "sql_TableOrAlias45", None)
                setattr(value, "sql_TableOrAlias45", self)

    @property
    def sql_FromTableJoin47(self):
        return self.__sql_FromTableJoin47

    @sql_FromTableJoin47.setter
    def sql_FromTableJoin47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FromTableJoin__sql_FromTableJoin47", None)
        self.__sql_FromTableJoin47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_OrExpr48"):
                opp_val = getattr(old_value, "sql_OrExpr48", None)
                if opp_val == self:
                    setattr(old_value, "sql_OrExpr48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OrExpr48"):
                opp_val = getattr(value, "sql_OrExpr48", None)
                setattr(value, "sql_OrExpr48", self)

class sql_TableOrAlias:

    def __init__(self, alias: str, sql_TableOrAlias: "sql_FromTable" = None, sql_TableOrAlias58: "sql_DbObjectName" = None, sql_TableOrAlias45: "sql_FromTableJoin" = None, sql_TableOrAlias50: "sql_TableFull" = None, sql_TableOrAlias52: "sql_SubQueryOperand" = None, sql_TableOrAlias54: "sql_PivotTable" = None, sql_TableOrAlias56: "sql_UnpivotTable" = None):
        self.alias = alias
        self.sql_TableOrAlias = sql_TableOrAlias
        self.sql_TableOrAlias58 = sql_TableOrAlias58
        self.sql_TableOrAlias45 = sql_TableOrAlias45
        self.sql_TableOrAlias50 = sql_TableOrAlias50
        self.sql_TableOrAlias52 = sql_TableOrAlias52
        self.sql_TableOrAlias54 = sql_TableOrAlias54
        self.sql_TableOrAlias56 = sql_TableOrAlias56
        
    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def sql_TableOrAlias56(self):
        return self.__sql_TableOrAlias56

    @sql_TableOrAlias56.setter
    def sql_TableOrAlias56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_TableOrAlias__sql_TableOrAlias56", None)
        self.__sql_TableOrAlias56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_UnpivotTable"):
                opp_val = getattr(old_value, "sql_UnpivotTable", None)
                if opp_val == self:
                    setattr(old_value, "sql_UnpivotTable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_UnpivotTable"):
                opp_val = getattr(value, "sql_UnpivotTable", None)
                setattr(value, "sql_UnpivotTable", self)

    @property
    def sql_TableOrAlias45(self):
        return self.__sql_TableOrAlias45

    @sql_TableOrAlias45.setter
    def sql_TableOrAlias45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_TableOrAlias__sql_TableOrAlias45", None)
        self.__sql_TableOrAlias45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FromTableJoin44"):
                opp_val = getattr(old_value, "sql_FromTableJoin44", None)
                if opp_val == self:
                    setattr(old_value, "sql_FromTableJoin44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FromTableJoin44"):
                opp_val = getattr(value, "sql_FromTableJoin44", None)
                setattr(value, "sql_FromTableJoin44", self)

    @property
    def sql_TableOrAlias54(self):
        return self.__sql_TableOrAlias54

    @sql_TableOrAlias54.setter
    def sql_TableOrAlias54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_TableOrAlias__sql_TableOrAlias54", None)
        self.__sql_TableOrAlias54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_PivotTable"):
                opp_val = getattr(old_value, "sql_PivotTable", None)
                if opp_val == self:
                    setattr(old_value, "sql_PivotTable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_PivotTable"):
                opp_val = getattr(value, "sql_PivotTable", None)
                setattr(value, "sql_PivotTable", self)

    @property
    def sql_TableOrAlias50(self):
        return self.__sql_TableOrAlias50

    @sql_TableOrAlias50.setter
    def sql_TableOrAlias50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_TableOrAlias__sql_TableOrAlias50", None)
        self.__sql_TableOrAlias50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_TableFull"):
                opp_val = getattr(old_value, "sql_TableFull", None)
                if opp_val == self:
                    setattr(old_value, "sql_TableFull", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_TableFull"):
                opp_val = getattr(value, "sql_TableFull", None)
                setattr(value, "sql_TableFull", self)

    @property
    def sql_TableOrAlias(self):
        return self.__sql_TableOrAlias

    @sql_TableOrAlias.setter
    def sql_TableOrAlias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_TableOrAlias__sql_TableOrAlias", None)
        self.__sql_TableOrAlias = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FromTable40"):
                opp_val = getattr(old_value, "sql_FromTable40", None)
                if opp_val == self:
                    setattr(old_value, "sql_FromTable40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FromTable40"):
                opp_val = getattr(value, "sql_FromTable40", None)
                setattr(value, "sql_FromTable40", self)

    @property
    def sql_TableOrAlias58(self):
        return self.__sql_TableOrAlias58

    @sql_TableOrAlias58.setter
    def sql_TableOrAlias58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_TableOrAlias__sql_TableOrAlias58", None)
        self.__sql_TableOrAlias58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_DbObjectName59"):
                opp_val = getattr(old_value, "sql_DbObjectName59", None)
                if opp_val == self:
                    setattr(old_value, "sql_DbObjectName59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_DbObjectName59"):
                opp_val = getattr(value, "sql_DbObjectName59", None)
                setattr(value, "sql_DbObjectName59", self)

    @property
    def sql_TableOrAlias52(self):
        return self.__sql_TableOrAlias52

    @sql_TableOrAlias52.setter
    def sql_TableOrAlias52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_TableOrAlias__sql_TableOrAlias52", None)
        self.__sql_TableOrAlias52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_SubQueryOperand"):
                opp_val = getattr(old_value, "sql_SubQueryOperand", None)
                if opp_val == self:
                    setattr(old_value, "sql_SubQueryOperand", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_SubQueryOperand"):
                opp_val = getattr(value, "sql_SubQueryOperand", None)
                setattr(value, "sql_SubQueryOperand", self)

class OrTable:

    pass
class sql_FromTable(OrTable):

    pass
class sql_OrGroupByColumn:

    pass
class sql_OrExpr:

    pass
class sql_OrTable:

    pass
class PivotForClause:

    pass
class sql_ColumnFull(PivotForClause):

    pass
class sql_OrColumn(PivotForClause):

    pass
class sql_OrOrderByColumn:

    pass
class sql_Limit:

    def __init__(self, l1: int, sql_Limit: "sql_IntegerValue" = None, sql_Limit23: "sql_Select" = None):
        self.l1 = l1
        self.sql_Limit = sql_Limit
        self.sql_Limit23 = sql_Limit23
        
    @property
    def l1(self) -> int:
        return self.__l1

    @l1.setter
    def l1(self, l1: int):
        self.__l1 = l1

    @property
    def sql_Limit23(self):
        return self.__sql_Limit23

    @sql_Limit23.setter
    def sql_Limit23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Limit__sql_Limit23", None)
        self.__sql_Limit23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Select22"):
                opp_val = getattr(old_value, "sql_Select22", None)
                if opp_val == self:
                    setattr(old_value, "sql_Select22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Select22"):
                opp_val = getattr(value, "sql_Select22", None)
                setattr(value, "sql_Select22", self)

    @property
    def sql_Limit(self):
        return self.__sql_Limit

    @sql_Limit.setter
    def sql_Limit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Limit__sql_Limit", None)
        self.__sql_Limit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_IntegerValue3"):
                opp_val = getattr(old_value, "sql_IntegerValue3", None)
                if opp_val == self:
                    setattr(old_value, "sql_IntegerValue3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_IntegerValue3"):
                opp_val = getattr(value, "sql_IntegerValue3", None)
                setattr(value, "sql_IntegerValue3", self)

class sql_Offset:

    def __init__(self, offset: int, sql_Offset: "sql_Select" = None):
        self.offset = offset
        self.sql_Offset = sql_Offset
        
    @property
    def offset(self) -> int:
        return self.__offset

    @offset.setter
    def offset(self, offset: int):
        self.__offset = offset

    @property
    def sql_Offset(self):
        return self.__sql_Offset

    @sql_Offset.setter
    def sql_Offset(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Offset__sql_Offset", None)
        self.__sql_Offset = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Select25"):
                opp_val = getattr(old_value, "sql_Select25", None)
                if opp_val == self:
                    setattr(old_value, "sql_Select25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Select25"):
                opp_val = getattr(value, "sql_Select25", None)
                setattr(value, "sql_Select25", self)

class sql_IntegerValue:

    def __init__(self, integer: int, sql_IntegerValue3: "sql_Limit" = None, sql_IntegerValue: "sql_FetchFirst" = None):
        self.integer = integer
        self.sql_IntegerValue3 = sql_IntegerValue3
        self.sql_IntegerValue = sql_IntegerValue
        
    @property
    def integer(self) -> int:
        return self.__integer

    @integer.setter
    def integer(self, integer: int):
        self.__integer = integer

    @property
    def sql_IntegerValue3(self):
        return self.__sql_IntegerValue3

    @sql_IntegerValue3.setter
    def sql_IntegerValue3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_IntegerValue__sql_IntegerValue3", None)
        self.__sql_IntegerValue3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Limit"):
                opp_val = getattr(old_value, "sql_Limit", None)
                if opp_val == self:
                    setattr(old_value, "sql_Limit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Limit"):
                opp_val = getattr(value, "sql_Limit", None)
                setattr(value, "sql_Limit", self)

    @property
    def sql_IntegerValue(self):
        return self.__sql_IntegerValue

    @sql_IntegerValue.setter
    def sql_IntegerValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_IntegerValue__sql_IntegerValue", None)
        self.__sql_IntegerValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FetchFirst"):
                opp_val = getattr(old_value, "sql_FetchFirst", None)
                if opp_val == self:
                    setattr(old_value, "sql_FetchFirst", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FetchFirst"):
                opp_val = getattr(value, "sql_FetchFirst", None)
                setattr(value, "sql_FetchFirst", self)

class sql_FetchFirst:

    def __init__(self, row: str, sql_FetchFirst: "sql_IntegerValue" = None, sql_FetchFirst28: "sql_Select" = None):
        self.row = row
        self.sql_FetchFirst = sql_FetchFirst
        self.sql_FetchFirst28 = sql_FetchFirst28
        
    @property
    def row(self) -> str:
        return self.__row

    @row.setter
    def row(self, row: str):
        self.__row = row

    @property
    def sql_FetchFirst(self):
        return self.__sql_FetchFirst

    @sql_FetchFirst.setter
    def sql_FetchFirst(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FetchFirst__sql_FetchFirst", None)
        self.__sql_FetchFirst = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_IntegerValue"):
                opp_val = getattr(old_value, "sql_IntegerValue", None)
                if opp_val == self:
                    setattr(old_value, "sql_IntegerValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_IntegerValue"):
                opp_val = getattr(value, "sql_IntegerValue", None)
                setattr(value, "sql_IntegerValue", self)

    @property
    def sql_FetchFirst28(self):
        return self.__sql_FetchFirst28

    @sql_FetchFirst28.setter
    def sql_FetchFirst28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FetchFirst__sql_FetchFirst28", None)
        self.__sql_FetchFirst28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Select27"):
                opp_val = getattr(old_value, "sql_Select27", None)
                if opp_val == self:
                    setattr(old_value, "sql_Select27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Select27"):
                opp_val = getattr(value, "sql_Select27", None)
                setattr(value, "sql_Select27", self)

class sql_SelectQuery:

    pass
class sql_Model:

    pass
class SelectQuery:

    pass
class sql_Select(SelectQuery):

    def __init__(self, select: str, sql_Select: "sql_SelectSubSet" = None, sql_Select6: set["sql_SelectSubSet"] = None, sql_Select17: "sql_OrExpr" = None, sql_Select20: "sql_OrOrderByColumn" = None, sql_Select22: "sql_Limit" = None, sql_Select25: "sql_Offset" = None, sql_Select27: "sql_FetchFirst" = None, sql_Select9: "sql_OrColumn" = None, sql_Select11: "sql_OrTable" = None, sql_Select13: "sql_OrExpr" = None, sql_Select15: "sql_OrGroupByColumn" = None):
        self.select = select
        self.sql_Select = sql_Select
        self.sql_Select6 = sql_Select6 if sql_Select6 is not None else set()
        self.sql_Select17 = sql_Select17
        self.sql_Select20 = sql_Select20
        self.sql_Select22 = sql_Select22
        self.sql_Select25 = sql_Select25
        self.sql_Select27 = sql_Select27
        self.sql_Select9 = sql_Select9
        self.sql_Select11 = sql_Select11
        self.sql_Select13 = sql_Select13
        self.sql_Select15 = sql_Select15
        
    @property
    def select(self) -> str:
        return self.__select

    @select.setter
    def select(self, select: str):
        self.__select = select

    @property
    def sql_Select27(self):
        return self.__sql_Select27

    @sql_Select27.setter
    def sql_Select27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Select__sql_Select27", None)
        self.__sql_Select27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FetchFirst28"):
                opp_val = getattr(old_value, "sql_FetchFirst28", None)
                if opp_val == self:
                    setattr(old_value, "sql_FetchFirst28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FetchFirst28"):
                opp_val = getattr(value, "sql_FetchFirst28", None)
                setattr(value, "sql_FetchFirst28", self)

    @property
    def sql_Select22(self):
        return self.__sql_Select22

    @sql_Select22.setter
    def sql_Select22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Select__sql_Select22", None)
        self.__sql_Select22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Limit23"):
                opp_val = getattr(old_value, "sql_Limit23", None)
                if opp_val == self:
                    setattr(old_value, "sql_Limit23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Limit23"):
                opp_val = getattr(value, "sql_Limit23", None)
                setattr(value, "sql_Limit23", self)

    @property
    def sql_Select6(self):
        return self.__sql_Select6

    @sql_Select6.setter
    def sql_Select6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Select__sql_Select6", None)
        self.__sql_Select6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sql_SelectSubSet7"):
                    opp_val = getattr(item, "sql_SelectSubSet7", None)
                    
                    if opp_val == self:
                        setattr(item, "sql_SelectSubSet7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sql_SelectSubSet7"):
                    opp_val = getattr(item, "sql_SelectSubSet7", None)
                    
                    setattr(item, "sql_SelectSubSet7", self)
                    

    @property
    def sql_Select17(self):
        return self.__sql_Select17

    @sql_Select17.setter
    def sql_Select17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Select__sql_Select17", None)
        self.__sql_Select17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_OrExpr18"):
                opp_val = getattr(old_value, "sql_OrExpr18", None)
                if opp_val == self:
                    setattr(old_value, "sql_OrExpr18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OrExpr18"):
                opp_val = getattr(value, "sql_OrExpr18", None)
                setattr(value, "sql_OrExpr18", self)

    @property
    def sql_Select11(self):
        return self.__sql_Select11

    @sql_Select11.setter
    def sql_Select11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Select__sql_Select11", None)
        self.__sql_Select11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_OrTable"):
                opp_val = getattr(old_value, "sql_OrTable", None)
                if opp_val == self:
                    setattr(old_value, "sql_OrTable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OrTable"):
                opp_val = getattr(value, "sql_OrTable", None)
                setattr(value, "sql_OrTable", self)

    @property
    def sql_Select13(self):
        return self.__sql_Select13

    @sql_Select13.setter
    def sql_Select13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Select__sql_Select13", None)
        self.__sql_Select13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_OrExpr"):
                opp_val = getattr(old_value, "sql_OrExpr", None)
                if opp_val == self:
                    setattr(old_value, "sql_OrExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OrExpr"):
                opp_val = getattr(value, "sql_OrExpr", None)
                setattr(value, "sql_OrExpr", self)

    @property
    def sql_Select20(self):
        return self.__sql_Select20

    @sql_Select20.setter
    def sql_Select20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Select__sql_Select20", None)
        self.__sql_Select20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_OrOrderByColumn"):
                opp_val = getattr(old_value, "sql_OrOrderByColumn", None)
                if opp_val == self:
                    setattr(old_value, "sql_OrOrderByColumn", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OrOrderByColumn"):
                opp_val = getattr(value, "sql_OrOrderByColumn", None)
                setattr(value, "sql_OrOrderByColumn", self)

    @property
    def sql_Select25(self):
        return self.__sql_Select25

    @sql_Select25.setter
    def sql_Select25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Select__sql_Select25", None)
        self.__sql_Select25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Offset"):
                opp_val = getattr(old_value, "sql_Offset", None)
                if opp_val == self:
                    setattr(old_value, "sql_Offset", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Offset"):
                opp_val = getattr(value, "sql_Offset", None)
                setattr(value, "sql_Offset", self)

    @property
    def sql_Select15(self):
        return self.__sql_Select15

    @sql_Select15.setter
    def sql_Select15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Select__sql_Select15", None)
        self.__sql_Select15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_OrGroupByColumn"):
                opp_val = getattr(old_value, "sql_OrGroupByColumn", None)
                if opp_val == self:
                    setattr(old_value, "sql_OrGroupByColumn", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OrGroupByColumn"):
                opp_val = getattr(value, "sql_OrGroupByColumn", None)
                setattr(value, "sql_OrGroupByColumn", self)

    @property
    def sql_Select9(self):
        return self.__sql_Select9

    @sql_Select9.setter
    def sql_Select9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Select__sql_Select9", None)
        self.__sql_Select9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_OrColumn"):
                opp_val = getattr(old_value, "sql_OrColumn", None)
                if opp_val == self:
                    setattr(old_value, "sql_OrColumn", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OrColumn"):
                opp_val = getattr(value, "sql_OrColumn", None)
                setattr(value, "sql_OrColumn", self)

    @property
    def sql_Select(self):
        return self.__sql_Select

    @sql_Select.setter
    def sql_Select(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Select__sql_Select", None)
        self.__sql_Select = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_SelectSubSet"):
                opp_val = getattr(old_value, "sql_SelectSubSet", None)
                if opp_val == self:
                    setattr(old_value, "sql_SelectSubSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_SelectSubSet"):
                opp_val = getattr(value, "sql_SelectSubSet", None)
                setattr(value, "sql_SelectSubSet", self)

class sql_SelectSubSet:

    def __init__(self, op: str, all: str, sql_SelectSubSet: "sql_Select" = None, sql_SelectSubSet7: "sql_Select" = None):
        self.op = op
        self.all = all
        self.sql_SelectSubSet = sql_SelectSubSet
        self.sql_SelectSubSet7 = sql_SelectSubSet7
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def all(self) -> str:
        return self.__all

    @all.setter
    def all(self, all: str):
        self.__all = all

    @property
    def sql_SelectSubSet(self):
        return self.__sql_SelectSubSet

    @sql_SelectSubSet.setter
    def sql_SelectSubSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_SelectSubSet__sql_SelectSubSet", None)
        self.__sql_SelectSubSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Select"):
                opp_val = getattr(old_value, "sql_Select", None)
                if opp_val == self:
                    setattr(old_value, "sql_Select", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Select"):
                opp_val = getattr(value, "sql_Select", None)
                setattr(value, "sql_Select", self)

    @property
    def sql_SelectSubSet7(self):
        return self.__sql_SelectSubSet7

    @sql_SelectSubSet7.setter
    def sql_SelectSubSet7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_SelectSubSet__sql_SelectSubSet7", None)
        self.__sql_SelectSubSet7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Select6"):
                opp_val = getattr(old_value, "sql_Select6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Select6"):
                opp_val = getattr(value, "sql_Select6", None)
                if opp_val is None:
                    setattr(value, "sql_Select6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
