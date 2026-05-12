import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    abstraction_declaration,
    pascal_bound_specification,
    pascal_unpacked_conformant_array_schema,
    pascal_packed_conformant_array_schema,
    pascal_conformant_array_schema,
    pascal_parameter_type,
    pascal_variable_parameter_section,
    pascal_value_parameter_section,
    pascal_formal_parameter_section,
    pascal_formal_parameter_list,
    pascal_record_section,
    pascal_variant_part,
    pascal_fixed_part,
    pascal_abstraction_declaration,
    pascal_abstraction_heading,
    pascal_variant,
    pascal_tag_field,
    pascal_variable_section,
    pascal_variable_identifier_list,
    pascal_enumerated_type,
    pascal_field_list,
    pascal_index_type,
    pascal_file_type,
    pascal_set_type,
    pascal_record_type,
    pascal_dynamic_array_type,
    pascal_array_type,
    pascal_unpacked_structured_type,
    pascal_constant,
    pascal_subrange_type,
    pascal_pointer_type,
    pascal_structured_type,
    pascal_simple_type,
    pascal_type,
    pascal_type_definition,
    pascal_constant_definition,
    pascal_for_statement,
    pascal_repeat_statement,
    pascal_while_statement,
    pascal_case_label_list,
    pascal_case_limb,
    pascal_case_statement,
    pascal_if_statement,
    pascal_factor,
    pascal_term,
    pascal_with_statement,
    pascal_conditional_statement,
    pascal_repetitive_statement,
    pascal_compound_statement,
    pascal_any_number,
    pascal_set,
    pascal_number,
    pascal_structured_statement,
    pascal_simple_statement,
    pascal_EObject,
    pascal_simple_expression,
    pascal_expression_list,
    pascal_var_,
    pascal_expression,
    pascal_variable,
    pascal_goto_statement,
    pascal_function_designator,
    pascal_assignment_statement,
    pascal_pascal,
    pascal_label,
    pascal_statement,
    pascal_statement_sequence,
    pascal_statement_part,
    pascal_procedure_and_function_declaration_part,
    pascal_variable_declaration_part,
    pascal_type_definition_part,
    pascal_constant_definition_part,
    pascal_label_declaration_part,
    pascal_identifier_list,
    pascal_block,
    pascal_program_heading_block,
    pascal_program,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstraction_declaration_is_not_abstract():
    assert not inspect.isabstract(abstraction_declaration)


def test_abstraction_declaration_constructor_exists():
    assert callable(abstraction_declaration.__init__)


def test_abstraction_declaration_constructor_args():
    sig = inspect.signature(abstraction_declaration.__init__)
    params = list(sig.parameters.keys())



def test_pascal_bound_specification_is_not_abstract():
    assert not inspect.isabstract(pascal_bound_specification)


def test_pascal_bound_specification_constructor_exists():
    assert callable(pascal_bound_specification.__init__)


def test_pascal_bound_specification_constructor_args():
    sig = inspect.signature(pascal_bound_specification.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "final" in params, "Missing parameter 'final'"
    assert "initial" in params, "Missing parameter 'initial'"

def test_pascal_bound_specification_has_name():
    assert hasattr(pascal_bound_specification, "name")
    descriptor = None
    for klass in pascal_bound_specification.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_pascal_bound_specification_has_final():
    assert hasattr(pascal_bound_specification, "final")
    descriptor = None
    for klass in pascal_bound_specification.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)

def test_pascal_bound_specification_has_initial():
    assert hasattr(pascal_bound_specification, "initial")
    descriptor = None
    for klass in pascal_bound_specification.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)



def test_pascal_unpacked_conformant_array_schema_is_not_abstract():
    assert not inspect.isabstract(pascal_unpacked_conformant_array_schema)


def test_pascal_unpacked_conformant_array_schema_constructor_exists():
    assert callable(pascal_unpacked_conformant_array_schema.__init__)


def test_pascal_unpacked_conformant_array_schema_constructor_args():
    sig = inspect.signature(pascal_unpacked_conformant_array_schema.__init__)
    params = list(sig.parameters.keys())



def test_pascal_packed_conformant_array_schema_is_not_abstract():
    assert not inspect.isabstract(pascal_packed_conformant_array_schema)


def test_pascal_packed_conformant_array_schema_constructor_exists():
    assert callable(pascal_packed_conformant_array_schema.__init__)


