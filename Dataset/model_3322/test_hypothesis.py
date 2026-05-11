import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    exp::aux,
    simpleJava::package::name::aux,
    variable::declarator,
    simpleJava::literal::expression,
    simpleJava::bit::expression,
    simpleJava::numeric::expression,
    simpleJava::logical::expression,
    expression::aux,
    expression,
    simpleJava::exp::aux,
    simpleJava::newBlock,
    simpleJava::type::specifier,
    simpleJava::creating::aux,
    simpleJava::creating::expression,
    creating::aux,
    simpleJava::aux,
    simpleJava::mais::aux,
    simpleJava::arglist,
    simpleJava::expression::aux,
    newBlock,
    simpleJava::variable::initializer,
    simpleJava::variable::declarator,
    simpleJava::switch::statement,
    simpleJava::try::statement,
    simpleJava::for::statement,
    simpleJava::while::statement,
    simpleJava::parameter,
    simpleJava::statement::block,
    simpleJava::parameter::list,
    simpleJava::type,
    simpleJava::static::initializer,
    simpleJava::variable::declaration,
    simpleJava::constructor::declaration,
    simpleJava::method::declaration,
    simpleJava::field::declaration,
    simpleJava::do::statement,
    simpleJava::if::statement,
    simpleJava::expression,
    simpleJava::statement,
    simpleJava::type::declaration,
    simpleJava::import::statement,
    simpleJava::package::statement,
    Model,
    simpleJava::compilation::unit,
    simpleJava::Model,
    simpleJava::MODIFIER,
    type::declaration,
    simpleJava::doc::comment,
    simpleJava::interface::declaration,
    simpleJava::class::declaration,
    simpleJava::name,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_exp::aux_is_not_abstract():
    assert not inspect.isabstract(exp::aux)


def test_exp::aux_constructor_exists():
    assert callable(exp::aux.__init__)


