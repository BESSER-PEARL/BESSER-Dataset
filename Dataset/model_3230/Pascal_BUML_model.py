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
pascal_identifier_list = Class(name="pascal::identifier::list")
pascal_program = Class(name="pascal::program")
pascal_program_heading = Class(name="pascal::program::heading")
pascal_block = Class(name="pascal::block")
pascal_variable_identifier_list = Class(name="pascal::variable::identifier::list")
pascal_abstraction_heading = Class(name="pascal::abstraction::heading")
pascal_declaration_part = Class(name="pascal::declaration::part")
pascal_statement_part = Class(name="pascal::statement::part")
pascal_label_declaration_part = Class(name="pascal::label::declaration::part")
pascal_constant_definition_part = Class(name="pascal::constant::definition::part")
pascal_type_definition_part = Class(name="pascal::type::definition::part")
pascal_variable_declaration_part = Class(name="pascal::variable::declaration::part")
pascal_procedure_and_function_declaration_part = Class(name="pascal::procedure::and::function::declaration::part")
pascal_label = Class(name="pascal::label")
pascal_constant_definition = Class(name="pascal::constant::definition")
pascal_constant = Class(name="pascal::constant")
pascal_type_definition = Class(name="pascal::type::definition")
pascal_type = Class(name="pascal::type")
pascal_variable_section = Class(name="pascal::variable::section")
pascal_conformant_array_schema = Class(name="pascal::conformant::array::schema")
pascal_abstraction_declaration = Class(name="pascal::abstraction::declaration")
abstraction_declaration = Class(name="abstraction::declaration")
pascal_formal_parameter_list = Class(name="pascal::formal::parameter::list")
pascal_statement_sequence = Class(name="pascal::statement::sequence")
pascal_formal_parameter_section = Class(name="pascal::formal::parameter::section")
pascal_value_parameter_section = Class(name="pascal::value::parameter::section")
pascal_variable_parameter_section = Class(name="pascal::variable::parameter::section")
pascal_parameter_type = Class(name="pascal::parameter::type")
pascal_packed_conformant_array_schema = Class(name="pascal::packed::conformant::array::schema")
pascal_unpacked_conformant_array_schema = Class(name="pascal::unpacked::conformant::array::schema")
pascal_bound_specification = Class(name="pascal::bound::specification")
pascal_statement = Class(name="pascal::statement")
pascal_simple_statement = Class(name="pascal::simple::statement")
pascal_structured_statement = Class(name="pascal::structured::statement")
pascal_assignment_statement = Class(name="pascal::assignment::statement")
pascal_function_designator = Class(name="pascal::function::designator")
pascal_goto_statement = Class(name="pascal::goto::statement")
pascal_variable = Class(name="pascal::variable")
pascal_expression = Class(name="pascal::expression")
pascal_compound_statement = Class(name="pascal::compound::statement")
pascal_repetitive_statement = Class(name="pascal::repetitive::statement")
pascal_conditional_statement = Class(name="pascal::conditional::statement")
pascal_with_statement = Class(name="pascal::with::statement")
pascal_while_statement = Class(name="pascal::while::statement")
pascal_repeat_statement = Class(name="pascal::repeat::statement")
pascal_for_statement = Class(name="pascal::for::statement")
pascal_if_statement = Class(name="pascal::if::statement")
pascal_resto = Class(name="pascal::resto")
pascal_simple_expression = Class(name="pascal::simple::expression")
pascal_expression_list = Class(name="pascal::expression::list")
pascal_EObject = Class(name="pascal::EObject")
pascal_term = Class(name="pascal::term")
pascal_factor = Class(name="pascal::factor")
pascal_number = Class(name="pascal::number")
pascal_set = Class(name="pascal::set")
pascal_simple_type = Class(name="pascal::simple::type")
pascal_structured_type = Class(name="pascal::structured::type")
pascal_pointer_type = Class(name="pascal::pointer::type")
pascal_subrange_type = Class(name="pascal::subrange::type")
pascal_enumerated_type = Class(name="pascal::enumerated::type")
pascal_unpacked_structured_type = Class(name="pascal::unpacked::structured::type")
pascal_array_type = Class(name="pascal::array::type")
pascal_record_type = Class(name="pascal::record::type")
pascal_set_type = Class(name="pascal::set::type")
pascal_file_type = Class(name="pascal::file::type")
pascal_field_list = Class(name="pascal::field::list")
pascal_fixed_part = Class(name="pascal::fixed::part")
pascal_variant_part = Class(name="pascal::variant::part")
pascal_record_section = Class(name="pascal::record::section")
pascal_tag_field = Class(name="pascal::tag::field")
pascal_variant = Class(name="pascal::variant")
pascal_case_label_list = Class(name="pascal::case::label::list")
pascal_any_number = Class(name="pascal::any::number")

# pascal_identifier_list class attributes and methods
pascal_identifier_list_ids: Property = Property(name="ids", type=StringType)
pascal_identifier_list.attributes={pascal_identifier_list_ids}

# pascal_program class attributes and methods

