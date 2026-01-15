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


############################################
# Definition of Classes
############################################

class Operands:

    pass
class sql_Concat(Operands):

    pass
class sql_Minus(Operands):

    pass
class sql_Star(Operands):

    pass
class sql_Div(Operands):

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
class sql_OpFunctionArgAgregate:

    pass
class OpFunctionArg:

    pass
class sql_OpFList(OpFunctionArg):

    pass
class sql_OpFunctionArgOperand(OpFunctionArg):

    pass
class sql_OpFunctionArg:

    pass
class sql_ScalarOperand(OperandList):

    def __init__(self, soint: int, sostr: str, sodbl: str, sodate: date, sotime: date, sodt: date, sql_ScalarOperand: "sql_Operand" = None, sql_ScalarOperand167: "sql_OpList" = None):
        self.soint = soint
        self.sostr = sostr
        self.sodbl = sodbl
        self.sodate = sodate
        self.sotime = sotime
        self.sodt = sodt
        self.sql_ScalarOperand = sql_ScalarOperand
        self.sql_ScalarOperand167 = sql_ScalarOperand167
        
    @property
    def sodbl(self) -> str:
        return self.__sodbl

    @sodbl.setter
    def sodbl(self, sodbl: str):
        self.__sodbl = sodbl

    @property
    def sotime(self) -> date:
        return self.__sotime

    @sotime.setter
    def sotime(self, sotime: date):
        self.__sotime = sotime

    @property
    def sostr(self) -> str:
        return self.__sostr

    @sostr.setter
    def sostr(self, sostr: str):
        self.__sostr = sostr

    @property
    def soint(self) -> int:
        return self.__soint

    @soint.setter
    def soint(self, soint: int):
        self.__soint = soint

    @property
    def sodate(self) -> date:
        return self.__sodate

    @sodate.setter
    def sodate(self, sodate: date):
        self.__sodate = sodate

    @property
    def sodt(self) -> date:
        return self.__sodt

    @sodt.setter
    def sodt(self, sodt: date):
        self.__sodt = sodt

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
            if hasattr(old_value, "sql_Operand136"):
                opp_val = getattr(old_value, "sql_Operand136", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operand136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operand136"):
                opp_val = getattr(value, "sql_Operand136", None)
                setattr(value, "sql_Operand136", self)

    @property
    def sql_ScalarOperand167(self):
        return self.__sql_ScalarOperand167

    @sql_ScalarOperand167.setter
    def sql_ScalarOperand167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ScalarOperand__sql_ScalarOperand167", None)
        self.__sql_ScalarOperand167 = value
        
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
            if hasattr(old_value, "sql_Operand134"):
                opp_val = getattr(old_value, "sql_Operand134", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operand134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operand134"):
                opp_val = getattr(value, "sql_Operand134", None)
                setattr(value, "sql_Operand134", self)

class sql_SQLCaseOperand:

    pass
class sql_ColumnOperand:

    pass
class sql_Operand:

    pass
class OpFunctionArgAgregate:

    pass
class sql_POperand:

    def __init__(self, prm: str, sql_POperand: "sql_Operand" = None):
        self.prm = prm
        self.sql_POperand = sql_POperand
        
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
            if hasattr(old_value, "sql_Operand132"):
                opp_val = getattr(old_value, "sql_Operand132", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operand132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operand132"):
                opp_val = getattr(value, "sql_Operand132", None)
                setattr(value, "sql_Operand132", self)

class sql_OperandList:

    pass
class sql_OpFunctionCast:

    def __init__(self, type: str, p: int, p2: int, sql_OpFunctionCast: "sql_LikeOperand" = None, sql_OpFunctionCast125: "sql_Operand" = None, sql_OpFunctionCast141: "sql_Operands" = None):
        self.type = type
        self.p = p
        self.p2 = p2
        self.sql_OpFunctionCast = sql_OpFunctionCast
        self.sql_OpFunctionCast125 = sql_OpFunctionCast125
        self.sql_OpFunctionCast141 = sql_OpFunctionCast141
        
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
    def sql_OpFunctionCast125(self):
        return self.__sql_OpFunctionCast125

    @sql_OpFunctionCast125.setter
    def sql_OpFunctionCast125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_OpFunctionCast__sql_OpFunctionCast125", None)
        self.__sql_OpFunctionCast125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operand124"):
                opp_val = getattr(old_value, "sql_Operand124", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operand124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operand124"):
                opp_val = getattr(value, "sql_Operand124", None)
                setattr(value, "sql_Operand124", self)

    @property
    def sql_OpFunctionCast141(self):
        return self.__sql_OpFunctionCast141

    @sql_OpFunctionCast141.setter
    def sql_OpFunctionCast141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_OpFunctionCast__sql_OpFunctionCast141", None)
        self.__sql_OpFunctionCast141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operands142"):
                opp_val = getattr(old_value, "sql_Operands142", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operands142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operands142"):
                opp_val = getattr(value, "sql_Operands142", None)
                setattr(value, "sql_Operands142", self)

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
            if hasattr(old_value, "sql_LikeOperand95"):
                opp_val = getattr(old_value, "sql_LikeOperand95", None)
                if opp_val == self:
                    setattr(old_value, "sql_LikeOperand95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_LikeOperand95"):
                opp_val = getattr(value, "sql_LikeOperand95", None)
                setattr(value, "sql_LikeOperand95", self)

class sql_OpFunction:

    def __init__(self, fname: str, sql_OpFunction: "sql_LikeOperand" = None, sql_OpFunction128: "sql_Operand" = None, sql_OpFunction138: "sql_OpFunctionArg" = None):
        self.fname = fname
        self.sql_OpFunction = sql_OpFunction
        self.sql_OpFunction128 = sql_OpFunction128
        self.sql_OpFunction138 = sql_OpFunction138
        
    @property
    def fname(self) -> str:
        return self.__fname

    @fname.setter
    def fname(self, fname: str):
        self.__fname = fname

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
            if hasattr(old_value, "sql_LikeOperand93"):
                opp_val = getattr(old_value, "sql_LikeOperand93", None)
                if opp_val == self:
                    setattr(old_value, "sql_LikeOperand93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_LikeOperand93"):
                opp_val = getattr(value, "sql_LikeOperand93", None)
                setattr(value, "sql_LikeOperand93", self)

    @property
    def sql_OpFunction138(self):
        return self.__sql_OpFunction138

    @sql_OpFunction138.setter
    def sql_OpFunction138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_OpFunction__sql_OpFunction138", None)
        self.__sql_OpFunction138 = value
        
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
    def sql_OpFunction128(self):
        return self.__sql_OpFunction128

    @sql_OpFunction128.setter
    def sql_OpFunction128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_OpFunction__sql_OpFunction128", None)
        self.__sql_OpFunction128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operand127"):
                opp_val = getattr(old_value, "sql_Operand127", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operand127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operand127"):
                opp_val = getattr(value, "sql_Operand127", None)
                setattr(value, "sql_Operand127", self)

class sql_LikeOperand:

    def __init__(self, op2: str, sql_LikeOperand: "sql_Like" = None, sql_LikeOperand93: "sql_OpFunction" = None, sql_LikeOperand95: "sql_OpFunctionCast" = None):
        self.op2 = op2
        self.sql_LikeOperand = sql_LikeOperand
        self.sql_LikeOperand93 = sql_LikeOperand93
        self.sql_LikeOperand95 = sql_LikeOperand95
        
    @property
    def op2(self) -> str:
        return self.__op2

    @op2.setter
    def op2(self, op2: str):
        self.__op2 = op2

    @property
    def sql_LikeOperand95(self):
        return self.__sql_LikeOperand95

    @sql_LikeOperand95.setter
    def sql_LikeOperand95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_LikeOperand__sql_LikeOperand95", None)
        self.__sql_LikeOperand95 = value
        
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
            if hasattr(old_value, "sql_Like91"):
                opp_val = getattr(old_value, "sql_Like91", None)
                if opp_val == self:
                    setattr(old_value, "sql_Like91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Like91"):
                opp_val = getattr(value, "sql_Like91", None)
                setattr(value, "sql_Like91", self)

    @property
    def sql_LikeOperand93(self):
        return self.__sql_LikeOperand93

    @sql_LikeOperand93.setter
    def sql_LikeOperand93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_LikeOperand__sql_LikeOperand93", None)
        self.__sql_LikeOperand93 = value
        
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
            if hasattr(old_value, "sql_Prms86"):
                opp_val = getattr(old_value, "sql_Prms86", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Prms86"):
                opp_val = getattr(value, "sql_Prms86", None)
                if opp_val is None:
                    setattr(value, "sql_Prms86", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sql_Prms:

    pass
class sql_Comparison:

    def __init__(self, operator: str, subOperator: str, sql_Comparison: "sql_FullExpression" = None, sql_Comparison88: "sql_Operands" = None):
        self.operator = operator
        self.subOperator = subOperator
        self.sql_Comparison = sql_Comparison
        self.sql_Comparison88 = sql_Comparison88
        
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
            if hasattr(old_value, "sql_FullExpression76"):
                opp_val = getattr(old_value, "sql_FullExpression76", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression76"):
                opp_val = getattr(value, "sql_FullExpression76", None)
                setattr(value, "sql_FullExpression76", self)

    @property
    def sql_Comparison88(self):
        return self.__sql_Comparison88

    @sql_Comparison88.setter
    def sql_Comparison88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Comparison__sql_Comparison88", None)
        self.__sql_Comparison88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operands89"):
                opp_val = getattr(old_value, "sql_Operands89", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operands89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operands89"):
                opp_val = getattr(value, "sql_Operands89", None)
                setattr(value, "sql_Operands89", self)

class sql_Like:

    def __init__(self, opLike: str, sql_Like: "sql_FullExpression" = None, sql_Like91: "sql_LikeOperand" = None):
        self.opLike = opLike
        self.sql_Like = sql_Like
        self.sql_Like91 = sql_Like91
        
    @property
    def opLike(self) -> str:
        return self.__opLike

    @opLike.setter
    def opLike(self, opLike: str):
        self.__opLike = opLike

    @property
    def sql_Like91(self):
        return self.__sql_Like91

    @sql_Like91.setter
    def sql_Like91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Like__sql_Like91", None)
        self.__sql_Like91 = value
        
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
            if hasattr(old_value, "sql_FullExpression74"):
                opp_val = getattr(old_value, "sql_FullExpression74", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression74"):
                opp_val = getattr(value, "sql_FullExpression74", None)
                setattr(value, "sql_FullExpression74", self)

class sql_Between:

    def __init__(self, opBetween: str, sql_Between: "sql_FullExpression" = None, sql_Between97: "sql_Operands" = None, sql_Between100: "sql_Operands" = None):
        self.opBetween = opBetween
        self.sql_Between = sql_Between
        self.sql_Between97 = sql_Between97
        self.sql_Between100 = sql_Between100
        
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
            if hasattr(old_value, "sql_FullExpression72"):
                opp_val = getattr(old_value, "sql_FullExpression72", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression72"):
                opp_val = getattr(value, "sql_FullExpression72", None)
                setattr(value, "sql_FullExpression72", self)

    @property
    def sql_Between97(self):
        return self.__sql_Between97

    @sql_Between97.setter
    def sql_Between97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Between__sql_Between97", None)
        self.__sql_Between97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operands98"):
                opp_val = getattr(old_value, "sql_Operands98", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operands98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operands98"):
                opp_val = getattr(value, "sql_Operands98", None)
                setattr(value, "sql_Operands98", self)

    @property
    def sql_Between100(self):
        return self.__sql_Between100

    @sql_Between100.setter
    def sql_Between100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Between__sql_Between100", None)
        self.__sql_Between100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operands101"):
                opp_val = getattr(old_value, "sql_Operands101", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operands101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operands101"):
                opp_val = getattr(value, "sql_Operands101", None)
                setattr(value, "sql_Operands101", self)

class sql_InOper:

    def __init__(self, op: str, sql_InOper: "sql_FullExpression" = None, sql_InOper103: "sql_SubQueryOperand" = None, sql_InOper106: "sql_OperandList" = None):
        self.op = op
        self.sql_InOper = sql_InOper
        self.sql_InOper103 = sql_InOper103
        self.sql_InOper106 = sql_InOper106
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def sql_InOper103(self):
        return self.__sql_InOper103

    @sql_InOper103.setter
    def sql_InOper103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_InOper__sql_InOper103", None)
        self.__sql_InOper103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_SubQueryOperand104"):
                opp_val = getattr(old_value, "sql_SubQueryOperand104", None)
                if opp_val == self:
                    setattr(old_value, "sql_SubQueryOperand104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_SubQueryOperand104"):
                opp_val = getattr(value, "sql_SubQueryOperand104", None)
                setattr(value, "sql_SubQueryOperand104", self)

    @property
    def sql_InOper106(self):
        return self.__sql_InOper106

    @sql_InOper106.setter
    def sql_InOper106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_InOper__sql_InOper106", None)
        self.__sql_InOper106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_OperandList"):
                opp_val = getattr(old_value, "sql_OperandList", None)
                if opp_val == self:
                    setattr(old_value, "sql_OperandList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OperandList"):
                opp_val = getattr(value, "sql_OperandList", None)
                setattr(value, "sql_OperandList", self)

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
            if hasattr(old_value, "sql_FullExpression70"):
                opp_val = getattr(old_value, "sql_FullExpression70", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression70"):
                opp_val = getattr(value, "sql_FullExpression70", None)
                setattr(value, "sql_FullExpression70", self)

class sql_XExpr:

    def __init__(self, xf: str, sql_XExpr: "sql_FullExpression" = None, sql_XExpr81: "sql_Operands" = None, sql_XExpr84: "sql_Prms" = None):
        self.xf = xf
        self.sql_XExpr = sql_XExpr
        self.sql_XExpr81 = sql_XExpr81
        self.sql_XExpr84 = sql_XExpr84
        
    @property
    def xf(self) -> str:
        return self.__xf

    @xf.setter
    def xf(self, xf: str):
        self.__xf = xf

    @property
    def sql_XExpr81(self):
        return self.__sql_XExpr81

    @sql_XExpr81.setter
    def sql_XExpr81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_XExpr__sql_XExpr81", None)
        self.__sql_XExpr81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operands82"):
                opp_val = getattr(old_value, "sql_Operands82", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operands82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operands82"):
                opp_val = getattr(value, "sql_Operands82", None)
                setattr(value, "sql_Operands82", self)

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
            if hasattr(old_value, "sql_FullExpression65"):
                opp_val = getattr(old_value, "sql_FullExpression65", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression65"):
                opp_val = getattr(value, "sql_FullExpression65", None)
                setattr(value, "sql_FullExpression65", self)

    @property
    def sql_XExpr84(self):
        return self.__sql_XExpr84

    @sql_XExpr84.setter
    def sql_XExpr84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_XExpr__sql_XExpr84", None)
        self.__sql_XExpr84 = value
        
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

class sql_ExprGroup:

    pass
class OrExpr:

    pass
class sql_FullExpression(OrExpr):

    def __init__(self, c: str, notPrm: str, isnull: str, sql_FullExpression: "sql_OrExpr" = None, sql_FullExpression58: "sql_FullExpression" = None, sql_FullExpression56: "sql_FullExpression" = None, sql_FullExpression60: "sql_ExprGroup" = None, sql_FullExpression65: "sql_XExpr" = None, sql_FullExpression67: "sql_Operands" = None, sql_FullExpression70: "sql_InOper" = None, sql_FullExpression72: "sql_Between" = None, sql_FullExpression74: "sql_Like" = None, sql_FullExpression76: "sql_Comparison" = None, sql_FullExpression63: "sql_FullExpression" = None, sql_FullExpression61: "sql_FullExpression" = None):
        self.c = c
        self.notPrm = notPrm
        self.isnull = isnull
        self.sql_FullExpression = sql_FullExpression
        self.sql_FullExpression58 = sql_FullExpression58
        self.sql_FullExpression56 = sql_FullExpression56
        self.sql_FullExpression60 = sql_FullExpression60
        self.sql_FullExpression65 = sql_FullExpression65
        self.sql_FullExpression67 = sql_FullExpression67
        self.sql_FullExpression70 = sql_FullExpression70
        self.sql_FullExpression72 = sql_FullExpression72
        self.sql_FullExpression74 = sql_FullExpression74
        self.sql_FullExpression76 = sql_FullExpression76
        self.sql_FullExpression63 = sql_FullExpression63
        self.sql_FullExpression61 = sql_FullExpression61
        
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
    def isnull(self) -> str:
        return self.__isnull

    @isnull.setter
    def isnull(self, isnull: str):
        self.__isnull = isnull

    @property
    def sql_FullExpression70(self):
        return self.__sql_FullExpression70

    @sql_FullExpression70.setter
    def sql_FullExpression70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression70", None)
        self.__sql_FullExpression70 = value
        
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
    def sql_FullExpression74(self):
        return self.__sql_FullExpression74

    @sql_FullExpression74.setter
    def sql_FullExpression74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression74", None)
        self.__sql_FullExpression74 = value
        
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
    def sql_FullExpression76(self):
        return self.__sql_FullExpression76

    @sql_FullExpression76.setter
    def sql_FullExpression76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression76", None)
        self.__sql_FullExpression76 = value
        
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
    def sql_FullExpression63(self):
        return self.__sql_FullExpression63

    @sql_FullExpression63.setter
    def sql_FullExpression63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression63", None)
        self.__sql_FullExpression63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FullExpression61"):
                opp_val = getattr(old_value, "sql_FullExpression61", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression61"):
                opp_val = getattr(value, "sql_FullExpression61", None)
                setattr(value, "sql_FullExpression61", self)

    @property
    def sql_FullExpression65(self):
        return self.__sql_FullExpression65

    @sql_FullExpression65.setter
    def sql_FullExpression65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression65", None)
        self.__sql_FullExpression65 = value
        
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
    def sql_FullExpression72(self):
        return self.__sql_FullExpression72

    @sql_FullExpression72.setter
    def sql_FullExpression72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression72", None)
        self.__sql_FullExpression72 = value
        
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
    def sql_FullExpression(self):
        return self.__sql_FullExpression

    @sql_FullExpression.setter
    def sql_FullExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression", None)
        self.__sql_FullExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_OrExpr55"):
                opp_val = getattr(old_value, "sql_OrExpr55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OrExpr55"):
                opp_val = getattr(value, "sql_OrExpr55", None)
                if opp_val is None:
                    setattr(value, "sql_OrExpr55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sql_FullExpression67(self):
        return self.__sql_FullExpression67

    @sql_FullExpression67.setter
    def sql_FullExpression67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression67", None)
        self.__sql_FullExpression67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Operands68"):
                opp_val = getattr(old_value, "sql_Operands68", None)
                if opp_val == self:
                    setattr(old_value, "sql_Operands68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Operands68"):
                opp_val = getattr(value, "sql_Operands68", None)
                setattr(value, "sql_Operands68", self)

    @property
    def sql_FullExpression56(self):
        return self.__sql_FullExpression56

    @sql_FullExpression56.setter
    def sql_FullExpression56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression56", None)
        self.__sql_FullExpression56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FullExpression58"):
                opp_val = getattr(old_value, "sql_FullExpression58", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression58"):
                opp_val = getattr(value, "sql_FullExpression58", None)
                setattr(value, "sql_FullExpression58", self)

    @property
    def sql_FullExpression58(self):
        return self.__sql_FullExpression58

    @sql_FullExpression58.setter
    def sql_FullExpression58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression58", None)
        self.__sql_FullExpression58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FullExpression56"):
                opp_val = getattr(old_value, "sql_FullExpression56", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression56"):
                opp_val = getattr(value, "sql_FullExpression56", None)
                setattr(value, "sql_FullExpression56", self)

    @property
    def sql_FullExpression60(self):
        return self.__sql_FullExpression60

    @sql_FullExpression60.setter
    def sql_FullExpression60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression60", None)
        self.__sql_FullExpression60 = value
        
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
    def sql_FullExpression61(self):
        return self.__sql_FullExpression61

    @sql_FullExpression61.setter
    def sql_FullExpression61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FullExpression__sql_FullExpression61", None)
        self.__sql_FullExpression61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FullExpression63"):
                opp_val = getattr(old_value, "sql_FullExpression63", None)
                if opp_val == self:
                    setattr(old_value, "sql_FullExpression63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FullExpression63"):
                opp_val = getattr(value, "sql_FullExpression63", None)
                setattr(value, "sql_FullExpression63", self)

class OrGroupByColumn:

    pass
class sql_GroupByColumnFull(OrGroupByColumn):

    pass
class OrOrderByColumn:

    pass
class sql_OrderByColumnFull(OrOrderByColumn):

    def __init__(self, colOrderInt: int, direction: str, sql_OrderByColumnFull: "sql_OrOrderByColumn" = None, sql_OrderByColumnFull48: "sql_ColumnFull" = None):
        self.colOrderInt = colOrderInt
        self.direction = direction
        self.sql_OrderByColumnFull = sql_OrderByColumnFull
        self.sql_OrderByColumnFull48 = sql_OrderByColumnFull48
        
    @property
    def colOrderInt(self) -> int:
        return self.__colOrderInt

    @colOrderInt.setter
    def colOrderInt(self, colOrderInt: int):
        self.__colOrderInt = colOrderInt

    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def sql_OrderByColumnFull48(self):
        return self.__sql_OrderByColumnFull48

    @sql_OrderByColumnFull48.setter
    def sql_OrderByColumnFull48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_OrderByColumnFull__sql_OrderByColumnFull48", None)
        self.__sql_OrderByColumnFull48 = value
        
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
            if hasattr(old_value, "sql_OrOrderByColumn46"):
                opp_val = getattr(old_value, "sql_OrOrderByColumn46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OrOrderByColumn46"):
                opp_val = getattr(value, "sql_OrOrderByColumn46", None)
                if opp_val is None:
                    setattr(value, "sql_OrOrderByColumn46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TableFull:

    pass
class sql_tbls(TableFull):

    pass
class ColumnFull:

    pass
class sql_Col(ColumnFull):

    pass
class sql_SubQueryOperand:

    pass
class sql_ColumnFull:

    pass
class sql_TableFull:

    pass
class sql_FromTableJoin:

    def __init__(self, join: str, sql_FromTableJoin: "sql_FromTable" = None, sql_FromTableJoin33: "sql_TableOrAlias" = None, sql_FromTableJoin36: "sql_OrExpr" = None):
        self.join = join
        self.sql_FromTableJoin = sql_FromTableJoin
        self.sql_FromTableJoin33 = sql_FromTableJoin33
        self.sql_FromTableJoin36 = sql_FromTableJoin36
        
    @property
    def join(self) -> str:
        return self.__join

    @join.setter
    def join(self, join: str):
        self.__join = join

    @property
    def sql_FromTableJoin36(self):
        return self.__sql_FromTableJoin36

    @sql_FromTableJoin36.setter
    def sql_FromTableJoin36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FromTableJoin__sql_FromTableJoin36", None)
        self.__sql_FromTableJoin36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_OrExpr37"):
                opp_val = getattr(old_value, "sql_OrExpr37", None)
                if opp_val == self:
                    setattr(old_value, "sql_OrExpr37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OrExpr37"):
                opp_val = getattr(value, "sql_OrExpr37", None)
                setattr(value, "sql_OrExpr37", self)

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
            if hasattr(old_value, "sql_FromTable31"):
                opp_val = getattr(old_value, "sql_FromTable31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FromTable31"):
                opp_val = getattr(value, "sql_FromTable31", None)
                if opp_val is None:
                    setattr(value, "sql_FromTable31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sql_FromTableJoin33(self):
        return self.__sql_FromTableJoin33

    @sql_FromTableJoin33.setter
    def sql_FromTableJoin33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_FromTableJoin__sql_FromTableJoin33", None)
        self.__sql_FromTableJoin33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_TableOrAlias34"):
                opp_val = getattr(old_value, "sql_TableOrAlias34", None)
                if opp_val == self:
                    setattr(old_value, "sql_TableOrAlias34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_TableOrAlias34"):
                opp_val = getattr(value, "sql_TableOrAlias34", None)
                setattr(value, "sql_TableOrAlias34", self)

class sql_TableOrAlias:

    def __init__(self, alias: str, sql_TableOrAlias: "sql_FromTable" = None, sql_TableOrAlias34: "sql_FromTableJoin" = None, sql_TableOrAlias39: "sql_TableFull" = None, sql_TableOrAlias41: "sql_SubQueryOperand" = None, sql_TableOrAlias43: "sql_DbObjectName" = None):
        self.alias = alias
        self.sql_TableOrAlias = sql_TableOrAlias
        self.sql_TableOrAlias34 = sql_TableOrAlias34
        self.sql_TableOrAlias39 = sql_TableOrAlias39
        self.sql_TableOrAlias41 = sql_TableOrAlias41
        self.sql_TableOrAlias43 = sql_TableOrAlias43
        
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
            if hasattr(old_value, "sql_FromTable29"):
                opp_val = getattr(old_value, "sql_FromTable29", None)
                if opp_val == self:
                    setattr(old_value, "sql_FromTable29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FromTable29"):
                opp_val = getattr(value, "sql_FromTable29", None)
                setattr(value, "sql_FromTable29", self)

    @property
    def sql_TableOrAlias39(self):
        return self.__sql_TableOrAlias39

    @sql_TableOrAlias39.setter
    def sql_TableOrAlias39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_TableOrAlias__sql_TableOrAlias39", None)
        self.__sql_TableOrAlias39 = value
        
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
    def sql_TableOrAlias34(self):
        return self.__sql_TableOrAlias34

    @sql_TableOrAlias34.setter
    def sql_TableOrAlias34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_TableOrAlias__sql_TableOrAlias34", None)
        self.__sql_TableOrAlias34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_FromTableJoin33"):
                opp_val = getattr(old_value, "sql_FromTableJoin33", None)
                if opp_val == self:
                    setattr(old_value, "sql_FromTableJoin33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_FromTableJoin33"):
                opp_val = getattr(value, "sql_FromTableJoin33", None)
                setattr(value, "sql_FromTableJoin33", self)

    @property
    def sql_TableOrAlias41(self):
        return self.__sql_TableOrAlias41

    @sql_TableOrAlias41.setter
    def sql_TableOrAlias41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_TableOrAlias__sql_TableOrAlias41", None)
        self.__sql_TableOrAlias41 = value
        
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
    def sql_TableOrAlias43(self):
        return self.__sql_TableOrAlias43

    @sql_TableOrAlias43.setter
    def sql_TableOrAlias43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_TableOrAlias__sql_TableOrAlias43", None)
        self.__sql_TableOrAlias43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_DbObjectName44"):
                opp_val = getattr(old_value, "sql_DbObjectName44", None)
                if opp_val == self:
                    setattr(old_value, "sql_DbObjectName44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_DbObjectName44"):
                opp_val = getattr(value, "sql_DbObjectName44", None)
                setattr(value, "sql_DbObjectName44", self)

class OrTable:

    pass
class sql_FromTable(OrTable):

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
            if hasattr(old_value, "sql_ColumnOrAlias25"):
                opp_val = getattr(old_value, "sql_ColumnOrAlias25", None)
                if opp_val == self:
                    setattr(old_value, "sql_ColumnOrAlias25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_ColumnOrAlias25"):
                opp_val = getattr(value, "sql_ColumnOrAlias25", None)
                setattr(value, "sql_ColumnOrAlias25", self)

class sql_DbObjectName(ColumnFull, TableFull):

    def __init__(self, dbname: str, sql_DbObjectName: "sql_ColumnOrAlias" = None, sql_DbObjectName44: "sql_TableOrAlias" = None, sql_DbObjectName163: "sql_Col" = None, sql_DbObjectName165: "sql_tbls" = None):
        self.dbname = dbname
        self.sql_DbObjectName = sql_DbObjectName
        self.sql_DbObjectName44 = sql_DbObjectName44
        self.sql_DbObjectName163 = sql_DbObjectName163
        self.sql_DbObjectName165 = sql_DbObjectName165
        
    @property
    def dbname(self) -> str:
        return self.__dbname

    @dbname.setter
    def dbname(self, dbname: str):
        self.__dbname = dbname

    @property
    def sql_DbObjectName44(self):
        return self.__sql_DbObjectName44

    @sql_DbObjectName44.setter
    def sql_DbObjectName44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_DbObjectName__sql_DbObjectName44", None)
        self.__sql_DbObjectName44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_TableOrAlias43"):
                opp_val = getattr(old_value, "sql_TableOrAlias43", None)
                if opp_val == self:
                    setattr(old_value, "sql_TableOrAlias43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_TableOrAlias43"):
                opp_val = getattr(value, "sql_TableOrAlias43", None)
                setattr(value, "sql_TableOrAlias43", self)

    @property
    def sql_DbObjectName165(self):
        return self.__sql_DbObjectName165

    @sql_DbObjectName165.setter
    def sql_DbObjectName165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_DbObjectName__sql_DbObjectName165", None)
        self.__sql_DbObjectName165 = value
        
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
    def sql_DbObjectName163(self):
        return self.__sql_DbObjectName163

    @sql_DbObjectName163.setter
    def sql_DbObjectName163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_DbObjectName__sql_DbObjectName163", None)
        self.__sql_DbObjectName163 = value
        
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
            if hasattr(old_value, "sql_ColumnOrAlias23"):
                opp_val = getattr(old_value, "sql_ColumnOrAlias23", None)
                if opp_val == self:
                    setattr(old_value, "sql_ColumnOrAlias23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_ColumnOrAlias23"):
                opp_val = getattr(value, "sql_ColumnOrAlias23", None)
                setattr(value, "sql_ColumnOrAlias23", self)

class sql_Operands(OpFunctionArgAgregate):

    pass
class OrColumn:

    pass
class sql_ColumnOrAlias(OrColumn):

    def __init__(self, alias: str, allCols: str, sql_ColumnOrAlias: "sql_OrColumn" = None, sql_ColumnOrAlias21: "sql_Operands" = None, sql_ColumnOrAlias23: "sql_DbObjectName" = None, sql_ColumnOrAlias25: "sql_DbObjectNameAll" = None):
        self.alias = alias
        self.allCols = allCols
        self.sql_ColumnOrAlias = sql_ColumnOrAlias
        self.sql_ColumnOrAlias21 = sql_ColumnOrAlias21
        self.sql_ColumnOrAlias23 = sql_ColumnOrAlias23
        self.sql_ColumnOrAlias25 = sql_ColumnOrAlias25
        
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
    def sql_ColumnOrAlias21(self):
        return self.__sql_ColumnOrAlias21

    @sql_ColumnOrAlias21.setter
    def sql_ColumnOrAlias21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ColumnOrAlias__sql_ColumnOrAlias21", None)
        self.__sql_ColumnOrAlias21 = value
        
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
    def sql_ColumnOrAlias25(self):
        return self.__sql_ColumnOrAlias25

    @sql_ColumnOrAlias25.setter
    def sql_ColumnOrAlias25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ColumnOrAlias__sql_ColumnOrAlias25", None)
        self.__sql_ColumnOrAlias25 = value
        
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
    def sql_ColumnOrAlias23(self):
        return self.__sql_ColumnOrAlias23

    @sql_ColumnOrAlias23.setter
    def sql_ColumnOrAlias23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ColumnOrAlias__sql_ColumnOrAlias23", None)
        self.__sql_ColumnOrAlias23 = value
        
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
    def sql_ColumnOrAlias(self):
        return self.__sql_ColumnOrAlias

    @sql_ColumnOrAlias.setter
    def sql_ColumnOrAlias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_ColumnOrAlias__sql_ColumnOrAlias", None)
        self.__sql_ColumnOrAlias = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_OrColumn19"):
                opp_val = getattr(old_value, "sql_OrColumn19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OrColumn19"):
                opp_val = getattr(value, "sql_OrColumn19", None)
                if opp_val is None:
                    setattr(value, "sql_OrColumn19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sql_SelectSubSet:

    def __init__(self, op: str, all: str, sql_SelectSubSet: "sql_Select" = None, sql_SelectSubSet6: "sql_Select" = None):
        self.op = op
        self.all = all
        self.sql_SelectSubSet = sql_SelectSubSet
        self.sql_SelectSubSet6 = sql_SelectSubSet6
        
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
    def sql_SelectSubSet6(self):
        return self.__sql_SelectSubSet6

    @sql_SelectSubSet6.setter
    def sql_SelectSubSet6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_SelectSubSet__sql_SelectSubSet6", None)
        self.__sql_SelectSubSet6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Select5"):
                opp_val = getattr(old_value, "sql_Select5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Select5"):
                opp_val = getattr(value, "sql_Select5", None)
                if opp_val is None:
                    setattr(value, "sql_Select5", set([self]))
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

class sql_OrGroupByColumn:

    pass
class sql_OrExpr:

    pass
class sql_OrTable:

    pass
class sql_OrColumn:

    pass
class SelectQuery:

    pass
class sql_Select(SelectQuery):

    def __init__(self, select: str, sql_Select: "sql_SelectSubSet" = None, sql_Select5: set["sql_SelectSubSet"] = None, sql_Select8: "sql_OrColumn" = None, sql_Select10: "sql_OrTable" = None, sql_Select12: "sql_OrExpr" = None, sql_Select14: "sql_OrGroupByColumn" = None, sql_Select16: "sql_OrExpr" = None):
        self.select = select
        self.sql_Select = sql_Select
        self.sql_Select5 = sql_Select5 if sql_Select5 is not None else set()
        self.sql_Select8 = sql_Select8
        self.sql_Select10 = sql_Select10
        self.sql_Select12 = sql_Select12
        self.sql_Select14 = sql_Select14
        self.sql_Select16 = sql_Select16
        
    @property
    def select(self) -> str:
        return self.__select

    @select.setter
    def select(self, select: str):
        self.__select = select

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
            if hasattr(old_value, "sql_OrExpr17"):
                opp_val = getattr(old_value, "sql_OrExpr17", None)
                if opp_val == self:
                    setattr(old_value, "sql_OrExpr17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_OrExpr17"):
                opp_val = getattr(value, "sql_OrExpr17", None)
                setattr(value, "sql_OrExpr17", self)

    @property
    def sql_Select10(self):
        return self.__sql_Select10

    @sql_Select10.setter
    def sql_Select10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Select__sql_Select10", None)
        self.__sql_Select10 = value
        
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
    def sql_Select14(self):
        return self.__sql_Select14

    @sql_Select14.setter
    def sql_Select14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Select__sql_Select14", None)
        self.__sql_Select14 = value
        
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
    def sql_Select8(self):
        return self.__sql_Select8

    @sql_Select8.setter
    def sql_Select8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Select__sql_Select8", None)
        self.__sql_Select8 = value
        
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
    def sql_Select5(self):
        return self.__sql_Select5

    @sql_Select5.setter
    def sql_Select5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Select__sql_Select5", None)
        self.__sql_Select5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sql_SelectSubSet6"):
                    opp_val = getattr(item, "sql_SelectSubSet6", None)
                    
                    if opp_val == self:
                        setattr(item, "sql_SelectSubSet6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sql_SelectSubSet6"):
                    opp_val = getattr(item, "sql_SelectSubSet6", None)
                    
                    setattr(item, "sql_SelectSubSet6", self)
                    

    @property
    def sql_Select12(self):
        return self.__sql_Select12

    @sql_Select12.setter
    def sql_Select12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Select__sql_Select12", None)
        self.__sql_Select12 = value
        
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

class sql_OrOrderByColumn:

    pass
class sql_SelectQuery:

    pass
class sql_Model:

    pass