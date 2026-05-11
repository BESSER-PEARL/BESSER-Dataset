import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    xs::SwitchCase,
    xs::Statement,
    xs::Type,
    Statement,
    xs::SwitchStatement,
    VarDeclaration,
    xs::ParameterDeclaration,
    xs::ForVarDeclaration,
    xs::LocalVarDeclaration,
    xs::Expression,
    xs::VarDeclaration,
    Declaration,
    xs::GlobalVarDeclaration,
    xs::FunctionDeclaration,
    xs::IncludeDeclaration,
    xs::Declaration,
    xs::Program,
    xs::RuleDeclaration,
    xs::Block,
    Type,
    xs::VectorType,
    xs::StringType,
    xs::FloatType,
    xs::VoidType,
    xs::BoolType,
    xs::IntType,
    Literal,
    xs::VectorLiteral,
    xs::LiteralBool,
    xs::LiteralFloat,
    xs::LiteralInt,
    xs::LiteralString,
    xs::BreakStatement,
    xs::ContinueStatement,
    xs::ReturnStatement,
    xs::ForStatement,
    xs::WhileStatement,
    xs::IfElseStatement,
    xs::PostfixStatement,
    Expression,
    xs::OrExpression,
    xs::Factor,
    xs::EqualsExpression,
    xs::Call,
    xs::Assign,
    xs::Term,
    xs::AndExpression,
    xs::Literal,
    xs::ComparisonExpression,
    xs::Var,
    xs::SwitchDefault,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_xs::switchcase_is_not_abstract():
    assert not inspect.isabstract(xs::SwitchCase)


def test_xs::switchcase_constructor_exists():
    assert callable(xs::SwitchCase.__init__)


