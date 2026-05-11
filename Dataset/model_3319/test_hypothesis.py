import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    java::Expression::aux,
    java::Numeric::Expression::NR,
    java::Expression,
    java::Variable::initializer,
    java::Variable::declarator,
    java::Class::declaration,
    java::Field::declaration,
    java::Constructor::declaration,
    java::Parameter::list::method::call,
    Return::value,
    java::Method::call,
    java::Parameter::list,
    java::Type,
    java::Method::declaration,
    java::Interface::declaration,
    java::EObject,
    java::Type::declaration,
    java::Import::statement,
    java::Package::statement,
    java::Compilation::unit,
    java::Head,
    java::Return::value,
    java::Try::statement,
    java::Switch::Statement,
    java::For::Statement,
    java::While::Statement,
    java::Do::Statement,
    java::If::Statement,
    java::Return::Statement,
    java::Statement,
    Statement,
    java::Statement::block,
    java::Static::initializer,
    java::Arg::List,
    java::Float::Literal,
    java::Ampersand::Rule,
    java::Variable::declaration,
    java::Parameter,
    java::Literal::Expression,
    java::Creating::Expression,
    java::Cast::Expression,
    java::Bit::Expression::NR,
    java::Logical::Expression::NR,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_java::expression::aux_is_not_abstract():
    assert not inspect.isabstract(java::Expression::aux)


def test_java::expression::aux_constructor_exists():
    assert callable(java::Expression::aux.__init__)


def test_java::expression::aux_constructor_args():
    sig = inspect.signature(java::Expression::aux.__init__)
    params = list(sig.parameters.keys())
    assert "bitSign" in params, "Missing parameter 'bitSign'"
    assert "stringSign" in params, "Missing parameter 'stringSign'"
    assert "name" in params, "Missing parameter 'name'"
    assert "numericSign" in params, "Missing parameter 'numericSign'"
    assert "testingSign" in params, "Missing parameter 'testingSign'"
    assert "logicalSign" in params, "Missing parameter 'logicalSign'"
    assert "sgin" in params, "Missing parameter 'sgin'"

def test_java::expression::aux_has_bitSign():
    assert hasattr(java::Expression::aux, "bitSign")
    descriptor = None
    for klass in java::Expression::aux.__mro__:
        if "bitSign" in klass.__dict__:
            descriptor = klass.__dict__["bitSign"]
            break
    assert isinstance(descriptor, property)

def test_java::expression::aux_has_stringSign():
    assert hasattr(java::Expression::aux, "stringSign")
    descriptor = None
    for klass in java::Expression::aux.__mro__:
        if "stringSign" in klass.__dict__:
            descriptor = klass.__dict__["stringSign"]
            break
    assert isinstance(descriptor, property)

def test_java::expression::aux_has_name():
    assert hasattr(java::Expression::aux, "name")
    descriptor = None
    for klass in java::Expression::aux.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_java::expression::aux_has_numericSign():
    assert hasattr(java::Expression::aux, "numericSign")
    descriptor = None
    for klass in java::Expression::aux.__mro__:
        if "numericSign" in klass.__dict__:
            descriptor = klass.__dict__["numericSign"]
            break
    assert isinstance(descriptor, property)

def test_java::expression::aux_has_testingSign():
    assert hasattr(java::Expression::aux, "testingSign")
    descriptor = None
    for klass in java::Expression::aux.__mro__:
        if "testingSign" in klass.__dict__:
            descriptor = klass.__dict__["testingSign"]
            break
    assert isinstance(descriptor, property)

def test_java::expression::aux_has_logicalSign():
    assert hasattr(java::Expression::aux, "logicalSign")
    descriptor = None
    for klass in java::Expression::aux.__mro__:
        if "logicalSign" in klass.__dict__:
            descriptor = klass.__dict__["logicalSign"]
            break
    assert isinstance(descriptor, property)

def test_java::expression::aux_has_sgin():
    assert hasattr(java::Expression::aux, "sgin")
    descriptor = None
    for klass in java::Expression::aux.__mro__:
        if "sgin" in klass.__dict__:
            descriptor = klass.__dict__["sgin"]
            break
    assert isinstance(descriptor, property)



def test_java::numeric::expression::nr_is_not_abstract():
    assert not inspect.isabstract(java::Numeric::Expression::NR)


def test_java::numeric::expression::nr_constructor_exists():
    assert callable(java::Numeric::Expression::NR.__init__)


def test_java::numeric::expression::nr_constructor_args():
    sig = inspect.signature(java::Numeric::Expression::NR.__init__)
    params = list(sig.parameters.keys())
    assert "sinal_numeric" in params, "Missing parameter 'sinal_numeric'"

def test_java::numeric::expression::nr_has_sinal_numeric():
    assert hasattr(java::Numeric::Expression::NR, "sinal_numeric")
    descriptor = None
    for klass in java::Numeric::Expression::NR.__mro__:
        if "sinal_numeric" in klass.__dict__:
            descriptor = klass.__dict__["sinal_numeric"]
            break
    assert isinstance(descriptor, property)



def test_java::expression_is_not_abstract():
    assert not inspect.isabstract(java::Expression)


def test_java::expression_constructor_exists():
    assert callable(java::Expression.__init__)


