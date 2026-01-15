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
myDsl_Model = Class(name="myDsl::Model")
myDsl_translation_unit = Class(name="myDsl::translation::unit")
myDsl_external_declaration = Class(name="myDsl::external::declaration")
myDsl_translation_unitR = Class(name="myDsl::translation::unitR")
myDsl_declaration_specifiers = Class(name="myDsl::declaration::specifiers")
myDsl_function_definition = Class(name="myDsl::function::definition")
external_declaration = Class(name="external::declaration")
myDsl_direct_declarator = Class(name="myDsl::direct::declarator")
myDsl_type_qualifier_list = Class(name="myDsl::type::qualifier::list")
pointer = Class(name="pointer")
myDsl_type_qualifier_listR = Class(name="myDsl::type::qualifier::listR")
declarator = Class(name="declarator")
myDsl_direct_declaratorR = Class(name="myDsl::direct::declaratorR")
myDsl_assignment_expression = Class(name="myDsl::assignment::expression")
myDsl_parameter_type_list = Class(name="myDsl::parameter::type::list")
myDsl_identifier_list = Class(name="myDsl::identifier::list")
myDsl_identifier_listR = Class(name="myDsl::identifier::listR")
myDsl_parameter_list = Class(name="myDsl::parameter::list")
parameter_type_list = Class(name="parameter::type::list")
myDsl_parameter_declaration = Class(name="myDsl::parameter::declaration")
myDsl_declarator = Class(name="myDsl::declarator")
myDsl_declaration_list = Class(name="myDsl::declaration::list")
myDsl_compound_statement = Class(name="myDsl::compound::statement")
init_declarator = Class(name="init::declarator")
struct_declarator = Class(name="struct::declarator")
myDsl_pointer = Class(name="myDsl::pointer")
myDsl_abstract_declarator = Class(name="myDsl::abstract::declarator")
myDsl_declaration = Class(name="myDsl::declaration")
myDsl_declaration_listR = Class(name="myDsl::declaration::listR")
statement = Class(name="statement")
myDsl_block_item_list = Class(name="myDsl::block::item::list")
compound_statement = Class(name="compound::statement")
myDsl_block_item = Class(name="myDsl::block::item")
myDsl_block_item_listR = Class(name="myDsl::block::item::listR")
myDsl_statement = Class(name="myDsl::statement")
block_item = Class(name="block::item")
myDsl_parameter_listR = Class(name="myDsl::parameter::listR")
myDsl_iteration_statement = Class(name="myDsl::iteration::statement")
myDsl_expression = Class(name="myDsl::expression")
myDsl_expression_statement = Class(name="myDsl::expression::statement")
myDsl_init_declarator_list = Class(name="myDsl::init::declarator::list")
myDsl_init_declarator = Class(name="myDsl::init::declarator")
myDsl_init_declarator_listR = Class(name="myDsl::init::declarator::listR")
myDsl_initializer = Class(name="myDsl::initializer")
parameter_declaration = Class(name="parameter::declaration")
myDsl_jump_statement = Class(name="myDsl::jump::statement")
myDsl_labeled_statement = Class(name="myDsl::labeled::statement")
myDsl_constant_expression = Class(name="myDsl::constant::expression")
jump_statement = Class(name="jump::statement")
expression_statement = Class(name="expression::statement")
primary_expression = Class(name="primary::expression")
myDsl_expressionR = Class(name="myDsl::expressionR")
myDsl_conditional_expression = Class(name="myDsl::conditional::expression")
assignment_expression = Class(name="assignment::expression")
constant_expression = Class(name="constant::expression")
myDsl_logical_or_expression = Class(name="myDsl::logical::or::expression")
conditional_expression = Class(name="conditional::expression")
myDsl_logical_and_expression = Class(name="myDsl::logical::and::expression")
myDsl_logical_or_expressionR = Class(name="myDsl::logical::or::expressionR")
myDsl_selection_statement = Class(name="myDsl::selection::statement")
myDsl_exclusive_or_expression = Class(name="myDsl::exclusive::or::expression")
myDsl_inclusive_or_expressionR = Class(name="myDsl::inclusive::or::expressionR")
myDsl_and_expression = Class(name="myDsl::and::expression")
myDsl_exclusive_or_expressionR = Class(name="myDsl::exclusive::or::expressionR")
myDsl_and_expressionR = Class(name="myDsl::and::expressionR")
myDsl_equality_expression = Class(name="myDsl::equality::expression")
myDsl_inclusive_or_expression = Class(name="myDsl::inclusive::or::expression")
myDsl_logical_and_expressionR = Class(name="myDsl::logical::and::expressionR")
myDsl_shift_expression = Class(name="myDsl::shift::expression")
myDsl_relational_expressionR = Class(name="myDsl::relational::expressionR")
myDsl_shift_expressionR = Class(name="myDsl::shift::expressionR")
myDsl_additive_expression = Class(name="myDsl::additive::expression")
shift_expression = Class(name="shift::expression")
myDsl_multiplicative_expression = Class(name="myDsl::multiplicative::expression")
myDsl_additive_expressionR = Class(name="myDsl::additive::expressionR")
myDsl_relational_expression = Class(name="myDsl::relational::expression")
myDsl_equality_expressionR = Class(name="myDsl::equality::expressionR")
initializer = Class(name="initializer")
myDsl_unary_expression = Class(name="myDsl::unary::expression")
myDsl_type_name = Class(name="myDsl::type::name")
cast_expression = Class(name="cast::expression")
myDsl_postfix_expression = Class(name="myDsl::postfix::expression")
unary_expression = Class(name="unary::expression")
myDsl_primary_expression = Class(name="myDsl::primary::expression")
myDsl_postfix_expressionR = Class(name="myDsl::postfix::expressionR")
myDsl_initializer_list = Class(name="myDsl::initializer::list")
myDsl_designation = Class(name="myDsl::designation")
myDsl_multiplicative_expressionR = Class(name="myDsl::multiplicative::expressionR")
myDsl_cast_expression = Class(name="myDsl::cast::expression")
myDsl_designator_list = Class(name="myDsl::designator::list")
designation = Class(name="designation")
myDsl_designator = Class(name="myDsl::designator")
myDsl_designator_listR = Class(name="myDsl::designator::listR")
designator = Class(name="designator")
static_assert_declaration = Class(name="static::assert::declaration")
atomic_type_specifier = Class(name="atomic::type::specifier")
myDsl_specifier_qualifier_list = Class(name="myDsl::specifier::qualifier::list")
type_name = Class(name="type::name")
struct_declaration = Class(name="struct::declaration")
myDsl_type_specifier = Class(name="myDsl::type::specifier")
myDsl_initializer_listR = Class(name="myDsl::initializer::listR")
myDsl_struct_declaration_list = Class(name="myDsl::struct::declaration::list")
myDsl_struct_declaration = Class(name="myDsl::struct::declaration")
myDsl_struct_declaration_listR = Class(name="myDsl::struct::declaration::listR")
myDsl_static_assert_declaration = Class(name="myDsl::static::assert::declaration")
declaration = Class(name="declaration")
myDsl_struct_or_union_specifier = Class(name="myDsl::struct::or::union::specifier")
type_specifier = Class(name="type::specifier")
myDsl_struct_declarator_list = Class(name="myDsl::struct::declarator::list")
myDsl_struct_declarator = Class(name="myDsl::struct::declarator")
myDsl_struct_declarator_listR = Class(name="myDsl::struct::declarator::listR")
myDsl_argument_expression_list = Class(name="myDsl::argument::expression::list")
myDsl_argument_expression_listR = Class(name="myDsl::argument::expression::listR")
abstract_declarator = Class(name="abstract::declarator")
direct_declarator = Class(name="direct::declarator")
identifier_list = Class(name="identifier::list")
identifier_listR = Class(name="identifier::listR")
labeled_statement = Class(name="labeled::statement")
struct_or_union_specifier = Class(name="struct::or::union::specifier")
postfix_expressionR = Class(name="postfix::expressionR")
myDsl_IDENTIFIER = Class(name="myDsl::IDENTIFIER")
myDsl_atomic_type_specifier = Class(name="myDsl::atomic::type::specifier")
myDsl_EObject = Class(name="myDsl::EObject")
declaration_specifiers = Class(name="declaration::specifiers")
myDsl_StringC = Class(name="myDsl::StringC")

