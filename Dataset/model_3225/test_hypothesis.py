import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    pascal_simple_expression,
    pascal_scale_factor,
    pascal_digit_sequence,
    pascal_real_number,
    pascal_integer_number,
    pascal_element_list,
    pascal_function_designator,
    pascal_set,
    pascal_number,
    pascal_goto_statement,
    pascal_procedure_statement,
    pascal_assignment_statement,
    pascal_structured_statement,
    pascal_simple_statement,
    output_value,
    pascal_expression,
    pascal_variable,
    pascal_actual_function,
    pascal_actual_procedure,
    pascal_actual_variable,
    pascal_actual_value,
    pascal_actual_parameter,
    pascal_actual_parameter_list,
    pascal_identifier,
    pascal_Begin,
    pascal_label,
    pascal_statement,
    pascal_statement_sequence,
    pascal_function_block,
    pascal_statement_part,
    pascal_declaration_part,
    pascal_procedure_block,
    pascal_identifier_list,
    pascal_block,
    pascal_program_heading,
    pascal_program,
    pascal_bound_specification,
    pascal_unpacked_conformant_array_schema,
    pascal_packed_conformant_array_schema,
    pascal_conformant_array_schema,
    output_list,
    pascal_output_value,
    pascal_output_list,
    pascal_ordinal_type_identifier,
    pascal_formal_parameter_section,
    pascal_formal_parameter_list,
    pascal_parameter_type,
    pascal_result_type,
    pascal_function_parameter_section,
    pascal_procedure_parameter_section,
    pascal_variable_parameter_section,
    pascal_value_parameter_section,
    pascal_subrange_type,
    pascal_element_type,
    pascal_index_type,
    pascal_compiler_defined_directives,
    pascal_variable_declaration,
    pascal_upper_bound,
    pascal_lower_bound,
    pascal_enumerated_type,
    pascal_file_component_type,
    pascal_file_type,
    pascal_set_type,
    pascal_record_type,
    pascal_array_type,
    pascal_unpacked_structured_type,
    pascal_variant,
    pascal_tag_field,
    pascal_record_section,
    pascal_variant_part,
    pascal_fixed_part,
    pascal_field_list,
    pascal_base_type,
    pascal_function_identification,
    pascal_function_body,
    pascal_function_heading,
    pascal_procedure_identification,
    pascal_directive,
    pascal_type_identifier,
    pascal_pointer_type,
    pascal_structured_type,
    pascal_simple_type,
    pascal_type,
    pascal_type_definition,
    pascal_constant_definition,
    pascal_for_statement,
    pascal_repeat_statement,
    pascal_while_statement,
    pascal_procedure_body,
    pascal_procedure_heading,
    pascal_variable_declaration_part,
    pascal_type_definition_part,
    pascal_constant_definition_part,
    pascal_label_declaration_part,
    pascal_final_expression,
    pascal_initial_expression,
    pascal_expression_list,
    pascal_entire_variable,
    pascal_constant,
    pascal_case_label_list,
    pascal_case_limb,
    pascal_case_statement,
    pascal_if_statement,
    pascal_with_statement,
    pascal_conditional_statement,
    pascal_repetitive_statement,
    pascal_compound_statement,
    pascal_factor,
    pascal_addition_operator,
    pascal_term,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pascal_simple_expression_is_not_abstract():
    assert not inspect.isabstract(pascal_simple_expression)


def test_pascal_simple_expression_constructor_exists():
    assert callable(pascal_simple_expression.__init__)


def test_pascal_simple_expression_constructor_args():
    sig = inspect.signature(pascal_simple_expression.__init__)
    params = list(sig.parameters.keys())
    assert "sign" in params, "Missing parameter 'sign'"

def test_pascal_simple_expression_has_sign():
    assert hasattr(pascal_simple_expression, "sign")
    descriptor = None
    for klass in pascal_simple_expression.__mro__:
        if "sign" in klass.__dict__:
            descriptor = klass.__dict__["sign"]
            break
    assert isinstance(descriptor, property)



def test_pascal_scale_factor_is_not_abstract():
    assert not inspect.isabstract(pascal_scale_factor)


def test_pascal_scale_factor_constructor_exists():
    assert callable(pascal_scale_factor.__init__)


def test_pascal_scale_factor_constructor_args():
    sig = inspect.signature(pascal_scale_factor.__init__)
    params = list(sig.parameters.keys())
    assert "sign" in params, "Missing parameter 'sign'"

def test_pascal_scale_factor_has_sign():
    assert hasattr(pascal_scale_factor, "sign")
    descriptor = None
    for klass in pascal_scale_factor.__mro__:
        if "sign" in klass.__dict__:
            descriptor = klass.__dict__["sign"]
            break
    assert isinstance(descriptor, property)



def test_pascal_digit_sequence_is_not_abstract():
    assert not inspect.isabstract(pascal_digit_sequence)


def test_pascal_digit_sequence_constructor_exists():
    assert callable(pascal_digit_sequence.__init__)


def test_pascal_digit_sequence_constructor_args():
    sig = inspect.signature(pascal_digit_sequence.__init__)
    params = list(sig.parameters.keys())
    assert "sign" in params, "Missing parameter 'sign'"
    assert "unsigned_digit_sequence" in params, "Missing parameter 'unsigned_digit_sequence'"

def test_pascal_digit_sequence_has_sign():
    assert hasattr(pascal_digit_sequence, "sign")
    descriptor = None
    for klass in pascal_digit_sequence.__mro__:
        if "sign" in klass.__dict__:
            descriptor = klass.__dict__["sign"]
            break
    assert isinstance(descriptor, property)

def test_pascal_digit_sequence_has_unsigned_digit_sequence():
    assert hasattr(pascal_digit_sequence, "unsigned_digit_sequence")
    descriptor = None
    for klass in pascal_digit_sequence.__mro__:
        if "unsigned_digit_sequence" in klass.__dict__:
            descriptor = klass.__dict__["unsigned_digit_sequence"]
            break
    assert isinstance(descriptor, property)



def test_pascal_real_number_is_not_abstract():
    assert not inspect.isabstract(pascal_real_number)


def test_pascal_real_number_constructor_exists():
    assert callable(pascal_real_number.__init__)


def test_pascal_real_number_constructor_args():
    sig = inspect.signature(pascal_real_number.__init__)
    params = list(sig.parameters.keys())



def test_pascal_integer_number_is_not_abstract():
    assert not inspect.isabstract(pascal_integer_number)


def test_pascal_integer_number_constructor_exists():
    assert callable(pascal_integer_number.__init__)


def test_pascal_integer_number_constructor_args():
    sig = inspect.signature(pascal_integer_number.__init__)
    params = list(sig.parameters.keys())



def test_pascal_element_list_is_not_abstract():
    assert not inspect.isabstract(pascal_element_list)


def test_pascal_element_list_constructor_exists():
    assert callable(pascal_element_list.__init__)


def test_pascal_element_list_constructor_args():
    sig = inspect.signature(pascal_element_list.__init__)
    params = list(sig.parameters.keys())



def test_pascal_function_designator_is_not_abstract():
    assert not inspect.isabstract(pascal_function_designator)


def test_pascal_function_designator_constructor_exists():
    assert callable(pascal_function_designator.__init__)


def test_pascal_function_designator_constructor_args():
    sig = inspect.signature(pascal_function_designator.__init__)
    params = list(sig.parameters.keys())



def test_pascal_set_is_not_abstract():
    assert not inspect.isabstract(pascal_set)


def test_pascal_set_constructor_exists():
    assert callable(pascal_set.__init__)


def test_pascal_set_constructor_args():
    sig = inspect.signature(pascal_set.__init__)
    params = list(sig.parameters.keys())



