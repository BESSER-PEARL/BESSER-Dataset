import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    dinkiemodel::TwoOperator,
    dinkiemodel::Character,
    dinkiemodel::OneOperator,
    dinkiemodel::ArrayExpr,
    dinkiemodel::BoolVal,
    dinkiemodel::BracketExpr,
    dinkiemodel::VariableExpr,
    dinkiemodel::Number,
    dinkiemodel::ThreadID,
    Type,
    dinkiemodel::ArrayType,
    dinkiemodel::Expression,
    dinkiemodel::BaseType,
    Statement,
    dinkiemodel::FuncExpr,
    dinkiemodel::Sync,
    dinkiemodel::EmptyArrayDecl,
    dinkiemodel::FilledArrayDecl,
    dinkiemodel::Parallel,
    dinkiemodel::Assign,
    dinkiemodel::StringArrayDecl,
    dinkiemodel::IfTwo,
    dinkiemodel::WriteStatement,
    dinkiemodel::IfOne,
    dinkiemodel::Return,
    dinkiemodel::While,
    dinkiemodel::ArrayAssign,
    dinkiemodel::Declaration,
    dinkiemodel::Type,
    dinkiemodel::Argument,
    dinkiemodel::ReadStatement,
    dinkiemodel::Program,
    dinkiemodel::Statement,
    dinkiemodel::Main,
    dinkiemodel::FunctionDecl,
    EOneOperator,
    ETwoOperator,
    EBaseType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_dinkiemodel::twooperator_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::TwoOperator)


def test_dinkiemodel::twooperator_constructor_exists():
    assert callable(dinkiemodel::TwoOperator.__init__)


def test_dinkiemodel::twooperator_constructor_args():
    sig = inspect.signature(dinkiemodel::TwoOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_dinkiemodel::twooperator_has_operator():
    assert hasattr(dinkiemodel::TwoOperator, "operator")
    descriptor = None
    for klass in dinkiemodel::TwoOperator.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel::character_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::Character)


def test_dinkiemodel::character_constructor_exists():
    assert callable(dinkiemodel::Character.__init__)


def test_dinkiemodel::character_constructor_args():
    sig = inspect.signature(dinkiemodel::Character.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dinkiemodel::character_has_value():
    assert hasattr(dinkiemodel::Character, "value")
    descriptor = None
    for klass in dinkiemodel::Character.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel::oneoperator_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::OneOperator)


def test_dinkiemodel::oneoperator_constructor_exists():
    assert callable(dinkiemodel::OneOperator.__init__)


def test_dinkiemodel::oneoperator_constructor_args():
    sig = inspect.signature(dinkiemodel::OneOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_dinkiemodel::oneoperator_has_operator():
    assert hasattr(dinkiemodel::OneOperator, "operator")
    descriptor = None
    for klass in dinkiemodel::OneOperator.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel::arrayexpr_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::ArrayExpr)


def test_dinkiemodel::arrayexpr_constructor_exists():
    assert callable(dinkiemodel::ArrayExpr.__init__)


def test_dinkiemodel::arrayexpr_constructor_args():
    sig = inspect.signature(dinkiemodel::ArrayExpr.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_dinkiemodel::arrayexpr_has_varName():
    assert hasattr(dinkiemodel::ArrayExpr, "varName")
    descriptor = None
    for klass in dinkiemodel::ArrayExpr.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel::boolval_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::BoolVal)


def test_dinkiemodel::boolval_constructor_exists():
    assert callable(dinkiemodel::BoolVal.__init__)


def test_dinkiemodel::boolval_constructor_args():
    sig = inspect.signature(dinkiemodel::BoolVal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dinkiemodel::boolval_has_value():
    assert hasattr(dinkiemodel::BoolVal, "value")
    descriptor = None
    for klass in dinkiemodel::BoolVal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel::bracketexpr_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::BracketExpr)


def test_dinkiemodel::bracketexpr_constructor_exists():
    assert callable(dinkiemodel::BracketExpr.__init__)


def test_dinkiemodel::bracketexpr_constructor_args():
    sig = inspect.signature(dinkiemodel::BracketExpr.__init__)
    params = list(sig.parameters.keys())



def test_dinkiemodel::variableexpr_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::VariableExpr)


def test_dinkiemodel::variableexpr_constructor_exists():
    assert callable(dinkiemodel::VariableExpr.__init__)


def test_dinkiemodel::variableexpr_constructor_args():
    sig = inspect.signature(dinkiemodel::VariableExpr.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dinkiemodel::variableexpr_has_name():
    assert hasattr(dinkiemodel::VariableExpr, "name")
    descriptor = None
    for klass in dinkiemodel::VariableExpr.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel::number_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::Number)


