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
myDsl_generic_assoc_list = Class(name="myDsl::generic::assoc::list")
myDsl_generic_association = Class(name="myDsl::generic::association")
myDsl_Model = Class(name="myDsl::Model")
myDsl_translation_unit = Class(name="myDsl::translation::unit")
myDsl_simple_expression = Class(name="myDsl::simple::expression")
myDsl_type_name = Class(name="myDsl::type::name")
myDsl_constant = Class(name="myDsl::constant")
myDsl_enumeration_constant = Class(name="myDsl::enumeration::constant")
myDsl_string_nova = Class(name="myDsl::string::nova")
myDsl_expression = Class(name="myDsl::expression")
myDsl_generic_selection = Class(name="myDsl::generic::selection")
myDsl_assignment_expression = Class(name="myDsl::assignment::expression")
myDsl_assignment_operator = Class(name="myDsl::assignment::operator")
myDsl_postfix_expression = Class(name="myDsl::postfix::expression")
myDsl_postfix_expression2 = Class(name="myDsl::postfix::expression2")
myDsl_initializer_list = Class(name="myDsl::initializer::list")
myDsl_argument_expression_list = Class(name="myDsl::argument::expression::list")
postfix_expression2 = Class(name="postfix::expression2")
myDsl_unary_expression = Class(name="myDsl::unary::expression")
simple_expression = Class(name="simple::expression")
myDsl_conditional_expression = Class(name="myDsl::conditional::expression")
myDsl_init_declarator_list = Class(name="myDsl::init::declarator::list")
myDsl_static_assert_declaration = Class(name="myDsl::static::assert::declaration")
myDsl_storage_class_specifier = Class(name="myDsl::storage::class::specifier")
myDsl_type_specifier = Class(name="myDsl::type::specifier")
myDsl_expression2 = Class(name="myDsl::expression2")
myDsl_constant_expression = Class(name="myDsl::constant::expression")
myDsl_declaration = Class(name="myDsl::declaration")
myDsl_declaration_specifiers = Class(name="myDsl::declaration::specifiers")
myDsl_declarator = Class(name="myDsl::declarator")
myDsl_type_qualifier = Class(name="myDsl::type::qualifier")
myDsl_function_specifier = Class(name="myDsl::function::specifier")
myDsl_alignment_specifier = Class(name="myDsl::alignment::specifier")
myDsl_init_declarator = Class(name="myDsl::init::declarator")
myDsl_init_declarator_list2 = Class(name="myDsl::init::declarator::list2")
myDsl_struct_declaration_list2 = Class(name="myDsl::struct::declaration::list2")
myDsl_specifier_qualifier_list = Class(name="myDsl::specifier::qualifier::list")
myDsl_struct_declarator_list = Class(name="myDsl::struct::declarator::list")
myDsl_atomic_type_specifier = Class(name="myDsl::atomic::type::specifier")
myDsl_struct_or_union_specifier = Class(name="myDsl::struct::or::union::specifier")
myDsl_enum_specifier = Class(name="myDsl::enum::specifier")
myDsl_struct_or_union = Class(name="myDsl::struct::or::union")
myDsl_struct_declaration_list = Class(name="myDsl::struct::declaration::list")
struct_or_union_specifier = Class(name="struct::or::union::specifier")
myDsl_struct_declaration = Class(name="myDsl::struct::declaration")
myDsl_struct_declarator = Class(name="myDsl::struct::declarator")
myDsl_struct_declarator_list2 = Class(name="myDsl::struct::declarator::list2")
myDsl_enumerator_list = Class(name="myDsl::enumerator::list")
myDsl_enumerator = Class(name="myDsl::enumerator")
myDsl_enumerator_list2 = Class(name="myDsl::enumerator::list2")
myDsl_type_qualifier_list2 = Class(name="myDsl::type::qualifier::list2")
myDsl_parameter_list = Class(name="myDsl::parameter::list")
myDsl_pointer = Class(name="myDsl::pointer")
myDsl_direct_declarator = Class(name="myDsl::direct::declarator")
myDsl_direct_declarator2 = Class(name="myDsl::direct::declarator2")
myDsl_type_qualifier_list = Class(name="myDsl::type::qualifier::list")
myDsl_parameter_type_list = Class(name="myDsl::parameter::type::list")
myDsl_identifier_list = Class(name="myDsl::identifier::list")
myDsl_direct_abstract_declarator = Class(name="myDsl::direct::abstract::declarator")
myDsl_direct_abstract_declarator2 = Class(name="myDsl::direct::abstract::declarator2")
myDsl_parameter_declaration = Class(name="myDsl::parameter::declaration")
myDsl_parameter_list2 = Class(name="myDsl::parameter::list2")
myDsl_abstract_declarator = Class(name="myDsl::abstract::declarator")
myDsl_identifier_list2 = Class(name="myDsl::identifier::list2")
myDsl_statement = Class(name="myDsl::statement")
myDsl_labeled_statement = Class(name="myDsl::labeled::statement")
myDsl_compound_statement = Class(name="myDsl::compound::statement")
myDsl_expression_statement = Class(name="myDsl::expression::statement")
myDsl_initializer = Class(name="myDsl::initializer")
myDsl_designation = Class(name="myDsl::designation")
myDsl_initializer_list2 = Class(name="myDsl::initializer::list2")
myDsl_designator_list = Class(name="myDsl::designator::list")
myDsl_designator = Class(name="myDsl::designator")
myDsl_designator_list2 = Class(name="myDsl::designator::list2")
myDsl_EObject = Class(name="myDsl::EObject")
myDsl_selection_statement = Class(name="myDsl::selection::statement")
myDsl_iteration_statement = Class(name="myDsl::iteration::statement")
myDsl_jump_statement = Class(name="myDsl::jump::statement")
myDsl_block_item = Class(name="myDsl::block::item")
myDsl_declaration_list2 = Class(name="myDsl::declaration::list2")
myDsl_variableRef = Class(name="myDsl::variableRef")
myDsl_intType = Class(name="myDsl::intType")
type_specifier = Class(name="type::specifier")
myDsl_external_declaration = Class(name="myDsl::external::declaration")
myDsl_function_definition = Class(name="myDsl::function::definition")
myDsl_declaration_list = Class(name="myDsl::declaration::list")
myDsl_SHF = Class(name="myDsl::SHF")
myDsl_REL = Class(name="myDsl::REL")
myDsl_EQL = Class(name="myDsl::EQL")
myDsl_floatType = Class(name="myDsl::floatType")
myDsl_stringType = Class(name="myDsl::stringType")
myDsl_booleanType = Class(name="myDsl::booleanType")
myDsl_MUL = Class(name="myDsl::MUL")
myDsl_ADD = Class(name="myDsl::ADD")
myDsl_MINUS = Class(name="myDsl::MINUS")
myDsl_LOG_OR = Class(name="myDsl::LOG::OR")
myDsl_voidType = Class(name="myDsl::voidType")
myDsl_charType = Class(name="myDsl::charType")
myDsl_shortType = Class(name="myDsl::shortType")
myDsl_longType = Class(name="myDsl::longType")
myDsl_AND = Class(name="myDsl::AND")
myDsl_EXC_OR = Class(name="myDsl::EXC::OR")
myDsl_INC_OR = Class(name="myDsl::INC::OR")
myDsl_LOG_AND = Class(name="myDsl::LOG::AND")
myDsl_doubleType = Class(name="myDsl::doubleType")
myDsl_signedType = Class(name="myDsl::signedType")
myDsl_unsignedType = Class(name="myDsl::unsignedType")
myDsl_complexType = Class(name="myDsl::complexType")
myDsl_imaginaryType = Class(name="myDsl::imaginaryType")

# myDsl_generic_assoc_list class attributes and methods

# myDsl_generic_association class attributes and methods
myDsl_generic_association_default: Property = Property(name="default", type=StringType)
myDsl_generic_association.attributes={myDsl_generic_association_default}

# myDsl_Model class attributes and methods

# myDsl_translation_unit class attributes and methods

# myDsl_simple_expression class attributes and methods

# myDsl_type_name class attributes and methods

# myDsl_constant class attributes and methods
myDsl_constant_i_constant: Property = Property(name="i_constant", type=StringType)
myDsl_constant_f_constant: Property = Property(name="f_constant", type=StringType)
myDsl_constant_enumt: Property = Property(name="enumt", type=StringType)
myDsl_constant.attributes={myDsl_constant_i_constant, myDsl_constant_enumt, myDsl_constant_f_constant}

# myDsl_enumeration_constant class attributes and methods
myDsl_enumeration_constant_identifier: Property = Property(name="identifier", type=StringType)
myDsl_enumeration_constant.attributes={myDsl_enumeration_constant_identifier}

# myDsl_string_nova class attributes and methods
myDsl_string_nova_string_literal: Property = Property(name="string_literal", type=StringType)
myDsl_string_nova_func_name: Property = Property(name="func_name", type=StringType)
myDsl_string_nova.attributes={myDsl_string_nova_func_name, myDsl_string_nova_string_literal}

# myDsl_expression class attributes and methods

# myDsl_generic_selection class attributes and methods
myDsl_generic_selection_generic: Property = Property(name="generic", type=StringType)
myDsl_generic_selection.attributes={myDsl_generic_selection_generic}

# myDsl_assignment_expression class attributes and methods

