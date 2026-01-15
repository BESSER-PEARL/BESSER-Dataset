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
simpleocl_LocatedElement = Class(name="simpleocl::LocatedElement", is_abstract=True)
simpleocl_IfExp = Class(name="simpleocl::IfExp")
simpleocl_PropertyCallExp = Class(name="simpleocl::PropertyCallExp")
simpleocl_LetExp = Class(name="simpleocl::LetExp")
simpleocl_LoopExp = Class(name="simpleocl::LoopExp", is_abstract=True)
simpleocl_OperationCall = Class(name="simpleocl::OperationCall")
simpleocl_NamedElement = Class(name="simpleocl::NamedElement", is_abstract=True)
LocatedElement = Class(name="LocatedElement")
simpleocl_Module = Class(name="simpleocl::Module")
NamedElement = Class(name="NamedElement")
simpleocl_OclMetamodel = Class(name="simpleocl::OclMetamodel")
simpleocl_Import = Class(name="simpleocl::Import")
simpleocl_ModuleElement = Class(name="simpleocl::ModuleElement", is_abstract=True)
simpleocl_OclExpression = Class(name="simpleocl::OclExpression", is_abstract=True)
simpleocl_OclType = Class(name="simpleocl::OclType")
simpleocl_BooleanExp = Class(name="simpleocl::BooleanExp")
simpleocl_NumericExp = Class(name="simpleocl::NumericExp", is_abstract=True)
simpleocl_RealExp = Class(name="simpleocl::RealExp")
NumericExp = Class(name="NumericExp")
simpleocl_IntegerExp = Class(name="simpleocl::IntegerExp")
simpleocl_CollectionExp = Class(name="simpleocl::CollectionExp", is_abstract=True)
simpleocl_LocalVariable = Class(name="simpleocl::LocalVariable")
simpleocl_Operation = Class(name="simpleocl::Operation")
simpleocl_Attribute = Class(name="simpleocl::Attribute")
simpleocl_OperatorCallExp = Class(name="simpleocl::OperatorCallExp")
simpleocl_VariableExp = Class(name="simpleocl::VariableExp")
OclExpression = Class(name="OclExpression")
simpleocl_VariableDeclaration = Class(name="simpleocl::VariableDeclaration", is_abstract=True)
simpleocl_SuperExp = Class(name="simpleocl::SuperExp")
simpleocl_SelfExp = Class(name="simpleocl::SelfExp")
simpleocl_EnvExp = Class(name="simpleocl::EnvExp")
simpleocl_PrimitiveExp = Class(name="simpleocl::PrimitiveExp", is_abstract=True)
simpleocl_StringExp = Class(name="simpleocl::StringExp")
PrimitiveExp = Class(name="PrimitiveExp")
simpleocl_CollectionPart = Class(name="simpleocl::CollectionPart", is_abstract=True)
simpleocl_CollectionRange = Class(name="simpleocl::CollectionRange")
CollectionPart = Class(name="CollectionPart")
simpleocl_EnumLiteralExp = Class(name="simpleocl::EnumLiteralExp")
simpleocl_OclUndefinedExp = Class(name="simpleocl::OclUndefinedExp")
simpleocl_CollectionItem = Class(name="simpleocl::CollectionItem")
simpleocl_BagExp = Class(name="simpleocl::BagExp")
CollectionExp = Class(name="CollectionExp")
simpleocl_OrderedSetExp = Class(name="simpleocl::OrderedSetExp")
simpleocl_SequenceExp = Class(name="simpleocl::SequenceExp")
simpleocl_SetExp = Class(name="simpleocl::SetExp")
simpleocl_TupleExp = Class(name="simpleocl::TupleExp")
simpleocl_TuplePart = Class(name="simpleocl::TuplePart")
LocalVariable = Class(name="LocalVariable")
simpleocl_MapExp = Class(name="simpleocl::MapExp")
simpleocl_MapElement = Class(name="simpleocl::MapElement")
simpleocl_NavigationOrAttributeCall = Class(name="simpleocl::NavigationOrAttributeCall")
PropertyCall = Class(name="PropertyCall")
simpleocl_StaticPropertyCallExp = Class(name="simpleocl::StaticPropertyCallExp")
simpleocl_StaticPropertyCall = Class(name="simpleocl::StaticPropertyCall", is_abstract=True)
simpleocl_StaticNavigationOrAttributeCall = Class(name="simpleocl::StaticNavigationOrAttributeCall")
StaticPropertyCall = Class(name="StaticPropertyCall")
simpleocl_StaticOperationCall = Class(name="simpleocl::StaticOperationCall")
simpleocl_PropertyCall = Class(name="simpleocl::PropertyCall", is_abstract=True)
simpleocl_AddOpCallExp = Class(name="simpleocl::AddOpCallExp")
simpleocl_IntOpCallExp = Class(name="simpleocl::IntOpCallExp")
simpleocl_MulOpCallExp = Class(name="simpleocl::MulOpCallExp")
simpleocl_LambdaCallExp = Class(name="simpleocl::LambdaCallExp")
VariableExp = Class(name="VariableExp")
simpleocl_BraceExp = Class(name="simpleocl::BraceExp")
simpleocl_NotOpCallExp = Class(name="simpleocl::NotOpCallExp")
OperatorCallExp = Class(name="OperatorCallExp")
simpleocl_RelOpCallExp = Class(name="simpleocl::RelOpCallExp")
simpleocl_EqOpCallExp = Class(name="simpleocl::EqOpCallExp")
simpleocl_CollectionOperationCall = Class(name="simpleocl::CollectionOperationCall")
OperationCall = Class(name="OperationCall")
simpleocl_Iterator = Class(name="simpleocl::Iterator")
simpleocl_IterateExp = Class(name="simpleocl::IterateExp")
LoopExp = Class(name="LoopExp")
simpleocl_IteratorExp = Class(name="simpleocl::IteratorExp")
simpleocl_CollectionType = Class(name="simpleocl::CollectionType")
OclType = Class(name="OclType")
simpleocl_OclContextDefinition = Class(name="simpleocl::OclContextDefinition")
VariableDeclaration = Class(name="VariableDeclaration")
simpleocl_Parameter = Class(name="simpleocl::Parameter")
simpleocl_OclModelElementExp = Class(name="simpleocl::OclModelElementExp")
simpleocl_OclModel = Class(name="simpleocl::OclModel", is_abstract=True)
simpleocl_Primitive = Class(name="simpleocl::Primitive", is_abstract=True)
simpleocl_StringType = Class(name="simpleocl::StringType")
Primitive = Class(name="Primitive")
simpleocl_MapType = Class(name="simpleocl::MapType")
simpleocl_TupleTypeAttribute = Class(name="simpleocl::TupleTypeAttribute")
simpleocl_LambdaType = Class(name="simpleocl::LambdaType")
simpleocl_OclModelElement = Class(name="simpleocl::OclModelElement")
simpleocl_BooleanType = Class(name="simpleocl::BooleanType")
simpleocl_NumericType = Class(name="simpleocl::NumericType", is_abstract=True)
simpleocl_IntegerType = Class(name="simpleocl::IntegerType")
NumericType = Class(name="NumericType")
simpleocl_RealType = Class(name="simpleocl::RealType")
simpleocl_BagType = Class(name="simpleocl::BagType")
CollectionType = Class(name="CollectionType")
simpleocl_OrderedSetType = Class(name="simpleocl::OrderedSetType")
simpleocl_SequenceType = Class(name="simpleocl::SequenceType")
simpleocl_SetType = Class(name="simpleocl::SetType")
simpleocl_OclAnyType = Class(name="simpleocl::OclAnyType")
simpleocl_TupleType = Class(name="simpleocl::TupleType")
OclFeature = Class(name="OclFeature")
simpleocl_EnvType = Class(name="simpleocl::EnvType")
simpleocl_OclFeatureDefinition = Class(name="simpleocl::OclFeatureDefinition")
ModuleElement = Class(name="ModuleElement")
simpleocl_OclFeature = Class(name="simpleocl::OclFeature", is_abstract=True)
OclModel = Class(name="OclModel")
simpleocl_OclInstanceModel = Class(name="simpleocl::OclInstanceModel")

