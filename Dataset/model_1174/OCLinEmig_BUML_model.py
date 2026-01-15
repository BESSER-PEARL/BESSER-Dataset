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
OCLinEmig_OclExpression = Class(name="OCLinEmig::OclExpression", is_abstract=True)
LocatedElement = Class(name="LocatedElement")
OCLinEmig_OclType = Class(name="OCLinEmig::OclType")
OCLinEmig_IfExp = Class(name="OCLinEmig::IfExp")
OCLinEmig_PropertyCallExp = Class(name="OCLinEmig::PropertyCallExp", is_abstract=True)
OCLinEmig_CollectionExp = Class(name="OCLinEmig::CollectionExp", is_abstract=True)
OCLinEmig_LoopExp = Class(name="OCLinEmig::LoopExp", is_abstract=True)
OCLinEmig_OperationCallExp = Class(name="OCLinEmig::OperationCallExp")
OCLinEmig_VariableDeclaration = Class(name="OCLinEmig::VariableDeclaration")
OCLinEmig_Operation = Class(name="OCLinEmig::Operation")
OCLinEmig_Attribute = Class(name="OCLinEmig::Attribute")
OCLinEmig_VariableExp = Class(name="OCLinEmig::VariableExp")
OclExpression = Class(name="OclExpression")
OCLinEmig_StringExp = Class(name="OCLinEmig::StringExp")
PrimitiveExp = Class(name="PrimitiveExp")
OCLinEmig_LetExp = Class(name="OCLinEmig::LetExp")
OCLinEmig_BooleanExp = Class(name="OCLinEmig::BooleanExp")
OCLinEmig_NumericExp = Class(name="OCLinEmig::NumericExp", is_abstract=True)
OCLinEmig_RealExp = Class(name="OCLinEmig::RealExp")
NumericExp = Class(name="NumericExp")
OCLinEmig_IntegerExp = Class(name="OCLinEmig::IntegerExp")
OCLinEmig_BagExp = Class(name="OCLinEmig::BagExp")
CollectionExp = Class(name="CollectionExp")
OCLinEmig_OrderedSetExp = Class(name="OCLinEmig::OrderedSetExp")
OCLinEmig_SequenceExp = Class(name="OCLinEmig::SequenceExp")
OCLinEmig_SetExp = Class(name="OCLinEmig::SetExp")
OCLinEmig_TupleExp = Class(name="OCLinEmig::TupleExp")
OCLinEmig_SuperExp = Class(name="OCLinEmig::SuperExp")
OCLinEmig_PrimitiveExp = Class(name="OCLinEmig::PrimitiveExp", is_abstract=True)
OCLinEmig_MapExp = Class(name="OCLinEmig::MapExp")
OCLinEmig_MapElement = Class(name="OCLinEmig::MapElement")
OCLinEmig_EnumLiteralExp = Class(name="OCLinEmig::EnumLiteralExp")
OCLinEmig_OclUndefinedExp = Class(name="OCLinEmig::OclUndefinedExp")
OCLinEmig_NavigationOrAttributeCallExp = Class(name="OCLinEmig::NavigationOrAttributeCallExp")
PropertyCallExp = Class(name="PropertyCallExp")
OCLinEmig_TuplePart = Class(name="OCLinEmig::TuplePart")
VariableDeclaration = Class(name="VariableDeclaration")
OCLinEmig_Iterator = Class(name="OCLinEmig::Iterator")
OCLinEmig_IterateExp = Class(name="OCLinEmig::IterateExp")
LoopExp = Class(name="LoopExp")
OCLinEmig_IteratorExp = Class(name="OCLinEmig::IteratorExp")
OCLinEmig_OperatorCallExp = Class(name="OCLinEmig::OperatorCallExp")
OperationCallExp = Class(name="OperationCallExp")
OCLinEmig_CollectionOperationCallExp = Class(name="OCLinEmig::CollectionOperationCallExp")
OCLinEmig_Parameter = Class(name="OCLinEmig::Parameter")
OCLinEmig_CollectionType = Class(name="OCLinEmig::CollectionType")
OclType = Class(name="OclType")
OCLinEmig_OclContextDefinition = Class(name="OCLinEmig::OclContextDefinition")
OCLinEmig_TupleTypeAttribute = Class(name="OCLinEmig::TupleTypeAttribute")
OCLinEmig_Primitive = Class(name="OCLinEmig::Primitive", is_abstract=True)
OCLinEmig_StringType = Class(name="OCLinEmig::StringType")
Primitive = Class(name="Primitive")
OCLinEmig_BooleanType = Class(name="OCLinEmig::BooleanType")
OCLinEmig_NumericType = Class(name="OCLinEmig::NumericType", is_abstract=True)
OCLinEmig_IntegerType = Class(name="OCLinEmig::IntegerType")
NumericType = Class(name="NumericType")
OCLinEmig_RealType = Class(name="OCLinEmig::RealType")
OCLinEmig_BagType = Class(name="OCLinEmig::BagType")
CollectionType = Class(name="CollectionType")
OCLinEmig_OrderedSetType = Class(name="OCLinEmig::OrderedSetType")
OCLinEmig_SequenceType = Class(name="OCLinEmig::SequenceType")
OCLinEmig_SetType = Class(name="OCLinEmig::SetType")
OCLinEmig_OclAnyType = Class(name="OCLinEmig::OclAnyType")
OCLinEmig_TupleType = Class(name="OCLinEmig::TupleType")
OCLinEmig_MapType = Class(name="OCLinEmig::MapType")
OCLinEmig_OclModelElement = Class(name="OCLinEmig::OclModelElement")
OCLinEmig_OclModel = Class(name="OCLinEmig::OclModel")
OCLinEmig_OclFeatureDefinition = Class(name="OCLinEmig::OclFeatureDefinition")
OCLinEmig_OclFeature = Class(name="OCLinEmig::OclFeature", is_abstract=True)
OCLinEmig_LocatedElement = Class(name="OCLinEmig::LocatedElement", is_abstract=True)
OCLinEmig_Module = Class(name="OCLinEmig::Module")
OclFeature = Class(name="OclFeature")