def test_pascal_number_is_not_abstract():
    assert not inspect.isabstract(pascal_number)


def test_pascal_number_constructor_exists():
    assert callable(pascal_number.__init__)


def test_pascal_number_constructor_args():
    sig = inspect.signature(pascal_number.__init__)
    params = list(sig.parameters.keys())



def test_pascal_goto_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_goto_statement)


def test_pascal_goto_statement_constructor_exists():
    assert callable(pascal_goto_statement.__init__)


def test_pascal_goto_statement_constructor_args():
    sig = inspect.signature(pascal_goto_statement.__init__)
    params = list(sig.parameters.keys())



def test_pascal_procedure_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_procedure_statement)


def test_pascal_procedure_statement_constructor_exists():
    assert callable(pascal_procedure_statement.__init__)


def test_pascal_procedure_statement_constructor_args():
    sig = inspect.signature(pascal_procedure_statement.__init__)
    params = list(sig.parameters.keys())



def test_pascal_assignment_statement_is_not_abstract():
    assert not inspect.isabstract(pascal_assignment_statement)


def test_pascal_assignment_statement_constructor_exists():
    assert callable(pascal_assignment_statement.__init__)


def test_pascal_assignment_statement_constructor_args():
    sig = inspect.signature(pascal_assignment_statement.__init__)
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



def test_output_value_is_not_abstract():
    assert not inspect.isabstract(output_value)


def test_output_value_constructor_exists():
    assert callable(output_value.__init__)


def test_output_value_constructor_args():
    sig = inspect.signature(output_value.__init__)
    params = list(sig.parameters.keys())



def test_pascal_expression_is_not_abstract():
    assert not inspect.isabstract(pascal_expression)


def test_pascal_expression_constructor_exists():
    assert callable(pascal_expression.__init__)


def test_pascal_expression_constructor_args():
    sig = inspect.signature(pascal_expression.__init__)
    params = list(sig.parameters.keys())
    assert "relational_operator" in params, "Missing parameter 'relational_operator'"

def test_pascal_expression_has_relational_operator():
    assert hasattr(pascal_expression, "relational_operator")
    descriptor = None
    for klass in pascal_expression.__mro__:
        if "relational_operator" in klass.__dict__:
            descriptor = klass.__dict__["relational_operator"]
            break
    assert isinstance(descriptor, property)



def test_pascal_variable_is_not_abstract():
    assert not inspect.isabstract(pascal_variable)


def test_pascal_variable_constructor_exists():
    assert callable(pascal_variable.__init__)


def test_pascal_variable_constructor_args():
    sig = inspect.signature(pascal_variable.__init__)
    params = list(sig.parameters.keys())



def test_pascal_actual_function_is_not_abstract():
    assert not inspect.isabstract(pascal_actual_function)


def test_pascal_actual_function_constructor_exists():
    assert callable(pascal_actual_function.__init__)


def test_pascal_actual_function_constructor_args():
    sig = inspect.signature(pascal_actual_function.__init__)
    params = list(sig.parameters.keys())



def test_pascal_actual_procedure_is_not_abstract():
    assert not inspect.isabstract(pascal_actual_procedure)


def test_pascal_actual_procedure_constructor_exists():
    assert callable(pascal_actual_procedure.__init__)


def test_pascal_actual_procedure_constructor_args():
    sig = inspect.signature(pascal_actual_procedure.__init__)
    params = list(sig.parameters.keys())



def test_pascal_actual_variable_is_not_abstract():
    assert not inspect.isabstract(pascal_actual_variable)


def test_pascal_actual_variable_constructor_exists():
    assert callable(pascal_actual_variable.__init__)


def test_pascal_actual_variable_constructor_args():
    sig = inspect.signature(pascal_actual_variable.__init__)
    params = list(sig.parameters.keys())



def test_pascal_actual_value_is_not_abstract():
    assert not inspect.isabstract(pascal_actual_value)


def test_pascal_actual_value_constructor_exists():
    assert callable(pascal_actual_value.__init__)


def test_pascal_actual_value_constructor_args():
    sig = inspect.signature(pascal_actual_value.__init__)
    params = list(sig.parameters.keys())



def test_pascal_actual_parameter_is_not_abstract():
    assert not inspect.isabstract(pascal_actual_parameter)


def test_pascal_actual_parameter_constructor_exists():
    assert callable(pascal_actual_parameter.__init__)


def test_pascal_actual_parameter_constructor_args():
    sig = inspect.signature(pascal_actual_parameter.__init__)
    params = list(sig.parameters.keys())



def test_pascal_actual_parameter_list_is_not_abstract():
    assert not inspect.isabstract(pascal_actual_parameter_list)


def test_pascal_actual_parameter_list_constructor_exists():
    assert callable(pascal_actual_parameter_list.__init__)


def test_pascal_actual_parameter_list_constructor_args():
    sig = inspect.signature(pascal_actual_parameter_list.__init__)
    params = list(sig.parameters.keys())



def test_pascal_identifier_is_not_abstract():
    assert not inspect.isabstract(pascal_identifier)


def test_pascal_identifier_constructor_exists():
    assert callable(pascal_identifier.__init__)


