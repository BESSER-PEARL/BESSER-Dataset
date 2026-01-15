####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
pascal_Begin = Class(name="pascal::Begin")
pascal_program = Class(name="pascal::program")
pascal_statement_sequence = Class(name="pascal::statement::sequence")
pascal_program_heading = Class(name="pascal::program::heading")
pascal_block = Class(name="pascal::block")
pascal_identifier_list = Class(name="pascal::identifier::list")
pascal_procedure_block = Class(name="pascal::procedure::block")
pascal_declaration_part = Class(name="pascal::declaration::part")
pascal_statement_part = Class(name="pascal::statement::part")
pascal_function_block = Class(name="pascal::function::block")
pascal_identifier = Class(name="pascal::identifier")
pascal_actual_parameter_list = Class(name="pascal::actual::parameter::list")
pascal_actual_parameter = Class(name="pascal::actual::parameter")
pascal_statement = Class(name="pascal::statement")
pascal_label = Class(name="pascal::label")
pascal_simple_statement = Class(name="pascal::simple::statement")
pascal_structured_statement = Class(name="pascal::structured::statement")
pascal_assignment_statement = Class(name="pascal::assignment::statement")
pascal_procedure_statement = Class(name="pascal::procedure::statement")
pascal_goto_statement = Class(name="pascal::goto::statement")
pascal_expression = Class(name="pascal::expression")
pascal_actual_value = Class(name="pascal::actual::value")
pascal_actual_variable = Class(name="pascal::actual::variable")
pascal_actual_procedure = Class(name="pascal::actual::procedure")
pascal_actual_function = Class(name="pascal::actual::function")
pascal_variable = Class(name="pascal::variable")
pascal_factor = Class(name="pascal::factor")
output_value = Class(name="output::value")
pascal_simple_expression = Class(name="pascal::simple::expression")
pascal_term = Class(name="pascal::term")
pascal_addition_operator = Class(name="pascal::addition::operator")
pascal_element_list = Class(name="pascal::element::list")
pascal_number = Class(name="pascal::number")
pascal_set = Class(name="pascal::set")
pascal_function_designator = Class(name="pascal::function::designator")
pascal_integer_number = Class(name="pascal::integer::number")
pascal_real_number = Class(name="pascal::real::number")
pascal_repetitive_statement = Class(name="pascal::repetitive::statement")
pascal_digit_sequence = Class(name="pascal::digit::sequence")
pascal_entire_variable = Class(name="pascal::entire::variable")
pascal_expression_list = Class(name="pascal::expression::list")
pascal_scale_factor = Class(name="pascal::scale::factor")
pascal_compound_statement = Class(name="pascal::compound::statement")
pascal_conditional_statement = Class(name="pascal::conditional::statement")
pascal_with_statement = Class(name="pascal::with::statement")
pascal_if_statement = Class(name="pascal::if::statement")
pascal_case_statement = Class(name="pascal::case::statement")
pascal_case_limb = Class(name="pascal::case::limb")
pascal_case_label_list = Class(name="pascal::case::label::list")
pascal_constant = Class(name="pascal::constant")
pascal_while_statement = Class(name="pascal::while::statement")
pascal_repeat_statement = Class(name="pascal::repeat::statement")
pascal_for_statement = Class(name="pascal::for::statement")
pascal_initial_expression = Class(name="pascal::initial::expression")
pascal_final_expression = Class(name="pascal::final::expression")
pascal_constant_definition_part = Class(name="pascal::constant::definition::part")
pascal_label_declaration_part = Class(name="pascal::label::declaration::part")
pascal_type_definition_part = Class(name="pascal::type::definition::part")
pascal_variable_declaration_part = Class(name="pascal::variable::declaration::part")
pascal_procedure_heading = Class(name="pascal::procedure::heading")
pascal_procedure_body = Class(name="pascal::procedure::body")
pascal_directive = Class(name="pascal::directive")
pascal_procedure_identification = Class(name="pascal::procedure::identification")
pascal_function_heading = Class(name="pascal::function::heading")
pascal_function_body = Class(name="pascal::function::body")
pascal_function_identification = Class(name="pascal::function::identification")
pascal_constant_definition = Class(name="pascal::constant::definition")
pascal_type_definition = Class(name="pascal::type::definition")
pascal_type = Class(name="pascal::type")
pascal_simple_type = Class(name="pascal::simple::type")
pascal_structured_type = Class(name="pascal::structured::type")
pascal_pointer_type = Class(name="pascal::pointer::type")
pascal_type_identifier = Class(name="pascal::type::identifier")
pascal_unpacked_structured_type = Class(name="pascal::unpacked::structured::type")
pascal_array_type = Class(name="pascal::array::type")
pascal_record_type = Class(name="pascal::record::type")
pascal_set_type = Class(name="pascal::set::type")
pascal_file_type = Class(name="pascal::file::type")
pascal_file_component_type = Class(name="pascal::file::component::type")
pascal_base_type = Class(name="pascal::base::type")
pascal_field_list = Class(name="pascal::field::list")
pascal_variant_part = Class(name="pascal::variant::part")
pascal_fixed_part = Class(name="pascal::fixed::part")
pascal_record_section = Class(name="pascal::record::section")
pascal_tag_field = Class(name="pascal::tag::field")
pascal_variant = Class(name="pascal::variant")
pascal_index_type = Class(name="pascal::index::type")
pascal_element_type = Class(name="pascal::element::type")
pascal_subrange_type = Class(name="pascal::subrange::type")
pascal_enumerated_type = Class(name="pascal::enumerated::type")
pascal_lower_bound = Class(name="pascal::lower::bound")
pascal_upper_bound = Class(name="pascal::upper::bound")
pascal_variable_declaration = Class(name="pascal::variable::declaration")
pascal_compiler_defined_directives = Class(name="pascal::compiler::defined::directives")
pascal_formal_parameter_list = Class(name="pascal::formal::parameter::list")
pascal_formal_parameter_section = Class(name="pascal::formal::parameter::section")
pascal_value_parameter_section = Class(name="pascal::value::parameter::section")
pascal_variable_parameter_section = Class(name="pascal::variable::parameter::section")
pascal_procedure_parameter_section = Class(name="pascal::procedure::parameter::section")
pascal_function_parameter_section = Class(name="pascal::function::parameter::section")
pascal_result_type = Class(name="pascal::result::type")
pascal_parameter_type = Class(name="pascal::parameter::type")
pascal_conformant_array_schema = Class(name="pascal::conformant::array::schema")
pascal_packed_conformant_array_schema = Class(name="pascal::packed::conformant::array::schema")
pascal_unpacked_conformant_array_schema = Class(name="pascal::unpacked::conformant::array::schema")
pascal_bound_specification = Class(name="pascal::bound::specification")
pascal_ordinal_type_identifier = Class(name="pascal::ordinal::type::identifier")
pascal_output_list = Class(name="pascal::output::list")
pascal_output_value = Class(name="pascal::output::value")
output_list = Class(name="output::list")

# pascal_Begin class attributes and methods

# pascal_program class attributes and methods

# pascal_statement_sequence class attributes and methods

# pascal_program_heading class attributes and methods
pascal_program_heading_identifier: Property = Property(name="identifier", type=StringType)
pascal_program_heading.attributes={pascal_program_heading_identifier}

# pascal_block class attributes and methods

