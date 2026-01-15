from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ETIOType(Enum):
    INPUT = "INPUT"
    OUTPUT = "OUTPUT"


############################################
# Definition of Classes
############################################

class ecdarText_EObject:

    pass
class ETExpression:

    pass
class ecdarText_ETLessEqualExpression(ETExpression):

    pass
class ecdarText_ETBitLeftAssignmentExpression(ETExpression):

    pass
class ecdarText_ETPreDecrementExpression(ETExpression):

    pass
class ecdarText_ETGreaterExpression(ETExpression):

    pass
class ecdarText_ETSubtractionAssignmentExpression(ETExpression):

    pass
class ecdarText_ETBitXORAssignmentExpression(ETExpression):

    pass
class ecdarText_ETMinusExpression(ETExpression):

    pass
class ecdarText_ETEqualExpression(ETExpression):

    pass
class ecdarText_ETConditionalExpression(ETExpression):

    pass
class ecdarText_ETExistsExpression(ETExpression):

    def __init__(self, name: str, ecdarText_ETExistsExpression: "ecdarText_ETType" = None, ecdarText_ETExistsExpression120: "ecdarText_ETExpression" = None):
        self.name = name
        self.ecdarText_ETExistsExpression = ecdarText_ETExistsExpression
        self.ecdarText_ETExistsExpression120 = ecdarText_ETExistsExpression120
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ecdarText_ETExistsExpression120(self):
        return self.__ecdarText_ETExistsExpression120

    @ecdarText_ETExistsExpression120.setter
    def ecdarText_ETExistsExpression120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETExistsExpression__ecdarText_ETExistsExpression120", None)
        self.__ecdarText_ETExistsExpression120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecdarText_ETExpression121"):
                opp_val = getattr(old_value, "ecdarText_ETExpression121", None)
                if opp_val == self:
                    setattr(old_value, "ecdarText_ETExpression121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecdarText_ETExpression121"):
                opp_val = getattr(value, "ecdarText_ETExpression121", None)
                setattr(value, "ecdarText_ETExpression121", self)

    @property
    def ecdarText_ETExistsExpression(self):
        return self.__ecdarText_ETExistsExpression

    @ecdarText_ETExistsExpression.setter
    def ecdarText_ETExistsExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETExistsExpression__ecdarText_ETExistsExpression", None)
        self.__ecdarText_ETExistsExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecdarText_ETType118"):
                opp_val = getattr(old_value, "ecdarText_ETType118", None)
                if opp_val == self:
                    setattr(old_value, "ecdarText_ETType118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecdarText_ETType118"):
                opp_val = getattr(value, "ecdarText_ETType118", None)
                setattr(value, "ecdarText_ETType118", self)