# myDsl_assignment_operator class attributes and methods
myDsl_assignment_operator_mul_assign: Property = Property(name="mul_assign", type=StringType)
myDsl_assignment_operator_div_assign: Property = Property(name="div_assign", type=StringType)
myDsl_assignment_operator_mod_assign: Property = Property(name="mod_assign", type=StringType)
myDsl_assignment_operator_add_assign: Property = Property(name="add_assign", type=StringType)
myDsl_assignment_operator_sub_assign: Property = Property(name="sub_assign", type=StringType)
myDsl_assignment_operator_left_assign: Property = Property(name="left_assign", type=StringType)
myDsl_assignment_operator_right_assign: Property = Property(name="right_assign", type=StringType)
myDsl_assignment_operator_and_assign: Property = Property(name="and_assign", type=StringType)
myDsl_assignment_operator_xor_assign: Property = Property(name="xor_assign", type=StringType)
myDsl_assignment_operator_or_assign: Property = Property(name="or_assign", type=StringType)
myDsl_assignment_operator.attributes={myDsl_assignment_operator_mul_assign, myDsl_assignment_operator_div_assign, myDsl_assignment_operator_add_assign, myDsl_assignment_operator_mod_assign, myDsl_assignment_operator_left_assign, myDsl_assignment_operator_or_assign, myDsl_assignment_operator_right_assign, myDsl_assignment_operator_sub_assign, myDsl_assignment_operator_and_assign, myDsl_assignment_operator_xor_assign}

# myDsl_postfix_expression class attributes and methods

# myDsl_postfix_expression2 class attributes and methods

# myDsl_initializer_list class attributes and methods

# myDsl_argument_expression_list class attributes and methods

# postfix_expression2 class attributes and methods

# myDsl_unary_expression class attributes and methods
myDsl_unary_expression_inc_op: Property = Property(name="inc_op", type=StringType)
myDsl_unary_expression_dec_op: Property = Property(name="dec_op", type=StringType)
myDsl_unary_expression_unary_operator: Property = Property(name="unary_operator", type=StringType)
myDsl_unary_expression_sizeof: Property = Property(name="sizeof", type=StringType)
myDsl_unary_expression_alignof: Property = Property(name="alignof", type=StringType)
myDsl_unary_expression.attributes={myDsl_unary_expression_inc_op, myDsl_unary_expression_dec_op, myDsl_unary_expression_unary_operator, myDsl_unary_expression_sizeof, myDsl_unary_expression_alignof}

# simple_expression class attributes and methods

# myDsl_conditional_expression class attributes and methods

# myDsl_init_declarator_list class attributes and methods

# myDsl_static_assert_declaration class attributes and methods
myDsl_static_assert_declaration_static_assert: Property = Property(name="static_assert", type=StringType)
myDsl_static_assert_declaration_string_literal: Property = Property(name="string_literal", type=StringType)
myDsl_static_assert_declaration.attributes={myDsl_static_assert_declaration_static_assert, myDsl_static_assert_declaration_string_literal}

# myDsl_storage_class_specifier class attributes and methods
myDsl_storage_class_specifier_typedef: Property = Property(name="typedef", type=StringType)
myDsl_storage_class_specifier_extern: Property = Property(name="extern", type=StringType)
myDsl_storage_class_specifier_static: Property = Property(name="static", type=StringType)
myDsl_storage_class_specifier_thread_local: Property = Property(name="thread_local", type=StringType)
myDsl_storage_class_specifier_auto: Property = Property(name="auto", type=StringType)
myDsl_storage_class_specifier_register: Property = Property(name="register", type=StringType)
myDsl_storage_class_specifier.attributes={myDsl_storage_class_specifier_auto, myDsl_storage_class_specifier_register, myDsl_storage_class_specifier_thread_local, myDsl_storage_class_specifier_static, myDsl_storage_class_specifier_extern, myDsl_storage_class_specifier_typedef}

# myDsl_type_specifier class attributes and methods
myDsl_type_specifier_typedef_name: Property = Property(name="typedef_name", type=StringType)
myDsl_type_specifier.attributes={myDsl_type_specifier_typedef_name}

# myDsl_expression2 class attributes and methods

# myDsl_constant_expression class attributes and methods

# myDsl_declaration class attributes and methods

# myDsl_declaration_specifiers class attributes and methods

# myDsl_declarator class attributes and methods

# myDsl_type_qualifier class attributes and methods
myDsl_type_qualifier_const: Property = Property(name="const", type=StringType)
myDsl_type_qualifier_restrict: Property = Property(name="restrict", type=StringType)
myDsl_type_qualifier_volatile: Property = Property(name="volatile", type=StringType)
myDsl_type_qualifier_atomic: Property = Property(name="atomic", type=StringType)
myDsl_type_qualifier.attributes={myDsl_type_qualifier_const, myDsl_type_qualifier_volatile, myDsl_type_qualifier_atomic, myDsl_type_qualifier_restrict}

# myDsl_function_specifier class attributes and methods
myDsl_function_specifier_inline: Property = Property(name="inline", type=StringType)
myDsl_function_specifier_noreturn: Property = Property(name="noreturn", type=StringType)
myDsl_function_specifier.attributes={myDsl_function_specifier_noreturn, myDsl_function_specifier_inline}

# myDsl_alignment_specifier class attributes and methods
myDsl_alignment_specifier_alignas: Property = Property(name="alignas", type=StringType)
myDsl_alignment_specifier.attributes={myDsl_alignment_specifier_alignas}

# myDsl_init_declarator class attributes and methods

# myDsl_init_declarator_list2 class attributes and methods

# myDsl_struct_declaration_list2 class attributes and methods

# myDsl_specifier_qualifier_list class attributes and methods

# myDsl_struct_declarator_list class attributes and methods

# myDsl_atomic_type_specifier class attributes and methods
myDsl_atomic_type_specifier_atomic: Property = Property(name="atomic", type=StringType)
myDsl_atomic_type_specifier.attributes={myDsl_atomic_type_specifier_atomic}

# myDsl_struct_or_union_specifier class attributes and methods
myDsl_struct_or_union_specifier_identifier: Property = Property(name="identifier", type=StringType)
myDsl_struct_or_union_specifier.attributes={myDsl_struct_or_union_specifier_identifier}

# myDsl_enum_specifier class attributes and methods
myDsl_enum_specifier_enumt: Property = Property(name="enumt", type=StringType)
myDsl_enum_specifier_identifier: Property = Property(name="identifier", type=StringType)
myDsl_enum_specifier.attributes={myDsl_enum_specifier_enumt, myDsl_enum_specifier_identifier}

# myDsl_struct_or_union class attributes and methods
myDsl_struct_or_union_struct: Property = Property(name="struct", type=StringType)
myDsl_struct_or_union_union: Property = Property(name="union", type=StringType)
myDsl_struct_or_union.attributes={myDsl_struct_or_union_struct, myDsl_struct_or_union_union}

# myDsl_struct_declaration_list class attributes and methods

# struct_or_union_specifier class attributes and methods

# myDsl_struct_declaration class attributes and methods

# myDsl_struct_declarator class attributes and methods

# myDsl_struct_declarator_list2 class attributes and methods

# myDsl_enumerator_list class attributes and methods

# myDsl_enumerator class attributes and methods

# myDsl_enumerator_list2 class attributes and methods

# myDsl_type_qualifier_list2 class attributes and methods

# myDsl_parameter_list class attributes and methods

# myDsl_pointer class attributes and methods

# myDsl_direct_declarator class attributes and methods
myDsl_direct_declarator_name: Property = Property(name="name", type=StringType)
myDsl_direct_declarator.attributes={myDsl_direct_declarator_name}

# myDsl_direct_declarator2 class attributes and methods
myDsl_direct_declarator2_static: Property = Property(name="static", type=StringType)
myDsl_direct_declarator2.attributes={myDsl_direct_declarator2_static}

# myDsl_type_qualifier_list class attributes and methods

# myDsl_parameter_type_list class attributes and methods
myDsl_parameter_type_list_ellipsis: Property = Property(name="ellipsis", type=StringType)
myDsl_parameter_type_list.attributes={myDsl_parameter_type_list_ellipsis}

# myDsl_identifier_list class attributes and methods
myDsl_identifier_list_identifier: Property = Property(name="identifier", type=StringType)
myDsl_identifier_list.attributes={myDsl_identifier_list_identifier}

# myDsl_direct_abstract_declarator class attributes and methods

# myDsl_direct_abstract_declarator2 class attributes and methods
myDsl_direct_abstract_declarator2_static: Property = Property(name="static", type=StringType)
myDsl_direct_abstract_declarator2.attributes={myDsl_direct_abstract_declarator2_static}

# myDsl_parameter_declaration class attributes and methods

# myDsl_parameter_list2 class attributes and methods

# myDsl_abstract_declarator class attributes and methods

# myDsl_identifier_list2 class attributes and methods
myDsl_identifier_list2_identifier: Property = Property(name="identifier", type=StringType)
myDsl_identifier_list2.attributes={myDsl_identifier_list2_identifier}

# myDsl_statement class attributes and methods

# myDsl_labeled_statement class attributes and methods
myDsl_labeled_statement_identifier: Property = Property(name="identifier", type=StringType)
myDsl_labeled_statement_case: Property = Property(name="case", type=StringType)
myDsl_labeled_statement_default: Property = Property(name="default", type=StringType)
myDsl_labeled_statement.attributes={myDsl_labeled_statement_case, myDsl_labeled_statement_identifier, myDsl_labeled_statement_default}

# myDsl_compound_statement class attributes and methods

# myDsl_expression_statement class attributes and methods

# myDsl_initializer class attributes and methods

# myDsl_designation class attributes and methods

# myDsl_initializer_list2 class attributes and methods

# myDsl_designator_list class attributes and methods

# myDsl_designator class attributes and methods
myDsl_designator_identifier: Property = Property(name="identifier", type=StringType)
myDsl_designator.attributes={myDsl_designator_identifier}

