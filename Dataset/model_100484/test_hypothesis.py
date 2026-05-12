import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    expressions_Selection,
    timedAutomata_core_System,
    timedAutomata_core_TemplateInstantiation,
    base_Commentable,
    System,
    timedAutomata_core_ComplexSystem,
    timedAutomata_core_SimpleSystem,
    TemplateInstantiation,
    timedAutomata_core_SystemDefinition,
    core_timedAutomata_Label,
    Selections,
    Guards,
    core_timedAutomata_Nail,
    Updates,
    Location,
    base_Identifyable,
    base_Nameable,
    timedAutomata_core_TAElement,
    core_TAElement,
    timedAutomata_core_Template,
    SystemDefinition,
    Template,
    Edge,
    core_timedAutomata_Parameter,
    declarations_FieldDeclaration,
    TAElement,
    timedAutomata_core_Project,
    Type,
    timedAutomata_types_Struct,
    timedAutomata_types_IntegerRange,
    timedAutomata_types_SimpleType,
    timedAutomata_types_IdentifierType,
    timedAutomata_types_Scalar,
    ChannelExpression,
    timedAutomata_declarations_IdentifierChannelExpression,
    timedAutomata_declarations_ChannelExpression,
    declarations_ChannelExpression,
    timedAutomata_types_Type,
    timedAutomata_declarations_ExpressionChannelExpression,
    ChannelPriority,
    timedAutomata_declarations_ComplexChannelPriority,
    timedAutomata_declarations_SimpleChannelPriority,
    timedAutomata_declarations_DefaultChannelPriority,
    timedAutomata_declarations_ChannelPriority,
    Statement,
    timedAutomata_declarations_ForLoopStatement,
    timedAutomata_declarations_IfStatement,
    timedAutomata_declarations_IterationStatement,
    timedAutomata_declarations_DoWhileLoopStatement,
    timedAutomata_declarations_ReturnStatement,
    timedAutomata_declarations_ExpressionStatement,
    timedAutomata_declarations_WhileLoopStatement,
    TAParameter,
    timedAutomata_declarations_CallByReferenceParameter,
    timedAutomata_declarations_CallByValueParameter,
    timedAutomata_declarations_TAParameter,
    Initialiser,
    timedAutomata_declarations_ArrayInitialiser,
    timedAutomata_declarations_Statement,
    declarations_Statement,
    declarations_Declaration,
    timedAutomata_declarations_Block,
    timedAutomata_declarations_ArrayDeclarationType,
    timedAutomata_declarations_ArrayDeclaration,
    timedAutomata_declarations_FieldDeclaration,
    declarations_ChannelPriority,
    timedAutomata_declarations_ExpressionInitialiser,
    timedAutomata_declarations_Initialiser,
    ArrayDeclarationType,
    timedAutomata_declarations_ArrayTypeType,
    timedAutomata_declarations_ArrayExpressionType,
    declarations_ArrayDeclaration,
    declarations_Initialiser,
    declarations_ArrayDeclarationType,
    timedAutomata_declarations_VariableIdentifier,
    declarations_VariableIdentifier,
    declarations_Block,
    timedAutomata_declarations_BlockStatement,
    declarations_TAParameter,
    types_Type,
    Declaration,
    timedAutomata_declarations_TypeDeclaration,
    timedAutomata_declarations_FunctionDeclaration,
    timedAutomata_declarations_ChannelPriorityDeclaration,
    timedAutomata_declarations_VariableDeclaration,
    timedAutomata_expressions_Selection,
    Identifier,
    Expression,
    timedAutomata_expressions_UnaryExpression,
    timedAutomata_expressions_VariableExpression,
    timedAutomata_expressions_PointExpression,
    timedAutomata_expressions_ForallExpression,
    timedAutomata_expressions_BinaryExpression,
    timedAutomata_expressions_FixedExpression,
    timedAutomata_expressions_GroupingExpression,
    timedAutomata_expressions_ExistsExpression,
    timedAutomata_expressions_IdentifierExpression,
    timedAutomata_expressions_AssignmentExpression,
    timedAutomata_expressions_SimpleIfExpression,
    timedAutomata_expressions_WithArgumentsExpression,
    timedAutomata_expressions_ConstantExpression,
    Commentable,
    timedAutomata_declarations_Declaration,
    timedAutomata_expressions_Expression,
    timedAutomata_expressions_IncDecExpression,
    timedAutomata_expressions_ArrayVariableExpression,
    Synchronisation,
    timedAutomata_bnf_ReceiveSynchronisation,
    timedAutomata_bnf_SendSynchronisation,
    timedAutomata_bnf_Identifier,
    timedAutomata_base_Nameable,
    timedAutomata_base_Identifyable,
    timedAutomata_base_Commentable,
    expressions_Expression,
    Position,
    timedAutomata_core_Selections,
    timedAutomata_core_Edge,
    timedAutomata_core_Guards,
    timedAutomata_core_Location,
    timedAutomata_core_Updates,
    timedAutomata_bnf_Synchronisation,
    TypePrefix,
    BinaryOperator,
    AssignOperator,
    UnaryOperator,
    FixedExpressionType,
    PriorityOperator,
    TypeId,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expressions_selection_is_not_abstract():
    assert not inspect.isabstract(expressions_Selection)


def test_expressions_selection_constructor_exists():
    assert callable(expressions_Selection.__init__)


def test_expressions_selection_constructor_args():
    sig = inspect.signature(expressions_Selection.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_core_system_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_core_System)


def test_timedautomata_core_system_constructor_exists():
    assert callable(timedAutomata_core_System.__init__)


def test_timedautomata_core_system_constructor_args():
    sig = inspect.signature(timedAutomata_core_System.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_core_templateinstantiation_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_core_TemplateInstantiation)


def test_timedautomata_core_templateinstantiation_constructor_exists():
    assert callable(timedAutomata_core_TemplateInstantiation.__init__)


def test_timedautomata_core_templateinstantiation_constructor_args():
    sig = inspect.signature(timedAutomata_core_TemplateInstantiation.__init__)
    params = list(sig.parameters.keys())



def test_base_commentable_is_not_abstract():
    assert not inspect.isabstract(base_Commentable)


def test_base_commentable_constructor_exists():
    assert callable(base_Commentable.__init__)


def test_base_commentable_constructor_args():
    sig = inspect.signature(base_Commentable.__init__)
    params = list(sig.parameters.keys())



def test_system_is_not_abstract():
    assert not inspect.isabstract(System)


def test_system_constructor_exists():
    assert callable(System.__init__)


def test_system_constructor_args():
    sig = inspect.signature(System.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_core_complexsystem_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_core_ComplexSystem)


def test_timedautomata_core_complexsystem_constructor_exists():
    assert callable(timedAutomata_core_ComplexSystem.__init__)


def test_timedautomata_core_complexsystem_constructor_args():
    sig = inspect.signature(timedAutomata_core_ComplexSystem.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_timedautomata_core_complexsystem_has_operator():
    assert hasattr(timedAutomata_core_ComplexSystem, "operator")
    descriptor = None
    for klass in timedAutomata_core_ComplexSystem.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_timedautomata_core_simplesystem_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_core_SimpleSystem)


def test_timedautomata_core_simplesystem_constructor_exists():
    assert callable(timedAutomata_core_SimpleSystem.__init__)


def test_timedautomata_core_simplesystem_constructor_args():
    sig = inspect.signature(timedAutomata_core_SimpleSystem.__init__)
    params = list(sig.parameters.keys())



def test_templateinstantiation_is_not_abstract():
    assert not inspect.isabstract(TemplateInstantiation)


def test_templateinstantiation_constructor_exists():
    assert callable(TemplateInstantiation.__init__)


def test_templateinstantiation_constructor_args():
    sig = inspect.signature(TemplateInstantiation.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_core_systemdefinition_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_core_SystemDefinition)


def test_timedautomata_core_systemdefinition_constructor_exists():
    assert callable(timedAutomata_core_SystemDefinition.__init__)


def test_timedautomata_core_systemdefinition_constructor_args():
    sig = inspect.signature(timedAutomata_core_SystemDefinition.__init__)
    params = list(sig.parameters.keys())



def test_core_timedautomata_label_is_not_abstract():
    assert not inspect.isabstract(core_timedAutomata_Label)


def test_core_timedautomata_label_constructor_exists():
    assert callable(core_timedAutomata_Label.__init__)


def test_core_timedautomata_label_constructor_args():
    sig = inspect.signature(core_timedAutomata_Label.__init__)
    params = list(sig.parameters.keys())



def test_selections_is_not_abstract():
    assert not inspect.isabstract(Selections)


def test_selections_constructor_exists():
    assert callable(Selections.__init__)


def test_selections_constructor_args():
    sig = inspect.signature(Selections.__init__)
    params = list(sig.parameters.keys())



def test_guards_is_not_abstract():
    assert not inspect.isabstract(Guards)


def test_guards_constructor_exists():
    assert callable(Guards.__init__)


def test_guards_constructor_args():
    sig = inspect.signature(Guards.__init__)
    params = list(sig.parameters.keys())



def test_core_timedautomata_nail_is_not_abstract():
    assert not inspect.isabstract(core_timedAutomata_Nail)


def test_core_timedautomata_nail_constructor_exists():
    assert callable(core_timedAutomata_Nail.__init__)


def test_core_timedautomata_nail_constructor_args():
    sig = inspect.signature(core_timedAutomata_Nail.__init__)
    params = list(sig.parameters.keys())



def test_updates_is_not_abstract():
    assert not inspect.isabstract(Updates)


def test_updates_constructor_exists():
    assert callable(Updates.__init__)


def test_updates_constructor_args():
    sig = inspect.signature(Updates.__init__)
    params = list(sig.parameters.keys())



def test_location_is_not_abstract():
    assert not inspect.isabstract(Location)


def test_location_constructor_exists():
    assert callable(Location.__init__)


def test_location_constructor_args():
    sig = inspect.signature(Location.__init__)
    params = list(sig.parameters.keys())



def test_base_identifyable_is_not_abstract():
    assert not inspect.isabstract(base_Identifyable)


def test_base_identifyable_constructor_exists():
    assert callable(base_Identifyable.__init__)


def test_base_identifyable_constructor_args():
    sig = inspect.signature(base_Identifyable.__init__)
    params = list(sig.parameters.keys())



def test_base_nameable_is_not_abstract():
    assert not inspect.isabstract(base_Nameable)


def test_base_nameable_constructor_exists():
    assert callable(base_Nameable.__init__)


