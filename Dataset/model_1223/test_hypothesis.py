import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    express::core::DomainConstraint,
    TypeElement,
    express::core::UniqueRule,
    core::ConcreteType,
    SimpleType,
    express::core::NumericType,
    express::core::Attribute,
    Relationship,
    InverseAttribute,
    SchemaElement,
    InterfacedElement,
    Remark,
    express::core::DataType,
    Schema,
    express::core::InterfacedElement,
    core::ParameterType,
    core::InstantiableType,
    core::NamedType,
    express::core::DefinedType,
    express::core::EntityType,
    Role,
    express::core::DomainRole,
    Redeclaration,
    AttributeType,
    express::core::Redeclaration,
    ConcreteAggregationType,
    express::core::LISTType,
    UniqueRule,
    RangeRole,
    DefinedType,
    express::core::EnumerationType,
    InvertibleAttribute,
    DomainRole,
    DataType,
    express::core::PartialEntityType,
    Scope,
    express::core::Schema,
    Instance,
    express::core::Expression,
    InstantiableType,
    express::core::ConcreteType,
    core::AggregationType,
    core::GeneralizedType,
    express::core::GeneralAggregationType,
    core::TypeElement,
    core::DomainConstraint,
    express::core::DomainRule,
    SingleEntityValue,
    express::instances::PartialEntityValue,
    express::instances::ConcreteValue,
    instances::AggregateValue,
    core::Instance,
    express::instances::LISTValue,
    LogicalValue,
    express::instances::BooleanValue,
    NumberValue,
    express::instances::RealValue,
    express::instances::Population,
    express::instances::ArrayMember,
    instances::ConcreteValue,
    instances::TypedInstance,
    express::instances::EnumerationItem,
    BagMember,
    LISTValue,
    express::instances::GenericAggregate,
    express::instances::Indeterminate,
    express::instances::SingleEntityValue,
    express::instances::BagMember,
    express::instances::ListMember,
    EntityValue,
    TypedInstance,
    express::instances::SpecializedValue,
    express::instances::EntityInstance,
    StringValue,
    express::instances::TypeName,
    express::instances::RoleName,
    ArrayMember,
    AggregateValue,
    express::instances::BAGValue,
    express::instances::SETValue,
    express::instances::ARRAYValue,
    express::instances::AttributeValue,
    core::GenericType,
    algorithms::Parameter,
    express::instances::TypedInstance,
    ConcreteValue,
    express::instances::SimpleValue,
    express::instances::AggregateValue,
    RealValue,
    express::instances::IntegerValue,
    AGGREGATEType,
    express::algorithms::ActualStructureConstraint,
    ActualStructure,
    express::algorithms::VARVariable,
    core::ActualType,
    express::algorithms::ActualAggregationType,
    EscapeStatement,
    SkipStatement,
    StatementBlock,
    express::algorithms::Statement,
    ActualType,
    express::algorithms::ActualAGGREGATEType,
    express::algorithms::ActualGenericType,
    core::AGGREGATEType,
    algorithms::GenericElement,
    express::algorithms::ActualDataType,
    express::algorithms::ActualStructure,
    InVariable,
    ActualDataType,
    GenericType,
    ActualAggregationType,
    express::algorithms::ActualBAGType,
    express::algorithms::ActualSETType,
    express::algorithms::ActualLISTType,
    express::algorithms::ActualARRAYType,
    InParameter,
    RepeatStatement,
    core::AnonymousType,
    express::core::ConcreteAggregationType,
    AlgorithmScope,
    express::core::CommonElement,
    Algorithm,
    express::algorithms::Procedure,
    express::algorithms::Function,
    express::algorithms::ActualTypeConstraint,
    express::core::ARRAYType,
    express::core::AggregationType,
    express::core::ScopedId,
    express::core::BinaryType,
    DomainRule,
    SelectType,
    core::CommonElement,
    core::Scope,
    express::core::LocalScope,
    express::core::Relationship,
    express::core::SelectType,
    express::core::ParameterType,
    express::core::Scope,
    express::core::Role,
    express::core::Remark,
    express::core::RangeRole,
    ArrayBound,
    ConcreteType,
    express::core::SpecializedType,
    express::core::SETType,
    LocalScope,
    express::core::AlgorithmScope,
    AnonymousType,
    express::core::SimpleType,
    express::core::AnonymousType,
    LengthConstraint,
    express::core::StringType,
    ActualTypeConstraint,
    express::core::LogicType,
    NumericType,
    express::core::RealType,
    express::core::BAGType,
    DomainConstraint,
    express::core::LengthConstraint,
    express::core::SizeConstraint,
    express::core::AttributeType,
    express::core::Instance,
    express::core::NamedElement,
    core::VariableType,
    express::core::InstantiableType,
    GeneralAggregationType,
    express::core::GeneralLISTType,
    express::core::GeneralSETType,
    express::core::GeneralARRAYType,
    express::core::GeneralBAGType,
    ActualStructureConstraint,
    ParameterType,
    express::core::ArrayBound,
    core::AttributeType,
    express::core::NamedType,
    express::core::GeneralizedType,
    core::DataType,
    express::core::VariableType,
    EnumerationType,
    NamedType,
    ListMember,
    RepeatCount,
    express::expressions::MemberBinding,
    FunctionResult,
    Function,
    SizeConstraint,
    GeneralizedType,
    express::core::GenericType,
    express::core::AGGREGATEType,
    PartialEntityType,
    express::core::SingleEntityType,
    NamedElement,
    express::core::LocalElement,
    express::core::SchemaElement,
    express::core::TypeElement,
    core::Expression,
    Constant,
    Attribute,
    express::core::DerivedAttribute,
    express::core::InverseAttribute,
    express::core::ExplicitAttribute,
    Selector,
    express::expressions::UsedInRef,
    express::expressions::GroupRef,
    express::expressions::AttributeRef,
    AttributeValue,
    express::expressions::AttributeBinding,
    QueryVariable,
    VariableType,
    express::core::ActualType,
    AttributeBinding,
    PartialEntityValue,
    express::instances::EntityValue,
    MemberBinding,
    GenericAggregate,
    Operation,
    express::expressions::UnaryOperation,
    express::expressions::Coercion,
    express::expressions::BinaryOperation,
    Parameter,
    express::algorithms::InParameter,
    FunctionCall,
    ProcedureCall,
    express::expressions::ActualParameter,
    IndexOperation,
    express::expressions::StringIndex,
    express::expressions::AggregateIndex,
    express::expressions::BinaryIndex,
    SimpleValue,
    express::instances::BinaryValue,
    express::instances::NumberValue,
    express::instances::LogicalValue,
    express::instances::StringValue,
    EnumerationItem,
    Primary,
    express::expressions::ExtentRef,
    express::expressions::Literal,
    express::expressions::VariableRef,
    express::expressions::ConstantRef,
    express::expressions::IndeterminateRef,
    express::expressions::ParameterRef,
    express::expressions::EnumItemRef,
    express::expressions::RepeatCount,
    express::expressions::SELFRef,
    Indeterminate,
    CaseAction,
    Variable,
    express::algorithms::InVariable,
    express::algorithms::FunctionResult,
    express::algorithms::LocalVariable,
    SingleEntityType,
    ControlVariable,
    ExplicitAttribute,
    express::core::InvertibleAttribute,
    express::statements::VARExpression,
    VARVariable,
    algorithms::VARVariable,
    express::algorithms::VARParameter,
    algorithms::NamedVariable,
    express::statements::AliasVariable,
    NamedVariable,
    express::algorithms::Variable,
    express::expressions::QueryVariable,
    express::statements::ControlVariable,
    AliasVariable,
    VARExpression,
    express::statements::VariableCell,
    express::statements::GroupCell,
    express::statements::AttributeCell,
    express::statements::VARCell,
    express::statements::MemberCell,
    core::LocalScope,
    express::expressions::QueryExpression,
    algorithms::Statement,
    express::statements::RepeatStatement,
    express::statements::AliasStatement,
    ControlStatement,
    express::statements::NullStatement,
    express::statements::EscapeStatement,
    express::statements::ReturnStatement,
    express::statements::SkipStatement,
    express::statements::CaseAction,
    LocalElement,
    express::algorithms::NamedVariable,
    express::algorithms::GenericElement,
    express::algorithms::Parameter,
    express::rules::NamedRule,
    NamedRule,
    Statement,
    express::statements::CaseStatement,
    express::statements::Assignment,
    express::statements::StatementBlock,
    express::statements::ControlStatement,
    express::statements::IfStatement,
    core::AlgorithmScope,
    express::algorithms::Algorithm,
    core::SchemaElement,
    express::rules::GlobalRule,
    ScopedId,
    GlobalRule,
    Population,
    EntityInstance,
    express::instances::SingleLeafInstance,
    express::instances::MultiLeafInstance,
    SETValue,
    express::rules::Extent,
    SupertypeRule,
    Expression,
    express::expressions::Primary,
    express::expressions::AggregateInitializer,
    express::expressions::Selector,
    express::expressions::FunctionCall,
    express::expressions::Operation,
    express::expressions::IndexOperation,
    express::expressions::PartialEntityConstructor,
    Extent,
    express::rules::SubtypeConstraint,
    ActualParameter,
    Procedure,
    express::statements::ProcedureCall,
    EntityType,
    CommonElement,
    express::instances::Constant,
    express::rules::SupertypeRule,
    SubtypeConstraint,
    express::rules::ANDConstraint,
    express::rules::TOTAL::OVERConstraint,
    express::rules::ONEOFConstraint,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_express::core::domainconstraint_is_not_abstract():
    assert not inspect.isabstract(express::core::DomainConstraint)


def test_express::core::domainconstraint_constructor_exists():
    assert callable(express::core::DomainConstraint.__init__)


def test_express::core::domainconstraint_constructor_args():
    sig = inspect.signature(express::core::DomainConstraint.__init__)
    params = list(sig.parameters.keys())



def test_typeelement_is_not_abstract():
    assert not inspect.isabstract(TypeElement)


def test_typeelement_constructor_exists():
    assert callable(TypeElement.__init__)


def test_typeelement_constructor_args():
    sig = inspect.signature(TypeElement.__init__)
    params = list(sig.parameters.keys())



def test_express::core::uniquerule_is_not_abstract():
    assert not inspect.isabstract(express::core::UniqueRule)


def test_express::core::uniquerule_constructor_exists():
    assert callable(express::core::UniqueRule.__init__)