def test_java::expression_constructor_args():
    sig = inspect.signature(java::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "null" in params, "Missing parameter 'null'"
    assert "this" in params, "Missing parameter 'this'"
    assert "super" in params, "Missing parameter 'super'"
    assert "name" in params, "Missing parameter 'name'"

def test_java::expression_has_null():
    assert hasattr(java::Expression, "null")
    descriptor = None
    for klass in java::Expression.__mro__:
        if "null" in klass.__dict__:
            descriptor = klass.__dict__["null"]
            break
    assert isinstance(descriptor, property)

def test_java::expression_has_this():
    assert hasattr(java::Expression, "this")
    descriptor = None
    for klass in java::Expression.__mro__:
        if "this" in klass.__dict__:
            descriptor = klass.__dict__["this"]
            break
    assert isinstance(descriptor, property)

def test_java::expression_has_super():
    assert hasattr(java::Expression, "super")
    descriptor = None
    for klass in java::Expression.__mro__:
        if "super" in klass.__dict__:
            descriptor = klass.__dict__["super"]
            break
    assert isinstance(descriptor, property)

def test_java::expression_has_name():
    assert hasattr(java::Expression, "name")
    descriptor = None
    for klass in java::Expression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java::variable::initializer_is_not_abstract():
    assert not inspect.isabstract(java::Variable::initializer)


def test_java::variable::initializer_constructor_exists():
    assert callable(java::Variable::initializer.__init__)


def test_java::variable::initializer_constructor_args():
    sig = inspect.signature(java::Variable::initializer.__init__)
    params = list(sig.parameters.keys())



def test_java::variable::declarator_is_not_abstract():
    assert not inspect.isabstract(java::Variable::declarator)


def test_java::variable::declarator_constructor_exists():
    assert callable(java::Variable::declarator.__init__)


def test_java::variable::declarator_constructor_args():
    sig = inspect.signature(java::Variable::declarator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java::variable::declarator_has_name():
    assert hasattr(java::Variable::declarator, "name")
    descriptor = None
    for klass in java::Variable::declarator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java::class::declaration_is_not_abstract():
    assert not inspect.isabstract(java::Class::declaration)


def test_java::class::declaration_constructor_exists():
    assert callable(java::Class::declaration.__init__)


def test_java::class::declaration_constructor_args():
    sig = inspect.signature(java::Class::declaration.__init__)
    params = list(sig.parameters.keys())
    assert "implements" in params, "Missing parameter 'implements'"
    assert "modifiers" in params, "Missing parameter 'modifiers'"
    assert "implement" in params, "Missing parameter 'implement'"
    assert "className" in params, "Missing parameter 'className'"
    assert "extend" in params, "Missing parameter 'extend'"

def test_java::class::declaration_has_implements():
    assert hasattr(java::Class::declaration, "implements")
    descriptor = None
    for klass in java::Class::declaration.__mro__:
        if "implements" in klass.__dict__:
            descriptor = klass.__dict__["implements"]
            break
    assert isinstance(descriptor, property)

def test_java::class::declaration_has_modifiers():
    assert hasattr(java::Class::declaration, "modifiers")
    descriptor = None
    for klass in java::Class::declaration.__mro__:
        if "modifiers" in klass.__dict__:
            descriptor = klass.__dict__["modifiers"]
            break
    assert isinstance(descriptor, property)

def test_java::class::declaration_has_implement():
    assert hasattr(java::Class::declaration, "implement")
    descriptor = None
    for klass in java::Class::declaration.__mro__:
        if "implement" in klass.__dict__:
            descriptor = klass.__dict__["implement"]
            break
    assert isinstance(descriptor, property)

def test_java::class::declaration_has_className():
    assert hasattr(java::Class::declaration, "className")
    descriptor = None
    for klass in java::Class::declaration.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)

def test_java::class::declaration_has_extend():
    assert hasattr(java::Class::declaration, "extend")
    descriptor = None
    for klass in java::Class::declaration.__mro__:
        if "extend" in klass.__dict__:
            descriptor = klass.__dict__["extend"]
            break
    assert isinstance(descriptor, property)



def test_java::field::declaration_is_not_abstract():
    assert not inspect.isabstract(java::Field::declaration)


def test_java::field::declaration_constructor_exists():
    assert callable(java::Field::declaration.__init__)


def test_java::field::declaration_constructor_args():
    sig = inspect.signature(java::Field::declaration.__init__)
    params = list(sig.parameters.keys())
    assert "debug" in params, "Missing parameter 'debug'"
    assert "doc" in params, "Missing parameter 'doc'"

def test_java::field::declaration_has_debug():
    assert hasattr(java::Field::declaration, "debug")
    descriptor = None
    for klass in java::Field::declaration.__mro__:
        if "debug" in klass.__dict__:
            descriptor = klass.__dict__["debug"]
            break
    assert isinstance(descriptor, property)

def test_java::field::declaration_has_doc():
    assert hasattr(java::Field::declaration, "doc")
    descriptor = None
    for klass in java::Field::declaration.__mro__:
        if "doc" in klass.__dict__:
            descriptor = klass.__dict__["doc"]
            break
    assert isinstance(descriptor, property)



def test_java::constructor::declaration_is_not_abstract():
    assert not inspect.isabstract(java::Constructor::declaration)


def test_java::constructor::declaration_constructor_exists():
    assert callable(java::Constructor::declaration.__init__)


def test_java::constructor::declaration_constructor_args():
    sig = inspect.signature(java::Constructor::declaration.__init__)
    params = list(sig.parameters.keys())
    assert "modifiers" in params, "Missing parameter 'modifiers'"
    assert "name" in params, "Missing parameter 'name'"

def test_java::constructor::declaration_has_modifiers():
    assert hasattr(java::Constructor::declaration, "modifiers")
    descriptor = None
    for klass in java::Constructor::declaration.__mro__:
        if "modifiers" in klass.__dict__:
            descriptor = klass.__dict__["modifiers"]
            break
    assert isinstance(descriptor, property)

def test_java::constructor::declaration_has_name():
    assert hasattr(java::Constructor::declaration, "name")
    descriptor = None
    for klass in java::Constructor::declaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java::parameter::list::method::call_is_not_abstract():
    assert not inspect.isabstract(java::Parameter::list::method::call)


def test_java::parameter::list::method::call_constructor_exists():
    assert callable(java::Parameter::list::method::call.__init__)


def test_java::parameter::list::method::call_constructor_args():
    sig = inspect.signature(java::Parameter::list::method::call.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "parameters" in params, "Missing parameter 'parameters'"

def test_java::parameter::list::method::call_has_name():
    assert hasattr(java::Parameter::list::method::call, "name")
    descriptor = None
    for klass in java::Parameter::list::method::call.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_java::parameter::list::method::call_has_parameters():
    assert hasattr(java::Parameter::list::method::call, "parameters")
    descriptor = None
    for klass in java::Parameter::list::method::call.__mro__:
        if "parameters" in klass.__dict__:
            descriptor = klass.__dict__["parameters"]
            break
    assert isinstance(descriptor, property)



def test_return::value_is_not_abstract():
    assert not inspect.isabstract(Return::value)


def test_return::value_constructor_exists():
    assert callable(Return::value.__init__)


def test_return::value_constructor_args():
    sig = inspect.signature(Return::value.__init__)
    params = list(sig.parameters.keys())



def test_java::method::call_is_not_abstract():
    assert not inspect.isabstract(java::Method::call)


def test_java::method::call_constructor_exists():
    assert callable(java::Method::call.__init__)


def test_java::method::call_constructor_args():
    sig = inspect.signature(java::Method::call.__init__)
    params = list(sig.parameters.keys())



def test_java::parameter::list_is_not_abstract():
    assert not inspect.isabstract(java::Parameter::list)


def test_java::parameter::list_constructor_exists():
    assert callable(java::Parameter::list.__init__)


def test_java::parameter::list_constructor_args():
    sig = inspect.signature(java::Parameter::list.__init__)
    params = list(sig.parameters.keys())



def test_java::type_is_not_abstract():
    assert not inspect.isabstract(java::Type)


def test_java::type_constructor_exists():
    assert callable(java::Type.__init__)


def test_java::type_constructor_args():
    sig = inspect.signature(java::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java::type_has_name():
    assert hasattr(java::Type, "name")
    descriptor = None
    for klass in java::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java::method::declaration_is_not_abstract():
    assert not inspect.isabstract(java::Method::declaration)


def test_java::method::declaration_constructor_exists():
    assert callable(java::Method::declaration.__init__)


def test_java::method::declaration_constructor_args():
    sig = inspect.signature(java::Method::declaration.__init__)
    params = list(sig.parameters.keys())
    assert "modifiers" in params, "Missing parameter 'modifiers'"
    assert "name" in params, "Missing parameter 'name'"
    assert "debug" in params, "Missing parameter 'debug'"

def test_java::method::declaration_has_modifiers():
    assert hasattr(java::Method::declaration, "modifiers")
    descriptor = None
    for klass in java::Method::declaration.__mro__:
        if "modifiers" in klass.__dict__:
            descriptor = klass.__dict__["modifiers"]
            break
    assert isinstance(descriptor, property)

def test_java::method::declaration_has_name():
    assert hasattr(java::Method::declaration, "name")
    descriptor = None
    for klass in java::Method::declaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_java::method::declaration_has_debug():
    assert hasattr(java::Method::declaration, "debug")
    descriptor = None
    for klass in java::Method::declaration.__mro__:
        if "debug" in klass.__dict__:
            descriptor = klass.__dict__["debug"]
            break
    assert isinstance(descriptor, property)



def test_java::interface::declaration_is_not_abstract():
    assert not inspect.isabstract(java::Interface::declaration)


def test_java::interface::declaration_constructor_exists():
    assert callable(java::Interface::declaration.__init__)


def test_java::interface::declaration_constructor_args():
    sig = inspect.signature(java::Interface::declaration.__init__)
    params = list(sig.parameters.keys())
    assert "modifiers" in params, "Missing parameter 'modifiers'"
    assert "extend" in params, "Missing parameter 'extend'"
    assert "extends" in params, "Missing parameter 'extends'"
    assert "interfaceName" in params, "Missing parameter 'interfaceName'"

def test_java::interface::declaration_has_modifiers():
    assert hasattr(java::Interface::declaration, "modifiers")
    descriptor = None
    for klass in java::Interface::declaration.__mro__:
        if "modifiers" in klass.__dict__:
            descriptor = klass.__dict__["modifiers"]
            break
    assert isinstance(descriptor, property)

def test_java::interface::declaration_has_extend():
    assert hasattr(java::Interface::declaration, "extend")
    descriptor = None
    for klass in java::Interface::declaration.__mro__:
        if "extend" in klass.__dict__:
            descriptor = klass.__dict__["extend"]
            break
    assert isinstance(descriptor, property)

def test_java::interface::declaration_has_extends():
    assert hasattr(java::Interface::declaration, "extends")
    descriptor = None
    for klass in java::Interface::declaration.__mro__:
        if "extends" in klass.__dict__:
            descriptor = klass.__dict__["extends"]
            break
    assert isinstance(descriptor, property)

def test_java::interface::declaration_has_interfaceName():
    assert hasattr(java::Interface::declaration, "interfaceName")
    descriptor = None
    for klass in java::Interface::declaration.__mro__:
        if "interfaceName" in klass.__dict__:
            descriptor = klass.__dict__["interfaceName"]
            break
    assert isinstance(descriptor, property)



def test_java::eobject_is_not_abstract():
    assert not inspect.isabstract(java::EObject)


def test_java::eobject_constructor_exists():
    assert callable(java::EObject.__init__)


def test_java::eobject_constructor_args():
    sig = inspect.signature(java::EObject.__init__)
    params = list(sig.parameters.keys())



def test_java::type::declaration_is_not_abstract():
    assert not inspect.isabstract(java::Type::declaration)


def test_java::type::declaration_constructor_exists():
    assert callable(java::Type::declaration.__init__)


def test_java::type::declaration_constructor_args():
    sig = inspect.signature(java::Type::declaration.__init__)
    params = list(sig.parameters.keys())
    assert "doc" in params, "Missing parameter 'doc'"

def test_java::type::declaration_has_doc():
    assert hasattr(java::Type::declaration, "doc")
    descriptor = None
    for klass in java::Type::declaration.__mro__:
        if "doc" in klass.__dict__:
            descriptor = klass.__dict__["doc"]
            break
    assert isinstance(descriptor, property)



def test_java::import::statement_is_not_abstract():
    assert not inspect.isabstract(java::Import::statement)


def test_java::import::statement_constructor_exists():
    assert callable(java::Import::statement.__init__)


def test_java::import::statement_constructor_args():
    sig = inspect.signature(java::Import::statement.__init__)
    params = list(sig.parameters.keys())
    assert "packagename" in params, "Missing parameter 'packagename'"
    assert "classname" in params, "Missing parameter 'classname'"

def test_java::import::statement_has_packagename():
    assert hasattr(java::Import::statement, "packagename")
    descriptor = None
    for klass in java::Import::statement.__mro__:
        if "packagename" in klass.__dict__:
            descriptor = klass.__dict__["packagename"]
            break
    assert isinstance(descriptor, property)

def test_java::import::statement_has_classname():
    assert hasattr(java::Import::statement, "classname")
    descriptor = None
    for klass in java::Import::statement.__mro__:
        if "classname" in klass.__dict__:
            descriptor = klass.__dict__["classname"]
            break
    assert isinstance(descriptor, property)



def test_java::package::statement_is_not_abstract():
    assert not inspect.isabstract(java::Package::statement)


def test_java::package::statement_constructor_exists():
    assert callable(java::Package::statement.__init__)


def test_java::package::statement_constructor_args():
    sig = inspect.signature(java::Package::statement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java::package::statement_has_name():
    assert hasattr(java::Package::statement, "name")
    descriptor = None
    for klass in java::Package::statement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java::compilation::unit_is_not_abstract():
    assert not inspect.isabstract(java::Compilation::unit)


def test_java::compilation::unit_constructor_exists():
    assert callable(java::Compilation::unit.__init__)


def test_java::compilation::unit_constructor_args():
    sig = inspect.signature(java::Compilation::unit.__init__)
    params = list(sig.parameters.keys())



def test_java::head_is_not_abstract():
    assert not inspect.isabstract(java::Head)


def test_java::head_constructor_exists():
    assert callable(java::Head.__init__)


def test_java::head_constructor_args():
    sig = inspect.signature(java::Head.__init__)
    params = list(sig.parameters.keys())



def test_java::return::value_is_not_abstract():
    assert not inspect.isabstract(java::Return::value)


def test_java::return::value_constructor_exists():
    assert callable(java::Return::value.__init__)


def test_java::return::value_constructor_args():
    sig = inspect.signature(java::Return::value.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java::return::value_has_name():
    assert hasattr(java::Return::value, "name")
    descriptor = None
    for klass in java::Return::value.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java::try::statement_is_not_abstract():
    assert not inspect.isabstract(java::Try::statement)


def test_java::try::statement_constructor_exists():
    assert callable(java::Try::statement.__init__)


def test_java::try::statement_constructor_args():
    sig = inspect.signature(java::Try::statement.__init__)
    params = list(sig.parameters.keys())
    assert "try_" in params, "Missing parameter 'try_'"
    assert "catchs" in params, "Missing parameter 'catchs'"
    assert "finally_" in params, "Missing parameter 'finally_'"

def test_java::try::statement_has_try_():
    assert hasattr(java::Try::statement, "try_")
    descriptor = None
    for klass in java::Try::statement.__mro__:
        if "try_" in klass.__dict__:
            descriptor = klass.__dict__["try_"]
            break
    assert isinstance(descriptor, property)

def test_java::try::statement_has_catchs():
    assert hasattr(java::Try::statement, "catchs")
    descriptor = None
    for klass in java::Try::statement.__mro__:
        if "catchs" in klass.__dict__:
            descriptor = klass.__dict__["catchs"]
            break
    assert isinstance(descriptor, property)

def test_java::try::statement_has_finally_():
    assert hasattr(java::Try::statement, "finally_")
    descriptor = None
    for klass in java::Try::statement.__mro__:
        if "finally_" in klass.__dict__:
            descriptor = klass.__dict__["finally_"]
            break
    assert isinstance(descriptor, property)



def test_java::switch::statement_is_not_abstract():
    assert not inspect.isabstract(java::Switch::Statement)


def test_java::switch::statement_constructor_exists():
    assert callable(java::Switch::Statement.__init__)


def test_java::switch::statement_constructor_args():
    sig = inspect.signature(java::Switch::Statement.__init__)
    params = list(sig.parameters.keys())



def test_java::for::statement_is_not_abstract():
    assert not inspect.isabstract(java::For::Statement)


def test_java::for::statement_constructor_exists():
    assert callable(java::For::Statement.__init__)


def test_java::for::statement_constructor_args():
    sig = inspect.signature(java::For::Statement.__init__)
    params = list(sig.parameters.keys())
    assert "pv" in params, "Missing parameter 'pv'"

def test_java::for::statement_has_pv():
    assert hasattr(java::For::Statement, "pv")
    descriptor = None
    for klass in java::For::Statement.__mro__:
        if "pv" in klass.__dict__:
            descriptor = klass.__dict__["pv"]
            break
    assert isinstance(descriptor, property)



def test_java::while::statement_is_not_abstract():
    assert not inspect.isabstract(java::While::Statement)


def test_java::while::statement_constructor_exists():
    assert callable(java::While::Statement.__init__)


def test_java::while::statement_constructor_args():
    sig = inspect.signature(java::While::Statement.__init__)
    params = list(sig.parameters.keys())



def test_java::do::statement_is_not_abstract():
    assert not inspect.isabstract(java::Do::Statement)


def test_java::do::statement_constructor_exists():
    assert callable(java::Do::Statement.__init__)


def test_java::do::statement_constructor_args():
    sig = inspect.signature(java::Do::Statement.__init__)
    params = list(sig.parameters.keys())



def test_java::if::statement_is_not_abstract():
    assert not inspect.isabstract(java::If::Statement)


def test_java::if::statement_constructor_exists():
    assert callable(java::If::Statement.__init__)


def test_java::if::statement_constructor_args():
    sig = inspect.signature(java::If::Statement.__init__)
    params = list(sig.parameters.keys())



def test_java::return::statement_is_not_abstract():
    assert not inspect.isabstract(java::Return::Statement)


def test_java::return::statement_constructor_exists():
    assert callable(java::Return::Statement.__init__)


def test_java::return::statement_constructor_args():
    sig = inspect.signature(java::Return::Statement.__init__)
    params = list(sig.parameters.keys())



def test_java::statement_is_not_abstract():
    assert not inspect.isabstract(java::Statement)


def test_java::statement_constructor_exists():
    assert callable(java::Statement.__init__)


def test_java::statement_constructor_args():
    sig = inspect.signature(java::Statement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java::statement_has_name():
    assert hasattr(java::Statement, "name")
    descriptor = None
    for klass in java::Statement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_java::statement::block_is_not_abstract():
    assert not inspect.isabstract(java::Statement::block)


def test_java::statement::block_constructor_exists():
    assert callable(java::Statement::block.__init__)


def test_java::statement::block_constructor_args():
    sig = inspect.signature(java::Statement::block.__init__)
    params = list(sig.parameters.keys())



def test_java::static::initializer_is_not_abstract():
    assert not inspect.isabstract(java::Static::initializer)


def test_java::static::initializer_constructor_exists():
    assert callable(java::Static::initializer.__init__)


def test_java::static::initializer_constructor_args():
    sig = inspect.signature(java::Static::initializer.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_java::static::initializer_has_static():
    assert hasattr(java::Static::initializer, "static")
    descriptor = None
    for klass in java::Static::initializer.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_java::arg::list_is_not_abstract():
    assert not inspect.isabstract(java::Arg::List)


def test_java::arg::list_constructor_exists():
    assert callable(java::Arg::List.__init__)


def test_java::arg::list_constructor_args():
    sig = inspect.signature(java::Arg::List.__init__)
    params = list(sig.parameters.keys())



def test_java::float::literal_is_not_abstract():
    assert not inspect.isabstract(java::Float::Literal)


def test_java::float::literal_constructor_exists():
    assert callable(java::Float::Literal.__init__)


def test_java::float::literal_constructor_args():
    sig = inspect.signature(java::Float::Literal.__init__)
    params = list(sig.parameters.keys())
    assert "decimalDigits1" in params, "Missing parameter 'decimalDigits1'"
    assert "exp" in params, "Missing parameter 'exp'"
    assert "decimalDigits2" in params, "Missing parameter 'decimalDigits2'"
    assert "floatTypeSufix" in params, "Missing parameter 'floatTypeSufix'"

def test_java::float::literal_has_decimalDigits1():
    assert hasattr(java::Float::Literal, "decimalDigits1")
    descriptor = None
    for klass in java::Float::Literal.__mro__:
        if "decimalDigits1" in klass.__dict__:
            descriptor = klass.__dict__["decimalDigits1"]
            break
    assert isinstance(descriptor, property)

def test_java::float::literal_has_exp():
    assert hasattr(java::Float::Literal, "exp")
    descriptor = None
    for klass in java::Float::Literal.__mro__:
        if "exp" in klass.__dict__:
            descriptor = klass.__dict__["exp"]
            break
    assert isinstance(descriptor, property)

def test_java::float::literal_has_decimalDigits2():
    assert hasattr(java::Float::Literal, "decimalDigits2")
    descriptor = None
    for klass in java::Float::Literal.__mro__:
        if "decimalDigits2" in klass.__dict__:
            descriptor = klass.__dict__["decimalDigits2"]
            break
    assert isinstance(descriptor, property)

def test_java::float::literal_has_floatTypeSufix():
    assert hasattr(java::Float::Literal, "floatTypeSufix")
    descriptor = None
    for klass in java::Float::Literal.__mro__:
        if "floatTypeSufix" in klass.__dict__:
            descriptor = klass.__dict__["floatTypeSufix"]
            break
    assert isinstance(descriptor, property)



def test_java::ampersand::rule_is_not_abstract():
    assert not inspect.isabstract(java::Ampersand::Rule)


def test_java::ampersand::rule_constructor_exists():
    assert callable(java::Ampersand::Rule.__init__)


def test_java::ampersand::rule_constructor_args():
    sig = inspect.signature(java::Ampersand::Rule.__init__)
    params = list(sig.parameters.keys())
    assert "a2" in params, "Missing parameter 'a2'"
    assert "a1" in params, "Missing parameter 'a1'"

def test_java::ampersand::rule_has_a2():
    assert hasattr(java::Ampersand::Rule, "a2")
    descriptor = None
    for klass in java::Ampersand::Rule.__mro__:
        if "a2" in klass.__dict__:
            descriptor = klass.__dict__["a2"]
            break
    assert isinstance(descriptor, property)

def test_java::ampersand::rule_has_a1():
    assert hasattr(java::Ampersand::Rule, "a1")
    descriptor = None
    for klass in java::Ampersand::Rule.__mro__:
        if "a1" in klass.__dict__:
            descriptor = klass.__dict__["a1"]
            break
    assert isinstance(descriptor, property)



def test_java::variable::declaration_is_not_abstract():
    assert not inspect.isabstract(java::Variable::declaration)


def test_java::variable::declaration_constructor_exists():
    assert callable(java::Variable::declaration.__init__)


def test_java::variable::declaration_constructor_args():
    sig = inspect.signature(java::Variable::declaration.__init__)
    params = list(sig.parameters.keys())
    assert "modifiers" in params, "Missing parameter 'modifiers'"

def test_java::variable::declaration_has_modifiers():
    assert hasattr(java::Variable::declaration, "modifiers")
    descriptor = None
    for klass in java::Variable::declaration.__mro__:
        if "modifiers" in klass.__dict__:
            descriptor = klass.__dict__["modifiers"]
            break
    assert isinstance(descriptor, property)



def test_java::parameter_is_not_abstract():
    assert not inspect.isabstract(java::Parameter)


def test_java::parameter_constructor_exists():
    assert callable(java::Parameter.__init__)


def test_java::parameter_constructor_args():
    sig = inspect.signature(java::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java::parameter_has_name():
    assert hasattr(java::Parameter, "name")
    descriptor = None
    for klass in java::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java::literal::expression_is_not_abstract():
    assert not inspect.isabstract(java::Literal::Expression)


def test_java::literal::expression_constructor_exists():
    assert callable(java::Literal::Expression.__init__)


def test_java::literal::expression_constructor_args():
    sig = inspect.signature(java::Literal::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "exp" in params, "Missing parameter 'exp'"
    assert "string" in params, "Missing parameter 'string'"
    assert "char" in params, "Missing parameter 'char'"
    assert "exp1" in params, "Missing parameter 'exp1'"

def test_java::literal::expression_has_exp():
    assert hasattr(java::Literal::Expression, "exp")
    descriptor = None
    for klass in java::Literal::Expression.__mro__:
        if "exp" in klass.__dict__:
            descriptor = klass.__dict__["exp"]
            break
    assert isinstance(descriptor, property)

def test_java::literal::expression_has_string():
    assert hasattr(java::Literal::Expression, "string")
    descriptor = None
    for klass in java::Literal::Expression.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)

def test_java::literal::expression_has_char():
    assert hasattr(java::Literal::Expression, "char")
    descriptor = None
    for klass in java::Literal::Expression.__mro__:
        if "char" in klass.__dict__:
            descriptor = klass.__dict__["char"]
            break
    assert isinstance(descriptor, property)

def test_java::literal::expression_has_exp1():
    assert hasattr(java::Literal::Expression, "exp1")
    descriptor = None
    for klass in java::Literal::Expression.__mro__:
        if "exp1" in klass.__dict__:
            descriptor = klass.__dict__["exp1"]
            break
    assert isinstance(descriptor, property)



def test_java::creating::expression_is_not_abstract():
    assert not inspect.isabstract(java::Creating::Expression)


def test_java::creating::expression_constructor_exists():
    assert callable(java::Creating::Expression.__init__)


def test_java::creating::expression_constructor_args():
    sig = inspect.signature(java::Creating::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "className" in params, "Missing parameter 'className'"
    assert "typeSpecifier" in params, "Missing parameter 'typeSpecifier'"

def test_java::creating::expression_has_className():
    assert hasattr(java::Creating::Expression, "className")
    descriptor = None
    for klass in java::Creating::Expression.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)

def test_java::creating::expression_has_typeSpecifier():
    assert hasattr(java::Creating::Expression, "typeSpecifier")
    descriptor = None
    for klass in java::Creating::Expression.__mro__:
        if "typeSpecifier" in klass.__dict__:
            descriptor = klass.__dict__["typeSpecifier"]
            break
    assert isinstance(descriptor, property)



def test_java::cast::expression_is_not_abstract():
    assert not inspect.isabstract(java::Cast::Expression)


def test_java::cast::expression_constructor_exists():
    assert callable(java::Cast::Expression.__init__)


def test_java::cast::expression_constructor_args():
    sig = inspect.signature(java::Cast::Expression.__init__)
    params = list(sig.parameters.keys())



def test_java::bit::expression::nr_is_not_abstract():
    assert not inspect.isabstract(java::Bit::Expression::NR)


def test_java::bit::expression::nr_constructor_exists():
    assert callable(java::Bit::Expression::NR.__init__)


def test_java::bit::expression::nr_constructor_args():
    sig = inspect.signature(java::Bit::Expression::NR.__init__)
    params = list(sig.parameters.keys())



def test_java::logical::expression::nr_is_not_abstract():
    assert not inspect.isabstract(java::Logical::Expression::NR)


def test_java::logical::expression::nr_constructor_exists():
    assert callable(java::Logical::Expression::NR.__init__)


def test_java::logical::expression::nr_constructor_args():
    sig = inspect.signature(java::Logical::Expression::NR.__init__)
    params = list(sig.parameters.keys())
    assert "false" in params, "Missing parameter 'false'"
    assert "true" in params, "Missing parameter 'true'"

def test_java::logical::expression::nr_has_false():
    assert hasattr(java::Logical::Expression::NR, "false")
    descriptor = None
    for klass in java::Logical::Expression::NR.__mro__:
        if "false" in klass.__dict__:
            descriptor = klass.__dict__["false"]
            break
    assert isinstance(descriptor, property)

def test_java::logical::expression::nr_has_true():
    assert hasattr(java::Logical::Expression::NR, "true")
    descriptor = None
    for klass in java::Logical::Expression::NR.__mro__:
        if "true" in klass.__dict__:
            descriptor = klass.__dict__["true"]
            break
    assert isinstance(descriptor, property)


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
java::Expression::aux_strategy = st.builds(
    java::Expression::aux,
    bitSign=
        safe_text,
    stringSign=
        safe_text,
    name=
        safe_text,
    numericSign=
        safe_text,
    testingSign=
        safe_text,
    logicalSign=
        safe_text,
    sgin=
        safe_text
)
java::Numeric::Expression::NR_strategy = st.builds(
    java::Numeric::Expression::NR,
    sinal_numeric=
        safe_text
)
java::Expression_strategy = st.builds(
    java::Expression,
    null=
        safe_text,
    this=
        safe_text,
    super=
        safe_text,
    name=
        safe_text
)
java::Variable::initializer_strategy = st.builds(
    java::Variable::initializer,
)
java::Variable::declarator_strategy = st.builds(
    java::Variable::declarator,
    name=
        safe_text
)
java::Class::declaration_strategy = st.builds(
    java::Class::declaration,
    implements=
        safe_text,
    modifiers=
        safe_text,
    implement=
        safe_text,
    className=
        safe_text,
    extend=
        safe_text
)
java::Field::declaration_strategy = st.builds(
    java::Field::declaration,
    debug=
        safe_text,
    doc=
        safe_text
)
java::Constructor::declaration_strategy = st.builds(
    java::Constructor::declaration,
    modifiers=
        safe_text,
    name=
        safe_text
)
java::Parameter::list::method::call_strategy = st.builds(
    java::Parameter::list::method::call,
    name=
        safe_text,
    parameters=
        safe_text
)
Return::value_strategy = st.builds(
    Return::value,
)
java::Method::call_strategy = st.builds(
    java::Method::call,
)
java::Parameter::list_strategy = st.builds(
    java::Parameter::list,
)
java::Type_strategy = st.builds(
    java::Type,
    name=
        safe_text
)
java::Method::declaration_strategy = st.builds(
    java::Method::declaration,
    modifiers=
        safe_text,
    name=
        safe_text,
    debug=
        safe_text
)
java::Interface::declaration_strategy = st.builds(
    java::Interface::declaration,
    modifiers=
        safe_text,
    extend=
        safe_text,
    extends=
        safe_text,
    interfaceName=
        safe_text
)
java::EObject_strategy = st.builds(
    java::EObject,
)
java::Type::declaration_strategy = st.builds(
    java::Type::declaration,
    doc=
        safe_text
)
java::Import::statement_strategy = st.builds(
    java::Import::statement,
    packagename=
        safe_text,
    classname=
        safe_text
)
java::Package::statement_strategy = st.builds(
    java::Package::statement,
    name=
        safe_text
)
java::Compilation::unit_strategy = st.builds(
    java::Compilation::unit,
)
java::Head_strategy = st.builds(
    java::Head,
)
java::Return::value_strategy = st.builds(
    java::Return::value,
    name=
        safe_text
)
java::Try::statement_strategy = st.builds(
    java::Try::statement,
    try_=
        safe_text,
    catchs=
        safe_text,
    finally_=
        safe_text
)
java::Switch::Statement_strategy = st.builds(
    java::Switch::Statement,
)
java::For::Statement_strategy = st.builds(
    java::For::Statement,
    pv=
        safe_text
)
java::While::Statement_strategy = st.builds(
    java::While::Statement,
)
java::Do::Statement_strategy = st.builds(
    java::Do::Statement,
)
java::If::Statement_strategy = st.builds(
    java::If::Statement,
)
java::Return::Statement_strategy = st.builds(
    java::Return::Statement,
)
java::Statement_strategy = st.builds(
    java::Statement,
    name=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
java::Statement::block_strategy = st.builds(
    java::Statement::block,
)
java::Static::initializer_strategy = st.builds(
    java::Static::initializer,
    static=
        safe_text
)
java::Arg::List_strategy = st.builds(
    java::Arg::List,
)
java::Float::Literal_strategy = st.builds(
    java::Float::Literal,
    decimalDigits1=
        st.integers(),
    exp=
        safe_text,
    decimalDigits2=
        st.integers(),
    floatTypeSufix=
        safe_text
)
java::Ampersand::Rule_strategy = st.builds(
    java::Ampersand::Rule,
    a2=
        safe_text,
    a1=
        safe_text
)
java::Variable::declaration_strategy = st.builds(
    java::Variable::declaration,
    modifiers=
        safe_text
)
java::Parameter_strategy = st.builds(
    java::Parameter,
    name=
        safe_text
)
java::Literal::Expression_strategy = st.builds(
    java::Literal::Expression,
    exp=
        safe_text,
    string=
        safe_text,
    char=
        safe_text,
    exp1=
        st.integers()
)
java::Creating::Expression_strategy = st.builds(
    java::Creating::Expression,
    className=
        safe_text,
    typeSpecifier=
        safe_text
)
java::Cast::Expression_strategy = st.builds(
    java::Cast::Expression,
)
java::Bit::Expression::NR_strategy = st.builds(
    java::Bit::Expression::NR,
)
java::Logical::Expression::NR_strategy = st.builds(
    java::Logical::Expression::NR,
    false=
        safe_text,
    true=
        safe_text
)

@given(instance=java::Expression::aux_strategy)
@settings(max_examples=50)
def test_java::expression::aux_instantiation(instance):
    assert isinstance(instance, java::Expression::aux)

@given(instance=java::Expression::aux_strategy)
def test_java::expression::aux_bitSign_type(instance):
    assert isinstance(instance.bitSign, str)


@given(instance=java::Expression::aux_strategy)
def test_java::expression::aux_bitSign_setter(instance):
    original = instance.bitSign
    instance.bitSign = original
    assert instance.bitSign == original

@given(instance=java::Expression::aux_strategy)
def test_java::expression::aux_stringSign_type(instance):
    assert isinstance(instance.stringSign, str)


@given(instance=java::Expression::aux_strategy)
def test_java::expression::aux_stringSign_setter(instance):
    original = instance.stringSign
    instance.stringSign = original
    assert instance.stringSign == original

@given(instance=java::Expression::aux_strategy)
def test_java::expression::aux_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=java::Expression::aux_strategy)
def test_java::expression::aux_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java::Expression::aux_strategy)
def test_java::expression::aux_numericSign_type(instance):
    assert isinstance(instance.numericSign, str)


@given(instance=java::Expression::aux_strategy)
def test_java::expression::aux_numericSign_setter(instance):
    original = instance.numericSign
    instance.numericSign = original
    assert instance.numericSign == original

@given(instance=java::Expression::aux_strategy)
def test_java::expression::aux_testingSign_type(instance):
    assert isinstance(instance.testingSign, str)


@given(instance=java::Expression::aux_strategy)
def test_java::expression::aux_testingSign_setter(instance):
    original = instance.testingSign
    instance.testingSign = original
    assert instance.testingSign == original

@given(instance=java::Expression::aux_strategy)
def test_java::expression::aux_logicalSign_type(instance):
    assert isinstance(instance.logicalSign, str)


@given(instance=java::Expression::aux_strategy)
def test_java::expression::aux_logicalSign_setter(instance):
    original = instance.logicalSign
    instance.logicalSign = original
    assert instance.logicalSign == original

@given(instance=java::Expression::aux_strategy)
def test_java::expression::aux_sgin_type(instance):
    assert isinstance(instance.sgin, str)


@given(instance=java::Expression::aux_strategy)
def test_java::expression::aux_sgin_setter(instance):
    original = instance.sgin
    instance.sgin = original
    assert instance.sgin == original

@given(instance=java::Numeric::Expression::NR_strategy)
@settings(max_examples=50)
def test_java::numeric::expression::nr_instantiation(instance):
    assert isinstance(instance, java::Numeric::Expression::NR)

@given(instance=java::Numeric::Expression::NR_strategy)
def test_java::numeric::expression::nr_sinal_numeric_type(instance):
    assert isinstance(instance.sinal_numeric, str)


@given(instance=java::Numeric::Expression::NR_strategy)
def test_java::numeric::expression::nr_sinal_numeric_setter(instance):
    original = instance.sinal_numeric
    instance.sinal_numeric = original
    assert instance.sinal_numeric == original

@given(instance=java::Expression_strategy)
@settings(max_examples=50)
def test_java::expression_instantiation(instance):
    assert isinstance(instance, java::Expression)

@given(instance=java::Expression_strategy)
def test_java::expression_null_type(instance):
    assert isinstance(instance.null, str)


@given(instance=java::Expression_strategy)
def test_java::expression_null_setter(instance):
    original = instance.null
    instance.null = original
    assert instance.null == original

@given(instance=java::Expression_strategy)
def test_java::expression_this_type(instance):
    assert isinstance(instance.this, str)


@given(instance=java::Expression_strategy)
def test_java::expression_this_setter(instance):
    original = instance.this
    instance.this = original
    assert instance.this == original

@given(instance=java::Expression_strategy)
def test_java::expression_super_type(instance):
    assert isinstance(instance.super, str)


@given(instance=java::Expression_strategy)
def test_java::expression_super_setter(instance):
    original = instance.super
    instance.super = original
    assert instance.super == original

@given(instance=java::Expression_strategy)
def test_java::expression_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=java::Expression_strategy)
def test_java::expression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java::Variable::initializer_strategy)
@settings(max_examples=50)
def test_java::variable::initializer_instantiation(instance):
    assert isinstance(instance, java::Variable::initializer)

@given(instance=java::Variable::declarator_strategy)
@settings(max_examples=50)
def test_java::variable::declarator_instantiation(instance):
    assert isinstance(instance, java::Variable::declarator)

@given(instance=java::Variable::declarator_strategy)
def test_java::variable::declarator_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=java::Variable::declarator_strategy)
def test_java::variable::declarator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java::Class::declaration_strategy)
@settings(max_examples=50)
def test_java::class::declaration_instantiation(instance):
    assert isinstance(instance, java::Class::declaration)

@given(instance=java::Class::declaration_strategy)
def test_java::class::declaration_implements_type(instance):
    assert isinstance(instance.implements, str)


@given(instance=java::Class::declaration_strategy)
def test_java::class::declaration_implements_setter(instance):
    original = instance.implements
    instance.implements = original
    assert instance.implements == original

@given(instance=java::Class::declaration_strategy)
def test_java::class::declaration_modifiers_type(instance):
    assert isinstance(instance.modifiers, str)


@given(instance=java::Class::declaration_strategy)
def test_java::class::declaration_modifiers_setter(instance):
    original = instance.modifiers
    instance.modifiers = original
    assert instance.modifiers == original

@given(instance=java::Class::declaration_strategy)
def test_java::class::declaration_implement_type(instance):
    assert isinstance(instance.implement, str)


@given(instance=java::Class::declaration_strategy)
def test_java::class::declaration_implement_setter(instance):
    original = instance.implement
    instance.implement = original
    assert instance.implement == original

@given(instance=java::Class::declaration_strategy)
def test_java::class::declaration_className_type(instance):
    assert isinstance(instance.className, str)


@given(instance=java::Class::declaration_strategy)
def test_java::class::declaration_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=java::Class::declaration_strategy)
def test_java::class::declaration_extend_type(instance):
    assert isinstance(instance.extend, str)


@given(instance=java::Class::declaration_strategy)
def test_java::class::declaration_extend_setter(instance):
    original = instance.extend
    instance.extend = original
    assert instance.extend == original

@given(instance=java::Field::declaration_strategy)
@settings(max_examples=50)
def test_java::field::declaration_instantiation(instance):
    assert isinstance(instance, java::Field::declaration)

@given(instance=java::Field::declaration_strategy)
def test_java::field::declaration_debug_type(instance):
    assert isinstance(instance.debug, str)


@given(instance=java::Field::declaration_strategy)
def test_java::field::declaration_debug_setter(instance):
    original = instance.debug
    instance.debug = original
    assert instance.debug == original

@given(instance=java::Field::declaration_strategy)
def test_java::field::declaration_doc_type(instance):
    assert isinstance(instance.doc, str)


@given(instance=java::Field::declaration_strategy)
def test_java::field::declaration_doc_setter(instance):
    original = instance.doc
    instance.doc = original
    assert instance.doc == original

@given(instance=java::Constructor::declaration_strategy)
@settings(max_examples=50)
def test_java::constructor::declaration_instantiation(instance):
    assert isinstance(instance, java::Constructor::declaration)

@given(instance=java::Constructor::declaration_strategy)
def test_java::constructor::declaration_modifiers_type(instance):
    assert isinstance(instance.modifiers, str)


@given(instance=java::Constructor::declaration_strategy)
def test_java::constructor::declaration_modifiers_setter(instance):
    original = instance.modifiers
    instance.modifiers = original
    assert instance.modifiers == original

@given(instance=java::Constructor::declaration_strategy)
def test_java::constructor::declaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=java::Constructor::declaration_strategy)
def test_java::constructor::declaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java::Parameter::list::method::call_strategy)
@settings(max_examples=50)
def test_java::parameter::list::method::call_instantiation(instance):
    assert isinstance(instance, java::Parameter::list::method::call)