def test_pascal_identifier_constructor_args():
    sig = inspect.signature(pascal_identifier.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_pascal_identifier_has_identifier():
    assert hasattr(pascal_identifier, "identifier")
    descriptor = None
    for klass in pascal_identifier.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_pascal_begin_is_not_abstract():
    assert not inspect.isabstract(pascal_Begin)


def test_pascal_begin_constructor_exists():
    assert callable(pascal_Begin.__init__)


def test_pascal_begin_constructor_args():
    sig = inspect.signature(pascal_Begin.__init__)
    params = list(sig.parameters.keys())



def test_pascal_label_is_not_abstract():
    assert not inspect.isabstract(pascal_label)


def test_pascal_label_constructor_exists():
    assert callable(pascal_label.__init__)


def test_pascal_label_constructor_args():
    sig = inspect.signature(pascal_label.__init__)
    params = list(sig.parameters.keys())



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



def test_pascal_function_block_is_not_abstract():
    assert not inspect.isabstract(pascal_function_block)


def test_pascal_function_block_constructor_exists():
    assert callable(pascal_function_block.__init__)


def test_pascal_function_block_constructor_args():
    sig = inspect.signature(pascal_function_block.__init__)
    params = list(sig.parameters.keys())



def test_pascal_statement_part_is_not_abstract():
    assert not inspect.isabstract(pascal_statement_part)


def test_pascal_statement_part_constructor_exists():
    assert callable(pascal_statement_part.__init__)


def test_pascal_statement_part_constructor_args():
    sig = inspect.signature(pascal_statement_part.__init__)
    params = list(sig.parameters.keys())



def test_pascal_declaration_part_is_not_abstract():
    assert not inspect.isabstract(pascal_declaration_part)


def test_pascal_declaration_part_constructor_exists():
    assert callable(pascal_declaration_part.__init__)


def test_pascal_declaration_part_constructor_args():
    sig = inspect.signature(pascal_declaration_part.__init__)
    params = list(sig.parameters.keys())



def test_pascal_procedure_block_is_not_abstract():
    assert not inspect.isabstract(pascal_procedure_block)


def test_pascal_procedure_block_constructor_exists():
    assert callable(pascal_procedure_block.__init__)


def test_pascal_procedure_block_constructor_args():
    sig = inspect.signature(pascal_procedure_block.__init__)
    params = list(sig.parameters.keys())



def test_pascal_identifier_list_is_not_abstract():
    assert not inspect.isabstract(pascal_identifier_list)


def test_pascal_identifier_list_constructor_exists():
    assert callable(pascal_identifier_list.__init__)


def test_pascal_identifier_list_constructor_args():
    sig = inspect.signature(pascal_identifier_list.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_pascal_identifier_list_has_identifier():
    assert hasattr(pascal_identifier_list, "identifier")
    descriptor = None
    for klass in pascal_identifier_list.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_pascal_block_is_not_abstract():
    assert not inspect.isabstract(pascal_block)


def test_pascal_block_constructor_exists():
    assert callable(pascal_block.__init__)


def test_pascal_block_constructor_args():
    sig = inspect.signature(pascal_block.__init__)
    params = list(sig.parameters.keys())



def test_pascal_program_heading_is_not_abstract():
    assert not inspect.isabstract(pascal_program_heading)


def test_pascal_program_heading_constructor_exists():
    assert callable(pascal_program_heading.__init__)


def test_pascal_program_heading_constructor_args():
    sig = inspect.signature(pascal_program_heading.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_pascal_program_heading_has_identifier():
    assert hasattr(pascal_program_heading, "identifier")
    descriptor = None
    for klass in pascal_program_heading.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_pascal_program_is_not_abstract():
    assert not inspect.isabstract(pascal_program)


def test_pascal_program_constructor_exists():
    assert callable(pascal_program.__init__)


def test_pascal_program_constructor_args():
    sig = inspect.signature(pascal_program.__init__)
    params = list(sig.parameters.keys())



def test_pascal_bound_specification_is_not_abstract():
    assert not inspect.isabstract(pascal_bound_specification)


def test_pascal_bound_specification_constructor_exists():
    assert callable(pascal_bound_specification.__init__)


def test_pascal_bound_specification_constructor_args():
    sig = inspect.signature(pascal_bound_specification.__init__)
    params = list(sig.parameters.keys())



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



def test_pascal_conformant_array_schema_is_not_abstract():
    assert not inspect.isabstract(pascal_conformant_array_schema)


def test_pascal_conformant_array_schema_constructor_exists():
    assert callable(pascal_conformant_array_schema.__init__)


def test_pascal_conformant_array_schema_constructor_args():
    sig = inspect.signature(pascal_conformant_array_schema.__init__)
    params = list(sig.parameters.keys())



def test_output_list_is_not_abstract():
    assert not inspect.isabstract(output_list)


def test_output_list_constructor_exists():
    assert callable(output_list.__init__)


def test_output_list_constructor_args():
    sig = inspect.signature(output_list.__init__)
    params = list(sig.parameters.keys())



def test_pascal_output_value_is_not_abstract():
    assert not inspect.isabstract(pascal_output_value)


def test_pascal_output_value_constructor_exists():
    assert callable(pascal_output_value.__init__)


def test_pascal_output_value_constructor_args():
    sig = inspect.signature(pascal_output_value.__init__)
    params = list(sig.parameters.keys())



def test_pascal_output_list_is_not_abstract():
    assert not inspect.isabstract(pascal_output_list)


def test_pascal_output_list_constructor_exists():
    assert callable(pascal_output_list.__init__)


def test_pascal_output_list_constructor_args():
    sig = inspect.signature(pascal_output_list.__init__)
    params = list(sig.parameters.keys())



def test_pascal_ordinal_type_identifier_is_not_abstract():
    assert not inspect.isabstract(pascal_ordinal_type_identifier)


def test_pascal_ordinal_type_identifier_constructor_exists():
    assert callable(pascal_ordinal_type_identifier.__init__)


def test_pascal_ordinal_type_identifier_constructor_args():
    sig = inspect.signature(pascal_ordinal_type_identifier.__init__)
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



def test_pascal_parameter_type_is_not_abstract():
    assert not inspect.isabstract(pascal_parameter_type)


def test_pascal_parameter_type_constructor_exists():
    assert callable(pascal_parameter_type.__init__)


def test_pascal_parameter_type_constructor_args():
    sig = inspect.signature(pascal_parameter_type.__init__)
    params = list(sig.parameters.keys())



def test_pascal_result_type_is_not_abstract():
    assert not inspect.isabstract(pascal_result_type)


def test_pascal_result_type_constructor_exists():
    assert callable(pascal_result_type.__init__)


def test_pascal_result_type_constructor_args():
    sig = inspect.signature(pascal_result_type.__init__)
    params = list(sig.parameters.keys())



def test_pascal_function_parameter_section_is_not_abstract():
    assert not inspect.isabstract(pascal_function_parameter_section)


def test_pascal_function_parameter_section_constructor_exists():
    assert callable(pascal_function_parameter_section.__init__)


def test_pascal_function_parameter_section_constructor_args():
    sig = inspect.signature(pascal_function_parameter_section.__init__)
    params = list(sig.parameters.keys())



def test_pascal_procedure_parameter_section_is_not_abstract():
    assert not inspect.isabstract(pascal_procedure_parameter_section)


def test_pascal_procedure_parameter_section_constructor_exists():
    assert callable(pascal_procedure_parameter_section.__init__)


def test_pascal_procedure_parameter_section_constructor_args():
    sig = inspect.signature(pascal_procedure_parameter_section.__init__)
    params = list(sig.parameters.keys())



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



def test_pascal_subrange_type_is_not_abstract():
    assert not inspect.isabstract(pascal_subrange_type)


def test_pascal_subrange_type_constructor_exists():
    assert callable(pascal_subrange_type.__init__)


def test_pascal_subrange_type_constructor_args():
    sig = inspect.signature(pascal_subrange_type.__init__)
    params = list(sig.parameters.keys())



def test_pascal_element_type_is_not_abstract():
    assert not inspect.isabstract(pascal_element_type)


def test_pascal_element_type_constructor_exists():
    assert callable(pascal_element_type.__init__)


def test_pascal_element_type_constructor_args():
    sig = inspect.signature(pascal_element_type.__init__)
    params = list(sig.parameters.keys())



def test_pascal_index_type_is_not_abstract():
    assert not inspect.isabstract(pascal_index_type)


def test_pascal_index_type_constructor_exists():
    assert callable(pascal_index_type.__init__)


def test_pascal_index_type_constructor_args():
    sig = inspect.signature(pascal_index_type.__init__)
    params = list(sig.parameters.keys())



def test_pascal_compiler_defined_directives_is_not_abstract():
    assert not inspect.isabstract(pascal_compiler_defined_directives)


def test_pascal_compiler_defined_directives_constructor_exists():
    assert callable(pascal_compiler_defined_directives.__init__)


def test_pascal_compiler_defined_directives_constructor_args():
    sig = inspect.signature(pascal_compiler_defined_directives.__init__)
    params = list(sig.parameters.keys())



def test_pascal_variable_declaration_is_not_abstract():
    assert not inspect.isabstract(pascal_variable_declaration)


def test_pascal_variable_declaration_constructor_exists():
    assert callable(pascal_variable_declaration.__init__)


def test_pascal_variable_declaration_constructor_args():
    sig = inspect.signature(pascal_variable_declaration.__init__)
    params = list(sig.parameters.keys())



def test_pascal_upper_bound_is_not_abstract():
    assert not inspect.isabstract(pascal_upper_bound)


def test_pascal_upper_bound_constructor_exists():
    assert callable(pascal_upper_bound.__init__)


def test_pascal_upper_bound_constructor_args():
    sig = inspect.signature(pascal_upper_bound.__init__)
    params = list(sig.parameters.keys())



def test_pascal_lower_bound_is_not_abstract():
    assert not inspect.isabstract(pascal_lower_bound)


def test_pascal_lower_bound_constructor_exists():
    assert callable(pascal_lower_bound.__init__)


def test_pascal_lower_bound_constructor_args():
    sig = inspect.signature(pascal_lower_bound.__init__)
    params = list(sig.parameters.keys())



def test_pascal_enumerated_type_is_not_abstract():
    assert not inspect.isabstract(pascal_enumerated_type)


def test_pascal_enumerated_type_constructor_exists():
    assert callable(pascal_enumerated_type.__init__)


def test_pascal_enumerated_type_constructor_args():
    sig = inspect.signature(pascal_enumerated_type.__init__)
    params = list(sig.parameters.keys())



def test_pascal_file_component_type_is_not_abstract():
    assert not inspect.isabstract(pascal_file_component_type)


def test_pascal_file_component_type_constructor_exists():
    assert callable(pascal_file_component_type.__init__)


def test_pascal_file_component_type_constructor_args():
    sig = inspect.signature(pascal_file_component_type.__init__)
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



def test_pascal_fixed_part_is_not_abstract():
    assert not inspect.isabstract(pascal_fixed_part)


def test_pascal_fixed_part_constructor_exists():
    assert callable(pascal_fixed_part.__init__)


def test_pascal_fixed_part_constructor_args():
    sig = inspect.signature(pascal_fixed_part.__init__)
    params = list(sig.parameters.keys())



def test_pascal_field_list_is_not_abstract():
    assert not inspect.isabstract(pascal_field_list)


def test_pascal_field_list_constructor_exists():
    assert callable(pascal_field_list.__init__)


def test_pascal_field_list_constructor_args():
    sig = inspect.signature(pascal_field_list.__init__)
    params = list(sig.parameters.keys())



def test_pascal_base_type_is_not_abstract():
    assert not inspect.isabstract(pascal_base_type)


def test_pascal_base_type_constructor_exists():
    assert callable(pascal_base_type.__init__)


def test_pascal_base_type_constructor_args():
    sig = inspect.signature(pascal_base_type.__init__)
    params = list(sig.parameters.keys())



def test_pascal_function_identification_is_not_abstract():
    assert not inspect.isabstract(pascal_function_identification)


def test_pascal_function_identification_constructor_exists():
    assert callable(pascal_function_identification.__init__)


def test_pascal_function_identification_constructor_args():
    sig = inspect.signature(pascal_function_identification.__init__)
    params = list(sig.parameters.keys())



def test_pascal_function_body_is_not_abstract():
    assert not inspect.isabstract(pascal_function_body)


def test_pascal_function_body_constructor_exists():
    assert callable(pascal_function_body.__init__)


def test_pascal_function_body_constructor_args():
    sig = inspect.signature(pascal_function_body.__init__)
    params = list(sig.parameters.keys())



def test_pascal_function_heading_is_not_abstract():
    assert not inspect.isabstract(pascal_function_heading)


def test_pascal_function_heading_constructor_exists():
    assert callable(pascal_function_heading.__init__)


def test_pascal_function_heading_constructor_args():
    sig = inspect.signature(pascal_function_heading.__init__)
    params = list(sig.parameters.keys())



def test_pascal_procedure_identification_is_not_abstract():
    assert not inspect.isabstract(pascal_procedure_identification)


def test_pascal_procedure_identification_constructor_exists():
    assert callable(pascal_procedure_identification.__init__)


def test_pascal_procedure_identification_constructor_args():
    sig = inspect.signature(pascal_procedure_identification.__init__)
    params = list(sig.parameters.keys())



def test_pascal_directive_is_not_abstract():
    assert not inspect.isabstract(pascal_directive)


def test_pascal_directive_constructor_exists():
    assert callable(pascal_directive.__init__)


def test_pascal_directive_constructor_args():
    sig = inspect.signature(pascal_directive.__init__)
    params = list(sig.parameters.keys())



def test_pascal_type_identifier_is_not_abstract():
    assert not inspect.isabstract(pascal_type_identifier)


def test_pascal_type_identifier_constructor_exists():
    assert callable(pascal_type_identifier.__init__)


def test_pascal_type_identifier_constructor_args():
    sig = inspect.signature(pascal_type_identifier.__init__)
    params = list(sig.parameters.keys())



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



def test_pascal_simple_type_is_not_abstract():
    assert not inspect.isabstract(pascal_simple_type)


def test_pascal_simple_type_constructor_exists():
    assert callable(pascal_simple_type.__init__)


def test_pascal_simple_type_constructor_args():
    sig = inspect.signature(pascal_simple_type.__init__)
    params = list(sig.parameters.keys())



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



def test_pascal_constant_definition_is_not_abstract():
    assert not inspect.isabstract(pascal_constant_definition)


def test_pascal_constant_definition_constructor_exists():
    assert callable(pascal_constant_definition.__init__)


def test_pascal_constant_definition_constructor_args():
    sig = inspect.signature(pascal_constant_definition.__init__)
    params = list(sig.parameters.keys())



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



def test_pascal_procedure_body_is_not_abstract():
    assert not inspect.isabstract(pascal_procedure_body)


def test_pascal_procedure_body_constructor_exists():
    assert callable(pascal_procedure_body.__init__)


def test_pascal_procedure_body_constructor_args():
    sig = inspect.signature(pascal_procedure_body.__init__)
    params = list(sig.parameters.keys())



def test_pascal_procedure_heading_is_not_abstract():
    assert not inspect.isabstract(pascal_procedure_heading)


def test_pascal_procedure_heading_constructor_exists():
    assert callable(pascal_procedure_heading.__init__)


def test_pascal_procedure_heading_constructor_args():
    sig = inspect.signature(pascal_procedure_heading.__init__)
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



def test_pascal_final_expression_is_not_abstract():
    assert not inspect.isabstract(pascal_final_expression)


def test_pascal_final_expression_constructor_exists():
    assert callable(pascal_final_expression.__init__)


def test_pascal_final_expression_constructor_args():
    sig = inspect.signature(pascal_final_expression.__init__)
    params = list(sig.parameters.keys())



def test_pascal_initial_expression_is_not_abstract():
    assert not inspect.isabstract(pascal_initial_expression)


def test_pascal_initial_expression_constructor_exists():
    assert callable(pascal_initial_expression.__init__)


def test_pascal_initial_expression_constructor_args():
    sig = inspect.signature(pascal_initial_expression.__init__)
    params = list(sig.parameters.keys())



def test_pascal_expression_list_is_not_abstract():
    assert not inspect.isabstract(pascal_expression_list)


def test_pascal_expression_list_constructor_exists():
    assert callable(pascal_expression_list.__init__)


def test_pascal_expression_list_constructor_args():
    sig = inspect.signature(pascal_expression_list.__init__)
    params = list(sig.parameters.keys())



def test_pascal_entire_variable_is_not_abstract():
    assert not inspect.isabstract(pascal_entire_variable)


def test_pascal_entire_variable_constructor_exists():
    assert callable(pascal_entire_variable.__init__)


def test_pascal_entire_variable_constructor_args():
    sig = inspect.signature(pascal_entire_variable.__init__)
    params = list(sig.parameters.keys())



def test_pascal_constant_is_not_abstract():
    assert not inspect.isabstract(pascal_constant)


def test_pascal_constant_constructor_exists():
    assert callable(pascal_constant.__init__)


def test_pascal_constant_constructor_args():
    sig = inspect.signature(pascal_constant.__init__)
    params = list(sig.parameters.keys())
    assert "sign" in params, "Missing parameter 'sign'"
    assert "boolean" in params, "Missing parameter 'boolean'"
    assert "strings" in params, "Missing parameter 'strings'"

def test_pascal_constant_has_sign():
    assert hasattr(pascal_constant, "sign")
    descriptor = None
    for klass in pascal_constant.__mro__:
        if "sign" in klass.__dict__:
            descriptor = klass.__dict__["sign"]
            break
    assert isinstance(descriptor, property)

def test_pascal_constant_has_boolean():
    assert hasattr(pascal_constant, "boolean")
    descriptor = None
    for klass in pascal_constant.__mro__:
        if "boolean" in klass.__dict__:
            descriptor = klass.__dict__["boolean"]
            break
    assert isinstance(descriptor, property)

def test_pascal_constant_has_strings():
    assert hasattr(pascal_constant, "strings")
    descriptor = None
    for klass in pascal_constant.__mro__:
        if "strings" in klass.__dict__:
            descriptor = klass.__dict__["strings"]
            break
    assert isinstance(descriptor, property)



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



def test_pascal_factor_is_not_abstract():
    assert not inspect.isabstract(pascal_factor)


def test_pascal_factor_constructor_exists():
    assert callable(pascal_factor.__init__)


def test_pascal_factor_constructor_args():
    sig = inspect.signature(pascal_factor.__init__)
    params = list(sig.parameters.keys())
    assert "boolean" in params, "Missing parameter 'boolean'"
    assert "strings" in params, "Missing parameter 'strings'"

def test_pascal_factor_has_boolean():
    assert hasattr(pascal_factor, "boolean")
    descriptor = None
    for klass in pascal_factor.__mro__:
        if "boolean" in klass.__dict__:
            descriptor = klass.__dict__["boolean"]
            break
    assert isinstance(descriptor, property)

def test_pascal_factor_has_strings():
    assert hasattr(pascal_factor, "strings")
    descriptor = None
    for klass in pascal_factor.__mro__:
        if "strings" in klass.__dict__:
            descriptor = klass.__dict__["strings"]
            break
    assert isinstance(descriptor, property)



def test_pascal_addition_operator_is_not_abstract():
    assert not inspect.isabstract(pascal_addition_operator)


def test_pascal_addition_operator_constructor_exists():
    assert callable(pascal_addition_operator.__init__)


def test_pascal_addition_operator_constructor_args():
    sig = inspect.signature(pascal_addition_operator.__init__)
    params = list(sig.parameters.keys())
    assert "sign" in params, "Missing parameter 'sign'"

def test_pascal_addition_operator_has_sign():
    assert hasattr(pascal_addition_operator, "sign")
    descriptor = None
    for klass in pascal_addition_operator.__mro__:
        if "sign" in klass.__dict__:
            descriptor = klass.__dict__["sign"]
            break
    assert isinstance(descriptor, property)



def test_pascal_term_is_not_abstract():
    assert not inspect.isabstract(pascal_term)


def test_pascal_term_constructor_exists():
    assert callable(pascal_term.__init__)


def test_pascal_term_constructor_args():
    sig = inspect.signature(pascal_term.__init__)
    params = list(sig.parameters.keys())
    assert "multiplication_operator" in params, "Missing parameter 'multiplication_operator'"

def test_pascal_term_has_multiplication_operator():
    assert hasattr(pascal_term, "multiplication_operator")
    descriptor = None
    for klass in pascal_term.__mro__:
        if "multiplication_operator" in klass.__dict__:
            descriptor = klass.__dict__["multiplication_operator"]
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
pascal_simple_expression_strategy = st.builds(
    pascal_simple_expression,
    sign=
        safe_text
)
pascal_scale_factor_strategy = st.builds(
    pascal_scale_factor,
    sign=
        safe_text
)
pascal_digit_sequence_strategy = st.builds(
    pascal_digit_sequence,
    sign=
        safe_text,
    unsigned_digit_sequence=
        safe_text
)
pascal_real_number_strategy = st.builds(
    pascal_real_number,
)
pascal_integer_number_strategy = st.builds(
    pascal_integer_number,
)
pascal_element_list_strategy = st.builds(
    pascal_element_list,
)
pascal_function_designator_strategy = st.builds(
    pascal_function_designator,
)
pascal_set_strategy = st.builds(
    pascal_set,
)
pascal_number_strategy = st.builds(
    pascal_number,
)
pascal_goto_statement_strategy = st.builds(
    pascal_goto_statement,
)
pascal_procedure_statement_strategy = st.builds(
    pascal_procedure_statement,
)
pascal_assignment_statement_strategy = st.builds(
    pascal_assignment_statement,
)
pascal_structured_statement_strategy = st.builds(
    pascal_structured_statement,
)
pascal_simple_statement_strategy = st.builds(
    pascal_simple_statement,
)
output_value_strategy = st.builds(
    output_value,
)
pascal_expression_strategy = st.builds(
    pascal_expression,
    relational_operator=
        safe_text
)
pascal_variable_strategy = st.builds(
    pascal_variable,
)
pascal_actual_function_strategy = st.builds(
    pascal_actual_function,
)
pascal_actual_procedure_strategy = st.builds(
    pascal_actual_procedure,
)
pascal_actual_variable_strategy = st.builds(
    pascal_actual_variable,
)
pascal_actual_value_strategy = st.builds(
    pascal_actual_value,
)
pascal_actual_parameter_strategy = st.builds(
    pascal_actual_parameter,
)
pascal_actual_parameter_list_strategy = st.builds(
    pascal_actual_parameter_list,
)
pascal_identifier_strategy = st.builds(
    pascal_identifier,
    identifier=
        safe_text
)
pascal_Begin_strategy = st.builds(
    pascal_Begin,
)
pascal_label_strategy = st.builds(
    pascal_label,
)
pascal_statement_strategy = st.builds(
    pascal_statement,
)
pascal_statement_sequence_strategy = st.builds(
    pascal_statement_sequence,
)
pascal_function_block_strategy = st.builds(
    pascal_function_block,
)
pascal_statement_part_strategy = st.builds(
    pascal_statement_part,
)
pascal_declaration_part_strategy = st.builds(
    pascal_declaration_part,
)
pascal_procedure_block_strategy = st.builds(
    pascal_procedure_block,
)
pascal_identifier_list_strategy = st.builds(
    pascal_identifier_list,
    identifier=
        safe_text
)
pascal_block_strategy = st.builds(
    pascal_block,
)
pascal_program_heading_strategy = st.builds(
    pascal_program_heading,
    identifier=
        safe_text
)
pascal_program_strategy = st.builds(
    pascal_program,
)
pascal_bound_specification_strategy = st.builds(
    pascal_bound_specification,
)
pascal_unpacked_conformant_array_schema_strategy = st.builds(
    pascal_unpacked_conformant_array_schema,
)
pascal_packed_conformant_array_schema_strategy = st.builds(
    pascal_packed_conformant_array_schema,
)
pascal_conformant_array_schema_strategy = st.builds(
    pascal_conformant_array_schema,
)
output_list_strategy = st.builds(
    output_list,
)
pascal_output_value_strategy = st.builds(
    pascal_output_value,
)
pascal_output_list_strategy = st.builds(
    pascal_output_list,
)
pascal_ordinal_type_identifier_strategy = st.builds(
    pascal_ordinal_type_identifier,
)
pascal_formal_parameter_section_strategy = st.builds(
    pascal_formal_parameter_section,
)
pascal_formal_parameter_list_strategy = st.builds(
    pascal_formal_parameter_list,
)
pascal_parameter_type_strategy = st.builds(
    pascal_parameter_type,
)
pascal_result_type_strategy = st.builds(
    pascal_result_type,
)
pascal_function_parameter_section_strategy = st.builds(
    pascal_function_parameter_section,
)
pascal_procedure_parameter_section_strategy = st.builds(
    pascal_procedure_parameter_section,
)
pascal_variable_parameter_section_strategy = st.builds(
    pascal_variable_parameter_section,
)
pascal_value_parameter_section_strategy = st.builds(
    pascal_value_parameter_section,
)
pascal_subrange_type_strategy = st.builds(
    pascal_subrange_type,
)
pascal_element_type_strategy = st.builds(
    pascal_element_type,
)
pascal_index_type_strategy = st.builds(
    pascal_index_type,
)
pascal_compiler_defined_directives_strategy = st.builds(
    pascal_compiler_defined_directives,
)
pascal_variable_declaration_strategy = st.builds(
    pascal_variable_declaration,
)
pascal_upper_bound_strategy = st.builds(
    pascal_upper_bound,
)
pascal_lower_bound_strategy = st.builds(
    pascal_lower_bound,
)
pascal_enumerated_type_strategy = st.builds(
    pascal_enumerated_type,
)
pascal_file_component_type_strategy = st.builds(
    pascal_file_component_type,
)
pascal_file_type_strategy = st.builds(
    pascal_file_type,
)
pascal_set_type_strategy = st.builds(
    pascal_set_type,
)
pascal_record_type_strategy = st.builds(
    pascal_record_type,
)
pascal_array_type_strategy = st.builds(
    pascal_array_type,
)
pascal_unpacked_structured_type_strategy = st.builds(
    pascal_unpacked_structured_type,
)
pascal_variant_strategy = st.builds(
    pascal_variant,
)
pascal_tag_field_strategy = st.builds(
    pascal_tag_field,
)
pascal_record_section_strategy = st.builds(
    pascal_record_section,
)
pascal_variant_part_strategy = st.builds(
    pascal_variant_part,
)
pascal_fixed_part_strategy = st.builds(
    pascal_fixed_part,
)
pascal_field_list_strategy = st.builds(
    pascal_field_list,
)
pascal_base_type_strategy = st.builds(
    pascal_base_type,
)
pascal_function_identification_strategy = st.builds(
    pascal_function_identification,
)
pascal_function_body_strategy = st.builds(
    pascal_function_body,
)
pascal_function_heading_strategy = st.builds(
    pascal_function_heading,
)
pascal_procedure_identification_strategy = st.builds(
    pascal_procedure_identification,
)
pascal_directive_strategy = st.builds(
    pascal_directive,
)
pascal_type_identifier_strategy = st.builds(
    pascal_type_identifier,
)
pascal_pointer_type_strategy = st.builds(
    pascal_pointer_type,
)
pascal_structured_type_strategy = st.builds(
    pascal_structured_type,
)
pascal_simple_type_strategy = st.builds(
    pascal_simple_type,
)
pascal_type_strategy = st.builds(
    pascal_type,
)
pascal_type_definition_strategy = st.builds(
    pascal_type_definition,
)
pascal_constant_definition_strategy = st.builds(
    pascal_constant_definition,
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
pascal_procedure_body_strategy = st.builds(
    pascal_procedure_body,
)
pascal_procedure_heading_strategy = st.builds(
    pascal_procedure_heading,
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
pascal_final_expression_strategy = st.builds(
    pascal_final_expression,
)
pascal_initial_expression_strategy = st.builds(
    pascal_initial_expression,
)
pascal_expression_list_strategy = st.builds(
    pascal_expression_list,
)
pascal_entire_variable_strategy = st.builds(
    pascal_entire_variable,
)
pascal_constant_strategy = st.builds(
    pascal_constant,
    sign=
        safe_text,
    boolean=
        safe_text,
    strings=
        safe_text
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
pascal_factor_strategy = st.builds(
    pascal_factor,
    boolean=
        safe_text,
    strings=
        safe_text
)
pascal_addition_operator_strategy = st.builds(
    pascal_addition_operator,
    sign=
        safe_text
)
pascal_term_strategy = st.builds(
    pascal_term,
    multiplication_operator=
        safe_text
)

@given(instance=pascal_simple_expression_strategy)
@settings(max_examples=50)
def test_pascal_simple_expression_instantiation(instance):
    assert isinstance(instance, pascal_simple_expression)



@given(instance=pascal_simple_expression_strategy)
def test_pascal_simple_expression_sign_setter(instance):
    original = instance.sign
    instance.sign = original
    assert instance.sign == original

@given(instance=pascal_scale_factor_strategy)
@settings(max_examples=50)
def test_pascal_scale_factor_instantiation(instance):
    assert isinstance(instance, pascal_scale_factor)



@given(instance=pascal_scale_factor_strategy)
def test_pascal_scale_factor_sign_setter(instance):
    original = instance.sign
    instance.sign = original
    assert instance.sign == original

@given(instance=pascal_digit_sequence_strategy)
@settings(max_examples=50)
def test_pascal_digit_sequence_instantiation(instance):
    assert isinstance(instance, pascal_digit_sequence)



@given(instance=pascal_digit_sequence_strategy)
def test_pascal_digit_sequence_sign_setter(instance):
    original = instance.sign
    instance.sign = original
    assert instance.sign == original



@given(instance=pascal_digit_sequence_strategy)
def test_pascal_digit_sequence_unsigned_digit_sequence_setter(instance):
    original = instance.unsigned_digit_sequence
    instance.unsigned_digit_sequence = original
    assert instance.unsigned_digit_sequence == original

@given(instance=pascal_real_number_strategy)
@settings(max_examples=50)
def test_pascal_real_number_instantiation(instance):
    assert isinstance(instance, pascal_real_number)

@given(instance=pascal_integer_number_strategy)
@settings(max_examples=50)
def test_pascal_integer_number_instantiation(instance):
    assert isinstance(instance, pascal_integer_number)

@given(instance=pascal_element_list_strategy)
@settings(max_examples=50)
def test_pascal_element_list_instantiation(instance):
    assert isinstance(instance, pascal_element_list)

@given(instance=pascal_function_designator_strategy)
@settings(max_examples=50)
def test_pascal_function_designator_instantiation(instance):
    assert isinstance(instance, pascal_function_designator)

@given(instance=pascal_set_strategy)
@settings(max_examples=50)
def test_pascal_set_instantiation(instance):
    assert isinstance(instance, pascal_set)

@given(instance=pascal_number_strategy)
@settings(max_examples=50)
def test_pascal_number_instantiation(instance):
    assert isinstance(instance, pascal_number)

@given(instance=pascal_goto_statement_strategy)
@settings(max_examples=50)
def test_pascal_goto_statement_instantiation(instance):
    assert isinstance(instance, pascal_goto_statement)

@given(instance=pascal_procedure_statement_strategy)
@settings(max_examples=50)
def test_pascal_procedure_statement_instantiation(instance):
    assert isinstance(instance, pascal_procedure_statement)

@given(instance=pascal_assignment_statement_strategy)
@settings(max_examples=50)
def test_pascal_assignment_statement_instantiation(instance):
    assert isinstance(instance, pascal_assignment_statement)

@given(instance=pascal_structured_statement_strategy)
@settings(max_examples=50)
def test_pascal_structured_statement_instantiation(instance):
    assert isinstance(instance, pascal_structured_statement)

@given(instance=pascal_simple_statement_strategy)
@settings(max_examples=50)
def test_pascal_simple_statement_instantiation(instance):
    assert isinstance(instance, pascal_simple_statement)

@given(instance=output_value_strategy)
@settings(max_examples=50)
def test_output_value_instantiation(instance):
    assert isinstance(instance, output_value)

@given(instance=pascal_expression_strategy)
@settings(max_examples=50)
def test_pascal_expression_instantiation(instance):
    assert isinstance(instance, pascal_expression)



@given(instance=pascal_expression_strategy)
def test_pascal_expression_relational_operator_setter(instance):
    original = instance.relational_operator
    instance.relational_operator = original
    assert instance.relational_operator == original

@given(instance=pascal_variable_strategy)
@settings(max_examples=50)
def test_pascal_variable_instantiation(instance):
    assert isinstance(instance, pascal_variable)

@given(instance=pascal_actual_function_strategy)
@settings(max_examples=50)
def test_pascal_actual_function_instantiation(instance):
    assert isinstance(instance, pascal_actual_function)

@given(instance=pascal_actual_procedure_strategy)
@settings(max_examples=50)
def test_pascal_actual_procedure_instantiation(instance):
    assert isinstance(instance, pascal_actual_procedure)

@given(instance=pascal_actual_variable_strategy)
@settings(max_examples=50)
def test_pascal_actual_variable_instantiation(instance):
    assert isinstance(instance, pascal_actual_variable)

@given(instance=pascal_actual_value_strategy)
@settings(max_examples=50)
def test_pascal_actual_value_instantiation(instance):
    assert isinstance(instance, pascal_actual_value)

@given(instance=pascal_actual_parameter_strategy)
@settings(max_examples=50)
def test_pascal_actual_parameter_instantiation(instance):
    assert isinstance(instance, pascal_actual_parameter)

@given(instance=pascal_actual_parameter_list_strategy)
@settings(max_examples=50)
def test_pascal_actual_parameter_list_instantiation(instance):
    assert isinstance(instance, pascal_actual_parameter_list)

@given(instance=pascal_identifier_strategy)
@settings(max_examples=50)
def test_pascal_identifier_instantiation(instance):
    assert isinstance(instance, pascal_identifier)



@given(instance=pascal_identifier_strategy)
def test_pascal_identifier_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=pascal_Begin_strategy)
@settings(max_examples=50)
def test_pascal_begin_instantiation(instance):
    assert isinstance(instance, pascal_Begin)

@given(instance=pascal_label_strategy)
@settings(max_examples=50)
def test_pascal_label_instantiation(instance):
    assert isinstance(instance, pascal_label)

@given(instance=pascal_statement_strategy)
@settings(max_examples=50)
def test_pascal_statement_instantiation(instance):
    assert isinstance(instance, pascal_statement)

@given(instance=pascal_statement_sequence_strategy)
@settings(max_examples=50)
def test_pascal_statement_sequence_instantiation(instance):
    assert isinstance(instance, pascal_statement_sequence)

@given(instance=pascal_function_block_strategy)
@settings(max_examples=50)
def test_pascal_function_block_instantiation(instance):
    assert isinstance(instance, pascal_function_block)

@given(instance=pascal_statement_part_strategy)
@settings(max_examples=50)
def test_pascal_statement_part_instantiation(instance):
    assert isinstance(instance, pascal_statement_part)

@given(instance=pascal_declaration_part_strategy)
@settings(max_examples=50)
def test_pascal_declaration_part_instantiation(instance):
    assert isinstance(instance, pascal_declaration_part)

@given(instance=pascal_procedure_block_strategy)
@settings(max_examples=50)
def test_pascal_procedure_block_instantiation(instance):
    assert isinstance(instance, pascal_procedure_block)

@given(instance=pascal_identifier_list_strategy)
@settings(max_examples=50)
def test_pascal_identifier_list_instantiation(instance):
    assert isinstance(instance, pascal_identifier_list)



@given(instance=pascal_identifier_list_strategy)
def test_pascal_identifier_list_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=pascal_block_strategy)
@settings(max_examples=50)
def test_pascal_block_instantiation(instance):
    assert isinstance(instance, pascal_block)

@given(instance=pascal_program_heading_strategy)
@settings(max_examples=50)
def test_pascal_program_heading_instantiation(instance):
    assert isinstance(instance, pascal_program_heading)



@given(instance=pascal_program_heading_strategy)
def test_pascal_program_heading_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=pascal_program_strategy)
@settings(max_examples=50)
def test_pascal_program_instantiation(instance):
    assert isinstance(instance, pascal_program)

@given(instance=pascal_bound_specification_strategy)
@settings(max_examples=50)
def test_pascal_bound_specification_instantiation(instance):
    assert isinstance(instance, pascal_bound_specification)

@given(instance=pascal_unpacked_conformant_array_schema_strategy)
@settings(max_examples=50)
def test_pascal_unpacked_conformant_array_schema_instantiation(instance):
    assert isinstance(instance, pascal_unpacked_conformant_array_schema)

@given(instance=pascal_packed_conformant_array_schema_strategy)
@settings(max_examples=50)
def test_pascal_packed_conformant_array_schema_instantiation(instance):
    assert isinstance(instance, pascal_packed_conformant_array_schema)

@given(instance=pascal_conformant_array_schema_strategy)
@settings(max_examples=50)
def test_pascal_conformant_array_schema_instantiation(instance):
    assert isinstance(instance, pascal_conformant_array_schema)

@given(instance=output_list_strategy)
@settings(max_examples=50)
def test_output_list_instantiation(instance):
    assert isinstance(instance, output_list)

@given(instance=pascal_output_value_strategy)
@settings(max_examples=50)
def test_pascal_output_value_instantiation(instance):
    assert isinstance(instance, pascal_output_value)

@given(instance=pascal_output_list_strategy)
@settings(max_examples=50)
def test_pascal_output_list_instantiation(instance):
    assert isinstance(instance, pascal_output_list)

@given(instance=pascal_ordinal_type_identifier_strategy)
@settings(max_examples=50)
def test_pascal_ordinal_type_identifier_instantiation(instance):
    assert isinstance(instance, pascal_ordinal_type_identifier)

@given(instance=pascal_formal_parameter_section_strategy)
@settings(max_examples=50)
def test_pascal_formal_parameter_section_instantiation(instance):
    assert isinstance(instance, pascal_formal_parameter_section)

@given(instance=pascal_formal_parameter_list_strategy)
@settings(max_examples=50)
def test_pascal_formal_parameter_list_instantiation(instance):
    assert isinstance(instance, pascal_formal_parameter_list)

@given(instance=pascal_parameter_type_strategy)
@settings(max_examples=50)
def test_pascal_parameter_type_instantiation(instance):
    assert isinstance(instance, pascal_parameter_type)

@given(instance=pascal_result_type_strategy)
@settings(max_examples=50)
def test_pascal_result_type_instantiation(instance):
    assert isinstance(instance, pascal_result_type)

@given(instance=pascal_function_parameter_section_strategy)
@settings(max_examples=50)
def test_pascal_function_parameter_section_instantiation(instance):
    assert isinstance(instance, pascal_function_parameter_section)

@given(instance=pascal_procedure_parameter_section_strategy)
@settings(max_examples=50)
def test_pascal_procedure_parameter_section_instantiation(instance):
    assert isinstance(instance, pascal_procedure_parameter_section)

@given(instance=pascal_variable_parameter_section_strategy)
@settings(max_examples=50)
def test_pascal_variable_parameter_section_instantiation(instance):
    assert isinstance(instance, pascal_variable_parameter_section)

@given(instance=pascal_value_parameter_section_strategy)
@settings(max_examples=50)
def test_pascal_value_parameter_section_instantiation(instance):
    assert isinstance(instance, pascal_value_parameter_section)

@given(instance=pascal_subrange_type_strategy)
@settings(max_examples=50)
def test_pascal_subrange_type_instantiation(instance):
    assert isinstance(instance, pascal_subrange_type)

@given(instance=pascal_element_type_strategy)
@settings(max_examples=50)
def test_pascal_element_type_instantiation(instance):
    assert isinstance(instance, pascal_element_type)

@given(instance=pascal_index_type_strategy)
@settings(max_examples=50)
def test_pascal_index_type_instantiation(instance):
    assert isinstance(instance, pascal_index_type)

@given(instance=pascal_compiler_defined_directives_strategy)
@settings(max_examples=50)
def test_pascal_compiler_defined_directives_instantiation(instance):
    assert isinstance(instance, pascal_compiler_defined_directives)

@given(instance=pascal_variable_declaration_strategy)
@settings(max_examples=50)
def test_pascal_variable_declaration_instantiation(instance):
    assert isinstance(instance, pascal_variable_declaration)

@given(instance=pascal_upper_bound_strategy)
@settings(max_examples=50)
def test_pascal_upper_bound_instantiation(instance):
    assert isinstance(instance, pascal_upper_bound)

@given(instance=pascal_lower_bound_strategy)
@settings(max_examples=50)
def test_pascal_lower_bound_instantiation(instance):
    assert isinstance(instance, pascal_lower_bound)

@given(instance=pascal_enumerated_type_strategy)
@settings(max_examples=50)
def test_pascal_enumerated_type_instantiation(instance):
    assert isinstance(instance, pascal_enumerated_type)

@given(instance=pascal_file_component_type_strategy)
@settings(max_examples=50)
def test_pascal_file_component_type_instantiation(instance):
    assert isinstance(instance, pascal_file_component_type)

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

@given(instance=pascal_array_type_strategy)
@settings(max_examples=50)
def test_pascal_array_type_instantiation(instance):
    assert isinstance(instance, pascal_array_type)

@given(instance=pascal_unpacked_structured_type_strategy)
@settings(max_examples=50)
def test_pascal_unpacked_structured_type_instantiation(instance):
    assert isinstance(instance, pascal_unpacked_structured_type)

@given(instance=pascal_variant_strategy)
@settings(max_examples=50)
def test_pascal_variant_instantiation(instance):
    assert isinstance(instance, pascal_variant)

@given(instance=pascal_tag_field_strategy)
@settings(max_examples=50)
def test_pascal_tag_field_instantiation(instance):
    assert isinstance(instance, pascal_tag_field)

@given(instance=pascal_record_section_strategy)
@settings(max_examples=50)
def test_pascal_record_section_instantiation(instance):
    assert isinstance(instance, pascal_record_section)

@given(instance=pascal_variant_part_strategy)
@settings(max_examples=50)
def test_pascal_variant_part_instantiation(instance):
    assert isinstance(instance, pascal_variant_part)

@given(instance=pascal_fixed_part_strategy)
@settings(max_examples=50)
def test_pascal_fixed_part_instantiation(instance):
    assert isinstance(instance, pascal_fixed_part)

@given(instance=pascal_field_list_strategy)
@settings(max_examples=50)
def test_pascal_field_list_instantiation(instance):
    assert isinstance(instance, pascal_field_list)

@given(instance=pascal_base_type_strategy)
@settings(max_examples=50)
def test_pascal_base_type_instantiation(instance):
    assert isinstance(instance, pascal_base_type)

@given(instance=pascal_function_identification_strategy)
@settings(max_examples=50)
def test_pascal_function_identification_instantiation(instance):
    assert isinstance(instance, pascal_function_identification)

@given(instance=pascal_function_body_strategy)
@settings(max_examples=50)
def test_pascal_function_body_instantiation(instance):
    assert isinstance(instance, pascal_function_body)

@given(instance=pascal_function_heading_strategy)
@settings(max_examples=50)
def test_pascal_function_heading_instantiation(instance):
    assert isinstance(instance, pascal_function_heading)

@given(instance=pascal_procedure_identification_strategy)
@settings(max_examples=50)
def test_pascal_procedure_identification_instantiation(instance):
    assert isinstance(instance, pascal_procedure_identification)

@given(instance=pascal_directive_strategy)
@settings(max_examples=50)
def test_pascal_directive_instantiation(instance):
    assert isinstance(instance, pascal_directive)

@given(instance=pascal_type_identifier_strategy)
@settings(max_examples=50)
def test_pascal_type_identifier_instantiation(instance):
    assert isinstance(instance, pascal_type_identifier)

@given(instance=pascal_pointer_type_strategy)
@settings(max_examples=50)
def test_pascal_pointer_type_instantiation(instance):
    assert isinstance(instance, pascal_pointer_type)

@given(instance=pascal_structured_type_strategy)
@settings(max_examples=50)
def test_pascal_structured_type_instantiation(instance):
    assert isinstance(instance, pascal_structured_type)

@given(instance=pascal_simple_type_strategy)
@settings(max_examples=50)
def test_pascal_simple_type_instantiation(instance):
    assert isinstance(instance, pascal_simple_type)

@given(instance=pascal_type_strategy)
@settings(max_examples=50)
def test_pascal_type_instantiation(instance):
    assert isinstance(instance, pascal_type)

@given(instance=pascal_type_definition_strategy)
@settings(max_examples=50)
def test_pascal_type_definition_instantiation(instance):
    assert isinstance(instance, pascal_type_definition)

@given(instance=pascal_constant_definition_strategy)
@settings(max_examples=50)
def test_pascal_constant_definition_instantiation(instance):
    assert isinstance(instance, pascal_constant_definition)

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

@given(instance=pascal_procedure_body_strategy)
@settings(max_examples=50)
def test_pascal_procedure_body_instantiation(instance):
    assert isinstance(instance, pascal_procedure_body)

@given(instance=pascal_procedure_heading_strategy)
@settings(max_examples=50)
def test_pascal_procedure_heading_instantiation(instance):
    assert isinstance(instance, pascal_procedure_heading)

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

@given(instance=pascal_final_expression_strategy)
@settings(max_examples=50)
def test_pascal_final_expression_instantiation(instance):
    assert isinstance(instance, pascal_final_expression)

@given(instance=pascal_initial_expression_strategy)
@settings(max_examples=50)
def test_pascal_initial_expression_instantiation(instance):
    assert isinstance(instance, pascal_initial_expression)

@given(instance=pascal_expression_list_strategy)
@settings(max_examples=50)
def test_pascal_expression_list_instantiation(instance):
    assert isinstance(instance, pascal_expression_list)

@given(instance=pascal_entire_variable_strategy)
@settings(max_examples=50)
def test_pascal_entire_variable_instantiation(instance):
    assert isinstance(instance, pascal_entire_variable)

@given(instance=pascal_constant_strategy)
@settings(max_examples=50)
def test_pascal_constant_instantiation(instance):
    assert isinstance(instance, pascal_constant)



@given(instance=pascal_constant_strategy)
def test_pascal_constant_sign_setter(instance):
    original = instance.sign
    instance.sign = original
    assert instance.sign == original



@given(instance=pascal_constant_strategy)
def test_pascal_constant_boolean_setter(instance):
    original = instance.boolean
    instance.boolean = original
    assert instance.boolean == original



@given(instance=pascal_constant_strategy)
def test_pascal_constant_strings_setter(instance):
    original = instance.strings
    instance.strings = original
    assert instance.strings == original

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

@given(instance=pascal_factor_strategy)
@settings(max_examples=50)
def test_pascal_factor_instantiation(instance):
    assert isinstance(instance, pascal_factor)



@given(instance=pascal_factor_strategy)
def test_pascal_factor_boolean_setter(instance):
    original = instance.boolean
    instance.boolean = original
    assert instance.boolean == original



@given(instance=pascal_factor_strategy)
def test_pascal_factor_strings_setter(instance):
    original = instance.strings
    instance.strings = original
    assert instance.strings == original

@given(instance=pascal_addition_operator_strategy)
@settings(max_examples=50)
def test_pascal_addition_operator_instantiation(instance):
    assert isinstance(instance, pascal_addition_operator)



@given(instance=pascal_addition_operator_strategy)
def test_pascal_addition_operator_sign_setter(instance):
    original = instance.sign
    instance.sign = original
    assert instance.sign == original

@given(instance=pascal_term_strategy)
@settings(max_examples=50)
def test_pascal_term_instantiation(instance):
    assert isinstance(instance, pascal_term)



@given(instance=pascal_term_strategy)
def test_pascal_term_multiplication_operator_setter(instance):
    original = instance.multiplication_operator
    instance.multiplication_operator = original
    assert instance.multiplication_operator == original
