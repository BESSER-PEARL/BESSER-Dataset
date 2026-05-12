import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    java_Return_value,
    java_Try_statement,
    java_Switch_Statement,
    java_For_Statement,
    java_While_Statement,
    java_Do_Statement,
    java_If_Statement,
    java_Return_Statement,
    java_Statement,
    Statement,
    java_Static_initializer,
    java_Arg_List,
    java_Float_Literal,
    java_Ampersand_Rule,
    java_Variable_declaration,
    java_Parameter,
    java_Creating_Expression,
    java_Cast_Expression,
    java_Bit_Expression_NR,
    java_Logical_Expression_NR,
    java_Expression_aux,
    java_Numeric_Expression_NR,
    java_Expression,
    java_Variable_initializer,
    java_Variable_declarator,
    java_Class_declaration,
    java_Field_declaration,
    java_Constructor_declaration,
    java_Parameter_list_method_call,
    Return_value,
    java_Literal_Expression,
    java_Method_call,
    java_Statement_block,
    java_Parameter_list,
    java_Type,
    java_Method_declaration,
    java_Interface_declaration,
    java_EObject,
    java_Type_declaration,
    java_Import_statement,
    java_Package_statement,
    java_Compilation_unit,
    java_Head,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_java_return_value_is_not_abstract():
    assert not inspect.isabstract(java_Return_value)


def test_java_return_value_constructor_exists():
    assert callable(java_Return_value.__init__)


