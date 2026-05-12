import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    uppaal_visuals_Point,
    uppaal_visuals_LinearElement,
    Point,
    uppaal_visuals_PlanarElement,
    uppaal_visuals_ColoredElement,
    expressions_Expression,
    BinaryExpression,
    uppaal_expressions_ArithmeticExpression,
    uppaal_expressions_MinMaxExpression,
    uppaal_expressions_LogicalExpression,
    uppaal_expressions_BitShiftExpression,
    uppaal_expressions_BitwiseExpression,
    uppaal_expressions_CompareExpression,
    uppaal_expressions_AssignmentExpression,
    uppaal_expressions_Expression,
    statements_Statement,
    Statement,
    uppaal_statements_WhileLoop,
    uppaal_statements_EmptyStatement,
    uppaal_statements_ReturnStatement,
    uppaal_statements_ForLoop,
    uppaal_statements_ExpressionStatement,
    uppaal_statements_DoWhileLoop,
    uppaal_statements_IfStatement,
    uppaal_statements_Block,
    uppaal_statements_Statement,
    uppaal_templates_Synchronization,
    Selection,
    Synchronization,
    visuals_ColoredElement,
    visuals_PlanarElement,
    visuals_LinearElement,
    system_TemplateDeclaration,
    Edge,
    Location,
    LocalDeclarations,
    uppaal_system_ProgressMeasure,
    AbstractTemplate,
    uppaal_templates_RedefinedTemplate,
    uppaal_templates_Template,
    uppaal_system_InstantiationList,
    system_InstantiationList,
    uppaal_system_System,
    RedefinedTemplate,
    IdentifierExpression,
    ChannelPriorityItem,
    uppaal_global_DefaultChannelPriority,
    uppaal_global_ChannelList,
    uppaal_global_ChannelPriorityItem,
    global_ChannelPriorityItem,
    uppaal_global_ChannelPriority,
    uppaal_declarations_Initializer,
    uppaal_declarations_Parameter,
    Variable,
    uppaal_declarations_VariableContainer,
    uppaal_declarations_Index,
    Initializer,
    uppaal_declarations_ArrayInitializer,
    uppaal_declarations_ExpressionInitializer,
    VariableContainer,
    uppaal_templates_Selection,
    DeclaredType,
    Parameter,
    Block,
    Function,
    VariableDeclaration,
    uppaal_declarations_ClockVariableDeclaration,
    uppaal_declarations_DataVariableDeclaration,
    uppaal_declarations_ChannelVariableDeclaration,
    declarations_VariableContainer,
    uppaal_expressions_QuantificationExpression,
    uppaal_statements_Iteration,
    declarations_Declaration,
    uppaal_declarations_VariableDeclaration,
    uppaal_declarations_Declaration,
    system_ProgressMeasure,
    system_System,
    global_ChannelPriority,
    Declarations,
    uppaal_declarations_LocalDeclarations,
    uppaal_declarations_SystemDeclarations,
    uppaal_declarations_GlobalDeclarations,
    Declaration,
    uppaal_declarations_FunctionDeclaration,
    uppaal_system_TemplateDeclaration,
    uppaal_declarations_TypeDeclaration,
    uppaal_declarations_Declarations,
    uppaal_types_Library,
    IntegerBounds,
    DataVariableDeclaration,
    Expression,
    uppaal_expressions_ConditionExpression,
    uppaal_expressions_NegationExpression,
    uppaal_expressions_BinaryExpression,
    uppaal_expressions_ScopedIdentifierExpression,
    uppaal_expressions_LiteralExpression,
    uppaal_expressions_IncrementDecrementExpression,
    uppaal_expressions_MinusExpression,
    uppaal_expressions_IdentifierExpression,
    uppaal_expressions_PlusExpression,
    uppaal_expressions_FunctionCallExpression,
    uppaal_types_TypeDefinition,
    TypeDefinition,
    uppaal_types_TypeSpecification,
    uppaal_types_TypeReference,
    uppaal_types_IntegerBounds,
    TypeDeclaration,
    Type,
    uppaal_types_DeclaredType,
    uppaal_types_PredefinedType,
    TypeSpecification,
    uppaal_types_RangeTypeSpecification,
    uppaal_types_StructTypeSpecification,
    uppaal_types_ScalarTypeSpecification,
    Index,
    uppaal_declarations_ValueIndex,
    uppaal_declarations_TypeIndex,
    NamedElement,
    uppaal_declarations_Function,
    uppaal_declarations_Variable,
    uppaal_types_Type,
    uppaal_core_CommentableElement,
    PredefinedType,
    SystemDeclarations,
    Template,
    GlobalDeclarations,
    uppaal_core_NamedElement,
    core_CommentableElement,
    uppaal_templates_Edge,
    core_NamedElement,
    uppaal_templates_AbstractTemplate,
    uppaal_templates_Location,
    uppaal_NTA,
    LogicalOperator,
    LocationKind,
    CompareOperator,
    IncrementDecrementOperator,
    IncrementDecrementPosition,
    DataVariablePrefix,
    BitShiftOperator,
    MinMaxOperator,
    BitwiseOperator,
    CallType,
    ArithmeticOperator,
    AssignmentOperator,
    Quantifier,
    SynchronizationKind,
    ColorKind,
    BuiltInType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uppaal_visuals_point_is_not_abstract():
    assert not inspect.isabstract(uppaal_visuals_Point)


def test_uppaal_visuals_point_constructor_exists():
    assert callable(uppaal_visuals_Point.__init__)


def test_uppaal_visuals_point_constructor_args():
    sig = inspect.signature(uppaal_visuals_Point.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_uppaal_visuals_point_has_y():
    assert hasattr(uppaal_visuals_Point, "y")
    descriptor = None
    for klass in uppaal_visuals_Point.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_visuals_point_has_x():
    assert hasattr(uppaal_visuals_Point, "x")
    descriptor = None
    for klass in uppaal_visuals_Point.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_visuals_linearelement_is_not_abstract():
    assert not inspect.isabstract(uppaal_visuals_LinearElement)


def test_uppaal_visuals_linearelement_constructor_exists():
    assert callable(uppaal_visuals_LinearElement.__init__)


def test_uppaal_visuals_linearelement_constructor_args():
    sig = inspect.signature(uppaal_visuals_LinearElement.__init__)
    params = list(sig.parameters.keys())



def test_point_is_not_abstract():
    assert not inspect.isabstract(Point)


def test_point_constructor_exists():
    assert callable(Point.__init__)


def test_point_constructor_args():
    sig = inspect.signature(Point.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_visuals_planarelement_is_not_abstract():
    assert not inspect.isabstract(uppaal_visuals_PlanarElement)


def test_uppaal_visuals_planarelement_constructor_exists():
    assert callable(uppaal_visuals_PlanarElement.__init__)


def test_uppaal_visuals_planarelement_constructor_args():
    sig = inspect.signature(uppaal_visuals_PlanarElement.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_visuals_coloredelement_is_not_abstract():
    assert not inspect.isabstract(uppaal_visuals_ColoredElement)


def test_uppaal_visuals_coloredelement_constructor_exists():
    assert callable(uppaal_visuals_ColoredElement.__init__)


def test_uppaal_visuals_coloredelement_constructor_args():
    sig = inspect.signature(uppaal_visuals_ColoredElement.__init__)
    params = list(sig.parameters.keys())
    assert "colorCode" in params, "Missing parameter 'colorCode'"
    assert "color" in params, "Missing parameter 'color'"

def test_uppaal_visuals_coloredelement_has_colorCode():
    assert hasattr(uppaal_visuals_ColoredElement, "colorCode")
    descriptor = None
    for klass in uppaal_visuals_ColoredElement.__mro__:
        if "colorCode" in klass.__dict__:
            descriptor = klass.__dict__["colorCode"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_visuals_coloredelement_has_color():
    assert hasattr(uppaal_visuals_ColoredElement, "color")
    descriptor = None
    for klass in uppaal_visuals_ColoredElement.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_expressions_expression_is_not_abstract():
    assert not inspect.isabstract(expressions_Expression)


def test_expressions_expression_constructor_exists():
    assert callable(expressions_Expression.__init__)


def test_expressions_expression_constructor_args():
    sig = inspect.signature(expressions_Expression.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_expressions_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_ArithmeticExpression)


def test_uppaal_expressions_arithmeticexpression_constructor_exists():
    assert callable(uppaal_expressions_ArithmeticExpression.__init__)


def test_uppaal_expressions_arithmeticexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_uppaal_expressions_arithmeticexpression_has_operator():
    assert hasattr(uppaal_expressions_ArithmeticExpression, "operator")
    descriptor = None
    for klass in uppaal_expressions_ArithmeticExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_expressions_minmaxexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_MinMaxExpression)


def test_uppaal_expressions_minmaxexpression_constructor_exists():
    assert callable(uppaal_expressions_MinMaxExpression.__init__)


def test_uppaal_expressions_minmaxexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_MinMaxExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_uppaal_expressions_minmaxexpression_has_operator():
    assert hasattr(uppaal_expressions_MinMaxExpression, "operator")
    descriptor = None
    for klass in uppaal_expressions_MinMaxExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_expressions_logicalexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_LogicalExpression)


def test_uppaal_expressions_logicalexpression_constructor_exists():
    assert callable(uppaal_expressions_LogicalExpression.__init__)


def test_uppaal_expressions_logicalexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_LogicalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_uppaal_expressions_logicalexpression_has_operator():
    assert hasattr(uppaal_expressions_LogicalExpression, "operator")
    descriptor = None
    for klass in uppaal_expressions_LogicalExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_expressions_bitshiftexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_BitShiftExpression)


def test_uppaal_expressions_bitshiftexpression_constructor_exists():
    assert callable(uppaal_expressions_BitShiftExpression.__init__)


def test_uppaal_expressions_bitshiftexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_BitShiftExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_uppaal_expressions_bitshiftexpression_has_operator():
    assert hasattr(uppaal_expressions_BitShiftExpression, "operator")
    descriptor = None
    for klass in uppaal_expressions_BitShiftExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_expressions_bitwiseexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_BitwiseExpression)


def test_uppaal_expressions_bitwiseexpression_constructor_exists():
    assert callable(uppaal_expressions_BitwiseExpression.__init__)


def test_uppaal_expressions_bitwiseexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_BitwiseExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_uppaal_expressions_bitwiseexpression_has_operator():
    assert hasattr(uppaal_expressions_BitwiseExpression, "operator")
    descriptor = None
    for klass in uppaal_expressions_BitwiseExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_expressions_compareexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_CompareExpression)


def test_uppaal_expressions_compareexpression_constructor_exists():
    assert callable(uppaal_expressions_CompareExpression.__init__)


def test_uppaal_expressions_compareexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_CompareExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_uppaal_expressions_compareexpression_has_operator():
    assert hasattr(uppaal_expressions_CompareExpression, "operator")
    descriptor = None
    for klass in uppaal_expressions_CompareExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_expressions_assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_AssignmentExpression)


def test_uppaal_expressions_assignmentexpression_constructor_exists():
    assert callable(uppaal_expressions_AssignmentExpression.__init__)


def test_uppaal_expressions_assignmentexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_AssignmentExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_uppaal_expressions_assignmentexpression_has_operator():
    assert hasattr(uppaal_expressions_AssignmentExpression, "operator")
    descriptor = None
    for klass in uppaal_expressions_AssignmentExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_expressions_expression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_Expression)


def test_uppaal_expressions_expression_constructor_exists():
    assert callable(uppaal_expressions_Expression.__init__)


def test_uppaal_expressions_expression_constructor_args():
    sig = inspect.signature(uppaal_expressions_Expression.__init__)
    params = list(sig.parameters.keys())



def test_statements_statement_is_not_abstract():
    assert not inspect.isabstract(statements_Statement)