def test_base_nameable_constructor_args():
    sig = inspect.signature(base_Nameable.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_core_taelement_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_core_TAElement)


def test_timedautomata_core_taelement_constructor_exists():
    assert callable(timedAutomata_core_TAElement.__init__)


def test_timedautomata_core_taelement_constructor_args():
    sig = inspect.signature(timedAutomata_core_TAElement.__init__)
    params = list(sig.parameters.keys())



def test_core_taelement_is_not_abstract():
    assert not inspect.isabstract(core_TAElement)


def test_core_taelement_constructor_exists():
    assert callable(core_TAElement.__init__)


def test_core_taelement_constructor_args():
    sig = inspect.signature(core_TAElement.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_core_template_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_core_Template)


def test_timedautomata_core_template_constructor_exists():
    assert callable(timedAutomata_core_Template.__init__)


def test_timedautomata_core_template_constructor_args():
    sig = inspect.signature(timedAutomata_core_Template.__init__)
    params = list(sig.parameters.keys())



def test_systemdefinition_is_not_abstract():
    assert not inspect.isabstract(SystemDefinition)


def test_systemdefinition_constructor_exists():
    assert callable(SystemDefinition.__init__)


def test_systemdefinition_constructor_args():
    sig = inspect.signature(SystemDefinition.__init__)
    params = list(sig.parameters.keys())



def test_template_is_not_abstract():
    assert not inspect.isabstract(Template)


def test_template_constructor_exists():
    assert callable(Template.__init__)


def test_template_constructor_args():
    sig = inspect.signature(Template.__init__)
    params = list(sig.parameters.keys())



def test_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_core_timedautomata_parameter_is_not_abstract():
    assert not inspect.isabstract(core_timedAutomata_Parameter)


def test_core_timedautomata_parameter_constructor_exists():
    assert callable(core_timedAutomata_Parameter.__init__)


def test_core_timedautomata_parameter_constructor_args():
    sig = inspect.signature(core_timedAutomata_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_declarations_fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(declarations_FieldDeclaration)


def test_declarations_fielddeclaration_constructor_exists():
    assert callable(declarations_FieldDeclaration.__init__)


def test_declarations_fielddeclaration_constructor_args():
    sig = inspect.signature(declarations_FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_taelement_is_not_abstract():
    assert not inspect.isabstract(TAElement)


def test_taelement_constructor_exists():
    assert callable(TAElement.__init__)


def test_taelement_constructor_args():
    sig = inspect.signature(TAElement.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_core_project_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_core_Project)


def test_timedautomata_core_project_constructor_exists():
    assert callable(timedAutomata_core_Project.__init__)


def test_timedautomata_core_project_constructor_args():
    sig = inspect.signature(timedAutomata_core_Project.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_timedautomata_core_project_has_id():
    assert hasattr(timedAutomata_core_Project, "id")
    descriptor = None
    for klass in timedAutomata_core_Project.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_types_struct_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_types_Struct)


def test_timedautomata_types_struct_constructor_exists():
    assert callable(timedAutomata_types_Struct.__init__)


def test_timedautomata_types_struct_constructor_args():
    sig = inspect.signature(timedAutomata_types_Struct.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_types_integerrange_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_types_IntegerRange)


def test_timedautomata_types_integerrange_constructor_exists():
    assert callable(timedAutomata_types_IntegerRange.__init__)


def test_timedautomata_types_integerrange_constructor_args():
    sig = inspect.signature(timedAutomata_types_IntegerRange.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_types_simpletype_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_types_SimpleType)


def test_timedautomata_types_simpletype_constructor_exists():
    assert callable(timedAutomata_types_SimpleType.__init__)


def test_timedautomata_types_simpletype_constructor_args():
    sig = inspect.signature(timedAutomata_types_SimpleType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_timedautomata_types_simpletype_has_type():
    assert hasattr(timedAutomata_types_SimpleType, "type")
    descriptor = None
    for klass in timedAutomata_types_SimpleType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_timedautomata_types_identifiertype_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_types_IdentifierType)


def test_timedautomata_types_identifiertype_constructor_exists():
    assert callable(timedAutomata_types_IdentifierType.__init__)


def test_timedautomata_types_identifiertype_constructor_args():
    sig = inspect.signature(timedAutomata_types_IdentifierType.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_types_scalar_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_types_Scalar)


def test_timedautomata_types_scalar_constructor_exists():
    assert callable(timedAutomata_types_Scalar.__init__)


def test_timedautomata_types_scalar_constructor_args():
    sig = inspect.signature(timedAutomata_types_Scalar.__init__)
    params = list(sig.parameters.keys())



def test_channelexpression_is_not_abstract():
    assert not inspect.isabstract(ChannelExpression)


def test_channelexpression_constructor_exists():
    assert callable(ChannelExpression.__init__)


def test_channelexpression_constructor_args():
    sig = inspect.signature(ChannelExpression.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_declarations_identifierchannelexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_IdentifierChannelExpression)


def test_timedautomata_declarations_identifierchannelexpression_constructor_exists():
    assert callable(timedAutomata_declarations_IdentifierChannelExpression.__init__)


def test_timedautomata_declarations_identifierchannelexpression_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_IdentifierChannelExpression.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_declarations_channelexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_ChannelExpression)


def test_timedautomata_declarations_channelexpression_constructor_exists():
    assert callable(timedAutomata_declarations_ChannelExpression.__init__)


def test_timedautomata_declarations_channelexpression_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_ChannelExpression.__init__)
    params = list(sig.parameters.keys())



def test_declarations_channelexpression_is_not_abstract():
    assert not inspect.isabstract(declarations_ChannelExpression)


def test_declarations_channelexpression_constructor_exists():
    assert callable(declarations_ChannelExpression.__init__)


def test_declarations_channelexpression_constructor_args():
    sig = inspect.signature(declarations_ChannelExpression.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_types_type_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_types_Type)


def test_timedautomata_types_type_constructor_exists():
    assert callable(timedAutomata_types_Type.__init__)


def test_timedautomata_types_type_constructor_args():
    sig = inspect.signature(timedAutomata_types_Type.__init__)
    params = list(sig.parameters.keys())
    assert "prefix" in params, "Missing parameter 'prefix'"

def test_timedautomata_types_type_has_prefix():
    assert hasattr(timedAutomata_types_Type, "prefix")
    descriptor = None
    for klass in timedAutomata_types_Type.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)



def test_timedautomata_declarations_expressionchannelexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_ExpressionChannelExpression)


def test_timedautomata_declarations_expressionchannelexpression_constructor_exists():
    assert callable(timedAutomata_declarations_ExpressionChannelExpression.__init__)


def test_timedautomata_declarations_expressionchannelexpression_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_ExpressionChannelExpression.__init__)
    params = list(sig.parameters.keys())



def test_channelpriority_is_not_abstract():
    assert not inspect.isabstract(ChannelPriority)


def test_channelpriority_constructor_exists():
    assert callable(ChannelPriority.__init__)


def test_channelpriority_constructor_args():
    sig = inspect.signature(ChannelPriority.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_declarations_complexchannelpriority_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_ComplexChannelPriority)


def test_timedautomata_declarations_complexchannelpriority_constructor_exists():
    assert callable(timedAutomata_declarations_ComplexChannelPriority.__init__)


def test_timedautomata_declarations_complexchannelpriority_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_ComplexChannelPriority.__init__)
    params = list(sig.parameters.keys())
    assert "channelOperator" in params, "Missing parameter 'channelOperator'"

def test_timedautomata_declarations_complexchannelpriority_has_channelOperator():
    assert hasattr(timedAutomata_declarations_ComplexChannelPriority, "channelOperator")
    descriptor = None
    for klass in timedAutomata_declarations_ComplexChannelPriority.__mro__:
        if "channelOperator" in klass.__dict__:
            descriptor = klass.__dict__["channelOperator"]
            break
    assert isinstance(descriptor, property)



def test_timedautomata_declarations_simplechannelpriority_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_SimpleChannelPriority)


def test_timedautomata_declarations_simplechannelpriority_constructor_exists():
    assert callable(timedAutomata_declarations_SimpleChannelPriority.__init__)


def test_timedautomata_declarations_simplechannelpriority_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_SimpleChannelPriority.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_declarations_defaultchannelpriority_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_DefaultChannelPriority)


def test_timedautomata_declarations_defaultchannelpriority_constructor_exists():
    assert callable(timedAutomata_declarations_DefaultChannelPriority.__init__)


def test_timedautomata_declarations_defaultchannelpriority_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_DefaultChannelPriority.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_declarations_channelpriority_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_ChannelPriority)


def test_timedautomata_declarations_channelpriority_constructor_exists():
    assert callable(timedAutomata_declarations_ChannelPriority.__init__)


def test_timedautomata_declarations_channelpriority_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_ChannelPriority.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_declarations_forloopstatement_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_ForLoopStatement)


def test_timedautomata_declarations_forloopstatement_constructor_exists():
    assert callable(timedAutomata_declarations_ForLoopStatement.__init__)


def test_timedautomata_declarations_forloopstatement_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_ForLoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_declarations_ifstatement_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_IfStatement)


def test_timedautomata_declarations_ifstatement_constructor_exists():
    assert callable(timedAutomata_declarations_IfStatement.__init__)


def test_timedautomata_declarations_ifstatement_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_declarations_iterationstatement_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_IterationStatement)


def test_timedautomata_declarations_iterationstatement_constructor_exists():
    assert callable(timedAutomata_declarations_IterationStatement.__init__)


def test_timedautomata_declarations_iterationstatement_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_IterationStatement.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_declarations_dowhileloopstatement_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_DoWhileLoopStatement)


def test_timedautomata_declarations_dowhileloopstatement_constructor_exists():
    assert callable(timedAutomata_declarations_DoWhileLoopStatement.__init__)


def test_timedautomata_declarations_dowhileloopstatement_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_DoWhileLoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_declarations_returnstatement_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_ReturnStatement)


def test_timedautomata_declarations_returnstatement_constructor_exists():
    assert callable(timedAutomata_declarations_ReturnStatement.__init__)


def test_timedautomata_declarations_returnstatement_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_declarations_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_ExpressionStatement)


def test_timedautomata_declarations_expressionstatement_constructor_exists():
    assert callable(timedAutomata_declarations_ExpressionStatement.__init__)


def test_timedautomata_declarations_expressionstatement_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_declarations_whileloopstatement_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_WhileLoopStatement)


