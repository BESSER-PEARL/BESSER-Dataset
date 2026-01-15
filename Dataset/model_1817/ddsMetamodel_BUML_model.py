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
DurabilityQosPolicyKind: Enumeration = Enumeration(
    name="DurabilityQosPolicyKind",
    literals={
            EnumerationLiteral(name="VOLATILE_DURABILITY_QOS"),
			EnumerationLiteral(name="TRANSIENT_LOCAL_DURABILITY_QOS"),
			EnumerationLiteral(name="TRANSIENT_DURABILITY_QOS"),
			EnumerationLiteral(name="PERSISTENT_DURABILITY_QOS")
    }
)

HistoryQosPolicyKind: Enumeration = Enumeration(
    name="HistoryQosPolicyKind",
    literals={
            EnumerationLiteral(name="KEEP_LAST_HISTORY_QOS"),
			EnumerationLiteral(name="KEEP_ALL_HISTORY_QOS")
    }
)

PresentationQosPolicyAccessScopeKind: Enumeration = Enumeration(
    name="PresentationQosPolicyAccessScopeKind",
    literals={
            EnumerationLiteral(name="INSTANCE_PRESENTATION_QOS"),
			EnumerationLiteral(name="TOPIC_PRESENTATION_QOS"),
			EnumerationLiteral(name="GROUP_PRESENTATION_QOS")
    }
)

OwnershipQosPolicyKind: Enumeration = Enumeration(
    name="OwnershipQosPolicyKind",
    literals={
            EnumerationLiteral(name="SHARED_OWNERSHIP_QOS"),
			EnumerationLiteral(name="EXCLUSIVE_OWNERSHIP_QOS")
    }
)

LivelinessQosPolicyKind: Enumeration = Enumeration(
    name="LivelinessQosPolicyKind",
    literals={
            EnumerationLiteral(name="AUTOMATIC_LIVELINESS_QOS"),
			EnumerationLiteral(name="MANUAL_LIVELINESS_QOS"),
			EnumerationLiteral(name="MANUAL_BY_PARTICIPANT_LIVELINESS_QOS"),
			EnumerationLiteral(name="MANUAL_BY_TOPIC_LIVELINESS_QOS")
    }
)

ReliabilityQosPolicyKind: Enumeration = Enumeration(
    name="ReliabilityQosPolicyKind",
    literals={
            EnumerationLiteral(name="RELIABLE_RELIABILITY_QOS"),
			EnumerationLiteral(name="BEST_EFFORT_RELIABILITY_QOS")
    }
)

DestinationOrderQosPolicyKind: Enumeration = Enumeration(
    name="DestinationOrderQosPolicyKind",
    literals={
            EnumerationLiteral(name="BY_RECEPTION_TIMESTAMP_DESTINATIONORDER_QOS"),
			EnumerationLiteral(name="BY_SOURCE_TIMESTAMP_DESTINATIONORDER_QOS")
    }
)

InvalidSampleVisibilityQosPolicy: Enumeration = Enumeration(
    name="InvalidSampleVisibilityQosPolicy",
    literals={
            EnumerationLiteral(name="NO_INVALID_SAMPLES"),
			EnumerationLiteral(name="MINIMUM_INVALID_SAMPLES"),
			EnumerationLiteral(name="ALL_INVALID_SAMPLES")
    }
)

ViewStateKind: Enumeration = Enumeration(
    name="ViewStateKind",
    literals={
            EnumerationLiteral(name="NEW_VIEW_STATE"),
			EnumerationLiteral(name="NOT_NEW_VIEW_STATE"),
			EnumerationLiteral(name="ANY_VIEW_STATE")
    }
)

InstanceStateKind: Enumeration = Enumeration(
    name="InstanceStateKind",
    literals={
            EnumerationLiteral(name="ALIVE_INSTANCE_STATE"),
			EnumerationLiteral(name="NOT_ALIVE_DISPOSED_INSTANCE_STATE"),
			EnumerationLiteral(name="NOT_ALIVE_NO_WRITERS_INSTANCE_STATE"),
			EnumerationLiteral(name="ANY_INSTANCE_STATE")
    }
)

SampleStateKind: Enumeration = Enumeration(
    name="SampleStateKind",
    literals={
            EnumerationLiteral(name="READ_SAMPLE_STATE"),
			EnumerationLiteral(name="NOT_READ_SAMPLE_STATE"),
			EnumerationLiteral(name="ANY_READ_SAMPLE_STATE")
    }
)

DomainParticipantStatus: Enumeration = Enumeration(
    name="DomainParticipantStatus",
    literals={
            EnumerationLiteral(name="INCONSISTENT_TOPIC_STATUS"),
			EnumerationLiteral(name="LIVELINESS_LOST_STATUS"),
			EnumerationLiteral(name="OFFERED_DEADLINE_MISSED_STATUS"),
			EnumerationLiteral(name="OFFERED_INCOMPATIBLE_QOS_STATUS"),
			EnumerationLiteral(name="PUBLICATION_MATCHED_STATUS"),
			EnumerationLiteral(name="SAMPLE_REJECTED_STATUS"),
			EnumerationLiteral(name="LIVELINESS_CHANGED_STATUS"),
			EnumerationLiteral(name="REQUESTED_DEADLINE_MISSED_STATUS"),
			EnumerationLiteral(name="REQUESTED_INCOMPATIBLE_QOS_STATUS"),
			EnumerationLiteral(name="DATA_AVAILABLE_STATUS"),
			EnumerationLiteral(name="SAMPLE_LOST_STATUS"),
			EnumerationLiteral(name="SUBSCRIPTION_MATCHED_STATUS"),
			EnumerationLiteral(name="DATA_ON_READERS_STATUS")
    }
)

SubscriberStatus: Enumeration = Enumeration(
    name="SubscriberStatus",
    literals={
            EnumerationLiteral(name="DATA_ON_READERS_STATUS"),
			EnumerationLiteral(name="DATA_AVAILABLE_STATUS"),
			EnumerationLiteral(name="LIVELINESS_CHANGED_STATUS"),
			EnumerationLiteral(name="REQUESTED_DEADLINE_MISSED_STATUS"),
			EnumerationLiteral(name="REQUESTED_INCOMPATIBLE_QOS_STATUS"),
			EnumerationLiteral(name="SAMPLE_LOST_STATUS"),
			EnumerationLiteral(name="SAMPLE_REJECTED_STATUS"),
			EnumerationLiteral(name="SUBSCRIPTION_MATCHED_STATUS")
    }
)

PublisherStatus: Enumeration = Enumeration(
    name="PublisherStatus",
    literals={
            EnumerationLiteral(name="LIVELINESS_LOST_STATUS"),
			EnumerationLiteral(name="OFFERED_DEADLINE_MISSED_STATUS"),
			EnumerationLiteral(name="OFFERED_INCOMPATIBLE_QOS_STATUS"),
			EnumerationLiteral(name="PUBLICATION_MATCHED_STATUS")
    }
)

DataWriterStatus: Enumeration = Enumeration(
    name="DataWriterStatus",
    literals={
            EnumerationLiteral(name="LIVELINESS_LOST_STATUS"),
			EnumerationLiteral(name="OFFERED_DEADLINE_MISSED_STATUS"),
			EnumerationLiteral(name="OFFERED_INCOMPATIBLE_QOS_STATUS"),
			EnumerationLiteral(name="PUBLICATION_MATCHED_STATUS")
    }
)

DataReaderStatus: Enumeration = Enumeration(
    name="DataReaderStatus",
    literals={
            EnumerationLiteral(name="DATA_AVAILABLE_STATUS"),
			EnumerationLiteral(name="LIVELINESS_CHANGED_STATUS"),
			EnumerationLiteral(name="SAMPLE_REJECTED_STATUS"),
			EnumerationLiteral(name="REQUESTED_DEADLINE_MISSED_STATUS"),
			EnumerationLiteral(name="REQUESTED_INCOMPATIBLE_QOS_STATUS"),
			EnumerationLiteral(name="SAMPLE_LOST_STATUS"),
			EnumerationLiteral(name="SUBSCRIPTION_MATCHED_STATUS")
    }
)

TopicStatus: Enumeration = Enumeration(
    name="TopicStatus",
    literals={
            EnumerationLiteral(name="INCONSISTENT_TOPIC_STATUS")
    }
)

