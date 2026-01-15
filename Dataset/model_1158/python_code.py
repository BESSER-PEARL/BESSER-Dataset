from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class OclModelElement:

    pass
class Parameter:

    pass
class OclFeatureDefinition:

    pass
class OclFeature:

    pass
class OCL_Operation(OclFeature):

    def __init__(self, name: str, 1177: set["Parameter"] = None, 1180: "OclType" = None, 1183: "OclExpression" = None, #157: "OCL_OclFeatureDefinition"):
        self.name = name
        self.1177 = 1177 if 1177 is not None else set()
        self.1180 = 1180
        self.1183 = 1183
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 1183(self):
        return self.__1183

    @1183.setter
    def 1183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Operation__1183", None)
        self.__1183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#184"):
                opp_val = getattr(old_value, "#184", None)
                if opp_val == self:
                    setattr(old_value, "#184", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#184"):
                opp_val = getattr(value, "#184", None)
                setattr(value, "#184", self)

    @property
    def 1180(self):
        return self.__1180

    @1180.setter
    def 1180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Operation__1180", None)
        self.__1180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#181"):
                opp_val = getattr(old_value, "#181", None)
                if opp_val == self:
                    setattr(old_value, "#181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#181"):
                opp_val = getattr(value, "#181", None)
                setattr(value, "#181", self)

    @property
    def 1177(self):
        return self.__1177

    @1177.setter
    def 1177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Operation__1177", None)
        self.__1177 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#178"):
                    opp_val = getattr(item, "#178", None)
                    
                    if opp_val == self:
                        setattr(item, "#178", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#178"):
                    opp_val = getattr(item, "#178", None)
                    
                    setattr(item, "#178", self)
                    

class OCL_Attribute(OclFeature):

    def __init__(self, name: str, 1171: "OclExpression" = None, 1174: "OclType" = None, #157: "OCL_OclFeatureDefinition"):
        self.name = name
        self.1171 = 1171
        self.1174 = 1174
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 1174(self):
        return self.__1174

    @1174.setter
    def 1174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Attribute__1174", None)
        self.__1174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#175"):
                opp_val = getattr(old_value, "#175", None)
                if opp_val == self:
                    setattr(old_value, "#175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#175"):
                opp_val = getattr(value, "#175", None)
                setattr(value, "#175", self)

    @property
    def 1171(self):
        return self.__1171

    @1171.setter
    def 1171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Attribute__1171", None)
        self.__1171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#172"):
                opp_val = getattr(old_value, "#172", None)
                if opp_val == self:
                    setattr(old_value, "#172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#172"):
                opp_val = getattr(value, "#172", None)
                setattr(value, "#172", self)

class OclModel:

    pass
class TupleType:

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
class TupleTypeAttribute:

    pass
class CollectionType:

    pass
class OCL_OrderedSetType(CollectionType):

    pass
class OCL_SetType(CollectionType):

    pass
class OCL_BagType(CollectionType):

    pass
class MapType:

    pass
class OclContextDefinition:

    pass
class OCL_SequenceType(CollectionType):

    pass
class VariableExp:

    pass
class IterateExp:

    pass
class Iterator:

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
class OCL_StringExp(PrimitiveExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
    @property
    def stringSymbol(self) -> str:
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol

class OclExpression:

    pass
class OCL_SuperExp(OclExpression):

    pass
class OCL_LetExp(OclExpression):

    pass
class OCL_OclType(OclExpression):

    def __init__(self, name: str, 1111: "OclContextDefinition" = None, 1114: "OclExpression" = None, 1117: "Operation" = None, 1120: "MapType" = None, 1123: "Attribute" = None, 1126: "MapType" = None, 1129: "CollectionType" = None, 1132: "TupleTypeAttribute" = None, 1135: "VariableDeclaration" = None, #91: "OCL_VariableDeclaration", #61: "OCL_OperationCallExp", #115: "OCL_OclType", OclExpression: "OCL_MapElement", #76: "OCL_LetExp", #184: "OCL_Operation", #172: "OCL_Attribute", #39: "OCL_CollectionExp", #64: "OCL_LoopExp", #82: "OCL_IfExp", #58: "OCL_PropertyCallExp", OclExpression55: "OCL_MapElement", #85: "OCL_IfExp", #79: "OCL_IfExp"):
        self.name = name
        self.1111 = 1111
        self.1114 = 1114
        self.1117 = 1117
        self.1120 = 1120
        self.1123 = 1123
        self.1126 = 1126
        self.1129 = 1129
        self.1132 = 1132
        self.1135 = 1135
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 1123(self):
        return self.__1123

    @1123.setter
    def 1123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__1123", None)
        self.__1123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#124"):
                opp_val = getattr(old_value, "#124", None)
                if opp_val == self:
                    setattr(old_value, "#124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#124"):
                opp_val = getattr(value, "#124", None)
                setattr(value, "#124", self)

    @property
    def 1111(self):
        return self.__1111

    @1111.setter
    def 1111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__1111", None)
        self.__1111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#112"):
                opp_val = getattr(old_value, "#112", None)
                if opp_val == self:
                    setattr(old_value, "#112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#112"):
                opp_val = getattr(value, "#112", None)
                setattr(value, "#112", self)

    @property
    def 1129(self):
        return self.__1129

    @1129.setter
    def 1129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__1129", None)
        self.__1129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#130"):
                opp_val = getattr(old_value, "#130", None)
                if opp_val == self:
                    setattr(old_value, "#130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#130"):
                opp_val = getattr(value, "#130", None)
                setattr(value, "#130", self)

    @property
    def 1120(self):
        return self.__1120

    @1120.setter
    def 1120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__1120", None)
        self.__1120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#121"):
                opp_val = getattr(old_value, "#121", None)
                if opp_val == self:
                    setattr(old_value, "#121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#121"):
                opp_val = getattr(value, "#121", None)
                setattr(value, "#121", self)

    @property
    def 1135(self):
        return self.__1135

    @1135.setter
    def 1135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__1135", None)
        self.__1135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#136"):
                opp_val = getattr(old_value, "#136", None)
                if opp_val == self:
                    setattr(old_value, "#136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#136"):
                opp_val = getattr(value, "#136", None)
                setattr(value, "#136", self)

    @property
    def 1126(self):
        return self.__1126

    @1126.setter
    def 1126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__1126", None)
        self.__1126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#127"):
                opp_val = getattr(old_value, "#127", None)
                if opp_val == self:
                    setattr(old_value, "#127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#127"):
                opp_val = getattr(value, "#127", None)
                setattr(value, "#127", self)

    @property
    def 1132(self):
        return self.__1132

    @1132.setter
    def 1132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__1132", None)
        self.__1132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#133"):
                opp_val = getattr(old_value, "#133", None)
                if opp_val == self:
                    setattr(old_value, "#133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#133"):
                opp_val = getattr(value, "#133", None)
                setattr(value, "#133", self)

    @property
    def 1117(self):
        return self.__1117

    @1117.setter
    def 1117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__1117", None)
        self.__1117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#118"):
                opp_val = getattr(old_value, "#118", None)
                if opp_val == self:
                    setattr(old_value, "#118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#118"):
                opp_val = getattr(value, "#118", None)
                setattr(value, "#118", self)

    @property
    def 1114(self):
        return self.__1114

    @1114.setter
    def 1114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__1114", None)
        self.__1114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#115"):
                opp_val = getattr(old_value, "#115", None)
                if opp_val == self:
                    setattr(old_value, "#115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#115"):
                opp_val = getattr(value, "#115", None)
                setattr(value, "#115", self)

class OCL_TupleExp(OclExpression):

    pass
class OCL_OclUndefinedExp(OclExpression):

    pass
class OCL_EnumLiteralExp(OclExpression):

    def __init__(self, name: str, #91: "OCL_VariableDeclaration", #61: "OCL_OperationCallExp", #115: "OCL_OclType", OclExpression: "OCL_MapElement", #76: "OCL_LetExp", #184: "OCL_Operation", #172: "OCL_Attribute", #39: "OCL_CollectionExp", #64: "OCL_LoopExp", #82: "OCL_IfExp", #58: "OCL_PropertyCallExp", OclExpression55: "OCL_MapElement", #85: "OCL_IfExp", #79: "OCL_IfExp"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class OCL_MapExp(OclExpression):

    pass
class OCL_PrimitiveExp(OclExpression):

    pass
class OCL_CollectionExp(OclExpression):

    pass
class OCL_IfExp(OclExpression):

    pass
class OCL_PropertyCallExp(OclExpression):

    pass
class OCL_VariableExp(OclExpression):

    pass
class Attribute:

    pass
class Operation:

    pass
class VariableDeclaration:

    pass
class OCL_Iterator(VariableDeclaration):

    pass
class OCL_Parameter(VariableDeclaration):

    pass
class OCL_TuplePart(VariableDeclaration):

    pass
class OperationCallExp:

    pass
class OCL_OperatorCallExp(OperationCallExp):

    pass
class OCL_CollectionOperationCallExp(OperationCallExp):

    pass
class LoopExp:

    pass
class OCL_IteratorExp(LoopExp):

    def __init__(self, name: str, #103: "OCL_Iterator", #15: "OCL_OclExpression"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class OCL_IterateExp(LoopExp):

    pass
class LetExp:

    pass
class CollectionExp:

    pass
class OCL_SetExp(CollectionExp):

    pass
class OCL_BagExp(CollectionExp):

    pass
class OCL_SequenceExp(CollectionExp):

    pass
class OCL_OrderedSetExp(CollectionExp):

    pass
class PropertyCallExp:

    pass
class OCL_LoopExp(PropertyCallExp):

    pass
class OCL_OperationCallExp(PropertyCallExp):

    def __init__(self, operationName: str, 160: set["OclExpression"] = None, #6: "OCL_OclExpression"):
        self.operationName = operationName
        self.160 = 160 if 160 is not None else set()
        
    @property
    def operationName(self) -> str:
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName

    @property
    def 160(self):
        return self.__160

    @160.setter
    def 160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OperationCallExp__160", None)
        self.__160 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#61"):
                    opp_val = getattr(item, "#61", None)
                    
                    if opp_val == self:
                        setattr(item, "#61", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#61"):
                    opp_val = getattr(item, "#61", None)
                    
                    setattr(item, "#61", self)
                    

class OCL_NavigationOrAttributeCallExp(PropertyCallExp):

    def __init__(self, name: str, #6: "OCL_OclExpression"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class IfExp:

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

class OclType:

    pass
class OCL_CollectionType(OclType):

    pass
class OCL_OclModelElement(OclType):

    pass
class OCL_OclAnyType(OclType):

    pass
class OCL_Primitive(OclType):

    pass
class OCL_TupleType(OclType):

    pass
class OCL_MapType(OclType):

    pass
class LocatedElement:

    pass
class OCL_MapElement(LocatedElement):

    pass
class OCL_OclFeatureDefinition(LocatedElement):

    pass
class OCL_OclContextDefinition(LocatedElement):

    pass
class OCL_TupleTypeAttribute(LocatedElement):

    def __init__(self, name: str, 1141: "OclType" = None, 1144: "TupleType" = None):
        self.name = name
        self.1141 = 1141
        self.1144 = 1144
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 1141(self):
        return self.__1141

    @1141.setter
    def 1141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_TupleTypeAttribute__1141", None)
        self.__1141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#142"):
                opp_val = getattr(old_value, "#142", None)
                if opp_val == self:
                    setattr(old_value, "#142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#142"):
                opp_val = getattr(value, "#142", None)
                setattr(value, "#142", self)

    @property
    def 1144(self):
        return self.__1144

    @1144.setter
    def 1144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_TupleTypeAttribute__1144", None)
        self.__1144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#145"):
                opp_val = getattr(old_value, "#145", None)
                if opp_val == self:
                    setattr(old_value, "#145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#145"):
                opp_val = getattr(value, "#145", None)
                setattr(value, "#145", self)

class OCL_VariableDeclaration(LocatedElement):

    def __init__(self, id: str, varName: str, 187: "OclType" = None, 190: "OclExpression" = None, 193: "LetExp" = None, 196: "IterateExp" = None, 199: set["VariableExp"] = None):
        self.id = id
        self.varName = varName
        self.187 = 187
        self.190 = 190
        self.193 = 193
        self.196 = 196
        self.199 = 199 if 199 is not None else set()
        
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
    def 199(self):
        return self.__199

    @199.setter
    def 199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_VariableDeclaration__199", None)
        self.__199 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#100"):
                    opp_val = getattr(item, "#100", None)
                    
                    if opp_val == self:
                        setattr(item, "#100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#100"):
                    opp_val = getattr(item, "#100", None)
                    
                    setattr(item, "#100", self)
                    

    @property
    def 190(self):
        return self.__190

    @190.setter
    def 190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_VariableDeclaration__190", None)
        self.__190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#91"):
                opp_val = getattr(old_value, "#91", None)
                if opp_val == self:
                    setattr(old_value, "#91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#91"):
                opp_val = getattr(value, "#91", None)
                setattr(value, "#91", self)

    @property
    def 193(self):
        return self.__193

    @193.setter
    def 193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_VariableDeclaration__193", None)
        self.__193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#94"):
                opp_val = getattr(old_value, "#94", None)
                if opp_val == self:
                    setattr(old_value, "#94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#94"):
                opp_val = getattr(value, "#94", None)
                setattr(value, "#94", self)

    @property
    def 196(self):
        return self.__196

    @196.setter
    def 196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_VariableDeclaration__196", None)
        self.__196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#97"):
                opp_val = getattr(old_value, "#97", None)
                if opp_val == self:
                    setattr(old_value, "#97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#97"):
                opp_val = getattr(value, "#97", None)
                setattr(value, "#97", self)

    @property
    def 187(self):
        return self.__187

    @187.setter
    def 187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_VariableDeclaration__187", None)
        self.__187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#88"):
                opp_val = getattr(old_value, "#88", None)
                if opp_val == self:
                    setattr(old_value, "#88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#88"):
                opp_val = getattr(value, "#88", None)
                setattr(value, "#88", self)

class OCL_OclFeature(LocatedElement):

    pass
class OCL_OclModel(LocatedElement):

    def __init__(self, name: str, 1186: "OclModel" = None, 1189: set["OclModelElement"] = None, 1192: set["OclModel"] = None):
        self.name = name
        self.1186 = 1186
        self.1189 = 1189 if 1189 is not None else set()
        self.1192 = 1192 if 1192 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 1192(self):
        return self.__1192

    @1192.setter
    def 1192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclModel__1192", None)
        self.__1192 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#193"):
                    opp_val = getattr(item, "#193", None)
                    
                    if opp_val == self:
                        setattr(item, "#193", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#193"):
                    opp_val = getattr(item, "#193", None)
                    
                    setattr(item, "#193", self)
                    

    @property
    def 1189(self):
        return self.__1189

    @1189.setter
    def 1189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclModel__1189", None)
        self.__1189 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#190"):
                    opp_val = getattr(item, "#190", None)
                    
                    if opp_val == self:
                        setattr(item, "#190", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#190"):
                    opp_val = getattr(item, "#190", None)
                    
                    setattr(item, "#190", self)
                    

    @property
    def 1186(self):
        return self.__1186

    @1186.setter
    def 1186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclModel__1186", None)
        self.__1186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#187"):
                opp_val = getattr(old_value, "#187", None)
                if opp_val == self:
                    setattr(old_value, "#187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#187"):
                opp_val = getattr(value, "#187", None)
                setattr(value, "#187", self)

class OCL_OclExpression(LocatedElement):

    pass
class ATL_LocatedElement(ABC):

    def __init__(self, location: str, commentsBefore: str, commentsAfter: str):
        self.location = location
        self.commentsBefore = commentsBefore
        self.commentsAfter = commentsAfter
        
    @property
    def commentsBefore(self) -> str:
        return self.__commentsBefore

    @commentsBefore.setter
    def commentsBefore(self, commentsBefore: str):
        self.__commentsBefore = commentsBefore

    @property
    def commentsAfter(self) -> str:
        return self.__commentsAfter

    @commentsAfter.setter
    def commentsAfter(self, commentsAfter: str):
        self.__commentsAfter = commentsAfter

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location