def test_dinkiemodel::number_constructor_exists():
    assert callable(dinkiemodel::Number.__init__)


def test_dinkiemodel::number_constructor_args():
    sig = inspect.signature(dinkiemodel::Number.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dinkiemodel::number_has_value():
    assert hasattr(dinkiemodel::Number, "value")
    descriptor = None
    for klass in dinkiemodel::Number.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel::threadid_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::ThreadID)


def test_dinkiemodel::threadid_constructor_exists():
    assert callable(dinkiemodel::ThreadID.__init__)


def test_dinkiemodel::threadid_constructor_args():
    sig = inspect.signature(dinkiemodel::ThreadID.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_dinkiemodel::arraytype_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::ArrayType)


def test_dinkiemodel::arraytype_constructor_exists():
    assert callable(dinkiemodel::ArrayType.__init__)


def test_dinkiemodel::arraytype_constructor_args():
    sig = inspect.signature(dinkiemodel::ArrayType.__init__)
    params = list(sig.parameters.keys())
    assert "arrayType" in params, "Missing parameter 'arrayType'"

def test_dinkiemodel::arraytype_has_arrayType():
    assert hasattr(dinkiemodel::ArrayType, "arrayType")
    descriptor = None
    for klass in dinkiemodel::ArrayType.__mro__:
        if "arrayType" in klass.__dict__:
            descriptor = klass.__dict__["arrayType"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel::expression_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::Expression)


def test_dinkiemodel::expression_constructor_exists():
    assert callable(dinkiemodel::Expression.__init__)


def test_dinkiemodel::expression_constructor_args():
    sig = inspect.signature(dinkiemodel::Expression.__init__)
    params = list(sig.parameters.keys())



def test_dinkiemodel::basetype_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::BaseType)


def test_dinkiemodel::basetype_constructor_exists():
    assert callable(dinkiemodel::BaseType.__init__)


def test_dinkiemodel::basetype_constructor_args():
    sig = inspect.signature(dinkiemodel::BaseType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_dinkiemodel::basetype_has_type():
    assert hasattr(dinkiemodel::BaseType, "type")
    descriptor = None
    for klass in dinkiemodel::BaseType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_dinkiemodel::funcexpr_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::FuncExpr)


def test_dinkiemodel::funcexpr_constructor_exists():
    assert callable(dinkiemodel::FuncExpr.__init__)


def test_dinkiemodel::funcexpr_constructor_args():
    sig = inspect.signature(dinkiemodel::FuncExpr.__init__)
    params = list(sig.parameters.keys())
    assert "funcName" in params, "Missing parameter 'funcName'"

def test_dinkiemodel::funcexpr_has_funcName():
    assert hasattr(dinkiemodel::FuncExpr, "funcName")
    descriptor = None
    for klass in dinkiemodel::FuncExpr.__mro__:
        if "funcName" in klass.__dict__:
            descriptor = klass.__dict__["funcName"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel::sync_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::Sync)


def test_dinkiemodel::sync_constructor_exists():
    assert callable(dinkiemodel::Sync.__init__)


def test_dinkiemodel::sync_constructor_args():
    sig = inspect.signature(dinkiemodel::Sync.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_dinkiemodel::sync_has_varName():
    assert hasattr(dinkiemodel::Sync, "varName")
    descriptor = None
    for klass in dinkiemodel::Sync.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel::emptyarraydecl_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::EmptyArrayDecl)


def test_dinkiemodel::emptyarraydecl_constructor_exists():
    assert callable(dinkiemodel::EmptyArrayDecl.__init__)


def test_dinkiemodel::emptyarraydecl_constructor_args():
    sig = inspect.signature(dinkiemodel::EmptyArrayDecl.__init__)
    params = list(sig.parameters.keys())
    assert "global_" in params, "Missing parameter 'global_'"
    assert "varName" in params, "Missing parameter 'varName'"
    assert "size" in params, "Missing parameter 'size'"

def test_dinkiemodel::emptyarraydecl_has_global_():
    assert hasattr(dinkiemodel::EmptyArrayDecl, "global_")
    descriptor = None
    for klass in dinkiemodel::EmptyArrayDecl.__mro__:
        if "global_" in klass.__dict__:
            descriptor = klass.__dict__["global_"]
            break
    assert isinstance(descriptor, property)

def test_dinkiemodel::emptyarraydecl_has_varName():
    assert hasattr(dinkiemodel::EmptyArrayDecl, "varName")
    descriptor = None
    for klass in dinkiemodel::EmptyArrayDecl.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)

def test_dinkiemodel::emptyarraydecl_has_size():
    assert hasattr(dinkiemodel::EmptyArrayDecl, "size")
    descriptor = None
    for klass in dinkiemodel::EmptyArrayDecl.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel::filledarraydecl_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::FilledArrayDecl)


