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
pascal_Model = Class(name="pascal::Model")
pascal_program = Class(name="pascal::program")
pascal_program_heading = Class(name="pascal::program::heading")
pascal_statement_part = Class(name="pascal::statement::part")
pascal_label_declaration_part = Class(name="pascal::label::declaration::part")
pascal_constant_definition_part = Class(name="pascal::constant::definition::part")
pascal_type_definition_part = Class(name="pascal::type::definition::part")
pascal_variable_declaration = Class(name="pascal::variable::declaration")
pascal_block = Class(name="pascal::block")
pascal_identifier_list = Class(name="pascal::identifier::list")
pascal_DeclarationPart = Class(name="pascal::DeclarationPart")
pascal_type = Class(name="pascal::type")
pascal_procedure_declaration = Class(name="pascal::procedure::declaration")
pascal_variable_declaration_part = Class(name="pascal::variable::declaration::part")
pascal_function_declaration = Class(name="pascal::function::declaration")
pascal_procedure_and_function_declaration_part = Class(name="pascal::procedure::and::function::declaration::part")
pascal_label = Class(name="pascal::label")
pascal_constant_definition = Class(name="pascal::constant::definition")
pascal_type_definition = Class(name="pascal::type::definition")
pascal_procedure_heading = Class(name="pascal::procedure::heading")
pascal_function_heading = Class(name="pascal::function::heading")
pascal_formal_parameter_section = Class(name="pascal::formal::parameter::section")
pascal_formal_parameter_list = Class(name="pascal::formal::parameter::list")
pascal_conformant_array_schema = Class(name="pascal::conformant::array::schema")
pascal_value_parameter_section = Class(name="pascal::value::parameter::section")
pascal_variable_parameter_section = Class(name="pascal::variable::parameter::section")
pascal_parameter_type = Class(name="pascal::parameter::type")
pascal_statement_sequence = Class(name="pascal::statement::sequence")
statement_part = Class(name="statement::part")
pascal_statement = Class(name="pascal::statement")
pascal_EObject = Class(name="pascal::EObject")
pascal_simple_statement = Class(name="pascal::simple::statement")
pascal_assignment_statement = Class(name="pascal::assignment::statement")
simple_statement = Class(name="simple::statement")
pascal_packed_conformant_array_schema = Class(name="pascal::packed::conformant::array::schema")
conformant_array_schema = Class(name="conformant::array::schema")
pascal_bound_specification = Class(name="pascal::bound::specification")
pascal_unpacked_conformant_array_Schema = Class(name="pascal::unpacked::conformant::array::Schema")
pascal_while_statement = Class(name="pascal::while::statement")
repetitive_statement = Class(name="repetitive::statement")
pascal_repeat_statement = Class(name="pascal::repeat::statement")
pascal_expression = Class(name="pascal::expression")
pascal_procedure_statement = Class(name="pascal::procedure::statement")
pascal_goto_statement = Class(name="pascal::goto::statement")
pascal_structured_statement = Class(name="pascal::structured::statement")
pascal_compound_statement = Class(name="pascal::compound::statement")
structured_statement = Class(name="structured::statement")
pascal_repetitive_statement = Class(name="pascal::repetitive::statement")
pascal_case_statement = Class(name="pascal::case::statement")
pascal_for_statement = Class(name="pascal::for::statement")
pascal_conditional_statement = Class(name="pascal::conditional::statement")
pascal_if_statement = Class(name="pascal::if::statement")
pascal_simple_expression = Class(name="pascal::simple::expression")
pascal_case_limb = Class(name="pascal::case::limb")
pascal_case_label_list = Class(name="pascal::case::label::list")
pascal_constant = Class(name="pascal::constant")
pascal_with_statement = Class(name="pascal::with::statement")
pascal_variable = Class(name="pascal::variable")
pascal_Set = Class(name="pascal::Set")
pascal_Variable1 = Class(name="pascal::Variable1")
pascal_term = Class(name="pascal::term")
pascal_factor = Class(name="pascal::factor")
pascal_FunctionDesignator = Class(name="pascal::FunctionDesignator")
pascal_number = Class(name="pascal::number")
type_definition = Class(name="type::definition")
pascal_simple_type = Class(name="pascal::simple::type")
pascal_structured_type = Class(name="pascal::structured::type")
pascal_ExpressionList = Class(name="pascal::ExpressionList")
pascal_ElementList = Class(name="pascal::ElementList")
pascal_unpacked_structured_type = Class(name="pascal::unpacked::structured::type")
pascal_array_type = Class(name="pascal::array::type")
pascal_record_type = Class(name="pascal::record::type")
pascal_pointer_type = Class(name="pascal::pointer::type")
pascal_set_type = Class(name="pascal::set::type")
pascal_subrange_type = Class(name="pascal::subrange::type")
pascal_enumerated_type = Class(name="pascal::enumerated::type")
pascal_field_list = Class(name="pascal::field::list")
pascal_file_type = Class(name="pascal::file::type")
program_heading = Class(name="program::heading")
pascal_fixed_part = Class(name="pascal::fixed::part")
pascal_variant_part = Class(name="pascal::variant::part")
pascal_record_section = Class(name="pascal::record::section")
pascal_tag_field = Class(name="pascal::tag::field")
pascal_variant = Class(name="pascal::variant")
statement = Class(name="statement")
goto_statement = Class(name="goto::statement")
constant_definition = Class(name="constant::definition")

