####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
ATL_LocatedElement = Class(name="ATL::LocatedElement", is_abstract=True)
OCL_OclExpression = Class(name="OCL::OclExpression", is_abstract=True)
LocatedElement = Class(name="LocatedElement")
OclType = Class(name="OclType")
OCL_BooleanExp = Class(name="OCL::BooleanExp")
IfExp = Class(name="IfExp")
PropertyCallExp = Class(name="PropertyCallExp")
CollectionExp = Class(name="CollectionExp")
LetExp = Class(name="LetExp")
LoopExp = Class(name="LoopExp")
OperationCallExp = Class(name="OperationCallExp")
VariableDeclaration = Class(name="VariableDeclaration")
Operation = Class(name="Operation")
Attribute = Class(name="Attribute")
OCL_VariableExp = Class(name="OCL::VariableExp")
OclExpression = Class(name="OclExpression")
OCL_SuperExp = Class(name="OCL::SuperExp")
OCL_PrimitiveExp = Class(name="OCL::PrimitiveExp", is_abstract=True)
OCL_StringExp = Class(name="OCL::StringExp")
PrimitiveExp = Class(name="PrimitiveExp")
OCL_NumericExp = Class(name="OCL::NumericExp", is_abstract=True)
OCL_RealExp = Class(name="OCL::RealExp")
NumericExp = Class(name="NumericExp")
OCL_IntegerExp = Class(name="OCL::IntegerExp")
OCL_CollectionExp = Class(name="OCL::CollectionExp", is_abstract=True)
OCL_BagExp = Class(name="OCL::BagExp")
OCL_OrderedSetExp = Class(name="OCL::OrderedSetExp")
OCL_SequenceExp = Class(name="OCL::SequenceExp")
OCL_SetExp = Class(name="OCL::SetExp")
OCL_TupleExp = Class(name="OCL::TupleExp")
TuplePart = Class(name="TuplePart")
OCL_TuplePart = Class(name="OCL::TuplePart")
TupleExp = Class(name="TupleExp")
OCL_MapExp = Class(name="OCL::MapExp")
MapElement = Class(name="MapElement")
OCL_MapElement = Class(name="OCL::MapElement")
MapExp = Class(name="MapExp")
OCL_EnumLiteralExp = Class(name="OCL::EnumLiteralExp")
OCL_OclUndefinedExp = Class(name="OCL::OclUndefinedExp")
OCL_PropertyCallExp = Class(name="OCL::PropertyCallExp", is_abstract=True)
OCL_NavigationOrAttributeCallExp = Class(name="OCL::NavigationOrAttributeCallExp")
OCL_OperationCallExp = Class(name="OCL::OperationCallExp")
OCL_OperatorCallExp = Class(name="OCL::OperatorCallExp")
OCL_CollectionOperationCallExp = Class(name="OCL::CollectionOperationCallExp")
OCL_LoopExp = Class(name="OCL::LoopExp", is_abstract=True)
Iterator = Class(name="Iterator")
OCL_IterateExp = Class(name="OCL::IterateExp")
OCL_IteratorExp = Class(name="OCL::IteratorExp")
OCL_LetExp = Class(name="OCL::LetExp")
OCL_IfExp = Class(name="OCL::IfExp")
OCL_OclType = Class(name="OCL::OclType")
OCL_VariableDeclaration = Class(name="OCL::VariableDeclaration")
IterateExp = Class(name="IterateExp")
VariableExp = Class(name="VariableExp")
OCL_Iterator = Class(name="OCL::Iterator")
OCL_Parameter = Class(name="OCL::Parameter")
OCL_CollectionType = Class(name="OCL::CollectionType")
OCL_SequenceType = Class(name="OCL::SequenceType")
OclContextDefinition = Class(name="OclContextDefinition")
MapType = Class(name="MapType")
CollectionType = Class(name="CollectionType")
TupleTypeAttribute = Class(name="TupleTypeAttribute")
OCL_Primitive = Class(name="OCL::Primitive", is_abstract=True)
OCL_StringType = Class(name="OCL::StringType")
Primitive = Class(name="Primitive")
OCL_BooleanType = Class(name="OCL::BooleanType")
OCL_NumericType = Class(name="OCL::NumericType", is_abstract=True)
OCL_IntegerType = Class(name="OCL::IntegerType")
NumericType = Class(name="NumericType")
OCL_RealType = Class(name="OCL::RealType")
OCL_BagType = Class(name="OCL::BagType")
OCL_OrderedSetType = Class(name="OCL::OrderedSetType")
OCL_SetType = Class(name="OCL::SetType")
OCL_OclAnyType = Class(name="OCL::OclAnyType")
OCL_TupleType = Class(name="OCL::TupleType")
OCL_TupleTypeAttribute = Class(name="OCL::TupleTypeAttribute")
TupleType = Class(name="TupleType")
OCL_OclModelElement = Class(name="OCL::OclModelElement")
OclModel = Class(name="OclModel")
OCL_MapType = Class(name="OCL::MapType")
OCL_OclFeatureDefinition = Class(name="OCL::OclFeatureDefinition")
OclFeature = Class(name="OclFeature")
OCL_OclContextDefinition = Class(name="OCL::OclContextDefinition")
OclFeatureDefinition = Class(name="OclFeatureDefinition")
OCL_OclFeature = Class(name="OCL::OclFeature", is_abstract=True)
OCL_Attribute = Class(name="OCL::Attribute")
OCL_Operation = Class(name="OCL::Operation")
Parameter_ = Class(name="Parameter")
OCL_OclModel = Class(name="OCL::OclModel")
OclModelElement = Class(name="OclModelElement")