def test_express::core::uniquerule_constructor_args():
    sig = inspect.signature(express::core::UniqueRule.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_express::core::uniquerule_has_position():
    assert hasattr(express::core::UniqueRule, "position")
    descriptor = None
    for klass in express::core::UniqueRule.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_core::concretetype_is_not_abstract():
    assert not inspect.isabstract(core::ConcreteType)


def test_core::concretetype_constructor_exists():
    assert callable(core::ConcreteType.__init__)


def test_core::concretetype_constructor_args():
    sig = inspect.signature(core::ConcreteType.__init__)
    params = list(sig.parameters.keys())



def test_simpletype_is_not_abstract():
    assert not inspect.isabstract(SimpleType)


def test_simpletype_constructor_exists():
    assert callable(SimpleType.__init__)


def test_simpletype_constructor_args():
    sig = inspect.signature(SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_express::core::numerictype_is_not_abstract():
    assert not inspect.isabstract(express::core::NumericType)


def test_express::core::numerictype_constructor_exists():
    assert callable(express::core::NumericType.__init__)


def test_express::core::numerictype_constructor_args():
    sig = inspect.signature(express::core::NumericType.__init__)
    params = list(sig.parameters.keys())



def test_express::core::attribute_is_not_abstract():
    assert not inspect.isabstract(express::core::Attribute)


def test_express::core::attribute_constructor_exists():
    assert callable(express::core::Attribute.__init__)


def test_express::core::attribute_constructor_args():
    sig = inspect.signature(express::core::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_express::core::attribute_has_position():
    assert hasattr(express::core::Attribute, "position")
    descriptor = None
    for klass in express::core::Attribute.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_express::core::attribute_has_isAbstract():
    assert hasattr(express::core::Attribute, "isAbstract")
    descriptor = None
    for klass in express::core::Attribute.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_relationship_is_not_abstract():
    assert not inspect.isabstract(Relationship)


def test_relationship_constructor_exists():
    assert callable(Relationship.__init__)


def test_relationship_constructor_args():
    sig = inspect.signature(Relationship.__init__)
    params = list(sig.parameters.keys())



def test_inverseattribute_is_not_abstract():
    assert not inspect.isabstract(InverseAttribute)


def test_inverseattribute_constructor_exists():
    assert callable(InverseAttribute.__init__)


def test_inverseattribute_constructor_args():
    sig = inspect.signature(InverseAttribute.__init__)
    params = list(sig.parameters.keys())



def test_schemaelement_is_not_abstract():
    assert not inspect.isabstract(SchemaElement)


def test_schemaelement_constructor_exists():
    assert callable(SchemaElement.__init__)


def test_schemaelement_constructor_args():
    sig = inspect.signature(SchemaElement.__init__)
    params = list(sig.parameters.keys())



def test_interfacedelement_is_not_abstract():
    assert not inspect.isabstract(InterfacedElement)


def test_interfacedelement_constructor_exists():
    assert callable(InterfacedElement.__init__)


def test_interfacedelement_constructor_args():
    sig = inspect.signature(InterfacedElement.__init__)
    params = list(sig.parameters.keys())



def test_remark_is_not_abstract():
    assert not inspect.isabstract(Remark)


def test_remark_constructor_exists():
    assert callable(Remark.__init__)


def test_remark_constructor_args():
    sig = inspect.signature(Remark.__init__)
    params = list(sig.parameters.keys())



def test_express::core::datatype_is_not_abstract():
    assert not inspect.isabstract(express::core::DataType)


def test_express::core::datatype_constructor_exists():
    assert callable(express::core::DataType.__init__)


def test_express::core::datatype_constructor_args():
    sig = inspect.signature(express::core::DataType.__init__)
    params = list(sig.parameters.keys())



def test_schema_is_not_abstract():
    assert not inspect.isabstract(Schema)


def test_schema_constructor_exists():
    assert callable(Schema.__init__)


def test_schema_constructor_args():
    sig = inspect.signature(Schema.__init__)
    params = list(sig.parameters.keys())



def test_express::core::interfacedelement_is_not_abstract():
    assert not inspect.isabstract(express::core::InterfacedElement)


def test_express::core::interfacedelement_constructor_exists():
    assert callable(express::core::InterfacedElement.__init__)


def test_express::core::interfacedelement_constructor_args():
    sig = inspect.signature(express::core::InterfacedElement.__init__)
    params = list(sig.parameters.keys())
    assert "isUSE" in params, "Missing parameter 'isUSE'"

def test_express::core::interfacedelement_has_isUSE():
    assert hasattr(express::core::InterfacedElement, "isUSE")
    descriptor = None
    for klass in express::core::InterfacedElement.__mro__:
        if "isUSE" in klass.__dict__:
            descriptor = klass.__dict__["isUSE"]
            break
    assert isinstance(descriptor, property)



def test_core::parametertype_is_not_abstract():
    assert not inspect.isabstract(core::ParameterType)


def test_core::parametertype_constructor_exists():
    assert callable(core::ParameterType.__init__)


def test_core::parametertype_constructor_args():
    sig = inspect.signature(core::ParameterType.__init__)
    params = list(sig.parameters.keys())



def test_core::instantiabletype_is_not_abstract():
    assert not inspect.isabstract(core::InstantiableType)


def test_core::instantiabletype_constructor_exists():
    assert callable(core::InstantiableType.__init__)


def test_core::instantiabletype_constructor_args():
    sig = inspect.signature(core::InstantiableType.__init__)
    params = list(sig.parameters.keys())



def test_core::namedtype_is_not_abstract():
    assert not inspect.isabstract(core::NamedType)


def test_core::namedtype_constructor_exists():
    assert callable(core::NamedType.__init__)


def test_core::namedtype_constructor_args():
    sig = inspect.signature(core::NamedType.__init__)
    params = list(sig.parameters.keys())



def test_express::core::definedtype_is_not_abstract():
    assert not inspect.isabstract(express::core::DefinedType)


def test_express::core::definedtype_constructor_exists():
    assert callable(express::core::DefinedType.__init__)


def test_express::core::definedtype_constructor_args():
    sig = inspect.signature(express::core::DefinedType.__init__)
    params = list(sig.parameters.keys())



def test_express::core::entitytype_is_not_abstract():
    assert not inspect.isabstract(express::core::EntityType)


def test_express::core::entitytype_constructor_exists():
    assert callable(express::core::EntityType.__init__)


def test_express::core::entitytype_constructor_args():
    sig = inspect.signature(express::core::EntityType.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_express::core::entitytype_has_isAbstract():
    assert hasattr(express::core::EntityType, "isAbstract")
    descriptor = None
    for klass in express::core::EntityType.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_role_is_not_abstract():
    assert not inspect.isabstract(Role)


def test_role_constructor_exists():
    assert callable(Role.__init__)


def test_role_constructor_args():
    sig = inspect.signature(Role.__init__)
    params = list(sig.parameters.keys())



def test_express::core::domainrole_is_not_abstract():
    assert not inspect.isabstract(express::core::DomainRole)


def test_express::core::domainrole_constructor_exists():
    assert callable(express::core::DomainRole.__init__)


def test_express::core::domainrole_constructor_args():
    sig = inspect.signature(express::core::DomainRole.__init__)
    params = list(sig.parameters.keys())



def test_redeclaration_is_not_abstract():
    assert not inspect.isabstract(Redeclaration)


def test_redeclaration_constructor_exists():
    assert callable(Redeclaration.__init__)


def test_redeclaration_constructor_args():
    sig = inspect.signature(Redeclaration.__init__)
    params = list(sig.parameters.keys())



def test_attributetype_is_not_abstract():
    assert not inspect.isabstract(AttributeType)


def test_attributetype_constructor_exists():
    assert callable(AttributeType.__init__)


def test_attributetype_constructor_args():
    sig = inspect.signature(AttributeType.__init__)
    params = list(sig.parameters.keys())



def test_express::core::redeclaration_is_not_abstract():
    assert not inspect.isabstract(express::core::Redeclaration)


def test_express::core::redeclaration_constructor_exists():
    assert callable(express::core::Redeclaration.__init__)


def test_express::core::redeclaration_constructor_args():
    sig = inspect.signature(express::core::Redeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"

def test_express::core::redeclaration_has_position():
    assert hasattr(express::core::Redeclaration, "position")
    descriptor = None
    for klass in express::core::Redeclaration.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_express::core::redeclaration_has_isMandatory():
    assert hasattr(express::core::Redeclaration, "isMandatory")
    descriptor = None
    for klass in express::core::Redeclaration.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)



def test_concreteaggregationtype_is_not_abstract():
    assert not inspect.isabstract(ConcreteAggregationType)


def test_concreteaggregationtype_constructor_exists():
    assert callable(ConcreteAggregationType.__init__)


def test_concreteaggregationtype_constructor_args():
    sig = inspect.signature(ConcreteAggregationType.__init__)
    params = list(sig.parameters.keys())



def test_express::core::listtype_is_not_abstract():
    assert not inspect.isabstract(express::core::LISTType)


def test_express::core::listtype_constructor_exists():
    assert callable(express::core::LISTType.__init__)


def test_express::core::listtype_constructor_args():
    sig = inspect.signature(express::core::LISTType.__init__)
    params = list(sig.parameters.keys())



def test_uniquerule_is_not_abstract():
    assert not inspect.isabstract(UniqueRule)


def test_uniquerule_constructor_exists():
    assert callable(UniqueRule.__init__)


def test_uniquerule_constructor_args():
    sig = inspect.signature(UniqueRule.__init__)
    params = list(sig.parameters.keys())



def test_rangerole_is_not_abstract():
    assert not inspect.isabstract(RangeRole)


def test_rangerole_constructor_exists():
    assert callable(RangeRole.__init__)


def test_rangerole_constructor_args():
    sig = inspect.signature(RangeRole.__init__)
    params = list(sig.parameters.keys())



def test_definedtype_is_not_abstract():
    assert not inspect.isabstract(DefinedType)


def test_definedtype_constructor_exists():
    assert callable(DefinedType.__init__)


def test_definedtype_constructor_args():
    sig = inspect.signature(DefinedType.__init__)
    params = list(sig.parameters.keys())



def test_express::core::enumerationtype_is_not_abstract():
    assert not inspect.isabstract(express::core::EnumerationType)


def test_express::core::enumerationtype_constructor_exists():
    assert callable(express::core::EnumerationType.__init__)


def test_express::core::enumerationtype_constructor_args():
    sig = inspect.signature(express::core::EnumerationType.__init__)
    params = list(sig.parameters.keys())
    assert "isExtensible" in params, "Missing parameter 'isExtensible'"

def test_express::core::enumerationtype_has_isExtensible():
    assert hasattr(express::core::EnumerationType, "isExtensible")
    descriptor = None
    for klass in express::core::EnumerationType.__mro__:
        if "isExtensible" in klass.__dict__:
            descriptor = klass.__dict__["isExtensible"]
            break
    assert isinstance(descriptor, property)



def test_invertibleattribute_is_not_abstract():
    assert not inspect.isabstract(InvertibleAttribute)


def test_invertibleattribute_constructor_exists():
    assert callable(InvertibleAttribute.__init__)


def test_invertibleattribute_constructor_args():
    sig = inspect.signature(InvertibleAttribute.__init__)
    params = list(sig.parameters.keys())



def test_domainrole_is_not_abstract():
    assert not inspect.isabstract(DomainRole)


def test_domainrole_constructor_exists():
    assert callable(DomainRole.__init__)


def test_domainrole_constructor_args():
    sig = inspect.signature(DomainRole.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_express::core::partialentitytype_is_not_abstract():
    assert not inspect.isabstract(express::core::PartialEntityType)


def test_express::core::partialentitytype_constructor_exists():
    assert callable(express::core::PartialEntityType.__init__)


def test_express::core::partialentitytype_constructor_args():
    sig = inspect.signature(express::core::PartialEntityType.__init__)
    params = list(sig.parameters.keys())



def test_scope_is_not_abstract():
    assert not inspect.isabstract(Scope)


def test_scope_constructor_exists():
    assert callable(Scope.__init__)


def test_scope_constructor_args():
    sig = inspect.signature(Scope.__init__)
    params = list(sig.parameters.keys())



def test_express::core::schema_is_not_abstract():
    assert not inspect.isabstract(express::core::Schema)


def test_express::core::schema_constructor_exists():
    assert callable(express::core::Schema.__init__)


def test_express::core::schema_constructor_args():
    sig = inspect.signature(express::core::Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "version" in params, "Missing parameter 'version'"

def test_express::core::schema_has_name():
    assert hasattr(express::core::Schema, "name")
    descriptor = None
    for klass in express::core::Schema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_express::core::schema_has_version():
    assert hasattr(express::core::Schema, "version")
    descriptor = None
    for klass in express::core::Schema.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_instance_is_not_abstract():
    assert not inspect.isabstract(Instance)


def test_instance_constructor_exists():
    assert callable(Instance.__init__)


def test_instance_constructor_args():
    sig = inspect.signature(Instance.__init__)
    params = list(sig.parameters.keys())



def test_express::core::expression_is_not_abstract():
    assert not inspect.isabstract(express::core::Expression)


def test_express::core::expression_constructor_exists():
    assert callable(express::core::Expression.__init__)


def test_express::core::expression_constructor_args():
    sig = inspect.signature(express::core::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_express::core::expression_has_text():
    assert hasattr(express::core::Expression, "text")
    descriptor = None
    for klass in express::core::Expression.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_instantiabletype_is_not_abstract():
    assert not inspect.isabstract(InstantiableType)


def test_instantiabletype_constructor_exists():
    assert callable(InstantiableType.__init__)


def test_instantiabletype_constructor_args():
    sig = inspect.signature(InstantiableType.__init__)
    params = list(sig.parameters.keys())



def test_express::core::concretetype_is_not_abstract():
    assert not inspect.isabstract(express::core::ConcreteType)


def test_express::core::concretetype_constructor_exists():
    assert callable(express::core::ConcreteType.__init__)


def test_express::core::concretetype_constructor_args():
    sig = inspect.signature(express::core::ConcreteType.__init__)
    params = list(sig.parameters.keys())



def test_core::aggregationtype_is_not_abstract():
    assert not inspect.isabstract(core::AggregationType)


def test_core::aggregationtype_constructor_exists():
    assert callable(core::AggregationType.__init__)


def test_core::aggregationtype_constructor_args():
    sig = inspect.signature(core::AggregationType.__init__)
    params = list(sig.parameters.keys())



def test_core::generalizedtype_is_not_abstract():
    assert not inspect.isabstract(core::GeneralizedType)


def test_core::generalizedtype_constructor_exists():
    assert callable(core::GeneralizedType.__init__)


def test_core::generalizedtype_constructor_args():
    sig = inspect.signature(core::GeneralizedType.__init__)
    params = list(sig.parameters.keys())



def test_express::core::generalaggregationtype_is_not_abstract():
    assert not inspect.isabstract(express::core::GeneralAggregationType)


def test_express::core::generalaggregationtype_constructor_exists():
    assert callable(express::core::GeneralAggregationType.__init__)


def test_express::core::generalaggregationtype_constructor_args():
    sig = inspect.signature(express::core::GeneralAggregationType.__init__)
    params = list(sig.parameters.keys())



def test_core::typeelement_is_not_abstract():
    assert not inspect.isabstract(core::TypeElement)


def test_core::typeelement_constructor_exists():
    assert callable(core::TypeElement.__init__)


def test_core::typeelement_constructor_args():
    sig = inspect.signature(core::TypeElement.__init__)
    params = list(sig.parameters.keys())



def test_core::domainconstraint_is_not_abstract():
    assert not inspect.isabstract(core::DomainConstraint)


def test_core::domainconstraint_constructor_exists():
    assert callable(core::DomainConstraint.__init__)


def test_core::domainconstraint_constructor_args():
    sig = inspect.signature(core::DomainConstraint.__init__)
    params = list(sig.parameters.keys())



def test_express::core::domainrule_is_not_abstract():
    assert not inspect.isabstract(express::core::DomainRule)


def test_express::core::domainrule_constructor_exists():
    assert callable(express::core::DomainRule.__init__)


def test_express::core::domainrule_constructor_args():
    sig = inspect.signature(express::core::DomainRule.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_express::core::domainrule_has_position():
    assert hasattr(express::core::DomainRule, "position")
    descriptor = None
    for klass in express::core::DomainRule.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_singleentityvalue_is_not_abstract():
    assert not inspect.isabstract(SingleEntityValue)


def test_singleentityvalue_constructor_exists():
    assert callable(SingleEntityValue.__init__)


def test_singleentityvalue_constructor_args():
    sig = inspect.signature(SingleEntityValue.__init__)
    params = list(sig.parameters.keys())



def test_express::instances::partialentityvalue_is_not_abstract():
    assert not inspect.isabstract(express::instances::PartialEntityValue)


def test_express::instances::partialentityvalue_constructor_exists():
    assert callable(express::instances::PartialEntityValue.__init__)


def test_express::instances::partialentityvalue_constructor_args():
    sig = inspect.signature(express::instances::PartialEntityValue.__init__)
    params = list(sig.parameters.keys())



def test_express::instances::concretevalue_is_not_abstract():
    assert not inspect.isabstract(express::instances::ConcreteValue)


def test_express::instances::concretevalue_constructor_exists():
    assert callable(express::instances::ConcreteValue.__init__)


def test_express::instances::concretevalue_constructor_args():
    sig = inspect.signature(express::instances::ConcreteValue.__init__)
    params = list(sig.parameters.keys())



def test_instances::aggregatevalue_is_not_abstract():
    assert not inspect.isabstract(instances::AggregateValue)


def test_instances::aggregatevalue_constructor_exists():
    assert callable(instances::AggregateValue.__init__)


def test_instances::aggregatevalue_constructor_args():
    sig = inspect.signature(instances::AggregateValue.__init__)
    params = list(sig.parameters.keys())



def test_core::instance_is_not_abstract():
    assert not inspect.isabstract(core::Instance)


def test_core::instance_constructor_exists():
    assert callable(core::Instance.__init__)


def test_core::instance_constructor_args():
    sig = inspect.signature(core::Instance.__init__)
    params = list(sig.parameters.keys())



def test_express::instances::listvalue_is_not_abstract():
    assert not inspect.isabstract(express::instances::LISTValue)


def test_express::instances::listvalue_constructor_exists():
    assert callable(express::instances::LISTValue.__init__)


def test_express::instances::listvalue_constructor_args():
    sig = inspect.signature(express::instances::LISTValue.__init__)
    params = list(sig.parameters.keys())



def test_logicalvalue_is_not_abstract():
    assert not inspect.isabstract(LogicalValue)


def test_logicalvalue_constructor_exists():
    assert callable(LogicalValue.__init__)


def test_logicalvalue_constructor_args():
    sig = inspect.signature(LogicalValue.__init__)
    params = list(sig.parameters.keys())



def test_express::instances::booleanvalue_is_not_abstract():
    assert not inspect.isabstract(express::instances::BooleanValue)


def test_express::instances::booleanvalue_constructor_exists():
    assert callable(express::instances::BooleanValue.__init__)


def test_express::instances::booleanvalue_constructor_args():
    sig = inspect.signature(express::instances::BooleanValue.__init__)
    params = list(sig.parameters.keys())



def test_numbervalue_is_not_abstract():
    assert not inspect.isabstract(NumberValue)


def test_numbervalue_constructor_exists():
    assert callable(NumberValue.__init__)


def test_numbervalue_constructor_args():
    sig = inspect.signature(NumberValue.__init__)
    params = list(sig.parameters.keys())



def test_express::instances::realvalue_is_not_abstract():
    assert not inspect.isabstract(express::instances::RealValue)


def test_express::instances::realvalue_constructor_exists():
    assert callable(express::instances::RealValue.__init__)


def test_express::instances::realvalue_constructor_args():
    sig = inspect.signature(express::instances::RealValue.__init__)
    params = list(sig.parameters.keys())



def test_express::instances::population_is_not_abstract():
    assert not inspect.isabstract(express::instances::Population)


def test_express::instances::population_constructor_exists():
    assert callable(express::instances::Population.__init__)


def test_express::instances::population_constructor_args():
    sig = inspect.signature(express::instances::Population.__init__)
    params = list(sig.parameters.keys())



def test_express::instances::arraymember_is_not_abstract():
    assert not inspect.isabstract(express::instances::ArrayMember)


def test_express::instances::arraymember_constructor_exists():
    assert callable(express::instances::ArrayMember.__init__)


def test_express::instances::arraymember_constructor_args():
    sig = inspect.signature(express::instances::ArrayMember.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"

def test_express::instances::arraymember_has_index():
    assert hasattr(express::instances::ArrayMember, "index")
    descriptor = None
    for klass in express::instances::ArrayMember.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)



def test_instances::concretevalue_is_not_abstract():
    assert not inspect.isabstract(instances::ConcreteValue)


def test_instances::concretevalue_constructor_exists():
    assert callable(instances::ConcreteValue.__init__)


def test_instances::concretevalue_constructor_args():
    sig = inspect.signature(instances::ConcreteValue.__init__)
    params = list(sig.parameters.keys())



def test_instances::typedinstance_is_not_abstract():
    assert not inspect.isabstract(instances::TypedInstance)


def test_instances::typedinstance_constructor_exists():
    assert callable(instances::TypedInstance.__init__)


def test_instances::typedinstance_constructor_args():
    sig = inspect.signature(instances::TypedInstance.__init__)
    params = list(sig.parameters.keys())



def test_express::instances::enumerationitem_is_not_abstract():
    assert not inspect.isabstract(express::instances::EnumerationItem)


def test_express::instances::enumerationitem_constructor_exists():
    assert callable(express::instances::EnumerationItem.__init__)


def test_express::instances::enumerationitem_constructor_args():
    sig = inspect.signature(express::instances::EnumerationItem.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_express::instances::enumerationitem_has_position():
    assert hasattr(express::instances::EnumerationItem, "position")
    descriptor = None
    for klass in express::instances::EnumerationItem.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_bagmember_is_not_abstract():
    assert not inspect.isabstract(BagMember)


def test_bagmember_constructor_exists():
    assert callable(BagMember.__init__)


def test_bagmember_constructor_args():
    sig = inspect.signature(BagMember.__init__)
    params = list(sig.parameters.keys())



def test_listvalue_is_not_abstract():
    assert not inspect.isabstract(LISTValue)


def test_listvalue_constructor_exists():
    assert callable(LISTValue.__init__)


def test_listvalue_constructor_args():
    sig = inspect.signature(LISTValue.__init__)
    params = list(sig.parameters.keys())



def test_express::instances::genericaggregate_is_not_abstract():
    assert not inspect.isabstract(express::instances::GenericAggregate)


def test_express::instances::genericaggregate_constructor_exists():
    assert callable(express::instances::GenericAggregate.__init__)


def test_express::instances::genericaggregate_constructor_args():
    sig = inspect.signature(express::instances::GenericAggregate.__init__)
    params = list(sig.parameters.keys())



def test_express::instances::indeterminate_is_not_abstract():
    assert not inspect.isabstract(express::instances::Indeterminate)


def test_express::instances::indeterminate_constructor_exists():
    assert callable(express::instances::Indeterminate.__init__)


def test_express::instances::indeterminate_constructor_args():
    sig = inspect.signature(express::instances::Indeterminate.__init__)
    params = list(sig.parameters.keys())



def test_express::instances::singleentityvalue_is_not_abstract():
    assert not inspect.isabstract(express::instances::SingleEntityValue)


def test_express::instances::singleentityvalue_constructor_exists():
    assert callable(express::instances::SingleEntityValue.__init__)


def test_express::instances::singleentityvalue_constructor_args():
    sig = inspect.signature(express::instances::SingleEntityValue.__init__)
    params = list(sig.parameters.keys())



def test_express::instances::bagmember_is_not_abstract():
    assert not inspect.isabstract(express::instances::BagMember)


def test_express::instances::bagmember_constructor_exists():
    assert callable(express::instances::BagMember.__init__)


def test_express::instances::bagmember_constructor_args():
    sig = inspect.signature(express::instances::BagMember.__init__)
    params = list(sig.parameters.keys())
    assert "count" in params, "Missing parameter 'count'"

def test_express::instances::bagmember_has_count():
    assert hasattr(express::instances::BagMember, "count")
    descriptor = None
    for klass in express::instances::BagMember.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)



def test_express::instances::listmember_is_not_abstract():
    assert not inspect.isabstract(express::instances::ListMember)


def test_express::instances::listmember_constructor_exists():
    assert callable(express::instances::ListMember.__init__)


def test_express::instances::listmember_constructor_args():
    sig = inspect.signature(express::instances::ListMember.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_express::instances::listmember_has_position():
    assert hasattr(express::instances::ListMember, "position")
    descriptor = None
    for klass in express::instances::ListMember.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_entityvalue_is_not_abstract():
    assert not inspect.isabstract(EntityValue)


def test_entityvalue_constructor_exists():
    assert callable(EntityValue.__init__)


def test_entityvalue_constructor_args():
    sig = inspect.signature(EntityValue.__init__)
    params = list(sig.parameters.keys())



def test_typedinstance_is_not_abstract():
    assert not inspect.isabstract(TypedInstance)


def test_typedinstance_constructor_exists():
    assert callable(TypedInstance.__init__)


def test_typedinstance_constructor_args():
    sig = inspect.signature(TypedInstance.__init__)
    params = list(sig.parameters.keys())



def test_express::instances::specializedvalue_is_not_abstract():
    assert not inspect.isabstract(express::instances::SpecializedValue)


def test_express::instances::specializedvalue_constructor_exists():
    assert callable(express::instances::SpecializedValue.__init__)


def test_express::instances::specializedvalue_constructor_args():
    sig = inspect.signature(express::instances::SpecializedValue.__init__)
    params = list(sig.parameters.keys())



def test_express::instances::entityinstance_is_not_abstract():
    assert not inspect.isabstract(express::instances::EntityInstance)


def test_express::instances::entityinstance_constructor_exists():
    assert callable(express::instances::EntityInstance.__init__)


def test_express::instances::entityinstance_constructor_args():
    sig = inspect.signature(express::instances::EntityInstance.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_express::instances::entityinstance_has_id():
    assert hasattr(express::instances::EntityInstance, "id")
    descriptor = None
    for klass in express::instances::EntityInstance.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_stringvalue_is_not_abstract():
    assert not inspect.isabstract(StringValue)


def test_stringvalue_constructor_exists():
    assert callable(StringValue.__init__)


def test_stringvalue_constructor_args():
    sig = inspect.signature(StringValue.__init__)
    params = list(sig.parameters.keys())



def test_express::instances::typename_is_not_abstract():
    assert not inspect.isabstract(express::instances::TypeName)


def test_express::instances::typename_constructor_exists():
    assert callable(express::instances::TypeName.__init__)


def test_express::instances::typename_constructor_args():
    sig = inspect.signature(express::instances::TypeName.__init__)
    params = list(sig.parameters.keys())



def test_express::instances::rolename_is_not_abstract():
    assert not inspect.isabstract(express::instances::RoleName)


def test_express::instances::rolename_constructor_exists():
    assert callable(express::instances::RoleName.__init__)


def test_express::instances::rolename_constructor_args():
    sig = inspect.signature(express::instances::RoleName.__init__)
    params = list(sig.parameters.keys())



def test_arraymember_is_not_abstract():
    assert not inspect.isabstract(ArrayMember)


def test_arraymember_constructor_exists():
    assert callable(ArrayMember.__init__)


def test_arraymember_constructor_args():
    sig = inspect.signature(ArrayMember.__init__)
    params = list(sig.parameters.keys())



def test_aggregatevalue_is_not_abstract():
    assert not inspect.isabstract(AggregateValue)


def test_aggregatevalue_constructor_exists():
    assert callable(AggregateValue.__init__)


def test_aggregatevalue_constructor_args():
    sig = inspect.signature(AggregateValue.__init__)
    params = list(sig.parameters.keys())



def test_express::instances::bagvalue_is_not_abstract():
    assert not inspect.isabstract(express::instances::BAGValue)


def test_express::instances::bagvalue_constructor_exists():
    assert callable(express::instances::BAGValue.__init__)


def test_express::instances::bagvalue_constructor_args():
    sig = inspect.signature(express::instances::BAGValue.__init__)
    params = list(sig.parameters.keys())



def test_express::instances::setvalue_is_not_abstract():
    assert not inspect.isabstract(express::instances::SETValue)


def test_express::instances::setvalue_constructor_exists():
    assert callable(express::instances::SETValue.__init__)


def test_express::instances::setvalue_constructor_args():
    sig = inspect.signature(express::instances::SETValue.__init__)
    params = list(sig.parameters.keys())



def test_express::instances::arrayvalue_is_not_abstract():
    assert not inspect.isabstract(express::instances::ARRAYValue)


def test_express::instances::arrayvalue_constructor_exists():
    assert callable(express::instances::ARRAYValue.__init__)


def test_express::instances::arrayvalue_constructor_args():
    sig = inspect.signature(express::instances::ARRAYValue.__init__)
    params = list(sig.parameters.keys())



def test_express::instances::attributevalue_is_not_abstract():
    assert not inspect.isabstract(express::instances::AttributeValue)


def test_express::instances::attributevalue_constructor_exists():
    assert callable(express::instances::AttributeValue.__init__)


def test_express::instances::attributevalue_constructor_args():
    sig = inspect.signature(express::instances::AttributeValue.__init__)
    params = list(sig.parameters.keys())



def test_core::generictype_is_not_abstract():
    assert not inspect.isabstract(core::GenericType)


def test_core::generictype_constructor_exists():
    assert callable(core::GenericType.__init__)


def test_core::generictype_constructor_args():
    sig = inspect.signature(core::GenericType.__init__)
    params = list(sig.parameters.keys())



def test_algorithms::parameter_is_not_abstract():
    assert not inspect.isabstract(algorithms::Parameter)


def test_algorithms::parameter_constructor_exists():
    assert callable(algorithms::Parameter.__init__)


def test_algorithms::parameter_constructor_args():
    sig = inspect.signature(algorithms::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_express::instances::typedinstance_is_not_abstract():
    assert not inspect.isabstract(express::instances::TypedInstance)


def test_express::instances::typedinstance_constructor_exists():
    assert callable(express::instances::TypedInstance.__init__)


def test_express::instances::typedinstance_constructor_args():
    sig = inspect.signature(express::instances::TypedInstance.__init__)
    params = list(sig.parameters.keys())



def test_concretevalue_is_not_abstract():
    assert not inspect.isabstract(ConcreteValue)


def test_concretevalue_constructor_exists():
    assert callable(ConcreteValue.__init__)


def test_concretevalue_constructor_args():
    sig = inspect.signature(ConcreteValue.__init__)
    params = list(sig.parameters.keys())



def test_express::instances::simplevalue_is_not_abstract():
    assert not inspect.isabstract(express::instances::SimpleValue)


def test_express::instances::simplevalue_constructor_exists():
    assert callable(express::instances::SimpleValue.__init__)


def test_express::instances::simplevalue_constructor_args():
    sig = inspect.signature(express::instances::SimpleValue.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_express::instances::simplevalue_has_name():
    assert hasattr(express::instances::SimpleValue, "name")
    descriptor = None
    for klass in express::instances::SimpleValue.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_express::instances::aggregatevalue_is_not_abstract():
    assert not inspect.isabstract(express::instances::AggregateValue)


def test_express::instances::aggregatevalue_constructor_exists():
    assert callable(express::instances::AggregateValue.__init__)


def test_express::instances::aggregatevalue_constructor_args():
    sig = inspect.signature(express::instances::AggregateValue.__init__)
    params = list(sig.parameters.keys())



def test_realvalue_is_not_abstract():
    assert not inspect.isabstract(RealValue)


def test_realvalue_constructor_exists():
    assert callable(RealValue.__init__)


def test_realvalue_constructor_args():
    sig = inspect.signature(RealValue.__init__)
    params = list(sig.parameters.keys())



def test_express::instances::integervalue_is_not_abstract():
    assert not inspect.isabstract(express::instances::IntegerValue)


def test_express::instances::integervalue_constructor_exists():
    assert callable(express::instances::IntegerValue.__init__)


def test_express::instances::integervalue_constructor_args():
    sig = inspect.signature(express::instances::IntegerValue.__init__)
    params = list(sig.parameters.keys())



def test_aggregatetype_is_not_abstract():
    assert not inspect.isabstract(AGGREGATEType)


def test_aggregatetype_constructor_exists():
    assert callable(AGGREGATEType.__init__)


def test_aggregatetype_constructor_args():
    sig = inspect.signature(AGGREGATEType.__init__)
    params = list(sig.parameters.keys())



def test_express::algorithms::actualstructureconstraint_is_not_abstract():
    assert not inspect.isabstract(express::algorithms::ActualStructureConstraint)


def test_express::algorithms::actualstructureconstraint_constructor_exists():
    assert callable(express::algorithms::ActualStructureConstraint.__init__)


def test_express::algorithms::actualstructureconstraint_constructor_args():
    sig = inspect.signature(express::algorithms::ActualStructureConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_express::algorithms::actualstructureconstraint_has_label():
    assert hasattr(express::algorithms::ActualStructureConstraint, "label")
    descriptor = None
    for klass in express::algorithms::ActualStructureConstraint.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_actualstructure_is_not_abstract():
    assert not inspect.isabstract(ActualStructure)


def test_actualstructure_constructor_exists():
    assert callable(ActualStructure.__init__)


def test_actualstructure_constructor_args():
    sig = inspect.signature(ActualStructure.__init__)
    params = list(sig.parameters.keys())



def test_express::algorithms::varvariable_is_not_abstract():
    assert not inspect.isabstract(express::algorithms::VARVariable)


def test_express::algorithms::varvariable_constructor_exists():
    assert callable(express::algorithms::VARVariable.__init__)


def test_express::algorithms::varvariable_constructor_args():
    sig = inspect.signature(express::algorithms::VARVariable.__init__)
    params = list(sig.parameters.keys())



def test_core::actualtype_is_not_abstract():
    assert not inspect.isabstract(core::ActualType)


def test_core::actualtype_constructor_exists():
    assert callable(core::ActualType.__init__)


def test_core::actualtype_constructor_args():
    sig = inspect.signature(core::ActualType.__init__)
    params = list(sig.parameters.keys())



def test_express::algorithms::actualaggregationtype_is_not_abstract():
    assert not inspect.isabstract(express::algorithms::ActualAggregationType)


def test_express::algorithms::actualaggregationtype_constructor_exists():
    assert callable(express::algorithms::ActualAggregationType.__init__)


def test_express::algorithms::actualaggregationtype_constructor_args():
    sig = inspect.signature(express::algorithms::ActualAggregationType.__init__)
    params = list(sig.parameters.keys())



def test_escapestatement_is_not_abstract():
    assert not inspect.isabstract(EscapeStatement)


def test_escapestatement_constructor_exists():
    assert callable(EscapeStatement.__init__)


def test_escapestatement_constructor_args():
    sig = inspect.signature(EscapeStatement.__init__)
    params = list(sig.parameters.keys())



def test_skipstatement_is_not_abstract():
    assert not inspect.isabstract(SkipStatement)


def test_skipstatement_constructor_exists():
    assert callable(SkipStatement.__init__)


def test_skipstatement_constructor_args():
    sig = inspect.signature(SkipStatement.__init__)
    params = list(sig.parameters.keys())



def test_statementblock_is_not_abstract():
    assert not inspect.isabstract(StatementBlock)


def test_statementblock_constructor_exists():
    assert callable(StatementBlock.__init__)


def test_statementblock_constructor_args():
    sig = inspect.signature(StatementBlock.__init__)
    params = list(sig.parameters.keys())



def test_express::algorithms::statement_is_not_abstract():
    assert not inspect.isabstract(express::algorithms::Statement)


def test_express::algorithms::statement_constructor_exists():
    assert callable(express::algorithms::Statement.__init__)


def test_express::algorithms::statement_constructor_args():
    sig = inspect.signature(express::algorithms::Statement.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_express::algorithms::statement_has_text():
    assert hasattr(express::algorithms::Statement, "text")
    descriptor = None
    for klass in express::algorithms::Statement.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_actualtype_is_not_abstract():
    assert not inspect.isabstract(ActualType)


def test_actualtype_constructor_exists():
    assert callable(ActualType.__init__)


def test_actualtype_constructor_args():
    sig = inspect.signature(ActualType.__init__)
    params = list(sig.parameters.keys())



def test_express::algorithms::actualaggregatetype_is_not_abstract():
    assert not inspect.isabstract(express::algorithms::ActualAGGREGATEType)


def test_express::algorithms::actualaggregatetype_constructor_exists():
    assert callable(express::algorithms::ActualAGGREGATEType.__init__)


def test_express::algorithms::actualaggregatetype_constructor_args():
    sig = inspect.signature(express::algorithms::ActualAGGREGATEType.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_express::algorithms::actualaggregatetype_has_label():
    assert hasattr(express::algorithms::ActualAGGREGATEType, "label")
    descriptor = None
    for klass in express::algorithms::ActualAGGREGATEType.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_express::algorithms::actualgenerictype_is_not_abstract():
    assert not inspect.isabstract(express::algorithms::ActualGenericType)


def test_express::algorithms::actualgenerictype_constructor_exists():
    assert callable(express::algorithms::ActualGenericType.__init__)


def test_express::algorithms::actualgenerictype_constructor_args():
    sig = inspect.signature(express::algorithms::ActualGenericType.__init__)
    params = list(sig.parameters.keys())
    assert "isEntity" in params, "Missing parameter 'isEntity'"
    assert "label" in params, "Missing parameter 'label'"

def test_express::algorithms::actualgenerictype_has_isEntity():
    assert hasattr(express::algorithms::ActualGenericType, "isEntity")
    descriptor = None
    for klass in express::algorithms::ActualGenericType.__mro__:
        if "isEntity" in klass.__dict__:
            descriptor = klass.__dict__["isEntity"]
            break
    assert isinstance(descriptor, property)

def test_express::algorithms::actualgenerictype_has_label():
    assert hasattr(express::algorithms::ActualGenericType, "label")
    descriptor = None
    for klass in express::algorithms::ActualGenericType.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_core::aggregatetype_is_not_abstract():
    assert not inspect.isabstract(core::AGGREGATEType)


def test_core::aggregatetype_constructor_exists():
    assert callable(core::AGGREGATEType.__init__)


def test_core::aggregatetype_constructor_args():
    sig = inspect.signature(core::AGGREGATEType.__init__)
    params = list(sig.parameters.keys())



def test_algorithms::genericelement_is_not_abstract():
    assert not inspect.isabstract(algorithms::GenericElement)


def test_algorithms::genericelement_constructor_exists():
    assert callable(algorithms::GenericElement.__init__)


def test_algorithms::genericelement_constructor_args():
    sig = inspect.signature(algorithms::GenericElement.__init__)
    params = list(sig.parameters.keys())



def test_express::algorithms::actualdatatype_is_not_abstract():
    assert not inspect.isabstract(express::algorithms::ActualDataType)


def test_express::algorithms::actualdatatype_constructor_exists():
    assert callable(express::algorithms::ActualDataType.__init__)


def test_express::algorithms::actualdatatype_constructor_args():
    sig = inspect.signature(express::algorithms::ActualDataType.__init__)
    params = list(sig.parameters.keys())



def test_express::algorithms::actualstructure_is_not_abstract():
    assert not inspect.isabstract(express::algorithms::ActualStructure)


def test_express::algorithms::actualstructure_constructor_exists():
    assert callable(express::algorithms::ActualStructure.__init__)


def test_express::algorithms::actualstructure_constructor_args():
    sig = inspect.signature(express::algorithms::ActualStructure.__init__)
    params = list(sig.parameters.keys())



def test_invariable_is_not_abstract():
    assert not inspect.isabstract(InVariable)


def test_invariable_constructor_exists():
    assert callable(InVariable.__init__)


def test_invariable_constructor_args():
    sig = inspect.signature(InVariable.__init__)
    params = list(sig.parameters.keys())



def test_actualdatatype_is_not_abstract():
    assert not inspect.isabstract(ActualDataType)


def test_actualdatatype_constructor_exists():
    assert callable(ActualDataType.__init__)


def test_actualdatatype_constructor_args():
    sig = inspect.signature(ActualDataType.__init__)
    params = list(sig.parameters.keys())



def test_generictype_is_not_abstract():
    assert not inspect.isabstract(GenericType)


def test_generictype_constructor_exists():
    assert callable(GenericType.__init__)


def test_generictype_constructor_args():
    sig = inspect.signature(GenericType.__init__)
    params = list(sig.parameters.keys())



def test_actualaggregationtype_is_not_abstract():
    assert not inspect.isabstract(ActualAggregationType)


def test_actualaggregationtype_constructor_exists():
    assert callable(ActualAggregationType.__init__)


def test_actualaggregationtype_constructor_args():
    sig = inspect.signature(ActualAggregationType.__init__)
    params = list(sig.parameters.keys())



def test_express::algorithms::actualbagtype_is_not_abstract():
    assert not inspect.isabstract(express::algorithms::ActualBAGType)


def test_express::algorithms::actualbagtype_constructor_exists():
    assert callable(express::algorithms::ActualBAGType.__init__)


def test_express::algorithms::actualbagtype_constructor_args():
    sig = inspect.signature(express::algorithms::ActualBAGType.__init__)
    params = list(sig.parameters.keys())



def test_express::algorithms::actualsettype_is_not_abstract():
    assert not inspect.isabstract(express::algorithms::ActualSETType)


def test_express::algorithms::actualsettype_constructor_exists():
    assert callable(express::algorithms::ActualSETType.__init__)


def test_express::algorithms::actualsettype_constructor_args():
    sig = inspect.signature(express::algorithms::ActualSETType.__init__)
    params = list(sig.parameters.keys())



def test_express::algorithms::actuallisttype_is_not_abstract():
    assert not inspect.isabstract(express::algorithms::ActualLISTType)


def test_express::algorithms::actuallisttype_constructor_exists():
    assert callable(express::algorithms::ActualLISTType.__init__)


def test_express::algorithms::actuallisttype_constructor_args():
    sig = inspect.signature(express::algorithms::ActualLISTType.__init__)
    params = list(sig.parameters.keys())



def test_express::algorithms::actualarraytype_is_not_abstract():
    assert not inspect.isabstract(express::algorithms::ActualARRAYType)


def test_express::algorithms::actualarraytype_constructor_exists():
    assert callable(express::algorithms::ActualARRAYType.__init__)


def test_express::algorithms::actualarraytype_constructor_args():
    sig = inspect.signature(express::algorithms::ActualARRAYType.__init__)
    params = list(sig.parameters.keys())
    assert "isOptional" in params, "Missing parameter 'isOptional'"

def test_express::algorithms::actualarraytype_has_isOptional():
    assert hasattr(express::algorithms::ActualARRAYType, "isOptional")
    descriptor = None
    for klass in express::algorithms::ActualARRAYType.__mro__:
        if "isOptional" in klass.__dict__:
            descriptor = klass.__dict__["isOptional"]
            break
    assert isinstance(descriptor, property)



def test_inparameter_is_not_abstract():
    assert not inspect.isabstract(InParameter)


def test_inparameter_constructor_exists():
    assert callable(InParameter.__init__)


def test_inparameter_constructor_args():
    sig = inspect.signature(InParameter.__init__)
    params = list(sig.parameters.keys())



def test_repeatstatement_is_not_abstract():
    assert not inspect.isabstract(RepeatStatement)


def test_repeatstatement_constructor_exists():
    assert callable(RepeatStatement.__init__)


def test_repeatstatement_constructor_args():
    sig = inspect.signature(RepeatStatement.__init__)
    params = list(sig.parameters.keys())



def test_core::anonymoustype_is_not_abstract():
    assert not inspect.isabstract(core::AnonymousType)


def test_core::anonymoustype_constructor_exists():
    assert callable(core::AnonymousType.__init__)


def test_core::anonymoustype_constructor_args():
    sig = inspect.signature(core::AnonymousType.__init__)
    params = list(sig.parameters.keys())



def test_express::core::concreteaggregationtype_is_not_abstract():
    assert not inspect.isabstract(express::core::ConcreteAggregationType)


def test_express::core::concreteaggregationtype_constructor_exists():
    assert callable(express::core::ConcreteAggregationType.__init__)


def test_express::core::concreteaggregationtype_constructor_args():
    sig = inspect.signature(express::core::ConcreteAggregationType.__init__)
    params = list(sig.parameters.keys())



def test_algorithmscope_is_not_abstract():
    assert not inspect.isabstract(AlgorithmScope)


def test_algorithmscope_constructor_exists():
    assert callable(AlgorithmScope.__init__)


def test_algorithmscope_constructor_args():
    sig = inspect.signature(AlgorithmScope.__init__)
    params = list(sig.parameters.keys())



def test_express::core::commonelement_is_not_abstract():
    assert not inspect.isabstract(express::core::CommonElement)


def test_express::core::commonelement_constructor_exists():
    assert callable(express::core::CommonElement.__init__)


def test_express::core::commonelement_constructor_args():
    sig = inspect.signature(express::core::CommonElement.__init__)
    params = list(sig.parameters.keys())



def test_algorithm_is_not_abstract():
    assert not inspect.isabstract(Algorithm)


def test_algorithm_constructor_exists():
    assert callable(Algorithm.__init__)


def test_algorithm_constructor_args():
    sig = inspect.signature(Algorithm.__init__)
    params = list(sig.parameters.keys())



def test_express::algorithms::procedure_is_not_abstract():
    assert not inspect.isabstract(express::algorithms::Procedure)


def test_express::algorithms::procedure_constructor_exists():
    assert callable(express::algorithms::Procedure.__init__)


def test_express::algorithms::procedure_constructor_args():
    sig = inspect.signature(express::algorithms::Procedure.__init__)
    params = list(sig.parameters.keys())



def test_express::algorithms::function_is_not_abstract():
    assert not inspect.isabstract(express::algorithms::Function)


def test_express::algorithms::function_constructor_exists():
    assert callable(express::algorithms::Function.__init__)


def test_express::algorithms::function_constructor_args():
    sig = inspect.signature(express::algorithms::Function.__init__)
    params = list(sig.parameters.keys())



def test_express::algorithms::actualtypeconstraint_is_not_abstract():
    assert not inspect.isabstract(express::algorithms::ActualTypeConstraint)


def test_express::algorithms::actualtypeconstraint_constructor_exists():
    assert callable(express::algorithms::ActualTypeConstraint.__init__)


def test_express::algorithms::actualtypeconstraint_constructor_args():
    sig = inspect.signature(express::algorithms::ActualTypeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_express::algorithms::actualtypeconstraint_has_label():
    assert hasattr(express::algorithms::ActualTypeConstraint, "label")
    descriptor = None
    for klass in express::algorithms::ActualTypeConstraint.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_express::core::arraytype_is_not_abstract():
    assert not inspect.isabstract(express::core::ARRAYType)


def test_express::core::arraytype_constructor_exists():
    assert callable(express::core::ARRAYType.__init__)


def test_express::core::arraytype_constructor_args():
    sig = inspect.signature(express::core::ARRAYType.__init__)
    params = list(sig.parameters.keys())
    assert "isOptional" in params, "Missing parameter 'isOptional'"

def test_express::core::arraytype_has_isOptional():
    assert hasattr(express::core::ARRAYType, "isOptional")
    descriptor = None
    for klass in express::core::ARRAYType.__mro__:
        if "isOptional" in klass.__dict__:
            descriptor = klass.__dict__["isOptional"]
            break
    assert isinstance(descriptor, property)



def test_express::core::aggregationtype_is_not_abstract():
    assert not inspect.isabstract(express::core::AggregationType)


def test_express::core::aggregationtype_constructor_exists():
    assert callable(express::core::AggregationType.__init__)


def test_express::core::aggregationtype_constructor_args():
    sig = inspect.signature(express::core::AggregationType.__init__)
    params = list(sig.parameters.keys())
    assert "ordering" in params, "Missing parameter 'ordering'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"

def test_express::core::aggregationtype_has_ordering():
    assert hasattr(express::core::AggregationType, "ordering")
    descriptor = None
    for klass in express::core::AggregationType.__mro__:
        if "ordering" in klass.__dict__:
            descriptor = klass.__dict__["ordering"]
            break
    assert isinstance(descriptor, property)

def test_express::core::aggregationtype_has_isUnique():
    assert hasattr(express::core::AggregationType, "isUnique")
    descriptor = None
    for klass in express::core::AggregationType.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)



def test_express::core::scopedid_is_not_abstract():
    assert not inspect.isabstract(express::core::ScopedId)


def test_express::core::scopedid_constructor_exists():
    assert callable(express::core::ScopedId.__init__)


def test_express::core::scopedid_constructor_args():
    sig = inspect.signature(express::core::ScopedId.__init__)
    params = list(sig.parameters.keys())
    assert "localName" in params, "Missing parameter 'localName'"

def test_express::core::scopedid_has_localName():
    assert hasattr(express::core::ScopedId, "localName")
    descriptor = None
    for klass in express::core::ScopedId.__mro__:
        if "localName" in klass.__dict__:
            descriptor = klass.__dict__["localName"]
            break
    assert isinstance(descriptor, property)



def test_express::core::binarytype_is_not_abstract():
    assert not inspect.isabstract(express::core::BinaryType)


def test_express::core::binarytype_constructor_exists():
    assert callable(express::core::BinaryType.__init__)


def test_express::core::binarytype_constructor_args():
    sig = inspect.signature(express::core::BinaryType.__init__)
    params = list(sig.parameters.keys())



def test_domainrule_is_not_abstract():
    assert not inspect.isabstract(DomainRule)


def test_domainrule_constructor_exists():
    assert callable(DomainRule.__init__)


def test_domainrule_constructor_args():
    sig = inspect.signature(DomainRule.__init__)
    params = list(sig.parameters.keys())



def test_selecttype_is_not_abstract():
    assert not inspect.isabstract(SelectType)


def test_selecttype_constructor_exists():
    assert callable(SelectType.__init__)


def test_selecttype_constructor_args():
    sig = inspect.signature(SelectType.__init__)
    params = list(sig.parameters.keys())



def test_core::commonelement_is_not_abstract():
    assert not inspect.isabstract(core::CommonElement)


def test_core::commonelement_constructor_exists():
    assert callable(core::CommonElement.__init__)


def test_core::commonelement_constructor_args():
    sig = inspect.signature(core::CommonElement.__init__)
    params = list(sig.parameters.keys())



def test_core::scope_is_not_abstract():
    assert not inspect.isabstract(core::Scope)


def test_core::scope_constructor_exists():
    assert callable(core::Scope.__init__)


def test_core::scope_constructor_args():
    sig = inspect.signature(core::Scope.__init__)
    params = list(sig.parameters.keys())



def test_express::core::localscope_is_not_abstract():
    assert not inspect.isabstract(express::core::LocalScope)


def test_express::core::localscope_constructor_exists():
    assert callable(express::core::LocalScope.__init__)


def test_express::core::localscope_constructor_args():
    sig = inspect.signature(express::core::LocalScope.__init__)
    params = list(sig.parameters.keys())



def test_express::core::relationship_is_not_abstract():
    assert not inspect.isabstract(express::core::Relationship)


def test_express::core::relationship_constructor_exists():
    assert callable(express::core::Relationship.__init__)


def test_express::core::relationship_constructor_args():
    sig = inspect.signature(express::core::Relationship.__init__)
    params = list(sig.parameters.keys())



def test_express::core::selecttype_is_not_abstract():
    assert not inspect.isabstract(express::core::SelectType)


def test_express::core::selecttype_constructor_exists():
    assert callable(express::core::SelectType.__init__)


def test_express::core::selecttype_constructor_args():
    sig = inspect.signature(express::core::SelectType.__init__)
    params = list(sig.parameters.keys())
    assert "isExtensible" in params, "Missing parameter 'isExtensible'"
    assert "isEntity" in params, "Missing parameter 'isEntity'"

def test_express::core::selecttype_has_isExtensible():
    assert hasattr(express::core::SelectType, "isExtensible")
    descriptor = None
    for klass in express::core::SelectType.__mro__:
        if "isExtensible" in klass.__dict__:
            descriptor = klass.__dict__["isExtensible"]
            break
    assert isinstance(descriptor, property)

def test_express::core::selecttype_has_isEntity():
    assert hasattr(express::core::SelectType, "isEntity")
    descriptor = None
    for klass in express::core::SelectType.__mro__:
        if "isEntity" in klass.__dict__:
            descriptor = klass.__dict__["isEntity"]
            break
    assert isinstance(descriptor, property)



def test_express::core::parametertype_is_not_abstract():
    assert not inspect.isabstract(express::core::ParameterType)


def test_express::core::parametertype_constructor_exists():
    assert callable(express::core::ParameterType.__init__)


def test_express::core::parametertype_constructor_args():
    sig = inspect.signature(express::core::ParameterType.__init__)
    params = list(sig.parameters.keys())



def test_express::core::scope_is_not_abstract():
    assert not inspect.isabstract(express::core::Scope)


def test_express::core::scope_constructor_exists():
    assert callable(express::core::Scope.__init__)


def test_express::core::scope_constructor_args():
    sig = inspect.signature(express::core::Scope.__init__)
    params = list(sig.parameters.keys())



def test_express::core::role_is_not_abstract():
    assert not inspect.isabstract(express::core::Role)


def test_express::core::role_constructor_exists():
    assert callable(express::core::Role.__init__)


def test_express::core::role_constructor_args():
    sig = inspect.signature(express::core::Role.__init__)
    params = list(sig.parameters.keys())



def test_express::core::remark_is_not_abstract():
    assert not inspect.isabstract(express::core::Remark)


def test_express::core::remark_constructor_exists():
    assert callable(express::core::Remark.__init__)


def test_express::core::remark_constructor_args():
    sig = inspect.signature(express::core::Remark.__init__)
    params = list(sig.parameters.keys())
    assert "isTagged" in params, "Missing parameter 'isTagged'"
    assert "text" in params, "Missing parameter 'text'"
    assert "isTail" in params, "Missing parameter 'isTail'"

def test_express::core::remark_has_isTagged():
    assert hasattr(express::core::Remark, "isTagged")
    descriptor = None
    for klass in express::core::Remark.__mro__:
        if "isTagged" in klass.__dict__:
            descriptor = klass.__dict__["isTagged"]
            break
    assert isinstance(descriptor, property)

def test_express::core::remark_has_text():
    assert hasattr(express::core::Remark, "text")
    descriptor = None
    for klass in express::core::Remark.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_express::core::remark_has_isTail():
    assert hasattr(express::core::Remark, "isTail")
    descriptor = None
    for klass in express::core::Remark.__mro__:
        if "isTail" in klass.__dict__:
            descriptor = klass.__dict__["isTail"]
            break
    assert isinstance(descriptor, property)



def test_express::core::rangerole_is_not_abstract():
    assert not inspect.isabstract(express::core::RangeRole)


def test_express::core::rangerole_constructor_exists():
    assert callable(express::core::RangeRole.__init__)


def test_express::core::rangerole_constructor_args():
    sig = inspect.signature(express::core::RangeRole.__init__)
    params = list(sig.parameters.keys())



def test_arraybound_is_not_abstract():
    assert not inspect.isabstract(ArrayBound)


def test_arraybound_constructor_exists():
    assert callable(ArrayBound.__init__)


def test_arraybound_constructor_args():
    sig = inspect.signature(ArrayBound.__init__)
    params = list(sig.parameters.keys())



def test_concretetype_is_not_abstract():
    assert not inspect.isabstract(ConcreteType)


def test_concretetype_constructor_exists():
    assert callable(ConcreteType.__init__)


def test_concretetype_constructor_args():
    sig = inspect.signature(ConcreteType.__init__)
    params = list(sig.parameters.keys())



def test_express::core::specializedtype_is_not_abstract():
    assert not inspect.isabstract(express::core::SpecializedType)


def test_express::core::specializedtype_constructor_exists():
    assert callable(express::core::SpecializedType.__init__)


def test_express::core::specializedtype_constructor_args():
    sig = inspect.signature(express::core::SpecializedType.__init__)
    params = list(sig.parameters.keys())



def test_express::core::settype_is_not_abstract():
    assert not inspect.isabstract(express::core::SETType)


def test_express::core::settype_constructor_exists():
    assert callable(express::core::SETType.__init__)


def test_express::core::settype_constructor_args():
    sig = inspect.signature(express::core::SETType.__init__)
    params = list(sig.parameters.keys())



def test_localscope_is_not_abstract():
    assert not inspect.isabstract(LocalScope)


def test_localscope_constructor_exists():
    assert callable(LocalScope.__init__)


def test_localscope_constructor_args():
    sig = inspect.signature(LocalScope.__init__)
    params = list(sig.parameters.keys())



def test_express::core::algorithmscope_is_not_abstract():
    assert not inspect.isabstract(express::core::AlgorithmScope)


def test_express::core::algorithmscope_constructor_exists():
    assert callable(express::core::AlgorithmScope.__init__)


def test_express::core::algorithmscope_constructor_args():
    sig = inspect.signature(express::core::AlgorithmScope.__init__)
    params = list(sig.parameters.keys())



def test_anonymoustype_is_not_abstract():
    assert not inspect.isabstract(AnonymousType)


def test_anonymoustype_constructor_exists():
    assert callable(AnonymousType.__init__)


def test_anonymoustype_constructor_args():
    sig = inspect.signature(AnonymousType.__init__)
    params = list(sig.parameters.keys())



def test_express::core::simpletype_is_not_abstract():
    assert not inspect.isabstract(express::core::SimpleType)


def test_express::core::simpletype_constructor_exists():
    assert callable(express::core::SimpleType.__init__)


def test_express::core::simpletype_constructor_args():
    sig = inspect.signature(express::core::SimpleType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_express::core::simpletype_has_id():
    assert hasattr(express::core::SimpleType, "id")
    descriptor = None
    for klass in express::core::SimpleType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_express::core::anonymoustype_is_not_abstract():
    assert not inspect.isabstract(express::core::AnonymousType)


def test_express::core::anonymoustype_constructor_exists():
    assert callable(express::core::AnonymousType.__init__)


def test_express::core::anonymoustype_constructor_args():
    sig = inspect.signature(express::core::AnonymousType.__init__)
    params = list(sig.parameters.keys())



def test_lengthconstraint_is_not_abstract():
    assert not inspect.isabstract(LengthConstraint)


def test_lengthconstraint_constructor_exists():
    assert callable(LengthConstraint.__init__)


def test_lengthconstraint_constructor_args():
    sig = inspect.signature(LengthConstraint.__init__)
    params = list(sig.parameters.keys())



def test_express::core::stringtype_is_not_abstract():
    assert not inspect.isabstract(express::core::StringType)


def test_express::core::stringtype_constructor_exists():
    assert callable(express::core::StringType.__init__)


def test_express::core::stringtype_constructor_args():
    sig = inspect.signature(express::core::StringType.__init__)
    params = list(sig.parameters.keys())



def test_actualtypeconstraint_is_not_abstract():
    assert not inspect.isabstract(ActualTypeConstraint)


def test_actualtypeconstraint_constructor_exists():
    assert callable(ActualTypeConstraint.__init__)


def test_actualtypeconstraint_constructor_args():
    sig = inspect.signature(ActualTypeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_express::core::logictype_is_not_abstract():
    assert not inspect.isabstract(express::core::LogicType)


def test_express::core::logictype_constructor_exists():
    assert callable(express::core::LogicType.__init__)


def test_express::core::logictype_constructor_args():
    sig = inspect.signature(express::core::LogicType.__init__)
    params = list(sig.parameters.keys())



def test_numerictype_is_not_abstract():
    assert not inspect.isabstract(NumericType)


def test_numerictype_constructor_exists():
    assert callable(NumericType.__init__)


def test_numerictype_constructor_args():
    sig = inspect.signature(NumericType.__init__)
    params = list(sig.parameters.keys())



def test_express::core::realtype_is_not_abstract():
    assert not inspect.isabstract(express::core::RealType)


def test_express::core::realtype_constructor_exists():
    assert callable(express::core::RealType.__init__)


def test_express::core::realtype_constructor_args():
    sig = inspect.signature(express::core::RealType.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"

def test_express::core::realtype_has_precision():
    assert hasattr(express::core::RealType, "precision")
    descriptor = None
    for klass in express::core::RealType.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_express::core::bagtype_is_not_abstract():
    assert not inspect.isabstract(express::core::BAGType)


def test_express::core::bagtype_constructor_exists():
    assert callable(express::core::BAGType.__init__)


def test_express::core::bagtype_constructor_args():
    sig = inspect.signature(express::core::BAGType.__init__)
    params = list(sig.parameters.keys())



def test_domainconstraint_is_not_abstract():
    assert not inspect.isabstract(DomainConstraint)


def test_domainconstraint_constructor_exists():
    assert callable(DomainConstraint.__init__)


def test_domainconstraint_constructor_args():
    sig = inspect.signature(DomainConstraint.__init__)
    params = list(sig.parameters.keys())



def test_express::core::lengthconstraint_is_not_abstract():
    assert not inspect.isabstract(express::core::LengthConstraint)


def test_express::core::lengthconstraint_constructor_exists():
    assert callable(express::core::LengthConstraint.__init__)


def test_express::core::lengthconstraint_constructor_args():
    sig = inspect.signature(express::core::LengthConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "maxLength" in params, "Missing parameter 'maxLength'"
    assert "isFixed" in params, "Missing parameter 'isFixed'"

def test_express::core::lengthconstraint_has_maxLength():
    assert hasattr(express::core::LengthConstraint, "maxLength")
    descriptor = None
    for klass in express::core::LengthConstraint.__mro__:
        if "maxLength" in klass.__dict__:
            descriptor = klass.__dict__["maxLength"]
            break
    assert isinstance(descriptor, property)

def test_express::core::lengthconstraint_has_isFixed():
    assert hasattr(express::core::LengthConstraint, "isFixed")
    descriptor = None
    for klass in express::core::LengthConstraint.__mro__:
        if "isFixed" in klass.__dict__:
            descriptor = klass.__dict__["isFixed"]
            break
    assert isinstance(descriptor, property)



def test_express::core::sizeconstraint_is_not_abstract():
    assert not inspect.isabstract(express::core::SizeConstraint)


def test_express::core::sizeconstraint_constructor_exists():
    assert callable(express::core::SizeConstraint.__init__)


def test_express::core::sizeconstraint_constructor_args():
    sig = inspect.signature(express::core::SizeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "bound" in params, "Missing parameter 'bound'"

def test_express::core::sizeconstraint_has_bound():
    assert hasattr(express::core::SizeConstraint, "bound")
    descriptor = None
    for klass in express::core::SizeConstraint.__mro__:
        if "bound" in klass.__dict__:
            descriptor = klass.__dict__["bound"]
            break
    assert isinstance(descriptor, property)



def test_express::core::attributetype_is_not_abstract():
    assert not inspect.isabstract(express::core::AttributeType)


def test_express::core::attributetype_constructor_exists():
    assert callable(express::core::AttributeType.__init__)


def test_express::core::attributetype_constructor_args():
    sig = inspect.signature(express::core::AttributeType.__init__)
    params = list(sig.parameters.keys())



def test_express::core::instance_is_not_abstract():
    assert not inspect.isabstract(express::core::Instance)


def test_express::core::instance_constructor_exists():
    assert callable(express::core::Instance.__init__)


def test_express::core::instance_constructor_args():
    sig = inspect.signature(express::core::Instance.__init__)
    params = list(sig.parameters.keys())



def test_express::core::namedelement_is_not_abstract():
    assert not inspect.isabstract(express::core::NamedElement)


def test_express::core::namedelement_constructor_exists():
    assert callable(express::core::NamedElement.__init__)


def test_express::core::namedelement_constructor_args():
    sig = inspect.signature(express::core::NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_core::variabletype_is_not_abstract():
    assert not inspect.isabstract(core::VariableType)


def test_core::variabletype_constructor_exists():
    assert callable(core::VariableType.__init__)


def test_core::variabletype_constructor_args():
    sig = inspect.signature(core::VariableType.__init__)
    params = list(sig.parameters.keys())



def test_express::core::instantiabletype_is_not_abstract():
    assert not inspect.isabstract(express::core::InstantiableType)


def test_express::core::instantiabletype_constructor_exists():
    assert callable(express::core::InstantiableType.__init__)


def test_express::core::instantiabletype_constructor_args():
    sig = inspect.signature(express::core::InstantiableType.__init__)
    params = list(sig.parameters.keys())



def test_generalaggregationtype_is_not_abstract():
    assert not inspect.isabstract(GeneralAggregationType)


def test_generalaggregationtype_constructor_exists():
    assert callable(GeneralAggregationType.__init__)


def test_generalaggregationtype_constructor_args():
    sig = inspect.signature(GeneralAggregationType.__init__)
    params = list(sig.parameters.keys())



def test_express::core::generallisttype_is_not_abstract():
    assert not inspect.isabstract(express::core::GeneralLISTType)


def test_express::core::generallisttype_constructor_exists():
    assert callable(express::core::GeneralLISTType.__init__)


def test_express::core::generallisttype_constructor_args():
    sig = inspect.signature(express::core::GeneralLISTType.__init__)
    params = list(sig.parameters.keys())



def test_express::core::generalsettype_is_not_abstract():
    assert not inspect.isabstract(express::core::GeneralSETType)


def test_express::core::generalsettype_constructor_exists():
    assert callable(express::core::GeneralSETType.__init__)


def test_express::core::generalsettype_constructor_args():
    sig = inspect.signature(express::core::GeneralSETType.__init__)
    params = list(sig.parameters.keys())



def test_express::core::generalarraytype_is_not_abstract():
    assert not inspect.isabstract(express::core::GeneralARRAYType)


def test_express::core::generalarraytype_constructor_exists():
    assert callable(express::core::GeneralARRAYType.__init__)


def test_express::core::generalarraytype_constructor_args():
    sig = inspect.signature(express::core::GeneralARRAYType.__init__)
    params = list(sig.parameters.keys())
    assert "isOptional" in params, "Missing parameter 'isOptional'"

def test_express::core::generalarraytype_has_isOptional():
    assert hasattr(express::core::GeneralARRAYType, "isOptional")
    descriptor = None
    for klass in express::core::GeneralARRAYType.__mro__:
        if "isOptional" in klass.__dict__:
            descriptor = klass.__dict__["isOptional"]
            break
    assert isinstance(descriptor, property)



def test_express::core::generalbagtype_is_not_abstract():
    assert not inspect.isabstract(express::core::GeneralBAGType)


def test_express::core::generalbagtype_constructor_exists():
    assert callable(express::core::GeneralBAGType.__init__)


def test_express::core::generalbagtype_constructor_args():
    sig = inspect.signature(express::core::GeneralBAGType.__init__)
    params = list(sig.parameters.keys())



def test_actualstructureconstraint_is_not_abstract():
    assert not inspect.isabstract(ActualStructureConstraint)


def test_actualstructureconstraint_constructor_exists():
    assert callable(ActualStructureConstraint.__init__)


def test_actualstructureconstraint_constructor_args():
    sig = inspect.signature(ActualStructureConstraint.__init__)
    params = list(sig.parameters.keys())



def test_parametertype_is_not_abstract():
    assert not inspect.isabstract(ParameterType)


def test_parametertype_constructor_exists():
    assert callable(ParameterType.__init__)


def test_parametertype_constructor_args():
    sig = inspect.signature(ParameterType.__init__)
    params = list(sig.parameters.keys())



def test_express::core::arraybound_is_not_abstract():
    assert not inspect.isabstract(express::core::ArrayBound)


def test_express::core::arraybound_constructor_exists():
    assert callable(express::core::ArrayBound.__init__)


def test_express::core::arraybound_constructor_args():
    sig = inspect.signature(express::core::ArrayBound.__init__)
    params = list(sig.parameters.keys())
    assert "bound" in params, "Missing parameter 'bound'"

def test_express::core::arraybound_has_bound():
    assert hasattr(express::core::ArrayBound, "bound")
    descriptor = None
    for klass in express::core::ArrayBound.__mro__:
        if "bound" in klass.__dict__:
            descriptor = klass.__dict__["bound"]
            break
    assert isinstance(descriptor, property)



def test_core::attributetype_is_not_abstract():
    assert not inspect.isabstract(core::AttributeType)


def test_core::attributetype_constructor_exists():
    assert callable(core::AttributeType.__init__)


def test_core::attributetype_constructor_args():
    sig = inspect.signature(core::AttributeType.__init__)
    params = list(sig.parameters.keys())



def test_express::core::namedtype_is_not_abstract():
    assert not inspect.isabstract(express::core::NamedType)


def test_express::core::namedtype_constructor_exists():
    assert callable(express::core::NamedType.__init__)


def test_express::core::namedtype_constructor_args():
    sig = inspect.signature(express::core::NamedType.__init__)
    params = list(sig.parameters.keys())



def test_express::core::generalizedtype_is_not_abstract():
    assert not inspect.isabstract(express::core::GeneralizedType)


def test_express::core::generalizedtype_constructor_exists():
    assert callable(express::core::GeneralizedType.__init__)


def test_express::core::generalizedtype_constructor_args():
    sig = inspect.signature(express::core::GeneralizedType.__init__)
    params = list(sig.parameters.keys())



def test_core::datatype_is_not_abstract():
    assert not inspect.isabstract(core::DataType)


def test_core::datatype_constructor_exists():
    assert callable(core::DataType.__init__)


def test_core::datatype_constructor_args():
    sig = inspect.signature(core::DataType.__init__)
    params = list(sig.parameters.keys())



def test_express::core::variabletype_is_not_abstract():
    assert not inspect.isabstract(express::core::VariableType)


def test_express::core::variabletype_constructor_exists():
    assert callable(express::core::VariableType.__init__)


def test_express::core::variabletype_constructor_args():
    sig = inspect.signature(express::core::VariableType.__init__)
    params = list(sig.parameters.keys())



def test_enumerationtype_is_not_abstract():
    assert not inspect.isabstract(EnumerationType)


def test_enumerationtype_constructor_exists():
    assert callable(EnumerationType.__init__)


def test_enumerationtype_constructor_args():
    sig = inspect.signature(EnumerationType.__init__)
    params = list(sig.parameters.keys())



def test_namedtype_is_not_abstract():
    assert not inspect.isabstract(NamedType)


def test_namedtype_constructor_exists():
    assert callable(NamedType.__init__)


def test_namedtype_constructor_args():
    sig = inspect.signature(NamedType.__init__)
    params = list(sig.parameters.keys())



def test_listmember_is_not_abstract():
    assert not inspect.isabstract(ListMember)


def test_listmember_constructor_exists():
    assert callable(ListMember.__init__)


def test_listmember_constructor_args():
    sig = inspect.signature(ListMember.__init__)
    params = list(sig.parameters.keys())



def test_repeatcount_is_not_abstract():
    assert not inspect.isabstract(RepeatCount)


def test_repeatcount_constructor_exists():
    assert callable(RepeatCount.__init__)


def test_repeatcount_constructor_args():
    sig = inspect.signature(RepeatCount.__init__)
    params = list(sig.parameters.keys())



def test_express::expressions::memberbinding_is_not_abstract():
    assert not inspect.isabstract(express::expressions::MemberBinding)


def test_express::expressions::memberbinding_constructor_exists():
    assert callable(express::expressions::MemberBinding.__init__)


def test_express::expressions::memberbinding_constructor_args():
    sig = inspect.signature(express::expressions::MemberBinding.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_express::expressions::memberbinding_has_position():
    assert hasattr(express::expressions::MemberBinding, "position")
    descriptor = None
    for klass in express::expressions::MemberBinding.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_functionresult_is_not_abstract():
    assert not inspect.isabstract(FunctionResult)


def test_functionresult_constructor_exists():
    assert callable(FunctionResult.__init__)


def test_functionresult_constructor_args():
    sig = inspect.signature(FunctionResult.__init__)
    params = list(sig.parameters.keys())



def test_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_function_constructor_exists():
    assert callable(Function.__init__)


def test_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())



def test_sizeconstraint_is_not_abstract():
    assert not inspect.isabstract(SizeConstraint)


def test_sizeconstraint_constructor_exists():
    assert callable(SizeConstraint.__init__)


def test_sizeconstraint_constructor_args():
    sig = inspect.signature(SizeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_generalizedtype_is_not_abstract():
    assert not inspect.isabstract(GeneralizedType)


def test_generalizedtype_constructor_exists():
    assert callable(GeneralizedType.__init__)


def test_generalizedtype_constructor_args():
    sig = inspect.signature(GeneralizedType.__init__)
    params = list(sig.parameters.keys())



def test_express::core::generictype_is_not_abstract():
    assert not inspect.isabstract(express::core::GenericType)


def test_express::core::generictype_constructor_exists():
    assert callable(express::core::GenericType.__init__)


def test_express::core::generictype_constructor_args():
    sig = inspect.signature(express::core::GenericType.__init__)
    params = list(sig.parameters.keys())
    assert "isEntity" in params, "Missing parameter 'isEntity'"

def test_express::core::generictype_has_isEntity():
    assert hasattr(express::core::GenericType, "isEntity")
    descriptor = None
    for klass in express::core::GenericType.__mro__:
        if "isEntity" in klass.__dict__:
            descriptor = klass.__dict__["isEntity"]
            break
    assert isinstance(descriptor, property)



def test_express::core::aggregatetype_is_not_abstract():
    assert not inspect.isabstract(express::core::AGGREGATEType)


def test_express::core::aggregatetype_constructor_exists():
    assert callable(express::core::AGGREGATEType.__init__)


def test_express::core::aggregatetype_constructor_args():
    sig = inspect.signature(express::core::AGGREGATEType.__init__)
    params = list(sig.parameters.keys())



def test_partialentitytype_is_not_abstract():
    assert not inspect.isabstract(PartialEntityType)


def test_partialentitytype_constructor_exists():
    assert callable(PartialEntityType.__init__)


def test_partialentitytype_constructor_args():
    sig = inspect.signature(PartialEntityType.__init__)
    params = list(sig.parameters.keys())



def test_express::core::singleentitytype_is_not_abstract():
    assert not inspect.isabstract(express::core::SingleEntityType)


def test_express::core::singleentitytype_constructor_exists():
    assert callable(express::core::SingleEntityType.__init__)


def test_express::core::singleentitytype_constructor_args():
    sig = inspect.signature(express::core::SingleEntityType.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_express::core::localelement_is_not_abstract():
    assert not inspect.isabstract(express::core::LocalElement)


def test_express::core::localelement_constructor_exists():
    assert callable(express::core::LocalElement.__init__)


def test_express::core::localelement_constructor_args():
    sig = inspect.signature(express::core::LocalElement.__init__)
    params = list(sig.parameters.keys())



def test_express::core::schemaelement_is_not_abstract():
    assert not inspect.isabstract(express::core::SchemaElement)


def test_express::core::schemaelement_constructor_exists():
    assert callable(express::core::SchemaElement.__init__)


def test_express::core::schemaelement_constructor_args():
    sig = inspect.signature(express::core::SchemaElement.__init__)
    params = list(sig.parameters.keys())



def test_express::core::typeelement_is_not_abstract():
    assert not inspect.isabstract(express::core::TypeElement)


def test_express::core::typeelement_constructor_exists():
    assert callable(express::core::TypeElement.__init__)


def test_express::core::typeelement_constructor_args():
    sig = inspect.signature(express::core::TypeElement.__init__)
    params = list(sig.parameters.keys())



def test_core::expression_is_not_abstract():
    assert not inspect.isabstract(core::Expression)


def test_core::expression_constructor_exists():
    assert callable(core::Expression.__init__)


def test_core::expression_constructor_args():
    sig = inspect.signature(core::Expression.__init__)
    params = list(sig.parameters.keys())



def test_constant_is_not_abstract():
    assert not inspect.isabstract(Constant)


def test_constant_constructor_exists():
    assert callable(Constant.__init__)


def test_constant_constructor_args():
    sig = inspect.signature(Constant.__init__)
    params = list(sig.parameters.keys())



def test_attribute_is_not_abstract():
    assert not inspect.isabstract(Attribute)


def test_attribute_constructor_exists():
    assert callable(Attribute.__init__)


def test_attribute_constructor_args():
    sig = inspect.signature(Attribute.__init__)
    params = list(sig.parameters.keys())



def test_express::core::derivedattribute_is_not_abstract():
    assert not inspect.isabstract(express::core::DerivedAttribute)


def test_express::core::derivedattribute_constructor_exists():
    assert callable(express::core::DerivedAttribute.__init__)


def test_express::core::derivedattribute_constructor_args():
    sig = inspect.signature(express::core::DerivedAttribute.__init__)
    params = list(sig.parameters.keys())



def test_express::core::inverseattribute_is_not_abstract():
    assert not inspect.isabstract(express::core::InverseAttribute)


def test_express::core::inverseattribute_constructor_exists():
    assert callable(express::core::InverseAttribute.__init__)


def test_express::core::inverseattribute_constructor_args():
    sig = inspect.signature(express::core::InverseAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "isUnique" in params, "Missing parameter 'isUnique'"

def test_express::core::inverseattribute_has_isUnique():
    assert hasattr(express::core::InverseAttribute, "isUnique")
    descriptor = None
    for klass in express::core::InverseAttribute.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)



def test_express::core::explicitattribute_is_not_abstract():
    assert not inspect.isabstract(express::core::ExplicitAttribute)


def test_express::core::explicitattribute_constructor_exists():
    assert callable(express::core::ExplicitAttribute.__init__)


def test_express::core::explicitattribute_constructor_args():
    sig = inspect.signature(express::core::ExplicitAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "isOptional" in params, "Missing parameter 'isOptional'"

def test_express::core::explicitattribute_has_isOptional():
    assert hasattr(express::core::ExplicitAttribute, "isOptional")
    descriptor = None
    for klass in express::core::ExplicitAttribute.__mro__:
        if "isOptional" in klass.__dict__:
            descriptor = klass.__dict__["isOptional"]
            break
    assert isinstance(descriptor, property)



def test_selector_is_not_abstract():
    assert not inspect.isabstract(Selector)


def test_selector_constructor_exists():
    assert callable(Selector.__init__)


def test_selector_constructor_args():
    sig = inspect.signature(Selector.__init__)
    params = list(sig.parameters.keys())



def test_express::expressions::usedinref_is_not_abstract():
    assert not inspect.isabstract(express::expressions::UsedInRef)


def test_express::expressions::usedinref_constructor_exists():
    assert callable(express::expressions::UsedInRef.__init__)


def test_express::expressions::usedinref_constructor_args():
    sig = inspect.signature(express::expressions::UsedInRef.__init__)
    params = list(sig.parameters.keys())



def test_express::expressions::groupref_is_not_abstract():
    assert not inspect.isabstract(express::expressions::GroupRef)


def test_express::expressions::groupref_constructor_exists():
    assert callable(express::expressions::GroupRef.__init__)


def test_express::expressions::groupref_constructor_args():
    sig = inspect.signature(express::expressions::GroupRef.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_express::expressions::groupref_has_id():
    assert hasattr(express::expressions::GroupRef, "id")
    descriptor = None
    for klass in express::expressions::GroupRef.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_express::expressions::attributeref_is_not_abstract():
    assert not inspect.isabstract(express::expressions::AttributeRef)


def test_express::expressions::attributeref_constructor_exists():
    assert callable(express::expressions::AttributeRef.__init__)


def test_express::expressions::attributeref_constructor_args():
    sig = inspect.signature(express::expressions::AttributeRef.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_express::expressions::attributeref_has_id():
    assert hasattr(express::expressions::AttributeRef, "id")
    descriptor = None
    for klass in express::expressions::AttributeRef.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_attributevalue_is_not_abstract():
    assert not inspect.isabstract(AttributeValue)


def test_attributevalue_constructor_exists():
    assert callable(AttributeValue.__init__)


def test_attributevalue_constructor_args():
    sig = inspect.signature(AttributeValue.__init__)
    params = list(sig.parameters.keys())



def test_express::expressions::attributebinding_is_not_abstract():
    assert not inspect.isabstract(express::expressions::AttributeBinding)


def test_express::expressions::attributebinding_constructor_exists():
    assert callable(express::expressions::AttributeBinding.__init__)


def test_express::expressions::attributebinding_constructor_args():
    sig = inspect.signature(express::expressions::AttributeBinding.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_express::expressions::attributebinding_has_position():
    assert hasattr(express::expressions::AttributeBinding, "position")
    descriptor = None
    for klass in express::expressions::AttributeBinding.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_queryvariable_is_not_abstract():
    assert not inspect.isabstract(QueryVariable)


def test_queryvariable_constructor_exists():
    assert callable(QueryVariable.__init__)


def test_queryvariable_constructor_args():
    sig = inspect.signature(QueryVariable.__init__)
    params = list(sig.parameters.keys())



def test_variabletype_is_not_abstract():
    assert not inspect.isabstract(VariableType)


def test_variabletype_constructor_exists():
    assert callable(VariableType.__init__)


def test_variabletype_constructor_args():
    sig = inspect.signature(VariableType.__init__)
    params = list(sig.parameters.keys())



def test_express::core::actualtype_is_not_abstract():
    assert not inspect.isabstract(express::core::ActualType)


def test_express::core::actualtype_constructor_exists():
    assert callable(express::core::ActualType.__init__)


def test_express::core::actualtype_constructor_args():
    sig = inspect.signature(express::core::ActualType.__init__)
    params = list(sig.parameters.keys())



def test_attributebinding_is_not_abstract():
    assert not inspect.isabstract(AttributeBinding)


def test_attributebinding_constructor_exists():
    assert callable(AttributeBinding.__init__)


def test_attributebinding_constructor_args():
    sig = inspect.signature(AttributeBinding.__init__)
    params = list(sig.parameters.keys())



def test_partialentityvalue_is_not_abstract():
    assert not inspect.isabstract(PartialEntityValue)


def test_partialentityvalue_constructor_exists():
    assert callable(PartialEntityValue.__init__)


def test_partialentityvalue_constructor_args():
    sig = inspect.signature(PartialEntityValue.__init__)
    params = list(sig.parameters.keys())



def test_express::instances::entityvalue_is_not_abstract():
    assert not inspect.isabstract(express::instances::EntityValue)


def test_express::instances::entityvalue_constructor_exists():
    assert callable(express::instances::EntityValue.__init__)


def test_express::instances::entityvalue_constructor_args():
    sig = inspect.signature(express::instances::EntityValue.__init__)
    params = list(sig.parameters.keys())



def test_memberbinding_is_not_abstract():
    assert not inspect.isabstract(MemberBinding)


def test_memberbinding_constructor_exists():
    assert callable(MemberBinding.__init__)


def test_memberbinding_constructor_args():
    sig = inspect.signature(MemberBinding.__init__)
    params = list(sig.parameters.keys())



def test_genericaggregate_is_not_abstract():
    assert not inspect.isabstract(GenericAggregate)


def test_genericaggregate_constructor_exists():
    assert callable(GenericAggregate.__init__)


def test_genericaggregate_constructor_args():
    sig = inspect.signature(GenericAggregate.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_express::expressions::unaryoperation_is_not_abstract():
    assert not inspect.isabstract(express::expressions::UnaryOperation)


def test_express::expressions::unaryoperation_constructor_exists():
    assert callable(express::expressions::UnaryOperation.__init__)


def test_express::expressions::unaryoperation_constructor_args():
    sig = inspect.signature(express::expressions::UnaryOperation.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_express::expressions::unaryoperation_has_operator():
    assert hasattr(express::expressions::UnaryOperation, "operator")
    descriptor = None
    for klass in express::expressions::UnaryOperation.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_express::expressions::coercion_is_not_abstract():
    assert not inspect.isabstract(express::expressions::Coercion)


def test_express::expressions::coercion_constructor_exists():
    assert callable(express::expressions::Coercion.__init__)


def test_express::expressions::coercion_constructor_args():
    sig = inspect.signature(express::expressions::Coercion.__init__)
    params = list(sig.parameters.keys())



def test_express::expressions::binaryoperation_is_not_abstract():
    assert not inspect.isabstract(express::expressions::BinaryOperation)


def test_express::expressions::binaryoperation_constructor_exists():
    assert callable(express::expressions::BinaryOperation.__init__)


def test_express::expressions::binaryoperation_constructor_args():
    sig = inspect.signature(express::expressions::BinaryOperation.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_express::expressions::binaryoperation_has_operator():
    assert hasattr(express::expressions::BinaryOperation, "operator")
    descriptor = None
    for klass in express::expressions::BinaryOperation.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_express::algorithms::inparameter_is_not_abstract():
    assert not inspect.isabstract(express::algorithms::InParameter)


def test_express::algorithms::inparameter_constructor_exists():
    assert callable(express::algorithms::InParameter.__init__)


def test_express::algorithms::inparameter_constructor_args():
    sig = inspect.signature(express::algorithms::InParameter.__init__)
    params = list(sig.parameters.keys())



def test_functioncall_is_not_abstract():
    assert not inspect.isabstract(FunctionCall)


def test_functioncall_constructor_exists():
    assert callable(FunctionCall.__init__)


def test_functioncall_constructor_args():
    sig = inspect.signature(FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_procedurecall_is_not_abstract():
    assert not inspect.isabstract(ProcedureCall)


def test_procedurecall_constructor_exists():
    assert callable(ProcedureCall.__init__)


def test_procedurecall_constructor_args():
    sig = inspect.signature(ProcedureCall.__init__)
    params = list(sig.parameters.keys())



def test_express::expressions::actualparameter_is_not_abstract():
    assert not inspect.isabstract(express::expressions::ActualParameter)


def test_express::expressions::actualparameter_constructor_exists():
    assert callable(express::expressions::ActualParameter.__init__)


def test_express::expressions::actualparameter_constructor_args():
    sig = inspect.signature(express::expressions::ActualParameter.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_express::expressions::actualparameter_has_position():
    assert hasattr(express::expressions::ActualParameter, "position")
    descriptor = None
    for klass in express::expressions::ActualParameter.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_indexoperation_is_not_abstract():
    assert not inspect.isabstract(IndexOperation)


def test_indexoperation_constructor_exists():
    assert callable(IndexOperation.__init__)


def test_indexoperation_constructor_args():
    sig = inspect.signature(IndexOperation.__init__)
    params = list(sig.parameters.keys())



def test_express::expressions::stringindex_is_not_abstract():
    assert not inspect.isabstract(express::expressions::StringIndex)


def test_express::expressions::stringindex_constructor_exists():
    assert callable(express::expressions::StringIndex.__init__)


def test_express::expressions::stringindex_constructor_args():
    sig = inspect.signature(express::expressions::StringIndex.__init__)
    params = list(sig.parameters.keys())



def test_express::expressions::aggregateindex_is_not_abstract():
    assert not inspect.isabstract(express::expressions::AggregateIndex)


def test_express::expressions::aggregateindex_constructor_exists():
    assert callable(express::expressions::AggregateIndex.__init__)


def test_express::expressions::aggregateindex_constructor_args():
    sig = inspect.signature(express::expressions::AggregateIndex.__init__)
    params = list(sig.parameters.keys())



def test_express::expressions::binaryindex_is_not_abstract():
    assert not inspect.isabstract(express::expressions::BinaryIndex)


def test_express::expressions::binaryindex_constructor_exists():
    assert callable(express::expressions::BinaryIndex.__init__)


def test_express::expressions::binaryindex_constructor_args():
    sig = inspect.signature(express::expressions::BinaryIndex.__init__)
    params = list(sig.parameters.keys())



def test_simplevalue_is_not_abstract():
    assert not inspect.isabstract(SimpleValue)


def test_simplevalue_constructor_exists():
    assert callable(SimpleValue.__init__)


def test_simplevalue_constructor_args():
    sig = inspect.signature(SimpleValue.__init__)
    params = list(sig.parameters.keys())



def test_express::instances::binaryvalue_is_not_abstract():
    assert not inspect.isabstract(express::instances::BinaryValue)


def test_express::instances::binaryvalue_constructor_exists():
    assert callable(express::instances::BinaryValue.__init__)


def test_express::instances::binaryvalue_constructor_args():
    sig = inspect.signature(express::instances::BinaryValue.__init__)
    params = list(sig.parameters.keys())



def test_express::instances::numbervalue_is_not_abstract():
    assert not inspect.isabstract(express::instances::NumberValue)


def test_express::instances::numbervalue_constructor_exists():
    assert callable(express::instances::NumberValue.__init__)


def test_express::instances::numbervalue_constructor_args():
    sig = inspect.signature(express::instances::NumberValue.__init__)
    params = list(sig.parameters.keys())



def test_express::instances::logicalvalue_is_not_abstract():
    assert not inspect.isabstract(express::instances::LogicalValue)


def test_express::instances::logicalvalue_constructor_exists():
    assert callable(express::instances::LogicalValue.__init__)


def test_express::instances::logicalvalue_constructor_args():
    sig = inspect.signature(express::instances::LogicalValue.__init__)
    params = list(sig.parameters.keys())



def test_express::instances::stringvalue_is_not_abstract():
    assert not inspect.isabstract(express::instances::StringValue)


def test_express::instances::stringvalue_constructor_exists():
    assert callable(express::instances::StringValue.__init__)


def test_express::instances::stringvalue_constructor_args():
    sig = inspect.signature(express::instances::StringValue.__init__)
    params = list(sig.parameters.keys())



def test_enumerationitem_is_not_abstract():
    assert not inspect.isabstract(EnumerationItem)


def test_enumerationitem_constructor_exists():
    assert callable(EnumerationItem.__init__)


def test_enumerationitem_constructor_args():
    sig = inspect.signature(EnumerationItem.__init__)
    params = list(sig.parameters.keys())



def test_primary_is_not_abstract():
    assert not inspect.isabstract(Primary)


def test_primary_constructor_exists():
    assert callable(Primary.__init__)


def test_primary_constructor_args():
    sig = inspect.signature(Primary.__init__)
    params = list(sig.parameters.keys())



def test_express::expressions::extentref_is_not_abstract():
    assert not inspect.isabstract(express::expressions::ExtentRef)


def test_express::expressions::extentref_constructor_exists():
    assert callable(express::expressions::ExtentRef.__init__)


def test_express::expressions::extentref_constructor_args():
    sig = inspect.signature(express::expressions::ExtentRef.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_express::expressions::extentref_has_id():
    assert hasattr(express::expressions::ExtentRef, "id")
    descriptor = None
    for klass in express::expressions::ExtentRef.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_express::expressions::literal_is_not_abstract():
    assert not inspect.isabstract(express::expressions::Literal)


def test_express::expressions::literal_constructor_exists():
    assert callable(express::expressions::Literal.__init__)


def test_express::expressions::literal_constructor_args():
    sig = inspect.signature(express::expressions::Literal.__init__)
    params = list(sig.parameters.keys())



def test_express::expressions::variableref_is_not_abstract():
    assert not inspect.isabstract(express::expressions::VariableRef)


def test_express::expressions::variableref_constructor_exists():
    assert callable(express::expressions::VariableRef.__init__)


def test_express::expressions::variableref_constructor_args():
    sig = inspect.signature(express::expressions::VariableRef.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_express::expressions::variableref_has_id():
    assert hasattr(express::expressions::VariableRef, "id")
    descriptor = None
    for klass in express::expressions::VariableRef.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_express::expressions::constantref_is_not_abstract():
    assert not inspect.isabstract(express::expressions::ConstantRef)


def test_express::expressions::constantref_constructor_exists():
    assert callable(express::expressions::ConstantRef.__init__)


def test_express::expressions::constantref_constructor_args():
    sig = inspect.signature(express::expressions::ConstantRef.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_express::expressions::constantref_has_id():
    assert hasattr(express::expressions::ConstantRef, "id")
    descriptor = None
    for klass in express::expressions::ConstantRef.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_express::expressions::indeterminateref_is_not_abstract():
    assert not inspect.isabstract(express::expressions::IndeterminateRef)


def test_express::expressions::indeterminateref_constructor_exists():
    assert callable(express::expressions::IndeterminateRef.__init__)


def test_express::expressions::indeterminateref_constructor_args():
    sig = inspect.signature(express::expressions::IndeterminateRef.__init__)
    params = list(sig.parameters.keys())



def test_express::expressions::parameterref_is_not_abstract():
    assert not inspect.isabstract(express::expressions::ParameterRef)


def test_express::expressions::parameterref_constructor_exists():
    assert callable(express::expressions::ParameterRef.__init__)


def test_express::expressions::parameterref_constructor_args():
    sig = inspect.signature(express::expressions::ParameterRef.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_express::expressions::parameterref_has_id():
    assert hasattr(express::expressions::ParameterRef, "id")
    descriptor = None
    for klass in express::expressions::ParameterRef.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_express::expressions::enumitemref_is_not_abstract():
    assert not inspect.isabstract(express::expressions::EnumItemRef)


def test_express::expressions::enumitemref_constructor_exists():
    assert callable(express::expressions::EnumItemRef.__init__)


def test_express::expressions::enumitemref_constructor_args():
    sig = inspect.signature(express::expressions::EnumItemRef.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_express::expressions::enumitemref_has_id():
    assert hasattr(express::expressions::EnumItemRef, "id")
    descriptor = None
    for klass in express::expressions::EnumItemRef.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_express::expressions::repeatcount_is_not_abstract():
    assert not inspect.isabstract(express::expressions::RepeatCount)


def test_express::expressions::repeatcount_constructor_exists():
    assert callable(express::expressions::RepeatCount.__init__)


def test_express::expressions::repeatcount_constructor_args():
    sig = inspect.signature(express::expressions::RepeatCount.__init__)
    params = list(sig.parameters.keys())



def test_express::expressions::selfref_is_not_abstract():
    assert not inspect.isabstract(express::expressions::SELFRef)


def test_express::expressions::selfref_constructor_exists():
    assert callable(express::expressions::SELFRef.__init__)


def test_express::expressions::selfref_constructor_args():
    sig = inspect.signature(express::expressions::SELFRef.__init__)
    params = list(sig.parameters.keys())



def test_indeterminate_is_not_abstract():
    assert not inspect.isabstract(Indeterminate)


def test_indeterminate_constructor_exists():
    assert callable(Indeterminate.__init__)


def test_indeterminate_constructor_args():
    sig = inspect.signature(Indeterminate.__init__)
    params = list(sig.parameters.keys())



def test_caseaction_is_not_abstract():
    assert not inspect.isabstract(CaseAction)


def test_caseaction_constructor_exists():
    assert callable(CaseAction.__init__)


def test_caseaction_constructor_args():
    sig = inspect.signature(CaseAction.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_express::algorithms::invariable_is_not_abstract():
    assert not inspect.isabstract(express::algorithms::InVariable)


def test_express::algorithms::invariable_constructor_exists():
    assert callable(express::algorithms::InVariable.__init__)


def test_express::algorithms::invariable_constructor_args():
    sig = inspect.signature(express::algorithms::InVariable.__init__)
    params = list(sig.parameters.keys())



def test_express::algorithms::functionresult_is_not_abstract():
    assert not inspect.isabstract(express::algorithms::FunctionResult)


def test_express::algorithms::functionresult_constructor_exists():
    assert callable(express::algorithms::FunctionResult.__init__)


def test_express::algorithms::functionresult_constructor_args():
    sig = inspect.signature(express::algorithms::FunctionResult.__init__)
    params = list(sig.parameters.keys())



def test_express::algorithms::localvariable_is_not_abstract():
    assert not inspect.isabstract(express::algorithms::LocalVariable)


def test_express::algorithms::localvariable_constructor_exists():
    assert callable(express::algorithms::LocalVariable.__init__)


def test_express::algorithms::localvariable_constructor_args():
    sig = inspect.signature(express::algorithms::LocalVariable.__init__)
    params = list(sig.parameters.keys())



def test_singleentitytype_is_not_abstract():
    assert not inspect.isabstract(SingleEntityType)


def test_singleentitytype_constructor_exists():
    assert callable(SingleEntityType.__init__)


def test_singleentitytype_constructor_args():
    sig = inspect.signature(SingleEntityType.__init__)
    params = list(sig.parameters.keys())



def test_controlvariable_is_not_abstract():
    assert not inspect.isabstract(ControlVariable)


def test_controlvariable_constructor_exists():
    assert callable(ControlVariable.__init__)


def test_controlvariable_constructor_args():
    sig = inspect.signature(ControlVariable.__init__)
    params = list(sig.parameters.keys())



def test_explicitattribute_is_not_abstract():
    assert not inspect.isabstract(ExplicitAttribute)


def test_explicitattribute_constructor_exists():
    assert callable(ExplicitAttribute.__init__)


def test_explicitattribute_constructor_args():
    sig = inspect.signature(ExplicitAttribute.__init__)
    params = list(sig.parameters.keys())



def test_express::core::invertibleattribute_is_not_abstract():
    assert not inspect.isabstract(express::core::InvertibleAttribute)


def test_express::core::invertibleattribute_constructor_exists():
    assert callable(express::core::InvertibleAttribute.__init__)


def test_express::core::invertibleattribute_constructor_args():
    sig = inspect.signature(express::core::InvertibleAttribute.__init__)
    params = list(sig.parameters.keys())



def test_express::statements::varexpression_is_not_abstract():
    assert not inspect.isabstract(express::statements::VARExpression)


def test_express::statements::varexpression_constructor_exists():
    assert callable(express::statements::VARExpression.__init__)


def test_express::statements::varexpression_constructor_args():
    sig = inspect.signature(express::statements::VARExpression.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_express::statements::varexpression_has_text():
    assert hasattr(express::statements::VARExpression, "text")
    descriptor = None
    for klass in express::statements::VARExpression.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_varvariable_is_not_abstract():
    assert not inspect.isabstract(VARVariable)


def test_varvariable_constructor_exists():
    assert callable(VARVariable.__init__)


def test_varvariable_constructor_args():
    sig = inspect.signature(VARVariable.__init__)
    params = list(sig.parameters.keys())



def test_algorithms::varvariable_is_not_abstract():
    assert not inspect.isabstract(algorithms::VARVariable)


def test_algorithms::varvariable_constructor_exists():
    assert callable(algorithms::VARVariable.__init__)


def test_algorithms::varvariable_constructor_args():
    sig = inspect.signature(algorithms::VARVariable.__init__)
    params = list(sig.parameters.keys())



def test_express::algorithms::varparameter_is_not_abstract():
    assert not inspect.isabstract(express::algorithms::VARParameter)


def test_express::algorithms::varparameter_constructor_exists():
    assert callable(express::algorithms::VARParameter.__init__)


def test_express::algorithms::varparameter_constructor_args():
    sig = inspect.signature(express::algorithms::VARParameter.__init__)
    params = list(sig.parameters.keys())



def test_algorithms::namedvariable_is_not_abstract():
    assert not inspect.isabstract(algorithms::NamedVariable)


def test_algorithms::namedvariable_constructor_exists():
    assert callable(algorithms::NamedVariable.__init__)


def test_algorithms::namedvariable_constructor_args():
    sig = inspect.signature(algorithms::NamedVariable.__init__)
    params = list(sig.parameters.keys())



def test_express::statements::aliasvariable_is_not_abstract():
    assert not inspect.isabstract(express::statements::AliasVariable)


def test_express::statements::aliasvariable_constructor_exists():
    assert callable(express::statements::AliasVariable.__init__)


def test_express::statements::aliasvariable_constructor_args():
    sig = inspect.signature(express::statements::AliasVariable.__init__)
    params = list(sig.parameters.keys())



def test_namedvariable_is_not_abstract():
    assert not inspect.isabstract(NamedVariable)


def test_namedvariable_constructor_exists():
    assert callable(NamedVariable.__init__)


def test_namedvariable_constructor_args():
    sig = inspect.signature(NamedVariable.__init__)
    params = list(sig.parameters.keys())



def test_express::algorithms::variable_is_not_abstract():
    assert not inspect.isabstract(express::algorithms::Variable)


def test_express::algorithms::variable_constructor_exists():
    assert callable(express::algorithms::Variable.__init__)


def test_express::algorithms::variable_constructor_args():
    sig = inspect.signature(express::algorithms::Variable.__init__)
    params = list(sig.parameters.keys())



def test_express::expressions::queryvariable_is_not_abstract():
    assert not inspect.isabstract(express::expressions::QueryVariable)


def test_express::expressions::queryvariable_constructor_exists():
    assert callable(express::expressions::QueryVariable.__init__)


def test_express::expressions::queryvariable_constructor_args():
    sig = inspect.signature(express::expressions::QueryVariable.__init__)
    params = list(sig.parameters.keys())



def test_express::statements::controlvariable_is_not_abstract():
    assert not inspect.isabstract(express::statements::ControlVariable)


def test_express::statements::controlvariable_constructor_exists():
    assert callable(express::statements::ControlVariable.__init__)


def test_express::statements::controlvariable_constructor_args():
    sig = inspect.signature(express::statements::ControlVariable.__init__)
    params = list(sig.parameters.keys())



def test_aliasvariable_is_not_abstract():
    assert not inspect.isabstract(AliasVariable)


def test_aliasvariable_constructor_exists():
    assert callable(AliasVariable.__init__)


def test_aliasvariable_constructor_args():
    sig = inspect.signature(AliasVariable.__init__)
    params = list(sig.parameters.keys())



def test_varexpression_is_not_abstract():
    assert not inspect.isabstract(VARExpression)


def test_varexpression_constructor_exists():
    assert callable(VARExpression.__init__)


def test_varexpression_constructor_args():
    sig = inspect.signature(VARExpression.__init__)
    params = list(sig.parameters.keys())



def test_express::statements::variablecell_is_not_abstract():
    assert not inspect.isabstract(express::statements::VariableCell)


def test_express::statements::variablecell_constructor_exists():
    assert callable(express::statements::VariableCell.__init__)


def test_express::statements::variablecell_constructor_args():
    sig = inspect.signature(express::statements::VariableCell.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_express::statements::variablecell_has_id():
    assert hasattr(express::statements::VariableCell, "id")
    descriptor = None
    for klass in express::statements::VariableCell.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_express::statements::groupcell_is_not_abstract():
    assert not inspect.isabstract(express::statements::GroupCell)


def test_express::statements::groupcell_constructor_exists():
    assert callable(express::statements::GroupCell.__init__)


def test_express::statements::groupcell_constructor_args():
    sig = inspect.signature(express::statements::GroupCell.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_express::statements::groupcell_has_id():
    assert hasattr(express::statements::GroupCell, "id")
    descriptor = None
    for klass in express::statements::GroupCell.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_express::statements::attributecell_is_not_abstract():
    assert not inspect.isabstract(express::statements::AttributeCell)


def test_express::statements::attributecell_constructor_exists():
    assert callable(express::statements::AttributeCell.__init__)


def test_express::statements::attributecell_constructor_args():
    sig = inspect.signature(express::statements::AttributeCell.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_express::statements::attributecell_has_id():
    assert hasattr(express::statements::AttributeCell, "id")
    descriptor = None
    for klass in express::statements::AttributeCell.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_express::statements::varcell_is_not_abstract():
    assert not inspect.isabstract(express::statements::VARCell)


def test_express::statements::varcell_constructor_exists():
    assert callable(express::statements::VARCell.__init__)


def test_express::statements::varcell_constructor_args():
    sig = inspect.signature(express::statements::VARCell.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_express::statements::varcell_has_id():
    assert hasattr(express::statements::VARCell, "id")
    descriptor = None
    for klass in express::statements::VARCell.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_express::statements::membercell_is_not_abstract():
    assert not inspect.isabstract(express::statements::MemberCell)


def test_express::statements::membercell_constructor_exists():
    assert callable(express::statements::MemberCell.__init__)


def test_express::statements::membercell_constructor_args():
    sig = inspect.signature(express::statements::MemberCell.__init__)
    params = list(sig.parameters.keys())



def test_core::localscope_is_not_abstract():
    assert not inspect.isabstract(core::LocalScope)


def test_core::localscope_constructor_exists():
    assert callable(core::LocalScope.__init__)


def test_core::localscope_constructor_args():
    sig = inspect.signature(core::LocalScope.__init__)
    params = list(sig.parameters.keys())



def test_express::expressions::queryexpression_is_not_abstract():
    assert not inspect.isabstract(express::expressions::QueryExpression)


def test_express::expressions::queryexpression_constructor_exists():
    assert callable(express::expressions::QueryExpression.__init__)


def test_express::expressions::queryexpression_constructor_args():
    sig = inspect.signature(express::expressions::QueryExpression.__init__)
    params = list(sig.parameters.keys())



def test_algorithms::statement_is_not_abstract():
    assert not inspect.isabstract(algorithms::Statement)


def test_algorithms::statement_constructor_exists():
    assert callable(algorithms::Statement.__init__)


def test_algorithms::statement_constructor_args():
    sig = inspect.signature(algorithms::Statement.__init__)
    params = list(sig.parameters.keys())



def test_express::statements::repeatstatement_is_not_abstract():
    assert not inspect.isabstract(express::statements::RepeatStatement)


def test_express::statements::repeatstatement_constructor_exists():
    assert callable(express::statements::RepeatStatement.__init__)


def test_express::statements::repeatstatement_constructor_args():
    sig = inspect.signature(express::statements::RepeatStatement.__init__)
    params = list(sig.parameters.keys())



def test_express::statements::aliasstatement_is_not_abstract():
    assert not inspect.isabstract(express::statements::AliasStatement)


def test_express::statements::aliasstatement_constructor_exists():
    assert callable(express::statements::AliasStatement.__init__)


def test_express::statements::aliasstatement_constructor_args():
    sig = inspect.signature(express::statements::AliasStatement.__init__)
    params = list(sig.parameters.keys())



def test_controlstatement_is_not_abstract():
    assert not inspect.isabstract(ControlStatement)


def test_controlstatement_constructor_exists():
    assert callable(ControlStatement.__init__)


def test_controlstatement_constructor_args():
    sig = inspect.signature(ControlStatement.__init__)
    params = list(sig.parameters.keys())



def test_express::statements::nullstatement_is_not_abstract():
    assert not inspect.isabstract(express::statements::NullStatement)


def test_express::statements::nullstatement_constructor_exists():
    assert callable(express::statements::NullStatement.__init__)


def test_express::statements::nullstatement_constructor_args():
    sig = inspect.signature(express::statements::NullStatement.__init__)
    params = list(sig.parameters.keys())



def test_express::statements::escapestatement_is_not_abstract():
    assert not inspect.isabstract(express::statements::EscapeStatement)


def test_express::statements::escapestatement_constructor_exists():
    assert callable(express::statements::EscapeStatement.__init__)


def test_express::statements::escapestatement_constructor_args():
    sig = inspect.signature(express::statements::EscapeStatement.__init__)
    params = list(sig.parameters.keys())



def test_express::statements::returnstatement_is_not_abstract():
    assert not inspect.isabstract(express::statements::ReturnStatement)


def test_express::statements::returnstatement_constructor_exists():
    assert callable(express::statements::ReturnStatement.__init__)


def test_express::statements::returnstatement_constructor_args():
    sig = inspect.signature(express::statements::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_express::statements::skipstatement_is_not_abstract():
    assert not inspect.isabstract(express::statements::SkipStatement)


def test_express::statements::skipstatement_constructor_exists():
    assert callable(express::statements::SkipStatement.__init__)


def test_express::statements::skipstatement_constructor_args():
    sig = inspect.signature(express::statements::SkipStatement.__init__)
    params = list(sig.parameters.keys())



def test_express::statements::caseaction_is_not_abstract():
    assert not inspect.isabstract(express::statements::CaseAction)


def test_express::statements::caseaction_constructor_exists():
    assert callable(express::statements::CaseAction.__init__)


def test_express::statements::caseaction_constructor_args():
    sig = inspect.signature(express::statements::CaseAction.__init__)
    params = list(sig.parameters.keys())
    assert "isDefault" in params, "Missing parameter 'isDefault'"

def test_express::statements::caseaction_has_isDefault():
    assert hasattr(express::statements::CaseAction, "isDefault")
    descriptor = None
    for klass in express::statements::CaseAction.__mro__:
        if "isDefault" in klass.__dict__:
            descriptor = klass.__dict__["isDefault"]
            break
    assert isinstance(descriptor, property)



def test_localelement_is_not_abstract():
    assert not inspect.isabstract(LocalElement)


def test_localelement_constructor_exists():
    assert callable(LocalElement.__init__)


def test_localelement_constructor_args():
    sig = inspect.signature(LocalElement.__init__)
    params = list(sig.parameters.keys())



def test_express::algorithms::namedvariable_is_not_abstract():
    assert not inspect.isabstract(express::algorithms::NamedVariable)


def test_express::algorithms::namedvariable_constructor_exists():
    assert callable(express::algorithms::NamedVariable.__init__)


def test_express::algorithms::namedvariable_constructor_args():
    sig = inspect.signature(express::algorithms::NamedVariable.__init__)
    params = list(sig.parameters.keys())



def test_express::algorithms::genericelement_is_not_abstract():
    assert not inspect.isabstract(express::algorithms::GenericElement)


def test_express::algorithms::genericelement_constructor_exists():
    assert callable(express::algorithms::GenericElement.__init__)


def test_express::algorithms::genericelement_constructor_args():
    sig = inspect.signature(express::algorithms::GenericElement.__init__)
    params = list(sig.parameters.keys())



def test_express::algorithms::parameter_is_not_abstract():
    assert not inspect.isabstract(express::algorithms::Parameter)


def test_express::algorithms::parameter_constructor_exists():
    assert callable(express::algorithms::Parameter.__init__)


def test_express::algorithms::parameter_constructor_args():
    sig = inspect.signature(express::algorithms::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "inout" in params, "Missing parameter 'inout'"
    assert "position" in params, "Missing parameter 'position'"

def test_express::algorithms::parameter_has_inout():
    assert hasattr(express::algorithms::Parameter, "inout")
    descriptor = None
    for klass in express::algorithms::Parameter.__mro__:
        if "inout" in klass.__dict__:
            descriptor = klass.__dict__["inout"]
            break
    assert isinstance(descriptor, property)

def test_express::algorithms::parameter_has_position():
    assert hasattr(express::algorithms::Parameter, "position")
    descriptor = None
    for klass in express::algorithms::Parameter.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_express::rules::namedrule_is_not_abstract():
    assert not inspect.isabstract(express::rules::NamedRule)


def test_express::rules::namedrule_constructor_exists():
    assert callable(express::rules::NamedRule.__init__)


def test_express::rules::namedrule_constructor_args():
    sig = inspect.signature(express::rules::NamedRule.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_express::rules::namedrule_has_position():
    assert hasattr(express::rules::NamedRule, "position")
    descriptor = None
    for klass in express::rules::NamedRule.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_namedrule_is_not_abstract():
    assert not inspect.isabstract(NamedRule)


def test_namedrule_constructor_exists():
    assert callable(NamedRule.__init__)


def test_namedrule_constructor_args():
    sig = inspect.signature(NamedRule.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_express::statements::casestatement_is_not_abstract():
    assert not inspect.isabstract(express::statements::CaseStatement)


def test_express::statements::casestatement_constructor_exists():
    assert callable(express::statements::CaseStatement.__init__)


def test_express::statements::casestatement_constructor_args():
    sig = inspect.signature(express::statements::CaseStatement.__init__)
    params = list(sig.parameters.keys())



def test_express::statements::assignment_is_not_abstract():
    assert not inspect.isabstract(express::statements::Assignment)


def test_express::statements::assignment_constructor_exists():
    assert callable(express::statements::Assignment.__init__)


def test_express::statements::assignment_constructor_args():
    sig = inspect.signature(express::statements::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_express::statements::statementblock_is_not_abstract():
    assert not inspect.isabstract(express::statements::StatementBlock)


def test_express::statements::statementblock_constructor_exists():
    assert callable(express::statements::StatementBlock.__init__)


def test_express::statements::statementblock_constructor_args():
    sig = inspect.signature(express::statements::StatementBlock.__init__)
    params = list(sig.parameters.keys())
    assert "delimited" in params, "Missing parameter 'delimited'"

def test_express::statements::statementblock_has_delimited():
    assert hasattr(express::statements::StatementBlock, "delimited")
    descriptor = None
    for klass in express::statements::StatementBlock.__mro__:
        if "delimited" in klass.__dict__:
            descriptor = klass.__dict__["delimited"]
            break
    assert isinstance(descriptor, property)



def test_express::statements::controlstatement_is_not_abstract():
    assert not inspect.isabstract(express::statements::ControlStatement)


def test_express::statements::controlstatement_constructor_exists():
    assert callable(express::statements::ControlStatement.__init__)


def test_express::statements::controlstatement_constructor_args():
    sig = inspect.signature(express::statements::ControlStatement.__init__)
    params = list(sig.parameters.keys())



def test_express::statements::ifstatement_is_not_abstract():
    assert not inspect.isabstract(express::statements::IfStatement)


def test_express::statements::ifstatement_constructor_exists():
    assert callable(express::statements::IfStatement.__init__)


def test_express::statements::ifstatement_constructor_args():
    sig = inspect.signature(express::statements::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_core::algorithmscope_is_not_abstract():
    assert not inspect.isabstract(core::AlgorithmScope)


def test_core::algorithmscope_constructor_exists():
    assert callable(core::AlgorithmScope.__init__)


def test_core::algorithmscope_constructor_args():
    sig = inspect.signature(core::AlgorithmScope.__init__)
    params = list(sig.parameters.keys())



def test_express::algorithms::algorithm_is_not_abstract():
    assert not inspect.isabstract(express::algorithms::Algorithm)


def test_express::algorithms::algorithm_constructor_exists():
    assert callable(express::algorithms::Algorithm.__init__)


def test_express::algorithms::algorithm_constructor_args():
    sig = inspect.signature(express::algorithms::Algorithm.__init__)
    params = list(sig.parameters.keys())



def test_core::schemaelement_is_not_abstract():
    assert not inspect.isabstract(core::SchemaElement)


def test_core::schemaelement_constructor_exists():
    assert callable(core::SchemaElement.__init__)


def test_core::schemaelement_constructor_args():
    sig = inspect.signature(core::SchemaElement.__init__)
    params = list(sig.parameters.keys())



def test_express::rules::globalrule_is_not_abstract():
    assert not inspect.isabstract(express::rules::GlobalRule)


def test_express::rules::globalrule_constructor_exists():
    assert callable(express::rules::GlobalRule.__init__)


def test_express::rules::globalrule_constructor_args():
    sig = inspect.signature(express::rules::GlobalRule.__init__)
    params = list(sig.parameters.keys())



def test_scopedid_is_not_abstract():
    assert not inspect.isabstract(ScopedId)


def test_scopedid_constructor_exists():
    assert callable(ScopedId.__init__)


def test_scopedid_constructor_args():
    sig = inspect.signature(ScopedId.__init__)
    params = list(sig.parameters.keys())



def test_globalrule_is_not_abstract():
    assert not inspect.isabstract(GlobalRule)


def test_globalrule_constructor_exists():
    assert callable(GlobalRule.__init__)


def test_globalrule_constructor_args():
    sig = inspect.signature(GlobalRule.__init__)
    params = list(sig.parameters.keys())



def test_population_is_not_abstract():
    assert not inspect.isabstract(Population)


def test_population_constructor_exists():
    assert callable(Population.__init__)


def test_population_constructor_args():
    sig = inspect.signature(Population.__init__)
    params = list(sig.parameters.keys())



def test_entityinstance_is_not_abstract():
    assert not inspect.isabstract(EntityInstance)


def test_entityinstance_constructor_exists():
    assert callable(EntityInstance.__init__)


def test_entityinstance_constructor_args():
    sig = inspect.signature(EntityInstance.__init__)
    params = list(sig.parameters.keys())



def test_express::instances::singleleafinstance_is_not_abstract():
    assert not inspect.isabstract(express::instances::SingleLeafInstance)


def test_express::instances::singleleafinstance_constructor_exists():
    assert callable(express::instances::SingleLeafInstance.__init__)


def test_express::instances::singleleafinstance_constructor_args():
    sig = inspect.signature(express::instances::SingleLeafInstance.__init__)
    params = list(sig.parameters.keys())



def test_express::instances::multileafinstance_is_not_abstract():
    assert not inspect.isabstract(express::instances::MultiLeafInstance)


def test_express::instances::multileafinstance_constructor_exists():
    assert callable(express::instances::MultiLeafInstance.__init__)


def test_express::instances::multileafinstance_constructor_args():
    sig = inspect.signature(express::instances::MultiLeafInstance.__init__)
    params = list(sig.parameters.keys())



def test_setvalue_is_not_abstract():
    assert not inspect.isabstract(SETValue)


def test_setvalue_constructor_exists():
    assert callable(SETValue.__init__)


def test_setvalue_constructor_args():
    sig = inspect.signature(SETValue.__init__)
    params = list(sig.parameters.keys())



def test_express::rules::extent_is_not_abstract():
    assert not inspect.isabstract(express::rules::Extent)


def test_express::rules::extent_constructor_exists():
    assert callable(express::rules::Extent.__init__)


def test_express::rules::extent_constructor_args():
    sig = inspect.signature(express::rules::Extent.__init__)
    params = list(sig.parameters.keys())



def test_supertyperule_is_not_abstract():
    assert not inspect.isabstract(SupertypeRule)


def test_supertyperule_constructor_exists():
    assert callable(SupertypeRule.__init__)


def test_supertyperule_constructor_args():
    sig = inspect.signature(SupertypeRule.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_express::expressions::primary_is_not_abstract():
    assert not inspect.isabstract(express::expressions::Primary)


def test_express::expressions::primary_constructor_exists():
    assert callable(express::expressions::Primary.__init__)


def test_express::expressions::primary_constructor_args():
    sig = inspect.signature(express::expressions::Primary.__init__)
    params = list(sig.parameters.keys())



def test_express::expressions::aggregateinitializer_is_not_abstract():
    assert not inspect.isabstract(express::expressions::AggregateInitializer)


def test_express::expressions::aggregateinitializer_constructor_exists():
    assert callable(express::expressions::AggregateInitializer.__init__)


def test_express::expressions::aggregateinitializer_constructor_args():
    sig = inspect.signature(express::expressions::AggregateInitializer.__init__)
    params = list(sig.parameters.keys())



def test_express::expressions::selector_is_not_abstract():
    assert not inspect.isabstract(express::expressions::Selector)


def test_express::expressions::selector_constructor_exists():
    assert callable(express::expressions::Selector.__init__)


def test_express::expressions::selector_constructor_args():
    sig = inspect.signature(express::expressions::Selector.__init__)
    params = list(sig.parameters.keys())



def test_express::expressions::functioncall_is_not_abstract():
    assert not inspect.isabstract(express::expressions::FunctionCall)


def test_express::expressions::functioncall_constructor_exists():
    assert callable(express::expressions::FunctionCall.__init__)


def test_express::expressions::functioncall_constructor_args():
    sig = inspect.signature(express::expressions::FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_express::expressions::operation_is_not_abstract():
    assert not inspect.isabstract(express::expressions::Operation)


def test_express::expressions::operation_constructor_exists():
    assert callable(express::expressions::Operation.__init__)


def test_express::expressions::operation_constructor_args():
    sig = inspect.signature(express::expressions::Operation.__init__)
    params = list(sig.parameters.keys())



def test_express::expressions::indexoperation_is_not_abstract():
    assert not inspect.isabstract(express::expressions::IndexOperation)


def test_express::expressions::indexoperation_constructor_exists():
    assert callable(express::expressions::IndexOperation.__init__)


def test_express::expressions::indexoperation_constructor_args():
    sig = inspect.signature(express::expressions::IndexOperation.__init__)
    params = list(sig.parameters.keys())



def test_express::expressions::partialentityconstructor_is_not_abstract():
    assert not inspect.isabstract(express::expressions::PartialEntityConstructor)


def test_express::expressions::partialentityconstructor_constructor_exists():
    assert callable(express::expressions::PartialEntityConstructor.__init__)


def test_express::expressions::partialentityconstructor_constructor_args():
    sig = inspect.signature(express::expressions::PartialEntityConstructor.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_express::expressions::partialentityconstructor_has_id():
    assert hasattr(express::expressions::PartialEntityConstructor, "id")
    descriptor = None
    for klass in express::expressions::PartialEntityConstructor.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_extent_is_not_abstract():
    assert not inspect.isabstract(Extent)


def test_extent_constructor_exists():
    assert callable(Extent.__init__)


def test_extent_constructor_args():
    sig = inspect.signature(Extent.__init__)
    params = list(sig.parameters.keys())



def test_express::rules::subtypeconstraint_is_not_abstract():
    assert not inspect.isabstract(express::rules::SubtypeConstraint)


def test_express::rules::subtypeconstraint_constructor_exists():
    assert callable(express::rules::SubtypeConstraint.__init__)


def test_express::rules::subtypeconstraint_constructor_args():
    sig = inspect.signature(express::rules::SubtypeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_actualparameter_is_not_abstract():
    assert not inspect.isabstract(ActualParameter)


def test_actualparameter_constructor_exists():
    assert callable(ActualParameter.__init__)


def test_actualparameter_constructor_args():
    sig = inspect.signature(ActualParameter.__init__)
    params = list(sig.parameters.keys())



def test_procedure_is_not_abstract():
    assert not inspect.isabstract(Procedure)


def test_procedure_constructor_exists():
    assert callable(Procedure.__init__)


def test_procedure_constructor_args():
    sig = inspect.signature(Procedure.__init__)
    params = list(sig.parameters.keys())



def test_express::statements::procedurecall_is_not_abstract():
    assert not inspect.isabstract(express::statements::ProcedureCall)


def test_express::statements::procedurecall_constructor_exists():
    assert callable(express::statements::ProcedureCall.__init__)


def test_express::statements::procedurecall_constructor_args():
    sig = inspect.signature(express::statements::ProcedureCall.__init__)
    params = list(sig.parameters.keys())



def test_entitytype_is_not_abstract():
    assert not inspect.isabstract(EntityType)


def test_entitytype_constructor_exists():
    assert callable(EntityType.__init__)


def test_entitytype_constructor_args():
    sig = inspect.signature(EntityType.__init__)
    params = list(sig.parameters.keys())



def test_commonelement_is_not_abstract():
    assert not inspect.isabstract(CommonElement)


def test_commonelement_constructor_exists():
    assert callable(CommonElement.__init__)


def test_commonelement_constructor_args():
    sig = inspect.signature(CommonElement.__init__)
    params = list(sig.parameters.keys())



def test_express::instances::constant_is_not_abstract():
    assert not inspect.isabstract(express::instances::Constant)


def test_express::instances::constant_constructor_exists():
    assert callable(express::instances::Constant.__init__)


def test_express::instances::constant_constructor_args():
    sig = inspect.signature(express::instances::Constant.__init__)
    params = list(sig.parameters.keys())



def test_express::rules::supertyperule_is_not_abstract():
    assert not inspect.isabstract(express::rules::SupertypeRule)


def test_express::rules::supertyperule_constructor_exists():
    assert callable(express::rules::SupertypeRule.__init__)


def test_express::rules::supertyperule_constructor_args():
    sig = inspect.signature(express::rules::SupertypeRule.__init__)
    params = list(sig.parameters.keys())
    assert "assertsAbstract" in params, "Missing parameter 'assertsAbstract'"

def test_express::rules::supertyperule_has_assertsAbstract():
    assert hasattr(express::rules::SupertypeRule, "assertsAbstract")
    descriptor = None
    for klass in express::rules::SupertypeRule.__mro__:
        if "assertsAbstract" in klass.__dict__:
            descriptor = klass.__dict__["assertsAbstract"]
            break
    assert isinstance(descriptor, property)



def test_subtypeconstraint_is_not_abstract():
    assert not inspect.isabstract(SubtypeConstraint)


def test_subtypeconstraint_constructor_exists():
    assert callable(SubtypeConstraint.__init__)


def test_subtypeconstraint_constructor_args():
    sig = inspect.signature(SubtypeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_express::rules::andconstraint_is_not_abstract():
    assert not inspect.isabstract(express::rules::ANDConstraint)


def test_express::rules::andconstraint_constructor_exists():
    assert callable(express::rules::ANDConstraint.__init__)


def test_express::rules::andconstraint_constructor_args():
    sig = inspect.signature(express::rules::ANDConstraint.__init__)
    params = list(sig.parameters.keys())



def test_express::rules::total::overconstraint_is_not_abstract():
    assert not inspect.isabstract(express::rules::TOTAL::OVERConstraint)


def test_express::rules::total::overconstraint_constructor_exists():
    assert callable(express::rules::TOTAL::OVERConstraint.__init__)


def test_express::rules::total::overconstraint_constructor_args():
    sig = inspect.signature(express::rules::TOTAL::OVERConstraint.__init__)
    params = list(sig.parameters.keys())



def test_express::rules::oneofconstraint_is_not_abstract():
    assert not inspect.isabstract(express::rules::ONEOFConstraint)


def test_express::rules::oneofconstraint_constructor_exists():
    assert callable(express::rules::ONEOFConstraint.__init__)


def test_express::rules::oneofconstraint_constructor_args():
    sig = inspect.signature(express::rules::ONEOFConstraint.__init__)
    params = list(sig.parameters.keys())


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
express::core::DomainConstraint_strategy = st.builds(
    express::core::DomainConstraint,
)
TypeElement_strategy = st.builds(
    TypeElement,
)
express::core::UniqueRule_strategy = st.builds(
    express::core::UniqueRule,
    position=
        safe_text
)
core::ConcreteType_strategy = st.builds(
    core::ConcreteType,
)
SimpleType_strategy = st.builds(
    SimpleType,
)
express::core::NumericType_strategy = st.builds(
    express::core::NumericType,
)
express::core::Attribute_strategy = st.builds(
    express::core::Attribute,
    position=
        safe_text,
    isAbstract=
        safe_text
)
Relationship_strategy = st.builds(
    Relationship,
)
InverseAttribute_strategy = st.builds(
    InverseAttribute,
)
SchemaElement_strategy = st.builds(
    SchemaElement,
)
InterfacedElement_strategy = st.builds(
    InterfacedElement,
)
Remark_strategy = st.builds(
    Remark,
)
express::core::DataType_strategy = st.builds(
    express::core::DataType,
)
Schema_strategy = st.builds(
    Schema,
)
express::core::InterfacedElement_strategy = st.builds(
    express::core::InterfacedElement,
    isUSE=
        safe_text
)
core::ParameterType_strategy = st.builds(
    core::ParameterType,
)
core::InstantiableType_strategy = st.builds(
    core::InstantiableType,
)
core::NamedType_strategy = st.builds(
    core::NamedType,
)
express::core::DefinedType_strategy = st.builds(
    express::core::DefinedType,
)
express::core::EntityType_strategy = st.builds(
    express::core::EntityType,
    isAbstract=
        safe_text
)
Role_strategy = st.builds(
    Role,
)
express::core::DomainRole_strategy = st.builds(
    express::core::DomainRole,
)
Redeclaration_strategy = st.builds(
    Redeclaration,
)
AttributeType_strategy = st.builds(
    AttributeType,
)
express::core::Redeclaration_strategy = st.builds(
    express::core::Redeclaration,
    position=
        safe_text,
    isMandatory=
        safe_text
)
ConcreteAggregationType_strategy = st.builds(
    ConcreteAggregationType,
)
express::core::LISTType_strategy = st.builds(
    express::core::LISTType,
)
UniqueRule_strategy = st.builds(
    UniqueRule,
)
RangeRole_strategy = st.builds(
    RangeRole,
)
DefinedType_strategy = st.builds(
    DefinedType,
)
express::core::EnumerationType_strategy = st.builds(
    express::core::EnumerationType,
    isExtensible=
        safe_text
)
InvertibleAttribute_strategy = st.builds(
    InvertibleAttribute,
)
DomainRole_strategy = st.builds(
    DomainRole,
)
DataType_strategy = st.builds(
    DataType,
)
express::core::PartialEntityType_strategy = st.builds(
    express::core::PartialEntityType,
)
Scope_strategy = st.builds(
    Scope,
)
express::core::Schema_strategy = st.builds(
    express::core::Schema,
    name=
        safe_text,
    version=
        safe_text
)
Instance_strategy = st.builds(
    Instance,
)
express::core::Expression_strategy = st.builds(
    express::core::Expression,
    text=
        safe_text
)
InstantiableType_strategy = st.builds(
    InstantiableType,
)
express::core::ConcreteType_strategy = st.builds(
    express::core::ConcreteType,
)
core::AggregationType_strategy = st.builds(
    core::AggregationType,
)
core::GeneralizedType_strategy = st.builds(
    core::GeneralizedType,
)
express::core::GeneralAggregationType_strategy = st.builds(
    express::core::GeneralAggregationType,
)
core::TypeElement_strategy = st.builds(
    core::TypeElement,
)
core::DomainConstraint_strategy = st.builds(
    core::DomainConstraint,
)
express::core::DomainRule_strategy = st.builds(
    express::core::DomainRule,
    position=
        safe_text
)
SingleEntityValue_strategy = st.builds(
    SingleEntityValue,
)
express::instances::PartialEntityValue_strategy = st.builds(
    express::instances::PartialEntityValue,
)
express::instances::ConcreteValue_strategy = st.builds(
    express::instances::ConcreteValue,
)
instances::AggregateValue_strategy = st.builds(
    instances::AggregateValue,
)
core::Instance_strategy = st.builds(
    core::Instance,
)
express::instances::LISTValue_strategy = st.builds(
    express::instances::LISTValue,
)
LogicalValue_strategy = st.builds(
    LogicalValue,
)
express::instances::BooleanValue_strategy = st.builds(
    express::instances::BooleanValue,
)
NumberValue_strategy = st.builds(
    NumberValue,
)
express::instances::RealValue_strategy = st.builds(
    express::instances::RealValue,
)
express::instances::Population_strategy = st.builds(
    express::instances::Population,
)
express::instances::ArrayMember_strategy = st.builds(
    express::instances::ArrayMember,
    index=
        safe_text
)
instances::ConcreteValue_strategy = st.builds(
    instances::ConcreteValue,
)
instances::TypedInstance_strategy = st.builds(
    instances::TypedInstance,
)
express::instances::EnumerationItem_strategy = st.builds(
    express::instances::EnumerationItem,
    position=
        safe_text
)
BagMember_strategy = st.builds(
    BagMember,
)
LISTValue_strategy = st.builds(
    LISTValue,
)
express::instances::GenericAggregate_strategy = st.builds(
    express::instances::GenericAggregate,
)
express::instances::Indeterminate_strategy = st.builds(
    express::instances::Indeterminate,
)
express::instances::SingleEntityValue_strategy = st.builds(
    express::instances::SingleEntityValue,
)
express::instances::BagMember_strategy = st.builds(
    express::instances::BagMember,
    count=
        safe_text
)
express::instances::ListMember_strategy = st.builds(
    express::instances::ListMember,
    position=
        safe_text
)
EntityValue_strategy = st.builds(
    EntityValue,
)
TypedInstance_strategy = st.builds(
    TypedInstance,
)
express::instances::SpecializedValue_strategy = st.builds(
    express::instances::SpecializedValue,
)
express::instances::EntityInstance_strategy = st.builds(
    express::instances::EntityInstance,
    id=
        safe_text
)
StringValue_strategy = st.builds(
    StringValue,
)
express::instances::TypeName_strategy = st.builds(
    express::instances::TypeName,
)
express::instances::RoleName_strategy = st.builds(
    express::instances::RoleName,
)
ArrayMember_strategy = st.builds(
    ArrayMember,
)
AggregateValue_strategy = st.builds(
    AggregateValue,
)
express::instances::BAGValue_strategy = st.builds(
    express::instances::BAGValue,
)
express::instances::SETValue_strategy = st.builds(
    express::instances::SETValue,
)
express::instances::ARRAYValue_strategy = st.builds(
    express::instances::ARRAYValue,
)
express::instances::AttributeValue_strategy = st.builds(
    express::instances::AttributeValue,
)
core::GenericType_strategy = st.builds(
    core::GenericType,
)
algorithms::Parameter_strategy = st.builds(
    algorithms::Parameter,
)
express::instances::TypedInstance_strategy = st.builds(
    express::instances::TypedInstance,
)
ConcreteValue_strategy = st.builds(
    ConcreteValue,
)
express::instances::SimpleValue_strategy = st.builds(
    express::instances::SimpleValue,
    name=
        safe_text
)
express::instances::AggregateValue_strategy = st.builds(
    express::instances::AggregateValue,
)
RealValue_strategy = st.builds(
    RealValue,
)
express::instances::IntegerValue_strategy = st.builds(
    express::instances::IntegerValue,
)
AGGREGATEType_strategy = st.builds(
    AGGREGATEType,
)
express::algorithms::ActualStructureConstraint_strategy = st.builds(
    express::algorithms::ActualStructureConstraint,
    label=
        safe_text
)
ActualStructure_strategy = st.builds(
    ActualStructure,
)
express::algorithms::VARVariable_strategy = st.builds(
    express::algorithms::VARVariable,
)
core::ActualType_strategy = st.builds(
    core::ActualType,
)
express::algorithms::ActualAggregationType_strategy = st.builds(
    express::algorithms::ActualAggregationType,
)
EscapeStatement_strategy = st.builds(
    EscapeStatement,
)
SkipStatement_strategy = st.builds(
    SkipStatement,
)
StatementBlock_strategy = st.builds(
    StatementBlock,
)
express::algorithms::Statement_strategy = st.builds(
    express::algorithms::Statement,
    text=
        safe_text
)
ActualType_strategy = st.builds(
    ActualType,
)
express::algorithms::ActualAGGREGATEType_strategy = st.builds(
    express::algorithms::ActualAGGREGATEType,
    label=
        safe_text
)
express::algorithms::ActualGenericType_strategy = st.builds(
    express::algorithms::ActualGenericType,
    isEntity=
        safe_text,
    label=
        safe_text
)
core::AGGREGATEType_strategy = st.builds(
    core::AGGREGATEType,
)
algorithms::GenericElement_strategy = st.builds(
    algorithms::GenericElement,
)
express::algorithms::ActualDataType_strategy = st.builds(
    express::algorithms::ActualDataType,
)
express::algorithms::ActualStructure_strategy = st.builds(
    express::algorithms::ActualStructure,
)
InVariable_strategy = st.builds(
    InVariable,
)
ActualDataType_strategy = st.builds(
    ActualDataType,
)
GenericType_strategy = st.builds(
    GenericType,
)
ActualAggregationType_strategy = st.builds(
    ActualAggregationType,
)
express::algorithms::ActualBAGType_strategy = st.builds(
    express::algorithms::ActualBAGType,
)
express::algorithms::ActualSETType_strategy = st.builds(
    express::algorithms::ActualSETType,
)
express::algorithms::ActualLISTType_strategy = st.builds(
    express::algorithms::ActualLISTType,
)
express::algorithms::ActualARRAYType_strategy = st.builds(
    express::algorithms::ActualARRAYType,
    isOptional=
        safe_text
)
InParameter_strategy = st.builds(
    InParameter,
)
RepeatStatement_strategy = st.builds(
    RepeatStatement,
)
core::AnonymousType_strategy = st.builds(
    core::AnonymousType,
)
express::core::ConcreteAggregationType_strategy = st.builds(
    express::core::ConcreteAggregationType,
)
AlgorithmScope_strategy = st.builds(
    AlgorithmScope,
)
express::core::CommonElement_strategy = st.builds(
    express::core::CommonElement,
)
Algorithm_strategy = st.builds(
    Algorithm,
)
express::algorithms::Procedure_strategy = st.builds(
    express::algorithms::Procedure,
)
express::algorithms::Function_strategy = st.builds(
    express::algorithms::Function,
)
express::algorithms::ActualTypeConstraint_strategy = st.builds(
    express::algorithms::ActualTypeConstraint,
    label=
        safe_text
)
express::core::ARRAYType_strategy = st.builds(
    express::core::ARRAYType,
    isOptional=
        safe_text
)
express::core::AggregationType_strategy = st.builds(
    express::core::AggregationType,
    ordering=
        safe_text,
    isUnique=
        safe_text
)
express::core::ScopedId_strategy = st.builds(
    express::core::ScopedId,
    localName=
        safe_text
)
express::core::BinaryType_strategy = st.builds(
    express::core::BinaryType,
)
DomainRule_strategy = st.builds(
    DomainRule,
)
SelectType_strategy = st.builds(
    SelectType,
)
core::CommonElement_strategy = st.builds(
    core::CommonElement,
)
core::Scope_strategy = st.builds(
    core::Scope,
)
express::core::LocalScope_strategy = st.builds(
    express::core::LocalScope,
)
express::core::Relationship_strategy = st.builds(
    express::core::Relationship,
)
express::core::SelectType_strategy = st.builds(
    express::core::SelectType,
    isExtensible=
        safe_text,
    isEntity=
        safe_text
)
express::core::ParameterType_strategy = st.builds(
    express::core::ParameterType,
)
express::core::Scope_strategy = st.builds(
    express::core::Scope,
)
express::core::Role_strategy = st.builds(
    express::core::Role,
)
express::core::Remark_strategy = st.builds(
    express::core::Remark,
    isTagged=
        safe_text,
    text=
        safe_text,
    isTail=
        safe_text
)
express::core::RangeRole_strategy = st.builds(
    express::core::RangeRole,
)
ArrayBound_strategy = st.builds(
    ArrayBound,
)
ConcreteType_strategy = st.builds(
    ConcreteType,
)
express::core::SpecializedType_strategy = st.builds(
    express::core::SpecializedType,
)
express::core::SETType_strategy = st.builds(
    express::core::SETType,
)
LocalScope_strategy = st.builds(
    LocalScope,
)
express::core::AlgorithmScope_strategy = st.builds(
    express::core::AlgorithmScope,
)
AnonymousType_strategy = st.builds(
    AnonymousType,
)
express::core::SimpleType_strategy = st.builds(
    express::core::SimpleType,
    id=
        safe_text
)
express::core::AnonymousType_strategy = st.builds(
    express::core::AnonymousType,
)
LengthConstraint_strategy = st.builds(
    LengthConstraint,
)
express::core::StringType_strategy = st.builds(
    express::core::StringType,
)
ActualTypeConstraint_strategy = st.builds(
    ActualTypeConstraint,
)
express::core::LogicType_strategy = st.builds(
    express::core::LogicType,
)
NumericType_strategy = st.builds(
    NumericType,
)
express::core::RealType_strategy = st.builds(
    express::core::RealType,
    precision=
        safe_text
)
express::core::BAGType_strategy = st.builds(
    express::core::BAGType,
)
DomainConstraint_strategy = st.builds(
    DomainConstraint,
)
express::core::LengthConstraint_strategy = st.builds(
    express::core::LengthConstraint,
    maxLength=
        safe_text,
    isFixed=
        safe_text
)
express::core::SizeConstraint_strategy = st.builds(
    express::core::SizeConstraint,
    bound=
        safe_text
)
express::core::AttributeType_strategy = st.builds(
    express::core::AttributeType,
)
express::core::Instance_strategy = st.builds(
    express::core::Instance,
)
express::core::NamedElement_strategy = st.builds(
    express::core::NamedElement,
)
core::VariableType_strategy = st.builds(
    core::VariableType,
)
express::core::InstantiableType_strategy = st.builds(
    express::core::InstantiableType,
)
GeneralAggregationType_strategy = st.builds(
    GeneralAggregationType,
)
express::core::GeneralLISTType_strategy = st.builds(
    express::core::GeneralLISTType,
)
express::core::GeneralSETType_strategy = st.builds(
    express::core::GeneralSETType,
)
express::core::GeneralARRAYType_strategy = st.builds(
    express::core::GeneralARRAYType,
    isOptional=
        safe_text
)
express::core::GeneralBAGType_strategy = st.builds(
    express::core::GeneralBAGType,
)
ActualStructureConstraint_strategy = st.builds(
    ActualStructureConstraint,
)
ParameterType_strategy = st.builds(
    ParameterType,
)
express::core::ArrayBound_strategy = st.builds(
    express::core::ArrayBound,
    bound=
        safe_text
)
core::AttributeType_strategy = st.builds(
    core::AttributeType,
)
express::core::NamedType_strategy = st.builds(
    express::core::NamedType,
)
express::core::GeneralizedType_strategy = st.builds(
    express::core::GeneralizedType,
)
core::DataType_strategy = st.builds(
    core::DataType,
)
express::core::VariableType_strategy = st.builds(
    express::core::VariableType,
)
EnumerationType_strategy = st.builds(
    EnumerationType,
)
NamedType_strategy = st.builds(
    NamedType,
)
ListMember_strategy = st.builds(
    ListMember,
)
RepeatCount_strategy = st.builds(
    RepeatCount,
)
express::expressions::MemberBinding_strategy = st.builds(
    express::expressions::MemberBinding,
    position=
        safe_text
)
FunctionResult_strategy = st.builds(
    FunctionResult,
)
Function_strategy = st.builds(
    Function,
)
SizeConstraint_strategy = st.builds(
    SizeConstraint,
)
GeneralizedType_strategy = st.builds(
    GeneralizedType,
)
express::core::GenericType_strategy = st.builds(
    express::core::GenericType,
    isEntity=
        safe_text
)
express::core::AGGREGATEType_strategy = st.builds(
    express::core::AGGREGATEType,
)
PartialEntityType_strategy = st.builds(
    PartialEntityType,
)
express::core::SingleEntityType_strategy = st.builds(
    express::core::SingleEntityType,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
express::core::LocalElement_strategy = st.builds(
    express::core::LocalElement,
)
express::core::SchemaElement_strategy = st.builds(
    express::core::SchemaElement,
)
express::core::TypeElement_strategy = st.builds(
    express::core::TypeElement,
)
core::Expression_strategy = st.builds(
    core::Expression,
)
Constant_strategy = st.builds(
    Constant,
)
Attribute_strategy = st.builds(
    Attribute,
)
express::core::DerivedAttribute_strategy = st.builds(
    express::core::DerivedAttribute,
)
express::core::InverseAttribute_strategy = st.builds(
    express::core::InverseAttribute,
    isUnique=
        safe_text
)
express::core::ExplicitAttribute_strategy = st.builds(
    express::core::ExplicitAttribute,
    isOptional=
        safe_text
)
Selector_strategy = st.builds(
    Selector,
)
express::expressions::UsedInRef_strategy = st.builds(
    express::expressions::UsedInRef,
)
express::expressions::GroupRef_strategy = st.builds(
    express::expressions::GroupRef,
    id=
        safe_text
)
express::expressions::AttributeRef_strategy = st.builds(
    express::expressions::AttributeRef,
    id=
        safe_text
)
AttributeValue_strategy = st.builds(
    AttributeValue,
)
express::expressions::AttributeBinding_strategy = st.builds(
    express::expressions::AttributeBinding,
    position=
        safe_text
)
QueryVariable_strategy = st.builds(
    QueryVariable,
)
VariableType_strategy = st.builds(
    VariableType,
)
express::core::ActualType_strategy = st.builds(
    express::core::ActualType,
)
AttributeBinding_strategy = st.builds(
    AttributeBinding,
)
PartialEntityValue_strategy = st.builds(
    PartialEntityValue,
)
express::instances::EntityValue_strategy = st.builds(
    express::instances::EntityValue,
)
MemberBinding_strategy = st.builds(
    MemberBinding,
)
GenericAggregate_strategy = st.builds(
    GenericAggregate,
)
Operation_strategy = st.builds(
    Operation,
)
express::expressions::UnaryOperation_strategy = st.builds(
    express::expressions::UnaryOperation,
    operator=
        safe_text
)
express::expressions::Coercion_strategy = st.builds(
    express::expressions::Coercion,
)
express::expressions::BinaryOperation_strategy = st.builds(
    express::expressions::BinaryOperation,
    operator=
        safe_text
)
Parameter_strategy = st.builds(
    Parameter,
)
express::algorithms::InParameter_strategy = st.builds(
    express::algorithms::InParameter,
)
FunctionCall_strategy = st.builds(
    FunctionCall,
)
ProcedureCall_strategy = st.builds(
    ProcedureCall,
)
express::expressions::ActualParameter_strategy = st.builds(
    express::expressions::ActualParameter,
    position=
        safe_text
)
IndexOperation_strategy = st.builds(
    IndexOperation,
)
express::expressions::StringIndex_strategy = st.builds(
    express::expressions::StringIndex,
)
express::expressions::AggregateIndex_strategy = st.builds(
    express::expressions::AggregateIndex,
)
express::expressions::BinaryIndex_strategy = st.builds(
    express::expressions::BinaryIndex,
)
SimpleValue_strategy = st.builds(
    SimpleValue,
)
express::instances::BinaryValue_strategy = st.builds(
    express::instances::BinaryValue,
)
express::instances::NumberValue_strategy = st.builds(
    express::instances::NumberValue,
)
express::instances::LogicalValue_strategy = st.builds(
    express::instances::LogicalValue,
)
express::instances::StringValue_strategy = st.builds(
    express::instances::StringValue,
)
EnumerationItem_strategy = st.builds(
    EnumerationItem,
)
Primary_strategy = st.builds(
    Primary,
)
express::expressions::ExtentRef_strategy = st.builds(
    express::expressions::ExtentRef,
    id=
        safe_text
)
express::expressions::Literal_strategy = st.builds(
    express::expressions::Literal,
)
express::expressions::VariableRef_strategy = st.builds(
    express::expressions::VariableRef,
    id=
        safe_text
)
express::expressions::ConstantRef_strategy = st.builds(
    express::expressions::ConstantRef,
    id=
        safe_text
)
express::expressions::IndeterminateRef_strategy = st.builds(
    express::expressions::IndeterminateRef,
)
express::expressions::ParameterRef_strategy = st.builds(
    express::expressions::ParameterRef,
    id=
        safe_text
)
express::expressions::EnumItemRef_strategy = st.builds(
    express::expressions::EnumItemRef,
    id=
        safe_text
)
express::expressions::RepeatCount_strategy = st.builds(
    express::expressions::RepeatCount,
)
express::expressions::SELFRef_strategy = st.builds(
    express::expressions::SELFRef,
)
Indeterminate_strategy = st.builds(
    Indeterminate,
)
CaseAction_strategy = st.builds(
    CaseAction,
)
Variable_strategy = st.builds(
    Variable,
)
express::algorithms::InVariable_strategy = st.builds(
    express::algorithms::InVariable,
)
express::algorithms::FunctionResult_strategy = st.builds(
    express::algorithms::FunctionResult,
)
express::algorithms::LocalVariable_strategy = st.builds(
    express::algorithms::LocalVariable,
)
SingleEntityType_strategy = st.builds(
    SingleEntityType,
)
ControlVariable_strategy = st.builds(
    ControlVariable,
)
ExplicitAttribute_strategy = st.builds(
    ExplicitAttribute,
)
express::core::InvertibleAttribute_strategy = st.builds(
    express::core::InvertibleAttribute,
)
express::statements::VARExpression_strategy = st.builds(
    express::statements::VARExpression,
    text=
        safe_text
)
VARVariable_strategy = st.builds(
    VARVariable,
)
algorithms::VARVariable_strategy = st.builds(
    algorithms::VARVariable,
)
express::algorithms::VARParameter_strategy = st.builds(
    express::algorithms::VARParameter,
)
algorithms::NamedVariable_strategy = st.builds(
    algorithms::NamedVariable,
)
express::statements::AliasVariable_strategy = st.builds(
    express::statements::AliasVariable,
)
NamedVariable_strategy = st.builds(
    NamedVariable,
)
express::algorithms::Variable_strategy = st.builds(
    express::algorithms::Variable,
)
express::expressions::QueryVariable_strategy = st.builds(
    express::expressions::QueryVariable,
)
express::statements::ControlVariable_strategy = st.builds(
    express::statements::ControlVariable,
)
AliasVariable_strategy = st.builds(
    AliasVariable,
)
VARExpression_strategy = st.builds(
    VARExpression,
)
express::statements::VariableCell_strategy = st.builds(
    express::statements::VariableCell,
    id=
        safe_text
)
express::statements::GroupCell_strategy = st.builds(
    express::statements::GroupCell,
    id=
        safe_text
)
express::statements::AttributeCell_strategy = st.builds(
    express::statements::AttributeCell,
    id=
        safe_text
)
express::statements::VARCell_strategy = st.builds(
    express::statements::VARCell,
    id=
        safe_text
)
express::statements::MemberCell_strategy = st.builds(
    express::statements::MemberCell,
)
core::LocalScope_strategy = st.builds(
    core::LocalScope,
)
express::expressions::QueryExpression_strategy = st.builds(
    express::expressions::QueryExpression,
)
algorithms::Statement_strategy = st.builds(
    algorithms::Statement,
)
express::statements::RepeatStatement_strategy = st.builds(
    express::statements::RepeatStatement,
)
express::statements::AliasStatement_strategy = st.builds(
    express::statements::AliasStatement,
)
ControlStatement_strategy = st.builds(
    ControlStatement,
)
express::statements::NullStatement_strategy = st.builds(
    express::statements::NullStatement,
)
express::statements::EscapeStatement_strategy = st.builds(
    express::statements::EscapeStatement,
)
express::statements::ReturnStatement_strategy = st.builds(
    express::statements::ReturnStatement,
)
express::statements::SkipStatement_strategy = st.builds(
    express::statements::SkipStatement,
)
express::statements::CaseAction_strategy = st.builds(
    express::statements::CaseAction,
    isDefault=
        safe_text
)
LocalElement_strategy = st.builds(
    LocalElement,
)
express::algorithms::NamedVariable_strategy = st.builds(
    express::algorithms::NamedVariable,
)
express::algorithms::GenericElement_strategy = st.builds(
    express::algorithms::GenericElement,
)
express::algorithms::Parameter_strategy = st.builds(
    express::algorithms::Parameter,
    inout=
        safe_text,
    position=
        safe_text
)
express::rules::NamedRule_strategy = st.builds(
    express::rules::NamedRule,
    position=
        safe_text
)
NamedRule_strategy = st.builds(
    NamedRule,
)
Statement_strategy = st.builds(
    Statement,
)
express::statements::CaseStatement_strategy = st.builds(
    express::statements::CaseStatement,
)
express::statements::Assignment_strategy = st.builds(
    express::statements::Assignment,
)
express::statements::StatementBlock_strategy = st.builds(
    express::statements::StatementBlock,
    delimited=
        safe_text
)
express::statements::ControlStatement_strategy = st.builds(
    express::statements::ControlStatement,
)
express::statements::IfStatement_strategy = st.builds(
    express::statements::IfStatement,
)
core::AlgorithmScope_strategy = st.builds(
    core::AlgorithmScope,
)
express::algorithms::Algorithm_strategy = st.builds(
    express::algorithms::Algorithm,
)
core::SchemaElement_strategy = st.builds(
    core::SchemaElement,
)
express::rules::GlobalRule_strategy = st.builds(
    express::rules::GlobalRule,
)
ScopedId_strategy = st.builds(
    ScopedId,
)
GlobalRule_strategy = st.builds(
    GlobalRule,
)
Population_strategy = st.builds(
    Population,
)
EntityInstance_strategy = st.builds(
    EntityInstance,
)
express::instances::SingleLeafInstance_strategy = st.builds(
    express::instances::SingleLeafInstance,
)
express::instances::MultiLeafInstance_strategy = st.builds(
    express::instances::MultiLeafInstance,
)
SETValue_strategy = st.builds(
    SETValue,
)
express::rules::Extent_strategy = st.builds(
    express::rules::Extent,
)
SupertypeRule_strategy = st.builds(
    SupertypeRule,
)
Expression_strategy = st.builds(
    Expression,
)
express::expressions::Primary_strategy = st.builds(
    express::expressions::Primary,
)
express::expressions::AggregateInitializer_strategy = st.builds(
    express::expressions::AggregateInitializer,
)
express::expressions::Selector_strategy = st.builds(
    express::expressions::Selector,
)
express::expressions::FunctionCall_strategy = st.builds(
    express::expressions::FunctionCall,
)
express::expressions::Operation_strategy = st.builds(
    express::expressions::Operation,
)
express::expressions::IndexOperation_strategy = st.builds(
    express::expressions::IndexOperation,
)
express::expressions::PartialEntityConstructor_strategy = st.builds(
    express::expressions::PartialEntityConstructor,
    id=
        safe_text
)
Extent_strategy = st.builds(
    Extent,
)
express::rules::SubtypeConstraint_strategy = st.builds(
    express::rules::SubtypeConstraint,
)
ActualParameter_strategy = st.builds(
    ActualParameter,
)
Procedure_strategy = st.builds(
    Procedure,
)
express::statements::ProcedureCall_strategy = st.builds(
    express::statements::ProcedureCall,
)
EntityType_strategy = st.builds(
    EntityType,
)
CommonElement_strategy = st.builds(
    CommonElement,
)
express::instances::Constant_strategy = st.builds(
    express::instances::Constant,
)
express::rules::SupertypeRule_strategy = st.builds(
    express::rules::SupertypeRule,
    assertsAbstract=
        safe_text
)
SubtypeConstraint_strategy = st.builds(
    SubtypeConstraint,
)
express::rules::ANDConstraint_strategy = st.builds(
    express::rules::ANDConstraint,
)
express::rules::TOTAL::OVERConstraint_strategy = st.builds(
    express::rules::TOTAL::OVERConstraint,
)
express::rules::ONEOFConstraint_strategy = st.builds(
    express::rules::ONEOFConstraint,
)

@given(instance=express::core::DomainConstraint_strategy)
@settings(max_examples=50)
def test_express::core::domainconstraint_instantiation(instance):
    assert isinstance(instance, express::core::DomainConstraint)

@given(instance=TypeElement_strategy)
@settings(max_examples=50)
def test_typeelement_instantiation(instance):
    assert isinstance(instance, TypeElement)

@given(instance=express::core::UniqueRule_strategy)
@settings(max_examples=50)
def test_express::core::uniquerule_instantiation(instance):
    assert isinstance(instance, express::core::UniqueRule)

@given(instance=express::core::UniqueRule_strategy)
def test_express::core::uniquerule_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=express::core::UniqueRule_strategy)
def test_express::core::uniquerule_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=core::ConcreteType_strategy)
@settings(max_examples=50)
def test_core::concretetype_instantiation(instance):
    assert isinstance(instance, core::ConcreteType)

@given(instance=SimpleType_strategy)
@settings(max_examples=50)
def test_simpletype_instantiation(instance):
    assert isinstance(instance, SimpleType)

@given(instance=express::core::NumericType_strategy)
@settings(max_examples=50)
def test_express::core::numerictype_instantiation(instance):
    assert isinstance(instance, express::core::NumericType)

@given(instance=express::core::Attribute_strategy)
@settings(max_examples=50)
def test_express::core::attribute_instantiation(instance):
    assert isinstance(instance, express::core::Attribute)

@given(instance=express::core::Attribute_strategy)
def test_express::core::attribute_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=express::core::Attribute_strategy)
def test_express::core::attribute_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=express::core::Attribute_strategy)
def test_express::core::attribute_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=express::core::Attribute_strategy)
def test_express::core::attribute_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=Relationship_strategy)
@settings(max_examples=50)
def test_relationship_instantiation(instance):
    assert isinstance(instance, Relationship)

@given(instance=InverseAttribute_strategy)
@settings(max_examples=50)
def test_inverseattribute_instantiation(instance):
    assert isinstance(instance, InverseAttribute)

@given(instance=SchemaElement_strategy)
@settings(max_examples=50)
def test_schemaelement_instantiation(instance):
    assert isinstance(instance, SchemaElement)

@given(instance=InterfacedElement_strategy)
@settings(max_examples=50)
def test_interfacedelement_instantiation(instance):
    assert isinstance(instance, InterfacedElement)

@given(instance=Remark_strategy)
@settings(max_examples=50)
def test_remark_instantiation(instance):
    assert isinstance(instance, Remark)

@given(instance=express::core::DataType_strategy)
@settings(max_examples=50)
def test_express::core::datatype_instantiation(instance):
    assert isinstance(instance, express::core::DataType)

@given(instance=Schema_strategy)
@settings(max_examples=50)
def test_schema_instantiation(instance):
    assert isinstance(instance, Schema)

@given(instance=express::core::InterfacedElement_strategy)
@settings(max_examples=50)
def test_express::core::interfacedelement_instantiation(instance):
    assert isinstance(instance, express::core::InterfacedElement)

@given(instance=express::core::InterfacedElement_strategy)
def test_express::core::interfacedelement_isUSE_type(instance):
    assert isinstance(instance.isUSE, str)


@given(instance=express::core::InterfacedElement_strategy)
def test_express::core::interfacedelement_isUSE_setter(instance):
    original = instance.isUSE
    instance.isUSE = original
    assert instance.isUSE == original

@given(instance=core::ParameterType_strategy)
@settings(max_examples=50)
def test_core::parametertype_instantiation(instance):
    assert isinstance(instance, core::ParameterType)

@given(instance=core::InstantiableType_strategy)
@settings(max_examples=50)
def test_core::instantiabletype_instantiation(instance):
    assert isinstance(instance, core::InstantiableType)

@given(instance=core::NamedType_strategy)
@settings(max_examples=50)
def test_core::namedtype_instantiation(instance):
    assert isinstance(instance, core::NamedType)

@given(instance=express::core::DefinedType_strategy)
@settings(max_examples=50)
def test_express::core::definedtype_instantiation(instance):
    assert isinstance(instance, express::core::DefinedType)

@given(instance=express::core::EntityType_strategy)
@settings(max_examples=50)
def test_express::core::entitytype_instantiation(instance):
    assert isinstance(instance, express::core::EntityType)

@given(instance=express::core::EntityType_strategy)
def test_express::core::entitytype_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=express::core::EntityType_strategy)
def test_express::core::entitytype_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=Role_strategy)
@settings(max_examples=50)
def test_role_instantiation(instance):
    assert isinstance(instance, Role)

@given(instance=express::core::DomainRole_strategy)
@settings(max_examples=50)
def test_express::core::domainrole_instantiation(instance):
    assert isinstance(instance, express::core::DomainRole)

@given(instance=Redeclaration_strategy)
@settings(max_examples=50)
def test_redeclaration_instantiation(instance):
    assert isinstance(instance, Redeclaration)

@given(instance=AttributeType_strategy)
@settings(max_examples=50)
def test_attributetype_instantiation(instance):
    assert isinstance(instance, AttributeType)

@given(instance=express::core::Redeclaration_strategy)
@settings(max_examples=50)
def test_express::core::redeclaration_instantiation(instance):
    assert isinstance(instance, express::core::Redeclaration)

@given(instance=express::core::Redeclaration_strategy)
def test_express::core::redeclaration_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=express::core::Redeclaration_strategy)
def test_express::core::redeclaration_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=express::core::Redeclaration_strategy)
def test_express::core::redeclaration_isMandatory_type(instance):
    assert isinstance(instance.isMandatory, str)


@given(instance=express::core::Redeclaration_strategy)
def test_express::core::redeclaration_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=ConcreteAggregationType_strategy)
@settings(max_examples=50)
def test_concreteaggregationtype_instantiation(instance):
    assert isinstance(instance, ConcreteAggregationType)

@given(instance=express::core::LISTType_strategy)
@settings(max_examples=50)
def test_express::core::listtype_instantiation(instance):
    assert isinstance(instance, express::core::LISTType)

@given(instance=UniqueRule_strategy)
@settings(max_examples=50)
def test_uniquerule_instantiation(instance):
    assert isinstance(instance, UniqueRule)

@given(instance=RangeRole_strategy)
@settings(max_examples=50)
def test_rangerole_instantiation(instance):
    assert isinstance(instance, RangeRole)

@given(instance=DefinedType_strategy)
@settings(max_examples=50)
def test_definedtype_instantiation(instance):
    assert isinstance(instance, DefinedType)

@given(instance=express::core::EnumerationType_strategy)
@settings(max_examples=50)
def test_express::core::enumerationtype_instantiation(instance):
    assert isinstance(instance, express::core::EnumerationType)

@given(instance=express::core::EnumerationType_strategy)
def test_express::core::enumerationtype_isExtensible_type(instance):
    assert isinstance(instance.isExtensible, str)


@given(instance=express::core::EnumerationType_strategy)
def test_express::core::enumerationtype_isExtensible_setter(instance):
    original = instance.isExtensible
    instance.isExtensible = original
    assert instance.isExtensible == original

@given(instance=InvertibleAttribute_strategy)
@settings(max_examples=50)
def test_invertibleattribute_instantiation(instance):
    assert isinstance(instance, InvertibleAttribute)

@given(instance=DomainRole_strategy)
@settings(max_examples=50)
def test_domainrole_instantiation(instance):
    assert isinstance(instance, DomainRole)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=express::core::PartialEntityType_strategy)
@settings(max_examples=50)
def test_express::core::partialentitytype_instantiation(instance):
    assert isinstance(instance, express::core::PartialEntityType)

@given(instance=Scope_strategy)
@settings(max_examples=50)
def test_scope_instantiation(instance):
    assert isinstance(instance, Scope)

@given(instance=express::core::Schema_strategy)
@settings(max_examples=50)
def test_express::core::schema_instantiation(instance):
    assert isinstance(instance, express::core::Schema)

@given(instance=express::core::Schema_strategy)
def test_express::core::schema_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=express::core::Schema_strategy)
def test_express::core::schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=express::core::Schema_strategy)
def test_express::core::schema_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=express::core::Schema_strategy)
def test_express::core::schema_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=Instance_strategy)
@settings(max_examples=50)
def test_instance_instantiation(instance):
    assert isinstance(instance, Instance)

@given(instance=express::core::Expression_strategy)
@settings(max_examples=50)
def test_express::core::expression_instantiation(instance):
    assert isinstance(instance, express::core::Expression)

@given(instance=express::core::Expression_strategy)
def test_express::core::expression_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=express::core::Expression_strategy)
def test_express::core::expression_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=InstantiableType_strategy)
@settings(max_examples=50)
def test_instantiabletype_instantiation(instance):
    assert isinstance(instance, InstantiableType)

@given(instance=express::core::ConcreteType_strategy)
@settings(max_examples=50)
def test_express::core::concretetype_instantiation(instance):
    assert isinstance(instance, express::core::ConcreteType)

@given(instance=core::AggregationType_strategy)
@settings(max_examples=50)
def test_core::aggregationtype_instantiation(instance):
    assert isinstance(instance, core::AggregationType)

@given(instance=core::GeneralizedType_strategy)
@settings(max_examples=50)
def test_core::generalizedtype_instantiation(instance):
    assert isinstance(instance, core::GeneralizedType)

@given(instance=express::core::GeneralAggregationType_strategy)
@settings(max_examples=50)
def test_express::core::generalaggregationtype_instantiation(instance):
    assert isinstance(instance, express::core::GeneralAggregationType)

@given(instance=core::TypeElement_strategy)
@settings(max_examples=50)
def test_core::typeelement_instantiation(instance):
    assert isinstance(instance, core::TypeElement)

@given(instance=core::DomainConstraint_strategy)
@settings(max_examples=50)
def test_core::domainconstraint_instantiation(instance):
    assert isinstance(instance, core::DomainConstraint)

@given(instance=express::core::DomainRule_strategy)
@settings(max_examples=50)
def test_express::core::domainrule_instantiation(instance):
    assert isinstance(instance, express::core::DomainRule)

@given(instance=express::core::DomainRule_strategy)
def test_express::core::domainrule_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=express::core::DomainRule_strategy)
def test_express::core::domainrule_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=SingleEntityValue_strategy)
@settings(max_examples=50)
def test_singleentityvalue_instantiation(instance):
    assert isinstance(instance, SingleEntityValue)

@given(instance=express::instances::PartialEntityValue_strategy)
@settings(max_examples=50)
def test_express::instances::partialentityvalue_instantiation(instance):
    assert isinstance(instance, express::instances::PartialEntityValue)

@given(instance=express::instances::ConcreteValue_strategy)
@settings(max_examples=50)
def test_express::instances::concretevalue_instantiation(instance):
    assert isinstance(instance, express::instances::ConcreteValue)

@given(instance=instances::AggregateValue_strategy)
@settings(max_examples=50)
def test_instances::aggregatevalue_instantiation(instance):
    assert isinstance(instance, instances::AggregateValue)

@given(instance=core::Instance_strategy)
@settings(max_examples=50)
def test_core::instance_instantiation(instance):
    assert isinstance(instance, core::Instance)

@given(instance=express::instances::LISTValue_strategy)
@settings(max_examples=50)
def test_express::instances::listvalue_instantiation(instance):
    assert isinstance(instance, express::instances::LISTValue)

@given(instance=LogicalValue_strategy)
@settings(max_examples=50)
def test_logicalvalue_instantiation(instance):
    assert isinstance(instance, LogicalValue)

@given(instance=express::instances::BooleanValue_strategy)
@settings(max_examples=50)
def test_express::instances::booleanvalue_instantiation(instance):
    assert isinstance(instance, express::instances::BooleanValue)

@given(instance=NumberValue_strategy)
@settings(max_examples=50)
def test_numbervalue_instantiation(instance):
    assert isinstance(instance, NumberValue)

@given(instance=express::instances::RealValue_strategy)
@settings(max_examples=50)
def test_express::instances::realvalue_instantiation(instance):
    assert isinstance(instance, express::instances::RealValue)

@given(instance=express::instances::Population_strategy)
@settings(max_examples=50)
def test_express::instances::population_instantiation(instance):
    assert isinstance(instance, express::instances::Population)

@given(instance=express::instances::ArrayMember_strategy)
@settings(max_examples=50)
def test_express::instances::arraymember_instantiation(instance):
    assert isinstance(instance, express::instances::ArrayMember)

@given(instance=express::instances::ArrayMember_strategy)
def test_express::instances::arraymember_index_type(instance):
    assert isinstance(instance.index, str)


@given(instance=express::instances::ArrayMember_strategy)
def test_express::instances::arraymember_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=instances::ConcreteValue_strategy)
@settings(max_examples=50)
def test_instances::concretevalue_instantiation(instance):
    assert isinstance(instance, instances::ConcreteValue)

@given(instance=instances::TypedInstance_strategy)
@settings(max_examples=50)
def test_instances::typedinstance_instantiation(instance):
    assert isinstance(instance, instances::TypedInstance)

@given(instance=express::instances::EnumerationItem_strategy)
@settings(max_examples=50)
def test_express::instances::enumerationitem_instantiation(instance):
    assert isinstance(instance, express::instances::EnumerationItem)

@given(instance=express::instances::EnumerationItem_strategy)
def test_express::instances::enumerationitem_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=express::instances::EnumerationItem_strategy)
def test_express::instances::enumerationitem_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=BagMember_strategy)
@settings(max_examples=50)
def test_bagmember_instantiation(instance):
    assert isinstance(instance, BagMember)

@given(instance=LISTValue_strategy)
@settings(max_examples=50)
def test_listvalue_instantiation(instance):
    assert isinstance(instance, LISTValue)

@given(instance=express::instances::GenericAggregate_strategy)
@settings(max_examples=50)
def test_express::instances::genericaggregate_instantiation(instance):
    assert isinstance(instance, express::instances::GenericAggregate)

@given(instance=express::instances::Indeterminate_strategy)
@settings(max_examples=50)
def test_express::instances::indeterminate_instantiation(instance):
    assert isinstance(instance, express::instances::Indeterminate)

@given(instance=express::instances::SingleEntityValue_strategy)
@settings(max_examples=50)
def test_express::instances::singleentityvalue_instantiation(instance):
    assert isinstance(instance, express::instances::SingleEntityValue)

@given(instance=express::instances::BagMember_strategy)
@settings(max_examples=50)
def test_express::instances::bagmember_instantiation(instance):
    assert isinstance(instance, express::instances::BagMember)

@given(instance=express::instances::BagMember_strategy)
def test_express::instances::bagmember_count_type(instance):
    assert isinstance(instance.count, str)


@given(instance=express::instances::BagMember_strategy)
def test_express::instances::bagmember_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original

@given(instance=express::instances::ListMember_strategy)
@settings(max_examples=50)
def test_express::instances::listmember_instantiation(instance):
    assert isinstance(instance, express::instances::ListMember)

@given(instance=express::instances::ListMember_strategy)
def test_express::instances::listmember_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=express::instances::ListMember_strategy)
def test_express::instances::listmember_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=EntityValue_strategy)
@settings(max_examples=50)
def test_entityvalue_instantiation(instance):
    assert isinstance(instance, EntityValue)

@given(instance=TypedInstance_strategy)
@settings(max_examples=50)
def test_typedinstance_instantiation(instance):
    assert isinstance(instance, TypedInstance)

@given(instance=express::instances::SpecializedValue_strategy)
@settings(max_examples=50)
def test_express::instances::specializedvalue_instantiation(instance):
    assert isinstance(instance, express::instances::SpecializedValue)

@given(instance=express::instances::EntityInstance_strategy)
@settings(max_examples=50)
def test_express::instances::entityinstance_instantiation(instance):
    assert isinstance(instance, express::instances::EntityInstance)

@given(instance=express::instances::EntityInstance_strategy)
def test_express::instances::entityinstance_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=express::instances::EntityInstance_strategy)
def test_express::instances::entityinstance_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=StringValue_strategy)
@settings(max_examples=50)
def test_stringvalue_instantiation(instance):
    assert isinstance(instance, StringValue)

@given(instance=express::instances::TypeName_strategy)
@settings(max_examples=50)
def test_express::instances::typename_instantiation(instance):
    assert isinstance(instance, express::instances::TypeName)

@given(instance=express::instances::RoleName_strategy)
@settings(max_examples=50)
def test_express::instances::rolename_instantiation(instance):
    assert isinstance(instance, express::instances::RoleName)

@given(instance=ArrayMember_strategy)
@settings(max_examples=50)
def test_arraymember_instantiation(instance):
    assert isinstance(instance, ArrayMember)

@given(instance=AggregateValue_strategy)
@settings(max_examples=50)
def test_aggregatevalue_instantiation(instance):
    assert isinstance(instance, AggregateValue)

@given(instance=express::instances::BAGValue_strategy)
@settings(max_examples=50)
def test_express::instances::bagvalue_instantiation(instance):
    assert isinstance(instance, express::instances::BAGValue)

@given(instance=express::instances::SETValue_strategy)
@settings(max_examples=50)
def test_express::instances::setvalue_instantiation(instance):
    assert isinstance(instance, express::instances::SETValue)

@given(instance=express::instances::ARRAYValue_strategy)
@settings(max_examples=50)
def test_express::instances::arrayvalue_instantiation(instance):
    assert isinstance(instance, express::instances::ARRAYValue)

@given(instance=express::instances::AttributeValue_strategy)
@settings(max_examples=50)
def test_express::instances::attributevalue_instantiation(instance):
    assert isinstance(instance, express::instances::AttributeValue)

@given(instance=core::GenericType_strategy)
@settings(max_examples=50)
def test_core::generictype_instantiation(instance):
    assert isinstance(instance, core::GenericType)

@given(instance=algorithms::Parameter_strategy)
@settings(max_examples=50)
def test_algorithms::parameter_instantiation(instance):
    assert isinstance(instance, algorithms::Parameter)

@given(instance=express::instances::TypedInstance_strategy)
@settings(max_examples=50)
def test_express::instances::typedinstance_instantiation(instance):
    assert isinstance(instance, express::instances::TypedInstance)

@given(instance=ConcreteValue_strategy)
@settings(max_examples=50)
def test_concretevalue_instantiation(instance):
    assert isinstance(instance, ConcreteValue)

@given(instance=express::instances::SimpleValue_strategy)
@settings(max_examples=50)
def test_express::instances::simplevalue_instantiation(instance):
    assert isinstance(instance, express::instances::SimpleValue)

@given(instance=express::instances::SimpleValue_strategy)
def test_express::instances::simplevalue_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=express::instances::SimpleValue_strategy)
def test_express::instances::simplevalue_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=express::instances::AggregateValue_strategy)
@settings(max_examples=50)
def test_express::instances::aggregatevalue_instantiation(instance):
    assert isinstance(instance, express::instances::AggregateValue)

@given(instance=RealValue_strategy)
@settings(max_examples=50)
def test_realvalue_instantiation(instance):
    assert isinstance(instance, RealValue)

@given(instance=express::instances::IntegerValue_strategy)
@settings(max_examples=50)
def test_express::instances::integervalue_instantiation(instance):
    assert isinstance(instance, express::instances::IntegerValue)

@given(instance=AGGREGATEType_strategy)
@settings(max_examples=50)
def test_aggregatetype_instantiation(instance):
    assert isinstance(instance, AGGREGATEType)

@given(instance=express::algorithms::ActualStructureConstraint_strategy)
@settings(max_examples=50)
def test_express::algorithms::actualstructureconstraint_instantiation(instance):
    assert isinstance(instance, express::algorithms::ActualStructureConstraint)

@given(instance=express::algorithms::ActualStructureConstraint_strategy)
def test_express::algorithms::actualstructureconstraint_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=express::algorithms::ActualStructureConstraint_strategy)
def test_express::algorithms::actualstructureconstraint_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=ActualStructure_strategy)
@settings(max_examples=50)
def test_actualstructure_instantiation(instance):
    assert isinstance(instance, ActualStructure)

@given(instance=express::algorithms::VARVariable_strategy)
@settings(max_examples=50)
def test_express::algorithms::varvariable_instantiation(instance):
    assert isinstance(instance, express::algorithms::VARVariable)

@given(instance=core::ActualType_strategy)
@settings(max_examples=50)
def test_core::actualtype_instantiation(instance):
    assert isinstance(instance, core::ActualType)

@given(instance=express::algorithms::ActualAggregationType_strategy)
@settings(max_examples=50)
def test_express::algorithms::actualaggregationtype_instantiation(instance):
    assert isinstance(instance, express::algorithms::ActualAggregationType)

@given(instance=EscapeStatement_strategy)
@settings(max_examples=50)
def test_escapestatement_instantiation(instance):
    assert isinstance(instance, EscapeStatement)

@given(instance=SkipStatement_strategy)
@settings(max_examples=50)
def test_skipstatement_instantiation(instance):
    assert isinstance(instance, SkipStatement)

@given(instance=StatementBlock_strategy)
@settings(max_examples=50)
def test_statementblock_instantiation(instance):
    assert isinstance(instance, StatementBlock)

@given(instance=express::algorithms::Statement_strategy)
@settings(max_examples=50)
def test_express::algorithms::statement_instantiation(instance):
    assert isinstance(instance, express::algorithms::Statement)

@given(instance=express::algorithms::Statement_strategy)
def test_express::algorithms::statement_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=express::algorithms::Statement_strategy)
def test_express::algorithms::statement_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=ActualType_strategy)
@settings(max_examples=50)
def test_actualtype_instantiation(instance):
    assert isinstance(instance, ActualType)

@given(instance=express::algorithms::ActualAGGREGATEType_strategy)
@settings(max_examples=50)
def test_express::algorithms::actualaggregatetype_instantiation(instance):
    assert isinstance(instance, express::algorithms::ActualAGGREGATEType)

@given(instance=express::algorithms::ActualAGGREGATEType_strategy)
def test_express::algorithms::actualaggregatetype_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=express::algorithms::ActualAGGREGATEType_strategy)
def test_express::algorithms::actualaggregatetype_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=express::algorithms::ActualGenericType_strategy)
@settings(max_examples=50)
def test_express::algorithms::actualgenerictype_instantiation(instance):
    assert isinstance(instance, express::algorithms::ActualGenericType)

@given(instance=express::algorithms::ActualGenericType_strategy)
def test_express::algorithms::actualgenerictype_isEntity_type(instance):
    assert isinstance(instance.isEntity, str)


@given(instance=express::algorithms::ActualGenericType_strategy)
def test_express::algorithms::actualgenerictype_isEntity_setter(instance):
    original = instance.isEntity
    instance.isEntity = original
    assert instance.isEntity == original

@given(instance=express::algorithms::ActualGenericType_strategy)
def test_express::algorithms::actualgenerictype_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=express::algorithms::ActualGenericType_strategy)
def test_express::algorithms::actualgenerictype_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=core::AGGREGATEType_strategy)
@settings(max_examples=50)
def test_core::aggregatetype_instantiation(instance):
    assert isinstance(instance, core::AGGREGATEType)

@given(instance=algorithms::GenericElement_strategy)
@settings(max_examples=50)
def test_algorithms::genericelement_instantiation(instance):
    assert isinstance(instance, algorithms::GenericElement)

@given(instance=express::algorithms::ActualDataType_strategy)
@settings(max_examples=50)
def test_express::algorithms::actualdatatype_instantiation(instance):
    assert isinstance(instance, express::algorithms::ActualDataType)

@given(instance=express::algorithms::ActualStructure_strategy)
@settings(max_examples=50)
def test_express::algorithms::actualstructure_instantiation(instance):
    assert isinstance(instance, express::algorithms::ActualStructure)

@given(instance=InVariable_strategy)
@settings(max_examples=50)
def test_invariable_instantiation(instance):
    assert isinstance(instance, InVariable)

@given(instance=ActualDataType_strategy)
@settings(max_examples=50)
def test_actualdatatype_instantiation(instance):
    assert isinstance(instance, ActualDataType)

@given(instance=GenericType_strategy)
@settings(max_examples=50)
def test_generictype_instantiation(instance):
    assert isinstance(instance, GenericType)

@given(instance=ActualAggregationType_strategy)
@settings(max_examples=50)
def test_actualaggregationtype_instantiation(instance):
    assert isinstance(instance, ActualAggregationType)

@given(instance=express::algorithms::ActualBAGType_strategy)
@settings(max_examples=50)
def test_express::algorithms::actualbagtype_instantiation(instance):
    assert isinstance(instance, express::algorithms::ActualBAGType)

@given(instance=express::algorithms::ActualSETType_strategy)
@settings(max_examples=50)
def test_express::algorithms::actualsettype_instantiation(instance):
    assert isinstance(instance, express::algorithms::ActualSETType)

@given(instance=express::algorithms::ActualLISTType_strategy)
@settings(max_examples=50)
def test_express::algorithms::actuallisttype_instantiation(instance):
    assert isinstance(instance, express::algorithms::ActualLISTType)

@given(instance=express::algorithms::ActualARRAYType_strategy)
@settings(max_examples=50)
def test_express::algorithms::actualarraytype_instantiation(instance):
    assert isinstance(instance, express::algorithms::ActualARRAYType)

@given(instance=express::algorithms::ActualARRAYType_strategy)
def test_express::algorithms::actualarraytype_isOptional_type(instance):
    assert isinstance(instance.isOptional, str)


@given(instance=express::algorithms::ActualARRAYType_strategy)
def test_express::algorithms::actualarraytype_isOptional_setter(instance):
    original = instance.isOptional
    instance.isOptional = original
    assert instance.isOptional == original

@given(instance=InParameter_strategy)
@settings(max_examples=50)
def test_inparameter_instantiation(instance):
    assert isinstance(instance, InParameter)

@given(instance=RepeatStatement_strategy)
@settings(max_examples=50)
def test_repeatstatement_instantiation(instance):
    assert isinstance(instance, RepeatStatement)

@given(instance=core::AnonymousType_strategy)
@settings(max_examples=50)
def test_core::anonymoustype_instantiation(instance):
    assert isinstance(instance, core::AnonymousType)

@given(instance=express::core::ConcreteAggregationType_strategy)
@settings(max_examples=50)
def test_express::core::concreteaggregationtype_instantiation(instance):
    assert isinstance(instance, express::core::ConcreteAggregationType)

@given(instance=AlgorithmScope_strategy)
@settings(max_examples=50)
def test_algorithmscope_instantiation(instance):
    assert isinstance(instance, AlgorithmScope)

@given(instance=express::core::CommonElement_strategy)
@settings(max_examples=50)
def test_express::core::commonelement_instantiation(instance):
    assert isinstance(instance, express::core::CommonElement)

@given(instance=Algorithm_strategy)
@settings(max_examples=50)
def test_algorithm_instantiation(instance):
    assert isinstance(instance, Algorithm)

@given(instance=express::algorithms::Procedure_strategy)
@settings(max_examples=50)
def test_express::algorithms::procedure_instantiation(instance):
    assert isinstance(instance, express::algorithms::Procedure)

@given(instance=express::algorithms::Function_strategy)
@settings(max_examples=50)
def test_express::algorithms::function_instantiation(instance):
    assert isinstance(instance, express::algorithms::Function)

@given(instance=express::algorithms::ActualTypeConstraint_strategy)
@settings(max_examples=50)
def test_express::algorithms::actualtypeconstraint_instantiation(instance):
    assert isinstance(instance, express::algorithms::ActualTypeConstraint)

@given(instance=express::algorithms::ActualTypeConstraint_strategy)
def test_express::algorithms::actualtypeconstraint_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=express::algorithms::ActualTypeConstraint_strategy)
def test_express::algorithms::actualtypeconstraint_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=express::core::ARRAYType_strategy)
@settings(max_examples=50)
def test_express::core::arraytype_instantiation(instance):
    assert isinstance(instance, express::core::ARRAYType)

@given(instance=express::core::ARRAYType_strategy)
def test_express::core::arraytype_isOptional_type(instance):
    assert isinstance(instance.isOptional, str)


@given(instance=express::core::ARRAYType_strategy)
def test_express::core::arraytype_isOptional_setter(instance):
    original = instance.isOptional
    instance.isOptional = original
    assert instance.isOptional == original

@given(instance=express::core::AggregationType_strategy)
@settings(max_examples=50)
def test_express::core::aggregationtype_instantiation(instance):
    assert isinstance(instance, express::core::AggregationType)

@given(instance=express::core::AggregationType_strategy)
def test_express::core::aggregationtype_ordering_type(instance):
    assert isinstance(instance.ordering, str)


@given(instance=express::core::AggregationType_strategy)
def test_express::core::aggregationtype_ordering_setter(instance):
    original = instance.ordering
    instance.ordering = original
    assert instance.ordering == original

@given(instance=express::core::AggregationType_strategy)
def test_express::core::aggregationtype_isUnique_type(instance):
    assert isinstance(instance.isUnique, str)


@given(instance=express::core::AggregationType_strategy)
def test_express::core::aggregationtype_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=express::core::ScopedId_strategy)
@settings(max_examples=50)
def test_express::core::scopedid_instantiation(instance):
    assert isinstance(instance, express::core::ScopedId)

@given(instance=express::core::ScopedId_strategy)
def test_express::core::scopedid_localName_type(instance):
    assert isinstance(instance.localName, str)


@given(instance=express::core::ScopedId_strategy)
def test_express::core::scopedid_localName_setter(instance):
    original = instance.localName
    instance.localName = original
    assert instance.localName == original

@given(instance=express::core::BinaryType_strategy)
@settings(max_examples=50)
def test_express::core::binarytype_instantiation(instance):
    assert isinstance(instance, express::core::BinaryType)

@given(instance=DomainRule_strategy)
@settings(max_examples=50)
def test_domainrule_instantiation(instance):
    assert isinstance(instance, DomainRule)

@given(instance=SelectType_strategy)
@settings(max_examples=50)
def test_selecttype_instantiation(instance):
    assert isinstance(instance, SelectType)

@given(instance=core::CommonElement_strategy)
@settings(max_examples=50)
def test_core::commonelement_instantiation(instance):
    assert isinstance(instance, core::CommonElement)

@given(instance=core::Scope_strategy)
@settings(max_examples=50)
def test_core::scope_instantiation(instance):
    assert isinstance(instance, core::Scope)

@given(instance=express::core::LocalScope_strategy)
@settings(max_examples=50)
def test_express::core::localscope_instantiation(instance):
    assert isinstance(instance, express::core::LocalScope)

@given(instance=express::core::Relationship_strategy)
@settings(max_examples=50)
def test_express::core::relationship_instantiation(instance):
    assert isinstance(instance, express::core::Relationship)

@given(instance=express::core::SelectType_strategy)
@settings(max_examples=50)
def test_express::core::selecttype_instantiation(instance):
    assert isinstance(instance, express::core::SelectType)

@given(instance=express::core::SelectType_strategy)
def test_express::core::selecttype_isExtensible_type(instance):
    assert isinstance(instance.isExtensible, str)


@given(instance=express::core::SelectType_strategy)
def test_express::core::selecttype_isExtensible_setter(instance):
    original = instance.isExtensible
    instance.isExtensible = original
    assert instance.isExtensible == original

@given(instance=express::core::SelectType_strategy)
def test_express::core::selecttype_isEntity_type(instance):
    assert isinstance(instance.isEntity, str)


@given(instance=express::core::SelectType_strategy)
def test_express::core::selecttype_isEntity_setter(instance):
    original = instance.isEntity
    instance.isEntity = original
    assert instance.isEntity == original

@given(instance=express::core::ParameterType_strategy)
@settings(max_examples=50)
def test_express::core::parametertype_instantiation(instance):
    assert isinstance(instance, express::core::ParameterType)

@given(instance=express::core::Scope_strategy)
@settings(max_examples=50)
def test_express::core::scope_instantiation(instance):
    assert isinstance(instance, express::core::Scope)

@given(instance=express::core::Role_strategy)
@settings(max_examples=50)
def test_express::core::role_instantiation(instance):
    assert isinstance(instance, express::core::Role)

@given(instance=express::core::Remark_strategy)
@settings(max_examples=50)
def test_express::core::remark_instantiation(instance):
    assert isinstance(instance, express::core::Remark)

@given(instance=express::core::Remark_strategy)
def test_express::core::remark_isTagged_type(instance):
    assert isinstance(instance.isTagged, str)


@given(instance=express::core::Remark_strategy)
def test_express::core::remark_isTagged_setter(instance):
    original = instance.isTagged
    instance.isTagged = original
    assert instance.isTagged == original

@given(instance=express::core::Remark_strategy)
def test_express::core::remark_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=express::core::Remark_strategy)
def test_express::core::remark_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=express::core::Remark_strategy)
def test_express::core::remark_isTail_type(instance):
    assert isinstance(instance.isTail, str)


@given(instance=express::core::Remark_strategy)
def test_express::core::remark_isTail_setter(instance):
    original = instance.isTail
    instance.isTail = original
    assert instance.isTail == original

@given(instance=express::core::RangeRole_strategy)
@settings(max_examples=50)
def test_express::core::rangerole_instantiation(instance):
    assert isinstance(instance, express::core::RangeRole)

@given(instance=ArrayBound_strategy)
@settings(max_examples=50)
def test_arraybound_instantiation(instance):
    assert isinstance(instance, ArrayBound)

@given(instance=ConcreteType_strategy)
@settings(max_examples=50)
def test_concretetype_instantiation(instance):
    assert isinstance(instance, ConcreteType)

@given(instance=express::core::SpecializedType_strategy)
@settings(max_examples=50)
def test_express::core::specializedtype_instantiation(instance):
    assert isinstance(instance, express::core::SpecializedType)

@given(instance=express::core::SETType_strategy)
@settings(max_examples=50)
def test_express::core::settype_instantiation(instance):
    assert isinstance(instance, express::core::SETType)

@given(instance=LocalScope_strategy)
@settings(max_examples=50)
def test_localscope_instantiation(instance):
    assert isinstance(instance, LocalScope)

@given(instance=express::core::AlgorithmScope_strategy)
@settings(max_examples=50)
def test_express::core::algorithmscope_instantiation(instance):
    assert isinstance(instance, express::core::AlgorithmScope)

@given(instance=AnonymousType_strategy)
@settings(max_examples=50)
def test_anonymoustype_instantiation(instance):
    assert isinstance(instance, AnonymousType)

@given(instance=express::core::SimpleType_strategy)
@settings(max_examples=50)
def test_express::core::simpletype_instantiation(instance):
    assert isinstance(instance, express::core::SimpleType)

@given(instance=express::core::SimpleType_strategy)
def test_express::core::simpletype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=express::core::SimpleType_strategy)
def test_express::core::simpletype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=express::core::AnonymousType_strategy)
@settings(max_examples=50)
def test_express::core::anonymoustype_instantiation(instance):
    assert isinstance(instance, express::core::AnonymousType)

@given(instance=LengthConstraint_strategy)
@settings(max_examples=50)
def test_lengthconstraint_instantiation(instance):
    assert isinstance(instance, LengthConstraint)

@given(instance=express::core::StringType_strategy)
@settings(max_examples=50)
def test_express::core::stringtype_instantiation(instance):
    assert isinstance(instance, express::core::StringType)

@given(instance=ActualTypeConstraint_strategy)
@settings(max_examples=50)
def test_actualtypeconstraint_instantiation(instance):
    assert isinstance(instance, ActualTypeConstraint)

@given(instance=express::core::LogicType_strategy)
@settings(max_examples=50)
def test_express::core::logictype_instantiation(instance):
    assert isinstance(instance, express::core::LogicType)

@given(instance=NumericType_strategy)
@settings(max_examples=50)
def test_numerictype_instantiation(instance):
    assert isinstance(instance, NumericType)

@given(instance=express::core::RealType_strategy)
@settings(max_examples=50)
def test_express::core::realtype_instantiation(instance):
    assert isinstance(instance, express::core::RealType)

@given(instance=express::core::RealType_strategy)
def test_express::core::realtype_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=express::core::RealType_strategy)
def test_express::core::realtype_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=express::core::BAGType_strategy)
@settings(max_examples=50)
def test_express::core::bagtype_instantiation(instance):
    assert isinstance(instance, express::core::BAGType)

@given(instance=DomainConstraint_strategy)
@settings(max_examples=50)
def test_domainconstraint_instantiation(instance):
    assert isinstance(instance, DomainConstraint)

@given(instance=express::core::LengthConstraint_strategy)
@settings(max_examples=50)
def test_express::core::lengthconstraint_instantiation(instance):
    assert isinstance(instance, express::core::LengthConstraint)

@given(instance=express::core::LengthConstraint_strategy)
def test_express::core::lengthconstraint_maxLength_type(instance):
    assert isinstance(instance.maxLength, str)


@given(instance=express::core::LengthConstraint_strategy)
def test_express::core::lengthconstraint_maxLength_setter(instance):
    original = instance.maxLength
    instance.maxLength = original
    assert instance.maxLength == original

@given(instance=express::core::LengthConstraint_strategy)
def test_express::core::lengthconstraint_isFixed_type(instance):
    assert isinstance(instance.isFixed, str)


@given(instance=express::core::LengthConstraint_strategy)
def test_express::core::lengthconstraint_isFixed_setter(instance):
    original = instance.isFixed
    instance.isFixed = original
    assert instance.isFixed == original

@given(instance=express::core::SizeConstraint_strategy)
@settings(max_examples=50)
def test_express::core::sizeconstraint_instantiation(instance):
    assert isinstance(instance, express::core::SizeConstraint)

@given(instance=express::core::SizeConstraint_strategy)
def test_express::core::sizeconstraint_bound_type(instance):
    assert isinstance(instance.bound, str)


@given(instance=express::core::SizeConstraint_strategy)
def test_express::core::sizeconstraint_bound_setter(instance):
    original = instance.bound
    instance.bound = original
    assert instance.bound == original

@given(instance=express::core::AttributeType_strategy)
@settings(max_examples=50)
def test_express::core::attributetype_instantiation(instance):
    assert isinstance(instance, express::core::AttributeType)

@given(instance=express::core::Instance_strategy)
@settings(max_examples=50)
def test_express::core::instance_instantiation(instance):
    assert isinstance(instance, express::core::Instance)

@given(instance=express::core::NamedElement_strategy)
@settings(max_examples=50)
def test_express::core::namedelement_instantiation(instance):
    assert isinstance(instance, express::core::NamedElement)

@given(instance=core::VariableType_strategy)
@settings(max_examples=50)
def test_core::variabletype_instantiation(instance):
    assert isinstance(instance, core::VariableType)

@given(instance=express::core::InstantiableType_strategy)
@settings(max_examples=50)
def test_express::core::instantiabletype_instantiation(instance):
    assert isinstance(instance, express::core::InstantiableType)

@given(instance=GeneralAggregationType_strategy)
@settings(max_examples=50)
def test_generalaggregationtype_instantiation(instance):
    assert isinstance(instance, GeneralAggregationType)

@given(instance=express::core::GeneralLISTType_strategy)
@settings(max_examples=50)
def test_express::core::generallisttype_instantiation(instance):
    assert isinstance(instance, express::core::GeneralLISTType)

@given(instance=express::core::GeneralSETType_strategy)
@settings(max_examples=50)
def test_express::core::generalsettype_instantiation(instance):
    assert isinstance(instance, express::core::GeneralSETType)

@given(instance=express::core::GeneralARRAYType_strategy)
@settings(max_examples=50)
def test_express::core::generalarraytype_instantiation(instance):
    assert isinstance(instance, express::core::GeneralARRAYType)

@given(instance=express::core::GeneralARRAYType_strategy)
def test_express::core::generalarraytype_isOptional_type(instance):
    assert isinstance(instance.isOptional, str)


@given(instance=express::core::GeneralARRAYType_strategy)
def test_express::core::generalarraytype_isOptional_setter(instance):
    original = instance.isOptional
    instance.isOptional = original
    assert instance.isOptional == original

@given(instance=express::core::GeneralBAGType_strategy)
@settings(max_examples=50)
def test_express::core::generalbagtype_instantiation(instance):
    assert isinstance(instance, express::core::GeneralBAGType)

@given(instance=ActualStructureConstraint_strategy)
@settings(max_examples=50)
def test_actualstructureconstraint_instantiation(instance):
    assert isinstance(instance, ActualStructureConstraint)

@given(instance=ParameterType_strategy)
@settings(max_examples=50)
def test_parametertype_instantiation(instance):
    assert isinstance(instance, ParameterType)

@given(instance=express::core::ArrayBound_strategy)
@settings(max_examples=50)
def test_express::core::arraybound_instantiation(instance):
    assert isinstance(instance, express::core::ArrayBound)

@given(instance=express::core::ArrayBound_strategy)
def test_express::core::arraybound_bound_type(instance):
    assert isinstance(instance.bound, str)


@given(instance=express::core::ArrayBound_strategy)
def test_express::core::arraybound_bound_setter(instance):
    original = instance.bound
    instance.bound = original
    assert instance.bound == original

@given(instance=core::AttributeType_strategy)
@settings(max_examples=50)
def test_core::attributetype_instantiation(instance):
    assert isinstance(instance, core::AttributeType)

@given(instance=express::core::NamedType_strategy)
@settings(max_examples=50)
def test_express::core::namedtype_instantiation(instance):
    assert isinstance(instance, express::core::NamedType)

@given(instance=express::core::GeneralizedType_strategy)
@settings(max_examples=50)
def test_express::core::generalizedtype_instantiation(instance):
    assert isinstance(instance, express::core::GeneralizedType)

@given(instance=core::DataType_strategy)
@settings(max_examples=50)
def test_core::datatype_instantiation(instance):
    assert isinstance(instance, core::DataType)

@given(instance=express::core::VariableType_strategy)
@settings(max_examples=50)
def test_express::core::variabletype_instantiation(instance):
    assert isinstance(instance, express::core::VariableType)

@given(instance=EnumerationType_strategy)
@settings(max_examples=50)
def test_enumerationtype_instantiation(instance):
    assert isinstance(instance, EnumerationType)

@given(instance=NamedType_strategy)
@settings(max_examples=50)
def test_namedtype_instantiation(instance):
    assert isinstance(instance, NamedType)

@given(instance=ListMember_strategy)
@settings(max_examples=50)
def test_listmember_instantiation(instance):
    assert isinstance(instance, ListMember)

@given(instance=RepeatCount_strategy)
@settings(max_examples=50)
def test_repeatcount_instantiation(instance):
    assert isinstance(instance, RepeatCount)

@given(instance=express::expressions::MemberBinding_strategy)
@settings(max_examples=50)
def test_express::expressions::memberbinding_instantiation(instance):
    assert isinstance(instance, express::expressions::MemberBinding)

@given(instance=express::expressions::MemberBinding_strategy)
def test_express::expressions::memberbinding_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=express::expressions::MemberBinding_strategy)
def test_express::expressions::memberbinding_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=FunctionResult_strategy)
@settings(max_examples=50)
def test_functionresult_instantiation(instance):
    assert isinstance(instance, FunctionResult)

@given(instance=Function_strategy)
@settings(max_examples=50)
def test_function_instantiation(instance):
    assert isinstance(instance, Function)

@given(instance=SizeConstraint_strategy)
@settings(max_examples=50)
def test_sizeconstraint_instantiation(instance):
    assert isinstance(instance, SizeConstraint)

@given(instance=GeneralizedType_strategy)
@settings(max_examples=50)
def test_generalizedtype_instantiation(instance):
    assert isinstance(instance, GeneralizedType)

@given(instance=express::core::GenericType_strategy)
@settings(max_examples=50)
def test_express::core::generictype_instantiation(instance):
    assert isinstance(instance, express::core::GenericType)

@given(instance=express::core::GenericType_strategy)
def test_express::core::generictype_isEntity_type(instance):
    assert isinstance(instance.isEntity, str)


@given(instance=express::core::GenericType_strategy)
def test_express::core::generictype_isEntity_setter(instance):
    original = instance.isEntity
    instance.isEntity = original
    assert instance.isEntity == original

@given(instance=express::core::AGGREGATEType_strategy)
@settings(max_examples=50)
def test_express::core::aggregatetype_instantiation(instance):
    assert isinstance(instance, express::core::AGGREGATEType)

@given(instance=PartialEntityType_strategy)
@settings(max_examples=50)
def test_partialentitytype_instantiation(instance):
    assert isinstance(instance, PartialEntityType)

@given(instance=express::core::SingleEntityType_strategy)
@settings(max_examples=50)
def test_express::core::singleentitytype_instantiation(instance):
    assert isinstance(instance, express::core::SingleEntityType)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=express::core::LocalElement_strategy)
@settings(max_examples=50)
def test_express::core::localelement_instantiation(instance):
    assert isinstance(instance, express::core::LocalElement)

@given(instance=express::core::SchemaElement_strategy)
@settings(max_examples=50)
def test_express::core::schemaelement_instantiation(instance):
    assert isinstance(instance, express::core::SchemaElement)

@given(instance=express::core::TypeElement_strategy)
@settings(max_examples=50)
def test_express::core::typeelement_instantiation(instance):
    assert isinstance(instance, express::core::TypeElement)

@given(instance=core::Expression_strategy)
@settings(max_examples=50)
def test_core::expression_instantiation(instance):
    assert isinstance(instance, core::Expression)

@given(instance=Constant_strategy)
@settings(max_examples=50)
def test_constant_instantiation(instance):
    assert isinstance(instance, Constant)

@given(instance=Attribute_strategy)
@settings(max_examples=50)
def test_attribute_instantiation(instance):
    assert isinstance(instance, Attribute)

@given(instance=express::core::DerivedAttribute_strategy)
@settings(max_examples=50)
def test_express::core::derivedattribute_instantiation(instance):
    assert isinstance(instance, express::core::DerivedAttribute)

@given(instance=express::core::InverseAttribute_strategy)
@settings(max_examples=50)
def test_express::core::inverseattribute_instantiation(instance):
    assert isinstance(instance, express::core::InverseAttribute)

@given(instance=express::core::InverseAttribute_strategy)
def test_express::core::inverseattribute_isUnique_type(instance):
    assert isinstance(instance.isUnique, str)


@given(instance=express::core::InverseAttribute_strategy)
def test_express::core::inverseattribute_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=express::core::ExplicitAttribute_strategy)
@settings(max_examples=50)
def test_express::core::explicitattribute_instantiation(instance):
    assert isinstance(instance, express::core::ExplicitAttribute)

@given(instance=express::core::ExplicitAttribute_strategy)
def test_express::core::explicitattribute_isOptional_type(instance):
    assert isinstance(instance.isOptional, str)


@given(instance=express::core::ExplicitAttribute_strategy)
def test_express::core::explicitattribute_isOptional_setter(instance):
    original = instance.isOptional
    instance.isOptional = original
    assert instance.isOptional == original

@given(instance=Selector_strategy)
@settings(max_examples=50)
def test_selector_instantiation(instance):
    assert isinstance(instance, Selector)

@given(instance=express::expressions::UsedInRef_strategy)
@settings(max_examples=50)
def test_express::expressions::usedinref_instantiation(instance):
    assert isinstance(instance, express::expressions::UsedInRef)

@given(instance=express::expressions::GroupRef_strategy)
@settings(max_examples=50)
def test_express::expressions::groupref_instantiation(instance):
    assert isinstance(instance, express::expressions::GroupRef)

@given(instance=express::expressions::GroupRef_strategy)
def test_express::expressions::groupref_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=express::expressions::GroupRef_strategy)
def test_express::expressions::groupref_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=express::expressions::AttributeRef_strategy)
@settings(max_examples=50)
def test_express::expressions::attributeref_instantiation(instance):
    assert isinstance(instance, express::expressions::AttributeRef)

@given(instance=express::expressions::AttributeRef_strategy)
def test_express::expressions::attributeref_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=express::expressions::AttributeRef_strategy)
def test_express::expressions::attributeref_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=AttributeValue_strategy)
@settings(max_examples=50)
def test_attributevalue_instantiation(instance):
    assert isinstance(instance, AttributeValue)

@given(instance=express::expressions::AttributeBinding_strategy)
@settings(max_examples=50)
def test_express::expressions::attributebinding_instantiation(instance):
    assert isinstance(instance, express::expressions::AttributeBinding)

@given(instance=express::expressions::AttributeBinding_strategy)
def test_express::expressions::attributebinding_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=express::expressions::AttributeBinding_strategy)
def test_express::expressions::attributebinding_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=QueryVariable_strategy)
@settings(max_examples=50)
def test_queryvariable_instantiation(instance):
    assert isinstance(instance, QueryVariable)

