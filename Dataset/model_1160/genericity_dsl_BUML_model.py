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
genericity_dsl_BindingModel = Class(name="genericity_dsl_BindingModel")
LocatedElement = Class(name="LocatedElement")
ConceptBinding = Class(name="ConceptBinding")
BHelper = Class(name="BHelper")
VariableDeclaration = Class(name="VariableDeclaration")
genericity_dsl_Metaclass = Class(name="genericity_dsl_Metaclass", is_abstract=True)
genericity_dsl_ClassBinding = Class(name="genericity_dsl_ClassBinding")
ConceptMetaclass = Class(name="ConceptMetaclass")
ConcreteMetaclass = Class(name="ConcreteMetaclass")
OclExpression = Class(name="OclExpression")
genericity_dsl_BaseFeatureBinding = Class(name="genericity_dsl_BaseFeatureBinding")
genericity_dsl_RenamingFeatureBinding = Class(name="genericity_dsl_RenamingFeatureBinding")
BaseFeatureBinding = Class(name="BaseFeatureBinding")
genericity_dsl_OclFeatureBinding = Class(name="genericity_dsl_OclFeatureBinding")
genericity_dsl_BHelper = Class(name="genericity_dsl_BHelper")
OclType = Class(name="OclType")
genericity_dsl_LocatedElement = Class(name="genericity_dsl_LocatedElement", is_abstract=True)
genericity_dsl_ConceptMetaclass = Class(name="genericity_dsl_ConceptMetaclass")
Metaclass = Class(name="Metaclass")
genericity_dsl_ConcreteMetaclass = Class(name="genericity_dsl_ConcreteMetaclass")
genericity_dsl_ConceptBinding = Class(name="genericity_dsl_ConceptBinding", is_abstract=True)
BindingModel = Class(name="BindingModel")
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
OCL_OclExpression = Class(name="OCL_OclExpression", is_abstract=True)
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
OCL_BooleanExp = Class(name="OCL_BooleanExp")
OCL_NumericExp = Class(name="OCL_NumericExp", is_abstract=True)
OCL_RealExp = Class(name="OCL_RealExp")
NumericExp = Class(name="NumericExp")
OCL_IntegerExp = Class(name="OCL_IntegerExp")
OCL_OperationCallExp = Class(name="OCL_OperationCallExp")
OCL_OperatorCallExp = Class(name="OCL_OperatorCallExp")
OCL_CollectionOperationCallExp = Class(name="OCL_CollectionOperationCallExp")
OCL_LoopExp = Class(name="OCL_LoopExp", is_abstract=True)
Iterator = Class(name="Iterator")
OCL_IterateExp = Class(name="OCL_IterateExp")
OCL_IteratorExp = Class(name="OCL_IteratorExp")
OCL_LetExp = Class(name="OCL_LetExp")
OCL_IfExp = Class(name="OCL_IfExp")
OCL_PropertyCallExp = Class(name="OCL_PropertyCallExp", is_abstract=True)
OCL_NavigationOrAttributeCallExp = Class(name="OCL_NavigationOrAttributeCallExp")
OCL_VariableDeclaration = Class(name="OCL_VariableDeclaration")
IterateExp = Class(name="IterateExp")
VariableExp = Class(name="VariableExp")
OCL_Iterator = Class(name="OCL_Iterator")
OCL_Parameter = Class(name="OCL_Parameter")
OCL_CollectionType = Class(name="OCL_CollectionType")
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
TupleType = Class(name="TupleType")
OCL_OclModelElement = Class(name="OCL_OclModelElement")
OclModel = Class(name="OclModel")
OCL_MapType = Class(name="OCL_MapType")
OCL_OclFeatureDefinition = Class(name="OCL_OclFeatureDefinition")
OclFeature = Class(name="OclFeature")
OCL_OclContextDefinition = Class(name="OCL_OclContextDefinition")
OclFeatureDefinition = Class(name="OclFeatureDefinition")
OCL_OclFeature = Class(name="OCL_OclFeature", is_abstract=True)
OCL_TupleType = Class(name="OCL_TupleType")
OCL_TupleTypeAttribute = Class(name="OCL_TupleTypeAttribute")
OCL_Operation = Class(name="OCL_Operation")
Parameter_ = Class(name="Parameter")
OCL_OclModel = Class(name="OCL_OclModel")
OclModelElement = Class(name="OclModelElement")
OCL_Attribute = Class(name="OCL_Attribute")