# pascal_Model class attributes and methods

# pascal_program class attributes and methods

# pascal_program_heading class attributes and methods

# pascal_statement_part class attributes and methods

# pascal_label_declaration_part class attributes and methods

# pascal_constant_definition_part class attributes and methods

# pascal_type_definition_part class attributes and methods

# pascal_variable_declaration class attributes and methods

# pascal_block class attributes and methods

# pascal_identifier_list class attributes and methods
pascal_identifier_list_ids: Property = Property(name="ids", type=StringType)
pascal_identifier_list.attributes={pascal_identifier_list_ids}

# pascal_DeclarationPart class attributes and methods

# pascal_type class attributes and methods
pascal_type_name: Property = Property(name="name", type=StringType)
pascal_type.attributes={pascal_type_name}

# pascal_procedure_declaration class attributes and methods
pascal_procedure_declaration_name: Property = Property(name="name", type=StringType)
pascal_procedure_declaration.attributes={pascal_procedure_declaration_name}

# pascal_variable_declaration_part class attributes and methods

# pascal_function_declaration class attributes and methods
pascal_function_declaration_name: Property = Property(name="name", type=StringType)
pascal_function_declaration.attributes={pascal_function_declaration_name}

# pascal_procedure_and_function_declaration_part class attributes and methods

# pascal_label class attributes and methods
pascal_label_int: Property = Property(name="int", type=StringType)
pascal_label.attributes={pascal_label_int}

# pascal_constant_definition class attributes and methods

# pascal_type_definition class attributes and methods

# pascal_procedure_heading class attributes and methods
pascal_procedure_heading_name: Property = Property(name="name", type=StringType)
pascal_procedure_heading.attributes={pascal_procedure_heading_name}

# pascal_function_heading class attributes and methods
pascal_function_heading_id1: Property = Property(name="id1", type=StringType)
pascal_function_heading_id2: Property = Property(name="id2", type=StringType)
pascal_function_heading.attributes={pascal_function_heading_id1, pascal_function_heading_id2}

# pascal_formal_parameter_section class attributes and methods

# pascal_formal_parameter_list class attributes and methods

# pascal_conformant_array_schema class attributes and methods
pascal_conformant_array_schema_id: Property = Property(name="id", type=StringType)
pascal_conformant_array_schema.attributes={pascal_conformant_array_schema_id}

# pascal_value_parameter_section class attributes and methods

# pascal_variable_parameter_section class attributes and methods

# pascal_parameter_type class attributes and methods
pascal_parameter_type_id: Property = Property(name="id", type=StringType)
pascal_parameter_type.attributes={pascal_parameter_type_id}

# pascal_statement_sequence class attributes and methods

# statement_part class attributes and methods

# pascal_statement class attributes and methods

# pascal_EObject class attributes and methods

# pascal_simple_statement class attributes and methods

# pascal_assignment_statement class attributes and methods
pascal_assignment_statement_variable: Property = Property(name="variable", type=StringType)
pascal_assignment_statement_identifier: Property = Property(name="identifier", type=StringType)
pascal_assignment_statement.attributes={pascal_assignment_statement_identifier, pascal_assignment_statement_variable}

# simple_statement class attributes and methods

# pascal_packed_conformant_array_schema class attributes and methods

# conformant_array_schema class attributes and methods

# pascal_bound_specification class attributes and methods
pascal_bound_specification_id3: Property = Property(name="id3", type=StringType)
pascal_bound_specification_id1: Property = Property(name="id1", type=StringType)
pascal_bound_specification_id2: Property = Property(name="id2", type=StringType)
pascal_bound_specification.attributes={pascal_bound_specification_id2, pascal_bound_specification_id3, pascal_bound_specification_id1}

# pascal_unpacked_conformant_array_Schema class attributes and methods

# pascal_while_statement class attributes and methods

# repetitive_statement class attributes and methods

# pascal_repeat_statement class attributes and methods

# pascal_expression class attributes and methods
pascal_expression_relational_operators: Property = Property(name="relational_operators", type=StringType)
pascal_expression.attributes={pascal_expression_relational_operators}

# pascal_procedure_statement class attributes and methods
pascal_procedure_statement_name: Property = Property(name="name", type=StringType)
pascal_procedure_statement_actualParameterList: Property = Property(name="actualParameterList", type=StringType)
pascal_procedure_statement.attributes={pascal_procedure_statement_name, pascal_procedure_statement_actualParameterList}

# pascal_goto_statement class attributes and methods

# pascal_structured_statement class attributes and methods

# pascal_compound_statement class attributes and methods

# structured_statement class attributes and methods

# pascal_repetitive_statement class attributes and methods

# pascal_case_statement class attributes and methods

# pascal_for_statement class attributes and methods
pascal_for_statement_name: Property = Property(name="name", type=StringType)
pascal_for_statement.attributes={pascal_for_statement_name}

# pascal_conditional_statement class attributes and methods

# pascal_if_statement class attributes and methods

# pascal_simple_expression class attributes and methods

# pascal_case_limb class attributes and methods

# pascal_case_label_list class attributes and methods

