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
EmigOcl_LocatedElement = Class(name="EmigOcl::LocatedElement", is_abstract=True)
EmigOcl_LocalVariable = Class(name="EmigOcl::LocalVariable")
EmigOcl_Operation = Class(name="EmigOcl::Operation")
EmigOcl_Attribute = Class(name="EmigOcl::Attribute")
EmigOcl_Module = Class(name="EmigOcl::Module")
LocatedElement = Class(name="LocatedElement")
EmigOcl_OclModel = Class(name="EmigOcl::OclModel")
EmigOcl_OclFeatureDefinition = Class(name="EmigOcl::OclFeatureDefinition")
EmigOcl_OclExpression = Class(name="EmigOcl::OclExpression", is_abstract=True)
EmigOcl_OclType = Class(name="EmigOcl::OclType", is_abstract=True)
EmigOcl_IfExp = Class(name="EmigOcl::IfExp")
EmigOcl_PropertyCallExp = Class(name="EmigOcl::PropertyCallExp")
EmigOcl_CollectionExp = Class(name="EmigOcl::CollectionExp", is_abstract=True)
EmigOcl_LetExp = Class(name="EmigOcl::LetExp")
EmigOcl_LoopExp = Class(name="EmigOcl::LoopExp", is_abstract=True)
EmigOcl_OperationCall = Class(name="EmigOcl::OperationCall")
EmigOcl_OrderedSetExp = Class(name="EmigOcl::OrderedSetExp")
EmigOcl_SequenceExp = Class(name="EmigOcl::SequenceExp")
EmigOcl_SetExp = Class(name="EmigOcl::SetExp")
EmigOcl_TupleExp = Class(name="EmigOcl::TupleExp")
EmigOcl_TuplePart = Class(name="EmigOcl::TuplePart")
LocalVariable = Class(name="LocalVariable")
EmigOcl_VariableExp = Class(name="EmigOcl::VariableExp")
EmigOcl_MapExp = Class(name="EmigOcl::MapExp")
OclExpression = Class(name="OclExpression")
EmigOcl_VariableDeclaration = Class(name="EmigOcl::VariableDeclaration", is_abstract=True)
EmigOcl_SuperExp = Class(name="EmigOcl::SuperExp")
EmigOcl_SelfExp = Class(name="EmigOcl::SelfExp")
EmigOcl_PrimitiveExp = Class(name="EmigOcl::PrimitiveExp", is_abstract=True)
EmigOcl_StringExp = Class(name="EmigOcl::StringExp")
PrimitiveExp = Class(name="PrimitiveExp")
EmigOcl_BooleanExp = Class(name="EmigOcl::BooleanExp")
EmigOcl_NumericExp = Class(name="EmigOcl::NumericExp", is_abstract=True)
EmigOcl_RealExp = Class(name="EmigOcl::RealExp")
NumericExp = Class(name="NumericExp")
EmigOcl_IntegerExp = Class(name="EmigOcl::IntegerExp")
EmigOcl_BagExp = Class(name="EmigOcl::BagExp")
CollectionExp = Class(name="CollectionExp")
EmigOcl_StaticOperationCall = Class(name="EmigOcl::StaticOperationCall")
EmigOcl_PropertyCall = Class(name="EmigOcl::PropertyCall", is_abstract=True)
EmigOcl_NavigationOrAttributeCall = Class(name="EmigOcl::NavigationOrAttributeCall")
PropertyCall = Class(name="PropertyCall")
EmigOcl_MapElement = Class(name="EmigOcl::MapElement")
EmigOcl_EnumLiteralExp = Class(name="EmigOcl::EnumLiteralExp")
EmigOcl_OclUndefinedExp = Class(name="EmigOcl::OclUndefinedExp")
EmigOcl_StaticPropertyCallExp = Class(name="EmigOcl::StaticPropertyCallExp")
EmigOcl_StaticPropertyCall = Class(name="EmigOcl::StaticPropertyCall", is_abstract=True)
EmigOcl_StaticNavigationOrAttributeCall = Class(name="EmigOcl::StaticNavigationOrAttributeCall")
StaticPropertyCall = Class(name="StaticPropertyCall")
EmigOcl_CollectionOperationCall = Class(name="EmigOcl::CollectionOperationCall")
OperationCall = Class(name="OperationCall")
EmigOcl_Iterator = Class(name="EmigOcl::Iterator")
EmigOcl_OperatorCallExp = Class(name="EmigOcl::OperatorCallExp")
PropertyCallExp = Class(name="PropertyCallExp")
EmigOcl_NotOpCallExp = Class(name="EmigOcl::NotOpCallExp")
OperatorCallExp = Class(name="OperatorCallExp")
EmigOcl_RelOpCallExp = Class(name="EmigOcl::RelOpCallExp")
EmigOcl_EqOpCallExp = Class(name="EmigOcl::EqOpCallExp")
EmigOcl_AddOpCallExp = Class(name="EmigOcl::AddOpCallExp")
EmigOcl_IntOpCallExp = Class(name="EmigOcl::IntOpCallExp")
EmigOcl_MulOpCallExp = Class(name="EmigOcl::MulOpCallExp")
EmigOcl_LambdaCallExp = Class(name="EmigOcl::LambdaCallExp")
VariableExp = Class(name="VariableExp")
EmigOcl_BraceExp = Class(name="EmigOcl::BraceExp")
VariableDeclaration = Class(name="VariableDeclaration")
EmigOcl_IterateExp = Class(name="EmigOcl::IterateExp")
LoopExp = Class(name="LoopExp")
EmigOcl_IteratorExp = Class(name="EmigOcl::IteratorExp")
EmigOcl_MapType = Class(name="EmigOcl::MapType")
EmigOcl_Parameter = Class(name="EmigOcl::Parameter")
EmigOcl_CollectionType = Class(name="EmigOcl::CollectionType")
OclType = Class(name="OclType")
EmigOcl_OclContextDefinition = Class(name="EmigOcl::OclContextDefinition")
EmigOcl_SequenceType = Class(name="EmigOcl::SequenceType")
EmigOcl_SetType = Class(name="EmigOcl::SetType")
EmigOcl_OclAnyType = Class(name="EmigOcl::OclAnyType")
EmigOcl_TupleType = Class(name="EmigOcl::TupleType")
EmigOcl_TupleTypeAttribute = Class(name="EmigOcl::TupleTypeAttribute")
EmigOcl_OclModelElementExp = Class(name="EmigOcl::OclModelElementExp")
EmigOcl_Primitive = Class(name="EmigOcl::Primitive", is_abstract=True)
EmigOcl_StringType = Class(name="EmigOcl::StringType")
Primitive = Class(name="Primitive")
EmigOcl_BooleanType = Class(name="EmigOcl::BooleanType")
EmigOcl_NumericType = Class(name="EmigOcl::NumericType", is_abstract=True)
EmigOcl_IntegerType = Class(name="EmigOcl::IntegerType")
NumericType = Class(name="NumericType")
EmigOcl_RealType = Class(name="EmigOcl::RealType")
EmigOcl_BagType = Class(name="EmigOcl::BagType")
CollectionType = Class(name="CollectionType")
EmigOcl_OrderedSetType = Class(name="EmigOcl::OrderedSetType")
EmigOcl_OclModelElement = Class(name="EmigOcl::OclModelElement")
EmigOcl_LambdaType = Class(name="EmigOcl::LambdaType")
EmigOcl_OclFeature = Class(name="EmigOcl::OclFeature", is_abstract=True)
OclFeature = Class(name="OclFeature")

