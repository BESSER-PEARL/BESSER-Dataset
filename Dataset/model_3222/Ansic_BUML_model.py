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
ansic_declaration_specifiers = Class(name="ansic::declaration::specifiers")
ansic_type_specifier = Class(name="ansic::type::specifier")
ansic_DomainModel = Class(name="ansic::DomainModel")
ansic_translation_unit = Class(name="ansic::translation::unit")
ansic_external_declaration = Class(name="ansic::external::declaration")
ansic_translation_unit_linha = Class(name="ansic::translation::unit::linha")
ansic_function_definition = Class(name="ansic::function::definition")
ansic_declaration = Class(name="ansic::declaration")
ansic_struct_declaration_list = Class(name="ansic::struct::declaration::list")
ansic_struct_or_union_specifier_complement = Class(name="ansic::struct::or::union::specifier::complement")
ansic_type_qualifier = Class(name="ansic::type::qualifier")
ansic_alignment_specifier = Class(name="ansic::alignment::specifier")
ansic_type_name = Class(name="ansic::type::name")
ansic_constant_expression = Class(name="ansic::constant::expression")
ansic_atomic_type_specifier = Class(name="ansic::atomic::type::specifier")
ansic_struct_or_union_specifier = Class(name="ansic::struct::or::union::specifier")
ansic_enum_specifier = Class(name="ansic::enum::specifier")
ansic_enumerator_list = Class(name="ansic::enumerator::list")
ansic_enumerator = Class(name="ansic::enumerator")
ansic_enumerator_list_linha = Class(name="ansic::enumerator::list::linha")
ansic_enumeration_constant = Class(name="ansic::enumeration::constant")
ansic_struct_declaration = Class(name="ansic::struct::declaration")
ansic_struct_declaration_list_linha = Class(name="ansic::struct::declaration::list::linha")
ansic_specifier_qualifier_list = Class(name="ansic::specifier::qualifier::list")
ansic_struct_declarator_list = Class(name="ansic::struct::declarator::list")
ansic_static_assert_declaration = Class(name="ansic::static::assert::declaration")
ansic_struct_declarator = Class(name="ansic::struct::declarator")
ansic_struct_declarator_list_linha = Class(name="ansic::struct::declarator::list::linha")
ansic_declarator = Class(name="ansic::declarator")
ansic_init_declarator_list = Class(name="ansic::init::declarator::list")
ansic_declaration_list = Class(name="ansic::declaration::list")
ansic_compound_statement = Class(name="ansic::compound::statement")
ansic_declaration_list_linha = Class(name="ansic::declaration::list::linha")
ansic_pointer = Class(name="ansic::pointer")
ansic_direct_declarator = Class(name="ansic::direct::declarator")
ansic_type_qualifier_list = Class(name="ansic::type::qualifier::list")
direct_abstract_declarator_complement = Class(name="direct::abstract::declarator::complement")
ansic_type_qualifier_list_linha = Class(name="ansic::type::qualifier::list::linha")
ansic_direct_declarator_linha = Class(name="ansic::direct::declarator::linha")
ansic_direct_declarator_complemento = Class(name="ansic::direct::declarator::complemento")
ansic_assignment_expression = Class(name="ansic::assignment::expression")
ansic_direct_abstract_declarator_linha = Class(name="ansic::direct::abstract::declarator::linha")
ansic_parameter_type_list = Class(name="ansic::parameter::type::list")
ansic_initializer = Class(name="ansic::initializer")
ansic_identifier_list = Class(name="ansic::identifier::list")
ansic_parameter_lista = Class(name="ansic::parameter::lista")
ansic_parameter_declaration = Class(name="ansic::parameter::declaration")
ansic_parameter_list_linha = Class(name="ansic::parameter::list::linha")
ansic_abstract_declarator = Class(name="ansic::abstract::declarator")
ansic_direct_abstract_declarator = Class(name="ansic::direct::abstract::declarator")
ansic_generic_assoc_list = Class(name="ansic::generic::assoc::list")
ansic_generic_association = Class(name="ansic::generic::association")
ansic_generic_assoc_list_linha = Class(name="ansic::generic::assoc::list::linha")
ansic_initializer_list = Class(name="ansic::initializer::list")
ansic_direct_abstract_declarator_complement = Class(name="ansic::direct::abstract::declarator::complement")
ansic_identifier_list_linha = Class(name="ansic::identifier::list::linha")
ansic_primary_expression = Class(name="ansic::primary::expression")
ansic_constant = Class(name="ansic::constant")
ansic_expression = Class(name="ansic::expression")
ansic_generic_selection = Class(name="ansic::generic::selection")
ansic_conditional_expression = Class(name="ansic::conditional::expression")
ansic_postfix_expression_complement = Class(name="ansic::postfix::expression::complement")
ansic_postfix_expression = Class(name="ansic::postfix::expression")
ansic_postfix_expression_linha = Class(name="ansic::postfix::expression::linha")
ansic_designation = Class(name="ansic::designation")
ansic_init_declarator_list_linha = Class(name="ansic::init::declarator::list::linha")
ansic_initializer_list_linha = Class(name="ansic::initializer::list::linha")
ansic_initializer_list_complement = Class(name="ansic::initializer::list::complement")
ansic_designator_list = Class(name="ansic::designator::list")
ansic_designator = Class(name="ansic::designator")
ansic_designator_list_linha = Class(name="ansic::designator::list::linha")
ansic_multiplicative_expression_complement = Class(name="ansic::multiplicative::expression::complement")
ansic_additive_expression = Class(name="ansic::additive::expression")
ansic_argument_expression_list = Class(name="ansic::argument::expression::list")
ansic_argument_expression_list_linha = Class(name="ansic::argument::expression::list::linha")
ansic_unary_expression = Class(name="ansic::unary::expression")
ansic_cast_expression = Class(name="ansic::cast::expression")
ansic_multiplicative_expression = Class(name="ansic::multiplicative::expression")
ansic_multiplicative_expression_linha = Class(name="ansic::multiplicative::expression::linha")
ansic_relational_expression_complement = Class(name="ansic::relational::expression::complement")
ansic_equality_expression = Class(name="ansic::equality::expression")
ansic_equality_expression_linha = Class(name="ansic::equality::expression::linha")
ansic_additive_expression_linha = Class(name="ansic::additive::expression::linha")
ansic_additive_expression_complement = Class(name="ansic::additive::expression::complement")
ansic_shift_expression = Class(name="ansic::shift::expression")
ansic_shift_expression_linha = Class(name="ansic::shift::expression::linha")
ansic_shift_expression_complement = Class(name="ansic::shift::expression::complement")
ansic_relational_expression = Class(name="ansic::relational::expression")
ansic_relational_expression_linha = Class(name="ansic::relational::expression::linha")
ansic_equality_expression_complement = Class(name="ansic::equality::expression::complement")
ansic_statement = Class(name="ansic::statement")
ansic_labeled_statement = Class(name="ansic::labeled::statement")
ansic_expression_statement = Class(name="ansic::expression::statement")
ansic_selection_statement = Class(name="ansic::selection::statement")
ansic_iteration_statement = Class(name="ansic::iteration::statement")
ansic_jump_statement = Class(name="ansic::jump::statement")
ansic_block_item_list = Class(name="ansic::block::item::list")
ansic_block_item = Class(name="ansic::block::item")
ansic_block_item_list_linha = Class(name="ansic::block::item::list::linha")
ansic_logical_and_expression = Class(name="ansic::logical::and::expression")
ansic_logical_and_expression_linha = Class(name="ansic::logical::and::expression::linha")
ansic_and_expression = Class(name="ansic::and::expression")
ansic_and_expression_linha = Class(name="ansic::and::expression::linha")
ansic_exclusive_or_expression = Class(name="ansic::exclusive::or::expression")
ansic_exclusive_or_expression_linha = Class(name="ansic::exclusive::or::expression::linha")
ansic_inclusive_or_expression = Class(name="ansic::inclusive::or::expression")
ansic_inclusive_or_expression_linha = Class(name="ansic::inclusive::or::expression::linha")
ansic_logical_or_expression = Class(name="ansic::logical::or::expression")
ansic_logical_or_expression_linha = Class(name="ansic::logical::or::expression::linha")
ansic_conditional_expression_linha = Class(name="ansic::conditional::expression::linha")
postfix_expression = Class(name="postfix::expression")
ansic_expression_linha = Class(name="ansic::expression::linha")
ansic_init_declarator = Class(name="ansic::init::declarator")
ansic_IdentifierListLinhaAction = Class(name="ansic::IdentifierListLinhaAction")
identifier_list_linha = Class(name="identifier::list::linha")
ansic_string_ufcg = Class(name="ansic::string::ufcg")
ansic_EnumeratorListLinhaAction = Class(name="ansic::EnumeratorListLinhaAction")
enumerator_list_linha = Class(name="enumerator::list::linha")
ansic_StructOrUnionSpecifierComplementAction = Class(name="ansic::StructOrUnionSpecifierComplementAction")
struct_or_union_specifier_complement = Class(name="struct::or::union::specifier::complement")
ansic_StructDeclarationListLinhaAction = Class(name="ansic::StructDeclarationListLinhaAction")
struct_declaration_list_linha = Class(name="struct::declaration::list::linha")
ansic_StructDeclaratorListLinhaAction = Class(name="ansic::StructDeclaratorListLinhaAction")
struct_declarator_list_linha = Class(name="struct::declarator::list::linha")
ansic_DeclarationListLinhaAction = Class(name="ansic::DeclarationListLinhaAction")
declaration_list_linha = Class(name="declaration::list::linha")
ansic_TypeQualifierListLinhaAtion = Class(name="ansic::TypeQualifierListLinhaAtion")
type_qualifier_list_linha = Class(name="type::qualifier::list::linha")
ansic_DirectAbstractDeclarratorLinhaAction = Class(name="ansic::DirectAbstractDeclarratorLinhaAction")
direct_abstract_declarator_linha = Class(name="direct::abstract::declarator::linha")
ansic_PlusPlus = Class(name="ansic::PlusPlus")
unary_expression = Class(name="unary::expression")
ansic_TranlationUnitLinhaAction = Class(name="ansic::TranlationUnitLinhaAction")
translation_unit_linha = Class(name="translation::unit::linha")
ansic_GenericAssocListLinhaAction = Class(name="ansic::GenericAssocListLinhaAction")
generic_assoc_list_linha = Class(name="generic::assoc::list::linha")
ansic_PostfixExpressionLinhaAction = Class(name="ansic::PostfixExpressionLinhaAction")
postfix_expression_linha = Class(name="postfix::expression::linha")
ansic_InitializerListLinhaAction = Class(name="ansic::InitializerListLinhaAction")
initializer_list_linha = Class(name="initializer::list::linha")
ansic_DesignatorListLinhaAction = Class(name="ansic::DesignatorListLinhaAction")
designator_list_linha = Class(name="designator::list::linha")
ansic_PostFixEmpryParams = Class(name="ansic::PostFixEmpryParams")
postfix_expression_complement = Class(name="postfix::expression::complement")
ansic_ArgumentExpressionListLinhaAction = Class(name="ansic::ArgumentExpressionListLinhaAction")
argument_expression_list_linha = Class(name="argument::expression::list::linha")
ansic_InitDecclaratorListLinhaAction = Class(name="ansic::InitDecclaratorListLinhaAction")
init_declarator_list_linha = Class(name="init::declarator::list::linha")

