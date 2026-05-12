import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ansic_relational_expression,
    ansic_shift_expression_complement,
    ansic_shift_expression_linha,
    ansic_shift_expression,
    ansic_designator_list_linha,
    ansic_designator,
    ansic_designator_list,
    ansic_additive_expression,
    ansic_multiplicative_expression_complement,
    ansic_multiplicative_expression_linha,
    ansic_multiplicative_expression,
    ansic_cast_expression,
    ansic_unary_expression,
    ansic_argument_expression_list_linha,
    ansic_argument_expression_list,
    ansic_postfix_expression_complement,
    ansic_conditional_expression,
    ansic_primary_expression,
    ansic_identifier_list_linha,
    ansic_initializer_list_complement,
    ansic_initializer_list_linha,
    ansic_init_declarator_list_linha,
    ansic_designation,
    ansic_postfix_expression_linha,
    ansic_postfix_expression,
    ansic_generic_assoc_list_linha,
    ansic_generic_association,
    ansic_generic_assoc_list,
    ansic_generic_selection,
    ansic_expression,
    ansic_constant,
    ansic_parameter_type_list,
    ansic_assignment_expression,
    ansic_direct_abstract_declarator_complement,
    ansic_initializer_list,
    ansic_initializer,
    ansic_direct_abstract_declarator_linha,
    ansic_direct_abstract_declarator,
    ansic_abstract_declarator,
    ansic_parameter_list_linha,
    ansic_parameter_declaration,
    ansic_parameter_lista,
    ansic_identifier_list,
    ansic_direct_declarator_complemento,
    ansic_direct_declarator_linha,
    ansic_type_qualifier_list_linha,
    direct_abstract_declarator_complement,
    ansic_type_qualifier_list,
    ansic_direct_declarator,
    ansic_pointer,
    ansic_declaration_list_linha,
    ansic_compound_statement,
    ansic_declaration_list,
    ansic_init_declarator_list,
    ansic_struct_declaration_list,
    ansic_declarator,
    ansic_struct_declarator_list_linha,
    ansic_struct_declarator,
    ansic_static_assert_declaration,
    ansic_struct_declarator_list,
    ansic_specifier_qualifier_list,
    ansic_struct_declaration_list_linha,
    ansic_struct_declaration,
    ansic_struct_or_union_specifier_complement,
    ansic_declaration,
    ansic_function_definition,
    ansic_translation_unit_linha,
    ansic_enumeration_constant,
    ansic_enumerator_list_linha,
    ansic_enumerator,
    ansic_enumerator_list,
    ansic_enum_specifier,
    ansic_struct_or_union_specifier,
    ansic_atomic_type_specifier,
    ansic_constant_expression,
    ansic_alignment_specifier,
    ansic_type_qualifier,
    ansic_type_specifier,
    ansic_declaration_specifiers,
    ansic_external_declaration,
    ansic_translation_unit,
    ansic_DomainModel,
    translation_unit_linha,
    ansic_TranlationUnitLinhaAction,
    init_declarator_list_linha,
    ansic_InitDecclaratorListLinhaAction,
    unary_expression,
    ansic_PlusPlus,
    argument_expression_list_linha,
    ansic_ArgumentExpressionListLinhaAction,
    postfix_expression_complement,
    ansic_PostFixEmpryParams,
    designator_list_linha,
    ansic_DesignatorListLinhaAction,
    initializer_list_linha,
    ansic_InitializerListLinhaAction,
    postfix_expression_linha,
    ansic_PostfixExpressionLinhaAction,
    generic_assoc_list_linha,
    ansic_GenericAssocListLinhaAction,
    ansic_string_ufcg,
    identifier_list_linha,
    ansic_IdentifierListLinhaAction,
    direct_abstract_declarator_linha,
    ansic_DirectAbstractDeclarratorLinhaAction,
    type_qualifier_list_linha,
    ansic_TypeQualifierListLinhaAtion,
    declaration_list_linha,
    ansic_DeclarationListLinhaAction,
    struct_declarator_list_linha,
    ansic_StructDeclaratorListLinhaAction,
    struct_declaration_list_linha,
    ansic_StructDeclarationListLinhaAction,
    struct_or_union_specifier_complement,
    ansic_StructOrUnionSpecifierComplementAction,
    enumerator_list_linha,
    ansic_EnumeratorListLinhaAction,
    ansic_init_declarator,
    ansic_expression_linha,
    postfix_expression,
    ansic_type_name,
    ansic_conditional_expression_linha,
    ansic_logical_or_expression_linha,
    ansic_logical_or_expression,
    ansic_logical_and_expression_linha,
    ansic_logical_and_expression,
    ansic_inclusive_or_expression_linha,
    ansic_inclusive_or_expression,
    ansic_exclusive_or_expression_linha,
    ansic_exclusive_or_expression,
    ansic_and_expression_linha,
    ansic_and_expression,
    ansic_jump_statement,
    ansic_iteration_statement,
    ansic_block_item_list_linha,
    ansic_block_item,
    ansic_block_item_list,
    ansic_additive_expression_complement,
    ansic_additive_expression_linha,
    ansic_selection_statement,
    ansic_expression_statement,
    ansic_labeled_statement,
    ansic_statement,
    ansic_equality_expression_complement,
    ansic_equality_expression_linha,
    ansic_equality_expression,
    ansic_relational_expression_complement,
    ansic_relational_expression_linha,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ansic_relational_expression_is_not_abstract():
    assert not inspect.isabstract(ansic_relational_expression)


def test_ansic_relational_expression_constructor_exists():
    assert callable(ansic_relational_expression.__init__)