# EmigOcl_LocatedElement class attributes and methods
EmigOcl_LocatedElement_line: Property = Property(name="line", type=StringType)
EmigOcl_LocatedElement_column: Property = Property(name="column", type=StringType)
EmigOcl_LocatedElement_charStart: Property = Property(name="charStart", type=StringType)
EmigOcl_LocatedElement_charEnd: Property = Property(name="charEnd", type=StringType)
EmigOcl_LocatedElement.attributes={EmigOcl_LocatedElement_line, EmigOcl_LocatedElement_charStart, EmigOcl_LocatedElement_column, EmigOcl_LocatedElement_charEnd}

# EmigOcl_LocalVariable class attributes and methods
EmigOcl_LocalVariable_eq: Property = Property(name="eq", type=StringType)
EmigOcl_LocalVariable.attributes={EmigOcl_LocalVariable_eq}

# EmigOcl_Operation class attributes and methods
EmigOcl_Operation_name: Property = Property(name="name", type=StringType)
EmigOcl_Operation.attributes={EmigOcl_Operation_name}

# EmigOcl_Attribute class attributes and methods
EmigOcl_Attribute_name: Property = Property(name="name", type=StringType)
EmigOcl_Attribute.attributes={EmigOcl_Attribute_name}

# EmigOcl_Module class attributes and methods
EmigOcl_Module_name: Property = Property(name="name", type=StringType)
EmigOcl_Module.attributes={EmigOcl_Module_name}

# LocatedElement class attributes and methods

# EmigOcl_OclModel class attributes and methods
EmigOcl_OclModel_name: Property = Property(name="name", type=StringType)
EmigOcl_OclModel.attributes={EmigOcl_OclModel_name}

# EmigOcl_OclFeatureDefinition class attributes and methods
EmigOcl_OclFeatureDefinition_static: Property = Property(name="static", type=StringType)
EmigOcl_OclFeatureDefinition.attributes={EmigOcl_OclFeatureDefinition_static}

# EmigOcl_OclExpression class attributes and methods

# EmigOcl_OclType class attributes and methods
EmigOcl_OclType_name: Property = Property(name="name", type=StringType)
EmigOcl_OclType.attributes={EmigOcl_OclType_name}

# EmigOcl_IfExp class attributes and methods

# EmigOcl_PropertyCallExp class attributes and methods

# EmigOcl_CollectionExp class attributes and methods

# EmigOcl_LetExp class attributes and methods

# EmigOcl_LoopExp class attributes and methods

# EmigOcl_OperationCall class attributes and methods
EmigOcl_OperationCall_operationName: Property = Property(name="operationName", type=StringType)
EmigOcl_OperationCall.attributes={EmigOcl_OperationCall_operationName}

# EmigOcl_OrderedSetExp class attributes and methods

# EmigOcl_SequenceExp class attributes and methods

# EmigOcl_SetExp class attributes and methods

# EmigOcl_TupleExp class attributes and methods

# EmigOcl_TuplePart class attributes and methods

# LocalVariable class attributes and methods

# EmigOcl_VariableExp class attributes and methods

# EmigOcl_MapExp class attributes and methods

# OclExpression class attributes and methods

# EmigOcl_VariableDeclaration class attributes and methods
EmigOcl_VariableDeclaration_varName: Property = Property(name="varName", type=StringType)
EmigOcl_VariableDeclaration.attributes={EmigOcl_VariableDeclaration_varName}

# EmigOcl_SuperExp class attributes and methods

# EmigOcl_SelfExp class attributes and methods

# EmigOcl_PrimitiveExp class attributes and methods

# EmigOcl_StringExp class attributes and methods
EmigOcl_StringExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
EmigOcl_StringExp.attributes={EmigOcl_StringExp_stringSymbol}

# PrimitiveExp class attributes and methods

# EmigOcl_BooleanExp class attributes and methods
EmigOcl_BooleanExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
EmigOcl_BooleanExp.attributes={EmigOcl_BooleanExp_booleanSymbol}

# EmigOcl_NumericExp class attributes and methods

# EmigOcl_RealExp class attributes and methods
EmigOcl_RealExp_realSymbol: Property = Property(name="realSymbol", type=StringType)
EmigOcl_RealExp.attributes={EmigOcl_RealExp_realSymbol}

# NumericExp class attributes and methods

# EmigOcl_IntegerExp class attributes and methods
EmigOcl_IntegerExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
EmigOcl_IntegerExp.attributes={EmigOcl_IntegerExp_integerSymbol}

# EmigOcl_BagExp class attributes and methods

# CollectionExp class attributes and methods

# EmigOcl_StaticOperationCall class attributes and methods
EmigOcl_StaticOperationCall_operationName: Property = Property(name="operationName", type=StringType)
EmigOcl_StaticOperationCall.attributes={EmigOcl_StaticOperationCall_operationName}

# EmigOcl_PropertyCall class attributes and methods

# EmigOcl_NavigationOrAttributeCall class attributes and methods
EmigOcl_NavigationOrAttributeCall_name: Property = Property(name="name", type=StringType)
EmigOcl_NavigationOrAttributeCall.attributes={EmigOcl_NavigationOrAttributeCall_name}

# PropertyCall class attributes and methods

# EmigOcl_MapElement class attributes and methods

# EmigOcl_EnumLiteralExp class attributes and methods
EmigOcl_EnumLiteralExp_name: Property = Property(name="name", type=StringType)
EmigOcl_EnumLiteralExp.attributes={EmigOcl_EnumLiteralExp_name}