# pascal_constant class attributes and methods
pascal_constant_name: Property = Property(name="name", type=StringType)
pascal_constant_string: Property = Property(name="string", type=StringType)
pascal_constant.attributes={pascal_constant_string, pascal_constant_name}

# pascal_with_statement class attributes and methods

# pascal_variable class attributes and methods
pascal_variable_name: Property = Property(name="name", type=StringType)
pascal_variable.attributes={pascal_variable_name}

# pascal_Set class attributes and methods

# pascal_Variable1 class attributes and methods
pascal_Variable1_name: Property = Property(name="name", type=StringType)
pascal_Variable1.attributes={pascal_Variable1_name}

# pascal_term class attributes and methods

# pascal_factor class attributes and methods
pascal_factor_nil: Property = Property(name="nil", type=StringType)
pascal_factor_id: Property = Property(name="id", type=StringType)
pascal_factor_string: Property = Property(name="string", type=StringType)
pascal_factor.attributes={pascal_factor_string, pascal_factor_nil, pascal_factor_id}

# pascal_FunctionDesignator class attributes and methods
pascal_FunctionDesignator_name: Property = Property(name="name", type=StringType)
pascal_FunctionDesignator.attributes={pascal_FunctionDesignator_name}

# pascal_number class attributes and methods
pascal_number_integer: Property = Property(name="integer", type=StringType)
pascal_number_real: Property = Property(name="real", type=StringType)
pascal_number.attributes={pascal_number_real, pascal_number_integer}

# type_definition class attributes and methods

# pascal_simple_type class attributes and methods
pascal_simple_type_primitiveType: Property = Property(name="primitiveType", type=StringType)
pascal_simple_type.attributes={pascal_simple_type_primitiveType}

# pascal_structured_type class attributes and methods

# pascal_ExpressionList class attributes and methods

# pascal_ElementList class attributes and methods

# pascal_unpacked_structured_type class attributes and methods

# pascal_array_type class attributes and methods

# pascal_record_type class attributes and methods

# pascal_pointer_type class attributes and methods
pascal_pointer_type_name: Property = Property(name="name", type=StringType)
pascal_pointer_type.attributes={pascal_pointer_type_name}

# pascal_set_type class attributes and methods

# pascal_subrange_type class attributes and methods

# pascal_enumerated_type class attributes and methods

# pascal_field_list class attributes and methods

# pascal_file_type class attributes and methods

# program_heading class attributes and methods

# pascal_fixed_part class attributes and methods

# pascal_variant_part class attributes and methods
pascal_variant_part_id: Property = Property(name="id", type=StringType)
pascal_variant_part.attributes={pascal_variant_part_id}

# pascal_record_section class attributes and methods

# pascal_tag_field class attributes and methods
pascal_tag_field_id: Property = Property(name="id", type=StringType)
pascal_tag_field.attributes={pascal_tag_field_id}

# pascal_variant class attributes and methods

# statement class attributes and methods

# goto_statement class attributes and methods

# constant_definition class attributes and methods

