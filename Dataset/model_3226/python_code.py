from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class pascal_caseListElement:

    pass
class pascal_caseStatement:

    pass
class pascal_statements:

    pass
class pascal_conditionalStatement:

    pass
class parameterList:

    pass
class pascal_actualParameter(parameterList):

    pass
class pascal_functionDesignator:

    pass
class pascal_unsignedConstant:

    def __init__(self, string_literal: str, pascal_unsignedConstant: "pascal_factor" = None, pascal_unsignedConstant285: "pascal_unsignedNumber" = None, pascal_unsignedConstant288: "pascal_constantChr" = None):
        self.string_literal = string_literal
        self.pascal_unsignedConstant = pascal_unsignedConstant
        self.pascal_unsignedConstant285 = pascal_unsignedConstant285
        self.pascal_unsignedConstant288 = pascal_unsignedConstant288
        
    @property
    def string_literal(self) -> str:
        return self.__string_literal

    @string_literal.setter
    def string_literal(self, string_literal: str):
        self.__string_literal = string_literal

    @property
    def pascal_unsignedConstant(self):
        return self.__pascal_unsignedConstant

    @pascal_unsignedConstant.setter
    def pascal_unsignedConstant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_unsignedConstant__pascal_unsignedConstant", None)
        self.__pascal_unsignedConstant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_factor275"):
                opp_val = getattr(old_value, "pascal_factor275", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor275", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor275"):
                opp_val = getattr(value, "pascal_factor275", None)
                setattr(value, "pascal_factor275", self)

    @property
    def pascal_unsignedConstant285(self):
        return self.__pascal_unsignedConstant285

    @pascal_unsignedConstant285.setter
    def pascal_unsignedConstant285(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_unsignedConstant__pascal_unsignedConstant285", None)
        self.__pascal_unsignedConstant285 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_unsignedNumber286"):
                opp_val = getattr(old_value, "pascal_unsignedNumber286", None)
                if opp_val == self:
                    setattr(old_value, "pascal_unsignedNumber286", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_unsignedNumber286"):
                opp_val = getattr(value, "pascal_unsignedNumber286", None)
                setattr(value, "pascal_unsignedNumber286", self)

    @property
    def pascal_unsignedConstant288(self):
        return self.__pascal_unsignedConstant288

    @pascal_unsignedConstant288.setter
    def pascal_unsignedConstant288(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_unsignedConstant__pascal_unsignedConstant288", None)
        self.__pascal_unsignedConstant288 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_constantChr289"):
                opp_val = getattr(old_value, "pascal_constantChr289", None)
                if opp_val == self:
                    setattr(old_value, "pascal_constantChr289", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_constantChr289"):
                opp_val = getattr(value, "pascal_constantChr289", None)
                setattr(value, "pascal_constantChr289", self)

class pascal_factor:

    def __init__(self, bool: str, pascal_factor: "pascal_signedFactor" = None, pascal_factor272: "pascal_expression" = None, pascal_factor275: "pascal_unsignedConstant" = None, pascal_factor278: "pascal_factor" = None, pascal_factor276: "pascal_factor" = None, pascal_factor280: "pascal_functionDesignator" = None, pascal_factor282: "pascal_variable" = None):
        self.bool = bool
        self.pascal_factor = pascal_factor
        self.pascal_factor272 = pascal_factor272
        self.pascal_factor275 = pascal_factor275
        self.pascal_factor278 = pascal_factor278
        self.pascal_factor276 = pascal_factor276
        self.pascal_factor280 = pascal_factor280
        self.pascal_factor282 = pascal_factor282
        
    @property
    def bool(self) -> str:
        return self.__bool

    @bool.setter
    def bool(self, bool: str):
        self.__bool = bool

    @property
    def pascal_factor282(self):
        return self.__pascal_factor282

    @pascal_factor282.setter
    def pascal_factor282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor282", None)
        self.__pascal_factor282 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_variable283"):
                opp_val = getattr(old_value, "pascal_variable283", None)
                if opp_val == self:
                    setattr(old_value, "pascal_variable283", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_variable283"):
                opp_val = getattr(value, "pascal_variable283", None)
                setattr(value, "pascal_variable283", self)

    @property
    def pascal_factor280(self):
        return self.__pascal_factor280

    @pascal_factor280.setter
    def pascal_factor280(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor280", None)
        self.__pascal_factor280 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_functionDesignator"):
                opp_val = getattr(old_value, "pascal_functionDesignator", None)
                if opp_val == self:
                    setattr(old_value, "pascal_functionDesignator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_functionDesignator"):
                opp_val = getattr(value, "pascal_functionDesignator", None)
                setattr(value, "pascal_functionDesignator", self)

    @property
    def pascal_factor276(self):
        return self.__pascal_factor276

    @pascal_factor276.setter
    def pascal_factor276(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor276", None)
        self.__pascal_factor276 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_factor278"):
                opp_val = getattr(old_value, "pascal_factor278", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor278", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor278"):
                opp_val = getattr(value, "pascal_factor278", None)
                setattr(value, "pascal_factor278", self)

    @property
    def pascal_factor275(self):
        return self.__pascal_factor275

    @pascal_factor275.setter
    def pascal_factor275(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor275", None)
        self.__pascal_factor275 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_unsignedConstant"):
                opp_val = getattr(old_value, "pascal_unsignedConstant", None)
                if opp_val == self:
                    setattr(old_value, "pascal_unsignedConstant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_unsignedConstant"):
                opp_val = getattr(value, "pascal_unsignedConstant", None)
                setattr(value, "pascal_unsignedConstant", self)

    @property
    def pascal_factor278(self):
        return self.__pascal_factor278

    @pascal_factor278.setter
    def pascal_factor278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor278", None)
        self.__pascal_factor278 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_factor276"):
                opp_val = getattr(old_value, "pascal_factor276", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor276", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor276"):
                opp_val = getattr(value, "pascal_factor276", None)
                setattr(value, "pascal_factor276", self)

    @property
    def pascal_factor(self):
        return self.__pascal_factor

    @pascal_factor.setter
    def pascal_factor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor", None)
        self.__pascal_factor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_signedFactor270"):
                opp_val = getattr(old_value, "pascal_signedFactor270", None)
                if opp_val == self:
                    setattr(old_value, "pascal_signedFactor270", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_signedFactor270"):
                opp_val = getattr(value, "pascal_signedFactor270", None)
                setattr(value, "pascal_signedFactor270", self)

    @property
    def pascal_factor272(self):
        return self.__pascal_factor272

    @pascal_factor272.setter
    def pascal_factor272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor272", None)
        self.__pascal_factor272 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_expression273"):
                opp_val = getattr(old_value, "pascal_expression273", None)
                if opp_val == self:
                    setattr(old_value, "pascal_expression273", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression273"):
                opp_val = getattr(value, "pascal_expression273", None)
                setattr(value, "pascal_expression273", self)

class pascal_signedFactor:

    pass
class pascal_term:

    def __init__(self, multiplicativeoperator: str, pascal_term: "pascal_simpleExpression" = None, pascal_term265: "pascal_signedFactor" = None, pascal_term268: "pascal_term" = None, pascal_term266: "pascal_term" = None):
        self.multiplicativeoperator = multiplicativeoperator
        self.pascal_term = pascal_term
        self.pascal_term265 = pascal_term265
        self.pascal_term268 = pascal_term268
        self.pascal_term266 = pascal_term266
        
    @property
    def multiplicativeoperator(self) -> str:
        return self.__multiplicativeoperator

    @multiplicativeoperator.setter
    def multiplicativeoperator(self, multiplicativeoperator: str):
        self.__multiplicativeoperator = multiplicativeoperator

    @property
    def pascal_term268(self):
        return self.__pascal_term268

    @pascal_term268.setter
    def pascal_term268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_term__pascal_term268", None)
        self.__pascal_term268 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_term266"):
                opp_val = getattr(old_value, "pascal_term266", None)
                if opp_val == self:
                    setattr(old_value, "pascal_term266", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_term266"):
                opp_val = getattr(value, "pascal_term266", None)
                setattr(value, "pascal_term266", self)

    @property
    def pascal_term266(self):
        return self.__pascal_term266

    @pascal_term266.setter
    def pascal_term266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_term__pascal_term266", None)
        self.__pascal_term266 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_term268"):
                opp_val = getattr(old_value, "pascal_term268", None)
                if opp_val == self:
                    setattr(old_value, "pascal_term268", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_term268"):
                opp_val = getattr(value, "pascal_term268", None)
                setattr(value, "pascal_term268", self)

    @property
    def pascal_term(self):
        return self.__pascal_term

    @pascal_term.setter
    def pascal_term(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_term__pascal_term", None)
        self.__pascal_term = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_simpleExpression260"):
                opp_val = getattr(old_value, "pascal_simpleExpression260", None)
                if opp_val == self:
                    setattr(old_value, "pascal_simpleExpression260", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_simpleExpression260"):
                opp_val = getattr(value, "pascal_simpleExpression260", None)
                setattr(value, "pascal_simpleExpression260", self)

    @property
    def pascal_term265(self):
        return self.__pascal_term265

    @pascal_term265.setter
    def pascal_term265(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_term__pascal_term265", None)
        self.__pascal_term265 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_signedFactor"):
                opp_val = getattr(old_value, "pascal_signedFactor", None)
                if opp_val == self:
                    setattr(old_value, "pascal_signedFactor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_signedFactor"):
                opp_val = getattr(value, "pascal_signedFactor", None)
                setattr(value, "pascal_signedFactor", self)

class pascal_simpleExpression:

    def __init__(self, additiveoperator: str, pascal_simpleExpression: "pascal_expression" = None, pascal_simpleExpression260: "pascal_term" = None, pascal_simpleExpression263: "pascal_simpleExpression" = None, pascal_simpleExpression261: "pascal_simpleExpression" = None):
        self.additiveoperator = additiveoperator
        self.pascal_simpleExpression = pascal_simpleExpression
        self.pascal_simpleExpression260 = pascal_simpleExpression260
        self.pascal_simpleExpression263 = pascal_simpleExpression263
        self.pascal_simpleExpression261 = pascal_simpleExpression261
        
    @property
    def additiveoperator(self) -> str:
        return self.__additiveoperator

    @additiveoperator.setter
    def additiveoperator(self, additiveoperator: str):
        self.__additiveoperator = additiveoperator

    @property
    def pascal_simpleExpression263(self):
        return self.__pascal_simpleExpression263

    @pascal_simpleExpression263.setter
    def pascal_simpleExpression263(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simpleExpression__pascal_simpleExpression263", None)
        self.__pascal_simpleExpression263 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_simpleExpression261"):
                opp_val = getattr(old_value, "pascal_simpleExpression261", None)
                if opp_val == self:
                    setattr(old_value, "pascal_simpleExpression261", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_simpleExpression261"):
                opp_val = getattr(value, "pascal_simpleExpression261", None)
                setattr(value, "pascal_simpleExpression261", self)

    @property
    def pascal_simpleExpression260(self):
        return self.__pascal_simpleExpression260

    @pascal_simpleExpression260.setter
    def pascal_simpleExpression260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simpleExpression__pascal_simpleExpression260", None)
        self.__pascal_simpleExpression260 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_term"):
                opp_val = getattr(old_value, "pascal_term", None)
                if opp_val == self:
                    setattr(old_value, "pascal_term", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_term"):
                opp_val = getattr(value, "pascal_term", None)
                setattr(value, "pascal_term", self)

    @property
    def pascal_simpleExpression261(self):
        return self.__pascal_simpleExpression261

    @pascal_simpleExpression261.setter
    def pascal_simpleExpression261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simpleExpression__pascal_simpleExpression261", None)
        self.__pascal_simpleExpression261 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_simpleExpression263"):
                opp_val = getattr(old_value, "pascal_simpleExpression263", None)
                if opp_val == self:
                    setattr(old_value, "pascal_simpleExpression263", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_simpleExpression263"):
                opp_val = getattr(value, "pascal_simpleExpression263", None)
                setattr(value, "pascal_simpleExpression263", self)

    @property
    def pascal_simpleExpression(self):
        return self.__pascal_simpleExpression

    @pascal_simpleExpression.setter
    def pascal_simpleExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simpleExpression__pascal_simpleExpression", None)
        self.__pascal_simpleExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_expression255"):
                opp_val = getattr(old_value, "pascal_expression255", None)
                if opp_val == self:
                    setattr(old_value, "pascal_expression255", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression255"):
                opp_val = getattr(value, "pascal_expression255", None)
                setattr(value, "pascal_expression255", self)

class pascal_variable:

    pass
class pascal_assignmentStatement:

    pass
class pascal_gotoStatement:

    pass
class pascal_parameterList:

    pass
class pascal_structuredStatement:

    pass
class pascal_simpleStatement:

    pass
class pascal_unlabelledStatement:

    pass
class pascal_statement:

    pass
class pascal_functionDeclaration:

    pass
class pascal_procedureDeclaration:

    pass
class pascal_procedureOrFunctionDeclaration:

    pass
class pascal_expression:

    def __init__(self, relationaloperator: str, pascal_expression: "pascal_variableDeclaration" = None, pascal_expression250: "pascal_assignmentStatement" = None, pascal_expression255: "pascal_simpleExpression" = None, pascal_expression258: "pascal_expression" = None, pascal_expression256: "pascal_expression" = None, pascal_expression273: "pascal_factor" = None, pascal_expression300: "pascal_actualParameter" = None, pascal_expression318: "pascal_caseStatement" = None):
        self.relationaloperator = relationaloperator
        self.pascal_expression = pascal_expression
        self.pascal_expression250 = pascal_expression250
        self.pascal_expression255 = pascal_expression255
        self.pascal_expression258 = pascal_expression258
        self.pascal_expression256 = pascal_expression256
        self.pascal_expression273 = pascal_expression273
        self.pascal_expression300 = pascal_expression300
        self.pascal_expression318 = pascal_expression318
        
    @property
    def relationaloperator(self) -> str:
        return self.__relationaloperator

    @relationaloperator.setter
    def relationaloperator(self, relationaloperator: str):
        self.__relationaloperator = relationaloperator

    @property
    def pascal_expression255(self):
        return self.__pascal_expression255

    @pascal_expression255.setter
    def pascal_expression255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression255", None)
        self.__pascal_expression255 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_simpleExpression"):
                opp_val = getattr(old_value, "pascal_simpleExpression", None)
                if opp_val == self:
                    setattr(old_value, "pascal_simpleExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_simpleExpression"):
                opp_val = getattr(value, "pascal_simpleExpression", None)
                setattr(value, "pascal_simpleExpression", self)

    @property
    def pascal_expression258(self):
        return self.__pascal_expression258

    @pascal_expression258.setter
    def pascal_expression258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression258", None)
        self.__pascal_expression258 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_expression256"):
                opp_val = getattr(old_value, "pascal_expression256", None)
                if opp_val == self:
                    setattr(old_value, "pascal_expression256", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression256"):
                opp_val = getattr(value, "pascal_expression256", None)
                setattr(value, "pascal_expression256", self)

    @property
    def pascal_expression256(self):
        return self.__pascal_expression256

    @pascal_expression256.setter
    def pascal_expression256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression256", None)
        self.__pascal_expression256 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_expression258"):
                opp_val = getattr(old_value, "pascal_expression258", None)
                if opp_val == self:
                    setattr(old_value, "pascal_expression258", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression258"):
                opp_val = getattr(value, "pascal_expression258", None)
                setattr(value, "pascal_expression258", self)

    @property
    def pascal_expression300(self):
        return self.__pascal_expression300

    @pascal_expression300.setter
    def pascal_expression300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression300", None)
        self.__pascal_expression300 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_actualParameter299"):
                opp_val = getattr(old_value, "pascal_actualParameter299", None)
                if opp_val == self:
                    setattr(old_value, "pascal_actualParameter299", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_actualParameter299"):
                opp_val = getattr(value, "pascal_actualParameter299", None)
                setattr(value, "pascal_actualParameter299", self)

    @property
    def pascal_expression(self):
        return self.__pascal_expression

    @pascal_expression.setter
    def pascal_expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression", None)
        self.__pascal_expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_variableDeclaration204"):
                opp_val = getattr(old_value, "pascal_variableDeclaration204", None)
                if opp_val == self:
                    setattr(old_value, "pascal_variableDeclaration204", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_variableDeclaration204"):
                opp_val = getattr(value, "pascal_variableDeclaration204", None)
                setattr(value, "pascal_variableDeclaration204", self)

    @property
    def pascal_expression273(self):
        return self.__pascal_expression273

    @pascal_expression273.setter
    def pascal_expression273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression273", None)
        self.__pascal_expression273 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_factor272"):
                opp_val = getattr(old_value, "pascal_factor272", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor272", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor272"):
                opp_val = getattr(value, "pascal_factor272", None)
                setattr(value, "pascal_factor272", self)

    @property
    def pascal_expression250(self):
        return self.__pascal_expression250

    @pascal_expression250.setter
    def pascal_expression250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression250", None)
        self.__pascal_expression250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_assignmentStatement249"):
                opp_val = getattr(old_value, "pascal_assignmentStatement249", None)
                if opp_val == self:
                    setattr(old_value, "pascal_assignmentStatement249", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_assignmentStatement249"):
                opp_val = getattr(value, "pascal_assignmentStatement249", None)
                setattr(value, "pascal_assignmentStatement249", self)

    @property
    def pascal_expression318(self):
        return self.__pascal_expression318

    @pascal_expression318.setter
    def pascal_expression318(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression318", None)
        self.__pascal_expression318 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_caseStatement317"):
                opp_val = getattr(old_value, "pascal_caseStatement317", None)
                if opp_val == self:
                    setattr(old_value, "pascal_caseStatement317", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_caseStatement317"):
                opp_val = getattr(value, "pascal_caseStatement317", None)
                setattr(value, "pascal_caseStatement317", self)

class pascal_variableDeclaration:

    pass
class pascal_constList:

    pass
class pascal_variant:

    pass
class pascal_tag:

    pass
class pascal_recordSection:

    pass
class pascal_variantPart:

    pass
class pascal_fixedPart:

    pass
class pascal_recordType:

    pass
class pascal_unpackedStructuredType:

    pass
class pascal_stringtype:

    pass
class pascal_subrangeType:

    pass
class pascal_scalarType:

    pass
class pascal_pointerType:

    pass
class pascal_structuredType:

    pass
class pascal_simpleType:

    pass
class pascal_formalParameterSection:

    pass
class pascal_parameterGroup:

    pass
class pascal_typeIdentifier:

    def __init__(self, char: str, boolean: str, integer: str, real: str, string: str, pascal_typeIdentifier: "pascal_functionType" = None, pascal_typeIdentifier105: "pascal_identifier" = None, pascal_typeIdentifier118: "pascal_pointerType" = None, pascal_typeIdentifier125: "pascal_simpleType" = None, pascal_typeIdentifier103: "pascal_parameterGroup" = None, pascal_typeIdentifier183: "pascal_tag" = None, pascal_typeIdentifier186: "pascal_tag" = None, pascal_typeIdentifier228: "pascal_functionDeclaration" = None):
        self.char = char
        self.boolean = boolean
        self.integer = integer
        self.real = real
        self.string = string
        self.pascal_typeIdentifier = pascal_typeIdentifier
        self.pascal_typeIdentifier105 = pascal_typeIdentifier105
        self.pascal_typeIdentifier118 = pascal_typeIdentifier118
        self.pascal_typeIdentifier125 = pascal_typeIdentifier125
        self.pascal_typeIdentifier103 = pascal_typeIdentifier103
        self.pascal_typeIdentifier183 = pascal_typeIdentifier183
        self.pascal_typeIdentifier186 = pascal_typeIdentifier186
        self.pascal_typeIdentifier228 = pascal_typeIdentifier228
        
    @property
    def string(self) -> str:
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string

    @property
    def char(self) -> str:
        return self.__char

    @char.setter
    def char(self, char: str):
        self.__char = char

    @property
    def integer(self) -> str:
        return self.__integer

    @integer.setter
    def integer(self, integer: str):
        self.__integer = integer

    @property
    def real(self) -> str:
        return self.__real

    @real.setter
    def real(self, real: str):
        self.__real = real

    @property
    def boolean(self) -> str:
        return self.__boolean

    @boolean.setter
    def boolean(self, boolean: str):
        self.__boolean = boolean

    @property
    def pascal_typeIdentifier183(self):
        return self.__pascal_typeIdentifier183

    @pascal_typeIdentifier183.setter
    def pascal_typeIdentifier183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_typeIdentifier__pascal_typeIdentifier183", None)
        self.__pascal_typeIdentifier183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_tag182"):
                opp_val = getattr(old_value, "pascal_tag182", None)
                if opp_val == self:
                    setattr(old_value, "pascal_tag182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_tag182"):
                opp_val = getattr(value, "pascal_tag182", None)
                setattr(value, "pascal_tag182", self)

    @property
    def pascal_typeIdentifier118(self):
        return self.__pascal_typeIdentifier118

    @pascal_typeIdentifier118.setter
    def pascal_typeIdentifier118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_typeIdentifier__pascal_typeIdentifier118", None)
        self.__pascal_typeIdentifier118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_pointerType117"):
                opp_val = getattr(old_value, "pascal_pointerType117", None)
                if opp_val == self:
                    setattr(old_value, "pascal_pointerType117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_pointerType117"):
                opp_val = getattr(value, "pascal_pointerType117", None)
                setattr(value, "pascal_pointerType117", self)

    @property
    def pascal_typeIdentifier125(self):
        return self.__pascal_typeIdentifier125

    @pascal_typeIdentifier125.setter
    def pascal_typeIdentifier125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_typeIdentifier__pascal_typeIdentifier125", None)
        self.__pascal_typeIdentifier125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_simpleType124"):
                opp_val = getattr(old_value, "pascal_simpleType124", None)
                if opp_val == self:
                    setattr(old_value, "pascal_simpleType124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_simpleType124"):
                opp_val = getattr(value, "pascal_simpleType124", None)
                setattr(value, "pascal_simpleType124", self)

    @property
    def pascal_typeIdentifier103(self):
        return self.__pascal_typeIdentifier103

    @pascal_typeIdentifier103.setter
    def pascal_typeIdentifier103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_typeIdentifier__pascal_typeIdentifier103", None)
        self.__pascal_typeIdentifier103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_parameterGroup102"):
                opp_val = getattr(old_value, "pascal_parameterGroup102", None)
                if opp_val == self:
                    setattr(old_value, "pascal_parameterGroup102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_parameterGroup102"):
                opp_val = getattr(value, "pascal_parameterGroup102", None)
                setattr(value, "pascal_parameterGroup102", self)

    @property
    def pascal_typeIdentifier186(self):
        return self.__pascal_typeIdentifier186

    @pascal_typeIdentifier186.setter
    def pascal_typeIdentifier186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_typeIdentifier__pascal_typeIdentifier186", None)
        self.__pascal_typeIdentifier186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_tag185"):
                opp_val = getattr(old_value, "pascal_tag185", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_tag185"):
                opp_val = getattr(value, "pascal_tag185", None)
                if opp_val is None:
                    setattr(value, "pascal_tag185", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_typeIdentifier228(self):
        return self.__pascal_typeIdentifier228

    @pascal_typeIdentifier228.setter
    def pascal_typeIdentifier228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_typeIdentifier__pascal_typeIdentifier228", None)
        self.__pascal_typeIdentifier228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_functionDeclaration227"):
                opp_val = getattr(old_value, "pascal_functionDeclaration227", None)
                if opp_val == self:
                    setattr(old_value, "pascal_functionDeclaration227", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_functionDeclaration227"):
                opp_val = getattr(value, "pascal_functionDeclaration227", None)
                setattr(value, "pascal_functionDeclaration227", self)

    @property
    def pascal_typeIdentifier(self):
        return self.__pascal_typeIdentifier

    @pascal_typeIdentifier.setter
    def pascal_typeIdentifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_typeIdentifier__pascal_typeIdentifier", None)
        self.__pascal_typeIdentifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_functionType81"):
                opp_val = getattr(old_value, "pascal_functionType81", None)
                if opp_val == self:
                    setattr(old_value, "pascal_functionType81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_functionType81"):
                opp_val = getattr(value, "pascal_functionType81", None)
                setattr(value, "pascal_functionType81", self)

    @property
    def pascal_typeIdentifier105(self):
        return self.__pascal_typeIdentifier105

    @pascal_typeIdentifier105.setter
    def pascal_typeIdentifier105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_typeIdentifier__pascal_typeIdentifier105", None)
        self.__pascal_typeIdentifier105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_identifier106"):
                opp_val = getattr(old_value, "pascal_identifier106", None)
                if opp_val == self:
                    setattr(old_value, "pascal_identifier106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_identifier106"):
                opp_val = getattr(value, "pascal_identifier106", None)
                setattr(value, "pascal_identifier106", self)

class pascal_formalParameterList:

    pass
class pascal_procedureType:

    pass
class pascal_functionType:

    pass
class pascal_type:

    pass
class pascal_typeDefinition:

    pass
class pascal_fieldList:

    pass
class pascal_constantChr:

    pass
class pascal_unsignedNumber:

    def __init__(self, unsignedReal: str, pascal_unsignedNumber: "pascal_constant" = None, pascal_unsignedNumber59: "pascal_unsignedInteger" = None, pascal_unsignedNumber149: "pascal_stringtype" = None, pascal_unsignedNumber286: "pascal_unsignedConstant" = None):
        self.unsignedReal = unsignedReal
        self.pascal_unsignedNumber = pascal_unsignedNumber
        self.pascal_unsignedNumber59 = pascal_unsignedNumber59
        self.pascal_unsignedNumber149 = pascal_unsignedNumber149
        self.pascal_unsignedNumber286 = pascal_unsignedNumber286
        
    @property
    def unsignedReal(self) -> str:
        return self.__unsignedReal

    @unsignedReal.setter
    def unsignedReal(self, unsignedReal: str):
        self.__unsignedReal = unsignedReal

    @property
    def pascal_unsignedNumber286(self):
        return self.__pascal_unsignedNumber286

    @pascal_unsignedNumber286.setter
    def pascal_unsignedNumber286(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_unsignedNumber__pascal_unsignedNumber286", None)
        self.__pascal_unsignedNumber286 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_unsignedConstant285"):
                opp_val = getattr(old_value, "pascal_unsignedConstant285", None)
                if opp_val == self:
                    setattr(old_value, "pascal_unsignedConstant285", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_unsignedConstant285"):
                opp_val = getattr(value, "pascal_unsignedConstant285", None)
                setattr(value, "pascal_unsignedConstant285", self)

    @property
    def pascal_unsignedNumber149(self):
        return self.__pascal_unsignedNumber149

    @pascal_unsignedNumber149.setter
    def pascal_unsignedNumber149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_unsignedNumber__pascal_unsignedNumber149", None)
        self.__pascal_unsignedNumber149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_stringtype148"):
                opp_val = getattr(old_value, "pascal_stringtype148", None)
                if opp_val == self:
                    setattr(old_value, "pascal_stringtype148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_stringtype148"):
                opp_val = getattr(value, "pascal_stringtype148", None)
                setattr(value, "pascal_stringtype148", self)

    @property
    def pascal_unsignedNumber(self):
        return self.__pascal_unsignedNumber

    @pascal_unsignedNumber.setter
    def pascal_unsignedNumber(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_unsignedNumber__pascal_unsignedNumber", None)
        self.__pascal_unsignedNumber = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_constant44"):
                opp_val = getattr(old_value, "pascal_constant44", None)
                if opp_val == self:
                    setattr(old_value, "pascal_constant44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_constant44"):
                opp_val = getattr(value, "pascal_constant44", None)
                setattr(value, "pascal_constant44", self)

    @property
    def pascal_unsignedNumber59(self):
        return self.__pascal_unsignedNumber59

    @pascal_unsignedNumber59.setter
    def pascal_unsignedNumber59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_unsignedNumber__pascal_unsignedNumber59", None)
        self.__pascal_unsignedNumber59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_unsignedInteger60"):
                opp_val = getattr(old_value, "pascal_unsignedInteger60", None)
                if opp_val == self:
                    setattr(old_value, "pascal_unsignedInteger60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_unsignedInteger60"):
                opp_val = getattr(value, "pascal_unsignedInteger60", None)
                setattr(value, "pascal_unsignedInteger60", self)

class variant:

    pass
class pascal_constant(variant):

    def __init__(self, sign: str, string: str, bool: str, pascal_constant: "pascal_constantDefinition" = None, pascal_constant44: "pascal_unsignedNumber" = None, pascal_constant46: "pascal_identifier" = None, pascal_constant49: "pascal_constantChr" = None, pascal_constant52: "pascal_constant" = None, pascal_constant50: set["pascal_constant"] = None, pascal_constant54: "pascal_fieldList" = None, pascal_constant136: "pascal_subrangeType" = None, pascal_constant133: "pascal_subrangeType" = None, pascal_constant188: "pascal_constList" = None, pascal_constant191: "pascal_constList" = None):
        self.sign = sign
        self.string = string
        self.bool = bool
        self.pascal_constant = pascal_constant
        self.pascal_constant44 = pascal_constant44
        self.pascal_constant46 = pascal_constant46
        self.pascal_constant49 = pascal_constant49
        self.pascal_constant52 = pascal_constant52
        self.pascal_constant50 = pascal_constant50 if pascal_constant50 is not None else set()
        self.pascal_constant54 = pascal_constant54
        self.pascal_constant136 = pascal_constant136
        self.pascal_constant133 = pascal_constant133
        self.pascal_constant188 = pascal_constant188
        self.pascal_constant191 = pascal_constant191
        
    @property
    def string(self) -> str:
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string

    @property
    def bool(self) -> str:
        return self.__bool

    @bool.setter
    def bool(self, bool: str):
        self.__bool = bool

    @property
    def sign(self) -> str:
        return self.__sign

    @sign.setter
    def sign(self, sign: str):
        self.__sign = sign

    @property
    def pascal_constant50(self):
        return self.__pascal_constant50

    @pascal_constant50.setter
    def pascal_constant50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant50", None)
        self.__pascal_constant50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pascal_constant52"):
                    opp_val = getattr(item, "pascal_constant52", None)
                    
                    if opp_val == self:
                        setattr(item, "pascal_constant52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pascal_constant52"):
                    opp_val = getattr(item, "pascal_constant52", None)
                    
                    setattr(item, "pascal_constant52", self)
                    

    @property
    def pascal_constant136(self):
        return self.__pascal_constant136

    @pascal_constant136.setter
    def pascal_constant136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant136", None)
        self.__pascal_constant136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_subrangeType135"):
                opp_val = getattr(old_value, "pascal_subrangeType135", None)
                if opp_val == self:
                    setattr(old_value, "pascal_subrangeType135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_subrangeType135"):
                opp_val = getattr(value, "pascal_subrangeType135", None)
                setattr(value, "pascal_subrangeType135", self)

    @property
    def pascal_constant188(self):
        return self.__pascal_constant188

    @pascal_constant188.setter
    def pascal_constant188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant188", None)
        self.__pascal_constant188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_constList"):
                opp_val = getattr(old_value, "pascal_constList", None)
                if opp_val == self:
                    setattr(old_value, "pascal_constList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_constList"):
                opp_val = getattr(value, "pascal_constList", None)
                setattr(value, "pascal_constList", self)

    @property
    def pascal_constant52(self):
        return self.__pascal_constant52

    @pascal_constant52.setter
    def pascal_constant52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant52", None)
        self.__pascal_constant52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_constant50"):
                opp_val = getattr(old_value, "pascal_constant50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_constant50"):
                opp_val = getattr(value, "pascal_constant50", None)
                if opp_val is None:
                    setattr(value, "pascal_constant50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_constant44(self):
        return self.__pascal_constant44

    @pascal_constant44.setter
    def pascal_constant44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant44", None)
        self.__pascal_constant44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_unsignedNumber"):
                opp_val = getattr(old_value, "pascal_unsignedNumber", None)
                if opp_val == self:
                    setattr(old_value, "pascal_unsignedNumber", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_unsignedNumber"):
                opp_val = getattr(value, "pascal_unsignedNumber", None)
                setattr(value, "pascal_unsignedNumber", self)

    @property
    def pascal_constant46(self):
        return self.__pascal_constant46

    @pascal_constant46.setter
    def pascal_constant46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant46", None)
        self.__pascal_constant46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_identifier47"):
                opp_val = getattr(old_value, "pascal_identifier47", None)
                if opp_val == self:
                    setattr(old_value, "pascal_identifier47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_identifier47"):
                opp_val = getattr(value, "pascal_identifier47", None)
                setattr(value, "pascal_identifier47", self)

    @property
    def pascal_constant54(self):
        return self.__pascal_constant54

    @pascal_constant54.setter
    def pascal_constant54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant54", None)
        self.__pascal_constant54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_fieldList"):
                opp_val = getattr(old_value, "pascal_fieldList", None)
                if opp_val == self:
                    setattr(old_value, "pascal_fieldList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_fieldList"):
                opp_val = getattr(value, "pascal_fieldList", None)
                setattr(value, "pascal_fieldList", self)

    @property
    def pascal_constant(self):
        return self.__pascal_constant

    @pascal_constant.setter
    def pascal_constant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant", None)
        self.__pascal_constant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_constantDefinition42"):
                opp_val = getattr(old_value, "pascal_constantDefinition42", None)
                if opp_val == self:
                    setattr(old_value, "pascal_constantDefinition42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_constantDefinition42"):
                opp_val = getattr(value, "pascal_constantDefinition42", None)
                setattr(value, "pascal_constantDefinition42", self)

    @property
    def pascal_constant49(self):
        return self.__pascal_constant49

    @pascal_constant49.setter
    def pascal_constant49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant49", None)
        self.__pascal_constant49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_constantChr"):
                opp_val = getattr(old_value, "pascal_constantChr", None)
                if opp_val == self:
                    setattr(old_value, "pascal_constantChr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_constantChr"):
                opp_val = getattr(value, "pascal_constantChr", None)
                setattr(value, "pascal_constantChr", self)

    @property
    def pascal_constant133(self):
        return self.__pascal_constant133

    @pascal_constant133.setter
    def pascal_constant133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant133", None)
        self.__pascal_constant133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_subrangeType132"):
                opp_val = getattr(old_value, "pascal_subrangeType132", None)
                if opp_val == self:
                    setattr(old_value, "pascal_subrangeType132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_subrangeType132"):
                opp_val = getattr(value, "pascal_subrangeType132", None)
                setattr(value, "pascal_subrangeType132", self)

    @property
    def pascal_constant191(self):
        return self.__pascal_constant191

    @pascal_constant191.setter
    def pascal_constant191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant191", None)
        self.__pascal_constant191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_constList190"):
                opp_val = getattr(old_value, "pascal_constList190", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_constList190"):
                opp_val = getattr(value, "pascal_constList190", None)
                if opp_val is None:
                    setattr(value, "pascal_constList190", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pascal_constantDefinition:

    pass
class pascal_unsignedInteger:

    def __init__(self, number: str, pascal_unsignedInteger: "pascal_label" = None, pascal_unsignedInteger57: "pascal_constantChr" = None, pascal_unsignedInteger60: "pascal_unsignedNumber" = None):
        self.number = number
        self.pascal_unsignedInteger = pascal_unsignedInteger
        self.pascal_unsignedInteger57 = pascal_unsignedInteger57
        self.pascal_unsignedInteger60 = pascal_unsignedInteger60
        
    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def pascal_unsignedInteger57(self):
        return self.__pascal_unsignedInteger57

    @pascal_unsignedInteger57.setter
    def pascal_unsignedInteger57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_unsignedInteger__pascal_unsignedInteger57", None)
        self.__pascal_unsignedInteger57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_constantChr56"):
                opp_val = getattr(old_value, "pascal_constantChr56", None)
                if opp_val == self:
                    setattr(old_value, "pascal_constantChr56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_constantChr56"):
                opp_val = getattr(value, "pascal_constantChr56", None)
                setattr(value, "pascal_constantChr56", self)

    @property
    def pascal_unsignedInteger(self):
        return self.__pascal_unsignedInteger

    @pascal_unsignedInteger.setter
    def pascal_unsignedInteger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_unsignedInteger__pascal_unsignedInteger", None)
        self.__pascal_unsignedInteger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_label32"):
                opp_val = getattr(old_value, "pascal_label32", None)
                if opp_val == self:
                    setattr(old_value, "pascal_label32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_label32"):
                opp_val = getattr(value, "pascal_label32", None)
                setattr(value, "pascal_label32", self)

    @property
    def pascal_unsignedInteger60(self):
        return self.__pascal_unsignedInteger60

    @pascal_unsignedInteger60.setter
    def pascal_unsignedInteger60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_unsignedInteger__pascal_unsignedInteger60", None)
        self.__pascal_unsignedInteger60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_unsignedNumber59"):
                opp_val = getattr(old_value, "pascal_unsignedNumber59", None)
                if opp_val == self:
                    setattr(old_value, "pascal_unsignedNumber59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_unsignedNumber59"):
                opp_val = getattr(value, "pascal_unsignedNumber59", None)
                setattr(value, "pascal_unsignedNumber59", self)

class statement:

    pass
class label_declaration_part:

    pass
class pascal_label(label_declaration_part, statement):

    pass
class pascal_compoundStatement:

    pass
class pascal_usesUnitsPart:

    pass
class pascal_procedureAndFunctionDeclarationPart:

    pass
class pascal_variableDeclarationPart:

    pass
class pascal_typeDefinitionPart:

    pass
class pascal_constantDefinitionPart:

    pass
class pascal_label_declaration_part:

    pass
class pascal_identifierList:

    pass
class pascal_identifier:

    def __init__(self, identifier: str, pascal_identifier: "pascal_programHeading" = None, pascal_identifier11: "pascal_identifierList" = None, pascal_identifier14: "pascal_identifierList" = None, pascal_identifier35: "pascal_label" = None, pascal_identifier40: "pascal_constantDefinition" = None, pascal_identifier47: "pascal_constant" = None, pascal_identifier71: "pascal_typeDefinition" = None, pascal_identifier106: "pascal_typeIdentifier" = None, pascal_identifier146: "pascal_stringtype" = None, pascal_identifier180: "pascal_tag" = None, pascal_identifier213: "pascal_procedureDeclaration" = None, pascal_identifier222: "pascal_functionDeclaration" = None, pascal_identifier239: "pascal_unlabelledStatement" = None, pascal_identifier253: "pascal_variable" = None, pascal_identifier292: "pascal_functionDesignator" = None):
        self.identifier = identifier
        self.pascal_identifier = pascal_identifier
        self.pascal_identifier11 = pascal_identifier11
        self.pascal_identifier14 = pascal_identifier14
        self.pascal_identifier35 = pascal_identifier35
        self.pascal_identifier40 = pascal_identifier40
        self.pascal_identifier47 = pascal_identifier47
        self.pascal_identifier71 = pascal_identifier71
        self.pascal_identifier106 = pascal_identifier106
        self.pascal_identifier146 = pascal_identifier146
        self.pascal_identifier180 = pascal_identifier180
        self.pascal_identifier213 = pascal_identifier213
        self.pascal_identifier222 = pascal_identifier222
        self.pascal_identifier239 = pascal_identifier239
        self.pascal_identifier253 = pascal_identifier253
        self.pascal_identifier292 = pascal_identifier292
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def pascal_identifier253(self):
        return self.__pascal_identifier253

    @pascal_identifier253.setter
    def pascal_identifier253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier253", None)
        self.__pascal_identifier253 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_variable252"):
                opp_val = getattr(old_value, "pascal_variable252", None)
                if opp_val == self:
                    setattr(old_value, "pascal_variable252", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_variable252"):
                opp_val = getattr(value, "pascal_variable252", None)
                setattr(value, "pascal_variable252", self)

    @property
    def pascal_identifier11(self):
        return self.__pascal_identifier11

    @pascal_identifier11.setter
    def pascal_identifier11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier11", None)
        self.__pascal_identifier11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_identifierList10"):
                opp_val = getattr(old_value, "pascal_identifierList10", None)
                if opp_val == self:
                    setattr(old_value, "pascal_identifierList10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_identifierList10"):
                opp_val = getattr(value, "pascal_identifierList10", None)
                setattr(value, "pascal_identifierList10", self)

    @property
    def pascal_identifier35(self):
        return self.__pascal_identifier35

    @pascal_identifier35.setter
    def pascal_identifier35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier35", None)
        self.__pascal_identifier35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_label34"):
                opp_val = getattr(old_value, "pascal_label34", None)
                if opp_val == self:
                    setattr(old_value, "pascal_label34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_label34"):
                opp_val = getattr(value, "pascal_label34", None)
                setattr(value, "pascal_label34", self)

    @property
    def pascal_identifier213(self):
        return self.__pascal_identifier213

    @pascal_identifier213.setter
    def pascal_identifier213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier213", None)
        self.__pascal_identifier213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_procedureDeclaration212"):
                opp_val = getattr(old_value, "pascal_procedureDeclaration212", None)
                if opp_val == self:
                    setattr(old_value, "pascal_procedureDeclaration212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_procedureDeclaration212"):
                opp_val = getattr(value, "pascal_procedureDeclaration212", None)
                setattr(value, "pascal_procedureDeclaration212", self)

    @property
    def pascal_identifier47(self):
        return self.__pascal_identifier47

    @pascal_identifier47.setter
    def pascal_identifier47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier47", None)
        self.__pascal_identifier47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_constant46"):
                opp_val = getattr(old_value, "pascal_constant46", None)
                if opp_val == self:
                    setattr(old_value, "pascal_constant46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_constant46"):
                opp_val = getattr(value, "pascal_constant46", None)
                setattr(value, "pascal_constant46", self)

    @property
    def pascal_identifier292(self):
        return self.__pascal_identifier292

    @pascal_identifier292.setter
    def pascal_identifier292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier292", None)
        self.__pascal_identifier292 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_functionDesignator291"):
                opp_val = getattr(old_value, "pascal_functionDesignator291", None)
                if opp_val == self:
                    setattr(old_value, "pascal_functionDesignator291", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_functionDesignator291"):
                opp_val = getattr(value, "pascal_functionDesignator291", None)
                setattr(value, "pascal_functionDesignator291", self)

    @property
    def pascal_identifier146(self):
        return self.__pascal_identifier146

    @pascal_identifier146.setter
    def pascal_identifier146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier146", None)
        self.__pascal_identifier146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_stringtype145"):
                opp_val = getattr(old_value, "pascal_stringtype145", None)
                if opp_val == self:
                    setattr(old_value, "pascal_stringtype145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_stringtype145"):
                opp_val = getattr(value, "pascal_stringtype145", None)
                setattr(value, "pascal_stringtype145", self)

    @property
    def pascal_identifier40(self):
        return self.__pascal_identifier40

    @pascal_identifier40.setter
    def pascal_identifier40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier40", None)
        self.__pascal_identifier40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_constantDefinition39"):
                opp_val = getattr(old_value, "pascal_constantDefinition39", None)
                if opp_val == self:
                    setattr(old_value, "pascal_constantDefinition39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_constantDefinition39"):
                opp_val = getattr(value, "pascal_constantDefinition39", None)
                setattr(value, "pascal_constantDefinition39", self)

    @property
    def pascal_identifier(self):
        return self.__pascal_identifier

    @pascal_identifier.setter
    def pascal_identifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier", None)
        self.__pascal_identifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_programHeading6"):
                opp_val = getattr(old_value, "pascal_programHeading6", None)
                if opp_val == self:
                    setattr(old_value, "pascal_programHeading6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_programHeading6"):
                opp_val = getattr(value, "pascal_programHeading6", None)
                setattr(value, "pascal_programHeading6", self)

    @property
    def pascal_identifier239(self):
        return self.__pascal_identifier239

    @pascal_identifier239.setter
    def pascal_identifier239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier239", None)
        self.__pascal_identifier239 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_unlabelledStatement238"):
                opp_val = getattr(old_value, "pascal_unlabelledStatement238", None)
                if opp_val == self:
                    setattr(old_value, "pascal_unlabelledStatement238", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_unlabelledStatement238"):
                opp_val = getattr(value, "pascal_unlabelledStatement238", None)
                setattr(value, "pascal_unlabelledStatement238", self)

    @property
    def pascal_identifier71(self):
        return self.__pascal_identifier71

    @pascal_identifier71.setter
    def pascal_identifier71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier71", None)
        self.__pascal_identifier71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_typeDefinition70"):
                opp_val = getattr(old_value, "pascal_typeDefinition70", None)
                if opp_val == self:
                    setattr(old_value, "pascal_typeDefinition70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_typeDefinition70"):
                opp_val = getattr(value, "pascal_typeDefinition70", None)
                setattr(value, "pascal_typeDefinition70", self)

    @property
    def pascal_identifier106(self):
        return self.__pascal_identifier106

    @pascal_identifier106.setter
    def pascal_identifier106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier106", None)
        self.__pascal_identifier106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_typeIdentifier105"):
                opp_val = getattr(old_value, "pascal_typeIdentifier105", None)
                if opp_val == self:
                    setattr(old_value, "pascal_typeIdentifier105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_typeIdentifier105"):
                opp_val = getattr(value, "pascal_typeIdentifier105", None)
                setattr(value, "pascal_typeIdentifier105", self)

    @property
    def pascal_identifier222(self):
        return self.__pascal_identifier222

    @pascal_identifier222.setter
    def pascal_identifier222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier222", None)
        self.__pascal_identifier222 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_functionDeclaration221"):
                opp_val = getattr(old_value, "pascal_functionDeclaration221", None)
                if opp_val == self:
                    setattr(old_value, "pascal_functionDeclaration221", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_functionDeclaration221"):
                opp_val = getattr(value, "pascal_functionDeclaration221", None)
                setattr(value, "pascal_functionDeclaration221", self)

    @property
    def pascal_identifier180(self):
        return self.__pascal_identifier180

    @pascal_identifier180.setter
    def pascal_identifier180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier180", None)
        self.__pascal_identifier180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_tag179"):
                opp_val = getattr(old_value, "pascal_tag179", None)
                if opp_val == self:
                    setattr(old_value, "pascal_tag179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_tag179"):
                opp_val = getattr(value, "pascal_tag179", None)
                setattr(value, "pascal_tag179", self)

    @property
    def pascal_identifier14(self):
        return self.__pascal_identifier14

    @pascal_identifier14.setter
    def pascal_identifier14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier14", None)
        self.__pascal_identifier14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_identifierList13"):
                opp_val = getattr(old_value, "pascal_identifierList13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_identifierList13"):
                opp_val = getattr(value, "pascal_identifierList13", None)
                if opp_val is None:
                    setattr(value, "pascal_identifierList13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pascal_block:

    pass
class pascal_programHeading:

    pass
class pascal_program:

    pass
class pascal_pascal:

    pass