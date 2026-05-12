import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Type,
    xs_StringType,
    xs_BoolType,
    xs_FloatType,
    xs_VectorType,
    xs_VoidType,
    xs_IntType,
    Literal,
    xs_LiteralFloat,
    xs_LiteralBool,
    xs_VectorLiteral,
    xs_LiteralInt,
    xs_LiteralString,
    Expression,
    xs_Call,
    xs_Assign,
    xs_OrExpression,
    xs_Term,
    xs_Literal,
    xs_EqualsExpression,
    xs_AndExpression,
    xs_Factor,
    xs_ComparisonExpression,
    xs_Var,
    xs_SwitchDefault,
    xs_SwitchCase,
    xs_Statement,
    xs_Type,
    Statement,
    xs_SwitchStatement,
    xs_ReturnStatement,
    xs_ForStatement,
    xs_ContinueStatement,
    xs_PostfixStatement,
    xs_BreakStatement,
    xs_IfElseStatement,
    xs_WhileStatement,
    VarDeclaration,
    xs_ParameterDeclaration,
    xs_ForVarDeclaration,
    xs_LocalVarDeclaration,
    xs_Expression,
    xs_VarDeclaration,
    Declaration,
    xs_FunctionDeclaration,
    xs_GlobalVarDeclaration,
    xs_IncludeDeclaration,
    xs_Declaration,
    xs_Program,
    xs_RuleDeclaration,
    xs_Block,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_xs_stringtype_is_not_abstract():
    assert not inspect.isabstract(xs_StringType)


def test_xs_stringtype_constructor_exists():
    assert callable(xs_StringType.__init__)


def test_xs_stringtype_constructor_args():
    sig = inspect.signature(xs_StringType.__init__)
    params = list(sig.parameters.keys())



def test_xs_booltype_is_not_abstract():
    assert not inspect.isabstract(xs_BoolType)


def test_xs_booltype_constructor_exists():
    assert callable(xs_BoolType.__init__)


def test_xs_booltype_constructor_args():
    sig = inspect.signature(xs_BoolType.__init__)
    params = list(sig.parameters.keys())



def test_xs_floattype_is_not_abstract():
    assert not inspect.isabstract(xs_FloatType)


def test_xs_floattype_constructor_exists():
    assert callable(xs_FloatType.__init__)


def test_xs_floattype_constructor_args():
    sig = inspect.signature(xs_FloatType.__init__)
    params = list(sig.parameters.keys())



def test_xs_vectortype_is_not_abstract():
    assert not inspect.isabstract(xs_VectorType)


def test_xs_vectortype_constructor_exists():
    assert callable(xs_VectorType.__init__)


def test_xs_vectortype_constructor_args():
    sig = inspect.signature(xs_VectorType.__init__)
    params = list(sig.parameters.keys())



def test_xs_voidtype_is_not_abstract():
    assert not inspect.isabstract(xs_VoidType)


def test_xs_voidtype_constructor_exists():
    assert callable(xs_VoidType.__init__)


def test_xs_voidtype_constructor_args():
    sig = inspect.signature(xs_VoidType.__init__)
    params = list(sig.parameters.keys())



def test_xs_inttype_is_not_abstract():
    assert not inspect.isabstract(xs_IntType)


def test_xs_inttype_constructor_exists():
    assert callable(xs_IntType.__init__)