# pascal_program_heading class attributes and methods
pascal_program_heading_name: Property = Property(name="name", type=StringType)
pascal_program_heading.attributes={pascal_program_heading_name}

# pascal_block class attributes and methods

# pascal_variable_identifier_list class attributes and methods
pascal_variable_identifier_list_names: Property = Property(name="names", type=StringType)
pascal_variable_identifier_list.attributes={pascal_variable_identifier_list_names}

# pascal_abstraction_heading class attributes and methods
pascal_abstraction_heading_name: Property = Property(name="name", type=StringType)
pascal_abstraction_heading_resultType: Property = Property(name="resultType", type=StringType)
pascal_abstraction_heading.attributes={pascal_abstraction_heading_name, pascal_abstraction_heading_resultType}

# pascal_declaration_part class attributes and methods

# pascal_statement_part class attributes and methods

# pascal_label_declaration_part class attributes and methods

# pascal_constant_definition_part class attributes and methods

# pascal_type_definition_part class attributes and methods

# pascal_variable_declaration_part class attributes and methods

# pascal_procedure_and_function_declaration_part class attributes and methods

# pascal_label class attributes and methods
pascal_label_number: Property = Property(name="number", type=StringType)
pascal_label.attributes={pascal_label_number}

# pascal_constant_definition class attributes and methods
pascal_constant_definition_name: Property = Property(name="name", type=StringType)
pascal_constant_definition.attributes={pascal_constant_definition_name}

# pascal_constant class attributes and methods
pascal_constant_opterator: Property = Property(name="opterator", type=StringType)
pascal_constant_name: Property = Property(name="name", type=StringType)
pascal_constant_string: Property = Property(name="string", type=StringType)
pascal_constant_boolLiteral: Property = Property(name="boolLiteral", type=StringType)
pascal_constant_nil: Property = Property(name="nil", type=StringType)
pascal_constant.attributes={pascal_constant_name, pascal_constant_boolLiteral, pascal_constant_opterator, pascal_constant_string, pascal_constant_nil}

# pascal_type_definition class attributes and methods
pascal_type_definition_name: Property = Property(name="name", type=StringType)
pascal_type_definition.attributes={pascal_type_definition_name}

# pascal_type class attributes and methods

# pascal_variable_section class attributes and methods

# pascal_conformant_array_schema class attributes and methods

# pascal_abstraction_declaration class attributes and methods
pascal_abstraction_declaration_forward: Property = Property(name="forward", type=BooleanType)
pascal_abstraction_declaration.attributes={pascal_abstraction_declaration_forward}

# abstraction_declaration class attributes and methods

# pascal_formal_parameter_list class attributes and methods

# pascal_statement_sequence class attributes and methods

# pascal_formal_parameter_section class attributes and methods

# pascal_value_parameter_section class attributes and methods

# pascal_variable_parameter_section class attributes and methods

# pascal_parameter_type class attributes and methods
pascal_parameter_type_name: Property = Property(name="name", type=StringType)
pascal_parameter_type.attributes={pascal_parameter_type_name}

# pascal_packed_conformant_array_schema class attributes and methods
pascal_packed_conformant_array_schema_name: Property = Property(name="name", type=StringType)
pascal_packed_conformant_array_schema.attributes={pascal_packed_conformant_array_schema_name}

# pascal_unpacked_conformant_array_schema class attributes and methods

# pascal_bound_specification class attributes and methods
pascal_bound_specification_init: Property = Property(name="init", type=StringType)
pascal_bound_specification_fin: Property = Property(name="fin", type=StringType)
pascal_bound_specification_name: Property = Property(name="name", type=StringType)
pascal_bound_specification.attributes={pascal_bound_specification_init, pascal_bound_specification_fin, pascal_bound_specification_name}

# pascal_statement class attributes and methods

# pascal_simple_statement class attributes and methods
pascal_simple_statement_function_noargs: Property = Property(name="function_noargs", type=StringType)
pascal_simple_statement.attributes={pascal_simple_statement_function_noargs}

# pascal_structured_statement class attributes and methods

# pascal_assignment_statement class attributes and methods

# pascal_function_designator class attributes and methods
pascal_function_designator_name: Property = Property(name="name", type=StringType)
pascal_function_designator.attributes={pascal_function_designator_name}

# pascal_goto_statement class attributes and methods

# pascal_variable class attributes and methods
pascal_variable_name: Property = Property(name="name", type=StringType)
pascal_variable.attributes={pascal_variable_name}

# pascal_expression class attributes and methods
pascal_expression_operators: Property = Property(name="operators", type=StringType)
pascal_expression.attributes={pascal_expression_operators}

# pascal_compound_statement class attributes and methods

# pascal_repetitive_statement class attributes and methods

# pascal_conditional_statement class attributes and methods

# pascal_with_statement class attributes and methods
pascal_with_statement_record: Property = Property(name="record", type=StringType)
pascal_with_statement_records: Property = Property(name="records", type=StringType)
pascal_with_statement.attributes={pascal_with_statement_record, pascal_with_statement_records}

# pascal_while_statement class attributes and methods

# pascal_repeat_statement class attributes and methods

