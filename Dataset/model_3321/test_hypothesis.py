import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    myDsl::Creating::Expression,
    myDsl::Float::Literal,
    myDsl::Ampersand::Rule,
    myDsl::Arg::List,
    myDsl::Literal::Expression,
    myDsl::Cast::Expression,
    myDsl::Bit::Expression::NR,
    myDsl::Logical::Expression::NR,
    myDsl::Expression::aux,
    myDsl::Numeric::Expression::NR,
    myDsl::Try::statement,
    myDsl::Switch::statement,
    myDsl::For::Statement,
    myDsl::While::Statement,
    myDsl::Do::Statement,
    myDsl::If::statement,
    myDsl::Statement,
    myDsl::Type::specifier,
    myDsl::Expression,
    myDsl::Array::initializer,
    myDsl::Variable::initializer,
    myDsl::Variable::declarator,
    myDsl::Parameter,
    myDsl::Package::statement,
    myDsl::Statement::block,
    myDsl::Parameter::list,
    myDsl::Type,
    myDsl::Static::initializer,
    myDsl::Method::declaration,
    myDsl::Constructor::declaration,
    myDsl::Variable::declaration,
    myDsl::Field::declaration,
    myDsl::Interface::declaration,
    myDsl::Class::declaration,
    myDsl::Type::declaration,
    myDsl::Import::statement,
    myDsl::Compilation::unit,
    myDsl::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl::creating::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::Creating::Expression)


def test_mydsl::creating::expression_constructor_exists():
    assert callable(myDsl::Creating::Expression.__init__)