# simpleocl_LocatedElement class attributes and methods
simpleocl_LocatedElement_line: Property = Property(name="line", type=StringType)
simpleocl_LocatedElement_column: Property = Property(name="column", type=StringType)
simpleocl_LocatedElement_charStart: Property = Property(name="charStart", type=StringType)
simpleocl_LocatedElement_charEnd: Property = Property(name="charEnd", type=StringType)
simpleocl_LocatedElement.attributes={simpleocl_LocatedElement_line, simpleocl_LocatedElement_charEnd, simpleocl_LocatedElement_charStart, simpleocl_LocatedElement_column}

# simpleocl_IfExp class attributes and methods

# simpleocl_PropertyCallExp class attributes and methods

# simpleocl_LetExp class attributes and methods

# simpleocl_LoopExp class attributes and methods

# simpleocl_OperationCall class attributes and methods
simpleocl_OperationCall_operationName: Property = Property(name="operationName", type=StringType)
simpleocl_OperationCall.attributes={simpleocl_OperationCall_operationName}

# simpleocl_NamedElement class attributes and methods
simpleocl_NamedElement_name: Property = Property(name="name", type=StringType)
simpleocl_NamedElement.attributes={simpleocl_NamedElement_name}

# LocatedElement class attributes and methods

# simpleocl_Module class attributes and methods

# NamedElement class attributes and methods

# simpleocl_OclMetamodel class attributes and methods
simpleocl_OclMetamodel_uri: Property = Property(name="uri", type=StringType)
simpleocl_OclMetamodel.attributes={simpleocl_OclMetamodel_uri}

# simpleocl_Import class attributes and methods

# simpleocl_ModuleElement class attributes and methods

# simpleocl_OclExpression class attributes and methods

# simpleocl_OclType class attributes and methods
simpleocl_OclType_name: Property = Property(name="name", type=StringType)
simpleocl_OclType.attributes={simpleocl_OclType_name}

# simpleocl_BooleanExp class attributes and methods
simpleocl_BooleanExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
simpleocl_BooleanExp.attributes={simpleocl_BooleanExp_booleanSymbol}

# simpleocl_NumericExp class attributes and methods

# simpleocl_RealExp class attributes and methods
simpleocl_RealExp_realSymbol: Property = Property(name="realSymbol", type=StringType)
simpleocl_RealExp.attributes={simpleocl_RealExp_realSymbol}

# NumericExp class attributes and methods

# simpleocl_IntegerExp class attributes and methods
simpleocl_IntegerExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
simpleocl_IntegerExp.attributes={simpleocl_IntegerExp_integerSymbol}

# simpleocl_CollectionExp class attributes and methods

# simpleocl_LocalVariable class attributes and methods
simpleocl_LocalVariable_eq: Property = Property(name="eq", type=StringType)
simpleocl_LocalVariable.attributes={simpleocl_LocalVariable_eq}

# simpleocl_Operation class attributes and methods

# simpleocl_Attribute class attributes and methods

# simpleocl_OperatorCallExp class attributes and methods
simpleocl_OperatorCallExp_operationName: Property = Property(name="operationName", type=StringType)
simpleocl_OperatorCallExp.attributes={simpleocl_OperatorCallExp_operationName}

# simpleocl_VariableExp class attributes and methods

# OclExpression class attributes and methods

# simpleocl_VariableDeclaration class attributes and methods
simpleocl_VariableDeclaration_varName: Property = Property(name="varName", type=StringType)
simpleocl_VariableDeclaration.attributes={simpleocl_VariableDeclaration_varName}

# simpleocl_SuperExp class attributes and methods

# simpleocl_SelfExp class attributes and methods

# simpleocl_EnvExp class attributes and methods

# simpleocl_PrimitiveExp class attributes and methods

# simpleocl_StringExp class attributes and methods
simpleocl_StringExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
simpleocl_StringExp.attributes={simpleocl_StringExp_stringSymbol}

# PrimitiveExp class attributes and methods

# simpleocl_CollectionPart class attributes and methods

# simpleocl_CollectionRange class attributes and methods

# CollectionPart class attributes and methods

# simpleocl_EnumLiteralExp class attributes and methods
simpleocl_EnumLiteralExp_name: Property = Property(name="name", type=StringType)
simpleocl_EnumLiteralExp.attributes={simpleocl_EnumLiteralExp_name}

# simpleocl_OclUndefinedExp class attributes and methods

# simpleocl_CollectionItem class attributes and methods

# simpleocl_BagExp class attributes and methods

# CollectionExp class attributes and methods

# simpleocl_OrderedSetExp class attributes and methods

# simpleocl_SequenceExp class attributes and methods

# simpleocl_SetExp class attributes and methods

# simpleocl_TupleExp class attributes and methods

# simpleocl_TuplePart class attributes and methods

# LocalVariable class attributes and methods

# simpleocl_MapExp class attributes and methods

# simpleocl_MapElement class attributes and methods

# simpleocl_NavigationOrAttributeCall class attributes and methods
simpleocl_NavigationOrAttributeCall_name: Property = Property(name="name", type=StringType)
simpleocl_NavigationOrAttributeCall.attributes={simpleocl_NavigationOrAttributeCall_name}

# PropertyCall class attributes and methods

# simpleocl_StaticPropertyCallExp class attributes and methods

# simpleocl_StaticPropertyCall class attributes and methods

# simpleocl_StaticNavigationOrAttributeCall class attributes and methods
simpleocl_StaticNavigationOrAttributeCall_name: Property = Property(name="name", type=StringType)
simpleocl_StaticNavigationOrAttributeCall.attributes={simpleocl_StaticNavigationOrAttributeCall_name}

# StaticPropertyCall class attributes and methods

# simpleocl_StaticOperationCall class attributes and methods
simpleocl_StaticOperationCall_operationName: Property = Property(name="operationName", type=StringType)
simpleocl_StaticOperationCall.attributes={simpleocl_StaticOperationCall_operationName}

# simpleocl_PropertyCall class attributes and methods