def test_dinkiemodel::filledarraydecl_constructor_exists():
    assert callable(dinkiemodel::FilledArrayDecl.__init__)


def test_dinkiemodel::filledarraydecl_constructor_args():
    sig = inspect.signature(dinkiemodel::FilledArrayDecl.__init__)
    params = list(sig.parameters.keys())
    assert "global_" in params, "Missing parameter 'global_'"
    assert "varName" in params, "Missing parameter 'varName'"

def test_dinkiemodel::filledarraydecl_has_global_():
    assert hasattr(dinkiemodel::FilledArrayDecl, "global_")
    descriptor = None
    for klass in dinkiemodel::FilledArrayDecl.__mro__:
        if "global_" in klass.__dict__:
            descriptor = klass.__dict__["global_"]
            break
    assert isinstance(descriptor, property)

def test_dinkiemodel::filledarraydecl_has_varName():
    assert hasattr(dinkiemodel::FilledArrayDecl, "varName")
    descriptor = None
    for klass in dinkiemodel::FilledArrayDecl.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel::parallel_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::Parallel)


def test_dinkiemodel::parallel_constructor_exists():
    assert callable(dinkiemodel::Parallel.__init__)


def test_dinkiemodel::parallel_constructor_args():
    sig = inspect.signature(dinkiemodel::Parallel.__init__)
    params = list(sig.parameters.keys())
    assert "nrOfThreads" in params, "Missing parameter 'nrOfThreads'"

def test_dinkiemodel::parallel_has_nrOfThreads():
    assert hasattr(dinkiemodel::Parallel, "nrOfThreads")
    descriptor = None
    for klass in dinkiemodel::Parallel.__mro__:
        if "nrOfThreads" in klass.__dict__:
            descriptor = klass.__dict__["nrOfThreads"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel::assign_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::Assign)


def test_dinkiemodel::assign_constructor_exists():
    assert callable(dinkiemodel::Assign.__init__)


def test_dinkiemodel::assign_constructor_args():
    sig = inspect.signature(dinkiemodel::Assign.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_dinkiemodel::assign_has_varName():
    assert hasattr(dinkiemodel::Assign, "varName")
    descriptor = None
    for klass in dinkiemodel::Assign.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel::stringarraydecl_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::StringArrayDecl)


def test_dinkiemodel::stringarraydecl_constructor_exists():
    assert callable(dinkiemodel::StringArrayDecl.__init__)


def test_dinkiemodel::stringarraydecl_constructor_args():
    sig = inspect.signature(dinkiemodel::StringArrayDecl.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"
    assert "content" in params, "Missing parameter 'content'"
    assert "global_" in params, "Missing parameter 'global_'"

def test_dinkiemodel::stringarraydecl_has_varName():
    assert hasattr(dinkiemodel::StringArrayDecl, "varName")
    descriptor = None
    for klass in dinkiemodel::StringArrayDecl.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)

def test_dinkiemodel::stringarraydecl_has_content():
    assert hasattr(dinkiemodel::StringArrayDecl, "content")
    descriptor = None
    for klass in dinkiemodel::StringArrayDecl.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_dinkiemodel::stringarraydecl_has_global_():
    assert hasattr(dinkiemodel::StringArrayDecl, "global_")
    descriptor = None
    for klass in dinkiemodel::StringArrayDecl.__mro__:
        if "global_" in klass.__dict__:
            descriptor = klass.__dict__["global_"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel::iftwo_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::IfTwo)


def test_dinkiemodel::iftwo_constructor_exists():
    assert callable(dinkiemodel::IfTwo.__init__)


def test_dinkiemodel::iftwo_constructor_args():
    sig = inspect.signature(dinkiemodel::IfTwo.__init__)
    params = list(sig.parameters.keys())



def test_dinkiemodel::writestatement_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::WriteStatement)


def test_dinkiemodel::writestatement_constructor_exists():
    assert callable(dinkiemodel::WriteStatement.__init__)


def test_dinkiemodel::writestatement_constructor_args():
    sig = inspect.signature(dinkiemodel::WriteStatement.__init__)
    params = list(sig.parameters.keys())



def test_dinkiemodel::ifone_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::IfOne)


def test_dinkiemodel::ifone_constructor_exists():
    assert callable(dinkiemodel::IfOne.__init__)


def test_dinkiemodel::ifone_constructor_args():
    sig = inspect.signature(dinkiemodel::IfOne.__init__)
    params = list(sig.parameters.keys())



def test_dinkiemodel::return_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::Return)


def test_dinkiemodel::return_constructor_exists():
    assert callable(dinkiemodel::Return.__init__)