# pascal_identifier_list class attributes and methods
pascal_identifier_list_identifier: Property = Property(name="identifier", type=StringType)
pascal_identifier_list.attributes={pascal_identifier_list_identifier}

# pascal_procedure_block class attributes and methods

# pascal_declaration_part class attributes and methods

# pascal_statement_part class attributes and methods

# pascal_function_block class attributes and methods

# pascal_identifier class attributes and methods
pascal_identifier_identifier: Property = Property(name="identifier", type=StringType)
pascal_identifier.attributes={pascal_identifier_identifier}

# pascal_actual_parameter_list class attributes and methods

# pascal_actual_parameter class attributes and methods

# pascal_statement class attributes and methods

# pascal_label class attributes and methods

# pascal_simple_statement class attributes and methods

# pascal_structured_statement class attributes and methods

# pascal_assignment_statement class attributes and methods

# pascal_procedure_statement class attributes and methods

# pascal_goto_statement class attributes and methods

# pascal_expression class attributes and methods
pascal_expression_relational_operator: Property = Property(name="relational_operator", type=StringType)
pascal_expression.attributes={pascal_expression_relational_operator}

# pascal_actual_value class attributes and methods

# pascal_actual_variable class attributes and methods

# pascal_actual_procedure class attributes and methods

# pascal_actual_function class attributes and methods

# pascal_variable class attributes and methods

# pascal_factor class attributes and methods
pascal_factor_strings: Property = Property(name="strings", type=StringType)
pascal_factor_boolean: Property = Property(name="boolean", type=StringType)
pascal_factor.attributes={pascal_factor_strings, pascal_factor_boolean}

# output_value class attributes and methods

# pascal_simple_expression class attributes and methods
pascal_simple_expression_sign: Property = Property(name="sign", type=StringType)
pascal_simple_expression.attributes={pascal_simple_expression_sign}

# pascal_term class attributes and methods
pascal_term_multiplication_operator: Property = Property(name="multiplication_operator", type=StringType)
pascal_term.attributes={pascal_term_multiplication_operator}

# pascal_addition_operator class attributes and methods
pascal_addition_operator_sign: Property = Property(name="sign", type=StringType)
pascal_addition_operator.attributes={pascal_addition_operator_sign}

# pascal_element_list class attributes and methods

# pascal_number class attributes and methods

# pascal_set class attributes and methods

# pascal_function_designator class attributes and methods

# pascal_integer_number class attributes and methods

# pascal_real_number class attributes and methods

# pascal_repetitive_statement class attributes and methods

# pascal_digit_sequence class attributes and methods
pascal_digit_sequence_sign: Property = Property(name="sign", type=StringType)
pascal_digit_sequence_unsigned_digit_sequence: Property = Property(name="unsigned_digit_sequence", type=StringType)
pascal_digit_sequence.attributes={pascal_digit_sequence_unsigned_digit_sequence, pascal_digit_sequence_sign}

# pascal_entire_variable class attributes and methods

# pascal_expression_list class attributes and methods

# pascal_scale_factor class attributes and methods
pascal_scale_factor_sign: Property = Property(name="sign", type=StringType)
pascal_scale_factor.attributes={pascal_scale_factor_sign}

# pascal_compound_statement class attributes and methods

# pascal_conditional_statement class attributes and methods

# pascal_with_statement class attributes and methods

# pascal_if_statement class attributes and methods

# pascal_case_statement class attributes and methods

# pascal_case_limb class attributes and methods

# pascal_case_label_list class attributes and methods

# pascal_constant class attributes and methods
pascal_constant_sign: Property = Property(name="sign", type=StringType)
pascal_constant_strings: Property = Property(name="strings", type=StringType)
pascal_constant_boolean: Property = Property(name="boolean", type=StringType)
pascal_constant.attributes={pascal_constant_sign, pascal_constant_strings, pascal_constant_boolean}

# pascal_while_statement class attributes and methods

# pascal_repeat_statement class attributes and methods

# pascal_for_statement class attributes and methods

# pascal_initial_expression class attributes and methods

# pascal_final_expression class attributes and methods

# pascal_constant_definition_part class attributes and methods

# pascal_label_declaration_part class attributes and methods

# pascal_type_definition_part class attributes and methods

# pascal_variable_declaration_part class attributes and methods

# pascal_procedure_heading class attributes and methods

# pascal_procedure_body class attributes and methods

# pascal_directive class attributes and methods

# pascal_procedure_identification class attributes and methods

# pascal_function_heading class attributes and methods

# pascal_function_body class attributes and methods

# pascal_function_identification class attributes and methods

# pascal_constant_definition class attributes and methods

# pascal_type_definition class attributes and methods

# pascal_type class attributes and methods

# pascal_simple_type class attributes and methods

# pascal_structured_type class attributes and methods

# pascal_pointer_type class attributes and methods

# pascal_type_identifier class attributes and methods

# pascal_unpacked_structured_type class attributes and methods

# pascal_array_type class attributes and methods

# pascal_record_type class attributes and methods

# pascal_set_type class attributes and methods

# pascal_file_type class attributes and methods

# pascal_file_component_type class attributes and methods

# pascal_base_type class attributes and methods

# pascal_field_list class attributes and methods

# pascal_variant_part class attributes and methods

# pascal_fixed_part class attributes and methods

# pascal_record_section class attributes and methods

# pascal_tag_field class attributes and methods

# pascal_variant class attributes and methods

# pascal_index_type class attributes and methods

# pascal_element_type class attributes and methods

# pascal_subrange_type class attributes and methods

# pascal_enumerated_type class attributes and methods

# pascal_lower_bound class attributes and methods

# pascal_upper_bound class attributes and methods

# pascal_variable_declaration class attributes and methods

# pascal_compiler_defined_directives class attributes and methods

# pascal_formal_parameter_list class attributes and methods

# pascal_formal_parameter_section class attributes and methods

# pascal_value_parameter_section class attributes and methods

# pascal_variable_parameter_section class attributes and methods

# pascal_procedure_parameter_section class attributes and methods

# pascal_function_parameter_section class attributes and methods

# pascal_result_type class attributes and methods

# pascal_parameter_type class attributes and methods

# pascal_conformant_array_schema class attributes and methods

# pascal_packed_conformant_array_schema class attributes and methods

# pascal_unpacked_conformant_array_schema class attributes and methods

# pascal_bound_specification class attributes and methods

# pascal_ordinal_type_identifier class attributes and methods

# pascal_output_list class attributes and methods

# pascal_output_value class attributes and methods

