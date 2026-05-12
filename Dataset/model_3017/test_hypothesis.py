import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    type_specifier,
    myDsl_declaration_list2,
    myDsl_external_declaration,
    myDsl_EObject,
    myDsl_declaration_list,
    myDsl_function_definition,
    myDsl_jump_statement,
    myDsl_iteration_statement,
    myDsl_selection_statement,
    myDsl_expression_statement,
    myDsl_compound_statement,
    myDsl_labeled_statement,
    myDsl_statement,
    myDsl_block_item,
    myDsl_initializer_list2,
    myDsl_designation,
    myDsl_initializer,
    myDsl_direct_abstract_declarator2,
    myDsl_direct_abstract_declarator,
    myDsl_designator_list2,
    myDsl_designator,
    myDsl_designator_list,
    myDsl_parameter_list2,
    myDsl_parameter_declaration,
    myDsl_parameter_list,
    myDsl_type_qualifier_list2,
    myDsl_identifier_list2,
    myDsl_abstract_declarator,
    myDsl_direct_declarator,
    myDsl_pointer,
    myDsl_identifier_list,
    myDsl_parameter_type_list,
    myDsl_type_qualifier_list,
    myDsl_direct_declarator2,
    myDsl_struct_declarator_list2,
    myDsl_struct_declarator,
    myDsl_struct_declarator_list,
    myDsl_specifier_qualifier_list,
    myDsl_enumerator_list2,
    myDsl_enumerator,
    myDsl_enumerator_list,
    myDsl_atomic_type_specifier,
    myDsl_declarator,
    myDsl_init_declarator_list2,
    myDsl_init_declarator,
    myDsl_alignment_specifier,
    myDsl_struct_declaration_list2,
    myDsl_struct_declaration,
    struct_or_union_specifier,
    myDsl_struct_declaration_list,
    myDsl_struct_or_union,
    myDsl_enum_specifier,
    myDsl_struct_or_union_specifier,
    myDsl_declaration_specifiers,
    myDsl_declaration,
    myDsl_constant_expression,
    myDsl_expression2,
    myDsl_assignment_operator,
    myDsl_function_specifier,
    myDsl_type_qualifier,
    myDsl_type_specifier,
    myDsl_storage_class_specifier,
    myDsl_static_assert_declaration,
    myDsl_init_declarator_list,
    simple_expression,
    myDsl_variableRef,
    myDsl_MINUS,
    myDsl_intType,
    myDsl_floatType,
    myDsl_ADD,
    myDsl_unary_expression,
    postfix_expression2,
    myDsl_argument_expression_list,
    myDsl_initializer_list,
    myDsl_postfix_expression2,
    myDsl_postfix_expression,
    myDsl_generic_association,
    myDsl_generic_assoc_list,
    myDsl_assignment_expression,
    myDsl_expression,
    myDsl_conditional_expression,
    myDsl_constant,
    myDsl_type_name,
    myDsl_simple_expression,
    myDsl_translation_unit,
    myDsl_Model,
    myDsl_generic_selection,
    myDsl_string_nova,
    myDsl_enumeration_constant,
    myDsl_unsignedType,
    myDsl_signedType,
    myDsl_doubleType,
    myDsl_longType,
    myDsl_shortType,
    myDsl_charType,
    myDsl_voidType,
    myDsl_LOG_OR,
    myDsl_imaginaryType,
    myDsl_complexType,
    myDsl_AND,
    myDsl_EQL,
    myDsl_REL,
    myDsl_SHF,
    myDsl_LOG_AND,
    myDsl_INC_OR,
    myDsl_MUL,
    myDsl_EXC_OR,
    myDsl_booleanType,
    myDsl_stringType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_type_specifier_is_not_abstract():
    assert not inspect.isabstract(type_specifier)


def test_type_specifier_constructor_exists():
    assert callable(type_specifier.__init__)