def test_java_return_value_constructor_args():
    sig = inspect.signature(java_Return_value.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java_return_value_has_name():
    assert hasattr(java_Return_value, "name")
    descriptor = None
    for klass in java_Return_value.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java_try_statement_is_not_abstract():
    assert not inspect.isabstract(java_Try_statement)


def test_java_try_statement_constructor_exists():
    assert callable(java_Try_statement.__init__)


def test_java_try_statement_constructor_args():
    sig = inspect.signature(java_Try_statement.__init__)
    params = list(sig.parameters.keys())
    assert "try_" in params, "Missing parameter 'try_'"
    assert "catchs" in params, "Missing parameter 'catchs'"
    assert "finally_" in params, "Missing parameter 'finally_'"

def test_java_try_statement_has_try_():
    assert hasattr(java_Try_statement, "try_")
    descriptor = None
    for klass in java_Try_statement.__mro__:
        if "try_" in klass.__dict__:
            descriptor = klass.__dict__["try_"]
            break
    assert isinstance(descriptor, property)

def test_java_try_statement_has_catchs():
    assert hasattr(java_Try_statement, "catchs")
    descriptor = None
    for klass in java_Try_statement.__mro__:
        if "catchs" in klass.__dict__:
            descriptor = klass.__dict__["catchs"]
            break
    assert isinstance(descriptor, property)

def test_java_try_statement_has_finally_():
    assert hasattr(java_Try_statement, "finally_")
    descriptor = None
    for klass in java_Try_statement.__mro__:
        if "finally_" in klass.__dict__:
            descriptor = klass.__dict__["finally_"]
            break
    assert isinstance(descriptor, property)



def test_java_switch_statement_is_not_abstract():
    assert not inspect.isabstract(java_Switch_Statement)


def test_java_switch_statement_constructor_exists():
    assert callable(java_Switch_Statement.__init__)


def test_java_switch_statement_constructor_args():
    sig = inspect.signature(java_Switch_Statement.__init__)
    params = list(sig.parameters.keys())



def test_java_for_statement_is_not_abstract():
    assert not inspect.isabstract(java_For_Statement)


def test_java_for_statement_constructor_exists():
    assert callable(java_For_Statement.__init__)


def test_java_for_statement_constructor_args():
    sig = inspect.signature(java_For_Statement.__init__)
    params = list(sig.parameters.keys())
    assert "pv" in params, "Missing parameter 'pv'"

def test_java_for_statement_has_pv():
    assert hasattr(java_For_Statement, "pv")
    descriptor = None
    for klass in java_For_Statement.__mro__:
        if "pv" in klass.__dict__:
            descriptor = klass.__dict__["pv"]
            break
    assert isinstance(descriptor, property)



def test_java_while_statement_is_not_abstract():
    assert not inspect.isabstract(java_While_Statement)


def test_java_while_statement_constructor_exists():
    assert callable(java_While_Statement.__init__)


def test_java_while_statement_constructor_args():
    sig = inspect.signature(java_While_Statement.__init__)
    params = list(sig.parameters.keys())



def test_java_do_statement_is_not_abstract():
    assert not inspect.isabstract(java_Do_Statement)


def test_java_do_statement_constructor_exists():
    assert callable(java_Do_Statement.__init__)


def test_java_do_statement_constructor_args():
    sig = inspect.signature(java_Do_Statement.__init__)
    params = list(sig.parameters.keys())



def test_java_if_statement_is_not_abstract():
    assert not inspect.isabstract(java_If_Statement)


def test_java_if_statement_constructor_exists():
    assert callable(java_If_Statement.__init__)


def test_java_if_statement_constructor_args():
    sig = inspect.signature(java_If_Statement.__init__)
    params = list(sig.parameters.keys())



def test_java_return_statement_is_not_abstract():
    assert not inspect.isabstract(java_Return_Statement)


def test_java_return_statement_constructor_exists():
    assert callable(java_Return_Statement.__init__)


def test_java_return_statement_constructor_args():
    sig = inspect.signature(java_Return_Statement.__init__)
    params = list(sig.parameters.keys())



def test_java_statement_is_not_abstract():
    assert not inspect.isabstract(java_Statement)


def test_java_statement_constructor_exists():
    assert callable(java_Statement.__init__)


def test_java_statement_constructor_args():
    sig = inspect.signature(java_Statement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java_statement_has_name():
    assert hasattr(java_Statement, "name")
    descriptor = None
    for klass in java_Statement.__mro__:
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



def test_java_static_initializer_is_not_abstract():
    assert not inspect.isabstract(java_Static_initializer)


def test_java_static_initializer_constructor_exists():
    assert callable(java_Static_initializer.__init__)


def test_java_static_initializer_constructor_args():
    sig = inspect.signature(java_Static_initializer.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_java_static_initializer_has_static():
    assert hasattr(java_Static_initializer, "static")
    descriptor = None
    for klass in java_Static_initializer.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_java_arg_list_is_not_abstract():
    assert not inspect.isabstract(java_Arg_List)


def test_java_arg_list_constructor_exists():
    assert callable(java_Arg_List.__init__)


def test_java_arg_list_constructor_args():
    sig = inspect.signature(java_Arg_List.__init__)
    params = list(sig.parameters.keys())



def test_java_float_literal_is_not_abstract():
    assert not inspect.isabstract(java_Float_Literal)


def test_java_float_literal_constructor_exists():
    assert callable(java_Float_Literal.__init__)


def test_java_float_literal_constructor_args():
    sig = inspect.signature(java_Float_Literal.__init__)
    params = list(sig.parameters.keys())
    assert "decimalDigits2" in params, "Missing parameter 'decimalDigits2'"
    assert "exp" in params, "Missing parameter 'exp'"
    assert "decimalDigits1" in params, "Missing parameter 'decimalDigits1'"
    assert "floatTypeSufix" in params, "Missing parameter 'floatTypeSufix'"

def test_java_float_literal_has_decimalDigits2():
    assert hasattr(java_Float_Literal, "decimalDigits2")
    descriptor = None
    for klass in java_Float_Literal.__mro__:
        if "decimalDigits2" in klass.__dict__:
            descriptor = klass.__dict__["decimalDigits2"]
            break
    assert isinstance(descriptor, property)

def test_java_float_literal_has_exp():
    assert hasattr(java_Float_Literal, "exp")
    descriptor = None
    for klass in java_Float_Literal.__mro__:
        if "exp" in klass.__dict__:
            descriptor = klass.__dict__["exp"]
            break
    assert isinstance(descriptor, property)

def test_java_float_literal_has_decimalDigits1():
    assert hasattr(java_Float_Literal, "decimalDigits1")
    descriptor = None
    for klass in java_Float_Literal.__mro__:
        if "decimalDigits1" in klass.__dict__:
            descriptor = klass.__dict__["decimalDigits1"]
            break
    assert isinstance(descriptor, property)

def test_java_float_literal_has_floatTypeSufix():
    assert hasattr(java_Float_Literal, "floatTypeSufix")
    descriptor = None
    for klass in java_Float_Literal.__mro__:
        if "floatTypeSufix" in klass.__dict__:
            descriptor = klass.__dict__["floatTypeSufix"]
            break
    assert isinstance(descriptor, property)



def test_java_ampersand_rule_is_not_abstract():
    assert not inspect.isabstract(java_Ampersand_Rule)


def test_java_ampersand_rule_constructor_exists():
    assert callable(java_Ampersand_Rule.__init__)


def test_java_ampersand_rule_constructor_args():
    sig = inspect.signature(java_Ampersand_Rule.__init__)
    params = list(sig.parameters.keys())
    assert "a2" in params, "Missing parameter 'a2'"
    assert "a1" in params, "Missing parameter 'a1'"

def test_java_ampersand_rule_has_a2():
    assert hasattr(java_Ampersand_Rule, "a2")
    descriptor = None
    for klass in java_Ampersand_Rule.__mro__:
        if "a2" in klass.__dict__:
            descriptor = klass.__dict__["a2"]
            break
    assert isinstance(descriptor, property)

def test_java_ampersand_rule_has_a1():
    assert hasattr(java_Ampersand_Rule, "a1")
    descriptor = None
    for klass in java_Ampersand_Rule.__mro__:
        if "a1" in klass.__dict__:
            descriptor = klass.__dict__["a1"]
            break
    assert isinstance(descriptor, property)



def test_java_variable_declaration_is_not_abstract():
    assert not inspect.isabstract(java_Variable_declaration)


def test_java_variable_declaration_constructor_exists():
    assert callable(java_Variable_declaration.__init__)


def test_java_variable_declaration_constructor_args():
    sig = inspect.signature(java_Variable_declaration.__init__)
    params = list(sig.parameters.keys())
    assert "modifiers" in params, "Missing parameter 'modifiers'"

def test_java_variable_declaration_has_modifiers():
    assert hasattr(java_Variable_declaration, "modifiers")
    descriptor = None
    for klass in java_Variable_declaration.__mro__:
        if "modifiers" in klass.__dict__:
            descriptor = klass.__dict__["modifiers"]
            break
    assert isinstance(descriptor, property)



def test_java_parameter_is_not_abstract():
    assert not inspect.isabstract(java_Parameter)


def test_java_parameter_constructor_exists():
    assert callable(java_Parameter.__init__)


def test_java_parameter_constructor_args():
    sig = inspect.signature(java_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java_parameter_has_name():
    assert hasattr(java_Parameter, "name")
    descriptor = None
    for klass in java_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java_creating_expression_is_not_abstract():
    assert not inspect.isabstract(java_Creating_Expression)


def test_java_creating_expression_constructor_exists():
    assert callable(java_Creating_Expression.__init__)


def test_java_creating_expression_constructor_args():
    sig = inspect.signature(java_Creating_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "typeSpecifier" in params, "Missing parameter 'typeSpecifier'"
    assert "className" in params, "Missing parameter 'className'"

def test_java_creating_expression_has_typeSpecifier():
    assert hasattr(java_Creating_Expression, "typeSpecifier")
    descriptor = None
    for klass in java_Creating_Expression.__mro__:
        if "typeSpecifier" in klass.__dict__:
            descriptor = klass.__dict__["typeSpecifier"]
            break
    assert isinstance(descriptor, property)

def test_java_creating_expression_has_className():
    assert hasattr(java_Creating_Expression, "className")
    descriptor = None
    for klass in java_Creating_Expression.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)



def test_java_cast_expression_is_not_abstract():
    assert not inspect.isabstract(java_Cast_Expression)


def test_java_cast_expression_constructor_exists():
    assert callable(java_Cast_Expression.__init__)


def test_java_cast_expression_constructor_args():
    sig = inspect.signature(java_Cast_Expression.__init__)
    params = list(sig.parameters.keys())



def test_java_bit_expression_nr_is_not_abstract():
    assert not inspect.isabstract(java_Bit_Expression_NR)


def test_java_bit_expression_nr_constructor_exists():
    assert callable(java_Bit_Expression_NR.__init__)


def test_java_bit_expression_nr_constructor_args():
    sig = inspect.signature(java_Bit_Expression_NR.__init__)
    params = list(sig.parameters.keys())



def test_java_logical_expression_nr_is_not_abstract():
    assert not inspect.isabstract(java_Logical_Expression_NR)


def test_java_logical_expression_nr_constructor_exists():
    assert callable(java_Logical_Expression_NR.__init__)


def test_java_logical_expression_nr_constructor_args():
    sig = inspect.signature(java_Logical_Expression_NR.__init__)
    params = list(sig.parameters.keys())
    assert "true" in params, "Missing parameter 'true'"
    assert "false" in params, "Missing parameter 'false'"

def test_java_logical_expression_nr_has_true():
    assert hasattr(java_Logical_Expression_NR, "true")
    descriptor = None
    for klass in java_Logical_Expression_NR.__mro__:
        if "true" in klass.__dict__:
            descriptor = klass.__dict__["true"]
            break
    assert isinstance(descriptor, property)

def test_java_logical_expression_nr_has_false():
    assert hasattr(java_Logical_Expression_NR, "false")
    descriptor = None
    for klass in java_Logical_Expression_NR.__mro__:
        if "false" in klass.__dict__:
            descriptor = klass.__dict__["false"]
            break
    assert isinstance(descriptor, property)



def test_java_expression_aux_is_not_abstract():
    assert not inspect.isabstract(java_Expression_aux)


def test_java_expression_aux_constructor_exists():
    assert callable(java_Expression_aux.__init__)


def test_java_expression_aux_constructor_args():
    sig = inspect.signature(java_Expression_aux.__init__)
    params = list(sig.parameters.keys())
    assert "testingSign" in params, "Missing parameter 'testingSign'"
    assert "stringSign" in params, "Missing parameter 'stringSign'"
    assert "numericSign" in params, "Missing parameter 'numericSign'"
    assert "bitSign" in params, "Missing parameter 'bitSign'"
    assert "sgin" in params, "Missing parameter 'sgin'"
    assert "name" in params, "Missing parameter 'name'"
    assert "logicalSign" in params, "Missing parameter 'logicalSign'"

def test_java_expression_aux_has_testingSign():
    assert hasattr(java_Expression_aux, "testingSign")
    descriptor = None
    for klass in java_Expression_aux.__mro__:
        if "testingSign" in klass.__dict__:
            descriptor = klass.__dict__["testingSign"]
            break
    assert isinstance(descriptor, property)

def test_java_expression_aux_has_stringSign():
    assert hasattr(java_Expression_aux, "stringSign")
    descriptor = None
    for klass in java_Expression_aux.__mro__:
        if "stringSign" in klass.__dict__:
            descriptor = klass.__dict__["stringSign"]
            break
    assert isinstance(descriptor, property)

def test_java_expression_aux_has_numericSign():
    assert hasattr(java_Expression_aux, "numericSign")
    descriptor = None
    for klass in java_Expression_aux.__mro__:
        if "numericSign" in klass.__dict__:
            descriptor = klass.__dict__["numericSign"]
            break
    assert isinstance(descriptor, property)

def test_java_expression_aux_has_bitSign():
    assert hasattr(java_Expression_aux, "bitSign")
    descriptor = None
    for klass in java_Expression_aux.__mro__:
        if "bitSign" in klass.__dict__:
            descriptor = klass.__dict__["bitSign"]
            break
    assert isinstance(descriptor, property)

def test_java_expression_aux_has_sgin():
    assert hasattr(java_Expression_aux, "sgin")
    descriptor = None
    for klass in java_Expression_aux.__mro__:
        if "sgin" in klass.__dict__:
            descriptor = klass.__dict__["sgin"]
            break
    assert isinstance(descriptor, property)

def test_java_expression_aux_has_name():
    assert hasattr(java_Expression_aux, "name")
    descriptor = None
    for klass in java_Expression_aux.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_java_expression_aux_has_logicalSign():
    assert hasattr(java_Expression_aux, "logicalSign")
    descriptor = None
    for klass in java_Expression_aux.__mro__:
        if "logicalSign" in klass.__dict__:
            descriptor = klass.__dict__["logicalSign"]
            break
    assert isinstance(descriptor, property)



def test_java_numeric_expression_nr_is_not_abstract():
    assert not inspect.isabstract(java_Numeric_Expression_NR)


def test_java_numeric_expression_nr_constructor_exists():
    assert callable(java_Numeric_Expression_NR.__init__)


def test_java_numeric_expression_nr_constructor_args():
    sig = inspect.signature(java_Numeric_Expression_NR.__init__)
    params = list(sig.parameters.keys())
    assert "sinal_numeric" in params, "Missing parameter 'sinal_numeric'"

def test_java_numeric_expression_nr_has_sinal_numeric():
    assert hasattr(java_Numeric_Expression_NR, "sinal_numeric")
    descriptor = None
    for klass in java_Numeric_Expression_NR.__mro__:
        if "sinal_numeric" in klass.__dict__:
            descriptor = klass.__dict__["sinal_numeric"]
            break
    assert isinstance(descriptor, property)



def test_java_expression_is_not_abstract():
    assert not inspect.isabstract(java_Expression)


def test_java_expression_constructor_exists():
    assert callable(java_Expression.__init__)


def test_java_expression_constructor_args():
    sig = inspect.signature(java_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "null" in params, "Missing parameter 'null'"
    assert "name" in params, "Missing parameter 'name'"
    assert "super" in params, "Missing parameter 'super'"
    assert "this" in params, "Missing parameter 'this'"

def test_java_expression_has_null():
    assert hasattr(java_Expression, "null")
    descriptor = None
    for klass in java_Expression.__mro__:
        if "null" in klass.__dict__:
            descriptor = klass.__dict__["null"]
            break
    assert isinstance(descriptor, property)

def test_java_expression_has_name():
    assert hasattr(java_Expression, "name")
    descriptor = None
    for klass in java_Expression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_java_expression_has_super():
    assert hasattr(java_Expression, "super")
    descriptor = None
    for klass in java_Expression.__mro__:
        if "super" in klass.__dict__:
            descriptor = klass.__dict__["super"]
            break
    assert isinstance(descriptor, property)

def test_java_expression_has_this():
    assert hasattr(java_Expression, "this")
    descriptor = None
    for klass in java_Expression.__mro__:
        if "this" in klass.__dict__:
            descriptor = klass.__dict__["this"]
            break
    assert isinstance(descriptor, property)



def test_java_variable_initializer_is_not_abstract():
    assert not inspect.isabstract(java_Variable_initializer)


def test_java_variable_initializer_constructor_exists():
    assert callable(java_Variable_initializer.__init__)


def test_java_variable_initializer_constructor_args():
    sig = inspect.signature(java_Variable_initializer.__init__)
    params = list(sig.parameters.keys())



def test_java_variable_declarator_is_not_abstract():
    assert not inspect.isabstract(java_Variable_declarator)


def test_java_variable_declarator_constructor_exists():
    assert callable(java_Variable_declarator.__init__)


def test_java_variable_declarator_constructor_args():
    sig = inspect.signature(java_Variable_declarator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java_variable_declarator_has_name():
    assert hasattr(java_Variable_declarator, "name")
    descriptor = None
    for klass in java_Variable_declarator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java_class_declaration_is_not_abstract():
    assert not inspect.isabstract(java_Class_declaration)


def test_java_class_declaration_constructor_exists():
    assert callable(java_Class_declaration.__init__)


def test_java_class_declaration_constructor_args():
    sig = inspect.signature(java_Class_declaration.__init__)
    params = list(sig.parameters.keys())
    assert "implements" in params, "Missing parameter 'implements'"
    assert "modifiers" in params, "Missing parameter 'modifiers'"
    assert "className" in params, "Missing parameter 'className'"
    assert "extend" in params, "Missing parameter 'extend'"
    assert "implement" in params, "Missing parameter 'implement'"

def test_java_class_declaration_has_implements():
    assert hasattr(java_Class_declaration, "implements")
    descriptor = None
    for klass in java_Class_declaration.__mro__:
        if "implements" in klass.__dict__:
            descriptor = klass.__dict__["implements"]
            break
    assert isinstance(descriptor, property)

def test_java_class_declaration_has_modifiers():
    assert hasattr(java_Class_declaration, "modifiers")
    descriptor = None
    for klass in java_Class_declaration.__mro__:
        if "modifiers" in klass.__dict__:
            descriptor = klass.__dict__["modifiers"]
            break
    assert isinstance(descriptor, property)

def test_java_class_declaration_has_className():
    assert hasattr(java_Class_declaration, "className")
    descriptor = None
    for klass in java_Class_declaration.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)

def test_java_class_declaration_has_extend():
    assert hasattr(java_Class_declaration, "extend")
    descriptor = None
    for klass in java_Class_declaration.__mro__:
        if "extend" in klass.__dict__:
            descriptor = klass.__dict__["extend"]
            break
    assert isinstance(descriptor, property)

def test_java_class_declaration_has_implement():
    assert hasattr(java_Class_declaration, "implement")
    descriptor = None
    for klass in java_Class_declaration.__mro__:
        if "implement" in klass.__dict__:
            descriptor = klass.__dict__["implement"]
            break
    assert isinstance(descriptor, property)



def test_java_field_declaration_is_not_abstract():
    assert not inspect.isabstract(java_Field_declaration)


def test_java_field_declaration_constructor_exists():
    assert callable(java_Field_declaration.__init__)


def test_java_field_declaration_constructor_args():
    sig = inspect.signature(java_Field_declaration.__init__)
    params = list(sig.parameters.keys())
    assert "doc" in params, "Missing parameter 'doc'"
    assert "debug" in params, "Missing parameter 'debug'"

def test_java_field_declaration_has_doc():
    assert hasattr(java_Field_declaration, "doc")
    descriptor = None
    for klass in java_Field_declaration.__mro__:
        if "doc" in klass.__dict__:
            descriptor = klass.__dict__["doc"]
            break
    assert isinstance(descriptor, property)

def test_java_field_declaration_has_debug():
    assert hasattr(java_Field_declaration, "debug")
    descriptor = None
    for klass in java_Field_declaration.__mro__:
        if "debug" in klass.__dict__:
            descriptor = klass.__dict__["debug"]
            break
    assert isinstance(descriptor, property)



def test_java_constructor_declaration_is_not_abstract():
    assert not inspect.isabstract(java_Constructor_declaration)


def test_java_constructor_declaration_constructor_exists():
    assert callable(java_Constructor_declaration.__init__)


def test_java_constructor_declaration_constructor_args():
    sig = inspect.signature(java_Constructor_declaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "modifiers" in params, "Missing parameter 'modifiers'"

def test_java_constructor_declaration_has_name():
    assert hasattr(java_Constructor_declaration, "name")
    descriptor = None
    for klass in java_Constructor_declaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_java_constructor_declaration_has_modifiers():
    assert hasattr(java_Constructor_declaration, "modifiers")
    descriptor = None
    for klass in java_Constructor_declaration.__mro__:
        if "modifiers" in klass.__dict__:
            descriptor = klass.__dict__["modifiers"]
            break
    assert isinstance(descriptor, property)



def test_java_parameter_list_method_call_is_not_abstract():
    assert not inspect.isabstract(java_Parameter_list_method_call)


def test_java_parameter_list_method_call_constructor_exists():
    assert callable(java_Parameter_list_method_call.__init__)


def test_java_parameter_list_method_call_constructor_args():
    sig = inspect.signature(java_Parameter_list_method_call.__init__)
    params = list(sig.parameters.keys())
    assert "parameters" in params, "Missing parameter 'parameters'"
    assert "name" in params, "Missing parameter 'name'"

def test_java_parameter_list_method_call_has_parameters():
    assert hasattr(java_Parameter_list_method_call, "parameters")
    descriptor = None
    for klass in java_Parameter_list_method_call.__mro__:
        if "parameters" in klass.__dict__:
            descriptor = klass.__dict__["parameters"]
            break
    assert isinstance(descriptor, property)

def test_java_parameter_list_method_call_has_name():
    assert hasattr(java_Parameter_list_method_call, "name")
    descriptor = None
    for klass in java_Parameter_list_method_call.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_return_value_is_not_abstract():
    assert not inspect.isabstract(Return_value)


def test_return_value_constructor_exists():
    assert callable(Return_value.__init__)


def test_return_value_constructor_args():
    sig = inspect.signature(Return_value.__init__)
    params = list(sig.parameters.keys())



def test_java_literal_expression_is_not_abstract():
    assert not inspect.isabstract(java_Literal_Expression)


def test_java_literal_expression_constructor_exists():
    assert callable(java_Literal_Expression.__init__)


def test_java_literal_expression_constructor_args():
    sig = inspect.signature(java_Literal_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"
    assert "exp" in params, "Missing parameter 'exp'"
    assert "exp1" in params, "Missing parameter 'exp1'"
    assert "char" in params, "Missing parameter 'char'"

def test_java_literal_expression_has_string():
    assert hasattr(java_Literal_Expression, "string")
    descriptor = None
    for klass in java_Literal_Expression.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)

def test_java_literal_expression_has_exp():
    assert hasattr(java_Literal_Expression, "exp")
    descriptor = None
    for klass in java_Literal_Expression.__mro__:
        if "exp" in klass.__dict__:
            descriptor = klass.__dict__["exp"]
            break
    assert isinstance(descriptor, property)

def test_java_literal_expression_has_exp1():
    assert hasattr(java_Literal_Expression, "exp1")
    descriptor = None
    for klass in java_Literal_Expression.__mro__:
        if "exp1" in klass.__dict__:
            descriptor = klass.__dict__["exp1"]
            break
    assert isinstance(descriptor, property)

def test_java_literal_expression_has_char():
    assert hasattr(java_Literal_Expression, "char")
    descriptor = None
    for klass in java_Literal_Expression.__mro__:
        if "char" in klass.__dict__:
            descriptor = klass.__dict__["char"]
            break
    assert isinstance(descriptor, property)



def test_java_method_call_is_not_abstract():
    assert not inspect.isabstract(java_Method_call)


def test_java_method_call_constructor_exists():
    assert callable(java_Method_call.__init__)


def test_java_method_call_constructor_args():
    sig = inspect.signature(java_Method_call.__init__)
    params = list(sig.parameters.keys())



def test_java_statement_block_is_not_abstract():
    assert not inspect.isabstract(java_Statement_block)


def test_java_statement_block_constructor_exists():
    assert callable(java_Statement_block.__init__)


def test_java_statement_block_constructor_args():
    sig = inspect.signature(java_Statement_block.__init__)
    params = list(sig.parameters.keys())



def test_java_parameter_list_is_not_abstract():
    assert not inspect.isabstract(java_Parameter_list)


def test_java_parameter_list_constructor_exists():
    assert callable(java_Parameter_list.__init__)


def test_java_parameter_list_constructor_args():
    sig = inspect.signature(java_Parameter_list.__init__)
    params = list(sig.parameters.keys())



def test_java_type_is_not_abstract():
    assert not inspect.isabstract(java_Type)


def test_java_type_constructor_exists():
    assert callable(java_Type.__init__)


def test_java_type_constructor_args():
    sig = inspect.signature(java_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java_type_has_name():
    assert hasattr(java_Type, "name")
    descriptor = None
    for klass in java_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java_method_declaration_is_not_abstract():
    assert not inspect.isabstract(java_Method_declaration)


def test_java_method_declaration_constructor_exists():
    assert callable(java_Method_declaration.__init__)


def test_java_method_declaration_constructor_args():
    sig = inspect.signature(java_Method_declaration.__init__)
    params = list(sig.parameters.keys())
    assert "debug" in params, "Missing parameter 'debug'"
    assert "name" in params, "Missing parameter 'name'"
    assert "modifiers" in params, "Missing parameter 'modifiers'"

def test_java_method_declaration_has_debug():
    assert hasattr(java_Method_declaration, "debug")
    descriptor = None
    for klass in java_Method_declaration.__mro__:
        if "debug" in klass.__dict__:
            descriptor = klass.__dict__["debug"]
            break
    assert isinstance(descriptor, property)

def test_java_method_declaration_has_name():
    assert hasattr(java_Method_declaration, "name")
    descriptor = None
    for klass in java_Method_declaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_java_method_declaration_has_modifiers():
    assert hasattr(java_Method_declaration, "modifiers")
    descriptor = None
    for klass in java_Method_declaration.__mro__:
        if "modifiers" in klass.__dict__:
            descriptor = klass.__dict__["modifiers"]
            break
    assert isinstance(descriptor, property)



def test_java_interface_declaration_is_not_abstract():
    assert not inspect.isabstract(java_Interface_declaration)


def test_java_interface_declaration_constructor_exists():
    assert callable(java_Interface_declaration.__init__)


def test_java_interface_declaration_constructor_args():
    sig = inspect.signature(java_Interface_declaration.__init__)
    params = list(sig.parameters.keys())
    assert "modifiers" in params, "Missing parameter 'modifiers'"
    assert "extends" in params, "Missing parameter 'extends'"
    assert "extend" in params, "Missing parameter 'extend'"
    assert "interfaceName" in params, "Missing parameter 'interfaceName'"

def test_java_interface_declaration_has_modifiers():
    assert hasattr(java_Interface_declaration, "modifiers")
    descriptor = None
    for klass in java_Interface_declaration.__mro__:
        if "modifiers" in klass.__dict__:
            descriptor = klass.__dict__["modifiers"]
            break
    assert isinstance(descriptor, property)

def test_java_interface_declaration_has_extends():
    assert hasattr(java_Interface_declaration, "extends")
    descriptor = None
    for klass in java_Interface_declaration.__mro__:
        if "extends" in klass.__dict__:
            descriptor = klass.__dict__["extends"]
            break
    assert isinstance(descriptor, property)

def test_java_interface_declaration_has_extend():
    assert hasattr(java_Interface_declaration, "extend")
    descriptor = None
    for klass in java_Interface_declaration.__mro__:
        if "extend" in klass.__dict__:
            descriptor = klass.__dict__["extend"]
            break
    assert isinstance(descriptor, property)

def test_java_interface_declaration_has_interfaceName():
    assert hasattr(java_Interface_declaration, "interfaceName")
    descriptor = None
    for klass in java_Interface_declaration.__mro__:
        if "interfaceName" in klass.__dict__:
            descriptor = klass.__dict__["interfaceName"]
            break
    assert isinstance(descriptor, property)



def test_java_eobject_is_not_abstract():
    assert not inspect.isabstract(java_EObject)


def test_java_eobject_constructor_exists():
    assert callable(java_EObject.__init__)


def test_java_eobject_constructor_args():
    sig = inspect.signature(java_EObject.__init__)
    params = list(sig.parameters.keys())



def test_java_type_declaration_is_not_abstract():
    assert not inspect.isabstract(java_Type_declaration)


def test_java_type_declaration_constructor_exists():
    assert callable(java_Type_declaration.__init__)


def test_java_type_declaration_constructor_args():
    sig = inspect.signature(java_Type_declaration.__init__)
    params = list(sig.parameters.keys())
    assert "doc" in params, "Missing parameter 'doc'"

def test_java_type_declaration_has_doc():
    assert hasattr(java_Type_declaration, "doc")
    descriptor = None
    for klass in java_Type_declaration.__mro__:
        if "doc" in klass.__dict__:
            descriptor = klass.__dict__["doc"]
            break
    assert isinstance(descriptor, property)



def test_java_import_statement_is_not_abstract():
    assert not inspect.isabstract(java_Import_statement)


def test_java_import_statement_constructor_exists():
    assert callable(java_Import_statement.__init__)


def test_java_import_statement_constructor_args():
    sig = inspect.signature(java_Import_statement.__init__)
    params = list(sig.parameters.keys())
    assert "packagename" in params, "Missing parameter 'packagename'"
    assert "classname" in params, "Missing parameter 'classname'"

def test_java_import_statement_has_packagename():
    assert hasattr(java_Import_statement, "packagename")
    descriptor = None
    for klass in java_Import_statement.__mro__:
        if "packagename" in klass.__dict__:
            descriptor = klass.__dict__["packagename"]
            break
    assert isinstance(descriptor, property)

def test_java_import_statement_has_classname():
    assert hasattr(java_Import_statement, "classname")
    descriptor = None
    for klass in java_Import_statement.__mro__:
        if "classname" in klass.__dict__:
            descriptor = klass.__dict__["classname"]
            break
    assert isinstance(descriptor, property)



def test_java_package_statement_is_not_abstract():
    assert not inspect.isabstract(java_Package_statement)


def test_java_package_statement_constructor_exists():
    assert callable(java_Package_statement.__init__)


def test_java_package_statement_constructor_args():
    sig = inspect.signature(java_Package_statement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java_package_statement_has_name():
    assert hasattr(java_Package_statement, "name")
    descriptor = None
    for klass in java_Package_statement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java_compilation_unit_is_not_abstract():
    assert not inspect.isabstract(java_Compilation_unit)


def test_java_compilation_unit_constructor_exists():
    assert callable(java_Compilation_unit.__init__)


def test_java_compilation_unit_constructor_args():
    sig = inspect.signature(java_Compilation_unit.__init__)
    params = list(sig.parameters.keys())



def test_java_head_is_not_abstract():
    assert not inspect.isabstract(java_Head)


def test_java_head_constructor_exists():
    assert callable(java_Head.__init__)


def test_java_head_constructor_args():
    sig = inspect.signature(java_Head.__init__)
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
java_Return_value_strategy = st.builds(
    java_Return_value,
    name=
        safe_text
)
java_Try_statement_strategy = st.builds(
    java_Try_statement,
    try_=
        safe_text,
    catchs=
        safe_text,
    finally_=
        safe_text
)
java_Switch_Statement_strategy = st.builds(
    java_Switch_Statement,
)
java_For_Statement_strategy = st.builds(
    java_For_Statement,
    pv=
        safe_text
)
java_While_Statement_strategy = st.builds(
    java_While_Statement,
)
java_Do_Statement_strategy = st.builds(
    java_Do_Statement,
)
java_If_Statement_strategy = st.builds(
    java_If_Statement,
)
java_Return_Statement_strategy = st.builds(
    java_Return_Statement,
)
java_Statement_strategy = st.builds(
    java_Statement,
    name=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
java_Static_initializer_strategy = st.builds(
    java_Static_initializer,
    static=
        safe_text
)
java_Arg_List_strategy = st.builds(
    java_Arg_List,
)
java_Float_Literal_strategy = st.builds(
    java_Float_Literal,
    decimalDigits2=
        st.integers(),
    exp=
        safe_text,
    decimalDigits1=
        st.integers(),
    floatTypeSufix=
        safe_text
)
java_Ampersand_Rule_strategy = st.builds(
    java_Ampersand_Rule,
    a2=
        safe_text,
    a1=
        safe_text
)
java_Variable_declaration_strategy = st.builds(
    java_Variable_declaration,
    modifiers=
        safe_text
)
java_Parameter_strategy = st.builds(
    java_Parameter,
    name=
        safe_text
)
java_Creating_Expression_strategy = st.builds(
    java_Creating_Expression,
    typeSpecifier=
        safe_text,
    className=
        safe_text
)
java_Cast_Expression_strategy = st.builds(
    java_Cast_Expression,
)
java_Bit_Expression_NR_strategy = st.builds(
    java_Bit_Expression_NR,
)
java_Logical_Expression_NR_strategy = st.builds(
    java_Logical_Expression_NR,
    true=
        safe_text,
    false=
        safe_text
)
java_Expression_aux_strategy = st.builds(
    java_Expression_aux,
    testingSign=
        safe_text,
    stringSign=
        safe_text,
    numericSign=
        safe_text,
    bitSign=
        safe_text,
    sgin=
        safe_text,
    name=
        safe_text,
    logicalSign=
        safe_text
)
java_Numeric_Expression_NR_strategy = st.builds(
    java_Numeric_Expression_NR,
    sinal_numeric=
        safe_text
)
java_Expression_strategy = st.builds(
    java_Expression,
    null=
        safe_text,
    name=
        safe_text,
    super=
        safe_text,
    this=
        safe_text
)
java_Variable_initializer_strategy = st.builds(
    java_Variable_initializer,
)
java_Variable_declarator_strategy = st.builds(
    java_Variable_declarator,
    name=
        safe_text
)
java_Class_declaration_strategy = st.builds(
    java_Class_declaration,
    implements=
        safe_text,
    modifiers=
        safe_text,
    className=
        safe_text,
    extend=
        safe_text,
    implement=
        safe_text
)
java_Field_declaration_strategy = st.builds(
    java_Field_declaration,
    doc=
        safe_text,
    debug=
        safe_text
)
java_Constructor_declaration_strategy = st.builds(
    java_Constructor_declaration,
    name=
        safe_text,
    modifiers=
        safe_text
)
java_Parameter_list_method_call_strategy = st.builds(
    java_Parameter_list_method_call,
    parameters=
        safe_text,
    name=
        safe_text
)
Return_value_strategy = st.builds(
    Return_value,
)
java_Literal_Expression_strategy = st.builds(
    java_Literal_Expression,
    string=
        safe_text,
    exp=
        safe_text,
    exp1=
        st.integers(),
    char=
        safe_text
)
java_Method_call_strategy = st.builds(
    java_Method_call,
)
java_Statement_block_strategy = st.builds(
    java_Statement_block,
)
java_Parameter_list_strategy = st.builds(
    java_Parameter_list,
)
java_Type_strategy = st.builds(
    java_Type,
    name=
        safe_text
)
java_Method_declaration_strategy = st.builds(
    java_Method_declaration,
    debug=
        safe_text,
    name=
        safe_text,
    modifiers=
        safe_text
)
java_Interface_declaration_strategy = st.builds(
    java_Interface_declaration,
    modifiers=
        safe_text,
    extends=
        safe_text,
    extend=
        safe_text,
    interfaceName=
        safe_text
)
java_EObject_strategy = st.builds(
    java_EObject,
)
java_Type_declaration_strategy = st.builds(
    java_Type_declaration,
    doc=
        safe_text
)
java_Import_statement_strategy = st.builds(
    java_Import_statement,
    packagename=
        safe_text,
    classname=
        safe_text
)
java_Package_statement_strategy = st.builds(
    java_Package_statement,
    name=
        safe_text
)
java_Compilation_unit_strategy = st.builds(
    java_Compilation_unit,
)
java_Head_strategy = st.builds(
    java_Head,
)

@given(instance=java_Return_value_strategy)
@settings(max_examples=50)
def test_java_return_value_instantiation(instance):
    assert isinstance(instance, java_Return_value)



@given(instance=java_Return_value_strategy)
def test_java_return_value_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java_Try_statement_strategy)
@settings(max_examples=50)
def test_java_try_statement_instantiation(instance):
    assert isinstance(instance, java_Try_statement)



@given(instance=java_Try_statement_strategy)
def test_java_try_statement_try__setter(instance):
    original = instance.try_
    instance.try_ = original
    assert instance.try_ == original



@given(instance=java_Try_statement_strategy)
def test_java_try_statement_catchs_setter(instance):
    original = instance.catchs
    instance.catchs = original
    assert instance.catchs == original



@given(instance=java_Try_statement_strategy)
def test_java_try_statement_finally__setter(instance):
    original = instance.finally_
    instance.finally_ = original
    assert instance.finally_ == original

@given(instance=java_Switch_Statement_strategy)
@settings(max_examples=50)
def test_java_switch_statement_instantiation(instance):
    assert isinstance(instance, java_Switch_Statement)

@given(instance=java_For_Statement_strategy)
@settings(max_examples=50)
def test_java_for_statement_instantiation(instance):
    assert isinstance(instance, java_For_Statement)



@given(instance=java_For_Statement_strategy)
def test_java_for_statement_pv_setter(instance):
    original = instance.pv
    instance.pv = original
    assert instance.pv == original

@given(instance=java_While_Statement_strategy)
@settings(max_examples=50)
def test_java_while_statement_instantiation(instance):
    assert isinstance(instance, java_While_Statement)

@given(instance=java_Do_Statement_strategy)
@settings(max_examples=50)
def test_java_do_statement_instantiation(instance):
    assert isinstance(instance, java_Do_Statement)

@given(instance=java_If_Statement_strategy)
@settings(max_examples=50)
def test_java_if_statement_instantiation(instance):
    assert isinstance(instance, java_If_Statement)

@given(instance=java_Return_Statement_strategy)
@settings(max_examples=50)
def test_java_return_statement_instantiation(instance):
    assert isinstance(instance, java_Return_Statement)

@given(instance=java_Statement_strategy)
@settings(max_examples=50)
def test_java_statement_instantiation(instance):
    assert isinstance(instance, java_Statement)



@given(instance=java_Statement_strategy)
def test_java_statement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=java_Static_initializer_strategy)
@settings(max_examples=50)
def test_java_static_initializer_instantiation(instance):
    assert isinstance(instance, java_Static_initializer)



@given(instance=java_Static_initializer_strategy)
def test_java_static_initializer_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=java_Arg_List_strategy)
@settings(max_examples=50)
def test_java_arg_list_instantiation(instance):
    assert isinstance(instance, java_Arg_List)

@given(instance=java_Float_Literal_strategy)
@settings(max_examples=50)
def test_java_float_literal_instantiation(instance):
    assert isinstance(instance, java_Float_Literal)



@given(instance=java_Float_Literal_strategy)
def test_java_float_literal_decimalDigits2_setter(instance):
    original = instance.decimalDigits2
    instance.decimalDigits2 = original
    assert instance.decimalDigits2 == original



@given(instance=java_Float_Literal_strategy)
def test_java_float_literal_exp_setter(instance):
    original = instance.exp
    instance.exp = original
    assert instance.exp == original



@given(instance=java_Float_Literal_strategy)
def test_java_float_literal_decimalDigits1_setter(instance):
    original = instance.decimalDigits1
    instance.decimalDigits1 = original
    assert instance.decimalDigits1 == original



@given(instance=java_Float_Literal_strategy)
def test_java_float_literal_floatTypeSufix_setter(instance):
    original = instance.floatTypeSufix
    instance.floatTypeSufix = original
    assert instance.floatTypeSufix == original

@given(instance=java_Ampersand_Rule_strategy)
@settings(max_examples=50)
def test_java_ampersand_rule_instantiation(instance):
    assert isinstance(instance, java_Ampersand_Rule)



@given(instance=java_Ampersand_Rule_strategy)
def test_java_ampersand_rule_a2_setter(instance):
    original = instance.a2
    instance.a2 = original
    assert instance.a2 == original



@given(instance=java_Ampersand_Rule_strategy)
def test_java_ampersand_rule_a1_setter(instance):
    original = instance.a1
    instance.a1 = original
    assert instance.a1 == original

@given(instance=java_Variable_declaration_strategy)
@settings(max_examples=50)
def test_java_variable_declaration_instantiation(instance):
    assert isinstance(instance, java_Variable_declaration)



@given(instance=java_Variable_declaration_strategy)
def test_java_variable_declaration_modifiers_setter(instance):
    original = instance.modifiers
    instance.modifiers = original
    assert instance.modifiers == original

@given(instance=java_Parameter_strategy)
@settings(max_examples=50)
def test_java_parameter_instantiation(instance):
    assert isinstance(instance, java_Parameter)



@given(instance=java_Parameter_strategy)
def test_java_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java_Creating_Expression_strategy)
@settings(max_examples=50)
def test_java_creating_expression_instantiation(instance):
    assert isinstance(instance, java_Creating_Expression)



@given(instance=java_Creating_Expression_strategy)
def test_java_creating_expression_typeSpecifier_setter(instance):
    original = instance.typeSpecifier
    instance.typeSpecifier = original
    assert instance.typeSpecifier == original



@given(instance=java_Creating_Expression_strategy)
def test_java_creating_expression_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=java_Cast_Expression_strategy)
@settings(max_examples=50)
def test_java_cast_expression_instantiation(instance):
    assert isinstance(instance, java_Cast_Expression)

@given(instance=java_Bit_Expression_NR_strategy)
@settings(max_examples=50)
def test_java_bit_expression_nr_instantiation(instance):
    assert isinstance(instance, java_Bit_Expression_NR)

@given(instance=java_Logical_Expression_NR_strategy)
@settings(max_examples=50)
def test_java_logical_expression_nr_instantiation(instance):
    assert isinstance(instance, java_Logical_Expression_NR)



@given(instance=java_Logical_Expression_NR_strategy)
def test_java_logical_expression_nr_true_setter(instance):
    original = instance.true
    instance.true = original
    assert instance.true == original



@given(instance=java_Logical_Expression_NR_strategy)
def test_java_logical_expression_nr_false_setter(instance):
    original = instance.false
    instance.false = original
    assert instance.false == original

@given(instance=java_Expression_aux_strategy)
@settings(max_examples=50)
def test_java_expression_aux_instantiation(instance):
    assert isinstance(instance, java_Expression_aux)



@given(instance=java_Expression_aux_strategy)
def test_java_expression_aux_testingSign_setter(instance):
    original = instance.testingSign
    instance.testingSign = original
    assert instance.testingSign == original



@given(instance=java_Expression_aux_strategy)
def test_java_expression_aux_stringSign_setter(instance):
    original = instance.stringSign
    instance.stringSign = original
    assert instance.stringSign == original



@given(instance=java_Expression_aux_strategy)
def test_java_expression_aux_numericSign_setter(instance):
    original = instance.numericSign
    instance.numericSign = original
    assert instance.numericSign == original



@given(instance=java_Expression_aux_strategy)
def test_java_expression_aux_bitSign_setter(instance):
    original = instance.bitSign
    instance.bitSign = original
    assert instance.bitSign == original



@given(instance=java_Expression_aux_strategy)
def test_java_expression_aux_sgin_setter(instance):
    original = instance.sgin
    instance.sgin = original
    assert instance.sgin == original



@given(instance=java_Expression_aux_strategy)
def test_java_expression_aux_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=java_Expression_aux_strategy)
def test_java_expression_aux_logicalSign_setter(instance):
    original = instance.logicalSign
    instance.logicalSign = original
    assert instance.logicalSign == original

@given(instance=java_Numeric_Expression_NR_strategy)
@settings(max_examples=50)
def test_java_numeric_expression_nr_instantiation(instance):
    assert isinstance(instance, java_Numeric_Expression_NR)



@given(instance=java_Numeric_Expression_NR_strategy)
def test_java_numeric_expression_nr_sinal_numeric_setter(instance):
    original = instance.sinal_numeric
    instance.sinal_numeric = original
    assert instance.sinal_numeric == original

@given(instance=java_Expression_strategy)
@settings(max_examples=50)
def test_java_expression_instantiation(instance):
    assert isinstance(instance, java_Expression)



@given(instance=java_Expression_strategy)
def test_java_expression_null_setter(instance):
    original = instance.null
    instance.null = original
    assert instance.null == original



@given(instance=java_Expression_strategy)
def test_java_expression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=java_Expression_strategy)
def test_java_expression_super_setter(instance):
    original = instance.super
    instance.super = original
    assert instance.super == original



@given(instance=java_Expression_strategy)
def test_java_expression_this_setter(instance):
    original = instance.this
    instance.this = original
    assert instance.this == original

@given(instance=java_Variable_initializer_strategy)
@settings(max_examples=50)
def test_java_variable_initializer_instantiation(instance):
    assert isinstance(instance, java_Variable_initializer)

@given(instance=java_Variable_declarator_strategy)
@settings(max_examples=50)
def test_java_variable_declarator_instantiation(instance):
    assert isinstance(instance, java_Variable_declarator)



@given(instance=java_Variable_declarator_strategy)
def test_java_variable_declarator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java_Class_declaration_strategy)
@settings(max_examples=50)
def test_java_class_declaration_instantiation(instance):
    assert isinstance(instance, java_Class_declaration)



@given(instance=java_Class_declaration_strategy)
def test_java_class_declaration_implements_setter(instance):
    original = instance.implements
    instance.implements = original
    assert instance.implements == original



@given(instance=java_Class_declaration_strategy)
def test_java_class_declaration_modifiers_setter(instance):
    original = instance.modifiers
    instance.modifiers = original
    assert instance.modifiers == original



@given(instance=java_Class_declaration_strategy)
def test_java_class_declaration_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original



@given(instance=java_Class_declaration_strategy)
def test_java_class_declaration_extend_setter(instance):
    original = instance.extend
    instance.extend = original
    assert instance.extend == original



@given(instance=java_Class_declaration_strategy)
def test_java_class_declaration_implement_setter(instance):
    original = instance.implement
    instance.implement = original
    assert instance.implement == original

@given(instance=java_Field_declaration_strategy)
@settings(max_examples=50)
def test_java_field_declaration_instantiation(instance):
    assert isinstance(instance, java_Field_declaration)



@given(instance=java_Field_declaration_strategy)
def test_java_field_declaration_doc_setter(instance):
    original = instance.doc
    instance.doc = original
    assert instance.doc == original



@given(instance=java_Field_declaration_strategy)
def test_java_field_declaration_debug_setter(instance):
    original = instance.debug
    instance.debug = original
    assert instance.debug == original

@given(instance=java_Constructor_declaration_strategy)
@settings(max_examples=50)
def test_java_constructor_declaration_instantiation(instance):
    assert isinstance(instance, java_Constructor_declaration)



@given(instance=java_Constructor_declaration_strategy)
def test_java_constructor_declaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=java_Constructor_declaration_strategy)
def test_java_constructor_declaration_modifiers_setter(instance):
    original = instance.modifiers
    instance.modifiers = original
    assert instance.modifiers == original

