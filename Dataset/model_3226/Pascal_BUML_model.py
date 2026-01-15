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
pascal_pascal = Class(name="pascal::pascal")
pascal_program = Class(name="pascal::program")
pascal_programHeading = Class(name="pascal::programHeading")
pascal_block = Class(name="pascal::block")
pascal_identifier = Class(name="pascal::identifier")
pascal_identifierList = Class(name="pascal::identifierList")
pascal_label_declaration_part = Class(name="pascal::label::declaration::part")
pascal_constantDefinitionPart = Class(name="pascal::constantDefinitionPart")
pascal_typeDefinitionPart = Class(name="pascal::typeDefinitionPart")
pascal_variableDeclarationPart = Class(name="pascal::variableDeclarationPart")
pascal_procedureAndFunctionDeclarationPart = Class(name="pascal::procedureAndFunctionDeclarationPart")
pascal_usesUnitsPart = Class(name="pascal::usesUnitsPart")
pascal_compoundStatement = Class(name="pascal::compoundStatement")
pascal_label = Class(name="pascal::label")
label_declaration_part = Class(name="label::declaration::part")
statement = Class(name="statement")
pascal_unsignedInteger = Class(name="pascal::unsignedInteger")
pascal_constantDefinition = Class(name="pascal::constantDefinition")
pascal_constant = Class(name="pascal::constant")
variant = Class(name="variant")
pascal_unsignedNumber = Class(name="pascal::unsignedNumber")
pascal_constantChr = Class(name="pascal::constantChr")
pascal_fieldList = Class(name="pascal::fieldList")
pascal_typeDefinition = Class(name="pascal::typeDefinition")
pascal_type = Class(name="pascal::type")
pascal_functionType = Class(name="pascal::functionType")
pascal_procedureType = Class(name="pascal::procedureType")
pascal_formalParameterList = Class(name="pascal::formalParameterList")
pascal_typeIdentifier = Class(name="pascal::typeIdentifier")
pascal_parameterGroup = Class(name="pascal::parameterGroup")
pascal_formalParameterSection = Class(name="pascal::formalParameterSection")
pascal_simpleType = Class(name="pascal::simpleType")
pascal_structuredType = Class(name="pascal::structuredType")
pascal_pointerType = Class(name="pascal::pointerType")
pascal_scalarType = Class(name="pascal::scalarType")
pascal_subrangeType = Class(name="pascal::subrangeType")
pascal_stringtype = Class(name="pascal::stringtype")
pascal_unpackedStructuredType = Class(name="pascal::unpackedStructuredType")
pascal_recordType = Class(name="pascal::recordType")
pascal_fixedPart = Class(name="pascal::fixedPart")
pascal_variantPart = Class(name="pascal::variantPart")
pascal_recordSection = Class(name="pascal::recordSection")
pascal_tag = Class(name="pascal::tag")
pascal_variant = Class(name="pascal::variant")
pascal_constList = Class(name="pascal::constList")
pascal_variableDeclaration = Class(name="pascal::variableDeclaration")
pascal_expression = Class(name="pascal::expression")
pascal_procedureOrFunctionDeclaration = Class(name="pascal::procedureOrFunctionDeclaration")
pascal_procedureDeclaration = Class(name="pascal::procedureDeclaration")
pascal_functionDeclaration = Class(name="pascal::functionDeclaration")
pascal_statement = Class(name="pascal::statement")
pascal_unlabelledStatement = Class(name="pascal::unlabelledStatement")
pascal_simpleStatement = Class(name="pascal::simpleStatement")
pascal_structuredStatement = Class(name="pascal::structuredStatement")
pascal_parameterList = Class(name="pascal::parameterList")
pascal_gotoStatement = Class(name="pascal::gotoStatement")
pascal_assignmentStatement = Class(name="pascal::assignmentStatement")
pascal_variable = Class(name="pascal::variable")
pascal_simpleExpression = Class(name="pascal::simpleExpression")
pascal_term = Class(name="pascal::term")
pascal_signedFactor = Class(name="pascal::signedFactor")
pascal_factor = Class(name="pascal::factor")
pascal_unsignedConstant = Class(name="pascal::unsignedConstant")
pascal_functionDesignator = Class(name="pascal::functionDesignator")
pascal_actualParameter = Class(name="pascal::actualParameter")
parameterList = Class(name="parameterList")
pascal_conditionalStatement = Class(name="pascal::conditionalStatement")
pascal_statements = Class(name="pascal::statements")
pascal_caseStatement = Class(name="pascal::caseStatement")
pascal_caseListElement = Class(name="pascal::caseListElement")

# pascal_pascal class attributes and methods

# pascal_program class attributes and methods

# pascal_programHeading class attributes and methods

# pascal_block class attributes and methods

# pascal_identifier class attributes and methods
pascal_identifier_identifier: Property = Property(name="identifier", type=StringType)
pascal_identifier.attributes={pascal_identifier_identifier}

# pascal_identifierList class attributes and methods

# pascal_label_declaration_part class attributes and methods

# pascal_constantDefinitionPart class attributes and methods

# pascal_typeDefinitionPart class attributes and methods

# pascal_variableDeclarationPart class attributes and methods

# pascal_procedureAndFunctionDeclarationPart class attributes and methods

# pascal_usesUnitsPart class attributes and methods

# pascal_compoundStatement class attributes and methods