# ansic_declaration_specifiers class attributes and methods
ansic_declaration_specifiers_storage_class_specifier: Property = Property(name="storage_class_specifier", type=StringType)
ansic_declaration_specifiers_function_specifier: Property = Property(name="function_specifier", type=StringType)
ansic_declaration_specifiers.attributes={ansic_declaration_specifiers_storage_class_specifier, ansic_declaration_specifiers_function_specifier}

# ansic_type_specifier class attributes and methods
ansic_type_specifier_type_name_str: Property = Property(name="type_name_str", type=StringType)
ansic_type_specifier.attributes={ansic_type_specifier_type_name_str}

# ansic_DomainModel class attributes and methods

# ansic_translation_unit class attributes and methods

# ansic_external_declaration class attributes and methods

# ansic_translation_unit_linha class attributes and methods

# ansic_function_definition class attributes and methods

# ansic_declaration class attributes and methods

# ansic_struct_declaration_list class attributes and methods

# ansic_struct_or_union_specifier_complement class attributes and methods

# ansic_type_qualifier class attributes and methods
ansic_type_qualifier_namez: Property = Property(name="namez", type=StringType)
ansic_type_qualifier.attributes={ansic_type_qualifier_namez}

# ansic_alignment_specifier class attributes and methods

# ansic_type_name class attributes and methods

# ansic_constant_expression class attributes and methods

# ansic_atomic_type_specifier class attributes and methods

# ansic_struct_or_union_specifier class attributes and methods
ansic_struct_or_union_specifier_struct_or_union: Property = Property(name="struct_or_union", type=StringType)
ansic_struct_or_union_specifier_identifier: Property = Property(name="identifier", type=StringType)
ansic_struct_or_union_specifier.attributes={ansic_struct_or_union_specifier_struct_or_union, ansic_struct_or_union_specifier_identifier}

# ansic_enum_specifier class attributes and methods
ansic_enum_specifier_identifier: Property = Property(name="identifier", type=StringType)
ansic_enum_specifier.attributes={ansic_enum_specifier_identifier}

# ansic_enumerator_list class attributes and methods

# ansic_enumerator class attributes and methods

# ansic_enumerator_list_linha class attributes and methods

# ansic_enumeration_constant class attributes and methods
ansic_enumeration_constant_identifier: Property = Property(name="identifier", type=StringType)
ansic_enumeration_constant.attributes={ansic_enumeration_constant_identifier}

# ansic_struct_declaration class attributes and methods

# ansic_struct_declaration_list_linha class attributes and methods

# ansic_specifier_qualifier_list class attributes and methods

# ansic_struct_declarator_list class attributes and methods

# ansic_static_assert_declaration class attributes and methods

# ansic_struct_declarator class attributes and methods

# ansic_struct_declarator_list_linha class attributes and methods

# ansic_declarator class attributes and methods

# ansic_init_declarator_list class attributes and methods

# ansic_declaration_list class attributes and methods

# ansic_compound_statement class attributes and methods

# ansic_declaration_list_linha class attributes and methods

# ansic_pointer class attributes and methods

# ansic_direct_declarator class attributes and methods
ansic_direct_declarator_identifier: Property = Property(name="identifier", type=StringType)
ansic_direct_declarator.attributes={ansic_direct_declarator_identifier}

# ansic_type_qualifier_list class attributes and methods

# direct_abstract_declarator_complement class attributes and methods

# ansic_type_qualifier_list_linha class attributes and methods

# ansic_direct_declarator_linha class attributes and methods

# ansic_direct_declarator_complemento class attributes and methods

# ansic_assignment_expression class attributes and methods
ansic_assignment_expression_assignment_operator: Property = Property(name="assignment_operator", type=StringType)
ansic_assignment_expression.attributes={ansic_assignment_expression_assignment_operator}

# ansic_direct_abstract_declarator_linha class attributes and methods

# ansic_parameter_type_list class attributes and methods

# ansic_initializer class attributes and methods

# ansic_identifier_list class attributes and methods
ansic_identifier_list_identifier: Property = Property(name="identifier", type=StringType)
ansic_identifier_list.attributes={ansic_identifier_list_identifier}

# ansic_parameter_lista class attributes and methods

# ansic_parameter_declaration class attributes and methods

# ansic_parameter_list_linha class attributes and methods

# ansic_abstract_declarator class attributes and methods

# ansic_direct_abstract_declarator class attributes and methods

# ansic_generic_assoc_list class attributes and methods

# ansic_generic_association class attributes and methods
ansic_generic_association_default: Property = Property(name="default", type=StringType)
ansic_generic_association.attributes={ansic_generic_association_default}

# ansic_generic_assoc_list_linha class attributes and methods

# ansic_initializer_list class attributes and methods

# ansic_direct_abstract_declarator_complement class attributes and methods

# ansic_identifier_list_linha class attributes and methods

# ansic_primary_expression class attributes and methods
ansic_primary_expression_identifier: Property = Property(name="identifier", type=StringType)
ansic_primary_expression.attributes={ansic_primary_expression_identifier}

# ansic_constant class attributes and methods
ansic_constant_i_constant: Property = Property(name="i_constant", type=IntegerType)
ansic_constant_f_constant: Property = Property(name="f_constant", type=StringType)
ansic_constant_char: Property = Property(name="char", type=StringType)
ansic_constant_enumz: Property = Property(name="enumz", type=StringType)
ansic_constant.attributes={ansic_constant_char, ansic_constant_f_constant, ansic_constant_i_constant, ansic_constant_enumz}

# ansic_expression class attributes and methods

# ansic_generic_selection class attributes and methods
ansic_generic_selection__generic: Property = Property(name="_generic", type=StringType)
ansic_generic_selection.attributes={ansic_generic_selection__generic}

# ansic_conditional_expression class attributes and methods

# ansic_postfix_expression_complement class attributes and methods
ansic_postfix_expression_complement_identifier: Property = Property(name="identifier", type=StringType)
ansic_postfix_expression_complement.attributes={ansic_postfix_expression_complement_identifier}

# ansic_postfix_expression class attributes and methods

# ansic_postfix_expression_linha class attributes and methods

# ansic_designation class attributes and methods

# ansic_init_declarator_list_linha class attributes and methods

# ansic_initializer_list_linha class attributes and methods

# ansic_initializer_list_complement class attributes and methods

# ansic_designator_list class attributes and methods

# ansic_designator class attributes and methods
ansic_designator_identifier: Property = Property(name="identifier", type=StringType)
ansic_designator.attributes={ansic_designator_identifier}

# ansic_designator_list_linha class attributes and methods

# ansic_multiplicative_expression_complement class attributes and methods

# ansic_additive_expression class attributes and methods

# ansic_argument_expression_list class attributes and methods

# ansic_argument_expression_list_linha class attributes and methods

# ansic_unary_expression class attributes and methods
ansic_unary_expression_unary_operator: Property = Property(name="unary_operator", type=StringType)
ansic_unary_expression.attributes={ansic_unary_expression_unary_operator}

# ansic_cast_expression class attributes and methods

# ansic_multiplicative_expression class attributes and methods

# ansic_multiplicative_expression_linha class attributes and methods

# ansic_relational_expression_complement class attributes and methods

# ansic_equality_expression class attributes and methods

# ansic_equality_expression_linha class attributes and methods

# ansic_additive_expression_linha class attributes and methods

# ansic_additive_expression_complement class attributes and methods

# ansic_shift_expression class attributes and methods

# ansic_shift_expression_linha class attributes and methods

# ansic_shift_expression_complement class attributes and methods

# ansic_relational_expression class attributes and methods

# ansic_relational_expression_linha class attributes and methods

# ansic_equality_expression_complement class attributes and methods

# ansic_statement class attributes and methods

# ansic_labeled_statement class attributes and methods
ansic_labeled_statement_identifier: Property = Property(name="identifier", type=StringType)
ansic_labeled_statement.attributes={ansic_labeled_statement_identifier}

# ansic_expression_statement class attributes and methods

# ansic_selection_statement class attributes and methods

# ansic_iteration_statement class attributes and methods

# ansic_jump_statement class attributes and methods
ansic_jump_statement_return: Property = Property(name="return", type=StringType)
ansic_jump_statement_identifier: Property = Property(name="identifier", type=StringType)
ansic_jump_statement_break: Property = Property(name="break", type=StringType)
ansic_jump_statement_return_vazio: Property = Property(name="return_vazio", type=StringType)
ansic_jump_statement.attributes={ansic_jump_statement_return, ansic_jump_statement_identifier, ansic_jump_statement_return_vazio, ansic_jump_statement_break}

# ansic_block_item_list class attributes and methods

# ansic_block_item class attributes and methods

# ansic_block_item_list_linha class attributes and methods

# ansic_logical_and_expression class attributes and methods

# ansic_logical_and_expression_linha class attributes and methods

# ansic_and_expression class attributes and methods

# ansic_and_expression_linha class attributes and methods

# ansic_exclusive_or_expression class attributes and methods

# ansic_exclusive_or_expression_linha class attributes and methods

# ansic_inclusive_or_expression class attributes and methods

# ansic_inclusive_or_expression_linha class attributes and methods

# ansic_logical_or_expression class attributes and methods

# ansic_logical_or_expression_linha class attributes and methods

# ansic_conditional_expression_linha class attributes and methods

# postfix_expression class attributes and methods

# ansic_expression_linha class attributes and methods

# ansic_init_declarator class attributes and methods

# ansic_IdentifierListLinhaAction class attributes and methods
ansic_IdentifierListLinhaAction_identifier: Property = Property(name="identifier", type=StringType)
ansic_IdentifierListLinhaAction.attributes={ansic_IdentifierListLinhaAction_identifier}

# identifier_list_linha class attributes and methods

# ansic_string_ufcg class attributes and methods
ansic_string_ufcg_string_literal: Property = Property(name="string_literal", type=StringType)
ansic_string_ufcg___func__: Property = Property(name="__func__", type=StringType)
ansic_string_ufcg.attributes={ansic_string_ufcg_string_literal, ansic_string_ufcg___func__}

# ansic_EnumeratorListLinhaAction class attributes and methods

# enumerator_list_linha class attributes and methods

# ansic_StructOrUnionSpecifierComplementAction class attributes and methods

# struct_or_union_specifier_complement class attributes and methods

# ansic_StructDeclarationListLinhaAction class attributes and methods

# struct_declaration_list_linha class attributes and methods

# ansic_StructDeclaratorListLinhaAction class attributes and methods

# struct_declarator_list_linha class attributes and methods

# ansic_DeclarationListLinhaAction class attributes and methods

# declaration_list_linha class attributes and methods

# ansic_TypeQualifierListLinhaAtion class attributes and methods

# type_qualifier_list_linha class attributes and methods

# ansic_DirectAbstractDeclarratorLinhaAction class attributes and methods

# direct_abstract_declarator_linha class attributes and methods

# ansic_PlusPlus class attributes and methods
ansic_PlusPlus_plus: Property = Property(name="plus", type=StringType)
ansic_PlusPlus.attributes={ansic_PlusPlus_plus}

# unary_expression class attributes and methods

# ansic_TranlationUnitLinhaAction class attributes and methods

# translation_unit_linha class attributes and methods

# ansic_GenericAssocListLinhaAction class attributes and methods

# generic_assoc_list_linha class attributes and methods

# ansic_PostfixExpressionLinhaAction class attributes and methods

# postfix_expression_linha class attributes and methods

# ansic_InitializerListLinhaAction class attributes and methods

# initializer_list_linha class attributes and methods

