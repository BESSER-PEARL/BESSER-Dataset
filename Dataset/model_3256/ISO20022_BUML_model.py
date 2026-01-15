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
            EnumerationLiteral(name="OBSOLETE"),
			EnumerationLiteral(name="PROVISIONALLY_REGISTERED"),
			EnumerationLiteral(name="REGISTERED")
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

DeliveryAssurance: Enumeration = Enumeration(
    name="DeliveryAssurance",
    literals={
            EnumerationLiteral(name="AT_LEAST_ONCE"),
			EnumerationLiteral(name="EXACTLY_ONCE"),
			EnumerationLiteral(name="AT_MOST_ONCE")
    }
)

MessageCasting: Enumeration = Enumeration(
    name="MessageCasting",
    literals={
            EnumerationLiteral(name="UNICAST"),
			EnumerationLiteral(name="MULTICAST"),
			EnumerationLiteral(name="BROADCAST"),
			EnumerationLiteral(name="ANYCAST")
    }
)

MessageDeliveryOrder: Enumeration = Enumeration(
    name="MessageDeliveryOrder",
    literals={
            EnumerationLiteral(name="EXPECTED_CAUSAL_ORDER"),
			EnumerationLiteral(name="FIFO_ORDERED"),
			EnumerationLiteral(name="UNORDERED")
    }
)

Durability: Enumeration = Enumeration(
    name="Durability",
    literals={
            EnumerationLiteral(name="TRANSIENT"),
			EnumerationLiteral(name="DURABLE"),
			EnumerationLiteral(name="PERSISTENT")
    }
)

MessageValidationOnOff: Enumeration = Enumeration(
    name="MessageValidationOnOff",
    literals={
            EnumerationLiteral(name="VALIDATION_ON"),
			EnumerationLiteral(name="VALIDATION_OFF")
    }
)

MessageValidationLevel: Enumeration = Enumeration(
    name="MessageValidationLevel",
    literals={
            EnumerationLiteral(name="SCHEMA_VALID"),
			EnumerationLiteral(name="MESSAGE_VALID"),
			EnumerationLiteral(name="RULE_VALID"),
			EnumerationLiteral(name="MARKET_PRACTICE_VALID"),
			EnumerationLiteral(name="BUSINESS_PROCESS_VALID"),
			EnumerationLiteral(name="COMPLETELY_VALID"),
			EnumerationLiteral(name="NO_VALIDATION"),
			EnumerationLiteral(name="SYNTAX_VALID")
    }
)

ReceiverAsynchronicity: Enumeration = Enumeration(
    name="ReceiverAsynchronicity",
    literals={
            EnumerationLiteral(name="ENDPOINT_SYNCHRONOUS"),
			EnumerationLiteral(name="CONVERSATION_SYNCHRONOUS"),
			EnumerationLiteral(name="ASYNCHRONOUS")
    }
)

SenderAsynchronicity: Enumeration = Enumeration(
    name="SenderAsynchronicity",
    literals={
            EnumerationLiteral(name="ENDPOINT_SYNCHRONOUS"),
			EnumerationLiteral(name="CONVERSATION_SYNCHRONOUS"),
			EnumerationLiteral(name="ASYNCHRONOUS")
    }
)