# myDsl_Model class attributes and methods

# myDsl_translation_unit class attributes and methods

# myDsl_external_declaration class attributes and methods

# myDsl_translation_unitR class attributes and methods

# myDsl_declaration_specifiers class attributes and methods
myDsl_declaration_specifiers_Storage_class_specifier: Property = Property(name="Storage_class_specifier", type=StringType)
myDsl_declaration_specifiers_Type_qualifier: Property = Property(name="Type_qualifier", type=StringType)
myDsl_declaration_specifiers.attributes={myDsl_declaration_specifiers_Type_qualifier, myDsl_declaration_specifiers_Storage_class_specifier}

# myDsl_function_definition class attributes and methods

# external_declaration class attributes and methods

# myDsl_direct_declarator class attributes and methods

# myDsl_type_qualifier_list class attributes and methods
myDsl_type_qualifier_list_Type_qualifier: Property = Property(name="Type_qualifier", type=StringType)
myDsl_type_qualifier_list.attributes={myDsl_type_qualifier_list_Type_qualifier}

# pointer class attributes and methods

# myDsl_type_qualifier_listR class attributes and methods
myDsl_type_qualifier_listR_Type_qualifier: Property = Property(name="Type_qualifier", type=StringType)
myDsl_type_qualifier_listR.attributes={myDsl_type_qualifier_listR_Type_qualifier}

# declarator class attributes and methods

# myDsl_direct_declaratorR class attributes and methods

# myDsl_assignment_expression class attributes and methods
myDsl_assignment_expression_Assignment_operator: Property = Property(name="Assignment_operator", type=StringType)
myDsl_assignment_expression.attributes={myDsl_assignment_expression_Assignment_operator}

# myDsl_parameter_type_list class attributes and methods

# myDsl_identifier_list class attributes and methods

# myDsl_identifier_listR class attributes and methods

# myDsl_parameter_list class attributes and methods

# parameter_type_list class attributes and methods

# myDsl_parameter_declaration class attributes and methods

# myDsl_declarator class attributes and methods

# myDsl_declaration_list class attributes and methods

# myDsl_compound_statement class attributes and methods

# init_declarator class attributes and methods

# struct_declarator class attributes and methods

# myDsl_pointer class attributes and methods

# myDsl_abstract_declarator class attributes and methods

# myDsl_declaration class attributes and methods

# myDsl_declaration_listR class attributes and methods

# statement class attributes and methods

# myDsl_block_item_list class attributes and methods

# compound_statement class attributes and methods

# myDsl_block_item class attributes and methods

# myDsl_block_item_listR class attributes and methods

# myDsl_statement class attributes and methods

# block_item class attributes and methods

# myDsl_parameter_listR class attributes and methods

# myDsl_iteration_statement class attributes and methods

# myDsl_expression class attributes and methods

# myDsl_expression_statement class attributes and methods

# myDsl_init_declarator_list class attributes and methods

# myDsl_init_declarator class attributes and methods

# myDsl_init_declarator_listR class attributes and methods

# myDsl_initializer class attributes and methods

# parameter_declaration class attributes and methods

# myDsl_jump_statement class attributes and methods

# myDsl_labeled_statement class attributes and methods

# myDsl_constant_expression class attributes and methods

# jump_statement class attributes and methods

# expression_statement class attributes and methods

# primary_expression class attributes and methods

# myDsl_expressionR class attributes and methods

# myDsl_conditional_expression class attributes and methods

# assignment_expression class attributes and methods

# constant_expression class attributes and methods

# myDsl_logical_or_expression class attributes and methods

# conditional_expression class attributes and methods

# myDsl_logical_and_expression class attributes and methods

# myDsl_logical_or_expressionR class attributes and methods

# myDsl_selection_statement class attributes and methods

# myDsl_exclusive_or_expression class attributes and methods

# myDsl_inclusive_or_expressionR class attributes and methods

# myDsl_and_expression class attributes and methods

# myDsl_exclusive_or_expressionR class attributes and methods

# myDsl_and_expressionR class attributes and methods

# myDsl_equality_expression class attributes and methods

# myDsl_inclusive_or_expression class attributes and methods

# myDsl_logical_and_expressionR class attributes and methods

# myDsl_shift_expression class attributes and methods

# myDsl_relational_expressionR class attributes and methods

# myDsl_shift_expressionR class attributes and methods

# myDsl_additive_expression class attributes and methods

# shift_expression class attributes and methods

# myDsl_multiplicative_expression class attributes and methods

# myDsl_additive_expressionR class attributes and methods

# myDsl_relational_expression class attributes and methods

# myDsl_equality_expressionR class attributes and methods

# initializer class attributes and methods

# myDsl_unary_expression class attributes and methods
myDsl_unary_expression_Unary_operator: Property = Property(name="Unary_operator", type=StringType)
myDsl_unary_expression.attributes={myDsl_unary_expression_Unary_operator}

# myDsl_type_name class attributes and methods

# cast_expression class attributes and methods

# myDsl_postfix_expression class attributes and methods

# unary_expression class attributes and methods

# myDsl_primary_expression class attributes and methods

# myDsl_postfix_expressionR class attributes and methods

# myDsl_initializer_list class attributes and methods

# myDsl_designation class attributes and methods

# myDsl_multiplicative_expressionR class attributes and methods

# myDsl_cast_expression class attributes and methods

# myDsl_designator_list class attributes and methods

# designation class attributes and methods

# myDsl_designator class attributes and methods

# myDsl_designator_listR class attributes and methods

# designator class attributes and methods

# static_assert_declaration class attributes and methods

# atomic_type_specifier class attributes and methods

# myDsl_specifier_qualifier_list class attributes and methods

# type_name class attributes and methods

# struct_declaration class attributes and methods

# myDsl_type_specifier class attributes and methods

# myDsl_initializer_listR class attributes and methods

# myDsl_struct_declaration_list class attributes and methods

# myDsl_struct_declaration class attributes and methods

# myDsl_struct_declaration_listR class attributes and methods

# myDsl_static_assert_declaration class attributes and methods

# declaration class attributes and methods

# myDsl_struct_or_union_specifier class attributes and methods
myDsl_struct_or_union_specifier_Struct_or_union: Property = Property(name="Struct_or_union", type=StringType)
myDsl_struct_or_union_specifier.attributes={myDsl_struct_or_union_specifier_Struct_or_union}

# type_specifier class attributes and methods

# myDsl_struct_declarator_list class attributes and methods

# myDsl_struct_declarator class attributes and methods

# myDsl_struct_declarator_listR class attributes and methods

# myDsl_argument_expression_list class attributes and methods

# myDsl_argument_expression_listR class attributes and methods

# abstract_declarator class attributes and methods

# direct_declarator class attributes and methods

# identifier_list class attributes and methods

# identifier_listR class attributes and methods

# labeled_statement class attributes and methods

# struct_or_union_specifier class attributes and methods

# postfix_expressionR class attributes and methods

# myDsl_IDENTIFIER class attributes and methods
myDsl_IDENTIFIER_name: Property = Property(name="name", type=StringType)
myDsl_IDENTIFIER.attributes={myDsl_IDENTIFIER_name}

# myDsl_atomic_type_specifier class attributes and methods

# myDsl_EObject class attributes and methods

# declaration_specifiers class attributes and methods

# myDsl_StringC class attributes and methods
myDsl_StringC_string: Property = Property(name="string", type=StringType)
myDsl_StringC.attributes={myDsl_StringC_string}

