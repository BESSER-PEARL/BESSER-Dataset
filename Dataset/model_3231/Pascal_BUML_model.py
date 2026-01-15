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
pascal_block = Class(name="pascal::block")
pascal_label_declaration = Class(name="pascal::label::declaration")
pascal_type_definition_part = Class(name="pascal::type::definition::part")
pascal_variable_declaration_part = Class(name="pascal::variable::declaration::part")
pascal_program = Class(name="pascal::program")
pascal_program_heading_block = Class(name="pascal::program::heading::block")
pascal_label = Class(name="pascal::label")
pascal_simple_statement = Class(name="pascal::simple::statement")
pascal_structured_statement = Class(name="pascal::structured::statement")
pascal_assignment_statement = Class(name="pascal::assignment::statement")
pascal_function_designator = Class(name="pascal::function::designator")
pascal_constant_definition_part = Class(name="pascal::constant::definition::part")
pascal_function_procedure_declaration = Class(name="pascal::function::procedure::declaration")
pascal_statement_part = Class(name="pascal::statement::part")
pascal_statement_sequence = Class(name="pascal::statement::sequence")
pascal_statement = Class(name="pascal::statement")
pascal_expression_list = Class(name="pascal::expression::list")
pascal_simple_expression = Class(name="pascal::simple::expression")
pascal_EObject = Class(name="pascal::EObject")
pascal_term = Class(name="pascal::term")
pascal_factor = Class(name="pascal::factor")
pascal_compound_statement = Class(name="pascal::compound::statement")
pascal_while_statement = Class(name="pascal::while::statement")
pascal_variable = Class(name="pascal::variable")
pascal_expression = Class(name="pascal::expression")
pascal_formal_parameter_section = Class(name="pascal::formal::parameter::section")
pascal_value_parameter_section = Class(name="pascal::value::parameter::section")
pascal_variable_parameter_section = Class(name="pascal::variable::parameter::section")
pascal_number = Class(name="pascal::number")
pascal_abstraction_declaration = Class(name="pascal::abstraction::declaration")
pascal_abstraction_heading = Class(name="pascal::abstraction::heading")
pascal_formal_parameter_list = Class(name="pascal::formal::parameter::list")
pascal_constant = Class(name="pascal::constant")
pascal_identifier_list = Class(name="pascal::identifier::list")
pascal_parameter_type = Class(name="pascal::parameter::type")
pascal_any_number = Class(name="pascal::any::number")
pascal_simple_type = Class(name="pascal::simple::type")
pascal_structured_type = Class(name="pascal::structured::type")
pascal_constant_definition = Class(name="pascal::constant::definition")
pascal_unpacked_structured_type = Class(name="pascal::unpacked::structured::type")
pascal_type_definition = Class(name="pascal::type::definition")
pascal_type = Class(name="pascal::type")
pascal_field_list = Class(name="pascal::field::list")
pascal_record_section = Class(name="pascal::record::section")
pascal_variable_section = Class(name="pascal::variable::section")
pascal_variable_identifier_list = Class(name="pascal::variable::identifier::list")
pascal_record_type = Class(name="pascal::record::type")

# pascal_block class attributes and methods

# pascal_label_declaration class attributes and methods

# pascal_type_definition_part class attributes and methods

# pascal_variable_declaration_part class attributes and methods

# pascal_program class attributes and methods

# pascal_program_heading_block class attributes and methods
pascal_program_heading_block_name: Property = Property(name="name", type=StringType)
pascal_program_heading_block.attributes={pascal_program_heading_block_name}

# pascal_label class attributes and methods
pascal_label_number: Property = Property(name="number", type=StringType)
pascal_label.attributes={pascal_label_number}

# pascal_simple_statement class attributes and methods
pascal_simple_statement_function_noargs: Property = Property(name="function_noargs", type=StringType)
pascal_simple_statement.attributes={pascal_simple_statement_function_noargs}

