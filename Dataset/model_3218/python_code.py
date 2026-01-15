from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class OOLanguage(Enum):
    JAVA = "JAVA"
    CPP = "CPP"
class OOCollectionType(Enum):
    NONE = "NONE"
    SET = "SET"
    LIST = "LIST"
class OOBaseType(Enum):
    INT = "INT"
    LONG = "LONG"
    DOUBLE = "DOUBLE"
    STRING = "STRING"
    OBJECT = "OBJECT"
    BYTE = "BYTE"
    BOOLEAN = "BOOLEAN"
class OOVisibility(Enum):
    PRIVATE = "PRIVATE"
    PACKAGE = "PACKAGE"
    PROTECTED = "PROTECTED"
    PUBLIC = "PUBLIC"


############################################
# Definition of Classes
############################################

class oogen_OOCommentOwner:

    pass
class oogen_OOComment:

    def __init__(self, text: str, isBlockComment: bool, oogen_OOComment: "oogen_OOCommentOwner" = None, oogen_OOComment144: "oogen_OOCommentOwner" = None):
        self.text = text
        self.isBlockComment = isBlockComment
        self.oogen_OOComment = oogen_OOComment
        self.oogen_OOComment144 = oogen_OOComment144
        
    @property
    def isBlockComment(self) -> bool:
        return self.__isBlockComment

    @isBlockComment.setter
    def isBlockComment(self, isBlockComment: bool):
        self.__isBlockComment = isBlockComment

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def oogen_OOComment144(self):
        return self.__oogen_OOComment144

    @oogen_OOComment144.setter
    def oogen_OOComment144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOComment__oogen_OOComment144", None)
        self.__oogen_OOComment144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oogen_OOCommentOwner143"):
                opp_val = getattr(old_value, "oogen_OOCommentOwner143", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oogen_OOCommentOwner143"):
                opp_val = getattr(value, "oogen_OOCommentOwner143", None)
                if opp_val is None:
                    setattr(value, "oogen_OOCommentOwner143", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def oogen_OOComment(self):
        return self.__oogen_OOComment

    @oogen_OOComment.setter
    def oogen_OOComment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOComment__oogen_OOComment", None)
        self.__oogen_OOComment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oogen_OOCommentOwner"):
                opp_val = getattr(old_value, "oogen_OOCommentOwner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oogen_OOCommentOwner"):
                opp_val = getattr(value, "oogen_OOCommentOwner", None)
                if opp_val is None:
                    setattr(value, "oogen_OOCommentOwner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class OOComparatorExpression:

    pass
class oogen_OOLessEqualsExpression(OOComparatorExpression):

    pass
class oogen_OOGreaterEqualsExpression(OOComparatorExpression):

    pass
class oogen_OOEqualsExpression(OOComparatorExpression):

    pass
class oogen_OONotEqualsExpression(OOComparatorExpression):

    pass
class oogen_OOLessThanExpression(OOComparatorExpression):

    pass
class oogen_OOGreaterThanExpression(OOComparatorExpression):

    pass
class oogen_OOLanguageSpecificSnippet:

    def __init__(self, code: str, lang: str, oogen_OOLanguageSpecificSnippet: "oogen_OOLanguageSpecificExpression" = None):
        self.code = code
        self.lang = lang
        self.oogen_OOLanguageSpecificSnippet = oogen_OOLanguageSpecificSnippet
        
    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def oogen_OOLanguageSpecificSnippet(self):
        return self.__oogen_OOLanguageSpecificSnippet

    @oogen_OOLanguageSpecificSnippet.setter
    def oogen_OOLanguageSpecificSnippet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOLanguageSpecificSnippet__oogen_OOLanguageSpecificSnippet", None)
        self.__oogen_OOLanguageSpecificSnippet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oogen_OOLanguageSpecificExpression"):
                opp_val = getattr(old_value, "oogen_OOLanguageSpecificExpression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oogen_OOLanguageSpecificExpression"):
                opp_val = getattr(value, "oogen_OOLanguageSpecificExpression", None)
                if opp_val is None:
                    setattr(value, "oogen_OOLanguageSpecificExpression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class OOOneOperandArithmeticExpression:

    pass
class oogen_OOPostfixDecrementExpression(OOOneOperandArithmeticExpression):

    pass
class oogen_OOPostfixIncrementExpression(OOOneOperandArithmeticExpression):

    pass
class oogen_OOPrefixDecrementExpression(OOOneOperandArithmeticExpression):

    pass
class oogen_OOBracketedExpression(OOOneOperandArithmeticExpression):

    pass
class oogen_OOPrefixIncrementExpression(OOOneOperandArithmeticExpression):

    pass
class oogen_OOPlusExpression(OOOneOperandArithmeticExpression):

    pass
class oogen_OOMinusExpression(OOOneOperandArithmeticExpression):

    pass
class oogen_OOBitWiseComplement(OOOneOperandArithmeticExpression):

    pass
class OOConditionalStatement:

    pass
class oogen_OODoWhile(OOConditionalStatement):

    pass
class oogen_OOFor(OOConditionalStatement):

    pass
class oogen_OOWhile(OOConditionalStatement):

    pass
class oogen_OOIf(OOConditionalStatement):

    pass
class OOCompoundStatement:

    pass
class oogen_OOCase(OOCompoundStatement):

    pass
class oogen_OODefault(OOCompoundStatement):

    pass
class OOLogicalExpression:

    pass
class oogen_OOTernaryOperator(OOLogicalExpression):

    pass
class oogen_OOLogicalLiteral(OOLogicalExpression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class oogen_OOComparatorExpression(OOLogicalExpression):

    pass
class oogen_OOTwoOperandLogicalExpression(OOLogicalExpression):

    pass
class OOOneOperandLogicalExpression:

    pass
class oogen_OONotExpression(OOOneOperandLogicalExpression):

    pass
class OOTwoOperandLogicalExpression:

    pass
class oogen_OOOrExpression(OOTwoOperandLogicalExpression):

    pass
class oogen_OOXorExpression(OOTwoOperandLogicalExpression):

    pass
class oogen_OOAndExpression(OOTwoOperandLogicalExpression):

    pass
class OOTwoOperandArithmeticExpression:

    pass
class oogen_OOTwoOperandAssignableExpression(OOTwoOperandArithmeticExpression):

    def __init__(self, assigned: bool):
        self.assigned = assigned
        
    @property
    def assigned(self) -> bool:
        return self.__assigned

    @assigned.setter
    def assigned(self, assigned: bool):
        self.__assigned = assigned

class oogen_OORootExpression(OOTwoOperandArithmeticExpression):

    pass
class oogen_OOPowerExpression(OOTwoOperandArithmeticExpression):

    pass
class oogen_OOOneOperandLogicalExpression(OOLogicalExpression):

    pass
class OOArithmeticExpression:

    pass
class oogen_OOOneOperandArithmeticExpression(OOArithmeticExpression):

    pass
class oogen_OOFloatLiteral(OOArithmeticExpression):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class oogen_OOIntegerLiteral(OOArithmeticExpression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class oogen_OODoubleLiteral(OOArithmeticExpression):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class oogen_OOLongLiteral(OOArithmeticExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class oogen_OOTwoOperandArithmeticExpression(OOArithmeticExpression):

    pass
class OOExpression:

    pass
class oogen_OOTypeCast(OOExpression):

    pass
class oogen_OOVariableReferenceExpression(OOExpression):

    pass
class oogen_OOBoolLiteral(OOExpression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class oogen_OOInitializerList(OOExpression):

    pass
class oogen_OONewArray(OOExpression):

    pass
class oogen_OOFieldReferenceExpression(OOExpression):

    def __init__(self, fieldName: str, oogen_OOFieldReferenceExpression: "oogen_OOExpression" = None):
        self.fieldName = fieldName
        self.oogen_OOFieldReferenceExpression = oogen_OOFieldReferenceExpression
        
    @property
    def fieldName(self) -> str:
        return self.__fieldName

    @fieldName.setter
    def fieldName(self, fieldName: str):
        self.__fieldName = fieldName

    @property
    def oogen_OOFieldReferenceExpression(self):
        return self.__oogen_OOFieldReferenceExpression

    @oogen_OOFieldReferenceExpression.setter
    def oogen_OOFieldReferenceExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOFieldReferenceExpression__oogen_OOFieldReferenceExpression", None)
        self.__oogen_OOFieldReferenceExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oogen_OOExpression120"):
                opp_val = getattr(old_value, "oogen_OOExpression120", None)
                if opp_val == self:
                    setattr(old_value, "oogen_OOExpression120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oogen_OOExpression120"):
                opp_val = getattr(value, "oogen_OOExpression120", None)
                setattr(value, "oogen_OOExpression120", self)

class oogen_OOThisLiteral(OOExpression):

    pass
class oogen_OONullLiteral(OOExpression):

    pass
class oogen_OONewClass(OOExpression):

    def __init__(self, className: str, oogen_OONewClass: set["oogen_OOExpression"] = None):
        self.className = className
        self.oogen_OONewClass = oogen_OONewClass if oogen_OONewClass is not None else set()
        
    @property
    def className(self) -> str:
        return self.__className

    @className.setter
    def className(self, className: str):
        self.__className = className

    @property
    def oogen_OONewClass(self):
        return self.__oogen_OONewClass

    @oogen_OONewClass.setter
    def oogen_OONewClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OONewClass__oogen_OONewClass", None)
        self.__oogen_OONewClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oogen_OOExpression90"):
                    opp_val = getattr(item, "oogen_OOExpression90", None)
                    
                    if opp_val == self:
                        setattr(item, "oogen_OOExpression90", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oogen_OOExpression90"):
                    opp_val = getattr(item, "oogen_OOExpression90", None)
                    
                    setattr(item, "oogen_OOExpression90", self)
                    

class oogen_OOFunctionCallExpression(OOExpression):

    def __init__(self, functionName: str, oogen_OOFunctionCallExpression: set["oogen_OOExpression"] = None, oogen_OOFunctionCallExpression128: "oogen_OOExpression" = None):
        self.functionName = functionName
        self.oogen_OOFunctionCallExpression = oogen_OOFunctionCallExpression if oogen_OOFunctionCallExpression is not None else set()
        self.oogen_OOFunctionCallExpression128 = oogen_OOFunctionCallExpression128
        
    @property
    def functionName(self) -> str:
        return self.__functionName

    @functionName.setter
    def functionName(self, functionName: str):
        self.__functionName = functionName

    @property
    def oogen_OOFunctionCallExpression(self):
        return self.__oogen_OOFunctionCallExpression

    @oogen_OOFunctionCallExpression.setter
    def oogen_OOFunctionCallExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOFunctionCallExpression__oogen_OOFunctionCallExpression", None)
        self.__oogen_OOFunctionCallExpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oogen_OOExpression126"):
                    opp_val = getattr(item, "oogen_OOExpression126", None)
                    
                    if opp_val == self:
                        setattr(item, "oogen_OOExpression126", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oogen_OOExpression126"):
                    opp_val = getattr(item, "oogen_OOExpression126", None)
                    
                    setattr(item, "oogen_OOExpression126", self)
                    

    @property
    def oogen_OOFunctionCallExpression128(self):
        return self.__oogen_OOFunctionCallExpression128

    @oogen_OOFunctionCallExpression128.setter
    def oogen_OOFunctionCallExpression128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOFunctionCallExpression__oogen_OOFunctionCallExpression128", None)
        self.__oogen_OOFunctionCallExpression128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oogen_OOExpression129"):
                opp_val = getattr(old_value, "oogen_OOExpression129", None)
                if opp_val == self:
                    setattr(old_value, "oogen_OOExpression129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oogen_OOExpression129"):
                opp_val = getattr(value, "oogen_OOExpression129", None)
                setattr(value, "oogen_OOExpression129", self)

class oogen_OOLogicalExpression(OOExpression):

    pass
class oogen_OOAssignmentExpression(OOExpression):

    pass
class oogen_OOLanguageSpecificExpression(OOExpression, OOLogicalExpression):

    pass
class oogen_OOStringLiteral(OOExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class oogen_OOIndexing(OOExpression):

    pass
class oogen_OOEmptyExpression(OOExpression):

    pass
class oogen_OOArithmeticExpression(OOExpression):

    pass
class OOTwoOperandAssignableExpression:

    pass
class oogen_OOBitwiseOrExpression(OOTwoOperandAssignableExpression):

    pass
class oogen_OOBitWiseLeftShift(OOTwoOperandAssignableExpression):

    pass
class oogen_OOIntegerDivisionExpression(OOTwoOperandAssignableExpression):

    pass
class oogen_OOBitwiseXorExpression(OOTwoOperandAssignableExpression):

    pass
class oogen_OOBitwiseAndExpression(OOTwoOperandAssignableExpression):

    pass
class oogen_OODivisionExpression(OOTwoOperandAssignableExpression):

    pass
class oogen_OOMultiplicationExpression(OOTwoOperandAssignableExpression):

    pass
class oogen_OOSubtractionExpression(OOTwoOperandAssignableExpression):

    pass
class oogen_OOModuloExpression(OOTwoOperandAssignableExpression):

    pass
class oogen_OOBitWiseRightShift(OOTwoOperandAssignableExpression):

    pass
class oogen_OOAdditionExpression(OOTwoOperandAssignableExpression):

    pass
class oogen_OOModel:

    pass
class oogen_OOType:

    def __init__(self, baseType: str, arrayDimensions: int, collectionType: str, numberOfIndirections: int, oogen_OOType: "oogen_OOVariable" = None, oogen_OOType12: "oogen_OOClass" = None, oogen_OOType15: set["oogen_OOExpression"] = None, oogen_OOType18: "oogen_OOEnumeration" = None, oogen_OOType25: "oogen_OOMethod" = None, oogen_OOType85: "oogen_OOTypeCast" = None, oogen_OOType137: "oogen_OONewArray" = None):
        self.baseType = baseType
        self.arrayDimensions = arrayDimensions
        self.collectionType = collectionType
        self.numberOfIndirections = numberOfIndirections
        self.oogen_OOType = oogen_OOType
        self.oogen_OOType12 = oogen_OOType12
        self.oogen_OOType15 = oogen_OOType15 if oogen_OOType15 is not None else set()
        self.oogen_OOType18 = oogen_OOType18
        self.oogen_OOType25 = oogen_OOType25
        self.oogen_OOType85 = oogen_OOType85
        self.oogen_OOType137 = oogen_OOType137
        
    @property
    def baseType(self) -> str:
        return self.__baseType

    @baseType.setter
    def baseType(self, baseType: str):
        self.__baseType = baseType

    @property
    def arrayDimensions(self) -> int:
        return self.__arrayDimensions

    @arrayDimensions.setter
    def arrayDimensions(self, arrayDimensions: int):
        self.__arrayDimensions = arrayDimensions

    @property
    def collectionType(self) -> str:
        return self.__collectionType

    @collectionType.setter
    def collectionType(self, collectionType: str):
        self.__collectionType = collectionType

    @property
    def numberOfIndirections(self) -> int:
        return self.__numberOfIndirections

    @numberOfIndirections.setter
    def numberOfIndirections(self, numberOfIndirections: int):
        self.__numberOfIndirections = numberOfIndirections

    @property
    def oogen_OOType85(self):
        return self.__oogen_OOType85

    @oogen_OOType85.setter
    def oogen_OOType85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOType__oogen_OOType85", None)
        self.__oogen_OOType85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oogen_OOTypeCast"):
                opp_val = getattr(old_value, "oogen_OOTypeCast", None)
                if opp_val == self:
                    setattr(old_value, "oogen_OOTypeCast", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oogen_OOTypeCast"):
                opp_val = getattr(value, "oogen_OOTypeCast", None)
                setattr(value, "oogen_OOTypeCast", self)

    @property
    def oogen_OOType12(self):
        return self.__oogen_OOType12

    @oogen_OOType12.setter
    def oogen_OOType12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOType__oogen_OOType12", None)
        self.__oogen_OOType12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oogen_OOClass13"):
                opp_val = getattr(old_value, "oogen_OOClass13", None)
                if opp_val == self:
                    setattr(old_value, "oogen_OOClass13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oogen_OOClass13"):
                opp_val = getattr(value, "oogen_OOClass13", None)
                setattr(value, "oogen_OOClass13", self)

    @property
    def oogen_OOType(self):
        return self.__oogen_OOType

    @oogen_OOType.setter
    def oogen_OOType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOType__oogen_OOType", None)
        self.__oogen_OOType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oogen_OOVariable"):
                opp_val = getattr(old_value, "oogen_OOVariable", None)
                if opp_val == self:
                    setattr(old_value, "oogen_OOVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oogen_OOVariable"):
                opp_val = getattr(value, "oogen_OOVariable", None)
                setattr(value, "oogen_OOVariable", self)

    @property
    def oogen_OOType25(self):
        return self.__oogen_OOType25

    @oogen_OOType25.setter
    def oogen_OOType25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOType__oogen_OOType25", None)
        self.__oogen_OOType25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oogen_OOMethod24"):
                opp_val = getattr(old_value, "oogen_OOMethod24", None)
                if opp_val == self:
                    setattr(old_value, "oogen_OOMethod24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oogen_OOMethod24"):
                opp_val = getattr(value, "oogen_OOMethod24", None)
                setattr(value, "oogen_OOMethod24", self)

    @property
    def oogen_OOType137(self):
        return self.__oogen_OOType137

    @oogen_OOType137.setter
    def oogen_OOType137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOType__oogen_OOType137", None)
        self.__oogen_OOType137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oogen_OONewArray"):
                opp_val = getattr(old_value, "oogen_OONewArray", None)
                if opp_val == self:
                    setattr(old_value, "oogen_OONewArray", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oogen_OONewArray"):
                opp_val = getattr(value, "oogen_OONewArray", None)
                setattr(value, "oogen_OONewArray", self)

    @property
    def oogen_OOType15(self):
        return self.__oogen_OOType15

    @oogen_OOType15.setter
    def oogen_OOType15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOType__oogen_OOType15", None)
        self.__oogen_OOType15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oogen_OOExpression16"):
                    opp_val = getattr(item, "oogen_OOExpression16", None)
                    
                    if opp_val == self:
                        setattr(item, "oogen_OOExpression16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oogen_OOExpression16"):
                    opp_val = getattr(item, "oogen_OOExpression16", None)
                    
                    setattr(item, "oogen_OOExpression16", self)
                    

    @property
    def oogen_OOType18(self):
        return self.__oogen_OOType18

    @oogen_OOType18.setter
    def oogen_OOType18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOType__oogen_OOType18", None)
        self.__oogen_OOType18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oogen_OOEnumeration19"):
                opp_val = getattr(old_value, "oogen_OOEnumeration19", None)
                if opp_val == self:
                    setattr(old_value, "oogen_OOEnumeration19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oogen_OOEnumeration19"):
                opp_val = getattr(value, "oogen_OOEnumeration19", None)
                setattr(value, "oogen_OOEnumeration19", self)

class OOStatement:

    pass
class oogen_OOBreak(OOStatement):

    pass
class oogen_OOContinue(OOStatement):

    pass
class oogen_OOSwitch(OOStatement):

    pass
class oogen_OOCompoundStatement(OOStatement):

    pass
class oogen_OOForEach(OOStatement):

    pass
class oogen_OOConditionalStatement(OOStatement, OOCompoundStatement):

    pass
class oogen_OOReturn(OOStatement):

    pass
class oogen_OOVariableDeclarationList(OOStatement):

    pass
class oogen_OOEmptyStatement(OOStatement):

    pass
class oogen_OOExpression(OOStatement):

    pass
class oogen_OOVariable(OOStatement):

    def __init__(self, name: str, transient: bool, oogen_OOVariable: "oogen_OOType" = None, oogen_OOVariable10: "oogen_OOExpression" = None, oogen_OOVariable22: "oogen_OOMethod" = None, oogen_OOVariable35: "oogen_OOModel" = None, oogen_OOVariable76: "oogen_OOForEach" = None, oogen_OOVariable79: "oogen_OOForEach" = None, oogen_OOVariable108: "oogen_OOVariableDeclarationList" = None, oogen_OOVariable122: "oogen_OOVariableReferenceExpression" = None, oogen_OOVariable132: "oogen_OOConstructor" = None):
        self.name = name
        self.transient = transient
        self.oogen_OOVariable = oogen_OOVariable
        self.oogen_OOVariable10 = oogen_OOVariable10
        self.oogen_OOVariable22 = oogen_OOVariable22
        self.oogen_OOVariable35 = oogen_OOVariable35
        self.oogen_OOVariable76 = oogen_OOVariable76
        self.oogen_OOVariable79 = oogen_OOVariable79
        self.oogen_OOVariable108 = oogen_OOVariable108
        self.oogen_OOVariable122 = oogen_OOVariable122
        self.oogen_OOVariable132 = oogen_OOVariable132
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def transient(self) -> bool:
        return self.__transient

    @transient.setter
    def transient(self, transient: bool):
        self.__transient = transient

    @property
    def oogen_OOVariable10(self):
        return self.__oogen_OOVariable10

    @oogen_OOVariable10.setter
    def oogen_OOVariable10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOVariable__oogen_OOVariable10", None)
        self.__oogen_OOVariable10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oogen_OOExpression"):
                opp_val = getattr(old_value, "oogen_OOExpression", None)
                if opp_val == self:
                    setattr(old_value, "oogen_OOExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oogen_OOExpression"):
                opp_val = getattr(value, "oogen_OOExpression", None)
                setattr(value, "oogen_OOExpression", self)

    @property
    def oogen_OOVariable122(self):
        return self.__oogen_OOVariable122

    @oogen_OOVariable122.setter
    def oogen_OOVariable122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOVariable__oogen_OOVariable122", None)
        self.__oogen_OOVariable122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oogen_OOVariableReferenceExpression"):
                opp_val = getattr(old_value, "oogen_OOVariableReferenceExpression", None)
                if opp_val == self:
                    setattr(old_value, "oogen_OOVariableReferenceExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oogen_OOVariableReferenceExpression"):
                opp_val = getattr(value, "oogen_OOVariableReferenceExpression", None)
                setattr(value, "oogen_OOVariableReferenceExpression", self)

    @property
    def oogen_OOVariable108(self):
        return self.__oogen_OOVariable108

    @oogen_OOVariable108.setter
    def oogen_OOVariable108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOVariable__oogen_OOVariable108", None)
        self.__oogen_OOVariable108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oogen_OOVariableDeclarationList"):
                opp_val = getattr(old_value, "oogen_OOVariableDeclarationList", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oogen_OOVariableDeclarationList"):
                opp_val = getattr(value, "oogen_OOVariableDeclarationList", None)
                if opp_val is None:
                    setattr(value, "oogen_OOVariableDeclarationList", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def oogen_OOVariable(self):
        return self.__oogen_OOVariable

    @oogen_OOVariable.setter
    def oogen_OOVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOVariable__oogen_OOVariable", None)
        self.__oogen_OOVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oogen_OOType"):
                opp_val = getattr(old_value, "oogen_OOType", None)
                if opp_val == self:
                    setattr(old_value, "oogen_OOType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oogen_OOType"):
                opp_val = getattr(value, "oogen_OOType", None)
                setattr(value, "oogen_OOType", self)

    @property
    def oogen_OOVariable35(self):
        return self.__oogen_OOVariable35

    @oogen_OOVariable35.setter
    def oogen_OOVariable35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOVariable__oogen_OOVariable35", None)
        self.__oogen_OOVariable35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oogen_OOModel34"):
                opp_val = getattr(old_value, "oogen_OOModel34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oogen_OOModel34"):
                opp_val = getattr(value, "oogen_OOModel34", None)
                if opp_val is None:
                    setattr(value, "oogen_OOModel34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def oogen_OOVariable22(self):
        return self.__oogen_OOVariable22

    @oogen_OOVariable22.setter
    def oogen_OOVariable22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOVariable__oogen_OOVariable22", None)
        self.__oogen_OOVariable22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oogen_OOMethod21"):
                opp_val = getattr(old_value, "oogen_OOMethod21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oogen_OOMethod21"):
                opp_val = getattr(value, "oogen_OOMethod21", None)
                if opp_val is None:
                    setattr(value, "oogen_OOMethod21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def oogen_OOVariable76(self):
        return self.__oogen_OOVariable76

    @oogen_OOVariable76.setter
    def oogen_OOVariable76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOVariable__oogen_OOVariable76", None)
        self.__oogen_OOVariable76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oogen_OOForEach"):
                opp_val = getattr(old_value, "oogen_OOForEach", None)
                if opp_val == self:
                    setattr(old_value, "oogen_OOForEach", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oogen_OOForEach"):
                opp_val = getattr(value, "oogen_OOForEach", None)
                setattr(value, "oogen_OOForEach", self)

    @property
    def oogen_OOVariable79(self):
        return self.__oogen_OOVariable79

    @oogen_OOVariable79.setter
    def oogen_OOVariable79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOVariable__oogen_OOVariable79", None)
        self.__oogen_OOVariable79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oogen_OOForEach78"):
                opp_val = getattr(old_value, "oogen_OOForEach78", None)
                if opp_val == self:
                    setattr(old_value, "oogen_OOForEach78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oogen_OOForEach78"):
                opp_val = getattr(value, "oogen_OOForEach78", None)
                setattr(value, "oogen_OOForEach78", self)

    @property
    def oogen_OOVariable132(self):
        return self.__oogen_OOVariable132

    @oogen_OOVariable132.setter
    def oogen_OOVariable132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOVariable__oogen_OOVariable132", None)
        self.__oogen_OOVariable132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oogen_OOConstructor131"):
                opp_val = getattr(old_value, "oogen_OOConstructor131", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oogen_OOConstructor131"):
                opp_val = getattr(value, "oogen_OOConstructor131", None)
                if opp_val is None:
                    setattr(value, "oogen_OOConstructor131", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class OOVariable:

    pass
class oogen_OOConstructor:

    def __init__(self, visibility: str, className: str, oogen_OOConstructor: "oogen_OOClass" = None, oogen_OOConstructor131: set["oogen_OOVariable"] = None, oogen_OOConstructor134: set["oogen_OOStatement"] = None):
        self.visibility = visibility
        self.className = className
        self.oogen_OOConstructor = oogen_OOConstructor
        self.oogen_OOConstructor131 = oogen_OOConstructor131 if oogen_OOConstructor131 is not None else set()
        self.oogen_OOConstructor134 = oogen_OOConstructor134 if oogen_OOConstructor134 is not None else set()
        
    @property
    def className(self) -> str:
        return self.__className

    @className.setter
    def className(self, className: str):
        self.__className = className

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def oogen_OOConstructor134(self):
        return self.__oogen_OOConstructor134

    @oogen_OOConstructor134.setter
    def oogen_OOConstructor134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOConstructor__oogen_OOConstructor134", None)
        self.__oogen_OOConstructor134 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oogen_OOStatement135"):
                    opp_val = getattr(item, "oogen_OOStatement135", None)
                    
                    if opp_val == self:
                        setattr(item, "oogen_OOStatement135", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oogen_OOStatement135"):
                    opp_val = getattr(item, "oogen_OOStatement135", None)
                    
                    setattr(item, "oogen_OOStatement135", self)
                    

    @property
    def oogen_OOConstructor(self):
        return self.__oogen_OOConstructor

    @oogen_OOConstructor.setter
    def oogen_OOConstructor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOConstructor__oogen_OOConstructor", None)
        self.__oogen_OOConstructor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oogen_OOClass7"):
                opp_val = getattr(old_value, "oogen_OOClass7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oogen_OOClass7"):
                opp_val = getattr(value, "oogen_OOClass7", None)
                if opp_val is None:
                    setattr(value, "oogen_OOClass7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def oogen_OOConstructor131(self):
        return self.__oogen_OOConstructor131

    @oogen_OOConstructor131.setter
    def oogen_OOConstructor131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOConstructor__oogen_OOConstructor131", None)
        self.__oogen_OOConstructor131 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oogen_OOVariable132"):
                    opp_val = getattr(item, "oogen_OOVariable132", None)
                    
                    if opp_val == self:
                        setattr(item, "oogen_OOVariable132", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oogen_OOVariable132"):
                    opp_val = getattr(item, "oogen_OOVariable132", None)
                    
                    setattr(item, "oogen_OOVariable132", self)
                    

class oogen_OOMember(OOVariable):

    def __init__(self, visibility: str, static: bool, languages: str, oogen_OOMember: "oogen_OOClass" = None):
        self.visibility = visibility
        self.static = static
        self.languages = languages
        self.oogen_OOMember = oogen_OOMember
        
    @property
    def languages(self) -> str:
        return self.__languages

    @languages.setter
    def languages(self, languages: str):
        self.__languages = languages

    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def oogen_OOMember(self):
        return self.__oogen_OOMember

    @oogen_OOMember.setter
    def oogen_OOMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOMember__oogen_OOMember", None)
        self.__oogen_OOMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oogen_OOClass"):
                opp_val = getattr(old_value, "oogen_OOClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oogen_OOClass"):
                opp_val = getattr(value, "oogen_OOClass", None)
                if opp_val is None:
                    setattr(value, "oogen_OOClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class OOCommentOwner:

    pass
class oogen_OOMethod(OOCommentOwner):

    def __init__(self, visibility: str, name: str, static: bool, languages: str, oogen_OOMethod: "oogen_OOClass" = None, oogen_OOMethod38: "oogen_OOModel" = None, oogen_OOMethod21: set["oogen_OOVariable"] = None, oogen_OOMethod24: "oogen_OOType" = None, oogen_OOMethod27: set["oogen_OOStatement"] = None):
        self.visibility = visibility
        self.name = name
        self.static = static
        self.languages = languages
        self.oogen_OOMethod = oogen_OOMethod
        self.oogen_OOMethod38 = oogen_OOMethod38
        self.oogen_OOMethod21 = oogen_OOMethod21 if oogen_OOMethod21 is not None else set()
        self.oogen_OOMethod24 = oogen_OOMethod24
        self.oogen_OOMethod27 = oogen_OOMethod27 if oogen_OOMethod27 is not None else set()
        
    @property
    def languages(self) -> str:
        return self.__languages

    @languages.setter
    def languages(self, languages: str):
        self.__languages = languages

    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def oogen_OOMethod24(self):
        return self.__oogen_OOMethod24

    @oogen_OOMethod24.setter
    def oogen_OOMethod24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOMethod__oogen_OOMethod24", None)
        self.__oogen_OOMethod24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oogen_OOType25"):
                opp_val = getattr(old_value, "oogen_OOType25", None)
                if opp_val == self:
                    setattr(old_value, "oogen_OOType25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oogen_OOType25"):
                opp_val = getattr(value, "oogen_OOType25", None)
                setattr(value, "oogen_OOType25", self)

    @property
    def oogen_OOMethod27(self):
        return self.__oogen_OOMethod27

    @oogen_OOMethod27.setter
    def oogen_OOMethod27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOMethod__oogen_OOMethod27", None)
        self.__oogen_OOMethod27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oogen_OOStatement"):
                    opp_val = getattr(item, "oogen_OOStatement", None)
                    
                    if opp_val == self:
                        setattr(item, "oogen_OOStatement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oogen_OOStatement"):
                    opp_val = getattr(item, "oogen_OOStatement", None)
                    
                    setattr(item, "oogen_OOStatement", self)
                    

    @property
    def oogen_OOMethod(self):
        return self.__oogen_OOMethod

    @oogen_OOMethod.setter
    def oogen_OOMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOMethod__oogen_OOMethod", None)
        self.__oogen_OOMethod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oogen_OOClass5"):
                opp_val = getattr(old_value, "oogen_OOClass5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oogen_OOClass5"):
                opp_val = getattr(value, "oogen_OOClass5", None)
                if opp_val is None:
                    setattr(value, "oogen_OOClass5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def oogen_OOMethod21(self):
        return self.__oogen_OOMethod21

    @oogen_OOMethod21.setter
    def oogen_OOMethod21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOMethod__oogen_OOMethod21", None)
        self.__oogen_OOMethod21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oogen_OOVariable22"):
                    opp_val = getattr(item, "oogen_OOVariable22", None)
                    
                    if opp_val == self:
                        setattr(item, "oogen_OOVariable22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oogen_OOVariable22"):
                    opp_val = getattr(item, "oogen_OOVariable22", None)
                    
                    setattr(item, "oogen_OOVariable22", self)
                    

    @property
    def oogen_OOMethod38(self):
        return self.__oogen_OOMethod38

    @oogen_OOMethod38.setter
    def oogen_OOMethod38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOMethod__oogen_OOMethod38", None)
        self.__oogen_OOMethod38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oogen_OOModel37"):
                opp_val = getattr(old_value, "oogen_OOModel37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oogen_OOModel37"):
                opp_val = getattr(value, "oogen_OOModel37", None)
                if opp_val is None:
                    setattr(value, "oogen_OOModel37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class oogen_OOStatement(OOCommentOwner):

    pass
class oogen_OOEnumeration(OOCommentOwner):

    def __init__(self, name: str, options: str, oogen_OOEnumeration: "oogen_OOPackage" = None, oogen_OOEnumeration19: "oogen_OOType" = None, oogen_OOEnumeration146: "oogen_OOPackage" = None):
        self.name = name
        self.options = options
        self.oogen_OOEnumeration = oogen_OOEnumeration
        self.oogen_OOEnumeration19 = oogen_OOEnumeration19
        self.oogen_OOEnumeration146 = oogen_OOEnumeration146
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def options(self) -> str:
        return self.__options

    @options.setter
    def options(self, options: str):
        self.__options = options

    @property
    def oogen_OOEnumeration19(self):
        return self.__oogen_OOEnumeration19

    @oogen_OOEnumeration19.setter
    def oogen_OOEnumeration19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOEnumeration__oogen_OOEnumeration19", None)
        self.__oogen_OOEnumeration19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oogen_OOType18"):
                opp_val = getattr(old_value, "oogen_OOType18", None)
                if opp_val == self:
                    setattr(old_value, "oogen_OOType18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oogen_OOType18"):
                opp_val = getattr(value, "oogen_OOType18", None)
                setattr(value, "oogen_OOType18", self)

    @property
    def oogen_OOEnumeration146(self):
        return self.__oogen_OOEnumeration146

    @oogen_OOEnumeration146.setter
    def oogen_OOEnumeration146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOEnumeration__oogen_OOEnumeration146", None)
        self.__oogen_OOEnumeration146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oogen_OOPackage147"):
                opp_val = getattr(old_value, "oogen_OOPackage147", None)
                if opp_val == self:
                    setattr(old_value, "oogen_OOPackage147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oogen_OOPackage147"):
                opp_val = getattr(value, "oogen_OOPackage147", None)
                setattr(value, "oogen_OOPackage147", self)

    @property
    def oogen_OOEnumeration(self):
        return self.__oogen_OOEnumeration

    @oogen_OOEnumeration.setter
    def oogen_OOEnumeration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOEnumeration__oogen_OOEnumeration", None)
        self.__oogen_OOEnumeration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oogen_OOPackage"):
                opp_val = getattr(old_value, "oogen_OOPackage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oogen_OOPackage"):
                opp_val = getattr(value, "oogen_OOPackage", None)
                if opp_val is None:
                    setattr(value, "oogen_OOPackage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class oogen_OOClass(OOCommentOwner):

    def __init__(self, name: str, keep: bool, languages: str, OOClass: "oogen_OOPackage" = None, oogen_OOClass: set["oogen_OOMember"] = None, classes: "oogen_OOPackage" = None, oogen_OOClass5: set["oogen_OOMethod"] = None, oogen_OOClass7: set["oogen_OOConstructor"] = None, oogen_OOClass13: "oogen_OOType" = None):
        self.name = name
        self.keep = keep
        self.languages = languages
        self.OOClass = OOClass
        self.oogen_OOClass = oogen_OOClass if oogen_OOClass is not None else set()
        self.classes = classes
        self.oogen_OOClass5 = oogen_OOClass5 if oogen_OOClass5 is not None else set()
        self.oogen_OOClass7 = oogen_OOClass7 if oogen_OOClass7 is not None else set()
        self.oogen_OOClass13 = oogen_OOClass13
        
    @property
    def keep(self) -> bool:
        return self.__keep

    @keep.setter
    def keep(self, keep: bool):
        self.__keep = keep

    @property
    def languages(self) -> str:
        return self.__languages

    @languages.setter
    def languages(self, languages: str):
        self.__languages = languages

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def oogen_OOClass7(self):
        return self.__oogen_OOClass7

    @oogen_OOClass7.setter
    def oogen_OOClass7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOClass__oogen_OOClass7", None)
        self.__oogen_OOClass7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oogen_OOConstructor"):
                    opp_val = getattr(item, "oogen_OOConstructor", None)
                    
                    if opp_val == self:
                        setattr(item, "oogen_OOConstructor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oogen_OOConstructor"):
                    opp_val = getattr(item, "oogen_OOConstructor", None)
                    
                    setattr(item, "oogen_OOConstructor", self)
                    

    @property
    def oogen_OOClass13(self):
        return self.__oogen_OOClass13

    @oogen_OOClass13.setter
    def oogen_OOClass13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOClass__oogen_OOClass13", None)
        self.__oogen_OOClass13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oogen_OOType12"):
                opp_val = getattr(old_value, "oogen_OOType12", None)
                if opp_val == self:
                    setattr(old_value, "oogen_OOType12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oogen_OOType12"):
                opp_val = getattr(value, "oogen_OOType12", None)
                setattr(value, "oogen_OOType12", self)

    @property
    def OOClass(self):
        return self.__OOClass

    @OOClass.setter
    def OOClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOClass__OOClass", None)
        self.__OOClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "package"):
                opp_val = getattr(old_value, "package", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "package"):
                opp_val = getattr(value, "package", None)
                if opp_val is None:
                    setattr(value, "package", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def oogen_OOClass5(self):
        return self.__oogen_OOClass5

    @oogen_OOClass5.setter
    def oogen_OOClass5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOClass__oogen_OOClass5", None)
        self.__oogen_OOClass5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oogen_OOMethod"):
                    opp_val = getattr(item, "oogen_OOMethod", None)
                    
                    if opp_val == self:
                        setattr(item, "oogen_OOMethod", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oogen_OOMethod"):
                    opp_val = getattr(item, "oogen_OOMethod", None)
                    
                    setattr(item, "oogen_OOMethod", self)
                    

    @property
    def classes(self):
        return self.__classes

    @classes.setter
    def classes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOClass__classes", None)
        self.__classes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OOPackage"):
                opp_val = getattr(old_value, "OOPackage", None)
                if opp_val == self:
                    setattr(old_value, "OOPackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OOPackage"):
                opp_val = getattr(value, "OOPackage", None)
                setattr(value, "OOPackage", self)

    @property
    def oogen_OOClass(self):
        return self.__oogen_OOClass

    @oogen_OOClass.setter
    def oogen_OOClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOClass__oogen_OOClass", None)
        self.__oogen_OOClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oogen_OOMember"):
                    opp_val = getattr(item, "oogen_OOMember", None)
                    
                    if opp_val == self:
                        setattr(item, "oogen_OOMember", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oogen_OOMember"):
                    opp_val = getattr(item, "oogen_OOMember", None)
                    
                    setattr(item, "oogen_OOMember", self)
                    

class oogen_OOPackage:

    def __init__(self, name: str, package: set["oogen_OOClass"] = None, oogen_OOPackage: set["oogen_OOEnumeration"] = None, OOPackage: "oogen_OOClass" = None, oogen_OOPackage29: "oogen_OOModel" = None, oogen_OOPackage32: "oogen_OOModel" = None, oogen_OOPackage147: "oogen_OOEnumeration" = None):
        self.name = name
        self.package = package if package is not None else set()
        self.oogen_OOPackage = oogen_OOPackage if oogen_OOPackage is not None else set()
        self.OOPackage = OOPackage
        self.oogen_OOPackage29 = oogen_OOPackage29
        self.oogen_OOPackage32 = oogen_OOPackage32
        self.oogen_OOPackage147 = oogen_OOPackage147
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def oogen_OOPackage(self):
        return self.__oogen_OOPackage

    @oogen_OOPackage.setter
    def oogen_OOPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOPackage__oogen_OOPackage", None)
        self.__oogen_OOPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oogen_OOEnumeration"):
                    opp_val = getattr(item, "oogen_OOEnumeration", None)
                    
                    if opp_val == self:
                        setattr(item, "oogen_OOEnumeration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oogen_OOEnumeration"):
                    opp_val = getattr(item, "oogen_OOEnumeration", None)
                    
                    setattr(item, "oogen_OOEnumeration", self)
                    

    @property
    def oogen_OOPackage147(self):
        return self.__oogen_OOPackage147

    @oogen_OOPackage147.setter
    def oogen_OOPackage147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOPackage__oogen_OOPackage147", None)
        self.__oogen_OOPackage147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oogen_OOEnumeration146"):
                opp_val = getattr(old_value, "oogen_OOEnumeration146", None)
                if opp_val == self:
                    setattr(old_value, "oogen_OOEnumeration146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oogen_OOEnumeration146"):
                opp_val = getattr(value, "oogen_OOEnumeration146", None)
                setattr(value, "oogen_OOEnumeration146", self)

    @property
    def oogen_OOPackage32(self):
        return self.__oogen_OOPackage32

    @oogen_OOPackage32.setter
    def oogen_OOPackage32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOPackage__oogen_OOPackage32", None)
        self.__oogen_OOPackage32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oogen_OOModel31"):
                opp_val = getattr(old_value, "oogen_OOModel31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oogen_OOModel31"):
                opp_val = getattr(value, "oogen_OOModel31", None)
                if opp_val is None:
                    setattr(value, "oogen_OOModel31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def package(self):
        return self.__package

    @package.setter
    def package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOPackage__package", None)
        self.__package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OOClass"):
                    opp_val = getattr(item, "OOClass", None)
                    
                    if opp_val == self:
                        setattr(item, "OOClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OOClass"):
                    opp_val = getattr(item, "OOClass", None)
                    
                    setattr(item, "OOClass", self)
                    

    @property
    def oogen_OOPackage29(self):
        return self.__oogen_OOPackage29

    @oogen_OOPackage29.setter
    def oogen_OOPackage29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOPackage__oogen_OOPackage29", None)
        self.__oogen_OOPackage29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oogen_OOModel"):
                opp_val = getattr(old_value, "oogen_OOModel", None)
                if opp_val == self:
                    setattr(old_value, "oogen_OOModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oogen_OOModel"):
                opp_val = getattr(value, "oogen_OOModel", None)
                setattr(value, "oogen_OOModel", self)

    @property
    def OOPackage(self):
        return self.__OOPackage

    @OOPackage.setter
    def OOPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oogen_OOPackage__OOPackage", None)
        self.__OOPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes"):
                opp_val = getattr(old_value, "classes", None)
                if opp_val == self:
                    setattr(old_value, "classes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes"):
                opp_val = getattr(value, "classes", None)
                setattr(value, "classes", self)