# output_list class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="pascal_program", type=pascal_Begin, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_Begin", type=pascal_program, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement_part12: BinaryAssociation = BinaryAssociation(
    name="statement_part12",
    ends={
        Property(name="pascal_statement_part14", type=pascal_function_block, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_function_block13", type=pascal_statement_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration_part15: BinaryAssociation = BinaryAssociation(
    name="declaration_part15",
    ends={
        Property(name="pascal_declaration_part17", type=pascal_block, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_block16", type=pascal_declaration_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement_part18: BinaryAssociation = BinaryAssociation(
    name="statement_part18",
    ends={
        Property(name="pascal_statement_part20", type=pascal_block, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_block19", type=pascal_statement_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement_sequence21: BinaryAssociation = BinaryAssociation(
    name="statement_sequence21",
    ends={
        Property(name="pascal_statement_sequence", type=pascal_statement_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_statement_part22", type=pascal_statement_sequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
program_heading1: BinaryAssociation = BinaryAssociation(
    name="program_heading1",
    ends={
        Property(name="pascal_program_heading", type=pascal_program, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_program2", type=pascal_program_heading, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block3: BinaryAssociation = BinaryAssociation(
    name="block3",
    ends={
        Property(name="pascal_block", type=pascal_program, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_program4", type=pascal_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier_list5: BinaryAssociation = BinaryAssociation(
    name="identifier_list5",
    ends={
        Property(name="pascal_identifier_list", type=pascal_program_heading, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_program_heading6", type=pascal_identifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration_part7: BinaryAssociation = BinaryAssociation(
    name="declaration_part7",
    ends={
        Property(name="pascal_declaration_part", type=pascal_procedure_block, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_procedure_block", type=pascal_declaration_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement_part8: BinaryAssociation = BinaryAssociation(
    name="statement_part8",
    ends={
        Property(name="pascal_statement_part", type=pascal_procedure_block, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_procedure_block9", type=pascal_statement_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration_part10: BinaryAssociation = BinaryAssociation(
    name="declaration_part10",
    ends={
        Property(name="pascal_declaration_part11", type=pascal_function_block, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_function_block", type=pascal_declaration_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
procedure_identifier40: BinaryAssociation = BinaryAssociation(
    name="procedure_identifier40",
    ends={
        Property(name="pascal_identifier", type=pascal_procedure_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_procedure_statement41", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actual_parameter_list42: BinaryAssociation = BinaryAssociation(
    name="actual_parameter_list42",
    ends={
        Property(name="pascal_actual_parameter_list", type=pascal_procedure_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_procedure_statement43", type=pascal_actual_parameter_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actual_parameter44: BinaryAssociation = BinaryAssociation(
    name="actual_parameter44",
    ends={
        Property(name="pascal_actual_parameter", type=pascal_actual_parameter_list, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_actual_parameter_list45", type=pascal_actual_parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement23: BinaryAssociation = BinaryAssociation(
    name="statement23",
    ends={
        Property(name="pascal_statement", type=pascal_statement_sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_statement_sequence24", type=pascal_statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label25: BinaryAssociation = BinaryAssociation(
    name="label25",
    ends={
        Property(name="pascal_label", type=pascal_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_statement26", type=pascal_label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simple_statement27: BinaryAssociation = BinaryAssociation(
    name="simple_statement27",
    ends={
        Property(name="pascal_simple_statement", type=pascal_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_statement28", type=pascal_simple_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structured_statement29: BinaryAssociation = BinaryAssociation(
    name="structured_statement29",
    ends={
        Property(name="pascal_structured_statement", type=pascal_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_statement30", type=pascal_structured_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment_statement31: BinaryAssociation = BinaryAssociation(
    name="assignment_statement31",
    ends={
        Property(name="pascal_assignment_statement", type=pascal_simple_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simple_statement32", type=pascal_assignment_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
procedure_statement33: BinaryAssociation = BinaryAssociation(
    name="procedure_statement33",
    ends={
        Property(name="pascal_procedure_statement", type=pascal_simple_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simple_statement34", type=pascal_procedure_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
goto_statement35: BinaryAssociation = BinaryAssociation(
    name="goto_statement35",
    ends={
        Property(name="pascal_goto_statement", type=pascal_simple_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simple_statement36", type=pascal_goto_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
label37: BinaryAssociation = BinaryAssociation(
    name="label37",
    ends={
        Property(name="pascal_label39", type=pascal_goto_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_goto_statement38", type=pascal_label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression62: BinaryAssociation = BinaryAssociation(
    name="expression62",
    ends={
        Property(name="pascal_expression", type=pascal_actual_value, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_actual_value63", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable64: BinaryAssociation = BinaryAssociation(
    name="variable64",
    ends={
        Property(name="pascal_variable66", type=pascal_assignment_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_assignment_statement65", type=pascal_variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actual_value46: BinaryAssociation = BinaryAssociation(
    name="actual_value46",
    ends={
        Property(name="pascal_actual_value", type=pascal_actual_parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_actual_parameter47", type=pascal_actual_value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actual_variable48: BinaryAssociation = BinaryAssociation(
    name="actual_variable48",
    ends={
        Property(name="pascal_actual_variable", type=pascal_actual_parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_actual_parameter49", type=pascal_actual_variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actual_procedure50: BinaryAssociation = BinaryAssociation(
    name="actual_procedure50",
    ends={
        Property(name="pascal_actual_procedure", type=pascal_actual_parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_actual_parameter51", type=pascal_actual_procedure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actual_function52: BinaryAssociation = BinaryAssociation(
    name="actual_function52",
    ends={
        Property(name="pascal_actual_function", type=pascal_actual_parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_actual_parameter53", type=pascal_actual_function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function_identifier54: BinaryAssociation = BinaryAssociation(
    name="function_identifier54",
    ends={
        Property(name="pascal_identifier56", type=pascal_actual_function, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_actual_function55", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
procedure_identifier57: BinaryAssociation = BinaryAssociation(
    name="procedure_identifier57",
    ends={
        Property(name="pascal_identifier59", type=pascal_actual_procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_actual_procedure58", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable60: BinaryAssociation = BinaryAssociation(
    name="variable60",
    ends={
        Property(name="pascal_variable", type=pascal_actual_variable, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_actual_variable61", type=pascal_variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
factor82: BinaryAssociation = BinaryAssociation(
    name="factor82",
    ends={
        Property(name="pascal_factor", type=pascal_term, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_term83", type=pascal_factor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function_identifier67: BinaryAssociation = BinaryAssociation(
    name="function_identifier67",
    ends={
        Property(name="pascal_identifier69", type=pascal_assignment_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_assignment_statement68", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression70: BinaryAssociation = BinaryAssociation(
    name="expression70",
    ends={
        Property(name="pascal_expression72", type=pascal_assignment_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_assignment_statement71", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simple_expression73: BinaryAssociation = BinaryAssociation(
    name="simple_expression73",
    ends={
        Property(name="pascal_simple_expression", type=pascal_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_expression74", type=pascal_simple_expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression76: BinaryAssociation = BinaryAssociation(
    name="expression76",
    ends={
        Property(name="pascal_expression77", type=pascal_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_expression75", type=pascal_expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
term78: BinaryAssociation = BinaryAssociation(
    name="term78",
    ends={
        Property(name="pascal_term", type=pascal_simple_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simple_expression79", type=pascal_term, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
addition_operator80: BinaryAssociation = BinaryAssociation(
    name="addition_operator80",
    ends={
        Property(name="pascal_addition_operator", type=pascal_simple_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simple_expression81", type=pascal_addition_operator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function_identifier102: BinaryAssociation = BinaryAssociation(
    name="function_identifier102",
    ends={
        Property(name="pascal_identifier104", type=pascal_function_designator, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_function_designator103", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actual_parameter_list105: BinaryAssociation = BinaryAssociation(
    name="actual_parameter_list105",
    ends={
        Property(name="pascal_actual_parameter_list107", type=pascal_function_designator, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_function_designator106", type=pascal_actual_parameter_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
element_list108: BinaryAssociation = BinaryAssociation(
    name="element_list108",
    ends={
        Property(name="pascal_element_list", type=pascal_set, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_set109", type=pascal_element_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable84: BinaryAssociation = BinaryAssociation(
    name="variable84",
    ends={
        Property(name="pascal_variable86", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor85", type=pascal_variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
number87: BinaryAssociation = BinaryAssociation(
    name="number87",
    ends={
        Property(name="pascal_number", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor88", type=pascal_number, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
set89: BinaryAssociation = BinaryAssociation(
    name="set89",
    ends={
        Property(name="pascal_set", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor90", type=pascal_set, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier91: BinaryAssociation = BinaryAssociation(
    name="identifier91",
    ends={
        Property(name="pascal_identifier93", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor92", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function_designator94: BinaryAssociation = BinaryAssociation(
    name="function_designator94",
    ends={
        Property(name="pascal_function_designator", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor95", type=pascal_function_designator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression96: BinaryAssociation = BinaryAssociation(
    name="expression96",
    ends={
        Property(name="pascal_expression98", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor97", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
factor100: BinaryAssociation = BinaryAssociation(
    name="factor100",
    ends={
        Property(name="pascal_factor101", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor99", type=pascal_factor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression110: BinaryAssociation = BinaryAssociation(
    name="expression110",
    ends={
        Property(name="pascal_expression112", type=pascal_element_list, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_element_list111", type=pascal_expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
integer_number113: BinaryAssociation = BinaryAssociation(
    name="integer_number113",
    ends={
        Property(name="pascal_integer_number", type=pascal_number, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_number114", type=pascal_integer_number, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
real_number115: BinaryAssociation = BinaryAssociation(
    name="real_number115",
    ends={
        Property(name="pascal_real_number", type=pascal_number, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_number116", type=pascal_real_number, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
digit_sequence124: BinaryAssociation = BinaryAssociation(
    name="digit_sequence124",
    ends={
        Property(name="pascal_scale_factor125", type=pascal_digit_sequence, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="pascal_digit_sequence126", type=pascal_scale_factor, multiplicity=Multiplicity(1, 1))
    }
)
digit_sequence117: BinaryAssociation = BinaryAssociation(
    name="digit_sequence117",
    ends={
        Property(name="pascal_digit_sequence", type=pascal_real_number, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_real_number118", type=pascal_digit_sequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entire_variable127: BinaryAssociation = BinaryAssociation(
    name="entire_variable127",
    ends={
        Property(name="pascal_entire_variable", type=pascal_variable, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variable128", type=pascal_entire_variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
digit_sequence2119: BinaryAssociation = BinaryAssociation(
    name="digit_sequence2119",
    ends={
        Property(name="pascal_digit_sequence121", type=pascal_real_number, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_real_number120", type=pascal_digit_sequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression_list129: BinaryAssociation = BinaryAssociation(
    name="expression_list129",
    ends={
        Property(name="pascal_expression_list", type=pascal_variable, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variable130", type=pascal_expression_list, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scale_factor122: BinaryAssociation = BinaryAssociation(
    name="scale_factor122",
    ends={
        Property(name="pascal_scale_factor", type=pascal_real_number, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_real_number123", type=pascal_scale_factor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
field_identifier131: BinaryAssociation = BinaryAssociation(
    name="field_identifier131",
    ends={
        Property(name="pascal_identifier133", type=pascal_variable, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variable132", type=pascal_identifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifier134: BinaryAssociation = BinaryAssociation(
    name="identifier134",
    ends={
        Property(name="pascal_identifier136", type=pascal_entire_variable, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_entire_variable135", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression137: BinaryAssociation = BinaryAssociation(
    name="expression137",
    ends={
        Property(name="pascal_expression139", type=pascal_expression_list, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_expression_list138", type=pascal_expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
integer_number140: BinaryAssociation = BinaryAssociation(
    name="integer_number140",
    ends={
        Property(name="pascal_integer_number142", type=pascal_label, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_label141", type=pascal_integer_number, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
digit_sequence143: BinaryAssociation = BinaryAssociation(
    name="digit_sequence143",
    ends={
        Property(name="pascal_digit_sequence145", type=pascal_integer_number, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_integer_number144", type=pascal_digit_sequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
compound_statement146: BinaryAssociation = BinaryAssociation(
    name="compound_statement146",
    ends={
        Property(name="pascal_compound_statement", type=pascal_structured_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_structured_statement147", type=pascal_compound_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
case_label_list169: BinaryAssociation = BinaryAssociation(
    name="case_label_list169",
    ends={
        Property(name="pascal_case_label_list", type=pascal_case_limb, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_case_limb170", type=pascal_case_label_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
repetitive_statement148: BinaryAssociation = BinaryAssociation(
    name="repetitive_statement148",
    ends={
        Property(name="pascal_repetitive_statement", type=pascal_structured_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_structured_statement149", type=pascal_repetitive_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditional_statement150: BinaryAssociation = BinaryAssociation(
    name="conditional_statement150",
    ends={
        Property(name="pascal_conditional_statement", type=pascal_structured_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_structured_statement151", type=pascal_conditional_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
with_statement152: BinaryAssociation = BinaryAssociation(
    name="with_statement152",
    ends={
        Property(name="pascal_with_statement", type=pascal_structured_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_structured_statement153", type=pascal_with_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable154: BinaryAssociation = BinaryAssociation(
    name="variable154",
    ends={
        Property(name="pascal_variable156", type=pascal_with_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_with_statement155", type=pascal_variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement157: BinaryAssociation = BinaryAssociation(
    name="statement157",
    ends={
        Property(name="pascal_statement159", type=pascal_with_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_with_statement158", type=pascal_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
if_statement160: BinaryAssociation = BinaryAssociation(
    name="if_statement160",
    ends={
        Property(name="pascal_if_statement", type=pascal_conditional_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_conditional_statement161", type=pascal_if_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
case_statement162: BinaryAssociation = BinaryAssociation(
    name="case_statement162",
    ends={
        Property(name="pascal_case_statement", type=pascal_conditional_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_conditional_statement163", type=pascal_case_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression164: BinaryAssociation = BinaryAssociation(
    name="expression164",
    ends={
        Property(name="pascal_expression166", type=pascal_case_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_case_statement165", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
case_limb167: BinaryAssociation = BinaryAssociation(
    name="case_limb167",
    ends={
        Property(name="pascal_case_limb", type=pascal_case_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_case_statement168", type=pascal_case_limb, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement171: BinaryAssociation = BinaryAssociation(
    name="statement171",
    ends={
        Property(name="pascal_statement173", type=pascal_case_limb, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_case_limb172", type=pascal_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant174: BinaryAssociation = BinaryAssociation(
    name="constant174",
    ends={
        Property(name="pascal_constant", type=pascal_case_label_list, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_case_label_list175", type=pascal_constant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression176: BinaryAssociation = BinaryAssociation(
    name="expression176",
    ends={
        Property(name="pascal_expression178", type=pascal_if_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_if_statement177", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement179: BinaryAssociation = BinaryAssociation(
    name="statement179",
    ends={
        Property(name="pascal_statement181", type=pascal_if_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_if_statement180", type=pascal_statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
while_statement182: BinaryAssociation = BinaryAssociation(
    name="while_statement182",
    ends={
        Property(name="pascal_while_statement", type=pascal_repetitive_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_repetitive_statement183", type=pascal_while_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
repeat_statement184: BinaryAssociation = BinaryAssociation(
    name="repeat_statement184",
    ends={
        Property(name="pascal_repeat_statement", type=pascal_repetitive_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_repetitive_statement185", type=pascal_repeat_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
for_statement186: BinaryAssociation = BinaryAssociation(
    name="for_statement186",
    ends={
        Property(name="pascal_for_statement", type=pascal_repetitive_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_repetitive_statement187", type=pascal_for_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable_identifier188: BinaryAssociation = BinaryAssociation(
    name="variable_identifier188",
    ends={
        Property(name="pascal_identifier190", type=pascal_for_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_for_statement189", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initial_expression191: BinaryAssociation = BinaryAssociation(
    name="initial_expression191",
    ends={
        Property(name="pascal_initial_expression", type=pascal_for_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_for_statement192", type=pascal_initial_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
final_expression193: BinaryAssociation = BinaryAssociation(
    name="final_expression193",
    ends={
        Property(name="pascal_final_expression", type=pascal_for_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_for_statement194", type=pascal_final_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant_definition_part221: BinaryAssociation = BinaryAssociation(
    name="constant_definition_part221",
    ends={
        Property(name="pascal_constant_definition_part", type=pascal_declaration_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_declaration_part222", type=pascal_constant_definition_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement195: BinaryAssociation = BinaryAssociation(
    name="statement195",
    ends={
        Property(name="pascal_statement197", type=pascal_for_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_for_statement196", type=pascal_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression198: BinaryAssociation = BinaryAssociation(
    name="expression198",
    ends={
        Property(name="pascal_expression200", type=pascal_final_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_final_expression199", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression201: BinaryAssociation = BinaryAssociation(
    name="expression201",
    ends={
        Property(name="pascal_expression203", type=pascal_initial_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_initial_expression202", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement_sequence204: BinaryAssociation = BinaryAssociation(
    name="statement_sequence204",
    ends={
        Property(name="pascal_statement_sequence206", type=pascal_repeat_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_repeat_statement205", type=pascal_statement_sequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression207: BinaryAssociation = BinaryAssociation(
    name="expression207",
    ends={
        Property(name="pascal_expression209", type=pascal_repeat_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_repeat_statement208", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression210: BinaryAssociation = BinaryAssociation(
    name="expression210",
    ends={
        Property(name="pascal_expression212", type=pascal_while_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_while_statement211", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement213: BinaryAssociation = BinaryAssociation(
    name="statement213",
    ends={
        Property(name="pascal_statement215", type=pascal_while_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_while_statement214", type=pascal_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement_sequence216: BinaryAssociation = BinaryAssociation(
    name="statement_sequence216",
    ends={
        Property(name="pascal_statement_sequence218", type=pascal_compound_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_compound_statement217", type=pascal_statement_sequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
label_declaration_part219: BinaryAssociation = BinaryAssociation(
    name="label_declaration_part219",
    ends={
        Property(name="pascal_label_declaration_part", type=pascal_declaration_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_declaration_part220", type=pascal_label_declaration_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
label241: BinaryAssociation = BinaryAssociation(
    name="label241",
    ends={
        Property(name="pascal_label243", type=pascal_label_declaration_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_label_declaration_part242", type=pascal_label, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type_definition_part223: BinaryAssociation = BinaryAssociation(
    name="type_definition_part223",
    ends={
        Property(name="pascal_type_definition_part", type=pascal_declaration_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_declaration_part224", type=pascal_type_definition_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable_declaration_part225: BinaryAssociation = BinaryAssociation(
    name="variable_declaration_part225",
    ends={
        Property(name="pascal_variable_declaration_part", type=pascal_declaration_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_declaration_part226", type=pascal_variable_declaration_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
procedure_heading227: BinaryAssociation = BinaryAssociation(
    name="procedure_heading227",
    ends={
        Property(name="pascal_procedure_heading", type=pascal_declaration_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_declaration_part228", type=pascal_procedure_heading, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
procedure_body229: BinaryAssociation = BinaryAssociation(
    name="procedure_body229",
    ends={
        Property(name="pascal_procedure_body", type=pascal_declaration_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_declaration_part230", type=pascal_procedure_body, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
directive231: BinaryAssociation = BinaryAssociation(
    name="directive231",
    ends={
        Property(name="pascal_directive", type=pascal_declaration_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_declaration_part232", type=pascal_directive, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
procedure_identification233: BinaryAssociation = BinaryAssociation(
    name="procedure_identification233",
    ends={
        Property(name="pascal_procedure_identification", type=pascal_declaration_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_declaration_part234", type=pascal_procedure_identification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function_heading235: BinaryAssociation = BinaryAssociation(
    name="function_heading235",
    ends={
        Property(name="pascal_function_heading", type=pascal_declaration_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_declaration_part236", type=pascal_function_heading, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function_body237: BinaryAssociation = BinaryAssociation(
    name="function_body237",
    ends={
        Property(name="pascal_function_body", type=pascal_declaration_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_declaration_part238", type=pascal_function_body, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function_identification239: BinaryAssociation = BinaryAssociation(
    name="function_identification239",
    ends={
        Property(name="pascal_function_identification", type=pascal_declaration_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_declaration_part240", type=pascal_function_identification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type263: BinaryAssociation = BinaryAssociation(
    name="type263",
    ends={
        Property(name="pascal_type_definition264", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="pascal_type", type=pascal_type_definition, multiplicity=Multiplicity(1, 1))
    }
)
constant_definition244: BinaryAssociation = BinaryAssociation(
    name="constant_definition244",
    ends={
        Property(name="pascal_constant_definition", type=pascal_constant_definition_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_constant_definition_part245", type=pascal_constant_definition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifier246: BinaryAssociation = BinaryAssociation(
    name="identifier246",
    ends={
        Property(name="pascal_identifier248", type=pascal_constant_definition, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_constant_definition247", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant249: BinaryAssociation = BinaryAssociation(
    name="constant249",
    ends={
        Property(name="pascal_constant251", type=pascal_constant_definition, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_constant_definition250", type=pascal_constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant_identifier252: BinaryAssociation = BinaryAssociation(
    name="constant_identifier252",
    ends={
        Property(name="pascal_identifier254", type=pascal_constant, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_constant253", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
number255: BinaryAssociation = BinaryAssociation(
    name="number255",
    ends={
        Property(name="pascal_number257", type=pascal_constant, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_constant256", type=pascal_number, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_definition258: BinaryAssociation = BinaryAssociation(
    name="type_definition258",
    ends={
        Property(name="pascal_type_definition", type=pascal_type_definition_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_type_definition_part259", type=pascal_type_definition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifier260: BinaryAssociation = BinaryAssociation(
    name="identifier260",
    ends={
        Property(name="pascal_identifier262", type=pascal_type_definition, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_type_definition261", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simple_type265: BinaryAssociation = BinaryAssociation(
    name="simple_type265",
    ends={
        Property(name="pascal_simple_type", type=pascal_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_type266", type=pascal_simple_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structured_type267: BinaryAssociation = BinaryAssociation(
    name="structured_type267",
    ends={
        Property(name="pascal_structured_type", type=pascal_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_type268", type=pascal_structured_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pointer_type269: BinaryAssociation = BinaryAssociation(
    name="pointer_type269",
    ends={
        Property(name="pascal_pointer_type", type=pascal_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_type270", type=pascal_pointer_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_identifier271: BinaryAssociation = BinaryAssociation(
    name="type_identifier271",
    ends={
        Property(name="pascal_type_identifier", type=pascal_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_type272", type=pascal_type_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier273: BinaryAssociation = BinaryAssociation(
    name="identifier273",
    ends={
        Property(name="pascal_identifier275", type=pascal_type_identifier, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_type_identifier274", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_identifier276: BinaryAssociation = BinaryAssociation(
    name="type_identifier276",
    ends={
        Property(name="pascal_type_identifier278", type=pascal_pointer_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_pointer_type277", type=pascal_type_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unpacked_structured_type279: BinaryAssociation = BinaryAssociation(
    name="unpacked_structured_type279",
    ends={
        Property(name="pascal_unpacked_structured_type", type=pascal_structured_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_structured_type280", type=pascal_unpacked_structured_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
array_type281: BinaryAssociation = BinaryAssociation(
    name="array_type281",
    ends={
        Property(name="pascal_array_type", type=pascal_unpacked_structured_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unpacked_structured_type282", type=pascal_array_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
record_type283: BinaryAssociation = BinaryAssociation(
    name="record_type283",
    ends={
        Property(name="pascal_record_type", type=pascal_unpacked_structured_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unpacked_structured_type284", type=pascal_record_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
set_type285: BinaryAssociation = BinaryAssociation(
    name="set_type285",
    ends={
        Property(name="pascal_set_type", type=pascal_unpacked_structured_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unpacked_structured_type286", type=pascal_set_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
file_type287: BinaryAssociation = BinaryAssociation(
    name="file_type287",
    ends={
        Property(name="pascal_file_type", type=pascal_unpacked_structured_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unpacked_structured_type288", type=pascal_file_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
file_component_type289: BinaryAssociation = BinaryAssociation(
    name="file_component_type289",
    ends={
        Property(name="pascal_file_component_type", type=pascal_file_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_file_type290", type=pascal_file_component_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type291: BinaryAssociation = BinaryAssociation(
    name="type291",
    ends={
        Property(name="pascal_type293", type=pascal_file_component_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_file_component_type292", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base_type294: BinaryAssociation = BinaryAssociation(
    name="base_type294",
    ends={
        Property(name="pascal_base_type", type=pascal_set_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_set_type295", type=pascal_base_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type296: BinaryAssociation = BinaryAssociation(
    name="type296",
    ends={
        Property(name="pascal_type298", type=pascal_base_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_base_type297", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
field_list299: BinaryAssociation = BinaryAssociation(
    name="field_list299",
    ends={
        Property(name="pascal_field_list", type=pascal_record_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_record_type300", type=pascal_field_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variant_part303: BinaryAssociation = BinaryAssociation(
    name="variant_part303",
    ends={
        Property(name="pascal_variant_part", type=pascal_field_list, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_field_list304", type=pascal_variant_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
record_section305: BinaryAssociation = BinaryAssociation(
    name="record_section305",
    ends={
        Property(name="pascal_record_section", type=pascal_fixed_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_fixed_part306", type=pascal_record_section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifier_list307: BinaryAssociation = BinaryAssociation(
    name="identifier_list307",
    ends={
        Property(name="pascal_identifier_list309", type=pascal_record_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_record_section308", type=pascal_identifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type310: BinaryAssociation = BinaryAssociation(
    name="type310",
    ends={
        Property(name="pascal_type312", type=pascal_record_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_record_section311", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tag_field313: BinaryAssociation = BinaryAssociation(
    name="tag_field313",
    ends={
        Property(name="pascal_tag_field", type=pascal_variant_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variant_part314", type=pascal_tag_field, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_identifier315: BinaryAssociation = BinaryAssociation(
    name="type_identifier315",
    ends={
        Property(name="pascal_type_identifier317", type=pascal_variant_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variant_part316", type=pascal_type_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variant318: BinaryAssociation = BinaryAssociation(
    name="variant318",
    ends={
        Property(name="pascal_variant", type=pascal_variant_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variant_part319", type=pascal_variant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
case_label_list320: BinaryAssociation = BinaryAssociation(
    name="case_label_list320",
    ends={
        Property(name="pascal_case_label_list322", type=pascal_variant, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variant321", type=pascal_case_label_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
field_list323: BinaryAssociation = BinaryAssociation(
    name="field_list323",
    ends={
        Property(name="pascal_field_list325", type=pascal_variant, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variant324", type=pascal_field_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fixed_part301: BinaryAssociation = BinaryAssociation(
    name="fixed_part301",
    ends={
        Property(name="pascal_fixed_part", type=pascal_field_list, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_field_list302", type=pascal_fixed_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier326: BinaryAssociation = BinaryAssociation(
    name="identifier326",
    ends={
        Property(name="pascal_identifier328", type=pascal_tag_field, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_tag_field327", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index_type329: BinaryAssociation = BinaryAssociation(
    name="index_type329",
    ends={
        Property(name="pascal_index_type", type=pascal_array_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_array_type330", type=pascal_index_type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element_type331: BinaryAssociation = BinaryAssociation(
    name="element_type331",
    ends={
        Property(name="pascal_element_type", type=pascal_array_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_array_type332", type=pascal_element_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type333: BinaryAssociation = BinaryAssociation(
    name="type333",
    ends={
        Property(name="pascal_type335", type=pascal_element_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_element_type334", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simple_type336: BinaryAssociation = BinaryAssociation(
    name="simple_type336",
    ends={
        Property(name="pascal_simple_type338", type=pascal_index_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_index_type337", type=pascal_simple_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subrange_type339: BinaryAssociation = BinaryAssociation(
    name="subrange_type339",
    ends={
        Property(name="pascal_subrange_type", type=pascal_simple_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simple_type340", type=pascal_subrange_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumerated_type341: BinaryAssociation = BinaryAssociation(
    name="enumerated_type341",
    ends={
        Property(name="pascal_enumerated_type", type=pascal_simple_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simple_type342", type=pascal_enumerated_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier_list343: BinaryAssociation = BinaryAssociation(
    name="identifier_list343",
    ends={
        Property(name="pascal_identifier_list345", type=pascal_enumerated_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_enumerated_type344", type=pascal_identifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lower_bound346: BinaryAssociation = BinaryAssociation(
    name="lower_bound346",
    ends={
        Property(name="pascal_lower_bound", type=pascal_subrange_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_subrange_type347", type=pascal_lower_bound, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
compiler_defined_directives373: BinaryAssociation = BinaryAssociation(
    name="compiler_defined_directives373",
    ends={
        Property(name="pascal_compiler_defined_directives", type=pascal_directive, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_directive374", type=pascal_compiler_defined_directives, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant350: BinaryAssociation = BinaryAssociation(
    name="constant350",
    ends={
        Property(name="pascal_constant352", type=pascal_lower_bound, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_lower_bound351", type=pascal_constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant353: BinaryAssociation = BinaryAssociation(
    name="constant353",
    ends={
        Property(name="pascal_constant355", type=pascal_upper_bound, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_upper_bound354", type=pascal_constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable_declaration356: BinaryAssociation = BinaryAssociation(
    name="variable_declaration356",
    ends={
        Property(name="pascal_variable_declaration", type=pascal_variable_declaration_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variable_declaration_part357", type=pascal_variable_declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifier_list358: BinaryAssociation = BinaryAssociation(
    name="identifier_list358",
    ends={
        Property(name="pascal_identifier_list360", type=pascal_variable_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variable_declaration359", type=pascal_identifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type361: BinaryAssociation = BinaryAssociation(
    name="type361",
    ends={
        Property(name="pascal_type363", type=pascal_variable_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variable_declaration362", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function_identifier364: BinaryAssociation = BinaryAssociation(
    name="function_identifier364",
    ends={
        Property(name="pascal_identifier366", type=pascal_function_identification, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_function_identification365", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function_block367: BinaryAssociation = BinaryAssociation(
    name="function_block367",
    ends={
        Property(name="pascal_function_block369", type=pascal_function_body, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_function_body368", type=pascal_function_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier370: BinaryAssociation = BinaryAssociation(
    name="identifier370",
    ends={
        Property(name="pascal_identifier372", type=pascal_procedure_identification, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_procedure_identification371", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
upper_bound348: BinaryAssociation = BinaryAssociation(
    name="upper_bound348",
    ends={
        Property(name="pascal_upper_bound", type=pascal_subrange_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_subrange_type349", type=pascal_upper_bound, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
procedure_heading375: BinaryAssociation = BinaryAssociation(
    name="procedure_heading375",
    ends={
        Property(name="pascal_procedure_heading377", type=pascal_compiler_defined_directives, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_compiler_defined_directives376", type=pascal_procedure_heading, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
procedure_block378: BinaryAssociation = BinaryAssociation(
    name="procedure_block378",
    ends={
        Property(name="pascal_procedure_block380", type=pascal_procedure_body, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_procedure_body379", type=pascal_procedure_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier381: BinaryAssociation = BinaryAssociation(
    name="identifier381",
    ends={
        Property(name="pascal_identifier383", type=pascal_procedure_heading, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_procedure_heading382", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formal_parameter_list384: BinaryAssociation = BinaryAssociation(
    name="formal_parameter_list384",
    ends={
        Property(name="pascal_formal_parameter_list", type=pascal_procedure_heading, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_procedure_heading385", type=pascal_formal_parameter_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formal_parameter_section386: BinaryAssociation = BinaryAssociation(
    name="formal_parameter_section386",
    ends={
        Property(name="pascal_formal_parameter_section", type=pascal_formal_parameter_list, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_formal_parameter_list387", type=pascal_formal_parameter_section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value_parameter_section388: BinaryAssociation = BinaryAssociation(
    name="value_parameter_section388",
    ends={
        Property(name="pascal_value_parameter_section", type=pascal_formal_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_formal_parameter_section389", type=pascal_value_parameter_section, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable_parameter_section390: BinaryAssociation = BinaryAssociation(
    name="variable_parameter_section390",
    ends={
        Property(name="pascal_variable_parameter_section", type=pascal_formal_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_formal_parameter_section391", type=pascal_variable_parameter_section, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
procedure_parameter_section392: BinaryAssociation = BinaryAssociation(
    name="procedure_parameter_section392",
    ends={
        Property(name="pascal_procedure_parameter_section", type=pascal_formal_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_formal_parameter_section393", type=pascal_procedure_parameter_section, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function_parameter_section394: BinaryAssociation = BinaryAssociation(
    name="function_parameter_section394",
    ends={
        Property(name="pascal_function_parameter_section", type=pascal_formal_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_formal_parameter_section395", type=pascal_function_parameter_section, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter_type421: BinaryAssociation = BinaryAssociation(
    name="parameter_type421",
    ends={
        Property(name="pascal_parameter_type423", type=pascal_value_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_value_parameter_section422", type=pascal_parameter_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function_heading396: BinaryAssociation = BinaryAssociation(
    name="function_heading396",
    ends={
        Property(name="pascal_function_heading398", type=pascal_function_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_function_parameter_section397", type=pascal_function_heading, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier399: BinaryAssociation = BinaryAssociation(
    name="identifier399",
    ends={
        Property(name="pascal_identifier401", type=pascal_function_heading, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_function_heading400", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formal_parameter_list402: BinaryAssociation = BinaryAssociation(
    name="formal_parameter_list402",
    ends={
        Property(name="pascal_formal_parameter_list404", type=pascal_function_heading, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_function_heading403", type=pascal_formal_parameter_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result_type405: BinaryAssociation = BinaryAssociation(
    name="result_type405",
    ends={
        Property(name="pascal_result_type", type=pascal_function_heading, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_function_heading406", type=pascal_result_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_identifier407: BinaryAssociation = BinaryAssociation(
    name="type_identifier407",
    ends={
        Property(name="pascal_type_identifier409", type=pascal_result_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_result_type408", type=pascal_type_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
procedure_heading410: BinaryAssociation = BinaryAssociation(
    name="procedure_heading410",
    ends={
        Property(name="pascal_procedure_heading412", type=pascal_procedure_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_procedure_parameter_section411", type=pascal_procedure_heading, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier_list413: BinaryAssociation = BinaryAssociation(
    name="identifier_list413",
    ends={
        Property(name="pascal_identifier_list415", type=pascal_variable_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variable_parameter_section414", type=pascal_identifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter_type416: BinaryAssociation = BinaryAssociation(
    name="parameter_type416",
    ends={
        Property(name="pascal_parameter_type", type=pascal_variable_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variable_parameter_section417", type=pascal_parameter_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier_list418: BinaryAssociation = BinaryAssociation(
    name="identifier_list418",
    ends={
        Property(name="pascal_identifier_list420", type=pascal_value_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_value_parameter_section419", type=pascal_identifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_identifier424: BinaryAssociation = BinaryAssociation(
    name="type_identifier424",
    ends={
        Property(name="pascal_type_identifier426", type=pascal_parameter_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_parameter_type425", type=pascal_type_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conformant_array_schema427: BinaryAssociation = BinaryAssociation(
    name="conformant_array_schema427",
    ends={
        Property(name="pascal_conformant_array_schema", type=pascal_parameter_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_parameter_type428", type=pascal_conformant_array_schema, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
packed_conformant_array_schema429: BinaryAssociation = BinaryAssociation(
    name="packed_conformant_array_schema429",
    ends={
        Property(name="pascal_packed_conformant_array_schema", type=pascal_conformant_array_schema, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_conformant_array_schema430", type=pascal_packed_conformant_array_schema, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unpacked_conformant_array_schema431: BinaryAssociation = BinaryAssociation(
    name="unpacked_conformant_array_schema431",
    ends={
        Property(name="pascal_unpacked_conformant_array_schema", type=pascal_conformant_array_schema, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_conformant_array_schema432", type=pascal_unpacked_conformant_array_schema, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bound_specification433: BinaryAssociation = BinaryAssociation(
    name="bound_specification433",
    ends={
        Property(name="pascal_bound_specification", type=pascal_unpacked_conformant_array_schema, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unpacked_conformant_array_schema434", type=pascal_bound_specification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type_identifier435: BinaryAssociation = BinaryAssociation(
    name="type_identifier435",
    ends={
        Property(name="pascal_type_identifier437", type=pascal_unpacked_conformant_array_schema, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unpacked_conformant_array_schema436", type=pascal_type_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conformant_array_schema438: BinaryAssociation = BinaryAssociation(
    name="conformant_array_schema438",
    ends={
        Property(name="pascal_conformant_array_schema440", type=pascal_unpacked_conformant_array_schema, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unpacked_conformant_array_schema439", type=pascal_conformant_array_schema, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier441: BinaryAssociation = BinaryAssociation(
    name="identifier441",
    ends={
        Property(name="pascal_identifier443", type=pascal_bound_specification, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_bound_specification442", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier2444: BinaryAssociation = BinaryAssociation(
    name="identifier2444",
    ends={
        Property(name="pascal_identifier446", type=pascal_bound_specification, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_bound_specification445", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ordinal_type_identifier447: BinaryAssociation = BinaryAssociation(
    name="ordinal_type_identifier447",
    ends={
        Property(name="pascal_ordinal_type_identifier", type=pascal_bound_specification, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_bound_specification448", type=pascal_ordinal_type_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_identifier449: BinaryAssociation = BinaryAssociation(
    name="type_identifier449",
    ends={
        Property(name="pascal_type_identifier451", type=pascal_ordinal_type_identifier, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_ordinal_type_identifier450", type=pascal_type_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bound_specification452: BinaryAssociation = BinaryAssociation(
    name="bound_specification452",
    ends={
        Property(name="pascal_bound_specification454", type=pascal_packed_conformant_array_schema, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_packed_conformant_array_schema453", type=pascal_bound_specification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_identifier455: BinaryAssociation = BinaryAssociation(
    name="type_identifier455",
    ends={
        Property(name="pascal_type_identifier457", type=pascal_packed_conformant_array_schema, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_packed_conformant_array_schema456", type=pascal_type_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
output_value459: BinaryAssociation = BinaryAssociation(
    name="output_value459",
    ends={
        Property(name="pascal_output_value", type=pascal_output_value, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_output_value458", type=pascal_output_value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_pascal_expression_output_value = Generalization(general=output_value, specific=pascal_expression)
gen_pascal_output_value_output_list = Generalization(general=output_list, specific=pascal_output_value)

# Domain Model
domain_model = DomainModel(
    name="pascal",
    types={pascal_Begin, pascal_program, pascal_statement_sequence, pascal_program_heading, pascal_block, pascal_identifier_list, pascal_procedure_block, pascal_declaration_part, pascal_statement_part, pascal_function_block, pascal_identifier, pascal_actual_parameter_list, pascal_actual_parameter, pascal_statement, pascal_label, pascal_simple_statement, pascal_structured_statement, pascal_assignment_statement, pascal_procedure_statement, pascal_goto_statement, pascal_expression, pascal_actual_value, pascal_actual_variable, pascal_actual_procedure, pascal_actual_function, pascal_variable, pascal_factor, output_value, pascal_simple_expression, pascal_term, pascal_addition_operator, pascal_element_list, pascal_number, pascal_set, pascal_function_designator, pascal_integer_number, pascal_real_number, pascal_repetitive_statement, pascal_digit_sequence, pascal_entire_variable, pascal_expression_list, pascal_scale_factor, pascal_compound_statement, pascal_conditional_statement, pascal_with_statement, pascal_if_statement, pascal_case_statement, pascal_case_limb, pascal_case_label_list, pascal_constant, pascal_while_statement, pascal_repeat_statement, pascal_for_statement, pascal_initial_expression, pascal_final_expression, pascal_constant_definition_part, pascal_label_declaration_part, pascal_type_definition_part, pascal_variable_declaration_part, pascal_procedure_heading, pascal_procedure_body, pascal_directive, pascal_procedure_identification, pascal_function_heading, pascal_function_body, pascal_function_identification, pascal_constant_definition, pascal_type_definition, pascal_type, pascal_simple_type, pascal_structured_type, pascal_pointer_type, pascal_type_identifier, pascal_unpacked_structured_type, pascal_array_type, pascal_record_type, pascal_set_type, pascal_file_type, pascal_file_component_type, pascal_base_type, pascal_field_list, pascal_variant_part, pascal_fixed_part, pascal_record_section, pascal_tag_field, pascal_variant, pascal_index_type, pascal_element_type, pascal_subrange_type, pascal_enumerated_type, pascal_lower_bound, pascal_upper_bound, pascal_variable_declaration, pascal_compiler_defined_directives, pascal_formal_parameter_list, pascal_formal_parameter_section, pascal_value_parameter_section, pascal_variable_parameter_section, pascal_procedure_parameter_section, pascal_function_parameter_section, pascal_result_type, pascal_parameter_type, pascal_conformant_array_schema, pascal_packed_conformant_array_schema, pascal_unpacked_conformant_array_schema, pascal_bound_specification, pascal_ordinal_type_identifier, pascal_output_list, pascal_output_value, output_list},
    associations={elements0, statement_part12, declaration_part15, statement_part18, statement_sequence21, program_heading1, block3, identifier_list5, declaration_part7, statement_part8, declaration_part10, procedure_identifier40, actual_parameter_list42, actual_parameter44, statement23, label25, simple_statement27, structured_statement29, assignment_statement31, procedure_statement33, goto_statement35, label37, expression62, variable64, actual_value46, actual_variable48, actual_procedure50, actual_function52, function_identifier54, procedure_identifier57, variable60, factor82, function_identifier67, expression70, simple_expression73, expression76, term78, addition_operator80, function_identifier102, actual_parameter_list105, element_list108, variable84, number87, set89, identifier91, function_designator94, expression96, factor100, expression110, integer_number113, real_number115, digit_sequence124, digit_sequence117, entire_variable127, digit_sequence2119, expression_list129, scale_factor122, field_identifier131, identifier134, expression137, integer_number140, digit_sequence143, compound_statement146, case_label_list169, repetitive_statement148, conditional_statement150, with_statement152, variable154, statement157, if_statement160, case_statement162, expression164, case_limb167, statement171, constant174, expression176, statement179, while_statement182, repeat_statement184, for_statement186, variable_identifier188, initial_expression191, final_expression193, constant_definition_part221, statement195, expression198, expression201, statement_sequence204, expression207, expression210, statement213, statement_sequence216, label_declaration_part219, label241, type_definition_part223, variable_declaration_part225, procedure_heading227, procedure_body229, directive231, procedure_identification233, function_heading235, function_body237, function_identification239, type263, constant_definition244, identifier246, constant249, constant_identifier252, number255, type_definition258, identifier260, simple_type265, structured_type267, pointer_type269, type_identifier271, identifier273, type_identifier276, unpacked_structured_type279, array_type281, record_type283, set_type285, file_type287, file_component_type289, type291, base_type294, type296, field_list299, variant_part303, record_section305, identifier_list307, type310, tag_field313, type_identifier315, variant318, case_label_list320, field_list323, fixed_part301, identifier326, index_type329, element_type331, type333, simple_type336, subrange_type339, enumerated_type341, identifier_list343, lower_bound346, compiler_defined_directives373, constant350, constant353, variable_declaration356, identifier_list358, type361, function_identifier364, function_block367, identifier370, upper_bound348, procedure_heading375, procedure_block378, identifier381, formal_parameter_list384, formal_parameter_section386, value_parameter_section388, variable_parameter_section390, procedure_parameter_section392, function_parameter_section394, parameter_type421, function_heading396, identifier399, formal_parameter_list402, result_type405, type_identifier407, procedure_heading410, identifier_list413, parameter_type416, identifier_list418, type_identifier424, conformant_array_schema427, packed_conformant_array_schema429, unpacked_conformant_array_schema431, bound_specification433, type_identifier435, conformant_array_schema438, identifier441, identifier2444, ordinal_type_identifier447, type_identifier449, bound_specification452, type_identifier455, output_value459},
    generalizations={gen_pascal_expression_output_value, gen_pascal_output_value_output_list},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)