def test_ansic_relational_expression_constructor_args():
    sig = inspect.signature(ansic_relational_expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic_shift_expression_complement_is_not_abstract():
    assert not inspect.isabstract(ansic_shift_expression_complement)


def test_ansic_shift_expression_complement_constructor_exists():
    assert callable(ansic_shift_expression_complement.__init__)


def test_ansic_shift_expression_complement_constructor_args():
    sig = inspect.signature(ansic_shift_expression_complement.__init__)
    params = list(sig.parameters.keys())



def test_ansic_shift_expression_linha_is_not_abstract():
    assert not inspect.isabstract(ansic_shift_expression_linha)


def test_ansic_shift_expression_linha_constructor_exists():
    assert callable(ansic_shift_expression_linha.__init__)


def test_ansic_shift_expression_linha_constructor_args():
    sig = inspect.signature(ansic_shift_expression_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_shift_expression_is_not_abstract():
    assert not inspect.isabstract(ansic_shift_expression)


def test_ansic_shift_expression_constructor_exists():
    assert callable(ansic_shift_expression.__init__)


def test_ansic_shift_expression_constructor_args():
    sig = inspect.signature(ansic_shift_expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic_designator_list_linha_is_not_abstract():
    assert not inspect.isabstract(ansic_designator_list_linha)


def test_ansic_designator_list_linha_constructor_exists():
    assert callable(ansic_designator_list_linha.__init__)


def test_ansic_designator_list_linha_constructor_args():
    sig = inspect.signature(ansic_designator_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_designator_is_not_abstract():
    assert not inspect.isabstract(ansic_designator)


def test_ansic_designator_constructor_exists():
    assert callable(ansic_designator.__init__)


def test_ansic_designator_constructor_args():
    sig = inspect.signature(ansic_designator.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_ansic_designator_has_identifier():
    assert hasattr(ansic_designator, "identifier")
    descriptor = None
    for klass in ansic_designator.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_ansic_designator_list_is_not_abstract():
    assert not inspect.isabstract(ansic_designator_list)


def test_ansic_designator_list_constructor_exists():
    assert callable(ansic_designator_list.__init__)


def test_ansic_designator_list_constructor_args():
    sig = inspect.signature(ansic_designator_list.__init__)
    params = list(sig.parameters.keys())



def test_ansic_additive_expression_is_not_abstract():
    assert not inspect.isabstract(ansic_additive_expression)


def test_ansic_additive_expression_constructor_exists():
    assert callable(ansic_additive_expression.__init__)


def test_ansic_additive_expression_constructor_args():
    sig = inspect.signature(ansic_additive_expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic_multiplicative_expression_complement_is_not_abstract():
    assert not inspect.isabstract(ansic_multiplicative_expression_complement)


def test_ansic_multiplicative_expression_complement_constructor_exists():
    assert callable(ansic_multiplicative_expression_complement.__init__)


def test_ansic_multiplicative_expression_complement_constructor_args():
    sig = inspect.signature(ansic_multiplicative_expression_complement.__init__)
    params = list(sig.parameters.keys())



def test_ansic_multiplicative_expression_linha_is_not_abstract():
    assert not inspect.isabstract(ansic_multiplicative_expression_linha)


def test_ansic_multiplicative_expression_linha_constructor_exists():
    assert callable(ansic_multiplicative_expression_linha.__init__)


def test_ansic_multiplicative_expression_linha_constructor_args():
    sig = inspect.signature(ansic_multiplicative_expression_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_multiplicative_expression_is_not_abstract():
    assert not inspect.isabstract(ansic_multiplicative_expression)


def test_ansic_multiplicative_expression_constructor_exists():
    assert callable(ansic_multiplicative_expression.__init__)


def test_ansic_multiplicative_expression_constructor_args():
    sig = inspect.signature(ansic_multiplicative_expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic_cast_expression_is_not_abstract():
    assert not inspect.isabstract(ansic_cast_expression)


def test_ansic_cast_expression_constructor_exists():
    assert callable(ansic_cast_expression.__init__)


def test_ansic_cast_expression_constructor_args():
    sig = inspect.signature(ansic_cast_expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic_unary_expression_is_not_abstract():
    assert not inspect.isabstract(ansic_unary_expression)


def test_ansic_unary_expression_constructor_exists():
    assert callable(ansic_unary_expression.__init__)


def test_ansic_unary_expression_constructor_args():
    sig = inspect.signature(ansic_unary_expression.__init__)
    params = list(sig.parameters.keys())
    assert "unary_operator" in params, "Missing parameter 'unary_operator'"

def test_ansic_unary_expression_has_unary_operator():
    assert hasattr(ansic_unary_expression, "unary_operator")
    descriptor = None
    for klass in ansic_unary_expression.__mro__:
        if "unary_operator" in klass.__dict__:
            descriptor = klass.__dict__["unary_operator"]
            break
    assert isinstance(descriptor, property)



def test_ansic_argument_expression_list_linha_is_not_abstract():
    assert not inspect.isabstract(ansic_argument_expression_list_linha)


def test_ansic_argument_expression_list_linha_constructor_exists():
    assert callable(ansic_argument_expression_list_linha.__init__)


def test_ansic_argument_expression_list_linha_constructor_args():
    sig = inspect.signature(ansic_argument_expression_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_argument_expression_list_is_not_abstract():
    assert not inspect.isabstract(ansic_argument_expression_list)


def test_ansic_argument_expression_list_constructor_exists():
    assert callable(ansic_argument_expression_list.__init__)


def test_ansic_argument_expression_list_constructor_args():
    sig = inspect.signature(ansic_argument_expression_list.__init__)
    params = list(sig.parameters.keys())



def test_ansic_postfix_expression_complement_is_not_abstract():
    assert not inspect.isabstract(ansic_postfix_expression_complement)


def test_ansic_postfix_expression_complement_constructor_exists():
    assert callable(ansic_postfix_expression_complement.__init__)


def test_ansic_postfix_expression_complement_constructor_args():
    sig = inspect.signature(ansic_postfix_expression_complement.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_ansic_postfix_expression_complement_has_identifier():
    assert hasattr(ansic_postfix_expression_complement, "identifier")
    descriptor = None
    for klass in ansic_postfix_expression_complement.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_ansic_conditional_expression_is_not_abstract():
    assert not inspect.isabstract(ansic_conditional_expression)


def test_ansic_conditional_expression_constructor_exists():
    assert callable(ansic_conditional_expression.__init__)


def test_ansic_conditional_expression_constructor_args():
    sig = inspect.signature(ansic_conditional_expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic_primary_expression_is_not_abstract():
    assert not inspect.isabstract(ansic_primary_expression)


def test_ansic_primary_expression_constructor_exists():
    assert callable(ansic_primary_expression.__init__)


def test_ansic_primary_expression_constructor_args():
    sig = inspect.signature(ansic_primary_expression.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_ansic_primary_expression_has_identifier():
    assert hasattr(ansic_primary_expression, "identifier")
    descriptor = None
    for klass in ansic_primary_expression.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_ansic_identifier_list_linha_is_not_abstract():
    assert not inspect.isabstract(ansic_identifier_list_linha)


def test_ansic_identifier_list_linha_constructor_exists():
    assert callable(ansic_identifier_list_linha.__init__)


def test_ansic_identifier_list_linha_constructor_args():
    sig = inspect.signature(ansic_identifier_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_initializer_list_complement_is_not_abstract():
    assert not inspect.isabstract(ansic_initializer_list_complement)


def test_ansic_initializer_list_complement_constructor_exists():
    assert callable(ansic_initializer_list_complement.__init__)


def test_ansic_initializer_list_complement_constructor_args():
    sig = inspect.signature(ansic_initializer_list_complement.__init__)
    params = list(sig.parameters.keys())



def test_ansic_initializer_list_linha_is_not_abstract():
    assert not inspect.isabstract(ansic_initializer_list_linha)


def test_ansic_initializer_list_linha_constructor_exists():
    assert callable(ansic_initializer_list_linha.__init__)


def test_ansic_initializer_list_linha_constructor_args():
    sig = inspect.signature(ansic_initializer_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_init_declarator_list_linha_is_not_abstract():
    assert not inspect.isabstract(ansic_init_declarator_list_linha)


def test_ansic_init_declarator_list_linha_constructor_exists():
    assert callable(ansic_init_declarator_list_linha.__init__)


def test_ansic_init_declarator_list_linha_constructor_args():
    sig = inspect.signature(ansic_init_declarator_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_designation_is_not_abstract():
    assert not inspect.isabstract(ansic_designation)


def test_ansic_designation_constructor_exists():
    assert callable(ansic_designation.__init__)


def test_ansic_designation_constructor_args():
    sig = inspect.signature(ansic_designation.__init__)
    params = list(sig.parameters.keys())



def test_ansic_postfix_expression_linha_is_not_abstract():
    assert not inspect.isabstract(ansic_postfix_expression_linha)


def test_ansic_postfix_expression_linha_constructor_exists():
    assert callable(ansic_postfix_expression_linha.__init__)


def test_ansic_postfix_expression_linha_constructor_args():
    sig = inspect.signature(ansic_postfix_expression_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_postfix_expression_is_not_abstract():
    assert not inspect.isabstract(ansic_postfix_expression)


def test_ansic_postfix_expression_constructor_exists():
    assert callable(ansic_postfix_expression.__init__)


def test_ansic_postfix_expression_constructor_args():
    sig = inspect.signature(ansic_postfix_expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic_generic_assoc_list_linha_is_not_abstract():
    assert not inspect.isabstract(ansic_generic_assoc_list_linha)


def test_ansic_generic_assoc_list_linha_constructor_exists():
    assert callable(ansic_generic_assoc_list_linha.__init__)


def test_ansic_generic_assoc_list_linha_constructor_args():
    sig = inspect.signature(ansic_generic_assoc_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_generic_association_is_not_abstract():
    assert not inspect.isabstract(ansic_generic_association)


def test_ansic_generic_association_constructor_exists():
    assert callable(ansic_generic_association.__init__)


def test_ansic_generic_association_constructor_args():
    sig = inspect.signature(ansic_generic_association.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_ansic_generic_association_has_default():
    assert hasattr(ansic_generic_association, "default")
    descriptor = None
    for klass in ansic_generic_association.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_ansic_generic_assoc_list_is_not_abstract():
    assert not inspect.isabstract(ansic_generic_assoc_list)


def test_ansic_generic_assoc_list_constructor_exists():
    assert callable(ansic_generic_assoc_list.__init__)


def test_ansic_generic_assoc_list_constructor_args():
    sig = inspect.signature(ansic_generic_assoc_list.__init__)
    params = list(sig.parameters.keys())



def test_ansic_generic_selection_is_not_abstract():
    assert not inspect.isabstract(ansic_generic_selection)


def test_ansic_generic_selection_constructor_exists():
    assert callable(ansic_generic_selection.__init__)


def test_ansic_generic_selection_constructor_args():
    sig = inspect.signature(ansic_generic_selection.__init__)
    params = list(sig.parameters.keys())
    assert "_generic" in params, "Missing parameter '_generic'"

def test_ansic_generic_selection_has__generic():
    assert hasattr(ansic_generic_selection, "_generic")
    descriptor = None
    for klass in ansic_generic_selection.__mro__:
        if "_generic" in klass.__dict__:
            descriptor = klass.__dict__["_generic"]
            break
    assert isinstance(descriptor, property)



def test_ansic_expression_is_not_abstract():
    assert not inspect.isabstract(ansic_expression)


def test_ansic_expression_constructor_exists():
    assert callable(ansic_expression.__init__)


def test_ansic_expression_constructor_args():
    sig = inspect.signature(ansic_expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic_constant_is_not_abstract():
    assert not inspect.isabstract(ansic_constant)


def test_ansic_constant_constructor_exists():
    assert callable(ansic_constant.__init__)


def test_ansic_constant_constructor_args():
    sig = inspect.signature(ansic_constant.__init__)
    params = list(sig.parameters.keys())
    assert "enumz" in params, "Missing parameter 'enumz'"
    assert "f_constant" in params, "Missing parameter 'f_constant'"
    assert "char" in params, "Missing parameter 'char'"
    assert "i_constant" in params, "Missing parameter 'i_constant'"

def test_ansic_constant_has_enumz():
    assert hasattr(ansic_constant, "enumz")
    descriptor = None
    for klass in ansic_constant.__mro__:
        if "enumz" in klass.__dict__:
            descriptor = klass.__dict__["enumz"]
            break
    assert isinstance(descriptor, property)

def test_ansic_constant_has_f_constant():
    assert hasattr(ansic_constant, "f_constant")
    descriptor = None
    for klass in ansic_constant.__mro__:
        if "f_constant" in klass.__dict__:
            descriptor = klass.__dict__["f_constant"]
            break
    assert isinstance(descriptor, property)

def test_ansic_constant_has_char():
    assert hasattr(ansic_constant, "char")
    descriptor = None
    for klass in ansic_constant.__mro__:
        if "char" in klass.__dict__:
            descriptor = klass.__dict__["char"]
            break
    assert isinstance(descriptor, property)

def test_ansic_constant_has_i_constant():
    assert hasattr(ansic_constant, "i_constant")
    descriptor = None
    for klass in ansic_constant.__mro__:
        if "i_constant" in klass.__dict__:
            descriptor = klass.__dict__["i_constant"]
            break
    assert isinstance(descriptor, property)



def test_ansic_parameter_type_list_is_not_abstract():
    assert not inspect.isabstract(ansic_parameter_type_list)


def test_ansic_parameter_type_list_constructor_exists():
    assert callable(ansic_parameter_type_list.__init__)


def test_ansic_parameter_type_list_constructor_args():
    sig = inspect.signature(ansic_parameter_type_list.__init__)
    params = list(sig.parameters.keys())



def test_ansic_assignment_expression_is_not_abstract():
    assert not inspect.isabstract(ansic_assignment_expression)


def test_ansic_assignment_expression_constructor_exists():
    assert callable(ansic_assignment_expression.__init__)


def test_ansic_assignment_expression_constructor_args():
    sig = inspect.signature(ansic_assignment_expression.__init__)
    params = list(sig.parameters.keys())
    assert "assignment_operator" in params, "Missing parameter 'assignment_operator'"

def test_ansic_assignment_expression_has_assignment_operator():
    assert hasattr(ansic_assignment_expression, "assignment_operator")
    descriptor = None
    for klass in ansic_assignment_expression.__mro__:
        if "assignment_operator" in klass.__dict__:
            descriptor = klass.__dict__["assignment_operator"]
            break
    assert isinstance(descriptor, property)



def test_ansic_direct_abstract_declarator_complement_is_not_abstract():
    assert not inspect.isabstract(ansic_direct_abstract_declarator_complement)


def test_ansic_direct_abstract_declarator_complement_constructor_exists():
    assert callable(ansic_direct_abstract_declarator_complement.__init__)


def test_ansic_direct_abstract_declarator_complement_constructor_args():
    sig = inspect.signature(ansic_direct_abstract_declarator_complement.__init__)
    params = list(sig.parameters.keys())



def test_ansic_initializer_list_is_not_abstract():
    assert not inspect.isabstract(ansic_initializer_list)


def test_ansic_initializer_list_constructor_exists():
    assert callable(ansic_initializer_list.__init__)


def test_ansic_initializer_list_constructor_args():
    sig = inspect.signature(ansic_initializer_list.__init__)
    params = list(sig.parameters.keys())



def test_ansic_initializer_is_not_abstract():
    assert not inspect.isabstract(ansic_initializer)


def test_ansic_initializer_constructor_exists():
    assert callable(ansic_initializer.__init__)


def test_ansic_initializer_constructor_args():
    sig = inspect.signature(ansic_initializer.__init__)
    params = list(sig.parameters.keys())



def test_ansic_direct_abstract_declarator_linha_is_not_abstract():
    assert not inspect.isabstract(ansic_direct_abstract_declarator_linha)


def test_ansic_direct_abstract_declarator_linha_constructor_exists():
    assert callable(ansic_direct_abstract_declarator_linha.__init__)


def test_ansic_direct_abstract_declarator_linha_constructor_args():
    sig = inspect.signature(ansic_direct_abstract_declarator_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_direct_abstract_declarator_is_not_abstract():
    assert not inspect.isabstract(ansic_direct_abstract_declarator)


def test_ansic_direct_abstract_declarator_constructor_exists():
    assert callable(ansic_direct_abstract_declarator.__init__)


def test_ansic_direct_abstract_declarator_constructor_args():
    sig = inspect.signature(ansic_direct_abstract_declarator.__init__)
    params = list(sig.parameters.keys())



def test_ansic_abstract_declarator_is_not_abstract():
    assert not inspect.isabstract(ansic_abstract_declarator)


def test_ansic_abstract_declarator_constructor_exists():
    assert callable(ansic_abstract_declarator.__init__)


def test_ansic_abstract_declarator_constructor_args():
    sig = inspect.signature(ansic_abstract_declarator.__init__)
    params = list(sig.parameters.keys())



def test_ansic_parameter_list_linha_is_not_abstract():
    assert not inspect.isabstract(ansic_parameter_list_linha)


def test_ansic_parameter_list_linha_constructor_exists():
    assert callable(ansic_parameter_list_linha.__init__)


def test_ansic_parameter_list_linha_constructor_args():
    sig = inspect.signature(ansic_parameter_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_parameter_declaration_is_not_abstract():
    assert not inspect.isabstract(ansic_parameter_declaration)


def test_ansic_parameter_declaration_constructor_exists():
    assert callable(ansic_parameter_declaration.__init__)


def test_ansic_parameter_declaration_constructor_args():
    sig = inspect.signature(ansic_parameter_declaration.__init__)
    params = list(sig.parameters.keys())



def test_ansic_parameter_lista_is_not_abstract():
    assert not inspect.isabstract(ansic_parameter_lista)


def test_ansic_parameter_lista_constructor_exists():
    assert callable(ansic_parameter_lista.__init__)


def test_ansic_parameter_lista_constructor_args():
    sig = inspect.signature(ansic_parameter_lista.__init__)
    params = list(sig.parameters.keys())



def test_ansic_identifier_list_is_not_abstract():
    assert not inspect.isabstract(ansic_identifier_list)


def test_ansic_identifier_list_constructor_exists():
    assert callable(ansic_identifier_list.__init__)


def test_ansic_identifier_list_constructor_args():
    sig = inspect.signature(ansic_identifier_list.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_ansic_identifier_list_has_identifier():
    assert hasattr(ansic_identifier_list, "identifier")
    descriptor = None
    for klass in ansic_identifier_list.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_ansic_direct_declarator_complemento_is_not_abstract():
    assert not inspect.isabstract(ansic_direct_declarator_complemento)


def test_ansic_direct_declarator_complemento_constructor_exists():
    assert callable(ansic_direct_declarator_complemento.__init__)


def test_ansic_direct_declarator_complemento_constructor_args():
    sig = inspect.signature(ansic_direct_declarator_complemento.__init__)
    params = list(sig.parameters.keys())



def test_ansic_direct_declarator_linha_is_not_abstract():
    assert not inspect.isabstract(ansic_direct_declarator_linha)


def test_ansic_direct_declarator_linha_constructor_exists():
    assert callable(ansic_direct_declarator_linha.__init__)


def test_ansic_direct_declarator_linha_constructor_args():
    sig = inspect.signature(ansic_direct_declarator_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_type_qualifier_list_linha_is_not_abstract():
    assert not inspect.isabstract(ansic_type_qualifier_list_linha)


def test_ansic_type_qualifier_list_linha_constructor_exists():
    assert callable(ansic_type_qualifier_list_linha.__init__)


def test_ansic_type_qualifier_list_linha_constructor_args():
    sig = inspect.signature(ansic_type_qualifier_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_direct_abstract_declarator_complement_is_not_abstract():
    assert not inspect.isabstract(direct_abstract_declarator_complement)


def test_direct_abstract_declarator_complement_constructor_exists():
    assert callable(direct_abstract_declarator_complement.__init__)


def test_direct_abstract_declarator_complement_constructor_args():
    sig = inspect.signature(direct_abstract_declarator_complement.__init__)
    params = list(sig.parameters.keys())



def test_ansic_type_qualifier_list_is_not_abstract():
    assert not inspect.isabstract(ansic_type_qualifier_list)


def test_ansic_type_qualifier_list_constructor_exists():
    assert callable(ansic_type_qualifier_list.__init__)


def test_ansic_type_qualifier_list_constructor_args():
    sig = inspect.signature(ansic_type_qualifier_list.__init__)
    params = list(sig.parameters.keys())



def test_ansic_direct_declarator_is_not_abstract():
    assert not inspect.isabstract(ansic_direct_declarator)


def test_ansic_direct_declarator_constructor_exists():
    assert callable(ansic_direct_declarator.__init__)


def test_ansic_direct_declarator_constructor_args():
    sig = inspect.signature(ansic_direct_declarator.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_ansic_direct_declarator_has_identifier():
    assert hasattr(ansic_direct_declarator, "identifier")
    descriptor = None
    for klass in ansic_direct_declarator.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_ansic_pointer_is_not_abstract():
    assert not inspect.isabstract(ansic_pointer)


def test_ansic_pointer_constructor_exists():
    assert callable(ansic_pointer.__init__)


def test_ansic_pointer_constructor_args():
    sig = inspect.signature(ansic_pointer.__init__)
    params = list(sig.parameters.keys())



def test_ansic_declaration_list_linha_is_not_abstract():
    assert not inspect.isabstract(ansic_declaration_list_linha)


def test_ansic_declaration_list_linha_constructor_exists():
    assert callable(ansic_declaration_list_linha.__init__)


def test_ansic_declaration_list_linha_constructor_args():
    sig = inspect.signature(ansic_declaration_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_compound_statement_is_not_abstract():
    assert not inspect.isabstract(ansic_compound_statement)


def test_ansic_compound_statement_constructor_exists():
    assert callable(ansic_compound_statement.__init__)


def test_ansic_compound_statement_constructor_args():
    sig = inspect.signature(ansic_compound_statement.__init__)
    params = list(sig.parameters.keys())



def test_ansic_declaration_list_is_not_abstract():
    assert not inspect.isabstract(ansic_declaration_list)


def test_ansic_declaration_list_constructor_exists():
    assert callable(ansic_declaration_list.__init__)


def test_ansic_declaration_list_constructor_args():
    sig = inspect.signature(ansic_declaration_list.__init__)
    params = list(sig.parameters.keys())



def test_ansic_init_declarator_list_is_not_abstract():
    assert not inspect.isabstract(ansic_init_declarator_list)


def test_ansic_init_declarator_list_constructor_exists():
    assert callable(ansic_init_declarator_list.__init__)


def test_ansic_init_declarator_list_constructor_args():
    sig = inspect.signature(ansic_init_declarator_list.__init__)
    params = list(sig.parameters.keys())



def test_ansic_struct_declaration_list_is_not_abstract():
    assert not inspect.isabstract(ansic_struct_declaration_list)


def test_ansic_struct_declaration_list_constructor_exists():
    assert callable(ansic_struct_declaration_list.__init__)


def test_ansic_struct_declaration_list_constructor_args():
    sig = inspect.signature(ansic_struct_declaration_list.__init__)
    params = list(sig.parameters.keys())



def test_ansic_declarator_is_not_abstract():
    assert not inspect.isabstract(ansic_declarator)


def test_ansic_declarator_constructor_exists():
    assert callable(ansic_declarator.__init__)


def test_ansic_declarator_constructor_args():
    sig = inspect.signature(ansic_declarator.__init__)
    params = list(sig.parameters.keys())



def test_ansic_struct_declarator_list_linha_is_not_abstract():
    assert not inspect.isabstract(ansic_struct_declarator_list_linha)


def test_ansic_struct_declarator_list_linha_constructor_exists():
    assert callable(ansic_struct_declarator_list_linha.__init__)


def test_ansic_struct_declarator_list_linha_constructor_args():
    sig = inspect.signature(ansic_struct_declarator_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_struct_declarator_is_not_abstract():
    assert not inspect.isabstract(ansic_struct_declarator)


def test_ansic_struct_declarator_constructor_exists():
    assert callable(ansic_struct_declarator.__init__)


def test_ansic_struct_declarator_constructor_args():
    sig = inspect.signature(ansic_struct_declarator.__init__)
    params = list(sig.parameters.keys())



def test_ansic_static_assert_declaration_is_not_abstract():
    assert not inspect.isabstract(ansic_static_assert_declaration)


def test_ansic_static_assert_declaration_constructor_exists():
    assert callable(ansic_static_assert_declaration.__init__)


def test_ansic_static_assert_declaration_constructor_args():
    sig = inspect.signature(ansic_static_assert_declaration.__init__)
    params = list(sig.parameters.keys())



def test_ansic_struct_declarator_list_is_not_abstract():
    assert not inspect.isabstract(ansic_struct_declarator_list)


def test_ansic_struct_declarator_list_constructor_exists():
    assert callable(ansic_struct_declarator_list.__init__)


def test_ansic_struct_declarator_list_constructor_args():
    sig = inspect.signature(ansic_struct_declarator_list.__init__)
    params = list(sig.parameters.keys())



def test_ansic_specifier_qualifier_list_is_not_abstract():
    assert not inspect.isabstract(ansic_specifier_qualifier_list)


def test_ansic_specifier_qualifier_list_constructor_exists():
    assert callable(ansic_specifier_qualifier_list.__init__)


def test_ansic_specifier_qualifier_list_constructor_args():
    sig = inspect.signature(ansic_specifier_qualifier_list.__init__)
    params = list(sig.parameters.keys())



def test_ansic_struct_declaration_list_linha_is_not_abstract():
    assert not inspect.isabstract(ansic_struct_declaration_list_linha)


def test_ansic_struct_declaration_list_linha_constructor_exists():
    assert callable(ansic_struct_declaration_list_linha.__init__)


def test_ansic_struct_declaration_list_linha_constructor_args():
    sig = inspect.signature(ansic_struct_declaration_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_struct_declaration_is_not_abstract():
    assert not inspect.isabstract(ansic_struct_declaration)


def test_ansic_struct_declaration_constructor_exists():
    assert callable(ansic_struct_declaration.__init__)


def test_ansic_struct_declaration_constructor_args():
    sig = inspect.signature(ansic_struct_declaration.__init__)
    params = list(sig.parameters.keys())



def test_ansic_struct_or_union_specifier_complement_is_not_abstract():
    assert not inspect.isabstract(ansic_struct_or_union_specifier_complement)


def test_ansic_struct_or_union_specifier_complement_constructor_exists():
    assert callable(ansic_struct_or_union_specifier_complement.__init__)


def test_ansic_struct_or_union_specifier_complement_constructor_args():
    sig = inspect.signature(ansic_struct_or_union_specifier_complement.__init__)
    params = list(sig.parameters.keys())



def test_ansic_declaration_is_not_abstract():
    assert not inspect.isabstract(ansic_declaration)


def test_ansic_declaration_constructor_exists():
    assert callable(ansic_declaration.__init__)


def test_ansic_declaration_constructor_args():
    sig = inspect.signature(ansic_declaration.__init__)
    params = list(sig.parameters.keys())



def test_ansic_function_definition_is_not_abstract():
    assert not inspect.isabstract(ansic_function_definition)


def test_ansic_function_definition_constructor_exists():
    assert callable(ansic_function_definition.__init__)


def test_ansic_function_definition_constructor_args():
    sig = inspect.signature(ansic_function_definition.__init__)
    params = list(sig.parameters.keys())



def test_ansic_translation_unit_linha_is_not_abstract():
    assert not inspect.isabstract(ansic_translation_unit_linha)


def test_ansic_translation_unit_linha_constructor_exists():
    assert callable(ansic_translation_unit_linha.__init__)


def test_ansic_translation_unit_linha_constructor_args():
    sig = inspect.signature(ansic_translation_unit_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_enumeration_constant_is_not_abstract():
    assert not inspect.isabstract(ansic_enumeration_constant)


def test_ansic_enumeration_constant_constructor_exists():
    assert callable(ansic_enumeration_constant.__init__)


def test_ansic_enumeration_constant_constructor_args():
    sig = inspect.signature(ansic_enumeration_constant.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_ansic_enumeration_constant_has_identifier():
    assert hasattr(ansic_enumeration_constant, "identifier")
    descriptor = None
    for klass in ansic_enumeration_constant.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_ansic_enumerator_list_linha_is_not_abstract():
    assert not inspect.isabstract(ansic_enumerator_list_linha)


def test_ansic_enumerator_list_linha_constructor_exists():
    assert callable(ansic_enumerator_list_linha.__init__)


def test_ansic_enumerator_list_linha_constructor_args():
    sig = inspect.signature(ansic_enumerator_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_enumerator_is_not_abstract():
    assert not inspect.isabstract(ansic_enumerator)


def test_ansic_enumerator_constructor_exists():
    assert callable(ansic_enumerator.__init__)


def test_ansic_enumerator_constructor_args():
    sig = inspect.signature(ansic_enumerator.__init__)
    params = list(sig.parameters.keys())



def test_ansic_enumerator_list_is_not_abstract():
    assert not inspect.isabstract(ansic_enumerator_list)


def test_ansic_enumerator_list_constructor_exists():
    assert callable(ansic_enumerator_list.__init__)


def test_ansic_enumerator_list_constructor_args():
    sig = inspect.signature(ansic_enumerator_list.__init__)
    params = list(sig.parameters.keys())



def test_ansic_enum_specifier_is_not_abstract():
    assert not inspect.isabstract(ansic_enum_specifier)


def test_ansic_enum_specifier_constructor_exists():
    assert callable(ansic_enum_specifier.__init__)


def test_ansic_enum_specifier_constructor_args():
    sig = inspect.signature(ansic_enum_specifier.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_ansic_enum_specifier_has_identifier():
    assert hasattr(ansic_enum_specifier, "identifier")
    descriptor = None
    for klass in ansic_enum_specifier.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_ansic_struct_or_union_specifier_is_not_abstract():
    assert not inspect.isabstract(ansic_struct_or_union_specifier)


def test_ansic_struct_or_union_specifier_constructor_exists():
    assert callable(ansic_struct_or_union_specifier.__init__)


def test_ansic_struct_or_union_specifier_constructor_args():
    sig = inspect.signature(ansic_struct_or_union_specifier.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "struct_or_union" in params, "Missing parameter 'struct_or_union'"

def test_ansic_struct_or_union_specifier_has_identifier():
    assert hasattr(ansic_struct_or_union_specifier, "identifier")
    descriptor = None
    for klass in ansic_struct_or_union_specifier.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_ansic_struct_or_union_specifier_has_struct_or_union():
    assert hasattr(ansic_struct_or_union_specifier, "struct_or_union")
    descriptor = None
    for klass in ansic_struct_or_union_specifier.__mro__:
        if "struct_or_union" in klass.__dict__:
            descriptor = klass.__dict__["struct_or_union"]
            break
    assert isinstance(descriptor, property)



def test_ansic_atomic_type_specifier_is_not_abstract():
    assert not inspect.isabstract(ansic_atomic_type_specifier)


def test_ansic_atomic_type_specifier_constructor_exists():
    assert callable(ansic_atomic_type_specifier.__init__)


def test_ansic_atomic_type_specifier_constructor_args():
    sig = inspect.signature(ansic_atomic_type_specifier.__init__)
    params = list(sig.parameters.keys())



def test_ansic_constant_expression_is_not_abstract():
    assert not inspect.isabstract(ansic_constant_expression)


def test_ansic_constant_expression_constructor_exists():
    assert callable(ansic_constant_expression.__init__)


def test_ansic_constant_expression_constructor_args():
    sig = inspect.signature(ansic_constant_expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic_alignment_specifier_is_not_abstract():
    assert not inspect.isabstract(ansic_alignment_specifier)


def test_ansic_alignment_specifier_constructor_exists():
    assert callable(ansic_alignment_specifier.__init__)


def test_ansic_alignment_specifier_constructor_args():
    sig = inspect.signature(ansic_alignment_specifier.__init__)
    params = list(sig.parameters.keys())



def test_ansic_type_qualifier_is_not_abstract():
    assert not inspect.isabstract(ansic_type_qualifier)


def test_ansic_type_qualifier_constructor_exists():
    assert callable(ansic_type_qualifier.__init__)


def test_ansic_type_qualifier_constructor_args():
    sig = inspect.signature(ansic_type_qualifier.__init__)
    params = list(sig.parameters.keys())
    assert "namez" in params, "Missing parameter 'namez'"

def test_ansic_type_qualifier_has_namez():
    assert hasattr(ansic_type_qualifier, "namez")
    descriptor = None
    for klass in ansic_type_qualifier.__mro__:
        if "namez" in klass.__dict__:
            descriptor = klass.__dict__["namez"]
            break
    assert isinstance(descriptor, property)



def test_ansic_type_specifier_is_not_abstract():
    assert not inspect.isabstract(ansic_type_specifier)


def test_ansic_type_specifier_constructor_exists():
    assert callable(ansic_type_specifier.__init__)


def test_ansic_type_specifier_constructor_args():
    sig = inspect.signature(ansic_type_specifier.__init__)
    params = list(sig.parameters.keys())
    assert "type_name_str" in params, "Missing parameter 'type_name_str'"

def test_ansic_type_specifier_has_type_name_str():
    assert hasattr(ansic_type_specifier, "type_name_str")
    descriptor = None
    for klass in ansic_type_specifier.__mro__:
        if "type_name_str" in klass.__dict__:
            descriptor = klass.__dict__["type_name_str"]
            break
    assert isinstance(descriptor, property)



def test_ansic_declaration_specifiers_is_not_abstract():
    assert not inspect.isabstract(ansic_declaration_specifiers)


def test_ansic_declaration_specifiers_constructor_exists():
    assert callable(ansic_declaration_specifiers.__init__)


def test_ansic_declaration_specifiers_constructor_args():
    sig = inspect.signature(ansic_declaration_specifiers.__init__)
    params = list(sig.parameters.keys())
    assert "storage_class_specifier" in params, "Missing parameter 'storage_class_specifier'"
    assert "function_specifier" in params, "Missing parameter 'function_specifier'"

def test_ansic_declaration_specifiers_has_storage_class_specifier():
    assert hasattr(ansic_declaration_specifiers, "storage_class_specifier")
    descriptor = None
    for klass in ansic_declaration_specifiers.__mro__:
        if "storage_class_specifier" in klass.__dict__:
            descriptor = klass.__dict__["storage_class_specifier"]
            break
    assert isinstance(descriptor, property)

def test_ansic_declaration_specifiers_has_function_specifier():
    assert hasattr(ansic_declaration_specifiers, "function_specifier")
    descriptor = None
    for klass in ansic_declaration_specifiers.__mro__:
        if "function_specifier" in klass.__dict__:
            descriptor = klass.__dict__["function_specifier"]
            break
    assert isinstance(descriptor, property)



def test_ansic_external_declaration_is_not_abstract():
    assert not inspect.isabstract(ansic_external_declaration)


def test_ansic_external_declaration_constructor_exists():
    assert callable(ansic_external_declaration.__init__)


def test_ansic_external_declaration_constructor_args():
    sig = inspect.signature(ansic_external_declaration.__init__)
    params = list(sig.parameters.keys())



def test_ansic_translation_unit_is_not_abstract():
    assert not inspect.isabstract(ansic_translation_unit)


def test_ansic_translation_unit_constructor_exists():
    assert callable(ansic_translation_unit.__init__)


def test_ansic_translation_unit_constructor_args():
    sig = inspect.signature(ansic_translation_unit.__init__)
    params = list(sig.parameters.keys())



def test_ansic_domainmodel_is_not_abstract():
    assert not inspect.isabstract(ansic_DomainModel)


def test_ansic_domainmodel_constructor_exists():
    assert callable(ansic_DomainModel.__init__)


def test_ansic_domainmodel_constructor_args():
    sig = inspect.signature(ansic_DomainModel.__init__)
    params = list(sig.parameters.keys())



def test_translation_unit_linha_is_not_abstract():
    assert not inspect.isabstract(translation_unit_linha)


def test_translation_unit_linha_constructor_exists():
    assert callable(translation_unit_linha.__init__)


def test_translation_unit_linha_constructor_args():
    sig = inspect.signature(translation_unit_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_tranlationunitlinhaaction_is_not_abstract():
    assert not inspect.isabstract(ansic_TranlationUnitLinhaAction)


def test_ansic_tranlationunitlinhaaction_constructor_exists():
    assert callable(ansic_TranlationUnitLinhaAction.__init__)


def test_ansic_tranlationunitlinhaaction_constructor_args():
    sig = inspect.signature(ansic_TranlationUnitLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_init_declarator_list_linha_is_not_abstract():
    assert not inspect.isabstract(init_declarator_list_linha)


def test_init_declarator_list_linha_constructor_exists():
    assert callable(init_declarator_list_linha.__init__)


def test_init_declarator_list_linha_constructor_args():
    sig = inspect.signature(init_declarator_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_initdecclaratorlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(ansic_InitDecclaratorListLinhaAction)


def test_ansic_initdecclaratorlistlinhaaction_constructor_exists():
    assert callable(ansic_InitDecclaratorListLinhaAction.__init__)


def test_ansic_initdecclaratorlistlinhaaction_constructor_args():
    sig = inspect.signature(ansic_InitDecclaratorListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_unary_expression_is_not_abstract():
    assert not inspect.isabstract(unary_expression)


def test_unary_expression_constructor_exists():
    assert callable(unary_expression.__init__)


def test_unary_expression_constructor_args():
    sig = inspect.signature(unary_expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic_plusplus_is_not_abstract():
    assert not inspect.isabstract(ansic_PlusPlus)


def test_ansic_plusplus_constructor_exists():
    assert callable(ansic_PlusPlus.__init__)


def test_ansic_plusplus_constructor_args():
    sig = inspect.signature(ansic_PlusPlus.__init__)
    params = list(sig.parameters.keys())
    assert "plus" in params, "Missing parameter 'plus'"

def test_ansic_plusplus_has_plus():
    assert hasattr(ansic_PlusPlus, "plus")
    descriptor = None
    for klass in ansic_PlusPlus.__mro__:
        if "plus" in klass.__dict__:
            descriptor = klass.__dict__["plus"]
            break
    assert isinstance(descriptor, property)



def test_argument_expression_list_linha_is_not_abstract():
    assert not inspect.isabstract(argument_expression_list_linha)


def test_argument_expression_list_linha_constructor_exists():
    assert callable(argument_expression_list_linha.__init__)


def test_argument_expression_list_linha_constructor_args():
    sig = inspect.signature(argument_expression_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_argumentexpressionlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(ansic_ArgumentExpressionListLinhaAction)


def test_ansic_argumentexpressionlistlinhaaction_constructor_exists():
    assert callable(ansic_ArgumentExpressionListLinhaAction.__init__)


def test_ansic_argumentexpressionlistlinhaaction_constructor_args():
    sig = inspect.signature(ansic_ArgumentExpressionListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_postfix_expression_complement_is_not_abstract():
    assert not inspect.isabstract(postfix_expression_complement)


def test_postfix_expression_complement_constructor_exists():
    assert callable(postfix_expression_complement.__init__)


def test_postfix_expression_complement_constructor_args():
    sig = inspect.signature(postfix_expression_complement.__init__)
    params = list(sig.parameters.keys())



def test_ansic_postfixempryparams_is_not_abstract():
    assert not inspect.isabstract(ansic_PostFixEmpryParams)


def test_ansic_postfixempryparams_constructor_exists():
    assert callable(ansic_PostFixEmpryParams.__init__)


def test_ansic_postfixempryparams_constructor_args():
    sig = inspect.signature(ansic_PostFixEmpryParams.__init__)
    params = list(sig.parameters.keys())



def test_designator_list_linha_is_not_abstract():
    assert not inspect.isabstract(designator_list_linha)


def test_designator_list_linha_constructor_exists():
    assert callable(designator_list_linha.__init__)


def test_designator_list_linha_constructor_args():
    sig = inspect.signature(designator_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_designatorlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(ansic_DesignatorListLinhaAction)


def test_ansic_designatorlistlinhaaction_constructor_exists():
    assert callable(ansic_DesignatorListLinhaAction.__init__)


def test_ansic_designatorlistlinhaaction_constructor_args():
    sig = inspect.signature(ansic_DesignatorListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_initializer_list_linha_is_not_abstract():
    assert not inspect.isabstract(initializer_list_linha)


def test_initializer_list_linha_constructor_exists():
    assert callable(initializer_list_linha.__init__)


def test_initializer_list_linha_constructor_args():
    sig = inspect.signature(initializer_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_initializerlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(ansic_InitializerListLinhaAction)


def test_ansic_initializerlistlinhaaction_constructor_exists():
    assert callable(ansic_InitializerListLinhaAction.__init__)


def test_ansic_initializerlistlinhaaction_constructor_args():
    sig = inspect.signature(ansic_InitializerListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_postfix_expression_linha_is_not_abstract():
    assert not inspect.isabstract(postfix_expression_linha)


def test_postfix_expression_linha_constructor_exists():
    assert callable(postfix_expression_linha.__init__)


def test_postfix_expression_linha_constructor_args():
    sig = inspect.signature(postfix_expression_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_postfixexpressionlinhaaction_is_not_abstract():
    assert not inspect.isabstract(ansic_PostfixExpressionLinhaAction)


def test_ansic_postfixexpressionlinhaaction_constructor_exists():
    assert callable(ansic_PostfixExpressionLinhaAction.__init__)


def test_ansic_postfixexpressionlinhaaction_constructor_args():
    sig = inspect.signature(ansic_PostfixExpressionLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_generic_assoc_list_linha_is_not_abstract():
    assert not inspect.isabstract(generic_assoc_list_linha)


def test_generic_assoc_list_linha_constructor_exists():
    assert callable(generic_assoc_list_linha.__init__)


def test_generic_assoc_list_linha_constructor_args():
    sig = inspect.signature(generic_assoc_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_genericassoclistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(ansic_GenericAssocListLinhaAction)


def test_ansic_genericassoclistlinhaaction_constructor_exists():
    assert callable(ansic_GenericAssocListLinhaAction.__init__)


def test_ansic_genericassoclistlinhaaction_constructor_args():
    sig = inspect.signature(ansic_GenericAssocListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_ansic_string_ufcg_is_not_abstract():
    assert not inspect.isabstract(ansic_string_ufcg)


def test_ansic_string_ufcg_constructor_exists():
    assert callable(ansic_string_ufcg.__init__)


def test_ansic_string_ufcg_constructor_args():
    sig = inspect.signature(ansic_string_ufcg.__init__)
    params = list(sig.parameters.keys())
    assert "string_literal" in params, "Missing parameter 'string_literal'"
    assert "__func__" in params, "Missing parameter '__func__'"

def test_ansic_string_ufcg_has_string_literal():
    assert hasattr(ansic_string_ufcg, "string_literal")
    descriptor = None
    for klass in ansic_string_ufcg.__mro__:
        if "string_literal" in klass.__dict__:
            descriptor = klass.__dict__["string_literal"]
            break
    assert isinstance(descriptor, property)

def test_ansic_string_ufcg_has___func__():
    assert hasattr(ansic_string_ufcg, "__func__")
    descriptor = None
    for klass in ansic_string_ufcg.__mro__:
        if "__func__" in klass.__dict__:
            descriptor = klass.__dict__["__func__"]
            break
    assert isinstance(descriptor, property)



def test_identifier_list_linha_is_not_abstract():
    assert not inspect.isabstract(identifier_list_linha)


def test_identifier_list_linha_constructor_exists():
    assert callable(identifier_list_linha.__init__)


def test_identifier_list_linha_constructor_args():
    sig = inspect.signature(identifier_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_identifierlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(ansic_IdentifierListLinhaAction)


def test_ansic_identifierlistlinhaaction_constructor_exists():
    assert callable(ansic_IdentifierListLinhaAction.__init__)


def test_ansic_identifierlistlinhaaction_constructor_args():
    sig = inspect.signature(ansic_IdentifierListLinhaAction.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_ansic_identifierlistlinhaaction_has_identifier():
    assert hasattr(ansic_IdentifierListLinhaAction, "identifier")
    descriptor = None
    for klass in ansic_IdentifierListLinhaAction.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_direct_abstract_declarator_linha_is_not_abstract():
    assert not inspect.isabstract(direct_abstract_declarator_linha)


def test_direct_abstract_declarator_linha_constructor_exists():
    assert callable(direct_abstract_declarator_linha.__init__)


def test_direct_abstract_declarator_linha_constructor_args():
    sig = inspect.signature(direct_abstract_declarator_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_directabstractdeclarratorlinhaaction_is_not_abstract():
    assert not inspect.isabstract(ansic_DirectAbstractDeclarratorLinhaAction)


def test_ansic_directabstractdeclarratorlinhaaction_constructor_exists():
    assert callable(ansic_DirectAbstractDeclarratorLinhaAction.__init__)


def test_ansic_directabstractdeclarratorlinhaaction_constructor_args():
    sig = inspect.signature(ansic_DirectAbstractDeclarratorLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_type_qualifier_list_linha_is_not_abstract():
    assert not inspect.isabstract(type_qualifier_list_linha)


def test_type_qualifier_list_linha_constructor_exists():
    assert callable(type_qualifier_list_linha.__init__)


def test_type_qualifier_list_linha_constructor_args():
    sig = inspect.signature(type_qualifier_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_typequalifierlistlinhaation_is_not_abstract():
    assert not inspect.isabstract(ansic_TypeQualifierListLinhaAtion)


def test_ansic_typequalifierlistlinhaation_constructor_exists():
    assert callable(ansic_TypeQualifierListLinhaAtion.__init__)


def test_ansic_typequalifierlistlinhaation_constructor_args():
    sig = inspect.signature(ansic_TypeQualifierListLinhaAtion.__init__)
    params = list(sig.parameters.keys())



def test_declaration_list_linha_is_not_abstract():
    assert not inspect.isabstract(declaration_list_linha)


def test_declaration_list_linha_constructor_exists():
    assert callable(declaration_list_linha.__init__)


def test_declaration_list_linha_constructor_args():
    sig = inspect.signature(declaration_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_declarationlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(ansic_DeclarationListLinhaAction)


def test_ansic_declarationlistlinhaaction_constructor_exists():
    assert callable(ansic_DeclarationListLinhaAction.__init__)


def test_ansic_declarationlistlinhaaction_constructor_args():
    sig = inspect.signature(ansic_DeclarationListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_struct_declarator_list_linha_is_not_abstract():
    assert not inspect.isabstract(struct_declarator_list_linha)


def test_struct_declarator_list_linha_constructor_exists():
    assert callable(struct_declarator_list_linha.__init__)


def test_struct_declarator_list_linha_constructor_args():
    sig = inspect.signature(struct_declarator_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_structdeclaratorlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(ansic_StructDeclaratorListLinhaAction)


def test_ansic_structdeclaratorlistlinhaaction_constructor_exists():
    assert callable(ansic_StructDeclaratorListLinhaAction.__init__)


def test_ansic_structdeclaratorlistlinhaaction_constructor_args():
    sig = inspect.signature(ansic_StructDeclaratorListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_struct_declaration_list_linha_is_not_abstract():
    assert not inspect.isabstract(struct_declaration_list_linha)


def test_struct_declaration_list_linha_constructor_exists():
    assert callable(struct_declaration_list_linha.__init__)


def test_struct_declaration_list_linha_constructor_args():
    sig = inspect.signature(struct_declaration_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_structdeclarationlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(ansic_StructDeclarationListLinhaAction)


def test_ansic_structdeclarationlistlinhaaction_constructor_exists():
    assert callable(ansic_StructDeclarationListLinhaAction.__init__)


def test_ansic_structdeclarationlistlinhaaction_constructor_args():
    sig = inspect.signature(ansic_StructDeclarationListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_struct_or_union_specifier_complement_is_not_abstract():
    assert not inspect.isabstract(struct_or_union_specifier_complement)


def test_struct_or_union_specifier_complement_constructor_exists():
    assert callable(struct_or_union_specifier_complement.__init__)


def test_struct_or_union_specifier_complement_constructor_args():
    sig = inspect.signature(struct_or_union_specifier_complement.__init__)
    params = list(sig.parameters.keys())



def test_ansic_structorunionspecifiercomplementaction_is_not_abstract():
    assert not inspect.isabstract(ansic_StructOrUnionSpecifierComplementAction)


def test_ansic_structorunionspecifiercomplementaction_constructor_exists():
    assert callable(ansic_StructOrUnionSpecifierComplementAction.__init__)


def test_ansic_structorunionspecifiercomplementaction_constructor_args():
    sig = inspect.signature(ansic_StructOrUnionSpecifierComplementAction.__init__)
    params = list(sig.parameters.keys())



def test_enumerator_list_linha_is_not_abstract():
    assert not inspect.isabstract(enumerator_list_linha)


def test_enumerator_list_linha_constructor_exists():
    assert callable(enumerator_list_linha.__init__)


def test_enumerator_list_linha_constructor_args():
    sig = inspect.signature(enumerator_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_enumeratorlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(ansic_EnumeratorListLinhaAction)


def test_ansic_enumeratorlistlinhaaction_constructor_exists():
    assert callable(ansic_EnumeratorListLinhaAction.__init__)


def test_ansic_enumeratorlistlinhaaction_constructor_args():
    sig = inspect.signature(ansic_EnumeratorListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_ansic_init_declarator_is_not_abstract():
    assert not inspect.isabstract(ansic_init_declarator)


def test_ansic_init_declarator_constructor_exists():
    assert callable(ansic_init_declarator.__init__)


def test_ansic_init_declarator_constructor_args():
    sig = inspect.signature(ansic_init_declarator.__init__)
    params = list(sig.parameters.keys())



def test_ansic_expression_linha_is_not_abstract():
    assert not inspect.isabstract(ansic_expression_linha)


def test_ansic_expression_linha_constructor_exists():
    assert callable(ansic_expression_linha.__init__)


def test_ansic_expression_linha_constructor_args():
    sig = inspect.signature(ansic_expression_linha.__init__)
    params = list(sig.parameters.keys())



def test_postfix_expression_is_not_abstract():
    assert not inspect.isabstract(postfix_expression)


def test_postfix_expression_constructor_exists():
    assert callable(postfix_expression.__init__)


def test_postfix_expression_constructor_args():
    sig = inspect.signature(postfix_expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic_type_name_is_not_abstract():
    assert not inspect.isabstract(ansic_type_name)


def test_ansic_type_name_constructor_exists():
    assert callable(ansic_type_name.__init__)


def test_ansic_type_name_constructor_args():
    sig = inspect.signature(ansic_type_name.__init__)
    params = list(sig.parameters.keys())



def test_ansic_conditional_expression_linha_is_not_abstract():
    assert not inspect.isabstract(ansic_conditional_expression_linha)


def test_ansic_conditional_expression_linha_constructor_exists():
    assert callable(ansic_conditional_expression_linha.__init__)


def test_ansic_conditional_expression_linha_constructor_args():
    sig = inspect.signature(ansic_conditional_expression_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_logical_or_expression_linha_is_not_abstract():
    assert not inspect.isabstract(ansic_logical_or_expression_linha)


def test_ansic_logical_or_expression_linha_constructor_exists():
    assert callable(ansic_logical_or_expression_linha.__init__)


def test_ansic_logical_or_expression_linha_constructor_args():
    sig = inspect.signature(ansic_logical_or_expression_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_logical_or_expression_is_not_abstract():
    assert not inspect.isabstract(ansic_logical_or_expression)


def test_ansic_logical_or_expression_constructor_exists():
    assert callable(ansic_logical_or_expression.__init__)


def test_ansic_logical_or_expression_constructor_args():
    sig = inspect.signature(ansic_logical_or_expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic_logical_and_expression_linha_is_not_abstract():
    assert not inspect.isabstract(ansic_logical_and_expression_linha)


def test_ansic_logical_and_expression_linha_constructor_exists():
    assert callable(ansic_logical_and_expression_linha.__init__)


def test_ansic_logical_and_expression_linha_constructor_args():
    sig = inspect.signature(ansic_logical_and_expression_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_logical_and_expression_is_not_abstract():
    assert not inspect.isabstract(ansic_logical_and_expression)


def test_ansic_logical_and_expression_constructor_exists():
    assert callable(ansic_logical_and_expression.__init__)


def test_ansic_logical_and_expression_constructor_args():
    sig = inspect.signature(ansic_logical_and_expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic_inclusive_or_expression_linha_is_not_abstract():
    assert not inspect.isabstract(ansic_inclusive_or_expression_linha)


def test_ansic_inclusive_or_expression_linha_constructor_exists():
    assert callable(ansic_inclusive_or_expression_linha.__init__)


def test_ansic_inclusive_or_expression_linha_constructor_args():
    sig = inspect.signature(ansic_inclusive_or_expression_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_inclusive_or_expression_is_not_abstract():
    assert not inspect.isabstract(ansic_inclusive_or_expression)


def test_ansic_inclusive_or_expression_constructor_exists():
    assert callable(ansic_inclusive_or_expression.__init__)


def test_ansic_inclusive_or_expression_constructor_args():
    sig = inspect.signature(ansic_inclusive_or_expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic_exclusive_or_expression_linha_is_not_abstract():
    assert not inspect.isabstract(ansic_exclusive_or_expression_linha)


def test_ansic_exclusive_or_expression_linha_constructor_exists():
    assert callable(ansic_exclusive_or_expression_linha.__init__)


def test_ansic_exclusive_or_expression_linha_constructor_args():
    sig = inspect.signature(ansic_exclusive_or_expression_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_exclusive_or_expression_is_not_abstract():
    assert not inspect.isabstract(ansic_exclusive_or_expression)


def test_ansic_exclusive_or_expression_constructor_exists():
    assert callable(ansic_exclusive_or_expression.__init__)


def test_ansic_exclusive_or_expression_constructor_args():
    sig = inspect.signature(ansic_exclusive_or_expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic_and_expression_linha_is_not_abstract():
    assert not inspect.isabstract(ansic_and_expression_linha)


def test_ansic_and_expression_linha_constructor_exists():
    assert callable(ansic_and_expression_linha.__init__)


def test_ansic_and_expression_linha_constructor_args():
    sig = inspect.signature(ansic_and_expression_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_and_expression_is_not_abstract():
    assert not inspect.isabstract(ansic_and_expression)


def test_ansic_and_expression_constructor_exists():
    assert callable(ansic_and_expression.__init__)


def test_ansic_and_expression_constructor_args():
    sig = inspect.signature(ansic_and_expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic_jump_statement_is_not_abstract():
    assert not inspect.isabstract(ansic_jump_statement)


def test_ansic_jump_statement_constructor_exists():
    assert callable(ansic_jump_statement.__init__)


def test_ansic_jump_statement_constructor_args():
    sig = inspect.signature(ansic_jump_statement.__init__)
    params = list(sig.parameters.keys())
    assert "return_vazio" in params, "Missing parameter 'return_vazio'"
    assert "return_" in params, "Missing parameter 'return_'"
    assert "break_" in params, "Missing parameter 'break_'"
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_ansic_jump_statement_has_return_vazio():
    assert hasattr(ansic_jump_statement, "return_vazio")
    descriptor = None
    for klass in ansic_jump_statement.__mro__:
        if "return_vazio" in klass.__dict__:
            descriptor = klass.__dict__["return_vazio"]
            break
    assert isinstance(descriptor, property)

def test_ansic_jump_statement_has_return_():
    assert hasattr(ansic_jump_statement, "return_")
    descriptor = None
    for klass in ansic_jump_statement.__mro__:
        if "return_" in klass.__dict__:
            descriptor = klass.__dict__["return_"]
            break
    assert isinstance(descriptor, property)

def test_ansic_jump_statement_has_break_():
    assert hasattr(ansic_jump_statement, "break_")
    descriptor = None
    for klass in ansic_jump_statement.__mro__:
        if "break_" in klass.__dict__:
            descriptor = klass.__dict__["break_"]
            break
    assert isinstance(descriptor, property)

def test_ansic_jump_statement_has_identifier():
    assert hasattr(ansic_jump_statement, "identifier")
    descriptor = None
    for klass in ansic_jump_statement.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_ansic_iteration_statement_is_not_abstract():
    assert not inspect.isabstract(ansic_iteration_statement)


def test_ansic_iteration_statement_constructor_exists():
    assert callable(ansic_iteration_statement.__init__)


def test_ansic_iteration_statement_constructor_args():
    sig = inspect.signature(ansic_iteration_statement.__init__)
    params = list(sig.parameters.keys())



def test_ansic_block_item_list_linha_is_not_abstract():
    assert not inspect.isabstract(ansic_block_item_list_linha)


def test_ansic_block_item_list_linha_constructor_exists():
    assert callable(ansic_block_item_list_linha.__init__)


def test_ansic_block_item_list_linha_constructor_args():
    sig = inspect.signature(ansic_block_item_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_block_item_is_not_abstract():
    assert not inspect.isabstract(ansic_block_item)


def test_ansic_block_item_constructor_exists():
    assert callable(ansic_block_item.__init__)


def test_ansic_block_item_constructor_args():
    sig = inspect.signature(ansic_block_item.__init__)
    params = list(sig.parameters.keys())



def test_ansic_block_item_list_is_not_abstract():
    assert not inspect.isabstract(ansic_block_item_list)


def test_ansic_block_item_list_constructor_exists():
    assert callable(ansic_block_item_list.__init__)


def test_ansic_block_item_list_constructor_args():
    sig = inspect.signature(ansic_block_item_list.__init__)
    params = list(sig.parameters.keys())



def test_ansic_additive_expression_complement_is_not_abstract():
    assert not inspect.isabstract(ansic_additive_expression_complement)


def test_ansic_additive_expression_complement_constructor_exists():
    assert callable(ansic_additive_expression_complement.__init__)


def test_ansic_additive_expression_complement_constructor_args():
    sig = inspect.signature(ansic_additive_expression_complement.__init__)
    params = list(sig.parameters.keys())



def test_ansic_additive_expression_linha_is_not_abstract():
    assert not inspect.isabstract(ansic_additive_expression_linha)


def test_ansic_additive_expression_linha_constructor_exists():
    assert callable(ansic_additive_expression_linha.__init__)


def test_ansic_additive_expression_linha_constructor_args():
    sig = inspect.signature(ansic_additive_expression_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_selection_statement_is_not_abstract():
    assert not inspect.isabstract(ansic_selection_statement)


def test_ansic_selection_statement_constructor_exists():
    assert callable(ansic_selection_statement.__init__)


def test_ansic_selection_statement_constructor_args():
    sig = inspect.signature(ansic_selection_statement.__init__)
    params = list(sig.parameters.keys())



def test_ansic_expression_statement_is_not_abstract():
    assert not inspect.isabstract(ansic_expression_statement)


def test_ansic_expression_statement_constructor_exists():
    assert callable(ansic_expression_statement.__init__)


def test_ansic_expression_statement_constructor_args():
    sig = inspect.signature(ansic_expression_statement.__init__)
    params = list(sig.parameters.keys())



def test_ansic_labeled_statement_is_not_abstract():
    assert not inspect.isabstract(ansic_labeled_statement)


def test_ansic_labeled_statement_constructor_exists():
    assert callable(ansic_labeled_statement.__init__)


def test_ansic_labeled_statement_constructor_args():
    sig = inspect.signature(ansic_labeled_statement.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_ansic_labeled_statement_has_identifier():
    assert hasattr(ansic_labeled_statement, "identifier")
    descriptor = None
    for klass in ansic_labeled_statement.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_ansic_statement_is_not_abstract():
    assert not inspect.isabstract(ansic_statement)


def test_ansic_statement_constructor_exists():
    assert callable(ansic_statement.__init__)


def test_ansic_statement_constructor_args():
    sig = inspect.signature(ansic_statement.__init__)
    params = list(sig.parameters.keys())



def test_ansic_equality_expression_complement_is_not_abstract():
    assert not inspect.isabstract(ansic_equality_expression_complement)


def test_ansic_equality_expression_complement_constructor_exists():
    assert callable(ansic_equality_expression_complement.__init__)


def test_ansic_equality_expression_complement_constructor_args():
    sig = inspect.signature(ansic_equality_expression_complement.__init__)
    params = list(sig.parameters.keys())



def test_ansic_equality_expression_linha_is_not_abstract():
    assert not inspect.isabstract(ansic_equality_expression_linha)


def test_ansic_equality_expression_linha_constructor_exists():
    assert callable(ansic_equality_expression_linha.__init__)


def test_ansic_equality_expression_linha_constructor_args():
    sig = inspect.signature(ansic_equality_expression_linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic_equality_expression_is_not_abstract():
    assert not inspect.isabstract(ansic_equality_expression)


def test_ansic_equality_expression_constructor_exists():
    assert callable(ansic_equality_expression.__init__)


def test_ansic_equality_expression_constructor_args():
    sig = inspect.signature(ansic_equality_expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic_relational_expression_complement_is_not_abstract():
    assert not inspect.isabstract(ansic_relational_expression_complement)


def test_ansic_relational_expression_complement_constructor_exists():
    assert callable(ansic_relational_expression_complement.__init__)


def test_ansic_relational_expression_complement_constructor_args():
    sig = inspect.signature(ansic_relational_expression_complement.__init__)
    params = list(sig.parameters.keys())



def test_ansic_relational_expression_linha_is_not_abstract():
    assert not inspect.isabstract(ansic_relational_expression_linha)


def test_ansic_relational_expression_linha_constructor_exists():
    assert callable(ansic_relational_expression_linha.__init__)


def test_ansic_relational_expression_linha_constructor_args():
    sig = inspect.signature(ansic_relational_expression_linha.__init__)
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
ansic_relational_expression_strategy = st.builds(
    ansic_relational_expression,
)
ansic_shift_expression_complement_strategy = st.builds(
    ansic_shift_expression_complement,
)
ansic_shift_expression_linha_strategy = st.builds(
    ansic_shift_expression_linha,
)
ansic_shift_expression_strategy = st.builds(
    ansic_shift_expression,
)
ansic_designator_list_linha_strategy = st.builds(
    ansic_designator_list_linha,
)
ansic_designator_strategy = st.builds(
    ansic_designator,
    identifier=
        safe_text
)
ansic_designator_list_strategy = st.builds(
    ansic_designator_list,
)
ansic_additive_expression_strategy = st.builds(
    ansic_additive_expression,
)
ansic_multiplicative_expression_complement_strategy = st.builds(
    ansic_multiplicative_expression_complement,
)
ansic_multiplicative_expression_linha_strategy = st.builds(
    ansic_multiplicative_expression_linha,
)
ansic_multiplicative_expression_strategy = st.builds(
    ansic_multiplicative_expression,
)
ansic_cast_expression_strategy = st.builds(
    ansic_cast_expression,
)
ansic_unary_expression_strategy = st.builds(
    ansic_unary_expression,
    unary_operator=
        safe_text
)
ansic_argument_expression_list_linha_strategy = st.builds(
    ansic_argument_expression_list_linha,
)
ansic_argument_expression_list_strategy = st.builds(
    ansic_argument_expression_list,
)
ansic_postfix_expression_complement_strategy = st.builds(
    ansic_postfix_expression_complement,
    identifier=
        safe_text
)
ansic_conditional_expression_strategy = st.builds(
    ansic_conditional_expression,
)
ansic_primary_expression_strategy = st.builds(
    ansic_primary_expression,
    identifier=
        safe_text
)
ansic_identifier_list_linha_strategy = st.builds(
    ansic_identifier_list_linha,
)
ansic_initializer_list_complement_strategy = st.builds(
    ansic_initializer_list_complement,
)
ansic_initializer_list_linha_strategy = st.builds(
    ansic_initializer_list_linha,
)
ansic_init_declarator_list_linha_strategy = st.builds(
    ansic_init_declarator_list_linha,
)
ansic_designation_strategy = st.builds(
    ansic_designation,
)
ansic_postfix_expression_linha_strategy = st.builds(
    ansic_postfix_expression_linha,
)
ansic_postfix_expression_strategy = st.builds(
    ansic_postfix_expression,
)
ansic_generic_assoc_list_linha_strategy = st.builds(
    ansic_generic_assoc_list_linha,
)
ansic_generic_association_strategy = st.builds(
    ansic_generic_association,
    default=
        safe_text
)
ansic_generic_assoc_list_strategy = st.builds(
    ansic_generic_assoc_list,
)
ansic_generic_selection_strategy = st.builds(
    ansic_generic_selection,
    _generic=
        safe_text
)
ansic_expression_strategy = st.builds(
    ansic_expression,
)
ansic_constant_strategy = st.builds(
    ansic_constant,
    enumz=
        safe_text,
    f_constant=
        safe_text,
    char=
        safe_text,
    i_constant=
        st.integers()
)
ansic_parameter_type_list_strategy = st.builds(
    ansic_parameter_type_list,
)
ansic_assignment_expression_strategy = st.builds(
    ansic_assignment_expression,
    assignment_operator=
        safe_text
)
ansic_direct_abstract_declarator_complement_strategy = st.builds(
    ansic_direct_abstract_declarator_complement,
)
ansic_initializer_list_strategy = st.builds(
    ansic_initializer_list,
)
ansic_initializer_strategy = st.builds(
    ansic_initializer,
)
ansic_direct_abstract_declarator_linha_strategy = st.builds(
    ansic_direct_abstract_declarator_linha,
)
ansic_direct_abstract_declarator_strategy = st.builds(
    ansic_direct_abstract_declarator,
)
ansic_abstract_declarator_strategy = st.builds(
    ansic_abstract_declarator,
)
ansic_parameter_list_linha_strategy = st.builds(
    ansic_parameter_list_linha,
)
ansic_parameter_declaration_strategy = st.builds(
    ansic_parameter_declaration,
)
ansic_parameter_lista_strategy = st.builds(
    ansic_parameter_lista,
)
ansic_identifier_list_strategy = st.builds(
    ansic_identifier_list,
    identifier=
        safe_text
)
ansic_direct_declarator_complemento_strategy = st.builds(
    ansic_direct_declarator_complemento,
)
ansic_direct_declarator_linha_strategy = st.builds(
    ansic_direct_declarator_linha,
)
ansic_type_qualifier_list_linha_strategy = st.builds(
    ansic_type_qualifier_list_linha,
)
direct_abstract_declarator_complement_strategy = st.builds(
    direct_abstract_declarator_complement,
)
ansic_type_qualifier_list_strategy = st.builds(
    ansic_type_qualifier_list,
)
ansic_direct_declarator_strategy = st.builds(
    ansic_direct_declarator,
    identifier=
        safe_text
)
ansic_pointer_strategy = st.builds(
    ansic_pointer,
)
ansic_declaration_list_linha_strategy = st.builds(
    ansic_declaration_list_linha,
)
ansic_compound_statement_strategy = st.builds(
    ansic_compound_statement,
)
ansic_declaration_list_strategy = st.builds(
    ansic_declaration_list,
)
ansic_init_declarator_list_strategy = st.builds(
    ansic_init_declarator_list,
)
ansic_struct_declaration_list_strategy = st.builds(
    ansic_struct_declaration_list,
)
ansic_declarator_strategy = st.builds(
    ansic_declarator,
)
ansic_struct_declarator_list_linha_strategy = st.builds(
    ansic_struct_declarator_list_linha,
)
ansic_struct_declarator_strategy = st.builds(
    ansic_struct_declarator,
)
ansic_static_assert_declaration_strategy = st.builds(
    ansic_static_assert_declaration,
)
ansic_struct_declarator_list_strategy = st.builds(
    ansic_struct_declarator_list,
)
ansic_specifier_qualifier_list_strategy = st.builds(
    ansic_specifier_qualifier_list,
)
ansic_struct_declaration_list_linha_strategy = st.builds(
    ansic_struct_declaration_list_linha,
)
ansic_struct_declaration_strategy = st.builds(
    ansic_struct_declaration,
)
ansic_struct_or_union_specifier_complement_strategy = st.builds(
    ansic_struct_or_union_specifier_complement,
)
ansic_declaration_strategy = st.builds(
    ansic_declaration,
)
ansic_function_definition_strategy = st.builds(
    ansic_function_definition,
)
ansic_translation_unit_linha_strategy = st.builds(
    ansic_translation_unit_linha,
)
ansic_enumeration_constant_strategy = st.builds(
    ansic_enumeration_constant,
    identifier=
        safe_text
)
ansic_enumerator_list_linha_strategy = st.builds(
    ansic_enumerator_list_linha,
)
ansic_enumerator_strategy = st.builds(
    ansic_enumerator,
)
ansic_enumerator_list_strategy = st.builds(
    ansic_enumerator_list,
)
ansic_enum_specifier_strategy = st.builds(
    ansic_enum_specifier,
    identifier=
        safe_text
)
ansic_struct_or_union_specifier_strategy = st.builds(
    ansic_struct_or_union_specifier,
    identifier=
        safe_text,
    struct_or_union=
        safe_text
)
ansic_atomic_type_specifier_strategy = st.builds(
    ansic_atomic_type_specifier,
)
ansic_constant_expression_strategy = st.builds(
    ansic_constant_expression,
)
ansic_alignment_specifier_strategy = st.builds(
    ansic_alignment_specifier,
)
ansic_type_qualifier_strategy = st.builds(
    ansic_type_qualifier,
    namez=
        safe_text
)
ansic_type_specifier_strategy = st.builds(
    ansic_type_specifier,
    type_name_str=
        safe_text
)
ansic_declaration_specifiers_strategy = st.builds(
    ansic_declaration_specifiers,
    storage_class_specifier=
        safe_text,
    function_specifier=
        safe_text
)
ansic_external_declaration_strategy = st.builds(
    ansic_external_declaration,
)
ansic_translation_unit_strategy = st.builds(
    ansic_translation_unit,
)
ansic_DomainModel_strategy = st.builds(
    ansic_DomainModel,
)
translation_unit_linha_strategy = st.builds(
    translation_unit_linha,
)
ansic_TranlationUnitLinhaAction_strategy = st.builds(
    ansic_TranlationUnitLinhaAction,
)
init_declarator_list_linha_strategy = st.builds(
    init_declarator_list_linha,
)
ansic_InitDecclaratorListLinhaAction_strategy = st.builds(
    ansic_InitDecclaratorListLinhaAction,
)
unary_expression_strategy = st.builds(
    unary_expression,
)
ansic_PlusPlus_strategy = st.builds(
    ansic_PlusPlus,
    plus=
        safe_text
)
argument_expression_list_linha_strategy = st.builds(
    argument_expression_list_linha,
)
ansic_ArgumentExpressionListLinhaAction_strategy = st.builds(
    ansic_ArgumentExpressionListLinhaAction,
)
postfix_expression_complement_strategy = st.builds(
    postfix_expression_complement,
)
ansic_PostFixEmpryParams_strategy = st.builds(
    ansic_PostFixEmpryParams,
)
designator_list_linha_strategy = st.builds(
    designator_list_linha,
)
ansic_DesignatorListLinhaAction_strategy = st.builds(
    ansic_DesignatorListLinhaAction,
)
initializer_list_linha_strategy = st.builds(
    initializer_list_linha,
)
ansic_InitializerListLinhaAction_strategy = st.builds(
    ansic_InitializerListLinhaAction,
)
postfix_expression_linha_strategy = st.builds(
    postfix_expression_linha,
)
ansic_PostfixExpressionLinhaAction_strategy = st.builds(
    ansic_PostfixExpressionLinhaAction,
)
generic_assoc_list_linha_strategy = st.builds(
    generic_assoc_list_linha,
)
ansic_GenericAssocListLinhaAction_strategy = st.builds(
    ansic_GenericAssocListLinhaAction,
)
ansic_string_ufcg_strategy = st.builds(
    ansic_string_ufcg,
    string_literal=
        safe_text,
    __func__=
        safe_text
)
identifier_list_linha_strategy = st.builds(
    identifier_list_linha,
)
ansic_IdentifierListLinhaAction_strategy = st.builds(
    ansic_IdentifierListLinhaAction,
    identifier=
        safe_text
)
direct_abstract_declarator_linha_strategy = st.builds(
    direct_abstract_declarator_linha,
)
ansic_DirectAbstractDeclarratorLinhaAction_strategy = st.builds(
    ansic_DirectAbstractDeclarratorLinhaAction,
)
type_qualifier_list_linha_strategy = st.builds(
    type_qualifier_list_linha,
)
ansic_TypeQualifierListLinhaAtion_strategy = st.builds(
    ansic_TypeQualifierListLinhaAtion,
)
declaration_list_linha_strategy = st.builds(
    declaration_list_linha,
)
ansic_DeclarationListLinhaAction_strategy = st.builds(
    ansic_DeclarationListLinhaAction,
)
struct_declarator_list_linha_strategy = st.builds(
    struct_declarator_list_linha,
)
ansic_StructDeclaratorListLinhaAction_strategy = st.builds(
    ansic_StructDeclaratorListLinhaAction,
)
struct_declaration_list_linha_strategy = st.builds(
    struct_declaration_list_linha,
)
ansic_StructDeclarationListLinhaAction_strategy = st.builds(
    ansic_StructDeclarationListLinhaAction,
)
struct_or_union_specifier_complement_strategy = st.builds(
    struct_or_union_specifier_complement,
)
ansic_StructOrUnionSpecifierComplementAction_strategy = st.builds(
    ansic_StructOrUnionSpecifierComplementAction,
)
enumerator_list_linha_strategy = st.builds(
    enumerator_list_linha,
)
ansic_EnumeratorListLinhaAction_strategy = st.builds(
    ansic_EnumeratorListLinhaAction,
)
ansic_init_declarator_strategy = st.builds(
    ansic_init_declarator,
)
ansic_expression_linha_strategy = st.builds(
    ansic_expression_linha,
)
postfix_expression_strategy = st.builds(
    postfix_expression,
)
ansic_type_name_strategy = st.builds(
    ansic_type_name,
)
ansic_conditional_expression_linha_strategy = st.builds(
    ansic_conditional_expression_linha,
)
ansic_logical_or_expression_linha_strategy = st.builds(
    ansic_logical_or_expression_linha,
)
ansic_logical_or_expression_strategy = st.builds(
    ansic_logical_or_expression,
)
ansic_logical_and_expression_linha_strategy = st.builds(
    ansic_logical_and_expression_linha,
)
ansic_logical_and_expression_strategy = st.builds(
    ansic_logical_and_expression,
)
ansic_inclusive_or_expression_linha_strategy = st.builds(
    ansic_inclusive_or_expression_linha,
)
ansic_inclusive_or_expression_strategy = st.builds(
    ansic_inclusive_or_expression,
)
ansic_exclusive_or_expression_linha_strategy = st.builds(
    ansic_exclusive_or_expression_linha,
)
ansic_exclusive_or_expression_strategy = st.builds(
    ansic_exclusive_or_expression,
)
ansic_and_expression_linha_strategy = st.builds(
    ansic_and_expression_linha,
)
ansic_and_expression_strategy = st.builds(
    ansic_and_expression,
)
ansic_jump_statement_strategy = st.builds(
    ansic_jump_statement,
    return_vazio=
        safe_text,
    return_=
        safe_text,
    break_=
        safe_text,
    identifier=
        safe_text
)
ansic_iteration_statement_strategy = st.builds(
    ansic_iteration_statement,
)
ansic_block_item_list_linha_strategy = st.builds(
    ansic_block_item_list_linha,
)
ansic_block_item_strategy = st.builds(
    ansic_block_item,
)
ansic_block_item_list_strategy = st.builds(
    ansic_block_item_list,
)
ansic_additive_expression_complement_strategy = st.builds(
    ansic_additive_expression_complement,
)
ansic_additive_expression_linha_strategy = st.builds(
    ansic_additive_expression_linha,
)
ansic_selection_statement_strategy = st.builds(
    ansic_selection_statement,
)
ansic_expression_statement_strategy = st.builds(
    ansic_expression_statement,
)
ansic_labeled_statement_strategy = st.builds(
    ansic_labeled_statement,
    identifier=
        safe_text
)
ansic_statement_strategy = st.builds(
    ansic_statement,
)
ansic_equality_expression_complement_strategy = st.builds(
    ansic_equality_expression_complement,
)
ansic_equality_expression_linha_strategy = st.builds(
    ansic_equality_expression_linha,
)
ansic_equality_expression_strategy = st.builds(
    ansic_equality_expression,
)
ansic_relational_expression_complement_strategy = st.builds(
    ansic_relational_expression_complement,
)
ansic_relational_expression_linha_strategy = st.builds(
    ansic_relational_expression_linha,
)

@given(instance=ansic_relational_expression_strategy)
@settings(max_examples=50)
def test_ansic_relational_expression_instantiation(instance):
    assert isinstance(instance, ansic_relational_expression)

@given(instance=ansic_shift_expression_complement_strategy)
@settings(max_examples=50)
def test_ansic_shift_expression_complement_instantiation(instance):
    assert isinstance(instance, ansic_shift_expression_complement)

@given(instance=ansic_shift_expression_linha_strategy)
@settings(max_examples=50)
def test_ansic_shift_expression_linha_instantiation(instance):
    assert isinstance(instance, ansic_shift_expression_linha)

@given(instance=ansic_shift_expression_strategy)
@settings(max_examples=50)
def test_ansic_shift_expression_instantiation(instance):
    assert isinstance(instance, ansic_shift_expression)

@given(instance=ansic_designator_list_linha_strategy)
@settings(max_examples=50)
def test_ansic_designator_list_linha_instantiation(instance):
    assert isinstance(instance, ansic_designator_list_linha)

@given(instance=ansic_designator_strategy)
@settings(max_examples=50)
def test_ansic_designator_instantiation(instance):
    assert isinstance(instance, ansic_designator)



@given(instance=ansic_designator_strategy)
def test_ansic_designator_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=ansic_designator_list_strategy)
@settings(max_examples=50)
def test_ansic_designator_list_instantiation(instance):
    assert isinstance(instance, ansic_designator_list)

@given(instance=ansic_additive_expression_strategy)
@settings(max_examples=50)
def test_ansic_additive_expression_instantiation(instance):
    assert isinstance(instance, ansic_additive_expression)

@given(instance=ansic_multiplicative_expression_complement_strategy)
@settings(max_examples=50)
def test_ansic_multiplicative_expression_complement_instantiation(instance):
    assert isinstance(instance, ansic_multiplicative_expression_complement)

@given(instance=ansic_multiplicative_expression_linha_strategy)
@settings(max_examples=50)
def test_ansic_multiplicative_expression_linha_instantiation(instance):
    assert isinstance(instance, ansic_multiplicative_expression_linha)

@given(instance=ansic_multiplicative_expression_strategy)
@settings(max_examples=50)
def test_ansic_multiplicative_expression_instantiation(instance):
    assert isinstance(instance, ansic_multiplicative_expression)

@given(instance=ansic_cast_expression_strategy)
@settings(max_examples=50)
def test_ansic_cast_expression_instantiation(instance):
    assert isinstance(instance, ansic_cast_expression)

@given(instance=ansic_unary_expression_strategy)
@settings(max_examples=50)
def test_ansic_unary_expression_instantiation(instance):
    assert isinstance(instance, ansic_unary_expression)



@given(instance=ansic_unary_expression_strategy)
def test_ansic_unary_expression_unary_operator_setter(instance):
    original = instance.unary_operator
    instance.unary_operator = original
    assert instance.unary_operator == original

@given(instance=ansic_argument_expression_list_linha_strategy)
@settings(max_examples=50)
def test_ansic_argument_expression_list_linha_instantiation(instance):
    assert isinstance(instance, ansic_argument_expression_list_linha)

@given(instance=ansic_argument_expression_list_strategy)
@settings(max_examples=50)
def test_ansic_argument_expression_list_instantiation(instance):
    assert isinstance(instance, ansic_argument_expression_list)

@given(instance=ansic_postfix_expression_complement_strategy)
@settings(max_examples=50)
def test_ansic_postfix_expression_complement_instantiation(instance):
    assert isinstance(instance, ansic_postfix_expression_complement)



@given(instance=ansic_postfix_expression_complement_strategy)
def test_ansic_postfix_expression_complement_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=ansic_conditional_expression_strategy)
@settings(max_examples=50)
def test_ansic_conditional_expression_instantiation(instance):
    assert isinstance(instance, ansic_conditional_expression)

@given(instance=ansic_primary_expression_strategy)
@settings(max_examples=50)
def test_ansic_primary_expression_instantiation(instance):
    assert isinstance(instance, ansic_primary_expression)



@given(instance=ansic_primary_expression_strategy)
def test_ansic_primary_expression_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=ansic_identifier_list_linha_strategy)
@settings(max_examples=50)
def test_ansic_identifier_list_linha_instantiation(instance):
    assert isinstance(instance, ansic_identifier_list_linha)

@given(instance=ansic_initializer_list_complement_strategy)
@settings(max_examples=50)
def test_ansic_initializer_list_complement_instantiation(instance):
    assert isinstance(instance, ansic_initializer_list_complement)

@given(instance=ansic_initializer_list_linha_strategy)
@settings(max_examples=50)
def test_ansic_initializer_list_linha_instantiation(instance):
    assert isinstance(instance, ansic_initializer_list_linha)

@given(instance=ansic_init_declarator_list_linha_strategy)
@settings(max_examples=50)
def test_ansic_init_declarator_list_linha_instantiation(instance):
    assert isinstance(instance, ansic_init_declarator_list_linha)

@given(instance=ansic_designation_strategy)
@settings(max_examples=50)
def test_ansic_designation_instantiation(instance):
    assert isinstance(instance, ansic_designation)

@given(instance=ansic_postfix_expression_linha_strategy)
@settings(max_examples=50)
def test_ansic_postfix_expression_linha_instantiation(instance):
    assert isinstance(instance, ansic_postfix_expression_linha)

@given(instance=ansic_postfix_expression_strategy)
@settings(max_examples=50)
def test_ansic_postfix_expression_instantiation(instance):
    assert isinstance(instance, ansic_postfix_expression)

@given(instance=ansic_generic_assoc_list_linha_strategy)
@settings(max_examples=50)
def test_ansic_generic_assoc_list_linha_instantiation(instance):
    assert isinstance(instance, ansic_generic_assoc_list_linha)

@given(instance=ansic_generic_association_strategy)
@settings(max_examples=50)
def test_ansic_generic_association_instantiation(instance):
    assert isinstance(instance, ansic_generic_association)



@given(instance=ansic_generic_association_strategy)
def test_ansic_generic_association_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=ansic_generic_assoc_list_strategy)
@settings(max_examples=50)
def test_ansic_generic_assoc_list_instantiation(instance):
    assert isinstance(instance, ansic_generic_assoc_list)

@given(instance=ansic_generic_selection_strategy)
@settings(max_examples=50)
def test_ansic_generic_selection_instantiation(instance):
    assert isinstance(instance, ansic_generic_selection)



@given(instance=ansic_generic_selection_strategy)
def test_ansic_generic_selection__generic_setter(instance):
    original = instance._generic
    instance._generic = original
    assert instance._generic == original

@given(instance=ansic_expression_strategy)
@settings(max_examples=50)
def test_ansic_expression_instantiation(instance):
    assert isinstance(instance, ansic_expression)

@given(instance=ansic_constant_strategy)
@settings(max_examples=50)
def test_ansic_constant_instantiation(instance):
    assert isinstance(instance, ansic_constant)



@given(instance=ansic_constant_strategy)
def test_ansic_constant_enumz_setter(instance):
    original = instance.enumz
    instance.enumz = original
    assert instance.enumz == original



@given(instance=ansic_constant_strategy)
def test_ansic_constant_f_constant_setter(instance):
    original = instance.f_constant
    instance.f_constant = original
    assert instance.f_constant == original



@given(instance=ansic_constant_strategy)
def test_ansic_constant_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original



@given(instance=ansic_constant_strategy)
def test_ansic_constant_i_constant_setter(instance):
    original = instance.i_constant
    instance.i_constant = original
    assert instance.i_constant == original

@given(instance=ansic_parameter_type_list_strategy)
@settings(max_examples=50)
def test_ansic_parameter_type_list_instantiation(instance):
    assert isinstance(instance, ansic_parameter_type_list)

@given(instance=ansic_assignment_expression_strategy)
@settings(max_examples=50)
def test_ansic_assignment_expression_instantiation(instance):
    assert isinstance(instance, ansic_assignment_expression)



@given(instance=ansic_assignment_expression_strategy)
def test_ansic_assignment_expression_assignment_operator_setter(instance):
    original = instance.assignment_operator
    instance.assignment_operator = original
    assert instance.assignment_operator == original

@given(instance=ansic_direct_abstract_declarator_complement_strategy)
@settings(max_examples=50)
def test_ansic_direct_abstract_declarator_complement_instantiation(instance):
    assert isinstance(instance, ansic_direct_abstract_declarator_complement)

@given(instance=ansic_initializer_list_strategy)
@settings(max_examples=50)
def test_ansic_initializer_list_instantiation(instance):
    assert isinstance(instance, ansic_initializer_list)

@given(instance=ansic_initializer_strategy)
@settings(max_examples=50)
def test_ansic_initializer_instantiation(instance):
    assert isinstance(instance, ansic_initializer)

@given(instance=ansic_direct_abstract_declarator_linha_strategy)
@settings(max_examples=50)
def test_ansic_direct_abstract_declarator_linha_instantiation(instance):
    assert isinstance(instance, ansic_direct_abstract_declarator_linha)

@given(instance=ansic_direct_abstract_declarator_strategy)
@settings(max_examples=50)
def test_ansic_direct_abstract_declarator_instantiation(instance):
    assert isinstance(instance, ansic_direct_abstract_declarator)

@given(instance=ansic_abstract_declarator_strategy)
@settings(max_examples=50)
def test_ansic_abstract_declarator_instantiation(instance):
    assert isinstance(instance, ansic_abstract_declarator)

@given(instance=ansic_parameter_list_linha_strategy)
@settings(max_examples=50)
def test_ansic_parameter_list_linha_instantiation(instance):
    assert isinstance(instance, ansic_parameter_list_linha)

@given(instance=ansic_parameter_declaration_strategy)
@settings(max_examples=50)
def test_ansic_parameter_declaration_instantiation(instance):
    assert isinstance(instance, ansic_parameter_declaration)

@given(instance=ansic_parameter_lista_strategy)
@settings(max_examples=50)
def test_ansic_parameter_lista_instantiation(instance):
    assert isinstance(instance, ansic_parameter_lista)

@given(instance=ansic_identifier_list_strategy)
@settings(max_examples=50)
def test_ansic_identifier_list_instantiation(instance):
    assert isinstance(instance, ansic_identifier_list)



@given(instance=ansic_identifier_list_strategy)
def test_ansic_identifier_list_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=ansic_direct_declarator_complemento_strategy)
@settings(max_examples=50)
def test_ansic_direct_declarator_complemento_instantiation(instance):
    assert isinstance(instance, ansic_direct_declarator_complemento)

@given(instance=ansic_direct_declarator_linha_strategy)
@settings(max_examples=50)
def test_ansic_direct_declarator_linha_instantiation(instance):
    assert isinstance(instance, ansic_direct_declarator_linha)

@given(instance=ansic_type_qualifier_list_linha_strategy)
@settings(max_examples=50)
def test_ansic_type_qualifier_list_linha_instantiation(instance):
    assert isinstance(instance, ansic_type_qualifier_list_linha)

@given(instance=direct_abstract_declarator_complement_strategy)
@settings(max_examples=50)
def test_direct_abstract_declarator_complement_instantiation(instance):
    assert isinstance(instance, direct_abstract_declarator_complement)

@given(instance=ansic_type_qualifier_list_strategy)
@settings(max_examples=50)
def test_ansic_type_qualifier_list_instantiation(instance):
    assert isinstance(instance, ansic_type_qualifier_list)

@given(instance=ansic_direct_declarator_strategy)
@settings(max_examples=50)
def test_ansic_direct_declarator_instantiation(instance):
    assert isinstance(instance, ansic_direct_declarator)



@given(instance=ansic_direct_declarator_strategy)
def test_ansic_direct_declarator_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=ansic_pointer_strategy)
@settings(max_examples=50)
def test_ansic_pointer_instantiation(instance):
    assert isinstance(instance, ansic_pointer)

@given(instance=ansic_declaration_list_linha_strategy)
@settings(max_examples=50)
def test_ansic_declaration_list_linha_instantiation(instance):
    assert isinstance(instance, ansic_declaration_list_linha)

@given(instance=ansic_compound_statement_strategy)
@settings(max_examples=50)
def test_ansic_compound_statement_instantiation(instance):
    assert isinstance(instance, ansic_compound_statement)

@given(instance=ansic_declaration_list_strategy)
@settings(max_examples=50)
def test_ansic_declaration_list_instantiation(instance):
    assert isinstance(instance, ansic_declaration_list)

@given(instance=ansic_init_declarator_list_strategy)
@settings(max_examples=50)
def test_ansic_init_declarator_list_instantiation(instance):
    assert isinstance(instance, ansic_init_declarator_list)

@given(instance=ansic_struct_declaration_list_strategy)
@settings(max_examples=50)
def test_ansic_struct_declaration_list_instantiation(instance):
    assert isinstance(instance, ansic_struct_declaration_list)

@given(instance=ansic_declarator_strategy)
@settings(max_examples=50)
def test_ansic_declarator_instantiation(instance):
    assert isinstance(instance, ansic_declarator)

@given(instance=ansic_struct_declarator_list_linha_strategy)
@settings(max_examples=50)
def test_ansic_struct_declarator_list_linha_instantiation(instance):
    assert isinstance(instance, ansic_struct_declarator_list_linha)

@given(instance=ansic_struct_declarator_strategy)
@settings(max_examples=50)
def test_ansic_struct_declarator_instantiation(instance):
    assert isinstance(instance, ansic_struct_declarator)

@given(instance=ansic_static_assert_declaration_strategy)
@settings(max_examples=50)
def test_ansic_static_assert_declaration_instantiation(instance):
    assert isinstance(instance, ansic_static_assert_declaration)

@given(instance=ansic_struct_declarator_list_strategy)
@settings(max_examples=50)
def test_ansic_struct_declarator_list_instantiation(instance):
    assert isinstance(instance, ansic_struct_declarator_list)

@given(instance=ansic_specifier_qualifier_list_strategy)
@settings(max_examples=50)
def test_ansic_specifier_qualifier_list_instantiation(instance):
    assert isinstance(instance, ansic_specifier_qualifier_list)

@given(instance=ansic_struct_declaration_list_linha_strategy)
@settings(max_examples=50)
def test_ansic_struct_declaration_list_linha_instantiation(instance):
    assert isinstance(instance, ansic_struct_declaration_list_linha)

@given(instance=ansic_struct_declaration_strategy)
@settings(max_examples=50)
def test_ansic_struct_declaration_instantiation(instance):
    assert isinstance(instance, ansic_struct_declaration)

@given(instance=ansic_struct_or_union_specifier_complement_strategy)
@settings(max_examples=50)
def test_ansic_struct_or_union_specifier_complement_instantiation(instance):
    assert isinstance(instance, ansic_struct_or_union_specifier_complement)

@given(instance=ansic_declaration_strategy)
@settings(max_examples=50)
def test_ansic_declaration_instantiation(instance):
    assert isinstance(instance, ansic_declaration)

@given(instance=ansic_function_definition_strategy)
@settings(max_examples=50)
def test_ansic_function_definition_instantiation(instance):
    assert isinstance(instance, ansic_function_definition)

@given(instance=ansic_translation_unit_linha_strategy)
@settings(max_examples=50)
def test_ansic_translation_unit_linha_instantiation(instance):
    assert isinstance(instance, ansic_translation_unit_linha)

@given(instance=ansic_enumeration_constant_strategy)
@settings(max_examples=50)
def test_ansic_enumeration_constant_instantiation(instance):
    assert isinstance(instance, ansic_enumeration_constant)



@given(instance=ansic_enumeration_constant_strategy)
def test_ansic_enumeration_constant_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=ansic_enumerator_list_linha_strategy)
@settings(max_examples=50)
def test_ansic_enumerator_list_linha_instantiation(instance):
    assert isinstance(instance, ansic_enumerator_list_linha)

@given(instance=ansic_enumerator_strategy)
@settings(max_examples=50)
def test_ansic_enumerator_instantiation(instance):
    assert isinstance(instance, ansic_enumerator)

@given(instance=ansic_enumerator_list_strategy)
@settings(max_examples=50)
def test_ansic_enumerator_list_instantiation(instance):
    assert isinstance(instance, ansic_enumerator_list)

@given(instance=ansic_enum_specifier_strategy)
@settings(max_examples=50)
def test_ansic_enum_specifier_instantiation(instance):
    assert isinstance(instance, ansic_enum_specifier)



@given(instance=ansic_enum_specifier_strategy)
def test_ansic_enum_specifier_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=ansic_struct_or_union_specifier_strategy)
@settings(max_examples=50)
def test_ansic_struct_or_union_specifier_instantiation(instance):
    assert isinstance(instance, ansic_struct_or_union_specifier)



@given(instance=ansic_struct_or_union_specifier_strategy)
def test_ansic_struct_or_union_specifier_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original



@given(instance=ansic_struct_or_union_specifier_strategy)
def test_ansic_struct_or_union_specifier_struct_or_union_setter(instance):
    original = instance.struct_or_union
    instance.struct_or_union = original
    assert instance.struct_or_union == original

@given(instance=ansic_atomic_type_specifier_strategy)
@settings(max_examples=50)
def test_ansic_atomic_type_specifier_instantiation(instance):
    assert isinstance(instance, ansic_atomic_type_specifier)

@given(instance=ansic_constant_expression_strategy)
@settings(max_examples=50)
def test_ansic_constant_expression_instantiation(instance):
    assert isinstance(instance, ansic_constant_expression)

@given(instance=ansic_alignment_specifier_strategy)
@settings(max_examples=50)
def test_ansic_alignment_specifier_instantiation(instance):
    assert isinstance(instance, ansic_alignment_specifier)

@given(instance=ansic_type_qualifier_strategy)
@settings(max_examples=50)
def test_ansic_type_qualifier_instantiation(instance):
    assert isinstance(instance, ansic_type_qualifier)



@given(instance=ansic_type_qualifier_strategy)
def test_ansic_type_qualifier_namez_setter(instance):
    original = instance.namez
    instance.namez = original
    assert instance.namez == original

@given(instance=ansic_type_specifier_strategy)
@settings(max_examples=50)
def test_ansic_type_specifier_instantiation(instance):
    assert isinstance(instance, ansic_type_specifier)



@given(instance=ansic_type_specifier_strategy)
def test_ansic_type_specifier_type_name_str_setter(instance):
    original = instance.type_name_str
    instance.type_name_str = original
    assert instance.type_name_str == original

@given(instance=ansic_declaration_specifiers_strategy)
@settings(max_examples=50)
def test_ansic_declaration_specifiers_instantiation(instance):
    assert isinstance(instance, ansic_declaration_specifiers)



@given(instance=ansic_declaration_specifiers_strategy)
def test_ansic_declaration_specifiers_storage_class_specifier_setter(instance):
    original = instance.storage_class_specifier
    instance.storage_class_specifier = original
    assert instance.storage_class_specifier == original



@given(instance=ansic_declaration_specifiers_strategy)
def test_ansic_declaration_specifiers_function_specifier_setter(instance):
    original = instance.function_specifier
    instance.function_specifier = original
    assert instance.function_specifier == original

@given(instance=ansic_external_declaration_strategy)
@settings(max_examples=50)
def test_ansic_external_declaration_instantiation(instance):
    assert isinstance(instance, ansic_external_declaration)

@given(instance=ansic_translation_unit_strategy)
@settings(max_examples=50)
def test_ansic_translation_unit_instantiation(instance):
    assert isinstance(instance, ansic_translation_unit)

@given(instance=ansic_DomainModel_strategy)
@settings(max_examples=50)
def test_ansic_domainmodel_instantiation(instance):
    assert isinstance(instance, ansic_DomainModel)

@given(instance=translation_unit_linha_strategy)
@settings(max_examples=50)
def test_translation_unit_linha_instantiation(instance):
    assert isinstance(instance, translation_unit_linha)

@given(instance=ansic_TranlationUnitLinhaAction_strategy)
@settings(max_examples=50)
def test_ansic_tranlationunitlinhaaction_instantiation(instance):
    assert isinstance(instance, ansic_TranlationUnitLinhaAction)

@given(instance=init_declarator_list_linha_strategy)
@settings(max_examples=50)
def test_init_declarator_list_linha_instantiation(instance):
    assert isinstance(instance, init_declarator_list_linha)

@given(instance=ansic_InitDecclaratorListLinhaAction_strategy)
@settings(max_examples=50)
def test_ansic_initdecclaratorlistlinhaaction_instantiation(instance):
    assert isinstance(instance, ansic_InitDecclaratorListLinhaAction)

@given(instance=unary_expression_strategy)
@settings(max_examples=50)
def test_unary_expression_instantiation(instance):
    assert isinstance(instance, unary_expression)

@given(instance=ansic_PlusPlus_strategy)
@settings(max_examples=50)
def test_ansic_plusplus_instantiation(instance):
    assert isinstance(instance, ansic_PlusPlus)



@given(instance=ansic_PlusPlus_strategy)
def test_ansic_plusplus_plus_setter(instance):
    original = instance.plus
    instance.plus = original
    assert instance.plus == original

@given(instance=argument_expression_list_linha_strategy)
@settings(max_examples=50)
def test_argument_expression_list_linha_instantiation(instance):
    assert isinstance(instance, argument_expression_list_linha)

@given(instance=ansic_ArgumentExpressionListLinhaAction_strategy)
@settings(max_examples=50)
def test_ansic_argumentexpressionlistlinhaaction_instantiation(instance):
    assert isinstance(instance, ansic_ArgumentExpressionListLinhaAction)

@given(instance=postfix_expression_complement_strategy)
@settings(max_examples=50)
def test_postfix_expression_complement_instantiation(instance):
    assert isinstance(instance, postfix_expression_complement)

@given(instance=ansic_PostFixEmpryParams_strategy)
@settings(max_examples=50)
def test_ansic_postfixempryparams_instantiation(instance):
    assert isinstance(instance, ansic_PostFixEmpryParams)

@given(instance=designator_list_linha_strategy)
@settings(max_examples=50)
def test_designator_list_linha_instantiation(instance):
    assert isinstance(instance, designator_list_linha)

@given(instance=ansic_DesignatorListLinhaAction_strategy)
@settings(max_examples=50)
def test_ansic_designatorlistlinhaaction_instantiation(instance):
    assert isinstance(instance, ansic_DesignatorListLinhaAction)

@given(instance=initializer_list_linha_strategy)
@settings(max_examples=50)
def test_initializer_list_linha_instantiation(instance):
    assert isinstance(instance, initializer_list_linha)

@given(instance=ansic_InitializerListLinhaAction_strategy)
@settings(max_examples=50)
def test_ansic_initializerlistlinhaaction_instantiation(instance):
    assert isinstance(instance, ansic_InitializerListLinhaAction)

@given(instance=postfix_expression_linha_strategy)
@settings(max_examples=50)
def test_postfix_expression_linha_instantiation(instance):
    assert isinstance(instance, postfix_expression_linha)

@given(instance=ansic_PostfixExpressionLinhaAction_strategy)
@settings(max_examples=50)
def test_ansic_postfixexpressionlinhaaction_instantiation(instance):
    assert isinstance(instance, ansic_PostfixExpressionLinhaAction)

@given(instance=generic_assoc_list_linha_strategy)
@settings(max_examples=50)
def test_generic_assoc_list_linha_instantiation(instance):
    assert isinstance(instance, generic_assoc_list_linha)

@given(instance=ansic_GenericAssocListLinhaAction_strategy)
@settings(max_examples=50)
def test_ansic_genericassoclistlinhaaction_instantiation(instance):
    assert isinstance(instance, ansic_GenericAssocListLinhaAction)

@given(instance=ansic_string_ufcg_strategy)
@settings(max_examples=50)
def test_ansic_string_ufcg_instantiation(instance):
    assert isinstance(instance, ansic_string_ufcg)



@given(instance=ansic_string_ufcg_strategy)
def test_ansic_string_ufcg_string_literal_setter(instance):
    original = instance.string_literal
    instance.string_literal = original
    assert instance.string_literal == original



@given(instance=ansic_string_ufcg_strategy)
def test_ansic_string_ufcg___func___setter(instance):
    original = instance.__func__
    instance.__func__ = original
    assert instance.__func__ == original

@given(instance=identifier_list_linha_strategy)
@settings(max_examples=50)
def test_identifier_list_linha_instantiation(instance):
    assert isinstance(instance, identifier_list_linha)

@given(instance=ansic_IdentifierListLinhaAction_strategy)
@settings(max_examples=50)
def test_ansic_identifierlistlinhaaction_instantiation(instance):
    assert isinstance(instance, ansic_IdentifierListLinhaAction)



@given(instance=ansic_IdentifierListLinhaAction_strategy)
def test_ansic_identifierlistlinhaaction_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=direct_abstract_declarator_linha_strategy)
@settings(max_examples=50)
def test_direct_abstract_declarator_linha_instantiation(instance):
    assert isinstance(instance, direct_abstract_declarator_linha)

@given(instance=ansic_DirectAbstractDeclarratorLinhaAction_strategy)
@settings(max_examples=50)
def test_ansic_directabstractdeclarratorlinhaaction_instantiation(instance):
    assert isinstance(instance, ansic_DirectAbstractDeclarratorLinhaAction)

@given(instance=type_qualifier_list_linha_strategy)
@settings(max_examples=50)
def test_type_qualifier_list_linha_instantiation(instance):
    assert isinstance(instance, type_qualifier_list_linha)

@given(instance=ansic_TypeQualifierListLinhaAtion_strategy)
@settings(max_examples=50)
def test_ansic_typequalifierlistlinhaation_instantiation(instance):
    assert isinstance(instance, ansic_TypeQualifierListLinhaAtion)

@given(instance=declaration_list_linha_strategy)
@settings(max_examples=50)
def test_declaration_list_linha_instantiation(instance):
    assert isinstance(instance, declaration_list_linha)

@given(instance=ansic_DeclarationListLinhaAction_strategy)
@settings(max_examples=50)
def test_ansic_declarationlistlinhaaction_instantiation(instance):
    assert isinstance(instance, ansic_DeclarationListLinhaAction)

@given(instance=struct_declarator_list_linha_strategy)
@settings(max_examples=50)
def test_struct_declarator_list_linha_instantiation(instance):
    assert isinstance(instance, struct_declarator_list_linha)

@given(instance=ansic_StructDeclaratorListLinhaAction_strategy)
@settings(max_examples=50)
def test_ansic_structdeclaratorlistlinhaaction_instantiation(instance):
    assert isinstance(instance, ansic_StructDeclaratorListLinhaAction)

@given(instance=struct_declaration_list_linha_strategy)
@settings(max_examples=50)
def test_struct_declaration_list_linha_instantiation(instance):
    assert isinstance(instance, struct_declaration_list_linha)

@given(instance=ansic_StructDeclarationListLinhaAction_strategy)
@settings(max_examples=50)
def test_ansic_structdeclarationlistlinhaaction_instantiation(instance):
    assert isinstance(instance, ansic_StructDeclarationListLinhaAction)

@given(instance=struct_or_union_specifier_complement_strategy)
@settings(max_examples=50)
def test_struct_or_union_specifier_complement_instantiation(instance):
    assert isinstance(instance, struct_or_union_specifier_complement)

@given(instance=ansic_StructOrUnionSpecifierComplementAction_strategy)
@settings(max_examples=50)
def test_ansic_structorunionspecifiercomplementaction_instantiation(instance):
    assert isinstance(instance, ansic_StructOrUnionSpecifierComplementAction)

@given(instance=enumerator_list_linha_strategy)
@settings(max_examples=50)
def test_enumerator_list_linha_instantiation(instance):
    assert isinstance(instance, enumerator_list_linha)

@given(instance=ansic_EnumeratorListLinhaAction_strategy)
@settings(max_examples=50)
def test_ansic_enumeratorlistlinhaaction_instantiation(instance):
    assert isinstance(instance, ansic_EnumeratorListLinhaAction)

@given(instance=ansic_init_declarator_strategy)
@settings(max_examples=50)
def test_ansic_init_declarator_instantiation(instance):
    assert isinstance(instance, ansic_init_declarator)

@given(instance=ansic_expression_linha_strategy)
@settings(max_examples=50)
def test_ansic_expression_linha_instantiation(instance):
    assert isinstance(instance, ansic_expression_linha)

@given(instance=postfix_expression_strategy)
@settings(max_examples=50)
def test_postfix_expression_instantiation(instance):
    assert isinstance(instance, postfix_expression)

@given(instance=ansic_type_name_strategy)
@settings(max_examples=50)
def test_ansic_type_name_instantiation(instance):
    assert isinstance(instance, ansic_type_name)

@given(instance=ansic_conditional_expression_linha_strategy)
@settings(max_examples=50)
def test_ansic_conditional_expression_linha_instantiation(instance):
    assert isinstance(instance, ansic_conditional_expression_linha)

@given(instance=ansic_logical_or_expression_linha_strategy)
@settings(max_examples=50)
def test_ansic_logical_or_expression_linha_instantiation(instance):
    assert isinstance(instance, ansic_logical_or_expression_linha)

@given(instance=ansic_logical_or_expression_strategy)
@settings(max_examples=50)
def test_ansic_logical_or_expression_instantiation(instance):
    assert isinstance(instance, ansic_logical_or_expression)

@given(instance=ansic_logical_and_expression_linha_strategy)
@settings(max_examples=50)
def test_ansic_logical_and_expression_linha_instantiation(instance):
    assert isinstance(instance, ansic_logical_and_expression_linha)

@given(instance=ansic_logical_and_expression_strategy)
@settings(max_examples=50)
def test_ansic_logical_and_expression_instantiation(instance):
    assert isinstance(instance, ansic_logical_and_expression)

@given(instance=ansic_inclusive_or_expression_linha_strategy)
@settings(max_examples=50)
def test_ansic_inclusive_or_expression_linha_instantiation(instance):
    assert isinstance(instance, ansic_inclusive_or_expression_linha)

@given(instance=ansic_inclusive_or_expression_strategy)
@settings(max_examples=50)
def test_ansic_inclusive_or_expression_instantiation(instance):
    assert isinstance(instance, ansic_inclusive_or_expression)

@given(instance=ansic_exclusive_or_expression_linha_strategy)
@settings(max_examples=50)
def test_ansic_exclusive_or_expression_linha_instantiation(instance):
    assert isinstance(instance, ansic_exclusive_or_expression_linha)

@given(instance=ansic_exclusive_or_expression_strategy)
@settings(max_examples=50)
def test_ansic_exclusive_or_expression_instantiation(instance):
    assert isinstance(instance, ansic_exclusive_or_expression)

@given(instance=ansic_and_expression_linha_strategy)
@settings(max_examples=50)
def test_ansic_and_expression_linha_instantiation(instance):
    assert isinstance(instance, ansic_and_expression_linha)

@given(instance=ansic_and_expression_strategy)
@settings(max_examples=50)
def test_ansic_and_expression_instantiation(instance):
    assert isinstance(instance, ansic_and_expression)

@given(instance=ansic_jump_statement_strategy)
@settings(max_examples=50)
def test_ansic_jump_statement_instantiation(instance):
    assert isinstance(instance, ansic_jump_statement)



@given(instance=ansic_jump_statement_strategy)
def test_ansic_jump_statement_return_vazio_setter(instance):
    original = instance.return_vazio
    instance.return_vazio = original
    assert instance.return_vazio == original



@given(instance=ansic_jump_statement_strategy)
def test_ansic_jump_statement_return__setter(instance):
    original = instance.return_
    instance.return_ = original
    assert instance.return_ == original



@given(instance=ansic_jump_statement_strategy)
def test_ansic_jump_statement_break__setter(instance):
    original = instance.break_
    instance.break_ = original
    assert instance.break_ == original



@given(instance=ansic_jump_statement_strategy)
def test_ansic_jump_statement_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=ansic_iteration_statement_strategy)
@settings(max_examples=50)
def test_ansic_iteration_statement_instantiation(instance):
    assert isinstance(instance, ansic_iteration_statement)

@given(instance=ansic_block_item_list_linha_strategy)
@settings(max_examples=50)
def test_ansic_block_item_list_linha_instantiation(instance):
    assert isinstance(instance, ansic_block_item_list_linha)

@given(instance=ansic_block_item_strategy)
@settings(max_examples=50)
def test_ansic_block_item_instantiation(instance):
    assert isinstance(instance, ansic_block_item)

@given(instance=ansic_block_item_list_strategy)
@settings(max_examples=50)
def test_ansic_block_item_list_instantiation(instance):
    assert isinstance(instance, ansic_block_item_list)

@given(instance=ansic_additive_expression_complement_strategy)
@settings(max_examples=50)
def test_ansic_additive_expression_complement_instantiation(instance):
    assert isinstance(instance, ansic_additive_expression_complement)

@given(instance=ansic_additive_expression_linha_strategy)
@settings(max_examples=50)
def test_ansic_additive_expression_linha_instantiation(instance):
    assert isinstance(instance, ansic_additive_expression_linha)

@given(instance=ansic_selection_statement_strategy)
@settings(max_examples=50)
def test_ansic_selection_statement_instantiation(instance):
    assert isinstance(instance, ansic_selection_statement)

@given(instance=ansic_expression_statement_strategy)
@settings(max_examples=50)
def test_ansic_expression_statement_instantiation(instance):
    assert isinstance(instance, ansic_expression_statement)

@given(instance=ansic_labeled_statement_strategy)
@settings(max_examples=50)
def test_ansic_labeled_statement_instantiation(instance):
    assert isinstance(instance, ansic_labeled_statement)



@given(instance=ansic_labeled_statement_strategy)
def test_ansic_labeled_statement_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=ansic_statement_strategy)
@settings(max_examples=50)
def test_ansic_statement_instantiation(instance):
    assert isinstance(instance, ansic_statement)

@given(instance=ansic_equality_expression_complement_strategy)
@settings(max_examples=50)
def test_ansic_equality_expression_complement_instantiation(instance):
    assert isinstance(instance, ansic_equality_expression_complement)

@given(instance=ansic_equality_expression_linha_strategy)
@settings(max_examples=50)
def test_ansic_equality_expression_linha_instantiation(instance):
    assert isinstance(instance, ansic_equality_expression_linha)

@given(instance=ansic_equality_expression_strategy)
@settings(max_examples=50)
def test_ansic_equality_expression_instantiation(instance):
    assert isinstance(instance, ansic_equality_expression)

@given(instance=ansic_relational_expression_complement_strategy)
@settings(max_examples=50)
def test_ansic_relational_expression_complement_instantiation(instance):
    assert isinstance(instance, ansic_relational_expression_complement)

@given(instance=ansic_relational_expression_linha_strategy)
@settings(max_examples=50)
def test_ansic_relational_expression_linha_instantiation(instance):
    assert isinstance(instance, ansic_relational_expression_linha)
