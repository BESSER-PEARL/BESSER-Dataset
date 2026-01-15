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
oCLlite_Module = Class(name="oCLlite::Module")
oCLlite_OclLModel = Class(name="oCLlite::OclLModel")
oCLlite_Import = Class(name="oCLlite::Import")
oCLlite_ModuleElement = Class(name="oCLlite::ModuleElement")
oCLlite_OclLExpression = Class(name="oCLlite::OclLExpression")
oCLlite_LocalVariable = Class(name="oCLlite::LocalVariable")
oCLlite_Iterator = Class(name="oCLlite::Iterator")
oCLlite_OclLType = Class(name="oCLlite::OclLType")
oCLlite_CollectionExp = Class(name="oCLlite::CollectionExp")
OclLExpression = Class(name="OclLExpression")
oCLlite_URI_ = Class(name="oCLlite::URI::")
oCLlite_Query = Class(name="oCLlite::Query")
ModuleElement = Class(name="ModuleElement")
oCLlite_TuplePart = Class(name="oCLlite::TuplePart")
oCLlite_PrimitiveExp = Class(name="oCLlite::PrimitiveExp")
oCLlite_NumberLiteralExp = Class(name="oCLlite::NumberLiteralExp")
PrimitiveExp = Class(name="PrimitiveExp")
oCLlite_StringLiteralExp = Class(name="oCLlite::StringLiteralExp")
oCLlite_BooleanLiteralExp = Class(name="oCLlite::BooleanLiteralExp")
oCLlite_UnlimitedNaturalLiteralExp = Class(name="oCLlite::UnlimitedNaturalLiteralExp")
oCLlite_InvalidLiteralExp = Class(name="oCLlite::InvalidLiteralExp")
oCLlite_NullLiteralExp = Class(name="oCLlite::NullLiteralExp")
oCLlite_IfExp = Class(name="oCLlite::IfExp")
oCLlite_BagExp = Class(name="oCLlite::BagExp")
CollectionExp = Class(name="CollectionExp")
oCLlite_SequenceExp = Class(name="oCLlite::SequenceExp")
oCLlite_SetExp = Class(name="oCLlite::SetExp")
oCLlite_OrderedSetExp = Class(name="oCLlite::OrderedSetExp")
oCLlite_MapExp = Class(name="oCLlite::MapExp")
oCLlite_MapElement = Class(name="oCLlite::MapElement")
oCLlite_EnvType = Class(name="oCLlite::EnvType")
oCLlite_LambdaType = Class(name="oCLlite::LambdaType")
oCLlite_MapType = Class(name="oCLlite::MapType")
oCLlite_TupleType = Class(name="oCLlite::TupleType")
oCLlite_OclLAnyType = Class(name="oCLlite::OclLAnyType")
oCLlite_SetType = Class(name="oCLlite::SetType")
oCLlite_OclLModelElementExp = Class(name="oCLlite::OclLModelElementExp")
OclLType = Class(name="OclLType")
oCLlite_RealType = Class(name="oCLlite::RealType")
oCLlite_IntegerType = Class(name="oCLlite::IntegerType")
oCLlite_BooleanType = Class(name="oCLlite::BooleanType")
oCLlite_StringType = Class(name="oCLlite::StringType")
oCLlite_BoolOpCallExp = Class(name="oCLlite::BoolOpCallExp")
oCLlite_EqOpCallExp = Class(name="oCLlite::EqOpCallExp")
oCLlite_ComOpCallExp = Class(name="oCLlite::ComOpCallExp")
oCLlite_AddOpCallExp = Class(name="oCLlite::AddOpCallExp")
oCLlite_SequenceType = Class(name="oCLlite::SequenceType")
oCLlite_OrderedSetType = Class(name="oCLlite::OrderedSetType")
oCLlite_BagType = Class(name="oCLlite::BagType")
oCLlite_IterateExp = Class(name="oCLlite::IterateExp")
oCLlite_IteratorExp = Class(name="oCLlite::IteratorExp")
oCLlite_NavigationOrAttributeCall = Class(name="oCLlite::NavigationOrAttributeCall")
oCLlite_OperationCall = Class(name="oCLlite::OperationCall")
oCLlite_LambdaExp = Class(name="oCLlite::LambdaExp")
oCLlite_MulOpCallExp = Class(name="oCLlite::MulOpCallExp")
oCLlite_NavigationExp = Class(name="oCLlite::NavigationExp")
oCLlite_CollectionOpCallExp = Class(name="oCLlite::CollectionOpCallExp")
oCLlite_SelfExp = Class(name="oCLlite::SelfExp")
oCLlite_NestedExp = Class(name="oCLlite::NestedExp")
oCLlite_TupleExp = Class(name="oCLlite::TupleExp")
oCLlite_ElseIfThenExp = Class(name="oCLlite::ElseIfThenExp")