def test_pascal_packed_conformant_array_schema_constructor_args():
    sig = inspect.signature(pascal_packed_conformant_array_schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pascal_packed_conformant_array_schema_has_name():
    assert hasattr(pascal_packed_conformant_array_schema, "name")
    descriptor = None
    for klass in pascal_packed_conformant_array_schema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pascal_conformant_array_schema_is_not_abstract():
    assert not inspect.isabstract(pascal_conformant_array_schema)


def test_pascal_conformant_array_schema_constructor_exists():
    assert callable(pascal_conformant_array_schema.__init__)


def test_pascal_conformant_array_schema_constructor_args():
    sig = inspect.signature(pascal_conformant_array_schema.__init__)
    params = list(sig.parameters.keys())



def test_pascal_parameter_type_is_not_abstract():
    assert not inspect.isabstract(pascal_parameter_type)


def test_pascal_parameter_type_constructor_exists():
    assert callable(pascal_parameter_type.__init__)


def test_pascal_parameter_type_constructor_args():
    sig = inspect.signature(pascal_parameter_type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pascal_parameter_type_has_name():
    assert hasattr(pascal_parameter_type, "name")
    descriptor = None
    for klass in pascal_parameter_type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pascal_variable_parameter_section_is_not_abstract():
    assert not inspect.isabstract(pascal_variable_parameter_section)


def test_pascal_variable_parameter_section_constructor_exists():
    assert callable(pascal_variable_parameter_section.__init__)


def test_pascal_variable_parameter_section_constructor_args():
    sig = inspect.signature(pascal_variable_parameter_section.__init__)
    params = list(sig.parameters.keys())



def test_pascal_value_parameter_section_is_not_abstract():
    assert not inspect.isabstract(pascal_value_parameter_section)


def test_pascal_value_parameter_section_constructor_exists():
    assert callable(pascal_value_parameter_section.__init__)


def test_pascal_value_parameter_section_constructor_args():
    sig = inspect.signature(pascal_value_parameter_section.__init__)
    params = list(sig.parameters.keys())



def test_pascal_formal_parameter_section_is_not_abstract():
    assert not inspect.isabstract(pascal_formal_parameter_section)


def test_pascal_formal_parameter_section_constructor_exists():
    assert callable(pascal_formal_parameter_section.__init__)


def test_pascal_formal_parameter_section_constructor_args():
    sig = inspect.signature(pascal_formal_parameter_section.__init__)
    params = list(sig.parameters.keys())



def test_pascal_formal_parameter_list_is_not_abstract():
    assert not inspect.isabstract(pascal_formal_parameter_list)


def test_pascal_formal_parameter_list_constructor_exists():
    assert callable(pascal_formal_parameter_list.__init__)


def test_pascal_formal_parameter_list_constructor_args():
    sig = inspect.signature(pascal_formal_parameter_list.__init__)
    params = list(sig.parameters.keys())



def test_pascal_record_section_is_not_abstract():
    assert not inspect.isabstract(pascal_record_section)


def test_pascal_record_section_constructor_exists():
    assert callable(pascal_record_section.__init__)


def test_pascal_record_section_constructor_args():
    sig = inspect.signature(pascal_record_section.__init__)
    params = list(sig.parameters.keys())



def test_pascal_variant_part_is_not_abstract():
    assert not inspect.isabstract(pascal_variant_part)


def test_pascal_variant_part_constructor_exists():
    assert callable(pascal_variant_part.__init__)


def test_pascal_variant_part_constructor_args():
    sig = inspect.signature(pascal_variant_part.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pascal_variant_part_has_name():
    assert hasattr(pascal_variant_part, "name")
    descriptor = None
    for klass in pascal_variant_part.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pascal_fixed_part_is_not_abstract():
    assert not inspect.isabstract(pascal_fixed_part)


def test_pascal_fixed_part_constructor_exists():
    assert callable(pascal_fixed_part.__init__)


def test_pascal_fixed_part_constructor_args():
    sig = inspect.signature(pascal_fixed_part.__init__)
    params = list(sig.parameters.keys())



def test_pascal_abstraction_declaration_is_not_abstract():
    assert not inspect.isabstract(pascal_abstraction_declaration)


def test_pascal_abstraction_declaration_constructor_exists():
    assert callable(pascal_abstraction_declaration.__init__)


def test_pascal_abstraction_declaration_constructor_args():
    sig = inspect.signature(pascal_abstraction_declaration.__init__)
    params = list(sig.parameters.keys())
    assert "forward" in params, "Missing parameter 'forward'"

def test_pascal_abstraction_declaration_has_forward():
    assert hasattr(pascal_abstraction_declaration, "forward")
    descriptor = None
    for klass in pascal_abstraction_declaration.__mro__:
        if "forward" in klass.__dict__:
            descriptor = klass.__dict__["forward"]
            break
    assert isinstance(descriptor, property)



def test_pascal_abstraction_heading_is_not_abstract():
    assert not inspect.isabstract(pascal_abstraction_heading)


def test_pascal_abstraction_heading_constructor_exists():
    assert callable(pascal_abstraction_heading.__init__)


def test_pascal_abstraction_heading_constructor_args():
    sig = inspect.signature(pascal_abstraction_heading.__init__)
    params = list(sig.parameters.keys())
    assert "returnType" in params, "Missing parameter 'returnType'"
    assert "name" in params, "Missing parameter 'name'"

def test_pascal_abstraction_heading_has_returnType():
    assert hasattr(pascal_abstraction_heading, "returnType")
    descriptor = None
    for klass in pascal_abstraction_heading.__mro__:
        if "returnType" in klass.__dict__:
            descriptor = klass.__dict__["returnType"]
            break
    assert isinstance(descriptor, property)

def test_pascal_abstraction_heading_has_name():
    assert hasattr(pascal_abstraction_heading, "name")
    descriptor = None
    for klass in pascal_abstraction_heading.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pascal_variant_is_not_abstract():
    assert not inspect.isabstract(pascal_variant)


def test_pascal_variant_constructor_exists():
    assert callable(pascal_variant.__init__)


def test_pascal_variant_constructor_args():
    sig = inspect.signature(pascal_variant.__init__)
    params = list(sig.parameters.keys())



def test_pascal_tag_field_is_not_abstract():
    assert not inspect.isabstract(pascal_tag_field)


def test_pascal_tag_field_constructor_exists():
    assert callable(pascal_tag_field.__init__)


def test_pascal_tag_field_constructor_args():
    sig = inspect.signature(pascal_tag_field.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pascal_tag_field_has_name():
    assert hasattr(pascal_tag_field, "name")
    descriptor = None
    for klass in pascal_tag_field.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pascal_variable_section_is_not_abstract():
    assert not inspect.isabstract(pascal_variable_section)


def test_pascal_variable_section_constructor_exists():
    assert callable(pascal_variable_section.__init__)


def test_pascal_variable_section_constructor_args():
    sig = inspect.signature(pascal_variable_section.__init__)
    params = list(sig.parameters.keys())



def test_pascal_variable_identifier_list_is_not_abstract():
    assert not inspect.isabstract(pascal_variable_identifier_list)


def test_pascal_variable_identifier_list_constructor_exists():
    assert callable(pascal_variable_identifier_list.__init__)


def test_pascal_variable_identifier_list_constructor_args():
    sig = inspect.signature(pascal_variable_identifier_list.__init__)
    params = list(sig.parameters.keys())
    assert "names" in params, "Missing parameter 'names'"

def test_pascal_variable_identifier_list_has_names():
    assert hasattr(pascal_variable_identifier_list, "names")
    descriptor = None
    for klass in pascal_variable_identifier_list.__mro__:
        if "names" in klass.__dict__:
            descriptor = klass.__dict__["names"]
            break
    assert isinstance(descriptor, property)



def test_pascal_enumerated_type_is_not_abstract():
    assert not inspect.isabstract(pascal_enumerated_type)


def test_pascal_enumerated_type_constructor_exists():
    assert callable(pascal_enumerated_type.__init__)


def test_pascal_enumerated_type_constructor_args():
    sig = inspect.signature(pascal_enumerated_type.__init__)
    params = list(sig.parameters.keys())



def test_pascal_field_list_is_not_abstract():
    assert not inspect.isabstract(pascal_field_list)


def test_pascal_field_list_constructor_exists():
    assert callable(pascal_field_list.__init__)


def test_pascal_field_list_constructor_args():
    sig = inspect.signature(pascal_field_list.__init__)
    params = list(sig.parameters.keys())



def test_pascal_index_type_is_not_abstract():
    assert not inspect.isabstract(pascal_index_type)


def test_pascal_index_type_constructor_exists():
    assert callable(pascal_index_type.__init__)


def test_pascal_index_type_constructor_args():
    sig = inspect.signature(pascal_index_type.__init__)
    params = list(sig.parameters.keys())



def test_pascal_file_type_is_not_abstract():
    assert not inspect.isabstract(pascal_file_type)


def test_pascal_file_type_constructor_exists():
    assert callable(pascal_file_type.__init__)


def test_pascal_file_type_constructor_args():
    sig = inspect.signature(pascal_file_type.__init__)
    params = list(sig.parameters.keys())



def test_pascal_set_type_is_not_abstract():
    assert not inspect.isabstract(pascal_set_type)


def test_pascal_set_type_constructor_exists():
    assert callable(pascal_set_type.__init__)


def test_pascal_set_type_constructor_args():
    sig = inspect.signature(pascal_set_type.__init__)
    params = list(sig.parameters.keys())



def test_pascal_record_type_is_not_abstract():
    assert not inspect.isabstract(pascal_record_type)


def test_pascal_record_type_constructor_exists():
    assert callable(pascal_record_type.__init__)


def test_pascal_record_type_constructor_args():
    sig = inspect.signature(pascal_record_type.__init__)
    params = list(sig.parameters.keys())
    assert "endKeyword" in params, "Missing parameter 'endKeyword'"
    assert "recordKeyword" in params, "Missing parameter 'recordKeyword'"

def test_pascal_record_type_has_endKeyword():
    assert hasattr(pascal_record_type, "endKeyword")
    descriptor = None
    for klass in pascal_record_type.__mro__:
        if "endKeyword" in klass.__dict__:
            descriptor = klass.__dict__["endKeyword"]
            break
    assert isinstance(descriptor, property)

def test_pascal_record_type_has_recordKeyword():
    assert hasattr(pascal_record_type, "recordKeyword")
    descriptor = None
    for klass in pascal_record_type.__mro__:
        if "recordKeyword" in klass.__dict__:
            descriptor = klass.__dict__["recordKeyword"]
            break
    assert isinstance(descriptor, property)



def test_pascal_dynamic_array_type_is_not_abstract():
    assert not inspect.isabstract(pascal_dynamic_array_type)


def test_pascal_dynamic_array_type_constructor_exists():
    assert callable(pascal_dynamic_array_type.__init__)


def test_pascal_dynamic_array_type_constructor_args():
    sig = inspect.signature(pascal_dynamic_array_type.__init__)
    params = list(sig.parameters.keys())



def test_pascal_array_type_is_not_abstract():
    assert not inspect.isabstract(pascal_array_type)


def test_pascal_array_type_constructor_exists():
    assert callable(pascal_array_type.__init__)


def test_pascal_array_type_constructor_args():
    sig = inspect.signature(pascal_array_type.__init__)
    params = list(sig.parameters.keys())



def test_pascal_unpacked_structured_type_is_not_abstract():
    assert not inspect.isabstract(pascal_unpacked_structured_type)


def test_pascal_unpacked_structured_type_constructor_exists():
    assert callable(pascal_unpacked_structured_type.__init__)


def test_pascal_unpacked_structured_type_constructor_args():
    sig = inspect.signature(pascal_unpacked_structured_type.__init__)
    params = list(sig.parameters.keys())



def test_pascal_constant_is_not_abstract():
    assert not inspect.isabstract(pascal_constant)


def test_pascal_constant_constructor_exists():
    assert callable(pascal_constant.__init__)


def test_pascal_constant_constructor_args():
    sig = inspect.signature(pascal_constant.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"
    assert "name" in params, "Missing parameter 'name'"
    assert "nil" in params, "Missing parameter 'nil'"
    assert "opterator" in params, "Missing parameter 'opterator'"
    assert "boolLiteral" in params, "Missing parameter 'boolLiteral'"

def test_pascal_constant_has_string():
    assert hasattr(pascal_constant, "string")
    descriptor = None
    for klass in pascal_constant.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)

def test_pascal_constant_has_name():
    assert hasattr(pascal_constant, "name")
    descriptor = None
    for klass in pascal_constant.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_pascal_constant_has_nil():
    assert hasattr(pascal_constant, "nil")
    descriptor = None
    for klass in pascal_constant.__mro__:
        if "nil" in klass.__dict__:
            descriptor = klass.__dict__["nil"]
            break
    assert isinstance(descriptor, property)

def test_pascal_constant_has_opterator():
    assert hasattr(pascal_constant, "opterator")
    descriptor = None
    for klass in pascal_constant.__mro__:
        if "opterator" in klass.__dict__:
            descriptor = klass.__dict__["opterator"]
            break
    assert isinstance(descriptor, property)

def test_pascal_constant_has_boolLiteral():
    assert hasattr(pascal_constant, "boolLiteral")
    descriptor = None
    for klass in pascal_constant.__mro__:
        if "boolLiteral" in klass.__dict__:
            descriptor = klass.__dict__["boolLiteral"]
            break
    assert isinstance(descriptor, property)



def test_pascal_subrange_type_is_not_abstract():
    assert not inspect.isabstract(pascal_subrange_type)


def test_pascal_subrange_type_constructor_exists():
    assert callable(pascal_subrange_type.__init__)


def test_pascal_subrange_type_constructor_args():
    sig = inspect.signature(pascal_subrange_type.__init__)
    params = list(sig.parameters.keys())
    assert "subrange" in params, "Missing parameter 'subrange'"

def test_pascal_subrange_type_has_subrange():
    assert hasattr(pascal_subrange_type, "subrange")
    descriptor = None
    for klass in pascal_subrange_type.__mro__:
        if "subrange" in klass.__dict__:
            descriptor = klass.__dict__["subrange"]
            break
    assert isinstance(descriptor, property)



def test_pascal_pointer_type_is_not_abstract():
    assert not inspect.isabstract(pascal_pointer_type)


def test_pascal_pointer_type_constructor_exists():
    assert callable(pascal_pointer_type.__init__)


def test_pascal_pointer_type_constructor_args():
    sig = inspect.signature(pascal_pointer_type.__init__)
    params = list(sig.parameters.keys())



def test_pascal_structured_type_is_not_abstract():
    assert not inspect.isabstract(pascal_structured_type)


def test_pascal_structured_type_constructor_exists():
    assert callable(pascal_structured_type.__init__)


def test_pascal_structured_type_constructor_args():
    sig = inspect.signature(pascal_structured_type.__init__)
    params = list(sig.parameters.keys())
    assert "packed" in params, "Missing parameter 'packed'"

def test_pascal_structured_type_has_packed():
    assert hasattr(pascal_structured_type, "packed")
    descriptor = None
    for klass in pascal_structured_type.__mro__:
        if "packed" in klass.__dict__:
            descriptor = klass.__dict__["packed"]
            break
    assert isinstance(descriptor, property)



def test_pascal_simple_type_is_not_abstract():
    assert not inspect.isabstract(pascal_simple_type)


def test_pascal_simple_type_constructor_exists():
    assert callable(pascal_simple_type.__init__)


def test_pascal_simple_type_constructor_args():
    sig = inspect.signature(pascal_simple_type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pascal_simple_type_has_name():
    assert hasattr(pascal_simple_type, "name")
    descriptor = None
    for klass in pascal_simple_type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pascal_type_is_not_abstract():
    assert not inspect.isabstract(pascal_type)


def test_pascal_type_constructor_exists():
    assert callable(pascal_type.__init__)


def test_pascal_type_constructor_args():
    sig = inspect.signature(pascal_type.__init__)
    params = list(sig.parameters.keys())



def test_pascal_type_definition_is_not_abstract():
    assert not inspect.isabstract(pascal_type_definition)


def test_pascal_type_definition_constructor_exists():
    assert callable(pascal_type_definition.__init__)


def test_pascal_type_definition_constructor_args():
    sig = inspect.signature(pascal_type_definition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pascal_type_definition_has_name():
    assert hasattr(pascal_type_definition, "name")
    descriptor = None
    for klass in pascal_type_definition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pascal_constant_definition_is_not_abstract():
    assert not inspect.isabstract(pascal_constant_definition)


def test_pascal_constant_definition_constructor_exists():
    assert callable(pascal_constant_definition.__init__)


def test_pascal_constant_definition_constructor_args():
    sig = inspect.signature(pascal_constant_definition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pascal_constant_definition_has_name():
    assert hasattr(pascal_constant_definition, "name")
    descriptor = None
    for klass in pascal_constant_definition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pascal_for_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_for_statement)


def test_pascal_for_statement_constructor_exists():
    assert callable(pascal_for_statement.__init__)


def test_pascal_for_statement_constructor_args():
    sig = inspect.signature(pascal_for_statement.__init__)
    params = list(sig.parameters.keys())



def test_pascal_repeat_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_repeat_statement)


def test_pascal_repeat_statement_constructor_exists():
    assert callable(pascal_repeat_statement.__init__)


def test_pascal_repeat_statement_constructor_args():
    sig = inspect.signature(pascal_repeat_statement.__init__)
    params = list(sig.parameters.keys())



def test_pascal_while_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_while_statement)


def test_pascal_while_statement_constructor_exists():
    assert callable(pascal_while_statement.__init__)


def test_pascal_while_statement_constructor_args():
    sig = inspect.signature(pascal_while_statement.__init__)
    params = list(sig.parameters.keys())



def test_pascal_case_label_list_is_not_abstract():
    assert not inspect.isabstract(pascal_case_label_list)


def test_pascal_case_label_list_constructor_exists():
    assert callable(pascal_case_label_list.__init__)


def test_pascal_case_label_list_constructor_args():
    sig = inspect.signature(pascal_case_label_list.__init__)
    params = list(sig.parameters.keys())



def test_pascal_case_limb_is_not_abstract():
    assert not inspect.isabstract(pascal_case_limb)


def test_pascal_case_limb_constructor_exists():
    assert callable(pascal_case_limb.__init__)


def test_pascal_case_limb_constructor_args():
    sig = inspect.signature(pascal_case_limb.__init__)
    params = list(sig.parameters.keys())



def test_pascal_case_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_case_statement)


def test_pascal_case_statement_constructor_exists():
    assert callable(pascal_case_statement.__init__)


def test_pascal_case_statement_constructor_args():
    sig = inspect.signature(pascal_case_statement.__init__)
    params = list(sig.parameters.keys())



def test_pascal_if_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_if_statement)


def test_pascal_if_statement_constructor_exists():
    assert callable(pascal_if_statement.__init__)


def test_pascal_if_statement_constructor_args():
    sig = inspect.signature(pascal_if_statement.__init__)
    params = list(sig.parameters.keys())



def test_pascal_factor_is_not_abstract():
    assert not inspect.isabstract(pascal_factor)


def test_pascal_factor_constructor_exists():
    assert callable(pascal_factor.__init__)


def test_pascal_factor_constructor_args():
    sig = inspect.signature(pascal_factor.__init__)
    params = list(sig.parameters.keys())
    assert "nil" in params, "Missing parameter 'nil'"
    assert "boolean" in params, "Missing parameter 'boolean'"
    assert "string" in params, "Missing parameter 'string'"

def test_pascal_factor_has_nil():
    assert hasattr(pascal_factor, "nil")
    descriptor = None
    for klass in pascal_factor.__mro__:
        if "nil" in klass.__dict__:
            descriptor = klass.__dict__["nil"]
            break
    assert isinstance(descriptor, property)

def test_pascal_factor_has_boolean():
    assert hasattr(pascal_factor, "boolean")
    descriptor = None
    for klass in pascal_factor.__mro__:
        if "boolean" in klass.__dict__:
            descriptor = klass.__dict__["boolean"]
            break
    assert isinstance(descriptor, property)

def test_pascal_factor_has_string():
    assert hasattr(pascal_factor, "string")
    descriptor = None
    for klass in pascal_factor.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)



def test_pascal_term_is_not_abstract():
    assert not inspect.isabstract(pascal_term)


def test_pascal_term_constructor_exists():
    assert callable(pascal_term.__init__)


def test_pascal_term_constructor_args():
    sig = inspect.signature(pascal_term.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_pascal_term_has_operators():
    assert hasattr(pascal_term, "operators")
    descriptor = None
    for klass in pascal_term.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)



def test_pascal_with_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_with_statement)


