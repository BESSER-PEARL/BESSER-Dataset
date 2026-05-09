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
UMLClass = Class(name="UMLClass")
ocl_constraints_OclConstraintsModel = Class(name="ocl_constraints_OclConstraintsModel")
LocatedElement = Class(name="LocatedElement")
Context = Class(name="Context")
VariableDeclaration = Class(name="VariableDeclaration")
ocl_constraints_Metaclass = Class(name="ocl_constraints_Metaclass", is_abstract=True)
ocl_constraints_UMLClass = Class(name="ocl_constraints_UMLClass")
Metaclass = Class(name="Metaclass")
ocl_constraints_Context = Class(name="ocl_constraints_Context")
OclConstraintsModel = Class(name="OclConstraintsModel")
OclInvariant = Class(name="OclInvariant")
OclPrecondition = Class(name="OclPrecondition")
ocl_constraints_OclInvariant = Class(name="ocl_constraints_OclInvariant")
OclExpression = Class(name="OclExpression")
ocl_constraints_OclPrecondition = Class(name="ocl_constraints_OclPrecondition")
ocl_constraints_LocatedElement = Class(name="ocl_constraints_LocatedElement", is_abstract=True)
OCL_OclExpression = Class(name="OCL_OclExpression", is_abstract=True)
OclType = Class(name="OclType")
IfExp = Class(name="IfExp")
PropertyCallExp = Class(name="PropertyCallExp")
CollectionExp = Class(name="CollectionExp")
LetExp = Class(name="LetExp")
LoopExp = Class(name="LoopExp")
OperationCallExp = Class(name="OperationCallExp")
Operation = Class(name="Operation")
Attribute = Class(name="Attribute")
OCL_VariableExp = Class(name="OCL_VariableExp")
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
TuplePart = Class(name="TuplePart")
OCL_TuplePart = Class(name="OCL_TuplePart")
TupleExp = Class(name="TupleExp")
OCL_MapExp = Class(name="OCL_MapExp")
MapElement = Class(name="MapElement")
OCL_MapElement = Class(name="OCL_MapElement")
MapExp = Class(name="MapExp")
OCL_EnumLiteralExp = Class(name="OCL_EnumLiteralExp")
OCL_OclUndefinedExp = Class(name="OCL_OclUndefinedExp")
OCL_PropertyCallExp = Class(name="OCL_PropertyCallExp", is_abstract=True)
OCL_NavigationOrAttributeCallExp = Class(name="OCL_NavigationOrAttributeCallExp")
OCL_OperationCallExp = Class(name="OCL_OperationCallExp")
OCL_OperatorCallExp = Class(name="OCL_OperatorCallExp")
OCL_CollectionOperationCallExp = Class(name="OCL_CollectionOperationCallExp")
OCL_LoopExp = Class(name="OCL_LoopExp", is_abstract=True)
Iterator = Class(name="Iterator")
OCL_IterateExp = Class(name="OCL_IterateExp")
OCL_IteratorExp = Class(name="OCL_IteratorExp")
OCL_LetExp = Class(name="OCL_LetExp")
OCL_IfExp = Class(name="OCL_IfExp")
OCL_VariableDeclaration = Class(name="OCL_VariableDeclaration")
OCL_CollectionType = Class(name="OCL_CollectionType")
IterateExp = Class(name="IterateExp")
VariableExp = Class(name="VariableExp")
OCL_Iterator = Class(name="OCL_Iterator")
OCL_Parameter = Class(name="OCL_Parameter")
OCL_TupleType = Class(name="OCL_TupleType")
OCL_OclType = Class(name="OCL_OclType")
OclContextDefinition = Class(name="OclContextDefinition")
MapType = Class(name="MapType")
CollectionType = Class(name="CollectionType")
TupleTypeAttribute = Class(name="TupleTypeAttribute")
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
OCL_SetType = Class(name="OCL_SetType")
OCL_OclAnyType = Class(name="OCL_OclAnyType")
OCL_TupleTypeAttribute = Class(name="OCL_TupleTypeAttribute")
TupleType = Class(name="TupleType")
OCL_OclModelElement = Class(name="OCL_OclModelElement")
OclModel = Class(name="OclModel")
OCL_MapType = Class(name="OCL_MapType")
OCL_OclFeatureDefinition = Class(name="OCL_OclFeatureDefinition")
OclFeature = Class(name="OclFeature")
OCL_OclContextDefinition = Class(name="OCL_OclContextDefinition")
OclFeatureDefinition = Class(name="OclFeatureDefinition")
OCL_OclFeature = Class(name="OCL_OclFeature", is_abstract=True)
OCL_Attribute = Class(name="OCL_Attribute")
OCL_Operation = Class(name="OCL_Operation")
Parameter_ = Class(name="Parameter")
OCL_OclModel = Class(name="OCL_OclModel")
OclModelElement = Class(name="OclModelElement")