# ATL_LocatedElement class attributes and methods
ATL_LocatedElement_location: Property = Property(name="location", type=StringType)
ATL_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
ATL_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
ATL_LocatedElement.attributes={ATL_LocatedElement_commentsBefore, ATL_LocatedElement_commentsAfter, ATL_LocatedElement_location}

# OCL_OclExpression class attributes and methods

# LocatedElement class attributes and methods

# OclType class attributes and methods

# OCL_BooleanExp class attributes and methods
OCL_BooleanExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
OCL_BooleanExp.attributes={OCL_BooleanExp_booleanSymbol}

# IfExp class attributes and methods

# PropertyCallExp class attributes and methods

# CollectionExp class attributes and methods

# LetExp class attributes and methods

# LoopExp class attributes and methods

# OperationCallExp class attributes and methods

# VariableDeclaration class attributes and methods

# Operation class attributes and methods

# Attribute class attributes and methods

# OCL_VariableExp class attributes and methods

# OclExpression class attributes and methods

# OCL_SuperExp class attributes and methods

# OCL_PrimitiveExp class attributes and methods

# OCL_StringExp class attributes and methods
OCL_StringExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
OCL_StringExp.attributes={OCL_StringExp_stringSymbol}

# PrimitiveExp class attributes and methods

# OCL_NumericExp class attributes and methods

# OCL_RealExp class attributes and methods
OCL_RealExp_realSymbol: Property = Property(name="realSymbol", type=StringType)
OCL_RealExp.attributes={OCL_RealExp_realSymbol}

# NumericExp class attributes and methods

# OCL_IntegerExp class attributes and methods
OCL_IntegerExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
OCL_IntegerExp.attributes={OCL_IntegerExp_integerSymbol}

# OCL_CollectionExp class attributes and methods

# OCL_BagExp class attributes and methods

# OCL_OrderedSetExp class attributes and methods

# OCL_SequenceExp class attributes and methods

# OCL_SetExp class attributes and methods

# OCL_TupleExp class attributes and methods

# TuplePart class attributes and methods

# OCL_TuplePart class attributes and methods

# TupleExp class attributes and methods

# OCL_MapExp class attributes and methods

# MapElement class attributes and methods

# OCL_MapElement class attributes and methods

# MapExp class attributes and methods

# OCL_EnumLiteralExp class attributes and methods
OCL_EnumLiteralExp_name: Property = Property(name="name", type=StringType)
OCL_EnumLiteralExp.attributes={OCL_EnumLiteralExp_name}

# OCL_OclUndefinedExp class attributes and methods

# OCL_PropertyCallExp class attributes and methods

# OCL_NavigationOrAttributeCallExp class attributes and methods
OCL_NavigationOrAttributeCallExp_name: Property = Property(name="name", type=StringType)
OCL_NavigationOrAttributeCallExp.attributes={OCL_NavigationOrAttributeCallExp_name}

