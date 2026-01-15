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
pascal_label_declaration_part = Class(name="pascal::label::declaration::part")
pascal_constant_definition_part = Class(name="pascal::constant::definition::part")
pascal_type_definition_part = Class(name="pascal::type::definition::part")
pascal_variable_declaration_part = Class(name="pascal::variable::declaration::part")
pascal_pascal = Class(name="pascal::pascal")
pascal_program = Class(name="pascal::program")
pascal_program_heading_block = Class(name="pascal::program::heading::block")
pascal_block = Class(name="pascal::block")
pascal_identifier_list = Class(name="pascal::identifier::list")
pascal_assignment_statement = Class(name="pascal::assignment::statement")
pascal_function_designator = Class(name="pascal::function::designator")
pascal_goto_statement = Class(name="pascal::goto::statement")
pascal_procedure_and_function_declaration_part = Class(name="pascal::procedure::and::function::declaration::part")
pascal_statement_part = Class(name="pascal::statement::part")
pascal_statement_sequence = Class(name="pascal::statement::sequence")
pascal_statement = Class(name="pascal::statement")
pascal_label = Class(name="pascal::label")
pascal_simple_statement = Class(name="pascal::simple::statement")
pascal_structured_statement = Class(name="pascal::structured::statement")
pascal_variable = Class(name="pascal::variable")
pascal_expression = Class(name="pascal::expression")
pascal_var_ = Class(name="pascal::var::")
pascal_expression_list = Class(name="pascal::expression::list")
pascal_number = Class(name="pascal::number")
pascal_set = Class(name="pascal::set")
pascal_simple_expression = Class(name="pascal::simple::expression")
pascal_EObject = Class(name="pascal::EObject")
pascal_term = Class(name="pascal::term")
pascal_factor = Class(name="pascal::factor")
pascal_compound_statement = Class(name="pascal::compound::statement")
pascal_repetitive_statement = Class(name="pascal::repetitive::statement")
pascal_conditional_statement = Class(name="pascal::conditional::statement")
pascal_any_number = Class(name="pascal::any::number")
pascal_with_statement = Class(name="pascal::with::statement")
pascal_while_statement = Class(name="pascal::while::statement")
pascal_repeat_statement = Class(name="pascal::repeat::statement")
pascal_for_statement = Class(name="pascal::for::statement")
pascal_case_limb = Class(name="pascal::case::limb")
pascal_case_label_list = Class(name="pascal::case::label::list")
pascal_if_statement = Class(name="pascal::if::statement")
pascal_case_statement = Class(name="pascal::case::statement")
pascal_constant_definition = Class(name="pascal::constant::definition")
pascal_constant = Class(name="pascal::constant")
pascal_subrange_type = Class(name="pascal::subrange::type")
pascal_enumerated_type = Class(name="pascal::enumerated::type")
pascal_type_definition = Class(name="pascal::type::definition")
pascal_type = Class(name="pascal::type")
pascal_simple_type = Class(name="pascal::simple::type")
pascal_structured_type = Class(name="pascal::structured::type")
pascal_pointer_type = Class(name="pascal::pointer::type")
pascal_record_type = Class(name="pascal::record::type")
pascal_set_type = Class(name="pascal::set::type")
pascal_file_type = Class(name="pascal::file::type")
pascal_unpacked_structured_type = Class(name="pascal::unpacked::structured::type")
pascal_array_type = Class(name="pascal::array::type")
pascal_dynamic_array_type = Class(name="pascal::dynamic::array::type")
pascal_variant_part = Class(name="pascal::variant::part")
pascal_record_section = Class(name="pascal::record::section")
pascal_variable_identifier_list = Class(name="pascal::variable::identifier::list")
pascal_index_type = Class(name="pascal::index::type")
pascal_field_list = Class(name="pascal::field::list")
pascal_fixed_part = Class(name="pascal::fixed::part")
pascal_abstraction_heading = Class(name="pascal::abstraction::heading")
pascal_variable_section = Class(name="pascal::variable::section")
pascal_tag_field = Class(name="pascal::tag::field")
pascal_variant = Class(name="pascal::variant")
pascal_unpacked_conformant_array_schema = Class(name="pascal::unpacked::conformant::array::schema")
pascal_bound_specification = Class(name="pascal::bound::specification")
pascal_abstraction_declaration = Class(name="pascal::abstraction::declaration")
abstraction_declaration = Class(name="abstraction::declaration")
pascal_formal_parameter_list = Class(name="pascal::formal::parameter::list")
pascal_formal_parameter_section = Class(name="pascal::formal::parameter::section")
pascal_value_parameter_section = Class(name="pascal::value::parameter::section")
pascal_variable_parameter_section = Class(name="pascal::variable::parameter::section")
pascal_parameter_type = Class(name="pascal::parameter::type")
pascal_conformant_array_schema = Class(name="pascal::conformant::array::schema")
pascal_packed_conformant_array_schema = Class(name="pascal::packed::conformant::array::schema")

# pascal_label_declaration_part class attributes and methods

# pascal_constant_definition_part class attributes and methods

# pascal_type_definition_part class attributes and methods

# pascal_variable_declaration_part class attributes and methods

# pascal_pascal class attributes and methods

# pascal_program class attributes and methods