# myDsl_designator_list2 class attributes and methods

# myDsl_EObject class attributes and methods

# myDsl_selection_statement class attributes and methods
myDsl_selection_statement_else: Property = Property(name="else", type=StringType)
myDsl_selection_statement_switch: Property = Property(name="switch", type=StringType)
myDsl_selection_statement_if: Property = Property(name="if", type=StringType)
myDsl_selection_statement.attributes={myDsl_selection_statement_if, myDsl_selection_statement_switch, myDsl_selection_statement_else}

# myDsl_iteration_statement class attributes and methods
myDsl_iteration_statement_while: Property = Property(name="while", type=StringType)
myDsl_iteration_statement_do: Property = Property(name="do", type=StringType)
myDsl_iteration_statement_for: Property = Property(name="for", type=StringType)
myDsl_iteration_statement.attributes={myDsl_iteration_statement_do, myDsl_iteration_statement_for, myDsl_iteration_statement_while}

# myDsl_jump_statement class attributes and methods
myDsl_jump_statement_goto: Property = Property(name="goto", type=StringType)
myDsl_jump_statement_identifier: Property = Property(name="identifier", type=StringType)
myDsl_jump_statement_continue: Property = Property(name="continue", type=StringType)
myDsl_jump_statement_break: Property = Property(name="break", type=StringType)
myDsl_jump_statement_return: Property = Property(name="return", type=StringType)
myDsl_jump_statement.attributes={myDsl_jump_statement_identifier, myDsl_jump_statement_return, myDsl_jump_statement_continue, myDsl_jump_statement_goto, myDsl_jump_statement_break}

# myDsl_block_item class attributes and methods

# myDsl_declaration_list2 class attributes and methods

# myDsl_variableRef class attributes and methods
myDsl_variableRef_variable: Property = Property(name="variable", type=StringType)
myDsl_variableRef.attributes={myDsl_variableRef_variable}

# myDsl_intType class attributes and methods
myDsl_intType_value: Property = Property(name="value", type=StringType)
myDsl_intType_int_type: Property = Property(name="int_type", type=StringType)
myDsl_intType.attributes={myDsl_intType_value, myDsl_intType_int_type}

# type_specifier class attributes and methods

# myDsl_external_declaration class attributes and methods

# myDsl_function_definition class attributes and methods

# myDsl_declaration_list class attributes and methods

# myDsl_SHF class attributes and methods
myDsl_SHF_op: Property = Property(name="op", type=StringType)
myDsl_SHF.attributes={myDsl_SHF_op}

# myDsl_REL class attributes and methods
myDsl_REL_op: Property = Property(name="op", type=StringType)
myDsl_REL.attributes={myDsl_REL_op}

# myDsl_EQL class attributes and methods
myDsl_EQL_op: Property = Property(name="op", type=StringType)
myDsl_EQL.attributes={myDsl_EQL_op}

# myDsl_floatType class attributes and methods
myDsl_floatType_value: Property = Property(name="value", type=StringType)
myDsl_floatType_float_type: Property = Property(name="float_type", type=StringType)
myDsl_floatType.attributes={myDsl_floatType_value, myDsl_floatType_float_type}

# myDsl_stringType class attributes and methods

# myDsl_booleanType class attributes and methods
myDsl_booleanType_value: Property = Property(name="value", type=StringType)
myDsl_booleanType_bool_type: Property = Property(name="bool_type", type=StringType)
myDsl_booleanType.attributes={myDsl_booleanType_bool_type, myDsl_booleanType_value}

# myDsl_MUL class attributes and methods
myDsl_MUL_op: Property = Property(name="op", type=StringType)
myDsl_MUL.attributes={myDsl_MUL_op}

# myDsl_ADD class attributes and methods

# myDsl_MINUS class attributes and methods

# myDsl_LOG_OR class attributes and methods

# myDsl_voidType class attributes and methods
myDsl_voidType_void_type: Property = Property(name="void_type", type=StringType)
myDsl_voidType.attributes={myDsl_voidType_void_type}

# myDsl_charType class attributes and methods
myDsl_charType_char_type: Property = Property(name="char_type", type=StringType)
myDsl_charType.attributes={myDsl_charType_char_type}

# myDsl_shortType class attributes and methods
myDsl_shortType_short_type: Property = Property(name="short_type", type=StringType)
myDsl_shortType.attributes={myDsl_shortType_short_type}

# myDsl_longType class attributes and methods
myDsl_longType_long_type: Property = Property(name="long_type", type=StringType)
myDsl_longType.attributes={myDsl_longType_long_type}

# myDsl_AND class attributes and methods

# myDsl_EXC_OR class attributes and methods

# myDsl_INC_OR class attributes and methods

# myDsl_LOG_AND class attributes and methods

# myDsl_doubleType class attributes and methods
myDsl_doubleType_double_type: Property = Property(name="double_type", type=StringType)
myDsl_doubleType.attributes={myDsl_doubleType_double_type}

# myDsl_signedType class attributes and methods
myDsl_signedType_signed_type: Property = Property(name="signed_type", type=StringType)
myDsl_signedType.attributes={myDsl_signedType_signed_type}

# myDsl_unsignedType class attributes and methods
myDsl_unsignedType_unsigned_type: Property = Property(name="unsigned_type", type=StringType)
myDsl_unsignedType.attributes={myDsl_unsignedType_unsigned_type}

# myDsl_complexType class attributes and methods
myDsl_complexType_complex_type: Property = Property(name="complex_type", type=StringType)
myDsl_complexType.attributes={myDsl_complexType_complex_type}

# myDsl_imaginaryType class attributes and methods
myDsl_imaginaryType_imaginary_type: Property = Property(name="imaginary_type", type=StringType)
myDsl_imaginaryType.attributes={myDsl_imaginaryType_imaginary_type}