MessageValidationResults: Enumeration = Enumeration(
    name="MessageValidationResults",
    literals={
            EnumerationLiteral(name="REJECT"),
			EnumerationLiteral(name="REJECT_AND_DELIVER"),
			EnumerationLiteral(name="DELIVER")
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

SchemaTypeKind: Enumeration = Enumeration(
    name="SchemaTypeKind",
    literals={
            EnumerationLiteral(name="anySimpleType"),
			EnumerationLiteral(name="anyURI"),
			EnumerationLiteral(name="base64Binary"),
			EnumerationLiteral(name="boolean"),
			EnumerationLiteral(name="byte"),
			EnumerationLiteral(name="date"),
			EnumerationLiteral(name="dateTime"),
			EnumerationLiteral(name="decimal"),
			EnumerationLiteral(name="double"),
			EnumerationLiteral(name="duration"),
			EnumerationLiteral(name="ENTITIES"),
			EnumerationLiteral(name="ENTITY"),
			EnumerationLiteral(name="IDREFS"),
			EnumerationLiteral(name="int"),
			EnumerationLiteral(name="integer"),
			EnumerationLiteral(name="language"),
			EnumerationLiteral(name="long"),
			EnumerationLiteral(name="Name"),
			EnumerationLiteral(name="NCName"),
			EnumerationLiteral(name="negativeInteger"),
			EnumerationLiteral(name="NMTOKEN"),
			EnumerationLiteral(name="NMTOKENS"),
			EnumerationLiteral(name="nonNegativeInteger"),
			EnumerationLiteral(name="nonPositiveInteger"),
			EnumerationLiteral(name="normalizedString"),
			EnumerationLiteral(name="positiveInteger"),
			EnumerationLiteral(name="QName"),
			EnumerationLiteral(name="short"),
			EnumerationLiteral(name="string"),
			EnumerationLiteral(name="time"),
			EnumerationLiteral(name="float"),
			EnumerationLiteral(name="gDay"),
			EnumerationLiteral(name="gMonth"),
			EnumerationLiteral(name="gMonthDay"),
			EnumerationLiteral(name="gYear"),
			EnumerationLiteral(name="gYearMonth"),
			EnumerationLiteral(name="hexBinary"),
			EnumerationLiteral(name="ID"),
			EnumerationLiteral(name="IDREF"),
			EnumerationLiteral(name="token"),
			EnumerationLiteral(name="unsignedByte"),
			EnumerationLiteral(name="unsignedInt"),
			EnumerationLiteral(name="unsignedLong"),
			EnumerationLiteral(name="unsignedShort")
    }
)

ISO20022Version: Enumeration = Enumeration(
    name="ISO20022Version",
    literals={
            EnumerationLiteral(name="_2013"),
			EnumerationLiteral(name="_2004")
    }
)

# Classes
iso20022_Address = Class(name="iso20022::Address")
ModelEntity = Class(name="ModelEntity")
iso20022_ModelEntity = Class(name="iso20022::ModelEntity", is_abstract=True)
iso20022_BroadcastList = Class(name="iso20022::BroadcastList")
iso20022_MessagingEndpoint = Class(name="iso20022::MessagingEndpoint")
iso20022_MessageTransportSystem = Class(name="iso20022::MessageTransportSystem")
iso20022_TransportMessage = Class(name="iso20022::TransportMessage")
iso20022_MessageInstance = Class(name="iso20022::MessageInstance")
TopLevelCatalogueEntry = Class(name="TopLevelCatalogueEntry")
iso20022_MessageDefinition = Class(name="iso20022::MessageDefinition")
iso20022_TopLevelCatalogueEntry = Class(name="iso20022::TopLevelCatalogueEntry", is_abstract=True)
RepositoryConcept = Class(name="RepositoryConcept")
iso20022_BusinessProcessCatalogue = Class(name="iso20022::BusinessProcessCatalogue")
iso20022_RepositoryConcept = Class(name="iso20022::RepositoryConcept", is_abstract=True)
iso20022_SyntaxMessageScheme = Class(name="iso20022::SyntaxMessageScheme")
iso20022_SemanticMarkup = Class(name="iso20022::SemanticMarkup")
iso20022_Doclet = Class(name="iso20022::Doclet")
iso20022_SemanticMarkupElement = Class(name="iso20022::SemanticMarkupElement")
iso20022_Constraint = Class(name="iso20022::Constraint")
iso20022_Repository = Class(name="iso20022::Repository")
iso20022_TopLevelDictionaryEntry = Class(name="iso20022::TopLevelDictionaryEntry", is_abstract=True)
iso20022_DataDictionary = Class(name="iso20022::DataDictionary")
iso20022_MessageSet = Class(name="iso20022::MessageSet")
iso20022_BusinessArea = Class(name="iso20022::BusinessArea")
RepositoryType = Class(name="RepositoryType")
iso20022_MessageChoreography = Class(name="iso20022::MessageChoreography")
iso20022_MessageTransmission = Class(name="iso20022::MessageTransmission")
iso20022_MessageDefinitionIdentifier = Class(name="iso20022::MessageDefinitionIdentifier")
iso20022_Xor = Class(name="iso20022::Xor")
iso20022_MessageBuildingBlock = Class(name="iso20022::MessageBuildingBlock")
iso20022_Syntax = Class(name="iso20022::Syntax")
iso20022_Encoding = Class(name="iso20022::Encoding")
iso20022_RepositoryType = Class(name="iso20022::RepositoryType", is_abstract=True)
iso20022_MessageElement = Class(name="iso20022::MessageElement", is_abstract=True)
iso20022_MessageComponent = Class(name="iso20022::MessageComponent")
iso20022_BusinessComponent = Class(name="iso20022::BusinessComponent")
MessageConstruct = Class(name="MessageConstruct")
MessageConcept = Class(name="MessageConcept")
iso20022_MessageConstruct = Class(name="iso20022::MessageConstruct", is_abstract=True)
Construct = Class(name="Construct")
iso20022_LogicalType = Class(name="iso20022::LogicalType", is_abstract=True)
iso20022_BusinessElement = Class(name="iso20022::BusinessElement", is_abstract=True)
iso20022_MessageElementContainer = Class(name="iso20022::MessageElementContainer", is_abstract=True)
iso20022_MultiplicityEntity = Class(name="iso20022::MultiplicityEntity", is_abstract=True)
iso20022_MessageConcept = Class(name="iso20022::MessageConcept", is_abstract=True)
iso20022_Construct = Class(name="iso20022::Construct", is_abstract=True)
MultiplicityEntity = Class(name="MultiplicityEntity")
iso20022_MessageComponentType = Class(name="iso20022::MessageComponentType", is_abstract=True)
TopLevelDictionaryEntry = Class(name="TopLevelDictionaryEntry")
BusinessElementType = Class(name="BusinessElementType")
BusinessConcept = Class(name="BusinessConcept")
iso20022_BusinessElementType = Class(name="iso20022::BusinessElementType", is_abstract=True)
iso20022_BusinessConcept = Class(name="iso20022::BusinessConcept", is_abstract=True)
iso20022_BusinessAssociationEnd = Class(name="iso20022::BusinessAssociationEnd")
LogicalType = Class(name="LogicalType")
iso20022_DataType = Class(name="iso20022::DataType", is_abstract=True)
BusinessElement = Class(name="BusinessElement")
MessageComponentType = Class(name="MessageComponentType")
MessageElementContainer = Class(name="MessageElementContainer")
iso20022_BusinessTransaction = Class(name="iso20022::BusinessTransaction")
iso20022_MessageTransportMode = Class(name="iso20022::MessageTransportMode")
iso20022_BusinessProcess = Class(name="iso20022::BusinessProcess")
iso20022_Participant = Class(name="iso20022::Participant")
iso20022_BusinessRole = Class(name="iso20022::BusinessRole")
iso20022_Receive = Class(name="iso20022::Receive")
iso20022_Send = Class(name="iso20022::Send")
iso20022_Conversation = Class(name="iso20022::Conversation")
iso20022_MessageAssociationEnd = Class(name="iso20022::MessageAssociationEnd")
MessageElement = Class(name="MessageElement")
iso20022_BusinessAttribute = Class(name="iso20022::BusinessAttribute")
iso20022_MessageAttribute = Class(name="iso20022::MessageAttribute")
iso20022_Text = Class(name="iso20022::Text")
String = Class(name="String")
iso20022_String = Class(name="iso20022::String")
DataType = Class(name="DataType")
iso20022_Indicator = Class(name="iso20022::Indicator")
Boolean = Class(name="Boolean")
iso20022_Boolean = Class(name="iso20022::Boolean")
iso20022_IdentifierSet = Class(name="iso20022::IdentifierSet")
iso20022_Decimal = Class(name="iso20022::Decimal")
iso20022_Rate = Class(name="iso20022::Rate")
Decimal = Class(name="Decimal")
iso20022_Quantity = Class(name="iso20022::Quantity")
iso20022_ExternalSchema = Class(name="iso20022::ExternalSchema")
iso20022_Code = Class(name="iso20022::Code")
iso20022_CodeSet = Class(name="iso20022::CodeSet")
iso20022_ChoiceComponent = Class(name="iso20022::ChoiceComponent")
iso20022_Amount = Class(name="iso20022::Amount")
iso20022_EndPointCategory = Class(name="iso20022::EndPointCategory")
iso20022_AbstractDateTimeConcept = Class(name="iso20022::AbstractDateTimeConcept", is_abstract=True)
iso20022_Binary = Class(name="iso20022::Binary")
iso20022_Date = Class(name="iso20022::Date")
AbstractDateTimeConcept = Class(name="AbstractDateTimeConcept")
iso20022_Duration = Class(name="iso20022::Duration")
iso20022_Month = Class(name="iso20022::Month")
iso20022_MonthDay = Class(name="iso20022::MonthDay")
iso20022_Time = Class(name="iso20022::Time")
iso20022_DateTime = Class(name="iso20022::DateTime")
iso20022_Day = Class(name="iso20022::Day")
iso20022_UserDefined = Class(name="iso20022::UserDefined")
iso20022_Year = Class(name="iso20022::Year")
iso20022_YearMonth = Class(name="iso20022::YearMonth")
iso20022_SchemaType = Class(name="iso20022::SchemaType")
iso20022_IndustryMessageSet = Class(name="iso20022::IndustryMessageSet")
iso20022_ConvergenceDocumentation = Class(name="iso20022::ConvergenceDocumentation")
iso20022_ISO15022MessageSet = Class(name="iso20022::ISO15022MessageSet")
IndustryMessageSet = Class(name="IndustryMessageSet")

# iso20022_Address class attributes and methods

# ModelEntity class attributes and methods

# iso20022_ModelEntity class attributes and methods
iso20022_ModelEntity_objectIdentifier: Property = Property(name="objectIdentifier", type=StringType)
iso20022_ModelEntity.attributes={iso20022_ModelEntity_objectIdentifier}

# iso20022_BroadcastList class attributes and methods

# iso20022_MessagingEndpoint class attributes and methods

# iso20022_MessageTransportSystem class attributes and methods

# iso20022_TransportMessage class attributes and methods
iso20022_TransportMessage_m_sameMessageTransportSystem: Method = Method(name="sameMessageTransportSystem", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
iso20022_TransportMessage.methods={iso20022_TransportMessage_m_sameMessageTransportSystem}

# iso20022_MessageInstance class attributes and methods

# TopLevelCatalogueEntry class attributes and methods

# iso20022_MessageDefinition class attributes and methods
iso20022_MessageDefinition_xmlName: Property = Property(name="xmlName", type=StringType)
iso20022_MessageDefinition_xmlTag: Property = Property(name="xmlTag", type=StringType)
iso20022_MessageDefinition_rootElement: Property = Property(name="rootElement", type=StringType)
iso20022_MessageDefinition_m_BusinessAreaNameMatch: Method = Method(name="BusinessAreaNameMatch", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
iso20022_MessageDefinition.attributes={iso20022_MessageDefinition_xmlTag, iso20022_MessageDefinition_xmlName, iso20022_MessageDefinition_rootElement}
iso20022_MessageDefinition.methods={iso20022_MessageDefinition_m_BusinessAreaNameMatch}

# iso20022_TopLevelCatalogueEntry class attributes and methods

# RepositoryConcept class attributes and methods

# iso20022_BusinessProcessCatalogue class attributes and methods
iso20022_BusinessProcessCatalogue_m_EntriesHaveUniqueName: Method = Method(name="EntriesHaveUniqueName", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
iso20022_BusinessProcessCatalogue.methods={iso20022_BusinessProcessCatalogue_m_EntriesHaveUniqueName}

# iso20022_RepositoryConcept class attributes and methods
iso20022_RepositoryConcept_name: Property = Property(name="name", type=StringType)
iso20022_RepositoryConcept_definition: Property = Property(name="definition", type=StringType)
iso20022_RepositoryConcept_example: Property = Property(name="example", type=StringType)
iso20022_RepositoryConcept_registrationStatus: Property = Property(name="registrationStatus", type=StringType)
iso20022_RepositoryConcept_removalDate: Property = Property(name="removalDate", type=DateType)
iso20022_RepositoryConcept_m_RemovalDateRegistrationStatus: Method = Method(name="RemovalDateRegistrationStatus", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
iso20022_RepositoryConcept_m_NameFirstLetterUppercase: Method = Method(name="NameFirstLetterUppercase", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
iso20022_RepositoryConcept.attributes={iso20022_RepositoryConcept_registrationStatus, iso20022_RepositoryConcept_name, iso20022_RepositoryConcept_definition, iso20022_RepositoryConcept_removalDate, iso20022_RepositoryConcept_example}
iso20022_RepositoryConcept.methods={iso20022_RepositoryConcept_m_RemovalDateRegistrationStatus, iso20022_RepositoryConcept_m_NameFirstLetterUppercase}

# iso20022_SyntaxMessageScheme class attributes and methods

# iso20022_SemanticMarkup class attributes and methods
iso20022_SemanticMarkup_type: Property = Property(name="type", type=StringType)
iso20022_SemanticMarkup.attributes={iso20022_SemanticMarkup_type}

# iso20022_Doclet class attributes and methods
iso20022_Doclet_type: Property = Property(name="type", type=StringType)
iso20022_Doclet_content: Property = Property(name="content", type=StringType)
iso20022_Doclet.attributes={iso20022_Doclet_content, iso20022_Doclet_type}

# iso20022_SemanticMarkupElement class attributes and methods
iso20022_SemanticMarkupElement_name: Property = Property(name="name", type=StringType)
iso20022_SemanticMarkupElement_value: Property = Property(name="value", type=StringType)
iso20022_SemanticMarkupElement.attributes={iso20022_SemanticMarkupElement_name, iso20022_SemanticMarkupElement_value}

# iso20022_Constraint class attributes and methods
iso20022_Constraint_expression: Property = Property(name="expression", type=StringType)
iso20022_Constraint_expressionLanguage: Property = Property(name="expressionLanguage", type=StringType)
iso20022_Constraint.attributes={iso20022_Constraint_expressionLanguage, iso20022_Constraint_expression}

# iso20022_Repository class attributes and methods

# iso20022_TopLevelDictionaryEntry class attributes and methods

# iso20022_DataDictionary class attributes and methods
iso20022_DataDictionary_m_EntriesHaveUniqueName: Method = Method(name="EntriesHaveUniqueName", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
iso20022_DataDictionary.methods={iso20022_DataDictionary_m_EntriesHaveUniqueName}

# iso20022_MessageSet class attributes and methods
iso20022_MessageSet_m_GeneratedSyntaxDerivation: Method = Method(name="GeneratedSyntaxDerivation", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
iso20022_MessageSet.methods={iso20022_MessageSet_m_GeneratedSyntaxDerivation}

# iso20022_BusinessArea class attributes and methods
iso20022_BusinessArea_code: Property = Property(name="code", type=StringType)
iso20022_BusinessArea.attributes={iso20022_BusinessArea_code}

# RepositoryType class attributes and methods

# iso20022_MessageChoreography class attributes and methods

# iso20022_MessageTransmission class attributes and methods
iso20022_MessageTransmission_messageTypeDescription: Property = Property(name="messageTypeDescription", type=StringType)
iso20022_MessageTransmission.attributes={iso20022_MessageTransmission_messageTypeDescription}

# iso20022_MessageDefinitionIdentifier class attributes and methods
iso20022_MessageDefinitionIdentifier_version: Property = Property(name="version", type=StringType)
iso20022_MessageDefinitionIdentifier_businessArea: Property = Property(name="businessArea", type=StringType)
iso20022_MessageDefinitionIdentifier_messageFunctionality: Property = Property(name="messageFunctionality", type=StringType)
iso20022_MessageDefinitionIdentifier_flavour: Property = Property(name="flavour", type=StringType)
iso20022_MessageDefinitionIdentifier.attributes={iso20022_MessageDefinitionIdentifier_version, iso20022_MessageDefinitionIdentifier_messageFunctionality, iso20022_MessageDefinitionIdentifier_flavour, iso20022_MessageDefinitionIdentifier_businessArea}

# iso20022_Xor class attributes and methods

# iso20022_MessageBuildingBlock class attributes and methods
iso20022_MessageBuildingBlock_m_MessageBuildingBlockHasExactlyOneType: Method = Method(name="MessageBuildingBlockHasExactlyOneType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
iso20022_MessageBuildingBlock.methods={iso20022_MessageBuildingBlock_m_MessageBuildingBlockHasExactlyOneType}

# iso20022_Syntax class attributes and methods
iso20022_Syntax_m_GeneratedForDerivation: Method = Method(name="GeneratedForDerivation", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
iso20022_Syntax.methods={iso20022_Syntax_m_GeneratedForDerivation}

# iso20022_Encoding class attributes and methods

# iso20022_RepositoryType class attributes and methods

# iso20022_MessageElement class attributes and methods
iso20022_MessageElement_isTechnical: Property = Property(name="isTechnical", type=BooleanType)
iso20022_MessageElement_isDerived: Property = Property(name="isDerived", type=BooleanType)
iso20022_MessageElement_m_NoMoreThanOneTrace: Method = Method(name="NoMoreThanOneTrace", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
iso20022_MessageElement_m_CardinalityAlignment: Method = Method(name="CardinalityAlignment", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
iso20022_MessageElement.attributes={iso20022_MessageElement_isDerived, iso20022_MessageElement_isTechnical}
iso20022_MessageElement.methods={iso20022_MessageElement_m_CardinalityAlignment, iso20022_MessageElement_m_NoMoreThanOneTrace}

# iso20022_MessageComponent class attributes and methods

# iso20022_BusinessComponent class attributes and methods
iso20022_BusinessComponent_m_BusinessElementsHaveUniqueNames: Method = Method(name="BusinessElementsHaveUniqueNames", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
iso20022_BusinessComponent.methods={iso20022_BusinessComponent_m_BusinessElementsHaveUniqueNames}

# MessageConstruct class attributes and methods

# MessageConcept class attributes and methods

# iso20022_MessageConstruct class attributes and methods
iso20022_MessageConstruct_xmlTag: Property = Property(name="xmlTag", type=StringType)
iso20022_MessageConstruct.attributes={iso20022_MessageConstruct_xmlTag}

# Construct class attributes and methods

# iso20022_LogicalType class attributes and methods

# iso20022_BusinessElement class attributes and methods
iso20022_BusinessElement_isDerived: Property = Property(name="isDerived", type=BooleanType)
iso20022_BusinessElement.attributes={iso20022_BusinessElement_isDerived}

# iso20022_MessageElementContainer class attributes and methods
iso20022_MessageElementContainer_m_technicalElement: Method = Method(name="technicalElement", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
iso20022_MessageElementContainer_m_MessageElementsHaveUniqueNames: Method = Method(name="MessageElementsHaveUniqueNames", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
iso20022_MessageElementContainer.methods={iso20022_MessageElementContainer_m_technicalElement, iso20022_MessageElementContainer_m_MessageElementsHaveUniqueNames}

# iso20022_MultiplicityEntity class attributes and methods
iso20022_MultiplicityEntity_maxOccurs: Property = Property(name="maxOccurs", type=StringType)
iso20022_MultiplicityEntity_minOccurs: Property = Property(name="minOccurs", type=StringType)
iso20022_MultiplicityEntity.attributes={iso20022_MultiplicityEntity_maxOccurs, iso20022_MultiplicityEntity_minOccurs}

# iso20022_MessageConcept class attributes and methods

# iso20022_Construct class attributes and methods

# MultiplicityEntity class attributes and methods

# iso20022_MessageComponentType class attributes and methods
iso20022_MessageComponentType_isTechnical: Property = Property(name="isTechnical", type=BooleanType)
iso20022_MessageComponentType.attributes={iso20022_MessageComponentType_isTechnical}

# TopLevelDictionaryEntry class attributes and methods

# BusinessElementType class attributes and methods

# BusinessConcept class attributes and methods

# iso20022_BusinessElementType class attributes and methods

# iso20022_BusinessConcept class attributes and methods

# iso20022_BusinessAssociationEnd class attributes and methods
iso20022_BusinessAssociationEnd_aggregation: Property = Property(name="aggregation", type=StringType)
iso20022_BusinessAssociationEnd_m_AtMostOneAggregatedEnd: Method = Method(name="AtMostOneAggregatedEnd", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
iso20022_BusinessAssociationEnd_m_ContextConsistentWithType: Method = Method(name="ContextConsistentWithType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
iso20022_BusinessAssociationEnd.attributes={iso20022_BusinessAssociationEnd_aggregation}
iso20022_BusinessAssociationEnd.methods={iso20022_BusinessAssociationEnd_m_ContextConsistentWithType, iso20022_BusinessAssociationEnd_m_AtMostOneAggregatedEnd}

# LogicalType class attributes and methods

# iso20022_DataType class attributes and methods

# BusinessElement class attributes and methods

# MessageComponentType class attributes and methods

# MessageElementContainer class attributes and methods

# iso20022_BusinessTransaction class attributes and methods
iso20022_BusinessTransaction_m_MessageTransmissionsHaveUniqueNames: Method = Method(name="MessageTransmissionsHaveUniqueNames", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
iso20022_BusinessTransaction_m_ParticipantsHaveUniqueNames: Method = Method(name="ParticipantsHaveUniqueNames", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
iso20022_BusinessTransaction.methods={iso20022_BusinessTransaction_m_MessageTransmissionsHaveUniqueNames, iso20022_BusinessTransaction_m_ParticipantsHaveUniqueNames}

# iso20022_MessageTransportMode class attributes and methods
iso20022_MessageTransportMode_maximumMessageSize: Property = Property(name="maximumMessageSize", type=StringType)
iso20022_MessageTransportMode_messageDeliveryWindow: Property = Property(name="messageDeliveryWindow", type=StringType)
iso20022_MessageTransportMode_messageSendingWindow: Property = Property(name="messageSendingWindow", type=StringType)
iso20022_MessageTransportMode_deliveryAssurance: Property = Property(name="deliveryAssurance", type=StringType)
iso20022_MessageTransportMode_durability: Property = Property(name="durability", type=StringType)
iso20022_MessageTransportMode_messageCasting: Property = Property(name="messageCasting", type=StringType)
iso20022_MessageTransportMode_boundedCommunicationDelay: Property = Property(name="boundedCommunicationDelay", type=StringType)
iso20022_MessageTransportMode_maximumClockVariation: Property = Property(name="maximumClockVariation", type=StringType)
iso20022_MessageTransportMode_messageValidationResults: Property = Property(name="messageValidationResults", type=StringType)
iso20022_MessageTransportMode_receiverAsynchronicity: Property = Property(name="receiverAsynchronicity", type=StringType)
iso20022_MessageTransportMode_senderAsynchronicity: Property = Property(name="senderAsynchronicity", type=StringType)
iso20022_MessageTransportMode_messageDeliveryOrder: Property = Property(name="messageDeliveryOrder", type=StringType)
iso20022_MessageTransportMode_messageValidationLevel: Property = Property(name="messageValidationLevel", type=StringType)
iso20022_MessageTransportMode_messageValidationOnOff: Property = Property(name="messageValidationOnOff", type=StringType)
iso20022_MessageTransportMode.attributes={iso20022_MessageTransportMode_messageValidationResults, iso20022_MessageTransportMode_senderAsynchronicity, iso20022_MessageTransportMode_maximumClockVariation, iso20022_MessageTransportMode_messageCasting, iso20022_MessageTransportMode_maximumMessageSize, iso20022_MessageTransportMode_durability, iso20022_MessageTransportMode_messageDeliveryOrder, iso20022_MessageTransportMode_boundedCommunicationDelay, iso20022_MessageTransportMode_messageValidationLevel, iso20022_MessageTransportMode_deliveryAssurance, iso20022_MessageTransportMode_messageValidationOnOff, iso20022_MessageTransportMode_messageDeliveryWindow, iso20022_MessageTransportMode_messageSendingWindow, iso20022_MessageTransportMode_receiverAsynchronicity}

# iso20022_BusinessProcess class attributes and methods

# iso20022_Participant class attributes and methods

# iso20022_BusinessRole class attributes and methods

# iso20022_Receive class attributes and methods

# iso20022_Send class attributes and methods

# iso20022_Conversation class attributes and methods

# iso20022_MessageAssociationEnd class attributes and methods
iso20022_MessageAssociationEnd_isComposite: Property = Property(name="isComposite", type=BooleanType)
iso20022_MessageAssociationEnd.attributes={iso20022_MessageAssociationEnd_isComposite}

# MessageElement class attributes and methods

# iso20022_BusinessAttribute class attributes and methods
iso20022_BusinessAttribute_m_BusinessAttributeHasExactlyOneType: Method = Method(name="BusinessAttributeHasExactlyOneType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
iso20022_BusinessAttribute_m_NoDerivingCodeSetType: Method = Method(name="NoDerivingCodeSetType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
iso20022_BusinessAttribute.methods={iso20022_BusinessAttribute_m_BusinessAttributeHasExactlyOneType, iso20022_BusinessAttribute_m_NoDerivingCodeSetType}

# iso20022_MessageAttribute class attributes and methods
iso20022_MessageAttribute_m_MessageAttributeHasExactlyOneType: Method = Method(name="MessageAttributeHasExactlyOneType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
iso20022_MessageAttribute.methods={iso20022_MessageAttribute_m_MessageAttributeHasExactlyOneType}

# iso20022_Text class attributes and methods

# String class attributes and methods

# iso20022_String class attributes and methods
iso20022_String_minLength: Property = Property(name="minLength", type=StringType)
iso20022_String_maxLength: Property = Property(name="maxLength", type=StringType)
iso20022_String_length: Property = Property(name="length", type=StringType)
iso20022_String_pattern: Property = Property(name="pattern", type=StringType)
iso20022_String.attributes={iso20022_String_pattern, iso20022_String_minLength, iso20022_String_length, iso20022_String_maxLength}

# DataType class attributes and methods

# iso20022_Indicator class attributes and methods
iso20022_Indicator_meaningWhenTrue: Property = Property(name="meaningWhenTrue", type=StringType)
iso20022_Indicator_meaningWhenFalse: Property = Property(name="meaningWhenFalse", type=StringType)
iso20022_Indicator.attributes={iso20022_Indicator_meaningWhenTrue, iso20022_Indicator_meaningWhenFalse}

# Boolean class attributes and methods

# iso20022_Boolean class attributes and methods
iso20022_Boolean_pattern: Property = Property(name="pattern", type=StringType)
iso20022_Boolean.attributes={iso20022_Boolean_pattern}

# iso20022_IdentifierSet class attributes and methods
iso20022_IdentifierSet_identificationScheme: Property = Property(name="identificationScheme", type=StringType)
iso20022_IdentifierSet.attributes={iso20022_IdentifierSet_identificationScheme}

# iso20022_Decimal class attributes and methods
iso20022_Decimal_minInclusive: Property = Property(name="minInclusive", type=StringType)
iso20022_Decimal_minExclusive: Property = Property(name="minExclusive", type=StringType)
iso20022_Decimal_maxInclusive: Property = Property(name="maxInclusive", type=StringType)
iso20022_Decimal_maxExclusive: Property = Property(name="maxExclusive", type=StringType)
iso20022_Decimal_totalDigits: Property = Property(name="totalDigits", type=StringType)
iso20022_Decimal_fractionDigits: Property = Property(name="fractionDigits", type=StringType)
iso20022_Decimal_pattern: Property = Property(name="pattern", type=StringType)
iso20022_Decimal.attributes={iso20022_Decimal_minInclusive, iso20022_Decimal_fractionDigits, iso20022_Decimal_totalDigits, iso20022_Decimal_maxExclusive, iso20022_Decimal_pattern, iso20022_Decimal_minExclusive, iso20022_Decimal_maxInclusive}

# iso20022_Rate class attributes and methods
iso20022_Rate_baseValue: Property = Property(name="baseValue", type=StringType)
iso20022_Rate_baseUnitCode: Property = Property(name="baseUnitCode", type=StringType)
iso20022_Rate.attributes={iso20022_Rate_baseValue, iso20022_Rate_baseUnitCode}

# Decimal class attributes and methods

# iso20022_Quantity class attributes and methods
iso20022_Quantity_unitCode: Property = Property(name="unitCode", type=StringType)
iso20022_Quantity.attributes={iso20022_Quantity_unitCode}

# iso20022_ExternalSchema class attributes and methods
iso20022_ExternalSchema_processContent: Property = Property(name="processContent", type=StringType)
iso20022_ExternalSchema_namespaceList: Property = Property(name="namespaceList", type=StringType)
iso20022_ExternalSchema.attributes={iso20022_ExternalSchema_namespaceList, iso20022_ExternalSchema_processContent}

# iso20022_Code class attributes and methods
iso20022_Code_codeName: Property = Property(name="codeName", type=StringType)
iso20022_Code.attributes={iso20022_Code_codeName}

# iso20022_CodeSet class attributes and methods
iso20022_CodeSet_identificationScheme: Property = Property(name="identificationScheme", type=StringType)
iso20022_CodeSet.attributes={iso20022_CodeSet_identificationScheme}

# iso20022_ChoiceComponent class attributes and methods
iso20022_ChoiceComponent_m_AtLeastOneProperty: Method = Method(name="AtLeastOneProperty", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
iso20022_ChoiceComponent.methods={iso20022_ChoiceComponent_m_AtLeastOneProperty}

# iso20022_Amount class attributes and methods

# iso20022_EndPointCategory class attributes and methods

# iso20022_AbstractDateTimeConcept class attributes and methods
iso20022_AbstractDateTimeConcept_minExclusive: Property = Property(name="minExclusive", type=StringType)
iso20022_AbstractDateTimeConcept_maxInclusive: Property = Property(name="maxInclusive", type=StringType)
iso20022_AbstractDateTimeConcept_maxExclusive: Property = Property(name="maxExclusive", type=StringType)
iso20022_AbstractDateTimeConcept_pattern: Property = Property(name="pattern", type=StringType)
iso20022_AbstractDateTimeConcept_minInclusive: Property = Property(name="minInclusive", type=StringType)
iso20022_AbstractDateTimeConcept.attributes={iso20022_AbstractDateTimeConcept_minInclusive, iso20022_AbstractDateTimeConcept_maxInclusive, iso20022_AbstractDateTimeConcept_maxExclusive, iso20022_AbstractDateTimeConcept_pattern, iso20022_AbstractDateTimeConcept_minExclusive}

# iso20022_Binary class attributes and methods
iso20022_Binary_minLength: Property = Property(name="minLength", type=StringType)
iso20022_Binary_maxLength: Property = Property(name="maxLength", type=StringType)
iso20022_Binary_length: Property = Property(name="length", type=StringType)
iso20022_Binary_pattern: Property = Property(name="pattern", type=StringType)
iso20022_Binary.attributes={iso20022_Binary_length, iso20022_Binary_minLength, iso20022_Binary_pattern, iso20022_Binary_maxLength}

# iso20022_Date class attributes and methods

# AbstractDateTimeConcept class attributes and methods

# iso20022_Duration class attributes and methods

# iso20022_Month class attributes and methods

# iso20022_MonthDay class attributes and methods

# iso20022_Time class attributes and methods

# iso20022_DateTime class attributes and methods

# iso20022_Day class attributes and methods

# iso20022_UserDefined class attributes and methods
iso20022_UserDefined_namespace: Property = Property(name="namespace", type=StringType)
iso20022_UserDefined_namespaceList: Property = Property(name="namespaceList", type=StringType)
iso20022_UserDefined_processContents: Property = Property(name="processContents", type=StringType)
iso20022_UserDefined.attributes={iso20022_UserDefined_processContents, iso20022_UserDefined_namespaceList, iso20022_UserDefined_namespace}

# iso20022_Year class attributes and methods

# iso20022_YearMonth class attributes and methods

# iso20022_SchemaType class attributes and methods
iso20022_SchemaType_kind: Property = Property(name="kind", type=StringType)
iso20022_SchemaType.attributes={iso20022_SchemaType_kind}

# iso20022_IndustryMessageSet class attributes and methods

# iso20022_ConvergenceDocumentation class attributes and methods

# iso20022_ISO15022MessageSet class attributes and methods

# IndustryMessageSet class attributes and methods

# Relationships
nextVersions3: BinaryAssociation = BinaryAssociation(
    name="nextVersions3",
    ends={
        Property(name="ModelEntity", type=iso20022_ModelEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="previousVersion", type=iso20022_ModelEntity, multiplicity=Multiplicity(0, 9999))
    }
)
previousVersion5: BinaryAssociation = BinaryAssociation(
    name="previousVersion5",
    ends={
        Property(name="ModelEntity6", type=iso20022_ModelEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="nextVersions", type=iso20022_ModelEntity, multiplicity=Multiplicity(0, 1))
    }
)
broadCastList0: BinaryAssociation = BinaryAssociation(
    name="broadCastList0",
    ends={
        Property(name="BroadcastList", type=iso20022_Address, multiplicity=Multiplicity(1, 1)),
        Property(name="address", type=iso20022_BroadcastList, multiplicity=Multiplicity(0, 9999))
    }
)
endpoint1: BinaryAssociation = BinaryAssociation(
    name="endpoint1",
    ends={
        Property(name="MessagingEndpoint", type=iso20022_Address, multiplicity=Multiplicity(1, 1)),
        Property(name="location", type=iso20022_MessagingEndpoint, multiplicity=Multiplicity(1, 1))
    }
)
transportSystem8: BinaryAssociation = BinaryAssociation(
    name="transportSystem8",
    ends={
        Property(name="MessageTransportSystem", type=iso20022_MessagingEndpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="endpoint", type=iso20022_MessageTransportSystem, multiplicity=Multiplicity(1, 1))
    }
)
receivedMessage9: BinaryAssociation = BinaryAssociation(
    name="receivedMessage9",
    ends={
        Property(name="TransportMessage", type=iso20022_MessagingEndpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="receiver", type=iso20022_TransportMessage, multiplicity=Multiplicity(0, 9999))
    }
)
sentMessage10: BinaryAssociation = BinaryAssociation(
    name="sentMessage10",
    ends={
        Property(name="TransportMessage11", type=iso20022_MessagingEndpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="sender", type=iso20022_TransportMessage, multiplicity=Multiplicity(0, 9999))
    }
)
location12: BinaryAssociation = BinaryAssociation(
    name="location12",
    ends={
        Property(name="Address14", type=iso20022_MessagingEndpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="endpoint13", type=iso20022_Address, multiplicity=Multiplicity(0, 9999))
    }
)
address7: BinaryAssociation = BinaryAssociation(
    name="address7",
    ends={
        Property(name="Address", type=iso20022_BroadcastList, multiplicity=Multiplicity(1, 1)),
        Property(name="broadCastList", type=iso20022_Address, multiplicity=Multiplicity(0, 9999))
    }
)
sender17: BinaryAssociation = BinaryAssociation(
    name="sender17",
    ends={
        Property(name="MessagingEndpoint18", type=iso20022_TransportMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="sentMessage", type=iso20022_MessagingEndpoint, multiplicity=Multiplicity(1, 1))
    }
)
messageInstance19: BinaryAssociation = BinaryAssociation(
    name="messageInstance19",
    ends={
        Property(name="MessageInstance", type=iso20022_TransportMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="transportMessage", type=iso20022_MessageInstance, multiplicity=Multiplicity(1, 1))
    }
)
receiver20: BinaryAssociation = BinaryAssociation(
    name="receiver20",
    ends={
        Property(name="MessagingEndpoint21", type=iso20022_TransportMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="receivedMessage", type=iso20022_MessagingEndpoint, multiplicity=Multiplicity(0, 9999))
    }
)
endpoint15: BinaryAssociation = BinaryAssociation(
    name="endpoint15",
    ends={
        Property(name="MessagingEndpoint16", type=iso20022_MessageTransportSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="transportSystem", type=iso20022_MessagingEndpoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageDefinitionTrace25: BinaryAssociation = BinaryAssociation(
    name="messageDefinitionTrace25",
    ends={
        Property(name="MessageDefinition", type=iso20022_SyntaxMessageScheme, multiplicity=Multiplicity(1, 1)),
        Property(name="derivation", type=iso20022_MessageDefinition, multiplicity=Multiplicity(0, 1))
    }
)
businessProcessCatalogue26: BinaryAssociation = BinaryAssociation(
    name="businessProcessCatalogue26",
    ends={
        Property(name="BusinessProcessCatalogue", type=iso20022_TopLevelCatalogueEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="topLevelCatalogueEntry", type=iso20022_BusinessProcessCatalogue, multiplicity=Multiplicity(1, 1))
    }
)
specification22: BinaryAssociation = BinaryAssociation(
    name="specification22",
    ends={
        Property(name="iso20022_SyntaxMessageScheme", type=iso20022_MessageInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="iso20022_MessageInstance", type=iso20022_SyntaxMessageScheme, multiplicity=Multiplicity(1, 1))
    }
)
transportMessage23: BinaryAssociation = BinaryAssociation(
    name="transportMessage23",
    ends={
        Property(name="TransportMessage24", type=iso20022_MessageInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="messageInstance", type=iso20022_TransportMessage, multiplicity=Multiplicity(1, 9999))
    }
)
semanticMarkup27: BinaryAssociation = BinaryAssociation(
    name="semanticMarkup27",
    ends={
        Property(name="iso20022_SemanticMarkup", type=iso20022_RepositoryConcept, multiplicity=Multiplicity(1, 1)),
        Property(name="iso20022_RepositoryConcept", type=iso20022_SemanticMarkup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
doclet28: BinaryAssociation = BinaryAssociation(
    name="doclet28",
    ends={
        Property(name="iso20022_Doclet", type=iso20022_RepositoryConcept, multiplicity=Multiplicity(1, 1)),
        Property(name="iso20022_RepositoryConcept29", type=iso20022_Doclet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements31: BinaryAssociation = BinaryAssociation(
    name="elements31",
    ends={
        Property(name="iso20022_SemanticMarkupElement", type=iso20022_SemanticMarkup, multiplicity=Multiplicity(1, 1)),
        Property(name="iso20022_SemanticMarkup32", type=iso20022_SemanticMarkupElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraint30: BinaryAssociation = BinaryAssociation(
    name="constraint30",
    ends={
        Property(name="Constraint", type=iso20022_RepositoryConcept, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=iso20022_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository34: BinaryAssociation = BinaryAssociation(
    name="repository34",
    ends={
        Property(name="Repository", type=iso20022_BusinessProcessCatalogue, multiplicity=Multiplicity(1, 1)),
        Property(name="businessProcessCatalogue", type=iso20022_Repository, multiplicity=Multiplicity(1, 1))
    }
)
topLevelCatalogueEntry35: BinaryAssociation = BinaryAssociation(
    name="topLevelCatalogueEntry35",
    ends={
        Property(name="TopLevelCatalogueEntry", type=iso20022_BusinessProcessCatalogue, multiplicity=Multiplicity(1, 1)),
        Property(name="businessProcessCatalogue36", type=iso20022_TopLevelCatalogueEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner33: BinaryAssociation = BinaryAssociation(
    name="owner33",
    ends={
        Property(name="RepositoryConcept", type=iso20022_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="constraint", type=iso20022_RepositoryConcept, multiplicity=Multiplicity(1, 1))
    }
)
topLevelDictionaryEntry41: BinaryAssociation = BinaryAssociation(
    name="topLevelDictionaryEntry41",
    ends={
        Property(name="TopLevelDictionaryEntry", type=iso20022_DataDictionary, multiplicity=Multiplicity(1, 1)),
        Property(name="dataDictionary", type=iso20022_TopLevelDictionaryEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository42: BinaryAssociation = BinaryAssociation(
    name="repository42",
    ends={
        Property(name="Repository44", type=iso20022_DataDictionary, multiplicity=Multiplicity(1, 1)),
        Property(name="dataDictionary43", type=iso20022_Repository, multiplicity=Multiplicity(1, 1))
    }
)
dataDictionary37: BinaryAssociation = BinaryAssociation(
    name="dataDictionary37",
    ends={
        Property(name="DataDictionary", type=iso20022_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository", type=iso20022_DataDictionary, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
businessProcessCatalogue38: BinaryAssociation = BinaryAssociation(
    name="businessProcessCatalogue38",
    ends={
        Property(name="BusinessProcessCatalogue40", type=iso20022_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository39", type=iso20022_BusinessProcessCatalogue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
messageSet47: BinaryAssociation = BinaryAssociation(
    name="messageSet47",
    ends={
        Property(name="MessageSet", type=iso20022_MessageDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="messageDefinition", type=iso20022_MessageSet, multiplicity=Multiplicity(0, 9999))
    }
)
businessArea48: BinaryAssociation = BinaryAssociation(
    name="businessArea48",
    ends={
        Property(name="BusinessArea", type=iso20022_MessageDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="messageDefinition49", type=iso20022_BusinessArea, multiplicity=Multiplicity(1, 1))
    }
)
dataDictionary45: BinaryAssociation = BinaryAssociation(
    name="dataDictionary45",
    ends={
        Property(name="DataDictionary46", type=iso20022_TopLevelDictionaryEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="topLevelDictionaryEntry", type=iso20022_DataDictionary, multiplicity=Multiplicity(1, 1))
    }
)
messageBuildingBlock52: BinaryAssociation = BinaryAssociation(
    name="messageBuildingBlock52",
    ends={
        Property(name="iso20022_MessageBuildingBlock", type=iso20022_MessageDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="iso20022_MessageDefinition", type=iso20022_MessageBuildingBlock, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
choreography53: BinaryAssociation = BinaryAssociation(
    name="choreography53",
    ends={
        Property(name="MessageChoreography", type=iso20022_MessageDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="messageDefinition54", type=iso20022_MessageChoreography, multiplicity=Multiplicity(0, 9999))
    }
)
trace55: BinaryAssociation = BinaryAssociation(
    name="trace55",
    ends={
        Property(name="MessageTransmission", type=iso20022_MessageDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="derivation56", type=iso20022_MessageTransmission, multiplicity=Multiplicity(0, 9999))
    }
)
messageDefinitionIdentifier57: BinaryAssociation = BinaryAssociation(
    name="messageDefinitionIdentifier57",
    ends={
        Property(name="iso20022_MessageDefinitionIdentifier", type=iso20022_MessageDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="iso20022_MessageDefinition58", type=iso20022_MessageDefinitionIdentifier, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
xors50: BinaryAssociation = BinaryAssociation(
    name="xors50",
    ends={
        Property(name="Xor", type=iso20022_MessageDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="messageDefinition51", type=iso20022_Xor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generatedSyntax60: BinaryAssociation = BinaryAssociation(
    name="generatedSyntax60",
    ends={
        Property(name="Syntax", type=iso20022_MessageSet, multiplicity=Multiplicity(1, 1)),
        Property(name="generatedFor", type=iso20022_Syntax, multiplicity=Multiplicity(0, 9999))
    }
)
validEncoding61: BinaryAssociation = BinaryAssociation(
    name="validEncoding61",
    ends={
        Property(name="Encoding", type=iso20022_MessageSet, multiplicity=Multiplicity(1, 1)),
        Property(name="messageSet", type=iso20022_Encoding, multiplicity=Multiplicity(0, 9999))
    }
)
derivation59: BinaryAssociation = BinaryAssociation(
    name="derivation59",
    ends={
        Property(name="SyntaxMessageScheme", type=iso20022_MessageDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="messageDefinitionTrace", type=iso20022_SyntaxMessageScheme, multiplicity=Multiplicity(0, 9999))
    }
)
possibleEncodings65: BinaryAssociation = BinaryAssociation(
    name="possibleEncodings65",
    ends={
        Property(name="Encoding66", type=iso20022_Syntax, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax", type=iso20022_Encoding, multiplicity=Multiplicity(1, 9999))
    }
)
generatedFor67: BinaryAssociation = BinaryAssociation(
    name="generatedFor67",
    ends={
        Property(name="MessageSet68", type=iso20022_Syntax, multiplicity=Multiplicity(1, 1)),
        Property(name="generatedSyntax", type=iso20022_MessageSet, multiplicity=Multiplicity(0, 9999))
    }
)
messageSet69: BinaryAssociation = BinaryAssociation(
    name="messageSet69",
    ends={
        Property(name="MessageSet70", type=iso20022_Encoding, multiplicity=Multiplicity(1, 1)),
        Property(name="validEncoding", type=iso20022_MessageSet, multiplicity=Multiplicity(0, 9999))
    }
)
syntax71: BinaryAssociation = BinaryAssociation(
    name="syntax71",
    ends={
        Property(name="Syntax72", type=iso20022_Encoding, multiplicity=Multiplicity(1, 1)),
        Property(name="possibleEncodings", type=iso20022_Syntax, multiplicity=Multiplicity(1, 1))
    }
)
messageDefinition62: BinaryAssociation = BinaryAssociation(
    name="messageDefinition62",
    ends={
        Property(name="MessageDefinition64", type=iso20022_MessageSet, multiplicity=Multiplicity(1, 1)),
        Property(name="messageSet63", type=iso20022_MessageDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
messageDefinition73: BinaryAssociation = BinaryAssociation(
    name="messageDefinition73",
    ends={
        Property(name="businessArea", type=iso20022_MessageDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="MessageDefinition74", type=iso20022_BusinessArea, multiplicity=Multiplicity(1, 1))
    }
)
impactedElements75: BinaryAssociation = BinaryAssociation(
    name="impactedElements75",
    ends={
        Property(name="iso20022_MessageElement", type=iso20022_Xor, multiplicity=Multiplicity(1, 1)),
        Property(name="iso20022_Xor", type=iso20022_MessageElement, multiplicity=Multiplicity(0, 9999))
    }
)
messageComponent76: BinaryAssociation = BinaryAssociation(
    name="messageComponent76",
    ends={
        Property(name="MessageComponent", type=iso20022_Xor, multiplicity=Multiplicity(1, 1)),
        Property(name="xors", type=iso20022_MessageComponent, multiplicity=Multiplicity(0, 1))
    }
)
impactedMessageBuildingBlocks77: BinaryAssociation = BinaryAssociation(
    name="impactedMessageBuildingBlocks77",
    ends={
        Property(name="iso20022_MessageBuildingBlock79", type=iso20022_Xor, multiplicity=Multiplicity(1, 1)),
        Property(name="iso20022_Xor78", type=iso20022_MessageBuildingBlock, multiplicity=Multiplicity(0, 9999))
    }
)
businessComponentTrace83: BinaryAssociation = BinaryAssociation(
    name="businessComponentTrace83",
    ends={
        Property(name="BusinessComponent", type=iso20022_MessageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="derivationElement", type=iso20022_BusinessComponent, multiplicity=Multiplicity(0, 1))
    }
)
messageDefinition80: BinaryAssociation = BinaryAssociation(
    name="messageDefinition80",
    ends={
        Property(name="MessageDefinition82", type=iso20022_Xor, multiplicity=Multiplicity(1, 1)),
        Property(name="xors81", type=iso20022_MessageDefinition, multiplicity=Multiplicity(0, 1))
    }
)
componentContext86: BinaryAssociation = BinaryAssociation(
    name="componentContext86",
    ends={
        Property(name="MessageElementContainer", type=iso20022_MessageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="messageElement", type=iso20022_MessageElementContainer, multiplicity=Multiplicity(1, 1))
    }
)
xmlMemberType87: BinaryAssociation = BinaryAssociation(
    name="xmlMemberType87",
    ends={
        Property(name="iso20022_LogicalType", type=iso20022_MessageConstruct, multiplicity=Multiplicity(1, 1)),
        Property(name="iso20022_MessageConstruct", type=iso20022_LogicalType, multiplicity=Multiplicity(1, 1))
    }
)
businessElementTrace84: BinaryAssociation = BinaryAssociation(
    name="businessElementTrace84",
    ends={
        Property(name="BusinessElement", type=iso20022_MessageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="derivation85", type=iso20022_BusinessElement, multiplicity=Multiplicity(0, 1))
    }
)
memberType88: BinaryAssociation = BinaryAssociation(
    name="memberType88",
    ends={
        Property(name="iso20022_RepositoryType", type=iso20022_Construct, multiplicity=Multiplicity(1, 1)),
        Property(name="iso20022_Construct", type=iso20022_RepositoryType, multiplicity=Multiplicity(1, 1))
    }
)
subType90: BinaryAssociation = BinaryAssociation(
    name="subType90",
    ends={
        Property(name="BusinessComponent91", type=iso20022_BusinessComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="superType", type=iso20022_BusinessComponent, multiplicity=Multiplicity(0, 9999))
    }
)
superType93: BinaryAssociation = BinaryAssociation(
    name="superType93",
    ends={
        Property(name="BusinessComponent94", type=iso20022_BusinessComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="subType", type=iso20022_BusinessComponent, multiplicity=Multiplicity(0, 1))
    }
)
element95: BinaryAssociation = BinaryAssociation(
    name="element95",
    ends={
        Property(name="BusinessElement96", type=iso20022_BusinessComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="elementContext", type=iso20022_BusinessElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
derivationComponent97: BinaryAssociation = BinaryAssociation(
    name="derivationComponent97",
    ends={
        Property(name="MessageComponentType", type=iso20022_BusinessComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="trace", type=iso20022_MessageComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
derivation100: BinaryAssociation = BinaryAssociation(
    name="derivation100",
    ends={
        Property(name="MessageElement101", type=iso20022_BusinessElement, multiplicity=Multiplicity(1, 1)),
        Property(name="businessElementTrace", type=iso20022_MessageElement, multiplicity=Multiplicity(0, 9999))
    }
)
associationDomain98: BinaryAssociation = BinaryAssociation(
    name="associationDomain98",
    ends={
        Property(name="BusinessAssociationEnd", type=iso20022_BusinessComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=iso20022_BusinessAssociationEnd, multiplicity=Multiplicity(0, 9999))
    }
)
derivationElement99: BinaryAssociation = BinaryAssociation(
    name="derivationElement99",
    ends={
        Property(name="MessageElement", type=iso20022_BusinessComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="businessComponentTrace", type=iso20022_MessageElement, multiplicity=Multiplicity(0, 9999))
    }
)
elementContext103: BinaryAssociation = BinaryAssociation(
    name="elementContext103",
    ends={
        Property(name="BusinessComponent104", type=iso20022_BusinessElement, multiplicity=Multiplicity(1, 1)),
        Property(name="element", type=iso20022_BusinessComponent, multiplicity=Multiplicity(1, 1))
    }
)
messageBuildingBlock105: BinaryAssociation = BinaryAssociation(
    name="messageBuildingBlock105",
    ends={
        Property(name="MessageBuildingBlock", type=iso20022_MessageComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="complexType", type=iso20022_MessageBuildingBlock, multiplicity=Multiplicity(0, 9999))
    }
)
trace106: BinaryAssociation = BinaryAssociation(
    name="trace106",
    ends={
        Property(name="BusinessComponent107", type=iso20022_MessageComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="derivationComponent", type=iso20022_BusinessComponent, multiplicity=Multiplicity(0, 1))
    }
)
businessElementType102: BinaryAssociation = BinaryAssociation(
    name="businessElementType102",
    ends={
        Property(name="iso20022_BusinessElementType", type=iso20022_BusinessElement, multiplicity=Multiplicity(1, 1)),
        Property(name="iso20022_BusinessElement", type=iso20022_BusinessElementType, multiplicity=Multiplicity(1, 1))
    }
)
simpleType108: BinaryAssociation = BinaryAssociation(
    name="simpleType108",
    ends={
        Property(name="iso20022_DataType", type=iso20022_MessageBuildingBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="iso20022_MessageBuildingBlock109", type=iso20022_DataType, multiplicity=Multiplicity(0, 1))
    }
)
complexType110: BinaryAssociation = BinaryAssociation(
    name="complexType110",
    ends={
        Property(name="MessageComponentType111", type=iso20022_MessageBuildingBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="messageBuildingBlock", type=iso20022_MessageComponentType, multiplicity=Multiplicity(0, 1))
    }
)
type114: BinaryAssociation = BinaryAssociation(
    name="type114",
    ends={
        Property(name="BusinessComponent115", type=iso20022_BusinessAssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="associationDomain", type=iso20022_BusinessComponent, multiplicity=Multiplicity(1, 1))
    }
)
opposite113: BinaryAssociation = BinaryAssociation(
    name="opposite113",
    ends={
        Property(name="iso20022_BusinessAssociationEnd", type=iso20022_BusinessAssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="iso20022_BusinessAssociationEnd112", type=iso20022_BusinessAssociationEnd, multiplicity=Multiplicity(0, 1))
    }
)
messageElement116: BinaryAssociation = BinaryAssociation(
    name="messageElement116",
    ends={
        Property(name="MessageElement117", type=iso20022_MessageElementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="componentContext", type=iso20022_MessageElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xors118: BinaryAssociation = BinaryAssociation(
    name="xors118",
    ends={
        Property(name="Xor119", type=iso20022_MessageComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="messageComponent", type=iso20022_Xor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageDefinition122: BinaryAssociation = BinaryAssociation(
    name="messageDefinition122",
    ends={
        Property(name="MessageDefinition123", type=iso20022_MessageChoreography, multiplicity=Multiplicity(1, 1)),
        Property(name="choreography", type=iso20022_MessageDefinition, multiplicity=Multiplicity(1, 9999))
    }
)
businessTransactionTrace120: BinaryAssociation = BinaryAssociation(
    name="businessTransactionTrace120",
    ends={
        Property(name="BusinessTransaction", type=iso20022_MessageChoreography, multiplicity=Multiplicity(1, 1)),
        Property(name="trace121", type=iso20022_BusinessTransaction, multiplicity=Multiplicity(0, 1))
    }
)
transmission126: BinaryAssociation = BinaryAssociation(
    name="transmission126",
    ends={
        Property(name="MessageTransmission128", type=iso20022_BusinessTransaction, multiplicity=Multiplicity(1, 1)),
        Property(name="businessTransaction127", type=iso20022_MessageTransmission, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageTransportMode129: BinaryAssociation = BinaryAssociation(
    name="messageTransportMode129",
    ends={
        Property(name="MessageTransportMode", type=iso20022_BusinessTransaction, multiplicity=Multiplicity(1, 1)),
        Property(name="businessTransaction130", type=iso20022_MessageTransportMode, multiplicity=Multiplicity(1, 1))
    }
)
subTransaction132: BinaryAssociation = BinaryAssociation(
    name="subTransaction132",
    ends={
        Property(name="BusinessTransaction133", type=iso20022_BusinessTransaction, multiplicity=Multiplicity(1, 1)),
        Property(name="parentTransaction", type=iso20022_BusinessTransaction, multiplicity=Multiplicity(0, 9999))
    }
)
parentTransaction135: BinaryAssociation = BinaryAssociation(
    name="parentTransaction135",
    ends={
        Property(name="BusinessTransaction136", type=iso20022_BusinessTransaction, multiplicity=Multiplicity(1, 1)),
        Property(name="subTransaction", type=iso20022_BusinessTransaction, multiplicity=Multiplicity(0, 1))
    }
)
trace137: BinaryAssociation = BinaryAssociation(
    name="trace137",
    ends={
        Property(name="MessageChoreography138", type=iso20022_BusinessTransaction, multiplicity=Multiplicity(1, 1)),
        Property(name="businessTransactionTrace", type=iso20022_MessageChoreography, multiplicity=Multiplicity(0, 9999))
    }
)
businessProcessTrace124: BinaryAssociation = BinaryAssociation(
    name="businessProcessTrace124",
    ends={
        Property(name="BusinessProcess", type=iso20022_BusinessTransaction, multiplicity=Multiplicity(1, 1)),
        Property(name="businessProcessTrace", type=iso20022_BusinessProcess, multiplicity=Multiplicity(1, 1))
    }
)
participant125: BinaryAssociation = BinaryAssociation(
    name="participant125",
    ends={
        Property(name="Participant", type=iso20022_BusinessTransaction, multiplicity=Multiplicity(1, 1)),
        Property(name="businessTransaction", type=iso20022_Participant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extended143: BinaryAssociation = BinaryAssociation(
    name="extended143",
    ends={
        Property(name="BusinessProcess144", type=iso20022_BusinessProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="extender", type=iso20022_BusinessProcess, multiplicity=Multiplicity(0, 9999))
    }
)
included146: BinaryAssociation = BinaryAssociation(
    name="included146",
    ends={
        Property(name="BusinessProcess147", type=iso20022_BusinessProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="includer", type=iso20022_BusinessProcess, multiplicity=Multiplicity(0, 9999))
    }
)
includer149: BinaryAssociation = BinaryAssociation(
    name="includer149",
    ends={
        Property(name="BusinessProcess150", type=iso20022_BusinessProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="included", type=iso20022_BusinessProcess, multiplicity=Multiplicity(0, 9999))
    }
)
businessRole151: BinaryAssociation = BinaryAssociation(
    name="businessRole151",
    ends={
        Property(name="BusinessRole", type=iso20022_BusinessProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="businessProcess", type=iso20022_BusinessRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
businessProcessTrace152: BinaryAssociation = BinaryAssociation(
    name="businessProcessTrace152",
    ends={
        Property(name="BusinessTransaction154", type=iso20022_BusinessProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="businessProcessTrace153", type=iso20022_BusinessTransaction, multiplicity=Multiplicity(0, 9999))
    }
)
extender140: BinaryAssociation = BinaryAssociation(
    name="extender140",
    ends={
        Property(name="BusinessProcess141", type=iso20022_BusinessProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="extended", type=iso20022_BusinessProcess, multiplicity=Multiplicity(0, 9999))
    }
)
businessProcess157: BinaryAssociation = BinaryAssociation(
    name="businessProcess157",
    ends={
        Property(name="BusinessProcess158", type=iso20022_BusinessRole, multiplicity=Multiplicity(1, 1)),
        Property(name="businessRole", type=iso20022_BusinessProcess, multiplicity=Multiplicity(1, 1))
    }
)
businessTransaction159: BinaryAssociation = BinaryAssociation(
    name="businessTransaction159",
    ends={
        Property(name="BusinessTransaction160", type=iso20022_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="participant", type=iso20022_BusinessTransaction, multiplicity=Multiplicity(1, 1))
    }
)
receives161: BinaryAssociation = BinaryAssociation(
    name="receives161",
    ends={
        Property(name="Receive", type=iso20022_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="receiver162", type=iso20022_Receive, multiplicity=Multiplicity(0, 9999))
    }
)
businessRoleTrace155: BinaryAssociation = BinaryAssociation(
    name="businessRoleTrace155",
    ends={
        Property(name="Participant156", type=iso20022_BusinessRole, multiplicity=Multiplicity(1, 1)),
        Property(name="businessRoleTrace", type=iso20022_Participant, multiplicity=Multiplicity(0, 9999))
    }
)
messageTransmission168: BinaryAssociation = BinaryAssociation(
    name="messageTransmission168",
    ends={
        Property(name="MessageTransmission169", type=iso20022_Receive, multiplicity=Multiplicity(1, 1)),
        Property(name="receive", type=iso20022_MessageTransmission, multiplicity=Multiplicity(1, 1))
    }
)
receiver170: BinaryAssociation = BinaryAssociation(
    name="receiver170",
    ends={
        Property(name="Participant171", type=iso20022_Receive, multiplicity=Multiplicity(1, 1)),
        Property(name="receives", type=iso20022_Participant, multiplicity=Multiplicity(1, 1))
    }
)
businessTransaction172: BinaryAssociation = BinaryAssociation(
    name="businessTransaction172",
    ends={
        Property(name="BusinessTransaction173", type=iso20022_MessageTransmission, multiplicity=Multiplicity(1, 1)),
        Property(name="transmission", type=iso20022_BusinessTransaction, multiplicity=Multiplicity(1, 1))
    }
)
sends163: BinaryAssociation = BinaryAssociation(
    name="sends163",
    ends={
        Property(name="Send", type=iso20022_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="sender164", type=iso20022_Send, multiplicity=Multiplicity(0, 9999))
    }
)
businessRoleTrace165: BinaryAssociation = BinaryAssociation(
    name="businessRoleTrace165",
    ends={
        Property(name="BusinessRole167", type=iso20022_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="businessRoleTrace166", type=iso20022_BusinessRole, multiplicity=Multiplicity(1, 1))
    }
)
send177: BinaryAssociation = BinaryAssociation(
    name="send177",
    ends={
        Property(name="Send178", type=iso20022_MessageTransmission, multiplicity=Multiplicity(1, 1)),
        Property(name="messageTransmission", type=iso20022_Send, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
receive179: BinaryAssociation = BinaryAssociation(
    name="receive179",
    ends={
        Property(name="Receive181", type=iso20022_MessageTransmission, multiplicity=Multiplicity(1, 1)),
        Property(name="messageTransmission180", type=iso20022_Receive, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sender182: BinaryAssociation = BinaryAssociation(
    name="sender182",
    ends={
        Property(name="Participant183", type=iso20022_Send, multiplicity=Multiplicity(1, 1)),
        Property(name="sends", type=iso20022_Participant, multiplicity=Multiplicity(1, 1))
    }
)
messageTransmission184: BinaryAssociation = BinaryAssociation(
    name="messageTransmission184",
    ends={
        Property(name="MessageTransmission185", type=iso20022_Send, multiplicity=Multiplicity(1, 1)),
        Property(name="send", type=iso20022_MessageTransmission, multiplicity=Multiplicity(1, 1))
    }
)
derivation174: BinaryAssociation = BinaryAssociation(
    name="derivation174",
    ends={
        Property(name="MessageDefinition176", type=iso20022_MessageTransmission, multiplicity=Multiplicity(1, 1)),
        Property(name="trace175", type=iso20022_MessageDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
businessTransaction186: BinaryAssociation = BinaryAssociation(
    name="businessTransaction186",
    ends={
        Property(name="BusinessTransaction187", type=iso20022_MessageTransportMode, multiplicity=Multiplicity(1, 1)),
        Property(name="messageTransportMode", type=iso20022_BusinessTransaction, multiplicity=Multiplicity(0, 9999))
    }
)
type188: BinaryAssociation = BinaryAssociation(
    name="type188",
    ends={
        Property(name="iso20022_MessageComponentType", type=iso20022_MessageAssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="iso20022_MessageAssociationEnd", type=iso20022_MessageComponentType, multiplicity=Multiplicity(1, 1))
    }
)
simpleType189: BinaryAssociation = BinaryAssociation(
    name="simpleType189",
    ends={
        Property(name="iso20022_DataType190", type=iso20022_MessageAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="iso20022_MessageAttribute", type=iso20022_DataType, multiplicity=Multiplicity(0, 1))
    }
)
complexType191: BinaryAssociation = BinaryAssociation(
    name="complexType191",
    ends={
        Property(name="iso20022_MessageComponentType193", type=iso20022_MessageAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="iso20022_MessageAttribute192", type=iso20022_MessageComponentType, multiplicity=Multiplicity(0, 1))
    }
)
complexType196: BinaryAssociation = BinaryAssociation(
    name="complexType196",
    ends={
        Property(name="iso20022_BusinessComponent", type=iso20022_BusinessAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="iso20022_BusinessAttribute197", type=iso20022_BusinessComponent, multiplicity=Multiplicity(0, 1))
    }
)
simpleType194: BinaryAssociation = BinaryAssociation(
    name="simpleType194",
    ends={
        Property(name="iso20022_DataType195", type=iso20022_BusinessAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="iso20022_BusinessAttribute", type=iso20022_DataType, multiplicity=Multiplicity(0, 1))
    }
)
trace200: BinaryAssociation = BinaryAssociation(
    name="trace200",
    ends={
        Property(name="CodeSet202", type=iso20022_CodeSet, multiplicity=Multiplicity(1, 1)),
        Property(name="derivation201", type=iso20022_CodeSet, multiplicity=Multiplicity(0, 1))
    }
)
derivation204: BinaryAssociation = BinaryAssociation(
    name="derivation204",
    ends={
        Property(name="CodeSet206", type=iso20022_CodeSet, multiplicity=Multiplicity(1, 1)),
        Property(name="trace205", type=iso20022_CodeSet, multiplicity=Multiplicity(0, 9999))
    }
)
owner198: BinaryAssociation = BinaryAssociation(
    name="owner198",
    ends={
        Property(name="CodeSet", type=iso20022_Code, multiplicity=Multiplicity(1, 1)),
        Property(name="code", type=iso20022_CodeSet, multiplicity=Multiplicity(1, 1))
    }
)
code207: BinaryAssociation = BinaryAssociation(
    name="code207",
    ends={
        Property(name="Code", type=iso20022_CodeSet, multiplicity=Multiplicity(1, 1)),
        Property(name="owner208", type=iso20022_Code, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
currencyIdentifierSet209: BinaryAssociation = BinaryAssociation(
    name="currencyIdentifierSet209",
    ends={
        Property(name="iso20022_DataType210", type=iso20022_Amount, multiplicity=Multiplicity(1, 1)),
        Property(name="iso20022_Amount", type=iso20022_DataType, multiplicity=Multiplicity(0, 1))
    }
)
endPoints211: BinaryAssociation = BinaryAssociation(
    name="endPoints211",
    ends={
        Property(name="iso20022_MessageElementContainer", type=iso20022_EndPointCategory, multiplicity=Multiplicity(1, 1)),
        Property(name="iso20022_EndPointCategory", type=iso20022_MessageElementContainer, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_iso20022_Address_ModelEntity = Generalization(general=ModelEntity, specific=iso20022_Address)
gen_iso20022_MessageTransportSystem_ModelEntity = Generalization(general=ModelEntity, specific=iso20022_MessageTransportSystem)
gen_iso20022_BroadcastList_ModelEntity = Generalization(general=ModelEntity, specific=iso20022_BroadcastList)
gen_iso20022_MessagingEndpoint_ModelEntity = Generalization(general=ModelEntity, specific=iso20022_MessagingEndpoint)
gen_iso20022_MessageInstance_ModelEntity = Generalization(general=ModelEntity, specific=iso20022_MessageInstance)
gen_iso20022_TransportMessage_ModelEntity = Generalization(general=ModelEntity, specific=iso20022_TransportMessage)
gen_iso20022_SyntaxMessageScheme_TopLevelCatalogueEntry = Generalization(general=TopLevelCatalogueEntry, specific=iso20022_SyntaxMessageScheme)
gen_iso20022_TopLevelCatalogueEntry_RepositoryConcept = Generalization(general=RepositoryConcept, specific=iso20022_TopLevelCatalogueEntry)
gen_iso20022_RepositoryConcept_ModelEntity = Generalization(general=ModelEntity, specific=iso20022_RepositoryConcept)
gen_iso20022_SemanticMarkup_ModelEntity = Generalization(general=ModelEntity, specific=iso20022_SemanticMarkup)
gen_iso20022_SemanticMarkupElement_ModelEntity = Generalization(general=ModelEntity, specific=iso20022_SemanticMarkupElement)
gen_iso20022_Constraint_RepositoryConcept = Generalization(general=RepositoryConcept, specific=iso20022_Constraint)
gen_iso20022_Doclet_ModelEntity = Generalization(general=ModelEntity, specific=iso20022_Doclet)
gen_iso20022_BusinessProcessCatalogue_ModelEntity = Generalization(general=ModelEntity, specific=iso20022_BusinessProcessCatalogue)
gen_iso20022_DataDictionary_ModelEntity = Generalization(general=ModelEntity, specific=iso20022_DataDictionary)
gen_iso20022_TopLevelDictionaryEntry_RepositoryConcept = Generalization(general=RepositoryConcept, specific=iso20022_TopLevelDictionaryEntry)
gen_iso20022_Repository_ModelEntity = Generalization(general=ModelEntity, specific=iso20022_Repository)
gen_iso20022_MessageDefinition_RepositoryType = Generalization(general=RepositoryType, specific=iso20022_MessageDefinition)
gen_iso20022_MessageSet_TopLevelCatalogueEntry = Generalization(general=TopLevelCatalogueEntry, specific=iso20022_MessageSet)
gen_iso20022_RepositoryType_RepositoryConcept = Generalization(general=RepositoryConcept, specific=iso20022_RepositoryType)
gen_iso20022_Encoding_ModelEntity = Generalization(general=ModelEntity, specific=iso20022_Encoding)
gen_iso20022_Syntax_ModelEntity = Generalization(general=ModelEntity, specific=iso20022_Syntax)
gen_iso20022_Xor_RepositoryConcept = Generalization(general=RepositoryConcept, specific=iso20022_Xor)
gen_iso20022_BusinessArea_TopLevelCatalogueEntry = Generalization(general=TopLevelCatalogueEntry, specific=iso20022_BusinessArea)
gen_iso20022_MessageElement_MessageConstruct = Generalization(general=MessageConstruct, specific=iso20022_MessageElement)
gen_iso20022_MessageElement_MessageConcept = Generalization(general=MessageConcept, specific=iso20022_MessageElement)
gen_iso20022_MessageConstruct_Construct = Generalization(general=Construct, specific=iso20022_MessageConstruct)
gen_iso20022_LogicalType_RepositoryType = Generalization(general=RepositoryType, specific=iso20022_LogicalType)
gen_iso20022_Construct_RepositoryConcept = Generalization(general=RepositoryConcept, specific=iso20022_Construct)
gen_iso20022_Construct_MultiplicityEntity = Generalization(general=MultiplicityEntity, specific=iso20022_Construct)
gen_iso20022_MessageConcept_ModelEntity = Generalization(general=ModelEntity, specific=iso20022_MessageConcept)
gen_iso20022_BusinessComponent_TopLevelDictionaryEntry = Generalization(general=TopLevelDictionaryEntry, specific=iso20022_BusinessComponent)
gen_iso20022_BusinessComponent_BusinessElementType = Generalization(general=BusinessElementType, specific=iso20022_BusinessComponent)
gen_iso20022_BusinessComponent_BusinessConcept = Generalization(general=BusinessConcept, specific=iso20022_BusinessComponent)
gen_iso20022_BusinessElementType_RepositoryType = Generalization(general=RepositoryType, specific=iso20022_BusinessElementType)
gen_iso20022_BusinessConcept_ModelEntity = Generalization(general=ModelEntity, specific=iso20022_BusinessConcept)
gen_iso20022_BusinessElement_Construct = Generalization(general=Construct, specific=iso20022_BusinessElement)
gen_iso20022_BusinessElement_BusinessConcept = Generalization(general=BusinessConcept, specific=iso20022_BusinessElement)
gen_iso20022_MessageComponentType_TopLevelDictionaryEntry = Generalization(general=TopLevelDictionaryEntry, specific=iso20022_MessageComponentType)
gen_iso20022_MessageComponentType_LogicalType = Generalization(general=LogicalType, specific=iso20022_MessageComponentType)
gen_iso20022_MessageComponentType_MessageConcept = Generalization(general=MessageConcept, specific=iso20022_MessageComponentType)
gen_iso20022_DataType_TopLevelDictionaryEntry = Generalization(general=TopLevelDictionaryEntry, specific=iso20022_DataType)
gen_iso20022_DataType_BusinessElementType = Generalization(general=BusinessElementType, specific=iso20022_DataType)
gen_iso20022_DataType_LogicalType = Generalization(general=LogicalType, specific=iso20022_DataType)
gen_iso20022_BusinessAssociationEnd_BusinessElement = Generalization(general=BusinessElement, specific=iso20022_BusinessAssociationEnd)
gen_iso20022_MessageBuildingBlock_MessageConstruct = Generalization(general=MessageConstruct, specific=iso20022_MessageBuildingBlock)
gen_iso20022_MessageElementContainer_MessageComponentType = Generalization(general=MessageComponentType, specific=iso20022_MessageElementContainer)
gen_iso20022_MessageComponent_MessageElementContainer = Generalization(general=MessageElementContainer, specific=iso20022_MessageComponent)
gen_iso20022_BusinessTransaction_TopLevelCatalogueEntry = Generalization(general=TopLevelCatalogueEntry, specific=iso20022_BusinessTransaction)
gen_iso20022_MessageChoreography_TopLevelCatalogueEntry = Generalization(general=TopLevelCatalogueEntry, specific=iso20022_MessageChoreography)
gen_iso20022_BusinessProcess_TopLevelCatalogueEntry = Generalization(general=TopLevelCatalogueEntry, specific=iso20022_BusinessProcess)
gen_iso20022_Participant_RepositoryConcept = Generalization(general=RepositoryConcept, specific=iso20022_Participant)
gen_iso20022_Participant_MultiplicityEntity = Generalization(general=MultiplicityEntity, specific=iso20022_Participant)
gen_iso20022_BusinessRole_RepositoryConcept = Generalization(general=RepositoryConcept, specific=iso20022_BusinessRole)
gen_iso20022_Receive_ModelEntity = Generalization(general=ModelEntity, specific=iso20022_Receive)
gen_iso20022_MessageTransmission_RepositoryConcept = Generalization(general=RepositoryConcept, specific=iso20022_MessageTransmission)
gen_iso20022_Send_ModelEntity = Generalization(general=ModelEntity, specific=iso20022_Send)
gen_iso20022_MessageTransportMode_TopLevelCatalogueEntry = Generalization(general=TopLevelCatalogueEntry, specific=iso20022_MessageTransportMode)
gen_iso20022_MessageDefinitionIdentifier_ModelEntity = Generalization(general=ModelEntity, specific=iso20022_MessageDefinitionIdentifier)
gen_iso20022_Conversation_ModelEntity = Generalization(general=ModelEntity, specific=iso20022_Conversation)
gen_iso20022_MessageAssociationEnd_MessageElement = Generalization(general=MessageElement, specific=iso20022_MessageAssociationEnd)
gen_iso20022_BusinessAttribute_BusinessElement = Generalization(general=BusinessElement, specific=iso20022_BusinessAttribute)
gen_iso20022_MessageAttribute_MessageElement = Generalization(general=MessageElement, specific=iso20022_MessageAttribute)
gen_iso20022_Text_String = Generalization(general=String, specific=iso20022_Text)
gen_iso20022_String_DataType = Generalization(general=DataType, specific=iso20022_String)
gen_iso20022_Indicator_Boolean = Generalization(general=Boolean, specific=iso20022_Indicator)
gen_iso20022_Boolean_DataType = Generalization(general=DataType, specific=iso20022_Boolean)
gen_iso20022_IdentifierSet_String = Generalization(general=String, specific=iso20022_IdentifierSet)
gen_iso20022_Decimal_DataType = Generalization(general=DataType, specific=iso20022_Decimal)
gen_iso20022_Rate_Decimal = Generalization(general=Decimal, specific=iso20022_Rate)
gen_iso20022_Quantity_Decimal = Generalization(general=Decimal, specific=iso20022_Quantity)
gen_iso20022_ExternalSchema_MessageComponentType = Generalization(general=MessageComponentType, specific=iso20022_ExternalSchema)
gen_iso20022_CodeSet_String = Generalization(general=String, specific=iso20022_CodeSet)
gen_iso20022_Code_RepositoryConcept = Generalization(general=RepositoryConcept, specific=iso20022_Code)
gen_iso20022_ChoiceComponent_MessageElementContainer = Generalization(general=MessageElementContainer, specific=iso20022_ChoiceComponent)
gen_iso20022_Amount_Decimal = Generalization(general=Decimal, specific=iso20022_Amount)
gen_iso20022_EndPointCategory_TopLevelDictionaryEntry = Generalization(general=TopLevelDictionaryEntry, specific=iso20022_EndPointCategory)
gen_iso20022_AbstractDateTimeConcept_DataType = Generalization(general=DataType, specific=iso20022_AbstractDateTimeConcept)
gen_iso20022_Binary_DataType = Generalization(general=DataType, specific=iso20022_Binary)
gen_iso20022_Date_AbstractDateTimeConcept = Generalization(general=AbstractDateTimeConcept, specific=iso20022_Date)
gen_iso20022_Duration_AbstractDateTimeConcept = Generalization(general=AbstractDateTimeConcept, specific=iso20022_Duration)
gen_iso20022_Month_AbstractDateTimeConcept = Generalization(general=AbstractDateTimeConcept, specific=iso20022_Month)
gen_iso20022_MonthDay_AbstractDateTimeConcept = Generalization(general=AbstractDateTimeConcept, specific=iso20022_MonthDay)
gen_iso20022_Time_AbstractDateTimeConcept = Generalization(general=AbstractDateTimeConcept, specific=iso20022_Time)
gen_iso20022_DateTime_AbstractDateTimeConcept = Generalization(general=AbstractDateTimeConcept, specific=iso20022_DateTime)
gen_iso20022_Day_AbstractDateTimeConcept = Generalization(general=AbstractDateTimeConcept, specific=iso20022_Day)
gen_iso20022_UserDefined_MessageComponentType = Generalization(general=MessageComponentType, specific=iso20022_UserDefined)
gen_iso20022_Year_AbstractDateTimeConcept = Generalization(general=AbstractDateTimeConcept, specific=iso20022_Year)
gen_iso20022_YearMonth_AbstractDateTimeConcept = Generalization(general=AbstractDateTimeConcept, specific=iso20022_YearMonth)
gen_iso20022_SchemaType_DataType = Generalization(general=DataType, specific=iso20022_SchemaType)
gen_iso20022_IndustryMessageSet_TopLevelCatalogueEntry = Generalization(general=TopLevelCatalogueEntry, specific=iso20022_IndustryMessageSet)
gen_iso20022_ConvergenceDocumentation_TopLevelCatalogueEntry = Generalization(general=TopLevelCatalogueEntry, specific=iso20022_ConvergenceDocumentation)
gen_iso20022_ISO15022MessageSet_IndustryMessageSet = Generalization(general=IndustryMessageSet, specific=iso20022_ISO15022MessageSet)

# Domain Model
domain_model = DomainModel(
    name="iso20022",
    types={iso20022_Address, ModelEntity, iso20022_ModelEntity, iso20022_BroadcastList, iso20022_MessagingEndpoint, iso20022_MessageTransportSystem, iso20022_TransportMessage, iso20022_MessageInstance, TopLevelCatalogueEntry, iso20022_MessageDefinition, iso20022_TopLevelCatalogueEntry, RepositoryConcept, iso20022_BusinessProcessCatalogue, iso20022_RepositoryConcept, iso20022_SyntaxMessageScheme, iso20022_SemanticMarkup, iso20022_Doclet, iso20022_SemanticMarkupElement, iso20022_Constraint, iso20022_Repository, iso20022_TopLevelDictionaryEntry, iso20022_DataDictionary, iso20022_MessageSet, iso20022_BusinessArea, RepositoryType, iso20022_MessageChoreography, iso20022_MessageTransmission, iso20022_MessageDefinitionIdentifier, iso20022_Xor, iso20022_MessageBuildingBlock, iso20022_Syntax, iso20022_Encoding, iso20022_RepositoryType, iso20022_MessageElement, iso20022_MessageComponent, iso20022_BusinessComponent, MessageConstruct, MessageConcept, iso20022_MessageConstruct, Construct, iso20022_LogicalType, iso20022_BusinessElement, iso20022_MessageElementContainer, iso20022_MultiplicityEntity, iso20022_MessageConcept, iso20022_Construct, MultiplicityEntity, iso20022_MessageComponentType, TopLevelDictionaryEntry, BusinessElementType, BusinessConcept, iso20022_BusinessElementType, iso20022_BusinessConcept, iso20022_BusinessAssociationEnd, LogicalType, iso20022_DataType, BusinessElement, MessageComponentType, MessageElementContainer, iso20022_BusinessTransaction, iso20022_MessageTransportMode, iso20022_BusinessProcess, iso20022_Participant, iso20022_BusinessRole, iso20022_Receive, iso20022_Send, iso20022_Conversation, iso20022_MessageAssociationEnd, MessageElement, iso20022_BusinessAttribute, iso20022_MessageAttribute, iso20022_Text, String, iso20022_String, DataType, iso20022_Indicator, Boolean, iso20022_Boolean, iso20022_IdentifierSet, iso20022_Decimal, iso20022_Rate, Decimal, iso20022_Quantity, iso20022_ExternalSchema, iso20022_Code, iso20022_CodeSet, iso20022_ChoiceComponent, iso20022_Amount, iso20022_EndPointCategory, iso20022_AbstractDateTimeConcept, iso20022_Binary, iso20022_Date, AbstractDateTimeConcept, iso20022_Duration, iso20022_Month, iso20022_MonthDay, iso20022_Time, iso20022_DateTime, iso20022_Day, iso20022_UserDefined, iso20022_Year, iso20022_YearMonth, iso20022_SchemaType, iso20022_IndustryMessageSet, iso20022_ConvergenceDocumentation, iso20022_ISO15022MessageSet, IndustryMessageSet, RegistrationStatus, Aggregation, DeliveryAssurance, MessageCasting, MessageDeliveryOrder, Durability, MessageValidationOnOff, MessageValidationLevel, ReceiverAsynchronicity, SenderAsynchronicity, MessageValidationResults, ProcessContent, Namespace, SchemaTypeKind, ISO20022Version},
    associations={nextVersions3, previousVersion5, broadCastList0, endpoint1, transportSystem8, receivedMessage9, sentMessage10, location12, address7, sender17, messageInstance19, receiver20, endpoint15, messageDefinitionTrace25, businessProcessCatalogue26, specification22, transportMessage23, semanticMarkup27, doclet28, elements31, constraint30, repository34, topLevelCatalogueEntry35, owner33, topLevelDictionaryEntry41, repository42, dataDictionary37, businessProcessCatalogue38, messageSet47, businessArea48, dataDictionary45, messageBuildingBlock52, choreography53, trace55, messageDefinitionIdentifier57, xors50, generatedSyntax60, validEncoding61, derivation59, possibleEncodings65, generatedFor67, messageSet69, syntax71, messageDefinition62, messageDefinition73, impactedElements75, messageComponent76, impactedMessageBuildingBlocks77, businessComponentTrace83, messageDefinition80, componentContext86, xmlMemberType87, businessElementTrace84, memberType88, subType90, superType93, element95, derivationComponent97, derivation100, associationDomain98, derivationElement99, elementContext103, messageBuildingBlock105, trace106, businessElementType102, simpleType108, complexType110, type114, opposite113, messageElement116, xors118, messageDefinition122, businessTransactionTrace120, transmission126, messageTransportMode129, subTransaction132, parentTransaction135, trace137, businessProcessTrace124, participant125, extended143, included146, includer149, businessRole151, businessProcessTrace152, extender140, businessProcess157, businessTransaction159, receives161, businessRoleTrace155, messageTransmission168, receiver170, businessTransaction172, sends163, businessRoleTrace165, send177, receive179, sender182, messageTransmission184, derivation174, businessTransaction186, type188, simpleType189, complexType191, complexType196, simpleType194, trace200, derivation204, owner198, code207, currencyIdentifierSet209, endPoints211},
    generalizations={gen_iso20022_Address_ModelEntity, gen_iso20022_MessageTransportSystem_ModelEntity, gen_iso20022_BroadcastList_ModelEntity, gen_iso20022_MessagingEndpoint_ModelEntity, gen_iso20022_MessageInstance_ModelEntity, gen_iso20022_TransportMessage_ModelEntity, gen_iso20022_SyntaxMessageScheme_TopLevelCatalogueEntry, gen_iso20022_TopLevelCatalogueEntry_RepositoryConcept, gen_iso20022_RepositoryConcept_ModelEntity, gen_iso20022_SemanticMarkup_ModelEntity, gen_iso20022_SemanticMarkupElement_ModelEntity, gen_iso20022_Constraint_RepositoryConcept, gen_iso20022_Doclet_ModelEntity, gen_iso20022_BusinessProcessCatalogue_ModelEntity, gen_iso20022_DataDictionary_ModelEntity, gen_iso20022_TopLevelDictionaryEntry_RepositoryConcept, gen_iso20022_Repository_ModelEntity, gen_iso20022_MessageDefinition_RepositoryType, gen_iso20022_MessageSet_TopLevelCatalogueEntry, gen_iso20022_RepositoryType_RepositoryConcept, gen_iso20022_Encoding_ModelEntity, gen_iso20022_Syntax_ModelEntity, gen_iso20022_Xor_RepositoryConcept, gen_iso20022_BusinessArea_TopLevelCatalogueEntry, gen_iso20022_MessageElement_MessageConstruct, gen_iso20022_MessageElement_MessageConcept, gen_iso20022_MessageConstruct_Construct, gen_iso20022_LogicalType_RepositoryType, gen_iso20022_Construct_RepositoryConcept, gen_iso20022_Construct_MultiplicityEntity, gen_iso20022_MessageConcept_ModelEntity, gen_iso20022_BusinessComponent_TopLevelDictionaryEntry, gen_iso20022_BusinessComponent_BusinessElementType, gen_iso20022_BusinessComponent_BusinessConcept, gen_iso20022_BusinessElementType_RepositoryType, gen_iso20022_BusinessConcept_ModelEntity, gen_iso20022_BusinessElement_Construct, gen_iso20022_BusinessElement_BusinessConcept, gen_iso20022_MessageComponentType_TopLevelDictionaryEntry, gen_iso20022_MessageComponentType_LogicalType, gen_iso20022_MessageComponentType_MessageConcept, gen_iso20022_DataType_TopLevelDictionaryEntry, gen_iso20022_DataType_BusinessElementType, gen_iso20022_DataType_LogicalType, gen_iso20022_BusinessAssociationEnd_BusinessElement, gen_iso20022_MessageBuildingBlock_MessageConstruct, gen_iso20022_MessageElementContainer_MessageComponentType, gen_iso20022_MessageComponent_MessageElementContainer, gen_iso20022_BusinessTransaction_TopLevelCatalogueEntry, gen_iso20022_MessageChoreography_TopLevelCatalogueEntry, gen_iso20022_BusinessProcess_TopLevelCatalogueEntry, gen_iso20022_Participant_RepositoryConcept, gen_iso20022_Participant_MultiplicityEntity, gen_iso20022_BusinessRole_RepositoryConcept, gen_iso20022_Receive_ModelEntity, gen_iso20022_MessageTransmission_RepositoryConcept, gen_iso20022_Send_ModelEntity, gen_iso20022_MessageTransportMode_TopLevelCatalogueEntry, gen_iso20022_MessageDefinitionIdentifier_ModelEntity, gen_iso20022_Conversation_ModelEntity, gen_iso20022_MessageAssociationEnd_MessageElement, gen_iso20022_BusinessAttribute_BusinessElement, gen_iso20022_MessageAttribute_MessageElement, gen_iso20022_Text_String, gen_iso20022_String_DataType, gen_iso20022_Indicator_Boolean, gen_iso20022_Boolean_DataType, gen_iso20022_IdentifierSet_String, gen_iso20022_Decimal_DataType, gen_iso20022_Rate_Decimal, gen_iso20022_Quantity_Decimal, gen_iso20022_ExternalSchema_MessageComponentType, gen_iso20022_CodeSet_String, gen_iso20022_Code_RepositoryConcept, gen_iso20022_ChoiceComponent_MessageElementContainer, gen_iso20022_Amount_Decimal, gen_iso20022_EndPointCategory_TopLevelDictionaryEntry, gen_iso20022_AbstractDateTimeConcept_DataType, gen_iso20022_Binary_DataType, gen_iso20022_Date_AbstractDateTimeConcept, gen_iso20022_Duration_AbstractDateTimeConcept, gen_iso20022_Month_AbstractDateTimeConcept, gen_iso20022_MonthDay_AbstractDateTimeConcept, gen_iso20022_Time_AbstractDateTimeConcept, gen_iso20022_DateTime_AbstractDateTimeConcept, gen_iso20022_Day_AbstractDateTimeConcept, gen_iso20022_UserDefined_MessageComponentType, gen_iso20022_Year_AbstractDateTimeConcept, gen_iso20022_YearMonth_AbstractDateTimeConcept, gen_iso20022_SchemaType_DataType, gen_iso20022_IndustryMessageSet_TopLevelCatalogueEntry, gen_iso20022_ConvergenceDocumentation_TopLevelCatalogueEntry, gen_iso20022_ISO15022MessageSet_IndustryMessageSet},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)