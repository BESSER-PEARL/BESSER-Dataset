import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    exp_aux,
    simpleJava_package_name_aux,
    variable_declarator,
    simpleJava_literal_expression,
    simpleJava_bit_expression,
    simpleJava_numeric_expression,
    simpleJava_logical_expression,
    expression_aux,
    expression,
    simpleJava_exp_aux,
    simpleJava_newBlock,
    simpleJava_type_specifier,
    simpleJava_creating_aux,
    simpleJava_creating_expression,
    creating_aux,
    simpleJava_aux,
    simpleJava_mais_aux,
    simpleJava_arglist,
    simpleJava_expression_aux,
    newBlock,
    simpleJava_variable_initializer,
    simpleJava_variable_declarator,
    simpleJava_switch_statement,
    simpleJava_try_statement,
    simpleJava_for_statement,
    simpleJava_while_statement,
    simpleJava_parameter,
    simpleJava_statement_block,
    simpleJava_parameter_list,
    simpleJava_type,
    simpleJava_static_initializer,
    simpleJava_variable_declaration,
    simpleJava_constructor_declaration,
    simpleJava_method_declaration,
    simpleJava_field_declaration,
    simpleJava_do_statement,
    simpleJava_if_statement,
    simpleJava_expression,
    simpleJava_statement,
    simpleJava_type_declaration,
    simpleJava_import_statement,
    simpleJava_package_statement,
    Model,
    simpleJava_compilation_unit,
    simpleJava_Model,
    simpleJava_MODIFIER,
    type_declaration,
    simpleJava_doc_comment,
    simpleJava_interface_declaration,
    simpleJava_class_declaration,
    simpleJava_name,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_exp_aux_is_not_abstract():
    assert not inspect.isabstract(exp_aux)


def test_exp_aux_constructor_exists():
    assert callable(exp_aux.__init__)


