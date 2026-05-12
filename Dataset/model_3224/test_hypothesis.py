import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    struct_declarator_list_linha,
    myDsl_StructDeclaratorListLinhaAction,
    postfix_expression_linha,
    myDsl_PostfixExpressionLinhaAction,
    generic_assoc_list_linha,
    myDsl_GenericAssocListLinhaAction,
    translation_unit_linha,
    myDsl_TranlationUnitLinhaAction,
    identifier_list_linha,
    myDsl_IdentifierListLinhaAction,
    myDsl_init_declarator,
    myDsl_expression_linha,
    struct_declaration_list_linha,
    myDsl_StructDeclarationListLinhaAction,
    struct_or_union_specifier_complement,
    myDsl_StructOrUnionSpecifierComplementAction,
    enumerator_list_linha,
    myDsl_EnumeratorListLinhaAction,
    myDsl_string_dsl,
    myDsl_conditional_expression_linha,
    myDsl_logical_or_expression_linha,
    myDsl_logical_or_expression,
    myDsl_logical_and_expression_linha,
    myDsl_logical_and_expression,
    postfix_expression,
    myDsl_block_item_list_linha,
    myDsl_block_item,
    myDsl_block_item_list,
    myDsl_inclusive_or_expression_linha,
    myDsl_inclusive_or_expression,
    myDsl_exclusive_or_expression_linha,
    myDsl_exclusive_or_expression,
    myDsl_and_expression_linha,
    myDsl_and_expression,
    myDsl_jump_statement,
    myDsl_iteration_statement,
    myDsl_selection_statement,
    myDsl_expression_statement,
    myDsl_labeled_statement,
    myDsl_statement,
    myDsl_shift_expression_complement,
    myDsl_shift_expression_linha,
    myDsl_shift_expression,
    myDsl_additive_expression_complement,
    myDsl_additive_expression_linha,
    myDsl_equality_expression_complement,
    myDsl_equality_expression_linha,
    myDsl_equality_expression,
    myDsl_relational_expression_complement,
    myDsl_relational_expression_linha,
    myDsl_relational_expression,
    myDsl_additive_expression,
    myDsl_multiplicative_expression_complement,
    myDsl_multiplicative_expression_linha,
    myDsl_multiplicative_expression,
    myDsl_cast_expression,
    myDsl_unary_expression,
    myDsl_argument_expression_list_linha,
    myDsl_argument_expression_list,
    myDsl_postfix_expression_complement,
    myDsl_conditional_expression,
    myDsl_designator_list_linha,
    myDsl_designator,
    myDsl_designator_list,
    myDsl_initializer_list_complement,
    myDsl_initializer_list_linha,
    myDsl_init_declarator_list_linha,
    myDsl_designation,
    myDsl_postfix_expression_linha,
    myDsl_postfix_expression,
    myDsl_generic_assoc_list_linha,
    myDsl_generic_association,
    myDsl_generic_assoc_list,
    myDsl_generic_selection,
    myDsl_expression,
    myDsl_constant,
    myDsl_primary_expression,
    myDsl_identifier_list_linha,
    myDsl_direct_abstract_declarator_complement,
    myDsl_initializer_list,
    myDsl_initializer,
    myDsl_direct_abstract_declarator_linha,
    myDsl_direct_abstract_declarator,
    myDsl_abstract_declarator,
    myDsl_parameter_list_linha,
    myDsl_parameter_declaration,
    myDsl_identifier_list,
    myDsl_parameter_type_list,
    myDsl_assignment_expression,
    myDsl_direct_declarator_complemento,
    myDsl_direct_declarator_linha,
    myDsl_type_qualifier_list_linha,
    direct_abstract_declarator_complement,
    myDsl_type_qualifier_list,
    myDsl_direct_declarator,
    myDsl_pointer,
    myDsl_declaration_list_linha,
    myDsl_compound_statement,
    myDsl_declaration_list,
    myDsl_parameter_lista,
    myDsl_init_declarator_list,
    myDsl_declarator,
    myDsl_struct_declarator_list_linha,
    myDsl_struct_declarator,
    myDsl_static_assert_declaration,
    myDsl_struct_declarator_list,
    myDsl_specifier_qualifier_list,
    myDsl_struct_declaration_list_linha,
    myDsl_struct_declaration,
    myDsl_struct_or_union_specifier_complement,
    myDsl_struct_declaration_list,
    myDsl_enumeration_constant,
    myDsl_enumerator_list_linha,
    myDsl_enumerator,
    myDsl_enumerator_list,
    myDsl_enum_specifier,
    argument_expression_list_linha,
    myDsl_ArgumentExpressionListLinhaAction,
    postfix_expression_complement,
    myDsl_PostFixEmpryParams,
    designator_list_linha,
    myDsl_DesignatorListLinhaAction,
    initializer_list_linha,
    myDsl_InitializerListLinhaAction,
    init_declarator_list_linha,
    myDsl_InitDecclaratorListLinhaAction,
    unary_expression,
    myDsl_PlusPlus,
    direct_abstract_declarator_linha,
    myDsl_DirectAbstractDeclarratorLinhaAction,
    type_qualifier_list_linha,
    myDsl_TypeQualifierListLinhaAtion,
    declaration_list_linha,
    myDsl_DeclarationListLinhaAction,
    myDsl_struct_or_union_specifier,
    myDsl_atomic_type_specifier,
    myDsl_constant_expression,
    myDsl_type_name,
    myDsl_alignment_specifier,
    myDsl_type_qualifier,
    myDsl_type_specifier,
    myDsl_declaration_specifiers,
    myDsl_declaration,
    myDsl_function_definition,
    myDsl_translation_unit_linha,
    myDsl_external_declaration,
    myDsl_translation_unit,
    myDsl_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_struct_declarator_list_linha_is_not_abstract():
    assert not inspect.isabstract(struct_declarator_list_linha)


def test_struct_declarator_list_linha_constructor_exists():
    assert callable(struct_declarator_list_linha.__init__)


