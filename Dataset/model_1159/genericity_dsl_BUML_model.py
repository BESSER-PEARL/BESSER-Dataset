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
genericity_dsl_BindingModel = Class(name="genericity::dsl::BindingModel")
LocatedElement = Class(name="LocatedElement")
ConceptBinding = Class(name="ConceptBinding")
BHelper = Class(name="BHelper")
VariableDeclaration = Class(name="VariableDeclaration")
genericity_dsl_Metaclass = Class(name="genericity::dsl::Metaclass", is_abstract=True)
genericity_dsl_ConceptMetaclass = Class(name="genericity::dsl::ConceptMetaclass")
Metaclass = Class(name="Metaclass")
genericity_dsl_ConcreteMetaclass = Class(name="genericity::dsl::ConcreteMetaclass")
genericity_dsl_ClassBinding = Class(name="genericity::dsl::ClassBinding")
ConceptMetaclass = Class(name="ConceptMetaclass")
ConcreteMetaclass = Class(name="ConcreteMetaclass")
OclExpression = Class(name="OclExpression")
genericity_dsl_BaseFeatureBinding = Class(name="genericity::dsl::BaseFeatureBinding")
genericity_dsl_RenamingFeatureBinding = Class(name="genericity::dsl::RenamingFeatureBinding")
BaseFeatureBinding = Class(name="BaseFeatureBinding")
genericity_dsl_OclFeatureBinding = Class(name="genericity::dsl::OclFeatureBinding")
genericity_dsl_BHelper = Class(name="genericity::dsl::BHelper")
OclType = Class(name="OclType")
genericity_dsl_ConceptBinding = Class(name="genericity::dsl::ConceptBinding", is_abstract=True)
BindingModel = Class(name="BindingModel")
OCL_OclExpression = Class(name="OCL::OclExpression", is_abstract=True)
IfExp = Class(name="IfExp")
PropertyCallExp = Class(name="PropertyCallExp")
CollectionExp = Class(name="CollectionExp")
LetExp = Class(name="LetExp")
LoopExp = Class(name="LoopExp")
OperationCallExp = Class(name="OperationCallExp")
Operation = Class(name="Operation")
genericity_dsl_LocatedElement = Class(name="genericity::dsl::LocatedElement", is_abstract=True)
OCL_VariableExp = Class(name="OCL::VariableExp")
OCL_SuperExp = Class(name="OCL::SuperExp")
OCL_PrimitiveExp = Class(name="OCL::PrimitiveExp", is_abstract=True)
OCL_StringExp = Class(name="OCL::StringExp")
PrimitiveExp = Class(name="PrimitiveExp")
OCL_BooleanExp = Class(name="OCL::BooleanExp")
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
Attribute = Class(name="Attribute")
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
OCL_TuplePart = Class(name="OCL::TuplePart")
TupleExp = Class(name="TupleExp")
OCL_IterateExp = Class(name="OCL::IterateExp")
OCL_IteratorExp = Class(name="OCL::IteratorExp")
OCL_LetExp = Class(name="OCL::LetExp")
OCL_IfExp = Class(name="OCL::IfExp")
OCL_VariableDeclaration = Class(name="OCL::VariableDeclaration")
Iterator = Class(name="Iterator")
OCL_Iterator = Class(name="OCL::Iterator")
OCL_Parameter = Class(name="OCL::Parameter")
OCL_CollectionType = Class(name="OCL::CollectionType")
OCL_OclType = Class(name="OCL::OclType")
OclContextDefinition = Class(name="OclContextDefinition")
MapType = Class(name="MapType")
CollectionType = Class(name="CollectionType")
TupleTypeAttribute = Class(name="TupleTypeAttribute")
IterateExp = Class(name="IterateExp")
VariableExp = Class(name="VariableExp")
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
OCL_SequenceType = Class(name="OCL::SequenceType")
OCL_SetType = Class(name="OCL::SetType")
OCL_OclAnyType = Class(name="OCL::OclAnyType")
OCL_TupleType = Class(name="OCL::TupleType")
OCL_TupleTypeAttribute = Class(name="OCL::TupleTypeAttribute")
TupleType = Class(name="TupleType")
OCL_OclModelElement = Class(name="OCL::OclModelElement")
OclModel = Class(name="OclModel")
OCL_MapType = Class(name="OCL::MapType")
OCL_OclContextDefinition = Class(name="OCL::OclContextDefinition")
OclFeatureDefinition = Class(name="OclFeatureDefinition")
OCL_OclFeature = Class(name="OCL::OclFeature", is_abstract=True)
OCL_Attribute = Class(name="OCL::Attribute")
OCL_Operation = Class(name="OCL::Operation")
Parameter_ = Class(name="Parameter")
OCL_OclModel = Class(name="OCL::OclModel")
OCL_OclFeatureDefinition = Class(name="OCL::OclFeatureDefinition")
OclFeature = Class(name="OclFeature")
OclModelElement = Class(name="OclModelElement")

