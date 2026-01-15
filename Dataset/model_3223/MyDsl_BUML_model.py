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
myDsl_type_specifier = Class(name="myDsl::type::specifier")
myDsl_type_qualifier = Class(name="myDsl::type::qualifier")
myDsl_alignment_specifier = Class(name="myDsl::alignment::specifier")
myDsl_type_name = Class(name="myDsl::type::name")
myDsl_constant_expression = Class(name="myDsl::constant::expression")
myDsl_Model = Class(name="myDsl::Model")
myDsl_translation_unit = Class(name="myDsl::translation::unit")
myDsl_external_declaration = Class(name="myDsl::external::declaration")
myDsl_translation_unit_linha = Class(name="myDsl::translation::unit::linha")
myDsl_function_definition = Class(name="myDsl::function::definition")
myDsl_declaration = Class(name="myDsl::declaration")
myDsl_declaration_specifiers = Class(name="myDsl::declaration::specifiers")
myDsl_struct_declaration = Class(name="myDsl::struct::declaration")
myDsl_struct_declaration_list_linha = Class(name="myDsl::struct::declaration::list::linha")
myDsl_specifier_qualifier_list = Class(name="myDsl::specifier::qualifier::list")
myDsl_struct_declarator_list = Class(name="myDsl::struct::declarator::list")
myDsl_static_assert_declaration = Class(name="myDsl::static::assert::declaration")
myDsl_struct_declarator = Class(name="myDsl::struct::declarator")
myDsl_atomic_type_specifier = Class(name="myDsl::atomic::type::specifier")
myDsl_struct_or_union_specifier = Class(name="myDsl::struct::or::union::specifier")
myDsl_enum_specifier = Class(name="myDsl::enum::specifier")
myDsl_enumerator_list = Class(name="myDsl::enumerator::list")
myDsl_enumerator = Class(name="myDsl::enumerator")
myDsl_enumerator_list_linha = Class(name="myDsl::enumerator::list::linha")
myDsl_enumeration_constant = Class(name="myDsl::enumeration::constant")
myDsl_struct_declaration_list = Class(name="myDsl::struct::declaration::list")
myDsl_struct_or_union_specifier_complement = Class(name="myDsl::struct::or::union::specifier::complement")
myDsl_declaration_list_linha = Class(name="myDsl::declaration::list::linha")
myDsl_pointer = Class(name="myDsl::pointer")
myDsl_direct_declarator = Class(name="myDsl::direct::declarator")
myDsl_type_qualifier_list = Class(name="myDsl::type::qualifier::list")
myDsl_struct_declarator_list_linha = Class(name="myDsl::struct::declarator::list::linha")
myDsl_declarator = Class(name="myDsl::declarator")
myDsl_init_declarator_list = Class(name="myDsl::init::declarator::list")
myDsl_declaration_list = Class(name="myDsl::declaration::list")
myDsl_compound_statement = Class(name="myDsl::compound::statement")
myDsl_parameter_declaration = Class(name="myDsl::parameter::declaration")
myDsl_parameter_list_linha = Class(name="myDsl::parameter::list::linha")
myDsl_abstract_declarator = Class(name="myDsl::abstract::declarator")
direct_abstract_declarator_complement = Class(name="direct::abstract::declarator::complement")
myDsl_type_qualifier_list_linha = Class(name="myDsl::type::qualifier::list::linha")
myDsl_direct_declarator_linha = Class(name="myDsl::direct::declarator::linha")
myDsl_direct_declarator_complemento = Class(name="myDsl::direct::declarator::complemento")
myDsl_assignment_expression = Class(name="myDsl::assignment::expression")
myDsl_parameter_type_list = Class(name="myDsl::parameter::type::list")
myDsl_identifier_list = Class(name="myDsl::identifier::list")
myDsl_parameter_lista = Class(name="myDsl::parameter::lista")
myDsl_identifier_list_linha = Class(name="myDsl::identifier::list::linha")
myDsl_direct_abstract_declarator = Class(name="myDsl::direct::abstract::declarator")
myDsl_direct_abstract_declarator_linha = Class(name="myDsl::direct::abstract::declarator::linha")
myDsl_initializer = Class(name="myDsl::initializer")
myDsl_initializer_list = Class(name="myDsl::initializer::list")
myDsl_direct_abstract_declarator_complement = Class(name="myDsl::direct::abstract::declarator::complement")
myDsl_postfix_expression_linha = Class(name="myDsl::postfix::expression::linha")
myDsl_designation = Class(name="myDsl::designation")
myDsl_init_declarator_list_linha = Class(name="myDsl::init::declarator::list::linha")
myDsl_initializer_list_linha = Class(name="myDsl::initializer::list::linha")
myDsl_initializer_list_complement = Class(name="myDsl::initializer::list::complement")
myDsl_designator_list = Class(name="myDsl::designator::list")
myDsl_primary_expression = Class(name="myDsl::primary::expression")
myDsl_designator = Class(name="myDsl::designator")
myDsl_designator_list_linha = Class(name="myDsl::designator::list::linha")
myDsl_constant = Class(name="myDsl::constant")
myDsl_expression = Class(name="myDsl::expression")
myDsl_generic_selection = Class(name="myDsl::generic::selection")
myDsl_generic_assoc_list = Class(name="myDsl::generic::assoc::list")
myDsl_generic_association = Class(name="myDsl::generic::association")
myDsl_generic_assoc_list_linha = Class(name="myDsl::generic::assoc::list::linha")
myDsl_postfix_expression = Class(name="myDsl::postfix::expression")
myDsl_cast_expression = Class(name="myDsl::cast::expression")
myDsl_multiplicative_expression = Class(name="myDsl::multiplicative::expression")
myDsl_multiplicative_expression_linha = Class(name="myDsl::multiplicative::expression::linha")
myDsl_multiplicative_expression_complement = Class(name="myDsl::multiplicative::expression::complement")
myDsl_conditional_expression = Class(name="myDsl::conditional::expression")
myDsl_postfix_expression_complement = Class(name="myDsl::postfix::expression::complement")
myDsl_argument_expression_list = Class(name="myDsl::argument::expression::list")
myDsl_argument_expression_list_linha = Class(name="myDsl::argument::expression::list::linha")
myDsl_unary_expression = Class(name="myDsl::unary::expression")
myDsl_relational_expression = Class(name="myDsl::relational::expression")
myDsl_relational_expression_linha = Class(name="myDsl::relational::expression::linha")
myDsl_relational_expression_complement = Class(name="myDsl::relational::expression::complement")
myDsl_equality_expression = Class(name="myDsl::equality::expression")
myDsl_additive_expression = Class(name="myDsl::additive::expression")
myDsl_additive_expression_linha = Class(name="myDsl::additive::expression::linha")
myDsl_additive_expression_complement = Class(name="myDsl::additive::expression::complement")
myDsl_shift_expression = Class(name="myDsl::shift::expression")
myDsl_shift_expression_linha = Class(name="myDsl::shift::expression::linha")
myDsl_shift_expression_complement = Class(name="myDsl::shift::expression::complement")
myDsl_equality_expression_linha = Class(name="myDsl::equality::expression::linha")
myDsl_equality_expression_complement = Class(name="myDsl::equality::expression::complement")
myDsl_statement = Class(name="myDsl::statement")
myDsl_labeled_statement = Class(name="myDsl::labeled::statement")
myDsl_expression_statement = Class(name="myDsl::expression::statement")
myDsl_selection_statement = Class(name="myDsl::selection::statement")
myDsl_iteration_statement = Class(name="myDsl::iteration::statement")
myDsl_jump_statement = Class(name="myDsl::jump::statement")
myDsl_and_expression = Class(name="myDsl::and::expression")
myDsl_and_expression_linha = Class(name="myDsl::and::expression::linha")
myDsl_block_item_list = Class(name="myDsl::block::item::list")
myDsl_block_item = Class(name="myDsl::block::item")
myDsl_block_item_list_linha = Class(name="myDsl::block::item::list::linha")
myDsl_logical_or_expression = Class(name="myDsl::logical::or::expression")
myDsl_logical_or_expression_linha = Class(name="myDsl::logical::or::expression::linha")
myDsl_conditional_expression_linha = Class(name="myDsl::conditional::expression::linha")
myDsl_exclusive_or_expression = Class(name="myDsl::exclusive::or::expression")
myDsl_exclusive_or_expression_linha = Class(name="myDsl::exclusive::or::expression::linha")
myDsl_inclusive_or_expression = Class(name="myDsl::inclusive::or::expression")
myDsl_inclusive_or_expression_linha = Class(name="myDsl::inclusive::or::expression::linha")
myDsl_logical_and_expression = Class(name="myDsl::logical::and::expression")
myDsl_logical_and_expression_linha = Class(name="myDsl::logical::and::expression::linha")
myDsl_init_declarator = Class(name="myDsl::init::declarator")
postfix_expression = Class(name="postfix::expression")
myDsl_expression_linha = Class(name="myDsl::expression::linha")
myDsl_DeclarationListLinhaAction = Class(name="myDsl::DeclarationListLinhaAction")
declaration_list_linha = Class(name="declaration::list::linha")
myDsl_TypeQualifierListLinhaAtion = Class(name="myDsl::TypeQualifierListLinhaAtion")
type_qualifier_list_linha = Class(name="type::qualifier::list::linha")
myDsl_DirectAbstractDeclarratorLinhaAction = Class(name="myDsl::DirectAbstractDeclarratorLinhaAction")
direct_abstract_declarator_linha = Class(name="direct::abstract::declarator::linha")
myDsl_string_dsl = Class(name="myDsl::string::dsl")
myDsl_EnumeratorListLinhaAction = Class(name="myDsl::EnumeratorListLinhaAction")
enumerator_list_linha = Class(name="enumerator::list::linha")
myDsl_StructOrUnionSpecifierComplementAction = Class(name="myDsl::StructOrUnionSpecifierComplementAction")
struct_or_union_specifier_complement = Class(name="struct::or::union::specifier::complement")
myDsl_StructDeclarationListLinhaAction = Class(name="myDsl::StructDeclarationListLinhaAction")
struct_declaration_list_linha = Class(name="struct::declaration::list::linha")
myDsl_StructDeclaratorListLinhaAction = Class(name="myDsl::StructDeclaratorListLinhaAction")
struct_declarator_list_linha = Class(name="struct::declarator::list::linha")
myDsl_DesignatorListLinhaAction = Class(name="myDsl::DesignatorListLinhaAction")
designator_list_linha = Class(name="designator::list::linha")
myDsl_PostFixEmpryParams = Class(name="myDsl::PostFixEmpryParams")
postfix_expression_complement = Class(name="postfix::expression::complement")
myDsl_ArgumentExpressionListLinhaAction = Class(name="myDsl::ArgumentExpressionListLinhaAction")
argument_expression_list_linha = Class(name="argument::expression::list::linha")
myDsl_IdentifierListLinhaAction = Class(name="myDsl::IdentifierListLinhaAction")
identifier_list_linha = Class(name="identifier::list::linha")
myDsl_TranlationUnitLinhaAction = Class(name="myDsl::TranlationUnitLinhaAction")
translation_unit_linha = Class(name="translation::unit::linha")
myDsl_GenericAssocListLinhaAction = Class(name="myDsl::GenericAssocListLinhaAction")
generic_assoc_list_linha = Class(name="generic::assoc::list::linha")
myDsl_PostfixExpressionLinhaAction = Class(name="myDsl::PostfixExpressionLinhaAction")
postfix_expression_linha = Class(name="postfix::expression::linha")
myDsl_InitializerListLinhaAction = Class(name="myDsl::InitializerListLinhaAction")
initializer_list_linha = Class(name="initializer::list::linha")
myDsl_PlusPlus = Class(name="myDsl::PlusPlus")
unary_expression = Class(name="unary::expression")
myDsl_InitDecclaratorListLinhaAction = Class(name="myDsl::InitDecclaratorListLinhaAction")
init_declarator_list_linha = Class(name="init::declarator::list::linha")

# myDsl_type_specifier class attributes and methods
myDsl_type_specifier_type_name_str: Property = Property(name="type_name_str", type=StringType)
myDsl_type_specifier.attributes={myDsl_type_specifier_type_name_str}