# pascal_for_statement class attributes and methods
pascal_for_statement_initID: Property = Property(name="initID", type=StringType)
pascal_for_statement.attributes={pascal_for_statement_initID}

# pascal_if_statement class attributes and methods

# pascal_resto class attributes and methods
pascal_resto_accessor: Property = Property(name="accessor", type=BooleanType)
pascal_resto_name: Property = Property(name="name", type=StringType)
pascal_resto.attributes={pascal_resto_name, pascal_resto_accessor}

# pascal_simple_expression class attributes and methods
pascal_simple_expression_prefixOperator: Property = Property(name="prefixOperator", type=StringType)
pascal_simple_expression_operators: Property = Property(name="operators", type=StringType)
pascal_simple_expression.attributes={pascal_simple_expression_operators, pascal_simple_expression_prefixOperator}

# pascal_expression_list class attributes and methods

# pascal_EObject class attributes and methods

# pascal_term class attributes and methods
pascal_term_operators: Property = Property(name="operators", type=StringType)
pascal_term.attributes={pascal_term_operators}

# pascal_factor class attributes and methods
pascal_factor_nil: Property = Property(name="nil", type=BooleanType)
pascal_factor_boolean: Property = Property(name="boolean", type=StringType)
pascal_factor_string: Property = Property(name="string", type=StringType)
pascal_factor.attributes={pascal_factor_string, pascal_factor_nil, pascal_factor_boolean}

# pascal_number class attributes and methods

# pascal_set class attributes and methods
pascal_set_brackets: Property = Property(name="brackets", type=StringType)
pascal_set.attributes={pascal_set_brackets}

# pascal_simple_type class attributes and methods
pascal_simple_type_name: Property = Property(name="name", type=StringType)
pascal_simple_type.attributes={pascal_simple_type_name}

# pascal_structured_type class attributes and methods
pascal_structured_type_packed: Property = Property(name="packed", type=BooleanType)
pascal_structured_type.attributes={pascal_structured_type_packed}

# pascal_pointer_type class attributes and methods

# pascal_subrange_type class attributes and methods
pascal_subrange_type_subrange: Property = Property(name="subrange", type=StringType)
pascal_subrange_type.attributes={pascal_subrange_type_subrange}

# pascal_enumerated_type class attributes and methods

# pascal_unpacked_structured_type class attributes and methods

# pascal_array_type class attributes and methods

# pascal_record_type class attributes and methods
pascal_record_type_record: Property = Property(name="record", type=StringType)
pascal_record_type_end: Property = Property(name="end", type=StringType)
pascal_record_type.attributes={pascal_record_type_record, pascal_record_type_end}

# pascal_set_type class attributes and methods

# pascal_file_type class attributes and methods

# pascal_field_list class attributes and methods

# pascal_fixed_part class attributes and methods

# pascal_variant_part class attributes and methods
pascal_variant_part_name: Property = Property(name="name", type=StringType)
pascal_variant_part.attributes={pascal_variant_part_name}

# pascal_record_section class attributes and methods

# pascal_tag_field class attributes and methods
pascal_tag_field_name: Property = Property(name="name", type=StringType)
pascal_tag_field.attributes={pascal_tag_field_name}

# pascal_variant class attributes and methods

# pascal_case_label_list class attributes and methods

# pascal_any_number class attributes and methods
pascal_any_number_integer: Property = Property(name="integer", type=StringType)
pascal_any_number_real: Property = Property(name="real", type=StringType)
pascal_any_number.attributes={pascal_any_number_integer, pascal_any_number_real}