# pascal_structured_statement class attributes and methods

# pascal_assignment_statement class attributes and methods

# pascal_function_designator class attributes and methods
pascal_function_designator_name: Property = Property(name="name", type=StringType)
pascal_function_designator.attributes={pascal_function_designator_name}

# pascal_constant_definition_part class attributes and methods

# pascal_function_procedure_declaration class attributes and methods

# pascal_statement_part class attributes and methods

# pascal_statement_sequence class attributes and methods

# pascal_statement class attributes and methods

# pascal_expression_list class attributes and methods

# pascal_simple_expression class attributes and methods
pascal_simple_expression_prefixOperator: Property = Property(name="prefixOperator", type=StringType)
pascal_simple_expression_operators: Property = Property(name="operators", type=StringType)
pascal_simple_expression.attributes={pascal_simple_expression_prefixOperator, pascal_simple_expression_operators}

# pascal_EObject class attributes and methods

# pascal_term class attributes and methods
pascal_term_operators: Property = Property(name="operators", type=StringType)
pascal_term.attributes={pascal_term_operators}

# pascal_factor class attributes and methods
pascal_factor_string: Property = Property(name="string", type=StringType)
pascal_factor_boolean: Property = Property(name="boolean", type=StringType)
pascal_factor_nil: Property = Property(name="nil", type=BooleanType)
pascal_factor.attributes={pascal_factor_nil, pascal_factor_boolean, pascal_factor_string}

# pascal_compound_statement class attributes and methods

# pascal_while_statement class attributes and methods

# pascal_variable class attributes and methods
pascal_variable_name: Property = Property(name="name", type=StringType)
pascal_variable.attributes={pascal_variable_name}

# pascal_expression class attributes and methods
pascal_expression_operators: Property = Property(name="operators", type=StringType)
pascal_expression.attributes={pascal_expression_operators}

# pascal_formal_parameter_section class attributes and methods

# pascal_value_parameter_section class attributes and methods

# pascal_variable_parameter_section class attributes and methods

# pascal_number class attributes and methods

# pascal_abstraction_declaration class attributes and methods

# pascal_abstraction_heading class attributes and methods
pascal_abstraction_heading_returnType: Property = Property(name="returnType", type=StringType)
pascal_abstraction_heading_name: Property = Property(name="name", type=StringType)
pascal_abstraction_heading.attributes={pascal_abstraction_heading_returnType, pascal_abstraction_heading_name}

# pascal_formal_parameter_list class attributes and methods

# pascal_constant class attributes and methods
pascal_constant_opterator: Property = Property(name="opterator", type=StringType)
pascal_constant_name: Property = Property(name="name", type=StringType)
pascal_constant_string: Property = Property(name="string", type=StringType)
pascal_constant_boolLiteral: Property = Property(name="boolLiteral", type=StringType)
pascal_constant_nil: Property = Property(name="nil", type=BooleanType)
pascal_constant.attributes={pascal_constant_boolLiteral, pascal_constant_string, pascal_constant_nil, pascal_constant_opterator, pascal_constant_name}

# pascal_identifier_list class attributes and methods
pascal_identifier_list_names: Property = Property(name="names", type=StringType)
pascal_identifier_list.attributes={pascal_identifier_list_names}

# pascal_parameter_type class attributes and methods
pascal_parameter_type_name: Property = Property(name="name", type=StringType)
pascal_parameter_type.attributes={pascal_parameter_type_name}

# pascal_any_number class attributes and methods
pascal_any_number_integer: Property = Property(name="integer", type=StringType)
pascal_any_number_real: Property = Property(name="real", type=StringType)
pascal_any_number.attributes={pascal_any_number_real, pascal_any_number_integer}

# pascal_simple_type class attributes and methods
pascal_simple_type_name: Property = Property(name="name", type=StringType)
pascal_simple_type.attributes={pascal_simple_type_name}

# pascal_structured_type class attributes and methods