def test_pascal_with_statement_constructor_exists():
    assert callable(pascal_with_statement.__init__)


def test_pascal_with_statement_constructor_args():
    sig = inspect.signature(pascal_with_statement.__init__)
    params = list(sig.parameters.keys())



def test_pascal_conditional_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_conditional_statement)


def test_pascal_conditional_statement_constructor_exists():
    assert callable(pascal_conditional_statement.__init__)


def test_pascal_conditional_statement_constructor_args():
    sig = inspect.signature(pascal_conditional_statement.__init__)
    params = list(sig.parameters.keys())



def test_pascal_repetitive_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_repetitive_statement)


def test_pascal_repetitive_statement_constructor_exists():
    assert callable(pascal_repetitive_statement.__init__)


def test_pascal_repetitive_statement_constructor_args():
    sig = inspect.signature(pascal_repetitive_statement.__init__)
    params = list(sig.parameters.keys())



def test_pascal_compound_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_compound_statement)


def test_pascal_compound_statement_constructor_exists():
    assert callable(pascal_compound_statement.__init__)


def test_pascal_compound_statement_constructor_args():
    sig = inspect.signature(pascal_compound_statement.__init__)
    params = list(sig.parameters.keys())



def test_pascal_any_number_is_not_abstract():
    assert not inspect.isabstract(pascal_any_number)