# Relationships
greetings0: BinaryAssociation = BinaryAssociation(
    name="greetings0",
    ends={
        Property(name="myDsl_translation_unit", type=myDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Model", type=myDsl_translation_unit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
External_declaration1: BinaryAssociation = BinaryAssociation(
    name="External_declaration1",
    ends={
        Property(name="myDsl_external_declaration", type=myDsl_translation_unit, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_translation_unit2", type=myDsl_external_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Translation_unitR3: BinaryAssociation = BinaryAssociation(
    name="Translation_unitR3",
    ends={
        Property(name="myDsl_translation_unitR", type=myDsl_translation_unit, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_translation_unit4", type=myDsl_translation_unitR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
External_declaration5: BinaryAssociation = BinaryAssociation(
    name="External_declaration5",
    ends={
        Property(name="myDsl_external_declaration7", type=myDsl_translation_unitR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_translation_unitR6", type=myDsl_external_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rec9: BinaryAssociation = BinaryAssociation(
    name="rec9",
    ends={
        Property(name="myDsl_translation_unitR10", type=myDsl_translation_unitR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_translation_unitR8", type=myDsl_translation_unitR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Declaration_specifiers11: BinaryAssociation = BinaryAssociation(
    name="Declaration_specifiers11",
    ends={
        Property(name="myDsl_declaration_specifiers", type=myDsl_external_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_external_declaration12", type=myDsl_declaration_specifiers, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dd20: BinaryAssociation = BinaryAssociation(
    name="dd20",
    ends={
        Property(name="myDsl_direct_declarator", type=myDsl_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declarator21", type=myDsl_direct_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Type_qualifier_listR22: BinaryAssociation = BinaryAssociation(
    name="Type_qualifier_listR22",
    ends={
        Property(name="myDsl_type_qualifier_listR", type=myDsl_type_qualifier_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_type_qualifier_list", type=myDsl_type_qualifier_listR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rec24: BinaryAssociation = BinaryAssociation(
    name="rec24",
    ends={
        Property(name="myDsl_type_qualifier_listR25", type=myDsl_type_qualifier_listR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_type_qualifier_listR23", type=myDsl_type_qualifier_listR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Direct_declaratorR26: BinaryAssociation = BinaryAssociation(
    name="Direct_declaratorR26",
    ends={
        Property(name="myDsl_direct_declaratorR", type=myDsl_direct_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_declarator27", type=myDsl_direct_declaratorR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rec29: BinaryAssociation = BinaryAssociation(
    name="rec29",
    ends={
        Property(name="myDsl_direct_declaratorR30", type=myDsl_direct_declaratorR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_declaratorR28", type=myDsl_direct_declaratorR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Type_qualifier_list31: BinaryAssociation = BinaryAssociation(
    name="Type_qualifier_list31",
    ends={
        Property(name="myDsl_type_qualifier_list33", type=myDsl_direct_declaratorR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_declaratorR32", type=myDsl_type_qualifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Assignment_expression34: BinaryAssociation = BinaryAssociation(
    name="Assignment_expression34",
    ends={
        Property(name="myDsl_assignment_expression", type=myDsl_direct_declaratorR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_declaratorR35", type=myDsl_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Parameter_type_list36: BinaryAssociation = BinaryAssociation(
    name="Parameter_type_list36",
    ends={
        Property(name="myDsl_parameter_type_list", type=myDsl_direct_declaratorR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_declaratorR37", type=myDsl_parameter_type_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Identifier_list38: BinaryAssociation = BinaryAssociation(
    name="Identifier_list38",
    ends={
        Property(name="myDsl_identifier_list", type=myDsl_direct_declaratorR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_declaratorR39", type=myDsl_identifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Parameter_declaration40: BinaryAssociation = BinaryAssociation(
    name="Parameter_declaration40",
    ends={
        Property(name="myDsl_parameter_declaration", type=myDsl_parameter_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_parameter_list", type=myDsl_parameter_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Declarator13: BinaryAssociation = BinaryAssociation(
    name="Declarator13",
    ends={
        Property(name="myDsl_declarator", type=myDsl_function_definition, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_function_definition", type=myDsl_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Declaration_list14: BinaryAssociation = BinaryAssociation(
    name="Declaration_list14",
    ends={
        Property(name="myDsl_declaration_list", type=myDsl_function_definition, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_function_definition15", type=myDsl_declaration_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Compound_statement16: BinaryAssociation = BinaryAssociation(
    name="Compound_statement16",
    ends={
        Property(name="myDsl_compound_statement", type=myDsl_function_definition, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_function_definition17", type=myDsl_compound_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Pointer18: BinaryAssociation = BinaryAssociation(
    name="Pointer18",
    ends={
        Property(name="myDsl_pointer", type=myDsl_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declarator19", type=myDsl_pointer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Declarator152: BinaryAssociation = BinaryAssociation(
    name="Declarator152",
    ends={
        Property(name="myDsl_declarator54", type=myDsl_parameter_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_parameter_declaration53", type=myDsl_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Declaration_specifiers155: BinaryAssociation = BinaryAssociation(
    name="Declaration_specifiers155",
    ends={
        Property(name="myDsl_declaration_specifiers57", type=myDsl_parameter_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_parameter_declaration56", type=myDsl_declaration_specifiers, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Abstract_declarator58: BinaryAssociation = BinaryAssociation(
    name="Abstract_declarator58",
    ends={
        Property(name="myDsl_abstract_declarator", type=myDsl_parameter_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_parameter_declaration59", type=myDsl_abstract_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Declaration60: BinaryAssociation = BinaryAssociation(
    name="Declaration60",
    ends={
        Property(name="myDsl_declaration", type=myDsl_declaration_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declaration_list61", type=myDsl_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Declaration_listR62: BinaryAssociation = BinaryAssociation(
    name="Declaration_listR62",
    ends={
        Property(name="myDsl_declaration_listR", type=myDsl_declaration_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declaration_list63", type=myDsl_declaration_listR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Declaration64: BinaryAssociation = BinaryAssociation(
    name="Declaration64",
    ends={
        Property(name="myDsl_declaration66", type=myDsl_declaration_listR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declaration_listR65", type=myDsl_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rec68: BinaryAssociation = BinaryAssociation(
    name="rec68",
    ends={
        Property(name="myDsl_declaration_listR69", type=myDsl_declaration_listR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declaration_listR67", type=myDsl_declaration_listR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Block_item70: BinaryAssociation = BinaryAssociation(
    name="Block_item70",
    ends={
        Property(name="myDsl_block_item", type=myDsl_block_item_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_block_item_list", type=myDsl_block_item, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Block_item_listR71: BinaryAssociation = BinaryAssociation(
    name="Block_item_listR71",
    ends={
        Property(name="myDsl_block_item_listR", type=myDsl_block_item_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_block_item_list72", type=myDsl_block_item_listR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Block_item73: BinaryAssociation = BinaryAssociation(
    name="Block_item73",
    ends={
        Property(name="myDsl_block_item75", type=myDsl_block_item_listR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_block_item_listR74", type=myDsl_block_item, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rec77: BinaryAssociation = BinaryAssociation(
    name="rec77",
    ends={
        Property(name="myDsl_block_item_listR78", type=myDsl_block_item_listR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_block_item_listR76", type=myDsl_block_item_listR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Parameter_listR41: BinaryAssociation = BinaryAssociation(
    name="Parameter_listR41",
    ends={
        Property(name="myDsl_parameter_listR", type=myDsl_parameter_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_parameter_list42", type=myDsl_parameter_listR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Parameter_declaration43: BinaryAssociation = BinaryAssociation(
    name="Parameter_declaration43",
    ends={
        Property(name="myDsl_parameter_declaration45", type=myDsl_parameter_listR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_parameter_listR44", type=myDsl_parameter_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rec47: BinaryAssociation = BinaryAssociation(
    name="rec47",
    ends={
        Property(name="myDsl_parameter_listR48", type=myDsl_parameter_listR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_parameter_listR46", type=myDsl_parameter_listR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Declaration_specifiers249: BinaryAssociation = BinaryAssociation(
    name="Declaration_specifiers249",
    ends={
        Property(name="myDsl_declaration_specifiers51", type=myDsl_parameter_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_parameter_declaration50", type=myDsl_declaration_specifiers, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Expression85: BinaryAssociation = BinaryAssociation(
    name="Expression85",
    ends={
        Property(name="myDsl_expression", type=myDsl_iteration_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_iteration_statement", type=myDsl_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Statement86: BinaryAssociation = BinaryAssociation(
    name="Statement86",
    ends={
        Property(name="myDsl_statement88", type=myDsl_iteration_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_iteration_statement87", type=myDsl_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Expression_statement89: BinaryAssociation = BinaryAssociation(
    name="Expression_statement89",
    ends={
        Property(name="myDsl_expression_statement", type=myDsl_iteration_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_iteration_statement90", type=myDsl_expression_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Declaration91: BinaryAssociation = BinaryAssociation(
    name="Declaration91",
    ends={
        Property(name="myDsl_declaration93", type=myDsl_iteration_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_iteration_statement92", type=myDsl_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Init_declarator_list94: BinaryAssociation = BinaryAssociation(
    name="Init_declarator_list94",
    ends={
        Property(name="myDsl_init_declarator_list", type=myDsl_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declaration95", type=myDsl_init_declarator_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Init_declarator96: BinaryAssociation = BinaryAssociation(
    name="Init_declarator96",
    ends={
        Property(name="myDsl_init_declarator", type=myDsl_init_declarator_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_init_declarator_list97", type=myDsl_init_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Init_declarator_listR98: BinaryAssociation = BinaryAssociation(
    name="Init_declarator_listR98",
    ends={
        Property(name="myDsl_init_declarator_listR", type=myDsl_init_declarator_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_init_declarator_list99", type=myDsl_init_declarator_listR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Declarator100: BinaryAssociation = BinaryAssociation(
    name="Declarator100",
    ends={
        Property(name="myDsl_declarator102", type=myDsl_init_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_init_declarator101", type=myDsl_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Initializer103: BinaryAssociation = BinaryAssociation(
    name="Initializer103",
    ends={
        Property(name="myDsl_initializer", type=myDsl_init_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_init_declarator104", type=myDsl_initializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Init_declarator105: BinaryAssociation = BinaryAssociation(
    name="Init_declarator105",
    ends={
        Property(name="myDsl_init_declarator107", type=myDsl_init_declarator_listR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_init_declarator_listR106", type=myDsl_init_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rec109: BinaryAssociation = BinaryAssociation(
    name="rec109",
    ends={
        Property(name="myDsl_init_declarator_listR110", type=myDsl_init_declarator_listR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_init_declarator_listR108", type=myDsl_init_declarator_listR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Constant_expression79: BinaryAssociation = BinaryAssociation(
    name="Constant_expression79",
    ends={
        Property(name="myDsl_constant_expression", type=myDsl_labeled_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_labeled_statement", type=myDsl_constant_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Statement80: BinaryAssociation = BinaryAssociation(
    name="Statement80",
    ends={
        Property(name="myDsl_statement", type=myDsl_labeled_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_labeled_statement81", type=myDsl_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
b82: BinaryAssociation = BinaryAssociation(
    name="b82",
    ends={
        Property(name="myDsl_statement84", type=myDsl_labeled_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_labeled_statement83", type=myDsl_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Expression117: BinaryAssociation = BinaryAssociation(
    name="Expression117",
    ends={
        Property(name="myDsl_expression118", type=myDsl_selection_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_selection_statement", type=myDsl_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Statement119: BinaryAssociation = BinaryAssociation(
    name="Statement119",
    ends={
        Property(name="myDsl_statement121", type=myDsl_selection_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_selection_statement120", type=myDsl_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Assignment_expression122: BinaryAssociation = BinaryAssociation(
    name="Assignment_expression122",
    ends={
        Property(name="myDsl_assignment_expression124", type=myDsl_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_expression123", type=myDsl_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ExpressionR125: BinaryAssociation = BinaryAssociation(
    name="ExpressionR125",
    ends={
        Property(name="myDsl_expressionR", type=myDsl_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_expression126", type=myDsl_expressionR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Assignment_expression127: BinaryAssociation = BinaryAssociation(
    name="Assignment_expression127",
    ends={
        Property(name="myDsl_assignment_expression129", type=myDsl_expressionR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_expressionR128", type=myDsl_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rec131: BinaryAssociation = BinaryAssociation(
    name="rec131",
    ends={
        Property(name="myDsl_expressionR132", type=myDsl_expressionR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_expressionR130", type=myDsl_expressionR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Logical_or_expression133: BinaryAssociation = BinaryAssociation(
    name="Logical_or_expression133",
    ends={
        Property(name="myDsl_logical_or_expression", type=myDsl_conditional_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_conditional_expression", type=myDsl_logical_or_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Expression134: BinaryAssociation = BinaryAssociation(
    name="Expression134",
    ends={
        Property(name="myDsl_expression136", type=myDsl_conditional_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_conditional_expression135", type=myDsl_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Logical_and_expression137: BinaryAssociation = BinaryAssociation(
    name="Logical_and_expression137",
    ends={
        Property(name="myDsl_logical_and_expression", type=myDsl_logical_or_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_logical_or_expression138", type=myDsl_logical_and_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Logical_or_expressionR139: BinaryAssociation = BinaryAssociation(
    name="Logical_or_expressionR139",
    ends={
        Property(name="myDsl_logical_or_expressionR", type=myDsl_logical_or_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_logical_or_expression140", type=myDsl_logical_or_expressionR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
r1112: BinaryAssociation = BinaryAssociation(
    name="r1112",
    ends={
        Property(name="myDsl_declaration_specifiers113", type=myDsl_declaration_specifiers, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declaration_specifiers111", type=myDsl_declaration_specifiers, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
r2115: BinaryAssociation = BinaryAssociation(
    name="r2115",
    ends={
        Property(name="myDsl_declaration_specifiers116", type=myDsl_declaration_specifiers, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declaration_specifiers114", type=myDsl_declaration_specifiers, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Inclusive_or_expression151: BinaryAssociation = BinaryAssociation(
    name="Inclusive_or_expression151",
    ends={
        Property(name="myDsl_inclusive_or_expression153", type=myDsl_logical_and_expressionR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_logical_and_expressionR152", type=myDsl_inclusive_or_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rec155: BinaryAssociation = BinaryAssociation(
    name="rec155",
    ends={
        Property(name="myDsl_logical_and_expressionR156", type=myDsl_logical_and_expressionR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_logical_and_expressionR154", type=myDsl_logical_and_expressionR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Exclusive_or_expression157: BinaryAssociation = BinaryAssociation(
    name="Exclusive_or_expression157",
    ends={
        Property(name="myDsl_exclusive_or_expression", type=myDsl_inclusive_or_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_inclusive_or_expression158", type=myDsl_exclusive_or_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Inclusive_or_expressionR159: BinaryAssociation = BinaryAssociation(
    name="Inclusive_or_expressionR159",
    ends={
        Property(name="myDsl_inclusive_or_expressionR", type=myDsl_inclusive_or_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_inclusive_or_expression160", type=myDsl_inclusive_or_expressionR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Exclusive_or_expression161: BinaryAssociation = BinaryAssociation(
    name="Exclusive_or_expression161",
    ends={
        Property(name="myDsl_exclusive_or_expression163", type=myDsl_inclusive_or_expressionR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_inclusive_or_expressionR162", type=myDsl_exclusive_or_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rec165: BinaryAssociation = BinaryAssociation(
    name="rec165",
    ends={
        Property(name="myDsl_inclusive_or_expressionR166", type=myDsl_inclusive_or_expressionR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_inclusive_or_expressionR164", type=myDsl_inclusive_or_expressionR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
And_expression167: BinaryAssociation = BinaryAssociation(
    name="And_expression167",
    ends={
        Property(name="myDsl_and_expression", type=myDsl_exclusive_or_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_exclusive_or_expression168", type=myDsl_and_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Exclusive_or_expressionR169: BinaryAssociation = BinaryAssociation(
    name="Exclusive_or_expressionR169",
    ends={
        Property(name="myDsl_exclusive_or_expressionR", type=myDsl_exclusive_or_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_exclusive_or_expression170", type=myDsl_exclusive_or_expressionR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
And_expression171: BinaryAssociation = BinaryAssociation(
    name="And_expression171",
    ends={
        Property(name="myDsl_and_expression173", type=myDsl_exclusive_or_expressionR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_exclusive_or_expressionR172", type=myDsl_and_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rec175: BinaryAssociation = BinaryAssociation(
    name="rec175",
    ends={
        Property(name="myDsl_exclusive_or_expressionR176", type=myDsl_exclusive_or_expressionR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_exclusive_or_expressionR174", type=myDsl_exclusive_or_expressionR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Equality_expression177: BinaryAssociation = BinaryAssociation(
    name="Equality_expression177",
    ends={
        Property(name="myDsl_equality_expression", type=myDsl_and_expressionR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_and_expressionR", type=myDsl_equality_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rec179: BinaryAssociation = BinaryAssociation(
    name="rec179",
    ends={
        Property(name="myDsl_and_expressionR180", type=myDsl_and_expressionR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_and_expressionR178", type=myDsl_and_expressionR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Equality_expression181: BinaryAssociation = BinaryAssociation(
    name="Equality_expression181",
    ends={
        Property(name="myDsl_equality_expression183", type=myDsl_and_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_and_expression182", type=myDsl_equality_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Logical_and_expression141: BinaryAssociation = BinaryAssociation(
    name="Logical_and_expression141",
    ends={
        Property(name="myDsl_logical_and_expression143", type=myDsl_logical_or_expressionR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_logical_or_expressionR142", type=myDsl_logical_and_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rec145: BinaryAssociation = BinaryAssociation(
    name="rec145",
    ends={
        Property(name="myDsl_logical_or_expressionR146", type=myDsl_logical_or_expressionR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_logical_or_expressionR144", type=myDsl_logical_or_expressionR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Inclusive_or_expression147: BinaryAssociation = BinaryAssociation(
    name="Inclusive_or_expression147",
    ends={
        Property(name="myDsl_inclusive_or_expression", type=myDsl_logical_and_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_logical_and_expression148", type=myDsl_inclusive_or_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Logical_and_expressionR149: BinaryAssociation = BinaryAssociation(
    name="Logical_and_expressionR149",
    ends={
        Property(name="myDsl_logical_and_expressionR", type=myDsl_logical_and_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_logical_and_expression150", type=myDsl_logical_and_expressionR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Relational_expression191: BinaryAssociation = BinaryAssociation(
    name="Relational_expression191",
    ends={
        Property(name="myDsl_relational_expression193", type=myDsl_equality_expressionR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_equality_expressionR192", type=myDsl_relational_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rec195: BinaryAssociation = BinaryAssociation(
    name="rec195",
    ends={
        Property(name="myDsl_equality_expressionR196", type=myDsl_equality_expressionR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_equality_expressionR194", type=myDsl_equality_expressionR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Shift_expression197: BinaryAssociation = BinaryAssociation(
    name="Shift_expression197",
    ends={
        Property(name="myDsl_shift_expression", type=myDsl_relational_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_relational_expression198", type=myDsl_shift_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
re199: BinaryAssociation = BinaryAssociation(
    name="re199",
    ends={
        Property(name="myDsl_relational_expressionR", type=myDsl_relational_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_relational_expression200", type=myDsl_relational_expressionR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Shift_expression201: BinaryAssociation = BinaryAssociation(
    name="Shift_expression201",
    ends={
        Property(name="myDsl_shift_expression203", type=myDsl_relational_expressionR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_relational_expressionR202", type=myDsl_shift_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rec205: BinaryAssociation = BinaryAssociation(
    name="rec205",
    ends={
        Property(name="myDsl_relational_expressionR206", type=myDsl_relational_expressionR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_relational_expressionR204", type=myDsl_relational_expressionR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Additive_expression207: BinaryAssociation = BinaryAssociation(
    name="Additive_expression207",
    ends={
        Property(name="myDsl_additive_expression", type=myDsl_shift_expressionR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_shift_expressionR", type=myDsl_additive_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rec209: BinaryAssociation = BinaryAssociation(
    name="rec209",
    ends={
        Property(name="myDsl_shift_expressionR210", type=myDsl_shift_expressionR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_shift_expressionR208", type=myDsl_shift_expressionR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Shift_expressionR211: BinaryAssociation = BinaryAssociation(
    name="Shift_expressionR211",
    ends={
        Property(name="myDsl_shift_expressionR213", type=myDsl_additive_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_additive_expression212", type=myDsl_shift_expressionR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Multiplicative_expression214: BinaryAssociation = BinaryAssociation(
    name="Multiplicative_expression214",
    ends={
        Property(name="myDsl_multiplicative_expression", type=myDsl_additive_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_additive_expression215", type=myDsl_multiplicative_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Additive_expressionR216: BinaryAssociation = BinaryAssociation(
    name="Additive_expressionR216",
    ends={
        Property(name="myDsl_additive_expressionR", type=myDsl_additive_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_additive_expression217", type=myDsl_additive_expressionR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Multiplicative_expression218: BinaryAssociation = BinaryAssociation(
    name="Multiplicative_expression218",
    ends={
        Property(name="myDsl_multiplicative_expression220", type=myDsl_additive_expressionR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_additive_expressionR219", type=myDsl_multiplicative_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
And_expressionR184: BinaryAssociation = BinaryAssociation(
    name="And_expressionR184",
    ends={
        Property(name="myDsl_and_expressionR186", type=myDsl_and_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_and_expression185", type=myDsl_and_expressionR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Relational_expression187: BinaryAssociation = BinaryAssociation(
    name="Relational_expression187",
    ends={
        Property(name="myDsl_relational_expression", type=myDsl_equality_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_equality_expression188", type=myDsl_relational_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Equality_expressionR189: BinaryAssociation = BinaryAssociation(
    name="Equality_expressionR189",
    ends={
        Property(name="myDsl_equality_expressionR", type=myDsl_equality_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_equality_expression190", type=myDsl_equality_expressionR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Multiplicative_expressionR231: BinaryAssociation = BinaryAssociation(
    name="Multiplicative_expressionR231",
    ends={
        Property(name="myDsl_multiplicative_expressionR233", type=myDsl_multiplicative_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_multiplicative_expression232", type=myDsl_multiplicative_expressionR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Unary_expression234: BinaryAssociation = BinaryAssociation(
    name="Unary_expression234",
    ends={
        Property(name="myDsl_unary_expression", type=myDsl_assignment_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_assignment_expression235", type=myDsl_unary_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rec237: BinaryAssociation = BinaryAssociation(
    name="rec237",
    ends={
        Property(name="myDsl_assignment_expression238", type=myDsl_assignment_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_assignment_expression236", type=myDsl_assignment_expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Type_name239: BinaryAssociation = BinaryAssociation(
    name="Type_name239",
    ends={
        Property(name="myDsl_type_name", type=myDsl_cast_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_cast_expression240", type=myDsl_type_name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rec242: BinaryAssociation = BinaryAssociation(
    name="rec242",
    ends={
        Property(name="myDsl_cast_expression243", type=myDsl_cast_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_cast_expression241", type=myDsl_cast_expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ce244: BinaryAssociation = BinaryAssociation(
    name="ce244",
    ends={
        Property(name="myDsl_cast_expression246", type=myDsl_unary_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_unary_expression245", type=myDsl_cast_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Primary_expression247: BinaryAssociation = BinaryAssociation(
    name="Primary_expression247",
    ends={
        Property(name="myDsl_primary_expression", type=myDsl_postfix_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_postfix_expression", type=myDsl_primary_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Postfix_expressionR248: BinaryAssociation = BinaryAssociation(
    name="Postfix_expressionR248",
    ends={
        Property(name="myDsl_postfix_expressionR", type=myDsl_postfix_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_postfix_expression249", type=myDsl_postfix_expressionR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Initializer_list250: BinaryAssociation = BinaryAssociation(
    name="Initializer_list250",
    ends={
        Property(name="myDsl_initializer_list", type=myDsl_postfix_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_postfix_expression251", type=myDsl_initializer_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Designation252: BinaryAssociation = BinaryAssociation(
    name="Designation252",
    ends={
        Property(name="myDsl_designation", type=myDsl_initializer_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_initializer_list253", type=myDsl_designation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rec222: BinaryAssociation = BinaryAssociation(
    name="rec222",
    ends={
        Property(name="myDsl_additive_expressionR223", type=myDsl_additive_expressionR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_additive_expressionR221", type=myDsl_additive_expressionR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Cast_expression224: BinaryAssociation = BinaryAssociation(
    name="Cast_expression224",
    ends={
        Property(name="myDsl_cast_expression", type=myDsl_multiplicative_expressionR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_multiplicative_expressionR", type=myDsl_cast_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rec226: BinaryAssociation = BinaryAssociation(
    name="rec226",
    ends={
        Property(name="myDsl_multiplicative_expressionR227", type=myDsl_multiplicative_expressionR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_multiplicative_expressionR225", type=myDsl_multiplicative_expressionR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Cast_expression228: BinaryAssociation = BinaryAssociation(
    name="Cast_expression228",
    ends={
        Property(name="myDsl_cast_expression230", type=myDsl_multiplicative_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_multiplicative_expression229", type=myDsl_cast_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Initializer265: BinaryAssociation = BinaryAssociation(
    name="Initializer265",
    ends={
        Property(name="myDsl_initializer267", type=myDsl_initializer_listR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_initializer_listR266", type=myDsl_initializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rec269: BinaryAssociation = BinaryAssociation(
    name="rec269",
    ends={
        Property(name="myDsl_initializer_listR270", type=myDsl_initializer_listR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_initializer_listR268", type=myDsl_initializer_listR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Designator271: BinaryAssociation = BinaryAssociation(
    name="Designator271",
    ends={
        Property(name="myDsl_designator", type=myDsl_designator_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_designator_list", type=myDsl_designator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
DesignatorR272: BinaryAssociation = BinaryAssociation(
    name="DesignatorR272",
    ends={
        Property(name="myDsl_designator_listR", type=myDsl_designator_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_designator_list273", type=myDsl_designator_listR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Designator274: BinaryAssociation = BinaryAssociation(
    name="Designator274",
    ends={
        Property(name="myDsl_designator276", type=myDsl_designator_listR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_designator_listR275", type=myDsl_designator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rec278: BinaryAssociation = BinaryAssociation(
    name="rec278",
    ends={
        Property(name="myDsl_designator_listR279", type=myDsl_designator_listR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_designator_listR277", type=myDsl_designator_listR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Specifier_qualifier_list280: BinaryAssociation = BinaryAssociation(
    name="Specifier_qualifier_list280",
    ends={
        Property(name="myDsl_specifier_qualifier_list", type=myDsl_type_name, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_type_name281", type=myDsl_specifier_qualifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ad282: BinaryAssociation = BinaryAssociation(
    name="ad282",
    ends={
        Property(name="myDsl_abstract_declarator284", type=myDsl_type_name, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_type_name283", type=myDsl_abstract_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Type_specifier285: BinaryAssociation = BinaryAssociation(
    name="Type_specifier285",
    ends={
        Property(name="myDsl_type_specifier", type=myDsl_specifier_qualifier_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_specifier_qualifier_list286", type=myDsl_type_specifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Initializer254: BinaryAssociation = BinaryAssociation(
    name="Initializer254",
    ends={
        Property(name="myDsl_initializer256", type=myDsl_initializer_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_initializer_list255", type=myDsl_initializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
il257: BinaryAssociation = BinaryAssociation(
    name="il257",
    ends={
        Property(name="myDsl_initializer_listR", type=myDsl_initializer_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_initializer_list258", type=myDsl_initializer_listR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ilr259: BinaryAssociation = BinaryAssociation(
    name="ilr259",
    ends={
        Property(name="myDsl_initializer_listR261", type=myDsl_initializer_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_initializer_list260", type=myDsl_initializer_listR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Designation262: BinaryAssociation = BinaryAssociation(
    name="Designation262",
    ends={
        Property(name="myDsl_designation264", type=myDsl_initializer_listR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_initializer_listR263", type=myDsl_designation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Struct_declaration293: BinaryAssociation = BinaryAssociation(
    name="Struct_declaration293",
    ends={
        Property(name="myDsl_struct_declaration", type=myDsl_struct_declaration_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declaration_list", type=myDsl_struct_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Struct_declaration_listR294: BinaryAssociation = BinaryAssociation(
    name="Struct_declaration_listR294",
    ends={
        Property(name="myDsl_struct_declaration_listR", type=myDsl_struct_declaration_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declaration_list295", type=myDsl_struct_declaration_listR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Struct_declaration296: BinaryAssociation = BinaryAssociation(
    name="Struct_declaration296",
    ends={
        Property(name="myDsl_struct_declaration298", type=myDsl_struct_declaration_listR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declaration_listR297", type=myDsl_struct_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rec300: BinaryAssociation = BinaryAssociation(
    name="rec300",
    ends={
        Property(name="myDsl_struct_declaration_listR301", type=myDsl_struct_declaration_listR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declaration_listR299", type=myDsl_struct_declaration_listR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Specifier_qualifier_listx302: BinaryAssociation = BinaryAssociation(
    name="Specifier_qualifier_listx302",
    ends={
        Property(name="myDsl_specifier_qualifier_list304", type=myDsl_struct_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declaration303", type=myDsl_specifier_qualifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Struct_declarator_list305: BinaryAssociation = BinaryAssociation(
    name="Struct_declarator_list305",
    ends={
        Property(name="myDsl_struct_declarator_list307", type=myDsl_struct_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declaration306", type=myDsl_struct_declarator_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Struct_declarator308: BinaryAssociation = BinaryAssociation(
    name="Struct_declarator308",
    ends={
        Property(name="myDsl_struct_declarator310", type=myDsl_struct_declarator_listR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declarator_listR309", type=myDsl_struct_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rec312: BinaryAssociation = BinaryAssociation(
    name="rec312",
    ends={
        Property(name="myDsl_struct_declarator_listR313", type=myDsl_struct_declarator_listR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declarator_listR311", type=myDsl_struct_declarator_listR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Declaratorx314: BinaryAssociation = BinaryAssociation(
    name="Declaratorx314",
    ends={
        Property(name="myDsl_declarator316", type=myDsl_struct_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declarator315", type=myDsl_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Constant_expression1317: BinaryAssociation = BinaryAssociation(
    name="Constant_expression1317",
    ends={
        Property(name="myDsl_constant_expression319", type=myDsl_struct_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declarator318", type=myDsl_constant_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Struct_declaration_list320: BinaryAssociation = BinaryAssociation(
    name="Struct_declaration_list320",
    ends={
        Property(name="myDsl_struct_declaration_list321", type=myDsl_struct_or_union_specifier, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_or_union_specifier", type=myDsl_struct_declaration_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rec288: BinaryAssociation = BinaryAssociation(
    name="rec288",
    ends={
        Property(name="myDsl_specifier_qualifier_list289", type=myDsl_specifier_qualifier_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_specifier_qualifier_list287", type=myDsl_specifier_qualifier_list, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Struct_declarator290: BinaryAssociation = BinaryAssociation(
    name="Struct_declarator290",
    ends={
        Property(name="myDsl_struct_declarator", type=myDsl_struct_declarator_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declarator_list", type=myDsl_struct_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Struct_declarator_listR291: BinaryAssociation = BinaryAssociation(
    name="Struct_declarator_listR291",
    ends={
        Property(name="myDsl_struct_declarator_listR", type=myDsl_struct_declarator_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declarator_list292", type=myDsl_struct_declarator_listR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Argument_expression_list329: BinaryAssociation = BinaryAssociation(
    name="Argument_expression_list329",
    ends={
        Property(name="myDsl_argument_expression_list", type=myDsl_postfix_expressionR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_postfix_expressionR330", type=myDsl_argument_expression_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Assignment_expression331: BinaryAssociation = BinaryAssociation(
    name="Assignment_expression331",
    ends={
        Property(name="myDsl_assignment_expression333", type=myDsl_argument_expression_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_argument_expression_list332", type=myDsl_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Argument_expression_listR334: BinaryAssociation = BinaryAssociation(
    name="Argument_expression_listR334",
    ends={
        Property(name="myDsl_argument_expression_listR", type=myDsl_argument_expression_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_argument_expression_list335", type=myDsl_argument_expression_listR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Assignment_expression336: BinaryAssociation = BinaryAssociation(
    name="Assignment_expression336",
    ends={
        Property(name="myDsl_assignment_expression338", type=myDsl_argument_expression_listR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_argument_expression_listR337", type=myDsl_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rec340: BinaryAssociation = BinaryAssociation(
    name="rec340",
    ends={
        Property(name="myDsl_argument_expression_listR341", type=myDsl_argument_expression_listR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_argument_expression_listR339", type=myDsl_argument_expression_listR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Type_qualifier_list342: BinaryAssociation = BinaryAssociation(
    name="Type_qualifier_list342",
    ends={
        Property(name="myDsl_type_qualifier_list344", type=myDsl_pointer, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_pointer343", type=myDsl_type_qualifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rec346: BinaryAssociation = BinaryAssociation(
    name="rec346",
    ends={
        Property(name="myDsl_pointer347", type=myDsl_pointer, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_pointer345", type=myDsl_pointer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dr348: BinaryAssociation = BinaryAssociation(
    name="dr348",
    ends={
        Property(name="myDsl_direct_declaratorR350", type=myDsl_IDENTIFIER, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_IDENTIFIER349", type=myDsl_direct_declaratorR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
il351: BinaryAssociation = BinaryAssociation(
    name="il351",
    ends={
        Property(name="myDsl_identifier_listR", type=myDsl_IDENTIFIER, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_IDENTIFIER352", type=myDsl_identifier_listR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id322: BinaryAssociation = BinaryAssociation(
    name="id322",
    ends={
        Property(name="myDsl_IDENTIFIER", type=myDsl_struct_or_union_specifier, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_or_union_specifier323", type=myDsl_IDENTIFIER, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Expression324: BinaryAssociation = BinaryAssociation(
    name="Expression324",
    ends={
        Property(name="myDsl_expression326", type=myDsl_postfix_expressionR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_postfix_expressionR325", type=myDsl_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rec327: BinaryAssociation = BinaryAssociation(
    name="rec327",
    ends={
        Property(name="myDsl_EObject", type=myDsl_postfix_expressionR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_postfix_expressionR328", type=myDsl_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
a353: BinaryAssociation = BinaryAssociation(
    name="a353",
    ends={
        Property(name="myDsl_statement355", type=myDsl_IDENTIFIER, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_IDENTIFIER354", type=myDsl_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ds356: BinaryAssociation = BinaryAssociation(
    name="ds356",
    ends={
        Property(name="myDsl_declaration_specifiers358", type=myDsl_type_specifier, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_type_specifier357", type=myDsl_declaration_specifiers, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_myDsl_function_definition_external_declaration = Generalization(general=external_declaration, specific=myDsl_function_definition)
gen_myDsl_type_qualifier_list_pointer = Generalization(general=pointer, specific=myDsl_type_qualifier_list)
gen_myDsl_direct_declarator_declarator = Generalization(general=declarator, specific=myDsl_direct_declarator)
gen_myDsl_parameter_list_parameter_type_list = Generalization(general=parameter_type_list, specific=myDsl_parameter_list)
gen_myDsl_declarator_init_declarator = Generalization(general=init_declarator, specific=myDsl_declarator)
gen_myDsl_declarator_struct_declarator = Generalization(general=struct_declarator, specific=myDsl_declarator)
gen_myDsl_compound_statement_statement = Generalization(general=statement, specific=myDsl_compound_statement)
gen_myDsl_block_item_list_compound_statement = Generalization(general=compound_statement, specific=myDsl_block_item_list)
gen_myDsl_statement_block_item = Generalization(general=block_item, specific=myDsl_statement)
gen_myDsl_iteration_statement_statement = Generalization(general=statement, specific=myDsl_iteration_statement)
gen_myDsl_declaration_external_declaration = Generalization(general=external_declaration, specific=myDsl_declaration)
gen_myDsl_declaration_block_item = Generalization(general=block_item, specific=myDsl_declaration)
gen_myDsl_declaration_specifiers_parameter_declaration = Generalization(general=parameter_declaration, specific=myDsl_declaration_specifiers)
gen_myDsl_jump_statement_statement = Generalization(general=statement, specific=myDsl_jump_statement)
gen_myDsl_labeled_statement_statement = Generalization(general=statement, specific=myDsl_labeled_statement)
gen_myDsl_expression_statement_statement = Generalization(general=statement, specific=myDsl_expression_statement)
gen_myDsl_expression_jump_statement = Generalization(general=jump_statement, specific=myDsl_expression)
gen_myDsl_expression_expression_statement = Generalization(general=expression_statement, specific=myDsl_expression)
gen_myDsl_expression_primary_expression = Generalization(general=primary_expression, specific=myDsl_expression)
gen_myDsl_conditional_expression_assignment_expression = Generalization(general=assignment_expression, specific=myDsl_conditional_expression)
gen_myDsl_conditional_expression_constant_expression = Generalization(general=constant_expression, specific=myDsl_conditional_expression)
gen_myDsl_logical_or_expression_conditional_expression = Generalization(general=conditional_expression, specific=myDsl_logical_or_expression)
gen_myDsl_selection_statement_statement = Generalization(general=statement, specific=myDsl_selection_statement)
gen_myDsl_additive_expression_shift_expression = Generalization(general=shift_expression, specific=myDsl_additive_expression)
gen_myDsl_assignment_expression_initializer = Generalization(general=initializer, specific=myDsl_assignment_expression)
gen_myDsl_unary_expression_cast_expression = Generalization(general=cast_expression, specific=myDsl_unary_expression)
gen_myDsl_postfix_expression_unary_expression = Generalization(general=unary_expression, specific=myDsl_postfix_expression)
gen_myDsl_initializer_list_initializer = Generalization(general=initializer, specific=myDsl_initializer_list)
gen_myDsl_designator_list_designation = Generalization(general=designation, specific=myDsl_designator_list)
gen_myDsl_constant_expression_designator = Generalization(general=designator, specific=myDsl_constant_expression)
gen_myDsl_constant_expression_struct_declarator = Generalization(general=struct_declarator, specific=myDsl_constant_expression)
gen_myDsl_constant_expression_static_assert_declaration = Generalization(general=static_assert_declaration, specific=myDsl_constant_expression)
gen_myDsl_type_name_atomic_type_specifier = Generalization(general=atomic_type_specifier, specific=myDsl_type_name)
gen_myDsl_specifier_qualifier_list_type_name = Generalization(general=type_name, specific=myDsl_specifier_qualifier_list)
gen_myDsl_specifier_qualifier_list_struct_declaration = Generalization(general=struct_declaration, specific=myDsl_specifier_qualifier_list)
gen_myDsl_static_assert_declaration_declaration = Generalization(general=declaration, specific=myDsl_static_assert_declaration)
gen_myDsl_static_assert_declaration_struct_declaration = Generalization(general=struct_declaration, specific=myDsl_static_assert_declaration)
gen_myDsl_struct_or_union_specifier_type_specifier = Generalization(general=type_specifier, specific=myDsl_struct_or_union_specifier)
gen_myDsl_pointer_abstract_declarator = Generalization(general=abstract_declarator, specific=myDsl_pointer)
gen_myDsl_IDENTIFIER_direct_declarator = Generalization(general=direct_declarator, specific=myDsl_IDENTIFIER)
gen_myDsl_IDENTIFIER_identifier_list = Generalization(general=identifier_list, specific=myDsl_IDENTIFIER)
gen_myDsl_IDENTIFIER_identifier_listR = Generalization(general=identifier_listR, specific=myDsl_IDENTIFIER)
gen_myDsl_IDENTIFIER_jump_statement = Generalization(general=jump_statement, specific=myDsl_IDENTIFIER)
gen_myDsl_IDENTIFIER_labeled_statement = Generalization(general=labeled_statement, specific=myDsl_IDENTIFIER)
gen_myDsl_IDENTIFIER_designator = Generalization(general=designator, specific=myDsl_IDENTIFIER)
gen_myDsl_IDENTIFIER_struct_or_union_specifier = Generalization(general=struct_or_union_specifier, specific=myDsl_IDENTIFIER)
gen_myDsl_IDENTIFIER_postfix_expressionR = Generalization(general=postfix_expressionR, specific=myDsl_IDENTIFIER)
gen_myDsl_IDENTIFIER_primary_expression = Generalization(general=primary_expression, specific=myDsl_IDENTIFIER)
gen_myDsl_atomic_type_specifier_type_specifier = Generalization(general=type_specifier, specific=myDsl_atomic_type_specifier)
gen_myDsl_type_specifier_declaration_specifiers = Generalization(general=declaration_specifiers, specific=myDsl_type_specifier)
gen_myDsl_StringC_primary_expression = Generalization(general=primary_expression, specific=myDsl_StringC)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_Model, myDsl_translation_unit, myDsl_external_declaration, myDsl_translation_unitR, myDsl_declaration_specifiers, myDsl_function_definition, external_declaration, myDsl_direct_declarator, myDsl_type_qualifier_list, pointer, myDsl_type_qualifier_listR, declarator, myDsl_direct_declaratorR, myDsl_assignment_expression, myDsl_parameter_type_list, myDsl_identifier_list, myDsl_identifier_listR, myDsl_parameter_list, parameter_type_list, myDsl_parameter_declaration, myDsl_declarator, myDsl_declaration_list, myDsl_compound_statement, init_declarator, struct_declarator, myDsl_pointer, myDsl_abstract_declarator, myDsl_declaration, myDsl_declaration_listR, statement, myDsl_block_item_list, compound_statement, myDsl_block_item, myDsl_block_item_listR, myDsl_statement, block_item, myDsl_parameter_listR, myDsl_iteration_statement, myDsl_expression, myDsl_expression_statement, myDsl_init_declarator_list, myDsl_init_declarator, myDsl_init_declarator_listR, myDsl_initializer, parameter_declaration, myDsl_jump_statement, myDsl_labeled_statement, myDsl_constant_expression, jump_statement, expression_statement, primary_expression, myDsl_expressionR, myDsl_conditional_expression, assignment_expression, constant_expression, myDsl_logical_or_expression, conditional_expression, myDsl_logical_and_expression, myDsl_logical_or_expressionR, myDsl_selection_statement, myDsl_exclusive_or_expression, myDsl_inclusive_or_expressionR, myDsl_and_expression, myDsl_exclusive_or_expressionR, myDsl_and_expressionR, myDsl_equality_expression, myDsl_inclusive_or_expression, myDsl_logical_and_expressionR, myDsl_shift_expression, myDsl_relational_expressionR, myDsl_shift_expressionR, myDsl_additive_expression, shift_expression, myDsl_multiplicative_expression, myDsl_additive_expressionR, myDsl_relational_expression, myDsl_equality_expressionR, initializer, myDsl_unary_expression, myDsl_type_name, cast_expression, myDsl_postfix_expression, unary_expression, myDsl_primary_expression, myDsl_postfix_expressionR, myDsl_initializer_list, myDsl_designation, myDsl_multiplicative_expressionR, myDsl_cast_expression, myDsl_designator_list, designation, myDsl_designator, myDsl_designator_listR, designator, static_assert_declaration, atomic_type_specifier, myDsl_specifier_qualifier_list, type_name, struct_declaration, myDsl_type_specifier, myDsl_initializer_listR, myDsl_struct_declaration_list, myDsl_struct_declaration, myDsl_struct_declaration_listR, myDsl_static_assert_declaration, declaration, myDsl_struct_or_union_specifier, type_specifier, myDsl_struct_declarator_list, myDsl_struct_declarator, myDsl_struct_declarator_listR, myDsl_argument_expression_list, myDsl_argument_expression_listR, abstract_declarator, direct_declarator, identifier_list, identifier_listR, labeled_statement, struct_or_union_specifier, postfix_expressionR, myDsl_IDENTIFIER, myDsl_atomic_type_specifier, myDsl_EObject, declaration_specifiers, myDsl_StringC},
    associations={greetings0, External_declaration1, Translation_unitR3, External_declaration5, rec9, Declaration_specifiers11, dd20, Type_qualifier_listR22, rec24, Direct_declaratorR26, rec29, Type_qualifier_list31, Assignment_expression34, Parameter_type_list36, Identifier_list38, Parameter_declaration40, Declarator13, Declaration_list14, Compound_statement16, Pointer18, Declarator152, Declaration_specifiers155, Abstract_declarator58, Declaration60, Declaration_listR62, Declaration64, rec68, Block_item70, Block_item_listR71, Block_item73, rec77, Parameter_listR41, Parameter_declaration43, rec47, Declaration_specifiers249, Expression85, Statement86, Expression_statement89, Declaration91, Init_declarator_list94, Init_declarator96, Init_declarator_listR98, Declarator100, Initializer103, Init_declarator105, rec109, Constant_expression79, Statement80, b82, Expression117, Statement119, Assignment_expression122, ExpressionR125, Assignment_expression127, rec131, Logical_or_expression133, Expression134, Logical_and_expression137, Logical_or_expressionR139, r1112, r2115, Inclusive_or_expression151, rec155, Exclusive_or_expression157, Inclusive_or_expressionR159, Exclusive_or_expression161, rec165, And_expression167, Exclusive_or_expressionR169, And_expression171, rec175, Equality_expression177, rec179, Equality_expression181, Logical_and_expression141, rec145, Inclusive_or_expression147, Logical_and_expressionR149, Relational_expression191, rec195, Shift_expression197, re199, Shift_expression201, rec205, Additive_expression207, rec209, Shift_expressionR211, Multiplicative_expression214, Additive_expressionR216, Multiplicative_expression218, And_expressionR184, Relational_expression187, Equality_expressionR189, Multiplicative_expressionR231, Unary_expression234, rec237, Type_name239, rec242, ce244, Primary_expression247, Postfix_expressionR248, Initializer_list250, Designation252, rec222, Cast_expression224, rec226, Cast_expression228, Initializer265, rec269, Designator271, DesignatorR272, Designator274, rec278, Specifier_qualifier_list280, ad282, Type_specifier285, Initializer254, il257, ilr259, Designation262, Struct_declaration293, Struct_declaration_listR294, Struct_declaration296, rec300, Specifier_qualifier_listx302, Struct_declarator_list305, Struct_declarator308, rec312, Declaratorx314, Constant_expression1317, Struct_declaration_list320, rec288, Struct_declarator290, Struct_declarator_listR291, Argument_expression_list329, Assignment_expression331, Argument_expression_listR334, Assignment_expression336, rec340, Type_qualifier_list342, rec346, dr348, il351, id322, Expression324, rec327, a353, ds356},
    generalizations={gen_myDsl_function_definition_external_declaration, gen_myDsl_type_qualifier_list_pointer, gen_myDsl_direct_declarator_declarator, gen_myDsl_parameter_list_parameter_type_list, gen_myDsl_declarator_init_declarator, gen_myDsl_declarator_struct_declarator, gen_myDsl_compound_statement_statement, gen_myDsl_block_item_list_compound_statement, gen_myDsl_statement_block_item, gen_myDsl_iteration_statement_statement, gen_myDsl_declaration_external_declaration, gen_myDsl_declaration_block_item, gen_myDsl_declaration_specifiers_parameter_declaration, gen_myDsl_jump_statement_statement, gen_myDsl_labeled_statement_statement, gen_myDsl_expression_statement_statement, gen_myDsl_expression_jump_statement, gen_myDsl_expression_expression_statement, gen_myDsl_expression_primary_expression, gen_myDsl_conditional_expression_assignment_expression, gen_myDsl_conditional_expression_constant_expression, gen_myDsl_logical_or_expression_conditional_expression, gen_myDsl_selection_statement_statement, gen_myDsl_additive_expression_shift_expression, gen_myDsl_assignment_expression_initializer, gen_myDsl_unary_expression_cast_expression, gen_myDsl_postfix_expression_unary_expression, gen_myDsl_initializer_list_initializer, gen_myDsl_designator_list_designation, gen_myDsl_constant_expression_designator, gen_myDsl_constant_expression_struct_declarator, gen_myDsl_constant_expression_static_assert_declaration, gen_myDsl_type_name_atomic_type_specifier, gen_myDsl_specifier_qualifier_list_type_name, gen_myDsl_specifier_qualifier_list_struct_declaration, gen_myDsl_static_assert_declaration_declaration, gen_myDsl_static_assert_declaration_struct_declaration, gen_myDsl_struct_or_union_specifier_type_specifier, gen_myDsl_pointer_abstract_declarator, gen_myDsl_IDENTIFIER_direct_declarator, gen_myDsl_IDENTIFIER_identifier_list, gen_myDsl_IDENTIFIER_identifier_listR, gen_myDsl_IDENTIFIER_jump_statement, gen_myDsl_IDENTIFIER_labeled_statement, gen_myDsl_IDENTIFIER_designator, gen_myDsl_IDENTIFIER_struct_or_union_specifier, gen_myDsl_IDENTIFIER_postfix_expressionR, gen_myDsl_IDENTIFIER_primary_expression, gen_myDsl_atomic_type_specifier_type_specifier, gen_myDsl_type_specifier_declaration_specifiers, gen_myDsl_StringC_primary_expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)