@given(instance=java::Parameter::list::method::call_strategy)
def test_java::parameter::list::method::call_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=java::Parameter::list::method::call_strategy)
def test_java::parameter::list::method::call_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java::Parameter::list::method::call_strategy)
def test_java::parameter::list::method::call_parameters_type(instance):
    assert isinstance(instance.parameters, str)


@given(instance=java::Parameter::list::method::call_strategy)
def test_java::parameter::list::method::call_parameters_setter(instance):
    original = instance.parameters
    instance.parameters = original
    assert instance.parameters == original

@given(instance=Return::value_strategy)
@settings(max_examples=50)
def test_return::value_instantiation(instance):
    assert isinstance(instance, Return::value)

@given(instance=java::Method::call_strategy)
@settings(max_examples=50)
def test_java::method::call_instantiation(instance):
    assert isinstance(instance, java::Method::call)

@given(instance=java::Parameter::list_strategy)
@settings(max_examples=50)
def test_java::parameter::list_instantiation(instance):
    assert isinstance(instance, java::Parameter::list)

@given(instance=java::Type_strategy)
@settings(max_examples=50)
def test_java::type_instantiation(instance):
    assert isinstance(instance, java::Type)

@given(instance=java::Type_strategy)
def test_java::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=java::Type_strategy)
def test_java::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java::Method::declaration_strategy)
@settings(max_examples=50)
def test_java::method::declaration_instantiation(instance):
    assert isinstance(instance, java::Method::declaration)