# ansic_DesignatorListLinhaAction class attributes and methods

# designator_list_linha class attributes and methods

# ansic_PostFixEmpryParams class attributes and methods

# postfix_expression_complement class attributes and methods

# ansic_ArgumentExpressionListLinhaAction class attributes and methods

# argument_expression_list_linha class attributes and methods

# ansic_InitDecclaratorListLinhaAction class attributes and methods

# init_declarator_list_linha class attributes and methods

# Relationships
declaration_specifiers10: BinaryAssociation = BinaryAssociation(
    name="declaration_specifiers10",
    ends={
        Property(name="ansic_declaration_specifiers", type=ansic_declaration_specifiers, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_declaration_specifiers9", type=ansic_declaration_specifiers, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type_specifier11: BinaryAssociation = BinaryAssociation(
    name="type_specifier11",
    ends={
        Property(name="ansic_type_specifier", type=ansic_declaration_specifiers, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_declaration_specifiers12", type=ansic_type_specifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
geetings0: BinaryAssociation = BinaryAssociation(
    name="geetings0",
    ends={
        Property(name="ansic_translation_unit", type=ansic_DomainModel, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_DomainModel", type=ansic_translation_unit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
external_declaration1: BinaryAssociation = BinaryAssociation(
    name="external_declaration1",
    ends={
        Property(name="ansic_external_declaration", type=ansic_translation_unit, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_translation_unit2", type=ansic_external_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
translation_unit_linha3: BinaryAssociation = BinaryAssociation(
    name="translation_unit_linha3",
    ends={
        Property(name="ansic_translation_unit_linha", type=ansic_translation_unit, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_translation_unit4", type=ansic_translation_unit_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function_definitio5: BinaryAssociation = BinaryAssociation(
    name="function_definitio5",
    ends={
        Property(name="ansic_function_definition", type=ansic_external_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_external_declaration6", type=ansic_function_definition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration7: BinaryAssociation = BinaryAssociation(
    name="declaration7",
    ends={
        Property(name="ansic_declaration", type=ansic_external_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_external_declaration8", type=ansic_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_declaration_list41: BinaryAssociation = BinaryAssociation(
    name="struct_declaration_list41",
    ends={
        Property(name="ansic_struct_declaration_list", type=ansic_struct_or_union_specifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_struct_or_union_specifier42", type=ansic_struct_declaration_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_or_union_specifier_complement43: BinaryAssociation = BinaryAssociation(
    name="struct_or_union_specifier_complement43",
    ends={
        Property(name="ansic_struct_or_union_specifier_complement", type=ansic_struct_or_union_specifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_struct_or_union_specifier44", type=ansic_struct_or_union_specifier_complement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_qualifier13: BinaryAssociation = BinaryAssociation(
    name="type_qualifier13",
    ends={
        Property(name="ansic_type_qualifier", type=ansic_declaration_specifiers, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_declaration_specifiers14", type=ansic_type_qualifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alignment_specifier15: BinaryAssociation = BinaryAssociation(
    name="alignment_specifier15",
    ends={
        Property(name="ansic_alignment_specifier", type=ansic_declaration_specifiers, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_declaration_specifiers16", type=ansic_alignment_specifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_name17: BinaryAssociation = BinaryAssociation(
    name="type_name17",
    ends={
        Property(name="ansic_type_name", type=ansic_alignment_specifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_alignment_specifier18", type=ansic_type_name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant_expression19: BinaryAssociation = BinaryAssociation(
    name="constant_expression19",
    ends={
        Property(name="ansic_constant_expression", type=ansic_alignment_specifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_alignment_specifier20", type=ansic_constant_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
atomic_type_specifier21: BinaryAssociation = BinaryAssociation(
    name="atomic_type_specifier21",
    ends={
        Property(name="ansic_atomic_type_specifier", type=ansic_type_specifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_type_specifier22", type=ansic_atomic_type_specifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_or_union_specifier23: BinaryAssociation = BinaryAssociation(
    name="struct_or_union_specifier23",
    ends={
        Property(name="ansic_struct_or_union_specifier", type=ansic_type_specifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_type_specifier24", type=ansic_struct_or_union_specifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enum_specifier25: BinaryAssociation = BinaryAssociation(
    name="enum_specifier25",
    ends={
        Property(name="ansic_enum_specifier", type=ansic_type_specifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_type_specifier26", type=ansic_enum_specifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumerator_list27: BinaryAssociation = BinaryAssociation(
    name="enumerator_list27",
    ends={
        Property(name="ansic_enumerator_list", type=ansic_enum_specifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_enum_specifier28", type=ansic_enumerator_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumarator29: BinaryAssociation = BinaryAssociation(
    name="enumarator29",
    ends={
        Property(name="ansic_enumerator", type=ansic_enumerator_list, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_enumerator_list30", type=ansic_enumerator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumerator_list_linha31: BinaryAssociation = BinaryAssociation(
    name="enumerator_list_linha31",
    ends={
        Property(name="ansic_enumerator_list_linha", type=ansic_enumerator_list, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_enumerator_list32", type=ansic_enumerator_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumeration_constant33: BinaryAssociation = BinaryAssociation(
    name="enumeration_constant33",
    ends={
        Property(name="ansic_enumeration_constant", type=ansic_enumerator, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_enumerator34", type=ansic_enumeration_constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditional_expression35: BinaryAssociation = BinaryAssociation(
    name="conditional_expression35",
    ends={
        Property(name="ansic_constant_expression37", type=ansic_enumerator, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_enumerator36", type=ansic_constant_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_name38: BinaryAssociation = BinaryAssociation(
    name="type_name38",
    ends={
        Property(name="ansic_type_name40", type=ansic_atomic_type_specifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_atomic_type_specifier39", type=ansic_type_name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
static_assert_declaration78: BinaryAssociation = BinaryAssociation(
    name="static_assert_declaration78",
    ends={
        Property(name="ansic_static_assert_declaration80", type=ansic_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_declaration79", type=ansic_static_assert_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration_specifiers81: BinaryAssociation = BinaryAssociation(
    name="declaration_specifiers81",
    ends={
        Property(name="ansic_declaration_specifiers83", type=ansic_function_definition, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_function_definition82", type=ansic_declaration_specifiers, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
struct_declaration45: BinaryAssociation = BinaryAssociation(
    name="struct_declaration45",
    ends={
        Property(name="ansic_struct_declaration", type=ansic_struct_declaration_list, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_struct_declaration_list46", type=ansic_struct_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_declaration_list_linha47: BinaryAssociation = BinaryAssociation(
    name="struct_declaration_list_linha47",
    ends={
        Property(name="ansic_struct_declaration_list_linha", type=ansic_struct_declaration_list, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_struct_declaration_list48", type=ansic_struct_declaration_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specifier_qualifier_list49: BinaryAssociation = BinaryAssociation(
    name="specifier_qualifier_list49",
    ends={
        Property(name="ansic_specifier_qualifier_list", type=ansic_struct_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_struct_declaration50", type=ansic_specifier_qualifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_declarator_list51: BinaryAssociation = BinaryAssociation(
    name="struct_declarator_list51",
    ends={
        Property(name="ansic_struct_declarator_list", type=ansic_struct_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_struct_declaration52", type=ansic_struct_declarator_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
static_assert_declaration53: BinaryAssociation = BinaryAssociation(
    name="static_assert_declaration53",
    ends={
        Property(name="ansic_static_assert_declaration", type=ansic_struct_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_struct_declaration54", type=ansic_static_assert_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_declarator55: BinaryAssociation = BinaryAssociation(
    name="struct_declarator55",
    ends={
        Property(name="ansic_struct_declarator", type=ansic_struct_declarator_list, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_struct_declarator_list56", type=ansic_struct_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_declarator_list_linha57: BinaryAssociation = BinaryAssociation(
    name="struct_declarator_list_linha57",
    ends={
        Property(name="ansic_struct_declarator_list_linha", type=ansic_struct_declarator_list, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_struct_declarator_list58", type=ansic_struct_declarator_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant_expression59: BinaryAssociation = BinaryAssociation(
    name="constant_expression59",
    ends={
        Property(name="ansic_constant_expression61", type=ansic_struct_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_struct_declarator60", type=ansic_constant_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarator62: BinaryAssociation = BinaryAssociation(
    name="declarator62",
    ends={
        Property(name="ansic_declarator", type=ansic_struct_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_struct_declarator63", type=ansic_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_specifier64: BinaryAssociation = BinaryAssociation(
    name="type_specifier64",
    ends={
        Property(name="ansic_type_specifier66", type=ansic_specifier_qualifier_list, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_specifier_qualifier_list65", type=ansic_type_specifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specifier_qualifier_list68: BinaryAssociation = BinaryAssociation(
    name="specifier_qualifier_list68",
    ends={
        Property(name="ansic_specifier_qualifier_list69", type=ansic_specifier_qualifier_list, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_specifier_qualifier_list67", type=ansic_specifier_qualifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_qualifier70: BinaryAssociation = BinaryAssociation(
    name="type_qualifier70",
    ends={
        Property(name="ansic_type_qualifier72", type=ansic_specifier_qualifier_list, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_specifier_qualifier_list71", type=ansic_type_qualifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration_specifiers73: BinaryAssociation = BinaryAssociation(
    name="declaration_specifiers73",
    ends={
        Property(name="ansic_declaration_specifiers75", type=ansic_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_declaration74", type=ansic_declaration_specifiers, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
init_declarator_list76: BinaryAssociation = BinaryAssociation(
    name="init_declarator_list76",
    ends={
        Property(name="ansic_init_declarator_list", type=ansic_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_declaration77", type=ansic_init_declarator_list, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
direct_declarator_linha118: BinaryAssociation = BinaryAssociation(
    name="direct_declarator_linha118",
    ends={
        Property(name="ansic_direct_declarator_linha119", type=ansic_direct_declarator_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_direct_declarator_linha117", type=ansic_direct_declarator_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_qualifier_list120: BinaryAssociation = BinaryAssociation(
    name="type_qualifier_list120",
    ends={
        Property(name="ansic_type_qualifier_list122", type=ansic_direct_declarator_complemento, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_direct_declarator_complemento121", type=ansic_type_qualifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarator84: BinaryAssociation = BinaryAssociation(
    name="declarator84",
    ends={
        Property(name="ansic_declarator86", type=ansic_function_definition, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_function_definition85", type=ansic_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration_list87: BinaryAssociation = BinaryAssociation(
    name="declaration_list87",
    ends={
        Property(name="ansic_declaration_list", type=ansic_function_definition, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_function_definition88", type=ansic_declaration_list, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compound_statement89: BinaryAssociation = BinaryAssociation(
    name="compound_statement89",
    ends={
        Property(name="ansic_compound_statement", type=ansic_function_definition, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_function_definition90", type=ansic_compound_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration91: BinaryAssociation = BinaryAssociation(
    name="declaration91",
    ends={
        Property(name="ansic_declaration93", type=ansic_declaration_list, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_declaration_list92", type=ansic_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration_list_linha94: BinaryAssociation = BinaryAssociation(
    name="declaration_list_linha94",
    ends={
        Property(name="ansic_declaration_list_linha", type=ansic_declaration_list, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_declaration_list95", type=ansic_declaration_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pointer96: BinaryAssociation = BinaryAssociation(
    name="pointer96",
    ends={
        Property(name="ansic_pointer", type=ansic_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_declarator97", type=ansic_pointer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
direct_declarator98: BinaryAssociation = BinaryAssociation(
    name="direct_declarator98",
    ends={
        Property(name="ansic_direct_declarator", type=ansic_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_declarator99", type=ansic_direct_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_qualifier_list100: BinaryAssociation = BinaryAssociation(
    name="type_qualifier_list100",
    ends={
        Property(name="ansic_type_qualifier_list", type=ansic_pointer, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_pointer101", type=ansic_type_qualifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pointer103: BinaryAssociation = BinaryAssociation(
    name="pointer103",
    ends={
        Property(name="ansic_pointer104", type=ansic_pointer, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_pointer102", type=ansic_pointer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_qualifier105: BinaryAssociation = BinaryAssociation(
    name="type_qualifier105",
    ends={
        Property(name="ansic_type_qualifier107", type=ansic_type_qualifier_list, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_type_qualifier_list106", type=ansic_type_qualifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_qualifier_list_linha108: BinaryAssociation = BinaryAssociation(
    name="type_qualifier_list_linha108",
    ends={
        Property(name="ansic_type_qualifier_list_linha", type=ansic_type_qualifier_list, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_type_qualifier_list109", type=ansic_type_qualifier_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
direct_declarator_linha110: BinaryAssociation = BinaryAssociation(
    name="direct_declarator_linha110",
    ends={
        Property(name="ansic_direct_declarator_linha", type=ansic_direct_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_direct_declarator111", type=ansic_direct_declarator_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarator112: BinaryAssociation = BinaryAssociation(
    name="declarator112",
    ends={
        Property(name="ansic_declarator114", type=ansic_direct_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_direct_declarator113", type=ansic_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
direct_declarator_complemento115: BinaryAssociation = BinaryAssociation(
    name="direct_declarator_complemento115",
    ends={
        Property(name="ansic_direct_declarator_complemento", type=ansic_direct_declarator_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_direct_declarator_linha116", type=ansic_direct_declarator_complemento, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_qualifier_list154: BinaryAssociation = BinaryAssociation(
    name="type_qualifier_list154",
    ends={
        Property(name="ansic_type_qualifier_list156", type=ansic_direct_abstract_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_direct_abstract_declarator155", type=ansic_type_qualifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment_expression157: BinaryAssociation = BinaryAssociation(
    name="assignment_expression157",
    ends={
        Property(name="ansic_assignment_expression159", type=ansic_direct_abstract_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_direct_abstract_declarator158", type=ansic_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter_type_list160: BinaryAssociation = BinaryAssociation(
    name="parameter_type_list160",
    ends={
        Property(name="ansic_parameter_type_list162", type=ansic_direct_abstract_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_direct_abstract_declarator161", type=ansic_parameter_type_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment_expression123: BinaryAssociation = BinaryAssociation(
    name="assignment_expression123",
    ends={
        Property(name="ansic_assignment_expression", type=ansic_direct_declarator_complemento, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_direct_declarator_complemento124", type=ansic_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
direct_abstract_declarator_linha163: BinaryAssociation = BinaryAssociation(
    name="direct_abstract_declarator_linha163",
    ends={
        Property(name="ansic_direct_abstract_declarator_linha", type=ansic_direct_abstract_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_direct_abstract_declarator164", type=ansic_direct_abstract_declarator_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter_type_list125: BinaryAssociation = BinaryAssociation(
    name="parameter_type_list125",
    ends={
        Property(name="ansic_parameter_type_list", type=ansic_direct_declarator_complemento, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_direct_declarator_complemento126", type=ansic_parameter_type_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier_list127: BinaryAssociation = BinaryAssociation(
    name="identifier_list127",
    ends={
        Property(name="ansic_identifier_list", type=ansic_direct_declarator_complemento, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_direct_declarator_complemento128", type=ansic_identifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter_lista129: BinaryAssociation = BinaryAssociation(
    name="parameter_lista129",
    ends={
        Property(name="ansic_parameter_lista", type=ansic_parameter_type_list, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_parameter_type_list130", type=ansic_parameter_lista, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter_declarations131: BinaryAssociation = BinaryAssociation(
    name="parameter_declarations131",
    ends={
        Property(name="ansic_parameter_declaration", type=ansic_parameter_lista, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_parameter_lista132", type=ansic_parameter_declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter_declaration133: BinaryAssociation = BinaryAssociation(
    name="parameter_declaration133",
    ends={
        Property(name="ansic_parameter_declaration134", type=ansic_parameter_list_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_parameter_list_linha", type=ansic_parameter_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter_list_linha136: BinaryAssociation = BinaryAssociation(
    name="parameter_list_linha136",
    ends={
        Property(name="ansic_parameter_list_linha137", type=ansic_parameter_list_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_parameter_list_linha135", type=ansic_parameter_list_linha, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaration_specifiers138: BinaryAssociation = BinaryAssociation(
    name="declaration_specifiers138",
    ends={
        Property(name="ansic_declaration_specifiers140", type=ansic_parameter_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_parameter_declaration139", type=ansic_declaration_specifiers, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarator141: BinaryAssociation = BinaryAssociation(
    name="declarator141",
    ends={
        Property(name="ansic_declarator143", type=ansic_parameter_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_parameter_declaration142", type=ansic_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
abstract_declarator144: BinaryAssociation = BinaryAssociation(
    name="abstract_declarator144",
    ends={
        Property(name="ansic_abstract_declarator", type=ansic_parameter_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_parameter_declaration145", type=ansic_abstract_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pointer146: BinaryAssociation = BinaryAssociation(
    name="pointer146",
    ends={
        Property(name="ansic_pointer148", type=ansic_abstract_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_abstract_declarator147", type=ansic_pointer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
direct_abstract_declarator149: BinaryAssociation = BinaryAssociation(
    name="direct_abstract_declarator149",
    ends={
        Property(name="ansic_direct_abstract_declarator", type=ansic_abstract_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_abstract_declarator150", type=ansic_direct_abstract_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
abstract_declarator151: BinaryAssociation = BinaryAssociation(
    name="abstract_declarator151",
    ends={
        Property(name="ansic_abstract_declarator153", type=ansic_direct_abstract_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_direct_abstract_declarator152", type=ansic_abstract_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
generic_assoc_list187: BinaryAssociation = BinaryAssociation(
    name="generic_assoc_list187",
    ends={
        Property(name="ansic_generic_assoc_list", type=ansic_generic_selection, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_generic_selection188", type=ansic_generic_assoc_list, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generic_association189: BinaryAssociation = BinaryAssociation(
    name="generic_association189",
    ends={
        Property(name="ansic_generic_association", type=ansic_generic_assoc_list, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_generic_assoc_list190", type=ansic_generic_association, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
generic_assoc_list_linha191: BinaryAssociation = BinaryAssociation(
    name="generic_assoc_list_linha191",
    ends={
        Property(name="ansic_generic_assoc_list_linha", type=ansic_generic_assoc_list, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_generic_assoc_list192", type=ansic_generic_assoc_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init_declarator_list165: BinaryAssociation = BinaryAssociation(
    name="init_declarator_list165",
    ends={
        Property(name="ansic_initializer_list", type=ansic_initializer, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_initializer", type=ansic_initializer_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment_expression166: BinaryAssociation = BinaryAssociation(
    name="assignment_expression166",
    ends={
        Property(name="ansic_assignment_expression168", type=ansic_initializer, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_initializer167", type=ansic_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment_expression169: BinaryAssociation = BinaryAssociation(
    name="assignment_expression169",
    ends={
        Property(name="ansic_assignment_expression170", type=ansic_direct_abstract_declarator_complement, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_direct_abstract_declarator_complement", type=ansic_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_qualifier_list171: BinaryAssociation = BinaryAssociation(
    name="type_qualifier_list171",
    ends={
        Property(name="ansic_type_qualifier_list173", type=ansic_direct_abstract_declarator_complement, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_direct_abstract_declarator_complement172", type=ansic_type_qualifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter_type_list174: BinaryAssociation = BinaryAssociation(
    name="parameter_type_list174",
    ends={
        Property(name="ansic_parameter_type_list176", type=ansic_direct_abstract_declarator_complement, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_direct_abstract_declarator_complement175", type=ansic_parameter_type_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier_list_linha177: BinaryAssociation = BinaryAssociation(
    name="identifier_list_linha177",
    ends={
        Property(name="ansic_identifier_list_linha", type=ansic_identifier_list, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_identifier_list178", type=ansic_identifier_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant179: BinaryAssociation = BinaryAssociation(
    name="constant179",
    ends={
        Property(name="ansic_constant", type=ansic_primary_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_primary_expression", type=ansic_constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression180: BinaryAssociation = BinaryAssociation(
    name="expression180",
    ends={
        Property(name="ansic_expression", type=ansic_primary_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_primary_expression181", type=ansic_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
generic_selection182: BinaryAssociation = BinaryAssociation(
    name="generic_selection182",
    ends={
        Property(name="ansic_generic_selection", type=ansic_primary_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_primary_expression183", type=ansic_generic_selection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment_expression184: BinaryAssociation = BinaryAssociation(
    name="assignment_expression184",
    ends={
        Property(name="ansic_assignment_expression186", type=ansic_generic_selection, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_generic_selection185", type=ansic_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant_expression221: BinaryAssociation = BinaryAssociation(
    name="constant_expression221",
    ends={
        Property(name="ansic_conditional_expression", type=ansic_designator, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_designator222", type=ansic_conditional_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant_expression223: BinaryAssociation = BinaryAssociation(
    name="constant_expression223",
    ends={
        Property(name="ansic_constant_expression225", type=ansic_static_assert_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_static_assert_declaration224", type=ansic_constant_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_name193: BinaryAssociation = BinaryAssociation(
    name="type_name193",
    ends={
        Property(name="ansic_type_name195", type=ansic_generic_association, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_generic_association194", type=ansic_type_name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment_expression196: BinaryAssociation = BinaryAssociation(
    name="assignment_expression196",
    ends={
        Property(name="ansic_assignment_expression198", type=ansic_generic_association, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_generic_association197", type=ansic_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primary_expression199: BinaryAssociation = BinaryAssociation(
    name="primary_expression199",
    ends={
        Property(name="ansic_primary_expression200", type=ansic_postfix_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_postfix_expression", type=ansic_primary_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postfix_expression_linha201: BinaryAssociation = BinaryAssociation(
    name="postfix_expression_linha201",
    ends={
        Property(name="ansic_postfix_expression_linha", type=ansic_postfix_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_postfix_expression202", type=ansic_postfix_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
designation203: BinaryAssociation = BinaryAssociation(
    name="designation203",
    ends={
        Property(name="ansic_designation", type=ansic_initializer_list, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_initializer_list204", type=ansic_designation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initializer205: BinaryAssociation = BinaryAssociation(
    name="initializer205",
    ends={
        Property(name="ansic_initializer207", type=ansic_initializer_list, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_initializer_list206", type=ansic_initializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init_declarator_list_linha208: BinaryAssociation = BinaryAssociation(
    name="init_declarator_list_linha208",
    ends={
        Property(name="ansic_init_declarator_list_linha", type=ansic_initializer_list, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_initializer_list209", type=ansic_init_declarator_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
designation210: BinaryAssociation = BinaryAssociation(
    name="designation210",
    ends={
        Property(name="ansic_designation211", type=ansic_initializer_list_complement, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_initializer_list_complement", type=ansic_designation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initializer212: BinaryAssociation = BinaryAssociation(
    name="initializer212",
    ends={
        Property(name="ansic_initializer214", type=ansic_initializer_list_complement, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_initializer_list_complement213", type=ansic_initializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
designator_list215: BinaryAssociation = BinaryAssociation(
    name="designator_list215",
    ends={
        Property(name="ansic_designator_list", type=ansic_designation, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_designation216", type=ansic_designator_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
designator217: BinaryAssociation = BinaryAssociation(
    name="designator217",
    ends={
        Property(name="ansic_designator", type=ansic_designator_list, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_designator_list218", type=ansic_designator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
designator_list_linha219: BinaryAssociation = BinaryAssociation(
    name="designator_list_linha219",
    ends={
        Property(name="ansic_designator_list_linha", type=ansic_designator_list, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_designator_list220", type=ansic_designator_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multiplicative_expression_complement256: BinaryAssociation = BinaryAssociation(
    name="multiplicative_expression_complement256",
    ends={
        Property(name="ansic_multiplicative_expression_complement", type=ansic_multiplicative_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_multiplicative_expression_linha257", type=ansic_multiplicative_expression_complement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multiplicative_expression_linha259: BinaryAssociation = BinaryAssociation(
    name="multiplicative_expression_linha259",
    ends={
        Property(name="ansic_multiplicative_expression_linha260", type=ansic_multiplicative_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_multiplicative_expression_linha258", type=ansic_multiplicative_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cast_expression261: BinaryAssociation = BinaryAssociation(
    name="cast_expression261",
    ends={
        Property(name="ansic_cast_expression263", type=ansic_multiplicative_expression_complement, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_multiplicative_expression_complement262", type=ansic_cast_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression226: BinaryAssociation = BinaryAssociation(
    name="expression226",
    ends={
        Property(name="ansic_expression227", type=ansic_postfix_expression_complement, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_postfix_expression_complement", type=ansic_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argument_expression_list228: BinaryAssociation = BinaryAssociation(
    name="argument_expression_list228",
    ends={
        Property(name="ansic_argument_expression_list", type=ansic_postfix_expression_complement, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_postfix_expression_complement229", type=ansic_argument_expression_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment_expressions230: BinaryAssociation = BinaryAssociation(
    name="assignment_expressions230",
    ends={
        Property(name="ansic_assignment_expression232", type=ansic_argument_expression_list, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_argument_expression_list231", type=ansic_assignment_expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postfix_expression233: BinaryAssociation = BinaryAssociation(
    name="postfix_expression233",
    ends={
        Property(name="ansic_postfix_expression234", type=ansic_unary_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_unary_expression", type=ansic_postfix_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unary_expression236: BinaryAssociation = BinaryAssociation(
    name="unary_expression236",
    ends={
        Property(name="ansic_unary_expression237", type=ansic_unary_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_unary_expression235", type=ansic_unary_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cast_expression238: BinaryAssociation = BinaryAssociation(
    name="cast_expression238",
    ends={
        Property(name="ansic_cast_expression", type=ansic_unary_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_unary_expression239", type=ansic_cast_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_name240: BinaryAssociation = BinaryAssociation(
    name="type_name240",
    ends={
        Property(name="ansic_type_name242", type=ansic_unary_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_unary_expression241", type=ansic_type_name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unary_expression243: BinaryAssociation = BinaryAssociation(
    name="unary_expression243",
    ends={
        Property(name="ansic_unary_expression245", type=ansic_cast_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_cast_expression244", type=ansic_unary_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_name246: BinaryAssociation = BinaryAssociation(
    name="type_name246",
    ends={
        Property(name="ansic_type_name248", type=ansic_cast_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_cast_expression247", type=ansic_type_name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cast_expression250: BinaryAssociation = BinaryAssociation(
    name="cast_expression250",
    ends={
        Property(name="ansic_cast_expression251", type=ansic_cast_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_cast_expression249", type=ansic_cast_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cast_expression252: BinaryAssociation = BinaryAssociation(
    name="cast_expression252",
    ends={
        Property(name="ansic_cast_expression253", type=ansic_multiplicative_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_multiplicative_expression", type=ansic_cast_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multiplicative_expression_linha254: BinaryAssociation = BinaryAssociation(
    name="multiplicative_expression_linha254",
    ends={
        Property(name="ansic_multiplicative_expression_linha", type=ansic_multiplicative_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_multiplicative_expression255", type=ansic_multiplicative_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relational_expression_linha296: BinaryAssociation = BinaryAssociation(
    name="relational_expression_linha296",
    ends={
        Property(name="ansic_relational_expression_linha297", type=ansic_relational_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_relational_expression_linha295", type=ansic_relational_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shift_expression298: BinaryAssociation = BinaryAssociation(
    name="shift_expression298",
    ends={
        Property(name="ansic_shift_expression299", type=ansic_relational_expression_complement, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_relational_expression_complement", type=ansic_shift_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relational_expression300: BinaryAssociation = BinaryAssociation(
    name="relational_expression300",
    ends={
        Property(name="ansic_relational_expression301", type=ansic_equality_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_equality_expression", type=ansic_relational_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
equality_expression_linha302: BinaryAssociation = BinaryAssociation(
    name="equality_expression_linha302",
    ends={
        Property(name="ansic_equality_expression_linha", type=ansic_equality_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_equality_expression303", type=ansic_equality_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multiplicative_expression264: BinaryAssociation = BinaryAssociation(
    name="multiplicative_expression264",
    ends={
        Property(name="ansic_multiplicative_expression265", type=ansic_additive_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_additive_expression", type=ansic_multiplicative_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
additive_expression_linha266: BinaryAssociation = BinaryAssociation(
    name="additive_expression_linha266",
    ends={
        Property(name="ansic_additive_expression_linha", type=ansic_additive_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_additive_expression267", type=ansic_additive_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
additive_expression_complement268: BinaryAssociation = BinaryAssociation(
    name="additive_expression_complement268",
    ends={
        Property(name="ansic_additive_expression_complement", type=ansic_additive_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_additive_expression_linha269", type=ansic_additive_expression_complement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
additive_expression_linha271: BinaryAssociation = BinaryAssociation(
    name="additive_expression_linha271",
    ends={
        Property(name="ansic_additive_expression_linha272", type=ansic_additive_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_additive_expression_linha270", type=ansic_additive_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multiplicative_expression273: BinaryAssociation = BinaryAssociation(
    name="multiplicative_expression273",
    ends={
        Property(name="ansic_multiplicative_expression275", type=ansic_additive_expression_complement, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_additive_expression_complement274", type=ansic_multiplicative_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
additive_expression276: BinaryAssociation = BinaryAssociation(
    name="additive_expression276",
    ends={
        Property(name="ansic_additive_expression277", type=ansic_shift_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_shift_expression", type=ansic_additive_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shift_expression_linha278: BinaryAssociation = BinaryAssociation(
    name="shift_expression_linha278",
    ends={
        Property(name="ansic_shift_expression_linha", type=ansic_shift_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_shift_expression279", type=ansic_shift_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shift_expression_complement280: BinaryAssociation = BinaryAssociation(
    name="shift_expression_complement280",
    ends={
        Property(name="ansic_shift_expression_complement", type=ansic_shift_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_shift_expression_linha281", type=ansic_shift_expression_complement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shift_expression_linha283: BinaryAssociation = BinaryAssociation(
    name="shift_expression_linha283",
    ends={
        Property(name="ansic_shift_expression_linha284", type=ansic_shift_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_shift_expression_linha282", type=ansic_shift_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
additive_expression285: BinaryAssociation = BinaryAssociation(
    name="additive_expression285",
    ends={
        Property(name="ansic_additive_expression287", type=ansic_shift_expression_complement, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_shift_expression_complement286", type=ansic_additive_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shift_expression288: BinaryAssociation = BinaryAssociation(
    name="shift_expression288",
    ends={
        Property(name="ansic_shift_expression289", type=ansic_relational_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_relational_expression", type=ansic_shift_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relational_expression_linha290: BinaryAssociation = BinaryAssociation(
    name="relational_expression_linha290",
    ends={
        Property(name="ansic_relational_expression_linha", type=ansic_relational_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_relational_expression291", type=ansic_relational_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shift_expression_complement292: BinaryAssociation = BinaryAssociation(
    name="shift_expression_complement292",
    ends={
        Property(name="ansic_shift_expression_complement294", type=ansic_relational_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_relational_expression_linha293", type=ansic_shift_expression_complement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression324: BinaryAssociation = BinaryAssociation(
    name="expression324",
    ends={
        Property(name="ansic_expression326", type=ansic_jump_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_jump_statement325", type=ansic_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression327: BinaryAssociation = BinaryAssociation(
    name="expression327",
    ends={
        Property(name="ansic_expression329", type=ansic_iteration_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_iteration_statement328", type=ansic_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
equality_expression_complement304: BinaryAssociation = BinaryAssociation(
    name="equality_expression_complement304",
    ends={
        Property(name="ansic_equality_expression_complement", type=ansic_equality_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_equality_expression_linha305", type=ansic_equality_expression_complement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
equality_expression_linha307: BinaryAssociation = BinaryAssociation(
    name="equality_expression_linha307",
    ends={
        Property(name="ansic_equality_expression_linha308", type=ansic_equality_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_equality_expression_linha306", type=ansic_equality_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relational_expression309: BinaryAssociation = BinaryAssociation(
    name="relational_expression309",
    ends={
        Property(name="ansic_relational_expression311", type=ansic_equality_expression_complement, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_equality_expression_complement310", type=ansic_relational_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labeled_statement312: BinaryAssociation = BinaryAssociation(
    name="labeled_statement312",
    ends={
        Property(name="ansic_labeled_statement", type=ansic_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_statement", type=ansic_labeled_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
compound_statement313: BinaryAssociation = BinaryAssociation(
    name="compound_statement313",
    ends={
        Property(name="ansic_compound_statement315", type=ansic_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_statement314", type=ansic_compound_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression_statement316: BinaryAssociation = BinaryAssociation(
    name="expression_statement316",
    ends={
        Property(name="ansic_expression_statement", type=ansic_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_statement317", type=ansic_expression_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selection_statement318: BinaryAssociation = BinaryAssociation(
    name="selection_statement318",
    ends={
        Property(name="ansic_selection_statement", type=ansic_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_statement319", type=ansic_selection_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iteration_statement320: BinaryAssociation = BinaryAssociation(
    name="iteration_statement320",
    ends={
        Property(name="ansic_iteration_statement", type=ansic_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_statement321", type=ansic_iteration_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
jump_statement322: BinaryAssociation = BinaryAssociation(
    name="jump_statement322",
    ends={
        Property(name="ansic_jump_statement", type=ansic_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_statement323", type=ansic_jump_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block_item_list_linha367: BinaryAssociation = BinaryAssociation(
    name="block_item_list_linha367",
    ends={
        Property(name="ansic_block_item_list_linha368", type=ansic_block_item_list_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_block_item_list_linha366", type=ansic_block_item_list_linha, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaration369: BinaryAssociation = BinaryAssociation(
    name="declaration369",
    ends={
        Property(name="ansic_declaration371", type=ansic_block_item, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_block_item370", type=ansic_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement372: BinaryAssociation = BinaryAssociation(
    name="statement372",
    ends={
        Property(name="ansic_statement374", type=ansic_block_item, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_block_item373", type=ansic_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement330: BinaryAssociation = BinaryAssociation(
    name="statement330",
    ends={
        Property(name="ansic_statement332", type=ansic_iteration_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_iteration_statement331", type=ansic_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression375: BinaryAssociation = BinaryAssociation(
    name="expression375",
    ends={
        Property(name="ansic_expression377", type=ansic_expression_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_expression_statement376", type=ansic_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression_statement333: BinaryAssociation = BinaryAssociation(
    name="expression_statement333",
    ends={
        Property(name="ansic_expression_statement335", type=ansic_iteration_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_iteration_statement334", type=ansic_expression_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression_statement2336: BinaryAssociation = BinaryAssociation(
    name="expression_statement2336",
    ends={
        Property(name="ansic_expression_statement338", type=ansic_iteration_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_iteration_statement337", type=ansic_expression_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration339: BinaryAssociation = BinaryAssociation(
    name="declaration339",
    ends={
        Property(name="ansic_declaration341", type=ansic_iteration_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_iteration_statement340", type=ansic_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression342: BinaryAssociation = BinaryAssociation(
    name="expression342",
    ends={
        Property(name="ansic_expression344", type=ansic_selection_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_selection_statement343", type=ansic_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement345: BinaryAssociation = BinaryAssociation(
    name="statement345",
    ends={
        Property(name="ansic_statement347", type=ansic_selection_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_selection_statement346", type=ansic_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement2348: BinaryAssociation = BinaryAssociation(
    name="statement2348",
    ends={
        Property(name="ansic_statement350", type=ansic_selection_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_selection_statement349", type=ansic_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement351: BinaryAssociation = BinaryAssociation(
    name="statement351",
    ends={
        Property(name="ansic_statement353", type=ansic_labeled_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_labeled_statement352", type=ansic_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditional_expression354: BinaryAssociation = BinaryAssociation(
    name="conditional_expression354",
    ends={
        Property(name="ansic_conditional_expression356", type=ansic_labeled_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_labeled_statement355", type=ansic_conditional_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block_item_list357: BinaryAssociation = BinaryAssociation(
    name="block_item_list357",
    ends={
        Property(name="ansic_block_item_list", type=ansic_compound_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_compound_statement358", type=ansic_block_item_list, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block_item359: BinaryAssociation = BinaryAssociation(
    name="block_item359",
    ends={
        Property(name="ansic_block_item", type=ansic_block_item_list, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_block_item_list360", type=ansic_block_item, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block_item_list_linha361: BinaryAssociation = BinaryAssociation(
    name="block_item_list_linha361",
    ends={
        Property(name="ansic_block_item_list_linha", type=ansic_block_item_list, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_block_item_list362", type=ansic_block_item_list_linha, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block_item363: BinaryAssociation = BinaryAssociation(
    name="block_item363",
    ends={
        Property(name="ansic_block_item365", type=ansic_block_item_list_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_block_item_list_linha364", type=ansic_block_item, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inclusive_or_expression_linha406: BinaryAssociation = BinaryAssociation(
    name="inclusive_or_expression_linha406",
    ends={
        Property(name="ansic_inclusive_or_expression_linha407", type=ansic_inclusive_or_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_inclusive_or_expression_linha405", type=ansic_inclusive_or_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inclusive_or_expression408: BinaryAssociation = BinaryAssociation(
    name="inclusive_or_expression408",
    ends={
        Property(name="ansic_inclusive_or_expression409", type=ansic_logical_and_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_logical_and_expression", type=ansic_inclusive_or_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
logical_and_expression_linha410: BinaryAssociation = BinaryAssociation(
    name="logical_and_expression_linha410",
    ends={
        Property(name="ansic_logical_and_expression_linha", type=ansic_logical_and_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_logical_and_expression411", type=ansic_logical_and_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inclusive_or_expression412: BinaryAssociation = BinaryAssociation(
    name="inclusive_or_expression412",
    ends={
        Property(name="ansic_inclusive_or_expression414", type=ansic_logical_and_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_logical_and_expression_linha413", type=ansic_inclusive_or_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
equality_expression378: BinaryAssociation = BinaryAssociation(
    name="equality_expression378",
    ends={
        Property(name="ansic_equality_expression379", type=ansic_and_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_and_expression", type=ansic_equality_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
and_expression_linha380: BinaryAssociation = BinaryAssociation(
    name="and_expression_linha380",
    ends={
        Property(name="ansic_and_expression_linha", type=ansic_and_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_and_expression381", type=ansic_and_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
equality_expression382: BinaryAssociation = BinaryAssociation(
    name="equality_expression382",
    ends={
        Property(name="ansic_equality_expression384", type=ansic_and_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_and_expression_linha383", type=ansic_equality_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
and_expression_linha386: BinaryAssociation = BinaryAssociation(
    name="and_expression_linha386",
    ends={
        Property(name="ansic_and_expression_linha387", type=ansic_and_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_and_expression_linha385", type=ansic_and_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
and_expression388: BinaryAssociation = BinaryAssociation(
    name="and_expression388",
    ends={
        Property(name="ansic_and_expression389", type=ansic_exclusive_or_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_exclusive_or_expression", type=ansic_and_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exclusive_or_expression_linha390: BinaryAssociation = BinaryAssociation(
    name="exclusive_or_expression_linha390",
    ends={
        Property(name="ansic_exclusive_or_expression_linha", type=ansic_exclusive_or_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_exclusive_or_expression391", type=ansic_exclusive_or_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
and_expression392: BinaryAssociation = BinaryAssociation(
    name="and_expression392",
    ends={
        Property(name="ansic_and_expression394", type=ansic_exclusive_or_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_exclusive_or_expression_linha393", type=ansic_and_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exclusive_or_expression_linha396: BinaryAssociation = BinaryAssociation(
    name="exclusive_or_expression_linha396",
    ends={
        Property(name="ansic_exclusive_or_expression_linha397", type=ansic_exclusive_or_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_exclusive_or_expression_linha395", type=ansic_exclusive_or_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exclusive_or_expression398: BinaryAssociation = BinaryAssociation(
    name="exclusive_or_expression398",
    ends={
        Property(name="ansic_exclusive_or_expression399", type=ansic_inclusive_or_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_inclusive_or_expression", type=ansic_exclusive_or_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inclusive_or_expression_linha400: BinaryAssociation = BinaryAssociation(
    name="inclusive_or_expression_linha400",
    ends={
        Property(name="ansic_inclusive_or_expression_linha", type=ansic_inclusive_or_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_inclusive_or_expression401", type=ansic_inclusive_or_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exclusive_or_expression402: BinaryAssociation = BinaryAssociation(
    name="exclusive_or_expression402",
    ends={
        Property(name="ansic_exclusive_or_expression404", type=ansic_inclusive_or_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_inclusive_or_expression_linha403", type=ansic_exclusive_or_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression433: BinaryAssociation = BinaryAssociation(
    name="expression433",
    ends={
        Property(name="ansic_conditional_expression_linha434", type=ansic_expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="ansic_expression435", type=ansic_conditional_expression_linha, multiplicity=Multiplicity(1, 1))
    }
)
conditional_expression436: BinaryAssociation = BinaryAssociation(
    name="conditional_expression436",
    ends={
        Property(name="ansic_conditional_expression438", type=ansic_conditional_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_conditional_expression_linha437", type=ansic_conditional_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditional_expression_linha440: BinaryAssociation = BinaryAssociation(
    name="conditional_expression_linha440",
    ends={
        Property(name="ansic_conditional_expression_linha441", type=ansic_conditional_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_conditional_expression_linha439", type=ansic_conditional_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
logical_and_expression_linha416: BinaryAssociation = BinaryAssociation(
    name="logical_and_expression_linha416",
    ends={
        Property(name="ansic_logical_and_expression_linha417", type=ansic_logical_and_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_logical_and_expression_linha415", type=ansic_logical_and_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
logical_and_expression418: BinaryAssociation = BinaryAssociation(
    name="logical_and_expression418",
    ends={
        Property(name="ansic_logical_and_expression419", type=ansic_logical_or_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_logical_or_expression", type=ansic_logical_and_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
logical_or_expression_linha420: BinaryAssociation = BinaryAssociation(
    name="logical_or_expression_linha420",
    ends={
        Property(name="ansic_logical_or_expression_linha", type=ansic_logical_or_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_logical_or_expression421", type=ansic_logical_or_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
logical_and_expression422: BinaryAssociation = BinaryAssociation(
    name="logical_and_expression422",
    ends={
        Property(name="ansic_logical_and_expression424", type=ansic_logical_or_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_logical_or_expression_linha423", type=ansic_logical_and_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
logical_or_expression_linha426: BinaryAssociation = BinaryAssociation(
    name="logical_or_expression_linha426",
    ends={
        Property(name="ansic_logical_or_expression_linha427", type=ansic_logical_or_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_logical_or_expression_linha425", type=ansic_logical_or_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
logical_or_expression428: BinaryAssociation = BinaryAssociation(
    name="logical_or_expression428",
    ends={
        Property(name="ansic_logical_or_expression430", type=ansic_conditional_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_conditional_expression429", type=ansic_logical_or_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init_declarator_list_linha476: BinaryAssociation = BinaryAssociation(
    name="init_declarator_list_linha476",
    ends={
        Property(name="ansic_init_declarator_list_linha478", type=ansic_init_declarator_list, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_init_declarator_list477", type=ansic_init_declarator_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditional_expression_linha431: BinaryAssociation = BinaryAssociation(
    name="conditional_expression_linha431",
    ends={
        Property(name="ansic_conditional_expression_linha", type=ansic_conditional_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_conditional_expression432", type=ansic_conditional_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarator479: BinaryAssociation = BinaryAssociation(
    name="declarator479",
    ends={
        Property(name="ansic_declarator481", type=ansic_init_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_init_declarator480", type=ansic_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initializer482: BinaryAssociation = BinaryAssociation(
    name="initializer482",
    ends={
        Property(name="ansic_initializer484", type=ansic_init_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_init_declarator483", type=ansic_initializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditional_expression442: BinaryAssociation = BinaryAssociation(
    name="conditional_expression442",
    ends={
        Property(name="ansic_conditional_expression444", type=ansic_assignment_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_assignment_expression443", type=ansic_conditional_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unary_expression445: BinaryAssociation = BinaryAssociation(
    name="unary_expression445",
    ends={
        Property(name="ansic_unary_expression447", type=ansic_assignment_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_assignment_expression446", type=ansic_unary_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment_expression449: BinaryAssociation = BinaryAssociation(
    name="assignment_expression449",
    ends={
        Property(name="ansic_assignment_expression450", type=ansic_assignment_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_assignment_expression448", type=ansic_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initializer_list451: BinaryAssociation = BinaryAssociation(
    name="initializer_list451",
    ends={
        Property(name="ansic_initializer_list453", type=ansic_type_name, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_type_name452", type=ansic_initializer_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specifier_qualifier_list454: BinaryAssociation = BinaryAssociation(
    name="specifier_qualifier_list454",
    ends={
        Property(name="ansic_specifier_qualifier_list456", type=ansic_type_name, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_type_name455", type=ansic_specifier_qualifier_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
abstract_declarator457: BinaryAssociation = BinaryAssociation(
    name="abstract_declarator457",
    ends={
        Property(name="ansic_abstract_declarator459", type=ansic_type_name, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_type_name458", type=ansic_abstract_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment_expression460: BinaryAssociation = BinaryAssociation(
    name="assignment_expression460",
    ends={
        Property(name="ansic_assignment_expression462", type=ansic_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_expression461", type=ansic_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression_linha463: BinaryAssociation = BinaryAssociation(
    name="expression_linha463",
    ends={
        Property(name="ansic_expression_linha", type=ansic_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_expression464", type=ansic_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment_expression465: BinaryAssociation = BinaryAssociation(
    name="assignment_expression465",
    ends={
        Property(name="ansic_assignment_expression467", type=ansic_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_expression_linha466", type=ansic_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression_linha469: BinaryAssociation = BinaryAssociation(
    name="expression_linha469",
    ends={
        Property(name="ansic_expression_linha470", type=ansic_expression_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_expression_linha468", type=ansic_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditional_expression471: BinaryAssociation = BinaryAssociation(
    name="conditional_expression471",
    ends={
        Property(name="ansic_conditional_expression473", type=ansic_constant_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_constant_expression472", type=ansic_conditional_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init_declarator474: BinaryAssociation = BinaryAssociation(
    name="init_declarator474",
    ends={
        Property(name="ansic_init_declarator", type=ansic_init_declarator_list, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_init_declarator_list475", type=ansic_init_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
direct_abstract_declarator_complement512: BinaryAssociation = BinaryAssociation(
    name="direct_abstract_declarator_complement512",
    ends={
        Property(name="ansic_direct_abstract_declarator_complement513", type=ansic_DirectAbstractDeclarratorLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_DirectAbstractDeclarratorLinhaAction", type=ansic_direct_abstract_declarator_complement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
direct_abstract_declarator_linha514: BinaryAssociation = BinaryAssociation(
    name="direct_abstract_declarator_linha514",
    ends={
        Property(name="ansic_direct_abstract_declarator_linha516", type=ansic_DirectAbstractDeclarratorLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_DirectAbstractDeclarratorLinhaAction515", type=ansic_direct_abstract_declarator_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumerator485: BinaryAssociation = BinaryAssociation(
    name="enumerator485",
    ends={
        Property(name="ansic_enumerator486", type=ansic_EnumeratorListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_EnumeratorListLinhaAction", type=ansic_enumerator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumerator_list_linha487: BinaryAssociation = BinaryAssociation(
    name="enumerator_list_linha487",
    ends={
        Property(name="ansic_enumerator_list_linha489", type=ansic_EnumeratorListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_EnumeratorListLinhaAction488", type=ansic_enumerator_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_declaration_list490: BinaryAssociation = BinaryAssociation(
    name="struct_declaration_list490",
    ends={
        Property(name="ansic_struct_declaration_list491", type=ansic_StructOrUnionSpecifierComplementAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_StructOrUnionSpecifierComplementAction", type=ansic_struct_declaration_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_declaration492: BinaryAssociation = BinaryAssociation(
    name="struct_declaration492",
    ends={
        Property(name="ansic_struct_declaration493", type=ansic_StructDeclarationListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_StructDeclarationListLinhaAction", type=ansic_struct_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_declaration_list_linha494: BinaryAssociation = BinaryAssociation(
    name="struct_declaration_list_linha494",
    ends={
        Property(name="ansic_struct_declaration_list_linha496", type=ansic_StructDeclarationListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_StructDeclarationListLinhaAction495", type=ansic_struct_declaration_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_declarator497: BinaryAssociation = BinaryAssociation(
    name="struct_declarator497",
    ends={
        Property(name="ansic_struct_declarator498", type=ansic_StructDeclaratorListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_StructDeclaratorListLinhaAction", type=ansic_struct_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
struct_declarator_list_linha499: BinaryAssociation = BinaryAssociation(
    name="struct_declarator_list_linha499",
    ends={
        Property(name="ansic_struct_declarator_list_linha501", type=ansic_StructDeclaratorListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_StructDeclaratorListLinhaAction500", type=ansic_struct_declarator_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration502: BinaryAssociation = BinaryAssociation(
    name="declaration502",
    ends={
        Property(name="ansic_declaration503", type=ansic_DeclarationListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_DeclarationListLinhaAction", type=ansic_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration_list_linha504: BinaryAssociation = BinaryAssociation(
    name="declaration_list_linha504",
    ends={
        Property(name="ansic_declaration_list_linha506", type=ansic_DeclarationListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_DeclarationListLinhaAction505", type=ansic_declaration_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_qualifier507: BinaryAssociation = BinaryAssociation(
    name="type_qualifier507",
    ends={
        Property(name="ansic_type_qualifier508", type=ansic_TypeQualifierListLinhaAtion, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_TypeQualifierListLinhaAtion", type=ansic_type_qualifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_qualifier_list_linha509: BinaryAssociation = BinaryAssociation(
    name="type_qualifier_list_linha509",
    ends={
        Property(name="ansic_type_qualifier_list_linha511", type=ansic_TypeQualifierListLinhaAtion, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_TypeQualifierListLinhaAtion510", type=ansic_type_qualifier_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment_expression544: BinaryAssociation = BinaryAssociation(
    name="assignment_expression544",
    ends={
        Property(name="ansic_ArgumentExpressionListLinhaAction", type=ansic_assignment_expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="ansic_assignment_expression545", type=ansic_ArgumentExpressionListLinhaAction, multiplicity=Multiplicity(1, 1))
    }
)
argument_expression_list_linha546: BinaryAssociation = BinaryAssociation(
    name="argument_expression_list_linha546",
    ends={
        Property(name="ansic_argument_expression_list_linha", type=ansic_ArgumentExpressionListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_ArgumentExpressionListLinhaAction547", type=ansic_argument_expression_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier_list_linha517: BinaryAssociation = BinaryAssociation(
    name="identifier_list_linha517",
    ends={
        Property(name="ansic_identifier_list_linha518", type=ansic_IdentifierListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_IdentifierListLinhaAction", type=ansic_identifier_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
external_declaration519: BinaryAssociation = BinaryAssociation(
    name="external_declaration519",
    ends={
        Property(name="ansic_external_declaration520", type=ansic_TranlationUnitLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_TranlationUnitLinhaAction", type=ansic_external_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
translation_unit_linha521: BinaryAssociation = BinaryAssociation(
    name="translation_unit_linha521",
    ends={
        Property(name="ansic_translation_unit_linha523", type=ansic_TranlationUnitLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_TranlationUnitLinhaAction522", type=ansic_translation_unit_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
generic_association524: BinaryAssociation = BinaryAssociation(
    name="generic_association524",
    ends={
        Property(name="ansic_generic_association525", type=ansic_GenericAssocListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_GenericAssocListLinhaAction", type=ansic_generic_association, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
generic_assoc_list_linha526: BinaryAssociation = BinaryAssociation(
    name="generic_assoc_list_linha526",
    ends={
        Property(name="ansic_generic_assoc_list_linha528", type=ansic_GenericAssocListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_GenericAssocListLinhaAction527", type=ansic_generic_assoc_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postfix_expression_complement529: BinaryAssociation = BinaryAssociation(
    name="postfix_expression_complement529",
    ends={
        Property(name="ansic_postfix_expression_complement530", type=ansic_PostfixExpressionLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_PostfixExpressionLinhaAction", type=ansic_postfix_expression_complement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postfix_expression_linha531: BinaryAssociation = BinaryAssociation(
    name="postfix_expression_linha531",
    ends={
        Property(name="ansic_postfix_expression_linha533", type=ansic_PostfixExpressionLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_PostfixExpressionLinhaAction532", type=ansic_postfix_expression_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initializer_list_complement534: BinaryAssociation = BinaryAssociation(
    name="initializer_list_complement534",
    ends={
        Property(name="ansic_initializer_list_complement535", type=ansic_InitializerListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_InitializerListLinhaAction", type=ansic_initializer_list_complement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init_declarator_list_linha536: BinaryAssociation = BinaryAssociation(
    name="init_declarator_list_linha536",
    ends={
        Property(name="ansic_init_declarator_list_linha538", type=ansic_InitializerListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_InitializerListLinhaAction537", type=ansic_init_declarator_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
designator539: BinaryAssociation = BinaryAssociation(
    name="designator539",
    ends={
        Property(name="ansic_designator540", type=ansic_DesignatorListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_DesignatorListLinhaAction", type=ansic_designator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
designator_list_linha541: BinaryAssociation = BinaryAssociation(
    name="designator_list_linha541",
    ends={
        Property(name="ansic_declaration_list_linha543", type=ansic_DesignatorListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_DesignatorListLinhaAction542", type=ansic_declaration_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init_declarator548: BinaryAssociation = BinaryAssociation(
    name="init_declarator548",
    ends={
        Property(name="ansic_init_declarator549", type=ansic_InitDecclaratorListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_InitDecclaratorListLinhaAction", type=ansic_init_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init_declarator_list_linha550: BinaryAssociation = BinaryAssociation(
    name="init_declarator_list_linha550",
    ends={
        Property(name="ansic_init_declarator_list_linha552", type=ansic_InitDecclaratorListLinhaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ansic_InitDecclaratorListLinhaAction551", type=ansic_init_declarator_list_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_ansic_type_qualifier_list_direct_abstract_declarator_complement = Generalization(general=direct_abstract_declarator_complement, specific=ansic_type_qualifier_list)
gen_ansic_type_name_postfix_expression = Generalization(general=postfix_expression, specific=ansic_type_name)
gen_ansic_DirectAbstractDeclarratorLinhaAction_direct_abstract_declarator_linha = Generalization(general=direct_abstract_declarator_linha, specific=ansic_DirectAbstractDeclarratorLinhaAction)
gen_ansic_IdentifierListLinhaAction_identifier_list_linha = Generalization(general=identifier_list_linha, specific=ansic_IdentifierListLinhaAction)
gen_ansic_EnumeratorListLinhaAction_enumerator_list_linha = Generalization(general=enumerator_list_linha, specific=ansic_EnumeratorListLinhaAction)
gen_ansic_StructOrUnionSpecifierComplementAction_struct_or_union_specifier_complement = Generalization(general=struct_or_union_specifier_complement, specific=ansic_StructOrUnionSpecifierComplementAction)
gen_ansic_StructDeclarationListLinhaAction_struct_declaration_list_linha = Generalization(general=struct_declaration_list_linha, specific=ansic_StructDeclarationListLinhaAction)
gen_ansic_StructDeclaratorListLinhaAction_struct_declarator_list_linha = Generalization(general=struct_declarator_list_linha, specific=ansic_StructDeclaratorListLinhaAction)
gen_ansic_DeclarationListLinhaAction_declaration_list_linha = Generalization(general=declaration_list_linha, specific=ansic_DeclarationListLinhaAction)
gen_ansic_TypeQualifierListLinhaAtion_type_qualifier_list_linha = Generalization(general=type_qualifier_list_linha, specific=ansic_TypeQualifierListLinhaAtion)
gen_ansic_PlusPlus_unary_expression = Generalization(general=unary_expression, specific=ansic_PlusPlus)
gen_ansic_TranlationUnitLinhaAction_translation_unit_linha = Generalization(general=translation_unit_linha, specific=ansic_TranlationUnitLinhaAction)
gen_ansic_GenericAssocListLinhaAction_generic_assoc_list_linha = Generalization(general=generic_assoc_list_linha, specific=ansic_GenericAssocListLinhaAction)
gen_ansic_PostfixExpressionLinhaAction_postfix_expression_linha = Generalization(general=postfix_expression_linha, specific=ansic_PostfixExpressionLinhaAction)
gen_ansic_InitializerListLinhaAction_initializer_list_linha = Generalization(general=initializer_list_linha, specific=ansic_InitializerListLinhaAction)
gen_ansic_DesignatorListLinhaAction_designator_list_linha = Generalization(general=designator_list_linha, specific=ansic_DesignatorListLinhaAction)
gen_ansic_PostFixEmpryParams_postfix_expression_complement = Generalization(general=postfix_expression_complement, specific=ansic_PostFixEmpryParams)
gen_ansic_ArgumentExpressionListLinhaAction_argument_expression_list_linha = Generalization(general=argument_expression_list_linha, specific=ansic_ArgumentExpressionListLinhaAction)
gen_ansic_InitDecclaratorListLinhaAction_init_declarator_list_linha = Generalization(general=init_declarator_list_linha, specific=ansic_InitDecclaratorListLinhaAction)

# Domain Model
domain_model = DomainModel(
    name="ansic",
    types={ansic_declaration_specifiers, ansic_type_specifier, ansic_DomainModel, ansic_translation_unit, ansic_external_declaration, ansic_translation_unit_linha, ansic_function_definition, ansic_declaration, ansic_struct_declaration_list, ansic_struct_or_union_specifier_complement, ansic_type_qualifier, ansic_alignment_specifier, ansic_type_name, ansic_constant_expression, ansic_atomic_type_specifier, ansic_struct_or_union_specifier, ansic_enum_specifier, ansic_enumerator_list, ansic_enumerator, ansic_enumerator_list_linha, ansic_enumeration_constant, ansic_struct_declaration, ansic_struct_declaration_list_linha, ansic_specifier_qualifier_list, ansic_struct_declarator_list, ansic_static_assert_declaration, ansic_struct_declarator, ansic_struct_declarator_list_linha, ansic_declarator, ansic_init_declarator_list, ansic_declaration_list, ansic_compound_statement, ansic_declaration_list_linha, ansic_pointer, ansic_direct_declarator, ansic_type_qualifier_list, direct_abstract_declarator_complement, ansic_type_qualifier_list_linha, ansic_direct_declarator_linha, ansic_direct_declarator_complemento, ansic_assignment_expression, ansic_direct_abstract_declarator_linha, ansic_parameter_type_list, ansic_initializer, ansic_identifier_list, ansic_parameter_lista, ansic_parameter_declaration, ansic_parameter_list_linha, ansic_abstract_declarator, ansic_direct_abstract_declarator, ansic_generic_assoc_list, ansic_generic_association, ansic_generic_assoc_list_linha, ansic_initializer_list, ansic_direct_abstract_declarator_complement, ansic_identifier_list_linha, ansic_primary_expression, ansic_constant, ansic_expression, ansic_generic_selection, ansic_conditional_expression, ansic_postfix_expression_complement, ansic_postfix_expression, ansic_postfix_expression_linha, ansic_designation, ansic_init_declarator_list_linha, ansic_initializer_list_linha, ansic_initializer_list_complement, ansic_designator_list, ansic_designator, ansic_designator_list_linha, ansic_multiplicative_expression_complement, ansic_additive_expression, ansic_argument_expression_list, ansic_argument_expression_list_linha, ansic_unary_expression, ansic_cast_expression, ansic_multiplicative_expression, ansic_multiplicative_expression_linha, ansic_relational_expression_complement, ansic_equality_expression, ansic_equality_expression_linha, ansic_additive_expression_linha, ansic_additive_expression_complement, ansic_shift_expression, ansic_shift_expression_linha, ansic_shift_expression_complement, ansic_relational_expression, ansic_relational_expression_linha, ansic_equality_expression_complement, ansic_statement, ansic_labeled_statement, ansic_expression_statement, ansic_selection_statement, ansic_iteration_statement, ansic_jump_statement, ansic_block_item_list, ansic_block_item, ansic_block_item_list_linha, ansic_logical_and_expression, ansic_logical_and_expression_linha, ansic_and_expression, ansic_and_expression_linha, ansic_exclusive_or_expression, ansic_exclusive_or_expression_linha, ansic_inclusive_or_expression, ansic_inclusive_or_expression_linha, ansic_logical_or_expression, ansic_logical_or_expression_linha, ansic_conditional_expression_linha, postfix_expression, ansic_expression_linha, ansic_init_declarator, ansic_IdentifierListLinhaAction, identifier_list_linha, ansic_string_ufcg, ansic_EnumeratorListLinhaAction, enumerator_list_linha, ansic_StructOrUnionSpecifierComplementAction, struct_or_union_specifier_complement, ansic_StructDeclarationListLinhaAction, struct_declaration_list_linha, ansic_StructDeclaratorListLinhaAction, struct_declarator_list_linha, ansic_DeclarationListLinhaAction, declaration_list_linha, ansic_TypeQualifierListLinhaAtion, type_qualifier_list_linha, ansic_DirectAbstractDeclarratorLinhaAction, direct_abstract_declarator_linha, ansic_PlusPlus, unary_expression, ansic_TranlationUnitLinhaAction, translation_unit_linha, ansic_GenericAssocListLinhaAction, generic_assoc_list_linha, ansic_PostfixExpressionLinhaAction, postfix_expression_linha, ansic_InitializerListLinhaAction, initializer_list_linha, ansic_DesignatorListLinhaAction, designator_list_linha, ansic_PostFixEmpryParams, postfix_expression_complement, ansic_ArgumentExpressionListLinhaAction, argument_expression_list_linha, ansic_InitDecclaratorListLinhaAction, init_declarator_list_linha},
    associations={declaration_specifiers10, type_specifier11, geetings0, external_declaration1, translation_unit_linha3, function_definitio5, declaration7, struct_declaration_list41, struct_or_union_specifier_complement43, type_qualifier13, alignment_specifier15, type_name17, constant_expression19, atomic_type_specifier21, struct_or_union_specifier23, enum_specifier25, enumerator_list27, enumarator29, enumerator_list_linha31, enumeration_constant33, conditional_expression35, type_name38, static_assert_declaration78, declaration_specifiers81, struct_declaration45, struct_declaration_list_linha47, specifier_qualifier_list49, struct_declarator_list51, static_assert_declaration53, struct_declarator55, struct_declarator_list_linha57, constant_expression59, declarator62, type_specifier64, specifier_qualifier_list68, type_qualifier70, declaration_specifiers73, init_declarator_list76, direct_declarator_linha118, type_qualifier_list120, declarator84, declaration_list87, compound_statement89, declaration91, declaration_list_linha94, pointer96, direct_declarator98, type_qualifier_list100, pointer103, type_qualifier105, type_qualifier_list_linha108, direct_declarator_linha110, declarator112, direct_declarator_complemento115, type_qualifier_list154, assignment_expression157, parameter_type_list160, assignment_expression123, direct_abstract_declarator_linha163, parameter_type_list125, identifier_list127, parameter_lista129, parameter_declarations131, parameter_declaration133, parameter_list_linha136, declaration_specifiers138, declarator141, abstract_declarator144, pointer146, direct_abstract_declarator149, abstract_declarator151, generic_assoc_list187, generic_association189, generic_assoc_list_linha191, init_declarator_list165, assignment_expression166, assignment_expression169, type_qualifier_list171, parameter_type_list174, identifier_list_linha177, constant179, expression180, generic_selection182, assignment_expression184, constant_expression221, constant_expression223, type_name193, assignment_expression196, primary_expression199, postfix_expression_linha201, designation203, initializer205, init_declarator_list_linha208, designation210, initializer212, designator_list215, designator217, designator_list_linha219, multiplicative_expression_complement256, multiplicative_expression_linha259, cast_expression261, expression226, argument_expression_list228, assignment_expressions230, postfix_expression233, unary_expression236, cast_expression238, type_name240, unary_expression243, type_name246, cast_expression250, cast_expression252, multiplicative_expression_linha254, relational_expression_linha296, shift_expression298, relational_expression300, equality_expression_linha302, multiplicative_expression264, additive_expression_linha266, additive_expression_complement268, additive_expression_linha271, multiplicative_expression273, additive_expression276, shift_expression_linha278, shift_expression_complement280, shift_expression_linha283, additive_expression285, shift_expression288, relational_expression_linha290, shift_expression_complement292, expression324, expression327, equality_expression_complement304, equality_expression_linha307, relational_expression309, labeled_statement312, compound_statement313, expression_statement316, selection_statement318, iteration_statement320, jump_statement322, block_item_list_linha367, declaration369, statement372, statement330, expression375, expression_statement333, expression_statement2336, declaration339, expression342, statement345, statement2348, statement351, conditional_expression354, block_item_list357, block_item359, block_item_list_linha361, block_item363, inclusive_or_expression_linha406, inclusive_or_expression408, logical_and_expression_linha410, inclusive_or_expression412, equality_expression378, and_expression_linha380, equality_expression382, and_expression_linha386, and_expression388, exclusive_or_expression_linha390, and_expression392, exclusive_or_expression_linha396, exclusive_or_expression398, inclusive_or_expression_linha400, exclusive_or_expression402, expression433, conditional_expression436, conditional_expression_linha440, logical_and_expression_linha416, logical_and_expression418, logical_or_expression_linha420, logical_and_expression422, logical_or_expression_linha426, logical_or_expression428, init_declarator_list_linha476, conditional_expression_linha431, declarator479, initializer482, conditional_expression442, unary_expression445, assignment_expression449, initializer_list451, specifier_qualifier_list454, abstract_declarator457, assignment_expression460, expression_linha463, assignment_expression465, expression_linha469, conditional_expression471, init_declarator474, direct_abstract_declarator_complement512, direct_abstract_declarator_linha514, enumerator485, enumerator_list_linha487, struct_declaration_list490, struct_declaration492, struct_declaration_list_linha494, struct_declarator497, struct_declarator_list_linha499, declaration502, declaration_list_linha504, type_qualifier507, type_qualifier_list_linha509, assignment_expression544, argument_expression_list_linha546, identifier_list_linha517, external_declaration519, translation_unit_linha521, generic_association524, generic_assoc_list_linha526, postfix_expression_complement529, postfix_expression_linha531, initializer_list_complement534, init_declarator_list_linha536, designator539, designator_list_linha541, init_declarator548, init_declarator_list_linha550},
    generalizations={gen_ansic_type_qualifier_list_direct_abstract_declarator_complement, gen_ansic_type_name_postfix_expression, gen_ansic_DirectAbstractDeclarratorLinhaAction_direct_abstract_declarator_linha, gen_ansic_IdentifierListLinhaAction_identifier_list_linha, gen_ansic_EnumeratorListLinhaAction_enumerator_list_linha, gen_ansic_StructOrUnionSpecifierComplementAction_struct_or_union_specifier_complement, gen_ansic_StructDeclarationListLinhaAction_struct_declaration_list_linha, gen_ansic_StructDeclaratorListLinhaAction_struct_declarator_list_linha, gen_ansic_DeclarationListLinhaAction_declaration_list_linha, gen_ansic_TypeQualifierListLinhaAtion_type_qualifier_list_linha, gen_ansic_PlusPlus_unary_expression, gen_ansic_TranlationUnitLinhaAction_translation_unit_linha, gen_ansic_GenericAssocListLinhaAction_generic_assoc_list_linha, gen_ansic_PostfixExpressionLinhaAction_postfix_expression_linha, gen_ansic_InitializerListLinhaAction_initializer_list_linha, gen_ansic_DesignatorListLinhaAction_designator_list_linha, gen_ansic_PostFixEmpryParams_postfix_expression_complement, gen_ansic_ArgumentExpressionListLinhaAction_argument_expression_list_linha, gen_ansic_InitDecclaratorListLinhaAction_init_declarator_list_linha},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)