def test_statements_statement_constructor_exists():
    assert callable(statements_Statement.__init__)


def test_statements_statement_constructor_args():
    sig = inspect.signature(statements_Statement.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_statements_whileloop_is_not_abstract():
    assert not inspect.isabstract(uppaal_statements_WhileLoop)


def test_uppaal_statements_whileloop_constructor_exists():
    assert callable(uppaal_statements_WhileLoop.__init__)


def test_uppaal_statements_whileloop_constructor_args():
    sig = inspect.signature(uppaal_statements_WhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_statements_emptystatement_is_not_abstract():
    assert not inspect.isabstract(uppaal_statements_EmptyStatement)


def test_uppaal_statements_emptystatement_constructor_exists():
    assert callable(uppaal_statements_EmptyStatement.__init__)


def test_uppaal_statements_emptystatement_constructor_args():
    sig = inspect.signature(uppaal_statements_EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_statements_returnstatement_is_not_abstract():
    assert not inspect.isabstract(uppaal_statements_ReturnStatement)


def test_uppaal_statements_returnstatement_constructor_exists():
    assert callable(uppaal_statements_ReturnStatement.__init__)


def test_uppaal_statements_returnstatement_constructor_args():
    sig = inspect.signature(uppaal_statements_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_statements_forloop_is_not_abstract():
    assert not inspect.isabstract(uppaal_statements_ForLoop)


def test_uppaal_statements_forloop_constructor_exists():
    assert callable(uppaal_statements_ForLoop.__init__)


def test_uppaal_statements_forloop_constructor_args():
    sig = inspect.signature(uppaal_statements_ForLoop.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_statements_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(uppaal_statements_ExpressionStatement)


def test_uppaal_statements_expressionstatement_constructor_exists():
    assert callable(uppaal_statements_ExpressionStatement.__init__)


def test_uppaal_statements_expressionstatement_constructor_args():
    sig = inspect.signature(uppaal_statements_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_statements_dowhileloop_is_not_abstract():
    assert not inspect.isabstract(uppaal_statements_DoWhileLoop)


def test_uppaal_statements_dowhileloop_constructor_exists():
    assert callable(uppaal_statements_DoWhileLoop.__init__)


def test_uppaal_statements_dowhileloop_constructor_args():
    sig = inspect.signature(uppaal_statements_DoWhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_statements_ifstatement_is_not_abstract():
    assert not inspect.isabstract(uppaal_statements_IfStatement)


def test_uppaal_statements_ifstatement_constructor_exists():
    assert callable(uppaal_statements_IfStatement.__init__)


def test_uppaal_statements_ifstatement_constructor_args():
    sig = inspect.signature(uppaal_statements_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_statements_block_is_not_abstract():
    assert not inspect.isabstract(uppaal_statements_Block)


def test_uppaal_statements_block_constructor_exists():
    assert callable(uppaal_statements_Block.__init__)


def test_uppaal_statements_block_constructor_args():
    sig = inspect.signature(uppaal_statements_Block.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_statements_statement_is_not_abstract():
    assert not inspect.isabstract(uppaal_statements_Statement)


def test_uppaal_statements_statement_constructor_exists():
    assert callable(uppaal_statements_Statement.__init__)


def test_uppaal_statements_statement_constructor_args():
    sig = inspect.signature(uppaal_statements_Statement.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_templates_synchronization_is_not_abstract():
    assert not inspect.isabstract(uppaal_templates_Synchronization)


def test_uppaal_templates_synchronization_constructor_exists():
    assert callable(uppaal_templates_Synchronization.__init__)


def test_uppaal_templates_synchronization_constructor_args():
    sig = inspect.signature(uppaal_templates_Synchronization.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_uppaal_templates_synchronization_has_kind():
    assert hasattr(uppaal_templates_Synchronization, "kind")
    descriptor = None
    for klass in uppaal_templates_Synchronization.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_selection_is_not_abstract():
    assert not inspect.isabstract(Selection)


def test_selection_constructor_exists():
    assert callable(Selection.__init__)


def test_selection_constructor_args():
    sig = inspect.signature(Selection.__init__)
    params = list(sig.parameters.keys())



def test_synchronization_is_not_abstract():
    assert not inspect.isabstract(Synchronization)


def test_synchronization_constructor_exists():
    assert callable(Synchronization.__init__)


def test_synchronization_constructor_args():
    sig = inspect.signature(Synchronization.__init__)
    params = list(sig.parameters.keys())



def test_visuals_coloredelement_is_not_abstract():
    assert not inspect.isabstract(visuals_ColoredElement)


def test_visuals_coloredelement_constructor_exists():
    assert callable(visuals_ColoredElement.__init__)


def test_visuals_coloredelement_constructor_args():
    sig = inspect.signature(visuals_ColoredElement.__init__)
    params = list(sig.parameters.keys())



def test_visuals_planarelement_is_not_abstract():
    assert not inspect.isabstract(visuals_PlanarElement)


def test_visuals_planarelement_constructor_exists():
    assert callable(visuals_PlanarElement.__init__)


def test_visuals_planarelement_constructor_args():
    sig = inspect.signature(visuals_PlanarElement.__init__)
    params = list(sig.parameters.keys())



def test_visuals_linearelement_is_not_abstract():
    assert not inspect.isabstract(visuals_LinearElement)


def test_visuals_linearelement_constructor_exists():
    assert callable(visuals_LinearElement.__init__)


def test_visuals_linearelement_constructor_args():
    sig = inspect.signature(visuals_LinearElement.__init__)
    params = list(sig.parameters.keys())



def test_system_templatedeclaration_is_not_abstract():
    assert not inspect.isabstract(system_TemplateDeclaration)


def test_system_templatedeclaration_constructor_exists():
    assert callable(system_TemplateDeclaration.__init__)


def test_system_templatedeclaration_constructor_args():
    sig = inspect.signature(system_TemplateDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_location_is_not_abstract():
    assert not inspect.isabstract(Location)


def test_location_constructor_exists():
    assert callable(Location.__init__)


def test_location_constructor_args():
    sig = inspect.signature(Location.__init__)
    params = list(sig.parameters.keys())



def test_localdeclarations_is_not_abstract():
    assert not inspect.isabstract(LocalDeclarations)


def test_localdeclarations_constructor_exists():
    assert callable(LocalDeclarations.__init__)


def test_localdeclarations_constructor_args():
    sig = inspect.signature(LocalDeclarations.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_system_progressmeasure_is_not_abstract():
    assert not inspect.isabstract(uppaal_system_ProgressMeasure)


def test_uppaal_system_progressmeasure_constructor_exists():
    assert callable(uppaal_system_ProgressMeasure.__init__)


def test_uppaal_system_progressmeasure_constructor_args():
    sig = inspect.signature(uppaal_system_ProgressMeasure.__init__)
    params = list(sig.parameters.keys())



def test_abstracttemplate_is_not_abstract():
    assert not inspect.isabstract(AbstractTemplate)


def test_abstracttemplate_constructor_exists():
    assert callable(AbstractTemplate.__init__)


def test_abstracttemplate_constructor_args():
    sig = inspect.signature(AbstractTemplate.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_templates_redefinedtemplate_is_not_abstract():
    assert not inspect.isabstract(uppaal_templates_RedefinedTemplate)


def test_uppaal_templates_redefinedtemplate_constructor_exists():
    assert callable(uppaal_templates_RedefinedTemplate.__init__)


def test_uppaal_templates_redefinedtemplate_constructor_args():
    sig = inspect.signature(uppaal_templates_RedefinedTemplate.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_templates_template_is_not_abstract():
    assert not inspect.isabstract(uppaal_templates_Template)


def test_uppaal_templates_template_constructor_exists():
    assert callable(uppaal_templates_Template.__init__)


def test_uppaal_templates_template_constructor_args():
    sig = inspect.signature(uppaal_templates_Template.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_system_instantiationlist_is_not_abstract():
    assert not inspect.isabstract(uppaal_system_InstantiationList)


def test_uppaal_system_instantiationlist_constructor_exists():
    assert callable(uppaal_system_InstantiationList.__init__)


def test_uppaal_system_instantiationlist_constructor_args():
    sig = inspect.signature(uppaal_system_InstantiationList.__init__)
    params = list(sig.parameters.keys())



def test_system_instantiationlist_is_not_abstract():
    assert not inspect.isabstract(system_InstantiationList)


def test_system_instantiationlist_constructor_exists():
    assert callable(system_InstantiationList.__init__)


def test_system_instantiationlist_constructor_args():
    sig = inspect.signature(system_InstantiationList.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_system_system_is_not_abstract():
    assert not inspect.isabstract(uppaal_system_System)


def test_uppaal_system_system_constructor_exists():
    assert callable(uppaal_system_System.__init__)


def test_uppaal_system_system_constructor_args():
    sig = inspect.signature(uppaal_system_System.__init__)
    params = list(sig.parameters.keys())



def test_redefinedtemplate_is_not_abstract():
    assert not inspect.isabstract(RedefinedTemplate)


def test_redefinedtemplate_constructor_exists():
    assert callable(RedefinedTemplate.__init__)


def test_redefinedtemplate_constructor_args():
    sig = inspect.signature(RedefinedTemplate.__init__)
    params = list(sig.parameters.keys())



def test_identifierexpression_is_not_abstract():
    assert not inspect.isabstract(IdentifierExpression)


def test_identifierexpression_constructor_exists():
    assert callable(IdentifierExpression.__init__)


def test_identifierexpression_constructor_args():
    sig = inspect.signature(IdentifierExpression.__init__)
    params = list(sig.parameters.keys())



def test_channelpriorityitem_is_not_abstract():
    assert not inspect.isabstract(ChannelPriorityItem)


def test_channelpriorityitem_constructor_exists():
    assert callable(ChannelPriorityItem.__init__)


def test_channelpriorityitem_constructor_args():
    sig = inspect.signature(ChannelPriorityItem.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_global_defaultchannelpriority_is_not_abstract():
    assert not inspect.isabstract(uppaal_global_DefaultChannelPriority)


def test_uppaal_global_defaultchannelpriority_constructor_exists():
    assert callable(uppaal_global_DefaultChannelPriority.__init__)


def test_uppaal_global_defaultchannelpriority_constructor_args():
    sig = inspect.signature(uppaal_global_DefaultChannelPriority.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_global_channellist_is_not_abstract():
    assert not inspect.isabstract(uppaal_global_ChannelList)


def test_uppaal_global_channellist_constructor_exists():
    assert callable(uppaal_global_ChannelList.__init__)


def test_uppaal_global_channellist_constructor_args():
    sig = inspect.signature(uppaal_global_ChannelList.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_global_channelpriorityitem_is_not_abstract():
    assert not inspect.isabstract(uppaal_global_ChannelPriorityItem)


def test_uppaal_global_channelpriorityitem_constructor_exists():
    assert callable(uppaal_global_ChannelPriorityItem.__init__)


def test_uppaal_global_channelpriorityitem_constructor_args():
    sig = inspect.signature(uppaal_global_ChannelPriorityItem.__init__)
    params = list(sig.parameters.keys())



def test_global_channelpriorityitem_is_not_abstract():
    assert not inspect.isabstract(global_ChannelPriorityItem)


def test_global_channelpriorityitem_constructor_exists():
    assert callable(global_ChannelPriorityItem.__init__)


def test_global_channelpriorityitem_constructor_args():
    sig = inspect.signature(global_ChannelPriorityItem.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_global_channelpriority_is_not_abstract():
    assert not inspect.isabstract(uppaal_global_ChannelPriority)


def test_uppaal_global_channelpriority_constructor_exists():
    assert callable(uppaal_global_ChannelPriority.__init__)


def test_uppaal_global_channelpriority_constructor_args():
    sig = inspect.signature(uppaal_global_ChannelPriority.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_declarations_initializer_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_Initializer)


def test_uppaal_declarations_initializer_constructor_exists():
    assert callable(uppaal_declarations_Initializer.__init__)


def test_uppaal_declarations_initializer_constructor_args():
    sig = inspect.signature(uppaal_declarations_Initializer.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_declarations_parameter_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_Parameter)


def test_uppaal_declarations_parameter_constructor_exists():
    assert callable(uppaal_declarations_Parameter.__init__)


def test_uppaal_declarations_parameter_constructor_args():
    sig = inspect.signature(uppaal_declarations_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "callType" in params, "Missing parameter 'callType'"

def test_uppaal_declarations_parameter_has_callType():
    assert hasattr(uppaal_declarations_Parameter, "callType")
    descriptor = None
    for klass in uppaal_declarations_Parameter.__mro__:
        if "callType" in klass.__dict__:
            descriptor = klass.__dict__["callType"]
            break
    assert isinstance(descriptor, property)



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_declarations_variablecontainer_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_VariableContainer)


def test_uppaal_declarations_variablecontainer_constructor_exists():
    assert callable(uppaal_declarations_VariableContainer.__init__)


def test_uppaal_declarations_variablecontainer_constructor_args():
    sig = inspect.signature(uppaal_declarations_VariableContainer.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_declarations_index_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_Index)


def test_uppaal_declarations_index_constructor_exists():
    assert callable(uppaal_declarations_Index.__init__)


def test_uppaal_declarations_index_constructor_args():
    sig = inspect.signature(uppaal_declarations_Index.__init__)
    params = list(sig.parameters.keys())



def test_initializer_is_not_abstract():
    assert not inspect.isabstract(Initializer)


def test_initializer_constructor_exists():
    assert callable(Initializer.__init__)


def test_initializer_constructor_args():
    sig = inspect.signature(Initializer.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_declarations_arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_ArrayInitializer)


def test_uppaal_declarations_arrayinitializer_constructor_exists():
    assert callable(uppaal_declarations_ArrayInitializer.__init__)


def test_uppaal_declarations_arrayinitializer_constructor_args():
    sig = inspect.signature(uppaal_declarations_ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_declarations_expressioninitializer_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_ExpressionInitializer)


def test_uppaal_declarations_expressioninitializer_constructor_exists():
    assert callable(uppaal_declarations_ExpressionInitializer.__init__)


def test_uppaal_declarations_expressioninitializer_constructor_args():
    sig = inspect.signature(uppaal_declarations_ExpressionInitializer.__init__)
    params = list(sig.parameters.keys())



def test_variablecontainer_is_not_abstract():
    assert not inspect.isabstract(VariableContainer)


def test_variablecontainer_constructor_exists():
    assert callable(VariableContainer.__init__)


def test_variablecontainer_constructor_args():
    sig = inspect.signature(VariableContainer.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_templates_selection_is_not_abstract():
    assert not inspect.isabstract(uppaal_templates_Selection)


def test_uppaal_templates_selection_constructor_exists():
    assert callable(uppaal_templates_Selection.__init__)


def test_uppaal_templates_selection_constructor_args():
    sig = inspect.signature(uppaal_templates_Selection.__init__)
    params = list(sig.parameters.keys())



def test_declaredtype_is_not_abstract():
    assert not inspect.isabstract(DeclaredType)


def test_declaredtype_constructor_exists():
    assert callable(DeclaredType.__init__)


def test_declaredtype_constructor_args():
    sig = inspect.signature(DeclaredType.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_function_constructor_exists():
    assert callable(Function.__init__)


def test_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_declarations_clockvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_ClockVariableDeclaration)


def test_uppaal_declarations_clockvariabledeclaration_constructor_exists():
    assert callable(uppaal_declarations_ClockVariableDeclaration.__init__)


def test_uppaal_declarations_clockvariabledeclaration_constructor_args():
    sig = inspect.signature(uppaal_declarations_ClockVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_declarations_datavariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_DataVariableDeclaration)


def test_uppaal_declarations_datavariabledeclaration_constructor_exists():
    assert callable(uppaal_declarations_DataVariableDeclaration.__init__)


def test_uppaal_declarations_datavariabledeclaration_constructor_args():
    sig = inspect.signature(uppaal_declarations_DataVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "prefix" in params, "Missing parameter 'prefix'"

def test_uppaal_declarations_datavariabledeclaration_has_prefix():
    assert hasattr(uppaal_declarations_DataVariableDeclaration, "prefix")
    descriptor = None
    for klass in uppaal_declarations_DataVariableDeclaration.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_declarations_channelvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_ChannelVariableDeclaration)


def test_uppaal_declarations_channelvariabledeclaration_constructor_exists():
    assert callable(uppaal_declarations_ChannelVariableDeclaration.__init__)


def test_uppaal_declarations_channelvariabledeclaration_constructor_args():
    sig = inspect.signature(uppaal_declarations_ChannelVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "urgent" in params, "Missing parameter 'urgent'"
    assert "broadcast" in params, "Missing parameter 'broadcast'"

def test_uppaal_declarations_channelvariabledeclaration_has_urgent():
    assert hasattr(uppaal_declarations_ChannelVariableDeclaration, "urgent")
    descriptor = None
    for klass in uppaal_declarations_ChannelVariableDeclaration.__mro__:
        if "urgent" in klass.__dict__:
            descriptor = klass.__dict__["urgent"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_declarations_channelvariabledeclaration_has_broadcast():
    assert hasattr(uppaal_declarations_ChannelVariableDeclaration, "broadcast")
    descriptor = None
    for klass in uppaal_declarations_ChannelVariableDeclaration.__mro__:
        if "broadcast" in klass.__dict__:
            descriptor = klass.__dict__["broadcast"]
            break
    assert isinstance(descriptor, property)



def test_declarations_variablecontainer_is_not_abstract():
    assert not inspect.isabstract(declarations_VariableContainer)


def test_declarations_variablecontainer_constructor_exists():
    assert callable(declarations_VariableContainer.__init__)


def test_declarations_variablecontainer_constructor_args():
    sig = inspect.signature(declarations_VariableContainer.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_expressions_quantificationexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_QuantificationExpression)


def test_uppaal_expressions_quantificationexpression_constructor_exists():
    assert callable(uppaal_expressions_QuantificationExpression.__init__)


def test_uppaal_expressions_quantificationexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_QuantificationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "quantifier" in params, "Missing parameter 'quantifier'"

def test_uppaal_expressions_quantificationexpression_has_quantifier():
    assert hasattr(uppaal_expressions_QuantificationExpression, "quantifier")
    descriptor = None
    for klass in uppaal_expressions_QuantificationExpression.__mro__:
        if "quantifier" in klass.__dict__:
            descriptor = klass.__dict__["quantifier"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_statements_iteration_is_not_abstract():
    assert not inspect.isabstract(uppaal_statements_Iteration)


def test_uppaal_statements_iteration_constructor_exists():
    assert callable(uppaal_statements_Iteration.__init__)


def test_uppaal_statements_iteration_constructor_args():
    sig = inspect.signature(uppaal_statements_Iteration.__init__)
    params = list(sig.parameters.keys())



def test_declarations_declaration_is_not_abstract():
    assert not inspect.isabstract(declarations_Declaration)


def test_declarations_declaration_constructor_exists():
    assert callable(declarations_Declaration.__init__)


def test_declarations_declaration_constructor_args():
    sig = inspect.signature(declarations_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_declarations_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_VariableDeclaration)


def test_uppaal_declarations_variabledeclaration_constructor_exists():
    assert callable(uppaal_declarations_VariableDeclaration.__init__)


def test_uppaal_declarations_variabledeclaration_constructor_args():
    sig = inspect.signature(uppaal_declarations_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_declarations_declaration_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_Declaration)


def test_uppaal_declarations_declaration_constructor_exists():
    assert callable(uppaal_declarations_Declaration.__init__)


def test_uppaal_declarations_declaration_constructor_args():
    sig = inspect.signature(uppaal_declarations_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_system_progressmeasure_is_not_abstract():
    assert not inspect.isabstract(system_ProgressMeasure)


def test_system_progressmeasure_constructor_exists():
    assert callable(system_ProgressMeasure.__init__)


def test_system_progressmeasure_constructor_args():
    sig = inspect.signature(system_ProgressMeasure.__init__)
    params = list(sig.parameters.keys())



def test_system_system_is_not_abstract():
    assert not inspect.isabstract(system_System)


def test_system_system_constructor_exists():
    assert callable(system_System.__init__)


def test_system_system_constructor_args():
    sig = inspect.signature(system_System.__init__)
    params = list(sig.parameters.keys())



def test_global_channelpriority_is_not_abstract():
    assert not inspect.isabstract(global_ChannelPriority)


def test_global_channelpriority_constructor_exists():
    assert callable(global_ChannelPriority.__init__)


def test_global_channelpriority_constructor_args():
    sig = inspect.signature(global_ChannelPriority.__init__)
    params = list(sig.parameters.keys())



def test_declarations_is_not_abstract():
    assert not inspect.isabstract(Declarations)


def test_declarations_constructor_exists():
    assert callable(Declarations.__init__)


def test_declarations_constructor_args():
    sig = inspect.signature(Declarations.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_declarations_localdeclarations_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_LocalDeclarations)


def test_uppaal_declarations_localdeclarations_constructor_exists():
    assert callable(uppaal_declarations_LocalDeclarations.__init__)


def test_uppaal_declarations_localdeclarations_constructor_args():
    sig = inspect.signature(uppaal_declarations_LocalDeclarations.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_declarations_systemdeclarations_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_SystemDeclarations)


def test_uppaal_declarations_systemdeclarations_constructor_exists():
    assert callable(uppaal_declarations_SystemDeclarations.__init__)


def test_uppaal_declarations_systemdeclarations_constructor_args():
    sig = inspect.signature(uppaal_declarations_SystemDeclarations.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_declarations_globaldeclarations_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_GlobalDeclarations)


def test_uppaal_declarations_globaldeclarations_constructor_exists():
    assert callable(uppaal_declarations_GlobalDeclarations.__init__)


def test_uppaal_declarations_globaldeclarations_constructor_args():
    sig = inspect.signature(uppaal_declarations_GlobalDeclarations.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_declarations_functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_FunctionDeclaration)


def test_uppaal_declarations_functiondeclaration_constructor_exists():
    assert callable(uppaal_declarations_FunctionDeclaration.__init__)


def test_uppaal_declarations_functiondeclaration_constructor_args():
    sig = inspect.signature(uppaal_declarations_FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_system_templatedeclaration_is_not_abstract():
    assert not inspect.isabstract(uppaal_system_TemplateDeclaration)


def test_uppaal_system_templatedeclaration_constructor_exists():
    assert callable(uppaal_system_TemplateDeclaration.__init__)


def test_uppaal_system_templatedeclaration_constructor_args():
    sig = inspect.signature(uppaal_system_TemplateDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_declarations_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_TypeDeclaration)


def test_uppaal_declarations_typedeclaration_constructor_exists():
    assert callable(uppaal_declarations_TypeDeclaration.__init__)


def test_uppaal_declarations_typedeclaration_constructor_args():
    sig = inspect.signature(uppaal_declarations_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_declarations_declarations_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_Declarations)


def test_uppaal_declarations_declarations_constructor_exists():
    assert callable(uppaal_declarations_Declarations.__init__)


def test_uppaal_declarations_declarations_constructor_args():
    sig = inspect.signature(uppaal_declarations_Declarations.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_types_library_is_not_abstract():
    assert not inspect.isabstract(uppaal_types_Library)


def test_uppaal_types_library_constructor_exists():
    assert callable(uppaal_types_Library.__init__)


def test_uppaal_types_library_constructor_args():
    sig = inspect.signature(uppaal_types_Library.__init__)
    params = list(sig.parameters.keys())



def test_integerbounds_is_not_abstract():
    assert not inspect.isabstract(IntegerBounds)


def test_integerbounds_constructor_exists():
    assert callable(IntegerBounds.__init__)


def test_integerbounds_constructor_args():
    sig = inspect.signature(IntegerBounds.__init__)
    params = list(sig.parameters.keys())



def test_datavariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(DataVariableDeclaration)


def test_datavariabledeclaration_constructor_exists():
    assert callable(DataVariableDeclaration.__init__)


def test_datavariabledeclaration_constructor_args():
    sig = inspect.signature(DataVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_expressions_conditionexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_ConditionExpression)


def test_uppaal_expressions_conditionexpression_constructor_exists():
    assert callable(uppaal_expressions_ConditionExpression.__init__)


def test_uppaal_expressions_conditionexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_ConditionExpression.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_expressions_negationexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_NegationExpression)


def test_uppaal_expressions_negationexpression_constructor_exists():
    assert callable(uppaal_expressions_NegationExpression.__init__)


def test_uppaal_expressions_negationexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_NegationExpression.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_expressions_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_BinaryExpression)


def test_uppaal_expressions_binaryexpression_constructor_exists():
    assert callable(uppaal_expressions_BinaryExpression.__init__)


def test_uppaal_expressions_binaryexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_expressions_scopedidentifierexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_ScopedIdentifierExpression)


def test_uppaal_expressions_scopedidentifierexpression_constructor_exists():
    assert callable(uppaal_expressions_ScopedIdentifierExpression.__init__)


def test_uppaal_expressions_scopedidentifierexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_ScopedIdentifierExpression.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_expressions_literalexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_LiteralExpression)


def test_uppaal_expressions_literalexpression_constructor_exists():
    assert callable(uppaal_expressions_LiteralExpression.__init__)


def test_uppaal_expressions_literalexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_LiteralExpression.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_uppaal_expressions_literalexpression_has_text():
    assert hasattr(uppaal_expressions_LiteralExpression, "text")
    descriptor = None
    for klass in uppaal_expressions_LiteralExpression.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_expressions_incrementdecrementexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_IncrementDecrementExpression)


def test_uppaal_expressions_incrementdecrementexpression_constructor_exists():
    assert callable(uppaal_expressions_IncrementDecrementExpression.__init__)


def test_uppaal_expressions_incrementdecrementexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_IncrementDecrementExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"
    assert "position" in params, "Missing parameter 'position'"

def test_uppaal_expressions_incrementdecrementexpression_has_operator():
    assert hasattr(uppaal_expressions_IncrementDecrementExpression, "operator")
    descriptor = None
    for klass in uppaal_expressions_IncrementDecrementExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_expressions_incrementdecrementexpression_has_position():
    assert hasattr(uppaal_expressions_IncrementDecrementExpression, "position")
    descriptor = None
    for klass in uppaal_expressions_IncrementDecrementExpression.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_expressions_minusexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_MinusExpression)


def test_uppaal_expressions_minusexpression_constructor_exists():
    assert callable(uppaal_expressions_MinusExpression.__init__)


def test_uppaal_expressions_minusexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_MinusExpression.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_expressions_identifierexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_IdentifierExpression)


def test_uppaal_expressions_identifierexpression_constructor_exists():
    assert callable(uppaal_expressions_IdentifierExpression.__init__)


def test_uppaal_expressions_identifierexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_IdentifierExpression.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_expressions_plusexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_PlusExpression)


def test_uppaal_expressions_plusexpression_constructor_exists():
    assert callable(uppaal_expressions_PlusExpression.__init__)


def test_uppaal_expressions_plusexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_PlusExpression.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_expressions_functioncallexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_FunctionCallExpression)


def test_uppaal_expressions_functioncallexpression_constructor_exists():
    assert callable(uppaal_expressions_FunctionCallExpression.__init__)


def test_uppaal_expressions_functioncallexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_FunctionCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_types_typedefinition_is_not_abstract():
    assert not inspect.isabstract(uppaal_types_TypeDefinition)


def test_uppaal_types_typedefinition_constructor_exists():
    assert callable(uppaal_types_TypeDefinition.__init__)


def test_uppaal_types_typedefinition_constructor_args():
    sig = inspect.signature(uppaal_types_TypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "baseType" in params, "Missing parameter 'baseType'"

def test_uppaal_types_typedefinition_has_baseType():
    assert hasattr(uppaal_types_TypeDefinition, "baseType")
    descriptor = None
    for klass in uppaal_types_TypeDefinition.__mro__:
        if "baseType" in klass.__dict__:
            descriptor = klass.__dict__["baseType"]
            break
    assert isinstance(descriptor, property)



def test_typedefinition_is_not_abstract():
    assert not inspect.isabstract(TypeDefinition)


def test_typedefinition_constructor_exists():
    assert callable(TypeDefinition.__init__)


def test_typedefinition_constructor_args():
    sig = inspect.signature(TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_types_typespecification_is_not_abstract():
    assert not inspect.isabstract(uppaal_types_TypeSpecification)


def test_uppaal_types_typespecification_constructor_exists():
    assert callable(uppaal_types_TypeSpecification.__init__)


def test_uppaal_types_typespecification_constructor_args():
    sig = inspect.signature(uppaal_types_TypeSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_types_typereference_is_not_abstract():
    assert not inspect.isabstract(uppaal_types_TypeReference)


def test_uppaal_types_typereference_constructor_exists():
    assert callable(uppaal_types_TypeReference.__init__)


def test_uppaal_types_typereference_constructor_args():
    sig = inspect.signature(uppaal_types_TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_types_integerbounds_is_not_abstract():
    assert not inspect.isabstract(uppaal_types_IntegerBounds)


def test_uppaal_types_integerbounds_constructor_exists():
    assert callable(uppaal_types_IntegerBounds.__init__)


def test_uppaal_types_integerbounds_constructor_args():
    sig = inspect.signature(uppaal_types_IntegerBounds.__init__)
    params = list(sig.parameters.keys())



def test_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(TypeDeclaration)


def test_typedeclaration_constructor_exists():
    assert callable(TypeDeclaration.__init__)


def test_typedeclaration_constructor_args():
    sig = inspect.signature(TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_types_declaredtype_is_not_abstract():
    assert not inspect.isabstract(uppaal_types_DeclaredType)


def test_uppaal_types_declaredtype_constructor_exists():
    assert callable(uppaal_types_DeclaredType.__init__)


def test_uppaal_types_declaredtype_constructor_args():
    sig = inspect.signature(uppaal_types_DeclaredType.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_types_predefinedtype_is_not_abstract():
    assert not inspect.isabstract(uppaal_types_PredefinedType)


def test_uppaal_types_predefinedtype_constructor_exists():
    assert callable(uppaal_types_PredefinedType.__init__)


def test_uppaal_types_predefinedtype_constructor_args():
    sig = inspect.signature(uppaal_types_PredefinedType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_uppaal_types_predefinedtype_has_type():
    assert hasattr(uppaal_types_PredefinedType, "type")
    descriptor = None
    for klass in uppaal_types_PredefinedType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_typespecification_is_not_abstract():
    assert not inspect.isabstract(TypeSpecification)


def test_typespecification_constructor_exists():
    assert callable(TypeSpecification.__init__)


def test_typespecification_constructor_args():
    sig = inspect.signature(TypeSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_types_rangetypespecification_is_not_abstract():
    assert not inspect.isabstract(uppaal_types_RangeTypeSpecification)


def test_uppaal_types_rangetypespecification_constructor_exists():
    assert callable(uppaal_types_RangeTypeSpecification.__init__)


def test_uppaal_types_rangetypespecification_constructor_args():
    sig = inspect.signature(uppaal_types_RangeTypeSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_types_structtypespecification_is_not_abstract():
    assert not inspect.isabstract(uppaal_types_StructTypeSpecification)


def test_uppaal_types_structtypespecification_constructor_exists():
    assert callable(uppaal_types_StructTypeSpecification.__init__)


def test_uppaal_types_structtypespecification_constructor_args():
    sig = inspect.signature(uppaal_types_StructTypeSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_types_scalartypespecification_is_not_abstract():
    assert not inspect.isabstract(uppaal_types_ScalarTypeSpecification)


def test_uppaal_types_scalartypespecification_constructor_exists():
    assert callable(uppaal_types_ScalarTypeSpecification.__init__)


def test_uppaal_types_scalartypespecification_constructor_args():
    sig = inspect.signature(uppaal_types_ScalarTypeSpecification.__init__)
    params = list(sig.parameters.keys())



def test_index_is_not_abstract():
    assert not inspect.isabstract(Index)


def test_index_constructor_exists():
    assert callable(Index.__init__)


def test_index_constructor_args():
    sig = inspect.signature(Index.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_declarations_valueindex_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_ValueIndex)


def test_uppaal_declarations_valueindex_constructor_exists():
    assert callable(uppaal_declarations_ValueIndex.__init__)


def test_uppaal_declarations_valueindex_constructor_args():
    sig = inspect.signature(uppaal_declarations_ValueIndex.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_declarations_typeindex_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_TypeIndex)


def test_uppaal_declarations_typeindex_constructor_exists():
    assert callable(uppaal_declarations_TypeIndex.__init__)


def test_uppaal_declarations_typeindex_constructor_args():
    sig = inspect.signature(uppaal_declarations_TypeIndex.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_declarations_function_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_Function)


def test_uppaal_declarations_function_constructor_exists():
    assert callable(uppaal_declarations_Function.__init__)


def test_uppaal_declarations_function_constructor_args():
    sig = inspect.signature(uppaal_declarations_Function.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_declarations_variable_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_Variable)


def test_uppaal_declarations_variable_constructor_exists():
    assert callable(uppaal_declarations_Variable.__init__)


def test_uppaal_declarations_variable_constructor_args():
    sig = inspect.signature(uppaal_declarations_Variable.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_types_type_is_not_abstract():
    assert not inspect.isabstract(uppaal_types_Type)


def test_uppaal_types_type_constructor_exists():
    assert callable(uppaal_types_Type.__init__)


def test_uppaal_types_type_constructor_args():
    sig = inspect.signature(uppaal_types_Type.__init__)
    params = list(sig.parameters.keys())
    assert "baseType" in params, "Missing parameter 'baseType'"

def test_uppaal_types_type_has_baseType():
    assert hasattr(uppaal_types_Type, "baseType")
    descriptor = None
    for klass in uppaal_types_Type.__mro__:
        if "baseType" in klass.__dict__:
            descriptor = klass.__dict__["baseType"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_core_commentableelement_is_not_abstract():
    assert not inspect.isabstract(uppaal_core_CommentableElement)


def test_uppaal_core_commentableelement_constructor_exists():
    assert callable(uppaal_core_CommentableElement.__init__)


def test_uppaal_core_commentableelement_constructor_args():
    sig = inspect.signature(uppaal_core_CommentableElement.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_uppaal_core_commentableelement_has_comment():
    assert hasattr(uppaal_core_CommentableElement, "comment")
    descriptor = None
    for klass in uppaal_core_CommentableElement.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_predefinedtype_is_not_abstract():
    assert not inspect.isabstract(PredefinedType)


def test_predefinedtype_constructor_exists():
    assert callable(PredefinedType.__init__)


def test_predefinedtype_constructor_args():
    sig = inspect.signature(PredefinedType.__init__)
    params = list(sig.parameters.keys())



def test_systemdeclarations_is_not_abstract():
    assert not inspect.isabstract(SystemDeclarations)


def test_systemdeclarations_constructor_exists():
    assert callable(SystemDeclarations.__init__)


def test_systemdeclarations_constructor_args():
    sig = inspect.signature(SystemDeclarations.__init__)
    params = list(sig.parameters.keys())



def test_template_is_not_abstract():
    assert not inspect.isabstract(Template)


def test_template_constructor_exists():
    assert callable(Template.__init__)


def test_template_constructor_args():
    sig = inspect.signature(Template.__init__)
    params = list(sig.parameters.keys())



def test_globaldeclarations_is_not_abstract():
    assert not inspect.isabstract(GlobalDeclarations)


def test_globaldeclarations_constructor_exists():
    assert callable(GlobalDeclarations.__init__)


def test_globaldeclarations_constructor_args():
    sig = inspect.signature(GlobalDeclarations.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_core_namedelement_is_not_abstract():
    assert not inspect.isabstract(uppaal_core_NamedElement)


def test_uppaal_core_namedelement_constructor_exists():
    assert callable(uppaal_core_NamedElement.__init__)


def test_uppaal_core_namedelement_constructor_args():
    sig = inspect.signature(uppaal_core_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uppaal_core_namedelement_has_name():
    assert hasattr(uppaal_core_NamedElement, "name")
    descriptor = None
    for klass in uppaal_core_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_core_commentableelement_is_not_abstract():
    assert not inspect.isabstract(core_CommentableElement)


def test_core_commentableelement_constructor_exists():
    assert callable(core_CommentableElement.__init__)


def test_core_commentableelement_constructor_args():
    sig = inspect.signature(core_CommentableElement.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_templates_edge_is_not_abstract():
    assert not inspect.isabstract(uppaal_templates_Edge)


def test_uppaal_templates_edge_constructor_exists():
    assert callable(uppaal_templates_Edge.__init__)


def test_uppaal_templates_edge_constructor_args():
    sig = inspect.signature(uppaal_templates_Edge.__init__)
    params = list(sig.parameters.keys())



def test_core_namedelement_is_not_abstract():
    assert not inspect.isabstract(core_NamedElement)


def test_core_namedelement_constructor_exists():
    assert callable(core_NamedElement.__init__)


def test_core_namedelement_constructor_args():
    sig = inspect.signature(core_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_templates_abstracttemplate_is_not_abstract():
    assert not inspect.isabstract(uppaal_templates_AbstractTemplate)


def test_uppaal_templates_abstracttemplate_constructor_exists():
    assert callable(uppaal_templates_AbstractTemplate.__init__)


def test_uppaal_templates_abstracttemplate_constructor_args():
    sig = inspect.signature(uppaal_templates_AbstractTemplate.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_templates_location_is_not_abstract():
    assert not inspect.isabstract(uppaal_templates_Location)


def test_uppaal_templates_location_constructor_exists():
    assert callable(uppaal_templates_Location.__init__)


def test_uppaal_templates_location_constructor_args():
    sig = inspect.signature(uppaal_templates_Location.__init__)
    params = list(sig.parameters.keys())
    assert "locationTimeKind" in params, "Missing parameter 'locationTimeKind'"

def test_uppaal_templates_location_has_locationTimeKind():
    assert hasattr(uppaal_templates_Location, "locationTimeKind")
    descriptor = None
    for klass in uppaal_templates_Location.__mro__:
        if "locationTimeKind" in klass.__dict__:
            descriptor = klass.__dict__["locationTimeKind"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_nta_is_not_abstract():
    assert not inspect.isabstract(uppaal_NTA)


def test_uppaal_nta_constructor_exists():
    assert callable(uppaal_NTA.__init__)


def test_uppaal_nta_constructor_args():
    sig = inspect.signature(uppaal_NTA.__init__)
    params = list(sig.parameters.keys())

def test_logicaloperator_exists():
    # Check that the Enumeration exists
    assert LogicalOperator is not None

def test_logicaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicalOperator]
    expected_literals = [
        "AND",
        "OR",
        "IMPLY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LogicalOperator"

def test_locationkind_exists():
    # Check that the Enumeration exists
    assert LocationKind is not None

def test_locationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LocationKind]
    expected_literals = [
        "NORMAL",
        "URGENT",
        "COMMITED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LocationKind"

def test_compareoperator_exists():
    # Check that the Enumeration exists
    assert CompareOperator is not None

def test_compareoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CompareOperator]
    expected_literals = [
        "EQUAL",
        "GREATER_OR_EQUAL",
        "LESS_OR_EQUAL",
        "LESS",
        "GREATER",
        "UNEQUAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CompareOperator"

def test_incrementdecrementoperator_exists():
    # Check that the Enumeration exists
    assert IncrementDecrementOperator is not None

def test_incrementdecrementoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IncrementDecrementOperator]
    expected_literals = [
        "INCREMENT",
        "DECREMENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IncrementDecrementOperator"

def test_incrementdecrementposition_exists():
    # Check that the Enumeration exists
    assert IncrementDecrementPosition is not None

def test_incrementdecrementposition_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IncrementDecrementPosition]
    expected_literals = [
        "POST",
        "PRE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IncrementDecrementPosition"

def test_datavariableprefix_exists():
    # Check that the Enumeration exists
    assert DataVariablePrefix is not None

def test_datavariableprefix_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataVariablePrefix]
    expected_literals = [
        "NONE",
        "CONST",
        "META",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataVariablePrefix"

def test_bitshiftoperator_exists():
    # Check that the Enumeration exists
    assert BitShiftOperator is not None

def test_bitshiftoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BitShiftOperator]
    expected_literals = [
        "RIGHT",
        "LEFT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BitShiftOperator"

def test_minmaxoperator_exists():
    # Check that the Enumeration exists
    assert MinMaxOperator is not None

def test_minmaxoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MinMaxOperator]
    expected_literals = [
        "MIN",
        "MAX",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MinMaxOperator"

def test_bitwiseoperator_exists():
    # Check that the Enumeration exists
    assert BitwiseOperator is not None

def test_bitwiseoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BitwiseOperator]
    expected_literals = [
        "XOR",
        "OR",
        "AND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BitwiseOperator"

def test_calltype_exists():
    # Check that the Enumeration exists
    assert CallType is not None

def test_calltype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CallType]
    expected_literals = [
        "CALL_BY_VALUE",
        "CALL_BY_REFERENCE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CallType"

def test_arithmeticoperator_exists():
    # Check that the Enumeration exists
    assert ArithmeticOperator is not None

def test_arithmeticoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArithmeticOperator]
    expected_literals = [
        "DIVIDE",
        "ADD",
        "SUBTRACT",
        "MULTIPLICATE",
        "MODULO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArithmeticOperator"

def test_assignmentoperator_exists():
    # Check that the Enumeration exists
    assert AssignmentOperator is not None

def test_assignmentoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentOperator]
    expected_literals = [
        "BIT_LEFT_EQUAL",
        "BIT_AND_EQUAL",
        "DIVIDE_EQUAL",
        "EQUAL",
        "BIT_OR_EQUAL",
        "BIT_XOR_EQUAL",
        "TIMES_EQUAL",
        "MODULO_EQUAL",
        "BIT_RIGHT_EQUAL",
        "MINUS_EQUAL",
        "PLUS_EQUAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentOperator"

def test_quantifier_exists():
    # Check that the Enumeration exists
    assert Quantifier is not None

def test_quantifier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Quantifier]
    expected_literals = [
        "UNIVERSAL",
        "EXISTENTIAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Quantifier"

def test_synchronizationkind_exists():
    # Check that the Enumeration exists
    assert SynchronizationKind is not None

def test_synchronizationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SynchronizationKind]
    expected_literals = [
        "SEND",
        "RECEIVE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SynchronizationKind"

def test_colorkind_exists():
    # Check that the Enumeration exists
    assert ColorKind is not None

def test_colorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ColorKind]
    expected_literals = [
        "BLACK",
        "PINK",
        "YELLOW",
        "GREEN",
        "BLUE",
        "LIGHTGREY",
        "SELF_DEFINED",
        "ORANGE",
        "RED",
        "CYAN",
        "DEFAULT",
        "DARKGREY",
        "WHITE",
        "MAGENTA",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ColorKind"

def test_builtintype_exists():
    # Check that the Enumeration exists
    assert BuiltInType is not None

def test_builtintype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BuiltInType]
    expected_literals = [
        "CHAN",
        "INT",
        "BOOL",
        "VOID",
        "CLOCK",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BuiltInType"


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
uppaal_visuals_Point_strategy = st.builds(
    uppaal_visuals_Point,
    y=
        st.integers(),
    x=
        st.integers()
)
uppaal_visuals_LinearElement_strategy = st.builds(
    uppaal_visuals_LinearElement,
)
Point_strategy = st.builds(
    Point,
)
uppaal_visuals_PlanarElement_strategy = st.builds(
    uppaal_visuals_PlanarElement,
)
uppaal_visuals_ColoredElement_strategy = st.builds(
    uppaal_visuals_ColoredElement,
    colorCode=
        safe_text,
    color=
        safe_text
)
expressions_Expression_strategy = st.builds(
    expressions_Expression,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
uppaal_expressions_ArithmeticExpression_strategy = st.builds(
    uppaal_expressions_ArithmeticExpression,
    operator=
        safe_text
)
uppaal_expressions_MinMaxExpression_strategy = st.builds(
    uppaal_expressions_MinMaxExpression,
    operator=
        safe_text
)
uppaal_expressions_LogicalExpression_strategy = st.builds(
    uppaal_expressions_LogicalExpression,
    operator=
        safe_text
)
uppaal_expressions_BitShiftExpression_strategy = st.builds(
    uppaal_expressions_BitShiftExpression,
    operator=
        safe_text
)
uppaal_expressions_BitwiseExpression_strategy = st.builds(
    uppaal_expressions_BitwiseExpression,
    operator=
        safe_text
)
uppaal_expressions_CompareExpression_strategy = st.builds(
    uppaal_expressions_CompareExpression,
    operator=
        safe_text
)
uppaal_expressions_AssignmentExpression_strategy = st.builds(
    uppaal_expressions_AssignmentExpression,
    operator=
        safe_text
)
uppaal_expressions_Expression_strategy = st.builds(
    uppaal_expressions_Expression,
)
statements_Statement_strategy = st.builds(
    statements_Statement,
)
Statement_strategy = st.builds(
    Statement,
)
uppaal_statements_WhileLoop_strategy = st.builds(
    uppaal_statements_WhileLoop,
)
uppaal_statements_EmptyStatement_strategy = st.builds(
    uppaal_statements_EmptyStatement,
)
uppaal_statements_ReturnStatement_strategy = st.builds(
    uppaal_statements_ReturnStatement,
)
uppaal_statements_ForLoop_strategy = st.builds(
    uppaal_statements_ForLoop,
)
uppaal_statements_ExpressionStatement_strategy = st.builds(
    uppaal_statements_ExpressionStatement,
)
uppaal_statements_DoWhileLoop_strategy = st.builds(
    uppaal_statements_DoWhileLoop,
)
uppaal_statements_IfStatement_strategy = st.builds(
    uppaal_statements_IfStatement,
)
uppaal_statements_Block_strategy = st.builds(
    uppaal_statements_Block,
)
uppaal_statements_Statement_strategy = st.builds(
    uppaal_statements_Statement,
)
uppaal_templates_Synchronization_strategy = st.builds(
    uppaal_templates_Synchronization,
    kind=
        safe_text
)
Selection_strategy = st.builds(
    Selection,
)
Synchronization_strategy = st.builds(
    Synchronization,
)
visuals_ColoredElement_strategy = st.builds(
    visuals_ColoredElement,
)
visuals_PlanarElement_strategy = st.builds(
    visuals_PlanarElement,
)
visuals_LinearElement_strategy = st.builds(
    visuals_LinearElement,
)
system_TemplateDeclaration_strategy = st.builds(
    system_TemplateDeclaration,
)
Edge_strategy = st.builds(
    Edge,
)
Location_strategy = st.builds(
    Location,
)
LocalDeclarations_strategy = st.builds(
    LocalDeclarations,
)
uppaal_system_ProgressMeasure_strategy = st.builds(
    uppaal_system_ProgressMeasure,
)
AbstractTemplate_strategy = st.builds(
    AbstractTemplate,
)
uppaal_templates_RedefinedTemplate_strategy = st.builds(
    uppaal_templates_RedefinedTemplate,
)
uppaal_templates_Template_strategy = st.builds(
    uppaal_templates_Template,
)
uppaal_system_InstantiationList_strategy = st.builds(
    uppaal_system_InstantiationList,
)
system_InstantiationList_strategy = st.builds(
    system_InstantiationList,
)
uppaal_system_System_strategy = st.builds(
    uppaal_system_System,
)
RedefinedTemplate_strategy = st.builds(
    RedefinedTemplate,
)
IdentifierExpression_strategy = st.builds(
    IdentifierExpression,
)
ChannelPriorityItem_strategy = st.builds(
    ChannelPriorityItem,
)
uppaal_global_DefaultChannelPriority_strategy = st.builds(
    uppaal_global_DefaultChannelPriority,
)
uppaal_global_ChannelList_strategy = st.builds(
    uppaal_global_ChannelList,
)
uppaal_global_ChannelPriorityItem_strategy = st.builds(
    uppaal_global_ChannelPriorityItem,
)
global_ChannelPriorityItem_strategy = st.builds(
    global_ChannelPriorityItem,
)
uppaal_global_ChannelPriority_strategy = st.builds(
    uppaal_global_ChannelPriority,
)
uppaal_declarations_Initializer_strategy = st.builds(
    uppaal_declarations_Initializer,
)
uppaal_declarations_Parameter_strategy = st.builds(
    uppaal_declarations_Parameter,
    callType=
        safe_text
)
Variable_strategy = st.builds(
    Variable,
)
uppaal_declarations_VariableContainer_strategy = st.builds(
    uppaal_declarations_VariableContainer,
)
uppaal_declarations_Index_strategy = st.builds(
    uppaal_declarations_Index,
)
Initializer_strategy = st.builds(
    Initializer,
)
uppaal_declarations_ArrayInitializer_strategy = st.builds(
    uppaal_declarations_ArrayInitializer,
)
uppaal_declarations_ExpressionInitializer_strategy = st.builds(
    uppaal_declarations_ExpressionInitializer,
)
VariableContainer_strategy = st.builds(
    VariableContainer,
)
uppaal_templates_Selection_strategy = st.builds(
    uppaal_templates_Selection,
)
DeclaredType_strategy = st.builds(
    DeclaredType,
)
Parameter_strategy = st.builds(
    Parameter,
)
Block_strategy = st.builds(
    Block,
)
Function_strategy = st.builds(
    Function,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
uppaal_declarations_ClockVariableDeclaration_strategy = st.builds(
    uppaal_declarations_ClockVariableDeclaration,
)
uppaal_declarations_DataVariableDeclaration_strategy = st.builds(
    uppaal_declarations_DataVariableDeclaration,
    prefix=
        safe_text
)
uppaal_declarations_ChannelVariableDeclaration_strategy = st.builds(
    uppaal_declarations_ChannelVariableDeclaration,
    urgent=
        st.booleans(),
    broadcast=
        st.booleans()
)
declarations_VariableContainer_strategy = st.builds(
    declarations_VariableContainer,
)
uppaal_expressions_QuantificationExpression_strategy = st.builds(
    uppaal_expressions_QuantificationExpression,
    quantifier=
        safe_text
)
uppaal_statements_Iteration_strategy = st.builds(
    uppaal_statements_Iteration,
)
declarations_Declaration_strategy = st.builds(
    declarations_Declaration,
)
uppaal_declarations_VariableDeclaration_strategy = st.builds(
    uppaal_declarations_VariableDeclaration,
)
uppaal_declarations_Declaration_strategy = st.builds(
    uppaal_declarations_Declaration,
)
system_ProgressMeasure_strategy = st.builds(
    system_ProgressMeasure,
)
system_System_strategy = st.builds(
    system_System,
)
global_ChannelPriority_strategy = st.builds(
    global_ChannelPriority,
)
Declarations_strategy = st.builds(
    Declarations,
)
uppaal_declarations_LocalDeclarations_strategy = st.builds(
    uppaal_declarations_LocalDeclarations,
)
uppaal_declarations_SystemDeclarations_strategy = st.builds(
    uppaal_declarations_SystemDeclarations,
)
uppaal_declarations_GlobalDeclarations_strategy = st.builds(
    uppaal_declarations_GlobalDeclarations,
)
Declaration_strategy = st.builds(
    Declaration,
)
uppaal_declarations_FunctionDeclaration_strategy = st.builds(
    uppaal_declarations_FunctionDeclaration,
)
uppaal_system_TemplateDeclaration_strategy = st.builds(
    uppaal_system_TemplateDeclaration,
)
uppaal_declarations_TypeDeclaration_strategy = st.builds(
    uppaal_declarations_TypeDeclaration,
)
uppaal_declarations_Declarations_strategy = st.builds(
    uppaal_declarations_Declarations,
)
uppaal_types_Library_strategy = st.builds(
    uppaal_types_Library,
)
IntegerBounds_strategy = st.builds(
    IntegerBounds,
)
DataVariableDeclaration_strategy = st.builds(
    DataVariableDeclaration,
)
Expression_strategy = st.builds(
    Expression,
)
uppaal_expressions_ConditionExpression_strategy = st.builds(
    uppaal_expressions_ConditionExpression,
)
uppaal_expressions_NegationExpression_strategy = st.builds(
    uppaal_expressions_NegationExpression,
)
uppaal_expressions_BinaryExpression_strategy = st.builds(
    uppaal_expressions_BinaryExpression,
)
uppaal_expressions_ScopedIdentifierExpression_strategy = st.builds(
    uppaal_expressions_ScopedIdentifierExpression,
)
uppaal_expressions_LiteralExpression_strategy = st.builds(
    uppaal_expressions_LiteralExpression,
    text=
        safe_text
)
uppaal_expressions_IncrementDecrementExpression_strategy = st.builds(
    uppaal_expressions_IncrementDecrementExpression,
    operator=
        safe_text,
    position=
        safe_text
)
uppaal_expressions_MinusExpression_strategy = st.builds(
    uppaal_expressions_MinusExpression,
)
uppaal_expressions_IdentifierExpression_strategy = st.builds(
    uppaal_expressions_IdentifierExpression,
)
uppaal_expressions_PlusExpression_strategy = st.builds(
    uppaal_expressions_PlusExpression,
)
uppaal_expressions_FunctionCallExpression_strategy = st.builds(
    uppaal_expressions_FunctionCallExpression,
)
uppaal_types_TypeDefinition_strategy = st.builds(
    uppaal_types_TypeDefinition,
    baseType=
        safe_text
)
TypeDefinition_strategy = st.builds(
    TypeDefinition,
)
uppaal_types_TypeSpecification_strategy = st.builds(
    uppaal_types_TypeSpecification,
)
uppaal_types_TypeReference_strategy = st.builds(
    uppaal_types_TypeReference,
)
uppaal_types_IntegerBounds_strategy = st.builds(
    uppaal_types_IntegerBounds,
)
TypeDeclaration_strategy = st.builds(
    TypeDeclaration,
)
Type_strategy = st.builds(
    Type,
)
uppaal_types_DeclaredType_strategy = st.builds(
    uppaal_types_DeclaredType,
)
uppaal_types_PredefinedType_strategy = st.builds(
    uppaal_types_PredefinedType,
    type=
        safe_text
)
TypeSpecification_strategy = st.builds(
    TypeSpecification,
)
uppaal_types_RangeTypeSpecification_strategy = st.builds(
    uppaal_types_RangeTypeSpecification,
)
uppaal_types_StructTypeSpecification_strategy = st.builds(
    uppaal_types_StructTypeSpecification,
)
uppaal_types_ScalarTypeSpecification_strategy = st.builds(
    uppaal_types_ScalarTypeSpecification,
)
Index_strategy = st.builds(
    Index,
)
uppaal_declarations_ValueIndex_strategy = st.builds(
    uppaal_declarations_ValueIndex,
)
uppaal_declarations_TypeIndex_strategy = st.builds(
    uppaal_declarations_TypeIndex,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
uppaal_declarations_Function_strategy = st.builds(
    uppaal_declarations_Function,
)
uppaal_declarations_Variable_strategy = st.builds(
    uppaal_declarations_Variable,
)
uppaal_types_Type_strategy = st.builds(
    uppaal_types_Type,
    baseType=
        safe_text
)
uppaal_core_CommentableElement_strategy = st.builds(
    uppaal_core_CommentableElement,
    comment=
        safe_text
)
PredefinedType_strategy = st.builds(
    PredefinedType,
)
SystemDeclarations_strategy = st.builds(
    SystemDeclarations,
)
Template_strategy = st.builds(
    Template,
)
GlobalDeclarations_strategy = st.builds(
    GlobalDeclarations,
)
uppaal_core_NamedElement_strategy = st.builds(
    uppaal_core_NamedElement,
    name=
        safe_text
)
core_CommentableElement_strategy = st.builds(
    core_CommentableElement,
)
uppaal_templates_Edge_strategy = st.builds(
    uppaal_templates_Edge,
)
core_NamedElement_strategy = st.builds(
    core_NamedElement,
)
uppaal_templates_AbstractTemplate_strategy = st.builds(
    uppaal_templates_AbstractTemplate,
)
uppaal_templates_Location_strategy = st.builds(
    uppaal_templates_Location,
    locationTimeKind=
        safe_text
)
uppaal_NTA_strategy = st.builds(
    uppaal_NTA,
)

@given(instance=uppaal_visuals_Point_strategy)
@settings(max_examples=50)
def test_uppaal_visuals_point_instantiation(instance):
    assert isinstance(instance, uppaal_visuals_Point)



@given(instance=uppaal_visuals_Point_strategy)
def test_uppaal_visuals_point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=uppaal_visuals_Point_strategy)
def test_uppaal_visuals_point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=uppaal_visuals_LinearElement_strategy)
@settings(max_examples=50)
def test_uppaal_visuals_linearelement_instantiation(instance):
    assert isinstance(instance, uppaal_visuals_LinearElement)

@given(instance=Point_strategy)
@settings(max_examples=50)
def test_point_instantiation(instance):
    assert isinstance(instance, Point)

@given(instance=uppaal_visuals_PlanarElement_strategy)
@settings(max_examples=50)
def test_uppaal_visuals_planarelement_instantiation(instance):
    assert isinstance(instance, uppaal_visuals_PlanarElement)

@given(instance=uppaal_visuals_ColoredElement_strategy)
@settings(max_examples=50)
def test_uppaal_visuals_coloredelement_instantiation(instance):
    assert isinstance(instance, uppaal_visuals_ColoredElement)



@given(instance=uppaal_visuals_ColoredElement_strategy)
def test_uppaal_visuals_coloredelement_colorCode_setter(instance):
    original = instance.colorCode
    instance.colorCode = original
    assert instance.colorCode == original



@given(instance=uppaal_visuals_ColoredElement_strategy)
def test_uppaal_visuals_coloredelement_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=expressions_Expression_strategy)
@settings(max_examples=50)
def test_expressions_expression_instantiation(instance):
    assert isinstance(instance, expressions_Expression)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=uppaal_expressions_ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_uppaal_expressions_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_ArithmeticExpression)



@given(instance=uppaal_expressions_ArithmeticExpression_strategy)
def test_uppaal_expressions_arithmeticexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=uppaal_expressions_MinMaxExpression_strategy)
@settings(max_examples=50)
def test_uppaal_expressions_minmaxexpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_MinMaxExpression)



@given(instance=uppaal_expressions_MinMaxExpression_strategy)
def test_uppaal_expressions_minmaxexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=uppaal_expressions_LogicalExpression_strategy)
@settings(max_examples=50)
def test_uppaal_expressions_logicalexpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_LogicalExpression)



@given(instance=uppaal_expressions_LogicalExpression_strategy)
def test_uppaal_expressions_logicalexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=uppaal_expressions_BitShiftExpression_strategy)
@settings(max_examples=50)
def test_uppaal_expressions_bitshiftexpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_BitShiftExpression)



@given(instance=uppaal_expressions_BitShiftExpression_strategy)
def test_uppaal_expressions_bitshiftexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=uppaal_expressions_BitwiseExpression_strategy)
@settings(max_examples=50)
def test_uppaal_expressions_bitwiseexpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_BitwiseExpression)



@given(instance=uppaal_expressions_BitwiseExpression_strategy)
def test_uppaal_expressions_bitwiseexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=uppaal_expressions_CompareExpression_strategy)
@settings(max_examples=50)
def test_uppaal_expressions_compareexpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_CompareExpression)



@given(instance=uppaal_expressions_CompareExpression_strategy)
def test_uppaal_expressions_compareexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=uppaal_expressions_AssignmentExpression_strategy)
@settings(max_examples=50)
def test_uppaal_expressions_assignmentexpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_AssignmentExpression)



@given(instance=uppaal_expressions_AssignmentExpression_strategy)
def test_uppaal_expressions_assignmentexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=uppaal_expressions_Expression_strategy)
@settings(max_examples=50)
def test_uppaal_expressions_expression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_Expression)

@given(instance=statements_Statement_strategy)
@settings(max_examples=50)
def test_statements_statement_instantiation(instance):
    assert isinstance(instance, statements_Statement)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=uppaal_statements_WhileLoop_strategy)
@settings(max_examples=50)
def test_uppaal_statements_whileloop_instantiation(instance):
    assert isinstance(instance, uppaal_statements_WhileLoop)

@given(instance=uppaal_statements_EmptyStatement_strategy)
@settings(max_examples=50)
def test_uppaal_statements_emptystatement_instantiation(instance):
    assert isinstance(instance, uppaal_statements_EmptyStatement)

@given(instance=uppaal_statements_ReturnStatement_strategy)
@settings(max_examples=50)
def test_uppaal_statements_returnstatement_instantiation(instance):
    assert isinstance(instance, uppaal_statements_ReturnStatement)

@given(instance=uppaal_statements_ForLoop_strategy)
@settings(max_examples=50)
def test_uppaal_statements_forloop_instantiation(instance):
    assert isinstance(instance, uppaal_statements_ForLoop)

@given(instance=uppaal_statements_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_uppaal_statements_expressionstatement_instantiation(instance):
    assert isinstance(instance, uppaal_statements_ExpressionStatement)

@given(instance=uppaal_statements_DoWhileLoop_strategy)
@settings(max_examples=50)
def test_uppaal_statements_dowhileloop_instantiation(instance):
    assert isinstance(instance, uppaal_statements_DoWhileLoop)

@given(instance=uppaal_statements_IfStatement_strategy)
@settings(max_examples=50)
def test_uppaal_statements_ifstatement_instantiation(instance):
    assert isinstance(instance, uppaal_statements_IfStatement)

@given(instance=uppaal_statements_Block_strategy)
@settings(max_examples=50)
def test_uppaal_statements_block_instantiation(instance):
    assert isinstance(instance, uppaal_statements_Block)

@given(instance=uppaal_statements_Statement_strategy)
@settings(max_examples=50)
def test_uppaal_statements_statement_instantiation(instance):
    assert isinstance(instance, uppaal_statements_Statement)

@given(instance=uppaal_templates_Synchronization_strategy)
@settings(max_examples=50)
def test_uppaal_templates_synchronization_instantiation(instance):
    assert isinstance(instance, uppaal_templates_Synchronization)



@given(instance=uppaal_templates_Synchronization_strategy)
def test_uppaal_templates_synchronization_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=Selection_strategy)
@settings(max_examples=50)
def test_selection_instantiation(instance):
    assert isinstance(instance, Selection)

@given(instance=Synchronization_strategy)
@settings(max_examples=50)
def test_synchronization_instantiation(instance):
    assert isinstance(instance, Synchronization)

@given(instance=visuals_ColoredElement_strategy)
@settings(max_examples=50)
def test_visuals_coloredelement_instantiation(instance):
    assert isinstance(instance, visuals_ColoredElement)

@given(instance=visuals_PlanarElement_strategy)
@settings(max_examples=50)
def test_visuals_planarelement_instantiation(instance):
    assert isinstance(instance, visuals_PlanarElement)

@given(instance=visuals_LinearElement_strategy)
@settings(max_examples=50)
def test_visuals_linearelement_instantiation(instance):
    assert isinstance(instance, visuals_LinearElement)

@given(instance=system_TemplateDeclaration_strategy)
@settings(max_examples=50)
def test_system_templatedeclaration_instantiation(instance):
    assert isinstance(instance, system_TemplateDeclaration)

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=Location_strategy)
@settings(max_examples=50)
def test_location_instantiation(instance):
    assert isinstance(instance, Location)

@given(instance=LocalDeclarations_strategy)
@settings(max_examples=50)
def test_localdeclarations_instantiation(instance):
    assert isinstance(instance, LocalDeclarations)

@given(instance=uppaal_system_ProgressMeasure_strategy)
@settings(max_examples=50)
def test_uppaal_system_progressmeasure_instantiation(instance):
    assert isinstance(instance, uppaal_system_ProgressMeasure)

@given(instance=AbstractTemplate_strategy)
@settings(max_examples=50)
def test_abstracttemplate_instantiation(instance):
    assert isinstance(instance, AbstractTemplate)

@given(instance=uppaal_templates_RedefinedTemplate_strategy)
@settings(max_examples=50)
def test_uppaal_templates_redefinedtemplate_instantiation(instance):
    assert isinstance(instance, uppaal_templates_RedefinedTemplate)

@given(instance=uppaal_templates_Template_strategy)
@settings(max_examples=50)
def test_uppaal_templates_template_instantiation(instance):
    assert isinstance(instance, uppaal_templates_Template)

@given(instance=uppaal_system_InstantiationList_strategy)
@settings(max_examples=50)
def test_uppaal_system_instantiationlist_instantiation(instance):
    assert isinstance(instance, uppaal_system_InstantiationList)

@given(instance=system_InstantiationList_strategy)
@settings(max_examples=50)
def test_system_instantiationlist_instantiation(instance):
    assert isinstance(instance, system_InstantiationList)

@given(instance=uppaal_system_System_strategy)
@settings(max_examples=50)
def test_uppaal_system_system_instantiation(instance):
    assert isinstance(instance, uppaal_system_System)

@given(instance=RedefinedTemplate_strategy)
@settings(max_examples=50)
def test_redefinedtemplate_instantiation(instance):
    assert isinstance(instance, RedefinedTemplate)

@given(instance=IdentifierExpression_strategy)
@settings(max_examples=50)
def test_identifierexpression_instantiation(instance):
    assert isinstance(instance, IdentifierExpression)

@given(instance=ChannelPriorityItem_strategy)
@settings(max_examples=50)
def test_channelpriorityitem_instantiation(instance):
    assert isinstance(instance, ChannelPriorityItem)

@given(instance=uppaal_global_DefaultChannelPriority_strategy)
@settings(max_examples=50)
def test_uppaal_global_defaultchannelpriority_instantiation(instance):
    assert isinstance(instance, uppaal_global_DefaultChannelPriority)

@given(instance=uppaal_global_ChannelList_strategy)
@settings(max_examples=50)
def test_uppaal_global_channellist_instantiation(instance):
    assert isinstance(instance, uppaal_global_ChannelList)

@given(instance=uppaal_global_ChannelPriorityItem_strategy)
@settings(max_examples=50)
def test_uppaal_global_channelpriorityitem_instantiation(instance):
    assert isinstance(instance, uppaal_global_ChannelPriorityItem)

@given(instance=global_ChannelPriorityItem_strategy)
@settings(max_examples=50)
def test_global_channelpriorityitem_instantiation(instance):
    assert isinstance(instance, global_ChannelPriorityItem)

@given(instance=uppaal_global_ChannelPriority_strategy)
@settings(max_examples=50)
def test_uppaal_global_channelpriority_instantiation(instance):
    assert isinstance(instance, uppaal_global_ChannelPriority)

@given(instance=uppaal_declarations_Initializer_strategy)
@settings(max_examples=50)
def test_uppaal_declarations_initializer_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_Initializer)

@given(instance=uppaal_declarations_Parameter_strategy)
@settings(max_examples=50)
def test_uppaal_declarations_parameter_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_Parameter)



@given(instance=uppaal_declarations_Parameter_strategy)
def test_uppaal_declarations_parameter_callType_setter(instance):
    original = instance.callType
    instance.callType = original
    assert instance.callType == original

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=uppaal_declarations_VariableContainer_strategy)
@settings(max_examples=50)
def test_uppaal_declarations_variablecontainer_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_VariableContainer)

@given(instance=uppaal_declarations_Index_strategy)
@settings(max_examples=50)
def test_uppaal_declarations_index_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_Index)

@given(instance=Initializer_strategy)
@settings(max_examples=50)
def test_initializer_instantiation(instance):
    assert isinstance(instance, Initializer)

@given(instance=uppaal_declarations_ArrayInitializer_strategy)
@settings(max_examples=50)
def test_uppaal_declarations_arrayinitializer_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_ArrayInitializer)

@given(instance=uppaal_declarations_ExpressionInitializer_strategy)
@settings(max_examples=50)
def test_uppaal_declarations_expressioninitializer_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_ExpressionInitializer)

@given(instance=VariableContainer_strategy)
@settings(max_examples=50)
def test_variablecontainer_instantiation(instance):
    assert isinstance(instance, VariableContainer)

@given(instance=uppaal_templates_Selection_strategy)
@settings(max_examples=50)
def test_uppaal_templates_selection_instantiation(instance):
    assert isinstance(instance, uppaal_templates_Selection)

@given(instance=DeclaredType_strategy)
@settings(max_examples=50)
def test_declaredtype_instantiation(instance):
    assert isinstance(instance, DeclaredType)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=Function_strategy)
@settings(max_examples=50)
def test_function_instantiation(instance):
    assert isinstance(instance, Function)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=uppaal_declarations_ClockVariableDeclaration_strategy)
@settings(max_examples=50)
def test_uppaal_declarations_clockvariabledeclaration_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_ClockVariableDeclaration)

@given(instance=uppaal_declarations_DataVariableDeclaration_strategy)
@settings(max_examples=50)
def test_uppaal_declarations_datavariabledeclaration_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_DataVariableDeclaration)



@given(instance=uppaal_declarations_DataVariableDeclaration_strategy)
def test_uppaal_declarations_datavariabledeclaration_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original

@given(instance=uppaal_declarations_ChannelVariableDeclaration_strategy)
@settings(max_examples=50)
def test_uppaal_declarations_channelvariabledeclaration_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_ChannelVariableDeclaration)



@given(instance=uppaal_declarations_ChannelVariableDeclaration_strategy)
def test_uppaal_declarations_channelvariabledeclaration_urgent_setter(instance):
    original = instance.urgent
    instance.urgent = original
    assert instance.urgent == original



@given(instance=uppaal_declarations_ChannelVariableDeclaration_strategy)
def test_uppaal_declarations_channelvariabledeclaration_broadcast_setter(instance):
    original = instance.broadcast
    instance.broadcast = original
    assert instance.broadcast == original

@given(instance=declarations_VariableContainer_strategy)
@settings(max_examples=50)
def test_declarations_variablecontainer_instantiation(instance):
    assert isinstance(instance, declarations_VariableContainer)

@given(instance=uppaal_expressions_QuantificationExpression_strategy)
@settings(max_examples=50)
def test_uppaal_expressions_quantificationexpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_QuantificationExpression)



@given(instance=uppaal_expressions_QuantificationExpression_strategy)
def test_uppaal_expressions_quantificationexpression_quantifier_setter(instance):
    original = instance.quantifier
    instance.quantifier = original
    assert instance.quantifier == original

@given(instance=uppaal_statements_Iteration_strategy)
@settings(max_examples=50)
def test_uppaal_statements_iteration_instantiation(instance):
    assert isinstance(instance, uppaal_statements_Iteration)

@given(instance=declarations_Declaration_strategy)
@settings(max_examples=50)
def test_declarations_declaration_instantiation(instance):
    assert isinstance(instance, declarations_Declaration)

@given(instance=uppaal_declarations_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_uppaal_declarations_variabledeclaration_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_VariableDeclaration)

@given(instance=uppaal_declarations_Declaration_strategy)
@settings(max_examples=50)
def test_uppaal_declarations_declaration_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_Declaration)

@given(instance=system_ProgressMeasure_strategy)
@settings(max_examples=50)
def test_system_progressmeasure_instantiation(instance):
    assert isinstance(instance, system_ProgressMeasure)

@given(instance=system_System_strategy)
@settings(max_examples=50)
def test_system_system_instantiation(instance):
    assert isinstance(instance, system_System)

@given(instance=global_ChannelPriority_strategy)
@settings(max_examples=50)
def test_global_channelpriority_instantiation(instance):
    assert isinstance(instance, global_ChannelPriority)

@given(instance=Declarations_strategy)
@settings(max_examples=50)
def test_declarations_instantiation(instance):
    assert isinstance(instance, Declarations)

@given(instance=uppaal_declarations_LocalDeclarations_strategy)
@settings(max_examples=50)
def test_uppaal_declarations_localdeclarations_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_LocalDeclarations)

@given(instance=uppaal_declarations_SystemDeclarations_strategy)
@settings(max_examples=50)
def test_uppaal_declarations_systemdeclarations_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_SystemDeclarations)

@given(instance=uppaal_declarations_GlobalDeclarations_strategy)
@settings(max_examples=50)
def test_uppaal_declarations_globaldeclarations_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_GlobalDeclarations)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=uppaal_declarations_FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_uppaal_declarations_functiondeclaration_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_FunctionDeclaration)

@given(instance=uppaal_system_TemplateDeclaration_strategy)
@settings(max_examples=50)
def test_uppaal_system_templatedeclaration_instantiation(instance):
    assert isinstance(instance, uppaal_system_TemplateDeclaration)

@given(instance=uppaal_declarations_TypeDeclaration_strategy)
@settings(max_examples=50)
def test_uppaal_declarations_typedeclaration_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_TypeDeclaration)

@given(instance=uppaal_declarations_Declarations_strategy)
@settings(max_examples=50)
def test_uppaal_declarations_declarations_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_Declarations)

@given(instance=uppaal_types_Library_strategy)
@settings(max_examples=50)
def test_uppaal_types_library_instantiation(instance):
    assert isinstance(instance, uppaal_types_Library)

@given(instance=IntegerBounds_strategy)
@settings(max_examples=50)
def test_integerbounds_instantiation(instance):
    assert isinstance(instance, IntegerBounds)

@given(instance=DataVariableDeclaration_strategy)
@settings(max_examples=50)
def test_datavariabledeclaration_instantiation(instance):
    assert isinstance(instance, DataVariableDeclaration)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=uppaal_expressions_ConditionExpression_strategy)