# Relationships
generic_assoc_list6: BinaryAssociation = BinaryAssociation(
    name="generic_assoc_list6",
    ends={
        Property(name="myDsl_generic_assoc_list", type=myDsl_generic_selection, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_generic_selection7", type=myDsl_generic_assoc_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
generic_association8: BinaryAssociation = BinaryAssociation(
    name="generic_association8",
    ends={
        Property(name="myDsl_generic_association", type=myDsl_generic_assoc_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_generic_assoc_list9", type=myDsl_generic_association, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
generic_list10: BinaryAssociation = BinaryAssociation(
    name="generic_list10",
    ends={
        Property(name="myDsl_generic_association12", type=myDsl_generic_assoc_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_generic_assoc_list11", type=myDsl_generic_association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type_name13: BinaryAssociation = BinaryAssociation(
    name="type_name13",
    ends={
        Property(name="myDsl_type_name15", type=myDsl_generic_association, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_generic_association14", type=myDsl_type_name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaracoes0: BinaryAssociation = BinaryAssociation(
    name="declaracoes0",
    ends={
        Property(name="myDsl_translation_unit", type=myDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Model", type=myDsl_translation_unit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type_name1: BinaryAssociation = BinaryAssociation(
    name="type_name1",
    ends={
        Property(name="myDsl_type_name", type=myDsl_simple_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_simple_expression", type=myDsl_type_name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cast_expression3: BinaryAssociation = BinaryAssociation(
    name="cast_expression3",
    ends={
        Property(name="myDsl_simple_expression4", type=myDsl_simple_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_simple_expression2", type=myDsl_simple_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
logical_or_expression40: BinaryAssociation = BinaryAssociation(
    name="logical_or_expression40",
    ends={
        Property(name="myDsl_simple_expression42", type=myDsl_conditional_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_conditional_expression41", type=myDsl_simple_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression43: BinaryAssociation = BinaryAssociation(
    name="expression43",
    ends={
        Property(name="myDsl_expression", type=myDsl_conditional_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_conditional_expression44", type=myDsl_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditional_expression46: BinaryAssociation = BinaryAssociation(
    name="conditional_expression46",
    ends={
        Property(name="myDsl_conditional_expression47", type=myDsl_conditional_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_conditional_expression45", type=myDsl_conditional_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment_expression5: BinaryAssociation = BinaryAssociation(
    name="assignment_expression5",
    ends={
        Property(name="myDsl_assignment_expression", type=myDsl_generic_selection, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_generic_selection", type=myDsl_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditional_expression48: BinaryAssociation = BinaryAssociation(
    name="conditional_expression48",
    ends={
        Property(name="myDsl_conditional_expression50", type=myDsl_assignment_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_assignment_expression49", type=myDsl_conditional_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unary_expression51: BinaryAssociation = BinaryAssociation(
    name="unary_expression51",
    ends={
        Property(name="myDsl_unary_expression53", type=myDsl_assignment_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_assignment_expression52", type=myDsl_unary_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment_operator54: BinaryAssociation = BinaryAssociation(
    name="assignment_operator54",
    ends={
        Property(name="myDsl_assignment_operator", type=myDsl_assignment_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_assignment_expression55", type=myDsl_assignment_operator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment_expression16: BinaryAssociation = BinaryAssociation(
    name="assignment_expression16",
    ends={
        Property(name="myDsl_assignment_expression18", type=myDsl_generic_association, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_generic_association17", type=myDsl_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primary_expression19: BinaryAssociation = BinaryAssociation(
    name="primary_expression19",
    ends={
        Property(name="myDsl_simple_expression20", type=myDsl_postfix_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_postfix_expression", type=myDsl_simple_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postifx_expres21: BinaryAssociation = BinaryAssociation(
    name="postifx_expres21",
    ends={
        Property(name="myDsl_postfix_expression2", type=myDsl_postfix_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_postfix_expression22", type=myDsl_postfix_expression2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type_name23: BinaryAssociation = BinaryAssociation(
    name="type_name23",
    ends={
        Property(name="myDsl_type_name25", type=myDsl_postfix_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_postfix_expression24", type=myDsl_type_name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initializer_list26: BinaryAssociation = BinaryAssociation(
    name="initializer_list26",
    ends={
        Property(name="myDsl_initializer_list", type=myDsl_postfix_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_postfix_expression27", type=myDsl_initializer_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment_expression28: BinaryAssociation = BinaryAssociation(
    name="assignment_expression28",
    ends={
        Property(name="myDsl_assignment_expression30", type=myDsl_postfix_expression2, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_postfix_expression229", type=myDsl_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
list31: BinaryAssociation = BinaryAssociation(
    name="list31",
    ends={
        Property(name="myDsl_assignment_expression32", type=myDsl_argument_expression_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_argument_expression_list", type=myDsl_assignment_expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postfix_expression33: BinaryAssociation = BinaryAssociation(
    name="postfix_expression33",
    ends={
        Property(name="myDsl_postfix_expression34", type=myDsl_unary_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_unary_expression", type=myDsl_postfix_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unary_expression36: BinaryAssociation = BinaryAssociation(
    name="unary_expression36",
    ends={
        Property(name="myDsl_unary_expression37", type=myDsl_unary_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_unary_expression35", type=myDsl_unary_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simple_expression38: BinaryAssociation = BinaryAssociation(
    name="simple_expression38",
    ends={
        Property(name="myDsl_simple_expression39", type=myDsl_conditional_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_conditional_expression", type=myDsl_simple_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init_declarator_list70: BinaryAssociation = BinaryAssociation(
    name="init_declarator_list70",
    ends={
        Property(name="myDsl_init_declarator_list", type=myDsl_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declaration71", type=myDsl_init_declarator_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
static_assert_declaration72: BinaryAssociation = BinaryAssociation(
    name="static_assert_declaration72",
    ends={
        Property(name="myDsl_static_assert_declaration", type=myDsl_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declaration73", type=myDsl_static_assert_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
storage_class_specifier74: BinaryAssociation = BinaryAssociation(
    name="storage_class_specifier74",
    ends={
        Property(name="myDsl_storage_class_specifier", type=myDsl_declaration_specifiers, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declaration_specifiers75", type=myDsl_storage_class_specifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration_specifiers77: BinaryAssociation = BinaryAssociation(
    name="declaration_specifiers77",
    ends={
        Property(name="myDsl_declaration_specifiers78", type=myDsl_declaration_specifiers, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declaration_specifiers76", type=myDsl_declaration_specifiers, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_specifier79: BinaryAssociation = BinaryAssociation(
    name="type_specifier79",
    ends={
        Property(name="myDsl_type_specifier", type=myDsl_declaration_specifiers, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declaration_specifiers80", type=myDsl_type_specifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment_expression57: BinaryAssociation = BinaryAssociation(
    name="assignment_expression57",
    ends={
        Property(name="myDsl_assignment_expression58", type=myDsl_assignment_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_assignment_expression56", type=myDsl_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression259: BinaryAssociation = BinaryAssociation(
    name="expression259",
    ends={
        Property(name="myDsl_expression2", type=myDsl_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_expression60", type=myDsl_expression2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment_expression61: BinaryAssociation = BinaryAssociation(
    name="assignment_expression61",
    ends={
        Property(name="myDsl_assignment_expression63", type=myDsl_expression2, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_expression262", type=myDsl_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression265: BinaryAssociation = BinaryAssociation(
    name="expression265",
    ends={
        Property(name="myDsl_expression266", type=myDsl_expression2, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_expression264", type=myDsl_expression2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditional_expression67: BinaryAssociation = BinaryAssociation(
    name="conditional_expression67",
    ends={
        Property(name="myDsl_conditional_expression68", type=myDsl_constant_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_constant_expression", type=myDsl_conditional_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration_specifiers69: BinaryAssociation = BinaryAssociation(
    name="declaration_specifiers69",
    ends={
        Property(name="myDsl_declaration_specifiers", type=myDsl_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declaration", type=myDsl_declaration_specifiers, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init_declarator_list295: BinaryAssociation = BinaryAssociation(
    name="init_declarator_list295",
    ends={
        Property(name="myDsl_init_declarator_list296", type=myDsl_init_declarator_list2, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_init_declarator_list294", type=myDsl_init_declarator_list2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarator97: BinaryAssociation = BinaryAssociation(
    name="declarator97",
    ends={
        Property(name="myDsl_declarator", type=myDsl_init_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_init_declarator98", type=myDsl_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initializer99: BinaryAssociation = BinaryAssociation(
    name="initializer99",
    ends={
        Property(name="myDsl_simple_expression101", type=myDsl_init_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_init_declarator100", type=myDsl_simple_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_qualifier81: BinaryAssociation = BinaryAssociation(
    name="type_qualifier81",
    ends={
        Property(name="myDsl_type_qualifier", type=myDsl_declaration_specifiers, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declaration_specifiers82", type=myDsl_type_qualifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function_specifier83: BinaryAssociation = BinaryAssociation(
    name="function_specifier83",
    ends={
        Property(name="myDsl_function_specifier", type=myDsl_declaration_specifiers, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declaration_specifiers84", type=myDsl_function_specifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alignment_specifier85: BinaryAssociation = BinaryAssociation(
    name="alignment_specifier85",
    ends={
        Property(name="myDsl_alignment_specifier", type=myDsl_declaration_specifiers, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declaration_specifiers86", type=myDsl_alignment_specifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init_declarator87: BinaryAssociation = BinaryAssociation(
    name="init_declarator87",
    ends={
        Property(name="myDsl_init_declarator", type=myDsl_init_declarator_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_init_declarator_list88", type=myDsl_init_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init_declarator_list289: BinaryAssociation = BinaryAssociation(
    name="init_declarator_list289",
    ends={
        Property(name="myDsl_init_declarator_list2", type=myDsl_init_declarator_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_init_declarator_list90", type=myDsl_init_declarator_list2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init_declarator91: BinaryAssociation = BinaryAssociation(
    name="init_declarator91",
    ends={
        Property(name="myDsl_init_declarator93", type=myDsl_init_declarator_list2, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_init_declarator_list292", type=myDsl_init_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_declaration_list2114: BinaryAssociation = BinaryAssociation(
    name="struct_declaration_list2114",
    ends={
        Property(name="myDsl_struct_declaration_list2", type=myDsl_struct_declaration_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declaration_list115", type=myDsl_struct_declaration_list2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_declaration116: BinaryAssociation = BinaryAssociation(
    name="struct_declaration116",
    ends={
        Property(name="myDsl_struct_declaration118", type=myDsl_struct_declaration_list2, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declaration_list2117", type=myDsl_struct_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_declaration_list2120: BinaryAssociation = BinaryAssociation(
    name="struct_declaration_list2120",
    ends={
        Property(name="myDsl_struct_declaration_list2121", type=myDsl_struct_declaration_list2, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declaration_list2119", type=myDsl_struct_declaration_list2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specifier_qualifier_list122: BinaryAssociation = BinaryAssociation(
    name="specifier_qualifier_list122",
    ends={
        Property(name="myDsl_specifier_qualifier_list", type=myDsl_struct_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declaration123", type=myDsl_specifier_qualifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_declarator_list124: BinaryAssociation = BinaryAssociation(
    name="struct_declarator_list124",
    ends={
        Property(name="myDsl_struct_declarator_list", type=myDsl_struct_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declaration125", type=myDsl_struct_declarator_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
static_assert_declaration126: BinaryAssociation = BinaryAssociation(
    name="static_assert_declaration126",
    ends={
        Property(name="myDsl_static_assert_declaration128", type=myDsl_struct_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declaration127", type=myDsl_static_assert_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_specifier129: BinaryAssociation = BinaryAssociation(
    name="type_specifier129",
    ends={
        Property(name="myDsl_type_specifier131", type=myDsl_specifier_qualifier_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_specifier_qualifier_list130", type=myDsl_type_specifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
atomic_type_specifier102: BinaryAssociation = BinaryAssociation(
    name="atomic_type_specifier102",
    ends={
        Property(name="myDsl_atomic_type_specifier", type=myDsl_type_specifier, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_type_specifier103", type=myDsl_atomic_type_specifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_or_union_specifier104: BinaryAssociation = BinaryAssociation(
    name="struct_or_union_specifier104",
    ends={
        Property(name="myDsl_struct_or_union_specifier", type=myDsl_type_specifier, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_type_specifier105", type=myDsl_struct_or_union_specifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enum_specifier106: BinaryAssociation = BinaryAssociation(
    name="enum_specifier106",
    ends={
        Property(name="myDsl_enum_specifier", type=myDsl_type_specifier, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_type_specifier107", type=myDsl_enum_specifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_or_union108: BinaryAssociation = BinaryAssociation(
    name="struct_or_union108",
    ends={
        Property(name="myDsl_struct_or_union", type=myDsl_struct_or_union_specifier, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_or_union_specifier109", type=myDsl_struct_or_union, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_declaration_list110: BinaryAssociation = BinaryAssociation(
    name="struct_declaration_list110",
    ends={
        Property(name="myDsl_struct_declaration_list", type=myDsl_struct_or_union_specifier, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_or_union_specifier111", type=myDsl_struct_declaration_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_declaration112: BinaryAssociation = BinaryAssociation(
    name="struct_declaration112",
    ends={
        Property(name="myDsl_struct_declaration", type=myDsl_struct_declaration_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declaration_list113", type=myDsl_struct_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumerator160: BinaryAssociation = BinaryAssociation(
    name="enumerator160",
    ends={
        Property(name="myDsl_enumerator162", type=myDsl_enumerator_list2, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_enumerator_list2161", type=myDsl_enumerator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumerator_list2164: BinaryAssociation = BinaryAssociation(
    name="enumerator_list2164",
    ends={
        Property(name="myDsl_enumerator_list2165", type=myDsl_enumerator_list2, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_enumerator_list2163", type=myDsl_enumerator_list2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumeration_constant166: BinaryAssociation = BinaryAssociation(
    name="enumeration_constant166",
    ends={
        Property(name="myDsl_enumeration_constant", type=myDsl_enumerator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_enumerator167", type=myDsl_enumeration_constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant_expression168: BinaryAssociation = BinaryAssociation(
    name="constant_expression168",
    ends={
        Property(name="myDsl_constant_expression170", type=myDsl_enumerator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_enumerator169", type=myDsl_constant_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_name171: BinaryAssociation = BinaryAssociation(
    name="type_name171",
    ends={
        Property(name="myDsl_type_name173", type=myDsl_atomic_type_specifier, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_atomic_type_specifier172", type=myDsl_type_name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specifier_qualifier_list133: BinaryAssociation = BinaryAssociation(
    name="specifier_qualifier_list133",
    ends={
        Property(name="myDsl_specifier_qualifier_list134", type=myDsl_specifier_qualifier_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_specifier_qualifier_list132", type=myDsl_specifier_qualifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_qualifier135: BinaryAssociation = BinaryAssociation(
    name="type_qualifier135",
    ends={
        Property(name="myDsl_type_specifier137", type=myDsl_specifier_qualifier_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_specifier_qualifier_list136", type=myDsl_type_specifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_declarator138: BinaryAssociation = BinaryAssociation(
    name="struct_declarator138",
    ends={
        Property(name="myDsl_struct_declarator", type=myDsl_struct_declarator_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declarator_list139", type=myDsl_struct_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_declarator_list2140: BinaryAssociation = BinaryAssociation(
    name="struct_declarator_list2140",
    ends={
        Property(name="myDsl_struct_declarator_list2", type=myDsl_struct_declarator_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declarator_list141", type=myDsl_struct_declarator_list2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_declarator142: BinaryAssociation = BinaryAssociation(
    name="struct_declarator142",
    ends={
        Property(name="myDsl_struct_declarator144", type=myDsl_struct_declarator_list2, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declarator_list2143", type=myDsl_struct_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_declarator_list2146: BinaryAssociation = BinaryAssociation(
    name="struct_declarator_list2146",
    ends={
        Property(name="myDsl_struct_declarator_list2147", type=myDsl_struct_declarator_list2, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declarator_list2145", type=myDsl_struct_declarator_list2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant_expression148: BinaryAssociation = BinaryAssociation(
    name="constant_expression148",
    ends={
        Property(name="myDsl_constant_expression150", type=myDsl_struct_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declarator149", type=myDsl_constant_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarator151: BinaryAssociation = BinaryAssociation(
    name="declarator151",
    ends={
        Property(name="myDsl_declarator153", type=myDsl_struct_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declarator152", type=myDsl_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumerator_list154: BinaryAssociation = BinaryAssociation(
    name="enumerator_list154",
    ends={
        Property(name="myDsl_enumerator_list", type=myDsl_enum_specifier, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_enum_specifier155", type=myDsl_enumerator_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumerator156: BinaryAssociation = BinaryAssociation(
    name="enumerator156",
    ends={
        Property(name="myDsl_enumerator", type=myDsl_enumerator_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_enumerator_list157", type=myDsl_enumerator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumerator_list2158: BinaryAssociation = BinaryAssociation(
    name="enumerator_list2158",
    ends={
        Property(name="myDsl_enumerator_list2", type=myDsl_enumerator_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_enumerator_list159", type=myDsl_enumerator_list2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier_list199: BinaryAssociation = BinaryAssociation(
    name="identifier_list199",
    ends={
        Property(name="myDsl_identifier_list", type=myDsl_direct_declarator2, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_declarator2200", type=myDsl_identifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_qualifier_list201: BinaryAssociation = BinaryAssociation(
    name="type_qualifier_list201",
    ends={
        Property(name="myDsl_type_qualifier_list203", type=myDsl_pointer, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_pointer202", type=myDsl_type_qualifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pointer205: BinaryAssociation = BinaryAssociation(
    name="pointer205",
    ends={
        Property(name="myDsl_pointer206", type=myDsl_pointer, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_pointer204", type=myDsl_pointer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_qualifier207: BinaryAssociation = BinaryAssociation(
    name="type_qualifier207",
    ends={
        Property(name="myDsl_type_qualifier209", type=myDsl_type_qualifier_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_type_qualifier_list208", type=myDsl_type_qualifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_qualifier_list2210: BinaryAssociation = BinaryAssociation(
    name="type_qualifier_list2210",
    ends={
        Property(name="myDsl_type_qualifier_list2", type=myDsl_type_qualifier_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_type_qualifier_list211", type=myDsl_type_qualifier_list2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_qualifier212: BinaryAssociation = BinaryAssociation(
    name="type_qualifier212",
    ends={
        Property(name="myDsl_type_qualifier214", type=myDsl_type_qualifier_list2, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_type_qualifier_list2213", type=myDsl_type_qualifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_qualifier_list2216: BinaryAssociation = BinaryAssociation(
    name="type_qualifier_list2216",
    ends={
        Property(name="myDsl_type_qualifier_list2217", type=myDsl_type_qualifier_list2, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_type_qualifier_list2215", type=myDsl_type_qualifier_list2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_name174: BinaryAssociation = BinaryAssociation(
    name="type_name174",
    ends={
        Property(name="myDsl_type_name176", type=myDsl_alignment_specifier, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_alignment_specifier175", type=myDsl_type_name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant_expression177: BinaryAssociation = BinaryAssociation(
    name="constant_expression177",
    ends={
        Property(name="myDsl_constant_expression179", type=myDsl_alignment_specifier, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_alignment_specifier178", type=myDsl_constant_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pointer180: BinaryAssociation = BinaryAssociation(
    name="pointer180",
    ends={
        Property(name="myDsl_pointer", type=myDsl_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declarator181", type=myDsl_pointer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
direct_declarator182: BinaryAssociation = BinaryAssociation(
    name="direct_declarator182",
    ends={
        Property(name="myDsl_direct_declarator", type=myDsl_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declarator183", type=myDsl_direct_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
direct_declarators184: BinaryAssociation = BinaryAssociation(
    name="direct_declarators184",
    ends={
        Property(name="myDsl_direct_declarator2", type=myDsl_direct_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_declarator185", type=myDsl_direct_declarator2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Declarator186: BinaryAssociation = BinaryAssociation(
    name="Declarator186",
    ends={
        Property(name="myDsl_declarator188", type=myDsl_direct_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_declarator187", type=myDsl_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarators190: BinaryAssociation = BinaryAssociation(
    name="declarators190",
    ends={
        Property(name="myDsl_direct_declarator2191", type=myDsl_direct_declarator2, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_declarator2189", type=myDsl_direct_declarator2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type_qualifier_list192: BinaryAssociation = BinaryAssociation(
    name="type_qualifier_list192",
    ends={
        Property(name="myDsl_type_qualifier_list", type=myDsl_direct_declarator2, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_declarator2193", type=myDsl_type_qualifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment_expression194: BinaryAssociation = BinaryAssociation(
    name="assignment_expression194",
    ends={
        Property(name="myDsl_assignment_expression196", type=myDsl_direct_declarator2, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_declarator2195", type=myDsl_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter_type_list197: BinaryAssociation = BinaryAssociation(
    name="parameter_type_list197",
    ends={
        Property(name="myDsl_parameter_type_list", type=myDsl_direct_declarator2, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_declarator2198", type=myDsl_parameter_type_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
abstract_declarator246: BinaryAssociation = BinaryAssociation(
    name="abstract_declarator246",
    ends={
        Property(name="myDsl_abstract_declarator248", type=myDsl_type_name, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_type_name247", type=myDsl_abstract_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pointer249: BinaryAssociation = BinaryAssociation(
    name="pointer249",
    ends={
        Property(name="myDsl_pointer251", type=myDsl_abstract_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_abstract_declarator250", type=myDsl_pointer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
direct_abstract_declarator252: BinaryAssociation = BinaryAssociation(
    name="direct_abstract_declarator252",
    ends={
        Property(name="myDsl_direct_abstract_declarator", type=myDsl_abstract_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_abstract_declarator253", type=myDsl_direct_abstract_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
direct_abstract_declarator2254: BinaryAssociation = BinaryAssociation(
    name="direct_abstract_declarator2254",
    ends={
        Property(name="myDsl_direct_abstract_declarator2", type=myDsl_direct_abstract_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_abstract_declarator255", type=myDsl_direct_abstract_declarator2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type_qualifier_list256: BinaryAssociation = BinaryAssociation(
    name="type_qualifier_list256",
    ends={
        Property(name="myDsl_type_qualifier_list258", type=myDsl_direct_abstract_declarator2, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_abstract_declarator2257", type=myDsl_type_qualifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment_expression259: BinaryAssociation = BinaryAssociation(
    name="assignment_expression259",
    ends={
        Property(name="myDsl_assignment_expression261", type=myDsl_direct_abstract_declarator2, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_abstract_declarator2260", type=myDsl_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter_list218: BinaryAssociation = BinaryAssociation(
    name="parameter_list218",
    ends={
        Property(name="myDsl_parameter_list", type=myDsl_parameter_type_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_parameter_type_list219", type=myDsl_parameter_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter_declaration220: BinaryAssociation = BinaryAssociation(
    name="parameter_declaration220",
    ends={
        Property(name="myDsl_parameter_declaration", type=myDsl_parameter_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_parameter_list221", type=myDsl_parameter_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter_list2222: BinaryAssociation = BinaryAssociation(
    name="parameter_list2222",
    ends={
        Property(name="myDsl_parameter_list2", type=myDsl_parameter_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_parameter_list223", type=myDsl_parameter_list2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter_declaration224: BinaryAssociation = BinaryAssociation(
    name="parameter_declaration224",
    ends={
        Property(name="myDsl_parameter_declaration226", type=myDsl_parameter_list2, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_parameter_list2225", type=myDsl_parameter_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter_list2228: BinaryAssociation = BinaryAssociation(
    name="parameter_list2228",
    ends={
        Property(name="myDsl_parameter_list2229", type=myDsl_parameter_list2, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_parameter_list2227", type=myDsl_parameter_list2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration_specifiers230: BinaryAssociation = BinaryAssociation(
    name="declaration_specifiers230",
    ends={
        Property(name="myDsl_declaration_specifiers232", type=myDsl_parameter_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_parameter_declaration231", type=myDsl_declaration_specifiers, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarator233: BinaryAssociation = BinaryAssociation(
    name="declarator233",
    ends={
        Property(name="myDsl_declarator235", type=myDsl_parameter_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_parameter_declaration234", type=myDsl_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
abstract_declarator236: BinaryAssociation = BinaryAssociation(
    name="abstract_declarator236",
    ends={
        Property(name="myDsl_abstract_declarator", type=myDsl_parameter_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_parameter_declaration237", type=myDsl_abstract_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier_list2238: BinaryAssociation = BinaryAssociation(
    name="identifier_list2238",
    ends={
        Property(name="myDsl_identifier_list2", type=myDsl_identifier_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_identifier_list239", type=myDsl_identifier_list2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier_list2241: BinaryAssociation = BinaryAssociation(
    name="identifier_list2241",
    ends={
        Property(name="myDsl_identifier_list2242", type=myDsl_identifier_list2, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_identifier_list2240", type=myDsl_identifier_list2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specifier_qualifier_list243: BinaryAssociation = BinaryAssociation(
    name="specifier_qualifier_list243",
    ends={
        Property(name="myDsl_specifier_qualifier_list245", type=myDsl_type_name, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_type_name244", type=myDsl_specifier_qualifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
designator292: BinaryAssociation = BinaryAssociation(
    name="designator292",
    ends={
        Property(name="myDsl_designator294", type=myDsl_designator_list2, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_designator_list2293", type=myDsl_designator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
designator_list2296: BinaryAssociation = BinaryAssociation(
    name="designator_list2296",
    ends={
        Property(name="myDsl_designator_list2297", type=myDsl_designator_list2, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_designator_list2295", type=myDsl_designator_list2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant_expression298: BinaryAssociation = BinaryAssociation(
    name="constant_expression298",
    ends={
        Property(name="myDsl_constant_expression300", type=myDsl_designator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_designator299", type=myDsl_constant_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant_expression301: BinaryAssociation = BinaryAssociation(
    name="constant_expression301",
    ends={
        Property(name="myDsl_constant_expression303", type=myDsl_static_assert_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_static_assert_declaration302", type=myDsl_constant_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labeled_statement304: BinaryAssociation = BinaryAssociation(
    name="labeled_statement304",
    ends={
        Property(name="myDsl_labeled_statement", type=myDsl_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_statement", type=myDsl_labeled_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
compound_statement305: BinaryAssociation = BinaryAssociation(
    name="compound_statement305",
    ends={
        Property(name="myDsl_compound_statement", type=myDsl_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_statement306", type=myDsl_compound_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter_type_list262: BinaryAssociation = BinaryAssociation(
    name="parameter_type_list262",
    ends={
        Property(name="myDsl_parameter_type_list264", type=myDsl_direct_abstract_declarator2, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_abstract_declarator2263", type=myDsl_parameter_type_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initializer_list265: BinaryAssociation = BinaryAssociation(
    name="initializer_list265",
    ends={
        Property(name="myDsl_initializer_list266", type=myDsl_initializer, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_initializer", type=myDsl_initializer_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment_expression267: BinaryAssociation = BinaryAssociation(
    name="assignment_expression267",
    ends={
        Property(name="myDsl_assignment_expression269", type=myDsl_initializer, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_initializer268", type=myDsl_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
designation270: BinaryAssociation = BinaryAssociation(
    name="designation270",
    ends={
        Property(name="myDsl_designation", type=myDsl_initializer_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_initializer_list271", type=myDsl_designation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initializer272: BinaryAssociation = BinaryAssociation(
    name="initializer272",
    ends={
        Property(name="myDsl_initializer274", type=myDsl_initializer_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_initializer_list273", type=myDsl_initializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initializer_list2275: BinaryAssociation = BinaryAssociation(
    name="initializer_list2275",
    ends={
        Property(name="myDsl_initializer_list2", type=myDsl_initializer_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_initializer_list276", type=myDsl_initializer_list2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
designation277: BinaryAssociation = BinaryAssociation(
    name="designation277",
    ends={
        Property(name="myDsl_designation279", type=myDsl_initializer_list2, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_initializer_list2278", type=myDsl_designation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initializer280: BinaryAssociation = BinaryAssociation(
    name="initializer280",
    ends={
        Property(name="myDsl_initializer282", type=myDsl_initializer_list2, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_initializer_list2281", type=myDsl_initializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initializer_list2284: BinaryAssociation = BinaryAssociation(
    name="initializer_list2284",
    ends={
        Property(name="myDsl_initializer_list2285", type=myDsl_initializer_list2, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_initializer_list2283", type=myDsl_initializer_list2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
designator_list286: BinaryAssociation = BinaryAssociation(
    name="designator_list286",
    ends={
        Property(name="myDsl_designator_list", type=myDsl_designation, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_designation287", type=myDsl_designator_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
designator288: BinaryAssociation = BinaryAssociation(
    name="designator288",
    ends={
        Property(name="myDsl_designator", type=myDsl_designator_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_designator_list289", type=myDsl_designator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
designator_list2290: BinaryAssociation = BinaryAssociation(
    name="designator_list2290",
    ends={
        Property(name="myDsl_designator_list2", type=myDsl_designator_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_designator_list291", type=myDsl_designator_list2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression332: BinaryAssociation = BinaryAssociation(
    name="expression332",
    ends={
        Property(name="myDsl_selection_statement333", type=myDsl_simple_expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="myDsl_simple_expression334", type=myDsl_selection_statement, multiplicity=Multiplicity(1, 1))
    }
)
statement335: BinaryAssociation = BinaryAssociation(
    name="statement335",
    ends={
        Property(name="myDsl_statement337", type=myDsl_selection_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_selection_statement336", type=myDsl_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement2338: BinaryAssociation = BinaryAssociation(
    name="statement2338",
    ends={
        Property(name="myDsl_statement340", type=myDsl_selection_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_selection_statement339", type=myDsl_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression341: BinaryAssociation = BinaryAssociation(
    name="expression341",
    ends={
        Property(name="myDsl_EObject", type=myDsl_iteration_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_iteration_statement342", type=myDsl_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement343: BinaryAssociation = BinaryAssociation(
    name="statement343",
    ends={
        Property(name="myDsl_statement345", type=myDsl_iteration_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_iteration_statement344", type=myDsl_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression_statement346: BinaryAssociation = BinaryAssociation(
    name="expression_statement346",
    ends={
        Property(name="myDsl_expression_statement348", type=myDsl_iteration_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_iteration_statement347", type=myDsl_expression_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression_statement307: BinaryAssociation = BinaryAssociation(
    name="expression_statement307",
    ends={
        Property(name="myDsl_expression_statement", type=myDsl_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_statement308", type=myDsl_expression_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selection_statement309: BinaryAssociation = BinaryAssociation(
    name="selection_statement309",
    ends={
        Property(name="myDsl_selection_statement", type=myDsl_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_statement310", type=myDsl_selection_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iteration_statement311: BinaryAssociation = BinaryAssociation(
    name="iteration_statement311",
    ends={
        Property(name="myDsl_iteration_statement", type=myDsl_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_statement312", type=myDsl_iteration_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
jump_statement313: BinaryAssociation = BinaryAssociation(
    name="jump_statement313",
    ends={
        Property(name="myDsl_jump_statement", type=myDsl_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_statement314", type=myDsl_jump_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement315: BinaryAssociation = BinaryAssociation(
    name="statement315",
    ends={
        Property(name="myDsl_statement317", type=myDsl_labeled_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_labeled_statement316", type=myDsl_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant_expression318: BinaryAssociation = BinaryAssociation(
    name="constant_expression318",
    ends={
        Property(name="myDsl_constant_expression320", type=myDsl_labeled_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_labeled_statement319", type=myDsl_constant_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block_item_list321: BinaryAssociation = BinaryAssociation(
    name="block_item_list321",
    ends={
        Property(name="myDsl_block_item", type=myDsl_compound_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_compound_statement322", type=myDsl_block_item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaration323: BinaryAssociation = BinaryAssociation(
    name="declaration323",
    ends={
        Property(name="myDsl_declaration325", type=myDsl_block_item, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_block_item324", type=myDsl_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement326: BinaryAssociation = BinaryAssociation(
    name="statement326",
    ends={
        Property(name="myDsl_statement328", type=myDsl_block_item, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_block_item327", type=myDsl_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression329: BinaryAssociation = BinaryAssociation(
    name="expression329",
    ends={
        Property(name="myDsl_expression331", type=myDsl_expression_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_expression_statement330", type=myDsl_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
compound_statement373: BinaryAssociation = BinaryAssociation(
    name="compound_statement373",
    ends={
        Property(name="myDsl_compound_statement375", type=myDsl_function_definition, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_function_definition374", type=myDsl_compound_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration376: BinaryAssociation = BinaryAssociation(
    name="declaration376",
    ends={
        Property(name="myDsl_declaration378", type=myDsl_declaration_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declaration_list377", type=myDsl_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration_list_2379: BinaryAssociation = BinaryAssociation(
    name="declaration_list_2379",
    ends={
        Property(name="myDsl_declaration_list2", type=myDsl_declaration_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declaration_list380", type=myDsl_declaration_list2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration381: BinaryAssociation = BinaryAssociation(
    name="declaration381",
    ends={
        Property(name="myDsl_declaration383", type=myDsl_declaration_list2, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declaration_list2382", type=myDsl_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration_list2385: BinaryAssociation = BinaryAssociation(
    name="declaration_list2385",
    ends={
        Property(name="myDsl_declaration_list2386", type=myDsl_declaration_list2, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declaration_list2384", type=myDsl_declaration_list2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression_statement2349: BinaryAssociation = BinaryAssociation(
    name="expression_statement2349",
    ends={
        Property(name="myDsl_expression_statement351", type=myDsl_iteration_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_iteration_statement350", type=myDsl_expression_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration352: BinaryAssociation = BinaryAssociation(
    name="declaration352",
    ends={
        Property(name="myDsl_declaration354", type=myDsl_iteration_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_iteration_statement353", type=myDsl_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression355: BinaryAssociation = BinaryAssociation(
    name="expression355",
    ends={
        Property(name="myDsl_expression357", type=myDsl_jump_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_jump_statement356", type=myDsl_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
external_declaration358: BinaryAssociation = BinaryAssociation(
    name="external_declaration358",
    ends={
        Property(name="myDsl_external_declaration", type=myDsl_translation_unit, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_translation_unit359", type=myDsl_external_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function_definition360: BinaryAssociation = BinaryAssociation(
    name="function_definition360",
    ends={
        Property(name="myDsl_function_definition", type=myDsl_external_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_external_declaration361", type=myDsl_function_definition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration362: BinaryAssociation = BinaryAssociation(
    name="declaration362",
    ends={
        Property(name="myDsl_declaration364", type=myDsl_external_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_external_declaration363", type=myDsl_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration_specifiers365: BinaryAssociation = BinaryAssociation(
    name="declaration_specifiers365",
    ends={
        Property(name="myDsl_declaration_specifiers367", type=myDsl_function_definition, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_function_definition366", type=myDsl_declaration_specifiers, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarator368: BinaryAssociation = BinaryAssociation(
    name="declarator368",
    ends={
        Property(name="myDsl_declarator370", type=myDsl_function_definition, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_function_definition369", type=myDsl_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration_list371: BinaryAssociation = BinaryAssociation(
    name="declaration_list371",
    ends={
        Property(name="myDsl_declaration_list", type=myDsl_function_definition, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_function_definition372", type=myDsl_declaration_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right400: BinaryAssociation = BinaryAssociation(
    name="right400",
    ends={
        Property(name="myDsl_simple_expression402", type=myDsl_MINUS, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_MINUS401", type=myDsl_simple_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left403: BinaryAssociation = BinaryAssociation(
    name="left403",
    ends={
        Property(name="myDsl_simple_expression404", type=myDsl_SHF, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_SHF", type=myDsl_simple_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right405: BinaryAssociation = BinaryAssociation(
    name="right405",
    ends={
        Property(name="myDsl_simple_expression407", type=myDsl_SHF, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_SHF406", type=myDsl_simple_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left408: BinaryAssociation = BinaryAssociation(
    name="left408",
    ends={
        Property(name="myDsl_simple_expression409", type=myDsl_REL, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_REL", type=myDsl_simple_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right410: BinaryAssociation = BinaryAssociation(
    name="right410",
    ends={
        Property(name="myDsl_simple_expression412", type=myDsl_REL, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_REL411", type=myDsl_simple_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value387: BinaryAssociation = BinaryAssociation(
    name="value387",
    ends={
        Property(name="myDsl_string_nova", type=myDsl_stringType, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_stringType", type=myDsl_string_nova, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left388: BinaryAssociation = BinaryAssociation(
    name="left388",
    ends={
        Property(name="myDsl_simple_expression389", type=myDsl_MUL, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_MUL", type=myDsl_simple_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right390: BinaryAssociation = BinaryAssociation(
    name="right390",
    ends={
        Property(name="myDsl_simple_expression392", type=myDsl_MUL, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_MUL391", type=myDsl_simple_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left393: BinaryAssociation = BinaryAssociation(
    name="left393",
    ends={
        Property(name="myDsl_simple_expression394", type=myDsl_ADD, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ADD", type=myDsl_simple_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right395: BinaryAssociation = BinaryAssociation(
    name="right395",
    ends={
        Property(name="myDsl_simple_expression397", type=myDsl_ADD, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ADD396", type=myDsl_simple_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left398: BinaryAssociation = BinaryAssociation(
    name="left398",
    ends={
        Property(name="myDsl_simple_expression399", type=myDsl_MINUS, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_MINUS", type=myDsl_simple_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right435: BinaryAssociation = BinaryAssociation(
    name="right435",
    ends={
        Property(name="myDsl_simple_expression437", type=myDsl_LOG_AND, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_LOG_AND436", type=myDsl_simple_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left438: BinaryAssociation = BinaryAssociation(
    name="left438",
    ends={
        Property(name="myDsl_simple_expression439", type=myDsl_LOG_OR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_LOG_OR", type=myDsl_simple_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right440: BinaryAssociation = BinaryAssociation(
    name="right440",
    ends={
        Property(name="myDsl_simple_expression442", type=myDsl_LOG_OR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_LOG_OR441", type=myDsl_simple_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left413: BinaryAssociation = BinaryAssociation(
    name="left413",
    ends={
        Property(name="myDsl_simple_expression414", type=myDsl_EQL, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_EQL", type=myDsl_simple_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right415: BinaryAssociation = BinaryAssociation(
    name="right415",
    ends={
        Property(name="myDsl_simple_expression417", type=myDsl_EQL, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_EQL416", type=myDsl_simple_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left418: BinaryAssociation = BinaryAssociation(
    name="left418",
    ends={
        Property(name="myDsl_simple_expression419", type=myDsl_AND, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_AND", type=myDsl_simple_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right420: BinaryAssociation = BinaryAssociation(
    name="right420",
    ends={
        Property(name="myDsl_simple_expression422", type=myDsl_AND, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_AND421", type=myDsl_simple_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left423: BinaryAssociation = BinaryAssociation(
    name="left423",
    ends={
        Property(name="myDsl_simple_expression424", type=myDsl_EXC_OR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_EXC_OR", type=myDsl_simple_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right425: BinaryAssociation = BinaryAssociation(
    name="right425",
    ends={
        Property(name="myDsl_simple_expression427", type=myDsl_EXC_OR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_EXC_OR426", type=myDsl_simple_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left428: BinaryAssociation = BinaryAssociation(
    name="left428",
    ends={
        Property(name="myDsl_simple_expression429", type=myDsl_INC_OR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_INC_OR", type=myDsl_simple_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right430: BinaryAssociation = BinaryAssociation(
    name="right430",
    ends={
        Property(name="myDsl_simple_expression432", type=myDsl_INC_OR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_INC_OR431", type=myDsl_simple_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left433: BinaryAssociation = BinaryAssociation(
    name="left433",
    ends={
        Property(name="myDsl_simple_expression434", type=myDsl_LOG_AND, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_LOG_AND", type=myDsl_simple_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_myDsl_argument_expression_list_postfix_expression2 = Generalization(general=postfix_expression2, specific=myDsl_argument_expression_list)
gen_myDsl_unary_expression_simple_expression = Generalization(general=simple_expression, specific=myDsl_unary_expression)
gen_myDsl_expression_postfix_expression2 = Generalization(general=postfix_expression2, specific=myDsl_expression)
gen_myDsl_struct_or_union_struct_or_union_specifier = Generalization(general=struct_or_union_specifier, specific=myDsl_struct_or_union)
gen_myDsl_variableRef_simple_expression = Generalization(general=simple_expression, specific=myDsl_variableRef)
gen_myDsl_intType_simple_expression = Generalization(general=simple_expression, specific=myDsl_intType)
gen_myDsl_intType_type_specifier = Generalization(general=type_specifier, specific=myDsl_intType)
gen_myDsl_SHF_simple_expression = Generalization(general=simple_expression, specific=myDsl_SHF)
gen_myDsl_REL_simple_expression = Generalization(general=simple_expression, specific=myDsl_REL)
gen_myDsl_EQL_simple_expression = Generalization(general=simple_expression, specific=myDsl_EQL)
gen_myDsl_floatType_simple_expression = Generalization(general=simple_expression, specific=myDsl_floatType)
gen_myDsl_floatType_type_specifier = Generalization(general=type_specifier, specific=myDsl_floatType)
gen_myDsl_stringType_simple_expression = Generalization(general=simple_expression, specific=myDsl_stringType)
gen_myDsl_booleanType_simple_expression = Generalization(general=simple_expression, specific=myDsl_booleanType)
gen_myDsl_booleanType_type_specifier = Generalization(general=type_specifier, specific=myDsl_booleanType)
gen_myDsl_MUL_simple_expression = Generalization(general=simple_expression, specific=myDsl_MUL)
gen_myDsl_ADD_simple_expression = Generalization(general=simple_expression, specific=myDsl_ADD)
gen_myDsl_MINUS_simple_expression = Generalization(general=simple_expression, specific=myDsl_MINUS)
gen_myDsl_LOG_OR_simple_expression = Generalization(general=simple_expression, specific=myDsl_LOG_OR)
gen_myDsl_voidType_type_specifier = Generalization(general=type_specifier, specific=myDsl_voidType)
gen_myDsl_charType_type_specifier = Generalization(general=type_specifier, specific=myDsl_charType)
gen_myDsl_shortType_type_specifier = Generalization(general=type_specifier, specific=myDsl_shortType)
gen_myDsl_longType_type_specifier = Generalization(general=type_specifier, specific=myDsl_longType)
gen_myDsl_AND_simple_expression = Generalization(general=simple_expression, specific=myDsl_AND)
gen_myDsl_EXC_OR_simple_expression = Generalization(general=simple_expression, specific=myDsl_EXC_OR)
gen_myDsl_INC_OR_simple_expression = Generalization(general=simple_expression, specific=myDsl_INC_OR)
gen_myDsl_LOG_AND_simple_expression = Generalization(general=simple_expression, specific=myDsl_LOG_AND)
gen_myDsl_doubleType_type_specifier = Generalization(general=type_specifier, specific=myDsl_doubleType)
gen_myDsl_signedType_type_specifier = Generalization(general=type_specifier, specific=myDsl_signedType)
gen_myDsl_unsignedType_type_specifier = Generalization(general=type_specifier, specific=myDsl_unsignedType)
gen_myDsl_complexType_type_specifier = Generalization(general=type_specifier, specific=myDsl_complexType)
gen_myDsl_imaginaryType_type_specifier = Generalization(general=type_specifier, specific=myDsl_imaginaryType)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_generic_assoc_list, myDsl_generic_association, myDsl_Model, myDsl_translation_unit, myDsl_simple_expression, myDsl_type_name, myDsl_constant, myDsl_enumeration_constant, myDsl_string_nova, myDsl_expression, myDsl_generic_selection, myDsl_assignment_expression, myDsl_assignment_operator, myDsl_postfix_expression, myDsl_postfix_expression2, myDsl_initializer_list, myDsl_argument_expression_list, postfix_expression2, myDsl_unary_expression, simple_expression, myDsl_conditional_expression, myDsl_init_declarator_list, myDsl_static_assert_declaration, myDsl_storage_class_specifier, myDsl_type_specifier, myDsl_expression2, myDsl_constant_expression, myDsl_declaration, myDsl_declaration_specifiers, myDsl_declarator, myDsl_type_qualifier, myDsl_function_specifier, myDsl_alignment_specifier, myDsl_init_declarator, myDsl_init_declarator_list2, myDsl_struct_declaration_list2, myDsl_specifier_qualifier_list, myDsl_struct_declarator_list, myDsl_atomic_type_specifier, myDsl_struct_or_union_specifier, myDsl_enum_specifier, myDsl_struct_or_union, myDsl_struct_declaration_list, struct_or_union_specifier, myDsl_struct_declaration, myDsl_struct_declarator, myDsl_struct_declarator_list2, myDsl_enumerator_list, myDsl_enumerator, myDsl_enumerator_list2, myDsl_type_qualifier_list2, myDsl_parameter_list, myDsl_pointer, myDsl_direct_declarator, myDsl_direct_declarator2, myDsl_type_qualifier_list, myDsl_parameter_type_list, myDsl_identifier_list, myDsl_direct_abstract_declarator, myDsl_direct_abstract_declarator2, myDsl_parameter_declaration, myDsl_parameter_list2, myDsl_abstract_declarator, myDsl_identifier_list2, myDsl_statement, myDsl_labeled_statement, myDsl_compound_statement, myDsl_expression_statement, myDsl_initializer, myDsl_designation, myDsl_initializer_list2, myDsl_designator_list, myDsl_designator, myDsl_designator_list2, myDsl_EObject, myDsl_selection_statement, myDsl_iteration_statement, myDsl_jump_statement, myDsl_block_item, myDsl_declaration_list2, myDsl_variableRef, myDsl_intType, type_specifier, myDsl_external_declaration, myDsl_function_definition, myDsl_declaration_list, myDsl_SHF, myDsl_REL, myDsl_EQL, myDsl_floatType, myDsl_stringType, myDsl_booleanType, myDsl_MUL, myDsl_ADD, myDsl_MINUS, myDsl_LOG_OR, myDsl_voidType, myDsl_charType, myDsl_shortType, myDsl_longType, myDsl_AND, myDsl_EXC_OR, myDsl_INC_OR, myDsl_LOG_AND, myDsl_doubleType, myDsl_signedType, myDsl_unsignedType, myDsl_complexType, myDsl_imaginaryType},
    associations={generic_assoc_list6, generic_association8, generic_list10, type_name13, declaracoes0, type_name1, cast_expression3, logical_or_expression40, expression43, conditional_expression46, assignment_expression5, conditional_expression48, unary_expression51, assignment_operator54, assignment_expression16, primary_expression19, postifx_expres21, type_name23, initializer_list26, assignment_expression28, list31, postfix_expression33, unary_expression36, simple_expression38, init_declarator_list70, static_assert_declaration72, storage_class_specifier74, declaration_specifiers77, type_specifier79, assignment_expression57, expression259, assignment_expression61, expression265, conditional_expression67, declaration_specifiers69, init_declarator_list295, declarator97, initializer99, type_qualifier81, function_specifier83, alignment_specifier85, init_declarator87, init_declarator_list289, init_declarator91, struct_declaration_list2114, struct_declaration116, struct_declaration_list2120, specifier_qualifier_list122, struct_declarator_list124, static_assert_declaration126, type_specifier129, atomic_type_specifier102, struct_or_union_specifier104, enum_specifier106, struct_or_union108, struct_declaration_list110, struct_declaration112, enumerator160, enumerator_list2164, enumeration_constant166, constant_expression168, type_name171, specifier_qualifier_list133, type_qualifier135, struct_declarator138, struct_declarator_list2140, struct_declarator142, struct_declarator_list2146, constant_expression148, declarator151, enumerator_list154, enumerator156, enumerator_list2158, identifier_list199, type_qualifier_list201, pointer205, type_qualifier207, type_qualifier_list2210, type_qualifier212, type_qualifier_list2216, type_name174, constant_expression177, pointer180, direct_declarator182, direct_declarators184, Declarator186, declarators190, type_qualifier_list192, assignment_expression194, parameter_type_list197, abstract_declarator246, pointer249, direct_abstract_declarator252, direct_abstract_declarator2254, type_qualifier_list256, assignment_expression259, parameter_list218, parameter_declaration220, parameter_list2222, parameter_declaration224, parameter_list2228, declaration_specifiers230, declarator233, abstract_declarator236, identifier_list2238, identifier_list2241, specifier_qualifier_list243, designator292, designator_list2296, constant_expression298, constant_expression301, labeled_statement304, compound_statement305, parameter_type_list262, initializer_list265, assignment_expression267, designation270, initializer272, initializer_list2275, designation277, initializer280, initializer_list2284, designator_list286, designator288, designator_list2290, expression332, statement335, statement2338, expression341, statement343, expression_statement346, expression_statement307, selection_statement309, iteration_statement311, jump_statement313, statement315, constant_expression318, block_item_list321, declaration323, statement326, expression329, compound_statement373, declaration376, declaration_list_2379, declaration381, declaration_list2385, expression_statement2349, declaration352, expression355, external_declaration358, function_definition360, declaration362, declaration_specifiers365, declarator368, declaration_list371, right400, left403, right405, left408, right410, value387, left388, right390, left393, right395, left398, right435, left438, right440, left413, right415, left418, right420, left423, right425, left428, right430, left433},
    generalizations={gen_myDsl_argument_expression_list_postfix_expression2, gen_myDsl_unary_expression_simple_expression, gen_myDsl_expression_postfix_expression2, gen_myDsl_struct_or_union_struct_or_union_specifier, gen_myDsl_variableRef_simple_expression, gen_myDsl_intType_simple_expression, gen_myDsl_intType_type_specifier, gen_myDsl_SHF_simple_expression, gen_myDsl_REL_simple_expression, gen_myDsl_EQL_simple_expression, gen_myDsl_floatType_simple_expression, gen_myDsl_floatType_type_specifier, gen_myDsl_stringType_simple_expression, gen_myDsl_booleanType_simple_expression, gen_myDsl_booleanType_type_specifier, gen_myDsl_MUL_simple_expression, gen_myDsl_ADD_simple_expression, gen_myDsl_MINUS_simple_expression, gen_myDsl_LOG_OR_simple_expression, gen_myDsl_voidType_type_specifier, gen_myDsl_charType_type_specifier, gen_myDsl_shortType_type_specifier, gen_myDsl_longType_type_specifier, gen_myDsl_AND_simple_expression, gen_myDsl_EXC_OR_simple_expression, gen_myDsl_INC_OR_simple_expression, gen_myDsl_LOG_AND_simple_expression, gen_myDsl_doubleType_type_specifier, gen_myDsl_signedType_type_specifier, gen_myDsl_unsignedType_type_specifier, gen_myDsl_complexType_type_specifier, gen_myDsl_imaginaryType_type_specifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)