def test_xs_inttype_constructor_args():
    sig = inspect.signature(xs_IntType.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_xs_literalfloat_is_not_abstract():
    assert not inspect.isabstract(xs_LiteralFloat)


def test_xs_literalfloat_constructor_exists():
    assert callable(xs_LiteralFloat.__init__)


def test_xs_literalfloat_constructor_args():
    sig = inspect.signature(xs_LiteralFloat.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_xs_literalfloat_has_value():
    assert hasattr(xs_LiteralFloat, "value")
    descriptor = None
    for klass in xs_LiteralFloat.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_xs_literalbool_is_not_abstract():
    assert not inspect.isabstract(xs_LiteralBool)


def test_xs_literalbool_constructor_exists():
    assert callable(xs_LiteralBool.__init__)


def test_xs_literalbool_constructor_args():
    sig = inspect.signature(xs_LiteralBool.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_xs_literalbool_has_value():
    assert hasattr(xs_LiteralBool, "value")
    descriptor = None
    for klass in xs_LiteralBool.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_xs_vectorliteral_is_not_abstract():
    assert not inspect.isabstract(xs_VectorLiteral)


def test_xs_vectorliteral_constructor_exists():
    assert callable(xs_VectorLiteral.__init__)


def test_xs_vectorliteral_constructor_args():
    sig = inspect.signature(xs_VectorLiteral.__init__)
    params = list(sig.parameters.keys())



def test_xs_literalint_is_not_abstract():
    assert not inspect.isabstract(xs_LiteralInt)


def test_xs_literalint_constructor_exists():
    assert callable(xs_LiteralInt.__init__)


def test_xs_literalint_constructor_args():
    sig = inspect.signature(xs_LiteralInt.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_xs_literalint_has_value():
    assert hasattr(xs_LiteralInt, "value")
    descriptor = None
    for klass in xs_LiteralInt.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_xs_literalstring_is_not_abstract():
    assert not inspect.isabstract(xs_LiteralString)


def test_xs_literalstring_constructor_exists():
    assert callable(xs_LiteralString.__init__)


def test_xs_literalstring_constructor_args():
    sig = inspect.signature(xs_LiteralString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_xs_literalstring_has_value():
    assert hasattr(xs_LiteralString, "value")
    descriptor = None
    for klass in xs_LiteralString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_xs_call_is_not_abstract():
    assert not inspect.isabstract(xs_Call)


def test_xs_call_constructor_exists():
    assert callable(xs_Call.__init__)


def test_xs_call_constructor_args():
    sig = inspect.signature(xs_Call.__init__)
    params = list(sig.parameters.keys())



def test_xs_assign_is_not_abstract():
    assert not inspect.isabstract(xs_Assign)


def test_xs_assign_constructor_exists():
    assert callable(xs_Assign.__init__)


def test_xs_assign_constructor_args():
    sig = inspect.signature(xs_Assign.__init__)
    params = list(sig.parameters.keys())



def test_xs_orexpression_is_not_abstract():
    assert not inspect.isabstract(xs_OrExpression)


def test_xs_orexpression_constructor_exists():
    assert callable(xs_OrExpression.__init__)


def test_xs_orexpression_constructor_args():
    sig = inspect.signature(xs_OrExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_xs_orexpression_has_op():
    assert hasattr(xs_OrExpression, "op")
    descriptor = None
    for klass in xs_OrExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_xs_term_is_not_abstract():
    assert not inspect.isabstract(xs_Term)


def test_xs_term_constructor_exists():
    assert callable(xs_Term.__init__)


def test_xs_term_constructor_args():
    sig = inspect.signature(xs_Term.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_xs_term_has_op():
    assert hasattr(xs_Term, "op")
    descriptor = None
    for klass in xs_Term.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_xs_literal_is_not_abstract():
    assert not inspect.isabstract(xs_Literal)


def test_xs_literal_constructor_exists():
    assert callable(xs_Literal.__init__)


def test_xs_literal_constructor_args():
    sig = inspect.signature(xs_Literal.__init__)
    params = list(sig.parameters.keys())



def test_xs_equalsexpression_is_not_abstract():
    assert not inspect.isabstract(xs_EqualsExpression)


def test_xs_equalsexpression_constructor_exists():
    assert callable(xs_EqualsExpression.__init__)


def test_xs_equalsexpression_constructor_args():
    sig = inspect.signature(xs_EqualsExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_xs_equalsexpression_has_op():
    assert hasattr(xs_EqualsExpression, "op")
    descriptor = None
    for klass in xs_EqualsExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_xs_andexpression_is_not_abstract():
    assert not inspect.isabstract(xs_AndExpression)


def test_xs_andexpression_constructor_exists():
    assert callable(xs_AndExpression.__init__)


def test_xs_andexpression_constructor_args():
    sig = inspect.signature(xs_AndExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_xs_andexpression_has_op():
    assert hasattr(xs_AndExpression, "op")
    descriptor = None
    for klass in xs_AndExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_xs_factor_is_not_abstract():
    assert not inspect.isabstract(xs_Factor)


def test_xs_factor_constructor_exists():
    assert callable(xs_Factor.__init__)


def test_xs_factor_constructor_args():
    sig = inspect.signature(xs_Factor.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_xs_factor_has_op():
    assert hasattr(xs_Factor, "op")
    descriptor = None
    for klass in xs_Factor.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_xs_comparisonexpression_is_not_abstract():
    assert not inspect.isabstract(xs_ComparisonExpression)


def test_xs_comparisonexpression_constructor_exists():
    assert callable(xs_ComparisonExpression.__init__)


def test_xs_comparisonexpression_constructor_args():
    sig = inspect.signature(xs_ComparisonExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_xs_comparisonexpression_has_op():
    assert hasattr(xs_ComparisonExpression, "op")
    descriptor = None
    for klass in xs_ComparisonExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_xs_var_is_not_abstract():
    assert not inspect.isabstract(xs_Var)


def test_xs_var_constructor_exists():
    assert callable(xs_Var.__init__)


def test_xs_var_constructor_args():
    sig = inspect.signature(xs_Var.__init__)
    params = list(sig.parameters.keys())



def test_xs_switchdefault_is_not_abstract():
    assert not inspect.isabstract(xs_SwitchDefault)


def test_xs_switchdefault_constructor_exists():
    assert callable(xs_SwitchDefault.__init__)


def test_xs_switchdefault_constructor_args():
    sig = inspect.signature(xs_SwitchDefault.__init__)
    params = list(sig.parameters.keys())



def test_xs_switchcase_is_not_abstract():
    assert not inspect.isabstract(xs_SwitchCase)


def test_xs_switchcase_constructor_exists():
    assert callable(xs_SwitchCase.__init__)


def test_xs_switchcase_constructor_args():
    sig = inspect.signature(xs_SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_xs_statement_is_not_abstract():
    assert not inspect.isabstract(xs_Statement)


def test_xs_statement_constructor_exists():
    assert callable(xs_Statement.__init__)


def test_xs_statement_constructor_args():
    sig = inspect.signature(xs_Statement.__init__)
    params = list(sig.parameters.keys())



def test_xs_type_is_not_abstract():
    assert not inspect.isabstract(xs_Type)


def test_xs_type_constructor_exists():
    assert callable(xs_Type.__init__)


def test_xs_type_constructor_args():
    sig = inspect.signature(xs_Type.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_xs_switchstatement_is_not_abstract():
    assert not inspect.isabstract(xs_SwitchStatement)


def test_xs_switchstatement_constructor_exists():
    assert callable(xs_SwitchStatement.__init__)


def test_xs_switchstatement_constructor_args():
    sig = inspect.signature(xs_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_xs_returnstatement_is_not_abstract():
    assert not inspect.isabstract(xs_ReturnStatement)


def test_xs_returnstatement_constructor_exists():
    assert callable(xs_ReturnStatement.__init__)


def test_xs_returnstatement_constructor_args():
    sig = inspect.signature(xs_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_xs_forstatement_is_not_abstract():
    assert not inspect.isabstract(xs_ForStatement)


def test_xs_forstatement_constructor_exists():
    assert callable(xs_ForStatement.__init__)


def test_xs_forstatement_constructor_args():
    sig = inspect.signature(xs_ForStatement.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_xs_forstatement_has_op():
    assert hasattr(xs_ForStatement, "op")
    descriptor = None
    for klass in xs_ForStatement.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_xs_continuestatement_is_not_abstract():
    assert not inspect.isabstract(xs_ContinueStatement)


def test_xs_continuestatement_constructor_exists():
    assert callable(xs_ContinueStatement.__init__)


def test_xs_continuestatement_constructor_args():
    sig = inspect.signature(xs_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_xs_postfixstatement_is_not_abstract():
    assert not inspect.isabstract(xs_PostfixStatement)


def test_xs_postfixstatement_constructor_exists():
    assert callable(xs_PostfixStatement.__init__)


def test_xs_postfixstatement_constructor_args():
    sig = inspect.signature(xs_PostfixStatement.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_xs_postfixstatement_has_op():
    assert hasattr(xs_PostfixStatement, "op")
    descriptor = None
    for klass in xs_PostfixStatement.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_xs_breakstatement_is_not_abstract():
    assert not inspect.isabstract(xs_BreakStatement)


def test_xs_breakstatement_constructor_exists():
    assert callable(xs_BreakStatement.__init__)


def test_xs_breakstatement_constructor_args():
    sig = inspect.signature(xs_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_xs_ifelsestatement_is_not_abstract():
    assert not inspect.isabstract(xs_IfElseStatement)


def test_xs_ifelsestatement_constructor_exists():
    assert callable(xs_IfElseStatement.__init__)


def test_xs_ifelsestatement_constructor_args():
    sig = inspect.signature(xs_IfElseStatement.__init__)
    params = list(sig.parameters.keys())



def test_xs_whilestatement_is_not_abstract():
    assert not inspect.isabstract(xs_WhileStatement)


def test_xs_whilestatement_constructor_exists():
    assert callable(xs_WhileStatement.__init__)


def test_xs_whilestatement_constructor_args():
    sig = inspect.signature(xs_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_vardeclaration_is_not_abstract():
    assert not inspect.isabstract(VarDeclaration)


def test_vardeclaration_constructor_exists():
    assert callable(VarDeclaration.__init__)


def test_vardeclaration_constructor_args():
    sig = inspect.signature(VarDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_xs_parameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(xs_ParameterDeclaration)


def test_xs_parameterdeclaration_constructor_exists():
    assert callable(xs_ParameterDeclaration.__init__)


def test_xs_parameterdeclaration_constructor_args():
    sig = inspect.signature(xs_ParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_xs_forvardeclaration_is_not_abstract():
    assert not inspect.isabstract(xs_ForVarDeclaration)


def test_xs_forvardeclaration_constructor_exists():
    assert callable(xs_ForVarDeclaration.__init__)


def test_xs_forvardeclaration_constructor_args():
    sig = inspect.signature(xs_ForVarDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_xs_localvardeclaration_is_not_abstract():
    assert not inspect.isabstract(xs_LocalVarDeclaration)


def test_xs_localvardeclaration_constructor_exists():
    assert callable(xs_LocalVarDeclaration.__init__)


def test_xs_localvardeclaration_constructor_args():
    sig = inspect.signature(xs_LocalVarDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_xs_expression_is_not_abstract():
    assert not inspect.isabstract(xs_Expression)


def test_xs_expression_constructor_exists():
    assert callable(xs_Expression.__init__)


def test_xs_expression_constructor_args():
    sig = inspect.signature(xs_Expression.__init__)
    params = list(sig.parameters.keys())



def test_xs_vardeclaration_is_not_abstract():
    assert not inspect.isabstract(xs_VarDeclaration)


def test_xs_vardeclaration_constructor_exists():
    assert callable(xs_VarDeclaration.__init__)


def test_xs_vardeclaration_constructor_args():
    sig = inspect.signature(xs_VarDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_xs_vardeclaration_has_name():
    assert hasattr(xs_VarDeclaration, "name")
    descriptor = None
    for klass in xs_VarDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_xs_functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(xs_FunctionDeclaration)


def test_xs_functiondeclaration_constructor_exists():
    assert callable(xs_FunctionDeclaration.__init__)


def test_xs_functiondeclaration_constructor_args():
    sig = inspect.signature(xs_FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "mutable" in params, "Missing parameter 'mutable'"
    assert "name" in params, "Missing parameter 'name'"

def test_xs_functiondeclaration_has_mutable():
    assert hasattr(xs_FunctionDeclaration, "mutable")
    descriptor = None
    for klass in xs_FunctionDeclaration.__mro__:
        if "mutable" in klass.__dict__:
            descriptor = klass.__dict__["mutable"]
            break
    assert isinstance(descriptor, property)

def test_xs_functiondeclaration_has_name():
    assert hasattr(xs_FunctionDeclaration, "name")
    descriptor = None
    for klass in xs_FunctionDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xs_globalvardeclaration_is_not_abstract():
    assert not inspect.isabstract(xs_GlobalVarDeclaration)


def test_xs_globalvardeclaration_constructor_exists():
    assert callable(xs_GlobalVarDeclaration.__init__)


def test_xs_globalvardeclaration_constructor_args():
    sig = inspect.signature(xs_GlobalVarDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "extern" in params, "Missing parameter 'extern'"
    assert "const" in params, "Missing parameter 'const'"

def test_xs_globalvardeclaration_has_extern():
    assert hasattr(xs_GlobalVarDeclaration, "extern")
    descriptor = None
    for klass in xs_GlobalVarDeclaration.__mro__:
        if "extern" in klass.__dict__:
            descriptor = klass.__dict__["extern"]
            break
    assert isinstance(descriptor, property)

def test_xs_globalvardeclaration_has_const():
    assert hasattr(xs_GlobalVarDeclaration, "const")
    descriptor = None
    for klass in xs_GlobalVarDeclaration.__mro__:
        if "const" in klass.__dict__:
            descriptor = klass.__dict__["const"]
            break
    assert isinstance(descriptor, property)



def test_xs_includedeclaration_is_not_abstract():
    assert not inspect.isabstract(xs_IncludeDeclaration)


def test_xs_includedeclaration_constructor_exists():
    assert callable(xs_IncludeDeclaration.__init__)


def test_xs_includedeclaration_constructor_args():
    sig = inspect.signature(xs_IncludeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "filePath" in params, "Missing parameter 'filePath'"

def test_xs_includedeclaration_has_filePath():
    assert hasattr(xs_IncludeDeclaration, "filePath")
    descriptor = None
    for klass in xs_IncludeDeclaration.__mro__:
        if "filePath" in klass.__dict__:
            descriptor = klass.__dict__["filePath"]
            break
    assert isinstance(descriptor, property)



def test_xs_declaration_is_not_abstract():
    assert not inspect.isabstract(xs_Declaration)


def test_xs_declaration_constructor_exists():
    assert callable(xs_Declaration.__init__)


def test_xs_declaration_constructor_args():
    sig = inspect.signature(xs_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_xs_program_is_not_abstract():
    assert not inspect.isabstract(xs_Program)


def test_xs_program_constructor_exists():
    assert callable(xs_Program.__init__)


def test_xs_program_constructor_args():
    sig = inspect.signature(xs_Program.__init__)
    params = list(sig.parameters.keys())



def test_xs_ruledeclaration_is_not_abstract():
    assert not inspect.isabstract(xs_RuleDeclaration)


def test_xs_ruledeclaration_constructor_exists():
    assert callable(xs_RuleDeclaration.__init__)


def test_xs_ruledeclaration_constructor_args():
    sig = inspect.signature(xs_RuleDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "runImmediately" in params, "Missing parameter 'runImmediately'"
    assert "group" in params, "Missing parameter 'group'"
    assert "active" in params, "Missing parameter 'active'"
    assert "highFrequency" in params, "Missing parameter 'highFrequency'"
    assert "maxInterval" in params, "Missing parameter 'maxInterval'"
    assert "minInterval" in params, "Missing parameter 'minInterval'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "name" in params, "Missing parameter 'name'"

def test_xs_ruledeclaration_has_runImmediately():
    assert hasattr(xs_RuleDeclaration, "runImmediately")
    descriptor = None
    for klass in xs_RuleDeclaration.__mro__:
        if "runImmediately" in klass.__dict__:
            descriptor = klass.__dict__["runImmediately"]
            break
    assert isinstance(descriptor, property)

def test_xs_ruledeclaration_has_group():
    assert hasattr(xs_RuleDeclaration, "group")
    descriptor = None
    for klass in xs_RuleDeclaration.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_xs_ruledeclaration_has_active():
    assert hasattr(xs_RuleDeclaration, "active")
    descriptor = None
    for klass in xs_RuleDeclaration.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)

def test_xs_ruledeclaration_has_highFrequency():
    assert hasattr(xs_RuleDeclaration, "highFrequency")
    descriptor = None
    for klass in xs_RuleDeclaration.__mro__:
        if "highFrequency" in klass.__dict__:
            descriptor = klass.__dict__["highFrequency"]
            break
    assert isinstance(descriptor, property)

def test_xs_ruledeclaration_has_maxInterval():
    assert hasattr(xs_RuleDeclaration, "maxInterval")
    descriptor = None
    for klass in xs_RuleDeclaration.__mro__:
        if "maxInterval" in klass.__dict__:
            descriptor = klass.__dict__["maxInterval"]
            break
    assert isinstance(descriptor, property)

def test_xs_ruledeclaration_has_minInterval():
    assert hasattr(xs_RuleDeclaration, "minInterval")
    descriptor = None
    for klass in xs_RuleDeclaration.__mro__:
        if "minInterval" in klass.__dict__:
            descriptor = klass.__dict__["minInterval"]
            break
    assert isinstance(descriptor, property)

def test_xs_ruledeclaration_has_priority():
    assert hasattr(xs_RuleDeclaration, "priority")
    descriptor = None
    for klass in xs_RuleDeclaration.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_xs_ruledeclaration_has_name():
    assert hasattr(xs_RuleDeclaration, "name")
    descriptor = None
    for klass in xs_RuleDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xs_block_is_not_abstract():
    assert not inspect.isabstract(xs_Block)


def test_xs_block_constructor_exists():
    assert callable(xs_Block.__init__)


def test_xs_block_constructor_args():
    sig = inspect.signature(xs_Block.__init__)
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
Type_strategy = st.builds(
    Type,
)
xs_StringType_strategy = st.builds(
    xs_StringType,
)
xs_BoolType_strategy = st.builds(
    xs_BoolType,
)
xs_FloatType_strategy = st.builds(
    xs_FloatType,
)
xs_VectorType_strategy = st.builds(
    xs_VectorType,
)
xs_VoidType_strategy = st.builds(
    xs_VoidType,
)
xs_IntType_strategy = st.builds(
    xs_IntType,
)
Literal_strategy = st.builds(
    Literal,
)
xs_LiteralFloat_strategy = st.builds(
    xs_LiteralFloat,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
xs_LiteralBool_strategy = st.builds(
    xs_LiteralBool,
    value=
        st.booleans()
)
xs_VectorLiteral_strategy = st.builds(
    xs_VectorLiteral,
)
xs_LiteralInt_strategy = st.builds(
    xs_LiteralInt,
    value=
        st.integers()
)
xs_LiteralString_strategy = st.builds(
    xs_LiteralString,
    value=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
xs_Call_strategy = st.builds(
    xs_Call,
)
xs_Assign_strategy = st.builds(
    xs_Assign,
)
xs_OrExpression_strategy = st.builds(
    xs_OrExpression,
    op=
        safe_text
)
xs_Term_strategy = st.builds(
    xs_Term,
    op=
        safe_text
)
xs_Literal_strategy = st.builds(
    xs_Literal,
)
xs_EqualsExpression_strategy = st.builds(
    xs_EqualsExpression,
    op=
        safe_text
)
xs_AndExpression_strategy = st.builds(
    xs_AndExpression,
    op=
        safe_text
)
xs_Factor_strategy = st.builds(
    xs_Factor,
    op=
        safe_text
)
xs_ComparisonExpression_strategy = st.builds(
    xs_ComparisonExpression,
    op=
        safe_text
)
xs_Var_strategy = st.builds(
    xs_Var,
)
xs_SwitchDefault_strategy = st.builds(
    xs_SwitchDefault,
)
xs_SwitchCase_strategy = st.builds(
    xs_SwitchCase,
)
xs_Statement_strategy = st.builds(
    xs_Statement,
)
xs_Type_strategy = st.builds(
    xs_Type,
)
Statement_strategy = st.builds(
    Statement,
)
xs_SwitchStatement_strategy = st.builds(
    xs_SwitchStatement,
)
xs_ReturnStatement_strategy = st.builds(
    xs_ReturnStatement,
)
xs_ForStatement_strategy = st.builds(
    xs_ForStatement,
    op=
        safe_text
)
xs_ContinueStatement_strategy = st.builds(
    xs_ContinueStatement,
)
xs_PostfixStatement_strategy = st.builds(
    xs_PostfixStatement,
    op=
        safe_text
)
xs_BreakStatement_strategy = st.builds(
    xs_BreakStatement,
)
xs_IfElseStatement_strategy = st.builds(
    xs_IfElseStatement,
)
xs_WhileStatement_strategy = st.builds(
    xs_WhileStatement,
)
VarDeclaration_strategy = st.builds(
    VarDeclaration,
)
xs_ParameterDeclaration_strategy = st.builds(
    xs_ParameterDeclaration,
)
xs_ForVarDeclaration_strategy = st.builds(
    xs_ForVarDeclaration,
)
xs_LocalVarDeclaration_strategy = st.builds(
    xs_LocalVarDeclaration,
)
xs_Expression_strategy = st.builds(
    xs_Expression,
)
xs_VarDeclaration_strategy = st.builds(
    xs_VarDeclaration,
    name=
        safe_text
)
Declaration_strategy = st.builds(
    Declaration,
)
xs_FunctionDeclaration_strategy = st.builds(
    xs_FunctionDeclaration,
    mutable=
        st.booleans(),
    name=
        safe_text
)
xs_GlobalVarDeclaration_strategy = st.builds(
    xs_GlobalVarDeclaration,
    extern=
        st.booleans(),
    const=
        st.booleans()
)
xs_IncludeDeclaration_strategy = st.builds(
    xs_IncludeDeclaration,
    filePath=
        safe_text
)
xs_Declaration_strategy = st.builds(
    xs_Declaration,
)
xs_Program_strategy = st.builds(
    xs_Program,
)
xs_RuleDeclaration_strategy = st.builds(
    xs_RuleDeclaration,
    runImmediately=
        st.booleans(),
    group=
        safe_text,
    active=
        st.booleans(),
    highFrequency=
        st.booleans(),
    maxInterval=
        st.integers(),
    minInterval=
        st.integers(),
    priority=
        st.integers(),
    name=
        safe_text
)
xs_Block_strategy = st.builds(
    xs_Block,
)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=xs_StringType_strategy)
@settings(max_examples=50)
def test_xs_stringtype_instantiation(instance):
    assert isinstance(instance, xs_StringType)

@given(instance=xs_BoolType_strategy)
@settings(max_examples=50)
def test_xs_booltype_instantiation(instance):
    assert isinstance(instance, xs_BoolType)

@given(instance=xs_FloatType_strategy)
@settings(max_examples=50)
def test_xs_floattype_instantiation(instance):
    assert isinstance(instance, xs_FloatType)

@given(instance=xs_VectorType_strategy)
@settings(max_examples=50)
def test_xs_vectortype_instantiation(instance):
    assert isinstance(instance, xs_VectorType)

@given(instance=xs_VoidType_strategy)
@settings(max_examples=50)
def test_xs_voidtype_instantiation(instance):
    assert isinstance(instance, xs_VoidType)

@given(instance=xs_IntType_strategy)
@settings(max_examples=50)
def test_xs_inttype_instantiation(instance):
    assert isinstance(instance, xs_IntType)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=xs_LiteralFloat_strategy)
@settings(max_examples=50)
def test_xs_literalfloat_instantiation(instance):
    assert isinstance(instance, xs_LiteralFloat)



@given(instance=xs_LiteralFloat_strategy)
def test_xs_literalfloat_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=xs_LiteralBool_strategy)
@settings(max_examples=50)
def test_xs_literalbool_instantiation(instance):
    assert isinstance(instance, xs_LiteralBool)



@given(instance=xs_LiteralBool_strategy)
def test_xs_literalbool_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=xs_VectorLiteral_strategy)
@settings(max_examples=50)
def test_xs_vectorliteral_instantiation(instance):
    assert isinstance(instance, xs_VectorLiteral)

@given(instance=xs_LiteralInt_strategy)
@settings(max_examples=50)
def test_xs_literalint_instantiation(instance):
    assert isinstance(instance, xs_LiteralInt)



@given(instance=xs_LiteralInt_strategy)
def test_xs_literalint_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=xs_LiteralString_strategy)
@settings(max_examples=50)
def test_xs_literalstring_instantiation(instance):
    assert isinstance(instance, xs_LiteralString)



@given(instance=xs_LiteralString_strategy)
def test_xs_literalstring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=xs_Call_strategy)
@settings(max_examples=50)
def test_xs_call_instantiation(instance):
    assert isinstance(instance, xs_Call)

@given(instance=xs_Assign_strategy)
@settings(max_examples=50)
def test_xs_assign_instantiation(instance):
    assert isinstance(instance, xs_Assign)

@given(instance=xs_OrExpression_strategy)
@settings(max_examples=50)
def test_xs_orexpression_instantiation(instance):
    assert isinstance(instance, xs_OrExpression)



@given(instance=xs_OrExpression_strategy)
def test_xs_orexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=xs_Term_strategy)
@settings(max_examples=50)
def test_xs_term_instantiation(instance):
    assert isinstance(instance, xs_Term)



@given(instance=xs_Term_strategy)
def test_xs_term_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=xs_Literal_strategy)
@settings(max_examples=50)
def test_xs_literal_instantiation(instance):
    assert isinstance(instance, xs_Literal)

@given(instance=xs_EqualsExpression_strategy)
@settings(max_examples=50)
def test_xs_equalsexpression_instantiation(instance):
    assert isinstance(instance, xs_EqualsExpression)



@given(instance=xs_EqualsExpression_strategy)
def test_xs_equalsexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=xs_AndExpression_strategy)
@settings(max_examples=50)
def test_xs_andexpression_instantiation(instance):
    assert isinstance(instance, xs_AndExpression)



@given(instance=xs_AndExpression_strategy)
def test_xs_andexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=xs_Factor_strategy)
@settings(max_examples=50)
def test_xs_factor_instantiation(instance):
    assert isinstance(instance, xs_Factor)



@given(instance=xs_Factor_strategy)
def test_xs_factor_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=xs_ComparisonExpression_strategy)
@settings(max_examples=50)
def test_xs_comparisonexpression_instantiation(instance):
    assert isinstance(instance, xs_ComparisonExpression)



@given(instance=xs_ComparisonExpression_strategy)
def test_xs_comparisonexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=xs_Var_strategy)
@settings(max_examples=50)
def test_xs_var_instantiation(instance):
    assert isinstance(instance, xs_Var)

@given(instance=xs_SwitchDefault_strategy)
@settings(max_examples=50)
def test_xs_switchdefault_instantiation(instance):
    assert isinstance(instance, xs_SwitchDefault)

@given(instance=xs_SwitchCase_strategy)
@settings(max_examples=50)
def test_xs_switchcase_instantiation(instance):
    assert isinstance(instance, xs_SwitchCase)

@given(instance=xs_Statement_strategy)
@settings(max_examples=50)
def test_xs_statement_instantiation(instance):
    assert isinstance(instance, xs_Statement)

@given(instance=xs_Type_strategy)
@settings(max_examples=50)
def test_xs_type_instantiation(instance):
    assert isinstance(instance, xs_Type)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=xs_SwitchStatement_strategy)
@settings(max_examples=50)
def test_xs_switchstatement_instantiation(instance):
    assert isinstance(instance, xs_SwitchStatement)

@given(instance=xs_ReturnStatement_strategy)
@settings(max_examples=50)
def test_xs_returnstatement_instantiation(instance):
    assert isinstance(instance, xs_ReturnStatement)

@given(instance=xs_ForStatement_strategy)
@settings(max_examples=50)
def test_xs_forstatement_instantiation(instance):
    assert isinstance(instance, xs_ForStatement)



@given(instance=xs_ForStatement_strategy)
def test_xs_forstatement_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=xs_ContinueStatement_strategy)
@settings(max_examples=50)
def test_xs_continuestatement_instantiation(instance):
    assert isinstance(instance, xs_ContinueStatement)

@given(instance=xs_PostfixStatement_strategy)
@settings(max_examples=50)
def test_xs_postfixstatement_instantiation(instance):
    assert isinstance(instance, xs_PostfixStatement)



@given(instance=xs_PostfixStatement_strategy)
def test_xs_postfixstatement_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=xs_BreakStatement_strategy)
@settings(max_examples=50)
def test_xs_breakstatement_instantiation(instance):
    assert isinstance(instance, xs_BreakStatement)

@given(instance=xs_IfElseStatement_strategy)
@settings(max_examples=50)
def test_xs_ifelsestatement_instantiation(instance):
    assert isinstance(instance, xs_IfElseStatement)

@given(instance=xs_WhileStatement_strategy)
@settings(max_examples=50)
def test_xs_whilestatement_instantiation(instance):
    assert isinstance(instance, xs_WhileStatement)

@given(instance=VarDeclaration_strategy)
@settings(max_examples=50)
def test_vardeclaration_instantiation(instance):
    assert isinstance(instance, VarDeclaration)

@given(instance=xs_ParameterDeclaration_strategy)
@settings(max_examples=50)
def test_xs_parameterdeclaration_instantiation(instance):
    assert isinstance(instance, xs_ParameterDeclaration)

@given(instance=xs_ForVarDeclaration_strategy)
@settings(max_examples=50)
def test_xs_forvardeclaration_instantiation(instance):
    assert isinstance(instance, xs_ForVarDeclaration)

@given(instance=xs_LocalVarDeclaration_strategy)
@settings(max_examples=50)
def test_xs_localvardeclaration_instantiation(instance):
    assert isinstance(instance, xs_LocalVarDeclaration)

@given(instance=xs_Expression_strategy)
@settings(max_examples=50)
def test_xs_expression_instantiation(instance):
    assert isinstance(instance, xs_Expression)

@given(instance=xs_VarDeclaration_strategy)
@settings(max_examples=50)
def test_xs_vardeclaration_instantiation(instance):
    assert isinstance(instance, xs_VarDeclaration)



@given(instance=xs_VarDeclaration_strategy)
def test_xs_vardeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=xs_FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_xs_functiondeclaration_instantiation(instance):
    assert isinstance(instance, xs_FunctionDeclaration)



@given(instance=xs_FunctionDeclaration_strategy)
def test_xs_functiondeclaration_mutable_setter(instance):
    original = instance.mutable
    instance.mutable = original
    assert instance.mutable == original



@given(instance=xs_FunctionDeclaration_strategy)
def test_xs_functiondeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xs_GlobalVarDeclaration_strategy)
@settings(max_examples=50)
def test_xs_globalvardeclaration_instantiation(instance):
    assert isinstance(instance, xs_GlobalVarDeclaration)



@given(instance=xs_GlobalVarDeclaration_strategy)
def test_xs_globalvardeclaration_extern_setter(instance):
    original = instance.extern
    instance.extern = original
    assert instance.extern == original



@given(instance=xs_GlobalVarDeclaration_strategy)
def test_xs_globalvardeclaration_const_setter(instance):
    original = instance.const
    instance.const = original
    assert instance.const == original

@given(instance=xs_IncludeDeclaration_strategy)
@settings(max_examples=50)
def test_xs_includedeclaration_instantiation(instance):
    assert isinstance(instance, xs_IncludeDeclaration)



@given(instance=xs_IncludeDeclaration_strategy)
def test_xs_includedeclaration_filePath_setter(instance):
    original = instance.filePath
    instance.filePath = original
    assert instance.filePath == original

@given(instance=xs_Declaration_strategy)
@settings(max_examples=50)
def test_xs_declaration_instantiation(instance):
    assert isinstance(instance, xs_Declaration)

@given(instance=xs_Program_strategy)
@settings(max_examples=50)
def test_xs_program_instantiation(instance):
    assert isinstance(instance, xs_Program)

@given(instance=xs_RuleDeclaration_strategy)
@settings(max_examples=50)
def test_xs_ruledeclaration_instantiation(instance):
    assert isinstance(instance, xs_RuleDeclaration)



@given(instance=xs_RuleDeclaration_strategy)
def test_xs_ruledeclaration_runImmediately_setter(instance):
    original = instance.runImmediately
    instance.runImmediately = original
    assert instance.runImmediately == original



@given(instance=xs_RuleDeclaration_strategy)
def test_xs_ruledeclaration_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=xs_RuleDeclaration_strategy)
def test_xs_ruledeclaration_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original



@given(instance=xs_RuleDeclaration_strategy)
def test_xs_ruledeclaration_highFrequency_setter(instance):
    original = instance.highFrequency
    instance.highFrequency = original
    assert instance.highFrequency == original



@given(instance=xs_RuleDeclaration_strategy)
def test_xs_ruledeclaration_maxInterval_setter(instance):
    original = instance.maxInterval
    instance.maxInterval = original
    assert instance.maxInterval == original



@given(instance=xs_RuleDeclaration_strategy)
def test_xs_ruledeclaration_minInterval_setter(instance):
    original = instance.minInterval
    instance.minInterval = original
    assert instance.minInterval == original



@given(instance=xs_RuleDeclaration_strategy)
def test_xs_ruledeclaration_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original



@given(instance=xs_RuleDeclaration_strategy)
def test_xs_ruledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xs_Block_strategy)
@settings(max_examples=50)
def test_xs_block_instantiation(instance):
    assert isinstance(instance, xs_Block)
