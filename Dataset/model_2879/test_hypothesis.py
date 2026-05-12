import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Configuration,
    vhdl_configuration_ConfigurationReference,
    configuration_vhdl_EntityReference,
    BlockConfiguration,
    configuration_vhdl_PortMaps,
    configuration_vhdl_GenericMaps,
    configuration_vhdl_MultiName,
    ConfigurationItem,
    vhdl_configuration_ComponentConfiguration,
    configuration_vhdl_Name,
    configuration_ConfigurationItem,
    nature_CompositeNatureDefinition,
    vhdl_type_TypeReference,
    vhdl_type_Typed,
    vhdl_nature_Natured,
    vhdl_nature_NatureReference,
    nature_vhdl_Name,
    RecordNatureElement,
    CompositeNatureDefinition,
    vhdl_nature_RecordNatureDefinition,
    ArrayNatureDefinition,
    vhdl_nature_UnconstrainedArrayNatureDefinition,
    vhdl_nature_ConstrainedArrayNatureDefinition,
    type_vhdl_Name,
    vhdl_type_PhysicalTypeDefinitionSecondary,
    PhysicalTypeDefinitionSecondary,
    EnumerationLiteral,
    vhdl_type_EnumerationLiteral,
    ArrayTypeDefinition,
    vhdl_type_UnconstrainedArrayTypeDefinition,
    vhdl_type_ConstrainedArrayTypeDefinition,
    type_CompositeTypeDefinition,
    RecordTypeElement,
    CompositeTypeDefinition,
    vhdl_type_RecordTypeDefinition,
    type_TypeDefinition,
    TypeDefinition,
    vhdl_type_EnumerationTypeDefinition,
    vhdl_type_PhysicalTypeDefinition,
    vhdl_type_RangeTypeDefinition,
    vhdl_type_CompositeTypeDefinition,
    NatureDefinition,
    vhdl_nature_CompositeNatureDefinition,
    vhdl_nature_ScalarNatureDefinition,
    ValueDeclaration,
    vhdl_declaration_SignalDeclaration,
    vhdl_declaration_VariableDeclaration,
    vhdl_declaration_ConstantDeclaration,
    SubprogramBody,
    declaration_vhdl_PortMaps,
    declaration_vhdl_GenericMaps,
    declaration_vhdl_EntityReference,
    declaration_vhdl_ComponentReference,
    declaration_SubprogramDeclaration,
    nature_Natured,
    vhdl_nature_ArrayNatureDefinition,
    SourceAspect,
    vhdl_ams_Noise,
    vhdl_ams_Spectrum,
    MultiNamed,
    declaration_QuantityDeclaration,
    QuantityAspect,
    QuantityDeclaration,
    vhdl_declaration_BranchQuantityDeclaration,
    declaration_vhdl_MultiName,
    declaration_vhdl_Name,
    AssociationExpression,
    vhdl_expression_ConditionalWaveformExpression,
    type_EnumerationLiteral,
    expression_BinaryExpression,
    expression_vhdl_Name,
    NatureReference,
    expression_IndicationExpression,
    ValueExpression,
    vhdl_expression_UnitValueExpression,
    vhdl_expression_BitStringExpression,
    expression_vhdl_Signature,
    expression_ValueExpression,
    type_Typed,
    vhdl_declaration_FunctionDeclaration,
    vhdl_type_FileTypeDefinition,
    vhdl_declaration_FreeQuantityDeclaration,
    vhdl_declaration_SourceQuantityDeclaration,
    vhdl_type_AccessTypeDefinition,
    vhdl_type_ArrayTypeDefinition,
    expression_Expression,
    vhdl_expression_AllocatorExpression,
    Name,
    vhdl_expression_CharacterExpression,
    vhdl_expression_RangeExpression,
    vhdl_expression_AllExpression,
    vhdl_expression_NameExpression,
    vhdl_expression_TypeQualificationExpression,
    vhdl_expression_IdentifierExpression,
    vhdl_expression_AttributeExpression,
    vhdl_expression_SignatureExpression,
    vhdl_expression_StringExpression,
    vhdl_expression_OthersExpression,
    expression_MultiExpression,
    vhdl_expression_AggregateExpression,
    BinaryExpression,
    vhdl_expression_LogicalExpression,
    vhdl_expression_MultiplyingExpression,
    vhdl_expression_ShiftExpression,
    vhdl_expression_RelationalExpression,
    vhdl_expression_PowerExpression,
    vhdl_expression_AddingExpression,
    ConfigurationReference,
    statement_vhdl_EntityReference,
    IterationScheme,
    vhdl_statement_WhileIterationScheme,
    vhdl_statement_ForIterationScheme,
    GenerationScheme,
    vhdl_statement_ForGenerationScheme,
    vhdl_statement_IfGenerationScheme,
    statement_vhdl_ComponentReference,
    InstantiationStatement,
    vhdl_statement_ConfigurationInstantiationStatement,
    vhdl_statement_EntityInstantiationStatement,
    vhdl_statement_ComponentInstantiationStatement,
    statement_vhdl_Name,
    BreakStatementItem,
    statement_vhdl_PortMaps,
    statement_vhdl_Ports,
    statement_vhdl_GenericMaps,
    statement_vhdl_Generics,
    CaseAlternative,
    CaseStatement,
    vhdl_statement_SimultaneousCaseStatement,
    statement_vhdl_CallReference,
    IfStatementTest,
    IfStatement,
    vhdl_statement_SimultaneousIfStatement,
    vhdl_ComponentReference,
    statement_vhdl_MultiName,
    DelayMechanism,
    vhdl_statement_TransportMechanism,
    vhdl_statement_RejectMechanism,
    ConditionalSignalAssignmentStatement,
    vhdl_statement_SelectedSignalAssignmentStatement,
    SignalAssignmentStatement,
    vhdl_statement_SequentialSignalAssignmentStatement,
    vhdl_statement_ConditionalSignalAssignmentStatement,
    ExpressionStatement,
    vhdl_statement_ReturnStatement,
    SubprogramDeclaration,
    vhdl_declaration_ProcedureDeclaration,
    vhdl_CallReference,
    vhdl_VhdlObject,
    vhdl_MultiName,
    vhdl_MultiNamed,
    vhdl_Named,
    CallReference,
    vhdl_CallResolvedReference,
    configuration_ConfigurationReference,
    ComponentReference,
    PackageReference,
    EntityReference,
    nature_NatureReference,
    vhdl_expression_SubnatureIndicationExpression,
    type_TypeReference,
    MultiName,
    declaration_Declaration,
    vhdl_declaration_DisconnectionSpecification,
    vhdl_declaration_FileDeclaration,
    vhdl_declaration_TerminalDeclaration,
    vhdl_declaration_ValueDeclaration,
    vhdl_declaration_LimitDeclaration,
    TypeReference,
    vhdl_PackageReference,
    Expression,
    vhdl_expression_UnaryExpression,
    vhdl_expression_NullExpression,
    vhdl_expression_BinaryExpression,
    vhdl_expression_OpenExpression,
    vhdl_expression_WaveformExpression,
    vhdl_expression_ValueExpression,
    vhdl_expression_SignExpression,
    vhdl_expression_MultiExpression,
    vhdl_expression_IndicationExpression,
    vhdl_expression_AssociationExpression,
    vhdl_expression_UnaffectedExpression,
    Declaration,
    vhdl_declaration_QuantityDeclaration,
    vhdl_declaration_ConfigurationSpecification,
    vhdl_declaration_UseClauseDeclaration,
    vhdl_Name,
    VhdlObject,
    vhdl_type_TypeDefinition,
    vhdl_statement_IterationScheme,
    vhdl_Module,
    vhdl_declaration_Declaration,
    vhdl_EntityResolvedReference,
    vhdl_Generics,
    vhdl_configuration_ConfigurationItem,
    vhdl_type_RecordTypeElement,
    vhdl_statement_CaseAlternative,
    vhdl_Signature,
    vhdl_statement_BreakStatementItem,
    vhdl_statement_Statement,
    vhdl_nature_NatureDefinition,
    vhdl_GenericMaps,
    vhdl_NameList,
    vhdl_Ports,
    vhdl_statement_DelayMechanism,
    vhdl_declaration_SubprogramBody,
    vhdl_ams_SourceAspect,
    vhdl_Model,
    vhdl_PortMaps,
    vhdl_statement_IfStatementTest,
    vhdl_nature_RecordNatureElement,
    vhdl_expression_Expression,
    vhdl_ams_QuantityAspect,
    vhdl_statement_GenerationScheme,
    vhdl_ComponentResolvedReference,
    vhdl_PackageResolvedReference,
    vhdl_configuration_ConfigurationResolvedReference,
    vhdl_DesignUnit,
    Statement,
    vhdl_statement_CaseStatement,
    vhdl_statement_LoopStatement,
    vhdl_statement_SignalAssignmentStatement,
    vhdl_statement_SimpleSimultaneousStatement,
    vhdl_statement_ProcedureCallStatement,
    vhdl_statement_ReportStatement,
    vhdl_statement_InstantiationStatement,
    vhdl_statement_ProcessStatement,
    vhdl_statement_VariableAssignmentStatement,
    vhdl_statement_ExpressionStatement,
    vhdl_statement_BlockStatement,
    vhdl_statement_ExitStatement,
    vhdl_statement_NextStatement,
    vhdl_statement_WaitStatement,
    vhdl_statement_IfStatement,
    vhdl_statement_SimultaneousProceduralStatement,
    vhdl_statement_GenerateStatement,
    vhdl_statement_BreakStatement,
    vhdl_statement_AssertionStatement,
    vhdl_EntityReference,
    Named,
    vhdl_declaration_AttributeSpecification,
    vhdl_declaration_GroupDeclaration,
    vhdl_declaration_SubprogramDeclaration,
    vhdl_declaration_TypeDeclaration,
    vhdl_expression_SubtypeIndicationExpression,
    vhdl_declaration_AliasDeclaration,
    vhdl_configuration_BlockConfiguration,
    vhdl_declaration_NatureDeclaration,
    vhdl_declaration_SubtypeDeclaration,
    vhdl_declaration_SubnatureDeclaration,
    vhdl_declaration_AttributeDeclaration,
    vhdl_Component,
    vhdl_declaration_GroupTemplateDeclaration,
    Module,
    vhdl_Entity,
    vhdl_configuration_Configuration,
    vhdl_Package,
    vhdl_PackageBody,
    vhdl_Architecture,
    MultiplyingOperator,
    RelationalOperator,
    ShiftOperator,
    LogicalOperator,
    SignalKind,
    AddingOperator,
    RangeDirection,
    Mode,
    UnaryOperator,
    Sign,
    Purity,
    EntityClass,
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



def test_vhdl_configuration_configurationreference_is_not_abstract():
    assert not inspect.isabstract(vhdl_configuration_ConfigurationReference)


def test_vhdl_configuration_configurationreference_constructor_exists():
    assert callable(vhdl_configuration_ConfigurationReference.__init__)


def test_vhdl_configuration_configurationreference_constructor_args():
    sig = inspect.signature(vhdl_configuration_ConfigurationReference.__init__)
    params = list(sig.parameters.keys())



def test_configuration_vhdl_entityreference_is_not_abstract():
    assert not inspect.isabstract(configuration_vhdl_EntityReference)


def test_configuration_vhdl_entityreference_constructor_exists():
    assert callable(configuration_vhdl_EntityReference.__init__)


def test_configuration_vhdl_entityreference_constructor_args():
    sig = inspect.signature(configuration_vhdl_EntityReference.__init__)
    params = list(sig.parameters.keys())



def test_blockconfiguration_is_not_abstract():
    assert not inspect.isabstract(BlockConfiguration)


def test_blockconfiguration_constructor_exists():
    assert callable(BlockConfiguration.__init__)


def test_blockconfiguration_constructor_args():
    sig = inspect.signature(BlockConfiguration.__init__)
    params = list(sig.parameters.keys())



def test_configuration_vhdl_portmaps_is_not_abstract():
    assert not inspect.isabstract(configuration_vhdl_PortMaps)


def test_configuration_vhdl_portmaps_constructor_exists():
    assert callable(configuration_vhdl_PortMaps.__init__)


def test_configuration_vhdl_portmaps_constructor_args():
    sig = inspect.signature(configuration_vhdl_PortMaps.__init__)
    params = list(sig.parameters.keys())



def test_configuration_vhdl_genericmaps_is_not_abstract():
    assert not inspect.isabstract(configuration_vhdl_GenericMaps)


def test_configuration_vhdl_genericmaps_constructor_exists():
    assert callable(configuration_vhdl_GenericMaps.__init__)


def test_configuration_vhdl_genericmaps_constructor_args():
    sig = inspect.signature(configuration_vhdl_GenericMaps.__init__)
    params = list(sig.parameters.keys())



def test_configuration_vhdl_multiname_is_not_abstract():
    assert not inspect.isabstract(configuration_vhdl_MultiName)


def test_configuration_vhdl_multiname_constructor_exists():
    assert callable(configuration_vhdl_MultiName.__init__)


def test_configuration_vhdl_multiname_constructor_args():
    sig = inspect.signature(configuration_vhdl_MultiName.__init__)
    params = list(sig.parameters.keys())



def test_configurationitem_is_not_abstract():
    assert not inspect.isabstract(ConfigurationItem)


def test_configurationitem_constructor_exists():
    assert callable(ConfigurationItem.__init__)