def test_timedautomata_declarations_whileloopstatement_constructor_exists():
    assert callable(timedAutomata_declarations_WhileLoopStatement.__init__)


def test_timedautomata_declarations_whileloopstatement_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_WhileLoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_taparameter_is_not_abstract():
    assert not inspect.isabstract(TAParameter)


def test_taparameter_constructor_exists():
    assert callable(TAParameter.__init__)


def test_taparameter_constructor_args():
    sig = inspect.signature(TAParameter.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_declarations_callbyreferenceparameter_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_CallByReferenceParameter)


def test_timedautomata_declarations_callbyreferenceparameter_constructor_exists():
    assert callable(timedAutomata_declarations_CallByReferenceParameter.__init__)


def test_timedautomata_declarations_callbyreferenceparameter_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_CallByReferenceParameter.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_declarations_callbyvalueparameter_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_CallByValueParameter)


def test_timedautomata_declarations_callbyvalueparameter_constructor_exists():
    assert callable(timedAutomata_declarations_CallByValueParameter.__init__)


def test_timedautomata_declarations_callbyvalueparameter_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_CallByValueParameter.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_declarations_taparameter_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_TAParameter)


def test_timedautomata_declarations_taparameter_constructor_exists():
    assert callable(timedAutomata_declarations_TAParameter.__init__)


def test_timedautomata_declarations_taparameter_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_TAParameter.__init__)
    params = list(sig.parameters.keys())



def test_initialiser_is_not_abstract():
    assert not inspect.isabstract(Initialiser)


def test_initialiser_constructor_exists():
    assert callable(Initialiser.__init__)


def test_initialiser_constructor_args():
    sig = inspect.signature(Initialiser.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_declarations_arrayinitialiser_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_ArrayInitialiser)


def test_timedautomata_declarations_arrayinitialiser_constructor_exists():
    assert callable(timedAutomata_declarations_ArrayInitialiser.__init__)


def test_timedautomata_declarations_arrayinitialiser_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_ArrayInitialiser.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_declarations_statement_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_Statement)


def test_timedautomata_declarations_statement_constructor_exists():
    assert callable(timedAutomata_declarations_Statement.__init__)


def test_timedautomata_declarations_statement_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_Statement.__init__)
    params = list(sig.parameters.keys())



def test_declarations_statement_is_not_abstract():
    assert not inspect.isabstract(declarations_Statement)


def test_declarations_statement_constructor_exists():
    assert callable(declarations_Statement.__init__)


def test_declarations_statement_constructor_args():
    sig = inspect.signature(declarations_Statement.__init__)
    params = list(sig.parameters.keys())



def test_declarations_declaration_is_not_abstract():
    assert not inspect.isabstract(declarations_Declaration)


def test_declarations_declaration_constructor_exists():
    assert callable(declarations_Declaration.__init__)


def test_declarations_declaration_constructor_args():
    sig = inspect.signature(declarations_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_declarations_block_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_Block)


def test_timedautomata_declarations_block_constructor_exists():
    assert callable(timedAutomata_declarations_Block.__init__)


def test_timedautomata_declarations_block_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_Block.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_declarations_arraydeclarationtype_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_ArrayDeclarationType)


def test_timedautomata_declarations_arraydeclarationtype_constructor_exists():
    assert callable(timedAutomata_declarations_ArrayDeclarationType.__init__)


def test_timedautomata_declarations_arraydeclarationtype_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_ArrayDeclarationType.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_declarations_arraydeclaration_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_ArrayDeclaration)


def test_timedautomata_declarations_arraydeclaration_constructor_exists():
    assert callable(timedAutomata_declarations_ArrayDeclaration.__init__)


def test_timedautomata_declarations_arraydeclaration_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_ArrayDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_declarations_fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_FieldDeclaration)


def test_timedautomata_declarations_fielddeclaration_constructor_exists():
    assert callable(timedAutomata_declarations_FieldDeclaration.__init__)


def test_timedautomata_declarations_fielddeclaration_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_declarations_channelpriority_is_not_abstract():
    assert not inspect.isabstract(declarations_ChannelPriority)


def test_declarations_channelpriority_constructor_exists():
    assert callable(declarations_ChannelPriority.__init__)


def test_declarations_channelpriority_constructor_args():
    sig = inspect.signature(declarations_ChannelPriority.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_declarations_expressioninitialiser_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_ExpressionInitialiser)


def test_timedautomata_declarations_expressioninitialiser_constructor_exists():
    assert callable(timedAutomata_declarations_ExpressionInitialiser.__init__)


def test_timedautomata_declarations_expressioninitialiser_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_ExpressionInitialiser.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_declarations_initialiser_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_Initialiser)


def test_timedautomata_declarations_initialiser_constructor_exists():
    assert callable(timedAutomata_declarations_Initialiser.__init__)


def test_timedautomata_declarations_initialiser_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_Initialiser.__init__)
    params = list(sig.parameters.keys())



def test_arraydeclarationtype_is_not_abstract():
    assert not inspect.isabstract(ArrayDeclarationType)


def test_arraydeclarationtype_constructor_exists():
    assert callable(ArrayDeclarationType.__init__)


def test_arraydeclarationtype_constructor_args():
    sig = inspect.signature(ArrayDeclarationType.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_declarations_arraytypetype_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_ArrayTypeType)


def test_timedautomata_declarations_arraytypetype_constructor_exists():
    assert callable(timedAutomata_declarations_ArrayTypeType.__init__)


def test_timedautomata_declarations_arraytypetype_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_ArrayTypeType.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_declarations_arrayexpressiontype_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_ArrayExpressionType)


def test_timedautomata_declarations_arrayexpressiontype_constructor_exists():
    assert callable(timedAutomata_declarations_ArrayExpressionType.__init__)


def test_timedautomata_declarations_arrayexpressiontype_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_ArrayExpressionType.__init__)
    params = list(sig.parameters.keys())



def test_declarations_arraydeclaration_is_not_abstract():
    assert not inspect.isabstract(declarations_ArrayDeclaration)


def test_declarations_arraydeclaration_constructor_exists():
    assert callable(declarations_ArrayDeclaration.__init__)


def test_declarations_arraydeclaration_constructor_args():
    sig = inspect.signature(declarations_ArrayDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_declarations_initialiser_is_not_abstract():
    assert not inspect.isabstract(declarations_Initialiser)


def test_declarations_initialiser_constructor_exists():
    assert callable(declarations_Initialiser.__init__)


def test_declarations_initialiser_constructor_args():
    sig = inspect.signature(declarations_Initialiser.__init__)
    params = list(sig.parameters.keys())



def test_declarations_arraydeclarationtype_is_not_abstract():
    assert not inspect.isabstract(declarations_ArrayDeclarationType)


def test_declarations_arraydeclarationtype_constructor_exists():
    assert callable(declarations_ArrayDeclarationType.__init__)


def test_declarations_arraydeclarationtype_constructor_args():
    sig = inspect.signature(declarations_ArrayDeclarationType.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_declarations_variableidentifier_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_VariableIdentifier)


def test_timedautomata_declarations_variableidentifier_constructor_exists():
    assert callable(timedAutomata_declarations_VariableIdentifier.__init__)


def test_timedautomata_declarations_variableidentifier_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_VariableIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_declarations_variableidentifier_is_not_abstract():
    assert not inspect.isabstract(declarations_VariableIdentifier)


def test_declarations_variableidentifier_constructor_exists():
    assert callable(declarations_VariableIdentifier.__init__)


def test_declarations_variableidentifier_constructor_args():
    sig = inspect.signature(declarations_VariableIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_declarations_block_is_not_abstract():
    assert not inspect.isabstract(declarations_Block)


def test_declarations_block_constructor_exists():
    assert callable(declarations_Block.__init__)


def test_declarations_block_constructor_args():
    sig = inspect.signature(declarations_Block.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_declarations_blockstatement_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_BlockStatement)


def test_timedautomata_declarations_blockstatement_constructor_exists():
    assert callable(timedAutomata_declarations_BlockStatement.__init__)


def test_timedautomata_declarations_blockstatement_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_declarations_taparameter_is_not_abstract():
    assert not inspect.isabstract(declarations_TAParameter)


def test_declarations_taparameter_constructor_exists():
    assert callable(declarations_TAParameter.__init__)


def test_declarations_taparameter_constructor_args():
    sig = inspect.signature(declarations_TAParameter.__init__)
    params = list(sig.parameters.keys())



def test_types_type_is_not_abstract():
    assert not inspect.isabstract(types_Type)


def test_types_type_constructor_exists():
    assert callable(types_Type.__init__)


def test_types_type_constructor_args():
    sig = inspect.signature(types_Type.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_declarations_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_TypeDeclaration)


def test_timedautomata_declarations_typedeclaration_constructor_exists():
    assert callable(timedAutomata_declarations_TypeDeclaration.__init__)


def test_timedautomata_declarations_typedeclaration_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_declarations_functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_FunctionDeclaration)


def test_timedautomata_declarations_functiondeclaration_constructor_exists():
    assert callable(timedAutomata_declarations_FunctionDeclaration.__init__)


def test_timedautomata_declarations_functiondeclaration_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_declarations_channelprioritydeclaration_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_ChannelPriorityDeclaration)


def test_timedautomata_declarations_channelprioritydeclaration_constructor_exists():
    assert callable(timedAutomata_declarations_ChannelPriorityDeclaration.__init__)


def test_timedautomata_declarations_channelprioritydeclaration_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_ChannelPriorityDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_declarations_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_VariableDeclaration)


def test_timedautomata_declarations_variabledeclaration_constructor_exists():
    assert callable(timedAutomata_declarations_VariableDeclaration.__init__)


def test_timedautomata_declarations_variabledeclaration_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_expressions_selection_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_expressions_Selection)


def test_timedautomata_expressions_selection_constructor_exists():
    assert callable(timedAutomata_expressions_Selection.__init__)


def test_timedautomata_expressions_selection_constructor_args():
    sig = inspect.signature(timedAutomata_expressions_Selection.__init__)
    params = list(sig.parameters.keys())



def test_identifier_is_not_abstract():
    assert not inspect.isabstract(Identifier)


def test_identifier_constructor_exists():
    assert callable(Identifier.__init__)


def test_identifier_constructor_args():
    sig = inspect.signature(Identifier.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_expressions_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_expressions_UnaryExpression)


def test_timedautomata_expressions_unaryexpression_constructor_exists():
    assert callable(timedAutomata_expressions_UnaryExpression.__init__)