def test_exp_aux_constructor_args():
    sig = inspect.signature(exp_aux.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_package_name_aux_is_not_abstract():
    assert not inspect.isabstract(simpleJava_package_name_aux)


def test_simplejava_package_name_aux_constructor_exists():
    assert callable(simpleJava_package_name_aux.__init__)


def test_simplejava_package_name_aux_constructor_args():
    sig = inspect.signature(simpleJava_package_name_aux.__init__)
    params = list(sig.parameters.keys())
    assert "nomePacote" in params, "Missing parameter 'nomePacote'"

def test_simplejava_package_name_aux_has_nomePacote():
    assert hasattr(simpleJava_package_name_aux, "nomePacote")
    descriptor = None
    for klass in simpleJava_package_name_aux.__mro__:
        if "nomePacote" in klass.__dict__:
            descriptor = klass.__dict__["nomePacote"]
            break
    assert isinstance(descriptor, property)



def test_variable_declarator_is_not_abstract():
    assert not inspect.isabstract(variable_declarator)


def test_variable_declarator_constructor_exists():
    assert callable(variable_declarator.__init__)


def test_variable_declarator_constructor_args():
    sig = inspect.signature(variable_declarator.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_literal_expression_is_not_abstract():
    assert not inspect.isabstract(simpleJava_literal_expression)


def test_simplejava_literal_expression_constructor_exists():
    assert callable(simpleJava_literal_expression.__init__)


def test_simplejava_literal_expression_constructor_args():
    sig = inspect.signature(simpleJava_literal_expression.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"
    assert "inteiro" in params, "Missing parameter 'inteiro'"
    assert "l_float" in params, "Missing parameter 'l_float'"
    assert "decimal" in params, "Missing parameter 'decimal'"

def test_simplejava_literal_expression_has_string():
    assert hasattr(simpleJava_literal_expression, "string")
    descriptor = None
    for klass in simpleJava_literal_expression.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)

def test_simplejava_literal_expression_has_inteiro():
    assert hasattr(simpleJava_literal_expression, "inteiro")
    descriptor = None
    for klass in simpleJava_literal_expression.__mro__:
        if "inteiro" in klass.__dict__:
            descriptor = klass.__dict__["inteiro"]
            break
    assert isinstance(descriptor, property)

def test_simplejava_literal_expression_has_l_float():
    assert hasattr(simpleJava_literal_expression, "l_float")
    descriptor = None
    for klass in simpleJava_literal_expression.__mro__:
        if "l_float" in klass.__dict__:
            descriptor = klass.__dict__["l_float"]
            break
    assert isinstance(descriptor, property)

def test_simplejava_literal_expression_has_decimal():
    assert hasattr(simpleJava_literal_expression, "decimal")
    descriptor = None
    for klass in simpleJava_literal_expression.__mro__:
        if "decimal" in klass.__dict__:
            descriptor = klass.__dict__["decimal"]
            break
    assert isinstance(descriptor, property)



def test_simplejava_bit_expression_is_not_abstract():
    assert not inspect.isabstract(simpleJava_bit_expression)


def test_simplejava_bit_expression_constructor_exists():
    assert callable(simpleJava_bit_expression.__init__)


def test_simplejava_bit_expression_constructor_args():
    sig = inspect.signature(simpleJava_bit_expression.__init__)
    params = list(sig.parameters.keys())
    assert "operador" in params, "Missing parameter 'operador'"

def test_simplejava_bit_expression_has_operador():
    assert hasattr(simpleJava_bit_expression, "operador")
    descriptor = None
    for klass in simpleJava_bit_expression.__mro__:
        if "operador" in klass.__dict__:
            descriptor = klass.__dict__["operador"]
            break
    assert isinstance(descriptor, property)



def test_simplejava_numeric_expression_is_not_abstract():
    assert not inspect.isabstract(simpleJava_numeric_expression)


def test_simplejava_numeric_expression_constructor_exists():
    assert callable(simpleJava_numeric_expression.__init__)


def test_simplejava_numeric_expression_constructor_args():
    sig = inspect.signature(simpleJava_numeric_expression.__init__)
    params = list(sig.parameters.keys())
    assert "operador" in params, "Missing parameter 'operador'"

def test_simplejava_numeric_expression_has_operador():
    assert hasattr(simpleJava_numeric_expression, "operador")
    descriptor = None
    for klass in simpleJava_numeric_expression.__mro__:
        if "operador" in klass.__dict__:
            descriptor = klass.__dict__["operador"]
            break
    assert isinstance(descriptor, property)



def test_simplejava_logical_expression_is_not_abstract():
    assert not inspect.isabstract(simpleJava_logical_expression)


def test_simplejava_logical_expression_constructor_exists():
    assert callable(simpleJava_logical_expression.__init__)


def test_simplejava_logical_expression_constructor_args():
    sig = inspect.signature(simpleJava_logical_expression.__init__)
    params = list(sig.parameters.keys())
    assert "operador" in params, "Missing parameter 'operador'"

def test_simplejava_logical_expression_has_operador():
    assert hasattr(simpleJava_logical_expression, "operador")
    descriptor = None
    for klass in simpleJava_logical_expression.__mro__:
        if "operador" in klass.__dict__:
            descriptor = klass.__dict__["operador"]
            break
    assert isinstance(descriptor, property)



def test_expression_aux_is_not_abstract():
    assert not inspect.isabstract(expression_aux)


def test_expression_aux_constructor_exists():
    assert callable(expression_aux.__init__)


def test_expression_aux_constructor_args():
    sig = inspect.signature(expression_aux.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(expression)


def test_expression_constructor_exists():
    assert callable(expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(expression.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_exp_aux_is_not_abstract():
    assert not inspect.isabstract(simpleJava_exp_aux)


def test_simplejava_exp_aux_constructor_exists():
    assert callable(simpleJava_exp_aux.__init__)


def test_simplejava_exp_aux_constructor_args():
    sig = inspect.signature(simpleJava_exp_aux.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_newblock_is_not_abstract():
    assert not inspect.isabstract(simpleJava_newBlock)


def test_simplejava_newblock_constructor_exists():
    assert callable(simpleJava_newBlock.__init__)


def test_simplejava_newblock_constructor_args():
    sig = inspect.signature(simpleJava_newBlock.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_type_specifier_is_not_abstract():
    assert not inspect.isabstract(simpleJava_type_specifier)


def test_simplejava_type_specifier_constructor_exists():
    assert callable(simpleJava_type_specifier.__init__)


def test_simplejava_type_specifier_constructor_args():
    sig = inspect.signature(simpleJava_type_specifier.__init__)
    params = list(sig.parameters.keys())
    assert "nome" in params, "Missing parameter 'nome'"

def test_simplejava_type_specifier_has_nome():
    assert hasattr(simpleJava_type_specifier, "nome")
    descriptor = None
    for klass in simpleJava_type_specifier.__mro__:
        if "nome" in klass.__dict__:
            descriptor = klass.__dict__["nome"]
            break
    assert isinstance(descriptor, property)



def test_simplejava_creating_aux_is_not_abstract():
    assert not inspect.isabstract(simpleJava_creating_aux)


def test_simplejava_creating_aux_constructor_exists():
    assert callable(simpleJava_creating_aux.__init__)


def test_simplejava_creating_aux_constructor_args():
    sig = inspect.signature(simpleJava_creating_aux.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_creating_expression_is_not_abstract():
    assert not inspect.isabstract(simpleJava_creating_expression)


def test_simplejava_creating_expression_constructor_exists():
    assert callable(simpleJava_creating_expression.__init__)


def test_simplejava_creating_expression_constructor_args():
    sig = inspect.signature(simpleJava_creating_expression.__init__)
    params = list(sig.parameters.keys())



def test_creating_aux_is_not_abstract():
    assert not inspect.isabstract(creating_aux)


def test_creating_aux_constructor_exists():
    assert callable(creating_aux.__init__)


def test_creating_aux_constructor_args():
    sig = inspect.signature(creating_aux.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_aux_is_not_abstract():
    assert not inspect.isabstract(simpleJava_aux)


def test_simplejava_aux_constructor_exists():
    assert callable(simpleJava_aux.__init__)


def test_simplejava_aux_constructor_args():
    sig = inspect.signature(simpleJava_aux.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_mais_aux_is_not_abstract():
    assert not inspect.isabstract(simpleJava_mais_aux)


def test_simplejava_mais_aux_constructor_exists():
    assert callable(simpleJava_mais_aux.__init__)


def test_simplejava_mais_aux_constructor_args():
    sig = inspect.signature(simpleJava_mais_aux.__init__)
    params = list(sig.parameters.keys())
    assert "operador" in params, "Missing parameter 'operador'"

def test_simplejava_mais_aux_has_operador():
    assert hasattr(simpleJava_mais_aux, "operador")
    descriptor = None
    for klass in simpleJava_mais_aux.__mro__:
        if "operador" in klass.__dict__:
            descriptor = klass.__dict__["operador"]
            break
    assert isinstance(descriptor, property)



def test_simplejava_arglist_is_not_abstract():
    assert not inspect.isabstract(simpleJava_arglist)


def test_simplejava_arglist_constructor_exists():
    assert callable(simpleJava_arglist.__init__)


def test_simplejava_arglist_constructor_args():
    sig = inspect.signature(simpleJava_arglist.__init__)
    params = list(sig.parameters.keys())
    assert "nomeParametro" in params, "Missing parameter 'nomeParametro'"

def test_simplejava_arglist_has_nomeParametro():
    assert hasattr(simpleJava_arglist, "nomeParametro")
    descriptor = None
    for klass in simpleJava_arglist.__mro__:
        if "nomeParametro" in klass.__dict__:
            descriptor = klass.__dict__["nomeParametro"]
            break
    assert isinstance(descriptor, property)



def test_simplejava_expression_aux_is_not_abstract():
    assert not inspect.isabstract(simpleJava_expression_aux)


def test_simplejava_expression_aux_constructor_exists():
    assert callable(simpleJava_expression_aux.__init__)


def test_simplejava_expression_aux_constructor_args():
    sig = inspect.signature(simpleJava_expression_aux.__init__)
    params = list(sig.parameters.keys())
    assert "operador" in params, "Missing parameter 'operador'"

def test_simplejava_expression_aux_has_operador():
    assert hasattr(simpleJava_expression_aux, "operador")
    descriptor = None
    for klass in simpleJava_expression_aux.__mro__:
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



def test_simplejava_variable_initializer_is_not_abstract():
    assert not inspect.isabstract(simpleJava_variable_initializer)


def test_simplejava_variable_initializer_constructor_exists():
    assert callable(simpleJava_variable_initializer.__init__)


def test_simplejava_variable_initializer_constructor_args():
    sig = inspect.signature(simpleJava_variable_initializer.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_variable_declarator_is_not_abstract():
    assert not inspect.isabstract(simpleJava_variable_declarator)


def test_simplejava_variable_declarator_constructor_exists():
    assert callable(simpleJava_variable_declarator.__init__)


def test_simplejava_variable_declarator_constructor_args():
    sig = inspect.signature(simpleJava_variable_declarator.__init__)
    params = list(sig.parameters.keys())
    assert "nomeVariavel" in params, "Missing parameter 'nomeVariavel'"
    assert "op" in params, "Missing parameter 'op'"

def test_simplejava_variable_declarator_has_nomeVariavel():
    assert hasattr(simpleJava_variable_declarator, "nomeVariavel")
    descriptor = None
    for klass in simpleJava_variable_declarator.__mro__:
        if "nomeVariavel" in klass.__dict__:
            descriptor = klass.__dict__["nomeVariavel"]
            break
    assert isinstance(descriptor, property)

def test_simplejava_variable_declarator_has_op():
    assert hasattr(simpleJava_variable_declarator, "op")
    descriptor = None
    for klass in simpleJava_variable_declarator.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_simplejava_switch_statement_is_not_abstract():
    assert not inspect.isabstract(simpleJava_switch_statement)


def test_simplejava_switch_statement_constructor_exists():
    assert callable(simpleJava_switch_statement.__init__)


def test_simplejava_switch_statement_constructor_args():
    sig = inspect.signature(simpleJava_switch_statement.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_try_statement_is_not_abstract():
    assert not inspect.isabstract(simpleJava_try_statement)


def test_simplejava_try_statement_constructor_exists():
    assert callable(simpleJava_try_statement.__init__)


def test_simplejava_try_statement_constructor_args():
    sig = inspect.signature(simpleJava_try_statement.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_for_statement_is_not_abstract():
    assert not inspect.isabstract(simpleJava_for_statement)


def test_simplejava_for_statement_constructor_exists():
    assert callable(simpleJava_for_statement.__init__)


def test_simplejava_for_statement_constructor_args():
    sig = inspect.signature(simpleJava_for_statement.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_while_statement_is_not_abstract():
    assert not inspect.isabstract(simpleJava_while_statement)


def test_simplejava_while_statement_constructor_exists():
    assert callable(simpleJava_while_statement.__init__)


def test_simplejava_while_statement_constructor_args():
    sig = inspect.signature(simpleJava_while_statement.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_parameter_is_not_abstract():
    assert not inspect.isabstract(simpleJava_parameter)


def test_simplejava_parameter_constructor_exists():
    assert callable(simpleJava_parameter.__init__)


def test_simplejava_parameter_constructor_args():
    sig = inspect.signature(simpleJava_parameter.__init__)
    params = list(sig.parameters.keys())
    assert "nomeParametro" in params, "Missing parameter 'nomeParametro'"

def test_simplejava_parameter_has_nomeParametro():
    assert hasattr(simpleJava_parameter, "nomeParametro")
    descriptor = None
    for klass in simpleJava_parameter.__mro__:
        if "nomeParametro" in klass.__dict__:
            descriptor = klass.__dict__["nomeParametro"]
            break
    assert isinstance(descriptor, property)



def test_simplejava_statement_block_is_not_abstract():
    assert not inspect.isabstract(simpleJava_statement_block)


def test_simplejava_statement_block_constructor_exists():
    assert callable(simpleJava_statement_block.__init__)


def test_simplejava_statement_block_constructor_args():
    sig = inspect.signature(simpleJava_statement_block.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_parameter_list_is_not_abstract():
    assert not inspect.isabstract(simpleJava_parameter_list)


def test_simplejava_parameter_list_constructor_exists():
    assert callable(simpleJava_parameter_list.__init__)


def test_simplejava_parameter_list_constructor_args():
    sig = inspect.signature(simpleJava_parameter_list.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_type_is_not_abstract():
    assert not inspect.isabstract(simpleJava_type)


def test_simplejava_type_constructor_exists():
    assert callable(simpleJava_type.__init__)


def test_simplejava_type_constructor_args():
    sig = inspect.signature(simpleJava_type.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_static_initializer_is_not_abstract():
    assert not inspect.isabstract(simpleJava_static_initializer)


def test_simplejava_static_initializer_constructor_exists():
    assert callable(simpleJava_static_initializer.__init__)


def test_simplejava_static_initializer_constructor_args():
    sig = inspect.signature(simpleJava_static_initializer.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_variable_declaration_is_not_abstract():
    assert not inspect.isabstract(simpleJava_variable_declaration)


def test_simplejava_variable_declaration_constructor_exists():
    assert callable(simpleJava_variable_declaration.__init__)


def test_simplejava_variable_declaration_constructor_args():
    sig = inspect.signature(simpleJava_variable_declaration.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_constructor_declaration_is_not_abstract():
    assert not inspect.isabstract(simpleJava_constructor_declaration)


def test_simplejava_constructor_declaration_constructor_exists():
    assert callable(simpleJava_constructor_declaration.__init__)


def test_simplejava_constructor_declaration_constructor_args():
    sig = inspect.signature(simpleJava_constructor_declaration.__init__)
    params = list(sig.parameters.keys())
    assert "nomeContrutor" in params, "Missing parameter 'nomeContrutor'"

def test_simplejava_constructor_declaration_has_nomeContrutor():
    assert hasattr(simpleJava_constructor_declaration, "nomeContrutor")
    descriptor = None
    for klass in simpleJava_constructor_declaration.__mro__:
        if "nomeContrutor" in klass.__dict__:
            descriptor = klass.__dict__["nomeContrutor"]
            break
    assert isinstance(descriptor, property)



def test_simplejava_method_declaration_is_not_abstract():
    assert not inspect.isabstract(simpleJava_method_declaration)


def test_simplejava_method_declaration_constructor_exists():
    assert callable(simpleJava_method_declaration.__init__)


def test_simplejava_method_declaration_constructor_args():
    sig = inspect.signature(simpleJava_method_declaration.__init__)
    params = list(sig.parameters.keys())
    assert "nomeMetodo" in params, "Missing parameter 'nomeMetodo'"

def test_simplejava_method_declaration_has_nomeMetodo():
    assert hasattr(simpleJava_method_declaration, "nomeMetodo")
    descriptor = None
    for klass in simpleJava_method_declaration.__mro__:
        if "nomeMetodo" in klass.__dict__:
            descriptor = klass.__dict__["nomeMetodo"]
            break
    assert isinstance(descriptor, property)



def test_simplejava_field_declaration_is_not_abstract():
    assert not inspect.isabstract(simpleJava_field_declaration)


def test_simplejava_field_declaration_constructor_exists():
    assert callable(simpleJava_field_declaration.__init__)


def test_simplejava_field_declaration_constructor_args():
    sig = inspect.signature(simpleJava_field_declaration.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_do_statement_is_not_abstract():
    assert not inspect.isabstract(simpleJava_do_statement)


def test_simplejava_do_statement_constructor_exists():
    assert callable(simpleJava_do_statement.__init__)


def test_simplejava_do_statement_constructor_args():
    sig = inspect.signature(simpleJava_do_statement.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_if_statement_is_not_abstract():
    assert not inspect.isabstract(simpleJava_if_statement)


def test_simplejava_if_statement_constructor_exists():
    assert callable(simpleJava_if_statement.__init__)


def test_simplejava_if_statement_constructor_args():
    sig = inspect.signature(simpleJava_if_statement.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_expression_is_not_abstract():
    assert not inspect.isabstract(simpleJava_expression)


def test_simplejava_expression_constructor_exists():
    assert callable(simpleJava_expression.__init__)


def test_simplejava_expression_constructor_args():
    sig = inspect.signature(simpleJava_expression.__init__)
    params = list(sig.parameters.keys())
    assert "identificador" in params, "Missing parameter 'identificador'"

def test_simplejava_expression_has_identificador():
    assert hasattr(simpleJava_expression, "identificador")
    descriptor = None
    for klass in simpleJava_expression.__mro__:
        if "identificador" in klass.__dict__:
            descriptor = klass.__dict__["identificador"]
            break
    assert isinstance(descriptor, property)



def test_simplejava_statement_is_not_abstract():
    assert not inspect.isabstract(simpleJava_statement)


def test_simplejava_statement_constructor_exists():
    assert callable(simpleJava_statement.__init__)


def test_simplejava_statement_constructor_args():
    sig = inspect.signature(simpleJava_statement.__init__)
    params = list(sig.parameters.keys())
    assert "continue_" in params, "Missing parameter 'continue_'"
    assert "break_" in params, "Missing parameter 'break_'"

def test_simplejava_statement_has_continue_():
    assert hasattr(simpleJava_statement, "continue_")
    descriptor = None
    for klass in simpleJava_statement.__mro__:
        if "continue_" in klass.__dict__:
            descriptor = klass.__dict__["continue_"]
            break
    assert isinstance(descriptor, property)

def test_simplejava_statement_has_break_():
    assert hasattr(simpleJava_statement, "break_")
    descriptor = None
    for klass in simpleJava_statement.__mro__:
        if "break_" in klass.__dict__:
            descriptor = klass.__dict__["break_"]
            break
    assert isinstance(descriptor, property)



def test_simplejava_type_declaration_is_not_abstract():
    assert not inspect.isabstract(simpleJava_type_declaration)


def test_simplejava_type_declaration_constructor_exists():
    assert callable(simpleJava_type_declaration.__init__)


def test_simplejava_type_declaration_constructor_args():
    sig = inspect.signature(simpleJava_type_declaration.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_import_statement_is_not_abstract():
    assert not inspect.isabstract(simpleJava_import_statement)


def test_simplejava_import_statement_constructor_exists():
    assert callable(simpleJava_import_statement.__init__)


def test_simplejava_import_statement_constructor_args():
    sig = inspect.signature(simpleJava_import_statement.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_package_statement_is_not_abstract():
    assert not inspect.isabstract(simpleJava_package_statement)


def test_simplejava_package_statement_constructor_exists():
    assert callable(simpleJava_package_statement.__init__)


def test_simplejava_package_statement_constructor_args():
    sig = inspect.signature(simpleJava_package_statement.__init__)
    params = list(sig.parameters.keys())



def test_model_is_not_abstract():
    assert not inspect.isabstract(Model)


def test_model_constructor_exists():
    assert callable(Model.__init__)


def test_model_constructor_args():
    sig = inspect.signature(Model.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_compilation_unit_is_not_abstract():
    assert not inspect.isabstract(simpleJava_compilation_unit)


def test_simplejava_compilation_unit_constructor_exists():
    assert callable(simpleJava_compilation_unit.__init__)


def test_simplejava_compilation_unit_constructor_args():
    sig = inspect.signature(simpleJava_compilation_unit.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_model_is_not_abstract():
    assert not inspect.isabstract(simpleJava_Model)


def test_simplejava_model_constructor_exists():
    assert callable(simpleJava_Model.__init__)


def test_simplejava_model_constructor_args():
    sig = inspect.signature(simpleJava_Model.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_modifier_is_not_abstract():
    assert not inspect.isabstract(simpleJava_MODIFIER)


def test_simplejava_modifier_constructor_exists():
    assert callable(simpleJava_MODIFIER.__init__)


def test_simplejava_modifier_constructor_args():
    sig = inspect.signature(simpleJava_MODIFIER.__init__)
    params = list(sig.parameters.keys())
    assert "modificador" in params, "Missing parameter 'modificador'"

def test_simplejava_modifier_has_modificador():
    assert hasattr(simpleJava_MODIFIER, "modificador")
    descriptor = None
    for klass in simpleJava_MODIFIER.__mro__:
        if "modificador" in klass.__dict__:
            descriptor = klass.__dict__["modificador"]
            break
    assert isinstance(descriptor, property)



def test_type_declaration_is_not_abstract():
    assert not inspect.isabstract(type_declaration)


def test_type_declaration_constructor_exists():
    assert callable(type_declaration.__init__)


def test_type_declaration_constructor_args():
    sig = inspect.signature(type_declaration.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_doc_comment_is_not_abstract():
    assert not inspect.isabstract(simpleJava_doc_comment)


def test_simplejava_doc_comment_constructor_exists():
    assert callable(simpleJava_doc_comment.__init__)


def test_simplejava_doc_comment_constructor_args():
    sig = inspect.signature(simpleJava_doc_comment.__init__)
    params = list(sig.parameters.keys())
    assert "comentario" in params, "Missing parameter 'comentario'"

def test_simplejava_doc_comment_has_comentario():
    assert hasattr(simpleJava_doc_comment, "comentario")
    descriptor = None
    for klass in simpleJava_doc_comment.__mro__:
        if "comentario" in klass.__dict__:
            descriptor = klass.__dict__["comentario"]
            break
    assert isinstance(descriptor, property)



def test_simplejava_interface_declaration_is_not_abstract():
    assert not inspect.isabstract(simpleJava_interface_declaration)


def test_simplejava_interface_declaration_constructor_exists():
    assert callable(simpleJava_interface_declaration.__init__)


def test_simplejava_interface_declaration_constructor_args():
    sig = inspect.signature(simpleJava_interface_declaration.__init__)
    params = list(sig.parameters.keys())
    assert "nomeInterface" in params, "Missing parameter 'nomeInterface'"

def test_simplejava_interface_declaration_has_nomeInterface():
    assert hasattr(simpleJava_interface_declaration, "nomeInterface")
    descriptor = None
    for klass in simpleJava_interface_declaration.__mro__:
        if "nomeInterface" in klass.__dict__:
            descriptor = klass.__dict__["nomeInterface"]
            break
    assert isinstance(descriptor, property)



def test_simplejava_class_declaration_is_not_abstract():
    assert not inspect.isabstract(simpleJava_class_declaration)


def test_simplejava_class_declaration_constructor_exists():
    assert callable(simpleJava_class_declaration.__init__)


def test_simplejava_class_declaration_constructor_args():
    sig = inspect.signature(simpleJava_class_declaration.__init__)
    params = list(sig.parameters.keys())
    assert "nomeClasse" in params, "Missing parameter 'nomeClasse'"

def test_simplejava_class_declaration_has_nomeClasse():
    assert hasattr(simpleJava_class_declaration, "nomeClasse")
    descriptor = None
    for klass in simpleJava_class_declaration.__mro__:
        if "nomeClasse" in klass.__dict__:
            descriptor = klass.__dict__["nomeClasse"]
            break
    assert isinstance(descriptor, property)



def test_simplejava_name_is_not_abstract():
    assert not inspect.isabstract(simpleJava_name)


def test_simplejava_name_constructor_exists():
    assert callable(simpleJava_name.__init__)


def test_simplejava_name_constructor_args():
    sig = inspect.signature(simpleJava_name.__init__)
    params = list(sig.parameters.keys())
    assert "nome" in params, "Missing parameter 'nome'"

def test_simplejava_name_has_nome():
    assert hasattr(simpleJava_name, "nome")
    descriptor = None
    for klass in simpleJava_name.__mro__:
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
exp_aux_strategy = st.builds(
    exp_aux,
)
simpleJava_package_name_aux_strategy = st.builds(
    simpleJava_package_name_aux,
    nomePacote=
        safe_text
)
variable_declarator_strategy = st.builds(
    variable_declarator,
)
simpleJava_literal_expression_strategy = st.builds(
    simpleJava_literal_expression,
    string=
        safe_text,
    inteiro=
        safe_text,
    l_float=
        safe_text,
    decimal=
        safe_text
)
simpleJava_bit_expression_strategy = st.builds(
    simpleJava_bit_expression,
    operador=
        safe_text
)
simpleJava_numeric_expression_strategy = st.builds(
    simpleJava_numeric_expression,
    operador=
        safe_text
)
simpleJava_logical_expression_strategy = st.builds(
    simpleJava_logical_expression,
    operador=
        safe_text
)
expression_aux_strategy = st.builds(
    expression_aux,
)
expression_strategy = st.builds(
    expression,
)
simpleJava_exp_aux_strategy = st.builds(
    simpleJava_exp_aux,
)
simpleJava_newBlock_strategy = st.builds(
    simpleJava_newBlock,
)
simpleJava_type_specifier_strategy = st.builds(
    simpleJava_type_specifier,
    nome=
        safe_text
)
simpleJava_creating_aux_strategy = st.builds(
    simpleJava_creating_aux,
)
simpleJava_creating_expression_strategy = st.builds(
    simpleJava_creating_expression,
)
creating_aux_strategy = st.builds(
    creating_aux,
)
simpleJava_aux_strategy = st.builds(
    simpleJava_aux,
)
simpleJava_mais_aux_strategy = st.builds(
    simpleJava_mais_aux,
    operador=
        safe_text
)
simpleJava_arglist_strategy = st.builds(
    simpleJava_arglist,
    nomeParametro=
        safe_text
)
simpleJava_expression_aux_strategy = st.builds(
    simpleJava_expression_aux,
    operador=
        safe_text
)
newBlock_strategy = st.builds(
    newBlock,
)
simpleJava_variable_initializer_strategy = st.builds(
    simpleJava_variable_initializer,
)
simpleJava_variable_declarator_strategy = st.builds(
    simpleJava_variable_declarator,
    nomeVariavel=
        safe_text,
    op=
        safe_text
)
simpleJava_switch_statement_strategy = st.builds(
    simpleJava_switch_statement,
)
simpleJava_try_statement_strategy = st.builds(
    simpleJava_try_statement,
)
simpleJava_for_statement_strategy = st.builds(
    simpleJava_for_statement,
)
simpleJava_while_statement_strategy = st.builds(
    simpleJava_while_statement,
)
simpleJava_parameter_strategy = st.builds(
    simpleJava_parameter,
    nomeParametro=
        safe_text
)
simpleJava_statement_block_strategy = st.builds(
    simpleJava_statement_block,
)
simpleJava_parameter_list_strategy = st.builds(
    simpleJava_parameter_list,
)
simpleJava_type_strategy = st.builds(
    simpleJava_type,
)
simpleJava_static_initializer_strategy = st.builds(
    simpleJava_static_initializer,
)
simpleJava_variable_declaration_strategy = st.builds(
    simpleJava_variable_declaration,
)
simpleJava_constructor_declaration_strategy = st.builds(
    simpleJava_constructor_declaration,
    nomeContrutor=
        safe_text
)
simpleJava_method_declaration_strategy = st.builds(
    simpleJava_method_declaration,
    nomeMetodo=
        safe_text
)
simpleJava_field_declaration_strategy = st.builds(
    simpleJava_field_declaration,
)
simpleJava_do_statement_strategy = st.builds(
    simpleJava_do_statement,
)
simpleJava_if_statement_strategy = st.builds(
    simpleJava_if_statement,
)
simpleJava_expression_strategy = st.builds(
    simpleJava_expression,
    identificador=
        safe_text
)
simpleJava_statement_strategy = st.builds(
    simpleJava_statement,
    continue_=
        safe_text,
    break_=
        safe_text
)
simpleJava_type_declaration_strategy = st.builds(
    simpleJava_type_declaration,
)
simpleJava_import_statement_strategy = st.builds(
    simpleJava_import_statement,
)
simpleJava_package_statement_strategy = st.builds(
    simpleJava_package_statement,
)
Model_strategy = st.builds(
    Model,
)
simpleJava_compilation_unit_strategy = st.builds(
    simpleJava_compilation_unit,
)
simpleJava_Model_strategy = st.builds(
    simpleJava_Model,
)
simpleJava_MODIFIER_strategy = st.builds(
    simpleJava_MODIFIER,
    modificador=
        safe_text
)
type_declaration_strategy = st.builds(
    type_declaration,
)
simpleJava_doc_comment_strategy = st.builds(
    simpleJava_doc_comment,
    comentario=
        safe_text
)
simpleJava_interface_declaration_strategy = st.builds(
    simpleJava_interface_declaration,
    nomeInterface=
        safe_text
)
simpleJava_class_declaration_strategy = st.builds(
    simpleJava_class_declaration,
    nomeClasse=
        safe_text
)
simpleJava_name_strategy = st.builds(
    simpleJava_name,
    nome=
        safe_text
)

@given(instance=exp_aux_strategy)
@settings(max_examples=50)
def test_exp_aux_instantiation(instance):
    assert isinstance(instance, exp_aux)

@given(instance=simpleJava_package_name_aux_strategy)
@settings(max_examples=50)
def test_simplejava_package_name_aux_instantiation(instance):
    assert isinstance(instance, simpleJava_package_name_aux)



@given(instance=simpleJava_package_name_aux_strategy)
def test_simplejava_package_name_aux_nomePacote_setter(instance):
    original = instance.nomePacote
    instance.nomePacote = original
    assert instance.nomePacote == original

@given(instance=variable_declarator_strategy)
@settings(max_examples=50)
def test_variable_declarator_instantiation(instance):
    assert isinstance(instance, variable_declarator)

@given(instance=simpleJava_literal_expression_strategy)
@settings(max_examples=50)
def test_simplejava_literal_expression_instantiation(instance):
    assert isinstance(instance, simpleJava_literal_expression)



@given(instance=simpleJava_literal_expression_strategy)
def test_simplejava_literal_expression_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original



@given(instance=simpleJava_literal_expression_strategy)
def test_simplejava_literal_expression_inteiro_setter(instance):
    original = instance.inteiro
    instance.inteiro = original
    assert instance.inteiro == original



@given(instance=simpleJava_literal_expression_strategy)
def test_simplejava_literal_expression_l_float_setter(instance):
    original = instance.l_float
    instance.l_float = original
    assert instance.l_float == original



@given(instance=simpleJava_literal_expression_strategy)
def test_simplejava_literal_expression_decimal_setter(instance):
    original = instance.decimal
    instance.decimal = original
    assert instance.decimal == original

@given(instance=simpleJava_bit_expression_strategy)
@settings(max_examples=50)
def test_simplejava_bit_expression_instantiation(instance):
    assert isinstance(instance, simpleJava_bit_expression)



@given(instance=simpleJava_bit_expression_strategy)
def test_simplejava_bit_expression_operador_setter(instance):
    original = instance.operador
    instance.operador = original
    assert instance.operador == original

@given(instance=simpleJava_numeric_expression_strategy)
@settings(max_examples=50)
def test_simplejava_numeric_expression_instantiation(instance):
    assert isinstance(instance, simpleJava_numeric_expression)



@given(instance=simpleJava_numeric_expression_strategy)
def test_simplejava_numeric_expression_operador_setter(instance):
    original = instance.operador
    instance.operador = original
    assert instance.operador == original

@given(instance=simpleJava_logical_expression_strategy)
@settings(max_examples=50)
def test_simplejava_logical_expression_instantiation(instance):
    assert isinstance(instance, simpleJava_logical_expression)



@given(instance=simpleJava_logical_expression_strategy)
def test_simplejava_logical_expression_operador_setter(instance):
    original = instance.operador
    instance.operador = original
    assert instance.operador == original

@given(instance=expression_aux_strategy)
@settings(max_examples=50)
def test_expression_aux_instantiation(instance):
    assert isinstance(instance, expression_aux)

@given(instance=expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, expression)

@given(instance=simpleJava_exp_aux_strategy)
@settings(max_examples=50)
def test_simplejava_exp_aux_instantiation(instance):
    assert isinstance(instance, simpleJava_exp_aux)

@given(instance=simpleJava_newBlock_strategy)
@settings(max_examples=50)
def test_simplejava_newblock_instantiation(instance):
    assert isinstance(instance, simpleJava_newBlock)

@given(instance=simpleJava_type_specifier_strategy)
@settings(max_examples=50)
def test_simplejava_type_specifier_instantiation(instance):
    assert isinstance(instance, simpleJava_type_specifier)



@given(instance=simpleJava_type_specifier_strategy)
def test_simplejava_type_specifier_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original

@given(instance=simpleJava_creating_aux_strategy)
@settings(max_examples=50)
def test_simplejava_creating_aux_instantiation(instance):
    assert isinstance(instance, simpleJava_creating_aux)

@given(instance=simpleJava_creating_expression_strategy)
@settings(max_examples=50)
def test_simplejava_creating_expression_instantiation(instance):
    assert isinstance(instance, simpleJava_creating_expression)

@given(instance=creating_aux_strategy)
@settings(max_examples=50)
def test_creating_aux_instantiation(instance):
    assert isinstance(instance, creating_aux)

@given(instance=simpleJava_aux_strategy)
@settings(max_examples=50)
def test_simplejava_aux_instantiation(instance):
    assert isinstance(instance, simpleJava_aux)

@given(instance=simpleJava_mais_aux_strategy)
@settings(max_examples=50)
def test_simplejava_mais_aux_instantiation(instance):
    assert isinstance(instance, simpleJava_mais_aux)



@given(instance=simpleJava_mais_aux_strategy)
def test_simplejava_mais_aux_operador_setter(instance):
    original = instance.operador
    instance.operador = original
    assert instance.operador == original

@given(instance=simpleJava_arglist_strategy)
@settings(max_examples=50)
def test_simplejava_arglist_instantiation(instance):
    assert isinstance(instance, simpleJava_arglist)



@given(instance=simpleJava_arglist_strategy)
def test_simplejava_arglist_nomeParametro_setter(instance):
    original = instance.nomeParametro
    instance.nomeParametro = original
    assert instance.nomeParametro == original

@given(instance=simpleJava_expression_aux_strategy)
@settings(max_examples=50)
def test_simplejava_expression_aux_instantiation(instance):
    assert isinstance(instance, simpleJava_expression_aux)



@given(instance=simpleJava_expression_aux_strategy)
def test_simplejava_expression_aux_operador_setter(instance):
    original = instance.operador
    instance.operador = original
    assert instance.operador == original

@given(instance=newBlock_strategy)
@settings(max_examples=50)
def test_newblock_instantiation(instance):
    assert isinstance(instance, newBlock)

@given(instance=simpleJava_variable_initializer_strategy)
@settings(max_examples=50)
def test_simplejava_variable_initializer_instantiation(instance):
    assert isinstance(instance, simpleJava_variable_initializer)

@given(instance=simpleJava_variable_declarator_strategy)
@settings(max_examples=50)
def test_simplejava_variable_declarator_instantiation(instance):
    assert isinstance(instance, simpleJava_variable_declarator)



@given(instance=simpleJava_variable_declarator_strategy)
def test_simplejava_variable_declarator_nomeVariavel_setter(instance):
    original = instance.nomeVariavel
    instance.nomeVariavel = original
    assert instance.nomeVariavel == original



@given(instance=simpleJava_variable_declarator_strategy)
def test_simplejava_variable_declarator_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=simpleJava_switch_statement_strategy)
@settings(max_examples=50)
def test_simplejava_switch_statement_instantiation(instance):
    assert isinstance(instance, simpleJava_switch_statement)

@given(instance=simpleJava_try_statement_strategy)
@settings(max_examples=50)
def test_simplejava_try_statement_instantiation(instance):
    assert isinstance(instance, simpleJava_try_statement)

@given(instance=simpleJava_for_statement_strategy)
@settings(max_examples=50)
def test_simplejava_for_statement_instantiation(instance):
    assert isinstance(instance, simpleJava_for_statement)

@given(instance=simpleJava_while_statement_strategy)
@settings(max_examples=50)
def test_simplejava_while_statement_instantiation(instance):
    assert isinstance(instance, simpleJava_while_statement)

@given(instance=simpleJava_parameter_strategy)
@settings(max_examples=50)
def test_simplejava_parameter_instantiation(instance):
    assert isinstance(instance, simpleJava_parameter)



@given(instance=simpleJava_parameter_strategy)
def test_simplejava_parameter_nomeParametro_setter(instance):
    original = instance.nomeParametro
    instance.nomeParametro = original
    assert instance.nomeParametro == original

@given(instance=simpleJava_statement_block_strategy)
@settings(max_examples=50)
def test_simplejava_statement_block_instantiation(instance):
    assert isinstance(instance, simpleJava_statement_block)

@given(instance=simpleJava_parameter_list_strategy)
@settings(max_examples=50)
def test_simplejava_parameter_list_instantiation(instance):
    assert isinstance(instance, simpleJava_parameter_list)

@given(instance=simpleJava_type_strategy)
@settings(max_examples=50)
def test_simplejava_type_instantiation(instance):
    assert isinstance(instance, simpleJava_type)

@given(instance=simpleJava_static_initializer_strategy)
@settings(max_examples=50)
def test_simplejava_static_initializer_instantiation(instance):
    assert isinstance(instance, simpleJava_static_initializer)

@given(instance=simpleJava_variable_declaration_strategy)
@settings(max_examples=50)
def test_simplejava_variable_declaration_instantiation(instance):
    assert isinstance(instance, simpleJava_variable_declaration)

@given(instance=simpleJava_constructor_declaration_strategy)
@settings(max_examples=50)
def test_simplejava_constructor_declaration_instantiation(instance):
    assert isinstance(instance, simpleJava_constructor_declaration)



@given(instance=simpleJava_constructor_declaration_strategy)
def test_simplejava_constructor_declaration_nomeContrutor_setter(instance):
    original = instance.nomeContrutor
    instance.nomeContrutor = original
    assert instance.nomeContrutor == original

@given(instance=simpleJava_method_declaration_strategy)
@settings(max_examples=50)
def test_simplejava_method_declaration_instantiation(instance):
    assert isinstance(instance, simpleJava_method_declaration)



@given(instance=simpleJava_method_declaration_strategy)
def test_simplejava_method_declaration_nomeMetodo_setter(instance):
    original = instance.nomeMetodo
    instance.nomeMetodo = original
    assert instance.nomeMetodo == original

@given(instance=simpleJava_field_declaration_strategy)
@settings(max_examples=50)
def test_simplejava_field_declaration_instantiation(instance):
    assert isinstance(instance, simpleJava_field_declaration)

@given(instance=simpleJava_do_statement_strategy)
@settings(max_examples=50)
def test_simplejava_do_statement_instantiation(instance):
    assert isinstance(instance, simpleJava_do_statement)

@given(instance=simpleJava_if_statement_strategy)
@settings(max_examples=50)
def test_simplejava_if_statement_instantiation(instance):
    assert isinstance(instance, simpleJava_if_statement)

@given(instance=simpleJava_expression_strategy)
@settings(max_examples=50)
def test_simplejava_expression_instantiation(instance):
    assert isinstance(instance, simpleJava_expression)



@given(instance=simpleJava_expression_strategy)
def test_simplejava_expression_identificador_setter(instance):
    original = instance.identificador
    instance.identificador = original
    assert instance.identificador == original

@given(instance=simpleJava_statement_strategy)
@settings(max_examples=50)
def test_simplejava_statement_instantiation(instance):
    assert isinstance(instance, simpleJava_statement)



@given(instance=simpleJava_statement_strategy)
def test_simplejava_statement_continue__setter(instance):
    original = instance.continue_
    instance.continue_ = original
    assert instance.continue_ == original



@given(instance=simpleJava_statement_strategy)
def test_simplejava_statement_break__setter(instance):
    original = instance.break_
    instance.break_ = original
    assert instance.break_ == original

@given(instance=simpleJava_type_declaration_strategy)
@settings(max_examples=50)
def test_simplejava_type_declaration_instantiation(instance):
    assert isinstance(instance, simpleJava_type_declaration)

@given(instance=simpleJava_import_statement_strategy)
@settings(max_examples=50)
def test_simplejava_import_statement_instantiation(instance):
    assert isinstance(instance, simpleJava_import_statement)

@given(instance=simpleJava_package_statement_strategy)
@settings(max_examples=50)
def test_simplejava_package_statement_instantiation(instance):
    assert isinstance(instance, simpleJava_package_statement)

@given(instance=Model_strategy)
@settings(max_examples=50)
def test_model_instantiation(instance):
    assert isinstance(instance, Model)

@given(instance=simpleJava_compilation_unit_strategy)
@settings(max_examples=50)
def test_simplejava_compilation_unit_instantiation(instance):
    assert isinstance(instance, simpleJava_compilation_unit)

@given(instance=simpleJava_Model_strategy)
@settings(max_examples=50)
def test_simplejava_model_instantiation(instance):
    assert isinstance(instance, simpleJava_Model)

@given(instance=simpleJava_MODIFIER_strategy)
@settings(max_examples=50)
def test_simplejava_modifier_instantiation(instance):
    assert isinstance(instance, simpleJava_MODIFIER)



@given(instance=simpleJava_MODIFIER_strategy)
def test_simplejava_modifier_modificador_setter(instance):
    original = instance.modificador
    instance.modificador = original
    assert instance.modificador == original

@given(instance=type_declaration_strategy)
@settings(max_examples=50)
def test_type_declaration_instantiation(instance):
    assert isinstance(instance, type_declaration)

@given(instance=simpleJava_doc_comment_strategy)
@settings(max_examples=50)
def test_simplejava_doc_comment_instantiation(instance):
    assert isinstance(instance, simpleJava_doc_comment)



@given(instance=simpleJava_doc_comment_strategy)
def test_simplejava_doc_comment_comentario_setter(instance):
    original = instance.comentario
    instance.comentario = original
    assert instance.comentario == original

@given(instance=simpleJava_interface_declaration_strategy)
@settings(max_examples=50)
def test_simplejava_interface_declaration_instantiation(instance):
    assert isinstance(instance, simpleJava_interface_declaration)



@given(instance=simpleJava_interface_declaration_strategy)
def test_simplejava_interface_declaration_nomeInterface_setter(instance):
    original = instance.nomeInterface
    instance.nomeInterface = original
    assert instance.nomeInterface == original

@given(instance=simpleJava_class_declaration_strategy)
@settings(max_examples=50)
def test_simplejava_class_declaration_instantiation(instance):
    assert isinstance(instance, simpleJava_class_declaration)



@given(instance=simpleJava_class_declaration_strategy)
def test_simplejava_class_declaration_nomeClasse_setter(instance):
    original = instance.nomeClasse
    instance.nomeClasse = original
    assert instance.nomeClasse == original

@given(instance=simpleJava_name_strategy)
@settings(max_examples=50)
def test_simplejava_name_instantiation(instance):
    assert isinstance(instance, simpleJava_name)



@given(instance=simpleJava_name_strategy)
def test_simplejava_name_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original