def test_pascal_any_number_constructor_exists():
    assert callable(pascal_any_number.__init__)


def test_pascal_any_number_constructor_args():
    sig = inspect.signature(pascal_any_number.__init__)
    params = list(sig.parameters.keys())
    assert "real" in params, "Missing parameter 'real'"
    assert "integer" in params, "Missing parameter 'integer'"

def test_pascal_any_number_has_real():
    assert hasattr(pascal_any_number, "real")
    descriptor = None
    for klass in pascal_any_number.__mro__:
        if "real" in klass.__dict__:
            descriptor = klass.__dict__["real"]
            break
    assert isinstance(descriptor, property)

def test_pascal_any_number_has_integer():
    assert hasattr(pascal_any_number, "integer")
    descriptor = None
    for klass in pascal_any_number.__mro__:
        if "integer" in klass.__dict__:
            descriptor = klass.__dict__["integer"]
            break
    assert isinstance(descriptor, property)



def test_pascal_set_is_not_abstract():
    assert not inspect.isabstract(pascal_set)


def test_pascal_set_constructor_exists():
    assert callable(pascal_set.__init__)


def test_pascal_set_constructor_args():
    sig = inspect.signature(pascal_set.__init__)
    params = list(sig.parameters.keys())
    assert "brackets" in params, "Missing parameter 'brackets'"

def test_pascal_set_has_brackets():
    assert hasattr(pascal_set, "brackets")
    descriptor = None
    for klass in pascal_set.__mro__:
        if "brackets" in klass.__dict__:
            descriptor = klass.__dict__["brackets"]
            break
    assert isinstance(descriptor, property)



def test_pascal_number_is_not_abstract():
    assert not inspect.isabstract(pascal_number)


def test_pascal_number_constructor_exists():
    assert callable(pascal_number.__init__)


def test_pascal_number_constructor_args():
    sig = inspect.signature(pascal_number.__init__)
    params = list(sig.parameters.keys())



def test_pascal_structured_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_structured_statement)


def test_pascal_structured_statement_constructor_exists():
    assert callable(pascal_structured_statement.__init__)


def test_pascal_structured_statement_constructor_args():
    sig = inspect.signature(pascal_structured_statement.__init__)
    params = list(sig.parameters.keys())



def test_pascal_simple_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_simple_statement)


def test_pascal_simple_statement_constructor_exists():
    assert callable(pascal_simple_statement.__init__)


def test_pascal_simple_statement_constructor_args():
    sig = inspect.signature(pascal_simple_statement.__init__)
    params = list(sig.parameters.keys())
    assert "function_noargs" in params, "Missing parameter 'function_noargs'"

def test_pascal_simple_statement_has_function_noargs():
    assert hasattr(pascal_simple_statement, "function_noargs")
    descriptor = None
    for klass in pascal_simple_statement.__mro__:
        if "function_noargs" in klass.__dict__:
            descriptor = klass.__dict__["function_noargs"]
            break
    assert isinstance(descriptor, property)



def test_pascal_eobject_is_not_abstract():
    assert not inspect.isabstract(pascal_EObject)


def test_pascal_eobject_constructor_exists():
    assert callable(pascal_EObject.__init__)


def test_pascal_eobject_constructor_args():
    sig = inspect.signature(pascal_EObject.__init__)
    params = list(sig.parameters.keys())



def test_pascal_simple_expression_is_not_abstract():
    assert not inspect.isabstract(pascal_simple_expression)


def test_pascal_simple_expression_constructor_exists():
    assert callable(pascal_simple_expression.__init__)


def test_pascal_simple_expression_constructor_args():
    sig = inspect.signature(pascal_simple_expression.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"
    assert "prefixOperator" in params, "Missing parameter 'prefixOperator'"

def test_pascal_simple_expression_has_operators():
    assert hasattr(pascal_simple_expression, "operators")
    descriptor = None
    for klass in pascal_simple_expression.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)

def test_pascal_simple_expression_has_prefixOperator():
    assert hasattr(pascal_simple_expression, "prefixOperator")
    descriptor = None
    for klass in pascal_simple_expression.__mro__:
        if "prefixOperator" in klass.__dict__:
            descriptor = klass.__dict__["prefixOperator"]
            break
    assert isinstance(descriptor, property)



def test_pascal_expression_list_is_not_abstract():
    assert not inspect.isabstract(pascal_expression_list)


def test_pascal_expression_list_constructor_exists():
    assert callable(pascal_expression_list.__init__)


def test_pascal_expression_list_constructor_args():
    sig = inspect.signature(pascal_expression_list.__init__)
    params = list(sig.parameters.keys())



def test_pascal_var__is_not_abstract():
    assert not inspect.isabstract(pascal_var_)


def test_pascal_var__constructor_exists():
    assert callable(pascal_var_.__init__)


