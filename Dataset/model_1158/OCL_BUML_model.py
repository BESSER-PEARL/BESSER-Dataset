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
ATL_LocatedElement = Class(name="ATL_LocatedElement", is_abstract=True)
OCL_OclExpression = Class(name="OCL_OclExpression", is_abstract=True)
LocatedElement = Class(name="LocatedElement")
OclType = Class(name="OclType")
IfExp = Class(name="IfExp")
PropertyCallExp = Class(name="PropertyCallExp")
CollectionExp = Class(name="CollectionExp")
LetExp = Class(name="LetExp")
LoopExp = Class(name="LoopExp")
OCL_SuperExp = Class(name="OCL_SuperExp")
OCL_PrimitiveExp = Class(name="OCL_PrimitiveExp", is_abstract=True)
OCL_StringExp = Class(name="OCL_StringExp")
PrimitiveExp = Class(name="PrimitiveExp")
OCL_BooleanExp = Class(name="OCL_BooleanExp")
OCL_NumericExp = Class(name="OCL_NumericExp", is_abstract=True)
OCL_RealExp = Class(name="OCL_RealExp")
NumericExp = Class(name="NumericExp")
OCL_IntegerExp = Class(name="OCL_IntegerExp")
OCL_CollectionExp = Class(name="OCL_CollectionExp", is_abstract=True)
OCL_BagExp = Class(name="OCL_BagExp")
OCL_OrderedSetExp = Class(name="OCL_OrderedSetExp")
OCL_SequenceExp = Class(name="OCL_SequenceExp")
OCL_SetExp = Class(name="OCL_SetExp")
OCL_TupleExp = Class(name="OCL_TupleExp")
OperationCallExp = Class(name="OperationCallExp")
VariableDeclaration = Class(name="VariableDeclaration")
Operation = Class(name="Operation")
Attribute = Class(name="Attribute")
OCL_VariableExp = Class(name="OCL_VariableExp")
OclExpression = Class(name="OclExpression")
OCL_EnumLiteralExp = Class(name="OCL_EnumLiteralExp")
OCL_OclUndefinedExp = Class(name="OCL_OclUndefinedExp")
OCL_PropertyCallExp = Class(name="OCL_PropertyCallExp", is_abstract=True)
OCL_NavigationOrAttributeCallExp = Class(name="OCL_NavigationOrAttributeCallExp")
OCL_OperationCallExp = Class(name="OCL_OperationCallExp")
OCL_OperatorCallExp = Class(name="OCL_OperatorCallExp")
OCL_CollectionOperationCallExp = Class(name="OCL_CollectionOperationCallExp")
TuplePart = Class(name="TuplePart")
OCL_TuplePart = Class(name="OCL_TuplePart")
TupleExp = Class(name="TupleExp")
OCL_MapExp = Class(name="OCL_MapExp")
MapElement = Class(name="MapElement")
OCL_MapElement = Class(name="OCL_MapElement")
MapExp = Class(name="MapExp")
OCL_IfExp = Class(name="OCL_IfExp")
OCL_VariableDeclaration = Class(name="OCL_VariableDeclaration")
OCL_LoopExp = Class(name="OCL_LoopExp", is_abstract=True)
Iterator = Class(name="Iterator")
OCL_IterateExp = Class(name="OCL_IterateExp")
OCL_IteratorExp = Class(name="OCL_IteratorExp")
OCL_LetExp = Class(name="OCL_LetExp")
OCL_OclType = Class(name="OCL_OclType")
OclContextDefinition = Class(name="OclContextDefinition")
MapType = Class(name="MapType")
CollectionType = Class(name="CollectionType")
TupleTypeAttribute = Class(name="TupleTypeAttribute")
IterateExp = Class(name="IterateExp")
VariableExp = Class(name="VariableExp")
OCL_Iterator = Class(name="OCL_Iterator")
OCL_Parameter = Class(name="OCL_Parameter")
OCL_CollectionType = Class(name="OCL_CollectionType")
OCL_SetType = Class(name="OCL_SetType")
OCL_OclAnyType = Class(name="OCL_OclAnyType")
OCL_TupleType = Class(name="OCL_TupleType")
OCL_TupleTypeAttribute = Class(name="OCL_TupleTypeAttribute")
TupleType = Class(name="TupleType")
OCL_OclModelElement = Class(name="OCL_OclModelElement")
OclModel = Class(name="OclModel")
OCL_MapType = Class(name="OCL_MapType")
OCL_Primitive = Class(name="OCL_Primitive", is_abstract=True)
OCL_StringType = Class(name="OCL_StringType")
Primitive = Class(name="Primitive")
OCL_BooleanType = Class(name="OCL_BooleanType")
OCL_NumericType = Class(name="OCL_NumericType", is_abstract=True)
OCL_IntegerType = Class(name="OCL_IntegerType")
NumericType = Class(name="NumericType")
OCL_RealType = Class(name="OCL_RealType")
OCL_BagType = Class(name="OCL_BagType")
OCL_OrderedSetType = Class(name="OCL_OrderedSetType")
OCL_SequenceType = Class(name="OCL_SequenceType")
OCL_Attribute = Class(name="OCL_Attribute")
OCL_Operation = Class(name="OCL_Operation")
Parameter_ = Class(name="Parameter")
OCL_OclFeatureDefinition = Class(name="OCL_OclFeatureDefinition")
OclFeature = Class(name="OclFeature")
OCL_OclContextDefinition = Class(name="OCL_OclContextDefinition")
OclFeatureDefinition = Class(name="OclFeatureDefinition")
OCL_OclFeature = Class(name="OCL_OclFeature", is_abstract=True)
OCL_OclModel = Class(name="OCL_OclModel")
OclModelElement = Class(name="OclModelElement")