# pascal_constant_definition class attributes and methods
pascal_constant_definition_name: Property = Property(name="name", type=StringType)
pascal_constant_definition.attributes={pascal_constant_definition_name}

# pascal_unpacked_structured_type class attributes and methods

# pascal_type_definition class attributes and methods
pascal_type_definition_name: Property = Property(name="name", type=StringType)
pascal_type_definition.attributes={pascal_type_definition_name}

# pascal_type class attributes and methods

# pascal_field_list class attributes and methods

# pascal_record_section class attributes and methods

# pascal_variable_section class attributes and methods

# pascal_variable_identifier_list class attributes and methods
pascal_variable_identifier_list_names: Property = Property(name="names", type=StringType)
pascal_variable_identifier_list.attributes={pascal_variable_identifier_list_names}

# pascal_record_type class attributes and methods
pascal_record_type_recordKeyword: Property = Property(name="recordKeyword", type=StringType)
pascal_record_type_endKeyword: Property = Property(name="endKeyword", type=StringType)
pascal_record_type.attributes={pascal_record_type_recordKeyword, pascal_record_type_endKeyword}

# Relationships
block1: BinaryAssociation = BinaryAssociation(
    name="block1",
    ends={
        Property(name="pascal_block", type=pascal_program, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_program2", type=pascal_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
label3: BinaryAssociation = BinaryAssociation(
    name="label3",
    ends={
        Property(name="pascal_label_declaration", type=pascal_block, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_block4", type=pascal_label_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="pascal_type_definition_part", type=pascal_block, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_block6", type=pascal_type_definition_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
heading0: BinaryAssociation = BinaryAssociation(
    name="heading0",
    ends={
        Property(name="pascal_program_heading_block", type=pascal_program, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_program", type=pascal_program_heading_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
label19: BinaryAssociation = BinaryAssociation(
    name="label19",
    ends={
        Property(name="pascal_label", type=pascal_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_statement20", type=pascal_label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simple21: BinaryAssociation = BinaryAssociation(
    name="simple21",
    ends={
        Property(name="pascal_simple_statement", type=pascal_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_statement22", type=pascal_simple_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structured23: BinaryAssociation = BinaryAssociation(
    name="structured23",
    ends={
        Property(name="pascal_structured_statement", type=pascal_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_statement24", type=pascal_structured_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment25: BinaryAssociation = BinaryAssociation(
    name="assignment25",
    ends={
        Property(name="pascal_assignment_statement", type=pascal_simple_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simple_statement26", type=pascal_assignment_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function27: BinaryAssociation = BinaryAssociation(
    name="function27",
    ends={
        Property(name="pascal_function_designator", type=pascal_simple_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simple_statement28", type=pascal_function_designator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable7: BinaryAssociation = BinaryAssociation(
    name="variable7",
    ends={
        Property(name="pascal_variable_declaration_part", type=pascal_block, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_block8", type=pascal_variable_declaration_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant9: BinaryAssociation = BinaryAssociation(
    name="constant9",
    ends={
        Property(name="pascal_constant_definition_part", type=pascal_block, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_block10", type=pascal_constant_definition_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
abstraction11: BinaryAssociation = BinaryAssociation(
    name="abstraction11",
    ends={
        Property(name="pascal_function_procedure_declaration", type=pascal_block, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_block12", type=pascal_function_procedure_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement13: BinaryAssociation = BinaryAssociation(
    name="statement13",
    ends={
        Property(name="pascal_statement_part", type=pascal_block, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_block14", type=pascal_statement_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequence15: BinaryAssociation = BinaryAssociation(
    name="sequence15",
    ends={
        Property(name="pascal_statement_sequence", type=pascal_statement_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_statement_part16", type=pascal_statement_sequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements17: BinaryAssociation = BinaryAssociation(
    name="statements17",
    ends={
        Property(name="pascal_statement", type=pascal_statement_sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_statement_sequence18", type=pascal_statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions40: BinaryAssociation = BinaryAssociation(
    name="expressions40",
    ends={
        Property(name="pascal_expression41", type=pascal_expression_list, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_expression_list", type=pascal_expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions42: BinaryAssociation = BinaryAssociation(
    name="expressions42",
    ends={
        Property(name="pascal_simple_expression", type=pascal_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_expression43", type=pascal_simple_expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
terms44: BinaryAssociation = BinaryAssociation(
    name="terms44",
    ends={
        Property(name="pascal_EObject", type=pascal_simple_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simple_expression45", type=pascal_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
factors46: BinaryAssociation = BinaryAssociation(
    name="factors46",
    ends={
        Property(name="pascal_factor", type=pascal_term, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_term", type=pascal_factor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable47: BinaryAssociation = BinaryAssociation(
    name="variable47",
    ends={
        Property(name="pascal_variable49", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor48", type=pascal_variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
compound29: BinaryAssociation = BinaryAssociation(
    name="compound29",
    ends={
        Property(name="pascal_compound_statement", type=pascal_structured_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_structured_statement30", type=pascal_compound_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
while_stmt31: BinaryAssociation = BinaryAssociation(
    name="while_stmt31",
    ends={
        Property(name="pascal_while_statement", type=pascal_structured_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_structured_statement32", type=pascal_while_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequence33: BinaryAssociation = BinaryAssociation(
    name="sequence33",
    ends={
        Property(name="pascal_statement_sequence35", type=pascal_compound_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_compound_statement34", type=pascal_statement_sequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable36: BinaryAssociation = BinaryAssociation(
    name="variable36",
    ends={
        Property(name="pascal_variable", type=pascal_assignment_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_assignment_statement37", type=pascal_variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression38: BinaryAssociation = BinaryAssociation(
    name="expression38",
    ends={
        Property(name="pascal_expression", type=pascal_assignment_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_assignment_statement39", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters69: BinaryAssociation = BinaryAssociation(
    name="parameters69",
    ends={
        Property(name="pascal_abstraction_heading", type=pascal_formal_parameter_list, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="pascal_formal_parameter_list", type=pascal_abstraction_heading, multiplicity=Multiplicity(1, 1))
    }
)
heading70: BinaryAssociation = BinaryAssociation(
    name="heading70",
    ends={
        Property(name="pascal_abstraction_heading72", type=pascal_abstraction_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_abstraction_declaration71", type=pascal_abstraction_heading, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block73: BinaryAssociation = BinaryAssociation(
    name="block73",
    ends={
        Property(name="pascal_block75", type=pascal_abstraction_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_abstraction_declaration74", type=pascal_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters76: BinaryAssociation = BinaryAssociation(
    name="parameters76",
    ends={
        Property(name="pascal_formal_parameter_section", type=pascal_formal_parameter_list, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_formal_parameter_list77", type=pascal_formal_parameter_section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value78: BinaryAssociation = BinaryAssociation(
    name="value78",
    ends={
        Property(name="pascal_value_parameter_section", type=pascal_formal_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_formal_parameter_section79", type=pascal_value_parameter_section, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable80: BinaryAssociation = BinaryAssociation(
    name="variable80",
    ends={
        Property(name="pascal_variable_parameter_section", type=pascal_formal_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_formal_parameter_section81", type=pascal_variable_parameter_section, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
procedure82: BinaryAssociation = BinaryAssociation(
    name="procedure82",
    ends={
        Property(name="pascal_abstraction_heading84", type=pascal_formal_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_formal_parameter_section83", type=pascal_abstraction_heading, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function85: BinaryAssociation = BinaryAssociation(
    name="function85",
    ends={
        Property(name="pascal_abstraction_heading87", type=pascal_formal_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_formal_parameter_section86", type=pascal_abstraction_heading, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
number50: BinaryAssociation = BinaryAssociation(
    name="number50",
    ends={
        Property(name="pascal_number", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor51", type=pascal_number, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function52: BinaryAssociation = BinaryAssociation(
    name="function52",
    ends={
        Property(name="pascal_function_designator54", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor53", type=pascal_function_designator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression55: BinaryAssociation = BinaryAssociation(
    name="expression55",
    ends={
        Property(name="pascal_expression57", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor56", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
not59: BinaryAssociation = BinaryAssociation(
    name="not59",
    ends={
        Property(name="pascal_factor60", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor58", type=pascal_factor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions61: BinaryAssociation = BinaryAssociation(
    name="expressions61",
    ends={
        Property(name="pascal_expression_list63", type=pascal_function_designator, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_function_designator62", type=pascal_expression_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functions64: BinaryAssociation = BinaryAssociation(
    name="functions64",
    ends={
        Property(name="pascal_abstraction_declaration", type=pascal_function_procedure_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_function_procedure_declaration65", type=pascal_abstraction_declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
procedures66: BinaryAssociation = BinaryAssociation(
    name="procedures66",
    ends={
        Property(name="pascal_abstraction_declaration68", type=pascal_function_procedure_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_function_procedure_declaration67", type=pascal_abstraction_declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
number103: BinaryAssociation = BinaryAssociation(
    name="number103",
    ends={
        Property(name="pascal_number104", type=pascal_constant, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_constant", type=pascal_number, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifiers88: BinaryAssociation = BinaryAssociation(
    name="identifiers88",
    ends={
        Property(name="pascal_identifier_list", type=pascal_value_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_value_parameter_section89", type=pascal_identifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type90: BinaryAssociation = BinaryAssociation(
    name="type90",
    ends={
        Property(name="pascal_parameter_type", type=pascal_value_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_value_parameter_section91", type=pascal_parameter_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
indentifiers92: BinaryAssociation = BinaryAssociation(
    name="indentifiers92",
    ends={
        Property(name="pascal_identifier_list94", type=pascal_variable_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variable_parameter_section93", type=pascal_identifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type95: BinaryAssociation = BinaryAssociation(
    name="type95",
    ends={
        Property(name="pascal_parameter_type97", type=pascal_variable_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variable_parameter_section96", type=pascal_parameter_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
number98: BinaryAssociation = BinaryAssociation(
    name="number98",
    ends={
        Property(name="pascal_any_number", type=pascal_number, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_number99", type=pascal_any_number, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labels100: BinaryAssociation = BinaryAssociation(
    name="labels100",
    ends={
        Property(name="pascal_label102", type=pascal_label_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_label_declaration101", type=pascal_label, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
simple114: BinaryAssociation = BinaryAssociation(
    name="simple114",
    ends={
        Property(name="pascal_simple_type", type=pascal_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_type115", type=pascal_simple_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structured116: BinaryAssociation = BinaryAssociation(
    name="structured116",
    ends={
        Property(name="pascal_structured_type", type=pascal_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_type117", type=pascal_structured_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
consts105: BinaryAssociation = BinaryAssociation(
    name="consts105",
    ends={
        Property(name="pascal_constant_definition", type=pascal_constant_definition_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_constant_definition_part106", type=pascal_constant_definition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type118: BinaryAssociation = BinaryAssociation(
    name="type118",
    ends={
        Property(name="pascal_unpacked_structured_type", type=pascal_structured_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_structured_type119", type=pascal_unpacked_structured_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
const107: BinaryAssociation = BinaryAssociation(
    name="const107",
    ends={
        Property(name="pascal_constant109", type=pascal_constant_definition, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_constant_definition108", type=pascal_constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
types110: BinaryAssociation = BinaryAssociation(
    name="types110",
    ends={
        Property(name="pascal_type_definition", type=pascal_type_definition_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_type_definition_part111", type=pascal_type_definition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type112: BinaryAssociation = BinaryAssociation(
    name="type112",
    ends={
        Property(name="pascal_type", type=pascal_type_definition, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_type_definition113", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fields122: BinaryAssociation = BinaryAssociation(
    name="fields122",
    ends={
        Property(name="pascal_field_list", type=pascal_record_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_record_type123", type=pascal_field_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sections124: BinaryAssociation = BinaryAssociation(
    name="sections124",
    ends={
        Property(name="pascal_record_section", type=pascal_field_list, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_field_list125", type=pascal_record_section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifiers126: BinaryAssociation = BinaryAssociation(
    name="identifiers126",
    ends={
        Property(name="pascal_identifier_list128", type=pascal_record_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_record_section127", type=pascal_identifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type129: BinaryAssociation = BinaryAssociation(
    name="type129",
    ends={
        Property(name="pascal_type131", type=pascal_record_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_record_section130", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sections132: BinaryAssociation = BinaryAssociation(
    name="sections132",
    ends={
        Property(name="pascal_variable_section", type=pascal_variable_declaration_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variable_declaration_part133", type=pascal_variable_section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifiers134: BinaryAssociation = BinaryAssociation(
    name="identifiers134",
    ends={
        Property(name="pascal_variable_identifier_list", type=pascal_variable_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variable_section135", type=pascal_variable_identifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
record120: BinaryAssociation = BinaryAssociation(
    name="record120",
    ends={
        Property(name="pascal_record_type", type=pascal_unpacked_structured_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unpacked_structured_type121", type=pascal_record_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression139: BinaryAssociation = BinaryAssociation(
    name="expression139",
    ends={
        Property(name="pascal_expression141", type=pascal_while_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_while_statement140", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement142: BinaryAssociation = BinaryAssociation(
    name="statement142",
    ends={
        Property(name="pascal_statement_sequence144", type=pascal_while_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_while_statement143", type=pascal_statement_sequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type136: BinaryAssociation = BinaryAssociation(
    name="type136",
    ends={
        Property(name="pascal_type138", type=pascal_variable_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variable_section137", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="pascal",
    types={pascal_block, pascal_label_declaration, pascal_type_definition_part, pascal_variable_declaration_part, pascal_program, pascal_program_heading_block, pascal_label, pascal_simple_statement, pascal_structured_statement, pascal_assignment_statement, pascal_function_designator, pascal_constant_definition_part, pascal_function_procedure_declaration, pascal_statement_part, pascal_statement_sequence, pascal_statement, pascal_expression_list, pascal_simple_expression, pascal_EObject, pascal_term, pascal_factor, pascal_compound_statement, pascal_while_statement, pascal_variable, pascal_expression, pascal_formal_parameter_section, pascal_value_parameter_section, pascal_variable_parameter_section, pascal_number, pascal_abstraction_declaration, pascal_abstraction_heading, pascal_formal_parameter_list, pascal_constant, pascal_identifier_list, pascal_parameter_type, pascal_any_number, pascal_simple_type, pascal_structured_type, pascal_constant_definition, pascal_unpacked_structured_type, pascal_type_definition, pascal_type, pascal_field_list, pascal_record_section, pascal_variable_section, pascal_variable_identifier_list, pascal_record_type},
    associations={block1, label3, type5, heading0, label19, simple21, structured23, assignment25, function27, variable7, constant9, abstraction11, statement13, sequence15, statements17, expressions40, expressions42, terms44, factors46, variable47, compound29, while_stmt31, sequence33, variable36, expression38, parameters69, heading70, block73, parameters76, value78, variable80, procedure82, function85, number50, function52, expression55, not59, expressions61, functions64, procedures66, number103, identifiers88, type90, indentifiers92, type95, number98, labels100, simple114, structured116, consts105, type118, const107, types110, type112, fields122, sections124, identifiers126, type129, sections132, identifiers134, record120, expression139, statement142, type136},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)