def test_dinkiemodel::return_constructor_args():
    sig = inspect.signature(dinkiemodel::Return.__init__)
    params = list(sig.parameters.keys())



def test_dinkiemodel::while_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::While)


def test_dinkiemodel::while_constructor_exists():
    assert callable(dinkiemodel::While.__init__)


def test_dinkiemodel::while_constructor_args():
    sig = inspect.signature(dinkiemodel::While.__init__)
    params = list(sig.parameters.keys())



def test_dinkiemodel::arrayassign_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::ArrayAssign)


def test_dinkiemodel::arrayassign_constructor_exists():
    assert callable(dinkiemodel::ArrayAssign.__init__)


def test_dinkiemodel::arrayassign_constructor_args():
    sig = inspect.signature(dinkiemodel::ArrayAssign.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_dinkiemodel::arrayassign_has_varName():
    assert hasattr(dinkiemodel::ArrayAssign, "varName")
    descriptor = None
    for klass in dinkiemodel::ArrayAssign.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel::declaration_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::Declaration)


def test_dinkiemodel::declaration_constructor_exists():
    assert callable(dinkiemodel::Declaration.__init__)


def test_dinkiemodel::declaration_constructor_args():
    sig = inspect.signature(dinkiemodel::Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"
    assert "global_" in params, "Missing parameter 'global_'"

def test_dinkiemodel::declaration_has_varName():
    assert hasattr(dinkiemodel::Declaration, "varName")
    descriptor = None
    for klass in dinkiemodel::Declaration.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)

def test_dinkiemodel::declaration_has_global_():
    assert hasattr(dinkiemodel::Declaration, "global_")
    descriptor = None
    for klass in dinkiemodel::Declaration.__mro__:
        if "global_" in klass.__dict__:
            descriptor = klass.__dict__["global_"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel::type_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::Type)


def test_dinkiemodel::type_constructor_exists():
    assert callable(dinkiemodel::Type.__init__)


def test_dinkiemodel::type_constructor_args():
    sig = inspect.signature(dinkiemodel::Type.__init__)
    params = list(sig.parameters.keys())



def test_dinkiemodel::argument_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::Argument)


def test_dinkiemodel::argument_constructor_exists():
    assert callable(dinkiemodel::Argument.__init__)


def test_dinkiemodel::argument_constructor_args():
    sig = inspect.signature(dinkiemodel::Argument.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dinkiemodel::argument_has_name():
    assert hasattr(dinkiemodel::Argument, "name")
    descriptor = None
    for klass in dinkiemodel::Argument.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel::readstatement_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::ReadStatement)


def test_dinkiemodel::readstatement_constructor_exists():
    assert callable(dinkiemodel::ReadStatement.__init__)


def test_dinkiemodel::readstatement_constructor_args():
    sig = inspect.signature(dinkiemodel::ReadStatement.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_dinkiemodel::readstatement_has_varName():
    assert hasattr(dinkiemodel::ReadStatement, "varName")
    descriptor = None
    for klass in dinkiemodel::ReadStatement.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel::program_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::Program)


def test_dinkiemodel::program_constructor_exists():
    assert callable(dinkiemodel::Program.__init__)


def test_dinkiemodel::program_constructor_args():
    sig = inspect.signature(dinkiemodel::Program.__init__)
    params = list(sig.parameters.keys())



def test_dinkiemodel::statement_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::Statement)


def test_dinkiemodel::statement_constructor_exists():
    assert callable(dinkiemodel::Statement.__init__)


def test_dinkiemodel::statement_constructor_args():
    sig = inspect.signature(dinkiemodel::Statement.__init__)
    params = list(sig.parameters.keys())



def test_dinkiemodel::main_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::Main)


def test_dinkiemodel::main_constructor_exists():
    assert callable(dinkiemodel::Main.__init__)


def test_dinkiemodel::main_constructor_args():
    sig = inspect.signature(dinkiemodel::Main.__init__)
    params = list(sig.parameters.keys())



def test_dinkiemodel::functiondecl_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel::FunctionDecl)


def test_dinkiemodel::functiondecl_constructor_exists():
    assert callable(dinkiemodel::FunctionDecl.__init__)