# EmigOcl_OclUndefinedExp class attributes and methods

# EmigOcl_StaticPropertyCallExp class attributes and methods

# EmigOcl_StaticPropertyCall class attributes and methods

# EmigOcl_StaticNavigationOrAttributeCall class attributes and methods
EmigOcl_StaticNavigationOrAttributeCall_name: Property = Property(name="name", type=StringType)
EmigOcl_StaticNavigationOrAttributeCall.attributes={EmigOcl_StaticNavigationOrAttributeCall_name}

# StaticPropertyCall class attributes and methods

# EmigOcl_CollectionOperationCall class attributes and methods

# OperationCall class attributes and methods

# EmigOcl_Iterator class attributes and methods

# EmigOcl_OperatorCallExp class attributes and methods
EmigOcl_OperatorCallExp_operationName: Property = Property(name="operationName", type=StringType)
EmigOcl_OperatorCallExp.attributes={EmigOcl_OperatorCallExp_operationName}

# PropertyCallExp class attributes and methods

# EmigOcl_NotOpCallExp class attributes and methods

# OperatorCallExp class attributes and methods

# EmigOcl_RelOpCallExp class attributes and methods

# EmigOcl_EqOpCallExp class attributes and methods

# EmigOcl_AddOpCallExp class attributes and methods

# EmigOcl_IntOpCallExp class attributes and methods

# EmigOcl_MulOpCallExp class attributes and methods

# EmigOcl_LambdaCallExp class attributes and methods

# VariableExp class attributes and methods

# EmigOcl_BraceExp class attributes and methods

# VariableDeclaration class attributes and methods

# EmigOcl_IterateExp class attributes and methods

# LoopExp class attributes and methods

# EmigOcl_IteratorExp class attributes and methods
EmigOcl_IteratorExp_name: Property = Property(name="name", type=StringType)
EmigOcl_IteratorExp.attributes={EmigOcl_IteratorExp_name}

# EmigOcl_MapType class attributes and methods

# EmigOcl_Parameter class attributes and methods

# EmigOcl_CollectionType class attributes and methods

# OclType class attributes and methods

# EmigOcl_OclContextDefinition class attributes and methods

# EmigOcl_SequenceType class attributes and methods

# EmigOcl_SetType class attributes and methods

# EmigOcl_OclAnyType class attributes and methods

# EmigOcl_TupleType class attributes and methods

# EmigOcl_TupleTypeAttribute class attributes and methods
EmigOcl_TupleTypeAttribute_name: Property = Property(name="name", type=StringType)
EmigOcl_TupleTypeAttribute.attributes={EmigOcl_TupleTypeAttribute_name}

# EmigOcl_OclModelElementExp class attributes and methods
EmigOcl_OclModelElementExp_name: Property = Property(name="name", type=StringType)
EmigOcl_OclModelElementExp.attributes={EmigOcl_OclModelElementExp_name}

# EmigOcl_Primitive class attributes and methods

# EmigOcl_StringType class attributes and methods

# Primitive class attributes and methods

# EmigOcl_BooleanType class attributes and methods

# EmigOcl_NumericType class attributes and methods

# EmigOcl_IntegerType class attributes and methods

# NumericType class attributes and methods

# EmigOcl_RealType class attributes and methods

# EmigOcl_BagType class attributes and methods

# CollectionType class attributes and methods

# EmigOcl_OrderedSetType class attributes and methods

# EmigOcl_OclModelElement class attributes and methods

# EmigOcl_LambdaType class attributes and methods

# EmigOcl_OclFeature class attributes and methods
EmigOcl_OclFeature_eq: Property = Property(name="eq", type=StringType)
EmigOcl_OclFeature.attributes={EmigOcl_OclFeature_eq}

# OclFeature class attributes and methods