def test_pascal_var__constructor_args():
    sig = inspect.signature(pascal_var_.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "accessor" in params, "Missing parameter 'accessor'"

def test_pascal_var__has_name():
    assert hasattr(pascal_var_, "name")
    descriptor = None
    for klass in pascal_var_.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_pascal_var__has_accessor():
    assert hasattr(pascal_var_, "accessor")
    descriptor = None
    for klass in pascal_var_.__mro__:
        if "accessor" in klass.__dict__:
            descriptor = klass.__dict__["accessor"]
            break
    assert isinstance(descriptor, property)



def test_pascal_expression_is_not_abstract():
    assert not inspect.isabstract(pascal_expression)


def test_pascal_expression_constructor_exists():
    assert callable(pascal_expression.__init__)


def test_pascal_expression_constructor_args():
    sig = inspect.signature(pascal_expression.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_pascal_expression_has_operators():
    assert hasattr(pascal_expression, "operators")
    descriptor = None
    for klass in pascal_expression.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)



def test_pascal_variable_is_not_abstract():
    assert not inspect.isabstract(pascal_variable)


def test_pascal_variable_constructor_exists():
    assert callable(pascal_variable.__init__)


def test_pascal_variable_constructor_args():
    sig = inspect.signature(pascal_variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pascal_variable_has_name():
    assert hasattr(pascal_variable, "name")
    descriptor = None
    for klass in pascal_variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pascal_goto_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_goto_statement)


def test_pascal_goto_statement_constructor_exists():
    assert callable(pascal_goto_statement.__init__)


def test_pascal_goto_statement_constructor_args():
    sig = inspect.signature(pascal_goto_statement.__init__)
    params = list(sig.parameters.keys())



def test_pascal_function_designator_is_not_abstract():
    assert not inspect.isabstract(pascal_function_designator)


def test_pascal_function_designator_constructor_exists():
    assert callable(pascal_function_designator.__init__)


def test_pascal_function_designator_constructor_args():
    sig = inspect.signature(pascal_function_designator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pascal_function_designator_has_name():
    assert hasattr(pascal_function_designator, "name")
    descriptor = None
    for klass in pascal_function_designator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pascal_assignment_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_assignment_statement)


def test_pascal_assignment_statement_constructor_exists():
    assert callable(pascal_assignment_statement.__init__)


def test_pascal_assignment_statement_constructor_args():
    sig = inspect.signature(pascal_assignment_statement.__init__)
    params = list(sig.parameters.keys())



def test_pascal_pascal_is_not_abstract():
    assert not inspect.isabstract(pascal_pascal)


def test_pascal_pascal_constructor_exists():
    assert callable(pascal_pascal.__init__)


def test_pascal_pascal_constructor_args():
    sig = inspect.signature(pascal_pascal.__init__)
    params = list(sig.parameters.keys())



def test_pascal_label_is_not_abstract():
    assert not inspect.isabstract(pascal_label)


def test_pascal_label_constructor_exists():
    assert callable(pascal_label.__init__)


def test_pascal_label_constructor_args():
    sig = inspect.signature(pascal_label.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"

def test_pascal_label_has_number():
    assert hasattr(pascal_label, "number")
    descriptor = None
    for klass in pascal_label.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_pascal_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_statement)


def test_pascal_statement_constructor_exists():
    assert callable(pascal_statement.__init__)


def test_pascal_statement_constructor_args():
    sig = inspect.signature(pascal_statement.__init__)
    params = list(sig.parameters.keys())



def test_pascal_statement_sequence_is_not_abstract():
    assert not inspect.isabstract(pascal_statement_sequence)


def test_pascal_statement_sequence_constructor_exists():
    assert callable(pascal_statement_sequence.__init__)


def test_pascal_statement_sequence_constructor_args():
    sig = inspect.signature(pascal_statement_sequence.__init__)
    params = list(sig.parameters.keys())



def test_pascal_statement_part_is_not_abstract():
    assert not inspect.isabstract(pascal_statement_part)


def test_pascal_statement_part_constructor_exists():
    assert callable(pascal_statement_part.__init__)


def test_pascal_statement_part_constructor_args():
    sig = inspect.signature(pascal_statement_part.__init__)
    params = list(sig.parameters.keys())



def test_pascal_procedure_and_function_declaration_part_is_not_abstract():
    assert not inspect.isabstract(pascal_procedure_and_function_declaration_part)


def test_pascal_procedure_and_function_declaration_part_constructor_exists():
    assert callable(pascal_procedure_and_function_declaration_part.__init__)


def test_pascal_procedure_and_function_declaration_part_constructor_args():
    sig = inspect.signature(pascal_procedure_and_function_declaration_part.__init__)
    params = list(sig.parameters.keys())



def test_pascal_variable_declaration_part_is_not_abstract():
    assert not inspect.isabstract(pascal_variable_declaration_part)


def test_pascal_variable_declaration_part_constructor_exists():
    assert callable(pascal_variable_declaration_part.__init__)


def test_pascal_variable_declaration_part_constructor_args():
    sig = inspect.signature(pascal_variable_declaration_part.__init__)
    params = list(sig.parameters.keys())



def test_pascal_type_definition_part_is_not_abstract():
    assert not inspect.isabstract(pascal_type_definition_part)


def test_pascal_type_definition_part_constructor_exists():
    assert callable(pascal_type_definition_part.__init__)


def test_pascal_type_definition_part_constructor_args():
    sig = inspect.signature(pascal_type_definition_part.__init__)
    params = list(sig.parameters.keys())



def test_pascal_constant_definition_part_is_not_abstract():
    assert not inspect.isabstract(pascal_constant_definition_part)


def test_pascal_constant_definition_part_constructor_exists():
    assert callable(pascal_constant_definition_part.__init__)


def test_pascal_constant_definition_part_constructor_args():
    sig = inspect.signature(pascal_constant_definition_part.__init__)
    params = list(sig.parameters.keys())



def test_pascal_label_declaration_part_is_not_abstract():
    assert not inspect.isabstract(pascal_label_declaration_part)


def test_pascal_label_declaration_part_constructor_exists():
    assert callable(pascal_label_declaration_part.__init__)


def test_pascal_label_declaration_part_constructor_args():
    sig = inspect.signature(pascal_label_declaration_part.__init__)
    params = list(sig.parameters.keys())



def test_pascal_identifier_list_is_not_abstract():
    assert not inspect.isabstract(pascal_identifier_list)


def test_pascal_identifier_list_constructor_exists():
    assert callable(pascal_identifier_list.__init__)


def test_pascal_identifier_list_constructor_args():
    sig = inspect.signature(pascal_identifier_list.__init__)
    params = list(sig.parameters.keys())
    assert "names" in params, "Missing parameter 'names'"

def test_pascal_identifier_list_has_names():
    assert hasattr(pascal_identifier_list, "names")
    descriptor = None
    for klass in pascal_identifier_list.__mro__:
        if "names" in klass.__dict__:
            descriptor = klass.__dict__["names"]
            break
    assert isinstance(descriptor, property)



def test_pascal_block_is_not_abstract():
    assert not inspect.isabstract(pascal_block)


def test_pascal_block_constructor_exists():
    assert callable(pascal_block.__init__)


def test_pascal_block_constructor_args():
    sig = inspect.signature(pascal_block.__init__)
    params = list(sig.parameters.keys())



def test_pascal_program_heading_block_is_not_abstract():
    assert not inspect.isabstract(pascal_program_heading_block)


def test_pascal_program_heading_block_constructor_exists():
    assert callable(pascal_program_heading_block.__init__)


def test_pascal_program_heading_block_constructor_args():
    sig = inspect.signature(pascal_program_heading_block.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pascal_program_heading_block_has_name():
    assert hasattr(pascal_program_heading_block, "name")
    descriptor = None
    for klass in pascal_program_heading_block.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pascal_program_is_not_abstract():
    assert not inspect.isabstract(pascal_program)


def test_pascal_program_constructor_exists():
    assert callable(pascal_program.__init__)


def test_pascal_program_constructor_args():
    sig = inspect.signature(pascal_program.__init__)
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
abstraction_declaration_strategy = st.builds(
    abstraction_declaration,
)
pascal_bound_specification_strategy = st.builds(
    pascal_bound_specification,
    name=
        safe_text,
    final=
        safe_text,
    initial=
        safe_text
)
pascal_unpacked_conformant_array_schema_strategy = st.builds(
    pascal_unpacked_conformant_array_schema,
)
pascal_packed_conformant_array_schema_strategy = st.builds(
    pascal_packed_conformant_array_schema,
    name=
        safe_text
)
pascal_conformant_array_schema_strategy = st.builds(
    pascal_conformant_array_schema,
)
pascal_parameter_type_strategy = st.builds(
    pascal_parameter_type,
    name=
        safe_text
)
pascal_variable_parameter_section_strategy = st.builds(
    pascal_variable_parameter_section,
)
pascal_value_parameter_section_strategy = st.builds(
    pascal_value_parameter_section,
)
pascal_formal_parameter_section_strategy = st.builds(
    pascal_formal_parameter_section,
)
pascal_formal_parameter_list_strategy = st.builds(
    pascal_formal_parameter_list,
)
pascal_record_section_strategy = st.builds(
    pascal_record_section,
)
pascal_variant_part_strategy = st.builds(
    pascal_variant_part,
    name=
        safe_text
)
pascal_fixed_part_strategy = st.builds(
    pascal_fixed_part,
)
pascal_abstraction_declaration_strategy = st.builds(
    pascal_abstraction_declaration,
    forward=
        st.booleans()
)
pascal_abstraction_heading_strategy = st.builds(
    pascal_abstraction_heading,
    returnType=
        safe_text,
    name=
        safe_text
)
pascal_variant_strategy = st.builds(
    pascal_variant,
)
pascal_tag_field_strategy = st.builds(
    pascal_tag_field,
    name=
        safe_text
)
pascal_variable_section_strategy = st.builds(
    pascal_variable_section,
)
pascal_variable_identifier_list_strategy = st.builds(
    pascal_variable_identifier_list,
    names=
        safe_text
)
pascal_enumerated_type_strategy = st.builds(
    pascal_enumerated_type,
)
pascal_field_list_strategy = st.builds(
    pascal_field_list,
)
pascal_index_type_strategy = st.builds(
    pascal_index_type,
)
pascal_file_type_strategy = st.builds(
    pascal_file_type,
)
pascal_set_type_strategy = st.builds(
    pascal_set_type,
)
pascal_record_type_strategy = st.builds(
    pascal_record_type,
    endKeyword=
        safe_text,
    recordKeyword=
        safe_text
)
pascal_dynamic_array_type_strategy = st.builds(
    pascal_dynamic_array_type,
)
pascal_array_type_strategy = st.builds(
    pascal_array_type,
)
pascal_unpacked_structured_type_strategy = st.builds(
    pascal_unpacked_structured_type,
)
pascal_constant_strategy = st.builds(
    pascal_constant,
    string=
        safe_text,
    name=
        safe_text,
    nil=
        safe_text,
    opterator=
        safe_text,
    boolLiteral=
        safe_text
)
pascal_subrange_type_strategy = st.builds(
    pascal_subrange_type,
    subrange=
        safe_text
)
pascal_pointer_type_strategy = st.builds(
    pascal_pointer_type,
)
pascal_structured_type_strategy = st.builds(
    pascal_structured_type,
    packed=
        st.booleans()
)
pascal_simple_type_strategy = st.builds(
    pascal_simple_type,
    name=
        safe_text
)
pascal_type_strategy = st.builds(
    pascal_type,
)
pascal_type_definition_strategy = st.builds(
    pascal_type_definition,
    name=
        safe_text
)
pascal_constant_definition_strategy = st.builds(
    pascal_constant_definition,
    name=
        safe_text
)
pascal_for_statement_strategy = st.builds(
    pascal_for_statement,
)
pascal_repeat_statement_strategy = st.builds(
    pascal_repeat_statement,
)
pascal_while_statement_strategy = st.builds(
    pascal_while_statement,
)
pascal_case_label_list_strategy = st.builds(
    pascal_case_label_list,
)
pascal_case_limb_strategy = st.builds(
    pascal_case_limb,
)
pascal_case_statement_strategy = st.builds(
    pascal_case_statement,
)
pascal_if_statement_strategy = st.builds(
    pascal_if_statement,
)
pascal_factor_strategy = st.builds(
    pascal_factor,
    nil=
        st.booleans(),
    boolean=
        safe_text,
    string=
        safe_text
)
pascal_term_strategy = st.builds(
    pascal_term,
    operators=
        safe_text
)
pascal_with_statement_strategy = st.builds(
    pascal_with_statement,
)
pascal_conditional_statement_strategy = st.builds(
    pascal_conditional_statement,
)
pascal_repetitive_statement_strategy = st.builds(
    pascal_repetitive_statement,
)
pascal_compound_statement_strategy = st.builds(
    pascal_compound_statement,
)
pascal_any_number_strategy = st.builds(
    pascal_any_number,
    real=
        safe_text,
    integer=
        safe_text
)
pascal_set_strategy = st.builds(
    pascal_set,
    brackets=
        safe_text
)
pascal_number_strategy = st.builds(
    pascal_number,
)
pascal_structured_statement_strategy = st.builds(
    pascal_structured_statement,
)
pascal_simple_statement_strategy = st.builds(
    pascal_simple_statement,
    function_noargs=
        safe_text
)
pascal_EObject_strategy = st.builds(
    pascal_EObject,
)
pascal_simple_expression_strategy = st.builds(
    pascal_simple_expression,
    operators=
        safe_text,
    prefixOperator=
        safe_text
)
pascal_expression_list_strategy = st.builds(
    pascal_expression_list,
)
pascal_var__strategy = st.builds(
    pascal_var_,
    name=
        safe_text,
    accessor=
        st.booleans()
)
pascal_expression_strategy = st.builds(
    pascal_expression,
    operators=
        safe_text
)
pascal_variable_strategy = st.builds(
    pascal_variable,
    name=
        safe_text
)
pascal_goto_statement_strategy = st.builds(
    pascal_goto_statement,
)
pascal_function_designator_strategy = st.builds(
    pascal_function_designator,
    name=
        safe_text
)
pascal_assignment_statement_strategy = st.builds(
    pascal_assignment_statement,
)
pascal_pascal_strategy = st.builds(
    pascal_pascal,
)
pascal_label_strategy = st.builds(
    pascal_label,
    number=
        safe_text
)
pascal_statement_strategy = st.builds(
    pascal_statement,
)
pascal_statement_sequence_strategy = st.builds(
    pascal_statement_sequence,
)
pascal_statement_part_strategy = st.builds(
    pascal_statement_part,
)
pascal_procedure_and_function_declaration_part_strategy = st.builds(
    pascal_procedure_and_function_declaration_part,
)
pascal_variable_declaration_part_strategy = st.builds(
    pascal_variable_declaration_part,
)
pascal_type_definition_part_strategy = st.builds(
    pascal_type_definition_part,
)
pascal_constant_definition_part_strategy = st.builds(
    pascal_constant_definition_part,
)
pascal_label_declaration_part_strategy = st.builds(
    pascal_label_declaration_part,
)
pascal_identifier_list_strategy = st.builds(
    pascal_identifier_list,
    names=
        safe_text
)
pascal_block_strategy = st.builds(
    pascal_block,
)
pascal_program_heading_block_strategy = st.builds(
    pascal_program_heading_block,
    name=
        safe_text
)
pascal_program_strategy = st.builds(
    pascal_program,
)

@given(instance=abstraction_declaration_strategy)
@settings(max_examples=50)
def test_abstraction_declaration_instantiation(instance):
    assert isinstance(instance, abstraction_declaration)

@given(instance=pascal_bound_specification_strategy)
@settings(max_examples=50)
def test_pascal_bound_specification_instantiation(instance):
    assert isinstance(instance, pascal_bound_specification)



@given(instance=pascal_bound_specification_strategy)
def test_pascal_bound_specification_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=pascal_bound_specification_strategy)
def test_pascal_bound_specification_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original



@given(instance=pascal_bound_specification_strategy)
def test_pascal_bound_specification_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original

@given(instance=pascal_unpacked_conformant_array_schema_strategy)
@settings(max_examples=50)
def test_pascal_unpacked_conformant_array_schema_instantiation(instance):
    assert isinstance(instance, pascal_unpacked_conformant_array_schema)

@given(instance=pascal_packed_conformant_array_schema_strategy)
@settings(max_examples=50)
def test_pascal_packed_conformant_array_schema_instantiation(instance):
    assert isinstance(instance, pascal_packed_conformant_array_schema)



@given(instance=pascal_packed_conformant_array_schema_strategy)
def test_pascal_packed_conformant_array_schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pascal_conformant_array_schema_strategy)
@settings(max_examples=50)
def test_pascal_conformant_array_schema_instantiation(instance):
    assert isinstance(instance, pascal_conformant_array_schema)