def test_dinkiemodel::functiondecl_constructor_args():
    sig = inspect.signature(dinkiemodel::FunctionDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dinkiemodel::functiondecl_has_name():
    assert hasattr(dinkiemodel::FunctionDecl, "name")
    descriptor = None
    for klass in dinkiemodel::FunctionDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_eoneoperator_exists():
    # Check that the Enumeration exists
    assert EOneOperator is not None

def test_eoneoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EOneOperator]
    expected_literals = [
        "MINUS",
        "NOT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EOneOperator"

def test_etwooperator_exists():
    # Check that the Enumeration exists
    assert ETwoOperator is not None

def test_etwooperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ETwoOperator]
    expected_literals = [
        "GT",
        "LT",
        "MINUS",
        "LE",
        "DEVIDE",
        "XOR",
        "TIMES",
        "NOT_EQUAL",
        "OR",
        "PLUS",
        "AND",
        "EQUAL",
        "GE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ETwoOperator"

def test_ebasetype_exists():
    # Check that the Enumeration exists
    assert EBaseType is not None

def test_ebasetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EBaseType]
    expected_literals = [
        "BOOL",
        "INT",
        "CHAR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EBaseType"


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
Expression_strategy = st.builds(
    Expression,
)
dinkiemodel::TwoOperator_strategy = st.builds(
    dinkiemodel::TwoOperator,
    operator=
        safe_text
)
dinkiemodel::Character_strategy = st.builds(
    dinkiemodel::Character,
    value=
        safe_text
)
dinkiemodel::OneOperator_strategy = st.builds(
    dinkiemodel::OneOperator,
    operator=
        safe_text
)
dinkiemodel::ArrayExpr_strategy = st.builds(
    dinkiemodel::ArrayExpr,
    varName=
        safe_text
)
dinkiemodel::BoolVal_strategy = st.builds(
    dinkiemodel::BoolVal,
    value=
        st.booleans()
)
dinkiemodel::BracketExpr_strategy = st.builds(
    dinkiemodel::BracketExpr,
)
dinkiemodel::VariableExpr_strategy = st.builds(
    dinkiemodel::VariableExpr,
    name=
        safe_text
)
dinkiemodel::Number_strategy = st.builds(
    dinkiemodel::Number,
    value=
        st.integers()
)
dinkiemodel::ThreadID_strategy = st.builds(
    dinkiemodel::ThreadID,
)
Type_strategy = st.builds(
    Type,
)
dinkiemodel::ArrayType_strategy = st.builds(
    dinkiemodel::ArrayType,
    arrayType=
        safe_text
)
dinkiemodel::Expression_strategy = st.builds(
    dinkiemodel::Expression,
)
dinkiemodel::BaseType_strategy = st.builds(
    dinkiemodel::BaseType,
    type=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
dinkiemodel::FuncExpr_strategy = st.builds(
    dinkiemodel::FuncExpr,
    funcName=
        safe_text
)
dinkiemodel::Sync_strategy = st.builds(
    dinkiemodel::Sync,
    varName=
        safe_text
)
dinkiemodel::EmptyArrayDecl_strategy = st.builds(
    dinkiemodel::EmptyArrayDecl,
    global_=
        st.booleans(),
    varName=
        safe_text,
    size=
        st.integers()
)
dinkiemodel::FilledArrayDecl_strategy = st.builds(
    dinkiemodel::FilledArrayDecl,
    global_=
        st.booleans(),
    varName=
        safe_text
)
dinkiemodel::Parallel_strategy = st.builds(
    dinkiemodel::Parallel,
    nrOfThreads=
        st.integers()
)
dinkiemodel::Assign_strategy = st.builds(
    dinkiemodel::Assign,
    varName=
        safe_text
)
dinkiemodel::StringArrayDecl_strategy = st.builds(
    dinkiemodel::StringArrayDecl,
    varName=
        safe_text,
    content=
        safe_text,
    global_=
        st.booleans()
)
dinkiemodel::IfTwo_strategy = st.builds(
    dinkiemodel::IfTwo,
)
dinkiemodel::WriteStatement_strategy = st.builds(
    dinkiemodel::WriteStatement,
)
dinkiemodel::IfOne_strategy = st.builds(
    dinkiemodel::IfOne,
)
dinkiemodel::Return_strategy = st.builds(
    dinkiemodel::Return,
)
dinkiemodel::While_strategy = st.builds(
    dinkiemodel::While,
)
dinkiemodel::ArrayAssign_strategy = st.builds(
    dinkiemodel::ArrayAssign,
    varName=
        safe_text
)
dinkiemodel::Declaration_strategy = st.builds(
    dinkiemodel::Declaration,
    varName=
        safe_text,
    global_=
        st.booleans()
)
dinkiemodel::Type_strategy = st.builds(
    dinkiemodel::Type,
)
dinkiemodel::Argument_strategy = st.builds(
    dinkiemodel::Argument,
    name=
        safe_text
)
dinkiemodel::ReadStatement_strategy = st.builds(
    dinkiemodel::ReadStatement,
    varName=
        safe_text
)
dinkiemodel::Program_strategy = st.builds(
    dinkiemodel::Program,
)
dinkiemodel::Statement_strategy = st.builds(
    dinkiemodel::Statement,
)
dinkiemodel::Main_strategy = st.builds(
    dinkiemodel::Main,
)
dinkiemodel::FunctionDecl_strategy = st.builds(
    dinkiemodel::FunctionDecl,
    name=
        safe_text
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=dinkiemodel::TwoOperator_strategy)
@settings(max_examples=50)
def test_dinkiemodel::twooperator_instantiation(instance):
    assert isinstance(instance, dinkiemodel::TwoOperator)

@given(instance=dinkiemodel::TwoOperator_strategy)
def test_dinkiemodel::twooperator_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=dinkiemodel::TwoOperator_strategy)
def test_dinkiemodel::twooperator_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=dinkiemodel::Character_strategy)
@settings(max_examples=50)
def test_dinkiemodel::character_instantiation(instance):
    assert isinstance(instance, dinkiemodel::Character)