@settings(max_examples=50)
def test_uppaal_expressions_conditionexpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_ConditionExpression)

@given(instance=uppaal_expressions_NegationExpression_strategy)
@settings(max_examples=50)
def test_uppaal_expressions_negationexpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_NegationExpression)

@given(instance=uppaal_expressions_BinaryExpression_strategy)
@settings(max_examples=50)
def test_uppaal_expressions_binaryexpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_BinaryExpression)

@given(instance=uppaal_expressions_ScopedIdentifierExpression_strategy)
@settings(max_examples=50)
def test_uppaal_expressions_scopedidentifierexpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_ScopedIdentifierExpression)

@given(instance=uppaal_expressions_LiteralExpression_strategy)
@settings(max_examples=50)
def test_uppaal_expressions_literalexpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_LiteralExpression)



@given(instance=uppaal_expressions_LiteralExpression_strategy)
def test_uppaal_expressions_literalexpression_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=uppaal_expressions_IncrementDecrementExpression_strategy)
@settings(max_examples=50)
def test_uppaal_expressions_incrementdecrementexpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_IncrementDecrementExpression)



@given(instance=uppaal_expressions_IncrementDecrementExpression_strategy)
def test_uppaal_expressions_incrementdecrementexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original



@given(instance=uppaal_expressions_IncrementDecrementExpression_strategy)
def test_uppaal_expressions_incrementdecrementexpression_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=uppaal_expressions_MinusExpression_strategy)
@settings(max_examples=50)
def test_uppaal_expressions_minusexpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_MinusExpression)

