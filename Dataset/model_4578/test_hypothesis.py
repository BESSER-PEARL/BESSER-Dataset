import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    postfix_expressionR,
    struct_or_union_specifier,
    labeled_statement,
    identifier_listR,
    identifier_list,
    direct_declarator,
    declaration_specifiers,
    myDsl_argument_expression_list,
    myDsl_EObject,
    abstract_declarator,
    myDsl_argument_expression_listR,
    type_specifier,
    myDsl_atomic_type_specifier,
    myDsl_struct_or_union_specifier,
    declaration,
    myDsl_struct_declaration,
    myDsl_struct_declaration_list,
    myDsl_struct_declarator_listR,
    myDsl_struct_declarator,
    myDsl_struct_declarator_list,
    myDsl_struct_declaration_listR,
    myDsl_type_specifier,
    struct_declaration,
    myDsl_static_assert_declaration,
    type_name,
    myDsl_specifier_qualifier_list,
    myDsl_designator_listR,
    myDsl_designator,
    designation,
    atomic_type_specifier,
    static_assert_declaration,
    designator,
    myDsl_designation,
    myDsl_postfix_expressionR,
    myDsl_primary_expression,
    unary_expression,
    myDsl_postfix_expression,
    cast_expression,
    myDsl_designator_list,
    myDsl_initializer_listR,
    myDsl_cast_expression,
    myDsl_multiplicative_expressionR,
    myDsl_additive_expressionR,
    myDsl_multiplicative_expression,
    myDsl_type_name,
    myDsl_unary_expression,
    initializer,
    myDsl_initializer_list,
    myDsl_relational_expressionR,
    myDsl_shift_expression,
    myDsl_equality_expressionR,
    myDsl_relational_expression,
    shift_expression,
    myDsl_additive_expression,
    myDsl_shift_expressionR,
    myDsl_inclusive_or_expressionR,
    myDsl_exclusive_or_expression,
    myDsl_logical_and_expressionR,
    myDsl_equality_expression,
    myDsl_and_expressionR,
    myDsl_exclusive_or_expressionR,
    myDsl_and_expression,
    constant_expression,
    assignment_expression,
    myDsl_conditional_expression,
    myDsl_expressionR,
    primary_expression,
    myDsl_StringC,
    expression_statement,
    jump_statement,
    myDsl_IDENTIFIER,
    myDsl_inclusive_or_expression,
    myDsl_logical_or_expressionR,
    myDsl_logical_and_expression,
    conditional_expression,
    myDsl_logical_or_expression,
    myDsl_initializer,
    myDsl_init_declarator_listR,
    myDsl_init_declarator,
    myDsl_init_declarator_list,
    parameter_declaration,
    block_item,
    myDsl_statement,
    myDsl_block_item_listR,
    myDsl_block_item,
    compound_statement,
    myDsl_block_item_list,
    statement,
    myDsl_jump_statement,
    myDsl_selection_statement,
    myDsl_expression_statement,
    myDsl_expression,
    myDsl_iteration_statement,
    myDsl_labeled_statement,
    myDsl_parameter_listR,
    myDsl_parameter_declaration,
    parameter_type_list,
    myDsl_parameter_list,
    myDsl_identifier_listR,
    myDsl_declaration_listR,
    myDsl_abstract_declarator,
    myDsl_type_qualifier_listR,
    pointer,
    myDsl_type_qualifier_list,
    myDsl_pointer,
    struct_declarator,
    myDsl_constant_expression,
    init_declarator,
    myDsl_compound_statement,
    myDsl_identifier_list,
    myDsl_parameter_type_list,
    myDsl_assignment_expression,
    myDsl_direct_declaratorR,
    declarator,
    myDsl_direct_declarator,
    myDsl_external_declaration,
    myDsl_translation_unit,
    myDsl_Model,
    myDsl_declaration_list,
    myDsl_declarator,
    external_declaration,
    myDsl_declaration,
    myDsl_function_definition,
    myDsl_declaration_specifiers,
    myDsl_translation_unitR,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_postfix_expressionr_is_not_abstract():
    assert not inspect.isabstract(postfix_expressionR)


def test_postfix_expressionr_constructor_exists():
    assert callable(postfix_expressionR.__init__)


def test_postfix_expressionr_constructor_args():
    sig = inspect.signature(postfix_expressionR.__init__)
    params = list(sig.parameters.keys())



def test_struct_or_union_specifier_is_not_abstract():
    assert not inspect.isabstract(struct_or_union_specifier)


def test_struct_or_union_specifier_constructor_exists():
    assert callable(struct_or_union_specifier.__init__)


def test_struct_or_union_specifier_constructor_args():
    sig = inspect.signature(struct_or_union_specifier.__init__)
    params = list(sig.parameters.keys())



def test_labeled_statement_is_not_abstract():
    assert not inspect.isabstract(labeled_statement)


def test_labeled_statement_constructor_exists():
    assert callable(labeled_statement.__init__)


def test_labeled_statement_constructor_args():
    sig = inspect.signature(labeled_statement.__init__)
    params = list(sig.parameters.keys())



def test_identifier_listr_is_not_abstract():
    assert not inspect.isabstract(identifier_listR)


def test_identifier_listr_constructor_exists():
    assert callable(identifier_listR.__init__)


def test_identifier_listr_constructor_args():
    sig = inspect.signature(identifier_listR.__init__)
    params = list(sig.parameters.keys())



def test_identifier_list_is_not_abstract():
    assert not inspect.isabstract(identifier_list)


def test_identifier_list_constructor_exists():
    assert callable(identifier_list.__init__)


def test_identifier_list_constructor_args():
    sig = inspect.signature(identifier_list.__init__)
    params = list(sig.parameters.keys())



def test_direct_declarator_is_not_abstract():
    assert not inspect.isabstract(direct_declarator)


def test_direct_declarator_constructor_exists():
    assert callable(direct_declarator.__init__)


def test_direct_declarator_constructor_args():
    sig = inspect.signature(direct_declarator.__init__)
    params = list(sig.parameters.keys())



def test_declaration_specifiers_is_not_abstract():
    assert not inspect.isabstract(declaration_specifiers)


def test_declaration_specifiers_constructor_exists():
    assert callable(declaration_specifiers.__init__)


def test_declaration_specifiers_constructor_args():
    sig = inspect.signature(declaration_specifiers.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_argument_expression_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_argument_expression_list)


def test_mydsl_argument_expression_list_constructor_exists():
    assert callable(myDsl_argument_expression_list.__init__)