# Classes
ddsMetamodel_DdsApplication = Class(name="ddsMetamodel::DdsApplication")
ddsMetamodel_DdsDomainParticipant = Class(name="ddsMetamodel::DdsDomainParticipant")
ddsMetamodel_DdsWaitSet = Class(name="ddsMetamodel::DdsWaitSet")
ddsMetamodel_DdsSubscriber = Class(name="ddsMetamodel::DdsSubscriber")
ddsMetamodel_DdsPublisher = Class(name="ddsMetamodel::DdsPublisher")
ddsMetamodel_DdsTopic = Class(name="ddsMetamodel::DdsTopic")
ddsMetamodel_DdsTopicListener = Class(name="ddsMetamodel::DdsTopicListener")
ddsMetamodel_DdsTopicQosProfile = Class(name="ddsMetamodel::DdsTopicQosProfile")
ddsMetamodel_DdsDataStructure = Class(name="ddsMetamodel::DdsDataStructure")
ddsMetamodel_DdsQosProfile = Class(name="ddsMetamodel::DdsQosProfile")
ddsMetamodel_DdsDataReader = Class(name="ddsMetamodel::DdsDataReader")
ddsMetamodel_DdsSubscriberListener = Class(name="ddsMetamodel::DdsSubscriberListener")
ddsMetamodel_DdsSubscriberQosProfile = Class(name="ddsMetamodel::DdsSubscriberQosProfile")
ddsMetamodel_DdsDomainParticipantQosProfile = Class(name="ddsMetamodel::DdsDomainParticipantQosProfile")
ddsMetamodel_DdsDomainParticipantListener = Class(name="ddsMetamodel::DdsDomainParticipantListener")
ddsMetamodel_DdsDataReaderListener = Class(name="ddsMetamodel::DdsDataReaderListener")
ddsMetamodel_DdsDataReaderQosProfile = Class(name="ddsMetamodel::DdsDataReaderQosProfile")
ddsMetamodel_DdsDataWriter = Class(name="ddsMetamodel::DdsDataWriter")
ddsMetamodel_DdsPublisherListener = Class(name="ddsMetamodel::DdsPublisherListener")
ddsMetamodel_DdsPublisherQosProfile = Class(name="ddsMetamodel::DdsPublisherQosProfile")
ddsMetamodel_DdsDataModule = Class(name="ddsMetamodel::DdsDataModule")
ddsMetamodel_DdsSystem = Class(name="ddsMetamodel::DdsSystem")
ddsMetamodel_DdsDataField = Class(name="ddsMetamodel::DdsDataField")
ddsMetamodel_DdsStructuredField = Class(name="ddsMetamodel::DdsStructuredField")
ddsMetamodel_DdsDataWriterListener = Class(name="ddsMetamodel::DdsDataWriterListener")
ddsMetamodel_DdsDataWriterQosProfile = Class(name="ddsMetamodel::DdsDataWriterQosProfile")
DdsQosProfile = Class(name="DdsQosProfile")
ddsMetamodel_DdsUserDataQos = Class(name="ddsMetamodel::DdsUserDataQos")
ddsMetamodel_DdsEntityFactoryQos = Class(name="ddsMetamodel::DdsEntityFactoryQos")
ddsMetamodel_DdsTopicDataQos = Class(name="ddsMetamodel::DdsTopicDataQos")
ddsMetamodel_DdsDurabilityQos = Class(name="ddsMetamodel::DdsDurabilityQos")
ddsMetamodel_DdsDurabilityServiceQos = Class(name="ddsMetamodel::DdsDurabilityServiceQos")
ddsMetamodel_DdsLatencyBudgetQos = Class(name="ddsMetamodel::DdsLatencyBudgetQos")
ddsMetamodel_DdsReliabilityQos = Class(name="ddsMetamodel::DdsReliabilityQos")
ddsMetamodel_DdsDestinationOrderQos = Class(name="ddsMetamodel::DdsDestinationOrderQos")
ddsMetamodel_DdsHistoryQos = Class(name="ddsMetamodel::DdsHistoryQos")
ddsMetamodel_DdsResourceLimits = Class(name="ddsMetamodel::DdsResourceLimits")
ddsMetamodel_DdsTransportPriorityQos = Class(name="ddsMetamodel::DdsTransportPriorityQos")
ddsMetamodel_DdsLifespan = Class(name="ddsMetamodel::DdsLifespan")
ddsMetamodel_DdsDeadlineQos = Class(name="ddsMetamodel::DdsDeadlineQos")
ddsMetamodel_DdsLivelinessQos = Class(name="ddsMetamodel::DdsLivelinessQos")
ddsMetamodel_DdsOwnershipQos = Class(name="ddsMetamodel::DdsOwnershipQos")
ddsMetamodel_DdsDuration = Class(name="ddsMetamodel::DdsDuration")
ddsMetamodel_DdsPresentationQos = Class(name="ddsMetamodel::DdsPresentationQos")
ddsMetamodel_DdsOwnershipStrengthQos = Class(name="ddsMetamodel::DdsOwnershipStrengthQos")
ddsMetamodel_DdsTimeBasedFilterQos = Class(name="ddsMetamodel::DdsTimeBasedFilterQos")
ddsMetamodel_DdsPartitionQos = Class(name="ddsMetamodel::DdsPartitionQos")
ddsMetamodel_DdsDataWriterLifecycleQos = Class(name="ddsMetamodel::DdsDataWriterLifecycleQos")
ddsMetamodel_DdsDataReaderLifecycleQos = Class(name="ddsMetamodel::DdsDataReaderLifecycleQos")
ddsMetamodel_DdsGroupDataQos = Class(name="ddsMetamodel::DdsGroupDataQos")
ddsMetamodel_DdsReadCondition = Class(name="ddsMetamodel::DdsReadCondition")
ddsMetamodel_DdsStatusCondition = Class(name="ddsMetamodel::DdsStatusCondition")
ddsMetamodel_GuardCondition = Class(name="ddsMetamodel::GuardCondition")
ddsMetamodel_DdsPublisherStatusCondition = Class(name="ddsMetamodel::DdsPublisherStatusCondition")
ddsMetamodel_DdsSubscriberStatusCondition = Class(name="ddsMetamodel::DdsSubscriberStatusCondition")
ddsMetamodel_DdsDomainParticipantStatusCondition = Class(name="ddsMetamodel::DdsDomainParticipantStatusCondition")
DdsStatusCondition = Class(name="DdsStatusCondition")
ddsMetamodel_DdsDataReaderStatusCondition = Class(name="ddsMetamodel::DdsDataReaderStatusCondition")
ddsMetamodel_DdsTopicStatusCondition = Class(name="ddsMetamodel::DdsTopicStatusCondition")
ddsMetamodel_QueryCondition = Class(name="ddsMetamodel::QueryCondition")
DdsReadCondition = Class(name="DdsReadCondition")
ddsMetamodel_DdsDataWriterStatusCondition = Class(name="ddsMetamodel::DdsDataWriterStatusCondition")
ddsMetamodel_DdsHost = Class(name="ddsMetamodel::DdsHost")

# ddsMetamodel_DdsApplication class attributes and methods
ddsMetamodel_DdsApplication_applicationName: Property = Property(name="applicationName", type=StringType)
ddsMetamodel_DdsApplication.attributes={ddsMetamodel_DdsApplication_applicationName}

# ddsMetamodel_DdsDomainParticipant class attributes and methods
ddsMetamodel_DdsDomainParticipant_domainParticipantName: Property = Property(name="domainParticipantName", type=StringType)
ddsMetamodel_DdsDomainParticipant_domainId: Property = Property(name="domainId", type=IntegerType)
ddsMetamodel_DdsDomainParticipant.attributes={ddsMetamodel_DdsDomainParticipant_domainParticipantName, ddsMetamodel_DdsDomainParticipant_domainId}

# ddsMetamodel_DdsWaitSet class attributes and methods
ddsMetamodel_DdsWaitSet_name: Property = Property(name="name", type=StringType)
ddsMetamodel_DdsWaitSet.attributes={ddsMetamodel_DdsWaitSet_name}

# ddsMetamodel_DdsSubscriber class attributes and methods
ddsMetamodel_DdsSubscriber_subscriberName: Property = Property(name="subscriberName", type=StringType)
ddsMetamodel_DdsSubscriber.attributes={ddsMetamodel_DdsSubscriber_subscriberName}

# ddsMetamodel_DdsPublisher class attributes and methods
ddsMetamodel_DdsPublisher_publisherName: Property = Property(name="publisherName", type=StringType)
ddsMetamodel_DdsPublisher.attributes={ddsMetamodel_DdsPublisher_publisherName}

# ddsMetamodel_DdsTopic class attributes and methods
ddsMetamodel_DdsTopic_topicName: Property = Property(name="topicName", type=StringType)
ddsMetamodel_DdsTopic.attributes={ddsMetamodel_DdsTopic_topicName}

# ddsMetamodel_DdsTopicListener class attributes and methods
ddsMetamodel_DdsTopicListener_name: Property = Property(name="name", type=StringType)
ddsMetamodel_DdsTopicListener_listenedStatus: Property = Property(name="listenedStatus", type=StringType)
ddsMetamodel_DdsTopicListener.attributes={ddsMetamodel_DdsTopicListener_name, ddsMetamodel_DdsTopicListener_listenedStatus}

# ddsMetamodel_DdsTopicQosProfile class attributes and methods

# ddsMetamodel_DdsDataStructure class attributes and methods
ddsMetamodel_DdsDataStructure_structureName: Property = Property(name="structureName", type=StringType)
ddsMetamodel_DdsDataStructure.attributes={ddsMetamodel_DdsDataStructure_structureName}

# ddsMetamodel_DdsQosProfile class attributes and methods
ddsMetamodel_DdsQosProfile_profileName: Property = Property(name="profileName", type=StringType)
ddsMetamodel_DdsQosProfile.attributes={ddsMetamodel_DdsQosProfile_profileName}

# ddsMetamodel_DdsDataReader class attributes and methods
ddsMetamodel_DdsDataReader_dataReaderName: Property = Property(name="dataReaderName", type=StringType)
ddsMetamodel_DdsDataReader.attributes={ddsMetamodel_DdsDataReader_dataReaderName}

# ddsMetamodel_DdsSubscriberListener class attributes and methods
ddsMetamodel_DdsSubscriberListener_name: Property = Property(name="name", type=StringType)
ddsMetamodel_DdsSubscriberListener_listenedStatus: Property = Property(name="listenedStatus", type=StringType)
ddsMetamodel_DdsSubscriberListener.attributes={ddsMetamodel_DdsSubscriberListener_name, ddsMetamodel_DdsSubscriberListener_listenedStatus}

# ddsMetamodel_DdsSubscriberQosProfile class attributes and methods

# ddsMetamodel_DdsDomainParticipantQosProfile class attributes and methods

# ddsMetamodel_DdsDomainParticipantListener class attributes and methods
ddsMetamodel_DdsDomainParticipantListener_name: Property = Property(name="name", type=StringType)
ddsMetamodel_DdsDomainParticipantListener_listenedStatus: Property = Property(name="listenedStatus", type=StringType)
ddsMetamodel_DdsDomainParticipantListener.attributes={ddsMetamodel_DdsDomainParticipantListener_name, ddsMetamodel_DdsDomainParticipantListener_listenedStatus}

# ddsMetamodel_DdsDataReaderListener class attributes and methods
ddsMetamodel_DdsDataReaderListener_name: Property = Property(name="name", type=StringType)
ddsMetamodel_DdsDataReaderListener_listenedStatus: Property = Property(name="listenedStatus", type=StringType)
ddsMetamodel_DdsDataReaderListener.attributes={ddsMetamodel_DdsDataReaderListener_listenedStatus, ddsMetamodel_DdsDataReaderListener_name}