@given(instance=uppaal_expressions_IdentifierExpression_strategy)
@settings(max_examples=50)
def test_uppaal_expressions_identifierexpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_IdentifierExpression)

@given(instance=uppaal_expressions_PlusExpression_strategy)
@settings(max_examples=50)
def test_uppaal_expressions_plusexpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_PlusExpression)

@given(instance=uppaal_expressions_FunctionCallExpression_strategy)
@settings(max_examples=50)
def test_uppaal_expressions_functioncallexpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_FunctionCallExpression)

@given(instance=uppaal_types_TypeDefinition_strategy)
@settings(max_examples=50)
def test_uppaal_types_typedefinition_instantiation(instance):
    assert isinstance(instance, uppaal_types_TypeDefinition)



@given(instance=uppaal_types_TypeDefinition_strategy)
def test_uppaal_types_typedefinition_baseType_setter(instance):
    original = instance.baseType
    instance.baseType = original
    assert instance.baseType == original

@given(instance=TypeDefinition_strategy)
@settings(max_examples=50)
def test_typedefinition_instantiation(instance):
    assert isinstance(instance, TypeDefinition)

@given(instance=uppaal_types_TypeSpecification_strategy)
@settings(max_examples=50)
def test_uppaal_types_typespecification_instantiation(instance):
    assert isinstance(instance, uppaal_types_TypeSpecification)