# OCLinEmig_OclExpression class attributes and methods

# LocatedElement class attributes and methods

# OCLinEmig_OclType class attributes and methods
OCLinEmig_OclType_name: Property = Property(name="name", type=StringType)
OCLinEmig_OclType.attributes={OCLinEmig_OclType_name}

# OCLinEmig_IfExp class attributes and methods

# OCLinEmig_PropertyCallExp class attributes and methods

# OCLinEmig_CollectionExp class attributes and methods

# OCLinEmig_LoopExp class attributes and methods

# OCLinEmig_OperationCallExp class attributes and methods
OCLinEmig_OperationCallExp_operationName: Property = Property(name="operationName", type=StringType)
OCLinEmig_OperationCallExp.attributes={OCLinEmig_OperationCallExp_operationName}

# OCLinEmig_VariableDeclaration class attributes and methods
OCLinEmig_VariableDeclaration_id: Property = Property(name="id", type=StringType)
OCLinEmig_VariableDeclaration_varName: Property = Property(name="varName", type=StringType)
OCLinEmig_VariableDeclaration.attributes={OCLinEmig_VariableDeclaration_id, OCLinEmig_VariableDeclaration_varName}

# OCLinEmig_Operation class attributes and methods
OCLinEmig_Operation_name: Property = Property(name="name", type=StringType)
OCLinEmig_Operation.attributes={OCLinEmig_Operation_name}

# OCLinEmig_Attribute class attributes and methods
OCLinEmig_Attribute_name: Property = Property(name="name", type=StringType)
OCLinEmig_Attribute.attributes={OCLinEmig_Attribute_name}

# OCLinEmig_VariableExp class attributes and methods

# OclExpression class attributes and methods

# OCLinEmig_StringExp class attributes and methods
OCLinEmig_StringExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
OCLinEmig_StringExp.attributes={OCLinEmig_StringExp_stringSymbol}

# PrimitiveExp class attributes and methods

# OCLinEmig_LetExp class attributes and methods

# OCLinEmig_BooleanExp class attributes and methods
OCLinEmig_BooleanExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
OCLinEmig_BooleanExp.attributes={OCLinEmig_BooleanExp_booleanSymbol}

# OCLinEmig_NumericExp class attributes and methods

# OCLinEmig_RealExp class attributes and methods
OCLinEmig_RealExp_realSymbol: Property = Property(name="realSymbol", type=StringType)
OCLinEmig_RealExp.attributes={OCLinEmig_RealExp_realSymbol}

# NumericExp class attributes and methods

# OCLinEmig_IntegerExp class attributes and methods
OCLinEmig_IntegerExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
OCLinEmig_IntegerExp.attributes={OCLinEmig_IntegerExp_integerSymbol}

# OCLinEmig_BagExp class attributes and methods

# CollectionExp class attributes and methods

# OCLinEmig_OrderedSetExp class attributes and methods

# OCLinEmig_SequenceExp class attributes and methods

# OCLinEmig_SetExp class attributes and methods

# OCLinEmig_TupleExp class attributes and methods

# OCLinEmig_SuperExp class attributes and methods

# OCLinEmig_PrimitiveExp class attributes and methods

# OCLinEmig_MapExp class attributes and methods

# OCLinEmig_MapElement class attributes and methods

# OCLinEmig_EnumLiteralExp class attributes and methods
OCLinEmig_EnumLiteralExp_name: Property = Property(name="name", type=StringType)
OCLinEmig_EnumLiteralExp.attributes={OCLinEmig_EnumLiteralExp_name}

# OCLinEmig_OclUndefinedExp class attributes and methods

# OCLinEmig_NavigationOrAttributeCallExp class attributes and methods
OCLinEmig_NavigationOrAttributeCallExp_name: Property = Property(name="name", type=StringType)
OCLinEmig_NavigationOrAttributeCallExp.attributes={OCLinEmig_NavigationOrAttributeCallExp_name}

# PropertyCallExp class attributes and methods

# OCLinEmig_TuplePart class attributes and methods

# VariableDeclaration class attributes and methods

# OCLinEmig_Iterator class attributes and methods

# OCLinEmig_IterateExp class attributes and methods

# LoopExp class attributes and methods

# OCLinEmig_IteratorExp class attributes and methods
OCLinEmig_IteratorExp_name: Property = Property(name="name", type=StringType)
OCLinEmig_IteratorExp.attributes={OCLinEmig_IteratorExp_name}