# simpleocl_AddOpCallExp class attributes and methods

# simpleocl_IntOpCallExp class attributes and methods

# simpleocl_MulOpCallExp class attributes and methods

# simpleocl_LambdaCallExp class attributes and methods

# VariableExp class attributes and methods

# simpleocl_BraceExp class attributes and methods

# simpleocl_NotOpCallExp class attributes and methods

# OperatorCallExp class attributes and methods

# simpleocl_RelOpCallExp class attributes and methods

# simpleocl_EqOpCallExp class attributes and methods

# simpleocl_CollectionOperationCall class attributes and methods

# OperationCall class attributes and methods

# simpleocl_Iterator class attributes and methods

# simpleocl_IterateExp class attributes and methods

# LoopExp class attributes and methods

# simpleocl_IteratorExp class attributes and methods
simpleocl_IteratorExp_name: Property = Property(name="name", type=StringType)
simpleocl_IteratorExp.attributes={simpleocl_IteratorExp_name}

# simpleocl_CollectionType class attributes and methods

# OclType class attributes and methods

# simpleocl_OclContextDefinition class attributes and methods

# VariableDeclaration class attributes and methods

# simpleocl_Parameter class attributes and methods

# simpleocl_OclModelElementExp class attributes and methods
simpleocl_OclModelElementExp_name: Property = Property(name="name", type=StringType)
simpleocl_OclModelElementExp.attributes={simpleocl_OclModelElementExp_name}

# simpleocl_OclModel class attributes and methods

# simpleocl_Primitive class attributes and methods

# simpleocl_StringType class attributes and methods

# Primitive class attributes and methods

# simpleocl_MapType class attributes and methods

# simpleocl_TupleTypeAttribute class attributes and methods
simpleocl_TupleTypeAttribute_name: Property = Property(name="name", type=StringType)
simpleocl_TupleTypeAttribute.attributes={simpleocl_TupleTypeAttribute_name}

# simpleocl_LambdaType class attributes and methods

# simpleocl_OclModelElement class attributes and methods

# simpleocl_BooleanType class attributes and methods

# simpleocl_NumericType class attributes and methods

# simpleocl_IntegerType class attributes and methods

# NumericType class attributes and methods

# simpleocl_RealType class attributes and methods

# simpleocl_BagType class attributes and methods

# CollectionType class attributes and methods

# simpleocl_OrderedSetType class attributes and methods

# simpleocl_SequenceType class attributes and methods

# simpleocl_SetType class attributes and methods

# simpleocl_OclAnyType class attributes and methods

# simpleocl_TupleType class attributes and methods

# OclFeature class attributes and methods

# simpleocl_EnvType class attributes and methods

# simpleocl_OclFeatureDefinition class attributes and methods
simpleocl_OclFeatureDefinition_static: Property = Property(name="static", type=StringType)
simpleocl_OclFeatureDefinition.attributes={simpleocl_OclFeatureDefinition_static}

# ModuleElement class attributes and methods

# simpleocl_OclFeature class attributes and methods
simpleocl_OclFeature_eq: Property = Property(name="eq", type=StringType)
simpleocl_OclFeature.attributes={simpleocl_OclFeature_eq}

# OclModel class attributes and methods

# simpleocl_OclInstanceModel class attributes and methods

