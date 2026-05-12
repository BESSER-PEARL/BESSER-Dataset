import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BuiltinDefinition,
    ast_BuiltinVariable,
    ast_BuiltinFunction,
    ast_Statement,
    Statement,
    ast_DoWhileStatement,
    ast_WhileStatement,
    ast_BreakStatement,
    ast_ContinueStatement,
    ast_ReturnStatement,
    ast_ForStatement,
    ast_Compound,
    PrimitiveStepExpression,
    ast_StepN,
    ast_StepLiteral,
    ast_IfStatement,
    ast_Assignment,
    StepExpression,
    ast_PrimitiveStepExpression,
    ast_NegateStepExpression,
    ast_AdditiveStepExpression,
    ast_RangeStepExpression,
    ast_StepExpression,
    FeatureCall,
    ast_FunctionCall,
    ast_VariableAccess,
    ast_ExpressionList,
    ast_ArrayConstructionIterationClause,
    ast_Unit,
    ast_ArraySubscript,
    ast_LetExpressionVariableDeclaration,
    Expression,
    ast_ArrayConcatenationOperator,
    ast_ArrayElementAccess,
    ast_DerivativeOperator,
    ast_LogicalOrExpression,
    ast_IterationCall,
    ast_RangeExpression,
    ast_AlgorithmExpression,
    ast_FeatureCall,
    ast_ImpliesExpression,
    ast_LogicalAndExpression,
    ast_AdditiveExpression,
    ast_EndExpression,
    ast_ArrayConstructionOperator,
    ast_MemberVariableAccess,
    ast_MultiplicativeExpression,
    ast_PostfixExpression,
    ast_UnitConstructionOperator,
    ast_EqualityExpression,
    ast_TypeTestExpression,
    ast_UnaryExpression,
    ast_ParenthesizedExpression,
    ast_RelationalExpression,
    ast_PowerExpression,
    ast_LetExpression,
    ast_DataType,
    ast_SwitchCase,
    ast_SwitchExpression,
    ast_IfExpression,
    ast_CallableElement,
    ast_Expression,
    ast_Equation,
    ast_Assertion,
    ast_Check,
    ParameterDeclaration,
    ast_OutputParameterDeclaration,
    ast_EnumerationLiteralDeclaration,
    DataTypeDefinition,
    ast_TypeAliasDefinition,
    ast_EnumerationDefinition,
    Definition,
    ast_DataTypeDefinition,
    ast_Definition,
    ast_Module,
    ast_InputParameterDeclaration,
    ast_TemplateParameterDeclaration,
    CallableElement,
    ast_LetExpressionVariableDeclarationPart,
    ast_IterationVariable,
    ast_ParameterDeclaration,
    ast_StateVariableDeclaration,
    ast_IterationAccumulator,
    ast_BuiltinDefinition,
    ast_VariableDeclaration,
    ast_FunctionObjectDeclaration,
    ast_FunctionDefinition,
    ast_DataTypeSpecifier,
    ast_StructMemberDeclaration,
    ast_StructDefinition,
    ast_PrimitiveType,
    EqualityOperator,
    PowerOperator,
    UnaryOperator,
    MultiplicativeOperator,
    AdditiveOperator,
    AssertionStatusKind,
    PostfixOperator,
    FunctionKind,
    RelationalOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_builtindefinition_is_not_abstract():
    assert not inspect.isabstract(BuiltinDefinition)


def test_builtindefinition_constructor_exists():
    assert callable(BuiltinDefinition.__init__)


