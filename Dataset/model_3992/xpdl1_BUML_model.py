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
AccessLevelType: Enumeration = Enumeration(
    name="AccessLevelType",
    literals={
            EnumerationLiteral(name="PUBLIC"),
			EnumerationLiteral(name="PRIVATE")
    }
)

DurationUnitType: Enumeration = Enumeration(
    name="DurationUnitType",
    literals={
            EnumerationLiteral(name="Y"),
			EnumerationLiteral(name="M"),
			EnumerationLiteral(name="D"),
			EnumerationLiteral(name="h"),
			EnumerationLiteral(name="m1"),
			EnumerationLiteral(name="s")
    }
)

ExecutionType: Enumeration = Enumeration(
    name="ExecutionType",
    literals={
            EnumerationLiteral(name="ASYNCHR"),
			EnumerationLiteral(name="SYNCHR")
    }
)

ExecutionType1: Enumeration = Enumeration(
    name="ExecutionType1",
    literals={
            EnumerationLiteral(name="ASYNCHR"),
			EnumerationLiteral(name="SYNCHR")
    }
)

GraphConformanceType: Enumeration = Enumeration(
    name="GraphConformanceType",
    literals={
            EnumerationLiteral(name="FULLBLOCKED"),
			EnumerationLiteral(name="LOOPBLOCKED"),
			EnumerationLiteral(name="NONBLOCKED")
    }
)

InstantiationType: Enumeration = Enumeration(
    name="InstantiationType",
    literals={
            EnumerationLiteral(name="ONCE"),
			EnumerationLiteral(name="MULTIPLE")
    }
)

IsArrayType: Enumeration = Enumeration(
    name="IsArrayType",
    literals={
            EnumerationLiteral(name="TRUE"),
			EnumerationLiteral(name="FALSE")
    }
)

ModeType: Enumeration = Enumeration(
    name="ModeType",
    literals={
            EnumerationLiteral(name="IN"),
			EnumerationLiteral(name="OUT"),
			EnumerationLiteral(name="INOUT")
    }
)

PublicationStatusType: Enumeration = Enumeration(
    name="PublicationStatusType",
    literals={
            EnumerationLiteral(name="UNDERREVISION"),
			EnumerationLiteral(name="RELEASED"),
			EnumerationLiteral(name="UNDERTEST")
    }
)

TypeType: Enumeration = Enumeration(
    name="TypeType",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="XOR")
    }
)

TypeType1: Enumeration = Enumeration(
    name="TypeType1",
    literals={
            EnumerationLiteral(name="RESOURCESET"),
			EnumerationLiteral(name="RESOURCE"),
			EnumerationLiteral(name="ROLE"),
			EnumerationLiteral(name="ORGANIZATIONALUNIT"),
			EnumerationLiteral(name="HUMAN"),
			EnumerationLiteral(name="SYSTEM")
    }
)

TypeType2: Enumeration = Enumeration(
    name="TypeType2",
    literals={
            EnumerationLiteral(name="CONDITION"),
			EnumerationLiteral(name="OTHERWISE"),
			EnumerationLiteral(name="EXCEPTION"),
			EnumerationLiteral(name="DEFAULTEXCEPTION")
    }
)

TypeType3: Enumeration = Enumeration(
    name="TypeType3",
    literals={
            EnumerationLiteral(name="STRING"),
			EnumerationLiteral(name="FLOAT"),
			EnumerationLiteral(name="INTEGER"),
			EnumerationLiteral(name="REFERENCE"),
			EnumerationLiteral(name="DATETIME"),
			EnumerationLiteral(name="BOOLEAN"),
			EnumerationLiteral(name="PERFORMER")
    }
)

TypeType4: Enumeration = Enumeration(
    name="TypeType4",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="XOR")
    }
)

TypeType5: Enumeration = Enumeration(
    name="TypeType5",
    literals={
            EnumerationLiteral(name="APPLICATION"),
			EnumerationLiteral(name="PROCEDURE")
    }
)

# Classes
xpdl1_ActivitySetsType = Class(name="xpdl1::ActivitySetsType")
xpdl1_ActivitiesType = Class(name="xpdl1::ActivitiesType")
xpdl1_ActivityType = Class(name="xpdl1::ActivityType")
xpdl1_ActivitySetType = Class(name="xpdl1::ActivitySetType")
xpdl1_TransitionsType = Class(name="xpdl1::TransitionsType")
xpdl1_RouteType = Class(name="xpdl1::RouteType")
xpdl1_ImplementationType = Class(name="xpdl1::ImplementationType")
xpdl1_BlockActivityType = Class(name="xpdl1::BlockActivityType")
xpdl1_StartModeType = Class(name="xpdl1::StartModeType")
xpdl1_FinishModeType = Class(name="xpdl1::FinishModeType")
xpdl1_DeadlineType = Class(name="xpdl1::DeadlineType")
xpdl1_SimulationInformationType = Class(name="xpdl1::SimulationInformationType")
xpdl1_TransitionRestrictionsType = Class(name="xpdl1::TransitionRestrictionsType")
xpdl1_ExtendedAttributesType = Class(name="xpdl1::ExtendedAttributesType")
xpdl1_ActualParametersType = Class(name="xpdl1::ActualParametersType")
xpdl1_ApplicationsType = Class(name="xpdl1::ApplicationsType")
xpdl1_ApplicationType = Class(name="xpdl1::ApplicationType")
xpdl1_FormalParametersType = Class(name="xpdl1::FormalParametersType")
xpdl1_ExternalReferenceType = Class(name="xpdl1::ExternalReferenceType")
xpdl1_ArrayTypeType = Class(name="xpdl1::ArrayTypeType")
xpdl1_BasicTypeType = Class(name="xpdl1::BasicTypeType")
xpdl1_DeclaredTypeType = Class(name="xpdl1::DeclaredTypeType")
xpdl1_SchemaTypeType = Class(name="xpdl1::SchemaTypeType")
xpdl1_RecordTypeType = Class(name="xpdl1::RecordTypeType")
xpdl1_UnionTypeType = Class(name="xpdl1::UnionTypeType")
xpdl1_EnumerationTypeType = Class(name="xpdl1::EnumerationTypeType")
xpdl1_ListTypeType = Class(name="xpdl1::ListTypeType")
xpdl1_AutomaticType = Class(name="xpdl1::AutomaticType")
xpdl1_ConditionType = Class(name="xpdl1::ConditionType")
xpdl1_XpressionType = Class(name="xpdl1::XpressionType")
xpdl1_ConformanceClassType = Class(name="xpdl1::ConformanceClassType")
xpdl1_DataFieldsType = Class(name="xpdl1::DataFieldsType")
xpdl1_DataFieldType = Class(name="xpdl1::DataFieldType")
xpdl1_DataTypeType = Class(name="xpdl1::DataTypeType")
xpdl1_EObject = Class(name="xpdl1::EObject")
xpdl1_DocumentRoot = Class(name="xpdl1::DocumentRoot")
xpdl1_EStringToStringMapEntry = Class(name="xpdl1::EStringToStringMapEntry")
xpdl1_ExternalPackagesType = Class(name="xpdl1::ExternalPackagesType")
xpdl1_EnumerationValueType = Class(name="xpdl1::EnumerationValueType")
xpdl1_ExtendedAttributeType = Class(name="xpdl1::ExtendedAttributeType")
xpdl1_ExternalPackageType = Class(name="xpdl1::ExternalPackageType")
xpdl1_FormalParameterType = Class(name="xpdl1::FormalParameterType")
xpdl1_JoinType = Class(name="xpdl1::JoinType")
xpdl1_PackageHeaderType = Class(name="xpdl1::PackageHeaderType")
xpdl1_ParticipantType = Class(name="xpdl1::ParticipantType")
xpdl1_ManualType = Class(name="xpdl1::ManualType")
xpdl1_MemberType = Class(name="xpdl1::MemberType")
xpdl1_NoType = Class(name="xpdl1::NoType")
xpdl1_PackageType = Class(name="xpdl1::PackageType")
xpdl1_ParticipantsType = Class(name="xpdl1::ParticipantsType")
xpdl1_ProcessHeaderType = Class(name="xpdl1::ProcessHeaderType")
xpdl1_RedefinableHeaderType = Class(name="xpdl1::RedefinableHeaderType")
xpdl1_ParticipantTypeType = Class(name="xpdl1::ParticipantTypeType")
xpdl1_ResponsiblesType = Class(name="xpdl1::ResponsiblesType")
xpdl1_ScriptType = Class(name="xpdl1::ScriptType")
xpdl1_SplitType = Class(name="xpdl1::SplitType")
xpdl1_SubFlowType = Class(name="xpdl1::SubFlowType")
xpdl1_TimeEstimationType = Class(name="xpdl1::TimeEstimationType")
xpdl1_ToolType = Class(name="xpdl1::ToolType")
xpdl1_TransitionType = Class(name="xpdl1::TransitionType")
xpdl1_TransitionRefType = Class(name="xpdl1::TransitionRefType")
xpdl1_TransitionRefsType = Class(name="xpdl1::TransitionRefsType")
xpdl1_TypeDeclarationType = Class(name="xpdl1::TypeDeclarationType")
xpdl1_TypeDeclarationsType = Class(name="xpdl1::TypeDeclarationsType")
xpdl1_TransitionRestrictionType = Class(name="xpdl1::TransitionRestrictionType")
xpdl1_WorkflowProcessType = Class(name="xpdl1::WorkflowProcessType")
xpdl1_WorkflowProcessesType = Class(name="xpdl1::WorkflowProcessesType")

# xpdl1_ActivitySetsType class attributes and methods

# xpdl1_ActivitiesType class attributes and methods