# oCLlite_Module class attributes and methods
oCLlite_Module_name: Property = Property(name="name", type=StringType)
oCLlite_Module.attributes={oCLlite_Module_name}

# oCLlite_OclLModel class attributes and methods
oCLlite_OclLModel_name: Property = Property(name="name", type=StringType)
oCLlite_OclLModel.attributes={oCLlite_OclLModel_name}

# oCLlite_Import class attributes and methods
oCLlite_Import_name: Property = Property(name="name", type=StringType)
oCLlite_Import.attributes={oCLlite_Import_name}

# oCLlite_ModuleElement class attributes and methods

# oCLlite_OclLExpression class attributes and methods
oCLlite_OclLExpression_name: Property = Property(name="name", type=StringType)
oCLlite_OclLExpression_elements: Property = Property(name="elements", type=StringType)
oCLlite_OclLExpression.attributes={oCLlite_OclLExpression_elements, oCLlite_OclLExpression_name}

# oCLlite_LocalVariable class attributes and methods
oCLlite_LocalVariable_name: Property = Property(name="name", type=StringType)
oCLlite_LocalVariable.attributes={oCLlite_LocalVariable_name}

# oCLlite_Iterator class attributes and methods
oCLlite_Iterator_name: Property = Property(name="name", type=StringType)
oCLlite_Iterator.attributes={oCLlite_Iterator_name}

# oCLlite_OclLType class attributes and methods

# oCLlite_CollectionExp class attributes and methods

# OclLExpression class attributes and methods

# oCLlite_URI_ class attributes and methods
oCLlite_URI__scheme: Property = Property(name="scheme", type=StringType)
oCLlite_URI__authority: Property = Property(name="authority", type=StringType)
oCLlite_URI__fragment_: Property = Property(name="fragment_", type=StringType)
oCLlite_URI_.attributes={oCLlite_URI__authority, oCLlite_URI__scheme, oCLlite_URI__fragment_}

# oCLlite_Query class attributes and methods
oCLlite_Query_name: Property = Property(name="name", type=StringType)
oCLlite_Query.attributes={oCLlite_Query_name}

# ModuleElement class attributes and methods

# oCLlite_TuplePart class attributes and methods
oCLlite_TuplePart_name: Property = Property(name="name", type=StringType)
oCLlite_TuplePart.attributes={oCLlite_TuplePart_name}

# oCLlite_PrimitiveExp class attributes and methods

# oCLlite_NumberLiteralExp class attributes and methods
oCLlite_NumberLiteralExp_symbol: Property = Property(name="symbol", type=IntegerType)
oCLlite_NumberLiteralExp.attributes={oCLlite_NumberLiteralExp_symbol}

# PrimitiveExp class attributes and methods

# oCLlite_StringLiteralExp class attributes and methods
oCLlite_StringLiteralExp_segments: Property = Property(name="segments", type=StringType)
oCLlite_StringLiteralExp.attributes={oCLlite_StringLiteralExp_segments}

# oCLlite_BooleanLiteralExp class attributes and methods
oCLlite_BooleanLiteralExp_symbol: Property = Property(name="symbol", type=StringType)
oCLlite_BooleanLiteralExp.attributes={oCLlite_BooleanLiteralExp_symbol}

# oCLlite_UnlimitedNaturalLiteralExp class attributes and methods

# oCLlite_InvalidLiteralExp class attributes and methods

# oCLlite_NullLiteralExp class attributes and methods

# oCLlite_IfExp class attributes and methods

# oCLlite_BagExp class attributes and methods

# CollectionExp class attributes and methods

# oCLlite_SequenceExp class attributes and methods

# oCLlite_SetExp class attributes and methods

# oCLlite_OrderedSetExp class attributes and methods

# oCLlite_MapExp class attributes and methods