@given(instance=VariableType_strategy)
@settings(max_examples=50)
def test_variabletype_instantiation(instance):
    assert isinstance(instance, VariableType)

@given(instance=express::core::ActualType_strategy)
@settings(max_examples=50)
def test_express::core::actualtype_instantiation(instance):
    assert isinstance(instance, express::core::ActualType)

@given(instance=AttributeBinding_strategy)
@settings(max_examples=50)
def test_attributebinding_instantiation(instance):
    assert isinstance(instance, AttributeBinding)

@given(instance=PartialEntityValue_strategy)
@settings(max_examples=50)
def test_partialentityvalue_instantiation(instance):
    assert isinstance(instance, PartialEntityValue)

@given(instance=express::instances::EntityValue_strategy)
@settings(max_examples=50)
def test_express::instances::entityvalue_instantiation(instance):
    assert isinstance(instance, express::instances::EntityValue)

@given(instance=MemberBinding_strategy)
@settings(max_examples=50)
def test_memberbinding_instantiation(instance):
    assert isinstance(instance, MemberBinding)

@given(instance=GenericAggregate_strategy)
@settings(max_examples=50)
def test_genericaggregate_instantiation(instance):
    assert isinstance(instance, GenericAggregate)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=express::expressions::UnaryOperation_strategy)
