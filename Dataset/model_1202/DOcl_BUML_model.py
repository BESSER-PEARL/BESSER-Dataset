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
docl_ModuleElement = Class(name="docl::ModuleElement")
docl_Module = Class(name="docl::Module")
docl_OclModel = Class(name="docl::OclModel")
docl_Import = Class(name="docl::Import")
docl_TuplePart = Class(name="docl::TuplePart")
docl_URI_ = Class(name="docl::URI::")
docl_Query = Class(name="docl::Query")
ModuleElement = Class(name="ModuleElement")
docl_OclExpression = Class(name="docl::OclExpression")
docl_LocalVariable = Class(name="docl::LocalVariable")
docl_Iterator = Class(name="docl::Iterator")
docl_OclType = Class(name="docl::OclType")
docl_LambdaType = Class(name="docl::LambdaType")
docl_PrimitiveExp = Class(name="docl::PrimitiveExp")
OclExpression = Class(name="OclExpression")
docl_NumberLiteralExp = Class(name="docl::NumberLiteralExp")
PrimitiveExp = Class(name="PrimitiveExp")
docl_StringLiteralExp = Class(name="docl::StringLiteralExp")
docl_BooleanLiteralExp = Class(name="docl::BooleanLiteralExp")
docl_UnlimitedNaturalLiteralExp = Class(name="docl::UnlimitedNaturalLiteralExp")
docl_InvalidLiteralExp = Class(name="docl::InvalidLiteralExp")
docl_NullLiteralExp = Class(name="docl::NullLiteralExp")
docl_IfExp = Class(name="docl::IfExp")
docl_OclModelElementExp = Class(name="docl::OclModelElementExp")
OclType = Class(name="OclType")
docl_EnvType = Class(name="docl::EnvType")
docl_RealType = Class(name="docl::RealType")
docl_MapType = Class(name="docl::MapType")
docl_TupleType = Class(name="docl::TupleType")
docl_OclAnyType = Class(name="docl::OclAnyType")
docl_SetType = Class(name="docl::SetType")
docl_SequenceType = Class(name="docl::SequenceType")
docl_OrderedSetType = Class(name="docl::OrderedSetType")
docl_BagType = Class(name="docl::BagType")
docl_IterateExp = Class(name="docl::IterateExp")
docl_IntegerType = Class(name="docl::IntegerType")
docl_BooleanType = Class(name="docl::BooleanType")
docl_StringType = Class(name="docl::StringType")
docl_BoolOpCallExp = Class(name="docl::BoolOpCallExp")
docl_EqOpCallExp = Class(name="docl::EqOpCallExp")
docl_ComOpCallExp = Class(name="docl::ComOpCallExp")
docl_AddOpCallExp = Class(name="docl::AddOpCallExp")
docl_MulOpCallExp = Class(name="docl::MulOpCallExp")
docl_NavigationExp = Class(name="docl::NavigationExp")
docl_CollectionOpCallExp = Class(name="docl::CollectionOpCallExp")
docl_NestedExp = Class(name="docl::NestedExp")
docl_IteratorExp = Class(name="docl::IteratorExp")
docl_NavigationOrAttributeCall = Class(name="docl::NavigationOrAttributeCall")
docl_OperationCall = Class(name="docl::OperationCall")
docl_LambdaExp = Class(name="docl::LambdaExp")
docl_TupleExp = Class(name="docl::TupleExp")
docl_ElseIfThenExp = Class(name="docl::ElseIfThenExp")
docl_SelfExp = Class(name="docl::SelfExp")

# docl_ModuleElement class attributes and methods

# docl_Module class attributes and methods
docl_Module_name: Property = Property(name="name", type=StringType)
docl_Module.attributes={docl_Module_name}

# docl_OclModel class attributes and methods
docl_OclModel_name: Property = Property(name="name", type=StringType)
docl_OclModel.attributes={docl_OclModel_name}

# docl_Import class attributes and methods
docl_Import_name: Property = Property(name="name", type=StringType)
docl_Import.attributes={docl_Import_name}

# docl_TuplePart class attributes and methods
docl_TuplePart_name: Property = Property(name="name", type=StringType)
docl_TuplePart.attributes={docl_TuplePart_name}

# docl_URI_ class attributes and methods
docl_URI__scheme: Property = Property(name="scheme", type=StringType)
docl_URI__authority: Property = Property(name="authority", type=StringType)
docl_URI__fragment_: Property = Property(name="fragment_", type=StringType)
docl_URI_.attributes={docl_URI__fragment_, docl_URI__authority, docl_URI__scheme}