# OCLinEmig_OperatorCallExp class attributes and methods

# OperationCallExp class attributes and methods

# OCLinEmig_CollectionOperationCallExp class attributes and methods

# OCLinEmig_Parameter class attributes and methods

# OCLinEmig_CollectionType class attributes and methods

# OclType class attributes and methods

# OCLinEmig_OclContextDefinition class attributes and methods

# OCLinEmig_TupleTypeAttribute class attributes and methods
OCLinEmig_TupleTypeAttribute_name: Property = Property(name="name", type=StringType)
OCLinEmig_TupleTypeAttribute.attributes={OCLinEmig_TupleTypeAttribute_name}

# OCLinEmig_Primitive class attributes and methods

# OCLinEmig_StringType class attributes and methods

# Primitive class attributes and methods

# OCLinEmig_BooleanType class attributes and methods

# OCLinEmig_NumericType class attributes and methods

# OCLinEmig_IntegerType class attributes and methods

# NumericType class attributes and methods

# OCLinEmig_RealType class attributes and methods

# OCLinEmig_BagType class attributes and methods

# CollectionType class attributes and methods

# OCLinEmig_OrderedSetType class attributes and methods

# OCLinEmig_SequenceType class attributes and methods

# OCLinEmig_SetType class attributes and methods

# OCLinEmig_OclAnyType class attributes and methods

# OCLinEmig_TupleType class attributes and methods

# OCLinEmig_MapType class attributes and methods

# OCLinEmig_OclModelElement class attributes and methods

# OCLinEmig_OclModel class attributes and methods
OCLinEmig_OclModel_name: Property = Property(name="name", type=StringType)
OCLinEmig_OclModel.attributes={OCLinEmig_OclModel_name}

# OCLinEmig_OclFeatureDefinition class attributes and methods

# OCLinEmig_OclFeature class attributes and methods

# OCLinEmig_LocatedElement class attributes and methods
OCLinEmig_LocatedElement_location: Property = Property(name="location", type=StringType)
OCLinEmig_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
OCLinEmig_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
OCLinEmig_LocatedElement.attributes={OCLinEmig_LocatedElement_location, OCLinEmig_LocatedElement_commentsAfter, OCLinEmig_LocatedElement_commentsBefore}

# OCLinEmig_Module class attributes and methods
OCLinEmig_Module_name: Property = Property(name="name", type=StringType)
OCLinEmig_Module.attributes={OCLinEmig_Module_name}

# OclFeature class attributes and methods

