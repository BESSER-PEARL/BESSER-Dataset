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

# Enumerations
RegistrationStatus: Enumeration = Enumeration(
    name="RegistrationStatus",
    literals={
            EnumerationLiteral(name="NO_STATUS"),
			EnumerationLiteral(name="PROVISIONALLY_REGISTERED"),
			EnumerationLiteral(name="REGISTERED"),
			EnumerationLiteral(name="OBSOLETE")
    }
)

Aggregation: Enumeration = Enumeration(
    name="Aggregation",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="COMPOSITE"),
			EnumerationLiteral(name="SHARED")
    }
)

Visibility: Enumeration = Enumeration(
    name="Visibility",
    literals={
            EnumerationLiteral(name="_"),
			EnumerationLiteral(name="Outdated"),
			EnumerationLiteral(name="Draft"),
			EnumerationLiteral(name="DoNotShow")
    }
)

ProcessContent: Enumeration = Enumeration(
    name="ProcessContent",
    literals={
            EnumerationLiteral(name="LAX"),
			EnumerationLiteral(name="SKIP"),
			EnumerationLiteral(name="STRICT")
    }
)

Namespace: Enumeration = Enumeration(
    name="Namespace",
    literals={
            EnumerationLiteral(name="any"),
			EnumerationLiteral(name="other"),
			EnumerationLiteral(name="list")
    }
)

# Classes
ISO20022_Constraint = Class(name="ISO20022::Constraint")
ISO20022_RepositoryConcept = Class(name="ISO20022::RepositoryConcept", is_abstract=True)
ModelEntity = Class(name="ModelEntity")
ISO20022_SemanticMarkup = Class(name="ISO20022::SemanticMarkup")
ISO20022_Doclet = Class(name="ISO20022::Doclet")
ISO20022_ModelEntity = Class(name="ISO20022::ModelEntity", is_abstract=True)
ISO20022_SemanticMarkupElement = Class(name="ISO20022::SemanticMarkupElement")
ISO20022_MessageAssociationEnd = Class(name="ISO20022::MessageAssociationEnd")
MessageElement = Class(name="MessageElement")
ISO20022_MessageComponentType = Class(name="ISO20022::MessageComponentType", is_abstract=True)
ISO20022_MessageElement = Class(name="ISO20022::MessageElement", is_abstract=True)
XMLMember = Class(name="XMLMember")
MessageConcept = Class(name="MessageConcept")
ISO20022_BusinessComponent = Class(name="ISO20022::BusinessComponent")
ISO20022_BusinessElement = Class(name="ISO20022::BusinessElement", is_abstract=True)
ISO20022_MessageElementContainer = Class(name="ISO20022::MessageElementContainer", is_abstract=True)
ISO20022_XMLMember = Class(name="ISO20022::XMLMember", is_abstract=True)
Member = Class(name="Member")
ISO20022_LogicalType = Class(name="ISO20022::LogicalType", is_abstract=True)
ISO20022_Member = Class(name="ISO20022::Member", is_abstract=True)
RepositoryConcept = Class(name="RepositoryConcept")
MultiplicityEntity = Class(name="MultiplicityEntity")
ISO20022_Type = Class(name="ISO20022::Type", is_abstract=True)
ISO20022_MultiplicityEntity = Class(name="ISO20022::MultiplicityEntity", is_abstract=True)
Type = Class(name="Type")
ISO20022_IsAnAlternativeFor = Class(name="ISO20022::IsAnAlternativeFor")
ISO20022_MessageConcept = Class(name="ISO20022::MessageConcept", is_abstract=True)
BusinessElementType = Class(name="BusinessElementType")
TopLevelDictionaryEntry = Class(name="TopLevelDictionaryEntry")
BusinessConcept = Class(name="BusinessConcept")
ISO20022_BusinessAssociationEnd = Class(name="ISO20022::BusinessAssociationEnd")
ISO20022_BusinessConcept = Class(name="ISO20022::BusinessConcept", is_abstract=True)
ISO20022_TopLevelDictionaryEntry = Class(name="ISO20022::TopLevelDictionaryEntry", is_abstract=True)
ISO20022_DataDictionary = Class(name="ISO20022::DataDictionary")
ISO20022_Repository = Class(name="ISO20022::Repository")
ISO20022_BusinessProcessCatalogue = Class(name="ISO20022::BusinessProcessCatalogue")
ISO20022_Diagram = Class(name="ISO20022::Diagram")
ISO20022_BusinessElementType = Class(name="ISO20022::BusinessElementType", is_abstract=True)
ISO20022_TopLevelCatalogueEntry = Class(name="ISO20022::TopLevelCatalogueEntry", is_abstract=True)
LogicalType = Class(name="LogicalType")
ISO20022_MessageBuildingBlock = Class(name="ISO20022::MessageBuildingBlock")
ISO20022_Facet = Class(name="ISO20022::Facet")
ISO20022_DataType = Class(name="ISO20022::DataType", is_abstract=True)
BusinessElement = Class(name="BusinessElement")
MessageComponentType = Class(name="MessageComponentType")
ISO20022_Syntax = Class(name="ISO20022::Syntax")
ISO20022_MessageAttribute = Class(name="ISO20022::MessageAttribute")
ISO20022_Encoding = Class(name="ISO20022::Encoding")
ISO20022_MessageSet = Class(name="ISO20022::MessageSet")
TopLevelCatalogueEntry = Class(name="TopLevelCatalogueEntry")
ISO20022_MessageDefinition = Class(name="ISO20022::MessageDefinition")
ISO20022_Interaction = Class(name="ISO20022::Interaction")
ISO20022_MessageChoreography = Class(name="ISO20022::MessageChoreography")
ISO20022_BusinessArea = Class(name="ISO20022::BusinessArea")
ISO20022_Xor = Class(name="ISO20022::Xor")
ISO20022_SyntaxMessageScheme = Class(name="ISO20022::SyntaxMessageScheme")
ISO20022_MessageDefinitionIdentifier = Class(name="ISO20022::MessageDefinitionIdentifier")
ISO20022_MessageComponent = Class(name="ISO20022::MessageComponent")
MessageElementContainer = Class(name="MessageElementContainer")
ISO20022_InteractionMessage = Class(name="ISO20022::InteractionMessage")
ISO20022_InteractionActor = Class(name="ISO20022::InteractionActor")
ISO20022_BusinessRole = Class(name="ISO20022::BusinessRole")
ISO20022_BusinessAttribute = Class(name="ISO20022::BusinessAttribute")
ISO20022_IdentifierSet = Class(name="ISO20022::IdentifierSet")
ISO20022_Text = Class(name="ISO20022::Text")
XSDString = Class(name="XSDString")
ISO20022_XSDString = Class(name="ISO20022::XSDString")
DataType = Class(name="DataType")
ISO20022_XSDDecimal = Class(name="ISO20022::XSDDecimal")
ISO20022_Indicator = Class(name="ISO20022::Indicator")
XSDBoolean = Class(name="XSDBoolean")
ISO20022_XSDBoolean = Class(name="ISO20022::XSDBoolean")
ISO20022_Rate = Class(name="ISO20022::Rate")
XSDDecimal = Class(name="XSDDecimal")
ISO20022_ExternalSchema = Class(name="ISO20022::ExternalSchema")
ISO20022_CodeSet = Class(name="ISO20022::CodeSet")
ISO20022_Quantity = Class(name="ISO20022::Quantity")
ISO20022_Code = Class(name="ISO20022::Code")
ISO20022_ChoiceComponent = Class(name="ISO20022::ChoiceComponent")
ISO20022_Amount = Class(name="ISO20022::Amount")
ISO20022_AbstractTimeConcept = Class(name="ISO20022::AbstractTimeConcept", is_abstract=True)
ISO20022_XSDBinary = Class(name="ISO20022::XSDBinary")
ISO20022_EndPointCategory = Class(name="ISO20022::EndPointCategory")
ISO20022_ApplicationHeader = Class(name="ISO20022::ApplicationHeader")
MessageDefinition = Class(name="MessageDefinition")
ISO20022_XSDID = Class(name="ISO20022::XSDID")
ISO20022_XSDDate = Class(name="ISO20022::XSDDate")
AbstractTimeConcept = Class(name="AbstractTimeConcept")
ISO20022_XSDDateTime = Class(name="ISO20022::XSDDateTime")
ISO20022_XSDDay = Class(name="ISO20022::XSDDay")
ISO20022_XSDDuration = Class(name="ISO20022::XSDDuration")
ISO20022_SWIFTSolution = Class(name="ISO20022::SWIFTSolution")
MessageSet = Class(name="MessageSet")
ISO20022_XSDMonth = Class(name="ISO20022::XSDMonth")
ISO20022_XSDMonthDay = Class(name="ISO20022::XSDMonthDay")
ISO20022_XSDTime = Class(name="ISO20022::XSDTime")
ISO20022_XSDYear = Class(name="ISO20022::XSDYear")
ISO20022_XSDYearMonth = Class(name="ISO20022::XSDYearMonth")
ISO20022_UserDefined = Class(name="ISO20022::UserDefined")

# ISO20022_Constraint class attributes and methods
ISO20022_Constraint_injected: Property = Property(name="injected", type=BooleanType)
ISO20022_Constraint_errorCode: Property = Property(name="errorCode", type=StringType)
ISO20022_Constraint_errorText: Property = Property(name="errorText", type=StringType)
ISO20022_Constraint_kind: Property = Property(name="kind", type=StringType)
ISO20022_Constraint_expression: Property = Property(name="expression", type=StringType)
ISO20022_Constraint_expressionLanguage: Property = Property(name="expressionLanguage", type=StringType)
ISO20022_Constraint.attributes={ISO20022_Constraint_errorCode, ISO20022_Constraint_errorText, ISO20022_Constraint_expressionLanguage, ISO20022_Constraint_injected, ISO20022_Constraint_kind, ISO20022_Constraint_expression}