def test_timedautomata_expressions_unaryexpression_constructor_args():
    sig = inspect.signature(timedAutomata_expressions_UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_timedautomata_expressions_unaryexpression_has_operator():
    assert hasattr(timedAutomata_expressions_UnaryExpression, "operator")
    descriptor = None
    for klass in timedAutomata_expressions_UnaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_timedautomata_expressions_variableexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_expressions_VariableExpression)


def test_timedautomata_expressions_variableexpression_constructor_exists():
    assert callable(timedAutomata_expressions_VariableExpression.__init__)


def test_timedautomata_expressions_variableexpression_constructor_args():
    sig = inspect.signature(timedAutomata_expressions_VariableExpression.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_expressions_pointexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_expressions_PointExpression)


def test_timedautomata_expressions_pointexpression_constructor_exists():
    assert callable(timedAutomata_expressions_PointExpression.__init__)


def test_timedautomata_expressions_pointexpression_constructor_args():
    sig = inspect.signature(timedAutomata_expressions_PointExpression.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_expressions_forallexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_expressions_ForallExpression)


def test_timedautomata_expressions_forallexpression_constructor_exists():
    assert callable(timedAutomata_expressions_ForallExpression.__init__)


def test_timedautomata_expressions_forallexpression_constructor_args():
    sig = inspect.signature(timedAutomata_expressions_ForallExpression.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_expressions_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_expressions_BinaryExpression)


def test_timedautomata_expressions_binaryexpression_constructor_exists():
    assert callable(timedAutomata_expressions_BinaryExpression.__init__)


def test_timedautomata_expressions_binaryexpression_constructor_args():
    sig = inspect.signature(timedAutomata_expressions_BinaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_timedautomata_expressions_binaryexpression_has_operator():
    assert hasattr(timedAutomata_expressions_BinaryExpression, "operator")
    descriptor = None
    for klass in timedAutomata_expressions_BinaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_timedautomata_expressions_fixedexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_expressions_FixedExpression)


def test_timedautomata_expressions_fixedexpression_constructor_exists():
    assert callable(timedAutomata_expressions_FixedExpression.__init__)


def test_timedautomata_expressions_fixedexpression_constructor_args():
    sig = inspect.signature(timedAutomata_expressions_FixedExpression.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_timedautomata_expressions_fixedexpression_has_type():
    assert hasattr(timedAutomata_expressions_FixedExpression, "type")
    descriptor = None
    for klass in timedAutomata_expressions_FixedExpression.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_timedautomata_expressions_groupingexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_expressions_GroupingExpression)


def test_timedautomata_expressions_groupingexpression_constructor_exists():
    assert callable(timedAutomata_expressions_GroupingExpression.__init__)


def test_timedautomata_expressions_groupingexpression_constructor_args():
    sig = inspect.signature(timedAutomata_expressions_GroupingExpression.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_expressions_existsexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_expressions_ExistsExpression)


def test_timedautomata_expressions_existsexpression_constructor_exists():
    assert callable(timedAutomata_expressions_ExistsExpression.__init__)


def test_timedautomata_expressions_existsexpression_constructor_args():
    sig = inspect.signature(timedAutomata_expressions_ExistsExpression.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_expressions_identifierexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_expressions_IdentifierExpression)


def test_timedautomata_expressions_identifierexpression_constructor_exists():
    assert callable(timedAutomata_expressions_IdentifierExpression.__init__)


def test_timedautomata_expressions_identifierexpression_constructor_args():
    sig = inspect.signature(timedAutomata_expressions_IdentifierExpression.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_expressions_assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_expressions_AssignmentExpression)


def test_timedautomata_expressions_assignmentexpression_constructor_exists():
    assert callable(timedAutomata_expressions_AssignmentExpression.__init__)


def test_timedautomata_expressions_assignmentexpression_constructor_args():
    sig = inspect.signature(timedAutomata_expressions_AssignmentExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_timedautomata_expressions_assignmentexpression_has_operator():
    assert hasattr(timedAutomata_expressions_AssignmentExpression, "operator")
    descriptor = None
    for klass in timedAutomata_expressions_AssignmentExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_timedautomata_expressions_simpleifexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_expressions_SimpleIfExpression)


def test_timedautomata_expressions_simpleifexpression_constructor_exists():
    assert callable(timedAutomata_expressions_SimpleIfExpression.__init__)


def test_timedautomata_expressions_simpleifexpression_constructor_args():
    sig = inspect.signature(timedAutomata_expressions_SimpleIfExpression.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_expressions_withargumentsexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_expressions_WithArgumentsExpression)


def test_timedautomata_expressions_withargumentsexpression_constructor_exists():
    assert callable(timedAutomata_expressions_WithArgumentsExpression.__init__)


def test_timedautomata_expressions_withargumentsexpression_constructor_args():
    sig = inspect.signature(timedAutomata_expressions_WithArgumentsExpression.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_expressions_constantexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_expressions_ConstantExpression)


def test_timedautomata_expressions_constantexpression_constructor_exists():
    assert callable(timedAutomata_expressions_ConstantExpression.__init__)


def test_timedautomata_expressions_constantexpression_constructor_args():
    sig = inspect.signature(timedAutomata_expressions_ConstantExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_timedautomata_expressions_constantexpression_has_value():
    assert hasattr(timedAutomata_expressions_ConstantExpression, "value")
    descriptor = None
    for klass in timedAutomata_expressions_ConstantExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_commentable_is_not_abstract():
    assert not inspect.isabstract(Commentable)


def test_commentable_constructor_exists():
    assert callable(Commentable.__init__)


def test_commentable_constructor_args():
    sig = inspect.signature(Commentable.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_declarations_declaration_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_declarations_Declaration)


def test_timedautomata_declarations_declaration_constructor_exists():
    assert callable(timedAutomata_declarations_Declaration.__init__)


def test_timedautomata_declarations_declaration_constructor_args():
    sig = inspect.signature(timedAutomata_declarations_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_expressions_expression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_expressions_Expression)


def test_timedautomata_expressions_expression_constructor_exists():
    assert callable(timedAutomata_expressions_Expression.__init__)


def test_timedautomata_expressions_expression_constructor_args():
    sig = inspect.signature(timedAutomata_expressions_Expression.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_expressions_incdecexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_expressions_IncDecExpression)


def test_timedautomata_expressions_incdecexpression_constructor_exists():
    assert callable(timedAutomata_expressions_IncDecExpression.__init__)


def test_timedautomata_expressions_incdecexpression_constructor_args():
    sig = inspect.signature(timedAutomata_expressions_IncDecExpression.__init__)
    params = list(sig.parameters.keys())
    assert "beforeExpression" in params, "Missing parameter 'beforeExpression'"
    assert "increment" in params, "Missing parameter 'increment'"

def test_timedautomata_expressions_incdecexpression_has_beforeExpression():
    assert hasattr(timedAutomata_expressions_IncDecExpression, "beforeExpression")
    descriptor = None
    for klass in timedAutomata_expressions_IncDecExpression.__mro__:
        if "beforeExpression" in klass.__dict__:
            descriptor = klass.__dict__["beforeExpression"]
            break
    assert isinstance(descriptor, property)

def test_timedautomata_expressions_incdecexpression_has_increment():
    assert hasattr(timedAutomata_expressions_IncDecExpression, "increment")
    descriptor = None
    for klass in timedAutomata_expressions_IncDecExpression.__mro__:
        if "increment" in klass.__dict__:
            descriptor = klass.__dict__["increment"]
            break
    assert isinstance(descriptor, property)



def test_timedautomata_expressions_arrayvariableexpression_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_expressions_ArrayVariableExpression)


def test_timedautomata_expressions_arrayvariableexpression_constructor_exists():
    assert callable(timedAutomata_expressions_ArrayVariableExpression.__init__)


def test_timedautomata_expressions_arrayvariableexpression_constructor_args():
    sig = inspect.signature(timedAutomata_expressions_ArrayVariableExpression.__init__)
    params = list(sig.parameters.keys())



def test_synchronisation_is_not_abstract():
    assert not inspect.isabstract(Synchronisation)


def test_synchronisation_constructor_exists():
    assert callable(Synchronisation.__init__)


def test_synchronisation_constructor_args():
    sig = inspect.signature(Synchronisation.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_bnf_receivesynchronisation_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_bnf_ReceiveSynchronisation)


def test_timedautomata_bnf_receivesynchronisation_constructor_exists():
    assert callable(timedAutomata_bnf_ReceiveSynchronisation.__init__)


def test_timedautomata_bnf_receivesynchronisation_constructor_args():
    sig = inspect.signature(timedAutomata_bnf_ReceiveSynchronisation.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_bnf_sendsynchronisation_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_bnf_SendSynchronisation)


def test_timedautomata_bnf_sendsynchronisation_constructor_exists():
    assert callable(timedAutomata_bnf_SendSynchronisation.__init__)


def test_timedautomata_bnf_sendsynchronisation_constructor_args():
    sig = inspect.signature(timedAutomata_bnf_SendSynchronisation.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_bnf_identifier_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_bnf_Identifier)


def test_timedautomata_bnf_identifier_constructor_exists():
    assert callable(timedAutomata_bnf_Identifier.__init__)


def test_timedautomata_bnf_identifier_constructor_args():
    sig = inspect.signature(timedAutomata_bnf_Identifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_timedautomata_bnf_identifier_has_name():
    assert hasattr(timedAutomata_bnf_Identifier, "name")
    descriptor = None
    for klass in timedAutomata_bnf_Identifier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_timedautomata_base_nameable_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_base_Nameable)


def test_timedautomata_base_nameable_constructor_exists():
    assert callable(timedAutomata_base_Nameable.__init__)


def test_timedautomata_base_nameable_constructor_args():
    sig = inspect.signature(timedAutomata_base_Nameable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_timedautomata_base_nameable_has_name():
    assert hasattr(timedAutomata_base_Nameable, "name")
    descriptor = None
    for klass in timedAutomata_base_Nameable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_timedautomata_base_identifyable_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_base_Identifyable)


def test_timedautomata_base_identifyable_constructor_exists():
    assert callable(timedAutomata_base_Identifyable.__init__)


def test_timedautomata_base_identifyable_constructor_args():
    sig = inspect.signature(timedAutomata_base_Identifyable.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_timedautomata_base_identifyable_has_id():
    assert hasattr(timedAutomata_base_Identifyable, "id")
    descriptor = None
    for klass in timedAutomata_base_Identifyable.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_timedautomata_base_commentable_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_base_Commentable)


