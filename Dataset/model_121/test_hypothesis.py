import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PrimitiveType,
    ccsl_datatype_StringPrimitiveType,
    DataType,
    ccsl_datatype_PrimitiveType,
    annotation_Annotation,
    complexType_AnnotationType,
    statements_Block,
    tryCatch_CatchClause,
    UnaryAssignment,
    ccsl_assignment_PostfixUnaryAssignment,
    ccsl_assignment_PrefixUnaryAssignment,
    AbstractAssignment,
    ccsl_assignment_UnaryAssignment,
    ccsl_assignment_Assignment,
    OperatorExpression,
    ccsl_expressions_InfixExpression,
    ccsl_expressions_BooleanExpression,
    ccsl_expressions_ArithmeticExpression,
    ccsl_expressions_StringConcatenation,
    Block,
    ccsl_controlFlow_SwitchCaseBlock,
    controlFlow_SwitchCaseBlock,
    ControlFlow,
    ccsl_controlFlow_LoopStatement,
    ccsl_controlFlow_IfStatement,
    ccsl_controlFlow_SwitchStatement,
    LiteralValue,
    ccsl_literalValues_BooleanLiteral,
    ccsl_literalValues_StringLiteral,
    ccsl_literalValues_CharacterLiteral,
    ccsl_literalValues_NumberLiteral,
    ccsl_literalValues_NullLiteral,
    ccsl_statements_ThrowStatement,
    Statement,
    ccsl_statements_ArrayCreation,
    ccsl_statements_ContinueStatement,
    ccsl_expressions_ParenthesizedExpression,
    ccsl_statements_Access,
    ccsl_statements_SynchronizedBlock,
    ccsl_expressions_OperatorExpression,
    ccsl_tryCatch_TryStatement,
    ccsl_annotation_Annotation,
    ccsl_literalValues_LiteralValue,
    ccsl_assignment_AbstractAssignment,
    ccsl_tryCatch_CatchClause,
    ccsl_statements_ThisStatement,
    ccsl_statements_ReturnStatement,
    ccsl_statements_InstanceOf,
    ccsl_statements_BreakStatement,
    ccsl_statements_EmptyStatement,
    ccsl_statements_NamedElementAccess,
    method_SimpleMethod,
    variable_ParameterVariable,
    elements_Element,
    SimpleMethod,
    ccsl_method_Constructor,
    ccsl_statements_InstanceCreation,
    ccsl_statements_VarDeclaration,
    ccsl_statements_Block,
    ccsl_statements_ControlFlow,
    Access,
    ccsl_statements_DataTypeAccess,
    ccsl_statements_VariableAccess,
    complexType_JClass,
    method_Constructor,
    datatype_ObjectType,
    ComplexType,
    ccsl_complexType_AnonymousClass,
    complexType_ComplexType,
    variable_InitializableVariable,
    statements_Statement,
    DeclaredType,
    ccsl_complexType_AnnotationType,
    method_Method,
    variable_FieldVariable,
    import_ImportStatement,
    complexType_JInterface,
    ccsl_elements_Element,
    InjectionStrategy,
    InjectionAction,
    ccsl_Root,
    Variable,
    ccsl_variable_InitializableVariable,
    InitializableVariable,
    ccsl_variable_LocalVariable,
    annotation_AnnotableElement,
    ccsl_variable_FieldVariable,
    ccsl_method_SimpleMethod,
    variable_Variable,
    ccsl_variable_ParameterVariable,
    datatype_DataType,
    NamedElement,
    ccsl_variable_Variable,
    complexType_DeclaredType,
    ccsl_complexType_JClass,
    ccsl_complexType_JInterface,
    import_ImportableElement,
    namedElements_NamedElement,
    ccsl_method_Method,
    ccsl_complexType_DeclaredType,
    ccsl_namedElements_Package,
    Context,
    Element,
    ccsl_complexType_ComplexType,
    ccsl_namedElements_NamedElement,
    ccsl_annotation_AnnotableElement,
    ccsl_datatype_DataType,
    ccsl_statements_Statement,
    Rule,
    ccsl_AtomicRule,
    ccsl_CompositeRule,
    Root,
    ccsl_FaultTypeDescription,
    ccsl_Rule,
    statements_Access,
    CcslNumberFunction,
    ccsl_numberFunctions_GetIndexOf,
    ccsl_numberFunctions_CcslIntegerLiteral,
    numberFunctions_CcslNumberFunction,
    ccsl_filters_EquationFilter,
    AtomicFilter,
    ccsl_filters_SameNameFilter,
    ccsl_filters_HasSameReferenceFilter,
    ccsl_filters_IsKindOfFilter,
    ccsl_filters_SuperClassClosureFilter,
    ccsl_filters_IsStringFilter,
    ccsl_filters_BlockLastStatementFilter,
    ccsl_filters_TemplateFilter,
    ccsl_filters_ChildClosureComplexTypeFilter,
    ccsl_filters_FromClosureFilter,
    ccsl_filters_SuperMethodClosureFilter,
    ccsl_filters_IsTypeOfFilter,
    ccsl_filters_PropertyFilter,
    Filter,
    ccsl_filters_CompositeFilter,
    ccsl_filters_AtomicFilter,
    CcslBooleanFunction,
    ccsl_filters_Filter,
    CcslFunction,
    ccsl_numberFunctions_CcslNumberFunction,
    ccsl_booleanFunctions_CcslBooleanFunction,
    ccsl_filters_ImplicityContainerFilter,
    expressions_OperatorExpression,
    TemplateFilter,
    ccsl_filters_ImplicityOperandFilter,
    ccsl_filters_RegexMatch,
    ccsl_filters_CountFilter,
    ccsl_faultTypeDescription_InjectionAction,
    filters_Filter,
    ccsl_context_Context,
    ccsl_datatype_VoidType,
    ccsl_datatype_IntPrimitiveType,
    ccsl_datatype_GenericType,
    ObjectType,
    ccsl_datatype_ArrayType,
    ccsl_datatype_ParameterizedType,
    ccsl_datatype_ObjectType,
    ccsl_functions_CcslFunction,
    ccsl_strategy_AllStrategy,
    ccsl_action_ArithmeticOperatorMap,
    action_ArithmeticOperatorMap,
    ccsl_action_ReplaceArithmeticOperatorAction,
    ccsl_action_ReplaceVariableAccessAction,
    ccsl_action_DeleteRandomStatementAction,
    ccsl_action_ChangeLiteralValueAction,
    ccsl_action_DeleteInfixOperatorAction,
    ccsl_action_MoveScopeUpAction,
    ccsl_action_DeleteAction,
    ccsl_faultTypeDescription_InjectionStrategy,
    ccsl_import_ImportStatement,
    ccsl_import_ImportableElement,
    Invocation,
    ccsl_invocation_SimpleMethodInvocation,
    ccsl_invocation_ConstructorInvocation,
    ccsl_invocation_Invocation,
    SimpleMethodInvocation,
    ccsl_invocation_SuperMethodInvocation,
    ccsl_invocation_MethodInvocation,
    ccsl_datatype_ShortPrimitiveType,
    ccsl_datatype_BooleanPrimitiveType,
    CollectionKind,
    EquationOperator,
    UnaryAssignmentOperator,
    Inheritance,
    AssignmentOperator,
    Visibility,
    ArithmeticOperator,
    LogicOperator,
    BooleanOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_datatype_stringprimitivetype_is_not_abstract():
    assert not inspect.isabstract(ccsl_datatype_StringPrimitiveType)


def test_ccsl_datatype_stringprimitivetype_constructor_exists():
    assert callable(ccsl_datatype_StringPrimitiveType.__init__)