# ddsMetamodel_DdsDataReaderQosProfile class attributes and methods

# ddsMetamodel_DdsDataWriter class attributes and methods
ddsMetamodel_DdsDataWriter_dataWriterName: Property = Property(name="dataWriterName", type=StringType)
ddsMetamodel_DdsDataWriter.attributes={ddsMetamodel_DdsDataWriter_dataWriterName}

# ddsMetamodel_DdsPublisherListener class attributes and methods
ddsMetamodel_DdsPublisherListener_listenedStatus: Property = Property(name="listenedStatus", type=StringType)
ddsMetamodel_DdsPublisherListener_name: Property = Property(name="name", type=StringType)
ddsMetamodel_DdsPublisherListener.attributes={ddsMetamodel_DdsPublisherListener_name, ddsMetamodel_DdsPublisherListener_listenedStatus}

# ddsMetamodel_DdsPublisherQosProfile class attributes and methods

# ddsMetamodel_DdsDataModule class attributes and methods
ddsMetamodel_DdsDataModule_moduleName: Property = Property(name="moduleName", type=StringType)
ddsMetamodel_DdsDataModule.attributes={ddsMetamodel_DdsDataModule_moduleName}

# ddsMetamodel_DdsSystem class attributes and methods
ddsMetamodel_DdsSystem_systemName: Property = Property(name="systemName", type=StringType)
ddsMetamodel_DdsSystem.attributes={ddsMetamodel_DdsSystem_systemName}

# ddsMetamodel_DdsDataField class attributes and methods
ddsMetamodel_DdsDataField_maxMultiplicity: Property = Property(name="maxMultiplicity", type=IntegerType)
ddsMetamodel_DdsDataField_fieldType: Property = Property(name="fieldType", type=StringType)
ddsMetamodel_DdsDataField_fieldName: Property = Property(name="fieldName", type=StringType)
ddsMetamodel_DdsDataField_isKey: Property = Property(name="isKey", type=BooleanType)
ddsMetamodel_DdsDataField.attributes={ddsMetamodel_DdsDataField_fieldType, ddsMetamodel_DdsDataField_isKey, ddsMetamodel_DdsDataField_maxMultiplicity, ddsMetamodel_DdsDataField_fieldName}

# ddsMetamodel_DdsStructuredField class attributes and methods
ddsMetamodel_DdsStructuredField_isKey: Property = Property(name="isKey", type=BooleanType)
ddsMetamodel_DdsStructuredField_maxMultiplicity: Property = Property(name="maxMultiplicity", type=IntegerType)
ddsMetamodel_DdsStructuredField_fieldName: Property = Property(name="fieldName", type=StringType)
ddsMetamodel_DdsStructuredField.attributes={ddsMetamodel_DdsStructuredField_isKey, ddsMetamodel_DdsStructuredField_maxMultiplicity, ddsMetamodel_DdsStructuredField_fieldName}

# ddsMetamodel_DdsDataWriterListener class attributes and methods
ddsMetamodel_DdsDataWriterListener_name: Property = Property(name="name", type=StringType)
ddsMetamodel_DdsDataWriterListener_listenedStatus: Property = Property(name="listenedStatus", type=StringType)
ddsMetamodel_DdsDataWriterListener.attributes={ddsMetamodel_DdsDataWriterListener_name, ddsMetamodel_DdsDataWriterListener_listenedStatus}

# ddsMetamodel_DdsDataWriterQosProfile class attributes and methods

# DdsQosProfile class attributes and methods

# ddsMetamodel_DdsUserDataQos class attributes and methods
ddsMetamodel_DdsUserDataQos_value: Property = Property(name="value", type=StringType)
ddsMetamodel_DdsUserDataQos.attributes={ddsMetamodel_DdsUserDataQos_value}

# ddsMetamodel_DdsEntityFactoryQos class attributes and methods
ddsMetamodel_DdsEntityFactoryQos_autoenable_created_entities: Property = Property(name="autoenable_created_entities", type=BooleanType)
ddsMetamodel_DdsEntityFactoryQos.attributes={ddsMetamodel_DdsEntityFactoryQos_autoenable_created_entities}

# ddsMetamodel_DdsTopicDataQos class attributes and methods
ddsMetamodel_DdsTopicDataQos_value: Property = Property(name="value", type=StringType)
ddsMetamodel_DdsTopicDataQos.attributes={ddsMetamodel_DdsTopicDataQos_value}

# ddsMetamodel_DdsDurabilityQos class attributes and methods
ddsMetamodel_DdsDurabilityQos_kind: Property = Property(name="kind", type=StringType)
ddsMetamodel_DdsDurabilityQos.attributes={ddsMetamodel_DdsDurabilityQos_kind}

# ddsMetamodel_DdsDurabilityServiceQos class attributes and methods
ddsMetamodel_DdsDurabilityServiceQos_history_kind: Property = Property(name="history_kind", type=StringType)
ddsMetamodel_DdsDurabilityServiceQos_history_depth: Property = Property(name="history_depth", type=StringType)
ddsMetamodel_DdsDurabilityServiceQos_max_samples: Property = Property(name="max_samples", type=StringType)
ddsMetamodel_DdsDurabilityServiceQos_max_instances: Property = Property(name="max_instances", type=StringType)
ddsMetamodel_DdsDurabilityServiceQos_max_samples_per_instances: Property = Property(name="max_samples_per_instances", type=StringType)
ddsMetamodel_DdsDurabilityServiceQos.attributes={ddsMetamodel_DdsDurabilityServiceQos_max_instances, ddsMetamodel_DdsDurabilityServiceQos_max_samples_per_instances, ddsMetamodel_DdsDurabilityServiceQos_max_samples, ddsMetamodel_DdsDurabilityServiceQos_history_kind, ddsMetamodel_DdsDurabilityServiceQos_history_depth}

# ddsMetamodel_DdsLatencyBudgetQos class attributes and methods

# ddsMetamodel_DdsReliabilityQos class attributes and methods
ddsMetamodel_DdsReliabilityQos_kind: Property = Property(name="kind", type=StringType)
ddsMetamodel_DdsReliabilityQos.attributes={ddsMetamodel_DdsReliabilityQos_kind}

# ddsMetamodel_DdsDestinationOrderQos class attributes and methods
ddsMetamodel_DdsDestinationOrderQos_kind: Property = Property(name="kind", type=StringType)
ddsMetamodel_DdsDestinationOrderQos.attributes={ddsMetamodel_DdsDestinationOrderQos_kind}

# ddsMetamodel_DdsHistoryQos class attributes and methods
ddsMetamodel_DdsHistoryQos_kind: Property = Property(name="kind", type=StringType)
ddsMetamodel_DdsHistoryQos_depth: Property = Property(name="depth", type=StringType)
ddsMetamodel_DdsHistoryQos.attributes={ddsMetamodel_DdsHistoryQos_depth, ddsMetamodel_DdsHistoryQos_kind}

# ddsMetamodel_DdsResourceLimits class attributes and methods
ddsMetamodel_DdsResourceLimits_max_samples: Property = Property(name="max_samples", type=StringType)
ddsMetamodel_DdsResourceLimits_max_instances: Property = Property(name="max_instances", type=StringType)
ddsMetamodel_DdsResourceLimits_max_samples_per_instances: Property = Property(name="max_samples_per_instances", type=StringType)
ddsMetamodel_DdsResourceLimits.attributes={ddsMetamodel_DdsResourceLimits_max_samples, ddsMetamodel_DdsResourceLimits_max_samples_per_instances, ddsMetamodel_DdsResourceLimits_max_instances}

# ddsMetamodel_DdsTransportPriorityQos class attributes and methods
ddsMetamodel_DdsTransportPriorityQos_value: Property = Property(name="value", type=StringType)
ddsMetamodel_DdsTransportPriorityQos.attributes={ddsMetamodel_DdsTransportPriorityQos_value}

# ddsMetamodel_DdsLifespan class attributes and methods

# ddsMetamodel_DdsDeadlineQos class attributes and methods

# ddsMetamodel_DdsLivelinessQos class attributes and methods
ddsMetamodel_DdsLivelinessQos_kind: Property = Property(name="kind", type=StringType)
ddsMetamodel_DdsLivelinessQos.attributes={ddsMetamodel_DdsLivelinessQos_kind}

# ddsMetamodel_DdsOwnershipQos class attributes and methods
ddsMetamodel_DdsOwnershipQos_kind: Property = Property(name="kind", type=StringType)
ddsMetamodel_DdsOwnershipQos.attributes={ddsMetamodel_DdsOwnershipQos_kind}

# ddsMetamodel_DdsDuration class attributes and methods
ddsMetamodel_DdsDuration_sec: Property = Property(name="sec", type=StringType)
ddsMetamodel_DdsDuration_nanoSec: Property = Property(name="nanoSec", type=StringType)
ddsMetamodel_DdsDuration.attributes={ddsMetamodel_DdsDuration_sec, ddsMetamodel_DdsDuration_nanoSec}

# ddsMetamodel_DdsPresentationQos class attributes and methods
ddsMetamodel_DdsPresentationQos_access_scope: Property = Property(name="access_scope", type=StringType)
ddsMetamodel_DdsPresentationQos_coherent_access: Property = Property(name="coherent_access", type=BooleanType)
ddsMetamodel_DdsPresentationQos_ordered_access: Property = Property(name="ordered_access", type=BooleanType)
ddsMetamodel_DdsPresentationQos.attributes={ddsMetamodel_DdsPresentationQos_ordered_access, ddsMetamodel_DdsPresentationQos_access_scope, ddsMetamodel_DdsPresentationQos_coherent_access}