def test_timedautomata_base_commentable_constructor_exists():
    assert callable(timedAutomata_base_Commentable.__init__)


def test_timedautomata_base_commentable_constructor_args():
    sig = inspect.signature(timedAutomata_base_Commentable.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_timedautomata_base_commentable_has_comment():
    assert hasattr(timedAutomata_base_Commentable, "comment")
    descriptor = None
    for klass in timedAutomata_base_Commentable.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_expressions_expression_is_not_abstract():
    assert not inspect.isabstract(expressions_Expression)


def test_expressions_expression_constructor_exists():
    assert callable(expressions_Expression.__init__)


def test_expressions_expression_constructor_args():
    sig = inspect.signature(expressions_Expression.__init__)
    params = list(sig.parameters.keys())



def test_position_is_not_abstract():
    assert not inspect.isabstract(Position)


def test_position_constructor_exists():
    assert callable(Position.__init__)


def test_position_constructor_args():
    sig = inspect.signature(Position.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_core_selections_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_core_Selections)


def test_timedautomata_core_selections_constructor_exists():
    assert callable(timedAutomata_core_Selections.__init__)


def test_timedautomata_core_selections_constructor_args():
    sig = inspect.signature(timedAutomata_core_Selections.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_core_edge_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_core_Edge)


def test_timedautomata_core_edge_constructor_exists():
    assert callable(timedAutomata_core_Edge.__init__)


def test_timedautomata_core_edge_constructor_args():
    sig = inspect.signature(timedAutomata_core_Edge.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_core_guards_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_core_Guards)


def test_timedautomata_core_guards_constructor_exists():
    assert callable(timedAutomata_core_Guards.__init__)


def test_timedautomata_core_guards_constructor_args():
    sig = inspect.signature(timedAutomata_core_Guards.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_core_location_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_core_Location)


def test_timedautomata_core_location_constructor_exists():
    assert callable(timedAutomata_core_Location.__init__)


def test_timedautomata_core_location_constructor_args():
    sig = inspect.signature(timedAutomata_core_Location.__init__)
    params = list(sig.parameters.keys())
    assert "urgent" in params, "Missing parameter 'urgent'"
    assert "committed" in params, "Missing parameter 'committed'"

def test_timedautomata_core_location_has_urgent():
    assert hasattr(timedAutomata_core_Location, "urgent")
    descriptor = None
    for klass in timedAutomata_core_Location.__mro__:
        if "urgent" in klass.__dict__:
            descriptor = klass.__dict__["urgent"]
            break
    assert isinstance(descriptor, property)

def test_timedautomata_core_location_has_committed():
    assert hasattr(timedAutomata_core_Location, "committed")
    descriptor = None
    for klass in timedAutomata_core_Location.__mro__:
        if "committed" in klass.__dict__:
            descriptor = klass.__dict__["committed"]
            break
    assert isinstance(descriptor, property)



def test_timedautomata_core_updates_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_core_Updates)


def test_timedautomata_core_updates_constructor_exists():
    assert callable(timedAutomata_core_Updates.__init__)


def test_timedautomata_core_updates_constructor_args():
    sig = inspect.signature(timedAutomata_core_Updates.__init__)
    params = list(sig.parameters.keys())



def test_timedautomata_bnf_synchronisation_is_not_abstract():
    assert not inspect.isabstract(timedAutomata_bnf_Synchronisation)


def test_timedautomata_bnf_synchronisation_constructor_exists():
    assert callable(timedAutomata_bnf_Synchronisation.__init__)


def test_timedautomata_bnf_synchronisation_constructor_args():
    sig = inspect.signature(timedAutomata_bnf_Synchronisation.__init__)
    params = list(sig.parameters.keys())

def test_typeprefix_exists():
    # Check that the Enumeration exists
    assert TypePrefix is not None