def test_mydsl::creating::expression_constructor_args():
    sig = inspect.signature(myDsl::Creating::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "className" in params, "Missing parameter 'className'"

def test_mydsl::creating::expression_has_className():
    assert hasattr(myDsl::Creating::Expression, "className")
    descriptor = None
    for klass in myDsl::Creating::Expression.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::float::literal_is_not_abstract():
    assert not inspect.isabstract(myDsl::Float::Literal)


def test_mydsl::float::literal_constructor_exists():
    assert callable(myDsl::Float::Literal.__init__)


def test_mydsl::float::literal_constructor_args():
    sig = inspect.signature(myDsl::Float::Literal.__init__)
    params = list(sig.parameters.keys())
    assert "floatTypeSufix" in params, "Missing parameter 'floatTypeSufix'"
    assert "exp" in params, "Missing parameter 'exp'"
    assert "decimalDigits2" in params, "Missing parameter 'decimalDigits2'"
    assert "decimalDigits1" in params, "Missing parameter 'decimalDigits1'"

def test_mydsl::float::literal_has_floatTypeSufix():
    assert hasattr(myDsl::Float::Literal, "floatTypeSufix")
    descriptor = None
    for klass in myDsl::Float::Literal.__mro__:
        if "floatTypeSufix" in klass.__dict__:
            descriptor = klass.__dict__["floatTypeSufix"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::float::literal_has_exp():
    assert hasattr(myDsl::Float::Literal, "exp")
    descriptor = None
    for klass in myDsl::Float::Literal.__mro__:
        if "exp" in klass.__dict__:
            descriptor = klass.__dict__["exp"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::float::literal_has_decimalDigits2():
    assert hasattr(myDsl::Float::Literal, "decimalDigits2")
    descriptor = None
    for klass in myDsl::Float::Literal.__mro__:
        if "decimalDigits2" in klass.__dict__:
            descriptor = klass.__dict__["decimalDigits2"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::float::literal_has_decimalDigits1():
    assert hasattr(myDsl::Float::Literal, "decimalDigits1")
    descriptor = None
    for klass in myDsl::Float::Literal.__mro__:
        if "decimalDigits1" in klass.__dict__:
            descriptor = klass.__dict__["decimalDigits1"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::ampersand::rule_is_not_abstract():
    assert not inspect.isabstract(myDsl::Ampersand::Rule)


def test_mydsl::ampersand::rule_constructor_exists():
    assert callable(myDsl::Ampersand::Rule.__init__)


def test_mydsl::ampersand::rule_constructor_args():
    sig = inspect.signature(myDsl::Ampersand::Rule.__init__)
    params = list(sig.parameters.keys())
    assert "a2" in params, "Missing parameter 'a2'"
    assert "a1" in params, "Missing parameter 'a1'"

def test_mydsl::ampersand::rule_has_a2():
    assert hasattr(myDsl::Ampersand::Rule, "a2")
    descriptor = None
    for klass in myDsl::Ampersand::Rule.__mro__:
        if "a2" in klass.__dict__:
            descriptor = klass.__dict__["a2"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::ampersand::rule_has_a1():
    assert hasattr(myDsl::Ampersand::Rule, "a1")
    descriptor = None
    for klass in myDsl::Ampersand::Rule.__mro__:
        if "a1" in klass.__dict__:
            descriptor = klass.__dict__["a1"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::arg::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::Arg::List)


def test_mydsl::arg::list_constructor_exists():
    assert callable(myDsl::Arg::List.__init__)


def test_mydsl::arg::list_constructor_args():
    sig = inspect.signature(myDsl::Arg::List.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::literal::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::Literal::Expression)


def test_mydsl::literal::expression_constructor_exists():
    assert callable(myDsl::Literal::Expression.__init__)


def test_mydsl::literal::expression_constructor_args():
    sig = inspect.signature(myDsl::Literal::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"
    assert "charLit" in params, "Missing parameter 'charLit'"
    assert "exp1" in params, "Missing parameter 'exp1'"
    assert "exp" in params, "Missing parameter 'exp'"

def test_mydsl::literal::expression_has_string():
    assert hasattr(myDsl::Literal::Expression, "string")
    descriptor = None
    for klass in myDsl::Literal::Expression.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::literal::expression_has_charLit():
    assert hasattr(myDsl::Literal::Expression, "charLit")
    descriptor = None
    for klass in myDsl::Literal::Expression.__mro__:
        if "charLit" in klass.__dict__:
            descriptor = klass.__dict__["charLit"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::literal::expression_has_exp1():
    assert hasattr(myDsl::Literal::Expression, "exp1")
    descriptor = None
    for klass in myDsl::Literal::Expression.__mro__:
        if "exp1" in klass.__dict__:
            descriptor = klass.__dict__["exp1"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::literal::expression_has_exp():
    assert hasattr(myDsl::Literal::Expression, "exp")
    descriptor = None
    for klass in myDsl::Literal::Expression.__mro__:
        if "exp" in klass.__dict__:
            descriptor = klass.__dict__["exp"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::cast::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::Cast::Expression)


def test_mydsl::cast::expression_constructor_exists():
    assert callable(myDsl::Cast::Expression.__init__)


def test_mydsl::cast::expression_constructor_args():
    sig = inspect.signature(myDsl::Cast::Expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::bit::expression::nr_is_not_abstract():
    assert not inspect.isabstract(myDsl::Bit::Expression::NR)


def test_mydsl::bit::expression::nr_constructor_exists():
    assert callable(myDsl::Bit::Expression::NR.__init__)


def test_mydsl::bit::expression::nr_constructor_args():
    sig = inspect.signature(myDsl::Bit::Expression::NR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::logical::expression::nr_is_not_abstract():
    assert not inspect.isabstract(myDsl::Logical::Expression::NR)


def test_mydsl::logical::expression::nr_constructor_exists():
    assert callable(myDsl::Logical::Expression::NR.__init__)


def test_mydsl::logical::expression::nr_constructor_args():
    sig = inspect.signature(myDsl::Logical::Expression::NR.__init__)
    params = list(sig.parameters.keys())
    assert "false" in params, "Missing parameter 'false'"
    assert "true" in params, "Missing parameter 'true'"
    assert "exclamation" in params, "Missing parameter 'exclamation'"

def test_mydsl::logical::expression::nr_has_false():
    assert hasattr(myDsl::Logical::Expression::NR, "false")
    descriptor = None
    for klass in myDsl::Logical::Expression::NR.__mro__:
        if "false" in klass.__dict__:
            descriptor = klass.__dict__["false"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::logical::expression::nr_has_true():
    assert hasattr(myDsl::Logical::Expression::NR, "true")
    descriptor = None
    for klass in myDsl::Logical::Expression::NR.__mro__:
        if "true" in klass.__dict__:
            descriptor = klass.__dict__["true"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::logical::expression::nr_has_exclamation():
    assert hasattr(myDsl::Logical::Expression::NR, "exclamation")
    descriptor = None
    for klass in myDsl::Logical::Expression::NR.__mro__:
        if "exclamation" in klass.__dict__:
            descriptor = klass.__dict__["exclamation"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::expression::aux_is_not_abstract():
    assert not inspect.isabstract(myDsl::Expression::aux)


def test_mydsl::expression::aux_constructor_exists():
    assert callable(myDsl::Expression::aux.__init__)


def test_mydsl::expression::aux_constructor_args():
    sig = inspect.signature(myDsl::Expression::aux.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "sgin" in params, "Missing parameter 'sgin'"
    assert "bitSign" in params, "Missing parameter 'bitSign'"
    assert "logicalSign" in params, "Missing parameter 'logicalSign'"
    assert "stringSign" in params, "Missing parameter 'stringSign'"
    assert "logicOp" in params, "Missing parameter 'logicOp'"
    assert "testingSign" in params, "Missing parameter 'testingSign'"
    assert "numericSign" in params, "Missing parameter 'numericSign'"

def test_mydsl::expression::aux_has_name():
    assert hasattr(myDsl::Expression::aux, "name")
    descriptor = None
    for klass in myDsl::Expression::aux.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::expression::aux_has_sgin():
    assert hasattr(myDsl::Expression::aux, "sgin")
    descriptor = None
    for klass in myDsl::Expression::aux.__mro__:
        if "sgin" in klass.__dict__:
            descriptor = klass.__dict__["sgin"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::expression::aux_has_bitSign():
    assert hasattr(myDsl::Expression::aux, "bitSign")
    descriptor = None
    for klass in myDsl::Expression::aux.__mro__:
        if "bitSign" in klass.__dict__:
            descriptor = klass.__dict__["bitSign"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::expression::aux_has_logicalSign():
    assert hasattr(myDsl::Expression::aux, "logicalSign")
    descriptor = None
    for klass in myDsl::Expression::aux.__mro__:
        if "logicalSign" in klass.__dict__:
            descriptor = klass.__dict__["logicalSign"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::expression::aux_has_stringSign():
    assert hasattr(myDsl::Expression::aux, "stringSign")
    descriptor = None
    for klass in myDsl::Expression::aux.__mro__:
        if "stringSign" in klass.__dict__:
            descriptor = klass.__dict__["stringSign"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::expression::aux_has_logicOp():
    assert hasattr(myDsl::Expression::aux, "logicOp")
    descriptor = None
    for klass in myDsl::Expression::aux.__mro__:
        if "logicOp" in klass.__dict__:
            descriptor = klass.__dict__["logicOp"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::expression::aux_has_testingSign():
    assert hasattr(myDsl::Expression::aux, "testingSign")
    descriptor = None
    for klass in myDsl::Expression::aux.__mro__:
        if "testingSign" in klass.__dict__:
            descriptor = klass.__dict__["testingSign"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::expression::aux_has_numericSign():
    assert hasattr(myDsl::Expression::aux, "numericSign")
    descriptor = None
    for klass in myDsl::Expression::aux.__mro__:
        if "numericSign" in klass.__dict__:
            descriptor = klass.__dict__["numericSign"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::numeric::expression::nr_is_not_abstract():
    assert not inspect.isabstract(myDsl::Numeric::Expression::NR)


def test_mydsl::numeric::expression::nr_constructor_exists():
    assert callable(myDsl::Numeric::Expression::NR.__init__)


def test_mydsl::numeric::expression::nr_constructor_args():
    sig = inspect.signature(myDsl::Numeric::Expression::NR.__init__)
    params = list(sig.parameters.keys())
    assert "sinal_numeric" in params, "Missing parameter 'sinal_numeric'"

def test_mydsl::numeric::expression::nr_has_sinal_numeric():
    assert hasattr(myDsl::Numeric::Expression::NR, "sinal_numeric")
    descriptor = None
    for klass in myDsl::Numeric::Expression::NR.__mro__:
        if "sinal_numeric" in klass.__dict__:
            descriptor = klass.__dict__["sinal_numeric"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::try::statement_is_not_abstract():
    assert not inspect.isabstract(myDsl::Try::statement)


def test_mydsl::try::statement_constructor_exists():
    assert callable(myDsl::Try::statement.__init__)


def test_mydsl::try::statement_constructor_args():
    sig = inspect.signature(myDsl::Try::statement.__init__)
    params = list(sig.parameters.keys())
    assert "lParen" in params, "Missing parameter 'lParen'"
    assert "rparent" in params, "Missing parameter 'rparent'"

def test_mydsl::try::statement_has_lParen():
    assert hasattr(myDsl::Try::statement, "lParen")
    descriptor = None
    for klass in myDsl::Try::statement.__mro__:
        if "lParen" in klass.__dict__:
            descriptor = klass.__dict__["lParen"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::try::statement_has_rparent():
    assert hasattr(myDsl::Try::statement, "rparent")
    descriptor = None
    for klass in myDsl::Try::statement.__mro__:
        if "rparent" in klass.__dict__:
            descriptor = klass.__dict__["rparent"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::switch::statement_is_not_abstract():
    assert not inspect.isabstract(myDsl::Switch::statement)


def test_mydsl::switch::statement_constructor_exists():
    assert callable(myDsl::Switch::statement.__init__)


def test_mydsl::switch::statement_constructor_args():
    sig = inspect.signature(myDsl::Switch::statement.__init__)
    params = list(sig.parameters.keys())
    assert "lParen" in params, "Missing parameter 'lParen'"
    assert "rparent" in params, "Missing parameter 'rparent'"

def test_mydsl::switch::statement_has_lParen():
    assert hasattr(myDsl::Switch::statement, "lParen")
    descriptor = None
    for klass in myDsl::Switch::statement.__mro__:
        if "lParen" in klass.__dict__:
            descriptor = klass.__dict__["lParen"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::switch::statement_has_rparent():
    assert hasattr(myDsl::Switch::statement, "rparent")
    descriptor = None
    for klass in myDsl::Switch::statement.__mro__:
        if "rparent" in klass.__dict__:
            descriptor = klass.__dict__["rparent"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::for::statement_is_not_abstract():
    assert not inspect.isabstract(myDsl::For::Statement)


def test_mydsl::for::statement_constructor_exists():
    assert callable(myDsl::For::Statement.__init__)


def test_mydsl::for::statement_constructor_args():
    sig = inspect.signature(myDsl::For::Statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::while::statement_is_not_abstract():
    assert not inspect.isabstract(myDsl::While::Statement)


def test_mydsl::while::statement_constructor_exists():
    assert callable(myDsl::While::Statement.__init__)


def test_mydsl::while::statement_constructor_args():
    sig = inspect.signature(myDsl::While::Statement.__init__)
    params = list(sig.parameters.keys())
    assert "rparent" in params, "Missing parameter 'rparent'"

def test_mydsl::while::statement_has_rparent():
    assert hasattr(myDsl::While::Statement, "rparent")
    descriptor = None
    for klass in myDsl::While::Statement.__mro__:
        if "rparent" in klass.__dict__:
            descriptor = klass.__dict__["rparent"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::do::statement_is_not_abstract():
    assert not inspect.isabstract(myDsl::Do::Statement)


def test_mydsl::do::statement_constructor_exists():
    assert callable(myDsl::Do::Statement.__init__)


def test_mydsl::do::statement_constructor_args():
    sig = inspect.signature(myDsl::Do::Statement.__init__)
    params = list(sig.parameters.keys())
    assert "lparent" in params, "Missing parameter 'lparent'"
    assert "rparent" in params, "Missing parameter 'rparent'"

def test_mydsl::do::statement_has_lparent():
    assert hasattr(myDsl::Do::Statement, "lparent")
    descriptor = None
    for klass in myDsl::Do::Statement.__mro__:
        if "lparent" in klass.__dict__:
            descriptor = klass.__dict__["lparent"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::do::statement_has_rparent():
    assert hasattr(myDsl::Do::Statement, "rparent")
    descriptor = None
    for klass in myDsl::Do::Statement.__mro__:
        if "rparent" in klass.__dict__:
            descriptor = klass.__dict__["rparent"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::if::statement_is_not_abstract():
    assert not inspect.isabstract(myDsl::If::statement)


def test_mydsl::if::statement_constructor_exists():
    assert callable(myDsl::If::statement.__init__)


def test_mydsl::if::statement_constructor_args():
    sig = inspect.signature(myDsl::If::statement.__init__)
    params = list(sig.parameters.keys())
    assert "rparent" in params, "Missing parameter 'rparent'"
    assert "lparen" in params, "Missing parameter 'lparen'"

def test_mydsl::if::statement_has_rparent():
    assert hasattr(myDsl::If::statement, "rparent")
    descriptor = None
    for klass in myDsl::If::statement.__mro__:
        if "rparent" in klass.__dict__:
            descriptor = klass.__dict__["rparent"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::if::statement_has_lparen():
    assert hasattr(myDsl::If::statement, "lparen")
    descriptor = None
    for klass in myDsl::If::statement.__mro__:
        if "lparen" in klass.__dict__:
            descriptor = klass.__dict__["lparen"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::statement_is_not_abstract():
    assert not inspect.isabstract(myDsl::Statement)


def test_mydsl::statement_constructor_exists():
    assert callable(myDsl::Statement.__init__)


def test_mydsl::statement_constructor_args():
    sig = inspect.signature(myDsl::Statement.__init__)
    params = list(sig.parameters.keys())
    assert "g" in params, "Missing parameter 'g'"
    assert "name" in params, "Missing parameter 'name'"
    assert "rparent" in params, "Missing parameter 'rparent'"
    assert "ret" in params, "Missing parameter 'ret'"
    assert "nameStatement" in params, "Missing parameter 'nameStatement'"

def test_mydsl::statement_has_g():
    assert hasattr(myDsl::Statement, "g")
    descriptor = None
    for klass in myDsl::Statement.__mro__:
        if "g" in klass.__dict__:
            descriptor = klass.__dict__["g"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::statement_has_name():
    assert hasattr(myDsl::Statement, "name")
    descriptor = None
    for klass in myDsl::Statement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::statement_has_rparent():
    assert hasattr(myDsl::Statement, "rparent")
    descriptor = None
    for klass in myDsl::Statement.__mro__:
        if "rparent" in klass.__dict__:
            descriptor = klass.__dict__["rparent"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::statement_has_ret():
    assert hasattr(myDsl::Statement, "ret")
    descriptor = None
    for klass in myDsl::Statement.__mro__:
        if "ret" in klass.__dict__:
            descriptor = klass.__dict__["ret"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::statement_has_nameStatement():
    assert hasattr(myDsl::Statement, "nameStatement")
    descriptor = None
    for klass in myDsl::Statement.__mro__:
        if "nameStatement" in klass.__dict__:
            descriptor = klass.__dict__["nameStatement"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::type::specifier_is_not_abstract():
    assert not inspect.isabstract(myDsl::Type::specifier)


def test_mydsl::type::specifier_constructor_exists():
    assert callable(myDsl::Type::specifier.__init__)


def test_mydsl::type::specifier_constructor_args():
    sig = inspect.signature(myDsl::Type::specifier.__init__)
    params = list(sig.parameters.keys())
    assert "primitiveType" in params, "Missing parameter 'primitiveType'"
    assert "className" in params, "Missing parameter 'className'"

def test_mydsl::type::specifier_has_primitiveType():
    assert hasattr(myDsl::Type::specifier, "primitiveType")
    descriptor = None
    for klass in myDsl::Type::specifier.__mro__:
        if "primitiveType" in klass.__dict__:
            descriptor = klass.__dict__["primitiveType"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::type::specifier_has_className():
    assert hasattr(myDsl::Type::specifier, "className")
    descriptor = None
    for klass in myDsl::Type::specifier.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::Expression)


def test_mydsl::expression_constructor_exists():
    assert callable(myDsl::Expression.__init__)


def test_mydsl::expression_constructor_args():
    sig = inspect.signature(myDsl::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "null" in params, "Missing parameter 'null'"
    assert "name" in params, "Missing parameter 'name'"
    assert "this" in params, "Missing parameter 'this'"
    assert "super" in params, "Missing parameter 'super'"

def test_mydsl::expression_has_null():
    assert hasattr(myDsl::Expression, "null")
    descriptor = None
    for klass in myDsl::Expression.__mro__:
        if "null" in klass.__dict__:
            descriptor = klass.__dict__["null"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::expression_has_name():
    assert hasattr(myDsl::Expression, "name")
    descriptor = None
    for klass in myDsl::Expression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::expression_has_this():
    assert hasattr(myDsl::Expression, "this")
    descriptor = None
    for klass in myDsl::Expression.__mro__:
        if "this" in klass.__dict__:
            descriptor = klass.__dict__["this"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::expression_has_super():
    assert hasattr(myDsl::Expression, "super")
    descriptor = None
    for klass in myDsl::Expression.__mro__:
        if "super" in klass.__dict__:
            descriptor = klass.__dict__["super"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::array::initializer_is_not_abstract():
    assert not inspect.isabstract(myDsl::Array::initializer)


def test_mydsl::array::initializer_constructor_exists():
    assert callable(myDsl::Array::initializer.__init__)


def test_mydsl::array::initializer_constructor_args():
    sig = inspect.signature(myDsl::Array::initializer.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::variable::initializer_is_not_abstract():
    assert not inspect.isabstract(myDsl::Variable::initializer)


def test_mydsl::variable::initializer_constructor_exists():
    assert callable(myDsl::Variable::initializer.__init__)


def test_mydsl::variable::initializer_constructor_args():
    sig = inspect.signature(myDsl::Variable::initializer.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::variable::declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl::Variable::declarator)


def test_mydsl::variable::declarator_constructor_exists():
    assert callable(myDsl::Variable::declarator.__init__)


def test_mydsl::variable::declarator_constructor_args():
    sig = inspect.signature(myDsl::Variable::declarator.__init__)
    params = list(sig.parameters.keys())
    assert "nameVariable" in params, "Missing parameter 'nameVariable'"
    assert "lenVector" in params, "Missing parameter 'lenVector'"

def test_mydsl::variable::declarator_has_nameVariable():
    assert hasattr(myDsl::Variable::declarator, "nameVariable")
    descriptor = None
    for klass in myDsl::Variable::declarator.__mro__:
        if "nameVariable" in klass.__dict__:
            descriptor = klass.__dict__["nameVariable"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::variable::declarator_has_lenVector():
    assert hasattr(myDsl::Variable::declarator, "lenVector")
    descriptor = None
    for klass in myDsl::Variable::declarator.__mro__:
        if "lenVector" in klass.__dict__:
            descriptor = klass.__dict__["lenVector"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::parameter_is_not_abstract():
    assert not inspect.isabstract(myDsl::Parameter)


def test_mydsl::parameter_constructor_exists():
    assert callable(myDsl::Parameter.__init__)


def test_mydsl::parameter_constructor_args():
    sig = inspect.signature(myDsl::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "parameterName" in params, "Missing parameter 'parameterName'"

def test_mydsl::parameter_has_parameterName():
    assert hasattr(myDsl::Parameter, "parameterName")
    descriptor = None
    for klass in myDsl::Parameter.__mro__:
        if "parameterName" in klass.__dict__:
            descriptor = klass.__dict__["parameterName"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::package::statement_is_not_abstract():
    assert not inspect.isabstract(myDsl::Package::statement)


def test_mydsl::package::statement_constructor_exists():
    assert callable(myDsl::Package::statement.__init__)


def test_mydsl::package::statement_constructor_args():
    sig = inspect.signature(myDsl::Package::statement.__init__)
    params = list(sig.parameters.keys())
    assert "pacName" in params, "Missing parameter 'pacName'"

def test_mydsl::package::statement_has_pacName():
    assert hasattr(myDsl::Package::statement, "pacName")
    descriptor = None
    for klass in myDsl::Package::statement.__mro__:
        if "pacName" in klass.__dict__:
            descriptor = klass.__dict__["pacName"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::statement::block_is_not_abstract():
    assert not inspect.isabstract(myDsl::Statement::block)


def test_mydsl::statement::block_constructor_exists():
    assert callable(myDsl::Statement::block.__init__)


def test_mydsl::statement::block_constructor_args():
    sig = inspect.signature(myDsl::Statement::block.__init__)
    params = list(sig.parameters.keys())
    assert "lCurly" in params, "Missing parameter 'lCurly'"
    assert "rCurly" in params, "Missing parameter 'rCurly'"

def test_mydsl::statement::block_has_lCurly():
    assert hasattr(myDsl::Statement::block, "lCurly")
    descriptor = None
    for klass in myDsl::Statement::block.__mro__:
        if "lCurly" in klass.__dict__:
            descriptor = klass.__dict__["lCurly"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::statement::block_has_rCurly():
    assert hasattr(myDsl::Statement::block, "rCurly")
    descriptor = None
    for klass in myDsl::Statement::block.__mro__:
        if "rCurly" in klass.__dict__:
            descriptor = klass.__dict__["rCurly"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::parameter::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::Parameter::list)


def test_mydsl::parameter::list_constructor_exists():
    assert callable(myDsl::Parameter::list.__init__)


def test_mydsl::parameter::list_constructor_args():
    sig = inspect.signature(myDsl::Parameter::list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::type_is_not_abstract():
    assert not inspect.isabstract(myDsl::Type)


def test_mydsl::type_constructor_exists():
    assert callable(myDsl::Type.__init__)


def test_mydsl::type_constructor_args():
    sig = inspect.signature(myDsl::Type.__init__)
    params = list(sig.parameters.keys())
    assert "typeVector" in params, "Missing parameter 'typeVector'"

def test_mydsl::type_has_typeVector():
    assert hasattr(myDsl::Type, "typeVector")
    descriptor = None
    for klass in myDsl::Type.__mro__:
        if "typeVector" in klass.__dict__:
            descriptor = klass.__dict__["typeVector"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::static::initializer_is_not_abstract():
    assert not inspect.isabstract(myDsl::Static::initializer)


def test_mydsl::static::initializer_constructor_exists():
    assert callable(myDsl::Static::initializer.__init__)


def test_mydsl::static::initializer_constructor_args():
    sig = inspect.signature(myDsl::Static::initializer.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_mydsl::static::initializer_has_static():
    assert hasattr(myDsl::Static::initializer, "static")
    descriptor = None
    for klass in myDsl::Static::initializer.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::method::declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl::Method::declaration)


def test_mydsl::method::declaration_constructor_exists():
    assert callable(myDsl::Method::declaration.__init__)


def test_mydsl::method::declaration_constructor_args():
    sig = inspect.signature(myDsl::Method::declaration.__init__)
    params = list(sig.parameters.keys())
    assert "modifiersMethod" in params, "Missing parameter 'modifiersMethod'"
    assert "rparent" in params, "Missing parameter 'rparent'"
    assert "debug" in params, "Missing parameter 'debug'"
    assert "nameMethod" in params, "Missing parameter 'nameMethod'"
    assert "lParen" in params, "Missing parameter 'lParen'"

def test_mydsl::method::declaration_has_modifiersMethod():
    assert hasattr(myDsl::Method::declaration, "modifiersMethod")
    descriptor = None
    for klass in myDsl::Method::declaration.__mro__:
        if "modifiersMethod" in klass.__dict__:
            descriptor = klass.__dict__["modifiersMethod"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::method::declaration_has_rparent():
    assert hasattr(myDsl::Method::declaration, "rparent")
    descriptor = None
    for klass in myDsl::Method::declaration.__mro__:
        if "rparent" in klass.__dict__:
            descriptor = klass.__dict__["rparent"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::method::declaration_has_debug():
    assert hasattr(myDsl::Method::declaration, "debug")
    descriptor = None
    for klass in myDsl::Method::declaration.__mro__:
        if "debug" in klass.__dict__:
            descriptor = klass.__dict__["debug"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::method::declaration_has_nameMethod():
    assert hasattr(myDsl::Method::declaration, "nameMethod")
    descriptor = None
    for klass in myDsl::Method::declaration.__mro__:
        if "nameMethod" in klass.__dict__:
            descriptor = klass.__dict__["nameMethod"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::method::declaration_has_lParen():
    assert hasattr(myDsl::Method::declaration, "lParen")
    descriptor = None
    for klass in myDsl::Method::declaration.__mro__:
        if "lParen" in klass.__dict__:
            descriptor = klass.__dict__["lParen"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::constructor::declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl::Constructor::declaration)


def test_mydsl::constructor::declaration_constructor_exists():
    assert callable(myDsl::Constructor::declaration.__init__)


def test_mydsl::constructor::declaration_constructor_args():
    sig = inspect.signature(myDsl::Constructor::declaration.__init__)
    params = list(sig.parameters.keys())
    assert "rparent" in params, "Missing parameter 'rparent'"
    assert "lParen" in params, "Missing parameter 'lParen'"
    assert "nameConstructor" in params, "Missing parameter 'nameConstructor'"
    assert "modifiersConstructor" in params, "Missing parameter 'modifiersConstructor'"

def test_mydsl::constructor::declaration_has_rparent():
    assert hasattr(myDsl::Constructor::declaration, "rparent")
    descriptor = None
    for klass in myDsl::Constructor::declaration.__mro__:
        if "rparent" in klass.__dict__:
            descriptor = klass.__dict__["rparent"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::constructor::declaration_has_lParen():
    assert hasattr(myDsl::Constructor::declaration, "lParen")
    descriptor = None
    for klass in myDsl::Constructor::declaration.__mro__:
        if "lParen" in klass.__dict__:
            descriptor = klass.__dict__["lParen"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::constructor::declaration_has_nameConstructor():
    assert hasattr(myDsl::Constructor::declaration, "nameConstructor")
    descriptor = None
    for klass in myDsl::Constructor::declaration.__mro__:
        if "nameConstructor" in klass.__dict__:
            descriptor = klass.__dict__["nameConstructor"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::constructor::declaration_has_modifiersConstructor():
    assert hasattr(myDsl::Constructor::declaration, "modifiersConstructor")
    descriptor = None
    for klass in myDsl::Constructor::declaration.__mro__:
        if "modifiersConstructor" in klass.__dict__:
            descriptor = klass.__dict__["modifiersConstructor"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::variable::declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl::Variable::declaration)


def test_mydsl::variable::declaration_constructor_exists():
    assert callable(myDsl::Variable::declaration.__init__)


def test_mydsl::variable::declaration_constructor_args():
    sig = inspect.signature(myDsl::Variable::declaration.__init__)
    params = list(sig.parameters.keys())
    assert "modifiersVariable" in params, "Missing parameter 'modifiersVariable'"

def test_mydsl::variable::declaration_has_modifiersVariable():
    assert hasattr(myDsl::Variable::declaration, "modifiersVariable")
    descriptor = None
    for klass in myDsl::Variable::declaration.__mro__:
        if "modifiersVariable" in klass.__dict__:
            descriptor = klass.__dict__["modifiersVariable"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::field::declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl::Field::declaration)


def test_mydsl::field::declaration_constructor_exists():
    assert callable(myDsl::Field::declaration.__init__)


def test_mydsl::field::declaration_constructor_args():
    sig = inspect.signature(myDsl::Field::declaration.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_mydsl::field::declaration_has_comment():
    assert hasattr(myDsl::Field::declaration, "comment")
    descriptor = None
    for klass in myDsl::Field::declaration.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::interface::declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl::Interface::declaration)


def test_mydsl::interface::declaration_constructor_exists():
    assert callable(myDsl::Interface::declaration.__init__)


def test_mydsl::interface::declaration_constructor_args():
    sig = inspect.signature(myDsl::Interface::declaration.__init__)
    params = list(sig.parameters.keys())
    assert "interfaceHerdada" in params, "Missing parameter 'interfaceHerdada'"
    assert "interfaceName" in params, "Missing parameter 'interfaceName'"
    assert "modifiers" in params, "Missing parameter 'modifiers'"
    assert "interfacesHerdadas" in params, "Missing parameter 'interfacesHerdadas'"

def test_mydsl::interface::declaration_has_interfaceHerdada():
    assert hasattr(myDsl::Interface::declaration, "interfaceHerdada")
    descriptor = None
    for klass in myDsl::Interface::declaration.__mro__:
        if "interfaceHerdada" in klass.__dict__:
            descriptor = klass.__dict__["interfaceHerdada"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::interface::declaration_has_interfaceName():
    assert hasattr(myDsl::Interface::declaration, "interfaceName")
    descriptor = None
    for klass in myDsl::Interface::declaration.__mro__:
        if "interfaceName" in klass.__dict__:
            descriptor = klass.__dict__["interfaceName"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::interface::declaration_has_modifiers():
    assert hasattr(myDsl::Interface::declaration, "modifiers")
    descriptor = None
    for klass in myDsl::Interface::declaration.__mro__:
        if "modifiers" in klass.__dict__:
            descriptor = klass.__dict__["modifiers"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::interface::declaration_has_interfacesHerdadas():
    assert hasattr(myDsl::Interface::declaration, "interfacesHerdadas")
    descriptor = None
    for klass in myDsl::Interface::declaration.__mro__:
        if "interfacesHerdadas" in klass.__dict__:
            descriptor = klass.__dict__["interfacesHerdadas"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::class::declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl::Class::declaration)


def test_mydsl::class::declaration_constructor_exists():
    assert callable(myDsl::Class::declaration.__init__)


def test_mydsl::class::declaration_constructor_args():
    sig = inspect.signature(myDsl::Class::declaration.__init__)
    params = list(sig.parameters.keys())
    assert "interfaceImplementada" in params, "Missing parameter 'interfaceImplementada'"
    assert "modifiers" in params, "Missing parameter 'modifiers'"
    assert "interfacesImplementadas" in params, "Missing parameter 'interfacesImplementadas'"
    assert "className" in params, "Missing parameter 'className'"
    assert "classHerdada" in params, "Missing parameter 'classHerdada'"

def test_mydsl::class::declaration_has_interfaceImplementada():
    assert hasattr(myDsl::Class::declaration, "interfaceImplementada")
    descriptor = None
    for klass in myDsl::Class::declaration.__mro__:
        if "interfaceImplementada" in klass.__dict__:
            descriptor = klass.__dict__["interfaceImplementada"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::class::declaration_has_modifiers():
    assert hasattr(myDsl::Class::declaration, "modifiers")
    descriptor = None
    for klass in myDsl::Class::declaration.__mro__:
        if "modifiers" in klass.__dict__:
            descriptor = klass.__dict__["modifiers"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::class::declaration_has_interfacesImplementadas():
    assert hasattr(myDsl::Class::declaration, "interfacesImplementadas")
    descriptor = None
    for klass in myDsl::Class::declaration.__mro__:
        if "interfacesImplementadas" in klass.__dict__:
            descriptor = klass.__dict__["interfacesImplementadas"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::class::declaration_has_className():
    assert hasattr(myDsl::Class::declaration, "className")
    descriptor = None
    for klass in myDsl::Class::declaration.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::class::declaration_has_classHerdada():
    assert hasattr(myDsl::Class::declaration, "classHerdada")
    descriptor = None
    for klass in myDsl::Class::declaration.__mro__:
        if "classHerdada" in klass.__dict__:
            descriptor = klass.__dict__["classHerdada"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::type::declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl::Type::declaration)


def test_mydsl::type::declaration_constructor_exists():
    assert callable(myDsl::Type::declaration.__init__)


def test_mydsl::type::declaration_constructor_args():
    sig = inspect.signature(myDsl::Type::declaration.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_mydsl::type::declaration_has_comment():
    assert hasattr(myDsl::Type::declaration, "comment")
    descriptor = None
    for klass in myDsl::Type::declaration.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::import::statement_is_not_abstract():
    assert not inspect.isabstract(myDsl::Import::statement)


def test_mydsl::import::statement_constructor_exists():
    assert callable(myDsl::Import::statement.__init__)


def test_mydsl::import::statement_constructor_args():
    sig = inspect.signature(myDsl::Import::statement.__init__)
    params = list(sig.parameters.keys())
    assert "pacName" in params, "Missing parameter 'pacName'"
    assert "className" in params, "Missing parameter 'className'"

def test_mydsl::import::statement_has_pacName():
    assert hasattr(myDsl::Import::statement, "pacName")
    descriptor = None
    for klass in myDsl::Import::statement.__mro__:
        if "pacName" in klass.__dict__:
            descriptor = klass.__dict__["pacName"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::import::statement_has_className():
    assert hasattr(myDsl::Import::statement, "className")
    descriptor = None
    for klass in myDsl::Import::statement.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::compilation::unit_is_not_abstract():
    assert not inspect.isabstract(myDsl::Compilation::unit)


def test_mydsl::compilation::unit_constructor_exists():
    assert callable(myDsl::Compilation::unit.__init__)


def test_mydsl::compilation::unit_constructor_args():
    sig = inspect.signature(myDsl::Compilation::unit.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::model_is_not_abstract():
    assert not inspect.isabstract(myDsl::Model)


def test_mydsl::model_constructor_exists():
    assert callable(myDsl::Model.__init__)


def test_mydsl::model_constructor_args():
    sig = inspect.signature(myDsl::Model.__init__)
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
myDsl::Creating::Expression_strategy = st.builds(
    myDsl::Creating::Expression,
    className=
        safe_text
)
myDsl::Float::Literal_strategy = st.builds(
    myDsl::Float::Literal,
    floatTypeSufix=
        safe_text,
    exp=
        safe_text,
    decimalDigits2=
        st.integers(),
    decimalDigits1=
        st.integers()
)
myDsl::Ampersand::Rule_strategy = st.builds(
    myDsl::Ampersand::Rule,
    a2=
        safe_text,
    a1=
        safe_text
)
myDsl::Arg::List_strategy = st.builds(
    myDsl::Arg::List,
)
myDsl::Literal::Expression_strategy = st.builds(
    myDsl::Literal::Expression,
    string=
        safe_text,
    charLit=
        safe_text,
    exp1=
        st.integers(),
    exp=
        safe_text
)
myDsl::Cast::Expression_strategy = st.builds(
    myDsl::Cast::Expression,
)
myDsl::Bit::Expression::NR_strategy = st.builds(
    myDsl::Bit::Expression::NR,
)
myDsl::Logical::Expression::NR_strategy = st.builds(
    myDsl::Logical::Expression::NR,
    false=
        safe_text,
    true=
        safe_text,
    exclamation=
        safe_text
)
myDsl::Expression::aux_strategy = st.builds(
    myDsl::Expression::aux,
    name=
        safe_text,
    sgin=
        safe_text,
    bitSign=
        safe_text,
    logicalSign=
        safe_text,
    stringSign=
        safe_text,
    logicOp=
        safe_text,
    testingSign=
        safe_text,
    numericSign=
        safe_text
)
myDsl::Numeric::Expression::NR_strategy = st.builds(
    myDsl::Numeric::Expression::NR,
    sinal_numeric=
        safe_text
)
myDsl::Try::statement_strategy = st.builds(
    myDsl::Try::statement,
    lParen=
        safe_text,
    rparent=
        safe_text
)
myDsl::Switch::statement_strategy = st.builds(
    myDsl::Switch::statement,
    lParen=
        safe_text,
    rparent=
        safe_text
)
myDsl::For::Statement_strategy = st.builds(
    myDsl::For::Statement,
)
myDsl::While::Statement_strategy = st.builds(
    myDsl::While::Statement,
    rparent=
        safe_text
)
myDsl::Do::Statement_strategy = st.builds(
    myDsl::Do::Statement,
    lparent=
        safe_text,
    rparent=
        safe_text
)
myDsl::If::statement_strategy = st.builds(
    myDsl::If::statement,
    rparent=
        safe_text,
    lparen=
        safe_text
)
myDsl::Statement_strategy = st.builds(
    myDsl::Statement,
    g=
        safe_text,
    name=
        safe_text,
    rparent=
        safe_text,
    ret=
        safe_text,
    nameStatement=
        safe_text
)
myDsl::Type::specifier_strategy = st.builds(
    myDsl::Type::specifier,
    primitiveType=
        safe_text,
    className=
        safe_text
)
myDsl::Expression_strategy = st.builds(
    myDsl::Expression,
    null=
        safe_text,
    name=
        safe_text,
    this=
        safe_text,
    super=
        safe_text
)
myDsl::Array::initializer_strategy = st.builds(
    myDsl::Array::initializer,
)
myDsl::Variable::initializer_strategy = st.builds(
    myDsl::Variable::initializer,
)
myDsl::Variable::declarator_strategy = st.builds(
    myDsl::Variable::declarator,
    nameVariable=
        safe_text,
    lenVector=
        safe_text
)
myDsl::Parameter_strategy = st.builds(
    myDsl::Parameter,
    parameterName=
        safe_text
)
myDsl::Package::statement_strategy = st.builds(
    myDsl::Package::statement,
    pacName=
        safe_text
)
myDsl::Statement::block_strategy = st.builds(
    myDsl::Statement::block,
    lCurly=
        safe_text,
    rCurly=
        safe_text
)
myDsl::Parameter::list_strategy = st.builds(
    myDsl::Parameter::list,
)
myDsl::Type_strategy = st.builds(
    myDsl::Type,
    typeVector=
        safe_text
)
myDsl::Static::initializer_strategy = st.builds(
    myDsl::Static::initializer,
    static=
        safe_text
)
myDsl::Method::declaration_strategy = st.builds(
    myDsl::Method::declaration,
    modifiersMethod=
        safe_text,
    rparent=
        safe_text,
    debug=
        safe_text,
    nameMethod=
        safe_text,
    lParen=
        safe_text
)
myDsl::Constructor::declaration_strategy = st.builds(
    myDsl::Constructor::declaration,
    rparent=
        safe_text,
    lParen=
        safe_text,
    nameConstructor=
        safe_text,
    modifiersConstructor=
        safe_text
)
myDsl::Variable::declaration_strategy = st.builds(
    myDsl::Variable::declaration,
    modifiersVariable=
        safe_text
)
myDsl::Field::declaration_strategy = st.builds(
    myDsl::Field::declaration,
    comment=
        safe_text
)
myDsl::Interface::declaration_strategy = st.builds(
    myDsl::Interface::declaration,
    interfaceHerdada=
        safe_text,
    interfaceName=
        safe_text,
    modifiers=
        safe_text,
    interfacesHerdadas=
        safe_text
)
myDsl::Class::declaration_strategy = st.builds(
    myDsl::Class::declaration,
    interfaceImplementada=
        safe_text,
    modifiers=
        safe_text,
    interfacesImplementadas=
        safe_text,
    className=
        safe_text,
    classHerdada=
        safe_text
)
myDsl::Type::declaration_strategy = st.builds(
    myDsl::Type::declaration,
    comment=
        safe_text
)
myDsl::Import::statement_strategy = st.builds(
    myDsl::Import::statement,
    pacName=
        safe_text,
    className=
        safe_text
)
myDsl::Compilation::unit_strategy = st.builds(
    myDsl::Compilation::unit,
)
myDsl::Model_strategy = st.builds(
    myDsl::Model,
)

@given(instance=myDsl::Creating::Expression_strategy)
@settings(max_examples=50)
def test_mydsl::creating::expression_instantiation(instance):
    assert isinstance(instance, myDsl::Creating::Expression)

@given(instance=myDsl::Creating::Expression_strategy)
def test_mydsl::creating::expression_className_type(instance):
    assert isinstance(instance.className, str)


@given(instance=myDsl::Creating::Expression_strategy)
def test_mydsl::creating::expression_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=myDsl::Float::Literal_strategy)
@settings(max_examples=50)
def test_mydsl::float::literal_instantiation(instance):
    assert isinstance(instance, myDsl::Float::Literal)

@given(instance=myDsl::Float::Literal_strategy)
def test_mydsl::float::literal_floatTypeSufix_type(instance):
    assert isinstance(instance.floatTypeSufix, str)


@given(instance=myDsl::Float::Literal_strategy)
def test_mydsl::float::literal_floatTypeSufix_setter(instance):
    original = instance.floatTypeSufix
    instance.floatTypeSufix = original
    assert instance.floatTypeSufix == original

@given(instance=myDsl::Float::Literal_strategy)
def test_mydsl::float::literal_exp_type(instance):
    assert isinstance(instance.exp, str)


@given(instance=myDsl::Float::Literal_strategy)
def test_mydsl::float::literal_exp_setter(instance):
    original = instance.exp
    instance.exp = original
    assert instance.exp == original

@given(instance=myDsl::Float::Literal_strategy)
def test_mydsl::float::literal_decimalDigits2_type(instance):
    assert isinstance(instance.decimalDigits2, int)


@given(instance=myDsl::Float::Literal_strategy)
def test_mydsl::float::literal_decimalDigits2_setter(instance):
    original = instance.decimalDigits2
    instance.decimalDigits2 = original
    assert instance.decimalDigits2 == original

@given(instance=myDsl::Float::Literal_strategy)
def test_mydsl::float::literal_decimalDigits1_type(instance):
    assert isinstance(instance.decimalDigits1, int)


@given(instance=myDsl::Float::Literal_strategy)
def test_mydsl::float::literal_decimalDigits1_setter(instance):
    original = instance.decimalDigits1
    instance.decimalDigits1 = original
    assert instance.decimalDigits1 == original

@given(instance=myDsl::Ampersand::Rule_strategy)
@settings(max_examples=50)
def test_mydsl::ampersand::rule_instantiation(instance):
    assert isinstance(instance, myDsl::Ampersand::Rule)

@given(instance=myDsl::Ampersand::Rule_strategy)
def test_mydsl::ampersand::rule_a2_type(instance):
    assert isinstance(instance.a2, str)


@given(instance=myDsl::Ampersand::Rule_strategy)
def test_mydsl::ampersand::rule_a2_setter(instance):
    original = instance.a2
    instance.a2 = original
    assert instance.a2 == original

@given(instance=myDsl::Ampersand::Rule_strategy)
def test_mydsl::ampersand::rule_a1_type(instance):
    assert isinstance(instance.a1, str)


@given(instance=myDsl::Ampersand::Rule_strategy)
def test_mydsl::ampersand::rule_a1_setter(instance):
    original = instance.a1
    instance.a1 = original
    assert instance.a1 == original

@given(instance=myDsl::Arg::List_strategy)
@settings(max_examples=50)
def test_mydsl::arg::list_instantiation(instance):
    assert isinstance(instance, myDsl::Arg::List)

@given(instance=myDsl::Literal::Expression_strategy)
@settings(max_examples=50)
def test_mydsl::literal::expression_instantiation(instance):
    assert isinstance(instance, myDsl::Literal::Expression)

@given(instance=myDsl::Literal::Expression_strategy)
def test_mydsl::literal::expression_string_type(instance):
    assert isinstance(instance.string, str)


@given(instance=myDsl::Literal::Expression_strategy)
def test_mydsl::literal::expression_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=myDsl::Literal::Expression_strategy)
def test_mydsl::literal::expression_charLit_type(instance):
    assert isinstance(instance.charLit, str)


@given(instance=myDsl::Literal::Expression_strategy)
def test_mydsl::literal::expression_charLit_setter(instance):
    original = instance.charLit
    instance.charLit = original
    assert instance.charLit == original

@given(instance=myDsl::Literal::Expression_strategy)
def test_mydsl::literal::expression_exp1_type(instance):
    assert isinstance(instance.exp1, int)


@given(instance=myDsl::Literal::Expression_strategy)
def test_mydsl::literal::expression_exp1_setter(instance):
    original = instance.exp1
    instance.exp1 = original
    assert instance.exp1 == original

@given(instance=myDsl::Literal::Expression_strategy)
def test_mydsl::literal::expression_exp_type(instance):
    assert isinstance(instance.exp, str)


@given(instance=myDsl::Literal::Expression_strategy)
def test_mydsl::literal::expression_exp_setter(instance):
    original = instance.exp
    instance.exp = original
    assert instance.exp == original

@given(instance=myDsl::Cast::Expression_strategy)
@settings(max_examples=50)
def test_mydsl::cast::expression_instantiation(instance):
    assert isinstance(instance, myDsl::Cast::Expression)

@given(instance=myDsl::Bit::Expression::NR_strategy)
@settings(max_examples=50)
def test_mydsl::bit::expression::nr_instantiation(instance):
    assert isinstance(instance, myDsl::Bit::Expression::NR)

@given(instance=myDsl::Logical::Expression::NR_strategy)
@settings(max_examples=50)
def test_mydsl::logical::expression::nr_instantiation(instance):
    assert isinstance(instance, myDsl::Logical::Expression::NR)

@given(instance=myDsl::Logical::Expression::NR_strategy)
def test_mydsl::logical::expression::nr_false_type(instance):
    assert isinstance(instance.false, str)


@given(instance=myDsl::Logical::Expression::NR_strategy)
def test_mydsl::logical::expression::nr_false_setter(instance):
    original = instance.false
    instance.false = original
    assert instance.false == original

@given(instance=myDsl::Logical::Expression::NR_strategy)
def test_mydsl::logical::expression::nr_true_type(instance):
    assert isinstance(instance.true, str)


@given(instance=myDsl::Logical::Expression::NR_strategy)
def test_mydsl::logical::expression::nr_true_setter(instance):
    original = instance.true
    instance.true = original
    assert instance.true == original

@given(instance=myDsl::Logical::Expression::NR_strategy)
def test_mydsl::logical::expression::nr_exclamation_type(instance):
    assert isinstance(instance.exclamation, str)


@given(instance=myDsl::Logical::Expression::NR_strategy)
def test_mydsl::logical::expression::nr_exclamation_setter(instance):
    original = instance.exclamation
    instance.exclamation = original
    assert instance.exclamation == original

@given(instance=myDsl::Expression::aux_strategy)
@settings(max_examples=50)
def test_mydsl::expression::aux_instantiation(instance):
    assert isinstance(instance, myDsl::Expression::aux)

@given(instance=myDsl::Expression::aux_strategy)
def test_mydsl::expression::aux_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Expression::aux_strategy)
def test_mydsl::expression::aux_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Expression::aux_strategy)
def test_mydsl::expression::aux_sgin_type(instance):
    assert isinstance(instance.sgin, str)


@given(instance=myDsl::Expression::aux_strategy)
def test_mydsl::expression::aux_sgin_setter(instance):
    original = instance.sgin
    instance.sgin = original
    assert instance.sgin == original

@given(instance=myDsl::Expression::aux_strategy)
def test_mydsl::expression::aux_bitSign_type(instance):
    assert isinstance(instance.bitSign, str)


@given(instance=myDsl::Expression::aux_strategy)
def test_mydsl::expression::aux_bitSign_setter(instance):
    original = instance.bitSign
    instance.bitSign = original
    assert instance.bitSign == original

@given(instance=myDsl::Expression::aux_strategy)
def test_mydsl::expression::aux_logicalSign_type(instance):
    assert isinstance(instance.logicalSign, str)


@given(instance=myDsl::Expression::aux_strategy)
def test_mydsl::expression::aux_logicalSign_setter(instance):
    original = instance.logicalSign
    instance.logicalSign = original
    assert instance.logicalSign == original

@given(instance=myDsl::Expression::aux_strategy)
def test_mydsl::expression::aux_stringSign_type(instance):
    assert isinstance(instance.stringSign, str)


@given(instance=myDsl::Expression::aux_strategy)
def test_mydsl::expression::aux_stringSign_setter(instance):
    original = instance.stringSign
    instance.stringSign = original
    assert instance.stringSign == original

@given(instance=myDsl::Expression::aux_strategy)
def test_mydsl::expression::aux_logicOp_type(instance):
    assert isinstance(instance.logicOp, str)


@given(instance=myDsl::Expression::aux_strategy)
def test_mydsl::expression::aux_logicOp_setter(instance):
    original = instance.logicOp
    instance.logicOp = original
    assert instance.logicOp == original

@given(instance=myDsl::Expression::aux_strategy)
def test_mydsl::expression::aux_testingSign_type(instance):
    assert isinstance(instance.testingSign, str)


@given(instance=myDsl::Expression::aux_strategy)
def test_mydsl::expression::aux_testingSign_setter(instance):
    original = instance.testingSign
    instance.testingSign = original
    assert instance.testingSign == original

@given(instance=myDsl::Expression::aux_strategy)
def test_mydsl::expression::aux_numericSign_type(instance):
    assert isinstance(instance.numericSign, str)


@given(instance=myDsl::Expression::aux_strategy)
def test_mydsl::expression::aux_numericSign_setter(instance):
    original = instance.numericSign
    instance.numericSign = original
    assert instance.numericSign == original

@given(instance=myDsl::Numeric::Expression::NR_strategy)
@settings(max_examples=50)
def test_mydsl::numeric::expression::nr_instantiation(instance):
    assert isinstance(instance, myDsl::Numeric::Expression::NR)

@given(instance=myDsl::Numeric::Expression::NR_strategy)
def test_mydsl::numeric::expression::nr_sinal_numeric_type(instance):
    assert isinstance(instance.sinal_numeric, str)


@given(instance=myDsl::Numeric::Expression::NR_strategy)
def test_mydsl::numeric::expression::nr_sinal_numeric_setter(instance):
    original = instance.sinal_numeric
    instance.sinal_numeric = original
    assert instance.sinal_numeric == original

@given(instance=myDsl::Try::statement_strategy)
@settings(max_examples=50)
def test_mydsl::try::statement_instantiation(instance):
    assert isinstance(instance, myDsl::Try::statement)

@given(instance=myDsl::Try::statement_strategy)
def test_mydsl::try::statement_lParen_type(instance):
    assert isinstance(instance.lParen, str)


@given(instance=myDsl::Try::statement_strategy)
def test_mydsl::try::statement_lParen_setter(instance):
    original = instance.lParen
    instance.lParen = original
    assert instance.lParen == original

@given(instance=myDsl::Try::statement_strategy)
def test_mydsl::try::statement_rparent_type(instance):
    assert isinstance(instance.rparent, str)


@given(instance=myDsl::Try::statement_strategy)
def test_mydsl::try::statement_rparent_setter(instance):
    original = instance.rparent
    instance.rparent = original
    assert instance.rparent == original

@given(instance=myDsl::Switch::statement_strategy)
@settings(max_examples=50)
def test_mydsl::switch::statement_instantiation(instance):
    assert isinstance(instance, myDsl::Switch::statement)

@given(instance=myDsl::Switch::statement_strategy)
def test_mydsl::switch::statement_lParen_type(instance):
    assert isinstance(instance.lParen, str)


@given(instance=myDsl::Switch::statement_strategy)
def test_mydsl::switch::statement_lParen_setter(instance):
    original = instance.lParen
    instance.lParen = original
    assert instance.lParen == original

@given(instance=myDsl::Switch::statement_strategy)
def test_mydsl::switch::statement_rparent_type(instance):
    assert isinstance(instance.rparent, str)


@given(instance=myDsl::Switch::statement_strategy)
def test_mydsl::switch::statement_rparent_setter(instance):
    original = instance.rparent
    instance.rparent = original
    assert instance.rparent == original

@given(instance=myDsl::For::Statement_strategy)
@settings(max_examples=50)
def test_mydsl::for::statement_instantiation(instance):
    assert isinstance(instance, myDsl::For::Statement)

@given(instance=myDsl::While::Statement_strategy)
@settings(max_examples=50)
def test_mydsl::while::statement_instantiation(instance):
    assert isinstance(instance, myDsl::While::Statement)

@given(instance=myDsl::While::Statement_strategy)
def test_mydsl::while::statement_rparent_type(instance):
    assert isinstance(instance.rparent, str)


@given(instance=myDsl::While::Statement_strategy)
def test_mydsl::while::statement_rparent_setter(instance):
    original = instance.rparent
    instance.rparent = original
    assert instance.rparent == original

@given(instance=myDsl::Do::Statement_strategy)
@settings(max_examples=50)
def test_mydsl::do::statement_instantiation(instance):
    assert isinstance(instance, myDsl::Do::Statement)

@given(instance=myDsl::Do::Statement_strategy)
def test_mydsl::do::statement_lparent_type(instance):
    assert isinstance(instance.lparent, str)


@given(instance=myDsl::Do::Statement_strategy)
def test_mydsl::do::statement_lparent_setter(instance):
    original = instance.lparent
    instance.lparent = original
    assert instance.lparent == original

@given(instance=myDsl::Do::Statement_strategy)
def test_mydsl::do::statement_rparent_type(instance):
    assert isinstance(instance.rparent, str)


@given(instance=myDsl::Do::Statement_strategy)
def test_mydsl::do::statement_rparent_setter(instance):
    original = instance.rparent
    instance.rparent = original
    assert instance.rparent == original

@given(instance=myDsl::If::statement_strategy)
@settings(max_examples=50)
def test_mydsl::if::statement_instantiation(instance):
    assert isinstance(instance, myDsl::If::statement)

@given(instance=myDsl::If::statement_strategy)
def test_mydsl::if::statement_rparent_type(instance):
    assert isinstance(instance.rparent, str)


@given(instance=myDsl::If::statement_strategy)
def test_mydsl::if::statement_rparent_setter(instance):
    original = instance.rparent
    instance.rparent = original
    assert instance.rparent == original

@given(instance=myDsl::If::statement_strategy)
def test_mydsl::if::statement_lparen_type(instance):
    assert isinstance(instance.lparen, str)


@given(instance=myDsl::If::statement_strategy)
def test_mydsl::if::statement_lparen_setter(instance):
    original = instance.lparen
    instance.lparen = original
    assert instance.lparen == original

@given(instance=myDsl::Statement_strategy)
@settings(max_examples=50)
def test_mydsl::statement_instantiation(instance):
    assert isinstance(instance, myDsl::Statement)

@given(instance=myDsl::Statement_strategy)
def test_mydsl::statement_g_type(instance):
    assert isinstance(instance.g, str)


@given(instance=myDsl::Statement_strategy)
def test_mydsl::statement_g_setter(instance):
    original = instance.g
    instance.g = original
    assert instance.g == original

@given(instance=myDsl::Statement_strategy)
def test_mydsl::statement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Statement_strategy)
def test_mydsl::statement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Statement_strategy)
def test_mydsl::statement_rparent_type(instance):
    assert isinstance(instance.rparent, str)


@given(instance=myDsl::Statement_strategy)
def test_mydsl::statement_rparent_setter(instance):
    original = instance.rparent
    instance.rparent = original
    assert instance.rparent == original

@given(instance=myDsl::Statement_strategy)
def test_mydsl::statement_ret_type(instance):
    assert isinstance(instance.ret, str)


@given(instance=myDsl::Statement_strategy)
def test_mydsl::statement_ret_setter(instance):
    original = instance.ret
    instance.ret = original
    assert instance.ret == original

@given(instance=myDsl::Statement_strategy)
def test_mydsl::statement_nameStatement_type(instance):
    assert isinstance(instance.nameStatement, str)


@given(instance=myDsl::Statement_strategy)
def test_mydsl::statement_nameStatement_setter(instance):
    original = instance.nameStatement
    instance.nameStatement = original
    assert instance.nameStatement == original

@given(instance=myDsl::Type::specifier_strategy)
@settings(max_examples=50)
def test_mydsl::type::specifier_instantiation(instance):
    assert isinstance(instance, myDsl::Type::specifier)

@given(instance=myDsl::Type::specifier_strategy)
def test_mydsl::type::specifier_primitiveType_type(instance):
    assert isinstance(instance.primitiveType, str)


@given(instance=myDsl::Type::specifier_strategy)
def test_mydsl::type::specifier_primitiveType_setter(instance):
    original = instance.primitiveType
    instance.primitiveType = original
    assert instance.primitiveType == original

@given(instance=myDsl::Type::specifier_strategy)
def test_mydsl::type::specifier_className_type(instance):
    assert isinstance(instance.className, str)


@given(instance=myDsl::Type::specifier_strategy)
def test_mydsl::type::specifier_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=myDsl::Expression_strategy)
@settings(max_examples=50)
def test_mydsl::expression_instantiation(instance):
    assert isinstance(instance, myDsl::Expression)

@given(instance=myDsl::Expression_strategy)
def test_mydsl::expression_null_type(instance):
    assert isinstance(instance.null, str)


@given(instance=myDsl::Expression_strategy)
def test_mydsl::expression_null_setter(instance):
    original = instance.null
    instance.null = original
    assert instance.null == original

@given(instance=myDsl::Expression_strategy)
def test_mydsl::expression_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Expression_strategy)
def test_mydsl::expression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Expression_strategy)
def test_mydsl::expression_this_type(instance):
    assert isinstance(instance.this, str)


@given(instance=myDsl::Expression_strategy)
def test_mydsl::expression_this_setter(instance):
    original = instance.this
    instance.this = original
    assert instance.this == original

@given(instance=myDsl::Expression_strategy)
def test_mydsl::expression_super_type(instance):
    assert isinstance(instance.super, str)


@given(instance=myDsl::Expression_strategy)
def test_mydsl::expression_super_setter(instance):
    original = instance.super
    instance.super = original
    assert instance.super == original

@given(instance=myDsl::Array::initializer_strategy)
@settings(max_examples=50)
def test_mydsl::array::initializer_instantiation(instance):
    assert isinstance(instance, myDsl::Array::initializer)

@given(instance=myDsl::Variable::initializer_strategy)
@settings(max_examples=50)
def test_mydsl::variable::initializer_instantiation(instance):
    assert isinstance(instance, myDsl::Variable::initializer)

@given(instance=myDsl::Variable::declarator_strategy)
@settings(max_examples=50)
def test_mydsl::variable::declarator_instantiation(instance):
    assert isinstance(instance, myDsl::Variable::declarator)

@given(instance=myDsl::Variable::declarator_strategy)
def test_mydsl::variable::declarator_nameVariable_type(instance):
    assert isinstance(instance.nameVariable, str)


@given(instance=myDsl::Variable::declarator_strategy)
def test_mydsl::variable::declarator_nameVariable_setter(instance):
    original = instance.nameVariable
    instance.nameVariable = original
    assert instance.nameVariable == original

@given(instance=myDsl::Variable::declarator_strategy)
def test_mydsl::variable::declarator_lenVector_type(instance):
    assert isinstance(instance.lenVector, str)


@given(instance=myDsl::Variable::declarator_strategy)
def test_mydsl::variable::declarator_lenVector_setter(instance):
    original = instance.lenVector
    instance.lenVector = original
    assert instance.lenVector == original

@given(instance=myDsl::Parameter_strategy)
@settings(max_examples=50)
def test_mydsl::parameter_instantiation(instance):
    assert isinstance(instance, myDsl::Parameter)

@given(instance=myDsl::Parameter_strategy)
def test_mydsl::parameter_parameterName_type(instance):
    assert isinstance(instance.parameterName, str)


@given(instance=myDsl::Parameter_strategy)
def test_mydsl::parameter_parameterName_setter(instance):
    original = instance.parameterName
    instance.parameterName = original
    assert instance.parameterName == original

@given(instance=myDsl::Package::statement_strategy)
@settings(max_examples=50)
def test_mydsl::package::statement_instantiation(instance):
    assert isinstance(instance, myDsl::Package::statement)

@given(instance=myDsl::Package::statement_strategy)
def test_mydsl::package::statement_pacName_type(instance):
    assert isinstance(instance.pacName, str)


@given(instance=myDsl::Package::statement_strategy)
def test_mydsl::package::statement_pacName_setter(instance):
    original = instance.pacName
    instance.pacName = original
    assert instance.pacName == original

@given(instance=myDsl::Statement::block_strategy)
@settings(max_examples=50)
def test_mydsl::statement::block_instantiation(instance):
    assert isinstance(instance, myDsl::Statement::block)

@given(instance=myDsl::Statement::block_strategy)
def test_mydsl::statement::block_lCurly_type(instance):
    assert isinstance(instance.lCurly, str)


@given(instance=myDsl::Statement::block_strategy)
def test_mydsl::statement::block_lCurly_setter(instance):
    original = instance.lCurly
    instance.lCurly = original
    assert instance.lCurly == original

@given(instance=myDsl::Statement::block_strategy)
def test_mydsl::statement::block_rCurly_type(instance):
    assert isinstance(instance.rCurly, str)


@given(instance=myDsl::Statement::block_strategy)
def test_mydsl::statement::block_rCurly_setter(instance):
    original = instance.rCurly
    instance.rCurly = original
    assert instance.rCurly == original

@given(instance=myDsl::Parameter::list_strategy)
@settings(max_examples=50)
def test_mydsl::parameter::list_instantiation(instance):
    assert isinstance(instance, myDsl::Parameter::list)

@given(instance=myDsl::Type_strategy)
@settings(max_examples=50)
def test_mydsl::type_instantiation(instance):
    assert isinstance(instance, myDsl::Type)

@given(instance=myDsl::Type_strategy)
def test_mydsl::type_typeVector_type(instance):
    assert isinstance(instance.typeVector, str)


@given(instance=myDsl::Type_strategy)
def test_mydsl::type_typeVector_setter(instance):
    original = instance.typeVector
    instance.typeVector = original
    assert instance.typeVector == original

@given(instance=myDsl::Static::initializer_strategy)
@settings(max_examples=50)
def test_mydsl::static::initializer_instantiation(instance):
    assert isinstance(instance, myDsl::Static::initializer)

@given(instance=myDsl::Static::initializer_strategy)
def test_mydsl::static::initializer_static_type(instance):
    assert isinstance(instance.static, str)


@given(instance=myDsl::Static::initializer_strategy)
def test_mydsl::static::initializer_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=myDsl::Method::declaration_strategy)
@settings(max_examples=50)
def test_mydsl::method::declaration_instantiation(instance):
    assert isinstance(instance, myDsl::Method::declaration)

@given(instance=myDsl::Method::declaration_strategy)
def test_mydsl::method::declaration_modifiersMethod_type(instance):
    assert isinstance(instance.modifiersMethod, str)


@given(instance=myDsl::Method::declaration_strategy)
def test_mydsl::method::declaration_modifiersMethod_setter(instance):
    original = instance.modifiersMethod
    instance.modifiersMethod = original
    assert instance.modifiersMethod == original

@given(instance=myDsl::Method::declaration_strategy)
def test_mydsl::method::declaration_rparent_type(instance):
    assert isinstance(instance.rparent, str)


@given(instance=myDsl::Method::declaration_strategy)
def test_mydsl::method::declaration_rparent_setter(instance):
    original = instance.rparent
    instance.rparent = original
    assert instance.rparent == original

@given(instance=myDsl::Method::declaration_strategy)
def test_mydsl::method::declaration_debug_type(instance):
    assert isinstance(instance.debug, str)


@given(instance=myDsl::Method::declaration_strategy)
def test_mydsl::method::declaration_debug_setter(instance):
    original = instance.debug
    instance.debug = original
    assert instance.debug == original

@given(instance=myDsl::Method::declaration_strategy)
def test_mydsl::method::declaration_nameMethod_type(instance):
    assert isinstance(instance.nameMethod, str)


@given(instance=myDsl::Method::declaration_strategy)
def test_mydsl::method::declaration_nameMethod_setter(instance):
    original = instance.nameMethod
    instance.nameMethod = original
    assert instance.nameMethod == original

@given(instance=myDsl::Method::declaration_strategy)
def test_mydsl::method::declaration_lParen_type(instance):
    assert isinstance(instance.lParen, str)


@given(instance=myDsl::Method::declaration_strategy)
def test_mydsl::method::declaration_lParen_setter(instance):
    original = instance.lParen
    instance.lParen = original
    assert instance.lParen == original

@given(instance=myDsl::Constructor::declaration_strategy)
@settings(max_examples=50)
def test_mydsl::constructor::declaration_instantiation(instance):
    assert isinstance(instance, myDsl::Constructor::declaration)

@given(instance=myDsl::Constructor::declaration_strategy)
def test_mydsl::constructor::declaration_rparent_type(instance):
    assert isinstance(instance.rparent, str)


@given(instance=myDsl::Constructor::declaration_strategy)
def test_mydsl::constructor::declaration_rparent_setter(instance):
    original = instance.rparent
    instance.rparent = original
    assert instance.rparent == original

@given(instance=myDsl::Constructor::declaration_strategy)
def test_mydsl::constructor::declaration_lParen_type(instance):
    assert isinstance(instance.lParen, str)


@given(instance=myDsl::Constructor::declaration_strategy)
def test_mydsl::constructor::declaration_lParen_setter(instance):
    original = instance.lParen
    instance.lParen = original
    assert instance.lParen == original

@given(instance=myDsl::Constructor::declaration_strategy)
def test_mydsl::constructor::declaration_nameConstructor_type(instance):
    assert isinstance(instance.nameConstructor, str)


@given(instance=myDsl::Constructor::declaration_strategy)
def test_mydsl::constructor::declaration_nameConstructor_setter(instance):
    original = instance.nameConstructor
    instance.nameConstructor = original
    assert instance.nameConstructor == original

@given(instance=myDsl::Constructor::declaration_strategy)
def test_mydsl::constructor::declaration_modifiersConstructor_type(instance):
    assert isinstance(instance.modifiersConstructor, str)


@given(instance=myDsl::Constructor::declaration_strategy)
def test_mydsl::constructor::declaration_modifiersConstructor_setter(instance):
    original = instance.modifiersConstructor
    instance.modifiersConstructor = original
    assert instance.modifiersConstructor == original

@given(instance=myDsl::Variable::declaration_strategy)
@settings(max_examples=50)
def test_mydsl::variable::declaration_instantiation(instance):
    assert isinstance(instance, myDsl::Variable::declaration)

@given(instance=myDsl::Variable::declaration_strategy)
def test_mydsl::variable::declaration_modifiersVariable_type(instance):
    assert isinstance(instance.modifiersVariable, str)


@given(instance=myDsl::Variable::declaration_strategy)
def test_mydsl::variable::declaration_modifiersVariable_setter(instance):
    original = instance.modifiersVariable
    instance.modifiersVariable = original
    assert instance.modifiersVariable == original

@given(instance=myDsl::Field::declaration_strategy)
@settings(max_examples=50)
def test_mydsl::field::declaration_instantiation(instance):
    assert isinstance(instance, myDsl::Field::declaration)

@given(instance=myDsl::Field::declaration_strategy)
def test_mydsl::field::declaration_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=myDsl::Field::declaration_strategy)
def test_mydsl::field::declaration_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=myDsl::Interface::declaration_strategy)
@settings(max_examples=50)
def test_mydsl::interface::declaration_instantiation(instance):
    assert isinstance(instance, myDsl::Interface::declaration)

@given(instance=myDsl::Interface::declaration_strategy)
def test_mydsl::interface::declaration_interfaceHerdada_type(instance):
    assert isinstance(instance.interfaceHerdada, str)


@given(instance=myDsl::Interface::declaration_strategy)
def test_mydsl::interface::declaration_interfaceHerdada_setter(instance):
    original = instance.interfaceHerdada
    instance.interfaceHerdada = original
    assert instance.interfaceHerdada == original

@given(instance=myDsl::Interface::declaration_strategy)
def test_mydsl::interface::declaration_interfaceName_type(instance):
    assert isinstance(instance.interfaceName, str)


@given(instance=myDsl::Interface::declaration_strategy)
def test_mydsl::interface::declaration_interfaceName_setter(instance):
    original = instance.interfaceName
    instance.interfaceName = original
    assert instance.interfaceName == original

@given(instance=myDsl::Interface::declaration_strategy)
def test_mydsl::interface::declaration_modifiers_type(instance):
    assert isinstance(instance.modifiers, str)


@given(instance=myDsl::Interface::declaration_strategy)
def test_mydsl::interface::declaration_modifiers_setter(instance):
    original = instance.modifiers
    instance.modifiers = original
    assert instance.modifiers == original

@given(instance=myDsl::Interface::declaration_strategy)
def test_mydsl::interface::declaration_interfacesHerdadas_type(instance):
    assert isinstance(instance.interfacesHerdadas, str)


@given(instance=myDsl::Interface::declaration_strategy)
def test_mydsl::interface::declaration_interfacesHerdadas_setter(instance):
    original = instance.interfacesHerdadas
    instance.interfacesHerdadas = original
    assert instance.interfacesHerdadas == original

@given(instance=myDsl::Class::declaration_strategy)
@settings(max_examples=50)
def test_mydsl::class::declaration_instantiation(instance):
    assert isinstance(instance, myDsl::Class::declaration)

@given(instance=myDsl::Class::declaration_strategy)
def test_mydsl::class::declaration_interfaceImplementada_type(instance):
    assert isinstance(instance.interfaceImplementada, str)


@given(instance=myDsl::Class::declaration_strategy)
def test_mydsl::class::declaration_interfaceImplementada_setter(instance):
    original = instance.interfaceImplementada
    instance.interfaceImplementada = original
    assert instance.interfaceImplementada == original

@given(instance=myDsl::Class::declaration_strategy)
def test_mydsl::class::declaration_modifiers_type(instance):
    assert isinstance(instance.modifiers, str)


@given(instance=myDsl::Class::declaration_strategy)
def test_mydsl::class::declaration_modifiers_setter(instance):
    original = instance.modifiers
    instance.modifiers = original
    assert instance.modifiers == original

@given(instance=myDsl::Class::declaration_strategy)
def test_mydsl::class::declaration_interfacesImplementadas_type(instance):
    assert isinstance(instance.interfacesImplementadas, str)


@given(instance=myDsl::Class::declaration_strategy)
def test_mydsl::class::declaration_interfacesImplementadas_setter(instance):
    original = instance.interfacesImplementadas
    instance.interfacesImplementadas = original
    assert instance.interfacesImplementadas == original

@given(instance=myDsl::Class::declaration_strategy)
def test_mydsl::class::declaration_className_type(instance):
    assert isinstance(instance.className, str)


@given(instance=myDsl::Class::declaration_strategy)
def test_mydsl::class::declaration_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=myDsl::Class::declaration_strategy)
def test_mydsl::class::declaration_classHerdada_type(instance):
    assert isinstance(instance.classHerdada, str)


@given(instance=myDsl::Class::declaration_strategy)
def test_mydsl::class::declaration_classHerdada_setter(instance):
    original = instance.classHerdada
    instance.classHerdada = original
    assert instance.classHerdada == original

@given(instance=myDsl::Type::declaration_strategy)
@settings(max_examples=50)
def test_mydsl::type::declaration_instantiation(instance):
    assert isinstance(instance, myDsl::Type::declaration)

@given(instance=myDsl::Type::declaration_strategy)
def test_mydsl::type::declaration_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=myDsl::Type::declaration_strategy)
def test_mydsl::type::declaration_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=myDsl::Import::statement_strategy)
@settings(max_examples=50)
def test_mydsl::import::statement_instantiation(instance):
    assert isinstance(instance, myDsl::Import::statement)

@given(instance=myDsl::Import::statement_strategy)
def test_mydsl::import::statement_pacName_type(instance):
    assert isinstance(instance.pacName, str)


@given(instance=myDsl::Import::statement_strategy)
def test_mydsl::import::statement_pacName_setter(instance):
    original = instance.pacName
    instance.pacName = original
    assert instance.pacName == original

@given(instance=myDsl::Import::statement_strategy)
def test_mydsl::import::statement_className_type(instance):
    assert isinstance(instance.className, str)


@given(instance=myDsl::Import::statement_strategy)
def test_mydsl::import::statement_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=myDsl::Compilation::unit_strategy)
@settings(max_examples=50)
def test_mydsl::compilation::unit_instantiation(instance):
    assert isinstance(instance, myDsl::Compilation::unit)

@given(instance=myDsl::Model_strategy)
@settings(max_examples=50)
def test_mydsl::model_instantiation(instance):
    assert isinstance(instance, myDsl::Model)