@given(instance=java_Parameter_list_method_call_strategy)
@settings(max_examples=50)
def test_java_parameter_list_method_call_instantiation(instance):
    assert isinstance(instance, java_Parameter_list_method_call)



@given(instance=java_Parameter_list_method_call_strategy)
def test_java_parameter_list_method_call_parameters_setter(instance):
    original = instance.parameters
    instance.parameters = original
    assert instance.parameters == original



@given(instance=java_Parameter_list_method_call_strategy)
def test_java_parameter_list_method_call_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Return_value_strategy)
@settings(max_examples=50)
def test_return_value_instantiation(instance):
    assert isinstance(instance, Return_value)

@given(instance=java_Literal_Expression_strategy)
@settings(max_examples=50)
def test_java_literal_expression_instantiation(instance):
    assert isinstance(instance, java_Literal_Expression)



@given(instance=java_Literal_Expression_strategy)
def test_java_literal_expression_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original



@given(instance=java_Literal_Expression_strategy)
def test_java_literal_expression_exp_setter(instance):
    original = instance.exp
    instance.exp = original
    assert instance.exp == original



@given(instance=java_Literal_Expression_strategy)
def test_java_literal_expression_exp1_setter(instance):
    original = instance.exp1
    instance.exp1 = original
    assert instance.exp1 == original