# genericity_dsl_BindingModel class attributes and methods
genericity_dsl_BindingModel_metamodel: Property = Property(name="metamodel", type=StringType)
genericity_dsl_BindingModel_name: Property = Property(name="name", type=StringType)
genericity_dsl_BindingModel.attributes={genericity_dsl_BindingModel_metamodel, genericity_dsl_BindingModel_name}

# LocatedElement class attributes and methods

# ConceptBinding class attributes and methods

# BHelper class attributes and methods

# VariableDeclaration class attributes and methods

# genericity_dsl_Metaclass class attributes and methods
genericity_dsl_Metaclass_name: Property = Property(name="name", type=StringType)
genericity_dsl_Metaclass.attributes={genericity_dsl_Metaclass_name}

# genericity_dsl_ClassBinding class attributes and methods

# ConceptMetaclass class attributes and methods

# ConcreteMetaclass class attributes and methods

# OclExpression class attributes and methods

# genericity_dsl_BaseFeatureBinding class attributes and methods
genericity_dsl_BaseFeatureBinding_conceptFeature: Property = Property(name="conceptFeature", type=StringType)
genericity_dsl_BaseFeatureBinding.attributes={genericity_dsl_BaseFeatureBinding_conceptFeature}

# genericity_dsl_RenamingFeatureBinding class attributes and methods
genericity_dsl_RenamingFeatureBinding_concreteFeature: Property = Property(name="concreteFeature", type=StringType)
genericity_dsl_RenamingFeatureBinding.attributes={genericity_dsl_RenamingFeatureBinding_concreteFeature}

# BaseFeatureBinding class attributes and methods

# genericity_dsl_OclFeatureBinding class attributes and methods

# genericity_dsl_BHelper class attributes and methods
genericity_dsl_BHelper_feature: Property = Property(name="feature", type=StringType)
genericity_dsl_BHelper.attributes={genericity_dsl_BHelper_feature}

# OclType class attributes and methods

# genericity_dsl_LocatedElement class attributes and methods
genericity_dsl_LocatedElement_location: Property = Property(name="location", type=StringType)
genericity_dsl_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
genericity_dsl_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
genericity_dsl_LocatedElement.attributes={genericity_dsl_LocatedElement_commentsAfter, genericity_dsl_LocatedElement_location, genericity_dsl_LocatedElement_commentsBefore}

# genericity_dsl_ConceptMetaclass class attributes and methods

# Metaclass class attributes and methods

# genericity_dsl_ConcreteMetaclass class attributes and methods

# genericity_dsl_ConceptBinding class attributes and methods
genericity_dsl_ConceptBinding_debugName: Property = Property(name="debugName", type=StringType)
genericity_dsl_ConceptBinding.attributes={genericity_dsl_ConceptBinding_debugName}

# BindingModel class attributes and methods

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

# OCL_OclExpression class attributes and methods

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

# OCL_PropertyCallExp class attributes and methods

# OCL_NavigationOrAttributeCallExp class attributes and methods
OCL_NavigationOrAttributeCallExp_name: Property = Property(name="name", type=StringType)
OCL_NavigationOrAttributeCallExp.attributes={OCL_NavigationOrAttributeCallExp_name}

# OCL_VariableDeclaration class attributes and methods
OCL_VariableDeclaration_id: Property = Property(name="id", type=StringType)
OCL_VariableDeclaration_varName: Property = Property(name="varName", type=StringType)
OCL_VariableDeclaration.attributes={OCL_VariableDeclaration_id, OCL_VariableDeclaration_varName}

# IterateExp class attributes and methods

# VariableExp class attributes and methods

# OCL_Iterator class attributes and methods

# OCL_Parameter class attributes and methods

# OCL_CollectionType class attributes and methods

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

# TupleType class attributes and methods

# OCL_OclModelElement class attributes and methods

# OclModel class attributes and methods

# OCL_MapType class attributes and methods

# OCL_OclFeatureDefinition class attributes and methods

# OclFeature class attributes and methods

# OCL_OclContextDefinition class attributes and methods

# OclFeatureDefinition class attributes and methods

# OCL_OclFeature class attributes and methods

# OCL_TupleType class attributes and methods

# OCL_TupleTypeAttribute class attributes and methods
OCL_TupleTypeAttribute_name: Property = Property(name="name", type=StringType)
OCL_TupleTypeAttribute.attributes={OCL_TupleTypeAttribute_name}

# OCL_Operation class attributes and methods
OCL_Operation_name: Property = Property(name="name", type=StringType)
OCL_Operation.attributes={OCL_Operation_name}

# Parameter class attributes and methods