@given(instance=java::Method::declaration_strategy)
def test_java::method::declaration_modifiers_type(instance):
    assert isinstance(instance.modifiers, str)


@given(instance=java::Method::declaration_strategy)
def test_java::method::declaration_modifiers_setter(instance):
    original = instance.modifiers
    instance.modifiers = original
    assert instance.modifiers == original

@given(instance=java::Method::declaration_strategy)
def test_java::method::declaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=java::Method::declaration_strategy)
def test_java::method::declaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java::Method::declaration_strategy)
def test_java::method::declaration_debug_type(instance):
    assert isinstance(instance.debug, str)


@given(instance=java::Method::declaration_strategy)
def test_java::method::declaration_debug_setter(instance):
    original = instance.debug
    instance.debug = original
    assert instance.debug == original

@given(instance=java::Interface::declaration_strategy)
@settings(max_examples=50)
def test_java::interface::declaration_instantiation(instance):
    assert isinstance(instance, java::Interface::declaration)

@given(instance=java::Interface::declaration_strategy)
def test_java::interface::declaration_modifiers_type(instance):
    assert isinstance(instance.modifiers, str)


@given(instance=java::Interface::declaration_strategy)
def test_java::interface::declaration_modifiers_setter(instance):
    original = instance.modifiers
    instance.modifiers = original
    assert instance.modifiers == original