@settings(max_examples=50)
def test_express::expressions::unaryoperation_instantiation(instance):
    assert isinstance(instance, express::expressions::UnaryOperation)

@given(instance=express::expressions::UnaryOperation_strategy)
def test_express::expressions::unaryoperation_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=express::expressions::UnaryOperation_strategy)
def test_express::expressions::unaryoperation_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=express::expressions::Coercion_strategy)
@settings(max_examples=50)
def test_express::expressions::coercion_instantiation(instance):
    assert isinstance(instance, express::expressions::Coercion)

@given(instance=express::expressions::BinaryOperation_strategy)
@settings(max_examples=50)
def test_express::expressions::binaryoperation_instantiation(instance):
    assert isinstance(instance, express::expressions::BinaryOperation)

@given(instance=express::expressions::BinaryOperation_strategy)
def test_express::expressions::binaryoperation_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=express::expressions::BinaryOperation_strategy)
def test_express::expressions::binaryoperation_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=express::algorithms::InParameter_strategy)
@settings(max_examples=50)
def test_express::algorithms::inparameter_instantiation(instance):
    assert isinstance(instance, express::algorithms::InParameter)

@given(instance=FunctionCall_strategy)
@settings(max_examples=50)
def test_functioncall_instantiation(instance):
    assert isinstance(instance, FunctionCall)