@given(instance=dinkiemodel::Character_strategy)
def test_dinkiemodel::character_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=dinkiemodel::Character_strategy)
def test_dinkiemodel::character_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dinkiemodel::OneOperator_strategy)
@settings(max_examples=50)
def test_dinkiemodel::oneoperator_instantiation(instance):
    assert isinstance(instance, dinkiemodel::OneOperator)

@given(instance=dinkiemodel::OneOperator_strategy)
def test_dinkiemodel::oneoperator_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=dinkiemodel::OneOperator_strategy)
def test_dinkiemodel::oneoperator_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=dinkiemodel::ArrayExpr_strategy)
@settings(max_examples=50)
def test_dinkiemodel::arrayexpr_instantiation(instance):
    assert isinstance(instance, dinkiemodel::ArrayExpr)

@given(instance=dinkiemodel::ArrayExpr_strategy)
def test_dinkiemodel::arrayexpr_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=dinkiemodel::ArrayExpr_strategy)
def test_dinkiemodel::arrayexpr_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=dinkiemodel::BoolVal_strategy)
@settings(max_examples=50)
def test_dinkiemodel::boolval_instantiation(instance):
    assert isinstance(instance, dinkiemodel::BoolVal)

@given(instance=dinkiemodel::BoolVal_strategy)
def test_dinkiemodel::boolval_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=dinkiemodel::BoolVal_strategy)
def test_dinkiemodel::boolval_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dinkiemodel::BracketExpr_strategy)
@settings(max_examples=50)
def test_dinkiemodel::bracketexpr_instantiation(instance):
    assert isinstance(instance, dinkiemodel::BracketExpr)

@given(instance=dinkiemodel::VariableExpr_strategy)
@settings(max_examples=50)
def test_dinkiemodel::variableexpr_instantiation(instance):
    assert isinstance(instance, dinkiemodel::VariableExpr)

@given(instance=dinkiemodel::VariableExpr_strategy)
def test_dinkiemodel::variableexpr_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dinkiemodel::VariableExpr_strategy)
def test_dinkiemodel::variableexpr_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dinkiemodel::Number_strategy)
@settings(max_examples=50)
def test_dinkiemodel::number_instantiation(instance):
    assert isinstance(instance, dinkiemodel::Number)

@given(instance=dinkiemodel::Number_strategy)
def test_dinkiemodel::number_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=dinkiemodel::Number_strategy)
def test_dinkiemodel::number_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dinkiemodel::ThreadID_strategy)
@settings(max_examples=50)
def test_dinkiemodel::threadid_instantiation(instance):
    assert isinstance(instance, dinkiemodel::ThreadID)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=dinkiemodel::ArrayType_strategy)
@settings(max_examples=50)
def test_dinkiemodel::arraytype_instantiation(instance):
    assert isinstance(instance, dinkiemodel::ArrayType)

@given(instance=dinkiemodel::ArrayType_strategy)
def test_dinkiemodel::arraytype_arrayType_type(instance):
    assert isinstance(instance.arrayType, str)


@given(instance=dinkiemodel::ArrayType_strategy)
def test_dinkiemodel::arraytype_arrayType_setter(instance):
    original = instance.arrayType
    instance.arrayType = original
    assert instance.arrayType == original

@given(instance=dinkiemodel::Expression_strategy)
@settings(max_examples=50)
def test_dinkiemodel::expression_instantiation(instance):
    assert isinstance(instance, dinkiemodel::Expression)

@given(instance=dinkiemodel::BaseType_strategy)
@settings(max_examples=50)
def test_dinkiemodel::basetype_instantiation(instance):
    assert isinstance(instance, dinkiemodel::BaseType)