# OCL_OclModel class attributes and methods
OCL_OclModel_name: Property = Property(name="name", type=StringType)
OCL_OclModel.attributes={OCL_OclModel_name}

# OclModelElement class attributes and methods

# OCL_Attribute class attributes and methods
OCL_Attribute_name: Property = Property(name="name", type=StringType)
OCL_Attribute.attributes={OCL_Attribute_name}

# Relationships
bindings0: BinaryAssociation = BinaryAssociation(
    name="bindings0",
    ends={
        Property(name="ConceptBinding", type=genericity_dsl_BindingModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model_", type=ConceptBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
helpers1: BinaryAssociation = BinaryAssociation(
    name="helpers1",
    ends={
        Property(name="BHelper", type=genericity_dsl_BindingModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model_2", type=BHelper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables3: BinaryAssociation = BinaryAssociation(
    name="variables3",
    ends={
        Property(name="VariableDeclaration", type=genericity_dsl_BindingModel, multiplicity=Multiplicity(1, 1)),
        Property(name="genericity_dsl_BindingModel", type=VariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model_4: BinaryAssociation = BinaryAssociation(
    name="model_4",
    ends={
        Property(name="bindings", type=BindingModel, multiplicity=Multiplicity(0, 1)),
        Property(name="BindingModel", type=genericity_dsl_ConceptBinding, multiplicity=Multiplicity(1, 1))
    }
)
concept5: BinaryAssociation = BinaryAssociation(
    name="concept5",
    ends={
        Property(name="ConceptMetaclass", type=genericity_dsl_ClassBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="genericity_dsl_ClassBinding", type=ConceptMetaclass, multiplicity=Multiplicity(1, 1))
    }
)
concrete6: BinaryAssociation = BinaryAssociation(
    name="concrete6",
    ends={
        Property(name="ConcreteMetaclass", type=genericity_dsl_ClassBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="genericity_dsl_ClassBinding7", type=ConcreteMetaclass, multiplicity=Multiplicity(1, 9999))
    }
)
whenClause8: BinaryAssociation = BinaryAssociation(
    name="whenClause8",
    ends={
        Property(name="OclExpression", type=genericity_dsl_ClassBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="genericity_dsl_ClassBinding9", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
conceptClass10: BinaryAssociation = BinaryAssociation(
    name="conceptClass10",
    ends={
        Property(name="ConceptMetaclass11", type=genericity_dsl_BaseFeatureBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="genericity_dsl_BaseFeatureBinding", type=ConceptMetaclass, multiplicity=Multiplicity(1, 1))
    }
)
qualifier12: BinaryAssociation = BinaryAssociation(
    name="qualifier12",
    ends={
        Property(name="ConcreteMetaclass14", type=genericity_dsl_BaseFeatureBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="genericity_dsl_BaseFeatureBinding13", type=ConcreteMetaclass, multiplicity=Multiplicity(0, 1))
    }
)
concrete15: BinaryAssociation = BinaryAssociation(
    name="concrete15",
    ends={
        Property(name="OclExpression16", type=genericity_dsl_OclFeatureBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="genericity_dsl_OclFeatureBinding", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
contextClass17: BinaryAssociation = BinaryAssociation(
    name="contextClass17",
    ends={
        Property(name="ConceptMetaclass18", type=genericity_dsl_BHelper, multiplicity=Multiplicity(1, 1)),
        Property(name="genericity_dsl_BHelper", type=ConceptMetaclass, multiplicity=Multiplicity(1, 1))
    }
)
body19: BinaryAssociation = BinaryAssociation(
    name="body19",
    ends={
        Property(name="OclExpression21", type=genericity_dsl_BHelper, multiplicity=Multiplicity(1, 1)),
        Property(name="genericity_dsl_BHelper20", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type22: BinaryAssociation = BinaryAssociation(
    name="type22",
    ends={
        Property(name="OclType", type=genericity_dsl_BHelper, multiplicity=Multiplicity(1, 1)),
        Property(name="genericity_dsl_BHelper23", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
model_24: BinaryAssociation = BinaryAssociation(
    name="model_24",
    ends={
        Property(name="BindingModel25", type=genericity_dsl_BHelper, multiplicity=Multiplicity(1, 1)),
        Property(name="helpers", type=BindingModel, multiplicity=Multiplicity(0, 1))
    }
)
type26: BinaryAssociation = BinaryAssociation(
    name="type26",
    ends={
        Property(name="oclExpression", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="OclType27", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1))
    }
)
ifExp328: BinaryAssociation = BinaryAssociation(
    name="ifExp328",
    ends={
        Property(name="IfExp", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="elseExpression", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
appliedProperty29: BinaryAssociation = BinaryAssociation(
    name="appliedProperty29",
    ends={
        Property(name="PropertyCallExp", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=PropertyCallExp, multiplicity=Multiplicity(0, 1))
    }
)
collection30: BinaryAssociation = BinaryAssociation(
    name="collection30",
    ends={
        Property(name="CollectionExp", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=CollectionExp, multiplicity=Multiplicity(0, 1))
    }
)
letExp31: BinaryAssociation = BinaryAssociation(
    name="letExp31",
    ends={
        Property(name="LetExp", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="in_", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
loopExp32: BinaryAssociation = BinaryAssociation(
    name="loopExp32",
    ends={
        Property(name="LoopExp", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="body", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
parentOperation33: BinaryAssociation = BinaryAssociation(
    name="parentOperation33",
    ends={
        Property(name="OperationCallExp", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="arguments", type=OperationCallExp, multiplicity=Multiplicity(0, 1))
    }
)
initializedVariable34: BinaryAssociation = BinaryAssociation(
    name="initializedVariable34",
    ends={
        Property(name="VariableDeclaration35", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="initExpression", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
ifExp236: BinaryAssociation = BinaryAssociation(
    name="ifExp236",
    ends={
        Property(name="IfExp37", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thenExpression", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningOperation38: BinaryAssociation = BinaryAssociation(
    name="owningOperation38",
    ends={
        Property(name="Operation", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="body39", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
ifExp140: BinaryAssociation = BinaryAssociation(
    name="ifExp140",
    ends={
        Property(name="IfExp41", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="condition", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningAttribute42: BinaryAssociation = BinaryAssociation(
    name="owningAttribute42",
    ends={
        Property(name="Attribute", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="initExpression43", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable44: BinaryAssociation = BinaryAssociation(
    name="referredVariable44",
    ends={
        Property(name="VariableDeclaration45", type=OCL_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="variableExp", type=VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
elements46: BinaryAssociation = BinaryAssociation(
    name="elements46",
    ends={
        Property(name="OclExpression47", type=OCL_CollectionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="collection", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuplePart48: BinaryAssociation = BinaryAssociation(
    name="tuplePart48",
    ends={
        Property(name="TuplePart", type=OCL_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="tuple", type=TuplePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuple49: BinaryAssociation = BinaryAssociation(
    name="tuple49",
    ends={
        Property(name="TupleExp", type=OCL_TuplePart, multiplicity=Multiplicity(1, 1)),
        Property(name="tuplePart", type=TupleExp, multiplicity=Multiplicity(1, 1))
    }
)
elements50: BinaryAssociation = BinaryAssociation(
    name="elements50",
    ends={
        Property(name="MapElement", type=OCL_MapExp, multiplicity=Multiplicity(1, 1)),
        Property(name="map", type=MapElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
map51: BinaryAssociation = BinaryAssociation(
    name="map51",
    ends={
        Property(name="MapExp", type=OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements52", type=MapExp, multiplicity=Multiplicity(1, 1))
    }
)
key53: BinaryAssociation = BinaryAssociation(
    name="key53",
    ends={
        Property(name="OclExpression54", type=OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_MapElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value55: BinaryAssociation = BinaryAssociation(
    name="value55",
    ends={
        Property(name="OclExpression57", type=OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_MapElement56", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments60: BinaryAssociation = BinaryAssociation(
    name="arguments60",
    ends={
        Property(name="OclExpression61", type=OCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="parentOperation", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body62: BinaryAssociation = BinaryAssociation(
    name="body62",
    ends={
        Property(name="OclExpression63", type=OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="loopExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterators64: BinaryAssociation = BinaryAssociation(
    name="iterators64",
    ends={
        Property(name="Iterator", type=OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="loopExpr", type=Iterator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result65: BinaryAssociation = BinaryAssociation(
    name="result65",
    ends={
        Property(name="VariableDeclaration66", type=OCL_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="baseExp", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable67: BinaryAssociation = BinaryAssociation(
    name="variable67",
    ends={
        Property(name="VariableDeclaration68", type=OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="letExp", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in_69: BinaryAssociation = BinaryAssociation(
    name="in_69",
    ends={
        Property(name="OclExpression71", type=OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="letExp70", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression72: BinaryAssociation = BinaryAssociation(
    name="thenExpression72",
    ends={
        Property(name="OclExpression73", type=OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp2", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source58: BinaryAssociation = BinaryAssociation(
    name="source58",
    ends={
        Property(name="OclExpression59", type=OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="appliedProperty", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type78: BinaryAssociation = BinaryAssociation(
    name="type78",
    ends={
        Property(name="OclType79", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variableDeclaration", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression80: BinaryAssociation = BinaryAssociation(
    name="initExpression80",
    ends={
        Property(name="OclExpression81", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="initializedVariable", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
letExp82: BinaryAssociation = BinaryAssociation(
    name="letExp82",
    ends={
        Property(name="LetExp83", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
baseExp84: BinaryAssociation = BinaryAssociation(
    name="baseExp84",
    ends={
        Property(name="IterateExp", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="result", type=IterateExp, multiplicity=Multiplicity(0, 1))
    }
)
variableExp85: BinaryAssociation = BinaryAssociation(
    name="variableExp85",
    ends={
        Property(name="VariableExp", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="referredVariable", type=VariableExp, multiplicity=Multiplicity(0, 9999))
    }
)
loopExpr86: BinaryAssociation = BinaryAssociation(
    name="loopExpr86",
    ends={
        Property(name="LoopExp87", type=OCL_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="iterators", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
operation88: BinaryAssociation = BinaryAssociation(
    name="operation88",
    ends={
        Property(name="Operation89", type=OCL_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
elementType90: BinaryAssociation = BinaryAssociation(
    name="elementType90",
    ends={
        Property(name="OclType91", type=OCL_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="collectionTypes", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition74: BinaryAssociation = BinaryAssociation(
    name="condition74",
    ends={
        Property(name="OclExpression75", type=OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp1", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression76: BinaryAssociation = BinaryAssociation(
    name="elseExpression76",
    ends={
        Property(name="OclExpression77", type=OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp3", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operation95: BinaryAssociation = BinaryAssociation(
    name="operation95",
    ends={
        Property(name="Operation96", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="returnType", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
mapType297: BinaryAssociation = BinaryAssociation(
    name="mapType297",
    ends={
        Property(name="MapType", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="valueType", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
attribute98: BinaryAssociation = BinaryAssociation(
    name="attribute98",
    ends={
        Property(name="Attribute100", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type99", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
mapType101: BinaryAssociation = BinaryAssociation(
    name="mapType101",
    ends={
        Property(name="MapType102", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="keyType", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
collectionTypes103: BinaryAssociation = BinaryAssociation(
    name="collectionTypes103",
    ends={
        Property(name="CollectionType", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="elementType", type=CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
tupleTypeAttribute104: BinaryAssociation = BinaryAssociation(
    name="tupleTypeAttribute104",
    ends={
        Property(name="TupleTypeAttribute", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type105", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclaration106: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration106",
    ends={
        Property(name="VariableDeclaration108", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type107", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
definitions92: BinaryAssociation = BinaryAssociation(
    name="definitions92",
    ends={
        Property(name="OclContextDefinition", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="context_", type=OclContextDefinition, multiplicity=Multiplicity(0, 1))
    }
)
oclExpression93: BinaryAssociation = BinaryAssociation(
    name="oclExpression93",
    ends={
        Property(name="OclExpression94", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=OclExpression, multiplicity=Multiplicity(0, 1))
    }
)
type111: BinaryAssociation = BinaryAssociation(
    name="type111",
    ends={
        Property(name="OclType112", type=OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="tupleTypeAttribute", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tupleType113: BinaryAssociation = BinaryAssociation(
    name="tupleType113",
    ends={
        Property(name="TupleType", type=OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=TupleType, multiplicity=Multiplicity(1, 1))
    }
)
model114: BinaryAssociation = BinaryAssociation(
    name="model114",
    ends={
        Property(name="OclModel", type=OCL_OclModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements115", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
valueType116: BinaryAssociation = BinaryAssociation(
    name="valueType116",
    ends={
        Property(name="OclType117", type=OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="mapType2", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
keyType118: BinaryAssociation = BinaryAssociation(
    name="keyType118",
    ends={
        Property(name="OclType119", type=OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="mapType", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
feature120: BinaryAssociation = BinaryAssociation(
    name="feature120",
    ends={
        Property(name="OclFeature", type=OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definition", type=OclFeature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context_121: BinaryAssociation = BinaryAssociation(
    name="context_121",
    ends={
        Property(name="OclContextDefinition123", type=OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definition122", type=OclContextDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition124: BinaryAssociation = BinaryAssociation(
    name="definition124",
    ends={
        Property(name="OclFeatureDefinition", type=OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="context_125", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1))
    }
)
context_126: BinaryAssociation = BinaryAssociation(
    name="context_126",
    ends={
        Property(name="OclType127", type=OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definitions", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attributes109: BinaryAssociation = BinaryAssociation(
    name="attributes109",
    ends={
        Property(name="TupleTypeAttribute110", type=OCL_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="tupleType", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type132: BinaryAssociation = BinaryAssociation(
    name="type132",
    ends={
        Property(name="OclType133", type=OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attribute", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters134: BinaryAssociation = BinaryAssociation(
    name="parameters134",
    ends={
        Property(name="Parameter", type=OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType135: BinaryAssociation = BinaryAssociation(
    name="returnType135",
    ends={
        Property(name="OclType137", type=OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation136", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body138: BinaryAssociation = BinaryAssociation(
    name="body138",
    ends={
        Property(name="OclExpression139", type=OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="owningOperation", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metamodel140: BinaryAssociation = BinaryAssociation(
    name="metamodel140",
    ends={
        Property(name="OclModel141", type=OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
elements142: BinaryAssociation = BinaryAssociation(
    name="elements142",
    ends={
        Property(name="OclModelElement", type=OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model143", type=OclModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
model144: BinaryAssociation = BinaryAssociation(
    name="model144",
    ends={
        Property(name="OclModel145", type=OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)
definition128: BinaryAssociation = BinaryAssociation(
    name="definition128",
    ends={
        Property(name="OclFeatureDefinition129", type=OCL_OclFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=OclFeatureDefinition, multiplicity=Multiplicity(0, 1))
    }
)
initExpression130: BinaryAssociation = BinaryAssociation(
    name="initExpression130",
    ends={
        Property(name="OclExpression131", type=OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="owningAttribute", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_genericity_dsl_BindingModel_LocatedElement = Generalization(general=LocatedElement, specific=genericity_dsl_BindingModel)
gen_genericity_dsl_Metaclass_LocatedElement = Generalization(general=LocatedElement, specific=genericity_dsl_Metaclass)
gen_genericity_dsl_ClassBinding_ConceptBinding = Generalization(general=ConceptBinding, specific=genericity_dsl_ClassBinding)
gen_genericity_dsl_BaseFeatureBinding_ConceptBinding = Generalization(general=ConceptBinding, specific=genericity_dsl_BaseFeatureBinding)
gen_genericity_dsl_RenamingFeatureBinding_BaseFeatureBinding = Generalization(general=BaseFeatureBinding, specific=genericity_dsl_RenamingFeatureBinding)
gen_genericity_dsl_OclFeatureBinding_BaseFeatureBinding = Generalization(general=BaseFeatureBinding, specific=genericity_dsl_OclFeatureBinding)
gen_genericity_dsl_BHelper_LocatedElement = Generalization(general=LocatedElement, specific=genericity_dsl_BHelper)
gen_genericity_dsl_ConceptMetaclass_Metaclass = Generalization(general=Metaclass, specific=genericity_dsl_ConceptMetaclass)
gen_genericity_dsl_ConcreteMetaclass_Metaclass = Generalization(general=Metaclass, specific=genericity_dsl_ConcreteMetaclass)
gen_genericity_dsl_ConceptBinding_LocatedElement = Generalization(general=LocatedElement, specific=genericity_dsl_ConceptBinding)
gen_OCL_VariableExp_OclExpression = Generalization(general=OclExpression, specific=OCL_VariableExp)
gen_OCL_SuperExp_OclExpression = Generalization(general=OclExpression, specific=OCL_SuperExp)
gen_OCL_PrimitiveExp_OclExpression = Generalization(general=OclExpression, specific=OCL_PrimitiveExp)
gen_OCL_StringExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=OCL_StringExp)
gen_OCL_OclExpression_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclExpression)
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
gen_OCL_BooleanExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=OCL_BooleanExp)
gen_OCL_NumericExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=OCL_NumericExp)
gen_OCL_RealExp_NumericExp = Generalization(general=NumericExp, specific=OCL_RealExp)
gen_OCL_IntegerExp_NumericExp = Generalization(general=NumericExp, specific=OCL_IntegerExp)
gen_OCL_OperationCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=OCL_OperationCallExp)
gen_OCL_OperatorCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=OCL_OperatorCallExp)
gen_OCL_CollectionOperationCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=OCL_CollectionOperationCallExp)
gen_OCL_LoopExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=OCL_LoopExp)
gen_OCL_IterateExp_LoopExp = Generalization(general=LoopExp, specific=OCL_IterateExp)
gen_OCL_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=OCL_IteratorExp)
gen_OCL_LetExp_OclExpression = Generalization(general=OclExpression, specific=OCL_LetExp)
gen_OCL_IfExp_OclExpression = Generalization(general=OclExpression, specific=OCL_IfExp)
gen_OCL_PropertyCallExp_OclExpression = Generalization(general=OclExpression, specific=OCL_PropertyCallExp)
gen_OCL_NavigationOrAttributeCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=OCL_NavigationOrAttributeCallExp)
gen_OCL_VariableDeclaration_LocatedElement = Generalization(general=LocatedElement, specific=OCL_VariableDeclaration)
gen_OCL_Iterator_VariableDeclaration = Generalization(general=VariableDeclaration, specific=OCL_Iterator)
gen_OCL_Parameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=OCL_Parameter)
gen_OCL_CollectionType_OclType = Generalization(general=OclType, specific=OCL_CollectionType)
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
gen_OCL_OclModelElement_OclType = Generalization(general=OclType, specific=OCL_OclModelElement)
gen_OCL_MapType_OclType = Generalization(general=OclType, specific=OCL_MapType)
gen_OCL_OclFeatureDefinition_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclFeatureDefinition)
gen_OCL_OclContextDefinition_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclContextDefinition)
gen_OCL_OclFeature_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclFeature)
gen_OCL_OclAnyType_OclType = Generalization(general=OclType, specific=OCL_OclAnyType)
gen_OCL_TupleType_OclType = Generalization(general=OclType, specific=OCL_TupleType)
gen_OCL_TupleTypeAttribute_LocatedElement = Generalization(general=LocatedElement, specific=OCL_TupleTypeAttribute)
gen_OCL_Operation_OclFeature = Generalization(general=OclFeature, specific=OCL_Operation)
gen_OCL_OclModel_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclModel)
gen_OCL_Attribute_OclFeature = Generalization(general=OclFeature, specific=OCL_Attribute)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={genericity_dsl_BindingModel, LocatedElement, ConceptBinding, BHelper, VariableDeclaration, genericity_dsl_Metaclass, genericity_dsl_ClassBinding, ConceptMetaclass, ConcreteMetaclass, OclExpression, genericity_dsl_BaseFeatureBinding, genericity_dsl_RenamingFeatureBinding, BaseFeatureBinding, genericity_dsl_OclFeatureBinding, genericity_dsl_BHelper, OclType, genericity_dsl_LocatedElement, genericity_dsl_ConceptMetaclass, Metaclass, genericity_dsl_ConcreteMetaclass, genericity_dsl_ConceptBinding, BindingModel, IfExp, PropertyCallExp, CollectionExp, LetExp, LoopExp, OperationCallExp, Operation, Attribute, OCL_VariableExp, OCL_SuperExp, OCL_PrimitiveExp, OCL_StringExp, PrimitiveExp, OCL_OclExpression, OCL_CollectionExp, OCL_BagExp, OCL_OrderedSetExp, OCL_SequenceExp, OCL_SetExp, OCL_TupleExp, TuplePart, OCL_TuplePart, TupleExp, OCL_MapExp, MapElement, OCL_MapElement, MapExp, OCL_EnumLiteralExp, OCL_OclUndefinedExp, OCL_BooleanExp, OCL_NumericExp, OCL_RealExp, NumericExp, OCL_IntegerExp, OCL_OperationCallExp, OCL_OperatorCallExp, OCL_CollectionOperationCallExp, OCL_LoopExp, Iterator, OCL_IterateExp, OCL_IteratorExp, OCL_LetExp, OCL_IfExp, OCL_PropertyCallExp, OCL_NavigationOrAttributeCallExp, OCL_VariableDeclaration, IterateExp, VariableExp, OCL_Iterator, OCL_Parameter, OCL_CollectionType, OCL_OclType, OclContextDefinition, MapType, CollectionType, TupleTypeAttribute, OCL_Primitive, OCL_StringType, Primitive, OCL_BooleanType, OCL_NumericType, OCL_IntegerType, NumericType, OCL_RealType, OCL_BagType, OCL_OrderedSetType, OCL_SequenceType, OCL_SetType, OCL_OclAnyType, TupleType, OCL_OclModelElement, OclModel, OCL_MapType, OCL_OclFeatureDefinition, OclFeature, OCL_OclContextDefinition, OclFeatureDefinition, OCL_OclFeature, OCL_TupleType, OCL_TupleTypeAttribute, OCL_Operation, Parameter_, OCL_OclModel, OclModelElement, OCL_Attribute},
    associations={bindings0, helpers1, variables3, model_4, concept5, concrete6, whenClause8, conceptClass10, qualifier12, concrete15, contextClass17, body19, type22, model_24, type26, ifExp328, appliedProperty29, collection30, letExp31, loopExp32, parentOperation33, initializedVariable34, ifExp236, owningOperation38, ifExp140, owningAttribute42, referredVariable44, elements46, tuplePart48, tuple49, elements50, map51, key53, value55, arguments60, body62, iterators64, result65, variable67, in_69, thenExpression72, source58, type78, initExpression80, letExp82, baseExp84, variableExp85, loopExpr86, operation88, elementType90, condition74, elseExpression76, operation95, mapType297, attribute98, mapType101, collectionTypes103, tupleTypeAttribute104, variableDeclaration106, definitions92, oclExpression93, type111, tupleType113, model114, valueType116, keyType118, feature120, context_121, definition124, context_126, attributes109, type132, parameters134, returnType135, body138, metamodel140, elements142, model144, definition128, initExpression130},
    generalizations={gen_genericity_dsl_BindingModel_LocatedElement, gen_genericity_dsl_Metaclass_LocatedElement, gen_genericity_dsl_ClassBinding_ConceptBinding, gen_genericity_dsl_BaseFeatureBinding_ConceptBinding, gen_genericity_dsl_RenamingFeatureBinding_BaseFeatureBinding, gen_genericity_dsl_OclFeatureBinding_BaseFeatureBinding, gen_genericity_dsl_BHelper_LocatedElement, gen_genericity_dsl_ConceptMetaclass_Metaclass, gen_genericity_dsl_ConcreteMetaclass_Metaclass, gen_genericity_dsl_ConceptBinding_LocatedElement, gen_OCL_VariableExp_OclExpression, gen_OCL_SuperExp_OclExpression, gen_OCL_PrimitiveExp_OclExpression, gen_OCL_StringExp_PrimitiveExp, gen_OCL_OclExpression_LocatedElement, gen_OCL_CollectionExp_OclExpression, gen_OCL_BagExp_CollectionExp, gen_OCL_OrderedSetExp_CollectionExp, gen_OCL_SequenceExp_CollectionExp, gen_OCL_SetExp_CollectionExp, gen_OCL_TupleExp_OclExpression, gen_OCL_TuplePart_VariableDeclaration, gen_OCL_MapExp_OclExpression, gen_OCL_MapElement_LocatedElement, gen_OCL_EnumLiteralExp_OclExpression, gen_OCL_OclUndefinedExp_OclExpression, gen_OCL_BooleanExp_PrimitiveExp, gen_OCL_NumericExp_PrimitiveExp, gen_OCL_RealExp_NumericExp, gen_OCL_IntegerExp_NumericExp, gen_OCL_OperationCallExp_PropertyCallExp, gen_OCL_OperatorCallExp_OperationCallExp, gen_OCL_CollectionOperationCallExp_OperationCallExp, gen_OCL_LoopExp_PropertyCallExp, gen_OCL_IterateExp_LoopExp, gen_OCL_IteratorExp_LoopExp, gen_OCL_LetExp_OclExpression, gen_OCL_IfExp_OclExpression, gen_OCL_PropertyCallExp_OclExpression, gen_OCL_NavigationOrAttributeCallExp_PropertyCallExp, gen_OCL_VariableDeclaration_LocatedElement, gen_OCL_Iterator_VariableDeclaration, gen_OCL_Parameter_VariableDeclaration, gen_OCL_CollectionType_OclType, gen_OCL_OclType_OclExpression, gen_OCL_Primitive_OclType, gen_OCL_StringType_Primitive, gen_OCL_BooleanType_Primitive, gen_OCL_NumericType_Primitive, gen_OCL_IntegerType_NumericType, gen_OCL_RealType_NumericType, gen_OCL_BagType_CollectionType, gen_OCL_OrderedSetType_CollectionType, gen_OCL_SequenceType_CollectionType, gen_OCL_SetType_CollectionType, gen_OCL_OclModelElement_OclType, gen_OCL_MapType_OclType, gen_OCL_OclFeatureDefinition_LocatedElement, gen_OCL_OclContextDefinition_LocatedElement, gen_OCL_OclFeature_LocatedElement, gen_OCL_OclAnyType_OclType, gen_OCL_TupleType_OclType, gen_OCL_TupleTypeAttribute_LocatedElement, gen_OCL_Operation_OclFeature, gen_OCL_OclModel_LocatedElement, gen_OCL_Attribute_OclFeature},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)