def test_configurationitem_constructor_args():
    sig = inspect.signature(ConfigurationItem.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_configuration_componentconfiguration_is_not_abstract():
    assert not inspect.isabstract(vhdl_configuration_ComponentConfiguration)


def test_vhdl_configuration_componentconfiguration_constructor_exists():
    assert callable(vhdl_configuration_ComponentConfiguration.__init__)


def test_vhdl_configuration_componentconfiguration_constructor_args():
    sig = inspect.signature(vhdl_configuration_ComponentConfiguration.__init__)
    params = list(sig.parameters.keys())



def test_configuration_vhdl_name_is_not_abstract():
    assert not inspect.isabstract(configuration_vhdl_Name)


def test_configuration_vhdl_name_constructor_exists():
    assert callable(configuration_vhdl_Name.__init__)


def test_configuration_vhdl_name_constructor_args():
    sig = inspect.signature(configuration_vhdl_Name.__init__)
    params = list(sig.parameters.keys())



def test_configuration_configurationitem_is_not_abstract():
    assert not inspect.isabstract(configuration_ConfigurationItem)


def test_configuration_configurationitem_constructor_exists():
    assert callable(configuration_ConfigurationItem.__init__)


def test_configuration_configurationitem_constructor_args():
    sig = inspect.signature(configuration_ConfigurationItem.__init__)
    params = list(sig.parameters.keys())



def test_nature_compositenaturedefinition_is_not_abstract():
    assert not inspect.isabstract(nature_CompositeNatureDefinition)


def test_nature_compositenaturedefinition_constructor_exists():
    assert callable(nature_CompositeNatureDefinition.__init__)


def test_nature_compositenaturedefinition_constructor_args():
    sig = inspect.signature(nature_CompositeNatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_type_typereference_is_not_abstract():
    assert not inspect.isabstract(vhdl_type_TypeReference)


def test_vhdl_type_typereference_constructor_exists():
    assert callable(vhdl_type_TypeReference.__init__)


def test_vhdl_type_typereference_constructor_args():
    sig = inspect.signature(vhdl_type_TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_type_typed_is_not_abstract():
    assert not inspect.isabstract(vhdl_type_Typed)


def test_vhdl_type_typed_constructor_exists():
    assert callable(vhdl_type_Typed.__init__)


def test_vhdl_type_typed_constructor_args():
    sig = inspect.signature(vhdl_type_Typed.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_nature_natured_is_not_abstract():
    assert not inspect.isabstract(vhdl_nature_Natured)


def test_vhdl_nature_natured_constructor_exists():
    assert callable(vhdl_nature_Natured.__init__)


def test_vhdl_nature_natured_constructor_args():
    sig = inspect.signature(vhdl_nature_Natured.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_nature_naturereference_is_not_abstract():
    assert not inspect.isabstract(vhdl_nature_NatureReference)


def test_vhdl_nature_naturereference_constructor_exists():
    assert callable(vhdl_nature_NatureReference.__init__)


def test_vhdl_nature_naturereference_constructor_args():
    sig = inspect.signature(vhdl_nature_NatureReference.__init__)
    params = list(sig.parameters.keys())



def test_nature_vhdl_name_is_not_abstract():
    assert not inspect.isabstract(nature_vhdl_Name)


def test_nature_vhdl_name_constructor_exists():
    assert callable(nature_vhdl_Name.__init__)


def test_nature_vhdl_name_constructor_args():
    sig = inspect.signature(nature_vhdl_Name.__init__)
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



def test_vhdl_nature_recordnaturedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl_nature_RecordNatureDefinition)


def test_vhdl_nature_recordnaturedefinition_constructor_exists():
    assert callable(vhdl_nature_RecordNatureDefinition.__init__)


def test_vhdl_nature_recordnaturedefinition_constructor_args():
    sig = inspect.signature(vhdl_nature_RecordNatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_arraynaturedefinition_is_not_abstract():
    assert not inspect.isabstract(ArrayNatureDefinition)


def test_arraynaturedefinition_constructor_exists():
    assert callable(ArrayNatureDefinition.__init__)


def test_arraynaturedefinition_constructor_args():
    sig = inspect.signature(ArrayNatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_nature_unconstrainedarraynaturedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl_nature_UnconstrainedArrayNatureDefinition)


def test_vhdl_nature_unconstrainedarraynaturedefinition_constructor_exists():
    assert callable(vhdl_nature_UnconstrainedArrayNatureDefinition.__init__)


def test_vhdl_nature_unconstrainedarraynaturedefinition_constructor_args():
    sig = inspect.signature(vhdl_nature_UnconstrainedArrayNatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_nature_constrainedarraynaturedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl_nature_ConstrainedArrayNatureDefinition)


def test_vhdl_nature_constrainedarraynaturedefinition_constructor_exists():
    assert callable(vhdl_nature_ConstrainedArrayNatureDefinition.__init__)


def test_vhdl_nature_constrainedarraynaturedefinition_constructor_args():
    sig = inspect.signature(vhdl_nature_ConstrainedArrayNatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_type_vhdl_name_is_not_abstract():
    assert not inspect.isabstract(type_vhdl_Name)


def test_type_vhdl_name_constructor_exists():
    assert callable(type_vhdl_Name.__init__)


def test_type_vhdl_name_constructor_args():
    sig = inspect.signature(type_vhdl_Name.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_type_physicaltypedefinitionsecondary_is_not_abstract():
    assert not inspect.isabstract(vhdl_type_PhysicalTypeDefinitionSecondary)


def test_vhdl_type_physicaltypedefinitionsecondary_constructor_exists():
    assert callable(vhdl_type_PhysicalTypeDefinitionSecondary.__init__)


def test_vhdl_type_physicaltypedefinitionsecondary_constructor_args():
    sig = inspect.signature(vhdl_type_PhysicalTypeDefinitionSecondary.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"
    assert "name" in params, "Missing parameter 'name'"

def test_vhdl_type_physicaltypedefinitionsecondary_has_number():
    assert hasattr(vhdl_type_PhysicalTypeDefinitionSecondary, "number")
    descriptor = None
    for klass in vhdl_type_PhysicalTypeDefinitionSecondary.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_vhdl_type_physicaltypedefinitionsecondary_has_name():
    assert hasattr(vhdl_type_PhysicalTypeDefinitionSecondary, "name")
    descriptor = None
    for klass in vhdl_type_PhysicalTypeDefinitionSecondary.__mro__:
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



def test_vhdl_type_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(vhdl_type_EnumerationLiteral)


def test_vhdl_type_enumerationliteral_constructor_exists():
    assert callable(vhdl_type_EnumerationLiteral.__init__)


def test_vhdl_type_enumerationliteral_constructor_args():
    sig = inspect.signature(vhdl_type_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_arraytypedefinition_is_not_abstract():
    assert not inspect.isabstract(ArrayTypeDefinition)


def test_arraytypedefinition_constructor_exists():
    assert callable(ArrayTypeDefinition.__init__)


def test_arraytypedefinition_constructor_args():
    sig = inspect.signature(ArrayTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_type_unconstrainedarraytypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl_type_UnconstrainedArrayTypeDefinition)


def test_vhdl_type_unconstrainedarraytypedefinition_constructor_exists():
    assert callable(vhdl_type_UnconstrainedArrayTypeDefinition.__init__)


def test_vhdl_type_unconstrainedarraytypedefinition_constructor_args():
    sig = inspect.signature(vhdl_type_UnconstrainedArrayTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_type_constrainedarraytypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl_type_ConstrainedArrayTypeDefinition)


def test_vhdl_type_constrainedarraytypedefinition_constructor_exists():
    assert callable(vhdl_type_ConstrainedArrayTypeDefinition.__init__)


def test_vhdl_type_constrainedarraytypedefinition_constructor_args():
    sig = inspect.signature(vhdl_type_ConstrainedArrayTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_type_compositetypedefinition_is_not_abstract():
    assert not inspect.isabstract(type_CompositeTypeDefinition)


def test_type_compositetypedefinition_constructor_exists():
    assert callable(type_CompositeTypeDefinition.__init__)


def test_type_compositetypedefinition_constructor_args():
    sig = inspect.signature(type_CompositeTypeDefinition.__init__)
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



def test_vhdl_type_recordtypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl_type_RecordTypeDefinition)


def test_vhdl_type_recordtypedefinition_constructor_exists():
    assert callable(vhdl_type_RecordTypeDefinition.__init__)


def test_vhdl_type_recordtypedefinition_constructor_args():
    sig = inspect.signature(vhdl_type_RecordTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_type_typedefinition_is_not_abstract():
    assert not inspect.isabstract(type_TypeDefinition)


def test_type_typedefinition_constructor_exists():
    assert callable(type_TypeDefinition.__init__)


def test_type_typedefinition_constructor_args():
    sig = inspect.signature(type_TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_typedefinition_is_not_abstract():
    assert not inspect.isabstract(TypeDefinition)


def test_typedefinition_constructor_exists():
    assert callable(TypeDefinition.__init__)


def test_typedefinition_constructor_args():
    sig = inspect.signature(TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_type_enumerationtypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl_type_EnumerationTypeDefinition)


def test_vhdl_type_enumerationtypedefinition_constructor_exists():
    assert callable(vhdl_type_EnumerationTypeDefinition.__init__)


def test_vhdl_type_enumerationtypedefinition_constructor_args():
    sig = inspect.signature(vhdl_type_EnumerationTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_type_physicaltypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl_type_PhysicalTypeDefinition)


def test_vhdl_type_physicaltypedefinition_constructor_exists():
    assert callable(vhdl_type_PhysicalTypeDefinition.__init__)


def test_vhdl_type_physicaltypedefinition_constructor_args():
    sig = inspect.signature(vhdl_type_PhysicalTypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "primary" in params, "Missing parameter 'primary'"

def test_vhdl_type_physicaltypedefinition_has_primary():
    assert hasattr(vhdl_type_PhysicalTypeDefinition, "primary")
    descriptor = None
    for klass in vhdl_type_PhysicalTypeDefinition.__mro__:
        if "primary" in klass.__dict__:
            descriptor = klass.__dict__["primary"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_type_rangetypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl_type_RangeTypeDefinition)


def test_vhdl_type_rangetypedefinition_constructor_exists():
    assert callable(vhdl_type_RangeTypeDefinition.__init__)


def test_vhdl_type_rangetypedefinition_constructor_args():
    sig = inspect.signature(vhdl_type_RangeTypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_vhdl_type_rangetypedefinition_has_direction():
    assert hasattr(vhdl_type_RangeTypeDefinition, "direction")
    descriptor = None
    for klass in vhdl_type_RangeTypeDefinition.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_type_compositetypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl_type_CompositeTypeDefinition)


def test_vhdl_type_compositetypedefinition_constructor_exists():
    assert callable(vhdl_type_CompositeTypeDefinition.__init__)


def test_vhdl_type_compositetypedefinition_constructor_args():
    sig = inspect.signature(vhdl_type_CompositeTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_naturedefinition_is_not_abstract():
    assert not inspect.isabstract(NatureDefinition)


def test_naturedefinition_constructor_exists():
    assert callable(NatureDefinition.__init__)


def test_naturedefinition_constructor_args():
    sig = inspect.signature(NatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_nature_compositenaturedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl_nature_CompositeNatureDefinition)


def test_vhdl_nature_compositenaturedefinition_constructor_exists():
    assert callable(vhdl_nature_CompositeNatureDefinition.__init__)


def test_vhdl_nature_compositenaturedefinition_constructor_args():
    sig = inspect.signature(vhdl_nature_CompositeNatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_nature_scalarnaturedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl_nature_ScalarNatureDefinition)


def test_vhdl_nature_scalarnaturedefinition_constructor_exists():
    assert callable(vhdl_nature_ScalarNatureDefinition.__init__)


def test_vhdl_nature_scalarnaturedefinition_constructor_args():
    sig = inspect.signature(vhdl_nature_ScalarNatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_valuedeclaration_is_not_abstract():
    assert not inspect.isabstract(ValueDeclaration)


def test_valuedeclaration_constructor_exists():
    assert callable(ValueDeclaration.__init__)


def test_valuedeclaration_constructor_args():
    sig = inspect.signature(ValueDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_declaration_signaldeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl_declaration_SignalDeclaration)


def test_vhdl_declaration_signaldeclaration_constructor_exists():
    assert callable(vhdl_declaration_SignalDeclaration.__init__)


def test_vhdl_declaration_signaldeclaration_constructor_args():
    sig = inspect.signature(vhdl_declaration_SignalDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "mode" in params, "Missing parameter 'mode'"

def test_vhdl_declaration_signaldeclaration_has_kind():
    assert hasattr(vhdl_declaration_SignalDeclaration, "kind")
    descriptor = None
    for klass in vhdl_declaration_SignalDeclaration.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_vhdl_declaration_signaldeclaration_has_mode():
    assert hasattr(vhdl_declaration_SignalDeclaration, "mode")
    descriptor = None
    for klass in vhdl_declaration_SignalDeclaration.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_declaration_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl_declaration_VariableDeclaration)


def test_vhdl_declaration_variabledeclaration_constructor_exists():
    assert callable(vhdl_declaration_VariableDeclaration.__init__)


def test_vhdl_declaration_variabledeclaration_constructor_args():
    sig = inspect.signature(vhdl_declaration_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"
    assert "shared" in params, "Missing parameter 'shared'"

def test_vhdl_declaration_variabledeclaration_has_mode():
    assert hasattr(vhdl_declaration_VariableDeclaration, "mode")
    descriptor = None
    for klass in vhdl_declaration_VariableDeclaration.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)

def test_vhdl_declaration_variabledeclaration_has_shared():
    assert hasattr(vhdl_declaration_VariableDeclaration, "shared")
    descriptor = None
    for klass in vhdl_declaration_VariableDeclaration.__mro__:
        if "shared" in klass.__dict__:
            descriptor = klass.__dict__["shared"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_declaration_constantdeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl_declaration_ConstantDeclaration)


def test_vhdl_declaration_constantdeclaration_constructor_exists():
    assert callable(vhdl_declaration_ConstantDeclaration.__init__)


def test_vhdl_declaration_constantdeclaration_constructor_args():
    sig = inspect.signature(vhdl_declaration_ConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_subprogrambody_is_not_abstract():
    assert not inspect.isabstract(SubprogramBody)


def test_subprogrambody_constructor_exists():
    assert callable(SubprogramBody.__init__)


def test_subprogrambody_constructor_args():
    sig = inspect.signature(SubprogramBody.__init__)
    params = list(sig.parameters.keys())



def test_declaration_vhdl_portmaps_is_not_abstract():
    assert not inspect.isabstract(declaration_vhdl_PortMaps)


def test_declaration_vhdl_portmaps_constructor_exists():
    assert callable(declaration_vhdl_PortMaps.__init__)


def test_declaration_vhdl_portmaps_constructor_args():
    sig = inspect.signature(declaration_vhdl_PortMaps.__init__)
    params = list(sig.parameters.keys())



def test_declaration_vhdl_genericmaps_is_not_abstract():
    assert not inspect.isabstract(declaration_vhdl_GenericMaps)


def test_declaration_vhdl_genericmaps_constructor_exists():
    assert callable(declaration_vhdl_GenericMaps.__init__)


def test_declaration_vhdl_genericmaps_constructor_args():
    sig = inspect.signature(declaration_vhdl_GenericMaps.__init__)
    params = list(sig.parameters.keys())



def test_declaration_vhdl_entityreference_is_not_abstract():
    assert not inspect.isabstract(declaration_vhdl_EntityReference)


def test_declaration_vhdl_entityreference_constructor_exists():
    assert callable(declaration_vhdl_EntityReference.__init__)


def test_declaration_vhdl_entityreference_constructor_args():
    sig = inspect.signature(declaration_vhdl_EntityReference.__init__)
    params = list(sig.parameters.keys())



def test_declaration_vhdl_componentreference_is_not_abstract():
    assert not inspect.isabstract(declaration_vhdl_ComponentReference)


def test_declaration_vhdl_componentreference_constructor_exists():
    assert callable(declaration_vhdl_ComponentReference.__init__)


def test_declaration_vhdl_componentreference_constructor_args():
    sig = inspect.signature(declaration_vhdl_ComponentReference.__init__)
    params = list(sig.parameters.keys())



def test_declaration_subprogramdeclaration_is_not_abstract():
    assert not inspect.isabstract(declaration_SubprogramDeclaration)


def test_declaration_subprogramdeclaration_constructor_exists():
    assert callable(declaration_SubprogramDeclaration.__init__)


def test_declaration_subprogramdeclaration_constructor_args():
    sig = inspect.signature(declaration_SubprogramDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_nature_natured_is_not_abstract():
    assert not inspect.isabstract(nature_Natured)


def test_nature_natured_constructor_exists():
    assert callable(nature_Natured.__init__)


def test_nature_natured_constructor_args():
    sig = inspect.signature(nature_Natured.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_nature_arraynaturedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl_nature_ArrayNatureDefinition)


def test_vhdl_nature_arraynaturedefinition_constructor_exists():
    assert callable(vhdl_nature_ArrayNatureDefinition.__init__)


def test_vhdl_nature_arraynaturedefinition_constructor_args():
    sig = inspect.signature(vhdl_nature_ArrayNatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_sourceaspect_is_not_abstract():
    assert not inspect.isabstract(SourceAspect)


def test_sourceaspect_constructor_exists():
    assert callable(SourceAspect.__init__)


def test_sourceaspect_constructor_args():
    sig = inspect.signature(SourceAspect.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_ams_noise_is_not_abstract():
    assert not inspect.isabstract(vhdl_ams_Noise)


def test_vhdl_ams_noise_constructor_exists():
    assert callable(vhdl_ams_Noise.__init__)


def test_vhdl_ams_noise_constructor_args():
    sig = inspect.signature(vhdl_ams_Noise.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_ams_spectrum_is_not_abstract():
    assert not inspect.isabstract(vhdl_ams_Spectrum)


def test_vhdl_ams_spectrum_constructor_exists():
    assert callable(vhdl_ams_Spectrum.__init__)


def test_vhdl_ams_spectrum_constructor_args():
    sig = inspect.signature(vhdl_ams_Spectrum.__init__)
    params = list(sig.parameters.keys())



def test_multinamed_is_not_abstract():
    assert not inspect.isabstract(MultiNamed)


def test_multinamed_constructor_exists():
    assert callable(MultiNamed.__init__)


def test_multinamed_constructor_args():
    sig = inspect.signature(MultiNamed.__init__)
    params = list(sig.parameters.keys())



def test_declaration_quantitydeclaration_is_not_abstract():
    assert not inspect.isabstract(declaration_QuantityDeclaration)


def test_declaration_quantitydeclaration_constructor_exists():
    assert callable(declaration_QuantityDeclaration.__init__)


def test_declaration_quantitydeclaration_constructor_args():
    sig = inspect.signature(declaration_QuantityDeclaration.__init__)
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



def test_vhdl_declaration_branchquantitydeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl_declaration_BranchQuantityDeclaration)


def test_vhdl_declaration_branchquantitydeclaration_constructor_exists():
    assert callable(vhdl_declaration_BranchQuantityDeclaration.__init__)


def test_vhdl_declaration_branchquantitydeclaration_constructor_args():
    sig = inspect.signature(vhdl_declaration_BranchQuantityDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_declaration_vhdl_multiname_is_not_abstract():
    assert not inspect.isabstract(declaration_vhdl_MultiName)


def test_declaration_vhdl_multiname_constructor_exists():
    assert callable(declaration_vhdl_MultiName.__init__)


def test_declaration_vhdl_multiname_constructor_args():
    sig = inspect.signature(declaration_vhdl_MultiName.__init__)
    params = list(sig.parameters.keys())



def test_declaration_vhdl_name_is_not_abstract():
    assert not inspect.isabstract(declaration_vhdl_Name)


def test_declaration_vhdl_name_constructor_exists():
    assert callable(declaration_vhdl_Name.__init__)


def test_declaration_vhdl_name_constructor_args():
    sig = inspect.signature(declaration_vhdl_Name.__init__)
    params = list(sig.parameters.keys())



def test_associationexpression_is_not_abstract():
    assert not inspect.isabstract(AssociationExpression)


def test_associationexpression_constructor_exists():
    assert callable(AssociationExpression.__init__)


def test_associationexpression_constructor_args():
    sig = inspect.signature(AssociationExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_expression_conditionalwaveformexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_ConditionalWaveformExpression)


def test_vhdl_expression_conditionalwaveformexpression_constructor_exists():
    assert callable(vhdl_expression_ConditionalWaveformExpression.__init__)


def test_vhdl_expression_conditionalwaveformexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_ConditionalWaveformExpression.__init__)
    params = list(sig.parameters.keys())



def test_type_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(type_EnumerationLiteral)


def test_type_enumerationliteral_constructor_exists():
    assert callable(type_EnumerationLiteral.__init__)


def test_type_enumerationliteral_constructor_args():
    sig = inspect.signature(type_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_expression_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(expression_BinaryExpression)


def test_expression_binaryexpression_constructor_exists():
    assert callable(expression_BinaryExpression.__init__)


def test_expression_binaryexpression_constructor_args():
    sig = inspect.signature(expression_BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_vhdl_name_is_not_abstract():
    assert not inspect.isabstract(expression_vhdl_Name)


def test_expression_vhdl_name_constructor_exists():
    assert callable(expression_vhdl_Name.__init__)


def test_expression_vhdl_name_constructor_args():
    sig = inspect.signature(expression_vhdl_Name.__init__)
    params = list(sig.parameters.keys())



def test_naturereference_is_not_abstract():
    assert not inspect.isabstract(NatureReference)


def test_naturereference_constructor_exists():
    assert callable(NatureReference.__init__)


def test_naturereference_constructor_args():
    sig = inspect.signature(NatureReference.__init__)
    params = list(sig.parameters.keys())



def test_expression_indicationexpression_is_not_abstract():
    assert not inspect.isabstract(expression_IndicationExpression)


def test_expression_indicationexpression_constructor_exists():
    assert callable(expression_IndicationExpression.__init__)


def test_expression_indicationexpression_constructor_args():
    sig = inspect.signature(expression_IndicationExpression.__init__)
    params = list(sig.parameters.keys())



def test_valueexpression_is_not_abstract():
    assert not inspect.isabstract(ValueExpression)


def test_valueexpression_constructor_exists():
    assert callable(ValueExpression.__init__)


def test_valueexpression_constructor_args():
    sig = inspect.signature(ValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_expression_unitvalueexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_UnitValueExpression)


def test_vhdl_expression_unitvalueexpression_constructor_exists():
    assert callable(vhdl_expression_UnitValueExpression.__init__)


def test_vhdl_expression_unitvalueexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_UnitValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_expression_bitstringexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_BitStringExpression)


def test_vhdl_expression_bitstringexpression_constructor_exists():
    assert callable(vhdl_expression_BitStringExpression.__init__)


def test_vhdl_expression_bitstringexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_BitStringExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_vhdl_signature_is_not_abstract():
    assert not inspect.isabstract(expression_vhdl_Signature)


def test_expression_vhdl_signature_constructor_exists():
    assert callable(expression_vhdl_Signature.__init__)


def test_expression_vhdl_signature_constructor_args():
    sig = inspect.signature(expression_vhdl_Signature.__init__)
    params = list(sig.parameters.keys())



def test_expression_valueexpression_is_not_abstract():
    assert not inspect.isabstract(expression_ValueExpression)


def test_expression_valueexpression_constructor_exists():
    assert callable(expression_ValueExpression.__init__)


def test_expression_valueexpression_constructor_args():
    sig = inspect.signature(expression_ValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_type_typed_is_not_abstract():
    assert not inspect.isabstract(type_Typed)


def test_type_typed_constructor_exists():
    assert callable(type_Typed.__init__)


def test_type_typed_constructor_args():
    sig = inspect.signature(type_Typed.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_declaration_functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl_declaration_FunctionDeclaration)


def test_vhdl_declaration_functiondeclaration_constructor_exists():
    assert callable(vhdl_declaration_FunctionDeclaration.__init__)


def test_vhdl_declaration_functiondeclaration_constructor_args():
    sig = inspect.signature(vhdl_declaration_FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "purity" in params, "Missing parameter 'purity'"

def test_vhdl_declaration_functiondeclaration_has_purity():
    assert hasattr(vhdl_declaration_FunctionDeclaration, "purity")
    descriptor = None
    for klass in vhdl_declaration_FunctionDeclaration.__mro__:
        if "purity" in klass.__dict__:
            descriptor = klass.__dict__["purity"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_type_filetypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl_type_FileTypeDefinition)


def test_vhdl_type_filetypedefinition_constructor_exists():
    assert callable(vhdl_type_FileTypeDefinition.__init__)


def test_vhdl_type_filetypedefinition_constructor_args():
    sig = inspect.signature(vhdl_type_FileTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_declaration_freequantitydeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl_declaration_FreeQuantityDeclaration)


def test_vhdl_declaration_freequantitydeclaration_constructor_exists():
    assert callable(vhdl_declaration_FreeQuantityDeclaration.__init__)


def test_vhdl_declaration_freequantitydeclaration_constructor_args():
    sig = inspect.signature(vhdl_declaration_FreeQuantityDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_declaration_sourcequantitydeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl_declaration_SourceQuantityDeclaration)


def test_vhdl_declaration_sourcequantitydeclaration_constructor_exists():
    assert callable(vhdl_declaration_SourceQuantityDeclaration.__init__)


def test_vhdl_declaration_sourcequantitydeclaration_constructor_args():
    sig = inspect.signature(vhdl_declaration_SourceQuantityDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_type_accesstypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl_type_AccessTypeDefinition)


def test_vhdl_type_accesstypedefinition_constructor_exists():
    assert callable(vhdl_type_AccessTypeDefinition.__init__)


def test_vhdl_type_accesstypedefinition_constructor_args():
    sig = inspect.signature(vhdl_type_AccessTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_type_arraytypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl_type_ArrayTypeDefinition)


def test_vhdl_type_arraytypedefinition_constructor_exists():
    assert callable(vhdl_type_ArrayTypeDefinition.__init__)


def test_vhdl_type_arraytypedefinition_constructor_args():
    sig = inspect.signature(vhdl_type_ArrayTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_expression_expression_is_not_abstract():
    assert not inspect.isabstract(expression_Expression)


def test_expression_expression_constructor_exists():
    assert callable(expression_Expression.__init__)


def test_expression_expression_constructor_args():
    sig = inspect.signature(expression_Expression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_expression_allocatorexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_AllocatorExpression)


def test_vhdl_expression_allocatorexpression_constructor_exists():
    assert callable(vhdl_expression_AllocatorExpression.__init__)


def test_vhdl_expression_allocatorexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_AllocatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_name_is_not_abstract():
    assert not inspect.isabstract(Name)


def test_name_constructor_exists():
    assert callable(Name.__init__)


def test_name_constructor_args():
    sig = inspect.signature(Name.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_expression_characterexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_CharacterExpression)


def test_vhdl_expression_characterexpression_constructor_exists():
    assert callable(vhdl_expression_CharacterExpression.__init__)


def test_vhdl_expression_characterexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_CharacterExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_expression_rangeexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_RangeExpression)


def test_vhdl_expression_rangeexpression_constructor_exists():
    assert callable(vhdl_expression_RangeExpression.__init__)


def test_vhdl_expression_rangeexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_RangeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_vhdl_expression_rangeexpression_has_direction():
    assert hasattr(vhdl_expression_RangeExpression, "direction")
    descriptor = None
    for klass in vhdl_expression_RangeExpression.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_expression_allexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_AllExpression)


def test_vhdl_expression_allexpression_constructor_exists():
    assert callable(vhdl_expression_AllExpression.__init__)


def test_vhdl_expression_allexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_AllExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_expression_nameexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_NameExpression)


def test_vhdl_expression_nameexpression_constructor_exists():
    assert callable(vhdl_expression_NameExpression.__init__)


def test_vhdl_expression_nameexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_NameExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_expression_typequalificationexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_TypeQualificationExpression)


def test_vhdl_expression_typequalificationexpression_constructor_exists():
    assert callable(vhdl_expression_TypeQualificationExpression.__init__)


def test_vhdl_expression_typequalificationexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_TypeQualificationExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_expression_identifierexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_IdentifierExpression)


def test_vhdl_expression_identifierexpression_constructor_exists():
    assert callable(vhdl_expression_IdentifierExpression.__init__)


def test_vhdl_expression_identifierexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_IdentifierExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_expression_attributeexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_AttributeExpression)


def test_vhdl_expression_attributeexpression_constructor_exists():
    assert callable(vhdl_expression_AttributeExpression.__init__)


def test_vhdl_expression_attributeexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_AttributeExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_expression_signatureexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_SignatureExpression)


def test_vhdl_expression_signatureexpression_constructor_exists():
    assert callable(vhdl_expression_SignatureExpression.__init__)


def test_vhdl_expression_signatureexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_SignatureExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_expression_stringexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_StringExpression)


def test_vhdl_expression_stringexpression_constructor_exists():
    assert callable(vhdl_expression_StringExpression.__init__)


def test_vhdl_expression_stringexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_StringExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_expression_othersexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_OthersExpression)


def test_vhdl_expression_othersexpression_constructor_exists():
    assert callable(vhdl_expression_OthersExpression.__init__)


def test_vhdl_expression_othersexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_OthersExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_multiexpression_is_not_abstract():
    assert not inspect.isabstract(expression_MultiExpression)


def test_expression_multiexpression_constructor_exists():
    assert callable(expression_MultiExpression.__init__)


def test_expression_multiexpression_constructor_args():
    sig = inspect.signature(expression_MultiExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_expression_aggregateexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_AggregateExpression)


def test_vhdl_expression_aggregateexpression_constructor_exists():
    assert callable(vhdl_expression_AggregateExpression.__init__)


def test_vhdl_expression_aggregateexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_AggregateExpression.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_expression_logicalexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_LogicalExpression)


def test_vhdl_expression_logicalexpression_constructor_exists():
    assert callable(vhdl_expression_LogicalExpression.__init__)


def test_vhdl_expression_logicalexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_LogicalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_vhdl_expression_logicalexpression_has_operator():
    assert hasattr(vhdl_expression_LogicalExpression, "operator")
    descriptor = None
    for klass in vhdl_expression_LogicalExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_expression_multiplyingexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_MultiplyingExpression)


def test_vhdl_expression_multiplyingexpression_constructor_exists():
    assert callable(vhdl_expression_MultiplyingExpression.__init__)


def test_vhdl_expression_multiplyingexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_MultiplyingExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_vhdl_expression_multiplyingexpression_has_operator():
    assert hasattr(vhdl_expression_MultiplyingExpression, "operator")
    descriptor = None
    for klass in vhdl_expression_MultiplyingExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_expression_shiftexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_ShiftExpression)


def test_vhdl_expression_shiftexpression_constructor_exists():
    assert callable(vhdl_expression_ShiftExpression.__init__)


def test_vhdl_expression_shiftexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_ShiftExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_vhdl_expression_shiftexpression_has_operator():
    assert hasattr(vhdl_expression_ShiftExpression, "operator")
    descriptor = None
    for klass in vhdl_expression_ShiftExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_expression_relationalexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_RelationalExpression)


def test_vhdl_expression_relationalexpression_constructor_exists():
    assert callable(vhdl_expression_RelationalExpression.__init__)


def test_vhdl_expression_relationalexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_RelationalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_vhdl_expression_relationalexpression_has_operator():
    assert hasattr(vhdl_expression_RelationalExpression, "operator")
    descriptor = None
    for klass in vhdl_expression_RelationalExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_expression_powerexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_PowerExpression)


def test_vhdl_expression_powerexpression_constructor_exists():
    assert callable(vhdl_expression_PowerExpression.__init__)


def test_vhdl_expression_powerexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_PowerExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_expression_addingexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_AddingExpression)


def test_vhdl_expression_addingexpression_constructor_exists():
    assert callable(vhdl_expression_AddingExpression.__init__)


def test_vhdl_expression_addingexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_AddingExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_vhdl_expression_addingexpression_has_operator():
    assert hasattr(vhdl_expression_AddingExpression, "operator")
    descriptor = None
    for klass in vhdl_expression_AddingExpression.__mro__:
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



def test_statement_vhdl_entityreference_is_not_abstract():
    assert not inspect.isabstract(statement_vhdl_EntityReference)


def test_statement_vhdl_entityreference_constructor_exists():
    assert callable(statement_vhdl_EntityReference.__init__)


def test_statement_vhdl_entityreference_constructor_args():
    sig = inspect.signature(statement_vhdl_EntityReference.__init__)
    params = list(sig.parameters.keys())



def test_iterationscheme_is_not_abstract():
    assert not inspect.isabstract(IterationScheme)


def test_iterationscheme_constructor_exists():
    assert callable(IterationScheme.__init__)


def test_iterationscheme_constructor_args():
    sig = inspect.signature(IterationScheme.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_statement_whileiterationscheme_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_WhileIterationScheme)


def test_vhdl_statement_whileiterationscheme_constructor_exists():
    assert callable(vhdl_statement_WhileIterationScheme.__init__)


def test_vhdl_statement_whileiterationscheme_constructor_args():
    sig = inspect.signature(vhdl_statement_WhileIterationScheme.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_statement_foriterationscheme_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_ForIterationScheme)


def test_vhdl_statement_foriterationscheme_constructor_exists():
    assert callable(vhdl_statement_ForIterationScheme.__init__)


def test_vhdl_statement_foriterationscheme_constructor_args():
    sig = inspect.signature(vhdl_statement_ForIterationScheme.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_vhdl_statement_foriterationscheme_has_variable():
    assert hasattr(vhdl_statement_ForIterationScheme, "variable")
    descriptor = None
    for klass in vhdl_statement_ForIterationScheme.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_generationscheme_is_not_abstract():
    assert not inspect.isabstract(GenerationScheme)


def test_generationscheme_constructor_exists():
    assert callable(GenerationScheme.__init__)


def test_generationscheme_constructor_args():
    sig = inspect.signature(GenerationScheme.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_statement_forgenerationscheme_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_ForGenerationScheme)


def test_vhdl_statement_forgenerationscheme_constructor_exists():
    assert callable(vhdl_statement_ForGenerationScheme.__init__)


def test_vhdl_statement_forgenerationscheme_constructor_args():
    sig = inspect.signature(vhdl_statement_ForGenerationScheme.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_vhdl_statement_forgenerationscheme_has_variable():
    assert hasattr(vhdl_statement_ForGenerationScheme, "variable")
    descriptor = None
    for klass in vhdl_statement_ForGenerationScheme.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_statement_ifgenerationscheme_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_IfGenerationScheme)


def test_vhdl_statement_ifgenerationscheme_constructor_exists():
    assert callable(vhdl_statement_IfGenerationScheme.__init__)


def test_vhdl_statement_ifgenerationscheme_constructor_args():
    sig = inspect.signature(vhdl_statement_IfGenerationScheme.__init__)
    params = list(sig.parameters.keys())



def test_statement_vhdl_componentreference_is_not_abstract():
    assert not inspect.isabstract(statement_vhdl_ComponentReference)


def test_statement_vhdl_componentreference_constructor_exists():
    assert callable(statement_vhdl_ComponentReference.__init__)


def test_statement_vhdl_componentreference_constructor_args():
    sig = inspect.signature(statement_vhdl_ComponentReference.__init__)
    params = list(sig.parameters.keys())



def test_instantiationstatement_is_not_abstract():
    assert not inspect.isabstract(InstantiationStatement)


def test_instantiationstatement_constructor_exists():
    assert callable(InstantiationStatement.__init__)


def test_instantiationstatement_constructor_args():
    sig = inspect.signature(InstantiationStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_statement_configurationinstantiationstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_ConfigurationInstantiationStatement)


def test_vhdl_statement_configurationinstantiationstatement_constructor_exists():
    assert callable(vhdl_statement_ConfigurationInstantiationStatement.__init__)


def test_vhdl_statement_configurationinstantiationstatement_constructor_args():
    sig = inspect.signature(vhdl_statement_ConfigurationInstantiationStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_statement_entityinstantiationstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_EntityInstantiationStatement)


def test_vhdl_statement_entityinstantiationstatement_constructor_exists():
    assert callable(vhdl_statement_EntityInstantiationStatement.__init__)


def test_vhdl_statement_entityinstantiationstatement_constructor_args():
    sig = inspect.signature(vhdl_statement_EntityInstantiationStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_statement_componentinstantiationstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_ComponentInstantiationStatement)


def test_vhdl_statement_componentinstantiationstatement_constructor_exists():
    assert callable(vhdl_statement_ComponentInstantiationStatement.__init__)


def test_vhdl_statement_componentinstantiationstatement_constructor_args():
    sig = inspect.signature(vhdl_statement_ComponentInstantiationStatement.__init__)
    params = list(sig.parameters.keys())



def test_statement_vhdl_name_is_not_abstract():
    assert not inspect.isabstract(statement_vhdl_Name)


def test_statement_vhdl_name_constructor_exists():
    assert callable(statement_vhdl_Name.__init__)


def test_statement_vhdl_name_constructor_args():
    sig = inspect.signature(statement_vhdl_Name.__init__)
    params = list(sig.parameters.keys())



def test_breakstatementitem_is_not_abstract():
    assert not inspect.isabstract(BreakStatementItem)


def test_breakstatementitem_constructor_exists():
    assert callable(BreakStatementItem.__init__)


def test_breakstatementitem_constructor_args():
    sig = inspect.signature(BreakStatementItem.__init__)
    params = list(sig.parameters.keys())



def test_statement_vhdl_portmaps_is_not_abstract():
    assert not inspect.isabstract(statement_vhdl_PortMaps)


def test_statement_vhdl_portmaps_constructor_exists():
    assert callable(statement_vhdl_PortMaps.__init__)


def test_statement_vhdl_portmaps_constructor_args():
    sig = inspect.signature(statement_vhdl_PortMaps.__init__)
    params = list(sig.parameters.keys())



def test_statement_vhdl_ports_is_not_abstract():
    assert not inspect.isabstract(statement_vhdl_Ports)


def test_statement_vhdl_ports_constructor_exists():
    assert callable(statement_vhdl_Ports.__init__)


def test_statement_vhdl_ports_constructor_args():
    sig = inspect.signature(statement_vhdl_Ports.__init__)
    params = list(sig.parameters.keys())



def test_statement_vhdl_genericmaps_is_not_abstract():
    assert not inspect.isabstract(statement_vhdl_GenericMaps)


def test_statement_vhdl_genericmaps_constructor_exists():
    assert callable(statement_vhdl_GenericMaps.__init__)


def test_statement_vhdl_genericmaps_constructor_args():
    sig = inspect.signature(statement_vhdl_GenericMaps.__init__)
    params = list(sig.parameters.keys())



def test_statement_vhdl_generics_is_not_abstract():
    assert not inspect.isabstract(statement_vhdl_Generics)


def test_statement_vhdl_generics_constructor_exists():
    assert callable(statement_vhdl_Generics.__init__)


def test_statement_vhdl_generics_constructor_args():
    sig = inspect.signature(statement_vhdl_Generics.__init__)
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



def test_vhdl_statement_simultaneouscasestatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_SimultaneousCaseStatement)


def test_vhdl_statement_simultaneouscasestatement_constructor_exists():
    assert callable(vhdl_statement_SimultaneousCaseStatement.__init__)


def test_vhdl_statement_simultaneouscasestatement_constructor_args():
    sig = inspect.signature(vhdl_statement_SimultaneousCaseStatement.__init__)
    params = list(sig.parameters.keys())



def test_statement_vhdl_callreference_is_not_abstract():
    assert not inspect.isabstract(statement_vhdl_CallReference)


def test_statement_vhdl_callreference_constructor_exists():
    assert callable(statement_vhdl_CallReference.__init__)


def test_statement_vhdl_callreference_constructor_args():
    sig = inspect.signature(statement_vhdl_CallReference.__init__)
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



def test_vhdl_statement_simultaneousifstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_SimultaneousIfStatement)


def test_vhdl_statement_simultaneousifstatement_constructor_exists():
    assert callable(vhdl_statement_SimultaneousIfStatement.__init__)


def test_vhdl_statement_simultaneousifstatement_constructor_args():
    sig = inspect.signature(vhdl_statement_SimultaneousIfStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_componentreference_is_not_abstract():
    assert not inspect.isabstract(vhdl_ComponentReference)


def test_vhdl_componentreference_constructor_exists():
    assert callable(vhdl_ComponentReference.__init__)


def test_vhdl_componentreference_constructor_args():
    sig = inspect.signature(vhdl_ComponentReference.__init__)
    params = list(sig.parameters.keys())



def test_statement_vhdl_multiname_is_not_abstract():
    assert not inspect.isabstract(statement_vhdl_MultiName)


def test_statement_vhdl_multiname_constructor_exists():
    assert callable(statement_vhdl_MultiName.__init__)


def test_statement_vhdl_multiname_constructor_args():
    sig = inspect.signature(statement_vhdl_MultiName.__init__)
    params = list(sig.parameters.keys())



def test_delaymechanism_is_not_abstract():
    assert not inspect.isabstract(DelayMechanism)


def test_delaymechanism_constructor_exists():
    assert callable(DelayMechanism.__init__)


def test_delaymechanism_constructor_args():
    sig = inspect.signature(DelayMechanism.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_statement_transportmechanism_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_TransportMechanism)


def test_vhdl_statement_transportmechanism_constructor_exists():
    assert callable(vhdl_statement_TransportMechanism.__init__)


def test_vhdl_statement_transportmechanism_constructor_args():
    sig = inspect.signature(vhdl_statement_TransportMechanism.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_statement_rejectmechanism_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_RejectMechanism)


def test_vhdl_statement_rejectmechanism_constructor_exists():
    assert callable(vhdl_statement_RejectMechanism.__init__)


def test_vhdl_statement_rejectmechanism_constructor_args():
    sig = inspect.signature(vhdl_statement_RejectMechanism.__init__)
    params = list(sig.parameters.keys())



def test_conditionalsignalassignmentstatement_is_not_abstract():
    assert not inspect.isabstract(ConditionalSignalAssignmentStatement)


def test_conditionalsignalassignmentstatement_constructor_exists():
    assert callable(ConditionalSignalAssignmentStatement.__init__)


def test_conditionalsignalassignmentstatement_constructor_args():
    sig = inspect.signature(ConditionalSignalAssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_statement_selectedsignalassignmentstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_SelectedSignalAssignmentStatement)


def test_vhdl_statement_selectedsignalassignmentstatement_constructor_exists():
    assert callable(vhdl_statement_SelectedSignalAssignmentStatement.__init__)


def test_vhdl_statement_selectedsignalassignmentstatement_constructor_args():
    sig = inspect.signature(vhdl_statement_SelectedSignalAssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_signalassignmentstatement_is_not_abstract():
    assert not inspect.isabstract(SignalAssignmentStatement)


def test_signalassignmentstatement_constructor_exists():
    assert callable(SignalAssignmentStatement.__init__)


def test_signalassignmentstatement_constructor_args():
    sig = inspect.signature(SignalAssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_statement_sequentialsignalassignmentstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_SequentialSignalAssignmentStatement)


def test_vhdl_statement_sequentialsignalassignmentstatement_constructor_exists():
    assert callable(vhdl_statement_SequentialSignalAssignmentStatement.__init__)


def test_vhdl_statement_sequentialsignalassignmentstatement_constructor_args():
    sig = inspect.signature(vhdl_statement_SequentialSignalAssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_statement_conditionalsignalassignmentstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_ConditionalSignalAssignmentStatement)


def test_vhdl_statement_conditionalsignalassignmentstatement_constructor_exists():
    assert callable(vhdl_statement_ConditionalSignalAssignmentStatement.__init__)


def test_vhdl_statement_conditionalsignalassignmentstatement_constructor_args():
    sig = inspect.signature(vhdl_statement_ConditionalSignalAssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(ExpressionStatement)


def test_expressionstatement_constructor_exists():
    assert callable(ExpressionStatement.__init__)


def test_expressionstatement_constructor_args():
    sig = inspect.signature(ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_statement_returnstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_ReturnStatement)


def test_vhdl_statement_returnstatement_constructor_exists():
    assert callable(vhdl_statement_ReturnStatement.__init__)


def test_vhdl_statement_returnstatement_constructor_args():
    sig = inspect.signature(vhdl_statement_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_subprogramdeclaration_is_not_abstract():
    assert not inspect.isabstract(SubprogramDeclaration)


def test_subprogramdeclaration_constructor_exists():
    assert callable(SubprogramDeclaration.__init__)


def test_subprogramdeclaration_constructor_args():
    sig = inspect.signature(SubprogramDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_declaration_proceduredeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl_declaration_ProcedureDeclaration)


def test_vhdl_declaration_proceduredeclaration_constructor_exists():
    assert callable(vhdl_declaration_ProcedureDeclaration.__init__)


def test_vhdl_declaration_proceduredeclaration_constructor_args():
    sig = inspect.signature(vhdl_declaration_ProcedureDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_callreference_is_not_abstract():
    assert not inspect.isabstract(vhdl_CallReference)


def test_vhdl_callreference_constructor_exists():
    assert callable(vhdl_CallReference.__init__)


def test_vhdl_callreference_constructor_args():
    sig = inspect.signature(vhdl_CallReference.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_vhdlobject_is_not_abstract():
    assert not inspect.isabstract(vhdl_VhdlObject)


def test_vhdl_vhdlobject_constructor_exists():
    assert callable(vhdl_VhdlObject.__init__)


def test_vhdl_vhdlobject_constructor_args():
    sig = inspect.signature(vhdl_VhdlObject.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_vhdl_vhdlobject_has_id():
    assert hasattr(vhdl_VhdlObject, "id")
    descriptor = None
    for klass in vhdl_VhdlObject.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_multiname_is_not_abstract():
    assert not inspect.isabstract(vhdl_MultiName)


def test_vhdl_multiname_constructor_exists():
    assert callable(vhdl_MultiName.__init__)


def test_vhdl_multiname_constructor_args():
    sig = inspect.signature(vhdl_MultiName.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_multinamed_is_not_abstract():
    assert not inspect.isabstract(vhdl_MultiNamed)


def test_vhdl_multinamed_constructor_exists():
    assert callable(vhdl_MultiNamed.__init__)


def test_vhdl_multinamed_constructor_args():
    sig = inspect.signature(vhdl_MultiNamed.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_named_is_not_abstract():
    assert not inspect.isabstract(vhdl_Named)


def test_vhdl_named_constructor_exists():
    assert callable(vhdl_Named.__init__)


def test_vhdl_named_constructor_args():
    sig = inspect.signature(vhdl_Named.__init__)
    params = list(sig.parameters.keys())



def test_callreference_is_not_abstract():
    assert not inspect.isabstract(CallReference)


def test_callreference_constructor_exists():
    assert callable(CallReference.__init__)


def test_callreference_constructor_args():
    sig = inspect.signature(CallReference.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_callresolvedreference_is_not_abstract():
    assert not inspect.isabstract(vhdl_CallResolvedReference)


def test_vhdl_callresolvedreference_constructor_exists():
    assert callable(vhdl_CallResolvedReference.__init__)


def test_vhdl_callresolvedreference_constructor_args():
    sig = inspect.signature(vhdl_CallResolvedReference.__init__)
    params = list(sig.parameters.keys())



def test_configuration_configurationreference_is_not_abstract():
    assert not inspect.isabstract(configuration_ConfigurationReference)


def test_configuration_configurationreference_constructor_exists():
    assert callable(configuration_ConfigurationReference.__init__)


def test_configuration_configurationreference_constructor_args():
    sig = inspect.signature(configuration_ConfigurationReference.__init__)
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



def test_nature_naturereference_is_not_abstract():
    assert not inspect.isabstract(nature_NatureReference)


def test_nature_naturereference_constructor_exists():
    assert callable(nature_NatureReference.__init__)


def test_nature_naturereference_constructor_args():
    sig = inspect.signature(nature_NatureReference.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_expression_subnatureindicationexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_SubnatureIndicationExpression)


def test_vhdl_expression_subnatureindicationexpression_constructor_exists():
    assert callable(vhdl_expression_SubnatureIndicationExpression.__init__)


def test_vhdl_expression_subnatureindicationexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_SubnatureIndicationExpression.__init__)
    params = list(sig.parameters.keys())



def test_type_typereference_is_not_abstract():
    assert not inspect.isabstract(type_TypeReference)


def test_type_typereference_constructor_exists():
    assert callable(type_TypeReference.__init__)


def test_type_typereference_constructor_args():
    sig = inspect.signature(type_TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_multiname_is_not_abstract():
    assert not inspect.isabstract(MultiName)


def test_multiname_constructor_exists():
    assert callable(MultiName.__init__)


def test_multiname_constructor_args():
    sig = inspect.signature(MultiName.__init__)
    params = list(sig.parameters.keys())



def test_declaration_declaration_is_not_abstract():
    assert not inspect.isabstract(declaration_Declaration)


def test_declaration_declaration_constructor_exists():
    assert callable(declaration_Declaration.__init__)


def test_declaration_declaration_constructor_args():
    sig = inspect.signature(declaration_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_declaration_disconnectionspecification_is_not_abstract():
    assert not inspect.isabstract(vhdl_declaration_DisconnectionSpecification)


def test_vhdl_declaration_disconnectionspecification_constructor_exists():
    assert callable(vhdl_declaration_DisconnectionSpecification.__init__)


def test_vhdl_declaration_disconnectionspecification_constructor_args():
    sig = inspect.signature(vhdl_declaration_DisconnectionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_declaration_filedeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl_declaration_FileDeclaration)


def test_vhdl_declaration_filedeclaration_constructor_exists():
    assert callable(vhdl_declaration_FileDeclaration.__init__)


def test_vhdl_declaration_filedeclaration_constructor_args():
    sig = inspect.signature(vhdl_declaration_FileDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_declaration_terminaldeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl_declaration_TerminalDeclaration)


def test_vhdl_declaration_terminaldeclaration_constructor_exists():
    assert callable(vhdl_declaration_TerminalDeclaration.__init__)


def test_vhdl_declaration_terminaldeclaration_constructor_args():
    sig = inspect.signature(vhdl_declaration_TerminalDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_declaration_valuedeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl_declaration_ValueDeclaration)


def test_vhdl_declaration_valuedeclaration_constructor_exists():
    assert callable(vhdl_declaration_ValueDeclaration.__init__)


def test_vhdl_declaration_valuedeclaration_constructor_args():
    sig = inspect.signature(vhdl_declaration_ValueDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_declaration_limitdeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl_declaration_LimitDeclaration)


def test_vhdl_declaration_limitdeclaration_constructor_exists():
    assert callable(vhdl_declaration_LimitDeclaration.__init__)


def test_vhdl_declaration_limitdeclaration_constructor_args():
    sig = inspect.signature(vhdl_declaration_LimitDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_typereference_is_not_abstract():
    assert not inspect.isabstract(TypeReference)


def test_typereference_constructor_exists():
    assert callable(TypeReference.__init__)


def test_typereference_constructor_args():
    sig = inspect.signature(TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_packagereference_is_not_abstract():
    assert not inspect.isabstract(vhdl_PackageReference)


def test_vhdl_packagereference_constructor_exists():
    assert callable(vhdl_PackageReference.__init__)


def test_vhdl_packagereference_constructor_args():
    sig = inspect.signature(vhdl_PackageReference.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_expression_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_UnaryExpression)


def test_vhdl_expression_unaryexpression_constructor_exists():
    assert callable(vhdl_expression_UnaryExpression.__init__)


def test_vhdl_expression_unaryexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_vhdl_expression_unaryexpression_has_operator():
    assert hasattr(vhdl_expression_UnaryExpression, "operator")
    descriptor = None
    for klass in vhdl_expression_UnaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_expression_nullexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_NullExpression)


def test_vhdl_expression_nullexpression_constructor_exists():
    assert callable(vhdl_expression_NullExpression.__init__)


def test_vhdl_expression_nullexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_NullExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_expression_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_BinaryExpression)


def test_vhdl_expression_binaryexpression_constructor_exists():
    assert callable(vhdl_expression_BinaryExpression.__init__)


def test_vhdl_expression_binaryexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_expression_openexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_OpenExpression)


def test_vhdl_expression_openexpression_constructor_exists():
    assert callable(vhdl_expression_OpenExpression.__init__)


def test_vhdl_expression_openexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_OpenExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_expression_waveformexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_WaveformExpression)


def test_vhdl_expression_waveformexpression_constructor_exists():
    assert callable(vhdl_expression_WaveformExpression.__init__)


def test_vhdl_expression_waveformexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_WaveformExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_expression_valueexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_ValueExpression)


def test_vhdl_expression_valueexpression_constructor_exists():
    assert callable(vhdl_expression_ValueExpression.__init__)


def test_vhdl_expression_valueexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_ValueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vhdl_expression_valueexpression_has_value():
    assert hasattr(vhdl_expression_ValueExpression, "value")
    descriptor = None
    for klass in vhdl_expression_ValueExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_expression_signexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_SignExpression)


def test_vhdl_expression_signexpression_constructor_exists():
    assert callable(vhdl_expression_SignExpression.__init__)


def test_vhdl_expression_signexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_SignExpression.__init__)
    params = list(sig.parameters.keys())
    assert "sign" in params, "Missing parameter 'sign'"

def test_vhdl_expression_signexpression_has_sign():
    assert hasattr(vhdl_expression_SignExpression, "sign")
    descriptor = None
    for klass in vhdl_expression_SignExpression.__mro__:
        if "sign" in klass.__dict__:
            descriptor = klass.__dict__["sign"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_expression_multiexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_MultiExpression)


def test_vhdl_expression_multiexpression_constructor_exists():
    assert callable(vhdl_expression_MultiExpression.__init__)


def test_vhdl_expression_multiexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_MultiExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_expression_indicationexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_IndicationExpression)


def test_vhdl_expression_indicationexpression_constructor_exists():
    assert callable(vhdl_expression_IndicationExpression.__init__)


def test_vhdl_expression_indicationexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_IndicationExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_expression_associationexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_AssociationExpression)


def test_vhdl_expression_associationexpression_constructor_exists():
    assert callable(vhdl_expression_AssociationExpression.__init__)


def test_vhdl_expression_associationexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_AssociationExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_expression_unaffectedexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_UnaffectedExpression)


def test_vhdl_expression_unaffectedexpression_constructor_exists():
    assert callable(vhdl_expression_UnaffectedExpression.__init__)


def test_vhdl_expression_unaffectedexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_UnaffectedExpression.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_declaration_quantitydeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl_declaration_QuantityDeclaration)


def test_vhdl_declaration_quantitydeclaration_constructor_exists():
    assert callable(vhdl_declaration_QuantityDeclaration.__init__)


def test_vhdl_declaration_quantitydeclaration_constructor_args():
    sig = inspect.signature(vhdl_declaration_QuantityDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_declaration_configurationspecification_is_not_abstract():
    assert not inspect.isabstract(vhdl_declaration_ConfigurationSpecification)


def test_vhdl_declaration_configurationspecification_constructor_exists():
    assert callable(vhdl_declaration_ConfigurationSpecification.__init__)


def test_vhdl_declaration_configurationspecification_constructor_args():
    sig = inspect.signature(vhdl_declaration_ConfigurationSpecification.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_declaration_useclausedeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl_declaration_UseClauseDeclaration)


def test_vhdl_declaration_useclausedeclaration_constructor_exists():
    assert callable(vhdl_declaration_UseClauseDeclaration.__init__)


def test_vhdl_declaration_useclausedeclaration_constructor_args():
    sig = inspect.signature(vhdl_declaration_UseClauseDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_name_is_not_abstract():
    assert not inspect.isabstract(vhdl_Name)


def test_vhdl_name_constructor_exists():
    assert callable(vhdl_Name.__init__)


def test_vhdl_name_constructor_args():
    sig = inspect.signature(vhdl_Name.__init__)
    params = list(sig.parameters.keys())



def test_vhdlobject_is_not_abstract():
    assert not inspect.isabstract(VhdlObject)


def test_vhdlobject_constructor_exists():
    assert callable(VhdlObject.__init__)


def test_vhdlobject_constructor_args():
    sig = inspect.signature(VhdlObject.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_type_typedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl_type_TypeDefinition)


def test_vhdl_type_typedefinition_constructor_exists():
    assert callable(vhdl_type_TypeDefinition.__init__)


def test_vhdl_type_typedefinition_constructor_args():
    sig = inspect.signature(vhdl_type_TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_statement_iterationscheme_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_IterationScheme)


def test_vhdl_statement_iterationscheme_constructor_exists():
    assert callable(vhdl_statement_IterationScheme.__init__)


def test_vhdl_statement_iterationscheme_constructor_args():
    sig = inspect.signature(vhdl_statement_IterationScheme.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_module_is_not_abstract():
    assert not inspect.isabstract(vhdl_Module)


def test_vhdl_module_constructor_exists():
    assert callable(vhdl_Module.__init__)


def test_vhdl_module_constructor_args():
    sig = inspect.signature(vhdl_Module.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_declaration_declaration_is_not_abstract():
    assert not inspect.isabstract(vhdl_declaration_Declaration)


def test_vhdl_declaration_declaration_constructor_exists():
    assert callable(vhdl_declaration_Declaration.__init__)


def test_vhdl_declaration_declaration_constructor_args():
    sig = inspect.signature(vhdl_declaration_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_entityresolvedreference_is_not_abstract():
    assert not inspect.isabstract(vhdl_EntityResolvedReference)


def test_vhdl_entityresolvedreference_constructor_exists():
    assert callable(vhdl_EntityResolvedReference.__init__)


def test_vhdl_entityresolvedreference_constructor_args():
    sig = inspect.signature(vhdl_EntityResolvedReference.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_generics_is_not_abstract():
    assert not inspect.isabstract(vhdl_Generics)


def test_vhdl_generics_constructor_exists():
    assert callable(vhdl_Generics.__init__)


def test_vhdl_generics_constructor_args():
    sig = inspect.signature(vhdl_Generics.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_configuration_configurationitem_is_not_abstract():
    assert not inspect.isabstract(vhdl_configuration_ConfigurationItem)


def test_vhdl_configuration_configurationitem_constructor_exists():
    assert callable(vhdl_configuration_ConfigurationItem.__init__)


def test_vhdl_configuration_configurationitem_constructor_args():
    sig = inspect.signature(vhdl_configuration_ConfigurationItem.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_type_recordtypeelement_is_not_abstract():
    assert not inspect.isabstract(vhdl_type_RecordTypeElement)


def test_vhdl_type_recordtypeelement_constructor_exists():
    assert callable(vhdl_type_RecordTypeElement.__init__)


def test_vhdl_type_recordtypeelement_constructor_args():
    sig = inspect.signature(vhdl_type_RecordTypeElement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_statement_casealternative_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_CaseAlternative)


def test_vhdl_statement_casealternative_constructor_exists():
    assert callable(vhdl_statement_CaseAlternative.__init__)


def test_vhdl_statement_casealternative_constructor_args():
    sig = inspect.signature(vhdl_statement_CaseAlternative.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_signature_is_not_abstract():
    assert not inspect.isabstract(vhdl_Signature)


def test_vhdl_signature_constructor_exists():
    assert callable(vhdl_Signature.__init__)


def test_vhdl_signature_constructor_args():
    sig = inspect.signature(vhdl_Signature.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_statement_breakstatementitem_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_BreakStatementItem)


def test_vhdl_statement_breakstatementitem_constructor_exists():
    assert callable(vhdl_statement_BreakStatementItem.__init__)


def test_vhdl_statement_breakstatementitem_constructor_args():
    sig = inspect.signature(vhdl_statement_BreakStatementItem.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_statement_statement_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_Statement)


def test_vhdl_statement_statement_constructor_exists():
    assert callable(vhdl_statement_Statement.__init__)


def test_vhdl_statement_statement_constructor_args():
    sig = inspect.signature(vhdl_statement_Statement.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_vhdl_statement_statement_has_label():
    assert hasattr(vhdl_statement_Statement, "label")
    descriptor = None
    for klass in vhdl_statement_Statement.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_nature_naturedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl_nature_NatureDefinition)


def test_vhdl_nature_naturedefinition_constructor_exists():
    assert callable(vhdl_nature_NatureDefinition.__init__)


def test_vhdl_nature_naturedefinition_constructor_args():
    sig = inspect.signature(vhdl_nature_NatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_genericmaps_is_not_abstract():
    assert not inspect.isabstract(vhdl_GenericMaps)


def test_vhdl_genericmaps_constructor_exists():
    assert callable(vhdl_GenericMaps.__init__)


def test_vhdl_genericmaps_constructor_args():
    sig = inspect.signature(vhdl_GenericMaps.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_namelist_is_not_abstract():
    assert not inspect.isabstract(vhdl_NameList)


def test_vhdl_namelist_constructor_exists():
    assert callable(vhdl_NameList.__init__)


def test_vhdl_namelist_constructor_args():
    sig = inspect.signature(vhdl_NameList.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_ports_is_not_abstract():
    assert not inspect.isabstract(vhdl_Ports)


def test_vhdl_ports_constructor_exists():
    assert callable(vhdl_Ports.__init__)


def test_vhdl_ports_constructor_args():
    sig = inspect.signature(vhdl_Ports.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_statement_delaymechanism_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_DelayMechanism)


def test_vhdl_statement_delaymechanism_constructor_exists():
    assert callable(vhdl_statement_DelayMechanism.__init__)


def test_vhdl_statement_delaymechanism_constructor_args():
    sig = inspect.signature(vhdl_statement_DelayMechanism.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_declaration_subprogrambody_is_not_abstract():
    assert not inspect.isabstract(vhdl_declaration_SubprogramBody)


def test_vhdl_declaration_subprogrambody_constructor_exists():
    assert callable(vhdl_declaration_SubprogramBody.__init__)


def test_vhdl_declaration_subprogrambody_constructor_args():
    sig = inspect.signature(vhdl_declaration_SubprogramBody.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_ams_sourceaspect_is_not_abstract():
    assert not inspect.isabstract(vhdl_ams_SourceAspect)


def test_vhdl_ams_sourceaspect_constructor_exists():
    assert callable(vhdl_ams_SourceAspect.__init__)


def test_vhdl_ams_sourceaspect_constructor_args():
    sig = inspect.signature(vhdl_ams_SourceAspect.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_model_is_not_abstract():
    assert not inspect.isabstract(vhdl_Model)


def test_vhdl_model_constructor_exists():
    assert callable(vhdl_Model.__init__)


def test_vhdl_model_constructor_args():
    sig = inspect.signature(vhdl_Model.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_portmaps_is_not_abstract():
    assert not inspect.isabstract(vhdl_PortMaps)


def test_vhdl_portmaps_constructor_exists():
    assert callable(vhdl_PortMaps.__init__)


def test_vhdl_portmaps_constructor_args():
    sig = inspect.signature(vhdl_PortMaps.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_statement_ifstatementtest_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_IfStatementTest)


def test_vhdl_statement_ifstatementtest_constructor_exists():
    assert callable(vhdl_statement_IfStatementTest.__init__)


def test_vhdl_statement_ifstatementtest_constructor_args():
    sig = inspect.signature(vhdl_statement_IfStatementTest.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_nature_recordnatureelement_is_not_abstract():
    assert not inspect.isabstract(vhdl_nature_RecordNatureElement)


def test_vhdl_nature_recordnatureelement_constructor_exists():
    assert callable(vhdl_nature_RecordNatureElement.__init__)


def test_vhdl_nature_recordnatureelement_constructor_args():
    sig = inspect.signature(vhdl_nature_RecordNatureElement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_expression_expression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_Expression)


def test_vhdl_expression_expression_constructor_exists():
    assert callable(vhdl_expression_Expression.__init__)


def test_vhdl_expression_expression_constructor_args():
    sig = inspect.signature(vhdl_expression_Expression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_ams_quantityaspect_is_not_abstract():
    assert not inspect.isabstract(vhdl_ams_QuantityAspect)


def test_vhdl_ams_quantityaspect_constructor_exists():
    assert callable(vhdl_ams_QuantityAspect.__init__)


def test_vhdl_ams_quantityaspect_constructor_args():
    sig = inspect.signature(vhdl_ams_QuantityAspect.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_statement_generationscheme_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_GenerationScheme)


def test_vhdl_statement_generationscheme_constructor_exists():
    assert callable(vhdl_statement_GenerationScheme.__init__)


def test_vhdl_statement_generationscheme_constructor_args():
    sig = inspect.signature(vhdl_statement_GenerationScheme.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_componentresolvedreference_is_not_abstract():
    assert not inspect.isabstract(vhdl_ComponentResolvedReference)


def test_vhdl_componentresolvedreference_constructor_exists():
    assert callable(vhdl_ComponentResolvedReference.__init__)


def test_vhdl_componentresolvedreference_constructor_args():
    sig = inspect.signature(vhdl_ComponentResolvedReference.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_packageresolvedreference_is_not_abstract():
    assert not inspect.isabstract(vhdl_PackageResolvedReference)


def test_vhdl_packageresolvedreference_constructor_exists():
    assert callable(vhdl_PackageResolvedReference.__init__)


def test_vhdl_packageresolvedreference_constructor_args():
    sig = inspect.signature(vhdl_PackageResolvedReference.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_configuration_configurationresolvedreference_is_not_abstract():
    assert not inspect.isabstract(vhdl_configuration_ConfigurationResolvedReference)


def test_vhdl_configuration_configurationresolvedreference_constructor_exists():
    assert callable(vhdl_configuration_ConfigurationResolvedReference.__init__)


def test_vhdl_configuration_configurationresolvedreference_constructor_args():
    sig = inspect.signature(vhdl_configuration_ConfigurationResolvedReference.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_designunit_is_not_abstract():
    assert not inspect.isabstract(vhdl_DesignUnit)


def test_vhdl_designunit_constructor_exists():
    assert callable(vhdl_DesignUnit.__init__)


def test_vhdl_designunit_constructor_args():
    sig = inspect.signature(vhdl_DesignUnit.__init__)
    params = list(sig.parameters.keys())
    assert "library" in params, "Missing parameter 'library'"

def test_vhdl_designunit_has_library():
    assert hasattr(vhdl_DesignUnit, "library")
    descriptor = None
    for klass in vhdl_DesignUnit.__mro__:
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



def test_vhdl_statement_casestatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_CaseStatement)


def test_vhdl_statement_casestatement_constructor_exists():
    assert callable(vhdl_statement_CaseStatement.__init__)


def test_vhdl_statement_casestatement_constructor_args():
    sig = inspect.signature(vhdl_statement_CaseStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_statement_loopstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_LoopStatement)


def test_vhdl_statement_loopstatement_constructor_exists():
    assert callable(vhdl_statement_LoopStatement.__init__)


def test_vhdl_statement_loopstatement_constructor_args():
    sig = inspect.signature(vhdl_statement_LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_statement_signalassignmentstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_SignalAssignmentStatement)


def test_vhdl_statement_signalassignmentstatement_constructor_exists():
    assert callable(vhdl_statement_SignalAssignmentStatement.__init__)


def test_vhdl_statement_signalassignmentstatement_constructor_args():
    sig = inspect.signature(vhdl_statement_SignalAssignmentStatement.__init__)
    params = list(sig.parameters.keys())
    assert "postponed" in params, "Missing parameter 'postponed'"
    assert "guarded" in params, "Missing parameter 'guarded'"

def test_vhdl_statement_signalassignmentstatement_has_postponed():
    assert hasattr(vhdl_statement_SignalAssignmentStatement, "postponed")
    descriptor = None
    for klass in vhdl_statement_SignalAssignmentStatement.__mro__:
        if "postponed" in klass.__dict__:
            descriptor = klass.__dict__["postponed"]
            break
    assert isinstance(descriptor, property)

def test_vhdl_statement_signalassignmentstatement_has_guarded():
    assert hasattr(vhdl_statement_SignalAssignmentStatement, "guarded")
    descriptor = None
    for klass in vhdl_statement_SignalAssignmentStatement.__mro__:
        if "guarded" in klass.__dict__:
            descriptor = klass.__dict__["guarded"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_statement_simplesimultaneousstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_SimpleSimultaneousStatement)


def test_vhdl_statement_simplesimultaneousstatement_constructor_exists():
    assert callable(vhdl_statement_SimpleSimultaneousStatement.__init__)


def test_vhdl_statement_simplesimultaneousstatement_constructor_args():
    sig = inspect.signature(vhdl_statement_SimpleSimultaneousStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_statement_procedurecallstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_ProcedureCallStatement)


def test_vhdl_statement_procedurecallstatement_constructor_exists():
    assert callable(vhdl_statement_ProcedureCallStatement.__init__)


def test_vhdl_statement_procedurecallstatement_constructor_args():
    sig = inspect.signature(vhdl_statement_ProcedureCallStatement.__init__)
    params = list(sig.parameters.keys())
    assert "postponed" in params, "Missing parameter 'postponed'"

def test_vhdl_statement_procedurecallstatement_has_postponed():
    assert hasattr(vhdl_statement_ProcedureCallStatement, "postponed")
    descriptor = None
    for klass in vhdl_statement_ProcedureCallStatement.__mro__:
        if "postponed" in klass.__dict__:
            descriptor = klass.__dict__["postponed"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_statement_reportstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_ReportStatement)


def test_vhdl_statement_reportstatement_constructor_exists():
    assert callable(vhdl_statement_ReportStatement.__init__)


def test_vhdl_statement_reportstatement_constructor_args():
    sig = inspect.signature(vhdl_statement_ReportStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_statement_instantiationstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_InstantiationStatement)


def test_vhdl_statement_instantiationstatement_constructor_exists():
    assert callable(vhdl_statement_InstantiationStatement.__init__)


def test_vhdl_statement_instantiationstatement_constructor_args():
    sig = inspect.signature(vhdl_statement_InstantiationStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_statement_processstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_ProcessStatement)


def test_vhdl_statement_processstatement_constructor_exists():
    assert callable(vhdl_statement_ProcessStatement.__init__)


def test_vhdl_statement_processstatement_constructor_args():
    sig = inspect.signature(vhdl_statement_ProcessStatement.__init__)
    params = list(sig.parameters.keys())
    assert "postponed" in params, "Missing parameter 'postponed'"

def test_vhdl_statement_processstatement_has_postponed():
    assert hasattr(vhdl_statement_ProcessStatement, "postponed")
    descriptor = None
    for klass in vhdl_statement_ProcessStatement.__mro__:
        if "postponed" in klass.__dict__:
            descriptor = klass.__dict__["postponed"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_statement_variableassignmentstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_VariableAssignmentStatement)


def test_vhdl_statement_variableassignmentstatement_constructor_exists():
    assert callable(vhdl_statement_VariableAssignmentStatement.__init__)


def test_vhdl_statement_variableassignmentstatement_constructor_args():
    sig = inspect.signature(vhdl_statement_VariableAssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_statement_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_ExpressionStatement)


def test_vhdl_statement_expressionstatement_constructor_exists():
    assert callable(vhdl_statement_ExpressionStatement.__init__)


def test_vhdl_statement_expressionstatement_constructor_args():
    sig = inspect.signature(vhdl_statement_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_statement_blockstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_BlockStatement)


def test_vhdl_statement_blockstatement_constructor_exists():
    assert callable(vhdl_statement_BlockStatement.__init__)


def test_vhdl_statement_blockstatement_constructor_args():
    sig = inspect.signature(vhdl_statement_BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_statement_exitstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_ExitStatement)


def test_vhdl_statement_exitstatement_constructor_exists():
    assert callable(vhdl_statement_ExitStatement.__init__)


def test_vhdl_statement_exitstatement_constructor_args():
    sig = inspect.signature(vhdl_statement_ExitStatement.__init__)
    params = list(sig.parameters.keys())
    assert "exit" in params, "Missing parameter 'exit'"

def test_vhdl_statement_exitstatement_has_exit():
    assert hasattr(vhdl_statement_ExitStatement, "exit")
    descriptor = None
    for klass in vhdl_statement_ExitStatement.__mro__:
        if "exit" in klass.__dict__:
            descriptor = klass.__dict__["exit"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_statement_nextstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_NextStatement)


def test_vhdl_statement_nextstatement_constructor_exists():
    assert callable(vhdl_statement_NextStatement.__init__)


def test_vhdl_statement_nextstatement_constructor_args():
    sig = inspect.signature(vhdl_statement_NextStatement.__init__)
    params = list(sig.parameters.keys())
    assert "next" in params, "Missing parameter 'next'"

def test_vhdl_statement_nextstatement_has_next():
    assert hasattr(vhdl_statement_NextStatement, "next")
    descriptor = None
    for klass in vhdl_statement_NextStatement.__mro__:
        if "next" in klass.__dict__:
            descriptor = klass.__dict__["next"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_statement_waitstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_WaitStatement)


def test_vhdl_statement_waitstatement_constructor_exists():
    assert callable(vhdl_statement_WaitStatement.__init__)


def test_vhdl_statement_waitstatement_constructor_args():
    sig = inspect.signature(vhdl_statement_WaitStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_statement_ifstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_IfStatement)


def test_vhdl_statement_ifstatement_constructor_exists():
    assert callable(vhdl_statement_IfStatement.__init__)


def test_vhdl_statement_ifstatement_constructor_args():
    sig = inspect.signature(vhdl_statement_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_statement_simultaneousproceduralstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_SimultaneousProceduralStatement)


def test_vhdl_statement_simultaneousproceduralstatement_constructor_exists():
    assert callable(vhdl_statement_SimultaneousProceduralStatement.__init__)


def test_vhdl_statement_simultaneousproceduralstatement_constructor_args():
    sig = inspect.signature(vhdl_statement_SimultaneousProceduralStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_statement_generatestatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_GenerateStatement)


def test_vhdl_statement_generatestatement_constructor_exists():
    assert callable(vhdl_statement_GenerateStatement.__init__)


def test_vhdl_statement_generatestatement_constructor_args():
    sig = inspect.signature(vhdl_statement_GenerateStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_statement_breakstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_BreakStatement)


def test_vhdl_statement_breakstatement_constructor_exists():
    assert callable(vhdl_statement_BreakStatement.__init__)


def test_vhdl_statement_breakstatement_constructor_args():
    sig = inspect.signature(vhdl_statement_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_statement_assertionstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl_statement_AssertionStatement)


def test_vhdl_statement_assertionstatement_constructor_exists():
    assert callable(vhdl_statement_AssertionStatement.__init__)


def test_vhdl_statement_assertionstatement_constructor_args():
    sig = inspect.signature(vhdl_statement_AssertionStatement.__init__)
    params = list(sig.parameters.keys())
    assert "postponed" in params, "Missing parameter 'postponed'"

def test_vhdl_statement_assertionstatement_has_postponed():
    assert hasattr(vhdl_statement_AssertionStatement, "postponed")
    descriptor = None
    for klass in vhdl_statement_AssertionStatement.__mro__:
        if "postponed" in klass.__dict__:
            descriptor = klass.__dict__["postponed"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_entityreference_is_not_abstract():
    assert not inspect.isabstract(vhdl_EntityReference)


def test_vhdl_entityreference_constructor_exists():
    assert callable(vhdl_EntityReference.__init__)


def test_vhdl_entityreference_constructor_args():
    sig = inspect.signature(vhdl_EntityReference.__init__)
    params = list(sig.parameters.keys())



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_declaration_attributespecification_is_not_abstract():
    assert not inspect.isabstract(vhdl_declaration_AttributeSpecification)


def test_vhdl_declaration_attributespecification_constructor_exists():
    assert callable(vhdl_declaration_AttributeSpecification.__init__)


def test_vhdl_declaration_attributespecification_constructor_args():
    sig = inspect.signature(vhdl_declaration_AttributeSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"

def test_vhdl_declaration_attributespecification_has_class_():
    assert hasattr(vhdl_declaration_AttributeSpecification, "class_")
    descriptor = None
    for klass in vhdl_declaration_AttributeSpecification.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_vhdl_declaration_groupdeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl_declaration_GroupDeclaration)


def test_vhdl_declaration_groupdeclaration_constructor_exists():
    assert callable(vhdl_declaration_GroupDeclaration.__init__)


def test_vhdl_declaration_groupdeclaration_constructor_args():
    sig = inspect.signature(vhdl_declaration_GroupDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_declaration_subprogramdeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl_declaration_SubprogramDeclaration)


def test_vhdl_declaration_subprogramdeclaration_constructor_exists():
    assert callable(vhdl_declaration_SubprogramDeclaration.__init__)


def test_vhdl_declaration_subprogramdeclaration_constructor_args():
    sig = inspect.signature(vhdl_declaration_SubprogramDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_declaration_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl_declaration_TypeDeclaration)


def test_vhdl_declaration_typedeclaration_constructor_exists():
    assert callable(vhdl_declaration_TypeDeclaration.__init__)


def test_vhdl_declaration_typedeclaration_constructor_args():
    sig = inspect.signature(vhdl_declaration_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_expression_subtypeindicationexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl_expression_SubtypeIndicationExpression)


def test_vhdl_expression_subtypeindicationexpression_constructor_exists():
    assert callable(vhdl_expression_SubtypeIndicationExpression.__init__)


def test_vhdl_expression_subtypeindicationexpression_constructor_args():
    sig = inspect.signature(vhdl_expression_SubtypeIndicationExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_declaration_aliasdeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl_declaration_AliasDeclaration)


def test_vhdl_declaration_aliasdeclaration_constructor_exists():
    assert callable(vhdl_declaration_AliasDeclaration.__init__)


def test_vhdl_declaration_aliasdeclaration_constructor_args():
    sig = inspect.signature(vhdl_declaration_AliasDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_configuration_blockconfiguration_is_not_abstract():
    assert not inspect.isabstract(vhdl_configuration_BlockConfiguration)


def test_vhdl_configuration_blockconfiguration_constructor_exists():
    assert callable(vhdl_configuration_BlockConfiguration.__init__)


def test_vhdl_configuration_blockconfiguration_constructor_args():
    sig = inspect.signature(vhdl_configuration_BlockConfiguration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_declaration_naturedeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl_declaration_NatureDeclaration)


def test_vhdl_declaration_naturedeclaration_constructor_exists():
    assert callable(vhdl_declaration_NatureDeclaration.__init__)


def test_vhdl_declaration_naturedeclaration_constructor_args():
    sig = inspect.signature(vhdl_declaration_NatureDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_declaration_subtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl_declaration_SubtypeDeclaration)


def test_vhdl_declaration_subtypedeclaration_constructor_exists():
    assert callable(vhdl_declaration_SubtypeDeclaration.__init__)


def test_vhdl_declaration_subtypedeclaration_constructor_args():
    sig = inspect.signature(vhdl_declaration_SubtypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_declaration_subnaturedeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl_declaration_SubnatureDeclaration)


def test_vhdl_declaration_subnaturedeclaration_constructor_exists():
    assert callable(vhdl_declaration_SubnatureDeclaration.__init__)


def test_vhdl_declaration_subnaturedeclaration_constructor_args():
    sig = inspect.signature(vhdl_declaration_SubnatureDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_declaration_attributedeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl_declaration_AttributeDeclaration)


def test_vhdl_declaration_attributedeclaration_constructor_exists():
    assert callable(vhdl_declaration_AttributeDeclaration.__init__)


def test_vhdl_declaration_attributedeclaration_constructor_args():
    sig = inspect.signature(vhdl_declaration_AttributeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_component_is_not_abstract():
    assert not inspect.isabstract(vhdl_Component)


def test_vhdl_component_constructor_exists():
    assert callable(vhdl_Component.__init__)


def test_vhdl_component_constructor_args():
    sig = inspect.signature(vhdl_Component.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_declaration_grouptemplatedeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl_declaration_GroupTemplateDeclaration)


def test_vhdl_declaration_grouptemplatedeclaration_constructor_exists():
    assert callable(vhdl_declaration_GroupTemplateDeclaration.__init__)


def test_vhdl_declaration_grouptemplatedeclaration_constructor_args():
    sig = inspect.signature(vhdl_declaration_GroupTemplateDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "entry" in params, "Missing parameter 'entry'"

def test_vhdl_declaration_grouptemplatedeclaration_has_entry():
    assert hasattr(vhdl_declaration_GroupTemplateDeclaration, "entry")
    descriptor = None
    for klass in vhdl_declaration_GroupTemplateDeclaration.__mro__:
        if "entry" in klass.__dict__:
            descriptor = klass.__dict__["entry"]
            break
    assert isinstance(descriptor, property)



def test_module_is_not_abstract():
    assert not inspect.isabstract(Module)


def test_module_constructor_exists():
    assert callable(Module.__init__)


def test_module_constructor_args():
    sig = inspect.signature(Module.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_entity_is_not_abstract():
    assert not inspect.isabstract(vhdl_Entity)


def test_vhdl_entity_constructor_exists():
    assert callable(vhdl_Entity.__init__)


def test_vhdl_entity_constructor_args():
    sig = inspect.signature(vhdl_Entity.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_configuration_configuration_is_not_abstract():
    assert not inspect.isabstract(vhdl_configuration_Configuration)


def test_vhdl_configuration_configuration_constructor_exists():
    assert callable(vhdl_configuration_Configuration.__init__)


def test_vhdl_configuration_configuration_constructor_args():
    sig = inspect.signature(vhdl_configuration_Configuration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_package_is_not_abstract():
    assert not inspect.isabstract(vhdl_Package)


def test_vhdl_package_constructor_exists():
    assert callable(vhdl_Package.__init__)


def test_vhdl_package_constructor_args():
    sig = inspect.signature(vhdl_Package.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_packagebody_is_not_abstract():
    assert not inspect.isabstract(vhdl_PackageBody)


def test_vhdl_packagebody_constructor_exists():
    assert callable(vhdl_PackageBody.__init__)


def test_vhdl_packagebody_constructor_args():
    sig = inspect.signature(vhdl_PackageBody.__init__)
    params = list(sig.parameters.keys())



def test_vhdl_architecture_is_not_abstract():
    assert not inspect.isabstract(vhdl_Architecture)


def test_vhdl_architecture_constructor_exists():
    assert callable(vhdl_Architecture.__init__)


def test_vhdl_architecture_constructor_args():
    sig = inspect.signature(vhdl_Architecture.__init__)
    params = list(sig.parameters.keys())

def test_multiplyingoperator_exists():
    # Check that the Enumeration exists
    assert MultiplyingOperator is not None

def test_multiplyingoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MultiplyingOperator]
    expected_literals = [
        "REM",
        "MOD",
        "MUL",
        "DIV",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MultiplyingOperator"

def test_relationaloperator_exists():
    # Check that the Enumeration exists
    assert RelationalOperator is not None

def test_relationaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalOperator]
    expected_literals = [
        "LOWERTHAN",
        "LE",
        "EQ",
        "NEQ",
        "GE",
        "GREATERTHAN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationalOperator"

def test_shiftoperator_exists():
    # Check that the Enumeration exists
    assert ShiftOperator is not None

def test_shiftoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ShiftOperator]
    expected_literals = [
        "SLL",
        "SLA",
        "ROL",
        "SRA",
        "SRL",
        "ROR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ShiftOperator"

def test_logicaloperator_exists():
    # Check that the Enumeration exists
    assert LogicalOperator is not None

def test_logicaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicalOperator]
    expected_literals = [
        "NAND",
        "OR",
        "AND",
        "XNOR",
        "XOR",
        "NOR",
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
        "REGISTER",
        "BUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SignalKind"

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
        "OUT",
        "INOUT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Mode"

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

def test_entityclass_exists():
    # Check that the Enumeration exists
    assert EntityClass is not None

def test_entityclass_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EntityClass]
    expected_literals = [
        "VARIABLE",
        "FILE",
        "QUANTITY",
        "SUBNATURE",
        "ENTITY",
        "LABEL",
        "ARCHITECTURE",
        "PROCEDURE",
        "FUNCTION",
        "NATURE",
        "UNITS",
        "CONFIGURATION",
        "COMPONENT",
        "PACKAGE",
        "TYPE",
        "SIGNAL",
        "GROUP",
        "LITERAL",
        "TERMINAL",
        "CONSTANT",
        "SUBTYPE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EntityClass"


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
vhdl_configuration_ConfigurationReference_strategy = st.builds(
    vhdl_configuration_ConfigurationReference,
)
configuration_vhdl_EntityReference_strategy = st.builds(
    configuration_vhdl_EntityReference,
)
BlockConfiguration_strategy = st.builds(
    BlockConfiguration,
)
configuration_vhdl_PortMaps_strategy = st.builds(
    configuration_vhdl_PortMaps,
)
configuration_vhdl_GenericMaps_strategy = st.builds(
    configuration_vhdl_GenericMaps,
)
configuration_vhdl_MultiName_strategy = st.builds(
    configuration_vhdl_MultiName,
)
ConfigurationItem_strategy = st.builds(
    ConfigurationItem,
)
vhdl_configuration_ComponentConfiguration_strategy = st.builds(
    vhdl_configuration_ComponentConfiguration,
)
configuration_vhdl_Name_strategy = st.builds(
    configuration_vhdl_Name,
)
configuration_ConfigurationItem_strategy = st.builds(
    configuration_ConfigurationItem,
)
nature_CompositeNatureDefinition_strategy = st.builds(
    nature_CompositeNatureDefinition,
)
vhdl_type_TypeReference_strategy = st.builds(
    vhdl_type_TypeReference,
)
vhdl_type_Typed_strategy = st.builds(
    vhdl_type_Typed,
)
vhdl_nature_Natured_strategy = st.builds(
    vhdl_nature_Natured,
)
vhdl_nature_NatureReference_strategy = st.builds(
    vhdl_nature_NatureReference,
)
nature_vhdl_Name_strategy = st.builds(
    nature_vhdl_Name,
)
RecordNatureElement_strategy = st.builds(
    RecordNatureElement,
)
CompositeNatureDefinition_strategy = st.builds(
    CompositeNatureDefinition,
)
vhdl_nature_RecordNatureDefinition_strategy = st.builds(
    vhdl_nature_RecordNatureDefinition,
)
ArrayNatureDefinition_strategy = st.builds(
    ArrayNatureDefinition,
)
vhdl_nature_UnconstrainedArrayNatureDefinition_strategy = st.builds(
    vhdl_nature_UnconstrainedArrayNatureDefinition,
)
vhdl_nature_ConstrainedArrayNatureDefinition_strategy = st.builds(
    vhdl_nature_ConstrainedArrayNatureDefinition,
)
type_vhdl_Name_strategy = st.builds(
    type_vhdl_Name,
)
vhdl_type_PhysicalTypeDefinitionSecondary_strategy = st.builds(
    vhdl_type_PhysicalTypeDefinitionSecondary,
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
vhdl_type_EnumerationLiteral_strategy = st.builds(
    vhdl_type_EnumerationLiteral,
)
ArrayTypeDefinition_strategy = st.builds(
    ArrayTypeDefinition,
)
vhdl_type_UnconstrainedArrayTypeDefinition_strategy = st.builds(
    vhdl_type_UnconstrainedArrayTypeDefinition,
)
vhdl_type_ConstrainedArrayTypeDefinition_strategy = st.builds(
    vhdl_type_ConstrainedArrayTypeDefinition,
)
type_CompositeTypeDefinition_strategy = st.builds(
    type_CompositeTypeDefinition,
)
RecordTypeElement_strategy = st.builds(
    RecordTypeElement,
)
CompositeTypeDefinition_strategy = st.builds(
    CompositeTypeDefinition,
)
vhdl_type_RecordTypeDefinition_strategy = st.builds(
    vhdl_type_RecordTypeDefinition,
)
type_TypeDefinition_strategy = st.builds(
    type_TypeDefinition,
)
TypeDefinition_strategy = st.builds(
    TypeDefinition,
)
vhdl_type_EnumerationTypeDefinition_strategy = st.builds(
    vhdl_type_EnumerationTypeDefinition,
)
vhdl_type_PhysicalTypeDefinition_strategy = st.builds(
    vhdl_type_PhysicalTypeDefinition,
    primary=
        safe_text
)
vhdl_type_RangeTypeDefinition_strategy = st.builds(
    vhdl_type_RangeTypeDefinition,
    direction=
        safe_text
)
vhdl_type_CompositeTypeDefinition_strategy = st.builds(
    vhdl_type_CompositeTypeDefinition,
)
NatureDefinition_strategy = st.builds(
    NatureDefinition,
)
vhdl_nature_CompositeNatureDefinition_strategy = st.builds(
    vhdl_nature_CompositeNatureDefinition,
)
vhdl_nature_ScalarNatureDefinition_strategy = st.builds(
    vhdl_nature_ScalarNatureDefinition,
)
ValueDeclaration_strategy = st.builds(
    ValueDeclaration,
)
vhdl_declaration_SignalDeclaration_strategy = st.builds(
    vhdl_declaration_SignalDeclaration,
    kind=
        safe_text,
    mode=
        safe_text
)
vhdl_declaration_VariableDeclaration_strategy = st.builds(
    vhdl_declaration_VariableDeclaration,
    mode=
        safe_text,
    shared=
        st.booleans()
)
vhdl_declaration_ConstantDeclaration_strategy = st.builds(
    vhdl_declaration_ConstantDeclaration,
)
SubprogramBody_strategy = st.builds(
    SubprogramBody,
)
declaration_vhdl_PortMaps_strategy = st.builds(
    declaration_vhdl_PortMaps,
)
declaration_vhdl_GenericMaps_strategy = st.builds(
    declaration_vhdl_GenericMaps,
)
declaration_vhdl_EntityReference_strategy = st.builds(
    declaration_vhdl_EntityReference,
)
declaration_vhdl_ComponentReference_strategy = st.builds(
    declaration_vhdl_ComponentReference,
)
declaration_SubprogramDeclaration_strategy = st.builds(
    declaration_SubprogramDeclaration,
)
nature_Natured_strategy = st.builds(
    nature_Natured,
)
vhdl_nature_ArrayNatureDefinition_strategy = st.builds(
    vhdl_nature_ArrayNatureDefinition,
)
SourceAspect_strategy = st.builds(
    SourceAspect,
)
vhdl_ams_Noise_strategy = st.builds(
    vhdl_ams_Noise,
)
vhdl_ams_Spectrum_strategy = st.builds(
    vhdl_ams_Spectrum,
)
MultiNamed_strategy = st.builds(
    MultiNamed,
)
declaration_QuantityDeclaration_strategy = st.builds(
    declaration_QuantityDeclaration,
)
QuantityAspect_strategy = st.builds(
    QuantityAspect,
)
QuantityDeclaration_strategy = st.builds(
    QuantityDeclaration,
)
vhdl_declaration_BranchQuantityDeclaration_strategy = st.builds(
    vhdl_declaration_BranchQuantityDeclaration,
)
declaration_vhdl_MultiName_strategy = st.builds(
    declaration_vhdl_MultiName,
)
declaration_vhdl_Name_strategy = st.builds(
    declaration_vhdl_Name,
)
AssociationExpression_strategy = st.builds(
    AssociationExpression,
)
vhdl_expression_ConditionalWaveformExpression_strategy = st.builds(
    vhdl_expression_ConditionalWaveformExpression,
)
type_EnumerationLiteral_strategy = st.builds(
    type_EnumerationLiteral,
)
expression_BinaryExpression_strategy = st.builds(
    expression_BinaryExpression,
)
expression_vhdl_Name_strategy = st.builds(
    expression_vhdl_Name,
)
NatureReference_strategy = st.builds(
    NatureReference,
)
expression_IndicationExpression_strategy = st.builds(
    expression_IndicationExpression,
)
ValueExpression_strategy = st.builds(
    ValueExpression,
)
vhdl_expression_UnitValueExpression_strategy = st.builds(
    vhdl_expression_UnitValueExpression,
)
vhdl_expression_BitStringExpression_strategy = st.builds(
    vhdl_expression_BitStringExpression,
)
expression_vhdl_Signature_strategy = st.builds(
    expression_vhdl_Signature,
)
expression_ValueExpression_strategy = st.builds(
    expression_ValueExpression,
)
type_Typed_strategy = st.builds(
    type_Typed,
)
vhdl_declaration_FunctionDeclaration_strategy = st.builds(
    vhdl_declaration_FunctionDeclaration,
    purity=
        safe_text
)
vhdl_type_FileTypeDefinition_strategy = st.builds(
    vhdl_type_FileTypeDefinition,
)
vhdl_declaration_FreeQuantityDeclaration_strategy = st.builds(
    vhdl_declaration_FreeQuantityDeclaration,
)
vhdl_declaration_SourceQuantityDeclaration_strategy = st.builds(
    vhdl_declaration_SourceQuantityDeclaration,
)
vhdl_type_AccessTypeDefinition_strategy = st.builds(
    vhdl_type_AccessTypeDefinition,
)
vhdl_type_ArrayTypeDefinition_strategy = st.builds(
    vhdl_type_ArrayTypeDefinition,
)
expression_Expression_strategy = st.builds(
    expression_Expression,
)
vhdl_expression_AllocatorExpression_strategy = st.builds(
    vhdl_expression_AllocatorExpression,
)
Name_strategy = st.builds(
    Name,
)
vhdl_expression_CharacterExpression_strategy = st.builds(
    vhdl_expression_CharacterExpression,
)
vhdl_expression_RangeExpression_strategy = st.builds(
    vhdl_expression_RangeExpression,
    direction=
        safe_text
)
vhdl_expression_AllExpression_strategy = st.builds(
    vhdl_expression_AllExpression,
)
vhdl_expression_NameExpression_strategy = st.builds(
    vhdl_expression_NameExpression,
)
vhdl_expression_TypeQualificationExpression_strategy = st.builds(
    vhdl_expression_TypeQualificationExpression,
)
vhdl_expression_IdentifierExpression_strategy = st.builds(
    vhdl_expression_IdentifierExpression,
)
vhdl_expression_AttributeExpression_strategy = st.builds(
    vhdl_expression_AttributeExpression,
)
vhdl_expression_SignatureExpression_strategy = st.builds(
    vhdl_expression_SignatureExpression,
)
vhdl_expression_StringExpression_strategy = st.builds(
    vhdl_expression_StringExpression,
)
vhdl_expression_OthersExpression_strategy = st.builds(
    vhdl_expression_OthersExpression,
)
expression_MultiExpression_strategy = st.builds(
    expression_MultiExpression,
)
vhdl_expression_AggregateExpression_strategy = st.builds(
    vhdl_expression_AggregateExpression,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
vhdl_expression_LogicalExpression_strategy = st.builds(
    vhdl_expression_LogicalExpression,
    operator=
        safe_text
)
vhdl_expression_MultiplyingExpression_strategy = st.builds(
    vhdl_expression_MultiplyingExpression,
    operator=
        safe_text
)
vhdl_expression_ShiftExpression_strategy = st.builds(
    vhdl_expression_ShiftExpression,
    operator=
        safe_text
)
vhdl_expression_RelationalExpression_strategy = st.builds(
    vhdl_expression_RelationalExpression,
    operator=
        safe_text
)
vhdl_expression_PowerExpression_strategy = st.builds(
    vhdl_expression_PowerExpression,
)
vhdl_expression_AddingExpression_strategy = st.builds(
    vhdl_expression_AddingExpression,
    operator=
        safe_text
)
ConfigurationReference_strategy = st.builds(
    ConfigurationReference,
)
statement_vhdl_EntityReference_strategy = st.builds(
    statement_vhdl_EntityReference,
)
IterationScheme_strategy = st.builds(
    IterationScheme,
)
vhdl_statement_WhileIterationScheme_strategy = st.builds(
    vhdl_statement_WhileIterationScheme,
)
vhdl_statement_ForIterationScheme_strategy = st.builds(
    vhdl_statement_ForIterationScheme,
    variable=
        safe_text
)
GenerationScheme_strategy = st.builds(
    GenerationScheme,
)
vhdl_statement_ForGenerationScheme_strategy = st.builds(
    vhdl_statement_ForGenerationScheme,
    variable=
        safe_text
)
vhdl_statement_IfGenerationScheme_strategy = st.builds(
    vhdl_statement_IfGenerationScheme,
)
statement_vhdl_ComponentReference_strategy = st.builds(
    statement_vhdl_ComponentReference,
)
InstantiationStatement_strategy = st.builds(
    InstantiationStatement,
)
vhdl_statement_ConfigurationInstantiationStatement_strategy = st.builds(
    vhdl_statement_ConfigurationInstantiationStatement,
)
vhdl_statement_EntityInstantiationStatement_strategy = st.builds(
    vhdl_statement_EntityInstantiationStatement,
)
vhdl_statement_ComponentInstantiationStatement_strategy = st.builds(
    vhdl_statement_ComponentInstantiationStatement,
)
statement_vhdl_Name_strategy = st.builds(
    statement_vhdl_Name,
)
BreakStatementItem_strategy = st.builds(
    BreakStatementItem,
)
statement_vhdl_PortMaps_strategy = st.builds(
    statement_vhdl_PortMaps,
)
statement_vhdl_Ports_strategy = st.builds(
    statement_vhdl_Ports,
)
statement_vhdl_GenericMaps_strategy = st.builds(
    statement_vhdl_GenericMaps,
)
statement_vhdl_Generics_strategy = st.builds(
    statement_vhdl_Generics,
)
CaseAlternative_strategy = st.builds(
    CaseAlternative,
)
CaseStatement_strategy = st.builds(
    CaseStatement,
)
vhdl_statement_SimultaneousCaseStatement_strategy = st.builds(
    vhdl_statement_SimultaneousCaseStatement,
)
statement_vhdl_CallReference_strategy = st.builds(
    statement_vhdl_CallReference,
)
IfStatementTest_strategy = st.builds(
    IfStatementTest,
)
IfStatement_strategy = st.builds(
    IfStatement,
)
vhdl_statement_SimultaneousIfStatement_strategy = st.builds(
    vhdl_statement_SimultaneousIfStatement,
)
vhdl_ComponentReference_strategy = st.builds(
    vhdl_ComponentReference,
)
statement_vhdl_MultiName_strategy = st.builds(
    statement_vhdl_MultiName,
)
DelayMechanism_strategy = st.builds(
    DelayMechanism,
)
vhdl_statement_TransportMechanism_strategy = st.builds(
    vhdl_statement_TransportMechanism,
)
vhdl_statement_RejectMechanism_strategy = st.builds(
    vhdl_statement_RejectMechanism,
)
ConditionalSignalAssignmentStatement_strategy = st.builds(
    ConditionalSignalAssignmentStatement,
)
vhdl_statement_SelectedSignalAssignmentStatement_strategy = st.builds(
    vhdl_statement_SelectedSignalAssignmentStatement,
)
SignalAssignmentStatement_strategy = st.builds(
    SignalAssignmentStatement,
)
vhdl_statement_SequentialSignalAssignmentStatement_strategy = st.builds(
    vhdl_statement_SequentialSignalAssignmentStatement,
)
vhdl_statement_ConditionalSignalAssignmentStatement_strategy = st.builds(
    vhdl_statement_ConditionalSignalAssignmentStatement,
)
ExpressionStatement_strategy = st.builds(
    ExpressionStatement,
)
vhdl_statement_ReturnStatement_strategy = st.builds(
    vhdl_statement_ReturnStatement,
)
SubprogramDeclaration_strategy = st.builds(
    SubprogramDeclaration,
)
vhdl_declaration_ProcedureDeclaration_strategy = st.builds(
    vhdl_declaration_ProcedureDeclaration,
)
vhdl_CallReference_strategy = st.builds(
    vhdl_CallReference,
)
vhdl_VhdlObject_strategy = st.builds(
    vhdl_VhdlObject,
    id=
        safe_text
)
vhdl_MultiName_strategy = st.builds(
    vhdl_MultiName,
)
vhdl_MultiNamed_strategy = st.builds(
    vhdl_MultiNamed,
)
vhdl_Named_strategy = st.builds(
    vhdl_Named,
)
CallReference_strategy = st.builds(
    CallReference,
)
vhdl_CallResolvedReference_strategy = st.builds(
    vhdl_CallResolvedReference,
)
configuration_ConfigurationReference_strategy = st.builds(
    configuration_ConfigurationReference,
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
nature_NatureReference_strategy = st.builds(
    nature_NatureReference,
)
vhdl_expression_SubnatureIndicationExpression_strategy = st.builds(
    vhdl_expression_SubnatureIndicationExpression,
)
type_TypeReference_strategy = st.builds(
    type_TypeReference,
)
MultiName_strategy = st.builds(
    MultiName,
)
declaration_Declaration_strategy = st.builds(
    declaration_Declaration,
)
vhdl_declaration_DisconnectionSpecification_strategy = st.builds(
    vhdl_declaration_DisconnectionSpecification,
)
vhdl_declaration_FileDeclaration_strategy = st.builds(
    vhdl_declaration_FileDeclaration,
)
vhdl_declaration_TerminalDeclaration_strategy = st.builds(
    vhdl_declaration_TerminalDeclaration,
)
vhdl_declaration_ValueDeclaration_strategy = st.builds(
    vhdl_declaration_ValueDeclaration,
)
vhdl_declaration_LimitDeclaration_strategy = st.builds(
    vhdl_declaration_LimitDeclaration,
)
TypeReference_strategy = st.builds(
    TypeReference,
)
vhdl_PackageReference_strategy = st.builds(
    vhdl_PackageReference,
)
Expression_strategy = st.builds(
    Expression,
)
vhdl_expression_UnaryExpression_strategy = st.builds(
    vhdl_expression_UnaryExpression,
    operator=
        safe_text
)
vhdl_expression_NullExpression_strategy = st.builds(
    vhdl_expression_NullExpression,
)
vhdl_expression_BinaryExpression_strategy = st.builds(
    vhdl_expression_BinaryExpression,
)
vhdl_expression_OpenExpression_strategy = st.builds(
    vhdl_expression_OpenExpression,
)
vhdl_expression_WaveformExpression_strategy = st.builds(
    vhdl_expression_WaveformExpression,
)
vhdl_expression_ValueExpression_strategy = st.builds(
    vhdl_expression_ValueExpression,
    value=
        safe_text
)
vhdl_expression_SignExpression_strategy = st.builds(
    vhdl_expression_SignExpression,
    sign=
        safe_text
)
vhdl_expression_MultiExpression_strategy = st.builds(
    vhdl_expression_MultiExpression,
)
vhdl_expression_IndicationExpression_strategy = st.builds(
    vhdl_expression_IndicationExpression,
)
vhdl_expression_AssociationExpression_strategy = st.builds(
    vhdl_expression_AssociationExpression,
)
vhdl_expression_UnaffectedExpression_strategy = st.builds(
    vhdl_expression_UnaffectedExpression,
)
Declaration_strategy = st.builds(
    Declaration,
)
vhdl_declaration_QuantityDeclaration_strategy = st.builds(
    vhdl_declaration_QuantityDeclaration,
)
vhdl_declaration_ConfigurationSpecification_strategy = st.builds(
    vhdl_declaration_ConfigurationSpecification,
)
vhdl_declaration_UseClauseDeclaration_strategy = st.builds(
    vhdl_declaration_UseClauseDeclaration,
)
vhdl_Name_strategy = st.builds(
    vhdl_Name,
)
VhdlObject_strategy = st.builds(
    VhdlObject,
)
vhdl_type_TypeDefinition_strategy = st.builds(
    vhdl_type_TypeDefinition,
)
vhdl_statement_IterationScheme_strategy = st.builds(
    vhdl_statement_IterationScheme,
)
vhdl_Module_strategy = st.builds(
    vhdl_Module,
)
vhdl_declaration_Declaration_strategy = st.builds(
    vhdl_declaration_Declaration,
)
vhdl_EntityResolvedReference_strategy = st.builds(
    vhdl_EntityResolvedReference,
)
vhdl_Generics_strategy = st.builds(
    vhdl_Generics,
)
vhdl_configuration_ConfigurationItem_strategy = st.builds(
    vhdl_configuration_ConfigurationItem,
)
vhdl_type_RecordTypeElement_strategy = st.builds(
    vhdl_type_RecordTypeElement,
)
vhdl_statement_CaseAlternative_strategy = st.builds(
    vhdl_statement_CaseAlternative,
)
vhdl_Signature_strategy = st.builds(
    vhdl_Signature,
)
vhdl_statement_BreakStatementItem_strategy = st.builds(
    vhdl_statement_BreakStatementItem,
)
vhdl_statement_Statement_strategy = st.builds(
    vhdl_statement_Statement,
    label=
        safe_text
)
vhdl_nature_NatureDefinition_strategy = st.builds(
    vhdl_nature_NatureDefinition,
)
vhdl_GenericMaps_strategy = st.builds(
    vhdl_GenericMaps,
)
vhdl_NameList_strategy = st.builds(
    vhdl_NameList,
)
vhdl_Ports_strategy = st.builds(
    vhdl_Ports,
)
vhdl_statement_DelayMechanism_strategy = st.builds(
    vhdl_statement_DelayMechanism,
)
vhdl_declaration_SubprogramBody_strategy = st.builds(
    vhdl_declaration_SubprogramBody,
)
vhdl_ams_SourceAspect_strategy = st.builds(
    vhdl_ams_SourceAspect,
)
vhdl_Model_strategy = st.builds(
    vhdl_Model,
)
vhdl_PortMaps_strategy = st.builds(
    vhdl_PortMaps,
)
vhdl_statement_IfStatementTest_strategy = st.builds(
    vhdl_statement_IfStatementTest,
)
vhdl_nature_RecordNatureElement_strategy = st.builds(
    vhdl_nature_RecordNatureElement,
)
vhdl_expression_Expression_strategy = st.builds(
    vhdl_expression_Expression,
)
vhdl_ams_QuantityAspect_strategy = st.builds(
    vhdl_ams_QuantityAspect,
)
vhdl_statement_GenerationScheme_strategy = st.builds(
    vhdl_statement_GenerationScheme,
)
vhdl_ComponentResolvedReference_strategy = st.builds(
    vhdl_ComponentResolvedReference,
)
vhdl_PackageResolvedReference_strategy = st.builds(
    vhdl_PackageResolvedReference,
)
vhdl_configuration_ConfigurationResolvedReference_strategy = st.builds(
    vhdl_configuration_ConfigurationResolvedReference,
)
vhdl_DesignUnit_strategy = st.builds(
    vhdl_DesignUnit,
    library=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
vhdl_statement_CaseStatement_strategy = st.builds(
    vhdl_statement_CaseStatement,
)
vhdl_statement_LoopStatement_strategy = st.builds(
    vhdl_statement_LoopStatement,
)
vhdl_statement_SignalAssignmentStatement_strategy = st.builds(
    vhdl_statement_SignalAssignmentStatement,
    postponed=
        st.booleans(),
    guarded=
        st.booleans()
)
vhdl_statement_SimpleSimultaneousStatement_strategy = st.builds(
    vhdl_statement_SimpleSimultaneousStatement,
)
vhdl_statement_ProcedureCallStatement_strategy = st.builds(
    vhdl_statement_ProcedureCallStatement,
    postponed=
        st.booleans()
)
vhdl_statement_ReportStatement_strategy = st.builds(
    vhdl_statement_ReportStatement,
)
vhdl_statement_InstantiationStatement_strategy = st.builds(
    vhdl_statement_InstantiationStatement,
)
vhdl_statement_ProcessStatement_strategy = st.builds(
    vhdl_statement_ProcessStatement,
    postponed=
        st.booleans()
)
vhdl_statement_VariableAssignmentStatement_strategy = st.builds(
    vhdl_statement_VariableAssignmentStatement,
)
vhdl_statement_ExpressionStatement_strategy = st.builds(
    vhdl_statement_ExpressionStatement,
)
vhdl_statement_BlockStatement_strategy = st.builds(
    vhdl_statement_BlockStatement,
)
vhdl_statement_ExitStatement_strategy = st.builds(
    vhdl_statement_ExitStatement,
    exit=
        safe_text
)
vhdl_statement_NextStatement_strategy = st.builds(
    vhdl_statement_NextStatement,
    next=
        safe_text
)
vhdl_statement_WaitStatement_strategy = st.builds(
    vhdl_statement_WaitStatement,
)
vhdl_statement_IfStatement_strategy = st.builds(
    vhdl_statement_IfStatement,
)
vhdl_statement_SimultaneousProceduralStatement_strategy = st.builds(
    vhdl_statement_SimultaneousProceduralStatement,
)
vhdl_statement_GenerateStatement_strategy = st.builds(
    vhdl_statement_GenerateStatement,
)
vhdl_statement_BreakStatement_strategy = st.builds(
    vhdl_statement_BreakStatement,
)
vhdl_statement_AssertionStatement_strategy = st.builds(
    vhdl_statement_AssertionStatement,
    postponed=
        st.booleans()
)
vhdl_EntityReference_strategy = st.builds(
    vhdl_EntityReference,
)
Named_strategy = st.builds(
    Named,
)
vhdl_declaration_AttributeSpecification_strategy = st.builds(
    vhdl_declaration_AttributeSpecification,
    class_=
        safe_text
)
vhdl_declaration_GroupDeclaration_strategy = st.builds(
    vhdl_declaration_GroupDeclaration,
)
vhdl_declaration_SubprogramDeclaration_strategy = st.builds(
    vhdl_declaration_SubprogramDeclaration,
)
vhdl_declaration_TypeDeclaration_strategy = st.builds(
    vhdl_declaration_TypeDeclaration,
)
vhdl_expression_SubtypeIndicationExpression_strategy = st.builds(
    vhdl_expression_SubtypeIndicationExpression,
)
vhdl_declaration_AliasDeclaration_strategy = st.builds(
    vhdl_declaration_AliasDeclaration,
)
vhdl_configuration_BlockConfiguration_strategy = st.builds(
    vhdl_configuration_BlockConfiguration,
)
vhdl_declaration_NatureDeclaration_strategy = st.builds(
    vhdl_declaration_NatureDeclaration,
)
vhdl_declaration_SubtypeDeclaration_strategy = st.builds(
    vhdl_declaration_SubtypeDeclaration,
)
vhdl_declaration_SubnatureDeclaration_strategy = st.builds(
    vhdl_declaration_SubnatureDeclaration,
)
vhdl_declaration_AttributeDeclaration_strategy = st.builds(
    vhdl_declaration_AttributeDeclaration,
)
vhdl_Component_strategy = st.builds(
    vhdl_Component,
)
vhdl_declaration_GroupTemplateDeclaration_strategy = st.builds(
    vhdl_declaration_GroupTemplateDeclaration,
    entry=
        safe_text
)
Module_strategy = st.builds(
    Module,
)
vhdl_Entity_strategy = st.builds(
    vhdl_Entity,
)
vhdl_configuration_Configuration_strategy = st.builds(
    vhdl_configuration_Configuration,
)
vhdl_Package_strategy = st.builds(
    vhdl_Package,
)
vhdl_PackageBody_strategy = st.builds(
    vhdl_PackageBody,
)
vhdl_Architecture_strategy = st.builds(
    vhdl_Architecture,
)

@given(instance=Configuration_strategy)
@settings(max_examples=50)
def test_configuration_instantiation(instance):
    assert isinstance(instance, Configuration)

@given(instance=vhdl_configuration_ConfigurationReference_strategy)
@settings(max_examples=50)
def test_vhdl_configuration_configurationreference_instantiation(instance):
    assert isinstance(instance, vhdl_configuration_ConfigurationReference)

@given(instance=configuration_vhdl_EntityReference_strategy)
@settings(max_examples=50)
def test_configuration_vhdl_entityreference_instantiation(instance):
    assert isinstance(instance, configuration_vhdl_EntityReference)

@given(instance=BlockConfiguration_strategy)
@settings(max_examples=50)
def test_blockconfiguration_instantiation(instance):
    assert isinstance(instance, BlockConfiguration)

@given(instance=configuration_vhdl_PortMaps_strategy)
@settings(max_examples=50)
def test_configuration_vhdl_portmaps_instantiation(instance):
    assert isinstance(instance, configuration_vhdl_PortMaps)

@given(instance=configuration_vhdl_GenericMaps_strategy)
@settings(max_examples=50)
def test_configuration_vhdl_genericmaps_instantiation(instance):
    assert isinstance(instance, configuration_vhdl_GenericMaps)

@given(instance=configuration_vhdl_MultiName_strategy)
@settings(max_examples=50)
def test_configuration_vhdl_multiname_instantiation(instance):
    assert isinstance(instance, configuration_vhdl_MultiName)

@given(instance=ConfigurationItem_strategy)
@settings(max_examples=50)
def test_configurationitem_instantiation(instance):
    assert isinstance(instance, ConfigurationItem)

@given(instance=vhdl_configuration_ComponentConfiguration_strategy)
@settings(max_examples=50)
def test_vhdl_configuration_componentconfiguration_instantiation(instance):
    assert isinstance(instance, vhdl_configuration_ComponentConfiguration)

@given(instance=configuration_vhdl_Name_strategy)
@settings(max_examples=50)
def test_configuration_vhdl_name_instantiation(instance):
    assert isinstance(instance, configuration_vhdl_Name)

@given(instance=configuration_ConfigurationItem_strategy)
@settings(max_examples=50)
def test_configuration_configurationitem_instantiation(instance):
    assert isinstance(instance, configuration_ConfigurationItem)

@given(instance=nature_CompositeNatureDefinition_strategy)
@settings(max_examples=50)
def test_nature_compositenaturedefinition_instantiation(instance):
    assert isinstance(instance, nature_CompositeNatureDefinition)

@given(instance=vhdl_type_TypeReference_strategy)
@settings(max_examples=50)
def test_vhdl_type_typereference_instantiation(instance):
    assert isinstance(instance, vhdl_type_TypeReference)

@given(instance=vhdl_type_Typed_strategy)
@settings(max_examples=50)
def test_vhdl_type_typed_instantiation(instance):
    assert isinstance(instance, vhdl_type_Typed)

@given(instance=vhdl_nature_Natured_strategy)
@settings(max_examples=50)
def test_vhdl_nature_natured_instantiation(instance):
    assert isinstance(instance, vhdl_nature_Natured)

@given(instance=vhdl_nature_NatureReference_strategy)
@settings(max_examples=50)
def test_vhdl_nature_naturereference_instantiation(instance):
    assert isinstance(instance, vhdl_nature_NatureReference)

@given(instance=nature_vhdl_Name_strategy)
@settings(max_examples=50)
def test_nature_vhdl_name_instantiation(instance):
    assert isinstance(instance, nature_vhdl_Name)

@given(instance=RecordNatureElement_strategy)
@settings(max_examples=50)
def test_recordnatureelement_instantiation(instance):
    assert isinstance(instance, RecordNatureElement)

@given(instance=CompositeNatureDefinition_strategy)
@settings(max_examples=50)
def test_compositenaturedefinition_instantiation(instance):
    assert isinstance(instance, CompositeNatureDefinition)

@given(instance=vhdl_nature_RecordNatureDefinition_strategy)
@settings(max_examples=50)
def test_vhdl_nature_recordnaturedefinition_instantiation(instance):
    assert isinstance(instance, vhdl_nature_RecordNatureDefinition)

@given(instance=ArrayNatureDefinition_strategy)
@settings(max_examples=50)
def test_arraynaturedefinition_instantiation(instance):
    assert isinstance(instance, ArrayNatureDefinition)

@given(instance=vhdl_nature_UnconstrainedArrayNatureDefinition_strategy)
@settings(max_examples=50)
def test_vhdl_nature_unconstrainedarraynaturedefinition_instantiation(instance):
    assert isinstance(instance, vhdl_nature_UnconstrainedArrayNatureDefinition)

@given(instance=vhdl_nature_ConstrainedArrayNatureDefinition_strategy)
@settings(max_examples=50)
def test_vhdl_nature_constrainedarraynaturedefinition_instantiation(instance):
    assert isinstance(instance, vhdl_nature_ConstrainedArrayNatureDefinition)

@given(instance=type_vhdl_Name_strategy)
@settings(max_examples=50)
def test_type_vhdl_name_instantiation(instance):
    assert isinstance(instance, type_vhdl_Name)

@given(instance=vhdl_type_PhysicalTypeDefinitionSecondary_strategy)
@settings(max_examples=50)
def test_vhdl_type_physicaltypedefinitionsecondary_instantiation(instance):
    assert isinstance(instance, vhdl_type_PhysicalTypeDefinitionSecondary)



@given(instance=vhdl_type_PhysicalTypeDefinitionSecondary_strategy)
def test_vhdl_type_physicaltypedefinitionsecondary_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=vhdl_type_PhysicalTypeDefinitionSecondary_strategy)
def test_vhdl_type_physicaltypedefinitionsecondary_name_setter(instance):
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

@given(instance=vhdl_type_EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_vhdl_type_enumerationliteral_instantiation(instance):
    assert isinstance(instance, vhdl_type_EnumerationLiteral)

@given(instance=ArrayTypeDefinition_strategy)
@settings(max_examples=50)
def test_arraytypedefinition_instantiation(instance):
    assert isinstance(instance, ArrayTypeDefinition)

@given(instance=vhdl_type_UnconstrainedArrayTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl_type_unconstrainedarraytypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl_type_UnconstrainedArrayTypeDefinition)

@given(instance=vhdl_type_ConstrainedArrayTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl_type_constrainedarraytypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl_type_ConstrainedArrayTypeDefinition)

@given(instance=type_CompositeTypeDefinition_strategy)
@settings(max_examples=50)
def test_type_compositetypedefinition_instantiation(instance):
    assert isinstance(instance, type_CompositeTypeDefinition)

@given(instance=RecordTypeElement_strategy)
@settings(max_examples=50)
def test_recordtypeelement_instantiation(instance):
    assert isinstance(instance, RecordTypeElement)

@given(instance=CompositeTypeDefinition_strategy)
@settings(max_examples=50)
def test_compositetypedefinition_instantiation(instance):
    assert isinstance(instance, CompositeTypeDefinition)

@given(instance=vhdl_type_RecordTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl_type_recordtypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl_type_RecordTypeDefinition)

@given(instance=type_TypeDefinition_strategy)
@settings(max_examples=50)
def test_type_typedefinition_instantiation(instance):
    assert isinstance(instance, type_TypeDefinition)

@given(instance=TypeDefinition_strategy)
@settings(max_examples=50)
def test_typedefinition_instantiation(instance):
    assert isinstance(instance, TypeDefinition)

@given(instance=vhdl_type_EnumerationTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl_type_enumerationtypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl_type_EnumerationTypeDefinition)

@given(instance=vhdl_type_PhysicalTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl_type_physicaltypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl_type_PhysicalTypeDefinition)



@given(instance=vhdl_type_PhysicalTypeDefinition_strategy)
def test_vhdl_type_physicaltypedefinition_primary_setter(instance):
    original = instance.primary
    instance.primary = original
    assert instance.primary == original

@given(instance=vhdl_type_RangeTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl_type_rangetypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl_type_RangeTypeDefinition)



@given(instance=vhdl_type_RangeTypeDefinition_strategy)
def test_vhdl_type_rangetypedefinition_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=vhdl_type_CompositeTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl_type_compositetypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl_type_CompositeTypeDefinition)

@given(instance=NatureDefinition_strategy)
@settings(max_examples=50)
def test_naturedefinition_instantiation(instance):
    assert isinstance(instance, NatureDefinition)

@given(instance=vhdl_nature_CompositeNatureDefinition_strategy)
@settings(max_examples=50)
def test_vhdl_nature_compositenaturedefinition_instantiation(instance):
    assert isinstance(instance, vhdl_nature_CompositeNatureDefinition)

@given(instance=vhdl_nature_ScalarNatureDefinition_strategy)
@settings(max_examples=50)
def test_vhdl_nature_scalarnaturedefinition_instantiation(instance):
    assert isinstance(instance, vhdl_nature_ScalarNatureDefinition)

@given(instance=ValueDeclaration_strategy)
@settings(max_examples=50)
def test_valuedeclaration_instantiation(instance):
    assert isinstance(instance, ValueDeclaration)

@given(instance=vhdl_declaration_SignalDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl_declaration_signaldeclaration_instantiation(instance):
    assert isinstance(instance, vhdl_declaration_SignalDeclaration)



@given(instance=vhdl_declaration_SignalDeclaration_strategy)
def test_vhdl_declaration_signaldeclaration_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=vhdl_declaration_SignalDeclaration_strategy)
def test_vhdl_declaration_signaldeclaration_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=vhdl_declaration_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl_declaration_variabledeclaration_instantiation(instance):
    assert isinstance(instance, vhdl_declaration_VariableDeclaration)



@given(instance=vhdl_declaration_VariableDeclaration_strategy)
def test_vhdl_declaration_variabledeclaration_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original



@given(instance=vhdl_declaration_VariableDeclaration_strategy)
def test_vhdl_declaration_variabledeclaration_shared_setter(instance):
    original = instance.shared
    instance.shared = original
    assert instance.shared == original

@given(instance=vhdl_declaration_ConstantDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl_declaration_constantdeclaration_instantiation(instance):
    assert isinstance(instance, vhdl_declaration_ConstantDeclaration)

@given(instance=SubprogramBody_strategy)
@settings(max_examples=50)
def test_subprogrambody_instantiation(instance):
    assert isinstance(instance, SubprogramBody)

@given(instance=declaration_vhdl_PortMaps_strategy)
@settings(max_examples=50)
def test_declaration_vhdl_portmaps_instantiation(instance):
    assert isinstance(instance, declaration_vhdl_PortMaps)

@given(instance=declaration_vhdl_GenericMaps_strategy)
@settings(max_examples=50)
def test_declaration_vhdl_genericmaps_instantiation(instance):
    assert isinstance(instance, declaration_vhdl_GenericMaps)

@given(instance=declaration_vhdl_EntityReference_strategy)
@settings(max_examples=50)
def test_declaration_vhdl_entityreference_instantiation(instance):
    assert isinstance(instance, declaration_vhdl_EntityReference)

@given(instance=declaration_vhdl_ComponentReference_strategy)
@settings(max_examples=50)
def test_declaration_vhdl_componentreference_instantiation(instance):
    assert isinstance(instance, declaration_vhdl_ComponentReference)

@given(instance=declaration_SubprogramDeclaration_strategy)
@settings(max_examples=50)
def test_declaration_subprogramdeclaration_instantiation(instance):
    assert isinstance(instance, declaration_SubprogramDeclaration)

@given(instance=nature_Natured_strategy)
@settings(max_examples=50)
def test_nature_natured_instantiation(instance):
    assert isinstance(instance, nature_Natured)

@given(instance=vhdl_nature_ArrayNatureDefinition_strategy)
@settings(max_examples=50)
def test_vhdl_nature_arraynaturedefinition_instantiation(instance):
    assert isinstance(instance, vhdl_nature_ArrayNatureDefinition)

@given(instance=SourceAspect_strategy)
@settings(max_examples=50)
def test_sourceaspect_instantiation(instance):
    assert isinstance(instance, SourceAspect)

@given(instance=vhdl_ams_Noise_strategy)
@settings(max_examples=50)
def test_vhdl_ams_noise_instantiation(instance):
    assert isinstance(instance, vhdl_ams_Noise)

@given(instance=vhdl_ams_Spectrum_strategy)
@settings(max_examples=50)
def test_vhdl_ams_spectrum_instantiation(instance):
    assert isinstance(instance, vhdl_ams_Spectrum)

@given(instance=MultiNamed_strategy)
@settings(max_examples=50)
def test_multinamed_instantiation(instance):
    assert isinstance(instance, MultiNamed)

@given(instance=declaration_QuantityDeclaration_strategy)
@settings(max_examples=50)
def test_declaration_quantitydeclaration_instantiation(instance):
    assert isinstance(instance, declaration_QuantityDeclaration)

@given(instance=QuantityAspect_strategy)
@settings(max_examples=50)
def test_quantityaspect_instantiation(instance):
    assert isinstance(instance, QuantityAspect)

@given(instance=QuantityDeclaration_strategy)
@settings(max_examples=50)
def test_quantitydeclaration_instantiation(instance):
    assert isinstance(instance, QuantityDeclaration)

@given(instance=vhdl_declaration_BranchQuantityDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl_declaration_branchquantitydeclaration_instantiation(instance):
    assert isinstance(instance, vhdl_declaration_BranchQuantityDeclaration)

@given(instance=declaration_vhdl_MultiName_strategy)
@settings(max_examples=50)
def test_declaration_vhdl_multiname_instantiation(instance):
    assert isinstance(instance, declaration_vhdl_MultiName)

@given(instance=declaration_vhdl_Name_strategy)
@settings(max_examples=50)
def test_declaration_vhdl_name_instantiation(instance):
    assert isinstance(instance, declaration_vhdl_Name)

@given(instance=AssociationExpression_strategy)
@settings(max_examples=50)
def test_associationexpression_instantiation(instance):
    assert isinstance(instance, AssociationExpression)

@given(instance=vhdl_expression_ConditionalWaveformExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_conditionalwaveformexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_ConditionalWaveformExpression)

@given(instance=type_EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_type_enumerationliteral_instantiation(instance):
    assert isinstance(instance, type_EnumerationLiteral)

@given(instance=expression_BinaryExpression_strategy)
@settings(max_examples=50)
def test_expression_binaryexpression_instantiation(instance):
    assert isinstance(instance, expression_BinaryExpression)

@given(instance=expression_vhdl_Name_strategy)
@settings(max_examples=50)
def test_expression_vhdl_name_instantiation(instance):
    assert isinstance(instance, expression_vhdl_Name)

@given(instance=NatureReference_strategy)
@settings(max_examples=50)
def test_naturereference_instantiation(instance):
    assert isinstance(instance, NatureReference)

@given(instance=expression_IndicationExpression_strategy)
@settings(max_examples=50)
def test_expression_indicationexpression_instantiation(instance):
    assert isinstance(instance, expression_IndicationExpression)

@given(instance=ValueExpression_strategy)
@settings(max_examples=50)
def test_valueexpression_instantiation(instance):
    assert isinstance(instance, ValueExpression)

@given(instance=vhdl_expression_UnitValueExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_unitvalueexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_UnitValueExpression)

@given(instance=vhdl_expression_BitStringExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_bitstringexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_BitStringExpression)

@given(instance=expression_vhdl_Signature_strategy)
@settings(max_examples=50)
def test_expression_vhdl_signature_instantiation(instance):
    assert isinstance(instance, expression_vhdl_Signature)

@given(instance=expression_ValueExpression_strategy)
@settings(max_examples=50)
def test_expression_valueexpression_instantiation(instance):
    assert isinstance(instance, expression_ValueExpression)

@given(instance=type_Typed_strategy)
@settings(max_examples=50)
def test_type_typed_instantiation(instance):
    assert isinstance(instance, type_Typed)

@given(instance=vhdl_declaration_FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl_declaration_functiondeclaration_instantiation(instance):
    assert isinstance(instance, vhdl_declaration_FunctionDeclaration)



@given(instance=vhdl_declaration_FunctionDeclaration_strategy)
def test_vhdl_declaration_functiondeclaration_purity_setter(instance):
    original = instance.purity
    instance.purity = original
    assert instance.purity == original

@given(instance=vhdl_type_FileTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl_type_filetypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl_type_FileTypeDefinition)

@given(instance=vhdl_declaration_FreeQuantityDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl_declaration_freequantitydeclaration_instantiation(instance):
    assert isinstance(instance, vhdl_declaration_FreeQuantityDeclaration)

@given(instance=vhdl_declaration_SourceQuantityDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl_declaration_sourcequantitydeclaration_instantiation(instance):
    assert isinstance(instance, vhdl_declaration_SourceQuantityDeclaration)

@given(instance=vhdl_type_AccessTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl_type_accesstypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl_type_AccessTypeDefinition)

@given(instance=vhdl_type_ArrayTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl_type_arraytypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl_type_ArrayTypeDefinition)

@given(instance=expression_Expression_strategy)
@settings(max_examples=50)
def test_expression_expression_instantiation(instance):
    assert isinstance(instance, expression_Expression)

@given(instance=vhdl_expression_AllocatorExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_allocatorexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_AllocatorExpression)

@given(instance=Name_strategy)
@settings(max_examples=50)
def test_name_instantiation(instance):
    assert isinstance(instance, Name)

@given(instance=vhdl_expression_CharacterExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_characterexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_CharacterExpression)

@given(instance=vhdl_expression_RangeExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_rangeexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_RangeExpression)



@given(instance=vhdl_expression_RangeExpression_strategy)
def test_vhdl_expression_rangeexpression_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=vhdl_expression_AllExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_allexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_AllExpression)

@given(instance=vhdl_expression_NameExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_nameexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_NameExpression)

@given(instance=vhdl_expression_TypeQualificationExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_typequalificationexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_TypeQualificationExpression)

@given(instance=vhdl_expression_IdentifierExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_identifierexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_IdentifierExpression)

@given(instance=vhdl_expression_AttributeExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_attributeexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_AttributeExpression)

@given(instance=vhdl_expression_SignatureExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_signatureexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_SignatureExpression)

@given(instance=vhdl_expression_StringExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_stringexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_StringExpression)

@given(instance=vhdl_expression_OthersExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_othersexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_OthersExpression)

@given(instance=expression_MultiExpression_strategy)
@settings(max_examples=50)
def test_expression_multiexpression_instantiation(instance):
    assert isinstance(instance, expression_MultiExpression)

@given(instance=vhdl_expression_AggregateExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_aggregateexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_AggregateExpression)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=vhdl_expression_LogicalExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_logicalexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_LogicalExpression)



@given(instance=vhdl_expression_LogicalExpression_strategy)
def test_vhdl_expression_logicalexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=vhdl_expression_MultiplyingExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_multiplyingexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_MultiplyingExpression)



@given(instance=vhdl_expression_MultiplyingExpression_strategy)
def test_vhdl_expression_multiplyingexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=vhdl_expression_ShiftExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_shiftexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_ShiftExpression)



@given(instance=vhdl_expression_ShiftExpression_strategy)
def test_vhdl_expression_shiftexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=vhdl_expression_RelationalExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_relationalexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_RelationalExpression)



@given(instance=vhdl_expression_RelationalExpression_strategy)
def test_vhdl_expression_relationalexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=vhdl_expression_PowerExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_powerexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_PowerExpression)

@given(instance=vhdl_expression_AddingExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_addingexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_AddingExpression)



@given(instance=vhdl_expression_AddingExpression_strategy)
def test_vhdl_expression_addingexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ConfigurationReference_strategy)
@settings(max_examples=50)
def test_configurationreference_instantiation(instance):
    assert isinstance(instance, ConfigurationReference)

@given(instance=statement_vhdl_EntityReference_strategy)
@settings(max_examples=50)
def test_statement_vhdl_entityreference_instantiation(instance):
    assert isinstance(instance, statement_vhdl_EntityReference)

@given(instance=IterationScheme_strategy)
@settings(max_examples=50)
def test_iterationscheme_instantiation(instance):
    assert isinstance(instance, IterationScheme)

@given(instance=vhdl_statement_WhileIterationScheme_strategy)
@settings(max_examples=50)
def test_vhdl_statement_whileiterationscheme_instantiation(instance):
    assert isinstance(instance, vhdl_statement_WhileIterationScheme)

@given(instance=vhdl_statement_ForIterationScheme_strategy)
@settings(max_examples=50)
def test_vhdl_statement_foriterationscheme_instantiation(instance):
    assert isinstance(instance, vhdl_statement_ForIterationScheme)



@given(instance=vhdl_statement_ForIterationScheme_strategy)
def test_vhdl_statement_foriterationscheme_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=GenerationScheme_strategy)
@settings(max_examples=50)
def test_generationscheme_instantiation(instance):
    assert isinstance(instance, GenerationScheme)

@given(instance=vhdl_statement_ForGenerationScheme_strategy)
@settings(max_examples=50)
def test_vhdl_statement_forgenerationscheme_instantiation(instance):
    assert isinstance(instance, vhdl_statement_ForGenerationScheme)



@given(instance=vhdl_statement_ForGenerationScheme_strategy)
def test_vhdl_statement_forgenerationscheme_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=vhdl_statement_IfGenerationScheme_strategy)
@settings(max_examples=50)
def test_vhdl_statement_ifgenerationscheme_instantiation(instance):
    assert isinstance(instance, vhdl_statement_IfGenerationScheme)

@given(instance=statement_vhdl_ComponentReference_strategy)
@settings(max_examples=50)
def test_statement_vhdl_componentreference_instantiation(instance):
    assert isinstance(instance, statement_vhdl_ComponentReference)

@given(instance=InstantiationStatement_strategy)
@settings(max_examples=50)
def test_instantiationstatement_instantiation(instance):
    assert isinstance(instance, InstantiationStatement)

@given(instance=vhdl_statement_ConfigurationInstantiationStatement_strategy)
@settings(max_examples=50)
def test_vhdl_statement_configurationinstantiationstatement_instantiation(instance):
    assert isinstance(instance, vhdl_statement_ConfigurationInstantiationStatement)

@given(instance=vhdl_statement_EntityInstantiationStatement_strategy)
@settings(max_examples=50)
def test_vhdl_statement_entityinstantiationstatement_instantiation(instance):
    assert isinstance(instance, vhdl_statement_EntityInstantiationStatement)

@given(instance=vhdl_statement_ComponentInstantiationStatement_strategy)
@settings(max_examples=50)
def test_vhdl_statement_componentinstantiationstatement_instantiation(instance):
    assert isinstance(instance, vhdl_statement_ComponentInstantiationStatement)

@given(instance=statement_vhdl_Name_strategy)
@settings(max_examples=50)
def test_statement_vhdl_name_instantiation(instance):
    assert isinstance(instance, statement_vhdl_Name)

@given(instance=BreakStatementItem_strategy)
@settings(max_examples=50)
def test_breakstatementitem_instantiation(instance):
    assert isinstance(instance, BreakStatementItem)

@given(instance=statement_vhdl_PortMaps_strategy)
@settings(max_examples=50)
def test_statement_vhdl_portmaps_instantiation(instance):
    assert isinstance(instance, statement_vhdl_PortMaps)

@given(instance=statement_vhdl_Ports_strategy)
@settings(max_examples=50)
def test_statement_vhdl_ports_instantiation(instance):
    assert isinstance(instance, statement_vhdl_Ports)

@given(instance=statement_vhdl_GenericMaps_strategy)
@settings(max_examples=50)
def test_statement_vhdl_genericmaps_instantiation(instance):
    assert isinstance(instance, statement_vhdl_GenericMaps)

@given(instance=statement_vhdl_Generics_strategy)
@settings(max_examples=50)
def test_statement_vhdl_generics_instantiation(instance):
    assert isinstance(instance, statement_vhdl_Generics)

@given(instance=CaseAlternative_strategy)
@settings(max_examples=50)
def test_casealternative_instantiation(instance):
    assert isinstance(instance, CaseAlternative)

@given(instance=CaseStatement_strategy)
@settings(max_examples=50)
def test_casestatement_instantiation(instance):
    assert isinstance(instance, CaseStatement)

@given(instance=vhdl_statement_SimultaneousCaseStatement_strategy)
@settings(max_examples=50)
def test_vhdl_statement_simultaneouscasestatement_instantiation(instance):
    assert isinstance(instance, vhdl_statement_SimultaneousCaseStatement)

@given(instance=statement_vhdl_CallReference_strategy)
@settings(max_examples=50)
def test_statement_vhdl_callreference_instantiation(instance):
    assert isinstance(instance, statement_vhdl_CallReference)

@given(instance=IfStatementTest_strategy)
@settings(max_examples=50)
def test_ifstatementtest_instantiation(instance):
    assert isinstance(instance, IfStatementTest)

@given(instance=IfStatement_strategy)
@settings(max_examples=50)
def test_ifstatement_instantiation(instance):
    assert isinstance(instance, IfStatement)

@given(instance=vhdl_statement_SimultaneousIfStatement_strategy)
@settings(max_examples=50)
def test_vhdl_statement_simultaneousifstatement_instantiation(instance):
    assert isinstance(instance, vhdl_statement_SimultaneousIfStatement)

@given(instance=vhdl_ComponentReference_strategy)
@settings(max_examples=50)
def test_vhdl_componentreference_instantiation(instance):
    assert isinstance(instance, vhdl_ComponentReference)

@given(instance=statement_vhdl_MultiName_strategy)
@settings(max_examples=50)
def test_statement_vhdl_multiname_instantiation(instance):
    assert isinstance(instance, statement_vhdl_MultiName)

@given(instance=DelayMechanism_strategy)
@settings(max_examples=50)
def test_delaymechanism_instantiation(instance):
    assert isinstance(instance, DelayMechanism)

@given(instance=vhdl_statement_TransportMechanism_strategy)
@settings(max_examples=50)
def test_vhdl_statement_transportmechanism_instantiation(instance):
    assert isinstance(instance, vhdl_statement_TransportMechanism)

@given(instance=vhdl_statement_RejectMechanism_strategy)
@settings(max_examples=50)
def test_vhdl_statement_rejectmechanism_instantiation(instance):
    assert isinstance(instance, vhdl_statement_RejectMechanism)

@given(instance=ConditionalSignalAssignmentStatement_strategy)
@settings(max_examples=50)
def test_conditionalsignalassignmentstatement_instantiation(instance):
    assert isinstance(instance, ConditionalSignalAssignmentStatement)

@given(instance=vhdl_statement_SelectedSignalAssignmentStatement_strategy)
@settings(max_examples=50)
def test_vhdl_statement_selectedsignalassignmentstatement_instantiation(instance):
    assert isinstance(instance, vhdl_statement_SelectedSignalAssignmentStatement)

@given(instance=SignalAssignmentStatement_strategy)
@settings(max_examples=50)
def test_signalassignmentstatement_instantiation(instance):
    assert isinstance(instance, SignalAssignmentStatement)

@given(instance=vhdl_statement_SequentialSignalAssignmentStatement_strategy)
@settings(max_examples=50)
def test_vhdl_statement_sequentialsignalassignmentstatement_instantiation(instance):
    assert isinstance(instance, vhdl_statement_SequentialSignalAssignmentStatement)

@given(instance=vhdl_statement_ConditionalSignalAssignmentStatement_strategy)
@settings(max_examples=50)
def test_vhdl_statement_conditionalsignalassignmentstatement_instantiation(instance):
    assert isinstance(instance, vhdl_statement_ConditionalSignalAssignmentStatement)

@given(instance=ExpressionStatement_strategy)
@settings(max_examples=50)
def test_expressionstatement_instantiation(instance):
    assert isinstance(instance, ExpressionStatement)

@given(instance=vhdl_statement_ReturnStatement_strategy)
@settings(max_examples=50)
def test_vhdl_statement_returnstatement_instantiation(instance):
    assert isinstance(instance, vhdl_statement_ReturnStatement)

@given(instance=SubprogramDeclaration_strategy)
@settings(max_examples=50)
def test_subprogramdeclaration_instantiation(instance):
    assert isinstance(instance, SubprogramDeclaration)

@given(instance=vhdl_declaration_ProcedureDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl_declaration_proceduredeclaration_instantiation(instance):
    assert isinstance(instance, vhdl_declaration_ProcedureDeclaration)

@given(instance=vhdl_CallReference_strategy)
@settings(max_examples=50)
def test_vhdl_callreference_instantiation(instance):
    assert isinstance(instance, vhdl_CallReference)

@given(instance=vhdl_VhdlObject_strategy)
@settings(max_examples=50)
def test_vhdl_vhdlobject_instantiation(instance):
    assert isinstance(instance, vhdl_VhdlObject)



@given(instance=vhdl_VhdlObject_strategy)
def test_vhdl_vhdlobject_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=vhdl_MultiName_strategy)
@settings(max_examples=50)
def test_vhdl_multiname_instantiation(instance):
    assert isinstance(instance, vhdl_MultiName)

@given(instance=vhdl_MultiNamed_strategy)
@settings(max_examples=50)
def test_vhdl_multinamed_instantiation(instance):
    assert isinstance(instance, vhdl_MultiNamed)

@given(instance=vhdl_Named_strategy)
@settings(max_examples=50)
def test_vhdl_named_instantiation(instance):
    assert isinstance(instance, vhdl_Named)

@given(instance=CallReference_strategy)
@settings(max_examples=50)
def test_callreference_instantiation(instance):
    assert isinstance(instance, CallReference)

@given(instance=vhdl_CallResolvedReference_strategy)
@settings(max_examples=50)
def test_vhdl_callresolvedreference_instantiation(instance):
    assert isinstance(instance, vhdl_CallResolvedReference)

@given(instance=configuration_ConfigurationReference_strategy)
@settings(max_examples=50)
def test_configuration_configurationreference_instantiation(instance):
    assert isinstance(instance, configuration_ConfigurationReference)

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

@given(instance=nature_NatureReference_strategy)
@settings(max_examples=50)
def test_nature_naturereference_instantiation(instance):
    assert isinstance(instance, nature_NatureReference)

@given(instance=vhdl_expression_SubnatureIndicationExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_subnatureindicationexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_SubnatureIndicationExpression)

@given(instance=type_TypeReference_strategy)
@settings(max_examples=50)
def test_type_typereference_instantiation(instance):
    assert isinstance(instance, type_TypeReference)

@given(instance=MultiName_strategy)
@settings(max_examples=50)
def test_multiname_instantiation(instance):
    assert isinstance(instance, MultiName)

@given(instance=declaration_Declaration_strategy)
@settings(max_examples=50)
def test_declaration_declaration_instantiation(instance):
    assert isinstance(instance, declaration_Declaration)

@given(instance=vhdl_declaration_DisconnectionSpecification_strategy)
@settings(max_examples=50)
def test_vhdl_declaration_disconnectionspecification_instantiation(instance):
    assert isinstance(instance, vhdl_declaration_DisconnectionSpecification)

@given(instance=vhdl_declaration_FileDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl_declaration_filedeclaration_instantiation(instance):
    assert isinstance(instance, vhdl_declaration_FileDeclaration)

@given(instance=vhdl_declaration_TerminalDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl_declaration_terminaldeclaration_instantiation(instance):
    assert isinstance(instance, vhdl_declaration_TerminalDeclaration)

@given(instance=vhdl_declaration_ValueDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl_declaration_valuedeclaration_instantiation(instance):
    assert isinstance(instance, vhdl_declaration_ValueDeclaration)

@given(instance=vhdl_declaration_LimitDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl_declaration_limitdeclaration_instantiation(instance):
    assert isinstance(instance, vhdl_declaration_LimitDeclaration)

@given(instance=TypeReference_strategy)
@settings(max_examples=50)
def test_typereference_instantiation(instance):
    assert isinstance(instance, TypeReference)

@given(instance=vhdl_PackageReference_strategy)
@settings(max_examples=50)
def test_vhdl_packagereference_instantiation(instance):
    assert isinstance(instance, vhdl_PackageReference)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=vhdl_expression_UnaryExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_unaryexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_UnaryExpression)



@given(instance=vhdl_expression_UnaryExpression_strategy)
def test_vhdl_expression_unaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=vhdl_expression_NullExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_nullexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_NullExpression)

@given(instance=vhdl_expression_BinaryExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_binaryexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_BinaryExpression)

@given(instance=vhdl_expression_OpenExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_openexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_OpenExpression)

@given(instance=vhdl_expression_WaveformExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_waveformexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_WaveformExpression)

@given(instance=vhdl_expression_ValueExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_valueexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_ValueExpression)



@given(instance=vhdl_expression_ValueExpression_strategy)
def test_vhdl_expression_valueexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vhdl_expression_SignExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_signexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_SignExpression)



@given(instance=vhdl_expression_SignExpression_strategy)
def test_vhdl_expression_signexpression_sign_setter(instance):
    original = instance.sign
    instance.sign = original
    assert instance.sign == original

@given(instance=vhdl_expression_MultiExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_multiexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_MultiExpression)

@given(instance=vhdl_expression_IndicationExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_indicationexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_IndicationExpression)

@given(instance=vhdl_expression_AssociationExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_associationexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_AssociationExpression)

@given(instance=vhdl_expression_UnaffectedExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_unaffectedexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_UnaffectedExpression)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=vhdl_declaration_QuantityDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl_declaration_quantitydeclaration_instantiation(instance):
    assert isinstance(instance, vhdl_declaration_QuantityDeclaration)

@given(instance=vhdl_declaration_ConfigurationSpecification_strategy)
@settings(max_examples=50)
def test_vhdl_declaration_configurationspecification_instantiation(instance):
    assert isinstance(instance, vhdl_declaration_ConfigurationSpecification)

@given(instance=vhdl_declaration_UseClauseDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl_declaration_useclausedeclaration_instantiation(instance):
    assert isinstance(instance, vhdl_declaration_UseClauseDeclaration)

@given(instance=vhdl_Name_strategy)
@settings(max_examples=50)
def test_vhdl_name_instantiation(instance):
    assert isinstance(instance, vhdl_Name)

@given(instance=VhdlObject_strategy)
@settings(max_examples=50)
def test_vhdlobject_instantiation(instance):
    assert isinstance(instance, VhdlObject)

@given(instance=vhdl_type_TypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl_type_typedefinition_instantiation(instance):
    assert isinstance(instance, vhdl_type_TypeDefinition)

@given(instance=vhdl_statement_IterationScheme_strategy)
@settings(max_examples=50)
def test_vhdl_statement_iterationscheme_instantiation(instance):
    assert isinstance(instance, vhdl_statement_IterationScheme)

@given(instance=vhdl_Module_strategy)
@settings(max_examples=50)
def test_vhdl_module_instantiation(instance):
    assert isinstance(instance, vhdl_Module)

@given(instance=vhdl_declaration_Declaration_strategy)
@settings(max_examples=50)
def test_vhdl_declaration_declaration_instantiation(instance):
    assert isinstance(instance, vhdl_declaration_Declaration)

@given(instance=vhdl_EntityResolvedReference_strategy)
@settings(max_examples=50)
def test_vhdl_entityresolvedreference_instantiation(instance):
    assert isinstance(instance, vhdl_EntityResolvedReference)

@given(instance=vhdl_Generics_strategy)
@settings(max_examples=50)
def test_vhdl_generics_instantiation(instance):
    assert isinstance(instance, vhdl_Generics)

@given(instance=vhdl_configuration_ConfigurationItem_strategy)
@settings(max_examples=50)
def test_vhdl_configuration_configurationitem_instantiation(instance):
    assert isinstance(instance, vhdl_configuration_ConfigurationItem)

@given(instance=vhdl_type_RecordTypeElement_strategy)
@settings(max_examples=50)
def test_vhdl_type_recordtypeelement_instantiation(instance):
    assert isinstance(instance, vhdl_type_RecordTypeElement)

@given(instance=vhdl_statement_CaseAlternative_strategy)
@settings(max_examples=50)
def test_vhdl_statement_casealternative_instantiation(instance):
    assert isinstance(instance, vhdl_statement_CaseAlternative)

@given(instance=vhdl_Signature_strategy)
@settings(max_examples=50)
def test_vhdl_signature_instantiation(instance):
    assert isinstance(instance, vhdl_Signature)

@given(instance=vhdl_statement_BreakStatementItem_strategy)
@settings(max_examples=50)
def test_vhdl_statement_breakstatementitem_instantiation(instance):
    assert isinstance(instance, vhdl_statement_BreakStatementItem)

@given(instance=vhdl_statement_Statement_strategy)
@settings(max_examples=50)
def test_vhdl_statement_statement_instantiation(instance):
    assert isinstance(instance, vhdl_statement_Statement)



@given(instance=vhdl_statement_Statement_strategy)
def test_vhdl_statement_statement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=vhdl_nature_NatureDefinition_strategy)
@settings(max_examples=50)
def test_vhdl_nature_naturedefinition_instantiation(instance):
    assert isinstance(instance, vhdl_nature_NatureDefinition)

@given(instance=vhdl_GenericMaps_strategy)
@settings(max_examples=50)
def test_vhdl_genericmaps_instantiation(instance):
    assert isinstance(instance, vhdl_GenericMaps)

@given(instance=vhdl_NameList_strategy)
@settings(max_examples=50)
def test_vhdl_namelist_instantiation(instance):
    assert isinstance(instance, vhdl_NameList)

@given(instance=vhdl_Ports_strategy)
@settings(max_examples=50)
def test_vhdl_ports_instantiation(instance):
    assert isinstance(instance, vhdl_Ports)

@given(instance=vhdl_statement_DelayMechanism_strategy)
@settings(max_examples=50)
def test_vhdl_statement_delaymechanism_instantiation(instance):
    assert isinstance(instance, vhdl_statement_DelayMechanism)

@given(instance=vhdl_declaration_SubprogramBody_strategy)
@settings(max_examples=50)
def test_vhdl_declaration_subprogrambody_instantiation(instance):
    assert isinstance(instance, vhdl_declaration_SubprogramBody)

@given(instance=vhdl_ams_SourceAspect_strategy)
@settings(max_examples=50)
def test_vhdl_ams_sourceaspect_instantiation(instance):
    assert isinstance(instance, vhdl_ams_SourceAspect)

@given(instance=vhdl_Model_strategy)
@settings(max_examples=50)
def test_vhdl_model_instantiation(instance):
    assert isinstance(instance, vhdl_Model)

@given(instance=vhdl_PortMaps_strategy)
@settings(max_examples=50)
def test_vhdl_portmaps_instantiation(instance):
    assert isinstance(instance, vhdl_PortMaps)

@given(instance=vhdl_statement_IfStatementTest_strategy)
@settings(max_examples=50)
def test_vhdl_statement_ifstatementtest_instantiation(instance):
    assert isinstance(instance, vhdl_statement_IfStatementTest)

@given(instance=vhdl_nature_RecordNatureElement_strategy)
@settings(max_examples=50)
def test_vhdl_nature_recordnatureelement_instantiation(instance):
    assert isinstance(instance, vhdl_nature_RecordNatureElement)

@given(instance=vhdl_expression_Expression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_expression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_Expression)

@given(instance=vhdl_ams_QuantityAspect_strategy)
@settings(max_examples=50)
def test_vhdl_ams_quantityaspect_instantiation(instance):
    assert isinstance(instance, vhdl_ams_QuantityAspect)

@given(instance=vhdl_statement_GenerationScheme_strategy)
@settings(max_examples=50)
def test_vhdl_statement_generationscheme_instantiation(instance):
    assert isinstance(instance, vhdl_statement_GenerationScheme)

@given(instance=vhdl_ComponentResolvedReference_strategy)
@settings(max_examples=50)
def test_vhdl_componentresolvedreference_instantiation(instance):
    assert isinstance(instance, vhdl_ComponentResolvedReference)

@given(instance=vhdl_PackageResolvedReference_strategy)
@settings(max_examples=50)
def test_vhdl_packageresolvedreference_instantiation(instance):
    assert isinstance(instance, vhdl_PackageResolvedReference)

@given(instance=vhdl_configuration_ConfigurationResolvedReference_strategy)
@settings(max_examples=50)
def test_vhdl_configuration_configurationresolvedreference_instantiation(instance):
    assert isinstance(instance, vhdl_configuration_ConfigurationResolvedReference)

@given(instance=vhdl_DesignUnit_strategy)
@settings(max_examples=50)
def test_vhdl_designunit_instantiation(instance):
    assert isinstance(instance, vhdl_DesignUnit)



@given(instance=vhdl_DesignUnit_strategy)
def test_vhdl_designunit_library_setter(instance):
    original = instance.library
    instance.library = original
    assert instance.library == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=vhdl_statement_CaseStatement_strategy)
@settings(max_examples=50)
def test_vhdl_statement_casestatement_instantiation(instance):
    assert isinstance(instance, vhdl_statement_CaseStatement)

@given(instance=vhdl_statement_LoopStatement_strategy)
@settings(max_examples=50)
def test_vhdl_statement_loopstatement_instantiation(instance):
    assert isinstance(instance, vhdl_statement_LoopStatement)

@given(instance=vhdl_statement_SignalAssignmentStatement_strategy)
@settings(max_examples=50)
def test_vhdl_statement_signalassignmentstatement_instantiation(instance):
    assert isinstance(instance, vhdl_statement_SignalAssignmentStatement)



@given(instance=vhdl_statement_SignalAssignmentStatement_strategy)
def test_vhdl_statement_signalassignmentstatement_postponed_setter(instance):
    original = instance.postponed
    instance.postponed = original
    assert instance.postponed == original



@given(instance=vhdl_statement_SignalAssignmentStatement_strategy)
def test_vhdl_statement_signalassignmentstatement_guarded_setter(instance):
    original = instance.guarded
    instance.guarded = original
    assert instance.guarded == original

@given(instance=vhdl_statement_SimpleSimultaneousStatement_strategy)
@settings(max_examples=50)
def test_vhdl_statement_simplesimultaneousstatement_instantiation(instance):
    assert isinstance(instance, vhdl_statement_SimpleSimultaneousStatement)

@given(instance=vhdl_statement_ProcedureCallStatement_strategy)
@settings(max_examples=50)
def test_vhdl_statement_procedurecallstatement_instantiation(instance):
    assert isinstance(instance, vhdl_statement_ProcedureCallStatement)



@given(instance=vhdl_statement_ProcedureCallStatement_strategy)
def test_vhdl_statement_procedurecallstatement_postponed_setter(instance):
    original = instance.postponed
    instance.postponed = original
    assert instance.postponed == original

@given(instance=vhdl_statement_ReportStatement_strategy)
@settings(max_examples=50)
def test_vhdl_statement_reportstatement_instantiation(instance):
    assert isinstance(instance, vhdl_statement_ReportStatement)

@given(instance=vhdl_statement_InstantiationStatement_strategy)
@settings(max_examples=50)
def test_vhdl_statement_instantiationstatement_instantiation(instance):
    assert isinstance(instance, vhdl_statement_InstantiationStatement)

@given(instance=vhdl_statement_ProcessStatement_strategy)
@settings(max_examples=50)
def test_vhdl_statement_processstatement_instantiation(instance):
    assert isinstance(instance, vhdl_statement_ProcessStatement)



@given(instance=vhdl_statement_ProcessStatement_strategy)
def test_vhdl_statement_processstatement_postponed_setter(instance):
    original = instance.postponed
    instance.postponed = original
    assert instance.postponed == original

@given(instance=vhdl_statement_VariableAssignmentStatement_strategy)
@settings(max_examples=50)
def test_vhdl_statement_variableassignmentstatement_instantiation(instance):
    assert isinstance(instance, vhdl_statement_VariableAssignmentStatement)

@given(instance=vhdl_statement_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_vhdl_statement_expressionstatement_instantiation(instance):
    assert isinstance(instance, vhdl_statement_ExpressionStatement)

@given(instance=vhdl_statement_BlockStatement_strategy)
@settings(max_examples=50)
def test_vhdl_statement_blockstatement_instantiation(instance):
    assert isinstance(instance, vhdl_statement_BlockStatement)

@given(instance=vhdl_statement_ExitStatement_strategy)
@settings(max_examples=50)
def test_vhdl_statement_exitstatement_instantiation(instance):
    assert isinstance(instance, vhdl_statement_ExitStatement)



@given(instance=vhdl_statement_ExitStatement_strategy)
def test_vhdl_statement_exitstatement_exit_setter(instance):
    original = instance.exit
    instance.exit = original
    assert instance.exit == original

@given(instance=vhdl_statement_NextStatement_strategy)
@settings(max_examples=50)
def test_vhdl_statement_nextstatement_instantiation(instance):
    assert isinstance(instance, vhdl_statement_NextStatement)



@given(instance=vhdl_statement_NextStatement_strategy)
def test_vhdl_statement_nextstatement_next_setter(instance):
    original = instance.next
    instance.next = original
    assert instance.next == original

@given(instance=vhdl_statement_WaitStatement_strategy)
@settings(max_examples=50)
def test_vhdl_statement_waitstatement_instantiation(instance):
    assert isinstance(instance, vhdl_statement_WaitStatement)

@given(instance=vhdl_statement_IfStatement_strategy)
@settings(max_examples=50)
def test_vhdl_statement_ifstatement_instantiation(instance):
    assert isinstance(instance, vhdl_statement_IfStatement)

@given(instance=vhdl_statement_SimultaneousProceduralStatement_strategy)
@settings(max_examples=50)
def test_vhdl_statement_simultaneousproceduralstatement_instantiation(instance):
    assert isinstance(instance, vhdl_statement_SimultaneousProceduralStatement)

@given(instance=vhdl_statement_GenerateStatement_strategy)
@settings(max_examples=50)
def test_vhdl_statement_generatestatement_instantiation(instance):
    assert isinstance(instance, vhdl_statement_GenerateStatement)

@given(instance=vhdl_statement_BreakStatement_strategy)
@settings(max_examples=50)
def test_vhdl_statement_breakstatement_instantiation(instance):
    assert isinstance(instance, vhdl_statement_BreakStatement)

@given(instance=vhdl_statement_AssertionStatement_strategy)
@settings(max_examples=50)
def test_vhdl_statement_assertionstatement_instantiation(instance):
    assert isinstance(instance, vhdl_statement_AssertionStatement)



@given(instance=vhdl_statement_AssertionStatement_strategy)
def test_vhdl_statement_assertionstatement_postponed_setter(instance):
    original = instance.postponed
    instance.postponed = original
    assert instance.postponed == original

@given(instance=vhdl_EntityReference_strategy)
@settings(max_examples=50)
def test_vhdl_entityreference_instantiation(instance):
    assert isinstance(instance, vhdl_EntityReference)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=vhdl_declaration_AttributeSpecification_strategy)
@settings(max_examples=50)
def test_vhdl_declaration_attributespecification_instantiation(instance):
    assert isinstance(instance, vhdl_declaration_AttributeSpecification)



@given(instance=vhdl_declaration_AttributeSpecification_strategy)
def test_vhdl_declaration_attributespecification_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=vhdl_declaration_GroupDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl_declaration_groupdeclaration_instantiation(instance):
    assert isinstance(instance, vhdl_declaration_GroupDeclaration)

@given(instance=vhdl_declaration_SubprogramDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl_declaration_subprogramdeclaration_instantiation(instance):
    assert isinstance(instance, vhdl_declaration_SubprogramDeclaration)

@given(instance=vhdl_declaration_TypeDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl_declaration_typedeclaration_instantiation(instance):
    assert isinstance(instance, vhdl_declaration_TypeDeclaration)

@given(instance=vhdl_expression_SubtypeIndicationExpression_strategy)
@settings(max_examples=50)
def test_vhdl_expression_subtypeindicationexpression_instantiation(instance):
    assert isinstance(instance, vhdl_expression_SubtypeIndicationExpression)

@given(instance=vhdl_declaration_AliasDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl_declaration_aliasdeclaration_instantiation(instance):
    assert isinstance(instance, vhdl_declaration_AliasDeclaration)

@given(instance=vhdl_configuration_BlockConfiguration_strategy)
@settings(max_examples=50)
def test_vhdl_configuration_blockconfiguration_instantiation(instance):
    assert isinstance(instance, vhdl_configuration_BlockConfiguration)

@given(instance=vhdl_declaration_NatureDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl_declaration_naturedeclaration_instantiation(instance):
    assert isinstance(instance, vhdl_declaration_NatureDeclaration)

@given(instance=vhdl_declaration_SubtypeDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl_declaration_subtypedeclaration_instantiation(instance):
    assert isinstance(instance, vhdl_declaration_SubtypeDeclaration)

@given(instance=vhdl_declaration_SubnatureDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl_declaration_subnaturedeclaration_instantiation(instance):
    assert isinstance(instance, vhdl_declaration_SubnatureDeclaration)

@given(instance=vhdl_declaration_AttributeDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl_declaration_attributedeclaration_instantiation(instance):
    assert isinstance(instance, vhdl_declaration_AttributeDeclaration)

@given(instance=vhdl_Component_strategy)
@settings(max_examples=50)
def test_vhdl_component_instantiation(instance):
    assert isinstance(instance, vhdl_Component)

@given(instance=vhdl_declaration_GroupTemplateDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl_declaration_grouptemplatedeclaration_instantiation(instance):
    assert isinstance(instance, vhdl_declaration_GroupTemplateDeclaration)



@given(instance=vhdl_declaration_GroupTemplateDeclaration_strategy)
def test_vhdl_declaration_grouptemplatedeclaration_entry_setter(instance):
    original = instance.entry
    instance.entry = original
    assert instance.entry == original

@given(instance=Module_strategy)
@settings(max_examples=50)
def test_module_instantiation(instance):
    assert isinstance(instance, Module)

@given(instance=vhdl_Entity_strategy)
@settings(max_examples=50)
def test_vhdl_entity_instantiation(instance):
    assert isinstance(instance, vhdl_Entity)

@given(instance=vhdl_configuration_Configuration_strategy)
@settings(max_examples=50)
def test_vhdl_configuration_configuration_instantiation(instance):
    assert isinstance(instance, vhdl_configuration_Configuration)

@given(instance=vhdl_Package_strategy)
@settings(max_examples=50)
def test_vhdl_package_instantiation(instance):
    assert isinstance(instance, vhdl_Package)

@given(instance=vhdl_PackageBody_strategy)
@settings(max_examples=50)
def test_vhdl_packagebody_instantiation(instance):
    assert isinstance(instance, vhdl_PackageBody)

@given(instance=vhdl_Architecture_strategy)
@settings(max_examples=50)
def test_vhdl_architecture_instantiation(instance):
    assert isinstance(instance, vhdl_Architecture)