@given(instance=uppaal_types_TypeReference_strategy)
@settings(max_examples=50)
def test_uppaal_types_typereference_instantiation(instance):
    assert isinstance(instance, uppaal_types_TypeReference)

@given(instance=uppaal_types_IntegerBounds_strategy)
@settings(max_examples=50)
def test_uppaal_types_integerbounds_instantiation(instance):
    assert isinstance(instance, uppaal_types_IntegerBounds)

@given(instance=TypeDeclaration_strategy)
@settings(max_examples=50)
def test_typedeclaration_instantiation(instance):
    assert isinstance(instance, TypeDeclaration)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=uppaal_types_DeclaredType_strategy)
@settings(max_examples=50)
def test_uppaal_types_declaredtype_instantiation(instance):
    assert isinstance(instance, uppaal_types_DeclaredType)

@given(instance=uppaal_types_PredefinedType_strategy)
@settings(max_examples=50)
def test_uppaal_types_predefinedtype_instantiation(instance):
    assert isinstance(instance, uppaal_types_PredefinedType)



@given(instance=uppaal_types_PredefinedType_strategy)
def test_uppaal_types_predefinedtype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=TypeSpecification_strategy)
@settings(max_examples=50)
def test_typespecification_instantiation(instance):
    assert isinstance(instance, TypeSpecification)