def test_typeprefix_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypePrefix]
    expected_literals = [
        "CONSTANT",
        "BROADCAST",
        "NONE",
        "META",
        "URGENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypePrefix"

def test_binaryoperator_exists():
    # Check that the Enumeration exists
    assert BinaryOperator is not None

def test_binaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BinaryOperator]
    expected_literals = [
        "MODULO",
        "BITWISE_OR",
        "GREATER_THAN_OR_EQUAL",
        "BITWISE_AND_ASSIGN",
        "ADDITION",
        "EQUALS",
        "SUBSTRACTION",
        "IMPLY",
        "RIGHT_BITSHIFT_ASSIGN",
        "MINIMUM",
        "BITWISE_OR_ASSIGN",
        "LESS_THAN",
        "LOGICAL_OR",
        "LEFT_BITSHIFT",
        "DECREMENT",
        "MAXIMUM",
        "INCREMENT",
        "LOGICAL_NEGATION",
        "BITWISE_XOR",
        "MULTIPLICATION",
        "NONE",
        "DIVISION",
        "LESS_THAN_OR_EQUAL",
        "LEFT_BITSHIFT_ASSIGN",
        "BITWISE_XOR_ASIGN",
        "GREATER_THAN",
        "LOGICAL_AND",
        "RIGHT_BITSHIFT",
        "BITWISE_AND",
        "NOT_EQUALS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BinaryOperator"

def test_assignoperator_exists():
    # Check that the Enumeration exists
    assert AssignOperator is not None

def test_assignoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignOperator]
    expected_literals = [
        "MOD_ASSIGN",
        "ASSIGN",
        "ADD_ASIGN",
        "DIV_ASSIGN",
        "SUB_ASSIGN",
        "MULT_ASSIGN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignOperator"

def test_unaryoperator_exists():
    # Check that the Enumeration exists
    assert UnaryOperator is not None

def test_unaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryOperator]
    expected_literals = [
        "MINUS",
        "NOT",
        "PLUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryOperator"

def test_fixedexpressiontype_exists():
    # Check that the Enumeration exists
    assert FixedExpressionType is not None

def test_fixedexpressiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FixedExpressionType]
    expected_literals = [
        "Deadlock",
        "True_",
        "False_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FixedExpressionType"

def test_priorityoperator_exists():
    # Check that the Enumeration exists
    assert PriorityOperator is not None

def test_priorityoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PriorityOperator]
    expected_literals = [
        "LessThan",
        "Seperator",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PriorityOperator"

def test_typeid_exists():
    # Check that the Enumeration exists
    assert TypeId is not None

def test_typeid_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeId]
    expected_literals = [
        "Clock",
        "Integer",
        "Void",
        "Channel",
        "Boolean",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeId"


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
expressions_Selection_strategy = st.builds(
    expressions_Selection,
)
timedAutomata_core_System_strategy = st.builds(
    timedAutomata_core_System,
)
timedAutomata_core_TemplateInstantiation_strategy = st.builds(
    timedAutomata_core_TemplateInstantiation,
)
base_Commentable_strategy = st.builds(
    base_Commentable,
)
System_strategy = st.builds(
    System,
)
timedAutomata_core_ComplexSystem_strategy = st.builds(
    timedAutomata_core_ComplexSystem,
    operator=
        safe_text
)
timedAutomata_core_SimpleSystem_strategy = st.builds(
    timedAutomata_core_SimpleSystem,
)
TemplateInstantiation_strategy = st.builds(
    TemplateInstantiation,
)
timedAutomata_core_SystemDefinition_strategy = st.builds(
    timedAutomata_core_SystemDefinition,
)
core_timedAutomata_Label_strategy = st.builds(
    core_timedAutomata_Label,
)
Selections_strategy = st.builds(
    Selections,
)
Guards_strategy = st.builds(
    Guards,
)
core_timedAutomata_Nail_strategy = st.builds(
    core_timedAutomata_Nail,
)
Updates_strategy = st.builds(
    Updates,
)
Location_strategy = st.builds(
    Location,
)
base_Identifyable_strategy = st.builds(
    base_Identifyable,
)
base_Nameable_strategy = st.builds(
    base_Nameable,
)
timedAutomata_core_TAElement_strategy = st.builds(
    timedAutomata_core_TAElement,
)
core_TAElement_strategy = st.builds(
    core_TAElement,
)
timedAutomata_core_Template_strategy = st.builds(
    timedAutomata_core_Template,
)
SystemDefinition_strategy = st.builds(
    SystemDefinition,
)
Template_strategy = st.builds(
    Template,
)
Edge_strategy = st.builds(
    Edge,
)
core_timedAutomata_Parameter_strategy = st.builds(
    core_timedAutomata_Parameter,
)
declarations_FieldDeclaration_strategy = st.builds(
    declarations_FieldDeclaration,
)
TAElement_strategy = st.builds(
    TAElement,
)
timedAutomata_core_Project_strategy = st.builds(
    timedAutomata_core_Project,
    id=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
timedAutomata_types_Struct_strategy = st.builds(
    timedAutomata_types_Struct,
)
timedAutomata_types_IntegerRange_strategy = st.builds(
    timedAutomata_types_IntegerRange,
)
timedAutomata_types_SimpleType_strategy = st.builds(
    timedAutomata_types_SimpleType,
    type=
        safe_text
)
timedAutomata_types_IdentifierType_strategy = st.builds(
    timedAutomata_types_IdentifierType,
)
timedAutomata_types_Scalar_strategy = st.builds(
    timedAutomata_types_Scalar,
)
ChannelExpression_strategy = st.builds(
    ChannelExpression,
)
timedAutomata_declarations_IdentifierChannelExpression_strategy = st.builds(
    timedAutomata_declarations_IdentifierChannelExpression,
)
timedAutomata_declarations_ChannelExpression_strategy = st.builds(
    timedAutomata_declarations_ChannelExpression,
)
declarations_ChannelExpression_strategy = st.builds(
    declarations_ChannelExpression,
)
timedAutomata_types_Type_strategy = st.builds(
    timedAutomata_types_Type,
    prefix=
        safe_text
)
timedAutomata_declarations_ExpressionChannelExpression_strategy = st.builds(
    timedAutomata_declarations_ExpressionChannelExpression,
)
ChannelPriority_strategy = st.builds(
    ChannelPriority,
)
timedAutomata_declarations_ComplexChannelPriority_strategy = st.builds(
    timedAutomata_declarations_ComplexChannelPriority,
    channelOperator=
        safe_text
)
timedAutomata_declarations_SimpleChannelPriority_strategy = st.builds(
    timedAutomata_declarations_SimpleChannelPriority,
)
timedAutomata_declarations_DefaultChannelPriority_strategy = st.builds(
    timedAutomata_declarations_DefaultChannelPriority,
)
timedAutomata_declarations_ChannelPriority_strategy = st.builds(
    timedAutomata_declarations_ChannelPriority,
)
Statement_strategy = st.builds(
    Statement,
)
timedAutomata_declarations_ForLoopStatement_strategy = st.builds(
    timedAutomata_declarations_ForLoopStatement,
)
timedAutomata_declarations_IfStatement_strategy = st.builds(
    timedAutomata_declarations_IfStatement,
)
timedAutomata_declarations_IterationStatement_strategy = st.builds(
    timedAutomata_declarations_IterationStatement,
)
timedAutomata_declarations_DoWhileLoopStatement_strategy = st.builds(
    timedAutomata_declarations_DoWhileLoopStatement,
)
timedAutomata_declarations_ReturnStatement_strategy = st.builds(
    timedAutomata_declarations_ReturnStatement,
)
timedAutomata_declarations_ExpressionStatement_strategy = st.builds(
    timedAutomata_declarations_ExpressionStatement,
)
timedAutomata_declarations_WhileLoopStatement_strategy = st.builds(
    timedAutomata_declarations_WhileLoopStatement,
)
TAParameter_strategy = st.builds(
    TAParameter,
)
timedAutomata_declarations_CallByReferenceParameter_strategy = st.builds(
    timedAutomata_declarations_CallByReferenceParameter,
)
timedAutomata_declarations_CallByValueParameter_strategy = st.builds(
    timedAutomata_declarations_CallByValueParameter,
)
timedAutomata_declarations_TAParameter_strategy = st.builds(
    timedAutomata_declarations_TAParameter,
)
Initialiser_strategy = st.builds(
    Initialiser,
)
timedAutomata_declarations_ArrayInitialiser_strategy = st.builds(
    timedAutomata_declarations_ArrayInitialiser,
)
timedAutomata_declarations_Statement_strategy = st.builds(
    timedAutomata_declarations_Statement,
)
declarations_Statement_strategy = st.builds(
    declarations_Statement,
)
declarations_Declaration_strategy = st.builds(
    declarations_Declaration,
)
timedAutomata_declarations_Block_strategy = st.builds(
    timedAutomata_declarations_Block,
)
timedAutomata_declarations_ArrayDeclarationType_strategy = st.builds(
    timedAutomata_declarations_ArrayDeclarationType,
)
timedAutomata_declarations_ArrayDeclaration_strategy = st.builds(
    timedAutomata_declarations_ArrayDeclaration,
)
timedAutomata_declarations_FieldDeclaration_strategy = st.builds(
    timedAutomata_declarations_FieldDeclaration,
)
declarations_ChannelPriority_strategy = st.builds(
    declarations_ChannelPriority,
)
timedAutomata_declarations_ExpressionInitialiser_strategy = st.builds(
    timedAutomata_declarations_ExpressionInitialiser,
)
timedAutomata_declarations_Initialiser_strategy = st.builds(
    timedAutomata_declarations_Initialiser,
)
ArrayDeclarationType_strategy = st.builds(
    ArrayDeclarationType,
)
timedAutomata_declarations_ArrayTypeType_strategy = st.builds(
    timedAutomata_declarations_ArrayTypeType,
)
timedAutomata_declarations_ArrayExpressionType_strategy = st.builds(
    timedAutomata_declarations_ArrayExpressionType,
)
declarations_ArrayDeclaration_strategy = st.builds(
    declarations_ArrayDeclaration,
)
declarations_Initialiser_strategy = st.builds(
    declarations_Initialiser,
)
declarations_ArrayDeclarationType_strategy = st.builds(
    declarations_ArrayDeclarationType,
)
timedAutomata_declarations_VariableIdentifier_strategy = st.builds(
    timedAutomata_declarations_VariableIdentifier,
)
declarations_VariableIdentifier_strategy = st.builds(
    declarations_VariableIdentifier,
)
declarations_Block_strategy = st.builds(
    declarations_Block,
)
timedAutomata_declarations_BlockStatement_strategy = st.builds(
    timedAutomata_declarations_BlockStatement,
)
declarations_TAParameter_strategy = st.builds(
    declarations_TAParameter,
)
types_Type_strategy = st.builds(
    types_Type,
)
Declaration_strategy = st.builds(
    Declaration,
)
timedAutomata_declarations_TypeDeclaration_strategy = st.builds(
    timedAutomata_declarations_TypeDeclaration,
)
timedAutomata_declarations_FunctionDeclaration_strategy = st.builds(
    timedAutomata_declarations_FunctionDeclaration,
)
timedAutomata_declarations_ChannelPriorityDeclaration_strategy = st.builds(
    timedAutomata_declarations_ChannelPriorityDeclaration,
)
timedAutomata_declarations_VariableDeclaration_strategy = st.builds(
    timedAutomata_declarations_VariableDeclaration,
)
timedAutomata_expressions_Selection_strategy = st.builds(
    timedAutomata_expressions_Selection,
)
Identifier_strategy = st.builds(
    Identifier,
)
Expression_strategy = st.builds(
    Expression,
)
timedAutomata_expressions_UnaryExpression_strategy = st.builds(
    timedAutomata_expressions_UnaryExpression,
    operator=
        safe_text
)
timedAutomata_expressions_VariableExpression_strategy = st.builds(
    timedAutomata_expressions_VariableExpression,
)
timedAutomata_expressions_PointExpression_strategy = st.builds(
    timedAutomata_expressions_PointExpression,
)
timedAutomata_expressions_ForallExpression_strategy = st.builds(
    timedAutomata_expressions_ForallExpression,
)
timedAutomata_expressions_BinaryExpression_strategy = st.builds(
    timedAutomata_expressions_BinaryExpression,
    operator=
        safe_text
)
timedAutomata_expressions_FixedExpression_strategy = st.builds(
    timedAutomata_expressions_FixedExpression,
    type=
        safe_text
)
timedAutomata_expressions_GroupingExpression_strategy = st.builds(
    timedAutomata_expressions_GroupingExpression,
)
timedAutomata_expressions_ExistsExpression_strategy = st.builds(
    timedAutomata_expressions_ExistsExpression,
)
timedAutomata_expressions_IdentifierExpression_strategy = st.builds(
    timedAutomata_expressions_IdentifierExpression,
)
timedAutomata_expressions_AssignmentExpression_strategy = st.builds(
    timedAutomata_expressions_AssignmentExpression,
    operator=
        safe_text
)
timedAutomata_expressions_SimpleIfExpression_strategy = st.builds(
    timedAutomata_expressions_SimpleIfExpression,
)
timedAutomata_expressions_WithArgumentsExpression_strategy = st.builds(
    timedAutomata_expressions_WithArgumentsExpression,
)
timedAutomata_expressions_ConstantExpression_strategy = st.builds(
    timedAutomata_expressions_ConstantExpression,
    value=
        st.integers()
)
Commentable_strategy = st.builds(
    Commentable,
)
timedAutomata_declarations_Declaration_strategy = st.builds(
    timedAutomata_declarations_Declaration,
)
timedAutomata_expressions_Expression_strategy = st.builds(
    timedAutomata_expressions_Expression,
)
timedAutomata_expressions_IncDecExpression_strategy = st.builds(
    timedAutomata_expressions_IncDecExpression,
    beforeExpression=
        st.booleans(),
    increment=
        st.booleans()
)
timedAutomata_expressions_ArrayVariableExpression_strategy = st.builds(
    timedAutomata_expressions_ArrayVariableExpression,
)
Synchronisation_strategy = st.builds(
    Synchronisation,
)
timedAutomata_bnf_ReceiveSynchronisation_strategy = st.builds(
    timedAutomata_bnf_ReceiveSynchronisation,
)
timedAutomata_bnf_SendSynchronisation_strategy = st.builds(
    timedAutomata_bnf_SendSynchronisation,
)
timedAutomata_bnf_Identifier_strategy = st.builds(
    timedAutomata_bnf_Identifier,
    name=
        safe_text
)
timedAutomata_base_Nameable_strategy = st.builds(
    timedAutomata_base_Nameable,
    name=
        safe_text
)
timedAutomata_base_Identifyable_strategy = st.builds(
    timedAutomata_base_Identifyable,
    id=
        st.integers()
)
timedAutomata_base_Commentable_strategy = st.builds(
    timedAutomata_base_Commentable,
    comment=
        safe_text
)
expressions_Expression_strategy = st.builds(
    expressions_Expression,
)
Position_strategy = st.builds(
    Position,
)
timedAutomata_core_Selections_strategy = st.builds(
    timedAutomata_core_Selections,
)
timedAutomata_core_Edge_strategy = st.builds(
    timedAutomata_core_Edge,
)
timedAutomata_core_Guards_strategy = st.builds(
    timedAutomata_core_Guards,
)
timedAutomata_core_Location_strategy = st.builds(
    timedAutomata_core_Location,
    urgent=
        safe_text,
    committed=
        safe_text
)
timedAutomata_core_Updates_strategy = st.builds(
    timedAutomata_core_Updates,
)
timedAutomata_bnf_Synchronisation_strategy = st.builds(
    timedAutomata_bnf_Synchronisation,
)

@given(instance=expressions_Selection_strategy)
@settings(max_examples=50)
def test_expressions_selection_instantiation(instance):
    assert isinstance(instance, expressions_Selection)

@given(instance=timedAutomata_core_System_strategy)
@settings(max_examples=50)
def test_timedautomata_core_system_instantiation(instance):
    assert isinstance(instance, timedAutomata_core_System)

@given(instance=timedAutomata_core_TemplateInstantiation_strategy)
@settings(max_examples=50)
def test_timedautomata_core_templateinstantiation_instantiation(instance):
    assert isinstance(instance, timedAutomata_core_TemplateInstantiation)

@given(instance=base_Commentable_strategy)
@settings(max_examples=50)
def test_base_commentable_instantiation(instance):
    assert isinstance(instance, base_Commentable)

@given(instance=System_strategy)
@settings(max_examples=50)
def test_system_instantiation(instance):
    assert isinstance(instance, System)

@given(instance=timedAutomata_core_ComplexSystem_strategy)
@settings(max_examples=50)
def test_timedautomata_core_complexsystem_instantiation(instance):
    assert isinstance(instance, timedAutomata_core_ComplexSystem)



@given(instance=timedAutomata_core_ComplexSystem_strategy)
def test_timedautomata_core_complexsystem_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=timedAutomata_core_SimpleSystem_strategy)
@settings(max_examples=50)
def test_timedautomata_core_simplesystem_instantiation(instance):
    assert isinstance(instance, timedAutomata_core_SimpleSystem)

@given(instance=TemplateInstantiation_strategy)
@settings(max_examples=50)
def test_templateinstantiation_instantiation(instance):
    assert isinstance(instance, TemplateInstantiation)

@given(instance=timedAutomata_core_SystemDefinition_strategy)
@settings(max_examples=50)
def test_timedautomata_core_systemdefinition_instantiation(instance):
    assert isinstance(instance, timedAutomata_core_SystemDefinition)

@given(instance=core_timedAutomata_Label_strategy)
@settings(max_examples=50)
def test_core_timedautomata_label_instantiation(instance):
    assert isinstance(instance, core_timedAutomata_Label)

@given(instance=Selections_strategy)
@settings(max_examples=50)
def test_selections_instantiation(instance):
    assert isinstance(instance, Selections)

@given(instance=Guards_strategy)
@settings(max_examples=50)
def test_guards_instantiation(instance):
    assert isinstance(instance, Guards)

@given(instance=core_timedAutomata_Nail_strategy)
@settings(max_examples=50)
def test_core_timedautomata_nail_instantiation(instance):
    assert isinstance(instance, core_timedAutomata_Nail)

@given(instance=Updates_strategy)
@settings(max_examples=50)
def test_updates_instantiation(instance):
    assert isinstance(instance, Updates)

@given(instance=Location_strategy)
@settings(max_examples=50)
def test_location_instantiation(instance):
    assert isinstance(instance, Location)

@given(instance=base_Identifyable_strategy)
@settings(max_examples=50)
def test_base_identifyable_instantiation(instance):
    assert isinstance(instance, base_Identifyable)

@given(instance=base_Nameable_strategy)
@settings(max_examples=50)
def test_base_nameable_instantiation(instance):
    assert isinstance(instance, base_Nameable)

@given(instance=timedAutomata_core_TAElement_strategy)
@settings(max_examples=50)
def test_timedautomata_core_taelement_instantiation(instance):
    assert isinstance(instance, timedAutomata_core_TAElement)

@given(instance=core_TAElement_strategy)
@settings(max_examples=50)
def test_core_taelement_instantiation(instance):
    assert isinstance(instance, core_TAElement)

@given(instance=timedAutomata_core_Template_strategy)
@settings(max_examples=50)
def test_timedautomata_core_template_instantiation(instance):
    assert isinstance(instance, timedAutomata_core_Template)

@given(instance=SystemDefinition_strategy)
@settings(max_examples=50)
def test_systemdefinition_instantiation(instance):
    assert isinstance(instance, SystemDefinition)

@given(instance=Template_strategy)
@settings(max_examples=50)
def test_template_instantiation(instance):
    assert isinstance(instance, Template)

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=core_timedAutomata_Parameter_strategy)
@settings(max_examples=50)
def test_core_timedautomata_parameter_instantiation(instance):
    assert isinstance(instance, core_timedAutomata_Parameter)