@given(instance=dinkiemodel::BaseType_strategy)
def test_dinkiemodel::basetype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=dinkiemodel::BaseType_strategy)
def test_dinkiemodel::basetype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=dinkiemodel::FuncExpr_strategy)
@settings(max_examples=50)
def test_dinkiemodel::funcexpr_instantiation(instance):
    assert isinstance(instance, dinkiemodel::FuncExpr)

@given(instance=dinkiemodel::FuncExpr_strategy)
def test_dinkiemodel::funcexpr_funcName_type(instance):
    assert isinstance(instance.funcName, str)


@given(instance=dinkiemodel::FuncExpr_strategy)
def test_dinkiemodel::funcexpr_funcName_setter(instance):
    original = instance.funcName
    instance.funcName = original
    assert instance.funcName == original

@given(instance=dinkiemodel::Sync_strategy)
@settings(max_examples=50)
def test_dinkiemodel::sync_instantiation(instance):
    assert isinstance(instance, dinkiemodel::Sync)

@given(instance=dinkiemodel::Sync_strategy)
def test_dinkiemodel::sync_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=dinkiemodel::Sync_strategy)
def test_dinkiemodel::sync_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=dinkiemodel::EmptyArrayDecl_strategy)
@settings(max_examples=50)
def test_dinkiemodel::emptyarraydecl_instantiation(instance):
    assert isinstance(instance, dinkiemodel::EmptyArrayDecl)

@given(instance=dinkiemodel::EmptyArrayDecl_strategy)
def test_dinkiemodel::emptyarraydecl_global__type(instance):
    assert isinstance(instance.global_, bool)


@given(instance=dinkiemodel::EmptyArrayDecl_strategy)
def test_dinkiemodel::emptyarraydecl_global__setter(instance):
    original = instance.global_
    instance.global_ = original
    assert instance.global_ == original

@given(instance=dinkiemodel::EmptyArrayDecl_strategy)
def test_dinkiemodel::emptyarraydecl_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=dinkiemodel::EmptyArrayDecl_strategy)
def test_dinkiemodel::emptyarraydecl_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=dinkiemodel::EmptyArrayDecl_strategy)
def test_dinkiemodel::emptyarraydecl_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=dinkiemodel::EmptyArrayDecl_strategy)
def test_dinkiemodel::emptyarraydecl_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=dinkiemodel::FilledArrayDecl_strategy)
@settings(max_examples=50)
def test_dinkiemodel::filledarraydecl_instantiation(instance):
    assert isinstance(instance, dinkiemodel::FilledArrayDecl)

@given(instance=dinkiemodel::FilledArrayDecl_strategy)
def test_dinkiemodel::filledarraydecl_global__type(instance):
    assert isinstance(instance.global_, bool)


@given(instance=dinkiemodel::FilledArrayDecl_strategy)
def test_dinkiemodel::filledarraydecl_global__setter(instance):
    original = instance.global_
    instance.global_ = original
    assert instance.global_ == original

@given(instance=dinkiemodel::FilledArrayDecl_strategy)
def test_dinkiemodel::filledarraydecl_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=dinkiemodel::FilledArrayDecl_strategy)
def test_dinkiemodel::filledarraydecl_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=dinkiemodel::Parallel_strategy)
@settings(max_examples=50)
def test_dinkiemodel::parallel_instantiation(instance):
    assert isinstance(instance, dinkiemodel::Parallel)

@given(instance=dinkiemodel::Parallel_strategy)
def test_dinkiemodel::parallel_nrOfThreads_type(instance):
    assert isinstance(instance.nrOfThreads, int)


@given(instance=dinkiemodel::Parallel_strategy)
def test_dinkiemodel::parallel_nrOfThreads_setter(instance):
    original = instance.nrOfThreads
    instance.nrOfThreads = original
    assert instance.nrOfThreads == original

@given(instance=dinkiemodel::Assign_strategy)
@settings(max_examples=50)
def test_dinkiemodel::assign_instantiation(instance):
    assert isinstance(instance, dinkiemodel::Assign)

@given(instance=dinkiemodel::Assign_strategy)
def test_dinkiemodel::assign_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=dinkiemodel::Assign_strategy)
def test_dinkiemodel::assign_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=dinkiemodel::StringArrayDecl_strategy)
@settings(max_examples=50)
def test_dinkiemodel::stringarraydecl_instantiation(instance):
    assert isinstance(instance, dinkiemodel::StringArrayDecl)

@given(instance=dinkiemodel::StringArrayDecl_strategy)
def test_dinkiemodel::stringarraydecl_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=dinkiemodel::StringArrayDecl_strategy)
def test_dinkiemodel::stringarraydecl_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=dinkiemodel::StringArrayDecl_strategy)
def test_dinkiemodel::stringarraydecl_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=dinkiemodel::StringArrayDecl_strategy)
def test_dinkiemodel::stringarraydecl_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=dinkiemodel::StringArrayDecl_strategy)
def test_dinkiemodel::stringarraydecl_global__type(instance):
    assert isinstance(instance.global_, bool)