@given(instance=uppaal_types_RangeTypeSpecification_strategy)
@settings(max_examples=50)
def test_uppaal_types_rangetypespecification_instantiation(instance):
    assert isinstance(instance, uppaal_types_RangeTypeSpecification)

@given(instance=uppaal_types_StructTypeSpecification_strategy)
@settings(max_examples=50)
def test_uppaal_types_structtypespecification_instantiation(instance):
    assert isinstance(instance, uppaal_types_StructTypeSpecification)

@given(instance=uppaal_types_ScalarTypeSpecification_strategy)
@settings(max_examples=50)
def test_uppaal_types_scalartypespecification_instantiation(instance):
    assert isinstance(instance, uppaal_types_ScalarTypeSpecification)

@given(instance=Index_strategy)
@settings(max_examples=50)
def test_index_instantiation(instance):
    assert isinstance(instance, Index)

@given(instance=uppaal_declarations_ValueIndex_strategy)
@settings(max_examples=50)
def test_uppaal_declarations_valueindex_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_ValueIndex)

@given(instance=uppaal_declarations_TypeIndex_strategy)
@settings(max_examples=50)
def test_uppaal_declarations_typeindex_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_TypeIndex)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=uppaal_declarations_Function_strategy)
@settings(max_examples=50)
def test_uppaal_declarations_function_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_Function)