# pascal_program_heading_block class attributes and methods
pascal_program_heading_block_name: Property = Property(name="name", type=StringType)
pascal_program_heading_block.attributes={pascal_program_heading_block_name}

# pascal_block class attributes and methods

# pascal_identifier_list class attributes and methods
pascal_identifier_list_names: Property = Property(name="names", type=StringType)
pascal_identifier_list.attributes={pascal_identifier_list_names}

# pascal_assignment_statement class attributes and methods

# pascal_function_designator class attributes and methods
pascal_function_designator_name: Property = Property(name="name", type=StringType)
pascal_function_designator.attributes={pascal_function_designator_name}

# pascal_goto_statement class attributes and methods

# pascal_procedure_and_function_declaration_part class attributes and methods

# pascal_statement_part class attributes and methods

# pascal_statement_sequence class attributes and methods

# pascal_statement class attributes and methods

# pascal_label class attributes and methods
pascal_label_number: Property = Property(name="number", type=StringType)
pascal_label.attributes={pascal_label_number}

# pascal_simple_statement class attributes and methods
pascal_simple_statement_function_noargs: Property = Property(name="function_noargs", type=StringType)
pascal_simple_statement.attributes={pascal_simple_statement_function_noargs}

# pascal_structured_statement class attributes and methods

# pascal_variable class attributes and methods
pascal_variable_name: Property = Property(name="name", type=StringType)
pascal_variable.attributes={pascal_variable_name}

# pascal_expression class attributes and methods
pascal_expression_operators: Property = Property(name="operators", type=StringType)
pascal_expression.attributes={pascal_expression_operators}

# pascal_var_ class attributes and methods
pascal_var__accessor: Property = Property(name="accessor", type=BooleanType)
pascal_var__name: Property = Property(name="name", type=StringType)
pascal_var_.attributes={pascal_var__accessor, pascal_var__name}

# pascal_expression_list class attributes and methods

# pascal_number class attributes and methods

# pascal_set class attributes and methods
pascal_set_brackets: Property = Property(name="brackets", type=StringType)
pascal_set.attributes={pascal_set_brackets}

# pascal_simple_expression class attributes and methods
pascal_simple_expression_prefixOperator: Property = Property(name="prefixOperator", type=StringType)
pascal_simple_expression_operators: Property = Property(name="operators", type=StringType)
pascal_simple_expression.attributes={pascal_simple_expression_operators, pascal_simple_expression_prefixOperator}

# pascal_EObject class attributes and methods

# pascal_term class attributes and methods
pascal_term_operators: Property = Property(name="operators", type=StringType)
pascal_term.attributes={pascal_term_operators}

# pascal_factor class attributes and methods
pascal_factor_string: Property = Property(name="string", type=StringType)
pascal_factor_nil: Property = Property(name="nil", type=BooleanType)
pascal_factor_boolean: Property = Property(name="boolean", type=StringType)
pascal_factor.attributes={pascal_factor_string, pascal_factor_nil, pascal_factor_boolean}

# pascal_compound_statement class attributes and methods

# pascal_repetitive_statement class attributes and methods

# pascal_conditional_statement class attributes and methods

# pascal_any_number class attributes and methods
pascal_any_number_integer: Property = Property(name="integer", type=StringType)
pascal_any_number_real: Property = Property(name="real", type=StringType)
pascal_any_number.attributes={pascal_any_number_real, pascal_any_number_integer}

# pascal_with_statement class attributes and methods

# pascal_while_statement class attributes and methods

# pascal_repeat_statement class attributes and methods

# pascal_for_statement class attributes and methods

# pascal_case_limb class attributes and methods

# pascal_case_label_list class attributes and methods

# pascal_if_statement class attributes and methods

# pascal_case_statement class attributes and methods

# pascal_constant_definition class attributes and methods
pascal_constant_definition_name: Property = Property(name="name", type=StringType)
pascal_constant_definition.attributes={pascal_constant_definition_name}

# pascal_constant class attributes and methods
pascal_constant_opterator: Property = Property(name="opterator", type=StringType)
pascal_constant_name: Property = Property(name="name", type=StringType)
pascal_constant_string: Property = Property(name="string", type=StringType)
pascal_constant_boolLiteral: Property = Property(name="boolLiteral", type=StringType)
pascal_constant_nil: Property = Property(name="nil", type=StringType)
pascal_constant.attributes={pascal_constant_nil, pascal_constant_name, pascal_constant_string, pascal_constant_opterator, pascal_constant_boolLiteral}

# pascal_subrange_type class attributes and methods
pascal_subrange_type_subrange: Property = Property(name="subrange", type=StringType)
pascal_subrange_type.attributes={pascal_subrange_type_subrange}

# pascal_enumerated_type class attributes and methods

# pascal_type_definition class attributes and methods
pascal_type_definition_name: Property = Property(name="name", type=StringType)
pascal_type_definition.attributes={pascal_type_definition_name}

# pascal_type class attributes and methods

# pascal_simple_type class attributes and methods
pascal_simple_type_name: Property = Property(name="name", type=StringType)
pascal_simple_type.attributes={pascal_simple_type_name}

# pascal_structured_type class attributes and methods
pascal_structured_type_packed: Property = Property(name="packed", type=BooleanType)
pascal_structured_type.attributes={pascal_structured_type_packed}

# pascal_pointer_type class attributes and methods