@given(instance=ProcedureCall_strategy)
@settings(max_examples=50)
def test_procedurecall_instantiation(instance):
    assert isinstance(instance, ProcedureCall)

@given(instance=express::expressions::ActualParameter_strategy)
@settings(max_examples=50)
def test_express::expressions::actualparameter_instantiation(instance):
    assert isinstance(instance, express::expressions::ActualParameter)

@given(instance=express::expressions::ActualParameter_strategy)
def test_express::expressions::actualparameter_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=express::expressions::ActualParameter_strategy)
def test_express::expressions::actualparameter_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=IndexOperation_strategy)
@settings(max_examples=50)
def test_indexoperation_instantiation(instance):
    assert isinstance(instance, IndexOperation)

@given(instance=express::expressions::StringIndex_strategy)
@settings(max_examples=50)
def test_express::expressions::stringindex_instantiation(instance):
    assert isinstance(instance, express::expressions::StringIndex)

@given(instance=express::expressions::AggregateIndex_strategy)
@settings(max_examples=50)
def test_express::expressions::aggregateindex_instantiation(instance):
    assert isinstance(instance, express::expressions::AggregateIndex)

@given(instance=express::expressions::BinaryIndex_strategy)
@settings(max_examples=50)
def test_express::expressions::binaryindex_instantiation(instance):
    assert isinstance(instance, express::expressions::BinaryIndex)