def test_ccsl_datatype_stringprimitivetype_constructor_args():
    sig = inspect.signature(ccsl_datatype_StringPrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_datatype_primitivetype_is_not_abstract():
    assert not inspect.isabstract(ccsl_datatype_PrimitiveType)


def test_ccsl_datatype_primitivetype_constructor_exists():
    assert callable(ccsl_datatype_PrimitiveType.__init__)


def test_ccsl_datatype_primitivetype_constructor_args():
    sig = inspect.signature(ccsl_datatype_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_annotation_annotation_is_not_abstract():
    assert not inspect.isabstract(annotation_Annotation)


def test_annotation_annotation_constructor_exists():
    assert callable(annotation_Annotation.__init__)


def test_annotation_annotation_constructor_args():
    sig = inspect.signature(annotation_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_complextype_annotationtype_is_not_abstract():
    assert not inspect.isabstract(complexType_AnnotationType)


def test_complextype_annotationtype_constructor_exists():
    assert callable(complexType_AnnotationType.__init__)


def test_complextype_annotationtype_constructor_args():
    sig = inspect.signature(complexType_AnnotationType.__init__)
    params = list(sig.parameters.keys())



def test_statements_block_is_not_abstract():
    assert not inspect.isabstract(statements_Block)


def test_statements_block_constructor_exists():
    assert callable(statements_Block.__init__)


def test_statements_block_constructor_args():
    sig = inspect.signature(statements_Block.__init__)
    params = list(sig.parameters.keys())



def test_trycatch_catchclause_is_not_abstract():
    assert not inspect.isabstract(tryCatch_CatchClause)


def test_trycatch_catchclause_constructor_exists():
    assert callable(tryCatch_CatchClause.__init__)


def test_trycatch_catchclause_constructor_args():
    sig = inspect.signature(tryCatch_CatchClause.__init__)
    params = list(sig.parameters.keys())



def test_unaryassignment_is_not_abstract():
    assert not inspect.isabstract(UnaryAssignment)


def test_unaryassignment_constructor_exists():
    assert callable(UnaryAssignment.__init__)


def test_unaryassignment_constructor_args():
    sig = inspect.signature(UnaryAssignment.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_assignment_postfixunaryassignment_is_not_abstract():
    assert not inspect.isabstract(ccsl_assignment_PostfixUnaryAssignment)


def test_ccsl_assignment_postfixunaryassignment_constructor_exists():
    assert callable(ccsl_assignment_PostfixUnaryAssignment.__init__)


def test_ccsl_assignment_postfixunaryassignment_constructor_args():
    sig = inspect.signature(ccsl_assignment_PostfixUnaryAssignment.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_assignment_prefixunaryassignment_is_not_abstract():
    assert not inspect.isabstract(ccsl_assignment_PrefixUnaryAssignment)


def test_ccsl_assignment_prefixunaryassignment_constructor_exists():
    assert callable(ccsl_assignment_PrefixUnaryAssignment.__init__)


def test_ccsl_assignment_prefixunaryassignment_constructor_args():
    sig = inspect.signature(ccsl_assignment_PrefixUnaryAssignment.__init__)
    params = list(sig.parameters.keys())



def test_abstractassignment_is_not_abstract():
    assert not inspect.isabstract(AbstractAssignment)


def test_abstractassignment_constructor_exists():
    assert callable(AbstractAssignment.__init__)


def test_abstractassignment_constructor_args():
    sig = inspect.signature(AbstractAssignment.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_assignment_unaryassignment_is_not_abstract():
    assert not inspect.isabstract(ccsl_assignment_UnaryAssignment)


def test_ccsl_assignment_unaryassignment_constructor_exists():
    assert callable(ccsl_assignment_UnaryAssignment.__init__)


def test_ccsl_assignment_unaryassignment_constructor_args():
    sig = inspect.signature(ccsl_assignment_UnaryAssignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ccsl_assignment_unaryassignment_has_operator():
    assert hasattr(ccsl_assignment_UnaryAssignment, "operator")
    descriptor = None
    for klass in ccsl_assignment_UnaryAssignment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_ccsl_assignment_assignment_is_not_abstract():
    assert not inspect.isabstract(ccsl_assignment_Assignment)


def test_ccsl_assignment_assignment_constructor_exists():
    assert callable(ccsl_assignment_Assignment.__init__)


def test_ccsl_assignment_assignment_constructor_args():
    sig = inspect.signature(ccsl_assignment_Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ccsl_assignment_assignment_has_operator():
    assert hasattr(ccsl_assignment_Assignment, "operator")
    descriptor = None
    for klass in ccsl_assignment_Assignment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_operatorexpression_is_not_abstract():
    assert not inspect.isabstract(OperatorExpression)


def test_operatorexpression_constructor_exists():
    assert callable(OperatorExpression.__init__)


def test_operatorexpression_constructor_args():
    sig = inspect.signature(OperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_expressions_infixexpression_is_not_abstract():
    assert not inspect.isabstract(ccsl_expressions_InfixExpression)


def test_ccsl_expressions_infixexpression_constructor_exists():
    assert callable(ccsl_expressions_InfixExpression.__init__)


def test_ccsl_expressions_infixexpression_constructor_args():
    sig = inspect.signature(ccsl_expressions_InfixExpression.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_expressions_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(ccsl_expressions_BooleanExpression)


def test_ccsl_expressions_booleanexpression_constructor_exists():
    assert callable(ccsl_expressions_BooleanExpression.__init__)


def test_ccsl_expressions_booleanexpression_constructor_args():
    sig = inspect.signature(ccsl_expressions_BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "booleanOperator" in params, "Missing parameter 'booleanOperator'"

def test_ccsl_expressions_booleanexpression_has_booleanOperator():
    assert hasattr(ccsl_expressions_BooleanExpression, "booleanOperator")
    descriptor = None
    for klass in ccsl_expressions_BooleanExpression.__mro__:
        if "booleanOperator" in klass.__dict__:
            descriptor = klass.__dict__["booleanOperator"]
            break
    assert isinstance(descriptor, property)



def test_ccsl_expressions_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(ccsl_expressions_ArithmeticExpression)


def test_ccsl_expressions_arithmeticexpression_constructor_exists():
    assert callable(ccsl_expressions_ArithmeticExpression.__init__)


def test_ccsl_expressions_arithmeticexpression_constructor_args():
    sig = inspect.signature(ccsl_expressions_ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())
    assert "arithmeticOperator" in params, "Missing parameter 'arithmeticOperator'"

def test_ccsl_expressions_arithmeticexpression_has_arithmeticOperator():
    assert hasattr(ccsl_expressions_ArithmeticExpression, "arithmeticOperator")
    descriptor = None
    for klass in ccsl_expressions_ArithmeticExpression.__mro__:
        if "arithmeticOperator" in klass.__dict__:
            descriptor = klass.__dict__["arithmeticOperator"]
            break
    assert isinstance(descriptor, property)



def test_ccsl_expressions_stringconcatenation_is_not_abstract():
    assert not inspect.isabstract(ccsl_expressions_StringConcatenation)


def test_ccsl_expressions_stringconcatenation_constructor_exists():
    assert callable(ccsl_expressions_StringConcatenation.__init__)


def test_ccsl_expressions_stringconcatenation_constructor_args():
    sig = inspect.signature(ccsl_expressions_StringConcatenation.__init__)
    params = list(sig.parameters.keys())



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_controlflow_switchcaseblock_is_not_abstract():
    assert not inspect.isabstract(ccsl_controlFlow_SwitchCaseBlock)


def test_ccsl_controlflow_switchcaseblock_constructor_exists():
    assert callable(ccsl_controlFlow_SwitchCaseBlock.__init__)


def test_ccsl_controlflow_switchcaseblock_constructor_args():
    sig = inspect.signature(ccsl_controlFlow_SwitchCaseBlock.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_ccsl_controlflow_switchcaseblock_has_default():
    assert hasattr(ccsl_controlFlow_SwitchCaseBlock, "default")
    descriptor = None
    for klass in ccsl_controlFlow_SwitchCaseBlock.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_controlflow_switchcaseblock_is_not_abstract():
    assert not inspect.isabstract(controlFlow_SwitchCaseBlock)


def test_controlflow_switchcaseblock_constructor_exists():
    assert callable(controlFlow_SwitchCaseBlock.__init__)


def test_controlflow_switchcaseblock_constructor_args():
    sig = inspect.signature(controlFlow_SwitchCaseBlock.__init__)
    params = list(sig.parameters.keys())



def test_controlflow_is_not_abstract():
    assert not inspect.isabstract(ControlFlow)


def test_controlflow_constructor_exists():
    assert callable(ControlFlow.__init__)


def test_controlflow_constructor_args():
    sig = inspect.signature(ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_controlflow_loopstatement_is_not_abstract():
    assert not inspect.isabstract(ccsl_controlFlow_LoopStatement)


def test_ccsl_controlflow_loopstatement_constructor_exists():
    assert callable(ccsl_controlFlow_LoopStatement.__init__)


def test_ccsl_controlflow_loopstatement_constructor_args():
    sig = inspect.signature(ccsl_controlFlow_LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_controlflow_ifstatement_is_not_abstract():
    assert not inspect.isabstract(ccsl_controlFlow_IfStatement)


def test_ccsl_controlflow_ifstatement_constructor_exists():
    assert callable(ccsl_controlFlow_IfStatement.__init__)


def test_ccsl_controlflow_ifstatement_constructor_args():
    sig = inspect.signature(ccsl_controlFlow_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_controlflow_switchstatement_is_not_abstract():
    assert not inspect.isabstract(ccsl_controlFlow_SwitchStatement)


def test_ccsl_controlflow_switchstatement_constructor_exists():
    assert callable(ccsl_controlFlow_SwitchStatement.__init__)


def test_ccsl_controlflow_switchstatement_constructor_args():
    sig = inspect.signature(ccsl_controlFlow_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_literalvalue_is_not_abstract():
    assert not inspect.isabstract(LiteralValue)


def test_literalvalue_constructor_exists():
    assert callable(LiteralValue.__init__)


def test_literalvalue_constructor_args():
    sig = inspect.signature(LiteralValue.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_literalvalues_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(ccsl_literalValues_BooleanLiteral)


def test_ccsl_literalvalues_booleanliteral_constructor_exists():
    assert callable(ccsl_literalValues_BooleanLiteral.__init__)


def test_ccsl_literalvalues_booleanliteral_constructor_args():
    sig = inspect.signature(ccsl_literalValues_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_literalvalues_stringliteral_is_not_abstract():
    assert not inspect.isabstract(ccsl_literalValues_StringLiteral)


def test_ccsl_literalvalues_stringliteral_constructor_exists():
    assert callable(ccsl_literalValues_StringLiteral.__init__)


def test_ccsl_literalvalues_stringliteral_constructor_args():
    sig = inspect.signature(ccsl_literalValues_StringLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_literalvalues_characterliteral_is_not_abstract():
    assert not inspect.isabstract(ccsl_literalValues_CharacterLiteral)


def test_ccsl_literalvalues_characterliteral_constructor_exists():
    assert callable(ccsl_literalValues_CharacterLiteral.__init__)


def test_ccsl_literalvalues_characterliteral_constructor_args():
    sig = inspect.signature(ccsl_literalValues_CharacterLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_literalvalues_numberliteral_is_not_abstract():
    assert not inspect.isabstract(ccsl_literalValues_NumberLiteral)


def test_ccsl_literalvalues_numberliteral_constructor_exists():
    assert callable(ccsl_literalValues_NumberLiteral.__init__)


def test_ccsl_literalvalues_numberliteral_constructor_args():
    sig = inspect.signature(ccsl_literalValues_NumberLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_literalvalues_nullliteral_is_not_abstract():
    assert not inspect.isabstract(ccsl_literalValues_NullLiteral)


def test_ccsl_literalvalues_nullliteral_constructor_exists():
    assert callable(ccsl_literalValues_NullLiteral.__init__)


def test_ccsl_literalvalues_nullliteral_constructor_args():
    sig = inspect.signature(ccsl_literalValues_NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_statements_throwstatement_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_ThrowStatement)


def test_ccsl_statements_throwstatement_constructor_exists():
    assert callable(ccsl_statements_ThrowStatement.__init__)


def test_ccsl_statements_throwstatement_constructor_args():
    sig = inspect.signature(ccsl_statements_ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_statements_arraycreation_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_ArrayCreation)


def test_ccsl_statements_arraycreation_constructor_exists():
    assert callable(ccsl_statements_ArrayCreation.__init__)


def test_ccsl_statements_arraycreation_constructor_args():
    sig = inspect.signature(ccsl_statements_ArrayCreation.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_statements_continuestatement_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_ContinueStatement)


def test_ccsl_statements_continuestatement_constructor_exists():
    assert callable(ccsl_statements_ContinueStatement.__init__)


def test_ccsl_statements_continuestatement_constructor_args():
    sig = inspect.signature(ccsl_statements_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_expressions_parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(ccsl_expressions_ParenthesizedExpression)


def test_ccsl_expressions_parenthesizedexpression_constructor_exists():
    assert callable(ccsl_expressions_ParenthesizedExpression.__init__)


def test_ccsl_expressions_parenthesizedexpression_constructor_args():
    sig = inspect.signature(ccsl_expressions_ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_statements_access_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_Access)


def test_ccsl_statements_access_constructor_exists():
    assert callable(ccsl_statements_Access.__init__)


def test_ccsl_statements_access_constructor_args():
    sig = inspect.signature(ccsl_statements_Access.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_statements_synchronizedblock_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_SynchronizedBlock)


def test_ccsl_statements_synchronizedblock_constructor_exists():
    assert callable(ccsl_statements_SynchronizedBlock.__init__)


def test_ccsl_statements_synchronizedblock_constructor_args():
    sig = inspect.signature(ccsl_statements_SynchronizedBlock.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_expressions_operatorexpression_is_not_abstract():
    assert not inspect.isabstract(ccsl_expressions_OperatorExpression)


def test_ccsl_expressions_operatorexpression_constructor_exists():
    assert callable(ccsl_expressions_OperatorExpression.__init__)


def test_ccsl_expressions_operatorexpression_constructor_args():
    sig = inspect.signature(ccsl_expressions_OperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_trycatch_trystatement_is_not_abstract():
    assert not inspect.isabstract(ccsl_tryCatch_TryStatement)


def test_ccsl_trycatch_trystatement_constructor_exists():
    assert callable(ccsl_tryCatch_TryStatement.__init__)


def test_ccsl_trycatch_trystatement_constructor_args():
    sig = inspect.signature(ccsl_tryCatch_TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_annotation_annotation_is_not_abstract():
    assert not inspect.isabstract(ccsl_annotation_Annotation)


def test_ccsl_annotation_annotation_constructor_exists():
    assert callable(ccsl_annotation_Annotation.__init__)


def test_ccsl_annotation_annotation_constructor_args():
    sig = inspect.signature(ccsl_annotation_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_literalvalues_literalvalue_is_not_abstract():
    assert not inspect.isabstract(ccsl_literalValues_LiteralValue)


def test_ccsl_literalvalues_literalvalue_constructor_exists():
    assert callable(ccsl_literalValues_LiteralValue.__init__)


def test_ccsl_literalvalues_literalvalue_constructor_args():
    sig = inspect.signature(ccsl_literalValues_LiteralValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ccsl_literalvalues_literalvalue_has_value():
    assert hasattr(ccsl_literalValues_LiteralValue, "value")
    descriptor = None
    for klass in ccsl_literalValues_LiteralValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ccsl_assignment_abstractassignment_is_not_abstract():
    assert not inspect.isabstract(ccsl_assignment_AbstractAssignment)


def test_ccsl_assignment_abstractassignment_constructor_exists():
    assert callable(ccsl_assignment_AbstractAssignment.__init__)


def test_ccsl_assignment_abstractassignment_constructor_args():
    sig = inspect.signature(ccsl_assignment_AbstractAssignment.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_trycatch_catchclause_is_not_abstract():
    assert not inspect.isabstract(ccsl_tryCatch_CatchClause)


def test_ccsl_trycatch_catchclause_constructor_exists():
    assert callable(ccsl_tryCatch_CatchClause.__init__)


def test_ccsl_trycatch_catchclause_constructor_args():
    sig = inspect.signature(ccsl_tryCatch_CatchClause.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_statements_thisstatement_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_ThisStatement)


def test_ccsl_statements_thisstatement_constructor_exists():
    assert callable(ccsl_statements_ThisStatement.__init__)


def test_ccsl_statements_thisstatement_constructor_args():
    sig = inspect.signature(ccsl_statements_ThisStatement.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_statements_returnstatement_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_ReturnStatement)


def test_ccsl_statements_returnstatement_constructor_exists():
    assert callable(ccsl_statements_ReturnStatement.__init__)


def test_ccsl_statements_returnstatement_constructor_args():
    sig = inspect.signature(ccsl_statements_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_statements_instanceof_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_InstanceOf)


def test_ccsl_statements_instanceof_constructor_exists():
    assert callable(ccsl_statements_InstanceOf.__init__)


def test_ccsl_statements_instanceof_constructor_args():
    sig = inspect.signature(ccsl_statements_InstanceOf.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_statements_breakstatement_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_BreakStatement)


def test_ccsl_statements_breakstatement_constructor_exists():
    assert callable(ccsl_statements_BreakStatement.__init__)


def test_ccsl_statements_breakstatement_constructor_args():
    sig = inspect.signature(ccsl_statements_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_statements_emptystatement_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_EmptyStatement)


def test_ccsl_statements_emptystatement_constructor_exists():
    assert callable(ccsl_statements_EmptyStatement.__init__)


def test_ccsl_statements_emptystatement_constructor_args():
    sig = inspect.signature(ccsl_statements_EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_statements_namedelementaccess_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_NamedElementAccess)


def test_ccsl_statements_namedelementaccess_constructor_exists():
    assert callable(ccsl_statements_NamedElementAccess.__init__)


def test_ccsl_statements_namedelementaccess_constructor_args():
    sig = inspect.signature(ccsl_statements_NamedElementAccess.__init__)
    params = list(sig.parameters.keys())



def test_method_simplemethod_is_not_abstract():
    assert not inspect.isabstract(method_SimpleMethod)


def test_method_simplemethod_constructor_exists():
    assert callable(method_SimpleMethod.__init__)


def test_method_simplemethod_constructor_args():
    sig = inspect.signature(method_SimpleMethod.__init__)
    params = list(sig.parameters.keys())



def test_variable_parametervariable_is_not_abstract():
    assert not inspect.isabstract(variable_ParameterVariable)


def test_variable_parametervariable_constructor_exists():
    assert callable(variable_ParameterVariable.__init__)


def test_variable_parametervariable_constructor_args():
    sig = inspect.signature(variable_ParameterVariable.__init__)
    params = list(sig.parameters.keys())



def test_elements_element_is_not_abstract():
    assert not inspect.isabstract(elements_Element)


def test_elements_element_constructor_exists():
    assert callable(elements_Element.__init__)


def test_elements_element_constructor_args():
    sig = inspect.signature(elements_Element.__init__)
    params = list(sig.parameters.keys())



def test_simplemethod_is_not_abstract():
    assert not inspect.isabstract(SimpleMethod)


def test_simplemethod_constructor_exists():
    assert callable(SimpleMethod.__init__)


def test_simplemethod_constructor_args():
    sig = inspect.signature(SimpleMethod.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_method_constructor_is_not_abstract():
    assert not inspect.isabstract(ccsl_method_Constructor)


def test_ccsl_method_constructor_constructor_exists():
    assert callable(ccsl_method_Constructor.__init__)


def test_ccsl_method_constructor_constructor_args():
    sig = inspect.signature(ccsl_method_Constructor.__init__)
    params = list(sig.parameters.keys())
    assert "avaliableInSourceCode" in params, "Missing parameter 'avaliableInSourceCode'"

def test_ccsl_method_constructor_has_avaliableInSourceCode():
    assert hasattr(ccsl_method_Constructor, "avaliableInSourceCode")
    descriptor = None
    for klass in ccsl_method_Constructor.__mro__:
        if "avaliableInSourceCode" in klass.__dict__:
            descriptor = klass.__dict__["avaliableInSourceCode"]
            break
    assert isinstance(descriptor, property)



def test_ccsl_statements_instancecreation_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_InstanceCreation)


def test_ccsl_statements_instancecreation_constructor_exists():
    assert callable(ccsl_statements_InstanceCreation.__init__)


def test_ccsl_statements_instancecreation_constructor_args():
    sig = inspect.signature(ccsl_statements_InstanceCreation.__init__)
    params = list(sig.parameters.keys())
    assert "argsKind" in params, "Missing parameter 'argsKind'"

def test_ccsl_statements_instancecreation_has_argsKind():
    assert hasattr(ccsl_statements_InstanceCreation, "argsKind")
    descriptor = None
    for klass in ccsl_statements_InstanceCreation.__mro__:
        if "argsKind" in klass.__dict__:
            descriptor = klass.__dict__["argsKind"]
            break
    assert isinstance(descriptor, property)



def test_ccsl_statements_vardeclaration_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_VarDeclaration)


def test_ccsl_statements_vardeclaration_constructor_exists():
    assert callable(ccsl_statements_VarDeclaration.__init__)


def test_ccsl_statements_vardeclaration_constructor_args():
    sig = inspect.signature(ccsl_statements_VarDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_statements_block_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_Block)


def test_ccsl_statements_block_constructor_exists():
    assert callable(ccsl_statements_Block.__init__)


def test_ccsl_statements_block_constructor_args():
    sig = inspect.signature(ccsl_statements_Block.__init__)
    params = list(sig.parameters.keys())
    assert "statementsKind" in params, "Missing parameter 'statementsKind'"

def test_ccsl_statements_block_has_statementsKind():
    assert hasattr(ccsl_statements_Block, "statementsKind")
    descriptor = None
    for klass in ccsl_statements_Block.__mro__:
        if "statementsKind" in klass.__dict__:
            descriptor = klass.__dict__["statementsKind"]
            break
    assert isinstance(descriptor, property)



def test_ccsl_statements_controlflow_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_ControlFlow)


def test_ccsl_statements_controlflow_constructor_exists():
    assert callable(ccsl_statements_ControlFlow.__init__)


def test_ccsl_statements_controlflow_constructor_args():
    sig = inspect.signature(ccsl_statements_ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_access_is_not_abstract():
    assert not inspect.isabstract(Access)


def test_access_constructor_exists():
    assert callable(Access.__init__)


def test_access_constructor_args():
    sig = inspect.signature(Access.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_statements_datatypeaccess_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_DataTypeAccess)


def test_ccsl_statements_datatypeaccess_constructor_exists():
    assert callable(ccsl_statements_DataTypeAccess.__init__)


def test_ccsl_statements_datatypeaccess_constructor_args():
    sig = inspect.signature(ccsl_statements_DataTypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_statements_variableaccess_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_VariableAccess)


def test_ccsl_statements_variableaccess_constructor_exists():
    assert callable(ccsl_statements_VariableAccess.__init__)


def test_ccsl_statements_variableaccess_constructor_args():
    sig = inspect.signature(ccsl_statements_VariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_complextype_jclass_is_not_abstract():
    assert not inspect.isabstract(complexType_JClass)


def test_complextype_jclass_constructor_exists():
    assert callable(complexType_JClass.__init__)


def test_complextype_jclass_constructor_args():
    sig = inspect.signature(complexType_JClass.__init__)
    params = list(sig.parameters.keys())



def test_method_constructor_is_not_abstract():
    assert not inspect.isabstract(method_Constructor)


def test_method_constructor_constructor_exists():
    assert callable(method_Constructor.__init__)


def test_method_constructor_constructor_args():
    sig = inspect.signature(method_Constructor.__init__)
    params = list(sig.parameters.keys())



def test_datatype_objecttype_is_not_abstract():
    assert not inspect.isabstract(datatype_ObjectType)


def test_datatype_objecttype_constructor_exists():
    assert callable(datatype_ObjectType.__init__)


def test_datatype_objecttype_constructor_args():
    sig = inspect.signature(datatype_ObjectType.__init__)
    params = list(sig.parameters.keys())



def test_complextype_is_not_abstract():
    assert not inspect.isabstract(ComplexType)


def test_complextype_constructor_exists():
    assert callable(ComplexType.__init__)


def test_complextype_constructor_args():
    sig = inspect.signature(ComplexType.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_complextype_anonymousclass_is_not_abstract():
    assert not inspect.isabstract(ccsl_complexType_AnonymousClass)


def test_ccsl_complextype_anonymousclass_constructor_exists():
    assert callable(ccsl_complexType_AnonymousClass.__init__)


def test_ccsl_complextype_anonymousclass_constructor_args():
    sig = inspect.signature(ccsl_complexType_AnonymousClass.__init__)
    params = list(sig.parameters.keys())



def test_complextype_complextype_is_not_abstract():
    assert not inspect.isabstract(complexType_ComplexType)


def test_complextype_complextype_constructor_exists():
    assert callable(complexType_ComplexType.__init__)


def test_complextype_complextype_constructor_args():
    sig = inspect.signature(complexType_ComplexType.__init__)
    params = list(sig.parameters.keys())



def test_variable_initializablevariable_is_not_abstract():
    assert not inspect.isabstract(variable_InitializableVariable)


def test_variable_initializablevariable_constructor_exists():
    assert callable(variable_InitializableVariable.__init__)


def test_variable_initializablevariable_constructor_args():
    sig = inspect.signature(variable_InitializableVariable.__init__)
    params = list(sig.parameters.keys())



def test_statements_statement_is_not_abstract():
    assert not inspect.isabstract(statements_Statement)


def test_statements_statement_constructor_exists():
    assert callable(statements_Statement.__init__)


def test_statements_statement_constructor_args():
    sig = inspect.signature(statements_Statement.__init__)
    params = list(sig.parameters.keys())



def test_declaredtype_is_not_abstract():
    assert not inspect.isabstract(DeclaredType)


def test_declaredtype_constructor_exists():
    assert callable(DeclaredType.__init__)


def test_declaredtype_constructor_args():
    sig = inspect.signature(DeclaredType.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_complextype_annotationtype_is_not_abstract():
    assert not inspect.isabstract(ccsl_complexType_AnnotationType)


def test_ccsl_complextype_annotationtype_constructor_exists():
    assert callable(ccsl_complexType_AnnotationType.__init__)


def test_ccsl_complextype_annotationtype_constructor_args():
    sig = inspect.signature(ccsl_complexType_AnnotationType.__init__)
    params = list(sig.parameters.keys())



def test_method_method_is_not_abstract():
    assert not inspect.isabstract(method_Method)


def test_method_method_constructor_exists():
    assert callable(method_Method.__init__)


def test_method_method_constructor_args():
    sig = inspect.signature(method_Method.__init__)
    params = list(sig.parameters.keys())



def test_variable_fieldvariable_is_not_abstract():
    assert not inspect.isabstract(variable_FieldVariable)


def test_variable_fieldvariable_constructor_exists():
    assert callable(variable_FieldVariable.__init__)


def test_variable_fieldvariable_constructor_args():
    sig = inspect.signature(variable_FieldVariable.__init__)
    params = list(sig.parameters.keys())



def test_import_importstatement_is_not_abstract():
    assert not inspect.isabstract(import_ImportStatement)


def test_import_importstatement_constructor_exists():
    assert callable(import_ImportStatement.__init__)


def test_import_importstatement_constructor_args():
    sig = inspect.signature(import_ImportStatement.__init__)
    params = list(sig.parameters.keys())



def test_complextype_jinterface_is_not_abstract():
    assert not inspect.isabstract(complexType_JInterface)


def test_complextype_jinterface_constructor_exists():
    assert callable(complexType_JInterface.__init__)


def test_complextype_jinterface_constructor_args():
    sig = inspect.signature(complexType_JInterface.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_elements_element_is_not_abstract():
    assert not inspect.isabstract(ccsl_elements_Element)


def test_ccsl_elements_element_constructor_exists():
    assert callable(ccsl_elements_Element.__init__)


def test_ccsl_elements_element_constructor_args():
    sig = inspect.signature(ccsl_elements_Element.__init__)
    params = list(sig.parameters.keys())
    assert "uniqueName" in params, "Missing parameter 'uniqueName'"

def test_ccsl_elements_element_has_uniqueName():
    assert hasattr(ccsl_elements_Element, "uniqueName")
    descriptor = None
    for klass in ccsl_elements_Element.__mro__:
        if "uniqueName" in klass.__dict__:
            descriptor = klass.__dict__["uniqueName"]
            break
    assert isinstance(descriptor, property)



def test_injectionstrategy_is_not_abstract():
    assert not inspect.isabstract(InjectionStrategy)


def test_injectionstrategy_constructor_exists():
    assert callable(InjectionStrategy.__init__)


def test_injectionstrategy_constructor_args():
    sig = inspect.signature(InjectionStrategy.__init__)
    params = list(sig.parameters.keys())



def test_injectionaction_is_not_abstract():
    assert not inspect.isabstract(InjectionAction)


def test_injectionaction_constructor_exists():
    assert callable(InjectionAction.__init__)


def test_injectionaction_constructor_args():
    sig = inspect.signature(InjectionAction.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_root_is_not_abstract():
    assert not inspect.isabstract(ccsl_Root)


def test_ccsl_root_constructor_exists():
    assert callable(ccsl_Root.__init__)


def test_ccsl_root_constructor_args():
    sig = inspect.signature(ccsl_Root.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_variable_initializablevariable_is_not_abstract():
    assert not inspect.isabstract(ccsl_variable_InitializableVariable)


def test_ccsl_variable_initializablevariable_constructor_exists():
    assert callable(ccsl_variable_InitializableVariable.__init__)


def test_ccsl_variable_initializablevariable_constructor_args():
    sig = inspect.signature(ccsl_variable_InitializableVariable.__init__)
    params = list(sig.parameters.keys())



def test_initializablevariable_is_not_abstract():
    assert not inspect.isabstract(InitializableVariable)


def test_initializablevariable_constructor_exists():
    assert callable(InitializableVariable.__init__)


def test_initializablevariable_constructor_args():
    sig = inspect.signature(InitializableVariable.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_variable_localvariable_is_not_abstract():
    assert not inspect.isabstract(ccsl_variable_LocalVariable)


def test_ccsl_variable_localvariable_constructor_exists():
    assert callable(ccsl_variable_LocalVariable.__init__)


def test_ccsl_variable_localvariable_constructor_args():
    sig = inspect.signature(ccsl_variable_LocalVariable.__init__)
    params = list(sig.parameters.keys())



def test_annotation_annotableelement_is_not_abstract():
    assert not inspect.isabstract(annotation_AnnotableElement)


def test_annotation_annotableelement_constructor_exists():
    assert callable(annotation_AnnotableElement.__init__)


def test_annotation_annotableelement_constructor_args():
    sig = inspect.signature(annotation_AnnotableElement.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_variable_fieldvariable_is_not_abstract():
    assert not inspect.isabstract(ccsl_variable_FieldVariable)


def test_ccsl_variable_fieldvariable_constructor_exists():
    assert callable(ccsl_variable_FieldVariable.__init__)


def test_ccsl_variable_fieldvariable_constructor_args():
    sig = inspect.signature(ccsl_variable_FieldVariable.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_ccsl_variable_fieldvariable_has_static():
    assert hasattr(ccsl_variable_FieldVariable, "static")
    descriptor = None
    for klass in ccsl_variable_FieldVariable.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_ccsl_variable_fieldvariable_has_visibility():
    assert hasattr(ccsl_variable_FieldVariable, "visibility")
    descriptor = None
    for klass in ccsl_variable_FieldVariable.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_ccsl_method_simplemethod_is_not_abstract():
    assert not inspect.isabstract(ccsl_method_SimpleMethod)


def test_ccsl_method_simplemethod_constructor_exists():
    assert callable(ccsl_method_SimpleMethod.__init__)


def test_ccsl_method_simplemethod_constructor_args():
    sig = inspect.signature(ccsl_method_SimpleMethod.__init__)
    params = list(sig.parameters.keys())
    assert "paramsKind" in params, "Missing parameter 'paramsKind'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_ccsl_method_simplemethod_has_paramsKind():
    assert hasattr(ccsl_method_SimpleMethod, "paramsKind")
    descriptor = None
    for klass in ccsl_method_SimpleMethod.__mro__:
        if "paramsKind" in klass.__dict__:
            descriptor = klass.__dict__["paramsKind"]
            break
    assert isinstance(descriptor, property)

def test_ccsl_method_simplemethod_has_visibility():
    assert hasattr(ccsl_method_SimpleMethod, "visibility")
    descriptor = None
    for klass in ccsl_method_SimpleMethod.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_variable_variable_is_not_abstract():
    assert not inspect.isabstract(variable_Variable)


def test_variable_variable_constructor_exists():
    assert callable(variable_Variable.__init__)


def test_variable_variable_constructor_args():
    sig = inspect.signature(variable_Variable.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_variable_parametervariable_is_not_abstract():
    assert not inspect.isabstract(ccsl_variable_ParameterVariable)


def test_ccsl_variable_parametervariable_constructor_exists():
    assert callable(ccsl_variable_ParameterVariable.__init__)


def test_ccsl_variable_parametervariable_constructor_args():
    sig = inspect.signature(ccsl_variable_ParameterVariable.__init__)
    params = list(sig.parameters.keys())



def test_datatype_datatype_is_not_abstract():
    assert not inspect.isabstract(datatype_DataType)


def test_datatype_datatype_constructor_exists():
    assert callable(datatype_DataType.__init__)


def test_datatype_datatype_constructor_args():
    sig = inspect.signature(datatype_DataType.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_variable_variable_is_not_abstract():
    assert not inspect.isabstract(ccsl_variable_Variable)


def test_ccsl_variable_variable_constructor_exists():
    assert callable(ccsl_variable_Variable.__init__)


def test_ccsl_variable_variable_constructor_args():
    sig = inspect.signature(ccsl_variable_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "final" in params, "Missing parameter 'final'"

def test_ccsl_variable_variable_has_final():
    assert hasattr(ccsl_variable_Variable, "final")
    descriptor = None
    for klass in ccsl_variable_Variable.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)



def test_complextype_declaredtype_is_not_abstract():
    assert not inspect.isabstract(complexType_DeclaredType)


def test_complextype_declaredtype_constructor_exists():
    assert callable(complexType_DeclaredType.__init__)


def test_complextype_declaredtype_constructor_args():
    sig = inspect.signature(complexType_DeclaredType.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_complextype_jclass_is_not_abstract():
    assert not inspect.isabstract(ccsl_complexType_JClass)


def test_ccsl_complextype_jclass_constructor_exists():
    assert callable(ccsl_complexType_JClass.__init__)


def test_ccsl_complextype_jclass_constructor_args():
    sig = inspect.signature(ccsl_complexType_JClass.__init__)
    params = list(sig.parameters.keys())
    assert "inheritance" in params, "Missing parameter 'inheritance'"

def test_ccsl_complextype_jclass_has_inheritance():
    assert hasattr(ccsl_complexType_JClass, "inheritance")
    descriptor = None
    for klass in ccsl_complexType_JClass.__mro__:
        if "inheritance" in klass.__dict__:
            descriptor = klass.__dict__["inheritance"]
            break
    assert isinstance(descriptor, property)



def test_ccsl_complextype_jinterface_is_not_abstract():
    assert not inspect.isabstract(ccsl_complexType_JInterface)


def test_ccsl_complextype_jinterface_constructor_exists():
    assert callable(ccsl_complexType_JInterface.__init__)


def test_ccsl_complextype_jinterface_constructor_args():
    sig = inspect.signature(ccsl_complexType_JInterface.__init__)
    params = list(sig.parameters.keys())



def test_import_importableelement_is_not_abstract():
    assert not inspect.isabstract(import_ImportableElement)


def test_import_importableelement_constructor_exists():
    assert callable(import_ImportableElement.__init__)


def test_import_importableelement_constructor_args():
    sig = inspect.signature(import_ImportableElement.__init__)
    params = list(sig.parameters.keys())



def test_namedelements_namedelement_is_not_abstract():
    assert not inspect.isabstract(namedElements_NamedElement)


def test_namedelements_namedelement_constructor_exists():
    assert callable(namedElements_NamedElement.__init__)


def test_namedelements_namedelement_constructor_args():
    sig = inspect.signature(namedElements_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_method_method_is_not_abstract():
    assert not inspect.isabstract(ccsl_method_Method)


def test_ccsl_method_method_constructor_exists():
    assert callable(ccsl_method_Method.__init__)


def test_ccsl_method_method_constructor_args():
    sig = inspect.signature(ccsl_method_Method.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "static" in params, "Missing parameter 'static'"
    assert "final" in params, "Missing parameter 'final'"
    assert "inheritance" in params, "Missing parameter 'inheritance'"

def test_ccsl_method_method_has_abstract():
    assert hasattr(ccsl_method_Method, "abstract")
    descriptor = None
    for klass in ccsl_method_Method.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_ccsl_method_method_has_static():
    assert hasattr(ccsl_method_Method, "static")
    descriptor = None
    for klass in ccsl_method_Method.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_ccsl_method_method_has_final():
    assert hasattr(ccsl_method_Method, "final")
    descriptor = None
    for klass in ccsl_method_Method.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)

def test_ccsl_method_method_has_inheritance():
    assert hasattr(ccsl_method_Method, "inheritance")
    descriptor = None
    for klass in ccsl_method_Method.__mro__:
        if "inheritance" in klass.__dict__:
            descriptor = klass.__dict__["inheritance"]
            break
    assert isinstance(descriptor, property)



def test_ccsl_complextype_declaredtype_is_not_abstract():
    assert not inspect.isabstract(ccsl_complexType_DeclaredType)


def test_ccsl_complextype_declaredtype_constructor_exists():
    assert callable(ccsl_complexType_DeclaredType.__init__)


def test_ccsl_complextype_declaredtype_constructor_args():
    sig = inspect.signature(ccsl_complexType_DeclaredType.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_ccsl_complextype_declaredtype_has_static():
    assert hasattr(ccsl_complexType_DeclaredType, "static")
    descriptor = None
    for klass in ccsl_complexType_DeclaredType.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_ccsl_complextype_declaredtype_has_visibility():
    assert hasattr(ccsl_complexType_DeclaredType, "visibility")
    descriptor = None
    for klass in ccsl_complexType_DeclaredType.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_ccsl_namedelements_package_is_not_abstract():
    assert not inspect.isabstract(ccsl_namedElements_Package)


def test_ccsl_namedelements_package_constructor_exists():
    assert callable(ccsl_namedElements_Package.__init__)


def test_ccsl_namedelements_package_constructor_args():
    sig = inspect.signature(ccsl_namedElements_Package.__init__)
    params = list(sig.parameters.keys())



def test_context_is_not_abstract():
    assert not inspect.isabstract(Context)


def test_context_constructor_exists():
    assert callable(Context.__init__)


def test_context_constructor_args():
    sig = inspect.signature(Context.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_complextype_complextype_is_not_abstract():
    assert not inspect.isabstract(ccsl_complexType_ComplexType)


def test_ccsl_complextype_complextype_constructor_exists():
    assert callable(ccsl_complexType_ComplexType.__init__)


def test_ccsl_complextype_complextype_constructor_args():
    sig = inspect.signature(ccsl_complexType_ComplexType.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_namedelements_namedelement_is_not_abstract():
    assert not inspect.isabstract(ccsl_namedElements_NamedElement)


def test_ccsl_namedelements_namedelement_constructor_exists():
    assert callable(ccsl_namedElements_NamedElement.__init__)


def test_ccsl_namedelements_namedelement_constructor_args():
    sig = inspect.signature(ccsl_namedElements_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "avaliableInSourceCode" in params, "Missing parameter 'avaliableInSourceCode'"

def test_ccsl_namedelements_namedelement_has_name():
    assert hasattr(ccsl_namedElements_NamedElement, "name")
    descriptor = None
    for klass in ccsl_namedElements_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ccsl_namedelements_namedelement_has_avaliableInSourceCode():
    assert hasattr(ccsl_namedElements_NamedElement, "avaliableInSourceCode")
    descriptor = None
    for klass in ccsl_namedElements_NamedElement.__mro__:
        if "avaliableInSourceCode" in klass.__dict__:
            descriptor = klass.__dict__["avaliableInSourceCode"]
            break
    assert isinstance(descriptor, property)



def test_ccsl_annotation_annotableelement_is_not_abstract():
    assert not inspect.isabstract(ccsl_annotation_AnnotableElement)


def test_ccsl_annotation_annotableelement_constructor_exists():
    assert callable(ccsl_annotation_AnnotableElement.__init__)


def test_ccsl_annotation_annotableelement_constructor_args():
    sig = inspect.signature(ccsl_annotation_AnnotableElement.__init__)
    params = list(sig.parameters.keys())
    assert "annotationsKind" in params, "Missing parameter 'annotationsKind'"

def test_ccsl_annotation_annotableelement_has_annotationsKind():
    assert hasattr(ccsl_annotation_AnnotableElement, "annotationsKind")
    descriptor = None
    for klass in ccsl_annotation_AnnotableElement.__mro__:
        if "annotationsKind" in klass.__dict__:
            descriptor = klass.__dict__["annotationsKind"]
            break
    assert isinstance(descriptor, property)



def test_ccsl_datatype_datatype_is_not_abstract():
    assert not inspect.isabstract(ccsl_datatype_DataType)


def test_ccsl_datatype_datatype_constructor_exists():
    assert callable(ccsl_datatype_DataType.__init__)


def test_ccsl_datatype_datatype_constructor_args():
    sig = inspect.signature(ccsl_datatype_DataType.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_statements_statement_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_Statement)


def test_ccsl_statements_statement_constructor_exists():
    assert callable(ccsl_statements_Statement.__init__)


def test_ccsl_statements_statement_constructor_args():
    sig = inspect.signature(ccsl_statements_Statement.__init__)
    params = list(sig.parameters.keys())



def test_rule_is_not_abstract():
    assert not inspect.isabstract(Rule)


def test_rule_constructor_exists():
    assert callable(Rule.__init__)


def test_rule_constructor_args():
    sig = inspect.signature(Rule.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_atomicrule_is_not_abstract():
    assert not inspect.isabstract(ccsl_AtomicRule)


def test_ccsl_atomicrule_constructor_exists():
    assert callable(ccsl_AtomicRule.__init__)


def test_ccsl_atomicrule_constructor_args():
    sig = inspect.signature(ccsl_AtomicRule.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_compositerule_is_not_abstract():
    assert not inspect.isabstract(ccsl_CompositeRule)


def test_ccsl_compositerule_constructor_exists():
    assert callable(ccsl_CompositeRule.__init__)


def test_ccsl_compositerule_constructor_args():
    sig = inspect.signature(ccsl_CompositeRule.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ccsl_compositerule_has_operator():
    assert hasattr(ccsl_CompositeRule, "operator")
    descriptor = None
    for klass in ccsl_CompositeRule.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_root_is_not_abstract():
    assert not inspect.isabstract(Root)


def test_root_constructor_exists():
    assert callable(Root.__init__)


def test_root_constructor_args():
    sig = inspect.signature(Root.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_faulttypedescription_is_not_abstract():
    assert not inspect.isabstract(ccsl_FaultTypeDescription)


def test_ccsl_faulttypedescription_constructor_exists():
    assert callable(ccsl_FaultTypeDescription.__init__)


def test_ccsl_faulttypedescription_constructor_args():
    sig = inspect.signature(ccsl_FaultTypeDescription.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ccsl_faulttypedescription_has_name():
    assert hasattr(ccsl_FaultTypeDescription, "name")
    descriptor = None
    for klass in ccsl_FaultTypeDescription.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ccsl_rule_is_not_abstract():
    assert not inspect.isabstract(ccsl_Rule)


def test_ccsl_rule_constructor_exists():
    assert callable(ccsl_Rule.__init__)


def test_ccsl_rule_constructor_args():
    sig = inspect.signature(ccsl_Rule.__init__)
    params = list(sig.parameters.keys())
    assert "negated" in params, "Missing parameter 'negated'"

def test_ccsl_rule_has_negated():
    assert hasattr(ccsl_Rule, "negated")
    descriptor = None
    for klass in ccsl_Rule.__mro__:
        if "negated" in klass.__dict__:
            descriptor = klass.__dict__["negated"]
            break
    assert isinstance(descriptor, property)



def test_statements_access_is_not_abstract():
    assert not inspect.isabstract(statements_Access)


def test_statements_access_constructor_exists():
    assert callable(statements_Access.__init__)


def test_statements_access_constructor_args():
    sig = inspect.signature(statements_Access.__init__)
    params = list(sig.parameters.keys())



def test_ccslnumberfunction_is_not_abstract():
    assert not inspect.isabstract(CcslNumberFunction)


def test_ccslnumberfunction_constructor_exists():
    assert callable(CcslNumberFunction.__init__)


def test_ccslnumberfunction_constructor_args():
    sig = inspect.signature(CcslNumberFunction.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_numberfunctions_getindexof_is_not_abstract():
    assert not inspect.isabstract(ccsl_numberFunctions_GetIndexOf)


def test_ccsl_numberfunctions_getindexof_constructor_exists():
    assert callable(ccsl_numberFunctions_GetIndexOf.__init__)


def test_ccsl_numberfunctions_getindexof_constructor_args():
    sig = inspect.signature(ccsl_numberFunctions_GetIndexOf.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_numberfunctions_ccslintegerliteral_is_not_abstract():
    assert not inspect.isabstract(ccsl_numberFunctions_CcslIntegerLiteral)


def test_ccsl_numberfunctions_ccslintegerliteral_constructor_exists():
    assert callable(ccsl_numberFunctions_CcslIntegerLiteral.__init__)


def test_ccsl_numberfunctions_ccslintegerliteral_constructor_args():
    sig = inspect.signature(ccsl_numberFunctions_CcslIntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ccsl_numberfunctions_ccslintegerliteral_has_value():
    assert hasattr(ccsl_numberFunctions_CcslIntegerLiteral, "value")
    descriptor = None
    for klass in ccsl_numberFunctions_CcslIntegerLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_numberfunctions_ccslnumberfunction_is_not_abstract():
    assert not inspect.isabstract(numberFunctions_CcslNumberFunction)


def test_numberfunctions_ccslnumberfunction_constructor_exists():
    assert callable(numberFunctions_CcslNumberFunction.__init__)


def test_numberfunctions_ccslnumberfunction_constructor_args():
    sig = inspect.signature(numberFunctions_CcslNumberFunction.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_filters_equationfilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_EquationFilter)


def test_ccsl_filters_equationfilter_constructor_exists():
    assert callable(ccsl_filters_EquationFilter.__init__)


def test_ccsl_filters_equationfilter_constructor_args():
    sig = inspect.signature(ccsl_filters_EquationFilter.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ccsl_filters_equationfilter_has_operator():
    assert hasattr(ccsl_filters_EquationFilter, "operator")
    descriptor = None
    for klass in ccsl_filters_EquationFilter.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_atomicfilter_is_not_abstract():
    assert not inspect.isabstract(AtomicFilter)


def test_atomicfilter_constructor_exists():
    assert callable(AtomicFilter.__init__)


def test_atomicfilter_constructor_args():
    sig = inspect.signature(AtomicFilter.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_filters_samenamefilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_SameNameFilter)


def test_ccsl_filters_samenamefilter_constructor_exists():
    assert callable(ccsl_filters_SameNameFilter.__init__)


def test_ccsl_filters_samenamefilter_constructor_args():
    sig = inspect.signature(ccsl_filters_SameNameFilter.__init__)
    params = list(sig.parameters.keys())
    assert "ignoreCase" in params, "Missing parameter 'ignoreCase'"

def test_ccsl_filters_samenamefilter_has_ignoreCase():
    assert hasattr(ccsl_filters_SameNameFilter, "ignoreCase")
    descriptor = None
    for klass in ccsl_filters_SameNameFilter.__mro__:
        if "ignoreCase" in klass.__dict__:
            descriptor = klass.__dict__["ignoreCase"]
            break
    assert isinstance(descriptor, property)



def test_ccsl_filters_hassamereferencefilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_HasSameReferenceFilter)


def test_ccsl_filters_hassamereferencefilter_constructor_exists():
    assert callable(ccsl_filters_HasSameReferenceFilter.__init__)


def test_ccsl_filters_hassamereferencefilter_constructor_args():
    sig = inspect.signature(ccsl_filters_HasSameReferenceFilter.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_filters_iskindoffilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_IsKindOfFilter)


def test_ccsl_filters_iskindoffilter_constructor_exists():
    assert callable(ccsl_filters_IsKindOfFilter.__init__)


def test_ccsl_filters_iskindoffilter_constructor_args():
    sig = inspect.signature(ccsl_filters_IsKindOfFilter.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_filters_superclassclosurefilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_SuperClassClosureFilter)


def test_ccsl_filters_superclassclosurefilter_constructor_exists():
    assert callable(ccsl_filters_SuperClassClosureFilter.__init__)


def test_ccsl_filters_superclassclosurefilter_constructor_args():
    sig = inspect.signature(ccsl_filters_SuperClassClosureFilter.__init__)
    params = list(sig.parameters.keys())
    assert "includesSubClass" in params, "Missing parameter 'includesSubClass'"

def test_ccsl_filters_superclassclosurefilter_has_includesSubClass():
    assert hasattr(ccsl_filters_SuperClassClosureFilter, "includesSubClass")
    descriptor = None
    for klass in ccsl_filters_SuperClassClosureFilter.__mro__:
        if "includesSubClass" in klass.__dict__:
            descriptor = klass.__dict__["includesSubClass"]
            break
    assert isinstance(descriptor, property)



def test_ccsl_filters_isstringfilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_IsStringFilter)


def test_ccsl_filters_isstringfilter_constructor_exists():
    assert callable(ccsl_filters_IsStringFilter.__init__)


def test_ccsl_filters_isstringfilter_constructor_args():
    sig = inspect.signature(ccsl_filters_IsStringFilter.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_filters_blocklaststatementfilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_BlockLastStatementFilter)


def test_ccsl_filters_blocklaststatementfilter_constructor_exists():
    assert callable(ccsl_filters_BlockLastStatementFilter.__init__)


def test_ccsl_filters_blocklaststatementfilter_constructor_args():
    sig = inspect.signature(ccsl_filters_BlockLastStatementFilter.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_filters_templatefilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_TemplateFilter)


def test_ccsl_filters_templatefilter_constructor_exists():
    assert callable(ccsl_filters_TemplateFilter.__init__)


def test_ccsl_filters_templatefilter_constructor_args():
    sig = inspect.signature(ccsl_filters_TemplateFilter.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_filters_childclosurecomplextypefilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_ChildClosureComplexTypeFilter)


def test_ccsl_filters_childclosurecomplextypefilter_constructor_exists():
    assert callable(ccsl_filters_ChildClosureComplexTypeFilter.__init__)


def test_ccsl_filters_childclosurecomplextypefilter_constructor_args():
    sig = inspect.signature(ccsl_filters_ChildClosureComplexTypeFilter.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_filters_fromclosurefilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_FromClosureFilter)


def test_ccsl_filters_fromclosurefilter_constructor_exists():
    assert callable(ccsl_filters_FromClosureFilter.__init__)


def test_ccsl_filters_fromclosurefilter_constructor_args():
    sig = inspect.signature(ccsl_filters_FromClosureFilter.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_filters_supermethodclosurefilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_SuperMethodClosureFilter)


def test_ccsl_filters_supermethodclosurefilter_constructor_exists():
    assert callable(ccsl_filters_SuperMethodClosureFilter.__init__)


def test_ccsl_filters_supermethodclosurefilter_constructor_args():
    sig = inspect.signature(ccsl_filters_SuperMethodClosureFilter.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_filters_istypeoffilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_IsTypeOfFilter)


def test_ccsl_filters_istypeoffilter_constructor_exists():
    assert callable(ccsl_filters_IsTypeOfFilter.__init__)


def test_ccsl_filters_istypeoffilter_constructor_args():
    sig = inspect.signature(ccsl_filters_IsTypeOfFilter.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_filters_propertyfilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_PropertyFilter)


def test_ccsl_filters_propertyfilter_constructor_exists():
    assert callable(ccsl_filters_PropertyFilter.__init__)


def test_ccsl_filters_propertyfilter_constructor_args():
    sig = inspect.signature(ccsl_filters_PropertyFilter.__init__)
    params = list(sig.parameters.keys())



def test_filter_is_not_abstract():
    assert not inspect.isabstract(Filter)


def test_filter_constructor_exists():
    assert callable(Filter.__init__)


def test_filter_constructor_args():
    sig = inspect.signature(Filter.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_filters_compositefilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_CompositeFilter)


def test_ccsl_filters_compositefilter_constructor_exists():
    assert callable(ccsl_filters_CompositeFilter.__init__)


def test_ccsl_filters_compositefilter_constructor_args():
    sig = inspect.signature(ccsl_filters_CompositeFilter.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ccsl_filters_compositefilter_has_operator():
    assert hasattr(ccsl_filters_CompositeFilter, "operator")
    descriptor = None
    for klass in ccsl_filters_CompositeFilter.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_ccsl_filters_atomicfilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_AtomicFilter)


def test_ccsl_filters_atomicfilter_constructor_exists():
    assert callable(ccsl_filters_AtomicFilter.__init__)


def test_ccsl_filters_atomicfilter_constructor_args():
    sig = inspect.signature(ccsl_filters_AtomicFilter.__init__)
    params = list(sig.parameters.keys())



def test_ccslbooleanfunction_is_not_abstract():
    assert not inspect.isabstract(CcslBooleanFunction)


def test_ccslbooleanfunction_constructor_exists():
    assert callable(CcslBooleanFunction.__init__)


def test_ccslbooleanfunction_constructor_args():
    sig = inspect.signature(CcslBooleanFunction.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_filters_filter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_Filter)


def test_ccsl_filters_filter_constructor_exists():
    assert callable(ccsl_filters_Filter.__init__)


def test_ccsl_filters_filter_constructor_args():
    sig = inspect.signature(ccsl_filters_Filter.__init__)
    params = list(sig.parameters.keys())
    assert "negated" in params, "Missing parameter 'negated'"

def test_ccsl_filters_filter_has_negated():
    assert hasattr(ccsl_filters_Filter, "negated")
    descriptor = None
    for klass in ccsl_filters_Filter.__mro__:
        if "negated" in klass.__dict__:
            descriptor = klass.__dict__["negated"]
            break
    assert isinstance(descriptor, property)



def test_ccslfunction_is_not_abstract():
    assert not inspect.isabstract(CcslFunction)


def test_ccslfunction_constructor_exists():
    assert callable(CcslFunction.__init__)


def test_ccslfunction_constructor_args():
    sig = inspect.signature(CcslFunction.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_numberfunctions_ccslnumberfunction_is_not_abstract():
    assert not inspect.isabstract(ccsl_numberFunctions_CcslNumberFunction)


def test_ccsl_numberfunctions_ccslnumberfunction_constructor_exists():
    assert callable(ccsl_numberFunctions_CcslNumberFunction.__init__)


def test_ccsl_numberfunctions_ccslnumberfunction_constructor_args():
    sig = inspect.signature(ccsl_numberFunctions_CcslNumberFunction.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_booleanfunctions_ccslbooleanfunction_is_not_abstract():
    assert not inspect.isabstract(ccsl_booleanFunctions_CcslBooleanFunction)


def test_ccsl_booleanfunctions_ccslbooleanfunction_constructor_exists():
    assert callable(ccsl_booleanFunctions_CcslBooleanFunction.__init__)


def test_ccsl_booleanfunctions_ccslbooleanfunction_constructor_args():
    sig = inspect.signature(ccsl_booleanFunctions_CcslBooleanFunction.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_filters_implicitycontainerfilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_ImplicityContainerFilter)


def test_ccsl_filters_implicitycontainerfilter_constructor_exists():
    assert callable(ccsl_filters_ImplicityContainerFilter.__init__)


def test_ccsl_filters_implicitycontainerfilter_constructor_args():
    sig = inspect.signature(ccsl_filters_ImplicityContainerFilter.__init__)
    params = list(sig.parameters.keys())



def test_expressions_operatorexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_OperatorExpression)


def test_expressions_operatorexpression_constructor_exists():
    assert callable(expressions_OperatorExpression.__init__)


def test_expressions_operatorexpression_constructor_args():
    sig = inspect.signature(expressions_OperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_templatefilter_is_not_abstract():
    assert not inspect.isabstract(TemplateFilter)


def test_templatefilter_constructor_exists():
    assert callable(TemplateFilter.__init__)


def test_templatefilter_constructor_args():
    sig = inspect.signature(TemplateFilter.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_filters_implicityoperandfilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_ImplicityOperandFilter)


def test_ccsl_filters_implicityoperandfilter_constructor_exists():
    assert callable(ccsl_filters_ImplicityOperandFilter.__init__)


def test_ccsl_filters_implicityoperandfilter_constructor_args():
    sig = inspect.signature(ccsl_filters_ImplicityOperandFilter.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_filters_regexmatch_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_RegexMatch)


def test_ccsl_filters_regexmatch_constructor_exists():
    assert callable(ccsl_filters_RegexMatch.__init__)


def test_ccsl_filters_regexmatch_constructor_args():
    sig = inspect.signature(ccsl_filters_RegexMatch.__init__)
    params = list(sig.parameters.keys())
    assert "regex" in params, "Missing parameter 'regex'"

def test_ccsl_filters_regexmatch_has_regex():
    assert hasattr(ccsl_filters_RegexMatch, "regex")
    descriptor = None
    for klass in ccsl_filters_RegexMatch.__mro__:
        if "regex" in klass.__dict__:
            descriptor = klass.__dict__["regex"]
            break
    assert isinstance(descriptor, property)



def test_ccsl_filters_countfilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_CountFilter)


def test_ccsl_filters_countfilter_constructor_exists():
    assert callable(ccsl_filters_CountFilter.__init__)


def test_ccsl_filters_countfilter_constructor_args():
    sig = inspect.signature(ccsl_filters_CountFilter.__init__)
    params = list(sig.parameters.keys())
    assert "min" in params, "Missing parameter 'min'"
    assert "max" in params, "Missing parameter 'max'"

def test_ccsl_filters_countfilter_has_min():
    assert hasattr(ccsl_filters_CountFilter, "min")
    descriptor = None
    for klass in ccsl_filters_CountFilter.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_ccsl_filters_countfilter_has_max():
    assert hasattr(ccsl_filters_CountFilter, "max")
    descriptor = None
    for klass in ccsl_filters_CountFilter.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)



def test_ccsl_faulttypedescription_injectionaction_is_not_abstract():
    assert not inspect.isabstract(ccsl_faultTypeDescription_InjectionAction)


def test_ccsl_faulttypedescription_injectionaction_constructor_exists():
    assert callable(ccsl_faultTypeDescription_InjectionAction.__init__)


def test_ccsl_faulttypedescription_injectionaction_constructor_args():
    sig = inspect.signature(ccsl_faultTypeDescription_InjectionAction.__init__)
    params = list(sig.parameters.keys())



def test_filters_filter_is_not_abstract():
    assert not inspect.isabstract(filters_Filter)


def test_filters_filter_constructor_exists():
    assert callable(filters_Filter.__init__)


def test_filters_filter_constructor_args():
    sig = inspect.signature(filters_Filter.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_context_context_is_not_abstract():
    assert not inspect.isabstract(ccsl_context_Context)


def test_ccsl_context_context_constructor_exists():
    assert callable(ccsl_context_Context.__init__)


def test_ccsl_context_context_constructor_args():
    sig = inspect.signature(ccsl_context_Context.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_datatype_voidtype_is_not_abstract():
    assert not inspect.isabstract(ccsl_datatype_VoidType)


def test_ccsl_datatype_voidtype_constructor_exists():
    assert callable(ccsl_datatype_VoidType.__init__)


def test_ccsl_datatype_voidtype_constructor_args():
    sig = inspect.signature(ccsl_datatype_VoidType.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_datatype_intprimitivetype_is_not_abstract():
    assert not inspect.isabstract(ccsl_datatype_IntPrimitiveType)


def test_ccsl_datatype_intprimitivetype_constructor_exists():
    assert callable(ccsl_datatype_IntPrimitiveType.__init__)


def test_ccsl_datatype_intprimitivetype_constructor_args():
    sig = inspect.signature(ccsl_datatype_IntPrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_datatype_generictype_is_not_abstract():
    assert not inspect.isabstract(ccsl_datatype_GenericType)


def test_ccsl_datatype_generictype_constructor_exists():
    assert callable(ccsl_datatype_GenericType.__init__)


def test_ccsl_datatype_generictype_constructor_args():
    sig = inspect.signature(ccsl_datatype_GenericType.__init__)
    params = list(sig.parameters.keys())



def test_objecttype_is_not_abstract():
    assert not inspect.isabstract(ObjectType)


def test_objecttype_constructor_exists():
    assert callable(ObjectType.__init__)


def test_objecttype_constructor_args():
    sig = inspect.signature(ObjectType.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_datatype_arraytype_is_not_abstract():
    assert not inspect.isabstract(ccsl_datatype_ArrayType)


def test_ccsl_datatype_arraytype_constructor_exists():
    assert callable(ccsl_datatype_ArrayType.__init__)


def test_ccsl_datatype_arraytype_constructor_args():
    sig = inspect.signature(ccsl_datatype_ArrayType.__init__)
    params = list(sig.parameters.keys())
    assert "dimensions" in params, "Missing parameter 'dimensions'"

def test_ccsl_datatype_arraytype_has_dimensions():
    assert hasattr(ccsl_datatype_ArrayType, "dimensions")
    descriptor = None
    for klass in ccsl_datatype_ArrayType.__mro__:
        if "dimensions" in klass.__dict__:
            descriptor = klass.__dict__["dimensions"]
            break
    assert isinstance(descriptor, property)



def test_ccsl_datatype_parameterizedtype_is_not_abstract():
    assert not inspect.isabstract(ccsl_datatype_ParameterizedType)


def test_ccsl_datatype_parameterizedtype_constructor_exists():
    assert callable(ccsl_datatype_ParameterizedType.__init__)


def test_ccsl_datatype_parameterizedtype_constructor_args():
    sig = inspect.signature(ccsl_datatype_ParameterizedType.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_datatype_objecttype_is_not_abstract():
    assert not inspect.isabstract(ccsl_datatype_ObjectType)


def test_ccsl_datatype_objecttype_constructor_exists():
    assert callable(ccsl_datatype_ObjectType.__init__)


def test_ccsl_datatype_objecttype_constructor_args():
    sig = inspect.signature(ccsl_datatype_ObjectType.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_functions_ccslfunction_is_not_abstract():
    assert not inspect.isabstract(ccsl_functions_CcslFunction)


def test_ccsl_functions_ccslfunction_constructor_exists():
    assert callable(ccsl_functions_CcslFunction.__init__)


def test_ccsl_functions_ccslfunction_constructor_args():
    sig = inspect.signature(ccsl_functions_CcslFunction.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_strategy_allstrategy_is_not_abstract():
    assert not inspect.isabstract(ccsl_strategy_AllStrategy)


def test_ccsl_strategy_allstrategy_constructor_exists():
    assert callable(ccsl_strategy_AllStrategy.__init__)


def test_ccsl_strategy_allstrategy_constructor_args():
    sig = inspect.signature(ccsl_strategy_AllStrategy.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_action_arithmeticoperatormap_is_not_abstract():
    assert not inspect.isabstract(ccsl_action_ArithmeticOperatorMap)


def test_ccsl_action_arithmeticoperatormap_constructor_exists():
    assert callable(ccsl_action_ArithmeticOperatorMap.__init__)


def test_ccsl_action_arithmeticoperatormap_constructor_args():
    sig = inspect.signature(ccsl_action_ArithmeticOperatorMap.__init__)
    params = list(sig.parameters.keys())
    assert "oldArithmeticOperator" in params, "Missing parameter 'oldArithmeticOperator'"
    assert "newArithmeticOperator" in params, "Missing parameter 'newArithmeticOperator'"

def test_ccsl_action_arithmeticoperatormap_has_oldArithmeticOperator():
    assert hasattr(ccsl_action_ArithmeticOperatorMap, "oldArithmeticOperator")
    descriptor = None
    for klass in ccsl_action_ArithmeticOperatorMap.__mro__:
        if "oldArithmeticOperator" in klass.__dict__:
            descriptor = klass.__dict__["oldArithmeticOperator"]
            break
    assert isinstance(descriptor, property)

def test_ccsl_action_arithmeticoperatormap_has_newArithmeticOperator():
    assert hasattr(ccsl_action_ArithmeticOperatorMap, "newArithmeticOperator")
    descriptor = None
    for klass in ccsl_action_ArithmeticOperatorMap.__mro__:
        if "newArithmeticOperator" in klass.__dict__:
            descriptor = klass.__dict__["newArithmeticOperator"]
            break
    assert isinstance(descriptor, property)



def test_action_arithmeticoperatormap_is_not_abstract():
    assert not inspect.isabstract(action_ArithmeticOperatorMap)


def test_action_arithmeticoperatormap_constructor_exists():
    assert callable(action_ArithmeticOperatorMap.__init__)


def test_action_arithmeticoperatormap_constructor_args():
    sig = inspect.signature(action_ArithmeticOperatorMap.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_action_replacearithmeticoperatoraction_is_not_abstract():
    assert not inspect.isabstract(ccsl_action_ReplaceArithmeticOperatorAction)


def test_ccsl_action_replacearithmeticoperatoraction_constructor_exists():
    assert callable(ccsl_action_ReplaceArithmeticOperatorAction.__init__)


def test_ccsl_action_replacearithmeticoperatoraction_constructor_args():
    sig = inspect.signature(ccsl_action_ReplaceArithmeticOperatorAction.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_action_replacevariableaccessaction_is_not_abstract():
    assert not inspect.isabstract(ccsl_action_ReplaceVariableAccessAction)


def test_ccsl_action_replacevariableaccessaction_constructor_exists():
    assert callable(ccsl_action_ReplaceVariableAccessAction.__init__)


def test_ccsl_action_replacevariableaccessaction_constructor_args():
    sig = inspect.signature(ccsl_action_ReplaceVariableAccessAction.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_action_deleterandomstatementaction_is_not_abstract():
    assert not inspect.isabstract(ccsl_action_DeleteRandomStatementAction)


def test_ccsl_action_deleterandomstatementaction_constructor_exists():
    assert callable(ccsl_action_DeleteRandomStatementAction.__init__)


def test_ccsl_action_deleterandomstatementaction_constructor_args():
    sig = inspect.signature(ccsl_action_DeleteRandomStatementAction.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_action_changeliteralvalueaction_is_not_abstract():
    assert not inspect.isabstract(ccsl_action_ChangeLiteralValueAction)


def test_ccsl_action_changeliteralvalueaction_constructor_exists():
    assert callable(ccsl_action_ChangeLiteralValueAction.__init__)


def test_ccsl_action_changeliteralvalueaction_constructor_args():
    sig = inspect.signature(ccsl_action_ChangeLiteralValueAction.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_action_deleteinfixoperatoraction_is_not_abstract():
    assert not inspect.isabstract(ccsl_action_DeleteInfixOperatorAction)


def test_ccsl_action_deleteinfixoperatoraction_constructor_exists():
    assert callable(ccsl_action_DeleteInfixOperatorAction.__init__)


def test_ccsl_action_deleteinfixoperatoraction_constructor_args():
    sig = inspect.signature(ccsl_action_DeleteInfixOperatorAction.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_action_movescopeupaction_is_not_abstract():
    assert not inspect.isabstract(ccsl_action_MoveScopeUpAction)


def test_ccsl_action_movescopeupaction_constructor_exists():
    assert callable(ccsl_action_MoveScopeUpAction.__init__)


def test_ccsl_action_movescopeupaction_constructor_args():
    sig = inspect.signature(ccsl_action_MoveScopeUpAction.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_action_deleteaction_is_not_abstract():
    assert not inspect.isabstract(ccsl_action_DeleteAction)


def test_ccsl_action_deleteaction_constructor_exists():
    assert callable(ccsl_action_DeleteAction.__init__)


def test_ccsl_action_deleteaction_constructor_args():
    sig = inspect.signature(ccsl_action_DeleteAction.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_faulttypedescription_injectionstrategy_is_not_abstract():
    assert not inspect.isabstract(ccsl_faultTypeDescription_InjectionStrategy)


def test_ccsl_faulttypedescription_injectionstrategy_constructor_exists():
    assert callable(ccsl_faultTypeDescription_InjectionStrategy.__init__)


def test_ccsl_faulttypedescription_injectionstrategy_constructor_args():
    sig = inspect.signature(ccsl_faultTypeDescription_InjectionStrategy.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_import_importstatement_is_not_abstract():
    assert not inspect.isabstract(ccsl_import_ImportStatement)


def test_ccsl_import_importstatement_constructor_exists():
    assert callable(ccsl_import_ImportStatement.__init__)


def test_ccsl_import_importstatement_constructor_args():
    sig = inspect.signature(ccsl_import_ImportStatement.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_import_importableelement_is_not_abstract():
    assert not inspect.isabstract(ccsl_import_ImportableElement)


def test_ccsl_import_importableelement_constructor_exists():
    assert callable(ccsl_import_ImportableElement.__init__)


def test_ccsl_import_importableelement_constructor_args():
    sig = inspect.signature(ccsl_import_ImportableElement.__init__)
    params = list(sig.parameters.keys())



def test_invocation_is_not_abstract():
    assert not inspect.isabstract(Invocation)


def test_invocation_constructor_exists():
    assert callable(Invocation.__init__)


def test_invocation_constructor_args():
    sig = inspect.signature(Invocation.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_invocation_simplemethodinvocation_is_not_abstract():
    assert not inspect.isabstract(ccsl_invocation_SimpleMethodInvocation)


def test_ccsl_invocation_simplemethodinvocation_constructor_exists():
    assert callable(ccsl_invocation_SimpleMethodInvocation.__init__)


def test_ccsl_invocation_simplemethodinvocation_constructor_args():
    sig = inspect.signature(ccsl_invocation_SimpleMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_invocation_constructorinvocation_is_not_abstract():
    assert not inspect.isabstract(ccsl_invocation_ConstructorInvocation)


def test_ccsl_invocation_constructorinvocation_constructor_exists():
    assert callable(ccsl_invocation_ConstructorInvocation.__init__)


def test_ccsl_invocation_constructorinvocation_constructor_args():
    sig = inspect.signature(ccsl_invocation_ConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_invocation_invocation_is_not_abstract():
    assert not inspect.isabstract(ccsl_invocation_Invocation)


def test_ccsl_invocation_invocation_constructor_exists():
    assert callable(ccsl_invocation_Invocation.__init__)


def test_ccsl_invocation_invocation_constructor_args():
    sig = inspect.signature(ccsl_invocation_Invocation.__init__)
    params = list(sig.parameters.keys())
    assert "argsKind" in params, "Missing parameter 'argsKind'"

def test_ccsl_invocation_invocation_has_argsKind():
    assert hasattr(ccsl_invocation_Invocation, "argsKind")
    descriptor = None
    for klass in ccsl_invocation_Invocation.__mro__:
        if "argsKind" in klass.__dict__:
            descriptor = klass.__dict__["argsKind"]
            break
    assert isinstance(descriptor, property)



def test_simplemethodinvocation_is_not_abstract():
    assert not inspect.isabstract(SimpleMethodInvocation)


def test_simplemethodinvocation_constructor_exists():
    assert callable(SimpleMethodInvocation.__init__)


def test_simplemethodinvocation_constructor_args():
    sig = inspect.signature(SimpleMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_invocation_supermethodinvocation_is_not_abstract():
    assert not inspect.isabstract(ccsl_invocation_SuperMethodInvocation)


def test_ccsl_invocation_supermethodinvocation_constructor_exists():
    assert callable(ccsl_invocation_SuperMethodInvocation.__init__)


def test_ccsl_invocation_supermethodinvocation_constructor_args():
    sig = inspect.signature(ccsl_invocation_SuperMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_invocation_methodinvocation_is_not_abstract():
    assert not inspect.isabstract(ccsl_invocation_MethodInvocation)


def test_ccsl_invocation_methodinvocation_constructor_exists():
    assert callable(ccsl_invocation_MethodInvocation.__init__)


def test_ccsl_invocation_methodinvocation_constructor_args():
    sig = inspect.signature(ccsl_invocation_MethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_datatype_shortprimitivetype_is_not_abstract():
    assert not inspect.isabstract(ccsl_datatype_ShortPrimitiveType)


def test_ccsl_datatype_shortprimitivetype_constructor_exists():
    assert callable(ccsl_datatype_ShortPrimitiveType.__init__)


def test_ccsl_datatype_shortprimitivetype_constructor_args():
    sig = inspect.signature(ccsl_datatype_ShortPrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_ccsl_datatype_booleanprimitivetype_is_not_abstract():
    assert not inspect.isabstract(ccsl_datatype_BooleanPrimitiveType)


def test_ccsl_datatype_booleanprimitivetype_constructor_exists():
    assert callable(ccsl_datatype_BooleanPrimitiveType.__init__)


def test_ccsl_datatype_booleanprimitivetype_constructor_args():
    sig = inspect.signature(ccsl_datatype_BooleanPrimitiveType.__init__)
    params = list(sig.parameters.keys())

def test_collectionkind_exists():
    # Check that the Enumeration exists
    assert CollectionKind is not None

def test_collectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionKind]
    expected_literals = [
        "IMMEDIATE",
        "SEQUENCE",
        "EXACT",
        "ANY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectionKind"

def test_equationoperator_exists():
    # Check that the Enumeration exists
    assert EquationOperator is not None

def test_equationoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EquationOperator]
    expected_literals = [
        "PLUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EquationOperator"

def test_unaryassignmentoperator_exists():
    # Check that the Enumeration exists
    assert UnaryAssignmentOperator is not None

def test_unaryassignmentoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryAssignmentOperator]
    expected_literals = [
        "DECREMENT",
        "ANY",
        "INCREMENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryAssignmentOperator"

def test_inheritance_exists():
    # Check that the Enumeration exists
    assert Inheritance is not None

def test_inheritance_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Inheritance]
    expected_literals = [
        "NONE",
        "ABSTRACT",
        "FINAL",
        "ANY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Inheritance"

def test_assignmentoperator_exists():
    # Check that the Enumeration exists
    assert AssignmentOperator is not None

def test_assignmentoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentOperator]
    expected_literals = [
        "ANY",
        "PLUS_ASSIGN",
        "ASSIGN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentOperator"

def test_visibility_exists():
    # Check that the Enumeration exists
    assert Visibility is not None

def test_visibility_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Visibility]
    expected_literals = [
        "ANY",
        "PROTECTED",
        "PACKAGE",
        "PRIVATE",
        "PUBLIC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Visibility"

def test_arithmeticoperator_exists():
    # Check that the Enumeration exists
    assert ArithmeticOperator is not None

def test_arithmeticoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArithmeticOperator]
    expected_literals = [
        "SUBTRACTION",
        "ADDITION",
        "DIVISION",
        "MODULUS",
        "UNDEFINED",
        "MULTIPLICATION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArithmeticOperator"

def test_logicoperator_exists():
    # Check that the Enumeration exists
    assert LogicOperator is not None

def test_logicoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicOperator]
    expected_literals = [
        "OR",
        "AND",
        "IF_THEN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LogicOperator"

def test_booleanoperator_exists():
    # Check that the Enumeration exists
    assert BooleanOperator is not None

def test_booleanoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanOperator]
    expected_literals = [
        "ANY",
        "EQUAL_TO",
        "LESS_THAN_OR_EQUAL_TO",
        "OR",
        "GREATER_THAN",
        "GREATER_THAN_OR_EQUAL_TO",
        "NOT",
        "NOT_EQUAL_TO",
        "AND",
        "LESS_THAN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanOperator"


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
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
ccsl_datatype_StringPrimitiveType_strategy = st.builds(
    ccsl_datatype_StringPrimitiveType,
)
DataType_strategy = st.builds(
    DataType,
)
ccsl_datatype_PrimitiveType_strategy = st.builds(
    ccsl_datatype_PrimitiveType,
)
annotation_Annotation_strategy = st.builds(
    annotation_Annotation,
)
complexType_AnnotationType_strategy = st.builds(
    complexType_AnnotationType,
)
statements_Block_strategy = st.builds(
    statements_Block,
)
tryCatch_CatchClause_strategy = st.builds(
    tryCatch_CatchClause,
)
UnaryAssignment_strategy = st.builds(
    UnaryAssignment,
)
ccsl_assignment_PostfixUnaryAssignment_strategy = st.builds(
    ccsl_assignment_PostfixUnaryAssignment,
)
ccsl_assignment_PrefixUnaryAssignment_strategy = st.builds(
    ccsl_assignment_PrefixUnaryAssignment,
)
AbstractAssignment_strategy = st.builds(
    AbstractAssignment,
)
ccsl_assignment_UnaryAssignment_strategy = st.builds(
    ccsl_assignment_UnaryAssignment,
    operator=
        safe_text
)
ccsl_assignment_Assignment_strategy = st.builds(
    ccsl_assignment_Assignment,
    operator=
        safe_text
)
OperatorExpression_strategy = st.builds(
    OperatorExpression,
)
ccsl_expressions_InfixExpression_strategy = st.builds(
    ccsl_expressions_InfixExpression,
)
ccsl_expressions_BooleanExpression_strategy = st.builds(
    ccsl_expressions_BooleanExpression,
    booleanOperator=
        safe_text
)
ccsl_expressions_ArithmeticExpression_strategy = st.builds(
    ccsl_expressions_ArithmeticExpression,
    arithmeticOperator=
        safe_text
)
ccsl_expressions_StringConcatenation_strategy = st.builds(
    ccsl_expressions_StringConcatenation,
)
Block_strategy = st.builds(
    Block,
)
ccsl_controlFlow_SwitchCaseBlock_strategy = st.builds(
    ccsl_controlFlow_SwitchCaseBlock,
    default=
        safe_text
)
controlFlow_SwitchCaseBlock_strategy = st.builds(
    controlFlow_SwitchCaseBlock,
)
ControlFlow_strategy = st.builds(
    ControlFlow,
)
ccsl_controlFlow_LoopStatement_strategy = st.builds(
    ccsl_controlFlow_LoopStatement,
)
ccsl_controlFlow_IfStatement_strategy = st.builds(
    ccsl_controlFlow_IfStatement,
)
ccsl_controlFlow_SwitchStatement_strategy = st.builds(
    ccsl_controlFlow_SwitchStatement,
)
LiteralValue_strategy = st.builds(
    LiteralValue,
)
ccsl_literalValues_BooleanLiteral_strategy = st.builds(
    ccsl_literalValues_BooleanLiteral,
)
ccsl_literalValues_StringLiteral_strategy = st.builds(
    ccsl_literalValues_StringLiteral,
)
ccsl_literalValues_CharacterLiteral_strategy = st.builds(
    ccsl_literalValues_CharacterLiteral,
)
ccsl_literalValues_NumberLiteral_strategy = st.builds(
    ccsl_literalValues_NumberLiteral,
)
ccsl_literalValues_NullLiteral_strategy = st.builds(
    ccsl_literalValues_NullLiteral,
)
ccsl_statements_ThrowStatement_strategy = st.builds(
    ccsl_statements_ThrowStatement,
)
Statement_strategy = st.builds(
    Statement,
)
ccsl_statements_ArrayCreation_strategy = st.builds(
    ccsl_statements_ArrayCreation,
)
ccsl_statements_ContinueStatement_strategy = st.builds(
    ccsl_statements_ContinueStatement,
)
ccsl_expressions_ParenthesizedExpression_strategy = st.builds(
    ccsl_expressions_ParenthesizedExpression,
)
ccsl_statements_Access_strategy = st.builds(
    ccsl_statements_Access,
)
ccsl_statements_SynchronizedBlock_strategy = st.builds(
    ccsl_statements_SynchronizedBlock,
)
ccsl_expressions_OperatorExpression_strategy = st.builds(
    ccsl_expressions_OperatorExpression,
)
ccsl_tryCatch_TryStatement_strategy = st.builds(
    ccsl_tryCatch_TryStatement,
)
ccsl_annotation_Annotation_strategy = st.builds(
    ccsl_annotation_Annotation,
)
ccsl_literalValues_LiteralValue_strategy = st.builds(
    ccsl_literalValues_LiteralValue,
    value=
        safe_text
)
ccsl_assignment_AbstractAssignment_strategy = st.builds(
    ccsl_assignment_AbstractAssignment,
)
ccsl_tryCatch_CatchClause_strategy = st.builds(
    ccsl_tryCatch_CatchClause,
)
ccsl_statements_ThisStatement_strategy = st.builds(
    ccsl_statements_ThisStatement,
)
ccsl_statements_ReturnStatement_strategy = st.builds(
    ccsl_statements_ReturnStatement,
)
ccsl_statements_InstanceOf_strategy = st.builds(
    ccsl_statements_InstanceOf,
)
ccsl_statements_BreakStatement_strategy = st.builds(
    ccsl_statements_BreakStatement,
)
ccsl_statements_EmptyStatement_strategy = st.builds(
    ccsl_statements_EmptyStatement,
)
ccsl_statements_NamedElementAccess_strategy = st.builds(
    ccsl_statements_NamedElementAccess,
)
method_SimpleMethod_strategy = st.builds(
    method_SimpleMethod,
)
variable_ParameterVariable_strategy = st.builds(
    variable_ParameterVariable,
)
elements_Element_strategy = st.builds(
    elements_Element,
)
SimpleMethod_strategy = st.builds(
    SimpleMethod,
)
ccsl_method_Constructor_strategy = st.builds(
    ccsl_method_Constructor,
    avaliableInSourceCode=
        safe_text
)
ccsl_statements_InstanceCreation_strategy = st.builds(
    ccsl_statements_InstanceCreation,
    argsKind=
        safe_text
)
ccsl_statements_VarDeclaration_strategy = st.builds(
    ccsl_statements_VarDeclaration,
)
ccsl_statements_Block_strategy = st.builds(
    ccsl_statements_Block,
    statementsKind=
        safe_text
)
ccsl_statements_ControlFlow_strategy = st.builds(
    ccsl_statements_ControlFlow,
)
Access_strategy = st.builds(
    Access,
)
ccsl_statements_DataTypeAccess_strategy = st.builds(
    ccsl_statements_DataTypeAccess,
)
ccsl_statements_VariableAccess_strategy = st.builds(
    ccsl_statements_VariableAccess,
)
complexType_JClass_strategy = st.builds(
    complexType_JClass,
)
method_Constructor_strategy = st.builds(
    method_Constructor,
)
datatype_ObjectType_strategy = st.builds(
    datatype_ObjectType,
)
ComplexType_strategy = st.builds(
    ComplexType,
)
ccsl_complexType_AnonymousClass_strategy = st.builds(
    ccsl_complexType_AnonymousClass,
)
complexType_ComplexType_strategy = st.builds(
    complexType_ComplexType,
)
variable_InitializableVariable_strategy = st.builds(
    variable_InitializableVariable,
)
statements_Statement_strategy = st.builds(
    statements_Statement,
)
DeclaredType_strategy = st.builds(
    DeclaredType,
)
ccsl_complexType_AnnotationType_strategy = st.builds(
    ccsl_complexType_AnnotationType,
)
method_Method_strategy = st.builds(
    method_Method,
)
variable_FieldVariable_strategy = st.builds(
    variable_FieldVariable,
)
import_ImportStatement_strategy = st.builds(
    import_ImportStatement,
)
complexType_JInterface_strategy = st.builds(
    complexType_JInterface,
)
ccsl_elements_Element_strategy = st.builds(
    ccsl_elements_Element,
    uniqueName=
        safe_text
)
InjectionStrategy_strategy = st.builds(
    InjectionStrategy,
)
InjectionAction_strategy = st.builds(
    InjectionAction,
)
ccsl_Root_strategy = st.builds(
    ccsl_Root,
)
Variable_strategy = st.builds(
    Variable,
)
ccsl_variable_InitializableVariable_strategy = st.builds(
    ccsl_variable_InitializableVariable,
)
InitializableVariable_strategy = st.builds(
    InitializableVariable,
)
ccsl_variable_LocalVariable_strategy = st.builds(
    ccsl_variable_LocalVariable,
)
annotation_AnnotableElement_strategy = st.builds(
    annotation_AnnotableElement,
)
ccsl_variable_FieldVariable_strategy = st.builds(
    ccsl_variable_FieldVariable,
    static=
        safe_text,
    visibility=
        safe_text
)
ccsl_method_SimpleMethod_strategy = st.builds(
    ccsl_method_SimpleMethod,
    paramsKind=
        safe_text,
    visibility=
        safe_text
)
variable_Variable_strategy = st.builds(
    variable_Variable,
)
ccsl_variable_ParameterVariable_strategy = st.builds(
    ccsl_variable_ParameterVariable,
)
datatype_DataType_strategy = st.builds(
    datatype_DataType,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
ccsl_variable_Variable_strategy = st.builds(
    ccsl_variable_Variable,
    final=
        safe_text
)
complexType_DeclaredType_strategy = st.builds(
    complexType_DeclaredType,
)
ccsl_complexType_JClass_strategy = st.builds(
    ccsl_complexType_JClass,
    inheritance=
        safe_text
)
ccsl_complexType_JInterface_strategy = st.builds(
    ccsl_complexType_JInterface,
)
import_ImportableElement_strategy = st.builds(
    import_ImportableElement,
)
namedElements_NamedElement_strategy = st.builds(
    namedElements_NamedElement,
)
ccsl_method_Method_strategy = st.builds(
    ccsl_method_Method,
    abstract=
        safe_text,
    static=
        safe_text,
    final=
        safe_text,
    inheritance=
        safe_text
)
ccsl_complexType_DeclaredType_strategy = st.builds(
    ccsl_complexType_DeclaredType,
    static=
        safe_text,
    visibility=
        safe_text
)
ccsl_namedElements_Package_strategy = st.builds(
    ccsl_namedElements_Package,
)
Context_strategy = st.builds(
    Context,
)
Element_strategy = st.builds(
    Element,
)
ccsl_complexType_ComplexType_strategy = st.builds(
    ccsl_complexType_ComplexType,
)
ccsl_namedElements_NamedElement_strategy = st.builds(
    ccsl_namedElements_NamedElement,
    name=
        safe_text,
    avaliableInSourceCode=
        safe_text
)
ccsl_annotation_AnnotableElement_strategy = st.builds(
    ccsl_annotation_AnnotableElement,
    annotationsKind=
        safe_text
)
ccsl_datatype_DataType_strategy = st.builds(
    ccsl_datatype_DataType,
)
ccsl_statements_Statement_strategy = st.builds(
    ccsl_statements_Statement,
)
Rule_strategy = st.builds(
    Rule,
)
ccsl_AtomicRule_strategy = st.builds(
    ccsl_AtomicRule,
)
ccsl_CompositeRule_strategy = st.builds(
    ccsl_CompositeRule,
    operator=
        safe_text
)
Root_strategy = st.builds(
    Root,
)
ccsl_FaultTypeDescription_strategy = st.builds(
    ccsl_FaultTypeDescription,
    name=
        safe_text
)
ccsl_Rule_strategy = st.builds(
    ccsl_Rule,
    negated=
        safe_text
)
statements_Access_strategy = st.builds(
    statements_Access,
)
CcslNumberFunction_strategy = st.builds(
    CcslNumberFunction,
)
ccsl_numberFunctions_GetIndexOf_strategy = st.builds(
    ccsl_numberFunctions_GetIndexOf,
)
ccsl_numberFunctions_CcslIntegerLiteral_strategy = st.builds(
    ccsl_numberFunctions_CcslIntegerLiteral,
    value=
        safe_text
)
numberFunctions_CcslNumberFunction_strategy = st.builds(
    numberFunctions_CcslNumberFunction,
)
ccsl_filters_EquationFilter_strategy = st.builds(
    ccsl_filters_EquationFilter,
    operator=
        safe_text
)
AtomicFilter_strategy = st.builds(
    AtomicFilter,
)
ccsl_filters_SameNameFilter_strategy = st.builds(
    ccsl_filters_SameNameFilter,
    ignoreCase=
        safe_text
)
ccsl_filters_HasSameReferenceFilter_strategy = st.builds(
    ccsl_filters_HasSameReferenceFilter,
)
ccsl_filters_IsKindOfFilter_strategy = st.builds(
    ccsl_filters_IsKindOfFilter,
)
ccsl_filters_SuperClassClosureFilter_strategy = st.builds(
    ccsl_filters_SuperClassClosureFilter,
    includesSubClass=
        safe_text
)
ccsl_filters_IsStringFilter_strategy = st.builds(
    ccsl_filters_IsStringFilter,
)
ccsl_filters_BlockLastStatementFilter_strategy = st.builds(
    ccsl_filters_BlockLastStatementFilter,
)
ccsl_filters_TemplateFilter_strategy = st.builds(
    ccsl_filters_TemplateFilter,
)
ccsl_filters_ChildClosureComplexTypeFilter_strategy = st.builds(
    ccsl_filters_ChildClosureComplexTypeFilter,
)
ccsl_filters_FromClosureFilter_strategy = st.builds(
    ccsl_filters_FromClosureFilter,
)
ccsl_filters_SuperMethodClosureFilter_strategy = st.builds(
    ccsl_filters_SuperMethodClosureFilter,
)
ccsl_filters_IsTypeOfFilter_strategy = st.builds(
    ccsl_filters_IsTypeOfFilter,
)
ccsl_filters_PropertyFilter_strategy = st.builds(
    ccsl_filters_PropertyFilter,
)
Filter_strategy = st.builds(
    Filter,
)
ccsl_filters_CompositeFilter_strategy = st.builds(
    ccsl_filters_CompositeFilter,
    operator=
        safe_text
)
ccsl_filters_AtomicFilter_strategy = st.builds(
    ccsl_filters_AtomicFilter,
)
CcslBooleanFunction_strategy = st.builds(
    CcslBooleanFunction,
)
ccsl_filters_Filter_strategy = st.builds(
    ccsl_filters_Filter,
    negated=
        safe_text
)
CcslFunction_strategy = st.builds(
    CcslFunction,
)
ccsl_numberFunctions_CcslNumberFunction_strategy = st.builds(
    ccsl_numberFunctions_CcslNumberFunction,
)
ccsl_booleanFunctions_CcslBooleanFunction_strategy = st.builds(
    ccsl_booleanFunctions_CcslBooleanFunction,
)
ccsl_filters_ImplicityContainerFilter_strategy = st.builds(
    ccsl_filters_ImplicityContainerFilter,
)
expressions_OperatorExpression_strategy = st.builds(
    expressions_OperatorExpression,
)
TemplateFilter_strategy = st.builds(
    TemplateFilter,
)
ccsl_filters_ImplicityOperandFilter_strategy = st.builds(
    ccsl_filters_ImplicityOperandFilter,
)
ccsl_filters_RegexMatch_strategy = st.builds(
    ccsl_filters_RegexMatch,
    regex=
        safe_text
)
ccsl_filters_CountFilter_strategy = st.builds(
    ccsl_filters_CountFilter,
    min=
        safe_text,
    max=
        safe_text
)
ccsl_faultTypeDescription_InjectionAction_strategy = st.builds(
    ccsl_faultTypeDescription_InjectionAction,
)
filters_Filter_strategy = st.builds(
    filters_Filter,
)
ccsl_context_Context_strategy = st.builds(
    ccsl_context_Context,
)
ccsl_datatype_VoidType_strategy = st.builds(
    ccsl_datatype_VoidType,
)
ccsl_datatype_IntPrimitiveType_strategy = st.builds(
    ccsl_datatype_IntPrimitiveType,
)
ccsl_datatype_GenericType_strategy = st.builds(
    ccsl_datatype_GenericType,
)
ObjectType_strategy = st.builds(
    ObjectType,
)
ccsl_datatype_ArrayType_strategy = st.builds(
    ccsl_datatype_ArrayType,
    dimensions=
        safe_text
)
ccsl_datatype_ParameterizedType_strategy = st.builds(
    ccsl_datatype_ParameterizedType,
)
ccsl_datatype_ObjectType_strategy = st.builds(
    ccsl_datatype_ObjectType,
)
ccsl_functions_CcslFunction_strategy = st.builds(
    ccsl_functions_CcslFunction,
)
ccsl_strategy_AllStrategy_strategy = st.builds(
    ccsl_strategy_AllStrategy,
)
ccsl_action_ArithmeticOperatorMap_strategy = st.builds(
    ccsl_action_ArithmeticOperatorMap,
    oldArithmeticOperator=
        safe_text,
    newArithmeticOperator=
        safe_text
)
action_ArithmeticOperatorMap_strategy = st.builds(
    action_ArithmeticOperatorMap,
)
ccsl_action_ReplaceArithmeticOperatorAction_strategy = st.builds(
    ccsl_action_ReplaceArithmeticOperatorAction,
)
ccsl_action_ReplaceVariableAccessAction_strategy = st.builds(
    ccsl_action_ReplaceVariableAccessAction,
)
ccsl_action_DeleteRandomStatementAction_strategy = st.builds(
    ccsl_action_DeleteRandomStatementAction,
)
ccsl_action_ChangeLiteralValueAction_strategy = st.builds(
    ccsl_action_ChangeLiteralValueAction,
)
ccsl_action_DeleteInfixOperatorAction_strategy = st.builds(
    ccsl_action_DeleteInfixOperatorAction,
)
ccsl_action_MoveScopeUpAction_strategy = st.builds(
    ccsl_action_MoveScopeUpAction,
)
ccsl_action_DeleteAction_strategy = st.builds(
    ccsl_action_DeleteAction,
)
ccsl_faultTypeDescription_InjectionStrategy_strategy = st.builds(
    ccsl_faultTypeDescription_InjectionStrategy,
)
ccsl_import_ImportStatement_strategy = st.builds(
    ccsl_import_ImportStatement,
)
ccsl_import_ImportableElement_strategy = st.builds(
    ccsl_import_ImportableElement,
)
Invocation_strategy = st.builds(
    Invocation,
)
ccsl_invocation_SimpleMethodInvocation_strategy = st.builds(
    ccsl_invocation_SimpleMethodInvocation,
)
ccsl_invocation_ConstructorInvocation_strategy = st.builds(
    ccsl_invocation_ConstructorInvocation,
)
ccsl_invocation_Invocation_strategy = st.builds(
    ccsl_invocation_Invocation,
    argsKind=
        safe_text
)
SimpleMethodInvocation_strategy = st.builds(
    SimpleMethodInvocation,
)
ccsl_invocation_SuperMethodInvocation_strategy = st.builds(
    ccsl_invocation_SuperMethodInvocation,
)
ccsl_invocation_MethodInvocation_strategy = st.builds(
    ccsl_invocation_MethodInvocation,
)
ccsl_datatype_ShortPrimitiveType_strategy = st.builds(
    ccsl_datatype_ShortPrimitiveType,
)
ccsl_datatype_BooleanPrimitiveType_strategy = st.builds(
    ccsl_datatype_BooleanPrimitiveType,
)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=ccsl_datatype_StringPrimitiveType_strategy)
@settings(max_examples=50)
def test_ccsl_datatype_stringprimitivetype_instantiation(instance):
    assert isinstance(instance, ccsl_datatype_StringPrimitiveType)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=ccsl_datatype_PrimitiveType_strategy)
@settings(max_examples=50)
def test_ccsl_datatype_primitivetype_instantiation(instance):
    assert isinstance(instance, ccsl_datatype_PrimitiveType)

@given(instance=annotation_Annotation_strategy)
@settings(max_examples=50)
def test_annotation_annotation_instantiation(instance):
    assert isinstance(instance, annotation_Annotation)

@given(instance=complexType_AnnotationType_strategy)
@settings(max_examples=50)
def test_complextype_annotationtype_instantiation(instance):
    assert isinstance(instance, complexType_AnnotationType)

@given(instance=statements_Block_strategy)
@settings(max_examples=50)
def test_statements_block_instantiation(instance):
    assert isinstance(instance, statements_Block)

@given(instance=tryCatch_CatchClause_strategy)
@settings(max_examples=50)
def test_trycatch_catchclause_instantiation(instance):
    assert isinstance(instance, tryCatch_CatchClause)

@given(instance=UnaryAssignment_strategy)
@settings(max_examples=50)
def test_unaryassignment_instantiation(instance):
    assert isinstance(instance, UnaryAssignment)

@given(instance=ccsl_assignment_PostfixUnaryAssignment_strategy)
@settings(max_examples=50)
def test_ccsl_assignment_postfixunaryassignment_instantiation(instance):
    assert isinstance(instance, ccsl_assignment_PostfixUnaryAssignment)

@given(instance=ccsl_assignment_PrefixUnaryAssignment_strategy)
@settings(max_examples=50)
def test_ccsl_assignment_prefixunaryassignment_instantiation(instance):
    assert isinstance(instance, ccsl_assignment_PrefixUnaryAssignment)

@given(instance=AbstractAssignment_strategy)
@settings(max_examples=50)
def test_abstractassignment_instantiation(instance):
    assert isinstance(instance, AbstractAssignment)

@given(instance=ccsl_assignment_UnaryAssignment_strategy)
@settings(max_examples=50)
def test_ccsl_assignment_unaryassignment_instantiation(instance):
    assert isinstance(instance, ccsl_assignment_UnaryAssignment)



@given(instance=ccsl_assignment_UnaryAssignment_strategy)
def test_ccsl_assignment_unaryassignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ccsl_assignment_Assignment_strategy)
@settings(max_examples=50)
def test_ccsl_assignment_assignment_instantiation(instance):
    assert isinstance(instance, ccsl_assignment_Assignment)



@given(instance=ccsl_assignment_Assignment_strategy)
def test_ccsl_assignment_assignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=OperatorExpression_strategy)
@settings(max_examples=50)
def test_operatorexpression_instantiation(instance):
    assert isinstance(instance, OperatorExpression)

@given(instance=ccsl_expressions_InfixExpression_strategy)
@settings(max_examples=50)
def test_ccsl_expressions_infixexpression_instantiation(instance):
    assert isinstance(instance, ccsl_expressions_InfixExpression)

@given(instance=ccsl_expressions_BooleanExpression_strategy)
@settings(max_examples=50)
def test_ccsl_expressions_booleanexpression_instantiation(instance):
    assert isinstance(instance, ccsl_expressions_BooleanExpression)



@given(instance=ccsl_expressions_BooleanExpression_strategy)
def test_ccsl_expressions_booleanexpression_booleanOperator_setter(instance):
    original = instance.booleanOperator
    instance.booleanOperator = original
    assert instance.booleanOperator == original

@given(instance=ccsl_expressions_ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_ccsl_expressions_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, ccsl_expressions_ArithmeticExpression)



@given(instance=ccsl_expressions_ArithmeticExpression_strategy)
def test_ccsl_expressions_arithmeticexpression_arithmeticOperator_setter(instance):
    original = instance.arithmeticOperator
    instance.arithmeticOperator = original
    assert instance.arithmeticOperator == original

@given(instance=ccsl_expressions_StringConcatenation_strategy)
@settings(max_examples=50)
def test_ccsl_expressions_stringconcatenation_instantiation(instance):
    assert isinstance(instance, ccsl_expressions_StringConcatenation)

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=ccsl_controlFlow_SwitchCaseBlock_strategy)
@settings(max_examples=50)
def test_ccsl_controlflow_switchcaseblock_instantiation(instance):
    assert isinstance(instance, ccsl_controlFlow_SwitchCaseBlock)



@given(instance=ccsl_controlFlow_SwitchCaseBlock_strategy)
def test_ccsl_controlflow_switchcaseblock_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=controlFlow_SwitchCaseBlock_strategy)
@settings(max_examples=50)
def test_controlflow_switchcaseblock_instantiation(instance):
    assert isinstance(instance, controlFlow_SwitchCaseBlock)

@given(instance=ControlFlow_strategy)
@settings(max_examples=50)
def test_controlflow_instantiation(instance):
    assert isinstance(instance, ControlFlow)

@given(instance=ccsl_controlFlow_LoopStatement_strategy)
@settings(max_examples=50)
def test_ccsl_controlflow_loopstatement_instantiation(instance):
    assert isinstance(instance, ccsl_controlFlow_LoopStatement)

@given(instance=ccsl_controlFlow_IfStatement_strategy)
@settings(max_examples=50)
def test_ccsl_controlflow_ifstatement_instantiation(instance):
    assert isinstance(instance, ccsl_controlFlow_IfStatement)

@given(instance=ccsl_controlFlow_SwitchStatement_strategy)
@settings(max_examples=50)
def test_ccsl_controlflow_switchstatement_instantiation(instance):
    assert isinstance(instance, ccsl_controlFlow_SwitchStatement)

@given(instance=LiteralValue_strategy)
@settings(max_examples=50)
def test_literalvalue_instantiation(instance):
    assert isinstance(instance, LiteralValue)

@given(instance=ccsl_literalValues_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_ccsl_literalvalues_booleanliteral_instantiation(instance):
    assert isinstance(instance, ccsl_literalValues_BooleanLiteral)

@given(instance=ccsl_literalValues_StringLiteral_strategy)
@settings(max_examples=50)
def test_ccsl_literalvalues_stringliteral_instantiation(instance):
    assert isinstance(instance, ccsl_literalValues_StringLiteral)

@given(instance=ccsl_literalValues_CharacterLiteral_strategy)
@settings(max_examples=50)
def test_ccsl_literalvalues_characterliteral_instantiation(instance):
    assert isinstance(instance, ccsl_literalValues_CharacterLiteral)

@given(instance=ccsl_literalValues_NumberLiteral_strategy)
@settings(max_examples=50)
def test_ccsl_literalvalues_numberliteral_instantiation(instance):
    assert isinstance(instance, ccsl_literalValues_NumberLiteral)

@given(instance=ccsl_literalValues_NullLiteral_strategy)
@settings(max_examples=50)
def test_ccsl_literalvalues_nullliteral_instantiation(instance):
    assert isinstance(instance, ccsl_literalValues_NullLiteral)

@given(instance=ccsl_statements_ThrowStatement_strategy)
@settings(max_examples=50)
def test_ccsl_statements_throwstatement_instantiation(instance):
    assert isinstance(instance, ccsl_statements_ThrowStatement)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=ccsl_statements_ArrayCreation_strategy)
@settings(max_examples=50)
def test_ccsl_statements_arraycreation_instantiation(instance):
    assert isinstance(instance, ccsl_statements_ArrayCreation)

@given(instance=ccsl_statements_ContinueStatement_strategy)
@settings(max_examples=50)
def test_ccsl_statements_continuestatement_instantiation(instance):
    assert isinstance(instance, ccsl_statements_ContinueStatement)

@given(instance=ccsl_expressions_ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_ccsl_expressions_parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, ccsl_expressions_ParenthesizedExpression)

@given(instance=ccsl_statements_Access_strategy)
@settings(max_examples=50)
def test_ccsl_statements_access_instantiation(instance):
    assert isinstance(instance, ccsl_statements_Access)

@given(instance=ccsl_statements_SynchronizedBlock_strategy)
@settings(max_examples=50)
def test_ccsl_statements_synchronizedblock_instantiation(instance):
    assert isinstance(instance, ccsl_statements_SynchronizedBlock)

@given(instance=ccsl_expressions_OperatorExpression_strategy)
@settings(max_examples=50)
def test_ccsl_expressions_operatorexpression_instantiation(instance):
    assert isinstance(instance, ccsl_expressions_OperatorExpression)

@given(instance=ccsl_tryCatch_TryStatement_strategy)
@settings(max_examples=50)
def test_ccsl_trycatch_trystatement_instantiation(instance):
    assert isinstance(instance, ccsl_tryCatch_TryStatement)

@given(instance=ccsl_annotation_Annotation_strategy)
@settings(max_examples=50)
def test_ccsl_annotation_annotation_instantiation(instance):
    assert isinstance(instance, ccsl_annotation_Annotation)

@given(instance=ccsl_literalValues_LiteralValue_strategy)
@settings(max_examples=50)
def test_ccsl_literalvalues_literalvalue_instantiation(instance):
    assert isinstance(instance, ccsl_literalValues_LiteralValue)



@given(instance=ccsl_literalValues_LiteralValue_strategy)
def test_ccsl_literalvalues_literalvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ccsl_assignment_AbstractAssignment_strategy)
@settings(max_examples=50)
def test_ccsl_assignment_abstractassignment_instantiation(instance):
    assert isinstance(instance, ccsl_assignment_AbstractAssignment)

@given(instance=ccsl_tryCatch_CatchClause_strategy)
@settings(max_examples=50)
def test_ccsl_trycatch_catchclause_instantiation(instance):
    assert isinstance(instance, ccsl_tryCatch_CatchClause)

@given(instance=ccsl_statements_ThisStatement_strategy)
@settings(max_examples=50)
def test_ccsl_statements_thisstatement_instantiation(instance):
    assert isinstance(instance, ccsl_statements_ThisStatement)

@given(instance=ccsl_statements_ReturnStatement_strategy)
@settings(max_examples=50)
def test_ccsl_statements_returnstatement_instantiation(instance):
    assert isinstance(instance, ccsl_statements_ReturnStatement)

@given(instance=ccsl_statements_InstanceOf_strategy)
@settings(max_examples=50)
def test_ccsl_statements_instanceof_instantiation(instance):
    assert isinstance(instance, ccsl_statements_InstanceOf)

@given(instance=ccsl_statements_BreakStatement_strategy)
@settings(max_examples=50)
def test_ccsl_statements_breakstatement_instantiation(instance):
    assert isinstance(instance, ccsl_statements_BreakStatement)

@given(instance=ccsl_statements_EmptyStatement_strategy)
@settings(max_examples=50)
def test_ccsl_statements_emptystatement_instantiation(instance):
    assert isinstance(instance, ccsl_statements_EmptyStatement)

@given(instance=ccsl_statements_NamedElementAccess_strategy)
@settings(max_examples=50)
def test_ccsl_statements_namedelementaccess_instantiation(instance):
    assert isinstance(instance, ccsl_statements_NamedElementAccess)

@given(instance=method_SimpleMethod_strategy)
@settings(max_examples=50)
def test_method_simplemethod_instantiation(instance):
    assert isinstance(instance, method_SimpleMethod)

@given(instance=variable_ParameterVariable_strategy)
@settings(max_examples=50)
def test_variable_parametervariable_instantiation(instance):
    assert isinstance(instance, variable_ParameterVariable)

@given(instance=elements_Element_strategy)
@settings(max_examples=50)
def test_elements_element_instantiation(instance):
    assert isinstance(instance, elements_Element)

@given(instance=SimpleMethod_strategy)
@settings(max_examples=50)
def test_simplemethod_instantiation(instance):
    assert isinstance(instance, SimpleMethod)

@given(instance=ccsl_method_Constructor_strategy)
@settings(max_examples=50)
def test_ccsl_method_constructor_instantiation(instance):
    assert isinstance(instance, ccsl_method_Constructor)



@given(instance=ccsl_method_Constructor_strategy)
def test_ccsl_method_constructor_avaliableInSourceCode_setter(instance):
    original = instance.avaliableInSourceCode
    instance.avaliableInSourceCode = original
    assert instance.avaliableInSourceCode == original

@given(instance=ccsl_statements_InstanceCreation_strategy)
@settings(max_examples=50)
def test_ccsl_statements_instancecreation_instantiation(instance):
    assert isinstance(instance, ccsl_statements_InstanceCreation)



@given(instance=ccsl_statements_InstanceCreation_strategy)
def test_ccsl_statements_instancecreation_argsKind_setter(instance):
    original = instance.argsKind
    instance.argsKind = original
    assert instance.argsKind == original

@given(instance=ccsl_statements_VarDeclaration_strategy)
@settings(max_examples=50)
def test_ccsl_statements_vardeclaration_instantiation(instance):
    assert isinstance(instance, ccsl_statements_VarDeclaration)

@given(instance=ccsl_statements_Block_strategy)
@settings(max_examples=50)
def test_ccsl_statements_block_instantiation(instance):
    assert isinstance(instance, ccsl_statements_Block)



@given(instance=ccsl_statements_Block_strategy)
def test_ccsl_statements_block_statementsKind_setter(instance):
    original = instance.statementsKind
    instance.statementsKind = original
    assert instance.statementsKind == original

@given(instance=ccsl_statements_ControlFlow_strategy)
@settings(max_examples=50)
def test_ccsl_statements_controlflow_instantiation(instance):
    assert isinstance(instance, ccsl_statements_ControlFlow)

@given(instance=Access_strategy)
@settings(max_examples=50)
def test_access_instantiation(instance):
    assert isinstance(instance, Access)

@given(instance=ccsl_statements_DataTypeAccess_strategy)
@settings(max_examples=50)
def test_ccsl_statements_datatypeaccess_instantiation(instance):
    assert isinstance(instance, ccsl_statements_DataTypeAccess)

@given(instance=ccsl_statements_VariableAccess_strategy)
@settings(max_examples=50)
def test_ccsl_statements_variableaccess_instantiation(instance):
    assert isinstance(instance, ccsl_statements_VariableAccess)

@given(instance=complexType_JClass_strategy)
@settings(max_examples=50)
def test_complextype_jclass_instantiation(instance):
    assert isinstance(instance, complexType_JClass)

@given(instance=method_Constructor_strategy)
@settings(max_examples=50)
def test_method_constructor_instantiation(instance):
    assert isinstance(instance, method_Constructor)

@given(instance=datatype_ObjectType_strategy)
@settings(max_examples=50)
def test_datatype_objecttype_instantiation(instance):
    assert isinstance(instance, datatype_ObjectType)

@given(instance=ComplexType_strategy)
@settings(max_examples=50)
def test_complextype_instantiation(instance):
    assert isinstance(instance, ComplexType)

@given(instance=ccsl_complexType_AnonymousClass_strategy)
@settings(max_examples=50)
def test_ccsl_complextype_anonymousclass_instantiation(instance):
    assert isinstance(instance, ccsl_complexType_AnonymousClass)

@given(instance=complexType_ComplexType_strategy)
@settings(max_examples=50)
def test_complextype_complextype_instantiation(instance):
    assert isinstance(instance, complexType_ComplexType)

@given(instance=variable_InitializableVariable_strategy)
@settings(max_examples=50)
def test_variable_initializablevariable_instantiation(instance):
    assert isinstance(instance, variable_InitializableVariable)

@given(instance=statements_Statement_strategy)
@settings(max_examples=50)
def test_statements_statement_instantiation(instance):
    assert isinstance(instance, statements_Statement)

@given(instance=DeclaredType_strategy)
@settings(max_examples=50)
def test_declaredtype_instantiation(instance):
    assert isinstance(instance, DeclaredType)

@given(instance=ccsl_complexType_AnnotationType_strategy)
@settings(max_examples=50)
def test_ccsl_complextype_annotationtype_instantiation(instance):
    assert isinstance(instance, ccsl_complexType_AnnotationType)

@given(instance=method_Method_strategy)
@settings(max_examples=50)
def test_method_method_instantiation(instance):
    assert isinstance(instance, method_Method)

@given(instance=variable_FieldVariable_strategy)
@settings(max_examples=50)
def test_variable_fieldvariable_instantiation(instance):
    assert isinstance(instance, variable_FieldVariable)

@given(instance=import_ImportStatement_strategy)
@settings(max_examples=50)
def test_import_importstatement_instantiation(instance):
    assert isinstance(instance, import_ImportStatement)

@given(instance=complexType_JInterface_strategy)
@settings(max_examples=50)
def test_complextype_jinterface_instantiation(instance):
    assert isinstance(instance, complexType_JInterface)

@given(instance=ccsl_elements_Element_strategy)
@settings(max_examples=50)
def test_ccsl_elements_element_instantiation(instance):
    assert isinstance(instance, ccsl_elements_Element)



@given(instance=ccsl_elements_Element_strategy)
def test_ccsl_elements_element_uniqueName_setter(instance):
    original = instance.uniqueName
    instance.uniqueName = original
    assert instance.uniqueName == original

@given(instance=InjectionStrategy_strategy)
@settings(max_examples=50)
def test_injectionstrategy_instantiation(instance):
    assert isinstance(instance, InjectionStrategy)

@given(instance=InjectionAction_strategy)
@settings(max_examples=50)
def test_injectionaction_instantiation(instance):
    assert isinstance(instance, InjectionAction)

@given(instance=ccsl_Root_strategy)
@settings(max_examples=50)
def test_ccsl_root_instantiation(instance):
    assert isinstance(instance, ccsl_Root)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=ccsl_variable_InitializableVariable_strategy)
@settings(max_examples=50)
def test_ccsl_variable_initializablevariable_instantiation(instance):
    assert isinstance(instance, ccsl_variable_InitializableVariable)

@given(instance=InitializableVariable_strategy)
@settings(max_examples=50)
def test_initializablevariable_instantiation(instance):
    assert isinstance(instance, InitializableVariable)

@given(instance=ccsl_variable_LocalVariable_strategy)
@settings(max_examples=50)
def test_ccsl_variable_localvariable_instantiation(instance):
    assert isinstance(instance, ccsl_variable_LocalVariable)

@given(instance=annotation_AnnotableElement_strategy)
@settings(max_examples=50)
def test_annotation_annotableelement_instantiation(instance):
    assert isinstance(instance, annotation_AnnotableElement)

@given(instance=ccsl_variable_FieldVariable_strategy)
@settings(max_examples=50)
def test_ccsl_variable_fieldvariable_instantiation(instance):
    assert isinstance(instance, ccsl_variable_FieldVariable)



@given(instance=ccsl_variable_FieldVariable_strategy)
def test_ccsl_variable_fieldvariable_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original



@given(instance=ccsl_variable_FieldVariable_strategy)
def test_ccsl_variable_fieldvariable_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=ccsl_method_SimpleMethod_strategy)
@settings(max_examples=50)
def test_ccsl_method_simplemethod_instantiation(instance):
    assert isinstance(instance, ccsl_method_SimpleMethod)



@given(instance=ccsl_method_SimpleMethod_strategy)
def test_ccsl_method_simplemethod_paramsKind_setter(instance):
    original = instance.paramsKind
    instance.paramsKind = original
    assert instance.paramsKind == original



@given(instance=ccsl_method_SimpleMethod_strategy)
def test_ccsl_method_simplemethod_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=variable_Variable_strategy)
@settings(max_examples=50)
def test_variable_variable_instantiation(instance):
    assert isinstance(instance, variable_Variable)

@given(instance=ccsl_variable_ParameterVariable_strategy)
@settings(max_examples=50)
def test_ccsl_variable_parametervariable_instantiation(instance):
    assert isinstance(instance, ccsl_variable_ParameterVariable)

@given(instance=datatype_DataType_strategy)
@settings(max_examples=50)
def test_datatype_datatype_instantiation(instance):
    assert isinstance(instance, datatype_DataType)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=ccsl_variable_Variable_strategy)
@settings(max_examples=50)
def test_ccsl_variable_variable_instantiation(instance):
    assert isinstance(instance, ccsl_variable_Variable)



@given(instance=ccsl_variable_Variable_strategy)
def test_ccsl_variable_variable_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

@given(instance=complexType_DeclaredType_strategy)
@settings(max_examples=50)
def test_complextype_declaredtype_instantiation(instance):
    assert isinstance(instance, complexType_DeclaredType)

@given(instance=ccsl_complexType_JClass_strategy)
@settings(max_examples=50)
def test_ccsl_complextype_jclass_instantiation(instance):
    assert isinstance(instance, ccsl_complexType_JClass)



@given(instance=ccsl_complexType_JClass_strategy)
def test_ccsl_complextype_jclass_inheritance_setter(instance):
    original = instance.inheritance
    instance.inheritance = original
    assert instance.inheritance == original

@given(instance=ccsl_complexType_JInterface_strategy)
@settings(max_examples=50)
def test_ccsl_complextype_jinterface_instantiation(instance):
    assert isinstance(instance, ccsl_complexType_JInterface)

@given(instance=import_ImportableElement_strategy)
@settings(max_examples=50)
def test_import_importableelement_instantiation(instance):
    assert isinstance(instance, import_ImportableElement)

@given(instance=namedElements_NamedElement_strategy)
@settings(max_examples=50)
def test_namedelements_namedelement_instantiation(instance):
    assert isinstance(instance, namedElements_NamedElement)

@given(instance=ccsl_method_Method_strategy)
@settings(max_examples=50)
def test_ccsl_method_method_instantiation(instance):
    assert isinstance(instance, ccsl_method_Method)



@given(instance=ccsl_method_Method_strategy)
def test_ccsl_method_method_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original



@given(instance=ccsl_method_Method_strategy)
def test_ccsl_method_method_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original



@given(instance=ccsl_method_Method_strategy)
def test_ccsl_method_method_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original



@given(instance=ccsl_method_Method_strategy)
def test_ccsl_method_method_inheritance_setter(instance):
    original = instance.inheritance
    instance.inheritance = original
    assert instance.inheritance == original

@given(instance=ccsl_complexType_DeclaredType_strategy)
@settings(max_examples=50)
def test_ccsl_complextype_declaredtype_instantiation(instance):
    assert isinstance(instance, ccsl_complexType_DeclaredType)



@given(instance=ccsl_complexType_DeclaredType_strategy)
def test_ccsl_complextype_declaredtype_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original



@given(instance=ccsl_complexType_DeclaredType_strategy)
def test_ccsl_complextype_declaredtype_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=ccsl_namedElements_Package_strategy)
@settings(max_examples=50)
def test_ccsl_namedelements_package_instantiation(instance):
    assert isinstance(instance, ccsl_namedElements_Package)

@given(instance=Context_strategy)
@settings(max_examples=50)
def test_context_instantiation(instance):
    assert isinstance(instance, Context)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=ccsl_complexType_ComplexType_strategy)
@settings(max_examples=50)
def test_ccsl_complextype_complextype_instantiation(instance):
    assert isinstance(instance, ccsl_complexType_ComplexType)

@given(instance=ccsl_namedElements_NamedElement_strategy)
@settings(max_examples=50)
def test_ccsl_namedelements_namedelement_instantiation(instance):
    assert isinstance(instance, ccsl_namedElements_NamedElement)



@given(instance=ccsl_namedElements_NamedElement_strategy)
def test_ccsl_namedelements_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ccsl_namedElements_NamedElement_strategy)
def test_ccsl_namedelements_namedelement_avaliableInSourceCode_setter(instance):
    original = instance.avaliableInSourceCode
    instance.avaliableInSourceCode = original
    assert instance.avaliableInSourceCode == original

@given(instance=ccsl_annotation_AnnotableElement_strategy)
@settings(max_examples=50)
def test_ccsl_annotation_annotableelement_instantiation(instance):
    assert isinstance(instance, ccsl_annotation_AnnotableElement)



@given(instance=ccsl_annotation_AnnotableElement_strategy)
def test_ccsl_annotation_annotableelement_annotationsKind_setter(instance):
    original = instance.annotationsKind
    instance.annotationsKind = original
    assert instance.annotationsKind == original

@given(instance=ccsl_datatype_DataType_strategy)
@settings(max_examples=50)
def test_ccsl_datatype_datatype_instantiation(instance):
    assert isinstance(instance, ccsl_datatype_DataType)

@given(instance=ccsl_statements_Statement_strategy)
@settings(max_examples=50)
def test_ccsl_statements_statement_instantiation(instance):
    assert isinstance(instance, ccsl_statements_Statement)

@given(instance=Rule_strategy)
@settings(max_examples=50)
def test_rule_instantiation(instance):
    assert isinstance(instance, Rule)

@given(instance=ccsl_AtomicRule_strategy)
@settings(max_examples=50)
def test_ccsl_atomicrule_instantiation(instance):
    assert isinstance(instance, ccsl_AtomicRule)

@given(instance=ccsl_CompositeRule_strategy)
@settings(max_examples=50)
def test_ccsl_compositerule_instantiation(instance):
    assert isinstance(instance, ccsl_CompositeRule)



@given(instance=ccsl_CompositeRule_strategy)
def test_ccsl_compositerule_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Root_strategy)
@settings(max_examples=50)
def test_root_instantiation(instance):
    assert isinstance(instance, Root)

@given(instance=ccsl_FaultTypeDescription_strategy)
@settings(max_examples=50)
def test_ccsl_faulttypedescription_instantiation(instance):
    assert isinstance(instance, ccsl_FaultTypeDescription)



@given(instance=ccsl_FaultTypeDescription_strategy)
def test_ccsl_faulttypedescription_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ccsl_Rule_strategy)
@settings(max_examples=50)
def test_ccsl_rule_instantiation(instance):
    assert isinstance(instance, ccsl_Rule)



@given(instance=ccsl_Rule_strategy)
def test_ccsl_rule_negated_setter(instance):
    original = instance.negated
    instance.negated = original
    assert instance.negated == original

@given(instance=statements_Access_strategy)
@settings(max_examples=50)
def test_statements_access_instantiation(instance):
    assert isinstance(instance, statements_Access)

@given(instance=CcslNumberFunction_strategy)
@settings(max_examples=50)
def test_ccslnumberfunction_instantiation(instance):
    assert isinstance(instance, CcslNumberFunction)

@given(instance=ccsl_numberFunctions_GetIndexOf_strategy)
@settings(max_examples=50)
def test_ccsl_numberfunctions_getindexof_instantiation(instance):
    assert isinstance(instance, ccsl_numberFunctions_GetIndexOf)

@given(instance=ccsl_numberFunctions_CcslIntegerLiteral_strategy)
@settings(max_examples=50)
def test_ccsl_numberfunctions_ccslintegerliteral_instantiation(instance):
    assert isinstance(instance, ccsl_numberFunctions_CcslIntegerLiteral)



@given(instance=ccsl_numberFunctions_CcslIntegerLiteral_strategy)
def test_ccsl_numberfunctions_ccslintegerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=numberFunctions_CcslNumberFunction_strategy)
@settings(max_examples=50)
def test_numberfunctions_ccslnumberfunction_instantiation(instance):
    assert isinstance(instance, numberFunctions_CcslNumberFunction)

@given(instance=ccsl_filters_EquationFilter_strategy)
@settings(max_examples=50)
def test_ccsl_filters_equationfilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_EquationFilter)



@given(instance=ccsl_filters_EquationFilter_strategy)
def test_ccsl_filters_equationfilter_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=AtomicFilter_strategy)
@settings(max_examples=50)
def test_atomicfilter_instantiation(instance):
    assert isinstance(instance, AtomicFilter)

@given(instance=ccsl_filters_SameNameFilter_strategy)
@settings(max_examples=50)
def test_ccsl_filters_samenamefilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_SameNameFilter)



@given(instance=ccsl_filters_SameNameFilter_strategy)
def test_ccsl_filters_samenamefilter_ignoreCase_setter(instance):
    original = instance.ignoreCase
    instance.ignoreCase = original
    assert instance.ignoreCase == original

@given(instance=ccsl_filters_HasSameReferenceFilter_strategy)
@settings(max_examples=50)
def test_ccsl_filters_hassamereferencefilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_HasSameReferenceFilter)

@given(instance=ccsl_filters_IsKindOfFilter_strategy)
@settings(max_examples=50)
def test_ccsl_filters_iskindoffilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_IsKindOfFilter)

@given(instance=ccsl_filters_SuperClassClosureFilter_strategy)
@settings(max_examples=50)
def test_ccsl_filters_superclassclosurefilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_SuperClassClosureFilter)



@given(instance=ccsl_filters_SuperClassClosureFilter_strategy)
def test_ccsl_filters_superclassclosurefilter_includesSubClass_setter(instance):
    original = instance.includesSubClass
    instance.includesSubClass = original
    assert instance.includesSubClass == original

@given(instance=ccsl_filters_IsStringFilter_strategy)
@settings(max_examples=50)
def test_ccsl_filters_isstringfilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_IsStringFilter)

@given(instance=ccsl_filters_BlockLastStatementFilter_strategy)
@settings(max_examples=50)
def test_ccsl_filters_blocklaststatementfilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_BlockLastStatementFilter)

@given(instance=ccsl_filters_TemplateFilter_strategy)
@settings(max_examples=50)
def test_ccsl_filters_templatefilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_TemplateFilter)

@given(instance=ccsl_filters_ChildClosureComplexTypeFilter_strategy)
@settings(max_examples=50)
def test_ccsl_filters_childclosurecomplextypefilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_ChildClosureComplexTypeFilter)

@given(instance=ccsl_filters_FromClosureFilter_strategy)
@settings(max_examples=50)
def test_ccsl_filters_fromclosurefilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_FromClosureFilter)

@given(instance=ccsl_filters_SuperMethodClosureFilter_strategy)
@settings(max_examples=50)
def test_ccsl_filters_supermethodclosurefilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_SuperMethodClosureFilter)

@given(instance=ccsl_filters_IsTypeOfFilter_strategy)
@settings(max_examples=50)
def test_ccsl_filters_istypeoffilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_IsTypeOfFilter)

@given(instance=ccsl_filters_PropertyFilter_strategy)
@settings(max_examples=50)
def test_ccsl_filters_propertyfilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_PropertyFilter)

@given(instance=Filter_strategy)
@settings(max_examples=50)
def test_filter_instantiation(instance):
    assert isinstance(instance, Filter)

@given(instance=ccsl_filters_CompositeFilter_strategy)
@settings(max_examples=50)
def test_ccsl_filters_compositefilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_CompositeFilter)



@given(instance=ccsl_filters_CompositeFilter_strategy)
def test_ccsl_filters_compositefilter_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ccsl_filters_AtomicFilter_strategy)
@settings(max_examples=50)
def test_ccsl_filters_atomicfilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_AtomicFilter)

@given(instance=CcslBooleanFunction_strategy)
@settings(max_examples=50)
def test_ccslbooleanfunction_instantiation(instance):
    assert isinstance(instance, CcslBooleanFunction)

@given(instance=ccsl_filters_Filter_strategy)
@settings(max_examples=50)
def test_ccsl_filters_filter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_Filter)



@given(instance=ccsl_filters_Filter_strategy)
def test_ccsl_filters_filter_negated_setter(instance):
    original = instance.negated
    instance.negated = original
    assert instance.negated == original

@given(instance=CcslFunction_strategy)
@settings(max_examples=50)
def test_ccslfunction_instantiation(instance):
    assert isinstance(instance, CcslFunction)

@given(instance=ccsl_numberFunctions_CcslNumberFunction_strategy)
@settings(max_examples=50)
def test_ccsl_numberfunctions_ccslnumberfunction_instantiation(instance):
    assert isinstance(instance, ccsl_numberFunctions_CcslNumberFunction)

@given(instance=ccsl_booleanFunctions_CcslBooleanFunction_strategy)
@settings(max_examples=50)
def test_ccsl_booleanfunctions_ccslbooleanfunction_instantiation(instance):
    assert isinstance(instance, ccsl_booleanFunctions_CcslBooleanFunction)

@given(instance=ccsl_filters_ImplicityContainerFilter_strategy)
@settings(max_examples=50)
def test_ccsl_filters_implicitycontainerfilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_ImplicityContainerFilter)

@given(instance=expressions_OperatorExpression_strategy)
@settings(max_examples=50)
def test_expressions_operatorexpression_instantiation(instance):
    assert isinstance(instance, expressions_OperatorExpression)

@given(instance=TemplateFilter_strategy)
@settings(max_examples=50)
def test_templatefilter_instantiation(instance):
    assert isinstance(instance, TemplateFilter)

@given(instance=ccsl_filters_ImplicityOperandFilter_strategy)
@settings(max_examples=50)
def test_ccsl_filters_implicityoperandfilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_ImplicityOperandFilter)

@given(instance=ccsl_filters_RegexMatch_strategy)
@settings(max_examples=50)
def test_ccsl_filters_regexmatch_instantiation(instance):
    assert isinstance(instance, ccsl_filters_RegexMatch)



@given(instance=ccsl_filters_RegexMatch_strategy)
def test_ccsl_filters_regexmatch_regex_setter(instance):
    original = instance.regex
    instance.regex = original
    assert instance.regex == original

@given(instance=ccsl_filters_CountFilter_strategy)
@settings(max_examples=50)
def test_ccsl_filters_countfilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_CountFilter)



@given(instance=ccsl_filters_CountFilter_strategy)
def test_ccsl_filters_countfilter_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original



@given(instance=ccsl_filters_CountFilter_strategy)
def test_ccsl_filters_countfilter_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=ccsl_faultTypeDescription_InjectionAction_strategy)
@settings(max_examples=50)
def test_ccsl_faulttypedescription_injectionaction_instantiation(instance):
    assert isinstance(instance, ccsl_faultTypeDescription_InjectionAction)

@given(instance=filters_Filter_strategy)
@settings(max_examples=50)
def test_filters_filter_instantiation(instance):
    assert isinstance(instance, filters_Filter)

@given(instance=ccsl_context_Context_strategy)
@settings(max_examples=50)
def test_ccsl_context_context_instantiation(instance):
    assert isinstance(instance, ccsl_context_Context)

@given(instance=ccsl_datatype_VoidType_strategy)
@settings(max_examples=50)
def test_ccsl_datatype_voidtype_instantiation(instance):
    assert isinstance(instance, ccsl_datatype_VoidType)

@given(instance=ccsl_datatype_IntPrimitiveType_strategy)
@settings(max_examples=50)
def test_ccsl_datatype_intprimitivetype_instantiation(instance):
    assert isinstance(instance, ccsl_datatype_IntPrimitiveType)

@given(instance=ccsl_datatype_GenericType_strategy)
@settings(max_examples=50)
def test_ccsl_datatype_generictype_instantiation(instance):
    assert isinstance(instance, ccsl_datatype_GenericType)

@given(instance=ObjectType_strategy)
@settings(max_examples=50)
def test_objecttype_instantiation(instance):
    assert isinstance(instance, ObjectType)

@given(instance=ccsl_datatype_ArrayType_strategy)
@settings(max_examples=50)
def test_ccsl_datatype_arraytype_instantiation(instance):
    assert isinstance(instance, ccsl_datatype_ArrayType)



@given(instance=ccsl_datatype_ArrayType_strategy)
def test_ccsl_datatype_arraytype_dimensions_setter(instance):
    original = instance.dimensions
    instance.dimensions = original
    assert instance.dimensions == original

@given(instance=ccsl_datatype_ParameterizedType_strategy)
@settings(max_examples=50)
def test_ccsl_datatype_parameterizedtype_instantiation(instance):
    assert isinstance(instance, ccsl_datatype_ParameterizedType)

@given(instance=ccsl_datatype_ObjectType_strategy)
@settings(max_examples=50)
def test_ccsl_datatype_objecttype_instantiation(instance):
    assert isinstance(instance, ccsl_datatype_ObjectType)

@given(instance=ccsl_functions_CcslFunction_strategy)
@settings(max_examples=50)
def test_ccsl_functions_ccslfunction_instantiation(instance):
    assert isinstance(instance, ccsl_functions_CcslFunction)

@given(instance=ccsl_strategy_AllStrategy_strategy)
@settings(max_examples=50)
def test_ccsl_strategy_allstrategy_instantiation(instance):
    assert isinstance(instance, ccsl_strategy_AllStrategy)

@given(instance=ccsl_action_ArithmeticOperatorMap_strategy)
@settings(max_examples=50)
def test_ccsl_action_arithmeticoperatormap_instantiation(instance):
    assert isinstance(instance, ccsl_action_ArithmeticOperatorMap)



@given(instance=ccsl_action_ArithmeticOperatorMap_strategy)
def test_ccsl_action_arithmeticoperatormap_oldArithmeticOperator_setter(instance):
    original = instance.oldArithmeticOperator
    instance.oldArithmeticOperator = original
    assert instance.oldArithmeticOperator == original



@given(instance=ccsl_action_ArithmeticOperatorMap_strategy)
def test_ccsl_action_arithmeticoperatormap_newArithmeticOperator_setter(instance):
    original = instance.newArithmeticOperator
    instance.newArithmeticOperator = original
    assert instance.newArithmeticOperator == original

@given(instance=action_ArithmeticOperatorMap_strategy)
@settings(max_examples=50)
def test_action_arithmeticoperatormap_instantiation(instance):
    assert isinstance(instance, action_ArithmeticOperatorMap)

@given(instance=ccsl_action_ReplaceArithmeticOperatorAction_strategy)
@settings(max_examples=50)
def test_ccsl_action_replacearithmeticoperatoraction_instantiation(instance):
    assert isinstance(instance, ccsl_action_ReplaceArithmeticOperatorAction)

@given(instance=ccsl_action_ReplaceVariableAccessAction_strategy)
@settings(max_examples=50)
def test_ccsl_action_replacevariableaccessaction_instantiation(instance):
    assert isinstance(instance, ccsl_action_ReplaceVariableAccessAction)

@given(instance=ccsl_action_DeleteRandomStatementAction_strategy)
@settings(max_examples=50)
def test_ccsl_action_deleterandomstatementaction_instantiation(instance):
    assert isinstance(instance, ccsl_action_DeleteRandomStatementAction)

@given(instance=ccsl_action_ChangeLiteralValueAction_strategy)
@settings(max_examples=50)
def test_ccsl_action_changeliteralvalueaction_instantiation(instance):
    assert isinstance(instance, ccsl_action_ChangeLiteralValueAction)

@given(instance=ccsl_action_DeleteInfixOperatorAction_strategy)
@settings(max_examples=50)
def test_ccsl_action_deleteinfixoperatoraction_instantiation(instance):
    assert isinstance(instance, ccsl_action_DeleteInfixOperatorAction)

@given(instance=ccsl_action_MoveScopeUpAction_strategy)
@settings(max_examples=50)
def test_ccsl_action_movescopeupaction_instantiation(instance):
    assert isinstance(instance, ccsl_action_MoveScopeUpAction)

@given(instance=ccsl_action_DeleteAction_strategy)
@settings(max_examples=50)
def test_ccsl_action_deleteaction_instantiation(instance):
    assert isinstance(instance, ccsl_action_DeleteAction)

@given(instance=ccsl_faultTypeDescription_InjectionStrategy_strategy)
@settings(max_examples=50)
def test_ccsl_faulttypedescription_injectionstrategy_instantiation(instance):
    assert isinstance(instance, ccsl_faultTypeDescription_InjectionStrategy)

@given(instance=ccsl_import_ImportStatement_strategy)
@settings(max_examples=50)
def test_ccsl_import_importstatement_instantiation(instance):
    assert isinstance(instance, ccsl_import_ImportStatement)

@given(instance=ccsl_import_ImportableElement_strategy)
@settings(max_examples=50)
def test_ccsl_import_importableelement_instantiation(instance):
    assert isinstance(instance, ccsl_import_ImportableElement)

@given(instance=Invocation_strategy)
@settings(max_examples=50)
def test_invocation_instantiation(instance):
    assert isinstance(instance, Invocation)

@given(instance=ccsl_invocation_SimpleMethodInvocation_strategy)
@settings(max_examples=50)
def test_ccsl_invocation_simplemethodinvocation_instantiation(instance):
    assert isinstance(instance, ccsl_invocation_SimpleMethodInvocation)

@given(instance=ccsl_invocation_ConstructorInvocation_strategy)
@settings(max_examples=50)
def test_ccsl_invocation_constructorinvocation_instantiation(instance):
    assert isinstance(instance, ccsl_invocation_ConstructorInvocation)

@given(instance=ccsl_invocation_Invocation_strategy)
@settings(max_examples=50)
def test_ccsl_invocation_invocation_instantiation(instance):
    assert isinstance(instance, ccsl_invocation_Invocation)



@given(instance=ccsl_invocation_Invocation_strategy)
def test_ccsl_invocation_invocation_argsKind_setter(instance):
    original = instance.argsKind
    instance.argsKind = original
    assert instance.argsKind == original

@given(instance=SimpleMethodInvocation_strategy)
@settings(max_examples=50)
def test_simplemethodinvocation_instantiation(instance):
    assert isinstance(instance, SimpleMethodInvocation)

@given(instance=ccsl_invocation_SuperMethodInvocation_strategy)
@settings(max_examples=50)
def test_ccsl_invocation_supermethodinvocation_instantiation(instance):
    assert isinstance(instance, ccsl_invocation_SuperMethodInvocation)

@given(instance=ccsl_invocation_MethodInvocation_strategy)
@settings(max_examples=50)
def test_ccsl_invocation_methodinvocation_instantiation(instance):
    assert isinstance(instance, ccsl_invocation_MethodInvocation)

@given(instance=ccsl_datatype_ShortPrimitiveType_strategy)
@settings(max_examples=50)
def test_ccsl_datatype_shortprimitivetype_instantiation(instance):
    assert isinstance(instance, ccsl_datatype_ShortPrimitiveType)

@given(instance=ccsl_datatype_BooleanPrimitiveType_strategy)
@settings(max_examples=50)
def test_ccsl_datatype_booleanprimitivetype_instantiation(instance):
    assert isinstance(instance, ccsl_datatype_BooleanPrimitiveType)