# Relationships
identifiers3: BinaryAssociation = BinaryAssociation(
    name="identifiers3",
    ends={
        Property(name="pascal_identifier_list", type=pascal_program_heading, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_program_heading4", type=pascal_identifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
heading0: BinaryAssociation = BinaryAssociation(
    name="heading0",
    ends={
        Property(name="pascal_program_heading", type=pascal_program, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_program", type=pascal_program_heading, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block1: BinaryAssociation = BinaryAssociation(
    name="block1",
    ends={
        Property(name="pascal_block", type=pascal_program, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_program2", type=pascal_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifiers31: BinaryAssociation = BinaryAssociation(
    name="identifiers31",
    ends={
        Property(name="pascal_variable_identifier_list", type=pascal_variable_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variable_section32", type=pascal_variable_identifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type33: BinaryAssociation = BinaryAssociation(
    name="type33",
    ends={
        Property(name="pascal_type35", type=pascal_variable_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variable_section34", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration5: BinaryAssociation = BinaryAssociation(
    name="declaration5",
    ends={
        Property(name="pascal_declaration_part", type=pascal_block, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_block6", type=pascal_declaration_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement7: BinaryAssociation = BinaryAssociation(
    name="statement7",
    ends={
        Property(name="pascal_statement_part", type=pascal_block, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_block8", type=pascal_statement_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
label_decl9: BinaryAssociation = BinaryAssociation(
    name="label_decl9",
    ends={
        Property(name="pascal_label_declaration_part", type=pascal_declaration_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_declaration_part10", type=pascal_label_declaration_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant_def11: BinaryAssociation = BinaryAssociation(
    name="constant_def11",
    ends={
        Property(name="pascal_constant_definition_part", type=pascal_declaration_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_declaration_part12", type=pascal_constant_definition_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_def13: BinaryAssociation = BinaryAssociation(
    name="type_def13",
    ends={
        Property(name="pascal_type_definition_part", type=pascal_declaration_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_declaration_part14", type=pascal_type_definition_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable_decl15: BinaryAssociation = BinaryAssociation(
    name="variable_decl15",
    ends={
        Property(name="pascal_variable_declaration_part", type=pascal_declaration_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_declaration_part16", type=pascal_variable_declaration_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
abstraction17: BinaryAssociation = BinaryAssociation(
    name="abstraction17",
    ends={
        Property(name="pascal_procedure_and_function_declaration_part", type=pascal_declaration_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_declaration_part18", type=pascal_procedure_and_function_declaration_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labels19: BinaryAssociation = BinaryAssociation(
    name="labels19",
    ends={
        Property(name="pascal_label", type=pascal_label_declaration_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_label_declaration_part20", type=pascal_label, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
consts21: BinaryAssociation = BinaryAssociation(
    name="consts21",
    ends={
        Property(name="pascal_constant_definition", type=pascal_constant_definition_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_constant_definition_part22", type=pascal_constant_definition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
const23: BinaryAssociation = BinaryAssociation(
    name="const23",
    ends={
        Property(name="pascal_constant", type=pascal_constant_definition, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_constant_definition24", type=pascal_constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
types25: BinaryAssociation = BinaryAssociation(
    name="types25",
    ends={
        Property(name="pascal_type_definition", type=pascal_type_definition_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_type_definition_part26", type=pascal_type_definition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type27: BinaryAssociation = BinaryAssociation(
    name="type27",
    ends={
        Property(name="pascal_type", type=pascal_type_definition, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_type_definition28", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sections29: BinaryAssociation = BinaryAssociation(
    name="sections29",
    ends={
        Property(name="pascal_variable_section", type=pascal_variable_declaration_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variable_declaration_part30", type=pascal_variable_section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type70: BinaryAssociation = BinaryAssociation(
    name="type70",
    ends={
        Property(name="pascal_variable_parameter_section71", type=pascal_parameter_type, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="pascal_parameter_type72", type=pascal_variable_parameter_section, multiplicity=Multiplicity(1, 1))
    }
)
array73: BinaryAssociation = BinaryAssociation(
    name="array73",
    ends={
        Property(name="pascal_conformant_array_schema", type=pascal_parameter_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_parameter_type74", type=pascal_conformant_array_schema, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
procedures36: BinaryAssociation = BinaryAssociation(
    name="procedures36",
    ends={
        Property(name="pascal_abstraction_heading", type=pascal_procedure_and_function_declaration_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_procedure_and_function_declaration_part37", type=pascal_abstraction_heading, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions38: BinaryAssociation = BinaryAssociation(
    name="functions38",
    ends={
        Property(name="pascal_abstraction_declaration", type=pascal_procedure_and_function_declaration_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_procedure_and_function_declaration_part39", type=pascal_abstraction_declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters40: BinaryAssociation = BinaryAssociation(
    name="parameters40",
    ends={
        Property(name="pascal_formal_parameter_list", type=pascal_abstraction_heading, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_abstraction_heading41", type=pascal_formal_parameter_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
heading42: BinaryAssociation = BinaryAssociation(
    name="heading42",
    ends={
        Property(name="pascal_abstraction_heading44", type=pascal_abstraction_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_abstraction_declaration43", type=pascal_abstraction_heading, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block45: BinaryAssociation = BinaryAssociation(
    name="block45",
    ends={
        Property(name="pascal_block47", type=pascal_abstraction_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_abstraction_declaration46", type=pascal_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequence48: BinaryAssociation = BinaryAssociation(
    name="sequence48",
    ends={
        Property(name="pascal_statement_sequence", type=pascal_statement_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_statement_part49", type=pascal_statement_sequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters50: BinaryAssociation = BinaryAssociation(
    name="parameters50",
    ends={
        Property(name="pascal_formal_parameter_section", type=pascal_formal_parameter_list, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_formal_parameter_list51", type=pascal_formal_parameter_section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value52: BinaryAssociation = BinaryAssociation(
    name="value52",
    ends={
        Property(name="pascal_value_parameter_section", type=pascal_formal_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_formal_parameter_section53", type=pascal_value_parameter_section, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable54: BinaryAssociation = BinaryAssociation(
    name="variable54",
    ends={
        Property(name="pascal_variable_parameter_section", type=pascal_formal_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_formal_parameter_section55", type=pascal_variable_parameter_section, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
procedure56: BinaryAssociation = BinaryAssociation(
    name="procedure56",
    ends={
        Property(name="pascal_abstraction_heading58", type=pascal_formal_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_formal_parameter_section57", type=pascal_abstraction_heading, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function59: BinaryAssociation = BinaryAssociation(
    name="function59",
    ends={
        Property(name="pascal_abstraction_heading61", type=pascal_formal_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_formal_parameter_section60", type=pascal_abstraction_heading, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifiers62: BinaryAssociation = BinaryAssociation(
    name="identifiers62",
    ends={
        Property(name="pascal_identifier_list64", type=pascal_value_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_value_parameter_section63", type=pascal_identifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type65: BinaryAssociation = BinaryAssociation(
    name="type65",
    ends={
        Property(name="pascal_parameter_type", type=pascal_value_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_value_parameter_section66", type=pascal_parameter_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifiers67: BinaryAssociation = BinaryAssociation(
    name="identifiers67",
    ends={
        Property(name="pascal_identifier_list69", type=pascal_variable_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variable_parameter_section68", type=pascal_identifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression104: BinaryAssociation = BinaryAssociation(
    name="expression104",
    ends={
        Property(name="pascal_expression", type=pascal_assignment_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_assignment_statement105", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
label106: BinaryAssociation = BinaryAssociation(
    name="label106",
    ends={
        Property(name="pascal_label108", type=pascal_goto_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_goto_statement107", type=pascal_label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
packed75: BinaryAssociation = BinaryAssociation(
    name="packed75",
    ends={
        Property(name="pascal_packed_conformant_array_schema", type=pascal_conformant_array_schema, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_conformant_array_schema76", type=pascal_packed_conformant_array_schema, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unpacked77: BinaryAssociation = BinaryAssociation(
    name="unpacked77",
    ends={
        Property(name="pascal_unpacked_conformant_array_schema", type=pascal_conformant_array_schema, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_conformant_array_schema78", type=pascal_unpacked_conformant_array_schema, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bound79: BinaryAssociation = BinaryAssociation(
    name="bound79",
    ends={
        Property(name="pascal_bound_specification", type=pascal_packed_conformant_array_schema, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_packed_conformant_array_schema80", type=pascal_bound_specification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bounds81: BinaryAssociation = BinaryAssociation(
    name="bounds81",
    ends={
        Property(name="pascal_bound_specification83", type=pascal_unpacked_conformant_array_schema, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unpacked_conformant_array_schema82", type=pascal_bound_specification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type84: BinaryAssociation = BinaryAssociation(
    name="type84",
    ends={
        Property(name="pascal_parameter_type86", type=pascal_unpacked_conformant_array_schema, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unpacked_conformant_array_schema85", type=pascal_parameter_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements87: BinaryAssociation = BinaryAssociation(
    name="statements87",
    ends={
        Property(name="pascal_statement", type=pascal_statement_sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_statement_sequence88", type=pascal_statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label89: BinaryAssociation = BinaryAssociation(
    name="label89",
    ends={
        Property(name="pascal_label91", type=pascal_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_statement90", type=pascal_label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simple92: BinaryAssociation = BinaryAssociation(
    name="simple92",
    ends={
        Property(name="pascal_simple_statement", type=pascal_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_statement93", type=pascal_simple_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structured94: BinaryAssociation = BinaryAssociation(
    name="structured94",
    ends={
        Property(name="pascal_structured_statement", type=pascal_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_statement95", type=pascal_structured_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment96: BinaryAssociation = BinaryAssociation(
    name="assignment96",
    ends={
        Property(name="pascal_assignment_statement", type=pascal_simple_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simple_statement97", type=pascal_assignment_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function98: BinaryAssociation = BinaryAssociation(
    name="function98",
    ends={
        Property(name="pascal_function_designator", type=pascal_simple_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simple_statement99", type=pascal_function_designator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
goto100: BinaryAssociation = BinaryAssociation(
    name="goto100",
    ends={
        Property(name="pascal_goto_statement", type=pascal_simple_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simple_statement101", type=pascal_goto_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable102: BinaryAssociation = BinaryAssociation(
    name="variable102",
    ends={
        Property(name="pascal_variable", type=pascal_assignment_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_assignment_statement103", type=pascal_variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression149: BinaryAssociation = BinaryAssociation(
    name="expression149",
    ends={
        Property(name="pascal_expression151", type=pascal_if_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_if_statement150", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifStatement152: BinaryAssociation = BinaryAssociation(
    name="ifStatement152",
    ends={
        Property(name="pascal_statement154", type=pascal_if_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_if_statement153", type=pascal_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
compound109: BinaryAssociation = BinaryAssociation(
    name="compound109",
    ends={
        Property(name="pascal_compound_statement", type=pascal_structured_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_structured_statement110", type=pascal_compound_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
repetitive111: BinaryAssociation = BinaryAssociation(
    name="repetitive111",
    ends={
        Property(name="pascal_repetitive_statement", type=pascal_structured_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_structured_statement112", type=pascal_repetitive_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditional113: BinaryAssociation = BinaryAssociation(
    name="conditional113",
    ends={
        Property(name="pascal_conditional_statement", type=pascal_structured_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_structured_statement114", type=pascal_conditional_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
with_stt115: BinaryAssociation = BinaryAssociation(
    name="with_stt115",
    ends={
        Property(name="pascal_with_statement", type=pascal_structured_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_structured_statement116", type=pascal_with_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequence117: BinaryAssociation = BinaryAssociation(
    name="sequence117",
    ends={
        Property(name="pascal_statement_sequence119", type=pascal_compound_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_compound_statement118", type=pascal_statement_sequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
while120: BinaryAssociation = BinaryAssociation(
    name="while120",
    ends={
        Property(name="pascal_while_statement", type=pascal_repetitive_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_repetitive_statement121", type=pascal_while_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
repeat122: BinaryAssociation = BinaryAssociation(
    name="repeat122",
    ends={
        Property(name="pascal_repeat_statement", type=pascal_repetitive_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_repetitive_statement123", type=pascal_repeat_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
for124: BinaryAssociation = BinaryAssociation(
    name="for124",
    ends={
        Property(name="pascal_for_statement", type=pascal_repetitive_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_repetitive_statement125", type=pascal_for_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression126: BinaryAssociation = BinaryAssociation(
    name="expression126",
    ends={
        Property(name="pascal_expression128", type=pascal_while_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_while_statement127", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement129: BinaryAssociation = BinaryAssociation(
    name="statement129",
    ends={
        Property(name="pascal_statement131", type=pascal_while_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_while_statement130", type=pascal_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequence132: BinaryAssociation = BinaryAssociation(
    name="sequence132",
    ends={
        Property(name="pascal_statement_sequence134", type=pascal_repeat_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_repeat_statement133", type=pascal_statement_sequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression135: BinaryAssociation = BinaryAssociation(
    name="expression135",
    ends={
        Property(name="pascal_expression137", type=pascal_repeat_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_repeat_statement136", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionInit138: BinaryAssociation = BinaryAssociation(
    name="expressionInit138",
    ends={
        Property(name="pascal_expression140", type=pascal_for_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_for_statement139", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionFin141: BinaryAssociation = BinaryAssociation(
    name="expressionFin141",
    ends={
        Property(name="pascal_expression143", type=pascal_for_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_for_statement142", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stmt144: BinaryAssociation = BinaryAssociation(
    name="stmt144",
    ends={
        Property(name="pascal_statement146", type=pascal_for_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_for_statement145", type=pascal_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifStmt147: BinaryAssociation = BinaryAssociation(
    name="ifStmt147",
    ends={
        Property(name="pascal_if_statement", type=pascal_conditional_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_conditional_statement148", type=pascal_if_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
set171: BinaryAssociation = BinaryAssociation(
    name="set171",
    ends={
        Property(name="pascal_factor172", type=pascal_set, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="pascal_set", type=pascal_factor, multiplicity=Multiplicity(1, 1))
    }
)
function173: BinaryAssociation = BinaryAssociation(
    name="function173",
    ends={
        Property(name="pascal_function_designator175", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor174", type=pascal_function_designator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression176: BinaryAssociation = BinaryAssociation(
    name="expression176",
    ends={
        Property(name="pascal_expression178", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor177", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseStatement155: BinaryAssociation = BinaryAssociation(
    name="elseStatement155",
    ends={
        Property(name="pascal_statement157", type=pascal_if_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_if_statement156", type=pascal_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
not180: BinaryAssociation = BinaryAssociation(
    name="not180",
    ends={
        Property(name="pascal_factor181", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor179", type=pascal_factor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stmt158: BinaryAssociation = BinaryAssociation(
    name="stmt158",
    ends={
        Property(name="pascal_statement160", type=pascal_with_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_with_statement159", type=pascal_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable182: BinaryAssociation = BinaryAssociation(
    name="variable182",
    ends={
        Property(name="pascal_resto", type=pascal_variable, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variable183", type=pascal_resto, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions161: BinaryAssociation = BinaryAssociation(
    name="expressions161",
    ends={
        Property(name="pascal_simple_expression", type=pascal_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_expression162", type=pascal_simple_expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions184: BinaryAssociation = BinaryAssociation(
    name="expressions184",
    ends={
        Property(name="pascal_expression_list", type=pascal_resto, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_resto185", type=pascal_expression_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
array187: BinaryAssociation = BinaryAssociation(
    name="array187",
    ends={
        Property(name="pascal_resto188", type=pascal_resto, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_resto186", type=pascal_resto, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
terms163: BinaryAssociation = BinaryAssociation(
    name="terms163",
    ends={
        Property(name="pascal_EObject", type=pascal_simple_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simple_expression164", type=pascal_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
factors165: BinaryAssociation = BinaryAssociation(
    name="factors165",
    ends={
        Property(name="pascal_factor", type=pascal_term, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_term", type=pascal_factor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable166: BinaryAssociation = BinaryAssociation(
    name="variable166",
    ends={
        Property(name="pascal_variable168", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor167", type=pascal_variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
number169: BinaryAssociation = BinaryAssociation(
    name="number169",
    ends={
        Property(name="pascal_number", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor170", type=pascal_number, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable190: BinaryAssociation = BinaryAssociation(
    name="variable190",
    ends={
        Property(name="pascal_resto191", type=pascal_resto, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_resto189", type=pascal_resto, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simple204: BinaryAssociation = BinaryAssociation(
    name="simple204",
    ends={
        Property(name="pascal_simple_type", type=pascal_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_type205", type=pascal_simple_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type247: BinaryAssociation = BinaryAssociation(
    name="type247",
    ends={
        Property(name="pascal_type249", type=pascal_file_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_file_type248", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pointer193: BinaryAssociation = BinaryAssociation(
    name="pointer193",
    ends={
        Property(name="pascal_resto194", type=pascal_resto, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_resto192", type=pascal_resto, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type250: BinaryAssociation = BinaryAssociation(
    name="type250",
    ends={
        Property(name="pascal_type252", type=pascal_pointer_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_pointer_type251", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structured206: BinaryAssociation = BinaryAssociation(
    name="structured206",
    ends={
        Property(name="pascal_structured_type", type=pascal_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_type207", type=pascal_structured_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pointer208: BinaryAssociation = BinaryAssociation(
    name="pointer208",
    ends={
        Property(name="pascal_pointer_type", type=pascal_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_type209", type=pascal_pointer_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions195: BinaryAssociation = BinaryAssociation(
    name="expressions195",
    ends={
        Property(name="pascal_expression_list197", type=pascal_set, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_set196", type=pascal_expression_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subrange210: BinaryAssociation = BinaryAssociation(
    name="subrange210",
    ends={
        Property(name="pascal_subrange_type", type=pascal_simple_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simple_type211", type=pascal_subrange_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions198: BinaryAssociation = BinaryAssociation(
    name="expressions198",
    ends={
        Property(name="pascal_expression200", type=pascal_expression_list, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_expression_list199", type=pascal_expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumerated212: BinaryAssociation = BinaryAssociation(
    name="enumerated212",
    ends={
        Property(name="pascal_enumerated_type", type=pascal_simple_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simple_type213", type=pascal_enumerated_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifiers214: BinaryAssociation = BinaryAssociation(
    name="identifiers214",
    ends={
        Property(name="pascal_identifier_list216", type=pascal_enumerated_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_enumerated_type215", type=pascal_identifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions201: BinaryAssociation = BinaryAssociation(
    name="expressions201",
    ends={
        Property(name="pascal_expression_list203", type=pascal_function_designator, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_function_designator202", type=pascal_expression_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialConst217: BinaryAssociation = BinaryAssociation(
    name="initialConst217",
    ends={
        Property(name="pascal_constant219", type=pascal_subrange_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_subrange_type218", type=pascal_constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finalConst220: BinaryAssociation = BinaryAssociation(
    name="finalConst220",
    ends={
        Property(name="pascal_constant222", type=pascal_subrange_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_subrange_type221", type=pascal_constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
const223: BinaryAssociation = BinaryAssociation(
    name="const223",
    ends={
        Property(name="pascal_constant225", type=pascal_subrange_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_subrange_type224", type=pascal_constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type226: BinaryAssociation = BinaryAssociation(
    name="type226",
    ends={
        Property(name="pascal_unpacked_structured_type", type=pascal_structured_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_structured_type227", type=pascal_unpacked_structured_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
array228: BinaryAssociation = BinaryAssociation(
    name="array228",
    ends={
        Property(name="pascal_array_type", type=pascal_unpacked_structured_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unpacked_structured_type229", type=pascal_array_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
record230: BinaryAssociation = BinaryAssociation(
    name="record230",
    ends={
        Property(name="pascal_record_type", type=pascal_unpacked_structured_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unpacked_structured_type231", type=pascal_record_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
set232: BinaryAssociation = BinaryAssociation(
    name="set232",
    ends={
        Property(name="pascal_set_type", type=pascal_unpacked_structured_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unpacked_structured_type233", type=pascal_set_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
file234: BinaryAssociation = BinaryAssociation(
    name="file234",
    ends={
        Property(name="pascal_file_type", type=pascal_unpacked_structured_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unpacked_structured_type235", type=pascal_file_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
indexes236: BinaryAssociation = BinaryAssociation(
    name="indexes236",
    ends={
        Property(name="pascal_simple_type238", type=pascal_array_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_array_type237", type=pascal_simple_type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type239: BinaryAssociation = BinaryAssociation(
    name="type239",
    ends={
        Property(name="pascal_type241", type=pascal_array_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_array_type240", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fields242: BinaryAssociation = BinaryAssociation(
    name="fields242",
    ends={
        Property(name="pascal_field_list", type=pascal_record_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_record_type243", type=pascal_field_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type244: BinaryAssociation = BinaryAssociation(
    name="type244",
    ends={
        Property(name="pascal_type246", type=pascal_set_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_set_type245", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fixed253: BinaryAssociation = BinaryAssociation(
    name="fixed253",
    ends={
        Property(name="pascal_fixed_part", type=pascal_field_list, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_field_list254", type=pascal_fixed_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variants255: BinaryAssociation = BinaryAssociation(
    name="variants255",
    ends={
        Property(name="pascal_variant_part", type=pascal_field_list, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_field_list256", type=pascal_variant_part, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sections257: BinaryAssociation = BinaryAssociation(
    name="sections257",
    ends={
        Property(name="pascal_record_section", type=pascal_fixed_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_fixed_part258", type=pascal_record_section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifiers259: BinaryAssociation = BinaryAssociation(
    name="identifiers259",
    ends={
        Property(name="pascal_identifier_list261", type=pascal_record_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_record_section260", type=pascal_identifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type262: BinaryAssociation = BinaryAssociation(
    name="type262",
    ends={
        Property(name="pascal_type264", type=pascal_record_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_record_section263", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tag265: BinaryAssociation = BinaryAssociation(
    name="tag265",
    ends={
        Property(name="pascal_tag_field", type=pascal_variant_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variant_part266", type=pascal_tag_field, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variants267: BinaryAssociation = BinaryAssociation(
    name="variants267",
    ends={
        Property(name="pascal_variant", type=pascal_variant_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variant_part268", type=pascal_variant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
labels269: BinaryAssociation = BinaryAssociation(
    name="labels269",
    ends={
        Property(name="pascal_case_label_list", type=pascal_variant, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variant270", type=pascal_case_label_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fields271: BinaryAssociation = BinaryAssociation(
    name="fields271",
    ends={
        Property(name="pascal_field_list273", type=pascal_variant, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variant272", type=pascal_field_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
number274: BinaryAssociation = BinaryAssociation(
    name="number274",
    ends={
        Property(name="pascal_any_number", type=pascal_number, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_number275", type=pascal_any_number, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
number276: BinaryAssociation = BinaryAssociation(
    name="number276",
    ends={
        Property(name="pascal_number278", type=pascal_constant, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_constant277", type=pascal_number, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constants279: BinaryAssociation = BinaryAssociation(
    name="constants279",
    ends={
        Property(name="pascal_constant281", type=pascal_case_label_list, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_case_label_list280", type=pascal_constant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_pascal_abstraction_heading_abstraction_declaration = Generalization(general=abstraction_declaration, specific=pascal_abstraction_heading)

# Domain Model
domain_model = DomainModel(
    name="pascal",
    types={pascal_identifier_list, pascal_program, pascal_program_heading, pascal_block, pascal_variable_identifier_list, pascal_abstraction_heading, pascal_declaration_part, pascal_statement_part, pascal_label_declaration_part, pascal_constant_definition_part, pascal_type_definition_part, pascal_variable_declaration_part, pascal_procedure_and_function_declaration_part, pascal_label, pascal_constant_definition, pascal_constant, pascal_type_definition, pascal_type, pascal_variable_section, pascal_conformant_array_schema, pascal_abstraction_declaration, abstraction_declaration, pascal_formal_parameter_list, pascal_statement_sequence, pascal_formal_parameter_section, pascal_value_parameter_section, pascal_variable_parameter_section, pascal_parameter_type, pascal_packed_conformant_array_schema, pascal_unpacked_conformant_array_schema, pascal_bound_specification, pascal_statement, pascal_simple_statement, pascal_structured_statement, pascal_assignment_statement, pascal_function_designator, pascal_goto_statement, pascal_variable, pascal_expression, pascal_compound_statement, pascal_repetitive_statement, pascal_conditional_statement, pascal_with_statement, pascal_while_statement, pascal_repeat_statement, pascal_for_statement, pascal_if_statement, pascal_resto, pascal_simple_expression, pascal_expression_list, pascal_EObject, pascal_term, pascal_factor, pascal_number, pascal_set, pascal_simple_type, pascal_structured_type, pascal_pointer_type, pascal_subrange_type, pascal_enumerated_type, pascal_unpacked_structured_type, pascal_array_type, pascal_record_type, pascal_set_type, pascal_file_type, pascal_field_list, pascal_fixed_part, pascal_variant_part, pascal_record_section, pascal_tag_field, pascal_variant, pascal_case_label_list, pascal_any_number},
    associations={identifiers3, heading0, block1, identifiers31, type33, declaration5, statement7, label_decl9, constant_def11, type_def13, variable_decl15, abstraction17, labels19, consts21, const23, types25, type27, sections29, type70, array73, procedures36, functions38, parameters40, heading42, block45, sequence48, parameters50, value52, variable54, procedure56, function59, identifiers62, type65, identifiers67, expression104, label106, packed75, unpacked77, bound79, bounds81, type84, statements87, label89, simple92, structured94, assignment96, function98, goto100, variable102, expression149, ifStatement152, compound109, repetitive111, conditional113, with_stt115, sequence117, while120, repeat122, for124, expression126, statement129, sequence132, expression135, expressionInit138, expressionFin141, stmt144, ifStmt147, set171, function173, expression176, elseStatement155, not180, stmt158, variable182, expressions161, expressions184, array187, terms163, factors165, variable166, number169, variable190, simple204, type247, pointer193, type250, structured206, pointer208, expressions195, subrange210, expressions198, enumerated212, identifiers214, expressions201, initialConst217, finalConst220, const223, type226, array228, record230, set232, file234, indexes236, type239, fields242, type244, fixed253, variants255, sections257, identifiers259, type262, tag265, variants267, labels269, fields271, number274, number276, constants279},
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