@given(instance=SimpleValue_strategy)
@settings(max_examples=50)
def test_simplevalue_instantiation(instance):
    assert isinstance(instance, SimpleValue)

@given(instance=express::instances::BinaryValue_strategy)
@settings(max_examples=50)
def test_express::instances::binaryvalue_instantiation(instance):
    assert isinstance(instance, express::instances::BinaryValue)

@given(instance=express::instances::NumberValue_strategy)
@settings(max_examples=50)
def test_express::instances::numbervalue_instantiation(instance):
    assert isinstance(instance, express::instances::NumberValue)

@given(instance=express::instances::LogicalValue_strategy)
@settings(max_examples=50)
def test_express::instances::logicalvalue_instantiation(instance):
    assert isinstance(instance, express::instances::LogicalValue)

@given(instance=express::instances::StringValue_strategy)
@settings(max_examples=50)
def test_express::instances::stringvalue_instantiation(instance):
    assert isinstance(instance, express::instances::StringValue)

@given(instance=EnumerationItem_strategy)
@settings(max_examples=50)
def test_enumerationitem_instantiation(instance):
    assert isinstance(instance, EnumerationItem)

@given(instance=Primary_strategy)
@settings(max_examples=50)
def test_primary_instantiation(instance):
    assert isinstance(instance, Primary)