# pascal_label class attributes and methods

# label_declaration_part class attributes and methods

# statement class attributes and methods

# pascal_unsignedInteger class attributes and methods
pascal_unsignedInteger_number: Property = Property(name="number", type=StringType)
pascal_unsignedInteger.attributes={pascal_unsignedInteger_number}

# pascal_constantDefinition class attributes and methods

# pascal_constant class attributes and methods
pascal_constant_sign: Property = Property(name="sign", type=StringType)
pascal_constant_string: Property = Property(name="string", type=StringType)
pascal_constant_bool: Property = Property(name="bool", type=StringType)
pascal_constant.attributes={pascal_constant_string, pascal_constant_bool, pascal_constant_sign}

# variant class attributes and methods

# pascal_unsignedNumber class attributes and methods
pascal_unsignedNumber_unsignedReal: Property = Property(name="unsignedReal", type=StringType)
pascal_unsignedNumber.attributes={pascal_unsignedNumber_unsignedReal}

# pascal_constantChr class attributes and methods

# pascal_fieldList class attributes and methods

# pascal_typeDefinition class attributes and methods

# pascal_type class attributes and methods

# pascal_functionType class attributes and methods

# pascal_procedureType class attributes and methods

# pascal_formalParameterList class attributes and methods

# pascal_typeIdentifier class attributes and methods
pascal_typeIdentifier_char: Property = Property(name="char", type=StringType)
pascal_typeIdentifier_boolean: Property = Property(name="boolean", type=StringType)
pascal_typeIdentifier_integer: Property = Property(name="integer", type=StringType)
pascal_typeIdentifier_real: Property = Property(name="real", type=StringType)
pascal_typeIdentifier_string: Property = Property(name="string", type=StringType)
pascal_typeIdentifier.attributes={pascal_typeIdentifier_string, pascal_typeIdentifier_char, pascal_typeIdentifier_integer, pascal_typeIdentifier_real, pascal_typeIdentifier_boolean}

# pascal_parameterGroup class attributes and methods

# pascal_formalParameterSection class attributes and methods

# pascal_simpleType class attributes and methods

# pascal_structuredType class attributes and methods

# pascal_pointerType class attributes and methods

# pascal_scalarType class attributes and methods

# pascal_subrangeType class attributes and methods

# pascal_stringtype class attributes and methods

# pascal_unpackedStructuredType class attributes and methods

# pascal_recordType class attributes and methods

# pascal_fixedPart class attributes and methods

# pascal_variantPart class attributes and methods

# pascal_recordSection class attributes and methods

# pascal_tag class attributes and methods

# pascal_variant class attributes and methods

# pascal_constList class attributes and methods

# pascal_variableDeclaration class attributes and methods

# pascal_expression class attributes and methods
pascal_expression_relationaloperator: Property = Property(name="relationaloperator", type=StringType)
pascal_expression.attributes={pascal_expression_relationaloperator}

# pascal_procedureOrFunctionDeclaration class attributes and methods

# pascal_procedureDeclaration class attributes and methods

# pascal_functionDeclaration class attributes and methods

# pascal_statement class attributes and methods

# pascal_unlabelledStatement class attributes and methods

# pascal_simpleStatement class attributes and methods

# pascal_structuredStatement class attributes and methods

# pascal_parameterList class attributes and methods

# pascal_gotoStatement class attributes and methods

# pascal_assignmentStatement class attributes and methods

# pascal_variable class attributes and methods

# pascal_simpleExpression class attributes and methods
pascal_simpleExpression_additiveoperator: Property = Property(name="additiveoperator", type=StringType)
pascal_simpleExpression.attributes={pascal_simpleExpression_additiveoperator}

# pascal_term class attributes and methods
pascal_term_multiplicativeoperator: Property = Property(name="multiplicativeoperator", type=StringType)
pascal_term.attributes={pascal_term_multiplicativeoperator}

# pascal_signedFactor class attributes and methods

# pascal_factor class attributes and methods
pascal_factor_bool: Property = Property(name="bool", type=StringType)
pascal_factor.attributes={pascal_factor_bool}

# pascal_unsignedConstant class attributes and methods
pascal_unsignedConstant_string_literal: Property = Property(name="string_literal", type=StringType)
pascal_unsignedConstant.attributes={pascal_unsignedConstant_string_literal}

# pascal_functionDesignator class attributes and methods

# pascal_actualParameter class attributes and methods

# parameterList class attributes and methods

# pascal_conditionalStatement class attributes and methods

# pascal_statements class attributes and methods

# pascal_caseStatement class attributes and methods

# pascal_caseListElement class attributes and methods