@given(instance=pascal_parameter_type_strategy)
@settings(max_examples=50)
def test_pascal_parameter_type_instantiation(instance):
    assert isinstance(instance, pascal_parameter_type)



@given(instance=pascal_parameter_type_strategy)
def test_pascal_parameter_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pascal_variable_parameter_section_strategy)
@settings(max_examples=50)
def test_pascal_variable_parameter_section_instantiation(instance):
    assert isinstance(instance, pascal_variable_parameter_section)

@given(instance=pascal_value_parameter_section_strategy)
@settings(max_examples=50)
def test_pascal_value_parameter_section_instantiation(instance):
    assert isinstance(instance, pascal_value_parameter_section)

@given(instance=pascal_formal_parameter_section_strategy)
@settings(max_examples=50)
def test_pascal_formal_parameter_section_instantiation(instance):
    assert isinstance(instance, pascal_formal_parameter_section)

@given(instance=pascal_formal_parameter_list_strategy)
@settings(max_examples=50)
def test_pascal_formal_parameter_list_instantiation(instance):
    assert isinstance(instance, pascal_formal_parameter_list)

@given(instance=pascal_record_section_strategy)
@settings(max_examples=50)
def test_pascal_record_section_instantiation(instance):
    assert isinstance(instance, pascal_record_section)

@given(instance=pascal_variant_part_strategy)
@settings(max_examples=50)
def test_pascal_variant_part_instantiation(instance):
    assert isinstance(instance, pascal_variant_part)