# xpdl1_ActivityType class attributes and methods
xpdl1_ActivityType_description: Property = Property(name="description", type=StringType)
xpdl1_ActivityType_limit: Property = Property(name="limit", type=StringType)
xpdl1_ActivityType_performer: Property = Property(name="performer", type=StringType)
xpdl1_ActivityType_priority: Property = Property(name="priority", type=StringType)
xpdl1_ActivityType_icon: Property = Property(name="icon", type=StringType)
xpdl1_ActivityType_documentation: Property = Property(name="documentation", type=StringType)
xpdl1_ActivityType_id: Property = Property(name="id", type=StringType)
xpdl1_ActivityType_name: Property = Property(name="name", type=StringType)
xpdl1_ActivityType.attributes={xpdl1_ActivityType_documentation, xpdl1_ActivityType_performer, xpdl1_ActivityType_limit, xpdl1_ActivityType_priority, xpdl1_ActivityType_id, xpdl1_ActivityType_description, xpdl1_ActivityType_name, xpdl1_ActivityType_icon}

# xpdl1_ActivitySetType class attributes and methods
xpdl1_ActivitySetType_id: Property = Property(name="id", type=StringType)
xpdl1_ActivitySetType.attributes={xpdl1_ActivitySetType_id}

# xpdl1_TransitionsType class attributes and methods

# xpdl1_RouteType class attributes and methods

# xpdl1_ImplementationType class attributes and methods

# xpdl1_BlockActivityType class attributes and methods
xpdl1_BlockActivityType_blockId: Property = Property(name="blockId", type=StringType)
xpdl1_BlockActivityType.attributes={xpdl1_BlockActivityType_blockId}

# xpdl1_StartModeType class attributes and methods

# xpdl1_FinishModeType class attributes and methods

# xpdl1_DeadlineType class attributes and methods
xpdl1_DeadlineType_execution: Property = Property(name="execution", type=StringType)
xpdl1_DeadlineType.attributes={xpdl1_DeadlineType_execution}

# xpdl1_SimulationInformationType class attributes and methods
xpdl1_SimulationInformationType_cost: Property = Property(name="cost", type=StringType)
xpdl1_SimulationInformationType_instantiation: Property = Property(name="instantiation", type=StringType)
xpdl1_SimulationInformationType.attributes={xpdl1_SimulationInformationType_instantiation, xpdl1_SimulationInformationType_cost}

# xpdl1_TransitionRestrictionsType class attributes and methods

# xpdl1_ExtendedAttributesType class attributes and methods

# xpdl1_ActualParametersType class attributes and methods
xpdl1_ActualParametersType_actualParameter: Property = Property(name="actualParameter", type=StringType)
xpdl1_ActualParametersType.attributes={xpdl1_ActualParametersType_actualParameter}

# xpdl1_ApplicationsType class attributes and methods

# xpdl1_ApplicationType class attributes and methods
xpdl1_ApplicationType_description: Property = Property(name="description", type=StringType)
xpdl1_ApplicationType_id: Property = Property(name="id", type=StringType)
xpdl1_ApplicationType_name: Property = Property(name="name", type=StringType)
xpdl1_ApplicationType.attributes={xpdl1_ApplicationType_description, xpdl1_ApplicationType_name, xpdl1_ApplicationType_id}

# xpdl1_FormalParametersType class attributes and methods

# xpdl1_ExternalReferenceType class attributes and methods
xpdl1_ExternalReferenceType_location: Property = Property(name="location", type=StringType)
xpdl1_ExternalReferenceType_namespace: Property = Property(name="namespace", type=StringType)
xpdl1_ExternalReferenceType_xref: Property = Property(name="xref", type=StringType)
xpdl1_ExternalReferenceType.attributes={xpdl1_ExternalReferenceType_namespace, xpdl1_ExternalReferenceType_location, xpdl1_ExternalReferenceType_xref}

# xpdl1_ArrayTypeType class attributes and methods
xpdl1_ArrayTypeType_upperIndex: Property = Property(name="upperIndex", type=StringType)
xpdl1_ArrayTypeType_lowerIndex: Property = Property(name="lowerIndex", type=StringType)
xpdl1_ArrayTypeType.attributes={xpdl1_ArrayTypeType_lowerIndex, xpdl1_ArrayTypeType_upperIndex}

# xpdl1_BasicTypeType class attributes and methods
xpdl1_BasicTypeType_type: Property = Property(name="type", type=StringType)
xpdl1_BasicTypeType.attributes={xpdl1_BasicTypeType_type}

# xpdl1_DeclaredTypeType class attributes and methods
xpdl1_DeclaredTypeType_id: Property = Property(name="id", type=StringType)
xpdl1_DeclaredTypeType.attributes={xpdl1_DeclaredTypeType_id}

# xpdl1_SchemaTypeType class attributes and methods
xpdl1_SchemaTypeType_any: Property = Property(name="any", type=StringType)
xpdl1_SchemaTypeType.attributes={xpdl1_SchemaTypeType_any}

# xpdl1_RecordTypeType class attributes and methods

# xpdl1_UnionTypeType class attributes and methods

# xpdl1_EnumerationTypeType class attributes and methods

# xpdl1_ListTypeType class attributes and methods

# xpdl1_AutomaticType class attributes and methods

# xpdl1_ConditionType class attributes and methods
xpdl1_ConditionType_mixed: Property = Property(name="mixed", type=StringType)
xpdl1_ConditionType_group: Property = Property(name="group", type=StringType)
xpdl1_ConditionType_type: Property = Property(name="type", type=StringType)
xpdl1_ConditionType.attributes={xpdl1_ConditionType_mixed, xpdl1_ConditionType_group, xpdl1_ConditionType_type}

# xpdl1_XpressionType class attributes and methods
xpdl1_XpressionType_mixed: Property = Property(name="mixed", type=StringType)
xpdl1_XpressionType_group: Property = Property(name="group", type=StringType)
xpdl1_XpressionType_any: Property = Property(name="any", type=StringType)
xpdl1_XpressionType.attributes={xpdl1_XpressionType_group, xpdl1_XpressionType_mixed, xpdl1_XpressionType_any}

# xpdl1_ConformanceClassType class attributes and methods
xpdl1_ConformanceClassType_graphConformance: Property = Property(name="graphConformance", type=StringType)
xpdl1_ConformanceClassType.attributes={xpdl1_ConformanceClassType_graphConformance}

# xpdl1_DataFieldsType class attributes and methods

# xpdl1_DataFieldType class attributes and methods
xpdl1_DataFieldType_initialValue: Property = Property(name="initialValue", type=StringType)
xpdl1_DataFieldType_length: Property = Property(name="length", type=StringType)
xpdl1_DataFieldType_description: Property = Property(name="description", type=StringType)
xpdl1_DataFieldType_id: Property = Property(name="id", type=StringType)
xpdl1_DataFieldType_isArray: Property = Property(name="isArray", type=StringType)
xpdl1_DataFieldType_name: Property = Property(name="name", type=StringType)
xpdl1_DataFieldType.attributes={xpdl1_DataFieldType_id, xpdl1_DataFieldType_description, xpdl1_DataFieldType_isArray, xpdl1_DataFieldType_initialValue, xpdl1_DataFieldType_length, xpdl1_DataFieldType_name}

# xpdl1_DataTypeType class attributes and methods

# xpdl1_EObject class attributes and methods

# xpdl1_DocumentRoot class attributes and methods
xpdl1_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
xpdl1_DocumentRoot_actualParameter: Property = Property(name="actualParameter", type=StringType)
xpdl1_DocumentRoot_author: Property = Property(name="author", type=StringType)
xpdl1_DocumentRoot_codepage: Property = Property(name="codepage", type=StringType)
xpdl1_DocumentRoot_cost: Property = Property(name="cost", type=StringType)
xpdl1_DocumentRoot_costUnit: Property = Property(name="costUnit", type=StringType)
xpdl1_DocumentRoot_countrykey: Property = Property(name="countrykey", type=StringType)
xpdl1_DocumentRoot_created: Property = Property(name="created", type=StringType)
xpdl1_DocumentRoot_description: Property = Property(name="description", type=StringType)
xpdl1_DocumentRoot_documentation: Property = Property(name="documentation", type=StringType)
xpdl1_DocumentRoot_duration: Property = Property(name="duration", type=StringType)
xpdl1_DocumentRoot_icon: Property = Property(name="icon", type=StringType)
xpdl1_DocumentRoot_initialValue: Property = Property(name="initialValue", type=StringType)
xpdl1_DocumentRoot_length: Property = Property(name="length", type=StringType)
xpdl1_DocumentRoot_limit: Property = Property(name="limit", type=StringType)
xpdl1_DocumentRoot_performer: Property = Property(name="performer", type=StringType)
xpdl1_DocumentRoot_priority: Property = Property(name="priority", type=StringType)
xpdl1_DocumentRoot_priorityUnit: Property = Property(name="priorityUnit", type=StringType)
xpdl1_DocumentRoot_responsible: Property = Property(name="responsible", type=StringType)
xpdl1_DocumentRoot_validFrom: Property = Property(name="validFrom", type=StringType)
xpdl1_DocumentRoot_validTo: Property = Property(name="validTo", type=StringType)
xpdl1_DocumentRoot_version: Property = Property(name="version", type=StringType)
xpdl1_DocumentRoot_waitingTime: Property = Property(name="waitingTime", type=StringType)
xpdl1_DocumentRoot_workingTime: Property = Property(name="workingTime", type=StringType)
xpdl1_DocumentRoot_xPDLVersion: Property = Property(name="xPDLVersion", type=StringType)
xpdl1_DocumentRoot_vendor: Property = Property(name="vendor", type=StringType)
xpdl1_DocumentRoot.attributes={xpdl1_DocumentRoot_actualParameter, xpdl1_DocumentRoot_costUnit, xpdl1_DocumentRoot_validTo, xpdl1_DocumentRoot_mixed, xpdl1_DocumentRoot_duration, xpdl1_DocumentRoot_countrykey, xpdl1_DocumentRoot_initialValue, xpdl1_DocumentRoot_responsible, xpdl1_DocumentRoot_vendor, xpdl1_DocumentRoot_waitingTime, xpdl1_DocumentRoot_icon, xpdl1_DocumentRoot_validFrom, xpdl1_DocumentRoot_priority, xpdl1_DocumentRoot_workingTime, xpdl1_DocumentRoot_cost, xpdl1_DocumentRoot_length, xpdl1_DocumentRoot_xPDLVersion, xpdl1_DocumentRoot_limit, xpdl1_DocumentRoot_performer, xpdl1_DocumentRoot_priorityUnit, xpdl1_DocumentRoot_documentation, xpdl1_DocumentRoot_description, xpdl1_DocumentRoot_version, xpdl1_DocumentRoot_created, xpdl1_DocumentRoot_codepage, xpdl1_DocumentRoot_author}

