from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class AccessLevel(Enum):
    PUBLIC = "PUBLIC"
    PROTECTED = "PROTECTED"
    INTERNAL = "INTERNAL"
    PRIVATE = "PRIVATE"


############################################
# Definition of Classes
############################################

class aS3_forInClauseTail:

    pass
class aS3_forInClauseDecl:

    pass
class aS3_forIter:

    pass
class aS3_forCond:

    pass
class aS3_forInit:

    pass
class aS3_traditionalForClause:

    pass
class aS3_forInClause:

    pass
class aS3_DefaultStatement:

    pass
class aS3_CaseStatement:

    pass
class aS3_catchBlock:

    pass
class aS3_finallyBlock:

    pass
class finallyBlock:

    pass
class aS3_parameterDefault:

    pass
class parameterDeclaration:

    pass
class aS3_parameterRestDeclaration(parameterDeclaration):

    pass
class aS3_basicParameterDeclaration(parameterDeclaration):

    pass
class aS3_parameterDeclaration:

    pass
class aS3_parameterDeclarationList:

    pass
class aS3_switchBlock:

    pass
class SwitchStatement:

    pass
class aS3_Condition(SwitchStatement):

    pass
class aS3_fullNewSubexpression:

    def __init__(self, fnsd: str, aS3_fullNewSubexpression: set["aS3_primaryExpression"] = None, aS3_fullNewSubexpression241: set["aS3_qualifiedIdent"] = None, aS3_fullNewSubexpression244: set["aS3_brackets"] = None):
        self.fnsd = fnsd
        self.aS3_fullNewSubexpression = aS3_fullNewSubexpression if aS3_fullNewSubexpression is not None else set()
        self.aS3_fullNewSubexpression241 = aS3_fullNewSubexpression241 if aS3_fullNewSubexpression241 is not None else set()
        self.aS3_fullNewSubexpression244 = aS3_fullNewSubexpression244 if aS3_fullNewSubexpression244 is not None else set()
        
    @property
    def fnsd(self) -> str:
        return self.__fnsd

    @fnsd.setter
    def fnsd(self, fnsd: str):
        self.__fnsd = fnsd

    @property
    def aS3_fullNewSubexpression244(self):
        return self.__aS3_fullNewSubexpression244

    @aS3_fullNewSubexpression244.setter
    def aS3_fullNewSubexpression244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_fullNewSubexpression__aS3_fullNewSubexpression244", None)
        self.__aS3_fullNewSubexpression244 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aS3_brackets245"):
                    opp_val = getattr(item, "aS3_brackets245", None)
                    
                    if opp_val == self:
                        setattr(item, "aS3_brackets245", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aS3_brackets245"):
                    opp_val = getattr(item, "aS3_brackets245", None)
                    
                    setattr(item, "aS3_brackets245", self)
                    

    @property
    def aS3_fullNewSubexpression(self):
        return self.__aS3_fullNewSubexpression

    @aS3_fullNewSubexpression.setter
    def aS3_fullNewSubexpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_fullNewSubexpression__aS3_fullNewSubexpression", None)
        self.__aS3_fullNewSubexpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aS3_primaryExpression239"):
                    opp_val = getattr(item, "aS3_primaryExpression239", None)
                    
                    if opp_val == self:
                        setattr(item, "aS3_primaryExpression239", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aS3_primaryExpression239"):
                    opp_val = getattr(item, "aS3_primaryExpression239", None)
                    
                    setattr(item, "aS3_primaryExpression239", self)
                    

    @property
    def aS3_fullNewSubexpression241(self):
        return self.__aS3_fullNewSubexpression241

    @aS3_fullNewSubexpression241.setter
    def aS3_fullNewSubexpression241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_fullNewSubexpression__aS3_fullNewSubexpression241", None)
        self.__aS3_fullNewSubexpression241 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aS3_qualifiedIdent242"):
                    opp_val = getattr(item, "aS3_qualifiedIdent242", None)
                    
                    if opp_val == self:
                        setattr(item, "aS3_qualifiedIdent242", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aS3_qualifiedIdent242"):
                    opp_val = getattr(item, "aS3_qualifiedIdent242", None)
                    
                    setattr(item, "aS3_qualifiedIdent242", self)
                    

class aS3_regexpLiteral:

    def __init__(self, s: str, aS3_regexpLiteral: "aS3_RegexpConstant" = None):
        self.s = s
        self.aS3_regexpLiteral = aS3_regexpLiteral
        
    @property
    def s(self) -> str:
        return self.__s

    @s.setter
    def s(self, s: str):
        self.__s = s

    @property
    def aS3_regexpLiteral(self):
        return self.__aS3_regexpLiteral

    @aS3_regexpLiteral.setter
    def aS3_regexpLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_regexpLiteral__aS3_regexpLiteral", None)
        self.__aS3_regexpLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_RegexpConstant"):
                opp_val = getattr(old_value, "aS3_RegexpConstant", None)
                if opp_val == self:
                    setattr(old_value, "aS3_RegexpConstant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_RegexpConstant"):
                opp_val = getattr(value, "aS3_RegexpConstant", None)
                setattr(value, "aS3_RegexpConstant", self)

class expressionQualifiedIdentifier:

    pass
class aS3_encapsulatedExpression(expressionQualifiedIdentifier):

    pass
class aS3_newExpression:

    pass
class aS3_arguments:

    pass
class aS3_primaryExpression:

    pass
class aS3_unaryExpressionNotPlusMinus:

    def __init__(self, in: str, de: str, aS3_unaryExpressionNotPlusMinus: "aS3_unaryExpression" = None):
        self.in = in
        self.de = de
        self.aS3_unaryExpressionNotPlusMinus = aS3_unaryExpressionNotPlusMinus
        
    @property
    def in(self) -> str:
        return self.__in

    @in.setter
    def in(self, in: str):
        self.__in = in

    @property
    def de(self) -> str:
        return self.__de

    @de.setter
    def de(self, de: str):
        self.__de = de

    @property
    def aS3_unaryExpressionNotPlusMinus(self):
        return self.__aS3_unaryExpressionNotPlusMinus

    @aS3_unaryExpressionNotPlusMinus.setter
    def aS3_unaryExpressionNotPlusMinus(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_unaryExpressionNotPlusMinus__aS3_unaryExpressionNotPlusMinus", None)
        self.__aS3_unaryExpressionNotPlusMinus = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_unaryExpression184"):
                opp_val = getattr(old_value, "aS3_unaryExpression184", None)
                if opp_val == self:
                    setattr(old_value, "aS3_unaryExpression184", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_unaryExpression184"):
                opp_val = getattr(value, "aS3_unaryExpression184", None)
                setattr(value, "aS3_unaryExpression184", self)

class unaryExpressionNotPlusMinus:

    pass
class aS3_postfixExpression(unaryExpressionNotPlusMinus):

    pass
class aS3_unaryExpression(unaryExpressionNotPlusMinus):

    pass
class aS3_multiplicativeExpression:

    def __init__(self, o: str, aS3_multiplicativeExpression: "aS3_additiveExpression" = None, aS3_multiplicativeExpression173: set["aS3_unaryExpression"] = None):
        self.o = o
        self.aS3_multiplicativeExpression = aS3_multiplicativeExpression
        self.aS3_multiplicativeExpression173 = aS3_multiplicativeExpression173 if aS3_multiplicativeExpression173 is not None else set()
        
    @property
    def o(self) -> str:
        return self.__o

    @o.setter
    def o(self, o: str):
        self.__o = o

    @property
    def aS3_multiplicativeExpression173(self):
        return self.__aS3_multiplicativeExpression173

    @aS3_multiplicativeExpression173.setter
    def aS3_multiplicativeExpression173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_multiplicativeExpression__aS3_multiplicativeExpression173", None)
        self.__aS3_multiplicativeExpression173 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aS3_unaryExpression"):
                    opp_val = getattr(item, "aS3_unaryExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "aS3_unaryExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aS3_unaryExpression"):
                    opp_val = getattr(item, "aS3_unaryExpression", None)
                    
                    setattr(item, "aS3_unaryExpression", self)
                    

    @property
    def aS3_multiplicativeExpression(self):
        return self.__aS3_multiplicativeExpression

    @aS3_multiplicativeExpression.setter
    def aS3_multiplicativeExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_multiplicativeExpression__aS3_multiplicativeExpression", None)
        self.__aS3_multiplicativeExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_additiveExpression171"):
                opp_val = getattr(old_value, "aS3_additiveExpression171", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_additiveExpression171"):
                opp_val = getattr(value, "aS3_additiveExpression171", None)
                if opp_val is None:
                    setattr(value, "aS3_additiveExpression171", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aS3_additiveExpression:

    def __init__(self, o: str, aS3_additiveExpression171: set["aS3_multiplicativeExpression"] = None, aS3_additiveExpression: "aS3_shiftExpression" = None):
        self.o = o
        self.aS3_additiveExpression171 = aS3_additiveExpression171 if aS3_additiveExpression171 is not None else set()
        self.aS3_additiveExpression = aS3_additiveExpression
        
    @property
    def o(self) -> str:
        return self.__o

    @o.setter
    def o(self, o: str):
        self.__o = o

    @property
    def aS3_additiveExpression(self):
        return self.__aS3_additiveExpression

    @aS3_additiveExpression.setter
    def aS3_additiveExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_additiveExpression__aS3_additiveExpression", None)
        self.__aS3_additiveExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_shiftExpression169"):
                opp_val = getattr(old_value, "aS3_shiftExpression169", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_shiftExpression169"):
                opp_val = getattr(value, "aS3_shiftExpression169", None)
                if opp_val is None:
                    setattr(value, "aS3_shiftExpression169", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aS3_additiveExpression171(self):
        return self.__aS3_additiveExpression171

    @aS3_additiveExpression171.setter
    def aS3_additiveExpression171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_additiveExpression__aS3_additiveExpression171", None)
        self.__aS3_additiveExpression171 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aS3_multiplicativeExpression"):
                    opp_val = getattr(item, "aS3_multiplicativeExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "aS3_multiplicativeExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aS3_multiplicativeExpression"):
                    opp_val = getattr(item, "aS3_multiplicativeExpression", None)
                    
                    setattr(item, "aS3_multiplicativeExpression", self)
                    

class aS3_shiftExpression:

    def __init__(self, o: str, aS3_shiftExpression: "aS3_relationalExpression" = None, aS3_shiftExpression169: set["aS3_additiveExpression"] = None):
        self.o = o
        self.aS3_shiftExpression = aS3_shiftExpression
        self.aS3_shiftExpression169 = aS3_shiftExpression169 if aS3_shiftExpression169 is not None else set()
        
    @property
    def o(self) -> str:
        return self.__o

    @o.setter
    def o(self, o: str):
        self.__o = o

    @property
    def aS3_shiftExpression169(self):
        return self.__aS3_shiftExpression169

    @aS3_shiftExpression169.setter
    def aS3_shiftExpression169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_shiftExpression__aS3_shiftExpression169", None)
        self.__aS3_shiftExpression169 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aS3_additiveExpression"):
                    opp_val = getattr(item, "aS3_additiveExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "aS3_additiveExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aS3_additiveExpression"):
                    opp_val = getattr(item, "aS3_additiveExpression", None)
                    
                    setattr(item, "aS3_additiveExpression", self)
                    

    @property
    def aS3_shiftExpression(self):
        return self.__aS3_shiftExpression

    @aS3_shiftExpression.setter
    def aS3_shiftExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_shiftExpression__aS3_shiftExpression", None)
        self.__aS3_shiftExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_relationalExpression167"):
                opp_val = getattr(old_value, "aS3_relationalExpression167", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_relationalExpression167"):
                opp_val = getattr(value, "aS3_relationalExpression167", None)
                if opp_val is None:
                    setattr(value, "aS3_relationalExpression167", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aS3_relationalExpression:

    def __init__(self, o: str, aS3_relationalExpression: "aS3_equalityExpression" = None, aS3_relationalExpression167: set["aS3_shiftExpression"] = None):
        self.o = o
        self.aS3_relationalExpression = aS3_relationalExpression
        self.aS3_relationalExpression167 = aS3_relationalExpression167 if aS3_relationalExpression167 is not None else set()
        
    @property
    def o(self) -> str:
        return self.__o

    @o.setter
    def o(self, o: str):
        self.__o = o

    @property
    def aS3_relationalExpression(self):
        return self.__aS3_relationalExpression

    @aS3_relationalExpression.setter
    def aS3_relationalExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_relationalExpression__aS3_relationalExpression", None)
        self.__aS3_relationalExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_equalityExpression165"):
                opp_val = getattr(old_value, "aS3_equalityExpression165", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_equalityExpression165"):
                opp_val = getattr(value, "aS3_equalityExpression165", None)
                if opp_val is None:
                    setattr(value, "aS3_equalityExpression165", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aS3_relationalExpression167(self):
        return self.__aS3_relationalExpression167

    @aS3_relationalExpression167.setter
    def aS3_relationalExpression167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_relationalExpression__aS3_relationalExpression167", None)
        self.__aS3_relationalExpression167 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aS3_shiftExpression"):
                    opp_val = getattr(item, "aS3_shiftExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "aS3_shiftExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aS3_shiftExpression"):
                    opp_val = getattr(item, "aS3_shiftExpression", None)
                    
                    setattr(item, "aS3_shiftExpression", self)
                    

class aS3_equalityExpression:

    def __init__(self, o: str, aS3_equalityExpression: "aS3_bitwiseAndExpression" = None, aS3_equalityExpression165: set["aS3_relationalExpression"] = None):
        self.o = o
        self.aS3_equalityExpression = aS3_equalityExpression
        self.aS3_equalityExpression165 = aS3_equalityExpression165 if aS3_equalityExpression165 is not None else set()
        
    @property
    def o(self) -> str:
        return self.__o

    @o.setter
    def o(self, o: str):
        self.__o = o

    @property
    def aS3_equalityExpression165(self):
        return self.__aS3_equalityExpression165

    @aS3_equalityExpression165.setter
    def aS3_equalityExpression165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_equalityExpression__aS3_equalityExpression165", None)
        self.__aS3_equalityExpression165 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aS3_relationalExpression"):
                    opp_val = getattr(item, "aS3_relationalExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "aS3_relationalExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aS3_relationalExpression"):
                    opp_val = getattr(item, "aS3_relationalExpression", None)
                    
                    setattr(item, "aS3_relationalExpression", self)
                    

    @property
    def aS3_equalityExpression(self):
        return self.__aS3_equalityExpression

    @aS3_equalityExpression.setter
    def aS3_equalityExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_equalityExpression__aS3_equalityExpression", None)
        self.__aS3_equalityExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_bitwiseAndExpression163"):
                opp_val = getattr(old_value, "aS3_bitwiseAndExpression163", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_bitwiseAndExpression163"):
                opp_val = getattr(value, "aS3_bitwiseAndExpression163", None)
                if opp_val is None:
                    setattr(value, "aS3_bitwiseAndExpression163", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aS3_bitwiseAndExpression:

    def __init__(self, o: str, aS3_bitwiseAndExpression: "aS3_bitwiseXorExpression" = None, aS3_bitwiseAndExpression163: set["aS3_equalityExpression"] = None):
        self.o = o
        self.aS3_bitwiseAndExpression = aS3_bitwiseAndExpression
        self.aS3_bitwiseAndExpression163 = aS3_bitwiseAndExpression163 if aS3_bitwiseAndExpression163 is not None else set()
        
    @property
    def o(self) -> str:
        return self.__o

    @o.setter
    def o(self, o: str):
        self.__o = o

    @property
    def aS3_bitwiseAndExpression(self):
        return self.__aS3_bitwiseAndExpression

    @aS3_bitwiseAndExpression.setter
    def aS3_bitwiseAndExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_bitwiseAndExpression__aS3_bitwiseAndExpression", None)
        self.__aS3_bitwiseAndExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_bitwiseXorExpression161"):
                opp_val = getattr(old_value, "aS3_bitwiseXorExpression161", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_bitwiseXorExpression161"):
                opp_val = getattr(value, "aS3_bitwiseXorExpression161", None)
                if opp_val is None:
                    setattr(value, "aS3_bitwiseXorExpression161", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aS3_bitwiseAndExpression163(self):
        return self.__aS3_bitwiseAndExpression163

    @aS3_bitwiseAndExpression163.setter
    def aS3_bitwiseAndExpression163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_bitwiseAndExpression__aS3_bitwiseAndExpression163", None)
        self.__aS3_bitwiseAndExpression163 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aS3_equalityExpression"):
                    opp_val = getattr(item, "aS3_equalityExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "aS3_equalityExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aS3_equalityExpression"):
                    opp_val = getattr(item, "aS3_equalityExpression", None)
                    
                    setattr(item, "aS3_equalityExpression", self)
                    

class aS3_bitwiseXorExpression:

    def __init__(self, o: str, aS3_bitwiseXorExpression: "aS3_bitwiseOrExpression" = None, aS3_bitwiseXorExpression161: set["aS3_bitwiseAndExpression"] = None):
        self.o = o
        self.aS3_bitwiseXorExpression = aS3_bitwiseXorExpression
        self.aS3_bitwiseXorExpression161 = aS3_bitwiseXorExpression161 if aS3_bitwiseXorExpression161 is not None else set()
        
    @property
    def o(self) -> str:
        return self.__o

    @o.setter
    def o(self, o: str):
        self.__o = o

    @property
    def aS3_bitwiseXorExpression(self):
        return self.__aS3_bitwiseXorExpression

    @aS3_bitwiseXorExpression.setter
    def aS3_bitwiseXorExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_bitwiseXorExpression__aS3_bitwiseXorExpression", None)
        self.__aS3_bitwiseXorExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_bitwiseOrExpression159"):
                opp_val = getattr(old_value, "aS3_bitwiseOrExpression159", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_bitwiseOrExpression159"):
                opp_val = getattr(value, "aS3_bitwiseOrExpression159", None)
                if opp_val is None:
                    setattr(value, "aS3_bitwiseOrExpression159", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aS3_bitwiseXorExpression161(self):
        return self.__aS3_bitwiseXorExpression161

    @aS3_bitwiseXorExpression161.setter
    def aS3_bitwiseXorExpression161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_bitwiseXorExpression__aS3_bitwiseXorExpression161", None)
        self.__aS3_bitwiseXorExpression161 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aS3_bitwiseAndExpression"):
                    opp_val = getattr(item, "aS3_bitwiseAndExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "aS3_bitwiseAndExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aS3_bitwiseAndExpression"):
                    opp_val = getattr(item, "aS3_bitwiseAndExpression", None)
                    
                    setattr(item, "aS3_bitwiseAndExpression", self)
                    

class aS3_bitwiseOrExpression:

    def __init__(self, o: str, aS3_bitwiseOrExpression: "aS3_logicalAndExpression" = None, aS3_bitwiseOrExpression159: set["aS3_bitwiseXorExpression"] = None):
        self.o = o
        self.aS3_bitwiseOrExpression = aS3_bitwiseOrExpression
        self.aS3_bitwiseOrExpression159 = aS3_bitwiseOrExpression159 if aS3_bitwiseOrExpression159 is not None else set()
        
    @property
    def o(self) -> str:
        return self.__o

    @o.setter
    def o(self, o: str):
        self.__o = o

    @property
    def aS3_bitwiseOrExpression(self):
        return self.__aS3_bitwiseOrExpression

    @aS3_bitwiseOrExpression.setter
    def aS3_bitwiseOrExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_bitwiseOrExpression__aS3_bitwiseOrExpression", None)
        self.__aS3_bitwiseOrExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_logicalAndExpression"):
                opp_val = getattr(old_value, "aS3_logicalAndExpression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_logicalAndExpression"):
                opp_val = getattr(value, "aS3_logicalAndExpression", None)
                if opp_val is None:
                    setattr(value, "aS3_logicalAndExpression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aS3_bitwiseOrExpression159(self):
        return self.__aS3_bitwiseOrExpression159

    @aS3_bitwiseOrExpression159.setter
    def aS3_bitwiseOrExpression159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_bitwiseOrExpression__aS3_bitwiseOrExpression159", None)
        self.__aS3_bitwiseOrExpression159 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aS3_bitwiseXorExpression"):
                    opp_val = getattr(item, "aS3_bitwiseXorExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "aS3_bitwiseXorExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aS3_bitwiseXorExpression"):
                    opp_val = getattr(item, "aS3_bitwiseXorExpression", None)
                    
                    setattr(item, "aS3_bitwiseXorExpression", self)
                    

class aS3_logicalAndExpression:

    def __init__(self, o: str, aS3_logicalAndExpression: set["aS3_bitwiseOrExpression"] = None):
        self.o = o
        self.aS3_logicalAndExpression = aS3_logicalAndExpression if aS3_logicalAndExpression is not None else set()
        
    @property
    def o(self) -> str:
        return self.__o

    @o.setter
    def o(self, o: str):
        self.__o = o

    @property
    def aS3_logicalAndExpression(self):
        return self.__aS3_logicalAndExpression

    @aS3_logicalAndExpression.setter
    def aS3_logicalAndExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_logicalAndExpression__aS3_logicalAndExpression", None)
        self.__aS3_logicalAndExpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aS3_bitwiseOrExpression"):
                    opp_val = getattr(item, "aS3_bitwiseOrExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "aS3_bitwiseOrExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aS3_bitwiseOrExpression"):
                    opp_val = getattr(item, "aS3_bitwiseOrExpression", None)
                    
                    setattr(item, "aS3_bitwiseOrExpression", self)
                    

class conditionalExpression:

    pass
class aS3_logicalOrExpression(conditionalExpression):

    def __init__(self, o: str, aS3_logicalOrExpression: "aS3_conditionalSubExpression" = None):
        self.o = o
        self.aS3_logicalOrExpression = aS3_logicalOrExpression
        
    @property
    def o(self) -> str:
        return self.__o

    @o.setter
    def o(self, o: str):
        self.__o = o

    @property
    def aS3_logicalOrExpression(self):
        return self.__aS3_logicalOrExpression

    @aS3_logicalOrExpression.setter
    def aS3_logicalOrExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_logicalOrExpression__aS3_logicalOrExpression", None)
        self.__aS3_logicalOrExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_conditionalSubExpression156"):
                opp_val = getattr(old_value, "aS3_conditionalSubExpression156", None)
                if opp_val == self:
                    setattr(old_value, "aS3_conditionalSubExpression156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_conditionalSubExpression156"):
                opp_val = getattr(value, "aS3_conditionalSubExpression156", None)
                setattr(value, "aS3_conditionalSubExpression156", self)

class aS3_conditionalSubExpression:

    pass
class parameterDefault:

    pass
class encapsulatedExpression:

    pass
class Expression:

    pass
class aS3_BoolConstant(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class aS3_NumberConstant(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class aS3_StringConstant(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class aS3_This(Expression):

    pass
class aS3_RegexpConstant(Expression):

    pass
class aS3_Null(Expression):

    pass
class aS3_Undefined(Expression):

    pass
class aS3_SymbolRef(Expression):

    pass
class aS3_XmlConstant(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class nonemptyElementList:

    pass
class element:

    pass
class forInClauseTail:

    pass
class ExpressionStatement:

    pass
class brackets:

    pass
class aS3_expressionList(ExpressionStatement, brackets, forInClauseTail):

    pass
class aS3_switchStatementList:

    pass
class CaseStatement:

    pass
class ThrowStatement:

    pass
class DefaultXMLNamespaceStatement:

    pass
class Condition:

    pass
class elementList:

    pass
class aS3_nonemptyElementList(elementList):

    pass
class aS3_elementList:

    pass
class aS3_arrayLiteral:

    pass
class qualifiedIdent:

    pass
class aS3_namespaceName(qualifiedIdent):

    def __init__(self, level: str):
        self.level = level
        
    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

class aS3_qualifiedIdentifier:

    pass
class qualifiedIdentifier:

    pass
class aS3_e4xAttributeIdentifier(qualifiedIdentifier):

    pass
class aS3_nonAttributeQualifiedIdentifier(qualifiedIdentifier):

    pass
class assignmentExpression:

    pass
class aS3_conditionalExpression(assignmentExpression):

    def __init__(self, op: str, aS3_conditionalExpression: set["aS3_Expression"] = None):
        self.op = op
        self.aS3_conditionalExpression = aS3_conditionalExpression if aS3_conditionalExpression is not None else set()
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def aS3_conditionalExpression(self):
        return self.__aS3_conditionalExpression

    @aS3_conditionalExpression.setter
    def aS3_conditionalExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_conditionalExpression__aS3_conditionalExpression", None)
        self.__aS3_conditionalExpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aS3_Expression149"):
                    opp_val = getattr(item, "aS3_Expression149", None)
                    
                    if opp_val == self:
                        setattr(item, "aS3_Expression149", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aS3_Expression149"):
                    opp_val = getattr(item, "aS3_Expression149", None)
                    
                    setattr(item, "aS3_Expression149", self)
                    

class nonAttributeQualifiedIdentifier:

    pass
class aS3_expressionQualifiedIdentifier(nonAttributeQualifiedIdentifier):

    pass
class aS3_simpleQualifiedIdentifier(nonAttributeQualifiedIdentifier):

    pass
class aS3_qualifier:

    def __init__(self, level: str, aS3_qualifier: "aS3_simpleQualifiedIdentifier" = None):
        self.level = level
        self.aS3_qualifier = aS3_qualifier
        
    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def aS3_qualifier(self):
        return self.__aS3_qualifier

    @aS3_qualifier.setter
    def aS3_qualifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_qualifier__aS3_qualifier", None)
        self.__aS3_qualifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_simpleQualifiedIdentifier134"):
                opp_val = getattr(old_value, "aS3_simpleQualifiedIdentifier134", None)
                if opp_val == self:
                    setattr(old_value, "aS3_simpleQualifiedIdentifier134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_simpleQualifiedIdentifier134"):
                opp_val = getattr(value, "aS3_simpleQualifiedIdentifier134", None)
                setattr(value, "aS3_simpleQualifiedIdentifier134", self)

class qualifier:

    pass
class aS3_propertyIdentifier(qualifier):

    pass
class aS3_propOrIdent:

    pass
class aS3_identifier:

    pass
class aS3_typeExpression:

    pass
class catchBlock:

    pass
class propertyIdentifier:

    pass
class aS3_qualifiedIdent:

    pass
class aS3_brackets:

    pass
class aS3_literalField:

    pass
class aS3_fieldList:

    pass
class exprOrObjectLiteral:

    pass
class aS3_objectLiteral(exprOrObjectLiteral):

    pass
class aS3_exprOrObjectLiteral:

    pass
class forInClauseDecl:

    pass
class aS3_identi(propertyIdentifier, forInClauseDecl, catchBlock):

    def __init__(self, i: str, aS3_identi: "aS3_fieldName" = None, aS3_identi122: "aS3_qualifiedIdent" = None, aS3_identi124: "aS3_typeExpression" = None, aS3_identi126: "aS3_Block" = None, aS3_identi264: "aS3_parameterDeclaration" = None):
        self.i = i
        self.aS3_identi = aS3_identi
        self.aS3_identi122 = aS3_identi122
        self.aS3_identi124 = aS3_identi124
        self.aS3_identi126 = aS3_identi126
        self.aS3_identi264 = aS3_identi264
        
    @property
    def i(self) -> str:
        return self.__i

    @i.setter
    def i(self, i: str):
        self.__i = i

    @property
    def aS3_identi126(self):
        return self.__aS3_identi126

    @aS3_identi126.setter
    def aS3_identi126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_identi__aS3_identi126", None)
        self.__aS3_identi126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_Block127"):
                opp_val = getattr(old_value, "aS3_Block127", None)
                if opp_val == self:
                    setattr(old_value, "aS3_Block127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_Block127"):
                opp_val = getattr(value, "aS3_Block127", None)
                setattr(value, "aS3_Block127", self)

    @property
    def aS3_identi(self):
        return self.__aS3_identi

    @aS3_identi.setter
    def aS3_identi(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_identi__aS3_identi", None)
        self.__aS3_identi = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_fieldName120"):
                opp_val = getattr(old_value, "aS3_fieldName120", None)
                if opp_val == self:
                    setattr(old_value, "aS3_fieldName120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_fieldName120"):
                opp_val = getattr(value, "aS3_fieldName120", None)
                setattr(value, "aS3_fieldName120", self)

    @property
    def aS3_identi124(self):
        return self.__aS3_identi124

    @aS3_identi124.setter
    def aS3_identi124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_identi__aS3_identi124", None)
        self.__aS3_identi124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_typeExpression"):
                opp_val = getattr(old_value, "aS3_typeExpression", None)
                if opp_val == self:
                    setattr(old_value, "aS3_typeExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_typeExpression"):
                opp_val = getattr(value, "aS3_typeExpression", None)
                setattr(value, "aS3_typeExpression", self)

    @property
    def aS3_identi264(self):
        return self.__aS3_identi264

    @aS3_identi264.setter
    def aS3_identi264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_identi__aS3_identi264", None)
        self.__aS3_identi264 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_parameterDeclaration"):
                opp_val = getattr(old_value, "aS3_parameterDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "aS3_parameterDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_parameterDeclaration"):
                opp_val = getattr(value, "aS3_parameterDeclaration", None)
                setattr(value, "aS3_parameterDeclaration", self)

    @property
    def aS3_identi122(self):
        return self.__aS3_identi122

    @aS3_identi122.setter
    def aS3_identi122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_identi__aS3_identi122", None)
        self.__aS3_identi122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_qualifiedIdent"):
                opp_val = getattr(old_value, "aS3_qualifiedIdent", None)
                if opp_val == self:
                    setattr(old_value, "aS3_qualifiedIdent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_qualifiedIdent"):
                opp_val = getattr(value, "aS3_qualifiedIdent", None)
                setattr(value, "aS3_qualifiedIdent", self)

class Statement:

    pass
class aS3_ThrowStatement(Statement):

    pass
class aS3_ExpressionStatement(Statement):

    pass
class aS3_IfStatement(Statement):

    pass
class aS3_WhileStatement(Statement):

    pass
class aS3_ReturnStatement(Statement):

    pass
class aS3_DefaultXMLNamespaceStatement(Statement):

    pass
class aS3_SwitchStatement(Statement):

    pass
class aS3_ForStatement(Statement):

    pass
class aS3_WithStatement(Statement):

    pass
class aS3_DoWhileStatement(Statement):

    pass
class aS3_ForEachStatement(Statement):

    pass
class aS3_TryStatement(Statement):

    pass
class aS3_VariableDeclaration(Statement, forInClauseDecl):

    def __init__(self, name: str, anytype: str, aS3_VariableDeclaration: "aS3_EObject" = None, aS3_VariableDeclaration102: "aS3_assignmentExpression" = None, aS3_VariableDeclaration325: "aS3_forInit" = None):
        self.name = name
        self.anytype = anytype
        self.aS3_VariableDeclaration = aS3_VariableDeclaration
        self.aS3_VariableDeclaration102 = aS3_VariableDeclaration102
        self.aS3_VariableDeclaration325 = aS3_VariableDeclaration325
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def anytype(self) -> str:
        return self.__anytype

    @anytype.setter
    def anytype(self, anytype: str):
        self.__anytype = anytype

    @property
    def aS3_VariableDeclaration(self):
        return self.__aS3_VariableDeclaration

    @aS3_VariableDeclaration.setter
    def aS3_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_VariableDeclaration__aS3_VariableDeclaration", None)
        self.__aS3_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_EObject100"):
                opp_val = getattr(old_value, "aS3_EObject100", None)
                if opp_val == self:
                    setattr(old_value, "aS3_EObject100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_EObject100"):
                opp_val = getattr(value, "aS3_EObject100", None)
                setattr(value, "aS3_EObject100", self)

    @property
    def aS3_VariableDeclaration325(self):
        return self.__aS3_VariableDeclaration325

    @aS3_VariableDeclaration325.setter
    def aS3_VariableDeclaration325(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_VariableDeclaration__aS3_VariableDeclaration325", None)
        self.__aS3_VariableDeclaration325 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_forInit324"):
                opp_val = getattr(old_value, "aS3_forInit324", None)
                if opp_val == self:
                    setattr(old_value, "aS3_forInit324", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_forInit324"):
                opp_val = getattr(value, "aS3_forInit324", None)
                setattr(value, "aS3_forInit324", self)

    @property
    def aS3_VariableDeclaration102(self):
        return self.__aS3_VariableDeclaration102

    @aS3_VariableDeclaration102.setter
    def aS3_VariableDeclaration102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_VariableDeclaration__aS3_VariableDeclaration102", None)
        self.__aS3_VariableDeclaration102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_assignmentExpression103"):
                opp_val = getattr(old_value, "aS3_assignmentExpression103", None)
                if opp_val == self:
                    setattr(old_value, "aS3_assignmentExpression103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_assignmentExpression103"):
                opp_val = getattr(value, "aS3_assignmentExpression103", None)
                setattr(value, "aS3_assignmentExpression103", self)

class aS3_assignmentExpression(parameterDefault, encapsulatedExpression, element, Expression, nonemptyElementList):

    pass
class aS3_element:

    pass
class aS3_fieldName:

    def __init__(self, number: str, name: str, aS3_fieldName: "aS3_literalField" = None, aS3_fieldName120: "aS3_identi" = None):
        self.number = number
        self.name = name
        self.aS3_fieldName = aS3_fieldName
        self.aS3_fieldName120 = aS3_fieldName120
        
    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def aS3_fieldName120(self):
        return self.__aS3_fieldName120

    @aS3_fieldName120.setter
    def aS3_fieldName120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_fieldName__aS3_fieldName120", None)
        self.__aS3_fieldName120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_identi"):
                opp_val = getattr(old_value, "aS3_identi", None)
                if opp_val == self:
                    setattr(old_value, "aS3_identi", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_identi"):
                opp_val = getattr(value, "aS3_identi", None)
                setattr(value, "aS3_identi", self)

    @property
    def aS3_fieldName(self):
        return self.__aS3_fieldName

    @aS3_fieldName.setter
    def aS3_fieldName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_fieldName__aS3_fieldName", None)
        self.__aS3_fieldName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_literalField116"):
                opp_val = getattr(old_value, "aS3_literalField116", None)
                if opp_val == self:
                    setattr(old_value, "aS3_literalField116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_literalField116"):
                opp_val = getattr(value, "aS3_literalField116", None)
                setattr(value, "aS3_literalField116", self)

class aS3_Method:

    def __init__(self, name: str, anytype: str, aS3_Method: "aS3_Member" = None, aS3_Method70: set["aS3_Annotation"] = None, aS3_Method73: "aS3_Modifier" = None, aS3_Method76: "aS3_AccessorRole" = None, aS3_Method79: set["aS3_Parameter"] = None, aS3_Method82: "aS3_EObject" = None, aS3_Method85: "aS3_Block" = None):
        self.name = name
        self.anytype = anytype
        self.aS3_Method = aS3_Method
        self.aS3_Method70 = aS3_Method70 if aS3_Method70 is not None else set()
        self.aS3_Method73 = aS3_Method73
        self.aS3_Method76 = aS3_Method76
        self.aS3_Method79 = aS3_Method79 if aS3_Method79 is not None else set()
        self.aS3_Method82 = aS3_Method82
        self.aS3_Method85 = aS3_Method85
        
    @property
    def anytype(self) -> str:
        return self.__anytype

    @anytype.setter
    def anytype(self, anytype: str):
        self.__anytype = anytype

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def aS3_Method82(self):
        return self.__aS3_Method82

    @aS3_Method82.setter
    def aS3_Method82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Method__aS3_Method82", None)
        self.__aS3_Method82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_EObject83"):
                opp_val = getattr(old_value, "aS3_EObject83", None)
                if opp_val == self:
                    setattr(old_value, "aS3_EObject83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_EObject83"):
                opp_val = getattr(value, "aS3_EObject83", None)
                setattr(value, "aS3_EObject83", self)

    @property
    def aS3_Method85(self):
        return self.__aS3_Method85

    @aS3_Method85.setter
    def aS3_Method85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Method__aS3_Method85", None)
        self.__aS3_Method85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_Block86"):
                opp_val = getattr(old_value, "aS3_Block86", None)
                if opp_val == self:
                    setattr(old_value, "aS3_Block86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_Block86"):
                opp_val = getattr(value, "aS3_Block86", None)
                setattr(value, "aS3_Block86", self)

    @property
    def aS3_Method70(self):
        return self.__aS3_Method70

    @aS3_Method70.setter
    def aS3_Method70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Method__aS3_Method70", None)
        self.__aS3_Method70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aS3_Annotation71"):
                    opp_val = getattr(item, "aS3_Annotation71", None)
                    
                    if opp_val == self:
                        setattr(item, "aS3_Annotation71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aS3_Annotation71"):
                    opp_val = getattr(item, "aS3_Annotation71", None)
                    
                    setattr(item, "aS3_Annotation71", self)
                    

    @property
    def aS3_Method76(self):
        return self.__aS3_Method76

    @aS3_Method76.setter
    def aS3_Method76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Method__aS3_Method76", None)
        self.__aS3_Method76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_AccessorRole77"):
                opp_val = getattr(old_value, "aS3_AccessorRole77", None)
                if opp_val == self:
                    setattr(old_value, "aS3_AccessorRole77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_AccessorRole77"):
                opp_val = getattr(value, "aS3_AccessorRole77", None)
                setattr(value, "aS3_AccessorRole77", self)

    @property
    def aS3_Method79(self):
        return self.__aS3_Method79

    @aS3_Method79.setter
    def aS3_Method79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Method__aS3_Method79", None)
        self.__aS3_Method79 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aS3_Parameter80"):
                    opp_val = getattr(item, "aS3_Parameter80", None)
                    
                    if opp_val == self:
                        setattr(item, "aS3_Parameter80", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aS3_Parameter80"):
                    opp_val = getattr(item, "aS3_Parameter80", None)
                    
                    setattr(item, "aS3_Parameter80", self)
                    

    @property
    def aS3_Method73(self):
        return self.__aS3_Method73

    @aS3_Method73.setter
    def aS3_Method73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Method__aS3_Method73", None)
        self.__aS3_Method73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_Modifier74"):
                opp_val = getattr(old_value, "aS3_Modifier74", None)
                if opp_val == self:
                    setattr(old_value, "aS3_Modifier74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_Modifier74"):
                opp_val = getattr(value, "aS3_Modifier74", None)
                setattr(value, "aS3_Modifier74", self)

    @property
    def aS3_Method(self):
        return self.__aS3_Method

    @aS3_Method.setter
    def aS3_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Method__aS3_Method", None)
        self.__aS3_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_Member68"):
                opp_val = getattr(old_value, "aS3_Member68", None)
                if opp_val == self:
                    setattr(old_value, "aS3_Member68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_Member68"):
                opp_val = getattr(value, "aS3_Member68", None)
                setattr(value, "aS3_Member68", self)

class aS3_MemberVariableDeclaration:

    def __init__(self, name: str, anytype: str, aS3_MemberVariableDeclaration: "aS3_Member" = None, aS3_MemberVariableDeclaration89: set["aS3_Annotation"] = None, aS3_MemberVariableDeclaration92: "aS3_Modifier" = None, aS3_MemberVariableDeclaration95: "aS3_EObject" = None, aS3_MemberVariableDeclaration98: "aS3_assignmentExpression" = None):
        self.name = name
        self.anytype = anytype
        self.aS3_MemberVariableDeclaration = aS3_MemberVariableDeclaration
        self.aS3_MemberVariableDeclaration89 = aS3_MemberVariableDeclaration89 if aS3_MemberVariableDeclaration89 is not None else set()
        self.aS3_MemberVariableDeclaration92 = aS3_MemberVariableDeclaration92
        self.aS3_MemberVariableDeclaration95 = aS3_MemberVariableDeclaration95
        self.aS3_MemberVariableDeclaration98 = aS3_MemberVariableDeclaration98
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def anytype(self) -> str:
        return self.__anytype

    @anytype.setter
    def anytype(self, anytype: str):
        self.__anytype = anytype

    @property
    def aS3_MemberVariableDeclaration95(self):
        return self.__aS3_MemberVariableDeclaration95

    @aS3_MemberVariableDeclaration95.setter
    def aS3_MemberVariableDeclaration95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_MemberVariableDeclaration__aS3_MemberVariableDeclaration95", None)
        self.__aS3_MemberVariableDeclaration95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_EObject96"):
                opp_val = getattr(old_value, "aS3_EObject96", None)
                if opp_val == self:
                    setattr(old_value, "aS3_EObject96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_EObject96"):
                opp_val = getattr(value, "aS3_EObject96", None)
                setattr(value, "aS3_EObject96", self)

    @property
    def aS3_MemberVariableDeclaration(self):
        return self.__aS3_MemberVariableDeclaration

    @aS3_MemberVariableDeclaration.setter
    def aS3_MemberVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_MemberVariableDeclaration__aS3_MemberVariableDeclaration", None)
        self.__aS3_MemberVariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_Member66"):
                opp_val = getattr(old_value, "aS3_Member66", None)
                if opp_val == self:
                    setattr(old_value, "aS3_Member66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_Member66"):
                opp_val = getattr(value, "aS3_Member66", None)
                setattr(value, "aS3_Member66", self)

    @property
    def aS3_MemberVariableDeclaration92(self):
        return self.__aS3_MemberVariableDeclaration92

    @aS3_MemberVariableDeclaration92.setter
    def aS3_MemberVariableDeclaration92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_MemberVariableDeclaration__aS3_MemberVariableDeclaration92", None)
        self.__aS3_MemberVariableDeclaration92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_Modifier93"):
                opp_val = getattr(old_value, "aS3_Modifier93", None)
                if opp_val == self:
                    setattr(old_value, "aS3_Modifier93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_Modifier93"):
                opp_val = getattr(value, "aS3_Modifier93", None)
                setattr(value, "aS3_Modifier93", self)

    @property
    def aS3_MemberVariableDeclaration89(self):
        return self.__aS3_MemberVariableDeclaration89

    @aS3_MemberVariableDeclaration89.setter
    def aS3_MemberVariableDeclaration89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_MemberVariableDeclaration__aS3_MemberVariableDeclaration89", None)
        self.__aS3_MemberVariableDeclaration89 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aS3_Annotation90"):
                    opp_val = getattr(item, "aS3_Annotation90", None)
                    
                    if opp_val == self:
                        setattr(item, "aS3_Annotation90", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aS3_Annotation90"):
                    opp_val = getattr(item, "aS3_Annotation90", None)
                    
                    setattr(item, "aS3_Annotation90", self)
                    

    @property
    def aS3_MemberVariableDeclaration98(self):
        return self.__aS3_MemberVariableDeclaration98

    @aS3_MemberVariableDeclaration98.setter
    def aS3_MemberVariableDeclaration98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_MemberVariableDeclaration__aS3_MemberVariableDeclaration98", None)
        self.__aS3_MemberVariableDeclaration98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_assignmentExpression"):
                opp_val = getattr(old_value, "aS3_assignmentExpression", None)
                if opp_val == self:
                    setattr(old_value, "aS3_assignmentExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_assignmentExpression"):
                opp_val = getattr(value, "aS3_assignmentExpression", None)
                setattr(value, "aS3_assignmentExpression", self)

class aS3_Statement:

    pass
class aS3_MethodBody:

    pass
class aS3_Class:

    def __init__(self, name: str, aS3_Class59: "aS3_Class" = None, aS3_Class57: "aS3_Class" = None, aS3_Class61: set["aS3_Interface"] = None, aS3_Class64: set["aS3_Member"] = None, aS3_Class: set["aS3_Annotation"] = None, aS3_Class55: "aS3_Modifier" = None):
        self.name = name
        self.aS3_Class59 = aS3_Class59
        self.aS3_Class57 = aS3_Class57
        self.aS3_Class61 = aS3_Class61 if aS3_Class61 is not None else set()
        self.aS3_Class64 = aS3_Class64 if aS3_Class64 is not None else set()
        self.aS3_Class = aS3_Class if aS3_Class is not None else set()
        self.aS3_Class55 = aS3_Class55
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def aS3_Class55(self):
        return self.__aS3_Class55

    @aS3_Class55.setter
    def aS3_Class55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Class__aS3_Class55", None)
        self.__aS3_Class55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_Modifier56"):
                opp_val = getattr(old_value, "aS3_Modifier56", None)
                if opp_val == self:
                    setattr(old_value, "aS3_Modifier56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_Modifier56"):
                opp_val = getattr(value, "aS3_Modifier56", None)
                setattr(value, "aS3_Modifier56", self)

    @property
    def aS3_Class61(self):
        return self.__aS3_Class61

    @aS3_Class61.setter
    def aS3_Class61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Class__aS3_Class61", None)
        self.__aS3_Class61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aS3_Interface62"):
                    opp_val = getattr(item, "aS3_Interface62", None)
                    
                    if opp_val == self:
                        setattr(item, "aS3_Interface62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aS3_Interface62"):
                    opp_val = getattr(item, "aS3_Interface62", None)
                    
                    setattr(item, "aS3_Interface62", self)
                    

    @property
    def aS3_Class64(self):
        return self.__aS3_Class64

    @aS3_Class64.setter
    def aS3_Class64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Class__aS3_Class64", None)
        self.__aS3_Class64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aS3_Member"):
                    opp_val = getattr(item, "aS3_Member", None)
                    
                    if opp_val == self:
                        setattr(item, "aS3_Member", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aS3_Member"):
                    opp_val = getattr(item, "aS3_Member", None)
                    
                    setattr(item, "aS3_Member", self)
                    

    @property
    def aS3_Class57(self):
        return self.__aS3_Class57

    @aS3_Class57.setter
    def aS3_Class57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Class__aS3_Class57", None)
        self.__aS3_Class57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_Class59"):
                opp_val = getattr(old_value, "aS3_Class59", None)
                if opp_val == self:
                    setattr(old_value, "aS3_Class59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_Class59"):
                opp_val = getattr(value, "aS3_Class59", None)
                setattr(value, "aS3_Class59", self)

    @property
    def aS3_Class(self):
        return self.__aS3_Class

    @aS3_Class.setter
    def aS3_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Class__aS3_Class", None)
        self.__aS3_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aS3_Annotation53"):
                    opp_val = getattr(item, "aS3_Annotation53", None)
                    
                    if opp_val == self:
                        setattr(item, "aS3_Annotation53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aS3_Annotation53"):
                    opp_val = getattr(item, "aS3_Annotation53", None)
                    
                    setattr(item, "aS3_Annotation53", self)
                    

    @property
    def aS3_Class59(self):
        return self.__aS3_Class59

    @aS3_Class59.setter
    def aS3_Class59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Class__aS3_Class59", None)
        self.__aS3_Class59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_Class57"):
                opp_val = getattr(old_value, "aS3_Class57", None)
                if opp_val == self:
                    setattr(old_value, "aS3_Class57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_Class57"):
                opp_val = getattr(value, "aS3_Class57", None)
                setattr(value, "aS3_Class57", self)

class aS3_Block(Statement, finallyBlock):

    pass
class aS3_functionSignature:

    pass
class aS3_functionCommon:

    pass
class aS3_functionExpression:

    def __init__(self, name: str, aS3_functionExpression: "aS3_functionCommon" = None, aS3_functionExpression218: "aS3_primaryExpression" = None):
        self.name = name
        self.aS3_functionExpression = aS3_functionExpression
        self.aS3_functionExpression218 = aS3_functionExpression218
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def aS3_functionExpression(self):
        return self.__aS3_functionExpression

    @aS3_functionExpression.setter
    def aS3_functionExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_functionExpression__aS3_functionExpression", None)
        self.__aS3_functionExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_functionCommon"):
                opp_val = getattr(old_value, "aS3_functionCommon", None)
                if opp_val == self:
                    setattr(old_value, "aS3_functionCommon", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_functionCommon"):
                opp_val = getattr(value, "aS3_functionCommon", None)
                setattr(value, "aS3_functionCommon", self)

    @property
    def aS3_functionExpression218(self):
        return self.__aS3_functionExpression218

    @aS3_functionExpression218.setter
    def aS3_functionExpression218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_functionExpression__aS3_functionExpression218", None)
        self.__aS3_functionExpression218 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_primaryExpression217"):
                opp_val = getattr(old_value, "aS3_primaryExpression217", None)
                if opp_val == self:
                    setattr(old_value, "aS3_primaryExpression217", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_primaryExpression217"):
                opp_val = getattr(value, "aS3_primaryExpression217", None)
                setattr(value, "aS3_primaryExpression217", self)

class aS3_Parameter:

    def __init__(self, name: str, anytype: str, aS3_Parameter: "aS3_InterfaceMethod" = None, aS3_Parameter80: "aS3_Method" = None, aS3_Parameter105: "aS3_EObject" = None, aS3_Parameter108: "aS3_exprOrObjectLiteral" = None, aS3_Parameter262: "aS3_parameterDeclarationList" = None):
        self.name = name
        self.anytype = anytype
        self.aS3_Parameter = aS3_Parameter
        self.aS3_Parameter80 = aS3_Parameter80
        self.aS3_Parameter105 = aS3_Parameter105
        self.aS3_Parameter108 = aS3_Parameter108
        self.aS3_Parameter262 = aS3_Parameter262
        
    @property
    def anytype(self) -> str:
        return self.__anytype

    @anytype.setter
    def anytype(self, anytype: str):
        self.__anytype = anytype

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def aS3_Parameter108(self):
        return self.__aS3_Parameter108

    @aS3_Parameter108.setter
    def aS3_Parameter108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Parameter__aS3_Parameter108", None)
        self.__aS3_Parameter108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_exprOrObjectLiteral"):
                opp_val = getattr(old_value, "aS3_exprOrObjectLiteral", None)
                if opp_val == self:
                    setattr(old_value, "aS3_exprOrObjectLiteral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_exprOrObjectLiteral"):
                opp_val = getattr(value, "aS3_exprOrObjectLiteral", None)
                setattr(value, "aS3_exprOrObjectLiteral", self)

    @property
    def aS3_Parameter(self):
        return self.__aS3_Parameter

    @aS3_Parameter.setter
    def aS3_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Parameter__aS3_Parameter", None)
        self.__aS3_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_InterfaceMethod43"):
                opp_val = getattr(old_value, "aS3_InterfaceMethod43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_InterfaceMethod43"):
                opp_val = getattr(value, "aS3_InterfaceMethod43", None)
                if opp_val is None:
                    setattr(value, "aS3_InterfaceMethod43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aS3_Parameter105(self):
        return self.__aS3_Parameter105

    @aS3_Parameter105.setter
    def aS3_Parameter105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Parameter__aS3_Parameter105", None)
        self.__aS3_Parameter105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_EObject106"):
                opp_val = getattr(old_value, "aS3_EObject106", None)
                if opp_val == self:
                    setattr(old_value, "aS3_EObject106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_EObject106"):
                opp_val = getattr(value, "aS3_EObject106", None)
                setattr(value, "aS3_EObject106", self)

    @property
    def aS3_Parameter80(self):
        return self.__aS3_Parameter80

    @aS3_Parameter80.setter
    def aS3_Parameter80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Parameter__aS3_Parameter80", None)
        self.__aS3_Parameter80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_Method79"):
                opp_val = getattr(old_value, "aS3_Method79", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_Method79"):
                opp_val = getattr(value, "aS3_Method79", None)
                if opp_val is None:
                    setattr(value, "aS3_Method79", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aS3_Parameter262(self):
        return self.__aS3_Parameter262

    @aS3_Parameter262.setter
    def aS3_Parameter262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Parameter__aS3_Parameter262", None)
        self.__aS3_Parameter262 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_parameterDeclarationList261"):
                opp_val = getattr(old_value, "aS3_parameterDeclarationList261", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_parameterDeclarationList261"):
                opp_val = getattr(value, "aS3_parameterDeclarationList261", None)
                if opp_val is None:
                    setattr(value, "aS3_parameterDeclarationList261", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aS3_AccessorRole:

    def __init__(self, accessor: str, aS3_AccessorRole: "aS3_InterfaceMethod" = None, aS3_AccessorRole77: "aS3_Method" = None):
        self.accessor = accessor
        self.aS3_AccessorRole = aS3_AccessorRole
        self.aS3_AccessorRole77 = aS3_AccessorRole77
        
    @property
    def accessor(self) -> str:
        return self.__accessor

    @accessor.setter
    def accessor(self, accessor: str):
        self.__accessor = accessor

    @property
    def aS3_AccessorRole(self):
        return self.__aS3_AccessorRole

    @aS3_AccessorRole.setter
    def aS3_AccessorRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_AccessorRole__aS3_AccessorRole", None)
        self.__aS3_AccessorRole = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_InterfaceMethod41"):
                opp_val = getattr(old_value, "aS3_InterfaceMethod41", None)
                if opp_val == self:
                    setattr(old_value, "aS3_InterfaceMethod41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_InterfaceMethod41"):
                opp_val = getattr(value, "aS3_InterfaceMethod41", None)
                setattr(value, "aS3_InterfaceMethod41", self)

    @property
    def aS3_AccessorRole77(self):
        return self.__aS3_AccessorRole77

    @aS3_AccessorRole77.setter
    def aS3_AccessorRole77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_AccessorRole__aS3_AccessorRole77", None)
        self.__aS3_AccessorRole77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_Method76"):
                opp_val = getattr(old_value, "aS3_Method76", None)
                if opp_val == self:
                    setattr(old_value, "aS3_Method76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_Method76"):
                opp_val = getattr(value, "aS3_Method76", None)
                setattr(value, "aS3_Method76", self)

class aS3_Modifier:

    def __init__(self, static: bool, final: bool, native: bool, dynamic: bool, access: str, aS3_Modifier: "aS3_InterfaceMethod" = None, aS3_Modifier56: "aS3_Class" = None, aS3_Modifier74: "aS3_Method" = None, aS3_Modifier93: "aS3_MemberVariableDeclaration" = None):
        self.static = static
        self.final = final
        self.native = native
        self.dynamic = dynamic
        self.access = access
        self.aS3_Modifier = aS3_Modifier
        self.aS3_Modifier56 = aS3_Modifier56
        self.aS3_Modifier74 = aS3_Modifier74
        self.aS3_Modifier93 = aS3_Modifier93
        
    @property
    def access(self) -> str:
        return self.__access

    @access.setter
    def access(self, access: str):
        self.__access = access

    @property
    def native(self) -> bool:
        return self.__native

    @native.setter
    def native(self, native: bool):
        self.__native = native

    @property
    def dynamic(self) -> bool:
        return self.__dynamic

    @dynamic.setter
    def dynamic(self, dynamic: bool):
        self.__dynamic = dynamic

    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def final(self) -> bool:
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final

    @property
    def aS3_Modifier93(self):
        return self.__aS3_Modifier93

    @aS3_Modifier93.setter
    def aS3_Modifier93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Modifier__aS3_Modifier93", None)
        self.__aS3_Modifier93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_MemberVariableDeclaration92"):
                opp_val = getattr(old_value, "aS3_MemberVariableDeclaration92", None)
                if opp_val == self:
                    setattr(old_value, "aS3_MemberVariableDeclaration92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_MemberVariableDeclaration92"):
                opp_val = getattr(value, "aS3_MemberVariableDeclaration92", None)
                setattr(value, "aS3_MemberVariableDeclaration92", self)

    @property
    def aS3_Modifier(self):
        return self.__aS3_Modifier

    @aS3_Modifier.setter
    def aS3_Modifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Modifier__aS3_Modifier", None)
        self.__aS3_Modifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_InterfaceMethod39"):
                opp_val = getattr(old_value, "aS3_InterfaceMethod39", None)
                if opp_val == self:
                    setattr(old_value, "aS3_InterfaceMethod39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_InterfaceMethod39"):
                opp_val = getattr(value, "aS3_InterfaceMethod39", None)
                setattr(value, "aS3_InterfaceMethod39", self)

    @property
    def aS3_Modifier74(self):
        return self.__aS3_Modifier74

    @aS3_Modifier74.setter
    def aS3_Modifier74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Modifier__aS3_Modifier74", None)
        self.__aS3_Modifier74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_Method73"):
                opp_val = getattr(old_value, "aS3_Method73", None)
                if opp_val == self:
                    setattr(old_value, "aS3_Method73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_Method73"):
                opp_val = getattr(value, "aS3_Method73", None)
                setattr(value, "aS3_Method73", self)

    @property
    def aS3_Modifier56(self):
        return self.__aS3_Modifier56

    @aS3_Modifier56.setter
    def aS3_Modifier56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Modifier__aS3_Modifier56", None)
        self.__aS3_Modifier56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_Class55"):
                opp_val = getattr(old_value, "aS3_Class55", None)
                if opp_val == self:
                    setattr(old_value, "aS3_Class55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_Class55"):
                opp_val = getattr(value, "aS3_Class55", None)
                setattr(value, "aS3_Class55", self)

class aS3_InterfaceMethod:

    def __init__(self, name: str, anytype: str, aS3_InterfaceMethod: "aS3_Interface" = None, aS3_InterfaceMethod36: set["aS3_Annotation"] = None, aS3_InterfaceMethod39: "aS3_Modifier" = None, aS3_InterfaceMethod41: "aS3_AccessorRole" = None, aS3_InterfaceMethod43: set["aS3_Parameter"] = None, aS3_InterfaceMethod45: "aS3_EObject" = None):
        self.name = name
        self.anytype = anytype
        self.aS3_InterfaceMethod = aS3_InterfaceMethod
        self.aS3_InterfaceMethod36 = aS3_InterfaceMethod36 if aS3_InterfaceMethod36 is not None else set()
        self.aS3_InterfaceMethod39 = aS3_InterfaceMethod39
        self.aS3_InterfaceMethod41 = aS3_InterfaceMethod41
        self.aS3_InterfaceMethod43 = aS3_InterfaceMethod43 if aS3_InterfaceMethod43 is not None else set()
        self.aS3_InterfaceMethod45 = aS3_InterfaceMethod45
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def anytype(self) -> str:
        return self.__anytype

    @anytype.setter
    def anytype(self, anytype: str):
        self.__anytype = anytype

    @property
    def aS3_InterfaceMethod39(self):
        return self.__aS3_InterfaceMethod39

    @aS3_InterfaceMethod39.setter
    def aS3_InterfaceMethod39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_InterfaceMethod__aS3_InterfaceMethod39", None)
        self.__aS3_InterfaceMethod39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_Modifier"):
                opp_val = getattr(old_value, "aS3_Modifier", None)
                if opp_val == self:
                    setattr(old_value, "aS3_Modifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_Modifier"):
                opp_val = getattr(value, "aS3_Modifier", None)
                setattr(value, "aS3_Modifier", self)

    @property
    def aS3_InterfaceMethod(self):
        return self.__aS3_InterfaceMethod

    @aS3_InterfaceMethod.setter
    def aS3_InterfaceMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_InterfaceMethod__aS3_InterfaceMethod", None)
        self.__aS3_InterfaceMethod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_Interface34"):
                opp_val = getattr(old_value, "aS3_Interface34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_Interface34"):
                opp_val = getattr(value, "aS3_Interface34", None)
                if opp_val is None:
                    setattr(value, "aS3_Interface34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aS3_InterfaceMethod45(self):
        return self.__aS3_InterfaceMethod45

    @aS3_InterfaceMethod45.setter
    def aS3_InterfaceMethod45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_InterfaceMethod__aS3_InterfaceMethod45", None)
        self.__aS3_InterfaceMethod45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_EObject46"):
                opp_val = getattr(old_value, "aS3_EObject46", None)
                if opp_val == self:
                    setattr(old_value, "aS3_EObject46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_EObject46"):
                opp_val = getattr(value, "aS3_EObject46", None)
                setattr(value, "aS3_EObject46", self)

    @property
    def aS3_InterfaceMethod36(self):
        return self.__aS3_InterfaceMethod36

    @aS3_InterfaceMethod36.setter
    def aS3_InterfaceMethod36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_InterfaceMethod__aS3_InterfaceMethod36", None)
        self.__aS3_InterfaceMethod36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aS3_Annotation37"):
                    opp_val = getattr(item, "aS3_Annotation37", None)
                    
                    if opp_val == self:
                        setattr(item, "aS3_Annotation37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aS3_Annotation37"):
                    opp_val = getattr(item, "aS3_Annotation37", None)
                    
                    setattr(item, "aS3_Annotation37", self)
                    

    @property
    def aS3_InterfaceMethod41(self):
        return self.__aS3_InterfaceMethod41

    @aS3_InterfaceMethod41.setter
    def aS3_InterfaceMethod41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_InterfaceMethod__aS3_InterfaceMethod41", None)
        self.__aS3_InterfaceMethod41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_AccessorRole"):
                opp_val = getattr(old_value, "aS3_AccessorRole", None)
                if opp_val == self:
                    setattr(old_value, "aS3_AccessorRole", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_AccessorRole"):
                opp_val = getattr(value, "aS3_AccessorRole", None)
                setattr(value, "aS3_AccessorRole", self)

    @property
    def aS3_InterfaceMethod43(self):
        return self.__aS3_InterfaceMethod43

    @aS3_InterfaceMethod43.setter
    def aS3_InterfaceMethod43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_InterfaceMethod__aS3_InterfaceMethod43", None)
        self.__aS3_InterfaceMethod43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aS3_Parameter"):
                    opp_val = getattr(item, "aS3_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "aS3_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aS3_Parameter"):
                    opp_val = getattr(item, "aS3_Parameter", None)
                    
                    setattr(item, "aS3_Parameter", self)
                    

class aS3_Interface:

    def __init__(self, access: str, name: str, aS3_Interface62: "aS3_Class" = None, aS3_Interface: set["aS3_Annotation"] = None, aS3_Interface32: "aS3_Interface" = None, aS3_Interface30: "aS3_Interface" = None, aS3_Interface34: set["aS3_InterfaceMethod"] = None):
        self.access = access
        self.name = name
        self.aS3_Interface62 = aS3_Interface62
        self.aS3_Interface = aS3_Interface if aS3_Interface is not None else set()
        self.aS3_Interface32 = aS3_Interface32
        self.aS3_Interface30 = aS3_Interface30
        self.aS3_Interface34 = aS3_Interface34 if aS3_Interface34 is not None else set()
        
    @property
    def access(self) -> str:
        return self.__access

    @access.setter
    def access(self, access: str):
        self.__access = access

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def aS3_Interface30(self):
        return self.__aS3_Interface30

    @aS3_Interface30.setter
    def aS3_Interface30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Interface__aS3_Interface30", None)
        self.__aS3_Interface30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_Interface32"):
                opp_val = getattr(old_value, "aS3_Interface32", None)
                if opp_val == self:
                    setattr(old_value, "aS3_Interface32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_Interface32"):
                opp_val = getattr(value, "aS3_Interface32", None)
                setattr(value, "aS3_Interface32", self)

    @property
    def aS3_Interface32(self):
        return self.__aS3_Interface32

    @aS3_Interface32.setter
    def aS3_Interface32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Interface__aS3_Interface32", None)
        self.__aS3_Interface32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_Interface30"):
                opp_val = getattr(old_value, "aS3_Interface30", None)
                if opp_val == self:
                    setattr(old_value, "aS3_Interface30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_Interface30"):
                opp_val = getattr(value, "aS3_Interface30", None)
                setattr(value, "aS3_Interface30", self)

    @property
    def aS3_Interface34(self):
        return self.__aS3_Interface34

    @aS3_Interface34.setter
    def aS3_Interface34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Interface__aS3_Interface34", None)
        self.__aS3_Interface34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aS3_InterfaceMethod"):
                    opp_val = getattr(item, "aS3_InterfaceMethod", None)
                    
                    if opp_val == self:
                        setattr(item, "aS3_InterfaceMethod", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aS3_InterfaceMethod"):
                    opp_val = getattr(item, "aS3_InterfaceMethod", None)
                    
                    setattr(item, "aS3_InterfaceMethod", self)
                    

    @property
    def aS3_Interface62(self):
        return self.__aS3_Interface62

    @aS3_Interface62.setter
    def aS3_Interface62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Interface__aS3_Interface62", None)
        self.__aS3_Interface62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_Class61"):
                opp_val = getattr(old_value, "aS3_Class61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_Class61"):
                opp_val = getattr(value, "aS3_Class61", None)
                if opp_val is None:
                    setattr(value, "aS3_Class61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aS3_Interface(self):
        return self.__aS3_Interface

    @aS3_Interface.setter
    def aS3_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Interface__aS3_Interface", None)
        self.__aS3_Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aS3_Annotation29"):
                    opp_val = getattr(item, "aS3_Annotation29", None)
                    
                    if opp_val == self:
                        setattr(item, "aS3_Annotation29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aS3_Annotation29"):
                    opp_val = getattr(item, "aS3_Annotation29", None)
                    
                    setattr(item, "aS3_Annotation29", self)
                    

class aS3_Member:

    pass
class aS3_annotationFields:

    pass
class aS3_Annotation:

    def __init__(self, name: str, aS3_Annotation: "aS3_annotationFields" = None, aS3_Annotation29: "aS3_Interface" = None, aS3_Annotation37: "aS3_InterfaceMethod" = None, aS3_Annotation53: "aS3_Class" = None, aS3_Annotation90: "aS3_MemberVariableDeclaration" = None, aS3_Annotation71: "aS3_Method" = None):
        self.name = name
        self.aS3_Annotation = aS3_Annotation
        self.aS3_Annotation29 = aS3_Annotation29
        self.aS3_Annotation37 = aS3_Annotation37
        self.aS3_Annotation53 = aS3_Annotation53
        self.aS3_Annotation90 = aS3_Annotation90
        self.aS3_Annotation71 = aS3_Annotation71
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def aS3_Annotation71(self):
        return self.__aS3_Annotation71

    @aS3_Annotation71.setter
    def aS3_Annotation71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Annotation__aS3_Annotation71", None)
        self.__aS3_Annotation71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_Method70"):
                opp_val = getattr(old_value, "aS3_Method70", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_Method70"):
                opp_val = getattr(value, "aS3_Method70", None)
                if opp_val is None:
                    setattr(value, "aS3_Method70", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aS3_Annotation29(self):
        return self.__aS3_Annotation29

    @aS3_Annotation29.setter
    def aS3_Annotation29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Annotation__aS3_Annotation29", None)
        self.__aS3_Annotation29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_Interface"):
                opp_val = getattr(old_value, "aS3_Interface", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_Interface"):
                opp_val = getattr(value, "aS3_Interface", None)
                if opp_val is None:
                    setattr(value, "aS3_Interface", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aS3_Annotation90(self):
        return self.__aS3_Annotation90

    @aS3_Annotation90.setter
    def aS3_Annotation90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Annotation__aS3_Annotation90", None)
        self.__aS3_Annotation90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_MemberVariableDeclaration89"):
                opp_val = getattr(old_value, "aS3_MemberVariableDeclaration89", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_MemberVariableDeclaration89"):
                opp_val = getattr(value, "aS3_MemberVariableDeclaration89", None)
                if opp_val is None:
                    setattr(value, "aS3_MemberVariableDeclaration89", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aS3_Annotation37(self):
        return self.__aS3_Annotation37

    @aS3_Annotation37.setter
    def aS3_Annotation37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Annotation__aS3_Annotation37", None)
        self.__aS3_Annotation37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_InterfaceMethod36"):
                opp_val = getattr(old_value, "aS3_InterfaceMethod36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_InterfaceMethod36"):
                opp_val = getattr(value, "aS3_InterfaceMethod36", None)
                if opp_val is None:
                    setattr(value, "aS3_InterfaceMethod36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aS3_Annotation53(self):
        return self.__aS3_Annotation53

    @aS3_Annotation53.setter
    def aS3_Annotation53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Annotation__aS3_Annotation53", None)
        self.__aS3_Annotation53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_Class"):
                opp_val = getattr(old_value, "aS3_Class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_Class"):
                opp_val = getattr(value, "aS3_Class", None)
                if opp_val is None:
                    setattr(value, "aS3_Class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aS3_Annotation(self):
        return self.__aS3_Annotation

    @aS3_Annotation.setter
    def aS3_Annotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Annotation__aS3_Annotation", None)
        self.__aS3_Annotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_annotationFields"):
                opp_val = getattr(old_value, "aS3_annotationFields", None)
                if opp_val == self:
                    setattr(old_value, "aS3_annotationFields", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_annotationFields"):
                opp_val = getattr(value, "aS3_annotationFields", None)
                setattr(value, "aS3_annotationFields", self)

class aS3_Uses:

    def __init__(self, anytype: str, type: str, aS3_Uses: "aS3_directive" = None):
        self.anytype = anytype
        self.type = type
        self.aS3_Uses = aS3_Uses
        
    @property
    def anytype(self) -> str:
        return self.__anytype

    @anytype.setter
    def anytype(self, anytype: str):
        self.__anytype = anytype

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def aS3_Uses(self):
        return self.__aS3_Uses

    @aS3_Uses.setter
    def aS3_Uses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Uses__aS3_Uses", None)
        self.__aS3_Uses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_directive22"):
                opp_val = getattr(old_value, "aS3_directive22", None)
                if opp_val == self:
                    setattr(old_value, "aS3_directive22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_directive22"):
                opp_val = getattr(value, "aS3_directive22", None)
                setattr(value, "aS3_directive22", self)

class aS3_Import:

    def __init__(self, importedNamespace: str, aS3_Import: "aS3_Imports" = None):
        self.importedNamespace = importedNamespace
        self.aS3_Import = aS3_Import
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

    @property
    def aS3_Import(self):
        return self.__aS3_Import

    @aS3_Import.setter
    def aS3_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Import__aS3_Import", None)
        self.__aS3_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_Imports20"):
                opp_val = getattr(old_value, "aS3_Imports20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_Imports20"):
                opp_val = getattr(value, "aS3_Imports20", None)
                if opp_val is None:
                    setattr(value, "aS3_Imports20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aS3_directive:

    pass
class aS3_EObject:

    pass
class aS3_Imports:

    pass
class aS3_Package:

    def __init__(self, name: str, aS3_Package: "aS3_Model" = None, aS3_Package9: "aS3_Imports" = None, aS3_Package12: set["aS3_directive"] = None, aS3_Package14: set["aS3_EObject"] = None, aS3_Package17: set["aS3_EObject"] = None):
        self.name = name
        self.aS3_Package = aS3_Package
        self.aS3_Package9 = aS3_Package9
        self.aS3_Package12 = aS3_Package12 if aS3_Package12 is not None else set()
        self.aS3_Package14 = aS3_Package14 if aS3_Package14 is not None else set()
        self.aS3_Package17 = aS3_Package17 if aS3_Package17 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def aS3_Package9(self):
        return self.__aS3_Package9

    @aS3_Package9.setter
    def aS3_Package9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Package__aS3_Package9", None)
        self.__aS3_Package9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_Imports10"):
                opp_val = getattr(old_value, "aS3_Imports10", None)
                if opp_val == self:
                    setattr(old_value, "aS3_Imports10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_Imports10"):
                opp_val = getattr(value, "aS3_Imports10", None)
                setattr(value, "aS3_Imports10", self)

    @property
    def aS3_Package(self):
        return self.__aS3_Package

    @aS3_Package.setter
    def aS3_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Package__aS3_Package", None)
        self.__aS3_Package = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_Model"):
                opp_val = getattr(old_value, "aS3_Model", None)
                if opp_val == self:
                    setattr(old_value, "aS3_Model", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_Model"):
                opp_val = getattr(value, "aS3_Model", None)
                setattr(value, "aS3_Model", self)

    @property
    def aS3_Package12(self):
        return self.__aS3_Package12

    @aS3_Package12.setter
    def aS3_Package12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Package__aS3_Package12", None)
        self.__aS3_Package12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aS3_directive"):
                    opp_val = getattr(item, "aS3_directive", None)
                    
                    if opp_val == self:
                        setattr(item, "aS3_directive", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aS3_directive"):
                    opp_val = getattr(item, "aS3_directive", None)
                    
                    setattr(item, "aS3_directive", self)
                    

    @property
    def aS3_Package14(self):
        return self.__aS3_Package14

    @aS3_Package14.setter
    def aS3_Package14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Package__aS3_Package14", None)
        self.__aS3_Package14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aS3_EObject15"):
                    opp_val = getattr(item, "aS3_EObject15", None)
                    
                    if opp_val == self:
                        setattr(item, "aS3_EObject15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aS3_EObject15"):
                    opp_val = getattr(item, "aS3_EObject15", None)
                    
                    setattr(item, "aS3_EObject15", self)
                    

    @property
    def aS3_Package17(self):
        return self.__aS3_Package17

    @aS3_Package17.setter
    def aS3_Package17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_Package__aS3_Package17", None)
        self.__aS3_Package17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aS3_EObject18"):
                    opp_val = getattr(item, "aS3_EObject18", None)
                    
                    if opp_val == self:
                        setattr(item, "aS3_EObject18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aS3_EObject18"):
                    opp_val = getattr(item, "aS3_EObject18", None)
                    
                    setattr(item, "aS3_EObject18", self)
                    

class aS3_Model:

    pass
class aS3_Expression(ThrowStatement, exprOrObjectLiteral, DefaultXMLNamespaceStatement, Condition, CaseStatement):

    pass
class aS3_annotationField:

    def __init__(self, name: str, aS3_annotationField: "aS3_annotationFields" = None, aS3_annotationField27: "aS3_Expression" = None):
        self.name = name
        self.aS3_annotationField = aS3_annotationField
        self.aS3_annotationField27 = aS3_annotationField27
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def aS3_annotationField(self):
        return self.__aS3_annotationField

    @aS3_annotationField.setter
    def aS3_annotationField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_annotationField__aS3_annotationField", None)
        self.__aS3_annotationField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_annotationFields25"):
                opp_val = getattr(old_value, "aS3_annotationFields25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_annotationFields25"):
                opp_val = getattr(value, "aS3_annotationFields25", None)
                if opp_val is None:
                    setattr(value, "aS3_annotationFields25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aS3_annotationField27(self):
        return self.__aS3_annotationField27

    @aS3_annotationField27.setter
    def aS3_annotationField27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aS3_annotationField__aS3_annotationField27", None)
        self.__aS3_annotationField27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aS3_Expression"):
                opp_val = getattr(old_value, "aS3_Expression", None)
                if opp_val == self:
                    setattr(old_value, "aS3_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aS3_Expression"):
                opp_val = getattr(value, "aS3_Expression", None)
                setattr(value, "aS3_Expression", self)