@given(instance=pascal_variant_part_strategy)
def test_pascal_variant_part_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pascal_fixed_part_strategy)
@settings(max_examples=50)
def test_pascal_fixed_part_instantiation(instance):
    assert isinstance(instance, pascal_fixed_part)

@given(instance=pascal_abstraction_declaration_strategy)
@settings(max_examples=50)
def test_pascal_abstraction_declaration_instantiation(instance):
    assert isinstance(instance, pascal_abstraction_declaration)



@given(instance=pascal_abstraction_declaration_strategy)
def test_pascal_abstraction_declaration_forward_setter(instance):
    original = instance.forward
    instance.forward = original
    assert instance.forward == original

@given(instance=pascal_abstraction_heading_strategy)
@settings(max_examples=50)
def test_pascal_abstraction_heading_instantiation(instance):
    assert isinstance(instance, pascal_abstraction_heading)



@given(instance=pascal_abstraction_heading_strategy)
def test_pascal_abstraction_heading_returnType_setter(instance):
    original = instance.returnType
    instance.returnType = original
    assert instance.returnType == original



@given(instance=pascal_abstraction_heading_strategy)
def test_pascal_abstraction_heading_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pascal_variant_strategy)
@settings(max_examples=50)
def test_pascal_variant_instantiation(instance):
    assert isinstance(instance, pascal_variant)

@given(instance=pascal_tag_field_strategy)
@settings(max_examples=50)
def test_pascal_tag_field_instantiation(instance):
    assert isinstance(instance, pascal_tag_field)



@given(instance=pascal_tag_field_strategy)
def test_pascal_tag_field_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pascal_variable_section_strategy)
@settings(max_examples=50)
def test_pascal_variable_section_instantiation(instance):
    assert isinstance(instance, pascal_variable_section)

@given(instance=pascal_variable_identifier_list_strategy)
@settings(max_examples=50)
def test_pascal_variable_identifier_list_instantiation(instance):
    assert isinstance(instance, pascal_variable_identifier_list)



@given(instance=pascal_variable_identifier_list_strategy)
def test_pascal_variable_identifier_list_names_setter(instance):
    original = instance.names
    instance.names = original
    assert instance.names == original

@given(instance=pascal_enumerated_type_strategy)
@settings(max_examples=50)
def test_pascal_enumerated_type_instantiation(instance):
    assert isinstance(instance, pascal_enumerated_type)

@given(instance=pascal_field_list_strategy)
@settings(max_examples=50)
def test_pascal_field_list_instantiation(instance):
    assert isinstance(instance, pascal_field_list)

@given(instance=pascal_index_type_strategy)
@settings(max_examples=50)
def test_pascal_index_type_instantiation(instance):
    assert isinstance(instance, pascal_index_type)

@given(instance=pascal_file_type_strategy)
@settings(max_examples=50)
def test_pascal_file_type_instantiation(instance):
    assert isinstance(instance, pascal_file_type)

@given(instance=pascal_set_type_strategy)
@settings(max_examples=50)
def test_pascal_set_type_instantiation(instance):
    assert isinstance(instance, pascal_set_type)

@given(instance=pascal_record_type_strategy)
@settings(max_examples=50)
def test_pascal_record_type_instantiation(instance):
    assert isinstance(instance, pascal_record_type)



@given(instance=pascal_record_type_strategy)
def test_pascal_record_type_endKeyword_setter(instance):
    original = instance.endKeyword
    instance.endKeyword = original
    assert instance.endKeyword == original



@given(instance=pascal_record_type_strategy)
def test_pascal_record_type_recordKeyword_setter(instance):
    original = instance.recordKeyword
    instance.recordKeyword = original
    assert instance.recordKeyword == original

@given(instance=pascal_dynamic_array_type_strategy)
@settings(max_examples=50)
def test_pascal_dynamic_array_type_instantiation(instance):
    assert isinstance(instance, pascal_dynamic_array_type)

@given(instance=pascal_array_type_strategy)
@settings(max_examples=50)
def test_pascal_array_type_instantiation(instance):
    assert isinstance(instance, pascal_array_type)

@given(instance=pascal_unpacked_structured_type_strategy)
@settings(max_examples=50)
def test_pascal_unpacked_structured_type_instantiation(instance):
    assert isinstance(instance, pascal_unpacked_structured_type)

@given(instance=pascal_constant_strategy)
@settings(max_examples=50)
def test_pascal_constant_instantiation(instance):
    assert isinstance(instance, pascal_constant)



@given(instance=pascal_constant_strategy)
def test_pascal_constant_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original



@given(instance=pascal_constant_strategy)
def test_pascal_constant_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=pascal_constant_strategy)
def test_pascal_constant_nil_setter(instance):
    original = instance.nil
    instance.nil = original
    assert instance.nil == original



@given(instance=pascal_constant_strategy)
def test_pascal_constant_opterator_setter(instance):
    original = instance.opterator
    instance.opterator = original
    assert instance.opterator == original



@given(instance=pascal_constant_strategy)
def test_pascal_constant_boolLiteral_setter(instance):
    original = instance.boolLiteral
    instance.boolLiteral = original
    assert instance.boolLiteral == original

@given(instance=pascal_subrange_type_strategy)
@settings(max_examples=50)
def test_pascal_subrange_type_instantiation(instance):
    assert isinstance(instance, pascal_subrange_type)



@given(instance=pascal_subrange_type_strategy)
def test_pascal_subrange_type_subrange_setter(instance):
    original = instance.subrange
    instance.subrange = original
    assert instance.subrange == original

@given(instance=pascal_pointer_type_strategy)
@settings(max_examples=50)
def test_pascal_pointer_type_instantiation(instance):
    assert isinstance(instance, pascal_pointer_type)

@given(instance=pascal_structured_type_strategy)
@settings(max_examples=50)
def test_pascal_structured_type_instantiation(instance):
    assert isinstance(instance, pascal_structured_type)



@given(instance=pascal_structured_type_strategy)
def test_pascal_structured_type_packed_setter(instance):
    original = instance.packed
    instance.packed = original
    assert instance.packed == original

@given(instance=pascal_simple_type_strategy)
@settings(max_examples=50)
def test_pascal_simple_type_instantiation(instance):
    assert isinstance(instance, pascal_simple_type)



@given(instance=pascal_simple_type_strategy)
def test_pascal_simple_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pascal_type_strategy)
@settings(max_examples=50)
def test_pascal_type_instantiation(instance):
    assert isinstance(instance, pascal_type)

@given(instance=pascal_type_definition_strategy)
@settings(max_examples=50)
def test_pascal_type_definition_instantiation(instance):
    assert isinstance(instance, pascal_type_definition)



@given(instance=pascal_type_definition_strategy)
def test_pascal_type_definition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pascal_constant_definition_strategy)
@settings(max_examples=50)
def test_pascal_constant_definition_instantiation(instance):
    assert isinstance(instance, pascal_constant_definition)



@given(instance=pascal_constant_definition_strategy)
def test_pascal_constant_definition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pascal_for_statement_strategy)
@settings(max_examples=50)
def test_pascal_for_statement_instantiation(instance):
    assert isinstance(instance, pascal_for_statement)

@given(instance=pascal_repeat_statement_strategy)
@settings(max_examples=50)
def test_pascal_repeat_statement_instantiation(instance):
    assert isinstance(instance, pascal_repeat_statement)

@given(instance=pascal_while_statement_strategy)
@settings(max_examples=50)
def test_pascal_while_statement_instantiation(instance):
    assert isinstance(instance, pascal_while_statement)

@given(instance=pascal_case_label_list_strategy)
@settings(max_examples=50)
def test_pascal_case_label_list_instantiation(instance):
    assert isinstance(instance, pascal_case_label_list)

@given(instance=pascal_case_limb_strategy)
@settings(max_examples=50)
def test_pascal_case_limb_instantiation(instance):
    assert isinstance(instance, pascal_case_limb)

@given(instance=pascal_case_statement_strategy)
@settings(max_examples=50)
def test_pascal_case_statement_instantiation(instance):
    assert isinstance(instance, pascal_case_statement)

@given(instance=pascal_if_statement_strategy)
@settings(max_examples=50)
def test_pascal_if_statement_instantiation(instance):
    assert isinstance(instance, pascal_if_statement)

@given(instance=pascal_factor_strategy)
@settings(max_examples=50)
def test_pascal_factor_instantiation(instance):
    assert isinstance(instance, pascal_factor)