# oCLlite_MapElement class attributes and methods

# oCLlite_EnvType class attributes and methods
oCLlite_EnvType_name: Property = Property(name="name", type=StringType)
oCLlite_EnvType.attributes={oCLlite_EnvType_name}

# oCLlite_LambdaType class attributes and methods
oCLlite_LambdaType_name: Property = Property(name="name", type=StringType)
oCLlite_LambdaType.attributes={oCLlite_LambdaType_name}

# oCLlite_MapType class attributes and methods
oCLlite_MapType_name: Property = Property(name="name", type=StringType)
oCLlite_MapType.attributes={oCLlite_MapType_name}

# oCLlite_TupleType class attributes and methods

# oCLlite_OclLAnyType class attributes and methods
oCLlite_OclLAnyType_name: Property = Property(name="name", type=StringType)
oCLlite_OclLAnyType.attributes={oCLlite_OclLAnyType_name}

# oCLlite_SetType class attributes and methods
oCLlite_SetType_name: Property = Property(name="name", type=StringType)
oCLlite_SetType.attributes={oCLlite_SetType_name}

# oCLlite_OclLModelElementExp class attributes and methods
oCLlite_OclLModelElementExp_name: Property = Property(name="name", type=StringType)
oCLlite_OclLModelElementExp.attributes={oCLlite_OclLModelElementExp_name}

# OclLType class attributes and methods

# oCLlite_RealType class attributes and methods
oCLlite_RealType_name: Property = Property(name="name", type=StringType)
oCLlite_RealType.attributes={oCLlite_RealType_name}

# oCLlite_IntegerType class attributes and methods
oCLlite_IntegerType_name: Property = Property(name="name", type=StringType)
oCLlite_IntegerType.attributes={oCLlite_IntegerType_name}

# oCLlite_BooleanType class attributes and methods
oCLlite_BooleanType_name: Property = Property(name="name", type=StringType)
oCLlite_BooleanType.attributes={oCLlite_BooleanType_name}

# oCLlite_StringType class attributes and methods
oCLlite_StringType_name: Property = Property(name="name", type=StringType)
oCLlite_StringType.attributes={oCLlite_StringType_name}

# oCLlite_BoolOpCallExp class attributes and methods

# oCLlite_EqOpCallExp class attributes and methods

# oCLlite_ComOpCallExp class attributes and methods

# oCLlite_AddOpCallExp class attributes and methods

# oCLlite_SequenceType class attributes and methods
oCLlite_SequenceType_name: Property = Property(name="name", type=StringType)
oCLlite_SequenceType.attributes={oCLlite_SequenceType_name}

# oCLlite_OrderedSetType class attributes and methods
oCLlite_OrderedSetType_name: Property = Property(name="name", type=StringType)
oCLlite_OrderedSetType.attributes={oCLlite_OrderedSetType_name}

# oCLlite_BagType class attributes and methods
oCLlite_BagType_name: Property = Property(name="name", type=StringType)
oCLlite_BagType.attributes={oCLlite_BagType_name}

# oCLlite_IterateExp class attributes and methods

# oCLlite_IteratorExp class attributes and methods

# oCLlite_NavigationOrAttributeCall class attributes and methods
oCLlite_NavigationOrAttributeCall_feature: Property = Property(name="feature", type=StringType)
oCLlite_NavigationOrAttributeCall.attributes={oCLlite_NavigationOrAttributeCall_feature}

# oCLlite_OperationCall class attributes and methods

# oCLlite_LambdaExp class attributes and methods

# oCLlite_MulOpCallExp class attributes and methods

# oCLlite_NavigationExp class attributes and methods

# oCLlite_CollectionOpCallExp class attributes and methods

# oCLlite_SelfExp class attributes and methods

# oCLlite_NestedExp class attributes and methods

# oCLlite_TupleExp class attributes and methods

# oCLlite_ElseIfThenExp class attributes and methods