# myDsl_type_qualifier class attributes and methods
myDsl_type_qualifier_namez: Property = Property(name="namez", type=StringType)
myDsl_type_qualifier.attributes={myDsl_type_qualifier_namez}

# myDsl_alignment_specifier class attributes and methods

# myDsl_type_name class attributes and methods

# myDsl_constant_expression class attributes and methods

# myDsl_Model class attributes and methods

# myDsl_translation_unit class attributes and methods

# myDsl_external_declaration class attributes and methods

# myDsl_translation_unit_linha class attributes and methods

# myDsl_function_definition class attributes and methods

# myDsl_declaration class attributes and methods

# myDsl_declaration_specifiers class attributes and methods
myDsl_declaration_specifiers_function_specifier: Property = Property(name="function_specifier", type=StringType)
myDsl_declaration_specifiers_storage_class_specifier: Property = Property(name="storage_class_specifier", type=StringType)
myDsl_declaration_specifiers.attributes={myDsl_declaration_specifiers_function_specifier, myDsl_declaration_specifiers_storage_class_specifier}

# myDsl_struct_declaration class attributes and methods

# myDsl_struct_declaration_list_linha class attributes and methods

# myDsl_specifier_qualifier_list class attributes and methods

# myDsl_struct_declarator_list class attributes and methods

# myDsl_static_assert_declaration class attributes and methods

# myDsl_struct_declarator class attributes and methods

# myDsl_atomic_type_specifier class attributes and methods

# myDsl_struct_or_union_specifier class attributes and methods
myDsl_struct_or_union_specifier_struct_or_union: Property = Property(name="struct_or_union", type=StringType)
myDsl_struct_or_union_specifier_identifier: Property = Property(name="identifier", type=StringType)
myDsl_struct_or_union_specifier.attributes={myDsl_struct_or_union_specifier_struct_or_union, myDsl_struct_or_union_specifier_identifier}

# myDsl_enum_specifier class attributes and methods
myDsl_enum_specifier_identifier: Property = Property(name="identifier", type=StringType)
myDsl_enum_specifier.attributes={myDsl_enum_specifier_identifier}

# myDsl_enumerator_list class attributes and methods

# myDsl_enumerator class attributes and methods

# myDsl_enumerator_list_linha class attributes and methods

# myDsl_enumeration_constant class attributes and methods
myDsl_enumeration_constant_identifier: Property = Property(name="identifier", type=StringType)
myDsl_enumeration_constant.attributes={myDsl_enumeration_constant_identifier}

# myDsl_struct_declaration_list class attributes and methods

# myDsl_struct_or_union_specifier_complement class attributes and methods

# myDsl_declaration_list_linha class attributes and methods

# myDsl_pointer class attributes and methods

# myDsl_direct_declarator class attributes and methods
myDsl_direct_declarator_identifier: Property = Property(name="identifier", type=StringType)
myDsl_direct_declarator.attributes={myDsl_direct_declarator_identifier}

# myDsl_type_qualifier_list class attributes and methods

# myDsl_struct_declarator_list_linha class attributes and methods

# myDsl_declarator class attributes and methods

# myDsl_init_declarator_list class attributes and methods

# myDsl_declaration_list class attributes and methods

# myDsl_compound_statement class attributes and methods

# myDsl_parameter_declaration class attributes and methods

# myDsl_parameter_list_linha class attributes and methods

# myDsl_abstract_declarator class attributes and methods

# direct_abstract_declarator_complement class attributes and methods

# myDsl_type_qualifier_list_linha class attributes and methods

# myDsl_direct_declarator_linha class attributes and methods

# myDsl_direct_declarator_complemento class attributes and methods

# myDsl_assignment_expression class attributes and methods
myDsl_assignment_expression_assignment_operator: Property = Property(name="assignment_operator", type=StringType)
myDsl_assignment_expression.attributes={myDsl_assignment_expression_assignment_operator}

# myDsl_parameter_type_list class attributes and methods

# myDsl_identifier_list class attributes and methods
myDsl_identifier_list_identifier: Property = Property(name="identifier", type=StringType)
myDsl_identifier_list.attributes={myDsl_identifier_list_identifier}

# myDsl_parameter_lista class attributes and methods

# myDsl_identifier_list_linha class attributes and methods

# myDsl_direct_abstract_declarator class attributes and methods

# myDsl_direct_abstract_declarator_linha class attributes and methods

# myDsl_initializer class attributes and methods

# myDsl_initializer_list class attributes and methods

# myDsl_direct_abstract_declarator_complement class attributes and methods

# myDsl_postfix_expression_linha class attributes and methods

# myDsl_designation class attributes and methods

# myDsl_init_declarator_list_linha class attributes and methods

# myDsl_initializer_list_linha class attributes and methods

# myDsl_initializer_list_complement class attributes and methods

# myDsl_designator_list class attributes and methods

# myDsl_primary_expression class attributes and methods
myDsl_primary_expression_identifier: Property = Property(name="identifier", type=StringType)
myDsl_primary_expression.attributes={myDsl_primary_expression_identifier}

# myDsl_designator class attributes and methods
myDsl_designator_identifier: Property = Property(name="identifier", type=StringType)
myDsl_designator.attributes={myDsl_designator_identifier}

# myDsl_designator_list_linha class attributes and methods

# myDsl_constant class attributes and methods
myDsl_constant_i_constant: Property = Property(name="i_constant", type=IntegerType)
myDsl_constant_f_constant: Property = Property(name="f_constant", type=StringType)
myDsl_constant_char: Property = Property(name="char", type=StringType)
myDsl_constant_string: Property = Property(name="string", type=StringType)
myDsl_constant_enumz: Property = Property(name="enumz", type=StringType)
myDsl_constant.attributes={myDsl_constant_string, myDsl_constant_f_constant, myDsl_constant_char, myDsl_constant_i_constant, myDsl_constant_enumz}

# myDsl_expression class attributes and methods

# myDsl_generic_selection class attributes and methods
myDsl_generic_selection__generic: Property = Property(name="_generic", type=StringType)
myDsl_generic_selection.attributes={myDsl_generic_selection__generic}

# myDsl_generic_assoc_list class attributes and methods

# myDsl_generic_association class attributes and methods
myDsl_generic_association_default: Property = Property(name="default", type=StringType)
myDsl_generic_association.attributes={myDsl_generic_association_default}

# myDsl_generic_assoc_list_linha class attributes and methods

# myDsl_postfix_expression class attributes and methods

# myDsl_cast_expression class attributes and methods

# myDsl_multiplicative_expression class attributes and methods

# myDsl_multiplicative_expression_linha class attributes and methods

# myDsl_multiplicative_expression_complement class attributes and methods
myDsl_multiplicative_expression_complement_multiplica: Property = Property(name="multiplica", type=StringType)
myDsl_multiplicative_expression_complement_divide: Property = Property(name="divide", type=StringType)
myDsl_multiplicative_expression_complement_modulo: Property = Property(name="modulo", type=StringType)
myDsl_multiplicative_expression_complement.attributes={myDsl_multiplicative_expression_complement_modulo, myDsl_multiplicative_expression_complement_divide, myDsl_multiplicative_expression_complement_multiplica}

# myDsl_conditional_expression class attributes and methods

# myDsl_postfix_expression_complement class attributes and methods
myDsl_postfix_expression_complement_identifier: Property = Property(name="identifier", type=StringType)
myDsl_postfix_expression_complement.attributes={myDsl_postfix_expression_complement_identifier}

# myDsl_argument_expression_list class attributes and methods

# myDsl_argument_expression_list_linha class attributes and methods

# myDsl_unary_expression class attributes and methods
myDsl_unary_expression_unary_operator: Property = Property(name="unary_operator", type=StringType)
myDsl_unary_expression.attributes={myDsl_unary_expression_unary_operator}

# myDsl_relational_expression class attributes and methods

# myDsl_relational_expression_linha class attributes and methods

# myDsl_relational_expression_complement class attributes and methods
myDsl_relational_expression_complement_menor: Property = Property(name="menor", type=StringType)
myDsl_relational_expression_complement_maior: Property = Property(name="maior", type=StringType)
myDsl_relational_expression_complement_menor_igual: Property = Property(name="menor_igual", type=StringType)
myDsl_relational_expression_complement_maior_igual: Property = Property(name="maior_igual", type=StringType)
myDsl_relational_expression_complement.attributes={myDsl_relational_expression_complement_maior, myDsl_relational_expression_complement_maior_igual, myDsl_relational_expression_complement_menor_igual, myDsl_relational_expression_complement_menor}

# myDsl_equality_expression class attributes and methods

# myDsl_additive_expression class attributes and methods

# myDsl_additive_expression_linha class attributes and methods

# myDsl_additive_expression_complement class attributes and methods
myDsl_additive_expression_complement_mais: Property = Property(name="mais", type=StringType)
myDsl_additive_expression_complement_menos: Property = Property(name="menos", type=StringType)
myDsl_additive_expression_complement.attributes={myDsl_additive_expression_complement_mais, myDsl_additive_expression_complement_menos}

# myDsl_shift_expression class attributes and methods

# myDsl_shift_expression_linha class attributes and methods

# myDsl_shift_expression_complement class attributes and methods
myDsl_shift_expression_complement_sright: Property = Property(name="sright", type=StringType)
myDsl_shift_expression_complement_sleft: Property = Property(name="sleft", type=StringType)
myDsl_shift_expression_complement.attributes={myDsl_shift_expression_complement_sright, myDsl_shift_expression_complement_sleft}

# myDsl_equality_expression_linha class attributes and methods

# myDsl_equality_expression_complement class attributes and methods
myDsl_equality_expression_complement_igual: Property = Property(name="igual", type=StringType)
myDsl_equality_expression_complement_menor: Property = Property(name="menor", type=StringType)
myDsl_equality_expression_complement_maior: Property = Property(name="maior", type=StringType)
myDsl_equality_expression_complement_menor_igual: Property = Property(name="menor_igual", type=StringType)
myDsl_equality_expression_complement_maior_igual: Property = Property(name="maior_igual", type=StringType)
myDsl_equality_expression_complement_n_igual: Property = Property(name="n_igual", type=StringType)
myDsl_equality_expression_complement.attributes={myDsl_equality_expression_complement_menor, myDsl_equality_expression_complement_menor_igual, myDsl_equality_expression_complement_maior_igual, myDsl_equality_expression_complement_igual, myDsl_equality_expression_complement_n_igual, myDsl_equality_expression_complement_maior}

# myDsl_statement class attributes and methods

# myDsl_labeled_statement class attributes and methods
myDsl_labeled_statement_identifier: Property = Property(name="identifier", type=StringType)
myDsl_labeled_statement.attributes={myDsl_labeled_statement_identifier}

# myDsl_expression_statement class attributes and methods

# myDsl_selection_statement class attributes and methods

# myDsl_iteration_statement class attributes and methods

# myDsl_jump_statement class attributes and methods
myDsl_jump_statement_return_vazio: Property = Property(name="return_vazio", type=StringType)
myDsl_jump_statement_return: Property = Property(name="return", type=StringType)
myDsl_jump_statement_identifier: Property = Property(name="identifier", type=StringType)
myDsl_jump_statement_break: Property = Property(name="break", type=StringType)
myDsl_jump_statement.attributes={myDsl_jump_statement_return, myDsl_jump_statement_break, myDsl_jump_statement_return_vazio, myDsl_jump_statement_identifier}

# myDsl_and_expression class attributes and methods

# myDsl_and_expression_linha class attributes and methods

# myDsl_block_item_list class attributes and methods

# myDsl_block_item class attributes and methods

# myDsl_block_item_list_linha class attributes and methods

# myDsl_logical_or_expression class attributes and methods

# myDsl_logical_or_expression_linha class attributes and methods

# myDsl_conditional_expression_linha class attributes and methods

# myDsl_exclusive_or_expression class attributes and methods

# myDsl_exclusive_or_expression_linha class attributes and methods

# myDsl_inclusive_or_expression class attributes and methods

# myDsl_inclusive_or_expression_linha class attributes and methods