def test_exp::aux_constructor_args():
    sig = inspect.signature(exp::aux.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::package::name::aux_is_not_abstract():
    assert not inspect.isabstract(simpleJava::package::name::aux)


def test_simplejava::package::name::aux_constructor_exists():
    assert callable(simpleJava::package::name::aux.__init__)


def test_simplejava::package::name::aux_constructor_args():
    sig = inspect.signature(simpleJava::package::name::aux.__init__)
    params = list(sig.parameters.keys())
    assert "nomePacote" in params, "Missing parameter 'nomePacote'"

def test_simplejava::package::name::aux_has_nomePacote():
    assert hasattr(simpleJava::package::name::aux, "nomePacote")
    descriptor = None
    for klass in simpleJava::package::name::aux.__mro__:
        if "nomePacote" in klass.__dict__:
            descriptor = klass.__dict__["nomePacote"]
            break
    assert isinstance(descriptor, property)



def test_variable::declarator_is_not_abstract():
    assert not inspect.isabstract(variable::declarator)


def test_variable::declarator_constructor_exists():
    assert callable(variable::declarator.__init__)


def test_variable::declarator_constructor_args():
    sig = inspect.signature(variable::declarator.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::literal::expression_is_not_abstract():
    assert not inspect.isabstract(simpleJava::literal::expression)


def test_simplejava::literal::expression_constructor_exists():
    assert callable(simpleJava::literal::expression.__init__)


def test_simplejava::literal::expression_constructor_args():
    sig = inspect.signature(simpleJava::literal::expression.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"
    assert "inteiro" in params, "Missing parameter 'inteiro'"
    assert "l_float" in params, "Missing parameter 'l_float'"
    assert "decimal" in params, "Missing parameter 'decimal'"

def test_simplejava::literal::expression_has_string():
    assert hasattr(simpleJava::literal::expression, "string")
    descriptor = None
    for klass in simpleJava::literal::expression.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)

def test_simplejava::literal::expression_has_inteiro():
    assert hasattr(simpleJava::literal::expression, "inteiro")
    descriptor = None
    for klass in simpleJava::literal::expression.__mro__:
        if "inteiro" in klass.__dict__:
            descriptor = klass.__dict__["inteiro"]
            break
    assert isinstance(descriptor, property)

def test_simplejava::literal::expression_has_l_float():
    assert hasattr(simpleJava::literal::expression, "l_float")
    descriptor = None
    for klass in simpleJava::literal::expression.__mro__:
        if "l_float" in klass.__dict__:
            descriptor = klass.__dict__["l_float"]
            break
    assert isinstance(descriptor, property)

def test_simplejava::literal::expression_has_decimal():
    assert hasattr(simpleJava::literal::expression, "decimal")
    descriptor = None
    for klass in simpleJava::literal::expression.__mro__:
        if "decimal" in klass.__dict__:
            descriptor = klass.__dict__["decimal"]
            break
    assert isinstance(descriptor, property)



def test_simplejava::bit::expression_is_not_abstract():
    assert not inspect.isabstract(simpleJava::bit::expression)


def test_simplejava::bit::expression_constructor_exists():
    assert callable(simpleJava::bit::expression.__init__)


def test_simplejava::bit::expression_constructor_args():
    sig = inspect.signature(simpleJava::bit::expression.__init__)
    params = list(sig.parameters.keys())
    assert "operador" in params, "Missing parameter 'operador'"

def test_simplejava::bit::expression_has_operador():
    assert hasattr(simpleJava::bit::expression, "operador")
    descriptor = None
    for klass in simpleJava::bit::expression.__mro__:
        if "operador" in klass.__dict__:
            descriptor = klass.__dict__["operador"]
            break
    assert isinstance(descriptor, property)



def test_simplejava::numeric::expression_is_not_abstract():
    assert not inspect.isabstract(simpleJava::numeric::expression)


def test_simplejava::numeric::expression_constructor_exists():
    assert callable(simpleJava::numeric::expression.__init__)


def test_simplejava::numeric::expression_constructor_args():
    sig = inspect.signature(simpleJava::numeric::expression.__init__)
    params = list(sig.parameters.keys())
    assert "operador" in params, "Missing parameter 'operador'"

def test_simplejava::numeric::expression_has_operador():
    assert hasattr(simpleJava::numeric::expression, "operador")
    descriptor = None
    for klass in simpleJava::numeric::expression.__mro__:
        if "operador" in klass.__dict__:
            descriptor = klass.__dict__["operador"]
            break
    assert isinstance(descriptor, property)



def test_simplejava::logical::expression_is_not_abstract():
    assert not inspect.isabstract(simpleJava::logical::expression)


def test_simplejava::logical::expression_constructor_exists():
    assert callable(simpleJava::logical::expression.__init__)


def test_simplejava::logical::expression_constructor_args():
    sig = inspect.signature(simpleJava::logical::expression.__init__)
    params = list(sig.parameters.keys())
    assert "operador" in params, "Missing parameter 'operador'"

def test_simplejava::logical::expression_has_operador():
    assert hasattr(simpleJava::logical::expression, "operador")
    descriptor = None
    for klass in simpleJava::logical::expression.__mro__:
        if "operador" in klass.__dict__:
            descriptor = klass.__dict__["operador"]
            break
    assert isinstance(descriptor, property)



def test_expression::aux_is_not_abstract():
    assert not inspect.isabstract(expression::aux)


def test_expression::aux_constructor_exists():
    assert callable(expression::aux.__init__)


def test_expression::aux_constructor_args():
    sig = inspect.signature(expression::aux.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(expression)


def test_expression_constructor_exists():
    assert callable(expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(expression.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::exp::aux_is_not_abstract():
    assert not inspect.isabstract(simpleJava::exp::aux)


def test_simplejava::exp::aux_constructor_exists():
    assert callable(simpleJava::exp::aux.__init__)


def test_simplejava::exp::aux_constructor_args():
    sig = inspect.signature(simpleJava::exp::aux.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::newblock_is_not_abstract():
    assert not inspect.isabstract(simpleJava::newBlock)


def test_simplejava::newblock_constructor_exists():
    assert callable(simpleJava::newBlock.__init__)


def test_simplejava::newblock_constructor_args():
    sig = inspect.signature(simpleJava::newBlock.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::type::specifier_is_not_abstract():
    assert not inspect.isabstract(simpleJava::type::specifier)


def test_simplejava::type::specifier_constructor_exists():
    assert callable(simpleJava::type::specifier.__init__)


def test_simplejava::type::specifier_constructor_args():
    sig = inspect.signature(simpleJava::type::specifier.__init__)
    params = list(sig.parameters.keys())
    assert "nome" in params, "Missing parameter 'nome'"

def test_simplejava::type::specifier_has_nome():
    assert hasattr(simpleJava::type::specifier, "nome")
    descriptor = None
    for klass in simpleJava::type::specifier.__mro__:
        if "nome" in klass.__dict__:
            descriptor = klass.__dict__["nome"]
            break
    assert isinstance(descriptor, property)



def test_simplejava::creating::aux_is_not_abstract():
    assert not inspect.isabstract(simpleJava::creating::aux)


def test_simplejava::creating::aux_constructor_exists():
    assert callable(simpleJava::creating::aux.__init__)


def test_simplejava::creating::aux_constructor_args():
    sig = inspect.signature(simpleJava::creating::aux.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::creating::expression_is_not_abstract():
    assert not inspect.isabstract(simpleJava::creating::expression)


def test_simplejava::creating::expression_constructor_exists():
    assert callable(simpleJava::creating::expression.__init__)


def test_simplejava::creating::expression_constructor_args():
    sig = inspect.signature(simpleJava::creating::expression.__init__)
    params = list(sig.parameters.keys())



def test_creating::aux_is_not_abstract():
    assert not inspect.isabstract(creating::aux)


def test_creating::aux_constructor_exists():
    assert callable(creating::aux.__init__)


def test_creating::aux_constructor_args():
    sig = inspect.signature(creating::aux.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::aux_is_not_abstract():
    assert not inspect.isabstract(simpleJava::aux)


def test_simplejava::aux_constructor_exists():
    assert callable(simpleJava::aux.__init__)


def test_simplejava::aux_constructor_args():
    sig = inspect.signature(simpleJava::aux.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::mais::aux_is_not_abstract():
    assert not inspect.isabstract(simpleJava::mais::aux)


def test_simplejava::mais::aux_constructor_exists():
    assert callable(simpleJava::mais::aux.__init__)


def test_simplejava::mais::aux_constructor_args():
    sig = inspect.signature(simpleJava::mais::aux.__init__)
    params = list(sig.parameters.keys())
    assert "operador" in params, "Missing parameter 'operador'"

def test_simplejava::mais::aux_has_operador():
    assert hasattr(simpleJava::mais::aux, "operador")
    descriptor = None
    for klass in simpleJava::mais::aux.__mro__:
        if "operador" in klass.__dict__:
            descriptor = klass.__dict__["operador"]
            break
    assert isinstance(descriptor, property)



def test_simplejava::arglist_is_not_abstract():
    assert not inspect.isabstract(simpleJava::arglist)


def test_simplejava::arglist_constructor_exists():
    assert callable(simpleJava::arglist.__init__)


def test_simplejava::arglist_constructor_args():
    sig = inspect.signature(simpleJava::arglist.__init__)
    params = list(sig.parameters.keys())
    assert "nomeParametro" in params, "Missing parameter 'nomeParametro'"

def test_simplejava::arglist_has_nomeParametro():
    assert hasattr(simpleJava::arglist, "nomeParametro")
    descriptor = None
    for klass in simpleJava::arglist.__mro__:
        if "nomeParametro" in klass.__dict__:
            descriptor = klass.__dict__["nomeParametro"]
            break
    assert isinstance(descriptor, property)



def test_simplejava::expression::aux_is_not_abstract():
    assert not inspect.isabstract(simpleJava::expression::aux)


def test_simplejava::expression::aux_constructor_exists():
    assert callable(simpleJava::expression::aux.__init__)


def test_simplejava::expression::aux_constructor_args():
    sig = inspect.signature(simpleJava::expression::aux.__init__)
    params = list(sig.parameters.keys())
    assert "operador" in params, "Missing parameter 'operador'"

def test_simplejava::expression::aux_has_operador():
    assert hasattr(simpleJava::expression::aux, "operador")
    descriptor = None
    for klass in simpleJava::expression::aux.__mro__:
        if "operador" in klass.__dict__:
            descriptor = klass.__dict__["operador"]
            break
    assert isinstance(descriptor, property)



def test_newblock_is_not_abstract():
    assert not inspect.isabstract(newBlock)


def test_newblock_constructor_exists():
    assert callable(newBlock.__init__)


def test_newblock_constructor_args():
    sig = inspect.signature(newBlock.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::variable::initializer_is_not_abstract():
    assert not inspect.isabstract(simpleJava::variable::initializer)


def test_simplejava::variable::initializer_constructor_exists():
    assert callable(simpleJava::variable::initializer.__init__)


def test_simplejava::variable::initializer_constructor_args():
    sig = inspect.signature(simpleJava::variable::initializer.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::variable::declarator_is_not_abstract():
    assert not inspect.isabstract(simpleJava::variable::declarator)


def test_simplejava::variable::declarator_constructor_exists():
    assert callable(simpleJava::variable::declarator.__init__)


def test_simplejava::variable::declarator_constructor_args():
    sig = inspect.signature(simpleJava::variable::declarator.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"
    assert "nomeVariavel" in params, "Missing parameter 'nomeVariavel'"

def test_simplejava::variable::declarator_has_op():
    assert hasattr(simpleJava::variable::declarator, "op")
    descriptor = None
    for klass in simpleJava::variable::declarator.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)

def test_simplejava::variable::declarator_has_nomeVariavel():
    assert hasattr(simpleJava::variable::declarator, "nomeVariavel")
    descriptor = None
    for klass in simpleJava::variable::declarator.__mro__:
        if "nomeVariavel" in klass.__dict__:
            descriptor = klass.__dict__["nomeVariavel"]
            break
    assert isinstance(descriptor, property)



def test_simplejava::switch::statement_is_not_abstract():
    assert not inspect.isabstract(simpleJava::switch::statement)


def test_simplejava::switch::statement_constructor_exists():
    assert callable(simpleJava::switch::statement.__init__)


def test_simplejava::switch::statement_constructor_args():
    sig = inspect.signature(simpleJava::switch::statement.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::try::statement_is_not_abstract():
    assert not inspect.isabstract(simpleJava::try::statement)


def test_simplejava::try::statement_constructor_exists():
    assert callable(simpleJava::try::statement.__init__)


def test_simplejava::try::statement_constructor_args():
    sig = inspect.signature(simpleJava::try::statement.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::for::statement_is_not_abstract():
    assert not inspect.isabstract(simpleJava::for::statement)


def test_simplejava::for::statement_constructor_exists():
    assert callable(simpleJava::for::statement.__init__)


def test_simplejava::for::statement_constructor_args():
    sig = inspect.signature(simpleJava::for::statement.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::while::statement_is_not_abstract():
    assert not inspect.isabstract(simpleJava::while::statement)


def test_simplejava::while::statement_constructor_exists():
    assert callable(simpleJava::while::statement.__init__)


def test_simplejava::while::statement_constructor_args():
    sig = inspect.signature(simpleJava::while::statement.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::parameter_is_not_abstract():
    assert not inspect.isabstract(simpleJava::parameter)


def test_simplejava::parameter_constructor_exists():
    assert callable(simpleJava::parameter.__init__)


def test_simplejava::parameter_constructor_args():
    sig = inspect.signature(simpleJava::parameter.__init__)
    params = list(sig.parameters.keys())
    assert "nomeParametro" in params, "Missing parameter 'nomeParametro'"

def test_simplejava::parameter_has_nomeParametro():
    assert hasattr(simpleJava::parameter, "nomeParametro")
    descriptor = None
    for klass in simpleJava::parameter.__mro__:
        if "nomeParametro" in klass.__dict__:
            descriptor = klass.__dict__["nomeParametro"]
            break
    assert isinstance(descriptor, property)



def test_simplejava::statement::block_is_not_abstract():
    assert not inspect.isabstract(simpleJava::statement::block)


def test_simplejava::statement::block_constructor_exists():
    assert callable(simpleJava::statement::block.__init__)


def test_simplejava::statement::block_constructor_args():
    sig = inspect.signature(simpleJava::statement::block.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::parameter::list_is_not_abstract():
    assert not inspect.isabstract(simpleJava::parameter::list)


def test_simplejava::parameter::list_constructor_exists():
    assert callable(simpleJava::parameter::list.__init__)


def test_simplejava::parameter::list_constructor_args():
    sig = inspect.signature(simpleJava::parameter::list.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::type_is_not_abstract():
    assert not inspect.isabstract(simpleJava::type)


def test_simplejava::type_constructor_exists():
    assert callable(simpleJava::type.__init__)


def test_simplejava::type_constructor_args():
    sig = inspect.signature(simpleJava::type.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::static::initializer_is_not_abstract():
    assert not inspect.isabstract(simpleJava::static::initializer)


def test_simplejava::static::initializer_constructor_exists():
    assert callable(simpleJava::static::initializer.__init__)


def test_simplejava::static::initializer_constructor_args():
    sig = inspect.signature(simpleJava::static::initializer.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::variable::declaration_is_not_abstract():
    assert not inspect.isabstract(simpleJava::variable::declaration)


def test_simplejava::variable::declaration_constructor_exists():
    assert callable(simpleJava::variable::declaration.__init__)


def test_simplejava::variable::declaration_constructor_args():
    sig = inspect.signature(simpleJava::variable::declaration.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::constructor::declaration_is_not_abstract():
    assert not inspect.isabstract(simpleJava::constructor::declaration)


def test_simplejava::constructor::declaration_constructor_exists():
    assert callable(simpleJava::constructor::declaration.__init__)


def test_simplejava::constructor::declaration_constructor_args():
    sig = inspect.signature(simpleJava::constructor::declaration.__init__)
    params = list(sig.parameters.keys())
    assert "nomeContrutor" in params, "Missing parameter 'nomeContrutor'"

def test_simplejava::constructor::declaration_has_nomeContrutor():
    assert hasattr(simpleJava::constructor::declaration, "nomeContrutor")
    descriptor = None
    for klass in simpleJava::constructor::declaration.__mro__:
        if "nomeContrutor" in klass.__dict__:
            descriptor = klass.__dict__["nomeContrutor"]
            break
    assert isinstance(descriptor, property)



def test_simplejava::method::declaration_is_not_abstract():
    assert not inspect.isabstract(simpleJava::method::declaration)


def test_simplejava::method::declaration_constructor_exists():
    assert callable(simpleJava::method::declaration.__init__)


def test_simplejava::method::declaration_constructor_args():
    sig = inspect.signature(simpleJava::method::declaration.__init__)
    params = list(sig.parameters.keys())
    assert "nomeMetodo" in params, "Missing parameter 'nomeMetodo'"

def test_simplejava::method::declaration_has_nomeMetodo():
    assert hasattr(simpleJava::method::declaration, "nomeMetodo")
    descriptor = None
    for klass in simpleJava::method::declaration.__mro__:
        if "nomeMetodo" in klass.__dict__:
            descriptor = klass.__dict__["nomeMetodo"]
            break
    assert isinstance(descriptor, property)



def test_simplejava::field::declaration_is_not_abstract():
    assert not inspect.isabstract(simpleJava::field::declaration)


def test_simplejava::field::declaration_constructor_exists():
    assert callable(simpleJava::field::declaration.__init__)


def test_simplejava::field::declaration_constructor_args():
    sig = inspect.signature(simpleJava::field::declaration.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::do::statement_is_not_abstract():
    assert not inspect.isabstract(simpleJava::do::statement)


def test_simplejava::do::statement_constructor_exists():
    assert callable(simpleJava::do::statement.__init__)


def test_simplejava::do::statement_constructor_args():
    sig = inspect.signature(simpleJava::do::statement.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::if::statement_is_not_abstract():
    assert not inspect.isabstract(simpleJava::if::statement)


def test_simplejava::if::statement_constructor_exists():
    assert callable(simpleJava::if::statement.__init__)


def test_simplejava::if::statement_constructor_args():
    sig = inspect.signature(simpleJava::if::statement.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::expression_is_not_abstract():
    assert not inspect.isabstract(simpleJava::expression)


def test_simplejava::expression_constructor_exists():
    assert callable(simpleJava::expression.__init__)


def test_simplejava::expression_constructor_args():
    sig = inspect.signature(simpleJava::expression.__init__)
    params = list(sig.parameters.keys())
    assert "identificador" in params, "Missing parameter 'identificador'"

def test_simplejava::expression_has_identificador():
    assert hasattr(simpleJava::expression, "identificador")
    descriptor = None
    for klass in simpleJava::expression.__mro__:
        if "identificador" in klass.__dict__:
            descriptor = klass.__dict__["identificador"]
            break
    assert isinstance(descriptor, property)



def test_simplejava::statement_is_not_abstract():
    assert not inspect.isabstract(simpleJava::statement)


def test_simplejava::statement_constructor_exists():
    assert callable(simpleJava::statement.__init__)


def test_simplejava::statement_constructor_args():
    sig = inspect.signature(simpleJava::statement.__init__)
    params = list(sig.parameters.keys())
    assert "break_" in params, "Missing parameter 'break_'"
    assert "continue_" in params, "Missing parameter 'continue_'"

def test_simplejava::statement_has_break_():
    assert hasattr(simpleJava::statement, "break_")
    descriptor = None
    for klass in simpleJava::statement.__mro__:
        if "break_" in klass.__dict__:
            descriptor = klass.__dict__["break_"]
            break
    assert isinstance(descriptor, property)

def test_simplejava::statement_has_continue_():
    assert hasattr(simpleJava::statement, "continue_")
    descriptor = None
    for klass in simpleJava::statement.__mro__:
        if "continue_" in klass.__dict__:
            descriptor = klass.__dict__["continue_"]
            break
    assert isinstance(descriptor, property)



def test_simplejava::type::declaration_is_not_abstract():
    assert not inspect.isabstract(simpleJava::type::declaration)


def test_simplejava::type::declaration_constructor_exists():
    assert callable(simpleJava::type::declaration.__init__)


def test_simplejava::type::declaration_constructor_args():
    sig = inspect.signature(simpleJava::type::declaration.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::import::statement_is_not_abstract():
    assert not inspect.isabstract(simpleJava::import::statement)


def test_simplejava::import::statement_constructor_exists():
    assert callable(simpleJava::import::statement.__init__)


def test_simplejava::import::statement_constructor_args():
    sig = inspect.signature(simpleJava::import::statement.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::package::statement_is_not_abstract():
    assert not inspect.isabstract(simpleJava::package::statement)


def test_simplejava::package::statement_constructor_exists():
    assert callable(simpleJava::package::statement.__init__)


def test_simplejava::package::statement_constructor_args():
    sig = inspect.signature(simpleJava::package::statement.__init__)
    params = list(sig.parameters.keys())



def test_model_is_not_abstract():
    assert not inspect.isabstract(Model)


def test_model_constructor_exists():
    assert callable(Model.__init__)


def test_model_constructor_args():
    sig = inspect.signature(Model.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::compilation::unit_is_not_abstract():
    assert not inspect.isabstract(simpleJava::compilation::unit)


def test_simplejava::compilation::unit_constructor_exists():
    assert callable(simpleJava::compilation::unit.__init__)


def test_simplejava::compilation::unit_constructor_args():
    sig = inspect.signature(simpleJava::compilation::unit.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::model_is_not_abstract():
    assert not inspect.isabstract(simpleJava::Model)


def test_simplejava::model_constructor_exists():
    assert callable(simpleJava::Model.__init__)


def test_simplejava::model_constructor_args():
    sig = inspect.signature(simpleJava::Model.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::modifier_is_not_abstract():
    assert not inspect.isabstract(simpleJava::MODIFIER)


def test_simplejava::modifier_constructor_exists():
    assert callable(simpleJava::MODIFIER.__init__)


def test_simplejava::modifier_constructor_args():
    sig = inspect.signature(simpleJava::MODIFIER.__init__)
    params = list(sig.parameters.keys())
    assert "modificador" in params, "Missing parameter 'modificador'"

def test_simplejava::modifier_has_modificador():
    assert hasattr(simpleJava::MODIFIER, "modificador")
    descriptor = None
    for klass in simpleJava::MODIFIER.__mro__:
        if "modificador" in klass.__dict__:
            descriptor = klass.__dict__["modificador"]
            break
    assert isinstance(descriptor, property)



def test_type::declaration_is_not_abstract():
    assert not inspect.isabstract(type::declaration)


def test_type::declaration_constructor_exists():
    assert callable(type::declaration.__init__)


def test_type::declaration_constructor_args():
    sig = inspect.signature(type::declaration.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::doc::comment_is_not_abstract():
    assert not inspect.isabstract(simpleJava::doc::comment)


def test_simplejava::doc::comment_constructor_exists():
    assert callable(simpleJava::doc::comment.__init__)


def test_simplejava::doc::comment_constructor_args():
    sig = inspect.signature(simpleJava::doc::comment.__init__)
    params = list(sig.parameters.keys())
    assert "comentario" in params, "Missing parameter 'comentario'"

def test_simplejava::doc::comment_has_comentario():
    assert hasattr(simpleJava::doc::comment, "comentario")
    descriptor = None
    for klass in simpleJava::doc::comment.__mro__:
        if "comentario" in klass.__dict__:
            descriptor = klass.__dict__["comentario"]
            break
    assert isinstance(descriptor, property)



def test_simplejava::interface::declaration_is_not_abstract():
    assert not inspect.isabstract(simpleJava::interface::declaration)


def test_simplejava::interface::declaration_constructor_exists():
    assert callable(simpleJava::interface::declaration.__init__)


def test_simplejava::interface::declaration_constructor_args():
    sig = inspect.signature(simpleJava::interface::declaration.__init__)
    params = list(sig.parameters.keys())
    assert "nomeInterface" in params, "Missing parameter 'nomeInterface'"

def test_simplejava::interface::declaration_has_nomeInterface():
    assert hasattr(simpleJava::interface::declaration, "nomeInterface")
    descriptor = None
    for klass in simpleJava::interface::declaration.__mro__:
        if "nomeInterface" in klass.__dict__:
            descriptor = klass.__dict__["nomeInterface"]
            break
    assert isinstance(descriptor, property)



def test_simplejava::class::declaration_is_not_abstract():
    assert not inspect.isabstract(simpleJava::class::declaration)


def test_simplejava::class::declaration_constructor_exists():
    assert callable(simpleJava::class::declaration.__init__)


def test_simplejava::class::declaration_constructor_args():
    sig = inspect.signature(simpleJava::class::declaration.__init__)
    params = list(sig.parameters.keys())
    assert "nomeClasse" in params, "Missing parameter 'nomeClasse'"

def test_simplejava::class::declaration_has_nomeClasse():
    assert hasattr(simpleJava::class::declaration, "nomeClasse")
    descriptor = None
    for klass in simpleJava::class::declaration.__mro__:
        if "nomeClasse" in klass.__dict__:
            descriptor = klass.__dict__["nomeClasse"]
            break
    assert isinstance(descriptor, property)



def test_simplejava::name_is_not_abstract():
    assert not inspect.isabstract(simpleJava::name)


def test_simplejava::name_constructor_exists():
    assert callable(simpleJava::name.__init__)


def test_simplejava::name_constructor_args():
    sig = inspect.signature(simpleJava::name.__init__)
    params = list(sig.parameters.keys())
    assert "nome" in params, "Missing parameter 'nome'"

def test_simplejava::name_has_nome():
    assert hasattr(simpleJava::name, "nome")
    descriptor = None
    for klass in simpleJava::name.__mro__:
        if "nome" in klass.__dict__:
            descriptor = klass.__dict__["nome"]
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
exp::aux_strategy = st.builds(
    exp::aux,
)
simpleJava::package::name::aux_strategy = st.builds(
    simpleJava::package::name::aux,
    nomePacote=
        safe_text
)
variable::declarator_strategy = st.builds(
    variable::declarator,
)
simpleJava::literal::expression_strategy = st.builds(
    simpleJava::literal::expression,
    string=
        safe_text,
    inteiro=
        safe_text,
    l_float=
        safe_text,
    decimal=
        safe_text
)
simpleJava::bit::expression_strategy = st.builds(
    simpleJava::bit::expression,
    operador=
        safe_text
)
simpleJava::numeric::expression_strategy = st.builds(
    simpleJava::numeric::expression,
    operador=
        safe_text
)
simpleJava::logical::expression_strategy = st.builds(
    simpleJava::logical::expression,
    operador=
        safe_text
)
expression::aux_strategy = st.builds(
    expression::aux,
)
expression_strategy = st.builds(
    expression,
)
simpleJava::exp::aux_strategy = st.builds(
    simpleJava::exp::aux,
)
simpleJava::newBlock_strategy = st.builds(
    simpleJava::newBlock,
)
simpleJava::type::specifier_strategy = st.builds(
    simpleJava::type::specifier,
    nome=
        safe_text
)
simpleJava::creating::aux_strategy = st.builds(
    simpleJava::creating::aux,
)
simpleJava::creating::expression_strategy = st.builds(
    simpleJava::creating::expression,
)
creating::aux_strategy = st.builds(
    creating::aux,
)
simpleJava::aux_strategy = st.builds(
    simpleJava::aux,
)
simpleJava::mais::aux_strategy = st.builds(
    simpleJava::mais::aux,
    operador=
        safe_text
)
simpleJava::arglist_strategy = st.builds(
    simpleJava::arglist,
    nomeParametro=
        safe_text
)
simpleJava::expression::aux_strategy = st.builds(
    simpleJava::expression::aux,
    operador=
        safe_text
)
newBlock_strategy = st.builds(
    newBlock,
)
simpleJava::variable::initializer_strategy = st.builds(
    simpleJava::variable::initializer,
)
simpleJava::variable::declarator_strategy = st.builds(
    simpleJava::variable::declarator,
    op=
        safe_text,
    nomeVariavel=
        safe_text
)
simpleJava::switch::statement_strategy = st.builds(
    simpleJava::switch::statement,
)
simpleJava::try::statement_strategy = st.builds(
    simpleJava::try::statement,
)
simpleJava::for::statement_strategy = st.builds(
    simpleJava::for::statement,
)
simpleJava::while::statement_strategy = st.builds(
    simpleJava::while::statement,
)
simpleJava::parameter_strategy = st.builds(
    simpleJava::parameter,
    nomeParametro=
        safe_text
)
simpleJava::statement::block_strategy = st.builds(
    simpleJava::statement::block,
)
simpleJava::parameter::list_strategy = st.builds(
    simpleJava::parameter::list,
)
simpleJava::type_strategy = st.builds(
    simpleJava::type,
)
simpleJava::static::initializer_strategy = st.builds(
    simpleJava::static::initializer,
)
simpleJava::variable::declaration_strategy = st.builds(
    simpleJava::variable::declaration,
)
simpleJava::constructor::declaration_strategy = st.builds(
    simpleJava::constructor::declaration,
    nomeContrutor=
        safe_text
)
simpleJava::method::declaration_strategy = st.builds(
    simpleJava::method::declaration,
    nomeMetodo=
        safe_text
)
simpleJava::field::declaration_strategy = st.builds(
    simpleJava::field::declaration,
)
simpleJava::do::statement_strategy = st.builds(
    simpleJava::do::statement,
)
simpleJava::if::statement_strategy = st.builds(
    simpleJava::if::statement,
)
simpleJava::expression_strategy = st.builds(
    simpleJava::expression,
    identificador=
        safe_text
)
simpleJava::statement_strategy = st.builds(
    simpleJava::statement,
    break_=
        safe_text,
    continue_=
        safe_text
)
simpleJava::type::declaration_strategy = st.builds(
    simpleJava::type::declaration,
)
simpleJava::import::statement_strategy = st.builds(
    simpleJava::import::statement,
)
simpleJava::package::statement_strategy = st.builds(
    simpleJava::package::statement,
)
Model_strategy = st.builds(
    Model,
)
simpleJava::compilation::unit_strategy = st.builds(
    simpleJava::compilation::unit,
)
simpleJava::Model_strategy = st.builds(
    simpleJava::Model,
)
simpleJava::MODIFIER_strategy = st.builds(
    simpleJava::MODIFIER,
    modificador=
        safe_text
)
type::declaration_strategy = st.builds(
    type::declaration,
)
simpleJava::doc::comment_strategy = st.builds(
    simpleJava::doc::comment,
    comentario=
        safe_text
)
simpleJava::interface::declaration_strategy = st.builds(
    simpleJava::interface::declaration,
    nomeInterface=
        safe_text
)
simpleJava::class::declaration_strategy = st.builds(
    simpleJava::class::declaration,
    nomeClasse=
        safe_text
)
simpleJava::name_strategy = st.builds(
    simpleJava::name,
    nome=
        safe_text
)

@given(instance=exp::aux_strategy)
@settings(max_examples=50)
def test_exp::aux_instantiation(instance):
    assert isinstance(instance, exp::aux)

@given(instance=simpleJava::package::name::aux_strategy)
@settings(max_examples=50)
def test_simplejava::package::name::aux_instantiation(instance):
    assert isinstance(instance, simpleJava::package::name::aux)

@given(instance=simpleJava::package::name::aux_strategy)
def test_simplejava::package::name::aux_nomePacote_type(instance):
    assert isinstance(instance.nomePacote, str)


@given(instance=simpleJava::package::name::aux_strategy)
def test_simplejava::package::name::aux_nomePacote_setter(instance):
    original = instance.nomePacote
    instance.nomePacote = original
    assert instance.nomePacote == original

@given(instance=variable::declarator_strategy)
@settings(max_examples=50)
def test_variable::declarator_instantiation(instance):
    assert isinstance(instance, variable::declarator)

@given(instance=simpleJava::literal::expression_strategy)
@settings(max_examples=50)
def test_simplejava::literal::expression_instantiation(instance):
    assert isinstance(instance, simpleJava::literal::expression)

@given(instance=simpleJava::literal::expression_strategy)
def test_simplejava::literal::expression_string_type(instance):
    assert isinstance(instance.string, str)


@given(instance=simpleJava::literal::expression_strategy)
def test_simplejava::literal::expression_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=simpleJava::literal::expression_strategy)
def test_simplejava::literal::expression_inteiro_type(instance):
    assert isinstance(instance.inteiro, str)


@given(instance=simpleJava::literal::expression_strategy)
def test_simplejava::literal::expression_inteiro_setter(instance):
    original = instance.inteiro
    instance.inteiro = original
    assert instance.inteiro == original

@given(instance=simpleJava::literal::expression_strategy)
def test_simplejava::literal::expression_l_float_type(instance):
    assert isinstance(instance.l_float, str)


@given(instance=simpleJava::literal::expression_strategy)
def test_simplejava::literal::expression_l_float_setter(instance):
    original = instance.l_float
    instance.l_float = original
    assert instance.l_float == original

@given(instance=simpleJava::literal::expression_strategy)
def test_simplejava::literal::expression_decimal_type(instance):
    assert isinstance(instance.decimal, str)


@given(instance=simpleJava::literal::expression_strategy)
def test_simplejava::literal::expression_decimal_setter(instance):
    original = instance.decimal
    instance.decimal = original
    assert instance.decimal == original

@given(instance=simpleJava::bit::expression_strategy)
@settings(max_examples=50)
def test_simplejava::bit::expression_instantiation(instance):
    assert isinstance(instance, simpleJava::bit::expression)

@given(instance=simpleJava::bit::expression_strategy)
def test_simplejava::bit::expression_operador_type(instance):
    assert isinstance(instance.operador, str)


@given(instance=simpleJava::bit::expression_strategy)
def test_simplejava::bit::expression_operador_setter(instance):
    original = instance.operador
    instance.operador = original
    assert instance.operador == original

@given(instance=simpleJava::numeric::expression_strategy)
@settings(max_examples=50)
def test_simplejava::numeric::expression_instantiation(instance):
    assert isinstance(instance, simpleJava::numeric::expression)

@given(instance=simpleJava::numeric::expression_strategy)
def test_simplejava::numeric::expression_operador_type(instance):
    assert isinstance(instance.operador, str)


@given(instance=simpleJava::numeric::expression_strategy)
def test_simplejava::numeric::expression_operador_setter(instance):
    original = instance.operador
    instance.operador = original
    assert instance.operador == original

@given(instance=simpleJava::logical::expression_strategy)
@settings(max_examples=50)
def test_simplejava::logical::expression_instantiation(instance):
    assert isinstance(instance, simpleJava::logical::expression)

@given(instance=simpleJava::logical::expression_strategy)
def test_simplejava::logical::expression_operador_type(instance):
    assert isinstance(instance.operador, str)


@given(instance=simpleJava::logical::expression_strategy)
def test_simplejava::logical::expression_operador_setter(instance):
    original = instance.operador
    instance.operador = original
    assert instance.operador == original

@given(instance=expression::aux_strategy)
@settings(max_examples=50)
def test_expression::aux_instantiation(instance):
    assert isinstance(instance, expression::aux)

@given(instance=expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, expression)

@given(instance=simpleJava::exp::aux_strategy)
@settings(max_examples=50)
def test_simplejava::exp::aux_instantiation(instance):
    assert isinstance(instance, simpleJava::exp::aux)

@given(instance=simpleJava::newBlock_strategy)
@settings(max_examples=50)
def test_simplejava::newblock_instantiation(instance):
    assert isinstance(instance, simpleJava::newBlock)

@given(instance=simpleJava::type::specifier_strategy)
@settings(max_examples=50)
def test_simplejava::type::specifier_instantiation(instance):
    assert isinstance(instance, simpleJava::type::specifier)

@given(instance=simpleJava::type::specifier_strategy)
def test_simplejava::type::specifier_nome_type(instance):
    assert isinstance(instance.nome, str)


@given(instance=simpleJava::type::specifier_strategy)
def test_simplejava::type::specifier_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original

@given(instance=simpleJava::creating::aux_strategy)
@settings(max_examples=50)
def test_simplejava::creating::aux_instantiation(instance):
    assert isinstance(instance, simpleJava::creating::aux)

@given(instance=simpleJava::creating::expression_strategy)
@settings(max_examples=50)
def test_simplejava::creating::expression_instantiation(instance):
    assert isinstance(instance, simpleJava::creating::expression)

@given(instance=creating::aux_strategy)
@settings(max_examples=50)
def test_creating::aux_instantiation(instance):
    assert isinstance(instance, creating::aux)

@given(instance=simpleJava::aux_strategy)
@settings(max_examples=50)
def test_simplejava::aux_instantiation(instance):
    assert isinstance(instance, simpleJava::aux)

@given(instance=simpleJava::mais::aux_strategy)
@settings(max_examples=50)
def test_simplejava::mais::aux_instantiation(instance):
    assert isinstance(instance, simpleJava::mais::aux)

@given(instance=simpleJava::mais::aux_strategy)
def test_simplejava::mais::aux_operador_type(instance):
    assert isinstance(instance.operador, str)


@given(instance=simpleJava::mais::aux_strategy)
def test_simplejava::mais::aux_operador_setter(instance):
    original = instance.operador
    instance.operador = original
    assert instance.operador == original

@given(instance=simpleJava::arglist_strategy)
@settings(max_examples=50)
def test_simplejava::arglist_instantiation(instance):
    assert isinstance(instance, simpleJava::arglist)

@given(instance=simpleJava::arglist_strategy)
def test_simplejava::arglist_nomeParametro_type(instance):
    assert isinstance(instance.nomeParametro, str)


@given(instance=simpleJava::arglist_strategy)
def test_simplejava::arglist_nomeParametro_setter(instance):
    original = instance.nomeParametro
    instance.nomeParametro = original
    assert instance.nomeParametro == original

@given(instance=simpleJava::expression::aux_strategy)
@settings(max_examples=50)
def test_simplejava::expression::aux_instantiation(instance):
    assert isinstance(instance, simpleJava::expression::aux)

@given(instance=simpleJava::expression::aux_strategy)
def test_simplejava::expression::aux_operador_type(instance):
    assert isinstance(instance.operador, str)


@given(instance=simpleJava::expression::aux_strategy)
def test_simplejava::expression::aux_operador_setter(instance):
    original = instance.operador
    instance.operador = original
    assert instance.operador == original

@given(instance=newBlock_strategy)
@settings(max_examples=50)
def test_newblock_instantiation(instance):
    assert isinstance(instance, newBlock)

@given(instance=simpleJava::variable::initializer_strategy)
@settings(max_examples=50)
def test_simplejava::variable::initializer_instantiation(instance):
    assert isinstance(instance, simpleJava::variable::initializer)

@given(instance=simpleJava::variable::declarator_strategy)
@settings(max_examples=50)
def test_simplejava::variable::declarator_instantiation(instance):
    assert isinstance(instance, simpleJava::variable::declarator)

@given(instance=simpleJava::variable::declarator_strategy)
def test_simplejava::variable::declarator_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=simpleJava::variable::declarator_strategy)
def test_simplejava::variable::declarator_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=simpleJava::variable::declarator_strategy)
def test_simplejava::variable::declarator_nomeVariavel_type(instance):
    assert isinstance(instance.nomeVariavel, str)


@given(instance=simpleJava::variable::declarator_strategy)
def test_simplejava::variable::declarator_nomeVariavel_setter(instance):
    original = instance.nomeVariavel
    instance.nomeVariavel = original
    assert instance.nomeVariavel == original

@given(instance=simpleJava::switch::statement_strategy)
@settings(max_examples=50)
def test_simplejava::switch::statement_instantiation(instance):
    assert isinstance(instance, simpleJava::switch::statement)

@given(instance=simpleJava::try::statement_strategy)
@settings(max_examples=50)
def test_simplejava::try::statement_instantiation(instance):
    assert isinstance(instance, simpleJava::try::statement)

@given(instance=simpleJava::for::statement_strategy)
@settings(max_examples=50)
def test_simplejava::for::statement_instantiation(instance):
    assert isinstance(instance, simpleJava::for::statement)

@given(instance=simpleJava::while::statement_strategy)
@settings(max_examples=50)
def test_simplejava::while::statement_instantiation(instance):
    assert isinstance(instance, simpleJava::while::statement)

@given(instance=simpleJava::parameter_strategy)
@settings(max_examples=50)
def test_simplejava::parameter_instantiation(instance):
    assert isinstance(instance, simpleJava::parameter)

@given(instance=simpleJava::parameter_strategy)
def test_simplejava::parameter_nomeParametro_type(instance):
    assert isinstance(instance.nomeParametro, str)


@given(instance=simpleJava::parameter_strategy)
def test_simplejava::parameter_nomeParametro_setter(instance):
    original = instance.nomeParametro
    instance.nomeParametro = original
    assert instance.nomeParametro == original

@given(instance=simpleJava::statement::block_strategy)
@settings(max_examples=50)
def test_simplejava::statement::block_instantiation(instance):
    assert isinstance(instance, simpleJava::statement::block)

@given(instance=simpleJava::parameter::list_strategy)
@settings(max_examples=50)
def test_simplejava::parameter::list_instantiation(instance):
    assert isinstance(instance, simpleJava::parameter::list)

@given(instance=simpleJava::type_strategy)
@settings(max_examples=50)
def test_simplejava::type_instantiation(instance):
    assert isinstance(instance, simpleJava::type)

@given(instance=simpleJava::static::initializer_strategy)
@settings(max_examples=50)
def test_simplejava::static::initializer_instantiation(instance):
    assert isinstance(instance, simpleJava::static::initializer)

@given(instance=simpleJava::variable::declaration_strategy)
@settings(max_examples=50)
def test_simplejava::variable::declaration_instantiation(instance):
    assert isinstance(instance, simpleJava::variable::declaration)

@given(instance=simpleJava::constructor::declaration_strategy)
@settings(max_examples=50)
def test_simplejava::constructor::declaration_instantiation(instance):
    assert isinstance(instance, simpleJava::constructor::declaration)

@given(instance=simpleJava::constructor::declaration_strategy)
def test_simplejava::constructor::declaration_nomeContrutor_type(instance):
    assert isinstance(instance.nomeContrutor, str)


@given(instance=simpleJava::constructor::declaration_strategy)
def test_simplejava::constructor::declaration_nomeContrutor_setter(instance):
    original = instance.nomeContrutor
    instance.nomeContrutor = original
    assert instance.nomeContrutor == original

@given(instance=simpleJava::method::declaration_strategy)
@settings(max_examples=50)
def test_simplejava::method::declaration_instantiation(instance):
    assert isinstance(instance, simpleJava::method::declaration)

@given(instance=simpleJava::method::declaration_strategy)
def test_simplejava::method::declaration_nomeMetodo_type(instance):
    assert isinstance(instance.nomeMetodo, str)


@given(instance=simpleJava::method::declaration_strategy)
def test_simplejava::method::declaration_nomeMetodo_setter(instance):
    original = instance.nomeMetodo
    instance.nomeMetodo = original
    assert instance.nomeMetodo == original

@given(instance=simpleJava::field::declaration_strategy)
@settings(max_examples=50)
def test_simplejava::field::declaration_instantiation(instance):
    assert isinstance(instance, simpleJava::field::declaration)

@given(instance=simpleJava::do::statement_strategy)
@settings(max_examples=50)
def test_simplejava::do::statement_instantiation(instance):
    assert isinstance(instance, simpleJava::do::statement)

@given(instance=simpleJava::if::statement_strategy)
@settings(max_examples=50)
def test_simplejava::if::statement_instantiation(instance):
    assert isinstance(instance, simpleJava::if::statement)

@given(instance=simpleJava::expression_strategy)
@settings(max_examples=50)
def test_simplejava::expression_instantiation(instance):
    assert isinstance(instance, simpleJava::expression)

@given(instance=simpleJava::expression_strategy)
def test_simplejava::expression_identificador_type(instance):
    assert isinstance(instance.identificador, str)


@given(instance=simpleJava::expression_strategy)
def test_simplejava::expression_identificador_setter(instance):
    original = instance.identificador
    instance.identificador = original
    assert instance.identificador == original

@given(instance=simpleJava::statement_strategy)
@settings(max_examples=50)
def test_simplejava::statement_instantiation(instance):
    assert isinstance(instance, simpleJava::statement)

@given(instance=simpleJava::statement_strategy)
def test_simplejava::statement_break__type(instance):
    assert isinstance(instance.break_, str)


@given(instance=simpleJava::statement_strategy)
def test_simplejava::statement_break__setter(instance):
    original = instance.break_
    instance.break_ = original
    assert instance.break_ == original

@given(instance=simpleJava::statement_strategy)
def test_simplejava::statement_continue__type(instance):
    assert isinstance(instance.continue_, str)


@given(instance=simpleJava::statement_strategy)
def test_simplejava::statement_continue__setter(instance):
    original = instance.continue_
    instance.continue_ = original
    assert instance.continue_ == original

@given(instance=simpleJava::type::declaration_strategy)
@settings(max_examples=50)
def test_simplejava::type::declaration_instantiation(instance):
    assert isinstance(instance, simpleJava::type::declaration)

@given(instance=simpleJava::import::statement_strategy)
@settings(max_examples=50)
def test_simplejava::import::statement_instantiation(instance):
    assert isinstance(instance, simpleJava::import::statement)

@given(instance=simpleJava::package::statement_strategy)
@settings(max_examples=50)
def test_simplejava::package::statement_instantiation(instance):
    assert isinstance(instance, simpleJava::package::statement)

@given(instance=Model_strategy)
@settings(max_examples=50)
def test_model_instantiation(instance):
    assert isinstance(instance, Model)

@given(instance=simpleJava::compilation::unit_strategy)
@settings(max_examples=50)
def test_simplejava::compilation::unit_instantiation(instance):
    assert isinstance(instance, simpleJava::compilation::unit)

@given(instance=simpleJava::Model_strategy)
@settings(max_examples=50)
def test_simplejava::model_instantiation(instance):
    assert isinstance(instance, simpleJava::Model)

@given(instance=simpleJava::MODIFIER_strategy)
@settings(max_examples=50)
def test_simplejava::modifier_instantiation(instance):
    assert isinstance(instance, simpleJava::MODIFIER)

@given(instance=simpleJava::MODIFIER_strategy)
def test_simplejava::modifier_modificador_type(instance):
    assert isinstance(instance.modificador, str)


@given(instance=simpleJava::MODIFIER_strategy)
def test_simplejava::modifier_modificador_setter(instance):
    original = instance.modificador
    instance.modificador = original
    assert instance.modificador == original

@given(instance=type::declaration_strategy)
@settings(max_examples=50)
def test_type::declaration_instantiation(instance):
    assert isinstance(instance, type::declaration)

@given(instance=simpleJava::doc::comment_strategy)
@settings(max_examples=50)
def test_simplejava::doc::comment_instantiation(instance):
    assert isinstance(instance, simpleJava::doc::comment)

@given(instance=simpleJava::doc::comment_strategy)
def test_simplejava::doc::comment_comentario_type(instance):
    assert isinstance(instance.comentario, str)


@given(instance=simpleJava::doc::comment_strategy)
def test_simplejava::doc::comment_comentario_setter(instance):
    original = instance.comentario
    instance.comentario = original
    assert instance.comentario == original

@given(instance=simpleJava::interface::declaration_strategy)
@settings(max_examples=50)
def test_simplejava::interface::declaration_instantiation(instance):
    assert isinstance(instance, simpleJava::interface::declaration)

@given(instance=simpleJava::interface::declaration_strategy)
def test_simplejava::interface::declaration_nomeInterface_type(instance):
    assert isinstance(instance.nomeInterface, str)


@given(instance=simpleJava::interface::declaration_strategy)
def test_simplejava::interface::declaration_nomeInterface_setter(instance):
    original = instance.nomeInterface
    instance.nomeInterface = original
    assert instance.nomeInterface == original

@given(instance=simpleJava::class::declaration_strategy)
@settings(max_examples=50)
def test_simplejava::class::declaration_instantiation(instance):
    assert isinstance(instance, simpleJava::class::declaration)

@given(instance=simpleJava::class::declaration_strategy)
def test_simplejava::class::declaration_nomeClasse_type(instance):
    assert isinstance(instance.nomeClasse, str)


@given(instance=simpleJava::class::declaration_strategy)
def test_simplejava::class::declaration_nomeClasse_setter(instance):
    original = instance.nomeClasse
    instance.nomeClasse = original
    assert instance.nomeClasse == original

@given(instance=simpleJava::name_strategy)
@settings(max_examples=50)
def test_simplejava::name_instantiation(instance):
    assert isinstance(instance, simpleJava::name)

@given(instance=simpleJava::name_strategy)
def test_simplejava::name_nome_type(instance):
    assert isinstance(instance.nome, str)


@given(instance=simpleJava::name_strategy)
def test_simplejava::name_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original