# OCL_OperationCallExp class attributes and methods
OCL_OperationCallExp_operationName: Property = Property(name="operationName", type=StringType)
OCL_OperationCallExp.attributes={OCL_OperationCallExp_operationName}

# OCL_OperatorCallExp class attributes and methods

# OCL_CollectionOperationCallExp class attributes and methods

# OCL_LoopExp class attributes and methods

# Iterator class attributes and methods

# OCL_IterateExp class attributes and methods

# OCL_IteratorExp class attributes and methods
OCL_IteratorExp_name: Property = Property(name="name", type=StringType)
OCL_IteratorExp.attributes={OCL_IteratorExp_name}

# OCL_LetExp class attributes and methods

# OCL_IfExp class attributes and methods

# OCL_OclType class attributes and methods
OCL_OclType_name: Property = Property(name="name", type=StringType)
OCL_OclType.attributes={OCL_OclType_name}

# OCL_VariableDeclaration class attributes and methods
OCL_VariableDeclaration_id: Property = Property(name="id", type=StringType)
OCL_VariableDeclaration_varName: Property = Property(name="varName", type=StringType)
OCL_VariableDeclaration.attributes={OCL_VariableDeclaration_id, OCL_VariableDeclaration_varName}

# IterateExp class attributes and methods

# VariableExp class attributes and methods

# OCL_Iterator class attributes and methods

# OCL_Parameter class attributes and methods

# OCL_CollectionType class attributes and methods

# OCL_SequenceType class attributes and methods

# OclContextDefinition class attributes and methods

# MapType class attributes and methods

# CollectionType class attributes and methods

# TupleTypeAttribute class attributes and methods

# OCL_Primitive class attributes and methods

# OCL_StringType class attributes and methods

# Primitive class attributes and methods

# OCL_BooleanType class attributes and methods

# OCL_NumericType class attributes and methods

# OCL_IntegerType class attributes and methods

# NumericType class attributes and methods

# OCL_RealType class attributes and methods

# OCL_BagType class attributes and methods

# OCL_OrderedSetType class attributes and methods

# OCL_SetType class attributes and methods

# OCL_OclAnyType class attributes and methods

# OCL_TupleType class attributes and methods

# OCL_TupleTypeAttribute class attributes and methods
OCL_TupleTypeAttribute_name: Property = Property(name="name", type=StringType)
OCL_TupleTypeAttribute.attributes={OCL_TupleTypeAttribute_name}

# TupleType class attributes and methods

# OCL_OclModelElement class attributes and methods

# OclModel class attributes and methods

# OCL_MapType class attributes and methods

# OCL_OclFeatureDefinition class attributes and methods

# OclFeature class attributes and methods

# OCL_OclContextDefinition class attributes and methods

# OclFeatureDefinition class attributes and methods

# OCL_OclFeature class attributes and methods

# OCL_Attribute class attributes and methods
OCL_Attribute_name: Property = Property(name="name", type=StringType)
OCL_Attribute.attributes={OCL_Attribute_name}

# OCL_Operation class attributes and methods
OCL_Operation_name: Property = Property(name="name", type=StringType)
OCL_Operation.attributes={OCL_Operation_name}

# Parameter class attributes and methods

# OCL_OclModel class attributes and methods
OCL_OclModel_name: Property = Property(name="name", type=StringType)
OCL_OclModel.attributes={OCL_OclModel_name}

# OclModelElement class attributes and methods