# xpdl1_EStringToStringMapEntry class attributes and methods

# xpdl1_ExternalPackagesType class attributes and methods

# xpdl1_EnumerationValueType class attributes and methods
xpdl1_EnumerationValueType_name: Property = Property(name="name", type=StringType)
xpdl1_EnumerationValueType.attributes={xpdl1_EnumerationValueType_name}

# xpdl1_ExtendedAttributeType class attributes and methods
xpdl1_ExtendedAttributeType_group: Property = Property(name="group", type=StringType)
xpdl1_ExtendedAttributeType_any: Property = Property(name="any", type=StringType)
xpdl1_ExtendedAttributeType_name: Property = Property(name="name", type=StringType)
xpdl1_ExtendedAttributeType_value: Property = Property(name="value", type=StringType)
xpdl1_ExtendedAttributeType_mixed: Property = Property(name="mixed", type=StringType)
xpdl1_ExtendedAttributeType.attributes={xpdl1_ExtendedAttributeType_group, xpdl1_ExtendedAttributeType_mixed, xpdl1_ExtendedAttributeType_name, xpdl1_ExtendedAttributeType_value, xpdl1_ExtendedAttributeType_any}

# xpdl1_ExternalPackageType class attributes and methods
xpdl1_ExternalPackageType_href: Property = Property(name="href", type=StringType)
xpdl1_ExternalPackageType.attributes={xpdl1_ExternalPackageType_href}

# xpdl1_FormalParameterType class attributes and methods
xpdl1_FormalParameterType_description: Property = Property(name="description", type=StringType)
xpdl1_FormalParameterType_id: Property = Property(name="id", type=StringType)
xpdl1_FormalParameterType_index: Property = Property(name="index", type=StringType)
xpdl1_FormalParameterType_mode: Property = Property(name="mode", type=StringType)
xpdl1_FormalParameterType.attributes={xpdl1_FormalParameterType_index, xpdl1_FormalParameterType_mode, xpdl1_FormalParameterType_description, xpdl1_FormalParameterType_id}

# xpdl1_JoinType class attributes and methods
xpdl1_JoinType_type: Property = Property(name="type", type=StringType)
xpdl1_JoinType.attributes={xpdl1_JoinType_type}

# xpdl1_PackageHeaderType class attributes and methods
xpdl1_PackageHeaderType_vendor: Property = Property(name="vendor", type=StringType)
xpdl1_PackageHeaderType_created: Property = Property(name="created", type=StringType)
xpdl1_PackageHeaderType_description: Property = Property(name="description", type=StringType)
xpdl1_PackageHeaderType_documentation: Property = Property(name="documentation", type=StringType)
xpdl1_PackageHeaderType_priorityUnit: Property = Property(name="priorityUnit", type=StringType)
xpdl1_PackageHeaderType_costUnit: Property = Property(name="costUnit", type=StringType)
xpdl1_PackageHeaderType_xPDLVersion: Property = Property(name="xPDLVersion", type=StringType)
xpdl1_PackageHeaderType.attributes={xpdl1_PackageHeaderType_created, xpdl1_PackageHeaderType_xPDLVersion, xpdl1_PackageHeaderType_description, xpdl1_PackageHeaderType_vendor, xpdl1_PackageHeaderType_documentation, xpdl1_PackageHeaderType_priorityUnit, xpdl1_PackageHeaderType_costUnit}

# xpdl1_ParticipantType class attributes and methods
xpdl1_ParticipantType_description: Property = Property(name="description", type=StringType)
xpdl1_ParticipantType_id: Property = Property(name="id", type=StringType)
xpdl1_ParticipantType_name: Property = Property(name="name", type=StringType)
xpdl1_ParticipantType.attributes={xpdl1_ParticipantType_id, xpdl1_ParticipantType_name, xpdl1_ParticipantType_description}

# xpdl1_ManualType class attributes and methods

# xpdl1_MemberType class attributes and methods

# xpdl1_NoType class attributes and methods

# xpdl1_PackageType class attributes and methods
xpdl1_PackageType_id: Property = Property(name="id", type=StringType)
xpdl1_PackageType_name: Property = Property(name="name", type=StringType)
xpdl1_PackageType.attributes={xpdl1_PackageType_id, xpdl1_PackageType_name}

# xpdl1_ParticipantsType class attributes and methods

# xpdl1_ProcessHeaderType class attributes and methods
xpdl1_ProcessHeaderType_description: Property = Property(name="description", type=StringType)
xpdl1_ProcessHeaderType_priority: Property = Property(name="priority", type=StringType)
xpdl1_ProcessHeaderType_limit: Property = Property(name="limit", type=StringType)
xpdl1_ProcessHeaderType_validFrom: Property = Property(name="validFrom", type=StringType)
xpdl1_ProcessHeaderType_validTo: Property = Property(name="validTo", type=StringType)
xpdl1_ProcessHeaderType_durationUnit: Property = Property(name="durationUnit", type=StringType)
xpdl1_ProcessHeaderType_created: Property = Property(name="created", type=StringType)
xpdl1_ProcessHeaderType.attributes={xpdl1_ProcessHeaderType_priority, xpdl1_ProcessHeaderType_validFrom, xpdl1_ProcessHeaderType_validTo, xpdl1_ProcessHeaderType_durationUnit, xpdl1_ProcessHeaderType_created, xpdl1_ProcessHeaderType_description, xpdl1_ProcessHeaderType_limit}

# xpdl1_RedefinableHeaderType class attributes and methods
xpdl1_RedefinableHeaderType_version: Property = Property(name="version", type=StringType)
xpdl1_RedefinableHeaderType_codepage: Property = Property(name="codepage", type=StringType)
xpdl1_RedefinableHeaderType_countrykey: Property = Property(name="countrykey", type=StringType)
xpdl1_RedefinableHeaderType_publicationStatus: Property = Property(name="publicationStatus", type=StringType)
xpdl1_RedefinableHeaderType_author: Property = Property(name="author", type=StringType)
xpdl1_RedefinableHeaderType.attributes={xpdl1_RedefinableHeaderType_countrykey, xpdl1_RedefinableHeaderType_codepage, xpdl1_RedefinableHeaderType_version, xpdl1_RedefinableHeaderType_author, xpdl1_RedefinableHeaderType_publicationStatus}

# xpdl1_ParticipantTypeType class attributes and methods
xpdl1_ParticipantTypeType_type: Property = Property(name="type", type=StringType)
xpdl1_ParticipantTypeType.attributes={xpdl1_ParticipantTypeType_type}

# xpdl1_ResponsiblesType class attributes and methods
xpdl1_ResponsiblesType_responsible: Property = Property(name="responsible", type=StringType)
xpdl1_ResponsiblesType.attributes={xpdl1_ResponsiblesType_responsible}

# xpdl1_ScriptType class attributes and methods
xpdl1_ScriptType_grammar: Property = Property(name="grammar", type=StringType)
xpdl1_ScriptType_type: Property = Property(name="type", type=StringType)
xpdl1_ScriptType_version: Property = Property(name="version", type=StringType)
xpdl1_ScriptType.attributes={xpdl1_ScriptType_version, xpdl1_ScriptType_type, xpdl1_ScriptType_grammar}

# xpdl1_SplitType class attributes and methods
xpdl1_SplitType_type: Property = Property(name="type", type=StringType)
xpdl1_SplitType.attributes={xpdl1_SplitType_type}

# xpdl1_SubFlowType class attributes and methods
xpdl1_SubFlowType_execution: Property = Property(name="execution", type=StringType)
xpdl1_SubFlowType_id: Property = Property(name="id", type=StringType)
xpdl1_SubFlowType.attributes={xpdl1_SubFlowType_id, xpdl1_SubFlowType_execution}

# xpdl1_TimeEstimationType class attributes and methods
xpdl1_TimeEstimationType_waitingTime: Property = Property(name="waitingTime", type=StringType)
xpdl1_TimeEstimationType_workingTime: Property = Property(name="workingTime", type=StringType)
xpdl1_TimeEstimationType_duration: Property = Property(name="duration", type=StringType)
xpdl1_TimeEstimationType.attributes={xpdl1_TimeEstimationType_duration, xpdl1_TimeEstimationType_waitingTime, xpdl1_TimeEstimationType_workingTime}

# xpdl1_ToolType class attributes and methods
xpdl1_ToolType_description: Property = Property(name="description", type=StringType)
xpdl1_ToolType_id: Property = Property(name="id", type=StringType)
xpdl1_ToolType_type: Property = Property(name="type", type=StringType)
xpdl1_ToolType.attributes={xpdl1_ToolType_id, xpdl1_ToolType_type, xpdl1_ToolType_description}

# xpdl1_TransitionType class attributes and methods
xpdl1_TransitionType_description: Property = Property(name="description", type=StringType)
xpdl1_TransitionType_from: Property = Property(name="from", type=StringType)
xpdl1_TransitionType_id: Property = Property(name="id", type=StringType)
xpdl1_TransitionType_name: Property = Property(name="name", type=StringType)
xpdl1_TransitionType_to: Property = Property(name="to", type=StringType)
xpdl1_TransitionType.attributes={xpdl1_TransitionType_from, xpdl1_TransitionType_id, xpdl1_TransitionType_to, xpdl1_TransitionType_description, xpdl1_TransitionType_name}

# xpdl1_TransitionRefType class attributes and methods
xpdl1_TransitionRefType_id: Property = Property(name="id", type=StringType)
xpdl1_TransitionRefType.attributes={xpdl1_TransitionRefType_id}

# xpdl1_TransitionRefsType class attributes and methods