# Relationships
ifExp38: BinaryAssociation = BinaryAssociation(
    name="ifExp38",
    ends={
        Property(name="IfExp", type=simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="elseExpression", type=simpleocl_IfExp, multiplicity=Multiplicity(0, 1))
    }
)
appliedProperty9: BinaryAssociation = BinaryAssociation(
    name="appliedProperty9",
    ends={
        Property(name="PropertyCallExp", type=simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=simpleocl_PropertyCallExp, multiplicity=Multiplicity(0, 1))
    }
)
letExp10: BinaryAssociation = BinaryAssociation(
    name="letExp10",
    ends={
        Property(name="LetExp", type=simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="in_", type=simpleocl_LetExp, multiplicity=Multiplicity(0, 1))
    }
)
loopExp11: BinaryAssociation = BinaryAssociation(
    name="loopExp11",
    ends={
        Property(name="LoopExp", type=simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="body", type=simpleocl_LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
metamodels0: BinaryAssociation = BinaryAssociation(
    name="metamodels0",
    ends={
        Property(name="simpleocl_OclMetamodel", type=simpleocl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleocl_Module", type=simpleocl_OclMetamodel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports1: BinaryAssociation = BinaryAssociation(
    name="imports1",
    ends={
        Property(name="Import", type=simpleocl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="module", type=simpleocl_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements2: BinaryAssociation = BinaryAssociation(
    name="elements2",
    ends={
        Property(name="ModuleElement", type=simpleocl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="module3", type=simpleocl_ModuleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
module4: BinaryAssociation = BinaryAssociation(
    name="module4",
    ends={
        Property(name="Module", type=simpleocl_ModuleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=simpleocl_Module, multiplicity=Multiplicity(1, 1))
    }
)
module5: BinaryAssociation = BinaryAssociation(
    name="module5",
    ends={
        Property(name="Module6", type=simpleocl_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="imports", type=simpleocl_Module, multiplicity=Multiplicity(1, 1))
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="OclType", type=simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="oclExpression", type=simpleocl_OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parentOperation12: BinaryAssociation = BinaryAssociation(
    name="parentOperation12",
    ends={
        Property(name="OperationCall", type=simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="arguments", type=simpleocl_OperationCall, multiplicity=Multiplicity(0, 1))
    }
)
initializedVariable13: BinaryAssociation = BinaryAssociation(
    name="initializedVariable13",
    ends={
        Property(name="LocalVariable", type=simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="initExpression", type=simpleocl_LocalVariable, multiplicity=Multiplicity(0, 1))
    }
)
ifExp214: BinaryAssociation = BinaryAssociation(
    name="ifExp214",
    ends={
        Property(name="IfExp15", type=simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thenExpression", type=simpleocl_IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningOperation16: BinaryAssociation = BinaryAssociation(
    name="owningOperation16",
    ends={
        Property(name="Operation", type=simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="body17", type=simpleocl_Operation, multiplicity=Multiplicity(0, 1))
    }
)
ifExp118: BinaryAssociation = BinaryAssociation(
    name="ifExp118",
    ends={
        Property(name="IfExp19", type=simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="condition", type=simpleocl_IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningAttribute20: BinaryAssociation = BinaryAssociation(
    name="owningAttribute20",
    ends={
        Property(name="Attribute", type=simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="initExpression21", type=simpleocl_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
appliedOperator22: BinaryAssociation = BinaryAssociation(
    name="appliedOperator22",
    ends={
        Property(name="OperatorCallExp", type=simpleocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="source23", type=simpleocl_OperatorCallExp, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable24: BinaryAssociation = BinaryAssociation(
    name="referredVariable24",
    ends={
        Property(name="VariableDeclaration", type=simpleocl_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="variableExp", type=simpleocl_VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
parts25: BinaryAssociation = BinaryAssociation(
    name="parts25",
    ends={
        Property(name="CollectionPart", type=simpleocl_CollectionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="collection", type=simpleocl_CollectionPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collection26: BinaryAssociation = BinaryAssociation(
    name="collection26",
    ends={
        Property(name="CollectionExp", type=simpleocl_CollectionPart, multiplicity=Multiplicity(1, 1)),
        Property(name="parts", type=simpleocl_CollectionExp, multiplicity=Multiplicity(0, 1))
    }
)
first27: BinaryAssociation = BinaryAssociation(
    name="first27",
    ends={
        Property(name="simpleocl_OclExpression", type=simpleocl_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleocl_CollectionRange", type=simpleocl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
map36: BinaryAssociation = BinaryAssociation(
    name="map36",
    ends={
        Property(name="MapExp", type=simpleocl_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements37", type=simpleocl_MapExp, multiplicity=Multiplicity(1, 1))
    }
)
key38: BinaryAssociation = BinaryAssociation(
    name="key38",
    ends={
        Property(name="simpleocl_OclExpression39", type=simpleocl_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleocl_MapElement", type=simpleocl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value40: BinaryAssociation = BinaryAssociation(
    name="value40",
    ends={
        Property(name="simpleocl_OclExpression42", type=simpleocl_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleocl_MapElement41", type=simpleocl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
last28: BinaryAssociation = BinaryAssociation(
    name="last28",
    ends={
        Property(name="simpleocl_OclExpression30", type=simpleocl_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleocl_CollectionRange29", type=simpleocl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
item31: BinaryAssociation = BinaryAssociation(
    name="item31",
    ends={
        Property(name="simpleocl_OclExpression32", type=simpleocl_CollectionItem, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleocl_CollectionItem", type=simpleocl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tuplePart33: BinaryAssociation = BinaryAssociation(
    name="tuplePart33",
    ends={
        Property(name="TuplePart", type=simpleocl_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="tuple", type=simpleocl_TuplePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuple34: BinaryAssociation = BinaryAssociation(
    name="tuple34",
    ends={
        Property(name="TupleExp", type=simpleocl_TuplePart, multiplicity=Multiplicity(1, 1)),
        Property(name="tuplePart", type=simpleocl_TupleExp, multiplicity=Multiplicity(1, 1))
    }
)
elements35: BinaryAssociation = BinaryAssociation(
    name="elements35",
    ends={
        Property(name="MapElement", type=simpleocl_MapExp, multiplicity=Multiplicity(1, 1)),
        Property(name="map", type=simpleocl_MapElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source50: BinaryAssociation = BinaryAssociation(
    name="source50",
    ends={
        Property(name="appliedProperty", type=simpleocl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="OclExpression", type=simpleocl_PropertyCallExp, multiplicity=Multiplicity(1, 1))
    }
)
callExp51: BinaryAssociation = BinaryAssociation(
    name="callExp51",
    ends={
        Property(name="PropertyCallExp52", type=simpleocl_PropertyCall, multiplicity=Multiplicity(1, 1)),
        Property(name="calls", type=simpleocl_PropertyCallExp, multiplicity=Multiplicity(1, 1))
    }
)
arguments53: BinaryAssociation = BinaryAssociation(
    name="arguments53",
    ends={
        Property(name="OclExpression54", type=simpleocl_OperationCall, multiplicity=Multiplicity(1, 1)),
        Property(name="parentOperation", type=simpleocl_OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source43: BinaryAssociation = BinaryAssociation(
    name="source43",
    ends={
        Property(name="OclType44", type=simpleocl_StaticPropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="staticPropertyCall", type=simpleocl_OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
staticCall45: BinaryAssociation = BinaryAssociation(
    name="staticCall45",
    ends={
        Property(name="StaticPropertyCall", type=simpleocl_StaticPropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="staticCallExp", type=simpleocl_StaticPropertyCall, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
staticCallExp46: BinaryAssociation = BinaryAssociation(
    name="staticCallExp46",
    ends={
        Property(name="StaticPropertyCallExp", type=simpleocl_StaticPropertyCall, multiplicity=Multiplicity(1, 1)),
        Property(name="staticCall", type=simpleocl_StaticPropertyCallExp, multiplicity=Multiplicity(1, 1))
    }
)
arguments47: BinaryAssociation = BinaryAssociation(
    name="arguments47",
    ends={
        Property(name="simpleocl_OclExpression48", type=simpleocl_StaticOperationCall, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleocl_StaticOperationCall", type=simpleocl_OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calls49: BinaryAssociation = BinaryAssociation(
    name="calls49",
    ends={
        Property(name="PropertyCall", type=simpleocl_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="callExp", type=simpleocl_PropertyCall, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
arguments59: BinaryAssociation = BinaryAssociation(
    name="arguments59",
    ends={
        Property(name="simpleocl_OclExpression60", type=simpleocl_LambdaCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleocl_LambdaCallExp", type=simpleocl_OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp61: BinaryAssociation = BinaryAssociation(
    name="exp61",
    ends={
        Property(name="simpleocl_OclExpression62", type=simpleocl_BraceExp, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleocl_BraceExp", type=simpleocl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
argument55: BinaryAssociation = BinaryAssociation(
    name="argument55",
    ends={
        Property(name="simpleocl_OclExpression56", type=simpleocl_OperatorCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleocl_OperatorCallExp", type=simpleocl_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source57: BinaryAssociation = BinaryAssociation(
    name="source57",
    ends={
        Property(name="OclExpression58", type=simpleocl_OperatorCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="appliedOperator", type=simpleocl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression73: BinaryAssociation = BinaryAssociation(
    name="thenExpression73",
    ends={
        Property(name="OclExpression74", type=simpleocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp2", type=simpleocl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition75: BinaryAssociation = BinaryAssociation(
    name="condition75",
    ends={
        Property(name="OclExpression76", type=simpleocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp1", type=simpleocl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression77: BinaryAssociation = BinaryAssociation(
    name="elseExpression77",
    ends={
        Property(name="OclExpression78", type=simpleocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp3", type=simpleocl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body63: BinaryAssociation = BinaryAssociation(
    name="body63",
    ends={
        Property(name="OclExpression64", type=simpleocl_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="loopExp", type=simpleocl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterators65: BinaryAssociation = BinaryAssociation(
    name="iterators65",
    ends={
        Property(name="Iterator", type=simpleocl_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="loopExpr", type=simpleocl_Iterator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result66: BinaryAssociation = BinaryAssociation(
    name="result66",
    ends={
        Property(name="LocalVariable67", type=simpleocl_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="baseExp", type=simpleocl_LocalVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable68: BinaryAssociation = BinaryAssociation(
    name="variable68",
    ends={
        Property(name="LocalVariable69", type=simpleocl_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="letExp", type=simpleocl_LocalVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in_70: BinaryAssociation = BinaryAssociation(
    name="in_70",
    ends={
        Property(name="OclExpression72", type=simpleocl_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="letExp71", type=simpleocl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operation89: BinaryAssociation = BinaryAssociation(
    name="operation89",
    ends={
        Property(name="Operation90", type=simpleocl_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=simpleocl_Operation, multiplicity=Multiplicity(1, 1))
    }
)
elementType91: BinaryAssociation = BinaryAssociation(
    name="elementType91",
    ends={
        Property(name="OclType92", type=simpleocl_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="collectionTypes", type=simpleocl_OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definitions93: BinaryAssociation = BinaryAssociation(
    name="definitions93",
    ends={
        Property(name="OclContextDefinition", type=simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="context_", type=simpleocl_OclContextDefinition, multiplicity=Multiplicity(0, 1))
    }
)
type79: BinaryAssociation = BinaryAssociation(
    name="type79",
    ends={
        Property(name="OclType80", type=simpleocl_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variableDeclaration", type=simpleocl_OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableExp81: BinaryAssociation = BinaryAssociation(
    name="variableExp81",
    ends={
        Property(name="VariableExp", type=simpleocl_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="referredVariable", type=simpleocl_VariableExp, multiplicity=Multiplicity(0, 9999))
    }
)
letExp82: BinaryAssociation = BinaryAssociation(
    name="letExp82",
    ends={
        Property(name="LetExp83", type=simpleocl_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=simpleocl_LetExp, multiplicity=Multiplicity(0, 1))
    }
)
initExpression84: BinaryAssociation = BinaryAssociation(
    name="initExpression84",
    ends={
        Property(name="OclExpression85", type=simpleocl_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="initializedVariable", type=simpleocl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
baseExp86: BinaryAssociation = BinaryAssociation(
    name="baseExp86",
    ends={
        Property(name="IterateExp", type=simpleocl_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="result", type=simpleocl_IterateExp, multiplicity=Multiplicity(0, 1))
    }
)
loopExpr87: BinaryAssociation = BinaryAssociation(
    name="loopExpr87",
    ends={
        Property(name="LoopExp88", type=simpleocl_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="iterators", type=simpleocl_LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
lambdaArgType112: BinaryAssociation = BinaryAssociation(
    name="lambdaArgType112",
    ends={
        Property(name="argumentTypes", type=simpleocl_LambdaType, multiplicity=Multiplicity(0, 1)),
        Property(name="LambdaType113", type=simpleocl_OclType, multiplicity=Multiplicity(1, 1))
    }
)
staticPropertyCall114: BinaryAssociation = BinaryAssociation(
    name="staticPropertyCall114",
    ends={
        Property(name="StaticPropertyCallExp116", type=simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="source115", type=simpleocl_StaticPropertyCallExp, multiplicity=Multiplicity(0, 1))
    }
)
model117: BinaryAssociation = BinaryAssociation(
    name="model117",
    ends={
        Property(name="simpleocl_OclModel", type=simpleocl_OclModelElementExp, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleocl_OclModelElementExp", type=simpleocl_OclModel, multiplicity=Multiplicity(1, 1))
    }
)
oclExpression94: BinaryAssociation = BinaryAssociation(
    name="oclExpression94",
    ends={
        Property(name="OclExpression95", type=simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=simpleocl_OclExpression, multiplicity=Multiplicity(0, 1))
    }
)
operation96: BinaryAssociation = BinaryAssociation(
    name="operation96",
    ends={
        Property(name="Operation97", type=simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="returnType", type=simpleocl_Operation, multiplicity=Multiplicity(0, 1))
    }
)
mapType298: BinaryAssociation = BinaryAssociation(
    name="mapType298",
    ends={
        Property(name="MapType", type=simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="valueType", type=simpleocl_MapType, multiplicity=Multiplicity(0, 1))
    }
)
attribute99: BinaryAssociation = BinaryAssociation(
    name="attribute99",
    ends={
        Property(name="Attribute101", type=simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type100", type=simpleocl_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
mapType102: BinaryAssociation = BinaryAssociation(
    name="mapType102",
    ends={
        Property(name="MapType103", type=simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="keyType", type=simpleocl_MapType, multiplicity=Multiplicity(0, 1))
    }
)
collectionTypes104: BinaryAssociation = BinaryAssociation(
    name="collectionTypes104",
    ends={
        Property(name="CollectionType", type=simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="elementType", type=simpleocl_CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
tupleTypeAttribute105: BinaryAssociation = BinaryAssociation(
    name="tupleTypeAttribute105",
    ends={
        Property(name="TupleTypeAttribute", type=simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type106", type=simpleocl_TupleTypeAttribute, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclaration107: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration107",
    ends={
        Property(name="VariableDeclaration109", type=simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type108", type=simpleocl_VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
lambdaReturnType110: BinaryAssociation = BinaryAssociation(
    name="lambdaReturnType110",
    ends={
        Property(name="LambdaType", type=simpleocl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="returnType111", type=simpleocl_LambdaType, multiplicity=Multiplicity(0, 1))
    }
)
tupleType122: BinaryAssociation = BinaryAssociation(
    name="tupleType122",
    ends={
        Property(name="TupleType", type=simpleocl_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=simpleocl_TupleType, multiplicity=Multiplicity(1, 1))
    }
)
model123: BinaryAssociation = BinaryAssociation(
    name="model123",
    ends={
        Property(name="OclModel", type=simpleocl_OclModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements124", type=simpleocl_OclModel, multiplicity=Multiplicity(1, 1))
    }
)
valueType125: BinaryAssociation = BinaryAssociation(
    name="valueType125",
    ends={
        Property(name="OclType126", type=simpleocl_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="mapType2", type=simpleocl_OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
keyType127: BinaryAssociation = BinaryAssociation(
    name="keyType127",
    ends={
        Property(name="OclType128", type=simpleocl_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="mapType", type=simpleocl_OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attributes118: BinaryAssociation = BinaryAssociation(
    name="attributes118",
    ends={
        Property(name="TupleTypeAttribute119", type=simpleocl_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="tupleType", type=simpleocl_TupleTypeAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type120: BinaryAssociation = BinaryAssociation(
    name="type120",
    ends={
        Property(name="OclType121", type=simpleocl_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="tupleTypeAttribute", type=simpleocl_OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definition141: BinaryAssociation = BinaryAssociation(
    name="definition141",
    ends={
        Property(name="OclFeatureDefinition142", type=simpleocl_OclFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=simpleocl_OclFeatureDefinition, multiplicity=Multiplicity(0, 1))
    }
)
initExpression143: BinaryAssociation = BinaryAssociation(
    name="initExpression143",
    ends={
        Property(name="OclExpression144", type=simpleocl_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="owningAttribute", type=simpleocl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type145: BinaryAssociation = BinaryAssociation(
    name="type145",
    ends={
        Property(name="OclType146", type=simpleocl_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attribute", type=simpleocl_OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnType129: BinaryAssociation = BinaryAssociation(
    name="returnType129",
    ends={
        Property(name="OclType130", type=simpleocl_LambdaType, multiplicity=Multiplicity(1, 1)),
        Property(name="lambdaReturnType", type=simpleocl_OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
argumentTypes131: BinaryAssociation = BinaryAssociation(
    name="argumentTypes131",
    ends={
        Property(name="OclType132", type=simpleocl_LambdaType, multiplicity=Multiplicity(1, 1)),
        Property(name="lambdaArgType", type=simpleocl_OclType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature133: BinaryAssociation = BinaryAssociation(
    name="feature133",
    ends={
        Property(name="OclFeature", type=simpleocl_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definition", type=simpleocl_OclFeature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context_134: BinaryAssociation = BinaryAssociation(
    name="context_134",
    ends={
        Property(name="OclContextDefinition136", type=simpleocl_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definition135", type=simpleocl_OclContextDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition137: BinaryAssociation = BinaryAssociation(
    name="definition137",
    ends={
        Property(name="OclFeatureDefinition", type=simpleocl_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="context_138", type=simpleocl_OclFeatureDefinition, multiplicity=Multiplicity(1, 1))
    }
)
context_139: BinaryAssociation = BinaryAssociation(
    name="context_139",
    ends={
        Property(name="OclType140", type=simpleocl_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definitions", type=simpleocl_OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters147: BinaryAssociation = BinaryAssociation(
    name="parameters147",
    ends={
        Property(name="Parameter", type=simpleocl_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation", type=simpleocl_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType148: BinaryAssociation = BinaryAssociation(
    name="returnType148",
    ends={
        Property(name="OclType150", type=simpleocl_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation149", type=simpleocl_OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body151: BinaryAssociation = BinaryAssociation(
    name="body151",
    ends={
        Property(name="OclExpression152", type=simpleocl_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="owningOperation", type=simpleocl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elements153: BinaryAssociation = BinaryAssociation(
    name="elements153",
    ends={
        Property(name="OclModelElement", type=simpleocl_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=simpleocl_OclModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
model154: BinaryAssociation = BinaryAssociation(
    name="model154",
    ends={
        Property(name="OclInstanceModel", type=simpleocl_OclMetamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel", type=simpleocl_OclInstanceModel, multiplicity=Multiplicity(0, 9999))
    }
)
metamodel155: BinaryAssociation = BinaryAssociation(
    name="metamodel155",
    ends={
        Property(name="OclMetamodel", type=simpleocl_OclInstanceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model156", type=simpleocl_OclMetamodel, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_simpleocl_NamedElement_LocatedElement = Generalization(general=LocatedElement, specific=simpleocl_NamedElement)
gen_simpleocl_Module_NamedElement = Generalization(general=NamedElement, specific=simpleocl_Module)
gen_simpleocl_ModuleElement_LocatedElement = Generalization(general=LocatedElement, specific=simpleocl_ModuleElement)
gen_simpleocl_Import_NamedElement = Generalization(general=NamedElement, specific=simpleocl_Import)
gen_simpleocl_OclExpression_LocatedElement = Generalization(general=LocatedElement, specific=simpleocl_OclExpression)
gen_simpleocl_BooleanExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=simpleocl_BooleanExp)
gen_simpleocl_NumericExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=simpleocl_NumericExp)
gen_simpleocl_RealExp_NumericExp = Generalization(general=NumericExp, specific=simpleocl_RealExp)
gen_simpleocl_IntegerExp_NumericExp = Generalization(general=NumericExp, specific=simpleocl_IntegerExp)
gen_simpleocl_CollectionExp_OclExpression = Generalization(general=OclExpression, specific=simpleocl_CollectionExp)
gen_simpleocl_VariableExp_OclExpression = Generalization(general=OclExpression, specific=simpleocl_VariableExp)
gen_simpleocl_SuperExp_OclExpression = Generalization(general=OclExpression, specific=simpleocl_SuperExp)
gen_simpleocl_SelfExp_OclExpression = Generalization(general=OclExpression, specific=simpleocl_SelfExp)
gen_simpleocl_EnvExp_OclExpression = Generalization(general=OclExpression, specific=simpleocl_EnvExp)
gen_simpleocl_PrimitiveExp_OclExpression = Generalization(general=OclExpression, specific=simpleocl_PrimitiveExp)
gen_simpleocl_StringExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=simpleocl_StringExp)
gen_simpleocl_CollectionPart_LocatedElement = Generalization(general=LocatedElement, specific=simpleocl_CollectionPart)
gen_simpleocl_CollectionRange_CollectionPart = Generalization(general=CollectionPart, specific=simpleocl_CollectionRange)
gen_simpleocl_EnumLiteralExp_OclExpression = Generalization(general=OclExpression, specific=simpleocl_EnumLiteralExp)
gen_simpleocl_OclUndefinedExp_OclExpression = Generalization(general=OclExpression, specific=simpleocl_OclUndefinedExp)
gen_simpleocl_CollectionItem_CollectionPart = Generalization(general=CollectionPart, specific=simpleocl_CollectionItem)
gen_simpleocl_BagExp_CollectionExp = Generalization(general=CollectionExp, specific=simpleocl_BagExp)
gen_simpleocl_OrderedSetExp_CollectionExp = Generalization(general=CollectionExp, specific=simpleocl_OrderedSetExp)
gen_simpleocl_SequenceExp_CollectionExp = Generalization(general=CollectionExp, specific=simpleocl_SequenceExp)
gen_simpleocl_SetExp_CollectionExp = Generalization(general=CollectionExp, specific=simpleocl_SetExp)
gen_simpleocl_TupleExp_OclExpression = Generalization(general=OclExpression, specific=simpleocl_TupleExp)
gen_simpleocl_TuplePart_LocalVariable = Generalization(general=LocalVariable, specific=simpleocl_TuplePart)
gen_simpleocl_MapExp_OclExpression = Generalization(general=OclExpression, specific=simpleocl_MapExp)
gen_simpleocl_MapElement_LocatedElement = Generalization(general=LocatedElement, specific=simpleocl_MapElement)
gen_simpleocl_PropertyCall_LocatedElement = Generalization(general=LocatedElement, specific=simpleocl_PropertyCall)
gen_simpleocl_NavigationOrAttributeCall_PropertyCall = Generalization(general=PropertyCall, specific=simpleocl_NavigationOrAttributeCall)
gen_simpleocl_OperationCall_PropertyCall = Generalization(general=PropertyCall, specific=simpleocl_OperationCall)
gen_simpleocl_StaticPropertyCallExp_OclExpression = Generalization(general=OclExpression, specific=simpleocl_StaticPropertyCallExp)
gen_simpleocl_StaticPropertyCall_LocatedElement = Generalization(general=LocatedElement, specific=simpleocl_StaticPropertyCall)
gen_simpleocl_StaticNavigationOrAttributeCall_StaticPropertyCall = Generalization(general=StaticPropertyCall, specific=simpleocl_StaticNavigationOrAttributeCall)
gen_simpleocl_StaticOperationCall_StaticPropertyCall = Generalization(general=StaticPropertyCall, specific=simpleocl_StaticOperationCall)
gen_simpleocl_PropertyCallExp_OclExpression = Generalization(general=OclExpression, specific=simpleocl_PropertyCallExp)
gen_simpleocl_AddOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=simpleocl_AddOpCallExp)
gen_simpleocl_IntOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=simpleocl_IntOpCallExp)
gen_simpleocl_MulOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=simpleocl_MulOpCallExp)
gen_simpleocl_LambdaCallExp_VariableExp = Generalization(general=VariableExp, specific=simpleocl_LambdaCallExp)
gen_simpleocl_BraceExp_OclExpression = Generalization(general=OclExpression, specific=simpleocl_BraceExp)
gen_simpleocl_OperatorCallExp_OclExpression = Generalization(general=OclExpression, specific=simpleocl_OperatorCallExp)
gen_simpleocl_NotOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=simpleocl_NotOpCallExp)
gen_simpleocl_RelOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=simpleocl_RelOpCallExp)
gen_simpleocl_EqOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=simpleocl_EqOpCallExp)
gen_simpleocl_VariableDeclaration_LocatedElement = Generalization(general=LocatedElement, specific=simpleocl_VariableDeclaration)
gen_simpleocl_CollectionOperationCall_OperationCall = Generalization(general=OperationCall, specific=simpleocl_CollectionOperationCall)
gen_simpleocl_LoopExp_PropertyCall = Generalization(general=PropertyCall, specific=simpleocl_LoopExp)
gen_simpleocl_IterateExp_LoopExp = Generalization(general=LoopExp, specific=simpleocl_IterateExp)
gen_simpleocl_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=simpleocl_IteratorExp)
gen_simpleocl_LetExp_OclExpression = Generalization(general=OclExpression, specific=simpleocl_LetExp)
gen_simpleocl_IfExp_OclExpression = Generalization(general=OclExpression, specific=simpleocl_IfExp)
gen_simpleocl_CollectionType_OclType = Generalization(general=OclType, specific=simpleocl_CollectionType)
gen_simpleocl_OclType_LocatedElement = Generalization(general=LocatedElement, specific=simpleocl_OclType)
gen_simpleocl_LocalVariable_VariableDeclaration = Generalization(general=VariableDeclaration, specific=simpleocl_LocalVariable)
gen_simpleocl_Iterator_VariableDeclaration = Generalization(general=VariableDeclaration, specific=simpleocl_Iterator)
gen_simpleocl_Parameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=simpleocl_Parameter)
gen_simpleocl_OclModelElementExp_OclExpression = Generalization(general=OclExpression, specific=simpleocl_OclModelElementExp)
gen_simpleocl_Primitive_OclType = Generalization(general=OclType, specific=simpleocl_Primitive)
gen_simpleocl_StringType_Primitive = Generalization(general=Primitive, specific=simpleocl_StringType)
gen_simpleocl_OclModelElement_OclType = Generalization(general=OclType, specific=simpleocl_OclModelElement)
gen_simpleocl_MapType_OclType = Generalization(general=OclType, specific=simpleocl_MapType)
gen_simpleocl_BooleanType_Primitive = Generalization(general=Primitive, specific=simpleocl_BooleanType)
gen_simpleocl_NumericType_Primitive = Generalization(general=Primitive, specific=simpleocl_NumericType)
gen_simpleocl_IntegerType_NumericType = Generalization(general=NumericType, specific=simpleocl_IntegerType)
gen_simpleocl_RealType_NumericType = Generalization(general=NumericType, specific=simpleocl_RealType)
gen_simpleocl_BagType_CollectionType = Generalization(general=CollectionType, specific=simpleocl_BagType)
gen_simpleocl_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=simpleocl_OrderedSetType)
gen_simpleocl_SequenceType_CollectionType = Generalization(general=CollectionType, specific=simpleocl_SequenceType)
gen_simpleocl_SetType_CollectionType = Generalization(general=CollectionType, specific=simpleocl_SetType)
gen_simpleocl_OclAnyType_OclType = Generalization(general=OclType, specific=simpleocl_OclAnyType)
gen_simpleocl_TupleType_OclType = Generalization(general=OclType, specific=simpleocl_TupleType)
gen_simpleocl_TupleTypeAttribute_LocatedElement = Generalization(general=LocatedElement, specific=simpleocl_TupleTypeAttribute)
gen_simpleocl_OclFeature_NamedElement = Generalization(general=NamedElement, specific=simpleocl_OclFeature)
gen_simpleocl_Attribute_OclFeature = Generalization(general=OclFeature, specific=simpleocl_Attribute)
gen_simpleocl_LambdaType_OclType = Generalization(general=OclType, specific=simpleocl_LambdaType)
gen_simpleocl_EnvType_OclType = Generalization(general=OclType, specific=simpleocl_EnvType)
gen_simpleocl_OclFeatureDefinition_ModuleElement = Generalization(general=ModuleElement, specific=simpleocl_OclFeatureDefinition)
gen_simpleocl_OclContextDefinition_LocatedElement = Generalization(general=LocatedElement, specific=simpleocl_OclContextDefinition)
gen_simpleocl_Operation_OclFeature = Generalization(general=OclFeature, specific=simpleocl_Operation)
gen_simpleocl_OclModel_NamedElement = Generalization(general=NamedElement, specific=simpleocl_OclModel)
gen_simpleocl_OclMetamodel_OclModel = Generalization(general=OclModel, specific=simpleocl_OclMetamodel)
gen_simpleocl_OclInstanceModel_OclModel = Generalization(general=OclModel, specific=simpleocl_OclInstanceModel)

# Domain Model
domain_model = DomainModel(
    name="simpleocl",
    types={simpleocl_LocatedElement, simpleocl_IfExp, simpleocl_PropertyCallExp, simpleocl_LetExp, simpleocl_LoopExp, simpleocl_OperationCall, simpleocl_NamedElement, LocatedElement, simpleocl_Module, NamedElement, simpleocl_OclMetamodel, simpleocl_Import, simpleocl_ModuleElement, simpleocl_OclExpression, simpleocl_OclType, simpleocl_BooleanExp, simpleocl_NumericExp, simpleocl_RealExp, NumericExp, simpleocl_IntegerExp, simpleocl_CollectionExp, simpleocl_LocalVariable, simpleocl_Operation, simpleocl_Attribute, simpleocl_OperatorCallExp, simpleocl_VariableExp, OclExpression, simpleocl_VariableDeclaration, simpleocl_SuperExp, simpleocl_SelfExp, simpleocl_EnvExp, simpleocl_PrimitiveExp, simpleocl_StringExp, PrimitiveExp, simpleocl_CollectionPart, simpleocl_CollectionRange, CollectionPart, simpleocl_EnumLiteralExp, simpleocl_OclUndefinedExp, simpleocl_CollectionItem, simpleocl_BagExp, CollectionExp, simpleocl_OrderedSetExp, simpleocl_SequenceExp, simpleocl_SetExp, simpleocl_TupleExp, simpleocl_TuplePart, LocalVariable, simpleocl_MapExp, simpleocl_MapElement, simpleocl_NavigationOrAttributeCall, PropertyCall, simpleocl_StaticPropertyCallExp, simpleocl_StaticPropertyCall, simpleocl_StaticNavigationOrAttributeCall, StaticPropertyCall, simpleocl_StaticOperationCall, simpleocl_PropertyCall, simpleocl_AddOpCallExp, simpleocl_IntOpCallExp, simpleocl_MulOpCallExp, simpleocl_LambdaCallExp, VariableExp, simpleocl_BraceExp, simpleocl_NotOpCallExp, OperatorCallExp, simpleocl_RelOpCallExp, simpleocl_EqOpCallExp, simpleocl_CollectionOperationCall, OperationCall, simpleocl_Iterator, simpleocl_IterateExp, LoopExp, simpleocl_IteratorExp, simpleocl_CollectionType, OclType, simpleocl_OclContextDefinition, VariableDeclaration, simpleocl_Parameter, simpleocl_OclModelElementExp, simpleocl_OclModel, simpleocl_Primitive, simpleocl_StringType, Primitive, simpleocl_MapType, simpleocl_TupleTypeAttribute, simpleocl_LambdaType, simpleocl_OclModelElement, simpleocl_BooleanType, simpleocl_NumericType, simpleocl_IntegerType, NumericType, simpleocl_RealType, simpleocl_BagType, CollectionType, simpleocl_OrderedSetType, simpleocl_SequenceType, simpleocl_SetType, simpleocl_OclAnyType, simpleocl_TupleType, OclFeature, simpleocl_EnvType, simpleocl_OclFeatureDefinition, ModuleElement, simpleocl_OclFeature, OclModel, simpleocl_OclInstanceModel},
    associations={ifExp38, appliedProperty9, letExp10, loopExp11, metamodels0, imports1, elements2, module4, module5, type7, parentOperation12, initializedVariable13, ifExp214, owningOperation16, ifExp118, owningAttribute20, appliedOperator22, referredVariable24, parts25, collection26, first27, map36, key38, value40, last28, item31, tuplePart33, tuple34, elements35, source50, callExp51, arguments53, source43, staticCall45, staticCallExp46, arguments47, calls49, arguments59, exp61, argument55, source57, thenExpression73, condition75, elseExpression77, body63, iterators65, result66, variable68, in_70, operation89, elementType91, definitions93, type79, variableExp81, letExp82, initExpression84, baseExp86, loopExpr87, lambdaArgType112, staticPropertyCall114, model117, oclExpression94, operation96, mapType298, attribute99, mapType102, collectionTypes104, tupleTypeAttribute105, variableDeclaration107, lambdaReturnType110, tupleType122, model123, valueType125, keyType127, attributes118, type120, definition141, initExpression143, type145, returnType129, argumentTypes131, feature133, context_134, definition137, context_139, parameters147, returnType148, body151, elements153, model154, metamodel155},
    generalizations={gen_simpleocl_NamedElement_LocatedElement, gen_simpleocl_Module_NamedElement, gen_simpleocl_ModuleElement_LocatedElement, gen_simpleocl_Import_NamedElement, gen_simpleocl_OclExpression_LocatedElement, gen_simpleocl_BooleanExp_PrimitiveExp, gen_simpleocl_NumericExp_PrimitiveExp, gen_simpleocl_RealExp_NumericExp, gen_simpleocl_IntegerExp_NumericExp, gen_simpleocl_CollectionExp_OclExpression, gen_simpleocl_VariableExp_OclExpression, gen_simpleocl_SuperExp_OclExpression, gen_simpleocl_SelfExp_OclExpression, gen_simpleocl_EnvExp_OclExpression, gen_simpleocl_PrimitiveExp_OclExpression, gen_simpleocl_StringExp_PrimitiveExp, gen_simpleocl_CollectionPart_LocatedElement, gen_simpleocl_CollectionRange_CollectionPart, gen_simpleocl_EnumLiteralExp_OclExpression, gen_simpleocl_OclUndefinedExp_OclExpression, gen_simpleocl_CollectionItem_CollectionPart, gen_simpleocl_BagExp_CollectionExp, gen_simpleocl_OrderedSetExp_CollectionExp, gen_simpleocl_SequenceExp_CollectionExp, gen_simpleocl_SetExp_CollectionExp, gen_simpleocl_TupleExp_OclExpression, gen_simpleocl_TuplePart_LocalVariable, gen_simpleocl_MapExp_OclExpression, gen_simpleocl_MapElement_LocatedElement, gen_simpleocl_PropertyCall_LocatedElement, gen_simpleocl_NavigationOrAttributeCall_PropertyCall, gen_simpleocl_OperationCall_PropertyCall, gen_simpleocl_StaticPropertyCallExp_OclExpression, gen_simpleocl_StaticPropertyCall_LocatedElement, gen_simpleocl_StaticNavigationOrAttributeCall_StaticPropertyCall, gen_simpleocl_StaticOperationCall_StaticPropertyCall, gen_simpleocl_PropertyCallExp_OclExpression, gen_simpleocl_AddOpCallExp_OperatorCallExp, gen_simpleocl_IntOpCallExp_OperatorCallExp, gen_simpleocl_MulOpCallExp_OperatorCallExp, gen_simpleocl_LambdaCallExp_VariableExp, gen_simpleocl_BraceExp_OclExpression, gen_simpleocl_OperatorCallExp_OclExpression, gen_simpleocl_NotOpCallExp_OperatorCallExp, gen_simpleocl_RelOpCallExp_OperatorCallExp, gen_simpleocl_EqOpCallExp_OperatorCallExp, gen_simpleocl_VariableDeclaration_LocatedElement, gen_simpleocl_CollectionOperationCall_OperationCall, gen_simpleocl_LoopExp_PropertyCall, gen_simpleocl_IterateExp_LoopExp, gen_simpleocl_IteratorExp_LoopExp, gen_simpleocl_LetExp_OclExpression, gen_simpleocl_IfExp_OclExpression, gen_simpleocl_CollectionType_OclType, gen_simpleocl_OclType_LocatedElement, gen_simpleocl_LocalVariable_VariableDeclaration, gen_simpleocl_Iterator_VariableDeclaration, gen_simpleocl_Parameter_VariableDeclaration, gen_simpleocl_OclModelElementExp_OclExpression, gen_simpleocl_Primitive_OclType, gen_simpleocl_StringType_Primitive, gen_simpleocl_OclModelElement_OclType, gen_simpleocl_MapType_OclType, gen_simpleocl_BooleanType_Primitive, gen_simpleocl_NumericType_Primitive, gen_simpleocl_IntegerType_NumericType, gen_simpleocl_RealType_NumericType, gen_simpleocl_BagType_CollectionType, gen_simpleocl_OrderedSetType_CollectionType, gen_simpleocl_SequenceType_CollectionType, gen_simpleocl_SetType_CollectionType, gen_simpleocl_OclAnyType_OclType, gen_simpleocl_TupleType_OclType, gen_simpleocl_TupleTypeAttribute_LocatedElement, gen_simpleocl_OclFeature_NamedElement, gen_simpleocl_Attribute_OclFeature, gen_simpleocl_LambdaType_OclType, gen_simpleocl_EnvType_OclType, gen_simpleocl_OclFeatureDefinition_ModuleElement, gen_simpleocl_OclContextDefinition_LocatedElement, gen_simpleocl_Operation_OclFeature, gen_simpleocl_OclModel_NamedElement, gen_simpleocl_OclMetamodel_OclModel, gen_simpleocl_OclInstanceModel_OclModel},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)