def test_mydsl_argument_expression_list_constructor_args():
    sig = inspect.signature(myDsl_argument_expression_list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_eobject_is_not_abstract():
    assert not inspect.isabstract(myDsl_EObject)


def test_mydsl_eobject_constructor_exists():
    assert callable(myDsl_EObject.__init__)


def test_mydsl_eobject_constructor_args():
    sig = inspect.signature(myDsl_EObject.__init__)
    params = list(sig.parameters.keys())



def test_abstract_declarator_is_not_abstract():
    assert not inspect.isabstract(abstract_declarator)


def test_abstract_declarator_constructor_exists():
    assert callable(abstract_declarator.__init__)


def test_abstract_declarator_constructor_args():
    sig = inspect.signature(abstract_declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_argument_expression_listr_is_not_abstract():
    assert not inspect.isabstract(myDsl_argument_expression_listR)


def test_mydsl_argument_expression_listr_constructor_exists():
    assert callable(myDsl_argument_expression_listR.__init__)


def test_mydsl_argument_expression_listr_constructor_args():
    sig = inspect.signature(myDsl_argument_expression_listR.__init__)
    params = list(sig.parameters.keys())



def test_type_specifier_is_not_abstract():
    assert not inspect.isabstract(type_specifier)


def test_type_specifier_constructor_exists():
    assert callable(type_specifier.__init__)


def test_type_specifier_constructor_args():
    sig = inspect.signature(type_specifier.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_atomic_type_specifier_is_not_abstract():
    assert not inspect.isabstract(myDsl_atomic_type_specifier)


def test_mydsl_atomic_type_specifier_constructor_exists():
    assert callable(myDsl_atomic_type_specifier.__init__)


def test_mydsl_atomic_type_specifier_constructor_args():
    sig = inspect.signature(myDsl_atomic_type_specifier.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_struct_or_union_specifier_is_not_abstract():
    assert not inspect.isabstract(myDsl_struct_or_union_specifier)


def test_mydsl_struct_or_union_specifier_constructor_exists():
    assert callable(myDsl_struct_or_union_specifier.__init__)


def test_mydsl_struct_or_union_specifier_constructor_args():
    sig = inspect.signature(myDsl_struct_or_union_specifier.__init__)
    params = list(sig.parameters.keys())
    assert "Struct_or_union" in params, "Missing parameter 'Struct_or_union'"

def test_mydsl_struct_or_union_specifier_has_Struct_or_union():
    assert hasattr(myDsl_struct_or_union_specifier, "Struct_or_union")
    descriptor = None
    for klass in myDsl_struct_or_union_specifier.__mro__:
        if "Struct_or_union" in klass.__dict__:
            descriptor = klass.__dict__["Struct_or_union"]
            break
    assert isinstance(descriptor, property)



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(declaration)


def test_declaration_constructor_exists():
    assert callable(declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(declaration.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_struct_declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl_struct_declaration)


def test_mydsl_struct_declaration_constructor_exists():
    assert callable(myDsl_struct_declaration.__init__)


def test_mydsl_struct_declaration_constructor_args():
    sig = inspect.signature(myDsl_struct_declaration.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_struct_declaration_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_struct_declaration_list)


def test_mydsl_struct_declaration_list_constructor_exists():
    assert callable(myDsl_struct_declaration_list.__init__)


def test_mydsl_struct_declaration_list_constructor_args():
    sig = inspect.signature(myDsl_struct_declaration_list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_struct_declarator_listr_is_not_abstract():
    assert not inspect.isabstract(myDsl_struct_declarator_listR)


def test_mydsl_struct_declarator_listr_constructor_exists():
    assert callable(myDsl_struct_declarator_listR.__init__)


def test_mydsl_struct_declarator_listr_constructor_args():
    sig = inspect.signature(myDsl_struct_declarator_listR.__init__)
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



def test_mydsl_struct_declaration_listr_is_not_abstract():
    assert not inspect.isabstract(myDsl_struct_declaration_listR)


def test_mydsl_struct_declaration_listr_constructor_exists():
    assert callable(myDsl_struct_declaration_listR.__init__)


def test_mydsl_struct_declaration_listr_constructor_args():
    sig = inspect.signature(myDsl_struct_declaration_listR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_type_specifier_is_not_abstract():
    assert not inspect.isabstract(myDsl_type_specifier)


def test_mydsl_type_specifier_constructor_exists():
    assert callable(myDsl_type_specifier.__init__)


def test_mydsl_type_specifier_constructor_args():
    sig = inspect.signature(myDsl_type_specifier.__init__)
    params = list(sig.parameters.keys())



def test_struct_declaration_is_not_abstract():
    assert not inspect.isabstract(struct_declaration)


def test_struct_declaration_constructor_exists():
    assert callable(struct_declaration.__init__)


def test_struct_declaration_constructor_args():
    sig = inspect.signature(struct_declaration.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_static_assert_declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl_static_assert_declaration)


def test_mydsl_static_assert_declaration_constructor_exists():
    assert callable(myDsl_static_assert_declaration.__init__)


def test_mydsl_static_assert_declaration_constructor_args():
    sig = inspect.signature(myDsl_static_assert_declaration.__init__)
    params = list(sig.parameters.keys())



def test_type_name_is_not_abstract():
    assert not inspect.isabstract(type_name)


def test_type_name_constructor_exists():
    assert callable(type_name.__init__)


def test_type_name_constructor_args():
    sig = inspect.signature(type_name.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_specifier_qualifier_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_specifier_qualifier_list)


def test_mydsl_specifier_qualifier_list_constructor_exists():
    assert callable(myDsl_specifier_qualifier_list.__init__)


def test_mydsl_specifier_qualifier_list_constructor_args():
    sig = inspect.signature(myDsl_specifier_qualifier_list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_designator_listr_is_not_abstract():
    assert not inspect.isabstract(myDsl_designator_listR)


def test_mydsl_designator_listr_constructor_exists():
    assert callable(myDsl_designator_listR.__init__)


def test_mydsl_designator_listr_constructor_args():
    sig = inspect.signature(myDsl_designator_listR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_designator_is_not_abstract():
    assert not inspect.isabstract(myDsl_designator)


def test_mydsl_designator_constructor_exists():
    assert callable(myDsl_designator.__init__)


def test_mydsl_designator_constructor_args():
    sig = inspect.signature(myDsl_designator.__init__)
    params = list(sig.parameters.keys())



def test_designation_is_not_abstract():
    assert not inspect.isabstract(designation)


def test_designation_constructor_exists():
    assert callable(designation.__init__)


def test_designation_constructor_args():
    sig = inspect.signature(designation.__init__)
    params = list(sig.parameters.keys())



def test_atomic_type_specifier_is_not_abstract():
    assert not inspect.isabstract(atomic_type_specifier)


def test_atomic_type_specifier_constructor_exists():
    assert callable(atomic_type_specifier.__init__)


def test_atomic_type_specifier_constructor_args():
    sig = inspect.signature(atomic_type_specifier.__init__)
    params = list(sig.parameters.keys())



def test_static_assert_declaration_is_not_abstract():
    assert not inspect.isabstract(static_assert_declaration)


def test_static_assert_declaration_constructor_exists():
    assert callable(static_assert_declaration.__init__)


def test_static_assert_declaration_constructor_args():
    sig = inspect.signature(static_assert_declaration.__init__)
    params = list(sig.parameters.keys())



def test_designator_is_not_abstract():
    assert not inspect.isabstract(designator)


def test_designator_constructor_exists():
    assert callable(designator.__init__)


def test_designator_constructor_args():
    sig = inspect.signature(designator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_designation_is_not_abstract():
    assert not inspect.isabstract(myDsl_designation)


def test_mydsl_designation_constructor_exists():
    assert callable(myDsl_designation.__init__)


def test_mydsl_designation_constructor_args():
    sig = inspect.signature(myDsl_designation.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_postfix_expressionr_is_not_abstract():
    assert not inspect.isabstract(myDsl_postfix_expressionR)


def test_mydsl_postfix_expressionr_constructor_exists():
    assert callable(myDsl_postfix_expressionR.__init__)


def test_mydsl_postfix_expressionr_constructor_args():
    sig = inspect.signature(myDsl_postfix_expressionR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_primary_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_primary_expression)


def test_mydsl_primary_expression_constructor_exists():
    assert callable(myDsl_primary_expression.__init__)


def test_mydsl_primary_expression_constructor_args():
    sig = inspect.signature(myDsl_primary_expression.__init__)
    params = list(sig.parameters.keys())



def test_unary_expression_is_not_abstract():
    assert not inspect.isabstract(unary_expression)


def test_unary_expression_constructor_exists():
    assert callable(unary_expression.__init__)


def test_unary_expression_constructor_args():
    sig = inspect.signature(unary_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_postfix_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_postfix_expression)


def test_mydsl_postfix_expression_constructor_exists():
    assert callable(myDsl_postfix_expression.__init__)


def test_mydsl_postfix_expression_constructor_args():
    sig = inspect.signature(myDsl_postfix_expression.__init__)
    params = list(sig.parameters.keys())



def test_cast_expression_is_not_abstract():
    assert not inspect.isabstract(cast_expression)


def test_cast_expression_constructor_exists():
    assert callable(cast_expression.__init__)


def test_cast_expression_constructor_args():
    sig = inspect.signature(cast_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_designator_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_designator_list)


def test_mydsl_designator_list_constructor_exists():
    assert callable(myDsl_designator_list.__init__)


def test_mydsl_designator_list_constructor_args():
    sig = inspect.signature(myDsl_designator_list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_initializer_listr_is_not_abstract():
    assert not inspect.isabstract(myDsl_initializer_listR)


def test_mydsl_initializer_listr_constructor_exists():
    assert callable(myDsl_initializer_listR.__init__)


def test_mydsl_initializer_listr_constructor_args():
    sig = inspect.signature(myDsl_initializer_listR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_cast_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_cast_expression)


def test_mydsl_cast_expression_constructor_exists():
    assert callable(myDsl_cast_expression.__init__)


def test_mydsl_cast_expression_constructor_args():
    sig = inspect.signature(myDsl_cast_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_multiplicative_expressionr_is_not_abstract():
    assert not inspect.isabstract(myDsl_multiplicative_expressionR)


def test_mydsl_multiplicative_expressionr_constructor_exists():
    assert callable(myDsl_multiplicative_expressionR.__init__)


def test_mydsl_multiplicative_expressionr_constructor_args():
    sig = inspect.signature(myDsl_multiplicative_expressionR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_additive_expressionr_is_not_abstract():
    assert not inspect.isabstract(myDsl_additive_expressionR)


def test_mydsl_additive_expressionr_constructor_exists():
    assert callable(myDsl_additive_expressionR.__init__)


def test_mydsl_additive_expressionr_constructor_args():
    sig = inspect.signature(myDsl_additive_expressionR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_multiplicative_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_multiplicative_expression)


def test_mydsl_multiplicative_expression_constructor_exists():
    assert callable(myDsl_multiplicative_expression.__init__)


def test_mydsl_multiplicative_expression_constructor_args():
    sig = inspect.signature(myDsl_multiplicative_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_type_name_is_not_abstract():
    assert not inspect.isabstract(myDsl_type_name)


def test_mydsl_type_name_constructor_exists():
    assert callable(myDsl_type_name.__init__)


def test_mydsl_type_name_constructor_args():
    sig = inspect.signature(myDsl_type_name.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_unary_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_unary_expression)


def test_mydsl_unary_expression_constructor_exists():
    assert callable(myDsl_unary_expression.__init__)


def test_mydsl_unary_expression_constructor_args():
    sig = inspect.signature(myDsl_unary_expression.__init__)
    params = list(sig.parameters.keys())
    assert "Unary_operator" in params, "Missing parameter 'Unary_operator'"

def test_mydsl_unary_expression_has_Unary_operator():
    assert hasattr(myDsl_unary_expression, "Unary_operator")
    descriptor = None
    for klass in myDsl_unary_expression.__mro__:
        if "Unary_operator" in klass.__dict__:
            descriptor = klass.__dict__["Unary_operator"]
            break
    assert isinstance(descriptor, property)



def test_initializer_is_not_abstract():
    assert not inspect.isabstract(initializer)


def test_initializer_constructor_exists():
    assert callable(initializer.__init__)


def test_initializer_constructor_args():
    sig = inspect.signature(initializer.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_initializer_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_initializer_list)


def test_mydsl_initializer_list_constructor_exists():
    assert callable(myDsl_initializer_list.__init__)


def test_mydsl_initializer_list_constructor_args():
    sig = inspect.signature(myDsl_initializer_list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_relational_expressionr_is_not_abstract():
    assert not inspect.isabstract(myDsl_relational_expressionR)


def test_mydsl_relational_expressionr_constructor_exists():
    assert callable(myDsl_relational_expressionR.__init__)


def test_mydsl_relational_expressionr_constructor_args():
    sig = inspect.signature(myDsl_relational_expressionR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_shift_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_shift_expression)


def test_mydsl_shift_expression_constructor_exists():
    assert callable(myDsl_shift_expression.__init__)


def test_mydsl_shift_expression_constructor_args():
    sig = inspect.signature(myDsl_shift_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_equality_expressionr_is_not_abstract():
    assert not inspect.isabstract(myDsl_equality_expressionR)


def test_mydsl_equality_expressionr_constructor_exists():
    assert callable(myDsl_equality_expressionR.__init__)


def test_mydsl_equality_expressionr_constructor_args():
    sig = inspect.signature(myDsl_equality_expressionR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_relational_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_relational_expression)


def test_mydsl_relational_expression_constructor_exists():
    assert callable(myDsl_relational_expression.__init__)


def test_mydsl_relational_expression_constructor_args():
    sig = inspect.signature(myDsl_relational_expression.__init__)
    params = list(sig.parameters.keys())



def test_shift_expression_is_not_abstract():
    assert not inspect.isabstract(shift_expression)


def test_shift_expression_constructor_exists():
    assert callable(shift_expression.__init__)


def test_shift_expression_constructor_args():
    sig = inspect.signature(shift_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_additive_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_additive_expression)


def test_mydsl_additive_expression_constructor_exists():
    assert callable(myDsl_additive_expression.__init__)


def test_mydsl_additive_expression_constructor_args():
    sig = inspect.signature(myDsl_additive_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_shift_expressionr_is_not_abstract():
    assert not inspect.isabstract(myDsl_shift_expressionR)


def test_mydsl_shift_expressionr_constructor_exists():
    assert callable(myDsl_shift_expressionR.__init__)


def test_mydsl_shift_expressionr_constructor_args():
    sig = inspect.signature(myDsl_shift_expressionR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_inclusive_or_expressionr_is_not_abstract():
    assert not inspect.isabstract(myDsl_inclusive_or_expressionR)


def test_mydsl_inclusive_or_expressionr_constructor_exists():
    assert callable(myDsl_inclusive_or_expressionR.__init__)


def test_mydsl_inclusive_or_expressionr_constructor_args():
    sig = inspect.signature(myDsl_inclusive_or_expressionR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_exclusive_or_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_exclusive_or_expression)


def test_mydsl_exclusive_or_expression_constructor_exists():
    assert callable(myDsl_exclusive_or_expression.__init__)


def test_mydsl_exclusive_or_expression_constructor_args():
    sig = inspect.signature(myDsl_exclusive_or_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_logical_and_expressionr_is_not_abstract():
    assert not inspect.isabstract(myDsl_logical_and_expressionR)


def test_mydsl_logical_and_expressionr_constructor_exists():
    assert callable(myDsl_logical_and_expressionR.__init__)


def test_mydsl_logical_and_expressionr_constructor_args():
    sig = inspect.signature(myDsl_logical_and_expressionR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_equality_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_equality_expression)


def test_mydsl_equality_expression_constructor_exists():
    assert callable(myDsl_equality_expression.__init__)


def test_mydsl_equality_expression_constructor_args():
    sig = inspect.signature(myDsl_equality_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_and_expressionr_is_not_abstract():
    assert not inspect.isabstract(myDsl_and_expressionR)


def test_mydsl_and_expressionr_constructor_exists():
    assert callable(myDsl_and_expressionR.__init__)


def test_mydsl_and_expressionr_constructor_args():
    sig = inspect.signature(myDsl_and_expressionR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_exclusive_or_expressionr_is_not_abstract():
    assert not inspect.isabstract(myDsl_exclusive_or_expressionR)


def test_mydsl_exclusive_or_expressionr_constructor_exists():
    assert callable(myDsl_exclusive_or_expressionR.__init__)


def test_mydsl_exclusive_or_expressionr_constructor_args():
    sig = inspect.signature(myDsl_exclusive_or_expressionR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_and_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_and_expression)


def test_mydsl_and_expression_constructor_exists():
    assert callable(myDsl_and_expression.__init__)


def test_mydsl_and_expression_constructor_args():
    sig = inspect.signature(myDsl_and_expression.__init__)
    params = list(sig.parameters.keys())



def test_constant_expression_is_not_abstract():
    assert not inspect.isabstract(constant_expression)


def test_constant_expression_constructor_exists():
    assert callable(constant_expression.__init__)


def test_constant_expression_constructor_args():
    sig = inspect.signature(constant_expression.__init__)
    params = list(sig.parameters.keys())



def test_assignment_expression_is_not_abstract():
    assert not inspect.isabstract(assignment_expression)


def test_assignment_expression_constructor_exists():
    assert callable(assignment_expression.__init__)


def test_assignment_expression_constructor_args():
    sig = inspect.signature(assignment_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_conditional_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_conditional_expression)


def test_mydsl_conditional_expression_constructor_exists():
    assert callable(myDsl_conditional_expression.__init__)


def test_mydsl_conditional_expression_constructor_args():
    sig = inspect.signature(myDsl_conditional_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_expressionr_is_not_abstract():
    assert not inspect.isabstract(myDsl_expressionR)


def test_mydsl_expressionr_constructor_exists():
    assert callable(myDsl_expressionR.__init__)


def test_mydsl_expressionr_constructor_args():
    sig = inspect.signature(myDsl_expressionR.__init__)
    params = list(sig.parameters.keys())



def test_primary_expression_is_not_abstract():
    assert not inspect.isabstract(primary_expression)


def test_primary_expression_constructor_exists():
    assert callable(primary_expression.__init__)


def test_primary_expression_constructor_args():
    sig = inspect.signature(primary_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_stringc_is_not_abstract():
    assert not inspect.isabstract(myDsl_StringC)


def test_mydsl_stringc_constructor_exists():
    assert callable(myDsl_StringC.__init__)


def test_mydsl_stringc_constructor_args():
    sig = inspect.signature(myDsl_StringC.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"

def test_mydsl_stringc_has_string():
    assert hasattr(myDsl_StringC, "string")
    descriptor = None
    for klass in myDsl_StringC.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)



def test_expression_statement_is_not_abstract():
    assert not inspect.isabstract(expression_statement)


def test_expression_statement_constructor_exists():
    assert callable(expression_statement.__init__)


def test_expression_statement_constructor_args():
    sig = inspect.signature(expression_statement.__init__)
    params = list(sig.parameters.keys())



def test_jump_statement_is_not_abstract():
    assert not inspect.isabstract(jump_statement)


def test_jump_statement_constructor_exists():
    assert callable(jump_statement.__init__)


def test_jump_statement_constructor_args():
    sig = inspect.signature(jump_statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_identifier_is_not_abstract():
    assert not inspect.isabstract(myDsl_IDENTIFIER)


def test_mydsl_identifier_constructor_exists():
    assert callable(myDsl_IDENTIFIER.__init__)


def test_mydsl_identifier_constructor_args():
    sig = inspect.signature(myDsl_IDENTIFIER.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_identifier_has_name():
    assert hasattr(myDsl_IDENTIFIER, "name")
    descriptor = None
    for klass in myDsl_IDENTIFIER.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_inclusive_or_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_inclusive_or_expression)


def test_mydsl_inclusive_or_expression_constructor_exists():
    assert callable(myDsl_inclusive_or_expression.__init__)


def test_mydsl_inclusive_or_expression_constructor_args():
    sig = inspect.signature(myDsl_inclusive_or_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_logical_or_expressionr_is_not_abstract():
    assert not inspect.isabstract(myDsl_logical_or_expressionR)


def test_mydsl_logical_or_expressionr_constructor_exists():
    assert callable(myDsl_logical_or_expressionR.__init__)


def test_mydsl_logical_or_expressionr_constructor_args():
    sig = inspect.signature(myDsl_logical_or_expressionR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_logical_and_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_logical_and_expression)


def test_mydsl_logical_and_expression_constructor_exists():
    assert callable(myDsl_logical_and_expression.__init__)


def test_mydsl_logical_and_expression_constructor_args():
    sig = inspect.signature(myDsl_logical_and_expression.__init__)
    params = list(sig.parameters.keys())



def test_conditional_expression_is_not_abstract():
    assert not inspect.isabstract(conditional_expression)


def test_conditional_expression_constructor_exists():
    assert callable(conditional_expression.__init__)


def test_conditional_expression_constructor_args():
    sig = inspect.signature(conditional_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_logical_or_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_logical_or_expression)


def test_mydsl_logical_or_expression_constructor_exists():
    assert callable(myDsl_logical_or_expression.__init__)


def test_mydsl_logical_or_expression_constructor_args():
    sig = inspect.signature(myDsl_logical_or_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_initializer_is_not_abstract():
    assert not inspect.isabstract(myDsl_initializer)


def test_mydsl_initializer_constructor_exists():
    assert callable(myDsl_initializer.__init__)


def test_mydsl_initializer_constructor_args():
    sig = inspect.signature(myDsl_initializer.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_init_declarator_listr_is_not_abstract():
    assert not inspect.isabstract(myDsl_init_declarator_listR)


def test_mydsl_init_declarator_listr_constructor_exists():
    assert callable(myDsl_init_declarator_listR.__init__)


def test_mydsl_init_declarator_listr_constructor_args():
    sig = inspect.signature(myDsl_init_declarator_listR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_init_declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl_init_declarator)


def test_mydsl_init_declarator_constructor_exists():
    assert callable(myDsl_init_declarator.__init__)


def test_mydsl_init_declarator_constructor_args():
    sig = inspect.signature(myDsl_init_declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_init_declarator_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_init_declarator_list)


def test_mydsl_init_declarator_list_constructor_exists():
    assert callable(myDsl_init_declarator_list.__init__)


def test_mydsl_init_declarator_list_constructor_args():
    sig = inspect.signature(myDsl_init_declarator_list.__init__)
    params = list(sig.parameters.keys())



def test_parameter_declaration_is_not_abstract():
    assert not inspect.isabstract(parameter_declaration)


def test_parameter_declaration_constructor_exists():
    assert callable(parameter_declaration.__init__)


def test_parameter_declaration_constructor_args():
    sig = inspect.signature(parameter_declaration.__init__)
    params = list(sig.parameters.keys())



def test_block_item_is_not_abstract():
    assert not inspect.isabstract(block_item)


def test_block_item_constructor_exists():
    assert callable(block_item.__init__)


def test_block_item_constructor_args():
    sig = inspect.signature(block_item.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_statement_is_not_abstract():
    assert not inspect.isabstract(myDsl_statement)


def test_mydsl_statement_constructor_exists():
    assert callable(myDsl_statement.__init__)


def test_mydsl_statement_constructor_args():
    sig = inspect.signature(myDsl_statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_block_item_listr_is_not_abstract():
    assert not inspect.isabstract(myDsl_block_item_listR)


def test_mydsl_block_item_listr_constructor_exists():
    assert callable(myDsl_block_item_listR.__init__)


def test_mydsl_block_item_listr_constructor_args():
    sig = inspect.signature(myDsl_block_item_listR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_block_item_is_not_abstract():
    assert not inspect.isabstract(myDsl_block_item)


def test_mydsl_block_item_constructor_exists():
    assert callable(myDsl_block_item.__init__)


def test_mydsl_block_item_constructor_args():
    sig = inspect.signature(myDsl_block_item.__init__)
    params = list(sig.parameters.keys())



def test_compound_statement_is_not_abstract():
    assert not inspect.isabstract(compound_statement)


def test_compound_statement_constructor_exists():
    assert callable(compound_statement.__init__)


def test_compound_statement_constructor_args():
    sig = inspect.signature(compound_statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_block_item_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_block_item_list)


def test_mydsl_block_item_list_constructor_exists():
    assert callable(myDsl_block_item_list.__init__)


def test_mydsl_block_item_list_constructor_args():
    sig = inspect.signature(myDsl_block_item_list.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(statement)


def test_statement_constructor_exists():
    assert callable(statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_jump_statement_is_not_abstract():
    assert not inspect.isabstract(myDsl_jump_statement)


def test_mydsl_jump_statement_constructor_exists():
    assert callable(myDsl_jump_statement.__init__)


def test_mydsl_jump_statement_constructor_args():
    sig = inspect.signature(myDsl_jump_statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_selection_statement_is_not_abstract():
    assert not inspect.isabstract(myDsl_selection_statement)


def test_mydsl_selection_statement_constructor_exists():
    assert callable(myDsl_selection_statement.__init__)


def test_mydsl_selection_statement_constructor_args():
    sig = inspect.signature(myDsl_selection_statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_expression_statement_is_not_abstract():
    assert not inspect.isabstract(myDsl_expression_statement)


def test_mydsl_expression_statement_constructor_exists():
    assert callable(myDsl_expression_statement.__init__)


def test_mydsl_expression_statement_constructor_args():
    sig = inspect.signature(myDsl_expression_statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_expression)


def test_mydsl_expression_constructor_exists():
    assert callable(myDsl_expression.__init__)


def test_mydsl_expression_constructor_args():
    sig = inspect.signature(myDsl_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_iteration_statement_is_not_abstract():
    assert not inspect.isabstract(myDsl_iteration_statement)


def test_mydsl_iteration_statement_constructor_exists():
    assert callable(myDsl_iteration_statement.__init__)


def test_mydsl_iteration_statement_constructor_args():
    sig = inspect.signature(myDsl_iteration_statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_labeled_statement_is_not_abstract():
    assert not inspect.isabstract(myDsl_labeled_statement)


def test_mydsl_labeled_statement_constructor_exists():
    assert callable(myDsl_labeled_statement.__init__)


def test_mydsl_labeled_statement_constructor_args():
    sig = inspect.signature(myDsl_labeled_statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_parameter_listr_is_not_abstract():
    assert not inspect.isabstract(myDsl_parameter_listR)


def test_mydsl_parameter_listr_constructor_exists():
    assert callable(myDsl_parameter_listR.__init__)


def test_mydsl_parameter_listr_constructor_args():
    sig = inspect.signature(myDsl_parameter_listR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_parameter_declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl_parameter_declaration)


def test_mydsl_parameter_declaration_constructor_exists():
    assert callable(myDsl_parameter_declaration.__init__)


def test_mydsl_parameter_declaration_constructor_args():
    sig = inspect.signature(myDsl_parameter_declaration.__init__)
    params = list(sig.parameters.keys())



def test_parameter_type_list_is_not_abstract():
    assert not inspect.isabstract(parameter_type_list)


def test_parameter_type_list_constructor_exists():
    assert callable(parameter_type_list.__init__)


def test_parameter_type_list_constructor_args():
    sig = inspect.signature(parameter_type_list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_parameter_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_parameter_list)


def test_mydsl_parameter_list_constructor_exists():
    assert callable(myDsl_parameter_list.__init__)


def test_mydsl_parameter_list_constructor_args():
    sig = inspect.signature(myDsl_parameter_list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_identifier_listr_is_not_abstract():
    assert not inspect.isabstract(myDsl_identifier_listR)


def test_mydsl_identifier_listr_constructor_exists():
    assert callable(myDsl_identifier_listR.__init__)


def test_mydsl_identifier_listr_constructor_args():
    sig = inspect.signature(myDsl_identifier_listR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_declaration_listr_is_not_abstract():
    assert not inspect.isabstract(myDsl_declaration_listR)


def test_mydsl_declaration_listr_constructor_exists():
    assert callable(myDsl_declaration_listR.__init__)


def test_mydsl_declaration_listr_constructor_args():
    sig = inspect.signature(myDsl_declaration_listR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_abstract_declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl_abstract_declarator)


def test_mydsl_abstract_declarator_constructor_exists():
    assert callable(myDsl_abstract_declarator.__init__)


def test_mydsl_abstract_declarator_constructor_args():
    sig = inspect.signature(myDsl_abstract_declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_type_qualifier_listr_is_not_abstract():
    assert not inspect.isabstract(myDsl_type_qualifier_listR)


def test_mydsl_type_qualifier_listr_constructor_exists():
    assert callable(myDsl_type_qualifier_listR.__init__)


def test_mydsl_type_qualifier_listr_constructor_args():
    sig = inspect.signature(myDsl_type_qualifier_listR.__init__)
    params = list(sig.parameters.keys())
    assert "Type_qualifier" in params, "Missing parameter 'Type_qualifier'"

def test_mydsl_type_qualifier_listr_has_Type_qualifier():
    assert hasattr(myDsl_type_qualifier_listR, "Type_qualifier")
    descriptor = None
    for klass in myDsl_type_qualifier_listR.__mro__:
        if "Type_qualifier" in klass.__dict__:
            descriptor = klass.__dict__["Type_qualifier"]
            break
    assert isinstance(descriptor, property)



def test_pointer_is_not_abstract():
    assert not inspect.isabstract(pointer)


def test_pointer_constructor_exists():
    assert callable(pointer.__init__)


def test_pointer_constructor_args():
    sig = inspect.signature(pointer.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_type_qualifier_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_type_qualifier_list)


def test_mydsl_type_qualifier_list_constructor_exists():
    assert callable(myDsl_type_qualifier_list.__init__)


def test_mydsl_type_qualifier_list_constructor_args():
    sig = inspect.signature(myDsl_type_qualifier_list.__init__)
    params = list(sig.parameters.keys())
    assert "Type_qualifier" in params, "Missing parameter 'Type_qualifier'"

def test_mydsl_type_qualifier_list_has_Type_qualifier():
    assert hasattr(myDsl_type_qualifier_list, "Type_qualifier")
    descriptor = None
    for klass in myDsl_type_qualifier_list.__mro__:
        if "Type_qualifier" in klass.__dict__:
            descriptor = klass.__dict__["Type_qualifier"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_pointer_is_not_abstract():
    assert not inspect.isabstract(myDsl_pointer)


def test_mydsl_pointer_constructor_exists():
    assert callable(myDsl_pointer.__init__)


def test_mydsl_pointer_constructor_args():
    sig = inspect.signature(myDsl_pointer.__init__)
    params = list(sig.parameters.keys())



def test_struct_declarator_is_not_abstract():
    assert not inspect.isabstract(struct_declarator)


def test_struct_declarator_constructor_exists():
    assert callable(struct_declarator.__init__)


def test_struct_declarator_constructor_args():
    sig = inspect.signature(struct_declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_constant_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_constant_expression)


def test_mydsl_constant_expression_constructor_exists():
    assert callable(myDsl_constant_expression.__init__)


def test_mydsl_constant_expression_constructor_args():
    sig = inspect.signature(myDsl_constant_expression.__init__)
    params = list(sig.parameters.keys())



def test_init_declarator_is_not_abstract():
    assert not inspect.isabstract(init_declarator)


def test_init_declarator_constructor_exists():
    assert callable(init_declarator.__init__)


def test_init_declarator_constructor_args():
    sig = inspect.signature(init_declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_compound_statement_is_not_abstract():
    assert not inspect.isabstract(myDsl_compound_statement)


def test_mydsl_compound_statement_constructor_exists():
    assert callable(myDsl_compound_statement.__init__)


def test_mydsl_compound_statement_constructor_args():
    sig = inspect.signature(myDsl_compound_statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_identifier_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_identifier_list)


def test_mydsl_identifier_list_constructor_exists():
    assert callable(myDsl_identifier_list.__init__)


def test_mydsl_identifier_list_constructor_args():
    sig = inspect.signature(myDsl_identifier_list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_parameter_type_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_parameter_type_list)


def test_mydsl_parameter_type_list_constructor_exists():
    assert callable(myDsl_parameter_type_list.__init__)


def test_mydsl_parameter_type_list_constructor_args():
    sig = inspect.signature(myDsl_parameter_type_list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_assignment_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_assignment_expression)


def test_mydsl_assignment_expression_constructor_exists():
    assert callable(myDsl_assignment_expression.__init__)


def test_mydsl_assignment_expression_constructor_args():
    sig = inspect.signature(myDsl_assignment_expression.__init__)
    params = list(sig.parameters.keys())
    assert "Assignment_operator" in params, "Missing parameter 'Assignment_operator'"

def test_mydsl_assignment_expression_has_Assignment_operator():
    assert hasattr(myDsl_assignment_expression, "Assignment_operator")
    descriptor = None
    for klass in myDsl_assignment_expression.__mro__:
        if "Assignment_operator" in klass.__dict__:
            descriptor = klass.__dict__["Assignment_operator"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_direct_declaratorr_is_not_abstract():
    assert not inspect.isabstract(myDsl_direct_declaratorR)


def test_mydsl_direct_declaratorr_constructor_exists():
    assert callable(myDsl_direct_declaratorR.__init__)


def test_mydsl_direct_declaratorr_constructor_args():
    sig = inspect.signature(myDsl_direct_declaratorR.__init__)
    params = list(sig.parameters.keys())



def test_declarator_is_not_abstract():
    assert not inspect.isabstract(declarator)


def test_declarator_constructor_exists():
    assert callable(declarator.__init__)


def test_declarator_constructor_args():
    sig = inspect.signature(declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_direct_declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl_direct_declarator)


def test_mydsl_direct_declarator_constructor_exists():
    assert callable(myDsl_direct_declarator.__init__)


def test_mydsl_direct_declarator_constructor_args():
    sig = inspect.signature(myDsl_direct_declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_external_declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl_external_declaration)


def test_mydsl_external_declaration_constructor_exists():
    assert callable(myDsl_external_declaration.__init__)


def test_mydsl_external_declaration_constructor_args():
    sig = inspect.signature(myDsl_external_declaration.__init__)
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



def test_mydsl_declaration_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_declaration_list)


def test_mydsl_declaration_list_constructor_exists():
    assert callable(myDsl_declaration_list.__init__)


def test_mydsl_declaration_list_constructor_args():
    sig = inspect.signature(myDsl_declaration_list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl_declarator)


def test_mydsl_declarator_constructor_exists():
    assert callable(myDsl_declarator.__init__)


def test_mydsl_declarator_constructor_args():
    sig = inspect.signature(myDsl_declarator.__init__)
    params = list(sig.parameters.keys())



def test_external_declaration_is_not_abstract():
    assert not inspect.isabstract(external_declaration)


def test_external_declaration_constructor_exists():
    assert callable(external_declaration.__init__)


def test_external_declaration_constructor_args():
    sig = inspect.signature(external_declaration.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl_declaration)


def test_mydsl_declaration_constructor_exists():
    assert callable(myDsl_declaration.__init__)


def test_mydsl_declaration_constructor_args():
    sig = inspect.signature(myDsl_declaration.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_function_definition_is_not_abstract():
    assert not inspect.isabstract(myDsl_function_definition)


def test_mydsl_function_definition_constructor_exists():
    assert callable(myDsl_function_definition.__init__)


def test_mydsl_function_definition_constructor_args():
    sig = inspect.signature(myDsl_function_definition.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_declaration_specifiers_is_not_abstract():
    assert not inspect.isabstract(myDsl_declaration_specifiers)


def test_mydsl_declaration_specifiers_constructor_exists():
    assert callable(myDsl_declaration_specifiers.__init__)


def test_mydsl_declaration_specifiers_constructor_args():
    sig = inspect.signature(myDsl_declaration_specifiers.__init__)
    params = list(sig.parameters.keys())
    assert "Storage_class_specifier" in params, "Missing parameter 'Storage_class_specifier'"
    assert "Type_qualifier" in params, "Missing parameter 'Type_qualifier'"

def test_mydsl_declaration_specifiers_has_Storage_class_specifier():
    assert hasattr(myDsl_declaration_specifiers, "Storage_class_specifier")
    descriptor = None
    for klass in myDsl_declaration_specifiers.__mro__:
        if "Storage_class_specifier" in klass.__dict__:
            descriptor = klass.__dict__["Storage_class_specifier"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_declaration_specifiers_has_Type_qualifier():
    assert hasattr(myDsl_declaration_specifiers, "Type_qualifier")
    descriptor = None
    for klass in myDsl_declaration_specifiers.__mro__:
        if "Type_qualifier" in klass.__dict__:
            descriptor = klass.__dict__["Type_qualifier"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_translation_unitr_is_not_abstract():
    assert not inspect.isabstract(myDsl_translation_unitR)


def test_mydsl_translation_unitr_constructor_exists():
    assert callable(myDsl_translation_unitR.__init__)


def test_mydsl_translation_unitr_constructor_args():
    sig = inspect.signature(myDsl_translation_unitR.__init__)
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
postfix_expressionR_strategy = st.builds(
    postfix_expressionR,
)
struct_or_union_specifier_strategy = st.builds(
    struct_or_union_specifier,
)
labeled_statement_strategy = st.builds(
    labeled_statement,
)
identifier_listR_strategy = st.builds(
    identifier_listR,
)
identifier_list_strategy = st.builds(
    identifier_list,
)
direct_declarator_strategy = st.builds(
    direct_declarator,
)
declaration_specifiers_strategy = st.builds(
    declaration_specifiers,
)
myDsl_argument_expression_list_strategy = st.builds(
    myDsl_argument_expression_list,
)
myDsl_EObject_strategy = st.builds(
    myDsl_EObject,
)
abstract_declarator_strategy = st.builds(
    abstract_declarator,
)
myDsl_argument_expression_listR_strategy = st.builds(
    myDsl_argument_expression_listR,
)
type_specifier_strategy = st.builds(
    type_specifier,
)
myDsl_atomic_type_specifier_strategy = st.builds(
    myDsl_atomic_type_specifier,
)
myDsl_struct_or_union_specifier_strategy = st.builds(
    myDsl_struct_or_union_specifier,
    Struct_or_union=
        safe_text
)
declaration_strategy = st.builds(
    declaration,
)
myDsl_struct_declaration_strategy = st.builds(
    myDsl_struct_declaration,
)
myDsl_struct_declaration_list_strategy = st.builds(
    myDsl_struct_declaration_list,
)
myDsl_struct_declarator_listR_strategy = st.builds(
    myDsl_struct_declarator_listR,
)
myDsl_struct_declarator_strategy = st.builds(
    myDsl_struct_declarator,
)
myDsl_struct_declarator_list_strategy = st.builds(
    myDsl_struct_declarator_list,
)
myDsl_struct_declaration_listR_strategy = st.builds(
    myDsl_struct_declaration_listR,
)
myDsl_type_specifier_strategy = st.builds(
    myDsl_type_specifier,
)
struct_declaration_strategy = st.builds(
    struct_declaration,
)
myDsl_static_assert_declaration_strategy = st.builds(
    myDsl_static_assert_declaration,
)
type_name_strategy = st.builds(
    type_name,
)
myDsl_specifier_qualifier_list_strategy = st.builds(
    myDsl_specifier_qualifier_list,
)
myDsl_designator_listR_strategy = st.builds(
    myDsl_designator_listR,
)
myDsl_designator_strategy = st.builds(
    myDsl_designator,
)
designation_strategy = st.builds(
    designation,
)
atomic_type_specifier_strategy = st.builds(
    atomic_type_specifier,
)
static_assert_declaration_strategy = st.builds(
    static_assert_declaration,
)
designator_strategy = st.builds(
    designator,
)
myDsl_designation_strategy = st.builds(
    myDsl_designation,
)
myDsl_postfix_expressionR_strategy = st.builds(
    myDsl_postfix_expressionR,
)
myDsl_primary_expression_strategy = st.builds(
    myDsl_primary_expression,
)
unary_expression_strategy = st.builds(
    unary_expression,
)
myDsl_postfix_expression_strategy = st.builds(
    myDsl_postfix_expression,
)
cast_expression_strategy = st.builds(
    cast_expression,
)
myDsl_designator_list_strategy = st.builds(
    myDsl_designator_list,
)
myDsl_initializer_listR_strategy = st.builds(
    myDsl_initializer_listR,
)
myDsl_cast_expression_strategy = st.builds(
    myDsl_cast_expression,
)
myDsl_multiplicative_expressionR_strategy = st.builds(
    myDsl_multiplicative_expressionR,
)
myDsl_additive_expressionR_strategy = st.builds(
    myDsl_additive_expressionR,
)
myDsl_multiplicative_expression_strategy = st.builds(
    myDsl_multiplicative_expression,
)
myDsl_type_name_strategy = st.builds(
    myDsl_type_name,
)
myDsl_unary_expression_strategy = st.builds(
    myDsl_unary_expression,
    Unary_operator=
        safe_text
)
initializer_strategy = st.builds(
    initializer,
)
myDsl_initializer_list_strategy = st.builds(
    myDsl_initializer_list,
)
myDsl_relational_expressionR_strategy = st.builds(
    myDsl_relational_expressionR,
)
myDsl_shift_expression_strategy = st.builds(
    myDsl_shift_expression,
)
myDsl_equality_expressionR_strategy = st.builds(
    myDsl_equality_expressionR,
)
myDsl_relational_expression_strategy = st.builds(
    myDsl_relational_expression,
)
shift_expression_strategy = st.builds(
    shift_expression,
)
myDsl_additive_expression_strategy = st.builds(
    myDsl_additive_expression,
)
myDsl_shift_expressionR_strategy = st.builds(
    myDsl_shift_expressionR,
)
myDsl_inclusive_or_expressionR_strategy = st.builds(
    myDsl_inclusive_or_expressionR,
)
myDsl_exclusive_or_expression_strategy = st.builds(
    myDsl_exclusive_or_expression,
)
myDsl_logical_and_expressionR_strategy = st.builds(
    myDsl_logical_and_expressionR,
)
myDsl_equality_expression_strategy = st.builds(
    myDsl_equality_expression,
)
myDsl_and_expressionR_strategy = st.builds(
    myDsl_and_expressionR,
)
myDsl_exclusive_or_expressionR_strategy = st.builds(
    myDsl_exclusive_or_expressionR,
)
myDsl_and_expression_strategy = st.builds(
    myDsl_and_expression,
)
constant_expression_strategy = st.builds(
    constant_expression,
)
assignment_expression_strategy = st.builds(
    assignment_expression,
)
myDsl_conditional_expression_strategy = st.builds(
    myDsl_conditional_expression,
)
myDsl_expressionR_strategy = st.builds(
    myDsl_expressionR,
)
primary_expression_strategy = st.builds(
    primary_expression,
)
myDsl_StringC_strategy = st.builds(
    myDsl_StringC,
    string=
        safe_text
)
expression_statement_strategy = st.builds(
    expression_statement,
)
jump_statement_strategy = st.builds(
    jump_statement,
)
myDsl_IDENTIFIER_strategy = st.builds(
    myDsl_IDENTIFIER,
    name=
        safe_text
)
myDsl_inclusive_or_expression_strategy = st.builds(
    myDsl_inclusive_or_expression,
)
myDsl_logical_or_expressionR_strategy = st.builds(
    myDsl_logical_or_expressionR,
)
myDsl_logical_and_expression_strategy = st.builds(
    myDsl_logical_and_expression,
)
conditional_expression_strategy = st.builds(
    conditional_expression,
)
myDsl_logical_or_expression_strategy = st.builds(
    myDsl_logical_or_expression,
)
myDsl_initializer_strategy = st.builds(
    myDsl_initializer,
)
myDsl_init_declarator_listR_strategy = st.builds(
    myDsl_init_declarator_listR,
)
myDsl_init_declarator_strategy = st.builds(
    myDsl_init_declarator,
)
myDsl_init_declarator_list_strategy = st.builds(
    myDsl_init_declarator_list,
)
parameter_declaration_strategy = st.builds(
    parameter_declaration,
)
block_item_strategy = st.builds(
    block_item,
)
myDsl_statement_strategy = st.builds(
    myDsl_statement,
)
myDsl_block_item_listR_strategy = st.builds(
    myDsl_block_item_listR,
)
myDsl_block_item_strategy = st.builds(
    myDsl_block_item,
)
compound_statement_strategy = st.builds(
    compound_statement,
)
myDsl_block_item_list_strategy = st.builds(
    myDsl_block_item_list,
)
statement_strategy = st.builds(
    statement,
)
myDsl_jump_statement_strategy = st.builds(
    myDsl_jump_statement,
)
myDsl_selection_statement_strategy = st.builds(
    myDsl_selection_statement,
)
myDsl_expression_statement_strategy = st.builds(
    myDsl_expression_statement,
)
myDsl_expression_strategy = st.builds(
    myDsl_expression,
)
myDsl_iteration_statement_strategy = st.builds(
    myDsl_iteration_statement,
)
myDsl_labeled_statement_strategy = st.builds(
    myDsl_labeled_statement,
)
myDsl_parameter_listR_strategy = st.builds(
    myDsl_parameter_listR,
)
myDsl_parameter_declaration_strategy = st.builds(
    myDsl_parameter_declaration,
)
parameter_type_list_strategy = st.builds(
    parameter_type_list,
)
myDsl_parameter_list_strategy = st.builds(
    myDsl_parameter_list,
)
myDsl_identifier_listR_strategy = st.builds(
    myDsl_identifier_listR,
)
myDsl_declaration_listR_strategy = st.builds(
    myDsl_declaration_listR,
)
myDsl_abstract_declarator_strategy = st.builds(
    myDsl_abstract_declarator,
)
myDsl_type_qualifier_listR_strategy = st.builds(
    myDsl_type_qualifier_listR,
    Type_qualifier=
        safe_text
)
pointer_strategy = st.builds(
    pointer,
)
myDsl_type_qualifier_list_strategy = st.builds(
    myDsl_type_qualifier_list,
    Type_qualifier=
        safe_text
)
myDsl_pointer_strategy = st.builds(
    myDsl_pointer,
)
struct_declarator_strategy = st.builds(
    struct_declarator,
)
myDsl_constant_expression_strategy = st.builds(
    myDsl_constant_expression,
)
init_declarator_strategy = st.builds(
    init_declarator,
)
myDsl_compound_statement_strategy = st.builds(
    myDsl_compound_statement,
)
myDsl_identifier_list_strategy = st.builds(
    myDsl_identifier_list,
)
myDsl_parameter_type_list_strategy = st.builds(
    myDsl_parameter_type_list,
)
myDsl_assignment_expression_strategy = st.builds(
    myDsl_assignment_expression,
    Assignment_operator=
        safe_text
)
myDsl_direct_declaratorR_strategy = st.builds(
    myDsl_direct_declaratorR,
)
declarator_strategy = st.builds(
    declarator,
)
myDsl_direct_declarator_strategy = st.builds(
    myDsl_direct_declarator,
)
myDsl_external_declaration_strategy = st.builds(
    myDsl_external_declaration,
)
myDsl_translation_unit_strategy = st.builds(
    myDsl_translation_unit,
)
myDsl_Model_strategy = st.builds(
    myDsl_Model,
)
myDsl_declaration_list_strategy = st.builds(
    myDsl_declaration_list,
)
myDsl_declarator_strategy = st.builds(
    myDsl_declarator,
)
external_declaration_strategy = st.builds(
    external_declaration,
)
myDsl_declaration_strategy = st.builds(
    myDsl_declaration,
)
myDsl_function_definition_strategy = st.builds(
    myDsl_function_definition,
)
myDsl_declaration_specifiers_strategy = st.builds(
    myDsl_declaration_specifiers,
    Storage_class_specifier=
        safe_text,
    Type_qualifier=
        safe_text
)
myDsl_translation_unitR_strategy = st.builds(
    myDsl_translation_unitR,
)

@given(instance=postfix_expressionR_strategy)
@settings(max_examples=50)
def test_postfix_expressionr_instantiation(instance):
    assert isinstance(instance, postfix_expressionR)

@given(instance=struct_or_union_specifier_strategy)
@settings(max_examples=50)
def test_struct_or_union_specifier_instantiation(instance):
    assert isinstance(instance, struct_or_union_specifier)

@given(instance=labeled_statement_strategy)
@settings(max_examples=50)
def test_labeled_statement_instantiation(instance):
    assert isinstance(instance, labeled_statement)

@given(instance=identifier_listR_strategy)
@settings(max_examples=50)
def test_identifier_listr_instantiation(instance):
    assert isinstance(instance, identifier_listR)

@given(instance=identifier_list_strategy)
@settings(max_examples=50)
def test_identifier_list_instantiation(instance):
    assert isinstance(instance, identifier_list)

@given(instance=direct_declarator_strategy)
@settings(max_examples=50)
def test_direct_declarator_instantiation(instance):
    assert isinstance(instance, direct_declarator)

@given(instance=declaration_specifiers_strategy)
@settings(max_examples=50)
def test_declaration_specifiers_instantiation(instance):
    assert isinstance(instance, declaration_specifiers)

@given(instance=myDsl_argument_expression_list_strategy)
@settings(max_examples=50)
def test_mydsl_argument_expression_list_instantiation(instance):
    assert isinstance(instance, myDsl_argument_expression_list)

@given(instance=myDsl_EObject_strategy)
@settings(max_examples=50)
def test_mydsl_eobject_instantiation(instance):
    assert isinstance(instance, myDsl_EObject)

@given(instance=abstract_declarator_strategy)
@settings(max_examples=50)
def test_abstract_declarator_instantiation(instance):
    assert isinstance(instance, abstract_declarator)

@given(instance=myDsl_argument_expression_listR_strategy)
@settings(max_examples=50)
def test_mydsl_argument_expression_listr_instantiation(instance):
    assert isinstance(instance, myDsl_argument_expression_listR)

@given(instance=type_specifier_strategy)
@settings(max_examples=50)
def test_type_specifier_instantiation(instance):
    assert isinstance(instance, type_specifier)

@given(instance=myDsl_atomic_type_specifier_strategy)
@settings(max_examples=50)
def test_mydsl_atomic_type_specifier_instantiation(instance):
    assert isinstance(instance, myDsl_atomic_type_specifier)

@given(instance=myDsl_struct_or_union_specifier_strategy)
@settings(max_examples=50)
def test_mydsl_struct_or_union_specifier_instantiation(instance):
    assert isinstance(instance, myDsl_struct_or_union_specifier)



@given(instance=myDsl_struct_or_union_specifier_strategy)
def test_mydsl_struct_or_union_specifier_Struct_or_union_setter(instance):
    original = instance.Struct_or_union
    instance.Struct_or_union = original
    assert instance.Struct_or_union == original

@given(instance=declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, declaration)

@given(instance=myDsl_struct_declaration_strategy)
@settings(max_examples=50)
def test_mydsl_struct_declaration_instantiation(instance):
    assert isinstance(instance, myDsl_struct_declaration)

@given(instance=myDsl_struct_declaration_list_strategy)
@settings(max_examples=50)
def test_mydsl_struct_declaration_list_instantiation(instance):
    assert isinstance(instance, myDsl_struct_declaration_list)

@given(instance=myDsl_struct_declarator_listR_strategy)
@settings(max_examples=50)
def test_mydsl_struct_declarator_listr_instantiation(instance):
    assert isinstance(instance, myDsl_struct_declarator_listR)

@given(instance=myDsl_struct_declarator_strategy)
@settings(max_examples=50)
def test_mydsl_struct_declarator_instantiation(instance):
    assert isinstance(instance, myDsl_struct_declarator)

@given(instance=myDsl_struct_declarator_list_strategy)
@settings(max_examples=50)
def test_mydsl_struct_declarator_list_instantiation(instance):
    assert isinstance(instance, myDsl_struct_declarator_list)

@given(instance=myDsl_struct_declaration_listR_strategy)
@settings(max_examples=50)
def test_mydsl_struct_declaration_listr_instantiation(instance):
    assert isinstance(instance, myDsl_struct_declaration_listR)

@given(instance=myDsl_type_specifier_strategy)
@settings(max_examples=50)
def test_mydsl_type_specifier_instantiation(instance):
    assert isinstance(instance, myDsl_type_specifier)

@given(instance=struct_declaration_strategy)
@settings(max_examples=50)
def test_struct_declaration_instantiation(instance):
    assert isinstance(instance, struct_declaration)

@given(instance=myDsl_static_assert_declaration_strategy)
@settings(max_examples=50)
def test_mydsl_static_assert_declaration_instantiation(instance):
    assert isinstance(instance, myDsl_static_assert_declaration)

@given(instance=type_name_strategy)
@settings(max_examples=50)
def test_type_name_instantiation(instance):
    assert isinstance(instance, type_name)

@given(instance=myDsl_specifier_qualifier_list_strategy)
@settings(max_examples=50)
def test_mydsl_specifier_qualifier_list_instantiation(instance):
    assert isinstance(instance, myDsl_specifier_qualifier_list)

@given(instance=myDsl_designator_listR_strategy)
@settings(max_examples=50)
def test_mydsl_designator_listr_instantiation(instance):
    assert isinstance(instance, myDsl_designator_listR)

@given(instance=myDsl_designator_strategy)
@settings(max_examples=50)
def test_mydsl_designator_instantiation(instance):
    assert isinstance(instance, myDsl_designator)

@given(instance=designation_strategy)
@settings(max_examples=50)
def test_designation_instantiation(instance):
    assert isinstance(instance, designation)

@given(instance=atomic_type_specifier_strategy)
@settings(max_examples=50)
def test_atomic_type_specifier_instantiation(instance):
    assert isinstance(instance, atomic_type_specifier)

@given(instance=static_assert_declaration_strategy)
@settings(max_examples=50)
def test_static_assert_declaration_instantiation(instance):
    assert isinstance(instance, static_assert_declaration)

@given(instance=designator_strategy)
@settings(max_examples=50)
def test_designator_instantiation(instance):
    assert isinstance(instance, designator)

@given(instance=myDsl_designation_strategy)
@settings(max_examples=50)
def test_mydsl_designation_instantiation(instance):
    assert isinstance(instance, myDsl_designation)

@given(instance=myDsl_postfix_expressionR_strategy)
@settings(max_examples=50)
def test_mydsl_postfix_expressionr_instantiation(instance):
    assert isinstance(instance, myDsl_postfix_expressionR)

@given(instance=myDsl_primary_expression_strategy)
@settings(max_examples=50)
def test_mydsl_primary_expression_instantiation(instance):
    assert isinstance(instance, myDsl_primary_expression)

@given(instance=unary_expression_strategy)
@settings(max_examples=50)
def test_unary_expression_instantiation(instance):
    assert isinstance(instance, unary_expression)

@given(instance=myDsl_postfix_expression_strategy)
@settings(max_examples=50)
def test_mydsl_postfix_expression_instantiation(instance):
    assert isinstance(instance, myDsl_postfix_expression)

@given(instance=cast_expression_strategy)
@settings(max_examples=50)
def test_cast_expression_instantiation(instance):
    assert isinstance(instance, cast_expression)

@given(instance=myDsl_designator_list_strategy)
@settings(max_examples=50)
def test_mydsl_designator_list_instantiation(instance):
    assert isinstance(instance, myDsl_designator_list)

@given(instance=myDsl_initializer_listR_strategy)
@settings(max_examples=50)
def test_mydsl_initializer_listr_instantiation(instance):
    assert isinstance(instance, myDsl_initializer_listR)

@given(instance=myDsl_cast_expression_strategy)
@settings(max_examples=50)
def test_mydsl_cast_expression_instantiation(instance):
    assert isinstance(instance, myDsl_cast_expression)

@given(instance=myDsl_multiplicative_expressionR_strategy)
@settings(max_examples=50)
def test_mydsl_multiplicative_expressionr_instantiation(instance):
    assert isinstance(instance, myDsl_multiplicative_expressionR)

@given(instance=myDsl_additive_expressionR_strategy)
@settings(max_examples=50)
def test_mydsl_additive_expressionr_instantiation(instance):
    assert isinstance(instance, myDsl_additive_expressionR)

@given(instance=myDsl_multiplicative_expression_strategy)
@settings(max_examples=50)
def test_mydsl_multiplicative_expression_instantiation(instance):
    assert isinstance(instance, myDsl_multiplicative_expression)

@given(instance=myDsl_type_name_strategy)
@settings(max_examples=50)
def test_mydsl_type_name_instantiation(instance):
    assert isinstance(instance, myDsl_type_name)

@given(instance=myDsl_unary_expression_strategy)
@settings(max_examples=50)
def test_mydsl_unary_expression_instantiation(instance):
    assert isinstance(instance, myDsl_unary_expression)



@given(instance=myDsl_unary_expression_strategy)
def test_mydsl_unary_expression_Unary_operator_setter(instance):
    original = instance.Unary_operator
    instance.Unary_operator = original
    assert instance.Unary_operator == original

@given(instance=initializer_strategy)
@settings(max_examples=50)
def test_initializer_instantiation(instance):
    assert isinstance(instance, initializer)

@given(instance=myDsl_initializer_list_strategy)
@settings(max_examples=50)
def test_mydsl_initializer_list_instantiation(instance):
    assert isinstance(instance, myDsl_initializer_list)

@given(instance=myDsl_relational_expressionR_strategy)
@settings(max_examples=50)
def test_mydsl_relational_expressionr_instantiation(instance):
    assert isinstance(instance, myDsl_relational_expressionR)

@given(instance=myDsl_shift_expression_strategy)
@settings(max_examples=50)
def test_mydsl_shift_expression_instantiation(instance):
    assert isinstance(instance, myDsl_shift_expression)

@given(instance=myDsl_equality_expressionR_strategy)
@settings(max_examples=50)
def test_mydsl_equality_expressionr_instantiation(instance):
    assert isinstance(instance, myDsl_equality_expressionR)

@given(instance=myDsl_relational_expression_strategy)
@settings(max_examples=50)
def test_mydsl_relational_expression_instantiation(instance):
    assert isinstance(instance, myDsl_relational_expression)

@given(instance=shift_expression_strategy)
@settings(max_examples=50)
def test_shift_expression_instantiation(instance):
    assert isinstance(instance, shift_expression)

@given(instance=myDsl_additive_expression_strategy)
@settings(max_examples=50)
def test_mydsl_additive_expression_instantiation(instance):
    assert isinstance(instance, myDsl_additive_expression)

@given(instance=myDsl_shift_expressionR_strategy)
@settings(max_examples=50)
def test_mydsl_shift_expressionr_instantiation(instance):
    assert isinstance(instance, myDsl_shift_expressionR)

@given(instance=myDsl_inclusive_or_expressionR_strategy)
@settings(max_examples=50)
def test_mydsl_inclusive_or_expressionr_instantiation(instance):
    assert isinstance(instance, myDsl_inclusive_or_expressionR)

@given(instance=myDsl_exclusive_or_expression_strategy)
@settings(max_examples=50)
def test_mydsl_exclusive_or_expression_instantiation(instance):
    assert isinstance(instance, myDsl_exclusive_or_expression)

@given(instance=myDsl_logical_and_expressionR_strategy)
@settings(max_examples=50)
def test_mydsl_logical_and_expressionr_instantiation(instance):
    assert isinstance(instance, myDsl_logical_and_expressionR)

@given(instance=myDsl_equality_expression_strategy)
@settings(max_examples=50)
def test_mydsl_equality_expression_instantiation(instance):
    assert isinstance(instance, myDsl_equality_expression)

@given(instance=myDsl_and_expressionR_strategy)
@settings(max_examples=50)
def test_mydsl_and_expressionr_instantiation(instance):
    assert isinstance(instance, myDsl_and_expressionR)

@given(instance=myDsl_exclusive_or_expressionR_strategy)
@settings(max_examples=50)
def test_mydsl_exclusive_or_expressionr_instantiation(instance):
    assert isinstance(instance, myDsl_exclusive_or_expressionR)

@given(instance=myDsl_and_expression_strategy)
@settings(max_examples=50)
def test_mydsl_and_expression_instantiation(instance):
    assert isinstance(instance, myDsl_and_expression)

@given(instance=constant_expression_strategy)
@settings(max_examples=50)
def test_constant_expression_instantiation(instance):
    assert isinstance(instance, constant_expression)

@given(instance=assignment_expression_strategy)
@settings(max_examples=50)
def test_assignment_expression_instantiation(instance):
    assert isinstance(instance, assignment_expression)

@given(instance=myDsl_conditional_expression_strategy)
@settings(max_examples=50)
def test_mydsl_conditional_expression_instantiation(instance):
    assert isinstance(instance, myDsl_conditional_expression)

@given(instance=myDsl_expressionR_strategy)
@settings(max_examples=50)
def test_mydsl_expressionr_instantiation(instance):
    assert isinstance(instance, myDsl_expressionR)

@given(instance=primary_expression_strategy)
@settings(max_examples=50)
def test_primary_expression_instantiation(instance):
    assert isinstance(instance, primary_expression)

@given(instance=myDsl_StringC_strategy)
@settings(max_examples=50)
def test_mydsl_stringc_instantiation(instance):
    assert isinstance(instance, myDsl_StringC)



@given(instance=myDsl_StringC_strategy)
def test_mydsl_stringc_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=expression_statement_strategy)
@settings(max_examples=50)
def test_expression_statement_instantiation(instance):
    assert isinstance(instance, expression_statement)

@given(instance=jump_statement_strategy)
@settings(max_examples=50)
def test_jump_statement_instantiation(instance):
    assert isinstance(instance, jump_statement)

@given(instance=myDsl_IDENTIFIER_strategy)
@settings(max_examples=50)
def test_mydsl_identifier_instantiation(instance):
    assert isinstance(instance, myDsl_IDENTIFIER)



@given(instance=myDsl_IDENTIFIER_strategy)
def test_mydsl_identifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_inclusive_or_expression_strategy)
@settings(max_examples=50)
def test_mydsl_inclusive_or_expression_instantiation(instance):
    assert isinstance(instance, myDsl_inclusive_or_expression)

@given(instance=myDsl_logical_or_expressionR_strategy)
@settings(max_examples=50)
def test_mydsl_logical_or_expressionr_instantiation(instance):
    assert isinstance(instance, myDsl_logical_or_expressionR)

@given(instance=myDsl_logical_and_expression_strategy)
@settings(max_examples=50)
def test_mydsl_logical_and_expression_instantiation(instance):
    assert isinstance(instance, myDsl_logical_and_expression)

@given(instance=conditional_expression_strategy)
@settings(max_examples=50)
def test_conditional_expression_instantiation(instance):
    assert isinstance(instance, conditional_expression)

@given(instance=myDsl_logical_or_expression_strategy)
@settings(max_examples=50)
def test_mydsl_logical_or_expression_instantiation(instance):
    assert isinstance(instance, myDsl_logical_or_expression)

@given(instance=myDsl_initializer_strategy)
@settings(max_examples=50)
def test_mydsl_initializer_instantiation(instance):
    assert isinstance(instance, myDsl_initializer)

@given(instance=myDsl_init_declarator_listR_strategy)
@settings(max_examples=50)
def test_mydsl_init_declarator_listr_instantiation(instance):
    assert isinstance(instance, myDsl_init_declarator_listR)

@given(instance=myDsl_init_declarator_strategy)
@settings(max_examples=50)
def test_mydsl_init_declarator_instantiation(instance):
    assert isinstance(instance, myDsl_init_declarator)

@given(instance=myDsl_init_declarator_list_strategy)
@settings(max_examples=50)
def test_mydsl_init_declarator_list_instantiation(instance):
    assert isinstance(instance, myDsl_init_declarator_list)

@given(instance=parameter_declaration_strategy)
@settings(max_examples=50)
def test_parameter_declaration_instantiation(instance):
    assert isinstance(instance, parameter_declaration)

@given(instance=block_item_strategy)
@settings(max_examples=50)
def test_block_item_instantiation(instance):
    assert isinstance(instance, block_item)

@given(instance=myDsl_statement_strategy)
@settings(max_examples=50)
def test_mydsl_statement_instantiation(instance):
    assert isinstance(instance, myDsl_statement)

@given(instance=myDsl_block_item_listR_strategy)
@settings(max_examples=50)
def test_mydsl_block_item_listr_instantiation(instance):
    assert isinstance(instance, myDsl_block_item_listR)

@given(instance=myDsl_block_item_strategy)
@settings(max_examples=50)
def test_mydsl_block_item_instantiation(instance):
    assert isinstance(instance, myDsl_block_item)

@given(instance=compound_statement_strategy)
@settings(max_examples=50)
def test_compound_statement_instantiation(instance):
    assert isinstance(instance, compound_statement)

@given(instance=myDsl_block_item_list_strategy)
@settings(max_examples=50)
def test_mydsl_block_item_list_instantiation(instance):
    assert isinstance(instance, myDsl_block_item_list)

@given(instance=statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, statement)

@given(instance=myDsl_jump_statement_strategy)
@settings(max_examples=50)
def test_mydsl_jump_statement_instantiation(instance):
    assert isinstance(instance, myDsl_jump_statement)

@given(instance=myDsl_selection_statement_strategy)
@settings(max_examples=50)
def test_mydsl_selection_statement_instantiation(instance):
    assert isinstance(instance, myDsl_selection_statement)

@given(instance=myDsl_expression_statement_strategy)
@settings(max_examples=50)
def test_mydsl_expression_statement_instantiation(instance):
    assert isinstance(instance, myDsl_expression_statement)

@given(instance=myDsl_expression_strategy)
@settings(max_examples=50)
def test_mydsl_expression_instantiation(instance):
    assert isinstance(instance, myDsl_expression)

@given(instance=myDsl_iteration_statement_strategy)
@settings(max_examples=50)
def test_mydsl_iteration_statement_instantiation(instance):
    assert isinstance(instance, myDsl_iteration_statement)

@given(instance=myDsl_labeled_statement_strategy)
@settings(max_examples=50)
def test_mydsl_labeled_statement_instantiation(instance):
    assert isinstance(instance, myDsl_labeled_statement)

@given(instance=myDsl_parameter_listR_strategy)
@settings(max_examples=50)
def test_mydsl_parameter_listr_instantiation(instance):
    assert isinstance(instance, myDsl_parameter_listR)

@given(instance=myDsl_parameter_declaration_strategy)
@settings(max_examples=50)
def test_mydsl_parameter_declaration_instantiation(instance):
    assert isinstance(instance, myDsl_parameter_declaration)

@given(instance=parameter_type_list_strategy)
@settings(max_examples=50)
def test_parameter_type_list_instantiation(instance):
    assert isinstance(instance, parameter_type_list)

@given(instance=myDsl_parameter_list_strategy)
@settings(max_examples=50)
def test_mydsl_parameter_list_instantiation(instance):
    assert isinstance(instance, myDsl_parameter_list)

@given(instance=myDsl_identifier_listR_strategy)
@settings(max_examples=50)
def test_mydsl_identifier_listr_instantiation(instance):
    assert isinstance(instance, myDsl_identifier_listR)

@given(instance=myDsl_declaration_listR_strategy)
@settings(max_examples=50)
def test_mydsl_declaration_listr_instantiation(instance):
    assert isinstance(instance, myDsl_declaration_listR)

@given(instance=myDsl_abstract_declarator_strategy)
@settings(max_examples=50)
def test_mydsl_abstract_declarator_instantiation(instance):
    assert isinstance(instance, myDsl_abstract_declarator)

@given(instance=myDsl_type_qualifier_listR_strategy)
@settings(max_examples=50)
def test_mydsl_type_qualifier_listr_instantiation(instance):
    assert isinstance(instance, myDsl_type_qualifier_listR)



@given(instance=myDsl_type_qualifier_listR_strategy)
def test_mydsl_type_qualifier_listr_Type_qualifier_setter(instance):
    original = instance.Type_qualifier
    instance.Type_qualifier = original
    assert instance.Type_qualifier == original

@given(instance=pointer_strategy)
@settings(max_examples=50)
def test_pointer_instantiation(instance):
    assert isinstance(instance, pointer)

@given(instance=myDsl_type_qualifier_list_strategy)
@settings(max_examples=50)
def test_mydsl_type_qualifier_list_instantiation(instance):
    assert isinstance(instance, myDsl_type_qualifier_list)



@given(instance=myDsl_type_qualifier_list_strategy)
def test_mydsl_type_qualifier_list_Type_qualifier_setter(instance):
    original = instance.Type_qualifier
    instance.Type_qualifier = original
    assert instance.Type_qualifier == original

@given(instance=myDsl_pointer_strategy)
@settings(max_examples=50)
def test_mydsl_pointer_instantiation(instance):
    assert isinstance(instance, myDsl_pointer)

@given(instance=struct_declarator_strategy)
@settings(max_examples=50)
def test_struct_declarator_instantiation(instance):
    assert isinstance(instance, struct_declarator)

@given(instance=myDsl_constant_expression_strategy)
@settings(max_examples=50)
def test_mydsl_constant_expression_instantiation(instance):
    assert isinstance(instance, myDsl_constant_expression)

@given(instance=init_declarator_strategy)
@settings(max_examples=50)
def test_init_declarator_instantiation(instance):
    assert isinstance(instance, init_declarator)

@given(instance=myDsl_compound_statement_strategy)
@settings(max_examples=50)
def test_mydsl_compound_statement_instantiation(instance):
    assert isinstance(instance, myDsl_compound_statement)

@given(instance=myDsl_identifier_list_strategy)
@settings(max_examples=50)
def test_mydsl_identifier_list_instantiation(instance):
    assert isinstance(instance, myDsl_identifier_list)

@given(instance=myDsl_parameter_type_list_strategy)
@settings(max_examples=50)
def test_mydsl_parameter_type_list_instantiation(instance):
    assert isinstance(instance, myDsl_parameter_type_list)

@given(instance=myDsl_assignment_expression_strategy)
@settings(max_examples=50)
def test_mydsl_assignment_expression_instantiation(instance):
    assert isinstance(instance, myDsl_assignment_expression)



@given(instance=myDsl_assignment_expression_strategy)
def test_mydsl_assignment_expression_Assignment_operator_setter(instance):
    original = instance.Assignment_operator
    instance.Assignment_operator = original
    assert instance.Assignment_operator == original

@given(instance=myDsl_direct_declaratorR_strategy)
@settings(max_examples=50)
def test_mydsl_direct_declaratorr_instantiation(instance):
    assert isinstance(instance, myDsl_direct_declaratorR)

@given(instance=declarator_strategy)
@settings(max_examples=50)
def test_declarator_instantiation(instance):
    assert isinstance(instance, declarator)

@given(instance=myDsl_direct_declarator_strategy)
@settings(max_examples=50)
def test_mydsl_direct_declarator_instantiation(instance):
    assert isinstance(instance, myDsl_direct_declarator)

@given(instance=myDsl_external_declaration_strategy)
@settings(max_examples=50)
def test_mydsl_external_declaration_instantiation(instance):
    assert isinstance(instance, myDsl_external_declaration)

@given(instance=myDsl_translation_unit_strategy)
@settings(max_examples=50)
def test_mydsl_translation_unit_instantiation(instance):
    assert isinstance(instance, myDsl_translation_unit)

@given(instance=myDsl_Model_strategy)
@settings(max_examples=50)
def test_mydsl_model_instantiation(instance):
    assert isinstance(instance, myDsl_Model)

@given(instance=myDsl_declaration_list_strategy)
@settings(max_examples=50)
def test_mydsl_declaration_list_instantiation(instance):
    assert isinstance(instance, myDsl_declaration_list)

@given(instance=myDsl_declarator_strategy)
@settings(max_examples=50)
def test_mydsl_declarator_instantiation(instance):
    assert isinstance(instance, myDsl_declarator)

@given(instance=external_declaration_strategy)
@settings(max_examples=50)
def test_external_declaration_instantiation(instance):
    assert isinstance(instance, external_declaration)

@given(instance=myDsl_declaration_strategy)
@settings(max_examples=50)
def test_mydsl_declaration_instantiation(instance):
    assert isinstance(instance, myDsl_declaration)

@given(instance=myDsl_function_definition_strategy)
@settings(max_examples=50)
def test_mydsl_function_definition_instantiation(instance):
    assert isinstance(instance, myDsl_function_definition)

@given(instance=myDsl_declaration_specifiers_strategy)
@settings(max_examples=50)
def test_mydsl_declaration_specifiers_instantiation(instance):
    assert isinstance(instance, myDsl_declaration_specifiers)



@given(instance=myDsl_declaration_specifiers_strategy)
def test_mydsl_declaration_specifiers_Storage_class_specifier_setter(instance):
    original = instance.Storage_class_specifier
    instance.Storage_class_specifier = original
    assert instance.Storage_class_specifier == original



@given(instance=myDsl_declaration_specifiers_strategy)
def test_mydsl_declaration_specifiers_Type_qualifier_setter(instance):
    original = instance.Type_qualifier
    instance.Type_qualifier = original
    assert instance.Type_qualifier == original

@given(instance=myDsl_translation_unitR_strategy)
@settings(max_examples=50)
def test_mydsl_translation_unitr_instantiation(instance):
    assert isinstance(instance, myDsl_translation_unitR)
