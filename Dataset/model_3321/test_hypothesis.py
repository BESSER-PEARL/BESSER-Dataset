import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    myDsl_Creating_Expression,
    myDsl_Float_Literal,
    myDsl_Ampersand_Rule,
    myDsl_Arg_List,
    myDsl_Literal_Expression,
    myDsl_Cast_Expression,
    myDsl_Bit_Expression_NR,
    myDsl_Logical_Expression_NR,
    myDsl_Expression_aux,
    myDsl_Numeric_Expression_NR,
    myDsl_Try_statement,
    myDsl_Switch_statement,
    myDsl_For_Statement,
    myDsl_While_Statement,
    myDsl_Do_Statement,
    myDsl_If_statement,
    myDsl_Statement,
    myDsl_Type_specifier,
    myDsl_Expression,
    myDsl_Array_initializer,
    myDsl_Variable_initializer,
    myDsl_Variable_declarator,
    myDsl_Parameter,
    myDsl_Package_statement,
    myDsl_Statement_block,
    myDsl_Parameter_list,
    myDsl_Type,
    myDsl_Static_initializer,
    myDsl_Method_declaration,
    myDsl_Constructor_declaration,
    myDsl_Variable_declaration,
    myDsl_Field_declaration,
    myDsl_Interface_declaration,
    myDsl_Class_declaration,
    myDsl_Type_declaration,
    myDsl_Import_statement,
    myDsl_Compilation_unit,
    myDsl_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl_creating_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_Creating_Expression)


def test_mydsl_creating_expression_constructor_exists():
    assert callable(myDsl_Creating_Expression.__init__)


