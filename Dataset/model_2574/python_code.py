from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class XFunction(Enum):
    xbwnc = "xbwnc"
    xbwnl = "xbwnl"
    xbwnr = "xbwnr"
    xin = "xin"
    xnotin = "xnotin"
    xeq = "xeq"
    xnoteq = "xnoteq"
    xls = "xls"
    xlsr = "xlsr"
    xgtl = "xgtl"
    xgt = "xgt"
    xbwn = "xbwn"
class EXTRACT_VALUES(Enum):
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
    hms = "hms"
    hs = "hs"
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
class sql_Concat(Operands):

    pass
class sql_Multiply(Operands):

    pass
class sql_Division(Operands):

    pass
class sql_Minus(Operands):

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
            if hasattr(old_value, "sql_UnpivotInClauseArgs288"):
                opp_val = getattr(old_value, "sql_UnpivotInClauseArgs288", None)
                if opp_val == self:
                    setattr(old_value, "sql_UnpivotInClauseArgs288", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_UnpivotInClauseArgs288"):
                opp_val = getattr(value, "sql_UnpivotInClauseArgs288", None)
                setattr(value, "sql_UnpivotInClauseArgs288", self)

class sql_IntegerValue:

    def __init__(self, integer: str):
        self.integer = integer
        
    @property
    def integer(self) -> str:
        return self.__integer

    @integer.setter
    def integer(self, integer: str):
        self.__integer = integer

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
class RowValue:

    pass
class sql_OpFunctionArgAgregate:

    pass
class OpFunctionArg:

    pass
class sql_OpFList(OpFunctionArg):

    pass
class sql_OpFunctionArgOperand(OpFunctionArg):

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
class sql_OrderByClauseArgs:

    pass
class sql_WindowingClauseOperandFollowing:

    pass
class WindowingClause:

    pass
class sql_WindowingClauseOperandPreceding(WindowingClause):

    pass
class sql_WindowingClauseBetween(WindowingClause):

    pass
class AnalyticExprArgs:

    pass
class sql_AExpArgs(AnalyticExprArgs):

    pass
class sql_AnalyticExprArg(AnalyticExprArgs):

    pass
class sql_WindowingClause:

    pass
class sql_OrderByClause:

    pass
class sql_QueryPartitionClause:

    pass
class sql_AnalyticClause:

    pass
class sql_FunctionAnalytical:

    pass
class sql_OpFunctionArg:

    pass
class sql_ScalarOperand(RowValue, OperandList):

    def __init__(self, sostr: str, sodbl: str, sodate: str, sotime: str, sodt: str, soUInt: str, soint: str, sql_ScalarOperand: "sql_Operand" = None, sql_ScalarOperand297: "sql_OpList" = None):
        self.sostr = sostr
        self.sodbl = sodbl
        self.sodate = sodate
        self.sotime = sotime
        self.sodt = sodt
        self.soUInt = soUInt
        self.soint = soint
        self.sql_ScalarOperand = sql_ScalarOperand
        self.sql_ScalarOperand297 = sql_ScalarOperand297
        
    @property
    def sodbl(self) -> str:
        return self.__sodbl

    @sodbl.setter
    def sodbl(self, sodbl: str):
        self.__sodbl = sodbl

    @property
    def sodt(self) -> str:
        return self.__sodt

    @sodt.setter
    def sodt(self, sodt: str):
        self.__sodt = sodt

    @property
    def sotime(self) -> str:
        return self.__sotime

    @sotime.setter
    def sotime(self, sotime: str):
        self.__sotime = sotime

    @property
    def sodate(self) -> str:
        return self.__sodate

    @sodate.setter
    def sodate(self, sodate: str):
        self.__sodate = sodate

    @property
    def soUInt(self) -> str:
        return self.__soUInt

    @soUInt.setter
    def soUInt(self, soUInt: str):
        self.__soUInt = soUInt

    @property
    def sostr(self) -> str:
        return self.__sostr

    @sostr.setter
    def sostr(self, sostr: str):
        self.__sostr = sostr

    @property
    def soint(self) -> str:
        return self.__soint

    @soint.setter
    def soint(self, soint: str):
        self.__soint = soint

    @property
    def sql_ScalarOperand297(self):
        return self.__sql_ScalarOperand297

    @sql_ScalarOperand297.setter
    def sql_ScalarOperand297(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ScalarOperand__sql_ScalarOperand297", None)
        self.__sql_ScalarOperand297 = value
        
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
            if hasattr(old_value, "sql_Operand219"):
                opp_val = getattr(old_value, "sql_Operand219", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operand219", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operand219"):
                opp_val = getattr(value, "sql_Operand219", None)
                setattr(value, "sql_Operand219", self)

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
            if hasattr(old_value, "sql_Operand217"):
                opp_val = getattr(old_value, "sql_Operand217", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operand217", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operand217"):
                opp_val = getattr(value, "sql_Operand217", None)
                setattr(value, "sql_Operand217", self)

class sql_SQLCaseOperand:

    pass
class sql_FunctionExtract:

    def __init__(self, v: str, sql_FunctionExtract: "sql_Operand" = None, sql_FunctionExtract225: "sql_Operands" = None):
        self.v = v
        self.sql_FunctionExtract = sql_FunctionExtract
        self.sql_FunctionExtract225 = sql_FunctionExtract225
        
    @property
    def v(self) -> str:
        return self.__v

    @v.setter
    def v(self, v: str):
        self.__v = v

    @property
    def sql_FunctionExtract225(self):
        return self.__sql_FunctionExtract225

    @sql_FunctionExtract225.setter
    def sql_FunctionExtract225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FunctionExtract__sql_FunctionExtract225", None)
        self.__sql_FunctionExtract225 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operands226"):
                opp_val = getattr(old_value, "sql_Operands226", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operands226", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operands226"):
                opp_val = getattr(value, "sql_Operands226", None)
                setattr(value, "sql_Operands226", self)

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
            if hasattr(old_value, "sql_Operand207"):
                opp_val = getattr(old_value, "sql_Operand207", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operand207", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operand207"):
                opp_val = getattr(value, "sql_Operand207", None)
                setattr(value, "sql_Operand207", self)

class sql_ColumnOperand:

    def __init__(self, ora: str, sql_ColumnOperand: "sql_Operand" = None, sql_ColumnOperand260: "sql_ColumnFull" = None):
        self.ora = ora
        self.sql_ColumnOperand = sql_ColumnOperand
        self.sql_ColumnOperand260 = sql_ColumnOperand260
        
    @property
    def ora(self) -> str:
        return self.__ora

    @ora.setter
    def ora(self, ora: str):
        self.__ora = ora

    @property
    def sql_ColumnOperand260(self):
        return self.__sql_ColumnOperand260

    @sql_ColumnOperand260.setter
    def sql_ColumnOperand260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ColumnOperand__sql_ColumnOperand260", None)
        self.__sql_ColumnOperand260 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_ColumnFull261"):
                opp_val = getattr(old_value, "sql_ColumnFull261", None)
                if opp_val == self:
                    setattr(old_value, "sql_ColumnFull261", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_ColumnFull261"):
                opp_val = getattr(value, "sql_ColumnFull261", None)
                setattr(value, "sql_ColumnFull261", self)

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
            if hasattr(old_value, "sql_Operand196"):
                opp_val = getattr(old_value, "sql_Operand196", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operand196", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operand196"):
                opp_val = getattr(value, "sql_Operand196", None)
                setattr(value, "sql_Operand196", self)

class sql_Operand:

    pass
class OpFunctionArgAgregate:

    pass
class sql_OperandList:

    pass
class sql_OperandListGroup:

    pass
class sql_POperand:

    def __init__(self, prm: str, sql_POperand: "sql_LikeOperand" = None, sql_POperand215: "sql_Operand" = None):
        self.prm = prm
        self.sql_POperand = sql_POperand
        self.sql_POperand215 = sql_POperand215
        
    @property
    def prm(self) -> str:
        return self.__prm

    @prm.setter
    def prm(self, prm: str):
        self.__prm = prm

    @property
    def sql_POperand215(self):
        return self.__sql_POperand215

    @sql_POperand215.setter
    def sql_POperand215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_POperand__sql_POperand215", None)
        self.__sql_POperand215 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operand214"):
                opp_val = getattr(old_value, "sql_Operand214", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operand214", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operand214"):
                opp_val = getattr(value, "sql_Operand214", None)
                setattr(value, "sql_Operand214", self)

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
            if hasattr(old_value, "sql_LikeOperand167"):
                opp_val = getattr(old_value, "sql_LikeOperand167", None)
                if opp_val == self:
                    setattr(old_value, "sql_LikeOperand167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_LikeOperand167"):
                opp_val = getattr(value, "sql_LikeOperand167", None)
                setattr(value, "sql_LikeOperand167", self)

class sql_OpFunctionCast:

    def __init__(self, type: str, p: str, p2: str, sql_OpFunctionCast: "sql_LikeOperand" = None, sql_OpFunctionCast205: "sql_Operand" = None, sql_OpFunctionCast257: "sql_Operands" = None):
        self.type = type
        self.p = p
        self.p2 = p2
        self.sql_OpFunctionCast = sql_OpFunctionCast
        self.sql_OpFunctionCast205 = sql_OpFunctionCast205
        self.sql_OpFunctionCast257 = sql_OpFunctionCast257
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def p(self) -> str:
        return self.__p

    @p.setter
    def p(self, p: str):
        self.__p = p

    @property
    def p2(self) -> str:
        return self.__p2

    @p2.setter
    def p2(self, p2: str):
        self.__p2 = p2

    @property
    def sql_OpFunctionCast257(self):
        return self.__sql_OpFunctionCast257

    @sql_OpFunctionCast257.setter
    def sql_OpFunctionCast257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_OpFunctionCast__sql_OpFunctionCast257", None)
        self.__sql_OpFunctionCast257 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operands258"):
                opp_val = getattr(old_value, "sql_Operands258", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operands258", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operands258"):
                opp_val = getattr(value, "sql_Operands258", None)
                setattr(value, "sql_Operands258", self)

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
            if hasattr(old_value, "sql_LikeOperand165"):
                opp_val = getattr(old_value, "sql_LikeOperand165", None)
                if opp_val == self:
                    setattr(old_value, "sql_LikeOperand165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_LikeOperand165"):
                opp_val = getattr(value, "sql_LikeOperand165", None)
                setattr(value, "sql_LikeOperand165", self)

    @property
    def sql_OpFunctionCast205(self):
        return self.__sql_OpFunctionCast205

    @sql_OpFunctionCast205.setter
    def sql_OpFunctionCast205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_OpFunctionCast__sql_OpFunctionCast205", None)
        self.__sql_OpFunctionCast205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operand204"):
                opp_val = getattr(old_value, "sql_Operand204", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operand204", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operand204"):
                opp_val = getattr(value, "sql_Operand204", None)
                setattr(value, "sql_Operand204", self)

class sql_LikeOperand:

    def __init__(self, op2: str, sql_LikeOperand: "sql_Like" = None, sql_LikeOperand162: "sql_OpFunction" = None, sql_LikeOperand165: "sql_OpFunctionCast" = None, sql_LikeOperand167: "sql_POperand" = None):
        self.op2 = op2
        self.sql_LikeOperand = sql_LikeOperand
        self.sql_LikeOperand162 = sql_LikeOperand162
        self.sql_LikeOperand165 = sql_LikeOperand165
        self.sql_LikeOperand167 = sql_LikeOperand167
        
    @property
    def op2(self) -> str:
        return self.__op2

    @op2.setter
    def op2(self, op2: str):
        self.__op2 = op2

    @property
    def sql_LikeOperand162(self):
        return self.__sql_LikeOperand162

    @sql_LikeOperand162.setter
    def sql_LikeOperand162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_LikeOperand__sql_LikeOperand162", None)
        self.__sql_LikeOperand162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_OpFunction163"):
                opp_val = getattr(old_value, "sql_OpFunction163", None)
                if opp_val == self:
                    setattr(old_value, "sql_OpFunction163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OpFunction163"):
                opp_val = getattr(value, "sql_OpFunction163", None)
                setattr(value, "sql_OpFunction163", self)

    @property
    def sql_LikeOperand165(self):
        return self.__sql_LikeOperand165

    @sql_LikeOperand165.setter
    def sql_LikeOperand165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_LikeOperand__sql_LikeOperand165", None)
        self.__sql_LikeOperand165 = value
        
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
    def sql_LikeOperand167(self):
        return self.__sql_LikeOperand167

    @sql_LikeOperand167.setter
    def sql_LikeOperand167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_LikeOperand__sql_LikeOperand167", None)
        self.__sql_LikeOperand167 = value
        
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
    def sql_LikeOperand(self):
        return self.__sql_LikeOperand

    @sql_LikeOperand.setter
    def sql_LikeOperand(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_LikeOperand__sql_LikeOperand", None)
        self.__sql_LikeOperand = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Like160"):
                opp_val = getattr(old_value, "sql_Like160", None)
                if opp_val == self:
                    setattr(old_value, "sql_Like160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Like160"):
                opp_val = getattr(value, "sql_Like160", None)
                setattr(value, "sql_Like160", self)

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
            if hasattr(old_value, "sql_Prms155"):
                opp_val = getattr(old_value, "sql_Prms155", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Prms155"):
                opp_val = getattr(value, "sql_Prms155", None)
                if opp_val is None:
                    setattr(value, "sql_Prms155", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sql_Prms:

    pass
class sql_Comparison:

    def __init__(self, operator: str, subOperator: str, sql_Comparison: "sql_FullExpression" = None, sql_Comparison157: "sql_Operands" = None):
        self.operator = operator
        self.subOperator = subOperator
        self.sql_Comparison = sql_Comparison
        self.sql_Comparison157 = sql_Comparison157
        
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
    def sql_Comparison(self):
        return self.__sql_Comparison

    @sql_Comparison.setter
    def sql_Comparison(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Comparison__sql_Comparison", None)
        self.__sql_Comparison = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FullExpression145"):
                opp_val = getattr(old_value, "sql_FullExpression145", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression145"):
                opp_val = getattr(value, "sql_FullExpression145", None)
                setattr(value, "sql_FullExpression145", self)

    @property
    def sql_Comparison157(self):
        return self.__sql_Comparison157

    @sql_Comparison157.setter
    def sql_Comparison157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Comparison__sql_Comparison157", None)
        self.__sql_Comparison157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operands158"):
                opp_val = getattr(old_value, "sql_Operands158", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operands158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operands158"):
                opp_val = getattr(value, "sql_Operands158", None)
                setattr(value, "sql_Operands158", self)

class sql_Like:

    def __init__(self, opLike: str, sql_Like: "sql_FullExpression" = None, sql_Like160: "sql_LikeOperand" = None):
        self.opLike = opLike
        self.sql_Like = sql_Like
        self.sql_Like160 = sql_Like160
        
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
            if hasattr(old_value, "sql_FullExpression143"):
                opp_val = getattr(old_value, "sql_FullExpression143", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression143"):
                opp_val = getattr(value, "sql_FullExpression143", None)
                setattr(value, "sql_FullExpression143", self)

    @property
    def sql_Like160(self):
        return self.__sql_Like160

    @sql_Like160.setter
    def sql_Like160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Like__sql_Like160", None)
        self.__sql_Like160 = value
        
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

class sql_ExistsOper:

    def __init__(self, op: str, sql_ExistsOper: "sql_FullExpression" = None, sql_ExistsOper180: "sql_SubQueryOperand" = None, sql_ExistsOper183: "sql_OperandListGroup" = None):
        self.op = op
        self.sql_ExistsOper = sql_ExistsOper
        self.sql_ExistsOper180 = sql_ExistsOper180
        self.sql_ExistsOper183 = sql_ExistsOper183
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

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
            if hasattr(old_value, "sql_FullExpression136"):
                opp_val = getattr(old_value, "sql_FullExpression136", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression136"):
                opp_val = getattr(value, "sql_FullExpression136", None)
                setattr(value, "sql_FullExpression136", self)

    @property
    def sql_ExistsOper183(self):
        return self.__sql_ExistsOper183

    @sql_ExistsOper183.setter
    def sql_ExistsOper183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ExistsOper__sql_ExistsOper183", None)
        self.__sql_ExistsOper183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_OperandListGroup184"):
                opp_val = getattr(old_value, "sql_OperandListGroup184", None)
                if opp_val == self:
                    setattr(old_value, "sql_OperandListGroup184", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OperandListGroup184"):
                opp_val = getattr(value, "sql_OperandListGroup184", None)
                setattr(value, "sql_OperandListGroup184", self)

    @property
    def sql_ExistsOper180(self):
        return self.__sql_ExistsOper180

    @sql_ExistsOper180.setter
    def sql_ExistsOper180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ExistsOper__sql_ExistsOper180", None)
        self.__sql_ExistsOper180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_SubQueryOperand181"):
                opp_val = getattr(old_value, "sql_SubQueryOperand181", None)
                if opp_val == self:
                    setattr(old_value, "sql_SubQueryOperand181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_SubQueryOperand181"):
                opp_val = getattr(value, "sql_SubQueryOperand181", None)
                setattr(value, "sql_SubQueryOperand181", self)

class sql_InOper:

    def __init__(self, op: str, sql_InOper: "sql_FullExpression" = None, sql_InOper175: "sql_SubQueryOperand" = None, sql_InOper178: "sql_OperandListGroup" = None):
        self.op = op
        self.sql_InOper = sql_InOper
        self.sql_InOper175 = sql_InOper175
        self.sql_InOper178 = sql_InOper178
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

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
            if hasattr(old_value, "sql_FullExpression134"):
                opp_val = getattr(old_value, "sql_FullExpression134", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression134"):
                opp_val = getattr(value, "sql_FullExpression134", None)
                setattr(value, "sql_FullExpression134", self)

    @property
    def sql_InOper175(self):
        return self.__sql_InOper175

    @sql_InOper175.setter
    def sql_InOper175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_InOper__sql_InOper175", None)
        self.__sql_InOper175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_SubQueryOperand176"):
                opp_val = getattr(old_value, "sql_SubQueryOperand176", None)
                if opp_val == self:
                    setattr(old_value, "sql_SubQueryOperand176", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_SubQueryOperand176"):
                opp_val = getattr(value, "sql_SubQueryOperand176", None)
                setattr(value, "sql_SubQueryOperand176", self)

    @property
    def sql_InOper178(self):
        return self.__sql_InOper178

    @sql_InOper178.setter
    def sql_InOper178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_InOper__sql_InOper178", None)
        self.__sql_InOper178 = value
        
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

class sql_XExpr:

    def __init__(self, xf: str, sql_XExpr: "sql_FullExpression" = None, sql_XExpr150: "sql_Operands" = None, sql_XExpr153: "sql_Prms" = None):
        self.xf = xf
        self.sql_XExpr = sql_XExpr
        self.sql_XExpr150 = sql_XExpr150
        self.sql_XExpr153 = sql_XExpr153
        
    @property
    def xf(self) -> str:
        return self.__xf

    @xf.setter
    def xf(self, xf: str):
        self.__xf = xf

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
            if hasattr(old_value, "sql_FullExpression132"):
                opp_val = getattr(old_value, "sql_FullExpression132", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression132"):
                opp_val = getattr(value, "sql_FullExpression132", None)
                setattr(value, "sql_FullExpression132", self)

    @property
    def sql_XExpr153(self):
        return self.__sql_XExpr153

    @sql_XExpr153.setter
    def sql_XExpr153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_XExpr__sql_XExpr153", None)
        self.__sql_XExpr153 = value
        
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
    def sql_XExpr150(self):
        return self.__sql_XExpr150

    @sql_XExpr150.setter
    def sql_XExpr150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_XExpr__sql_XExpr150", None)
        self.__sql_XExpr150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operands151"):
                opp_val = getattr(old_value, "sql_Operands151", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operands151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operands151"):
                opp_val = getattr(value, "sql_Operands151", None)
                setattr(value, "sql_Operands151", self)

class sql_ExprGroup:

    def __init__(self, isnot: str, sql_ExprGroup: "sql_FullExpression" = None, sql_ExprGroup147: "sql_OrExpr" = None):
        self.isnot = isnot
        self.sql_ExprGroup = sql_ExprGroup
        self.sql_ExprGroup147 = sql_ExprGroup147
        
    @property
    def isnot(self) -> str:
        return self.__isnot

    @isnot.setter
    def isnot(self, isnot: str):
        self.__isnot = isnot

    @property
    def sql_ExprGroup147(self):
        return self.__sql_ExprGroup147

    @sql_ExprGroup147.setter
    def sql_ExprGroup147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ExprGroup__sql_ExprGroup147", None)
        self.__sql_ExprGroup147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_OrExpr148"):
                opp_val = getattr(old_value, "sql_OrExpr148", None)
                if opp_val == self:
                    setattr(old_value, "sql_OrExpr148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OrExpr148"):
                opp_val = getattr(value, "sql_OrExpr148", None)
                setattr(value, "sql_OrExpr148", self)

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
            if hasattr(old_value, "sql_FullExpression127"):
                opp_val = getattr(old_value, "sql_FullExpression127", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression127"):
                opp_val = getattr(value, "sql_FullExpression127", None)
                setattr(value, "sql_FullExpression127", self)

class OrExpr:

    pass
class sql_FullExpression(OrExpr):

    def __init__(self, c: str, notPrm: str, isnull: str, sql_FullExpression141: "sql_Between" = None, sql_FullExpression: "sql_OrExpr" = None, sql_FullExpression125: "sql_FullExpression" = None, sql_FullExpression123: "sql_FullExpression" = None, sql_FullExpression127: "sql_ExprGroup" = None, sql_FullExpression130: "sql_FullExpression" = None, sql_FullExpression128: "sql_FullExpression" = None, sql_FullExpression132: "sql_XExpr" = None, sql_FullExpression134: "sql_InOper" = None, sql_FullExpression136: "sql_ExistsOper" = None, sql_FullExpression138: "sql_Operands" = None, sql_FullExpression143: "sql_Like" = None, sql_FullExpression145: "sql_Comparison" = None):
        self.c = c
        self.notPrm = notPrm
        self.isnull = isnull
        self.sql_FullExpression141 = sql_FullExpression141
        self.sql_FullExpression = sql_FullExpression
        self.sql_FullExpression125 = sql_FullExpression125
        self.sql_FullExpression123 = sql_FullExpression123
        self.sql_FullExpression127 = sql_FullExpression127
        self.sql_FullExpression130 = sql_FullExpression130
        self.sql_FullExpression128 = sql_FullExpression128
        self.sql_FullExpression132 = sql_FullExpression132
        self.sql_FullExpression134 = sql_FullExpression134
        self.sql_FullExpression136 = sql_FullExpression136
        self.sql_FullExpression138 = sql_FullExpression138
        self.sql_FullExpression143 = sql_FullExpression143
        self.sql_FullExpression145 = sql_FullExpression145
        
    @property
    def isnull(self) -> str:
        return self.__isnull

    @isnull.setter
    def isnull(self, isnull: str):
        self.__isnull = isnull

    @property
    def notPrm(self) -> str:
        return self.__notPrm

    @notPrm.setter
    def notPrm(self, notPrm: str):
        self.__notPrm = notPrm

    @property
    def c(self) -> str:
        return self.__c

    @c.setter
    def c(self, c: str):
        self.__c = c

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
            if hasattr(old_value, "sql_OrExpr122"):
                opp_val = getattr(old_value, "sql_OrExpr122", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OrExpr122"):
                opp_val = getattr(value, "sql_OrExpr122", None)
                if opp_val is None:
                    setattr(value, "sql_OrExpr122", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sql_FullExpression125(self):
        return self.__sql_FullExpression125

    @sql_FullExpression125.setter
    def sql_FullExpression125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression125", None)
        self.__sql_FullExpression125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FullExpression123"):
                opp_val = getattr(old_value, "sql_FullExpression123", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression123"):
                opp_val = getattr(value, "sql_FullExpression123", None)
                setattr(value, "sql_FullExpression123", self)

    @property
    def sql_FullExpression138(self):
        return self.__sql_FullExpression138

    @sql_FullExpression138.setter
    def sql_FullExpression138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression138", None)
        self.__sql_FullExpression138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operands139"):
                opp_val = getattr(old_value, "sql_Operands139", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operands139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operands139"):
                opp_val = getattr(value, "sql_Operands139", None)
                setattr(value, "sql_Operands139", self)

    @property
    def sql_FullExpression134(self):
        return self.__sql_FullExpression134

    @sql_FullExpression134.setter
    def sql_FullExpression134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression134", None)
        self.__sql_FullExpression134 = value
        
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
    def sql_FullExpression136(self):
        return self.__sql_FullExpression136

    @sql_FullExpression136.setter
    def sql_FullExpression136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression136", None)
        self.__sql_FullExpression136 = value
        
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
    def sql_FullExpression123(self):
        return self.__sql_FullExpression123

    @sql_FullExpression123.setter
    def sql_FullExpression123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression123", None)
        self.__sql_FullExpression123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FullExpression125"):
                opp_val = getattr(old_value, "sql_FullExpression125", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression125"):
                opp_val = getattr(value, "sql_FullExpression125", None)
                setattr(value, "sql_FullExpression125", self)

    @property
    def sql_FullExpression127(self):
        return self.__sql_FullExpression127

    @sql_FullExpression127.setter
    def sql_FullExpression127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression127", None)
        self.__sql_FullExpression127 = value
        
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
    def sql_FullExpression130(self):
        return self.__sql_FullExpression130

    @sql_FullExpression130.setter
    def sql_FullExpression130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression130", None)
        self.__sql_FullExpression130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FullExpression128"):
                opp_val = getattr(old_value, "sql_FullExpression128", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression128"):
                opp_val = getattr(value, "sql_FullExpression128", None)
                setattr(value, "sql_FullExpression128", self)

    @property
    def sql_FullExpression145(self):
        return self.__sql_FullExpression145

    @sql_FullExpression145.setter
    def sql_FullExpression145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression145", None)
        self.__sql_FullExpression145 = value
        
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

    @property
    def sql_FullExpression141(self):
        return self.__sql_FullExpression141

    @sql_FullExpression141.setter
    def sql_FullExpression141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression141", None)
        self.__sql_FullExpression141 = value
        
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
    def sql_FullExpression143(self):
        return self.__sql_FullExpression143

    @sql_FullExpression143.setter
    def sql_FullExpression143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression143", None)
        self.__sql_FullExpression143 = value
        
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
    def sql_FullExpression132(self):
        return self.__sql_FullExpression132

    @sql_FullExpression132.setter
    def sql_FullExpression132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression132", None)
        self.__sql_FullExpression132 = value
        
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
    def sql_FullExpression128(self):
        return self.__sql_FullExpression128

    @sql_FullExpression128.setter
    def sql_FullExpression128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression128", None)
        self.__sql_FullExpression128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FullExpression130"):
                opp_val = getattr(old_value, "sql_FullExpression130", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression130"):
                opp_val = getattr(value, "sql_FullExpression130", None)
                setattr(value, "sql_FullExpression130", self)

class sql_Between:

    def __init__(self, opBetween: str, sql_Between: "sql_FullExpression" = None, sql_Between169: "sql_Operands" = None, sql_Between172: "sql_Operands" = None):
        self.opBetween = opBetween
        self.sql_Between = sql_Between
        self.sql_Between169 = sql_Between169
        self.sql_Between172 = sql_Between172
        
    @property
    def opBetween(self) -> str:
        return self.__opBetween

    @opBetween.setter
    def opBetween(self, opBetween: str):
        self.__opBetween = opBetween

    @property
    def sql_Between169(self):
        return self.__sql_Between169

    @sql_Between169.setter
    def sql_Between169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Between__sql_Between169", None)
        self.__sql_Between169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operands170"):
                opp_val = getattr(old_value, "sql_Operands170", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operands170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operands170"):
                opp_val = getattr(value, "sql_Operands170", None)
                setattr(value, "sql_Operands170", self)

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
            if hasattr(old_value, "sql_FullExpression141"):
                opp_val = getattr(old_value, "sql_FullExpression141", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression141"):
                opp_val = getattr(value, "sql_FullExpression141", None)
                setattr(value, "sql_FullExpression141", self)

    @property
    def sql_Between172(self):
        return self.__sql_Between172

    @sql_Between172.setter
    def sql_Between172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Between__sql_Between172", None)
        self.__sql_Between172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operands173"):
                opp_val = getattr(old_value, "sql_Operands173", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operands173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operands173"):
                opp_val = getattr(value, "sql_Operands173", None)
                setattr(value, "sql_Operands173", self)

class OrGroupByColumn:

    pass
class sql_GroupByColumnFull(OrGroupByColumn):

    def __init__(self, grByInt: str, sql_GroupByColumnFull117: "sql_ColumnFull" = None, sql_GroupByColumnFull120: "sql_OpFunction" = None, sql_GroupByColumnFull: "sql_OrGroupByColumn" = None):
        self.grByInt = grByInt
        self.sql_GroupByColumnFull117 = sql_GroupByColumnFull117
        self.sql_GroupByColumnFull120 = sql_GroupByColumnFull120
        self.sql_GroupByColumnFull = sql_GroupByColumnFull
        
    @property
    def grByInt(self) -> str:
        return self.__grByInt

    @grByInt.setter
    def grByInt(self, grByInt: str):
        self.__grByInt = grByInt

    @property
    def sql_GroupByColumnFull120(self):
        return self.__sql_GroupByColumnFull120

    @sql_GroupByColumnFull120.setter
    def sql_GroupByColumnFull120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_GroupByColumnFull__sql_GroupByColumnFull120", None)
        self.__sql_GroupByColumnFull120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_OpFunction"):
                opp_val = getattr(old_value, "sql_OpFunction", None)
                if opp_val == self:
                    setattr(old_value, "sql_OpFunction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OpFunction"):
                opp_val = getattr(value, "sql_OpFunction", None)
                setattr(value, "sql_OpFunction", self)

    @property
    def sql_GroupByColumnFull117(self):
        return self.__sql_GroupByColumnFull117

    @sql_GroupByColumnFull117.setter
    def sql_GroupByColumnFull117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_GroupByColumnFull__sql_GroupByColumnFull117", None)
        self.__sql_GroupByColumnFull117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_ColumnFull118"):
                opp_val = getattr(old_value, "sql_ColumnFull118", None)
                if opp_val == self:
                    setattr(old_value, "sql_ColumnFull118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_ColumnFull118"):
                opp_val = getattr(value, "sql_ColumnFull118", None)
                setattr(value, "sql_ColumnFull118", self)

    @property
    def sql_GroupByColumnFull(self):
        return self.__sql_GroupByColumnFull

    @sql_GroupByColumnFull.setter
    def sql_GroupByColumnFull(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_GroupByColumnFull__sql_GroupByColumnFull", None)
        self.__sql_GroupByColumnFull = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_OrGroupByColumn115"):
                opp_val = getattr(old_value, "sql_OrGroupByColumn115", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OrGroupByColumn115"):
                opp_val = getattr(value, "sql_OrGroupByColumn115", None)
                if opp_val is None:
                    setattr(value, "sql_OrGroupByColumn115", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class OrOrderByColumn:

    pass
class sql_OrderByColumnFull(OrOrderByColumn):

    def __init__(self, colOrderInt: str, direction: str, sql_OrderByColumnFull: "sql_OrOrderByColumn" = None, sql_OrderByColumnFull113: "sql_ColumnFull" = None):
        self.colOrderInt = colOrderInt
        self.direction = direction
        self.sql_OrderByColumnFull = sql_OrderByColumnFull
        self.sql_OrderByColumnFull113 = sql_OrderByColumnFull113
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def colOrderInt(self) -> str:
        return self.__colOrderInt

    @colOrderInt.setter
    def colOrderInt(self, colOrderInt: str):
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
            if hasattr(old_value, "sql_OrOrderByColumn111"):
                opp_val = getattr(old_value, "sql_OrOrderByColumn111", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OrOrderByColumn111"):
                opp_val = getattr(value, "sql_OrOrderByColumn111", None)
                if opp_val is None:
                    setattr(value, "sql_OrOrderByColumn111", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sql_OrderByColumnFull113(self):
        return self.__sql_OrderByColumnFull113

    @sql_OrderByColumnFull113.setter
    def sql_OrderByColumnFull113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_OrderByColumnFull__sql_OrderByColumnFull113", None)
        self.__sql_OrderByColumnFull113 = value
        
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
class UsingCols:

    pass
class ColumnFull:

    pass
class sql_Col(ColumnFull):

    pass
class Pivots:

    pass
class sql_pvcs(Pivots):

    pass
class PivotFunction:

    pass
class PivotColumns:

    pass
class sql_PivotCol(Pivots, PivotFunction, PivotColumns):

    pass
class sql_Pivots(PivotColumns):

    pass
class sql_OpFunction:

    def __init__(self, fname: str, star: str, sql_OpFunction: "sql_GroupByColumnFull" = None, sql_OpFunction163: "sql_LikeOperand" = None, sql_OpFunction210: "sql_Operand" = None, sql_OpFunction221: "sql_OpFunctionArg" = None, sql_OpFunction223: "sql_FunctionAnalytical" = None):
        self.fname = fname
        self.star = star
        self.sql_OpFunction = sql_OpFunction
        self.sql_OpFunction163 = sql_OpFunction163
        self.sql_OpFunction210 = sql_OpFunction210
        self.sql_OpFunction221 = sql_OpFunction221
        self.sql_OpFunction223 = sql_OpFunction223
        
    @property
    def star(self) -> str:
        return self.__star

    @star.setter
    def star(self, star: str):
        self.__star = star

    @property
    def fname(self) -> str:
        return self.__fname

    @fname.setter
    def fname(self, fname: str):
        self.__fname = fname

    @property
    def sql_OpFunction210(self):
        return self.__sql_OpFunction210

    @sql_OpFunction210.setter
    def sql_OpFunction210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_OpFunction__sql_OpFunction210", None)
        self.__sql_OpFunction210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operand209"):
                opp_val = getattr(old_value, "sql_Operand209", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operand209", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operand209"):
                opp_val = getattr(value, "sql_Operand209", None)
                setattr(value, "sql_Operand209", self)

    @property
    def sql_OpFunction221(self):
        return self.__sql_OpFunction221

    @sql_OpFunction221.setter
    def sql_OpFunction221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_OpFunction__sql_OpFunction221", None)
        self.__sql_OpFunction221 = value
        
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
    def sql_OpFunction223(self):
        return self.__sql_OpFunction223

    @sql_OpFunction223.setter
    def sql_OpFunction223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_OpFunction__sql_OpFunction223", None)
        self.__sql_OpFunction223 = value
        
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
    def sql_OpFunction163(self):
        return self.__sql_OpFunction163

    @sql_OpFunction163.setter
    def sql_OpFunction163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_OpFunction__sql_OpFunction163", None)
        self.__sql_OpFunction163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_LikeOperand162"):
                opp_val = getattr(old_value, "sql_LikeOperand162", None)
                if opp_val == self:
                    setattr(old_value, "sql_LikeOperand162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_LikeOperand162"):
                opp_val = getattr(value, "sql_LikeOperand162", None)
                setattr(value, "sql_LikeOperand162", self)

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
            if hasattr(old_value, "sql_GroupByColumnFull120"):
                opp_val = getattr(old_value, "sql_GroupByColumnFull120", None)
                if opp_val == self:
                    setattr(old_value, "sql_GroupByColumnFull120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_GroupByColumnFull120"):
                opp_val = getattr(value, "sql_GroupByColumnFull120", None)
                setattr(value, "sql_GroupByColumnFull120", self)

class UnpivotInClauseArgs:

    pass
class sql_uicargs(UnpivotInClauseArgs):

    pass
class sql_UnpivotInClauseArg(UnpivotInClauseArgs):

    pass
class sql_UnpivotInClause:

    pass
class sql_PivotColumns:

    pass
class sql_UnpivotInClauseArgs:

    pass
class sql_PivotFunction:

    pass
class sql_PivotInClause:

    def __init__(self, pinany: str, sql_PivotInClause: "sql_PivotTable" = None, sql_PivotInClause94: "sql_SubQueryOperand" = None, sql_PivotInClause97: "sql_UnpivotInClauseArgs" = None):
        self.pinany = pinany
        self.sql_PivotInClause = sql_PivotInClause
        self.sql_PivotInClause94 = sql_PivotInClause94
        self.sql_PivotInClause97 = sql_PivotInClause97
        
    @property
    def pinany(self) -> str:
        return self.__pinany

    @pinany.setter
    def pinany(self, pinany: str):
        self.__pinany = pinany

    @property
    def sql_PivotInClause97(self):
        return self.__sql_PivotInClause97

    @sql_PivotInClause97.setter
    def sql_PivotInClause97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_PivotInClause__sql_PivotInClause97", None)
        self.__sql_PivotInClause97 = value
        
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
    def sql_PivotInClause94(self):
        return self.__sql_PivotInClause94

    @sql_PivotInClause94.setter
    def sql_PivotInClause94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_PivotInClause__sql_PivotInClause94", None)
        self.__sql_PivotInClause94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_SubQueryOperand95"):
                opp_val = getattr(old_value, "sql_SubQueryOperand95", None)
                if opp_val == self:
                    setattr(old_value, "sql_SubQueryOperand95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_SubQueryOperand95"):
                opp_val = getattr(value, "sql_SubQueryOperand95", None)
                setattr(value, "sql_SubQueryOperand95", self)

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
            if hasattr(old_value, "sql_PivotTable92"):
                opp_val = getattr(old_value, "sql_PivotTable92", None)
                if opp_val == self:
                    setattr(old_value, "sql_PivotTable92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_PivotTable92"):
                opp_val = getattr(value, "sql_PivotTable92", None)
                setattr(value, "sql_PivotTable92", self)

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
            if hasattr(old_value, "sql_PivotTable88"):
                opp_val = getattr(old_value, "sql_PivotTable88", None)
                if opp_val == self:
                    setattr(old_value, "sql_PivotTable88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_PivotTable88"):
                opp_val = getattr(value, "sql_PivotTable88", None)
                setattr(value, "sql_PivotTable88", self)

class RowValues:

    pass
class sql_RowValue(RowValues):

    def __init__(self, null: str, sql_RowValue: "sql_RowValues" = None):
        self.null = null
        self.sql_RowValue = sql_RowValue
        
    @property
    def null(self) -> str:
        return self.__null

    @null.setter
    def null(self, null: str):
        self.__null = null

    @property
    def sql_RowValue(self):
        return self.__sql_RowValue

    @sql_RowValue.setter
    def sql_RowValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_RowValue__sql_RowValue", None)
        self.__sql_RowValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_RowValues86"):
                opp_val = getattr(old_value, "sql_RowValues86", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_RowValues86"):
                opp_val = getattr(value, "sql_RowValues86", None)
                if opp_val is None:
                    setattr(value, "sql_RowValues86", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sql_RowValues:

    pass
class Rows:

    pass
class sql_Row(Rows):

    pass
class sql_Rows:

    pass
class sql_FromValuesColumnNames:

    pass
class sql_FromValuesColumns:

    pass
class sql_Values:

    pass
class sql_UnpivotTable:

    pass
class sql_PivotTable:

    pass
class sql_FromValues:

    pass
class sql_SubQueryOperand:

    pass
class sql_TableFull:

    pass
class WithColumns:

    pass
class sql_UsingCols(WithColumns):

    pass
class sql_JoinCondition:

    pass
class sql_FromTableJoin:

    def __init__(self, join: str, sql_FromTableJoin: "sql_FromTable" = None, sql_FromTableJoin48: "sql_TableOrAlias" = None, sql_FromTableJoin51: "sql_OrExpr" = None, sql_FromTableJoin54: "sql_JoinCondition" = None):
        self.join = join
        self.sql_FromTableJoin = sql_FromTableJoin
        self.sql_FromTableJoin48 = sql_FromTableJoin48
        self.sql_FromTableJoin51 = sql_FromTableJoin51
        self.sql_FromTableJoin54 = sql_FromTableJoin54
        
    @property
    def join(self) -> str:
        return self.__join

    @join.setter
    def join(self, join: str):
        self.__join = join

    @property
    def sql_FromTableJoin48(self):
        return self.__sql_FromTableJoin48

    @sql_FromTableJoin48.setter
    def sql_FromTableJoin48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FromTableJoin__sql_FromTableJoin48", None)
        self.__sql_FromTableJoin48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_TableOrAlias49"):
                opp_val = getattr(old_value, "sql_TableOrAlias49", None)
                if opp_val == self:
                    setattr(old_value, "sql_TableOrAlias49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_TableOrAlias49"):
                opp_val = getattr(value, "sql_TableOrAlias49", None)
                setattr(value, "sql_TableOrAlias49", self)

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
            if hasattr(old_value, "sql_FromTable46"):
                opp_val = getattr(old_value, "sql_FromTable46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FromTable46"):
                opp_val = getattr(value, "sql_FromTable46", None)
                if opp_val is None:
                    setattr(value, "sql_FromTable46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sql_FromTableJoin51(self):
        return self.__sql_FromTableJoin51

    @sql_FromTableJoin51.setter
    def sql_FromTableJoin51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FromTableJoin__sql_FromTableJoin51", None)
        self.__sql_FromTableJoin51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_OrExpr52"):
                opp_val = getattr(old_value, "sql_OrExpr52", None)
                if opp_val == self:
                    setattr(old_value, "sql_OrExpr52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OrExpr52"):
                opp_val = getattr(value, "sql_OrExpr52", None)
                setattr(value, "sql_OrExpr52", self)

    @property
    def sql_FromTableJoin54(self):
        return self.__sql_FromTableJoin54

    @sql_FromTableJoin54.setter
    def sql_FromTableJoin54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FromTableJoin__sql_FromTableJoin54", None)
        self.__sql_FromTableJoin54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_JoinCondition"):
                opp_val = getattr(old_value, "sql_JoinCondition", None)
                if opp_val == self:
                    setattr(old_value, "sql_JoinCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_JoinCondition"):
                opp_val = getattr(value, "sql_JoinCondition", None)
                setattr(value, "sql_JoinCondition", self)

class sql_TableOrAlias:

    def __init__(self, alias: str, sql_TableOrAlias: "sql_FromTable" = None, sql_TableOrAlias49: "sql_FromTableJoin" = None, sql_TableOrAlias61: "sql_TableFull" = None, sql_TableOrAlias63: "sql_SubQueryOperand" = None, sql_TableOrAlias65: "sql_FromValues" = None, sql_TableOrAlias67: "sql_PivotTable" = None, sql_TableOrAlias69: "sql_UnpivotTable" = None, sql_TableOrAlias71: "sql_DbObjectName" = None):
        self.alias = alias
        self.sql_TableOrAlias = sql_TableOrAlias
        self.sql_TableOrAlias49 = sql_TableOrAlias49
        self.sql_TableOrAlias61 = sql_TableOrAlias61
        self.sql_TableOrAlias63 = sql_TableOrAlias63
        self.sql_TableOrAlias65 = sql_TableOrAlias65
        self.sql_TableOrAlias67 = sql_TableOrAlias67
        self.sql_TableOrAlias69 = sql_TableOrAlias69
        self.sql_TableOrAlias71 = sql_TableOrAlias71
        
    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

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
            if hasattr(old_value, "sql_FromTable44"):
                opp_val = getattr(old_value, "sql_FromTable44", None)
                if opp_val == self:
                    setattr(old_value, "sql_FromTable44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FromTable44"):
                opp_val = getattr(value, "sql_FromTable44", None)
                setattr(value, "sql_FromTable44", self)

    @property
    def sql_TableOrAlias63(self):
        return self.__sql_TableOrAlias63

    @sql_TableOrAlias63.setter
    def sql_TableOrAlias63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_TableOrAlias__sql_TableOrAlias63", None)
        self.__sql_TableOrAlias63 = value
        
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

    @property
    def sql_TableOrAlias71(self):
        return self.__sql_TableOrAlias71

    @sql_TableOrAlias71.setter
    def sql_TableOrAlias71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_TableOrAlias__sql_TableOrAlias71", None)
        self.__sql_TableOrAlias71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_DbObjectName72"):
                opp_val = getattr(old_value, "sql_DbObjectName72", None)
                if opp_val == self:
                    setattr(old_value, "sql_DbObjectName72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_DbObjectName72"):
                opp_val = getattr(value, "sql_DbObjectName72", None)
                setattr(value, "sql_DbObjectName72", self)

    @property
    def sql_TableOrAlias67(self):
        return self.__sql_TableOrAlias67

    @sql_TableOrAlias67.setter
    def sql_TableOrAlias67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_TableOrAlias__sql_TableOrAlias67", None)
        self.__sql_TableOrAlias67 = value
        
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
    def sql_TableOrAlias49(self):
        return self.__sql_TableOrAlias49

    @sql_TableOrAlias49.setter
    def sql_TableOrAlias49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_TableOrAlias__sql_TableOrAlias49", None)
        self.__sql_TableOrAlias49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FromTableJoin48"):
                opp_val = getattr(old_value, "sql_FromTableJoin48", None)
                if opp_val == self:
                    setattr(old_value, "sql_FromTableJoin48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FromTableJoin48"):
                opp_val = getattr(value, "sql_FromTableJoin48", None)
                setattr(value, "sql_FromTableJoin48", self)

    @property
    def sql_TableOrAlias65(self):
        return self.__sql_TableOrAlias65

    @sql_TableOrAlias65.setter
    def sql_TableOrAlias65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_TableOrAlias__sql_TableOrAlias65", None)
        self.__sql_TableOrAlias65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FromValues"):
                opp_val = getattr(old_value, "sql_FromValues", None)
                if opp_val == self:
                    setattr(old_value, "sql_FromValues", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FromValues"):
                opp_val = getattr(value, "sql_FromValues", None)
                setattr(value, "sql_FromValues", self)

    @property
    def sql_TableOrAlias69(self):
        return self.__sql_TableOrAlias69

    @sql_TableOrAlias69.setter
    def sql_TableOrAlias69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_TableOrAlias__sql_TableOrAlias69", None)
        self.__sql_TableOrAlias69 = value
        
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
    def sql_TableOrAlias61(self):
        return self.__sql_TableOrAlias61

    @sql_TableOrAlias61.setter
    def sql_TableOrAlias61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_TableOrAlias__sql_TableOrAlias61", None)
        self.__sql_TableOrAlias61 = value
        
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

class OrTable:

    pass
class sql_FromTable(OrTable):

    pass
class FromValuesColumnNames:

    pass
class sql_abc(FromValuesColumnNames):

    pass
class sql_ColumnNames(FromValuesColumnNames):

    def __init__(self, colName: str, sql_ColumnNames: "sql_abc" = None):
        self.colName = colName
        self.sql_ColumnNames = sql_ColumnNames
        
    @property
    def colName(self) -> str:
        return self.__colName

    @colName.setter
    def colName(self, colName: str):
        self.__colName = colName

    @property
    def sql_ColumnNames(self):
        return self.__sql_ColumnNames

    @sql_ColumnNames.setter
    def sql_ColumnNames(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ColumnNames__sql_ColumnNames", None)
        self.__sql_ColumnNames = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_abc"):
                opp_val = getattr(old_value, "sql_abc", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_abc"):
                opp_val = getattr(value, "sql_abc", None)
                if opp_val is None:
                    setattr(value, "sql_abc", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "sql_ColumnOrAlias40"):
                opp_val = getattr(old_value, "sql_ColumnOrAlias40", None)
                if opp_val == self:
                    setattr(old_value, "sql_ColumnOrAlias40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_ColumnOrAlias40"):
                opp_val = getattr(value, "sql_ColumnOrAlias40", None)
                setattr(value, "sql_ColumnOrAlias40", self)

class sql_DbObjectName(TableFull, UsingCols, PivotCol, ColumnFull):

    def __init__(self, dbname: str, sql_DbObjectName: "sql_ColumnOrAlias" = None, sql_DbObjectName59: "sql_UsingCols" = None, sql_DbObjectName72: "sql_TableOrAlias" = None, sql_DbObjectName254: "sql_AnalyticExprArg" = None, sql_DbObjectName293: "sql_pcols" = None, sql_DbObjectName285: "sql_Col" = None, sql_DbObjectName295: "sql_tbls" = None):
        self.dbname = dbname
        self.sql_DbObjectName = sql_DbObjectName
        self.sql_DbObjectName59 = sql_DbObjectName59
        self.sql_DbObjectName72 = sql_DbObjectName72
        self.sql_DbObjectName254 = sql_DbObjectName254
        self.sql_DbObjectName293 = sql_DbObjectName293
        self.sql_DbObjectName285 = sql_DbObjectName285
        self.sql_DbObjectName295 = sql_DbObjectName295
        
    @property
    def dbname(self) -> str:
        return self.__dbname

    @dbname.setter
    def dbname(self, dbname: str):
        self.__dbname = dbname

    @property
    def sql_DbObjectName254(self):
        return self.__sql_DbObjectName254

    @sql_DbObjectName254.setter
    def sql_DbObjectName254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_DbObjectName__sql_DbObjectName254", None)
        self.__sql_DbObjectName254 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_AnalyticExprArg253"):
                opp_val = getattr(old_value, "sql_AnalyticExprArg253", None)
                if opp_val == self:
                    setattr(old_value, "sql_AnalyticExprArg253", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_AnalyticExprArg253"):
                opp_val = getattr(value, "sql_AnalyticExprArg253", None)
                setattr(value, "sql_AnalyticExprArg253", self)

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
            if hasattr(old_value, "sql_UsingCols58"):
                opp_val = getattr(old_value, "sql_UsingCols58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_UsingCols58"):
                opp_val = getattr(value, "sql_UsingCols58", None)
                if opp_val is None:
                    setattr(value, "sql_UsingCols58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sql_DbObjectName295(self):
        return self.__sql_DbObjectName295

    @sql_DbObjectName295.setter
    def sql_DbObjectName295(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_DbObjectName__sql_DbObjectName295", None)
        self.__sql_DbObjectName295 = value
        
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
    def sql_DbObjectName285(self):
        return self.__sql_DbObjectName285

    @sql_DbObjectName285.setter
    def sql_DbObjectName285(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_DbObjectName__sql_DbObjectName285", None)
        self.__sql_DbObjectName285 = value
        
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

    @property
    def sql_DbObjectName72(self):
        return self.__sql_DbObjectName72

    @sql_DbObjectName72.setter
    def sql_DbObjectName72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_DbObjectName__sql_DbObjectName72", None)
        self.__sql_DbObjectName72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_TableOrAlias71"):
                opp_val = getattr(old_value, "sql_TableOrAlias71", None)
                if opp_val == self:
                    setattr(old_value, "sql_TableOrAlias71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_TableOrAlias71"):
                opp_val = getattr(value, "sql_TableOrAlias71", None)
                setattr(value, "sql_TableOrAlias71", self)

    @property
    def sql_DbObjectName293(self):
        return self.__sql_DbObjectName293

    @sql_DbObjectName293.setter
    def sql_DbObjectName293(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_DbObjectName__sql_DbObjectName293", None)
        self.__sql_DbObjectName293 = value
        
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
            if hasattr(old_value, "sql_ColumnOrAlias38"):
                opp_val = getattr(old_value, "sql_ColumnOrAlias38", None)
                if opp_val == self:
                    setattr(old_value, "sql_ColumnOrAlias38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_ColumnOrAlias38"):
                opp_val = getattr(value, "sql_ColumnOrAlias38", None)
                setattr(value, "sql_ColumnOrAlias38", self)

class sql_Operands(OpFunctionArgAgregate):

    pass
class OrColumn:

    pass
class sql_ColumnOrAlias(OrColumn):

    def __init__(self, alias: str, allCols: str, sql_ColumnOrAlias: "sql_OrColumn" = None, sql_ColumnOrAlias36: "sql_Operands" = None, sql_ColumnOrAlias38: "sql_DbObjectName" = None, sql_ColumnOrAlias40: "sql_DbObjectNameAll" = None):
        self.alias = alias
        self.allCols = allCols
        self.sql_ColumnOrAlias = sql_ColumnOrAlias
        self.sql_ColumnOrAlias36 = sql_ColumnOrAlias36
        self.sql_ColumnOrAlias38 = sql_ColumnOrAlias38
        self.sql_ColumnOrAlias40 = sql_ColumnOrAlias40
        
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
    def sql_ColumnOrAlias(self):
        return self.__sql_ColumnOrAlias

    @sql_ColumnOrAlias.setter
    def sql_ColumnOrAlias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ColumnOrAlias__sql_ColumnOrAlias", None)
        self.__sql_ColumnOrAlias = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_OrColumn34"):
                opp_val = getattr(old_value, "sql_OrColumn34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OrColumn34"):
                opp_val = getattr(value, "sql_OrColumn34", None)
                if opp_val is None:
                    setattr(value, "sql_OrColumn34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sql_ColumnOrAlias40(self):
        return self.__sql_ColumnOrAlias40

    @sql_ColumnOrAlias40.setter
    def sql_ColumnOrAlias40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ColumnOrAlias__sql_ColumnOrAlias40", None)
        self.__sql_ColumnOrAlias40 = value
        
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
    def sql_ColumnOrAlias38(self):
        return self.__sql_ColumnOrAlias38

    @sql_ColumnOrAlias38.setter
    def sql_ColumnOrAlias38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ColumnOrAlias__sql_ColumnOrAlias38", None)
        self.__sql_ColumnOrAlias38 = value
        
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

class PivotForClause:

    pass
class sql_OrOrderByColumn:

    pass
class sql_OrGroupByColumn:

    pass
class sql_OrExpr:

    pass
class sql_OrTable:

    pass
class sql_OrColumn(PivotForClause):

    pass
class SelectQuery:

    pass
class sql_ColumnFull(PivotForClause):

    pass
class sql_SelectSubSet:

    def __init__(self, op: str, all: str, sql_SelectSubSet: "sql_Select" = None, sql_SelectSubSet12: "sql_Select" = None):
        self.op = op
        self.all = all
        self.sql_SelectSubSet = sql_SelectSubSet
        self.sql_SelectSubSet12 = sql_SelectSubSet12
        
    @property
    def all(self) -> str:
        return self.__all

    @all.setter
    def all(self, all: str):
        self.__all = all

    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def sql_SelectSubSet12(self):
        return self.__sql_SelectSubSet12

    @sql_SelectSubSet12.setter
    def sql_SelectSubSet12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_SelectSubSet__sql_SelectSubSet12", None)
        self.__sql_SelectSubSet12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Select11"):
                opp_val = getattr(old_value, "sql_Select11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Select11"):
                opp_val = getattr(value, "sql_Select11", None)
                if opp_val is None:
                    setattr(value, "sql_Select11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

class sql_Limit:

    def __init__(self, l1: str, l2: str, sql_Limit: "sql_Select" = None):
        self.l1 = l1
        self.l2 = l2
        self.sql_Limit = sql_Limit
        
    @property
    def l2(self) -> str:
        return self.__l2

    @l2.setter
    def l2(self, l2: str):
        self.__l2 = l2

    @property
    def l1(self) -> str:
        return self.__l1

    @l1.setter
    def l1(self, l1: str):
        self.__l1 = l1

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
            if hasattr(old_value, "sql_Select27"):
                opp_val = getattr(old_value, "sql_Select27", None)
                if opp_val == self:
                    setattr(old_value, "sql_Select27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Select27"):
                opp_val = getattr(value, "sql_Select27", None)
                setattr(value, "sql_Select27", self)

class sql_Offset:

    def __init__(self, offset: str, sql_Offset: "sql_Select" = None):
        self.offset = offset
        self.sql_Offset = sql_Offset
        
    @property
    def offset(self) -> str:
        return self.__offset

    @offset.setter
    def offset(self, offset: str):
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
            if hasattr(old_value, "sql_Select29"):
                opp_val = getattr(old_value, "sql_Select29", None)
                if opp_val == self:
                    setattr(old_value, "sql_Select29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Select29"):
                opp_val = getattr(value, "sql_Select29", None)
                setattr(value, "sql_Select29", self)

class sql_UnsignedValue:

    def __init__(self, integer: str, sql_UnsignedValue: "sql_FetchFirst" = None):
        self.integer = integer
        self.sql_UnsignedValue = sql_UnsignedValue
        
    @property
    def integer(self) -> str:
        return self.__integer

    @integer.setter
    def integer(self, integer: str):
        self.__integer = integer

    @property
    def sql_UnsignedValue(self):
        return self.__sql_UnsignedValue

    @sql_UnsignedValue.setter
    def sql_UnsignedValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_UnsignedValue__sql_UnsignedValue", None)
        self.__sql_UnsignedValue = value
        
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

    def __init__(self, row: str, sql_FetchFirst: "sql_UnsignedValue" = None, sql_FetchFirst32: "sql_Select" = None):
        self.row = row
        self.sql_FetchFirst = sql_FetchFirst
        self.sql_FetchFirst32 = sql_FetchFirst32
        
    @property
    def row(self) -> str:
        return self.__row

    @row.setter
    def row(self, row: str):
        self.__row = row

    @property
    def sql_FetchFirst32(self):
        return self.__sql_FetchFirst32

    @sql_FetchFirst32.setter
    def sql_FetchFirst32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FetchFirst__sql_FetchFirst32", None)
        self.__sql_FetchFirst32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Select31"):
                opp_val = getattr(old_value, "sql_Select31", None)
                if opp_val == self:
                    setattr(old_value, "sql_Select31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Select31"):
                opp_val = getattr(value, "sql_Select31", None)
                setattr(value, "sql_Select31", self)

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
            if hasattr(old_value, "sql_UnsignedValue"):
                opp_val = getattr(old_value, "sql_UnsignedValue", None)
                if opp_val == self:
                    setattr(old_value, "sql_UnsignedValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_UnsignedValue"):
                opp_val = getattr(value, "sql_UnsignedValue", None)
                setattr(value, "sql_UnsignedValue", self)

class sql_WithColumns:

    pass
class sql_SelectQuery:

    pass
class sql_WithQuery:

    def __init__(self, w: str, wname: str, sql_WithQuery: "sql_Model" = None, sql_WithQuery4: "sql_WithColumns" = None, sql_WithQuery6: "sql_SelectQuery" = None):
        self.w = w
        self.wname = wname
        self.sql_WithQuery = sql_WithQuery
        self.sql_WithQuery4 = sql_WithQuery4
        self.sql_WithQuery6 = sql_WithQuery6
        
    @property
    def w(self) -> str:
        return self.__w

    @w.setter
    def w(self, w: str):
        self.__w = w

    @property
    def wname(self) -> str:
        return self.__wname

    @wname.setter
    def wname(self, wname: str):
        self.__wname = wname

    @property
    def sql_WithQuery(self):
        return self.__sql_WithQuery

    @sql_WithQuery.setter
    def sql_WithQuery(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_WithQuery__sql_WithQuery", None)
        self.__sql_WithQuery = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Model"):
                opp_val = getattr(old_value, "sql_Model", None)
                if opp_val == self:
                    setattr(old_value, "sql_Model", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Model"):
                opp_val = getattr(value, "sql_Model", None)
                setattr(value, "sql_Model", self)

    @property
    def sql_WithQuery4(self):
        return self.__sql_WithQuery4

    @sql_WithQuery4.setter
    def sql_WithQuery4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_WithQuery__sql_WithQuery4", None)
        self.__sql_WithQuery4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_WithColumns"):
                opp_val = getattr(old_value, "sql_WithColumns", None)
                if opp_val == self:
                    setattr(old_value, "sql_WithColumns", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_WithColumns"):
                opp_val = getattr(value, "sql_WithColumns", None)
                setattr(value, "sql_WithColumns", self)

    @property
    def sql_WithQuery6(self):
        return self.__sql_WithQuery6

    @sql_WithQuery6.setter
    def sql_WithQuery6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_WithQuery__sql_WithQuery6", None)
        self.__sql_WithQuery6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_SelectQuery7"):
                opp_val = getattr(old_value, "sql_SelectQuery7", None)
                if opp_val == self:
                    setattr(old_value, "sql_SelectQuery7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_SelectQuery7"):
                opp_val = getattr(value, "sql_SelectQuery7", None)
                setattr(value, "sql_SelectQuery7", self)

class sql_Model:

    pass
class sql_Select(SelectQuery):

    def __init__(self, select: str, sql_Select: "sql_SelectSubSet" = None, sql_Select11: set["sql_SelectSubSet"] = None, sql_Select14: "sql_OrColumn" = None, sql_Select16: "sql_OrTable" = None, sql_Select18: "sql_OrExpr" = None, sql_Select20: "sql_OrGroupByColumn" = None, sql_Select22: "sql_OrExpr" = None, sql_Select25: "sql_OrOrderByColumn" = None, sql_Select27: "sql_Limit" = None, sql_Select29: "sql_Offset" = None, sql_Select31: "sql_FetchFirst" = None):
        self.select = select
        self.sql_Select = sql_Select
        self.sql_Select11 = sql_Select11 if sql_Select11 is not None else set()
        self.sql_Select14 = sql_Select14
        self.sql_Select16 = sql_Select16
        self.sql_Select18 = sql_Select18
        self.sql_Select20 = sql_Select20
        self.sql_Select22 = sql_Select22
        self.sql_Select25 = sql_Select25
        self.sql_Select27 = sql_Select27
        self.sql_Select29 = sql_Select29
        self.sql_Select31 = sql_Select31
        
    @property
    def select(self) -> str:
        return self.__select

    @select.setter
    def select(self, select: str):
        self.__select = select

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
            if hasattr(old_value, "sql_OrExpr23"):
                opp_val = getattr(old_value, "sql_OrExpr23", None)
                if opp_val == self:
                    setattr(old_value, "sql_OrExpr23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OrExpr23"):
                opp_val = getattr(value, "sql_OrExpr23", None)
                setattr(value, "sql_OrExpr23", self)

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
    def sql_Select29(self):
        return self.__sql_Select29

    @sql_Select29.setter
    def sql_Select29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Select__sql_Select29", None)
        self.__sql_Select29 = value
        
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
    def sql_Select14(self):
        return self.__sql_Select14

    @sql_Select14.setter
    def sql_Select14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Select__sql_Select14", None)
        self.__sql_Select14 = value
        
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

    @property
    def sql_Select31(self):
        return self.__sql_Select31

    @sql_Select31.setter
    def sql_Select31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Select__sql_Select31", None)
        self.__sql_Select31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FetchFirst32"):
                opp_val = getattr(old_value, "sql_FetchFirst32", None)
                if opp_val == self:
                    setattr(old_value, "sql_FetchFirst32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FetchFirst32"):
                opp_val = getattr(value, "sql_FetchFirst32", None)
                setattr(value, "sql_FetchFirst32", self)

    @property
    def sql_Select18(self):
        return self.__sql_Select18

    @sql_Select18.setter
    def sql_Select18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Select__sql_Select18", None)
        self.__sql_Select18 = value
        
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
    def sql_Select16(self):
        return self.__sql_Select16

    @sql_Select16.setter
    def sql_Select16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Select__sql_Select16", None)
        self.__sql_Select16 = value
        
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
    def sql_Select27(self):
        return self.__sql_Select27

    @sql_Select27.setter
    def sql_Select27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Select__sql_Select27", None)
        self.__sql_Select27 = value
        
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
    def sql_Select20(self):
        return self.__sql_Select20

    @sql_Select20.setter
    def sql_Select20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Select__sql_Select20", None)
        self.__sql_Select20 = value
        
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
    def sql_Select11(self):
        return self.__sql_Select11

    @sql_Select11.setter
    def sql_Select11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Select__sql_Select11", None)
        self.__sql_Select11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sql_SelectSubSet12"):
                    opp_val = getattr(item, "sql_SelectSubSet12", None)
                    
                    if opp_val == self:
                        setattr(item, "sql_SelectSubSet12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sql_SelectSubSet12"):
                    opp_val = getattr(item, "sql_SelectSubSet12", None)
                    
                    setattr(item, "sql_SelectSubSet12", self)
                    