def test_xs::switchcase_constructor_args():
    sig = inspect.signature(xs::SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_xs::statement_is_not_abstract():
    assert not inspect.isabstract(xs::Statement)


def test_xs::statement_constructor_exists():
    assert callable(xs::Statement.__init__)


def test_xs::statement_constructor_args():
    sig = inspect.signature(xs::Statement.__init__)
    params = list(sig.parameters.keys())



def test_xs::type_is_not_abstract():
    assert not inspect.isabstract(xs::Type)


def test_xs::type_constructor_exists():
    assert callable(xs::Type.__init__)


def test_xs::type_constructor_args():
    sig = inspect.signature(xs::Type.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_xs::switchstatement_is_not_abstract():
    assert not inspect.isabstract(xs::SwitchStatement)


def test_xs::switchstatement_constructor_exists():
    assert callable(xs::SwitchStatement.__init__)


def test_xs::switchstatement_constructor_args():
    sig = inspect.signature(xs::SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_vardeclaration_is_not_abstract():
    assert not inspect.isabstract(VarDeclaration)


def test_vardeclaration_constructor_exists():
    assert callable(VarDeclaration.__init__)


def test_vardeclaration_constructor_args():
    sig = inspect.signature(VarDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_xs::parameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(xs::ParameterDeclaration)


def test_xs::parameterdeclaration_constructor_exists():
    assert callable(xs::ParameterDeclaration.__init__)


def test_xs::parameterdeclaration_constructor_args():
    sig = inspect.signature(xs::ParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_xs::forvardeclaration_is_not_abstract():
    assert not inspect.isabstract(xs::ForVarDeclaration)


def test_xs::forvardeclaration_constructor_exists():
    assert callable(xs::ForVarDeclaration.__init__)


def test_xs::forvardeclaration_constructor_args():
    sig = inspect.signature(xs::ForVarDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_xs::localvardeclaration_is_not_abstract():
    assert not inspect.isabstract(xs::LocalVarDeclaration)


def test_xs::localvardeclaration_constructor_exists():
    assert callable(xs::LocalVarDeclaration.__init__)


def test_xs::localvardeclaration_constructor_args():
    sig = inspect.signature(xs::LocalVarDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_xs::expression_is_not_abstract():
    assert not inspect.isabstract(xs::Expression)


def test_xs::expression_constructor_exists():
    assert callable(xs::Expression.__init__)


def test_xs::expression_constructor_args():
    sig = inspect.signature(xs::Expression.__init__)
    params = list(sig.parameters.keys())



def test_xs::vardeclaration_is_not_abstract():
    assert not inspect.isabstract(xs::VarDeclaration)


def test_xs::vardeclaration_constructor_exists():
    assert callable(xs::VarDeclaration.__init__)


def test_xs::vardeclaration_constructor_args():
    sig = inspect.signature(xs::VarDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_xs::vardeclaration_has_name():
    assert hasattr(xs::VarDeclaration, "name")
    descriptor = None
    for klass in xs::VarDeclaration.__mro__:
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



def test_xs::globalvardeclaration_is_not_abstract():
    assert not inspect.isabstract(xs::GlobalVarDeclaration)


def test_xs::globalvardeclaration_constructor_exists():
    assert callable(xs::GlobalVarDeclaration.__init__)


def test_xs::globalvardeclaration_constructor_args():
    sig = inspect.signature(xs::GlobalVarDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "extern" in params, "Missing parameter 'extern'"
    assert "const" in params, "Missing parameter 'const'"

def test_xs::globalvardeclaration_has_extern():
    assert hasattr(xs::GlobalVarDeclaration, "extern")
    descriptor = None
    for klass in xs::GlobalVarDeclaration.__mro__:
        if "extern" in klass.__dict__:
            descriptor = klass.__dict__["extern"]
            break
    assert isinstance(descriptor, property)

def test_xs::globalvardeclaration_has_const():
    assert hasattr(xs::GlobalVarDeclaration, "const")
    descriptor = None
    for klass in xs::GlobalVarDeclaration.__mro__:
        if "const" in klass.__dict__:
            descriptor = klass.__dict__["const"]
            break
    assert isinstance(descriptor, property)



def test_xs::functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(xs::FunctionDeclaration)


def test_xs::functiondeclaration_constructor_exists():
    assert callable(xs::FunctionDeclaration.__init__)


def test_xs::functiondeclaration_constructor_args():
    sig = inspect.signature(xs::FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "mutable" in params, "Missing parameter 'mutable'"
    assert "name" in params, "Missing parameter 'name'"

def test_xs::functiondeclaration_has_mutable():
    assert hasattr(xs::FunctionDeclaration, "mutable")
    descriptor = None
    for klass in xs::FunctionDeclaration.__mro__:
        if "mutable" in klass.__dict__:
            descriptor = klass.__dict__["mutable"]
            break
    assert isinstance(descriptor, property)

def test_xs::functiondeclaration_has_name():
    assert hasattr(xs::FunctionDeclaration, "name")
    descriptor = None
    for klass in xs::FunctionDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xs::includedeclaration_is_not_abstract():
    assert not inspect.isabstract(xs::IncludeDeclaration)


def test_xs::includedeclaration_constructor_exists():
    assert callable(xs::IncludeDeclaration.__init__)


def test_xs::includedeclaration_constructor_args():
    sig = inspect.signature(xs::IncludeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "filePath" in params, "Missing parameter 'filePath'"

def test_xs::includedeclaration_has_filePath():
    assert hasattr(xs::IncludeDeclaration, "filePath")
    descriptor = None
    for klass in xs::IncludeDeclaration.__mro__:
        if "filePath" in klass.__dict__:
            descriptor = klass.__dict__["filePath"]
            break
    assert isinstance(descriptor, property)



def test_xs::declaration_is_not_abstract():
    assert not inspect.isabstract(xs::Declaration)


def test_xs::declaration_constructor_exists():
    assert callable(xs::Declaration.__init__)


def test_xs::declaration_constructor_args():
    sig = inspect.signature(xs::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_xs::program_is_not_abstract():
    assert not inspect.isabstract(xs::Program)


def test_xs::program_constructor_exists():
    assert callable(xs::Program.__init__)


def test_xs::program_constructor_args():
    sig = inspect.signature(xs::Program.__init__)
    params = list(sig.parameters.keys())



def test_xs::ruledeclaration_is_not_abstract():
    assert not inspect.isabstract(xs::RuleDeclaration)


def test_xs::ruledeclaration_constructor_exists():
    assert callable(xs::RuleDeclaration.__init__)


def test_xs::ruledeclaration_constructor_args():
    sig = inspect.signature(xs::RuleDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"
    assert "minInterval" in params, "Missing parameter 'minInterval'"
    assert "maxInterval" in params, "Missing parameter 'maxInterval'"
    assert "highFrequency" in params, "Missing parameter 'highFrequency'"
    assert "active" in params, "Missing parameter 'active'"
    assert "name" in params, "Missing parameter 'name'"
    assert "group" in params, "Missing parameter 'group'"
    assert "runImmediately" in params, "Missing parameter 'runImmediately'"

def test_xs::ruledeclaration_has_priority():
    assert hasattr(xs::RuleDeclaration, "priority")
    descriptor = None
    for klass in xs::RuleDeclaration.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_xs::ruledeclaration_has_minInterval():
    assert hasattr(xs::RuleDeclaration, "minInterval")
    descriptor = None
    for klass in xs::RuleDeclaration.__mro__:
        if "minInterval" in klass.__dict__:
            descriptor = klass.__dict__["minInterval"]
            break
    assert isinstance(descriptor, property)

def test_xs::ruledeclaration_has_maxInterval():
    assert hasattr(xs::RuleDeclaration, "maxInterval")
    descriptor = None
    for klass in xs::RuleDeclaration.__mro__:
        if "maxInterval" in klass.__dict__:
            descriptor = klass.__dict__["maxInterval"]
            break
    assert isinstance(descriptor, property)

def test_xs::ruledeclaration_has_highFrequency():
    assert hasattr(xs::RuleDeclaration, "highFrequency")
    descriptor = None
    for klass in xs::RuleDeclaration.__mro__:
        if "highFrequency" in klass.__dict__:
            descriptor = klass.__dict__["highFrequency"]
            break
    assert isinstance(descriptor, property)

def test_xs::ruledeclaration_has_active():
    assert hasattr(xs::RuleDeclaration, "active")
    descriptor = None
    for klass in xs::RuleDeclaration.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)

def test_xs::ruledeclaration_has_name():
    assert hasattr(xs::RuleDeclaration, "name")
    descriptor = None
    for klass in xs::RuleDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xs::ruledeclaration_has_group():
    assert hasattr(xs::RuleDeclaration, "group")
    descriptor = None
    for klass in xs::RuleDeclaration.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_xs::ruledeclaration_has_runImmediately():
    assert hasattr(xs::RuleDeclaration, "runImmediately")
    descriptor = None
    for klass in xs::RuleDeclaration.__mro__:
        if "runImmediately" in klass.__dict__:
            descriptor = klass.__dict__["runImmediately"]
            break
    assert isinstance(descriptor, property)



def test_xs::block_is_not_abstract():
    assert not inspect.isabstract(xs::Block)


def test_xs::block_constructor_exists():
    assert callable(xs::Block.__init__)


def test_xs::block_constructor_args():
    sig = inspect.signature(xs::Block.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_xs::vectortype_is_not_abstract():
    assert not inspect.isabstract(xs::VectorType)


def test_xs::vectortype_constructor_exists():
    assert callable(xs::VectorType.__init__)


def test_xs::vectortype_constructor_args():
    sig = inspect.signature(xs::VectorType.__init__)
    params = list(sig.parameters.keys())



def test_xs::stringtype_is_not_abstract():
    assert not inspect.isabstract(xs::StringType)


def test_xs::stringtype_constructor_exists():
    assert callable(xs::StringType.__init__)


def test_xs::stringtype_constructor_args():
    sig = inspect.signature(xs::StringType.__init__)
    params = list(sig.parameters.keys())



def test_xs::floattype_is_not_abstract():
    assert not inspect.isabstract(xs::FloatType)


def test_xs::floattype_constructor_exists():
    assert callable(xs::FloatType.__init__)


def test_xs::floattype_constructor_args():
    sig = inspect.signature(xs::FloatType.__init__)
    params = list(sig.parameters.keys())



def test_xs::voidtype_is_not_abstract():
    assert not inspect.isabstract(xs::VoidType)


def test_xs::voidtype_constructor_exists():
    assert callable(xs::VoidType.__init__)


def test_xs::voidtype_constructor_args():
    sig = inspect.signature(xs::VoidType.__init__)
    params = list(sig.parameters.keys())



def test_xs::booltype_is_not_abstract():
    assert not inspect.isabstract(xs::BoolType)


def test_xs::booltype_constructor_exists():
    assert callable(xs::BoolType.__init__)


def test_xs::booltype_constructor_args():
    sig = inspect.signature(xs::BoolType.__init__)
    params = list(sig.parameters.keys())



def test_xs::inttype_is_not_abstract():
    assert not inspect.isabstract(xs::IntType)


def test_xs::inttype_constructor_exists():
    assert callable(xs::IntType.__init__)


def test_xs::inttype_constructor_args():
    sig = inspect.signature(xs::IntType.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_xs::vectorliteral_is_not_abstract():
    assert not inspect.isabstract(xs::VectorLiteral)


def test_xs::vectorliteral_constructor_exists():
    assert callable(xs::VectorLiteral.__init__)


def test_xs::vectorliteral_constructor_args():
    sig = inspect.signature(xs::VectorLiteral.__init__)
    params = list(sig.parameters.keys())



def test_xs::literalbool_is_not_abstract():
    assert not inspect.isabstract(xs::LiteralBool)


def test_xs::literalbool_constructor_exists():
    assert callable(xs::LiteralBool.__init__)


def test_xs::literalbool_constructor_args():
    sig = inspect.signature(xs::LiteralBool.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_xs::literalbool_has_value():
    assert hasattr(xs::LiteralBool, "value")
    descriptor = None
    for klass in xs::LiteralBool.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_xs::literalfloat_is_not_abstract():
    assert not inspect.isabstract(xs::LiteralFloat)


def test_xs::literalfloat_constructor_exists():
    assert callable(xs::LiteralFloat.__init__)


def test_xs::literalfloat_constructor_args():
    sig = inspect.signature(xs::LiteralFloat.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_xs::literalfloat_has_value():
    assert hasattr(xs::LiteralFloat, "value")
    descriptor = None
    for klass in xs::LiteralFloat.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_xs::literalint_is_not_abstract():
    assert not inspect.isabstract(xs::LiteralInt)


def test_xs::literalint_constructor_exists():
    assert callable(xs::LiteralInt.__init__)


def test_xs::literalint_constructor_args():
    sig = inspect.signature(xs::LiteralInt.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_xs::literalint_has_value():
    assert hasattr(xs::LiteralInt, "value")
    descriptor = None
    for klass in xs::LiteralInt.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_xs::literalstring_is_not_abstract():
    assert not inspect.isabstract(xs::LiteralString)


def test_xs::literalstring_constructor_exists():
    assert callable(xs::LiteralString.__init__)


def test_xs::literalstring_constructor_args():
    sig = inspect.signature(xs::LiteralString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_xs::literalstring_has_value():
    assert hasattr(xs::LiteralString, "value")
    descriptor = None
    for klass in xs::LiteralString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_xs::breakstatement_is_not_abstract():
    assert not inspect.isabstract(xs::BreakStatement)


def test_xs::breakstatement_constructor_exists():
    assert callable(xs::BreakStatement.__init__)


def test_xs::breakstatement_constructor_args():
    sig = inspect.signature(xs::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_xs::continuestatement_is_not_abstract():
    assert not inspect.isabstract(xs::ContinueStatement)


def test_xs::continuestatement_constructor_exists():
    assert callable(xs::ContinueStatement.__init__)


def test_xs::continuestatement_constructor_args():
    sig = inspect.signature(xs::ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_xs::returnstatement_is_not_abstract():
    assert not inspect.isabstract(xs::ReturnStatement)


def test_xs::returnstatement_constructor_exists():
    assert callable(xs::ReturnStatement.__init__)


def test_xs::returnstatement_constructor_args():
    sig = inspect.signature(xs::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_xs::forstatement_is_not_abstract():
    assert not inspect.isabstract(xs::ForStatement)


def test_xs::forstatement_constructor_exists():
    assert callable(xs::ForStatement.__init__)


def test_xs::forstatement_constructor_args():
    sig = inspect.signature(xs::ForStatement.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_xs::forstatement_has_op():
    assert hasattr(xs::ForStatement, "op")
    descriptor = None
    for klass in xs::ForStatement.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_xs::whilestatement_is_not_abstract():
    assert not inspect.isabstract(xs::WhileStatement)


def test_xs::whilestatement_constructor_exists():
    assert callable(xs::WhileStatement.__init__)


def test_xs::whilestatement_constructor_args():
    sig = inspect.signature(xs::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_xs::ifelsestatement_is_not_abstract():
    assert not inspect.isabstract(xs::IfElseStatement)


def test_xs::ifelsestatement_constructor_exists():
    assert callable(xs::IfElseStatement.__init__)


def test_xs::ifelsestatement_constructor_args():
    sig = inspect.signature(xs::IfElseStatement.__init__)
    params = list(sig.parameters.keys())



def test_xs::postfixstatement_is_not_abstract():
    assert not inspect.isabstract(xs::PostfixStatement)


def test_xs::postfixstatement_constructor_exists():
    assert callable(xs::PostfixStatement.__init__)


def test_xs::postfixstatement_constructor_args():
    sig = inspect.signature(xs::PostfixStatement.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_xs::postfixstatement_has_op():
    assert hasattr(xs::PostfixStatement, "op")
    descriptor = None
    for klass in xs::PostfixStatement.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_xs::orexpression_is_not_abstract():
    assert not inspect.isabstract(xs::OrExpression)


def test_xs::orexpression_constructor_exists():
    assert callable(xs::OrExpression.__init__)


def test_xs::orexpression_constructor_args():
    sig = inspect.signature(xs::OrExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_xs::orexpression_has_op():
    assert hasattr(xs::OrExpression, "op")
    descriptor = None
    for klass in xs::OrExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_xs::factor_is_not_abstract():
    assert not inspect.isabstract(xs::Factor)


def test_xs::factor_constructor_exists():
    assert callable(xs::Factor.__init__)


def test_xs::factor_constructor_args():
    sig = inspect.signature(xs::Factor.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_xs::factor_has_op():
    assert hasattr(xs::Factor, "op")
    descriptor = None
    for klass in xs::Factor.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_xs::equalsexpression_is_not_abstract():
    assert not inspect.isabstract(xs::EqualsExpression)


def test_xs::equalsexpression_constructor_exists():
    assert callable(xs::EqualsExpression.__init__)


def test_xs::equalsexpression_constructor_args():
    sig = inspect.signature(xs::EqualsExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_xs::equalsexpression_has_op():
    assert hasattr(xs::EqualsExpression, "op")
    descriptor = None
    for klass in xs::EqualsExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_xs::call_is_not_abstract():
    assert not inspect.isabstract(xs::Call)


def test_xs::call_constructor_exists():
    assert callable(xs::Call.__init__)


def test_xs::call_constructor_args():
    sig = inspect.signature(xs::Call.__init__)
    params = list(sig.parameters.keys())



def test_xs::assign_is_not_abstract():
    assert not inspect.isabstract(xs::Assign)


def test_xs::assign_constructor_exists():
    assert callable(xs::Assign.__init__)


def test_xs::assign_constructor_args():
    sig = inspect.signature(xs::Assign.__init__)
    params = list(sig.parameters.keys())



def test_xs::term_is_not_abstract():
    assert not inspect.isabstract(xs::Term)


def test_xs::term_constructor_exists():
    assert callable(xs::Term.__init__)


def test_xs::term_constructor_args():
    sig = inspect.signature(xs::Term.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_xs::term_has_op():
    assert hasattr(xs::Term, "op")
    descriptor = None
    for klass in xs::Term.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_xs::andexpression_is_not_abstract():
    assert not inspect.isabstract(xs::AndExpression)


def test_xs::andexpression_constructor_exists():
    assert callable(xs::AndExpression.__init__)


def test_xs::andexpression_constructor_args():
    sig = inspect.signature(xs::AndExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_xs::andexpression_has_op():
    assert hasattr(xs::AndExpression, "op")
    descriptor = None
    for klass in xs::AndExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_xs::literal_is_not_abstract():
    assert not inspect.isabstract(xs::Literal)


def test_xs::literal_constructor_exists():
    assert callable(xs::Literal.__init__)


def test_xs::literal_constructor_args():
    sig = inspect.signature(xs::Literal.__init__)
    params = list(sig.parameters.keys())



def test_xs::comparisonexpression_is_not_abstract():
    assert not inspect.isabstract(xs::ComparisonExpression)


def test_xs::comparisonexpression_constructor_exists():
    assert callable(xs::ComparisonExpression.__init__)


def test_xs::comparisonexpression_constructor_args():
    sig = inspect.signature(xs::ComparisonExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_xs::comparisonexpression_has_op():
    assert hasattr(xs::ComparisonExpression, "op")
    descriptor = None
    for klass in xs::ComparisonExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_xs::var_is_not_abstract():
    assert not inspect.isabstract(xs::Var)


def test_xs::var_constructor_exists():
    assert callable(xs::Var.__init__)


def test_xs::var_constructor_args():
    sig = inspect.signature(xs::Var.__init__)
    params = list(sig.parameters.keys())



def test_xs::switchdefault_is_not_abstract():
    assert not inspect.isabstract(xs::SwitchDefault)


def test_xs::switchdefault_constructor_exists():
    assert callable(xs::SwitchDefault.__init__)


def test_xs::switchdefault_constructor_args():
    sig = inspect.signature(xs::SwitchDefault.__init__)
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
xs::SwitchCase_strategy = st.builds(
    xs::SwitchCase,
)
xs::Statement_strategy = st.builds(
    xs::Statement,
)
xs::Type_strategy = st.builds(
    xs::Type,
)
Statement_strategy = st.builds(
    Statement,
)
xs::SwitchStatement_strategy = st.builds(
    xs::SwitchStatement,
)
VarDeclaration_strategy = st.builds(
    VarDeclaration,
)
xs::ParameterDeclaration_strategy = st.builds(
    xs::ParameterDeclaration,
)
xs::ForVarDeclaration_strategy = st.builds(
    xs::ForVarDeclaration,
)
xs::LocalVarDeclaration_strategy = st.builds(
    xs::LocalVarDeclaration,
)
xs::Expression_strategy = st.builds(
    xs::Expression,
)
xs::VarDeclaration_strategy = st.builds(
    xs::VarDeclaration,
    name=
        safe_text
)
Declaration_strategy = st.builds(
    Declaration,
)
xs::GlobalVarDeclaration_strategy = st.builds(
    xs::GlobalVarDeclaration,
    extern=
        st.booleans(),
    const=
        st.booleans()
)
xs::FunctionDeclaration_strategy = st.builds(
    xs::FunctionDeclaration,
    mutable=
        st.booleans(),
    name=
        safe_text
)
xs::IncludeDeclaration_strategy = st.builds(
    xs::IncludeDeclaration,
    filePath=
        safe_text
)
xs::Declaration_strategy = st.builds(
    xs::Declaration,
)
xs::Program_strategy = st.builds(
    xs::Program,
)
xs::RuleDeclaration_strategy = st.builds(
    xs::RuleDeclaration,
    priority=
        st.integers(),
    minInterval=
        st.integers(),
    maxInterval=
        st.integers(),
    highFrequency=
        st.booleans(),
    active=
        st.booleans(),
    name=
        safe_text,
    group=
        safe_text,
    runImmediately=
        st.booleans()
)
xs::Block_strategy = st.builds(
    xs::Block,
)
Type_strategy = st.builds(
    Type,
)
xs::VectorType_strategy = st.builds(
    xs::VectorType,
)
xs::StringType_strategy = st.builds(
    xs::StringType,
)
xs::FloatType_strategy = st.builds(
    xs::FloatType,
)
xs::VoidType_strategy = st.builds(
    xs::VoidType,
)
xs::BoolType_strategy = st.builds(
    xs::BoolType,
)
xs::IntType_strategy = st.builds(
    xs::IntType,
)
Literal_strategy = st.builds(
    Literal,
)
xs::VectorLiteral_strategy = st.builds(
    xs::VectorLiteral,
)
xs::LiteralBool_strategy = st.builds(
    xs::LiteralBool,
    value=
        st.booleans()
)
xs::LiteralFloat_strategy = st.builds(
    xs::LiteralFloat,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
xs::LiteralInt_strategy = st.builds(
    xs::LiteralInt,
    value=
        st.integers()
)
xs::LiteralString_strategy = st.builds(
    xs::LiteralString,
    value=
        safe_text
)
xs::BreakStatement_strategy = st.builds(
    xs::BreakStatement,
)
xs::ContinueStatement_strategy = st.builds(
    xs::ContinueStatement,
)
xs::ReturnStatement_strategy = st.builds(
    xs::ReturnStatement,
)
xs::ForStatement_strategy = st.builds(
    xs::ForStatement,
    op=
        safe_text
)
xs::WhileStatement_strategy = st.builds(
    xs::WhileStatement,
)
xs::IfElseStatement_strategy = st.builds(
    xs::IfElseStatement,
)
xs::PostfixStatement_strategy = st.builds(
    xs::PostfixStatement,
    op=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
xs::OrExpression_strategy = st.builds(
    xs::OrExpression,
    op=
        safe_text
)
xs::Factor_strategy = st.builds(
    xs::Factor,
    op=
        safe_text
)
xs::EqualsExpression_strategy = st.builds(
    xs::EqualsExpression,
    op=
        safe_text
)
xs::Call_strategy = st.builds(
    xs::Call,
)
xs::Assign_strategy = st.builds(
    xs::Assign,
)
xs::Term_strategy = st.builds(
    xs::Term,
    op=
        safe_text
)
xs::AndExpression_strategy = st.builds(
    xs::AndExpression,
    op=
        safe_text
)
xs::Literal_strategy = st.builds(
    xs::Literal,
)
xs::ComparisonExpression_strategy = st.builds(
    xs::ComparisonExpression,
    op=
        safe_text
)
xs::Var_strategy = st.builds(
    xs::Var,
)
xs::SwitchDefault_strategy = st.builds(
    xs::SwitchDefault,
)

@given(instance=xs::SwitchCase_strategy)
@settings(max_examples=50)
def test_xs::switchcase_instantiation(instance):
    assert isinstance(instance, xs::SwitchCase)

@given(instance=xs::Statement_strategy)
@settings(max_examples=50)
def test_xs::statement_instantiation(instance):
    assert isinstance(instance, xs::Statement)

@given(instance=xs::Type_strategy)
@settings(max_examples=50)
def test_xs::type_instantiation(instance):
    assert isinstance(instance, xs::Type)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=xs::SwitchStatement_strategy)
@settings(max_examples=50)
def test_xs::switchstatement_instantiation(instance):
    assert isinstance(instance, xs::SwitchStatement)

@given(instance=VarDeclaration_strategy)
@settings(max_examples=50)
def test_vardeclaration_instantiation(instance):
    assert isinstance(instance, VarDeclaration)

@given(instance=xs::ParameterDeclaration_strategy)
@settings(max_examples=50)
def test_xs::parameterdeclaration_instantiation(instance):
    assert isinstance(instance, xs::ParameterDeclaration)

@given(instance=xs::ForVarDeclaration_strategy)
@settings(max_examples=50)
def test_xs::forvardeclaration_instantiation(instance):
    assert isinstance(instance, xs::ForVarDeclaration)

@given(instance=xs::LocalVarDeclaration_strategy)
@settings(max_examples=50)
def test_xs::localvardeclaration_instantiation(instance):
    assert isinstance(instance, xs::LocalVarDeclaration)

@given(instance=xs::Expression_strategy)
@settings(max_examples=50)
def test_xs::expression_instantiation(instance):
    assert isinstance(instance, xs::Expression)

@given(instance=xs::VarDeclaration_strategy)
@settings(max_examples=50)
def test_xs::vardeclaration_instantiation(instance):
    assert isinstance(instance, xs::VarDeclaration)

@given(instance=xs::VarDeclaration_strategy)
def test_xs::vardeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xs::VarDeclaration_strategy)
def test_xs::vardeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=xs::GlobalVarDeclaration_strategy)
@settings(max_examples=50)
def test_xs::globalvardeclaration_instantiation(instance):
    assert isinstance(instance, xs::GlobalVarDeclaration)

@given(instance=xs::GlobalVarDeclaration_strategy)
def test_xs::globalvardeclaration_extern_type(instance):
    assert isinstance(instance.extern, bool)


@given(instance=xs::GlobalVarDeclaration_strategy)
def test_xs::globalvardeclaration_extern_setter(instance):
    original = instance.extern
    instance.extern = original
    assert instance.extern == original

@given(instance=xs::GlobalVarDeclaration_strategy)
def test_xs::globalvardeclaration_const_type(instance):
    assert isinstance(instance.const, bool)


@given(instance=xs::GlobalVarDeclaration_strategy)
def test_xs::globalvardeclaration_const_setter(instance):
    original = instance.const
    instance.const = original
    assert instance.const == original

@given(instance=xs::FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_xs::functiondeclaration_instantiation(instance):
    assert isinstance(instance, xs::FunctionDeclaration)

@given(instance=xs::FunctionDeclaration_strategy)
def test_xs::functiondeclaration_mutable_type(instance):
    assert isinstance(instance.mutable, bool)


@given(instance=xs::FunctionDeclaration_strategy)
def test_xs::functiondeclaration_mutable_setter(instance):
    original = instance.mutable
    instance.mutable = original
    assert instance.mutable == original

@given(instance=xs::FunctionDeclaration_strategy)
def test_xs::functiondeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xs::FunctionDeclaration_strategy)
def test_xs::functiondeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xs::IncludeDeclaration_strategy)
@settings(max_examples=50)
def test_xs::includedeclaration_instantiation(instance):
    assert isinstance(instance, xs::IncludeDeclaration)

@given(instance=xs::IncludeDeclaration_strategy)
def test_xs::includedeclaration_filePath_type(instance):
    assert isinstance(instance.filePath, str)


@given(instance=xs::IncludeDeclaration_strategy)
def test_xs::includedeclaration_filePath_setter(instance):
    original = instance.filePath
    instance.filePath = original
    assert instance.filePath == original

@given(instance=xs::Declaration_strategy)
@settings(max_examples=50)
def test_xs::declaration_instantiation(instance):
    assert isinstance(instance, xs::Declaration)

@given(instance=xs::Program_strategy)
@settings(max_examples=50)
def test_xs::program_instantiation(instance):
    assert isinstance(instance, xs::Program)

@given(instance=xs::RuleDeclaration_strategy)
@settings(max_examples=50)
def test_xs::ruledeclaration_instantiation(instance):
    assert isinstance(instance, xs::RuleDeclaration)

@given(instance=xs::RuleDeclaration_strategy)
def test_xs::ruledeclaration_priority_type(instance):
    assert isinstance(instance.priority, int)


@given(instance=xs::RuleDeclaration_strategy)
def test_xs::ruledeclaration_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=xs::RuleDeclaration_strategy)
def test_xs::ruledeclaration_minInterval_type(instance):
    assert isinstance(instance.minInterval, int)


@given(instance=xs::RuleDeclaration_strategy)
def test_xs::ruledeclaration_minInterval_setter(instance):
    original = instance.minInterval
    instance.minInterval = original
    assert instance.minInterval == original

@given(instance=xs::RuleDeclaration_strategy)
def test_xs::ruledeclaration_maxInterval_type(instance):
    assert isinstance(instance.maxInterval, int)


@given(instance=xs::RuleDeclaration_strategy)
def test_xs::ruledeclaration_maxInterval_setter(instance):
    original = instance.maxInterval
    instance.maxInterval = original
    assert instance.maxInterval == original

@given(instance=xs::RuleDeclaration_strategy)
def test_xs::ruledeclaration_highFrequency_type(instance):
    assert isinstance(instance.highFrequency, bool)


@given(instance=xs::RuleDeclaration_strategy)
def test_xs::ruledeclaration_highFrequency_setter(instance):
    original = instance.highFrequency
    instance.highFrequency = original
    assert instance.highFrequency == original

@given(instance=xs::RuleDeclaration_strategy)
def test_xs::ruledeclaration_active_type(instance):
    assert isinstance(instance.active, bool)


@given(instance=xs::RuleDeclaration_strategy)
def test_xs::ruledeclaration_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original

@given(instance=xs::RuleDeclaration_strategy)
def test_xs::ruledeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xs::RuleDeclaration_strategy)
def test_xs::ruledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xs::RuleDeclaration_strategy)
def test_xs::ruledeclaration_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=xs::RuleDeclaration_strategy)
def test_xs::ruledeclaration_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=xs::RuleDeclaration_strategy)
def test_xs::ruledeclaration_runImmediately_type(instance):
    assert isinstance(instance.runImmediately, bool)


@given(instance=xs::RuleDeclaration_strategy)
def test_xs::ruledeclaration_runImmediately_setter(instance):
    original = instance.runImmediately
    instance.runImmediately = original
    assert instance.runImmediately == original

@given(instance=xs::Block_strategy)
@settings(max_examples=50)
def test_xs::block_instantiation(instance):
    assert isinstance(instance, xs::Block)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=xs::VectorType_strategy)
@settings(max_examples=50)
def test_xs::vectortype_instantiation(instance):
    assert isinstance(instance, xs::VectorType)

@given(instance=xs::StringType_strategy)
@settings(max_examples=50)
def test_xs::stringtype_instantiation(instance):
    assert isinstance(instance, xs::StringType)

@given(instance=xs::FloatType_strategy)
@settings(max_examples=50)
def test_xs::floattype_instantiation(instance):
    assert isinstance(instance, xs::FloatType)

@given(instance=xs::VoidType_strategy)
@settings(max_examples=50)
def test_xs::voidtype_instantiation(instance):
    assert isinstance(instance, xs::VoidType)

@given(instance=xs::BoolType_strategy)
@settings(max_examples=50)
def test_xs::booltype_instantiation(instance):
    assert isinstance(instance, xs::BoolType)

@given(instance=xs::IntType_strategy)
@settings(max_examples=50)
def test_xs::inttype_instantiation(instance):
    assert isinstance(instance, xs::IntType)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=xs::VectorLiteral_strategy)
@settings(max_examples=50)
def test_xs::vectorliteral_instantiation(instance):
    assert isinstance(instance, xs::VectorLiteral)

@given(instance=xs::LiteralBool_strategy)
@settings(max_examples=50)
def test_xs::literalbool_instantiation(instance):
    assert isinstance(instance, xs::LiteralBool)

@given(instance=xs::LiteralBool_strategy)
def test_xs::literalbool_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=xs::LiteralBool_strategy)
def test_xs::literalbool_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=xs::LiteralFloat_strategy)
@settings(max_examples=50)
def test_xs::literalfloat_instantiation(instance):
    assert isinstance(instance, xs::LiteralFloat)

@given(instance=xs::LiteralFloat_strategy)
def test_xs::literalfloat_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=xs::LiteralFloat_strategy)
def test_xs::literalfloat_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=xs::LiteralInt_strategy)
@settings(max_examples=50)
def test_xs::literalint_instantiation(instance):
    assert isinstance(instance, xs::LiteralInt)

@given(instance=xs::LiteralInt_strategy)
def test_xs::literalint_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=xs::LiteralInt_strategy)
def test_xs::literalint_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=xs::LiteralString_strategy)
@settings(max_examples=50)
def test_xs::literalstring_instantiation(instance):
    assert isinstance(instance, xs::LiteralString)

@given(instance=xs::LiteralString_strategy)
def test_xs::literalstring_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=xs::LiteralString_strategy)
def test_xs::literalstring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=xs::BreakStatement_strategy)
@settings(max_examples=50)
def test_xs::breakstatement_instantiation(instance):
    assert isinstance(instance, xs::BreakStatement)

@given(instance=xs::ContinueStatement_strategy)
@settings(max_examples=50)
def test_xs::continuestatement_instantiation(instance):
    assert isinstance(instance, xs::ContinueStatement)

@given(instance=xs::ReturnStatement_strategy)
@settings(max_examples=50)
def test_xs::returnstatement_instantiation(instance):
    assert isinstance(instance, xs::ReturnStatement)

@given(instance=xs::ForStatement_strategy)
@settings(max_examples=50)
def test_xs::forstatement_instantiation(instance):
    assert isinstance(instance, xs::ForStatement)

@given(instance=xs::ForStatement_strategy)
def test_xs::forstatement_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=xs::ForStatement_strategy)
def test_xs::forstatement_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=xs::WhileStatement_strategy)
@settings(max_examples=50)
def test_xs::whilestatement_instantiation(instance):
    assert isinstance(instance, xs::WhileStatement)

@given(instance=xs::IfElseStatement_strategy)
@settings(max_examples=50)
def test_xs::ifelsestatement_instantiation(instance):
    assert isinstance(instance, xs::IfElseStatement)

@given(instance=xs::PostfixStatement_strategy)
@settings(max_examples=50)
def test_xs::postfixstatement_instantiation(instance):
    assert isinstance(instance, xs::PostfixStatement)

@given(instance=xs::PostfixStatement_strategy)
def test_xs::postfixstatement_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=xs::PostfixStatement_strategy)
def test_xs::postfixstatement_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=xs::OrExpression_strategy)
@settings(max_examples=50)
def test_xs::orexpression_instantiation(instance):
    assert isinstance(instance, xs::OrExpression)

@given(instance=xs::OrExpression_strategy)
def test_xs::orexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=xs::OrExpression_strategy)
def test_xs::orexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=xs::Factor_strategy)
@settings(max_examples=50)
def test_xs::factor_instantiation(instance):
    assert isinstance(instance, xs::Factor)

@given(instance=xs::Factor_strategy)
def test_xs::factor_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=xs::Factor_strategy)
def test_xs::factor_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=xs::EqualsExpression_strategy)
@settings(max_examples=50)
def test_xs::equalsexpression_instantiation(instance):
    assert isinstance(instance, xs::EqualsExpression)

@given(instance=xs::EqualsExpression_strategy)
def test_xs::equalsexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=xs::EqualsExpression_strategy)
def test_xs::equalsexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=xs::Call_strategy)
@settings(max_examples=50)
def test_xs::call_instantiation(instance):
    assert isinstance(instance, xs::Call)

@given(instance=xs::Assign_strategy)
@settings(max_examples=50)
def test_xs::assign_instantiation(instance):
    assert isinstance(instance, xs::Assign)

@given(instance=xs::Term_strategy)
@settings(max_examples=50)
def test_xs::term_instantiation(instance):
    assert isinstance(instance, xs::Term)

@given(instance=xs::Term_strategy)
def test_xs::term_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=xs::Term_strategy)
def test_xs::term_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=xs::AndExpression_strategy)
@settings(max_examples=50)
def test_xs::andexpression_instantiation(instance):
    assert isinstance(instance, xs::AndExpression)

@given(instance=xs::AndExpression_strategy)
def test_xs::andexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=xs::AndExpression_strategy)
def test_xs::andexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=xs::Literal_strategy)
@settings(max_examples=50)
def test_xs::literal_instantiation(instance):
    assert isinstance(instance, xs::Literal)

@given(instance=xs::ComparisonExpression_strategy)
@settings(max_examples=50)
def test_xs::comparisonexpression_instantiation(instance):
    assert isinstance(instance, xs::ComparisonExpression)

@given(instance=xs::ComparisonExpression_strategy)
def test_xs::comparisonexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=xs::ComparisonExpression_strategy)
def test_xs::comparisonexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=xs::Var_strategy)
@settings(max_examples=50)
def test_xs::var_instantiation(instance):
    assert isinstance(instance, xs::Var)

@given(instance=xs::SwitchDefault_strategy)
@settings(max_examples=50)
def test_xs::switchdefault_instantiation(instance):
    assert isinstance(instance, xs::SwitchDefault)