@given(instance=java::Interface::declaration_strategy)
def test_java::interface::declaration_extend_type(instance):
    assert isinstance(instance.extend, str)


@given(instance=java::Interface::declaration_strategy)
def test_java::interface::declaration_extend_setter(instance):
    original = instance.extend
    instance.extend = original
    assert instance.extend == original

@given(instance=java::Interface::declaration_strategy)
def test_java::interface::declaration_extends_type(instance):
    assert isinstance(instance.extends, str)


@given(instance=java::Interface::declaration_strategy)
def test_java::interface::declaration_extends_setter(instance):
    original = instance.extends
    instance.extends = original
    assert instance.extends == original

@given(instance=java::Interface::declaration_strategy)
def test_java::interface::declaration_interfaceName_type(instance):
    assert isinstance(instance.interfaceName, str)


@given(instance=java::Interface::declaration_strategy)
def test_java::interface::declaration_interfaceName_setter(instance):
    original = instance.interfaceName
    instance.interfaceName = original
    assert instance.interfaceName == original

@given(instance=java::EObject_strategy)
@settings(max_examples=50)
def test_java::eobject_instantiation(instance):
    assert isinstance(instance, java::EObject)

@given(instance=java::Type::declaration_strategy)
@settings(max_examples=50)
def test_java::type::declaration_instantiation(instance):
    assert isinstance(instance, java::Type::declaration)