# Relationships
type0: BinaryAssociation = BinaryAssociation(
    name="type0",
    ends={
        Property(name="1", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="#", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1))
    }
)
ifExp31: BinaryAssociation = BinaryAssociation(
    name="ifExp31",
    ends={
        Property(name="#3", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="12", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
appliedProperty4: BinaryAssociation = BinaryAssociation(
    name="appliedProperty4",
    ends={
        Property(name="#6", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="15", type=PropertyCallExp, multiplicity=Multiplicity(0, 1))
    }
)
collection7: BinaryAssociation = BinaryAssociation(
    name="collection7",
    ends={
        Property(name="#9", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="18", type=CollectionExp, multiplicity=Multiplicity(0, 1))
    }
)
letExp10: BinaryAssociation = BinaryAssociation(
    name="letExp10",
    ends={
        Property(name="#12", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="111", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
loopExp13: BinaryAssociation = BinaryAssociation(
    name="loopExp13",
    ends={
        Property(name="#15", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="114", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
parentOperation16: BinaryAssociation = BinaryAssociation(
    name="parentOperation16",
    ends={
        Property(name="#18", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="117", type=OperationCallExp, multiplicity=Multiplicity(0, 1))
    }
)
initializedVariable19: BinaryAssociation = BinaryAssociation(
    name="initializedVariable19",
    ends={
        Property(name="#21", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="120", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
ifExp222: BinaryAssociation = BinaryAssociation(
    name="ifExp222",
    ends={
        Property(name="#24", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="123", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningOperation25: BinaryAssociation = BinaryAssociation(
    name="owningOperation25",
    ends={
        Property(name="#27", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="126", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
ifExp128: BinaryAssociation = BinaryAssociation(
    name="ifExp128",
    ends={
        Property(name="#30", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="129", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningAttribute31: BinaryAssociation = BinaryAssociation(
    name="owningAttribute31",
    ends={
        Property(name="#33", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="132", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable34: BinaryAssociation = BinaryAssociation(
    name="referredVariable34",
    ends={
        Property(name="#36", type=OCL_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="135", type=VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
elements37: BinaryAssociation = BinaryAssociation(
    name="elements37",
    ends={
        Property(name="#39", type=OCL_CollectionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="138", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuplePart40: BinaryAssociation = BinaryAssociation(
    name="tuplePart40",
    ends={
        Property(name="#42", type=OCL_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="141", type=TuplePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuple43: BinaryAssociation = BinaryAssociation(
    name="tuple43",
    ends={
        Property(name="#45", type=OCL_TuplePart, multiplicity=Multiplicity(1, 1)),
        Property(name="144", type=TupleExp, multiplicity=Multiplicity(1, 1))
    }
)
elements46: BinaryAssociation = BinaryAssociation(
    name="elements46",
    ends={
        Property(name="#48", type=OCL_MapExp, multiplicity=Multiplicity(1, 1)),
        Property(name="147", type=MapElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
map49: BinaryAssociation = BinaryAssociation(
    name="map49",
    ends={
        Property(name="#51", type=OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="150", type=MapExp, multiplicity=Multiplicity(1, 1))
    }
)
key52: BinaryAssociation = BinaryAssociation(
    name="key52",
    ends={
        Property(name="OclExpression", type=OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_MapElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value53: BinaryAssociation = BinaryAssociation(
    name="value53",
    ends={
        Property(name="OclExpression55", type=OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_MapElement54", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression77: BinaryAssociation = BinaryAssociation(
    name="thenExpression77",
    ends={
        Property(name="#79", type=OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="178", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source56: BinaryAssociation = BinaryAssociation(
    name="source56",
    ends={
        Property(name="#58", type=OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="157", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments59: BinaryAssociation = BinaryAssociation(
    name="arguments59",
    ends={
        Property(name="#61", type=OCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="160", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body62: BinaryAssociation = BinaryAssociation(
    name="body62",
    ends={
        Property(name="#64", type=OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="163", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterators65: BinaryAssociation = BinaryAssociation(
    name="iterators65",
    ends={
        Property(name="#67", type=OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="166", type=Iterator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result68: BinaryAssociation = BinaryAssociation(
    name="result68",
    ends={
        Property(name="#70", type=OCL_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="169", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable71: BinaryAssociation = BinaryAssociation(
    name="variable71",
    ends={
        Property(name="#73", type=OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="172", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in_74: BinaryAssociation = BinaryAssociation(
    name="in_74",
    ends={
        Property(name="#76", type=OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="175", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition80: BinaryAssociation = BinaryAssociation(
    name="condition80",
    ends={
        Property(name="#82", type=OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="181", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression83: BinaryAssociation = BinaryAssociation(
    name="elseExpression83",
    ends={
        Property(name="#85", type=OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="184", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type86: BinaryAssociation = BinaryAssociation(
    name="type86",
    ends={
        Property(name="#88", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="187", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression89: BinaryAssociation = BinaryAssociation(
    name="initExpression89",
    ends={
        Property(name="#91", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="190", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
letExp92: BinaryAssociation = BinaryAssociation(
    name="letExp92",
    ends={
        Property(name="#94", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="193", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
baseExp95: BinaryAssociation = BinaryAssociation(
    name="baseExp95",
    ends={
        Property(name="#97", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="196", type=IterateExp, multiplicity=Multiplicity(0, 1))
    }
)
variableExp98: BinaryAssociation = BinaryAssociation(
    name="variableExp98",
    ends={
        Property(name="#100", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="199", type=VariableExp, multiplicity=Multiplicity(0, 9999))
    }
)
loopExpr101: BinaryAssociation = BinaryAssociation(
    name="loopExpr101",
    ends={
        Property(name="#103", type=OCL_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="1102", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
operation104: BinaryAssociation = BinaryAssociation(
    name="operation104",
    ends={
        Property(name="#106", type=OCL_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="1105", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
elementType107: BinaryAssociation = BinaryAssociation(
    name="elementType107",
    ends={
        Property(name="#109", type=OCL_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="1108", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definitions110: BinaryAssociation = BinaryAssociation(
    name="definitions110",
    ends={
        Property(name="#112", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1111", type=OclContextDefinition, multiplicity=Multiplicity(0, 1))
    }
)
oclExpression113: BinaryAssociation = BinaryAssociation(
    name="oclExpression113",
    ends={
        Property(name="#115", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1114", type=OclExpression, multiplicity=Multiplicity(0, 1))
    }
)
operation116: BinaryAssociation = BinaryAssociation(
    name="operation116",
    ends={
        Property(name="#118", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1117", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
mapType2119: BinaryAssociation = BinaryAssociation(
    name="mapType2119",
    ends={
        Property(name="#121", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1120", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
attribute122: BinaryAssociation = BinaryAssociation(
    name="attribute122",
    ends={
        Property(name="#124", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1123", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
mapType125: BinaryAssociation = BinaryAssociation(
    name="mapType125",
    ends={
        Property(name="#127", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1126", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
collectionTypes128: BinaryAssociation = BinaryAssociation(
    name="collectionTypes128",
    ends={
        Property(name="#130", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1129", type=CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
tupleTypeAttribute131: BinaryAssociation = BinaryAssociation(
    name="tupleTypeAttribute131",
    ends={
        Property(name="#133", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1132", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclaration134: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration134",
    ends={
        Property(name="#136", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1135", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
context_164: BinaryAssociation = BinaryAssociation(
    name="context_164",
    ends={
        Property(name="#166", type=OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="1165", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attributes137: BinaryAssociation = BinaryAssociation(
    name="attributes137",
    ends={
        Property(name="#139", type=OCL_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="1138", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type140: BinaryAssociation = BinaryAssociation(
    name="type140",
    ends={
        Property(name="#142", type=OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="1141", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tupleType143: BinaryAssociation = BinaryAssociation(
    name="tupleType143",
    ends={
        Property(name="#145", type=OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="1144", type=TupleType, multiplicity=Multiplicity(1, 1))
    }
)
model146: BinaryAssociation = BinaryAssociation(
    name="model146",
    ends={
        Property(name="#148", type=OCL_OclModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="1147", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
valueType149: BinaryAssociation = BinaryAssociation(
    name="valueType149",
    ends={
        Property(name="#151", type=OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="1150", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
keyType152: BinaryAssociation = BinaryAssociation(
    name="keyType152",
    ends={
        Property(name="#154", type=OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="1153", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
feature155: BinaryAssociation = BinaryAssociation(
    name="feature155",
    ends={
        Property(name="#157", type=OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="1156", type=OclFeature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context_158: BinaryAssociation = BinaryAssociation(
    name="context_158",
    ends={
        Property(name="#160", type=OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="1159", type=OclContextDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition161: BinaryAssociation = BinaryAssociation(
    name="definition161",
    ends={
        Property(name="#163", type=OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="1162", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1))
    }
)
definition167: BinaryAssociation = BinaryAssociation(
    name="definition167",
    ends={
        Property(name="#169", type=OCL_OclFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="1168", type=OclFeatureDefinition, multiplicity=Multiplicity(0, 1))
    }
)
initExpression170: BinaryAssociation = BinaryAssociation(
    name="initExpression170",
    ends={
        Property(name="#172", type=OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="1171", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type173: BinaryAssociation = BinaryAssociation(
    name="type173",
    ends={
        Property(name="#175", type=OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="1174", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters176: BinaryAssociation = BinaryAssociation(
    name="parameters176",
    ends={
        Property(name="#178", type=OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="1177", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType179: BinaryAssociation = BinaryAssociation(
    name="returnType179",
    ends={
        Property(name="#181", type=OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="1180", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body182: BinaryAssociation = BinaryAssociation(
    name="body182",
    ends={
        Property(name="#184", type=OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="1183", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metamodel185: BinaryAssociation = BinaryAssociation(
    name="metamodel185",
    ends={
        Property(name="#187", type=OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="1186", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
elements188: BinaryAssociation = BinaryAssociation(
    name="elements188",
    ends={
        Property(name="#190", type=OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="1189", type=OclModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
model191: BinaryAssociation = BinaryAssociation(
    name="model191",
    ends={
        Property(name="#193", type=OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="1192", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_OCL_OclExpression_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclExpression)
gen_OCL_BooleanExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=OCL_BooleanExp)
gen_OCL_VariableExp_OclExpression = Generalization(general=OclExpression, specific=OCL_VariableExp)
gen_OCL_SuperExp_OclExpression = Generalization(general=OclExpression, specific=OCL_SuperExp)
gen_OCL_PrimitiveExp_OclExpression = Generalization(general=OclExpression, specific=OCL_PrimitiveExp)
gen_OCL_StringExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=OCL_StringExp)
gen_OCL_NumericExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=OCL_NumericExp)
gen_OCL_RealExp_NumericExp = Generalization(general=NumericExp, specific=OCL_RealExp)
gen_OCL_IntegerExp_NumericExp = Generalization(general=NumericExp, specific=OCL_IntegerExp)
gen_OCL_CollectionExp_OclExpression = Generalization(general=OclExpression, specific=OCL_CollectionExp)
gen_OCL_BagExp_CollectionExp = Generalization(general=CollectionExp, specific=OCL_BagExp)
gen_OCL_OrderedSetExp_CollectionExp = Generalization(general=CollectionExp, specific=OCL_OrderedSetExp)
gen_OCL_SequenceExp_CollectionExp = Generalization(general=CollectionExp, specific=OCL_SequenceExp)
gen_OCL_SetExp_CollectionExp = Generalization(general=CollectionExp, specific=OCL_SetExp)
gen_OCL_TupleExp_OclExpression = Generalization(general=OclExpression, specific=OCL_TupleExp)
gen_OCL_TuplePart_VariableDeclaration = Generalization(general=VariableDeclaration, specific=OCL_TuplePart)
gen_OCL_MapExp_OclExpression = Generalization(general=OclExpression, specific=OCL_MapExp)
gen_OCL_MapElement_LocatedElement = Generalization(general=LocatedElement, specific=OCL_MapElement)
gen_OCL_EnumLiteralExp_OclExpression = Generalization(general=OclExpression, specific=OCL_EnumLiteralExp)
gen_OCL_OclUndefinedExp_OclExpression = Generalization(general=OclExpression, specific=OCL_OclUndefinedExp)
gen_OCL_PropertyCallExp_OclExpression = Generalization(general=OclExpression, specific=OCL_PropertyCallExp)
gen_OCL_NavigationOrAttributeCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=OCL_NavigationOrAttributeCallExp)
gen_OCL_OperationCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=OCL_OperationCallExp)
gen_OCL_OperatorCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=OCL_OperatorCallExp)
gen_OCL_CollectionOperationCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=OCL_CollectionOperationCallExp)
gen_OCL_LoopExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=OCL_LoopExp)
gen_OCL_IterateExp_LoopExp = Generalization(general=LoopExp, specific=OCL_IterateExp)
gen_OCL_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=OCL_IteratorExp)
gen_OCL_LetExp_OclExpression = Generalization(general=OclExpression, specific=OCL_LetExp)
gen_OCL_IfExp_OclExpression = Generalization(general=OclExpression, specific=OCL_IfExp)
gen_OCL_VariableDeclaration_LocatedElement = Generalization(general=LocatedElement, specific=OCL_VariableDeclaration)
gen_OCL_Iterator_VariableDeclaration = Generalization(general=VariableDeclaration, specific=OCL_Iterator)
gen_OCL_Parameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=OCL_Parameter)
gen_OCL_CollectionType_OclType = Generalization(general=OclType, specific=OCL_CollectionType)
gen_OCL_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=OCL_OrderedSetType)
gen_OCL_SequenceType_CollectionType = Generalization(general=CollectionType, specific=OCL_SequenceType)
gen_OCL_OclType_OclExpression = Generalization(general=OclExpression, specific=OCL_OclType)
gen_OCL_Primitive_OclType = Generalization(general=OclType, specific=OCL_Primitive)
gen_OCL_StringType_Primitive = Generalization(general=Primitive, specific=OCL_StringType)
gen_OCL_BooleanType_Primitive = Generalization(general=Primitive, specific=OCL_BooleanType)
gen_OCL_NumericType_Primitive = Generalization(general=Primitive, specific=OCL_NumericType)
gen_OCL_IntegerType_NumericType = Generalization(general=NumericType, specific=OCL_IntegerType)
gen_OCL_RealType_NumericType = Generalization(general=NumericType, specific=OCL_RealType)
gen_OCL_BagType_CollectionType = Generalization(general=CollectionType, specific=OCL_BagType)
gen_OCL_SetType_CollectionType = Generalization(general=CollectionType, specific=OCL_SetType)
gen_OCL_OclAnyType_OclType = Generalization(general=OclType, specific=OCL_OclAnyType)
gen_OCL_TupleType_OclType = Generalization(general=OclType, specific=OCL_TupleType)
gen_OCL_TupleTypeAttribute_LocatedElement = Generalization(general=LocatedElement, specific=OCL_TupleTypeAttribute)
gen_OCL_OclModelElement_OclType = Generalization(general=OclType, specific=OCL_OclModelElement)
gen_OCL_MapType_OclType = Generalization(general=OclType, specific=OCL_MapType)
gen_OCL_OclFeatureDefinition_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclFeatureDefinition)
gen_OCL_OclContextDefinition_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclContextDefinition)
gen_OCL_OclFeature_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclFeature)
gen_OCL_Attribute_OclFeature = Generalization(general=OclFeature, specific=OCL_Attribute)
gen_OCL_Operation_OclFeature = Generalization(general=OclFeature, specific=OCL_Operation)
gen_OCL_OclModel_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclModel)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={ATL_LocatedElement, OCL_OclExpression, LocatedElement, OclType, OCL_BooleanExp, IfExp, PropertyCallExp, CollectionExp, LetExp, LoopExp, OperationCallExp, VariableDeclaration, Operation, Attribute, OCL_VariableExp, OclExpression, OCL_SuperExp, OCL_PrimitiveExp, OCL_StringExp, PrimitiveExp, OCL_NumericExp, OCL_RealExp, NumericExp, OCL_IntegerExp, OCL_CollectionExp, OCL_BagExp, OCL_OrderedSetExp, OCL_SequenceExp, OCL_SetExp, OCL_TupleExp, TuplePart, OCL_TuplePart, TupleExp, OCL_MapExp, MapElement, OCL_MapElement, MapExp, OCL_EnumLiteralExp, OCL_OclUndefinedExp, OCL_PropertyCallExp, OCL_NavigationOrAttributeCallExp, OCL_OperationCallExp, OCL_OperatorCallExp, OCL_CollectionOperationCallExp, OCL_LoopExp, Iterator, OCL_IterateExp, OCL_IteratorExp, OCL_LetExp, OCL_IfExp, OCL_OclType, OCL_VariableDeclaration, IterateExp, VariableExp, OCL_Iterator, OCL_Parameter, OCL_CollectionType, OCL_SequenceType, OclContextDefinition, MapType, CollectionType, TupleTypeAttribute, OCL_Primitive, OCL_StringType, Primitive, OCL_BooleanType, OCL_NumericType, OCL_IntegerType, NumericType, OCL_RealType, OCL_BagType, OCL_OrderedSetType, OCL_SetType, OCL_OclAnyType, OCL_TupleType, OCL_TupleTypeAttribute, TupleType, OCL_OclModelElement, OclModel, OCL_MapType, OCL_OclFeatureDefinition, OclFeature, OCL_OclContextDefinition, OclFeatureDefinition, OCL_OclFeature, OCL_Attribute, OCL_Operation, Parameter_, OCL_OclModel, OclModelElement},
    associations={type0, ifExp31, appliedProperty4, collection7, letExp10, loopExp13, parentOperation16, initializedVariable19, ifExp222, owningOperation25, ifExp128, owningAttribute31, referredVariable34, elements37, tuplePart40, tuple43, elements46, map49, key52, value53, thenExpression77, source56, arguments59, body62, iterators65, result68, variable71, in_74, condition80, elseExpression83, type86, initExpression89, letExp92, baseExp95, variableExp98, loopExpr101, operation104, elementType107, definitions110, oclExpression113, operation116, mapType2119, attribute122, mapType125, collectionTypes128, tupleTypeAttribute131, variableDeclaration134, context_164, attributes137, type140, tupleType143, model146, valueType149, keyType152, feature155, context_158, definition161, definition167, initExpression170, type173, parameters176, returnType179, body182, metamodel185, elements188, model191},
    generalizations={gen_OCL_OclExpression_LocatedElement, gen_OCL_BooleanExp_PrimitiveExp, gen_OCL_VariableExp_OclExpression, gen_OCL_SuperExp_OclExpression, gen_OCL_PrimitiveExp_OclExpression, gen_OCL_StringExp_PrimitiveExp, gen_OCL_NumericExp_PrimitiveExp, gen_OCL_RealExp_NumericExp, gen_OCL_IntegerExp_NumericExp, gen_OCL_CollectionExp_OclExpression, gen_OCL_BagExp_CollectionExp, gen_OCL_OrderedSetExp_CollectionExp, gen_OCL_SequenceExp_CollectionExp, gen_OCL_SetExp_CollectionExp, gen_OCL_TupleExp_OclExpression, gen_OCL_TuplePart_VariableDeclaration, gen_OCL_MapExp_OclExpression, gen_OCL_MapElement_LocatedElement, gen_OCL_EnumLiteralExp_OclExpression, gen_OCL_OclUndefinedExp_OclExpression, gen_OCL_PropertyCallExp_OclExpression, gen_OCL_NavigationOrAttributeCallExp_PropertyCallExp, gen_OCL_OperationCallExp_PropertyCallExp, gen_OCL_OperatorCallExp_OperationCallExp, gen_OCL_CollectionOperationCallExp_OperationCallExp, gen_OCL_LoopExp_PropertyCallExp, gen_OCL_IterateExp_LoopExp, gen_OCL_IteratorExp_LoopExp, gen_OCL_LetExp_OclExpression, gen_OCL_IfExp_OclExpression, gen_OCL_VariableDeclaration_LocatedElement, gen_OCL_Iterator_VariableDeclaration, gen_OCL_Parameter_VariableDeclaration, gen_OCL_CollectionType_OclType, gen_OCL_OrderedSetType_CollectionType, gen_OCL_SequenceType_CollectionType, gen_OCL_OclType_OclExpression, gen_OCL_Primitive_OclType, gen_OCL_StringType_Primitive, gen_OCL_BooleanType_Primitive, gen_OCL_NumericType_Primitive, gen_OCL_IntegerType_NumericType, gen_OCL_RealType_NumericType, gen_OCL_BagType_CollectionType, gen_OCL_SetType_CollectionType, gen_OCL_OclAnyType_OclType, gen_OCL_TupleType_OclType, gen_OCL_TupleTypeAttribute_LocatedElement, gen_OCL_OclModelElement_OclType, gen_OCL_MapType_OclType, gen_OCL_OclFeatureDefinition_LocatedElement, gen_OCL_OclContextDefinition_LocatedElement, gen_OCL_OclFeature_LocatedElement, gen_OCL_Attribute_OclFeature, gen_OCL_Operation_OclFeature, gen_OCL_OclModel_LocatedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)