# ddsMetamodel_DdsOwnershipStrengthQos class attributes and methods
ddsMetamodel_DdsOwnershipStrengthQos_value: Property = Property(name="value", type=StringType)
ddsMetamodel_DdsOwnershipStrengthQos.attributes={ddsMetamodel_DdsOwnershipStrengthQos_value}

# ddsMetamodel_DdsTimeBasedFilterQos class attributes and methods

# ddsMetamodel_DdsPartitionQos class attributes and methods
ddsMetamodel_DdsPartitionQos_name: Property = Property(name="name", type=StringType)
ddsMetamodel_DdsPartitionQos.attributes={ddsMetamodel_DdsPartitionQos_name}

# ddsMetamodel_DdsDataWriterLifecycleQos class attributes and methods
ddsMetamodel_DdsDataWriterLifecycleQos_autodispose_unregistered_instances: Property = Property(name="autodispose_unregistered_instances", type=BooleanType)
ddsMetamodel_DdsDataWriterLifecycleQos.attributes={ddsMetamodel_DdsDataWriterLifecycleQos_autodispose_unregistered_instances}

# ddsMetamodel_DdsDataReaderLifecycleQos class attributes and methods
ddsMetamodel_DdsDataReaderLifecycleQos_autopurge_dispose_all: Property = Property(name="autopurge_dispose_all", type=BooleanType)
ddsMetamodel_DdsDataReaderLifecycleQos_enable_invalid_samples: Property = Property(name="enable_invalid_samples", type=BooleanType)
ddsMetamodel_DdsDataReaderLifecycleQos.attributes={ddsMetamodel_DdsDataReaderLifecycleQos_enable_invalid_samples, ddsMetamodel_DdsDataReaderLifecycleQos_autopurge_dispose_all}

# ddsMetamodel_DdsGroupDataQos class attributes and methods
ddsMetamodel_DdsGroupDataQos_value: Property = Property(name="value", type=StringType)
ddsMetamodel_DdsGroupDataQos.attributes={ddsMetamodel_DdsGroupDataQos_value}

# ddsMetamodel_DdsReadCondition class attributes and methods
ddsMetamodel_DdsReadCondition_instance_state_mask: Property = Property(name="instance_state_mask", type=StringType)
ddsMetamodel_DdsReadCondition_sample_state_mask: Property = Property(name="sample_state_mask", type=StringType)
ddsMetamodel_DdsReadCondition_view_state_mask: Property = Property(name="view_state_mask", type=StringType)
ddsMetamodel_DdsReadCondition.attributes={ddsMetamodel_DdsReadCondition_view_state_mask, ddsMetamodel_DdsReadCondition_instance_state_mask, ddsMetamodel_DdsReadCondition_sample_state_mask}

# ddsMetamodel_DdsStatusCondition class attributes and methods

# ddsMetamodel_GuardCondition class attributes and methods
ddsMetamodel_GuardCondition_name: Property = Property(name="name", type=StringType)
ddsMetamodel_GuardCondition.attributes={ddsMetamodel_GuardCondition_name}

# ddsMetamodel_DdsPublisherStatusCondition class attributes and methods
ddsMetamodel_DdsPublisherStatusCondition_enabled_status: Property = Property(name="enabled_status", type=StringType)
ddsMetamodel_DdsPublisherStatusCondition.attributes={ddsMetamodel_DdsPublisherStatusCondition_enabled_status}

# ddsMetamodel_DdsSubscriberStatusCondition class attributes and methods
ddsMetamodel_DdsSubscriberStatusCondition_enabled_status: Property = Property(name="enabled_status", type=StringType)
ddsMetamodel_DdsSubscriberStatusCondition.attributes={ddsMetamodel_DdsSubscriberStatusCondition_enabled_status}

# ddsMetamodel_DdsDomainParticipantStatusCondition class attributes and methods
ddsMetamodel_DdsDomainParticipantStatusCondition_enabled_status: Property = Property(name="enabled_status", type=StringType)
ddsMetamodel_DdsDomainParticipantStatusCondition.attributes={ddsMetamodel_DdsDomainParticipantStatusCondition_enabled_status}

# DdsStatusCondition class attributes and methods

# ddsMetamodel_DdsDataReaderStatusCondition class attributes and methods
ddsMetamodel_DdsDataReaderStatusCondition_enabled_status: Property = Property(name="enabled_status", type=StringType)
ddsMetamodel_DdsDataReaderStatusCondition.attributes={ddsMetamodel_DdsDataReaderStatusCondition_enabled_status}

# ddsMetamodel_DdsTopicStatusCondition class attributes and methods
ddsMetamodel_DdsTopicStatusCondition_enabled_status: Property = Property(name="enabled_status", type=StringType)
ddsMetamodel_DdsTopicStatusCondition.attributes={ddsMetamodel_DdsTopicStatusCondition_enabled_status}

# ddsMetamodel_QueryCondition class attributes and methods
ddsMetamodel_QueryCondition_query: Property = Property(name="query", type=StringType)
ddsMetamodel_QueryCondition_queryParameters: Property = Property(name="queryParameters", type=StringType)
ddsMetamodel_QueryCondition.attributes={ddsMetamodel_QueryCondition_queryParameters, ddsMetamodel_QueryCondition_query}

# DdsReadCondition class attributes and methods

# ddsMetamodel_DdsDataWriterStatusCondition class attributes and methods
ddsMetamodel_DdsDataWriterStatusCondition_enabled_status: Property = Property(name="enabled_status", type=StringType)
ddsMetamodel_DdsDataWriterStatusCondition.attributes={ddsMetamodel_DdsDataWriterStatusCondition_enabled_status}

# ddsMetamodel_DdsHost class attributes and methods
ddsMetamodel_DdsHost_hostName: Property = Property(name="hostName", type=StringType)
ddsMetamodel_DdsHost.attributes={ddsMetamodel_DdsHost_hostName}