@given(instance=express::expressions::ExtentRef_strategy)
@settings(max_examples=50)
def test_express::expressions::extentref_instantiation(instance):
    assert isinstance(instance, express::expressions::ExtentRef)

@given(instance=express::expressions::ExtentRef_strategy)
def test_express::expressions::extentref_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=express::expressions::ExtentRef_strategy)
def test_express::expressions::extentref_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=express::expressions::Literal_strategy)
@settings(max_examples=50)
def test_express::expressions::literal_instantiation(instance):
    assert isinstance(instance, express::expressions::Literal)

@given(instance=express::expressions::VariableRef_strategy)
@settings(max_examples=50)
def test_express::expressions::variableref_instantiation(instance):
    assert isinstance(instance, express::expressions::VariableRef)

@given(instance=express::expressions::VariableRef_strategy)
def test_express::expressions::variableref_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=express::expressions::VariableRef_strategy)
def test_express::expressions::variableref_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=express::expressions::ConstantRef_strategy)
@settings(max_examples=50)
def test_express::expressions::constantref_instantiation(instance):
    assert isinstance(instance, express::expressions::ConstantRef)

@given(instance=express::expressions::ConstantRef_strategy)
def test_express::expressions::constantref_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=express::expressions::ConstantRef_strategy)
def test_express::expressions::constantref_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=express::expressions::IndeterminateRef_strategy)
@settings(max_examples=50)
def test_express::expressions::indeterminateref_instantiation(instance):
    assert isinstance(instance, express::expressions::IndeterminateRef)