# ATL_LocatedElement class attributes and methods
ATL_LocatedElement_location: Property = Property(name="location", type=StringType)
ATL_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
ATL_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
ATL_LocatedElement.attributes={ATL_LocatedElement_commentsBefore, ATL_LocatedElement_location, ATL_LocatedElement_commentsAfter}

# OCL_OclExpression class attributes and methods

# LocatedElement class attributes and methods

# OclType class attributes and methods

# IfExp class attributes and methods

# PropertyCallExp class attributes and methods

# CollectionExp class attributes and methods

# LetExp class attributes and methods

# LoopExp class attributes and methods

# OCL_SuperExp class attributes and methods

# OCL_PrimitiveExp class attributes and methods

# OCL_StringExp class attributes and methods
OCL_StringExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
OCL_StringExp.attributes={OCL_StringExp_stringSymbol}

# PrimitiveExp class attributes and methods

# OCL_BooleanExp class attributes and methods
OCL_BooleanExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
OCL_BooleanExp.attributes={OCL_BooleanExp_booleanSymbol}

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

# OperationCallExp class attributes and methods

# VariableDeclaration class attributes and methods

# Operation class attributes and methods

# Attribute class attributes and methods

# OCL_VariableExp class attributes and methods

# OclExpression class attributes and methods

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

# TuplePart class attributes and methods

# OCL_TuplePart class attributes and methods

# TupleExp class attributes and methods

# OCL_MapExp class attributes and methods

# MapElement class attributes and methods

# OCL_MapElement class attributes and methods

# MapExp class attributes and methods

# OCL_IfExp class attributes and methods

# OCL_VariableDeclaration class attributes and methods
OCL_VariableDeclaration_id: Property = Property(name="id", type=StringType)
OCL_VariableDeclaration_varName: Property = Property(name="varName", type=StringType)
OCL_VariableDeclaration.attributes={OCL_VariableDeclaration_varName, OCL_VariableDeclaration_id}

# OCL_LoopExp class attributes and methods

# Iterator class attributes and methods

# OCL_IterateExp class attributes and methods

# OCL_IteratorExp class attributes and methods
OCL_IteratorExp_name: Property = Property(name="name", type=StringType)
OCL_IteratorExp.attributes={OCL_IteratorExp_name}

