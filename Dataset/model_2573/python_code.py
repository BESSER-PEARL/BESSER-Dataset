from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

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


############################################
# Definition of Classes
############################################

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
            if hasattr(old_value, "sql_UnpivotInClauseArgs275"):
                opp_val = getattr(old_value, "sql_UnpivotInClauseArgs275", None)
                if opp_val == self:
                    setattr(old_value, "sql_UnpivotInClauseArgs275", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_UnpivotInClauseArgs275"):
                opp_val = getattr(value, "sql_UnpivotInClauseArgs275", None)
                setattr(value, "sql_UnpivotInClauseArgs275", self)

class sql_IntegerValue:

    def __init__(self, integer: str):
        self.integer = integer
        
    @property
    def integer(self) -> str:
        return self.__integer

    @integer.setter
    def integer(self, integer: str):
        self.__integer = integer

class Operands:

    pass
class sql_Division(Operands):

    pass
class sql_Minus(Operands):

    pass
class sql_Multiply(Operands):

    pass
class sql_Concat(Operands):

    pass
class sql_Plus(Operands):

    pass
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
class sql_QueryPartitionClause:

    pass
class sql_AnalyticClause:

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
            if hasattr(old_value, "sql_Operand210"):
                opp_val = getattr(old_value, "sql_Operand210", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operand210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operand210"):
                opp_val = getattr(value, "sql_Operand210", None)
                setattr(value, "sql_Operand210", self)

class sql_SQLCaseOperand:

    pass
class sql_FunctionExtract:

    def __init__(self, v: str, sql_FunctionExtract218: "sql_Operands" = None, sql_FunctionExtract: "sql_Operand" = None):
        self.v = v
        self.sql_FunctionExtract218 = sql_FunctionExtract218
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
            if hasattr(old_value, "sql_Operand200"):
                opp_val = getattr(old_value, "sql_Operand200", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operand200", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operand200"):
                opp_val = getattr(value, "sql_Operand200", None)
                setattr(value, "sql_Operand200", self)

    @property
    def sql_FunctionExtract218(self):
        return self.__sql_FunctionExtract218

    @sql_FunctionExtract218.setter
    def sql_FunctionExtract218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FunctionExtract__sql_FunctionExtract218", None)
        self.__sql_FunctionExtract218 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operands219"):
                opp_val = getattr(old_value, "sql_Operands219", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operands219", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operands219"):
                opp_val = getattr(value, "sql_Operands219", None)
                setattr(value, "sql_Operands219", self)

class sql_FunctionAnalytical:

    pass
class sql_OpFunctionArg:

    pass
class sql_ScalarOperand(RowValue, OperandList):

    def __init__(self, sostr: str, sodbl: str, sodate: str, sotime: str, sodt: str, soUInt: str, soint: str, sql_ScalarOperand: "sql_Operand" = None, sql_ScalarOperand284: "sql_OpList" = None):
        self.sostr = sostr
        self.sodbl = sodbl
        self.sodate = sodate
        self.sotime = sotime
        self.sodt = sodt
        self.soUInt = soUInt
        self.soint = soint
        self.sql_ScalarOperand = sql_ScalarOperand
        self.sql_ScalarOperand284 = sql_ScalarOperand284
        
    @property
    def sostr(self) -> str:
        return self.__sostr

    @sostr.setter
    def sostr(self, sostr: str):
        self.__sostr = sostr

    @property
    def sodt(self) -> str:
        return self.__sodt

    @sodt.setter
    def sodt(self, sodt: str):
        self.__sodt = sodt

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
    def soint(self) -> str:
        return self.__soint

    @soint.setter
    def soint(self, soint: str):
        self.__soint = soint

    @property
    def sodbl(self) -> str:
        return self.__sodbl

    @sodbl.setter
    def sodbl(self, sodbl: str):
        self.__sodbl = sodbl

    @property
    def sotime(self) -> str:
        return self.__sotime

    @sotime.setter
    def sotime(self, sotime: str):
        self.__sotime = sotime

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
            if hasattr(old_value, "sql_Operand212"):
                opp_val = getattr(old_value, "sql_Operand212", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operand212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operand212"):
                opp_val = getattr(value, "sql_Operand212", None)
                setattr(value, "sql_Operand212", self)

    @property
    def sql_ScalarOperand284(self):
        return self.__sql_ScalarOperand284

    @sql_ScalarOperand284.setter
    def sql_ScalarOperand284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ScalarOperand__sql_ScalarOperand284", None)
        self.__sql_ScalarOperand284 = value
        
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

class sql_Operand:

    pass
class OpFunctionArgAgregate:

    pass
class sql_OperandList:

    pass
class sql_OperandListGroup:

    pass
class sql_ColumnOperand:

    def __init__(self, ora: str, sql_ColumnOperand: "sql_Operand" = None, sql_ColumnOperand253: "sql_ColumnFull" = None):
        self.ora = ora
        self.sql_ColumnOperand = sql_ColumnOperand
        self.sql_ColumnOperand253 = sql_ColumnOperand253
        
    @property
    def ora(self) -> str:
        return self.__ora

    @ora.setter
    def ora(self, ora: str):
        self.__ora = ora

    @property
    def sql_ColumnOperand253(self):
        return self.__sql_ColumnOperand253

    @sql_ColumnOperand253.setter
    def sql_ColumnOperand253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ColumnOperand__sql_ColumnOperand253", None)
        self.__sql_ColumnOperand253 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_ColumnFull254"):
                opp_val = getattr(old_value, "sql_ColumnFull254", None)
                if opp_val == self:
                    setattr(old_value, "sql_ColumnFull254", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_ColumnFull254"):
                opp_val = getattr(value, "sql_ColumnFull254", None)
                setattr(value, "sql_ColumnFull254", self)

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
            if hasattr(old_value, "sql_Operand189"):
                opp_val = getattr(old_value, "sql_Operand189", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operand189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operand189"):
                opp_val = getattr(value, "sql_Operand189", None)
                setattr(value, "sql_Operand189", self)

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
            if hasattr(old_value, "sql_Prms148"):
                opp_val = getattr(old_value, "sql_Prms148", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Prms148"):
                opp_val = getattr(value, "sql_Prms148", None)
                if opp_val is None:
                    setattr(value, "sql_Prms148", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sql_Prms:

    pass
class sql_POperand:

    def __init__(self, prm: str, sql_POperand: "sql_LikeOperand" = None, sql_POperand208: "sql_Operand" = None):
        self.prm = prm
        self.sql_POperand = sql_POperand
        self.sql_POperand208 = sql_POperand208
        
    @property
    def prm(self) -> str:
        return self.__prm

    @prm.setter
    def prm(self, prm: str):
        self.__prm = prm

    @property
    def sql_POperand208(self):
        return self.__sql_POperand208

    @sql_POperand208.setter
    def sql_POperand208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_POperand__sql_POperand208", None)
        self.__sql_POperand208 = value
        
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
            if hasattr(old_value, "sql_LikeOperand160"):
                opp_val = getattr(old_value, "sql_LikeOperand160", None)
                if opp_val == self:
                    setattr(old_value, "sql_LikeOperand160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_LikeOperand160"):
                opp_val = getattr(value, "sql_LikeOperand160", None)
                setattr(value, "sql_LikeOperand160", self)

class sql_OpFunctionCast:

    def __init__(self, type: str, p: str, p2: str, sql_OpFunctionCast: "sql_LikeOperand" = None, sql_OpFunctionCast198: "sql_Operand" = None, sql_OpFunctionCast250: "sql_Operands" = None):
        self.type = type
        self.p = p
        self.p2 = p2
        self.sql_OpFunctionCast = sql_OpFunctionCast
        self.sql_OpFunctionCast198 = sql_OpFunctionCast198
        self.sql_OpFunctionCast250 = sql_OpFunctionCast250
        
    @property
    def p2(self) -> str:
        return self.__p2

    @p2.setter
    def p2(self, p2: str):
        self.__p2 = p2

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
    def sql_OpFunctionCast250(self):
        return self.__sql_OpFunctionCast250

    @sql_OpFunctionCast250.setter
    def sql_OpFunctionCast250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_OpFunctionCast__sql_OpFunctionCast250", None)
        self.__sql_OpFunctionCast250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operands251"):
                opp_val = getattr(old_value, "sql_Operands251", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operands251", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operands251"):
                opp_val = getattr(value, "sql_Operands251", None)
                setattr(value, "sql_Operands251", self)

    @property
    def sql_OpFunctionCast198(self):
        return self.__sql_OpFunctionCast198

    @sql_OpFunctionCast198.setter
    def sql_OpFunctionCast198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_OpFunctionCast__sql_OpFunctionCast198", None)
        self.__sql_OpFunctionCast198 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operand197"):
                opp_val = getattr(old_value, "sql_Operand197", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operand197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operand197"):
                opp_val = getattr(value, "sql_Operand197", None)
                setattr(value, "sql_Operand197", self)

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
            if hasattr(old_value, "sql_LikeOperand158"):
                opp_val = getattr(old_value, "sql_LikeOperand158", None)
                if opp_val == self:
                    setattr(old_value, "sql_LikeOperand158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_LikeOperand158"):
                opp_val = getattr(value, "sql_LikeOperand158", None)
                setattr(value, "sql_LikeOperand158", self)

class sql_LikeOperand:

    def __init__(self, op2: str, sql_LikeOperand: "sql_Like" = None, sql_LikeOperand155: "sql_OpFunction" = None, sql_LikeOperand158: "sql_OpFunctionCast" = None, sql_LikeOperand160: "sql_POperand" = None):
        self.op2 = op2
        self.sql_LikeOperand = sql_LikeOperand
        self.sql_LikeOperand155 = sql_LikeOperand155
        self.sql_LikeOperand158 = sql_LikeOperand158
        self.sql_LikeOperand160 = sql_LikeOperand160
        
    @property
    def op2(self) -> str:
        return self.__op2

    @op2.setter
    def op2(self, op2: str):
        self.__op2 = op2

    @property
    def sql_LikeOperand158(self):
        return self.__sql_LikeOperand158

    @sql_LikeOperand158.setter
    def sql_LikeOperand158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_LikeOperand__sql_LikeOperand158", None)
        self.__sql_LikeOperand158 = value
        
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
    def sql_LikeOperand160(self):
        return self.__sql_LikeOperand160

    @sql_LikeOperand160.setter
    def sql_LikeOperand160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_LikeOperand__sql_LikeOperand160", None)
        self.__sql_LikeOperand160 = value
        
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
            if hasattr(old_value, "sql_Like153"):
                opp_val = getattr(old_value, "sql_Like153", None)
                if opp_val == self:
                    setattr(old_value, "sql_Like153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Like153"):
                opp_val = getattr(value, "sql_Like153", None)
                setattr(value, "sql_Like153", self)

    @property
    def sql_LikeOperand155(self):
        return self.__sql_LikeOperand155

    @sql_LikeOperand155.setter
    def sql_LikeOperand155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_LikeOperand__sql_LikeOperand155", None)
        self.__sql_LikeOperand155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_OpFunction156"):
                opp_val = getattr(old_value, "sql_OpFunction156", None)
                if opp_val == self:
                    setattr(old_value, "sql_OpFunction156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OpFunction156"):
                opp_val = getattr(value, "sql_OpFunction156", None)
                setattr(value, "sql_OpFunction156", self)

class sql_ExistsOper:

    def __init__(self, op: str, sql_ExistsOper: "sql_FullExpression" = None, sql_ExistsOper173: "sql_SubQueryOperand" = None, sql_ExistsOper176: "sql_OperandListGroup" = None):
        self.op = op
        self.sql_ExistsOper = sql_ExistsOper
        self.sql_ExistsOper173 = sql_ExistsOper173
        self.sql_ExistsOper176 = sql_ExistsOper176
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def sql_ExistsOper173(self):
        return self.__sql_ExistsOper173

    @sql_ExistsOper173.setter
    def sql_ExistsOper173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ExistsOper__sql_ExistsOper173", None)
        self.__sql_ExistsOper173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_SubQueryOperand174"):
                opp_val = getattr(old_value, "sql_SubQueryOperand174", None)
                if opp_val == self:
                    setattr(old_value, "sql_SubQueryOperand174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_SubQueryOperand174"):
                opp_val = getattr(value, "sql_SubQueryOperand174", None)
                setattr(value, "sql_SubQueryOperand174", self)

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
            if hasattr(old_value, "sql_FullExpression129"):
                opp_val = getattr(old_value, "sql_FullExpression129", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression129"):
                opp_val = getattr(value, "sql_FullExpression129", None)
                setattr(value, "sql_FullExpression129", self)

    @property
    def sql_ExistsOper176(self):
        return self.__sql_ExistsOper176

    @sql_ExistsOper176.setter
    def sql_ExistsOper176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ExistsOper__sql_ExistsOper176", None)
        self.__sql_ExistsOper176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_OperandListGroup177"):
                opp_val = getattr(old_value, "sql_OperandListGroup177", None)
                if opp_val == self:
                    setattr(old_value, "sql_OperandListGroup177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OperandListGroup177"):
                opp_val = getattr(value, "sql_OperandListGroup177", None)
                setattr(value, "sql_OperandListGroup177", self)

class sql_InOper:

    def __init__(self, op: str, sql_InOper: "sql_FullExpression" = None, sql_InOper168: "sql_SubQueryOperand" = None, sql_InOper171: "sql_OperandListGroup" = None):
        self.op = op
        self.sql_InOper = sql_InOper
        self.sql_InOper168 = sql_InOper168
        self.sql_InOper171 = sql_InOper171
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def sql_InOper171(self):
        return self.__sql_InOper171

    @sql_InOper171.setter
    def sql_InOper171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_InOper__sql_InOper171", None)
        self.__sql_InOper171 = value
        
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
            if hasattr(old_value, "sql_FullExpression127"):
                opp_val = getattr(old_value, "sql_FullExpression127", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression127"):
                opp_val = getattr(value, "sql_FullExpression127", None)
                setattr(value, "sql_FullExpression127", self)

    @property
    def sql_InOper168(self):
        return self.__sql_InOper168

    @sql_InOper168.setter
    def sql_InOper168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_InOper__sql_InOper168", None)
        self.__sql_InOper168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_SubQueryOperand169"):
                opp_val = getattr(old_value, "sql_SubQueryOperand169", None)
                if opp_val == self:
                    setattr(old_value, "sql_SubQueryOperand169", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_SubQueryOperand169"):
                opp_val = getattr(value, "sql_SubQueryOperand169", None)
                setattr(value, "sql_SubQueryOperand169", self)

class sql_XExpr:

    def __init__(self, xf: str, sql_XExpr: "sql_FullExpression" = None, sql_XExpr143: "sql_Operands" = None, sql_XExpr146: "sql_Prms" = None):
        self.xf = xf
        self.sql_XExpr = sql_XExpr
        self.sql_XExpr143 = sql_XExpr143
        self.sql_XExpr146 = sql_XExpr146
        
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
    def sql_XExpr146(self):
        return self.__sql_XExpr146

    @sql_XExpr146.setter
    def sql_XExpr146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_XExpr__sql_XExpr146", None)
        self.__sql_XExpr146 = value
        
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
    def sql_XExpr143(self):
        return self.__sql_XExpr143

    @sql_XExpr143.setter
    def sql_XExpr143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_XExpr__sql_XExpr143", None)
        self.__sql_XExpr143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operands144"):
                opp_val = getattr(old_value, "sql_Operands144", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operands144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operands144"):
                opp_val = getattr(value, "sql_Operands144", None)
                setattr(value, "sql_Operands144", self)

class sql_ExprGroup:

    def __init__(self, isnot: str, sql_ExprGroup: "sql_FullExpression" = None, sql_ExprGroup140: "sql_OrExpr" = None):
        self.isnot = isnot
        self.sql_ExprGroup = sql_ExprGroup
        self.sql_ExprGroup140 = sql_ExprGroup140
        
    @property
    def isnot(self) -> str:
        return self.__isnot

    @isnot.setter
    def isnot(self, isnot: str):
        self.__isnot = isnot

    @property
    def sql_ExprGroup140(self):
        return self.__sql_ExprGroup140

    @sql_ExprGroup140.setter
    def sql_ExprGroup140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ExprGroup__sql_ExprGroup140", None)
        self.__sql_ExprGroup140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_OrExpr141"):
                opp_val = getattr(old_value, "sql_OrExpr141", None)
                if opp_val == self:
                    setattr(old_value, "sql_OrExpr141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OrExpr141"):
                opp_val = getattr(value, "sql_OrExpr141", None)
                setattr(value, "sql_OrExpr141", self)

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
            if hasattr(old_value, "sql_FullExpression120"):
                opp_val = getattr(old_value, "sql_FullExpression120", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression120"):
                opp_val = getattr(value, "sql_FullExpression120", None)
                setattr(value, "sql_FullExpression120", self)

class OrExpr:

    pass
class sql_FullExpression(OrExpr):

    def __init__(self, isnull: str, c: str, notPrm: str, sql_FullExpression131: "sql_Operands" = None, sql_FullExpression134: "sql_Between" = None, sql_FullExpression136: "sql_Like" = None, sql_FullExpression138: "sql_Comparison" = None, sql_FullExpression: "sql_OrExpr" = None, sql_FullExpression118: "sql_FullExpression" = None, sql_FullExpression116: "sql_FullExpression" = None, sql_FullExpression120: "sql_ExprGroup" = None, sql_FullExpression123: "sql_FullExpression" = None, sql_FullExpression121: "sql_FullExpression" = None, sql_FullExpression125: "sql_XExpr" = None, sql_FullExpression127: "sql_InOper" = None, sql_FullExpression129: "sql_ExistsOper" = None):
        self.isnull = isnull
        self.c = c
        self.notPrm = notPrm
        self.sql_FullExpression131 = sql_FullExpression131
        self.sql_FullExpression134 = sql_FullExpression134
        self.sql_FullExpression136 = sql_FullExpression136
        self.sql_FullExpression138 = sql_FullExpression138
        self.sql_FullExpression = sql_FullExpression
        self.sql_FullExpression118 = sql_FullExpression118
        self.sql_FullExpression116 = sql_FullExpression116
        self.sql_FullExpression120 = sql_FullExpression120
        self.sql_FullExpression123 = sql_FullExpression123
        self.sql_FullExpression121 = sql_FullExpression121
        self.sql_FullExpression125 = sql_FullExpression125
        self.sql_FullExpression127 = sql_FullExpression127
        self.sql_FullExpression129 = sql_FullExpression129
        
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
    def sql_FullExpression120(self):
        return self.__sql_FullExpression120

    @sql_FullExpression120.setter
    def sql_FullExpression120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression120", None)
        self.__sql_FullExpression120 = value
        
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
    def sql_FullExpression116(self):
        return self.__sql_FullExpression116

    @sql_FullExpression116.setter
    def sql_FullExpression116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression116", None)
        self.__sql_FullExpression116 = value
        
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
    def sql_FullExpression121(self):
        return self.__sql_FullExpression121

    @sql_FullExpression121.setter
    def sql_FullExpression121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression121", None)
        self.__sql_FullExpression121 = value
        
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
    def sql_FullExpression(self):
        return self.__sql_FullExpression

    @sql_FullExpression.setter
    def sql_FullExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression", None)
        self.__sql_FullExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_OrExpr115"):
                opp_val = getattr(old_value, "sql_OrExpr115", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OrExpr115"):
                opp_val = getattr(value, "sql_OrExpr115", None)
                if opp_val is None:
                    setattr(value, "sql_OrExpr115", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def sql_FullExpression129(self):
        return self.__sql_FullExpression129

    @sql_FullExpression129.setter
    def sql_FullExpression129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression129", None)
        self.__sql_FullExpression129 = value
        
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
    def sql_FullExpression127(self):
        return self.__sql_FullExpression127

    @sql_FullExpression127.setter
    def sql_FullExpression127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression127", None)
        self.__sql_FullExpression127 = value
        
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
    def sql_FullExpression118(self):
        return self.__sql_FullExpression118

    @sql_FullExpression118.setter
    def sql_FullExpression118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression118", None)
        self.__sql_FullExpression118 = value
        
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
    def sql_FullExpression131(self):
        return self.__sql_FullExpression131

    @sql_FullExpression131.setter
    def sql_FullExpression131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression131", None)
        self.__sql_FullExpression131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operands132"):
                opp_val = getattr(old_value, "sql_Operands132", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operands132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operands132"):
                opp_val = getattr(value, "sql_Operands132", None)
                setattr(value, "sql_Operands132", self)

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
    def sql_FullExpression123(self):
        return self.__sql_FullExpression123

    @sql_FullExpression123.setter
    def sql_FullExpression123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression123", None)
        self.__sql_FullExpression123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FullExpression121"):
                opp_val = getattr(old_value, "sql_FullExpression121", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression121"):
                opp_val = getattr(value, "sql_FullExpression121", None)
                setattr(value, "sql_FullExpression121", self)

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
            if hasattr(old_value, "sql_XExpr"):
                opp_val = getattr(old_value, "sql_XExpr", None)
                if opp_val == self:
                    setattr(old_value, "sql_XExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_XExpr"):
                opp_val = getattr(value, "sql_XExpr", None)
                setattr(value, "sql_XExpr", self)

class sql_Comparison:

    def __init__(self, operator: str, subOperator: str, sql_Comparison: "sql_FullExpression" = None, sql_Comparison150: "sql_Operands" = None):
        self.operator = operator
        self.subOperator = subOperator
        self.sql_Comparison = sql_Comparison
        self.sql_Comparison150 = sql_Comparison150
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def subOperator(self) -> str:
        return self.__subOperator

    @subOperator.setter
    def subOperator(self, subOperator: str):
        self.__subOperator = subOperator

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
            if hasattr(old_value, "sql_FullExpression138"):
                opp_val = getattr(old_value, "sql_FullExpression138", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression138"):
                opp_val = getattr(value, "sql_FullExpression138", None)
                setattr(value, "sql_FullExpression138", self)

    @property
    def sql_Comparison150(self):
        return self.__sql_Comparison150

    @sql_Comparison150.setter
    def sql_Comparison150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Comparison__sql_Comparison150", None)
        self.__sql_Comparison150 = value
        
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

class sql_Like:

    def __init__(self, opLike: str, sql_Like: "sql_FullExpression" = None, sql_Like153: "sql_LikeOperand" = None):
        self.opLike = opLike
        self.sql_Like = sql_Like
        self.sql_Like153 = sql_Like153
        
    @property
    def opLike(self) -> str:
        return self.__opLike

    @opLike.setter
    def opLike(self, opLike: str):
        self.__opLike = opLike

    @property
    def sql_Like153(self):
        return self.__sql_Like153

    @sql_Like153.setter
    def sql_Like153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Like__sql_Like153", None)
        self.__sql_Like153 = value
        
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
            if hasattr(old_value, "sql_FullExpression136"):
                opp_val = getattr(old_value, "sql_FullExpression136", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression136"):
                opp_val = getattr(value, "sql_FullExpression136", None)
                setattr(value, "sql_FullExpression136", self)

class sql_Between:

    def __init__(self, opBetween: str, sql_Between: "sql_FullExpression" = None, sql_Between162: "sql_Operands" = None, sql_Between165: "sql_Operands" = None):
        self.opBetween = opBetween
        self.sql_Between = sql_Between
        self.sql_Between162 = sql_Between162
        self.sql_Between165 = sql_Between165
        
    @property
    def opBetween(self) -> str:
        return self.__opBetween

    @opBetween.setter
    def opBetween(self, opBetween: str):
        self.__opBetween = opBetween

    @property
    def sql_Between165(self):
        return self.__sql_Between165

    @sql_Between165.setter
    def sql_Between165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Between__sql_Between165", None)
        self.__sql_Between165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operands166"):
                opp_val = getattr(old_value, "sql_Operands166", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operands166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operands166"):
                opp_val = getattr(value, "sql_Operands166", None)
                setattr(value, "sql_Operands166", self)

    @property
    def sql_Between162(self):
        return self.__sql_Between162

    @sql_Between162.setter
    def sql_Between162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Between__sql_Between162", None)
        self.__sql_Between162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operands163"):
                opp_val = getattr(old_value, "sql_Operands163", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operands163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operands163"):
                opp_val = getattr(value, "sql_Operands163", None)
                setattr(value, "sql_Operands163", self)

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
            if hasattr(old_value, "sql_FullExpression134"):
                opp_val = getattr(old_value, "sql_FullExpression134", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression134"):
                opp_val = getattr(value, "sql_FullExpression134", None)
                setattr(value, "sql_FullExpression134", self)

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
class sql_PivotCol(PivotFunction, PivotColumns, Pivots):

    pass
class sql_Pivots(PivotColumns):

    pass
class sql_OpFunction:

    def __init__(self, fname: str, star: str, sql_OpFunction: "sql_GroupByColumnFull" = None, sql_OpFunction156: "sql_LikeOperand" = None, sql_OpFunction214: "sql_OpFunctionArg" = None, sql_OpFunction216: "sql_FunctionAnalytical" = None, sql_OpFunction203: "sql_Operand" = None):
        self.fname = fname
        self.star = star
        self.sql_OpFunction = sql_OpFunction
        self.sql_OpFunction156 = sql_OpFunction156
        self.sql_OpFunction214 = sql_OpFunction214
        self.sql_OpFunction216 = sql_OpFunction216
        self.sql_OpFunction203 = sql_OpFunction203
        
    @property
    def fname(self) -> str:
        return self.__fname

    @fname.setter
    def fname(self, fname: str):
        self.__fname = fname

    @property
    def star(self) -> str:
        return self.__star

    @star.setter
    def star(self, star: str):
        self.__star = star

    @property
    def sql_OpFunction203(self):
        return self.__sql_OpFunction203

    @sql_OpFunction203.setter
    def sql_OpFunction203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_OpFunction__sql_OpFunction203", None)
        self.__sql_OpFunction203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operand202"):
                opp_val = getattr(old_value, "sql_Operand202", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operand202", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operand202"):
                opp_val = getattr(value, "sql_Operand202", None)
                setattr(value, "sql_Operand202", self)

    @property
    def sql_OpFunction214(self):
        return self.__sql_OpFunction214

    @sql_OpFunction214.setter
    def sql_OpFunction214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_OpFunction__sql_OpFunction214", None)
        self.__sql_OpFunction214 = value
        
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
    def sql_OpFunction216(self):
        return self.__sql_OpFunction216

    @sql_OpFunction216.setter
    def sql_OpFunction216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_OpFunction__sql_OpFunction216", None)
        self.__sql_OpFunction216 = value
        
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
    def sql_OpFunction156(self):
        return self.__sql_OpFunction156

    @sql_OpFunction156.setter
    def sql_OpFunction156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_OpFunction__sql_OpFunction156", None)
        self.__sql_OpFunction156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_LikeOperand155"):
                opp_val = getattr(old_value, "sql_LikeOperand155", None)
                if opp_val == self:
                    setattr(old_value, "sql_LikeOperand155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_LikeOperand155"):
                opp_val = getattr(value, "sql_LikeOperand155", None)
                setattr(value, "sql_LikeOperand155", self)

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
            if hasattr(old_value, "sql_GroupByColumnFull113"):
                opp_val = getattr(old_value, "sql_GroupByColumnFull113", None)
                if opp_val == self:
                    setattr(old_value, "sql_GroupByColumnFull113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_GroupByColumnFull113"):
                opp_val = getattr(value, "sql_GroupByColumnFull113", None)
                setattr(value, "sql_GroupByColumnFull113", self)

class OrGroupByColumn:

    pass
class sql_GroupByColumnFull(OrGroupByColumn):

    def __init__(self, grByInt: str, sql_GroupByColumnFull: "sql_OrGroupByColumn" = None, sql_GroupByColumnFull110: "sql_ColumnFull" = None, sql_GroupByColumnFull113: "sql_OpFunction" = None):
        self.grByInt = grByInt
        self.sql_GroupByColumnFull = sql_GroupByColumnFull
        self.sql_GroupByColumnFull110 = sql_GroupByColumnFull110
        self.sql_GroupByColumnFull113 = sql_GroupByColumnFull113
        
    @property
    def grByInt(self) -> str:
        return self.__grByInt

    @grByInt.setter
    def grByInt(self, grByInt: str):
        self.__grByInt = grByInt

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
            if hasattr(old_value, "sql_OrGroupByColumn108"):
                opp_val = getattr(old_value, "sql_OrGroupByColumn108", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OrGroupByColumn108"):
                opp_val = getattr(value, "sql_OrGroupByColumn108", None)
                if opp_val is None:
                    setattr(value, "sql_OrGroupByColumn108", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sql_GroupByColumnFull113(self):
        return self.__sql_GroupByColumnFull113

    @sql_GroupByColumnFull113.setter
    def sql_GroupByColumnFull113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_GroupByColumnFull__sql_GroupByColumnFull113", None)
        self.__sql_GroupByColumnFull113 = value
        
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
    def sql_GroupByColumnFull110(self):
        return self.__sql_GroupByColumnFull110

    @sql_GroupByColumnFull110.setter
    def sql_GroupByColumnFull110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_GroupByColumnFull__sql_GroupByColumnFull110", None)
        self.__sql_GroupByColumnFull110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_ColumnFull111"):
                opp_val = getattr(old_value, "sql_ColumnFull111", None)
                if opp_val == self:
                    setattr(old_value, "sql_ColumnFull111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_ColumnFull111"):
                opp_val = getattr(value, "sql_ColumnFull111", None)
                setattr(value, "sql_ColumnFull111", self)

class OrOrderByColumn:

    pass
class sql_OrderByColumnFull(OrOrderByColumn):

    def __init__(self, colOrderInt: str, direction: str, sql_OrderByColumnFull106: "sql_ColumnFull" = None, sql_OrderByColumnFull: "sql_OrOrderByColumn" = None):
        self.colOrderInt = colOrderInt
        self.direction = direction
        self.sql_OrderByColumnFull106 = sql_OrderByColumnFull106
        self.sql_OrderByColumnFull = sql_OrderByColumnFull
        
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
            if hasattr(old_value, "sql_OrOrderByColumn104"):
                opp_val = getattr(old_value, "sql_OrOrderByColumn104", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OrOrderByColumn104"):
                opp_val = getattr(value, "sql_OrOrderByColumn104", None)
                if opp_val is None:
                    setattr(value, "sql_OrOrderByColumn104", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sql_OrderByColumnFull106(self):
        return self.__sql_OrderByColumnFull106

    @sql_OrderByColumnFull106.setter
    def sql_OrderByColumnFull106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_OrderByColumnFull__sql_OrderByColumnFull106", None)
        self.__sql_OrderByColumnFull106 = value
        
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

class sql_PivotInClause:

    def __init__(self, pinany: str, sql_PivotInClause87: "sql_SubQueryOperand" = None, sql_PivotInClause90: "sql_UnpivotInClauseArgs" = None, sql_PivotInClause: "sql_PivotTable" = None):
        self.pinany = pinany
        self.sql_PivotInClause87 = sql_PivotInClause87
        self.sql_PivotInClause90 = sql_PivotInClause90
        self.sql_PivotInClause = sql_PivotInClause
        
    @property
    def pinany(self) -> str:
        return self.__pinany

    @pinany.setter
    def pinany(self, pinany: str):
        self.__pinany = pinany

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
            if hasattr(old_value, "sql_PivotTable85"):
                opp_val = getattr(old_value, "sql_PivotTable85", None)
                if opp_val == self:
                    setattr(old_value, "sql_PivotTable85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_PivotTable85"):
                opp_val = getattr(value, "sql_PivotTable85", None)
                setattr(value, "sql_PivotTable85", self)

    @property
    def sql_PivotInClause90(self):
        return self.__sql_PivotInClause90

    @sql_PivotInClause90.setter
    def sql_PivotInClause90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_PivotInClause__sql_PivotInClause90", None)
        self.__sql_PivotInClause90 = value
        
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
    def sql_PivotInClause87(self):
        return self.__sql_PivotInClause87

    @sql_PivotInClause87.setter
    def sql_PivotInClause87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_PivotInClause__sql_PivotInClause87", None)
        self.__sql_PivotInClause87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_SubQueryOperand88"):
                opp_val = getattr(old_value, "sql_SubQueryOperand88", None)
                if opp_val == self:
                    setattr(old_value, "sql_SubQueryOperand88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_SubQueryOperand88"):
                opp_val = getattr(value, "sql_SubQueryOperand88", None)
                setattr(value, "sql_SubQueryOperand88", self)

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
            if hasattr(old_value, "sql_PivotTable81"):
                opp_val = getattr(old_value, "sql_PivotTable81", None)
                if opp_val == self:
                    setattr(old_value, "sql_PivotTable81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_PivotTable81"):
                opp_val = getattr(value, "sql_PivotTable81", None)
                setattr(value, "sql_PivotTable81", self)

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
            if hasattr(old_value, "sql_RowValues79"):
                opp_val = getattr(old_value, "sql_RowValues79", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_RowValues79"):
                opp_val = getattr(value, "sql_RowValues79", None)
                if opp_val is None:
                    setattr(value, "sql_RowValues79", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sql_RowValues:

    pass
class Rows:

    pass
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
class sql_Row(Rows):

    pass
class sql_Rows:

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

class sql_FromValuesColumnNames:

    pass
class sql_FromValuesColumns:

    pass
class sql_Values:

    pass
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
            if hasattr(old_value, "sql_ColumnOrAlias33"):
                opp_val = getattr(old_value, "sql_ColumnOrAlias33", None)
                if opp_val == self:
                    setattr(old_value, "sql_ColumnOrAlias33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_ColumnOrAlias33"):
                opp_val = getattr(value, "sql_ColumnOrAlias33", None)
                setattr(value, "sql_ColumnOrAlias33", self)

class sql_DbObjectName(TableFull, PivotCol, ColumnFull, UsingCols):

    def __init__(self, dbname: str, sql_DbObjectName: "sql_ColumnOrAlias" = None, sql_DbObjectName52: "sql_UsingCols" = None, sql_DbObjectName65: "sql_TableOrAlias" = None, sql_DbObjectName247: "sql_AnalyticExprArg" = None, sql_DbObjectName280: "sql_pcols" = None, sql_DbObjectName282: "sql_tbls" = None, sql_DbObjectName272: "sql_Col" = None):
        self.dbname = dbname
        self.sql_DbObjectName = sql_DbObjectName
        self.sql_DbObjectName52 = sql_DbObjectName52
        self.sql_DbObjectName65 = sql_DbObjectName65
        self.sql_DbObjectName247 = sql_DbObjectName247
        self.sql_DbObjectName280 = sql_DbObjectName280
        self.sql_DbObjectName282 = sql_DbObjectName282
        self.sql_DbObjectName272 = sql_DbObjectName272
        
    @property
    def dbname(self) -> str:
        return self.__dbname

    @dbname.setter
    def dbname(self, dbname: str):
        self.__dbname = dbname

    @property
    def sql_DbObjectName272(self):
        return self.__sql_DbObjectName272

    @sql_DbObjectName272.setter
    def sql_DbObjectName272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_DbObjectName__sql_DbObjectName272", None)
        self.__sql_DbObjectName272 = value
        
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
    def sql_DbObjectName(self):
        return self.__sql_DbObjectName

    @sql_DbObjectName.setter
    def sql_DbObjectName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_DbObjectName__sql_DbObjectName", None)
        self.__sql_DbObjectName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_ColumnOrAlias31"):
                opp_val = getattr(old_value, "sql_ColumnOrAlias31", None)
                if opp_val == self:
                    setattr(old_value, "sql_ColumnOrAlias31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_ColumnOrAlias31"):
                opp_val = getattr(value, "sql_ColumnOrAlias31", None)
                setattr(value, "sql_ColumnOrAlias31", self)

    @property
    def sql_DbObjectName52(self):
        return self.__sql_DbObjectName52

    @sql_DbObjectName52.setter
    def sql_DbObjectName52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_DbObjectName__sql_DbObjectName52", None)
        self.__sql_DbObjectName52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_UsingCols51"):
                opp_val = getattr(old_value, "sql_UsingCols51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_UsingCols51"):
                opp_val = getattr(value, "sql_UsingCols51", None)
                if opp_val is None:
                    setattr(value, "sql_UsingCols51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sql_DbObjectName247(self):
        return self.__sql_DbObjectName247

    @sql_DbObjectName247.setter
    def sql_DbObjectName247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_DbObjectName__sql_DbObjectName247", None)
        self.__sql_DbObjectName247 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_AnalyticExprArg246"):
                opp_val = getattr(old_value, "sql_AnalyticExprArg246", None)
                if opp_val == self:
                    setattr(old_value, "sql_AnalyticExprArg246", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_AnalyticExprArg246"):
                opp_val = getattr(value, "sql_AnalyticExprArg246", None)
                setattr(value, "sql_AnalyticExprArg246", self)

    @property
    def sql_DbObjectName280(self):
        return self.__sql_DbObjectName280

    @sql_DbObjectName280.setter
    def sql_DbObjectName280(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_DbObjectName__sql_DbObjectName280", None)
        self.__sql_DbObjectName280 = value
        
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
    def sql_DbObjectName65(self):
        return self.__sql_DbObjectName65

    @sql_DbObjectName65.setter
    def sql_DbObjectName65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_DbObjectName__sql_DbObjectName65", None)
        self.__sql_DbObjectName65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_TableOrAlias64"):
                opp_val = getattr(old_value, "sql_TableOrAlias64", None)
                if opp_val == self:
                    setattr(old_value, "sql_TableOrAlias64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_TableOrAlias64"):
                opp_val = getattr(value, "sql_TableOrAlias64", None)
                setattr(value, "sql_TableOrAlias64", self)

    @property
    def sql_DbObjectName282(self):
        return self.__sql_DbObjectName282

    @sql_DbObjectName282.setter
    def sql_DbObjectName282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_DbObjectName__sql_DbObjectName282", None)
        self.__sql_DbObjectName282 = value
        
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

class sql_Operands(OpFunctionArgAgregate):

    pass
class OrColumn:

    pass
class sql_ColumnOrAlias(OrColumn):

    def __init__(self, alias: str, allCols: str, sql_ColumnOrAlias: "sql_OrColumn" = None, sql_ColumnOrAlias29: "sql_Operands" = None, sql_ColumnOrAlias31: "sql_DbObjectName" = None, sql_ColumnOrAlias33: "sql_DbObjectNameAll" = None):
        self.alias = alias
        self.allCols = allCols
        self.sql_ColumnOrAlias = sql_ColumnOrAlias
        self.sql_ColumnOrAlias29 = sql_ColumnOrAlias29
        self.sql_ColumnOrAlias31 = sql_ColumnOrAlias31
        self.sql_ColumnOrAlias33 = sql_ColumnOrAlias33
        
    @property
    def allCols(self) -> str:
        return self.__allCols

    @allCols.setter
    def allCols(self, allCols: str):
        self.__allCols = allCols

    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def sql_ColumnOrAlias31(self):
        return self.__sql_ColumnOrAlias31

    @sql_ColumnOrAlias31.setter
    def sql_ColumnOrAlias31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ColumnOrAlias__sql_ColumnOrAlias31", None)
        self.__sql_ColumnOrAlias31 = value
        
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
    def sql_ColumnOrAlias29(self):
        return self.__sql_ColumnOrAlias29

    @sql_ColumnOrAlias29.setter
    def sql_ColumnOrAlias29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ColumnOrAlias__sql_ColumnOrAlias29", None)
        self.__sql_ColumnOrAlias29 = value
        
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
            if hasattr(old_value, "sql_OrColumn27"):
                opp_val = getattr(old_value, "sql_OrColumn27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OrColumn27"):
                opp_val = getattr(value, "sql_OrColumn27", None)
                if opp_val is None:
                    setattr(value, "sql_OrColumn27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sql_ColumnOrAlias33(self):
        return self.__sql_ColumnOrAlias33

    @sql_ColumnOrAlias33.setter
    def sql_ColumnOrAlias33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ColumnOrAlias__sql_ColumnOrAlias33", None)
        self.__sql_ColumnOrAlias33 = value
        
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

class PivotForClause:

    pass
class sql_ColumnFull(PivotForClause):

    pass
class sql_UsingCols:

    pass
class sql_JoinCondition:

    pass
class sql_FromTableJoin:

    def __init__(self, join: str, sql_FromTableJoin: "sql_FromTable" = None, sql_FromTableJoin41: "sql_TableOrAlias" = None, sql_FromTableJoin44: "sql_OrExpr" = None, sql_FromTableJoin47: "sql_JoinCondition" = None):
        self.join = join
        self.sql_FromTableJoin = sql_FromTableJoin
        self.sql_FromTableJoin41 = sql_FromTableJoin41
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
            if hasattr(old_value, "sql_FromTable39"):
                opp_val = getattr(old_value, "sql_FromTable39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FromTable39"):
                opp_val = getattr(value, "sql_FromTable39", None)
                if opp_val is None:
                    setattr(value, "sql_FromTable39", set([self]))
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
            if hasattr(old_value, "sql_OrExpr45"):
                opp_val = getattr(old_value, "sql_OrExpr45", None)
                if opp_val == self:
                    setattr(old_value, "sql_OrExpr45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OrExpr45"):
                opp_val = getattr(value, "sql_OrExpr45", None)
                setattr(value, "sql_OrExpr45", self)

    @property
    def sql_FromTableJoin41(self):
        return self.__sql_FromTableJoin41

    @sql_FromTableJoin41.setter
    def sql_FromTableJoin41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FromTableJoin__sql_FromTableJoin41", None)
        self.__sql_FromTableJoin41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_TableOrAlias42"):
                opp_val = getattr(old_value, "sql_TableOrAlias42", None)
                if opp_val == self:
                    setattr(old_value, "sql_TableOrAlias42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_TableOrAlias42"):
                opp_val = getattr(value, "sql_TableOrAlias42", None)
                setattr(value, "sql_TableOrAlias42", self)

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

    def __init__(self, alias: str, sql_TableOrAlias: "sql_FromTable" = None, sql_TableOrAlias42: "sql_FromTableJoin" = None, sql_TableOrAlias54: "sql_TableFull" = None, sql_TableOrAlias56: "sql_SubQueryOperand" = None, sql_TableOrAlias58: "sql_FromValues" = None, sql_TableOrAlias60: "sql_PivotTable" = None, sql_TableOrAlias62: "sql_UnpivotTable" = None, sql_TableOrAlias64: "sql_DbObjectName" = None):
        self.alias = alias
        self.sql_TableOrAlias = sql_TableOrAlias
        self.sql_TableOrAlias42 = sql_TableOrAlias42
        self.sql_TableOrAlias54 = sql_TableOrAlias54
        self.sql_TableOrAlias56 = sql_TableOrAlias56
        self.sql_TableOrAlias58 = sql_TableOrAlias58
        self.sql_TableOrAlias60 = sql_TableOrAlias60
        self.sql_TableOrAlias62 = sql_TableOrAlias62
        self.sql_TableOrAlias64 = sql_TableOrAlias64
        
    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

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
    def sql_TableOrAlias62(self):
        return self.__sql_TableOrAlias62

    @sql_TableOrAlias62.setter
    def sql_TableOrAlias62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_TableOrAlias__sql_TableOrAlias62", None)
        self.__sql_TableOrAlias62 = value
        
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
    def sql_TableOrAlias54(self):
        return self.__sql_TableOrAlias54

    @sql_TableOrAlias54.setter
    def sql_TableOrAlias54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_TableOrAlias__sql_TableOrAlias54", None)
        self.__sql_TableOrAlias54 = value
        
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
            if hasattr(old_value, "sql_FromTable37"):
                opp_val = getattr(old_value, "sql_FromTable37", None)
                if opp_val == self:
                    setattr(old_value, "sql_FromTable37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FromTable37"):
                opp_val = getattr(value, "sql_FromTable37", None)
                setattr(value, "sql_FromTable37", self)

    @property
    def sql_TableOrAlias64(self):
        return self.__sql_TableOrAlias64

    @sql_TableOrAlias64.setter
    def sql_TableOrAlias64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_TableOrAlias__sql_TableOrAlias64", None)
        self.__sql_TableOrAlias64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_DbObjectName65"):
                opp_val = getattr(old_value, "sql_DbObjectName65", None)
                if opp_val == self:
                    setattr(old_value, "sql_DbObjectName65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_DbObjectName65"):
                opp_val = getattr(value, "sql_DbObjectName65", None)
                setattr(value, "sql_DbObjectName65", self)

    @property
    def sql_TableOrAlias60(self):
        return self.__sql_TableOrAlias60

    @sql_TableOrAlias60.setter
    def sql_TableOrAlias60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_TableOrAlias__sql_TableOrAlias60", None)
        self.__sql_TableOrAlias60 = value
        
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
    def sql_TableOrAlias56(self):
        return self.__sql_TableOrAlias56

    @sql_TableOrAlias56.setter
    def sql_TableOrAlias56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_TableOrAlias__sql_TableOrAlias56", None)
        self.__sql_TableOrAlias56 = value
        
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
    def sql_TableOrAlias42(self):
        return self.__sql_TableOrAlias42

    @sql_TableOrAlias42.setter
    def sql_TableOrAlias42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_TableOrAlias__sql_TableOrAlias42", None)
        self.__sql_TableOrAlias42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FromTableJoin41"):
                opp_val = getattr(old_value, "sql_FromTableJoin41", None)
                if opp_val == self:
                    setattr(old_value, "sql_FromTableJoin41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FromTableJoin41"):
                opp_val = getattr(value, "sql_FromTableJoin41", None)
                setattr(value, "sql_FromTableJoin41", self)

class OrTable:

    pass
class sql_FromTable(OrTable):

    pass
class sql_OrTable:

    pass
class sql_OrColumn(PivotForClause):

    pass
class SelectQuery:

    pass
class sql_Select(SelectQuery):

    def __init__(self, select: str, sql_Select11: "sql_OrExpr" = None, sql_Select13: "sql_OrGroupByColumn" = None, sql_Select15: "sql_OrExpr" = None, sql_Select18: "sql_OrOrderByColumn" = None, sql_Select20: "sql_Limit" = None, sql_Select22: "sql_Offset" = None, sql_Select: "sql_SelectSubSet" = None, sql_Select4: set["sql_SelectSubSet"] = None, sql_Select7: "sql_OrColumn" = None, sql_Select9: "sql_OrTable" = None, sql_Select24: "sql_FetchFirst" = None):
        self.select = select
        self.sql_Select11 = sql_Select11
        self.sql_Select13 = sql_Select13
        self.sql_Select15 = sql_Select15
        self.sql_Select18 = sql_Select18
        self.sql_Select20 = sql_Select20
        self.sql_Select22 = sql_Select22
        self.sql_Select = sql_Select
        self.sql_Select4 = sql_Select4 if sql_Select4 is not None else set()
        self.sql_Select7 = sql_Select7
        self.sql_Select9 = sql_Select9
        self.sql_Select24 = sql_Select24
        
    @property
    def select(self) -> str:
        return self.__select

    @select.setter
    def select(self, select: str):
        self.__select = select

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
            if hasattr(old_value, "sql_OrExpr16"):
                opp_val = getattr(old_value, "sql_OrExpr16", None)
                if opp_val == self:
                    setattr(old_value, "sql_OrExpr16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OrExpr16"):
                opp_val = getattr(value, "sql_OrExpr16", None)
                setattr(value, "sql_OrExpr16", self)

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
    def sql_Select11(self):
        return self.__sql_Select11

    @sql_Select11.setter
    def sql_Select11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Select__sql_Select11", None)
        self.__sql_Select11 = value
        
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
    def sql_Select18(self):
        return self.__sql_Select18

    @sql_Select18.setter
    def sql_Select18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Select__sql_Select18", None)
        self.__sql_Select18 = value
        
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
    def sql_Select20(self):
        return self.__sql_Select20

    @sql_Select20.setter
    def sql_Select20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Select__sql_Select20", None)
        self.__sql_Select20 = value
        
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
    def sql_Select9(self):
        return self.__sql_Select9

    @sql_Select9.setter
    def sql_Select9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Select__sql_Select9", None)
        self.__sql_Select9 = value
        
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
    def sql_Select24(self):
        return self.__sql_Select24

    @sql_Select24.setter
    def sql_Select24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Select__sql_Select24", None)
        self.__sql_Select24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FetchFirst25"):
                opp_val = getattr(old_value, "sql_FetchFirst25", None)
                if opp_val == self:
                    setattr(old_value, "sql_FetchFirst25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FetchFirst25"):
                opp_val = getattr(value, "sql_FetchFirst25", None)
                setattr(value, "sql_FetchFirst25", self)

    @property
    def sql_Select7(self):
        return self.__sql_Select7

    @sql_Select7.setter
    def sql_Select7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Select__sql_Select7", None)
        self.__sql_Select7 = value
        
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
    def sql_Select4(self):
        return self.__sql_Select4

    @sql_Select4.setter
    def sql_Select4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Select__sql_Select4", None)
        self.__sql_Select4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sql_SelectSubSet5"):
                    opp_val = getattr(item, "sql_SelectSubSet5", None)
                    
                    if opp_val == self:
                        setattr(item, "sql_SelectSubSet5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sql_SelectSubSet5"):
                    opp_val = getattr(item, "sql_SelectSubSet5", None)
                    
                    setattr(item, "sql_SelectSubSet5", self)
                    

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

    def __init__(self, op: str, all: str, sql_SelectSubSet: "sql_Select" = None, sql_SelectSubSet5: "sql_Select" = None):
        self.op = op
        self.all = all
        self.sql_SelectSubSet = sql_SelectSubSet
        self.sql_SelectSubSet5 = sql_SelectSubSet5
        
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
    def sql_SelectSubSet5(self):
        return self.__sql_SelectSubSet5

    @sql_SelectSubSet5.setter
    def sql_SelectSubSet5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_SelectSubSet__sql_SelectSubSet5", None)
        self.__sql_SelectSubSet5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Select4"):
                opp_val = getattr(old_value, "sql_Select4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Select4"):
                opp_val = getattr(value, "sql_Select4", None)
                if opp_val is None:
                    setattr(value, "sql_Select4", set([self]))
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
            if hasattr(old_value, "sql_Select20"):
                opp_val = getattr(old_value, "sql_Select20", None)
                if opp_val == self:
                    setattr(old_value, "sql_Select20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Select20"):
                opp_val = getattr(value, "sql_Select20", None)
                setattr(value, "sql_Select20", self)

class sql_OrOrderByColumn:

    pass
class sql_OrGroupByColumn:

    pass
class sql_OrExpr:

    pass
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
            if hasattr(old_value, "sql_Select22"):
                opp_val = getattr(old_value, "sql_Select22", None)
                if opp_val == self:
                    setattr(old_value, "sql_Select22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Select22"):
                opp_val = getattr(value, "sql_Select22", None)
                setattr(value, "sql_Select22", self)

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

    def __init__(self, row: str, sql_FetchFirst: "sql_UnsignedValue" = None, sql_FetchFirst25: "sql_Select" = None):
        self.row = row
        self.sql_FetchFirst = sql_FetchFirst
        self.sql_FetchFirst25 = sql_FetchFirst25
        
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
            if hasattr(old_value, "sql_UnsignedValue"):
                opp_val = getattr(old_value, "sql_UnsignedValue", None)
                if opp_val == self:
                    setattr(old_value, "sql_UnsignedValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_UnsignedValue"):
                opp_val = getattr(value, "sql_UnsignedValue", None)
                setattr(value, "sql_UnsignedValue", self)

    @property
    def sql_FetchFirst25(self):
        return self.__sql_FetchFirst25

    @sql_FetchFirst25.setter
    def sql_FetchFirst25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FetchFirst__sql_FetchFirst25", None)
        self.__sql_FetchFirst25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Select24"):
                opp_val = getattr(old_value, "sql_Select24", None)
                if opp_val == self:
                    setattr(old_value, "sql_Select24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Select24"):
                opp_val = getattr(value, "sql_Select24", None)
                setattr(value, "sql_Select24", self)

class sql_SelectQuery:

    pass
class sql_Model:

    pass