# pascal_record_type class attributes and methods
pascal_record_type_recordKeyword: Property = Property(name="recordKeyword", type=StringType)
pascal_record_type_endKeyword: Property = Property(name="endKeyword", type=StringType)
pascal_record_type.attributes={pascal_record_type_recordKeyword, pascal_record_type_endKeyword}

# pascal_set_type class attributes and methods

# pascal_file_type class attributes and methods

# pascal_unpacked_structured_type class attributes and methods

# pascal_array_type class attributes and methods

# pascal_dynamic_array_type class attributes and methods

# pascal_variant_part class attributes and methods
pascal_variant_part_name: Property = Property(name="name", type=StringType)
pascal_variant_part.attributes={pascal_variant_part_name}

# pascal_record_section class attributes and methods

# pascal_variable_identifier_list class attributes and methods
pascal_variable_identifier_list_names: Property = Property(name="names", type=StringType)
pascal_variable_identifier_list.attributes={pascal_variable_identifier_list_names}

# pascal_index_type class attributes and methods

# pascal_field_list class attributes and methods

# pascal_fixed_part class attributes and methods

# pascal_abstraction_heading class attributes and methods
pascal_abstraction_heading_name: Property = Property(name="name", type=StringType)
pascal_abstraction_heading_returnType: Property = Property(name="returnType", type=StringType)
pascal_abstraction_heading.attributes={pascal_abstraction_heading_name, pascal_abstraction_heading_returnType}

# pascal_variable_section class attributes and methods

# pascal_tag_field class attributes and methods
pascal_tag_field_name: Property = Property(name="name", type=StringType)
pascal_tag_field.attributes={pascal_tag_field_name}

# pascal_variant class attributes and methods

# pascal_unpacked_conformant_array_schema class attributes and methods

# pascal_bound_specification class attributes and methods
pascal_bound_specification_initial: Property = Property(name="initial", type=StringType)
pascal_bound_specification_final: Property = Property(name="final", type=StringType)
pascal_bound_specification_name: Property = Property(name="name", type=StringType)
pascal_bound_specification.attributes={pascal_bound_specification_initial, pascal_bound_specification_name, pascal_bound_specification_final}

# pascal_abstraction_declaration class attributes and methods
pascal_abstraction_declaration_forward: Property = Property(name="forward", type=BooleanType)
pascal_abstraction_declaration.attributes={pascal_abstraction_declaration_forward}

# abstraction_declaration class attributes and methods

# pascal_formal_parameter_list class attributes and methods

# pascal_formal_parameter_section class attributes and methods

# pascal_value_parameter_section class attributes and methods

# pascal_variable_parameter_section class attributes and methods

# pascal_parameter_type class attributes and methods
pascal_parameter_type_name: Property = Property(name="name", type=StringType)
pascal_parameter_type.attributes={pascal_parameter_type_name}

# pascal_conformant_array_schema class attributes and methods

# pascal_packed_conformant_array_schema class attributes and methods
pascal_packed_conformant_array_schema_name: Property = Property(name="name", type=StringType)
pascal_packed_conformant_array_schema.attributes={pascal_packed_conformant_array_schema_name}