@given(instance=java::Type::declaration_strategy)
def test_java::type::declaration_doc_type(instance):
    assert isinstance(instance.doc, str)


@given(instance=java::Type::declaration_strategy)
def test_java::type::declaration_doc_setter(instance):
    original = instance.doc
    instance.doc = original
    assert instance.doc == original

@given(instance=java::Import::statement_strategy)
@settings(max_examples=50)
def test_java::import::statement_instantiation(instance):
    assert isinstance(instance, java::Import::statement)

@given(instance=java::Import::statement_strategy)
def test_java::import::statement_packagename_type(instance):
    assert isinstance(instance.packagename, str)


@given(instance=java::Import::statement_strategy)
def test_java::import::statement_packagename_setter(instance):
    original = instance.packagename
    instance.packagename = original
    assert instance.packagename == original

@given(instance=java::Import::statement_strategy)
def test_java::import::statement_classname_type(instance):
    assert isinstance(instance.classname, str)


@given(instance=java::Import::statement_strategy)
def test_java::import::statement_classname_setter(instance):
    original = instance.classname
    instance.classname = original
    assert instance.classname == original

@given(instance=java::Package::statement_strategy)
@settings(max_examples=50)
def test_java::package::statement_instantiation(instance):
    assert isinstance(instance, java::Package::statement)