# OCL_LetExp class attributes and methods

# OCL_OclType class attributes and methods
OCL_OclType_name: Property = Property(name="name", type=StringType)
OCL_OclType.attributes={OCL_OclType_name}

# OclContextDefinition class attributes and methods

# MapType class attributes and methods

# CollectionType class attributes and methods

# TupleTypeAttribute class attributes and methods

# IterateExp class attributes and methods

# VariableExp class attributes and methods

# OCL_Iterator class attributes and methods

# OCL_Parameter class attributes and methods

# OCL_CollectionType class attributes and methods

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

# OCL_SequenceType class attributes and methods

# OCL_Attribute class attributes and methods
OCL_Attribute_name: Property = Property(name="name", type=StringType)
OCL_Attribute.attributes={OCL_Attribute_name}

# OCL_Operation class attributes and methods
OCL_Operation_name: Property = Property(name="name", type=StringType)
OCL_Operation.attributes={OCL_Operation_name}

# Parameter class attributes and methods

# OCL_OclFeatureDefinition class attributes and methods

# OclFeature class attributes and methods

# OCL_OclContextDefinition class attributes and methods

# OclFeatureDefinition class attributes and methods

# OCL_OclFeature class attributes and methods

# OCL_OclModel class attributes and methods
OCL_OclModel_name: Property = Property(name="name", type=StringType)
OCL_OclModel.attributes={OCL_OclModel_name}

# OclModelElement class attributes and methods