# xpdl1_TypeDeclarationType class attributes and methods
xpdl1_TypeDeclarationType_description: Property = Property(name="description", type=StringType)
xpdl1_TypeDeclarationType_id: Property = Property(name="id", type=StringType)
xpdl1_TypeDeclarationType_name: Property = Property(name="name", type=StringType)
xpdl1_TypeDeclarationType.attributes={xpdl1_TypeDeclarationType_id, xpdl1_TypeDeclarationType_name, xpdl1_TypeDeclarationType_description}

# xpdl1_TypeDeclarationsType class attributes and methods

# xpdl1_TransitionRestrictionType class attributes and methods

# xpdl1_WorkflowProcessType class attributes and methods
xpdl1_WorkflowProcessType_accessLevel: Property = Property(name="accessLevel", type=StringType)
xpdl1_WorkflowProcessType_id: Property = Property(name="id", type=StringType)
xpdl1_WorkflowProcessType_name: Property = Property(name="name", type=StringType)
xpdl1_WorkflowProcessType.attributes={xpdl1_WorkflowProcessType_accessLevel, xpdl1_WorkflowProcessType_id, xpdl1_WorkflowProcessType_name}

# xpdl1_WorkflowProcessesType class attributes and methods

# Relationships
activity0: BinaryAssociation = BinaryAssociation(
    name="activity0",
    ends={
        Property(name="xpdl1_ActivityType", type=xpdl1_ActivitiesType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ActivitiesType", type=xpdl1_ActivityType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitySet1: BinaryAssociation = BinaryAssociation(
    name="activitySet1",
    ends={
        Property(name="xpdl1_ActivitySetType", type=xpdl1_ActivitySetsType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ActivitySetsType", type=xpdl1_ActivitySetType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activities2: BinaryAssociation = BinaryAssociation(
    name="activities2",
    ends={
        Property(name="xpdl1_ActivitiesType4", type=xpdl1_ActivitySetType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ActivitySetType3", type=xpdl1_ActivitiesType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transitions5: BinaryAssociation = BinaryAssociation(
    name="transitions5",
    ends={
        Property(name="xpdl1_TransitionsType", type=xpdl1_ActivitySetType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ActivitySetType6", type=xpdl1_TransitionsType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
route7: BinaryAssociation = BinaryAssociation(
    name="route7",
    ends={
        Property(name="xpdl1_RouteType", type=xpdl1_ActivityType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ActivityType8", type=xpdl1_RouteType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
implementation9: BinaryAssociation = BinaryAssociation(
    name="implementation9",
    ends={
        Property(name="xpdl1_ImplementationType", type=xpdl1_ActivityType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ActivityType10", type=xpdl1_ImplementationType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
blockActivity11: BinaryAssociation = BinaryAssociation(
    name="blockActivity11",
    ends={
        Property(name="xpdl1_BlockActivityType", type=xpdl1_ActivityType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ActivityType12", type=xpdl1_BlockActivityType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
startMode13: BinaryAssociation = BinaryAssociation(
    name="startMode13",
    ends={
        Property(name="xpdl1_StartModeType", type=xpdl1_ActivityType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ActivityType14", type=xpdl1_StartModeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finishMode15: BinaryAssociation = BinaryAssociation(
    name="finishMode15",
    ends={
        Property(name="xpdl1_FinishModeType", type=xpdl1_ActivityType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ActivityType16", type=xpdl1_FinishModeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
deadline17: BinaryAssociation = BinaryAssociation(
    name="deadline17",
    ends={
        Property(name="xpdl1_DeadlineType", type=xpdl1_ActivityType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ActivityType18", type=xpdl1_DeadlineType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
simulationInformation19: BinaryAssociation = BinaryAssociation(
    name="simulationInformation19",
    ends={
        Property(name="xpdl1_SimulationInformationType", type=xpdl1_ActivityType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ActivityType20", type=xpdl1_SimulationInformationType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transitionRestrictions21: BinaryAssociation = BinaryAssociation(
    name="transitionRestrictions21",
    ends={
        Property(name="xpdl1_TransitionRestrictionsType", type=xpdl1_ActivityType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ActivityType22", type=xpdl1_TransitionRestrictionsType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extendedAttributes23: BinaryAssociation = BinaryAssociation(
    name="extendedAttributes23",
    ends={
        Property(name="xpdl1_ExtendedAttributesType", type=xpdl1_ActivityType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ActivityType24", type=xpdl1_ExtendedAttributesType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
application25: BinaryAssociation = BinaryAssociation(
    name="application25",
    ends={
        Property(name="xpdl1_ApplicationType", type=xpdl1_ApplicationsType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ApplicationsType", type=xpdl1_ApplicationType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
recordType41: BinaryAssociation = BinaryAssociation(
    name="recordType41",
    ends={
        Property(name="xpdl1_RecordTypeType", type=xpdl1_ArrayTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ArrayTypeType42", type=xpdl1_RecordTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters26: BinaryAssociation = BinaryAssociation(
    name="formalParameters26",
    ends={
        Property(name="xpdl1_FormalParametersType", type=xpdl1_ApplicationType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ApplicationType27", type=xpdl1_FormalParametersType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
externalReference28: BinaryAssociation = BinaryAssociation(
    name="externalReference28",
    ends={
        Property(name="xpdl1_ExternalReferenceType", type=xpdl1_ApplicationType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ApplicationType29", type=xpdl1_ExternalReferenceType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extendedAttributes30: BinaryAssociation = BinaryAssociation(
    name="extendedAttributes30",
    ends={
        Property(name="xpdl1_ExtendedAttributesType32", type=xpdl1_ApplicationType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ApplicationType31", type=xpdl1_ExtendedAttributesType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basicType33: BinaryAssociation = BinaryAssociation(
    name="basicType33",
    ends={
        Property(name="xpdl1_BasicTypeType", type=xpdl1_ArrayTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ArrayTypeType", type=xpdl1_BasicTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaredType34: BinaryAssociation = BinaryAssociation(
    name="declaredType34",
    ends={
        Property(name="xpdl1_DeclaredTypeType", type=xpdl1_ArrayTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ArrayTypeType35", type=xpdl1_DeclaredTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schemaType36: BinaryAssociation = BinaryAssociation(
    name="schemaType36",
    ends={
        Property(name="xpdl1_SchemaTypeType", type=xpdl1_ArrayTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ArrayTypeType37", type=xpdl1_SchemaTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
externalReference38: BinaryAssociation = BinaryAssociation(
    name="externalReference38",
    ends={
        Property(name="xpdl1_ExternalReferenceType40", type=xpdl1_ArrayTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ArrayTypeType39", type=xpdl1_ExternalReferenceType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unionType43: BinaryAssociation = BinaryAssociation(
    name="unionType43",
    ends={
        Property(name="xpdl1_UnionTypeType", type=xpdl1_ArrayTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ArrayTypeType44", type=xpdl1_UnionTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumerationType45: BinaryAssociation = BinaryAssociation(
    name="enumerationType45",
    ends={
        Property(name="xpdl1_EnumerationTypeType", type=xpdl1_ArrayTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ArrayTypeType46", type=xpdl1_EnumerationTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrayType48: BinaryAssociation = BinaryAssociation(
    name="arrayType48",
    ends={
        Property(name="xpdl1_ArrayTypeType49", type=xpdl1_ArrayTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ArrayTypeType47", type=xpdl1_ArrayTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
listType50: BinaryAssociation = BinaryAssociation(
    name="listType50",
    ends={
        Property(name="xpdl1_ListTypeType", type=xpdl1_ArrayTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ArrayTypeType51", type=xpdl1_ListTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
xpression52: BinaryAssociation = BinaryAssociation(
    name="xpression52",
    ends={
        Property(name="xpdl1_XpressionType", type=xpdl1_ConditionType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ConditionType", type=xpdl1_XpressionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataField53: BinaryAssociation = BinaryAssociation(
    name="dataField53",
    ends={
        Property(name="xpdl1_DataFieldType", type=xpdl1_DataFieldsType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DataFieldsType", type=xpdl1_DataFieldType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataType54: BinaryAssociation = BinaryAssociation(
    name="dataType54",
    ends={
        Property(name="xpdl1_DataTypeType", type=xpdl1_DataFieldType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DataFieldType55", type=xpdl1_DataTypeType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extendedAttributes56: BinaryAssociation = BinaryAssociation(
    name="extendedAttributes56",
    ends={
        Property(name="xpdl1_ExtendedAttributesType58", type=xpdl1_DataFieldType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DataFieldType57", type=xpdl1_ExtendedAttributesType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basicType59: BinaryAssociation = BinaryAssociation(
    name="basicType59",
    ends={
        Property(name="xpdl1_BasicTypeType61", type=xpdl1_DataTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DataTypeType60", type=xpdl1_BasicTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaredType62: BinaryAssociation = BinaryAssociation(
    name="declaredType62",
    ends={
        Property(name="xpdl1_DeclaredTypeType64", type=xpdl1_DataTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DataTypeType63", type=xpdl1_DeclaredTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schemaType65: BinaryAssociation = BinaryAssociation(
    name="schemaType65",
    ends={
        Property(name="xpdl1_SchemaTypeType67", type=xpdl1_DataTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DataTypeType66", type=xpdl1_SchemaTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
externalReference68: BinaryAssociation = BinaryAssociation(
    name="externalReference68",
    ends={
        Property(name="xpdl1_ExternalReferenceType70", type=xpdl1_DataTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DataTypeType69", type=xpdl1_ExternalReferenceType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
recordType71: BinaryAssociation = BinaryAssociation(
    name="recordType71",
    ends={
        Property(name="xpdl1_RecordTypeType73", type=xpdl1_DataTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DataTypeType72", type=xpdl1_RecordTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unionType74: BinaryAssociation = BinaryAssociation(
    name="unionType74",
    ends={
        Property(name="xpdl1_UnionTypeType76", type=xpdl1_DataTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DataTypeType75", type=xpdl1_UnionTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumerationType77: BinaryAssociation = BinaryAssociation(
    name="enumerationType77",
    ends={
        Property(name="xpdl1_EnumerationTypeType79", type=xpdl1_DataTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DataTypeType78", type=xpdl1_EnumerationTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrayType80: BinaryAssociation = BinaryAssociation(
    name="arrayType80",
    ends={
        Property(name="xpdl1_ArrayTypeType82", type=xpdl1_DataTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DataTypeType81", type=xpdl1_ArrayTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
listType83: BinaryAssociation = BinaryAssociation(
    name="listType83",
    ends={
        Property(name="xpdl1_ListTypeType85", type=xpdl1_DataTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DataTypeType84", type=xpdl1_ListTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
deadlineCondition86: BinaryAssociation = BinaryAssociation(
    name="deadlineCondition86",
    ends={
        Property(name="xpdl1_EObject", type=xpdl1_DeadlineType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DeadlineType87", type=xpdl1_EObject, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exceptionName88: BinaryAssociation = BinaryAssociation(
    name="exceptionName88",
    ends={
        Property(name="xpdl1_EObject90", type=xpdl1_DeadlineType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DeadlineType89", type=xpdl1_EObject, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
xMLNSPrefixMap91: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap91",
    ends={
        Property(name="xpdl1_EStringToStringMapEntry", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot", type=xpdl1_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation92: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation92",
    ends={
        Property(name="xpdl1_EStringToStringMapEntry94", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot93", type=xpdl1_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activities95: BinaryAssociation = BinaryAssociation(
    name="activities95",
    ends={
        Property(name="xpdl1_ActivitiesType97", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot96", type=xpdl1_ActivitiesType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activity98: BinaryAssociation = BinaryAssociation(
    name="activity98",
    ends={
        Property(name="xpdl1_ActivityType100", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot99", type=xpdl1_ActivityType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitySet101: BinaryAssociation = BinaryAssociation(
    name="activitySet101",
    ends={
        Property(name="xpdl1_ActivitySetType103", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot102", type=xpdl1_ActivitySetType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitySets104: BinaryAssociation = BinaryAssociation(
    name="activitySets104",
    ends={
        Property(name="xpdl1_ActivitySetsType106", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot105", type=xpdl1_ActivitySetsType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actualParameters107: BinaryAssociation = BinaryAssociation(
    name="actualParameters107",
    ends={
        Property(name="xpdl1_ActualParametersType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot108", type=xpdl1_ActualParametersType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
application109: BinaryAssociation = BinaryAssociation(
    name="application109",
    ends={
        Property(name="xpdl1_ApplicationType111", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot110", type=xpdl1_ApplicationType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
applications112: BinaryAssociation = BinaryAssociation(
    name="applications112",
    ends={
        Property(name="xpdl1_ApplicationsType114", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot113", type=xpdl1_ApplicationsType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arrayType115: BinaryAssociation = BinaryAssociation(
    name="arrayType115",
    ends={
        Property(name="xpdl1_ArrayTypeType117", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot116", type=xpdl1_ArrayTypeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
automatic118: BinaryAssociation = BinaryAssociation(
    name="automatic118",
    ends={
        Property(name="xpdl1_AutomaticType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot119", type=xpdl1_AutomaticType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basicType120: BinaryAssociation = BinaryAssociation(
    name="basicType120",
    ends={
        Property(name="xpdl1_BasicTypeType122", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot121", type=xpdl1_BasicTypeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blockActivity123: BinaryAssociation = BinaryAssociation(
    name="blockActivity123",
    ends={
        Property(name="xpdl1_BlockActivityType125", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot124", type=xpdl1_BlockActivityType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition126: BinaryAssociation = BinaryAssociation(
    name="condition126",
    ends={
        Property(name="xpdl1_ConditionType128", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot127", type=xpdl1_ConditionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conformanceClass129: BinaryAssociation = BinaryAssociation(
    name="conformanceClass129",
    ends={
        Property(name="xpdl1_ConformanceClassType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot130", type=xpdl1_ConformanceClassType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataField131: BinaryAssociation = BinaryAssociation(
    name="dataField131",
    ends={
        Property(name="xpdl1_DataFieldType133", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot132", type=xpdl1_DataFieldType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataFields134: BinaryAssociation = BinaryAssociation(
    name="dataFields134",
    ends={
        Property(name="xpdl1_DataFieldsType136", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot135", type=xpdl1_DataFieldsType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataType137: BinaryAssociation = BinaryAssociation(
    name="dataType137",
    ends={
        Property(name="xpdl1_DataTypeType139", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot138", type=xpdl1_DataTypeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deadline140: BinaryAssociation = BinaryAssociation(
    name="deadline140",
    ends={
        Property(name="xpdl1_DeadlineType142", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot141", type=xpdl1_DeadlineType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaredType143: BinaryAssociation = BinaryAssociation(
    name="declaredType143",
    ends={
        Property(name="xpdl1_DeclaredTypeType145", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot144", type=xpdl1_DeclaredTypeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumerationType146: BinaryAssociation = BinaryAssociation(
    name="enumerationType146",
    ends={
        Property(name="xpdl1_EnumerationTypeType148", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot147", type=xpdl1_EnumerationTypeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumerationValue149: BinaryAssociation = BinaryAssociation(
    name="enumerationValue149",
    ends={
        Property(name="xpdl1_EnumerationValueType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot150", type=xpdl1_EnumerationValueType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extendedAttribute151: BinaryAssociation = BinaryAssociation(
    name="extendedAttribute151",
    ends={
        Property(name="xpdl1_ExtendedAttributeType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot152", type=xpdl1_ExtendedAttributeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extendedAttributes153: BinaryAssociation = BinaryAssociation(
    name="extendedAttributes153",
    ends={
        Property(name="xpdl1_ExtendedAttributesType155", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot154", type=xpdl1_ExtendedAttributesType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externalPackage156: BinaryAssociation = BinaryAssociation(
    name="externalPackage156",
    ends={
        Property(name="xpdl1_ExternalPackageType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot157", type=xpdl1_ExternalPackageType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
join174: BinaryAssociation = BinaryAssociation(
    name="join174",
    ends={
        Property(name="xpdl1_JoinType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot175", type=xpdl1_JoinType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externalPackages158: BinaryAssociation = BinaryAssociation(
    name="externalPackages158",
    ends={
        Property(name="xpdl1_ExternalPackagesType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot159", type=xpdl1_ExternalPackagesType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externalReference160: BinaryAssociation = BinaryAssociation(
    name="externalReference160",
    ends={
        Property(name="xpdl1_ExternalReferenceType162", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot161", type=xpdl1_ExternalReferenceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
finishMode163: BinaryAssociation = BinaryAssociation(
    name="finishMode163",
    ends={
        Property(name="xpdl1_FinishModeType165", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot164", type=xpdl1_FinishModeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formalParameter166: BinaryAssociation = BinaryAssociation(
    name="formalParameter166",
    ends={
        Property(name="xpdl1_FormalParameterType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot167", type=xpdl1_FormalParameterType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formalParameters168: BinaryAssociation = BinaryAssociation(
    name="formalParameters168",
    ends={
        Property(name="xpdl1_FormalParametersType170", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot169", type=xpdl1_FormalParametersType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implementation171: BinaryAssociation = BinaryAssociation(
    name="implementation171",
    ends={
        Property(name="xpdl1_ImplementationType173", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot172", type=xpdl1_ImplementationType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageHeader187: BinaryAssociation = BinaryAssociation(
    name="packageHeader187",
    ends={
        Property(name="xpdl1_PackageHeaderType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot188", type=xpdl1_PackageHeaderType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listType176: BinaryAssociation = BinaryAssociation(
    name="listType176",
    ends={
        Property(name="xpdl1_ListTypeType178", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot177", type=xpdl1_ListTypeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
participant189: BinaryAssociation = BinaryAssociation(
    name="participant189",
    ends={
        Property(name="xpdl1_ParticipantType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot190", type=xpdl1_ParticipantType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
manual179: BinaryAssociation = BinaryAssociation(
    name="manual179",
    ends={
        Property(name="xpdl1_ManualType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot180", type=xpdl1_ManualType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
member181: BinaryAssociation = BinaryAssociation(
    name="member181",
    ends={
        Property(name="xpdl1_MemberType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot182", type=xpdl1_MemberType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
no183: BinaryAssociation = BinaryAssociation(
    name="no183",
    ends={
        Property(name="xpdl1_NoType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot184", type=xpdl1_NoType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package185: BinaryAssociation = BinaryAssociation(
    name="package185",
    ends={
        Property(name="xpdl1_PackageType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot186", type=xpdl1_PackageType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
participants191: BinaryAssociation = BinaryAssociation(
    name="participants191",
    ends={
        Property(name="xpdl1_ParticipantsType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot192", type=xpdl1_ParticipantsType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processHeader195: BinaryAssociation = BinaryAssociation(
    name="processHeader195",
    ends={
        Property(name="xpdl1_ProcessHeaderType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot196", type=xpdl1_ProcessHeaderType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
recordType197: BinaryAssociation = BinaryAssociation(
    name="recordType197",
    ends={
        Property(name="xpdl1_RecordTypeType199", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot198", type=xpdl1_RecordTypeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
redefinableHeader200: BinaryAssociation = BinaryAssociation(
    name="redefinableHeader200",
    ends={
        Property(name="xpdl1_RedefinableHeaderType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot201", type=xpdl1_RedefinableHeaderType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
participantType193: BinaryAssociation = BinaryAssociation(
    name="participantType193",
    ends={
        Property(name="xpdl1_ParticipantTypeType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot194", type=xpdl1_ParticipantTypeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
responsibles202: BinaryAssociation = BinaryAssociation(
    name="responsibles202",
    ends={
        Property(name="xpdl1_ResponsiblesType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot203", type=xpdl1_ResponsiblesType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
route204: BinaryAssociation = BinaryAssociation(
    name="route204",
    ends={
        Property(name="xpdl1_RouteType206", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot205", type=xpdl1_RouteType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schemaType207: BinaryAssociation = BinaryAssociation(
    name="schemaType207",
    ends={
        Property(name="xpdl1_SchemaTypeType209", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot208", type=xpdl1_SchemaTypeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script210: BinaryAssociation = BinaryAssociation(
    name="script210",
    ends={
        Property(name="xpdl1_ScriptType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot211", type=xpdl1_ScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
simulationInformation212: BinaryAssociation = BinaryAssociation(
    name="simulationInformation212",
    ends={
        Property(name="xpdl1_SimulationInformationType214", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot213", type=xpdl1_SimulationInformationType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
split215: BinaryAssociation = BinaryAssociation(
    name="split215",
    ends={
        Property(name="xpdl1_SplitType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot216", type=xpdl1_SplitType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subFlow220: BinaryAssociation = BinaryAssociation(
    name="subFlow220",
    ends={
        Property(name="xpdl1_SubFlowType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot221", type=xpdl1_SubFlowType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timeEstimation222: BinaryAssociation = BinaryAssociation(
    name="timeEstimation222",
    ends={
        Property(name="xpdl1_TimeEstimationType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot223", type=xpdl1_TimeEstimationType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tool224: BinaryAssociation = BinaryAssociation(
    name="tool224",
    ends={
        Property(name="xpdl1_ToolType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot225", type=xpdl1_ToolType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition226: BinaryAssociation = BinaryAssociation(
    name="transition226",
    ends={
        Property(name="xpdl1_TransitionType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot227", type=xpdl1_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitionRef228: BinaryAssociation = BinaryAssociation(
    name="transitionRef228",
    ends={
        Property(name="xpdl1_TransitionRefType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot229", type=xpdl1_TransitionRefType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitionRefs230: BinaryAssociation = BinaryAssociation(
    name="transitionRefs230",
    ends={
        Property(name="xpdl1_TransitionRefsType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot231", type=xpdl1_TransitionRefsType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
startMode217: BinaryAssociation = BinaryAssociation(
    name="startMode217",
    ends={
        Property(name="xpdl1_StartModeType219", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot218", type=xpdl1_StartModeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitionRestrictions234: BinaryAssociation = BinaryAssociation(
    name="transitionRestrictions234",
    ends={
        Property(name="xpdl1_TransitionRestrictionsType236", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot235", type=xpdl1_TransitionRestrictionsType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions237: BinaryAssociation = BinaryAssociation(
    name="transitions237",
    ends={
        Property(name="xpdl1_TransitionsType239", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot238", type=xpdl1_TransitionsType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeDeclaration240: BinaryAssociation = BinaryAssociation(
    name="typeDeclaration240",
    ends={
        Property(name="xpdl1_TypeDeclarationType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot241", type=xpdl1_TypeDeclarationType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeDeclarations242: BinaryAssociation = BinaryAssociation(
    name="typeDeclarations242",
    ends={
        Property(name="xpdl1_TypeDeclarationsType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot243", type=xpdl1_TypeDeclarationsType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unionType244: BinaryAssociation = BinaryAssociation(
    name="unionType244",
    ends={
        Property(name="xpdl1_UnionTypeType246", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot245", type=xpdl1_UnionTypeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitionRestriction232: BinaryAssociation = BinaryAssociation(
    name="transitionRestriction232",
    ends={
        Property(name="xpdl1_TransitionRestrictionType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot233", type=xpdl1_TransitionRestrictionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
workflowProcess247: BinaryAssociation = BinaryAssociation(
    name="workflowProcess247",
    ends={
        Property(name="xpdl1_WorkflowProcessType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot248", type=xpdl1_WorkflowProcessType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
workflowProcesses249: BinaryAssociation = BinaryAssociation(
    name="workflowProcesses249",
    ends={
        Property(name="xpdl1_WorkflowProcessesType", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot250", type=xpdl1_WorkflowProcessesType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xpression251: BinaryAssociation = BinaryAssociation(
    name="xpression251",
    ends={
        Property(name="xpdl1_XpressionType253", type=xpdl1_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_DocumentRoot252", type=xpdl1_XpressionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumerationValue254: BinaryAssociation = BinaryAssociation(
    name="enumerationValue254",
    ends={
        Property(name="xpdl1_EnumerationValueType256", type=xpdl1_EnumerationTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_EnumerationTypeType255", type=xpdl1_EnumerationValueType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
extendedAttribute257: BinaryAssociation = BinaryAssociation(
    name="extendedAttribute257",
    ends={
        Property(name="xpdl1_ExtendedAttributeType259", type=xpdl1_ExtendedAttributesType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ExtendedAttributesType258", type=xpdl1_ExtendedAttributeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externalPackage260: BinaryAssociation = BinaryAssociation(
    name="externalPackage260",
    ends={
        Property(name="xpdl1_ExternalPackageType262", type=xpdl1_ExternalPackagesType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ExternalPackagesType261", type=xpdl1_ExternalPackageType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extendedAttributes263: BinaryAssociation = BinaryAssociation(
    name="extendedAttributes263",
    ends={
        Property(name="xpdl1_ExtendedAttributesType265", type=xpdl1_ExternalPackageType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ExternalPackageType264", type=xpdl1_ExtendedAttributesType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
automatic266: BinaryAssociation = BinaryAssociation(
    name="automatic266",
    ends={
        Property(name="xpdl1_AutomaticType268", type=xpdl1_FinishModeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_FinishModeType267", type=xpdl1_AutomaticType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
manual269: BinaryAssociation = BinaryAssociation(
    name="manual269",
    ends={
        Property(name="xpdl1_ManualType271", type=xpdl1_FinishModeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_FinishModeType270", type=xpdl1_ManualType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameter272: BinaryAssociation = BinaryAssociation(
    name="formalParameter272",
    ends={
        Property(name="xpdl1_FormalParameterType274", type=xpdl1_FormalParametersType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_FormalParametersType273", type=xpdl1_FormalParameterType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataType275: BinaryAssociation = BinaryAssociation(
    name="dataType275",
    ends={
        Property(name="xpdl1_DataTypeType277", type=xpdl1_FormalParameterType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_FormalParameterType276", type=xpdl1_DataTypeType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tool281: BinaryAssociation = BinaryAssociation(
    name="tool281",
    ends={
        Property(name="xpdl1_ToolType283", type=xpdl1_ImplementationType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ImplementationType282", type=xpdl1_ToolType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subFlow284: BinaryAssociation = BinaryAssociation(
    name="subFlow284",
    ends={
        Property(name="xpdl1_SubFlowType286", type=xpdl1_ImplementationType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ImplementationType285", type=xpdl1_SubFlowType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basicType287: BinaryAssociation = BinaryAssociation(
    name="basicType287",
    ends={
        Property(name="xpdl1_BasicTypeType289", type=xpdl1_ListTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ListTypeType288", type=xpdl1_BasicTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaredType290: BinaryAssociation = BinaryAssociation(
    name="declaredType290",
    ends={
        Property(name="xpdl1_DeclaredTypeType292", type=xpdl1_ListTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ListTypeType291", type=xpdl1_DeclaredTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schemaType293: BinaryAssociation = BinaryAssociation(
    name="schemaType293",
    ends={
        Property(name="xpdl1_SchemaTypeType295", type=xpdl1_ListTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ListTypeType294", type=xpdl1_SchemaTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
no278: BinaryAssociation = BinaryAssociation(
    name="no278",
    ends={
        Property(name="xpdl1_NoType280", type=xpdl1_ImplementationType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ImplementationType279", type=xpdl1_NoType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
externalReference296: BinaryAssociation = BinaryAssociation(
    name="externalReference296",
    ends={
        Property(name="xpdl1_ExternalReferenceType298", type=xpdl1_ListTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ListTypeType297", type=xpdl1_ExternalReferenceType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
recordType299: BinaryAssociation = BinaryAssociation(
    name="recordType299",
    ends={
        Property(name="xpdl1_RecordTypeType301", type=xpdl1_ListTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ListTypeType300", type=xpdl1_RecordTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unionType302: BinaryAssociation = BinaryAssociation(
    name="unionType302",
    ends={
        Property(name="xpdl1_UnionTypeType304", type=xpdl1_ListTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ListTypeType303", type=xpdl1_UnionTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumerationType305: BinaryAssociation = BinaryAssociation(
    name="enumerationType305",
    ends={
        Property(name="xpdl1_EnumerationTypeType307", type=xpdl1_ListTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ListTypeType306", type=xpdl1_EnumerationTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrayType308: BinaryAssociation = BinaryAssociation(
    name="arrayType308",
    ends={
        Property(name="xpdl1_ArrayTypeType310", type=xpdl1_ListTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ListTypeType309", type=xpdl1_ArrayTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
listType312: BinaryAssociation = BinaryAssociation(
    name="listType312",
    ends={
        Property(name="xpdl1_ListTypeType313", type=xpdl1_ListTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ListTypeType311", type=xpdl1_ListTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basicType314: BinaryAssociation = BinaryAssociation(
    name="basicType314",
    ends={
        Property(name="xpdl1_BasicTypeType316", type=xpdl1_MemberType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_MemberType315", type=xpdl1_BasicTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaredType317: BinaryAssociation = BinaryAssociation(
    name="declaredType317",
    ends={
        Property(name="xpdl1_DeclaredTypeType319", type=xpdl1_MemberType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_MemberType318", type=xpdl1_DeclaredTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
externalReference323: BinaryAssociation = BinaryAssociation(
    name="externalReference323",
    ends={
        Property(name="xpdl1_ExternalReferenceType325", type=xpdl1_MemberType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_MemberType324", type=xpdl1_ExternalReferenceType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
recordType326: BinaryAssociation = BinaryAssociation(
    name="recordType326",
    ends={
        Property(name="xpdl1_RecordTypeType328", type=xpdl1_MemberType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_MemberType327", type=xpdl1_RecordTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unionType329: BinaryAssociation = BinaryAssociation(
    name="unionType329",
    ends={
        Property(name="xpdl1_UnionTypeType331", type=xpdl1_MemberType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_MemberType330", type=xpdl1_UnionTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumerationType332: BinaryAssociation = BinaryAssociation(
    name="enumerationType332",
    ends={
        Property(name="xpdl1_EnumerationTypeType334", type=xpdl1_MemberType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_MemberType333", type=xpdl1_EnumerationTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrayType335: BinaryAssociation = BinaryAssociation(
    name="arrayType335",
    ends={
        Property(name="xpdl1_ArrayTypeType337", type=xpdl1_MemberType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_MemberType336", type=xpdl1_ArrayTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
listType338: BinaryAssociation = BinaryAssociation(
    name="listType338",
    ends={
        Property(name="xpdl1_ListTypeType340", type=xpdl1_MemberType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_MemberType339", type=xpdl1_ListTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schemaType320: BinaryAssociation = BinaryAssociation(
    name="schemaType320",
    ends={
        Property(name="xpdl1_SchemaTypeType322", type=xpdl1_MemberType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_MemberType321", type=xpdl1_SchemaTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
packageHeader341: BinaryAssociation = BinaryAssociation(
    name="packageHeader341",
    ends={
        Property(name="xpdl1_PackageHeaderType343", type=xpdl1_PackageType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_PackageType342", type=xpdl1_PackageHeaderType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
redefinableHeader344: BinaryAssociation = BinaryAssociation(
    name="redefinableHeader344",
    ends={
        Property(name="xpdl1_RedefinableHeaderType346", type=xpdl1_PackageType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_PackageType345", type=xpdl1_RedefinableHeaderType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conformanceClass347: BinaryAssociation = BinaryAssociation(
    name="conformanceClass347",
    ends={
        Property(name="xpdl1_ConformanceClassType349", type=xpdl1_PackageType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_PackageType348", type=xpdl1_ConformanceClassType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
script350: BinaryAssociation = BinaryAssociation(
    name="script350",
    ends={
        Property(name="xpdl1_ScriptType352", type=xpdl1_PackageType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_PackageType351", type=xpdl1_ScriptType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
externalPackages353: BinaryAssociation = BinaryAssociation(
    name="externalPackages353",
    ends={
        Property(name="xpdl1_ExternalPackagesType355", type=xpdl1_PackageType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_PackageType354", type=xpdl1_ExternalPackagesType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeDeclarations356: BinaryAssociation = BinaryAssociation(
    name="typeDeclarations356",
    ends={
        Property(name="xpdl1_TypeDeclarationsType358", type=xpdl1_PackageType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_PackageType357", type=xpdl1_TypeDeclarationsType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
participants359: BinaryAssociation = BinaryAssociation(
    name="participants359",
    ends={
        Property(name="xpdl1_ParticipantsType361", type=xpdl1_PackageType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_PackageType360", type=xpdl1_ParticipantsType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
applications362: BinaryAssociation = BinaryAssociation(
    name="applications362",
    ends={
        Property(name="xpdl1_ApplicationsType364", type=xpdl1_PackageType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_PackageType363", type=xpdl1_ApplicationsType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dataFields365: BinaryAssociation = BinaryAssociation(
    name="dataFields365",
    ends={
        Property(name="xpdl1_DataFieldsType367", type=xpdl1_PackageType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_PackageType366", type=xpdl1_DataFieldsType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
workflowProcesses368: BinaryAssociation = BinaryAssociation(
    name="workflowProcesses368",
    ends={
        Property(name="xpdl1_WorkflowProcessesType370", type=xpdl1_PackageType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_PackageType369", type=xpdl1_WorkflowProcessesType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extendedAttributes371: BinaryAssociation = BinaryAssociation(
    name="extendedAttributes371",
    ends={
        Property(name="xpdl1_ExtendedAttributesType373", type=xpdl1_PackageType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_PackageType372", type=xpdl1_ExtendedAttributesType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
participant374: BinaryAssociation = BinaryAssociation(
    name="participant374",
    ends={
        Property(name="xpdl1_ParticipantType376", type=xpdl1_ParticipantsType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ParticipantsType375", type=xpdl1_ParticipantType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
participantType377: BinaryAssociation = BinaryAssociation(
    name="participantType377",
    ends={
        Property(name="xpdl1_ParticipantTypeType379", type=xpdl1_ParticipantType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ParticipantType378", type=xpdl1_ParticipantTypeType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
externalReference380: BinaryAssociation = BinaryAssociation(
    name="externalReference380",
    ends={
        Property(name="xpdl1_ExternalReferenceType382", type=xpdl1_ParticipantType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ParticipantType381", type=xpdl1_ExternalReferenceType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extendedAttributes383: BinaryAssociation = BinaryAssociation(
    name="extendedAttributes383",
    ends={
        Property(name="xpdl1_ExtendedAttributesType385", type=xpdl1_ParticipantType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ParticipantType384", type=xpdl1_ExtendedAttributesType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeEstimation386: BinaryAssociation = BinaryAssociation(
    name="timeEstimation386",
    ends={
        Property(name="xpdl1_TimeEstimationType388", type=xpdl1_ProcessHeaderType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ProcessHeaderType387", type=xpdl1_TimeEstimationType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
member389: BinaryAssociation = BinaryAssociation(
    name="member389",
    ends={
        Property(name="xpdl1_MemberType391", type=xpdl1_RecordTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_RecordTypeType390", type=xpdl1_MemberType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
responsibles392: BinaryAssociation = BinaryAssociation(
    name="responsibles392",
    ends={
        Property(name="xpdl1_ResponsiblesType394", type=xpdl1_RedefinableHeaderType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_RedefinableHeaderType393", type=xpdl1_ResponsiblesType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeEstimation395: BinaryAssociation = BinaryAssociation(
    name="timeEstimation395",
    ends={
        Property(name="xpdl1_TimeEstimationType397", type=xpdl1_SimulationInformationType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_SimulationInformationType396", type=xpdl1_TimeEstimationType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
transitionRefs398: BinaryAssociation = BinaryAssociation(
    name="transitionRefs398",
    ends={
        Property(name="xpdl1_TransitionRefsType400", type=xpdl1_SplitType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_SplitType399", type=xpdl1_TransitionRefsType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
automatic401: BinaryAssociation = BinaryAssociation(
    name="automatic401",
    ends={
        Property(name="xpdl1_AutomaticType403", type=xpdl1_StartModeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_StartModeType402", type=xpdl1_AutomaticType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
manual404: BinaryAssociation = BinaryAssociation(
    name="manual404",
    ends={
        Property(name="xpdl1_ManualType406", type=xpdl1_StartModeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_StartModeType405", type=xpdl1_ManualType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actualParameters410: BinaryAssociation = BinaryAssociation(
    name="actualParameters410",
    ends={
        Property(name="xpdl1_ActualParametersType412", type=xpdl1_ToolType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ToolType411", type=xpdl1_ActualParametersType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extendedAttributes413: BinaryAssociation = BinaryAssociation(
    name="extendedAttributes413",
    ends={
        Property(name="xpdl1_ExtendedAttributesType415", type=xpdl1_ToolType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_ToolType414", type=xpdl1_ExtendedAttributesType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actualParameters407: BinaryAssociation = BinaryAssociation(
    name="actualParameters407",
    ends={
        Property(name="xpdl1_ActualParametersType409", type=xpdl1_SubFlowType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_SubFlowType408", type=xpdl1_ActualParametersType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transitionRestriction419: BinaryAssociation = BinaryAssociation(
    name="transitionRestriction419",
    ends={
        Property(name="xpdl1_TransitionRestrictionType421", type=xpdl1_TransitionRestrictionsType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_TransitionRestrictionsType420", type=xpdl1_TransitionRestrictionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
join422: BinaryAssociation = BinaryAssociation(
    name="join422",
    ends={
        Property(name="xpdl1_JoinType424", type=xpdl1_TransitionRestrictionType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_TransitionRestrictionType423", type=xpdl1_JoinType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
split425: BinaryAssociation = BinaryAssociation(
    name="split425",
    ends={
        Property(name="xpdl1_SplitType427", type=xpdl1_TransitionRestrictionType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_TransitionRestrictionType426", type=xpdl1_SplitType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transition428: BinaryAssociation = BinaryAssociation(
    name="transition428",
    ends={
        Property(name="xpdl1_TransitionType430", type=xpdl1_TransitionsType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_TransitionsType429", type=xpdl1_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition431: BinaryAssociation = BinaryAssociation(
    name="condition431",
    ends={
        Property(name="xpdl1_ConditionType433", type=xpdl1_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_TransitionType432", type=xpdl1_ConditionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transitionRef416: BinaryAssociation = BinaryAssociation(
    name="transitionRef416",
    ends={
        Property(name="xpdl1_TransitionRefType418", type=xpdl1_TransitionRefsType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_TransitionRefsType417", type=xpdl1_TransitionRefType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extendedAttributes434: BinaryAssociation = BinaryAssociation(
    name="extendedAttributes434",
    ends={
        Property(name="xpdl1_ExtendedAttributesType436", type=xpdl1_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_TransitionType435", type=xpdl1_ExtendedAttributesType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeDeclaration437: BinaryAssociation = BinaryAssociation(
    name="typeDeclaration437",
    ends={
        Property(name="xpdl1_TypeDeclarationType439", type=xpdl1_TypeDeclarationsType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_TypeDeclarationsType438", type=xpdl1_TypeDeclarationType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basicType440: BinaryAssociation = BinaryAssociation(
    name="basicType440",
    ends={
        Property(name="xpdl1_BasicTypeType442", type=xpdl1_TypeDeclarationType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_TypeDeclarationType441", type=xpdl1_BasicTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaredType443: BinaryAssociation = BinaryAssociation(
    name="declaredType443",
    ends={
        Property(name="xpdl1_DeclaredTypeType445", type=xpdl1_TypeDeclarationType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_TypeDeclarationType444", type=xpdl1_DeclaredTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
externalReference449: BinaryAssociation = BinaryAssociation(
    name="externalReference449",
    ends={
        Property(name="xpdl1_ExternalReferenceType451", type=xpdl1_TypeDeclarationType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_TypeDeclarationType450", type=xpdl1_ExternalReferenceType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
recordType452: BinaryAssociation = BinaryAssociation(
    name="recordType452",
    ends={
        Property(name="xpdl1_RecordTypeType454", type=xpdl1_TypeDeclarationType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_TypeDeclarationType453", type=xpdl1_RecordTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unionType455: BinaryAssociation = BinaryAssociation(
    name="unionType455",
    ends={
        Property(name="xpdl1_UnionTypeType457", type=xpdl1_TypeDeclarationType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_TypeDeclarationType456", type=xpdl1_UnionTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumerationType458: BinaryAssociation = BinaryAssociation(
    name="enumerationType458",
    ends={
        Property(name="xpdl1_EnumerationTypeType460", type=xpdl1_TypeDeclarationType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_TypeDeclarationType459", type=xpdl1_EnumerationTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrayType461: BinaryAssociation = BinaryAssociation(
    name="arrayType461",
    ends={
        Property(name="xpdl1_ArrayTypeType463", type=xpdl1_TypeDeclarationType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_TypeDeclarationType462", type=xpdl1_ArrayTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
listType464: BinaryAssociation = BinaryAssociation(
    name="listType464",
    ends={
        Property(name="xpdl1_ListTypeType466", type=xpdl1_TypeDeclarationType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_TypeDeclarationType465", type=xpdl1_ListTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extendedAttributes467: BinaryAssociation = BinaryAssociation(
    name="extendedAttributes467",
    ends={
        Property(name="xpdl1_ExtendedAttributesType469", type=xpdl1_TypeDeclarationType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_TypeDeclarationType468", type=xpdl1_ExtendedAttributesType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schemaType446: BinaryAssociation = BinaryAssociation(
    name="schemaType446",
    ends={
        Property(name="xpdl1_SchemaTypeType448", type=xpdl1_TypeDeclarationType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_TypeDeclarationType447", type=xpdl1_SchemaTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
member470: BinaryAssociation = BinaryAssociation(
    name="member470",
    ends={
        Property(name="xpdl1_MemberType472", type=xpdl1_UnionTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_UnionTypeType471", type=xpdl1_MemberType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
workflowProcess473: BinaryAssociation = BinaryAssociation(
    name="workflowProcess473",
    ends={
        Property(name="xpdl1_WorkflowProcessType475", type=xpdl1_WorkflowProcessesType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_WorkflowProcessesType474", type=xpdl1_WorkflowProcessType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processHeader476: BinaryAssociation = BinaryAssociation(
    name="processHeader476",
    ends={
        Property(name="xpdl1_ProcessHeaderType478", type=xpdl1_WorkflowProcessType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_WorkflowProcessType477", type=xpdl1_ProcessHeaderType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
redefinableHeader479: BinaryAssociation = BinaryAssociation(
    name="redefinableHeader479",
    ends={
        Property(name="xpdl1_RedefinableHeaderType481", type=xpdl1_WorkflowProcessType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_WorkflowProcessType480", type=xpdl1_RedefinableHeaderType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters482: BinaryAssociation = BinaryAssociation(
    name="formalParameters482",
    ends={
        Property(name="xpdl1_FormalParametersType484", type=xpdl1_WorkflowProcessType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_WorkflowProcessType483", type=xpdl1_FormalParametersType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dataFields485: BinaryAssociation = BinaryAssociation(
    name="dataFields485",
    ends={
        Property(name="xpdl1_DataFieldsType487", type=xpdl1_WorkflowProcessType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_WorkflowProcessType486", type=xpdl1_DataFieldsType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
participants488: BinaryAssociation = BinaryAssociation(
    name="participants488",
    ends={
        Property(name="xpdl1_ParticipantsType490", type=xpdl1_WorkflowProcessType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_WorkflowProcessType489", type=xpdl1_ParticipantsType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
activitySets494: BinaryAssociation = BinaryAssociation(
    name="activitySets494",
    ends={
        Property(name="xpdl1_ActivitySetsType496", type=xpdl1_WorkflowProcessType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_WorkflowProcessType495", type=xpdl1_ActivitySetsType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
activities497: BinaryAssociation = BinaryAssociation(
    name="activities497",
    ends={
        Property(name="xpdl1_ActivitiesType499", type=xpdl1_WorkflowProcessType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_WorkflowProcessType498", type=xpdl1_ActivitiesType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transitions500: BinaryAssociation = BinaryAssociation(
    name="transitions500",
    ends={
        Property(name="xpdl1_TransitionsType502", type=xpdl1_WorkflowProcessType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_WorkflowProcessType501", type=xpdl1_TransitionsType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extendedAttributes503: BinaryAssociation = BinaryAssociation(
    name="extendedAttributes503",
    ends={
        Property(name="xpdl1_ExtendedAttributesType505", type=xpdl1_WorkflowProcessType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_WorkflowProcessType504", type=xpdl1_ExtendedAttributesType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
applications491: BinaryAssociation = BinaryAssociation(
    name="applications491",
    ends={
        Property(name="xpdl1_ApplicationsType493", type=xpdl1_WorkflowProcessType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl1_WorkflowProcessType492", type=xpdl1_ApplicationsType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="xpdl1",
    types={xpdl1_ActivitySetsType, xpdl1_ActivitiesType, xpdl1_ActivityType, xpdl1_ActivitySetType, xpdl1_TransitionsType, xpdl1_RouteType, xpdl1_ImplementationType, xpdl1_BlockActivityType, xpdl1_StartModeType, xpdl1_FinishModeType, xpdl1_DeadlineType, xpdl1_SimulationInformationType, xpdl1_TransitionRestrictionsType, xpdl1_ExtendedAttributesType, xpdl1_ActualParametersType, xpdl1_ApplicationsType, xpdl1_ApplicationType, xpdl1_FormalParametersType, xpdl1_ExternalReferenceType, xpdl1_ArrayTypeType, xpdl1_BasicTypeType, xpdl1_DeclaredTypeType, xpdl1_SchemaTypeType, xpdl1_RecordTypeType, xpdl1_UnionTypeType, xpdl1_EnumerationTypeType, xpdl1_ListTypeType, xpdl1_AutomaticType, xpdl1_ConditionType, xpdl1_XpressionType, xpdl1_ConformanceClassType, xpdl1_DataFieldsType, xpdl1_DataFieldType, xpdl1_DataTypeType, xpdl1_EObject, xpdl1_DocumentRoot, xpdl1_EStringToStringMapEntry, xpdl1_ExternalPackagesType, xpdl1_EnumerationValueType, xpdl1_ExtendedAttributeType, xpdl1_ExternalPackageType, xpdl1_FormalParameterType, xpdl1_JoinType, xpdl1_PackageHeaderType, xpdl1_ParticipantType, xpdl1_ManualType, xpdl1_MemberType, xpdl1_NoType, xpdl1_PackageType, xpdl1_ParticipantsType, xpdl1_ProcessHeaderType, xpdl1_RedefinableHeaderType, xpdl1_ParticipantTypeType, xpdl1_ResponsiblesType, xpdl1_ScriptType, xpdl1_SplitType, xpdl1_SubFlowType, xpdl1_TimeEstimationType, xpdl1_ToolType, xpdl1_TransitionType, xpdl1_TransitionRefType, xpdl1_TransitionRefsType, xpdl1_TypeDeclarationType, xpdl1_TypeDeclarationsType, xpdl1_TransitionRestrictionType, xpdl1_WorkflowProcessType, xpdl1_WorkflowProcessesType, AccessLevelType, DurationUnitType, ExecutionType, ExecutionType1, GraphConformanceType, InstantiationType, IsArrayType, ModeType, PublicationStatusType, TypeType, TypeType1, TypeType2, TypeType3, TypeType4, TypeType5},
    associations={activity0, activitySet1, activities2, transitions5, route7, implementation9, blockActivity11, startMode13, finishMode15, deadline17, simulationInformation19, transitionRestrictions21, extendedAttributes23, application25, recordType41, formalParameters26, externalReference28, extendedAttributes30, basicType33, declaredType34, schemaType36, externalReference38, unionType43, enumerationType45, arrayType48, listType50, xpression52, dataField53, dataType54, extendedAttributes56, basicType59, declaredType62, schemaType65, externalReference68, recordType71, unionType74, enumerationType77, arrayType80, listType83, deadlineCondition86, exceptionName88, xMLNSPrefixMap91, xSISchemaLocation92, activities95, activity98, activitySet101, activitySets104, actualParameters107, application109, applications112, arrayType115, automatic118, basicType120, blockActivity123, condition126, conformanceClass129, dataField131, dataFields134, dataType137, deadline140, declaredType143, enumerationType146, enumerationValue149, extendedAttribute151, extendedAttributes153, externalPackage156, join174, externalPackages158, externalReference160, finishMode163, formalParameter166, formalParameters168, implementation171, packageHeader187, listType176, participant189, manual179, member181, no183, package185, participants191, processHeader195, recordType197, redefinableHeader200, participantType193, responsibles202, route204, schemaType207, script210, simulationInformation212, split215, subFlow220, timeEstimation222, tool224, transition226, transitionRef228, transitionRefs230, startMode217, transitionRestrictions234, transitions237, typeDeclaration240, typeDeclarations242, unionType244, transitionRestriction232, workflowProcess247, workflowProcesses249, xpression251, enumerationValue254, extendedAttribute257, externalPackage260, extendedAttributes263, automatic266, manual269, formalParameter272, dataType275, tool281, subFlow284, basicType287, declaredType290, schemaType293, no278, externalReference296, recordType299, unionType302, enumerationType305, arrayType308, listType312, basicType314, declaredType317, externalReference323, recordType326, unionType329, enumerationType332, arrayType335, listType338, schemaType320, packageHeader341, redefinableHeader344, conformanceClass347, script350, externalPackages353, typeDeclarations356, participants359, applications362, dataFields365, workflowProcesses368, extendedAttributes371, participant374, participantType377, externalReference380, extendedAttributes383, timeEstimation386, member389, responsibles392, timeEstimation395, transitionRefs398, automatic401, manual404, actualParameters410, extendedAttributes413, actualParameters407, transitionRestriction419, join422, split425, transition428, condition431, transitionRef416, extendedAttributes434, typeDeclaration437, basicType440, declaredType443, externalReference449, recordType452, unionType455, enumerationType458, arrayType461, listType464, extendedAttributes467, schemaType446, member470, workflowProcess473, processHeader476, redefinableHeader479, formalParameters482, dataFields485, participants488, activitySets494, activities497, transitions500, extendedAttributes503, applications491},
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