# genericity_dsl_BindingModel class attributes and methods
genericity_dsl_BindingModel_metamodel: Property = Property(name="metamodel", type=StringType)
genericity_dsl_BindingModel_name: Property = Property(name="name", type=StringType)
genericity_dsl_BindingModel.attributes={genericity_dsl_BindingModel_name, genericity_dsl_BindingModel_metamodel}

# LocatedElement class attributes and methods

# ConceptBinding class attributes and methods

# BHelper class attributes and methods

# VariableDeclaration class attributes and methods

# genericity_dsl_Metaclass class attributes and methods
genericity_dsl_Metaclass_name: Property = Property(name="name", type=StringType)
genericity_dsl_Metaclass.attributes={genericity_dsl_Metaclass_name}

# genericity_dsl_ConceptMetaclass class attributes and methods

# Metaclass class attributes and methods

# genericity_dsl_ConcreteMetaclass class attributes and methods

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

# genericity_dsl_ConceptBinding class attributes and methods
genericity_dsl_ConceptBinding_debugName: Property = Property(name="debugName", type=StringType)
genericity_dsl_ConceptBinding.attributes={genericity_dsl_ConceptBinding_debugName}

# BindingModel class attributes and methods

# OCL_OclExpression class attributes and methods

# IfExp class attributes and methods

# PropertyCallExp class attributes and methods

# CollectionExp class attributes and methods

# LetExp class attributes and methods

# LoopExp class attributes and methods

# OperationCallExp class attributes and methods

# Operation class attributes and methods

# genericity_dsl_LocatedElement class attributes and methods
genericity_dsl_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
genericity_dsl_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
genericity_dsl_LocatedElement_location: Property = Property(name="location", type=StringType)
genericity_dsl_LocatedElement.attributes={genericity_dsl_LocatedElement_location, genericity_dsl_LocatedElement_commentsAfter, genericity_dsl_LocatedElement_commentsBefore}

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

# Attribute class attributes and methods

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

# OCL_TuplePart class attributes and methods

# TupleExp class attributes and methods

# OCL_IterateExp class attributes and methods

# OCL_IteratorExp class attributes and methods
OCL_IteratorExp_name: Property = Property(name="name", type=StringType)
OCL_IteratorExp.attributes={OCL_IteratorExp_name}

# OCL_LetExp class attributes and methods

# OCL_IfExp class attributes and methods

# OCL_VariableDeclaration class attributes and methods
OCL_VariableDeclaration_id: Property = Property(name="id", type=StringType)
OCL_VariableDeclaration_varName: Property = Property(name="varName", type=StringType)
OCL_VariableDeclaration.attributes={OCL_VariableDeclaration_varName, OCL_VariableDeclaration_id}

# Iterator class attributes and methods

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

# IterateExp class attributes and methods

# VariableExp class attributes and methods

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

# OCL_TupleType class attributes and methods

# OCL_TupleTypeAttribute class attributes and methods
OCL_TupleTypeAttribute_name: Property = Property(name="name", type=StringType)
OCL_TupleTypeAttribute.attributes={OCL_TupleTypeAttribute_name}

# TupleType class attributes and methods

# OCL_OclModelElement class attributes and methods

# OclModel class attributes and methods

# OCL_MapType class attributes and methods

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