@given(instance=declarations_FieldDeclaration_strategy)
@settings(max_examples=50)
def test_declarations_fielddeclaration_instantiation(instance):
    assert isinstance(instance, declarations_FieldDeclaration)

@given(instance=TAElement_strategy)
@settings(max_examples=50)
def test_taelement_instantiation(instance):
    assert isinstance(instance, TAElement)

@given(instance=timedAutomata_core_Project_strategy)
@settings(max_examples=50)
def test_timedautomata_core_project_instantiation(instance):
    assert isinstance(instance, timedAutomata_core_Project)



@given(instance=timedAutomata_core_Project_strategy)
def test_timedautomata_core_project_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=timedAutomata_types_Struct_strategy)
@settings(max_examples=50)
def test_timedautomata_types_struct_instantiation(instance):
    assert isinstance(instance, timedAutomata_types_Struct)

@given(instance=timedAutomata_types_IntegerRange_strategy)
@settings(max_examples=50)
def test_timedautomata_types_integerrange_instantiation(instance):
    assert isinstance(instance, timedAutomata_types_IntegerRange)

@given(instance=timedAutomata_types_SimpleType_strategy)
@settings(max_examples=50)
def test_timedautomata_types_simpletype_instantiation(instance):
    assert isinstance(instance, timedAutomata_types_SimpleType)



@given(instance=timedAutomata_types_SimpleType_strategy)
def test_timedautomata_types_simpletype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=timedAutomata_types_IdentifierType_strategy)
@settings(max_examples=50)
def test_timedautomata_types_identifiertype_instantiation(instance):
    assert isinstance(instance, timedAutomata_types_IdentifierType)

@given(instance=timedAutomata_types_Scalar_strategy)
@settings(max_examples=50)
def test_timedautomata_types_scalar_instantiation(instance):
    assert isinstance(instance, timedAutomata_types_Scalar)

@given(instance=ChannelExpression_strategy)
@settings(max_examples=50)
def test_channelexpression_instantiation(instance):
    assert isinstance(instance, ChannelExpression)

@given(instance=timedAutomata_declarations_IdentifierChannelExpression_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_identifierchannelexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_IdentifierChannelExpression)

@given(instance=timedAutomata_declarations_ChannelExpression_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_channelexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_ChannelExpression)

@given(instance=declarations_ChannelExpression_strategy)
@settings(max_examples=50)
def test_declarations_channelexpression_instantiation(instance):
    assert isinstance(instance, declarations_ChannelExpression)

@given(instance=timedAutomata_types_Type_strategy)
@settings(max_examples=50)
def test_timedautomata_types_type_instantiation(instance):
    assert isinstance(instance, timedAutomata_types_Type)



@given(instance=timedAutomata_types_Type_strategy)
def test_timedautomata_types_type_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original

@given(instance=timedAutomata_declarations_ExpressionChannelExpression_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_expressionchannelexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_ExpressionChannelExpression)

@given(instance=ChannelPriority_strategy)
@settings(max_examples=50)
def test_channelpriority_instantiation(instance):
    assert isinstance(instance, ChannelPriority)

@given(instance=timedAutomata_declarations_ComplexChannelPriority_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_complexchannelpriority_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_ComplexChannelPriority)



@given(instance=timedAutomata_declarations_ComplexChannelPriority_strategy)
def test_timedautomata_declarations_complexchannelpriority_channelOperator_setter(instance):
    original = instance.channelOperator
    instance.channelOperator = original
    assert instance.channelOperator == original

@given(instance=timedAutomata_declarations_SimpleChannelPriority_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_simplechannelpriority_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_SimpleChannelPriority)

@given(instance=timedAutomata_declarations_DefaultChannelPriority_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_defaultchannelpriority_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_DefaultChannelPriority)

@given(instance=timedAutomata_declarations_ChannelPriority_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_channelpriority_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_ChannelPriority)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=timedAutomata_declarations_ForLoopStatement_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_forloopstatement_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_ForLoopStatement)

@given(instance=timedAutomata_declarations_IfStatement_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_ifstatement_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_IfStatement)

@given(instance=timedAutomata_declarations_IterationStatement_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_iterationstatement_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_IterationStatement)

@given(instance=timedAutomata_declarations_DoWhileLoopStatement_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_dowhileloopstatement_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_DoWhileLoopStatement)

@given(instance=timedAutomata_declarations_ReturnStatement_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_returnstatement_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_ReturnStatement)

@given(instance=timedAutomata_declarations_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_expressionstatement_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_ExpressionStatement)

@given(instance=timedAutomata_declarations_WhileLoopStatement_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_whileloopstatement_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_WhileLoopStatement)

@given(instance=TAParameter_strategy)
@settings(max_examples=50)
def test_taparameter_instantiation(instance):
    assert isinstance(instance, TAParameter)

@given(instance=timedAutomata_declarations_CallByReferenceParameter_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_callbyreferenceparameter_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_CallByReferenceParameter)

@given(instance=timedAutomata_declarations_CallByValueParameter_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_callbyvalueparameter_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_CallByValueParameter)

@given(instance=timedAutomata_declarations_TAParameter_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_taparameter_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_TAParameter)

@given(instance=Initialiser_strategy)
@settings(max_examples=50)
def test_initialiser_instantiation(instance):
    assert isinstance(instance, Initialiser)

@given(instance=timedAutomata_declarations_ArrayInitialiser_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_arrayinitialiser_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_ArrayInitialiser)

@given(instance=timedAutomata_declarations_Statement_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_statement_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_Statement)

@given(instance=declarations_Statement_strategy)
@settings(max_examples=50)
def test_declarations_statement_instantiation(instance):
    assert isinstance(instance, declarations_Statement)

@given(instance=declarations_Declaration_strategy)
@settings(max_examples=50)
def test_declarations_declaration_instantiation(instance):
    assert isinstance(instance, declarations_Declaration)

@given(instance=timedAutomata_declarations_Block_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_block_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_Block)

@given(instance=timedAutomata_declarations_ArrayDeclarationType_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_arraydeclarationtype_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_ArrayDeclarationType)

@given(instance=timedAutomata_declarations_ArrayDeclaration_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_arraydeclaration_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_ArrayDeclaration)

@given(instance=timedAutomata_declarations_FieldDeclaration_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_fielddeclaration_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_FieldDeclaration)

@given(instance=declarations_ChannelPriority_strategy)
@settings(max_examples=50)
def test_declarations_channelpriority_instantiation(instance):
    assert isinstance(instance, declarations_ChannelPriority)

@given(instance=timedAutomata_declarations_ExpressionInitialiser_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_expressioninitialiser_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_ExpressionInitialiser)

@given(instance=timedAutomata_declarations_Initialiser_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_initialiser_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_Initialiser)

@given(instance=ArrayDeclarationType_strategy)
@settings(max_examples=50)
def test_arraydeclarationtype_instantiation(instance):
    assert isinstance(instance, ArrayDeclarationType)

@given(instance=timedAutomata_declarations_ArrayTypeType_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_arraytypetype_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_ArrayTypeType)

@given(instance=timedAutomata_declarations_ArrayExpressionType_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_arrayexpressiontype_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_ArrayExpressionType)

@given(instance=declarations_ArrayDeclaration_strategy)
@settings(max_examples=50)
def test_declarations_arraydeclaration_instantiation(instance):
    assert isinstance(instance, declarations_ArrayDeclaration)

@given(instance=declarations_Initialiser_strategy)
@settings(max_examples=50)
def test_declarations_initialiser_instantiation(instance):
    assert isinstance(instance, declarations_Initialiser)