@given(instance=uppaal_declarations_Variable_strategy)
@settings(max_examples=50)
def test_uppaal_declarations_variable_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_Variable)

@given(instance=uppaal_types_Type_strategy)
@settings(max_examples=50)
def test_uppaal_types_type_instantiation(instance):
    assert isinstance(instance, uppaal_types_Type)



@given(instance=uppaal_types_Type_strategy)
def test_uppaal_types_type_baseType_setter(instance):
    original = instance.baseType
    instance.baseType = original
    assert instance.baseType == original

@given(instance=uppaal_core_CommentableElement_strategy)
@settings(max_examples=50)
def test_uppaal_core_commentableelement_instantiation(instance):
    assert isinstance(instance, uppaal_core_CommentableElement)



@given(instance=uppaal_core_CommentableElement_strategy)
def test_uppaal_core_commentableelement_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=PredefinedType_strategy)
@settings(max_examples=50)
def test_predefinedtype_instantiation(instance):
    assert isinstance(instance, PredefinedType)

@given(instance=SystemDeclarations_strategy)
@settings(max_examples=50)
def test_systemdeclarations_instantiation(instance):
    assert isinstance(instance, SystemDeclarations)

@given(instance=Template_strategy)
@settings(max_examples=50)
def test_template_instantiation(instance):
    assert isinstance(instance, Template)