# UMLClass class attributes and methods

# ocl_constraints_OclConstraintsModel class attributes and methods
ocl_constraints_OclConstraintsModel_metamodel: Property = Property(name="metamodel", type=StringType)
ocl_constraints_OclConstraintsModel_name: Property = Property(name="name", type=StringType)
ocl_constraints_OclConstraintsModel.attributes={ocl_constraints_OclConstraintsModel_name, ocl_constraints_OclConstraintsModel_metamodel}

# LocatedElement class attributes and methods

# Context class attributes and methods

# VariableDeclaration class attributes and methods

# ocl_constraints_Metaclass class attributes and methods
ocl_constraints_Metaclass_name: Property = Property(name="name", type=StringType)
ocl_constraints_Metaclass.attributes={ocl_constraints_Metaclass_name}

# ocl_constraints_UMLClass class attributes and methods

# Metaclass class attributes and methods

# ocl_constraints_Context class attributes and methods

# OclConstraintsModel class attributes and methods

# OclInvariant class attributes and methods

# OclPrecondition class attributes and methods

# ocl_constraints_OclInvariant class attributes and methods
ocl_constraints_OclInvariant_name: Property = Property(name="name", type=StringType)
ocl_constraints_OclInvariant_description: Property = Property(name="description", type=StringType)
ocl_constraints_OclInvariant.attributes={ocl_constraints_OclInvariant_description, ocl_constraints_OclInvariant_name}

# OclExpression class attributes and methods

# ocl_constraints_OclPrecondition class attributes and methods
ocl_constraints_OclPrecondition_name: Property = Property(name="name", type=StringType)
ocl_constraints_OclPrecondition_description: Property = Property(name="description", type=StringType)
ocl_constraints_OclPrecondition.attributes={ocl_constraints_OclPrecondition_description, ocl_constraints_OclPrecondition_name}

# ocl_constraints_LocatedElement class attributes and methods
ocl_constraints_LocatedElement_location: Property = Property(name="location", type=StringType)
ocl_constraints_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
ocl_constraints_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
ocl_constraints_LocatedElement.attributes={ocl_constraints_LocatedElement_location, ocl_constraints_LocatedElement_commentsBefore, ocl_constraints_LocatedElement_commentsAfter}

# OCL_OclExpression class attributes and methods

# OclType class attributes and methods

# IfExp class attributes and methods

# PropertyCallExp class attributes and methods

# CollectionExp class attributes and methods

# LetExp class attributes and methods

# LoopExp class attributes and methods

# OperationCallExp class attributes and methods

# Operation class attributes and methods

# Attribute class attributes and methods

# OCL_VariableExp class attributes and methods

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

# OCL_VariableDeclaration class attributes and methods
OCL_VariableDeclaration_id: Property = Property(name="id", type=StringType)
OCL_VariableDeclaration_varName: Property = Property(name="varName", type=StringType)
OCL_VariableDeclaration.attributes={OCL_VariableDeclaration_id, OCL_VariableDeclaration_varName}

# OCL_CollectionType class attributes and methods

# IterateExp class attributes and methods

# VariableExp class attributes and methods

# OCL_Iterator class attributes and methods

# OCL_Parameter class attributes and methods

# OCL_TupleType class attributes and methods

# OCL_OclType class attributes and methods
OCL_OclType_name: Property = Property(name="name", type=StringType)
OCL_OclType.attributes={OCL_OclType_name}

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

# OCL_SequenceType class attributes and methods

# OCL_SetType class attributes and methods