@given(instance=java_Literal_Expression_strategy)
def test_java_literal_expression_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original

@given(instance=java_Method_call_strategy)
@settings(max_examples=50)
def test_java_method_call_instantiation(instance):
    assert isinstance(instance, java_Method_call)

@given(instance=java_Statement_block_strategy)
@settings(max_examples=50)
def test_java_statement_block_instantiation(instance):
    assert isinstance(instance, java_Statement_block)

@given(instance=java_Parameter_list_strategy)
@settings(max_examples=50)
def test_java_parameter_list_instantiation(instance):
    assert isinstance(instance, java_Parameter_list)

@given(instance=java_Type_strategy)
@settings(max_examples=50)
def test_java_type_instantiation(instance):
    assert isinstance(instance, java_Type)



@given(instance=java_Type_strategy)
def test_java_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java_Method_declaration_strategy)
@settings(max_examples=50)
def test_java_method_declaration_instantiation(instance):
    assert isinstance(instance, java_Method_declaration)



@given(instance=java_Method_declaration_strategy)
def test_java_method_declaration_debug_setter(instance):
    original = instance.debug
    instance.debug = original
    assert instance.debug == original



@given(instance=java_Method_declaration_strategy)
def test_java_method_declaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=java_Method_declaration_strategy)
def test_java_method_declaration_modifiers_setter(instance):
    original = instance.modifiers
    instance.modifiers = original
    assert instance.modifiers == original