@given(instance=express::expressions::ParameterRef_strategy)
@settings(max_examples=50)
def test_express::expressions::parameterref_instantiation(instance):
    assert isinstance(instance, express::expressions::ParameterRef)

@given(instance=express::expressions::ParameterRef_strategy)
def test_express::expressions::parameterref_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=express::expressions::ParameterRef_strategy)
def test_express::expressions::parameterref_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=express::expressions::EnumItemRef_strategy)
@settings(max_examples=50)
def test_express::expressions::enumitemref_instantiation(instance):
    assert isinstance(instance, express::expressions::EnumItemRef)

@given(instance=express::expressions::EnumItemRef_strategy)
def test_express::expressions::enumitemref_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=express::expressions::EnumItemRef_strategy)
def test_express::expressions::enumitemref_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=express::expressions::RepeatCount_strategy)
@settings(max_examples=50)
def test_express::expressions::repeatcount_instantiation(instance):
    assert isinstance(instance, express::expressions::RepeatCount)

@given(instance=express::expressions::SELFRef_strategy)
@settings(max_examples=50)
def test_express::expressions::selfref_instantiation(instance):
    assert isinstance(instance, express::expressions::SELFRef)

@given(instance=Indeterminate_strategy)
@settings(max_examples=50)
def test_indeterminate_instantiation(instance):
    assert isinstance(instance, Indeterminate)

@given(instance=CaseAction_strategy)
@settings(max_examples=50)
def test_caseaction_instantiation(instance):
    assert isinstance(instance, CaseAction)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=express::algorithms::InVariable_strategy)
@settings(max_examples=50)
def test_express::algorithms::invariable_instantiation(instance):
    assert isinstance(instance, express::algorithms::InVariable)

@given(instance=express::algorithms::FunctionResult_strategy)
@settings(max_examples=50)
def test_express::algorithms::functionresult_instantiation(instance):
    assert isinstance(instance, express::algorithms::FunctionResult)

@given(instance=express::algorithms::LocalVariable_strategy)
@settings(max_examples=50)
def test_express::algorithms::localvariable_instantiation(instance):
    assert isinstance(instance, express::algorithms::LocalVariable)

@given(instance=SingleEntityType_strategy)
@settings(max_examples=50)
def test_singleentitytype_instantiation(instance):
    assert isinstance(instance, SingleEntityType)

@given(instance=ControlVariable_strategy)
@settings(max_examples=50)
def test_controlvariable_instantiation(instance):
    assert isinstance(instance, ControlVariable)

@given(instance=ExplicitAttribute_strategy)
@settings(max_examples=50)
def test_explicitattribute_instantiation(instance):
    assert isinstance(instance, ExplicitAttribute)

@given(instance=express::core::InvertibleAttribute_strategy)
@settings(max_examples=50)
def test_express::core::invertibleattribute_instantiation(instance):
    assert isinstance(instance, express::core::InvertibleAttribute)

@given(instance=express::statements::VARExpression_strategy)
@settings(max_examples=50)
def test_express::statements::varexpression_instantiation(instance):
    assert isinstance(instance, express::statements::VARExpression)

@given(instance=express::statements::VARExpression_strategy)
def test_express::statements::varexpression_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=express::statements::VARExpression_strategy)
def test_express::statements::varexpression_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=VARVariable_strategy)
@settings(max_examples=50)
def test_varvariable_instantiation(instance):
    assert isinstance(instance, VARVariable)

@given(instance=algorithms::VARVariable_strategy)
@settings(max_examples=50)
def test_algorithms::varvariable_instantiation(instance):
    assert isinstance(instance, algorithms::VARVariable)

@given(instance=express::algorithms::VARParameter_strategy)
@settings(max_examples=50)
def test_express::algorithms::varparameter_instantiation(instance):
    assert isinstance(instance, express::algorithms::VARParameter)

@given(instance=algorithms::NamedVariable_strategy)
@settings(max_examples=50)
def test_algorithms::namedvariable_instantiation(instance):
    assert isinstance(instance, algorithms::NamedVariable)

@given(instance=express::statements::AliasVariable_strategy)
@settings(max_examples=50)
def test_express::statements::aliasvariable_instantiation(instance):
    assert isinstance(instance, express::statements::AliasVariable)

@given(instance=NamedVariable_strategy)
@settings(max_examples=50)
def test_namedvariable_instantiation(instance):
    assert isinstance(instance, NamedVariable)

@given(instance=express::algorithms::Variable_strategy)
@settings(max_examples=50)
def test_express::algorithms::variable_instantiation(instance):
    assert isinstance(instance, express::algorithms::Variable)

@given(instance=express::expressions::QueryVariable_strategy)
@settings(max_examples=50)
def test_express::expressions::queryvariable_instantiation(instance):
    assert isinstance(instance, express::expressions::QueryVariable)

@given(instance=express::statements::ControlVariable_strategy)
@settings(max_examples=50)
def test_express::statements::controlvariable_instantiation(instance):
    assert isinstance(instance, express::statements::ControlVariable)

@given(instance=AliasVariable_strategy)
@settings(max_examples=50)
def test_aliasvariable_instantiation(instance):
    assert isinstance(instance, AliasVariable)

@given(instance=VARExpression_strategy)
@settings(max_examples=50)
def test_varexpression_instantiation(instance):
    assert isinstance(instance, VARExpression)

@given(instance=express::statements::VariableCell_strategy)
@settings(max_examples=50)
def test_express::statements::variablecell_instantiation(instance):
    assert isinstance(instance, express::statements::VariableCell)

@given(instance=express::statements::VariableCell_strategy)
def test_express::statements::variablecell_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=express::statements::VariableCell_strategy)
def test_express::statements::variablecell_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=express::statements::GroupCell_strategy)
@settings(max_examples=50)
def test_express::statements::groupcell_instantiation(instance):
    assert isinstance(instance, express::statements::GroupCell)

@given(instance=express::statements::GroupCell_strategy)
def test_express::statements::groupcell_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=express::statements::GroupCell_strategy)
def test_express::statements::groupcell_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=express::statements::AttributeCell_strategy)
@settings(max_examples=50)
def test_express::statements::attributecell_instantiation(instance):
    assert isinstance(instance, express::statements::AttributeCell)

@given(instance=express::statements::AttributeCell_strategy)
def test_express::statements::attributecell_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=express::statements::AttributeCell_strategy)
def test_express::statements::attributecell_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=express::statements::VARCell_strategy)
@settings(max_examples=50)
def test_express::statements::varcell_instantiation(instance):
    assert isinstance(instance, express::statements::VARCell)

@given(instance=express::statements::VARCell_strategy)
def test_express::statements::varcell_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=express::statements::VARCell_strategy)
def test_express::statements::varcell_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=express::statements::MemberCell_strategy)
@settings(max_examples=50)
def test_express::statements::membercell_instantiation(instance):
    assert isinstance(instance, express::statements::MemberCell)

@given(instance=core::LocalScope_strategy)
@settings(max_examples=50)
def test_core::localscope_instantiation(instance):
    assert isinstance(instance, core::LocalScope)

@given(instance=express::expressions::QueryExpression_strategy)
@settings(max_examples=50)
def test_express::expressions::queryexpression_instantiation(instance):
    assert isinstance(instance, express::expressions::QueryExpression)

@given(instance=algorithms::Statement_strategy)
@settings(max_examples=50)
def test_algorithms::statement_instantiation(instance):
    assert isinstance(instance, algorithms::Statement)

@given(instance=express::statements::RepeatStatement_strategy)
@settings(max_examples=50)
def test_express::statements::repeatstatement_instantiation(instance):
    assert isinstance(instance, express::statements::RepeatStatement)

@given(instance=express::statements::AliasStatement_strategy)
@settings(max_examples=50)
def test_express::statements::aliasstatement_instantiation(instance):
    assert isinstance(instance, express::statements::AliasStatement)

@given(instance=ControlStatement_strategy)
@settings(max_examples=50)
def test_controlstatement_instantiation(instance):
    assert isinstance(instance, ControlStatement)

@given(instance=express::statements::NullStatement_strategy)
@settings(max_examples=50)
def test_express::statements::nullstatement_instantiation(instance):
    assert isinstance(instance, express::statements::NullStatement)

@given(instance=express::statements::EscapeStatement_strategy)
@settings(max_examples=50)
def test_express::statements::escapestatement_instantiation(instance):
    assert isinstance(instance, express::statements::EscapeStatement)

@given(instance=express::statements::ReturnStatement_strategy)
@settings(max_examples=50)
def test_express::statements::returnstatement_instantiation(instance):
    assert isinstance(instance, express::statements::ReturnStatement)

@given(instance=express::statements::SkipStatement_strategy)
@settings(max_examples=50)
def test_express::statements::skipstatement_instantiation(instance):
    assert isinstance(instance, express::statements::SkipStatement)

@given(instance=express::statements::CaseAction_strategy)
@settings(max_examples=50)
def test_express::statements::caseaction_instantiation(instance):
    assert isinstance(instance, express::statements::CaseAction)

@given(instance=express::statements::CaseAction_strategy)
def test_express::statements::caseaction_isDefault_type(instance):
    assert isinstance(instance.isDefault, str)


@given(instance=express::statements::CaseAction_strategy)
def test_express::statements::caseaction_isDefault_setter(instance):
    original = instance.isDefault
    instance.isDefault = original
    assert instance.isDefault == original

@given(instance=LocalElement_strategy)
@settings(max_examples=50)
def test_localelement_instantiation(instance):
    assert isinstance(instance, LocalElement)

@given(instance=express::algorithms::NamedVariable_strategy)
@settings(max_examples=50)
def test_express::algorithms::namedvariable_instantiation(instance):
    assert isinstance(instance, express::algorithms::NamedVariable)

@given(instance=express::algorithms::GenericElement_strategy)
@settings(max_examples=50)
def test_express::algorithms::genericelement_instantiation(instance):
    assert isinstance(instance, express::algorithms::GenericElement)

@given(instance=express::algorithms::Parameter_strategy)
@settings(max_examples=50)
def test_express::algorithms::parameter_instantiation(instance):
    assert isinstance(instance, express::algorithms::Parameter)

@given(instance=express::algorithms::Parameter_strategy)
def test_express::algorithms::parameter_inout_type(instance):
    assert isinstance(instance.inout, str)


@given(instance=express::algorithms::Parameter_strategy)
def test_express::algorithms::parameter_inout_setter(instance):
    original = instance.inout
    instance.inout = original
    assert instance.inout == original

@given(instance=express::algorithms::Parameter_strategy)
def test_express::algorithms::parameter_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=express::algorithms::Parameter_strategy)
def test_express::algorithms::parameter_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=express::rules::NamedRule_strategy)
@settings(max_examples=50)
def test_express::rules::namedrule_instantiation(instance):
    assert isinstance(instance, express::rules::NamedRule)

@given(instance=express::rules::NamedRule_strategy)
def test_express::rules::namedrule_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=express::rules::NamedRule_strategy)
def test_express::rules::namedrule_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=NamedRule_strategy)
@settings(max_examples=50)
def test_namedrule_instantiation(instance):
    assert isinstance(instance, NamedRule)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=express::statements::CaseStatement_strategy)
@settings(max_examples=50)
def test_express::statements::casestatement_instantiation(instance):
    assert isinstance(instance, express::statements::CaseStatement)

@given(instance=express::statements::Assignment_strategy)
@settings(max_examples=50)
def test_express::statements::assignment_instantiation(instance):
    assert isinstance(instance, express::statements::Assignment)

@given(instance=express::statements::StatementBlock_strategy)
@settings(max_examples=50)
def test_express::statements::statementblock_instantiation(instance):
    assert isinstance(instance, express::statements::StatementBlock)

@given(instance=express::statements::StatementBlock_strategy)
def test_express::statements::statementblock_delimited_type(instance):
    assert isinstance(instance.delimited, str)


@given(instance=express::statements::StatementBlock_strategy)
def test_express::statements::statementblock_delimited_setter(instance):
    original = instance.delimited
    instance.delimited = original
    assert instance.delimited == original

@given(instance=express::statements::ControlStatement_strategy)
@settings(max_examples=50)
def test_express::statements::controlstatement_instantiation(instance):
    assert isinstance(instance, express::statements::ControlStatement)

@given(instance=express::statements::IfStatement_strategy)
@settings(max_examples=50)
def test_express::statements::ifstatement_instantiation(instance):
    assert isinstance(instance, express::statements::IfStatement)

@given(instance=core::AlgorithmScope_strategy)
@settings(max_examples=50)
def test_core::algorithmscope_instantiation(instance):
    assert isinstance(instance, core::AlgorithmScope)

@given(instance=express::algorithms::Algorithm_strategy)
@settings(max_examples=50)
def test_express::algorithms::algorithm_instantiation(instance):
    assert isinstance(instance, express::algorithms::Algorithm)

@given(instance=core::SchemaElement_strategy)
@settings(max_examples=50)
def test_core::schemaelement_instantiation(instance):
    assert isinstance(instance, core::SchemaElement)

@given(instance=express::rules::GlobalRule_strategy)
@settings(max_examples=50)
def test_express::rules::globalrule_instantiation(instance):
    assert isinstance(instance, express::rules::GlobalRule)

@given(instance=ScopedId_strategy)
@settings(max_examples=50)
def test_scopedid_instantiation(instance):
    assert isinstance(instance, ScopedId)

@given(instance=GlobalRule_strategy)
@settings(max_examples=50)
def test_globalrule_instantiation(instance):
    assert isinstance(instance, GlobalRule)

@given(instance=Population_strategy)
@settings(max_examples=50)
def test_population_instantiation(instance):
    assert isinstance(instance, Population)

@given(instance=EntityInstance_strategy)
@settings(max_examples=50)
def test_entityinstance_instantiation(instance):
    assert isinstance(instance, EntityInstance)

@given(instance=express::instances::SingleLeafInstance_strategy)
@settings(max_examples=50)
def test_express::instances::singleleafinstance_instantiation(instance):
    assert isinstance(instance, express::instances::SingleLeafInstance)

@given(instance=express::instances::MultiLeafInstance_strategy)
@settings(max_examples=50)
def test_express::instances::multileafinstance_instantiation(instance):
    assert isinstance(instance, express::instances::MultiLeafInstance)

@given(instance=SETValue_strategy)
@settings(max_examples=50)
def test_setvalue_instantiation(instance):
    assert isinstance(instance, SETValue)

@given(instance=express::rules::Extent_strategy)
@settings(max_examples=50)
def test_express::rules::extent_instantiation(instance):
    assert isinstance(instance, express::rules::Extent)

@given(instance=SupertypeRule_strategy)
@settings(max_examples=50)
def test_supertyperule_instantiation(instance):
    assert isinstance(instance, SupertypeRule)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=express::expressions::Primary_strategy)
@settings(max_examples=50)
def test_express::expressions::primary_instantiation(instance):
    assert isinstance(instance, express::expressions::Primary)

@given(instance=express::expressions::AggregateInitializer_strategy)
@settings(max_examples=50)
def test_express::expressions::aggregateinitializer_instantiation(instance):
    assert isinstance(instance, express::expressions::AggregateInitializer)

@given(instance=express::expressions::Selector_strategy)
@settings(max_examples=50)
def test_express::expressions::selector_instantiation(instance):
    assert isinstance(instance, express::expressions::Selector)

@given(instance=express::expressions::FunctionCall_strategy)
@settings(max_examples=50)
def test_express::expressions::functioncall_instantiation(instance):
    assert isinstance(instance, express::expressions::FunctionCall)

@given(instance=express::expressions::Operation_strategy)
@settings(max_examples=50)
def test_express::expressions::operation_instantiation(instance):
    assert isinstance(instance, express::expressions::Operation)

@given(instance=express::expressions::IndexOperation_strategy)
@settings(max_examples=50)
def test_express::expressions::indexoperation_instantiation(instance):
    assert isinstance(instance, express::expressions::IndexOperation)

@given(instance=express::expressions::PartialEntityConstructor_strategy)
@settings(max_examples=50)
def test_express::expressions::partialentityconstructor_instantiation(instance):
    assert isinstance(instance, express::expressions::PartialEntityConstructor)

@given(instance=express::expressions::PartialEntityConstructor_strategy)
def test_express::expressions::partialentityconstructor_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=express::expressions::PartialEntityConstructor_strategy)
def test_express::expressions::partialentityconstructor_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Extent_strategy)
@settings(max_examples=50)
def test_extent_instantiation(instance):
    assert isinstance(instance, Extent)

@given(instance=express::rules::SubtypeConstraint_strategy)
@settings(max_examples=50)
def test_express::rules::subtypeconstraint_instantiation(instance):
    assert isinstance(instance, express::rules::SubtypeConstraint)

@given(instance=ActualParameter_strategy)
@settings(max_examples=50)
def test_actualparameter_instantiation(instance):
    assert isinstance(instance, ActualParameter)

@given(instance=Procedure_strategy)
@settings(max_examples=50)
def test_procedure_instantiation(instance):
    assert isinstance(instance, Procedure)

@given(instance=express::statements::ProcedureCall_strategy)
@settings(max_examples=50)
def test_express::statements::procedurecall_instantiation(instance):
    assert isinstance(instance, express::statements::ProcedureCall)

@given(instance=EntityType_strategy)
@settings(max_examples=50)
def test_entitytype_instantiation(instance):
    assert isinstance(instance, EntityType)

@given(instance=CommonElement_strategy)
@settings(max_examples=50)
def test_commonelement_instantiation(instance):
    assert isinstance(instance, CommonElement)

@given(instance=express::instances::Constant_strategy)
@settings(max_examples=50)
def test_express::instances::constant_instantiation(instance):
    assert isinstance(instance, express::instances::Constant)

@given(instance=express::rules::SupertypeRule_strategy)
@settings(max_examples=50)
def test_express::rules::supertyperule_instantiation(instance):
    assert isinstance(instance, express::rules::SupertypeRule)

@given(instance=express::rules::SupertypeRule_strategy)
def test_express::rules::supertyperule_assertsAbstract_type(instance):
    assert isinstance(instance.assertsAbstract, str)


@given(instance=express::rules::SupertypeRule_strategy)
def test_express::rules::supertyperule_assertsAbstract_setter(instance):
    original = instance.assertsAbstract
    instance.assertsAbstract = original
    assert instance.assertsAbstract == original

@given(instance=SubtypeConstraint_strategy)
@settings(max_examples=50)
def test_subtypeconstraint_instantiation(instance):
    assert isinstance(instance, SubtypeConstraint)

@given(instance=express::rules::ANDConstraint_strategy)
@settings(max_examples=50)
def test_express::rules::andconstraint_instantiation(instance):
    assert isinstance(instance, express::rules::ANDConstraint)

@given(instance=express::rules::TOTAL::OVERConstraint_strategy)
@settings(max_examples=50)
def test_express::rules::total::overconstraint_instantiation(instance):
    assert isinstance(instance, express::rules::TOTAL::OVERConstraint)

@given(instance=express::rules::ONEOFConstraint_strategy)
@settings(max_examples=50)
def test_express::rules::oneofconstraint_instantiation(instance):
    assert isinstance(instance, express::rules::ONEOFConstraint)