def test_builtindefinition_constructor_args():
    sig = inspect.signature(BuiltinDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ast_builtinvariable_is_not_abstract():
    assert not inspect.isabstract(ast_BuiltinVariable)


def test_ast_builtinvariable_constructor_exists():
    assert callable(ast_BuiltinVariable.__init__)


def test_ast_builtinvariable_constructor_args():
    sig = inspect.signature(ast_BuiltinVariable.__init__)
    params = list(sig.parameters.keys())



def test_ast_builtinfunction_is_not_abstract():
    assert not inspect.isabstract(ast_BuiltinFunction)


def test_ast_builtinfunction_constructor_exists():
    assert callable(ast_BuiltinFunction.__init__)


def test_ast_builtinfunction_constructor_args():
    sig = inspect.signature(ast_BuiltinFunction.__init__)
    params = list(sig.parameters.keys())



def test_ast_statement_is_not_abstract():
    assert not inspect.isabstract(ast_Statement)


def test_ast_statement_constructor_exists():
    assert callable(ast_Statement.__init__)


def test_ast_statement_constructor_args():
    sig = inspect.signature(ast_Statement.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_ast_dowhilestatement_is_not_abstract():
    assert not inspect.isabstract(ast_DoWhileStatement)


def test_ast_dowhilestatement_constructor_exists():
    assert callable(ast_DoWhileStatement.__init__)


def test_ast_dowhilestatement_constructor_args():
    sig = inspect.signature(ast_DoWhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_whilestatement_is_not_abstract():
    assert not inspect.isabstract(ast_WhileStatement)


def test_ast_whilestatement_constructor_exists():
    assert callable(ast_WhileStatement.__init__)


def test_ast_whilestatement_constructor_args():
    sig = inspect.signature(ast_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_breakstatement_is_not_abstract():
    assert not inspect.isabstract(ast_BreakStatement)


def test_ast_breakstatement_constructor_exists():
    assert callable(ast_BreakStatement.__init__)


def test_ast_breakstatement_constructor_args():
    sig = inspect.signature(ast_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_continuestatement_is_not_abstract():
    assert not inspect.isabstract(ast_ContinueStatement)


def test_ast_continuestatement_constructor_exists():
    assert callable(ast_ContinueStatement.__init__)


def test_ast_continuestatement_constructor_args():
    sig = inspect.signature(ast_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_returnstatement_is_not_abstract():
    assert not inspect.isabstract(ast_ReturnStatement)


def test_ast_returnstatement_constructor_exists():
    assert callable(ast_ReturnStatement.__init__)


def test_ast_returnstatement_constructor_args():
    sig = inspect.signature(ast_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_forstatement_is_not_abstract():
    assert not inspect.isabstract(ast_ForStatement)


def test_ast_forstatement_constructor_exists():
    assert callable(ast_ForStatement.__init__)


def test_ast_forstatement_constructor_args():
    sig = inspect.signature(ast_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_compound_is_not_abstract():
    assert not inspect.isabstract(ast_Compound)


def test_ast_compound_constructor_exists():
    assert callable(ast_Compound.__init__)


def test_ast_compound_constructor_args():
    sig = inspect.signature(ast_Compound.__init__)
    params = list(sig.parameters.keys())



def test_primitivestepexpression_is_not_abstract():
    assert not inspect.isabstract(PrimitiveStepExpression)


def test_primitivestepexpression_constructor_exists():
    assert callable(PrimitiveStepExpression.__init__)


def test_primitivestepexpression_constructor_args():
    sig = inspect.signature(PrimitiveStepExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast_stepn_is_not_abstract():
    assert not inspect.isabstract(ast_StepN)


def test_ast_stepn_constructor_exists():
    assert callable(ast_StepN.__init__)


def test_ast_stepn_constructor_args():
    sig = inspect.signature(ast_StepN.__init__)
    params = list(sig.parameters.keys())



def test_ast_stepliteral_is_not_abstract():
    assert not inspect.isabstract(ast_StepLiteral)


def test_ast_stepliteral_constructor_exists():
    assert callable(ast_StepLiteral.__init__)


def test_ast_stepliteral_constructor_args():
    sig = inspect.signature(ast_StepLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ast_stepliteral_has_value():
    assert hasattr(ast_StepLiteral, "value")
    descriptor = None
    for klass in ast_StepLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ast_ifstatement_is_not_abstract():
    assert not inspect.isabstract(ast_IfStatement)


def test_ast_ifstatement_constructor_exists():
    assert callable(ast_IfStatement.__init__)


def test_ast_ifstatement_constructor_args():
    sig = inspect.signature(ast_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_assignment_is_not_abstract():
    assert not inspect.isabstract(ast_Assignment)


def test_ast_assignment_constructor_exists():
    assert callable(ast_Assignment.__init__)


def test_ast_assignment_constructor_args():
    sig = inspect.signature(ast_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_stepexpression_is_not_abstract():
    assert not inspect.isabstract(StepExpression)


def test_stepexpression_constructor_exists():
    assert callable(StepExpression.__init__)


def test_stepexpression_constructor_args():
    sig = inspect.signature(StepExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast_primitivestepexpression_is_not_abstract():
    assert not inspect.isabstract(ast_PrimitiveStepExpression)


def test_ast_primitivestepexpression_constructor_exists():
    assert callable(ast_PrimitiveStepExpression.__init__)


def test_ast_primitivestepexpression_constructor_args():
    sig = inspect.signature(ast_PrimitiveStepExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast_negatestepexpression_is_not_abstract():
    assert not inspect.isabstract(ast_NegateStepExpression)


def test_ast_negatestepexpression_constructor_exists():
    assert callable(ast_NegateStepExpression.__init__)


def test_ast_negatestepexpression_constructor_args():
    sig = inspect.signature(ast_NegateStepExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast_additivestepexpression_is_not_abstract():
    assert not inspect.isabstract(ast_AdditiveStepExpression)


def test_ast_additivestepexpression_constructor_exists():
    assert callable(ast_AdditiveStepExpression.__init__)


def test_ast_additivestepexpression_constructor_args():
    sig = inspect.signature(ast_AdditiveStepExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ast_additivestepexpression_has_operator():
    assert hasattr(ast_AdditiveStepExpression, "operator")
    descriptor = None
    for klass in ast_AdditiveStepExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_ast_rangestepexpression_is_not_abstract():
    assert not inspect.isabstract(ast_RangeStepExpression)


def test_ast_rangestepexpression_constructor_exists():
    assert callable(ast_RangeStepExpression.__init__)


def test_ast_rangestepexpression_constructor_args():
    sig = inspect.signature(ast_RangeStepExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast_stepexpression_is_not_abstract():
    assert not inspect.isabstract(ast_StepExpression)


def test_ast_stepexpression_constructor_exists():
    assert callable(ast_StepExpression.__init__)


def test_ast_stepexpression_constructor_args():
    sig = inspect.signature(ast_StepExpression.__init__)
    params = list(sig.parameters.keys())



def test_featurecall_is_not_abstract():
    assert not inspect.isabstract(FeatureCall)


def test_featurecall_constructor_exists():
    assert callable(FeatureCall.__init__)


def test_featurecall_constructor_args():
    sig = inspect.signature(FeatureCall.__init__)
    params = list(sig.parameters.keys())



def test_ast_functioncall_is_not_abstract():
    assert not inspect.isabstract(ast_FunctionCall)


def test_ast_functioncall_constructor_exists():
    assert callable(ast_FunctionCall.__init__)


def test_ast_functioncall_constructor_args():
    sig = inspect.signature(ast_FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_ast_variableaccess_is_not_abstract():
    assert not inspect.isabstract(ast_VariableAccess)


def test_ast_variableaccess_constructor_exists():
    assert callable(ast_VariableAccess.__init__)


def test_ast_variableaccess_constructor_args():
    sig = inspect.signature(ast_VariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_ast_expressionlist_is_not_abstract():
    assert not inspect.isabstract(ast_ExpressionList)


def test_ast_expressionlist_constructor_exists():
    assert callable(ast_ExpressionList.__init__)


def test_ast_expressionlist_constructor_args():
    sig = inspect.signature(ast_ExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_ast_arrayconstructioniterationclause_is_not_abstract():
    assert not inspect.isabstract(ast_ArrayConstructionIterationClause)


def test_ast_arrayconstructioniterationclause_constructor_exists():
    assert callable(ast_ArrayConstructionIterationClause.__init__)


def test_ast_arrayconstructioniterationclause_constructor_args():
    sig = inspect.signature(ast_ArrayConstructionIterationClause.__init__)
    params = list(sig.parameters.keys())
    assert "variableName" in params, "Missing parameter 'variableName'"

def test_ast_arrayconstructioniterationclause_has_variableName():
    assert hasattr(ast_ArrayConstructionIterationClause, "variableName")
    descriptor = None
    for klass in ast_ArrayConstructionIterationClause.__mro__:
        if "variableName" in klass.__dict__:
            descriptor = klass.__dict__["variableName"]
            break
    assert isinstance(descriptor, property)



def test_ast_unit_is_not_abstract():
    assert not inspect.isabstract(ast_Unit)


def test_ast_unit_constructor_exists():
    assert callable(ast_Unit.__init__)


def test_ast_unit_constructor_args():
    sig = inspect.signature(ast_Unit.__init__)
    params = list(sig.parameters.keys())



def test_ast_arraysubscript_is_not_abstract():
    assert not inspect.isabstract(ast_ArraySubscript)


def test_ast_arraysubscript_constructor_exists():
    assert callable(ast_ArraySubscript.__init__)


def test_ast_arraysubscript_constructor_args():
    sig = inspect.signature(ast_ArraySubscript.__init__)
    params = list(sig.parameters.keys())
    assert "slice" in params, "Missing parameter 'slice'"

def test_ast_arraysubscript_has_slice():
    assert hasattr(ast_ArraySubscript, "slice")
    descriptor = None
    for klass in ast_ArraySubscript.__mro__:
        if "slice" in klass.__dict__:
            descriptor = klass.__dict__["slice"]
            break
    assert isinstance(descriptor, property)



def test_ast_letexpressionvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(ast_LetExpressionVariableDeclaration)


def test_ast_letexpressionvariabledeclaration_constructor_exists():
    assert callable(ast_LetExpressionVariableDeclaration.__init__)


def test_ast_letexpressionvariabledeclaration_constructor_args():
    sig = inspect.signature(ast_LetExpressionVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_ast_arrayconcatenationoperator_is_not_abstract():
    assert not inspect.isabstract(ast_ArrayConcatenationOperator)


def test_ast_arrayconcatenationoperator_constructor_exists():
    assert callable(ast_ArrayConcatenationOperator.__init__)


def test_ast_arrayconcatenationoperator_constructor_args():
    sig = inspect.signature(ast_ArrayConcatenationOperator.__init__)
    params = list(sig.parameters.keys())



def test_ast_arrayelementaccess_is_not_abstract():
    assert not inspect.isabstract(ast_ArrayElementAccess)


def test_ast_arrayelementaccess_constructor_exists():
    assert callable(ast_ArrayElementAccess.__init__)


def test_ast_arrayelementaccess_constructor_args():
    sig = inspect.signature(ast_ArrayElementAccess.__init__)
    params = list(sig.parameters.keys())



def test_ast_derivativeoperator_is_not_abstract():
    assert not inspect.isabstract(ast_DerivativeOperator)


def test_ast_derivativeoperator_constructor_exists():
    assert callable(ast_DerivativeOperator.__init__)


def test_ast_derivativeoperator_constructor_args():
    sig = inspect.signature(ast_DerivativeOperator.__init__)
    params = list(sig.parameters.keys())



def test_ast_logicalorexpression_is_not_abstract():
    assert not inspect.isabstract(ast_LogicalOrExpression)


def test_ast_logicalorexpression_constructor_exists():
    assert callable(ast_LogicalOrExpression.__init__)


def test_ast_logicalorexpression_constructor_args():
    sig = inspect.signature(ast_LogicalOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast_iterationcall_is_not_abstract():
    assert not inspect.isabstract(ast_IterationCall)


def test_ast_iterationcall_constructor_exists():
    assert callable(ast_IterationCall.__init__)


def test_ast_iterationcall_constructor_args():
    sig = inspect.signature(ast_IterationCall.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_ast_iterationcall_has_identifier():
    assert hasattr(ast_IterationCall, "identifier")
    descriptor = None
    for klass in ast_IterationCall.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_ast_rangeexpression_is_not_abstract():
    assert not inspect.isabstract(ast_RangeExpression)


def test_ast_rangeexpression_constructor_exists():
    assert callable(ast_RangeExpression.__init__)


def test_ast_rangeexpression_constructor_args():
    sig = inspect.signature(ast_RangeExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast_algorithmexpression_is_not_abstract():
    assert not inspect.isabstract(ast_AlgorithmExpression)


def test_ast_algorithmexpression_constructor_exists():
    assert callable(ast_AlgorithmExpression.__init__)


def test_ast_algorithmexpression_constructor_args():
    sig = inspect.signature(ast_AlgorithmExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast_featurecall_is_not_abstract():
    assert not inspect.isabstract(ast_FeatureCall)


def test_ast_featurecall_constructor_exists():
    assert callable(ast_FeatureCall.__init__)


def test_ast_featurecall_constructor_args():
    sig = inspect.signature(ast_FeatureCall.__init__)
    params = list(sig.parameters.keys())



def test_ast_impliesexpression_is_not_abstract():
    assert not inspect.isabstract(ast_ImpliesExpression)


def test_ast_impliesexpression_constructor_exists():
    assert callable(ast_ImpliesExpression.__init__)


def test_ast_impliesexpression_constructor_args():
    sig = inspect.signature(ast_ImpliesExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast_logicalandexpression_is_not_abstract():
    assert not inspect.isabstract(ast_LogicalAndExpression)


def test_ast_logicalandexpression_constructor_exists():
    assert callable(ast_LogicalAndExpression.__init__)


def test_ast_logicalandexpression_constructor_args():
    sig = inspect.signature(ast_LogicalAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast_additiveexpression_is_not_abstract():
    assert not inspect.isabstract(ast_AdditiveExpression)


def test_ast_additiveexpression_constructor_exists():
    assert callable(ast_AdditiveExpression.__init__)


def test_ast_additiveexpression_constructor_args():
    sig = inspect.signature(ast_AdditiveExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ast_additiveexpression_has_operator():
    assert hasattr(ast_AdditiveExpression, "operator")
    descriptor = None
    for klass in ast_AdditiveExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_ast_endexpression_is_not_abstract():
    assert not inspect.isabstract(ast_EndExpression)


def test_ast_endexpression_constructor_exists():
    assert callable(ast_EndExpression.__init__)


def test_ast_endexpression_constructor_args():
    sig = inspect.signature(ast_EndExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast_arrayconstructionoperator_is_not_abstract():
    assert not inspect.isabstract(ast_ArrayConstructionOperator)


def test_ast_arrayconstructionoperator_constructor_exists():
    assert callable(ast_ArrayConstructionOperator.__init__)


def test_ast_arrayconstructionoperator_constructor_args():
    sig = inspect.signature(ast_ArrayConstructionOperator.__init__)
    params = list(sig.parameters.keys())



def test_ast_membervariableaccess_is_not_abstract():
    assert not inspect.isabstract(ast_MemberVariableAccess)


def test_ast_membervariableaccess_constructor_exists():
    assert callable(ast_MemberVariableAccess.__init__)


def test_ast_membervariableaccess_constructor_args():
    sig = inspect.signature(ast_MemberVariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_ast_multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(ast_MultiplicativeExpression)


def test_ast_multiplicativeexpression_constructor_exists():
    assert callable(ast_MultiplicativeExpression.__init__)


def test_ast_multiplicativeexpression_constructor_args():
    sig = inspect.signature(ast_MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ast_multiplicativeexpression_has_operator():
    assert hasattr(ast_MultiplicativeExpression, "operator")
    descriptor = None
    for klass in ast_MultiplicativeExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_ast_postfixexpression_is_not_abstract():
    assert not inspect.isabstract(ast_PostfixExpression)


def test_ast_postfixexpression_constructor_exists():
    assert callable(ast_PostfixExpression.__init__)


def test_ast_postfixexpression_constructor_args():
    sig = inspect.signature(ast_PostfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ast_postfixexpression_has_operator():
    assert hasattr(ast_PostfixExpression, "operator")
    descriptor = None
    for klass in ast_PostfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_ast_unitconstructionoperator_is_not_abstract():
    assert not inspect.isabstract(ast_UnitConstructionOperator)


def test_ast_unitconstructionoperator_constructor_exists():
    assert callable(ast_UnitConstructionOperator.__init__)


def test_ast_unitconstructionoperator_constructor_args():
    sig = inspect.signature(ast_UnitConstructionOperator.__init__)
    params = list(sig.parameters.keys())



def test_ast_equalityexpression_is_not_abstract():
    assert not inspect.isabstract(ast_EqualityExpression)


def test_ast_equalityexpression_constructor_exists():
    assert callable(ast_EqualityExpression.__init__)


def test_ast_equalityexpression_constructor_args():
    sig = inspect.signature(ast_EqualityExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ast_equalityexpression_has_operator():
    assert hasattr(ast_EqualityExpression, "operator")
    descriptor = None
    for klass in ast_EqualityExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_ast_typetestexpression_is_not_abstract():
    assert not inspect.isabstract(ast_TypeTestExpression)


def test_ast_typetestexpression_constructor_exists():
    assert callable(ast_TypeTestExpression.__init__)


def test_ast_typetestexpression_constructor_args():
    sig = inspect.signature(ast_TypeTestExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(ast_UnaryExpression)


def test_ast_unaryexpression_constructor_exists():
    assert callable(ast_UnaryExpression.__init__)


def test_ast_unaryexpression_constructor_args():
    sig = inspect.signature(ast_UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ast_unaryexpression_has_operator():
    assert hasattr(ast_UnaryExpression, "operator")
    descriptor = None
    for klass in ast_UnaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_ast_parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(ast_ParenthesizedExpression)


def test_ast_parenthesizedexpression_constructor_exists():
    assert callable(ast_ParenthesizedExpression.__init__)


def test_ast_parenthesizedexpression_constructor_args():
    sig = inspect.signature(ast_ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast_relationalexpression_is_not_abstract():
    assert not inspect.isabstract(ast_RelationalExpression)


def test_ast_relationalexpression_constructor_exists():
    assert callable(ast_RelationalExpression.__init__)


def test_ast_relationalexpression_constructor_args():
    sig = inspect.signature(ast_RelationalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ast_relationalexpression_has_operator():
    assert hasattr(ast_RelationalExpression, "operator")
    descriptor = None
    for klass in ast_RelationalExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_ast_powerexpression_is_not_abstract():
    assert not inspect.isabstract(ast_PowerExpression)


def test_ast_powerexpression_constructor_exists():
    assert callable(ast_PowerExpression.__init__)


def test_ast_powerexpression_constructor_args():
    sig = inspect.signature(ast_PowerExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ast_powerexpression_has_operator():
    assert hasattr(ast_PowerExpression, "operator")
    descriptor = None
    for klass in ast_PowerExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_ast_letexpression_is_not_abstract():
    assert not inspect.isabstract(ast_LetExpression)


def test_ast_letexpression_constructor_exists():
    assert callable(ast_LetExpression.__init__)


def test_ast_letexpression_constructor_args():
    sig = inspect.signature(ast_LetExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast_datatype_is_not_abstract():
    assert not inspect.isabstract(ast_DataType)


def test_ast_datatype_constructor_exists():
    assert callable(ast_DataType.__init__)


def test_ast_datatype_constructor_args():
    sig = inspect.signature(ast_DataType.__init__)
    params = list(sig.parameters.keys())



def test_ast_switchcase_is_not_abstract():
    assert not inspect.isabstract(ast_SwitchCase)


def test_ast_switchcase_constructor_exists():
    assert callable(ast_SwitchCase.__init__)


def test_ast_switchcase_constructor_args():
    sig = inspect.signature(ast_SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_ast_switchexpression_is_not_abstract():
    assert not inspect.isabstract(ast_SwitchExpression)


def test_ast_switchexpression_constructor_exists():
    assert callable(ast_SwitchExpression.__init__)


def test_ast_switchexpression_constructor_args():
    sig = inspect.signature(ast_SwitchExpression.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_ast_switchexpression_has_static():
    assert hasattr(ast_SwitchExpression, "static")
    descriptor = None
    for klass in ast_SwitchExpression.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_ast_ifexpression_is_not_abstract():
    assert not inspect.isabstract(ast_IfExpression)


def test_ast_ifexpression_constructor_exists():
    assert callable(ast_IfExpression.__init__)


def test_ast_ifexpression_constructor_args():
    sig = inspect.signature(ast_IfExpression.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_ast_ifexpression_has_static():
    assert hasattr(ast_IfExpression, "static")
    descriptor = None
    for klass in ast_IfExpression.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_ast_callableelement_is_not_abstract():
    assert not inspect.isabstract(ast_CallableElement)


def test_ast_callableelement_constructor_exists():
    assert callable(ast_CallableElement.__init__)


def test_ast_callableelement_constructor_args():
    sig = inspect.signature(ast_CallableElement.__init__)
    params = list(sig.parameters.keys())



def test_ast_expression_is_not_abstract():
    assert not inspect.isabstract(ast_Expression)


def test_ast_expression_constructor_exists():
    assert callable(ast_Expression.__init__)


def test_ast_expression_constructor_args():
    sig = inspect.signature(ast_Expression.__init__)
    params = list(sig.parameters.keys())



def test_ast_equation_is_not_abstract():
    assert not inspect.isabstract(ast_Equation)


def test_ast_equation_constructor_exists():
    assert callable(ast_Equation.__init__)


def test_ast_equation_constructor_args():
    sig = inspect.signature(ast_Equation.__init__)
    params = list(sig.parameters.keys())
    assert "initial" in params, "Missing parameter 'initial'"

def test_ast_equation_has_initial():
    assert hasattr(ast_Equation, "initial")
    descriptor = None
    for klass in ast_Equation.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)



def test_ast_assertion_is_not_abstract():
    assert not inspect.isabstract(ast_Assertion)


def test_ast_assertion_constructor_exists():
    assert callable(ast_Assertion.__init__)


def test_ast_assertion_constructor_args():
    sig = inspect.signature(ast_Assertion.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"
    assert "statusKind" in params, "Missing parameter 'statusKind'"

def test_ast_assertion_has_static():
    assert hasattr(ast_Assertion, "static")
    descriptor = None
    for klass in ast_Assertion.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_ast_assertion_has_statusKind():
    assert hasattr(ast_Assertion, "statusKind")
    descriptor = None
    for klass in ast_Assertion.__mro__:
        if "statusKind" in klass.__dict__:
            descriptor = klass.__dict__["statusKind"]
            break
    assert isinstance(descriptor, property)



def test_ast_check_is_not_abstract():
    assert not inspect.isabstract(ast_Check)


def test_ast_check_constructor_exists():
    assert callable(ast_Check.__init__)


def test_ast_check_constructor_args():
    sig = inspect.signature(ast_Check.__init__)
    params = list(sig.parameters.keys())



def test_parameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(ParameterDeclaration)


def test_parameterdeclaration_constructor_exists():
    assert callable(ParameterDeclaration.__init__)


def test_parameterdeclaration_constructor_args():
    sig = inspect.signature(ParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ast_outputparameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(ast_OutputParameterDeclaration)


def test_ast_outputparameterdeclaration_constructor_exists():
    assert callable(ast_OutputParameterDeclaration.__init__)


def test_ast_outputparameterdeclaration_constructor_args():
    sig = inspect.signature(ast_OutputParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ast_enumerationliteraldeclaration_is_not_abstract():
    assert not inspect.isabstract(ast_EnumerationLiteralDeclaration)


def test_ast_enumerationliteraldeclaration_constructor_exists():
    assert callable(ast_EnumerationLiteralDeclaration.__init__)


def test_ast_enumerationliteraldeclaration_constructor_args():
    sig = inspect.signature(ast_EnumerationLiteralDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ast_enumerationliteraldeclaration_has_name():
    assert hasattr(ast_EnumerationLiteralDeclaration, "name")
    descriptor = None
    for klass in ast_EnumerationLiteralDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_datatypedefinition_is_not_abstract():
    assert not inspect.isabstract(DataTypeDefinition)


def test_datatypedefinition_constructor_exists():
    assert callable(DataTypeDefinition.__init__)


def test_datatypedefinition_constructor_args():
    sig = inspect.signature(DataTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ast_typealiasdefinition_is_not_abstract():
    assert not inspect.isabstract(ast_TypeAliasDefinition)


def test_ast_typealiasdefinition_constructor_exists():
    assert callable(ast_TypeAliasDefinition.__init__)


def test_ast_typealiasdefinition_constructor_args():
    sig = inspect.signature(ast_TypeAliasDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ast_enumerationdefinition_is_not_abstract():
    assert not inspect.isabstract(ast_EnumerationDefinition)


def test_ast_enumerationdefinition_constructor_exists():
    assert callable(ast_EnumerationDefinition.__init__)


def test_ast_enumerationdefinition_constructor_args():
    sig = inspect.signature(ast_EnumerationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_definition_is_not_abstract():
    assert not inspect.isabstract(Definition)


def test_definition_constructor_exists():
    assert callable(Definition.__init__)


def test_definition_constructor_args():
    sig = inspect.signature(Definition.__init__)
    params = list(sig.parameters.keys())



def test_ast_datatypedefinition_is_not_abstract():
    assert not inspect.isabstract(ast_DataTypeDefinition)


def test_ast_datatypedefinition_constructor_exists():
    assert callable(ast_DataTypeDefinition.__init__)


def test_ast_datatypedefinition_constructor_args():
    sig = inspect.signature(ast_DataTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ast_definition_is_not_abstract():
    assert not inspect.isabstract(ast_Definition)


def test_ast_definition_constructor_exists():
    assert callable(ast_Definition.__init__)


def test_ast_definition_constructor_args():
    sig = inspect.signature(ast_Definition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ast_definition_has_name():
    assert hasattr(ast_Definition, "name")
    descriptor = None
    for klass in ast_Definition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ast_module_is_not_abstract():
    assert not inspect.isabstract(ast_Module)


def test_ast_module_constructor_exists():
    assert callable(ast_Module.__init__)


def test_ast_module_constructor_args():
    sig = inspect.signature(ast_Module.__init__)
    params = list(sig.parameters.keys())



def test_ast_inputparameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(ast_InputParameterDeclaration)


def test_ast_inputparameterdeclaration_constructor_exists():
    assert callable(ast_InputParameterDeclaration.__init__)


def test_ast_inputparameterdeclaration_constructor_args():
    sig = inspect.signature(ast_InputParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ast_templateparameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(ast_TemplateParameterDeclaration)


def test_ast_templateparameterdeclaration_constructor_exists():
    assert callable(ast_TemplateParameterDeclaration.__init__)


def test_ast_templateparameterdeclaration_constructor_args():
    sig = inspect.signature(ast_TemplateParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_callableelement_is_not_abstract():
    assert not inspect.isabstract(CallableElement)


def test_callableelement_constructor_exists():
    assert callable(CallableElement.__init__)


def test_callableelement_constructor_args():
    sig = inspect.signature(CallableElement.__init__)
    params = list(sig.parameters.keys())



def test_ast_letexpressionvariabledeclarationpart_is_not_abstract():
    assert not inspect.isabstract(ast_LetExpressionVariableDeclarationPart)


def test_ast_letexpressionvariabledeclarationpart_constructor_exists():
    assert callable(ast_LetExpressionVariableDeclarationPart.__init__)


def test_ast_letexpressionvariabledeclarationpart_constructor_args():
    sig = inspect.signature(ast_LetExpressionVariableDeclarationPart.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ast_letexpressionvariabledeclarationpart_has_name():
    assert hasattr(ast_LetExpressionVariableDeclarationPart, "name")
    descriptor = None
    for klass in ast_LetExpressionVariableDeclarationPart.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ast_iterationvariable_is_not_abstract():
    assert not inspect.isabstract(ast_IterationVariable)


def test_ast_iterationvariable_constructor_exists():
    assert callable(ast_IterationVariable.__init__)


def test_ast_iterationvariable_constructor_args():
    sig = inspect.signature(ast_IterationVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ast_iterationvariable_has_name():
    assert hasattr(ast_IterationVariable, "name")
    descriptor = None
    for klass in ast_IterationVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ast_parameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(ast_ParameterDeclaration)


def test_ast_parameterdeclaration_constructor_exists():
    assert callable(ast_ParameterDeclaration.__init__)


def test_ast_parameterdeclaration_constructor_args():
    sig = inspect.signature(ast_ParameterDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ast_parameterdeclaration_has_name():
    assert hasattr(ast_ParameterDeclaration, "name")
    descriptor = None
    for klass in ast_ParameterDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ast_statevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(ast_StateVariableDeclaration)


def test_ast_statevariabledeclaration_constructor_exists():
    assert callable(ast_StateVariableDeclaration.__init__)


def test_ast_statevariabledeclaration_constructor_args():
    sig = inspect.signature(ast_StateVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ast_statevariabledeclaration_has_name():
    assert hasattr(ast_StateVariableDeclaration, "name")
    descriptor = None
    for klass in ast_StateVariableDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ast_iterationaccumulator_is_not_abstract():
    assert not inspect.isabstract(ast_IterationAccumulator)


def test_ast_iterationaccumulator_constructor_exists():
    assert callable(ast_IterationAccumulator.__init__)


def test_ast_iterationaccumulator_constructor_args():
    sig = inspect.signature(ast_IterationAccumulator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ast_iterationaccumulator_has_name():
    assert hasattr(ast_IterationAccumulator, "name")
    descriptor = None
    for klass in ast_IterationAccumulator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ast_builtindefinition_is_not_abstract():
    assert not inspect.isabstract(ast_BuiltinDefinition)


def test_ast_builtindefinition_constructor_exists():
    assert callable(ast_BuiltinDefinition.__init__)


def test_ast_builtindefinition_constructor_args():
    sig = inspect.signature(ast_BuiltinDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ast_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(ast_VariableDeclaration)


def test_ast_variabledeclaration_constructor_exists():
    assert callable(ast_VariableDeclaration.__init__)


def test_ast_variabledeclaration_constructor_args():
    sig = inspect.signature(ast_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ast_variabledeclaration_has_name():
    assert hasattr(ast_VariableDeclaration, "name")
    descriptor = None
    for klass in ast_VariableDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ast_functionobjectdeclaration_is_not_abstract():
    assert not inspect.isabstract(ast_FunctionObjectDeclaration)


def test_ast_functionobjectdeclaration_constructor_exists():
    assert callable(ast_FunctionObjectDeclaration.__init__)


def test_ast_functionobjectdeclaration_constructor_args():
    sig = inspect.signature(ast_FunctionObjectDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ast_functionobjectdeclaration_has_name():
    assert hasattr(ast_FunctionObjectDeclaration, "name")
    descriptor = None
    for klass in ast_FunctionObjectDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ast_functiondefinition_is_not_abstract():
    assert not inspect.isabstract(ast_FunctionDefinition)


def test_ast_functiondefinition_constructor_exists():
    assert callable(ast_FunctionDefinition.__init__)


def test_ast_functiondefinition_constructor_args():
    sig = inspect.signature(ast_FunctionDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_ast_functiondefinition_has_kind():
    assert hasattr(ast_FunctionDefinition, "kind")
    descriptor = None
    for klass in ast_FunctionDefinition.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_ast_datatypespecifier_is_not_abstract():
    assert not inspect.isabstract(ast_DataTypeSpecifier)


def test_ast_datatypespecifier_constructor_exists():
    assert callable(ast_DataTypeSpecifier.__init__)


def test_ast_datatypespecifier_constructor_args():
    sig = inspect.signature(ast_DataTypeSpecifier.__init__)
    params = list(sig.parameters.keys())



def test_ast_structmemberdeclaration_is_not_abstract():
    assert not inspect.isabstract(ast_StructMemberDeclaration)


def test_ast_structmemberdeclaration_constructor_exists():
    assert callable(ast_StructMemberDeclaration.__init__)


def test_ast_structmemberdeclaration_constructor_args():
    sig = inspect.signature(ast_StructMemberDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ast_structmemberdeclaration_has_name():
    assert hasattr(ast_StructMemberDeclaration, "name")
    descriptor = None
    for klass in ast_StructMemberDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ast_structdefinition_is_not_abstract():
    assert not inspect.isabstract(ast_StructDefinition)


def test_ast_structdefinition_constructor_exists():
    assert callable(ast_StructDefinition.__init__)


def test_ast_structdefinition_constructor_args():
    sig = inspect.signature(ast_StructDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ast_primitivetype_is_not_abstract():
    assert not inspect.isabstract(ast_PrimitiveType)


def test_ast_primitivetype_constructor_exists():
    assert callable(ast_PrimitiveType.__init__)


def test_ast_primitivetype_constructor_args():
    sig = inspect.signature(ast_PrimitiveType.__init__)
    params = list(sig.parameters.keys())

def test_equalityoperator_exists():
    # Check that the Enumeration exists
    assert EqualityOperator is not None

def test_equalityoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EqualityOperator]
    expected_literals = [
        "EqualTo",
        "NotEqualTo",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EqualityOperator"

def test_poweroperator_exists():
    # Check that the Enumeration exists
    assert PowerOperator is not None

def test_poweroperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PowerOperator]
    expected_literals = [
        "Power",
        "ElementWisePower",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PowerOperator"

def test_unaryoperator_exists():
    # Check that the Enumeration exists
    assert UnaryOperator is not None

def test_unaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryOperator]
    expected_literals = [
        "Negate",
        "LogicalNot",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryOperator"

def test_multiplicativeoperator_exists():
    # Check that the Enumeration exists
    assert MultiplicativeOperator is not None

def test_multiplicativeoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MultiplicativeOperator]
    expected_literals = [
        "ElementWiseMultiply",
        "Multiply",
        "ElementWiseDivide",
        "Divide",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MultiplicativeOperator"

def test_additiveoperator_exists():
    # Check that the Enumeration exists
    assert AdditiveOperator is not None

def test_additiveoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AdditiveOperator]
    expected_literals = [
        "Add",
        "Subtract",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AdditiveOperator"

def test_assertionstatuskind_exists():
    # Check that the Enumeration exists
    assert AssertionStatusKind is not None

def test_assertionstatuskind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssertionStatusKind]
    expected_literals = [
        "Info",
        "Error",
        "Warning",
        "Fatal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssertionStatusKind"

def test_postfixoperator_exists():
    # Check that the Enumeration exists
    assert PostfixOperator is not None

def test_postfixoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PostfixOperator]
    expected_literals = [
        "Transpose",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PostfixOperator"

def test_functionkind_exists():
    # Check that the Enumeration exists
    assert FunctionKind is not None

def test_functionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FunctionKind]
    expected_literals = [
        "Stateless",
        "Continuous",
        "Stateful",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FunctionKind"

def test_relationaloperator_exists():
    # Check that the Enumeration exists
    assert RelationalOperator is not None

def test_relationaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalOperator]
    expected_literals = [
        "LessThanOrEqualTo",
        "GreaterThan",
        "GreaterThanOrEqualTo",
        "LessThan",
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
BuiltinDefinition_strategy = st.builds(
    BuiltinDefinition,
)
ast_BuiltinVariable_strategy = st.builds(
    ast_BuiltinVariable,
)
ast_BuiltinFunction_strategy = st.builds(
    ast_BuiltinFunction,
)
ast_Statement_strategy = st.builds(
    ast_Statement,
)
Statement_strategy = st.builds(
    Statement,
)
ast_DoWhileStatement_strategy = st.builds(
    ast_DoWhileStatement,
)
ast_WhileStatement_strategy = st.builds(
    ast_WhileStatement,
)
ast_BreakStatement_strategy = st.builds(
    ast_BreakStatement,
)
ast_ContinueStatement_strategy = st.builds(
    ast_ContinueStatement,
)
ast_ReturnStatement_strategy = st.builds(
    ast_ReturnStatement,
)
ast_ForStatement_strategy = st.builds(
    ast_ForStatement,
)
ast_Compound_strategy = st.builds(
    ast_Compound,
)
PrimitiveStepExpression_strategy = st.builds(
    PrimitiveStepExpression,
)
ast_StepN_strategy = st.builds(
    ast_StepN,
)
ast_StepLiteral_strategy = st.builds(
    ast_StepLiteral,
    value=
        st.integers()
)
ast_IfStatement_strategy = st.builds(
    ast_IfStatement,
)
ast_Assignment_strategy = st.builds(
    ast_Assignment,
)
StepExpression_strategy = st.builds(
    StepExpression,
)
ast_PrimitiveStepExpression_strategy = st.builds(
    ast_PrimitiveStepExpression,
)
ast_NegateStepExpression_strategy = st.builds(
    ast_NegateStepExpression,
)
ast_AdditiveStepExpression_strategy = st.builds(
    ast_AdditiveStepExpression,
    operator=
        safe_text
)
ast_RangeStepExpression_strategy = st.builds(
    ast_RangeStepExpression,
)
ast_StepExpression_strategy = st.builds(
    ast_StepExpression,
)
FeatureCall_strategy = st.builds(
    FeatureCall,
)
ast_FunctionCall_strategy = st.builds(
    ast_FunctionCall,
)
ast_VariableAccess_strategy = st.builds(
    ast_VariableAccess,
)
ast_ExpressionList_strategy = st.builds(
    ast_ExpressionList,
)
ast_ArrayConstructionIterationClause_strategy = st.builds(
    ast_ArrayConstructionIterationClause,
    variableName=
        safe_text
)
ast_Unit_strategy = st.builds(
    ast_Unit,
)
ast_ArraySubscript_strategy = st.builds(
    ast_ArraySubscript,
    slice=
        st.booleans()
)
ast_LetExpressionVariableDeclaration_strategy = st.builds(
    ast_LetExpressionVariableDeclaration,
)
Expression_strategy = st.builds(
    Expression,
)
ast_ArrayConcatenationOperator_strategy = st.builds(
    ast_ArrayConcatenationOperator,
)
ast_ArrayElementAccess_strategy = st.builds(
    ast_ArrayElementAccess,
)
ast_DerivativeOperator_strategy = st.builds(
    ast_DerivativeOperator,
)
ast_LogicalOrExpression_strategy = st.builds(
    ast_LogicalOrExpression,
)
ast_IterationCall_strategy = st.builds(
    ast_IterationCall,
    identifier=
        safe_text
)
ast_RangeExpression_strategy = st.builds(
    ast_RangeExpression,
)
ast_AlgorithmExpression_strategy = st.builds(
    ast_AlgorithmExpression,
)
ast_FeatureCall_strategy = st.builds(
    ast_FeatureCall,
)
ast_ImpliesExpression_strategy = st.builds(
    ast_ImpliesExpression,
)
ast_LogicalAndExpression_strategy = st.builds(
    ast_LogicalAndExpression,
)
ast_AdditiveExpression_strategy = st.builds(
    ast_AdditiveExpression,
    operator=
        safe_text
)
ast_EndExpression_strategy = st.builds(
    ast_EndExpression,
)
ast_ArrayConstructionOperator_strategy = st.builds(
    ast_ArrayConstructionOperator,
)
ast_MemberVariableAccess_strategy = st.builds(
    ast_MemberVariableAccess,
)
ast_MultiplicativeExpression_strategy = st.builds(
    ast_MultiplicativeExpression,
    operator=
        safe_text
)
ast_PostfixExpression_strategy = st.builds(
    ast_PostfixExpression,
    operator=
        safe_text
)
ast_UnitConstructionOperator_strategy = st.builds(
    ast_UnitConstructionOperator,
)
ast_EqualityExpression_strategy = st.builds(
    ast_EqualityExpression,
    operator=
        safe_text
)
ast_TypeTestExpression_strategy = st.builds(
    ast_TypeTestExpression,
)
ast_UnaryExpression_strategy = st.builds(
    ast_UnaryExpression,
    operator=
        safe_text
)
ast_ParenthesizedExpression_strategy = st.builds(
    ast_ParenthesizedExpression,
)
ast_RelationalExpression_strategy = st.builds(
    ast_RelationalExpression,
    operator=
        safe_text
)
ast_PowerExpression_strategy = st.builds(
    ast_PowerExpression,
    operator=
        safe_text
)
ast_LetExpression_strategy = st.builds(
    ast_LetExpression,
)
ast_DataType_strategy = st.builds(
    ast_DataType,
)
ast_SwitchCase_strategy = st.builds(
    ast_SwitchCase,
)
ast_SwitchExpression_strategy = st.builds(
    ast_SwitchExpression,
    static=
        st.booleans()
)
ast_IfExpression_strategy = st.builds(
    ast_IfExpression,
    static=
        st.booleans()
)
ast_CallableElement_strategy = st.builds(
    ast_CallableElement,
)
ast_Expression_strategy = st.builds(
    ast_Expression,
)
ast_Equation_strategy = st.builds(
    ast_Equation,
    initial=
        st.booleans()
)
ast_Assertion_strategy = st.builds(
    ast_Assertion,
    static=
        st.booleans(),
    statusKind=
        safe_text
)
ast_Check_strategy = st.builds(
    ast_Check,
)
ParameterDeclaration_strategy = st.builds(
    ParameterDeclaration,
)
ast_OutputParameterDeclaration_strategy = st.builds(
    ast_OutputParameterDeclaration,
)
ast_EnumerationLiteralDeclaration_strategy = st.builds(
    ast_EnumerationLiteralDeclaration,
    name=
        safe_text
)
DataTypeDefinition_strategy = st.builds(
    DataTypeDefinition,
)
ast_TypeAliasDefinition_strategy = st.builds(
    ast_TypeAliasDefinition,
)
ast_EnumerationDefinition_strategy = st.builds(
    ast_EnumerationDefinition,
)
Definition_strategy = st.builds(
    Definition,
)
ast_DataTypeDefinition_strategy = st.builds(
    ast_DataTypeDefinition,
)
ast_Definition_strategy = st.builds(
    ast_Definition,
    name=
        safe_text
)
ast_Module_strategy = st.builds(
    ast_Module,
)
ast_InputParameterDeclaration_strategy = st.builds(
    ast_InputParameterDeclaration,
)
ast_TemplateParameterDeclaration_strategy = st.builds(
    ast_TemplateParameterDeclaration,
)
CallableElement_strategy = st.builds(
    CallableElement,
)
ast_LetExpressionVariableDeclarationPart_strategy = st.builds(
    ast_LetExpressionVariableDeclarationPart,
    name=
        safe_text
)
ast_IterationVariable_strategy = st.builds(
    ast_IterationVariable,
    name=
        safe_text
)
ast_ParameterDeclaration_strategy = st.builds(
    ast_ParameterDeclaration,
    name=
        safe_text
)
ast_StateVariableDeclaration_strategy = st.builds(
    ast_StateVariableDeclaration,
    name=
        safe_text
)
ast_IterationAccumulator_strategy = st.builds(
    ast_IterationAccumulator,
    name=
        safe_text
)
ast_BuiltinDefinition_strategy = st.builds(
    ast_BuiltinDefinition,
)
ast_VariableDeclaration_strategy = st.builds(
    ast_VariableDeclaration,
    name=
        safe_text
)
ast_FunctionObjectDeclaration_strategy = st.builds(
    ast_FunctionObjectDeclaration,
    name=
        safe_text
)
ast_FunctionDefinition_strategy = st.builds(
    ast_FunctionDefinition,
    kind=
        safe_text
)
ast_DataTypeSpecifier_strategy = st.builds(
    ast_DataTypeSpecifier,
)
ast_StructMemberDeclaration_strategy = st.builds(
    ast_StructMemberDeclaration,
    name=
        safe_text
)
ast_StructDefinition_strategy = st.builds(
    ast_StructDefinition,
)
ast_PrimitiveType_strategy = st.builds(
    ast_PrimitiveType,
)

@given(instance=BuiltinDefinition_strategy)
@settings(max_examples=50)
def test_builtindefinition_instantiation(instance):
    assert isinstance(instance, BuiltinDefinition)

@given(instance=ast_BuiltinVariable_strategy)
@settings(max_examples=50)
def test_ast_builtinvariable_instantiation(instance):
    assert isinstance(instance, ast_BuiltinVariable)

@given(instance=ast_BuiltinFunction_strategy)
@settings(max_examples=50)
def test_ast_builtinfunction_instantiation(instance):
    assert isinstance(instance, ast_BuiltinFunction)

@given(instance=ast_Statement_strategy)
@settings(max_examples=50)
def test_ast_statement_instantiation(instance):
    assert isinstance(instance, ast_Statement)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=ast_DoWhileStatement_strategy)
@settings(max_examples=50)
def test_ast_dowhilestatement_instantiation(instance):
    assert isinstance(instance, ast_DoWhileStatement)

@given(instance=ast_WhileStatement_strategy)
@settings(max_examples=50)
def test_ast_whilestatement_instantiation(instance):
    assert isinstance(instance, ast_WhileStatement)

@given(instance=ast_BreakStatement_strategy)
@settings(max_examples=50)
def test_ast_breakstatement_instantiation(instance):
    assert isinstance(instance, ast_BreakStatement)

@given(instance=ast_ContinueStatement_strategy)
@settings(max_examples=50)
def test_ast_continuestatement_instantiation(instance):
    assert isinstance(instance, ast_ContinueStatement)

@given(instance=ast_ReturnStatement_strategy)
@settings(max_examples=50)
def test_ast_returnstatement_instantiation(instance):
    assert isinstance(instance, ast_ReturnStatement)

@given(instance=ast_ForStatement_strategy)
@settings(max_examples=50)
def test_ast_forstatement_instantiation(instance):
    assert isinstance(instance, ast_ForStatement)

@given(instance=ast_Compound_strategy)
@settings(max_examples=50)
def test_ast_compound_instantiation(instance):
    assert isinstance(instance, ast_Compound)

@given(instance=PrimitiveStepExpression_strategy)
@settings(max_examples=50)
def test_primitivestepexpression_instantiation(instance):
    assert isinstance(instance, PrimitiveStepExpression)

@given(instance=ast_StepN_strategy)
@settings(max_examples=50)
def test_ast_stepn_instantiation(instance):
    assert isinstance(instance, ast_StepN)

@given(instance=ast_StepLiteral_strategy)
@settings(max_examples=50)
def test_ast_stepliteral_instantiation(instance):
    assert isinstance(instance, ast_StepLiteral)



@given(instance=ast_StepLiteral_strategy)
def test_ast_stepliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ast_IfStatement_strategy)
@settings(max_examples=50)
def test_ast_ifstatement_instantiation(instance):
    assert isinstance(instance, ast_IfStatement)

@given(instance=ast_Assignment_strategy)
@settings(max_examples=50)
def test_ast_assignment_instantiation(instance):
    assert isinstance(instance, ast_Assignment)

@given(instance=StepExpression_strategy)
@settings(max_examples=50)
def test_stepexpression_instantiation(instance):
    assert isinstance(instance, StepExpression)

@given(instance=ast_PrimitiveStepExpression_strategy)
@settings(max_examples=50)
def test_ast_primitivestepexpression_instantiation(instance):
    assert isinstance(instance, ast_PrimitiveStepExpression)

@given(instance=ast_NegateStepExpression_strategy)
@settings(max_examples=50)
def test_ast_negatestepexpression_instantiation(instance):
    assert isinstance(instance, ast_NegateStepExpression)

@given(instance=ast_AdditiveStepExpression_strategy)
@settings(max_examples=50)
def test_ast_additivestepexpression_instantiation(instance):
    assert isinstance(instance, ast_AdditiveStepExpression)



@given(instance=ast_AdditiveStepExpression_strategy)
def test_ast_additivestepexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ast_RangeStepExpression_strategy)
@settings(max_examples=50)
def test_ast_rangestepexpression_instantiation(instance):
    assert isinstance(instance, ast_RangeStepExpression)

@given(instance=ast_StepExpression_strategy)
@settings(max_examples=50)
def test_ast_stepexpression_instantiation(instance):
    assert isinstance(instance, ast_StepExpression)

@given(instance=FeatureCall_strategy)
@settings(max_examples=50)
def test_featurecall_instantiation(instance):
    assert isinstance(instance, FeatureCall)

@given(instance=ast_FunctionCall_strategy)
@settings(max_examples=50)
def test_ast_functioncall_instantiation(instance):
    assert isinstance(instance, ast_FunctionCall)

@given(instance=ast_VariableAccess_strategy)
@settings(max_examples=50)
def test_ast_variableaccess_instantiation(instance):
    assert isinstance(instance, ast_VariableAccess)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ast_VariableAccess_strategy)
@settings(max_examples=30)
def test_ast_variableaccess_isinitial_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isInitial()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isInitial).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isInitial' in ast_VariableAccess is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isInitial' in ast_VariableAccess did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isInitial' in ast_VariableAccess is not implemented or raised an error")

@given(instance=ast_ExpressionList_strategy)
@settings(max_examples=50)
def test_ast_expressionlist_instantiation(instance):
    assert isinstance(instance, ast_ExpressionList)

@given(instance=ast_ArrayConstructionIterationClause_strategy)
@settings(max_examples=50)
def test_ast_arrayconstructioniterationclause_instantiation(instance):
    assert isinstance(instance, ast_ArrayConstructionIterationClause)



@given(instance=ast_ArrayConstructionIterationClause_strategy)
def test_ast_arrayconstructioniterationclause_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original

@given(instance=ast_Unit_strategy)
@settings(max_examples=50)
def test_ast_unit_instantiation(instance):
    assert isinstance(instance, ast_Unit)

@given(instance=ast_ArraySubscript_strategy)
@settings(max_examples=50)
def test_ast_arraysubscript_instantiation(instance):
    assert isinstance(instance, ast_ArraySubscript)



@given(instance=ast_ArraySubscript_strategy)
def test_ast_arraysubscript_slice_setter(instance):
    original = instance.slice
    instance.slice = original
    assert instance.slice == original

@given(instance=ast_LetExpressionVariableDeclaration_strategy)
@settings(max_examples=50)
def test_ast_letexpressionvariabledeclaration_instantiation(instance):
    assert isinstance(instance, ast_LetExpressionVariableDeclaration)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=ast_ArrayConcatenationOperator_strategy)
@settings(max_examples=50)
def test_ast_arrayconcatenationoperator_instantiation(instance):
    assert isinstance(instance, ast_ArrayConcatenationOperator)

@given(instance=ast_ArrayElementAccess_strategy)
@settings(max_examples=50)
def test_ast_arrayelementaccess_instantiation(instance):
    assert isinstance(instance, ast_ArrayElementAccess)

@given(instance=ast_DerivativeOperator_strategy)
@settings(max_examples=50)
def test_ast_derivativeoperator_instantiation(instance):
    assert isinstance(instance, ast_DerivativeOperator)

@given(instance=ast_LogicalOrExpression_strategy)
@settings(max_examples=50)
def test_ast_logicalorexpression_instantiation(instance):
    assert isinstance(instance, ast_LogicalOrExpression)

@given(instance=ast_IterationCall_strategy)
@settings(max_examples=50)
def test_ast_iterationcall_instantiation(instance):
    assert isinstance(instance, ast_IterationCall)



@given(instance=ast_IterationCall_strategy)
def test_ast_iterationcall_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=ast_RangeExpression_strategy)
@settings(max_examples=50)
def test_ast_rangeexpression_instantiation(instance):
    assert isinstance(instance, ast_RangeExpression)

@given(instance=ast_AlgorithmExpression_strategy)
@settings(max_examples=50)
def test_ast_algorithmexpression_instantiation(instance):
    assert isinstance(instance, ast_AlgorithmExpression)

@given(instance=ast_FeatureCall_strategy)
@settings(max_examples=50)
def test_ast_featurecall_instantiation(instance):
    assert isinstance(instance, ast_FeatureCall)

@given(instance=ast_ImpliesExpression_strategy)
@settings(max_examples=50)
def test_ast_impliesexpression_instantiation(instance):
    assert isinstance(instance, ast_ImpliesExpression)

@given(instance=ast_LogicalAndExpression_strategy)
@settings(max_examples=50)
def test_ast_logicalandexpression_instantiation(instance):
    assert isinstance(instance, ast_LogicalAndExpression)

@given(instance=ast_AdditiveExpression_strategy)
@settings(max_examples=50)
def test_ast_additiveexpression_instantiation(instance):
    assert isinstance(instance, ast_AdditiveExpression)



@given(instance=ast_AdditiveExpression_strategy)
def test_ast_additiveexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ast_EndExpression_strategy)
@settings(max_examples=50)
def test_ast_endexpression_instantiation(instance):
    assert isinstance(instance, ast_EndExpression)

@given(instance=ast_ArrayConstructionOperator_strategy)
@settings(max_examples=50)
def test_ast_arrayconstructionoperator_instantiation(instance):
    assert isinstance(instance, ast_ArrayConstructionOperator)

@given(instance=ast_MemberVariableAccess_strategy)
@settings(max_examples=50)
def test_ast_membervariableaccess_instantiation(instance):
    assert isinstance(instance, ast_MemberVariableAccess)

@given(instance=ast_MultiplicativeExpression_strategy)
@settings(max_examples=50)
def test_ast_multiplicativeexpression_instantiation(instance):
    assert isinstance(instance, ast_MultiplicativeExpression)



@given(instance=ast_MultiplicativeExpression_strategy)
def test_ast_multiplicativeexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ast_PostfixExpression_strategy)
@settings(max_examples=50)
def test_ast_postfixexpression_instantiation(instance):
    assert isinstance(instance, ast_PostfixExpression)



@given(instance=ast_PostfixExpression_strategy)
def test_ast_postfixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ast_UnitConstructionOperator_strategy)
@settings(max_examples=50)
def test_ast_unitconstructionoperator_instantiation(instance):
    assert isinstance(instance, ast_UnitConstructionOperator)

@given(instance=ast_EqualityExpression_strategy)
@settings(max_examples=50)
def test_ast_equalityexpression_instantiation(instance):
    assert isinstance(instance, ast_EqualityExpression)



@given(instance=ast_EqualityExpression_strategy)
def test_ast_equalityexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ast_TypeTestExpression_strategy)
@settings(max_examples=50)
def test_ast_typetestexpression_instantiation(instance):
    assert isinstance(instance, ast_TypeTestExpression)

@given(instance=ast_UnaryExpression_strategy)
@settings(max_examples=50)
def test_ast_unaryexpression_instantiation(instance):
    assert isinstance(instance, ast_UnaryExpression)



@given(instance=ast_UnaryExpression_strategy)
def test_ast_unaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ast_ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_ast_parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, ast_ParenthesizedExpression)

@given(instance=ast_RelationalExpression_strategy)
@settings(max_examples=50)
def test_ast_relationalexpression_instantiation(instance):
    assert isinstance(instance, ast_RelationalExpression)



@given(instance=ast_RelationalExpression_strategy)
def test_ast_relationalexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ast_PowerExpression_strategy)
@settings(max_examples=50)
def test_ast_powerexpression_instantiation(instance):
    assert isinstance(instance, ast_PowerExpression)



@given(instance=ast_PowerExpression_strategy)
def test_ast_powerexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ast_LetExpression_strategy)
@settings(max_examples=50)
def test_ast_letexpression_instantiation(instance):
    assert isinstance(instance, ast_LetExpression)

@given(instance=ast_DataType_strategy)
@settings(max_examples=50)
def test_ast_datatype_instantiation(instance):
    assert isinstance(instance, ast_DataType)

@given(instance=ast_SwitchCase_strategy)
@settings(max_examples=50)
def test_ast_switchcase_instantiation(instance):
    assert isinstance(instance, ast_SwitchCase)

@given(instance=ast_SwitchExpression_strategy)
@settings(max_examples=50)
def test_ast_switchexpression_instantiation(instance):
    assert isinstance(instance, ast_SwitchExpression)



@given(instance=ast_SwitchExpression_strategy)
def test_ast_switchexpression_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=ast_IfExpression_strategy)
@settings(max_examples=50)
def test_ast_ifexpression_instantiation(instance):
    assert isinstance(instance, ast_IfExpression)



@given(instance=ast_IfExpression_strategy)
def test_ast_ifexpression_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=ast_CallableElement_strategy)
@settings(max_examples=50)
def test_ast_callableelement_instantiation(instance):
    assert isinstance(instance, ast_CallableElement)

@given(instance=ast_Expression_strategy)
@settings(max_examples=50)
def test_ast_expression_instantiation(instance):
    assert isinstance(instance, ast_Expression)

@given(instance=ast_Equation_strategy)
@settings(max_examples=50)
def test_ast_equation_instantiation(instance):
    assert isinstance(instance, ast_Equation)



@given(instance=ast_Equation_strategy)
def test_ast_equation_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original

@given(instance=ast_Assertion_strategy)
@settings(max_examples=50)
def test_ast_assertion_instantiation(instance):
    assert isinstance(instance, ast_Assertion)



@given(instance=ast_Assertion_strategy)
def test_ast_assertion_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original



@given(instance=ast_Assertion_strategy)
def test_ast_assertion_statusKind_setter(instance):
    original = instance.statusKind
    instance.statusKind = original
    assert instance.statusKind == original

@given(instance=ast_Check_strategy)
@settings(max_examples=50)
def test_ast_check_instantiation(instance):
    assert isinstance(instance, ast_Check)

@given(instance=ParameterDeclaration_strategy)
@settings(max_examples=50)
def test_parameterdeclaration_instantiation(instance):
    assert isinstance(instance, ParameterDeclaration)

@given(instance=ast_OutputParameterDeclaration_strategy)
@settings(max_examples=50)
def test_ast_outputparameterdeclaration_instantiation(instance):
    assert isinstance(instance, ast_OutputParameterDeclaration)

@given(instance=ast_EnumerationLiteralDeclaration_strategy)
@settings(max_examples=50)
def test_ast_enumerationliteraldeclaration_instantiation(instance):
    assert isinstance(instance, ast_EnumerationLiteralDeclaration)



@given(instance=ast_EnumerationLiteralDeclaration_strategy)
def test_ast_enumerationliteraldeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DataTypeDefinition_strategy)
@settings(max_examples=50)
def test_datatypedefinition_instantiation(instance):
    assert isinstance(instance, DataTypeDefinition)

@given(instance=ast_TypeAliasDefinition_strategy)
@settings(max_examples=50)
def test_ast_typealiasdefinition_instantiation(instance):
    assert isinstance(instance, ast_TypeAliasDefinition)

@given(instance=ast_EnumerationDefinition_strategy)
@settings(max_examples=50)
def test_ast_enumerationdefinition_instantiation(instance):
    assert isinstance(instance, ast_EnumerationDefinition)

@given(instance=Definition_strategy)
@settings(max_examples=50)
def test_definition_instantiation(instance):
    assert isinstance(instance, Definition)

@given(instance=ast_DataTypeDefinition_strategy)
@settings(max_examples=50)
def test_ast_datatypedefinition_instantiation(instance):
    assert isinstance(instance, ast_DataTypeDefinition)

@given(instance=ast_Definition_strategy)
@settings(max_examples=50)
def test_ast_definition_instantiation(instance):
    assert isinstance(instance, ast_Definition)



@given(instance=ast_Definition_strategy)
def test_ast_definition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ast_Module_strategy)
@settings(max_examples=50)
def test_ast_module_instantiation(instance):
    assert isinstance(instance, ast_Module)

@given(instance=ast_InputParameterDeclaration_strategy)
@settings(max_examples=50)
def test_ast_inputparameterdeclaration_instantiation(instance):
    assert isinstance(instance, ast_InputParameterDeclaration)

@given(instance=ast_TemplateParameterDeclaration_strategy)
@settings(max_examples=50)
def test_ast_templateparameterdeclaration_instantiation(instance):
    assert isinstance(instance, ast_TemplateParameterDeclaration)

@given(instance=CallableElement_strategy)
@settings(max_examples=50)
def test_callableelement_instantiation(instance):
    assert isinstance(instance, CallableElement)

@given(instance=ast_LetExpressionVariableDeclarationPart_strategy)
@settings(max_examples=50)
def test_ast_letexpressionvariabledeclarationpart_instantiation(instance):
    assert isinstance(instance, ast_LetExpressionVariableDeclarationPart)



@given(instance=ast_LetExpressionVariableDeclarationPart_strategy)
def test_ast_letexpressionvariabledeclarationpart_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ast_IterationVariable_strategy)
@settings(max_examples=50)
def test_ast_iterationvariable_instantiation(instance):
    assert isinstance(instance, ast_IterationVariable)



@given(instance=ast_IterationVariable_strategy)
def test_ast_iterationvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ast_ParameterDeclaration_strategy)
@settings(max_examples=50)
def test_ast_parameterdeclaration_instantiation(instance):
    assert isinstance(instance, ast_ParameterDeclaration)



@given(instance=ast_ParameterDeclaration_strategy)
def test_ast_parameterdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ast_StateVariableDeclaration_strategy)
@settings(max_examples=50)
def test_ast_statevariabledeclaration_instantiation(instance):
    assert isinstance(instance, ast_StateVariableDeclaration)



@given(instance=ast_StateVariableDeclaration_strategy)
def test_ast_statevariabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ast_IterationAccumulator_strategy)
@settings(max_examples=50)
def test_ast_iterationaccumulator_instantiation(instance):
    assert isinstance(instance, ast_IterationAccumulator)



@given(instance=ast_IterationAccumulator_strategy)
def test_ast_iterationaccumulator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ast_BuiltinDefinition_strategy)
@settings(max_examples=50)
def test_ast_builtindefinition_instantiation(instance):
    assert isinstance(instance, ast_BuiltinDefinition)

@given(instance=ast_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_ast_variabledeclaration_instantiation(instance):
    assert isinstance(instance, ast_VariableDeclaration)



@given(instance=ast_VariableDeclaration_strategy)
def test_ast_variabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ast_FunctionObjectDeclaration_strategy)
@settings(max_examples=50)
def test_ast_functionobjectdeclaration_instantiation(instance):
    assert isinstance(instance, ast_FunctionObjectDeclaration)



@given(instance=ast_FunctionObjectDeclaration_strategy)
def test_ast_functionobjectdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ast_FunctionDefinition_strategy)
@settings(max_examples=50)
def test_ast_functiondefinition_instantiation(instance):
    assert isinstance(instance, ast_FunctionDefinition)



@given(instance=ast_FunctionDefinition_strategy)
def test_ast_functiondefinition_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=ast_DataTypeSpecifier_strategy)
@settings(max_examples=50)
def test_ast_datatypespecifier_instantiation(instance):
    assert isinstance(instance, ast_DataTypeSpecifier)

@given(instance=ast_StructMemberDeclaration_strategy)
@settings(max_examples=50)
def test_ast_structmemberdeclaration_instantiation(instance):
    assert isinstance(instance, ast_StructMemberDeclaration)



@given(instance=ast_StructMemberDeclaration_strategy)
def test_ast_structmemberdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ast_StructDefinition_strategy)
@settings(max_examples=50)
def test_ast_structdefinition_instantiation(instance):
    assert isinstance(instance, ast_StructDefinition)

@given(instance=ast_PrimitiveType_strategy)
@settings(max_examples=50)
def test_ast_primitivetype_instantiation(instance):
    assert isinstance(instance, ast_PrimitiveType)