# OCL_OclAnyType class attributes and methods

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
contexts0: BinaryAssociation = BinaryAssociation(
    name="contexts0",
    ends={
        Property(name="Context", type=ocl_constraints_OclConstraintsModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model_", type=Context, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables1: BinaryAssociation = BinaryAssociation(
    name="variables1",
    ends={
        Property(name="VariableDeclaration", type=ocl_constraints_OclConstraintsModel, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_constraints_OclConstraintsModel", type=VariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model_2: BinaryAssociation = BinaryAssociation(
    name="model_2",
    ends={
        Property(name="OclConstraintsModel", type=ocl_constraints_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="contexts", type=OclConstraintsModel, multiplicity=Multiplicity(0, 1))
    }
)
collection14: BinaryAssociation = BinaryAssociation(
    name="collection14",
    ends={
        Property(name="elements", type=CollectionExp, multiplicity=Multiplicity(0, 1)),
        Property(name="CollectionExp", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1))
    }
)
metaclass_3: BinaryAssociation = BinaryAssociation(
    name="metaclass_3",
    ends={
        Property(name="UMLClass", type=ocl_constraints_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_constraints_Context", type=UMLClass, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
invariant4: BinaryAssociation = BinaryAssociation(
    name="invariant4",
    ends={
        Property(name="OclInvariant", type=ocl_constraints_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_constraints_Context5", type=OclInvariant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
precondition6: BinaryAssociation = BinaryAssociation(
    name="precondition6",
    ends={
        Property(name="OclPrecondition", type=ocl_constraints_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_constraints_Context7", type=OclPrecondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr8: BinaryAssociation = BinaryAssociation(
    name="expr8",
    ends={
        Property(name="OclExpression", type=ocl_constraints_OclInvariant, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_constraints_OclInvariant", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr9: BinaryAssociation = BinaryAssociation(
    name="expr9",
    ends={
        Property(name="OclExpression10", type=ocl_constraints_OclPrecondition, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_constraints_OclPrecondition", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type11: BinaryAssociation = BinaryAssociation(
    name="type11",
    ends={
        Property(name="OclType", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="oclExpression", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifExp312: BinaryAssociation = BinaryAssociation(
    name="ifExp312",
    ends={
        Property(name="IfExp", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="elseExpression", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
appliedProperty13: BinaryAssociation = BinaryAssociation(
    name="appliedProperty13",
    ends={
        Property(name="PropertyCallExp", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=PropertyCallExp, multiplicity=Multiplicity(0, 1))
    }
)
elements30: BinaryAssociation = BinaryAssociation(
    name="elements30",
    ends={
        Property(name="OclExpression31", type=OCL_CollectionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="collection", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
letExp15: BinaryAssociation = BinaryAssociation(
    name="letExp15",
    ends={
        Property(name="LetExp", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="in_", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
loopExp16: BinaryAssociation = BinaryAssociation(
    name="loopExp16",
    ends={
        Property(name="LoopExp", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="body", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
parentOperation17: BinaryAssociation = BinaryAssociation(
    name="parentOperation17",
    ends={
        Property(name="OperationCallExp", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="arguments", type=OperationCallExp, multiplicity=Multiplicity(0, 1))
    }
)
initializedVariable18: BinaryAssociation = BinaryAssociation(
    name="initializedVariable18",
    ends={
        Property(name="VariableDeclaration19", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="initExpression", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
ifExp220: BinaryAssociation = BinaryAssociation(
    name="ifExp220",
    ends={
        Property(name="IfExp21", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thenExpression", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningOperation22: BinaryAssociation = BinaryAssociation(
    name="owningOperation22",
    ends={
        Property(name="Operation", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="body23", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
ifExp124: BinaryAssociation = BinaryAssociation(
    name="ifExp124",
    ends={
        Property(name="IfExp25", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="condition", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningAttribute26: BinaryAssociation = BinaryAssociation(
    name="owningAttribute26",
    ends={
        Property(name="Attribute", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="initExpression27", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable28: BinaryAssociation = BinaryAssociation(
    name="referredVariable28",
    ends={
        Property(name="VariableDeclaration29", type=OCL_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="variableExp", type=VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
tuplePart32: BinaryAssociation = BinaryAssociation(
    name="tuplePart32",
    ends={
        Property(name="TuplePart", type=OCL_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="tuple", type=TuplePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuple33: BinaryAssociation = BinaryAssociation(
    name="tuple33",
    ends={
        Property(name="TupleExp", type=OCL_TuplePart, multiplicity=Multiplicity(1, 1)),
        Property(name="tuplePart", type=TupleExp, multiplicity=Multiplicity(1, 1))
    }
)
elements34: BinaryAssociation = BinaryAssociation(
    name="elements34",
    ends={
        Property(name="MapElement", type=OCL_MapExp, multiplicity=Multiplicity(1, 1)),
        Property(name="map", type=MapElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
map35: BinaryAssociation = BinaryAssociation(
    name="map35",
    ends={
        Property(name="MapExp", type=OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements36", type=MapExp, multiplicity=Multiplicity(1, 1))
    }
)
key37: BinaryAssociation = BinaryAssociation(
    name="key37",
    ends={
        Property(name="OclExpression38", type=OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_MapElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value39: BinaryAssociation = BinaryAssociation(
    name="value39",
    ends={
        Property(name="OclExpression41", type=OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_MapElement40", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source42: BinaryAssociation = BinaryAssociation(
    name="source42",
    ends={
        Property(name="OclExpression43", type=OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="appliedProperty", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments44: BinaryAssociation = BinaryAssociation(
    name="arguments44",
    ends={
        Property(name="OclExpression45", type=OCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="parentOperation", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body46: BinaryAssociation = BinaryAssociation(
    name="body46",
    ends={
        Property(name="OclExpression47", type=OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="loopExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterators48: BinaryAssociation = BinaryAssociation(
    name="iterators48",
    ends={
        Property(name="Iterator", type=OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="loopExpr", type=Iterator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result49: BinaryAssociation = BinaryAssociation(
    name="result49",
    ends={
        Property(name="VariableDeclaration50", type=OCL_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="baseExp", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable51: BinaryAssociation = BinaryAssociation(
    name="variable51",
    ends={
        Property(name="VariableDeclaration52", type=OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="letExp", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in_53: BinaryAssociation = BinaryAssociation(
    name="in_53",
    ends={
        Property(name="OclExpression55", type=OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="letExp54", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression56: BinaryAssociation = BinaryAssociation(
    name="thenExpression56",
    ends={
        Property(name="OclExpression57", type=OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp2", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition58: BinaryAssociation = BinaryAssociation(
    name="condition58",
    ends={
        Property(name="OclExpression59", type=OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp1", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression60: BinaryAssociation = BinaryAssociation(
    name="elseExpression60",
    ends={
        Property(name="OclExpression61", type=OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp3", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type62: BinaryAssociation = BinaryAssociation(
    name="type62",
    ends={
        Property(name="OclType63", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variableDeclaration", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression64: BinaryAssociation = BinaryAssociation(
    name="initExpression64",
    ends={
        Property(name="OclExpression65", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="initializedVariable", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
letExp66: BinaryAssociation = BinaryAssociation(
    name="letExp66",
    ends={
        Property(name="LetExp67", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
baseExp68: BinaryAssociation = BinaryAssociation(
    name="baseExp68",
    ends={
        Property(name="IterateExp", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="result", type=IterateExp, multiplicity=Multiplicity(0, 1))
    }
)
variableExp69: BinaryAssociation = BinaryAssociation(
    name="variableExp69",
    ends={
        Property(name="VariableExp", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="referredVariable", type=VariableExp, multiplicity=Multiplicity(0, 9999))
    }
)
loopExpr70: BinaryAssociation = BinaryAssociation(
    name="loopExpr70",
    ends={
        Property(name="LoopExp71", type=OCL_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="iterators", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
operation72: BinaryAssociation = BinaryAssociation(
    name="operation72",
    ends={
        Property(name="Operation73", type=OCL_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
elementType74: BinaryAssociation = BinaryAssociation(
    name="elementType74",
    ends={
        Property(name="OclType75", type=OCL_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="collectionTypes", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definitions76: BinaryAssociation = BinaryAssociation(
    name="definitions76",
    ends={
        Property(name="OclContextDefinition", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="context_", type=OclContextDefinition, multiplicity=Multiplicity(0, 1))
    }
)
oclExpression77: BinaryAssociation = BinaryAssociation(
    name="oclExpression77",
    ends={
        Property(name="OclExpression78", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=OclExpression, multiplicity=Multiplicity(0, 1))
    }
)
operation79: BinaryAssociation = BinaryAssociation(
    name="operation79",
    ends={
        Property(name="Operation80", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="returnType", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
mapType281: BinaryAssociation = BinaryAssociation(
    name="mapType281",
    ends={
        Property(name="MapType", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="valueType", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
attribute82: BinaryAssociation = BinaryAssociation(
    name="attribute82",
    ends={
        Property(name="Attribute84", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type83", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
mapType85: BinaryAssociation = BinaryAssociation(
    name="mapType85",
    ends={
        Property(name="MapType86", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="keyType", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
collectionTypes87: BinaryAssociation = BinaryAssociation(
    name="collectionTypes87",
    ends={
        Property(name="CollectionType", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="elementType", type=CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
tupleTypeAttribute88: BinaryAssociation = BinaryAssociation(
    name="tupleTypeAttribute88",
    ends={
        Property(name="TupleTypeAttribute", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type89", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclaration90: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration90",
    ends={
        Property(name="VariableDeclaration92", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type91", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
attributes93: BinaryAssociation = BinaryAssociation(
    name="attributes93",
    ends={
        Property(name="TupleTypeAttribute94", type=OCL_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="tupleType", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type95: BinaryAssociation = BinaryAssociation(
    name="type95",
    ends={
        Property(name="OclType96", type=OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="tupleTypeAttribute", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tupleType97: BinaryAssociation = BinaryAssociation(
    name="tupleType97",
    ends={
        Property(name="TupleType", type=OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=TupleType, multiplicity=Multiplicity(1, 1))
    }
)
model98: BinaryAssociation = BinaryAssociation(
    name="model98",
    ends={
        Property(name="OclModel", type=OCL_OclModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements99", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
valueType100: BinaryAssociation = BinaryAssociation(
    name="valueType100",
    ends={
        Property(name="OclType101", type=OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="mapType2", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
keyType102: BinaryAssociation = BinaryAssociation(
    name="keyType102",
    ends={
        Property(name="OclType103", type=OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="mapType", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
feature104: BinaryAssociation = BinaryAssociation(
    name="feature104",
    ends={
        Property(name="OclFeature", type=OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definition", type=OclFeature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context_105: BinaryAssociation = BinaryAssociation(
    name="context_105",
    ends={
        Property(name="OclContextDefinition107", type=OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definition106", type=OclContextDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition108: BinaryAssociation = BinaryAssociation(
    name="definition108",
    ends={
        Property(name="OclFeatureDefinition", type=OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="context_109", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1))
    }
)
context_110: BinaryAssociation = BinaryAssociation(
    name="context_110",
    ends={
        Property(name="OclType111", type=OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definitions", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definition112: BinaryAssociation = BinaryAssociation(
    name="definition112",
    ends={
        Property(name="OclFeatureDefinition113", type=OCL_OclFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=OclFeatureDefinition, multiplicity=Multiplicity(0, 1))
    }
)
initExpression114: BinaryAssociation = BinaryAssociation(
    name="initExpression114",
    ends={
        Property(name="OclExpression115", type=OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="owningAttribute", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type116: BinaryAssociation = BinaryAssociation(
    name="type116",
    ends={
        Property(name="OclType117", type=OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attribute", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters118: BinaryAssociation = BinaryAssociation(
    name="parameters118",
    ends={
        Property(name="Parameter", type=OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType119: BinaryAssociation = BinaryAssociation(
    name="returnType119",
    ends={
        Property(name="OclType121", type=OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation120", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body122: BinaryAssociation = BinaryAssociation(
    name="body122",
    ends={
        Property(name="OclExpression123", type=OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="owningOperation", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metamodel124: BinaryAssociation = BinaryAssociation(
    name="metamodel124",
    ends={
        Property(name="OclModel125", type=OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
elements126: BinaryAssociation = BinaryAssociation(
    name="elements126",
    ends={
        Property(name="OclModelElement", type=OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model127", type=OclModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
model128: BinaryAssociation = BinaryAssociation(
    name="model128",
    ends={
        Property(name="OclModel129", type=OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_ocl_constraints_OclConstraintsModel_LocatedElement = Generalization(general=LocatedElement, specific=ocl_constraints_OclConstraintsModel)
gen_ocl_constraints_Metaclass_LocatedElement = Generalization(general=LocatedElement, specific=ocl_constraints_Metaclass)
gen_ocl_constraints_UMLClass_Metaclass = Generalization(general=Metaclass, specific=ocl_constraints_UMLClass)
gen_ocl_constraints_Context_LocatedElement = Generalization(general=LocatedElement, specific=ocl_constraints_Context)
gen_ocl_constraints_OclInvariant_LocatedElement = Generalization(general=LocatedElement, specific=ocl_constraints_OclInvariant)
gen_ocl_constraints_OclPrecondition_LocatedElement = Generalization(general=LocatedElement, specific=ocl_constraints_OclPrecondition)
gen_OCL_OclExpression_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclExpression)
gen_OCL_VariableExp_OclExpression = Generalization(general=OclExpression, specific=OCL_VariableExp)
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
gen_OCL_CollectionType_OclType = Generalization(general=OclType, specific=OCL_CollectionType)
gen_OCL_Iterator_VariableDeclaration = Generalization(general=VariableDeclaration, specific=OCL_Iterator)
gen_OCL_Parameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=OCL_Parameter)
gen_OCL_TupleType_OclType = Generalization(general=OclType, specific=OCL_TupleType)
gen_OCL_OclType_OclExpression = Generalization(general=OclExpression, specific=OCL_OclType)
gen_OCL_Primitive_OclType = Generalization(general=OclType, specific=OCL_Primitive)
gen_OCL_StringType_Primitive = Generalization(general=Primitive, specific=OCL_StringType)
gen_OCL_BooleanType_Primitive = Generalization(general=Primitive, specific=OCL_BooleanType)
gen_OCL_NumericType_Primitive = Generalization(general=Primitive, specific=OCL_NumericType)
gen_OCL_IntegerType_NumericType = Generalization(general=NumericType, specific=OCL_IntegerType)
gen_OCL_RealType_NumericType = Generalization(general=NumericType, specific=OCL_RealType)
gen_OCL_BagType_CollectionType = Generalization(general=CollectionType, specific=OCL_BagType)
gen_OCL_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=OCL_OrderedSetType)
gen_OCL_SequenceType_CollectionType = Generalization(general=CollectionType, specific=OCL_SequenceType)
gen_OCL_SetType_CollectionType = Generalization(general=CollectionType, specific=OCL_SetType)
gen_OCL_OclAnyType_OclType = Generalization(general=OclType, specific=OCL_OclAnyType)
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
    types={UMLClass, ocl_constraints_OclConstraintsModel, LocatedElement, Context, VariableDeclaration, ocl_constraints_Metaclass, ocl_constraints_UMLClass, Metaclass, ocl_constraints_Context, OclConstraintsModel, OclInvariant, OclPrecondition, ocl_constraints_OclInvariant, OclExpression, ocl_constraints_OclPrecondition, ocl_constraints_LocatedElement, OCL_OclExpression, OclType, IfExp, PropertyCallExp, CollectionExp, LetExp, LoopExp, OperationCallExp, Operation, Attribute, OCL_VariableExp, OCL_SuperExp, OCL_PrimitiveExp, OCL_StringExp, PrimitiveExp, OCL_BooleanExp, OCL_NumericExp, OCL_RealExp, NumericExp, OCL_IntegerExp, OCL_CollectionExp, OCL_BagExp, OCL_OrderedSetExp, OCL_SequenceExp, OCL_SetExp, OCL_TupleExp, TuplePart, OCL_TuplePart, TupleExp, OCL_MapExp, MapElement, OCL_MapElement, MapExp, OCL_EnumLiteralExp, OCL_OclUndefinedExp, OCL_PropertyCallExp, OCL_NavigationOrAttributeCallExp, OCL_OperationCallExp, OCL_OperatorCallExp, OCL_CollectionOperationCallExp, OCL_LoopExp, Iterator, OCL_IterateExp, OCL_IteratorExp, OCL_LetExp, OCL_IfExp, OCL_VariableDeclaration, OCL_CollectionType, IterateExp, VariableExp, OCL_Iterator, OCL_Parameter, OCL_TupleType, OCL_OclType, OclContextDefinition, MapType, CollectionType, TupleTypeAttribute, OCL_Primitive, OCL_StringType, Primitive, OCL_BooleanType, OCL_NumericType, OCL_IntegerType, NumericType, OCL_RealType, OCL_BagType, OCL_OrderedSetType, OCL_SequenceType, OCL_SetType, OCL_OclAnyType, OCL_TupleTypeAttribute, TupleType, OCL_OclModelElement, OclModel, OCL_MapType, OCL_OclFeatureDefinition, OclFeature, OCL_OclContextDefinition, OclFeatureDefinition, OCL_OclFeature, OCL_Attribute, OCL_Operation, Parameter_, OCL_OclModel, OclModelElement},
    associations={contexts0, variables1, model_2, collection14, metaclass_3, invariant4, precondition6, expr8, expr9, type11, ifExp312, appliedProperty13, elements30, letExp15, loopExp16, parentOperation17, initializedVariable18, ifExp220, owningOperation22, ifExp124, owningAttribute26, referredVariable28, tuplePart32, tuple33, elements34, map35, key37, value39, source42, arguments44, body46, iterators48, result49, variable51, in_53, thenExpression56, condition58, elseExpression60, type62, initExpression64, letExp66, baseExp68, variableExp69, loopExpr70, operation72, elementType74, definitions76, oclExpression77, operation79, mapType281, attribute82, mapType85, collectionTypes87, tupleTypeAttribute88, variableDeclaration90, attributes93, type95, tupleType97, model98, valueType100, keyType102, feature104, context_105, definition108, context_110, definition112, initExpression114, type116, parameters118, returnType119, body122, metamodel124, elements126, model128},
    generalizations={gen_ocl_constraints_OclConstraintsModel_LocatedElement, gen_ocl_constraints_Metaclass_LocatedElement, gen_ocl_constraints_UMLClass_Metaclass, gen_ocl_constraints_Context_LocatedElement, gen_ocl_constraints_OclInvariant_LocatedElement, gen_ocl_constraints_OclPrecondition_LocatedElement, gen_OCL_OclExpression_LocatedElement, gen_OCL_VariableExp_OclExpression, gen_OCL_SuperExp_OclExpression, gen_OCL_PrimitiveExp_OclExpression, gen_OCL_StringExp_PrimitiveExp, gen_OCL_BooleanExp_PrimitiveExp, gen_OCL_NumericExp_PrimitiveExp, gen_OCL_RealExp_NumericExp, gen_OCL_IntegerExp_NumericExp, gen_OCL_CollectionExp_OclExpression, gen_OCL_BagExp_CollectionExp, gen_OCL_OrderedSetExp_CollectionExp, gen_OCL_SequenceExp_CollectionExp, gen_OCL_SetExp_CollectionExp, gen_OCL_TupleExp_OclExpression, gen_OCL_TuplePart_VariableDeclaration, gen_OCL_MapExp_OclExpression, gen_OCL_MapElement_LocatedElement, gen_OCL_EnumLiteralExp_OclExpression, gen_OCL_OclUndefinedExp_OclExpression, gen_OCL_PropertyCallExp_OclExpression, gen_OCL_NavigationOrAttributeCallExp_PropertyCallExp, gen_OCL_OperationCallExp_PropertyCallExp, gen_OCL_OperatorCallExp_OperationCallExp, gen_OCL_CollectionOperationCallExp_OperationCallExp, gen_OCL_LoopExp_PropertyCallExp, gen_OCL_IterateExp_LoopExp, gen_OCL_IteratorExp_LoopExp, gen_OCL_LetExp_OclExpression, gen_OCL_IfExp_OclExpression, gen_OCL_VariableDeclaration_LocatedElement, gen_OCL_CollectionType_OclType, gen_OCL_Iterator_VariableDeclaration, gen_OCL_Parameter_VariableDeclaration, gen_OCL_TupleType_OclType, gen_OCL_OclType_OclExpression, gen_OCL_Primitive_OclType, gen_OCL_StringType_Primitive, gen_OCL_BooleanType_Primitive, gen_OCL_NumericType_Primitive, gen_OCL_IntegerType_NumericType, gen_OCL_RealType_NumericType, gen_OCL_BagType_CollectionType, gen_OCL_OrderedSetType_CollectionType, gen_OCL_SequenceType_CollectionType, gen_OCL_SetType_CollectionType, gen_OCL_OclAnyType_OclType, gen_OCL_TupleTypeAttribute_LocatedElement, gen_OCL_OclModelElement_OclType, gen_OCL_MapType_OclType, gen_OCL_OclFeatureDefinition_LocatedElement, gen_OCL_OclContextDefinition_LocatedElement, gen_OCL_OclFeature_LocatedElement, gen_OCL_Attribute_OclFeature, gen_OCL_Operation_OclFeature, gen_OCL_OclModel_LocatedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)