# Relationships
domainParticipants0: BinaryAssociation = BinaryAssociation(
    name="domainParticipants0",
    ends={
        Property(name="ddsMetamodel_DdsDomainParticipant", type=ddsMetamodel_DdsApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsApplication", type=ddsMetamodel_DdsDomainParticipant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
waitset1: BinaryAssociation = BinaryAssociation(
    name="waitset1",
    ends={
        Property(name="ddsMetamodel_DdsWaitSet", type=ddsMetamodel_DdsApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsApplication2", type=ddsMetamodel_DdsWaitSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ddssubscriber3: BinaryAssociation = BinaryAssociation(
    name="ddssubscriber3",
    ends={
        Property(name="ddsMetamodel_DdsSubscriber", type=ddsMetamodel_DdsDomainParticipant, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDomainParticipant4", type=ddsMetamodel_DdsSubscriber, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ddspublisher5: BinaryAssociation = BinaryAssociation(
    name="ddspublisher5",
    ends={
        Property(name="ddsMetamodel_DdsPublisher", type=ddsMetamodel_DdsDomainParticipant, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDomainParticipant6", type=ddsMetamodel_DdsPublisher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
topicListener11: BinaryAssociation = BinaryAssociation(
    name="topicListener11",
    ends={
        Property(name="ddsMetamodel_DdsTopicListener", type=ddsMetamodel_DdsTopic, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsTopic", type=ddsMetamodel_DdsTopicListener, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
topicQosProfile12: BinaryAssociation = BinaryAssociation(
    name="topicQosProfile12",
    ends={
        Property(name="ddsMetamodel_DdsTopicQosProfile", type=ddsMetamodel_DdsTopic, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsTopic13", type=ddsMetamodel_DdsTopicQosProfile, multiplicity=Multiplicity(0, 1))
    }
)
ddsdatastructure14: BinaryAssociation = BinaryAssociation(
    name="ddsdatastructure14",
    ends={
        Property(name="ddsMetamodel_DdsDataStructure", type=ddsMetamodel_DdsTopic, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsTopic15", type=ddsMetamodel_DdsDataStructure, multiplicity=Multiplicity(0, 1))
    }
)
ddsdatareader16: BinaryAssociation = BinaryAssociation(
    name="ddsdatareader16",
    ends={
        Property(name="DdsDataReader", type=ddsMetamodel_DdsSubscriber, multiplicity=Multiplicity(1, 1)),
        Property(name="containingSubscriber", type=ddsMetamodel_DdsDataReader, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subscriberListener17: BinaryAssociation = BinaryAssociation(
    name="subscriberListener17",
    ends={
        Property(name="ddsMetamodel_DdsSubscriberListener", type=ddsMetamodel_DdsSubscriber, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsSubscriber18", type=ddsMetamodel_DdsSubscriberListener, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subscriberQosProfile19: BinaryAssociation = BinaryAssociation(
    name="subscriberQosProfile19",
    ends={
        Property(name="ddsMetamodel_DdsSubscriberQosProfile", type=ddsMetamodel_DdsSubscriber, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsSubscriber20", type=ddsMetamodel_DdsSubscriberQosProfile, multiplicity=Multiplicity(0, 1))
    }
)
ddsdomainparticipantqosprofile7: BinaryAssociation = BinaryAssociation(
    name="ddsdomainparticipantqosprofile7",
    ends={
        Property(name="ddsMetamodel_DdsDomainParticipantQosProfile", type=ddsMetamodel_DdsDomainParticipant, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDomainParticipant8", type=ddsMetamodel_DdsDomainParticipantQosProfile, multiplicity=Multiplicity(0, 1))
    }
)
domainParticipantListener9: BinaryAssociation = BinaryAssociation(
    name="domainParticipantListener9",
    ends={
        Property(name="ddsMetamodel_DdsDomainParticipantListener", type=ddsMetamodel_DdsDomainParticipant, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDomainParticipant10", type=ddsMetamodel_DdsDomainParticipantListener, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dataReaderListener23: BinaryAssociation = BinaryAssociation(
    name="dataReaderListener23",
    ends={
        Property(name="ddsMetamodel_DdsDataReaderListener", type=ddsMetamodel_DdsDataReader, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataReader24", type=ddsMetamodel_DdsDataReaderListener, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dataReaderQosProfile25: BinaryAssociation = BinaryAssociation(
    name="dataReaderQosProfile25",
    ends={
        Property(name="ddsMetamodel_DdsDataReaderQosProfile", type=ddsMetamodel_DdsDataReader, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataReader26", type=ddsMetamodel_DdsDataReaderQosProfile, multiplicity=Multiplicity(0, 1))
    }
)
containingSubscriber27: BinaryAssociation = BinaryAssociation(
    name="containingSubscriber27",
    ends={
        Property(name="DdsSubscriber", type=ddsMetamodel_DdsDataReader, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsdatareader", type=ddsMetamodel_DdsSubscriber, multiplicity=Multiplicity(1, 1))
    }
)
ddsdatawriter28: BinaryAssociation = BinaryAssociation(
    name="ddsdatawriter28",
    ends={
        Property(name="ddsMetamodel_DdsDataWriter", type=ddsMetamodel_DdsPublisher, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsPublisher29", type=ddsMetamodel_DdsDataWriter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
publisherListener30: BinaryAssociation = BinaryAssociation(
    name="publisherListener30",
    ends={
        Property(name="ddsMetamodel_DdsPublisherListener", type=ddsMetamodel_DdsPublisher, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsPublisher31", type=ddsMetamodel_DdsPublisherListener, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
publisherQosProfile32: BinaryAssociation = BinaryAssociation(
    name="publisherQosProfile32",
    ends={
        Property(name="ddsMetamodel_DdsPublisherQosProfile", type=ddsMetamodel_DdsPublisher, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsPublisher33", type=ddsMetamodel_DdsPublisherQosProfile, multiplicity=Multiplicity(0, 1))
    }
)
publiableTopic34: BinaryAssociation = BinaryAssociation(
    name="publiableTopic34",
    ends={
        Property(name="ddsMetamodel_DdsTopic36", type=ddsMetamodel_DdsDataWriter, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataWriter35", type=ddsMetamodel_DdsTopic, multiplicity=Multiplicity(1, 1))
    }
)
readableTopic21: BinaryAssociation = BinaryAssociation(
    name="readableTopic21",
    ends={
        Property(name="ddsMetamodel_DdsTopic22", type=ddsMetamodel_DdsDataReader, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataReader", type=ddsMetamodel_DdsTopic, multiplicity=Multiplicity(1, 1))
    }
)
dataStructures41: BinaryAssociation = BinaryAssociation(
    name="dataStructures41",
    ends={
        Property(name="DdsDataStructure", type=ddsMetamodel_DdsDataModule, multiplicity=Multiplicity(1, 1)),
        Property(name="containerDataModule", type=ddsMetamodel_DdsDataStructure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerModules43: BinaryAssociation = BinaryAssociation(
    name="innerModules43",
    ends={
        Property(name="DdsDataModule", type=ddsMetamodel_DdsDataModule, multiplicity=Multiplicity(1, 1)),
        Property(name="containingModule", type=ddsMetamodel_DdsDataModule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containingSystem44: BinaryAssociation = BinaryAssociation(
    name="containingSystem44",
    ends={
        Property(name="DdsSystem", type=ddsMetamodel_DdsDataModule, multiplicity=Multiplicity(1, 1)),
        Property(name="dataModules", type=ddsMetamodel_DdsSystem, multiplicity=Multiplicity(0, 1))
    }
)
containingModule46: BinaryAssociation = BinaryAssociation(
    name="containingModule46",
    ends={
        Property(name="DdsDataModule47", type=ddsMetamodel_DdsDataModule, multiplicity=Multiplicity(1, 1)),
        Property(name="innerModules", type=ddsMetamodel_DdsDataModule, multiplicity=Multiplicity(0, 1))
    }
)
fields48: BinaryAssociation = BinaryAssociation(
    name="fields48",
    ends={
        Property(name="ddsMetamodel_DdsDataField", type=ddsMetamodel_DdsDataStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataStructure49", type=ddsMetamodel_DdsDataField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuredFields50: BinaryAssociation = BinaryAssociation(
    name="structuredFields50",
    ends={
        Property(name="DdsStructuredField", type=ddsMetamodel_DdsDataStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="dataStructure", type=ddsMetamodel_DdsStructuredField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containerDataModule51: BinaryAssociation = BinaryAssociation(
    name="containerDataModule51",
    ends={
        Property(name="DdsDataModule52", type=ddsMetamodel_DdsDataStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="dataStructures", type=ddsMetamodel_DdsDataModule, multiplicity=Multiplicity(0, 1))
    }
)
dataWriterListener37: BinaryAssociation = BinaryAssociation(
    name="dataWriterListener37",
    ends={
        Property(name="ddsMetamodel_DdsDataWriterListener", type=ddsMetamodel_DdsDataWriter, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataWriter38", type=ddsMetamodel_DdsDataWriterListener, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dataWriterQosProfile39: BinaryAssociation = BinaryAssociation(
    name="dataWriterQosProfile39",
    ends={
        Property(name="ddsMetamodel_DdsDataWriterQosProfile", type=ddsMetamodel_DdsDataWriter, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataWriter40", type=ddsMetamodel_DdsDataWriterQosProfile, multiplicity=Multiplicity(0, 1))
    }
)
userDataQos53: BinaryAssociation = BinaryAssociation(
    name="userDataQos53",
    ends={
        Property(name="ddsMetamodel_DdsUserDataQos", type=ddsMetamodel_DdsDomainParticipantQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDomainParticipantQosProfile54", type=ddsMetamodel_DdsUserDataQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entityFactoryQos55: BinaryAssociation = BinaryAssociation(
    name="entityFactoryQos55",
    ends={
        Property(name="ddsMetamodel_DdsEntityFactoryQos", type=ddsMetamodel_DdsDomainParticipantQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDomainParticipantQosProfile56", type=ddsMetamodel_DdsEntityFactoryQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
topicDataQos57: BinaryAssociation = BinaryAssociation(
    name="topicDataQos57",
    ends={
        Property(name="ddsMetamodel_DdsTopicDataQos", type=ddsMetamodel_DdsTopicQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsTopicQosProfile58", type=ddsMetamodel_DdsTopicDataQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
durabilityQos59: BinaryAssociation = BinaryAssociation(
    name="durabilityQos59",
    ends={
        Property(name="ddsMetamodel_DdsDurabilityQos", type=ddsMetamodel_DdsTopicQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsTopicQosProfile60", type=ddsMetamodel_DdsDurabilityQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
durabilityServiceQos61: BinaryAssociation = BinaryAssociation(
    name="durabilityServiceQos61",
    ends={
        Property(name="ddsMetamodel_DdsDurabilityServiceQos", type=ddsMetamodel_DdsTopicQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsTopicQosProfile62", type=ddsMetamodel_DdsDurabilityServiceQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
latencyBudgetQos63: BinaryAssociation = BinaryAssociation(
    name="latencyBudgetQos63",
    ends={
        Property(name="ddsMetamodel_DdsLatencyBudgetQos", type=ddsMetamodel_DdsTopicQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsTopicQosProfile64", type=ddsMetamodel_DdsLatencyBudgetQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownershipQos67: BinaryAssociation = BinaryAssociation(
    name="ownershipQos67",
    ends={
        Property(name="ddsMetamodel_DdsTopicQosProfile68", type=ddsMetamodel_DdsOwnershipQos, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="ddsMetamodel_DdsOwnershipQos", type=ddsMetamodel_DdsTopicQosProfile, multiplicity=Multiplicity(1, 1))
    }
)
reliabilityQos69: BinaryAssociation = BinaryAssociation(
    name="reliabilityQos69",
    ends={
        Property(name="ddsMetamodel_DdsReliabilityQos", type=ddsMetamodel_DdsTopicQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsTopicQosProfile70", type=ddsMetamodel_DdsReliabilityQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
destinationOrderQos71: BinaryAssociation = BinaryAssociation(
    name="destinationOrderQos71",
    ends={
        Property(name="ddsMetamodel_DdsDestinationOrderQos", type=ddsMetamodel_DdsTopicQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsTopicQosProfile72", type=ddsMetamodel_DdsDestinationOrderQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
historyQos73: BinaryAssociation = BinaryAssociation(
    name="historyQos73",
    ends={
        Property(name="ddsMetamodel_DdsHistoryQos", type=ddsMetamodel_DdsTopicQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsTopicQosProfile74", type=ddsMetamodel_DdsHistoryQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceLimitsQos75: BinaryAssociation = BinaryAssociation(
    name="resourceLimitsQos75",
    ends={
        Property(name="ddsMetamodel_DdsResourceLimits", type=ddsMetamodel_DdsTopicQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsTopicQosProfile76", type=ddsMetamodel_DdsResourceLimits, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transportPriorityQos77: BinaryAssociation = BinaryAssociation(
    name="transportPriorityQos77",
    ends={
        Property(name="ddsMetamodel_DdsTransportPriorityQos", type=ddsMetamodel_DdsTopicQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsTopicQosProfile78", type=ddsMetamodel_DdsTransportPriorityQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lifespanQos79: BinaryAssociation = BinaryAssociation(
    name="lifespanQos79",
    ends={
        Property(name="ddsMetamodel_DdsLifespan", type=ddsMetamodel_DdsTopicQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsTopicQosProfile80", type=ddsMetamodel_DdsLifespan, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
deadlineQos81: BinaryAssociation = BinaryAssociation(
    name="deadlineQos81",
    ends={
        Property(name="ddsMetamodel_DdsDeadlineQos", type=ddsMetamodel_DdsTopicQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsTopicQosProfile82", type=ddsMetamodel_DdsDeadlineQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
livelinessQos65: BinaryAssociation = BinaryAssociation(
    name="livelinessQos65",
    ends={
        Property(name="ddsMetamodel_DdsLivelinessQos", type=ddsMetamodel_DdsTopicQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsTopicQosProfile66", type=ddsMetamodel_DdsLivelinessQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
service_cleanup_delay83: BinaryAssociation = BinaryAssociation(
    name="service_cleanup_delay83",
    ends={
        Property(name="ddsMetamodel_DdsDuration", type=ddsMetamodel_DdsDurabilityServiceQos, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDurabilityServiceQos84", type=ddsMetamodel_DdsDuration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
period85: BinaryAssociation = BinaryAssociation(
    name="period85",
    ends={
        Property(name="ddsMetamodel_DdsDuration87", type=ddsMetamodel_DdsDeadlineQos, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDeadlineQos86", type=ddsMetamodel_DdsDuration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
duration88: BinaryAssociation = BinaryAssociation(
    name="duration88",
    ends={
        Property(name="ddsMetamodel_DdsDuration90", type=ddsMetamodel_DdsLatencyBudgetQos, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsLatencyBudgetQos89", type=ddsMetamodel_DdsDuration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lease_duration91: BinaryAssociation = BinaryAssociation(
    name="lease_duration91",
    ends={
        Property(name="ddsMetamodel_DdsLivelinessQos92", type=ddsMetamodel_DdsDuration, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="ddsMetamodel_DdsDuration93", type=ddsMetamodel_DdsLivelinessQos, multiplicity=Multiplicity(1, 1))
    }
)
minimum_separation94: BinaryAssociation = BinaryAssociation(
    name="minimum_separation94",
    ends={
        Property(name="ddsMetamodel_DdsDuration95", type=ddsMetamodel_DdsTimeBasedFilterQos, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsTimeBasedFilterQos", type=ddsMetamodel_DdsDuration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
duration99: BinaryAssociation = BinaryAssociation(
    name="duration99",
    ends={
        Property(name="ddsMetamodel_DdsDuration101", type=ddsMetamodel_DdsLifespan, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsLifespan100", type=ddsMetamodel_DdsDuration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
max_blocking_time96: BinaryAssociation = BinaryAssociation(
    name="max_blocking_time96",
    ends={
        Property(name="ddsMetamodel_DdsDuration98", type=ddsMetamodel_DdsReliabilityQos, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsReliabilityQos97", type=ddsMetamodel_DdsDuration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
autopurge_suspended_samples_delay102: BinaryAssociation = BinaryAssociation(
    name="autopurge_suspended_samples_delay102",
    ends={
        Property(name="ddsMetamodel_DdsDuration103", type=ddsMetamodel_DdsDataWriterLifecycleQos, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataWriterLifecycleQos", type=ddsMetamodel_DdsDuration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
autounregister_instance_delay104: BinaryAssociation = BinaryAssociation(
    name="autounregister_instance_delay104",
    ends={
        Property(name="ddsMetamodel_DdsDuration106", type=ddsMetamodel_DdsDataWriterLifecycleQos, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataWriterLifecycleQos105", type=ddsMetamodel_DdsDuration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
autopurge_nowriters_samples_delay107: BinaryAssociation = BinaryAssociation(
    name="autopurge_nowriters_samples_delay107",
    ends={
        Property(name="ddsMetamodel_DdsDataReaderLifecycleQos", type=ddsMetamodel_DdsDuration, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="ddsMetamodel_DdsDuration108", type=ddsMetamodel_DdsDataReaderLifecycleQos, multiplicity=Multiplicity(1, 1))
    }
)
autopurge_disposed_samples_delay109: BinaryAssociation = BinaryAssociation(
    name="autopurge_disposed_samples_delay109",
    ends={
        Property(name="ddsMetamodel_DdsDuration111", type=ddsMetamodel_DdsDataReaderLifecycleQos, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataReaderLifecycleQos110", type=ddsMetamodel_DdsDuration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
groupDataQos112: BinaryAssociation = BinaryAssociation(
    name="groupDataQos112",
    ends={
        Property(name="ddsMetamodel_DdsGroupDataQos", type=ddsMetamodel_DdsPublisherQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsPublisherQosProfile113", type=ddsMetamodel_DdsGroupDataQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entityFactoryQos114: BinaryAssociation = BinaryAssociation(
    name="entityFactoryQos114",
    ends={
        Property(name="ddsMetamodel_DdsEntityFactoryQos116", type=ddsMetamodel_DdsPublisherQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsPublisherQosProfile115", type=ddsMetamodel_DdsEntityFactoryQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
presentationQos117: BinaryAssociation = BinaryAssociation(
    name="presentationQos117",
    ends={
        Property(name="ddsMetamodel_DdsPresentationQos", type=ddsMetamodel_DdsPublisherQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsPublisherQosProfile118", type=ddsMetamodel_DdsPresentationQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
partitionQos119: BinaryAssociation = BinaryAssociation(
    name="partitionQos119",
    ends={
        Property(name="ddsMetamodel_DdsPartitionQos", type=ddsMetamodel_DdsPublisherQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsPublisherQosProfile120", type=ddsMetamodel_DdsPartitionQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
userDataQos121: BinaryAssociation = BinaryAssociation(
    name="userDataQos121",
    ends={
        Property(name="ddsMetamodel_DdsUserDataQos123", type=ddsMetamodel_DdsDataWriterQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataWriterQosProfile122", type=ddsMetamodel_DdsUserDataQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
durabilityQos124: BinaryAssociation = BinaryAssociation(
    name="durabilityQos124",
    ends={
        Property(name="ddsMetamodel_DdsDurabilityQos126", type=ddsMetamodel_DdsDataWriterQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataWriterQosProfile125", type=ddsMetamodel_DdsDurabilityQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
deadlineQos127: BinaryAssociation = BinaryAssociation(
    name="deadlineQos127",
    ends={
        Property(name="ddsMetamodel_DdsDeadlineQos129", type=ddsMetamodel_DdsDataWriterQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataWriterQosProfile128", type=ddsMetamodel_DdsDeadlineQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
latencyBudgetQos130: BinaryAssociation = BinaryAssociation(
    name="latencyBudgetQos130",
    ends={
        Property(name="ddsMetamodel_DdsLatencyBudgetQos132", type=ddsMetamodel_DdsDataWriterQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataWriterQosProfile131", type=ddsMetamodel_DdsLatencyBudgetQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownershipStrength136: BinaryAssociation = BinaryAssociation(
    name="ownershipStrength136",
    ends={
        Property(name="ddsMetamodel_DdsOwnershipStrengthQos", type=ddsMetamodel_DdsDataWriterQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataWriterQosProfile137", type=ddsMetamodel_DdsOwnershipStrengthQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
livelinessQos138: BinaryAssociation = BinaryAssociation(
    name="livelinessQos138",
    ends={
        Property(name="ddsMetamodel_DdsLivelinessQos140", type=ddsMetamodel_DdsDataWriterQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataWriterQosProfile139", type=ddsMetamodel_DdsLivelinessQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reliabilityQos141: BinaryAssociation = BinaryAssociation(
    name="reliabilityQos141",
    ends={
        Property(name="ddsMetamodel_DdsReliabilityQos143", type=ddsMetamodel_DdsDataWriterQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataWriterQosProfile142", type=ddsMetamodel_DdsReliabilityQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transportPriorityQos144: BinaryAssociation = BinaryAssociation(
    name="transportPriorityQos144",
    ends={
        Property(name="ddsMetamodel_DdsTransportPriorityQos146", type=ddsMetamodel_DdsDataWriterQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataWriterQosProfile145", type=ddsMetamodel_DdsTransportPriorityQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownershipQos133: BinaryAssociation = BinaryAssociation(
    name="ownershipQos133",
    ends={
        Property(name="ddsMetamodel_DdsOwnershipQos135", type=ddsMetamodel_DdsDataWriterQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataWriterQosProfile134", type=ddsMetamodel_DdsOwnershipQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
destinationOrderQos150: BinaryAssociation = BinaryAssociation(
    name="destinationOrderQos150",
    ends={
        Property(name="ddsMetamodel_DdsDestinationOrderQos152", type=ddsMetamodel_DdsDataWriterQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataWriterQosProfile151", type=ddsMetamodel_DdsDestinationOrderQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
historyQos153: BinaryAssociation = BinaryAssociation(
    name="historyQos153",
    ends={
        Property(name="ddsMetamodel_DdsHistoryQos155", type=ddsMetamodel_DdsDataWriterQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataWriterQosProfile154", type=ddsMetamodel_DdsHistoryQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceLimitsQos156: BinaryAssociation = BinaryAssociation(
    name="resourceLimitsQos156",
    ends={
        Property(name="ddsMetamodel_DdsResourceLimits158", type=ddsMetamodel_DdsDataWriterQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataWriterQosProfile157", type=ddsMetamodel_DdsResourceLimits, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dataWriterLifecycleQos159: BinaryAssociation = BinaryAssociation(
    name="dataWriterLifecycleQos159",
    ends={
        Property(name="ddsMetamodel_DdsDataWriterLifecycleQos161", type=ddsMetamodel_DdsDataWriterQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataWriterQosProfile160", type=ddsMetamodel_DdsDataWriterLifecycleQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lifespanQos147: BinaryAssociation = BinaryAssociation(
    name="lifespanQos147",
    ends={
        Property(name="ddsMetamodel_DdsLifespan149", type=ddsMetamodel_DdsDataWriterQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataWriterQosProfile148", type=ddsMetamodel_DdsLifespan, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entityFactoryQos165: BinaryAssociation = BinaryAssociation(
    name="entityFactoryQos165",
    ends={
        Property(name="ddsMetamodel_DdsEntityFactoryQos167", type=ddsMetamodel_DdsSubscriberQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsSubscriberQosProfile166", type=ddsMetamodel_DdsEntityFactoryQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
presentationQos168: BinaryAssociation = BinaryAssociation(
    name="presentationQos168",
    ends={
        Property(name="ddsMetamodel_DdsPresentationQos170", type=ddsMetamodel_DdsSubscriberQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsSubscriberQosProfile169", type=ddsMetamodel_DdsPresentationQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
partitionQos171: BinaryAssociation = BinaryAssociation(
    name="partitionQos171",
    ends={
        Property(name="ddsMetamodel_DdsPartitionQos173", type=ddsMetamodel_DdsSubscriberQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsSubscriberQosProfile172", type=ddsMetamodel_DdsPartitionQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
userDataQos174: BinaryAssociation = BinaryAssociation(
    name="userDataQos174",
    ends={
        Property(name="ddsMetamodel_DdsUserDataQos176", type=ddsMetamodel_DdsDataReaderQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataReaderQosProfile175", type=ddsMetamodel_DdsUserDataQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
durabilityQos177: BinaryAssociation = BinaryAssociation(
    name="durabilityQos177",
    ends={
        Property(name="ddsMetamodel_DdsDurabilityQos179", type=ddsMetamodel_DdsDataReaderQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataReaderQosProfile178", type=ddsMetamodel_DdsDurabilityQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
deadlineQos180: BinaryAssociation = BinaryAssociation(
    name="deadlineQos180",
    ends={
        Property(name="ddsMetamodel_DdsDeadlineQos182", type=ddsMetamodel_DdsDataReaderQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataReaderQosProfile181", type=ddsMetamodel_DdsDeadlineQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
latencyBudgetQos183: BinaryAssociation = BinaryAssociation(
    name="latencyBudgetQos183",
    ends={
        Property(name="ddsMetamodel_DdsLatencyBudgetQos185", type=ddsMetamodel_DdsDataReaderQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataReaderQosProfile184", type=ddsMetamodel_DdsLatencyBudgetQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
livelinessQos186: BinaryAssociation = BinaryAssociation(
    name="livelinessQos186",
    ends={
        Property(name="ddsMetamodel_DdsLivelinessQos188", type=ddsMetamodel_DdsDataReaderQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataReaderQosProfile187", type=ddsMetamodel_DdsLivelinessQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeBasedFilterQos192: BinaryAssociation = BinaryAssociation(
    name="timeBasedFilterQos192",
    ends={
        Property(name="ddsMetamodel_DdsTimeBasedFilterQos194", type=ddsMetamodel_DdsDataReaderQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataReaderQosProfile193", type=ddsMetamodel_DdsTimeBasedFilterQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
groupDataQos162: BinaryAssociation = BinaryAssociation(
    name="groupDataQos162",
    ends={
        Property(name="ddsMetamodel_DdsGroupDataQos164", type=ddsMetamodel_DdsSubscriberQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsSubscriberQosProfile163", type=ddsMetamodel_DdsGroupDataQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reliabilityQos195: BinaryAssociation = BinaryAssociation(
    name="reliabilityQos195",
    ends={
        Property(name="ddsMetamodel_DdsReliabilityQos197", type=ddsMetamodel_DdsDataReaderQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataReaderQosProfile196", type=ddsMetamodel_DdsReliabilityQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
destinationOrderQos198: BinaryAssociation = BinaryAssociation(
    name="destinationOrderQos198",
    ends={
        Property(name="ddsMetamodel_DdsDestinationOrderQos200", type=ddsMetamodel_DdsDataReaderQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataReaderQosProfile199", type=ddsMetamodel_DdsDestinationOrderQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
historyQos201: BinaryAssociation = BinaryAssociation(
    name="historyQos201",
    ends={
        Property(name="ddsMetamodel_DdsHistoryQos203", type=ddsMetamodel_DdsDataReaderQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataReaderQosProfile202", type=ddsMetamodel_DdsHistoryQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceLimitsQos204: BinaryAssociation = BinaryAssociation(
    name="resourceLimitsQos204",
    ends={
        Property(name="ddsMetamodel_DdsResourceLimits206", type=ddsMetamodel_DdsDataReaderQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataReaderQosProfile205", type=ddsMetamodel_DdsResourceLimits, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dataReaderLifecycleQos207: BinaryAssociation = BinaryAssociation(
    name="dataReaderLifecycleQos207",
    ends={
        Property(name="ddsMetamodel_DdsDataReaderLifecycleQos209", type=ddsMetamodel_DdsDataReaderQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataReaderQosProfile208", type=ddsMetamodel_DdsDataReaderLifecycleQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownershipQos189: BinaryAssociation = BinaryAssociation(
    name="ownershipQos189",
    ends={
        Property(name="ddsMetamodel_DdsOwnershipQos191", type=ddsMetamodel_DdsDataReaderQosProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataReaderQosProfile190", type=ddsMetamodel_DdsOwnershipQos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
readConditions210: BinaryAssociation = BinaryAssociation(
    name="readConditions210",
    ends={
        Property(name="ddsMetamodel_DdsReadCondition", type=ddsMetamodel_DdsWaitSet, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsWaitSet211", type=ddsMetamodel_DdsReadCondition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statusConditions212: BinaryAssociation = BinaryAssociation(
    name="statusConditions212",
    ends={
        Property(name="DdsStatusCondition", type=ddsMetamodel_DdsWaitSet, multiplicity=Multiplicity(1, 1)),
        Property(name="containingWaitset", type=ddsMetamodel_DdsStatusCondition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataReader215: BinaryAssociation = BinaryAssociation(
    name="dataReader215",
    ends={
        Property(name="ddsMetamodel_DdsDataReader217", type=ddsMetamodel_DdsReadCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsReadCondition216", type=ddsMetamodel_DdsDataReader, multiplicity=Multiplicity(0, 1))
    }
)
referencedType218: BinaryAssociation = BinaryAssociation(
    name="referencedType218",
    ends={
        Property(name="ddsMetamodel_DdsDataStructure219", type=ddsMetamodel_DdsStructuredField, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsStructuredField", type=ddsMetamodel_DdsDataStructure, multiplicity=Multiplicity(0, 1))
    }
)
guardConditions213: BinaryAssociation = BinaryAssociation(
    name="guardConditions213",
    ends={
        Property(name="ddsMetamodel_GuardCondition", type=ddsMetamodel_DdsWaitSet, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsWaitSet214", type=ddsMetamodel_GuardCondition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataStructure220: BinaryAssociation = BinaryAssociation(
    name="dataStructure220",
    ends={
        Property(name="DdsDataStructure221", type=ddsMetamodel_DdsStructuredField, multiplicity=Multiplicity(1, 1)),
        Property(name="structuredFields", type=ddsMetamodel_DdsDataStructure, multiplicity=Multiplicity(0, 1))
    }
)
containingWaitset222: BinaryAssociation = BinaryAssociation(
    name="containingWaitset222",
    ends={
        Property(name="DdsWaitSet", type=ddsMetamodel_DdsStatusCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="statusConditions", type=ddsMetamodel_DdsWaitSet, multiplicity=Multiplicity(0, 1))
    }
)
domainParticipant223: BinaryAssociation = BinaryAssociation(
    name="domainParticipant223",
    ends={
        Property(name="ddsMetamodel_DdsDomainParticipant224", type=ddsMetamodel_DdsDomainParticipantStatusCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDomainParticipantStatusCondition", type=ddsMetamodel_DdsDomainParticipant, multiplicity=Multiplicity(1, 1))
    }
)
publisher225: BinaryAssociation = BinaryAssociation(
    name="publisher225",
    ends={
        Property(name="ddsMetamodel_DdsPublisher226", type=ddsMetamodel_DdsPublisherStatusCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsPublisherStatusCondition", type=ddsMetamodel_DdsPublisher, multiplicity=Multiplicity(1, 1))
    }
)
dataWriter229: BinaryAssociation = BinaryAssociation(
    name="dataWriter229",
    ends={
        Property(name="ddsMetamodel_DdsDataWriter230", type=ddsMetamodel_DdsDataWriterStatusCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataWriterStatusCondition", type=ddsMetamodel_DdsDataWriter, multiplicity=Multiplicity(1, 1))
    }
)
dataReader231: BinaryAssociation = BinaryAssociation(
    name="dataReader231",
    ends={
        Property(name="ddsMetamodel_DdsDataReader232", type=ddsMetamodel_DdsDataReaderStatusCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsDataReaderStatusCondition", type=ddsMetamodel_DdsDataReader, multiplicity=Multiplicity(1, 1))
    }
)
topic233: BinaryAssociation = BinaryAssociation(
    name="topic233",
    ends={
        Property(name="ddsMetamodel_DdsTopic234", type=ddsMetamodel_DdsTopicStatusCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsTopicStatusCondition", type=ddsMetamodel_DdsTopic, multiplicity=Multiplicity(1, 1))
    }
)
subscriber227: BinaryAssociation = BinaryAssociation(
    name="subscriber227",
    ends={
        Property(name="ddsMetamodel_DdsSubscriber228", type=ddsMetamodel_DdsSubscriberStatusCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsSubscriberStatusCondition", type=ddsMetamodel_DdsSubscriber, multiplicity=Multiplicity(1, 1))
    }
)
hosts235: BinaryAssociation = BinaryAssociation(
    name="hosts235",
    ends={
        Property(name="ddsMetamodel_DdsHost", type=ddsMetamodel_DdsSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsSystem", type=ddsMetamodel_DdsHost, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qosProfiles236: BinaryAssociation = BinaryAssociation(
    name="qosProfiles236",
    ends={
        Property(name="ddsMetamodel_DdsQosProfile", type=ddsMetamodel_DdsSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsSystem237", type=ddsMetamodel_DdsQosProfile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataModules238: BinaryAssociation = BinaryAssociation(
    name="dataModules238",
    ends={
        Property(name="DdsDataModule239", type=ddsMetamodel_DdsSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="containingSystem", type=ddsMetamodel_DdsDataModule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
topics240: BinaryAssociation = BinaryAssociation(
    name="topics240",
    ends={
        Property(name="ddsMetamodel_DdsTopic242", type=ddsMetamodel_DdsSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsSystem241", type=ddsMetamodel_DdsTopic, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
applications243: BinaryAssociation = BinaryAssociation(
    name="applications243",
    ends={
        Property(name="ddsMetamodel_DdsApplication245", type=ddsMetamodel_DdsHost, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsMetamodel_DdsHost244", type=ddsMetamodel_DdsApplication, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_ddsMetamodel_DdsDomainParticipantQosProfile_DdsQosProfile = Generalization(general=DdsQosProfile, specific=ddsMetamodel_DdsDomainParticipantQosProfile)
gen_ddsMetamodel_DdsTopicQosProfile_DdsQosProfile = Generalization(general=DdsQosProfile, specific=ddsMetamodel_DdsTopicQosProfile)
gen_ddsMetamodel_DdsPublisherQosProfile_DdsQosProfile = Generalization(general=DdsQosProfile, specific=ddsMetamodel_DdsPublisherQosProfile)
gen_ddsMetamodel_DdsDataWriterQosProfile_DdsQosProfile = Generalization(general=DdsQosProfile, specific=ddsMetamodel_DdsDataWriterQosProfile)
gen_ddsMetamodel_DdsSubscriberQosProfile_DdsQosProfile = Generalization(general=DdsQosProfile, specific=ddsMetamodel_DdsSubscriberQosProfile)
gen_ddsMetamodel_DdsDataReaderQosProfile_DdsQosProfile = Generalization(general=DdsQosProfile, specific=ddsMetamodel_DdsDataReaderQosProfile)
gen_ddsMetamodel_DdsPublisherStatusCondition_DdsStatusCondition = Generalization(general=DdsStatusCondition, specific=ddsMetamodel_DdsPublisherStatusCondition)
gen_ddsMetamodel_DdsSubscriberStatusCondition_DdsStatusCondition = Generalization(general=DdsStatusCondition, specific=ddsMetamodel_DdsSubscriberStatusCondition)
gen_ddsMetamodel_DdsDomainParticipantStatusCondition_DdsStatusCondition = Generalization(general=DdsStatusCondition, specific=ddsMetamodel_DdsDomainParticipantStatusCondition)
gen_ddsMetamodel_DdsDataWriterStatusCondition_DdsStatusCondition = Generalization(general=DdsStatusCondition, specific=ddsMetamodel_DdsDataWriterStatusCondition)
gen_ddsMetamodel_DdsDataReaderStatusCondition_DdsStatusCondition = Generalization(general=DdsStatusCondition, specific=ddsMetamodel_DdsDataReaderStatusCondition)
gen_ddsMetamodel_DdsTopicStatusCondition_DdsStatusCondition = Generalization(general=DdsStatusCondition, specific=ddsMetamodel_DdsTopicStatusCondition)
gen_ddsMetamodel_QueryCondition_DdsReadCondition = Generalization(general=DdsReadCondition, specific=ddsMetamodel_QueryCondition)

# Domain Model
domain_model = DomainModel(
    name="ddsMetamodel",
    types={ddsMetamodel_DdsApplication, ddsMetamodel_DdsDomainParticipant, ddsMetamodel_DdsWaitSet, ddsMetamodel_DdsSubscriber, ddsMetamodel_DdsPublisher, ddsMetamodel_DdsTopic, ddsMetamodel_DdsTopicListener, ddsMetamodel_DdsTopicQosProfile, ddsMetamodel_DdsDataStructure, ddsMetamodel_DdsQosProfile, ddsMetamodel_DdsDataReader, ddsMetamodel_DdsSubscriberListener, ddsMetamodel_DdsSubscriberQosProfile, ddsMetamodel_DdsDomainParticipantQosProfile, ddsMetamodel_DdsDomainParticipantListener, ddsMetamodel_DdsDataReaderListener, ddsMetamodel_DdsDataReaderQosProfile, ddsMetamodel_DdsDataWriter, ddsMetamodel_DdsPublisherListener, ddsMetamodel_DdsPublisherQosProfile, ddsMetamodel_DdsDataModule, ddsMetamodel_DdsSystem, ddsMetamodel_DdsDataField, ddsMetamodel_DdsStructuredField, ddsMetamodel_DdsDataWriterListener, ddsMetamodel_DdsDataWriterQosProfile, DdsQosProfile, ddsMetamodel_DdsUserDataQos, ddsMetamodel_DdsEntityFactoryQos, ddsMetamodel_DdsTopicDataQos, ddsMetamodel_DdsDurabilityQos, ddsMetamodel_DdsDurabilityServiceQos, ddsMetamodel_DdsLatencyBudgetQos, ddsMetamodel_DdsReliabilityQos, ddsMetamodel_DdsDestinationOrderQos, ddsMetamodel_DdsHistoryQos, ddsMetamodel_DdsResourceLimits, ddsMetamodel_DdsTransportPriorityQos, ddsMetamodel_DdsLifespan, ddsMetamodel_DdsDeadlineQos, ddsMetamodel_DdsLivelinessQos, ddsMetamodel_DdsOwnershipQos, ddsMetamodel_DdsDuration, ddsMetamodel_DdsPresentationQos, ddsMetamodel_DdsOwnershipStrengthQos, ddsMetamodel_DdsTimeBasedFilterQos, ddsMetamodel_DdsPartitionQos, ddsMetamodel_DdsDataWriterLifecycleQos, ddsMetamodel_DdsDataReaderLifecycleQos, ddsMetamodel_DdsGroupDataQos, ddsMetamodel_DdsReadCondition, ddsMetamodel_DdsStatusCondition, ddsMetamodel_GuardCondition, ddsMetamodel_DdsPublisherStatusCondition, ddsMetamodel_DdsSubscriberStatusCondition, ddsMetamodel_DdsDomainParticipantStatusCondition, DdsStatusCondition, ddsMetamodel_DdsDataReaderStatusCondition, ddsMetamodel_DdsTopicStatusCondition, ddsMetamodel_QueryCondition, DdsReadCondition, ddsMetamodel_DdsDataWriterStatusCondition, ddsMetamodel_DdsHost, DurabilityQosPolicyKind, HistoryQosPolicyKind, PresentationQosPolicyAccessScopeKind, OwnershipQosPolicyKind, LivelinessQosPolicyKind, ReliabilityQosPolicyKind, DestinationOrderQosPolicyKind, InvalidSampleVisibilityQosPolicy, ViewStateKind, InstanceStateKind, SampleStateKind, DomainParticipantStatus, SubscriberStatus, PublisherStatus, DataWriterStatus, DataReaderStatus, TopicStatus},
    associations={domainParticipants0, waitset1, ddssubscriber3, ddspublisher5, topicListener11, topicQosProfile12, ddsdatastructure14, ddsdatareader16, subscriberListener17, subscriberQosProfile19, ddsdomainparticipantqosprofile7, domainParticipantListener9, dataReaderListener23, dataReaderQosProfile25, containingSubscriber27, ddsdatawriter28, publisherListener30, publisherQosProfile32, publiableTopic34, readableTopic21, dataStructures41, innerModules43, containingSystem44, containingModule46, fields48, structuredFields50, containerDataModule51, dataWriterListener37, dataWriterQosProfile39, userDataQos53, entityFactoryQos55, topicDataQos57, durabilityQos59, durabilityServiceQos61, latencyBudgetQos63, ownershipQos67, reliabilityQos69, destinationOrderQos71, historyQos73, resourceLimitsQos75, transportPriorityQos77, lifespanQos79, deadlineQos81, livelinessQos65, service_cleanup_delay83, period85, duration88, lease_duration91, minimum_separation94, duration99, max_blocking_time96, autopurge_suspended_samples_delay102, autounregister_instance_delay104, autopurge_nowriters_samples_delay107, autopurge_disposed_samples_delay109, groupDataQos112, entityFactoryQos114, presentationQos117, partitionQos119, userDataQos121, durabilityQos124, deadlineQos127, latencyBudgetQos130, ownershipStrength136, livelinessQos138, reliabilityQos141, transportPriorityQos144, ownershipQos133, destinationOrderQos150, historyQos153, resourceLimitsQos156, dataWriterLifecycleQos159, lifespanQos147, entityFactoryQos165, presentationQos168, partitionQos171, userDataQos174, durabilityQos177, deadlineQos180, latencyBudgetQos183, livelinessQos186, timeBasedFilterQos192, groupDataQos162, reliabilityQos195, destinationOrderQos198, historyQos201, resourceLimitsQos204, dataReaderLifecycleQos207, ownershipQos189, readConditions210, statusConditions212, dataReader215, referencedType218, guardConditions213, dataStructure220, containingWaitset222, domainParticipant223, publisher225, dataWriter229, dataReader231, topic233, subscriber227, hosts235, qosProfiles236, dataModules238, topics240, applications243},
    generalizations={gen_ddsMetamodel_DdsDomainParticipantQosProfile_DdsQosProfile, gen_ddsMetamodel_DdsTopicQosProfile_DdsQosProfile, gen_ddsMetamodel_DdsPublisherQosProfile_DdsQosProfile, gen_ddsMetamodel_DdsDataWriterQosProfile_DdsQosProfile, gen_ddsMetamodel_DdsSubscriberQosProfile_DdsQosProfile, gen_ddsMetamodel_DdsDataReaderQosProfile_DdsQosProfile, gen_ddsMetamodel_DdsPublisherStatusCondition_DdsStatusCondition, gen_ddsMetamodel_DdsSubscriberStatusCondition_DdsStatusCondition, gen_ddsMetamodel_DdsDomainParticipantStatusCondition_DdsStatusCondition, gen_ddsMetamodel_DdsDataWriterStatusCondition_DdsStatusCondition, gen_ddsMetamodel_DdsDataReaderStatusCondition_DdsStatusCondition, gen_ddsMetamodel_DdsTopicStatusCondition_DdsStatusCondition, gen_ddsMetamodel_QueryCondition_DdsReadCondition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)