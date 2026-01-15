from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class OclModelElement:

    pass
class OclFeature:

    pass
class OCL_Attribute(OclFeature):

    def __init__(self, name: str, 1303: "OclType" = None, 1300: "OclExpression" = None, ATL.ecore#286: "OCL_OclFeatureDefinition"):
        self.name = name
        self.1303 = 1303
        self.1300 = 1300
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 1300(self):
        return self.__1300

    @1300.setter
    def 1300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Attribute__1300", None)
        self.__1300 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL.ecore#301"):
                opp_val = getattr(old_value, "ATL.ecore#301", None)
                if opp_val == self:
                    setattr(old_value, "ATL.ecore#301", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL.ecore#301"):
                opp_val = getattr(value, "ATL.ecore#301", None)
                setattr(value, "ATL.ecore#301", self)

    @property
    def 1303(self):
        return self.__1303

    @1303.setter
    def 1303(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Attribute__1303", None)
        self.__1303 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL.ecore#304"):
                opp_val = getattr(old_value, "ATL.ecore#304", None)
                if opp_val == self:
                    setattr(old_value, "ATL.ecore#304", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL.ecore#304"):
                opp_val = getattr(value, "ATL.ecore#304", None)
                setattr(value, "ATL.ecore#304", self)

class OCL_Operation(OclFeature):

    def __init__(self, name: str, 1306: set["Parameter"] = None, 1309: "OclType" = None, 1312: "OclExpression" = None, ATL.ecore#286: "OCL_OclFeatureDefinition"):
        self.name = name
        self.1306 = 1306 if 1306 is not None else set()
        self.1309 = 1309
        self.1312 = 1312
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 1312(self):
        return self.__1312

    @1312.setter
    def 1312(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Operation__1312", None)
        self.__1312 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL.ecore#313"):
                opp_val = getattr(old_value, "ATL.ecore#313", None)
                if opp_val == self:
                    setattr(old_value, "ATL.ecore#313", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL.ecore#313"):
                opp_val = getattr(value, "ATL.ecore#313", None)
                setattr(value, "ATL.ecore#313", self)

    @property
    def 1309(self):
        return self.__1309

    @1309.setter
    def 1309(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Operation__1309", None)
        self.__1309 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL.ecore#310"):
                opp_val = getattr(old_value, "ATL.ecore#310", None)
                if opp_val == self:
                    setattr(old_value, "ATL.ecore#310", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL.ecore#310"):
                opp_val = getattr(value, "ATL.ecore#310", None)
                setattr(value, "ATL.ecore#310", self)

    @property
    def 1306(self):
        return self.__1306

    @1306.setter
    def 1306(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Operation__1306", None)
        self.__1306 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ATL.ecore#307"):
                    opp_val = getattr(item, "ATL.ecore#307", None)
                    
                    if opp_val == self:
                        setattr(item, "ATL.ecore#307", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ATL.ecore#307"):
                    opp_val = getattr(item, "ATL.ecore#307", None)
                    
                    setattr(item, "ATL.ecore#307", self)
                    

class TupleType:

    pass
class NumericType:

    pass
class OCL_RealType(NumericType):

    pass
class OCL_IntegerType(NumericType):

    pass
class TupleTypeAttribute:

    pass
class CollectionType:

    pass
class OCL_BagType(CollectionType):

    pass
class OCL_SetType(CollectionType):

    pass
class OCL_SequenceType(CollectionType):

    pass
class OCL_OrderedSetType(CollectionType):

    pass
class MapType:

    pass
class OclContextDefinition:

    pass
class Primitive:

    pass
class OCL_BooleanType(Primitive):

    pass
class OCL_NumericType(Primitive):

    pass
class OCL_StringType(Primitive):

    pass
class VariableExp:

    pass
class IterateExp:

    pass
class MapExp:

    pass
class MapElement:

    pass
class TupleExp:

    pass
class TuplePart:

    pass
class NumericExp:

    pass
class OCL_IntegerExp(NumericExp):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
    @property
    def integerSymbol(self) -> str:
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol

class OCL_RealExp(NumericExp):

    def __init__(self, realSymbol: str):
        self.realSymbol = realSymbol
        
    @property
    def realSymbol(self) -> str:
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: str):
        self.__realSymbol = realSymbol

class PrimitiveExp:

    pass
class OCL_NumericExp(PrimitiveExp):

    pass
class OCL_BooleanExp(PrimitiveExp):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
    @property
    def booleanSymbol(self) -> str:
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol

class OCL_StringExp(PrimitiveExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
    @property
    def stringSymbol(self) -> str:
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol

class Attribute:

    pass
class Operation:

    pass
class LetExp:

    pass
class CollectionExp:

    pass
class OCL_SequenceExp(CollectionExp):

    pass
class OCL_OrderedSetExp(CollectionExp):

    pass
class OCL_BagExp(CollectionExp):

    pass
class OCL_SetExp(CollectionExp):

    pass
class PropertyCallExp:

    pass
class OCL_OperationCallExp(PropertyCallExp):

    def __init__(self, operationName: str, 1189: set["OclExpression"] = None, ATL.ecore#134: "OCL_OclExpression"):
        self.operationName = operationName
        self.1189 = 1189 if 1189 is not None else set()
        
    @property
    def operationName(self) -> str:
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName

    @property
    def 1189(self):
        return self.__1189

    @1189.setter
    def 1189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OperationCallExp__1189", None)
        self.__1189 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ATL.ecore#190"):
                    opp_val = getattr(item, "ATL.ecore#190", None)
                    
                    if opp_val == self:
                        setattr(item, "ATL.ecore#190", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ATL.ecore#190"):
                    opp_val = getattr(item, "ATL.ecore#190", None)
                    
                    setattr(item, "ATL.ecore#190", self)
                    

class OCL_LoopExp(PropertyCallExp):

    pass
class OCL_NavigationOrAttributeCallExp(PropertyCallExp):

    def __init__(self, name: str, ATL.ecore#134: "OCL_OclExpression"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class IfExp:

    pass
class OclType:

    pass
class OCL_MapType(OclType):

    pass
class OCL_Primitive(OclType):

    pass
class OCL_TupleType(OclType):

    pass
class OCL_CollectionType(OclType):

    pass
class OCL_OclAnyType(OclType):

    pass
class OCL_OclModelElement(OclType):

    pass
class OperationCallExp:

    pass
class OCL_CollectionOperationCallExp(OperationCallExp):

    pass
class OCL_OperatorCallExp(OperationCallExp):

    pass
class LoopExp:

    pass
class OCL_IterateExp(LoopExp):

    pass
class OCL_IteratorExp(LoopExp):

    def __init__(self, name: str, ATL.ecore#232: "OCL_Iterator", ATL.ecore#143: "OCL_OclExpression"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Statement:

    pass
class ATL_BindingStat(Statement):

    def __init__(self, propertyName: str, isAssignment: str, ATL_BindingStat109: "OclExpression" = None, ATL_BindingStat: "OclExpression" = None, Statement126: "ATL_ForStat", Statement118: "ATL_IfStat", Statement: "ATL_ActionBlock", Statement115: "ATL_IfStat"):
        self.propertyName = propertyName
        self.isAssignment = isAssignment
        self.ATL_BindingStat109 = ATL_BindingStat109
        self.ATL_BindingStat = ATL_BindingStat
        
    @property
    def isAssignment(self) -> str:
        return self.__isAssignment

    @isAssignment.setter
    def isAssignment(self, isAssignment: str):
        self.__isAssignment = isAssignment

    @property
    def propertyName(self) -> str:
        return self.__propertyName

    @propertyName.setter
    def propertyName(self, propertyName: str):
        self.__propertyName = propertyName

    @property
    def ATL_BindingStat(self):
        return self.__ATL_BindingStat

    @ATL_BindingStat.setter
    def ATL_BindingStat(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_BindingStat__ATL_BindingStat", None)
        self.__ATL_BindingStat = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression107"):
                opp_val = getattr(old_value, "OclExpression107", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression107"):
                opp_val = getattr(value, "OclExpression107", None)
                setattr(value, "OclExpression107", self)

    @property
    def ATL_BindingStat109(self):
        return self.__ATL_BindingStat109

    @ATL_BindingStat109.setter
    def ATL_BindingStat109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_BindingStat__ATL_BindingStat109", None)
        self.__ATL_BindingStat109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression110"):
                opp_val = getattr(old_value, "OclExpression110", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression110"):
                opp_val = getattr(value, "OclExpression110", None)
                setattr(value, "OclExpression110", self)

class ATL_ExpressionStat(Statement):

    pass
class ATL_ForStat(Statement):

    pass
class ATL_IfStat(Statement):

    pass
class Iterator:

    pass
class Binding:

    pass
class PatternElement:

    pass
class ATL_OutPatternElement(PatternElement):

    pass
class ATL_InPatternElement(PatternElement):

    pass
class DropPattern:

    pass
class InPatternElement:

    pass
class ATL_SimpleInPatternElement(InPatternElement):

    pass
class Parameter:

    pass
class VariableDeclaration:

    pass
class OCL_Parameter(VariableDeclaration):

    pass
class ATL_RuleVariableDeclaration(VariableDeclaration):

    pass
class OCL_Iterator(VariableDeclaration):

    pass
class OCL_TuplePart(VariableDeclaration):

    pass
class ATL_PatternElement(VariableDeclaration):

    pass
class OutPatternElement:

    pass
class ATL_ForEachOutPatternElement(OutPatternElement):

    pass
class ATL_SimpleOutPatternElement(OutPatternElement):

    pass
class RuleVariableDeclaration:

    pass
class ActionBlock:

    pass
class OutPattern:

    pass
class OclFeatureDefinition:

    pass
class Library:

    pass
class Query:

    pass
class Module:

    pass
class ModuleElement:

    pass
class ATL_Rule(ModuleElement):

    def __init__(self, name: str, 026: "OutPattern" = None, 029: "ActionBlock" = None, 032: set["RuleVariableDeclaration"] = None, ATL.ecore#14: "ATL_Module"):
        self.name = name
        self.026 = 026
        self.029 = 029
        self.032 = 032 if 032 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 026(self):
        return self.__026

    @026.setter
    def 026(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_Rule__026", None)
        self.__026 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL.ecore#27"):
                opp_val = getattr(old_value, "ATL.ecore#27", None)
                if opp_val == self:
                    setattr(old_value, "ATL.ecore#27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL.ecore#27"):
                opp_val = getattr(value, "ATL.ecore#27", None)
                setattr(value, "ATL.ecore#27", self)

    @property
    def 029(self):
        return self.__029

    @029.setter
    def 029(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_Rule__029", None)
        self.__029 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL.ecore#30"):
                opp_val = getattr(old_value, "ATL.ecore#30", None)
                if opp_val == self:
                    setattr(old_value, "ATL.ecore#30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL.ecore#30"):
                opp_val = getattr(value, "ATL.ecore#30", None)
                setattr(value, "ATL.ecore#30", self)

    @property
    def 032(self):
        return self.__032

    @032.setter
    def 032(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_Rule__032", None)
        self.__032 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ATL.ecore#33"):
                    opp_val = getattr(item, "ATL.ecore#33", None)
                    
                    if opp_val == self:
                        setattr(item, "ATL.ecore#33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ATL.ecore#33"):
                    opp_val = getattr(item, "ATL.ecore#33", None)
                    
                    setattr(item, "ATL.ecore#33", self)
                    

class ATL_Helper(ModuleElement):

    pass
class OclModel:

    pass
class MatchedRule:

    pass
class ATL_LazyMatchedRule(MatchedRule):

    def __init__(self, isUnique: str, ATL.ecore#39: "ATL_MatchedRule", ATL.ecore#49: "ATL_InPattern", ATL.ecore#42: "ATL_MatchedRule"):
        self.isUnique = isUnique
        
    @property
    def isUnique(self) -> str:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique

class InPattern:

    pass
class Rule:

    pass
class ATL_CalledRule(Rule):

    def __init__(self, isEntrypoint: str, isEndpoint: str, ATL_CalledRule: set["Parameter"] = None, ATL.ecore#102: "ATL_ActionBlock", ATL.ecore#96: "ATL_RuleVariableDeclaration", ATL.ecore#54: "ATL_OutPattern"):
        self.isEntrypoint = isEntrypoint
        self.isEndpoint = isEndpoint
        self.ATL_CalledRule = ATL_CalledRule if ATL_CalledRule is not None else set()
        
    @property
    def isEntrypoint(self) -> str:
        return self.__isEntrypoint

    @isEntrypoint.setter
    def isEntrypoint(self, isEntrypoint: str):
        self.__isEntrypoint = isEntrypoint

    @property
    def isEndpoint(self) -> str:
        return self.__isEndpoint

    @isEndpoint.setter
    def isEndpoint(self, isEndpoint: str):
        self.__isEndpoint = isEndpoint

    @property
    def ATL_CalledRule(self):
        return self.__ATL_CalledRule

    @ATL_CalledRule.setter
    def ATL_CalledRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_CalledRule__ATL_CalledRule", None)
        self.__ATL_CalledRule = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    setattr(item, "Parameter", self)
                    

class ATL_MatchedRule(Rule):

    def __init__(self, isAbstract: str, isRefining: str, isNoDefault: str, 035: "InPattern" = None, 038: set["MatchedRule"] = None, 041: "MatchedRule" = None, ATL.ecore#102: "ATL_ActionBlock", ATL.ecore#96: "ATL_RuleVariableDeclaration", ATL.ecore#54: "ATL_OutPattern"):
        self.isAbstract = isAbstract
        self.isRefining = isRefining
        self.isNoDefault = isNoDefault
        self.035 = 035
        self.038 = 038 if 038 is not None else set()
        self.041 = 041
        
    @property
    def isRefining(self) -> str:
        return self.__isRefining

    @isRefining.setter
    def isRefining(self, isRefining: str):
        self.__isRefining = isRefining

    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def isNoDefault(self) -> str:
        return self.__isNoDefault

    @isNoDefault.setter
    def isNoDefault(self, isNoDefault: str):
        self.__isNoDefault = isNoDefault

    @property
    def 038(self):
        return self.__038

    @038.setter
    def 038(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_MatchedRule__038", None)
        self.__038 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ATL.ecore#39"):
                    opp_val = getattr(item, "ATL.ecore#39", None)
                    
                    if opp_val == self:
                        setattr(item, "ATL.ecore#39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ATL.ecore#39"):
                    opp_val = getattr(item, "ATL.ecore#39", None)
                    
                    setattr(item, "ATL.ecore#39", self)
                    

    @property
    def 041(self):
        return self.__041

    @041.setter
    def 041(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_MatchedRule__041", None)
        self.__041 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL.ecore#42"):
                opp_val = getattr(old_value, "ATL.ecore#42", None)
                if opp_val == self:
                    setattr(old_value, "ATL.ecore#42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL.ecore#42"):
                opp_val = getattr(value, "ATL.ecore#42", None)
                setattr(value, "ATL.ecore#42", self)

    @property
    def 035(self):
        return self.__035

    @035.setter
    def 035(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_MatchedRule__035", None)
        self.__035 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL.ecore#36"):
                opp_val = getattr(old_value, "ATL.ecore#36", None)
                if opp_val == self:
                    setattr(old_value, "ATL.ecore#36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL.ecore#36"):
                opp_val = getattr(value, "ATL.ecore#36", None)
                setattr(value, "ATL.ecore#36", self)

class Helper:

    pass
class Unit:

    pass
class ATL_Query(Unit):

    pass
class ATL_Library(Unit):

    pass
class LibraryRef:

    pass
class LocatedElement:

    pass
class OCL_TupleTypeAttribute(LocatedElement):

    def __init__(self, name: str, 1270: "OclType" = None, 1273: "TupleType" = None):
        self.name = name
        self.1270 = 1270
        self.1273 = 1273
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 1270(self):
        return self.__1270

    @1270.setter
    def 1270(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_TupleTypeAttribute__1270", None)
        self.__1270 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL.ecore#271"):
                opp_val = getattr(old_value, "ATL.ecore#271", None)
                if opp_val == self:
                    setattr(old_value, "ATL.ecore#271", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL.ecore#271"):
                opp_val = getattr(value, "ATL.ecore#271", None)
                setattr(value, "ATL.ecore#271", self)

    @property
    def 1273(self):
        return self.__1273

    @1273.setter
    def 1273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_TupleTypeAttribute__1273", None)
        self.__1273 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL.ecore#274"):
                opp_val = getattr(old_value, "ATL.ecore#274", None)
                if opp_val == self:
                    setattr(old_value, "ATL.ecore#274", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL.ecore#274"):
                opp_val = getattr(value, "ATL.ecore#274", None)
                setattr(value, "ATL.ecore#274", self)

class ATL_LibraryRef(LocatedElement):

    def __init__(self, name: str, 098: "Unit" = None):
        self.name = name
        self.098 = 098
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 098(self):
        return self.__098

    @098.setter
    def 098(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_LibraryRef__098", None)
        self.__098 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL.ecore#99"):
                opp_val = getattr(old_value, "ATL.ecore#99", None)
                if opp_val == self:
                    setattr(old_value, "ATL.ecore#99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL.ecore#99"):
                opp_val = getattr(value, "ATL.ecore#99", None)
                setattr(value, "ATL.ecore#99", self)

class OCL_OclModel(LocatedElement):

    def __init__(self, name: str, 1315: "OclModel" = None, 1318: set["OclModelElement"] = None, 1321: set["OclModel"] = None):
        self.name = name
        self.1315 = 1315
        self.1318 = 1318 if 1318 is not None else set()
        self.1321 = 1321 if 1321 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 1321(self):
        return self.__1321

    @1321.setter
    def 1321(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclModel__1321", None)
        self.__1321 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ATL.ecore#322"):
                    opp_val = getattr(item, "ATL.ecore#322", None)
                    
                    if opp_val == self:
                        setattr(item, "ATL.ecore#322", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ATL.ecore#322"):
                    opp_val = getattr(item, "ATL.ecore#322", None)
                    
                    setattr(item, "ATL.ecore#322", self)
                    

    @property
    def 1315(self):
        return self.__1315

    @1315.setter
    def 1315(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclModel__1315", None)
        self.__1315 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL.ecore#316"):
                opp_val = getattr(old_value, "ATL.ecore#316", None)
                if opp_val == self:
                    setattr(old_value, "ATL.ecore#316", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL.ecore#316"):
                opp_val = getattr(value, "ATL.ecore#316", None)
                setattr(value, "ATL.ecore#316", self)

    @property
    def 1318(self):
        return self.__1318

    @1318.setter
    def 1318(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclModel__1318", None)
        self.__1318 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ATL.ecore#319"):
                    opp_val = getattr(item, "ATL.ecore#319", None)
                    
                    if opp_val == self:
                        setattr(item, "ATL.ecore#319", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ATL.ecore#319"):
                    opp_val = getattr(item, "ATL.ecore#319", None)
                    
                    setattr(item, "ATL.ecore#319", self)
                    

class ATL_Binding(LocatedElement):

    def __init__(self, propertyName: str, isAssignment: str, ATL_Binding: "OclExpression" = None, 092: "OutPatternElement" = None):
        self.propertyName = propertyName
        self.isAssignment = isAssignment
        self.ATL_Binding = ATL_Binding
        self.092 = 092
        
    @property
    def isAssignment(self) -> str:
        return self.__isAssignment

    @isAssignment.setter
    def isAssignment(self, isAssignment: str):
        self.__isAssignment = isAssignment

    @property
    def propertyName(self) -> str:
        return self.__propertyName

    @propertyName.setter
    def propertyName(self, propertyName: str):
        self.__propertyName = propertyName

    @property
    def 092(self):
        return self.__092

    @092.setter
    def 092(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_Binding__092", None)
        self.__092 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL.ecore#93"):
                opp_val = getattr(old_value, "ATL.ecore#93", None)
                if opp_val == self:
                    setattr(old_value, "ATL.ecore#93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL.ecore#93"):
                opp_val = getattr(value, "ATL.ecore#93", None)
                setattr(value, "ATL.ecore#93", self)

    @property
    def ATL_Binding(self):
        return self.__ATL_Binding

    @ATL_Binding.setter
    def ATL_Binding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_Binding__ATL_Binding", None)
        self.__ATL_Binding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression90"):
                opp_val = getattr(old_value, "OclExpression90", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression90"):
                opp_val = getattr(value, "OclExpression90", None)
                setattr(value, "OclExpression90", self)

class OCL_MapElement(LocatedElement):

    pass
class ATL_Statement(LocatedElement):

    pass
class ATL_ActionBlock(LocatedElement):

    pass
class OCL_OclContextDefinition(LocatedElement):

    pass
class ATL_ModuleElement(LocatedElement):

    pass
class ATL_InPattern(LocatedElement):

    pass
class OCL_VariableDeclaration(LocatedElement):

    def __init__(self, id: str, varName: str, 1216: "OclType" = None, 1219: "OclExpression" = None, 1222: "LetExp" = None, 1225: "IterateExp" = None, 1228: set["VariableExp"] = None):
        self.id = id
        self.varName = varName
        self.1216 = 1216
        self.1219 = 1219
        self.1222 = 1222
        self.1225 = 1225
        self.1228 = 1228 if 1228 is not None else set()
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def 1216(self):
        return self.__1216

    @1216.setter
    def 1216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_VariableDeclaration__1216", None)
        self.__1216 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL.ecore#217"):
                opp_val = getattr(old_value, "ATL.ecore#217", None)
                if opp_val == self:
                    setattr(old_value, "ATL.ecore#217", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL.ecore#217"):
                opp_val = getattr(value, "ATL.ecore#217", None)
                setattr(value, "ATL.ecore#217", self)

    @property
    def 1228(self):
        return self.__1228

    @1228.setter
    def 1228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_VariableDeclaration__1228", None)
        self.__1228 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ATL.ecore#229"):
                    opp_val = getattr(item, "ATL.ecore#229", None)
                    
                    if opp_val == self:
                        setattr(item, "ATL.ecore#229", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ATL.ecore#229"):
                    opp_val = getattr(item, "ATL.ecore#229", None)
                    
                    setattr(item, "ATL.ecore#229", self)
                    

    @property
    def 1219(self):
        return self.__1219

    @1219.setter
    def 1219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_VariableDeclaration__1219", None)
        self.__1219 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL.ecore#220"):
                opp_val = getattr(old_value, "ATL.ecore#220", None)
                if opp_val == self:
                    setattr(old_value, "ATL.ecore#220", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL.ecore#220"):
                opp_val = getattr(value, "ATL.ecore#220", None)
                setattr(value, "ATL.ecore#220", self)

    @property
    def 1222(self):
        return self.__1222

    @1222.setter
    def 1222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_VariableDeclaration__1222", None)
        self.__1222 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL.ecore#223"):
                opp_val = getattr(old_value, "ATL.ecore#223", None)
                if opp_val == self:
                    setattr(old_value, "ATL.ecore#223", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL.ecore#223"):
                opp_val = getattr(value, "ATL.ecore#223", None)
                setattr(value, "ATL.ecore#223", self)

    @property
    def 1225(self):
        return self.__1225

    @1225.setter
    def 1225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_VariableDeclaration__1225", None)
        self.__1225 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL.ecore#226"):
                opp_val = getattr(old_value, "ATL.ecore#226", None)
                if opp_val == self:
                    setattr(old_value, "ATL.ecore#226", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL.ecore#226"):
                opp_val = getattr(value, "ATL.ecore#226", None)
                setattr(value, "ATL.ecore#226", self)

class OCL_OclExpression(LocatedElement):

    pass
class OCL_OclFeature(LocatedElement):

    pass
class OCL_OclFeatureDefinition(LocatedElement):

    pass
class ATL_OutPattern(LocatedElement):

    pass
class ATL_DropPattern(LocatedElement):

    pass
class ATL_Unit(LocatedElement):

    def __init__(self, name: str, 0: set["LibraryRef"] = None):
        self.name = name
        self.0 = 0 if 0 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 0(self):
        return self.__0

    @0.setter
    def 0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_Unit__0", None)
        self.__0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ATL.ecore#"):
                    opp_val = getattr(item, "ATL.ecore#", None)
                    
                    if opp_val == self:
                        setattr(item, "ATL.ecore#", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ATL.ecore#"):
                    opp_val = getattr(item, "ATL.ecore#", None)
                    
                    setattr(item, "ATL.ecore#", self)
                    

class ATL_LocatedElement(ABC):

    def __init__(self, location: str, commentsBefore: str, commentsAfter: str):
        self.location = location
        self.commentsBefore = commentsBefore
        self.commentsAfter = commentsAfter
        
    @property
    def commentsAfter(self) -> str:
        return self.__commentsAfter

    @commentsAfter.setter
    def commentsAfter(self, commentsAfter: str):
        self.__commentsAfter = commentsAfter

    @property
    def commentsBefore(self) -> str:
        return self.__commentsBefore

    @commentsBefore.setter
    def commentsBefore(self, commentsBefore: str):
        self.__commentsBefore = commentsBefore

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

class ATL_Module(Unit):

    def __init__(self, isRefining: str, ATL_Module: set["OclModel"] = None, ATL_Module10: set["OclModel"] = None, 013: set["ModuleElement"] = None, ATL.ecore#99: "ATL_LibraryRef"):
        self.isRefining = isRefining
        self.ATL_Module = ATL_Module if ATL_Module is not None else set()
        self.ATL_Module10 = ATL_Module10 if ATL_Module10 is not None else set()
        self.013 = 013 if 013 is not None else set()
        
    @property
    def isRefining(self) -> str:
        return self.__isRefining

    @isRefining.setter
    def isRefining(self, isRefining: str):
        self.__isRefining = isRefining

    @property
    def ATL_Module10(self):
        return self.__ATL_Module10

    @ATL_Module10.setter
    def ATL_Module10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_Module__ATL_Module10", None)
        self.__ATL_Module10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclModel11"):
                    opp_val = getattr(item, "OclModel11", None)
                    
                    if opp_val == self:
                        setattr(item, "OclModel11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclModel11"):
                    opp_val = getattr(item, "OclModel11", None)
                    
                    setattr(item, "OclModel11", self)
                    

    @property
    def ATL_Module(self):
        return self.__ATL_Module

    @ATL_Module.setter
    def ATL_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_Module__ATL_Module", None)
        self.__ATL_Module = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclModel"):
                    opp_val = getattr(item, "OclModel", None)
                    
                    if opp_val == self:
                        setattr(item, "OclModel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclModel"):
                    opp_val = getattr(item, "OclModel", None)
                    
                    setattr(item, "OclModel", self)
                    

    @property
    def 013(self):
        return self.__013

    @013.setter
    def 013(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_Module__013", None)
        self.__013 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ATL.ecore#14"):
                    opp_val = getattr(item, "ATL.ecore#14", None)
                    
                    if opp_val == self:
                        setattr(item, "ATL.ecore#14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ATL.ecore#14"):
                    opp_val = getattr(item, "ATL.ecore#14", None)
                    
                    setattr(item, "ATL.ecore#14", self)
                    

class OclExpression:

    pass
class OCL_PrimitiveExp(OclExpression):

    pass
class OCL_TupleExp(OclExpression):

    pass
class OCL_OclType(OclExpression):

    def __init__(self, name: str, 1264: "VariableDeclaration" = None, 1240: "OclContextDefinition" = None, 1243: "OclExpression" = None, 1246: "Operation" = None, 1249: "MapType" = None, 1252: "Attribute" = None, 1255: "MapType" = None, 1258: "CollectionType" = None, 1261: "TupleTypeAttribute" = None, OclExpression112: "ATL_IfStat", OclExpression110: "ATL_BindingStat", ATL.ecore#244: "OCL_OclType", ATL.ecore#167: "OCL_CollectionExp", OclExpression107: "ATL_BindingStat", OclExpression105: "ATL_ExpressionStat", OclExpression84: "ATL_SimpleOutPatternElement", ATL.ecore#313: "OCL_Operation", OclExpression123: "ATL_ForStat", ATL.ecore#214: "OCL_IfExp", OclExpression181: "OCL_MapElement", OclExpression86: "ATL_ForEachOutPatternElement", ATL.ecore#211: "OCL_IfExp", OclExpression90: "ATL_Binding", ATL.ecore#208: "OCL_IfExp", ATL.ecore#190: "OCL_OperationCallExp", ATL.ecore#301: "OCL_Attribute", OclExpression51: "ATL_InPattern", ATL.ecore#193: "OCL_LoopExp", OclExpression184: "OCL_MapElement", OclExpression: "ATL_Query", ATL.ecore#220: "OCL_VariableDeclaration", ATL.ecore#205: "OCL_LetExp", ATL.ecore#187: "OCL_PropertyCallExp"):
        self.name = name
        self.1264 = 1264
        self.1240 = 1240
        self.1243 = 1243
        self.1246 = 1246
        self.1249 = 1249
        self.1252 = 1252
        self.1255 = 1255
        self.1258 = 1258
        self.1261 = 1261
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 1252(self):
        return self.__1252

    @1252.setter
    def 1252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__1252", None)
        self.__1252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL.ecore#253"):
                opp_val = getattr(old_value, "ATL.ecore#253", None)
                if opp_val == self:
                    setattr(old_value, "ATL.ecore#253", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL.ecore#253"):
                opp_val = getattr(value, "ATL.ecore#253", None)
                setattr(value, "ATL.ecore#253", self)

    @property
    def 1240(self):
        return self.__1240

    @1240.setter
    def 1240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__1240", None)
        self.__1240 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL.ecore#241"):
                opp_val = getattr(old_value, "ATL.ecore#241", None)
                if opp_val == self:
                    setattr(old_value, "ATL.ecore#241", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL.ecore#241"):
                opp_val = getattr(value, "ATL.ecore#241", None)
                setattr(value, "ATL.ecore#241", self)

    @property
    def 1243(self):
        return self.__1243

    @1243.setter
    def 1243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__1243", None)
        self.__1243 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL.ecore#244"):
                opp_val = getattr(old_value, "ATL.ecore#244", None)
                if opp_val == self:
                    setattr(old_value, "ATL.ecore#244", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL.ecore#244"):
                opp_val = getattr(value, "ATL.ecore#244", None)
                setattr(value, "ATL.ecore#244", self)

    @property
    def 1255(self):
        return self.__1255

    @1255.setter
    def 1255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__1255", None)
        self.__1255 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL.ecore#256"):
                opp_val = getattr(old_value, "ATL.ecore#256", None)
                if opp_val == self:
                    setattr(old_value, "ATL.ecore#256", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL.ecore#256"):
                opp_val = getattr(value, "ATL.ecore#256", None)
                setattr(value, "ATL.ecore#256", self)

    @property
    def 1264(self):
        return self.__1264

    @1264.setter
    def 1264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__1264", None)
        self.__1264 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL.ecore#265"):
                opp_val = getattr(old_value, "ATL.ecore#265", None)
                if opp_val == self:
                    setattr(old_value, "ATL.ecore#265", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL.ecore#265"):
                opp_val = getattr(value, "ATL.ecore#265", None)
                setattr(value, "ATL.ecore#265", self)

    @property
    def 1249(self):
        return self.__1249

    @1249.setter
    def 1249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__1249", None)
        self.__1249 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL.ecore#250"):
                opp_val = getattr(old_value, "ATL.ecore#250", None)
                if opp_val == self:
                    setattr(old_value, "ATL.ecore#250", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL.ecore#250"):
                opp_val = getattr(value, "ATL.ecore#250", None)
                setattr(value, "ATL.ecore#250", self)

    @property
    def 1258(self):
        return self.__1258

    @1258.setter
    def 1258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__1258", None)
        self.__1258 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL.ecore#259"):
                opp_val = getattr(old_value, "ATL.ecore#259", None)
                if opp_val == self:
                    setattr(old_value, "ATL.ecore#259", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL.ecore#259"):
                opp_val = getattr(value, "ATL.ecore#259", None)
                setattr(value, "ATL.ecore#259", self)

    @property
    def 1246(self):
        return self.__1246

    @1246.setter
    def 1246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__1246", None)
        self.__1246 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL.ecore#247"):
                opp_val = getattr(old_value, "ATL.ecore#247", None)
                if opp_val == self:
                    setattr(old_value, "ATL.ecore#247", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL.ecore#247"):
                opp_val = getattr(value, "ATL.ecore#247", None)
                setattr(value, "ATL.ecore#247", self)

    @property
    def 1261(self):
        return self.__1261

    @1261.setter
    def 1261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__1261", None)
        self.__1261 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL.ecore#262"):
                opp_val = getattr(old_value, "ATL.ecore#262", None)
                if opp_val == self:
                    setattr(old_value, "ATL.ecore#262", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL.ecore#262"):
                opp_val = getattr(value, "ATL.ecore#262", None)
                setattr(value, "ATL.ecore#262", self)

class OCL_IfExp(OclExpression):

    pass
class OCL_MapExp(OclExpression):

    pass
class OCL_SuperExp(OclExpression):

    pass
class OCL_VariableExp(OclExpression):

    pass
class OCL_EnumLiteralExp(OclExpression):

    def __init__(self, name: str, OclExpression112: "ATL_IfStat", OclExpression110: "ATL_BindingStat", ATL.ecore#244: "OCL_OclType", ATL.ecore#167: "OCL_CollectionExp", OclExpression107: "ATL_BindingStat", OclExpression105: "ATL_ExpressionStat", OclExpression84: "ATL_SimpleOutPatternElement", ATL.ecore#313: "OCL_Operation", OclExpression123: "ATL_ForStat", ATL.ecore#214: "OCL_IfExp", OclExpression181: "OCL_MapElement", OclExpression86: "ATL_ForEachOutPatternElement", ATL.ecore#211: "OCL_IfExp", OclExpression90: "ATL_Binding", ATL.ecore#208: "OCL_IfExp", ATL.ecore#190: "OCL_OperationCallExp", ATL.ecore#301: "OCL_Attribute", OclExpression51: "ATL_InPattern", ATL.ecore#193: "OCL_LoopExp", OclExpression184: "OCL_MapElement", OclExpression: "ATL_Query", ATL.ecore#220: "OCL_VariableDeclaration", ATL.ecore#205: "OCL_LetExp", ATL.ecore#187: "OCL_PropertyCallExp"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class OCL_CollectionExp(OclExpression):

    pass
class OCL_LetExp(OclExpression):

    pass
class OCL_PropertyCallExp(OclExpression):

    pass
class OCL_OclUndefinedExp(OclExpression):

    pass