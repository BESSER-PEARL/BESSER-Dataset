import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Configuration,
    vhdl::configuration::ConfigurationReference,
    configuration::vhdl::EntityReference,
    BlockConfiguration,
    configuration::vhdl::PortMaps,
    configuration::vhdl::GenericMaps,
    configuration::vhdl::MultiName,
    ConfigurationItem,
    vhdl::configuration::ComponentConfiguration,
    configuration::vhdl::Name,
    configuration::ConfigurationItem,
    nature::CompositeNatureDefinition,
    vhdl::type::TypeReference,
    vhdl::type::Typed,
    vhdl::nature::Natured,
    vhdl::nature::NatureReference,
    nature::vhdl::Name,
    RecordNatureElement,
    CompositeNatureDefinition,
    vhdl::nature::RecordNatureDefinition,
    ArrayNatureDefinition,
    vhdl::nature::UnconstrainedArrayNatureDefinition,
    vhdl::nature::ConstrainedArrayNatureDefinition,
    type::vhdl::Name,
    vhdl::type::PhysicalTypeDefinitionSecondary,
    PhysicalTypeDefinitionSecondary,
    EnumerationLiteral,
    vhdl::type::EnumerationLiteral,
    ArrayTypeDefinition,
    vhdl::type::UnconstrainedArrayTypeDefinition,
    vhdl::type::ConstrainedArrayTypeDefinition,
    type::CompositeTypeDefinition,
    RecordTypeElement,
    CompositeTypeDefinition,
    vhdl::type::RecordTypeDefinition,
    type::TypeDefinition,
    TypeDefinition,
    vhdl::type::EnumerationTypeDefinition,
    vhdl::type::CompositeTypeDefinition,
    vhdl::type::PhysicalTypeDefinition,
    vhdl::type::RangeTypeDefinition,
    NatureDefinition,
    vhdl::nature::ScalarNatureDefinition,
    vhdl::nature::CompositeNatureDefinition,
    ValueDeclaration,
    vhdl::declaration::VariableDeclaration,
    vhdl::declaration::SignalDeclaration,
    vhdl::declaration::ConstantDeclaration,
    SubprogramBody,
    declaration::vhdl::PortMaps,
    declaration::vhdl::GenericMaps,
    declaration::vhdl::EntityReference,
    declaration::vhdl::ComponentReference,
    declaration::SubprogramDeclaration,
    nature::Natured,
    vhdl::nature::ArrayNatureDefinition,
    SourceAspect,
    vhdl::ams::Spectrum,
    vhdl::ams::Noise,
    MultiNamed,
    declaration::QuantityDeclaration,
    QuantityAspect,
    QuantityDeclaration,
    vhdl::declaration::BranchQuantityDeclaration,
    declaration::vhdl::MultiName,
    declaration::vhdl::Name,
    AssociationExpression,
    vhdl::expression::ConditionalWaveformExpression,
    type::EnumerationLiteral,
    expression::ValueExpression,
    type::Typed,
    vhdl::type::FileTypeDefinition,
    vhdl::type::AccessTypeDefinition,
    vhdl::type::ArrayTypeDefinition,
    vhdl::declaration::FunctionDeclaration,
    vhdl::declaration::SourceQuantityDeclaration,
    vhdl::declaration::FreeQuantityDeclaration,
    expression::Expression,
    vhdl::expression::AllocatorExpression,
    Name,
    vhdl::expression::TypeQualificationExpression,
    vhdl::expression::IdentifierExpression,
    vhdl::expression::AllExpression,
    vhdl::expression::AttributeExpression,
    expression::MultiExpression,
    vhdl::expression::AggregateExpression,
    BinaryExpression,
    vhdl::expression::PowerExpression,
    vhdl::expression::RelationalExpression,
    vhdl::expression::MultiplyingExpression,
    vhdl::expression::AddingExpression,
    ConfigurationReference,
    statement::vhdl::EntityReference,
    IterationScheme,
    vhdl::statement::ForIterationScheme,
    vhdl::statement::WhileIterationScheme,
    GenerationScheme,
    vhdl::statement::IfGenerationScheme,
    statement::vhdl::ComponentReference,
    InstantiationStatement,
    vhdl::statement::ConfigurationInstantiationStatement,
    vhdl::statement::EntityInstantiationStatement,
    vhdl::statement::ComponentInstantiationStatement,
    statement::vhdl::Name,
    BreakStatementItem,
    statement::vhdl::PortMaps,
    statement::vhdl::Ports,
    statement::vhdl::GenericMaps,
    statement::vhdl::Generics,
    CaseAlternative,
    CaseStatement,
    vhdl::statement::SimultaneousCaseStatement,
    statement::vhdl::CallReference,
    IfStatementTest,
    IfStatement,
    vhdl::statement::SimultaneousIfStatement,
    vhdl::ComponentReference,
    statement::vhdl::MultiName,
    DelayMechanism,
    vhdl::statement::RejectMechanism,
    vhdl::statement::TransportMechanism,
    ConditionalSignalAssignmentStatement,
    vhdl::statement::SelectedSignalAssignmentStatement,
    SignalAssignmentStatement,
    vhdl::statement::SequentialSignalAssignmentStatement,
    vhdl::statement::ConditionalSignalAssignmentStatement,
    ExpressionStatement,
    vhdl::statement::ReturnStatement,
    SubprogramDeclaration,
    vhdl::declaration::ProcedureDeclaration,
    vhdl::CallReference,
    vhdl::VhdlObject,
    vhdl::MultiName,
    vhdl::MultiNamed,
    vhdl::Named,
    CallReference,
    vhdl::CallResolvedReference,
    configuration::ConfigurationReference,
    ComponentReference,
    PackageReference,
    EntityReference,
    nature::NatureReference,
    type::TypeReference,
    MultiName,
    declaration::Declaration,
    vhdl::declaration::DisconnectionSpecification,
    vhdl::declaration::TerminalDeclaration,
    vhdl::declaration::ValueDeclaration,
    vhdl::declaration::FileDeclaration,
    vhdl::declaration::LimitDeclaration,
    TypeReference,
    vhdl::PackageReference,
    Expression,
    vhdl::expression::UnaffectedExpression,
    vhdl::expression::AssociationExpression,
    vhdl::expression::ValueExpression,
    vhdl::expression::WaveformExpression,
    vhdl::expression::MultiExpression,
    vhdl::expression::NullExpression,
    Declaration,
    vhdl::declaration::ConfigurationSpecification,
    vhdl::declaration::QuantityDeclaration,
    vhdl::declaration::UseClauseDeclaration,
    vhdl::Name,
    VhdlObject,
    vhdl::declaration::Declaration,
    vhdl::statement::IterationScheme,
    vhdl::statement::BreakStatementItem,
    vhdl::statement::Statement,
    vhdl::statement::GenerationScheme,
    vhdl::declaration::SubprogramBody,
    vhdl::ams::SourceAspect,
    vhdl::Signature,
    vhdl::type::RecordTypeElement,
    vhdl::configuration::ConfigurationItem,
    vhdl::EntityResolvedReference,
    vhdl::Generics,
    vhdl::PortMaps,
    vhdl::type::TypeDefinition,
    vhdl::Model,
    vhdl::statement::IfStatementTest,
    vhdl::PackageResolvedReference,
    vhdl::NameList,
    vhdl::ComponentResolvedReference,
    vhdl::Module,
    vhdl::statement::CaseAlternative,
    vhdl::ams::QuantityAspect,
    vhdl::GenericMaps,
    vhdl::nature::RecordNatureElement,
    vhdl::configuration::ConfigurationResolvedReference,
    vhdl::Ports,
    vhdl::nature::NatureDefinition,
    vhdl::DesignUnit,
    Statement,
    vhdl::statement::ExitStatement,
    vhdl::statement::SimultaneousProceduralStatement,
    vhdl::statement::InstantiationStatement,
    vhdl::statement::WaitStatement,
    vhdl::statement::BlockStatement,
    vhdl::statement::NextStatement,
    vhdl::statement::ProcessStatement,
    vhdl::statement::LoopStatement,
    vhdl::statement::ProcedureCallStatement,
    vhdl::statement::ReportStatement,
    vhdl::statement::BreakStatement,
    vhdl::statement::AssertionStatement,
    vhdl::statement::IfStatement,
    vhdl::statement::VariableAssignmentStatement,
    vhdl::statement::SignalAssignmentStatement,
    vhdl::statement::CaseStatement,
    vhdl::statement::GenerateStatement,
    vhdl::statement::SimpleSimultaneousStatement,
    vhdl::EntityReference,
    Named,
    vhdl::declaration::AttributeSpecification,
    vhdl::declaration::GroupDeclaration,
    vhdl::declaration::SubnatureDeclaration,
    vhdl::declaration::NatureDeclaration,
    vhdl::declaration::SubprogramDeclaration,
    vhdl::Component,
    vhdl::declaration::AttributeDeclaration,
    vhdl::configuration::BlockConfiguration,
    vhdl::declaration::SubtypeDeclaration,
    vhdl::declaration::AliasDeclaration,
    vhdl::declaration::GroupTemplateDeclaration,
    vhdl::declaration::TypeDeclaration,
    Module,
    vhdl::Entity,
    vhdl::configuration::Configuration,
    vhdl::Package,
    vhdl::PackageBody,
    vhdl::Architecture,
    vhdl::expression::CharacterExpression,
    vhdl::expression::StringExpression,
    expression::BinaryExpression,
    vhdl::expression::RangeExpression,
    vhdl::expression::OthersExpression,
    vhdl::expression::OpenExpression,
    vhdl::expression::UnaryExpression,
    vhdl::expression::SignExpression,
    vhdl::expression::SignatureExpression,
    vhdl::expression::ShiftExpression,
    vhdl::expression::BinaryExpression,
    expression::vhdl::Name,
    vhdl::expression::NameExpression,
    vhdl::expression::LogicalExpression,
    NatureReference,
    expression::IndicationExpression,
    vhdl::expression::SubnatureIndicationExpression,
    vhdl::expression::SubtypeIndicationExpression,
    vhdl::expression::IndicationExpression,
    vhdl::expression::Expression,
    ValueExpression,
    vhdl::expression::UnitValueExpression,
    vhdl::expression::BitStringExpression,
    vhdl::statement::ForGenerationScheme,
    vhdl::statement::ExpressionStatement,
    vhdl::statement::DelayMechanism,
    expression::vhdl::Signature,
    Sign,
    ShiftOperator,
    AddingOperator,
    UnaryOperator,
    RangeDirection,
    MultiplyingOperator,
    EntityClass,
    LogicalOperator,
    SignalKind,
    Mode,
    Purity,
    RelationalOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_configuration_is_not_abstract():
    assert not inspect.isabstract(Configuration)


def test_configuration_constructor_exists():
    assert callable(Configuration.__init__)