@given(instance=dinkiemodel::StringArrayDecl_strategy)
def test_dinkiemodel::stringarraydecl_global__setter(instance):
    original = instance.global_
    instance.global_ = original
    assert instance.global_ == original

@given(instance=dinkiemodel::IfTwo_strategy)
@settings(max_examples=50)
def test_dinkiemodel::iftwo_instantiation(instance):
    assert isinstance(instance, dinkiemodel::IfTwo)

@given(instance=dinkiemodel::WriteStatement_strategy)
@settings(max_examples=50)
def test_dinkiemodel::writestatement_instantiation(instance):
    assert isinstance(instance, dinkiemodel::WriteStatement)

@given(instance=dinkiemodel::IfOne_strategy)
@settings(max_examples=50)
def test_dinkiemodel::ifone_instantiation(instance):
    assert isinstance(instance, dinkiemodel::IfOne)

@given(instance=dinkiemodel::Return_strategy)
@settings(max_examples=50)
def test_dinkiemodel::return_instantiation(instance):
    assert isinstance(instance, dinkiemodel::Return)

@given(instance=dinkiemodel::While_strategy)
@settings(max_examples=50)
def test_dinkiemodel::while_instantiation(instance):
    assert isinstance(instance, dinkiemodel::While)

@given(instance=dinkiemodel::ArrayAssign_strategy)
@settings(max_examples=50)
def test_dinkiemodel::arrayassign_instantiation(instance):
    assert isinstance(instance, dinkiemodel::ArrayAssign)

@given(instance=dinkiemodel::ArrayAssign_strategy)
def test_dinkiemodel::arrayassign_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=dinkiemodel::ArrayAssign_strategy)
def test_dinkiemodel::arrayassign_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=dinkiemodel::Declaration_strategy)
@settings(max_examples=50)
def test_dinkiemodel::declaration_instantiation(instance):
    assert isinstance(instance, dinkiemodel::Declaration)

@given(instance=dinkiemodel::Declaration_strategy)
def test_dinkiemodel::declaration_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=dinkiemodel::Declaration_strategy)
def test_dinkiemodel::declaration_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=dinkiemodel::Declaration_strategy)
def test_dinkiemodel::declaration_global__type(instance):
    assert isinstance(instance.global_, bool)


@given(instance=dinkiemodel::Declaration_strategy)
def test_dinkiemodel::declaration_global__setter(instance):
    original = instance.global_
    instance.global_ = original
    assert instance.global_ == original

@given(instance=dinkiemodel::Type_strategy)
@settings(max_examples=50)
def test_dinkiemodel::type_instantiation(instance):
    assert isinstance(instance, dinkiemodel::Type)

@given(instance=dinkiemodel::Argument_strategy)
@settings(max_examples=50)
def test_dinkiemodel::argument_instantiation(instance):
    assert isinstance(instance, dinkiemodel::Argument)

@given(instance=dinkiemodel::Argument_strategy)
def test_dinkiemodel::argument_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dinkiemodel::Argument_strategy)
def test_dinkiemodel::argument_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dinkiemodel::ReadStatement_strategy)
@settings(max_examples=50)
def test_dinkiemodel::readstatement_instantiation(instance):
    assert isinstance(instance, dinkiemodel::ReadStatement)

@given(instance=dinkiemodel::ReadStatement_strategy)
def test_dinkiemodel::readstatement_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=dinkiemodel::ReadStatement_strategy)
def test_dinkiemodel::readstatement_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=dinkiemodel::Program_strategy)
@settings(max_examples=50)
def test_dinkiemodel::program_instantiation(instance):
    assert isinstance(instance, dinkiemodel::Program)

@given(instance=dinkiemodel::Statement_strategy)
@settings(max_examples=50)
def test_dinkiemodel::statement_instantiation(instance):
    assert isinstance(instance, dinkiemodel::Statement)

@given(instance=dinkiemodel::Main_strategy)
@settings(max_examples=50)
def test_dinkiemodel::main_instantiation(instance):
    assert isinstance(instance, dinkiemodel::Main)

@given(instance=dinkiemodel::FunctionDecl_strategy)
@settings(max_examples=50)
def test_dinkiemodel::functiondecl_instantiation(instance):
    assert isinstance(instance, dinkiemodel::FunctionDecl)

@given(instance=dinkiemodel::FunctionDecl_strategy)
def test_dinkiemodel::functiondecl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dinkiemodel::FunctionDecl_strategy)
def test_dinkiemodel::functiondecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