# Relationships
parentOperation9: BinaryAssociation = BinaryAssociation(
    name="parentOperation9",
    ends={
        Property(name="arguments", type=EmigOcl_OperationCall, multiplicity=Multiplicity(0, 1)),
        Property(name="OperationCall", type=EmigOcl_OclExpression, multiplicity=Multiplicity(1, 1))
    }
)
initializedVariable10: BinaryAssociation = BinaryAssociation(
    name="initializedVariable10",
    ends={
        Property(name="LocalVariable", type=EmigOcl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="initExpression", type=EmigOcl_LocalVariable, multiplicity=Multiplicity(0, 1))
    }
)
ifExp211: BinaryAssociation = BinaryAssociation(
    name="ifExp211",
    ends={
        Property(name="IfExp12", type=EmigOcl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thenExpression", type=EmigOcl_IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningOperation13: BinaryAssociation = BinaryAssociation(
    name="owningOperation13",
    ends={
        Property(name="Operation", type=EmigOcl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="body14", type=EmigOcl_Operation, multiplicity=Multiplicity(0, 1))
    }
)
ifExp115: BinaryAssociation = BinaryAssociation(
    name="ifExp115",
    ends={
        Property(name="IfExp16", type=EmigOcl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="condition", type=EmigOcl_IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningAttribute17: BinaryAssociation = BinaryAssociation(
    name="owningAttribute17",
    ends={
        Property(name="Attribute", type=EmigOcl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="initExpression18", type=EmigOcl_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
models0: BinaryAssociation = BinaryAssociation(
    name="models0",
    ends={
        Property(name="EmigOcl_OclModel", type=EmigOcl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="EmigOcl_Module", type=EmigOcl_OclModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features1: BinaryAssociation = BinaryAssociation(
    name="features1",
    ends={
        Property(name="EmigOcl_OclFeatureDefinition", type=EmigOcl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="EmigOcl_Module2", type=EmigOcl_OclFeatureDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type3: BinaryAssociation = BinaryAssociation(
    name="type3",
    ends={
        Property(name="OclType", type=EmigOcl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="oclExpression", type=EmigOcl_OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifExp34: BinaryAssociation = BinaryAssociation(
    name="ifExp34",
    ends={
        Property(name="IfExp", type=EmigOcl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="elseExpression", type=EmigOcl_IfExp, multiplicity=Multiplicity(0, 1))
    }
)
appliedProperty5: BinaryAssociation = BinaryAssociation(
    name="appliedProperty5",
    ends={
        Property(name="PropertyCallExp", type=EmigOcl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=EmigOcl_PropertyCallExp, multiplicity=Multiplicity(0, 1))
    }
)
collection6: BinaryAssociation = BinaryAssociation(
    name="collection6",
    ends={
        Property(name="CollectionExp", type=EmigOcl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=EmigOcl_CollectionExp, multiplicity=Multiplicity(0, 1))
    }
)
letExp7: BinaryAssociation = BinaryAssociation(
    name="letExp7",
    ends={
        Property(name="LetExp", type=EmigOcl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="in_", type=EmigOcl_LetExp, multiplicity=Multiplicity(0, 1))
    }
)
loopExp8: BinaryAssociation = BinaryAssociation(
    name="loopExp8",
    ends={
        Property(name="LoopExp", type=EmigOcl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="body", type=EmigOcl_LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
tuplePart21: BinaryAssociation = BinaryAssociation(
    name="tuplePart21",
    ends={
        Property(name="TuplePart", type=EmigOcl_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="tuple", type=EmigOcl_TuplePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuple22: BinaryAssociation = BinaryAssociation(
    name="tuple22",
    ends={
        Property(name="TupleExp", type=EmigOcl_TuplePart, multiplicity=Multiplicity(1, 1)),
        Property(name="tuplePart", type=EmigOcl_TupleExp, multiplicity=Multiplicity(1, 1))
    }
)
referredVariable19: BinaryAssociation = BinaryAssociation(
    name="referredVariable19",
    ends={
        Property(name="VariableDeclaration", type=EmigOcl_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="variableExp", type=EmigOcl_VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
elements20: BinaryAssociation = BinaryAssociation(
    name="elements20",
    ends={
        Property(name="OclExpression", type=EmigOcl_CollectionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="collection", type=EmigOcl_OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arguments33: BinaryAssociation = BinaryAssociation(
    name="arguments33",
    ends={
        Property(name="EmigOcl_OclExpression34", type=EmigOcl_StaticOperationCall, multiplicity=Multiplicity(1, 1)),
        Property(name="EmigOcl_StaticOperationCall", type=EmigOcl_OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calls35: BinaryAssociation = BinaryAssociation(
    name="calls35",
    ends={
        Property(name="EmigOcl_PropertyCall", type=EmigOcl_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EmigOcl_PropertyCallExp", type=EmigOcl_PropertyCall, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
source36: BinaryAssociation = BinaryAssociation(
    name="source36",
    ends={
        Property(name="OclExpression37", type=EmigOcl_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="appliedProperty", type=EmigOcl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elements23: BinaryAssociation = BinaryAssociation(
    name="elements23",
    ends={
        Property(name="MapElement", type=EmigOcl_MapExp, multiplicity=Multiplicity(1, 1)),
        Property(name="map", type=EmigOcl_MapElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
map24: BinaryAssociation = BinaryAssociation(
    name="map24",
    ends={
        Property(name="MapExp", type=EmigOcl_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements25", type=EmigOcl_MapExp, multiplicity=Multiplicity(1, 1))
    }
)
key26: BinaryAssociation = BinaryAssociation(
    name="key26",
    ends={
        Property(name="EmigOcl_OclExpression", type=EmigOcl_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="EmigOcl_MapElement", type=EmigOcl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value27: BinaryAssociation = BinaryAssociation(
    name="value27",
    ends={
        Property(name="EmigOcl_OclExpression29", type=EmigOcl_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="EmigOcl_MapElement28", type=EmigOcl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source30: BinaryAssociation = BinaryAssociation(
    name="source30",
    ends={
        Property(name="EmigOcl_OclType", type=EmigOcl_StaticPropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EmigOcl_StaticPropertyCallExp", type=EmigOcl_OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
staticCall31: BinaryAssociation = BinaryAssociation(
    name="staticCall31",
    ends={
        Property(name="EmigOcl_StaticPropertyCall", type=EmigOcl_StaticPropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EmigOcl_StaticPropertyCallExp32", type=EmigOcl_StaticPropertyCall, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exp44: BinaryAssociation = BinaryAssociation(
    name="exp44",
    ends={
        Property(name="EmigOcl_OclExpression45", type=EmigOcl_BraceExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EmigOcl_BraceExp", type=EmigOcl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body46: BinaryAssociation = BinaryAssociation(
    name="body46",
    ends={
        Property(name="OclExpression47", type=EmigOcl_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="loopExp", type=EmigOcl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterators48: BinaryAssociation = BinaryAssociation(
    name="iterators48",
    ends={
        Property(name="Iterator", type=EmigOcl_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="loopExpr", type=EmigOcl_Iterator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
arguments38: BinaryAssociation = BinaryAssociation(
    name="arguments38",
    ends={
        Property(name="OclExpression39", type=EmigOcl_OperationCall, multiplicity=Multiplicity(1, 1)),
        Property(name="parentOperation", type=EmigOcl_OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument40: BinaryAssociation = BinaryAssociation(
    name="argument40",
    ends={
        Property(name="EmigOcl_OclExpression41", type=EmigOcl_OperatorCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EmigOcl_OperatorCallExp", type=EmigOcl_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type62: BinaryAssociation = BinaryAssociation(
    name="type62",
    ends={
        Property(name="OclType63", type=EmigOcl_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variableDeclaration", type=EmigOcl_OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments42: BinaryAssociation = BinaryAssociation(
    name="arguments42",
    ends={
        Property(name="EmigOcl_OclExpression43", type=EmigOcl_LambdaCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EmigOcl_LambdaCallExp", type=EmigOcl_OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variableExp64: BinaryAssociation = BinaryAssociation(
    name="variableExp64",
    ends={
        Property(name="VariableExp", type=EmigOcl_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="referredVariable", type=EmigOcl_VariableExp, multiplicity=Multiplicity(0, 9999))
    }
)
letExp65: BinaryAssociation = BinaryAssociation(
    name="letExp65",
    ends={
        Property(name="LetExp66", type=EmigOcl_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=EmigOcl_LetExp, multiplicity=Multiplicity(0, 1))
    }
)
initExpression67: BinaryAssociation = BinaryAssociation(
    name="initExpression67",
    ends={
        Property(name="OclExpression68", type=EmigOcl_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="initializedVariable", type=EmigOcl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
baseExp69: BinaryAssociation = BinaryAssociation(
    name="baseExp69",
    ends={
        Property(name="IterateExp", type=EmigOcl_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="result", type=EmigOcl_IterateExp, multiplicity=Multiplicity(0, 1))
    }
)
result49: BinaryAssociation = BinaryAssociation(
    name="result49",
    ends={
        Property(name="LocalVariable50", type=EmigOcl_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="baseExp", type=EmigOcl_LocalVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable51: BinaryAssociation = BinaryAssociation(
    name="variable51",
    ends={
        Property(name="LocalVariable52", type=EmigOcl_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="letExp", type=EmigOcl_LocalVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in_53: BinaryAssociation = BinaryAssociation(
    name="in_53",
    ends={
        Property(name="OclExpression55", type=EmigOcl_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="letExp54", type=EmigOcl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression56: BinaryAssociation = BinaryAssociation(
    name="thenExpression56",
    ends={
        Property(name="OclExpression57", type=EmigOcl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp2", type=EmigOcl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition58: BinaryAssociation = BinaryAssociation(
    name="condition58",
    ends={
        Property(name="OclExpression59", type=EmigOcl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp1", type=EmigOcl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression60: BinaryAssociation = BinaryAssociation(
    name="elseExpression60",
    ends={
        Property(name="OclExpression61", type=EmigOcl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp3", type=EmigOcl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
oclExpression77: BinaryAssociation = BinaryAssociation(
    name="oclExpression77",
    ends={
        Property(name="OclExpression78", type=EmigOcl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=EmigOcl_OclExpression, multiplicity=Multiplicity(0, 1))
    }
)
operation79: BinaryAssociation = BinaryAssociation(
    name="operation79",
    ends={
        Property(name="Operation80", type=EmigOcl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="returnType", type=EmigOcl_Operation, multiplicity=Multiplicity(0, 1))
    }
)
mapType281: BinaryAssociation = BinaryAssociation(
    name="mapType281",
    ends={
        Property(name="MapType", type=EmigOcl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="valueType", type=EmigOcl_MapType, multiplicity=Multiplicity(0, 1))
    }
)
attribute82: BinaryAssociation = BinaryAssociation(
    name="attribute82",
    ends={
        Property(name="Attribute84", type=EmigOcl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type83", type=EmigOcl_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
loopExpr70: BinaryAssociation = BinaryAssociation(
    name="loopExpr70",
    ends={
        Property(name="LoopExp71", type=EmigOcl_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="iterators", type=EmigOcl_LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
operation72: BinaryAssociation = BinaryAssociation(
    name="operation72",
    ends={
        Property(name="Operation73", type=EmigOcl_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=EmigOcl_Operation, multiplicity=Multiplicity(1, 1))
    }
)
elementType74: BinaryAssociation = BinaryAssociation(
    name="elementType74",
    ends={
        Property(name="OclType75", type=EmigOcl_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="collectionTypes", type=EmigOcl_OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definitions76: BinaryAssociation = BinaryAssociation(
    name="definitions76",
    ends={
        Property(name="OclContextDefinition", type=EmigOcl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="context_", type=EmigOcl_OclContextDefinition, multiplicity=Multiplicity(0, 1))
    }
)
attributes95: BinaryAssociation = BinaryAssociation(
    name="attributes95",
    ends={
        Property(name="TupleTypeAttribute96", type=EmigOcl_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="tupleType", type=EmigOcl_TupleTypeAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type97: BinaryAssociation = BinaryAssociation(
    name="type97",
    ends={
        Property(name="OclType98", type=EmigOcl_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="tupleTypeAttribute", type=EmigOcl_OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tupleType99: BinaryAssociation = BinaryAssociation(
    name="tupleType99",
    ends={
        Property(name="TupleType", type=EmigOcl_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=EmigOcl_TupleType, multiplicity=Multiplicity(1, 1))
    }
)
mapType85: BinaryAssociation = BinaryAssociation(
    name="mapType85",
    ends={
        Property(name="MapType86", type=EmigOcl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="keyType", type=EmigOcl_MapType, multiplicity=Multiplicity(0, 1))
    }
)
collectionTypes87: BinaryAssociation = BinaryAssociation(
    name="collectionTypes87",
    ends={
        Property(name="CollectionType", type=EmigOcl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="elementType", type=EmigOcl_CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
tupleTypeAttribute88: BinaryAssociation = BinaryAssociation(
    name="tupleTypeAttribute88",
    ends={
        Property(name="TupleTypeAttribute", type=EmigOcl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type89", type=EmigOcl_TupleTypeAttribute, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclaration90: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration90",
    ends={
        Property(name="VariableDeclaration92", type=EmigOcl_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type91", type=EmigOcl_VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
model93: BinaryAssociation = BinaryAssociation(
    name="model93",
    ends={
        Property(name="EmigOcl_OclModel94", type=EmigOcl_OclModelElementExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EmigOcl_OclModelElementExp", type=EmigOcl_OclModel, multiplicity=Multiplicity(1, 1))
    }
)
context_112: BinaryAssociation = BinaryAssociation(
    name="context_112",
    ends={
        Property(name="definition113", type=EmigOcl_OclContextDefinition, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="OclContextDefinition114", type=EmigOcl_OclFeatureDefinition, multiplicity=Multiplicity(1, 1))
    }
)
definition115: BinaryAssociation = BinaryAssociation(
    name="definition115",
    ends={
        Property(name="OclFeatureDefinition", type=EmigOcl_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="context_116", type=EmigOcl_OclFeatureDefinition, multiplicity=Multiplicity(1, 1))
    }
)
context_117: BinaryAssociation = BinaryAssociation(
    name="context_117",
    ends={
        Property(name="OclType118", type=EmigOcl_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definitions", type=EmigOcl_OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definition119: BinaryAssociation = BinaryAssociation(
    name="definition119",
    ends={
        Property(name="OclFeatureDefinition120", type=EmigOcl_OclFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=EmigOcl_OclFeatureDefinition, multiplicity=Multiplicity(0, 1))
    }
)
model100: BinaryAssociation = BinaryAssociation(
    name="model100",
    ends={
        Property(name="OclModel", type=EmigOcl_OclModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements101", type=EmigOcl_OclModel, multiplicity=Multiplicity(1, 1))
    }
)
valueType102: BinaryAssociation = BinaryAssociation(
    name="valueType102",
    ends={
        Property(name="OclType103", type=EmigOcl_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="mapType2", type=EmigOcl_OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
keyType104: BinaryAssociation = BinaryAssociation(
    name="keyType104",
    ends={
        Property(name="OclType105", type=EmigOcl_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="mapType", type=EmigOcl_OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnType106: BinaryAssociation = BinaryAssociation(
    name="returnType106",
    ends={
        Property(name="EmigOcl_OclType107", type=EmigOcl_LambdaType, multiplicity=Multiplicity(1, 1)),
        Property(name="EmigOcl_LambdaType", type=EmigOcl_OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
argumentTypes108: BinaryAssociation = BinaryAssociation(
    name="argumentTypes108",
    ends={
        Property(name="EmigOcl_OclType110", type=EmigOcl_LambdaType, multiplicity=Multiplicity(1, 1)),
        Property(name="EmigOcl_LambdaType109", type=EmigOcl_OclType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature111: BinaryAssociation = BinaryAssociation(
    name="feature111",
    ends={
        Property(name="OclFeature", type=EmigOcl_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definition", type=EmigOcl_OclFeature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metamodel132: BinaryAssociation = BinaryAssociation(
    name="metamodel132",
    ends={
        Property(name="OclModel133", type=EmigOcl_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=EmigOcl_OclModel, multiplicity=Multiplicity(1, 1))
    }
)
elements134: BinaryAssociation = BinaryAssociation(
    name="elements134",
    ends={
        Property(name="OclModelElement", type=EmigOcl_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model135", type=EmigOcl_OclModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
model137: BinaryAssociation = BinaryAssociation(
    name="model137",
    ends={
        Property(name="OclModel138", type=EmigOcl_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel", type=EmigOcl_OclModel, multiplicity=Multiplicity(0, 9999))
    }
)
initExpression121: BinaryAssociation = BinaryAssociation(
    name="initExpression121",
    ends={
        Property(name="OclExpression122", type=EmigOcl_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="owningAttribute", type=EmigOcl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type123: BinaryAssociation = BinaryAssociation(
    name="type123",
    ends={
        Property(name="OclType124", type=EmigOcl_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attribute", type=EmigOcl_OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters125: BinaryAssociation = BinaryAssociation(
    name="parameters125",
    ends={
        Property(name="Parameter", type=EmigOcl_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation", type=EmigOcl_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType126: BinaryAssociation = BinaryAssociation(
    name="returnType126",
    ends={
        Property(name="OclType128", type=EmigOcl_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation127", type=EmigOcl_OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body129: BinaryAssociation = BinaryAssociation(
    name="body129",
    ends={
        Property(name="OclExpression130", type=EmigOcl_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="owningOperation", type=EmigOcl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_EmigOcl_Module_LocatedElement = Generalization(general=LocatedElement, specific=EmigOcl_Module)
gen_EmigOcl_OclExpression_LocatedElement = Generalization(general=LocatedElement, specific=EmigOcl_OclExpression)
gen_EmigOcl_OrderedSetExp_CollectionExp = Generalization(general=CollectionExp, specific=EmigOcl_OrderedSetExp)
gen_EmigOcl_SequenceExp_CollectionExp = Generalization(general=CollectionExp, specific=EmigOcl_SequenceExp)
gen_EmigOcl_SetExp_CollectionExp = Generalization(general=CollectionExp, specific=EmigOcl_SetExp)
gen_EmigOcl_TupleExp_OclExpression = Generalization(general=OclExpression, specific=EmigOcl_TupleExp)
gen_EmigOcl_TuplePart_LocalVariable = Generalization(general=LocalVariable, specific=EmigOcl_TuplePart)
gen_EmigOcl_MapExp_OclExpression = Generalization(general=OclExpression, specific=EmigOcl_MapExp)
gen_EmigOcl_VariableExp_OclExpression = Generalization(general=OclExpression, specific=EmigOcl_VariableExp)
gen_EmigOcl_SuperExp_OclExpression = Generalization(general=OclExpression, specific=EmigOcl_SuperExp)
gen_EmigOcl_SelfExp_OclExpression = Generalization(general=OclExpression, specific=EmigOcl_SelfExp)
gen_EmigOcl_PrimitiveExp_OclExpression = Generalization(general=OclExpression, specific=EmigOcl_PrimitiveExp)
gen_EmigOcl_StringExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=EmigOcl_StringExp)
gen_EmigOcl_BooleanExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=EmigOcl_BooleanExp)
gen_EmigOcl_NumericExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=EmigOcl_NumericExp)
gen_EmigOcl_RealExp_NumericExp = Generalization(general=NumericExp, specific=EmigOcl_RealExp)
gen_EmigOcl_IntegerExp_NumericExp = Generalization(general=NumericExp, specific=EmigOcl_IntegerExp)
gen_EmigOcl_CollectionExp_OclExpression = Generalization(general=OclExpression, specific=EmigOcl_CollectionExp)
gen_EmigOcl_BagExp_CollectionExp = Generalization(general=CollectionExp, specific=EmigOcl_BagExp)
gen_EmigOcl_StaticOperationCall_StaticPropertyCall = Generalization(general=StaticPropertyCall, specific=EmigOcl_StaticOperationCall)
gen_EmigOcl_PropertyCallExp_OclExpression = Generalization(general=OclExpression, specific=EmigOcl_PropertyCallExp)
gen_EmigOcl_NavigationOrAttributeCall_PropertyCall = Generalization(general=PropertyCall, specific=EmigOcl_NavigationOrAttributeCall)
gen_EmigOcl_MapElement_LocatedElement = Generalization(general=LocatedElement, specific=EmigOcl_MapElement)
gen_EmigOcl_EnumLiteralExp_OclExpression = Generalization(general=OclExpression, specific=EmigOcl_EnumLiteralExp)
gen_EmigOcl_OclUndefinedExp_OclExpression = Generalization(general=OclExpression, specific=EmigOcl_OclUndefinedExp)
gen_EmigOcl_StaticPropertyCallExp_OclExpression = Generalization(general=OclExpression, specific=EmigOcl_StaticPropertyCallExp)
gen_EmigOcl_StaticNavigationOrAttributeCall_StaticPropertyCall = Generalization(general=StaticPropertyCall, specific=EmigOcl_StaticNavigationOrAttributeCall)
gen_EmigOcl_CollectionOperationCall_OperationCall = Generalization(general=OperationCall, specific=EmigOcl_CollectionOperationCall)
gen_EmigOcl_LoopExp_PropertyCall = Generalization(general=PropertyCall, specific=EmigOcl_LoopExp)
gen_EmigOcl_OperationCall_PropertyCall = Generalization(general=PropertyCall, specific=EmigOcl_OperationCall)
gen_EmigOcl_OperatorCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=EmigOcl_OperatorCallExp)
gen_EmigOcl_NotOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=EmigOcl_NotOpCallExp)
gen_EmigOcl_RelOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=EmigOcl_RelOpCallExp)
gen_EmigOcl_EqOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=EmigOcl_EqOpCallExp)
gen_EmigOcl_AddOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=EmigOcl_AddOpCallExp)
gen_EmigOcl_IntOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=EmigOcl_IntOpCallExp)
gen_EmigOcl_MulOpCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=EmigOcl_MulOpCallExp)
gen_EmigOcl_LambdaCallExp_VariableExp = Generalization(general=VariableExp, specific=EmigOcl_LambdaCallExp)
gen_EmigOcl_BraceExp_OclExpression = Generalization(general=OclExpression, specific=EmigOcl_BraceExp)
gen_EmigOcl_LocalVariable_VariableDeclaration = Generalization(general=VariableDeclaration, specific=EmigOcl_LocalVariable)
gen_EmigOcl_IterateExp_LoopExp = Generalization(general=LoopExp, specific=EmigOcl_IterateExp)
gen_EmigOcl_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=EmigOcl_IteratorExp)
gen_EmigOcl_LetExp_OclExpression = Generalization(general=OclExpression, specific=EmigOcl_LetExp)
gen_EmigOcl_IfExp_OclExpression = Generalization(general=OclExpression, specific=EmigOcl_IfExp)
gen_EmigOcl_VariableDeclaration_LocatedElement = Generalization(general=LocatedElement, specific=EmigOcl_VariableDeclaration)
gen_EmigOcl_Iterator_VariableDeclaration = Generalization(general=VariableDeclaration, specific=EmigOcl_Iterator)
gen_EmigOcl_Parameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=EmigOcl_Parameter)
gen_EmigOcl_CollectionType_OclType = Generalization(general=OclType, specific=EmigOcl_CollectionType)
gen_EmigOcl_OclType_LocatedElement = Generalization(general=LocatedElement, specific=EmigOcl_OclType)
gen_EmigOcl_SequenceType_CollectionType = Generalization(general=CollectionType, specific=EmigOcl_SequenceType)
gen_EmigOcl_SetType_CollectionType = Generalization(general=CollectionType, specific=EmigOcl_SetType)
gen_EmigOcl_OclAnyType_OclType = Generalization(general=OclType, specific=EmigOcl_OclAnyType)
gen_EmigOcl_TupleType_OclType = Generalization(general=OclType, specific=EmigOcl_TupleType)
gen_EmigOcl_TupleTypeAttribute_LocatedElement = Generalization(general=LocatedElement, specific=EmigOcl_TupleTypeAttribute)
gen_EmigOcl_OclModelElementExp_OclExpression = Generalization(general=OclExpression, specific=EmigOcl_OclModelElementExp)
gen_EmigOcl_Primitive_OclType = Generalization(general=OclType, specific=EmigOcl_Primitive)
gen_EmigOcl_StringType_Primitive = Generalization(general=Primitive, specific=EmigOcl_StringType)
gen_EmigOcl_BooleanType_Primitive = Generalization(general=Primitive, specific=EmigOcl_BooleanType)
gen_EmigOcl_NumericType_Primitive = Generalization(general=Primitive, specific=EmigOcl_NumericType)
gen_EmigOcl_IntegerType_NumericType = Generalization(general=NumericType, specific=EmigOcl_IntegerType)
gen_EmigOcl_RealType_NumericType = Generalization(general=NumericType, specific=EmigOcl_RealType)
gen_EmigOcl_BagType_CollectionType = Generalization(general=CollectionType, specific=EmigOcl_BagType)
gen_EmigOcl_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=EmigOcl_OrderedSetType)
gen_EmigOcl_OclContextDefinition_LocatedElement = Generalization(general=LocatedElement, specific=EmigOcl_OclContextDefinition)
gen_EmigOcl_OclFeature_LocatedElement = Generalization(general=LocatedElement, specific=EmigOcl_OclFeature)
gen_EmigOcl_OclModelElement_OclType = Generalization(general=OclType, specific=EmigOcl_OclModelElement)
gen_EmigOcl_MapType_OclType = Generalization(general=OclType, specific=EmigOcl_MapType)
gen_EmigOcl_LambdaType_OclType = Generalization(general=OclType, specific=EmigOcl_LambdaType)
gen_EmigOcl_OclFeatureDefinition_LocatedElement = Generalization(general=LocatedElement, specific=EmigOcl_OclFeatureDefinition)
gen_EmigOcl_Attribute_OclFeature = Generalization(general=OclFeature, specific=EmigOcl_Attribute)
gen_EmigOcl_Operation_OclFeature = Generalization(general=OclFeature, specific=EmigOcl_Operation)
gen_EmigOcl_OclModel_LocatedElement = Generalization(general=LocatedElement, specific=EmigOcl_OclModel)

# Domain Model
domain_model = DomainModel(
    name="EmigOcl",
    types={EmigOcl_LocatedElement, EmigOcl_LocalVariable, EmigOcl_Operation, EmigOcl_Attribute, EmigOcl_Module, LocatedElement, EmigOcl_OclModel, EmigOcl_OclFeatureDefinition, EmigOcl_OclExpression, EmigOcl_OclType, EmigOcl_IfExp, EmigOcl_PropertyCallExp, EmigOcl_CollectionExp, EmigOcl_LetExp, EmigOcl_LoopExp, EmigOcl_OperationCall, EmigOcl_OrderedSetExp, EmigOcl_SequenceExp, EmigOcl_SetExp, EmigOcl_TupleExp, EmigOcl_TuplePart, LocalVariable, EmigOcl_VariableExp, EmigOcl_MapExp, OclExpression, EmigOcl_VariableDeclaration, EmigOcl_SuperExp, EmigOcl_SelfExp, EmigOcl_PrimitiveExp, EmigOcl_StringExp, PrimitiveExp, EmigOcl_BooleanExp, EmigOcl_NumericExp, EmigOcl_RealExp, NumericExp, EmigOcl_IntegerExp, EmigOcl_BagExp, CollectionExp, EmigOcl_StaticOperationCall, EmigOcl_PropertyCall, EmigOcl_NavigationOrAttributeCall, PropertyCall, EmigOcl_MapElement, EmigOcl_EnumLiteralExp, EmigOcl_OclUndefinedExp, EmigOcl_StaticPropertyCallExp, EmigOcl_StaticPropertyCall, EmigOcl_StaticNavigationOrAttributeCall, StaticPropertyCall, EmigOcl_CollectionOperationCall, OperationCall, EmigOcl_Iterator, EmigOcl_OperatorCallExp, PropertyCallExp, EmigOcl_NotOpCallExp, OperatorCallExp, EmigOcl_RelOpCallExp, EmigOcl_EqOpCallExp, EmigOcl_AddOpCallExp, EmigOcl_IntOpCallExp, EmigOcl_MulOpCallExp, EmigOcl_LambdaCallExp, VariableExp, EmigOcl_BraceExp, VariableDeclaration, EmigOcl_IterateExp, LoopExp, EmigOcl_IteratorExp, EmigOcl_MapType, EmigOcl_Parameter, EmigOcl_CollectionType, OclType, EmigOcl_OclContextDefinition, EmigOcl_SequenceType, EmigOcl_SetType, EmigOcl_OclAnyType, EmigOcl_TupleType, EmigOcl_TupleTypeAttribute, EmigOcl_OclModelElementExp, EmigOcl_Primitive, EmigOcl_StringType, Primitive, EmigOcl_BooleanType, EmigOcl_NumericType, EmigOcl_IntegerType, NumericType, EmigOcl_RealType, EmigOcl_BagType, CollectionType, EmigOcl_OrderedSetType, EmigOcl_OclModelElement, EmigOcl_LambdaType, EmigOcl_OclFeature, OclFeature},
    associations={parentOperation9, initializedVariable10, ifExp211, owningOperation13, ifExp115, owningAttribute17, models0, features1, type3, ifExp34, appliedProperty5, collection6, letExp7, loopExp8, tuplePart21, tuple22, referredVariable19, elements20, arguments33, calls35, source36, elements23, map24, key26, value27, source30, staticCall31, exp44, body46, iterators48, arguments38, argument40, type62, arguments42, variableExp64, letExp65, initExpression67, baseExp69, result49, variable51, in_53, thenExpression56, condition58, elseExpression60, oclExpression77, operation79, mapType281, attribute82, loopExpr70, operation72, elementType74, definitions76, attributes95, type97, tupleType99, mapType85, collectionTypes87, tupleTypeAttribute88, variableDeclaration90, model93, context_112, definition115, context_117, definition119, model100, valueType102, keyType104, returnType106, argumentTypes108, feature111, metamodel132, elements134, model137, initExpression121, type123, parameters125, returnType126, body129},
    generalizations={gen_EmigOcl_Module_LocatedElement, gen_EmigOcl_OclExpression_LocatedElement, gen_EmigOcl_OrderedSetExp_CollectionExp, gen_EmigOcl_SequenceExp_CollectionExp, gen_EmigOcl_SetExp_CollectionExp, gen_EmigOcl_TupleExp_OclExpression, gen_EmigOcl_TuplePart_LocalVariable, gen_EmigOcl_MapExp_OclExpression, gen_EmigOcl_VariableExp_OclExpression, gen_EmigOcl_SuperExp_OclExpression, gen_EmigOcl_SelfExp_OclExpression, gen_EmigOcl_PrimitiveExp_OclExpression, gen_EmigOcl_StringExp_PrimitiveExp, gen_EmigOcl_BooleanExp_PrimitiveExp, gen_EmigOcl_NumericExp_PrimitiveExp, gen_EmigOcl_RealExp_NumericExp, gen_EmigOcl_IntegerExp_NumericExp, gen_EmigOcl_CollectionExp_OclExpression, gen_EmigOcl_BagExp_CollectionExp, gen_EmigOcl_StaticOperationCall_StaticPropertyCall, gen_EmigOcl_PropertyCallExp_OclExpression, gen_EmigOcl_NavigationOrAttributeCall_PropertyCall, gen_EmigOcl_MapElement_LocatedElement, gen_EmigOcl_EnumLiteralExp_OclExpression, gen_EmigOcl_OclUndefinedExp_OclExpression, gen_EmigOcl_StaticPropertyCallExp_OclExpression, gen_EmigOcl_StaticNavigationOrAttributeCall_StaticPropertyCall, gen_EmigOcl_CollectionOperationCall_OperationCall, gen_EmigOcl_LoopExp_PropertyCall, gen_EmigOcl_OperationCall_PropertyCall, gen_EmigOcl_OperatorCallExp_PropertyCallExp, gen_EmigOcl_NotOpCallExp_OperatorCallExp, gen_EmigOcl_RelOpCallExp_OperatorCallExp, gen_EmigOcl_EqOpCallExp_OperatorCallExp, gen_EmigOcl_AddOpCallExp_OperatorCallExp, gen_EmigOcl_IntOpCallExp_OperatorCallExp, gen_EmigOcl_MulOpCallExp_OperatorCallExp, gen_EmigOcl_LambdaCallExp_VariableExp, gen_EmigOcl_BraceExp_OclExpression, gen_EmigOcl_LocalVariable_VariableDeclaration, gen_EmigOcl_IterateExp_LoopExp, gen_EmigOcl_IteratorExp_LoopExp, gen_EmigOcl_LetExp_OclExpression, gen_EmigOcl_IfExp_OclExpression, gen_EmigOcl_VariableDeclaration_LocatedElement, gen_EmigOcl_Iterator_VariableDeclaration, gen_EmigOcl_Parameter_VariableDeclaration, gen_EmigOcl_CollectionType_OclType, gen_EmigOcl_OclType_LocatedElement, gen_EmigOcl_SequenceType_CollectionType, gen_EmigOcl_SetType_CollectionType, gen_EmigOcl_OclAnyType_OclType, gen_EmigOcl_TupleType_OclType, gen_EmigOcl_TupleTypeAttribute_LocatedElement, gen_EmigOcl_OclModelElementExp_OclExpression, gen_EmigOcl_Primitive_OclType, gen_EmigOcl_StringType_Primitive, gen_EmigOcl_BooleanType_Primitive, gen_EmigOcl_NumericType_Primitive, gen_EmigOcl_IntegerType_NumericType, gen_EmigOcl_RealType_NumericType, gen_EmigOcl_BagType_CollectionType, gen_EmigOcl_OrderedSetType_CollectionType, gen_EmigOcl_OclContextDefinition_LocatedElement, gen_EmigOcl_OclFeature_LocatedElement, gen_EmigOcl_OclModelElement_OclType, gen_EmigOcl_MapType_OclType, gen_EmigOcl_LambdaType_OclType, gen_EmigOcl_OclFeatureDefinition_LocatedElement, gen_EmigOcl_Attribute_OclFeature, gen_EmigOcl_Operation_OclFeature, gen_EmigOcl_OclModel_LocatedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)