# Relationships
program0: BinaryAssociation = BinaryAssociation(
    name="program0",
    ends={
        Property(name="pascal_program", type=pascal_pascal, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_pascal", type=pascal_program, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
head1: BinaryAssociation = BinaryAssociation(
    name="head1",
    ends={
        Property(name="pascal_programHeading", type=pascal_program, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_program2", type=pascal_programHeading, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block3: BinaryAssociation = BinaryAssociation(
    name="block3",
    ends={
        Property(name="pascal_block", type=pascal_program, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_program4", type=pascal_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifer5: BinaryAssociation = BinaryAssociation(
    name="identifer5",
    ends={
        Property(name="pascal_identifier", type=pascal_programHeading, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_programHeading6", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifierList7: BinaryAssociation = BinaryAssociation(
    name="identifierList7",
    ends={
        Property(name="pascal_identifierList", type=pascal_programHeading, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_programHeading8", type=pascal_identifierList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier9: BinaryAssociation = BinaryAssociation(
    name="identifier9",
    ends={
        Property(name="pascal_identifier11", type=pascal_identifierList, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_identifierList10", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifierList112: BinaryAssociation = BinaryAssociation(
    name="identifierList112",
    ends={
        Property(name="pascal_identifier14", type=pascal_identifierList, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_identifierList13", type=pascal_identifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label15: BinaryAssociation = BinaryAssociation(
    name="label15",
    ends={
        Property(name="pascal_label_declaration_part", type=pascal_block, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_block16", type=pascal_label_declaration_part, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constantDefinitionParts17: BinaryAssociation = BinaryAssociation(
    name="constantDefinitionParts17",
    ends={
        Property(name="pascal_constantDefinitionPart", type=pascal_block, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_block18", type=pascal_constantDefinitionPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeDefinitionParts19: BinaryAssociation = BinaryAssociation(
    name="typeDefinitionParts19",
    ends={
        Property(name="pascal_typeDefinitionPart", type=pascal_block, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_block20", type=pascal_typeDefinitionPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variableDeclarationParts21: BinaryAssociation = BinaryAssociation(
    name="variableDeclarationParts21",
    ends={
        Property(name="pascal_variableDeclarationPart", type=pascal_block, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_block22", type=pascal_variableDeclarationPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
procedureAndFunctionDeclarationParts23: BinaryAssociation = BinaryAssociation(
    name="procedureAndFunctionDeclarationParts23",
    ends={
        Property(name="pascal_procedureAndFunctionDeclarationPart", type=pascal_block, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_block24", type=pascal_procedureAndFunctionDeclarationPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usesUnitsParts25: BinaryAssociation = BinaryAssociation(
    name="usesUnitsParts25",
    ends={
        Property(name="pascal_usesUnitsPart", type=pascal_block, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_block26", type=pascal_usesUnitsPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compoundStatement27: BinaryAssociation = BinaryAssociation(
    name="compoundStatement27",
    ends={
        Property(name="pascal_compoundStatement", type=pascal_block, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_block28", type=pascal_compoundStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
label30: BinaryAssociation = BinaryAssociation(
    name="label30",
    ends={
        Property(name="pascal_label", type=pascal_label, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_label29", type=pascal_label, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unsignedInteger31: BinaryAssociation = BinaryAssociation(
    name="unsignedInteger31",
    ends={
        Property(name="pascal_unsignedInteger", type=pascal_label, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_label32", type=pascal_unsignedInteger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier33: BinaryAssociation = BinaryAssociation(
    name="identifier33",
    ends={
        Property(name="pascal_identifier35", type=pascal_label, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_label34", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constantDefinition36: BinaryAssociation = BinaryAssociation(
    name="constantDefinition36",
    ends={
        Property(name="pascal_constantDefinition", type=pascal_constantDefinitionPart, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_constantDefinitionPart37", type=pascal_constantDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifier38: BinaryAssociation = BinaryAssociation(
    name="identifier38",
    ends={
        Property(name="pascal_identifier40", type=pascal_constantDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_constantDefinition39", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant41: BinaryAssociation = BinaryAssociation(
    name="constant41",
    ends={
        Property(name="pascal_constant", type=pascal_constantDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_constantDefinition42", type=pascal_constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unsignedNumber43: BinaryAssociation = BinaryAssociation(
    name="unsignedNumber43",
    ends={
        Property(name="pascal_unsignedNumber", type=pascal_constant, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_constant44", type=pascal_unsignedNumber, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier45: BinaryAssociation = BinaryAssociation(
    name="identifier45",
    ends={
        Property(name="pascal_identifier47", type=pascal_constant, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_constant46", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constantChr48: BinaryAssociation = BinaryAssociation(
    name="constantChr48",
    ends={
        Property(name="pascal_constantChr", type=pascal_constant, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_constant49", type=pascal_constantChr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant51: BinaryAssociation = BinaryAssociation(
    name="constant51",
    ends={
        Property(name="pascal_constant52", type=pascal_constant, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_constant50", type=pascal_constant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fieldList53: BinaryAssociation = BinaryAssociation(
    name="fieldList53",
    ends={
        Property(name="pascal_fieldList", type=pascal_constant, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_constant54", type=pascal_fieldList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unsignedInteger55: BinaryAssociation = BinaryAssociation(
    name="unsignedInteger55",
    ends={
        Property(name="pascal_unsignedInteger57", type=pascal_constantChr, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_constantChr56", type=pascal_unsignedInteger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unsignedInteger58: BinaryAssociation = BinaryAssociation(
    name="unsignedInteger58",
    ends={
        Property(name="pascal_unsignedInteger60", type=pascal_unsignedNumber, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unsignedNumber59", type=pascal_unsignedInteger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifierList61: BinaryAssociation = BinaryAssociation(
    name="identifierList61",
    ends={
        Property(name="pascal_identifierList63", type=pascal_usesUnitsPart, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_usesUnitsPart62", type=pascal_identifierList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeDefinition64: BinaryAssociation = BinaryAssociation(
    name="typeDefinition64",
    ends={
        Property(name="pascal_typeDefinition", type=pascal_typeDefinitionPart, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_typeDefinitionPart65", type=pascal_typeDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeDefinition166: BinaryAssociation = BinaryAssociation(
    name="typeDefinition166",
    ends={
        Property(name="pascal_typeDefinition68", type=pascal_typeDefinitionPart, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_typeDefinitionPart67", type=pascal_typeDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifier69: BinaryAssociation = BinaryAssociation(
    name="identifier69",
    ends={
        Property(name="pascal_identifier71", type=pascal_typeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_typeDefinition70", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type72: BinaryAssociation = BinaryAssociation(
    name="type72",
    ends={
        Property(name="pascal_type", type=pascal_typeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_typeDefinition73", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functionType74: BinaryAssociation = BinaryAssociation(
    name="functionType74",
    ends={
        Property(name="pascal_functionType", type=pascal_typeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_typeDefinition75", type=pascal_functionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
procedureType76: BinaryAssociation = BinaryAssociation(
    name="procedureType76",
    ends={
        Property(name="pascal_procedureType", type=pascal_typeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_typeDefinition77", type=pascal_procedureType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameterList78: BinaryAssociation = BinaryAssociation(
    name="formalParameterList78",
    ends={
        Property(name="pascal_formalParameterList", type=pascal_functionType, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_functionType79", type=pascal_formalParameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeIdentifier80: BinaryAssociation = BinaryAssociation(
    name="typeIdentifier80",
    ends={
        Property(name="pascal_typeIdentifier", type=pascal_functionType, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_functionType81", type=pascal_typeIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameterSection82: BinaryAssociation = BinaryAssociation(
    name="formalParameterSection82",
    ends={
        Property(name="pascal_formalParameterList83", type=pascal_formalParameterSection, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="pascal_formalParameterSection", type=pascal_formalParameterList, multiplicity=Multiplicity(1, 1))
    }
)
formalParameterSection284: BinaryAssociation = BinaryAssociation(
    name="formalParameterSection284",
    ends={
        Property(name="pascal_formalParameterSection86", type=pascal_formalParameterList, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_formalParameterList85", type=pascal_formalParameterSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterGroup87: BinaryAssociation = BinaryAssociation(
    name="parameterGroup87",
    ends={
        Property(name="pascal_parameterGroup", type=pascal_formalParameterSection, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_formalParameterSection88", type=pascal_parameterGroup, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterGroup289: BinaryAssociation = BinaryAssociation(
    name="parameterGroup289",
    ends={
        Property(name="pascal_parameterGroup91", type=pascal_formalParameterSection, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_formalParameterSection90", type=pascal_parameterGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterGroup392: BinaryAssociation = BinaryAssociation(
    name="parameterGroup392",
    ends={
        Property(name="pascal_parameterGroup94", type=pascal_formalParameterSection, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_formalParameterSection93", type=pascal_parameterGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterGroup495: BinaryAssociation = BinaryAssociation(
    name="parameterGroup495",
    ends={
        Property(name="pascal_parameterGroup97", type=pascal_formalParameterSection, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_formalParameterSection96", type=pascal_parameterGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifierList98: BinaryAssociation = BinaryAssociation(
    name="identifierList98",
    ends={
        Property(name="pascal_identifierList100", type=pascal_parameterGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_parameterGroup99", type=pascal_identifierList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier104: BinaryAssociation = BinaryAssociation(
    name="identifier104",
    ends={
        Property(name="pascal_identifier106", type=pascal_typeIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_typeIdentifier105", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameterList107: BinaryAssociation = BinaryAssociation(
    name="formalParameterList107",
    ends={
        Property(name="pascal_formalParameterList109", type=pascal_procedureType, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_procedureType108", type=pascal_formalParameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleType110: BinaryAssociation = BinaryAssociation(
    name="simpleType110",
    ends={
        Property(name="pascal_simpleType", type=pascal_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_type111", type=pascal_simpleType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structuredType112: BinaryAssociation = BinaryAssociation(
    name="structuredType112",
    ends={
        Property(name="pascal_structuredType", type=pascal_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_type113", type=pascal_structuredType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pointerType114: BinaryAssociation = BinaryAssociation(
    name="pointerType114",
    ends={
        Property(name="pascal_pointerType", type=pascal_type, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_type115", type=pascal_pointerType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeIdentifier116: BinaryAssociation = BinaryAssociation(
    name="typeIdentifier116",
    ends={
        Property(name="pascal_typeIdentifier118", type=pascal_pointerType, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_pointerType117", type=pascal_typeIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scalarType119: BinaryAssociation = BinaryAssociation(
    name="scalarType119",
    ends={
        Property(name="pascal_scalarType", type=pascal_simpleType, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simpleType120", type=pascal_scalarType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subrangeType121: BinaryAssociation = BinaryAssociation(
    name="subrangeType121",
    ends={
        Property(name="pascal_subrangeType", type=pascal_simpleType, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simpleType122", type=pascal_subrangeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeIdentifier123: BinaryAssociation = BinaryAssociation(
    name="typeIdentifier123",
    ends={
        Property(name="pascal_typeIdentifier125", type=pascal_simpleType, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simpleType124", type=pascal_typeIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stringtype126: BinaryAssociation = BinaryAssociation(
    name="stringtype126",
    ends={
        Property(name="pascal_stringtype", type=pascal_simpleType, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simpleType127", type=pascal_stringtype, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifierList128: BinaryAssociation = BinaryAssociation(
    name="identifierList128",
    ends={
        Property(name="pascal_identifierList130", type=pascal_scalarType, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_scalarType129", type=pascal_identifierList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeIdentifier101: BinaryAssociation = BinaryAssociation(
    name="typeIdentifier101",
    ends={
        Property(name="pascal_typeIdentifier103", type=pascal_parameterGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_parameterGroup102", type=pascal_typeIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant2134: BinaryAssociation = BinaryAssociation(
    name="constant2134",
    ends={
        Property(name="pascal_constant136", type=pascal_subrangeType, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_subrangeType135", type=pascal_constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unpackedStructuredType137: BinaryAssociation = BinaryAssociation(
    name="unpackedStructuredType137",
    ends={
        Property(name="pascal_unpackedStructuredType", type=pascal_structuredType, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_structuredType138", type=pascal_unpackedStructuredType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unpackedStructuredType1139: BinaryAssociation = BinaryAssociation(
    name="unpackedStructuredType1139",
    ends={
        Property(name="pascal_unpackedStructuredType141", type=pascal_structuredType, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_structuredType140", type=pascal_unpackedStructuredType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
recordType142: BinaryAssociation = BinaryAssociation(
    name="recordType142",
    ends={
        Property(name="pascal_recordType", type=pascal_unpackedStructuredType, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unpackedStructuredType143", type=pascal_recordType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier144: BinaryAssociation = BinaryAssociation(
    name="identifier144",
    ends={
        Property(name="pascal_identifier146", type=pascal_stringtype, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_stringtype145", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unsignedNumber147: BinaryAssociation = BinaryAssociation(
    name="unsignedNumber147",
    ends={
        Property(name="pascal_unsignedNumber149", type=pascal_stringtype, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_stringtype148", type=pascal_unsignedNumber, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fieldList150: BinaryAssociation = BinaryAssociation(
    name="fieldList150",
    ends={
        Property(name="pascal_fieldList152", type=pascal_recordType, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_recordType151", type=pascal_fieldList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fixedPart153: BinaryAssociation = BinaryAssociation(
    name="fixedPart153",
    ends={
        Property(name="pascal_fixedPart", type=pascal_fieldList, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_fieldList154", type=pascal_fixedPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variantPart155: BinaryAssociation = BinaryAssociation(
    name="variantPart155",
    ends={
        Property(name="pascal_variantPart", type=pascal_fieldList, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_fieldList156", type=pascal_variantPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variantPart1157: BinaryAssociation = BinaryAssociation(
    name="variantPart1157",
    ends={
        Property(name="pascal_variantPart159", type=pascal_fieldList, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_fieldList158", type=pascal_variantPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
recordSection160: BinaryAssociation = BinaryAssociation(
    name="recordSection160",
    ends={
        Property(name="pascal_recordSection", type=pascal_fixedPart, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_fixedPart161", type=pascal_recordSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
recordSection1162: BinaryAssociation = BinaryAssociation(
    name="recordSection1162",
    ends={
        Property(name="pascal_recordSection164", type=pascal_fixedPart, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_fixedPart163", type=pascal_recordSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifierList165: BinaryAssociation = BinaryAssociation(
    name="identifierList165",
    ends={
        Property(name="pascal_identifierList167", type=pascal_recordSection, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_recordSection166", type=pascal_identifierList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type168: BinaryAssociation = BinaryAssociation(
    name="type168",
    ends={
        Property(name="pascal_type170", type=pascal_recordSection, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_recordSection169", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tag171: BinaryAssociation = BinaryAssociation(
    name="tag171",
    ends={
        Property(name="pascal_tag", type=pascal_variantPart, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variantPart172", type=pascal_tag, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variant173: BinaryAssociation = BinaryAssociation(
    name="variant173",
    ends={
        Property(name="pascal_variant", type=pascal_variantPart, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variantPart174", type=pascal_variant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant131: BinaryAssociation = BinaryAssociation(
    name="constant131",
    ends={
        Property(name="pascal_constant133", type=pascal_subrangeType, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_subrangeType132", type=pascal_constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variant1175: BinaryAssociation = BinaryAssociation(
    name="variant1175",
    ends={
        Property(name="pascal_variant177", type=pascal_variantPart, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variantPart176", type=pascal_variant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifier178: BinaryAssociation = BinaryAssociation(
    name="identifier178",
    ends={
        Property(name="pascal_identifier180", type=pascal_tag, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_tag179", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeIdentifier181: BinaryAssociation = BinaryAssociation(
    name="typeIdentifier181",
    ends={
        Property(name="pascal_typeIdentifier183", type=pascal_tag, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_tag182", type=pascal_typeIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeIdentifier1184: BinaryAssociation = BinaryAssociation(
    name="typeIdentifier1184",
    ends={
        Property(name="pascal_typeIdentifier186", type=pascal_tag, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_tag185", type=pascal_typeIdentifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constant187: BinaryAssociation = BinaryAssociation(
    name="constant187",
    ends={
        Property(name="pascal_constant188", type=pascal_constList, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_constList", type=pascal_constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant1189: BinaryAssociation = BinaryAssociation(
    name="constant1189",
    ends={
        Property(name="pascal_constant191", type=pascal_constList, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_constList190", type=pascal_constant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variableDeclaration192: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration192",
    ends={
        Property(name="pascal_variableDeclaration", type=pascal_variableDeclarationPart, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variableDeclarationPart193", type=pascal_variableDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableDeclaration1194: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration1194",
    ends={
        Property(name="pascal_variableDeclaration196", type=pascal_variableDeclarationPart, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variableDeclarationPart195", type=pascal_variableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifierList197: BinaryAssociation = BinaryAssociation(
    name="identifierList197",
    ends={
        Property(name="pascal_identifierList199", type=pascal_variableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variableDeclaration198", type=pascal_identifierList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type200: BinaryAssociation = BinaryAssociation(
    name="type200",
    ends={
        Property(name="pascal_type202", type=pascal_variableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variableDeclaration201", type=pascal_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression203: BinaryAssociation = BinaryAssociation(
    name="expression203",
    ends={
        Property(name="pascal_expression", type=pascal_variableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variableDeclaration204", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
procedureOrFunctionDeclaration205: BinaryAssociation = BinaryAssociation(
    name="procedureOrFunctionDeclaration205",
    ends={
        Property(name="pascal_procedureOrFunctionDeclaration", type=pascal_procedureAndFunctionDeclarationPart, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_procedureAndFunctionDeclarationPart206", type=pascal_procedureOrFunctionDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
procedureDeclaration207: BinaryAssociation = BinaryAssociation(
    name="procedureDeclaration207",
    ends={
        Property(name="pascal_procedureDeclaration", type=pascal_procedureOrFunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_procedureOrFunctionDeclaration208", type=pascal_procedureDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functionDeclaration209: BinaryAssociation = BinaryAssociation(
    name="functionDeclaration209",
    ends={
        Property(name="pascal_functionDeclaration", type=pascal_procedureOrFunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_procedureOrFunctionDeclaration210", type=pascal_functionDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier211: BinaryAssociation = BinaryAssociation(
    name="identifier211",
    ends={
        Property(name="pascal_identifier213", type=pascal_procedureDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_procedureDeclaration212", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameterList214: BinaryAssociation = BinaryAssociation(
    name="formalParameterList214",
    ends={
        Property(name="pascal_formalParameterList216", type=pascal_procedureDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_procedureDeclaration215", type=pascal_formalParameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block217: BinaryAssociation = BinaryAssociation(
    name="block217",
    ends={
        Property(name="pascal_block219", type=pascal_procedureDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_procedureDeclaration218", type=pascal_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier220: BinaryAssociation = BinaryAssociation(
    name="identifier220",
    ends={
        Property(name="pascal_identifier222", type=pascal_functionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_functionDeclaration221", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameterList223: BinaryAssociation = BinaryAssociation(
    name="formalParameterList223",
    ends={
        Property(name="pascal_formalParameterList225", type=pascal_functionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_functionDeclaration224", type=pascal_formalParameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeIdentifier226: BinaryAssociation = BinaryAssociation(
    name="typeIdentifier226",
    ends={
        Property(name="pascal_typeIdentifier228", type=pascal_functionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_functionDeclaration227", type=pascal_typeIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block229: BinaryAssociation = BinaryAssociation(
    name="block229",
    ends={
        Property(name="pascal_block231", type=pascal_functionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_functionDeclaration230", type=pascal_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unlabelledStatement232: BinaryAssociation = BinaryAssociation(
    name="unlabelledStatement232",
    ends={
        Property(name="pascal_unlabelledStatement", type=pascal_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_statement", type=pascal_unlabelledStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleStatement233: BinaryAssociation = BinaryAssociation(
    name="simpleStatement233",
    ends={
        Property(name="pascal_simpleStatement", type=pascal_unlabelledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unlabelledStatement234", type=pascal_simpleStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structuredStatement235: BinaryAssociation = BinaryAssociation(
    name="structuredStatement235",
    ends={
        Property(name="pascal_structuredStatement", type=pascal_unlabelledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unlabelledStatement236", type=pascal_structuredStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier237: BinaryAssociation = BinaryAssociation(
    name="identifier237",
    ends={
        Property(name="pascal_identifier239", type=pascal_unlabelledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unlabelledStatement238", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterList240: BinaryAssociation = BinaryAssociation(
    name="parameterList240",
    ends={
        Property(name="pascal_parameterList", type=pascal_unlabelledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unlabelledStatement241", type=pascal_parameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
gotoStatement242: BinaryAssociation = BinaryAssociation(
    name="gotoStatement242",
    ends={
        Property(name="pascal_gotoStatement", type=pascal_simpleStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simpleStatement243", type=pascal_gotoStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignmentStatement244: BinaryAssociation = BinaryAssociation(
    name="assignmentStatement244",
    ends={
        Property(name="pascal_assignmentStatement", type=pascal_simpleStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simpleStatement245", type=pascal_assignmentStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable246: BinaryAssociation = BinaryAssociation(
    name="variable246",
    ends={
        Property(name="pascal_variable", type=pascal_assignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_assignmentStatement247", type=pascal_variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression248: BinaryAssociation = BinaryAssociation(
    name="expression248",
    ends={
        Property(name="pascal_expression250", type=pascal_assignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_assignmentStatement249", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier251: BinaryAssociation = BinaryAssociation(
    name="identifier251",
    ends={
        Property(name="pascal_identifier253", type=pascal_variable, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_variable252", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleExpression254: BinaryAssociation = BinaryAssociation(
    name="simpleExpression254",
    ends={
        Property(name="pascal_simpleExpression", type=pascal_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_expression255", type=pascal_simpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression257: BinaryAssociation = BinaryAssociation(
    name="expression257",
    ends={
        Property(name="pascal_expression258", type=pascal_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_expression256", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
term259: BinaryAssociation = BinaryAssociation(
    name="term259",
    ends={
        Property(name="pascal_term", type=pascal_simpleExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simpleExpression260", type=pascal_term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleExpression262: BinaryAssociation = BinaryAssociation(
    name="simpleExpression262",
    ends={
        Property(name="pascal_simpleExpression263", type=pascal_simpleExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_simpleExpression261", type=pascal_simpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
signedFactor264: BinaryAssociation = BinaryAssociation(
    name="signedFactor264",
    ends={
        Property(name="pascal_signedFactor", type=pascal_term, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_term265", type=pascal_signedFactor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
term267: BinaryAssociation = BinaryAssociation(
    name="term267",
    ends={
        Property(name="pascal_term268", type=pascal_term, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_term266", type=pascal_term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
factor269: BinaryAssociation = BinaryAssociation(
    name="factor269",
    ends={
        Property(name="pascal_factor", type=pascal_signedFactor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_signedFactor270", type=pascal_factor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression271: BinaryAssociation = BinaryAssociation(
    name="expression271",
    ends={
        Property(name="pascal_expression273", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor272", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unsignedConstant274: BinaryAssociation = BinaryAssociation(
    name="unsignedConstant274",
    ends={
        Property(name="pascal_unsignedConstant", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor275", type=pascal_unsignedConstant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
factor277: BinaryAssociation = BinaryAssociation(
    name="factor277",
    ends={
        Property(name="pascal_factor278", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor276", type=pascal_factor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functionDesignator279: BinaryAssociation = BinaryAssociation(
    name="functionDesignator279",
    ends={
        Property(name="pascal_functionDesignator", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor280", type=pascal_functionDesignator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable281: BinaryAssociation = BinaryAssociation(
    name="variable281",
    ends={
        Property(name="pascal_variable283", type=pascal_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_factor282", type=pascal_variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unsignedNumber284: BinaryAssociation = BinaryAssociation(
    name="unsignedNumber284",
    ends={
        Property(name="pascal_unsignedNumber286", type=pascal_unsignedConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unsignedConstant285", type=pascal_unsignedNumber, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constantChr287: BinaryAssociation = BinaryAssociation(
    name="constantChr287",
    ends={
        Property(name="pascal_constantChr289", type=pascal_unsignedConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_unsignedConstant288", type=pascal_constantChr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier290: BinaryAssociation = BinaryAssociation(
    name="identifier290",
    ends={
        Property(name="pascal_identifier292", type=pascal_functionDesignator, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_functionDesignator291", type=pascal_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterList293: BinaryAssociation = BinaryAssociation(
    name="parameterList293",
    ends={
        Property(name="pascal_parameterList295", type=pascal_functionDesignator, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_functionDesignator294", type=pascal_parameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actualParameter297: BinaryAssociation = BinaryAssociation(
    name="actualParameter297",
    ends={
        Property(name="pascal_actualParameter", type=pascal_actualParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_actualParameter296", type=pascal_actualParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression298: BinaryAssociation = BinaryAssociation(
    name="expression298",
    ends={
        Property(name="pascal_expression300", type=pascal_actualParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_actualParameter299", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
label301: BinaryAssociation = BinaryAssociation(
    name="label301",
    ends={
        Property(name="pascal_label303", type=pascal_gotoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_gotoStatement302", type=pascal_label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
compoundStatement304: BinaryAssociation = BinaryAssociation(
    name="compoundStatement304",
    ends={
        Property(name="pascal_compoundStatement306", type=pascal_structuredStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_structuredStatement305", type=pascal_compoundStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements309: BinaryAssociation = BinaryAssociation(
    name="statements309",
    ends={
        Property(name="pascal_statements", type=pascal_compoundStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_compoundStatement310", type=pascal_statements, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement311: BinaryAssociation = BinaryAssociation(
    name="statement311",
    ends={
        Property(name="pascal_statement313", type=pascal_statements, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_statements312", type=pascal_statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
caseStatement314: BinaryAssociation = BinaryAssociation(
    name="caseStatement314",
    ends={
        Property(name="pascal_caseStatement", type=pascal_conditionalStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_conditionalStatement315", type=pascal_caseStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression316: BinaryAssociation = BinaryAssociation(
    name="expression316",
    ends={
        Property(name="pascal_expression318", type=pascal_caseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_caseStatement317", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
caseListElement319: BinaryAssociation = BinaryAssociation(
    name="caseListElement319",
    ends={
        Property(name="pascal_caseListElement", type=pascal_caseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_caseStatement320", type=pascal_caseListElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
caseListElement1321: BinaryAssociation = BinaryAssociation(
    name="caseListElement1321",
    ends={
        Property(name="pascal_caseListElement323", type=pascal_caseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_caseStatement322", type=pascal_caseListElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements324: BinaryAssociation = BinaryAssociation(
    name="statements324",
    ends={
        Property(name="pascal_statements326", type=pascal_caseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_caseStatement325", type=pascal_statements, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constList327: BinaryAssociation = BinaryAssociation(
    name="constList327",
    ends={
        Property(name="pascal_constList329", type=pascal_caseListElement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_caseListElement328", type=pascal_constList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement330: BinaryAssociation = BinaryAssociation(
    name="statement330",
    ends={
        Property(name="pascal_statement332", type=pascal_caseListElement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_caseListElement331", type=pascal_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditionalStatement307: BinaryAssociation = BinaryAssociation(
    name="conditionalStatement307",
    ends={
        Property(name="pascal_conditionalStatement", type=pascal_structuredStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_structuredStatement308", type=pascal_conditionalStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_pascal_label_label_declaration_part = Generalization(general=label_declaration_part, specific=pascal_label)
gen_pascal_label_statement = Generalization(general=statement, specific=pascal_label)
gen_pascal_constant_variant = Generalization(general=variant, specific=pascal_constant)
gen_pascal_actualParameter_parameterList = Generalization(general=parameterList, specific=pascal_actualParameter)

# Domain Model
domain_model = DomainModel(
    name="pascal",
    types={pascal_pascal, pascal_program, pascal_programHeading, pascal_block, pascal_identifier, pascal_identifierList, pascal_label_declaration_part, pascal_constantDefinitionPart, pascal_typeDefinitionPart, pascal_variableDeclarationPart, pascal_procedureAndFunctionDeclarationPart, pascal_usesUnitsPart, pascal_compoundStatement, pascal_label, label_declaration_part, statement, pascal_unsignedInteger, pascal_constantDefinition, pascal_constant, variant, pascal_unsignedNumber, pascal_constantChr, pascal_fieldList, pascal_typeDefinition, pascal_type, pascal_functionType, pascal_procedureType, pascal_formalParameterList, pascal_typeIdentifier, pascal_parameterGroup, pascal_formalParameterSection, pascal_simpleType, pascal_structuredType, pascal_pointerType, pascal_scalarType, pascal_subrangeType, pascal_stringtype, pascal_unpackedStructuredType, pascal_recordType, pascal_fixedPart, pascal_variantPart, pascal_recordSection, pascal_tag, pascal_variant, pascal_constList, pascal_variableDeclaration, pascal_expression, pascal_procedureOrFunctionDeclaration, pascal_procedureDeclaration, pascal_functionDeclaration, pascal_statement, pascal_unlabelledStatement, pascal_simpleStatement, pascal_structuredStatement, pascal_parameterList, pascal_gotoStatement, pascal_assignmentStatement, pascal_variable, pascal_simpleExpression, pascal_term, pascal_signedFactor, pascal_factor, pascal_unsignedConstant, pascal_functionDesignator, pascal_actualParameter, parameterList, pascal_conditionalStatement, pascal_statements, pascal_caseStatement, pascal_caseListElement},
    associations={program0, head1, block3, identifer5, identifierList7, identifier9, identifierList112, label15, constantDefinitionParts17, typeDefinitionParts19, variableDeclarationParts21, procedureAndFunctionDeclarationParts23, usesUnitsParts25, compoundStatement27, label30, unsignedInteger31, identifier33, constantDefinition36, identifier38, constant41, unsignedNumber43, identifier45, constantChr48, constant51, fieldList53, unsignedInteger55, unsignedInteger58, identifierList61, typeDefinition64, typeDefinition166, identifier69, type72, functionType74, procedureType76, formalParameterList78, typeIdentifier80, formalParameterSection82, formalParameterSection284, parameterGroup87, parameterGroup289, parameterGroup392, parameterGroup495, identifierList98, identifier104, formalParameterList107, simpleType110, structuredType112, pointerType114, typeIdentifier116, scalarType119, subrangeType121, typeIdentifier123, stringtype126, identifierList128, typeIdentifier101, constant2134, unpackedStructuredType137, unpackedStructuredType1139, recordType142, identifier144, unsignedNumber147, fieldList150, fixedPart153, variantPart155, variantPart1157, recordSection160, recordSection1162, identifierList165, type168, tag171, variant173, constant131, variant1175, identifier178, typeIdentifier181, typeIdentifier1184, constant187, constant1189, variableDeclaration192, variableDeclaration1194, identifierList197, type200, expression203, procedureOrFunctionDeclaration205, procedureDeclaration207, functionDeclaration209, identifier211, formalParameterList214, block217, identifier220, formalParameterList223, typeIdentifier226, block229, unlabelledStatement232, simpleStatement233, structuredStatement235, identifier237, parameterList240, gotoStatement242, assignmentStatement244, variable246, expression248, identifier251, simpleExpression254, expression257, term259, simpleExpression262, signedFactor264, term267, factor269, expression271, unsignedConstant274, factor277, functionDesignator279, variable281, unsignedNumber284, constantChr287, identifier290, parameterList293, actualParameter297, expression298, label301, compoundStatement304, statements309, statement311, caseStatement314, expression316, caseListElement319, caseListElement1321, statements324, constList327, statement330, conditionalStatement307},
    generalizations={gen_pascal_label_label_declaration_part, gen_pascal_label_statement, gen_pascal_constant_variant, gen_pascal_actualParameter_parameterList},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)