def test_configuration_constructor_args():
    sig = inspect.signature(Configuration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::configuration::configurationreference_is_not_abstract():
    assert not inspect.isabstract(vhdl::configuration::ConfigurationReference)


def test_vhdl::configuration::configurationreference_constructor_exists():
    assert callable(vhdl::configuration::ConfigurationReference.__init__)


def test_vhdl::configuration::configurationreference_constructor_args():
    sig = inspect.signature(vhdl::configuration::ConfigurationReference.__init__)
    params = list(sig.parameters.keys())



def test_configuration::vhdl::entityreference_is_not_abstract():
    assert not inspect.isabstract(configuration::vhdl::EntityReference)


def test_configuration::vhdl::entityreference_constructor_exists():
    assert callable(configuration::vhdl::EntityReference.__init__)


def test_configuration::vhdl::entityreference_constructor_args():
    sig = inspect.signature(configuration::vhdl::EntityReference.__init__)
    params = list(sig.parameters.keys())



def test_blockconfiguration_is_not_abstract():
    assert not inspect.isabstract(BlockConfiguration)


def test_blockconfiguration_constructor_exists():
    assert callable(BlockConfiguration.__init__)


def test_blockconfiguration_constructor_args():
    sig = inspect.signature(BlockConfiguration.__init__)
    params = list(sig.parameters.keys())



def test_configuration::vhdl::portmaps_is_not_abstract():
    assert not inspect.isabstract(configuration::vhdl::PortMaps)


def test_configuration::vhdl::portmaps_constructor_exists():
    assert callable(configuration::vhdl::PortMaps.__init__)


def test_configuration::vhdl::portmaps_constructor_args():
    sig = inspect.signature(configuration::vhdl::PortMaps.__init__)
    params = list(sig.parameters.keys())



def test_configuration::vhdl::genericmaps_is_not_abstract():
    assert not inspect.isabstract(configuration::vhdl::GenericMaps)


def test_configuration::vhdl::genericmaps_constructor_exists():
    assert callable(configuration::vhdl::GenericMaps.__init__)


def test_configuration::vhdl::genericmaps_constructor_args():
    sig = inspect.signature(configuration::vhdl::GenericMaps.__init__)
    params = list(sig.parameters.keys())



def test_configuration::vhdl::multiname_is_not_abstract():
    assert not inspect.isabstract(configuration::vhdl::MultiName)


def test_configuration::vhdl::multiname_constructor_exists():
    assert callable(configuration::vhdl::MultiName.__init__)


def test_configuration::vhdl::multiname_constructor_args():
    sig = inspect.signature(configuration::vhdl::MultiName.__init__)
    params = list(sig.parameters.keys())



def test_configurationitem_is_not_abstract():
    assert not inspect.isabstract(ConfigurationItem)


def test_configurationitem_constructor_exists():
    assert callable(ConfigurationItem.__init__)


def test_configurationitem_constructor_args():
    sig = inspect.signature(ConfigurationItem.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::configuration::componentconfiguration_is_not_abstract():
    assert not inspect.isabstract(vhdl::configuration::ComponentConfiguration)


def test_vhdl::configuration::componentconfiguration_constructor_exists():
    assert callable(vhdl::configuration::ComponentConfiguration.__init__)


def test_vhdl::configuration::componentconfiguration_constructor_args():
    sig = inspect.signature(vhdl::configuration::ComponentConfiguration.__init__)
    params = list(sig.parameters.keys())



def test_configuration::vhdl::name_is_not_abstract():
    assert not inspect.isabstract(configuration::vhdl::Name)


def test_configuration::vhdl::name_constructor_exists():
    assert callable(configuration::vhdl::Name.__init__)


def test_configuration::vhdl::name_constructor_args():
    sig = inspect.signature(configuration::vhdl::Name.__init__)
    params = list(sig.parameters.keys())



def test_configuration::configurationitem_is_not_abstract():
    assert not inspect.isabstract(configuration::ConfigurationItem)


def test_configuration::configurationitem_constructor_exists():
    assert callable(configuration::ConfigurationItem.__init__)


def test_configuration::configurationitem_constructor_args():
    sig = inspect.signature(configuration::ConfigurationItem.__init__)
    params = list(sig.parameters.keys())



def test_nature::compositenaturedefinition_is_not_abstract():
    assert not inspect.isabstract(nature::CompositeNatureDefinition)


def test_nature::compositenaturedefinition_constructor_exists():
    assert callable(nature::CompositeNatureDefinition.__init__)


def test_nature::compositenaturedefinition_constructor_args():
    sig = inspect.signature(nature::CompositeNatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::type::typereference_is_not_abstract():
    assert not inspect.isabstract(vhdl::type::TypeReference)


def test_vhdl::type::typereference_constructor_exists():
    assert callable(vhdl::type::TypeReference.__init__)


def test_vhdl::type::typereference_constructor_args():
    sig = inspect.signature(vhdl::type::TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::type::typed_is_not_abstract():
    assert not inspect.isabstract(vhdl::type::Typed)


def test_vhdl::type::typed_constructor_exists():
    assert callable(vhdl::type::Typed.__init__)


def test_vhdl::type::typed_constructor_args():
    sig = inspect.signature(vhdl::type::Typed.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::nature::natured_is_not_abstract():
    assert not inspect.isabstract(vhdl::nature::Natured)


def test_vhdl::nature::natured_constructor_exists():
    assert callable(vhdl::nature::Natured.__init__)


def test_vhdl::nature::natured_constructor_args():
    sig = inspect.signature(vhdl::nature::Natured.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::nature::naturereference_is_not_abstract():
    assert not inspect.isabstract(vhdl::nature::NatureReference)


def test_vhdl::nature::naturereference_constructor_exists():
    assert callable(vhdl::nature::NatureReference.__init__)


def test_vhdl::nature::naturereference_constructor_args():
    sig = inspect.signature(vhdl::nature::NatureReference.__init__)
    params = list(sig.parameters.keys())



def test_nature::vhdl::name_is_not_abstract():
    assert not inspect.isabstract(nature::vhdl::Name)


def test_nature::vhdl::name_constructor_exists():
    assert callable(nature::vhdl::Name.__init__)


def test_nature::vhdl::name_constructor_args():
    sig = inspect.signature(nature::vhdl::Name.__init__)
    params = list(sig.parameters.keys())



def test_recordnatureelement_is_not_abstract():
    assert not inspect.isabstract(RecordNatureElement)


def test_recordnatureelement_constructor_exists():
    assert callable(RecordNatureElement.__init__)


def test_recordnatureelement_constructor_args():
    sig = inspect.signature(RecordNatureElement.__init__)
    params = list(sig.parameters.keys())



def test_compositenaturedefinition_is_not_abstract():
    assert not inspect.isabstract(CompositeNatureDefinition)


def test_compositenaturedefinition_constructor_exists():
    assert callable(CompositeNatureDefinition.__init__)


def test_compositenaturedefinition_constructor_args():
    sig = inspect.signature(CompositeNatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::nature::recordnaturedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl::nature::RecordNatureDefinition)


def test_vhdl::nature::recordnaturedefinition_constructor_exists():
    assert callable(vhdl::nature::RecordNatureDefinition.__init__)


def test_vhdl::nature::recordnaturedefinition_constructor_args():
    sig = inspect.signature(vhdl::nature::RecordNatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_arraynaturedefinition_is_not_abstract():
    assert not inspect.isabstract(ArrayNatureDefinition)


def test_arraynaturedefinition_constructor_exists():
    assert callable(ArrayNatureDefinition.__init__)


def test_arraynaturedefinition_constructor_args():
    sig = inspect.signature(ArrayNatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::nature::unconstrainedarraynaturedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl::nature::UnconstrainedArrayNatureDefinition)


def test_vhdl::nature::unconstrainedarraynaturedefinition_constructor_exists():
    assert callable(vhdl::nature::UnconstrainedArrayNatureDefinition.__init__)


def test_vhdl::nature::unconstrainedarraynaturedefinition_constructor_args():
    sig = inspect.signature(vhdl::nature::UnconstrainedArrayNatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::nature::constrainedarraynaturedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl::nature::ConstrainedArrayNatureDefinition)


def test_vhdl::nature::constrainedarraynaturedefinition_constructor_exists():
    assert callable(vhdl::nature::ConstrainedArrayNatureDefinition.__init__)


def test_vhdl::nature::constrainedarraynaturedefinition_constructor_args():
    sig = inspect.signature(vhdl::nature::ConstrainedArrayNatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_type::vhdl::name_is_not_abstract():
    assert not inspect.isabstract(type::vhdl::Name)


def test_type::vhdl::name_constructor_exists():
    assert callable(type::vhdl::Name.__init__)


def test_type::vhdl::name_constructor_args():
    sig = inspect.signature(type::vhdl::Name.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::type::physicaltypedefinitionsecondary_is_not_abstract():
    assert not inspect.isabstract(vhdl::type::PhysicalTypeDefinitionSecondary)


def test_vhdl::type::physicaltypedefinitionsecondary_constructor_exists():
    assert callable(vhdl::type::PhysicalTypeDefinitionSecondary.__init__)


def test_vhdl::type::physicaltypedefinitionsecondary_constructor_args():
    sig = inspect.signature(vhdl::type::PhysicalTypeDefinitionSecondary.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"
    assert "name" in params, "Missing parameter 'name'"

def test_vhdl::type::physicaltypedefinitionsecondary_has_number():
    assert hasattr(vhdl::type::PhysicalTypeDefinitionSecondary, "number")
    descriptor = None
    for klass in vhdl::type::PhysicalTypeDefinitionSecondary.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_vhdl::type::physicaltypedefinitionsecondary_has_name():
    assert hasattr(vhdl::type::PhysicalTypeDefinitionSecondary, "name")
    descriptor = None
    for klass in vhdl::type::PhysicalTypeDefinitionSecondary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_physicaltypedefinitionsecondary_is_not_abstract():
    assert not inspect.isabstract(PhysicalTypeDefinitionSecondary)


def test_physicaltypedefinitionsecondary_constructor_exists():
    assert callable(PhysicalTypeDefinitionSecondary.__init__)


def test_physicaltypedefinitionsecondary_constructor_args():
    sig = inspect.signature(PhysicalTypeDefinitionSecondary.__init__)
    params = list(sig.parameters.keys())



def test_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(EnumerationLiteral)


def test_enumerationliteral_constructor_exists():
    assert callable(EnumerationLiteral.__init__)


def test_enumerationliteral_constructor_args():
    sig = inspect.signature(EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::type::enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(vhdl::type::EnumerationLiteral)


def test_vhdl::type::enumerationliteral_constructor_exists():
    assert callable(vhdl::type::EnumerationLiteral.__init__)


def test_vhdl::type::enumerationliteral_constructor_args():
    sig = inspect.signature(vhdl::type::EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_arraytypedefinition_is_not_abstract():
    assert not inspect.isabstract(ArrayTypeDefinition)


def test_arraytypedefinition_constructor_exists():
    assert callable(ArrayTypeDefinition.__init__)


def test_arraytypedefinition_constructor_args():
    sig = inspect.signature(ArrayTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::type::unconstrainedarraytypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl::type::UnconstrainedArrayTypeDefinition)


def test_vhdl::type::unconstrainedarraytypedefinition_constructor_exists():
    assert callable(vhdl::type::UnconstrainedArrayTypeDefinition.__init__)


def test_vhdl::type::unconstrainedarraytypedefinition_constructor_args():
    sig = inspect.signature(vhdl::type::UnconstrainedArrayTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::type::constrainedarraytypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl::type::ConstrainedArrayTypeDefinition)


def test_vhdl::type::constrainedarraytypedefinition_constructor_exists():
    assert callable(vhdl::type::ConstrainedArrayTypeDefinition.__init__)


def test_vhdl::type::constrainedarraytypedefinition_constructor_args():
    sig = inspect.signature(vhdl::type::ConstrainedArrayTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_type::compositetypedefinition_is_not_abstract():
    assert not inspect.isabstract(type::CompositeTypeDefinition)


def test_type::compositetypedefinition_constructor_exists():
    assert callable(type::CompositeTypeDefinition.__init__)


def test_type::compositetypedefinition_constructor_args():
    sig = inspect.signature(type::CompositeTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_recordtypeelement_is_not_abstract():
    assert not inspect.isabstract(RecordTypeElement)


def test_recordtypeelement_constructor_exists():
    assert callable(RecordTypeElement.__init__)


def test_recordtypeelement_constructor_args():
    sig = inspect.signature(RecordTypeElement.__init__)
    params = list(sig.parameters.keys())



def test_compositetypedefinition_is_not_abstract():
    assert not inspect.isabstract(CompositeTypeDefinition)


def test_compositetypedefinition_constructor_exists():
    assert callable(CompositeTypeDefinition.__init__)


def test_compositetypedefinition_constructor_args():
    sig = inspect.signature(CompositeTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::type::recordtypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl::type::RecordTypeDefinition)


def test_vhdl::type::recordtypedefinition_constructor_exists():
    assert callable(vhdl::type::RecordTypeDefinition.__init__)


def test_vhdl::type::recordtypedefinition_constructor_args():
    sig = inspect.signature(vhdl::type::RecordTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_type::typedefinition_is_not_abstract():
    assert not inspect.isabstract(type::TypeDefinition)


def test_type::typedefinition_constructor_exists():
    assert callable(type::TypeDefinition.__init__)


def test_type::typedefinition_constructor_args():
    sig = inspect.signature(type::TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_typedefinition_is_not_abstract():
    assert not inspect.isabstract(TypeDefinition)


def test_typedefinition_constructor_exists():
    assert callable(TypeDefinition.__init__)


def test_typedefinition_constructor_args():
    sig = inspect.signature(TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::type::enumerationtypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl::type::EnumerationTypeDefinition)


def test_vhdl::type::enumerationtypedefinition_constructor_exists():
    assert callable(vhdl::type::EnumerationTypeDefinition.__init__)


def test_vhdl::type::enumerationtypedefinition_constructor_args():
    sig = inspect.signature(vhdl::type::EnumerationTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::type::compositetypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl::type::CompositeTypeDefinition)


def test_vhdl::type::compositetypedefinition_constructor_exists():
    assert callable(vhdl::type::CompositeTypeDefinition.__init__)


def test_vhdl::type::compositetypedefinition_constructor_args():
    sig = inspect.signature(vhdl::type::CompositeTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::type::physicaltypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl::type::PhysicalTypeDefinition)


def test_vhdl::type::physicaltypedefinition_constructor_exists():
    assert callable(vhdl::type::PhysicalTypeDefinition.__init__)


def test_vhdl::type::physicaltypedefinition_constructor_args():
    sig = inspect.signature(vhdl::type::PhysicalTypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "primary" in params, "Missing parameter 'primary'"

def test_vhdl::type::physicaltypedefinition_has_primary():
    assert hasattr(vhdl::type::PhysicalTypeDefinition, "primary")
    descriptor = None
    for klass in vhdl::type::PhysicalTypeDefinition.__mro__:
        if "primary" in klass.__dict__:
            descriptor = klass.__dict__["primary"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::type::rangetypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl::type::RangeTypeDefinition)


def test_vhdl::type::rangetypedefinition_constructor_exists():
    assert callable(vhdl::type::RangeTypeDefinition.__init__)


def test_vhdl::type::rangetypedefinition_constructor_args():
    sig = inspect.signature(vhdl::type::RangeTypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_vhdl::type::rangetypedefinition_has_direction():
    assert hasattr(vhdl::type::RangeTypeDefinition, "direction")
    descriptor = None
    for klass in vhdl::type::RangeTypeDefinition.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_naturedefinition_is_not_abstract():
    assert not inspect.isabstract(NatureDefinition)


def test_naturedefinition_constructor_exists():
    assert callable(NatureDefinition.__init__)


def test_naturedefinition_constructor_args():
    sig = inspect.signature(NatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::nature::scalarnaturedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl::nature::ScalarNatureDefinition)


def test_vhdl::nature::scalarnaturedefinition_constructor_exists():
    assert callable(vhdl::nature::ScalarNatureDefinition.__init__)


def test_vhdl::nature::scalarnaturedefinition_constructor_args():
    sig = inspect.signature(vhdl::nature::ScalarNatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::nature::compositenaturedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl::nature::CompositeNatureDefinition)


def test_vhdl::nature::compositenaturedefinition_constructor_exists():
    assert callable(vhdl::nature::CompositeNatureDefinition.__init__)


def test_vhdl::nature::compositenaturedefinition_constructor_args():
    sig = inspect.signature(vhdl::nature::CompositeNatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_valuedeclaration_is_not_abstract():
    assert not inspect.isabstract(ValueDeclaration)


def test_valuedeclaration_constructor_exists():
    assert callable(ValueDeclaration.__init__)


def test_valuedeclaration_constructor_args():
    sig = inspect.signature(ValueDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::declaration::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl::declaration::VariableDeclaration)


def test_vhdl::declaration::variabledeclaration_constructor_exists():
    assert callable(vhdl::declaration::VariableDeclaration.__init__)


def test_vhdl::declaration::variabledeclaration_constructor_args():
    sig = inspect.signature(vhdl::declaration::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"
    assert "shared" in params, "Missing parameter 'shared'"

def test_vhdl::declaration::variabledeclaration_has_mode():
    assert hasattr(vhdl::declaration::VariableDeclaration, "mode")
    descriptor = None
    for klass in vhdl::declaration::VariableDeclaration.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)

def test_vhdl::declaration::variabledeclaration_has_shared():
    assert hasattr(vhdl::declaration::VariableDeclaration, "shared")
    descriptor = None
    for klass in vhdl::declaration::VariableDeclaration.__mro__:
        if "shared" in klass.__dict__:
            descriptor = klass.__dict__["shared"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::declaration::signaldeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl::declaration::SignalDeclaration)


def test_vhdl::declaration::signaldeclaration_constructor_exists():
    assert callable(vhdl::declaration::SignalDeclaration.__init__)


def test_vhdl::declaration::signaldeclaration_constructor_args():
    sig = inspect.signature(vhdl::declaration::SignalDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "mode" in params, "Missing parameter 'mode'"

def test_vhdl::declaration::signaldeclaration_has_kind():
    assert hasattr(vhdl::declaration::SignalDeclaration, "kind")
    descriptor = None
    for klass in vhdl::declaration::SignalDeclaration.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_vhdl::declaration::signaldeclaration_has_mode():
    assert hasattr(vhdl::declaration::SignalDeclaration, "mode")
    descriptor = None
    for klass in vhdl::declaration::SignalDeclaration.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::declaration::constantdeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl::declaration::ConstantDeclaration)


def test_vhdl::declaration::constantdeclaration_constructor_exists():
    assert callable(vhdl::declaration::ConstantDeclaration.__init__)


def test_vhdl::declaration::constantdeclaration_constructor_args():
    sig = inspect.signature(vhdl::declaration::ConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_subprogrambody_is_not_abstract():
    assert not inspect.isabstract(SubprogramBody)


def test_subprogrambody_constructor_exists():
    assert callable(SubprogramBody.__init__)


def test_subprogrambody_constructor_args():
    sig = inspect.signature(SubprogramBody.__init__)
    params = list(sig.parameters.keys())



def test_declaration::vhdl::portmaps_is_not_abstract():
    assert not inspect.isabstract(declaration::vhdl::PortMaps)


def test_declaration::vhdl::portmaps_constructor_exists():
    assert callable(declaration::vhdl::PortMaps.__init__)


def test_declaration::vhdl::portmaps_constructor_args():
    sig = inspect.signature(declaration::vhdl::PortMaps.__init__)
    params = list(sig.parameters.keys())



def test_declaration::vhdl::genericmaps_is_not_abstract():
    assert not inspect.isabstract(declaration::vhdl::GenericMaps)


def test_declaration::vhdl::genericmaps_constructor_exists():
    assert callable(declaration::vhdl::GenericMaps.__init__)


def test_declaration::vhdl::genericmaps_constructor_args():
    sig = inspect.signature(declaration::vhdl::GenericMaps.__init__)
    params = list(sig.parameters.keys())



def test_declaration::vhdl::entityreference_is_not_abstract():
    assert not inspect.isabstract(declaration::vhdl::EntityReference)


def test_declaration::vhdl::entityreference_constructor_exists():
    assert callable(declaration::vhdl::EntityReference.__init__)


def test_declaration::vhdl::entityreference_constructor_args():
    sig = inspect.signature(declaration::vhdl::EntityReference.__init__)
    params = list(sig.parameters.keys())



def test_declaration::vhdl::componentreference_is_not_abstract():
    assert not inspect.isabstract(declaration::vhdl::ComponentReference)


def test_declaration::vhdl::componentreference_constructor_exists():
    assert callable(declaration::vhdl::ComponentReference.__init__)


def test_declaration::vhdl::componentreference_constructor_args():
    sig = inspect.signature(declaration::vhdl::ComponentReference.__init__)
    params = list(sig.parameters.keys())



def test_declaration::subprogramdeclaration_is_not_abstract():
    assert not inspect.isabstract(declaration::SubprogramDeclaration)


def test_declaration::subprogramdeclaration_constructor_exists():
    assert callable(declaration::SubprogramDeclaration.__init__)


def test_declaration::subprogramdeclaration_constructor_args():
    sig = inspect.signature(declaration::SubprogramDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_nature::natured_is_not_abstract():
    assert not inspect.isabstract(nature::Natured)


def test_nature::natured_constructor_exists():
    assert callable(nature::Natured.__init__)


def test_nature::natured_constructor_args():
    sig = inspect.signature(nature::Natured.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::nature::arraynaturedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl::nature::ArrayNatureDefinition)


def test_vhdl::nature::arraynaturedefinition_constructor_exists():
    assert callable(vhdl::nature::ArrayNatureDefinition.__init__)


def test_vhdl::nature::arraynaturedefinition_constructor_args():
    sig = inspect.signature(vhdl::nature::ArrayNatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_sourceaspect_is_not_abstract():
    assert not inspect.isabstract(SourceAspect)


def test_sourceaspect_constructor_exists():
    assert callable(SourceAspect.__init__)


def test_sourceaspect_constructor_args():
    sig = inspect.signature(SourceAspect.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::ams::spectrum_is_not_abstract():
    assert not inspect.isabstract(vhdl::ams::Spectrum)


def test_vhdl::ams::spectrum_constructor_exists():
    assert callable(vhdl::ams::Spectrum.__init__)


def test_vhdl::ams::spectrum_constructor_args():
    sig = inspect.signature(vhdl::ams::Spectrum.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::ams::noise_is_not_abstract():
    assert not inspect.isabstract(vhdl::ams::Noise)


def test_vhdl::ams::noise_constructor_exists():
    assert callable(vhdl::ams::Noise.__init__)


def test_vhdl::ams::noise_constructor_args():
    sig = inspect.signature(vhdl::ams::Noise.__init__)
    params = list(sig.parameters.keys())



def test_multinamed_is_not_abstract():
    assert not inspect.isabstract(MultiNamed)


def test_multinamed_constructor_exists():
    assert callable(MultiNamed.__init__)


def test_multinamed_constructor_args():
    sig = inspect.signature(MultiNamed.__init__)
    params = list(sig.parameters.keys())



def test_declaration::quantitydeclaration_is_not_abstract():
    assert not inspect.isabstract(declaration::QuantityDeclaration)


def test_declaration::quantitydeclaration_constructor_exists():
    assert callable(declaration::QuantityDeclaration.__init__)


def test_declaration::quantitydeclaration_constructor_args():
    sig = inspect.signature(declaration::QuantityDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_quantityaspect_is_not_abstract():
    assert not inspect.isabstract(QuantityAspect)


def test_quantityaspect_constructor_exists():
    assert callable(QuantityAspect.__init__)


def test_quantityaspect_constructor_args():
    sig = inspect.signature(QuantityAspect.__init__)
    params = list(sig.parameters.keys())



def test_quantitydeclaration_is_not_abstract():
    assert not inspect.isabstract(QuantityDeclaration)


def test_quantitydeclaration_constructor_exists():
    assert callable(QuantityDeclaration.__init__)


def test_quantitydeclaration_constructor_args():
    sig = inspect.signature(QuantityDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::declaration::branchquantitydeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl::declaration::BranchQuantityDeclaration)


def test_vhdl::declaration::branchquantitydeclaration_constructor_exists():
    assert callable(vhdl::declaration::BranchQuantityDeclaration.__init__)


def test_vhdl::declaration::branchquantitydeclaration_constructor_args():
    sig = inspect.signature(vhdl::declaration::BranchQuantityDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_declaration::vhdl::multiname_is_not_abstract():
    assert not inspect.isabstract(declaration::vhdl::MultiName)


def test_declaration::vhdl::multiname_constructor_exists():
    assert callable(declaration::vhdl::MultiName.__init__)


def test_declaration::vhdl::multiname_constructor_args():
    sig = inspect.signature(declaration::vhdl::MultiName.__init__)
    params = list(sig.parameters.keys())



def test_declaration::vhdl::name_is_not_abstract():
    assert not inspect.isabstract(declaration::vhdl::Name)


def test_declaration::vhdl::name_constructor_exists():
    assert callable(declaration::vhdl::Name.__init__)


def test_declaration::vhdl::name_constructor_args():
    sig = inspect.signature(declaration::vhdl::Name.__init__)
    params = list(sig.parameters.keys())



def test_associationexpression_is_not_abstract():
    assert not inspect.isabstract(AssociationExpression)


def test_associationexpression_constructor_exists():
    assert callable(AssociationExpression.__init__)


def test_associationexpression_constructor_args():
    sig = inspect.signature(AssociationExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::expression::conditionalwaveformexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::ConditionalWaveformExpression)


def test_vhdl::expression::conditionalwaveformexpression_constructor_exists():
    assert callable(vhdl::expression::ConditionalWaveformExpression.__init__)


def test_vhdl::expression::conditionalwaveformexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::ConditionalWaveformExpression.__init__)
    params = list(sig.parameters.keys())



def test_type::enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(type::EnumerationLiteral)


def test_type::enumerationliteral_constructor_exists():
    assert callable(type::EnumerationLiteral.__init__)


def test_type::enumerationliteral_constructor_args():
    sig = inspect.signature(type::EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_expression::valueexpression_is_not_abstract():
    assert not inspect.isabstract(expression::ValueExpression)


def test_expression::valueexpression_constructor_exists():
    assert callable(expression::ValueExpression.__init__)


def test_expression::valueexpression_constructor_args():
    sig = inspect.signature(expression::ValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_type::typed_is_not_abstract():
    assert not inspect.isabstract(type::Typed)


def test_type::typed_constructor_exists():
    assert callable(type::Typed.__init__)


def test_type::typed_constructor_args():
    sig = inspect.signature(type::Typed.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::type::filetypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl::type::FileTypeDefinition)


def test_vhdl::type::filetypedefinition_constructor_exists():
    assert callable(vhdl::type::FileTypeDefinition.__init__)


def test_vhdl::type::filetypedefinition_constructor_args():
    sig = inspect.signature(vhdl::type::FileTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::type::accesstypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl::type::AccessTypeDefinition)


def test_vhdl::type::accesstypedefinition_constructor_exists():
    assert callable(vhdl::type::AccessTypeDefinition.__init__)


def test_vhdl::type::accesstypedefinition_constructor_args():
    sig = inspect.signature(vhdl::type::AccessTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::type::arraytypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl::type::ArrayTypeDefinition)


def test_vhdl::type::arraytypedefinition_constructor_exists():
    assert callable(vhdl::type::ArrayTypeDefinition.__init__)


def test_vhdl::type::arraytypedefinition_constructor_args():
    sig = inspect.signature(vhdl::type::ArrayTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::declaration::functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl::declaration::FunctionDeclaration)


def test_vhdl::declaration::functiondeclaration_constructor_exists():
    assert callable(vhdl::declaration::FunctionDeclaration.__init__)


def test_vhdl::declaration::functiondeclaration_constructor_args():
    sig = inspect.signature(vhdl::declaration::FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "purity" in params, "Missing parameter 'purity'"

def test_vhdl::declaration::functiondeclaration_has_purity():
    assert hasattr(vhdl::declaration::FunctionDeclaration, "purity")
    descriptor = None
    for klass in vhdl::declaration::FunctionDeclaration.__mro__:
        if "purity" in klass.__dict__:
            descriptor = klass.__dict__["purity"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::declaration::sourcequantitydeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl::declaration::SourceQuantityDeclaration)


def test_vhdl::declaration::sourcequantitydeclaration_constructor_exists():
    assert callable(vhdl::declaration::SourceQuantityDeclaration.__init__)


def test_vhdl::declaration::sourcequantitydeclaration_constructor_args():
    sig = inspect.signature(vhdl::declaration::SourceQuantityDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::declaration::freequantitydeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl::declaration::FreeQuantityDeclaration)


def test_vhdl::declaration::freequantitydeclaration_constructor_exists():
    assert callable(vhdl::declaration::FreeQuantityDeclaration.__init__)


def test_vhdl::declaration::freequantitydeclaration_constructor_args():
    sig = inspect.signature(vhdl::declaration::FreeQuantityDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_expression::expression_is_not_abstract():
    assert not inspect.isabstract(expression::Expression)


def test_expression::expression_constructor_exists():
    assert callable(expression::Expression.__init__)


def test_expression::expression_constructor_args():
    sig = inspect.signature(expression::Expression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::expression::allocatorexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::AllocatorExpression)


def test_vhdl::expression::allocatorexpression_constructor_exists():
    assert callable(vhdl::expression::AllocatorExpression.__init__)


def test_vhdl::expression::allocatorexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::AllocatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_name_is_not_abstract():
    assert not inspect.isabstract(Name)


def test_name_constructor_exists():
    assert callable(Name.__init__)


def test_name_constructor_args():
    sig = inspect.signature(Name.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::expression::typequalificationexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::TypeQualificationExpression)


def test_vhdl::expression::typequalificationexpression_constructor_exists():
    assert callable(vhdl::expression::TypeQualificationExpression.__init__)


def test_vhdl::expression::typequalificationexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::TypeQualificationExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::expression::identifierexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::IdentifierExpression)


def test_vhdl::expression::identifierexpression_constructor_exists():
    assert callable(vhdl::expression::IdentifierExpression.__init__)


def test_vhdl::expression::identifierexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::IdentifierExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::expression::allexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::AllExpression)


def test_vhdl::expression::allexpression_constructor_exists():
    assert callable(vhdl::expression::AllExpression.__init__)


def test_vhdl::expression::allexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::AllExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::expression::attributeexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::AttributeExpression)


def test_vhdl::expression::attributeexpression_constructor_exists():
    assert callable(vhdl::expression::AttributeExpression.__init__)


def test_vhdl::expression::attributeexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::AttributeExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression::multiexpression_is_not_abstract():
    assert not inspect.isabstract(expression::MultiExpression)


def test_expression::multiexpression_constructor_exists():
    assert callable(expression::MultiExpression.__init__)


def test_expression::multiexpression_constructor_args():
    sig = inspect.signature(expression::MultiExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::expression::aggregateexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::AggregateExpression)


def test_vhdl::expression::aggregateexpression_constructor_exists():
    assert callable(vhdl::expression::AggregateExpression.__init__)


def test_vhdl::expression::aggregateexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::AggregateExpression.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::expression::powerexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::PowerExpression)


def test_vhdl::expression::powerexpression_constructor_exists():
    assert callable(vhdl::expression::PowerExpression.__init__)


def test_vhdl::expression::powerexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::PowerExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::expression::relationalexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::RelationalExpression)


def test_vhdl::expression::relationalexpression_constructor_exists():
    assert callable(vhdl::expression::RelationalExpression.__init__)


def test_vhdl::expression::relationalexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::RelationalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_vhdl::expression::relationalexpression_has_operator():
    assert hasattr(vhdl::expression::RelationalExpression, "operator")
    descriptor = None
    for klass in vhdl::expression::RelationalExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::expression::multiplyingexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::MultiplyingExpression)


def test_vhdl::expression::multiplyingexpression_constructor_exists():
    assert callable(vhdl::expression::MultiplyingExpression.__init__)


def test_vhdl::expression::multiplyingexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::MultiplyingExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_vhdl::expression::multiplyingexpression_has_operator():
    assert hasattr(vhdl::expression::MultiplyingExpression, "operator")
    descriptor = None
    for klass in vhdl::expression::MultiplyingExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::expression::addingexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::AddingExpression)


def test_vhdl::expression::addingexpression_constructor_exists():
    assert callable(vhdl::expression::AddingExpression.__init__)


def test_vhdl::expression::addingexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::AddingExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_vhdl::expression::addingexpression_has_operator():
    assert hasattr(vhdl::expression::AddingExpression, "operator")
    descriptor = None
    for klass in vhdl::expression::AddingExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_configurationreference_is_not_abstract():
    assert not inspect.isabstract(ConfigurationReference)


def test_configurationreference_constructor_exists():
    assert callable(ConfigurationReference.__init__)


def test_configurationreference_constructor_args():
    sig = inspect.signature(ConfigurationReference.__init__)
    params = list(sig.parameters.keys())



def test_statement::vhdl::entityreference_is_not_abstract():
    assert not inspect.isabstract(statement::vhdl::EntityReference)


def test_statement::vhdl::entityreference_constructor_exists():
    assert callable(statement::vhdl::EntityReference.__init__)


def test_statement::vhdl::entityreference_constructor_args():
    sig = inspect.signature(statement::vhdl::EntityReference.__init__)
    params = list(sig.parameters.keys())



def test_iterationscheme_is_not_abstract():
    assert not inspect.isabstract(IterationScheme)


def test_iterationscheme_constructor_exists():
    assert callable(IterationScheme.__init__)


def test_iterationscheme_constructor_args():
    sig = inspect.signature(IterationScheme.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::statement::foriterationscheme_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::ForIterationScheme)


def test_vhdl::statement::foriterationscheme_constructor_exists():
    assert callable(vhdl::statement::ForIterationScheme.__init__)


def test_vhdl::statement::foriterationscheme_constructor_args():
    sig = inspect.signature(vhdl::statement::ForIterationScheme.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_vhdl::statement::foriterationscheme_has_variable():
    assert hasattr(vhdl::statement::ForIterationScheme, "variable")
    descriptor = None
    for klass in vhdl::statement::ForIterationScheme.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::statement::whileiterationscheme_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::WhileIterationScheme)


def test_vhdl::statement::whileiterationscheme_constructor_exists():
    assert callable(vhdl::statement::WhileIterationScheme.__init__)


def test_vhdl::statement::whileiterationscheme_constructor_args():
    sig = inspect.signature(vhdl::statement::WhileIterationScheme.__init__)
    params = list(sig.parameters.keys())



def test_generationscheme_is_not_abstract():
    assert not inspect.isabstract(GenerationScheme)


def test_generationscheme_constructor_exists():
    assert callable(GenerationScheme.__init__)


def test_generationscheme_constructor_args():
    sig = inspect.signature(GenerationScheme.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::statement::ifgenerationscheme_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::IfGenerationScheme)


def test_vhdl::statement::ifgenerationscheme_constructor_exists():
    assert callable(vhdl::statement::IfGenerationScheme.__init__)


def test_vhdl::statement::ifgenerationscheme_constructor_args():
    sig = inspect.signature(vhdl::statement::IfGenerationScheme.__init__)
    params = list(sig.parameters.keys())



def test_statement::vhdl::componentreference_is_not_abstract():
    assert not inspect.isabstract(statement::vhdl::ComponentReference)


def test_statement::vhdl::componentreference_constructor_exists():
    assert callable(statement::vhdl::ComponentReference.__init__)


def test_statement::vhdl::componentreference_constructor_args():
    sig = inspect.signature(statement::vhdl::ComponentReference.__init__)
    params = list(sig.parameters.keys())



def test_instantiationstatement_is_not_abstract():
    assert not inspect.isabstract(InstantiationStatement)


def test_instantiationstatement_constructor_exists():
    assert callable(InstantiationStatement.__init__)


def test_instantiationstatement_constructor_args():
    sig = inspect.signature(InstantiationStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::statement::configurationinstantiationstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::ConfigurationInstantiationStatement)


def test_vhdl::statement::configurationinstantiationstatement_constructor_exists():
    assert callable(vhdl::statement::ConfigurationInstantiationStatement.__init__)


def test_vhdl::statement::configurationinstantiationstatement_constructor_args():
    sig = inspect.signature(vhdl::statement::ConfigurationInstantiationStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::statement::entityinstantiationstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::EntityInstantiationStatement)


def test_vhdl::statement::entityinstantiationstatement_constructor_exists():
    assert callable(vhdl::statement::EntityInstantiationStatement.__init__)


def test_vhdl::statement::entityinstantiationstatement_constructor_args():
    sig = inspect.signature(vhdl::statement::EntityInstantiationStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::statement::componentinstantiationstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::ComponentInstantiationStatement)


def test_vhdl::statement::componentinstantiationstatement_constructor_exists():
    assert callable(vhdl::statement::ComponentInstantiationStatement.__init__)


def test_vhdl::statement::componentinstantiationstatement_constructor_args():
    sig = inspect.signature(vhdl::statement::ComponentInstantiationStatement.__init__)
    params = list(sig.parameters.keys())



def test_statement::vhdl::name_is_not_abstract():
    assert not inspect.isabstract(statement::vhdl::Name)


def test_statement::vhdl::name_constructor_exists():
    assert callable(statement::vhdl::Name.__init__)


def test_statement::vhdl::name_constructor_args():
    sig = inspect.signature(statement::vhdl::Name.__init__)
    params = list(sig.parameters.keys())



def test_breakstatementitem_is_not_abstract():
    assert not inspect.isabstract(BreakStatementItem)


def test_breakstatementitem_constructor_exists():
    assert callable(BreakStatementItem.__init__)


def test_breakstatementitem_constructor_args():
    sig = inspect.signature(BreakStatementItem.__init__)
    params = list(sig.parameters.keys())



def test_statement::vhdl::portmaps_is_not_abstract():
    assert not inspect.isabstract(statement::vhdl::PortMaps)


def test_statement::vhdl::portmaps_constructor_exists():
    assert callable(statement::vhdl::PortMaps.__init__)


def test_statement::vhdl::portmaps_constructor_args():
    sig = inspect.signature(statement::vhdl::PortMaps.__init__)
    params = list(sig.parameters.keys())



def test_statement::vhdl::ports_is_not_abstract():
    assert not inspect.isabstract(statement::vhdl::Ports)


def test_statement::vhdl::ports_constructor_exists():
    assert callable(statement::vhdl::Ports.__init__)


def test_statement::vhdl::ports_constructor_args():
    sig = inspect.signature(statement::vhdl::Ports.__init__)
    params = list(sig.parameters.keys())



def test_statement::vhdl::genericmaps_is_not_abstract():
    assert not inspect.isabstract(statement::vhdl::GenericMaps)


def test_statement::vhdl::genericmaps_constructor_exists():
    assert callable(statement::vhdl::GenericMaps.__init__)


def test_statement::vhdl::genericmaps_constructor_args():
    sig = inspect.signature(statement::vhdl::GenericMaps.__init__)
    params = list(sig.parameters.keys())



def test_statement::vhdl::generics_is_not_abstract():
    assert not inspect.isabstract(statement::vhdl::Generics)


def test_statement::vhdl::generics_constructor_exists():
    assert callable(statement::vhdl::Generics.__init__)


def test_statement::vhdl::generics_constructor_args():
    sig = inspect.signature(statement::vhdl::Generics.__init__)
    params = list(sig.parameters.keys())



def test_casealternative_is_not_abstract():
    assert not inspect.isabstract(CaseAlternative)


def test_casealternative_constructor_exists():
    assert callable(CaseAlternative.__init__)


def test_casealternative_constructor_args():
    sig = inspect.signature(CaseAlternative.__init__)
    params = list(sig.parameters.keys())



def test_casestatement_is_not_abstract():
    assert not inspect.isabstract(CaseStatement)


def test_casestatement_constructor_exists():
    assert callable(CaseStatement.__init__)


def test_casestatement_constructor_args():
    sig = inspect.signature(CaseStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::statement::simultaneouscasestatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::SimultaneousCaseStatement)


def test_vhdl::statement::simultaneouscasestatement_constructor_exists():
    assert callable(vhdl::statement::SimultaneousCaseStatement.__init__)


def test_vhdl::statement::simultaneouscasestatement_constructor_args():
    sig = inspect.signature(vhdl::statement::SimultaneousCaseStatement.__init__)
    params = list(sig.parameters.keys())



def test_statement::vhdl::callreference_is_not_abstract():
    assert not inspect.isabstract(statement::vhdl::CallReference)


def test_statement::vhdl::callreference_constructor_exists():
    assert callable(statement::vhdl::CallReference.__init__)


def test_statement::vhdl::callreference_constructor_args():
    sig = inspect.signature(statement::vhdl::CallReference.__init__)
    params = list(sig.parameters.keys())



def test_ifstatementtest_is_not_abstract():
    assert not inspect.isabstract(IfStatementTest)


def test_ifstatementtest_constructor_exists():
    assert callable(IfStatementTest.__init__)


def test_ifstatementtest_constructor_args():
    sig = inspect.signature(IfStatementTest.__init__)
    params = list(sig.parameters.keys())



def test_ifstatement_is_not_abstract():
    assert not inspect.isabstract(IfStatement)


def test_ifstatement_constructor_exists():
    assert callable(IfStatement.__init__)


def test_ifstatement_constructor_args():
    sig = inspect.signature(IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::statement::simultaneousifstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::SimultaneousIfStatement)


def test_vhdl::statement::simultaneousifstatement_constructor_exists():
    assert callable(vhdl::statement::SimultaneousIfStatement.__init__)


def test_vhdl::statement::simultaneousifstatement_constructor_args():
    sig = inspect.signature(vhdl::statement::SimultaneousIfStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::componentreference_is_not_abstract():
    assert not inspect.isabstract(vhdl::ComponentReference)


def test_vhdl::componentreference_constructor_exists():
    assert callable(vhdl::ComponentReference.__init__)


def test_vhdl::componentreference_constructor_args():
    sig = inspect.signature(vhdl::ComponentReference.__init__)
    params = list(sig.parameters.keys())



def test_statement::vhdl::multiname_is_not_abstract():
    assert not inspect.isabstract(statement::vhdl::MultiName)


def test_statement::vhdl::multiname_constructor_exists():
    assert callable(statement::vhdl::MultiName.__init__)


def test_statement::vhdl::multiname_constructor_args():
    sig = inspect.signature(statement::vhdl::MultiName.__init__)
    params = list(sig.parameters.keys())



def test_delaymechanism_is_not_abstract():
    assert not inspect.isabstract(DelayMechanism)


def test_delaymechanism_constructor_exists():
    assert callable(DelayMechanism.__init__)


def test_delaymechanism_constructor_args():
    sig = inspect.signature(DelayMechanism.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::statement::rejectmechanism_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::RejectMechanism)


def test_vhdl::statement::rejectmechanism_constructor_exists():
    assert callable(vhdl::statement::RejectMechanism.__init__)


def test_vhdl::statement::rejectmechanism_constructor_args():
    sig = inspect.signature(vhdl::statement::RejectMechanism.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::statement::transportmechanism_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::TransportMechanism)


def test_vhdl::statement::transportmechanism_constructor_exists():
    assert callable(vhdl::statement::TransportMechanism.__init__)


def test_vhdl::statement::transportmechanism_constructor_args():
    sig = inspect.signature(vhdl::statement::TransportMechanism.__init__)
    params = list(sig.parameters.keys())



def test_conditionalsignalassignmentstatement_is_not_abstract():
    assert not inspect.isabstract(ConditionalSignalAssignmentStatement)


def test_conditionalsignalassignmentstatement_constructor_exists():
    assert callable(ConditionalSignalAssignmentStatement.__init__)


def test_conditionalsignalassignmentstatement_constructor_args():
    sig = inspect.signature(ConditionalSignalAssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::statement::selectedsignalassignmentstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::SelectedSignalAssignmentStatement)


def test_vhdl::statement::selectedsignalassignmentstatement_constructor_exists():
    assert callable(vhdl::statement::SelectedSignalAssignmentStatement.__init__)


def test_vhdl::statement::selectedsignalassignmentstatement_constructor_args():
    sig = inspect.signature(vhdl::statement::SelectedSignalAssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_signalassignmentstatement_is_not_abstract():
    assert not inspect.isabstract(SignalAssignmentStatement)


def test_signalassignmentstatement_constructor_exists():
    assert callable(SignalAssignmentStatement.__init__)


def test_signalassignmentstatement_constructor_args():
    sig = inspect.signature(SignalAssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::statement::sequentialsignalassignmentstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::SequentialSignalAssignmentStatement)


def test_vhdl::statement::sequentialsignalassignmentstatement_constructor_exists():
    assert callable(vhdl::statement::SequentialSignalAssignmentStatement.__init__)


def test_vhdl::statement::sequentialsignalassignmentstatement_constructor_args():
    sig = inspect.signature(vhdl::statement::SequentialSignalAssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::statement::conditionalsignalassignmentstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::ConditionalSignalAssignmentStatement)


def test_vhdl::statement::conditionalsignalassignmentstatement_constructor_exists():
    assert callable(vhdl::statement::ConditionalSignalAssignmentStatement.__init__)


def test_vhdl::statement::conditionalsignalassignmentstatement_constructor_args():
    sig = inspect.signature(vhdl::statement::ConditionalSignalAssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(ExpressionStatement)


def test_expressionstatement_constructor_exists():
    assert callable(ExpressionStatement.__init__)


def test_expressionstatement_constructor_args():
    sig = inspect.signature(ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::statement::returnstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::ReturnStatement)


def test_vhdl::statement::returnstatement_constructor_exists():
    assert callable(vhdl::statement::ReturnStatement.__init__)


def test_vhdl::statement::returnstatement_constructor_args():
    sig = inspect.signature(vhdl::statement::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_subprogramdeclaration_is_not_abstract():
    assert not inspect.isabstract(SubprogramDeclaration)


def test_subprogramdeclaration_constructor_exists():
    assert callable(SubprogramDeclaration.__init__)


def test_subprogramdeclaration_constructor_args():
    sig = inspect.signature(SubprogramDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::declaration::proceduredeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl::declaration::ProcedureDeclaration)


def test_vhdl::declaration::proceduredeclaration_constructor_exists():
    assert callable(vhdl::declaration::ProcedureDeclaration.__init__)


def test_vhdl::declaration::proceduredeclaration_constructor_args():
    sig = inspect.signature(vhdl::declaration::ProcedureDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::callreference_is_not_abstract():
    assert not inspect.isabstract(vhdl::CallReference)


def test_vhdl::callreference_constructor_exists():
    assert callable(vhdl::CallReference.__init__)


def test_vhdl::callreference_constructor_args():
    sig = inspect.signature(vhdl::CallReference.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::vhdlobject_is_not_abstract():
    assert not inspect.isabstract(vhdl::VhdlObject)


def test_vhdl::vhdlobject_constructor_exists():
    assert callable(vhdl::VhdlObject.__init__)


def test_vhdl::vhdlobject_constructor_args():
    sig = inspect.signature(vhdl::VhdlObject.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_vhdl::vhdlobject_has_id():
    assert hasattr(vhdl::VhdlObject, "id")
    descriptor = None
    for klass in vhdl::VhdlObject.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::multiname_is_not_abstract():
    assert not inspect.isabstract(vhdl::MultiName)


def test_vhdl::multiname_constructor_exists():
    assert callable(vhdl::MultiName.__init__)


def test_vhdl::multiname_constructor_args():
    sig = inspect.signature(vhdl::MultiName.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::multinamed_is_not_abstract():
    assert not inspect.isabstract(vhdl::MultiNamed)


def test_vhdl::multinamed_constructor_exists():
    assert callable(vhdl::MultiNamed.__init__)


def test_vhdl::multinamed_constructor_args():
    sig = inspect.signature(vhdl::MultiNamed.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::named_is_not_abstract():
    assert not inspect.isabstract(vhdl::Named)


def test_vhdl::named_constructor_exists():
    assert callable(vhdl::Named.__init__)


def test_vhdl::named_constructor_args():
    sig = inspect.signature(vhdl::Named.__init__)
    params = list(sig.parameters.keys())



def test_callreference_is_not_abstract():
    assert not inspect.isabstract(CallReference)


def test_callreference_constructor_exists():
    assert callable(CallReference.__init__)


def test_callreference_constructor_args():
    sig = inspect.signature(CallReference.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::callresolvedreference_is_not_abstract():
    assert not inspect.isabstract(vhdl::CallResolvedReference)


def test_vhdl::callresolvedreference_constructor_exists():
    assert callable(vhdl::CallResolvedReference.__init__)


def test_vhdl::callresolvedreference_constructor_args():
    sig = inspect.signature(vhdl::CallResolvedReference.__init__)
    params = list(sig.parameters.keys())



def test_configuration::configurationreference_is_not_abstract():
    assert not inspect.isabstract(configuration::ConfigurationReference)


def test_configuration::configurationreference_constructor_exists():
    assert callable(configuration::ConfigurationReference.__init__)


def test_configuration::configurationreference_constructor_args():
    sig = inspect.signature(configuration::ConfigurationReference.__init__)
    params = list(sig.parameters.keys())



def test_componentreference_is_not_abstract():
    assert not inspect.isabstract(ComponentReference)


def test_componentreference_constructor_exists():
    assert callable(ComponentReference.__init__)


def test_componentreference_constructor_args():
    sig = inspect.signature(ComponentReference.__init__)
    params = list(sig.parameters.keys())



def test_packagereference_is_not_abstract():
    assert not inspect.isabstract(PackageReference)


def test_packagereference_constructor_exists():
    assert callable(PackageReference.__init__)


def test_packagereference_constructor_args():
    sig = inspect.signature(PackageReference.__init__)
    params = list(sig.parameters.keys())



def test_entityreference_is_not_abstract():
    assert not inspect.isabstract(EntityReference)


def test_entityreference_constructor_exists():
    assert callable(EntityReference.__init__)


def test_entityreference_constructor_args():
    sig = inspect.signature(EntityReference.__init__)
    params = list(sig.parameters.keys())



def test_nature::naturereference_is_not_abstract():
    assert not inspect.isabstract(nature::NatureReference)


def test_nature::naturereference_constructor_exists():
    assert callable(nature::NatureReference.__init__)


def test_nature::naturereference_constructor_args():
    sig = inspect.signature(nature::NatureReference.__init__)
    params = list(sig.parameters.keys())



def test_type::typereference_is_not_abstract():
    assert not inspect.isabstract(type::TypeReference)


def test_type::typereference_constructor_exists():
    assert callable(type::TypeReference.__init__)


def test_type::typereference_constructor_args():
    sig = inspect.signature(type::TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_multiname_is_not_abstract():
    assert not inspect.isabstract(MultiName)


def test_multiname_constructor_exists():
    assert callable(MultiName.__init__)


def test_multiname_constructor_args():
    sig = inspect.signature(MultiName.__init__)
    params = list(sig.parameters.keys())



def test_declaration::declaration_is_not_abstract():
    assert not inspect.isabstract(declaration::Declaration)


def test_declaration::declaration_constructor_exists():
    assert callable(declaration::Declaration.__init__)


def test_declaration::declaration_constructor_args():
    sig = inspect.signature(declaration::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::declaration::disconnectionspecification_is_not_abstract():
    assert not inspect.isabstract(vhdl::declaration::DisconnectionSpecification)


def test_vhdl::declaration::disconnectionspecification_constructor_exists():
    assert callable(vhdl::declaration::DisconnectionSpecification.__init__)


def test_vhdl::declaration::disconnectionspecification_constructor_args():
    sig = inspect.signature(vhdl::declaration::DisconnectionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::declaration::terminaldeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl::declaration::TerminalDeclaration)


def test_vhdl::declaration::terminaldeclaration_constructor_exists():
    assert callable(vhdl::declaration::TerminalDeclaration.__init__)


def test_vhdl::declaration::terminaldeclaration_constructor_args():
    sig = inspect.signature(vhdl::declaration::TerminalDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::declaration::valuedeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl::declaration::ValueDeclaration)


def test_vhdl::declaration::valuedeclaration_constructor_exists():
    assert callable(vhdl::declaration::ValueDeclaration.__init__)


def test_vhdl::declaration::valuedeclaration_constructor_args():
    sig = inspect.signature(vhdl::declaration::ValueDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::declaration::filedeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl::declaration::FileDeclaration)


def test_vhdl::declaration::filedeclaration_constructor_exists():
    assert callable(vhdl::declaration::FileDeclaration.__init__)


def test_vhdl::declaration::filedeclaration_constructor_args():
    sig = inspect.signature(vhdl::declaration::FileDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::declaration::limitdeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl::declaration::LimitDeclaration)


def test_vhdl::declaration::limitdeclaration_constructor_exists():
    assert callable(vhdl::declaration::LimitDeclaration.__init__)


def test_vhdl::declaration::limitdeclaration_constructor_args():
    sig = inspect.signature(vhdl::declaration::LimitDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_typereference_is_not_abstract():
    assert not inspect.isabstract(TypeReference)


def test_typereference_constructor_exists():
    assert callable(TypeReference.__init__)


def test_typereference_constructor_args():
    sig = inspect.signature(TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::packagereference_is_not_abstract():
    assert not inspect.isabstract(vhdl::PackageReference)


def test_vhdl::packagereference_constructor_exists():
    assert callable(vhdl::PackageReference.__init__)


def test_vhdl::packagereference_constructor_args():
    sig = inspect.signature(vhdl::PackageReference.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::expression::unaffectedexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::UnaffectedExpression)


def test_vhdl::expression::unaffectedexpression_constructor_exists():
    assert callable(vhdl::expression::UnaffectedExpression.__init__)


def test_vhdl::expression::unaffectedexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::UnaffectedExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::expression::associationexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::AssociationExpression)


def test_vhdl::expression::associationexpression_constructor_exists():
    assert callable(vhdl::expression::AssociationExpression.__init__)


def test_vhdl::expression::associationexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::AssociationExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::expression::valueexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::ValueExpression)


def test_vhdl::expression::valueexpression_constructor_exists():
    assert callable(vhdl::expression::ValueExpression.__init__)


def test_vhdl::expression::valueexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::ValueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vhdl::expression::valueexpression_has_value():
    assert hasattr(vhdl::expression::ValueExpression, "value")
    descriptor = None
    for klass in vhdl::expression::ValueExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::expression::waveformexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::WaveformExpression)


def test_vhdl::expression::waveformexpression_constructor_exists():
    assert callable(vhdl::expression::WaveformExpression.__init__)


def test_vhdl::expression::waveformexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::WaveformExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::expression::multiexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::MultiExpression)


def test_vhdl::expression::multiexpression_constructor_exists():
    assert callable(vhdl::expression::MultiExpression.__init__)


def test_vhdl::expression::multiexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::MultiExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::expression::nullexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::NullExpression)


def test_vhdl::expression::nullexpression_constructor_exists():
    assert callable(vhdl::expression::NullExpression.__init__)


def test_vhdl::expression::nullexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::NullExpression.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::declaration::configurationspecification_is_not_abstract():
    assert not inspect.isabstract(vhdl::declaration::ConfigurationSpecification)


def test_vhdl::declaration::configurationspecification_constructor_exists():
    assert callable(vhdl::declaration::ConfigurationSpecification.__init__)


def test_vhdl::declaration::configurationspecification_constructor_args():
    sig = inspect.signature(vhdl::declaration::ConfigurationSpecification.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::declaration::quantitydeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl::declaration::QuantityDeclaration)


def test_vhdl::declaration::quantitydeclaration_constructor_exists():
    assert callable(vhdl::declaration::QuantityDeclaration.__init__)


def test_vhdl::declaration::quantitydeclaration_constructor_args():
    sig = inspect.signature(vhdl::declaration::QuantityDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::declaration::useclausedeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl::declaration::UseClauseDeclaration)


def test_vhdl::declaration::useclausedeclaration_constructor_exists():
    assert callable(vhdl::declaration::UseClauseDeclaration.__init__)


def test_vhdl::declaration::useclausedeclaration_constructor_args():
    sig = inspect.signature(vhdl::declaration::UseClauseDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::name_is_not_abstract():
    assert not inspect.isabstract(vhdl::Name)


def test_vhdl::name_constructor_exists():
    assert callable(vhdl::Name.__init__)


def test_vhdl::name_constructor_args():
    sig = inspect.signature(vhdl::Name.__init__)
    params = list(sig.parameters.keys())



def test_vhdlobject_is_not_abstract():
    assert not inspect.isabstract(VhdlObject)


def test_vhdlobject_constructor_exists():
    assert callable(VhdlObject.__init__)


def test_vhdlobject_constructor_args():
    sig = inspect.signature(VhdlObject.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::declaration::declaration_is_not_abstract():
    assert not inspect.isabstract(vhdl::declaration::Declaration)


def test_vhdl::declaration::declaration_constructor_exists():
    assert callable(vhdl::declaration::Declaration.__init__)


def test_vhdl::declaration::declaration_constructor_args():
    sig = inspect.signature(vhdl::declaration::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::statement::iterationscheme_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::IterationScheme)


def test_vhdl::statement::iterationscheme_constructor_exists():
    assert callable(vhdl::statement::IterationScheme.__init__)


def test_vhdl::statement::iterationscheme_constructor_args():
    sig = inspect.signature(vhdl::statement::IterationScheme.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::statement::breakstatementitem_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::BreakStatementItem)


def test_vhdl::statement::breakstatementitem_constructor_exists():
    assert callable(vhdl::statement::BreakStatementItem.__init__)


def test_vhdl::statement::breakstatementitem_constructor_args():
    sig = inspect.signature(vhdl::statement::BreakStatementItem.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::statement::statement_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::Statement)


def test_vhdl::statement::statement_constructor_exists():
    assert callable(vhdl::statement::Statement.__init__)


def test_vhdl::statement::statement_constructor_args():
    sig = inspect.signature(vhdl::statement::Statement.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_vhdl::statement::statement_has_label():
    assert hasattr(vhdl::statement::Statement, "label")
    descriptor = None
    for klass in vhdl::statement::Statement.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::statement::generationscheme_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::GenerationScheme)


def test_vhdl::statement::generationscheme_constructor_exists():
    assert callable(vhdl::statement::GenerationScheme.__init__)


def test_vhdl::statement::generationscheme_constructor_args():
    sig = inspect.signature(vhdl::statement::GenerationScheme.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::declaration::subprogrambody_is_not_abstract():
    assert not inspect.isabstract(vhdl::declaration::SubprogramBody)


def test_vhdl::declaration::subprogrambody_constructor_exists():
    assert callable(vhdl::declaration::SubprogramBody.__init__)


def test_vhdl::declaration::subprogrambody_constructor_args():
    sig = inspect.signature(vhdl::declaration::SubprogramBody.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::ams::sourceaspect_is_not_abstract():
    assert not inspect.isabstract(vhdl::ams::SourceAspect)


def test_vhdl::ams::sourceaspect_constructor_exists():
    assert callable(vhdl::ams::SourceAspect.__init__)


def test_vhdl::ams::sourceaspect_constructor_args():
    sig = inspect.signature(vhdl::ams::SourceAspect.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::signature_is_not_abstract():
    assert not inspect.isabstract(vhdl::Signature)


def test_vhdl::signature_constructor_exists():
    assert callable(vhdl::Signature.__init__)


def test_vhdl::signature_constructor_args():
    sig = inspect.signature(vhdl::Signature.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::type::recordtypeelement_is_not_abstract():
    assert not inspect.isabstract(vhdl::type::RecordTypeElement)


def test_vhdl::type::recordtypeelement_constructor_exists():
    assert callable(vhdl::type::RecordTypeElement.__init__)


def test_vhdl::type::recordtypeelement_constructor_args():
    sig = inspect.signature(vhdl::type::RecordTypeElement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::configuration::configurationitem_is_not_abstract():
    assert not inspect.isabstract(vhdl::configuration::ConfigurationItem)


def test_vhdl::configuration::configurationitem_constructor_exists():
    assert callable(vhdl::configuration::ConfigurationItem.__init__)


def test_vhdl::configuration::configurationitem_constructor_args():
    sig = inspect.signature(vhdl::configuration::ConfigurationItem.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::entityresolvedreference_is_not_abstract():
    assert not inspect.isabstract(vhdl::EntityResolvedReference)


def test_vhdl::entityresolvedreference_constructor_exists():
    assert callable(vhdl::EntityResolvedReference.__init__)


def test_vhdl::entityresolvedreference_constructor_args():
    sig = inspect.signature(vhdl::EntityResolvedReference.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::generics_is_not_abstract():
    assert not inspect.isabstract(vhdl::Generics)


def test_vhdl::generics_constructor_exists():
    assert callable(vhdl::Generics.__init__)


def test_vhdl::generics_constructor_args():
    sig = inspect.signature(vhdl::Generics.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::portmaps_is_not_abstract():
    assert not inspect.isabstract(vhdl::PortMaps)


def test_vhdl::portmaps_constructor_exists():
    assert callable(vhdl::PortMaps.__init__)


def test_vhdl::portmaps_constructor_args():
    sig = inspect.signature(vhdl::PortMaps.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::type::typedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl::type::TypeDefinition)


def test_vhdl::type::typedefinition_constructor_exists():
    assert callable(vhdl::type::TypeDefinition.__init__)


def test_vhdl::type::typedefinition_constructor_args():
    sig = inspect.signature(vhdl::type::TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::model_is_not_abstract():
    assert not inspect.isabstract(vhdl::Model)


def test_vhdl::model_constructor_exists():
    assert callable(vhdl::Model.__init__)


def test_vhdl::model_constructor_args():
    sig = inspect.signature(vhdl::Model.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::statement::ifstatementtest_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::IfStatementTest)


def test_vhdl::statement::ifstatementtest_constructor_exists():
    assert callable(vhdl::statement::IfStatementTest.__init__)


def test_vhdl::statement::ifstatementtest_constructor_args():
    sig = inspect.signature(vhdl::statement::IfStatementTest.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::packageresolvedreference_is_not_abstract():
    assert not inspect.isabstract(vhdl::PackageResolvedReference)


def test_vhdl::packageresolvedreference_constructor_exists():
    assert callable(vhdl::PackageResolvedReference.__init__)


def test_vhdl::packageresolvedreference_constructor_args():
    sig = inspect.signature(vhdl::PackageResolvedReference.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::namelist_is_not_abstract():
    assert not inspect.isabstract(vhdl::NameList)


def test_vhdl::namelist_constructor_exists():
    assert callable(vhdl::NameList.__init__)


def test_vhdl::namelist_constructor_args():
    sig = inspect.signature(vhdl::NameList.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::componentresolvedreference_is_not_abstract():
    assert not inspect.isabstract(vhdl::ComponentResolvedReference)


def test_vhdl::componentresolvedreference_constructor_exists():
    assert callable(vhdl::ComponentResolvedReference.__init__)


def test_vhdl::componentresolvedreference_constructor_args():
    sig = inspect.signature(vhdl::ComponentResolvedReference.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::module_is_not_abstract():
    assert not inspect.isabstract(vhdl::Module)


def test_vhdl::module_constructor_exists():
    assert callable(vhdl::Module.__init__)


def test_vhdl::module_constructor_args():
    sig = inspect.signature(vhdl::Module.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::statement::casealternative_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::CaseAlternative)


def test_vhdl::statement::casealternative_constructor_exists():
    assert callable(vhdl::statement::CaseAlternative.__init__)


def test_vhdl::statement::casealternative_constructor_args():
    sig = inspect.signature(vhdl::statement::CaseAlternative.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::ams::quantityaspect_is_not_abstract():
    assert not inspect.isabstract(vhdl::ams::QuantityAspect)


def test_vhdl::ams::quantityaspect_constructor_exists():
    assert callable(vhdl::ams::QuantityAspect.__init__)


def test_vhdl::ams::quantityaspect_constructor_args():
    sig = inspect.signature(vhdl::ams::QuantityAspect.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::genericmaps_is_not_abstract():
    assert not inspect.isabstract(vhdl::GenericMaps)


def test_vhdl::genericmaps_constructor_exists():
    assert callable(vhdl::GenericMaps.__init__)


def test_vhdl::genericmaps_constructor_args():
    sig = inspect.signature(vhdl::GenericMaps.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::nature::recordnatureelement_is_not_abstract():
    assert not inspect.isabstract(vhdl::nature::RecordNatureElement)


def test_vhdl::nature::recordnatureelement_constructor_exists():
    assert callable(vhdl::nature::RecordNatureElement.__init__)


def test_vhdl::nature::recordnatureelement_constructor_args():
    sig = inspect.signature(vhdl::nature::RecordNatureElement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::configuration::configurationresolvedreference_is_not_abstract():
    assert not inspect.isabstract(vhdl::configuration::ConfigurationResolvedReference)


def test_vhdl::configuration::configurationresolvedreference_constructor_exists():
    assert callable(vhdl::configuration::ConfigurationResolvedReference.__init__)


def test_vhdl::configuration::configurationresolvedreference_constructor_args():
    sig = inspect.signature(vhdl::configuration::ConfigurationResolvedReference.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::ports_is_not_abstract():
    assert not inspect.isabstract(vhdl::Ports)


def test_vhdl::ports_constructor_exists():
    assert callable(vhdl::Ports.__init__)


def test_vhdl::ports_constructor_args():
    sig = inspect.signature(vhdl::Ports.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::nature::naturedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl::nature::NatureDefinition)


def test_vhdl::nature::naturedefinition_constructor_exists():
    assert callable(vhdl::nature::NatureDefinition.__init__)


def test_vhdl::nature::naturedefinition_constructor_args():
    sig = inspect.signature(vhdl::nature::NatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::designunit_is_not_abstract():
    assert not inspect.isabstract(vhdl::DesignUnit)


def test_vhdl::designunit_constructor_exists():
    assert callable(vhdl::DesignUnit.__init__)


def test_vhdl::designunit_constructor_args():
    sig = inspect.signature(vhdl::DesignUnit.__init__)
    params = list(sig.parameters.keys())
    assert "library" in params, "Missing parameter 'library'"

def test_vhdl::designunit_has_library():
    assert hasattr(vhdl::DesignUnit, "library")
    descriptor = None
    for klass in vhdl::DesignUnit.__mro__:
        if "library" in klass.__dict__:
            descriptor = klass.__dict__["library"]
            break
    assert isinstance(descriptor, property)



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::statement::exitstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::ExitStatement)


def test_vhdl::statement::exitstatement_constructor_exists():
    assert callable(vhdl::statement::ExitStatement.__init__)


def test_vhdl::statement::exitstatement_constructor_args():
    sig = inspect.signature(vhdl::statement::ExitStatement.__init__)
    params = list(sig.parameters.keys())
    assert "exit" in params, "Missing parameter 'exit'"

def test_vhdl::statement::exitstatement_has_exit():
    assert hasattr(vhdl::statement::ExitStatement, "exit")
    descriptor = None
    for klass in vhdl::statement::ExitStatement.__mro__:
        if "exit" in klass.__dict__:
            descriptor = klass.__dict__["exit"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::statement::simultaneousproceduralstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::SimultaneousProceduralStatement)


def test_vhdl::statement::simultaneousproceduralstatement_constructor_exists():
    assert callable(vhdl::statement::SimultaneousProceduralStatement.__init__)


def test_vhdl::statement::simultaneousproceduralstatement_constructor_args():
    sig = inspect.signature(vhdl::statement::SimultaneousProceduralStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::statement::instantiationstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::InstantiationStatement)


def test_vhdl::statement::instantiationstatement_constructor_exists():
    assert callable(vhdl::statement::InstantiationStatement.__init__)


def test_vhdl::statement::instantiationstatement_constructor_args():
    sig = inspect.signature(vhdl::statement::InstantiationStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::statement::waitstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::WaitStatement)


def test_vhdl::statement::waitstatement_constructor_exists():
    assert callable(vhdl::statement::WaitStatement.__init__)


def test_vhdl::statement::waitstatement_constructor_args():
    sig = inspect.signature(vhdl::statement::WaitStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::statement::blockstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::BlockStatement)


def test_vhdl::statement::blockstatement_constructor_exists():
    assert callable(vhdl::statement::BlockStatement.__init__)


def test_vhdl::statement::blockstatement_constructor_args():
    sig = inspect.signature(vhdl::statement::BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::statement::nextstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::NextStatement)


def test_vhdl::statement::nextstatement_constructor_exists():
    assert callable(vhdl::statement::NextStatement.__init__)


def test_vhdl::statement::nextstatement_constructor_args():
    sig = inspect.signature(vhdl::statement::NextStatement.__init__)
    params = list(sig.parameters.keys())
    assert "next" in params, "Missing parameter 'next'"

def test_vhdl::statement::nextstatement_has_next():
    assert hasattr(vhdl::statement::NextStatement, "next")
    descriptor = None
    for klass in vhdl::statement::NextStatement.__mro__:
        if "next" in klass.__dict__:
            descriptor = klass.__dict__["next"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::statement::processstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::ProcessStatement)


def test_vhdl::statement::processstatement_constructor_exists():
    assert callable(vhdl::statement::ProcessStatement.__init__)


def test_vhdl::statement::processstatement_constructor_args():
    sig = inspect.signature(vhdl::statement::ProcessStatement.__init__)
    params = list(sig.parameters.keys())
    assert "postponed" in params, "Missing parameter 'postponed'"

def test_vhdl::statement::processstatement_has_postponed():
    assert hasattr(vhdl::statement::ProcessStatement, "postponed")
    descriptor = None
    for klass in vhdl::statement::ProcessStatement.__mro__:
        if "postponed" in klass.__dict__:
            descriptor = klass.__dict__["postponed"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::statement::loopstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::LoopStatement)


def test_vhdl::statement::loopstatement_constructor_exists():
    assert callable(vhdl::statement::LoopStatement.__init__)


def test_vhdl::statement::loopstatement_constructor_args():
    sig = inspect.signature(vhdl::statement::LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::statement::procedurecallstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::ProcedureCallStatement)


def test_vhdl::statement::procedurecallstatement_constructor_exists():
    assert callable(vhdl::statement::ProcedureCallStatement.__init__)


def test_vhdl::statement::procedurecallstatement_constructor_args():
    sig = inspect.signature(vhdl::statement::ProcedureCallStatement.__init__)
    params = list(sig.parameters.keys())
    assert "postponed" in params, "Missing parameter 'postponed'"

def test_vhdl::statement::procedurecallstatement_has_postponed():
    assert hasattr(vhdl::statement::ProcedureCallStatement, "postponed")
    descriptor = None
    for klass in vhdl::statement::ProcedureCallStatement.__mro__:
        if "postponed" in klass.__dict__:
            descriptor = klass.__dict__["postponed"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::statement::reportstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::ReportStatement)


def test_vhdl::statement::reportstatement_constructor_exists():
    assert callable(vhdl::statement::ReportStatement.__init__)


def test_vhdl::statement::reportstatement_constructor_args():
    sig = inspect.signature(vhdl::statement::ReportStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::statement::breakstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::BreakStatement)


def test_vhdl::statement::breakstatement_constructor_exists():
    assert callable(vhdl::statement::BreakStatement.__init__)


def test_vhdl::statement::breakstatement_constructor_args():
    sig = inspect.signature(vhdl::statement::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::statement::assertionstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::AssertionStatement)


def test_vhdl::statement::assertionstatement_constructor_exists():
    assert callable(vhdl::statement::AssertionStatement.__init__)


def test_vhdl::statement::assertionstatement_constructor_args():
    sig = inspect.signature(vhdl::statement::AssertionStatement.__init__)
    params = list(sig.parameters.keys())
    assert "postponed" in params, "Missing parameter 'postponed'"

def test_vhdl::statement::assertionstatement_has_postponed():
    assert hasattr(vhdl::statement::AssertionStatement, "postponed")
    descriptor = None
    for klass in vhdl::statement::AssertionStatement.__mro__:
        if "postponed" in klass.__dict__:
            descriptor = klass.__dict__["postponed"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::statement::ifstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::IfStatement)


def test_vhdl::statement::ifstatement_constructor_exists():
    assert callable(vhdl::statement::IfStatement.__init__)


def test_vhdl::statement::ifstatement_constructor_args():
    sig = inspect.signature(vhdl::statement::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::statement::variableassignmentstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::VariableAssignmentStatement)


def test_vhdl::statement::variableassignmentstatement_constructor_exists():
    assert callable(vhdl::statement::VariableAssignmentStatement.__init__)


def test_vhdl::statement::variableassignmentstatement_constructor_args():
    sig = inspect.signature(vhdl::statement::VariableAssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::statement::signalassignmentstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::SignalAssignmentStatement)


def test_vhdl::statement::signalassignmentstatement_constructor_exists():
    assert callable(vhdl::statement::SignalAssignmentStatement.__init__)


def test_vhdl::statement::signalassignmentstatement_constructor_args():
    sig = inspect.signature(vhdl::statement::SignalAssignmentStatement.__init__)
    params = list(sig.parameters.keys())
    assert "postponed" in params, "Missing parameter 'postponed'"
    assert "guarded" in params, "Missing parameter 'guarded'"

def test_vhdl::statement::signalassignmentstatement_has_postponed():
    assert hasattr(vhdl::statement::SignalAssignmentStatement, "postponed")
    descriptor = None
    for klass in vhdl::statement::SignalAssignmentStatement.__mro__:
        if "postponed" in klass.__dict__:
            descriptor = klass.__dict__["postponed"]
            break
    assert isinstance(descriptor, property)

def test_vhdl::statement::signalassignmentstatement_has_guarded():
    assert hasattr(vhdl::statement::SignalAssignmentStatement, "guarded")
    descriptor = None
    for klass in vhdl::statement::SignalAssignmentStatement.__mro__:
        if "guarded" in klass.__dict__:
            descriptor = klass.__dict__["guarded"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::statement::casestatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::CaseStatement)


def test_vhdl::statement::casestatement_constructor_exists():
    assert callable(vhdl::statement::CaseStatement.__init__)


def test_vhdl::statement::casestatement_constructor_args():
    sig = inspect.signature(vhdl::statement::CaseStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::statement::generatestatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::GenerateStatement)


def test_vhdl::statement::generatestatement_constructor_exists():
    assert callable(vhdl::statement::GenerateStatement.__init__)


def test_vhdl::statement::generatestatement_constructor_args():
    sig = inspect.signature(vhdl::statement::GenerateStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::statement::simplesimultaneousstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::SimpleSimultaneousStatement)


def test_vhdl::statement::simplesimultaneousstatement_constructor_exists():
    assert callable(vhdl::statement::SimpleSimultaneousStatement.__init__)


def test_vhdl::statement::simplesimultaneousstatement_constructor_args():
    sig = inspect.signature(vhdl::statement::SimpleSimultaneousStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::entityreference_is_not_abstract():
    assert not inspect.isabstract(vhdl::EntityReference)


def test_vhdl::entityreference_constructor_exists():
    assert callable(vhdl::EntityReference.__init__)


def test_vhdl::entityreference_constructor_args():
    sig = inspect.signature(vhdl::EntityReference.__init__)
    params = list(sig.parameters.keys())



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::declaration::attributespecification_is_not_abstract():
    assert not inspect.isabstract(vhdl::declaration::AttributeSpecification)


def test_vhdl::declaration::attributespecification_constructor_exists():
    assert callable(vhdl::declaration::AttributeSpecification.__init__)


def test_vhdl::declaration::attributespecification_constructor_args():
    sig = inspect.signature(vhdl::declaration::AttributeSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"

def test_vhdl::declaration::attributespecification_has_class_():
    assert hasattr(vhdl::declaration::AttributeSpecification, "class_")
    descriptor = None
    for klass in vhdl::declaration::AttributeSpecification.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::declaration::groupdeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl::declaration::GroupDeclaration)


def test_vhdl::declaration::groupdeclaration_constructor_exists():
    assert callable(vhdl::declaration::GroupDeclaration.__init__)


def test_vhdl::declaration::groupdeclaration_constructor_args():
    sig = inspect.signature(vhdl::declaration::GroupDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::declaration::subnaturedeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl::declaration::SubnatureDeclaration)


def test_vhdl::declaration::subnaturedeclaration_constructor_exists():
    assert callable(vhdl::declaration::SubnatureDeclaration.__init__)


def test_vhdl::declaration::subnaturedeclaration_constructor_args():
    sig = inspect.signature(vhdl::declaration::SubnatureDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::declaration::naturedeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl::declaration::NatureDeclaration)


def test_vhdl::declaration::naturedeclaration_constructor_exists():
    assert callable(vhdl::declaration::NatureDeclaration.__init__)


def test_vhdl::declaration::naturedeclaration_constructor_args():
    sig = inspect.signature(vhdl::declaration::NatureDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::declaration::subprogramdeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl::declaration::SubprogramDeclaration)


def test_vhdl::declaration::subprogramdeclaration_constructor_exists():
    assert callable(vhdl::declaration::SubprogramDeclaration.__init__)


def test_vhdl::declaration::subprogramdeclaration_constructor_args():
    sig = inspect.signature(vhdl::declaration::SubprogramDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::component_is_not_abstract():
    assert not inspect.isabstract(vhdl::Component)


def test_vhdl::component_constructor_exists():
    assert callable(vhdl::Component.__init__)


def test_vhdl::component_constructor_args():
    sig = inspect.signature(vhdl::Component.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::declaration::attributedeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl::declaration::AttributeDeclaration)


def test_vhdl::declaration::attributedeclaration_constructor_exists():
    assert callable(vhdl::declaration::AttributeDeclaration.__init__)


def test_vhdl::declaration::attributedeclaration_constructor_args():
    sig = inspect.signature(vhdl::declaration::AttributeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::configuration::blockconfiguration_is_not_abstract():
    assert not inspect.isabstract(vhdl::configuration::BlockConfiguration)


def test_vhdl::configuration::blockconfiguration_constructor_exists():
    assert callable(vhdl::configuration::BlockConfiguration.__init__)


def test_vhdl::configuration::blockconfiguration_constructor_args():
    sig = inspect.signature(vhdl::configuration::BlockConfiguration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::declaration::subtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl::declaration::SubtypeDeclaration)


def test_vhdl::declaration::subtypedeclaration_constructor_exists():
    assert callable(vhdl::declaration::SubtypeDeclaration.__init__)


def test_vhdl::declaration::subtypedeclaration_constructor_args():
    sig = inspect.signature(vhdl::declaration::SubtypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::declaration::aliasdeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl::declaration::AliasDeclaration)


def test_vhdl::declaration::aliasdeclaration_constructor_exists():
    assert callable(vhdl::declaration::AliasDeclaration.__init__)


def test_vhdl::declaration::aliasdeclaration_constructor_args():
    sig = inspect.signature(vhdl::declaration::AliasDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::declaration::grouptemplatedeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl::declaration::GroupTemplateDeclaration)


def test_vhdl::declaration::grouptemplatedeclaration_constructor_exists():
    assert callable(vhdl::declaration::GroupTemplateDeclaration.__init__)


def test_vhdl::declaration::grouptemplatedeclaration_constructor_args():
    sig = inspect.signature(vhdl::declaration::GroupTemplateDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "entry" in params, "Missing parameter 'entry'"

def test_vhdl::declaration::grouptemplatedeclaration_has_entry():
    assert hasattr(vhdl::declaration::GroupTemplateDeclaration, "entry")
    descriptor = None
    for klass in vhdl::declaration::GroupTemplateDeclaration.__mro__:
        if "entry" in klass.__dict__:
            descriptor = klass.__dict__["entry"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::declaration::typedeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl::declaration::TypeDeclaration)


def test_vhdl::declaration::typedeclaration_constructor_exists():
    assert callable(vhdl::declaration::TypeDeclaration.__init__)


def test_vhdl::declaration::typedeclaration_constructor_args():
    sig = inspect.signature(vhdl::declaration::TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_module_is_not_abstract():
    assert not inspect.isabstract(Module)


def test_module_constructor_exists():
    assert callable(Module.__init__)


def test_module_constructor_args():
    sig = inspect.signature(Module.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::entity_is_not_abstract():
    assert not inspect.isabstract(vhdl::Entity)


def test_vhdl::entity_constructor_exists():
    assert callable(vhdl::Entity.__init__)


def test_vhdl::entity_constructor_args():
    sig = inspect.signature(vhdl::Entity.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::configuration::configuration_is_not_abstract():
    assert not inspect.isabstract(vhdl::configuration::Configuration)


def test_vhdl::configuration::configuration_constructor_exists():
    assert callable(vhdl::configuration::Configuration.__init__)


def test_vhdl::configuration::configuration_constructor_args():
    sig = inspect.signature(vhdl::configuration::Configuration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::package_is_not_abstract():
    assert not inspect.isabstract(vhdl::Package)


def test_vhdl::package_constructor_exists():
    assert callable(vhdl::Package.__init__)


def test_vhdl::package_constructor_args():
    sig = inspect.signature(vhdl::Package.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::packagebody_is_not_abstract():
    assert not inspect.isabstract(vhdl::PackageBody)


def test_vhdl::packagebody_constructor_exists():
    assert callable(vhdl::PackageBody.__init__)


def test_vhdl::packagebody_constructor_args():
    sig = inspect.signature(vhdl::PackageBody.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::architecture_is_not_abstract():
    assert not inspect.isabstract(vhdl::Architecture)


def test_vhdl::architecture_constructor_exists():
    assert callable(vhdl::Architecture.__init__)


def test_vhdl::architecture_constructor_args():
    sig = inspect.signature(vhdl::Architecture.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::expression::characterexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::CharacterExpression)


def test_vhdl::expression::characterexpression_constructor_exists():
    assert callable(vhdl::expression::CharacterExpression.__init__)


def test_vhdl::expression::characterexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::CharacterExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::expression::stringexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::StringExpression)


def test_vhdl::expression::stringexpression_constructor_exists():
    assert callable(vhdl::expression::StringExpression.__init__)


def test_vhdl::expression::stringexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::StringExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(expression::BinaryExpression)


def test_expression::binaryexpression_constructor_exists():
    assert callable(expression::BinaryExpression.__init__)


def test_expression::binaryexpression_constructor_args():
    sig = inspect.signature(expression::BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::expression::rangeexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::RangeExpression)


def test_vhdl::expression::rangeexpression_constructor_exists():
    assert callable(vhdl::expression::RangeExpression.__init__)


def test_vhdl::expression::rangeexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::RangeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_vhdl::expression::rangeexpression_has_direction():
    assert hasattr(vhdl::expression::RangeExpression, "direction")
    descriptor = None
    for klass in vhdl::expression::RangeExpression.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::expression::othersexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::OthersExpression)


def test_vhdl::expression::othersexpression_constructor_exists():
    assert callable(vhdl::expression::OthersExpression.__init__)


def test_vhdl::expression::othersexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::OthersExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::expression::openexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::OpenExpression)


def test_vhdl::expression::openexpression_constructor_exists():
    assert callable(vhdl::expression::OpenExpression.__init__)


def test_vhdl::expression::openexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::OpenExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::expression::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::UnaryExpression)


def test_vhdl::expression::unaryexpression_constructor_exists():
    assert callable(vhdl::expression::UnaryExpression.__init__)


def test_vhdl::expression::unaryexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_vhdl::expression::unaryexpression_has_operator():
    assert hasattr(vhdl::expression::UnaryExpression, "operator")
    descriptor = None
    for klass in vhdl::expression::UnaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::expression::signexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::SignExpression)


def test_vhdl::expression::signexpression_constructor_exists():
    assert callable(vhdl::expression::SignExpression.__init__)


def test_vhdl::expression::signexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::SignExpression.__init__)
    params = list(sig.parameters.keys())
    assert "sign" in params, "Missing parameter 'sign'"

def test_vhdl::expression::signexpression_has_sign():
    assert hasattr(vhdl::expression::SignExpression, "sign")
    descriptor = None
    for klass in vhdl::expression::SignExpression.__mro__:
        if "sign" in klass.__dict__:
            descriptor = klass.__dict__["sign"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::expression::signatureexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::SignatureExpression)


def test_vhdl::expression::signatureexpression_constructor_exists():
    assert callable(vhdl::expression::SignatureExpression.__init__)


def test_vhdl::expression::signatureexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::SignatureExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::expression::shiftexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::ShiftExpression)


def test_vhdl::expression::shiftexpression_constructor_exists():
    assert callable(vhdl::expression::ShiftExpression.__init__)


def test_vhdl::expression::shiftexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::ShiftExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_vhdl::expression::shiftexpression_has_operator():
    assert hasattr(vhdl::expression::ShiftExpression, "operator")
    descriptor = None
    for klass in vhdl::expression::ShiftExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::expression::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::BinaryExpression)


def test_vhdl::expression::binaryexpression_constructor_exists():
    assert callable(vhdl::expression::BinaryExpression.__init__)


def test_vhdl::expression::binaryexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression::vhdl::name_is_not_abstract():
    assert not inspect.isabstract(expression::vhdl::Name)


def test_expression::vhdl::name_constructor_exists():
    assert callable(expression::vhdl::Name.__init__)


def test_expression::vhdl::name_constructor_args():
    sig = inspect.signature(expression::vhdl::Name.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::expression::nameexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::NameExpression)


def test_vhdl::expression::nameexpression_constructor_exists():
    assert callable(vhdl::expression::NameExpression.__init__)


def test_vhdl::expression::nameexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::NameExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::expression::logicalexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::LogicalExpression)


def test_vhdl::expression::logicalexpression_constructor_exists():
    assert callable(vhdl::expression::LogicalExpression.__init__)


def test_vhdl::expression::logicalexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::LogicalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_vhdl::expression::logicalexpression_has_operator():
    assert hasattr(vhdl::expression::LogicalExpression, "operator")
    descriptor = None
    for klass in vhdl::expression::LogicalExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_naturereference_is_not_abstract():
    assert not inspect.isabstract(NatureReference)


def test_naturereference_constructor_exists():
    assert callable(NatureReference.__init__)


def test_naturereference_constructor_args():
    sig = inspect.signature(NatureReference.__init__)
    params = list(sig.parameters.keys())



def test_expression::indicationexpression_is_not_abstract():
    assert not inspect.isabstract(expression::IndicationExpression)


def test_expression::indicationexpression_constructor_exists():
    assert callable(expression::IndicationExpression.__init__)


def test_expression::indicationexpression_constructor_args():
    sig = inspect.signature(expression::IndicationExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::expression::subnatureindicationexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::SubnatureIndicationExpression)


def test_vhdl::expression::subnatureindicationexpression_constructor_exists():
    assert callable(vhdl::expression::SubnatureIndicationExpression.__init__)


def test_vhdl::expression::subnatureindicationexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::SubnatureIndicationExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::expression::subtypeindicationexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::SubtypeIndicationExpression)


def test_vhdl::expression::subtypeindicationexpression_constructor_exists():
    assert callable(vhdl::expression::SubtypeIndicationExpression.__init__)


def test_vhdl::expression::subtypeindicationexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::SubtypeIndicationExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::expression::indicationexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::IndicationExpression)


def test_vhdl::expression::indicationexpression_constructor_exists():
    assert callable(vhdl::expression::IndicationExpression.__init__)


def test_vhdl::expression::indicationexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::IndicationExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::expression::expression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::Expression)


def test_vhdl::expression::expression_constructor_exists():
    assert callable(vhdl::expression::Expression.__init__)


def test_vhdl::expression::expression_constructor_args():
    sig = inspect.signature(vhdl::expression::Expression.__init__)
    params = list(sig.parameters.keys())



def test_valueexpression_is_not_abstract():
    assert not inspect.isabstract(ValueExpression)


def test_valueexpression_constructor_exists():
    assert callable(ValueExpression.__init__)


def test_valueexpression_constructor_args():
    sig = inspect.signature(ValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::expression::unitvalueexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::UnitValueExpression)


def test_vhdl::expression::unitvalueexpression_constructor_exists():
    assert callable(vhdl::expression::UnitValueExpression.__init__)


def test_vhdl::expression::unitvalueexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::UnitValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::expression::bitstringexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::expression::BitStringExpression)


def test_vhdl::expression::bitstringexpression_constructor_exists():
    assert callable(vhdl::expression::BitStringExpression.__init__)


def test_vhdl::expression::bitstringexpression_constructor_args():
    sig = inspect.signature(vhdl::expression::BitStringExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::statement::forgenerationscheme_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::ForGenerationScheme)


def test_vhdl::statement::forgenerationscheme_constructor_exists():
    assert callable(vhdl::statement::ForGenerationScheme.__init__)


def test_vhdl::statement::forgenerationscheme_constructor_args():
    sig = inspect.signature(vhdl::statement::ForGenerationScheme.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_vhdl::statement::forgenerationscheme_has_variable():
    assert hasattr(vhdl::statement::ForGenerationScheme, "variable")
    descriptor = None
    for klass in vhdl::statement::ForGenerationScheme.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::statement::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::ExpressionStatement)


def test_vhdl::statement::expressionstatement_constructor_exists():
    assert callable(vhdl::statement::ExpressionStatement.__init__)


def test_vhdl::statement::expressionstatement_constructor_args():
    sig = inspect.signature(vhdl::statement::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::statement::delaymechanism_is_not_abstract():
    assert not inspect.isabstract(vhdl::statement::DelayMechanism)


def test_vhdl::statement::delaymechanism_constructor_exists():
    assert callable(vhdl::statement::DelayMechanism.__init__)


def test_vhdl::statement::delaymechanism_constructor_args():
    sig = inspect.signature(vhdl::statement::DelayMechanism.__init__)
    params = list(sig.parameters.keys())



def test_expression::vhdl::signature_is_not_abstract():
    assert not inspect.isabstract(expression::vhdl::Signature)


def test_expression::vhdl::signature_constructor_exists():
    assert callable(expression::vhdl::Signature.__init__)


def test_expression::vhdl::signature_constructor_args():
    sig = inspect.signature(expression::vhdl::Signature.__init__)
    params = list(sig.parameters.keys())

def test_sign_exists():
    # Check that the Enumeration exists
    assert Sign is not None

def test_sign_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Sign]
    expected_literals = [
        "MINUS",
        "PLUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Sign"

def test_shiftoperator_exists():
    # Check that the Enumeration exists
    assert ShiftOperator is not None

def test_shiftoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ShiftOperator]
    expected_literals = [
        "SRL",
        "SLA",
        "ROL",
        "SRA",
        "SLL",
        "ROR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ShiftOperator"

def test_addingoperator_exists():
    # Check that the Enumeration exists
    assert AddingOperator is not None

def test_addingoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AddingOperator]
    expected_literals = [
        "AMPERSAND",
        "PLUS",
        "MINUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AddingOperator"

def test_unaryoperator_exists():
    # Check that the Enumeration exists
    assert UnaryOperator is not None

def test_unaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryOperator]
    expected_literals = [
        "NOT",
        "ABS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryOperator"

def test_rangedirection_exists():
    # Check that the Enumeration exists
    assert RangeDirection is not None

def test_rangedirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RangeDirection]
    expected_literals = [
        "TO",
        "DOWNTO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RangeDirection"

def test_multiplyingoperator_exists():
    # Check that the Enumeration exists
    assert MultiplyingOperator is not None

def test_multiplyingoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MultiplyingOperator]
    expected_literals = [
        "DIV",
        "REM",
        "MOD",
        "MUL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MultiplyingOperator"

def test_entityclass_exists():
    # Check that the Enumeration exists
    assert EntityClass is not None

def test_entityclass_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EntityClass]
    expected_literals = [
        "ENTITY",
        "ARCHITECTURE",
        "SUBTYPE",
        "FUNCTION",
        "UNITS",
        "TYPE",
        "FILE",
        "QUANTITY",
        "NATURE",
        "GROUP",
        "CONSTANT",
        "PACKAGE",
        "CONFIGURATION",
        "SUBNATURE",
        "LITERAL",
        "VARIABLE",
        "COMPONENT",
        "PROCEDURE",
        "LABEL",
        "SIGNAL",
        "TERMINAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EntityClass"

def test_logicaloperator_exists():
    # Check that the Enumeration exists
    assert LogicalOperator is not None

def test_logicaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicalOperator]
    expected_literals = [
        "XNOR",
        "AND",
        "NAND",
        "OR",
        "NOR",
        "XOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LogicalOperator"

def test_signalkind_exists():
    # Check that the Enumeration exists
    assert SignalKind is not None

def test_signalkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SignalKind]
    expected_literals = [
        "BUS",
        "REGISTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SignalKind"

def test_mode_exists():
    # Check that the Enumeration exists
    assert Mode is not None

def test_mode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Mode]
    expected_literals = [
        "BUFFER",
        "LINKAGE",
        "IN",
        "INOUT",
        "OUT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Mode"

def test_purity_exists():
    # Check that the Enumeration exists
    assert Purity is not None

def test_purity_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Purity]
    expected_literals = [
        "IMPURE",
        "PURE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Purity"

def test_relationaloperator_exists():
    # Check that the Enumeration exists
    assert RelationalOperator is not None

def test_relationaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalOperator]
    expected_literals = [
        "GREATERTHAN",
        "LE",
        "LOWERTHAN",
        "EQ",
        "NEQ",
        "GE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationalOperator"


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
Configuration_strategy = st.builds(
    Configuration,
)
vhdl::configuration::ConfigurationReference_strategy = st.builds(
    vhdl::configuration::ConfigurationReference,
)
configuration::vhdl::EntityReference_strategy = st.builds(
    configuration::vhdl::EntityReference,
)
BlockConfiguration_strategy = st.builds(
    BlockConfiguration,
)
configuration::vhdl::PortMaps_strategy = st.builds(
    configuration::vhdl::PortMaps,
)
configuration::vhdl::GenericMaps_strategy = st.builds(
    configuration::vhdl::GenericMaps,
)
configuration::vhdl::MultiName_strategy = st.builds(
    configuration::vhdl::MultiName,
)
ConfigurationItem_strategy = st.builds(
    ConfigurationItem,
)
vhdl::configuration::ComponentConfiguration_strategy = st.builds(
    vhdl::configuration::ComponentConfiguration,
)
configuration::vhdl::Name_strategy = st.builds(
    configuration::vhdl::Name,
)
configuration::ConfigurationItem_strategy = st.builds(
    configuration::ConfigurationItem,
)
nature::CompositeNatureDefinition_strategy = st.builds(
    nature::CompositeNatureDefinition,
)
vhdl::type::TypeReference_strategy = st.builds(
    vhdl::type::TypeReference,
)
vhdl::type::Typed_strategy = st.builds(
    vhdl::type::Typed,
)
vhdl::nature::Natured_strategy = st.builds(
    vhdl::nature::Natured,
)
vhdl::nature::NatureReference_strategy = st.builds(
    vhdl::nature::NatureReference,
)
nature::vhdl::Name_strategy = st.builds(
    nature::vhdl::Name,
)
RecordNatureElement_strategy = st.builds(
    RecordNatureElement,
)
CompositeNatureDefinition_strategy = st.builds(
    CompositeNatureDefinition,
)
vhdl::nature::RecordNatureDefinition_strategy = st.builds(
    vhdl::nature::RecordNatureDefinition,
)
ArrayNatureDefinition_strategy = st.builds(
    ArrayNatureDefinition,
)
vhdl::nature::UnconstrainedArrayNatureDefinition_strategy = st.builds(
    vhdl::nature::UnconstrainedArrayNatureDefinition,
)
vhdl::nature::ConstrainedArrayNatureDefinition_strategy = st.builds(
    vhdl::nature::ConstrainedArrayNatureDefinition,
)
type::vhdl::Name_strategy = st.builds(
    type::vhdl::Name,
)
vhdl::type::PhysicalTypeDefinitionSecondary_strategy = st.builds(
    vhdl::type::PhysicalTypeDefinitionSecondary,
    number=
        safe_text,
    name=
        safe_text
)
PhysicalTypeDefinitionSecondary_strategy = st.builds(
    PhysicalTypeDefinitionSecondary,
)
EnumerationLiteral_strategy = st.builds(
    EnumerationLiteral,
)
vhdl::type::EnumerationLiteral_strategy = st.builds(
    vhdl::type::EnumerationLiteral,
)
ArrayTypeDefinition_strategy = st.builds(
    ArrayTypeDefinition,
)
vhdl::type::UnconstrainedArrayTypeDefinition_strategy = st.builds(
    vhdl::type::UnconstrainedArrayTypeDefinition,
)
vhdl::type::ConstrainedArrayTypeDefinition_strategy = st.builds(
    vhdl::type::ConstrainedArrayTypeDefinition,
)
type::CompositeTypeDefinition_strategy = st.builds(
    type::CompositeTypeDefinition,
)
RecordTypeElement_strategy = st.builds(
    RecordTypeElement,
)
CompositeTypeDefinition_strategy = st.builds(
    CompositeTypeDefinition,
)
vhdl::type::RecordTypeDefinition_strategy = st.builds(
    vhdl::type::RecordTypeDefinition,
)
type::TypeDefinition_strategy = st.builds(
    type::TypeDefinition,
)
TypeDefinition_strategy = st.builds(
    TypeDefinition,
)
vhdl::type::EnumerationTypeDefinition_strategy = st.builds(
    vhdl::type::EnumerationTypeDefinition,
)
vhdl::type::CompositeTypeDefinition_strategy = st.builds(
    vhdl::type::CompositeTypeDefinition,
)
vhdl::type::PhysicalTypeDefinition_strategy = st.builds(
    vhdl::type::PhysicalTypeDefinition,
    primary=
        safe_text
)
vhdl::type::RangeTypeDefinition_strategy = st.builds(
    vhdl::type::RangeTypeDefinition,
    direction=
        safe_text
)
NatureDefinition_strategy = st.builds(
    NatureDefinition,
)
vhdl::nature::ScalarNatureDefinition_strategy = st.builds(
    vhdl::nature::ScalarNatureDefinition,
)
vhdl::nature::CompositeNatureDefinition_strategy = st.builds(
    vhdl::nature::CompositeNatureDefinition,
)
ValueDeclaration_strategy = st.builds(
    ValueDeclaration,
)
vhdl::declaration::VariableDeclaration_strategy = st.builds(
    vhdl::declaration::VariableDeclaration,
    mode=
        safe_text,
    shared=
        st.booleans()
)
vhdl::declaration::SignalDeclaration_strategy = st.builds(
    vhdl::declaration::SignalDeclaration,
    kind=
        safe_text,
    mode=
        safe_text
)
vhdl::declaration::ConstantDeclaration_strategy = st.builds(
    vhdl::declaration::ConstantDeclaration,
)
SubprogramBody_strategy = st.builds(
    SubprogramBody,
)
declaration::vhdl::PortMaps_strategy = st.builds(
    declaration::vhdl::PortMaps,
)
declaration::vhdl::GenericMaps_strategy = st.builds(
    declaration::vhdl::GenericMaps,
)
declaration::vhdl::EntityReference_strategy = st.builds(
    declaration::vhdl::EntityReference,
)
declaration::vhdl::ComponentReference_strategy = st.builds(
    declaration::vhdl::ComponentReference,
)
declaration::SubprogramDeclaration_strategy = st.builds(
    declaration::SubprogramDeclaration,
)
nature::Natured_strategy = st.builds(
    nature::Natured,
)
vhdl::nature::ArrayNatureDefinition_strategy = st.builds(
    vhdl::nature::ArrayNatureDefinition,
)
SourceAspect_strategy = st.builds(
    SourceAspect,
)
vhdl::ams::Spectrum_strategy = st.builds(
    vhdl::ams::Spectrum,
)
vhdl::ams::Noise_strategy = st.builds(
    vhdl::ams::Noise,
)
MultiNamed_strategy = st.builds(
    MultiNamed,
)
declaration::QuantityDeclaration_strategy = st.builds(
    declaration::QuantityDeclaration,
)
QuantityAspect_strategy = st.builds(
    QuantityAspect,
)
QuantityDeclaration_strategy = st.builds(
    QuantityDeclaration,
)
vhdl::declaration::BranchQuantityDeclaration_strategy = st.builds(
    vhdl::declaration::BranchQuantityDeclaration,
)
declaration::vhdl::MultiName_strategy = st.builds(
    declaration::vhdl::MultiName,
)
declaration::vhdl::Name_strategy = st.builds(
    declaration::vhdl::Name,
)
AssociationExpression_strategy = st.builds(
    AssociationExpression,
)
vhdl::expression::ConditionalWaveformExpression_strategy = st.builds(
    vhdl::expression::ConditionalWaveformExpression,
)
type::EnumerationLiteral_strategy = st.builds(
    type::EnumerationLiteral,
)
expression::ValueExpression_strategy = st.builds(
    expression::ValueExpression,
)
type::Typed_strategy = st.builds(
    type::Typed,
)
vhdl::type::FileTypeDefinition_strategy = st.builds(
    vhdl::type::FileTypeDefinition,
)
vhdl::type::AccessTypeDefinition_strategy = st.builds(
    vhdl::type::AccessTypeDefinition,
)
vhdl::type::ArrayTypeDefinition_strategy = st.builds(
    vhdl::type::ArrayTypeDefinition,
)
vhdl::declaration::FunctionDeclaration_strategy = st.builds(
    vhdl::declaration::FunctionDeclaration,
    purity=
        safe_text
)
vhdl::declaration::SourceQuantityDeclaration_strategy = st.builds(
    vhdl::declaration::SourceQuantityDeclaration,
)
vhdl::declaration::FreeQuantityDeclaration_strategy = st.builds(
    vhdl::declaration::FreeQuantityDeclaration,
)
expression::Expression_strategy = st.builds(
    expression::Expression,
)
vhdl::expression::AllocatorExpression_strategy = st.builds(
    vhdl::expression::AllocatorExpression,
)
Name_strategy = st.builds(
    Name,
)
vhdl::expression::TypeQualificationExpression_strategy = st.builds(
    vhdl::expression::TypeQualificationExpression,
)
vhdl::expression::IdentifierExpression_strategy = st.builds(
    vhdl::expression::IdentifierExpression,
)
vhdl::expression::AllExpression_strategy = st.builds(
    vhdl::expression::AllExpression,
)
vhdl::expression::AttributeExpression_strategy = st.builds(
    vhdl::expression::AttributeExpression,
)
expression::MultiExpression_strategy = st.builds(
    expression::MultiExpression,
)
vhdl::expression::AggregateExpression_strategy = st.builds(
    vhdl::expression::AggregateExpression,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
vhdl::expression::PowerExpression_strategy = st.builds(
    vhdl::expression::PowerExpression,
)
vhdl::expression::RelationalExpression_strategy = st.builds(
    vhdl::expression::RelationalExpression,
    operator=
        safe_text
)
vhdl::expression::MultiplyingExpression_strategy = st.builds(
    vhdl::expression::MultiplyingExpression,
    operator=
        safe_text
)
vhdl::expression::AddingExpression_strategy = st.builds(
    vhdl::expression::AddingExpression,
    operator=
        safe_text
)
ConfigurationReference_strategy = st.builds(
    ConfigurationReference,
)
statement::vhdl::EntityReference_strategy = st.builds(
    statement::vhdl::EntityReference,
)
IterationScheme_strategy = st.builds(
    IterationScheme,
)
vhdl::statement::ForIterationScheme_strategy = st.builds(
    vhdl::statement::ForIterationScheme,
    variable=
        safe_text
)
vhdl::statement::WhileIterationScheme_strategy = st.builds(
    vhdl::statement::WhileIterationScheme,
)
GenerationScheme_strategy = st.builds(
    GenerationScheme,
)
vhdl::statement::IfGenerationScheme_strategy = st.builds(
    vhdl::statement::IfGenerationScheme,
)
statement::vhdl::ComponentReference_strategy = st.builds(
    statement::vhdl::ComponentReference,
)
InstantiationStatement_strategy = st.builds(
    InstantiationStatement,
)
vhdl::statement::ConfigurationInstantiationStatement_strategy = st.builds(
    vhdl::statement::ConfigurationInstantiationStatement,
)
vhdl::statement::EntityInstantiationStatement_strategy = st.builds(
    vhdl::statement::EntityInstantiationStatement,
)
vhdl::statement::ComponentInstantiationStatement_strategy = st.builds(
    vhdl::statement::ComponentInstantiationStatement,
)
statement::vhdl::Name_strategy = st.builds(
    statement::vhdl::Name,
)
BreakStatementItem_strategy = st.builds(
    BreakStatementItem,
)
statement::vhdl::PortMaps_strategy = st.builds(
    statement::vhdl::PortMaps,
)
statement::vhdl::Ports_strategy = st.builds(
    statement::vhdl::Ports,
)
statement::vhdl::GenericMaps_strategy = st.builds(
    statement::vhdl::GenericMaps,
)
statement::vhdl::Generics_strategy = st.builds(
    statement::vhdl::Generics,
)
CaseAlternative_strategy = st.builds(
    CaseAlternative,
)
CaseStatement_strategy = st.builds(
    CaseStatement,
)
vhdl::statement::SimultaneousCaseStatement_strategy = st.builds(
    vhdl::statement::SimultaneousCaseStatement,
)
statement::vhdl::CallReference_strategy = st.builds(
    statement::vhdl::CallReference,
)
IfStatementTest_strategy = st.builds(
    IfStatementTest,
)
IfStatement_strategy = st.builds(
    IfStatement,
)
vhdl::statement::SimultaneousIfStatement_strategy = st.builds(
    vhdl::statement::SimultaneousIfStatement,
)
vhdl::ComponentReference_strategy = st.builds(
    vhdl::ComponentReference,
)
statement::vhdl::MultiName_strategy = st.builds(
    statement::vhdl::MultiName,
)
DelayMechanism_strategy = st.builds(
    DelayMechanism,
)
vhdl::statement::RejectMechanism_strategy = st.builds(
    vhdl::statement::RejectMechanism,
)
vhdl::statement::TransportMechanism_strategy = st.builds(
    vhdl::statement::TransportMechanism,
)
ConditionalSignalAssignmentStatement_strategy = st.builds(
    ConditionalSignalAssignmentStatement,
)
vhdl::statement::SelectedSignalAssignmentStatement_strategy = st.builds(
    vhdl::statement::SelectedSignalAssignmentStatement,
)
SignalAssignmentStatement_strategy = st.builds(
    SignalAssignmentStatement,
)
vhdl::statement::SequentialSignalAssignmentStatement_strategy = st.builds(
    vhdl::statement::SequentialSignalAssignmentStatement,
)
vhdl::statement::ConditionalSignalAssignmentStatement_strategy = st.builds(
    vhdl::statement::ConditionalSignalAssignmentStatement,
)
ExpressionStatement_strategy = st.builds(
    ExpressionStatement,
)
vhdl::statement::ReturnStatement_strategy = st.builds(
    vhdl::statement::ReturnStatement,
)
SubprogramDeclaration_strategy = st.builds(
    SubprogramDeclaration,
)
vhdl::declaration::ProcedureDeclaration_strategy = st.builds(
    vhdl::declaration::ProcedureDeclaration,
)
vhdl::CallReference_strategy = st.builds(
    vhdl::CallReference,
)
vhdl::VhdlObject_strategy = st.builds(
    vhdl::VhdlObject,
    id=
        safe_text
)
vhdl::MultiName_strategy = st.builds(
    vhdl::MultiName,
)
vhdl::MultiNamed_strategy = st.builds(
    vhdl::MultiNamed,
)
vhdl::Named_strategy = st.builds(
    vhdl::Named,
)
CallReference_strategy = st.builds(
    CallReference,
)
vhdl::CallResolvedReference_strategy = st.builds(
    vhdl::CallResolvedReference,
)
configuration::ConfigurationReference_strategy = st.builds(
    configuration::ConfigurationReference,
)
ComponentReference_strategy = st.builds(
    ComponentReference,
)
PackageReference_strategy = st.builds(
    PackageReference,
)
EntityReference_strategy = st.builds(
    EntityReference,
)
nature::NatureReference_strategy = st.builds(
    nature::NatureReference,
)
type::TypeReference_strategy = st.builds(
    type::TypeReference,
)
MultiName_strategy = st.builds(
    MultiName,
)
declaration::Declaration_strategy = st.builds(
    declaration::Declaration,
)
vhdl::declaration::DisconnectionSpecification_strategy = st.builds(
    vhdl::declaration::DisconnectionSpecification,
)
vhdl::declaration::TerminalDeclaration_strategy = st.builds(
    vhdl::declaration::TerminalDeclaration,
)
vhdl::declaration::ValueDeclaration_strategy = st.builds(
    vhdl::declaration::ValueDeclaration,
)
vhdl::declaration::FileDeclaration_strategy = st.builds(
    vhdl::declaration::FileDeclaration,
)
vhdl::declaration::LimitDeclaration_strategy = st.builds(
    vhdl::declaration::LimitDeclaration,
)
TypeReference_strategy = st.builds(
    TypeReference,
)
vhdl::PackageReference_strategy = st.builds(
    vhdl::PackageReference,
)
Expression_strategy = st.builds(
    Expression,
)
vhdl::expression::UnaffectedExpression_strategy = st.builds(
    vhdl::expression::UnaffectedExpression,
)
vhdl::expression::AssociationExpression_strategy = st.builds(
    vhdl::expression::AssociationExpression,
)
vhdl::expression::ValueExpression_strategy = st.builds(
    vhdl::expression::ValueExpression,
    value=
        safe_text
)
vhdl::expression::WaveformExpression_strategy = st.builds(
    vhdl::expression::WaveformExpression,
)
vhdl::expression::MultiExpression_strategy = st.builds(
    vhdl::expression::MultiExpression,
)
vhdl::expression::NullExpression_strategy = st.builds(
    vhdl::expression::NullExpression,
)
Declaration_strategy = st.builds(
    Declaration,
)
vhdl::declaration::ConfigurationSpecification_strategy = st.builds(
    vhdl::declaration::ConfigurationSpecification,
)
vhdl::declaration::QuantityDeclaration_strategy = st.builds(
    vhdl::declaration::QuantityDeclaration,
)
vhdl::declaration::UseClauseDeclaration_strategy = st.builds(
    vhdl::declaration::UseClauseDeclaration,
)
vhdl::Name_strategy = st.builds(
    vhdl::Name,
)
VhdlObject_strategy = st.builds(
    VhdlObject,
)
vhdl::declaration::Declaration_strategy = st.builds(
    vhdl::declaration::Declaration,
)
vhdl::statement::IterationScheme_strategy = st.builds(
    vhdl::statement::IterationScheme,
)
vhdl::statement::BreakStatementItem_strategy = st.builds(
    vhdl::statement::BreakStatementItem,
)
vhdl::statement::Statement_strategy = st.builds(
    vhdl::statement::Statement,
    label=
        safe_text
)
vhdl::statement::GenerationScheme_strategy = st.builds(
    vhdl::statement::GenerationScheme,
)
vhdl::declaration::SubprogramBody_strategy = st.builds(
    vhdl::declaration::SubprogramBody,
)
vhdl::ams::SourceAspect_strategy = st.builds(
    vhdl::ams::SourceAspect,
)
vhdl::Signature_strategy = st.builds(
    vhdl::Signature,
)
vhdl::type::RecordTypeElement_strategy = st.builds(
    vhdl::type::RecordTypeElement,
)
vhdl::configuration::ConfigurationItem_strategy = st.builds(
    vhdl::configuration::ConfigurationItem,
)
vhdl::EntityResolvedReference_strategy = st.builds(
    vhdl::EntityResolvedReference,
)
vhdl::Generics_strategy = st.builds(
    vhdl::Generics,
)
vhdl::PortMaps_strategy = st.builds(
    vhdl::PortMaps,
)
vhdl::type::TypeDefinition_strategy = st.builds(
    vhdl::type::TypeDefinition,
)
vhdl::Model_strategy = st.builds(
    vhdl::Model,
)
vhdl::statement::IfStatementTest_strategy = st.builds(
    vhdl::statement::IfStatementTest,
)
vhdl::PackageResolvedReference_strategy = st.builds(
    vhdl::PackageResolvedReference,
)
vhdl::NameList_strategy = st.builds(
    vhdl::NameList,
)
vhdl::ComponentResolvedReference_strategy = st.builds(
    vhdl::ComponentResolvedReference,
)
vhdl::Module_strategy = st.builds(
    vhdl::Module,
)
vhdl::statement::CaseAlternative_strategy = st.builds(
    vhdl::statement::CaseAlternative,
)
vhdl::ams::QuantityAspect_strategy = st.builds(
    vhdl::ams::QuantityAspect,
)
vhdl::GenericMaps_strategy = st.builds(
    vhdl::GenericMaps,
)
vhdl::nature::RecordNatureElement_strategy = st.builds(
    vhdl::nature::RecordNatureElement,
)
vhdl::configuration::ConfigurationResolvedReference_strategy = st.builds(
    vhdl::configuration::ConfigurationResolvedReference,
)
vhdl::Ports_strategy = st.builds(
    vhdl::Ports,
)
vhdl::nature::NatureDefinition_strategy = st.builds(
    vhdl::nature::NatureDefinition,
)
vhdl::DesignUnit_strategy = st.builds(
    vhdl::DesignUnit,
    library=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
vhdl::statement::ExitStatement_strategy = st.builds(
    vhdl::statement::ExitStatement,
    exit=
        safe_text
)
vhdl::statement::SimultaneousProceduralStatement_strategy = st.builds(
    vhdl::statement::SimultaneousProceduralStatement,
)
vhdl::statement::InstantiationStatement_strategy = st.builds(
    vhdl::statement::InstantiationStatement,
)
vhdl::statement::WaitStatement_strategy = st.builds(
    vhdl::statement::WaitStatement,
)
vhdl::statement::BlockStatement_strategy = st.builds(
    vhdl::statement::BlockStatement,
)
vhdl::statement::NextStatement_strategy = st.builds(
    vhdl::statement::NextStatement,
    next=
        safe_text
)
vhdl::statement::ProcessStatement_strategy = st.builds(
    vhdl::statement::ProcessStatement,
    postponed=
        st.booleans()
)
vhdl::statement::LoopStatement_strategy = st.builds(
    vhdl::statement::LoopStatement,
)
vhdl::statement::ProcedureCallStatement_strategy = st.builds(
    vhdl::statement::ProcedureCallStatement,
    postponed=
        st.booleans()
)
vhdl::statement::ReportStatement_strategy = st.builds(
    vhdl::statement::ReportStatement,
)
vhdl::statement::BreakStatement_strategy = st.builds(
    vhdl::statement::BreakStatement,
)
vhdl::statement::AssertionStatement_strategy = st.builds(
    vhdl::statement::AssertionStatement,
    postponed=
        st.booleans()
)
vhdl::statement::IfStatement_strategy = st.builds(
    vhdl::statement::IfStatement,
)
vhdl::statement::VariableAssignmentStatement_strategy = st.builds(
    vhdl::statement::VariableAssignmentStatement,
)
vhdl::statement::SignalAssignmentStatement_strategy = st.builds(
    vhdl::statement::SignalAssignmentStatement,
    postponed=
        st.booleans(),
    guarded=
        st.booleans()
)
vhdl::statement::CaseStatement_strategy = st.builds(
    vhdl::statement::CaseStatement,
)
vhdl::statement::GenerateStatement_strategy = st.builds(
    vhdl::statement::GenerateStatement,
)
vhdl::statement::SimpleSimultaneousStatement_strategy = st.builds(
    vhdl::statement::SimpleSimultaneousStatement,
)
vhdl::EntityReference_strategy = st.builds(
    vhdl::EntityReference,
)
Named_strategy = st.builds(
    Named,
)
vhdl::declaration::AttributeSpecification_strategy = st.builds(
    vhdl::declaration::AttributeSpecification,
    class_=
        safe_text
)
vhdl::declaration::GroupDeclaration_strategy = st.builds(
    vhdl::declaration::GroupDeclaration,
)
vhdl::declaration::SubnatureDeclaration_strategy = st.builds(
    vhdl::declaration::SubnatureDeclaration,
)
vhdl::declaration::NatureDeclaration_strategy = st.builds(
    vhdl::declaration::NatureDeclaration,
)
vhdl::declaration::SubprogramDeclaration_strategy = st.builds(
    vhdl::declaration::SubprogramDeclaration,
)
vhdl::Component_strategy = st.builds(
    vhdl::Component,
)
vhdl::declaration::AttributeDeclaration_strategy = st.builds(
    vhdl::declaration::AttributeDeclaration,
)
vhdl::configuration::BlockConfiguration_strategy = st.builds(
    vhdl::configuration::BlockConfiguration,
)
vhdl::declaration::SubtypeDeclaration_strategy = st.builds(
    vhdl::declaration::SubtypeDeclaration,
)
vhdl::declaration::AliasDeclaration_strategy = st.builds(
    vhdl::declaration::AliasDeclaration,
)
vhdl::declaration::GroupTemplateDeclaration_strategy = st.builds(
    vhdl::declaration::GroupTemplateDeclaration,
    entry=
        safe_text
)
vhdl::declaration::TypeDeclaration_strategy = st.builds(
    vhdl::declaration::TypeDeclaration,
)
Module_strategy = st.builds(
    Module,
)
vhdl::Entity_strategy = st.builds(
    vhdl::Entity,
)
vhdl::configuration::Configuration_strategy = st.builds(
    vhdl::configuration::Configuration,
)
vhdl::Package_strategy = st.builds(
    vhdl::Package,
)
vhdl::PackageBody_strategy = st.builds(
    vhdl::PackageBody,
)
vhdl::Architecture_strategy = st.builds(
    vhdl::Architecture,
)
vhdl::expression::CharacterExpression_strategy = st.builds(
    vhdl::expression::CharacterExpression,
)
vhdl::expression::StringExpression_strategy = st.builds(
    vhdl::expression::StringExpression,
)
expression::BinaryExpression_strategy = st.builds(
    expression::BinaryExpression,
)
vhdl::expression::RangeExpression_strategy = st.builds(
    vhdl::expression::RangeExpression,
    direction=
        safe_text
)
vhdl::expression::OthersExpression_strategy = st.builds(
    vhdl::expression::OthersExpression,
)
vhdl::expression::OpenExpression_strategy = st.builds(
    vhdl::expression::OpenExpression,
)
vhdl::expression::UnaryExpression_strategy = st.builds(
    vhdl::expression::UnaryExpression,
    operator=
        safe_text
)
vhdl::expression::SignExpression_strategy = st.builds(
    vhdl::expression::SignExpression,
    sign=
        safe_text
)
vhdl::expression::SignatureExpression_strategy = st.builds(
    vhdl::expression::SignatureExpression,
)
vhdl::expression::ShiftExpression_strategy = st.builds(
    vhdl::expression::ShiftExpression,
    operator=
        safe_text
)
vhdl::expression::BinaryExpression_strategy = st.builds(
    vhdl::expression::BinaryExpression,
)
expression::vhdl::Name_strategy = st.builds(
    expression::vhdl::Name,
)
vhdl::expression::NameExpression_strategy = st.builds(
    vhdl::expression::NameExpression,
)
vhdl::expression::LogicalExpression_strategy = st.builds(
    vhdl::expression::LogicalExpression,
    operator=
        safe_text
)
NatureReference_strategy = st.builds(
    NatureReference,
)
expression::IndicationExpression_strategy = st.builds(
    expression::IndicationExpression,
)
vhdl::expression::SubnatureIndicationExpression_strategy = st.builds(
    vhdl::expression::SubnatureIndicationExpression,
)
vhdl::expression::SubtypeIndicationExpression_strategy = st.builds(
    vhdl::expression::SubtypeIndicationExpression,
)
vhdl::expression::IndicationExpression_strategy = st.builds(
    vhdl::expression::IndicationExpression,
)
vhdl::expression::Expression_strategy = st.builds(
    vhdl::expression::Expression,
)
ValueExpression_strategy = st.builds(
    ValueExpression,
)
vhdl::expression::UnitValueExpression_strategy = st.builds(
    vhdl::expression::UnitValueExpression,
)
vhdl::expression::BitStringExpression_strategy = st.builds(
    vhdl::expression::BitStringExpression,
)
vhdl::statement::ForGenerationScheme_strategy = st.builds(
    vhdl::statement::ForGenerationScheme,
    variable=
        safe_text
)
vhdl::statement::ExpressionStatement_strategy = st.builds(
    vhdl::statement::ExpressionStatement,
)
vhdl::statement::DelayMechanism_strategy = st.builds(
    vhdl::statement::DelayMechanism,
)
expression::vhdl::Signature_strategy = st.builds(
    expression::vhdl::Signature,
)

@given(instance=Configuration_strategy)
@settings(max_examples=50)
def test_configuration_instantiation(instance):
    assert isinstance(instance, Configuration)

@given(instance=vhdl::configuration::ConfigurationReference_strategy)
@settings(max_examples=50)
def test_vhdl::configuration::configurationreference_instantiation(instance):
    assert isinstance(instance, vhdl::configuration::ConfigurationReference)

@given(instance=configuration::vhdl::EntityReference_strategy)
@settings(max_examples=50)
def test_configuration::vhdl::entityreference_instantiation(instance):
    assert isinstance(instance, configuration::vhdl::EntityReference)

@given(instance=BlockConfiguration_strategy)
@settings(max_examples=50)
def test_blockconfiguration_instantiation(instance):
    assert isinstance(instance, BlockConfiguration)

@given(instance=configuration::vhdl::PortMaps_strategy)
@settings(max_examples=50)
def test_configuration::vhdl::portmaps_instantiation(instance):
    assert isinstance(instance, configuration::vhdl::PortMaps)

@given(instance=configuration::vhdl::GenericMaps_strategy)
@settings(max_examples=50)
def test_configuration::vhdl::genericmaps_instantiation(instance):
    assert isinstance(instance, configuration::vhdl::GenericMaps)

@given(instance=configuration::vhdl::MultiName_strategy)
@settings(max_examples=50)
def test_configuration::vhdl::multiname_instantiation(instance):
    assert isinstance(instance, configuration::vhdl::MultiName)

@given(instance=ConfigurationItem_strategy)
@settings(max_examples=50)
def test_configurationitem_instantiation(instance):
    assert isinstance(instance, ConfigurationItem)

@given(instance=vhdl::configuration::ComponentConfiguration_strategy)
@settings(max_examples=50)
def test_vhdl::configuration::componentconfiguration_instantiation(instance):
    assert isinstance(instance, vhdl::configuration::ComponentConfiguration)

@given(instance=configuration::vhdl::Name_strategy)
@settings(max_examples=50)
def test_configuration::vhdl::name_instantiation(instance):
    assert isinstance(instance, configuration::vhdl::Name)

@given(instance=configuration::ConfigurationItem_strategy)
@settings(max_examples=50)
def test_configuration::configurationitem_instantiation(instance):
    assert isinstance(instance, configuration::ConfigurationItem)

@given(instance=nature::CompositeNatureDefinition_strategy)
@settings(max_examples=50)
def test_nature::compositenaturedefinition_instantiation(instance):
    assert isinstance(instance, nature::CompositeNatureDefinition)

@given(instance=vhdl::type::TypeReference_strategy)
@settings(max_examples=50)
def test_vhdl::type::typereference_instantiation(instance):
    assert isinstance(instance, vhdl::type::TypeReference)

@given(instance=vhdl::type::Typed_strategy)
@settings(max_examples=50)
def test_vhdl::type::typed_instantiation(instance):
    assert isinstance(instance, vhdl::type::Typed)

@given(instance=vhdl::nature::Natured_strategy)
@settings(max_examples=50)
def test_vhdl::nature::natured_instantiation(instance):
    assert isinstance(instance, vhdl::nature::Natured)

@given(instance=vhdl::nature::NatureReference_strategy)
@settings(max_examples=50)
def test_vhdl::nature::naturereference_instantiation(instance):
    assert isinstance(instance, vhdl::nature::NatureReference)

@given(instance=nature::vhdl::Name_strategy)
@settings(max_examples=50)
def test_nature::vhdl::name_instantiation(instance):
    assert isinstance(instance, nature::vhdl::Name)

@given(instance=RecordNatureElement_strategy)
@settings(max_examples=50)
def test_recordnatureelement_instantiation(instance):
    assert isinstance(instance, RecordNatureElement)

@given(instance=CompositeNatureDefinition_strategy)
@settings(max_examples=50)
def test_compositenaturedefinition_instantiation(instance):
    assert isinstance(instance, CompositeNatureDefinition)

@given(instance=vhdl::nature::RecordNatureDefinition_strategy)
@settings(max_examples=50)
def test_vhdl::nature::recordnaturedefinition_instantiation(instance):
    assert isinstance(instance, vhdl::nature::RecordNatureDefinition)

@given(instance=ArrayNatureDefinition_strategy)
@settings(max_examples=50)
def test_arraynaturedefinition_instantiation(instance):
    assert isinstance(instance, ArrayNatureDefinition)

@given(instance=vhdl::nature::UnconstrainedArrayNatureDefinition_strategy)
@settings(max_examples=50)
def test_vhdl::nature::unconstrainedarraynaturedefinition_instantiation(instance):
    assert isinstance(instance, vhdl::nature::UnconstrainedArrayNatureDefinition)

@given(instance=vhdl::nature::ConstrainedArrayNatureDefinition_strategy)
@settings(max_examples=50)
def test_vhdl::nature::constrainedarraynaturedefinition_instantiation(instance):
    assert isinstance(instance, vhdl::nature::ConstrainedArrayNatureDefinition)

@given(instance=type::vhdl::Name_strategy)
@settings(max_examples=50)
def test_type::vhdl::name_instantiation(instance):
    assert isinstance(instance, type::vhdl::Name)

@given(instance=vhdl::type::PhysicalTypeDefinitionSecondary_strategy)
@settings(max_examples=50)
def test_vhdl::type::physicaltypedefinitionsecondary_instantiation(instance):
    assert isinstance(instance, vhdl::type::PhysicalTypeDefinitionSecondary)

@given(instance=vhdl::type::PhysicalTypeDefinitionSecondary_strategy)
def test_vhdl::type::physicaltypedefinitionsecondary_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=vhdl::type::PhysicalTypeDefinitionSecondary_strategy)
def test_vhdl::type::physicaltypedefinitionsecondary_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=vhdl::type::PhysicalTypeDefinitionSecondary_strategy)
def test_vhdl::type::physicaltypedefinitionsecondary_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=vhdl::type::PhysicalTypeDefinitionSecondary_strategy)
def test_vhdl::type::physicaltypedefinitionsecondary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PhysicalTypeDefinitionSecondary_strategy)
@settings(max_examples=50)
def test_physicaltypedefinitionsecondary_instantiation(instance):
    assert isinstance(instance, PhysicalTypeDefinitionSecondary)

@given(instance=EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_enumerationliteral_instantiation(instance):
    assert isinstance(instance, EnumerationLiteral)

@given(instance=vhdl::type::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_vhdl::type::enumerationliteral_instantiation(instance):
    assert isinstance(instance, vhdl::type::EnumerationLiteral)

@given(instance=ArrayTypeDefinition_strategy)
@settings(max_examples=50)
def test_arraytypedefinition_instantiation(instance):
    assert isinstance(instance, ArrayTypeDefinition)

@given(instance=vhdl::type::UnconstrainedArrayTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl::type::unconstrainedarraytypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl::type::UnconstrainedArrayTypeDefinition)

@given(instance=vhdl::type::ConstrainedArrayTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl::type::constrainedarraytypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl::type::ConstrainedArrayTypeDefinition)

@given(instance=type::CompositeTypeDefinition_strategy)
@settings(max_examples=50)
def test_type::compositetypedefinition_instantiation(instance):
    assert isinstance(instance, type::CompositeTypeDefinition)

@given(instance=RecordTypeElement_strategy)
@settings(max_examples=50)
def test_recordtypeelement_instantiation(instance):
    assert isinstance(instance, RecordTypeElement)

@given(instance=CompositeTypeDefinition_strategy)
@settings(max_examples=50)
def test_compositetypedefinition_instantiation(instance):
    assert isinstance(instance, CompositeTypeDefinition)

@given(instance=vhdl::type::RecordTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl::type::recordtypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl::type::RecordTypeDefinition)

@given(instance=type::TypeDefinition_strategy)
@settings(max_examples=50)
def test_type::typedefinition_instantiation(instance):
    assert isinstance(instance, type::TypeDefinition)

@given(instance=TypeDefinition_strategy)
@settings(max_examples=50)
def test_typedefinition_instantiation(instance):
    assert isinstance(instance, TypeDefinition)

@given(instance=vhdl::type::EnumerationTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl::type::enumerationtypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl::type::EnumerationTypeDefinition)

@given(instance=vhdl::type::CompositeTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl::type::compositetypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl::type::CompositeTypeDefinition)

@given(instance=vhdl::type::PhysicalTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl::type::physicaltypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl::type::PhysicalTypeDefinition)

@given(instance=vhdl::type::PhysicalTypeDefinition_strategy)
def test_vhdl::type::physicaltypedefinition_primary_type(instance):
    assert isinstance(instance.primary, str)


@given(instance=vhdl::type::PhysicalTypeDefinition_strategy)
def test_vhdl::type::physicaltypedefinition_primary_setter(instance):
    original = instance.primary
    instance.primary = original
    assert instance.primary == original

@given(instance=vhdl::type::RangeTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl::type::rangetypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl::type::RangeTypeDefinition)

@given(instance=vhdl::type::RangeTypeDefinition_strategy)
def test_vhdl::type::rangetypedefinition_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=vhdl::type::RangeTypeDefinition_strategy)
def test_vhdl::type::rangetypedefinition_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=NatureDefinition_strategy)
@settings(max_examples=50)
def test_naturedefinition_instantiation(instance):
    assert isinstance(instance, NatureDefinition)

@given(instance=vhdl::nature::ScalarNatureDefinition_strategy)
@settings(max_examples=50)
def test_vhdl::nature::scalarnaturedefinition_instantiation(instance):
    assert isinstance(instance, vhdl::nature::ScalarNatureDefinition)

@given(instance=vhdl::nature::CompositeNatureDefinition_strategy)
@settings(max_examples=50)
def test_vhdl::nature::compositenaturedefinition_instantiation(instance):
    assert isinstance(instance, vhdl::nature::CompositeNatureDefinition)

@given(instance=ValueDeclaration_strategy)
@settings(max_examples=50)
def test_valuedeclaration_instantiation(instance):
    assert isinstance(instance, ValueDeclaration)

@given(instance=vhdl::declaration::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl::declaration::variabledeclaration_instantiation(instance):
    assert isinstance(instance, vhdl::declaration::VariableDeclaration)

@given(instance=vhdl::declaration::VariableDeclaration_strategy)
def test_vhdl::declaration::variabledeclaration_mode_type(instance):
    assert isinstance(instance.mode, str)


@given(instance=vhdl::declaration::VariableDeclaration_strategy)
def test_vhdl::declaration::variabledeclaration_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=vhdl::declaration::VariableDeclaration_strategy)
def test_vhdl::declaration::variabledeclaration_shared_type(instance):
    assert isinstance(instance.shared, bool)


@given(instance=vhdl::declaration::VariableDeclaration_strategy)
def test_vhdl::declaration::variabledeclaration_shared_setter(instance):
    original = instance.shared
    instance.shared = original
    assert instance.shared == original

@given(instance=vhdl::declaration::SignalDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl::declaration::signaldeclaration_instantiation(instance):
    assert isinstance(instance, vhdl::declaration::SignalDeclaration)

@given(instance=vhdl::declaration::SignalDeclaration_strategy)
def test_vhdl::declaration::signaldeclaration_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=vhdl::declaration::SignalDeclaration_strategy)
def test_vhdl::declaration::signaldeclaration_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=vhdl::declaration::SignalDeclaration_strategy)
def test_vhdl::declaration::signaldeclaration_mode_type(instance):
    assert isinstance(instance.mode, str)


@given(instance=vhdl::declaration::SignalDeclaration_strategy)
def test_vhdl::declaration::signaldeclaration_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=vhdl::declaration::ConstantDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl::declaration::constantdeclaration_instantiation(instance):
    assert isinstance(instance, vhdl::declaration::ConstantDeclaration)

@given(instance=SubprogramBody_strategy)
@settings(max_examples=50)
def test_subprogrambody_instantiation(instance):
    assert isinstance(instance, SubprogramBody)

@given(instance=declaration::vhdl::PortMaps_strategy)
@settings(max_examples=50)
def test_declaration::vhdl::portmaps_instantiation(instance):
    assert isinstance(instance, declaration::vhdl::PortMaps)

@given(instance=declaration::vhdl::GenericMaps_strategy)
@settings(max_examples=50)
def test_declaration::vhdl::genericmaps_instantiation(instance):
    assert isinstance(instance, declaration::vhdl::GenericMaps)

@given(instance=declaration::vhdl::EntityReference_strategy)
@settings(max_examples=50)
def test_declaration::vhdl::entityreference_instantiation(instance):
    assert isinstance(instance, declaration::vhdl::EntityReference)

@given(instance=declaration::vhdl::ComponentReference_strategy)
@settings(max_examples=50)
def test_declaration::vhdl::componentreference_instantiation(instance):
    assert isinstance(instance, declaration::vhdl::ComponentReference)

@given(instance=declaration::SubprogramDeclaration_strategy)
@settings(max_examples=50)
def test_declaration::subprogramdeclaration_instantiation(instance):
    assert isinstance(instance, declaration::SubprogramDeclaration)

@given(instance=nature::Natured_strategy)
@settings(max_examples=50)
def test_nature::natured_instantiation(instance):
    assert isinstance(instance, nature::Natured)

@given(instance=vhdl::nature::ArrayNatureDefinition_strategy)
@settings(max_examples=50)
def test_vhdl::nature::arraynaturedefinition_instantiation(instance):
    assert isinstance(instance, vhdl::nature::ArrayNatureDefinition)

@given(instance=SourceAspect_strategy)
@settings(max_examples=50)
def test_sourceaspect_instantiation(instance):
    assert isinstance(instance, SourceAspect)

@given(instance=vhdl::ams::Spectrum_strategy)
@settings(max_examples=50)
def test_vhdl::ams::spectrum_instantiation(instance):
    assert isinstance(instance, vhdl::ams::Spectrum)

@given(instance=vhdl::ams::Noise_strategy)
@settings(max_examples=50)
def test_vhdl::ams::noise_instantiation(instance):
    assert isinstance(instance, vhdl::ams::Noise)

@given(instance=MultiNamed_strategy)
@settings(max_examples=50)
def test_multinamed_instantiation(instance):
    assert isinstance(instance, MultiNamed)

@given(instance=declaration::QuantityDeclaration_strategy)
@settings(max_examples=50)
def test_declaration::quantitydeclaration_instantiation(instance):
    assert isinstance(instance, declaration::QuantityDeclaration)

@given(instance=QuantityAspect_strategy)
@settings(max_examples=50)
def test_quantityaspect_instantiation(instance):
    assert isinstance(instance, QuantityAspect)

@given(instance=QuantityDeclaration_strategy)
@settings(max_examples=50)
def test_quantitydeclaration_instantiation(instance):
    assert isinstance(instance, QuantityDeclaration)

@given(instance=vhdl::declaration::BranchQuantityDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl::declaration::branchquantitydeclaration_instantiation(instance):
    assert isinstance(instance, vhdl::declaration::BranchQuantityDeclaration)

@given(instance=declaration::vhdl::MultiName_strategy)
@settings(max_examples=50)
def test_declaration::vhdl::multiname_instantiation(instance):
    assert isinstance(instance, declaration::vhdl::MultiName)

@given(instance=declaration::vhdl::Name_strategy)
@settings(max_examples=50)
def test_declaration::vhdl::name_instantiation(instance):
    assert isinstance(instance, declaration::vhdl::Name)

@given(instance=AssociationExpression_strategy)
@settings(max_examples=50)
def test_associationexpression_instantiation(instance):
    assert isinstance(instance, AssociationExpression)

@given(instance=vhdl::expression::ConditionalWaveformExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::conditionalwaveformexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::ConditionalWaveformExpression)

@given(instance=type::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_type::enumerationliteral_instantiation(instance):
    assert isinstance(instance, type::EnumerationLiteral)

@given(instance=expression::ValueExpression_strategy)
@settings(max_examples=50)
def test_expression::valueexpression_instantiation(instance):
    assert isinstance(instance, expression::ValueExpression)

@given(instance=type::Typed_strategy)
@settings(max_examples=50)
def test_type::typed_instantiation(instance):
    assert isinstance(instance, type::Typed)

@given(instance=vhdl::type::FileTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl::type::filetypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl::type::FileTypeDefinition)

@given(instance=vhdl::type::AccessTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl::type::accesstypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl::type::AccessTypeDefinition)

@given(instance=vhdl::type::ArrayTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl::type::arraytypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl::type::ArrayTypeDefinition)

@given(instance=vhdl::declaration::FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl::declaration::functiondeclaration_instantiation(instance):
    assert isinstance(instance, vhdl::declaration::FunctionDeclaration)

@given(instance=vhdl::declaration::FunctionDeclaration_strategy)
def test_vhdl::declaration::functiondeclaration_purity_type(instance):
    assert isinstance(instance.purity, str)


@given(instance=vhdl::declaration::FunctionDeclaration_strategy)
def test_vhdl::declaration::functiondeclaration_purity_setter(instance):
    original = instance.purity
    instance.purity = original
    assert instance.purity == original

@given(instance=vhdl::declaration::SourceQuantityDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl::declaration::sourcequantitydeclaration_instantiation(instance):
    assert isinstance(instance, vhdl::declaration::SourceQuantityDeclaration)

@given(instance=vhdl::declaration::FreeQuantityDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl::declaration::freequantitydeclaration_instantiation(instance):
    assert isinstance(instance, vhdl::declaration::FreeQuantityDeclaration)

@given(instance=expression::Expression_strategy)
@settings(max_examples=50)
def test_expression::expression_instantiation(instance):
    assert isinstance(instance, expression::Expression)

@given(instance=vhdl::expression::AllocatorExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::allocatorexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::AllocatorExpression)

@given(instance=Name_strategy)
@settings(max_examples=50)
def test_name_instantiation(instance):
    assert isinstance(instance, Name)

@given(instance=vhdl::expression::TypeQualificationExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::typequalificationexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::TypeQualificationExpression)

@given(instance=vhdl::expression::IdentifierExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::identifierexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::IdentifierExpression)

@given(instance=vhdl::expression::AllExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::allexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::AllExpression)

@given(instance=vhdl::expression::AttributeExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::attributeexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::AttributeExpression)

@given(instance=expression::MultiExpression_strategy)
@settings(max_examples=50)
def test_expression::multiexpression_instantiation(instance):
    assert isinstance(instance, expression::MultiExpression)

@given(instance=vhdl::expression::AggregateExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::aggregateexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::AggregateExpression)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=vhdl::expression::PowerExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::powerexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::PowerExpression)

@given(instance=vhdl::expression::RelationalExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::relationalexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::RelationalExpression)

@given(instance=vhdl::expression::RelationalExpression_strategy)
def test_vhdl::expression::relationalexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=vhdl::expression::RelationalExpression_strategy)
def test_vhdl::expression::relationalexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=vhdl::expression::MultiplyingExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::multiplyingexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::MultiplyingExpression)

@given(instance=vhdl::expression::MultiplyingExpression_strategy)
def test_vhdl::expression::multiplyingexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=vhdl::expression::MultiplyingExpression_strategy)
def test_vhdl::expression::multiplyingexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=vhdl::expression::AddingExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::addingexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::AddingExpression)

@given(instance=vhdl::expression::AddingExpression_strategy)
def test_vhdl::expression::addingexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=vhdl::expression::AddingExpression_strategy)
def test_vhdl::expression::addingexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ConfigurationReference_strategy)
@settings(max_examples=50)
def test_configurationreference_instantiation(instance):
    assert isinstance(instance, ConfigurationReference)

@given(instance=statement::vhdl::EntityReference_strategy)
@settings(max_examples=50)
def test_statement::vhdl::entityreference_instantiation(instance):
    assert isinstance(instance, statement::vhdl::EntityReference)

@given(instance=IterationScheme_strategy)
@settings(max_examples=50)
def test_iterationscheme_instantiation(instance):
    assert isinstance(instance, IterationScheme)

@given(instance=vhdl::statement::ForIterationScheme_strategy)
@settings(max_examples=50)
def test_vhdl::statement::foriterationscheme_instantiation(instance):
    assert isinstance(instance, vhdl::statement::ForIterationScheme)

@given(instance=vhdl::statement::ForIterationScheme_strategy)
def test_vhdl::statement::foriterationscheme_variable_type(instance):
    assert isinstance(instance.variable, str)


@given(instance=vhdl::statement::ForIterationScheme_strategy)
def test_vhdl::statement::foriterationscheme_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=vhdl::statement::WhileIterationScheme_strategy)
@settings(max_examples=50)
def test_vhdl::statement::whileiterationscheme_instantiation(instance):
    assert isinstance(instance, vhdl::statement::WhileIterationScheme)

@given(instance=GenerationScheme_strategy)
@settings(max_examples=50)
def test_generationscheme_instantiation(instance):
    assert isinstance(instance, GenerationScheme)

@given(instance=vhdl::statement::IfGenerationScheme_strategy)
@settings(max_examples=50)
def test_vhdl::statement::ifgenerationscheme_instantiation(instance):
    assert isinstance(instance, vhdl::statement::IfGenerationScheme)

@given(instance=statement::vhdl::ComponentReference_strategy)
@settings(max_examples=50)
def test_statement::vhdl::componentreference_instantiation(instance):
    assert isinstance(instance, statement::vhdl::ComponentReference)

@given(instance=InstantiationStatement_strategy)
@settings(max_examples=50)
def test_instantiationstatement_instantiation(instance):
    assert isinstance(instance, InstantiationStatement)

@given(instance=vhdl::statement::ConfigurationInstantiationStatement_strategy)
@settings(max_examples=50)
def test_vhdl::statement::configurationinstantiationstatement_instantiation(instance):
    assert isinstance(instance, vhdl::statement::ConfigurationInstantiationStatement)

@given(instance=vhdl::statement::EntityInstantiationStatement_strategy)
@settings(max_examples=50)
def test_vhdl::statement::entityinstantiationstatement_instantiation(instance):
    assert isinstance(instance, vhdl::statement::EntityInstantiationStatement)

@given(instance=vhdl::statement::ComponentInstantiationStatement_strategy)
@settings(max_examples=50)
def test_vhdl::statement::componentinstantiationstatement_instantiation(instance):
    assert isinstance(instance, vhdl::statement::ComponentInstantiationStatement)

@given(instance=statement::vhdl::Name_strategy)
@settings(max_examples=50)
def test_statement::vhdl::name_instantiation(instance):
    assert isinstance(instance, statement::vhdl::Name)

@given(instance=BreakStatementItem_strategy)
@settings(max_examples=50)
def test_breakstatementitem_instantiation(instance):
    assert isinstance(instance, BreakStatementItem)

@given(instance=statement::vhdl::PortMaps_strategy)
@settings(max_examples=50)
def test_statement::vhdl::portmaps_instantiation(instance):
    assert isinstance(instance, statement::vhdl::PortMaps)

@given(instance=statement::vhdl::Ports_strategy)
@settings(max_examples=50)
def test_statement::vhdl::ports_instantiation(instance):
    assert isinstance(instance, statement::vhdl::Ports)

@given(instance=statement::vhdl::GenericMaps_strategy)
@settings(max_examples=50)
def test_statement::vhdl::genericmaps_instantiation(instance):
    assert isinstance(instance, statement::vhdl::GenericMaps)

@given(instance=statement::vhdl::Generics_strategy)
@settings(max_examples=50)
def test_statement::vhdl::generics_instantiation(instance):
    assert isinstance(instance, statement::vhdl::Generics)

@given(instance=CaseAlternative_strategy)
@settings(max_examples=50)
def test_casealternative_instantiation(instance):
    assert isinstance(instance, CaseAlternative)

@given(instance=CaseStatement_strategy)
@settings(max_examples=50)
def test_casestatement_instantiation(instance):
    assert isinstance(instance, CaseStatement)

@given(instance=vhdl::statement::SimultaneousCaseStatement_strategy)
@settings(max_examples=50)
def test_vhdl::statement::simultaneouscasestatement_instantiation(instance):
    assert isinstance(instance, vhdl::statement::SimultaneousCaseStatement)

@given(instance=statement::vhdl::CallReference_strategy)
@settings(max_examples=50)
def test_statement::vhdl::callreference_instantiation(instance):
    assert isinstance(instance, statement::vhdl::CallReference)

@given(instance=IfStatementTest_strategy)
@settings(max_examples=50)
def test_ifstatementtest_instantiation(instance):
    assert isinstance(instance, IfStatementTest)

@given(instance=IfStatement_strategy)
@settings(max_examples=50)
def test_ifstatement_instantiation(instance):
    assert isinstance(instance, IfStatement)

@given(instance=vhdl::statement::SimultaneousIfStatement_strategy)
@settings(max_examples=50)
def test_vhdl::statement::simultaneousifstatement_instantiation(instance):
    assert isinstance(instance, vhdl::statement::SimultaneousIfStatement)

@given(instance=vhdl::ComponentReference_strategy)
@settings(max_examples=50)
def test_vhdl::componentreference_instantiation(instance):
    assert isinstance(instance, vhdl::ComponentReference)

@given(instance=statement::vhdl::MultiName_strategy)
@settings(max_examples=50)
def test_statement::vhdl::multiname_instantiation(instance):
    assert isinstance(instance, statement::vhdl::MultiName)

@given(instance=DelayMechanism_strategy)
@settings(max_examples=50)
def test_delaymechanism_instantiation(instance):
    assert isinstance(instance, DelayMechanism)

@given(instance=vhdl::statement::RejectMechanism_strategy)
@settings(max_examples=50)
def test_vhdl::statement::rejectmechanism_instantiation(instance):
    assert isinstance(instance, vhdl::statement::RejectMechanism)

@given(instance=vhdl::statement::TransportMechanism_strategy)
@settings(max_examples=50)
def test_vhdl::statement::transportmechanism_instantiation(instance):
    assert isinstance(instance, vhdl::statement::TransportMechanism)

@given(instance=ConditionalSignalAssignmentStatement_strategy)
@settings(max_examples=50)
def test_conditionalsignalassignmentstatement_instantiation(instance):
    assert isinstance(instance, ConditionalSignalAssignmentStatement)

@given(instance=vhdl::statement::SelectedSignalAssignmentStatement_strategy)
@settings(max_examples=50)
def test_vhdl::statement::selectedsignalassignmentstatement_instantiation(instance):
    assert isinstance(instance, vhdl::statement::SelectedSignalAssignmentStatement)

@given(instance=SignalAssignmentStatement_strategy)
@settings(max_examples=50)
def test_signalassignmentstatement_instantiation(instance):
    assert isinstance(instance, SignalAssignmentStatement)

@given(instance=vhdl::statement::SequentialSignalAssignmentStatement_strategy)
@settings(max_examples=50)
def test_vhdl::statement::sequentialsignalassignmentstatement_instantiation(instance):
    assert isinstance(instance, vhdl::statement::SequentialSignalAssignmentStatement)

@given(instance=vhdl::statement::ConditionalSignalAssignmentStatement_strategy)
@settings(max_examples=50)
def test_vhdl::statement::conditionalsignalassignmentstatement_instantiation(instance):
    assert isinstance(instance, vhdl::statement::ConditionalSignalAssignmentStatement)

@given(instance=ExpressionStatement_strategy)
@settings(max_examples=50)
def test_expressionstatement_instantiation(instance):
    assert isinstance(instance, ExpressionStatement)

@given(instance=vhdl::statement::ReturnStatement_strategy)
@settings(max_examples=50)
def test_vhdl::statement::returnstatement_instantiation(instance):
    assert isinstance(instance, vhdl::statement::ReturnStatement)

@given(instance=SubprogramDeclaration_strategy)
@settings(max_examples=50)
def test_subprogramdeclaration_instantiation(instance):
    assert isinstance(instance, SubprogramDeclaration)

@given(instance=vhdl::declaration::ProcedureDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl::declaration::proceduredeclaration_instantiation(instance):
    assert isinstance(instance, vhdl::declaration::ProcedureDeclaration)

@given(instance=vhdl::CallReference_strategy)
@settings(max_examples=50)
def test_vhdl::callreference_instantiation(instance):
    assert isinstance(instance, vhdl::CallReference)

@given(instance=vhdl::VhdlObject_strategy)
@settings(max_examples=50)
def test_vhdl::vhdlobject_instantiation(instance):
    assert isinstance(instance, vhdl::VhdlObject)

@given(instance=vhdl::VhdlObject_strategy)
def test_vhdl::vhdlobject_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=vhdl::VhdlObject_strategy)
def test_vhdl::vhdlobject_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=vhdl::MultiName_strategy)
@settings(max_examples=50)
def test_vhdl::multiname_instantiation(instance):
    assert isinstance(instance, vhdl::MultiName)

@given(instance=vhdl::MultiNamed_strategy)
@settings(max_examples=50)
def test_vhdl::multinamed_instantiation(instance):
    assert isinstance(instance, vhdl::MultiNamed)

@given(instance=vhdl::Named_strategy)
@settings(max_examples=50)
def test_vhdl::named_instantiation(instance):
    assert isinstance(instance, vhdl::Named)

@given(instance=CallReference_strategy)
@settings(max_examples=50)
def test_callreference_instantiation(instance):
    assert isinstance(instance, CallReference)

@given(instance=vhdl::CallResolvedReference_strategy)
@settings(max_examples=50)
def test_vhdl::callresolvedreference_instantiation(instance):
    assert isinstance(instance, vhdl::CallResolvedReference)

@given(instance=configuration::ConfigurationReference_strategy)
@settings(max_examples=50)
def test_configuration::configurationreference_instantiation(instance):
    assert isinstance(instance, configuration::ConfigurationReference)

@given(instance=ComponentReference_strategy)
@settings(max_examples=50)
def test_componentreference_instantiation(instance):
    assert isinstance(instance, ComponentReference)

@given(instance=PackageReference_strategy)
@settings(max_examples=50)
def test_packagereference_instantiation(instance):
    assert isinstance(instance, PackageReference)

@given(instance=EntityReference_strategy)
@settings(max_examples=50)
def test_entityreference_instantiation(instance):
    assert isinstance(instance, EntityReference)

@given(instance=nature::NatureReference_strategy)
@settings(max_examples=50)
def test_nature::naturereference_instantiation(instance):
    assert isinstance(instance, nature::NatureReference)

@given(instance=type::TypeReference_strategy)
@settings(max_examples=50)
def test_type::typereference_instantiation(instance):
    assert isinstance(instance, type::TypeReference)

@given(instance=MultiName_strategy)
@settings(max_examples=50)
def test_multiname_instantiation(instance):
    assert isinstance(instance, MultiName)

@given(instance=declaration::Declaration_strategy)
@settings(max_examples=50)
def test_declaration::declaration_instantiation(instance):
    assert isinstance(instance, declaration::Declaration)

@given(instance=vhdl::declaration::DisconnectionSpecification_strategy)
@settings(max_examples=50)
def test_vhdl::declaration::disconnectionspecification_instantiation(instance):
    assert isinstance(instance, vhdl::declaration::DisconnectionSpecification)

@given(instance=vhdl::declaration::TerminalDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl::declaration::terminaldeclaration_instantiation(instance):
    assert isinstance(instance, vhdl::declaration::TerminalDeclaration)

@given(instance=vhdl::declaration::ValueDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl::declaration::valuedeclaration_instantiation(instance):
    assert isinstance(instance, vhdl::declaration::ValueDeclaration)

@given(instance=vhdl::declaration::FileDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl::declaration::filedeclaration_instantiation(instance):
    assert isinstance(instance, vhdl::declaration::FileDeclaration)

@given(instance=vhdl::declaration::LimitDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl::declaration::limitdeclaration_instantiation(instance):
    assert isinstance(instance, vhdl::declaration::LimitDeclaration)

@given(instance=TypeReference_strategy)
@settings(max_examples=50)
def test_typereference_instantiation(instance):
    assert isinstance(instance, TypeReference)

@given(instance=vhdl::PackageReference_strategy)
@settings(max_examples=50)
def test_vhdl::packagereference_instantiation(instance):
    assert isinstance(instance, vhdl::PackageReference)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=vhdl::expression::UnaffectedExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::unaffectedexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::UnaffectedExpression)

@given(instance=vhdl::expression::AssociationExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::associationexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::AssociationExpression)

@given(instance=vhdl::expression::ValueExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::valueexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::ValueExpression)

@given(instance=vhdl::expression::ValueExpression_strategy)
def test_vhdl::expression::valueexpression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vhdl::expression::ValueExpression_strategy)
def test_vhdl::expression::valueexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vhdl::expression::WaveformExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::waveformexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::WaveformExpression)

@given(instance=vhdl::expression::MultiExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::multiexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::MultiExpression)

@given(instance=vhdl::expression::NullExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::nullexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::NullExpression)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=vhdl::declaration::ConfigurationSpecification_strategy)
@settings(max_examples=50)
def test_vhdl::declaration::configurationspecification_instantiation(instance):
    assert isinstance(instance, vhdl::declaration::ConfigurationSpecification)

@given(instance=vhdl::declaration::QuantityDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl::declaration::quantitydeclaration_instantiation(instance):
    assert isinstance(instance, vhdl::declaration::QuantityDeclaration)

@given(instance=vhdl::declaration::UseClauseDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl::declaration::useclausedeclaration_instantiation(instance):
    assert isinstance(instance, vhdl::declaration::UseClauseDeclaration)

@given(instance=vhdl::Name_strategy)
@settings(max_examples=50)
def test_vhdl::name_instantiation(instance):
    assert isinstance(instance, vhdl::Name)

@given(instance=VhdlObject_strategy)
@settings(max_examples=50)
def test_vhdlobject_instantiation(instance):
    assert isinstance(instance, VhdlObject)

@given(instance=vhdl::declaration::Declaration_strategy)
@settings(max_examples=50)
def test_vhdl::declaration::declaration_instantiation(instance):
    assert isinstance(instance, vhdl::declaration::Declaration)

@given(instance=vhdl::statement::IterationScheme_strategy)
@settings(max_examples=50)
def test_vhdl::statement::iterationscheme_instantiation(instance):
    assert isinstance(instance, vhdl::statement::IterationScheme)

@given(instance=vhdl::statement::BreakStatementItem_strategy)
@settings(max_examples=50)
def test_vhdl::statement::breakstatementitem_instantiation(instance):
    assert isinstance(instance, vhdl::statement::BreakStatementItem)

@given(instance=vhdl::statement::Statement_strategy)
@settings(max_examples=50)
def test_vhdl::statement::statement_instantiation(instance):
    assert isinstance(instance, vhdl::statement::Statement)

@given(instance=vhdl::statement::Statement_strategy)
def test_vhdl::statement::statement_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=vhdl::statement::Statement_strategy)
def test_vhdl::statement::statement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=vhdl::statement::GenerationScheme_strategy)
@settings(max_examples=50)
def test_vhdl::statement::generationscheme_instantiation(instance):
    assert isinstance(instance, vhdl::statement::GenerationScheme)

@given(instance=vhdl::declaration::SubprogramBody_strategy)
@settings(max_examples=50)
def test_vhdl::declaration::subprogrambody_instantiation(instance):
    assert isinstance(instance, vhdl::declaration::SubprogramBody)

@given(instance=vhdl::ams::SourceAspect_strategy)
@settings(max_examples=50)
def test_vhdl::ams::sourceaspect_instantiation(instance):
    assert isinstance(instance, vhdl::ams::SourceAspect)

@given(instance=vhdl::Signature_strategy)
@settings(max_examples=50)
def test_vhdl::signature_instantiation(instance):
    assert isinstance(instance, vhdl::Signature)

@given(instance=vhdl::type::RecordTypeElement_strategy)
@settings(max_examples=50)
def test_vhdl::type::recordtypeelement_instantiation(instance):
    assert isinstance(instance, vhdl::type::RecordTypeElement)

@given(instance=vhdl::configuration::ConfigurationItem_strategy)
@settings(max_examples=50)
def test_vhdl::configuration::configurationitem_instantiation(instance):
    assert isinstance(instance, vhdl::configuration::ConfigurationItem)

@given(instance=vhdl::EntityResolvedReference_strategy)
@settings(max_examples=50)
def test_vhdl::entityresolvedreference_instantiation(instance):
    assert isinstance(instance, vhdl::EntityResolvedReference)

@given(instance=vhdl::Generics_strategy)
@settings(max_examples=50)
def test_vhdl::generics_instantiation(instance):
    assert isinstance(instance, vhdl::Generics)

@given(instance=vhdl::PortMaps_strategy)
@settings(max_examples=50)
def test_vhdl::portmaps_instantiation(instance):
    assert isinstance(instance, vhdl::PortMaps)

@given(instance=vhdl::type::TypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl::type::typedefinition_instantiation(instance):
    assert isinstance(instance, vhdl::type::TypeDefinition)

@given(instance=vhdl::Model_strategy)
@settings(max_examples=50)
def test_vhdl::model_instantiation(instance):
    assert isinstance(instance, vhdl::Model)

@given(instance=vhdl::statement::IfStatementTest_strategy)
@settings(max_examples=50)
def test_vhdl::statement::ifstatementtest_instantiation(instance):
    assert isinstance(instance, vhdl::statement::IfStatementTest)

@given(instance=vhdl::PackageResolvedReference_strategy)
@settings(max_examples=50)
def test_vhdl::packageresolvedreference_instantiation(instance):
    assert isinstance(instance, vhdl::PackageResolvedReference)

@given(instance=vhdl::NameList_strategy)
@settings(max_examples=50)
def test_vhdl::namelist_instantiation(instance):
    assert isinstance(instance, vhdl::NameList)

@given(instance=vhdl::ComponentResolvedReference_strategy)
@settings(max_examples=50)
def test_vhdl::componentresolvedreference_instantiation(instance):
    assert isinstance(instance, vhdl::ComponentResolvedReference)

@given(instance=vhdl::Module_strategy)
@settings(max_examples=50)
def test_vhdl::module_instantiation(instance):
    assert isinstance(instance, vhdl::Module)

@given(instance=vhdl::statement::CaseAlternative_strategy)
@settings(max_examples=50)
def test_vhdl::statement::casealternative_instantiation(instance):
    assert isinstance(instance, vhdl::statement::CaseAlternative)

@given(instance=vhdl::ams::QuantityAspect_strategy)
@settings(max_examples=50)
def test_vhdl::ams::quantityaspect_instantiation(instance):
    assert isinstance(instance, vhdl::ams::QuantityAspect)

@given(instance=vhdl::GenericMaps_strategy)
@settings(max_examples=50)
def test_vhdl::genericmaps_instantiation(instance):
    assert isinstance(instance, vhdl::GenericMaps)

@given(instance=vhdl::nature::RecordNatureElement_strategy)
@settings(max_examples=50)
def test_vhdl::nature::recordnatureelement_instantiation(instance):
    assert isinstance(instance, vhdl::nature::RecordNatureElement)

@given(instance=vhdl::configuration::ConfigurationResolvedReference_strategy)
@settings(max_examples=50)
def test_vhdl::configuration::configurationresolvedreference_instantiation(instance):
    assert isinstance(instance, vhdl::configuration::ConfigurationResolvedReference)

@given(instance=vhdl::Ports_strategy)
@settings(max_examples=50)
def test_vhdl::ports_instantiation(instance):
    assert isinstance(instance, vhdl::Ports)

@given(instance=vhdl::nature::NatureDefinition_strategy)
@settings(max_examples=50)
def test_vhdl::nature::naturedefinition_instantiation(instance):
    assert isinstance(instance, vhdl::nature::NatureDefinition)

@given(instance=vhdl::DesignUnit_strategy)
@settings(max_examples=50)
def test_vhdl::designunit_instantiation(instance):
    assert isinstance(instance, vhdl::DesignUnit)

@given(instance=vhdl::DesignUnit_strategy)
def test_vhdl::designunit_library_type(instance):
    assert isinstance(instance.library, str)


@given(instance=vhdl::DesignUnit_strategy)
def test_vhdl::designunit_library_setter(instance):
    original = instance.library
    instance.library = original
    assert instance.library == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=vhdl::statement::ExitStatement_strategy)
@settings(max_examples=50)
def test_vhdl::statement::exitstatement_instantiation(instance):
    assert isinstance(instance, vhdl::statement::ExitStatement)

@given(instance=vhdl::statement::ExitStatement_strategy)
def test_vhdl::statement::exitstatement_exit_type(instance):
    assert isinstance(instance.exit, str)


@given(instance=vhdl::statement::ExitStatement_strategy)
def test_vhdl::statement::exitstatement_exit_setter(instance):
    original = instance.exit
    instance.exit = original
    assert instance.exit == original

@given(instance=vhdl::statement::SimultaneousProceduralStatement_strategy)
@settings(max_examples=50)
def test_vhdl::statement::simultaneousproceduralstatement_instantiation(instance):
    assert isinstance(instance, vhdl::statement::SimultaneousProceduralStatement)

@given(instance=vhdl::statement::InstantiationStatement_strategy)
@settings(max_examples=50)
def test_vhdl::statement::instantiationstatement_instantiation(instance):
    assert isinstance(instance, vhdl::statement::InstantiationStatement)

@given(instance=vhdl::statement::WaitStatement_strategy)
@settings(max_examples=50)
def test_vhdl::statement::waitstatement_instantiation(instance):
    assert isinstance(instance, vhdl::statement::WaitStatement)

@given(instance=vhdl::statement::BlockStatement_strategy)
@settings(max_examples=50)
def test_vhdl::statement::blockstatement_instantiation(instance):
    assert isinstance(instance, vhdl::statement::BlockStatement)

@given(instance=vhdl::statement::NextStatement_strategy)
@settings(max_examples=50)
def test_vhdl::statement::nextstatement_instantiation(instance):
    assert isinstance(instance, vhdl::statement::NextStatement)

@given(instance=vhdl::statement::NextStatement_strategy)
def test_vhdl::statement::nextstatement_next_type(instance):
    assert isinstance(instance.next, str)


@given(instance=vhdl::statement::NextStatement_strategy)
def test_vhdl::statement::nextstatement_next_setter(instance):
    original = instance.next
    instance.next = original
    assert instance.next == original

@given(instance=vhdl::statement::ProcessStatement_strategy)
@settings(max_examples=50)
def test_vhdl::statement::processstatement_instantiation(instance):
    assert isinstance(instance, vhdl::statement::ProcessStatement)

@given(instance=vhdl::statement::ProcessStatement_strategy)
def test_vhdl::statement::processstatement_postponed_type(instance):
    assert isinstance(instance.postponed, bool)


@given(instance=vhdl::statement::ProcessStatement_strategy)
def test_vhdl::statement::processstatement_postponed_setter(instance):
    original = instance.postponed
    instance.postponed = original
    assert instance.postponed == original

@given(instance=vhdl::statement::LoopStatement_strategy)
@settings(max_examples=50)
def test_vhdl::statement::loopstatement_instantiation(instance):
    assert isinstance(instance, vhdl::statement::LoopStatement)

@given(instance=vhdl::statement::ProcedureCallStatement_strategy)
@settings(max_examples=50)
def test_vhdl::statement::procedurecallstatement_instantiation(instance):
    assert isinstance(instance, vhdl::statement::ProcedureCallStatement)

@given(instance=vhdl::statement::ProcedureCallStatement_strategy)
def test_vhdl::statement::procedurecallstatement_postponed_type(instance):
    assert isinstance(instance.postponed, bool)


@given(instance=vhdl::statement::ProcedureCallStatement_strategy)
def test_vhdl::statement::procedurecallstatement_postponed_setter(instance):
    original = instance.postponed
    instance.postponed = original
    assert instance.postponed == original

@given(instance=vhdl::statement::ReportStatement_strategy)
@settings(max_examples=50)
def test_vhdl::statement::reportstatement_instantiation(instance):
    assert isinstance(instance, vhdl::statement::ReportStatement)

@given(instance=vhdl::statement::BreakStatement_strategy)
@settings(max_examples=50)
def test_vhdl::statement::breakstatement_instantiation(instance):
    assert isinstance(instance, vhdl::statement::BreakStatement)

@given(instance=vhdl::statement::AssertionStatement_strategy)
@settings(max_examples=50)
def test_vhdl::statement::assertionstatement_instantiation(instance):
    assert isinstance(instance, vhdl::statement::AssertionStatement)

@given(instance=vhdl::statement::AssertionStatement_strategy)
def test_vhdl::statement::assertionstatement_postponed_type(instance):
    assert isinstance(instance.postponed, bool)


@given(instance=vhdl::statement::AssertionStatement_strategy)
def test_vhdl::statement::assertionstatement_postponed_setter(instance):
    original = instance.postponed
    instance.postponed = original
    assert instance.postponed == original

@given(instance=vhdl::statement::IfStatement_strategy)
@settings(max_examples=50)
def test_vhdl::statement::ifstatement_instantiation(instance):
    assert isinstance(instance, vhdl::statement::IfStatement)

@given(instance=vhdl::statement::VariableAssignmentStatement_strategy)
@settings(max_examples=50)
def test_vhdl::statement::variableassignmentstatement_instantiation(instance):
    assert isinstance(instance, vhdl::statement::VariableAssignmentStatement)

@given(instance=vhdl::statement::SignalAssignmentStatement_strategy)
@settings(max_examples=50)
def test_vhdl::statement::signalassignmentstatement_instantiation(instance):
    assert isinstance(instance, vhdl::statement::SignalAssignmentStatement)

@given(instance=vhdl::statement::SignalAssignmentStatement_strategy)
def test_vhdl::statement::signalassignmentstatement_postponed_type(instance):
    assert isinstance(instance.postponed, bool)


@given(instance=vhdl::statement::SignalAssignmentStatement_strategy)
def test_vhdl::statement::signalassignmentstatement_postponed_setter(instance):
    original = instance.postponed
    instance.postponed = original
    assert instance.postponed == original

@given(instance=vhdl::statement::SignalAssignmentStatement_strategy)
def test_vhdl::statement::signalassignmentstatement_guarded_type(instance):
    assert isinstance(instance.guarded, bool)


@given(instance=vhdl::statement::SignalAssignmentStatement_strategy)
def test_vhdl::statement::signalassignmentstatement_guarded_setter(instance):
    original = instance.guarded
    instance.guarded = original
    assert instance.guarded == original

@given(instance=vhdl::statement::CaseStatement_strategy)
@settings(max_examples=50)
def test_vhdl::statement::casestatement_instantiation(instance):
    assert isinstance(instance, vhdl::statement::CaseStatement)

@given(instance=vhdl::statement::GenerateStatement_strategy)
@settings(max_examples=50)
def test_vhdl::statement::generatestatement_instantiation(instance):
    assert isinstance(instance, vhdl::statement::GenerateStatement)

@given(instance=vhdl::statement::SimpleSimultaneousStatement_strategy)
@settings(max_examples=50)
def test_vhdl::statement::simplesimultaneousstatement_instantiation(instance):
    assert isinstance(instance, vhdl::statement::SimpleSimultaneousStatement)

@given(instance=vhdl::EntityReference_strategy)
@settings(max_examples=50)
def test_vhdl::entityreference_instantiation(instance):
    assert isinstance(instance, vhdl::EntityReference)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=vhdl::declaration::AttributeSpecification_strategy)
@settings(max_examples=50)
def test_vhdl::declaration::attributespecification_instantiation(instance):
    assert isinstance(instance, vhdl::declaration::AttributeSpecification)

@given(instance=vhdl::declaration::AttributeSpecification_strategy)
def test_vhdl::declaration::attributespecification_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=vhdl::declaration::AttributeSpecification_strategy)
def test_vhdl::declaration::attributespecification_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=vhdl::declaration::GroupDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl::declaration::groupdeclaration_instantiation(instance):
    assert isinstance(instance, vhdl::declaration::GroupDeclaration)

@given(instance=vhdl::declaration::SubnatureDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl::declaration::subnaturedeclaration_instantiation(instance):
    assert isinstance(instance, vhdl::declaration::SubnatureDeclaration)

@given(instance=vhdl::declaration::NatureDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl::declaration::naturedeclaration_instantiation(instance):
    assert isinstance(instance, vhdl::declaration::NatureDeclaration)

@given(instance=vhdl::declaration::SubprogramDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl::declaration::subprogramdeclaration_instantiation(instance):
    assert isinstance(instance, vhdl::declaration::SubprogramDeclaration)

@given(instance=vhdl::Component_strategy)
@settings(max_examples=50)
def test_vhdl::component_instantiation(instance):
    assert isinstance(instance, vhdl::Component)

@given(instance=vhdl::declaration::AttributeDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl::declaration::attributedeclaration_instantiation(instance):
    assert isinstance(instance, vhdl::declaration::AttributeDeclaration)

@given(instance=vhdl::configuration::BlockConfiguration_strategy)
@settings(max_examples=50)
def test_vhdl::configuration::blockconfiguration_instantiation(instance):
    assert isinstance(instance, vhdl::configuration::BlockConfiguration)

@given(instance=vhdl::declaration::SubtypeDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl::declaration::subtypedeclaration_instantiation(instance):
    assert isinstance(instance, vhdl::declaration::SubtypeDeclaration)

@given(instance=vhdl::declaration::AliasDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl::declaration::aliasdeclaration_instantiation(instance):
    assert isinstance(instance, vhdl::declaration::AliasDeclaration)

@given(instance=vhdl::declaration::GroupTemplateDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl::declaration::grouptemplatedeclaration_instantiation(instance):
    assert isinstance(instance, vhdl::declaration::GroupTemplateDeclaration)

@given(instance=vhdl::declaration::GroupTemplateDeclaration_strategy)
def test_vhdl::declaration::grouptemplatedeclaration_entry_type(instance):
    assert isinstance(instance.entry, str)


@given(instance=vhdl::declaration::GroupTemplateDeclaration_strategy)
def test_vhdl::declaration::grouptemplatedeclaration_entry_setter(instance):
    original = instance.entry
    instance.entry = original
    assert instance.entry == original

@given(instance=vhdl::declaration::TypeDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl::declaration::typedeclaration_instantiation(instance):
    assert isinstance(instance, vhdl::declaration::TypeDeclaration)

@given(instance=Module_strategy)
@settings(max_examples=50)
def test_module_instantiation(instance):
    assert isinstance(instance, Module)

@given(instance=vhdl::Entity_strategy)
@settings(max_examples=50)
def test_vhdl::entity_instantiation(instance):
    assert isinstance(instance, vhdl::Entity)

@given(instance=vhdl::configuration::Configuration_strategy)
@settings(max_examples=50)
def test_vhdl::configuration::configuration_instantiation(instance):
    assert isinstance(instance, vhdl::configuration::Configuration)

@given(instance=vhdl::Package_strategy)
@settings(max_examples=50)
def test_vhdl::package_instantiation(instance):
    assert isinstance(instance, vhdl::Package)

@given(instance=vhdl::PackageBody_strategy)
@settings(max_examples=50)
def test_vhdl::packagebody_instantiation(instance):
    assert isinstance(instance, vhdl::PackageBody)

@given(instance=vhdl::Architecture_strategy)
@settings(max_examples=50)
def test_vhdl::architecture_instantiation(instance):
    assert isinstance(instance, vhdl::Architecture)

@given(instance=vhdl::expression::CharacterExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::characterexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::CharacterExpression)

@given(instance=vhdl::expression::StringExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::stringexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::StringExpression)

@given(instance=expression::BinaryExpression_strategy)
@settings(max_examples=50)
def test_expression::binaryexpression_instantiation(instance):
    assert isinstance(instance, expression::BinaryExpression)

@given(instance=vhdl::expression::RangeExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::rangeexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::RangeExpression)

@given(instance=vhdl::expression::RangeExpression_strategy)
def test_vhdl::expression::rangeexpression_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=vhdl::expression::RangeExpression_strategy)
def test_vhdl::expression::rangeexpression_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=vhdl::expression::OthersExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::othersexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::OthersExpression)

@given(instance=vhdl::expression::OpenExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::openexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::OpenExpression)

@given(instance=vhdl::expression::UnaryExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::unaryexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::UnaryExpression)

@given(instance=vhdl::expression::UnaryExpression_strategy)
def test_vhdl::expression::unaryexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=vhdl::expression::UnaryExpression_strategy)
def test_vhdl::expression::unaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=vhdl::expression::SignExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::signexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::SignExpression)

@given(instance=vhdl::expression::SignExpression_strategy)
def test_vhdl::expression::signexpression_sign_type(instance):
    assert isinstance(instance.sign, str)


@given(instance=vhdl::expression::SignExpression_strategy)
def test_vhdl::expression::signexpression_sign_setter(instance):
    original = instance.sign
    instance.sign = original
    assert instance.sign == original

@given(instance=vhdl::expression::SignatureExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::signatureexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::SignatureExpression)

@given(instance=vhdl::expression::ShiftExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::shiftexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::ShiftExpression)

@given(instance=vhdl::expression::ShiftExpression_strategy)
def test_vhdl::expression::shiftexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=vhdl::expression::ShiftExpression_strategy)
def test_vhdl::expression::shiftexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=vhdl::expression::BinaryExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::binaryexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::BinaryExpression)

@given(instance=expression::vhdl::Name_strategy)
@settings(max_examples=50)
def test_expression::vhdl::name_instantiation(instance):
    assert isinstance(instance, expression::vhdl::Name)

@given(instance=vhdl::expression::NameExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::nameexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::NameExpression)

@given(instance=vhdl::expression::LogicalExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::logicalexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::LogicalExpression)

@given(instance=vhdl::expression::LogicalExpression_strategy)
def test_vhdl::expression::logicalexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=vhdl::expression::LogicalExpression_strategy)
def test_vhdl::expression::logicalexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=NatureReference_strategy)
@settings(max_examples=50)
def test_naturereference_instantiation(instance):
    assert isinstance(instance, NatureReference)

@given(instance=expression::IndicationExpression_strategy)
@settings(max_examples=50)
def test_expression::indicationexpression_instantiation(instance):
    assert isinstance(instance, expression::IndicationExpression)

@given(instance=vhdl::expression::SubnatureIndicationExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::subnatureindicationexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::SubnatureIndicationExpression)

@given(instance=vhdl::expression::SubtypeIndicationExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::subtypeindicationexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::SubtypeIndicationExpression)

@given(instance=vhdl::expression::IndicationExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::indicationexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::IndicationExpression)

@given(instance=vhdl::expression::Expression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::expression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::Expression)

@given(instance=ValueExpression_strategy)
@settings(max_examples=50)
def test_valueexpression_instantiation(instance):
    assert isinstance(instance, ValueExpression)

@given(instance=vhdl::expression::UnitValueExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::unitvalueexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::UnitValueExpression)

@given(instance=vhdl::expression::BitStringExpression_strategy)
@settings(max_examples=50)
def test_vhdl::expression::bitstringexpression_instantiation(instance):
    assert isinstance(instance, vhdl::expression::BitStringExpression)

@given(instance=vhdl::statement::ForGenerationScheme_strategy)
@settings(max_examples=50)
def test_vhdl::statement::forgenerationscheme_instantiation(instance):
    assert isinstance(instance, vhdl::statement::ForGenerationScheme)

@given(instance=vhdl::statement::ForGenerationScheme_strategy)
def test_vhdl::statement::forgenerationscheme_variable_type(instance):
    assert isinstance(instance.variable, str)


@given(instance=vhdl::statement::ForGenerationScheme_strategy)
def test_vhdl::statement::forgenerationscheme_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=vhdl::statement::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_vhdl::statement::expressionstatement_instantiation(instance):
    assert isinstance(instance, vhdl::statement::ExpressionStatement)

@given(instance=vhdl::statement::DelayMechanism_strategy)
@settings(max_examples=50)
def test_vhdl::statement::delaymechanism_instantiation(instance):
    assert isinstance(instance, vhdl::statement::DelayMechanism)

@given(instance=expression::vhdl::Signature_strategy)
@settings(max_examples=50)
def test_expression::vhdl::signature_instantiation(instance):
    assert isinstance(instance, expression::vhdl::Signature)