def test_type_specifier_constructor_args():
    sig = inspect.signature(type_specifier.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_declaration_list2_is_not_abstract():
    assert not inspect.isabstract(myDsl_declaration_list2)


def test_mydsl_declaration_list2_constructor_exists():
    assert callable(myDsl_declaration_list2.__init__)


def test_mydsl_declaration_list2_constructor_args():
    sig = inspect.signature(myDsl_declaration_list2.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_external_declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl_external_declaration)


def test_mydsl_external_declaration_constructor_exists():
    assert callable(myDsl_external_declaration.__init__)


def test_mydsl_external_declaration_constructor_args():
    sig = inspect.signature(myDsl_external_declaration.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_eobject_is_not_abstract():
    assert not inspect.isabstract(myDsl_EObject)


def test_mydsl_eobject_constructor_exists():
    assert callable(myDsl_EObject.__init__)


def test_mydsl_eobject_constructor_args():
    sig = inspect.signature(myDsl_EObject.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_declaration_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_declaration_list)


def test_mydsl_declaration_list_constructor_exists():
    assert callable(myDsl_declaration_list.__init__)


def test_mydsl_declaration_list_constructor_args():
    sig = inspect.signature(myDsl_declaration_list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_function_definition_is_not_abstract():
    assert not inspect.isabstract(myDsl_function_definition)


def test_mydsl_function_definition_constructor_exists():
    assert callable(myDsl_function_definition.__init__)


def test_mydsl_function_definition_constructor_args():
    sig = inspect.signature(myDsl_function_definition.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_jump_statement_is_not_abstract():
    assert not inspect.isabstract(myDsl_jump_statement)


def test_mydsl_jump_statement_constructor_exists():
    assert callable(myDsl_jump_statement.__init__)


def test_mydsl_jump_statement_constructor_args():
    sig = inspect.signature(myDsl_jump_statement.__init__)
    params = list(sig.parameters.keys())
    assert "return_" in params, "Missing parameter 'return_'"
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "continue_" in params, "Missing parameter 'continue_'"
    assert "goto" in params, "Missing parameter 'goto'"
    assert "break_" in params, "Missing parameter 'break_'"

def test_mydsl_jump_statement_has_return_():
    assert hasattr(myDsl_jump_statement, "return_")
    descriptor = None
    for klass in myDsl_jump_statement.__mro__:
        if "return_" in klass.__dict__:
            descriptor = klass.__dict__["return_"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_jump_statement_has_identifier():
    assert hasattr(myDsl_jump_statement, "identifier")
    descriptor = None
    for klass in myDsl_jump_statement.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_jump_statement_has_continue_():
    assert hasattr(myDsl_jump_statement, "continue_")
    descriptor = None
    for klass in myDsl_jump_statement.__mro__:
        if "continue_" in klass.__dict__:
            descriptor = klass.__dict__["continue_"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_jump_statement_has_goto():
    assert hasattr(myDsl_jump_statement, "goto")
    descriptor = None
    for klass in myDsl_jump_statement.__mro__:
        if "goto" in klass.__dict__:
            descriptor = klass.__dict__["goto"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_jump_statement_has_break_():
    assert hasattr(myDsl_jump_statement, "break_")
    descriptor = None
    for klass in myDsl_jump_statement.__mro__:
        if "break_" in klass.__dict__:
            descriptor = klass.__dict__["break_"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_iteration_statement_is_not_abstract():
    assert not inspect.isabstract(myDsl_iteration_statement)


def test_mydsl_iteration_statement_constructor_exists():
    assert callable(myDsl_iteration_statement.__init__)


def test_mydsl_iteration_statement_constructor_args():
    sig = inspect.signature(myDsl_iteration_statement.__init__)
    params = list(sig.parameters.keys())
    assert "while_" in params, "Missing parameter 'while_'"
    assert "for_" in params, "Missing parameter 'for_'"
    assert "do" in params, "Missing parameter 'do'"

def test_mydsl_iteration_statement_has_while_():
    assert hasattr(myDsl_iteration_statement, "while_")
    descriptor = None
    for klass in myDsl_iteration_statement.__mro__:
        if "while_" in klass.__dict__:
            descriptor = klass.__dict__["while_"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_iteration_statement_has_for_():
    assert hasattr(myDsl_iteration_statement, "for_")
    descriptor = None
    for klass in myDsl_iteration_statement.__mro__:
        if "for_" in klass.__dict__:
            descriptor = klass.__dict__["for_"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_iteration_statement_has_do():
    assert hasattr(myDsl_iteration_statement, "do")
    descriptor = None
    for klass in myDsl_iteration_statement.__mro__:
        if "do" in klass.__dict__:
            descriptor = klass.__dict__["do"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_selection_statement_is_not_abstract():
    assert not inspect.isabstract(myDsl_selection_statement)


def test_mydsl_selection_statement_constructor_exists():
    assert callable(myDsl_selection_statement.__init__)


def test_mydsl_selection_statement_constructor_args():
    sig = inspect.signature(myDsl_selection_statement.__init__)
    params = list(sig.parameters.keys())
    assert "else_" in params, "Missing parameter 'else_'"
    assert "if_" in params, "Missing parameter 'if_'"
    assert "switch" in params, "Missing parameter 'switch'"

def test_mydsl_selection_statement_has_else_():
    assert hasattr(myDsl_selection_statement, "else_")
    descriptor = None
    for klass in myDsl_selection_statement.__mro__:
        if "else_" in klass.__dict__:
            descriptor = klass.__dict__["else_"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_selection_statement_has_if_():
    assert hasattr(myDsl_selection_statement, "if_")
    descriptor = None
    for klass in myDsl_selection_statement.__mro__:
        if "if_" in klass.__dict__:
            descriptor = klass.__dict__["if_"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_selection_statement_has_switch():
    assert hasattr(myDsl_selection_statement, "switch")
    descriptor = None
    for klass in myDsl_selection_statement.__mro__:
        if "switch" in klass.__dict__:
            descriptor = klass.__dict__["switch"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_expression_statement_is_not_abstract():
    assert not inspect.isabstract(myDsl_expression_statement)


def test_mydsl_expression_statement_constructor_exists():
    assert callable(myDsl_expression_statement.__init__)


def test_mydsl_expression_statement_constructor_args():
    sig = inspect.signature(myDsl_expression_statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_compound_statement_is_not_abstract():
    assert not inspect.isabstract(myDsl_compound_statement)


def test_mydsl_compound_statement_constructor_exists():
    assert callable(myDsl_compound_statement.__init__)


def test_mydsl_compound_statement_constructor_args():
    sig = inspect.signature(myDsl_compound_statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_labeled_statement_is_not_abstract():
    assert not inspect.isabstract(myDsl_labeled_statement)


def test_mydsl_labeled_statement_constructor_exists():
    assert callable(myDsl_labeled_statement.__init__)


def test_mydsl_labeled_statement_constructor_args():
    sig = inspect.signature(myDsl_labeled_statement.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "default" in params, "Missing parameter 'default'"
    assert "case" in params, "Missing parameter 'case'"

def test_mydsl_labeled_statement_has_identifier():
    assert hasattr(myDsl_labeled_statement, "identifier")
    descriptor = None
    for klass in myDsl_labeled_statement.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_labeled_statement_has_default():
    assert hasattr(myDsl_labeled_statement, "default")
    descriptor = None
    for klass in myDsl_labeled_statement.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_labeled_statement_has_case():
    assert hasattr(myDsl_labeled_statement, "case")
    descriptor = None
    for klass in myDsl_labeled_statement.__mro__:
        if "case" in klass.__dict__:
            descriptor = klass.__dict__["case"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_statement_is_not_abstract():
    assert not inspect.isabstract(myDsl_statement)


def test_mydsl_statement_constructor_exists():
    assert callable(myDsl_statement.__init__)


def test_mydsl_statement_constructor_args():
    sig = inspect.signature(myDsl_statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_block_item_is_not_abstract():
    assert not inspect.isabstract(myDsl_block_item)


def test_mydsl_block_item_constructor_exists():
    assert callable(myDsl_block_item.__init__)


def test_mydsl_block_item_constructor_args():
    sig = inspect.signature(myDsl_block_item.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_initializer_list2_is_not_abstract():
    assert not inspect.isabstract(myDsl_initializer_list2)


def test_mydsl_initializer_list2_constructor_exists():
    assert callable(myDsl_initializer_list2.__init__)


def test_mydsl_initializer_list2_constructor_args():
    sig = inspect.signature(myDsl_initializer_list2.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_designation_is_not_abstract():
    assert not inspect.isabstract(myDsl_designation)


def test_mydsl_designation_constructor_exists():
    assert callable(myDsl_designation.__init__)


def test_mydsl_designation_constructor_args():
    sig = inspect.signature(myDsl_designation.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_initializer_is_not_abstract():
    assert not inspect.isabstract(myDsl_initializer)


def test_mydsl_initializer_constructor_exists():
    assert callable(myDsl_initializer.__init__)


def test_mydsl_initializer_constructor_args():
    sig = inspect.signature(myDsl_initializer.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_direct_abstract_declarator2_is_not_abstract():
    assert not inspect.isabstract(myDsl_direct_abstract_declarator2)


def test_mydsl_direct_abstract_declarator2_constructor_exists():
    assert callable(myDsl_direct_abstract_declarator2.__init__)


def test_mydsl_direct_abstract_declarator2_constructor_args():
    sig = inspect.signature(myDsl_direct_abstract_declarator2.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_mydsl_direct_abstract_declarator2_has_static():
    assert hasattr(myDsl_direct_abstract_declarator2, "static")
    descriptor = None
    for klass in myDsl_direct_abstract_declarator2.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_direct_abstract_declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl_direct_abstract_declarator)


def test_mydsl_direct_abstract_declarator_constructor_exists():
    assert callable(myDsl_direct_abstract_declarator.__init__)


def test_mydsl_direct_abstract_declarator_constructor_args():
    sig = inspect.signature(myDsl_direct_abstract_declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_designator_list2_is_not_abstract():
    assert not inspect.isabstract(myDsl_designator_list2)


def test_mydsl_designator_list2_constructor_exists():
    assert callable(myDsl_designator_list2.__init__)


def test_mydsl_designator_list2_constructor_args():
    sig = inspect.signature(myDsl_designator_list2.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_designator_is_not_abstract():
    assert not inspect.isabstract(myDsl_designator)


def test_mydsl_designator_constructor_exists():
    assert callable(myDsl_designator.__init__)


def test_mydsl_designator_constructor_args():
    sig = inspect.signature(myDsl_designator.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_mydsl_designator_has_identifier():
    assert hasattr(myDsl_designator, "identifier")
    descriptor = None
    for klass in myDsl_designator.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_designator_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_designator_list)


def test_mydsl_designator_list_constructor_exists():
    assert callable(myDsl_designator_list.__init__)


def test_mydsl_designator_list_constructor_args():
    sig = inspect.signature(myDsl_designator_list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_parameter_list2_is_not_abstract():
    assert not inspect.isabstract(myDsl_parameter_list2)


def test_mydsl_parameter_list2_constructor_exists():
    assert callable(myDsl_parameter_list2.__init__)


def test_mydsl_parameter_list2_constructor_args():
    sig = inspect.signature(myDsl_parameter_list2.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_parameter_declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl_parameter_declaration)


def test_mydsl_parameter_declaration_constructor_exists():
    assert callable(myDsl_parameter_declaration.__init__)


def test_mydsl_parameter_declaration_constructor_args():
    sig = inspect.signature(myDsl_parameter_declaration.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_parameter_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_parameter_list)


def test_mydsl_parameter_list_constructor_exists():
    assert callable(myDsl_parameter_list.__init__)


def test_mydsl_parameter_list_constructor_args():
    sig = inspect.signature(myDsl_parameter_list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_type_qualifier_list2_is_not_abstract():
    assert not inspect.isabstract(myDsl_type_qualifier_list2)


def test_mydsl_type_qualifier_list2_constructor_exists():
    assert callable(myDsl_type_qualifier_list2.__init__)


def test_mydsl_type_qualifier_list2_constructor_args():
    sig = inspect.signature(myDsl_type_qualifier_list2.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_identifier_list2_is_not_abstract():
    assert not inspect.isabstract(myDsl_identifier_list2)


def test_mydsl_identifier_list2_constructor_exists():
    assert callable(myDsl_identifier_list2.__init__)


def test_mydsl_identifier_list2_constructor_args():
    sig = inspect.signature(myDsl_identifier_list2.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_mydsl_identifier_list2_has_identifier():
    assert hasattr(myDsl_identifier_list2, "identifier")
    descriptor = None
    for klass in myDsl_identifier_list2.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_abstract_declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl_abstract_declarator)


def test_mydsl_abstract_declarator_constructor_exists():
    assert callable(myDsl_abstract_declarator.__init__)


def test_mydsl_abstract_declarator_constructor_args():
    sig = inspect.signature(myDsl_abstract_declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_direct_declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl_direct_declarator)


def test_mydsl_direct_declarator_constructor_exists():
    assert callable(myDsl_direct_declarator.__init__)


def test_mydsl_direct_declarator_constructor_args():
    sig = inspect.signature(myDsl_direct_declarator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_direct_declarator_has_name():
    assert hasattr(myDsl_direct_declarator, "name")
    descriptor = None
    for klass in myDsl_direct_declarator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_pointer_is_not_abstract():
    assert not inspect.isabstract(myDsl_pointer)


def test_mydsl_pointer_constructor_exists():
    assert callable(myDsl_pointer.__init__)


def test_mydsl_pointer_constructor_args():
    sig = inspect.signature(myDsl_pointer.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_identifier_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_identifier_list)


def test_mydsl_identifier_list_constructor_exists():
    assert callable(myDsl_identifier_list.__init__)


def test_mydsl_identifier_list_constructor_args():
    sig = inspect.signature(myDsl_identifier_list.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_mydsl_identifier_list_has_identifier():
    assert hasattr(myDsl_identifier_list, "identifier")
    descriptor = None
    for klass in myDsl_identifier_list.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_parameter_type_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_parameter_type_list)


def test_mydsl_parameter_type_list_constructor_exists():
    assert callable(myDsl_parameter_type_list.__init__)


def test_mydsl_parameter_type_list_constructor_args():
    sig = inspect.signature(myDsl_parameter_type_list.__init__)
    params = list(sig.parameters.keys())
    assert "ellipsis" in params, "Missing parameter 'ellipsis'"

def test_mydsl_parameter_type_list_has_ellipsis():
    assert hasattr(myDsl_parameter_type_list, "ellipsis")
    descriptor = None
    for klass in myDsl_parameter_type_list.__mro__:
        if "ellipsis" in klass.__dict__:
            descriptor = klass.__dict__["ellipsis"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_type_qualifier_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_type_qualifier_list)


def test_mydsl_type_qualifier_list_constructor_exists():
    assert callable(myDsl_type_qualifier_list.__init__)


def test_mydsl_type_qualifier_list_constructor_args():
    sig = inspect.signature(myDsl_type_qualifier_list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_direct_declarator2_is_not_abstract():
    assert not inspect.isabstract(myDsl_direct_declarator2)


def test_mydsl_direct_declarator2_constructor_exists():
    assert callable(myDsl_direct_declarator2.__init__)


def test_mydsl_direct_declarator2_constructor_args():
    sig = inspect.signature(myDsl_direct_declarator2.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_mydsl_direct_declarator2_has_static():
    assert hasattr(myDsl_direct_declarator2, "static")
    descriptor = None
    for klass in myDsl_direct_declarator2.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_struct_declarator_list2_is_not_abstract():
    assert not inspect.isabstract(myDsl_struct_declarator_list2)


def test_mydsl_struct_declarator_list2_constructor_exists():
    assert callable(myDsl_struct_declarator_list2.__init__)


def test_mydsl_struct_declarator_list2_constructor_args():
    sig = inspect.signature(myDsl_struct_declarator_list2.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_struct_declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl_struct_declarator)


def test_mydsl_struct_declarator_constructor_exists():
    assert callable(myDsl_struct_declarator.__init__)


def test_mydsl_struct_declarator_constructor_args():
    sig = inspect.signature(myDsl_struct_declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_struct_declarator_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_struct_declarator_list)


def test_mydsl_struct_declarator_list_constructor_exists():
    assert callable(myDsl_struct_declarator_list.__init__)


def test_mydsl_struct_declarator_list_constructor_args():
    sig = inspect.signature(myDsl_struct_declarator_list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_specifier_qualifier_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_specifier_qualifier_list)


def test_mydsl_specifier_qualifier_list_constructor_exists():
    assert callable(myDsl_specifier_qualifier_list.__init__)


def test_mydsl_specifier_qualifier_list_constructor_args():
    sig = inspect.signature(myDsl_specifier_qualifier_list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_enumerator_list2_is_not_abstract():
    assert not inspect.isabstract(myDsl_enumerator_list2)


def test_mydsl_enumerator_list2_constructor_exists():
    assert callable(myDsl_enumerator_list2.__init__)


def test_mydsl_enumerator_list2_constructor_args():
    sig = inspect.signature(myDsl_enumerator_list2.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_enumerator_is_not_abstract():
    assert not inspect.isabstract(myDsl_enumerator)


def test_mydsl_enumerator_constructor_exists():
    assert callable(myDsl_enumerator.__init__)


def test_mydsl_enumerator_constructor_args():
    sig = inspect.signature(myDsl_enumerator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_enumerator_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_enumerator_list)


def test_mydsl_enumerator_list_constructor_exists():
    assert callable(myDsl_enumerator_list.__init__)


def test_mydsl_enumerator_list_constructor_args():
    sig = inspect.signature(myDsl_enumerator_list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_atomic_type_specifier_is_not_abstract():
    assert not inspect.isabstract(myDsl_atomic_type_specifier)


def test_mydsl_atomic_type_specifier_constructor_exists():
    assert callable(myDsl_atomic_type_specifier.__init__)


def test_mydsl_atomic_type_specifier_constructor_args():
    sig = inspect.signature(myDsl_atomic_type_specifier.__init__)
    params = list(sig.parameters.keys())
    assert "atomic" in params, "Missing parameter 'atomic'"

def test_mydsl_atomic_type_specifier_has_atomic():
    assert hasattr(myDsl_atomic_type_specifier, "atomic")
    descriptor = None
    for klass in myDsl_atomic_type_specifier.__mro__:
        if "atomic" in klass.__dict__:
            descriptor = klass.__dict__["atomic"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl_declarator)


def test_mydsl_declarator_constructor_exists():
    assert callable(myDsl_declarator.__init__)


def test_mydsl_declarator_constructor_args():
    sig = inspect.signature(myDsl_declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_init_declarator_list2_is_not_abstract():
    assert not inspect.isabstract(myDsl_init_declarator_list2)


def test_mydsl_init_declarator_list2_constructor_exists():
    assert callable(myDsl_init_declarator_list2.__init__)


def test_mydsl_init_declarator_list2_constructor_args():
    sig = inspect.signature(myDsl_init_declarator_list2.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_init_declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl_init_declarator)


def test_mydsl_init_declarator_constructor_exists():
    assert callable(myDsl_init_declarator.__init__)


def test_mydsl_init_declarator_constructor_args():
    sig = inspect.signature(myDsl_init_declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_alignment_specifier_is_not_abstract():
    assert not inspect.isabstract(myDsl_alignment_specifier)


def test_mydsl_alignment_specifier_constructor_exists():
    assert callable(myDsl_alignment_specifier.__init__)


def test_mydsl_alignment_specifier_constructor_args():
    sig = inspect.signature(myDsl_alignment_specifier.__init__)
    params = list(sig.parameters.keys())
    assert "alignas" in params, "Missing parameter 'alignas'"

def test_mydsl_alignment_specifier_has_alignas():
    assert hasattr(myDsl_alignment_specifier, "alignas")
    descriptor = None
    for klass in myDsl_alignment_specifier.__mro__:
        if "alignas" in klass.__dict__:
            descriptor = klass.__dict__["alignas"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_struct_declaration_list2_is_not_abstract():
    assert not inspect.isabstract(myDsl_struct_declaration_list2)


def test_mydsl_struct_declaration_list2_constructor_exists():
    assert callable(myDsl_struct_declaration_list2.__init__)


def test_mydsl_struct_declaration_list2_constructor_args():
    sig = inspect.signature(myDsl_struct_declaration_list2.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_struct_declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl_struct_declaration)


def test_mydsl_struct_declaration_constructor_exists():
    assert callable(myDsl_struct_declaration.__init__)


def test_mydsl_struct_declaration_constructor_args():
    sig = inspect.signature(myDsl_struct_declaration.__init__)
    params = list(sig.parameters.keys())



def test_struct_or_union_specifier_is_not_abstract():
    assert not inspect.isabstract(struct_or_union_specifier)


def test_struct_or_union_specifier_constructor_exists():
    assert callable(struct_or_union_specifier.__init__)


def test_struct_or_union_specifier_constructor_args():
    sig = inspect.signature(struct_or_union_specifier.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_struct_declaration_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_struct_declaration_list)


def test_mydsl_struct_declaration_list_constructor_exists():
    assert callable(myDsl_struct_declaration_list.__init__)


def test_mydsl_struct_declaration_list_constructor_args():
    sig = inspect.signature(myDsl_struct_declaration_list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_struct_or_union_is_not_abstract():
    assert not inspect.isabstract(myDsl_struct_or_union)


def test_mydsl_struct_or_union_constructor_exists():
    assert callable(myDsl_struct_or_union.__init__)


def test_mydsl_struct_or_union_constructor_args():
    sig = inspect.signature(myDsl_struct_or_union.__init__)
    params = list(sig.parameters.keys())
    assert "union" in params, "Missing parameter 'union'"
    assert "struct" in params, "Missing parameter 'struct'"

def test_mydsl_struct_or_union_has_union():
    assert hasattr(myDsl_struct_or_union, "union")
    descriptor = None
    for klass in myDsl_struct_or_union.__mro__:
        if "union" in klass.__dict__:
            descriptor = klass.__dict__["union"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_struct_or_union_has_struct():
    assert hasattr(myDsl_struct_or_union, "struct")
    descriptor = None
    for klass in myDsl_struct_or_union.__mro__:
        if "struct" in klass.__dict__:
            descriptor = klass.__dict__["struct"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_enum_specifier_is_not_abstract():
    assert not inspect.isabstract(myDsl_enum_specifier)


def test_mydsl_enum_specifier_constructor_exists():
    assert callable(myDsl_enum_specifier.__init__)


def test_mydsl_enum_specifier_constructor_args():
    sig = inspect.signature(myDsl_enum_specifier.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "enumt" in params, "Missing parameter 'enumt'"

def test_mydsl_enum_specifier_has_identifier():
    assert hasattr(myDsl_enum_specifier, "identifier")
    descriptor = None
    for klass in myDsl_enum_specifier.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_enum_specifier_has_enumt():
    assert hasattr(myDsl_enum_specifier, "enumt")
    descriptor = None
    for klass in myDsl_enum_specifier.__mro__:
        if "enumt" in klass.__dict__:
            descriptor = klass.__dict__["enumt"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_struct_or_union_specifier_is_not_abstract():
    assert not inspect.isabstract(myDsl_struct_or_union_specifier)


def test_mydsl_struct_or_union_specifier_constructor_exists():
    assert callable(myDsl_struct_or_union_specifier.__init__)


def test_mydsl_struct_or_union_specifier_constructor_args():
    sig = inspect.signature(myDsl_struct_or_union_specifier.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_mydsl_struct_or_union_specifier_has_identifier():
    assert hasattr(myDsl_struct_or_union_specifier, "identifier")
    descriptor = None
    for klass in myDsl_struct_or_union_specifier.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_declaration_specifiers_is_not_abstract():
    assert not inspect.isabstract(myDsl_declaration_specifiers)


def test_mydsl_declaration_specifiers_constructor_exists():
    assert callable(myDsl_declaration_specifiers.__init__)


def test_mydsl_declaration_specifiers_constructor_args():
    sig = inspect.signature(myDsl_declaration_specifiers.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl_declaration)


def test_mydsl_declaration_constructor_exists():
    assert callable(myDsl_declaration.__init__)


def test_mydsl_declaration_constructor_args():
    sig = inspect.signature(myDsl_declaration.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_constant_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_constant_expression)


def test_mydsl_constant_expression_constructor_exists():
    assert callable(myDsl_constant_expression.__init__)


def test_mydsl_constant_expression_constructor_args():
    sig = inspect.signature(myDsl_constant_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_expression2_is_not_abstract():
    assert not inspect.isabstract(myDsl_expression2)


def test_mydsl_expression2_constructor_exists():
    assert callable(myDsl_expression2.__init__)


def test_mydsl_expression2_constructor_args():
    sig = inspect.signature(myDsl_expression2.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_assignment_operator_is_not_abstract():
    assert not inspect.isabstract(myDsl_assignment_operator)


def test_mydsl_assignment_operator_constructor_exists():
    assert callable(myDsl_assignment_operator.__init__)


def test_mydsl_assignment_operator_constructor_args():
    sig = inspect.signature(myDsl_assignment_operator.__init__)
    params = list(sig.parameters.keys())
    assert "left_assign" in params, "Missing parameter 'left_assign'"
    assert "or_assign" in params, "Missing parameter 'or_assign'"
    assert "and_assign" in params, "Missing parameter 'and_assign'"
    assert "add_assign" in params, "Missing parameter 'add_assign'"
    assert "right_assign" in params, "Missing parameter 'right_assign'"
    assert "sub_assign" in params, "Missing parameter 'sub_assign'"
    assert "mul_assign" in params, "Missing parameter 'mul_assign'"
    assert "mod_assign" in params, "Missing parameter 'mod_assign'"
    assert "xor_assign" in params, "Missing parameter 'xor_assign'"
    assert "div_assign" in params, "Missing parameter 'div_assign'"

def test_mydsl_assignment_operator_has_left_assign():
    assert hasattr(myDsl_assignment_operator, "left_assign")
    descriptor = None
    for klass in myDsl_assignment_operator.__mro__:
        if "left_assign" in klass.__dict__:
            descriptor = klass.__dict__["left_assign"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_assignment_operator_has_or_assign():
    assert hasattr(myDsl_assignment_operator, "or_assign")
    descriptor = None
    for klass in myDsl_assignment_operator.__mro__:
        if "or_assign" in klass.__dict__:
            descriptor = klass.__dict__["or_assign"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_assignment_operator_has_and_assign():
    assert hasattr(myDsl_assignment_operator, "and_assign")
    descriptor = None
    for klass in myDsl_assignment_operator.__mro__:
        if "and_assign" in klass.__dict__:
            descriptor = klass.__dict__["and_assign"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_assignment_operator_has_add_assign():
    assert hasattr(myDsl_assignment_operator, "add_assign")
    descriptor = None
    for klass in myDsl_assignment_operator.__mro__:
        if "add_assign" in klass.__dict__:
            descriptor = klass.__dict__["add_assign"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_assignment_operator_has_right_assign():
    assert hasattr(myDsl_assignment_operator, "right_assign")
    descriptor = None
    for klass in myDsl_assignment_operator.__mro__:
        if "right_assign" in klass.__dict__:
            descriptor = klass.__dict__["right_assign"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_assignment_operator_has_sub_assign():
    assert hasattr(myDsl_assignment_operator, "sub_assign")
    descriptor = None
    for klass in myDsl_assignment_operator.__mro__:
        if "sub_assign" in klass.__dict__:
            descriptor = klass.__dict__["sub_assign"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_assignment_operator_has_mul_assign():
    assert hasattr(myDsl_assignment_operator, "mul_assign")
    descriptor = None
    for klass in myDsl_assignment_operator.__mro__:
        if "mul_assign" in klass.__dict__:
            descriptor = klass.__dict__["mul_assign"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_assignment_operator_has_mod_assign():
    assert hasattr(myDsl_assignment_operator, "mod_assign")
    descriptor = None
    for klass in myDsl_assignment_operator.__mro__:
        if "mod_assign" in klass.__dict__:
            descriptor = klass.__dict__["mod_assign"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_assignment_operator_has_xor_assign():
    assert hasattr(myDsl_assignment_operator, "xor_assign")
    descriptor = None
    for klass in myDsl_assignment_operator.__mro__:
        if "xor_assign" in klass.__dict__:
            descriptor = klass.__dict__["xor_assign"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_assignment_operator_has_div_assign():
    assert hasattr(myDsl_assignment_operator, "div_assign")
    descriptor = None
    for klass in myDsl_assignment_operator.__mro__:
        if "div_assign" in klass.__dict__:
            descriptor = klass.__dict__["div_assign"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_function_specifier_is_not_abstract():
    assert not inspect.isabstract(myDsl_function_specifier)


def test_mydsl_function_specifier_constructor_exists():
    assert callable(myDsl_function_specifier.__init__)


def test_mydsl_function_specifier_constructor_args():
    sig = inspect.signature(myDsl_function_specifier.__init__)
    params = list(sig.parameters.keys())
    assert "noreturn" in params, "Missing parameter 'noreturn'"
    assert "inline" in params, "Missing parameter 'inline'"

def test_mydsl_function_specifier_has_noreturn():
    assert hasattr(myDsl_function_specifier, "noreturn")
    descriptor = None
    for klass in myDsl_function_specifier.__mro__:
        if "noreturn" in klass.__dict__:
            descriptor = klass.__dict__["noreturn"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_function_specifier_has_inline():
    assert hasattr(myDsl_function_specifier, "inline")
    descriptor = None
    for klass in myDsl_function_specifier.__mro__:
        if "inline" in klass.__dict__:
            descriptor = klass.__dict__["inline"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_type_qualifier_is_not_abstract():
    assert not inspect.isabstract(myDsl_type_qualifier)


def test_mydsl_type_qualifier_constructor_exists():
    assert callable(myDsl_type_qualifier.__init__)


def test_mydsl_type_qualifier_constructor_args():
    sig = inspect.signature(myDsl_type_qualifier.__init__)
    params = list(sig.parameters.keys())
    assert "const" in params, "Missing parameter 'const'"
    assert "volatile" in params, "Missing parameter 'volatile'"
    assert "restrict" in params, "Missing parameter 'restrict'"
    assert "atomic" in params, "Missing parameter 'atomic'"

def test_mydsl_type_qualifier_has_const():
    assert hasattr(myDsl_type_qualifier, "const")
    descriptor = None
    for klass in myDsl_type_qualifier.__mro__:
        if "const" in klass.__dict__:
            descriptor = klass.__dict__["const"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_type_qualifier_has_volatile():
    assert hasattr(myDsl_type_qualifier, "volatile")
    descriptor = None
    for klass in myDsl_type_qualifier.__mro__:
        if "volatile" in klass.__dict__:
            descriptor = klass.__dict__["volatile"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_type_qualifier_has_restrict():
    assert hasattr(myDsl_type_qualifier, "restrict")
    descriptor = None
    for klass in myDsl_type_qualifier.__mro__:
        if "restrict" in klass.__dict__:
            descriptor = klass.__dict__["restrict"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_type_qualifier_has_atomic():
    assert hasattr(myDsl_type_qualifier, "atomic")
    descriptor = None
    for klass in myDsl_type_qualifier.__mro__:
        if "atomic" in klass.__dict__:
            descriptor = klass.__dict__["atomic"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_type_specifier_is_not_abstract():
    assert not inspect.isabstract(myDsl_type_specifier)


def test_mydsl_type_specifier_constructor_exists():
    assert callable(myDsl_type_specifier.__init__)


def test_mydsl_type_specifier_constructor_args():
    sig = inspect.signature(myDsl_type_specifier.__init__)
    params = list(sig.parameters.keys())
    assert "typedef_name" in params, "Missing parameter 'typedef_name'"

def test_mydsl_type_specifier_has_typedef_name():
    assert hasattr(myDsl_type_specifier, "typedef_name")
    descriptor = None
    for klass in myDsl_type_specifier.__mro__:
        if "typedef_name" in klass.__dict__:
            descriptor = klass.__dict__["typedef_name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_storage_class_specifier_is_not_abstract():
    assert not inspect.isabstract(myDsl_storage_class_specifier)


def test_mydsl_storage_class_specifier_constructor_exists():
    assert callable(myDsl_storage_class_specifier.__init__)


def test_mydsl_storage_class_specifier_constructor_args():
    sig = inspect.signature(myDsl_storage_class_specifier.__init__)
    params = list(sig.parameters.keys())
    assert "thread_local" in params, "Missing parameter 'thread_local'"
    assert "auto" in params, "Missing parameter 'auto'"
    assert "typedef" in params, "Missing parameter 'typedef'"
    assert "static" in params, "Missing parameter 'static'"
    assert "register" in params, "Missing parameter 'register'"
    assert "extern" in params, "Missing parameter 'extern'"

def test_mydsl_storage_class_specifier_has_thread_local():
    assert hasattr(myDsl_storage_class_specifier, "thread_local")
    descriptor = None
    for klass in myDsl_storage_class_specifier.__mro__:
        if "thread_local" in klass.__dict__:
            descriptor = klass.__dict__["thread_local"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_storage_class_specifier_has_auto():
    assert hasattr(myDsl_storage_class_specifier, "auto")
    descriptor = None
    for klass in myDsl_storage_class_specifier.__mro__:
        if "auto" in klass.__dict__:
            descriptor = klass.__dict__["auto"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_storage_class_specifier_has_typedef():
    assert hasattr(myDsl_storage_class_specifier, "typedef")
    descriptor = None
    for klass in myDsl_storage_class_specifier.__mro__:
        if "typedef" in klass.__dict__:
            descriptor = klass.__dict__["typedef"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_storage_class_specifier_has_static():
    assert hasattr(myDsl_storage_class_specifier, "static")
    descriptor = None
    for klass in myDsl_storage_class_specifier.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_storage_class_specifier_has_register():
    assert hasattr(myDsl_storage_class_specifier, "register")
    descriptor = None
    for klass in myDsl_storage_class_specifier.__mro__:
        if "register" in klass.__dict__:
            descriptor = klass.__dict__["register"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_storage_class_specifier_has_extern():
    assert hasattr(myDsl_storage_class_specifier, "extern")
    descriptor = None
    for klass in myDsl_storage_class_specifier.__mro__:
        if "extern" in klass.__dict__:
            descriptor = klass.__dict__["extern"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_static_assert_declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl_static_assert_declaration)


def test_mydsl_static_assert_declaration_constructor_exists():
    assert callable(myDsl_static_assert_declaration.__init__)


def test_mydsl_static_assert_declaration_constructor_args():
    sig = inspect.signature(myDsl_static_assert_declaration.__init__)
    params = list(sig.parameters.keys())
    assert "static_assert" in params, "Missing parameter 'static_assert'"
    assert "string_literal" in params, "Missing parameter 'string_literal'"

def test_mydsl_static_assert_declaration_has_static_assert():
    assert hasattr(myDsl_static_assert_declaration, "static_assert")
    descriptor = None
    for klass in myDsl_static_assert_declaration.__mro__:
        if "static_assert" in klass.__dict__:
            descriptor = klass.__dict__["static_assert"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_static_assert_declaration_has_string_literal():
    assert hasattr(myDsl_static_assert_declaration, "string_literal")
    descriptor = None
    for klass in myDsl_static_assert_declaration.__mro__:
        if "string_literal" in klass.__dict__:
            descriptor = klass.__dict__["string_literal"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_init_declarator_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_init_declarator_list)


def test_mydsl_init_declarator_list_constructor_exists():
    assert callable(myDsl_init_declarator_list.__init__)


def test_mydsl_init_declarator_list_constructor_args():
    sig = inspect.signature(myDsl_init_declarator_list.__init__)
    params = list(sig.parameters.keys())



def test_simple_expression_is_not_abstract():
    assert not inspect.isabstract(simple_expression)


def test_simple_expression_constructor_exists():
    assert callable(simple_expression.__init__)


def test_simple_expression_constructor_args():
    sig = inspect.signature(simple_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_variableref_is_not_abstract():
    assert not inspect.isabstract(myDsl_variableRef)


def test_mydsl_variableref_constructor_exists():
    assert callable(myDsl_variableRef.__init__)


def test_mydsl_variableref_constructor_args():
    sig = inspect.signature(myDsl_variableRef.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_mydsl_variableref_has_variable():
    assert hasattr(myDsl_variableRef, "variable")
    descriptor = None
    for klass in myDsl_variableRef.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_minus_is_not_abstract():
    assert not inspect.isabstract(myDsl_MINUS)


def test_mydsl_minus_constructor_exists():
    assert callable(myDsl_MINUS.__init__)


def test_mydsl_minus_constructor_args():
    sig = inspect.signature(myDsl_MINUS.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_inttype_is_not_abstract():
    assert not inspect.isabstract(myDsl_intType)


def test_mydsl_inttype_constructor_exists():
    assert callable(myDsl_intType.__init__)


def test_mydsl_inttype_constructor_args():
    sig = inspect.signature(myDsl_intType.__init__)
    params = list(sig.parameters.keys())
    assert "int_type" in params, "Missing parameter 'int_type'"
    assert "value" in params, "Missing parameter 'value'"

def test_mydsl_inttype_has_int_type():
    assert hasattr(myDsl_intType, "int_type")
    descriptor = None
    for klass in myDsl_intType.__mro__:
        if "int_type" in klass.__dict__:
            descriptor = klass.__dict__["int_type"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_inttype_has_value():
    assert hasattr(myDsl_intType, "value")
    descriptor = None
    for klass in myDsl_intType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_floattype_is_not_abstract():
    assert not inspect.isabstract(myDsl_floatType)


def test_mydsl_floattype_constructor_exists():
    assert callable(myDsl_floatType.__init__)


def test_mydsl_floattype_constructor_args():
    sig = inspect.signature(myDsl_floatType.__init__)
    params = list(sig.parameters.keys())
    assert "float_type" in params, "Missing parameter 'float_type'"
    assert "value" in params, "Missing parameter 'value'"

def test_mydsl_floattype_has_float_type():
    assert hasattr(myDsl_floatType, "float_type")
    descriptor = None
    for klass in myDsl_floatType.__mro__:
        if "float_type" in klass.__dict__:
            descriptor = klass.__dict__["float_type"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_floattype_has_value():
    assert hasattr(myDsl_floatType, "value")
    descriptor = None
    for klass in myDsl_floatType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_add_is_not_abstract():
    assert not inspect.isabstract(myDsl_ADD)


def test_mydsl_add_constructor_exists():
    assert callable(myDsl_ADD.__init__)


def test_mydsl_add_constructor_args():
    sig = inspect.signature(myDsl_ADD.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_unary_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_unary_expression)


def test_mydsl_unary_expression_constructor_exists():
    assert callable(myDsl_unary_expression.__init__)


def test_mydsl_unary_expression_constructor_args():
    sig = inspect.signature(myDsl_unary_expression.__init__)
    params = list(sig.parameters.keys())
    assert "dec_op" in params, "Missing parameter 'dec_op'"
    assert "sizeof" in params, "Missing parameter 'sizeof'"
    assert "unary_operator" in params, "Missing parameter 'unary_operator'"
    assert "alignof" in params, "Missing parameter 'alignof'"
    assert "inc_op" in params, "Missing parameter 'inc_op'"

def test_mydsl_unary_expression_has_dec_op():
    assert hasattr(myDsl_unary_expression, "dec_op")
    descriptor = None
    for klass in myDsl_unary_expression.__mro__:
        if "dec_op" in klass.__dict__:
            descriptor = klass.__dict__["dec_op"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_unary_expression_has_sizeof():
    assert hasattr(myDsl_unary_expression, "sizeof")
    descriptor = None
    for klass in myDsl_unary_expression.__mro__:
        if "sizeof" in klass.__dict__:
            descriptor = klass.__dict__["sizeof"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_unary_expression_has_unary_operator():
    assert hasattr(myDsl_unary_expression, "unary_operator")
    descriptor = None
    for klass in myDsl_unary_expression.__mro__:
        if "unary_operator" in klass.__dict__:
            descriptor = klass.__dict__["unary_operator"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_unary_expression_has_alignof():
    assert hasattr(myDsl_unary_expression, "alignof")
    descriptor = None
    for klass in myDsl_unary_expression.__mro__:
        if "alignof" in klass.__dict__:
            descriptor = klass.__dict__["alignof"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_unary_expression_has_inc_op():
    assert hasattr(myDsl_unary_expression, "inc_op")
    descriptor = None
    for klass in myDsl_unary_expression.__mro__:
        if "inc_op" in klass.__dict__:
            descriptor = klass.__dict__["inc_op"]
            break
    assert isinstance(descriptor, property)



def test_postfix_expression2_is_not_abstract():
    assert not inspect.isabstract(postfix_expression2)


def test_postfix_expression2_constructor_exists():
    assert callable(postfix_expression2.__init__)


def test_postfix_expression2_constructor_args():
    sig = inspect.signature(postfix_expression2.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_argument_expression_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_argument_expression_list)


def test_mydsl_argument_expression_list_constructor_exists():
    assert callable(myDsl_argument_expression_list.__init__)


def test_mydsl_argument_expression_list_constructor_args():
    sig = inspect.signature(myDsl_argument_expression_list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_initializer_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_initializer_list)


def test_mydsl_initializer_list_constructor_exists():
    assert callable(myDsl_initializer_list.__init__)


def test_mydsl_initializer_list_constructor_args():
    sig = inspect.signature(myDsl_initializer_list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_postfix_expression2_is_not_abstract():
    assert not inspect.isabstract(myDsl_postfix_expression2)


def test_mydsl_postfix_expression2_constructor_exists():
    assert callable(myDsl_postfix_expression2.__init__)


def test_mydsl_postfix_expression2_constructor_args():
    sig = inspect.signature(myDsl_postfix_expression2.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_postfix_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_postfix_expression)


def test_mydsl_postfix_expression_constructor_exists():
    assert callable(myDsl_postfix_expression.__init__)


def test_mydsl_postfix_expression_constructor_args():
    sig = inspect.signature(myDsl_postfix_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_generic_association_is_not_abstract():
    assert not inspect.isabstract(myDsl_generic_association)


def test_mydsl_generic_association_constructor_exists():
    assert callable(myDsl_generic_association.__init__)


def test_mydsl_generic_association_constructor_args():
    sig = inspect.signature(myDsl_generic_association.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_mydsl_generic_association_has_default():
    assert hasattr(myDsl_generic_association, "default")
    descriptor = None
    for klass in myDsl_generic_association.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_generic_assoc_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_generic_assoc_list)


def test_mydsl_generic_assoc_list_constructor_exists():
    assert callable(myDsl_generic_assoc_list.__init__)


def test_mydsl_generic_assoc_list_constructor_args():
    sig = inspect.signature(myDsl_generic_assoc_list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_assignment_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_assignment_expression)


def test_mydsl_assignment_expression_constructor_exists():
    assert callable(myDsl_assignment_expression.__init__)


def test_mydsl_assignment_expression_constructor_args():
    sig = inspect.signature(myDsl_assignment_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_expression)


def test_mydsl_expression_constructor_exists():
    assert callable(myDsl_expression.__init__)


def test_mydsl_expression_constructor_args():
    sig = inspect.signature(myDsl_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_conditional_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_conditional_expression)


def test_mydsl_conditional_expression_constructor_exists():
    assert callable(myDsl_conditional_expression.__init__)


def test_mydsl_conditional_expression_constructor_args():
    sig = inspect.signature(myDsl_conditional_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_constant_is_not_abstract():
    assert not inspect.isabstract(myDsl_constant)


def test_mydsl_constant_constructor_exists():
    assert callable(myDsl_constant.__init__)


def test_mydsl_constant_constructor_args():
    sig = inspect.signature(myDsl_constant.__init__)
    params = list(sig.parameters.keys())
    assert "f_constant" in params, "Missing parameter 'f_constant'"
    assert "i_constant" in params, "Missing parameter 'i_constant'"
    assert "enumt" in params, "Missing parameter 'enumt'"

def test_mydsl_constant_has_f_constant():
    assert hasattr(myDsl_constant, "f_constant")
    descriptor = None
    for klass in myDsl_constant.__mro__:
        if "f_constant" in klass.__dict__:
            descriptor = klass.__dict__["f_constant"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_constant_has_i_constant():
    assert hasattr(myDsl_constant, "i_constant")
    descriptor = None
    for klass in myDsl_constant.__mro__:
        if "i_constant" in klass.__dict__:
            descriptor = klass.__dict__["i_constant"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_constant_has_enumt():
    assert hasattr(myDsl_constant, "enumt")
    descriptor = None
    for klass in myDsl_constant.__mro__:
        if "enumt" in klass.__dict__:
            descriptor = klass.__dict__["enumt"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_type_name_is_not_abstract():
    assert not inspect.isabstract(myDsl_type_name)


def test_mydsl_type_name_constructor_exists():
    assert callable(myDsl_type_name.__init__)


def test_mydsl_type_name_constructor_args():
    sig = inspect.signature(myDsl_type_name.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_simple_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_simple_expression)


def test_mydsl_simple_expression_constructor_exists():
    assert callable(myDsl_simple_expression.__init__)


def test_mydsl_simple_expression_constructor_args():
    sig = inspect.signature(myDsl_simple_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_translation_unit_is_not_abstract():
    assert not inspect.isabstract(myDsl_translation_unit)


def test_mydsl_translation_unit_constructor_exists():
    assert callable(myDsl_translation_unit.__init__)


def test_mydsl_translation_unit_constructor_args():
    sig = inspect.signature(myDsl_translation_unit.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_model_is_not_abstract():
    assert not inspect.isabstract(myDsl_Model)


def test_mydsl_model_constructor_exists():
    assert callable(myDsl_Model.__init__)


def test_mydsl_model_constructor_args():
    sig = inspect.signature(myDsl_Model.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_generic_selection_is_not_abstract():
    assert not inspect.isabstract(myDsl_generic_selection)


def test_mydsl_generic_selection_constructor_exists():
    assert callable(myDsl_generic_selection.__init__)


def test_mydsl_generic_selection_constructor_args():
    sig = inspect.signature(myDsl_generic_selection.__init__)
    params = list(sig.parameters.keys())
    assert "generic" in params, "Missing parameter 'generic'"

def test_mydsl_generic_selection_has_generic():
    assert hasattr(myDsl_generic_selection, "generic")
    descriptor = None
    for klass in myDsl_generic_selection.__mro__:
        if "generic" in klass.__dict__:
            descriptor = klass.__dict__["generic"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_string_nova_is_not_abstract():
    assert not inspect.isabstract(myDsl_string_nova)


def test_mydsl_string_nova_constructor_exists():
    assert callable(myDsl_string_nova.__init__)


def test_mydsl_string_nova_constructor_args():
    sig = inspect.signature(myDsl_string_nova.__init__)
    params = list(sig.parameters.keys())
    assert "func_name" in params, "Missing parameter 'func_name'"
    assert "string_literal" in params, "Missing parameter 'string_literal'"

def test_mydsl_string_nova_has_func_name():
    assert hasattr(myDsl_string_nova, "func_name")
    descriptor = None
    for klass in myDsl_string_nova.__mro__:
        if "func_name" in klass.__dict__:
            descriptor = klass.__dict__["func_name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_string_nova_has_string_literal():
    assert hasattr(myDsl_string_nova, "string_literal")
    descriptor = None
    for klass in myDsl_string_nova.__mro__:
        if "string_literal" in klass.__dict__:
            descriptor = klass.__dict__["string_literal"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_enumeration_constant_is_not_abstract():
    assert not inspect.isabstract(myDsl_enumeration_constant)


def test_mydsl_enumeration_constant_constructor_exists():
    assert callable(myDsl_enumeration_constant.__init__)


def test_mydsl_enumeration_constant_constructor_args():
    sig = inspect.signature(myDsl_enumeration_constant.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_mydsl_enumeration_constant_has_identifier():
    assert hasattr(myDsl_enumeration_constant, "identifier")
    descriptor = None
    for klass in myDsl_enumeration_constant.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_unsignedtype_is_not_abstract():
    assert not inspect.isabstract(myDsl_unsignedType)


def test_mydsl_unsignedtype_constructor_exists():
    assert callable(myDsl_unsignedType.__init__)


def test_mydsl_unsignedtype_constructor_args():
    sig = inspect.signature(myDsl_unsignedType.__init__)
    params = list(sig.parameters.keys())
    assert "unsigned_type" in params, "Missing parameter 'unsigned_type'"

def test_mydsl_unsignedtype_has_unsigned_type():
    assert hasattr(myDsl_unsignedType, "unsigned_type")
    descriptor = None
    for klass in myDsl_unsignedType.__mro__:
        if "unsigned_type" in klass.__dict__:
            descriptor = klass.__dict__["unsigned_type"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_signedtype_is_not_abstract():
    assert not inspect.isabstract(myDsl_signedType)


def test_mydsl_signedtype_constructor_exists():
    assert callable(myDsl_signedType.__init__)


def test_mydsl_signedtype_constructor_args():
    sig = inspect.signature(myDsl_signedType.__init__)
    params = list(sig.parameters.keys())
    assert "signed_type" in params, "Missing parameter 'signed_type'"

def test_mydsl_signedtype_has_signed_type():
    assert hasattr(myDsl_signedType, "signed_type")
    descriptor = None
    for klass in myDsl_signedType.__mro__:
        if "signed_type" in klass.__dict__:
            descriptor = klass.__dict__["signed_type"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_doubletype_is_not_abstract():
    assert not inspect.isabstract(myDsl_doubleType)


def test_mydsl_doubletype_constructor_exists():
    assert callable(myDsl_doubleType.__init__)


def test_mydsl_doubletype_constructor_args():
    sig = inspect.signature(myDsl_doubleType.__init__)
    params = list(sig.parameters.keys())
    assert "double_type" in params, "Missing parameter 'double_type'"

def test_mydsl_doubletype_has_double_type():
    assert hasattr(myDsl_doubleType, "double_type")
    descriptor = None
    for klass in myDsl_doubleType.__mro__:
        if "double_type" in klass.__dict__:
            descriptor = klass.__dict__["double_type"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_longtype_is_not_abstract():
    assert not inspect.isabstract(myDsl_longType)


def test_mydsl_longtype_constructor_exists():
    assert callable(myDsl_longType.__init__)


def test_mydsl_longtype_constructor_args():
    sig = inspect.signature(myDsl_longType.__init__)
    params = list(sig.parameters.keys())
    assert "long_type" in params, "Missing parameter 'long_type'"

def test_mydsl_longtype_has_long_type():
    assert hasattr(myDsl_longType, "long_type")
    descriptor = None
    for klass in myDsl_longType.__mro__:
        if "long_type" in klass.__dict__:
            descriptor = klass.__dict__["long_type"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_shorttype_is_not_abstract():
    assert not inspect.isabstract(myDsl_shortType)


def test_mydsl_shorttype_constructor_exists():
    assert callable(myDsl_shortType.__init__)


def test_mydsl_shorttype_constructor_args():
    sig = inspect.signature(myDsl_shortType.__init__)
    params = list(sig.parameters.keys())
    assert "short_type" in params, "Missing parameter 'short_type'"

def test_mydsl_shorttype_has_short_type():
    assert hasattr(myDsl_shortType, "short_type")
    descriptor = None
    for klass in myDsl_shortType.__mro__:
        if "short_type" in klass.__dict__:
            descriptor = klass.__dict__["short_type"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_chartype_is_not_abstract():
    assert not inspect.isabstract(myDsl_charType)


def test_mydsl_chartype_constructor_exists():
    assert callable(myDsl_charType.__init__)


def test_mydsl_chartype_constructor_args():
    sig = inspect.signature(myDsl_charType.__init__)
    params = list(sig.parameters.keys())
    assert "char_type" in params, "Missing parameter 'char_type'"

def test_mydsl_chartype_has_char_type():
    assert hasattr(myDsl_charType, "char_type")
    descriptor = None
    for klass in myDsl_charType.__mro__:
        if "char_type" in klass.__dict__:
            descriptor = klass.__dict__["char_type"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_voidtype_is_not_abstract():
    assert not inspect.isabstract(myDsl_voidType)


def test_mydsl_voidtype_constructor_exists():
    assert callable(myDsl_voidType.__init__)


def test_mydsl_voidtype_constructor_args():
    sig = inspect.signature(myDsl_voidType.__init__)
    params = list(sig.parameters.keys())
    assert "void_type" in params, "Missing parameter 'void_type'"

def test_mydsl_voidtype_has_void_type():
    assert hasattr(myDsl_voidType, "void_type")
    descriptor = None
    for klass in myDsl_voidType.__mro__:
        if "void_type" in klass.__dict__:
            descriptor = klass.__dict__["void_type"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_log_or_is_not_abstract():
    assert not inspect.isabstract(myDsl_LOG_OR)


def test_mydsl_log_or_constructor_exists():
    assert callable(myDsl_LOG_OR.__init__)


def test_mydsl_log_or_constructor_args():
    sig = inspect.signature(myDsl_LOG_OR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_imaginarytype_is_not_abstract():
    assert not inspect.isabstract(myDsl_imaginaryType)


def test_mydsl_imaginarytype_constructor_exists():
    assert callable(myDsl_imaginaryType.__init__)


def test_mydsl_imaginarytype_constructor_args():
    sig = inspect.signature(myDsl_imaginaryType.__init__)
    params = list(sig.parameters.keys())
    assert "imaginary_type" in params, "Missing parameter 'imaginary_type'"

def test_mydsl_imaginarytype_has_imaginary_type():
    assert hasattr(myDsl_imaginaryType, "imaginary_type")
    descriptor = None
    for klass in myDsl_imaginaryType.__mro__:
        if "imaginary_type" in klass.__dict__:
            descriptor = klass.__dict__["imaginary_type"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_complextype_is_not_abstract():
    assert not inspect.isabstract(myDsl_complexType)


def test_mydsl_complextype_constructor_exists():
    assert callable(myDsl_complexType.__init__)


def test_mydsl_complextype_constructor_args():
    sig = inspect.signature(myDsl_complexType.__init__)
    params = list(sig.parameters.keys())
    assert "complex_type" in params, "Missing parameter 'complex_type'"

def test_mydsl_complextype_has_complex_type():
    assert hasattr(myDsl_complexType, "complex_type")
    descriptor = None
    for klass in myDsl_complexType.__mro__:
        if "complex_type" in klass.__dict__:
            descriptor = klass.__dict__["complex_type"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_and_is_not_abstract():
    assert not inspect.isabstract(myDsl_AND)


def test_mydsl_and_constructor_exists():
    assert callable(myDsl_AND.__init__)


def test_mydsl_and_constructor_args():
    sig = inspect.signature(myDsl_AND.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_eql_is_not_abstract():
    assert not inspect.isabstract(myDsl_EQL)


def test_mydsl_eql_constructor_exists():
    assert callable(myDsl_EQL.__init__)


def test_mydsl_eql_constructor_args():
    sig = inspect.signature(myDsl_EQL.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_mydsl_eql_has_op():
    assert hasattr(myDsl_EQL, "op")
    descriptor = None
    for klass in myDsl_EQL.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_rel_is_not_abstract():
    assert not inspect.isabstract(myDsl_REL)


def test_mydsl_rel_constructor_exists():
    assert callable(myDsl_REL.__init__)


def test_mydsl_rel_constructor_args():
    sig = inspect.signature(myDsl_REL.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_mydsl_rel_has_op():
    assert hasattr(myDsl_REL, "op")
    descriptor = None
    for klass in myDsl_REL.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_shf_is_not_abstract():
    assert not inspect.isabstract(myDsl_SHF)


def test_mydsl_shf_constructor_exists():
    assert callable(myDsl_SHF.__init__)


def test_mydsl_shf_constructor_args():
    sig = inspect.signature(myDsl_SHF.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_mydsl_shf_has_op():
    assert hasattr(myDsl_SHF, "op")
    descriptor = None
    for klass in myDsl_SHF.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_log_and_is_not_abstract():
    assert not inspect.isabstract(myDsl_LOG_AND)


def test_mydsl_log_and_constructor_exists():
    assert callable(myDsl_LOG_AND.__init__)


def test_mydsl_log_and_constructor_args():
    sig = inspect.signature(myDsl_LOG_AND.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_inc_or_is_not_abstract():
    assert not inspect.isabstract(myDsl_INC_OR)


def test_mydsl_inc_or_constructor_exists():
    assert callable(myDsl_INC_OR.__init__)


def test_mydsl_inc_or_constructor_args():
    sig = inspect.signature(myDsl_INC_OR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_mul_is_not_abstract():
    assert not inspect.isabstract(myDsl_MUL)


def test_mydsl_mul_constructor_exists():
    assert callable(myDsl_MUL.__init__)


def test_mydsl_mul_constructor_args():
    sig = inspect.signature(myDsl_MUL.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_mydsl_mul_has_op():
    assert hasattr(myDsl_MUL, "op")
    descriptor = None
    for klass in myDsl_MUL.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_exc_or_is_not_abstract():
    assert not inspect.isabstract(myDsl_EXC_OR)


def test_mydsl_exc_or_constructor_exists():
    assert callable(myDsl_EXC_OR.__init__)


def test_mydsl_exc_or_constructor_args():
    sig = inspect.signature(myDsl_EXC_OR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_booleantype_is_not_abstract():
    assert not inspect.isabstract(myDsl_booleanType)


def test_mydsl_booleantype_constructor_exists():
    assert callable(myDsl_booleanType.__init__)


def test_mydsl_booleantype_constructor_args():
    sig = inspect.signature(myDsl_booleanType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "bool_type" in params, "Missing parameter 'bool_type'"

def test_mydsl_booleantype_has_value():
    assert hasattr(myDsl_booleanType, "value")
    descriptor = None
    for klass in myDsl_booleanType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_booleantype_has_bool_type():
    assert hasattr(myDsl_booleanType, "bool_type")
    descriptor = None
    for klass in myDsl_booleanType.__mro__:
        if "bool_type" in klass.__dict__:
            descriptor = klass.__dict__["bool_type"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_stringtype_is_not_abstract():
    assert not inspect.isabstract(myDsl_stringType)


def test_mydsl_stringtype_constructor_exists():
    assert callable(myDsl_stringType.__init__)


def test_mydsl_stringtype_constructor_args():
    sig = inspect.signature(myDsl_stringType.__init__)
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
type_specifier_strategy = st.builds(
    type_specifier,
)
myDsl_declaration_list2_strategy = st.builds(
    myDsl_declaration_list2,
)
myDsl_external_declaration_strategy = st.builds(
    myDsl_external_declaration,
)
myDsl_EObject_strategy = st.builds(
    myDsl_EObject,
)
myDsl_declaration_list_strategy = st.builds(
    myDsl_declaration_list,
)
myDsl_function_definition_strategy = st.builds(
    myDsl_function_definition,
)
myDsl_jump_statement_strategy = st.builds(
    myDsl_jump_statement,
    return_=
        safe_text,
    identifier=
        safe_text,
    continue_=
        safe_text,
    goto=
        safe_text,
    break_=
        safe_text
)
myDsl_iteration_statement_strategy = st.builds(
    myDsl_iteration_statement,
    while_=
        safe_text,
    for_=
        safe_text,
    do=
        safe_text
)
myDsl_selection_statement_strategy = st.builds(
    myDsl_selection_statement,
    else_=
        safe_text,
    if_=
        safe_text,
    switch=
        safe_text
)
myDsl_expression_statement_strategy = st.builds(
    myDsl_expression_statement,
)
myDsl_compound_statement_strategy = st.builds(
    myDsl_compound_statement,
)
myDsl_labeled_statement_strategy = st.builds(
    myDsl_labeled_statement,
    identifier=
        safe_text,
    default=
        safe_text,
    case=
        safe_text
)
myDsl_statement_strategy = st.builds(
    myDsl_statement,
)
myDsl_block_item_strategy = st.builds(
    myDsl_block_item,
)
myDsl_initializer_list2_strategy = st.builds(
    myDsl_initializer_list2,
)
myDsl_designation_strategy = st.builds(
    myDsl_designation,
)
myDsl_initializer_strategy = st.builds(
    myDsl_initializer,
)
myDsl_direct_abstract_declarator2_strategy = st.builds(
    myDsl_direct_abstract_declarator2,
    static=
        safe_text
)
myDsl_direct_abstract_declarator_strategy = st.builds(
    myDsl_direct_abstract_declarator,
)
myDsl_designator_list2_strategy = st.builds(
    myDsl_designator_list2,
)
myDsl_designator_strategy = st.builds(
    myDsl_designator,
    identifier=
        safe_text
)
myDsl_designator_list_strategy = st.builds(
    myDsl_designator_list,
)
myDsl_parameter_list2_strategy = st.builds(
    myDsl_parameter_list2,
)
myDsl_parameter_declaration_strategy = st.builds(
    myDsl_parameter_declaration,
)
myDsl_parameter_list_strategy = st.builds(
    myDsl_parameter_list,
)
myDsl_type_qualifier_list2_strategy = st.builds(
    myDsl_type_qualifier_list2,
)
myDsl_identifier_list2_strategy = st.builds(
    myDsl_identifier_list2,
    identifier=
        safe_text
)
myDsl_abstract_declarator_strategy = st.builds(
    myDsl_abstract_declarator,
)
myDsl_direct_declarator_strategy = st.builds(
    myDsl_direct_declarator,
    name=
        safe_text
)
myDsl_pointer_strategy = st.builds(
    myDsl_pointer,
)
myDsl_identifier_list_strategy = st.builds(
    myDsl_identifier_list,
    identifier=
        safe_text
)
myDsl_parameter_type_list_strategy = st.builds(
    myDsl_parameter_type_list,
    ellipsis=
        safe_text
)
myDsl_type_qualifier_list_strategy = st.builds(
    myDsl_type_qualifier_list,
)
myDsl_direct_declarator2_strategy = st.builds(
    myDsl_direct_declarator2,
    static=
        safe_text
)
myDsl_struct_declarator_list2_strategy = st.builds(
    myDsl_struct_declarator_list2,
)
myDsl_struct_declarator_strategy = st.builds(
    myDsl_struct_declarator,
)
myDsl_struct_declarator_list_strategy = st.builds(
    myDsl_struct_declarator_list,
)
myDsl_specifier_qualifier_list_strategy = st.builds(
    myDsl_specifier_qualifier_list,
)
myDsl_enumerator_list2_strategy = st.builds(
    myDsl_enumerator_list2,
)
myDsl_enumerator_strategy = st.builds(
    myDsl_enumerator,
)
myDsl_enumerator_list_strategy = st.builds(
    myDsl_enumerator_list,
)
myDsl_atomic_type_specifier_strategy = st.builds(
    myDsl_atomic_type_specifier,
    atomic=
        safe_text
)
myDsl_declarator_strategy = st.builds(
    myDsl_declarator,
)
myDsl_init_declarator_list2_strategy = st.builds(
    myDsl_init_declarator_list2,
)
myDsl_init_declarator_strategy = st.builds(
    myDsl_init_declarator,
)
myDsl_alignment_specifier_strategy = st.builds(
    myDsl_alignment_specifier,
    alignas=
        safe_text
)
myDsl_struct_declaration_list2_strategy = st.builds(
    myDsl_struct_declaration_list2,
)
myDsl_struct_declaration_strategy = st.builds(
    myDsl_struct_declaration,
)
struct_or_union_specifier_strategy = st.builds(
    struct_or_union_specifier,
)
myDsl_struct_declaration_list_strategy = st.builds(
    myDsl_struct_declaration_list,
)
myDsl_struct_or_union_strategy = st.builds(
    myDsl_struct_or_union,
    union=
        safe_text,
    struct=
        safe_text
)
myDsl_enum_specifier_strategy = st.builds(
    myDsl_enum_specifier,
    identifier=
        safe_text,
    enumt=
        safe_text
)
myDsl_struct_or_union_specifier_strategy = st.builds(
    myDsl_struct_or_union_specifier,
    identifier=
        safe_text
)
myDsl_declaration_specifiers_strategy = st.builds(
    myDsl_declaration_specifiers,
)
myDsl_declaration_strategy = st.builds(
    myDsl_declaration,
)
myDsl_constant_expression_strategy = st.builds(
    myDsl_constant_expression,
)
myDsl_expression2_strategy = st.builds(
    myDsl_expression2,
)
myDsl_assignment_operator_strategy = st.builds(
    myDsl_assignment_operator,
    left_assign=
        safe_text,
    or_assign=
        safe_text,
    and_assign=
        safe_text,
    add_assign=
        safe_text,
    right_assign=
        safe_text,
    sub_assign=
        safe_text,
    mul_assign=
        safe_text,
    mod_assign=
        safe_text,
    xor_assign=
        safe_text,
    div_assign=
        safe_text
)
myDsl_function_specifier_strategy = st.builds(
    myDsl_function_specifier,
    noreturn=
        safe_text,
    inline=
        safe_text
)
myDsl_type_qualifier_strategy = st.builds(
    myDsl_type_qualifier,
    const=
        safe_text,
    volatile=
        safe_text,
    restrict=
        safe_text,
    atomic=
        safe_text
)
myDsl_type_specifier_strategy = st.builds(
    myDsl_type_specifier,
    typedef_name=
        safe_text
)
myDsl_storage_class_specifier_strategy = st.builds(
    myDsl_storage_class_specifier,
    thread_local=
        safe_text,
    auto=
        safe_text,
    typedef=
        safe_text,
    static=
        safe_text,
    register=
        safe_text,
    extern=
        safe_text
)
myDsl_static_assert_declaration_strategy = st.builds(
    myDsl_static_assert_declaration,
    static_assert=
        safe_text,
    string_literal=
        safe_text
)
myDsl_init_declarator_list_strategy = st.builds(
    myDsl_init_declarator_list,
)
simple_expression_strategy = st.builds(
    simple_expression,
)
myDsl_variableRef_strategy = st.builds(
    myDsl_variableRef,
    variable=
        safe_text
)
myDsl_MINUS_strategy = st.builds(
    myDsl_MINUS,
)
myDsl_intType_strategy = st.builds(
    myDsl_intType,
    int_type=
        safe_text,
    value=
        safe_text
)
myDsl_floatType_strategy = st.builds(
    myDsl_floatType,
    float_type=
        safe_text,
    value=
        safe_text
)
myDsl_ADD_strategy = st.builds(
    myDsl_ADD,
)
myDsl_unary_expression_strategy = st.builds(
    myDsl_unary_expression,
    dec_op=
        safe_text,
    sizeof=
        safe_text,
    unary_operator=
        safe_text,
    alignof=
        safe_text,
    inc_op=
        safe_text
)
postfix_expression2_strategy = st.builds(
    postfix_expression2,
)
myDsl_argument_expression_list_strategy = st.builds(
    myDsl_argument_expression_list,
)
myDsl_initializer_list_strategy = st.builds(
    myDsl_initializer_list,
)
myDsl_postfix_expression2_strategy = st.builds(
    myDsl_postfix_expression2,
)
myDsl_postfix_expression_strategy = st.builds(
    myDsl_postfix_expression,
)
myDsl_generic_association_strategy = st.builds(
    myDsl_generic_association,
    default=
        safe_text
)
myDsl_generic_assoc_list_strategy = st.builds(
    myDsl_generic_assoc_list,
)
myDsl_assignment_expression_strategy = st.builds(
    myDsl_assignment_expression,
)
myDsl_expression_strategy = st.builds(
    myDsl_expression,
)
myDsl_conditional_expression_strategy = st.builds(
    myDsl_conditional_expression,
)
myDsl_constant_strategy = st.builds(
    myDsl_constant,
    f_constant=
        safe_text,
    i_constant=
        safe_text,
    enumt=
        safe_text
)
myDsl_type_name_strategy = st.builds(
    myDsl_type_name,
)
myDsl_simple_expression_strategy = st.builds(
    myDsl_simple_expression,
)
myDsl_translation_unit_strategy = st.builds(
    myDsl_translation_unit,
)
myDsl_Model_strategy = st.builds(
    myDsl_Model,
)
myDsl_generic_selection_strategy = st.builds(
    myDsl_generic_selection,
    generic=
        safe_text
)
myDsl_string_nova_strategy = st.builds(
    myDsl_string_nova,
    func_name=
        safe_text,
    string_literal=
        safe_text
)
myDsl_enumeration_constant_strategy = st.builds(
    myDsl_enumeration_constant,
    identifier=
        safe_text
)
myDsl_unsignedType_strategy = st.builds(
    myDsl_unsignedType,
    unsigned_type=
        safe_text
)
myDsl_signedType_strategy = st.builds(
    myDsl_signedType,
    signed_type=
        safe_text
)
myDsl_doubleType_strategy = st.builds(
    myDsl_doubleType,
    double_type=
        safe_text
)
myDsl_longType_strategy = st.builds(
    myDsl_longType,
    long_type=
        safe_text
)
myDsl_shortType_strategy = st.builds(
    myDsl_shortType,
    short_type=
        safe_text
)
myDsl_charType_strategy = st.builds(
    myDsl_charType,
    char_type=
        safe_text
)
myDsl_voidType_strategy = st.builds(
    myDsl_voidType,
    void_type=
        safe_text
)
myDsl_LOG_OR_strategy = st.builds(
    myDsl_LOG_OR,
)
myDsl_imaginaryType_strategy = st.builds(
    myDsl_imaginaryType,
    imaginary_type=
        safe_text
)
myDsl_complexType_strategy = st.builds(
    myDsl_complexType,
    complex_type=
        safe_text
)
myDsl_AND_strategy = st.builds(
    myDsl_AND,
)
myDsl_EQL_strategy = st.builds(
    myDsl_EQL,
    op=
        safe_text
)
myDsl_REL_strategy = st.builds(
    myDsl_REL,
    op=
        safe_text
)
myDsl_SHF_strategy = st.builds(
    myDsl_SHF,
    op=
        safe_text
)
myDsl_LOG_AND_strategy = st.builds(
    myDsl_LOG_AND,
)
myDsl_INC_OR_strategy = st.builds(
    myDsl_INC_OR,
)
myDsl_MUL_strategy = st.builds(
    myDsl_MUL,
    op=
        safe_text
)
myDsl_EXC_OR_strategy = st.builds(
    myDsl_EXC_OR,
)
myDsl_booleanType_strategy = st.builds(
    myDsl_booleanType,
    value=
        safe_text,
    bool_type=
        safe_text
)
myDsl_stringType_strategy = st.builds(
    myDsl_stringType,
)

@given(instance=type_specifier_strategy)
@settings(max_examples=50)
def test_type_specifier_instantiation(instance):
    assert isinstance(instance, type_specifier)

@given(instance=myDsl_declaration_list2_strategy)
@settings(max_examples=50)
def test_mydsl_declaration_list2_instantiation(instance):
    assert isinstance(instance, myDsl_declaration_list2)

@given(instance=myDsl_external_declaration_strategy)
@settings(max_examples=50)
def test_mydsl_external_declaration_instantiation(instance):
    assert isinstance(instance, myDsl_external_declaration)

@given(instance=myDsl_EObject_strategy)
@settings(max_examples=50)
def test_mydsl_eobject_instantiation(instance):
    assert isinstance(instance, myDsl_EObject)

@given(instance=myDsl_declaration_list_strategy)
@settings(max_examples=50)
def test_mydsl_declaration_list_instantiation(instance):
    assert isinstance(instance, myDsl_declaration_list)

@given(instance=myDsl_function_definition_strategy)
@settings(max_examples=50)
def test_mydsl_function_definition_instantiation(instance):
    assert isinstance(instance, myDsl_function_definition)

@given(instance=myDsl_jump_statement_strategy)
@settings(max_examples=50)
def test_mydsl_jump_statement_instantiation(instance):
    assert isinstance(instance, myDsl_jump_statement)



@given(instance=myDsl_jump_statement_strategy)
def test_mydsl_jump_statement_return__setter(instance):
    original = instance.return_
    instance.return_ = original
    assert instance.return_ == original



@given(instance=myDsl_jump_statement_strategy)
def test_mydsl_jump_statement_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original



@given(instance=myDsl_jump_statement_strategy)
def test_mydsl_jump_statement_continue__setter(instance):
    original = instance.continue_
    instance.continue_ = original
    assert instance.continue_ == original



@given(instance=myDsl_jump_statement_strategy)
def test_mydsl_jump_statement_goto_setter(instance):
    original = instance.goto
    instance.goto = original
    assert instance.goto == original



@given(instance=myDsl_jump_statement_strategy)
def test_mydsl_jump_statement_break__setter(instance):
    original = instance.break_
    instance.break_ = original
    assert instance.break_ == original

@given(instance=myDsl_iteration_statement_strategy)
@settings(max_examples=50)
def test_mydsl_iteration_statement_instantiation(instance):
    assert isinstance(instance, myDsl_iteration_statement)



@given(instance=myDsl_iteration_statement_strategy)
def test_mydsl_iteration_statement_while__setter(instance):
    original = instance.while_
    instance.while_ = original
    assert instance.while_ == original



@given(instance=myDsl_iteration_statement_strategy)
def test_mydsl_iteration_statement_for__setter(instance):
    original = instance.for_
    instance.for_ = original
    assert instance.for_ == original



@given(instance=myDsl_iteration_statement_strategy)
def test_mydsl_iteration_statement_do_setter(instance):
    original = instance.do
    instance.do = original
    assert instance.do == original

@given(instance=myDsl_selection_statement_strategy)
@settings(max_examples=50)
def test_mydsl_selection_statement_instantiation(instance):
    assert isinstance(instance, myDsl_selection_statement)



@given(instance=myDsl_selection_statement_strategy)
def test_mydsl_selection_statement_else__setter(instance):
    original = instance.else_
    instance.else_ = original
    assert instance.else_ == original



@given(instance=myDsl_selection_statement_strategy)
def test_mydsl_selection_statement_if__setter(instance):
    original = instance.if_
    instance.if_ = original
    assert instance.if_ == original



@given(instance=myDsl_selection_statement_strategy)
def test_mydsl_selection_statement_switch_setter(instance):
    original = instance.switch
    instance.switch = original
    assert instance.switch == original

@given(instance=myDsl_expression_statement_strategy)
@settings(max_examples=50)
def test_mydsl_expression_statement_instantiation(instance):
    assert isinstance(instance, myDsl_expression_statement)

@given(instance=myDsl_compound_statement_strategy)
@settings(max_examples=50)
def test_mydsl_compound_statement_instantiation(instance):
    assert isinstance(instance, myDsl_compound_statement)

@given(instance=myDsl_labeled_statement_strategy)
@settings(max_examples=50)
def test_mydsl_labeled_statement_instantiation(instance):
    assert isinstance(instance, myDsl_labeled_statement)



@given(instance=myDsl_labeled_statement_strategy)
def test_mydsl_labeled_statement_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original



@given(instance=myDsl_labeled_statement_strategy)
def test_mydsl_labeled_statement_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=myDsl_labeled_statement_strategy)
def test_mydsl_labeled_statement_case_setter(instance):
    original = instance.case
    instance.case = original
    assert instance.case == original

@given(instance=myDsl_statement_strategy)
@settings(max_examples=50)
def test_mydsl_statement_instantiation(instance):
    assert isinstance(instance, myDsl_statement)

@given(instance=myDsl_block_item_strategy)
@settings(max_examples=50)
def test_mydsl_block_item_instantiation(instance):
    assert isinstance(instance, myDsl_block_item)

@given(instance=myDsl_initializer_list2_strategy)
@settings(max_examples=50)
def test_mydsl_initializer_list2_instantiation(instance):
    assert isinstance(instance, myDsl_initializer_list2)

@given(instance=myDsl_designation_strategy)
@settings(max_examples=50)
def test_mydsl_designation_instantiation(instance):
    assert isinstance(instance, myDsl_designation)

@given(instance=myDsl_initializer_strategy)
@settings(max_examples=50)
def test_mydsl_initializer_instantiation(instance):
    assert isinstance(instance, myDsl_initializer)

@given(instance=myDsl_direct_abstract_declarator2_strategy)
@settings(max_examples=50)
def test_mydsl_direct_abstract_declarator2_instantiation(instance):
    assert isinstance(instance, myDsl_direct_abstract_declarator2)



@given(instance=myDsl_direct_abstract_declarator2_strategy)
def test_mydsl_direct_abstract_declarator2_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=myDsl_direct_abstract_declarator_strategy)
@settings(max_examples=50)
def test_mydsl_direct_abstract_declarator_instantiation(instance):
    assert isinstance(instance, myDsl_direct_abstract_declarator)

@given(instance=myDsl_designator_list2_strategy)
@settings(max_examples=50)
def test_mydsl_designator_list2_instantiation(instance):
    assert isinstance(instance, myDsl_designator_list2)

@given(instance=myDsl_designator_strategy)
@settings(max_examples=50)
def test_mydsl_designator_instantiation(instance):
    assert isinstance(instance, myDsl_designator)



@given(instance=myDsl_designator_strategy)
def test_mydsl_designator_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=myDsl_designator_list_strategy)
@settings(max_examples=50)
def test_mydsl_designator_list_instantiation(instance):
    assert isinstance(instance, myDsl_designator_list)

@given(instance=myDsl_parameter_list2_strategy)
@settings(max_examples=50)
def test_mydsl_parameter_list2_instantiation(instance):
    assert isinstance(instance, myDsl_parameter_list2)

@given(instance=myDsl_parameter_declaration_strategy)
@settings(max_examples=50)
def test_mydsl_parameter_declaration_instantiation(instance):
    assert isinstance(instance, myDsl_parameter_declaration)

@given(instance=myDsl_parameter_list_strategy)
@settings(max_examples=50)
def test_mydsl_parameter_list_instantiation(instance):
    assert isinstance(instance, myDsl_parameter_list)

@given(instance=myDsl_type_qualifier_list2_strategy)
@settings(max_examples=50)
def test_mydsl_type_qualifier_list2_instantiation(instance):
    assert isinstance(instance, myDsl_type_qualifier_list2)

@given(instance=myDsl_identifier_list2_strategy)
@settings(max_examples=50)
def test_mydsl_identifier_list2_instantiation(instance):
    assert isinstance(instance, myDsl_identifier_list2)



@given(instance=myDsl_identifier_list2_strategy)
def test_mydsl_identifier_list2_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=myDsl_abstract_declarator_strategy)
@settings(max_examples=50)
def test_mydsl_abstract_declarator_instantiation(instance):
    assert isinstance(instance, myDsl_abstract_declarator)

@given(instance=myDsl_direct_declarator_strategy)
@settings(max_examples=50)
def test_mydsl_direct_declarator_instantiation(instance):
    assert isinstance(instance, myDsl_direct_declarator)



@given(instance=myDsl_direct_declarator_strategy)
def test_mydsl_direct_declarator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_pointer_strategy)
@settings(max_examples=50)
def test_mydsl_pointer_instantiation(instance):
    assert isinstance(instance, myDsl_pointer)

@given(instance=myDsl_identifier_list_strategy)
@settings(max_examples=50)
def test_mydsl_identifier_list_instantiation(instance):
    assert isinstance(instance, myDsl_identifier_list)



@given(instance=myDsl_identifier_list_strategy)
def test_mydsl_identifier_list_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=myDsl_parameter_type_list_strategy)
@settings(max_examples=50)
def test_mydsl_parameter_type_list_instantiation(instance):
    assert isinstance(instance, myDsl_parameter_type_list)



@given(instance=myDsl_parameter_type_list_strategy)
def test_mydsl_parameter_type_list_ellipsis_setter(instance):
    original = instance.ellipsis
    instance.ellipsis = original
    assert instance.ellipsis == original

@given(instance=myDsl_type_qualifier_list_strategy)
@settings(max_examples=50)
def test_mydsl_type_qualifier_list_instantiation(instance):
    assert isinstance(instance, myDsl_type_qualifier_list)

@given(instance=myDsl_direct_declarator2_strategy)
@settings(max_examples=50)
def test_mydsl_direct_declarator2_instantiation(instance):
    assert isinstance(instance, myDsl_direct_declarator2)



@given(instance=myDsl_direct_declarator2_strategy)
def test_mydsl_direct_declarator2_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=myDsl_struct_declarator_list2_strategy)
@settings(max_examples=50)
def test_mydsl_struct_declarator_list2_instantiation(instance):
    assert isinstance(instance, myDsl_struct_declarator_list2)

@given(instance=myDsl_struct_declarator_strategy)
@settings(max_examples=50)
def test_mydsl_struct_declarator_instantiation(instance):
    assert isinstance(instance, myDsl_struct_declarator)

@given(instance=myDsl_struct_declarator_list_strategy)
@settings(max_examples=50)
def test_mydsl_struct_declarator_list_instantiation(instance):
    assert isinstance(instance, myDsl_struct_declarator_list)

@given(instance=myDsl_specifier_qualifier_list_strategy)
@settings(max_examples=50)
def test_mydsl_specifier_qualifier_list_instantiation(instance):
    assert isinstance(instance, myDsl_specifier_qualifier_list)

@given(instance=myDsl_enumerator_list2_strategy)
@settings(max_examples=50)
def test_mydsl_enumerator_list2_instantiation(instance):
    assert isinstance(instance, myDsl_enumerator_list2)

@given(instance=myDsl_enumerator_strategy)
@settings(max_examples=50)
def test_mydsl_enumerator_instantiation(instance):
    assert isinstance(instance, myDsl_enumerator)

@given(instance=myDsl_enumerator_list_strategy)
@settings(max_examples=50)
def test_mydsl_enumerator_list_instantiation(instance):
    assert isinstance(instance, myDsl_enumerator_list)

@given(instance=myDsl_atomic_type_specifier_strategy)
@settings(max_examples=50)
def test_mydsl_atomic_type_specifier_instantiation(instance):
    assert isinstance(instance, myDsl_atomic_type_specifier)



@given(instance=myDsl_atomic_type_specifier_strategy)
def test_mydsl_atomic_type_specifier_atomic_setter(instance):
    original = instance.atomic
    instance.atomic = original
    assert instance.atomic == original

@given(instance=myDsl_declarator_strategy)
@settings(max_examples=50)
def test_mydsl_declarator_instantiation(instance):
    assert isinstance(instance, myDsl_declarator)

@given(instance=myDsl_init_declarator_list2_strategy)
@settings(max_examples=50)
def test_mydsl_init_declarator_list2_instantiation(instance):
    assert isinstance(instance, myDsl_init_declarator_list2)

@given(instance=myDsl_init_declarator_strategy)
@settings(max_examples=50)
def test_mydsl_init_declarator_instantiation(instance):
    assert isinstance(instance, myDsl_init_declarator)

@given(instance=myDsl_alignment_specifier_strategy)
@settings(max_examples=50)
def test_mydsl_alignment_specifier_instantiation(instance):
    assert isinstance(instance, myDsl_alignment_specifier)



@given(instance=myDsl_alignment_specifier_strategy)
def test_mydsl_alignment_specifier_alignas_setter(instance):
    original = instance.alignas
    instance.alignas = original
    assert instance.alignas == original

@given(instance=myDsl_struct_declaration_list2_strategy)
@settings(max_examples=50)
def test_mydsl_struct_declaration_list2_instantiation(instance):
    assert isinstance(instance, myDsl_struct_declaration_list2)

@given(instance=myDsl_struct_declaration_strategy)
@settings(max_examples=50)
def test_mydsl_struct_declaration_instantiation(instance):
    assert isinstance(instance, myDsl_struct_declaration)

@given(instance=struct_or_union_specifier_strategy)
@settings(max_examples=50)
def test_struct_or_union_specifier_instantiation(instance):
    assert isinstance(instance, struct_or_union_specifier)

@given(instance=myDsl_struct_declaration_list_strategy)
@settings(max_examples=50)
def test_mydsl_struct_declaration_list_instantiation(instance):
    assert isinstance(instance, myDsl_struct_declaration_list)

@given(instance=myDsl_struct_or_union_strategy)
@settings(max_examples=50)
def test_mydsl_struct_or_union_instantiation(instance):
    assert isinstance(instance, myDsl_struct_or_union)



@given(instance=myDsl_struct_or_union_strategy)
def test_mydsl_struct_or_union_union_setter(instance):
    original = instance.union
    instance.union = original
    assert instance.union == original



@given(instance=myDsl_struct_or_union_strategy)
def test_mydsl_struct_or_union_struct_setter(instance):
    original = instance.struct
    instance.struct = original
    assert instance.struct == original

@given(instance=myDsl_enum_specifier_strategy)
@settings(max_examples=50)
def test_mydsl_enum_specifier_instantiation(instance):
    assert isinstance(instance, myDsl_enum_specifier)



@given(instance=myDsl_enum_specifier_strategy)
def test_mydsl_enum_specifier_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original



@given(instance=myDsl_enum_specifier_strategy)
def test_mydsl_enum_specifier_enumt_setter(instance):
    original = instance.enumt
    instance.enumt = original
    assert instance.enumt == original

@given(instance=myDsl_struct_or_union_specifier_strategy)
@settings(max_examples=50)
def test_mydsl_struct_or_union_specifier_instantiation(instance):
    assert isinstance(instance, myDsl_struct_or_union_specifier)



@given(instance=myDsl_struct_or_union_specifier_strategy)
def test_mydsl_struct_or_union_specifier_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=myDsl_declaration_specifiers_strategy)
@settings(max_examples=50)
def test_mydsl_declaration_specifiers_instantiation(instance):
    assert isinstance(instance, myDsl_declaration_specifiers)

@given(instance=myDsl_declaration_strategy)
@settings(max_examples=50)
def test_mydsl_declaration_instantiation(instance):
    assert isinstance(instance, myDsl_declaration)

@given(instance=myDsl_constant_expression_strategy)
@settings(max_examples=50)
def test_mydsl_constant_expression_instantiation(instance):
    assert isinstance(instance, myDsl_constant_expression)

@given(instance=myDsl_expression2_strategy)
@settings(max_examples=50)
def test_mydsl_expression2_instantiation(instance):
    assert isinstance(instance, myDsl_expression2)

@given(instance=myDsl_assignment_operator_strategy)
@settings(max_examples=50)
def test_mydsl_assignment_operator_instantiation(instance):
    assert isinstance(instance, myDsl_assignment_operator)



@given(instance=myDsl_assignment_operator_strategy)
def test_mydsl_assignment_operator_left_assign_setter(instance):
    original = instance.left_assign
    instance.left_assign = original
    assert instance.left_assign == original



@given(instance=myDsl_assignment_operator_strategy)
def test_mydsl_assignment_operator_or_assign_setter(instance):
    original = instance.or_assign
    instance.or_assign = original
    assert instance.or_assign == original



@given(instance=myDsl_assignment_operator_strategy)
def test_mydsl_assignment_operator_and_assign_setter(instance):
    original = instance.and_assign
    instance.and_assign = original
    assert instance.and_assign == original



@given(instance=myDsl_assignment_operator_strategy)
def test_mydsl_assignment_operator_add_assign_setter(instance):
    original = instance.add_assign
    instance.add_assign = original
    assert instance.add_assign == original



@given(instance=myDsl_assignment_operator_strategy)
def test_mydsl_assignment_operator_right_assign_setter(instance):
    original = instance.right_assign
    instance.right_assign = original
    assert instance.right_assign == original



@given(instance=myDsl_assignment_operator_strategy)
def test_mydsl_assignment_operator_sub_assign_setter(instance):
    original = instance.sub_assign
    instance.sub_assign = original
    assert instance.sub_assign == original



@given(instance=myDsl_assignment_operator_strategy)
def test_mydsl_assignment_operator_mul_assign_setter(instance):
    original = instance.mul_assign
    instance.mul_assign = original
    assert instance.mul_assign == original



@given(instance=myDsl_assignment_operator_strategy)
def test_mydsl_assignment_operator_mod_assign_setter(instance):
    original = instance.mod_assign
    instance.mod_assign = original
    assert instance.mod_assign == original



@given(instance=myDsl_assignment_operator_strategy)
def test_mydsl_assignment_operator_xor_assign_setter(instance):
    original = instance.xor_assign
    instance.xor_assign = original
    assert instance.xor_assign == original



@given(instance=myDsl_assignment_operator_strategy)
def test_mydsl_assignment_operator_div_assign_setter(instance):
    original = instance.div_assign
    instance.div_assign = original
    assert instance.div_assign == original

@given(instance=myDsl_function_specifier_strategy)
@settings(max_examples=50)
def test_mydsl_function_specifier_instantiation(instance):
    assert isinstance(instance, myDsl_function_specifier)



@given(instance=myDsl_function_specifier_strategy)
def test_mydsl_function_specifier_noreturn_setter(instance):
    original = instance.noreturn
    instance.noreturn = original
    assert instance.noreturn == original



@given(instance=myDsl_function_specifier_strategy)
def test_mydsl_function_specifier_inline_setter(instance):
    original = instance.inline
    instance.inline = original
    assert instance.inline == original

@given(instance=myDsl_type_qualifier_strategy)
@settings(max_examples=50)
def test_mydsl_type_qualifier_instantiation(instance):
    assert isinstance(instance, myDsl_type_qualifier)



@given(instance=myDsl_type_qualifier_strategy)
def test_mydsl_type_qualifier_const_setter(instance):
    original = instance.const
    instance.const = original
    assert instance.const == original



@given(instance=myDsl_type_qualifier_strategy)
def test_mydsl_type_qualifier_volatile_setter(instance):
    original = instance.volatile
    instance.volatile = original
    assert instance.volatile == original



@given(instance=myDsl_type_qualifier_strategy)
def test_mydsl_type_qualifier_restrict_setter(instance):
    original = instance.restrict
    instance.restrict = original
    assert instance.restrict == original



@given(instance=myDsl_type_qualifier_strategy)
def test_mydsl_type_qualifier_atomic_setter(instance):
    original = instance.atomic
    instance.atomic = original
    assert instance.atomic == original

@given(instance=myDsl_type_specifier_strategy)
@settings(max_examples=50)
def test_mydsl_type_specifier_instantiation(instance):
    assert isinstance(instance, myDsl_type_specifier)



@given(instance=myDsl_type_specifier_strategy)
def test_mydsl_type_specifier_typedef_name_setter(instance):
    original = instance.typedef_name
    instance.typedef_name = original
    assert instance.typedef_name == original

@given(instance=myDsl_storage_class_specifier_strategy)
@settings(max_examples=50)
def test_mydsl_storage_class_specifier_instantiation(instance):
    assert isinstance(instance, myDsl_storage_class_specifier)



@given(instance=myDsl_storage_class_specifier_strategy)
def test_mydsl_storage_class_specifier_thread_local_setter(instance):
    original = instance.thread_local
    instance.thread_local = original
    assert instance.thread_local == original



@given(instance=myDsl_storage_class_specifier_strategy)
def test_mydsl_storage_class_specifier_auto_setter(instance):
    original = instance.auto
    instance.auto = original
    assert instance.auto == original



@given(instance=myDsl_storage_class_specifier_strategy)
def test_mydsl_storage_class_specifier_typedef_setter(instance):
    original = instance.typedef
    instance.typedef = original
    assert instance.typedef == original



@given(instance=myDsl_storage_class_specifier_strategy)
def test_mydsl_storage_class_specifier_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original



@given(instance=myDsl_storage_class_specifier_strategy)
def test_mydsl_storage_class_specifier_register_setter(instance):
    original = instance.register
    instance.register = original
    assert instance.register == original



@given(instance=myDsl_storage_class_specifier_strategy)
def test_mydsl_storage_class_specifier_extern_setter(instance):
    original = instance.extern
    instance.extern = original
    assert instance.extern == original

@given(instance=myDsl_static_assert_declaration_strategy)
@settings(max_examples=50)
def test_mydsl_static_assert_declaration_instantiation(instance):
    assert isinstance(instance, myDsl_static_assert_declaration)



@given(instance=myDsl_static_assert_declaration_strategy)
def test_mydsl_static_assert_declaration_static_assert_setter(instance):
    original = instance.static_assert
    instance.static_assert = original
    assert instance.static_assert == original



@given(instance=myDsl_static_assert_declaration_strategy)
def test_mydsl_static_assert_declaration_string_literal_setter(instance):
    original = instance.string_literal
    instance.string_literal = original
    assert instance.string_literal == original

@given(instance=myDsl_init_declarator_list_strategy)
@settings(max_examples=50)
def test_mydsl_init_declarator_list_instantiation(instance):
    assert isinstance(instance, myDsl_init_declarator_list)

@given(instance=simple_expression_strategy)
@settings(max_examples=50)
def test_simple_expression_instantiation(instance):
    assert isinstance(instance, simple_expression)

@given(instance=myDsl_variableRef_strategy)
@settings(max_examples=50)
def test_mydsl_variableref_instantiation(instance):
    assert isinstance(instance, myDsl_variableRef)



@given(instance=myDsl_variableRef_strategy)
def test_mydsl_variableref_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=myDsl_MINUS_strategy)
@settings(max_examples=50)
def test_mydsl_minus_instantiation(instance):
    assert isinstance(instance, myDsl_MINUS)

@given(instance=myDsl_intType_strategy)
@settings(max_examples=50)
def test_mydsl_inttype_instantiation(instance):
    assert isinstance(instance, myDsl_intType)



@given(instance=myDsl_intType_strategy)
def test_mydsl_inttype_int_type_setter(instance):
    original = instance.int_type
    instance.int_type = original
    assert instance.int_type == original



@given(instance=myDsl_intType_strategy)
def test_mydsl_inttype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=myDsl_floatType_strategy)
@settings(max_examples=50)
def test_mydsl_floattype_instantiation(instance):
    assert isinstance(instance, myDsl_floatType)



@given(instance=myDsl_floatType_strategy)
def test_mydsl_floattype_float_type_setter(instance):
    original = instance.float_type
    instance.float_type = original
    assert instance.float_type == original



@given(instance=myDsl_floatType_strategy)
def test_mydsl_floattype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=myDsl_ADD_strategy)
@settings(max_examples=50)
def test_mydsl_add_instantiation(instance):
    assert isinstance(instance, myDsl_ADD)

@given(instance=myDsl_unary_expression_strategy)
@settings(max_examples=50)
def test_mydsl_unary_expression_instantiation(instance):
    assert isinstance(instance, myDsl_unary_expression)



@given(instance=myDsl_unary_expression_strategy)
def test_mydsl_unary_expression_dec_op_setter(instance):
    original = instance.dec_op
    instance.dec_op = original
    assert instance.dec_op == original



@given(instance=myDsl_unary_expression_strategy)
def test_mydsl_unary_expression_sizeof_setter(instance):
    original = instance.sizeof
    instance.sizeof = original
    assert instance.sizeof == original



@given(instance=myDsl_unary_expression_strategy)
def test_mydsl_unary_expression_unary_operator_setter(instance):
    original = instance.unary_operator
    instance.unary_operator = original
    assert instance.unary_operator == original



@given(instance=myDsl_unary_expression_strategy)
def test_mydsl_unary_expression_alignof_setter(instance):
    original = instance.alignof
    instance.alignof = original
    assert instance.alignof == original



@given(instance=myDsl_unary_expression_strategy)
def test_mydsl_unary_expression_inc_op_setter(instance):
    original = instance.inc_op
    instance.inc_op = original
    assert instance.inc_op == original

@given(instance=postfix_expression2_strategy)
@settings(max_examples=50)
def test_postfix_expression2_instantiation(instance):
    assert isinstance(instance, postfix_expression2)

@given(instance=myDsl_argument_expression_list_strategy)
@settings(max_examples=50)
def test_mydsl_argument_expression_list_instantiation(instance):
    assert isinstance(instance, myDsl_argument_expression_list)

@given(instance=myDsl_initializer_list_strategy)
@settings(max_examples=50)
def test_mydsl_initializer_list_instantiation(instance):
    assert isinstance(instance, myDsl_initializer_list)

@given(instance=myDsl_postfix_expression2_strategy)
@settings(max_examples=50)
def test_mydsl_postfix_expression2_instantiation(instance):
    assert isinstance(instance, myDsl_postfix_expression2)

@given(instance=myDsl_postfix_expression_strategy)
@settings(max_examples=50)
def test_mydsl_postfix_expression_instantiation(instance):
    assert isinstance(instance, myDsl_postfix_expression)

@given(instance=myDsl_generic_association_strategy)
@settings(max_examples=50)
def test_mydsl_generic_association_instantiation(instance):
    assert isinstance(instance, myDsl_generic_association)



@given(instance=myDsl_generic_association_strategy)
def test_mydsl_generic_association_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=myDsl_generic_assoc_list_strategy)
@settings(max_examples=50)
def test_mydsl_generic_assoc_list_instantiation(instance):
    assert isinstance(instance, myDsl_generic_assoc_list)

@given(instance=myDsl_assignment_expression_strategy)
@settings(max_examples=50)
def test_mydsl_assignment_expression_instantiation(instance):
    assert isinstance(instance, myDsl_assignment_expression)

@given(instance=myDsl_expression_strategy)
@settings(max_examples=50)
def test_mydsl_expression_instantiation(instance):
    assert isinstance(instance, myDsl_expression)

@given(instance=myDsl_conditional_expression_strategy)
@settings(max_examples=50)
def test_mydsl_conditional_expression_instantiation(instance):
    assert isinstance(instance, myDsl_conditional_expression)

@given(instance=myDsl_constant_strategy)
@settings(max_examples=50)
def test_mydsl_constant_instantiation(instance):
    assert isinstance(instance, myDsl_constant)



@given(instance=myDsl_constant_strategy)
def test_mydsl_constant_f_constant_setter(instance):
    original = instance.f_constant
    instance.f_constant = original
    assert instance.f_constant == original



@given(instance=myDsl_constant_strategy)
def test_mydsl_constant_i_constant_setter(instance):
    original = instance.i_constant
    instance.i_constant = original
    assert instance.i_constant == original



@given(instance=myDsl_constant_strategy)
def test_mydsl_constant_enumt_setter(instance):
    original = instance.enumt
    instance.enumt = original
    assert instance.enumt == original

@given(instance=myDsl_type_name_strategy)
@settings(max_examples=50)
def test_mydsl_type_name_instantiation(instance):
    assert isinstance(instance, myDsl_type_name)

@given(instance=myDsl_simple_expression_strategy)
@settings(max_examples=50)
def test_mydsl_simple_expression_instantiation(instance):
    assert isinstance(instance, myDsl_simple_expression)

@given(instance=myDsl_translation_unit_strategy)
@settings(max_examples=50)
def test_mydsl_translation_unit_instantiation(instance):
    assert isinstance(instance, myDsl_translation_unit)

@given(instance=myDsl_Model_strategy)
@settings(max_examples=50)
def test_mydsl_model_instantiation(instance):
    assert isinstance(instance, myDsl_Model)

@given(instance=myDsl_generic_selection_strategy)
@settings(max_examples=50)
def test_mydsl_generic_selection_instantiation(instance):
    assert isinstance(instance, myDsl_generic_selection)



@given(instance=myDsl_generic_selection_strategy)
def test_mydsl_generic_selection_generic_setter(instance):
    original = instance.generic
    instance.generic = original
    assert instance.generic == original

@given(instance=myDsl_string_nova_strategy)
@settings(max_examples=50)
def test_mydsl_string_nova_instantiation(instance):
    assert isinstance(instance, myDsl_string_nova)



@given(instance=myDsl_string_nova_strategy)
def test_mydsl_string_nova_func_name_setter(instance):
    original = instance.func_name
    instance.func_name = original
    assert instance.func_name == original



@given(instance=myDsl_string_nova_strategy)
def test_mydsl_string_nova_string_literal_setter(instance):
    original = instance.string_literal
    instance.string_literal = original
    assert instance.string_literal == original

@given(instance=myDsl_enumeration_constant_strategy)
@settings(max_examples=50)
def test_mydsl_enumeration_constant_instantiation(instance):
    assert isinstance(instance, myDsl_enumeration_constant)



@given(instance=myDsl_enumeration_constant_strategy)
def test_mydsl_enumeration_constant_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=myDsl_unsignedType_strategy)
@settings(max_examples=50)
def test_mydsl_unsignedtype_instantiation(instance):
    assert isinstance(instance, myDsl_unsignedType)



@given(instance=myDsl_unsignedType_strategy)
def test_mydsl_unsignedtype_unsigned_type_setter(instance):
    original = instance.unsigned_type
    instance.unsigned_type = original
    assert instance.unsigned_type == original

@given(instance=myDsl_signedType_strategy)
@settings(max_examples=50)
def test_mydsl_signedtype_instantiation(instance):
    assert isinstance(instance, myDsl_signedType)



@given(instance=myDsl_signedType_strategy)
def test_mydsl_signedtype_signed_type_setter(instance):
    original = instance.signed_type
    instance.signed_type = original
    assert instance.signed_type == original

@given(instance=myDsl_doubleType_strategy)
@settings(max_examples=50)
def test_mydsl_doubletype_instantiation(instance):
    assert isinstance(instance, myDsl_doubleType)



@given(instance=myDsl_doubleType_strategy)
def test_mydsl_doubletype_double_type_setter(instance):
    original = instance.double_type
    instance.double_type = original
    assert instance.double_type == original

@given(instance=myDsl_longType_strategy)
@settings(max_examples=50)
def test_mydsl_longtype_instantiation(instance):
    assert isinstance(instance, myDsl_longType)



@given(instance=myDsl_longType_strategy)
def test_mydsl_longtype_long_type_setter(instance):
    original = instance.long_type
    instance.long_type = original
    assert instance.long_type == original

@given(instance=myDsl_shortType_strategy)
@settings(max_examples=50)
def test_mydsl_shorttype_instantiation(instance):
    assert isinstance(instance, myDsl_shortType)



@given(instance=myDsl_shortType_strategy)
def test_mydsl_shorttype_short_type_setter(instance):
    original = instance.short_type
    instance.short_type = original
    assert instance.short_type == original

@given(instance=myDsl_charType_strategy)
@settings(max_examples=50)
def test_mydsl_chartype_instantiation(instance):
    assert isinstance(instance, myDsl_charType)



@given(instance=myDsl_charType_strategy)
def test_mydsl_chartype_char_type_setter(instance):
    original = instance.char_type
    instance.char_type = original
    assert instance.char_type == original

@given(instance=myDsl_voidType_strategy)
@settings(max_examples=50)
def test_mydsl_voidtype_instantiation(instance):
    assert isinstance(instance, myDsl_voidType)



@given(instance=myDsl_voidType_strategy)
def test_mydsl_voidtype_void_type_setter(instance):
    original = instance.void_type
    instance.void_type = original
    assert instance.void_type == original

@given(instance=myDsl_LOG_OR_strategy)
@settings(max_examples=50)
def test_mydsl_log_or_instantiation(instance):
    assert isinstance(instance, myDsl_LOG_OR)

@given(instance=myDsl_imaginaryType_strategy)
@settings(max_examples=50)
def test_mydsl_imaginarytype_instantiation(instance):
    assert isinstance(instance, myDsl_imaginaryType)



@given(instance=myDsl_imaginaryType_strategy)
def test_mydsl_imaginarytype_imaginary_type_setter(instance):
    original = instance.imaginary_type
    instance.imaginary_type = original
    assert instance.imaginary_type == original

@given(instance=myDsl_complexType_strategy)
@settings(max_examples=50)
def test_mydsl_complextype_instantiation(instance):
    assert isinstance(instance, myDsl_complexType)



@given(instance=myDsl_complexType_strategy)
def test_mydsl_complextype_complex_type_setter(instance):
    original = instance.complex_type
    instance.complex_type = original
    assert instance.complex_type == original

@given(instance=myDsl_AND_strategy)
@settings(max_examples=50)
def test_mydsl_and_instantiation(instance):
    assert isinstance(instance, myDsl_AND)

@given(instance=myDsl_EQL_strategy)
@settings(max_examples=50)
def test_mydsl_eql_instantiation(instance):
    assert isinstance(instance, myDsl_EQL)



@given(instance=myDsl_EQL_strategy)
def test_mydsl_eql_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=myDsl_REL_strategy)
@settings(max_examples=50)
def test_mydsl_rel_instantiation(instance):
    assert isinstance(instance, myDsl_REL)



@given(instance=myDsl_REL_strategy)
def test_mydsl_rel_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=myDsl_SHF_strategy)
@settings(max_examples=50)
def test_mydsl_shf_instantiation(instance):
    assert isinstance(instance, myDsl_SHF)



@given(instance=myDsl_SHF_strategy)
def test_mydsl_shf_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=myDsl_LOG_AND_strategy)
@settings(max_examples=50)
def test_mydsl_log_and_instantiation(instance):
    assert isinstance(instance, myDsl_LOG_AND)

@given(instance=myDsl_INC_OR_strategy)
@settings(max_examples=50)
def test_mydsl_inc_or_instantiation(instance):
    assert isinstance(instance, myDsl_INC_OR)

@given(instance=myDsl_MUL_strategy)
@settings(max_examples=50)
def test_mydsl_mul_instantiation(instance):
    assert isinstance(instance, myDsl_MUL)



@given(instance=myDsl_MUL_strategy)
def test_mydsl_mul_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=myDsl_EXC_OR_strategy)
@settings(max_examples=50)
def test_mydsl_exc_or_instantiation(instance):
    assert isinstance(instance, myDsl_EXC_OR)

@given(instance=myDsl_booleanType_strategy)
@settings(max_examples=50)
def test_mydsl_booleantype_instantiation(instance):
    assert isinstance(instance, myDsl_booleanType)



@given(instance=myDsl_booleanType_strategy)
def test_mydsl_booleantype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=myDsl_booleanType_strategy)
def test_mydsl_booleantype_bool_type_setter(instance):
    original = instance.bool_type
    instance.bool_type = original
    assert instance.bool_type == original

@given(instance=myDsl_stringType_strategy)
@settings(max_examples=50)
def test_mydsl_stringtype_instantiation(instance):
    assert isinstance(instance, myDsl_stringType)