# Relationships
source0: BinaryAssociation = BinaryAssociation(
    name="source0",
    ends={
        Property(name="oCLlite_OclLModel", type=oCLlite_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_Module", type=oCLlite_OclLModel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
input1: BinaryAssociation = BinaryAssociation(
    name="input1",
    ends={
        Property(name="oCLlite_OclLModel3", type=oCLlite_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_Module2", type=oCLlite_OclLModel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
imports4: BinaryAssociation = BinaryAssociation(
    name="imports4",
    ends={
        Property(name="oCLlite_Import", type=oCLlite_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_Module5", type=oCLlite_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements6: BinaryAssociation = BinaryAssociation(
    name="elements6",
    ends={
        Property(name="oCLlite_ModuleElement", type=oCLlite_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_Module7", type=oCLlite_ModuleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body10: BinaryAssociation = BinaryAssociation(
    name="body10",
    ends={
        Property(name="oCLlite_OclLExpression", type=oCLlite_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_Query", type=oCLlite_OclLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable11: BinaryAssociation = BinaryAssociation(
    name="variable11",
    ends={
        Property(name="oCLlite_LocalVariable", type=oCLlite_OclLExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_OclLExpression12", type=oCLlite_LocalVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
in14: BinaryAssociation = BinaryAssociation(
    name="in14",
    ends={
        Property(name="oCLlite_OclLExpression15", type=oCLlite_OclLExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_OclLExpression13", type=oCLlite_OclLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target17: BinaryAssociation = BinaryAssociation(
    name="target17",
    ends={
        Property(name="oCLlite_OclLExpression18", type=oCLlite_OclLExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_OclLExpression16", type=oCLlite_OclLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
model19: BinaryAssociation = BinaryAssociation(
    name="model19",
    ends={
        Property(name="oCLlite_OclLModel21", type=oCLlite_OclLExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_OclLExpression20", type=oCLlite_OclLModel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type22: BinaryAssociation = BinaryAssociation(
    name="type22",
    ends={
        Property(name="oCLlite_OclLType", type=oCLlite_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_Iterator", type=oCLlite_OclLType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type23: BinaryAssociation = BinaryAssociation(
    name="type23",
    ends={
        Property(name="oCLlite_OclLType25", type=oCLlite_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_LocalVariable24", type=oCLlite_OclLType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExp26: BinaryAssociation = BinaryAssociation(
    name="initExp26",
    ends={
        Property(name="oCLlite_OclLExpression28", type=oCLlite_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_LocalVariable27", type=oCLlite_OclLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
uri8: BinaryAssociation = BinaryAssociation(
    name="uri8",
    ends={
        Property(name="oCLlite_URI_", type=oCLlite_OclLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_OclLModel9", type=oCLlite_URI_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
key32: BinaryAssociation = BinaryAssociation(
    name="key32",
    ends={
        Property(name="oCLlite_OclLExpression34", type=oCLlite_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_MapElement33", type=oCLlite_OclLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value35: BinaryAssociation = BinaryAssociation(
    name="value35",
    ends={
        Property(name="oCLlite_OclLExpression37", type=oCLlite_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_MapElement36", type=oCLlite_OclLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type38: BinaryAssociation = BinaryAssociation(
    name="type38",
    ends={
        Property(name="oCLlite_OclLType39", type=oCLlite_TuplePart, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_TuplePart", type=oCLlite_OclLType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init40: BinaryAssociation = BinaryAssociation(
    name="init40",
    ends={
        Property(name="oCLlite_OclLExpression42", type=oCLlite_TuplePart, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_TuplePart41", type=oCLlite_OclLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition43: BinaryAssociation = BinaryAssociation(
    name="condition43",
    ends={
        Property(name="oCLlite_OclLExpression44", type=oCLlite_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_IfExp", type=oCLlite_OclLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parts29: BinaryAssociation = BinaryAssociation(
    name="parts29",
    ends={
        Property(name="oCLlite_OclLExpression30", type=oCLlite_CollectionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_CollectionExp", type=oCLlite_OclLExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mapElements31: BinaryAssociation = BinaryAssociation(
    name="mapElements31",
    ends={
        Property(name="oCLlite_MapElement", type=oCLlite_MapExp, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_MapExp", type=oCLlite_MapElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model54: BinaryAssociation = BinaryAssociation(
    name="model54",
    ends={
        Property(name="oCLlite_OclLModel55", type=oCLlite_OclLModelElementExp, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_OclLModelElementExp", type=oCLlite_OclLModel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argsTypes56: BinaryAssociation = BinaryAssociation(
    name="argsTypes56",
    ends={
        Property(name="oCLlite_OclLType57", type=oCLlite_LambdaType, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_LambdaType", type=oCLlite_OclLType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType58: BinaryAssociation = BinaryAssociation(
    name="returnType58",
    ends={
        Property(name="oCLlite_OclLType60", type=oCLlite_LambdaType, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_LambdaType59", type=oCLlite_OclLType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
keyType61: BinaryAssociation = BinaryAssociation(
    name="keyType61",
    ends={
        Property(name="oCLlite_OclLType62", type=oCLlite_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_MapType", type=oCLlite_OclLType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
valueType63: BinaryAssociation = BinaryAssociation(
    name="valueType63",
    ends={
        Property(name="oCLlite_OclLType65", type=oCLlite_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_MapType64", type=oCLlite_OclLType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elementType66: BinaryAssociation = BinaryAssociation(
    name="elementType66",
    ends={
        Property(name="oCLlite_OclLType67", type=oCLlite_SetType, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_SetType", type=oCLlite_OclLType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then45: BinaryAssociation = BinaryAssociation(
    name="then45",
    ends={
        Property(name="oCLlite_OclLExpression47", type=oCLlite_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_IfExp46", type=oCLlite_OclLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifThen48: BinaryAssociation = BinaryAssociation(
    name="ifThen48",
    ends={
        Property(name="oCLlite_OclLExpression50", type=oCLlite_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_IfExp49", type=oCLlite_OclLExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
else51: BinaryAssociation = BinaryAssociation(
    name="else51",
    ends={
        Property(name="oCLlite_OclLExpression53", type=oCLlite_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_IfExp52", type=oCLlite_OclLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elementType72: BinaryAssociation = BinaryAssociation(
    name="elementType72",
    ends={
        Property(name="oCLlite_OclLType73", type=oCLlite_BagType, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_BagType", type=oCLlite_OclLType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source74: BinaryAssociation = BinaryAssociation(
    name="source74",
    ends={
        Property(name="oCLlite_OclLExpression75", type=oCLlite_BoolOpCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_BoolOpCallExp", type=oCLlite_OclLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source76: BinaryAssociation = BinaryAssociation(
    name="source76",
    ends={
        Property(name="oCLlite_OclLExpression77", type=oCLlite_EqOpCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_EqOpCallExp", type=oCLlite_OclLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source78: BinaryAssociation = BinaryAssociation(
    name="source78",
    ends={
        Property(name="oCLlite_OclLExpression79", type=oCLlite_ComOpCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_ComOpCallExp", type=oCLlite_OclLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source80: BinaryAssociation = BinaryAssociation(
    name="source80",
    ends={
        Property(name="oCLlite_OclLExpression81", type=oCLlite_AddOpCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_AddOpCallExp", type=oCLlite_OclLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elementType68: BinaryAssociation = BinaryAssociation(
    name="elementType68",
    ends={
        Property(name="oCLlite_OclLType69", type=oCLlite_SequenceType, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_SequenceType", type=oCLlite_OclLType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elementType70: BinaryAssociation = BinaryAssociation(
    name="elementType70",
    ends={
        Property(name="oCLlite_OclLType71", type=oCLlite_OrderedSetType, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_OrderedSetType", type=oCLlite_OclLType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments86: BinaryAssociation = BinaryAssociation(
    name="arguments86",
    ends={
        Property(name="oCLlite_OclLExpression87", type=oCLlite_CollectionOpCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_CollectionOpCallExp", type=oCLlite_OclLExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iterators88: BinaryAssociation = BinaryAssociation(
    name="iterators88",
    ends={
        Property(name="oCLlite_Iterator89", type=oCLlite_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_IterateExp", type=oCLlite_Iterator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result90: BinaryAssociation = BinaryAssociation(
    name="result90",
    ends={
        Property(name="oCLlite_LocalVariable92", type=oCLlite_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_IterateExp91", type=oCLlite_LocalVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body93: BinaryAssociation = BinaryAssociation(
    name="body93",
    ends={
        Property(name="oCLlite_OclLExpression95", type=oCLlite_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_IterateExp94", type=oCLlite_OclLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iterators96: BinaryAssociation = BinaryAssociation(
    name="iterators96",
    ends={
        Property(name="oCLlite_Iterator97", type=oCLlite_IteratorExp, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_IteratorExp", type=oCLlite_Iterator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body98: BinaryAssociation = BinaryAssociation(
    name="body98",
    ends={
        Property(name="oCLlite_OclLExpression100", type=oCLlite_IteratorExp, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_IteratorExp99", type=oCLlite_OclLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments101: BinaryAssociation = BinaryAssociation(
    name="arguments101",
    ends={
        Property(name="oCLlite_OclLExpression102", type=oCLlite_OperationCall, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_OperationCall", type=oCLlite_OclLExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source82: BinaryAssociation = BinaryAssociation(
    name="source82",
    ends={
        Property(name="oCLlite_OclLExpression83", type=oCLlite_MulOpCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_MulOpCallExp", type=oCLlite_OclLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source84: BinaryAssociation = BinaryAssociation(
    name="source84",
    ends={
        Property(name="oCLlite_OclLExpression85", type=oCLlite_NavigationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_NavigationExp", type=oCLlite_OclLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then109: BinaryAssociation = BinaryAssociation(
    name="then109",
    ends={
        Property(name="oCLlite_OclLExpression111", type=oCLlite_ElseIfThenExp, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_ElseIfThenExp110", type=oCLlite_OclLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp112: BinaryAssociation = BinaryAssociation(
    name="exp112",
    ends={
        Property(name="oCLlite_OclLExpression113", type=oCLlite_NestedExp, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_NestedExp", type=oCLlite_OclLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression103: BinaryAssociation = BinaryAssociation(
    name="expression103",
    ends={
        Property(name="oCLlite_OclLExpression104", type=oCLlite_LambdaExp, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_LambdaExp", type=oCLlite_OclLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parts105: BinaryAssociation = BinaryAssociation(
    name="parts105",
    ends={
        Property(name="oCLlite_TuplePart106", type=oCLlite_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_TupleExp", type=oCLlite_TuplePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition107: BinaryAssociation = BinaryAssociation(
    name="condition107",
    ends={
        Property(name="oCLlite_OclLExpression108", type=oCLlite_ElseIfThenExp, multiplicity=Multiplicity(1, 1)),
        Property(name="oCLlite_ElseIfThenExp", type=oCLlite_OclLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_oCLlite_CollectionExp_OclLExpression = Generalization(general=OclLExpression, specific=oCLlite_CollectionExp)
gen_oCLlite_Query_ModuleElement = Generalization(general=ModuleElement, specific=oCLlite_Query)
gen_oCLlite_PrimitiveExp_OclLExpression = Generalization(general=OclLExpression, specific=oCLlite_PrimitiveExp)
gen_oCLlite_NumberLiteralExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=oCLlite_NumberLiteralExp)
gen_oCLlite_StringLiteralExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=oCLlite_StringLiteralExp)
gen_oCLlite_BooleanLiteralExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=oCLlite_BooleanLiteralExp)
gen_oCLlite_UnlimitedNaturalLiteralExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=oCLlite_UnlimitedNaturalLiteralExp)
gen_oCLlite_InvalidLiteralExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=oCLlite_InvalidLiteralExp)
gen_oCLlite_NullLiteralExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=oCLlite_NullLiteralExp)
gen_oCLlite_IfExp_OclLExpression = Generalization(general=OclLExpression, specific=oCLlite_IfExp)
gen_oCLlite_BagExp_CollectionExp = Generalization(general=CollectionExp, specific=oCLlite_BagExp)
gen_oCLlite_SequenceExp_CollectionExp = Generalization(general=CollectionExp, specific=oCLlite_SequenceExp)
gen_oCLlite_SetExp_CollectionExp = Generalization(general=CollectionExp, specific=oCLlite_SetExp)
gen_oCLlite_OrderedSetExp_CollectionExp = Generalization(general=CollectionExp, specific=oCLlite_OrderedSetExp)
gen_oCLlite_MapExp_OclLExpression = Generalization(general=OclLExpression, specific=oCLlite_MapExp)
gen_oCLlite_EnvType_OclLType = Generalization(general=OclLType, specific=oCLlite_EnvType)
gen_oCLlite_LambdaType_OclLType = Generalization(general=OclLType, specific=oCLlite_LambdaType)
gen_oCLlite_MapType_OclLType = Generalization(general=OclLType, specific=oCLlite_MapType)
gen_oCLlite_TupleType_OclLType = Generalization(general=OclLType, specific=oCLlite_TupleType)
gen_oCLlite_OclLAnyType_OclLType = Generalization(general=OclLType, specific=oCLlite_OclLAnyType)
gen_oCLlite_SetType_OclLType = Generalization(general=OclLType, specific=oCLlite_SetType)
gen_oCLlite_OclLModelElementExp_OclLType = Generalization(general=OclLType, specific=oCLlite_OclLModelElementExp)
gen_oCLlite_RealType_OclLType = Generalization(general=OclLType, specific=oCLlite_RealType)
gen_oCLlite_IntegerType_OclLType = Generalization(general=OclLType, specific=oCLlite_IntegerType)
gen_oCLlite_BooleanType_OclLType = Generalization(general=OclLType, specific=oCLlite_BooleanType)
gen_oCLlite_StringType_OclLType = Generalization(general=OclLType, specific=oCLlite_StringType)
gen_oCLlite_BoolOpCallExp_OclLExpression = Generalization(general=OclLExpression, specific=oCLlite_BoolOpCallExp)
gen_oCLlite_EqOpCallExp_OclLExpression = Generalization(general=OclLExpression, specific=oCLlite_EqOpCallExp)
gen_oCLlite_ComOpCallExp_OclLExpression = Generalization(general=OclLExpression, specific=oCLlite_ComOpCallExp)
gen_oCLlite_AddOpCallExp_OclLExpression = Generalization(general=OclLExpression, specific=oCLlite_AddOpCallExp)
gen_oCLlite_SequenceType_OclLType = Generalization(general=OclLType, specific=oCLlite_SequenceType)
gen_oCLlite_OrderedSetType_OclLType = Generalization(general=OclLType, specific=oCLlite_OrderedSetType)
gen_oCLlite_BagType_OclLType = Generalization(general=OclLType, specific=oCLlite_BagType)
gen_oCLlite_IterateExp_OclLExpression = Generalization(general=OclLExpression, specific=oCLlite_IterateExp)
gen_oCLlite_IteratorExp_OclLExpression = Generalization(general=OclLExpression, specific=oCLlite_IteratorExp)
gen_oCLlite_NavigationOrAttributeCall_OclLExpression = Generalization(general=OclLExpression, specific=oCLlite_NavigationOrAttributeCall)
gen_oCLlite_OperationCall_OclLExpression = Generalization(general=OclLExpression, specific=oCLlite_OperationCall)
gen_oCLlite_LambdaExp_OclLExpression = Generalization(general=OclLExpression, specific=oCLlite_LambdaExp)
gen_oCLlite_MulOpCallExp_OclLExpression = Generalization(general=OclLExpression, specific=oCLlite_MulOpCallExp)
gen_oCLlite_NavigationExp_OclLExpression = Generalization(general=OclLExpression, specific=oCLlite_NavigationExp)
gen_oCLlite_CollectionOpCallExp_OclLExpression = Generalization(general=OclLExpression, specific=oCLlite_CollectionOpCallExp)
gen_oCLlite_SelfExp_OclLExpression = Generalization(general=OclLExpression, specific=oCLlite_SelfExp)
gen_oCLlite_NestedExp_OclLExpression = Generalization(general=OclLExpression, specific=oCLlite_NestedExp)
gen_oCLlite_TupleExp_OclLExpression = Generalization(general=OclLExpression, specific=oCLlite_TupleExp)
gen_oCLlite_ElseIfThenExp_OclLExpression = Generalization(general=OclLExpression, specific=oCLlite_ElseIfThenExp)

# Domain Model
domain_model = DomainModel(
    name="oCLlite",
    types={oCLlite_Module, oCLlite_OclLModel, oCLlite_Import, oCLlite_ModuleElement, oCLlite_OclLExpression, oCLlite_LocalVariable, oCLlite_Iterator, oCLlite_OclLType, oCLlite_CollectionExp, OclLExpression, oCLlite_URI_, oCLlite_Query, ModuleElement, oCLlite_TuplePart, oCLlite_PrimitiveExp, oCLlite_NumberLiteralExp, PrimitiveExp, oCLlite_StringLiteralExp, oCLlite_BooleanLiteralExp, oCLlite_UnlimitedNaturalLiteralExp, oCLlite_InvalidLiteralExp, oCLlite_NullLiteralExp, oCLlite_IfExp, oCLlite_BagExp, CollectionExp, oCLlite_SequenceExp, oCLlite_SetExp, oCLlite_OrderedSetExp, oCLlite_MapExp, oCLlite_MapElement, oCLlite_EnvType, oCLlite_LambdaType, oCLlite_MapType, oCLlite_TupleType, oCLlite_OclLAnyType, oCLlite_SetType, oCLlite_OclLModelElementExp, OclLType, oCLlite_RealType, oCLlite_IntegerType, oCLlite_BooleanType, oCLlite_StringType, oCLlite_BoolOpCallExp, oCLlite_EqOpCallExp, oCLlite_ComOpCallExp, oCLlite_AddOpCallExp, oCLlite_SequenceType, oCLlite_OrderedSetType, oCLlite_BagType, oCLlite_IterateExp, oCLlite_IteratorExp, oCLlite_NavigationOrAttributeCall, oCLlite_OperationCall, oCLlite_LambdaExp, oCLlite_MulOpCallExp, oCLlite_NavigationExp, oCLlite_CollectionOpCallExp, oCLlite_SelfExp, oCLlite_NestedExp, oCLlite_TupleExp, oCLlite_ElseIfThenExp},
    associations={source0, input1, imports4, elements6, body10, variable11, in14, target17, model19, type22, type23, initExp26, uri8, key32, value35, type38, init40, condition43, parts29, mapElements31, model54, argsTypes56, returnType58, keyType61, valueType63, elementType66, then45, ifThen48, else51, elementType72, source74, source76, source78, source80, elementType68, elementType70, arguments86, iterators88, result90, body93, iterators96, body98, arguments101, source82, source84, then109, exp112, expression103, parts105, condition107},
    generalizations={gen_oCLlite_CollectionExp_OclLExpression, gen_oCLlite_Query_ModuleElement, gen_oCLlite_PrimitiveExp_OclLExpression, gen_oCLlite_NumberLiteralExp_PrimitiveExp, gen_oCLlite_StringLiteralExp_PrimitiveExp, gen_oCLlite_BooleanLiteralExp_PrimitiveExp, gen_oCLlite_UnlimitedNaturalLiteralExp_PrimitiveExp, gen_oCLlite_InvalidLiteralExp_PrimitiveExp, gen_oCLlite_NullLiteralExp_PrimitiveExp, gen_oCLlite_IfExp_OclLExpression, gen_oCLlite_BagExp_CollectionExp, gen_oCLlite_SequenceExp_CollectionExp, gen_oCLlite_SetExp_CollectionExp, gen_oCLlite_OrderedSetExp_CollectionExp, gen_oCLlite_MapExp_OclLExpression, gen_oCLlite_EnvType_OclLType, gen_oCLlite_LambdaType_OclLType, gen_oCLlite_MapType_OclLType, gen_oCLlite_TupleType_OclLType, gen_oCLlite_OclLAnyType_OclLType, gen_oCLlite_SetType_OclLType, gen_oCLlite_OclLModelElementExp_OclLType, gen_oCLlite_RealType_OclLType, gen_oCLlite_IntegerType_OclLType, gen_oCLlite_BooleanType_OclLType, gen_oCLlite_StringType_OclLType, gen_oCLlite_BoolOpCallExp_OclLExpression, gen_oCLlite_EqOpCallExp_OclLExpression, gen_oCLlite_ComOpCallExp_OclLExpression, gen_oCLlite_AddOpCallExp_OclLExpression, gen_oCLlite_SequenceType_OclLType, gen_oCLlite_OrderedSetType_OclLType, gen_oCLlite_BagType_OclLType, gen_oCLlite_IterateExp_OclLExpression, gen_oCLlite_IteratorExp_OclLExpression, gen_oCLlite_NavigationOrAttributeCall_OclLExpression, gen_oCLlite_OperationCall_OclLExpression, gen_oCLlite_LambdaExp_OclLExpression, gen_oCLlite_MulOpCallExp_OclLExpression, gen_oCLlite_NavigationExp_OclLExpression, gen_oCLlite_CollectionOpCallExp_OclLExpression, gen_oCLlite_SelfExp_OclLExpression, gen_oCLlite_NestedExp_OclLExpression, gen_oCLlite_TupleExp_OclLExpression, gen_oCLlite_ElseIfThenExp_OclLExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)