def test_struct_declarator_list_linha_constructor_args():
    sig = inspect.signature(struct_declarator_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_structdeclaratorlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(myDsl_StructDeclaratorListLinhaAction)


def test_mydsl_structdeclaratorlistlinhaaction_constructor_exists():
    assert callable(myDsl_StructDeclaratorListLinhaAction.__init__)


def test_mydsl_structdeclaratorlistlinhaaction_constructor_args():
    sig = inspect.signature(myDsl_StructDeclaratorListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_postfix_expression_linha_is_not_abstract():
    assert not inspect.isabstract(postfix_expression_linha)


def test_postfix_expression_linha_constructor_exists():
    assert callable(postfix_expression_linha.__init__)


def test_postfix_expression_linha_constructor_args():
    sig = inspect.signature(postfix_expression_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_postfixexpressionlinhaaction_is_not_abstract():
    assert not inspect.isabstract(myDsl_PostfixExpressionLinhaAction)


def test_mydsl_postfixexpressionlinhaaction_constructor_exists():
    assert callable(myDsl_PostfixExpressionLinhaAction.__init__)


def test_mydsl_postfixexpressionlinhaaction_constructor_args():
    sig = inspect.signature(myDsl_PostfixExpressionLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_generic_assoc_list_linha_is_not_abstract():
    assert not inspect.isabstract(generic_assoc_list_linha)


def test_generic_assoc_list_linha_constructor_exists():
    assert callable(generic_assoc_list_linha.__init__)


def test_generic_assoc_list_linha_constructor_args():
    sig = inspect.signature(generic_assoc_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_genericassoclistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(myDsl_GenericAssocListLinhaAction)


def test_mydsl_genericassoclistlinhaaction_constructor_exists():
    assert callable(myDsl_GenericAssocListLinhaAction.__init__)


def test_mydsl_genericassoclistlinhaaction_constructor_args():
    sig = inspect.signature(myDsl_GenericAssocListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_translation_unit_linha_is_not_abstract():
    assert not inspect.isabstract(translation_unit_linha)


def test_translation_unit_linha_constructor_exists():
    assert callable(translation_unit_linha.__init__)


def test_translation_unit_linha_constructor_args():
    sig = inspect.signature(translation_unit_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_tranlationunitlinhaaction_is_not_abstract():
    assert not inspect.isabstract(myDsl_TranlationUnitLinhaAction)


def test_mydsl_tranlationunitlinhaaction_constructor_exists():
    assert callable(myDsl_TranlationUnitLinhaAction.__init__)


def test_mydsl_tranlationunitlinhaaction_constructor_args():
    sig = inspect.signature(myDsl_TranlationUnitLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_identifier_list_linha_is_not_abstract():
    assert not inspect.isabstract(identifier_list_linha)


def test_identifier_list_linha_constructor_exists():
    assert callable(identifier_list_linha.__init__)


def test_identifier_list_linha_constructor_args():
    sig = inspect.signature(identifier_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_identifierlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(myDsl_IdentifierListLinhaAction)


def test_mydsl_identifierlistlinhaaction_constructor_exists():
    assert callable(myDsl_IdentifierListLinhaAction.__init__)


def test_mydsl_identifierlistlinhaaction_constructor_args():
    sig = inspect.signature(myDsl_IdentifierListLinhaAction.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_mydsl_identifierlistlinhaaction_has_identifier():
    assert hasattr(myDsl_IdentifierListLinhaAction, "identifier")
    descriptor = None
    for klass in myDsl_IdentifierListLinhaAction.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_init_declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl_init_declarator)


def test_mydsl_init_declarator_constructor_exists():
    assert callable(myDsl_init_declarator.__init__)


def test_mydsl_init_declarator_constructor_args():
    sig = inspect.signature(myDsl_init_declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_expression_linha_is_not_abstract():
    assert not inspect.isabstract(myDsl_expression_linha)


def test_mydsl_expression_linha_constructor_exists():
    assert callable(myDsl_expression_linha.__init__)


def test_mydsl_expression_linha_constructor_args():
    sig = inspect.signature(myDsl_expression_linha.__init__)
    params = list(sig.parameters.keys())



def test_struct_declaration_list_linha_is_not_abstract():
    assert not inspect.isabstract(struct_declaration_list_linha)


def test_struct_declaration_list_linha_constructor_exists():
    assert callable(struct_declaration_list_linha.__init__)


def test_struct_declaration_list_linha_constructor_args():
    sig = inspect.signature(struct_declaration_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_structdeclarationlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(myDsl_StructDeclarationListLinhaAction)


def test_mydsl_structdeclarationlistlinhaaction_constructor_exists():
    assert callable(myDsl_StructDeclarationListLinhaAction.__init__)


def test_mydsl_structdeclarationlistlinhaaction_constructor_args():
    sig = inspect.signature(myDsl_StructDeclarationListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_struct_or_union_specifier_complement_is_not_abstract():
    assert not inspect.isabstract(struct_or_union_specifier_complement)


def test_struct_or_union_specifier_complement_constructor_exists():
    assert callable(struct_or_union_specifier_complement.__init__)


def test_struct_or_union_specifier_complement_constructor_args():
    sig = inspect.signature(struct_or_union_specifier_complement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_structorunionspecifiercomplementaction_is_not_abstract():
    assert not inspect.isabstract(myDsl_StructOrUnionSpecifierComplementAction)


def test_mydsl_structorunionspecifiercomplementaction_constructor_exists():
    assert callable(myDsl_StructOrUnionSpecifierComplementAction.__init__)


def test_mydsl_structorunionspecifiercomplementaction_constructor_args():
    sig = inspect.signature(myDsl_StructOrUnionSpecifierComplementAction.__init__)
    params = list(sig.parameters.keys())



def test_enumerator_list_linha_is_not_abstract():
    assert not inspect.isabstract(enumerator_list_linha)


def test_enumerator_list_linha_constructor_exists():
    assert callable(enumerator_list_linha.__init__)


def test_enumerator_list_linha_constructor_args():
    sig = inspect.signature(enumerator_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_enumeratorlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(myDsl_EnumeratorListLinhaAction)


def test_mydsl_enumeratorlistlinhaaction_constructor_exists():
    assert callable(myDsl_EnumeratorListLinhaAction.__init__)


def test_mydsl_enumeratorlistlinhaaction_constructor_args():
    sig = inspect.signature(myDsl_EnumeratorListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_string_dsl_is_not_abstract():
    assert not inspect.isabstract(myDsl_string_dsl)


def test_mydsl_string_dsl_constructor_exists():
    assert callable(myDsl_string_dsl.__init__)


def test_mydsl_string_dsl_constructor_args():
    sig = inspect.signature(myDsl_string_dsl.__init__)
    params = list(sig.parameters.keys())
    assert "__func__" in params, "Missing parameter '__func__'"
    assert "string_literal" in params, "Missing parameter 'string_literal'"

def test_mydsl_string_dsl_has___func__():
    assert hasattr(myDsl_string_dsl, "__func__")
    descriptor = None
    for klass in myDsl_string_dsl.__mro__:
        if "__func__" in klass.__dict__:
            descriptor = klass.__dict__["__func__"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_string_dsl_has_string_literal():
    assert hasattr(myDsl_string_dsl, "string_literal")
    descriptor = None
    for klass in myDsl_string_dsl.__mro__:
        if "string_literal" in klass.__dict__:
            descriptor = klass.__dict__["string_literal"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_conditional_expression_linha_is_not_abstract():
    assert not inspect.isabstract(myDsl_conditional_expression_linha)


def test_mydsl_conditional_expression_linha_constructor_exists():
    assert callable(myDsl_conditional_expression_linha.__init__)


def test_mydsl_conditional_expression_linha_constructor_args():
    sig = inspect.signature(myDsl_conditional_expression_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_logical_or_expression_linha_is_not_abstract():
    assert not inspect.isabstract(myDsl_logical_or_expression_linha)


def test_mydsl_logical_or_expression_linha_constructor_exists():
    assert callable(myDsl_logical_or_expression_linha.__init__)


def test_mydsl_logical_or_expression_linha_constructor_args():
    sig = inspect.signature(myDsl_logical_or_expression_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_logical_or_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_logical_or_expression)


def test_mydsl_logical_or_expression_constructor_exists():
    assert callable(myDsl_logical_or_expression.__init__)


def test_mydsl_logical_or_expression_constructor_args():
    sig = inspect.signature(myDsl_logical_or_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_logical_and_expression_linha_is_not_abstract():
    assert not inspect.isabstract(myDsl_logical_and_expression_linha)


def test_mydsl_logical_and_expression_linha_constructor_exists():
    assert callable(myDsl_logical_and_expression_linha.__init__)


def test_mydsl_logical_and_expression_linha_constructor_args():
    sig = inspect.signature(myDsl_logical_and_expression_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_logical_and_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_logical_and_expression)


def test_mydsl_logical_and_expression_constructor_exists():
    assert callable(myDsl_logical_and_expression.__init__)


def test_mydsl_logical_and_expression_constructor_args():
    sig = inspect.signature(myDsl_logical_and_expression.__init__)
    params = list(sig.parameters.keys())



def test_postfix_expression_is_not_abstract():
    assert not inspect.isabstract(postfix_expression)


def test_postfix_expression_constructor_exists():
    assert callable(postfix_expression.__init__)


def test_postfix_expression_constructor_args():
    sig = inspect.signature(postfix_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_block_item_list_linha_is_not_abstract():
    assert not inspect.isabstract(myDsl_block_item_list_linha)


def test_mydsl_block_item_list_linha_constructor_exists():
    assert callable(myDsl_block_item_list_linha.__init__)


def test_mydsl_block_item_list_linha_constructor_args():
    sig = inspect.signature(myDsl_block_item_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_block_item_is_not_abstract():
    assert not inspect.isabstract(myDsl_block_item)


def test_mydsl_block_item_constructor_exists():
    assert callable(myDsl_block_item.__init__)


def test_mydsl_block_item_constructor_args():
    sig = inspect.signature(myDsl_block_item.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_block_item_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_block_item_list)


def test_mydsl_block_item_list_constructor_exists():
    assert callable(myDsl_block_item_list.__init__)


def test_mydsl_block_item_list_constructor_args():
    sig = inspect.signature(myDsl_block_item_list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_inclusive_or_expression_linha_is_not_abstract():
    assert not inspect.isabstract(myDsl_inclusive_or_expression_linha)


def test_mydsl_inclusive_or_expression_linha_constructor_exists():
    assert callable(myDsl_inclusive_or_expression_linha.__init__)


def test_mydsl_inclusive_or_expression_linha_constructor_args():
    sig = inspect.signature(myDsl_inclusive_or_expression_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_inclusive_or_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_inclusive_or_expression)


def test_mydsl_inclusive_or_expression_constructor_exists():
    assert callable(myDsl_inclusive_or_expression.__init__)


def test_mydsl_inclusive_or_expression_constructor_args():
    sig = inspect.signature(myDsl_inclusive_or_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_exclusive_or_expression_linha_is_not_abstract():
    assert not inspect.isabstract(myDsl_exclusive_or_expression_linha)


def test_mydsl_exclusive_or_expression_linha_constructor_exists():
    assert callable(myDsl_exclusive_or_expression_linha.__init__)


def test_mydsl_exclusive_or_expression_linha_constructor_args():
    sig = inspect.signature(myDsl_exclusive_or_expression_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_exclusive_or_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_exclusive_or_expression)


def test_mydsl_exclusive_or_expression_constructor_exists():
    assert callable(myDsl_exclusive_or_expression.__init__)


def test_mydsl_exclusive_or_expression_constructor_args():
    sig = inspect.signature(myDsl_exclusive_or_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_and_expression_linha_is_not_abstract():
    assert not inspect.isabstract(myDsl_and_expression_linha)


def test_mydsl_and_expression_linha_constructor_exists():
    assert callable(myDsl_and_expression_linha.__init__)


def test_mydsl_and_expression_linha_constructor_args():
    sig = inspect.signature(myDsl_and_expression_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_and_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_and_expression)


def test_mydsl_and_expression_constructor_exists():
    assert callable(myDsl_and_expression.__init__)


def test_mydsl_and_expression_constructor_args():
    sig = inspect.signature(myDsl_and_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_jump_statement_is_not_abstract():
    assert not inspect.isabstract(myDsl_jump_statement)


def test_mydsl_jump_statement_constructor_exists():
    assert callable(myDsl_jump_statement.__init__)


def test_mydsl_jump_statement_constructor_args():
    sig = inspect.signature(myDsl_jump_statement.__init__)
    params = list(sig.parameters.keys())
    assert "break_" in params, "Missing parameter 'break_'"
    assert "return_" in params, "Missing parameter 'return_'"
    assert "return_vazio" in params, "Missing parameter 'return_vazio'"
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_mydsl_jump_statement_has_break_():
    assert hasattr(myDsl_jump_statement, "break_")
    descriptor = None
    for klass in myDsl_jump_statement.__mro__:
        if "break_" in klass.__dict__:
            descriptor = klass.__dict__["break_"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_jump_statement_has_return_():
    assert hasattr(myDsl_jump_statement, "return_")
    descriptor = None
    for klass in myDsl_jump_statement.__mro__:
        if "return_" in klass.__dict__:
            descriptor = klass.__dict__["return_"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_jump_statement_has_return_vazio():
    assert hasattr(myDsl_jump_statement, "return_vazio")
    descriptor = None
    for klass in myDsl_jump_statement.__mro__:
        if "return_vazio" in klass.__dict__:
            descriptor = klass.__dict__["return_vazio"]
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



def test_mydsl_iteration_statement_is_not_abstract():
    assert not inspect.isabstract(myDsl_iteration_statement)


def test_mydsl_iteration_statement_constructor_exists():
    assert callable(myDsl_iteration_statement.__init__)


def test_mydsl_iteration_statement_constructor_args():
    sig = inspect.signature(myDsl_iteration_statement.__init__)
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



def test_mydsl_labeled_statement_is_not_abstract():
    assert not inspect.isabstract(myDsl_labeled_statement)


def test_mydsl_labeled_statement_constructor_exists():
    assert callable(myDsl_labeled_statement.__init__)


def test_mydsl_labeled_statement_constructor_args():
    sig = inspect.signature(myDsl_labeled_statement.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_mydsl_labeled_statement_has_identifier():
    assert hasattr(myDsl_labeled_statement, "identifier")
    descriptor = None
    for klass in myDsl_labeled_statement.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_statement_is_not_abstract():
    assert not inspect.isabstract(myDsl_statement)


def test_mydsl_statement_constructor_exists():
    assert callable(myDsl_statement.__init__)


def test_mydsl_statement_constructor_args():
    sig = inspect.signature(myDsl_statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_shift_expression_complement_is_not_abstract():
    assert not inspect.isabstract(myDsl_shift_expression_complement)


def test_mydsl_shift_expression_complement_constructor_exists():
    assert callable(myDsl_shift_expression_complement.__init__)


def test_mydsl_shift_expression_complement_constructor_args():
    sig = inspect.signature(myDsl_shift_expression_complement.__init__)
    params = list(sig.parameters.keys())
    assert "sright" in params, "Missing parameter 'sright'"
    assert "sleft" in params, "Missing parameter 'sleft'"

def test_mydsl_shift_expression_complement_has_sright():
    assert hasattr(myDsl_shift_expression_complement, "sright")
    descriptor = None
    for klass in myDsl_shift_expression_complement.__mro__:
        if "sright" in klass.__dict__:
            descriptor = klass.__dict__["sright"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_shift_expression_complement_has_sleft():
    assert hasattr(myDsl_shift_expression_complement, "sleft")
    descriptor = None
    for klass in myDsl_shift_expression_complement.__mro__:
        if "sleft" in klass.__dict__:
            descriptor = klass.__dict__["sleft"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_shift_expression_linha_is_not_abstract():
    assert not inspect.isabstract(myDsl_shift_expression_linha)


def test_mydsl_shift_expression_linha_constructor_exists():
    assert callable(myDsl_shift_expression_linha.__init__)


def test_mydsl_shift_expression_linha_constructor_args():
    sig = inspect.signature(myDsl_shift_expression_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_shift_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_shift_expression)


def test_mydsl_shift_expression_constructor_exists():
    assert callable(myDsl_shift_expression.__init__)


def test_mydsl_shift_expression_constructor_args():
    sig = inspect.signature(myDsl_shift_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_additive_expression_complement_is_not_abstract():
    assert not inspect.isabstract(myDsl_additive_expression_complement)


def test_mydsl_additive_expression_complement_constructor_exists():
    assert callable(myDsl_additive_expression_complement.__init__)


def test_mydsl_additive_expression_complement_constructor_args():
    sig = inspect.signature(myDsl_additive_expression_complement.__init__)
    params = list(sig.parameters.keys())
    assert "menos" in params, "Missing parameter 'menos'"
    assert "mais" in params, "Missing parameter 'mais'"

def test_mydsl_additive_expression_complement_has_menos():
    assert hasattr(myDsl_additive_expression_complement, "menos")
    descriptor = None
    for klass in myDsl_additive_expression_complement.__mro__:
        if "menos" in klass.__dict__:
            descriptor = klass.__dict__["menos"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_additive_expression_complement_has_mais():
    assert hasattr(myDsl_additive_expression_complement, "mais")
    descriptor = None
    for klass in myDsl_additive_expression_complement.__mro__:
        if "mais" in klass.__dict__:
            descriptor = klass.__dict__["mais"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_additive_expression_linha_is_not_abstract():
    assert not inspect.isabstract(myDsl_additive_expression_linha)


def test_mydsl_additive_expression_linha_constructor_exists():
    assert callable(myDsl_additive_expression_linha.__init__)


def test_mydsl_additive_expression_linha_constructor_args():
    sig = inspect.signature(myDsl_additive_expression_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_equality_expression_complement_is_not_abstract():
    assert not inspect.isabstract(myDsl_equality_expression_complement)


def test_mydsl_equality_expression_complement_constructor_exists():
    assert callable(myDsl_equality_expression_complement.__init__)


def test_mydsl_equality_expression_complement_constructor_args():
    sig = inspect.signature(myDsl_equality_expression_complement.__init__)
    params = list(sig.parameters.keys())
    assert "maior" in params, "Missing parameter 'maior'"
    assert "maior_igual" in params, "Missing parameter 'maior_igual'"
    assert "n_igual" in params, "Missing parameter 'n_igual'"
    assert "menor" in params, "Missing parameter 'menor'"
    assert "igual" in params, "Missing parameter 'igual'"
    assert "menor_igual" in params, "Missing parameter 'menor_igual'"

def test_mydsl_equality_expression_complement_has_maior():
    assert hasattr(myDsl_equality_expression_complement, "maior")
    descriptor = None
    for klass in myDsl_equality_expression_complement.__mro__:
        if "maior" in klass.__dict__:
            descriptor = klass.__dict__["maior"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_equality_expression_complement_has_maior_igual():
    assert hasattr(myDsl_equality_expression_complement, "maior_igual")
    descriptor = None
    for klass in myDsl_equality_expression_complement.__mro__:
        if "maior_igual" in klass.__dict__:
            descriptor = klass.__dict__["maior_igual"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_equality_expression_complement_has_n_igual():
    assert hasattr(myDsl_equality_expression_complement, "n_igual")
    descriptor = None
    for klass in myDsl_equality_expression_complement.__mro__:
        if "n_igual" in klass.__dict__:
            descriptor = klass.__dict__["n_igual"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_equality_expression_complement_has_menor():
    assert hasattr(myDsl_equality_expression_complement, "menor")
    descriptor = None
    for klass in myDsl_equality_expression_complement.__mro__:
        if "menor" in klass.__dict__:
            descriptor = klass.__dict__["menor"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_equality_expression_complement_has_igual():
    assert hasattr(myDsl_equality_expression_complement, "igual")
    descriptor = None
    for klass in myDsl_equality_expression_complement.__mro__:
        if "igual" in klass.__dict__:
            descriptor = klass.__dict__["igual"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_equality_expression_complement_has_menor_igual():
    assert hasattr(myDsl_equality_expression_complement, "menor_igual")
    descriptor = None
    for klass in myDsl_equality_expression_complement.__mro__:
        if "menor_igual" in klass.__dict__:
            descriptor = klass.__dict__["menor_igual"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_equality_expression_linha_is_not_abstract():
    assert not inspect.isabstract(myDsl_equality_expression_linha)


def test_mydsl_equality_expression_linha_constructor_exists():
    assert callable(myDsl_equality_expression_linha.__init__)


def test_mydsl_equality_expression_linha_constructor_args():
    sig = inspect.signature(myDsl_equality_expression_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_equality_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_equality_expression)


def test_mydsl_equality_expression_constructor_exists():
    assert callable(myDsl_equality_expression.__init__)


def test_mydsl_equality_expression_constructor_args():
    sig = inspect.signature(myDsl_equality_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_relational_expression_complement_is_not_abstract():
    assert not inspect.isabstract(myDsl_relational_expression_complement)


def test_mydsl_relational_expression_complement_constructor_exists():
    assert callable(myDsl_relational_expression_complement.__init__)


def test_mydsl_relational_expression_complement_constructor_args():
    sig = inspect.signature(myDsl_relational_expression_complement.__init__)
    params = list(sig.parameters.keys())
    assert "menor_igual" in params, "Missing parameter 'menor_igual'"
    assert "menor" in params, "Missing parameter 'menor'"
    assert "maior_igual" in params, "Missing parameter 'maior_igual'"
    assert "maior" in params, "Missing parameter 'maior'"

def test_mydsl_relational_expression_complement_has_menor_igual():
    assert hasattr(myDsl_relational_expression_complement, "menor_igual")
    descriptor = None
    for klass in myDsl_relational_expression_complement.__mro__:
        if "menor_igual" in klass.__dict__:
            descriptor = klass.__dict__["menor_igual"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_relational_expression_complement_has_menor():
    assert hasattr(myDsl_relational_expression_complement, "menor")
    descriptor = None
    for klass in myDsl_relational_expression_complement.__mro__:
        if "menor" in klass.__dict__:
            descriptor = klass.__dict__["menor"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_relational_expression_complement_has_maior_igual():
    assert hasattr(myDsl_relational_expression_complement, "maior_igual")
    descriptor = None
    for klass in myDsl_relational_expression_complement.__mro__:
        if "maior_igual" in klass.__dict__:
            descriptor = klass.__dict__["maior_igual"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_relational_expression_complement_has_maior():
    assert hasattr(myDsl_relational_expression_complement, "maior")
    descriptor = None
    for klass in myDsl_relational_expression_complement.__mro__:
        if "maior" in klass.__dict__:
            descriptor = klass.__dict__["maior"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_relational_expression_linha_is_not_abstract():
    assert not inspect.isabstract(myDsl_relational_expression_linha)


def test_mydsl_relational_expression_linha_constructor_exists():
    assert callable(myDsl_relational_expression_linha.__init__)


def test_mydsl_relational_expression_linha_constructor_args():
    sig = inspect.signature(myDsl_relational_expression_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_relational_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_relational_expression)


def test_mydsl_relational_expression_constructor_exists():
    assert callable(myDsl_relational_expression.__init__)


def test_mydsl_relational_expression_constructor_args():
    sig = inspect.signature(myDsl_relational_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_additive_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_additive_expression)


def test_mydsl_additive_expression_constructor_exists():
    assert callable(myDsl_additive_expression.__init__)


def test_mydsl_additive_expression_constructor_args():
    sig = inspect.signature(myDsl_additive_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_multiplicative_expression_complement_is_not_abstract():
    assert not inspect.isabstract(myDsl_multiplicative_expression_complement)


def test_mydsl_multiplicative_expression_complement_constructor_exists():
    assert callable(myDsl_multiplicative_expression_complement.__init__)


def test_mydsl_multiplicative_expression_complement_constructor_args():
    sig = inspect.signature(myDsl_multiplicative_expression_complement.__init__)
    params = list(sig.parameters.keys())
    assert "modulo" in params, "Missing parameter 'modulo'"
    assert "multiplica" in params, "Missing parameter 'multiplica'"
    assert "divide" in params, "Missing parameter 'divide'"

def test_mydsl_multiplicative_expression_complement_has_modulo():
    assert hasattr(myDsl_multiplicative_expression_complement, "modulo")
    descriptor = None
    for klass in myDsl_multiplicative_expression_complement.__mro__:
        if "modulo" in klass.__dict__:
            descriptor = klass.__dict__["modulo"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_multiplicative_expression_complement_has_multiplica():
    assert hasattr(myDsl_multiplicative_expression_complement, "multiplica")
    descriptor = None
    for klass in myDsl_multiplicative_expression_complement.__mro__:
        if "multiplica" in klass.__dict__:
            descriptor = klass.__dict__["multiplica"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_multiplicative_expression_complement_has_divide():
    assert hasattr(myDsl_multiplicative_expression_complement, "divide")
    descriptor = None
    for klass in myDsl_multiplicative_expression_complement.__mro__:
        if "divide" in klass.__dict__:
            descriptor = klass.__dict__["divide"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_multiplicative_expression_linha_is_not_abstract():
    assert not inspect.isabstract(myDsl_multiplicative_expression_linha)


def test_mydsl_multiplicative_expression_linha_constructor_exists():
    assert callable(myDsl_multiplicative_expression_linha.__init__)


def test_mydsl_multiplicative_expression_linha_constructor_args():
    sig = inspect.signature(myDsl_multiplicative_expression_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_multiplicative_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_multiplicative_expression)


def test_mydsl_multiplicative_expression_constructor_exists():
    assert callable(myDsl_multiplicative_expression.__init__)


def test_mydsl_multiplicative_expression_constructor_args():
    sig = inspect.signature(myDsl_multiplicative_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_cast_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_cast_expression)


def test_mydsl_cast_expression_constructor_exists():
    assert callable(myDsl_cast_expression.__init__)


def test_mydsl_cast_expression_constructor_args():
    sig = inspect.signature(myDsl_cast_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_unary_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_unary_expression)


def test_mydsl_unary_expression_constructor_exists():
    assert callable(myDsl_unary_expression.__init__)


def test_mydsl_unary_expression_constructor_args():
    sig = inspect.signature(myDsl_unary_expression.__init__)
    params = list(sig.parameters.keys())
    assert "unary_operator" in params, "Missing parameter 'unary_operator'"

def test_mydsl_unary_expression_has_unary_operator():
    assert hasattr(myDsl_unary_expression, "unary_operator")
    descriptor = None
    for klass in myDsl_unary_expression.__mro__:
        if "unary_operator" in klass.__dict__:
            descriptor = klass.__dict__["unary_operator"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_argument_expression_list_linha_is_not_abstract():
    assert not inspect.isabstract(myDsl_argument_expression_list_linha)


def test_mydsl_argument_expression_list_linha_constructor_exists():
    assert callable(myDsl_argument_expression_list_linha.__init__)


def test_mydsl_argument_expression_list_linha_constructor_args():
    sig = inspect.signature(myDsl_argument_expression_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_argument_expression_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_argument_expression_list)


def test_mydsl_argument_expression_list_constructor_exists():
    assert callable(myDsl_argument_expression_list.__init__)


def test_mydsl_argument_expression_list_constructor_args():
    sig = inspect.signature(myDsl_argument_expression_list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_postfix_expression_complement_is_not_abstract():
    assert not inspect.isabstract(myDsl_postfix_expression_complement)


def test_mydsl_postfix_expression_complement_constructor_exists():
    assert callable(myDsl_postfix_expression_complement.__init__)


def test_mydsl_postfix_expression_complement_constructor_args():
    sig = inspect.signature(myDsl_postfix_expression_complement.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_mydsl_postfix_expression_complement_has_identifier():
    assert hasattr(myDsl_postfix_expression_complement, "identifier")
    descriptor = None
    for klass in myDsl_postfix_expression_complement.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_conditional_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_conditional_expression)


def test_mydsl_conditional_expression_constructor_exists():
    assert callable(myDsl_conditional_expression.__init__)


def test_mydsl_conditional_expression_constructor_args():
    sig = inspect.signature(myDsl_conditional_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_designator_list_linha_is_not_abstract():
    assert not inspect.isabstract(myDsl_designator_list_linha)


def test_mydsl_designator_list_linha_constructor_exists():
    assert callable(myDsl_designator_list_linha.__init__)


def test_mydsl_designator_list_linha_constructor_args():
    sig = inspect.signature(myDsl_designator_list_linha.__init__)
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



def test_mydsl_initializer_list_complement_is_not_abstract():
    assert not inspect.isabstract(myDsl_initializer_list_complement)


def test_mydsl_initializer_list_complement_constructor_exists():
    assert callable(myDsl_initializer_list_complement.__init__)


def test_mydsl_initializer_list_complement_constructor_args():
    sig = inspect.signature(myDsl_initializer_list_complement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_initializer_list_linha_is_not_abstract():
    assert not inspect.isabstract(myDsl_initializer_list_linha)


def test_mydsl_initializer_list_linha_constructor_exists():
    assert callable(myDsl_initializer_list_linha.__init__)


def test_mydsl_initializer_list_linha_constructor_args():
    sig = inspect.signature(myDsl_initializer_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_init_declarator_list_linha_is_not_abstract():
    assert not inspect.isabstract(myDsl_init_declarator_list_linha)


def test_mydsl_init_declarator_list_linha_constructor_exists():
    assert callable(myDsl_init_declarator_list_linha.__init__)


def test_mydsl_init_declarator_list_linha_constructor_args():
    sig = inspect.signature(myDsl_init_declarator_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_designation_is_not_abstract():
    assert not inspect.isabstract(myDsl_designation)


def test_mydsl_designation_constructor_exists():
    assert callable(myDsl_designation.__init__)


def test_mydsl_designation_constructor_args():
    sig = inspect.signature(myDsl_designation.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_postfix_expression_linha_is_not_abstract():
    assert not inspect.isabstract(myDsl_postfix_expression_linha)


def test_mydsl_postfix_expression_linha_constructor_exists():
    assert callable(myDsl_postfix_expression_linha.__init__)


def test_mydsl_postfix_expression_linha_constructor_args():
    sig = inspect.signature(myDsl_postfix_expression_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_postfix_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_postfix_expression)


def test_mydsl_postfix_expression_constructor_exists():
    assert callable(myDsl_postfix_expression.__init__)


def test_mydsl_postfix_expression_constructor_args():
    sig = inspect.signature(myDsl_postfix_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_generic_assoc_list_linha_is_not_abstract():
    assert not inspect.isabstract(myDsl_generic_assoc_list_linha)


def test_mydsl_generic_assoc_list_linha_constructor_exists():
    assert callable(myDsl_generic_assoc_list_linha.__init__)


def test_mydsl_generic_assoc_list_linha_constructor_args():
    sig = inspect.signature(myDsl_generic_assoc_list_linha.__init__)
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



def test_mydsl_generic_selection_is_not_abstract():
    assert not inspect.isabstract(myDsl_generic_selection)


def test_mydsl_generic_selection_constructor_exists():
    assert callable(myDsl_generic_selection.__init__)


def test_mydsl_generic_selection_constructor_args():
    sig = inspect.signature(myDsl_generic_selection.__init__)
    params = list(sig.parameters.keys())
    assert "_generic" in params, "Missing parameter '_generic'"

def test_mydsl_generic_selection_has__generic():
    assert hasattr(myDsl_generic_selection, "_generic")
    descriptor = None
    for klass in myDsl_generic_selection.__mro__:
        if "_generic" in klass.__dict__:
            descriptor = klass.__dict__["_generic"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_expression)


def test_mydsl_expression_constructor_exists():
    assert callable(myDsl_expression.__init__)


def test_mydsl_expression_constructor_args():
    sig = inspect.signature(myDsl_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_constant_is_not_abstract():
    assert not inspect.isabstract(myDsl_constant)


def test_mydsl_constant_constructor_exists():
    assert callable(myDsl_constant.__init__)


def test_mydsl_constant_constructor_args():
    sig = inspect.signature(myDsl_constant.__init__)
    params = list(sig.parameters.keys())
    assert "i_constant" in params, "Missing parameter 'i_constant'"
    assert "string" in params, "Missing parameter 'string'"
    assert "f_constant" in params, "Missing parameter 'f_constant'"
    assert "enumz" in params, "Missing parameter 'enumz'"
    assert "char" in params, "Missing parameter 'char'"

def test_mydsl_constant_has_i_constant():
    assert hasattr(myDsl_constant, "i_constant")
    descriptor = None
    for klass in myDsl_constant.__mro__:
        if "i_constant" in klass.__dict__:
            descriptor = klass.__dict__["i_constant"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_constant_has_string():
    assert hasattr(myDsl_constant, "string")
    descriptor = None
    for klass in myDsl_constant.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_constant_has_f_constant():
    assert hasattr(myDsl_constant, "f_constant")
    descriptor = None
    for klass in myDsl_constant.__mro__:
        if "f_constant" in klass.__dict__:
            descriptor = klass.__dict__["f_constant"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_constant_has_enumz():
    assert hasattr(myDsl_constant, "enumz")
    descriptor = None
    for klass in myDsl_constant.__mro__:
        if "enumz" in klass.__dict__:
            descriptor = klass.__dict__["enumz"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_constant_has_char():
    assert hasattr(myDsl_constant, "char")
    descriptor = None
    for klass in myDsl_constant.__mro__:
        if "char" in klass.__dict__:
            descriptor = klass.__dict__["char"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_primary_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_primary_expression)


def test_mydsl_primary_expression_constructor_exists():
    assert callable(myDsl_primary_expression.__init__)


def test_mydsl_primary_expression_constructor_args():
    sig = inspect.signature(myDsl_primary_expression.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_mydsl_primary_expression_has_identifier():
    assert hasattr(myDsl_primary_expression, "identifier")
    descriptor = None
    for klass in myDsl_primary_expression.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_identifier_list_linha_is_not_abstract():
    assert not inspect.isabstract(myDsl_identifier_list_linha)


def test_mydsl_identifier_list_linha_constructor_exists():
    assert callable(myDsl_identifier_list_linha.__init__)


def test_mydsl_identifier_list_linha_constructor_args():
    sig = inspect.signature(myDsl_identifier_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_direct_abstract_declarator_complement_is_not_abstract():
    assert not inspect.isabstract(myDsl_direct_abstract_declarator_complement)


def test_mydsl_direct_abstract_declarator_complement_constructor_exists():
    assert callable(myDsl_direct_abstract_declarator_complement.__init__)


def test_mydsl_direct_abstract_declarator_complement_constructor_args():
    sig = inspect.signature(myDsl_direct_abstract_declarator_complement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_initializer_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_initializer_list)


def test_mydsl_initializer_list_constructor_exists():
    assert callable(myDsl_initializer_list.__init__)


def test_mydsl_initializer_list_constructor_args():
    sig = inspect.signature(myDsl_initializer_list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_initializer_is_not_abstract():
    assert not inspect.isabstract(myDsl_initializer)


def test_mydsl_initializer_constructor_exists():
    assert callable(myDsl_initializer.__init__)


def test_mydsl_initializer_constructor_args():
    sig = inspect.signature(myDsl_initializer.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_direct_abstract_declarator_linha_is_not_abstract():
    assert not inspect.isabstract(myDsl_direct_abstract_declarator_linha)


def test_mydsl_direct_abstract_declarator_linha_constructor_exists():
    assert callable(myDsl_direct_abstract_declarator_linha.__init__)


def test_mydsl_direct_abstract_declarator_linha_constructor_args():
    sig = inspect.signature(myDsl_direct_abstract_declarator_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_direct_abstract_declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl_direct_abstract_declarator)


def test_mydsl_direct_abstract_declarator_constructor_exists():
    assert callable(myDsl_direct_abstract_declarator.__init__)


def test_mydsl_direct_abstract_declarator_constructor_args():
    sig = inspect.signature(myDsl_direct_abstract_declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_abstract_declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl_abstract_declarator)


def test_mydsl_abstract_declarator_constructor_exists():
    assert callable(myDsl_abstract_declarator.__init__)


def test_mydsl_abstract_declarator_constructor_args():
    sig = inspect.signature(myDsl_abstract_declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_parameter_list_linha_is_not_abstract():
    assert not inspect.isabstract(myDsl_parameter_list_linha)


def test_mydsl_parameter_list_linha_constructor_exists():
    assert callable(myDsl_parameter_list_linha.__init__)


def test_mydsl_parameter_list_linha_constructor_args():
    sig = inspect.signature(myDsl_parameter_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_parameter_declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl_parameter_declaration)


def test_mydsl_parameter_declaration_constructor_exists():
    assert callable(myDsl_parameter_declaration.__init__)


def test_mydsl_parameter_declaration_constructor_args():
    sig = inspect.signature(myDsl_parameter_declaration.__init__)
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



def test_mydsl_assignment_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_assignment_expression)


def test_mydsl_assignment_expression_constructor_exists():
    assert callable(myDsl_assignment_expression.__init__)


def test_mydsl_assignment_expression_constructor_args():
    sig = inspect.signature(myDsl_assignment_expression.__init__)
    params = list(sig.parameters.keys())
    assert "assignment_operator" in params, "Missing parameter 'assignment_operator'"

def test_mydsl_assignment_expression_has_assignment_operator():
    assert hasattr(myDsl_assignment_expression, "assignment_operator")
    descriptor = None
    for klass in myDsl_assignment_expression.__mro__:
        if "assignment_operator" in klass.__dict__:
            descriptor = klass.__dict__["assignment_operator"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_direct_declarator_complemento_is_not_abstract():
    assert not inspect.isabstract(myDsl_direct_declarator_complemento)


def test_mydsl_direct_declarator_complemento_constructor_exists():
    assert callable(myDsl_direct_declarator_complemento.__init__)


def test_mydsl_direct_declarator_complemento_constructor_args():
    sig = inspect.signature(myDsl_direct_declarator_complemento.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_direct_declarator_linha_is_not_abstract():
    assert not inspect.isabstract(myDsl_direct_declarator_linha)


def test_mydsl_direct_declarator_linha_constructor_exists():
    assert callable(myDsl_direct_declarator_linha.__init__)


def test_mydsl_direct_declarator_linha_constructor_args():
    sig = inspect.signature(myDsl_direct_declarator_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_type_qualifier_list_linha_is_not_abstract():
    assert not inspect.isabstract(myDsl_type_qualifier_list_linha)


def test_mydsl_type_qualifier_list_linha_constructor_exists():
    assert callable(myDsl_type_qualifier_list_linha.__init__)


def test_mydsl_type_qualifier_list_linha_constructor_args():
    sig = inspect.signature(myDsl_type_qualifier_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_direct_abstract_declarator_complement_is_not_abstract():
    assert not inspect.isabstract(direct_abstract_declarator_complement)


def test_direct_abstract_declarator_complement_constructor_exists():
    assert callable(direct_abstract_declarator_complement.__init__)


def test_direct_abstract_declarator_complement_constructor_args():
    sig = inspect.signature(direct_abstract_declarator_complement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_type_qualifier_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_type_qualifier_list)


def test_mydsl_type_qualifier_list_constructor_exists():
    assert callable(myDsl_type_qualifier_list.__init__)


def test_mydsl_type_qualifier_list_constructor_args():
    sig = inspect.signature(myDsl_type_qualifier_list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_direct_declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl_direct_declarator)


def test_mydsl_direct_declarator_constructor_exists():
    assert callable(myDsl_direct_declarator.__init__)


def test_mydsl_direct_declarator_constructor_args():
    sig = inspect.signature(myDsl_direct_declarator.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_mydsl_direct_declarator_has_identifier():
    assert hasattr(myDsl_direct_declarator, "identifier")
    descriptor = None
    for klass in myDsl_direct_declarator.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_pointer_is_not_abstract():
    assert not inspect.isabstract(myDsl_pointer)


def test_mydsl_pointer_constructor_exists():
    assert callable(myDsl_pointer.__init__)


def test_mydsl_pointer_constructor_args():
    sig = inspect.signature(myDsl_pointer.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_declaration_list_linha_is_not_abstract():
    assert not inspect.isabstract(myDsl_declaration_list_linha)


def test_mydsl_declaration_list_linha_constructor_exists():
    assert callable(myDsl_declaration_list_linha.__init__)


def test_mydsl_declaration_list_linha_constructor_args():
    sig = inspect.signature(myDsl_declaration_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_compound_statement_is_not_abstract():
    assert not inspect.isabstract(myDsl_compound_statement)


def test_mydsl_compound_statement_constructor_exists():
    assert callable(myDsl_compound_statement.__init__)


def test_mydsl_compound_statement_constructor_args():
    sig = inspect.signature(myDsl_compound_statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_declaration_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_declaration_list)


def test_mydsl_declaration_list_constructor_exists():
    assert callable(myDsl_declaration_list.__init__)


def test_mydsl_declaration_list_constructor_args():
    sig = inspect.signature(myDsl_declaration_list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_parameter_lista_is_not_abstract():
    assert not inspect.isabstract(myDsl_parameter_lista)


def test_mydsl_parameter_lista_constructor_exists():
    assert callable(myDsl_parameter_lista.__init__)


def test_mydsl_parameter_lista_constructor_args():
    sig = inspect.signature(myDsl_parameter_lista.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_init_declarator_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_init_declarator_list)


def test_mydsl_init_declarator_list_constructor_exists():
    assert callable(myDsl_init_declarator_list.__init__)


def test_mydsl_init_declarator_list_constructor_args():
    sig = inspect.signature(myDsl_init_declarator_list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl_declarator)


def test_mydsl_declarator_constructor_exists():
    assert callable(myDsl_declarator.__init__)


def test_mydsl_declarator_constructor_args():
    sig = inspect.signature(myDsl_declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_struct_declarator_list_linha_is_not_abstract():
    assert not inspect.isabstract(myDsl_struct_declarator_list_linha)


def test_mydsl_struct_declarator_list_linha_constructor_exists():
    assert callable(myDsl_struct_declarator_list_linha.__init__)


def test_mydsl_struct_declarator_list_linha_constructor_args():
    sig = inspect.signature(myDsl_struct_declarator_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_struct_declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl_struct_declarator)


def test_mydsl_struct_declarator_constructor_exists():
    assert callable(myDsl_struct_declarator.__init__)


def test_mydsl_struct_declarator_constructor_args():
    sig = inspect.signature(myDsl_struct_declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_static_assert_declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl_static_assert_declaration)


def test_mydsl_static_assert_declaration_constructor_exists():
    assert callable(myDsl_static_assert_declaration.__init__)


def test_mydsl_static_assert_declaration_constructor_args():
    sig = inspect.signature(myDsl_static_assert_declaration.__init__)
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



def test_mydsl_struct_declaration_list_linha_is_not_abstract():
    assert not inspect.isabstract(myDsl_struct_declaration_list_linha)


def test_mydsl_struct_declaration_list_linha_constructor_exists():
    assert callable(myDsl_struct_declaration_list_linha.__init__)


def test_mydsl_struct_declaration_list_linha_constructor_args():
    sig = inspect.signature(myDsl_struct_declaration_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_struct_declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl_struct_declaration)


def test_mydsl_struct_declaration_constructor_exists():
    assert callable(myDsl_struct_declaration.__init__)


def test_mydsl_struct_declaration_constructor_args():
    sig = inspect.signature(myDsl_struct_declaration.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_struct_or_union_specifier_complement_is_not_abstract():
    assert not inspect.isabstract(myDsl_struct_or_union_specifier_complement)


def test_mydsl_struct_or_union_specifier_complement_constructor_exists():
    assert callable(myDsl_struct_or_union_specifier_complement.__init__)


def test_mydsl_struct_or_union_specifier_complement_constructor_args():
    sig = inspect.signature(myDsl_struct_or_union_specifier_complement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_struct_declaration_list_is_not_abstract():
    assert not inspect.isabstract(myDsl_struct_declaration_list)


def test_mydsl_struct_declaration_list_constructor_exists():
    assert callable(myDsl_struct_declaration_list.__init__)


def test_mydsl_struct_declaration_list_constructor_args():
    sig = inspect.signature(myDsl_struct_declaration_list.__init__)
    params = list(sig.parameters.keys())



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



def test_mydsl_enumerator_list_linha_is_not_abstract():
    assert not inspect.isabstract(myDsl_enumerator_list_linha)


def test_mydsl_enumerator_list_linha_constructor_exists():
    assert callable(myDsl_enumerator_list_linha.__init__)


def test_mydsl_enumerator_list_linha_constructor_args():
    sig = inspect.signature(myDsl_enumerator_list_linha.__init__)
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



def test_mydsl_enum_specifier_is_not_abstract():
    assert not inspect.isabstract(myDsl_enum_specifier)


def test_mydsl_enum_specifier_constructor_exists():
    assert callable(myDsl_enum_specifier.__init__)


def test_mydsl_enum_specifier_constructor_args():
    sig = inspect.signature(myDsl_enum_specifier.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_mydsl_enum_specifier_has_identifier():
    assert hasattr(myDsl_enum_specifier, "identifier")
    descriptor = None
    for klass in myDsl_enum_specifier.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_argument_expression_list_linha_is_not_abstract():
    assert not inspect.isabstract(argument_expression_list_linha)


def test_argument_expression_list_linha_constructor_exists():
    assert callable(argument_expression_list_linha.__init__)


def test_argument_expression_list_linha_constructor_args():
    sig = inspect.signature(argument_expression_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_argumentexpressionlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(myDsl_ArgumentExpressionListLinhaAction)


def test_mydsl_argumentexpressionlistlinhaaction_constructor_exists():
    assert callable(myDsl_ArgumentExpressionListLinhaAction.__init__)


def test_mydsl_argumentexpressionlistlinhaaction_constructor_args():
    sig = inspect.signature(myDsl_ArgumentExpressionListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_postfix_expression_complement_is_not_abstract():
    assert not inspect.isabstract(postfix_expression_complement)


def test_postfix_expression_complement_constructor_exists():
    assert callable(postfix_expression_complement.__init__)


def test_postfix_expression_complement_constructor_args():
    sig = inspect.signature(postfix_expression_complement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_postfixempryparams_is_not_abstract():
    assert not inspect.isabstract(myDsl_PostFixEmpryParams)


def test_mydsl_postfixempryparams_constructor_exists():
    assert callable(myDsl_PostFixEmpryParams.__init__)


def test_mydsl_postfixempryparams_constructor_args():
    sig = inspect.signature(myDsl_PostFixEmpryParams.__init__)
    params = list(sig.parameters.keys())



def test_designator_list_linha_is_not_abstract():
    assert not inspect.isabstract(designator_list_linha)


def test_designator_list_linha_constructor_exists():
    assert callable(designator_list_linha.__init__)


def test_designator_list_linha_constructor_args():
    sig = inspect.signature(designator_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_designatorlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(myDsl_DesignatorListLinhaAction)


def test_mydsl_designatorlistlinhaaction_constructor_exists():
    assert callable(myDsl_DesignatorListLinhaAction.__init__)


def test_mydsl_designatorlistlinhaaction_constructor_args():
    sig = inspect.signature(myDsl_DesignatorListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_initializer_list_linha_is_not_abstract():
    assert not inspect.isabstract(initializer_list_linha)


def test_initializer_list_linha_constructor_exists():
    assert callable(initializer_list_linha.__init__)


def test_initializer_list_linha_constructor_args():
    sig = inspect.signature(initializer_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_initializerlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(myDsl_InitializerListLinhaAction)


def test_mydsl_initializerlistlinhaaction_constructor_exists():
    assert callable(myDsl_InitializerListLinhaAction.__init__)


def test_mydsl_initializerlistlinhaaction_constructor_args():
    sig = inspect.signature(myDsl_InitializerListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_init_declarator_list_linha_is_not_abstract():
    assert not inspect.isabstract(init_declarator_list_linha)


def test_init_declarator_list_linha_constructor_exists():
    assert callable(init_declarator_list_linha.__init__)


def test_init_declarator_list_linha_constructor_args():
    sig = inspect.signature(init_declarator_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_initdecclaratorlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(myDsl_InitDecclaratorListLinhaAction)


def test_mydsl_initdecclaratorlistlinhaaction_constructor_exists():
    assert callable(myDsl_InitDecclaratorListLinhaAction.__init__)


def test_mydsl_initdecclaratorlistlinhaaction_constructor_args():
    sig = inspect.signature(myDsl_InitDecclaratorListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_unary_expression_is_not_abstract():
    assert not inspect.isabstract(unary_expression)


def test_unary_expression_constructor_exists():
    assert callable(unary_expression.__init__)


def test_unary_expression_constructor_args():
    sig = inspect.signature(unary_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_plusplus_is_not_abstract():
    assert not inspect.isabstract(myDsl_PlusPlus)


def test_mydsl_plusplus_constructor_exists():
    assert callable(myDsl_PlusPlus.__init__)


def test_mydsl_plusplus_constructor_args():
    sig = inspect.signature(myDsl_PlusPlus.__init__)
    params = list(sig.parameters.keys())
    assert "plus" in params, "Missing parameter 'plus'"

def test_mydsl_plusplus_has_plus():
    assert hasattr(myDsl_PlusPlus, "plus")
    descriptor = None
    for klass in myDsl_PlusPlus.__mro__:
        if "plus" in klass.__dict__:
            descriptor = klass.__dict__["plus"]
            break
    assert isinstance(descriptor, property)



def test_direct_abstract_declarator_linha_is_not_abstract():
    assert not inspect.isabstract(direct_abstract_declarator_linha)


def test_direct_abstract_declarator_linha_constructor_exists():
    assert callable(direct_abstract_declarator_linha.__init__)


def test_direct_abstract_declarator_linha_constructor_args():
    sig = inspect.signature(direct_abstract_declarator_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_directabstractdeclarratorlinhaaction_is_not_abstract():
    assert not inspect.isabstract(myDsl_DirectAbstractDeclarratorLinhaAction)


def test_mydsl_directabstractdeclarratorlinhaaction_constructor_exists():
    assert callable(myDsl_DirectAbstractDeclarratorLinhaAction.__init__)


def test_mydsl_directabstractdeclarratorlinhaaction_constructor_args():
    sig = inspect.signature(myDsl_DirectAbstractDeclarratorLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_type_qualifier_list_linha_is_not_abstract():
    assert not inspect.isabstract(type_qualifier_list_linha)


def test_type_qualifier_list_linha_constructor_exists():
    assert callable(type_qualifier_list_linha.__init__)


def test_type_qualifier_list_linha_constructor_args():
    sig = inspect.signature(type_qualifier_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_typequalifierlistlinhaation_is_not_abstract():
    assert not inspect.isabstract(myDsl_TypeQualifierListLinhaAtion)


def test_mydsl_typequalifierlistlinhaation_constructor_exists():
    assert callable(myDsl_TypeQualifierListLinhaAtion.__init__)


def test_mydsl_typequalifierlistlinhaation_constructor_args():
    sig = inspect.signature(myDsl_TypeQualifierListLinhaAtion.__init__)
    params = list(sig.parameters.keys())



def test_declaration_list_linha_is_not_abstract():
    assert not inspect.isabstract(declaration_list_linha)


def test_declaration_list_linha_constructor_exists():
    assert callable(declaration_list_linha.__init__)


def test_declaration_list_linha_constructor_args():
    sig = inspect.signature(declaration_list_linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_declarationlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(myDsl_DeclarationListLinhaAction)


def test_mydsl_declarationlistlinhaaction_constructor_exists():
    assert callable(myDsl_DeclarationListLinhaAction.__init__)


def test_mydsl_declarationlistlinhaaction_constructor_args():
    sig = inspect.signature(myDsl_DeclarationListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_struct_or_union_specifier_is_not_abstract():
    assert not inspect.isabstract(myDsl_struct_or_union_specifier)


def test_mydsl_struct_or_union_specifier_constructor_exists():
    assert callable(myDsl_struct_or_union_specifier.__init__)


def test_mydsl_struct_or_union_specifier_constructor_args():
    sig = inspect.signature(myDsl_struct_or_union_specifier.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "struct_or_union" in params, "Missing parameter 'struct_or_union'"

def test_mydsl_struct_or_union_specifier_has_identifier():
    assert hasattr(myDsl_struct_or_union_specifier, "identifier")
    descriptor = None
    for klass in myDsl_struct_or_union_specifier.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_struct_or_union_specifier_has_struct_or_union():
    assert hasattr(myDsl_struct_or_union_specifier, "struct_or_union")
    descriptor = None
    for klass in myDsl_struct_or_union_specifier.__mro__:
        if "struct_or_union" in klass.__dict__:
            descriptor = klass.__dict__["struct_or_union"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_atomic_type_specifier_is_not_abstract():
    assert not inspect.isabstract(myDsl_atomic_type_specifier)


def test_mydsl_atomic_type_specifier_constructor_exists():
    assert callable(myDsl_atomic_type_specifier.__init__)


def test_mydsl_atomic_type_specifier_constructor_args():
    sig = inspect.signature(myDsl_atomic_type_specifier.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_constant_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_constant_expression)


def test_mydsl_constant_expression_constructor_exists():
    assert callable(myDsl_constant_expression.__init__)


def test_mydsl_constant_expression_constructor_args():
    sig = inspect.signature(myDsl_constant_expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_type_name_is_not_abstract():
    assert not inspect.isabstract(myDsl_type_name)


def test_mydsl_type_name_constructor_exists():
    assert callable(myDsl_type_name.__init__)


def test_mydsl_type_name_constructor_args():
    sig = inspect.signature(myDsl_type_name.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_alignment_specifier_is_not_abstract():
    assert not inspect.isabstract(myDsl_alignment_specifier)


def test_mydsl_alignment_specifier_constructor_exists():
    assert callable(myDsl_alignment_specifier.__init__)


def test_mydsl_alignment_specifier_constructor_args():
    sig = inspect.signature(myDsl_alignment_specifier.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_type_qualifier_is_not_abstract():
    assert not inspect.isabstract(myDsl_type_qualifier)


def test_mydsl_type_qualifier_constructor_exists():
    assert callable(myDsl_type_qualifier.__init__)


def test_mydsl_type_qualifier_constructor_args():
    sig = inspect.signature(myDsl_type_qualifier.__init__)
    params = list(sig.parameters.keys())
    assert "namez" in params, "Missing parameter 'namez'"

def test_mydsl_type_qualifier_has_namez():
    assert hasattr(myDsl_type_qualifier, "namez")
    descriptor = None
    for klass in myDsl_type_qualifier.__mro__:
        if "namez" in klass.__dict__:
            descriptor = klass.__dict__["namez"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_type_specifier_is_not_abstract():
    assert not inspect.isabstract(myDsl_type_specifier)


def test_mydsl_type_specifier_constructor_exists():
    assert callable(myDsl_type_specifier.__init__)


def test_mydsl_type_specifier_constructor_args():
    sig = inspect.signature(myDsl_type_specifier.__init__)
    params = list(sig.parameters.keys())
    assert "type_name_str" in params, "Missing parameter 'type_name_str'"

def test_mydsl_type_specifier_has_type_name_str():
    assert hasattr(myDsl_type_specifier, "type_name_str")
    descriptor = None
    for klass in myDsl_type_specifier.__mro__:
        if "type_name_str" in klass.__dict__:
            descriptor = klass.__dict__["type_name_str"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_declaration_specifiers_is_not_abstract():
    assert not inspect.isabstract(myDsl_declaration_specifiers)


def test_mydsl_declaration_specifiers_constructor_exists():
    assert callable(myDsl_declaration_specifiers.__init__)


def test_mydsl_declaration_specifiers_constructor_args():
    sig = inspect.signature(myDsl_declaration_specifiers.__init__)
    params = list(sig.parameters.keys())
    assert "function_specifier" in params, "Missing parameter 'function_specifier'"
    assert "storage_class_specifier" in params, "Missing parameter 'storage_class_specifier'"

def test_mydsl_declaration_specifiers_has_function_specifier():
    assert hasattr(myDsl_declaration_specifiers, "function_specifier")
    descriptor = None
    for klass in myDsl_declaration_specifiers.__mro__:
        if "function_specifier" in klass.__dict__:
            descriptor = klass.__dict__["function_specifier"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_declaration_specifiers_has_storage_class_specifier():
    assert hasattr(myDsl_declaration_specifiers, "storage_class_specifier")
    descriptor = None
    for klass in myDsl_declaration_specifiers.__mro__:
        if "storage_class_specifier" in klass.__dict__:
            descriptor = klass.__dict__["storage_class_specifier"]
            break
    assert isinstance(descriptor, property)



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



def test_mydsl_translation_unit_linha_is_not_abstract():
    assert not inspect.isabstract(myDsl_translation_unit_linha)


def test_mydsl_translation_unit_linha_constructor_exists():
    assert callable(myDsl_translation_unit_linha.__init__)


def test_mydsl_translation_unit_linha_constructor_args():
    sig = inspect.signature(myDsl_translation_unit_linha.__init__)
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
struct_declarator_list_linha_strategy = st.builds(
    struct_declarator_list_linha,
)
myDsl_StructDeclaratorListLinhaAction_strategy = st.builds(
    myDsl_StructDeclaratorListLinhaAction,
)
postfix_expression_linha_strategy = st.builds(
    postfix_expression_linha,
)
myDsl_PostfixExpressionLinhaAction_strategy = st.builds(
    myDsl_PostfixExpressionLinhaAction,
)
generic_assoc_list_linha_strategy = st.builds(
    generic_assoc_list_linha,
)
myDsl_GenericAssocListLinhaAction_strategy = st.builds(
    myDsl_GenericAssocListLinhaAction,
)
translation_unit_linha_strategy = st.builds(
    translation_unit_linha,
)
myDsl_TranlationUnitLinhaAction_strategy = st.builds(
    myDsl_TranlationUnitLinhaAction,
)
identifier_list_linha_strategy = st.builds(
    identifier_list_linha,
)
myDsl_IdentifierListLinhaAction_strategy = st.builds(
    myDsl_IdentifierListLinhaAction,
    identifier=
        safe_text
)
myDsl_init_declarator_strategy = st.builds(
    myDsl_init_declarator,
)
myDsl_expression_linha_strategy = st.builds(
    myDsl_expression_linha,
)
struct_declaration_list_linha_strategy = st.builds(
    struct_declaration_list_linha,
)
myDsl_StructDeclarationListLinhaAction_strategy = st.builds(
    myDsl_StructDeclarationListLinhaAction,
)
struct_or_union_specifier_complement_strategy = st.builds(
    struct_or_union_specifier_complement,
)
myDsl_StructOrUnionSpecifierComplementAction_strategy = st.builds(
    myDsl_StructOrUnionSpecifierComplementAction,
)
enumerator_list_linha_strategy = st.builds(
    enumerator_list_linha,
)
myDsl_EnumeratorListLinhaAction_strategy = st.builds(
    myDsl_EnumeratorListLinhaAction,
)
myDsl_string_dsl_strategy = st.builds(
    myDsl_string_dsl,
    __func__=
        safe_text,
    string_literal=
        safe_text
)
myDsl_conditional_expression_linha_strategy = st.builds(
    myDsl_conditional_expression_linha,
)
myDsl_logical_or_expression_linha_strategy = st.builds(
    myDsl_logical_or_expression_linha,
)
myDsl_logical_or_expression_strategy = st.builds(
    myDsl_logical_or_expression,
)
myDsl_logical_and_expression_linha_strategy = st.builds(
    myDsl_logical_and_expression_linha,
)
myDsl_logical_and_expression_strategy = st.builds(
    myDsl_logical_and_expression,
)
postfix_expression_strategy = st.builds(
    postfix_expression,
)
myDsl_block_item_list_linha_strategy = st.builds(
    myDsl_block_item_list_linha,
)
myDsl_block_item_strategy = st.builds(
    myDsl_block_item,
)
myDsl_block_item_list_strategy = st.builds(
    myDsl_block_item_list,
)
myDsl_inclusive_or_expression_linha_strategy = st.builds(
    myDsl_inclusive_or_expression_linha,
)
myDsl_inclusive_or_expression_strategy = st.builds(
    myDsl_inclusive_or_expression,
)
myDsl_exclusive_or_expression_linha_strategy = st.builds(
    myDsl_exclusive_or_expression_linha,
)
myDsl_exclusive_or_expression_strategy = st.builds(
    myDsl_exclusive_or_expression,
)
myDsl_and_expression_linha_strategy = st.builds(
    myDsl_and_expression_linha,
)
myDsl_and_expression_strategy = st.builds(
    myDsl_and_expression,
)
myDsl_jump_statement_strategy = st.builds(
    myDsl_jump_statement,
    break_=
        safe_text,
    return_=
        safe_text,
    return_vazio=
        safe_text,
    identifier=
        safe_text
)
myDsl_iteration_statement_strategy = st.builds(
    myDsl_iteration_statement,
)
myDsl_selection_statement_strategy = st.builds(
    myDsl_selection_statement,
)
myDsl_expression_statement_strategy = st.builds(
    myDsl_expression_statement,
)
myDsl_labeled_statement_strategy = st.builds(
    myDsl_labeled_statement,
    identifier=
        safe_text
)
myDsl_statement_strategy = st.builds(
    myDsl_statement,
)
myDsl_shift_expression_complement_strategy = st.builds(
    myDsl_shift_expression_complement,
    sright=
        safe_text,
    sleft=
        safe_text
)
myDsl_shift_expression_linha_strategy = st.builds(
    myDsl_shift_expression_linha,
)
myDsl_shift_expression_strategy = st.builds(
    myDsl_shift_expression,
)
myDsl_additive_expression_complement_strategy = st.builds(
    myDsl_additive_expression_complement,
    menos=
        safe_text,
    mais=
        safe_text
)
myDsl_additive_expression_linha_strategy = st.builds(
    myDsl_additive_expression_linha,
)
myDsl_equality_expression_complement_strategy = st.builds(
    myDsl_equality_expression_complement,
    maior=
        safe_text,
    maior_igual=
        safe_text,
    n_igual=
        safe_text,
    menor=
        safe_text,
    igual=
        safe_text,
    menor_igual=
        safe_text
)
myDsl_equality_expression_linha_strategy = st.builds(
    myDsl_equality_expression_linha,
)
myDsl_equality_expression_strategy = st.builds(
    myDsl_equality_expression,
)
myDsl_relational_expression_complement_strategy = st.builds(
    myDsl_relational_expression_complement,
    menor_igual=
        safe_text,
    menor=
        safe_text,
    maior_igual=
        safe_text,
    maior=
        safe_text
)
myDsl_relational_expression_linha_strategy = st.builds(
    myDsl_relational_expression_linha,
)
myDsl_relational_expression_strategy = st.builds(
    myDsl_relational_expression,
)
myDsl_additive_expression_strategy = st.builds(
    myDsl_additive_expression,
)
myDsl_multiplicative_expression_complement_strategy = st.builds(
    myDsl_multiplicative_expression_complement,
    modulo=
        safe_text,
    multiplica=
        safe_text,
    divide=
        safe_text
)
myDsl_multiplicative_expression_linha_strategy = st.builds(
    myDsl_multiplicative_expression_linha,
)
myDsl_multiplicative_expression_strategy = st.builds(
    myDsl_multiplicative_expression,
)
myDsl_cast_expression_strategy = st.builds(
    myDsl_cast_expression,
)
myDsl_unary_expression_strategy = st.builds(
    myDsl_unary_expression,
    unary_operator=
        safe_text
)
myDsl_argument_expression_list_linha_strategy = st.builds(
    myDsl_argument_expression_list_linha,
)
myDsl_argument_expression_list_strategy = st.builds(
    myDsl_argument_expression_list,
)
myDsl_postfix_expression_complement_strategy = st.builds(
    myDsl_postfix_expression_complement,
    identifier=
        safe_text
)
myDsl_conditional_expression_strategy = st.builds(
    myDsl_conditional_expression,
)
myDsl_designator_list_linha_strategy = st.builds(
    myDsl_designator_list_linha,
)
myDsl_designator_strategy = st.builds(
    myDsl_designator,
    identifier=
        safe_text
)
myDsl_designator_list_strategy = st.builds(
    myDsl_designator_list,
)
myDsl_initializer_list_complement_strategy = st.builds(
    myDsl_initializer_list_complement,
)
myDsl_initializer_list_linha_strategy = st.builds(
    myDsl_initializer_list_linha,
)
myDsl_init_declarator_list_linha_strategy = st.builds(
    myDsl_init_declarator_list_linha,
)
myDsl_designation_strategy = st.builds(
    myDsl_designation,
)
myDsl_postfix_expression_linha_strategy = st.builds(
    myDsl_postfix_expression_linha,
)
myDsl_postfix_expression_strategy = st.builds(
    myDsl_postfix_expression,
)
myDsl_generic_assoc_list_linha_strategy = st.builds(
    myDsl_generic_assoc_list_linha,
)
myDsl_generic_association_strategy = st.builds(
    myDsl_generic_association,
    default=
        safe_text
)
myDsl_generic_assoc_list_strategy = st.builds(
    myDsl_generic_assoc_list,
)
myDsl_generic_selection_strategy = st.builds(
    myDsl_generic_selection,
    _generic=
        safe_text
)
myDsl_expression_strategy = st.builds(
    myDsl_expression,
)
myDsl_constant_strategy = st.builds(
    myDsl_constant,
    i_constant=
        st.integers(),
    string=
        safe_text,
    f_constant=
        safe_text,
    enumz=
        safe_text,
    char=
        safe_text
)
myDsl_primary_expression_strategy = st.builds(
    myDsl_primary_expression,
    identifier=
        safe_text
)
myDsl_identifier_list_linha_strategy = st.builds(
    myDsl_identifier_list_linha,
)
myDsl_direct_abstract_declarator_complement_strategy = st.builds(
    myDsl_direct_abstract_declarator_complement,
)
myDsl_initializer_list_strategy = st.builds(
    myDsl_initializer_list,
)
myDsl_initializer_strategy = st.builds(
    myDsl_initializer,
)
myDsl_direct_abstract_declarator_linha_strategy = st.builds(
    myDsl_direct_abstract_declarator_linha,
)
myDsl_direct_abstract_declarator_strategy = st.builds(
    myDsl_direct_abstract_declarator,
)
myDsl_abstract_declarator_strategy = st.builds(
    myDsl_abstract_declarator,
)
myDsl_parameter_list_linha_strategy = st.builds(
    myDsl_parameter_list_linha,
)
myDsl_parameter_declaration_strategy = st.builds(
    myDsl_parameter_declaration,
)
myDsl_identifier_list_strategy = st.builds(
    myDsl_identifier_list,
    identifier=
        safe_text
)
myDsl_parameter_type_list_strategy = st.builds(
    myDsl_parameter_type_list,
)
myDsl_assignment_expression_strategy = st.builds(
    myDsl_assignment_expression,
    assignment_operator=
        safe_text
)
myDsl_direct_declarator_complemento_strategy = st.builds(
    myDsl_direct_declarator_complemento,
)
myDsl_direct_declarator_linha_strategy = st.builds(
    myDsl_direct_declarator_linha,
)
myDsl_type_qualifier_list_linha_strategy = st.builds(
    myDsl_type_qualifier_list_linha,
)
direct_abstract_declarator_complement_strategy = st.builds(
    direct_abstract_declarator_complement,
)
myDsl_type_qualifier_list_strategy = st.builds(
    myDsl_type_qualifier_list,
)
myDsl_direct_declarator_strategy = st.builds(
    myDsl_direct_declarator,
    identifier=
        safe_text
)
myDsl_pointer_strategy = st.builds(
    myDsl_pointer,
)
myDsl_declaration_list_linha_strategy = st.builds(
    myDsl_declaration_list_linha,
)
myDsl_compound_statement_strategy = st.builds(
    myDsl_compound_statement,
)
myDsl_declaration_list_strategy = st.builds(
    myDsl_declaration_list,
)
myDsl_parameter_lista_strategy = st.builds(
    myDsl_parameter_lista,
)
myDsl_init_declarator_list_strategy = st.builds(
    myDsl_init_declarator_list,
)
myDsl_declarator_strategy = st.builds(
    myDsl_declarator,
)
myDsl_struct_declarator_list_linha_strategy = st.builds(
    myDsl_struct_declarator_list_linha,
)
myDsl_struct_declarator_strategy = st.builds(
    myDsl_struct_declarator,
)
myDsl_static_assert_declaration_strategy = st.builds(
    myDsl_static_assert_declaration,
)
myDsl_struct_declarator_list_strategy = st.builds(
    myDsl_struct_declarator_list,
)
myDsl_specifier_qualifier_list_strategy = st.builds(
    myDsl_specifier_qualifier_list,
)
myDsl_struct_declaration_list_linha_strategy = st.builds(
    myDsl_struct_declaration_list_linha,
)
myDsl_struct_declaration_strategy = st.builds(
    myDsl_struct_declaration,
)
myDsl_struct_or_union_specifier_complement_strategy = st.builds(
    myDsl_struct_or_union_specifier_complement,
)
myDsl_struct_declaration_list_strategy = st.builds(
    myDsl_struct_declaration_list,
)
myDsl_enumeration_constant_strategy = st.builds(
    myDsl_enumeration_constant,
    identifier=
        safe_text
)
myDsl_enumerator_list_linha_strategy = st.builds(
    myDsl_enumerator_list_linha,
)
myDsl_enumerator_strategy = st.builds(
    myDsl_enumerator,
)
myDsl_enumerator_list_strategy = st.builds(
    myDsl_enumerator_list,
)
myDsl_enum_specifier_strategy = st.builds(
    myDsl_enum_specifier,
    identifier=
        safe_text
)
argument_expression_list_linha_strategy = st.builds(
    argument_expression_list_linha,
)
myDsl_ArgumentExpressionListLinhaAction_strategy = st.builds(
    myDsl_ArgumentExpressionListLinhaAction,
)
postfix_expression_complement_strategy = st.builds(
    postfix_expression_complement,
)
myDsl_PostFixEmpryParams_strategy = st.builds(
    myDsl_PostFixEmpryParams,
)
designator_list_linha_strategy = st.builds(
    designator_list_linha,
)
myDsl_DesignatorListLinhaAction_strategy = st.builds(
    myDsl_DesignatorListLinhaAction,
)
initializer_list_linha_strategy = st.builds(
    initializer_list_linha,
)
myDsl_InitializerListLinhaAction_strategy = st.builds(
    myDsl_InitializerListLinhaAction,
)
init_declarator_list_linha_strategy = st.builds(
    init_declarator_list_linha,
)
myDsl_InitDecclaratorListLinhaAction_strategy = st.builds(
    myDsl_InitDecclaratorListLinhaAction,
)
unary_expression_strategy = st.builds(
    unary_expression,
)
myDsl_PlusPlus_strategy = st.builds(
    myDsl_PlusPlus,
    plus=
        safe_text
)
direct_abstract_declarator_linha_strategy = st.builds(
    direct_abstract_declarator_linha,
)
myDsl_DirectAbstractDeclarratorLinhaAction_strategy = st.builds(
    myDsl_DirectAbstractDeclarratorLinhaAction,
)
type_qualifier_list_linha_strategy = st.builds(
    type_qualifier_list_linha,
)
myDsl_TypeQualifierListLinhaAtion_strategy = st.builds(
    myDsl_TypeQualifierListLinhaAtion,
)
declaration_list_linha_strategy = st.builds(
    declaration_list_linha,
)
myDsl_DeclarationListLinhaAction_strategy = st.builds(
    myDsl_DeclarationListLinhaAction,
)
myDsl_struct_or_union_specifier_strategy = st.builds(
    myDsl_struct_or_union_specifier,
    identifier=
        safe_text,
    struct_or_union=
        safe_text
)
myDsl_atomic_type_specifier_strategy = st.builds(
    myDsl_atomic_type_specifier,
)
myDsl_constant_expression_strategy = st.builds(
    myDsl_constant_expression,
)
myDsl_type_name_strategy = st.builds(
    myDsl_type_name,
)
myDsl_alignment_specifier_strategy = st.builds(
    myDsl_alignment_specifier,
)
myDsl_type_qualifier_strategy = st.builds(
    myDsl_type_qualifier,
    namez=
        safe_text
)
myDsl_type_specifier_strategy = st.builds(
    myDsl_type_specifier,
    type_name_str=
        safe_text
)
myDsl_declaration_specifiers_strategy = st.builds(
    myDsl_declaration_specifiers,
    function_specifier=
        safe_text,
    storage_class_specifier=
        safe_text
)
myDsl_declaration_strategy = st.builds(
    myDsl_declaration,
)
myDsl_function_definition_strategy = st.builds(
    myDsl_function_definition,
)
myDsl_translation_unit_linha_strategy = st.builds(
    myDsl_translation_unit_linha,
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

@given(instance=struct_declarator_list_linha_strategy)
@settings(max_examples=50)
def test_struct_declarator_list_linha_instantiation(instance):
    assert isinstance(instance, struct_declarator_list_linha)

@given(instance=myDsl_StructDeclaratorListLinhaAction_strategy)
@settings(max_examples=50)
def test_mydsl_structdeclaratorlistlinhaaction_instantiation(instance):
    assert isinstance(instance, myDsl_StructDeclaratorListLinhaAction)

@given(instance=postfix_expression_linha_strategy)
@settings(max_examples=50)
def test_postfix_expression_linha_instantiation(instance):
    assert isinstance(instance, postfix_expression_linha)

@given(instance=myDsl_PostfixExpressionLinhaAction_strategy)
@settings(max_examples=50)
def test_mydsl_postfixexpressionlinhaaction_instantiation(instance):
    assert isinstance(instance, myDsl_PostfixExpressionLinhaAction)

@given(instance=generic_assoc_list_linha_strategy)
@settings(max_examples=50)
def test_generic_assoc_list_linha_instantiation(instance):
    assert isinstance(instance, generic_assoc_list_linha)

@given(instance=myDsl_GenericAssocListLinhaAction_strategy)
@settings(max_examples=50)
def test_mydsl_genericassoclistlinhaaction_instantiation(instance):
    assert isinstance(instance, myDsl_GenericAssocListLinhaAction)

@given(instance=translation_unit_linha_strategy)
@settings(max_examples=50)
def test_translation_unit_linha_instantiation(instance):
    assert isinstance(instance, translation_unit_linha)

@given(instance=myDsl_TranlationUnitLinhaAction_strategy)
@settings(max_examples=50)
def test_mydsl_tranlationunitlinhaaction_instantiation(instance):
    assert isinstance(instance, myDsl_TranlationUnitLinhaAction)

@given(instance=identifier_list_linha_strategy)
@settings(max_examples=50)
def test_identifier_list_linha_instantiation(instance):
    assert isinstance(instance, identifier_list_linha)

@given(instance=myDsl_IdentifierListLinhaAction_strategy)
@settings(max_examples=50)
def test_mydsl_identifierlistlinhaaction_instantiation(instance):
    assert isinstance(instance, myDsl_IdentifierListLinhaAction)



@given(instance=myDsl_IdentifierListLinhaAction_strategy)
def test_mydsl_identifierlistlinhaaction_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=myDsl_init_declarator_strategy)
@settings(max_examples=50)
def test_mydsl_init_declarator_instantiation(instance):
    assert isinstance(instance, myDsl_init_declarator)

@given(instance=myDsl_expression_linha_strategy)
@settings(max_examples=50)
def test_mydsl_expression_linha_instantiation(instance):
    assert isinstance(instance, myDsl_expression_linha)

@given(instance=struct_declaration_list_linha_strategy)
@settings(max_examples=50)
def test_struct_declaration_list_linha_instantiation(instance):
    assert isinstance(instance, struct_declaration_list_linha)

@given(instance=myDsl_StructDeclarationListLinhaAction_strategy)
@settings(max_examples=50)
def test_mydsl_structdeclarationlistlinhaaction_instantiation(instance):
    assert isinstance(instance, myDsl_StructDeclarationListLinhaAction)

@given(instance=struct_or_union_specifier_complement_strategy)
@settings(max_examples=50)
def test_struct_or_union_specifier_complement_instantiation(instance):
    assert isinstance(instance, struct_or_union_specifier_complement)

@given(instance=myDsl_StructOrUnionSpecifierComplementAction_strategy)
@settings(max_examples=50)
def test_mydsl_structorunionspecifiercomplementaction_instantiation(instance):
    assert isinstance(instance, myDsl_StructOrUnionSpecifierComplementAction)

@given(instance=enumerator_list_linha_strategy)
@settings(max_examples=50)
def test_enumerator_list_linha_instantiation(instance):
    assert isinstance(instance, enumerator_list_linha)

@given(instance=myDsl_EnumeratorListLinhaAction_strategy)
@settings(max_examples=50)
def test_mydsl_enumeratorlistlinhaaction_instantiation(instance):
    assert isinstance(instance, myDsl_EnumeratorListLinhaAction)

@given(instance=myDsl_string_dsl_strategy)
@settings(max_examples=50)
def test_mydsl_string_dsl_instantiation(instance):
    assert isinstance(instance, myDsl_string_dsl)



@given(instance=myDsl_string_dsl_strategy)
def test_mydsl_string_dsl___func___setter(instance):
    original = instance.__func__
    instance.__func__ = original
    assert instance.__func__ == original



@given(instance=myDsl_string_dsl_strategy)
def test_mydsl_string_dsl_string_literal_setter(instance):
    original = instance.string_literal
    instance.string_literal = original
    assert instance.string_literal == original

@given(instance=myDsl_conditional_expression_linha_strategy)
@settings(max_examples=50)
def test_mydsl_conditional_expression_linha_instantiation(instance):
    assert isinstance(instance, myDsl_conditional_expression_linha)

@given(instance=myDsl_logical_or_expression_linha_strategy)
@settings(max_examples=50)
def test_mydsl_logical_or_expression_linha_instantiation(instance):
    assert isinstance(instance, myDsl_logical_or_expression_linha)

@given(instance=myDsl_logical_or_expression_strategy)
@settings(max_examples=50)
def test_mydsl_logical_or_expression_instantiation(instance):
    assert isinstance(instance, myDsl_logical_or_expression)

@given(instance=myDsl_logical_and_expression_linha_strategy)
@settings(max_examples=50)
def test_mydsl_logical_and_expression_linha_instantiation(instance):
    assert isinstance(instance, myDsl_logical_and_expression_linha)

@given(instance=myDsl_logical_and_expression_strategy)
@settings(max_examples=50)
def test_mydsl_logical_and_expression_instantiation(instance):
    assert isinstance(instance, myDsl_logical_and_expression)

@given(instance=postfix_expression_strategy)
@settings(max_examples=50)
def test_postfix_expression_instantiation(instance):
    assert isinstance(instance, postfix_expression)

@given(instance=myDsl_block_item_list_linha_strategy)
@settings(max_examples=50)
def test_mydsl_block_item_list_linha_instantiation(instance):
    assert isinstance(instance, myDsl_block_item_list_linha)

@given(instance=myDsl_block_item_strategy)
@settings(max_examples=50)
def test_mydsl_block_item_instantiation(instance):
    assert isinstance(instance, myDsl_block_item)

@given(instance=myDsl_block_item_list_strategy)
@settings(max_examples=50)
def test_mydsl_block_item_list_instantiation(instance):
    assert isinstance(instance, myDsl_block_item_list)

@given(instance=myDsl_inclusive_or_expression_linha_strategy)
@settings(max_examples=50)
def test_mydsl_inclusive_or_expression_linha_instantiation(instance):
    assert isinstance(instance, myDsl_inclusive_or_expression_linha)

@given(instance=myDsl_inclusive_or_expression_strategy)
@settings(max_examples=50)
def test_mydsl_inclusive_or_expression_instantiation(instance):
    assert isinstance(instance, myDsl_inclusive_or_expression)

@given(instance=myDsl_exclusive_or_expression_linha_strategy)
@settings(max_examples=50)
def test_mydsl_exclusive_or_expression_linha_instantiation(instance):
    assert isinstance(instance, myDsl_exclusive_or_expression_linha)

@given(instance=myDsl_exclusive_or_expression_strategy)
@settings(max_examples=50)
def test_mydsl_exclusive_or_expression_instantiation(instance):
    assert isinstance(instance, myDsl_exclusive_or_expression)

@given(instance=myDsl_and_expression_linha_strategy)
@settings(max_examples=50)
def test_mydsl_and_expression_linha_instantiation(instance):
    assert isinstance(instance, myDsl_and_expression_linha)

@given(instance=myDsl_and_expression_strategy)
@settings(max_examples=50)
def test_mydsl_and_expression_instantiation(instance):
    assert isinstance(instance, myDsl_and_expression)

@given(instance=myDsl_jump_statement_strategy)
@settings(max_examples=50)
def test_mydsl_jump_statement_instantiation(instance):
    assert isinstance(instance, myDsl_jump_statement)



@given(instance=myDsl_jump_statement_strategy)
def test_mydsl_jump_statement_break__setter(instance):
    original = instance.break_
    instance.break_ = original
    assert instance.break_ == original



@given(instance=myDsl_jump_statement_strategy)
def test_mydsl_jump_statement_return__setter(instance):
    original = instance.return_
    instance.return_ = original
    assert instance.return_ == original



@given(instance=myDsl_jump_statement_strategy)
def test_mydsl_jump_statement_return_vazio_setter(instance):
    original = instance.return_vazio
    instance.return_vazio = original
    assert instance.return_vazio == original



@given(instance=myDsl_jump_statement_strategy)
def test_mydsl_jump_statement_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=myDsl_iteration_statement_strategy)
@settings(max_examples=50)
def test_mydsl_iteration_statement_instantiation(instance):
    assert isinstance(instance, myDsl_iteration_statement)

@given(instance=myDsl_selection_statement_strategy)
@settings(max_examples=50)
def test_mydsl_selection_statement_instantiation(instance):
    assert isinstance(instance, myDsl_selection_statement)

@given(instance=myDsl_expression_statement_strategy)
@settings(max_examples=50)
def test_mydsl_expression_statement_instantiation(instance):
    assert isinstance(instance, myDsl_expression_statement)

@given(instance=myDsl_labeled_statement_strategy)
@settings(max_examples=50)
def test_mydsl_labeled_statement_instantiation(instance):
    assert isinstance(instance, myDsl_labeled_statement)



@given(instance=myDsl_labeled_statement_strategy)
def test_mydsl_labeled_statement_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=myDsl_statement_strategy)
@settings(max_examples=50)
def test_mydsl_statement_instantiation(instance):
    assert isinstance(instance, myDsl_statement)

@given(instance=myDsl_shift_expression_complement_strategy)
@settings(max_examples=50)
def test_mydsl_shift_expression_complement_instantiation(instance):
    assert isinstance(instance, myDsl_shift_expression_complement)



@given(instance=myDsl_shift_expression_complement_strategy)
def test_mydsl_shift_expression_complement_sright_setter(instance):
    original = instance.sright
    instance.sright = original
    assert instance.sright == original



@given(instance=myDsl_shift_expression_complement_strategy)
def test_mydsl_shift_expression_complement_sleft_setter(instance):
    original = instance.sleft
    instance.sleft = original
    assert instance.sleft == original

@given(instance=myDsl_shift_expression_linha_strategy)
@settings(max_examples=50)
def test_mydsl_shift_expression_linha_instantiation(instance):
    assert isinstance(instance, myDsl_shift_expression_linha)

@given(instance=myDsl_shift_expression_strategy)
@settings(max_examples=50)
def test_mydsl_shift_expression_instantiation(instance):
    assert isinstance(instance, myDsl_shift_expression)

@given(instance=myDsl_additive_expression_complement_strategy)
@settings(max_examples=50)
def test_mydsl_additive_expression_complement_instantiation(instance):
    assert isinstance(instance, myDsl_additive_expression_complement)



@given(instance=myDsl_additive_expression_complement_strategy)
def test_mydsl_additive_expression_complement_menos_setter(instance):
    original = instance.menos
    instance.menos = original
    assert instance.menos == original



@given(instance=myDsl_additive_expression_complement_strategy)
def test_mydsl_additive_expression_complement_mais_setter(instance):
    original = instance.mais
    instance.mais = original
    assert instance.mais == original

@given(instance=myDsl_additive_expression_linha_strategy)
@settings(max_examples=50)
def test_mydsl_additive_expression_linha_instantiation(instance):
    assert isinstance(instance, myDsl_additive_expression_linha)

@given(instance=myDsl_equality_expression_complement_strategy)
@settings(max_examples=50)
def test_mydsl_equality_expression_complement_instantiation(instance):
    assert isinstance(instance, myDsl_equality_expression_complement)



@given(instance=myDsl_equality_expression_complement_strategy)
def test_mydsl_equality_expression_complement_maior_setter(instance):
    original = instance.maior
    instance.maior = original
    assert instance.maior == original



@given(instance=myDsl_equality_expression_complement_strategy)
def test_mydsl_equality_expression_complement_maior_igual_setter(instance):
    original = instance.maior_igual
    instance.maior_igual = original
    assert instance.maior_igual == original



@given(instance=myDsl_equality_expression_complement_strategy)
def test_mydsl_equality_expression_complement_n_igual_setter(instance):
    original = instance.n_igual
    instance.n_igual = original
    assert instance.n_igual == original



@given(instance=myDsl_equality_expression_complement_strategy)
def test_mydsl_equality_expression_complement_menor_setter(instance):
    original = instance.menor
    instance.menor = original
    assert instance.menor == original



@given(instance=myDsl_equality_expression_complement_strategy)
def test_mydsl_equality_expression_complement_igual_setter(instance):
    original = instance.igual
    instance.igual = original
    assert instance.igual == original



@given(instance=myDsl_equality_expression_complement_strategy)
def test_mydsl_equality_expression_complement_menor_igual_setter(instance):
    original = instance.menor_igual
    instance.menor_igual = original
    assert instance.menor_igual == original

@given(instance=myDsl_equality_expression_linha_strategy)
@settings(max_examples=50)
def test_mydsl_equality_expression_linha_instantiation(instance):
    assert isinstance(instance, myDsl_equality_expression_linha)

@given(instance=myDsl_equality_expression_strategy)
@settings(max_examples=50)
def test_mydsl_equality_expression_instantiation(instance):
    assert isinstance(instance, myDsl_equality_expression)

@given(instance=myDsl_relational_expression_complement_strategy)
@settings(max_examples=50)
def test_mydsl_relational_expression_complement_instantiation(instance):
    assert isinstance(instance, myDsl_relational_expression_complement)



@given(instance=myDsl_relational_expression_complement_strategy)
def test_mydsl_relational_expression_complement_menor_igual_setter(instance):
    original = instance.menor_igual
    instance.menor_igual = original
    assert instance.menor_igual == original



@given(instance=myDsl_relational_expression_complement_strategy)
def test_mydsl_relational_expression_complement_menor_setter(instance):
    original = instance.menor
    instance.menor = original
    assert instance.menor == original



@given(instance=myDsl_relational_expression_complement_strategy)
def test_mydsl_relational_expression_complement_maior_igual_setter(instance):
    original = instance.maior_igual
    instance.maior_igual = original
    assert instance.maior_igual == original



@given(instance=myDsl_relational_expression_complement_strategy)
def test_mydsl_relational_expression_complement_maior_setter(instance):
    original = instance.maior
    instance.maior = original
    assert instance.maior == original

@given(instance=myDsl_relational_expression_linha_strategy)
@settings(max_examples=50)
def test_mydsl_relational_expression_linha_instantiation(instance):
    assert isinstance(instance, myDsl_relational_expression_linha)

@given(instance=myDsl_relational_expression_strategy)
@settings(max_examples=50)
def test_mydsl_relational_expression_instantiation(instance):
    assert isinstance(instance, myDsl_relational_expression)

@given(instance=myDsl_additive_expression_strategy)
@settings(max_examples=50)
def test_mydsl_additive_expression_instantiation(instance):
    assert isinstance(instance, myDsl_additive_expression)

@given(instance=myDsl_multiplicative_expression_complement_strategy)
@settings(max_examples=50)
def test_mydsl_multiplicative_expression_complement_instantiation(instance):
    assert isinstance(instance, myDsl_multiplicative_expression_complement)



@given(instance=myDsl_multiplicative_expression_complement_strategy)
def test_mydsl_multiplicative_expression_complement_modulo_setter(instance):
    original = instance.modulo
    instance.modulo = original
    assert instance.modulo == original



@given(instance=myDsl_multiplicative_expression_complement_strategy)
def test_mydsl_multiplicative_expression_complement_multiplica_setter(instance):
    original = instance.multiplica
    instance.multiplica = original
    assert instance.multiplica == original



@given(instance=myDsl_multiplicative_expression_complement_strategy)
def test_mydsl_multiplicative_expression_complement_divide_setter(instance):
    original = instance.divide
    instance.divide = original
    assert instance.divide == original

@given(instance=myDsl_multiplicative_expression_linha_strategy)
@settings(max_examples=50)
def test_mydsl_multiplicative_expression_linha_instantiation(instance):
    assert isinstance(instance, myDsl_multiplicative_expression_linha)

@given(instance=myDsl_multiplicative_expression_strategy)
@settings(max_examples=50)
def test_mydsl_multiplicative_expression_instantiation(instance):
    assert isinstance(instance, myDsl_multiplicative_expression)

@given(instance=myDsl_cast_expression_strategy)
@settings(max_examples=50)
def test_mydsl_cast_expression_instantiation(instance):
    assert isinstance(instance, myDsl_cast_expression)

@given(instance=myDsl_unary_expression_strategy)
@settings(max_examples=50)
def test_mydsl_unary_expression_instantiation(instance):
    assert isinstance(instance, myDsl_unary_expression)



@given(instance=myDsl_unary_expression_strategy)
def test_mydsl_unary_expression_unary_operator_setter(instance):
    original = instance.unary_operator
    instance.unary_operator = original
    assert instance.unary_operator == original

@given(instance=myDsl_argument_expression_list_linha_strategy)
@settings(max_examples=50)
def test_mydsl_argument_expression_list_linha_instantiation(instance):
    assert isinstance(instance, myDsl_argument_expression_list_linha)

@given(instance=myDsl_argument_expression_list_strategy)
@settings(max_examples=50)
def test_mydsl_argument_expression_list_instantiation(instance):
    assert isinstance(instance, myDsl_argument_expression_list)

@given(instance=myDsl_postfix_expression_complement_strategy)
@settings(max_examples=50)
def test_mydsl_postfix_expression_complement_instantiation(instance):
    assert isinstance(instance, myDsl_postfix_expression_complement)



@given(instance=myDsl_postfix_expression_complement_strategy)
def test_mydsl_postfix_expression_complement_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=myDsl_conditional_expression_strategy)
@settings(max_examples=50)
def test_mydsl_conditional_expression_instantiation(instance):
    assert isinstance(instance, myDsl_conditional_expression)

@given(instance=myDsl_designator_list_linha_strategy)
@settings(max_examples=50)
def test_mydsl_designator_list_linha_instantiation(instance):
    assert isinstance(instance, myDsl_designator_list_linha)

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

@given(instance=myDsl_initializer_list_complement_strategy)
@settings(max_examples=50)
def test_mydsl_initializer_list_complement_instantiation(instance):
    assert isinstance(instance, myDsl_initializer_list_complement)

@given(instance=myDsl_initializer_list_linha_strategy)
@settings(max_examples=50)
def test_mydsl_initializer_list_linha_instantiation(instance):
    assert isinstance(instance, myDsl_initializer_list_linha)

@given(instance=myDsl_init_declarator_list_linha_strategy)
@settings(max_examples=50)
def test_mydsl_init_declarator_list_linha_instantiation(instance):
    assert isinstance(instance, myDsl_init_declarator_list_linha)

@given(instance=myDsl_designation_strategy)
@settings(max_examples=50)
def test_mydsl_designation_instantiation(instance):
    assert isinstance(instance, myDsl_designation)

@given(instance=myDsl_postfix_expression_linha_strategy)
@settings(max_examples=50)
def test_mydsl_postfix_expression_linha_instantiation(instance):
    assert isinstance(instance, myDsl_postfix_expression_linha)

@given(instance=myDsl_postfix_expression_strategy)
@settings(max_examples=50)
def test_mydsl_postfix_expression_instantiation(instance):
    assert isinstance(instance, myDsl_postfix_expression)

@given(instance=myDsl_generic_assoc_list_linha_strategy)
@settings(max_examples=50)
def test_mydsl_generic_assoc_list_linha_instantiation(instance):
    assert isinstance(instance, myDsl_generic_assoc_list_linha)

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

@given(instance=myDsl_generic_selection_strategy)
@settings(max_examples=50)
def test_mydsl_generic_selection_instantiation(instance):
    assert isinstance(instance, myDsl_generic_selection)



@given(instance=myDsl_generic_selection_strategy)
def test_mydsl_generic_selection__generic_setter(instance):
    original = instance._generic
    instance._generic = original
    assert instance._generic == original

@given(instance=myDsl_expression_strategy)
@settings(max_examples=50)
def test_mydsl_expression_instantiation(instance):
    assert isinstance(instance, myDsl_expression)

@given(instance=myDsl_constant_strategy)
@settings(max_examples=50)
def test_mydsl_constant_instantiation(instance):
    assert isinstance(instance, myDsl_constant)



@given(instance=myDsl_constant_strategy)
def test_mydsl_constant_i_constant_setter(instance):
    original = instance.i_constant
    instance.i_constant = original
    assert instance.i_constant == original



@given(instance=myDsl_constant_strategy)
def test_mydsl_constant_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original



@given(instance=myDsl_constant_strategy)
def test_mydsl_constant_f_constant_setter(instance):
    original = instance.f_constant
    instance.f_constant = original
    assert instance.f_constant == original



@given(instance=myDsl_constant_strategy)
def test_mydsl_constant_enumz_setter(instance):
    original = instance.enumz
    instance.enumz = original
    assert instance.enumz == original



@given(instance=myDsl_constant_strategy)
def test_mydsl_constant_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original

@given(instance=myDsl_primary_expression_strategy)
@settings(max_examples=50)
def test_mydsl_primary_expression_instantiation(instance):
    assert isinstance(instance, myDsl_primary_expression)



@given(instance=myDsl_primary_expression_strategy)
def test_mydsl_primary_expression_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=myDsl_identifier_list_linha_strategy)
@settings(max_examples=50)
def test_mydsl_identifier_list_linha_instantiation(instance):
    assert isinstance(instance, myDsl_identifier_list_linha)

@given(instance=myDsl_direct_abstract_declarator_complement_strategy)
@settings(max_examples=50)
def test_mydsl_direct_abstract_declarator_complement_instantiation(instance):
    assert isinstance(instance, myDsl_direct_abstract_declarator_complement)

@given(instance=myDsl_initializer_list_strategy)
@settings(max_examples=50)
def test_mydsl_initializer_list_instantiation(instance):
    assert isinstance(instance, myDsl_initializer_list)

@given(instance=myDsl_initializer_strategy)
@settings(max_examples=50)
def test_mydsl_initializer_instantiation(instance):
    assert isinstance(instance, myDsl_initializer)

@given(instance=myDsl_direct_abstract_declarator_linha_strategy)
@settings(max_examples=50)
def test_mydsl_direct_abstract_declarator_linha_instantiation(instance):
    assert isinstance(instance, myDsl_direct_abstract_declarator_linha)

@given(instance=myDsl_direct_abstract_declarator_strategy)
@settings(max_examples=50)
def test_mydsl_direct_abstract_declarator_instantiation(instance):
    assert isinstance(instance, myDsl_direct_abstract_declarator)

@given(instance=myDsl_abstract_declarator_strategy)
@settings(max_examples=50)
def test_mydsl_abstract_declarator_instantiation(instance):
    assert isinstance(instance, myDsl_abstract_declarator)

@given(instance=myDsl_parameter_list_linha_strategy)
@settings(max_examples=50)
def test_mydsl_parameter_list_linha_instantiation(instance):
    assert isinstance(instance, myDsl_parameter_list_linha)

@given(instance=myDsl_parameter_declaration_strategy)
@settings(max_examples=50)
def test_mydsl_parameter_declaration_instantiation(instance):
    assert isinstance(instance, myDsl_parameter_declaration)

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

@given(instance=myDsl_assignment_expression_strategy)
@settings(max_examples=50)
def test_mydsl_assignment_expression_instantiation(instance):
    assert isinstance(instance, myDsl_assignment_expression)



@given(instance=myDsl_assignment_expression_strategy)
def test_mydsl_assignment_expression_assignment_operator_setter(instance):
    original = instance.assignment_operator
    instance.assignment_operator = original
    assert instance.assignment_operator == original

@given(instance=myDsl_direct_declarator_complemento_strategy)
@settings(max_examples=50)
def test_mydsl_direct_declarator_complemento_instantiation(instance):
    assert isinstance(instance, myDsl_direct_declarator_complemento)

@given(instance=myDsl_direct_declarator_linha_strategy)
@settings(max_examples=50)
def test_mydsl_direct_declarator_linha_instantiation(instance):
    assert isinstance(instance, myDsl_direct_declarator_linha)

@given(instance=myDsl_type_qualifier_list_linha_strategy)
@settings(max_examples=50)
def test_mydsl_type_qualifier_list_linha_instantiation(instance):
    assert isinstance(instance, myDsl_type_qualifier_list_linha)

@given(instance=direct_abstract_declarator_complement_strategy)
@settings(max_examples=50)
def test_direct_abstract_declarator_complement_instantiation(instance):
    assert isinstance(instance, direct_abstract_declarator_complement)

@given(instance=myDsl_type_qualifier_list_strategy)
@settings(max_examples=50)
def test_mydsl_type_qualifier_list_instantiation(instance):
    assert isinstance(instance, myDsl_type_qualifier_list)

@given(instance=myDsl_direct_declarator_strategy)
@settings(max_examples=50)
def test_mydsl_direct_declarator_instantiation(instance):
    assert isinstance(instance, myDsl_direct_declarator)



@given(instance=myDsl_direct_declarator_strategy)
def test_mydsl_direct_declarator_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=myDsl_pointer_strategy)
@settings(max_examples=50)
def test_mydsl_pointer_instantiation(instance):
    assert isinstance(instance, myDsl_pointer)

@given(instance=myDsl_declaration_list_linha_strategy)
@settings(max_examples=50)
def test_mydsl_declaration_list_linha_instantiation(instance):
    assert isinstance(instance, myDsl_declaration_list_linha)

@given(instance=myDsl_compound_statement_strategy)
@settings(max_examples=50)
def test_mydsl_compound_statement_instantiation(instance):
    assert isinstance(instance, myDsl_compound_statement)

@given(instance=myDsl_declaration_list_strategy)
@settings(max_examples=50)
def test_mydsl_declaration_list_instantiation(instance):
    assert isinstance(instance, myDsl_declaration_list)

@given(instance=myDsl_parameter_lista_strategy)
@settings(max_examples=50)
def test_mydsl_parameter_lista_instantiation(instance):
    assert isinstance(instance, myDsl_parameter_lista)

@given(instance=myDsl_init_declarator_list_strategy)
@settings(max_examples=50)
def test_mydsl_init_declarator_list_instantiation(instance):
    assert isinstance(instance, myDsl_init_declarator_list)

@given(instance=myDsl_declarator_strategy)
@settings(max_examples=50)
def test_mydsl_declarator_instantiation(instance):
    assert isinstance(instance, myDsl_declarator)

@given(instance=myDsl_struct_declarator_list_linha_strategy)
@settings(max_examples=50)
def test_mydsl_struct_declarator_list_linha_instantiation(instance):
    assert isinstance(instance, myDsl_struct_declarator_list_linha)

@given(instance=myDsl_struct_declarator_strategy)
@settings(max_examples=50)
def test_mydsl_struct_declarator_instantiation(instance):
    assert isinstance(instance, myDsl_struct_declarator)

@given(instance=myDsl_static_assert_declaration_strategy)
@settings(max_examples=50)
def test_mydsl_static_assert_declaration_instantiation(instance):
    assert isinstance(instance, myDsl_static_assert_declaration)

@given(instance=myDsl_struct_declarator_list_strategy)
@settings(max_examples=50)
def test_mydsl_struct_declarator_list_instantiation(instance):
    assert isinstance(instance, myDsl_struct_declarator_list)

@given(instance=myDsl_specifier_qualifier_list_strategy)
@settings(max_examples=50)
def test_mydsl_specifier_qualifier_list_instantiation(instance):
    assert isinstance(instance, myDsl_specifier_qualifier_list)

@given(instance=myDsl_struct_declaration_list_linha_strategy)
@settings(max_examples=50)
def test_mydsl_struct_declaration_list_linha_instantiation(instance):
    assert isinstance(instance, myDsl_struct_declaration_list_linha)

@given(instance=myDsl_struct_declaration_strategy)
@settings(max_examples=50)
def test_mydsl_struct_declaration_instantiation(instance):
    assert isinstance(instance, myDsl_struct_declaration)

@given(instance=myDsl_struct_or_union_specifier_complement_strategy)
@settings(max_examples=50)
def test_mydsl_struct_or_union_specifier_complement_instantiation(instance):
    assert isinstance(instance, myDsl_struct_or_union_specifier_complement)

@given(instance=myDsl_struct_declaration_list_strategy)
@settings(max_examples=50)
def test_mydsl_struct_declaration_list_instantiation(instance):
    assert isinstance(instance, myDsl_struct_declaration_list)

@given(instance=myDsl_enumeration_constant_strategy)
@settings(max_examples=50)
def test_mydsl_enumeration_constant_instantiation(instance):
    assert isinstance(instance, myDsl_enumeration_constant)



@given(instance=myDsl_enumeration_constant_strategy)
def test_mydsl_enumeration_constant_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=myDsl_enumerator_list_linha_strategy)
@settings(max_examples=50)
def test_mydsl_enumerator_list_linha_instantiation(instance):
    assert isinstance(instance, myDsl_enumerator_list_linha)

@given(instance=myDsl_enumerator_strategy)
@settings(max_examples=50)
def test_mydsl_enumerator_instantiation(instance):
    assert isinstance(instance, myDsl_enumerator)

@given(instance=myDsl_enumerator_list_strategy)
@settings(max_examples=50)
def test_mydsl_enumerator_list_instantiation(instance):
    assert isinstance(instance, myDsl_enumerator_list)

@given(instance=myDsl_enum_specifier_strategy)
@settings(max_examples=50)
def test_mydsl_enum_specifier_instantiation(instance):
    assert isinstance(instance, myDsl_enum_specifier)



@given(instance=myDsl_enum_specifier_strategy)
def test_mydsl_enum_specifier_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=argument_expression_list_linha_strategy)
@settings(max_examples=50)
def test_argument_expression_list_linha_instantiation(instance):
    assert isinstance(instance, argument_expression_list_linha)

@given(instance=myDsl_ArgumentExpressionListLinhaAction_strategy)
@settings(max_examples=50)
def test_mydsl_argumentexpressionlistlinhaaction_instantiation(instance):
    assert isinstance(instance, myDsl_ArgumentExpressionListLinhaAction)

@given(instance=postfix_expression_complement_strategy)
@settings(max_examples=50)
def test_postfix_expression_complement_instantiation(instance):
    assert isinstance(instance, postfix_expression_complement)

@given(instance=myDsl_PostFixEmpryParams_strategy)
@settings(max_examples=50)
def test_mydsl_postfixempryparams_instantiation(instance):
    assert isinstance(instance, myDsl_PostFixEmpryParams)

@given(instance=designator_list_linha_strategy)
@settings(max_examples=50)
def test_designator_list_linha_instantiation(instance):
    assert isinstance(instance, designator_list_linha)

@given(instance=myDsl_DesignatorListLinhaAction_strategy)
@settings(max_examples=50)
def test_mydsl_designatorlistlinhaaction_instantiation(instance):
    assert isinstance(instance, myDsl_DesignatorListLinhaAction)

@given(instance=initializer_list_linha_strategy)
@settings(max_examples=50)
def test_initializer_list_linha_instantiation(instance):
    assert isinstance(instance, initializer_list_linha)

@given(instance=myDsl_InitializerListLinhaAction_strategy)
@settings(max_examples=50)
def test_mydsl_initializerlistlinhaaction_instantiation(instance):
    assert isinstance(instance, myDsl_InitializerListLinhaAction)

@given(instance=init_declarator_list_linha_strategy)
@settings(max_examples=50)
def test_init_declarator_list_linha_instantiation(instance):
    assert isinstance(instance, init_declarator_list_linha)

@given(instance=myDsl_InitDecclaratorListLinhaAction_strategy)
@settings(max_examples=50)
def test_mydsl_initdecclaratorlistlinhaaction_instantiation(instance):
    assert isinstance(instance, myDsl_InitDecclaratorListLinhaAction)

@given(instance=unary_expression_strategy)
@settings(max_examples=50)
def test_unary_expression_instantiation(instance):
    assert isinstance(instance, unary_expression)

@given(instance=myDsl_PlusPlus_strategy)
@settings(max_examples=50)
def test_mydsl_plusplus_instantiation(instance):
    assert isinstance(instance, myDsl_PlusPlus)



@given(instance=myDsl_PlusPlus_strategy)
def test_mydsl_plusplus_plus_setter(instance):
    original = instance.plus
    instance.plus = original
    assert instance.plus == original

@given(instance=direct_abstract_declarator_linha_strategy)
@settings(max_examples=50)
def test_direct_abstract_declarator_linha_instantiation(instance):
    assert isinstance(instance, direct_abstract_declarator_linha)

@given(instance=myDsl_DirectAbstractDeclarratorLinhaAction_strategy)
@settings(max_examples=50)
def test_mydsl_directabstractdeclarratorlinhaaction_instantiation(instance):
    assert isinstance(instance, myDsl_DirectAbstractDeclarratorLinhaAction)

@given(instance=type_qualifier_list_linha_strategy)
@settings(max_examples=50)
def test_type_qualifier_list_linha_instantiation(instance):
    assert isinstance(instance, type_qualifier_list_linha)

@given(instance=myDsl_TypeQualifierListLinhaAtion_strategy)
@settings(max_examples=50)
def test_mydsl_typequalifierlistlinhaation_instantiation(instance):
    assert isinstance(instance, myDsl_TypeQualifierListLinhaAtion)

@given(instance=declaration_list_linha_strategy)
@settings(max_examples=50)
def test_declaration_list_linha_instantiation(instance):
    assert isinstance(instance, declaration_list_linha)

@given(instance=myDsl_DeclarationListLinhaAction_strategy)
@settings(max_examples=50)
def test_mydsl_declarationlistlinhaaction_instantiation(instance):
    assert isinstance(instance, myDsl_DeclarationListLinhaAction)

@given(instance=myDsl_struct_or_union_specifier_strategy)
@settings(max_examples=50)
def test_mydsl_struct_or_union_specifier_instantiation(instance):
    assert isinstance(instance, myDsl_struct_or_union_specifier)



@given(instance=myDsl_struct_or_union_specifier_strategy)
def test_mydsl_struct_or_union_specifier_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original



@given(instance=myDsl_struct_or_union_specifier_strategy)
def test_mydsl_struct_or_union_specifier_struct_or_union_setter(instance):
    original = instance.struct_or_union
    instance.struct_or_union = original
    assert instance.struct_or_union == original

@given(instance=myDsl_atomic_type_specifier_strategy)
@settings(max_examples=50)
def test_mydsl_atomic_type_specifier_instantiation(instance):
    assert isinstance(instance, myDsl_atomic_type_specifier)

@given(instance=myDsl_constant_expression_strategy)
@settings(max_examples=50)
def test_mydsl_constant_expression_instantiation(instance):
    assert isinstance(instance, myDsl_constant_expression)

@given(instance=myDsl_type_name_strategy)
@settings(max_examples=50)
def test_mydsl_type_name_instantiation(instance):
    assert isinstance(instance, myDsl_type_name)

@given(instance=myDsl_alignment_specifier_strategy)
@settings(max_examples=50)
def test_mydsl_alignment_specifier_instantiation(instance):
    assert isinstance(instance, myDsl_alignment_specifier)

@given(instance=myDsl_type_qualifier_strategy)
@settings(max_examples=50)
def test_mydsl_type_qualifier_instantiation(instance):
    assert isinstance(instance, myDsl_type_qualifier)



@given(instance=myDsl_type_qualifier_strategy)
def test_mydsl_type_qualifier_namez_setter(instance):
    original = instance.namez
    instance.namez = original
    assert instance.namez == original

@given(instance=myDsl_type_specifier_strategy)
@settings(max_examples=50)
def test_mydsl_type_specifier_instantiation(instance):
    assert isinstance(instance, myDsl_type_specifier)



@given(instance=myDsl_type_specifier_strategy)
def test_mydsl_type_specifier_type_name_str_setter(instance):
    original = instance.type_name_str
    instance.type_name_str = original
    assert instance.type_name_str == original

@given(instance=myDsl_declaration_specifiers_strategy)
@settings(max_examples=50)
def test_mydsl_declaration_specifiers_instantiation(instance):
    assert isinstance(instance, myDsl_declaration_specifiers)



@given(instance=myDsl_declaration_specifiers_strategy)
def test_mydsl_declaration_specifiers_function_specifier_setter(instance):
    original = instance.function_specifier
    instance.function_specifier = original
    assert instance.function_specifier == original



@given(instance=myDsl_declaration_specifiers_strategy)
def test_mydsl_declaration_specifiers_storage_class_specifier_setter(instance):
    original = instance.storage_class_specifier
    instance.storage_class_specifier = original
    assert instance.storage_class_specifier == original

@given(instance=myDsl_declaration_strategy)
@settings(max_examples=50)
def test_mydsl_declaration_instantiation(instance):
    assert isinstance(instance, myDsl_declaration)

@given(instance=myDsl_function_definition_strategy)
@settings(max_examples=50)
def test_mydsl_function_definition_instantiation(instance):
    assert isinstance(instance, myDsl_function_definition)

@given(instance=myDsl_translation_unit_linha_strategy)
@settings(max_examples=50)
def test_mydsl_translation_unit_linha_instantiation(instance):
    assert isinstance(instance, myDsl_translation_unit_linha)

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