# Relationships
type0: BinaryAssociation = BinaryAssociation(
    name="type0",
    ends={
        Property(name="OclType", type=OCLinEmig_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="oclExpression", type=OCLinEmig_OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifExp31: BinaryAssociation = BinaryAssociation(
    name="ifExp31",
    ends={
        Property(name="IfExp", type=OCLinEmig_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="elseExpression", type=OCLinEmig_IfExp, multiplicity=Multiplicity(0, 1))
    }
)
appliedProperty2: BinaryAssociation = BinaryAssociation(
    name="appliedProperty2",
    ends={
        Property(name="PropertyCallExp", type=OCLinEmig_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=OCLinEmig_PropertyCallExp, multiplicity=Multiplicity(0, 1))
    }
)
collection3: BinaryAssociation = BinaryAssociation(
    name="collection3",
    ends={
        Property(name="CollectionExp", type=OCLinEmig_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=OCLinEmig_CollectionExp, multiplicity=Multiplicity(0, 1))
    }
)
loopExp5: BinaryAssociation = BinaryAssociation(
    name="loopExp5",
    ends={
        Property(name="LoopExp", type=OCLinEmig_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="body", type=OCLinEmig_LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
parentOperation6: BinaryAssociation = BinaryAssociation(
    name="parentOperation6",
    ends={
        Property(name="OperationCallExp", type=OCLinEmig_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="arguments", type=OCLinEmig_OperationCallExp, multiplicity=Multiplicity(0, 1))
    }
)
initializedVariable7: BinaryAssociation = BinaryAssociation(
    name="initializedVariable7",
    ends={
        Property(name="VariableDeclaration", type=OCLinEmig_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="initExpression", type=OCLinEmig_VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
ifExp28: BinaryAssociation = BinaryAssociation(
    name="ifExp28",
    ends={
        Property(name="IfExp9", type=OCLinEmig_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thenExpression", type=OCLinEmig_IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningOperation10: BinaryAssociation = BinaryAssociation(
    name="owningOperation10",
    ends={
        Property(name="Operation", type=OCLinEmig_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="body11", type=OCLinEmig_Operation, multiplicity=Multiplicity(0, 1))
    }
)
ifExp112: BinaryAssociation = BinaryAssociation(
    name="ifExp112",
    ends={
        Property(name="IfExp13", type=OCLinEmig_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="condition", type=OCLinEmig_IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningAttribute14: BinaryAssociation = BinaryAssociation(
    name="owningAttribute14",
    ends={
        Property(name="Attribute", type=OCLinEmig_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="initExpression15", type=OCLinEmig_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
letExp4: BinaryAssociation = BinaryAssociation(
    name="letExp4",
    ends={
        Property(name="LetExp", type=OCLinEmig_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="in_", type=OCLinEmig_LetExp, multiplicity=Multiplicity(0, 1))
    }
)
elements18: BinaryAssociation = BinaryAssociation(
    name="elements18",
    ends={
        Property(name="OclExpression", type=OCLinEmig_CollectionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="collection", type=OCLinEmig_OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredVariable16: BinaryAssociation = BinaryAssociation(
    name="referredVariable16",
    ends={
        Property(name="VariableDeclaration17", type=OCLinEmig_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="variableExp", type=OCLinEmig_VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
tuple20: BinaryAssociation = BinaryAssociation(
    name="tuple20",
    ends={
        Property(name="tuplePart", type=OCLinEmig_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleExp", type=OCLinEmig_TuplePart, multiplicity=Multiplicity(1, 1))
    }
)
elements21: BinaryAssociation = BinaryAssociation(
    name="elements21",
    ends={
        Property(name="MapElement", type=OCLinEmig_MapExp, multiplicity=Multiplicity(1, 1)),
        Property(name="map", type=OCLinEmig_MapElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
map22: BinaryAssociation = BinaryAssociation(
    name="map22",
    ends={
        Property(name="MapExp", type=OCLinEmig_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements23", type=OCLinEmig_MapExp, multiplicity=Multiplicity(1, 1))
    }
)
key24: BinaryAssociation = BinaryAssociation(
    name="key24",
    ends={
        Property(name="OCLinEmig_OclExpression", type=OCLinEmig_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OCLinEmig_MapElement", type=OCLinEmig_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value25: BinaryAssociation = BinaryAssociation(
    name="value25",
    ends={
        Property(name="OCLinEmig_OclExpression27", type=OCLinEmig_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OCLinEmig_MapElement26", type=OCLinEmig_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source28: BinaryAssociation = BinaryAssociation(
    name="source28",
    ends={
        Property(name="OclExpression29", type=OCLinEmig_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="appliedProperty", type=OCLinEmig_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments30: BinaryAssociation = BinaryAssociation(
    name="arguments30",
    ends={
        Property(name="OclExpression31", type=OCLinEmig_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="parentOperation", type=OCLinEmig_OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuplePart19: BinaryAssociation = BinaryAssociation(
    name="tuplePart19",
    ends={
        Property(name="TuplePart", type=OCLinEmig_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="tuple", type=OCLinEmig_TuplePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body32: BinaryAssociation = BinaryAssociation(
    name="body32",
    ends={
        Property(name="OclExpression33", type=OCLinEmig_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="loopExp", type=OCLinEmig_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterators34: BinaryAssociation = BinaryAssociation(
    name="iterators34",
    ends={
        Property(name="Iterator", type=OCLinEmig_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="loopExpr", type=OCLinEmig_Iterator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result35: BinaryAssociation = BinaryAssociation(
    name="result35",
    ends={
        Property(name="VariableDeclaration36", type=OCLinEmig_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="baseExp", type=OCLinEmig_VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable37: BinaryAssociation = BinaryAssociation(
    name="variable37",
    ends={
        Property(name="VariableDeclaration38", type=OCLinEmig_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="letExp", type=OCLinEmig_VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in_39: BinaryAssociation = BinaryAssociation(
    name="in_39",
    ends={
        Property(name="OclExpression41", type=OCLinEmig_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="letExp40", type=OCLinEmig_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression42: BinaryAssociation = BinaryAssociation(
    name="thenExpression42",
    ends={
        Property(name="OclExpression43", type=OCLinEmig_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp2", type=OCLinEmig_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition44: BinaryAssociation = BinaryAssociation(
    name="condition44",
    ends={
        Property(name="OclExpression45", type=OCLinEmig_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp1", type=OCLinEmig_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression46: BinaryAssociation = BinaryAssociation(
    name="elseExpression46",
    ends={
        Property(name="OclExpression47", type=OCLinEmig_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp3", type=OCLinEmig_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initExpression50: BinaryAssociation = BinaryAssociation(
    name="initExpression50",
    ends={
        Property(name="OclExpression51", type=OCLinEmig_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="initializedVariable", type=OCLinEmig_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
letExp52: BinaryAssociation = BinaryAssociation(
    name="letExp52",
    ends={
        Property(name="LetExp53", type=OCLinEmig_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=OCLinEmig_LetExp, multiplicity=Multiplicity(0, 1))
    }
)
baseExp54: BinaryAssociation = BinaryAssociation(
    name="baseExp54",
    ends={
        Property(name="IterateExp", type=OCLinEmig_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="result", type=OCLinEmig_IterateExp, multiplicity=Multiplicity(0, 1))
    }
)
variableExp55: BinaryAssociation = BinaryAssociation(
    name="variableExp55",
    ends={
        Property(name="VariableExp", type=OCLinEmig_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="referredVariable", type=OCLinEmig_VariableExp, multiplicity=Multiplicity(0, 9999))
    }
)
loopExpr56: BinaryAssociation = BinaryAssociation(
    name="loopExpr56",
    ends={
        Property(name="LoopExp57", type=OCLinEmig_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="iterators", type=OCLinEmig_LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
operation58: BinaryAssociation = BinaryAssociation(
    name="operation58",
    ends={
        Property(name="Operation59", type=OCLinEmig_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=OCLinEmig_Operation, multiplicity=Multiplicity(1, 1))
    }
)
elementType60: BinaryAssociation = BinaryAssociation(
    name="elementType60",
    ends={
        Property(name="OclType61", type=OCLinEmig_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="collectionTypes", type=OCLinEmig_OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definitions62: BinaryAssociation = BinaryAssociation(
    name="definitions62",
    ends={
        Property(name="OclContextDefinition", type=OCLinEmig_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="context_", type=OCLinEmig_OclContextDefinition, multiplicity=Multiplicity(0, 1))
    }
)
oclExpression63: BinaryAssociation = BinaryAssociation(
    name="oclExpression63",
    ends={
        Property(name="OclExpression64", type=OCLinEmig_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=OCLinEmig_OclExpression, multiplicity=Multiplicity(0, 1))
    }
)
operation65: BinaryAssociation = BinaryAssociation(
    name="operation65",
    ends={
        Property(name="Operation66", type=OCLinEmig_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="returnType", type=OCLinEmig_Operation, multiplicity=Multiplicity(0, 1))
    }
)
type48: BinaryAssociation = BinaryAssociation(
    name="type48",
    ends={
        Property(name="OclType49", type=OCLinEmig_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variableDeclaration", type=OCLinEmig_OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mapType71: BinaryAssociation = BinaryAssociation(
    name="mapType71",
    ends={
        Property(name="MapType72", type=OCLinEmig_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="keyType", type=OCLinEmig_MapType, multiplicity=Multiplicity(0, 1))
    }
)
collectionTypes73: BinaryAssociation = BinaryAssociation(
    name="collectionTypes73",
    ends={
        Property(name="CollectionType", type=OCLinEmig_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="elementType", type=OCLinEmig_CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
tupleTypeAttribute74: BinaryAssociation = BinaryAssociation(
    name="tupleTypeAttribute74",
    ends={
        Property(name="TupleTypeAttribute", type=OCLinEmig_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type75", type=OCLinEmig_TupleTypeAttribute, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclaration76: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration76",
    ends={
        Property(name="VariableDeclaration78", type=OCLinEmig_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type77", type=OCLinEmig_VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
attributes79: BinaryAssociation = BinaryAssociation(
    name="attributes79",
    ends={
        Property(name="TupleTypeAttribute80", type=OCLinEmig_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="tupleType", type=OCLinEmig_TupleTypeAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mapType267: BinaryAssociation = BinaryAssociation(
    name="mapType267",
    ends={
        Property(name="MapType", type=OCLinEmig_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="valueType", type=OCLinEmig_MapType, multiplicity=Multiplicity(0, 1))
    }
)
attribute68: BinaryAssociation = BinaryAssociation(
    name="attribute68",
    ends={
        Property(name="Attribute70", type=OCLinEmig_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type69", type=OCLinEmig_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
tupleType83: BinaryAssociation = BinaryAssociation(
    name="tupleType83",
    ends={
        Property(name="TupleType", type=OCLinEmig_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=OCLinEmig_TupleType, multiplicity=Multiplicity(1, 1))
    }
)
model84: BinaryAssociation = BinaryAssociation(
    name="model84",
    ends={
        Property(name="OclModel", type=OCLinEmig_OclModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements85", type=OCLinEmig_OclModel, multiplicity=Multiplicity(1, 1))
    }
)
valueType86: BinaryAssociation = BinaryAssociation(
    name="valueType86",
    ends={
        Property(name="OclType87", type=OCLinEmig_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="mapType2", type=OCLinEmig_OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
keyType88: BinaryAssociation = BinaryAssociation(
    name="keyType88",
    ends={
        Property(name="OclType89", type=OCLinEmig_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="mapType", type=OCLinEmig_OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
feature90: BinaryAssociation = BinaryAssociation(
    name="feature90",
    ends={
        Property(name="OclFeature", type=OCLinEmig_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definition", type=OCLinEmig_OclFeature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context_91: BinaryAssociation = BinaryAssociation(
    name="context_91",
    ends={
        Property(name="OclContextDefinition93", type=OCLinEmig_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definition92", type=OCLinEmig_OclContextDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition94: BinaryAssociation = BinaryAssociation(
    name="definition94",
    ends={
        Property(name="OclFeatureDefinition", type=OCLinEmig_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="context_95", type=OCLinEmig_OclFeatureDefinition, multiplicity=Multiplicity(1, 1))
    }
)
context_96: BinaryAssociation = BinaryAssociation(
    name="context_96",
    ends={
        Property(name="OclType97", type=OCLinEmig_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definitions", type=OCLinEmig_OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definition98: BinaryAssociation = BinaryAssociation(
    name="definition98",
    ends={
        Property(name="OclFeatureDefinition99", type=OCLinEmig_OclFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=OCLinEmig_OclFeatureDefinition, multiplicity=Multiplicity(0, 1))
    }
)
type81: BinaryAssociation = BinaryAssociation(
    name="type81",
    ends={
        Property(name="OclType82", type=OCLinEmig_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="tupleTypeAttribute", type=OCLinEmig_OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type102: BinaryAssociation = BinaryAssociation(
    name="type102",
    ends={
        Property(name="OclType103", type=OCLinEmig_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attribute", type=OCLinEmig_OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters104: BinaryAssociation = BinaryAssociation(
    name="parameters104",
    ends={
        Property(name="Parameter", type=OCLinEmig_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation", type=OCLinEmig_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType105: BinaryAssociation = BinaryAssociation(
    name="returnType105",
    ends={
        Property(name="OclType107", type=OCLinEmig_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation106", type=OCLinEmig_OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body108: BinaryAssociation = BinaryAssociation(
    name="body108",
    ends={
        Property(name="OclExpression109", type=OCLinEmig_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="owningOperation", type=OCLinEmig_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metamodel111: BinaryAssociation = BinaryAssociation(
    name="metamodel111",
    ends={
        Property(name="OclModel112", type=OCLinEmig_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=OCLinEmig_OclModel, multiplicity=Multiplicity(1, 1))
    }
)
elements113: BinaryAssociation = BinaryAssociation(
    name="elements113",
    ends={
        Property(name="OclModelElement", type=OCLinEmig_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model114", type=OCLinEmig_OclModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
model116: BinaryAssociation = BinaryAssociation(
    name="model116",
    ends={
        Property(name="OclModel117", type=OCLinEmig_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel", type=OCLinEmig_OclModel, multiplicity=Multiplicity(0, 9999))
    }
)
initExpression100: BinaryAssociation = BinaryAssociation(
    name="initExpression100",
    ends={
        Property(name="OclExpression101", type=OCLinEmig_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="owningAttribute", type=OCLinEmig_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
oclFeatures118: BinaryAssociation = BinaryAssociation(
    name="oclFeatures118",
    ends={
        Property(name="OCLinEmig_OclFeatureDefinition", type=OCLinEmig_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="OCLinEmig_Module", type=OCLinEmig_OclFeatureDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_OCLinEmig_OclExpression_LocatedElement = Generalization(general=LocatedElement, specific=OCLinEmig_OclExpression)
gen_OCLinEmig_VariableExp_OclExpression = Generalization(general=OclExpression, specific=OCLinEmig_VariableExp)
gen_OCLinEmig_PrimitiveExp_OclExpression = Generalization(general=OclExpression, specific=OCLinEmig_PrimitiveExp)
gen_OCLinEmig_StringExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=OCLinEmig_StringExp)
gen_OCLinEmig_BooleanExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=OCLinEmig_BooleanExp)
gen_OCLinEmig_NumericExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=OCLinEmig_NumericExp)
gen_OCLinEmig_RealExp_NumericExp = Generalization(general=NumericExp, specific=OCLinEmig_RealExp)
gen_OCLinEmig_IntegerExp_NumericExp = Generalization(general=NumericExp, specific=OCLinEmig_IntegerExp)
gen_OCLinEmig_CollectionExp_OclExpression = Generalization(general=OclExpression, specific=OCLinEmig_CollectionExp)
gen_OCLinEmig_BagExp_CollectionExp = Generalization(general=CollectionExp, specific=OCLinEmig_BagExp)
gen_OCLinEmig_OrderedSetExp_CollectionExp = Generalization(general=CollectionExp, specific=OCLinEmig_OrderedSetExp)
gen_OCLinEmig_SequenceExp_CollectionExp = Generalization(general=CollectionExp, specific=OCLinEmig_SequenceExp)
gen_OCLinEmig_SetExp_CollectionExp = Generalization(general=CollectionExp, specific=OCLinEmig_SetExp)
gen_OCLinEmig_TupleExp_OclExpression = Generalization(general=OclExpression, specific=OCLinEmig_TupleExp)
gen_OCLinEmig_SuperExp_OclExpression = Generalization(general=OclExpression, specific=OCLinEmig_SuperExp)
gen_OCLinEmig_MapExp_OclExpression = Generalization(general=OclExpression, specific=OCLinEmig_MapExp)
gen_OCLinEmig_MapElement_LocatedElement = Generalization(general=LocatedElement, specific=OCLinEmig_MapElement)
gen_OCLinEmig_EnumLiteralExp_OclExpression = Generalization(general=OclExpression, specific=OCLinEmig_EnumLiteralExp)
gen_OCLinEmig_OclUndefinedExp_OclExpression = Generalization(general=OclExpression, specific=OCLinEmig_OclUndefinedExp)
gen_OCLinEmig_PropertyCallExp_OclExpression = Generalization(general=OclExpression, specific=OCLinEmig_PropertyCallExp)
gen_OCLinEmig_NavigationOrAttributeCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=OCLinEmig_NavigationOrAttributeCallExp)
gen_OCLinEmig_OperationCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=OCLinEmig_OperationCallExp)
gen_OCLinEmig_TuplePart_VariableDeclaration = Generalization(general=VariableDeclaration, specific=OCLinEmig_TuplePart)
gen_OCLinEmig_IterateExp_LoopExp = Generalization(general=LoopExp, specific=OCLinEmig_IterateExp)
gen_OCLinEmig_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=OCLinEmig_IteratorExp)
gen_OCLinEmig_LetExp_OclExpression = Generalization(general=OclExpression, specific=OCLinEmig_LetExp)
gen_OCLinEmig_IfExp_OclExpression = Generalization(general=OclExpression, specific=OCLinEmig_IfExp)
gen_OCLinEmig_VariableDeclaration_LocatedElement = Generalization(general=LocatedElement, specific=OCLinEmig_VariableDeclaration)
gen_OCLinEmig_OperatorCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=OCLinEmig_OperatorCallExp)
gen_OCLinEmig_CollectionOperationCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=OCLinEmig_CollectionOperationCallExp)
gen_OCLinEmig_LoopExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=OCLinEmig_LoopExp)
gen_OCLinEmig_Iterator_VariableDeclaration = Generalization(general=VariableDeclaration, specific=OCLinEmig_Iterator)
gen_OCLinEmig_Parameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=OCLinEmig_Parameter)
gen_OCLinEmig_CollectionType_OclType = Generalization(general=OclType, specific=OCLinEmig_CollectionType)
gen_OCLinEmig_OclType_OclExpression = Generalization(general=OclExpression, specific=OCLinEmig_OclType)
gen_OCLinEmig_Primitive_OclType = Generalization(general=OclType, specific=OCLinEmig_Primitive)
gen_OCLinEmig_StringType_Primitive = Generalization(general=Primitive, specific=OCLinEmig_StringType)
gen_OCLinEmig_BooleanType_Primitive = Generalization(general=Primitive, specific=OCLinEmig_BooleanType)
gen_OCLinEmig_NumericType_Primitive = Generalization(general=Primitive, specific=OCLinEmig_NumericType)
gen_OCLinEmig_IntegerType_NumericType = Generalization(general=NumericType, specific=OCLinEmig_IntegerType)
gen_OCLinEmig_RealType_NumericType = Generalization(general=NumericType, specific=OCLinEmig_RealType)
gen_OCLinEmig_BagType_CollectionType = Generalization(general=CollectionType, specific=OCLinEmig_BagType)
gen_OCLinEmig_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=OCLinEmig_OrderedSetType)
gen_OCLinEmig_SequenceType_CollectionType = Generalization(general=CollectionType, specific=OCLinEmig_SequenceType)
gen_OCLinEmig_SetType_CollectionType = Generalization(general=CollectionType, specific=OCLinEmig_SetType)
gen_OCLinEmig_OclAnyType_OclType = Generalization(general=OclType, specific=OCLinEmig_OclAnyType)
gen_OCLinEmig_TupleType_OclType = Generalization(general=OclType, specific=OCLinEmig_TupleType)
gen_OCLinEmig_TupleTypeAttribute_LocatedElement = Generalization(general=LocatedElement, specific=OCLinEmig_TupleTypeAttribute)
gen_OCLinEmig_OclModelElement_OclType = Generalization(general=OclType, specific=OCLinEmig_OclModelElement)
gen_OCLinEmig_MapType_OclType = Generalization(general=OclType, specific=OCLinEmig_MapType)
gen_OCLinEmig_OclFeatureDefinition_LocatedElement = Generalization(general=LocatedElement, specific=OCLinEmig_OclFeatureDefinition)
gen_OCLinEmig_OclContextDefinition_LocatedElement = Generalization(general=LocatedElement, specific=OCLinEmig_OclContextDefinition)
gen_OCLinEmig_OclFeature_LocatedElement = Generalization(general=LocatedElement, specific=OCLinEmig_OclFeature)
gen_OCLinEmig_Operation_OclFeature = Generalization(general=OclFeature, specific=OCLinEmig_Operation)
gen_OCLinEmig_OclModel_LocatedElement = Generalization(general=LocatedElement, specific=OCLinEmig_OclModel)
gen_OCLinEmig_Attribute_OclFeature = Generalization(general=OclFeature, specific=OCLinEmig_Attribute)

# Domain Model
domain_model = DomainModel(
    name="OCLinEmig",
    types={OCLinEmig_OclExpression, LocatedElement, OCLinEmig_OclType, OCLinEmig_IfExp, OCLinEmig_PropertyCallExp, OCLinEmig_CollectionExp, OCLinEmig_LoopExp, OCLinEmig_OperationCallExp, OCLinEmig_VariableDeclaration, OCLinEmig_Operation, OCLinEmig_Attribute, OCLinEmig_VariableExp, OclExpression, OCLinEmig_StringExp, PrimitiveExp, OCLinEmig_LetExp, OCLinEmig_BooleanExp, OCLinEmig_NumericExp, OCLinEmig_RealExp, NumericExp, OCLinEmig_IntegerExp, OCLinEmig_BagExp, CollectionExp, OCLinEmig_OrderedSetExp, OCLinEmig_SequenceExp, OCLinEmig_SetExp, OCLinEmig_TupleExp, OCLinEmig_SuperExp, OCLinEmig_PrimitiveExp, OCLinEmig_MapExp, OCLinEmig_MapElement, OCLinEmig_EnumLiteralExp, OCLinEmig_OclUndefinedExp, OCLinEmig_NavigationOrAttributeCallExp, PropertyCallExp, OCLinEmig_TuplePart, VariableDeclaration, OCLinEmig_Iterator, OCLinEmig_IterateExp, LoopExp, OCLinEmig_IteratorExp, OCLinEmig_OperatorCallExp, OperationCallExp, OCLinEmig_CollectionOperationCallExp, OCLinEmig_Parameter, OCLinEmig_CollectionType, OclType, OCLinEmig_OclContextDefinition, OCLinEmig_TupleTypeAttribute, OCLinEmig_Primitive, OCLinEmig_StringType, Primitive, OCLinEmig_BooleanType, OCLinEmig_NumericType, OCLinEmig_IntegerType, NumericType, OCLinEmig_RealType, OCLinEmig_BagType, CollectionType, OCLinEmig_OrderedSetType, OCLinEmig_SequenceType, OCLinEmig_SetType, OCLinEmig_OclAnyType, OCLinEmig_TupleType, OCLinEmig_MapType, OCLinEmig_OclModelElement, OCLinEmig_OclModel, OCLinEmig_OclFeatureDefinition, OCLinEmig_OclFeature, OCLinEmig_LocatedElement, OCLinEmig_Module, OclFeature},
    associations={type0, ifExp31, appliedProperty2, collection3, loopExp5, parentOperation6, initializedVariable7, ifExp28, owningOperation10, ifExp112, owningAttribute14, letExp4, elements18, referredVariable16, tuple20, elements21, map22, key24, value25, source28, arguments30, tuplePart19, body32, iterators34, result35, variable37, in_39, thenExpression42, condition44, elseExpression46, initExpression50, letExp52, baseExp54, variableExp55, loopExpr56, operation58, elementType60, definitions62, oclExpression63, operation65, type48, mapType71, collectionTypes73, tupleTypeAttribute74, variableDeclaration76, attributes79, mapType267, attribute68, tupleType83, model84, valueType86, keyType88, feature90, context_91, definition94, context_96, definition98, type81, type102, parameters104, returnType105, body108, metamodel111, elements113, model116, initExpression100, oclFeatures118},
    generalizations={gen_OCLinEmig_OclExpression_LocatedElement, gen_OCLinEmig_VariableExp_OclExpression, gen_OCLinEmig_PrimitiveExp_OclExpression, gen_OCLinEmig_StringExp_PrimitiveExp, gen_OCLinEmig_BooleanExp_PrimitiveExp, gen_OCLinEmig_NumericExp_PrimitiveExp, gen_OCLinEmig_RealExp_NumericExp, gen_OCLinEmig_IntegerExp_NumericExp, gen_OCLinEmig_CollectionExp_OclExpression, gen_OCLinEmig_BagExp_CollectionExp, gen_OCLinEmig_OrderedSetExp_CollectionExp, gen_OCLinEmig_SequenceExp_CollectionExp, gen_OCLinEmig_SetExp_CollectionExp, gen_OCLinEmig_TupleExp_OclExpression, gen_OCLinEmig_SuperExp_OclExpression, gen_OCLinEmig_MapExp_OclExpression, gen_OCLinEmig_MapElement_LocatedElement, gen_OCLinEmig_EnumLiteralExp_OclExpression, gen_OCLinEmig_OclUndefinedExp_OclExpression, gen_OCLinEmig_PropertyCallExp_OclExpression, gen_OCLinEmig_NavigationOrAttributeCallExp_PropertyCallExp, gen_OCLinEmig_OperationCallExp_PropertyCallExp, gen_OCLinEmig_TuplePart_VariableDeclaration, gen_OCLinEmig_IterateExp_LoopExp, gen_OCLinEmig_IteratorExp_LoopExp, gen_OCLinEmig_LetExp_OclExpression, gen_OCLinEmig_IfExp_OclExpression, gen_OCLinEmig_VariableDeclaration_LocatedElement, gen_OCLinEmig_OperatorCallExp_OperationCallExp, gen_OCLinEmig_CollectionOperationCallExp_OperationCallExp, gen_OCLinEmig_LoopExp_PropertyCallExp, gen_OCLinEmig_Iterator_VariableDeclaration, gen_OCLinEmig_Parameter_VariableDeclaration, gen_OCLinEmig_CollectionType_OclType, gen_OCLinEmig_OclType_OclExpression, gen_OCLinEmig_Primitive_OclType, gen_OCLinEmig_StringType_Primitive, gen_OCLinEmig_BooleanType_Primitive, gen_OCLinEmig_NumericType_Primitive, gen_OCLinEmig_IntegerType_NumericType, gen_OCLinEmig_RealType_NumericType, gen_OCLinEmig_BagType_CollectionType, gen_OCLinEmig_OrderedSetType_CollectionType, gen_OCLinEmig_SequenceType_CollectionType, gen_OCLinEmig_SetType_CollectionType, gen_OCLinEmig_OclAnyType_OclType, gen_OCLinEmig_TupleType_OclType, gen_OCLinEmig_TupleTypeAttribute_LocatedElement, gen_OCLinEmig_OclModelElement_OclType, gen_OCLinEmig_MapType_OclType, gen_OCLinEmig_OclFeatureDefinition_LocatedElement, gen_OCLinEmig_OclContextDefinition_LocatedElement, gen_OCLinEmig_OclFeature_LocatedElement, gen_OCLinEmig_Operation_OclFeature, gen_OCLinEmig_OclModel_LocatedElement, gen_OCLinEmig_Attribute_OclFeature},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)