# docl_Query class attributes and methods
docl_Query_name: Property = Property(name="name", type=StringType)
docl_Query.attributes={docl_Query_name}

# ModuleElement class attributes and methods

# docl_OclExpression class attributes and methods
docl_OclExpression_name: Property = Property(name="name", type=StringType)
docl_OclExpression_elements: Property = Property(name="elements", type=StringType)
docl_OclExpression.attributes={docl_OclExpression_elements, docl_OclExpression_name}

# docl_LocalVariable class attributes and methods
docl_LocalVariable_name: Property = Property(name="name", type=StringType)
docl_LocalVariable.attributes={docl_LocalVariable_name}

# docl_Iterator class attributes and methods
docl_Iterator_name: Property = Property(name="name", type=StringType)
docl_Iterator.attributes={docl_Iterator_name}

# docl_OclType class attributes and methods

# docl_LambdaType class attributes and methods
docl_LambdaType_name: Property = Property(name="name", type=StringType)
docl_LambdaType.attributes={docl_LambdaType_name}

# docl_PrimitiveExp class attributes and methods

# OclExpression class attributes and methods

# docl_NumberLiteralExp class attributes and methods
docl_NumberLiteralExp_symbol: Property = Property(name="symbol", type=IntegerType)
docl_NumberLiteralExp.attributes={docl_NumberLiteralExp_symbol}

# PrimitiveExp class attributes and methods

# docl_StringLiteralExp class attributes and methods
docl_StringLiteralExp_segments: Property = Property(name="segments", type=StringType)
docl_StringLiteralExp.attributes={docl_StringLiteralExp_segments}

# docl_BooleanLiteralExp class attributes and methods
docl_BooleanLiteralExp_symbol: Property = Property(name="symbol", type=StringType)
docl_BooleanLiteralExp.attributes={docl_BooleanLiteralExp_symbol}

# docl_UnlimitedNaturalLiteralExp class attributes and methods

# docl_InvalidLiteralExp class attributes and methods

# docl_NullLiteralExp class attributes and methods

# docl_IfExp class attributes and methods

# docl_OclModelElementExp class attributes and methods
docl_OclModelElementExp_name: Property = Property(name="name", type=StringType)
docl_OclModelElementExp.attributes={docl_OclModelElementExp_name}

# OclType class attributes and methods

# docl_EnvType class attributes and methods
docl_EnvType_name: Property = Property(name="name", type=StringType)
docl_EnvType.attributes={docl_EnvType_name}

# docl_RealType class attributes and methods
docl_RealType_name: Property = Property(name="name", type=StringType)
docl_RealType.attributes={docl_RealType_name}

# docl_MapType class attributes and methods
docl_MapType_name: Property = Property(name="name", type=StringType)
docl_MapType.attributes={docl_MapType_name}

# docl_TupleType class attributes and methods

# docl_OclAnyType class attributes and methods
docl_OclAnyType_name: Property = Property(name="name", type=StringType)
docl_OclAnyType.attributes={docl_OclAnyType_name}

# docl_SetType class attributes and methods
docl_SetType_name: Property = Property(name="name", type=StringType)
docl_SetType.attributes={docl_SetType_name}

# docl_SequenceType class attributes and methods
docl_SequenceType_name: Property = Property(name="name", type=StringType)
docl_SequenceType.attributes={docl_SequenceType_name}

# docl_OrderedSetType class attributes and methods
docl_OrderedSetType_name: Property = Property(name="name", type=StringType)
docl_OrderedSetType.attributes={docl_OrderedSetType_name}

# docl_BagType class attributes and methods
docl_BagType_name: Property = Property(name="name", type=StringType)
docl_BagType.attributes={docl_BagType_name}

# docl_IterateExp class attributes and methods

# docl_IntegerType class attributes and methods
docl_IntegerType_name: Property = Property(name="name", type=StringType)
docl_IntegerType.attributes={docl_IntegerType_name}

# docl_BooleanType class attributes and methods
docl_BooleanType_name: Property = Property(name="name", type=StringType)
docl_BooleanType.attributes={docl_BooleanType_name}

# docl_StringType class attributes and methods
docl_StringType_name: Property = Property(name="name", type=StringType)
docl_StringType.attributes={docl_StringType_name}