# OCL_OclFeatureDefinition class attributes and methods

# OclFeature class attributes and methods

# OclModelElement class attributes and methods

# Relationships
bindings0: BinaryAssociation = BinaryAssociation(
    name="bindings0",
    ends={
        Property(name="", type=genericity_dsl_BindingModel, multiplicity=Multiplicity(1, 1)),
        Property(name="0", type=ConceptBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
helpers1: BinaryAssociation = BinaryAssociation(
    name="helpers1",
    ends={
        Property(name="3", type=genericity_dsl_BindingModel, multiplicity=Multiplicity(1, 1)),
        Property(name="02", type=BHelper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables4: BinaryAssociation = BinaryAssociation(
    name="variables4",
    ends={
        Property(name="VariableDeclaration", type=genericity_dsl_BindingModel, multiplicity=Multiplicity(1, 1)),
        Property(name="genericity_dsl_BindingModel", type=VariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model_5: BinaryAssociation = BinaryAssociation(
    name="model_5",
    ends={
        Property(name="7", type=genericity_dsl_ConceptBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="06", type=BindingModel, multiplicity=Multiplicity(0, 1))
    }
)
concept8: BinaryAssociation = BinaryAssociation(
    name="concept8",
    ends={
        Property(name="ConceptMetaclass", type=genericity_dsl_ClassBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="genericity_dsl_ClassBinding", type=ConceptMetaclass, multiplicity=Multiplicity(1, 1))
    }
)
concrete9: BinaryAssociation = BinaryAssociation(
    name="concrete9",
    ends={
        Property(name="ConcreteMetaclass", type=genericity_dsl_ClassBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="genericity_dsl_ClassBinding10", type=ConcreteMetaclass, multiplicity=Multiplicity(1, 9999))
    }
)
whenClause11: BinaryAssociation = BinaryAssociation(
    name="whenClause11",
    ends={
        Property(name="OclExpression", type=genericity_dsl_ClassBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="genericity_dsl_ClassBinding12", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
conceptClass13: BinaryAssociation = BinaryAssociation(
    name="conceptClass13",
    ends={
        Property(name="ConceptMetaclass14", type=genericity_dsl_BaseFeatureBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="genericity_dsl_BaseFeatureBinding", type=ConceptMetaclass, multiplicity=Multiplicity(1, 1))
    }
)
qualifier15: BinaryAssociation = BinaryAssociation(
    name="qualifier15",
    ends={
        Property(name="ConcreteMetaclass17", type=genericity_dsl_BaseFeatureBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="genericity_dsl_BaseFeatureBinding16", type=ConcreteMetaclass, multiplicity=Multiplicity(0, 1))
    }
)
concrete18: BinaryAssociation = BinaryAssociation(
    name="concrete18",
    ends={
        Property(name="OclExpression19", type=genericity_dsl_OclFeatureBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="genericity_dsl_OclFeatureBinding", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
contextClass20: BinaryAssociation = BinaryAssociation(
    name="contextClass20",
    ends={
        Property(name="ConceptMetaclass21", type=genericity_dsl_BHelper, multiplicity=Multiplicity(1, 1)),
        Property(name="genericity_dsl_BHelper", type=ConceptMetaclass, multiplicity=Multiplicity(1, 1))
    }
)
body22: BinaryAssociation = BinaryAssociation(
    name="body22",
    ends={
        Property(name="OclExpression24", type=genericity_dsl_BHelper, multiplicity=Multiplicity(1, 1)),
        Property(name="genericity_dsl_BHelper23", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type25: BinaryAssociation = BinaryAssociation(
    name="type25",
    ends={
        Property(name="OclType", type=genericity_dsl_BHelper, multiplicity=Multiplicity(1, 1)),
        Property(name="genericity_dsl_BHelper26", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
model_27: BinaryAssociation = BinaryAssociation(
    name="model_27",
    ends={
        Property(name="29", type=genericity_dsl_BHelper, multiplicity=Multiplicity(1, 1)),
        Property(name="028", type=BindingModel, multiplicity=Multiplicity(0, 1))
    }
)
type30: BinaryAssociation = BinaryAssociation(
    name="type30",
    ends={
        Property(name="31", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="1", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifExp332: BinaryAssociation = BinaryAssociation(
    name="ifExp332",
    ends={
        Property(name="34", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="133", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
appliedProperty35: BinaryAssociation = BinaryAssociation(
    name="appliedProperty35",
    ends={
        Property(name="37", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="136", type=PropertyCallExp, multiplicity=Multiplicity(0, 1))
    }
)
collection38: BinaryAssociation = BinaryAssociation(
    name="collection38",
    ends={
        Property(name="40", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="139", type=CollectionExp, multiplicity=Multiplicity(0, 1))
    }
)
letExp41: BinaryAssociation = BinaryAssociation(
    name="letExp41",
    ends={
        Property(name="43", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="142", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
loopExp44: BinaryAssociation = BinaryAssociation(
    name="loopExp44",
    ends={
        Property(name="46", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="145", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
parentOperation47: BinaryAssociation = BinaryAssociation(
    name="parentOperation47",
    ends={
        Property(name="49", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="148", type=OperationCallExp, multiplicity=Multiplicity(0, 1))
    }
)
initializedVariable50: BinaryAssociation = BinaryAssociation(
    name="initializedVariable50",
    ends={
        Property(name="52", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="151", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
ifExp253: BinaryAssociation = BinaryAssociation(
    name="ifExp253",
    ends={
        Property(name="55", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="154", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningOperation56: BinaryAssociation = BinaryAssociation(
    name="owningOperation56",
    ends={
        Property(name="58", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="157", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable65: BinaryAssociation = BinaryAssociation(
    name="referredVariable65",
    ends={
        Property(name="67", type=OCL_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="166", type=VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
elements68: BinaryAssociation = BinaryAssociation(
    name="elements68",
    ends={
        Property(name="70", type=OCL_CollectionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="169", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuplePart71: BinaryAssociation = BinaryAssociation(
    name="tuplePart71",
    ends={
        Property(name="73", type=OCL_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="172", type=TuplePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ifExp159: BinaryAssociation = BinaryAssociation(
    name="ifExp159",
    ends={
        Property(name="61", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="160", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningAttribute62: BinaryAssociation = BinaryAssociation(
    name="owningAttribute62",
    ends={
        Property(name="64", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="163", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
elements77: BinaryAssociation = BinaryAssociation(
    name="elements77",
    ends={
        Property(name="79", type=OCL_MapExp, multiplicity=Multiplicity(1, 1)),
        Property(name="178", type=MapElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
map80: BinaryAssociation = BinaryAssociation(
    name="map80",
    ends={
        Property(name="82", type=OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="181", type=MapExp, multiplicity=Multiplicity(1, 1))
    }
)
key83: BinaryAssociation = BinaryAssociation(
    name="key83",
    ends={
        Property(name="OclExpression84", type=OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_MapElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value85: BinaryAssociation = BinaryAssociation(
    name="value85",
    ends={
        Property(name="OclExpression87", type=OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_MapElement86", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source88: BinaryAssociation = BinaryAssociation(
    name="source88",
    ends={
        Property(name="90", type=OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="189", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments91: BinaryAssociation = BinaryAssociation(
    name="arguments91",
    ends={
        Property(name="93", type=OCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="192", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body94: BinaryAssociation = BinaryAssociation(
    name="body94",
    ends={
        Property(name="96", type=OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="195", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tuple74: BinaryAssociation = BinaryAssociation(
    name="tuple74",
    ends={
        Property(name="76", type=OCL_TuplePart, multiplicity=Multiplicity(1, 1)),
        Property(name="175", type=TupleExp, multiplicity=Multiplicity(1, 1))
    }
)
result100: BinaryAssociation = BinaryAssociation(
    name="result100",
    ends={
        Property(name="102", type=OCL_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1101", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable103: BinaryAssociation = BinaryAssociation(
    name="variable103",
    ends={
        Property(name="105", type=OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1104", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in_106: BinaryAssociation = BinaryAssociation(
    name="in_106",
    ends={
        Property(name="108", type=OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1107", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression109: BinaryAssociation = BinaryAssociation(
    name="thenExpression109",
    ends={
        Property(name="111", type=OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1110", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition112: BinaryAssociation = BinaryAssociation(
    name="condition112",
    ends={
        Property(name="114", type=OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1113", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression115: BinaryAssociation = BinaryAssociation(
    name="elseExpression115",
    ends={
        Property(name="117", type=OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1116", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type118: BinaryAssociation = BinaryAssociation(
    name="type118",
    ends={
        Property(name="120", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="1119", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression121: BinaryAssociation = BinaryAssociation(
    name="initExpression121",
    ends={
        Property(name="123", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="1122", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
letExp124: BinaryAssociation = BinaryAssociation(
    name="letExp124",
    ends={
        Property(name="126", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="1125", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
iterators97: BinaryAssociation = BinaryAssociation(
    name="iterators97",
    ends={
        Property(name="99", type=OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="198", type=Iterator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
variableExp130: BinaryAssociation = BinaryAssociation(
    name="variableExp130",
    ends={
        Property(name="132", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="1131", type=VariableExp, multiplicity=Multiplicity(0, 9999))
    }
)
loopExpr133: BinaryAssociation = BinaryAssociation(
    name="loopExpr133",
    ends={
        Property(name="135", type=OCL_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="1134", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
operation136: BinaryAssociation = BinaryAssociation(
    name="operation136",
    ends={
        Property(name="138", type=OCL_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="1137", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
elementType139: BinaryAssociation = BinaryAssociation(
    name="elementType139",
    ends={
        Property(name="141", type=OCL_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="1140", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definitions142: BinaryAssociation = BinaryAssociation(
    name="definitions142",
    ends={
        Property(name="144", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1143", type=OclContextDefinition, multiplicity=Multiplicity(0, 1))
    }
)
oclExpression145: BinaryAssociation = BinaryAssociation(
    name="oclExpression145",
    ends={
        Property(name="147", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1146", type=OclExpression, multiplicity=Multiplicity(0, 1))
    }
)
operation148: BinaryAssociation = BinaryAssociation(
    name="operation148",
    ends={
        Property(name="150", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1149", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
mapType2151: BinaryAssociation = BinaryAssociation(
    name="mapType2151",
    ends={
        Property(name="153", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1152", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
attribute154: BinaryAssociation = BinaryAssociation(
    name="attribute154",
    ends={
        Property(name="156", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1155", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
mapType157: BinaryAssociation = BinaryAssociation(
    name="mapType157",
    ends={
        Property(name="159", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1158", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
collectionTypes160: BinaryAssociation = BinaryAssociation(
    name="collectionTypes160",
    ends={
        Property(name="162", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1161", type=CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
tupleTypeAttribute163: BinaryAssociation = BinaryAssociation(
    name="tupleTypeAttribute163",
    ends={
        Property(name="165", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1164", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 1))
    }
)
baseExp127: BinaryAssociation = BinaryAssociation(
    name="baseExp127",
    ends={
        Property(name="129", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="1128", type=IterateExp, multiplicity=Multiplicity(0, 1))
    }
)
attributes169: BinaryAssociation = BinaryAssociation(
    name="attributes169",
    ends={
        Property(name="171", type=OCL_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="1170", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type172: BinaryAssociation = BinaryAssociation(
    name="type172",
    ends={
        Property(name="174", type=OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="1173", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tupleType175: BinaryAssociation = BinaryAssociation(
    name="tupleType175",
    ends={
        Property(name="177", type=OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="1176", type=TupleType, multiplicity=Multiplicity(1, 1))
    }
)
model178: BinaryAssociation = BinaryAssociation(
    name="model178",
    ends={
        Property(name="180", type=OCL_OclModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="1179", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
valueType181: BinaryAssociation = BinaryAssociation(
    name="valueType181",
    ends={
        Property(name="183", type=OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="1182", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
keyType184: BinaryAssociation = BinaryAssociation(
    name="keyType184",
    ends={
        Property(name="186", type=OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="1185", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variableDeclaration166: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration166",
    ends={
        Property(name="168", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1167", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
feature187: BinaryAssociation = BinaryAssociation(
    name="feature187",
    ends={
        Property(name="1188", type=OclFeature, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="189", type=OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1))
    }
)
context_190: BinaryAssociation = BinaryAssociation(
    name="context_190",
    ends={
        Property(name="192", type=OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="1191", type=OclContextDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition193: BinaryAssociation = BinaryAssociation(
    name="definition193",
    ends={
        Property(name="195", type=OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="1194", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1))
    }
)
context_196: BinaryAssociation = BinaryAssociation(
    name="context_196",
    ends={
        Property(name="198", type=OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="1197", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definition199: BinaryAssociation = BinaryAssociation(
    name="definition199",
    ends={
        Property(name="201", type=OCL_OclFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="1200", type=OclFeatureDefinition, multiplicity=Multiplicity(0, 1))
    }
)
initExpression202: BinaryAssociation = BinaryAssociation(
    name="initExpression202",
    ends={
        Property(name="204", type=OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="1203", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type205: BinaryAssociation = BinaryAssociation(
    name="type205",
    ends={
        Property(name="207", type=OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="1206", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters208: BinaryAssociation = BinaryAssociation(
    name="parameters208",
    ends={
        Property(name="210", type=OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="1209", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType211: BinaryAssociation = BinaryAssociation(
    name="returnType211",
    ends={
        Property(name="213", type=OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="1212", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body214: BinaryAssociation = BinaryAssociation(
    name="body214",
    ends={
        Property(name="216", type=OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="1215", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elements220: BinaryAssociation = BinaryAssociation(
    name="elements220",
    ends={
        Property(name="1221", type=OclModelElement, multiplicity=Multiplicity(0, 9999)),
        Property(name="222", type=OCL_OclModel, multiplicity=Multiplicity(1, 1))
    }
)
model223: BinaryAssociation = BinaryAssociation(
    name="model223",
    ends={
        Property(name="225", type=OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="1224", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)
metamodel217: BinaryAssociation = BinaryAssociation(
    name="metamodel217",
    ends={
        Property(name="219", type=OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="1218", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_genericity_dsl_BindingModel_LocatedElement = Generalization(general=LocatedElement, specific=genericity_dsl_BindingModel)
gen_genericity_dsl_Metaclass_LocatedElement = Generalization(general=LocatedElement, specific=genericity_dsl_Metaclass)
gen_genericity_dsl_ConceptMetaclass_Metaclass = Generalization(general=Metaclass, specific=genericity_dsl_ConceptMetaclass)
gen_genericity_dsl_ConcreteMetaclass_Metaclass = Generalization(general=Metaclass, specific=genericity_dsl_ConcreteMetaclass)
gen_genericity_dsl_ClassBinding_ConceptBinding = Generalization(general=ConceptBinding, specific=genericity_dsl_ClassBinding)
gen_genericity_dsl_BaseFeatureBinding_ConceptBinding = Generalization(general=ConceptBinding, specific=genericity_dsl_BaseFeatureBinding)
gen_genericity_dsl_RenamingFeatureBinding_BaseFeatureBinding = Generalization(general=BaseFeatureBinding, specific=genericity_dsl_RenamingFeatureBinding)
gen_genericity_dsl_OclFeatureBinding_BaseFeatureBinding = Generalization(general=BaseFeatureBinding, specific=genericity_dsl_OclFeatureBinding)
gen_genericity_dsl_BHelper_LocatedElement = Generalization(general=LocatedElement, specific=genericity_dsl_BHelper)
gen_genericity_dsl_ConceptBinding_LocatedElement = Generalization(general=LocatedElement, specific=genericity_dsl_ConceptBinding)
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
gen_OCL_TuplePart_VariableDeclaration = Generalization(general=VariableDeclaration, specific=OCL_TuplePart)
gen_OCL_IterateExp_LoopExp = Generalization(general=LoopExp, specific=OCL_IterateExp)
gen_OCL_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=OCL_IteratorExp)
gen_OCL_LetExp_OclExpression = Generalization(general=OclExpression, specific=OCL_LetExp)
gen_OCL_IfExp_OclExpression = Generalization(general=OclExpression, specific=OCL_IfExp)
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
gen_OCL_OclAnyType_OclType = Generalization(general=OclType, specific=OCL_OclAnyType)
gen_OCL_TupleType_OclType = Generalization(general=OclType, specific=OCL_TupleType)
gen_OCL_TupleTypeAttribute_LocatedElement = Generalization(general=LocatedElement, specific=OCL_TupleTypeAttribute)
gen_OCL_OclModelElement_OclType = Generalization(general=OclType, specific=OCL_OclModelElement)
gen_OCL_MapType_OclType = Generalization(general=OclType, specific=OCL_MapType)
gen_OCL_OclContextDefinition_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclContextDefinition)
gen_OCL_OclFeature_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclFeature)
gen_OCL_Attribute_OclFeature = Generalization(general=OclFeature, specific=OCL_Attribute)
gen_OCL_Operation_OclFeature = Generalization(general=OclFeature, specific=OCL_Operation)
gen_OCL_OclModel_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclModel)
gen_OCL_OclFeatureDefinition_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclFeatureDefinition)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={genericity_dsl_BindingModel, LocatedElement, ConceptBinding, BHelper, VariableDeclaration, genericity_dsl_Metaclass, genericity_dsl_ConceptMetaclass, Metaclass, genericity_dsl_ConcreteMetaclass, genericity_dsl_ClassBinding, ConceptMetaclass, ConcreteMetaclass, OclExpression, genericity_dsl_BaseFeatureBinding, genericity_dsl_RenamingFeatureBinding, BaseFeatureBinding, genericity_dsl_OclFeatureBinding, genericity_dsl_BHelper, OclType, genericity_dsl_ConceptBinding, BindingModel, OCL_OclExpression, IfExp, PropertyCallExp, CollectionExp, LetExp, LoopExp, OperationCallExp, Operation, genericity_dsl_LocatedElement, OCL_VariableExp, OCL_SuperExp, OCL_PrimitiveExp, OCL_StringExp, PrimitiveExp, OCL_BooleanExp, OCL_NumericExp, OCL_RealExp, NumericExp, OCL_IntegerExp, OCL_CollectionExp, OCL_BagExp, OCL_OrderedSetExp, OCL_SequenceExp, OCL_SetExp, OCL_TupleExp, TuplePart, Attribute, OCL_MapExp, MapElement, OCL_MapElement, MapExp, OCL_EnumLiteralExp, OCL_OclUndefinedExp, OCL_PropertyCallExp, OCL_NavigationOrAttributeCallExp, OCL_OperationCallExp, OCL_OperatorCallExp, OCL_CollectionOperationCallExp, OCL_LoopExp, OCL_TuplePart, TupleExp, OCL_IterateExp, OCL_IteratorExp, OCL_LetExp, OCL_IfExp, OCL_VariableDeclaration, Iterator, OCL_Iterator, OCL_Parameter, OCL_CollectionType, OCL_OclType, OclContextDefinition, MapType, CollectionType, TupleTypeAttribute, IterateExp, VariableExp, OCL_Primitive, OCL_StringType, Primitive, OCL_BooleanType, OCL_NumericType, OCL_IntegerType, NumericType, OCL_RealType, OCL_BagType, OCL_OrderedSetType, OCL_SequenceType, OCL_SetType, OCL_OclAnyType, OCL_TupleType, OCL_TupleTypeAttribute, TupleType, OCL_OclModelElement, OclModel, OCL_MapType, OCL_OclContextDefinition, OclFeatureDefinition, OCL_OclFeature, OCL_Attribute, OCL_Operation, Parameter_, OCL_OclModel, OCL_OclFeatureDefinition, OclFeature, OclModelElement},
    associations={bindings0, helpers1, variables4, model_5, concept8, concrete9, whenClause11, conceptClass13, qualifier15, concrete18, contextClass20, body22, type25, model_27, type30, ifExp332, appliedProperty35, collection38, letExp41, loopExp44, parentOperation47, initializedVariable50, ifExp253, owningOperation56, referredVariable65, elements68, tuplePart71, ifExp159, owningAttribute62, elements77, map80, key83, value85, source88, arguments91, body94, tuple74, result100, variable103, in_106, thenExpression109, condition112, elseExpression115, type118, initExpression121, letExp124, iterators97, variableExp130, loopExpr133, operation136, elementType139, definitions142, oclExpression145, operation148, mapType2151, attribute154, mapType157, collectionTypes160, tupleTypeAttribute163, baseExp127, attributes169, type172, tupleType175, model178, valueType181, keyType184, variableDeclaration166, feature187, context_190, definition193, context_196, definition199, initExpression202, type205, parameters208, returnType211, body214, elements220, model223, metamodel217},
    generalizations={gen_genericity_dsl_BindingModel_LocatedElement, gen_genericity_dsl_Metaclass_LocatedElement, gen_genericity_dsl_ConceptMetaclass_Metaclass, gen_genericity_dsl_ConcreteMetaclass_Metaclass, gen_genericity_dsl_ClassBinding_ConceptBinding, gen_genericity_dsl_BaseFeatureBinding_ConceptBinding, gen_genericity_dsl_RenamingFeatureBinding_BaseFeatureBinding, gen_genericity_dsl_OclFeatureBinding_BaseFeatureBinding, gen_genericity_dsl_BHelper_LocatedElement, gen_genericity_dsl_ConceptBinding_LocatedElement, gen_OCL_OclExpression_LocatedElement, gen_OCL_VariableExp_OclExpression, gen_OCL_SuperExp_OclExpression, gen_OCL_PrimitiveExp_OclExpression, gen_OCL_StringExp_PrimitiveExp, gen_OCL_BooleanExp_PrimitiveExp, gen_OCL_NumericExp_PrimitiveExp, gen_OCL_RealExp_NumericExp, gen_OCL_IntegerExp_NumericExp, gen_OCL_CollectionExp_OclExpression, gen_OCL_BagExp_CollectionExp, gen_OCL_OrderedSetExp_CollectionExp, gen_OCL_SequenceExp_CollectionExp, gen_OCL_SetExp_CollectionExp, gen_OCL_TupleExp_OclExpression, gen_OCL_MapExp_OclExpression, gen_OCL_MapElement_LocatedElement, gen_OCL_EnumLiteralExp_OclExpression, gen_OCL_OclUndefinedExp_OclExpression, gen_OCL_PropertyCallExp_OclExpression, gen_OCL_NavigationOrAttributeCallExp_PropertyCallExp, gen_OCL_OperationCallExp_PropertyCallExp, gen_OCL_OperatorCallExp_OperationCallExp, gen_OCL_CollectionOperationCallExp_OperationCallExp, gen_OCL_LoopExp_PropertyCallExp, gen_OCL_TuplePart_VariableDeclaration, gen_OCL_IterateExp_LoopExp, gen_OCL_IteratorExp_LoopExp, gen_OCL_LetExp_OclExpression, gen_OCL_IfExp_OclExpression, gen_OCL_VariableDeclaration_LocatedElement, gen_OCL_Iterator_VariableDeclaration, gen_OCL_Parameter_VariableDeclaration, gen_OCL_CollectionType_OclType, gen_OCL_OclType_OclExpression, gen_OCL_Primitive_OclType, gen_OCL_StringType_Primitive, gen_OCL_BooleanType_Primitive, gen_OCL_NumericType_Primitive, gen_OCL_IntegerType_NumericType, gen_OCL_RealType_NumericType, gen_OCL_BagType_CollectionType, gen_OCL_OrderedSetType_CollectionType, gen_OCL_SequenceType_CollectionType, gen_OCL_SetType_CollectionType, gen_OCL_OclAnyType_OclType, gen_OCL_TupleType_OclType, gen_OCL_TupleTypeAttribute_LocatedElement, gen_OCL_OclModelElement_OclType, gen_OCL_MapType_OclType, gen_OCL_OclContextDefinition_LocatedElement, gen_OCL_OclFeature_LocatedElement, gen_OCL_Attribute_OclFeature, gen_OCL_Operation_OclFeature, gen_OCL_OclModel_LocatedElement, gen_OCL_OclFeatureDefinition_LocatedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)