@given(instance=java::Package::statement_strategy)
def test_java::package::statement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=java::Package::statement_strategy)
def test_java::package::statement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java::Compilation::unit_strategy)
@settings(max_examples=50)
def test_java::compilation::unit_instantiation(instance):
    assert isinstance(instance, java::Compilation::unit)

@given(instance=java::Head_strategy)
@settings(max_examples=50)
def test_java::head_instantiation(instance):
    assert isinstance(instance, java::Head)

@given(instance=java::Return::value_strategy)
@settings(max_examples=50)
def test_java::return::value_instantiation(instance):
    assert isinstance(instance, java::Return::value)

@given(instance=java::Return::value_strategy)
def test_java::return::value_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=java::Return::value_strategy)
def test_java::return::value_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java::Try::statement_strategy)
@settings(max_examples=50)
def test_java::try::statement_instantiation(instance):
    assert isinstance(instance, java::Try::statement)

@given(instance=java::Try::statement_strategy)
def test_java::try::statement_try__type(instance):
    assert isinstance(instance.try_, str)


@given(instance=java::Try::statement_strategy)
def test_java::try::statement_try__setter(instance):
    original = instance.try_
    instance.try_ = original
    assert instance.try_ == original

@given(instance=java::Try::statement_strategy)
def test_java::try::statement_catchs_type(instance):
    assert isinstance(instance.catchs, str)


@given(instance=java::Try::statement_strategy)
def test_java::try::statement_catchs_setter(instance):
    original = instance.catchs
    instance.catchs = original
    assert instance.catchs == original

@given(instance=java::Try::statement_strategy)
def test_java::try::statement_finally__type(instance):
    assert isinstance(instance.finally_, str)


@given(instance=java::Try::statement_strategy)
def test_java::try::statement_finally__setter(instance):
    original = instance.finally_
    instance.finally_ = original
    assert instance.finally_ == original

@given(instance=java::Switch::Statement_strategy)
@settings(max_examples=50)
def test_java::switch::statement_instantiation(instance):
    assert isinstance(instance, java::Switch::Statement)

@given(instance=java::For::Statement_strategy)
@settings(max_examples=50)
def test_java::for::statement_instantiation(instance):
    assert isinstance(instance, java::For::Statement)

@given(instance=java::For::Statement_strategy)
def test_java::for::statement_pv_type(instance):
    assert isinstance(instance.pv, str)


@given(instance=java::For::Statement_strategy)
def test_java::for::statement_pv_setter(instance):
    original = instance.pv
    instance.pv = original
    assert instance.pv == original

@given(instance=java::While::Statement_strategy)
@settings(max_examples=50)
def test_java::while::statement_instantiation(instance):
    assert isinstance(instance, java::While::Statement)

@given(instance=java::Do::Statement_strategy)
@settings(max_examples=50)
def test_java::do::statement_instantiation(instance):
    assert isinstance(instance, java::Do::Statement)