# ISO20022_RepositoryConcept class attributes and methods
ISO20022_RepositoryConcept_name: Property = Property(name="name", type=StringType)
ISO20022_RepositoryConcept_definition: Property = Property(name="definition", type=StringType)
ISO20022_RepositoryConcept_example: Property = Property(name="example", type=StringType)
ISO20022_RepositoryConcept_swiftRegistrationStatus: Property = Property(name="swiftRegistrationStatus", type=StringType)
ISO20022_RepositoryConcept_swiftRemovalDate: Property = Property(name="swiftRemovalDate", type=DateType)
ISO20022_RepositoryConcept_registrationStatus: Property = Property(name="registrationStatus", type=StringType)
ISO20022_RepositoryConcept_removalDate: Property = Property(name="removalDate", type=DateType)
ISO20022_RepositoryConcept_m_RemovalDateRegistrationStatus: Method = Method(name="RemovalDateRegistrationStatus", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ISO20022_RepositoryConcept.attributes={ISO20022_RepositoryConcept_removalDate, ISO20022_RepositoryConcept_swiftRemovalDate, ISO20022_RepositoryConcept_swiftRegistrationStatus, ISO20022_RepositoryConcept_example, ISO20022_RepositoryConcept_name, ISO20022_RepositoryConcept_registrationStatus, ISO20022_RepositoryConcept_definition}
ISO20022_RepositoryConcept.methods={ISO20022_RepositoryConcept_m_RemovalDateRegistrationStatus}

# ModelEntity class attributes and methods

# ISO20022_SemanticMarkup class attributes and methods
ISO20022_SemanticMarkup_type: Property = Property(name="type", type=StringType)
ISO20022_SemanticMarkup.attributes={ISO20022_SemanticMarkup_type}

# ISO20022_Doclet class attributes and methods
ISO20022_Doclet_type: Property = Property(name="type", type=StringType)
ISO20022_Doclet_content: Property = Property(name="content", type=StringType)
ISO20022_Doclet.attributes={ISO20022_Doclet_content, ISO20022_Doclet_type}

# ISO20022_ModelEntity class attributes and methods
ISO20022_ModelEntity_objectIdentifier: Property = Property(name="objectIdentifier", type=StringType)
ISO20022_ModelEntity.attributes={ISO20022_ModelEntity_objectIdentifier}

# ISO20022_SemanticMarkupElement class attributes and methods
ISO20022_SemanticMarkupElement_name: Property = Property(name="name", type=StringType)
ISO20022_SemanticMarkupElement_value: Property = Property(name="value", type=StringType)
ISO20022_SemanticMarkupElement.attributes={ISO20022_SemanticMarkupElement_value, ISO20022_SemanticMarkupElement_name}

# ISO20022_MessageAssociationEnd class attributes and methods
ISO20022_MessageAssociationEnd_isComposite: Property = Property(name="isComposite", type=BooleanType)
ISO20022_MessageAssociationEnd.attributes={ISO20022_MessageAssociationEnd_isComposite}

# MessageElement class attributes and methods

# ISO20022_MessageComponentType class attributes and methods
ISO20022_MessageComponentType_isTechnical: Property = Property(name="isTechnical", type=BooleanType)
ISO20022_MessageComponentType_tracePath: Property = Property(name="tracePath", type=StringType)
ISO20022_MessageComponentType.attributes={ISO20022_MessageComponentType_tracePath, ISO20022_MessageComponentType_isTechnical}

# ISO20022_MessageElement class attributes and methods
ISO20022_MessageElement_isTechnical: Property = Property(name="isTechnical", type=BooleanType)
ISO20022_MessageElement_tracePath: Property = Property(name="tracePath", type=StringType)
ISO20022_MessageElement_isDerived: Property = Property(name="isDerived", type=BooleanType)
ISO20022_MessageElement_m_NoMoreThanOneTrace: Method = Method(name="NoMoreThanOneTrace", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ISO20022_MessageElement_m_CardinalityAlignment: Method = Method(name="CardinalityAlignment", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
ISO20022_MessageElement.attributes={ISO20022_MessageElement_isTechnical, ISO20022_MessageElement_tracePath, ISO20022_MessageElement_isDerived}
ISO20022_MessageElement.methods={ISO20022_MessageElement_m_NoMoreThanOneTrace, ISO20022_MessageElement_m_CardinalityAlignment}

# XMLMember class attributes and methods

# MessageConcept class attributes and methods

# ISO20022_BusinessComponent class attributes and methods
ISO20022_BusinessComponent_previousVersionDocumentation: Property = Property(name="previousVersionDocumentation", type=StringType)
ISO20022_BusinessComponent_m_BusinessElementsHaveUniqueNames: Method = Method(name="BusinessElementsHaveUniqueNames", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ISO20022_BusinessComponent.attributes={ISO20022_BusinessComponent_previousVersionDocumentation}
ISO20022_BusinessComponent.methods={ISO20022_BusinessComponent_m_BusinessElementsHaveUniqueNames}

# ISO20022_BusinessElement class attributes and methods
ISO20022_BusinessElement_isDerived: Property = Property(name="isDerived", type=BooleanType)
ISO20022_BusinessElement.attributes={ISO20022_BusinessElement_isDerived}

# ISO20022_MessageElementContainer class attributes and methods
ISO20022_MessageElementContainer_m_MessageElementsHaveUniqueNames: Method = Method(name="MessageElementsHaveUniqueNames", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
ISO20022_MessageElementContainer_m_technicalElement: Method = Method(name="technicalElement", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
ISO20022_MessageElementContainer.methods={ISO20022_MessageElementContainer_m_technicalElement, ISO20022_MessageElementContainer_m_MessageElementsHaveUniqueNames}

# ISO20022_XMLMember class attributes and methods
ISO20022_XMLMember_xmlTag: Property = Property(name="xmlTag", type=StringType)
ISO20022_XMLMember.attributes={ISO20022_XMLMember_xmlTag}

# Member class attributes and methods

# ISO20022_LogicalType class attributes and methods

# ISO20022_Member class attributes and methods

# RepositoryConcept class attributes and methods

# MultiplicityEntity class attributes and methods

# ISO20022_Type class attributes and methods

# ISO20022_MultiplicityEntity class attributes and methods
ISO20022_MultiplicityEntity_maxOccurs: Property = Property(name="maxOccurs", type=StringType)
ISO20022_MultiplicityEntity_minOccurs: Property = Property(name="minOccurs", type=StringType)
ISO20022_MultiplicityEntity.attributes={ISO20022_MultiplicityEntity_minOccurs, ISO20022_MultiplicityEntity_maxOccurs}

# Type class attributes and methods

# ISO20022_IsAnAlternativeFor class attributes and methods

# ISO20022_MessageConcept class attributes and methods

# BusinessElementType class attributes and methods

# TopLevelDictionaryEntry class attributes and methods

# BusinessConcept class attributes and methods

# ISO20022_BusinessAssociationEnd class attributes and methods
ISO20022_BusinessAssociationEnd_aggregation: Property = Property(name="aggregation", type=StringType)
ISO20022_BusinessAssociationEnd_m_AtMostOneAggregatedEnd: Method = Method(name="AtMostOneAggregatedEnd", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ISO20022_BusinessAssociationEnd_m_ContextConsistentWithType: Method = Method(name="ContextConsistentWithType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
ISO20022_BusinessAssociationEnd.attributes={ISO20022_BusinessAssociationEnd_aggregation}
ISO20022_BusinessAssociationEnd.methods={ISO20022_BusinessAssociationEnd_m_ContextConsistentWithType, ISO20022_BusinessAssociationEnd_m_AtMostOneAggregatedEnd}

# ISO20022_BusinessConcept class attributes and methods

# ISO20022_TopLevelDictionaryEntry class attributes and methods

# ISO20022_DataDictionary class attributes and methods
ISO20022_DataDictionary_m_EntriesHaveUniqueName: Method = Method(name="EntriesHaveUniqueName", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
ISO20022_DataDictionary.methods={ISO20022_DataDictionary_m_EntriesHaveUniqueName}

# ISO20022_Repository class attributes and methods

# ISO20022_BusinessProcessCatalogue class attributes and methods
ISO20022_BusinessProcessCatalogue_m_EntriesHaveUniqueName: Method = Method(name="EntriesHaveUniqueName", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ISO20022_BusinessProcessCatalogue.methods={ISO20022_BusinessProcessCatalogue_m_EntriesHaveUniqueName}

# ISO20022_Diagram class attributes and methods
ISO20022_Diagram_content: Property = Property(name="content", type=StringType)
ISO20022_Diagram_location: Property = Property(name="location", type=StringType)
ISO20022_Diagram.attributes={ISO20022_Diagram_content, ISO20022_Diagram_location}

# ISO20022_BusinessElementType class attributes and methods

# ISO20022_TopLevelCatalogueEntry class attributes and methods

# LogicalType class attributes and methods

# ISO20022_MessageBuildingBlock class attributes and methods
ISO20022_MessageBuildingBlock_m_MessageBuildingBlockHasExactlyOneType: Method = Method(name="MessageBuildingBlockHasExactlyOneType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
ISO20022_MessageBuildingBlock.methods={ISO20022_MessageBuildingBlock_m_MessageBuildingBlockHasExactlyOneType}

# ISO20022_Facet class attributes and methods
ISO20022_Facet_name: Property = Property(name="name", type=StringType)
ISO20022_Facet_value: Property = Property(name="value", type=StringType)
ISO20022_Facet.attributes={ISO20022_Facet_name, ISO20022_Facet_value}

# ISO20022_DataType class attributes and methods

# BusinessElement class attributes and methods

# MessageComponentType class attributes and methods

# ISO20022_Syntax class attributes and methods
ISO20022_Syntax_m_GeneratedForDerivation: Method = Method(name="GeneratedForDerivation", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ISO20022_Syntax.methods={ISO20022_Syntax_m_GeneratedForDerivation}

# ISO20022_MessageAttribute class attributes and methods
ISO20022_MessageAttribute_m_MessageAttributeHasExactlyOneType: Method = Method(name="MessageAttributeHasExactlyOneType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ISO20022_MessageAttribute.methods={ISO20022_MessageAttribute_m_MessageAttributeHasExactlyOneType}

# ISO20022_Encoding class attributes and methods

# ISO20022_MessageSet class attributes and methods
ISO20022_MessageSet_m_GeneratedSyntaxDerivation: Method = Method(name="GeneratedSyntaxDerivation", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ISO20022_MessageSet.methods={ISO20022_MessageSet_m_GeneratedSyntaxDerivation}

# TopLevelCatalogueEntry class attributes and methods

# ISO20022_MessageDefinition class attributes and methods
ISO20022_MessageDefinition_xmlTag: Property = Property(name="xmlTag", type=StringType)
ISO20022_MessageDefinition_previousVersionDocumentation: Property = Property(name="previousVersionDocumentation", type=StringType)
ISO20022_MessageDefinition_urn: Property = Property(name="urn", type=StringType)
ISO20022_MessageDefinition_xmlName: Property = Property(name="xmlName", type=StringType)
ISO20022_MessageDefinition_rootElement: Property = Property(name="rootElement", type=StringType)
ISO20022_MessageDefinition_visibility: Property = Property(name="visibility", type=StringType)
ISO20022_MessageDefinition_m_BusinessAreaNameMatch: Method = Method(name="BusinessAreaNameMatch", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ISO20022_MessageDefinition.attributes={ISO20022_MessageDefinition_visibility, ISO20022_MessageDefinition_xmlTag, ISO20022_MessageDefinition_rootElement, ISO20022_MessageDefinition_xmlName, ISO20022_MessageDefinition_previousVersionDocumentation, ISO20022_MessageDefinition_urn}
ISO20022_MessageDefinition.methods={ISO20022_MessageDefinition_m_BusinessAreaNameMatch}

# ISO20022_Interaction class attributes and methods
ISO20022_Interaction_location: Property = Property(name="location", type=StringType)
ISO20022_Interaction.attributes={ISO20022_Interaction_location}

# ISO20022_MessageChoreography class attributes and methods

# ISO20022_BusinessArea class attributes and methods
ISO20022_BusinessArea_code: Property = Property(name="code", type=StringType)
ISO20022_BusinessArea.attributes={ISO20022_BusinessArea_code}

# ISO20022_Xor class attributes and methods

# ISO20022_SyntaxMessageScheme class attributes and methods

# ISO20022_MessageDefinitionIdentifier class attributes and methods
ISO20022_MessageDefinitionIdentifier_businessArea: Property = Property(name="businessArea", type=StringType)
ISO20022_MessageDefinitionIdentifier_messageFunctionality: Property = Property(name="messageFunctionality", type=StringType)
ISO20022_MessageDefinitionIdentifier_flavour: Property = Property(name="flavour", type=StringType)
ISO20022_MessageDefinitionIdentifier_version: Property = Property(name="version", type=StringType)
ISO20022_MessageDefinitionIdentifier.attributes={ISO20022_MessageDefinitionIdentifier_messageFunctionality, ISO20022_MessageDefinitionIdentifier_flavour, ISO20022_MessageDefinitionIdentifier_version, ISO20022_MessageDefinitionIdentifier_businessArea}

# ISO20022_MessageComponent class attributes and methods

# MessageElementContainer class attributes and methods

# ISO20022_InteractionMessage class attributes and methods

# ISO20022_InteractionActor class attributes and methods

# ISO20022_BusinessRole class attributes and methods

# ISO20022_BusinessAttribute class attributes and methods
ISO20022_BusinessAttribute_m_BusinessAttributeHasExactlyOneType: Method = Method(name="BusinessAttributeHasExactlyOneType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
ISO20022_BusinessAttribute_m_NoDerivingCodeSetType: Method = Method(name="NoDerivingCodeSetType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
ISO20022_BusinessAttribute.methods={ISO20022_BusinessAttribute_m_NoDerivingCodeSetType, ISO20022_BusinessAttribute_m_BusinessAttributeHasExactlyOneType}

# ISO20022_IdentifierSet class attributes and methods
ISO20022_IdentifierSet_identificationScheme: Property = Property(name="identificationScheme", type=StringType)
ISO20022_IdentifierSet.attributes={ISO20022_IdentifierSet_identificationScheme}

# ISO20022_Text class attributes and methods

# XSDString class attributes and methods

# ISO20022_XSDString class attributes and methods
ISO20022_XSDString_minLength: Property = Property(name="minLength", type=StringType)
ISO20022_XSDString_maxLength: Property = Property(name="maxLength", type=StringType)
ISO20022_XSDString_length: Property = Property(name="length", type=StringType)
ISO20022_XSDString_pattern: Property = Property(name="pattern", type=StringType)
ISO20022_XSDString.attributes={ISO20022_XSDString_maxLength, ISO20022_XSDString_length, ISO20022_XSDString_pattern, ISO20022_XSDString_minLength}

# DataType class attributes and methods

# ISO20022_XSDDecimal class attributes and methods
ISO20022_XSDDecimal_minInclusive: Property = Property(name="minInclusive", type=StringType)
ISO20022_XSDDecimal_minExclusive: Property = Property(name="minExclusive", type=StringType)
ISO20022_XSDDecimal_maxInclusive: Property = Property(name="maxInclusive", type=StringType)
ISO20022_XSDDecimal_maxExclusive: Property = Property(name="maxExclusive", type=StringType)
ISO20022_XSDDecimal_totalDigits: Property = Property(name="totalDigits", type=StringType)
ISO20022_XSDDecimal_fractionDigits: Property = Property(name="fractionDigits", type=StringType)
ISO20022_XSDDecimal_pattern: Property = Property(name="pattern", type=StringType)
ISO20022_XSDDecimal.attributes={ISO20022_XSDDecimal_totalDigits, ISO20022_XSDDecimal_maxExclusive, ISO20022_XSDDecimal_minInclusive, ISO20022_XSDDecimal_pattern, ISO20022_XSDDecimal_fractionDigits, ISO20022_XSDDecimal_minExclusive, ISO20022_XSDDecimal_maxInclusive}

# ISO20022_Indicator class attributes and methods
ISO20022_Indicator_meaningWhenTrue: Property = Property(name="meaningWhenTrue", type=StringType)
ISO20022_Indicator_meaningWhenFalse: Property = Property(name="meaningWhenFalse", type=StringType)
ISO20022_Indicator_pattern: Property = Property(name="pattern", type=StringType)
ISO20022_Indicator.attributes={ISO20022_Indicator_meaningWhenFalse, ISO20022_Indicator_meaningWhenTrue, ISO20022_Indicator_pattern}

# XSDBoolean class attributes and methods

# ISO20022_XSDBoolean class attributes and methods

# ISO20022_Rate class attributes and methods
ISO20022_Rate_baseUnitCode: Property = Property(name="baseUnitCode", type=StringType)
ISO20022_Rate_baseValue: Property = Property(name="baseValue", type=StringType)
ISO20022_Rate.attributes={ISO20022_Rate_baseUnitCode, ISO20022_Rate_baseValue}

# XSDDecimal class attributes and methods

# ISO20022_ExternalSchema class attributes and methods
ISO20022_ExternalSchema_namespaceList: Property = Property(name="namespaceList", type=StringType)
ISO20022_ExternalSchema_processContent: Property = Property(name="processContent", type=StringType)
ISO20022_ExternalSchema.attributes={ISO20022_ExternalSchema_namespaceList, ISO20022_ExternalSchema_processContent}

# ISO20022_CodeSet class attributes and methods
ISO20022_CodeSet_identificationScheme: Property = Property(name="identificationScheme", type=StringType)
ISO20022_CodeSet.attributes={ISO20022_CodeSet_identificationScheme}

# ISO20022_Quantity class attributes and methods
ISO20022_Quantity_unitCode: Property = Property(name="unitCode", type=StringType)
ISO20022_Quantity.attributes={ISO20022_Quantity_unitCode}

# ISO20022_Code class attributes and methods
ISO20022_Code_codeName: Property = Property(name="codeName", type=StringType)
ISO20022_Code.attributes={ISO20022_Code_codeName}

# ISO20022_ChoiceComponent class attributes and methods
ISO20022_ChoiceComponent_m_AtLeastOneProperty: Method = Method(name="AtLeastOneProperty", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
ISO20022_ChoiceComponent.methods={ISO20022_ChoiceComponent_m_AtLeastOneProperty}

# ISO20022_Amount class attributes and methods

# ISO20022_AbstractTimeConcept class attributes and methods
ISO20022_AbstractTimeConcept_minExclusive: Property = Property(name="minExclusive", type=StringType)
ISO20022_AbstractTimeConcept_maxInclusive: Property = Property(name="maxInclusive", type=StringType)
ISO20022_AbstractTimeConcept_maxExclusive: Property = Property(name="maxExclusive", type=StringType)
ISO20022_AbstractTimeConcept_minInclusive: Property = Property(name="minInclusive", type=StringType)
ISO20022_AbstractTimeConcept_pattern: Property = Property(name="pattern", type=StringType)
ISO20022_AbstractTimeConcept.attributes={ISO20022_AbstractTimeConcept_minInclusive, ISO20022_AbstractTimeConcept_maxExclusive, ISO20022_AbstractTimeConcept_minExclusive, ISO20022_AbstractTimeConcept_pattern, ISO20022_AbstractTimeConcept_maxInclusive}

# ISO20022_XSDBinary class attributes and methods
ISO20022_XSDBinary_minLength: Property = Property(name="minLength", type=StringType)
ISO20022_XSDBinary_maxLength: Property = Property(name="maxLength", type=StringType)
ISO20022_XSDBinary_length: Property = Property(name="length", type=StringType)
ISO20022_XSDBinary_pattern: Property = Property(name="pattern", type=StringType)
ISO20022_XSDBinary.attributes={ISO20022_XSDBinary_minLength, ISO20022_XSDBinary_maxLength, ISO20022_XSDBinary_length, ISO20022_XSDBinary_pattern}

# ISO20022_EndPointCategory class attributes and methods

# ISO20022_ApplicationHeader class attributes and methods

# MessageDefinition class attributes and methods

# ISO20022_XSDID class attributes and methods

# ISO20022_XSDDate class attributes and methods

# AbstractTimeConcept class attributes and methods

# ISO20022_XSDDateTime class attributes and methods

# ISO20022_XSDDay class attributes and methods

# ISO20022_XSDDuration class attributes and methods

# ISO20022_SWIFTSolution class attributes and methods
ISO20022_SWIFTSolution_serviceName: Property = Property(name="serviceName", type=StringType)
ISO20022_SWIFTSolution.attributes={ISO20022_SWIFTSolution_serviceName}

# MessageSet class attributes and methods

# ISO20022_XSDMonth class attributes and methods

# ISO20022_XSDMonthDay class attributes and methods

# ISO20022_XSDTime class attributes and methods

# ISO20022_XSDYear class attributes and methods

# ISO20022_XSDYearMonth class attributes and methods

# ISO20022_UserDefined class attributes and methods
ISO20022_UserDefined__: Property = Property(name="_", type=StringType)
ISO20022_UserDefined_namespaceList: Property = Property(name="namespaceList", type=StringType)
ISO20022_UserDefined_processContents: Property = Property(name="processContents", type=StringType)
ISO20022_UserDefined.attributes={ISO20022_UserDefined_namespaceList, ISO20022_UserDefined_processContents, ISO20022_UserDefined__}

# Relationships
owner0: BinaryAssociation = BinaryAssociation(
    name="owner0",
    ends={
        Property(name="RepositoryConcept", type=ISO20022_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="constraint", type=ISO20022_RepositoryConcept, multiplicity=Multiplicity(1, 1))
    }
)
semanticMarkup1: BinaryAssociation = BinaryAssociation(
    name="semanticMarkup1",
    ends={
        Property(name="ISO20022_SemanticMarkup", type=ISO20022_RepositoryConcept, multiplicity=Multiplicity(1, 1)),
        Property(name="ISO20022_RepositoryConcept", type=ISO20022_SemanticMarkup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
doclet2: BinaryAssociation = BinaryAssociation(
    name="doclet2",
    ends={
        Property(name="ISO20022_Doclet", type=ISO20022_RepositoryConcept, multiplicity=Multiplicity(1, 1)),
        Property(name="ISO20022_RepositoryConcept3", type=ISO20022_Doclet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraint4: BinaryAssociation = BinaryAssociation(
    name="constraint4",
    ends={
        Property(name="Constraint", type=ISO20022_RepositoryConcept, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=ISO20022_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nextVersions6: BinaryAssociation = BinaryAssociation(
    name="nextVersions6",
    ends={
        Property(name="ModelEntity", type=ISO20022_ModelEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="previousVersion", type=ISO20022_ModelEntity, multiplicity=Multiplicity(0, 9999))
    }
)
previousVersion8: BinaryAssociation = BinaryAssociation(
    name="previousVersion8",
    ends={
        Property(name="ModelEntity9", type=ISO20022_ModelEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="nextVersions", type=ISO20022_ModelEntity, multiplicity=Multiplicity(0, 1))
    }
)
elements10: BinaryAssociation = BinaryAssociation(
    name="elements10",
    ends={
        Property(name="ISO20022_SemanticMarkupElement", type=ISO20022_SemanticMarkup, multiplicity=Multiplicity(1, 1)),
        Property(name="ISO20022_SemanticMarkup11", type=ISO20022_SemanticMarkupElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type12: BinaryAssociation = BinaryAssociation(
    name="type12",
    ends={
        Property(name="ISO20022_MessageComponentType", type=ISO20022_MessageAssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="ISO20022_MessageAssociationEnd", type=ISO20022_MessageComponentType, multiplicity=Multiplicity(1, 1))
    }
)
opposite14: BinaryAssociation = BinaryAssociation(
    name="opposite14",
    ends={
        Property(name="ISO20022_MessageAssociationEnd15", type=ISO20022_MessageAssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="ISO20022_MessageAssociationEnd13", type=ISO20022_MessageAssociationEnd, multiplicity=Multiplicity(0, 1))
    }
)
businessComponentTrace16: BinaryAssociation = BinaryAssociation(
    name="businessComponentTrace16",
    ends={
        Property(name="BusinessComponent", type=ISO20022_MessageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="derivationElement", type=ISO20022_BusinessComponent, multiplicity=Multiplicity(0, 1))
    }
)
businessElementTrace17: BinaryAssociation = BinaryAssociation(
    name="businessElementTrace17",
    ends={
        Property(name="BusinessElement", type=ISO20022_MessageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="derivation", type=ISO20022_BusinessElement, multiplicity=Multiplicity(0, 1))
    }
)
componentContext18: BinaryAssociation = BinaryAssociation(
    name="componentContext18",
    ends={
        Property(name="MessageElementContainer", type=ISO20022_MessageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="messageElement", type=ISO20022_MessageElementContainer, multiplicity=Multiplicity(1, 1))
    }
)
xmlMemberType19: BinaryAssociation = BinaryAssociation(
    name="xmlMemberType19",
    ends={
        Property(name="LogicalType", type=ISO20022_XMLMember, multiplicity=Multiplicity(1, 1)),
        Property(name="typedXMLMember", type=ISO20022_LogicalType, multiplicity=Multiplicity(1, 1))
    }
)
memberType20: BinaryAssociation = BinaryAssociation(
    name="memberType20",
    ends={
        Property(name="Type", type=ISO20022_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="typedMember", type=ISO20022_Type, multiplicity=Multiplicity(1, 1))
    }
)
typedMember21: BinaryAssociation = BinaryAssociation(
    name="typedMember21",
    ends={
        Property(name="Member", type=ISO20022_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="memberType", type=ISO20022_Member, multiplicity=Multiplicity(0, 9999))
    }
)
isAnAlternativeFors22: BinaryAssociation = BinaryAssociation(
    name="isAnAlternativeFors22",
    ends={
        Property(name="IsAnAlternativeFor", type=ISO20022_LogicalType, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=ISO20022_IsAnAlternativeFor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
derivations24: BinaryAssociation = BinaryAssociation(
    name="derivations24",
    ends={
        Property(name="LogicalType25", type=ISO20022_LogicalType, multiplicity=Multiplicity(1, 1)),
        Property(name="derivedFroms", type=ISO20022_LogicalType, multiplicity=Multiplicity(0, 9999))
    }
)
derivedFroms27: BinaryAssociation = BinaryAssociation(
    name="derivedFroms27",
    ends={
        Property(name="LogicalType28", type=ISO20022_LogicalType, multiplicity=Multiplicity(1, 1)),
        Property(name="derivations", type=ISO20022_LogicalType, multiplicity=Multiplicity(0, 9999))
    }
)
typedXMLMember29: BinaryAssociation = BinaryAssociation(
    name="typedXMLMember29",
    ends={
        Property(name="XMLMember", type=ISO20022_LogicalType, multiplicity=Multiplicity(1, 1)),
        Property(name="xmlMemberType", type=ISO20022_XMLMember, multiplicity=Multiplicity(0, 9999))
    }
)
target30: BinaryAssociation = BinaryAssociation(
    name="target30",
    ends={
        Property(name="ISO20022_LogicalType", type=ISO20022_IsAnAlternativeFor, multiplicity=Multiplicity(1, 1)),
        Property(name="ISO20022_IsAnAlternativeFor", type=ISO20022_LogicalType, multiplicity=Multiplicity(1, 1))
    }
)
source31: BinaryAssociation = BinaryAssociation(
    name="source31",
    ends={
        Property(name="isAnAlternativeFors", type=ISO20022_LogicalType, multiplicity=Multiplicity(1, 1)),
        Property(name="LogicalType32", type=ISO20022_IsAnAlternativeFor, multiplicity=Multiplicity(1, 1))
    }
)
subType34: BinaryAssociation = BinaryAssociation(
    name="subType34",
    ends={
        Property(name="BusinessComponent35", type=ISO20022_BusinessComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="superType", type=ISO20022_BusinessComponent, multiplicity=Multiplicity(0, 9999))
    }
)
superType37: BinaryAssociation = BinaryAssociation(
    name="superType37",
    ends={
        Property(name="BusinessComponent38", type=ISO20022_BusinessComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="subType", type=ISO20022_BusinessComponent, multiplicity=Multiplicity(0, 1))
    }
)
element39: BinaryAssociation = BinaryAssociation(
    name="element39",
    ends={
        Property(name="BusinessElement40", type=ISO20022_BusinessComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="elementContext", type=ISO20022_BusinessElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
derivationComponent41: BinaryAssociation = BinaryAssociation(
    name="derivationComponent41",
    ends={
        Property(name="MessageComponentType", type=ISO20022_BusinessComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="trace", type=ISO20022_MessageComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
associationDomain42: BinaryAssociation = BinaryAssociation(
    name="associationDomain42",
    ends={
        Property(name="BusinessAssociationEnd", type=ISO20022_BusinessComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=ISO20022_BusinessAssociationEnd, multiplicity=Multiplicity(0, 9999))
    }
)
derivationElement43: BinaryAssociation = BinaryAssociation(
    name="derivationElement43",
    ends={
        Property(name="MessageElement", type=ISO20022_BusinessComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="businessComponentTrace", type=ISO20022_MessageElement, multiplicity=Multiplicity(0, 9999))
    }
)
dataDictionary44: BinaryAssociation = BinaryAssociation(
    name="dataDictionary44",
    ends={
        Property(name="DataDictionary", type=ISO20022_TopLevelDictionaryEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="topLevelDictionaryEntry", type=ISO20022_DataDictionary, multiplicity=Multiplicity(1, 1))
    }
)
repository45: BinaryAssociation = BinaryAssociation(
    name="repository45",
    ends={
        Property(name="Repository", type=ISO20022_DataDictionary, multiplicity=Multiplicity(1, 1)),
        Property(name="dataDictionary", type=ISO20022_Repository, multiplicity=Multiplicity(1, 1))
    }
)
topLevelDictionaryEntry46: BinaryAssociation = BinaryAssociation(
    name="topLevelDictionaryEntry46",
    ends={
        Property(name="TopLevelDictionaryEntry", type=ISO20022_DataDictionary, multiplicity=Multiplicity(1, 1)),
        Property(name="dataDictionary47", type=ISO20022_TopLevelDictionaryEntry, multiplicity=Multiplicity(0, 9999))
    }
)
businessProcessCatalogue48: BinaryAssociation = BinaryAssociation(
    name="businessProcessCatalogue48",
    ends={
        Property(name="BusinessProcessCatalogue", type=ISO20022_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository", type=ISO20022_BusinessProcessCatalogue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
diagrams49: BinaryAssociation = BinaryAssociation(
    name="diagrams49",
    ends={
        Property(name="Diagram", type=ISO20022_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository50", type=ISO20022_Diagram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataDictionary51: BinaryAssociation = BinaryAssociation(
    name="dataDictionary51",
    ends={
        Property(name="DataDictionary53", type=ISO20022_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository52", type=ISO20022_DataDictionary, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
topLevelCatalogueEntry54: BinaryAssociation = BinaryAssociation(
    name="topLevelCatalogueEntry54",
    ends={
        Property(name="TopLevelCatalogueEntry", type=ISO20022_BusinessProcessCatalogue, multiplicity=Multiplicity(1, 1)),
        Property(name="businessProcessCatalogue", type=ISO20022_TopLevelCatalogueEntry, multiplicity=Multiplicity(0, 9999))
    }
)
repository55: BinaryAssociation = BinaryAssociation(
    name="repository55",
    ends={
        Property(name="Repository57", type=ISO20022_BusinessProcessCatalogue, multiplicity=Multiplicity(1, 1)),
        Property(name="businessProcessCatalogue56", type=ISO20022_Repository, multiplicity=Multiplicity(1, 1))
    }
)
businessProcessCatalogue58: BinaryAssociation = BinaryAssociation(
    name="businessProcessCatalogue58",
    ends={
        Property(name="BusinessProcessCatalogue59", type=ISO20022_TopLevelCatalogueEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="topLevelCatalogueEntry", type=ISO20022_BusinessProcessCatalogue, multiplicity=Multiplicity(1, 1))
    }
)
repository60: BinaryAssociation = BinaryAssociation(
    name="repository60",
    ends={
        Property(name="Repository61", type=ISO20022_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagrams", type=ISO20022_Repository, multiplicity=Multiplicity(1, 1))
    }
)
trace68: BinaryAssociation = BinaryAssociation(
    name="trace68",
    ends={
        Property(name="BusinessComponent69", type=ISO20022_MessageComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="derivationComponent", type=ISO20022_BusinessComponent, multiplicity=Multiplicity(0, 1))
    }
)
derivation62: BinaryAssociation = BinaryAssociation(
    name="derivation62",
    ends={
        Property(name="MessageElement63", type=ISO20022_BusinessElement, multiplicity=Multiplicity(1, 1)),
        Property(name="businessElementTrace", type=ISO20022_MessageElement, multiplicity=Multiplicity(0, 9999))
    }
)
businessElementType64: BinaryAssociation = BinaryAssociation(
    name="businessElementType64",
    ends={
        Property(name="ISO20022_BusinessElementType", type=ISO20022_BusinessElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ISO20022_BusinessElement", type=ISO20022_BusinessElementType, multiplicity=Multiplicity(1, 1))
    }
)
elementContext65: BinaryAssociation = BinaryAssociation(
    name="elementContext65",
    ends={
        Property(name="BusinessComponent66", type=ISO20022_BusinessElement, multiplicity=Multiplicity(1, 1)),
        Property(name="element", type=ISO20022_BusinessComponent, multiplicity=Multiplicity(1, 1))
    }
)
messageBuildingBlock67: BinaryAssociation = BinaryAssociation(
    name="messageBuildingBlock67",
    ends={
        Property(name="MessageBuildingBlock", type=ISO20022_MessageComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="complexType", type=ISO20022_MessageBuildingBlock, multiplicity=Multiplicity(0, 9999))
    }
)
facets73: BinaryAssociation = BinaryAssociation(
    name="facets73",
    ends={
        Property(name="ISO20022_Facet", type=ISO20022_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="ISO20022_DataType74", type=ISO20022_Facet, multiplicity=Multiplicity(0, 9999))
    }
)
simpleType70: BinaryAssociation = BinaryAssociation(
    name="simpleType70",
    ends={
        Property(name="ISO20022_DataType", type=ISO20022_MessageBuildingBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="ISO20022_MessageBuildingBlock", type=ISO20022_DataType, multiplicity=Multiplicity(0, 1))
    }
)
complexType71: BinaryAssociation = BinaryAssociation(
    name="complexType71",
    ends={
        Property(name="MessageComponentType72", type=ISO20022_MessageBuildingBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="messageBuildingBlock", type=ISO20022_MessageComponentType, multiplicity=Multiplicity(0, 1))
    }
)
opposite76: BinaryAssociation = BinaryAssociation(
    name="opposite76",
    ends={
        Property(name="ISO20022_BusinessAssociationEnd", type=ISO20022_BusinessAssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="ISO20022_BusinessAssociationEnd75", type=ISO20022_BusinessAssociationEnd, multiplicity=Multiplicity(0, 1))
    }
)
messageElement79: BinaryAssociation = BinaryAssociation(
    name="messageElement79",
    ends={
        Property(name="MessageElement80", type=ISO20022_MessageElementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="componentContext", type=ISO20022_MessageElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type77: BinaryAssociation = BinaryAssociation(
    name="type77",
    ends={
        Property(name="BusinessComponent78", type=ISO20022_BusinessAssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="associationDomain", type=ISO20022_BusinessComponent, multiplicity=Multiplicity(1, 1))
    }
)
syntax87: BinaryAssociation = BinaryAssociation(
    name="syntax87",
    ends={
        Property(name="Syntax", type=ISO20022_Encoding, multiplicity=Multiplicity(1, 1)),
        Property(name="possibleEncodings", type=ISO20022_Syntax, multiplicity=Multiplicity(1, 1))
    }
)
simpleType81: BinaryAssociation = BinaryAssociation(
    name="simpleType81",
    ends={
        Property(name="ISO20022_DataType82", type=ISO20022_MessageAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ISO20022_MessageAttribute", type=ISO20022_DataType, multiplicity=Multiplicity(0, 1))
    }
)
complexType83: BinaryAssociation = BinaryAssociation(
    name="complexType83",
    ends={
        Property(name="ISO20022_MessageComponentType85", type=ISO20022_MessageAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ISO20022_MessageAttribute84", type=ISO20022_MessageComponentType, multiplicity=Multiplicity(0, 1))
    }
)
messageSet86: BinaryAssociation = BinaryAssociation(
    name="messageSet86",
    ends={
        Property(name="MessageSet", type=ISO20022_Encoding, multiplicity=Multiplicity(1, 1)),
        Property(name="validEncoding", type=ISO20022_MessageSet, multiplicity=Multiplicity(0, 9999))
    }
)
validEncoding93: BinaryAssociation = BinaryAssociation(
    name="validEncoding93",
    ends={
        Property(name="Encoding", type=ISO20022_MessageSet, multiplicity=Multiplicity(1, 1)),
        Property(name="messageSet94", type=ISO20022_Encoding, multiplicity=Multiplicity(1, 9999))
    }
)
messageDefinition88: BinaryAssociation = BinaryAssociation(
    name="messageDefinition88",
    ends={
        Property(name="MessageDefinition", type=ISO20022_MessageSet, multiplicity=Multiplicity(1, 1)),
        Property(name="messageSet", type=ISO20022_MessageDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
interactions89: BinaryAssociation = BinaryAssociation(
    name="interactions89",
    ends={
        Property(name="Interaction", type=ISO20022_MessageSet, multiplicity=Multiplicity(1, 1)),
        Property(name="messageSet90", type=ISO20022_Interaction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generatedSyntax91: BinaryAssociation = BinaryAssociation(
    name="generatedSyntax91",
    ends={
        Property(name="Syntax92", type=ISO20022_MessageSet, multiplicity=Multiplicity(1, 1)),
        Property(name="generatedFor", type=ISO20022_Syntax, multiplicity=Multiplicity(1, 9999))
    }
)
master96: BinaryAssociation = BinaryAssociation(
    name="master96",
    ends={
        Property(name="MessageDefinition97", type=ISO20022_MessageDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="subsets", type=ISO20022_MessageDefinition, multiplicity=Multiplicity(0, 1))
    }
)
subsets99: BinaryAssociation = BinaryAssociation(
    name="subsets99",
    ends={
        Property(name="MessageDefinition100", type=ISO20022_MessageDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="master", type=ISO20022_MessageDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
messageChoreography107: BinaryAssociation = BinaryAssociation(
    name="messageChoreography107",
    ends={
        Property(name="MessageChoreography", type=ISO20022_MessageDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="messageDefinition108", type=ISO20022_MessageChoreography, multiplicity=Multiplicity(1, 9999))
    }
)
businessArea101: BinaryAssociation = BinaryAssociation(
    name="businessArea101",
    ends={
        Property(name="BusinessArea", type=ISO20022_MessageDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="messageDefinition", type=ISO20022_BusinessArea, multiplicity=Multiplicity(1, 1))
    }
)
xors102: BinaryAssociation = BinaryAssociation(
    name="xors102",
    ends={
        Property(name="Xor", type=ISO20022_MessageDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="messageDefinition103", type=ISO20022_Xor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageBuildingBlock104: BinaryAssociation = BinaryAssociation(
    name="messageBuildingBlock104",
    ends={
        Property(name="ISO20022_MessageBuildingBlock105", type=ISO20022_MessageDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="ISO20022_MessageDefinition", type=ISO20022_MessageBuildingBlock, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
derivation106: BinaryAssociation = BinaryAssociation(
    name="derivation106",
    ends={
        Property(name="SyntaxMessageScheme", type=ISO20022_MessageDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="messageDefinitionTrace", type=ISO20022_SyntaxMessageScheme, multiplicity=Multiplicity(0, 9999))
    }
)
messageDefinitionIdentifier109: BinaryAssociation = BinaryAssociation(
    name="messageDefinitionIdentifier109",
    ends={
        Property(name="ISO20022_MessageDefinitionIdentifier", type=ISO20022_MessageDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="ISO20022_MessageDefinition110", type=ISO20022_MessageDefinitionIdentifier, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
messageSet111: BinaryAssociation = BinaryAssociation(
    name="messageSet111",
    ends={
        Property(name="MessageSet113", type=ISO20022_MessageDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="messageDefinition112", type=ISO20022_MessageSet, multiplicity=Multiplicity(0, 9999))
    }
)
messageDefinition114: BinaryAssociation = BinaryAssociation(
    name="messageDefinition114",
    ends={
        Property(name="MessageDefinition115", type=ISO20022_BusinessArea, multiplicity=Multiplicity(1, 1)),
        Property(name="businessArea", type=ISO20022_MessageDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xors124: BinaryAssociation = BinaryAssociation(
    name="xors124",
    ends={
        Property(name="Xor125", type=ISO20022_MessageComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="messageComponent", type=ISO20022_Xor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
impactedElements116: BinaryAssociation = BinaryAssociation(
    name="impactedElements116",
    ends={
        Property(name="ISO20022_MessageElement", type=ISO20022_Xor, multiplicity=Multiplicity(1, 1)),
        Property(name="ISO20022_Xor", type=ISO20022_MessageElement, multiplicity=Multiplicity(0, 9999))
    }
)
messageComponent117: BinaryAssociation = BinaryAssociation(
    name="messageComponent117",
    ends={
        Property(name="MessageComponent", type=ISO20022_Xor, multiplicity=Multiplicity(1, 1)),
        Property(name="xors", type=ISO20022_MessageComponent, multiplicity=Multiplicity(0, 1))
    }
)
impactedMessageBuildingBlocks118: BinaryAssociation = BinaryAssociation(
    name="impactedMessageBuildingBlocks118",
    ends={
        Property(name="ISO20022_MessageBuildingBlock120", type=ISO20022_Xor, multiplicity=Multiplicity(1, 1)),
        Property(name="ISO20022_Xor119", type=ISO20022_MessageBuildingBlock, multiplicity=Multiplicity(0, 9999))
    }
)
messageDefinition121: BinaryAssociation = BinaryAssociation(
    name="messageDefinition121",
    ends={
        Property(name="MessageDefinition123", type=ISO20022_Xor, multiplicity=Multiplicity(1, 1)),
        Property(name="xors122", type=ISO20022_MessageDefinition, multiplicity=Multiplicity(0, 1))
    }
)
messageDefinitionTrace126: BinaryAssociation = BinaryAssociation(
    name="messageDefinitionTrace126",
    ends={
        Property(name="MessageDefinition128", type=ISO20022_SyntaxMessageScheme, multiplicity=Multiplicity(1, 1)),
        Property(name="derivation127", type=ISO20022_MessageDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
messageDefinition129: BinaryAssociation = BinaryAssociation(
    name="messageDefinition129",
    ends={
        Property(name="MessageDefinition130", type=ISO20022_MessageChoreography, multiplicity=Multiplicity(1, 1)),
        Property(name="messageChoreography", type=ISO20022_MessageDefinition, multiplicity=Multiplicity(1, 9999))
    }
)
messages132: BinaryAssociation = BinaryAssociation(
    name="messages132",
    ends={
        Property(name="InteractionMessage", type=ISO20022_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction133", type=ISO20022_InteractionMessage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actors131: BinaryAssociation = BinaryAssociation(
    name="actors131",
    ends={
        Property(name="InteractionActor", type=ISO20022_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction", type=ISO20022_InteractionActor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interaction138: BinaryAssociation = BinaryAssociation(
    name="interaction138",
    ends={
        Property(name="Interaction139", type=ISO20022_InteractionActor, multiplicity=Multiplicity(1, 1)),
        Property(name="actors", type=ISO20022_Interaction, multiplicity=Multiplicity(1, 1))
    }
)
diagram134: BinaryAssociation = BinaryAssociation(
    name="diagram134",
    ends={
        Property(name="ISO20022_Diagram", type=ISO20022_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="ISO20022_Interaction", type=ISO20022_Diagram, multiplicity=Multiplicity(0, 1))
    }
)
messageSet135: BinaryAssociation = BinaryAssociation(
    name="messageSet135",
    ends={
        Property(name="MessageSet136", type=ISO20022_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="interactions", type=ISO20022_MessageSet, multiplicity=Multiplicity(1, 1))
    }
)
businessActor137: BinaryAssociation = BinaryAssociation(
    name="businessActor137",
    ends={
        Property(name="ISO20022_BusinessRole", type=ISO20022_InteractionActor, multiplicity=Multiplicity(1, 1)),
        Property(name="ISO20022_InteractionActor", type=ISO20022_BusinessRole, multiplicity=Multiplicity(0, 1))
    }
)
sender140: BinaryAssociation = BinaryAssociation(
    name="sender140",
    ends={
        Property(name="ISO20022_InteractionActor141", type=ISO20022_InteractionMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="ISO20022_InteractionMessage", type=ISO20022_InteractionActor, multiplicity=Multiplicity(1, 1))
    }
)
receiver142: BinaryAssociation = BinaryAssociation(
    name="receiver142",
    ends={
        Property(name="ISO20022_InteractionActor144", type=ISO20022_InteractionMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="ISO20022_InteractionMessage143", type=ISO20022_InteractionActor, multiplicity=Multiplicity(1, 1))
    }
)
interaction145: BinaryAssociation = BinaryAssociation(
    name="interaction145",
    ends={
        Property(name="Interaction146", type=ISO20022_InteractionMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="messages", type=ISO20022_Interaction, multiplicity=Multiplicity(1, 1))
    }
)
simpleType151: BinaryAssociation = BinaryAssociation(
    name="simpleType151",
    ends={
        Property(name="ISO20022_DataType152", type=ISO20022_BusinessAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ISO20022_BusinessAttribute", type=ISO20022_DataType, multiplicity=Multiplicity(0, 1))
    }
)
possibleEncodings147: BinaryAssociation = BinaryAssociation(
    name="possibleEncodings147",
    ends={
        Property(name="Encoding148", type=ISO20022_Syntax, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax", type=ISO20022_Encoding, multiplicity=Multiplicity(1, 9999))
    }
)
generatedFor149: BinaryAssociation = BinaryAssociation(
    name="generatedFor149",
    ends={
        Property(name="MessageSet150", type=ISO20022_Syntax, multiplicity=Multiplicity(1, 1)),
        Property(name="generatedSyntax", type=ISO20022_MessageSet, multiplicity=Multiplicity(0, 9999))
    }
)
complexType153: BinaryAssociation = BinaryAssociation(
    name="complexType153",
    ends={
        Property(name="ISO20022_BusinessComponent", type=ISO20022_BusinessAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ISO20022_BusinessAttribute154", type=ISO20022_BusinessComponent, multiplicity=Multiplicity(0, 1))
    }
)
owner155: BinaryAssociation = BinaryAssociation(
    name="owner155",
    ends={
        Property(name="CodeSet", type=ISO20022_Code, multiplicity=Multiplicity(1, 1)),
        Property(name="code", type=ISO20022_CodeSet, multiplicity=Multiplicity(1, 1))
    }
)
currencyIdentifierSet166: BinaryAssociation = BinaryAssociation(
    name="currencyIdentifierSet166",
    ends={
        Property(name="ISO20022_IdentifierSet", type=ISO20022_Amount, multiplicity=Multiplicity(1, 1)),
        Property(name="ISO20022_Amount", type=ISO20022_IdentifierSet, multiplicity=Multiplicity(0, 1))
    }
)
trace157: BinaryAssociation = BinaryAssociation(
    name="trace157",
    ends={
        Property(name="CodeSet159", type=ISO20022_CodeSet, multiplicity=Multiplicity(1, 1)),
        Property(name="derivation158", type=ISO20022_CodeSet, multiplicity=Multiplicity(0, 1))
    }
)
derivation161: BinaryAssociation = BinaryAssociation(
    name="derivation161",
    ends={
        Property(name="CodeSet163", type=ISO20022_CodeSet, multiplicity=Multiplicity(1, 1)),
        Property(name="trace162", type=ISO20022_CodeSet, multiplicity=Multiplicity(0, 9999))
    }
)
code164: BinaryAssociation = BinaryAssociation(
    name="code164",
    ends={
        Property(name="Code", type=ISO20022_CodeSet, multiplicity=Multiplicity(1, 1)),
        Property(name="owner165", type=ISO20022_Code, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endPoints167: BinaryAssociation = BinaryAssociation(
    name="endPoints167",
    ends={
        Property(name="ISO20022_MessageElementContainer", type=ISO20022_EndPointCategory, multiplicity=Multiplicity(1, 1)),
        Property(name="ISO20022_EndPointCategory", type=ISO20022_MessageElementContainer, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_ISO20022_RepositoryConcept_ModelEntity = Generalization(general=ModelEntity, specific=ISO20022_RepositoryConcept)
gen_ISO20022_SemanticMarkup_ModelEntity = Generalization(general=ModelEntity, specific=ISO20022_SemanticMarkup)
gen_ISO20022_SemanticMarkupElement_ModelEntity = Generalization(general=ModelEntity, specific=ISO20022_SemanticMarkupElement)
gen_ISO20022_Doclet_ModelEntity = Generalization(general=ModelEntity, specific=ISO20022_Doclet)
gen_ISO20022_MessageAssociationEnd_MessageElement = Generalization(general=MessageElement, specific=ISO20022_MessageAssociationEnd)
gen_ISO20022_MessageElement_XMLMember = Generalization(general=XMLMember, specific=ISO20022_MessageElement)
gen_ISO20022_MessageElement_MessageConcept = Generalization(general=MessageConcept, specific=ISO20022_MessageElement)
gen_ISO20022_XMLMember_Member = Generalization(general=Member, specific=ISO20022_XMLMember)
gen_ISO20022_Member_RepositoryConcept = Generalization(general=RepositoryConcept, specific=ISO20022_Member)
gen_ISO20022_Member_MultiplicityEntity = Generalization(general=MultiplicityEntity, specific=ISO20022_Member)
gen_ISO20022_Type_RepositoryConcept = Generalization(general=RepositoryConcept, specific=ISO20022_Type)
gen_ISO20022_LogicalType_Type = Generalization(general=Type, specific=ISO20022_LogicalType)
gen_ISO20022_IsAnAlternativeFor_RepositoryConcept = Generalization(general=RepositoryConcept, specific=ISO20022_IsAnAlternativeFor)
gen_ISO20022_MessageConcept_ModelEntity = Generalization(general=ModelEntity, specific=ISO20022_MessageConcept)
gen_ISO20022_BusinessComponent_BusinessElementType = Generalization(general=BusinessElementType, specific=ISO20022_BusinessComponent)
gen_ISO20022_BusinessComponent_TopLevelDictionaryEntry = Generalization(general=TopLevelDictionaryEntry, specific=ISO20022_BusinessComponent)
gen_ISO20022_BusinessComponent_BusinessConcept = Generalization(general=BusinessConcept, specific=ISO20022_BusinessComponent)
gen_ISO20022_BusinessElementType_Type = Generalization(general=Type, specific=ISO20022_BusinessElementType)
gen_ISO20022_BusinessProcessCatalogue_ModelEntity = Generalization(general=ModelEntity, specific=ISO20022_BusinessProcessCatalogue)
gen_ISO20022_BusinessConcept_ModelEntity = Generalization(general=ModelEntity, specific=ISO20022_BusinessConcept)
gen_ISO20022_TopLevelDictionaryEntry_RepositoryConcept = Generalization(general=RepositoryConcept, specific=ISO20022_TopLevelDictionaryEntry)
gen_ISO20022_DataDictionary_ModelEntity = Generalization(general=ModelEntity, specific=ISO20022_DataDictionary)
gen_ISO20022_Repository_ModelEntity = Generalization(general=ModelEntity, specific=ISO20022_Repository)
gen_ISO20022_BusinessElement_Member = Generalization(general=Member, specific=ISO20022_BusinessElement)
gen_ISO20022_BusinessElement_BusinessConcept = Generalization(general=BusinessConcept, specific=ISO20022_BusinessElement)
gen_ISO20022_TopLevelCatalogueEntry_RepositoryConcept = Generalization(general=RepositoryConcept, specific=ISO20022_TopLevelCatalogueEntry)
gen_ISO20022_Diagram_RepositoryConcept = Generalization(general=RepositoryConcept, specific=ISO20022_Diagram)
gen_ISO20022_MessageBuildingBlock_XMLMember = Generalization(general=XMLMember, specific=ISO20022_MessageBuildingBlock)
gen_ISO20022_MessageComponentType_LogicalType = Generalization(general=LogicalType, specific=ISO20022_MessageComponentType)
gen_ISO20022_MessageComponentType_TopLevelDictionaryEntry = Generalization(general=TopLevelDictionaryEntry, specific=ISO20022_MessageComponentType)
gen_ISO20022_MessageComponentType_MessageConcept = Generalization(general=MessageConcept, specific=ISO20022_MessageComponentType)
gen_ISO20022_DataType_LogicalType = Generalization(general=LogicalType, specific=ISO20022_DataType)
gen_ISO20022_DataType_BusinessElementType = Generalization(general=BusinessElementType, specific=ISO20022_DataType)
gen_ISO20022_DataType_TopLevelDictionaryEntry = Generalization(general=TopLevelDictionaryEntry, specific=ISO20022_DataType)
gen_ISO20022_Facet_ModelEntity = Generalization(general=ModelEntity, specific=ISO20022_Facet)
gen_ISO20022_BusinessAssociationEnd_BusinessElement = Generalization(general=BusinessElement, specific=ISO20022_BusinessAssociationEnd)
gen_ISO20022_MessageElementContainer_MessageComponentType = Generalization(general=MessageComponentType, specific=ISO20022_MessageElementContainer)
gen_ISO20022_MessageAttribute_MessageElement = Generalization(general=MessageElement, specific=ISO20022_MessageAttribute)
gen_ISO20022_Encoding_ModelEntity = Generalization(general=ModelEntity, specific=ISO20022_Encoding)
gen_ISO20022_MessageDefinition_Type = Generalization(general=Type, specific=ISO20022_MessageDefinition)
gen_ISO20022_MessageSet_TopLevelCatalogueEntry = Generalization(general=TopLevelCatalogueEntry, specific=ISO20022_MessageSet)
gen_ISO20022_Xor_RepositoryConcept = Generalization(general=RepositoryConcept, specific=ISO20022_Xor)
gen_ISO20022_BusinessArea_TopLevelCatalogueEntry = Generalization(general=TopLevelCatalogueEntry, specific=ISO20022_BusinessArea)
gen_ISO20022_MessageComponent_MessageElementContainer = Generalization(general=MessageElementContainer, specific=ISO20022_MessageComponent)
gen_ISO20022_SyntaxMessageScheme_TopLevelCatalogueEntry = Generalization(general=TopLevelCatalogueEntry, specific=ISO20022_SyntaxMessageScheme)
gen_ISO20022_MessageChoreography_TopLevelCatalogueEntry = Generalization(general=TopLevelCatalogueEntry, specific=ISO20022_MessageChoreography)
gen_ISO20022_Interaction_RepositoryConcept = Generalization(general=RepositoryConcept, specific=ISO20022_Interaction)
gen_ISO20022_InteractionActor_RepositoryConcept = Generalization(general=RepositoryConcept, specific=ISO20022_InteractionActor)
gen_ISO20022_Syntax_ModelEntity = Generalization(general=ModelEntity, specific=ISO20022_Syntax)
gen_ISO20022_BusinessRole_RepositoryConcept = Generalization(general=RepositoryConcept, specific=ISO20022_BusinessRole)
gen_ISO20022_InteractionMessage_RepositoryConcept = Generalization(general=RepositoryConcept, specific=ISO20022_InteractionMessage)
gen_ISO20022_BusinessAttribute_BusinessElement = Generalization(general=BusinessElement, specific=ISO20022_BusinessAttribute)
gen_ISO20022_IdentifierSet_XSDString = Generalization(general=XSDString, specific=ISO20022_IdentifierSet)
gen_ISO20022_Text_XSDString = Generalization(general=XSDString, specific=ISO20022_Text)
gen_ISO20022_XSDString_DataType = Generalization(general=DataType, specific=ISO20022_XSDString)
gen_ISO20022_XSDDecimal_DataType = Generalization(general=DataType, specific=ISO20022_XSDDecimal)
gen_ISO20022_Indicator_XSDBoolean = Generalization(general=XSDBoolean, specific=ISO20022_Indicator)
gen_ISO20022_XSDBoolean_DataType = Generalization(general=DataType, specific=ISO20022_XSDBoolean)
gen_ISO20022_Rate_XSDDecimal = Generalization(general=XSDDecimal, specific=ISO20022_Rate)
gen_ISO20022_ExternalSchema_MessageComponentType = Generalization(general=MessageComponentType, specific=ISO20022_ExternalSchema)
gen_ISO20022_CodeSet_XSDString = Generalization(general=XSDString, specific=ISO20022_CodeSet)
gen_ISO20022_Quantity_XSDDecimal = Generalization(general=XSDDecimal, specific=ISO20022_Quantity)
gen_ISO20022_Code_RepositoryConcept = Generalization(general=RepositoryConcept, specific=ISO20022_Code)
gen_ISO20022_ChoiceComponent_MessageElementContainer = Generalization(general=MessageElementContainer, specific=ISO20022_ChoiceComponent)
gen_ISO20022_Amount_XSDDecimal = Generalization(general=XSDDecimal, specific=ISO20022_Amount)
gen_ISO20022_AbstractTimeConcept_DataType = Generalization(general=DataType, specific=ISO20022_AbstractTimeConcept)
gen_ISO20022_XSDBinary_DataType = Generalization(general=DataType, specific=ISO20022_XSDBinary)
gen_ISO20022_EndPointCategory_TopLevelDictionaryEntry = Generalization(general=TopLevelDictionaryEntry, specific=ISO20022_EndPointCategory)
gen_ISO20022_ApplicationHeader_MessageDefinition = Generalization(general=MessageDefinition, specific=ISO20022_ApplicationHeader)
gen_ISO20022_XSDDuration_AbstractTimeConcept = Generalization(general=AbstractTimeConcept, specific=ISO20022_XSDDuration)
gen_ISO20022_XSDID_XSDString = Generalization(general=XSDString, specific=ISO20022_XSDID)
gen_ISO20022_XSDDate_AbstractTimeConcept = Generalization(general=AbstractTimeConcept, specific=ISO20022_XSDDate)
gen_ISO20022_XSDDateTime_AbstractTimeConcept = Generalization(general=AbstractTimeConcept, specific=ISO20022_XSDDateTime)
gen_ISO20022_XSDDay_AbstractTimeConcept = Generalization(general=AbstractTimeConcept, specific=ISO20022_XSDDay)
gen_ISO20022_SWIFTSolution_MessageSet = Generalization(general=MessageSet, specific=ISO20022_SWIFTSolution)
gen_ISO20022_XSDMonth_AbstractTimeConcept = Generalization(general=AbstractTimeConcept, specific=ISO20022_XSDMonth)
gen_ISO20022_XSDMonthDay_AbstractTimeConcept = Generalization(general=AbstractTimeConcept, specific=ISO20022_XSDMonthDay)
gen_ISO20022_XSDTime_AbstractTimeConcept = Generalization(general=AbstractTimeConcept, specific=ISO20022_XSDTime)
gen_ISO20022_XSDYear_AbstractTimeConcept = Generalization(general=AbstractTimeConcept, specific=ISO20022_XSDYear)
gen_ISO20022_XSDYearMonth_AbstractTimeConcept = Generalization(general=AbstractTimeConcept, specific=ISO20022_XSDYearMonth)
gen_ISO20022_UserDefined_MessageComponentType = Generalization(general=MessageComponentType, specific=ISO20022_UserDefined)

# Domain Model
domain_model = DomainModel(
    name="ISO20022",
    types={ISO20022_Constraint, ISO20022_RepositoryConcept, ModelEntity, ISO20022_SemanticMarkup, ISO20022_Doclet, ISO20022_ModelEntity, ISO20022_SemanticMarkupElement, ISO20022_MessageAssociationEnd, MessageElement, ISO20022_MessageComponentType, ISO20022_MessageElement, XMLMember, MessageConcept, ISO20022_BusinessComponent, ISO20022_BusinessElement, ISO20022_MessageElementContainer, ISO20022_XMLMember, Member, ISO20022_LogicalType, ISO20022_Member, RepositoryConcept, MultiplicityEntity, ISO20022_Type, ISO20022_MultiplicityEntity, Type, ISO20022_IsAnAlternativeFor, ISO20022_MessageConcept, BusinessElementType, TopLevelDictionaryEntry, BusinessConcept, ISO20022_BusinessAssociationEnd, ISO20022_BusinessConcept, ISO20022_TopLevelDictionaryEntry, ISO20022_DataDictionary, ISO20022_Repository, ISO20022_BusinessProcessCatalogue, ISO20022_Diagram, ISO20022_BusinessElementType, ISO20022_TopLevelCatalogueEntry, LogicalType, ISO20022_MessageBuildingBlock, ISO20022_Facet, ISO20022_DataType, BusinessElement, MessageComponentType, ISO20022_Syntax, ISO20022_MessageAttribute, ISO20022_Encoding, ISO20022_MessageSet, TopLevelCatalogueEntry, ISO20022_MessageDefinition, ISO20022_Interaction, ISO20022_MessageChoreography, ISO20022_BusinessArea, ISO20022_Xor, ISO20022_SyntaxMessageScheme, ISO20022_MessageDefinitionIdentifier, ISO20022_MessageComponent, MessageElementContainer, ISO20022_InteractionMessage, ISO20022_InteractionActor, ISO20022_BusinessRole, ISO20022_BusinessAttribute, ISO20022_IdentifierSet, ISO20022_Text, XSDString, ISO20022_XSDString, DataType, ISO20022_XSDDecimal, ISO20022_Indicator, XSDBoolean, ISO20022_XSDBoolean, ISO20022_Rate, XSDDecimal, ISO20022_ExternalSchema, ISO20022_CodeSet, ISO20022_Quantity, ISO20022_Code, ISO20022_ChoiceComponent, ISO20022_Amount, ISO20022_AbstractTimeConcept, ISO20022_XSDBinary, ISO20022_EndPointCategory, ISO20022_ApplicationHeader, MessageDefinition, ISO20022_XSDID, ISO20022_XSDDate, AbstractTimeConcept, ISO20022_XSDDateTime, ISO20022_XSDDay, ISO20022_XSDDuration, ISO20022_SWIFTSolution, MessageSet, ISO20022_XSDMonth, ISO20022_XSDMonthDay, ISO20022_XSDTime, ISO20022_XSDYear, ISO20022_XSDYearMonth, ISO20022_UserDefined, RegistrationStatus, Aggregation, Visibility, ProcessContent, Namespace},
    associations={owner0, semanticMarkup1, doclet2, constraint4, nextVersions6, previousVersion8, elements10, type12, opposite14, businessComponentTrace16, businessElementTrace17, componentContext18, xmlMemberType19, memberType20, typedMember21, isAnAlternativeFors22, derivations24, derivedFroms27, typedXMLMember29, target30, source31, subType34, superType37, element39, derivationComponent41, associationDomain42, derivationElement43, dataDictionary44, repository45, topLevelDictionaryEntry46, businessProcessCatalogue48, diagrams49, dataDictionary51, topLevelCatalogueEntry54, repository55, businessProcessCatalogue58, repository60, trace68, derivation62, businessElementType64, elementContext65, messageBuildingBlock67, facets73, simpleType70, complexType71, opposite76, messageElement79, type77, syntax87, simpleType81, complexType83, messageSet86, validEncoding93, messageDefinition88, interactions89, generatedSyntax91, master96, subsets99, messageChoreography107, businessArea101, xors102, messageBuildingBlock104, derivation106, messageDefinitionIdentifier109, messageSet111, messageDefinition114, xors124, impactedElements116, messageComponent117, impactedMessageBuildingBlocks118, messageDefinition121, messageDefinitionTrace126, messageDefinition129, messages132, actors131, interaction138, diagram134, messageSet135, businessActor137, sender140, receiver142, interaction145, simpleType151, possibleEncodings147, generatedFor149, complexType153, owner155, currencyIdentifierSet166, trace157, derivation161, code164, endPoints167},
    generalizations={gen_ISO20022_RepositoryConcept_ModelEntity, gen_ISO20022_SemanticMarkup_ModelEntity, gen_ISO20022_SemanticMarkupElement_ModelEntity, gen_ISO20022_Doclet_ModelEntity, gen_ISO20022_MessageAssociationEnd_MessageElement, gen_ISO20022_MessageElement_XMLMember, gen_ISO20022_MessageElement_MessageConcept, gen_ISO20022_XMLMember_Member, gen_ISO20022_Member_RepositoryConcept, gen_ISO20022_Member_MultiplicityEntity, gen_ISO20022_Type_RepositoryConcept, gen_ISO20022_LogicalType_Type, gen_ISO20022_IsAnAlternativeFor_RepositoryConcept, gen_ISO20022_MessageConcept_ModelEntity, gen_ISO20022_BusinessComponent_BusinessElementType, gen_ISO20022_BusinessComponent_TopLevelDictionaryEntry, gen_ISO20022_BusinessComponent_BusinessConcept, gen_ISO20022_BusinessElementType_Type, gen_ISO20022_BusinessProcessCatalogue_ModelEntity, gen_ISO20022_BusinessConcept_ModelEntity, gen_ISO20022_TopLevelDictionaryEntry_RepositoryConcept, gen_ISO20022_DataDictionary_ModelEntity, gen_ISO20022_Repository_ModelEntity, gen_ISO20022_BusinessElement_Member, gen_ISO20022_BusinessElement_BusinessConcept, gen_ISO20022_TopLevelCatalogueEntry_RepositoryConcept, gen_ISO20022_Diagram_RepositoryConcept, gen_ISO20022_MessageBuildingBlock_XMLMember, gen_ISO20022_MessageComponentType_LogicalType, gen_ISO20022_MessageComponentType_TopLevelDictionaryEntry, gen_ISO20022_MessageComponentType_MessageConcept, gen_ISO20022_DataType_LogicalType, gen_ISO20022_DataType_BusinessElementType, gen_ISO20022_DataType_TopLevelDictionaryEntry, gen_ISO20022_Facet_ModelEntity, gen_ISO20022_BusinessAssociationEnd_BusinessElement, gen_ISO20022_MessageElementContainer_MessageComponentType, gen_ISO20022_MessageAttribute_MessageElement, gen_ISO20022_Encoding_ModelEntity, gen_ISO20022_MessageDefinition_Type, gen_ISO20022_MessageSet_TopLevelCatalogueEntry, gen_ISO20022_Xor_RepositoryConcept, gen_ISO20022_BusinessArea_TopLevelCatalogueEntry, gen_ISO20022_MessageComponent_MessageElementContainer, gen_ISO20022_SyntaxMessageScheme_TopLevelCatalogueEntry, gen_ISO20022_MessageChoreography_TopLevelCatalogueEntry, gen_ISO20022_Interaction_RepositoryConcept, gen_ISO20022_InteractionActor_RepositoryConcept, gen_ISO20022_Syntax_ModelEntity, gen_ISO20022_BusinessRole_RepositoryConcept, gen_ISO20022_InteractionMessage_RepositoryConcept, gen_ISO20022_BusinessAttribute_BusinessElement, gen_ISO20022_IdentifierSet_XSDString, gen_ISO20022_Text_XSDString, gen_ISO20022_XSDString_DataType, gen_ISO20022_XSDDecimal_DataType, gen_ISO20022_Indicator_XSDBoolean, gen_ISO20022_XSDBoolean_DataType, gen_ISO20022_Rate_XSDDecimal, gen_ISO20022_ExternalSchema_MessageComponentType, gen_ISO20022_CodeSet_XSDString, gen_ISO20022_Quantity_XSDDecimal, gen_ISO20022_Code_RepositoryConcept, gen_ISO20022_ChoiceComponent_MessageElementContainer, gen_ISO20022_Amount_XSDDecimal, gen_ISO20022_AbstractTimeConcept_DataType, gen_ISO20022_XSDBinary_DataType, gen_ISO20022_EndPointCategory_TopLevelDictionaryEntry, gen_ISO20022_ApplicationHeader_MessageDefinition, gen_ISO20022_XSDDuration_AbstractTimeConcept, gen_ISO20022_XSDID_XSDString, gen_ISO20022_XSDDate_AbstractTimeConcept, gen_ISO20022_XSDDateTime_AbstractTimeConcept, gen_ISO20022_XSDDay_AbstractTimeConcept, gen_ISO20022_SWIFTSolution_MessageSet, gen_ISO20022_XSDMonth_AbstractTimeConcept, gen_ISO20022_XSDMonthDay_AbstractTimeConcept, gen_ISO20022_XSDTime_AbstractTimeConcept, gen_ISO20022_XSDYear_AbstractTimeConcept, gen_ISO20022_XSDYearMonth_AbstractTimeConcept, gen_ISO20022_UserDefined_MessageComponentType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)