# docl_BoolOpCallExp class attributes and methods

# docl_EqOpCallExp class attributes and methods

# docl_ComOpCallExp class attributes and methods

# docl_AddOpCallExp class attributes and methods

# docl_MulOpCallExp class attributes and methods

# docl_NavigationExp class attributes and methods

# docl_CollectionOpCallExp class attributes and methods

# docl_NestedExp class attributes and methods

# docl_IteratorExp class attributes and methods

# docl_NavigationOrAttributeCall class attributes and methods
docl_NavigationOrAttributeCall_feature: Property = Property(name="feature", type=StringType)
docl_NavigationOrAttributeCall.attributes={docl_NavigationOrAttributeCall_feature}

# docl_OperationCall class attributes and methods

# docl_LambdaExp class attributes and methods

# docl_TupleExp class attributes and methods

# docl_ElseIfThenExp class attributes and methods

# docl_SelfExp class attributes and methods

# Relationships
elements6: BinaryAssociation = BinaryAssociation(
    name="elements6",
    ends={
        Property(name="docl_ModuleElement", type=docl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_Module7", type=docl_ModuleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source0: BinaryAssociation = BinaryAssociation(
    name="source0",
    ends={
        Property(name="docl_OclModel", type=docl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_Module", type=docl_OclModel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
input1: BinaryAssociation = BinaryAssociation(
    name="input1",
    ends={
        Property(name="docl_OclModel3", type=docl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_Module2", type=docl_OclModel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
imports4: BinaryAssociation = BinaryAssociation(
    name="imports4",
    ends={
        Property(name="docl_Import", type=docl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_Module5", type=docl_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initExp26: BinaryAssociation = BinaryAssociation(
    name="initExp26",
    ends={
        Property(name="docl_OclExpression28", type=docl_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_LocalVariable27", type=docl_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
uri8: BinaryAssociation = BinaryAssociation(
    name="uri8",
    ends={
        Property(name="docl_URI_", type=docl_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_OclModel9", type=docl_URI_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body10: BinaryAssociation = BinaryAssociation(
    name="body10",
    ends={
        Property(name="docl_OclExpression", type=docl_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_Query", type=docl_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable11: BinaryAssociation = BinaryAssociation(
    name="variable11",
    ends={
        Property(name="docl_LocalVariable", type=docl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_OclExpression12", type=docl_LocalVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
in14: BinaryAssociation = BinaryAssociation(
    name="in14",
    ends={
        Property(name="docl_OclExpression15", type=docl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_OclExpression13", type=docl_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target17: BinaryAssociation = BinaryAssociation(
    name="target17",
    ends={
        Property(name="docl_OclExpression18", type=docl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_OclExpression16", type=docl_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
model19: BinaryAssociation = BinaryAssociation(
    name="model19",
    ends={
        Property(name="docl_OclModel21", type=docl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_OclExpression20", type=docl_OclModel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type22: BinaryAssociation = BinaryAssociation(
    name="type22",
    ends={
        Property(name="docl_OclType", type=docl_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_Iterator", type=docl_OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type23: BinaryAssociation = BinaryAssociation(
    name="type23",
    ends={
        Property(name="docl_OclType25", type=docl_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_LocalVariable24", type=docl_OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type29: BinaryAssociation = BinaryAssociation(
    name="type29",
    ends={
        Property(name="docl_OclType30", type=docl_TuplePart, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_TuplePart", type=docl_OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init31: BinaryAssociation = BinaryAssociation(
    name="init31",
    ends={
        Property(name="docl_OclExpression33", type=docl_TuplePart, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_TuplePart32", type=docl_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition34: BinaryAssociation = BinaryAssociation(
    name="condition34",
    ends={
        Property(name="docl_OclExpression35", type=docl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_IfExp", type=docl_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then36: BinaryAssociation = BinaryAssociation(
    name="then36",
    ends={
        Property(name="docl_OclExpression38", type=docl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_IfExp37", type=docl_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifThen39: BinaryAssociation = BinaryAssociation(
    name="ifThen39",
    ends={
        Property(name="docl_OclExpression41", type=docl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_IfExp40", type=docl_OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
else42: BinaryAssociation = BinaryAssociation(
    name="else42",
    ends={
        Property(name="docl_OclExpression44", type=docl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_IfExp43", type=docl_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
model45: BinaryAssociation = BinaryAssociation(
    name="model45",
    ends={
        Property(name="docl_OclModel46", type=docl_OclModelElementExp, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_OclModelElementExp", type=docl_OclModel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argsTypes47: BinaryAssociation = BinaryAssociation(
    name="argsTypes47",
    ends={
        Property(name="docl_OclType48", type=docl_LambdaType, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_LambdaType", type=docl_OclType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType49: BinaryAssociation = BinaryAssociation(
    name="returnType49",
    ends={
        Property(name="docl_OclType51", type=docl_LambdaType, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_LambdaType50", type=docl_OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
keyType52: BinaryAssociation = BinaryAssociation(
    name="keyType52",
    ends={
        Property(name="docl_OclType53", type=docl_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_MapType", type=docl_OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
valueType54: BinaryAssociation = BinaryAssociation(
    name="valueType54",
    ends={
        Property(name="docl_OclType56", type=docl_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_MapType55", type=docl_OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elementType57: BinaryAssociation = BinaryAssociation(
    name="elementType57",
    ends={
        Property(name="docl_OclType58", type=docl_SetType, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_SetType", type=docl_OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elementType59: BinaryAssociation = BinaryAssociation(
    name="elementType59",
    ends={
        Property(name="docl_OclType60", type=docl_SequenceType, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_SequenceType", type=docl_OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elementType61: BinaryAssociation = BinaryAssociation(
    name="elementType61",
    ends={
        Property(name="docl_OclType62", type=docl_OrderedSetType, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_OrderedSetType", type=docl_OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elementType63: BinaryAssociation = BinaryAssociation(
    name="elementType63",
    ends={
        Property(name="docl_OclType64", type=docl_BagType, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_BagType", type=docl_OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iterators79: BinaryAssociation = BinaryAssociation(
    name="iterators79",
    ends={
        Property(name="docl_Iterator80", type=docl_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_IterateExp", type=docl_Iterator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source65: BinaryAssociation = BinaryAssociation(
    name="source65",
    ends={
        Property(name="docl_OclExpression66", type=docl_BoolOpCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_BoolOpCallExp", type=docl_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source67: BinaryAssociation = BinaryAssociation(
    name="source67",
    ends={
        Property(name="docl_OclExpression68", type=docl_EqOpCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_EqOpCallExp", type=docl_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source69: BinaryAssociation = BinaryAssociation(
    name="source69",
    ends={
        Property(name="docl_OclExpression70", type=docl_ComOpCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_ComOpCallExp", type=docl_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source71: BinaryAssociation = BinaryAssociation(
    name="source71",
    ends={
        Property(name="docl_OclExpression72", type=docl_AddOpCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_AddOpCallExp", type=docl_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source73: BinaryAssociation = BinaryAssociation(
    name="source73",
    ends={
        Property(name="docl_OclExpression74", type=docl_MulOpCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_MulOpCallExp", type=docl_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source75: BinaryAssociation = BinaryAssociation(
    name="source75",
    ends={
        Property(name="docl_OclExpression76", type=docl_NavigationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_NavigationExp", type=docl_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments77: BinaryAssociation = BinaryAssociation(
    name="arguments77",
    ends={
        Property(name="docl_OclExpression78", type=docl_CollectionOpCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_CollectionOpCallExp", type=docl_OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp103: BinaryAssociation = BinaryAssociation(
    name="exp103",
    ends={
        Property(name="docl_OclExpression104", type=docl_NestedExp, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_NestedExp", type=docl_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result81: BinaryAssociation = BinaryAssociation(
    name="result81",
    ends={
        Property(name="docl_LocalVariable83", type=docl_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_IterateExp82", type=docl_LocalVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body84: BinaryAssociation = BinaryAssociation(
    name="body84",
    ends={
        Property(name="docl_OclExpression86", type=docl_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_IterateExp85", type=docl_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iterators87: BinaryAssociation = BinaryAssociation(
    name="iterators87",
    ends={
        Property(name="docl_Iterator88", type=docl_IteratorExp, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_IteratorExp", type=docl_Iterator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body89: BinaryAssociation = BinaryAssociation(
    name="body89",
    ends={
        Property(name="docl_OclExpression91", type=docl_IteratorExp, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_IteratorExp90", type=docl_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments92: BinaryAssociation = BinaryAssociation(
    name="arguments92",
    ends={
        Property(name="docl_OclExpression93", type=docl_OperationCall, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_OperationCall", type=docl_OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression94: BinaryAssociation = BinaryAssociation(
    name="expression94",
    ends={
        Property(name="docl_OclExpression95", type=docl_LambdaExp, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_LambdaExp", type=docl_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parts96: BinaryAssociation = BinaryAssociation(
    name="parts96",
    ends={
        Property(name="docl_TuplePart97", type=docl_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_TupleExp", type=docl_TuplePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition98: BinaryAssociation = BinaryAssociation(
    name="condition98",
    ends={
        Property(name="docl_OclExpression99", type=docl_ElseIfThenExp, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_ElseIfThenExp", type=docl_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then100: BinaryAssociation = BinaryAssociation(
    name="then100",
    ends={
        Property(name="docl_OclExpression102", type=docl_ElseIfThenExp, multiplicity=Multiplicity(1, 1)),
        Property(name="docl_ElseIfThenExp101", type=docl_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_docl_Query_ModuleElement = Generalization(general=ModuleElement, specific=docl_Query)
gen_docl_LambdaType_OclType = Generalization(general=OclType, specific=docl_LambdaType)
gen_docl_PrimitiveExp_OclExpression = Generalization(general=OclExpression, specific=docl_PrimitiveExp)
gen_docl_NumberLiteralExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=docl_NumberLiteralExp)
gen_docl_StringLiteralExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=docl_StringLiteralExp)
gen_docl_BooleanLiteralExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=docl_BooleanLiteralExp)
gen_docl_UnlimitedNaturalLiteralExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=docl_UnlimitedNaturalLiteralExp)
gen_docl_InvalidLiteralExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=docl_InvalidLiteralExp)
gen_docl_NullLiteralExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=docl_NullLiteralExp)
gen_docl_IfExp_OclExpression = Generalization(general=OclExpression, specific=docl_IfExp)
gen_docl_OclModelElementExp_OclType = Generalization(general=OclType, specific=docl_OclModelElementExp)
gen_docl_EnvType_OclType = Generalization(general=OclType, specific=docl_EnvType)
gen_docl_RealType_OclType = Generalization(general=OclType, specific=docl_RealType)
gen_docl_MapType_OclType = Generalization(general=OclType, specific=docl_MapType)
gen_docl_TupleType_OclType = Generalization(general=OclType, specific=docl_TupleType)
gen_docl_OclAnyType_OclType = Generalization(general=OclType, specific=docl_OclAnyType)
gen_docl_SetType_OclType = Generalization(general=OclType, specific=docl_SetType)
gen_docl_SequenceType_OclType = Generalization(general=OclType, specific=docl_SequenceType)
gen_docl_OrderedSetType_OclType = Generalization(general=OclType, specific=docl_OrderedSetType)
gen_docl_BagType_OclType = Generalization(general=OclType, specific=docl_BagType)
gen_docl_IterateExp_OclExpression = Generalization(general=OclExpression, specific=docl_IterateExp)
gen_docl_IntegerType_OclType = Generalization(general=OclType, specific=docl_IntegerType)
gen_docl_BooleanType_OclType = Generalization(general=OclType, specific=docl_BooleanType)
gen_docl_StringType_OclType = Generalization(general=OclType, specific=docl_StringType)
gen_docl_BoolOpCallExp_OclExpression = Generalization(general=OclExpression, specific=docl_BoolOpCallExp)
gen_docl_EqOpCallExp_OclExpression = Generalization(general=OclExpression, specific=docl_EqOpCallExp)
gen_docl_ComOpCallExp_OclExpression = Generalization(general=OclExpression, specific=docl_ComOpCallExp)
gen_docl_AddOpCallExp_OclExpression = Generalization(general=OclExpression, specific=docl_AddOpCallExp)
gen_docl_MulOpCallExp_OclExpression = Generalization(general=OclExpression, specific=docl_MulOpCallExp)
gen_docl_NavigationExp_OclExpression = Generalization(general=OclExpression, specific=docl_NavigationExp)
gen_docl_CollectionOpCallExp_OclExpression = Generalization(general=OclExpression, specific=docl_CollectionOpCallExp)
gen_docl_NestedExp_OclExpression = Generalization(general=OclExpression, specific=docl_NestedExp)
gen_docl_IteratorExp_OclExpression = Generalization(general=OclExpression, specific=docl_IteratorExp)
gen_docl_NavigationOrAttributeCall_OclExpression = Generalization(general=OclExpression, specific=docl_NavigationOrAttributeCall)
gen_docl_OperationCall_OclExpression = Generalization(general=OclExpression, specific=docl_OperationCall)
gen_docl_LambdaExp_OclExpression = Generalization(general=OclExpression, specific=docl_LambdaExp)
gen_docl_TupleExp_OclExpression = Generalization(general=OclExpression, specific=docl_TupleExp)
gen_docl_ElseIfThenExp_OclExpression = Generalization(general=OclExpression, specific=docl_ElseIfThenExp)
gen_docl_SelfExp_OclExpression = Generalization(general=OclExpression, specific=docl_SelfExp)

# Domain Model
domain_model = DomainModel(
    name="docl",
    types={docl_ModuleElement, docl_Module, docl_OclModel, docl_Import, docl_TuplePart, docl_URI_, docl_Query, ModuleElement, docl_OclExpression, docl_LocalVariable, docl_Iterator, docl_OclType, docl_LambdaType, docl_PrimitiveExp, OclExpression, docl_NumberLiteralExp, PrimitiveExp, docl_StringLiteralExp, docl_BooleanLiteralExp, docl_UnlimitedNaturalLiteralExp, docl_InvalidLiteralExp, docl_NullLiteralExp, docl_IfExp, docl_OclModelElementExp, OclType, docl_EnvType, docl_RealType, docl_MapType, docl_TupleType, docl_OclAnyType, docl_SetType, docl_SequenceType, docl_OrderedSetType, docl_BagType, docl_IterateExp, docl_IntegerType, docl_BooleanType, docl_StringType, docl_BoolOpCallExp, docl_EqOpCallExp, docl_ComOpCallExp, docl_AddOpCallExp, docl_MulOpCallExp, docl_NavigationExp, docl_CollectionOpCallExp, docl_NestedExp, docl_IteratorExp, docl_NavigationOrAttributeCall, docl_OperationCall, docl_LambdaExp, docl_TupleExp, docl_ElseIfThenExp, docl_SelfExp},
    associations={elements6, source0, input1, imports4, initExp26, uri8, body10, variable11, in14, target17, model19, type22, type23, type29, init31, condition34, then36, ifThen39, else42, model45, argsTypes47, returnType49, keyType52, valueType54, elementType57, elementType59, elementType61, elementType63, iterators79, source65, source67, source69, source71, source73, source75, arguments77, exp103, result81, body84, iterators87, body89, arguments92, expression94, parts96, condition98, then100},
    generalizations={gen_docl_Query_ModuleElement, gen_docl_LambdaType_OclType, gen_docl_PrimitiveExp_OclExpression, gen_docl_NumberLiteralExp_PrimitiveExp, gen_docl_StringLiteralExp_PrimitiveExp, gen_docl_BooleanLiteralExp_PrimitiveExp, gen_docl_UnlimitedNaturalLiteralExp_PrimitiveExp, gen_docl_InvalidLiteralExp_PrimitiveExp, gen_docl_NullLiteralExp_PrimitiveExp, gen_docl_IfExp_OclExpression, gen_docl_OclModelElementExp_OclType, gen_docl_EnvType_OclType, gen_docl_RealType_OclType, gen_docl_MapType_OclType, gen_docl_TupleType_OclType, gen_docl_OclAnyType_OclType, gen_docl_SetType_OclType, gen_docl_SequenceType_OclType, gen_docl_OrderedSetType_OclType, gen_docl_BagType_OclType, gen_docl_IterateExp_OclExpression, gen_docl_IntegerType_OclType, gen_docl_BooleanType_OclType, gen_docl_StringType_OclType, gen_docl_BoolOpCallExp_OclExpression, gen_docl_EqOpCallExp_OclExpression, gen_docl_ComOpCallExp_OclExpression, gen_docl_AddOpCallExp_OclExpression, gen_docl_MulOpCallExp_OclExpression, gen_docl_NavigationExp_OclExpression, gen_docl_CollectionOpCallExp_OclExpression, gen_docl_NestedExp_OclExpression, gen_docl_IteratorExp_OclExpression, gen_docl_NavigationOrAttributeCall_OclExpression, gen_docl_OperationCall_OclExpression, gen_docl_LambdaExp_OclExpression, gen_docl_TupleExp_OclExpression, gen_docl_ElseIfThenExp_OclExpression, gen_docl_SelfExp_OclExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)