@given(instance=java::If::Statement_strategy)
@settings(max_examples=50)
def test_java::if::statement_instantiation(instance):
    assert isinstance(instance, java::If::Statement)

@given(instance=java::Return::Statement_strategy)
@settings(max_examples=50)
def test_java::return::statement_instantiation(instance):
    assert isinstance(instance, java::Return::Statement)

@given(instance=java::Statement_strategy)
@settings(max_examples=50)
def test_java::statement_instantiation(instance):
    assert isinstance(instance, java::Statement)

@given(instance=java::Statement_strategy)
def test_java::statement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=java::Statement_strategy)
def test_java::statement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=java::Statement::block_strategy)
@settings(max_examples=50)
def test_java::statement::block_instantiation(instance):
    assert isinstance(instance, java::Statement::block)

@given(instance=java::Static::initializer_strategy)
@settings(max_examples=50)
def test_java::static::initializer_instantiation(instance):
    assert isinstance(instance, java::Static::initializer)

@given(instance=java::Static::initializer_strategy)
def test_java::static::initializer_static_type(instance):
    assert isinstance(instance.static, str)


@given(instance=java::Static::initializer_strategy)
def test_java::static::initializer_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=java::Arg::List_strategy)
@settings(max_examples=50)
def test_java::arg::list_instantiation(instance):
    assert isinstance(instance, java::Arg::List)

@given(instance=java::Float::Literal_strategy)
@settings(max_examples=50)
def test_java::float::literal_instantiation(instance):
    assert isinstance(instance, java::Float::Literal)

@given(instance=java::Float::Literal_strategy)
def test_java::float::literal_decimalDigits1_type(instance):
    assert isinstance(instance.decimalDigits1, int)


@given(instance=java::Float::Literal_strategy)
def test_java::float::literal_decimalDigits1_setter(instance):
    original = instance.decimalDigits1
    instance.decimalDigits1 = original
    assert instance.decimalDigits1 == original

@given(instance=java::Float::Literal_strategy)
def test_java::float::literal_exp_type(instance):
    assert isinstance(instance.exp, str)


@given(instance=java::Float::Literal_strategy)
def test_java::float::literal_exp_setter(instance):
    original = instance.exp
    instance.exp = original
    assert instance.exp == original

@given(instance=java::Float::Literal_strategy)
def test_java::float::literal_decimalDigits2_type(instance):
    assert isinstance(instance.decimalDigits2, int)


@given(instance=java::Float::Literal_strategy)
def test_java::float::literal_decimalDigits2_setter(instance):
    original = instance.decimalDigits2
    instance.decimalDigits2 = original
    assert instance.decimalDigits2 == original

@given(instance=java::Float::Literal_strategy)
def test_java::float::literal_floatTypeSufix_type(instance):
    assert isinstance(instance.floatTypeSufix, str)


@given(instance=java::Float::Literal_strategy)
def test_java::float::literal_floatTypeSufix_setter(instance):
    original = instance.floatTypeSufix
    instance.floatTypeSufix = original
    assert instance.floatTypeSufix == original

@given(instance=java::Ampersand::Rule_strategy)
@settings(max_examples=50)
def test_java::ampersand::rule_instantiation(instance):
    assert isinstance(instance, java::Ampersand::Rule)

@given(instance=java::Ampersand::Rule_strategy)
def test_java::ampersand::rule_a2_type(instance):
    assert isinstance(instance.a2, str)


@given(instance=java::Ampersand::Rule_strategy)
def test_java::ampersand::rule_a2_setter(instance):
    original = instance.a2
    instance.a2 = original
    assert instance.a2 == original

@given(instance=java::Ampersand::Rule_strategy)
def test_java::ampersand::rule_a1_type(instance):
    assert isinstance(instance.a1, str)


@given(instance=java::Ampersand::Rule_strategy)
def test_java::ampersand::rule_a1_setter(instance):
    original = instance.a1
    instance.a1 = original
    assert instance.a1 == original

@given(instance=java::Variable::declaration_strategy)
@settings(max_examples=50)
def test_java::variable::declaration_instantiation(instance):
    assert isinstance(instance, java::Variable::declaration)

@given(instance=java::Variable::declaration_strategy)
def test_java::variable::declaration_modifiers_type(instance):
    assert isinstance(instance.modifiers, str)


@given(instance=java::Variable::declaration_strategy)
def test_java::variable::declaration_modifiers_setter(instance):
    original = instance.modifiers
    instance.modifiers = original
    assert instance.modifiers == original

@given(instance=java::Parameter_strategy)
@settings(max_examples=50)
def test_java::parameter_instantiation(instance):
    assert isinstance(instance, java::Parameter)

@given(instance=java::Parameter_strategy)
def test_java::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=java::Parameter_strategy)
def test_java::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java::Literal::Expression_strategy)
@settings(max_examples=50)
def test_java::literal::expression_instantiation(instance):
    assert isinstance(instance, java::Literal::Expression)

@given(instance=java::Literal::Expression_strategy)
def test_java::literal::expression_exp_type(instance):
    assert isinstance(instance.exp, str)


@given(instance=java::Literal::Expression_strategy)
def test_java::literal::expression_exp_setter(instance):
    original = instance.exp
    instance.exp = original
    assert instance.exp == original

@given(instance=java::Literal::Expression_strategy)
def test_java::literal::expression_string_type(instance):
    assert isinstance(instance.string, str)


@given(instance=java::Literal::Expression_strategy)
def test_java::literal::expression_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=java::Literal::Expression_strategy)
def test_java::literal::expression_char_type(instance):
    assert isinstance(instance.char, str)


@given(instance=java::Literal::Expression_strategy)
def test_java::literal::expression_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original

@given(instance=java::Literal::Expression_strategy)
def test_java::literal::expression_exp1_type(instance):
    assert isinstance(instance.exp1, int)


@given(instance=java::Literal::Expression_strategy)
def test_java::literal::expression_exp1_setter(instance):
    original = instance.exp1
    instance.exp1 = original
    assert instance.exp1 == original

@given(instance=java::Creating::Expression_strategy)
@settings(max_examples=50)
def test_java::creating::expression_instantiation(instance):
    assert isinstance(instance, java::Creating::Expression)

@given(instance=java::Creating::Expression_strategy)
def test_java::creating::expression_className_type(instance):
    assert isinstance(instance.className, str)


@given(instance=java::Creating::Expression_strategy)
def test_java::creating::expression_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=java::Creating::Expression_strategy)
def test_java::creating::expression_typeSpecifier_type(instance):
    assert isinstance(instance.typeSpecifier, str)


@given(instance=java::Creating::Expression_strategy)
def test_java::creating::expression_typeSpecifier_setter(instance):
    original = instance.typeSpecifier
    instance.typeSpecifier = original
    assert instance.typeSpecifier == original

@given(instance=java::Cast::Expression_strategy)
@settings(max_examples=50)
def test_java::cast::expression_instantiation(instance):
    assert isinstance(instance, java::Cast::Expression)

@given(instance=java::Bit::Expression::NR_strategy)
@settings(max_examples=50)
def test_java::bit::expression::nr_instantiation(instance):
    assert isinstance(instance, java::Bit::Expression::NR)

@given(instance=java::Logical::Expression::NR_strategy)
@settings(max_examples=50)
def test_java::logical::expression::nr_instantiation(instance):
    assert isinstance(instance, java::Logical::Expression::NR)

@given(instance=java::Logical::Expression::NR_strategy)
def test_java::logical::expression::nr_false_type(instance):
    assert isinstance(instance.false, str)


@given(instance=java::Logical::Expression::NR_strategy)
def test_java::logical::expression::nr_false_setter(instance):
    original = instance.false
    instance.false = original
    assert instance.false == original

@given(instance=java::Logical::Expression::NR_strategy)
def test_java::logical::expression::nr_true_type(instance):
    assert isinstance(instance.true, str)


@given(instance=java::Logical::Expression::NR_strategy)
def test_java::logical::expression::nr_true_setter(instance):
    original = instance.true
    instance.true = original
    assert instance.true == original