# Relationships
label7: BinaryAssociation = BinaryAssociation(
    name="label7",
    ends={
        Property(name="pascal_label_declaration_part", type=pascal_block, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_block8", type=pascal_label_declaration_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant9: BinaryAssociation = BinaryAssociation(
    name="constant9",
    ends={
        Property(name="pascal_constant_definition_part", type=pascal_block, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_block10", type=pascal_constant_definition_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type11: BinaryAssociation = BinaryAssociation(
    name="type11",
    ends={
        Property(name="pascal_type_definition_part", type=pascal_block, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_block12", type=pascal_type_definition_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable13: BinaryAssociation = BinaryAssociation(
    name="variable13",
    ends={
        Property(name="pascal_variable_declaration_part", type=pascal_block, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_block14", type=pascal_variable_declaration_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
program0: BinaryAssociation = BinaryAssociation(
    name="program0",
    ends={
        Property(name="pascal_program", type=pascal_pascal, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_pascal", type=pascal_program, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
heading1: BinaryAssociation = BinaryAssociation(
    name="heading1",
    ends={
        Property(name="pascal_program_heading_block", type=pascal_program, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_program2", type=pascal_program_heading_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block3: BinaryAssociation = BinaryAssociation(
    name="block3",
    ends={
        Property(name="pascal_block", type=pascal_program, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_program4", type=pascal_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifiers5: BinaryAssociation = BinaryAssociation(
    name="identifiers5",
    ends={
        Property(name="pascal_identifier_list", type=pascal_program_heading_block, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_program_heading_block6", type=pascal_identifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structured27: BinaryAssociation = BinaryAssociation(
    name="structured27",
    ends={
        Property(name="pascal_structured_statement", type=pascal_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_statement28", type=pascal_structured_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment29: BinaryAssociation = BinaryAssociation(
    name="assignment29",
    ends={
        Property(name="pascal_assignment_statement", type=pascal_simple_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simple_statement30", type=pascal_assignment_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function31: BinaryAssociation = BinaryAssociation(
    name="function31",
    ends={
        Property(name="pascal_function_designator", type=pascal_simple_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simple_statement32", type=pascal_function_designator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
abstraction15: BinaryAssociation = BinaryAssociation(
    name="abstraction15",
    ends={
        Property(name="pascal_procedure_and_function_declaration_part", type=pascal_block, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_block16", type=pascal_procedure_and_function_declaration_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement17: BinaryAssociation = BinaryAssociation(
    name="statement17",
    ends={
        Property(name="pascal_statement_part", type=pascal_block, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_block18", type=pascal_statement_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequence19: BinaryAssociation = BinaryAssociation(
    name="sequence19",
    ends={
        Property(name="pascal_statement_sequence", type=pascal_statement_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_statement_part20", type=pascal_statement_sequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements21: BinaryAssociation = BinaryAssociation(
    name="statements21",
    ends={
        Property(name="pascal_statement", type=pascal_statement_sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_statement_sequence22", type=pascal_statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label23: BinaryAssociation = BinaryAssociation(
    name="label23",
    ends={
        Property(name="pascal_label", type=pascal_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_statement24", type=pascal_label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simple25: BinaryAssociation = BinaryAssociation(
    name="simple25",
    ends={
        Property(name="pascal_simple_statement", type=pascal_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_statement26", type=pascal_simple_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
array44: BinaryAssociation = BinaryAssociation(
    name="array44",
    ends={
        Property(name="pascal_var_43", type=pascal_var_, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="pascal_var_45", type=pascal_var_, multiplicity=Multiplicity(1, 1))
    }
)
variable47: BinaryAssociation = BinaryAssociation(
    name="variable47",
    ends={
        Property(name="pascal_var_48", type=pascal_var_, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_var_46", type=pascal_var_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pointer50: BinaryAssociation = BinaryAssociation(
    name="pointer50",
    ends={
        Property(name="pascal_var_51", type=pascal_var_, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_var_49", type=pascal_var_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
goto33: BinaryAssociation = BinaryAssociation(
    name="goto33",
    ends={
        Property(name="pascal_goto_statement", type=pascal_simple_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simple_statement34", type=pascal_goto_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable35: BinaryAssociation = BinaryAssociation(
    name="variable35",
    ends={
        Property(name="pascal_variable", type=pascal_assignment_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_assignment_statement36", type=pascal_variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression37: BinaryAssociation = BinaryAssociation(
    name="expression37",
    ends={
        Property(name="pascal_expression", type=pascal_assignment_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_assignment_statement38", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable39: BinaryAssociation = BinaryAssociation(
    name="variable39",
    ends={
        Property(name="pascal_var_", type=pascal_variable, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variable40", type=pascal_var_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions41: BinaryAssociation = BinaryAssociation(
    name="expressions41",
    ends={
        Property(name="pascal_expression_list", type=pascal_var_, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_var_42", type=pascal_expression_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable60: BinaryAssociation = BinaryAssociation(
    name="variable60",
    ends={
        Property(name="pascal_variable62", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor61", type=pascal_variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
number63: BinaryAssociation = BinaryAssociation(
    name="number63",
    ends={
        Property(name="pascal_number", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor64", type=pascal_number, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
set65: BinaryAssociation = BinaryAssociation(
    name="set65",
    ends={
        Property(name="pascal_set", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor66", type=pascal_set, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions52: BinaryAssociation = BinaryAssociation(
    name="expressions52",
    ends={
        Property(name="pascal_expression54", type=pascal_expression_list, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_expression_list53", type=pascal_expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions55: BinaryAssociation = BinaryAssociation(
    name="expressions55",
    ends={
        Property(name="pascal_simple_expression", type=pascal_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_expression56", type=pascal_simple_expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
terms57: BinaryAssociation = BinaryAssociation(
    name="terms57",
    ends={
        Property(name="pascal_EObject", type=pascal_simple_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simple_expression58", type=pascal_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
factors59: BinaryAssociation = BinaryAssociation(
    name="factors59",
    ends={
        Property(name="pascal_factor", type=pascal_term, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_term", type=pascal_factor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions81: BinaryAssociation = BinaryAssociation(
    name="expressions81",
    ends={
        Property(name="pascal_expression_list83", type=pascal_function_designator, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_function_designator82", type=pascal_expression_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
compound84: BinaryAssociation = BinaryAssociation(
    name="compound84",
    ends={
        Property(name="pascal_compound_statement", type=pascal_structured_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_structured_statement85", type=pascal_compound_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
repetitive86: BinaryAssociation = BinaryAssociation(
    name="repetitive86",
    ends={
        Property(name="pascal_repetitive_statement", type=pascal_structured_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_structured_statement87", type=pascal_repetitive_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditional88: BinaryAssociation = BinaryAssociation(
    name="conditional88",
    ends={
        Property(name="pascal_conditional_statement", type=pascal_structured_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_structured_statement89", type=pascal_conditional_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function67: BinaryAssociation = BinaryAssociation(
    name="function67",
    ends={
        Property(name="pascal_function_designator69", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor68", type=pascal_function_designator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression70: BinaryAssociation = BinaryAssociation(
    name="expression70",
    ends={
        Property(name="pascal_expression72", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor71", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
not74: BinaryAssociation = BinaryAssociation(
    name="not74",
    ends={
        Property(name="pascal_factor75", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor73", type=pascal_factor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
number76: BinaryAssociation = BinaryAssociation(
    name="number76",
    ends={
        Property(name="pascal_any_number", type=pascal_number, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_number77", type=pascal_any_number, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions78: BinaryAssociation = BinaryAssociation(
    name="expressions78",
    ends={
        Property(name="pascal_expression_list80", type=pascal_set, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_set79", type=pascal_expression_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement104: BinaryAssociation = BinaryAssociation(
    name="statement104",
    ends={
        Property(name="pascal_statement106", type=pascal_while_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_while_statement105", type=pascal_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequence107: BinaryAssociation = BinaryAssociation(
    name="sequence107",
    ends={
        Property(name="pascal_statement_sequence109", type=pascal_repeat_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_repeat_statement108", type=pascal_statement_sequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression110: BinaryAssociation = BinaryAssociation(
    name="expression110",
    ends={
        Property(name="pascal_expression112", type=pascal_repeat_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_repeat_statement111", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment113: BinaryAssociation = BinaryAssociation(
    name="assignment113",
    ends={
        Property(name="pascal_assignment_statement115", type=pascal_for_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_for_statement114", type=pascal_assignment_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
withStmt90: BinaryAssociation = BinaryAssociation(
    name="withStmt90",
    ends={
        Property(name="pascal_with_statement", type=pascal_structured_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_structured_statement91", type=pascal_with_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequence92: BinaryAssociation = BinaryAssociation(
    name="sequence92",
    ends={
        Property(name="pascal_statement_sequence94", type=pascal_compound_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_compound_statement93", type=pascal_statement_sequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whileStmt95: BinaryAssociation = BinaryAssociation(
    name="whileStmt95",
    ends={
        Property(name="pascal_while_statement", type=pascal_repetitive_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_repetitive_statement96", type=pascal_while_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
repeatStmt97: BinaryAssociation = BinaryAssociation(
    name="repeatStmt97",
    ends={
        Property(name="pascal_repeat_statement", type=pascal_repetitive_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_repetitive_statement98", type=pascal_repeat_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
forStmt99: BinaryAssociation = BinaryAssociation(
    name="forStmt99",
    ends={
        Property(name="pascal_for_statement", type=pascal_repetitive_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_repetitive_statement100", type=pascal_for_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression101: BinaryAssociation = BinaryAssociation(
    name="expression101",
    ends={
        Property(name="pascal_expression103", type=pascal_while_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_while_statement102", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression135: BinaryAssociation = BinaryAssociation(
    name="expression135",
    ends={
        Property(name="pascal_expression137", type=pascal_case_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_case_statement136", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cases138: BinaryAssociation = BinaryAssociation(
    name="cases138",
    ends={
        Property(name="pascal_case_limb", type=pascal_case_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_case_statement139", type=pascal_case_limb, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cases140: BinaryAssociation = BinaryAssociation(
    name="cases140",
    ends={
        Property(name="pascal_case_label_list", type=pascal_case_limb, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_case_limb141", type=pascal_case_label_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression116: BinaryAssociation = BinaryAssociation(
    name="expression116",
    ends={
        Property(name="pascal_expression118", type=pascal_for_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_for_statement117", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement119: BinaryAssociation = BinaryAssociation(
    name="statement119",
    ends={
        Property(name="pascal_statement121", type=pascal_for_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_for_statement120", type=pascal_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifStmt122: BinaryAssociation = BinaryAssociation(
    name="ifStmt122",
    ends={
        Property(name="pascal_if_statement", type=pascal_conditional_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_conditional_statement123", type=pascal_if_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
caseStmt124: BinaryAssociation = BinaryAssociation(
    name="caseStmt124",
    ends={
        Property(name="pascal_case_statement", type=pascal_conditional_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_conditional_statement125", type=pascal_case_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression126: BinaryAssociation = BinaryAssociation(
    name="expression126",
    ends={
        Property(name="pascal_expression128", type=pascal_if_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_if_statement127", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifStatement129: BinaryAssociation = BinaryAssociation(
    name="ifStatement129",
    ends={
        Property(name="pascal_statement131", type=pascal_if_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_if_statement130", type=pascal_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseStatement132: BinaryAssociation = BinaryAssociation(
    name="elseStatement132",
    ends={
        Property(name="pascal_statement134", type=pascal_if_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_if_statement133", type=pascal_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
label156: BinaryAssociation = BinaryAssociation(
    name="label156",
    ends={
        Property(name="pascal_label158", type=pascal_goto_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_goto_statement157", type=pascal_label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labels159: BinaryAssociation = BinaryAssociation(
    name="labels159",
    ends={
        Property(name="pascal_label161", type=pascal_label_declaration_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_label_declaration_part160", type=pascal_label, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
consts162: BinaryAssociation = BinaryAssociation(
    name="consts162",
    ends={
        Property(name="pascal_constant_definition", type=pascal_constant_definition_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_constant_definition_part163", type=pascal_constant_definition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement142: BinaryAssociation = BinaryAssociation(
    name="statement142",
    ends={
        Property(name="pascal_statement144", type=pascal_case_limb, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_case_limb143", type=pascal_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constants145: BinaryAssociation = BinaryAssociation(
    name="constants145",
    ends={
        Property(name="pascal_constant", type=pascal_case_label_list, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_case_label_list146", type=pascal_constant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
number147: BinaryAssociation = BinaryAssociation(
    name="number147",
    ends={
        Property(name="pascal_number149", type=pascal_constant, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_constant148", type=pascal_number, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables150: BinaryAssociation = BinaryAssociation(
    name="variables150",
    ends={
        Property(name="pascal_variable152", type=pascal_with_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_with_statement151", type=pascal_variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement153: BinaryAssociation = BinaryAssociation(
    name="statement153",
    ends={
        Property(name="pascal_statement155", type=pascal_with_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_with_statement154", type=pascal_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pointer175: BinaryAssociation = BinaryAssociation(
    name="pointer175",
    ends={
        Property(name="pascal_pointer_type", type=pascal_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_type176", type=pascal_pointer_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subrange177: BinaryAssociation = BinaryAssociation(
    name="subrange177",
    ends={
        Property(name="pascal_subrange_type", type=pascal_simple_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simple_type178", type=pascal_subrange_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumerated179: BinaryAssociation = BinaryAssociation(
    name="enumerated179",
    ends={
        Property(name="pascal_enumerated_type", type=pascal_simple_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simple_type180", type=pascal_enumerated_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
const164: BinaryAssociation = BinaryAssociation(
    name="const164",
    ends={
        Property(name="pascal_constant166", type=pascal_constant_definition, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_constant_definition165", type=pascal_constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
types167: BinaryAssociation = BinaryAssociation(
    name="types167",
    ends={
        Property(name="pascal_type_definition", type=pascal_type_definition_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_type_definition_part168", type=pascal_type_definition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type169: BinaryAssociation = BinaryAssociation(
    name="type169",
    ends={
        Property(name="pascal_type", type=pascal_type_definition, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_type_definition170", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simple171: BinaryAssociation = BinaryAssociation(
    name="simple171",
    ends={
        Property(name="pascal_simple_type", type=pascal_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_type172", type=pascal_simple_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structured173: BinaryAssociation = BinaryAssociation(
    name="structured173",
    ends={
        Property(name="pascal_structured_type", type=pascal_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_type174", type=pascal_structured_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dynamic197: BinaryAssociation = BinaryAssociation(
    name="dynamic197",
    ends={
        Property(name="pascal_dynamic_array_type", type=pascal_unpacked_structured_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unpacked_structured_type198", type=pascal_dynamic_array_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
record199: BinaryAssociation = BinaryAssociation(
    name="record199",
    ends={
        Property(name="pascal_record_type", type=pascal_unpacked_structured_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unpacked_structured_type200", type=pascal_record_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
set201: BinaryAssociation = BinaryAssociation(
    name="set201",
    ends={
        Property(name="pascal_set_type", type=pascal_unpacked_structured_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unpacked_structured_type202", type=pascal_set_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
file203: BinaryAssociation = BinaryAssociation(
    name="file203",
    ends={
        Property(name="pascal_file_type", type=pascal_unpacked_structured_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unpacked_structured_type204", type=pascal_file_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialConst181: BinaryAssociation = BinaryAssociation(
    name="initialConst181",
    ends={
        Property(name="pascal_constant183", type=pascal_subrange_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_subrange_type182", type=pascal_constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finalConst184: BinaryAssociation = BinaryAssociation(
    name="finalConst184",
    ends={
        Property(name="pascal_constant186", type=pascal_subrange_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_subrange_type185", type=pascal_constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
const187: BinaryAssociation = BinaryAssociation(
    name="const187",
    ends={
        Property(name="pascal_constant189", type=pascal_subrange_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_subrange_type188", type=pascal_constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifiers190: BinaryAssociation = BinaryAssociation(
    name="identifiers190",
    ends={
        Property(name="pascal_identifier_list192", type=pascal_enumerated_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_enumerated_type191", type=pascal_identifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type193: BinaryAssociation = BinaryAssociation(
    name="type193",
    ends={
        Property(name="pascal_unpacked_structured_type", type=pascal_structured_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_structured_type194", type=pascal_unpacked_structured_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
array195: BinaryAssociation = BinaryAssociation(
    name="array195",
    ends={
        Property(name="pascal_array_type", type=pascal_unpacked_structured_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unpacked_structured_type196", type=pascal_array_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fixed218: BinaryAssociation = BinaryAssociation(
    name="fixed218",
    ends={
        Property(name="pascal_fixed_part", type=pascal_field_list, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_field_list219", type=pascal_fixed_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variants220: BinaryAssociation = BinaryAssociation(
    name="variants220",
    ends={
        Property(name="pascal_variant_part", type=pascal_field_list, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_field_list221", type=pascal_variant_part, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sections222: BinaryAssociation = BinaryAssociation(
    name="sections222",
    ends={
        Property(name="pascal_record_section", type=pascal_fixed_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_fixed_part223", type=pascal_record_section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
indexes205: BinaryAssociation = BinaryAssociation(
    name="indexes205",
    ends={
        Property(name="pascal_index_type", type=pascal_array_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_array_type206", type=pascal_index_type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type207: BinaryAssociation = BinaryAssociation(
    name="type207",
    ends={
        Property(name="pascal_type209", type=pascal_array_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_array_type208", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type210: BinaryAssociation = BinaryAssociation(
    name="type210",
    ends={
        Property(name="pascal_type212", type=pascal_dynamic_array_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_dynamic_array_type211", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type213: BinaryAssociation = BinaryAssociation(
    name="type213",
    ends={
        Property(name="pascal_simple_type215", type=pascal_index_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_index_type214", type=pascal_simple_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fields216: BinaryAssociation = BinaryAssociation(
    name="fields216",
    ends={
        Property(name="pascal_field_list", type=pascal_record_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_record_type217", type=pascal_field_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labels238: BinaryAssociation = BinaryAssociation(
    name="labels238",
    ends={
        Property(name="pascal_case_label_list240", type=pascal_variant, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variant239", type=pascal_case_label_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fields241: BinaryAssociation = BinaryAssociation(
    name="fields241",
    ends={
        Property(name="pascal_field_list243", type=pascal_variant, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variant242", type=pascal_field_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type244: BinaryAssociation = BinaryAssociation(
    name="type244",
    ends={
        Property(name="pascal_type246", type=pascal_set_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_set_type245", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type247: BinaryAssociation = BinaryAssociation(
    name="type247",
    ends={
        Property(name="pascal_type249", type=pascal_file_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_file_type248", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type250: BinaryAssociation = BinaryAssociation(
    name="type250",
    ends={
        Property(name="pascal_type252", type=pascal_pointer_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_pointer_type251", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sections253: BinaryAssociation = BinaryAssociation(
    name="sections253",
    ends={
        Property(name="pascal_variable_section255", type=pascal_variable_declaration_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variable_declaration_part254", type=pascal_variable_section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
procedures256: BinaryAssociation = BinaryAssociation(
    name="procedures256",
    ends={
        Property(name="pascal_abstraction_heading", type=pascal_procedure_and_function_declaration_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_procedure_and_function_declaration_part257", type=pascal_abstraction_heading, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifiers224: BinaryAssociation = BinaryAssociation(
    name="identifiers224",
    ends={
        Property(name="pascal_variable_identifier_list", type=pascal_variable_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variable_section", type=pascal_variable_identifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type225: BinaryAssociation = BinaryAssociation(
    name="type225",
    ends={
        Property(name="pascal_type227", type=pascal_variable_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variable_section226", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifiers228: BinaryAssociation = BinaryAssociation(
    name="identifiers228",
    ends={
        Property(name="pascal_identifier_list230", type=pascal_record_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_record_section229", type=pascal_identifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type231: BinaryAssociation = BinaryAssociation(
    name="type231",
    ends={
        Property(name="pascal_type233", type=pascal_record_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_record_section232", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tag234: BinaryAssociation = BinaryAssociation(
    name="tag234",
    ends={
        Property(name="pascal_tag_field", type=pascal_variant_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variant_part235", type=pascal_tag_field, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variants236: BinaryAssociation = BinaryAssociation(
    name="variants236",
    ends={
        Property(name="pascal_variant", type=pascal_variant_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variant_part237", type=pascal_variant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packed287: BinaryAssociation = BinaryAssociation(
    name="packed287",
    ends={
        Property(name="pascal_packed_conformant_array_schema", type=pascal_conformant_array_schema, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_conformant_array_schema288", type=pascal_packed_conformant_array_schema, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unpacked289: BinaryAssociation = BinaryAssociation(
    name="unpacked289",
    ends={
        Property(name="pascal_unpacked_conformant_array_schema", type=pascal_conformant_array_schema, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_conformant_array_schema290", type=pascal_unpacked_conformant_array_schema, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bound291: BinaryAssociation = BinaryAssociation(
    name="bound291",
    ends={
        Property(name="pascal_bound_specification", type=pascal_packed_conformant_array_schema, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_packed_conformant_array_schema292", type=pascal_bound_specification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bounds293: BinaryAssociation = BinaryAssociation(
    name="bounds293",
    ends={
        Property(name="pascal_bound_specification295", type=pascal_unpacked_conformant_array_schema, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unpacked_conformant_array_schema294", type=pascal_bound_specification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type296: BinaryAssociation = BinaryAssociation(
    name="type296",
    ends={
        Property(name="pascal_parameter_type298", type=pascal_unpacked_conformant_array_schema, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unpacked_conformant_array_schema297", type=pascal_parameter_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifiers299: BinaryAssociation = BinaryAssociation(
    name="identifiers299",
    ends={
        Property(name="pascal_identifier_list301", type=pascal_variable_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variable_parameter_section300", type=pascal_identifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type302: BinaryAssociation = BinaryAssociation(
    name="type302",
    ends={
        Property(name="pascal_parameter_type304", type=pascal_variable_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variable_parameter_section303", type=pascal_parameter_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functions258: BinaryAssociation = BinaryAssociation(
    name="functions258",
    ends={
        Property(name="pascal_abstraction_declaration", type=pascal_procedure_and_function_declaration_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_procedure_and_function_declaration_part259", type=pascal_abstraction_declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
heading260: BinaryAssociation = BinaryAssociation(
    name="heading260",
    ends={
        Property(name="pascal_abstraction_heading262", type=pascal_abstraction_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_abstraction_declaration261", type=pascal_abstraction_heading, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block263: BinaryAssociation = BinaryAssociation(
    name="block263",
    ends={
        Property(name="pascal_block265", type=pascal_abstraction_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_abstraction_declaration264", type=pascal_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters266: BinaryAssociation = BinaryAssociation(
    name="parameters266",
    ends={
        Property(name="pascal_formal_parameter_list", type=pascal_abstraction_heading, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_abstraction_heading267", type=pascal_formal_parameter_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters268: BinaryAssociation = BinaryAssociation(
    name="parameters268",
    ends={
        Property(name="pascal_formal_parameter_section", type=pascal_formal_parameter_list, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_formal_parameter_list269", type=pascal_formal_parameter_section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value270: BinaryAssociation = BinaryAssociation(
    name="value270",
    ends={
        Property(name="pascal_value_parameter_section", type=pascal_formal_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_formal_parameter_section271", type=pascal_value_parameter_section, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable272: BinaryAssociation = BinaryAssociation(
    name="variable272",
    ends={
        Property(name="pascal_variable_parameter_section", type=pascal_formal_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_formal_parameter_section273", type=pascal_variable_parameter_section, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
procedure274: BinaryAssociation = BinaryAssociation(
    name="procedure274",
    ends={
        Property(name="pascal_abstraction_heading276", type=pascal_formal_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_formal_parameter_section275", type=pascal_abstraction_heading, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function277: BinaryAssociation = BinaryAssociation(
    name="function277",
    ends={
        Property(name="pascal_abstraction_heading279", type=pascal_formal_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_formal_parameter_section278", type=pascal_abstraction_heading, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifiers280: BinaryAssociation = BinaryAssociation(
    name="identifiers280",
    ends={
        Property(name="pascal_identifier_list282", type=pascal_value_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_value_parameter_section281", type=pascal_identifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type283: BinaryAssociation = BinaryAssociation(
    name="type283",
    ends={
        Property(name="pascal_parameter_type", type=pascal_value_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_value_parameter_section284", type=pascal_parameter_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
array285: BinaryAssociation = BinaryAssociation(
    name="array285",
    ends={
        Property(name="pascal_conformant_array_schema", type=pascal_parameter_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_parameter_type286", type=pascal_conformant_array_schema, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_pascal_abstraction_heading_abstraction_declaration = Generalization(general=abstraction_declaration, specific=pascal_abstraction_heading)

# Domain Model
domain_model = DomainModel(
    name="pascal",
    types={pascal_label_declaration_part, pascal_constant_definition_part, pascal_type_definition_part, pascal_variable_declaration_part, pascal_pascal, pascal_program, pascal_program_heading_block, pascal_block, pascal_identifier_list, pascal_assignment_statement, pascal_function_designator, pascal_goto_statement, pascal_procedure_and_function_declaration_part, pascal_statement_part, pascal_statement_sequence, pascal_statement, pascal_label, pascal_simple_statement, pascal_structured_statement, pascal_variable, pascal_expression, pascal_var_, pascal_expression_list, pascal_number, pascal_set, pascal_simple_expression, pascal_EObject, pascal_term, pascal_factor, pascal_compound_statement, pascal_repetitive_statement, pascal_conditional_statement, pascal_any_number, pascal_with_statement, pascal_while_statement, pascal_repeat_statement, pascal_for_statement, pascal_case_limb, pascal_case_label_list, pascal_if_statement, pascal_case_statement, pascal_constant_definition, pascal_constant, pascal_subrange_type, pascal_enumerated_type, pascal_type_definition, pascal_type, pascal_simple_type, pascal_structured_type, pascal_pointer_type, pascal_record_type, pascal_set_type, pascal_file_type, pascal_unpacked_structured_type, pascal_array_type, pascal_dynamic_array_type, pascal_variant_part, pascal_record_section, pascal_variable_identifier_list, pascal_index_type, pascal_field_list, pascal_fixed_part, pascal_abstraction_heading, pascal_variable_section, pascal_tag_field, pascal_variant, pascal_unpacked_conformant_array_schema, pascal_bound_specification, pascal_abstraction_declaration, abstraction_declaration, pascal_formal_parameter_list, pascal_formal_parameter_section, pascal_value_parameter_section, pascal_variable_parameter_section, pascal_parameter_type, pascal_conformant_array_schema, pascal_packed_conformant_array_schema},
    associations={label7, constant9, type11, variable13, program0, heading1, block3, identifiers5, structured27, assignment29, function31, abstraction15, statement17, sequence19, statements21, label23, simple25, array44, variable47, pointer50, goto33, variable35, expression37, variable39, expressions41, variable60, number63, set65, expressions52, expressions55, terms57, factors59, expressions81, compound84, repetitive86, conditional88, function67, expression70, not74, number76, expressions78, statement104, sequence107, expression110, assignment113, withStmt90, sequence92, whileStmt95, repeatStmt97, forStmt99, expression101, expression135, cases138, cases140, expression116, statement119, ifStmt122, caseStmt124, expression126, ifStatement129, elseStatement132, label156, labels159, consts162, statement142, constants145, number147, variables150, statement153, pointer175, subrange177, enumerated179, const164, types167, type169, simple171, structured173, dynamic197, record199, set201, file203, initialConst181, finalConst184, const187, identifiers190, type193, array195, fixed218, variants220, sections222, indexes205, type207, type210, type213, fields216, labels238, fields241, type244, type247, type250, sections253, procedures256, identifiers224, type225, identifiers228, type231, tag234, variants236, packed287, unpacked289, bound291, bounds293, type296, identifiers299, type302, functions258, heading260, block263, parameters266, parameters268, value270, variable272, procedure274, function277, identifiers280, type283, array285},
    generalizations={gen_pascal_abstraction_heading_abstraction_declaration},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)