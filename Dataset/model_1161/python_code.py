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

    def __init__(self, name: str, 1291: "OclExpression" = None, 1294: "OclType" = None, #277: "OCL_OclFeatureDefinition"):
        self.name = name
        self.1291 = 1291
        self.1294 = 1294
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 1291(self):
        return self.__1291

    @1291.setter
    def 1291(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Attribute__1291", None)
        self.__1291 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#292"):
                opp_val = getattr(old_value, "#292", None)
                if opp_val == self:
                    setattr(old_value, "#292", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#292"):
                opp_val = getattr(value, "#292", None)
                setattr(value, "#292", self)

    @property
    def 1294(self):
        return self.__1294

    @1294.setter
    def 1294(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Attribute__1294", None)
        self.__1294 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#295"):
                opp_val = getattr(old_value, "#295", None)
                if opp_val == self:
                    setattr(old_value, "#295", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#295"):
                opp_val = getattr(value, "#295", None)
                setattr(value, "#295", self)

class OCL_Operation(OclFeature):

    def __init__(self, name: str, 1300: "OclType" = None, 1303: "OclExpression" = None, 1297: set["Parameter"] = None, #277: "OCL_OclFeatureDefinition"):
        self.name = name
        self.1300 = 1300
        self.1303 = 1303
        self.1297 = 1297 if 1297 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 1303(self):
        return self.__1303

    @1303.setter
    def 1303(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Operation__1303", None)
        self.__1303 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#304"):
                opp_val = getattr(old_value, "#304", None)
                if opp_val == self:
                    setattr(old_value, "#304", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#304"):
                opp_val = getattr(value, "#304", None)
                setattr(value, "#304", self)

    @property
    def 1300(self):
        return self.__1300

    @1300.setter
    def 1300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Operation__1300", None)
        self.__1300 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#301"):
                opp_val = getattr(old_value, "#301", None)
                if opp_val == self:
                    setattr(old_value, "#301", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#301"):
                opp_val = getattr(value, "#301", None)
                setattr(value, "#301", self)

    @property
    def 1297(self):
        return self.__1297

    @1297.setter
    def 1297(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Operation__1297", None)
        self.__1297 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#298"):
                    opp_val = getattr(item, "#298", None)
                    
                    if opp_val == self:
                        setattr(item, "#298", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#298"):
                    opp_val = getattr(item, "#298", None)
                    
                    setattr(item, "#298", self)
                    

class TupleType:

    pass
class TupleTypeAttribute:

    pass
class CollectionType:

    pass
class OCL_SetType(CollectionType):

    pass
class OCL_SequenceType(CollectionType):

    pass
class OCL_OrderedSetType(CollectionType):

    pass
class OCL_BagType(CollectionType):

    pass
class MapType:

    pass
class NumericType:

    pass
class OCL_RealType(NumericType):

    pass
class OCL_IntegerType(NumericType):

    pass
class Primitive:

    pass
class OCL_NumericType(Primitive):

    pass
class OCL_BooleanType(Primitive):

    pass
class OCL_StringType(Primitive):

    pass
class OclContextDefinition:

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
class OCL_BooleanExp(PrimitiveExp):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
    @property
    def booleanSymbol(self) -> str:
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol

class OCL_NumericExp(PrimitiveExp):

    pass
class OCL_StringExp(PrimitiveExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
    @property
    def stringSymbol(self) -> str:
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol

class TuplePart:

    pass
class Attribute:

    pass
class Operation:

    pass
class OperationCallExp:

    pass
class OCL_CollectionOperationCallExp(OperationCallExp):

    pass
class OCL_OperatorCallExp(OperationCallExp):

    pass
class LoopExp:

    pass
class OCL_IteratorExp(LoopExp):

    def __init__(self, name: str, #223: "OCL_Iterator", #134: "OCL_OclExpression"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class OCL_IterateExp(LoopExp):

    pass
class PropertyCallExp:

    pass
class OCL_LoopExp(PropertyCallExp):

    pass
class OCL_NavigationOrAttributeCallExp(PropertyCallExp):

    def __init__(self, name: str, #125: "OCL_OclExpression"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class OCL_OperationCallExp(PropertyCallExp):

    def __init__(self, operationName: str, 1180: set["OclExpression"] = None, #125: "OCL_OclExpression"):
        self.operationName = operationName
        self.1180 = 1180 if 1180 is not None else set()
        
    @property
    def operationName(self) -> str:
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName

    @property
    def 1180(self):
        return self.__1180

    @1180.setter
    def 1180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OperationCallExp__1180", None)
        self.__1180 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#181"):
                    opp_val = getattr(item, "#181", None)
                    
                    if opp_val == self:
                        setattr(item, "#181", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#181"):
                    opp_val = getattr(item, "#181", None)
                    
                    setattr(item, "#181", self)
                    

class IfExp:

    pass
class OclType:

    pass
class OCL_MapType(OclType):

    pass
class OCL_OclAnyType(OclType):

    pass
class OCL_CollectionType(OclType):

    pass
class OCL_TupleType(OclType):

    pass
class OCL_OclModelElement(OclType):

    pass
class OCL_Primitive(OclType):

    pass
class LetExp:

    pass
class CollectionExp:

    pass
class OCL_SequenceExp(CollectionExp):

    pass
class OCL_OrderedSetExp(CollectionExp):

    pass
class OCL_SetExp(CollectionExp):

    pass
class OCL_BagExp(CollectionExp):

    pass
class Statement:

    pass
class ATL_ExpressionStat(Statement):

    pass
class ATL_ForStat(Statement):

    pass
class ATL_IfStat(Statement):

    pass
class ATL_BindingStat(Statement):

    def __init__(self, propertyName: str, isAssignment: str, ATL_BindingStat: "OclExpression" = None, ATL_BindingStat100: "OclExpression" = None, Statement117: "ATL_ForStat", Statement109: "ATL_IfStat", Statement: "ATL_ActionBlock", Statement106: "ATL_IfStat"):
        self.propertyName = propertyName
        self.isAssignment = isAssignment
        self.ATL_BindingStat = ATL_BindingStat
        self.ATL_BindingStat100 = ATL_BindingStat100
        
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
            if hasattr(old_value, "OclExpression98"):
                opp_val = getattr(old_value, "OclExpression98", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression98"):
                opp_val = getattr(value, "OclExpression98", None)
                setattr(value, "OclExpression98", self)

    @property
    def ATL_BindingStat100(self):
        return self.__ATL_BindingStat100

    @ATL_BindingStat100.setter
    def ATL_BindingStat100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_BindingStat__ATL_BindingStat100", None)
        self.__ATL_BindingStat100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression101"):
                opp_val = getattr(old_value, "OclExpression101", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression101"):
                opp_val = getattr(value, "OclExpression101", None)
                setattr(value, "OclExpression101", self)

class Binding:

    pass
class Iterator:

    pass
class OutPatternElement:

    pass
class ATL_ForEachOutPatternElement(OutPatternElement):

    pass
class ATL_SimpleOutPatternElement(OutPatternElement):

    pass
class PatternElement:

    pass
class ATL_OutPatternElement(PatternElement):

    pass
class ATL_InPatternElement(PatternElement):

    pass
class VariableDeclaration:

    pass
class OCL_TuplePart(VariableDeclaration):

    pass
class OCL_Parameter(VariableDeclaration):

    pass
class OCL_Iterator(VariableDeclaration):

    pass
class ATL_RuleVariableDeclaration(VariableDeclaration):

    pass
class Parameter:

    pass
class ATL_PatternElement(VariableDeclaration):

    pass
class MatchedRule:

    pass
class ATL_LazyMatchedRule(MatchedRule):

    def __init__(self, isUnique: str, #39: "ATL_MatchedRule", #36: "ATL_MatchedRule", #46: "ATL_InPattern"):
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

    def __init__(self, isEntrypoint: str, isEndpoint: str, ATL_CalledRule: set["Parameter"] = None, #93: "ATL_ActionBlock", #87: "ATL_RuleVariableDeclaration", #51: "ATL_OutPattern"):
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

    def __init__(self, isAbstract: str, isRefining: str, isNoDefault: str, 032: "InPattern" = None, 035: set["MatchedRule"] = None, 038: "MatchedRule" = None, #93: "ATL_ActionBlock", #87: "ATL_RuleVariableDeclaration", #51: "ATL_OutPattern"):
        self.isAbstract = isAbstract
        self.isRefining = isRefining
        self.isNoDefault = isNoDefault
        self.032 = 032
        self.035 = 035 if 035 is not None else set()
        self.038 = 038
        
    @property
    def isRefining(self) -> str:
        return self.__isRefining

    @isRefining.setter
    def isRefining(self, isRefining: str):
        self.__isRefining = isRefining

    @property
    def isNoDefault(self) -> str:
        return self.__isNoDefault

    @isNoDefault.setter
    def isNoDefault(self, isNoDefault: str):
        self.__isNoDefault = isNoDefault

    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def 035(self):
        return self.__035

    @035.setter
    def 035(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_MatchedRule__035", None)
        self.__035 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#36"):
                    opp_val = getattr(item, "#36", None)
                    
                    if opp_val == self:
                        setattr(item, "#36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#36"):
                    opp_val = getattr(item, "#36", None)
                    
                    setattr(item, "#36", self)
                    

    @property
    def 032(self):
        return self.__032

    @032.setter
    def 032(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_MatchedRule__032", None)
        self.__032 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#33"):
                opp_val = getattr(old_value, "#33", None)
                if opp_val == self:
                    setattr(old_value, "#33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#33"):
                opp_val = getattr(value, "#33", None)
                setattr(value, "#33", self)

    @property
    def 038(self):
        return self.__038

    @038.setter
    def 038(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_MatchedRule__038", None)
        self.__038 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#39"):
                opp_val = getattr(old_value, "#39", None)
                if opp_val == self:
                    setattr(old_value, "#39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#39"):
                opp_val = getattr(value, "#39", None)
                setattr(value, "#39", self)

class RuleVariableDeclaration:

    pass
class ActionBlock:

    pass
class OutPattern:

    pass
class InPatternElement:

    pass
class ATL_SimpleInPatternElement(InPatternElement):

    pass
class ModuleElement:

    pass
class OclModel:

    pass
class OclExpression:

    pass
class OCL_OclUndefinedExp(OclExpression):

    pass
class OCL_VariableExp(OclExpression):

    pass
class OCL_OclType(OclExpression):

    def __init__(self, name: str, 1234: "OclExpression" = None, 1237: "Operation" = None, 1231: "OclContextDefinition" = None, 1240: "MapType" = None, 1243: "Attribute" = None, 1246: "MapType" = None, 1249: "CollectionType" = None, 1252: "TupleTypeAttribute" = None, 1255: "VariableDeclaration" = None, #158: "OCL_CollectionExp", #211: "OCL_VariableDeclaration", OclExpression101: "ATL_BindingStat", #202: "OCL_IfExp", OclExpression172: "OCL_MapElement", OclExpression96: "ATL_ExpressionStat", OclExpression103: "ATL_IfStat", OclExpression75: "ATL_SimpleOutPatternElement", #181: "OCL_OperationCallExp", OclExpression81: "ATL_Binding", OclExpression175: "OCL_MapElement", #205: "OCL_IfExp", OclExpression: "ATL_Query", OclExpression48: "ATL_InPattern", #184: "OCL_LoopExp", OclExpression114: "ATL_ForStat", #304: "OCL_Operation", #199: "OCL_IfExp", #235: "OCL_OclType", OclExpression98: "ATL_BindingStat", OclExpression77: "ATL_ForEachOutPatternElement", #196: "OCL_LetExp", #178: "OCL_PropertyCallExp", #292: "OCL_Attribute"):
        self.name = name
        self.1234 = 1234
        self.1237 = 1237
        self.1231 = 1231
        self.1240 = 1240
        self.1243 = 1243
        self.1246 = 1246
        self.1249 = 1249
        self.1252 = 1252
        self.1255 = 1255
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 1231(self):
        return self.__1231

    @1231.setter
    def 1231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__1231", None)
        self.__1231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#232"):
                opp_val = getattr(old_value, "#232", None)
                if opp_val == self:
                    setattr(old_value, "#232", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#232"):
                opp_val = getattr(value, "#232", None)
                setattr(value, "#232", self)

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
            if hasattr(old_value, "#256"):
                opp_val = getattr(old_value, "#256", None)
                if opp_val == self:
                    setattr(old_value, "#256", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#256"):
                opp_val = getattr(value, "#256", None)
                setattr(value, "#256", self)

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
            if hasattr(old_value, "#247"):
                opp_val = getattr(old_value, "#247", None)
                if opp_val == self:
                    setattr(old_value, "#247", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#247"):
                opp_val = getattr(value, "#247", None)
                setattr(value, "#247", self)

    @property
    def 1234(self):
        return self.__1234

    @1234.setter
    def 1234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__1234", None)
        self.__1234 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#235"):
                opp_val = getattr(old_value, "#235", None)
                if opp_val == self:
                    setattr(old_value, "#235", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#235"):
                opp_val = getattr(value, "#235", None)
                setattr(value, "#235", self)

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
            if hasattr(old_value, "#253"):
                opp_val = getattr(old_value, "#253", None)
                if opp_val == self:
                    setattr(old_value, "#253", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#253"):
                opp_val = getattr(value, "#253", None)
                setattr(value, "#253", self)

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
            if hasattr(old_value, "#241"):
                opp_val = getattr(old_value, "#241", None)
                if opp_val == self:
                    setattr(old_value, "#241", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#241"):
                opp_val = getattr(value, "#241", None)
                setattr(value, "#241", self)

    @property
    def 1237(self):
        return self.__1237

    @1237.setter
    def 1237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__1237", None)
        self.__1237 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#238"):
                opp_val = getattr(old_value, "#238", None)
                if opp_val == self:
                    setattr(old_value, "#238", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#238"):
                opp_val = getattr(value, "#238", None)
                setattr(value, "#238", self)

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
            if hasattr(old_value, "#244"):
                opp_val = getattr(old_value, "#244", None)
                if opp_val == self:
                    setattr(old_value, "#244", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#244"):
                opp_val = getattr(value, "#244", None)
                setattr(value, "#244", self)

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
            if hasattr(old_value, "#250"):
                opp_val = getattr(old_value, "#250", None)
                if opp_val == self:
                    setattr(old_value, "#250", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#250"):
                opp_val = getattr(value, "#250", None)
                setattr(value, "#250", self)

class OCL_PropertyCallExp(OclExpression):

    pass
class OCL_EnumLiteralExp(OclExpression):

    def __init__(self, name: str, #158: "OCL_CollectionExp", #211: "OCL_VariableDeclaration", OclExpression101: "ATL_BindingStat", #202: "OCL_IfExp", OclExpression172: "OCL_MapElement", OclExpression96: "ATL_ExpressionStat", OclExpression103: "ATL_IfStat", OclExpression75: "ATL_SimpleOutPatternElement", #181: "OCL_OperationCallExp", OclExpression81: "ATL_Binding", OclExpression175: "OCL_MapElement", #205: "OCL_IfExp", OclExpression: "ATL_Query", OclExpression48: "ATL_InPattern", #184: "OCL_LoopExp", OclExpression114: "ATL_ForStat", #304: "OCL_Operation", #199: "OCL_IfExp", #235: "OCL_OclType", OclExpression98: "ATL_BindingStat", OclExpression77: "ATL_ForEachOutPatternElement", #196: "OCL_LetExp", #178: "OCL_PropertyCallExp", #292: "OCL_Attribute"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class OCL_CollectionExp(OclExpression):

    pass
class OCL_PrimitiveExp(OclExpression):

    pass
class OCL_IfExp(OclExpression):

    pass
class OCL_MapExp(OclExpression):

    pass
class OCL_SuperExp(OclExpression):

    pass
class OCL_LetExp(OclExpression):

    pass
class OCL_TupleExp(OclExpression):

    pass
class Helper:

    pass
class Unit:

    pass
class ATL_Query(Unit):

    pass
class ATL_Module(Unit):

    def __init__(self, isRefining: str, ATL_Module: set["OclModel"] = None, ATL_Module8: set["OclModel"] = None, 011: set["ModuleElement"] = None, #90: "ATL_LibraryRef"):
        self.isRefining = isRefining
        self.ATL_Module = ATL_Module if ATL_Module is not None else set()
        self.ATL_Module8 = ATL_Module8 if ATL_Module8 is not None else set()
        self.011 = 011 if 011 is not None else set()
        
    @property
    def isRefining(self) -> str:
        return self.__isRefining

    @isRefining.setter
    def isRefining(self, isRefining: str):
        self.__isRefining = isRefining

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
    def 011(self):
        return self.__011

    @011.setter
    def 011(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_Module__011", None)
        self.__011 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#12"):
                    opp_val = getattr(item, "#12", None)
                    
                    if opp_val == self:
                        setattr(item, "#12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#12"):
                    opp_val = getattr(item, "#12", None)
                    
                    setattr(item, "#12", self)
                    

    @property
    def ATL_Module8(self):
        return self.__ATL_Module8

    @ATL_Module8.setter
    def ATL_Module8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_Module__ATL_Module8", None)
        self.__ATL_Module8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclModel9"):
                    opp_val = getattr(item, "OclModel9", None)
                    
                    if opp_val == self:
                        setattr(item, "OclModel9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclModel9"):
                    opp_val = getattr(item, "OclModel9", None)
                    
                    setattr(item, "OclModel9", self)
                    

class ATL_Library(Unit):

    pass
class LibraryRef:

    pass
class ATL_Rule(ModuleElement):

    def __init__(self, name: str, 023: "OutPattern" = None, 026: "ActionBlock" = None, 029: set["RuleVariableDeclaration"] = None, #12: "ATL_Module"):
        self.name = name
        self.023 = 023
        self.026 = 026
        self.029 = 029 if 029 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 029(self):
        return self.__029

    @029.setter
    def 029(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_Rule__029", None)
        self.__029 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#30"):
                    opp_val = getattr(item, "#30", None)
                    
                    if opp_val == self:
                        setattr(item, "#30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#30"):
                    opp_val = getattr(item, "#30", None)
                    
                    setattr(item, "#30", self)
                    

    @property
    def 023(self):
        return self.__023

    @023.setter
    def 023(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_Rule__023", None)
        self.__023 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#24"):
                opp_val = getattr(old_value, "#24", None)
                if opp_val == self:
                    setattr(old_value, "#24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#24"):
                opp_val = getattr(value, "#24", None)
                setattr(value, "#24", self)

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
            if hasattr(old_value, "#27"):
                opp_val = getattr(old_value, "#27", None)
                if opp_val == self:
                    setattr(old_value, "#27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#27"):
                opp_val = getattr(value, "#27", None)
                setattr(value, "#27", self)

class OclFeatureDefinition:

    pass
class Library:

    pass
class Query:

    pass
class ATL_Helper(ModuleElement):

    pass
class Module:

    pass
class LocatedElement:

    pass
class OCL_OclModel(LocatedElement):

    def __init__(self, name: str, 1306: "OclModel" = None, 1309: set["OclModelElement"] = None, 1312: set["OclModel"] = None):
        self.name = name
        self.1306 = 1306
        self.1309 = 1309 if 1309 is not None else set()
        self.1312 = 1312 if 1312 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 1309(self):
        return self.__1309

    @1309.setter
    def 1309(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclModel__1309", None)
        self.__1309 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#310"):
                    opp_val = getattr(item, "#310", None)
                    
                    if opp_val == self:
                        setattr(item, "#310", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#310"):
                    opp_val = getattr(item, "#310", None)
                    
                    setattr(item, "#310", self)
                    

    @property
    def 1312(self):
        return self.__1312

    @1312.setter
    def 1312(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclModel__1312", None)
        self.__1312 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#313"):
                    opp_val = getattr(item, "#313", None)
                    
                    if opp_val == self:
                        setattr(item, "#313", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#313"):
                    opp_val = getattr(item, "#313", None)
                    
                    setattr(item, "#313", self)
                    

    @property
    def 1306(self):
        return self.__1306

    @1306.setter
    def 1306(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclModel__1306", None)
        self.__1306 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#307"):
                opp_val = getattr(old_value, "#307", None)
                if opp_val == self:
                    setattr(old_value, "#307", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#307"):
                opp_val = getattr(value, "#307", None)
                setattr(value, "#307", self)

class OCL_TupleTypeAttribute(LocatedElement):

    def __init__(self, name: str, 1264: "TupleType" = None, 1261: "OclType" = None):
        self.name = name
        self.1264 = 1264
        self.1261 = 1261
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 1264(self):
        return self.__1264

    @1264.setter
    def 1264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_TupleTypeAttribute__1264", None)
        self.__1264 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#265"):
                opp_val = getattr(old_value, "#265", None)
                if opp_val == self:
                    setattr(old_value, "#265", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#265"):
                opp_val = getattr(value, "#265", None)
                setattr(value, "#265", self)

    @property
    def 1261(self):
        return self.__1261

    @1261.setter
    def 1261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_TupleTypeAttribute__1261", None)
        self.__1261 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#262"):
                opp_val = getattr(old_value, "#262", None)
                if opp_val == self:
                    setattr(old_value, "#262", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#262"):
                opp_val = getattr(value, "#262", None)
                setattr(value, "#262", self)

class OCL_MapElement(LocatedElement):

    pass
class OCL_OclFeature(LocatedElement):

    pass
class ATL_ModuleElement(LocatedElement):

    pass
class ATL_Binding(LocatedElement):

    def __init__(self, propertyName: str, isAssignment: str, ATL_Binding: "OclExpression" = None, 083: "OutPatternElement" = None):
        self.propertyName = propertyName
        self.isAssignment = isAssignment
        self.ATL_Binding = ATL_Binding
        self.083 = 083
        
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
    def 083(self):
        return self.__083

    @083.setter
    def 083(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_Binding__083", None)
        self.__083 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#84"):
                opp_val = getattr(old_value, "#84", None)
                if opp_val == self:
                    setattr(old_value, "#84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#84"):
                opp_val = getattr(value, "#84", None)
                setattr(value, "#84", self)

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
            if hasattr(old_value, "OclExpression81"):
                opp_val = getattr(old_value, "OclExpression81", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression81"):
                opp_val = getattr(value, "OclExpression81", None)
                setattr(value, "OclExpression81", self)

class OCL_VariableDeclaration(LocatedElement):

    def __init__(self, id: str, varName: str, 1213: "LetExp" = None, 1216: "IterateExp" = None, 1219: set["VariableExp"] = None, 1207: "OclType" = None, 1210: "OclExpression" = None):
        self.id = id
        self.varName = varName
        self.1213 = 1213
        self.1216 = 1216
        self.1219 = 1219 if 1219 is not None else set()
        self.1207 = 1207
        self.1210 = 1210
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

    @property
    def 1210(self):
        return self.__1210

    @1210.setter
    def 1210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_VariableDeclaration__1210", None)
        self.__1210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#211"):
                opp_val = getattr(old_value, "#211", None)
                if opp_val == self:
                    setattr(old_value, "#211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#211"):
                opp_val = getattr(value, "#211", None)
                setattr(value, "#211", self)

    @property
    def 1219(self):
        return self.__1219

    @1219.setter
    def 1219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_VariableDeclaration__1219", None)
        self.__1219 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#220"):
                    opp_val = getattr(item, "#220", None)
                    
                    if opp_val == self:
                        setattr(item, "#220", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#220"):
                    opp_val = getattr(item, "#220", None)
                    
                    setattr(item, "#220", self)
                    

    @property
    def 1213(self):
        return self.__1213

    @1213.setter
    def 1213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_VariableDeclaration__1213", None)
        self.__1213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#214"):
                opp_val = getattr(old_value, "#214", None)
                if opp_val == self:
                    setattr(old_value, "#214", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#214"):
                opp_val = getattr(value, "#214", None)
                setattr(value, "#214", self)

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
            if hasattr(old_value, "#217"):
                opp_val = getattr(old_value, "#217", None)
                if opp_val == self:
                    setattr(old_value, "#217", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#217"):
                opp_val = getattr(value, "#217", None)
                setattr(value, "#217", self)

    @property
    def 1207(self):
        return self.__1207

    @1207.setter
    def 1207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_VariableDeclaration__1207", None)
        self.__1207 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#208"):
                opp_val = getattr(old_value, "#208", None)
                if opp_val == self:
                    setattr(old_value, "#208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#208"):
                opp_val = getattr(value, "#208", None)
                setattr(value, "#208", self)

class ATL_LibraryRef(LocatedElement):

    def __init__(self, name: str, 089: "Unit" = None):
        self.name = name
        self.089 = 089
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 089(self):
        return self.__089

    @089.setter
    def 089(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_LibraryRef__089", None)
        self.__089 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#90"):
                opp_val = getattr(old_value, "#90", None)
                if opp_val == self:
                    setattr(old_value, "#90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#90"):
                opp_val = getattr(value, "#90", None)
                setattr(value, "#90", self)

class OCL_OclExpression(LocatedElement):

    pass
class OCL_OclContextDefinition(LocatedElement):

    pass
class OCL_OclFeatureDefinition(LocatedElement):

    pass
class ATL_Statement(LocatedElement):

    pass
class ATL_ActionBlock(LocatedElement):

    pass
class ATL_OutPattern(LocatedElement):

    pass
class ATL_InPattern(LocatedElement):

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
                if hasattr(item, "#"):
                    opp_val = getattr(item, "#", None)
                    
                    if opp_val == self:
                        setattr(item, "#", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#"):
                    opp_val = getattr(item, "#", None)
                    
                    setattr(item, "#", self)
                    

class ATL_LocatedElement(ABC):

    def __init__(self, location: str, commentsBefore: str, commentsAfter: str):
        self.location = location
        self.commentsBefore = commentsBefore
        self.commentsAfter = commentsAfter
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

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