# myDsl_logical_and_expression class attributes and methods

# myDsl_logical_and_expression_linha class attributes and methods

# myDsl_init_declarator class attributes and methods

# postfix_expression class attributes and methods

# myDsl_expression_linha class attributes and methods

# myDsl_DeclarationListLinhaAction class attributes and methods

# declaration_list_linha class attributes and methods

# myDsl_TypeQualifierListLinhaAtion class attributes and methods

# type_qualifier_list_linha class attributes and methods

# myDsl_DirectAbstractDeclarratorLinhaAction class attributes and methods

# direct_abstract_declarator_linha class attributes and methods

# myDsl_string_dsl class attributes and methods
myDsl_string_dsl_string_literal: Property = Property(name="string_literal", type=StringType)
myDsl_string_dsl___func__: Property = Property(name="__func__", type=StringType)
myDsl_string_dsl.attributes={myDsl_string_dsl_string_literal, myDsl_string_dsl___func__}

# myDsl_EnumeratorListLinhaAction class attributes and methods

# enumerator_list_linha class attributes and methods

# myDsl_StructOrUnionSpecifierComplementAction class attributes and methods

# struct_or_union_specifier_complement class attributes and methods

# myDsl_StructDeclarationListLinhaAction class attributes and methods

# struct_declaration_list_linha class attributes and methods

# myDsl_StructDeclaratorListLinhaAction class attributes and methods

# struct_declarator_list_linha class attributes and methods

# myDsl_DesignatorListLinhaAction class attributes and methods

# designator_list_linha class attributes and methods

# myDsl_PostFixEmpryParams class attributes and methods

# postfix_expression_complement class attributes and methods

# myDsl_ArgumentExpressionListLinhaAction class attributes and methods

# argument_expression_list_linha class attributes and methods

# myDsl_IdentifierListLinhaAction class attributes and methods
myDsl_IdentifierListLinhaAction_identifier: Property = Property(name="identifier", type=StringType)
myDsl_IdentifierListLinhaAction.attributes={myDsl_IdentifierListLinhaAction_identifier}

# identifier_list_linha class attributes and methods

# myDsl_TranlationUnitLinhaAction class attributes and methods

# translation_unit_linha class attributes and methods

# myDsl_GenericAssocListLinhaAction class attributes and methods

# generic_assoc_list_linha class attributes and methods

# myDsl_PostfixExpressionLinhaAction class attributes and methods

# postfix_expression_linha class attributes and methods

# myDsl_InitializerListLinhaAction class attributes and methods

# initializer_list_linha class attributes and methods

# myDsl_PlusPlus class attributes and methods
myDsl_PlusPlus_plus: Property = Property(name="plus", type=StringType)
myDsl_PlusPlus.attributes={myDsl_PlusPlus_plus}

# unary_expression class attributes and methods

# myDsl_InitDecclaratorListLinhaAction class attributes and methods

# init_declarator_list_linha class attributes and methods