def test_mydsl_creating_expression_constructor_args():
    sig = inspect.signature(myDsl_Creating_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "className" in params, "Missing parameter 'className'"

def test_mydsl_creating_expression_has_className():
    assert hasattr(myDsl_Creating_Expression, "className")
    descriptor = None
    for klass in myDsl_Creating_Expression.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_float_literal_is_not_abstract():
    assert not inspect.isabstract(myDsl_Float_Literal)


def test_mydsl_float_literal_constructor_exists():
    assert callable(myDsl_Float_Literal.__init__)


def test_mydsl_float_literal_constructor_args():
    sig = inspect.signature(myDsl_Float_Literal.__init__)
    params = list(sig.parameters.keys())
    assert "exp" in params, "Missing parameter 'exp'"
    assert "floatTypeSufix" in params, "Missing parameter 'floatTypeSufix'"
    assert "decimalDigits2" in params, "Missing parameter 'decimalDigits2'"
    assert "decimalDigits1" in params, "Missing parameter 'decimalDigits1'"

def test_mydsl_float_literal_has_exp():
    assert hasattr(myDsl_Float_Literal, "exp")
    descriptor = None
    for klass in myDsl_Float_Literal.__mro__:
        if "exp" in klass.__dict__:
            descriptor = klass.__dict__["exp"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_float_literal_has_floatTypeSufix():
    assert hasattr(myDsl_Float_Literal, "floatTypeSufix")
    descriptor = None
    for klass in myDsl_Float_Literal.__mro__:
        if "floatTypeSufix" in klass.__dict__:
            descriptor = klass.__dict__["floatTypeSufix"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_float_literal_has_decimalDigits2():
    assert hasattr(myDsl_Float_Literal, "decimalDigits2")
    descriptor = None
    for klass in myDsl_Float_Literal.__mro__:
        if "decimalDigits2" in klass.__dict__:
            descriptor = klass.__dict__["decimalDigits2"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_float_literal_has_decimalDigits1():
    assert hasattr(myDsl_Float_Literal, "decimalDigits1")
    descriptor = None
    for klass in myDsl_Float_Literal.__mro__:
        if "decimalDigits1" in klass.__dict__:
            descriptor = klass.__dict__["decimalDigits1"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_ampersand_rule_is_not_abstract():
    assert not inspect.isabstract(myDsl_Ampersand_Rule)


def test_mydsl_ampersand_rule_constructor_exists():
    assert callable(myDsl_Ampersand_Rule.__init__)


def test_mydsl_ampersand_rule_constructor_args():
    sig = inspect.signature(myDsl_Ampersand_Rule.__init__)
    params = list(sig.parameters.keys())
    assert "a2" in params, "Missing parameter 'a2'"
    assert "a1" in params, "Missing parameter 'a1'"

def test_mydsl_ampersand_rule_has_a2():
    assert hasattr(myDsl_Ampersand_Rule, "a2")
    descriptor = None
    for klass in myDsl_Ampersand_Rule.__mro__:
        if "a2" in klass.__dict__:
            descriptor = klass.__dict__["a2"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_ampersand_rule_has_a1():
    assert hasattr(myDsl_Ampersand_Rule, "a1")
    descriptor = None
    for klass in myDsl_Ampersand_Rule.__mro__:
        if "a1" in klass.__dict__:
            descriptor = klass.__dict__["a1"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_arg_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_Arg_List)


def test_mydsl_arg_list_constructor_exists():
    assert callable(myDsl_Arg_List.__init__)


def test_mydsl_arg_list_constructor_args():
    sig = inspect.signature(myDsl_Arg_List.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_literal_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_Literal_Expression)


def test_mydsl_literal_expression_constructor_exists():
    assert callable(myDsl_Literal_Expression.__init__)


def test_mydsl_literal_expression_constructor_args():
    sig = inspect.signature(myDsl_Literal_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "exp1" in params, "Missing parameter 'exp1'"
    assert "string" in params, "Missing parameter 'string'"
    assert "charLit" in params, "Missing parameter 'charLit'"
    assert "exp" in params, "Missing parameter 'exp'"

def test_mydsl_literal_expression_has_exp1():
    assert hasattr(myDsl_Literal_Expression, "exp1")
    descriptor = None
    for klass in myDsl_Literal_Expression.__mro__:
        if "exp1" in klass.__dict__:
            descriptor = klass.__dict__["exp1"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_literal_expression_has_string():
    assert hasattr(myDsl_Literal_Expression, "string")
    descriptor = None
    for klass in myDsl_Literal_Expression.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_literal_expression_has_charLit():
    assert hasattr(myDsl_Literal_Expression, "charLit")
    descriptor = None
    for klass in myDsl_Literal_Expression.__mro__:
        if "charLit" in klass.__dict__:
            descriptor = klass.__dict__["charLit"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_literal_expression_has_exp():
    assert hasattr(myDsl_Literal_Expression, "exp")
    descriptor = None
    for klass in myDsl_Literal_Expression.__mro__:
        if "exp" in klass.__dict__:
            descriptor = klass.__dict__["exp"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_cast_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_Cast_Expression)


def test_mydsl_cast_expression_constructor_exists():
    assert callable(myDsl_Cast_Expression.__init__)


def test_mydsl_cast_expression_constructor_args():
    sig = inspect.signature(myDsl_Cast_Expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_bit_expression_nr_is_not_abstract():
    assert not inspect.isabstract(myDsl_Bit_Expression_NR)


def test_mydsl_bit_expression_nr_constructor_exists():
    assert callable(myDsl_Bit_Expression_NR.__init__)


def test_mydsl_bit_expression_nr_constructor_args():
    sig = inspect.signature(myDsl_Bit_Expression_NR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_logical_expression_nr_is_not_abstract():
    assert not inspect.isabstract(myDsl_Logical_Expression_NR)


def test_mydsl_logical_expression_nr_constructor_exists():
    assert callable(myDsl_Logical_Expression_NR.__init__)


def test_mydsl_logical_expression_nr_constructor_args():
    sig = inspect.signature(myDsl_Logical_Expression_NR.__init__)
    params = list(sig.parameters.keys())
    assert "false" in params, "Missing parameter 'false'"
    assert "true" in params, "Missing parameter 'true'"
    assert "exclamation" in params, "Missing parameter 'exclamation'"

def test_mydsl_logical_expression_nr_has_false():
    assert hasattr(myDsl_Logical_Expression_NR, "false")
    descriptor = None
    for klass in myDsl_Logical_Expression_NR.__mro__:
        if "false" in klass.__dict__:
            descriptor = klass.__dict__["false"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_logical_expression_nr_has_true():
    assert hasattr(myDsl_Logical_Expression_NR, "true")
    descriptor = None
    for klass in myDsl_Logical_Expression_NR.__mro__:
        if "true" in klass.__dict__:
            descriptor = klass.__dict__["true"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_logical_expression_nr_has_exclamation():
    assert hasattr(myDsl_Logical_Expression_NR, "exclamation")
    descriptor = None
    for klass in myDsl_Logical_Expression_NR.__mro__:
        if "exclamation" in klass.__dict__:
            descriptor = klass.__dict__["exclamation"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_expression_aux_is_not_abstract():
    assert not inspect.isabstract(myDsl_Expression_aux)


def test_mydsl_expression_aux_constructor_exists():
    assert callable(myDsl_Expression_aux.__init__)


def test_mydsl_expression_aux_constructor_args():
    sig = inspect.signature(myDsl_Expression_aux.__init__)
    params = list(sig.parameters.keys())
    assert "sgin" in params, "Missing parameter 'sgin'"
    assert "logicalSign" in params, "Missing parameter 'logicalSign'"
    assert "stringSign" in params, "Missing parameter 'stringSign'"
    assert "logicOp" in params, "Missing parameter 'logicOp'"
    assert "name" in params, "Missing parameter 'name'"
    assert "testingSign" in params, "Missing parameter 'testingSign'"
    assert "bitSign" in params, "Missing parameter 'bitSign'"
    assert "numericSign" in params, "Missing parameter 'numericSign'"

def test_mydsl_expression_aux_has_sgin():
    assert hasattr(myDsl_Expression_aux, "sgin")
    descriptor = None
    for klass in myDsl_Expression_aux.__mro__:
        if "sgin" in klass.__dict__:
            descriptor = klass.__dict__["sgin"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_expression_aux_has_logicalSign():
    assert hasattr(myDsl_Expression_aux, "logicalSign")
    descriptor = None
    for klass in myDsl_Expression_aux.__mro__:
        if "logicalSign" in klass.__dict__:
            descriptor = klass.__dict__["logicalSign"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_expression_aux_has_stringSign():
    assert hasattr(myDsl_Expression_aux, "stringSign")
    descriptor = None
    for klass in myDsl_Expression_aux.__mro__:
        if "stringSign" in klass.__dict__:
            descriptor = klass.__dict__["stringSign"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_expression_aux_has_logicOp():
    assert hasattr(myDsl_Expression_aux, "logicOp")
    descriptor = None
    for klass in myDsl_Expression_aux.__mro__:
        if "logicOp" in klass.__dict__:
            descriptor = klass.__dict__["logicOp"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_expression_aux_has_name():
    assert hasattr(myDsl_Expression_aux, "name")
    descriptor = None
    for klass in myDsl_Expression_aux.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_expression_aux_has_testingSign():
    assert hasattr(myDsl_Expression_aux, "testingSign")
    descriptor = None
    for klass in myDsl_Expression_aux.__mro__:
        if "testingSign" in klass.__dict__:
            descriptor = klass.__dict__["testingSign"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_expression_aux_has_bitSign():
    assert hasattr(myDsl_Expression_aux, "bitSign")
    descriptor = None
    for klass in myDsl_Expression_aux.__mro__:
        if "bitSign" in klass.__dict__:
            descriptor = klass.__dict__["bitSign"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_expression_aux_has_numericSign():
    assert hasattr(myDsl_Expression_aux, "numericSign")
    descriptor = None
    for klass in myDsl_Expression_aux.__mro__:
        if "numericSign" in klass.__dict__:
            descriptor = klass.__dict__["numericSign"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_numeric_expression_nr_is_not_abstract():
    assert not inspect.isabstract(myDsl_Numeric_Expression_NR)


def test_mydsl_numeric_expression_nr_constructor_exists():
    assert callable(myDsl_Numeric_Expression_NR.__init__)


def test_mydsl_numeric_expression_nr_constructor_args():
    sig = inspect.signature(myDsl_Numeric_Expression_NR.__init__)
    params = list(sig.parameters.keys())
    assert "sinal_numeric" in params, "Missing parameter 'sinal_numeric'"

def test_mydsl_numeric_expression_nr_has_sinal_numeric():
    assert hasattr(myDsl_Numeric_Expression_NR, "sinal_numeric")
    descriptor = None
    for klass in myDsl_Numeric_Expression_NR.__mro__:
        if "sinal_numeric" in klass.__dict__:
            descriptor = klass.__dict__["sinal_numeric"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_try_statement_is_not_abstract():
    assert not inspect.isabstract(myDsl_Try_statement)


def test_mydsl_try_statement_constructor_exists():
    assert callable(myDsl_Try_statement.__init__)


def test_mydsl_try_statement_constructor_args():
    sig = inspect.signature(myDsl_Try_statement.__init__)
    params = list(sig.parameters.keys())
    assert "rparent" in params, "Missing parameter 'rparent'"
    assert "lParen" in params, "Missing parameter 'lParen'"

def test_mydsl_try_statement_has_rparent():
    assert hasattr(myDsl_Try_statement, "rparent")
    descriptor = None
    for klass in myDsl_Try_statement.__mro__:
        if "rparent" in klass.__dict__:
            descriptor = klass.__dict__["rparent"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_try_statement_has_lParen():
    assert hasattr(myDsl_Try_statement, "lParen")
    descriptor = None
    for klass in myDsl_Try_statement.__mro__:
        if "lParen" in klass.__dict__:
            descriptor = klass.__dict__["lParen"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_switch_statement_is_not_abstract():
    assert not inspect.isabstract(myDsl_Switch_statement)


def test_mydsl_switch_statement_constructor_exists():
    assert callable(myDsl_Switch_statement.__init__)


def test_mydsl_switch_statement_constructor_args():
    sig = inspect.signature(myDsl_Switch_statement.__init__)
    params = list(sig.parameters.keys())
    assert "rparent" in params, "Missing parameter 'rparent'"
    assert "lParen" in params, "Missing parameter 'lParen'"

def test_mydsl_switch_statement_has_rparent():
    assert hasattr(myDsl_Switch_statement, "rparent")
    descriptor = None
    for klass in myDsl_Switch_statement.__mro__:
        if "rparent" in klass.__dict__:
            descriptor = klass.__dict__["rparent"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_switch_statement_has_lParen():
    assert hasattr(myDsl_Switch_statement, "lParen")
    descriptor = None
    for klass in myDsl_Switch_statement.__mro__:
        if "lParen" in klass.__dict__:
            descriptor = klass.__dict__["lParen"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_for_statement_is_not_abstract():
    assert not inspect.isabstract(myDsl_For_Statement)


def test_mydsl_for_statement_constructor_exists():
    assert callable(myDsl_For_Statement.__init__)


def test_mydsl_for_statement_constructor_args():
    sig = inspect.signature(myDsl_For_Statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_while_statement_is_not_abstract():
    assert not inspect.isabstract(myDsl_While_Statement)


def test_mydsl_while_statement_constructor_exists():
    assert callable(myDsl_While_Statement.__init__)


def test_mydsl_while_statement_constructor_args():
    sig = inspect.signature(myDsl_While_Statement.__init__)
    params = list(sig.parameters.keys())
    assert "rparent" in params, "Missing parameter 'rparent'"

def test_mydsl_while_statement_has_rparent():
    assert hasattr(myDsl_While_Statement, "rparent")
    descriptor = None
    for klass in myDsl_While_Statement.__mro__:
        if "rparent" in klass.__dict__:
            descriptor = klass.__dict__["rparent"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_do_statement_is_not_abstract():
    assert not inspect.isabstract(myDsl_Do_Statement)


def test_mydsl_do_statement_constructor_exists():
    assert callable(myDsl_Do_Statement.__init__)


def test_mydsl_do_statement_constructor_args():
    sig = inspect.signature(myDsl_Do_Statement.__init__)
    params = list(sig.parameters.keys())
    assert "rparent" in params, "Missing parameter 'rparent'"
    assert "lparent" in params, "Missing parameter 'lparent'"

def test_mydsl_do_statement_has_rparent():
    assert hasattr(myDsl_Do_Statement, "rparent")
    descriptor = None
    for klass in myDsl_Do_Statement.__mro__:
        if "rparent" in klass.__dict__:
            descriptor = klass.__dict__["rparent"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_do_statement_has_lparent():
    assert hasattr(myDsl_Do_Statement, "lparent")
    descriptor = None
    for klass in myDsl_Do_Statement.__mro__:
        if "lparent" in klass.__dict__:
            descriptor = klass.__dict__["lparent"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_if_statement_is_not_abstract():
    assert not inspect.isabstract(myDsl_If_statement)


def test_mydsl_if_statement_constructor_exists():
    assert callable(myDsl_If_statement.__init__)


def test_mydsl_if_statement_constructor_args():
    sig = inspect.signature(myDsl_If_statement.__init__)
    params = list(sig.parameters.keys())
    assert "rparent" in params, "Missing parameter 'rparent'"
    assert "lparen" in params, "Missing parameter 'lparen'"

def test_mydsl_if_statement_has_rparent():
    assert hasattr(myDsl_If_statement, "rparent")
    descriptor = None
    for klass in myDsl_If_statement.__mro__:
        if "rparent" in klass.__dict__:
            descriptor = klass.__dict__["rparent"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_if_statement_has_lparen():
    assert hasattr(myDsl_If_statement, "lparen")
    descriptor = None
    for klass in myDsl_If_statement.__mro__:
        if "lparen" in klass.__dict__:
            descriptor = klass.__dict__["lparen"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_statement_is_not_abstract():
    assert not inspect.isabstract(myDsl_Statement)


def test_mydsl_statement_constructor_exists():
    assert callable(myDsl_Statement.__init__)


def test_mydsl_statement_constructor_args():
    sig = inspect.signature(myDsl_Statement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "g" in params, "Missing parameter 'g'"
    assert "nameStatement" in params, "Missing parameter 'nameStatement'"
    assert "ret" in params, "Missing parameter 'ret'"
    assert "rparent" in params, "Missing parameter 'rparent'"

def test_mydsl_statement_has_name():
    assert hasattr(myDsl_Statement, "name")
    descriptor = None
    for klass in myDsl_Statement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_statement_has_g():
    assert hasattr(myDsl_Statement, "g")
    descriptor = None
    for klass in myDsl_Statement.__mro__:
        if "g" in klass.__dict__:
            descriptor = klass.__dict__["g"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_statement_has_nameStatement():
    assert hasattr(myDsl_Statement, "nameStatement")
    descriptor = None
    for klass in myDsl_Statement.__mro__:
        if "nameStatement" in klass.__dict__:
            descriptor = klass.__dict__["nameStatement"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_statement_has_ret():
    assert hasattr(myDsl_Statement, "ret")
    descriptor = None
    for klass in myDsl_Statement.__mro__:
        if "ret" in klass.__dict__:
            descriptor = klass.__dict__["ret"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_statement_has_rparent():
    assert hasattr(myDsl_Statement, "rparent")
    descriptor = None
    for klass in myDsl_Statement.__mro__:
        if "rparent" in klass.__dict__:
            descriptor = klass.__dict__["rparent"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_type_specifier_is_not_abstract():
    assert not inspect.isabstract(myDsl_Type_specifier)


def test_mydsl_type_specifier_constructor_exists():
    assert callable(myDsl_Type_specifier.__init__)


def test_mydsl_type_specifier_constructor_args():
    sig = inspect.signature(myDsl_Type_specifier.__init__)
    params = list(sig.parameters.keys())
    assert "className" in params, "Missing parameter 'className'"
    assert "primitiveType" in params, "Missing parameter 'primitiveType'"

def test_mydsl_type_specifier_has_className():
    assert hasattr(myDsl_Type_specifier, "className")
    descriptor = None
    for klass in myDsl_Type_specifier.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_type_specifier_has_primitiveType():
    assert hasattr(myDsl_Type_specifier, "primitiveType")
    descriptor = None
    for klass in myDsl_Type_specifier.__mro__:
        if "primitiveType" in klass.__dict__:
            descriptor = klass.__dict__["primitiveType"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_Expression)


def test_mydsl_expression_constructor_exists():
    assert callable(myDsl_Expression.__init__)


def test_mydsl_expression_constructor_args():
    sig = inspect.signature(myDsl_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "this" in params, "Missing parameter 'this'"
    assert "super" in params, "Missing parameter 'super'"
    assert "name" in params, "Missing parameter 'name'"
    assert "null" in params, "Missing parameter 'null'"

def test_mydsl_expression_has_this():
    assert hasattr(myDsl_Expression, "this")
    descriptor = None
    for klass in myDsl_Expression.__mro__:
        if "this" in klass.__dict__:
            descriptor = klass.__dict__["this"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_expression_has_super():
    assert hasattr(myDsl_Expression, "super")
    descriptor = None
    for klass in myDsl_Expression.__mro__:
        if "super" in klass.__dict__:
            descriptor = klass.__dict__["super"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_expression_has_name():
    assert hasattr(myDsl_Expression, "name")
    descriptor = None
    for klass in myDsl_Expression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_expression_has_null():
    assert hasattr(myDsl_Expression, "null")
    descriptor = None
    for klass in myDsl_Expression.__mro__:
        if "null" in klass.__dict__:
            descriptor = klass.__dict__["null"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_array_initializer_is_not_abstract():
    assert not inspect.isabstract(myDsl_Array_initializer)


def test_mydsl_array_initializer_constructor_exists():
    assert callable(myDsl_Array_initializer.__init__)


def test_mydsl_array_initializer_constructor_args():
    sig = inspect.signature(myDsl_Array_initializer.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_variable_initializer_is_not_abstract():
    assert not inspect.isabstract(myDsl_Variable_initializer)


def test_mydsl_variable_initializer_constructor_exists():
    assert callable(myDsl_Variable_initializer.__init__)


def test_mydsl_variable_initializer_constructor_args():
    sig = inspect.signature(myDsl_Variable_initializer.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_variable_declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl_Variable_declarator)


def test_mydsl_variable_declarator_constructor_exists():
    assert callable(myDsl_Variable_declarator.__init__)


def test_mydsl_variable_declarator_constructor_args():
    sig = inspect.signature(myDsl_Variable_declarator.__init__)
    params = list(sig.parameters.keys())
    assert "nameVariable" in params, "Missing parameter 'nameVariable'"
    assert "lenVector" in params, "Missing parameter 'lenVector'"

def test_mydsl_variable_declarator_has_nameVariable():
    assert hasattr(myDsl_Variable_declarator, "nameVariable")
    descriptor = None
    for klass in myDsl_Variable_declarator.__mro__:
        if "nameVariable" in klass.__dict__:
            descriptor = klass.__dict__["nameVariable"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_variable_declarator_has_lenVector():
    assert hasattr(myDsl_Variable_declarator, "lenVector")
    descriptor = None
    for klass in myDsl_Variable_declarator.__mro__:
        if "lenVector" in klass.__dict__:
            descriptor = klass.__dict__["lenVector"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_parameter_is_not_abstract():
    assert not inspect.isabstract(myDsl_Parameter)


def test_mydsl_parameter_constructor_exists():
    assert callable(myDsl_Parameter.__init__)


def test_mydsl_parameter_constructor_args():
    sig = inspect.signature(myDsl_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "parameterName" in params, "Missing parameter 'parameterName'"

def test_mydsl_parameter_has_parameterName():
    assert hasattr(myDsl_Parameter, "parameterName")
    descriptor = None
    for klass in myDsl_Parameter.__mro__:
        if "parameterName" in klass.__dict__:
            descriptor = klass.__dict__["parameterName"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_package_statement_is_not_abstract():
    assert not inspect.isabstract(myDsl_Package_statement)


def test_mydsl_package_statement_constructor_exists():
    assert callable(myDsl_Package_statement.__init__)


def test_mydsl_package_statement_constructor_args():
    sig = inspect.signature(myDsl_Package_statement.__init__)
    params = list(sig.parameters.keys())
    assert "pacName" in params, "Missing parameter 'pacName'"

def test_mydsl_package_statement_has_pacName():
    assert hasattr(myDsl_Package_statement, "pacName")
    descriptor = None
    for klass in myDsl_Package_statement.__mro__:
        if "pacName" in klass.__dict__:
            descriptor = klass.__dict__["pacName"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_statement_block_is_not_abstract():
    assert not inspect.isabstract(myDsl_Statement_block)


def test_mydsl_statement_block_constructor_exists():
    assert callable(myDsl_Statement_block.__init__)


def test_mydsl_statement_block_constructor_args():
    sig = inspect.signature(myDsl_Statement_block.__init__)
    params = list(sig.parameters.keys())
    assert "rCurly" in params, "Missing parameter 'rCurly'"
    assert "lCurly" in params, "Missing parameter 'lCurly'"

def test_mydsl_statement_block_has_rCurly():
    assert hasattr(myDsl_Statement_block, "rCurly")
    descriptor = None
    for klass in myDsl_Statement_block.__mro__:
        if "rCurly" in klass.__dict__:
            descriptor = klass.__dict__["rCurly"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_statement_block_has_lCurly():
    assert hasattr(myDsl_Statement_block, "lCurly")
    descriptor = None
    for klass in myDsl_Statement_block.__mro__:
        if "lCurly" in klass.__dict__:
            descriptor = klass.__dict__["lCurly"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_parameter_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_Parameter_list)


def test_mydsl_parameter_list_constructor_exists():
    assert callable(myDsl_Parameter_list.__init__)


def test_mydsl_parameter_list_constructor_args():
    sig = inspect.signature(myDsl_Parameter_list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_type_is_not_abstract():
    assert not inspect.isabstract(myDsl_Type)


def test_mydsl_type_constructor_exists():
    assert callable(myDsl_Type.__init__)


def test_mydsl_type_constructor_args():
    sig = inspect.signature(myDsl_Type.__init__)
    params = list(sig.parameters.keys())
    assert "typeVector" in params, "Missing parameter 'typeVector'"

def test_mydsl_type_has_typeVector():
    assert hasattr(myDsl_Type, "typeVector")
    descriptor = None
    for klass in myDsl_Type.__mro__:
        if "typeVector" in klass.__dict__:
            descriptor = klass.__dict__["typeVector"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_static_initializer_is_not_abstract():
    assert not inspect.isabstract(myDsl_Static_initializer)


def test_mydsl_static_initializer_constructor_exists():
    assert callable(myDsl_Static_initializer.__init__)


def test_mydsl_static_initializer_constructor_args():
    sig = inspect.signature(myDsl_Static_initializer.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_mydsl_static_initializer_has_static():
    assert hasattr(myDsl_Static_initializer, "static")
    descriptor = None
    for klass in myDsl_Static_initializer.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_method_declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl_Method_declaration)


def test_mydsl_method_declaration_constructor_exists():
    assert callable(myDsl_Method_declaration.__init__)


def test_mydsl_method_declaration_constructor_args():
    sig = inspect.signature(myDsl_Method_declaration.__init__)
    params = list(sig.parameters.keys())
    assert "nameMethod" in params, "Missing parameter 'nameMethod'"
    assert "rparent" in params, "Missing parameter 'rparent'"
    assert "debug" in params, "Missing parameter 'debug'"
    assert "modifiersMethod" in params, "Missing parameter 'modifiersMethod'"
    assert "lParen" in params, "Missing parameter 'lParen'"

def test_mydsl_method_declaration_has_nameMethod():
    assert hasattr(myDsl_Method_declaration, "nameMethod")
    descriptor = None
    for klass in myDsl_Method_declaration.__mro__:
        if "nameMethod" in klass.__dict__:
            descriptor = klass.__dict__["nameMethod"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_method_declaration_has_rparent():
    assert hasattr(myDsl_Method_declaration, "rparent")
    descriptor = None
    for klass in myDsl_Method_declaration.__mro__:
        if "rparent" in klass.__dict__:
            descriptor = klass.__dict__["rparent"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_method_declaration_has_debug():
    assert hasattr(myDsl_Method_declaration, "debug")
    descriptor = None
    for klass in myDsl_Method_declaration.__mro__:
        if "debug" in klass.__dict__:
            descriptor = klass.__dict__["debug"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_method_declaration_has_modifiersMethod():
    assert hasattr(myDsl_Method_declaration, "modifiersMethod")
    descriptor = None
    for klass in myDsl_Method_declaration.__mro__:
        if "modifiersMethod" in klass.__dict__:
            descriptor = klass.__dict__["modifiersMethod"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_method_declaration_has_lParen():
    assert hasattr(myDsl_Method_declaration, "lParen")
    descriptor = None
    for klass in myDsl_Method_declaration.__mro__:
        if "lParen" in klass.__dict__:
            descriptor = klass.__dict__["lParen"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_constructor_declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl_Constructor_declaration)


def test_mydsl_constructor_declaration_constructor_exists():
    assert callable(myDsl_Constructor_declaration.__init__)


def test_mydsl_constructor_declaration_constructor_args():
    sig = inspect.signature(myDsl_Constructor_declaration.__init__)
    params = list(sig.parameters.keys())
    assert "rparent" in params, "Missing parameter 'rparent'"
    assert "lParen" in params, "Missing parameter 'lParen'"
    assert "modifiersConstructor" in params, "Missing parameter 'modifiersConstructor'"
    assert "nameConstructor" in params, "Missing parameter 'nameConstructor'"

def test_mydsl_constructor_declaration_has_rparent():
    assert hasattr(myDsl_Constructor_declaration, "rparent")
    descriptor = None
    for klass in myDsl_Constructor_declaration.__mro__:
        if "rparent" in klass.__dict__:
            descriptor = klass.__dict__["rparent"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_constructor_declaration_has_lParen():
    assert hasattr(myDsl_Constructor_declaration, "lParen")
    descriptor = None
    for klass in myDsl_Constructor_declaration.__mro__:
        if "lParen" in klass.__dict__:
            descriptor = klass.__dict__["lParen"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_constructor_declaration_has_modifiersConstructor():
    assert hasattr(myDsl_Constructor_declaration, "modifiersConstructor")
    descriptor = None
    for klass in myDsl_Constructor_declaration.__mro__:
        if "modifiersConstructor" in klass.__dict__:
            descriptor = klass.__dict__["modifiersConstructor"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_constructor_declaration_has_nameConstructor():
    assert hasattr(myDsl_Constructor_declaration, "nameConstructor")
    descriptor = None
    for klass in myDsl_Constructor_declaration.__mro__:
        if "nameConstructor" in klass.__dict__:
            descriptor = klass.__dict__["nameConstructor"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_variable_declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl_Variable_declaration)


def test_mydsl_variable_declaration_constructor_exists():
    assert callable(myDsl_Variable_declaration.__init__)


def test_mydsl_variable_declaration_constructor_args():
    sig = inspect.signature(myDsl_Variable_declaration.__init__)
    params = list(sig.parameters.keys())
    assert "modifiersVariable" in params, "Missing parameter 'modifiersVariable'"

def test_mydsl_variable_declaration_has_modifiersVariable():
    assert hasattr(myDsl_Variable_declaration, "modifiersVariable")
    descriptor = None
    for klass in myDsl_Variable_declaration.__mro__:
        if "modifiersVariable" in klass.__dict__:
            descriptor = klass.__dict__["modifiersVariable"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_field_declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl_Field_declaration)


def test_mydsl_field_declaration_constructor_exists():
    assert callable(myDsl_Field_declaration.__init__)


def test_mydsl_field_declaration_constructor_args():
    sig = inspect.signature(myDsl_Field_declaration.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_mydsl_field_declaration_has_comment():
    assert hasattr(myDsl_Field_declaration, "comment")
    descriptor = None
    for klass in myDsl_Field_declaration.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_interface_declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl_Interface_declaration)


def test_mydsl_interface_declaration_constructor_exists():
    assert callable(myDsl_Interface_declaration.__init__)


def test_mydsl_interface_declaration_constructor_args():
    sig = inspect.signature(myDsl_Interface_declaration.__init__)
    params = list(sig.parameters.keys())
    assert "interfaceHerdada" in params, "Missing parameter 'interfaceHerdada'"
    assert "interfacesHerdadas" in params, "Missing parameter 'interfacesHerdadas'"
    assert "modifiers" in params, "Missing parameter 'modifiers'"
    assert "interfaceName" in params, "Missing parameter 'interfaceName'"

def test_mydsl_interface_declaration_has_interfaceHerdada():
    assert hasattr(myDsl_Interface_declaration, "interfaceHerdada")
    descriptor = None
    for klass in myDsl_Interface_declaration.__mro__:
        if "interfaceHerdada" in klass.__dict__:
            descriptor = klass.__dict__["interfaceHerdada"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_interface_declaration_has_interfacesHerdadas():
    assert hasattr(myDsl_Interface_declaration, "interfacesHerdadas")
    descriptor = None
    for klass in myDsl_Interface_declaration.__mro__:
        if "interfacesHerdadas" in klass.__dict__:
            descriptor = klass.__dict__["interfacesHerdadas"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_interface_declaration_has_modifiers():
    assert hasattr(myDsl_Interface_declaration, "modifiers")
    descriptor = None
    for klass in myDsl_Interface_declaration.__mro__:
        if "modifiers" in klass.__dict__:
            descriptor = klass.__dict__["modifiers"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_interface_declaration_has_interfaceName():
    assert hasattr(myDsl_Interface_declaration, "interfaceName")
    descriptor = None
    for klass in myDsl_Interface_declaration.__mro__:
        if "interfaceName" in klass.__dict__:
            descriptor = klass.__dict__["interfaceName"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_class_declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl_Class_declaration)


def test_mydsl_class_declaration_constructor_exists():
    assert callable(myDsl_Class_declaration.__init__)


def test_mydsl_class_declaration_constructor_args():
    sig = inspect.signature(myDsl_Class_declaration.__init__)
    params = list(sig.parameters.keys())
    assert "className" in params, "Missing parameter 'className'"
    assert "classHerdada" in params, "Missing parameter 'classHerdada'"
    assert "modifiers" in params, "Missing parameter 'modifiers'"
    assert "interfaceImplementada" in params, "Missing parameter 'interfaceImplementada'"
    assert "interfacesImplementadas" in params, "Missing parameter 'interfacesImplementadas'"

def test_mydsl_class_declaration_has_className():
    assert hasattr(myDsl_Class_declaration, "className")
    descriptor = None
    for klass in myDsl_Class_declaration.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_class_declaration_has_classHerdada():
    assert hasattr(myDsl_Class_declaration, "classHerdada")
    descriptor = None
    for klass in myDsl_Class_declaration.__mro__:
        if "classHerdada" in klass.__dict__:
            descriptor = klass.__dict__["classHerdada"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_class_declaration_has_modifiers():
    assert hasattr(myDsl_Class_declaration, "modifiers")
    descriptor = None
    for klass in myDsl_Class_declaration.__mro__:
        if "modifiers" in klass.__dict__:
            descriptor = klass.__dict__["modifiers"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_class_declaration_has_interfaceImplementada():
    assert hasattr(myDsl_Class_declaration, "interfaceImplementada")
    descriptor = None
    for klass in myDsl_Class_declaration.__mro__:
        if "interfaceImplementada" in klass.__dict__:
            descriptor = klass.__dict__["interfaceImplementada"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_class_declaration_has_interfacesImplementadas():
    assert hasattr(myDsl_Class_declaration, "interfacesImplementadas")
    descriptor = None
    for klass in myDsl_Class_declaration.__mro__:
        if "interfacesImplementadas" in klass.__dict__:
            descriptor = klass.__dict__["interfacesImplementadas"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_type_declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl_Type_declaration)


def test_mydsl_type_declaration_constructor_exists():
    assert callable(myDsl_Type_declaration.__init__)


def test_mydsl_type_declaration_constructor_args():
    sig = inspect.signature(myDsl_Type_declaration.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_mydsl_type_declaration_has_comment():
    assert hasattr(myDsl_Type_declaration, "comment")
    descriptor = None
    for klass in myDsl_Type_declaration.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_import_statement_is_not_abstract():
    assert not inspect.isabstract(myDsl_Import_statement)


def test_mydsl_import_statement_constructor_exists():
    assert callable(myDsl_Import_statement.__init__)


def test_mydsl_import_statement_constructor_args():
    sig = inspect.signature(myDsl_Import_statement.__init__)
    params = list(sig.parameters.keys())
    assert "className" in params, "Missing parameter 'className'"
    assert "pacName" in params, "Missing parameter 'pacName'"

def test_mydsl_import_statement_has_className():
    assert hasattr(myDsl_Import_statement, "className")
    descriptor = None
    for klass in myDsl_Import_statement.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_import_statement_has_pacName():
    assert hasattr(myDsl_Import_statement, "pacName")
    descriptor = None
    for klass in myDsl_Import_statement.__mro__:
        if "pacName" in klass.__dict__:
            descriptor = klass.__dict__["pacName"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_compilation_unit_is_not_abstract():
    assert not inspect.isabstract(myDsl_Compilation_unit)


def test_mydsl_compilation_unit_constructor_exists():
    assert callable(myDsl_Compilation_unit.__init__)


def test_mydsl_compilation_unit_constructor_args():
    sig = inspect.signature(myDsl_Compilation_unit.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_model_is_not_abstract():
    assert not inspect.isabstract(myDsl_Model)


def test_mydsl_model_constructor_exists():
    assert callable(myDsl_Model.__init__)


def test_mydsl_model_constructor_args():
    sig = inspect.signature(myDsl_Model.__init__)
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
myDsl_Creating_Expression_strategy = st.builds(
    myDsl_Creating_Expression,
    className=
        safe_text
)
myDsl_Float_Literal_strategy = st.builds(
    myDsl_Float_Literal,
    exp=
        safe_text,
    floatTypeSufix=
        safe_text,
    decimalDigits2=
        st.integers(),
    decimalDigits1=
        st.integers()
)
myDsl_Ampersand_Rule_strategy = st.builds(
    myDsl_Ampersand_Rule,
    a2=
        safe_text,
    a1=
        safe_text
)
myDsl_Arg_List_strategy = st.builds(
    myDsl_Arg_List,
)
myDsl_Literal_Expression_strategy = st.builds(
    myDsl_Literal_Expression,
    exp1=
        st.integers(),
    string=
        safe_text,
    charLit=
        safe_text,
    exp=
        safe_text
)
myDsl_Cast_Expression_strategy = st.builds(
    myDsl_Cast_Expression,
)
myDsl_Bit_Expression_NR_strategy = st.builds(
    myDsl_Bit_Expression_NR,
)
myDsl_Logical_Expression_NR_strategy = st.builds(
    myDsl_Logical_Expression_NR,
    false=
        safe_text,
    true=
        safe_text,
    exclamation=
        safe_text
)
myDsl_Expression_aux_strategy = st.builds(
    myDsl_Expression_aux,
    sgin=
        safe_text,
    logicalSign=
        safe_text,
    stringSign=
        safe_text,
    logicOp=
        safe_text,
    name=
        safe_text,
    testingSign=
        safe_text,
    bitSign=
        safe_text,
    numericSign=
        safe_text
)
myDsl_Numeric_Expression_NR_strategy = st.builds(
    myDsl_Numeric_Expression_NR,
    sinal_numeric=
        safe_text
)
myDsl_Try_statement_strategy = st.builds(
    myDsl_Try_statement,
    rparent=
        safe_text,
    lParen=
        safe_text
)
myDsl_Switch_statement_strategy = st.builds(
    myDsl_Switch_statement,
    rparent=
        safe_text,
    lParen=
        safe_text
)
myDsl_For_Statement_strategy = st.builds(
    myDsl_For_Statement,
)
myDsl_While_Statement_strategy = st.builds(
    myDsl_While_Statement,
    rparent=
        safe_text
)
myDsl_Do_Statement_strategy = st.builds(
    myDsl_Do_Statement,
    rparent=
        safe_text,
    lparent=
        safe_text
)
myDsl_If_statement_strategy = st.builds(
    myDsl_If_statement,
    rparent=
        safe_text,
    lparen=
        safe_text
)
myDsl_Statement_strategy = st.builds(
    myDsl_Statement,
    name=
        safe_text,
    g=
        safe_text,
    nameStatement=
        safe_text,
    ret=
        safe_text,
    rparent=
        safe_text
)
myDsl_Type_specifier_strategy = st.builds(
    myDsl_Type_specifier,
    className=
        safe_text,
    primitiveType=
        safe_text
)
myDsl_Expression_strategy = st.builds(
    myDsl_Expression,
    this=
        safe_text,
    super=
        safe_text,
    name=
        safe_text,
    null=
        safe_text
)
myDsl_Array_initializer_strategy = st.builds(
    myDsl_Array_initializer,
)
myDsl_Variable_initializer_strategy = st.builds(
    myDsl_Variable_initializer,
)
myDsl_Variable_declarator_strategy = st.builds(
    myDsl_Variable_declarator,
    nameVariable=
        safe_text,
    lenVector=
        safe_text
)
myDsl_Parameter_strategy = st.builds(
    myDsl_Parameter,
    parameterName=
        safe_text
)
myDsl_Package_statement_strategy = st.builds(
    myDsl_Package_statement,
    pacName=
        safe_text
)
myDsl_Statement_block_strategy = st.builds(
    myDsl_Statement_block,
    rCurly=
        safe_text,
    lCurly=
        safe_text
)
myDsl_Parameter_list_strategy = st.builds(
    myDsl_Parameter_list,
)
myDsl_Type_strategy = st.builds(
    myDsl_Type,
    typeVector=
        safe_text
)
myDsl_Static_initializer_strategy = st.builds(
    myDsl_Static_initializer,
    static=
        safe_text
)
myDsl_Method_declaration_strategy = st.builds(
    myDsl_Method_declaration,
    nameMethod=
        safe_text,
    rparent=
        safe_text,
    debug=
        safe_text,
    modifiersMethod=
        safe_text,
    lParen=
        safe_text
)
myDsl_Constructor_declaration_strategy = st.builds(
    myDsl_Constructor_declaration,
    rparent=
        safe_text,
    lParen=
        safe_text,
    modifiersConstructor=
        safe_text,
    nameConstructor=
        safe_text
)
myDsl_Variable_declaration_strategy = st.builds(
    myDsl_Variable_declaration,
    modifiersVariable=
        safe_text
)
myDsl_Field_declaration_strategy = st.builds(
    myDsl_Field_declaration,
    comment=
        safe_text
)
myDsl_Interface_declaration_strategy = st.builds(
    myDsl_Interface_declaration,
    interfaceHerdada=
        safe_text,
    interfacesHerdadas=
        safe_text,
    modifiers=
        safe_text,
    interfaceName=
        safe_text
)
myDsl_Class_declaration_strategy = st.builds(
    myDsl_Class_declaration,
    className=
        safe_text,
    classHerdada=
        safe_text,
    modifiers=
        safe_text,
    interfaceImplementada=
        safe_text,
    interfacesImplementadas=
        safe_text
)
myDsl_Type_declaration_strategy = st.builds(
    myDsl_Type_declaration,
    comment=
        safe_text
)
myDsl_Import_statement_strategy = st.builds(
    myDsl_Import_statement,
    className=
        safe_text,
    pacName=
        safe_text
)
myDsl_Compilation_unit_strategy = st.builds(
    myDsl_Compilation_unit,
)
myDsl_Model_strategy = st.builds(
    myDsl_Model,
)

@given(instance=myDsl_Creating_Expression_strategy)
@settings(max_examples=50)
def test_mydsl_creating_expression_instantiation(instance):
    assert isinstance(instance, myDsl_Creating_Expression)



@given(instance=myDsl_Creating_Expression_strategy)
def test_mydsl_creating_expression_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=myDsl_Float_Literal_strategy)
@settings(max_examples=50)
def test_mydsl_float_literal_instantiation(instance):
    assert isinstance(instance, myDsl_Float_Literal)



@given(instance=myDsl_Float_Literal_strategy)
def test_mydsl_float_literal_exp_setter(instance):
    original = instance.exp
    instance.exp = original
    assert instance.exp == original



@given(instance=myDsl_Float_Literal_strategy)
def test_mydsl_float_literal_floatTypeSufix_setter(instance):
    original = instance.floatTypeSufix
    instance.floatTypeSufix = original
    assert instance.floatTypeSufix == original



@given(instance=myDsl_Float_Literal_strategy)
def test_mydsl_float_literal_decimalDigits2_setter(instance):
    original = instance.decimalDigits2
    instance.decimalDigits2 = original
    assert instance.decimalDigits2 == original



@given(instance=myDsl_Float_Literal_strategy)
def test_mydsl_float_literal_decimalDigits1_setter(instance):
    original = instance.decimalDigits1
    instance.decimalDigits1 = original
    assert instance.decimalDigits1 == original

@given(instance=myDsl_Ampersand_Rule_strategy)
@settings(max_examples=50)
def test_mydsl_ampersand_rule_instantiation(instance):
    assert isinstance(instance, myDsl_Ampersand_Rule)



@given(instance=myDsl_Ampersand_Rule_strategy)
def test_mydsl_ampersand_rule_a2_setter(instance):
    original = instance.a2
    instance.a2 = original
    assert instance.a2 == original



@given(instance=myDsl_Ampersand_Rule_strategy)
def test_mydsl_ampersand_rule_a1_setter(instance):
    original = instance.a1
    instance.a1 = original
    assert instance.a1 == original

@given(instance=myDsl_Arg_List_strategy)
@settings(max_examples=50)
def test_mydsl_arg_list_instantiation(instance):
    assert isinstance(instance, myDsl_Arg_List)

@given(instance=myDsl_Literal_Expression_strategy)
@settings(max_examples=50)
def test_mydsl_literal_expression_instantiation(instance):
    assert isinstance(instance, myDsl_Literal_Expression)



@given(instance=myDsl_Literal_Expression_strategy)
def test_mydsl_literal_expression_exp1_setter(instance):
    original = instance.exp1
    instance.exp1 = original
    assert instance.exp1 == original



@given(instance=myDsl_Literal_Expression_strategy)
def test_mydsl_literal_expression_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original



@given(instance=myDsl_Literal_Expression_strategy)
def test_mydsl_literal_expression_charLit_setter(instance):
    original = instance.charLit
    instance.charLit = original
    assert instance.charLit == original



@given(instance=myDsl_Literal_Expression_strategy)
def test_mydsl_literal_expression_exp_setter(instance):
    original = instance.exp
    instance.exp = original
    assert instance.exp == original

@given(instance=myDsl_Cast_Expression_strategy)
@settings(max_examples=50)
def test_mydsl_cast_expression_instantiation(instance):
    assert isinstance(instance, myDsl_Cast_Expression)

@given(instance=myDsl_Bit_Expression_NR_strategy)
@settings(max_examples=50)
def test_mydsl_bit_expression_nr_instantiation(instance):
    assert isinstance(instance, myDsl_Bit_Expression_NR)

@given(instance=myDsl_Logical_Expression_NR_strategy)
@settings(max_examples=50)
def test_mydsl_logical_expression_nr_instantiation(instance):
    assert isinstance(instance, myDsl_Logical_Expression_NR)



@given(instance=myDsl_Logical_Expression_NR_strategy)
def test_mydsl_logical_expression_nr_false_setter(instance):
    original = instance.false
    instance.false = original
    assert instance.false == original



@given(instance=myDsl_Logical_Expression_NR_strategy)
def test_mydsl_logical_expression_nr_true_setter(instance):
    original = instance.true
    instance.true = original
    assert instance.true == original



@given(instance=myDsl_Logical_Expression_NR_strategy)
def test_mydsl_logical_expression_nr_exclamation_setter(instance):
    original = instance.exclamation
    instance.exclamation = original
    assert instance.exclamation == original

@given(instance=myDsl_Expression_aux_strategy)
@settings(max_examples=50)
def test_mydsl_expression_aux_instantiation(instance):
    assert isinstance(instance, myDsl_Expression_aux)



@given(instance=myDsl_Expression_aux_strategy)
def test_mydsl_expression_aux_sgin_setter(instance):
    original = instance.sgin
    instance.sgin = original
    assert instance.sgin == original



@given(instance=myDsl_Expression_aux_strategy)
def test_mydsl_expression_aux_logicalSign_setter(instance):
    original = instance.logicalSign
    instance.logicalSign = original
    assert instance.logicalSign == original



@given(instance=myDsl_Expression_aux_strategy)
def test_mydsl_expression_aux_stringSign_setter(instance):
    original = instance.stringSign
    instance.stringSign = original
    assert instance.stringSign == original



@given(instance=myDsl_Expression_aux_strategy)
def test_mydsl_expression_aux_logicOp_setter(instance):
    original = instance.logicOp
    instance.logicOp = original
    assert instance.logicOp == original



@given(instance=myDsl_Expression_aux_strategy)
def test_mydsl_expression_aux_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=myDsl_Expression_aux_strategy)
def test_mydsl_expression_aux_testingSign_setter(instance):
    original = instance.testingSign
    instance.testingSign = original
    assert instance.testingSign == original



@given(instance=myDsl_Expression_aux_strategy)
def test_mydsl_expression_aux_bitSign_setter(instance):
    original = instance.bitSign
    instance.bitSign = original
    assert instance.bitSign == original



@given(instance=myDsl_Expression_aux_strategy)
def test_mydsl_expression_aux_numericSign_setter(instance):
    original = instance.numericSign
    instance.numericSign = original
    assert instance.numericSign == original

@given(instance=myDsl_Numeric_Expression_NR_strategy)
@settings(max_examples=50)
def test_mydsl_numeric_expression_nr_instantiation(instance):
    assert isinstance(instance, myDsl_Numeric_Expression_NR)



@given(instance=myDsl_Numeric_Expression_NR_strategy)
def test_mydsl_numeric_expression_nr_sinal_numeric_setter(instance):
    original = instance.sinal_numeric
    instance.sinal_numeric = original
    assert instance.sinal_numeric == original

@given(instance=myDsl_Try_statement_strategy)
@settings(max_examples=50)
def test_mydsl_try_statement_instantiation(instance):
    assert isinstance(instance, myDsl_Try_statement)



@given(instance=myDsl_Try_statement_strategy)
def test_mydsl_try_statement_rparent_setter(instance):
    original = instance.rparent
    instance.rparent = original
    assert instance.rparent == original



@given(instance=myDsl_Try_statement_strategy)
def test_mydsl_try_statement_lParen_setter(instance):
    original = instance.lParen
    instance.lParen = original
    assert instance.lParen == original

@given(instance=myDsl_Switch_statement_strategy)
@settings(max_examples=50)
def test_mydsl_switch_statement_instantiation(instance):
    assert isinstance(instance, myDsl_Switch_statement)



@given(instance=myDsl_Switch_statement_strategy)
def test_mydsl_switch_statement_rparent_setter(instance):
    original = instance.rparent
    instance.rparent = original
    assert instance.rparent == original



@given(instance=myDsl_Switch_statement_strategy)
def test_mydsl_switch_statement_lParen_setter(instance):
    original = instance.lParen
    instance.lParen = original
    assert instance.lParen == original

@given(instance=myDsl_For_Statement_strategy)
@settings(max_examples=50)
def test_mydsl_for_statement_instantiation(instance):
    assert isinstance(instance, myDsl_For_Statement)

@given(instance=myDsl_While_Statement_strategy)
@settings(max_examples=50)
def test_mydsl_while_statement_instantiation(instance):
    assert isinstance(instance, myDsl_While_Statement)



@given(instance=myDsl_While_Statement_strategy)
def test_mydsl_while_statement_rparent_setter(instance):
    original = instance.rparent
    instance.rparent = original
    assert instance.rparent == original

@given(instance=myDsl_Do_Statement_strategy)
@settings(max_examples=50)
def test_mydsl_do_statement_instantiation(instance):
    assert isinstance(instance, myDsl_Do_Statement)



@given(instance=myDsl_Do_Statement_strategy)
def test_mydsl_do_statement_rparent_setter(instance):
    original = instance.rparent
    instance.rparent = original
    assert instance.rparent == original



@given(instance=myDsl_Do_Statement_strategy)
def test_mydsl_do_statement_lparent_setter(instance):
    original = instance.lparent
    instance.lparent = original
    assert instance.lparent == original

@given(instance=myDsl_If_statement_strategy)
@settings(max_examples=50)
def test_mydsl_if_statement_instantiation(instance):
    assert isinstance(instance, myDsl_If_statement)



@given(instance=myDsl_If_statement_strategy)
def test_mydsl_if_statement_rparent_setter(instance):
    original = instance.rparent
    instance.rparent = original
    assert instance.rparent == original



@given(instance=myDsl_If_statement_strategy)
def test_mydsl_if_statement_lparen_setter(instance):
    original = instance.lparen
    instance.lparen = original
    assert instance.lparen == original

@given(instance=myDsl_Statement_strategy)
@settings(max_examples=50)
def test_mydsl_statement_instantiation(instance):
    assert isinstance(instance, myDsl_Statement)



@given(instance=myDsl_Statement_strategy)
def test_mydsl_statement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=myDsl_Statement_strategy)
def test_mydsl_statement_g_setter(instance):
    original = instance.g
    instance.g = original
    assert instance.g == original



@given(instance=myDsl_Statement_strategy)
def test_mydsl_statement_nameStatement_setter(instance):
    original = instance.nameStatement
    instance.nameStatement = original
    assert instance.nameStatement == original



@given(instance=myDsl_Statement_strategy)
def test_mydsl_statement_ret_setter(instance):
    original = instance.ret
    instance.ret = original
    assert instance.ret == original



@given(instance=myDsl_Statement_strategy)
def test_mydsl_statement_rparent_setter(instance):
    original = instance.rparent
    instance.rparent = original
    assert instance.rparent == original

@given(instance=myDsl_Type_specifier_strategy)
@settings(max_examples=50)
def test_mydsl_type_specifier_instantiation(instance):
    assert isinstance(instance, myDsl_Type_specifier)



@given(instance=myDsl_Type_specifier_strategy)
def test_mydsl_type_specifier_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original



@given(instance=myDsl_Type_specifier_strategy)
def test_mydsl_type_specifier_primitiveType_setter(instance):
    original = instance.primitiveType
    instance.primitiveType = original
    assert instance.primitiveType == original

@given(instance=myDsl_Expression_strategy)
@settings(max_examples=50)
def test_mydsl_expression_instantiation(instance):
    assert isinstance(instance, myDsl_Expression)



@given(instance=myDsl_Expression_strategy)
def test_mydsl_expression_this_setter(instance):
    original = instance.this
    instance.this = original
    assert instance.this == original



@given(instance=myDsl_Expression_strategy)
def test_mydsl_expression_super_setter(instance):
    original = instance.super
    instance.super = original
    assert instance.super == original



@given(instance=myDsl_Expression_strategy)
def test_mydsl_expression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=myDsl_Expression_strategy)
def test_mydsl_expression_null_setter(instance):
    original = instance.null
    instance.null = original
    assert instance.null == original

@given(instance=myDsl_Array_initializer_strategy)
@settings(max_examples=50)
def test_mydsl_array_initializer_instantiation(instance):
    assert isinstance(instance, myDsl_Array_initializer)

@given(instance=myDsl_Variable_initializer_strategy)
@settings(max_examples=50)
def test_mydsl_variable_initializer_instantiation(instance):
    assert isinstance(instance, myDsl_Variable_initializer)

@given(instance=myDsl_Variable_declarator_strategy)
@settings(max_examples=50)
def test_mydsl_variable_declarator_instantiation(instance):
    assert isinstance(instance, myDsl_Variable_declarator)



@given(instance=myDsl_Variable_declarator_strategy)
def test_mydsl_variable_declarator_nameVariable_setter(instance):
    original = instance.nameVariable
    instance.nameVariable = original
    assert instance.nameVariable == original



@given(instance=myDsl_Variable_declarator_strategy)
def test_mydsl_variable_declarator_lenVector_setter(instance):
    original = instance.lenVector
    instance.lenVector = original
    assert instance.lenVector == original

@given(instance=myDsl_Parameter_strategy)
@settings(max_examples=50)
def test_mydsl_parameter_instantiation(instance):
    assert isinstance(instance, myDsl_Parameter)



@given(instance=myDsl_Parameter_strategy)
def test_mydsl_parameter_parameterName_setter(instance):
    original = instance.parameterName
    instance.parameterName = original
    assert instance.parameterName == original

@given(instance=myDsl_Package_statement_strategy)
@settings(max_examples=50)
def test_mydsl_package_statement_instantiation(instance):
    assert isinstance(instance, myDsl_Package_statement)



@given(instance=myDsl_Package_statement_strategy)
def test_mydsl_package_statement_pacName_setter(instance):
    original = instance.pacName
    instance.pacName = original
    assert instance.pacName == original

@given(instance=myDsl_Statement_block_strategy)
@settings(max_examples=50)
def test_mydsl_statement_block_instantiation(instance):
    assert isinstance(instance, myDsl_Statement_block)



@given(instance=myDsl_Statement_block_strategy)
def test_mydsl_statement_block_rCurly_setter(instance):
    original = instance.rCurly
    instance.rCurly = original
    assert instance.rCurly == original



@given(instance=myDsl_Statement_block_strategy)
def test_mydsl_statement_block_lCurly_setter(instance):
    original = instance.lCurly
    instance.lCurly = original
    assert instance.lCurly == original

@given(instance=myDsl_Parameter_list_strategy)
@settings(max_examples=50)
def test_mydsl_parameter_list_instantiation(instance):
    assert isinstance(instance, myDsl_Parameter_list)

@given(instance=myDsl_Type_strategy)
@settings(max_examples=50)
def test_mydsl_type_instantiation(instance):
    assert isinstance(instance, myDsl_Type)



@given(instance=myDsl_Type_strategy)
def test_mydsl_type_typeVector_setter(instance):
    original = instance.typeVector
    instance.typeVector = original
    assert instance.typeVector == original

@given(instance=myDsl_Static_initializer_strategy)
@settings(max_examples=50)
def test_mydsl_static_initializer_instantiation(instance):
    assert isinstance(instance, myDsl_Static_initializer)



@given(instance=myDsl_Static_initializer_strategy)
def test_mydsl_static_initializer_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=myDsl_Method_declaration_strategy)
@settings(max_examples=50)
def test_mydsl_method_declaration_instantiation(instance):
    assert isinstance(instance, myDsl_Method_declaration)



@given(instance=myDsl_Method_declaration_strategy)
def test_mydsl_method_declaration_nameMethod_setter(instance):
    original = instance.nameMethod
    instance.nameMethod = original
    assert instance.nameMethod == original



@given(instance=myDsl_Method_declaration_strategy)
def test_mydsl_method_declaration_rparent_setter(instance):
    original = instance.rparent
    instance.rparent = original
    assert instance.rparent == original



@given(instance=myDsl_Method_declaration_strategy)
def test_mydsl_method_declaration_debug_setter(instance):
    original = instance.debug
    instance.debug = original
    assert instance.debug == original



@given(instance=myDsl_Method_declaration_strategy)
def test_mydsl_method_declaration_modifiersMethod_setter(instance):
    original = instance.modifiersMethod
    instance.modifiersMethod = original
    assert instance.modifiersMethod == original



@given(instance=myDsl_Method_declaration_strategy)
def test_mydsl_method_declaration_lParen_setter(instance):
    original = instance.lParen
    instance.lParen = original
    assert instance.lParen == original

@given(instance=myDsl_Constructor_declaration_strategy)
@settings(max_examples=50)
def test_mydsl_constructor_declaration_instantiation(instance):
    assert isinstance(instance, myDsl_Constructor_declaration)



@given(instance=myDsl_Constructor_declaration_strategy)
def test_mydsl_constructor_declaration_rparent_setter(instance):
    original = instance.rparent
    instance.rparent = original
    assert instance.rparent == original



@given(instance=myDsl_Constructor_declaration_strategy)
def test_mydsl_constructor_declaration_lParen_setter(instance):
    original = instance.lParen
    instance.lParen = original
    assert instance.lParen == original



@given(instance=myDsl_Constructor_declaration_strategy)
def test_mydsl_constructor_declaration_modifiersConstructor_setter(instance):
    original = instance.modifiersConstructor
    instance.modifiersConstructor = original
    assert instance.modifiersConstructor == original



@given(instance=myDsl_Constructor_declaration_strategy)
def test_mydsl_constructor_declaration_nameConstructor_setter(instance):
    original = instance.nameConstructor
    instance.nameConstructor = original
    assert instance.nameConstructor == original

@given(instance=myDsl_Variable_declaration_strategy)
@settings(max_examples=50)
def test_mydsl_variable_declaration_instantiation(instance):
    assert isinstance(instance, myDsl_Variable_declaration)



@given(instance=myDsl_Variable_declaration_strategy)
def test_mydsl_variable_declaration_modifiersVariable_setter(instance):
    original = instance.modifiersVariable
    instance.modifiersVariable = original
    assert instance.modifiersVariable == original

@given(instance=myDsl_Field_declaration_strategy)
@settings(max_examples=50)
def test_mydsl_field_declaration_instantiation(instance):
    assert isinstance(instance, myDsl_Field_declaration)



@given(instance=myDsl_Field_declaration_strategy)
def test_mydsl_field_declaration_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=myDsl_Interface_declaration_strategy)
@settings(max_examples=50)
def test_mydsl_interface_declaration_instantiation(instance):
    assert isinstance(instance, myDsl_Interface_declaration)



@given(instance=myDsl_Interface_declaration_strategy)
def test_mydsl_interface_declaration_interfaceHerdada_setter(instance):
    original = instance.interfaceHerdada
    instance.interfaceHerdada = original
    assert instance.interfaceHerdada == original



@given(instance=myDsl_Interface_declaration_strategy)
def test_mydsl_interface_declaration_interfacesHerdadas_setter(instance):
    original = instance.interfacesHerdadas
    instance.interfacesHerdadas = original
    assert instance.interfacesHerdadas == original



@given(instance=myDsl_Interface_declaration_strategy)
def test_mydsl_interface_declaration_modifiers_setter(instance):
    original = instance.modifiers
    instance.modifiers = original
    assert instance.modifiers == original



@given(instance=myDsl_Interface_declaration_strategy)
def test_mydsl_interface_declaration_interfaceName_setter(instance):
    original = instance.interfaceName
    instance.interfaceName = original
    assert instance.interfaceName == original

@given(instance=myDsl_Class_declaration_strategy)
@settings(max_examples=50)
def test_mydsl_class_declaration_instantiation(instance):
    assert isinstance(instance, myDsl_Class_declaration)



@given(instance=myDsl_Class_declaration_strategy)
def test_mydsl_class_declaration_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original



@given(instance=myDsl_Class_declaration_strategy)
def test_mydsl_class_declaration_classHerdada_setter(instance):
    original = instance.classHerdada
    instance.classHerdada = original
    assert instance.classHerdada == original



@given(instance=myDsl_Class_declaration_strategy)
def test_mydsl_class_declaration_modifiers_setter(instance):
    original = instance.modifiers
    instance.modifiers = original
    assert instance.modifiers == original



@given(instance=myDsl_Class_declaration_strategy)
def test_mydsl_class_declaration_interfaceImplementada_setter(instance):
    original = instance.interfaceImplementada
    instance.interfaceImplementada = original
    assert instance.interfaceImplementada == original



@given(instance=myDsl_Class_declaration_strategy)
def test_mydsl_class_declaration_interfacesImplementadas_setter(instance):
    original = instance.interfacesImplementadas
    instance.interfacesImplementadas = original
    assert instance.interfacesImplementadas == original

@given(instance=myDsl_Type_declaration_strategy)
@settings(max_examples=50)
def test_mydsl_type_declaration_instantiation(instance):
    assert isinstance(instance, myDsl_Type_declaration)



@given(instance=myDsl_Type_declaration_strategy)
def test_mydsl_type_declaration_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=myDsl_Import_statement_strategy)
@settings(max_examples=50)
def test_mydsl_import_statement_instantiation(instance):
    assert isinstance(instance, myDsl_Import_statement)



@given(instance=myDsl_Import_statement_strategy)
def test_mydsl_import_statement_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original



@given(instance=myDsl_Import_statement_strategy)
def test_mydsl_import_statement_pacName_setter(instance):
    original = instance.pacName
    instance.pacName = original
    assert instance.pacName == original

@given(instance=myDsl_Compilation_unit_strategy)
@settings(max_examples=50)
def test_mydsl_compilation_unit_instantiation(instance):
    assert isinstance(instance, myDsl_Compilation_unit)

@given(instance=myDsl_Model_strategy)
@settings(max_examples=50)
def test_mydsl_model_instantiation(instance):
    assert isinstance(instance, myDsl_Model)