class ecdarText_ETNumberLiteral(ETExpression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class ecdarText_ETBitRightExpression(ETExpression):

    pass
class ecdarText_ETBitOrExpression(ETExpression):

    pass
class ecdarText_ETBitRightAssignmentExpression(ETExpression):

    pass
class ecdarText_ETUnequalExpression(ETExpression):

    pass
class ecdarText_ETStructExpression(ETExpression):

    def __init__(self, right: str, ecdarText_ETStructExpression: "ecdarText_ETExpression" = None):
        self.right = right
        self.ecdarText_ETStructExpression = ecdarText_ETStructExpression
        
    @property
    def right(self) -> str:
        return self.__right

    @right.setter
    def right(self, right: str):
        self.__right = right

    @property
    def ecdarText_ETStructExpression(self):
        return self.__ecdarText_ETStructExpression

    @ecdarText_ETStructExpression.setter
    def ecdarText_ETStructExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETStructExpression__ecdarText_ETStructExpression", None)
        self.__ecdarText_ETStructExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecdarText_ETExpression303"):
                opp_val = getattr(old_value, "ecdarText_ETExpression303", None)
                if opp_val == self:
                    setattr(old_value, "ecdarText_ETExpression303", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecdarText_ETExpression303"):
                opp_val = getattr(value, "ecdarText_ETExpression303", None)
                setattr(value, "ecdarText_ETExpression303", self)

class ecdarText_ETModuloExpression(ETExpression):

    pass
class ecdarText_ETMaxExpression(ETExpression):

    pass
class ecdarText_ETModuloAssignmentExpression(ETExpression):

    pass
class ecdarText_ETBooleanLiteral(ETExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ecdarText_ETBitLeftExpression(ETExpression):

    pass
class ecdarText_ETPostDecrementExpression(ETExpression):

    pass
class ecdarText_ETDivideExpression(ETExpression):

    pass
class ecdarText_ETBitXORExpression(ETExpression):

    pass
class ecdarText_ETPreIncrementExpression(ETExpression):

    pass
class ecdarText_ETDivisionAssignmentExpression(ETExpression):

    pass
class ecdarText_ETArrayExpression(ETExpression):

    pass
class ecdarText_ETMultiplicationAssignmentExpression(ETExpression):

    pass
class ecdarText_ETLessExpression(ETExpression):

    pass
class ecdarText_ETBitAndExpression(ETExpression):

    pass
class ecdarText_ETLogicNotExpression(ETExpression):

    pass
class ecdarText_ETPostIncrementExpression(ETExpression):

    pass
class ecdarText_ETSubtractExpression(ETExpression):

    pass
class ecdarText_ETMultiplyExpression(ETExpression):

    pass
class ecdarText_ETAddExpression(ETExpression):

    pass
class ecdarText_ETMinExpression(ETExpression):

    pass
class ecdarText_ETBitAndAssignmentExpression(ETExpression):

    pass
class ecdarText_ETReference(ETExpression):

    pass
class ecdarText_ETBitOrAssignmentExpression(ETExpression):

    pass
class ecdarText_ETGreaterEqualExpression(ETExpression):

    pass
class ecdarText_ETForallExpression(ETExpression):

    def __init__(self, name: str, ecdarText_ETForallExpression: "ecdarText_ETType" = None, ecdarText_ETForallExpression115: "ecdarText_ETExpression" = None):
        self.name = name
        self.ecdarText_ETForallExpression = ecdarText_ETForallExpression
        self.ecdarText_ETForallExpression115 = ecdarText_ETForallExpression115
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ecdarText_ETForallExpression115(self):
        return self.__ecdarText_ETForallExpression115

    @ecdarText_ETForallExpression115.setter
    def ecdarText_ETForallExpression115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETForallExpression__ecdarText_ETForallExpression115", None)
        self.__ecdarText_ETForallExpression115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecdarText_ETExpression116"):
                opp_val = getattr(old_value, "ecdarText_ETExpression116", None)
                if opp_val == self:
                    setattr(old_value, "ecdarText_ETExpression116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecdarText_ETExpression116"):
                opp_val = getattr(value, "ecdarText_ETExpression116", None)
                setattr(value, "ecdarText_ETExpression116", self)

    @property
    def ecdarText_ETForallExpression(self):
        return self.__ecdarText_ETForallExpression

    @ecdarText_ETForallExpression.setter
    def ecdarText_ETForallExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETForallExpression__ecdarText_ETForallExpression", None)
        self.__ecdarText_ETForallExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecdarText_ETType113"):
                opp_val = getattr(old_value, "ecdarText_ETType113", None)
                if opp_val == self:
                    setattr(old_value, "ecdarText_ETType113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecdarText_ETType113"):
                opp_val = getattr(value, "ecdarText_ETType113", None)
                setattr(value, "ecdarText_ETType113", self)

class ecdarText_ETAdditionAssignmentExpression(ETExpression):

    pass
class ecdarText_ETAssignmentExpression(ETExpression):

    pass
class ecdarText_ETLogicAndExpression(ETExpression):

    pass
class ecdarText_ETLogicOrExpression(ETExpression):

    pass
class ecdarText_ETImplyExpression(ETExpression):

    pass
class ETSpecificationExpression:

    pass
class ecdarText_ETSpecificationInstantiation(ETSpecificationExpression):

    pass
class ecdarText_ETSpecificationConjunctionExpression(ETSpecificationExpression):

    pass
class ecdarText_ETSpecificationReference(ETSpecificationExpression):

    pass
class ecdarText_ETSpecificationCompositionExpression(ETSpecificationExpression):

    pass
class ecdarText_ETSpecificationDisjunctionExpression(ETSpecificationExpression):

    pass
class ecdarText_ETLocation:

    def __init__(self, urgent: bool, universal: bool, name: str, ecdarText_ETLocation65: set["ecdarText_ETExpression"] = None, ecdarText_ETLocation68: set["ecdarText_ETEdge"] = None, ecdarText_ETLocation78: "ecdarText_ETEdge" = None, ecdarText_ETLocation: "ecdarText_ETSpecificationBody" = None, ecdarText_ETLocation57: "ecdarText_ETSpecificationBody" = None):
        self.urgent = urgent
        self.universal = universal
        self.name = name
        self.ecdarText_ETLocation65 = ecdarText_ETLocation65 if ecdarText_ETLocation65 is not None else set()
        self.ecdarText_ETLocation68 = ecdarText_ETLocation68 if ecdarText_ETLocation68 is not None else set()
        self.ecdarText_ETLocation78 = ecdarText_ETLocation78
        self.ecdarText_ETLocation = ecdarText_ETLocation
        self.ecdarText_ETLocation57 = ecdarText_ETLocation57
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def universal(self) -> bool:
        return self.__universal

    @universal.setter
    def universal(self, universal: bool):
        self.__universal = universal

    @property
    def urgent(self) -> bool:
        return self.__urgent

    @urgent.setter
    def urgent(self, urgent: bool):
        self.__urgent = urgent

    @property
    def ecdarText_ETLocation65(self):
        return self.__ecdarText_ETLocation65

    @ecdarText_ETLocation65.setter
    def ecdarText_ETLocation65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETLocation__ecdarText_ETLocation65", None)
        self.__ecdarText_ETLocation65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecdarText_ETExpression66"):
                    opp_val = getattr(item, "ecdarText_ETExpression66", None)
                    
                    if opp_val == self:
                        setattr(item, "ecdarText_ETExpression66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecdarText_ETExpression66"):
                    opp_val = getattr(item, "ecdarText_ETExpression66", None)
                    
                    setattr(item, "ecdarText_ETExpression66", self)
                    

    @property
    def ecdarText_ETLocation78(self):
        return self.__ecdarText_ETLocation78

    @ecdarText_ETLocation78.setter
    def ecdarText_ETLocation78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETLocation__ecdarText_ETLocation78", None)
        self.__ecdarText_ETLocation78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecdarText_ETEdge77"):
                opp_val = getattr(old_value, "ecdarText_ETEdge77", None)
                if opp_val == self:
                    setattr(old_value, "ecdarText_ETEdge77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecdarText_ETEdge77"):
                opp_val = getattr(value, "ecdarText_ETEdge77", None)
                setattr(value, "ecdarText_ETEdge77", self)

    @property
    def ecdarText_ETLocation(self):
        return self.__ecdarText_ETLocation

    @ecdarText_ETLocation.setter
    def ecdarText_ETLocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETLocation__ecdarText_ETLocation", None)
        self.__ecdarText_ETLocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecdarText_ETSpecificationBody54"):
                opp_val = getattr(old_value, "ecdarText_ETSpecificationBody54", None)
                if opp_val == self:
                    setattr(old_value, "ecdarText_ETSpecificationBody54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecdarText_ETSpecificationBody54"):
                opp_val = getattr(value, "ecdarText_ETSpecificationBody54", None)
                setattr(value, "ecdarText_ETSpecificationBody54", self)

    @property
    def ecdarText_ETLocation68(self):
        return self.__ecdarText_ETLocation68

    @ecdarText_ETLocation68.setter
    def ecdarText_ETLocation68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETLocation__ecdarText_ETLocation68", None)
        self.__ecdarText_ETLocation68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecdarText_ETEdge"):
                    opp_val = getattr(item, "ecdarText_ETEdge", None)
                    
                    if opp_val == self:
                        setattr(item, "ecdarText_ETEdge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecdarText_ETEdge"):
                    opp_val = getattr(item, "ecdarText_ETEdge", None)
                    
                    setattr(item, "ecdarText_ETEdge", self)
                    

    @property
    def ecdarText_ETLocation57(self):
        return self.__ecdarText_ETLocation57

    @ecdarText_ETLocation57.setter
    def ecdarText_ETLocation57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETLocation__ecdarText_ETLocation57", None)
        self.__ecdarText_ETLocation57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecdarText_ETSpecificationBody56"):
                opp_val = getattr(old_value, "ecdarText_ETSpecificationBody56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecdarText_ETSpecificationBody56"):
                opp_val = getattr(value, "ecdarText_ETSpecificationBody56", None)
                if opp_val is None:
                    setattr(value, "ecdarText_ETSpecificationBody56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ecdarText_ETParameter:

    def __init__(self, name: str, ioType: str, ecdarText_ETParameter59: "ecdarText_ETType" = None, ecdarText_ETParameter62: set["ecdarText_ETArrayDeclaration"] = None, ecdarText_ETParameter: "ecdarText_ETSpecificationTemplate" = None):
        self.name = name
        self.ioType = ioType
        self.ecdarText_ETParameter59 = ecdarText_ETParameter59
        self.ecdarText_ETParameter62 = ecdarText_ETParameter62 if ecdarText_ETParameter62 is not None else set()
        self.ecdarText_ETParameter = ecdarText_ETParameter
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ioType(self) -> str:
        return self.__ioType

    @ioType.setter
    def ioType(self, ioType: str):
        self.__ioType = ioType

    @property
    def ecdarText_ETParameter62(self):
        return self.__ecdarText_ETParameter62

    @ecdarText_ETParameter62.setter
    def ecdarText_ETParameter62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETParameter__ecdarText_ETParameter62", None)
        self.__ecdarText_ETParameter62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecdarText_ETArrayDeclaration63"):
                    opp_val = getattr(item, "ecdarText_ETArrayDeclaration63", None)
                    
                    if opp_val == self:
                        setattr(item, "ecdarText_ETArrayDeclaration63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecdarText_ETArrayDeclaration63"):
                    opp_val = getattr(item, "ecdarText_ETArrayDeclaration63", None)
                    
                    setattr(item, "ecdarText_ETArrayDeclaration63", self)
                    

    @property
    def ecdarText_ETParameter59(self):
        return self.__ecdarText_ETParameter59

    @ecdarText_ETParameter59.setter
    def ecdarText_ETParameter59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETParameter__ecdarText_ETParameter59", None)
        self.__ecdarText_ETParameter59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecdarText_ETType60"):
                opp_val = getattr(old_value, "ecdarText_ETType60", None)
                if opp_val == self:
                    setattr(old_value, "ecdarText_ETType60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecdarText_ETType60"):
                opp_val = getattr(value, "ecdarText_ETType60", None)
                setattr(value, "ecdarText_ETType60", self)

    @property
    def ecdarText_ETParameter(self):
        return self.__ecdarText_ETParameter

    @ecdarText_ETParameter.setter
    def ecdarText_ETParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETParameter__ecdarText_ETParameter", None)
        self.__ecdarText_ETParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecdarText_ETSpecificationTemplate"):
                opp_val = getattr(old_value, "ecdarText_ETSpecificationTemplate", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecdarText_ETSpecificationTemplate"):
                opp_val = getattr(value, "ecdarText_ETSpecificationTemplate", None)
                if opp_val is None:
                    setattr(value, "ecdarText_ETSpecificationTemplate", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ecdarText_ETIO:

    def __init__(self, type: str, ecdarText_ETIO: "ecdarText_ETEdge" = None, ecdarText_ETIO83: "ecdarText_ETExpression" = None):
        self.type = type
        self.ecdarText_ETIO = ecdarText_ETIO
        self.ecdarText_ETIO83 = ecdarText_ETIO83
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def ecdarText_ETIO(self):
        return self.__ecdarText_ETIO

    @ecdarText_ETIO.setter
    def ecdarText_ETIO(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETIO__ecdarText_ETIO", None)
        self.__ecdarText_ETIO = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecdarText_ETEdge72"):
                opp_val = getattr(old_value, "ecdarText_ETEdge72", None)
                if opp_val == self:
                    setattr(old_value, "ecdarText_ETEdge72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecdarText_ETEdge72"):
                opp_val = getattr(value, "ecdarText_ETEdge72", None)
                setattr(value, "ecdarText_ETEdge72", self)

    @property
    def ecdarText_ETIO83(self):
        return self.__ecdarText_ETIO83

    @ecdarText_ETIO83.setter
    def ecdarText_ETIO83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETIO__ecdarText_ETIO83", None)
        self.__ecdarText_ETIO83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecdarText_ETExpression84"):
                opp_val = getattr(old_value, "ecdarText_ETExpression84", None)
                if opp_val == self:
                    setattr(old_value, "ecdarText_ETExpression84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecdarText_ETExpression84"):
                opp_val = getattr(value, "ecdarText_ETExpression84", None)
                setattr(value, "ecdarText_ETExpression84", self)

class ecdarText_ETSelect:

    def __init__(self, name: str, ecdarText_ETSelect: "ecdarText_ETEdge" = None, ecdarText_ETSelect86: "ecdarText_ETType" = None):
        self.name = name
        self.ecdarText_ETSelect = ecdarText_ETSelect
        self.ecdarText_ETSelect86 = ecdarText_ETSelect86
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ecdarText_ETSelect86(self):
        return self.__ecdarText_ETSelect86

    @ecdarText_ETSelect86.setter
    def ecdarText_ETSelect86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETSelect__ecdarText_ETSelect86", None)
        self.__ecdarText_ETSelect86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecdarText_ETType87"):
                opp_val = getattr(old_value, "ecdarText_ETType87", None)
                if opp_val == self:
                    setattr(old_value, "ecdarText_ETType87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecdarText_ETType87"):
                opp_val = getattr(value, "ecdarText_ETType87", None)
                setattr(value, "ecdarText_ETType87", self)

    @property
    def ecdarText_ETSelect(self):
        return self.__ecdarText_ETSelect

    @ecdarText_ETSelect.setter
    def ecdarText_ETSelect(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETSelect__ecdarText_ETSelect", None)
        self.__ecdarText_ETSelect = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecdarText_ETEdge70"):
                opp_val = getattr(old_value, "ecdarText_ETEdge70", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecdarText_ETEdge70"):
                opp_val = getattr(value, "ecdarText_ETEdge70", None)
                if opp_val is None:
                    setattr(value, "ecdarText_ETEdge70", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ecdarText_ETEdge:

    def __init__(self, controllable: bool, ecdarText_ETEdge: "ecdarText_ETLocation" = None, ecdarText_ETEdge70: set["ecdarText_ETSelect"] = None, ecdarText_ETEdge72: "ecdarText_ETIO" = None, ecdarText_ETEdge74: "ecdarText_ETExpression" = None, ecdarText_ETEdge77: "ecdarText_ETLocation" = None, ecdarText_ETEdge80: set["ecdarText_ETExpression"] = None):
        self.controllable = controllable
        self.ecdarText_ETEdge = ecdarText_ETEdge
        self.ecdarText_ETEdge70 = ecdarText_ETEdge70 if ecdarText_ETEdge70 is not None else set()
        self.ecdarText_ETEdge72 = ecdarText_ETEdge72
        self.ecdarText_ETEdge74 = ecdarText_ETEdge74
        self.ecdarText_ETEdge77 = ecdarText_ETEdge77
        self.ecdarText_ETEdge80 = ecdarText_ETEdge80 if ecdarText_ETEdge80 is not None else set()
        
    @property
    def controllable(self) -> bool:
        return self.__controllable

    @controllable.setter
    def controllable(self, controllable: bool):
        self.__controllable = controllable

    @property
    def ecdarText_ETEdge74(self):
        return self.__ecdarText_ETEdge74

    @ecdarText_ETEdge74.setter
    def ecdarText_ETEdge74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETEdge__ecdarText_ETEdge74", None)
        self.__ecdarText_ETEdge74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecdarText_ETExpression75"):
                opp_val = getattr(old_value, "ecdarText_ETExpression75", None)
                if opp_val == self:
                    setattr(old_value, "ecdarText_ETExpression75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecdarText_ETExpression75"):
                opp_val = getattr(value, "ecdarText_ETExpression75", None)
                setattr(value, "ecdarText_ETExpression75", self)

    @property
    def ecdarText_ETEdge77(self):
        return self.__ecdarText_ETEdge77

    @ecdarText_ETEdge77.setter
    def ecdarText_ETEdge77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETEdge__ecdarText_ETEdge77", None)
        self.__ecdarText_ETEdge77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecdarText_ETLocation78"):
                opp_val = getattr(old_value, "ecdarText_ETLocation78", None)
                if opp_val == self:
                    setattr(old_value, "ecdarText_ETLocation78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecdarText_ETLocation78"):
                opp_val = getattr(value, "ecdarText_ETLocation78", None)
                setattr(value, "ecdarText_ETLocation78", self)

    @property
    def ecdarText_ETEdge70(self):
        return self.__ecdarText_ETEdge70

    @ecdarText_ETEdge70.setter
    def ecdarText_ETEdge70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETEdge__ecdarText_ETEdge70", None)
        self.__ecdarText_ETEdge70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecdarText_ETSelect"):
                    opp_val = getattr(item, "ecdarText_ETSelect", None)
                    
                    if opp_val == self:
                        setattr(item, "ecdarText_ETSelect", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecdarText_ETSelect"):
                    opp_val = getattr(item, "ecdarText_ETSelect", None)
                    
                    setattr(item, "ecdarText_ETSelect", self)
                    

    @property
    def ecdarText_ETEdge(self):
        return self.__ecdarText_ETEdge

    @ecdarText_ETEdge.setter
    def ecdarText_ETEdge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETEdge__ecdarText_ETEdge", None)
        self.__ecdarText_ETEdge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecdarText_ETLocation68"):
                opp_val = getattr(old_value, "ecdarText_ETLocation68", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecdarText_ETLocation68"):
                opp_val = getattr(value, "ecdarText_ETLocation68", None)
                if opp_val is None:
                    setattr(value, "ecdarText_ETLocation68", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecdarText_ETEdge80(self):
        return self.__ecdarText_ETEdge80

    @ecdarText_ETEdge80.setter
    def ecdarText_ETEdge80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETEdge__ecdarText_ETEdge80", None)
        self.__ecdarText_ETEdge80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecdarText_ETExpression81"):
                    opp_val = getattr(item, "ecdarText_ETExpression81", None)
                    
                    if opp_val == self:
                        setattr(item, "ecdarText_ETExpression81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecdarText_ETExpression81"):
                    opp_val = getattr(item, "ecdarText_ETExpression81", None)
                    
                    setattr(item, "ecdarText_ETExpression81", self)
                    

    @property
    def ecdarText_ETEdge72(self):
        return self.__ecdarText_ETEdge72

    @ecdarText_ETEdge72.setter
    def ecdarText_ETEdge72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETEdge__ecdarText_ETEdge72", None)
        self.__ecdarText_ETEdge72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecdarText_ETIO"):
                opp_val = getattr(old_value, "ecdarText_ETIO", None)
                if opp_val == self:
                    setattr(old_value, "ecdarText_ETIO", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecdarText_ETIO"):
                opp_val = getattr(value, "ecdarText_ETIO", None)
                setattr(value, "ecdarText_ETIO", self)

class ETSpecificationDefinition:

    pass
class ecdarText_ETSpecificationTemplate(ETSpecificationDefinition):

    pass
class ecdarText_ETSpecificationBody:

    pass
class ETSpecification:

    pass
class ecdarText_ETSpecificationDefinition(ETSpecification):

    pass
class ecdarText_ETSpecificationBinding(ETSpecification):

    pass
class ecdarText_ETSpecificationExpression:

    pass
class ecdarText_ETFieldID:

    def __init__(self, name: str, ioType: str, ecdarText_ETFieldID: "ecdarText_ETFieldDeclaration" = None, ecdarText_ETFieldID45: set["ecdarText_ETArrayDeclaration"] = None):
        self.name = name
        self.ioType = ioType
        self.ecdarText_ETFieldID = ecdarText_ETFieldID
        self.ecdarText_ETFieldID45 = ecdarText_ETFieldID45 if ecdarText_ETFieldID45 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ioType(self) -> str:
        return self.__ioType

    @ioType.setter
    def ioType(self, ioType: str):
        self.__ioType = ioType

    @property
    def ecdarText_ETFieldID(self):
        return self.__ecdarText_ETFieldID

    @ecdarText_ETFieldID.setter
    def ecdarText_ETFieldID(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETFieldID__ecdarText_ETFieldID", None)
        self.__ecdarText_ETFieldID = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecdarText_ETFieldDeclaration43"):
                opp_val = getattr(old_value, "ecdarText_ETFieldDeclaration43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecdarText_ETFieldDeclaration43"):
                opp_val = getattr(value, "ecdarText_ETFieldDeclaration43", None)
                if opp_val is None:
                    setattr(value, "ecdarText_ETFieldDeclaration43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecdarText_ETFieldID45(self):
        return self.__ecdarText_ETFieldID45

    @ecdarText_ETFieldID45.setter
    def ecdarText_ETFieldID45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETFieldID__ecdarText_ETFieldID45", None)
        self.__ecdarText_ETFieldID45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecdarText_ETArrayDeclaration46"):
                    opp_val = getattr(item, "ecdarText_ETArrayDeclaration46", None)
                    
                    if opp_val == self:
                        setattr(item, "ecdarText_ETArrayDeclaration46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecdarText_ETArrayDeclaration46"):
                    opp_val = getattr(item, "ecdarText_ETArrayDeclaration46", None)
                    
                    setattr(item, "ecdarText_ETArrayDeclaration46", self)
                    

class ecdarText_ETFieldDeclaration:

    pass
class ETActionType:

    pass
class ecdarText_ETOutputType(ETActionType):

    pass
class ecdarText_ETInputType(ETActionType):

    pass
class ETTypeIdentifier:

    pass
class ecdarText_ETScalarType(ETTypeIdentifier):

    pass
class ecdarText_ETBooleanType(ETTypeIdentifier):

    pass
class ecdarText_ETActionType(ETTypeIdentifier):

    pass
class ecdarText_ETClockType(ETTypeIdentifier):

    pass
class ecdarText_ETStructType(ETTypeIdentifier):

    pass
class ecdarText_ETTypeReference(ETTypeIdentifier):

    pass
class ecdarText_ETIntegerType(ETTypeIdentifier):

    pass
class ecdarText_ETTypeID:

    def __init__(self, name: str, ecdarText_ETTypeID: "ecdarText_ETTypeDeclaration" = None, ecdarText_ETTypeID29: set["ecdarText_ETArrayDeclaration"] = None, ecdarText_ETTypeID89: "ecdarText_ETTypeReference" = None):
        self.name = name
        self.ecdarText_ETTypeID = ecdarText_ETTypeID
        self.ecdarText_ETTypeID29 = ecdarText_ETTypeID29 if ecdarText_ETTypeID29 is not None else set()
        self.ecdarText_ETTypeID89 = ecdarText_ETTypeID89
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ecdarText_ETTypeID29(self):
        return self.__ecdarText_ETTypeID29

    @ecdarText_ETTypeID29.setter
    def ecdarText_ETTypeID29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETTypeID__ecdarText_ETTypeID29", None)
        self.__ecdarText_ETTypeID29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecdarText_ETArrayDeclaration30"):
                    opp_val = getattr(item, "ecdarText_ETArrayDeclaration30", None)
                    
                    if opp_val == self:
                        setattr(item, "ecdarText_ETArrayDeclaration30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecdarText_ETArrayDeclaration30"):
                    opp_val = getattr(item, "ecdarText_ETArrayDeclaration30", None)
                    
                    setattr(item, "ecdarText_ETArrayDeclaration30", self)
                    

    @property
    def ecdarText_ETTypeID89(self):
        return self.__ecdarText_ETTypeID89

    @ecdarText_ETTypeID89.setter
    def ecdarText_ETTypeID89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETTypeID__ecdarText_ETTypeID89", None)
        self.__ecdarText_ETTypeID89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecdarText_ETTypeReference"):
                opp_val = getattr(old_value, "ecdarText_ETTypeReference", None)
                if opp_val == self:
                    setattr(old_value, "ecdarText_ETTypeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecdarText_ETTypeReference"):
                opp_val = getattr(value, "ecdarText_ETTypeReference", None)
                setattr(value, "ecdarText_ETTypeReference", self)

    @property
    def ecdarText_ETTypeID(self):
        return self.__ecdarText_ETTypeID

    @ecdarText_ETTypeID.setter
    def ecdarText_ETTypeID(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETTypeID__ecdarText_ETTypeID", None)
        self.__ecdarText_ETTypeID = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecdarText_ETTypeDeclaration27"):
                opp_val = getattr(old_value, "ecdarText_ETTypeDeclaration27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecdarText_ETTypeDeclaration27"):
                opp_val = getattr(value, "ecdarText_ETTypeDeclaration27", None)
                if opp_val is None:
                    setattr(value, "ecdarText_ETTypeDeclaration27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ecdarText_ETTypeIdentifier:

    pass
class ecdarText_ETTypeModifiers:

    def __init__(self, urgent: bool, meta: bool, const: bool, ecdarText_ETTypeModifiers: "ecdarText_ETType" = None):
        self.urgent = urgent
        self.meta = meta
        self.const = const
        self.ecdarText_ETTypeModifiers = ecdarText_ETTypeModifiers
        
    @property
    def urgent(self) -> bool:
        return self.__urgent

    @urgent.setter
    def urgent(self, urgent: bool):
        self.__urgent = urgent

    @property
    def meta(self) -> bool:
        return self.__meta

    @meta.setter
    def meta(self, meta: bool):
        self.__meta = meta

    @property
    def const(self) -> bool:
        return self.__const

    @const.setter
    def const(self, const: bool):
        self.__const = const

    @property
    def ecdarText_ETTypeModifiers(self):
        return self.__ecdarText_ETTypeModifiers

    @ecdarText_ETTypeModifiers.setter
    def ecdarText_ETTypeModifiers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETTypeModifiers__ecdarText_ETTypeModifiers", None)
        self.__ecdarText_ETTypeModifiers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecdarText_ETType"):
                opp_val = getattr(old_value, "ecdarText_ETType", None)
                if opp_val == self:
                    setattr(old_value, "ecdarText_ETType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecdarText_ETType"):
                opp_val = getattr(value, "ecdarText_ETType", None)
                setattr(value, "ecdarText_ETType", self)

class ecdarText_ETType:

    pass
class ETInitialiser:

    pass
class ecdarText_ETMultiInitialiser(ETInitialiser):

    pass
class ecdarText_ETSingleInitialiser(ETInitialiser):

    pass
class ecdarText_ETInitialiser:

    pass
class ecdarText_ETVariableID:

    def __init__(self, name: str, ioType: str, ecdarText_ETVariableID: "ecdarText_ETVariableDeclaration" = None, ecdarText_ETVariableID16: set["ecdarText_ETArrayDeclaration"] = None, ecdarText_ETVariableID19: "ecdarText_ETInitialiser" = None):
        self.name = name
        self.ioType = ioType
        self.ecdarText_ETVariableID = ecdarText_ETVariableID
        self.ecdarText_ETVariableID16 = ecdarText_ETVariableID16 if ecdarText_ETVariableID16 is not None else set()
        self.ecdarText_ETVariableID19 = ecdarText_ETVariableID19
        
    @property
    def ioType(self) -> str:
        return self.__ioType

    @ioType.setter
    def ioType(self, ioType: str):
        self.__ioType = ioType

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ecdarText_ETVariableID16(self):
        return self.__ecdarText_ETVariableID16

    @ecdarText_ETVariableID16.setter
    def ecdarText_ETVariableID16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETVariableID__ecdarText_ETVariableID16", None)
        self.__ecdarText_ETVariableID16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecdarText_ETArrayDeclaration17"):
                    opp_val = getattr(item, "ecdarText_ETArrayDeclaration17", None)
                    
                    if opp_val == self:
                        setattr(item, "ecdarText_ETArrayDeclaration17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecdarText_ETArrayDeclaration17"):
                    opp_val = getattr(item, "ecdarText_ETArrayDeclaration17", None)
                    
                    setattr(item, "ecdarText_ETArrayDeclaration17", self)
                    

    @property
    def ecdarText_ETVariableID19(self):
        return self.__ecdarText_ETVariableID19

    @ecdarText_ETVariableID19.setter
    def ecdarText_ETVariableID19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETVariableID__ecdarText_ETVariableID19", None)
        self.__ecdarText_ETVariableID19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecdarText_ETInitialiser"):
                opp_val = getattr(old_value, "ecdarText_ETInitialiser", None)
                if opp_val == self:
                    setattr(old_value, "ecdarText_ETInitialiser", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecdarText_ETInitialiser"):
                opp_val = getattr(value, "ecdarText_ETInitialiser", None)
                setattr(value, "ecdarText_ETInitialiser", self)

    @property
    def ecdarText_ETVariableID(self):
        return self.__ecdarText_ETVariableID

    @ecdarText_ETVariableID.setter
    def ecdarText_ETVariableID(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETVariableID__ecdarText_ETVariableID", None)
        self.__ecdarText_ETVariableID = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecdarText_ETVariableDeclaration14"):
                opp_val = getattr(old_value, "ecdarText_ETVariableDeclaration14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecdarText_ETVariableDeclaration14"):
                opp_val = getattr(value, "ecdarText_ETVariableDeclaration14", None)
                if opp_val is None:
                    setattr(value, "ecdarText_ETVariableDeclaration14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ETDeclaration:

    pass
class ecdarText_ETTypeDeclaration(ETDeclaration):

    pass
class ecdarText_ETVariableDeclaration(ETDeclaration):

    pass
class ecdarText_ETDeclaration:

    pass
class ecdarText_ETExpression:

    pass
class ecdarText_ETArrayDeclaration:

    pass
class ecdarText_ETSpecification:

    def __init__(self, name: str, ecdarText_ETSpecification: "ecdarText_ETFile" = None, ecdarText_ETSpecification106: "ecdarText_ETSpecificationReference" = None):
        self.name = name
        self.ecdarText_ETSpecification = ecdarText_ETSpecification
        self.ecdarText_ETSpecification106 = ecdarText_ETSpecification106
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ecdarText_ETSpecification106(self):
        return self.__ecdarText_ETSpecification106

    @ecdarText_ETSpecification106.setter
    def ecdarText_ETSpecification106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETSpecification__ecdarText_ETSpecification106", None)
        self.__ecdarText_ETSpecification106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecdarText_ETSpecificationReference"):
                opp_val = getattr(old_value, "ecdarText_ETSpecificationReference", None)
                if opp_val == self:
                    setattr(old_value, "ecdarText_ETSpecificationReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecdarText_ETSpecificationReference"):
                opp_val = getattr(value, "ecdarText_ETSpecificationReference", None)
                setattr(value, "ecdarText_ETSpecificationReference", self)

    @property
    def ecdarText_ETSpecification(self):
        return self.__ecdarText_ETSpecification

    @ecdarText_ETSpecification.setter
    def ecdarText_ETSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETSpecification__ecdarText_ETSpecification", None)
        self.__ecdarText_ETSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecdarText_ETFile4"):
                opp_val = getattr(old_value, "ecdarText_ETFile4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecdarText_ETFile4"):
                opp_val = getattr(value, "ecdarText_ETFile4", None)
                if opp_val is None:
                    setattr(value, "ecdarText_ETFile4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ecdarText_ETDeclarations:

    pass
class ecdarText_ETImport:

    def __init__(self, importedNamespace: str, ecdarText_ETImport: "ecdarText_ETFile" = None):
        self.importedNamespace = importedNamespace
        self.ecdarText_ETImport = ecdarText_ETImport
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

    @property
    def ecdarText_ETImport(self):
        return self.__ecdarText_ETImport

    @ecdarText_ETImport.setter
    def ecdarText_ETImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecdarText_ETImport__ecdarText_ETImport", None)
        self.__ecdarText_ETImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecdarText_ETFile"):
                opp_val = getattr(old_value, "ecdarText_ETFile", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecdarText_ETFile"):
                opp_val = getattr(value, "ecdarText_ETFile", None)
                if opp_val is None:
                    setattr(value, "ecdarText_ETFile", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ecdarText_ETFile:

    pass