# Relationships
declaration_specifiers10: BinaryAssociation = BinaryAssociation(
    name="declaration_specifiers10",
    ends={
        Property(name="myDsl_declaration_specifiers", type=myDsl_declaration_specifiers, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declaration_specifiers9", type=myDsl_declaration_specifiers, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type_specifier11: BinaryAssociation = BinaryAssociation(
    name="type_specifier11",
    ends={
        Property(name="myDsl_type_specifier", type=myDsl_declaration_specifiers, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declaration_specifiers12", type=myDsl_type_specifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_qualifier13: BinaryAssociation = BinaryAssociation(
    name="type_qualifier13",
    ends={
        Property(name="myDsl_type_qualifier", type=myDsl_declaration_specifiers, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declaration_specifiers14", type=myDsl_type_qualifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alignment_specifier15: BinaryAssociation = BinaryAssociation(
    name="alignment_specifier15",
    ends={
        Property(name="myDsl_alignment_specifier", type=myDsl_declaration_specifiers, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declaration_specifiers16", type=myDsl_alignment_specifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_name17: BinaryAssociation = BinaryAssociation(
    name="type_name17",
    ends={
        Property(name="myDsl_type_name", type=myDsl_alignment_specifier, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_alignment_specifier18", type=myDsl_type_name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant_expression19: BinaryAssociation = BinaryAssociation(
    name="constant_expression19",
    ends={
        Property(name="myDsl_constant_expression", type=myDsl_alignment_specifier, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_alignment_specifier20", type=myDsl_constant_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
greetings0: BinaryAssociation = BinaryAssociation(
    name="greetings0",
    ends={
        Property(name="myDsl_translation_unit", type=myDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Model", type=myDsl_translation_unit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
external_declaration1: BinaryAssociation = BinaryAssociation(
    name="external_declaration1",
    ends={
        Property(name="myDsl_external_declaration", type=myDsl_translation_unit, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_translation_unit2", type=myDsl_external_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
translation_unit_linha3: BinaryAssociation = BinaryAssociation(
    name="translation_unit_linha3",
    ends={
        Property(name="myDsl_translation_unit_linha", type=myDsl_translation_unit, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_translation_unit4", type=myDsl_translation_unit_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function_definitio5: BinaryAssociation = BinaryAssociation(
    name="function_definitio5",
    ends={
        Property(name="myDsl_function_definition", type=myDsl_external_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_external_declaration6", type=myDsl_function_definition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration7: BinaryAssociation = BinaryAssociation(
    name="declaration7",
    ends={
        Property(name="myDsl_declaration", type=myDsl_external_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_external_declaration8", type=myDsl_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_declaration45: BinaryAssociation = BinaryAssociation(
    name="struct_declaration45",
    ends={
        Property(name="myDsl_struct_declaration", type=myDsl_struct_declaration_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declaration_list46", type=myDsl_struct_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_declaration_list_linha47: BinaryAssociation = BinaryAssociation(
    name="struct_declaration_list_linha47",
    ends={
        Property(name="myDsl_struct_declaration_list_linha", type=myDsl_struct_declaration_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declaration_list48", type=myDsl_struct_declaration_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specifier_qualifier_list49: BinaryAssociation = BinaryAssociation(
    name="specifier_qualifier_list49",
    ends={
        Property(name="myDsl_specifier_qualifier_list", type=myDsl_struct_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declaration50", type=myDsl_specifier_qualifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_declarator_list51: BinaryAssociation = BinaryAssociation(
    name="struct_declarator_list51",
    ends={
        Property(name="myDsl_struct_declarator_list", type=myDsl_struct_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declaration52", type=myDsl_struct_declarator_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
static_assert_declaration53: BinaryAssociation = BinaryAssociation(
    name="static_assert_declaration53",
    ends={
        Property(name="myDsl_static_assert_declaration", type=myDsl_struct_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declaration54", type=myDsl_static_assert_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_declarator55: BinaryAssociation = BinaryAssociation(
    name="struct_declarator55",
    ends={
        Property(name="myDsl_struct_declarator", type=myDsl_struct_declarator_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declarator_list56", type=myDsl_struct_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
atomic_type_specifier21: BinaryAssociation = BinaryAssociation(
    name="atomic_type_specifier21",
    ends={
        Property(name="myDsl_atomic_type_specifier", type=myDsl_type_specifier, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_type_specifier22", type=myDsl_atomic_type_specifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_or_union_specifier23: BinaryAssociation = BinaryAssociation(
    name="struct_or_union_specifier23",
    ends={
        Property(name="myDsl_struct_or_union_specifier", type=myDsl_type_specifier, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_type_specifier24", type=myDsl_struct_or_union_specifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enum_specifier25: BinaryAssociation = BinaryAssociation(
    name="enum_specifier25",
    ends={
        Property(name="myDsl_enum_specifier", type=myDsl_type_specifier, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_type_specifier26", type=myDsl_enum_specifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumerator_list27: BinaryAssociation = BinaryAssociation(
    name="enumerator_list27",
    ends={
        Property(name="myDsl_enumerator_list", type=myDsl_enum_specifier, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_enum_specifier28", type=myDsl_enumerator_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumarator29: BinaryAssociation = BinaryAssociation(
    name="enumarator29",
    ends={
        Property(name="myDsl_enumerator", type=myDsl_enumerator_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_enumerator_list30", type=myDsl_enumerator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumerator_list_linha31: BinaryAssociation = BinaryAssociation(
    name="enumerator_list_linha31",
    ends={
        Property(name="myDsl_enumerator_list_linha", type=myDsl_enumerator_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_enumerator_list32", type=myDsl_enumerator_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumeration_constant33: BinaryAssociation = BinaryAssociation(
    name="enumeration_constant33",
    ends={
        Property(name="myDsl_enumeration_constant", type=myDsl_enumerator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_enumerator34", type=myDsl_enumeration_constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditional_expression35: BinaryAssociation = BinaryAssociation(
    name="conditional_expression35",
    ends={
        Property(name="myDsl_constant_expression37", type=myDsl_enumerator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_enumerator36", type=myDsl_constant_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_name38: BinaryAssociation = BinaryAssociation(
    name="type_name38",
    ends={
        Property(name="myDsl_type_name40", type=myDsl_atomic_type_specifier, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_atomic_type_specifier39", type=myDsl_type_name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_declaration_list41: BinaryAssociation = BinaryAssociation(
    name="struct_declaration_list41",
    ends={
        Property(name="myDsl_struct_declaration_list", type=myDsl_struct_or_union_specifier, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_or_union_specifier42", type=myDsl_struct_declaration_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_or_union_specifier_complement43: BinaryAssociation = BinaryAssociation(
    name="struct_or_union_specifier_complement43",
    ends={
        Property(name="myDsl_struct_or_union_specifier_complement", type=myDsl_struct_or_union_specifier, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_or_union_specifier44", type=myDsl_struct_or_union_specifier_complement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration91: BinaryAssociation = BinaryAssociation(
    name="declaration91",
    ends={
        Property(name="myDsl_declaration_list92", type=myDsl_declaration, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="myDsl_declaration93", type=myDsl_declaration_list, multiplicity=Multiplicity(1, 1))
    }
)
declaration_list_linha94: BinaryAssociation = BinaryAssociation(
    name="declaration_list_linha94",
    ends={
        Property(name="myDsl_declaration_list_linha", type=myDsl_declaration_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declaration_list95", type=myDsl_declaration_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pointer96: BinaryAssociation = BinaryAssociation(
    name="pointer96",
    ends={
        Property(name="myDsl_pointer", type=myDsl_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declarator97", type=myDsl_pointer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
direct_declarator98: BinaryAssociation = BinaryAssociation(
    name="direct_declarator98",
    ends={
        Property(name="myDsl_direct_declarator", type=myDsl_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declarator99", type=myDsl_direct_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_qualifier_list100: BinaryAssociation = BinaryAssociation(
    name="type_qualifier_list100",
    ends={
        Property(name="myDsl_type_qualifier_list", type=myDsl_pointer, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_pointer101", type=myDsl_type_qualifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pointer103: BinaryAssociation = BinaryAssociation(
    name="pointer103",
    ends={
        Property(name="myDsl_pointer104", type=myDsl_pointer, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_pointer102", type=myDsl_pointer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_declarator_list_linha57: BinaryAssociation = BinaryAssociation(
    name="struct_declarator_list_linha57",
    ends={
        Property(name="myDsl_struct_declarator_list_linha", type=myDsl_struct_declarator_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declarator_list58", type=myDsl_struct_declarator_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant_expression59: BinaryAssociation = BinaryAssociation(
    name="constant_expression59",
    ends={
        Property(name="myDsl_constant_expression61", type=myDsl_struct_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declarator60", type=myDsl_constant_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarator62: BinaryAssociation = BinaryAssociation(
    name="declarator62",
    ends={
        Property(name="myDsl_declarator", type=myDsl_struct_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_struct_declarator63", type=myDsl_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_specifier64: BinaryAssociation = BinaryAssociation(
    name="type_specifier64",
    ends={
        Property(name="myDsl_type_specifier66", type=myDsl_specifier_qualifier_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_specifier_qualifier_list65", type=myDsl_type_specifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specifier_qualifier_list68: BinaryAssociation = BinaryAssociation(
    name="specifier_qualifier_list68",
    ends={
        Property(name="myDsl_specifier_qualifier_list69", type=myDsl_specifier_qualifier_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_specifier_qualifier_list67", type=myDsl_specifier_qualifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_qualifier70: BinaryAssociation = BinaryAssociation(
    name="type_qualifier70",
    ends={
        Property(name="myDsl_type_qualifier72", type=myDsl_specifier_qualifier_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_specifier_qualifier_list71", type=myDsl_type_qualifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration_specifiers73: BinaryAssociation = BinaryAssociation(
    name="declaration_specifiers73",
    ends={
        Property(name="myDsl_declaration_specifiers75", type=myDsl_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declaration74", type=myDsl_declaration_specifiers, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
init_declarator_list76: BinaryAssociation = BinaryAssociation(
    name="init_declarator_list76",
    ends={
        Property(name="myDsl_init_declarator_list", type=myDsl_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declaration77", type=myDsl_init_declarator_list, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
static_assert_declaration78: BinaryAssociation = BinaryAssociation(
    name="static_assert_declaration78",
    ends={
        Property(name="myDsl_static_assert_declaration80", type=myDsl_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_declaration79", type=myDsl_static_assert_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration_specifiers81: BinaryAssociation = BinaryAssociation(
    name="declaration_specifiers81",
    ends={
        Property(name="myDsl_declaration_specifiers83", type=myDsl_function_definition, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_function_definition82", type=myDsl_declaration_specifiers, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarator84: BinaryAssociation = BinaryAssociation(
    name="declarator84",
    ends={
        Property(name="myDsl_declarator86", type=myDsl_function_definition, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_function_definition85", type=myDsl_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration_list87: BinaryAssociation = BinaryAssociation(
    name="declaration_list87",
    ends={
        Property(name="myDsl_declaration_list", type=myDsl_function_definition, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_function_definition88", type=myDsl_declaration_list, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compound_statement89: BinaryAssociation = BinaryAssociation(
    name="compound_statement89",
    ends={
        Property(name="myDsl_compound_statement", type=myDsl_function_definition, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_function_definition90", type=myDsl_compound_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter_declarations131: BinaryAssociation = BinaryAssociation(
    name="parameter_declarations131",
    ends={
        Property(name="myDsl_parameter_declaration", type=myDsl_parameter_lista, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_parameter_lista132", type=myDsl_parameter_declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter_declaration133: BinaryAssociation = BinaryAssociation(
    name="parameter_declaration133",
    ends={
        Property(name="myDsl_parameter_declaration134", type=myDsl_parameter_list_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_parameter_list_linha", type=myDsl_parameter_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter_list_linha136: BinaryAssociation = BinaryAssociation(
    name="parameter_list_linha136",
    ends={
        Property(name="myDsl_parameter_list_linha137", type=myDsl_parameter_list_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_parameter_list_linha135", type=myDsl_parameter_list_linha, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaration_specifiers138: BinaryAssociation = BinaryAssociation(
    name="declaration_specifiers138",
    ends={
        Property(name="myDsl_declaration_specifiers140", type=myDsl_parameter_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_parameter_declaration139", type=myDsl_declaration_specifiers, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarator141: BinaryAssociation = BinaryAssociation(
    name="declarator141",
    ends={
        Property(name="myDsl_declarator143", type=myDsl_parameter_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_parameter_declaration142", type=myDsl_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
abstract_declarator144: BinaryAssociation = BinaryAssociation(
    name="abstract_declarator144",
    ends={
        Property(name="myDsl_abstract_declarator", type=myDsl_parameter_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_parameter_declaration145", type=myDsl_abstract_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pointer146: BinaryAssociation = BinaryAssociation(
    name="pointer146",
    ends={
        Property(name="myDsl_pointer148", type=myDsl_abstract_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_abstract_declarator147", type=myDsl_pointer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_qualifier105: BinaryAssociation = BinaryAssociation(
    name="type_qualifier105",
    ends={
        Property(name="myDsl_type_qualifier107", type=myDsl_type_qualifier_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_type_qualifier_list106", type=myDsl_type_qualifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_qualifier_list_linha108: BinaryAssociation = BinaryAssociation(
    name="type_qualifier_list_linha108",
    ends={
        Property(name="myDsl_type_qualifier_list_linha", type=myDsl_type_qualifier_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_type_qualifier_list109", type=myDsl_type_qualifier_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
direct_declarator_linha110: BinaryAssociation = BinaryAssociation(
    name="direct_declarator_linha110",
    ends={
        Property(name="myDsl_direct_declarator_linha", type=myDsl_direct_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_declarator111", type=myDsl_direct_declarator_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarator112: BinaryAssociation = BinaryAssociation(
    name="declarator112",
    ends={
        Property(name="myDsl_declarator114", type=myDsl_direct_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_declarator113", type=myDsl_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
direct_declarator_complemento115: BinaryAssociation = BinaryAssociation(
    name="direct_declarator_complemento115",
    ends={
        Property(name="myDsl_direct_declarator_complemento", type=myDsl_direct_declarator_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_declarator_linha116", type=myDsl_direct_declarator_complemento, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
direct_declarator_linha118: BinaryAssociation = BinaryAssociation(
    name="direct_declarator_linha118",
    ends={
        Property(name="myDsl_direct_declarator_linha119", type=myDsl_direct_declarator_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_declarator_linha117", type=myDsl_direct_declarator_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_qualifier_list120: BinaryAssociation = BinaryAssociation(
    name="type_qualifier_list120",
    ends={
        Property(name="myDsl_type_qualifier_list122", type=myDsl_direct_declarator_complemento, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_declarator_complemento121", type=myDsl_type_qualifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment_expression123: BinaryAssociation = BinaryAssociation(
    name="assignment_expression123",
    ends={
        Property(name="myDsl_assignment_expression", type=myDsl_direct_declarator_complemento, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_declarator_complemento124", type=myDsl_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter_type_list125: BinaryAssociation = BinaryAssociation(
    name="parameter_type_list125",
    ends={
        Property(name="myDsl_parameter_type_list", type=myDsl_direct_declarator_complemento, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_declarator_complemento126", type=myDsl_parameter_type_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier_list127: BinaryAssociation = BinaryAssociation(
    name="identifier_list127",
    ends={
        Property(name="myDsl_identifier_list", type=myDsl_direct_declarator_complemento, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_declarator_complemento128", type=myDsl_identifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter_lista129: BinaryAssociation = BinaryAssociation(
    name="parameter_lista129",
    ends={
        Property(name="myDsl_parameter_lista", type=myDsl_parameter_type_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_parameter_type_list130", type=myDsl_parameter_lista, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier_list_linha177: BinaryAssociation = BinaryAssociation(
    name="identifier_list_linha177",
    ends={
        Property(name="myDsl_identifier_list_linha", type=myDsl_identifier_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_identifier_list178", type=myDsl_identifier_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
direct_abstract_declarator149: BinaryAssociation = BinaryAssociation(
    name="direct_abstract_declarator149",
    ends={
        Property(name="myDsl_direct_abstract_declarator", type=myDsl_abstract_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_abstract_declarator150", type=myDsl_direct_abstract_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
abstract_declarator151: BinaryAssociation = BinaryAssociation(
    name="abstract_declarator151",
    ends={
        Property(name="myDsl_abstract_declarator153", type=myDsl_direct_abstract_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_abstract_declarator152", type=myDsl_abstract_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_qualifier_list154: BinaryAssociation = BinaryAssociation(
    name="type_qualifier_list154",
    ends={
        Property(name="myDsl_type_qualifier_list156", type=myDsl_direct_abstract_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_abstract_declarator155", type=myDsl_type_qualifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment_expression157: BinaryAssociation = BinaryAssociation(
    name="assignment_expression157",
    ends={
        Property(name="myDsl_assignment_expression159", type=myDsl_direct_abstract_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_abstract_declarator158", type=myDsl_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter_type_list160: BinaryAssociation = BinaryAssociation(
    name="parameter_type_list160",
    ends={
        Property(name="myDsl_parameter_type_list162", type=myDsl_direct_abstract_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_abstract_declarator161", type=myDsl_parameter_type_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
direct_abstract_declarator_linha163: BinaryAssociation = BinaryAssociation(
    name="direct_abstract_declarator_linha163",
    ends={
        Property(name="myDsl_direct_abstract_declarator_linha", type=myDsl_direct_abstract_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_abstract_declarator164", type=myDsl_direct_abstract_declarator_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init_declarator_list165: BinaryAssociation = BinaryAssociation(
    name="init_declarator_list165",
    ends={
        Property(name="myDsl_initializer_list", type=myDsl_initializer, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_initializer", type=myDsl_initializer_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment_expression166: BinaryAssociation = BinaryAssociation(
    name="assignment_expression166",
    ends={
        Property(name="myDsl_assignment_expression168", type=myDsl_initializer, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_initializer167", type=myDsl_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment_expression169: BinaryAssociation = BinaryAssociation(
    name="assignment_expression169",
    ends={
        Property(name="myDsl_assignment_expression170", type=myDsl_direct_abstract_declarator_complement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_abstract_declarator_complement", type=myDsl_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_qualifier_list171: BinaryAssociation = BinaryAssociation(
    name="type_qualifier_list171",
    ends={
        Property(name="myDsl_type_qualifier_list173", type=myDsl_direct_abstract_declarator_complement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_abstract_declarator_complement172", type=myDsl_type_qualifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter_type_list174: BinaryAssociation = BinaryAssociation(
    name="parameter_type_list174",
    ends={
        Property(name="myDsl_parameter_type_list176", type=myDsl_direct_abstract_declarator_complement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_direct_abstract_declarator_complement175", type=myDsl_parameter_type_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postfix_expression_linha201: BinaryAssociation = BinaryAssociation(
    name="postfix_expression_linha201",
    ends={
        Property(name="myDsl_postfix_expression_linha", type=myDsl_postfix_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_postfix_expression202", type=myDsl_postfix_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
designation203: BinaryAssociation = BinaryAssociation(
    name="designation203",
    ends={
        Property(name="myDsl_designation", type=myDsl_initializer_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_initializer_list204", type=myDsl_designation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initializer205: BinaryAssociation = BinaryAssociation(
    name="initializer205",
    ends={
        Property(name="myDsl_initializer207", type=myDsl_initializer_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_initializer_list206", type=myDsl_initializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init_declarator_list_linha208: BinaryAssociation = BinaryAssociation(
    name="init_declarator_list_linha208",
    ends={
        Property(name="myDsl_init_declarator_list_linha", type=myDsl_initializer_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_initializer_list209", type=myDsl_init_declarator_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
designation210: BinaryAssociation = BinaryAssociation(
    name="designation210",
    ends={
        Property(name="myDsl_designation211", type=myDsl_initializer_list_complement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_initializer_list_complement", type=myDsl_designation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initializer212: BinaryAssociation = BinaryAssociation(
    name="initializer212",
    ends={
        Property(name="myDsl_initializer214", type=myDsl_initializer_list_complement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_initializer_list_complement213", type=myDsl_initializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
designator_list215: BinaryAssociation = BinaryAssociation(
    name="designator_list215",
    ends={
        Property(name="myDsl_designator_list", type=myDsl_designation, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_designation216", type=myDsl_designator_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
designator217: BinaryAssociation = BinaryAssociation(
    name="designator217",
    ends={
        Property(name="myDsl_designator", type=myDsl_designator_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_designator_list218", type=myDsl_designator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
designator_list_linha219: BinaryAssociation = BinaryAssociation(
    name="designator_list_linha219",
    ends={
        Property(name="myDsl_designator_list_linha", type=myDsl_designator_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_designator_list220", type=myDsl_designator_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant179: BinaryAssociation = BinaryAssociation(
    name="constant179",
    ends={
        Property(name="myDsl_constant", type=myDsl_primary_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_primary_expression", type=myDsl_constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression180: BinaryAssociation = BinaryAssociation(
    name="expression180",
    ends={
        Property(name="myDsl_expression", type=myDsl_primary_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_primary_expression181", type=myDsl_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
generic_selection182: BinaryAssociation = BinaryAssociation(
    name="generic_selection182",
    ends={
        Property(name="myDsl_generic_selection", type=myDsl_primary_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_primary_expression183", type=myDsl_generic_selection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment_expression184: BinaryAssociation = BinaryAssociation(
    name="assignment_expression184",
    ends={
        Property(name="myDsl_assignment_expression186", type=myDsl_generic_selection, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_generic_selection185", type=myDsl_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
generic_assoc_list187: BinaryAssociation = BinaryAssociation(
    name="generic_assoc_list187",
    ends={
        Property(name="myDsl_generic_assoc_list", type=myDsl_generic_selection, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_generic_selection188", type=myDsl_generic_assoc_list, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generic_association189: BinaryAssociation = BinaryAssociation(
    name="generic_association189",
    ends={
        Property(name="myDsl_generic_association", type=myDsl_generic_assoc_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_generic_assoc_list190", type=myDsl_generic_association, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
generic_assoc_list_linha191: BinaryAssociation = BinaryAssociation(
    name="generic_assoc_list_linha191",
    ends={
        Property(name="myDsl_generic_assoc_list_linha", type=myDsl_generic_assoc_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_generic_assoc_list192", type=myDsl_generic_assoc_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_name193: BinaryAssociation = BinaryAssociation(
    name="type_name193",
    ends={
        Property(name="myDsl_type_name195", type=myDsl_generic_association, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_generic_association194", type=myDsl_type_name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment_expression196: BinaryAssociation = BinaryAssociation(
    name="assignment_expression196",
    ends={
        Property(name="myDsl_assignment_expression198", type=myDsl_generic_association, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_generic_association197", type=myDsl_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primary_expression199: BinaryAssociation = BinaryAssociation(
    name="primary_expression199",
    ends={
        Property(name="myDsl_primary_expression200", type=myDsl_postfix_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_postfix_expression", type=myDsl_primary_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cast_expression238: BinaryAssociation = BinaryAssociation(
    name="cast_expression238",
    ends={
        Property(name="myDsl_cast_expression", type=myDsl_unary_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_unary_expression239", type=myDsl_cast_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_name240: BinaryAssociation = BinaryAssociation(
    name="type_name240",
    ends={
        Property(name="myDsl_type_name242", type=myDsl_unary_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_unary_expression241", type=myDsl_type_name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unary_expression243: BinaryAssociation = BinaryAssociation(
    name="unary_expression243",
    ends={
        Property(name="myDsl_unary_expression245", type=myDsl_cast_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_cast_expression244", type=myDsl_unary_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_name246: BinaryAssociation = BinaryAssociation(
    name="type_name246",
    ends={
        Property(name="myDsl_type_name248", type=myDsl_cast_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_cast_expression247", type=myDsl_type_name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cast_expression250: BinaryAssociation = BinaryAssociation(
    name="cast_expression250",
    ends={
        Property(name="myDsl_cast_expression251", type=myDsl_cast_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_cast_expression249", type=myDsl_cast_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cast_expression252: BinaryAssociation = BinaryAssociation(
    name="cast_expression252",
    ends={
        Property(name="myDsl_cast_expression253", type=myDsl_multiplicative_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_multiplicative_expression", type=myDsl_cast_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multiplicative_expression_linha254: BinaryAssociation = BinaryAssociation(
    name="multiplicative_expression_linha254",
    ends={
        Property(name="myDsl_multiplicative_expression_linha", type=myDsl_multiplicative_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_multiplicative_expression255", type=myDsl_multiplicative_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multiplicative_expression_complement256: BinaryAssociation = BinaryAssociation(
    name="multiplicative_expression_complement256",
    ends={
        Property(name="myDsl_multiplicative_expression_complement", type=myDsl_multiplicative_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_multiplicative_expression_linha257", type=myDsl_multiplicative_expression_complement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant_expression221: BinaryAssociation = BinaryAssociation(
    name="constant_expression221",
    ends={
        Property(name="myDsl_conditional_expression", type=myDsl_designator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_designator222", type=myDsl_conditional_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant_expression223: BinaryAssociation = BinaryAssociation(
    name="constant_expression223",
    ends={
        Property(name="myDsl_constant_expression225", type=myDsl_static_assert_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_static_assert_declaration224", type=myDsl_constant_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression226: BinaryAssociation = BinaryAssociation(
    name="expression226",
    ends={
        Property(name="myDsl_expression227", type=myDsl_postfix_expression_complement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_postfix_expression_complement", type=myDsl_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argument_expression_list228: BinaryAssociation = BinaryAssociation(
    name="argument_expression_list228",
    ends={
        Property(name="myDsl_argument_expression_list", type=myDsl_postfix_expression_complement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_postfix_expression_complement229", type=myDsl_argument_expression_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment_expressions230: BinaryAssociation = BinaryAssociation(
    name="assignment_expressions230",
    ends={
        Property(name="myDsl_assignment_expression232", type=myDsl_argument_expression_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_argument_expression_list231", type=myDsl_assignment_expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postfix_expression233: BinaryAssociation = BinaryAssociation(
    name="postfix_expression233",
    ends={
        Property(name="myDsl_postfix_expression234", type=myDsl_unary_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_unary_expression", type=myDsl_postfix_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shift_expression288: BinaryAssociation = BinaryAssociation(
    name="shift_expression288",
    ends={
        Property(name="myDsl_shift_expression289", type=myDsl_relational_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_relational_expression", type=myDsl_shift_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unary_expression236: BinaryAssociation = BinaryAssociation(
    name="unary_expression236",
    ends={
        Property(name="myDsl_unary_expression237", type=myDsl_unary_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_unary_expression235", type=myDsl_unary_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relational_expression_linha290: BinaryAssociation = BinaryAssociation(
    name="relational_expression_linha290",
    ends={
        Property(name="myDsl_relational_expression_linha", type=myDsl_relational_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_relational_expression291", type=myDsl_relational_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shift_expression_complement292: BinaryAssociation = BinaryAssociation(
    name="shift_expression_complement292",
    ends={
        Property(name="myDsl_shift_expression_complement294", type=myDsl_relational_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_relational_expression_linha293", type=myDsl_shift_expression_complement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relational_expression_linha296: BinaryAssociation = BinaryAssociation(
    name="relational_expression_linha296",
    ends={
        Property(name="myDsl_relational_expression_linha297", type=myDsl_relational_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_relational_expression_linha295", type=myDsl_relational_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shift_expression298: BinaryAssociation = BinaryAssociation(
    name="shift_expression298",
    ends={
        Property(name="myDsl_shift_expression299", type=myDsl_relational_expression_complement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_relational_expression_complement", type=myDsl_shift_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relational_expression300: BinaryAssociation = BinaryAssociation(
    name="relational_expression300",
    ends={
        Property(name="myDsl_relational_expression301", type=myDsl_equality_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_equality_expression", type=myDsl_relational_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multiplicative_expression_linha259: BinaryAssociation = BinaryAssociation(
    name="multiplicative_expression_linha259",
    ends={
        Property(name="myDsl_multiplicative_expression_linha260", type=myDsl_multiplicative_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_multiplicative_expression_linha258", type=myDsl_multiplicative_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cast_expression261: BinaryAssociation = BinaryAssociation(
    name="cast_expression261",
    ends={
        Property(name="myDsl_cast_expression263", type=myDsl_multiplicative_expression_complement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_multiplicative_expression_complement262", type=myDsl_cast_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multiplicative_expression264: BinaryAssociation = BinaryAssociation(
    name="multiplicative_expression264",
    ends={
        Property(name="myDsl_multiplicative_expression265", type=myDsl_additive_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_additive_expression", type=myDsl_multiplicative_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
additive_expression_linha266: BinaryAssociation = BinaryAssociation(
    name="additive_expression_linha266",
    ends={
        Property(name="myDsl_additive_expression_linha", type=myDsl_additive_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_additive_expression267", type=myDsl_additive_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
additive_expression_complement268: BinaryAssociation = BinaryAssociation(
    name="additive_expression_complement268",
    ends={
        Property(name="myDsl_additive_expression_complement", type=myDsl_additive_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_additive_expression_linha269", type=myDsl_additive_expression_complement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
additive_expression_linha271: BinaryAssociation = BinaryAssociation(
    name="additive_expression_linha271",
    ends={
        Property(name="myDsl_additive_expression_linha272", type=myDsl_additive_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_additive_expression_linha270", type=myDsl_additive_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multiplicative_expression273: BinaryAssociation = BinaryAssociation(
    name="multiplicative_expression273",
    ends={
        Property(name="myDsl_multiplicative_expression275", type=myDsl_additive_expression_complement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_additive_expression_complement274", type=myDsl_multiplicative_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
additive_expression276: BinaryAssociation = BinaryAssociation(
    name="additive_expression276",
    ends={
        Property(name="myDsl_additive_expression277", type=myDsl_shift_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_shift_expression", type=myDsl_additive_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shift_expression_linha278: BinaryAssociation = BinaryAssociation(
    name="shift_expression_linha278",
    ends={
        Property(name="myDsl_shift_expression_linha", type=myDsl_shift_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_shift_expression279", type=myDsl_shift_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shift_expression_complement280: BinaryAssociation = BinaryAssociation(
    name="shift_expression_complement280",
    ends={
        Property(name="myDsl_shift_expression_complement", type=myDsl_shift_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_shift_expression_linha281", type=myDsl_shift_expression_complement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shift_expression_linha283: BinaryAssociation = BinaryAssociation(
    name="shift_expression_linha283",
    ends={
        Property(name="myDsl_shift_expression_linha284", type=myDsl_shift_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_shift_expression_linha282", type=myDsl_shift_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
additive_expression285: BinaryAssociation = BinaryAssociation(
    name="additive_expression285",
    ends={
        Property(name="myDsl_additive_expression287", type=myDsl_shift_expression_complement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_shift_expression_complement286", type=myDsl_additive_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression324: BinaryAssociation = BinaryAssociation(
    name="expression324",
    ends={
        Property(name="myDsl_expression326", type=myDsl_jump_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_jump_statement325", type=myDsl_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression327: BinaryAssociation = BinaryAssociation(
    name="expression327",
    ends={
        Property(name="myDsl_expression329", type=myDsl_iteration_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_iteration_statement328", type=myDsl_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement330: BinaryAssociation = BinaryAssociation(
    name="statement330",
    ends={
        Property(name="myDsl_statement332", type=myDsl_iteration_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_iteration_statement331", type=myDsl_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression_statement333: BinaryAssociation = BinaryAssociation(
    name="expression_statement333",
    ends={
        Property(name="myDsl_expression_statement335", type=myDsl_iteration_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_iteration_statement334", type=myDsl_expression_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression_statement2336: BinaryAssociation = BinaryAssociation(
    name="expression_statement2336",
    ends={
        Property(name="myDsl_expression_statement338", type=myDsl_iteration_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_iteration_statement337", type=myDsl_expression_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration339: BinaryAssociation = BinaryAssociation(
    name="declaration339",
    ends={
        Property(name="myDsl_declaration341", type=myDsl_iteration_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_iteration_statement340", type=myDsl_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
equality_expression_linha302: BinaryAssociation = BinaryAssociation(
    name="equality_expression_linha302",
    ends={
        Property(name="myDsl_equality_expression_linha", type=myDsl_equality_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_equality_expression303", type=myDsl_equality_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
equality_expression_complement304: BinaryAssociation = BinaryAssociation(
    name="equality_expression_complement304",
    ends={
        Property(name="myDsl_equality_expression_complement", type=myDsl_equality_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_equality_expression_linha305", type=myDsl_equality_expression_complement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
equality_expression_linha307: BinaryAssociation = BinaryAssociation(
    name="equality_expression_linha307",
    ends={
        Property(name="myDsl_equality_expression_linha308", type=myDsl_equality_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_equality_expression_linha306", type=myDsl_equality_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relational_expression309: BinaryAssociation = BinaryAssociation(
    name="relational_expression309",
    ends={
        Property(name="myDsl_relational_expression311", type=myDsl_equality_expression_complement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_equality_expression_complement310", type=myDsl_relational_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labeled_statement312: BinaryAssociation = BinaryAssociation(
    name="labeled_statement312",
    ends={
        Property(name="myDsl_labeled_statement", type=myDsl_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_statement", type=myDsl_labeled_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
compound_statement313: BinaryAssociation = BinaryAssociation(
    name="compound_statement313",
    ends={
        Property(name="myDsl_compound_statement315", type=myDsl_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_statement314", type=myDsl_compound_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression_statement316: BinaryAssociation = BinaryAssociation(
    name="expression_statement316",
    ends={
        Property(name="myDsl_expression_statement", type=myDsl_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_statement317", type=myDsl_expression_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selection_statement318: BinaryAssociation = BinaryAssociation(
    name="selection_statement318",
    ends={
        Property(name="myDsl_selection_statement", type=myDsl_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_statement319", type=myDsl_selection_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iteration_statement320: BinaryAssociation = BinaryAssociation(
    name="iteration_statement320",
    ends={
        Property(name="myDsl_iteration_statement", type=myDsl_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_statement321", type=myDsl_iteration_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
jump_statement322: BinaryAssociation = BinaryAssociation(
    name="jump_statement322",
    ends={
        Property(name="myDsl_jump_statement", type=myDsl_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_statement323", type=myDsl_jump_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement372: BinaryAssociation = BinaryAssociation(
    name="statement372",
    ends={
        Property(name="myDsl_statement374", type=myDsl_block_item, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_block_item373", type=myDsl_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression375: BinaryAssociation = BinaryAssociation(
    name="expression375",
    ends={
        Property(name="myDsl_expression377", type=myDsl_expression_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_expression_statement376", type=myDsl_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
equality_expression378: BinaryAssociation = BinaryAssociation(
    name="equality_expression378",
    ends={
        Property(name="myDsl_equality_expression379", type=myDsl_and_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_and_expression", type=myDsl_equality_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
and_expression_linha380: BinaryAssociation = BinaryAssociation(
    name="and_expression_linha380",
    ends={
        Property(name="myDsl_and_expression_linha", type=myDsl_and_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_and_expression381", type=myDsl_and_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
equality_expression382: BinaryAssociation = BinaryAssociation(
    name="equality_expression382",
    ends={
        Property(name="myDsl_equality_expression384", type=myDsl_and_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_and_expression_linha383", type=myDsl_equality_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
and_expression_linha386: BinaryAssociation = BinaryAssociation(
    name="and_expression_linha386",
    ends={
        Property(name="myDsl_and_expression_linha387", type=myDsl_and_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_and_expression_linha385", type=myDsl_and_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression342: BinaryAssociation = BinaryAssociation(
    name="expression342",
    ends={
        Property(name="myDsl_expression344", type=myDsl_selection_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_selection_statement343", type=myDsl_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement345: BinaryAssociation = BinaryAssociation(
    name="statement345",
    ends={
        Property(name="myDsl_statement347", type=myDsl_selection_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_selection_statement346", type=myDsl_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement2348: BinaryAssociation = BinaryAssociation(
    name="statement2348",
    ends={
        Property(name="myDsl_statement350", type=myDsl_selection_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_selection_statement349", type=myDsl_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement351: BinaryAssociation = BinaryAssociation(
    name="statement351",
    ends={
        Property(name="myDsl_statement353", type=myDsl_labeled_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_labeled_statement352", type=myDsl_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditional_expression354: BinaryAssociation = BinaryAssociation(
    name="conditional_expression354",
    ends={
        Property(name="myDsl_conditional_expression356", type=myDsl_labeled_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_labeled_statement355", type=myDsl_conditional_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block_item_list357: BinaryAssociation = BinaryAssociation(
    name="block_item_list357",
    ends={
        Property(name="myDsl_block_item_list", type=myDsl_compound_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_compound_statement358", type=myDsl_block_item_list, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block_item359: BinaryAssociation = BinaryAssociation(
    name="block_item359",
    ends={
        Property(name="myDsl_block_item", type=myDsl_block_item_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_block_item_list360", type=myDsl_block_item, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block_item_list_linha361: BinaryAssociation = BinaryAssociation(
    name="block_item_list_linha361",
    ends={
        Property(name="myDsl_block_item_list_linha", type=myDsl_block_item_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_block_item_list362", type=myDsl_block_item_list_linha, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block_item363: BinaryAssociation = BinaryAssociation(
    name="block_item363",
    ends={
        Property(name="myDsl_block_item365", type=myDsl_block_item_list_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_block_item_list_linha364", type=myDsl_block_item, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block_item_list_linha367: BinaryAssociation = BinaryAssociation(
    name="block_item_list_linha367",
    ends={
        Property(name="myDsl_block_item_list_linha368", type=myDsl_block_item_list_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_block_item_list_linha366", type=myDsl_block_item_list_linha, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaration369: BinaryAssociation = BinaryAssociation(
    name="declaration369",
    ends={
        Property(name="myDsl_declaration371", type=myDsl_block_item, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_block_item370", type=myDsl_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
logical_and_expression418: BinaryAssociation = BinaryAssociation(
    name="logical_and_expression418",
    ends={
        Property(name="myDsl_logical_and_expression419", type=myDsl_logical_or_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_logical_or_expression", type=myDsl_logical_and_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
logical_or_expression_linha420: BinaryAssociation = BinaryAssociation(
    name="logical_or_expression_linha420",
    ends={
        Property(name="myDsl_logical_or_expression_linha", type=myDsl_logical_or_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_logical_or_expression421", type=myDsl_logical_or_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
logical_and_expression422: BinaryAssociation = BinaryAssociation(
    name="logical_and_expression422",
    ends={
        Property(name="myDsl_logical_and_expression424", type=myDsl_logical_or_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_logical_or_expression_linha423", type=myDsl_logical_and_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
logical_or_expression_linha426: BinaryAssociation = BinaryAssociation(
    name="logical_or_expression_linha426",
    ends={
        Property(name="myDsl_logical_or_expression_linha427", type=myDsl_logical_or_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_logical_or_expression_linha425", type=myDsl_logical_or_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
logical_or_expression428: BinaryAssociation = BinaryAssociation(
    name="logical_or_expression428",
    ends={
        Property(name="myDsl_logical_or_expression430", type=myDsl_conditional_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_conditional_expression429", type=myDsl_logical_or_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditional_expression_linha431: BinaryAssociation = BinaryAssociation(
    name="conditional_expression_linha431",
    ends={
        Property(name="myDsl_conditional_expression_linha", type=myDsl_conditional_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_conditional_expression432", type=myDsl_conditional_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
and_expression388: BinaryAssociation = BinaryAssociation(
    name="and_expression388",
    ends={
        Property(name="myDsl_and_expression389", type=myDsl_exclusive_or_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_exclusive_or_expression", type=myDsl_and_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exclusive_or_expression_linha390: BinaryAssociation = BinaryAssociation(
    name="exclusive_or_expression_linha390",
    ends={
        Property(name="myDsl_exclusive_or_expression_linha", type=myDsl_exclusive_or_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_exclusive_or_expression391", type=myDsl_exclusive_or_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
and_expression392: BinaryAssociation = BinaryAssociation(
    name="and_expression392",
    ends={
        Property(name="myDsl_and_expression394", type=myDsl_exclusive_or_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_exclusive_or_expression_linha393", type=myDsl_and_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exclusive_or_expression_linha396: BinaryAssociation = BinaryAssociation(
    name="exclusive_or_expression_linha396",
    ends={
        Property(name="myDsl_exclusive_or_expression_linha397", type=myDsl_exclusive_or_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_exclusive_or_expression_linha395", type=myDsl_exclusive_or_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exclusive_or_expression398: BinaryAssociation = BinaryAssociation(
    name="exclusive_or_expression398",
    ends={
        Property(name="myDsl_exclusive_or_expression399", type=myDsl_inclusive_or_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_inclusive_or_expression", type=myDsl_exclusive_or_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inclusive_or_expression_linha400: BinaryAssociation = BinaryAssociation(
    name="inclusive_or_expression_linha400",
    ends={
        Property(name="myDsl_inclusive_or_expression_linha", type=myDsl_inclusive_or_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_inclusive_or_expression401", type=myDsl_inclusive_or_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exclusive_or_expression402: BinaryAssociation = BinaryAssociation(
    name="exclusive_or_expression402",
    ends={
        Property(name="myDsl_exclusive_or_expression404", type=myDsl_inclusive_or_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_inclusive_or_expression_linha403", type=myDsl_exclusive_or_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inclusive_or_expression_linha406: BinaryAssociation = BinaryAssociation(
    name="inclusive_or_expression_linha406",
    ends={
        Property(name="myDsl_inclusive_or_expression_linha407", type=myDsl_inclusive_or_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_inclusive_or_expression_linha405", type=myDsl_inclusive_or_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inclusive_or_expression408: BinaryAssociation = BinaryAssociation(
    name="inclusive_or_expression408",
    ends={
        Property(name="myDsl_inclusive_or_expression409", type=myDsl_logical_and_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_logical_and_expression", type=myDsl_inclusive_or_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
logical_and_expression_linha410: BinaryAssociation = BinaryAssociation(
    name="logical_and_expression_linha410",
    ends={
        Property(name="myDsl_logical_and_expression_linha", type=myDsl_logical_and_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_logical_and_expression411", type=myDsl_logical_and_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inclusive_or_expression412: BinaryAssociation = BinaryAssociation(
    name="inclusive_or_expression412",
    ends={
        Property(name="myDsl_inclusive_or_expression414", type=myDsl_logical_and_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_logical_and_expression_linha413", type=myDsl_inclusive_or_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
logical_and_expression_linha416: BinaryAssociation = BinaryAssociation(
    name="logical_and_expression_linha416",
    ends={
        Property(name="myDsl_logical_and_expression_linha417", type=myDsl_logical_and_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_logical_and_expression_linha415", type=myDsl_logical_and_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment_expression465: BinaryAssociation = BinaryAssociation(
    name="assignment_expression465",
    ends={
        Property(name="myDsl_assignment_expression467", type=myDsl_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_expression_linha466", type=myDsl_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression_linha469: BinaryAssociation = BinaryAssociation(
    name="expression_linha469",
    ends={
        Property(name="myDsl_expression_linha470", type=myDsl_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_expression_linha468", type=myDsl_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditional_expression471: BinaryAssociation = BinaryAssociation(
    name="conditional_expression471",
    ends={
        Property(name="myDsl_conditional_expression473", type=myDsl_constant_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_constant_expression472", type=myDsl_conditional_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init_declarator474: BinaryAssociation = BinaryAssociation(
    name="init_declarator474",
    ends={
        Property(name="myDsl_init_declarator", type=myDsl_init_declarator_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_init_declarator_list475", type=myDsl_init_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init_declarator_list_linha476: BinaryAssociation = BinaryAssociation(
    name="init_declarator_list_linha476",
    ends={
        Property(name="myDsl_init_declarator_list_linha478", type=myDsl_init_declarator_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_init_declarator_list477", type=myDsl_init_declarator_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarator479: BinaryAssociation = BinaryAssociation(
    name="declarator479",
    ends={
        Property(name="myDsl_declarator481", type=myDsl_init_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_init_declarator480", type=myDsl_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression433: BinaryAssociation = BinaryAssociation(
    name="expression433",
    ends={
        Property(name="myDsl_expression435", type=myDsl_conditional_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_conditional_expression_linha434", type=myDsl_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditional_expression436: BinaryAssociation = BinaryAssociation(
    name="conditional_expression436",
    ends={
        Property(name="myDsl_conditional_expression438", type=myDsl_conditional_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_conditional_expression_linha437", type=myDsl_conditional_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditional_expression_linha440: BinaryAssociation = BinaryAssociation(
    name="conditional_expression_linha440",
    ends={
        Property(name="myDsl_conditional_expression_linha441", type=myDsl_conditional_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_conditional_expression_linha439", type=myDsl_conditional_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditional_expression442: BinaryAssociation = BinaryAssociation(
    name="conditional_expression442",
    ends={
        Property(name="myDsl_conditional_expression444", type=myDsl_assignment_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_assignment_expression443", type=myDsl_conditional_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unary_expression445: BinaryAssociation = BinaryAssociation(
    name="unary_expression445",
    ends={
        Property(name="myDsl_unary_expression447", type=myDsl_assignment_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_assignment_expression446", type=myDsl_unary_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment_expression449: BinaryAssociation = BinaryAssociation(
    name="assignment_expression449",
    ends={
        Property(name="myDsl_assignment_expression450", type=myDsl_assignment_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_assignment_expression448", type=myDsl_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initializer_list451: BinaryAssociation = BinaryAssociation(
    name="initializer_list451",
    ends={
        Property(name="myDsl_initializer_list453", type=myDsl_type_name, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_type_name452", type=myDsl_initializer_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specifier_qualifier_list454: BinaryAssociation = BinaryAssociation(
    name="specifier_qualifier_list454",
    ends={
        Property(name="myDsl_specifier_qualifier_list456", type=myDsl_type_name, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_type_name455", type=myDsl_specifier_qualifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
abstract_declarator457: BinaryAssociation = BinaryAssociation(
    name="abstract_declarator457",
    ends={
        Property(name="myDsl_abstract_declarator459", type=myDsl_type_name, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_type_name458", type=myDsl_abstract_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment_expression460: BinaryAssociation = BinaryAssociation(
    name="assignment_expression460",
    ends={
        Property(name="myDsl_assignment_expression462", type=myDsl_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_expression461", type=myDsl_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression_linha463: BinaryAssociation = BinaryAssociation(
    name="expression_linha463",
    ends={
        Property(name="myDsl_expression_linha", type=myDsl_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_expression464", type=myDsl_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration502: BinaryAssociation = BinaryAssociation(
    name="declaration502",
    ends={
        Property(name="myDsl_declaration503", type=myDsl_DeclarationListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_DeclarationListLinhaAction", type=myDsl_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration_list_linha504: BinaryAssociation = BinaryAssociation(
    name="declaration_list_linha504",
    ends={
        Property(name="myDsl_declaration_list_linha506", type=myDsl_DeclarationListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_DeclarationListLinhaAction505", type=myDsl_declaration_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_qualifier507: BinaryAssociation = BinaryAssociation(
    name="type_qualifier507",
    ends={
        Property(name="myDsl_type_qualifier508", type=myDsl_TypeQualifierListLinhaAtion, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_TypeQualifierListLinhaAtion", type=myDsl_type_qualifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_qualifier_list_linha509: BinaryAssociation = BinaryAssociation(
    name="type_qualifier_list_linha509",
    ends={
        Property(name="myDsl_type_qualifier_list_linha511", type=myDsl_TypeQualifierListLinhaAtion, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_TypeQualifierListLinhaAtion510", type=myDsl_type_qualifier_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initializer482: BinaryAssociation = BinaryAssociation(
    name="initializer482",
    ends={
        Property(name="myDsl_initializer484", type=myDsl_init_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_init_declarator483", type=myDsl_initializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumerator485: BinaryAssociation = BinaryAssociation(
    name="enumerator485",
    ends={
        Property(name="myDsl_enumerator486", type=myDsl_EnumeratorListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_EnumeratorListLinhaAction", type=myDsl_enumerator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumerator_list_linha487: BinaryAssociation = BinaryAssociation(
    name="enumerator_list_linha487",
    ends={
        Property(name="myDsl_enumerator_list_linha489", type=myDsl_EnumeratorListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_EnumeratorListLinhaAction488", type=myDsl_enumerator_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_declaration_list490: BinaryAssociation = BinaryAssociation(
    name="struct_declaration_list490",
    ends={
        Property(name="myDsl_struct_declaration_list491", type=myDsl_StructOrUnionSpecifierComplementAction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_StructOrUnionSpecifierComplementAction", type=myDsl_struct_declaration_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_declaration492: BinaryAssociation = BinaryAssociation(
    name="struct_declaration492",
    ends={
        Property(name="myDsl_struct_declaration493", type=myDsl_StructDeclarationListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_StructDeclarationListLinhaAction", type=myDsl_struct_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_declaration_list_linha494: BinaryAssociation = BinaryAssociation(
    name="struct_declaration_list_linha494",
    ends={
        Property(name="myDsl_struct_declaration_list_linha496", type=myDsl_StructDeclarationListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_StructDeclarationListLinhaAction495", type=myDsl_struct_declaration_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_declarator497: BinaryAssociation = BinaryAssociation(
    name="struct_declarator497",
    ends={
        Property(name="myDsl_struct_declarator498", type=myDsl_StructDeclaratorListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_StructDeclaratorListLinhaAction", type=myDsl_struct_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_declarator_list_linha499: BinaryAssociation = BinaryAssociation(
    name="struct_declarator_list_linha499",
    ends={
        Property(name="myDsl_struct_declarator_list_linha501", type=myDsl_StructDeclaratorListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_StructDeclaratorListLinhaAction500", type=myDsl_struct_declarator_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init_declarator_list_linha536: BinaryAssociation = BinaryAssociation(
    name="init_declarator_list_linha536",
    ends={
        Property(name="myDsl_init_declarator_list_linha538", type=myDsl_InitializerListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_InitializerListLinhaAction537", type=myDsl_init_declarator_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
designator539: BinaryAssociation = BinaryAssociation(
    name="designator539",
    ends={
        Property(name="myDsl_designator540", type=myDsl_DesignatorListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_DesignatorListLinhaAction", type=myDsl_designator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
designator_list_linha541: BinaryAssociation = BinaryAssociation(
    name="designator_list_linha541",
    ends={
        Property(name="myDsl_declaration_list_linha543", type=myDsl_DesignatorListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_DesignatorListLinhaAction542", type=myDsl_declaration_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment_expression544: BinaryAssociation = BinaryAssociation(
    name="assignment_expression544",
    ends={
        Property(name="myDsl_assignment_expression545", type=myDsl_ArgumentExpressionListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ArgumentExpressionListLinhaAction", type=myDsl_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argument_expression_list_linha546: BinaryAssociation = BinaryAssociation(
    name="argument_expression_list_linha546",
    ends={
        Property(name="myDsl_argument_expression_list_linha", type=myDsl_ArgumentExpressionListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ArgumentExpressionListLinhaAction547", type=myDsl_argument_expression_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
direct_abstract_declarator_complement512: BinaryAssociation = BinaryAssociation(
    name="direct_abstract_declarator_complement512",
    ends={
        Property(name="myDsl_direct_abstract_declarator_complement513", type=myDsl_DirectAbstractDeclarratorLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_DirectAbstractDeclarratorLinhaAction", type=myDsl_direct_abstract_declarator_complement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
direct_abstract_declarator_linha514: BinaryAssociation = BinaryAssociation(
    name="direct_abstract_declarator_linha514",
    ends={
        Property(name="myDsl_direct_abstract_declarator_linha516", type=myDsl_DirectAbstractDeclarratorLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_DirectAbstractDeclarratorLinhaAction515", type=myDsl_direct_abstract_declarator_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier_list_linha517: BinaryAssociation = BinaryAssociation(
    name="identifier_list_linha517",
    ends={
        Property(name="myDsl_identifier_list_linha518", type=myDsl_IdentifierListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_IdentifierListLinhaAction", type=myDsl_identifier_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
external_declaration519: BinaryAssociation = BinaryAssociation(
    name="external_declaration519",
    ends={
        Property(name="myDsl_external_declaration520", type=myDsl_TranlationUnitLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_TranlationUnitLinhaAction", type=myDsl_external_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
translation_unit_linha521: BinaryAssociation = BinaryAssociation(
    name="translation_unit_linha521",
    ends={
        Property(name="myDsl_translation_unit_linha523", type=myDsl_TranlationUnitLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_TranlationUnitLinhaAction522", type=myDsl_translation_unit_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
generic_association524: BinaryAssociation = BinaryAssociation(
    name="generic_association524",
    ends={
        Property(name="myDsl_generic_association525", type=myDsl_GenericAssocListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_GenericAssocListLinhaAction", type=myDsl_generic_association, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
generic_assoc_list_linha526: BinaryAssociation = BinaryAssociation(
    name="generic_assoc_list_linha526",
    ends={
        Property(name="myDsl_generic_assoc_list_linha528", type=myDsl_GenericAssocListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_GenericAssocListLinhaAction527", type=myDsl_generic_assoc_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postfix_expression_complement529: BinaryAssociation = BinaryAssociation(
    name="postfix_expression_complement529",
    ends={
        Property(name="myDsl_postfix_expression_complement530", type=myDsl_PostfixExpressionLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_PostfixExpressionLinhaAction", type=myDsl_postfix_expression_complement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postfix_expression_linha531: BinaryAssociation = BinaryAssociation(
    name="postfix_expression_linha531",
    ends={
        Property(name="myDsl_postfix_expression_linha533", type=myDsl_PostfixExpressionLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_PostfixExpressionLinhaAction532", type=myDsl_postfix_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initializer_list_complement534: BinaryAssociation = BinaryAssociation(
    name="initializer_list_complement534",
    ends={
        Property(name="myDsl_initializer_list_complement535", type=myDsl_InitializerListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_InitializerListLinhaAction", type=myDsl_initializer_list_complement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init_declarator548: BinaryAssociation = BinaryAssociation(
    name="init_declarator548",
    ends={
        Property(name="myDsl_init_declarator549", type=myDsl_InitDecclaratorListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_InitDecclaratorListLinhaAction", type=myDsl_init_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init_declarator_list_linha550: BinaryAssociation = BinaryAssociation(
    name="init_declarator_list_linha550",
    ends={
        Property(name="myDsl_init_declarator_list_linha552", type=myDsl_InitDecclaratorListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_InitDecclaratorListLinhaAction551", type=myDsl_init_declarator_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_myDsl_type_qualifier_list_direct_abstract_declarator_complement = Generalization(general=direct_abstract_declarator_complement, specific=myDsl_type_qualifier_list)
gen_myDsl_type_name_postfix_expression = Generalization(general=postfix_expression, specific=myDsl_type_name)
gen_myDsl_DeclarationListLinhaAction_declaration_list_linha = Generalization(general=declaration_list_linha, specific=myDsl_DeclarationListLinhaAction)
gen_myDsl_TypeQualifierListLinhaAtion_type_qualifier_list_linha = Generalization(general=type_qualifier_list_linha, specific=myDsl_TypeQualifierListLinhaAtion)
gen_myDsl_DirectAbstractDeclarratorLinhaAction_direct_abstract_declarator_linha = Generalization(general=direct_abstract_declarator_linha, specific=myDsl_DirectAbstractDeclarratorLinhaAction)
gen_myDsl_EnumeratorListLinhaAction_enumerator_list_linha = Generalization(general=enumerator_list_linha, specific=myDsl_EnumeratorListLinhaAction)
gen_myDsl_StructOrUnionSpecifierComplementAction_struct_or_union_specifier_complement = Generalization(general=struct_or_union_specifier_complement, specific=myDsl_StructOrUnionSpecifierComplementAction)
gen_myDsl_StructDeclarationListLinhaAction_struct_declaration_list_linha = Generalization(general=struct_declaration_list_linha, specific=myDsl_StructDeclarationListLinhaAction)
gen_myDsl_StructDeclaratorListLinhaAction_struct_declarator_list_linha = Generalization(general=struct_declarator_list_linha, specific=myDsl_StructDeclaratorListLinhaAction)
gen_myDsl_DesignatorListLinhaAction_designator_list_linha = Generalization(general=designator_list_linha, specific=myDsl_DesignatorListLinhaAction)
gen_myDsl_PostFixEmpryParams_postfix_expression_complement = Generalization(general=postfix_expression_complement, specific=myDsl_PostFixEmpryParams)
gen_myDsl_ArgumentExpressionListLinhaAction_argument_expression_list_linha = Generalization(general=argument_expression_list_linha, specific=myDsl_ArgumentExpressionListLinhaAction)
gen_myDsl_IdentifierListLinhaAction_identifier_list_linha = Generalization(general=identifier_list_linha, specific=myDsl_IdentifierListLinhaAction)
gen_myDsl_TranlationUnitLinhaAction_translation_unit_linha = Generalization(general=translation_unit_linha, specific=myDsl_TranlationUnitLinhaAction)
gen_myDsl_GenericAssocListLinhaAction_generic_assoc_list_linha = Generalization(general=generic_assoc_list_linha, specific=myDsl_GenericAssocListLinhaAction)
gen_myDsl_PostfixExpressionLinhaAction_postfix_expression_linha = Generalization(general=postfix_expression_linha, specific=myDsl_PostfixExpressionLinhaAction)
gen_myDsl_InitializerListLinhaAction_initializer_list_linha = Generalization(general=initializer_list_linha, specific=myDsl_InitializerListLinhaAction)
gen_myDsl_PlusPlus_unary_expression = Generalization(general=unary_expression, specific=myDsl_PlusPlus)
gen_myDsl_InitDecclaratorListLinhaAction_init_declarator_list_linha = Generalization(general=init_declarator_list_linha, specific=myDsl_InitDecclaratorListLinhaAction)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_type_specifier, myDsl_type_qualifier, myDsl_alignment_specifier, myDsl_type_name, myDsl_constant_expression, myDsl_Model, myDsl_translation_unit, myDsl_external_declaration, myDsl_translation_unit_linha, myDsl_function_definition, myDsl_declaration, myDsl_declaration_specifiers, myDsl_struct_declaration, myDsl_struct_declaration_list_linha, myDsl_specifier_qualifier_list, myDsl_struct_declarator_list, myDsl_static_assert_declaration, myDsl_struct_declarator, myDsl_atomic_type_specifier, myDsl_struct_or_union_specifier, myDsl_enum_specifier, myDsl_enumerator_list, myDsl_enumerator, myDsl_enumerator_list_linha, myDsl_enumeration_constant, myDsl_struct_declaration_list, myDsl_struct_or_union_specifier_complement, myDsl_declaration_list_linha, myDsl_pointer, myDsl_direct_declarator, myDsl_type_qualifier_list, myDsl_struct_declarator_list_linha, myDsl_declarator, myDsl_init_declarator_list, myDsl_declaration_list, myDsl_compound_statement, myDsl_parameter_declaration, myDsl_parameter_list_linha, myDsl_abstract_declarator, direct_abstract_declarator_complement, myDsl_type_qualifier_list_linha, myDsl_direct_declarator_linha, myDsl_direct_declarator_complemento, myDsl_assignment_expression, myDsl_parameter_type_list, myDsl_identifier_list, myDsl_parameter_lista, myDsl_identifier_list_linha, myDsl_direct_abstract_declarator, myDsl_direct_abstract_declarator_linha, myDsl_initializer, myDsl_initializer_list, myDsl_direct_abstract_declarator_complement, myDsl_postfix_expression_linha, myDsl_designation, myDsl_init_declarator_list_linha, myDsl_initializer_list_linha, myDsl_initializer_list_complement, myDsl_designator_list, myDsl_primary_expression, myDsl_designator, myDsl_designator_list_linha, myDsl_constant, myDsl_expression, myDsl_generic_selection, myDsl_generic_assoc_list, myDsl_generic_association, myDsl_generic_assoc_list_linha, myDsl_postfix_expression, myDsl_cast_expression, myDsl_multiplicative_expression, myDsl_multiplicative_expression_linha, myDsl_multiplicative_expression_complement, myDsl_conditional_expression, myDsl_postfix_expression_complement, myDsl_argument_expression_list, myDsl_argument_expression_list_linha, myDsl_unary_expression, myDsl_relational_expression, myDsl_relational_expression_linha, myDsl_relational_expression_complement, myDsl_equality_expression, myDsl_additive_expression, myDsl_additive_expression_linha, myDsl_additive_expression_complement, myDsl_shift_expression, myDsl_shift_expression_linha, myDsl_shift_expression_complement, myDsl_equality_expression_linha, myDsl_equality_expression_complement, myDsl_statement, myDsl_labeled_statement, myDsl_expression_statement, myDsl_selection_statement, myDsl_iteration_statement, myDsl_jump_statement, myDsl_and_expression, myDsl_and_expression_linha, myDsl_block_item_list, myDsl_block_item, myDsl_block_item_list_linha, myDsl_logical_or_expression, myDsl_logical_or_expression_linha, myDsl_conditional_expression_linha, myDsl_exclusive_or_expression, myDsl_exclusive_or_expression_linha, myDsl_inclusive_or_expression, myDsl_inclusive_or_expression_linha, myDsl_logical_and_expression, myDsl_logical_and_expression_linha, myDsl_init_declarator, postfix_expression, myDsl_expression_linha, myDsl_DeclarationListLinhaAction, declaration_list_linha, myDsl_TypeQualifierListLinhaAtion, type_qualifier_list_linha, myDsl_DirectAbstractDeclarratorLinhaAction, direct_abstract_declarator_linha, myDsl_string_dsl, myDsl_EnumeratorListLinhaAction, enumerator_list_linha, myDsl_StructOrUnionSpecifierComplementAction, struct_or_union_specifier_complement, myDsl_StructDeclarationListLinhaAction, struct_declaration_list_linha, myDsl_StructDeclaratorListLinhaAction, struct_declarator_list_linha, myDsl_DesignatorListLinhaAction, designator_list_linha, myDsl_PostFixEmpryParams, postfix_expression_complement, myDsl_ArgumentExpressionListLinhaAction, argument_expression_list_linha, myDsl_IdentifierListLinhaAction, identifier_list_linha, myDsl_TranlationUnitLinhaAction, translation_unit_linha, myDsl_GenericAssocListLinhaAction, generic_assoc_list_linha, myDsl_PostfixExpressionLinhaAction, postfix_expression_linha, myDsl_InitializerListLinhaAction, initializer_list_linha, myDsl_PlusPlus, unary_expression, myDsl_InitDecclaratorListLinhaAction, init_declarator_list_linha},
    associations={declaration_specifiers10, type_specifier11, type_qualifier13, alignment_specifier15, type_name17, constant_expression19, greetings0, external_declaration1, translation_unit_linha3, function_definitio5, declaration7, struct_declaration45, struct_declaration_list_linha47, specifier_qualifier_list49, struct_declarator_list51, static_assert_declaration53, struct_declarator55, atomic_type_specifier21, struct_or_union_specifier23, enum_specifier25, enumerator_list27, enumarator29, enumerator_list_linha31, enumeration_constant33, conditional_expression35, type_name38, struct_declaration_list41, struct_or_union_specifier_complement43, declaration91, declaration_list_linha94, pointer96, direct_declarator98, type_qualifier_list100, pointer103, struct_declarator_list_linha57, constant_expression59, declarator62, type_specifier64, specifier_qualifier_list68, type_qualifier70, declaration_specifiers73, init_declarator_list76, static_assert_declaration78, declaration_specifiers81, declarator84, declaration_list87, compound_statement89, parameter_declarations131, parameter_declaration133, parameter_list_linha136, declaration_specifiers138, declarator141, abstract_declarator144, pointer146, type_qualifier105, type_qualifier_list_linha108, direct_declarator_linha110, declarator112, direct_declarator_complemento115, direct_declarator_linha118, type_qualifier_list120, assignment_expression123, parameter_type_list125, identifier_list127, parameter_lista129, identifier_list_linha177, direct_abstract_declarator149, abstract_declarator151, type_qualifier_list154, assignment_expression157, parameter_type_list160, direct_abstract_declarator_linha163, init_declarator_list165, assignment_expression166, assignment_expression169, type_qualifier_list171, parameter_type_list174, postfix_expression_linha201, designation203, initializer205, init_declarator_list_linha208, designation210, initializer212, designator_list215, designator217, designator_list_linha219, constant179, expression180, generic_selection182, assignment_expression184, generic_assoc_list187, generic_association189, generic_assoc_list_linha191, type_name193, assignment_expression196, primary_expression199, cast_expression238, type_name240, unary_expression243, type_name246, cast_expression250, cast_expression252, multiplicative_expression_linha254, multiplicative_expression_complement256, constant_expression221, constant_expression223, expression226, argument_expression_list228, assignment_expressions230, postfix_expression233, shift_expression288, unary_expression236, relational_expression_linha290, shift_expression_complement292, relational_expression_linha296, shift_expression298, relational_expression300, multiplicative_expression_linha259, cast_expression261, multiplicative_expression264, additive_expression_linha266, additive_expression_complement268, additive_expression_linha271, multiplicative_expression273, additive_expression276, shift_expression_linha278, shift_expression_complement280, shift_expression_linha283, additive_expression285, expression324, expression327, statement330, expression_statement333, expression_statement2336, declaration339, equality_expression_linha302, equality_expression_complement304, equality_expression_linha307, relational_expression309, labeled_statement312, compound_statement313, expression_statement316, selection_statement318, iteration_statement320, jump_statement322, statement372, expression375, equality_expression378, and_expression_linha380, equality_expression382, and_expression_linha386, expression342, statement345, statement2348, statement351, conditional_expression354, block_item_list357, block_item359, block_item_list_linha361, block_item363, block_item_list_linha367, declaration369, logical_and_expression418, logical_or_expression_linha420, logical_and_expression422, logical_or_expression_linha426, logical_or_expression428, conditional_expression_linha431, and_expression388, exclusive_or_expression_linha390, and_expression392, exclusive_or_expression_linha396, exclusive_or_expression398, inclusive_or_expression_linha400, exclusive_or_expression402, inclusive_or_expression_linha406, inclusive_or_expression408, logical_and_expression_linha410, inclusive_or_expression412, logical_and_expression_linha416, assignment_expression465, expression_linha469, conditional_expression471, init_declarator474, init_declarator_list_linha476, declarator479, expression433, conditional_expression436, conditional_expression_linha440, conditional_expression442, unary_expression445, assignment_expression449, initializer_list451, specifier_qualifier_list454, abstract_declarator457, assignment_expression460, expression_linha463, declaration502, declaration_list_linha504, type_qualifier507, type_qualifier_list_linha509, initializer482, enumerator485, enumerator_list_linha487, struct_declaration_list490, struct_declaration492, struct_declaration_list_linha494, struct_declarator497, struct_declarator_list_linha499, init_declarator_list_linha536, designator539, designator_list_linha541, assignment_expression544, argument_expression_list_linha546, direct_abstract_declarator_complement512, direct_abstract_declarator_linha514, identifier_list_linha517, external_declaration519, translation_unit_linha521, generic_association524, generic_assoc_list_linha526, postfix_expression_complement529, postfix_expression_linha531, initializer_list_complement534, init_declarator548, init_declarator_list_linha550},
    generalizations={gen_myDsl_type_qualifier_list_direct_abstract_declarator_complement, gen_myDsl_type_name_postfix_expression, gen_myDsl_DeclarationListLinhaAction_declaration_list_linha, gen_myDsl_TypeQualifierListLinhaAtion_type_qualifier_list_linha, gen_myDsl_DirectAbstractDeclarratorLinhaAction_direct_abstract_declarator_linha, gen_myDsl_EnumeratorListLinhaAction_enumerator_list_linha, gen_myDsl_StructOrUnionSpecifierComplementAction_struct_or_union_specifier_complement, gen_myDsl_StructDeclarationListLinhaAction_struct_declaration_list_linha, gen_myDsl_StructDeclaratorListLinhaAction_struct_declarator_list_linha, gen_myDsl_DesignatorListLinhaAction_designator_list_linha, gen_myDsl_PostFixEmpryParams_postfix_expression_complement, gen_myDsl_ArgumentExpressionListLinhaAction_argument_expression_list_linha, gen_myDsl_IdentifierListLinhaAction_identifier_list_linha, gen_myDsl_TranlationUnitLinhaAction_translation_unit_linha, gen_myDsl_GenericAssocListLinhaAction_generic_assoc_list_linha, gen_myDsl_PostfixExpressionLinhaAction_postfix_expression_linha, gen_myDsl_InitializerListLinhaAction_initializer_list_linha, gen_myDsl_PlusPlus_unary_expression, gen_myDsl_InitDecclaratorListLinhaAction_init_declarator_list_linha},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)