# Relationships
type0: BinaryAssociation = BinaryAssociation(
    name="type0",
    ends={
        Property(name="OclType", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="oclExpression", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifExp31: BinaryAssociation = BinaryAssociation(
    name="ifExp31",
    ends={
        Property(name="IfExp", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="elseExpression", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
appliedProperty2: BinaryAssociation = BinaryAssociation(
    name="appliedProperty2",
    ends={
        Property(name="PropertyCallExp", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=PropertyCallExp, multiplicity=Multiplicity(0, 1))
    }
)
collection3: BinaryAssociation = BinaryAssociation(
    name="collection3",
    ends={
        Property(name="CollectionExp", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=CollectionExp, multiplicity=Multiplicity(0, 1))
    }
)
letExp4: BinaryAssociation = BinaryAssociation(
    name="letExp4",
    ends={
        Property(name="LetExp", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="in_", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
loopExp5: BinaryAssociation = BinaryAssociation(
    name="loopExp5",
    ends={
        Property(name="LoopExp", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="body", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable16: BinaryAssociation = BinaryAssociation(
    name="referredVariable16",
    ends={
        Property(name="VariableDeclaration17", type=OCL_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="variableExp", type=VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
elements18: BinaryAssociation = BinaryAssociation(
    name="elements18",
    ends={
        Property(name="OclExpression", type=OCL_CollectionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="collection", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentOperation6: BinaryAssociation = BinaryAssociation(
    name="parentOperation6",
    ends={
        Property(name="OperationCallExp", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="arguments", type=OperationCallExp, multiplicity=Multiplicity(0, 1))
    }
)
initializedVariable7: BinaryAssociation = BinaryAssociation(
    name="initializedVariable7",
    ends={
        Property(name="VariableDeclaration", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="initExpression", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
ifExp28: BinaryAssociation = BinaryAssociation(
    name="ifExp28",
    ends={
        Property(name="IfExp9", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thenExpression", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningOperation10: BinaryAssociation = BinaryAssociation(
    name="owningOperation10",
    ends={
        Property(name="Operation", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="body11", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
ifExp112: BinaryAssociation = BinaryAssociation(
    name="ifExp112",
    ends={
        Property(name="IfExp13", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="condition", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningAttribute14: BinaryAssociation = BinaryAssociation(
    name="owningAttribute14",
    ends={
        Property(name="Attribute", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="initExpression15", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
value26: BinaryAssociation = BinaryAssociation(
    name="value26",
    ends={
        Property(name="OclExpression28", type=OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_MapElement27", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source29: BinaryAssociation = BinaryAssociation(
    name="source29",
    ends={
        Property(name="OclExpression30", type=OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="appliedProperty", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments31: BinaryAssociation = BinaryAssociation(
    name="arguments31",
    ends={
        Property(name="OclExpression32", type=OCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="parentOperation", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuplePart19: BinaryAssociation = BinaryAssociation(
    name="tuplePart19",
    ends={
        Property(name="TuplePart", type=OCL_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="tuple", type=TuplePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuple20: BinaryAssociation = BinaryAssociation(
    name="tuple20",
    ends={
        Property(name="TupleExp", type=OCL_TuplePart, multiplicity=Multiplicity(1, 1)),
        Property(name="tuplePart", type=TupleExp, multiplicity=Multiplicity(1, 1))
    }
)
elements21: BinaryAssociation = BinaryAssociation(
    name="elements21",
    ends={
        Property(name="MapElement", type=OCL_MapExp, multiplicity=Multiplicity(1, 1)),
        Property(name="map", type=MapElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
map22: BinaryAssociation = BinaryAssociation(
    name="map22",
    ends={
        Property(name="MapExp", type=OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements23", type=MapExp, multiplicity=Multiplicity(1, 1))
    }
)
key24: BinaryAssociation = BinaryAssociation(
    name="key24",
    ends={
        Property(name="OclExpression25", type=OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_MapElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in_40: BinaryAssociation = BinaryAssociation(
    name="in_40",
    ends={
        Property(name="OclExpression42", type=OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="letExp41", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression43: BinaryAssociation = BinaryAssociation(
    name="thenExpression43",
    ends={
        Property(name="OclExpression44", type=OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp2", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition45: BinaryAssociation = BinaryAssociation(
    name="condition45",
    ends={
        Property(name="OclExpression46", type=OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp1", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression47: BinaryAssociation = BinaryAssociation(
    name="elseExpression47",
    ends={
        Property(name="OclExpression48", type=OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp3", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type49: BinaryAssociation = BinaryAssociation(
    name="type49",
    ends={
        Property(name="OclType50", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variableDeclaration", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression51: BinaryAssociation = BinaryAssociation(
    name="initExpression51",
    ends={
        Property(name="OclExpression52", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="initializedVariable", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body33: BinaryAssociation = BinaryAssociation(
    name="body33",
    ends={
        Property(name="OclExpression34", type=OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="loopExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterators35: BinaryAssociation = BinaryAssociation(
    name="iterators35",
    ends={
        Property(name="Iterator", type=OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="loopExpr", type=Iterator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result36: BinaryAssociation = BinaryAssociation(
    name="result36",
    ends={
        Property(name="VariableDeclaration37", type=OCL_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="baseExp", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable38: BinaryAssociation = BinaryAssociation(
    name="variable38",
    ends={
        Property(name="VariableDeclaration39", type=OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="letExp", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definitions63: BinaryAssociation = BinaryAssociation(
    name="definitions63",
    ends={
        Property(name="OclContextDefinition", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="context_", type=OclContextDefinition, multiplicity=Multiplicity(0, 1))
    }
)
oclExpression64: BinaryAssociation = BinaryAssociation(
    name="oclExpression64",
    ends={
        Property(name="OclExpression65", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=OclExpression, multiplicity=Multiplicity(0, 1))
    }
)
operation66: BinaryAssociation = BinaryAssociation(
    name="operation66",
    ends={
        Property(name="Operation67", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="returnType", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
mapType268: BinaryAssociation = BinaryAssociation(
    name="mapType268",
    ends={
        Property(name="MapType", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="valueType", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
attribute69: BinaryAssociation = BinaryAssociation(
    name="attribute69",
    ends={
        Property(name="Attribute71", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type70", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
mapType72: BinaryAssociation = BinaryAssociation(
    name="mapType72",
    ends={
        Property(name="MapType73", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="keyType", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
collectionTypes74: BinaryAssociation = BinaryAssociation(
    name="collectionTypes74",
    ends={
        Property(name="CollectionType", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="elementType", type=CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
letExp53: BinaryAssociation = BinaryAssociation(
    name="letExp53",
    ends={
        Property(name="LetExp54", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
baseExp55: BinaryAssociation = BinaryAssociation(
    name="baseExp55",
    ends={
        Property(name="IterateExp", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="result", type=IterateExp, multiplicity=Multiplicity(0, 1))
    }
)
variableExp56: BinaryAssociation = BinaryAssociation(
    name="variableExp56",
    ends={
        Property(name="VariableExp", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="referredVariable", type=VariableExp, multiplicity=Multiplicity(0, 9999))
    }
)
loopExpr57: BinaryAssociation = BinaryAssociation(
    name="loopExpr57",
    ends={
        Property(name="LoopExp58", type=OCL_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="iterators", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
operation59: BinaryAssociation = BinaryAssociation(
    name="operation59",
    ends={
        Property(name="Operation60", type=OCL_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
elementType61: BinaryAssociation = BinaryAssociation(
    name="elementType61",
    ends={
        Property(name="OclType62", type=OCL_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="collectionTypes", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attributes80: BinaryAssociation = BinaryAssociation(
    name="attributes80",
    ends={
        Property(name="TupleTypeAttribute81", type=OCL_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="tupleType", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type82: BinaryAssociation = BinaryAssociation(
    name="type82",
    ends={
        Property(name="OclType83", type=OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="tupleTypeAttribute", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tupleType84: BinaryAssociation = BinaryAssociation(
    name="tupleType84",
    ends={
        Property(name="TupleType", type=OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=TupleType, multiplicity=Multiplicity(1, 1))
    }
)
model85: BinaryAssociation = BinaryAssociation(
    name="model85",
    ends={
        Property(name="OclModel", type=OCL_OclModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements86", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
valueType87: BinaryAssociation = BinaryAssociation(
    name="valueType87",
    ends={
        Property(name="OclType88", type=OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="mapType2", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
keyType89: BinaryAssociation = BinaryAssociation(
    name="keyType89",
    ends={
        Property(name="OclType90", type=OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="mapType", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tupleTypeAttribute75: BinaryAssociation = BinaryAssociation(
    name="tupleTypeAttribute75",
    ends={
        Property(name="TupleTypeAttribute", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type76", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclaration77: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration77",
    ends={
        Property(name="VariableDeclaration79", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type78", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
definition99: BinaryAssociation = BinaryAssociation(
    name="definition99",
    ends={
        Property(name="OclFeatureDefinition100", type=OCL_OclFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=OclFeatureDefinition, multiplicity=Multiplicity(0, 1))
    }
)
initExpression101: BinaryAssociation = BinaryAssociation(
    name="initExpression101",
    ends={
        Property(name="OclExpression102", type=OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="owningAttribute", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type103: BinaryAssociation = BinaryAssociation(
    name="type103",
    ends={
        Property(name="OclType104", type=OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attribute", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters105: BinaryAssociation = BinaryAssociation(
    name="parameters105",
    ends={
        Property(name="Parameter", type=OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType106: BinaryAssociation = BinaryAssociation(
    name="returnType106",
    ends={
        Property(name="OclType108", type=OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation107", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body109: BinaryAssociation = BinaryAssociation(
    name="body109",
    ends={
        Property(name="OclExpression110", type=OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="owningOperation", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
feature91: BinaryAssociation = BinaryAssociation(
    name="feature91",
    ends={
        Property(name="OclFeature", type=OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definition", type=OclFeature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context_92: BinaryAssociation = BinaryAssociation(
    name="context_92",
    ends={
        Property(name="OclContextDefinition94", type=OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definition93", type=OclContextDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition95: BinaryAssociation = BinaryAssociation(
    name="definition95",
    ends={
        Property(name="OclFeatureDefinition", type=OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="context_96", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1))
    }
)
context_97: BinaryAssociation = BinaryAssociation(
    name="context_97",
    ends={
        Property(name="OclType98", type=OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definitions", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metamodel111: BinaryAssociation = BinaryAssociation(
    name="metamodel111",
    ends={
        Property(name="OclModel112", type=OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
elements113: BinaryAssociation = BinaryAssociation(
    name="elements113",
    ends={
        Property(name="OclModelElement", type=OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model114", type=OclModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
model115: BinaryAssociation = BinaryAssociation(
    name="model115",
    ends={
        Property(name="OclModel116", type=OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_OCL_OclExpression_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclExpression)
gen_OCL_SuperExp_OclExpression = Generalization(general=OclExpression, specific=OCL_SuperExp)
gen_OCL_PrimitiveExp_OclExpression = Generalization(general=OclExpression, specific=OCL_PrimitiveExp)
gen_OCL_StringExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=OCL_StringExp)
gen_OCL_BooleanExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=OCL_BooleanExp)
gen_OCL_NumericExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=OCL_NumericExp)
gen_OCL_RealExp_NumericExp = Generalization(general=NumericExp, specific=OCL_RealExp)
gen_OCL_IntegerExp_NumericExp = Generalization(general=NumericExp, specific=OCL_IntegerExp)
gen_OCL_CollectionExp_OclExpression = Generalization(general=OclExpression, specific=OCL_CollectionExp)
gen_OCL_BagExp_CollectionExp = Generalization(general=CollectionExp, specific=OCL_BagExp)
gen_OCL_OrderedSetExp_CollectionExp = Generalization(general=CollectionExp, specific=OCL_OrderedSetExp)
gen_OCL_SequenceExp_CollectionExp = Generalization(general=CollectionExp, specific=OCL_SequenceExp)
gen_OCL_SetExp_CollectionExp = Generalization(general=CollectionExp, specific=OCL_SetExp)
gen_OCL_TupleExp_OclExpression = Generalization(general=OclExpression, specific=OCL_TupleExp)
gen_OCL_VariableExp_OclExpression = Generalization(general=OclExpression, specific=OCL_VariableExp)
gen_OCL_EnumLiteralExp_OclExpression = Generalization(general=OclExpression, specific=OCL_EnumLiteralExp)
gen_OCL_OclUndefinedExp_OclExpression = Generalization(general=OclExpression, specific=OCL_OclUndefinedExp)
gen_OCL_PropertyCallExp_OclExpression = Generalization(general=OclExpression, specific=OCL_PropertyCallExp)
gen_OCL_NavigationOrAttributeCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=OCL_NavigationOrAttributeCallExp)
gen_OCL_OperationCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=OCL_OperationCallExp)
gen_OCL_OperatorCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=OCL_OperatorCallExp)
gen_OCL_CollectionOperationCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=OCL_CollectionOperationCallExp)
gen_OCL_TuplePart_VariableDeclaration = Generalization(general=VariableDeclaration, specific=OCL_TuplePart)
gen_OCL_MapExp_OclExpression = Generalization(general=OclExpression, specific=OCL_MapExp)
gen_OCL_MapElement_LocatedElement = Generalization(general=LocatedElement, specific=OCL_MapElement)
gen_OCL_IfExp_OclExpression = Generalization(general=OclExpression, specific=OCL_IfExp)
gen_OCL_VariableDeclaration_LocatedElement = Generalization(general=LocatedElement, specific=OCL_VariableDeclaration)
gen_OCL_LoopExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=OCL_LoopExp)
gen_OCL_IterateExp_LoopExp = Generalization(general=LoopExp, specific=OCL_IterateExp)
gen_OCL_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=OCL_IteratorExp)
gen_OCL_LetExp_OclExpression = Generalization(general=OclExpression, specific=OCL_LetExp)
gen_OCL_OclType_OclExpression = Generalization(general=OclExpression, specific=OCL_OclType)
gen_OCL_Iterator_VariableDeclaration = Generalization(general=VariableDeclaration, specific=OCL_Iterator)
gen_OCL_Parameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=OCL_Parameter)
gen_OCL_CollectionType_OclType = Generalization(general=OclType, specific=OCL_CollectionType)
gen_OCL_SetType_CollectionType = Generalization(general=CollectionType, specific=OCL_SetType)
gen_OCL_OclAnyType_OclType = Generalization(general=OclType, specific=OCL_OclAnyType)
gen_OCL_TupleType_OclType = Generalization(general=OclType, specific=OCL_TupleType)
gen_OCL_TupleTypeAttribute_LocatedElement = Generalization(general=LocatedElement, specific=OCL_TupleTypeAttribute)
gen_OCL_OclModelElement_OclType = Generalization(general=OclType, specific=OCL_OclModelElement)
gen_OCL_MapType_OclType = Generalization(general=OclType, specific=OCL_MapType)
gen_OCL_Primitive_OclType = Generalization(general=OclType, specific=OCL_Primitive)
gen_OCL_StringType_Primitive = Generalization(general=Primitive, specific=OCL_StringType)
gen_OCL_BooleanType_Primitive = Generalization(general=Primitive, specific=OCL_BooleanType)
gen_OCL_NumericType_Primitive = Generalization(general=Primitive, specific=OCL_NumericType)
gen_OCL_IntegerType_NumericType = Generalization(general=NumericType, specific=OCL_IntegerType)
gen_OCL_RealType_NumericType = Generalization(general=NumericType, specific=OCL_RealType)
gen_OCL_BagType_CollectionType = Generalization(general=CollectionType, specific=OCL_BagType)
gen_OCL_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=OCL_OrderedSetType)
gen_OCL_SequenceType_CollectionType = Generalization(general=CollectionType, specific=OCL_SequenceType)
gen_OCL_Attribute_OclFeature = Generalization(general=OclFeature, specific=OCL_Attribute)
gen_OCL_Operation_OclFeature = Generalization(general=OclFeature, specific=OCL_Operation)
gen_OCL_OclFeatureDefinition_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclFeatureDefinition)
gen_OCL_OclContextDefinition_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclContextDefinition)
gen_OCL_OclFeature_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclFeature)
gen_OCL_OclModel_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclModel)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={ATL_LocatedElement, OCL_OclExpression, LocatedElement, OclType, IfExp, PropertyCallExp, CollectionExp, LetExp, LoopExp, OCL_SuperExp, OCL_PrimitiveExp, OCL_StringExp, PrimitiveExp, OCL_BooleanExp, OCL_NumericExp, OCL_RealExp, NumericExp, OCL_IntegerExp, OCL_CollectionExp, OCL_BagExp, OCL_OrderedSetExp, OCL_SequenceExp, OCL_SetExp, OCL_TupleExp, OperationCallExp, VariableDeclaration, Operation, Attribute, OCL_VariableExp, OclExpression, OCL_EnumLiteralExp, OCL_OclUndefinedExp, OCL_PropertyCallExp, OCL_NavigationOrAttributeCallExp, OCL_OperationCallExp, OCL_OperatorCallExp, OCL_CollectionOperationCallExp, TuplePart, OCL_TuplePart, TupleExp, OCL_MapExp, MapElement, OCL_MapElement, MapExp, OCL_IfExp, OCL_VariableDeclaration, OCL_LoopExp, Iterator, OCL_IterateExp, OCL_IteratorExp, OCL_LetExp, OCL_OclType, OclContextDefinition, MapType, CollectionType, TupleTypeAttribute, IterateExp, VariableExp, OCL_Iterator, OCL_Parameter, OCL_CollectionType, OCL_SetType, OCL_OclAnyType, OCL_TupleType, OCL_TupleTypeAttribute, TupleType, OCL_OclModelElement, OclModel, OCL_MapType, OCL_Primitive, OCL_StringType, Primitive, OCL_BooleanType, OCL_NumericType, OCL_IntegerType, NumericType, OCL_RealType, OCL_BagType, OCL_OrderedSetType, OCL_SequenceType, OCL_Attribute, OCL_Operation, Parameter_, OCL_OclFeatureDefinition, OclFeature, OCL_OclContextDefinition, OclFeatureDefinition, OCL_OclFeature, OCL_OclModel, OclModelElement},
    associations={type0, ifExp31, appliedProperty2, collection3, letExp4, loopExp5, referredVariable16, elements18, parentOperation6, initializedVariable7, ifExp28, owningOperation10, ifExp112, owningAttribute14, value26, source29, arguments31, tuplePart19, tuple20, elements21, map22, key24, in_40, thenExpression43, condition45, elseExpression47, type49, initExpression51, body33, iterators35, result36, variable38, definitions63, oclExpression64, operation66, mapType268, attribute69, mapType72, collectionTypes74, letExp53, baseExp55, variableExp56, loopExpr57, operation59, elementType61, attributes80, type82, tupleType84, model85, valueType87, keyType89, tupleTypeAttribute75, variableDeclaration77, definition99, initExpression101, type103, parameters105, returnType106, body109, feature91, context_92, definition95, context_97, metamodel111, elements113, model115},
    generalizations={gen_OCL_OclExpression_LocatedElement, gen_OCL_SuperExp_OclExpression, gen_OCL_PrimitiveExp_OclExpression, gen_OCL_StringExp_PrimitiveExp, gen_OCL_BooleanExp_PrimitiveExp, gen_OCL_NumericExp_PrimitiveExp, gen_OCL_RealExp_NumericExp, gen_OCL_IntegerExp_NumericExp, gen_OCL_CollectionExp_OclExpression, gen_OCL_BagExp_CollectionExp, gen_OCL_OrderedSetExp_CollectionExp, gen_OCL_SequenceExp_CollectionExp, gen_OCL_SetExp_CollectionExp, gen_OCL_TupleExp_OclExpression, gen_OCL_VariableExp_OclExpression, gen_OCL_EnumLiteralExp_OclExpression, gen_OCL_OclUndefinedExp_OclExpression, gen_OCL_PropertyCallExp_OclExpression, gen_OCL_NavigationOrAttributeCallExp_PropertyCallExp, gen_OCL_OperationCallExp_PropertyCallExp, gen_OCL_OperatorCallExp_OperationCallExp, gen_OCL_CollectionOperationCallExp_OperationCallExp, gen_OCL_TuplePart_VariableDeclaration, gen_OCL_MapExp_OclExpression, gen_OCL_MapElement_LocatedElement, gen_OCL_IfExp_OclExpression, gen_OCL_VariableDeclaration_LocatedElement, gen_OCL_LoopExp_PropertyCallExp, gen_OCL_IterateExp_LoopExp, gen_OCL_IteratorExp_LoopExp, gen_OCL_LetExp_OclExpression, gen_OCL_OclType_OclExpression, gen_OCL_Iterator_VariableDeclaration, gen_OCL_Parameter_VariableDeclaration, gen_OCL_CollectionType_OclType, gen_OCL_SetType_CollectionType, gen_OCL_OclAnyType_OclType, gen_OCL_TupleType_OclType, gen_OCL_TupleTypeAttribute_LocatedElement, gen_OCL_OclModelElement_OclType, gen_OCL_MapType_OclType, gen_OCL_Primitive_OclType, gen_OCL_StringType_Primitive, gen_OCL_BooleanType_Primitive, gen_OCL_NumericType_Primitive, gen_OCL_IntegerType_NumericType, gen_OCL_RealType_NumericType, gen_OCL_BagType_CollectionType, gen_OCL_OrderedSetType_CollectionType, gen_OCL_SequenceType_CollectionType, gen_OCL_Attribute_OclFeature, gen_OCL_Operation_OclFeature, gen_OCL_OclFeatureDefinition_LocatedElement, gen_OCL_OclContextDefinition_LocatedElement, gen_OCL_OclFeature_LocatedElement, gen_OCL_OclModel_LocatedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)