@given(instance=declarations_ArrayDeclarationType_strategy)
@settings(max_examples=50)
def test_declarations_arraydeclarationtype_instantiation(instance):
    assert isinstance(instance, declarations_ArrayDeclarationType)

@given(instance=timedAutomata_declarations_VariableIdentifier_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_variableidentifier_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_VariableIdentifier)

@given(instance=declarations_VariableIdentifier_strategy)
@settings(max_examples=50)
def test_declarations_variableidentifier_instantiation(instance):
    assert isinstance(instance, declarations_VariableIdentifier)

@given(instance=declarations_Block_strategy)
@settings(max_examples=50)
def test_declarations_block_instantiation(instance):
    assert isinstance(instance, declarations_Block)

@given(instance=timedAutomata_declarations_BlockStatement_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_blockstatement_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_BlockStatement)

@given(instance=declarations_TAParameter_strategy)
@settings(max_examples=50)
def test_declarations_taparameter_instantiation(instance):
    assert isinstance(instance, declarations_TAParameter)

@given(instance=types_Type_strategy)
@settings(max_examples=50)
def test_types_type_instantiation(instance):
    assert isinstance(instance, types_Type)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=timedAutomata_declarations_TypeDeclaration_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_typedeclaration_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_TypeDeclaration)

@given(instance=timedAutomata_declarations_FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_functiondeclaration_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_FunctionDeclaration)

@given(instance=timedAutomata_declarations_ChannelPriorityDeclaration_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_channelprioritydeclaration_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_ChannelPriorityDeclaration)

@given(instance=timedAutomata_declarations_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_variabledeclaration_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_VariableDeclaration)

@given(instance=timedAutomata_expressions_Selection_strategy)
@settings(max_examples=50)
def test_timedautomata_expressions_selection_instantiation(instance):
    assert isinstance(instance, timedAutomata_expressions_Selection)

@given(instance=Identifier_strategy)
@settings(max_examples=50)
def test_identifier_instantiation(instance):
    assert isinstance(instance, Identifier)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=timedAutomata_expressions_UnaryExpression_strategy)
@settings(max_examples=50)
def test_timedautomata_expressions_unaryexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata_expressions_UnaryExpression)



@given(instance=timedAutomata_expressions_UnaryExpression_strategy)
def test_timedautomata_expressions_unaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=timedAutomata_expressions_VariableExpression_strategy)
@settings(max_examples=50)
def test_timedautomata_expressions_variableexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata_expressions_VariableExpression)

@given(instance=timedAutomata_expressions_PointExpression_strategy)
@settings(max_examples=50)
def test_timedautomata_expressions_pointexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata_expressions_PointExpression)

@given(instance=timedAutomata_expressions_ForallExpression_strategy)
@settings(max_examples=50)
def test_timedautomata_expressions_forallexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata_expressions_ForallExpression)

@given(instance=timedAutomata_expressions_BinaryExpression_strategy)
@settings(max_examples=50)
def test_timedautomata_expressions_binaryexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata_expressions_BinaryExpression)



@given(instance=timedAutomata_expressions_BinaryExpression_strategy)
def test_timedautomata_expressions_binaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=timedAutomata_expressions_FixedExpression_strategy)
@settings(max_examples=50)
def test_timedautomata_expressions_fixedexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata_expressions_FixedExpression)



@given(instance=timedAutomata_expressions_FixedExpression_strategy)
def test_timedautomata_expressions_fixedexpression_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=timedAutomata_expressions_GroupingExpression_strategy)
@settings(max_examples=50)
def test_timedautomata_expressions_groupingexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata_expressions_GroupingExpression)

@given(instance=timedAutomata_expressions_ExistsExpression_strategy)
@settings(max_examples=50)
def test_timedautomata_expressions_existsexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata_expressions_ExistsExpression)

@given(instance=timedAutomata_expressions_IdentifierExpression_strategy)
@settings(max_examples=50)
def test_timedautomata_expressions_identifierexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata_expressions_IdentifierExpression)

@given(instance=timedAutomata_expressions_AssignmentExpression_strategy)
@settings(max_examples=50)
def test_timedautomata_expressions_assignmentexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata_expressions_AssignmentExpression)



@given(instance=timedAutomata_expressions_AssignmentExpression_strategy)
def test_timedautomata_expressions_assignmentexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=timedAutomata_expressions_SimpleIfExpression_strategy)
@settings(max_examples=50)
def test_timedautomata_expressions_simpleifexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata_expressions_SimpleIfExpression)

@given(instance=timedAutomata_expressions_WithArgumentsExpression_strategy)
@settings(max_examples=50)
def test_timedautomata_expressions_withargumentsexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata_expressions_WithArgumentsExpression)

@given(instance=timedAutomata_expressions_ConstantExpression_strategy)
@settings(max_examples=50)
def test_timedautomata_expressions_constantexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata_expressions_ConstantExpression)



@given(instance=timedAutomata_expressions_ConstantExpression_strategy)
def test_timedautomata_expressions_constantexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Commentable_strategy)
@settings(max_examples=50)
def test_commentable_instantiation(instance):
    assert isinstance(instance, Commentable)

@given(instance=timedAutomata_declarations_Declaration_strategy)
@settings(max_examples=50)
def test_timedautomata_declarations_declaration_instantiation(instance):
    assert isinstance(instance, timedAutomata_declarations_Declaration)

@given(instance=timedAutomata_expressions_Expression_strategy)
@settings(max_examples=50)
def test_timedautomata_expressions_expression_instantiation(instance):
    assert isinstance(instance, timedAutomata_expressions_Expression)

@given(instance=timedAutomata_expressions_IncDecExpression_strategy)
@settings(max_examples=50)
def test_timedautomata_expressions_incdecexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata_expressions_IncDecExpression)



@given(instance=timedAutomata_expressions_IncDecExpression_strategy)
def test_timedautomata_expressions_incdecexpression_beforeExpression_setter(instance):
    original = instance.beforeExpression
    instance.beforeExpression = original
    assert instance.beforeExpression == original



@given(instance=timedAutomata_expressions_IncDecExpression_strategy)
def test_timedautomata_expressions_incdecexpression_increment_setter(instance):
    original = instance.increment
    instance.increment = original
    assert instance.increment == original

@given(instance=timedAutomata_expressions_ArrayVariableExpression_strategy)
@settings(max_examples=50)
def test_timedautomata_expressions_arrayvariableexpression_instantiation(instance):
    assert isinstance(instance, timedAutomata_expressions_ArrayVariableExpression)

@given(instance=Synchronisation_strategy)
@settings(max_examples=50)
def test_synchronisation_instantiation(instance):
    assert isinstance(instance, Synchronisation)

@given(instance=timedAutomata_bnf_ReceiveSynchronisation_strategy)
@settings(max_examples=50)
def test_timedautomata_bnf_receivesynchronisation_instantiation(instance):
    assert isinstance(instance, timedAutomata_bnf_ReceiveSynchronisation)

@given(instance=timedAutomata_bnf_SendSynchronisation_strategy)
@settings(max_examples=50)
def test_timedautomata_bnf_sendsynchronisation_instantiation(instance):
    assert isinstance(instance, timedAutomata_bnf_SendSynchronisation)

@given(instance=timedAutomata_bnf_Identifier_strategy)
@settings(max_examples=50)
def test_timedautomata_bnf_identifier_instantiation(instance):
    assert isinstance(instance, timedAutomata_bnf_Identifier)



@given(instance=timedAutomata_bnf_Identifier_strategy)
def test_timedautomata_bnf_identifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=timedAutomata_base_Nameable_strategy)
@settings(max_examples=50)
def test_timedautomata_base_nameable_instantiation(instance):
    assert isinstance(instance, timedAutomata_base_Nameable)



@given(instance=timedAutomata_base_Nameable_strategy)
def test_timedautomata_base_nameable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=timedAutomata_base_Identifyable_strategy)
@settings(max_examples=50)
def test_timedautomata_base_identifyable_instantiation(instance):
    assert isinstance(instance, timedAutomata_base_Identifyable)



@given(instance=timedAutomata_base_Identifyable_strategy)
def test_timedautomata_base_identifyable_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=timedAutomata_base_Commentable_strategy)
@settings(max_examples=50)
def test_timedautomata_base_commentable_instantiation(instance):
    assert isinstance(instance, timedAutomata_base_Commentable)



@given(instance=timedAutomata_base_Commentable_strategy)
def test_timedautomata_base_commentable_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=expressions_Expression_strategy)
@settings(max_examples=50)
def test_expressions_expression_instantiation(instance):
    assert isinstance(instance, expressions_Expression)

@given(instance=Position_strategy)
@settings(max_examples=50)
def test_position_instantiation(instance):
    assert isinstance(instance, Position)

@given(instance=timedAutomata_core_Selections_strategy)
@settings(max_examples=50)
def test_timedautomata_core_selections_instantiation(instance):
    assert isinstance(instance, timedAutomata_core_Selections)

@given(instance=timedAutomata_core_Edge_strategy)
@settings(max_examples=50)
def test_timedautomata_core_edge_instantiation(instance):
    assert isinstance(instance, timedAutomata_core_Edge)

@given(instance=timedAutomata_core_Guards_strategy)
@settings(max_examples=50)
def test_timedautomata_core_guards_instantiation(instance):
    assert isinstance(instance, timedAutomata_core_Guards)

@given(instance=timedAutomata_core_Location_strategy)
@settings(max_examples=50)
def test_timedautomata_core_location_instantiation(instance):
    assert isinstance(instance, timedAutomata_core_Location)



@given(instance=timedAutomata_core_Location_strategy)
def test_timedautomata_core_location_urgent_setter(instance):
    original = instance.urgent
    instance.urgent = original
    assert instance.urgent == original



@given(instance=timedAutomata_core_Location_strategy)
def test_timedautomata_core_location_committed_setter(instance):
    original = instance.committed
    instance.committed = original
    assert instance.committed == original

@given(instance=timedAutomata_core_Updates_strategy)
@settings(max_examples=50)
def test_timedautomata_core_updates_instantiation(instance):
    assert isinstance(instance, timedAutomata_core_Updates)

@given(instance=timedAutomata_bnf_Synchronisation_strategy)
@settings(max_examples=50)
def test_timedautomata_bnf_synchronisation_instantiation(instance):
    assert isinstance(instance, timedAutomata_bnf_Synchronisation)