@given(instance=java_Interface_declaration_strategy)
@settings(max_examples=50)
def test_java_interface_declaration_instantiation(instance):
    assert isinstance(instance, java_Interface_declaration)



@given(instance=java_Interface_declaration_strategy)
def test_java_interface_declaration_modifiers_setter(instance):
    original = instance.modifiers
    instance.modifiers = original
    assert instance.modifiers == original



@given(instance=java_Interface_declaration_strategy)
def test_java_interface_declaration_extends_setter(instance):
    original = instance.extends
    instance.extends = original
    assert instance.extends == original



@given(instance=java_Interface_declaration_strategy)
def test_java_interface_declaration_extend_setter(instance):
    original = instance.extend
    instance.extend = original
    assert instance.extend == original



@given(instance=java_Interface_declaration_strategy)
def test_java_interface_declaration_interfaceName_setter(instance):
    original = instance.interfaceName
    instance.interfaceName = original
    assert instance.interfaceName == original

@given(instance=java_EObject_strategy)
@settings(max_examples=50)
def test_java_eobject_instantiation(instance):
    assert isinstance(instance, java_EObject)

@given(instance=java_Type_declaration_strategy)
@settings(max_examples=50)
def test_java_type_declaration_instantiation(instance):
    assert isinstance(instance, java_Type_declaration)



@given(instance=java_Type_declaration_strategy)
def test_java_type_declaration_doc_setter(instance):
    original = instance.doc
    instance.doc = original
    assert instance.doc == original

@given(instance=java_Import_statement_strategy)
@settings(max_examples=50)
def test_java_import_statement_instantiation(instance):
    assert isinstance(instance, java_Import_statement)



@given(instance=java_Import_statement_strategy)
def test_java_import_statement_packagename_setter(instance):
    original = instance.packagename
    instance.packagename = original
    assert instance.packagename == original



@given(instance=java_Import_statement_strategy)
def test_java_import_statement_classname_setter(instance):
    original = instance.classname
    instance.classname = original
    assert instance.classname == original

@given(instance=java_Package_statement_strategy)
@settings(max_examples=50)
def test_java_package_statement_instantiation(instance):
    assert isinstance(instance, java_Package_statement)



@given(instance=java_Package_statement_strategy)
def test_java_package_statement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java_Compilation_unit_strategy)
@settings(max_examples=50)
def test_java_compilation_unit_instantiation(instance):
    assert isinstance(instance, java_Compilation_unit)

@given(instance=java_Head_strategy)
@settings(max_examples=50)
def test_java_head_instantiation(instance):
    assert isinstance(instance, java_Head)