@given(instance=pascal_factor_strategy)
def test_pascal_factor_nil_setter(instance):
    original = instance.nil
    instance.nil = original
    assert instance.nil == original



@given(instance=pascal_factor_strategy)
def test_pascal_factor_boolean_setter(instance):
    original = instance.boolean
    instance.boolean = original
    assert instance.boolean == original



@given(instance=pascal_factor_strategy)
def test_pascal_factor_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=pascal_term_strategy)
@settings(max_examples=50)
def test_pascal_term_instantiation(instance):
    assert isinstance(instance, pascal_term)



@given(instance=pascal_term_strategy)
def test_pascal_term_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=pascal_with_statement_strategy)
@settings(max_examples=50)
def test_pascal_with_statement_instantiation(instance):
    assert isinstance(instance, pascal_with_statement)

@given(instance=pascal_conditional_statement_strategy)
@settings(max_examples=50)
def test_pascal_conditional_statement_instantiation(instance):
    assert isinstance(instance, pascal_conditional_statement)

@given(instance=pascal_repetitive_statement_strategy)
@settings(max_examples=50)
def test_pascal_repetitive_statement_instantiation(instance):
    assert isinstance(instance, pascal_repetitive_statement)

@given(instance=pascal_compound_statement_strategy)
@settings(max_examples=50)
def test_pascal_compound_statement_instantiation(instance):
    assert isinstance(instance, pascal_compound_statement)

@given(instance=pascal_any_number_strategy)
@settings(max_examples=50)
def test_pascal_any_number_instantiation(instance):
    assert isinstance(instance, pascal_any_number)



@given(instance=pascal_any_number_strategy)
def test_pascal_any_number_real_setter(instance):
    original = instance.real
    instance.real = original
    assert instance.real == original



@given(instance=pascal_any_number_strategy)
def test_pascal_any_number_integer_setter(instance):
    original = instance.integer
    instance.integer = original
    assert instance.integer == original

@given(instance=pascal_set_strategy)
@settings(max_examples=50)
def test_pascal_set_instantiation(instance):
    assert isinstance(instance, pascal_set)



@given(instance=pascal_set_strategy)
def test_pascal_set_brackets_setter(instance):
    original = instance.brackets
    instance.brackets = original
    assert instance.brackets == original

@given(instance=pascal_number_strategy)
@settings(max_examples=50)
def test_pascal_number_instantiation(instance):
    assert isinstance(instance, pascal_number)

@given(instance=pascal_structured_statement_strategy)
@settings(max_examples=50)
def test_pascal_structured_statement_instantiation(instance):
    assert isinstance(instance, pascal_structured_statement)

@given(instance=pascal_simple_statement_strategy)
@settings(max_examples=50)
def test_pascal_simple_statement_instantiation(instance):
    assert isinstance(instance, pascal_simple_statement)



@given(instance=pascal_simple_statement_strategy)
def test_pascal_simple_statement_function_noargs_setter(instance):
    original = instance.function_noargs
    instance.function_noargs = original
    assert instance.function_noargs == original

@given(instance=pascal_EObject_strategy)
@settings(max_examples=50)
def test_pascal_eobject_instantiation(instance):
    assert isinstance(instance, pascal_EObject)

@given(instance=pascal_simple_expression_strategy)
@settings(max_examples=50)
def test_pascal_simple_expression_instantiation(instance):
    assert isinstance(instance, pascal_simple_expression)



@given(instance=pascal_simple_expression_strategy)
def test_pascal_simple_expression_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original



@given(instance=pascal_simple_expression_strategy)
def test_pascal_simple_expression_prefixOperator_setter(instance):
    original = instance.prefixOperator
    instance.prefixOperator = original
    assert instance.prefixOperator == original

@given(instance=pascal_expression_list_strategy)
@settings(max_examples=50)
def test_pascal_expression_list_instantiation(instance):
    assert isinstance(instance, pascal_expression_list)

@given(instance=pascal_var__strategy)
@settings(max_examples=50)
def test_pascal_var__instantiation(instance):
    assert isinstance(instance, pascal_var_)



@given(instance=pascal_var__strategy)
def test_pascal_var__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=pascal_var__strategy)
def test_pascal_var__accessor_setter(instance):
    original = instance.accessor
    instance.accessor = original
    assert instance.accessor == original

@given(instance=pascal_expression_strategy)
@settings(max_examples=50)
def test_pascal_expression_instantiation(instance):
    assert isinstance(instance, pascal_expression)



@given(instance=pascal_expression_strategy)
def test_pascal_expression_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=pascal_variable_strategy)
@settings(max_examples=50)
def test_pascal_variable_instantiation(instance):
    assert isinstance(instance, pascal_variable)



@given(instance=pascal_variable_strategy)
def test_pascal_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pascal_goto_statement_strategy)
@settings(max_examples=50)
def test_pascal_goto_statement_instantiation(instance):
    assert isinstance(instance, pascal_goto_statement)

@given(instance=pascal_function_designator_strategy)
@settings(max_examples=50)
def test_pascal_function_designator_instantiation(instance):
    assert isinstance(instance, pascal_function_designator)



@given(instance=pascal_function_designator_strategy)
def test_pascal_function_designator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pascal_assignment_statement_strategy)
@settings(max_examples=50)
def test_pascal_assignment_statement_instantiation(instance):
    assert isinstance(instance, pascal_assignment_statement)

@given(instance=pascal_pascal_strategy)
@settings(max_examples=50)
def test_pascal_pascal_instantiation(instance):
    assert isinstance(instance, pascal_pascal)

@given(instance=pascal_label_strategy)
@settings(max_examples=50)
def test_pascal_label_instantiation(instance):
    assert isinstance(instance, pascal_label)



@given(instance=pascal_label_strategy)
def test_pascal_label_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=pascal_statement_strategy)
@settings(max_examples=50)
def test_pascal_statement_instantiation(instance):
    assert isinstance(instance, pascal_statement)

@given(instance=pascal_statement_sequence_strategy)
@settings(max_examples=50)
def test_pascal_statement_sequence_instantiation(instance):
    assert isinstance(instance, pascal_statement_sequence)

@given(instance=pascal_statement_part_strategy)
@settings(max_examples=50)
def test_pascal_statement_part_instantiation(instance):
    assert isinstance(instance, pascal_statement_part)

@given(instance=pascal_procedure_and_function_declaration_part_strategy)
@settings(max_examples=50)
def test_pascal_procedure_and_function_declaration_part_instantiation(instance):
    assert isinstance(instance, pascal_procedure_and_function_declaration_part)

@given(instance=pascal_variable_declaration_part_strategy)
@settings(max_examples=50)
def test_pascal_variable_declaration_part_instantiation(instance):
    assert isinstance(instance, pascal_variable_declaration_part)

@given(instance=pascal_type_definition_part_strategy)
@settings(max_examples=50)
def test_pascal_type_definition_part_instantiation(instance):
    assert isinstance(instance, pascal_type_definition_part)

@given(instance=pascal_constant_definition_part_strategy)
@settings(max_examples=50)
def test_pascal_constant_definition_part_instantiation(instance):
    assert isinstance(instance, pascal_constant_definition_part)

@given(instance=pascal_label_declaration_part_strategy)
@settings(max_examples=50)
def test_pascal_label_declaration_part_instantiation(instance):
    assert isinstance(instance, pascal_label_declaration_part)

@given(instance=pascal_identifier_list_strategy)
@settings(max_examples=50)
def test_pascal_identifier_list_instantiation(instance):
    assert isinstance(instance, pascal_identifier_list)



@given(instance=pascal_identifier_list_strategy)
def test_pascal_identifier_list_names_setter(instance):
    original = instance.names
    instance.names = original
    assert instance.names == original

@given(instance=pascal_block_strategy)
@settings(max_examples=50)
def test_pascal_block_instantiation(instance):
    assert isinstance(instance, pascal_block)

@given(instance=pascal_program_heading_block_strategy)
@settings(max_examples=50)
def test_pascal_program_heading_block_instantiation(instance):
    assert isinstance(instance, pascal_program_heading_block)



@given(instance=pascal_program_heading_block_strategy)
def test_pascal_program_heading_block_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pascal_program_strategy)
@settings(max_examples=50)
def test_pascal_program_instantiation(instance):
    assert isinstance(instance, pascal_program)