@given(instance=GlobalDeclarations_strategy)
@settings(max_examples=50)
def test_globaldeclarations_instantiation(instance):
    assert isinstance(instance, GlobalDeclarations)

@given(instance=uppaal_core_NamedElement_strategy)
@settings(max_examples=50)
def test_uppaal_core_namedelement_instantiation(instance):
    assert isinstance(instance, uppaal_core_NamedElement)



@given(instance=uppaal_core_NamedElement_strategy)
def test_uppaal_core_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=core_CommentableElement_strategy)
@settings(max_examples=50)
def test_core_commentableelement_instantiation(instance):
    assert isinstance(instance, core_CommentableElement)

@given(instance=uppaal_templates_Edge_strategy)
@settings(max_examples=50)
def test_uppaal_templates_edge_instantiation(instance):
    assert isinstance(instance, uppaal_templates_Edge)

@given(instance=core_NamedElement_strategy)
@settings(max_examples=50)
def test_core_namedelement_instantiation(instance):
    assert isinstance(instance, core_NamedElement)

@given(instance=uppaal_templates_AbstractTemplate_strategy)
@settings(max_examples=50)
def test_uppaal_templates_abstracttemplate_instantiation(instance):
    assert isinstance(instance, uppaal_templates_AbstractTemplate)

@given(instance=uppaal_templates_Location_strategy)
@settings(max_examples=50)
def test_uppaal_templates_location_instantiation(instance):
    assert isinstance(instance, uppaal_templates_Location)



@given(instance=uppaal_templates_Location_strategy)
def test_uppaal_templates_location_locationTimeKind_setter(instance):
    original = instance.locationTimeKind
    instance.locationTimeKind = original
    assert instance.locationTimeKind == original

@given(instance=uppaal_NTA_strategy)
@settings(max_examples=50)
def test_uppaal_nta_instantiation(instance):
    assert isinstance(instance, uppaal_NTA)