# Relationships
programs0: BinaryAssociation = BinaryAssociation(
    name="programs0",
    ends={
        Property(name="pascal_program", type=pascal_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_Model", type=pascal_program, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
program1: BinaryAssociation = BinaryAssociation(
    name="program1",
    ends={
        Property(name="pascal_program_heading", type=pascal_program, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_program2", type=pascal_program_heading, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statementPart7: BinaryAssociation = BinaryAssociation(
    name="statementPart7",
    ends={
        Property(name="pascal_statement_part", type=pascal_block, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_block8", type=pascal_statement_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labelDeclarationPart9: BinaryAssociation = BinaryAssociation(
    name="labelDeclarationPart9",
    ends={
        Property(name="pascal_label_declaration_part", type=pascal_DeclarationPart, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_DeclarationPart10", type=pascal_label_declaration_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constantDefinitionPart11: BinaryAssociation = BinaryAssociation(
    name="constantDefinitionPart11",
    ends={
        Property(name="pascal_constant_definition_part", type=pascal_DeclarationPart, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_DeclarationPart12", type=pascal_constant_definition_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableDeclarations25: BinaryAssociation = BinaryAssociation(
    name="variableDeclarations25",
    ends={
        Property(name="pascal_variable_declaration", type=pascal_variable_declaration_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variable_declaration_part26", type=pascal_variable_declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block3: BinaryAssociation = BinaryAssociation(
    name="block3",
    ends={
        Property(name="pascal_block", type=pascal_program, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_program4", type=pascal_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifierList27: BinaryAssociation = BinaryAssociation(
    name="identifierList27",
    ends={
        Property(name="pascal_identifier_list", type=pascal_variable_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variable_declaration28", type=pascal_identifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarationPart5: BinaryAssociation = BinaryAssociation(
    name="declarationPart5",
    ends={
        Property(name="pascal_DeclarationPart", type=pascal_block, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_block6", type=pascal_DeclarationPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type29: BinaryAssociation = BinaryAssociation(
    name="type29",
    ends={
        Property(name="pascal_type", type=pascal_variable_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variable_declaration30", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeDefinitionPart13: BinaryAssociation = BinaryAssociation(
    name="typeDefinitionPart13",
    ends={
        Property(name="pascal_type_definition_part", type=pascal_DeclarationPart, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_DeclarationPart14", type=pascal_type_definition_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
procedureDeclarations31: BinaryAssociation = BinaryAssociation(
    name="procedureDeclarations31",
    ends={
        Property(name="pascal_procedure_declaration", type=pascal_procedure_and_function_declaration_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_procedure_and_function_declaration_part32", type=pascal_procedure_declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variableDeclarationPart15: BinaryAssociation = BinaryAssociation(
    name="variableDeclarationPart15",
    ends={
        Property(name="pascal_variable_declaration_part", type=pascal_DeclarationPart, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_DeclarationPart16", type=pascal_variable_declaration_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functionDeclarations33: BinaryAssociation = BinaryAssociation(
    name="functionDeclarations33",
    ends={
        Property(name="pascal_function_declaration", type=pascal_procedure_and_function_declaration_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_procedure_and_function_declaration_part34", type=pascal_function_declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
procedureAndFunctionDeclarationPart17: BinaryAssociation = BinaryAssociation(
    name="procedureAndFunctionDeclarationPart17",
    ends={
        Property(name="pascal_procedure_and_function_declaration_part", type=pascal_DeclarationPart, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_DeclarationPart18", type=pascal_procedure_and_function_declaration_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labels19: BinaryAssociation = BinaryAssociation(
    name="labels19",
    ends={
        Property(name="pascal_label", type=pascal_label_declaration_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_label_declaration_part20", type=pascal_label, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constantDefinitions21: BinaryAssociation = BinaryAssociation(
    name="constantDefinitions21",
    ends={
        Property(name="pascal_constant_definition", type=pascal_constant_definition_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_constant_definition_part22", type=pascal_constant_definition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeDefinitions23: BinaryAssociation = BinaryAssociation(
    name="typeDefinitions23",
    ends={
        Property(name="pascal_type_definition", type=pascal_type_definition_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_type_definition_part24", type=pascal_type_definition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
FormalParameterList49: BinaryAssociation = BinaryAssociation(
    name="FormalParameterList49",
    ends={
        Property(name="pascal_formal_parameter_list50", type=pascal_procedure_heading, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_procedure_heading", type=pascal_formal_parameter_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
FormalParameterList51: BinaryAssociation = BinaryAssociation(
    name="FormalParameterList51",
    ends={
        Property(name="pascal_formal_parameter_list52", type=pascal_function_heading, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_function_heading", type=pascal_formal_parameter_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
FormalParameterSections53: BinaryAssociation = BinaryAssociation(
    name="FormalParameterSections53",
    ends={
        Property(name="pascal_formal_parameter_section", type=pascal_formal_parameter_list, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_formal_parameter_list54", type=pascal_formal_parameter_section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formalParameterList35: BinaryAssociation = BinaryAssociation(
    name="formalParameterList35",
    ends={
        Property(name="pascal_formal_parameter_list", type=pascal_procedure_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_procedure_declaration36", type=pascal_formal_parameter_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block37: BinaryAssociation = BinaryAssociation(
    name="block37",
    ends={
        Property(name="pascal_block39", type=pascal_procedure_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_procedure_declaration38", type=pascal_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameterList40: BinaryAssociation = BinaryAssociation(
    name="formalParameterList40",
    ends={
        Property(name="pascal_formal_parameter_list42", type=pascal_function_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_function_declaration41", type=pascal_formal_parameter_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type43: BinaryAssociation = BinaryAssociation(
    name="type43",
    ends={
        Property(name="pascal_type45", type=pascal_function_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_function_declaration44", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block46: BinaryAssociation = BinaryAssociation(
    name="block46",
    ends={
        Property(name="pascal_block48", type=pascal_function_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_function_declaration47", type=pascal_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterType68: BinaryAssociation = BinaryAssociation(
    name="parameterType68",
    ends={
        Property(name="pascal_parameter_type", type=pascal_value_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_value_parameter_section69", type=pascal_parameter_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifierList70: BinaryAssociation = BinaryAssociation(
    name="identifierList70",
    ends={
        Property(name="pascal_identifier_list72", type=pascal_variable_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variable_parameter_section71", type=pascal_identifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterType73: BinaryAssociation = BinaryAssociation(
    name="parameterType73",
    ends={
        Property(name="pascal_parameter_type75", type=pascal_variable_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variable_parameter_section74", type=pascal_parameter_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conformantArraySchema76: BinaryAssociation = BinaryAssociation(
    name="conformantArraySchema76",
    ends={
        Property(name="pascal_conformant_array_schema", type=pascal_parameter_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_parameter_type77", type=pascal_conformant_array_schema, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
valueParameterSection55: BinaryAssociation = BinaryAssociation(
    name="valueParameterSection55",
    ends={
        Property(name="pascal_value_parameter_section", type=pascal_formal_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_formal_parameter_section56", type=pascal_value_parameter_section, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableParamenterSection57: BinaryAssociation = BinaryAssociation(
    name="variableParamenterSection57",
    ends={
        Property(name="pascal_variable_parameter_section", type=pascal_formal_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_formal_parameter_section58", type=pascal_variable_parameter_section, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
procedureHeading59: BinaryAssociation = BinaryAssociation(
    name="procedureHeading59",
    ends={
        Property(name="pascal_procedure_heading61", type=pascal_formal_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_formal_parameter_section60", type=pascal_procedure_heading, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functionHeading62: BinaryAssociation = BinaryAssociation(
    name="functionHeading62",
    ends={
        Property(name="pascal_function_heading64", type=pascal_formal_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_formal_parameter_section63", type=pascal_function_heading, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifierList65: BinaryAssociation = BinaryAssociation(
    name="identifierList65",
    ends={
        Property(name="pascal_identifier_list67", type=pascal_value_parameter_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_value_parameter_section66", type=pascal_identifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements84: BinaryAssociation = BinaryAssociation(
    name="statements84",
    ends={
        Property(name="pascal_statement", type=pascal_statement_sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_statement_sequence", type=pascal_statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement85: BinaryAssociation = BinaryAssociation(
    name="statement85",
    ends={
        Property(name="pascal_EObject", type=pascal_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_statement86", type=pascal_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
boundSpecification78: BinaryAssociation = BinaryAssociation(
    name="boundSpecification78",
    ends={
        Property(name="pascal_bound_specification", type=pascal_packed_conformant_array_schema, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_packed_conformant_array_schema", type=pascal_bound_specification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
boundSpecifications79: BinaryAssociation = BinaryAssociation(
    name="boundSpecifications79",
    ends={
        Property(name="pascal_bound_specification80", type=pascal_unpacked_conformant_array_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unpacked_conformant_array_Schema", type=pascal_bound_specification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conformantArraySchema81: BinaryAssociation = BinaryAssociation(
    name="conformantArraySchema81",
    ends={
        Property(name="pascal_conformant_array_schema83", type=pascal_unpacked_conformant_array_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unpacked_conformant_array_Schema82", type=pascal_conformant_array_schema, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression90: BinaryAssociation = BinaryAssociation(
    name="expression90",
    ends={
        Property(name="pascal_expression91", type=pascal_while_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_while_statement", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement92: BinaryAssociation = BinaryAssociation(
    name="statement92",
    ends={
        Property(name="pascal_statement94", type=pascal_while_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_while_statement93", type=pascal_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statementSequence95: BinaryAssociation = BinaryAssociation(
    name="statementSequence95",
    ends={
        Property(name="pascal_statement_sequence96", type=pascal_repeat_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_repeat_statement", type=pascal_statement_sequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression87: BinaryAssociation = BinaryAssociation(
    name="expression87",
    ends={
        Property(name="pascal_expression", type=pascal_assignment_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_assignment_statement", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statementSequence88: BinaryAssociation = BinaryAssociation(
    name="statementSequence88",
    ends={
        Property(name="pascal_statement_sequence89", type=pascal_compound_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_compound_statement", type=pascal_statement_sequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
caseStatement109: BinaryAssociation = BinaryAssociation(
    name="caseStatement109",
    ends={
        Property(name="pascal_case_statement", type=pascal_conditional_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_conditional_statement110", type=pascal_case_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression111: BinaryAssociation = BinaryAssociation(
    name="expression111",
    ends={
        Property(name="pascal_expression113", type=pascal_if_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_if_statement112", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifStatement114: BinaryAssociation = BinaryAssociation(
    name="ifStatement114",
    ends={
        Property(name="pascal_statement116", type=pascal_if_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_if_statement115", type=pascal_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseStatement117: BinaryAssociation = BinaryAssociation(
    name="elseStatement117",
    ends={
        Property(name="pascal_statement119", type=pascal_if_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_if_statement118", type=pascal_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression97: BinaryAssociation = BinaryAssociation(
    name="expression97",
    ends={
        Property(name="pascal_expression99", type=pascal_repeat_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_repeat_statement98", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression1100: BinaryAssociation = BinaryAssociation(
    name="expression1100",
    ends={
        Property(name="pascal_expression101", type=pascal_for_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_for_statement", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression2102: BinaryAssociation = BinaryAssociation(
    name="expression2102",
    ends={
        Property(name="pascal_expression104", type=pascal_for_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_for_statement103", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement105: BinaryAssociation = BinaryAssociation(
    name="statement105",
    ends={
        Property(name="pascal_statement107", type=pascal_for_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_for_statement106", type=pascal_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifStatement108: BinaryAssociation = BinaryAssociation(
    name="ifStatement108",
    ends={
        Property(name="pascal_if_statement", type=pascal_conditional_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_conditional_statement", type=pascal_if_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables132: BinaryAssociation = BinaryAssociation(
    name="variables132",
    ends={
        Property(name="pascal_variable", type=pascal_with_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_with_statement", type=pascal_variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement133: BinaryAssociation = BinaryAssociation(
    name="statement133",
    ends={
        Property(name="pascal_statement135", type=pascal_with_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_with_statement134", type=pascal_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleExpressions136: BinaryAssociation = BinaryAssociation(
    name="simpleExpressions136",
    ends={
        Property(name="pascal_simple_expression", type=pascal_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_expression137", type=pascal_simple_expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression120: BinaryAssociation = BinaryAssociation(
    name="expression120",
    ends={
        Property(name="pascal_expression122", type=pascal_case_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_case_statement121", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
caseLimbs123: BinaryAssociation = BinaryAssociation(
    name="caseLimbs123",
    ends={
        Property(name="pascal_case_limb", type=pascal_case_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_case_statement124", type=pascal_case_limb, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
caseLabelList125: BinaryAssociation = BinaryAssociation(
    name="caseLabelList125",
    ends={
        Property(name="pascal_case_label_list", type=pascal_case_limb, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_case_limb126", type=pascal_case_label_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement127: BinaryAssociation = BinaryAssociation(
    name="statement127",
    ends={
        Property(name="pascal_statement129", type=pascal_case_limb, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_case_limb128", type=pascal_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constants130: BinaryAssociation = BinaryAssociation(
    name="constants130",
    ends={
        Property(name="pascal_constant", type=pascal_case_label_list, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_case_label_list131", type=pascal_constant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
set149: BinaryAssociation = BinaryAssociation(
    name="set149",
    ends={
        Property(name="pascal_Set", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor150", type=pascal_Set, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression151: BinaryAssociation = BinaryAssociation(
    name="expression151",
    ends={
        Property(name="pascal_expression153", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor152", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
factor155: BinaryAssociation = BinaryAssociation(
    name="factor155",
    ends={
        Property(name="pascal_factor156", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor154", type=pascal_factor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
terms138: BinaryAssociation = BinaryAssociation(
    name="terms138",
    ends={
        Property(name="pascal_term", type=pascal_simple_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simple_expression139", type=pascal_term, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
factors140: BinaryAssociation = BinaryAssociation(
    name="factors140",
    ends={
        Property(name="pascal_factor", type=pascal_term, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_term141", type=pascal_factor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionDesignator142: BinaryAssociation = BinaryAssociation(
    name="functionDesignator142",
    ends={
        Property(name="pascal_FunctionDesignator", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor143", type=pascal_FunctionDesignator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable144: BinaryAssociation = BinaryAssociation(
    name="variable144",
    ends={
        Property(name="pascal_variable146", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor145", type=pascal_variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
number147: BinaryAssociation = BinaryAssociation(
    name="number147",
    ends={
        Property(name="pascal_number", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor148", type=pascal_number, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleType169: BinaryAssociation = BinaryAssociation(
    name="simpleType169",
    ends={
        Property(name="pascal_simple_type", type=pascal_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_type170", type=pascal_simple_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structuredType171: BinaryAssociation = BinaryAssociation(
    name="structuredType171",
    ends={
        Property(name="pascal_structured_type", type=pascal_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_type172", type=pascal_structured_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable1157: BinaryAssociation = BinaryAssociation(
    name="variable1157",
    ends={
        Property(name="pascal_Variable1", type=pascal_variable, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variable158", type=pascal_Variable1, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionList159: BinaryAssociation = BinaryAssociation(
    name="expressionList159",
    ends={
        Property(name="pascal_ExpressionList", type=pascal_Variable1, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_Variable1160", type=pascal_ExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable1162: BinaryAssociation = BinaryAssociation(
    name="variable1162",
    ends={
        Property(name="pascal_Variable1163", type=pascal_Variable1, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_Variable1161", type=pascal_Variable1, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elementList164: BinaryAssociation = BinaryAssociation(
    name="elementList164",
    ends={
        Property(name="pascal_ElementList", type=pascal_Set, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_Set165", type=pascal_ElementList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant2185: BinaryAssociation = BinaryAssociation(
    name="constant2185",
    ends={
        Property(name="pascal_constant187", type=pascal_subrange_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_subrange_type186", type=pascal_constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions166: BinaryAssociation = BinaryAssociation(
    name="expressions166",
    ends={
        Property(name="pascal_expression168", type=pascal_ElementList, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_ElementList167", type=pascal_expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unpackedStructuredType188: BinaryAssociation = BinaryAssociation(
    name="unpackedStructuredType188",
    ends={
        Property(name="pascal_unpacked_structured_type", type=pascal_structured_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_structured_type189", type=pascal_unpacked_structured_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrayType190: BinaryAssociation = BinaryAssociation(
    name="arrayType190",
    ends={
        Property(name="pascal_array_type", type=pascal_unpacked_structured_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unpacked_structured_type191", type=pascal_array_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
recordType192: BinaryAssociation = BinaryAssociation(
    name="recordType192",
    ends={
        Property(name="pascal_record_type", type=pascal_unpacked_structured_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unpacked_structured_type193", type=pascal_record_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pointerType173: BinaryAssociation = BinaryAssociation(
    name="pointerType173",
    ends={
        Property(name="pascal_pointer_type", type=pascal_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_type174", type=pascal_pointer_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subrangeType175: BinaryAssociation = BinaryAssociation(
    name="subrangeType175",
    ends={
        Property(name="pascal_subrange_type", type=pascal_simple_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simple_type176", type=pascal_subrange_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumeratedType177: BinaryAssociation = BinaryAssociation(
    name="enumeratedType177",
    ends={
        Property(name="pascal_enumerated_type", type=pascal_simple_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simple_type178", type=pascal_enumerated_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifierList179: BinaryAssociation = BinaryAssociation(
    name="identifierList179",
    ends={
        Property(name="pascal_identifier_list181", type=pascal_enumerated_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_enumerated_type180", type=pascal_identifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant182: BinaryAssociation = BinaryAssociation(
    name="constant182",
    ends={
        Property(name="pascal_constant184", type=pascal_subrange_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_subrange_type183", type=pascal_constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fieldlist204: BinaryAssociation = BinaryAssociation(
    name="fieldlist204",
    ends={
        Property(name="pascal_field_list", type=pascal_record_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_record_type205", type=pascal_field_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type206: BinaryAssociation = BinaryAssociation(
    name="type206",
    ends={
        Property(name="pascal_type208", type=pascal_set_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_set_type207", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type209: BinaryAssociation = BinaryAssociation(
    name="type209",
    ends={
        Property(name="pascal_type211", type=pascal_file_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_file_type210", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
setType194: BinaryAssociation = BinaryAssociation(
    name="setType194",
    ends={
        Property(name="pascal_set_type", type=pascal_unpacked_structured_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unpacked_structured_type195", type=pascal_set_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fileType196: BinaryAssociation = BinaryAssociation(
    name="fileType196",
    ends={
        Property(name="pascal_file_type", type=pascal_unpacked_structured_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unpacked_structured_type197", type=pascal_file_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleTypes198: BinaryAssociation = BinaryAssociation(
    name="simpleTypes198",
    ends={
        Property(name="pascal_simple_type200", type=pascal_array_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_array_type199", type=pascal_simple_type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type201: BinaryAssociation = BinaryAssociation(
    name="type201",
    ends={
        Property(name="pascal_type203", type=pascal_array_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_array_type202", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
caseLabelList228: BinaryAssociation = BinaryAssociation(
    name="caseLabelList228",
    ends={
        Property(name="pascal_case_label_list230", type=pascal_variant, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variant229", type=pascal_case_label_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fieldList231: BinaryAssociation = BinaryAssociation(
    name="fieldList231",
    ends={
        Property(name="pascal_field_list233", type=pascal_variant, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variant232", type=pascal_field_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions234: BinaryAssociation = BinaryAssociation(
    name="expressions234",
    ends={
        Property(name="pascal_expression236", type=pascal_ExpressionList, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_ExpressionList235", type=pascal_expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fixedPart212: BinaryAssociation = BinaryAssociation(
    name="fixedPart212",
    ends={
        Property(name="pascal_fixed_part", type=pascal_field_list, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_field_list213", type=pascal_fixed_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variantPart214: BinaryAssociation = BinaryAssociation(
    name="variantPart214",
    ends={
        Property(name="pascal_variant_part", type=pascal_field_list, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_field_list215", type=pascal_variant_part, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
recordSections216: BinaryAssociation = BinaryAssociation(
    name="recordSections216",
    ends={
        Property(name="pascal_record_section", type=pascal_fixed_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_fixed_part217", type=pascal_record_section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifierList218: BinaryAssociation = BinaryAssociation(
    name="identifierList218",
    ends={
        Property(name="pascal_identifier_list220", type=pascal_record_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_record_section219", type=pascal_identifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type221: BinaryAssociation = BinaryAssociation(
    name="type221",
    ends={
        Property(name="pascal_type223", type=pascal_record_section, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_record_section222", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tagfield224: BinaryAssociation = BinaryAssociation(
    name="tagfield224",
    ends={
        Property(name="pascal_tag_field", type=pascal_variant_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variant_part225", type=pascal_tag_field, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variants226: BinaryAssociation = BinaryAssociation(
    name="variants226",
    ends={
        Property(name="pascal_variant", type=pascal_variant_part, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variant_part227", type=pascal_variant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
number237: BinaryAssociation = BinaryAssociation(
    name="number237",
    ends={
        Property(name="pascal_number239", type=pascal_constant, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_constant238", type=pascal_number, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_pascal_statement_sequence_statement_part = Generalization(general=statement_part, specific=pascal_statement_sequence)
gen_pascal_assignment_statement_simple_statement = Generalization(general=simple_statement, specific=pascal_assignment_statement)
gen_pascal_packed_conformant_array_schema_conformant_array_schema = Generalization(general=conformant_array_schema, specific=pascal_packed_conformant_array_schema)
gen_pascal_unpacked_conformant_array_Schema_conformant_array_schema = Generalization(general=conformant_array_schema, specific=pascal_unpacked_conformant_array_Schema)
gen_pascal_while_statement_repetitive_statement = Generalization(general=repetitive_statement, specific=pascal_while_statement)
gen_pascal_repeat_statement_repetitive_statement = Generalization(general=repetitive_statement, specific=pascal_repeat_statement)
gen_pascal_procedure_statement_simple_statement = Generalization(general=simple_statement, specific=pascal_procedure_statement)
gen_pascal_goto_statement_simple_statement = Generalization(general=simple_statement, specific=pascal_goto_statement)
gen_pascal_compound_statement_structured_statement = Generalization(general=structured_statement, specific=pascal_compound_statement)
gen_pascal_repetitive_statement_structured_statement = Generalization(general=structured_statement, specific=pascal_repetitive_statement)
gen_pascal_for_statement_repetitive_statement = Generalization(general=repetitive_statement, specific=pascal_for_statement)
gen_pascal_conditional_statement_structured_statement = Generalization(general=structured_statement, specific=pascal_conditional_statement)
gen_pascal_with_statement_structured_statement = Generalization(general=structured_statement, specific=pascal_with_statement)
gen_pascal_type_type_definition = Generalization(general=type_definition, specific=pascal_type)
gen_pascal_identifier_list_program_heading = Generalization(general=program_heading, specific=pascal_identifier_list)
gen_pascal_label_statement = Generalization(general=statement, specific=pascal_label)
gen_pascal_label_goto_statement = Generalization(general=goto_statement, specific=pascal_label)
gen_pascal_constant_constant_definition = Generalization(general=constant_definition, specific=pascal_constant)

# Domain Model
domain_model = DomainModel(
    name="pascal",
    types={pascal_Model, pascal_program, pascal_program_heading, pascal_statement_part, pascal_label_declaration_part, pascal_constant_definition_part, pascal_type_definition_part, pascal_variable_declaration, pascal_block, pascal_identifier_list, pascal_DeclarationPart, pascal_type, pascal_procedure_declaration, pascal_variable_declaration_part, pascal_function_declaration, pascal_procedure_and_function_declaration_part, pascal_label, pascal_constant_definition, pascal_type_definition, pascal_procedure_heading, pascal_function_heading, pascal_formal_parameter_section, pascal_formal_parameter_list, pascal_conformant_array_schema, pascal_value_parameter_section, pascal_variable_parameter_section, pascal_parameter_type, pascal_statement_sequence, statement_part, pascal_statement, pascal_EObject, pascal_simple_statement, pascal_assignment_statement, simple_statement, pascal_packed_conformant_array_schema, conformant_array_schema, pascal_bound_specification, pascal_unpacked_conformant_array_Schema, pascal_while_statement, repetitive_statement, pascal_repeat_statement, pascal_expression, pascal_procedure_statement, pascal_goto_statement, pascal_structured_statement, pascal_compound_statement, structured_statement, pascal_repetitive_statement, pascal_case_statement, pascal_for_statement, pascal_conditional_statement, pascal_if_statement, pascal_simple_expression, pascal_case_limb, pascal_case_label_list, pascal_constant, pascal_with_statement, pascal_variable, pascal_Set, pascal_Variable1, pascal_term, pascal_factor, pascal_FunctionDesignator, pascal_number, type_definition, pascal_simple_type, pascal_structured_type, pascal_ExpressionList, pascal_ElementList, pascal_unpacked_structured_type, pascal_array_type, pascal_record_type, pascal_pointer_type, pascal_set_type, pascal_subrange_type, pascal_enumerated_type, pascal_field_list, pascal_file_type, program_heading, pascal_fixed_part, pascal_variant_part, pascal_record_section, pascal_tag_field, pascal_variant, statement, goto_statement, constant_definition},
    associations={programs0, program1, statementPart7, labelDeclarationPart9, constantDefinitionPart11, variableDeclarations25, block3, identifierList27, declarationPart5, type29, typeDefinitionPart13, procedureDeclarations31, variableDeclarationPart15, functionDeclarations33, procedureAndFunctionDeclarationPart17, labels19, constantDefinitions21, typeDefinitions23, FormalParameterList49, FormalParameterList51, FormalParameterSections53, formalParameterList35, block37, formalParameterList40, type43, block46, parameterType68, identifierList70, parameterType73, conformantArraySchema76, valueParameterSection55, variableParamenterSection57, procedureHeading59, functionHeading62, identifierList65, statements84, statement85, boundSpecification78, boundSpecifications79, conformantArraySchema81, expression90, statement92, statementSequence95, expression87, statementSequence88, caseStatement109, expression111, ifStatement114, elseStatement117, expression97, expression1100, expression2102, statement105, ifStatement108, variables132, statement133, simpleExpressions136, expression120, caseLimbs123, caseLabelList125, statement127, constants130, set149, expression151, factor155, terms138, factors140, functionDesignator142, variable144, number147, simpleType169, structuredType171, variable1157, expressionList159, variable1162, elementList164, constant2185, expressions166, unpackedStructuredType188, arrayType190, recordType192, pointerType173, subrangeType175, enumeratedType177, identifierList179, constant182, fieldlist204, type206, type209, setType194, fileType196, simpleTypes198, type201, caseLabelList228, fieldList231, expressions234, fixedPart212, variantPart214, recordSections216, identifierList218, type221, tagfield224, variants226, number237},
    generalizations={gen_pascal_statement_sequence_statement_part, gen_pascal_assignment_statement_simple_statement, gen_pascal_packed_conformant_array_schema_conformant_array_schema, gen_pascal_unpacked_conformant_array_Schema_conformant_array_schema, gen_pascal_while_statement_repetitive_statement, gen_pascal_repeat_statement_repetitive_statement, gen_pascal_procedure_statement_simple_statement, gen_pascal_goto_statement_simple_statement, gen_pascal_compound_statement_structured_statement, gen_pascal_repetitive_statement_structured_statement, gen_pascal_for_statement_repetitive_statement, gen_pascal_conditional_statement_structured_statement, gen_pascal_with_statement_structured_statement, gen_pascal_type_type_definition, gen_pascal_identifier_list_program_heading, gen_pascal_label_statement, gen_pascal_label_goto_statement, gen_pascal_constant_constant_definition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)