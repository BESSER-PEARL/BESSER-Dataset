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
dcps_PublisherSubscriber = Class(name="dcps::PublisherSubscriber", is_abstract=True)
dcps_Domain = Class(name="dcps::Domain")
Entity = Class(name="Entity")
dcps_DomainParticipant = Class(name="dcps::DomainParticipant")
DomainEntity = Class(name="DomainEntity")
dcps_Publisher = Class(name="dcps::Publisher")
dcps_Subscriber = Class(name="dcps::Subscriber")
dcps_EntityFactoryQosPolicy = Class(name="dcps::EntityFactoryQosPolicy")
dcps_UserDataQosPolicy = Class(name="dcps::UserDataQosPolicy")
dcps_GroupDataQosPolicy = Class(name="dcps::GroupDataQosPolicy")
dcps_PresentationQosPolicy = Class(name="dcps::PresentationQosPolicy")
dcps_PartitionQosPolicy = Class(name="dcps::PartitionQosPolicy")
PublisherSubscriber = Class(name="PublisherSubscriber")
dcps_DataReader = Class(name="dcps::DataReader")
dcps_DataWriter = Class(name="dcps::DataWriter")
dcps_DataReaderWriter = Class(name="dcps::DataReaderWriter", is_abstract=True)
dcps_DeadlineQosPolicy = Class(name="dcps::DeadlineQosPolicy")
dcps_DestinationOrderQosPolicy = Class(name="dcps::DestinationOrderQosPolicy")
dcps_DurabilityQosPolicy = Class(name="dcps::DurabilityQosPolicy")
dcps_HistoryQosPolicy = Class(name="dcps::HistoryQosPolicy")
dcps_LatencyBudgetQosPolicy = Class(name="dcps::LatencyBudgetQosPolicy")
dcps_LivelinessQosPolicy = Class(name="dcps::LivelinessQosPolicy")
dcps_OwnershipQosPolicy = Class(name="dcps::OwnershipQosPolicy")
dcps_ReliabilityQosPolicy = Class(name="dcps::ReliabilityQosPolicy")
dcps_ResourceLimitsQosPolicy = Class(name="dcps::ResourceLimitsQosPolicy")
DataReaderWriter = Class(name="DataReaderWriter")
dcps_ReaderDataLifecycleQosPolicy = Class(name="dcps::ReaderDataLifecycleQosPolicy")
dcps_TimeBasedFilterQosPolicy = Class(name="dcps::TimeBasedFilterQosPolicy")
dcps_TopicDescription = Class(name="dcps::TopicDescription")
dcps_DurabilityServiceQosPolicy = Class(name="dcps::DurabilityServiceQosPolicy")
dcps_OwnershipStrengthQosPolicy = Class(name="dcps::OwnershipStrengthQosPolicy")
dcps_TransportPriorityQosPolicy = Class(name="dcps::TransportPriorityQosPolicy")
dcps_WriterDataLifecycleQosPolicy = Class(name="dcps::WriterDataLifecycleQosPolicy")
dcps_LifespanQosPolicy = Class(name="dcps::LifespanQosPolicy")
dcps_Topic = Class(name="dcps::Topic")

# dcps_PublisherSubscriber class attributes and methods
dcps_PublisherSubscriber_transportId: Property = Property(name="transportId", type=IntegerType)
dcps_PublisherSubscriber.attributes={dcps_PublisherSubscriber_transportId}

# dcps_Domain class attributes and methods
dcps_Domain_domainId: Property = Property(name="domainId", type=StringType)
dcps_Domain.attributes={dcps_Domain_domainId}

# Entity class attributes and methods

# dcps_DomainParticipant class attributes and methods

# DomainEntity class attributes and methods

# dcps_Publisher class attributes and methods

# dcps_Subscriber class attributes and methods

# dcps_EntityFactoryQosPolicy class attributes and methods

# dcps_UserDataQosPolicy class attributes and methods

# dcps_GroupDataQosPolicy class attributes and methods

# dcps_PresentationQosPolicy class attributes and methods

# dcps_PartitionQosPolicy class attributes and methods

# PublisherSubscriber class attributes and methods

# dcps_DataReader class attributes and methods

# dcps_DataWriter class attributes and methods

# dcps_DataReaderWriter class attributes and methods
dcps_DataReaderWriter_copyFromTopicQos: Property = Property(name="copyFromTopicQos", type=BooleanType)
dcps_DataReaderWriter.attributes={dcps_DataReaderWriter_copyFromTopicQos}

# dcps_DeadlineQosPolicy class attributes and methods

# dcps_DestinationOrderQosPolicy class attributes and methods

# dcps_DurabilityQosPolicy class attributes and methods

# dcps_HistoryQosPolicy class attributes and methods

# dcps_LatencyBudgetQosPolicy class attributes and methods

# dcps_LivelinessQosPolicy class attributes and methods

# dcps_OwnershipQosPolicy class attributes and methods

# dcps_ReliabilityQosPolicy class attributes and methods

# dcps_ResourceLimitsQosPolicy class attributes and methods

# DataReaderWriter class attributes and methods

# dcps_ReaderDataLifecycleQosPolicy class attributes and methods

# dcps_TimeBasedFilterQosPolicy class attributes and methods

# dcps_TopicDescription class attributes and methods

# dcps_DurabilityServiceQosPolicy class attributes and methods

# dcps_OwnershipStrengthQosPolicy class attributes and methods

# dcps_TransportPriorityQosPolicy class attributes and methods

# dcps_WriterDataLifecycleQosPolicy class attributes and methods

# dcps_LifespanQosPolicy class attributes and methods

# dcps_Topic class attributes and methods

# Relationships
domain0: BinaryAssociation = BinaryAssociation(
    name="domain0",
    ends={
        Property(name="dcps_Domain", type=dcps_DomainParticipant, multiplicity=Multiplicity(1, 1)),
        Property(name="dcps_DomainParticipant", type=dcps_Domain, multiplicity=Multiplicity(1, 1))
    }
)
publishers1: BinaryAssociation = BinaryAssociation(
    name="publishers1",
    ends={
        Property(name="dcps_Publisher", type=dcps_DomainParticipant, multiplicity=Multiplicity(1, 1)),
        Property(name="dcps_DomainParticipant2", type=dcps_Publisher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subscribers3: BinaryAssociation = BinaryAssociation(
    name="subscribers3",
    ends={
        Property(name="dcps_Subscriber", type=dcps_DomainParticipant, multiplicity=Multiplicity(1, 1)),
        Property(name="dcps_DomainParticipant4", type=dcps_Subscriber, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entity_factory5: BinaryAssociation = BinaryAssociation(
    name="entity_factory5",
    ends={
        Property(name="dcps_EntityFactoryQosPolicy", type=dcps_DomainParticipant, multiplicity=Multiplicity(1, 1)),
        Property(name="dcps_DomainParticipant6", type=dcps_EntityFactoryQosPolicy, multiplicity=Multiplicity(0, 1))
    }
)
user_data7: BinaryAssociation = BinaryAssociation(
    name="user_data7",
    ends={
        Property(name="dcps_UserDataQosPolicy", type=dcps_DomainParticipant, multiplicity=Multiplicity(1, 1)),
        Property(name="dcps_DomainParticipant8", type=dcps_UserDataQosPolicy, multiplicity=Multiplicity(0, 1))
    }
)
entity_factory9: BinaryAssociation = BinaryAssociation(
    name="entity_factory9",
    ends={
        Property(name="dcps_EntityFactoryQosPolicy10", type=dcps_PublisherSubscriber, multiplicity=Multiplicity(1, 1)),
        Property(name="dcps_PublisherSubscriber", type=dcps_EntityFactoryQosPolicy, multiplicity=Multiplicity(0, 1))
    }
)
group_data11: BinaryAssociation = BinaryAssociation(
    name="group_data11",
    ends={
        Property(name="dcps_GroupDataQosPolicy", type=dcps_PublisherSubscriber, multiplicity=Multiplicity(1, 1)),
        Property(name="dcps_PublisherSubscriber12", type=dcps_GroupDataQosPolicy, multiplicity=Multiplicity(0, 1))
    }
)
presentation13: BinaryAssociation = BinaryAssociation(
    name="presentation13",
    ends={
        Property(name="dcps_PresentationQosPolicy", type=dcps_PublisherSubscriber, multiplicity=Multiplicity(1, 1)),
        Property(name="dcps_PublisherSubscriber14", type=dcps_PresentationQosPolicy, multiplicity=Multiplicity(0, 1))
    }
)
partition15: BinaryAssociation = BinaryAssociation(
    name="partition15",
    ends={
        Property(name="dcps_PartitionQosPolicy", type=dcps_PublisherSubscriber, multiplicity=Multiplicity(1, 1)),
        Property(name="dcps_PublisherSubscriber16", type=dcps_PartitionQosPolicy, multiplicity=Multiplicity(0, 1))
    }
)
readers17: BinaryAssociation = BinaryAssociation(
    name="readers17",
    ends={
        Property(name="dcps_DataReader", type=dcps_Subscriber, multiplicity=Multiplicity(1, 1)),
        Property(name="dcps_Subscriber18", type=dcps_DataReader, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
writers19: BinaryAssociation = BinaryAssociation(
    name="writers19",
    ends={
        Property(name="dcps_DataWriter", type=dcps_Publisher, multiplicity=Multiplicity(1, 1)),
        Property(name="dcps_Publisher20", type=dcps_DataWriter, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
deadline21: BinaryAssociation = BinaryAssociation(
    name="deadline21",
    ends={
        Property(name="dcps_DeadlineQosPolicy", type=dcps_DataReaderWriter, multiplicity=Multiplicity(1, 1)),
        Property(name="dcps_DataReaderWriter", type=dcps_DeadlineQosPolicy, multiplicity=Multiplicity(0, 1))
    }
)
destination_order22: BinaryAssociation = BinaryAssociation(
    name="destination_order22",
    ends={
        Property(name="dcps_DestinationOrderQosPolicy", type=dcps_DataReaderWriter, multiplicity=Multiplicity(1, 1)),
        Property(name="dcps_DataReaderWriter23", type=dcps_DestinationOrderQosPolicy, multiplicity=Multiplicity(0, 1))
    }
)
durability24: BinaryAssociation = BinaryAssociation(
    name="durability24",
    ends={
        Property(name="dcps_DurabilityQosPolicy", type=dcps_DataReaderWriter, multiplicity=Multiplicity(1, 1)),
        Property(name="dcps_DataReaderWriter25", type=dcps_DurabilityQosPolicy, multiplicity=Multiplicity(0, 1))
    }
)
history26: BinaryAssociation = BinaryAssociation(
    name="history26",
    ends={
        Property(name="dcps_HistoryQosPolicy", type=dcps_DataReaderWriter, multiplicity=Multiplicity(1, 1)),
        Property(name="dcps_DataReaderWriter27", type=dcps_HistoryQosPolicy, multiplicity=Multiplicity(0, 1))
    }
)
latency_budget28: BinaryAssociation = BinaryAssociation(
    name="latency_budget28",
    ends={
        Property(name="dcps_LatencyBudgetQosPolicy", type=dcps_DataReaderWriter, multiplicity=Multiplicity(1, 1)),
        Property(name="dcps_DataReaderWriter29", type=dcps_LatencyBudgetQosPolicy, multiplicity=Multiplicity(0, 1))
    }
)
liveliness30: BinaryAssociation = BinaryAssociation(
    name="liveliness30",
    ends={
        Property(name="dcps_LivelinessQosPolicy", type=dcps_DataReaderWriter, multiplicity=Multiplicity(1, 1)),
        Property(name="dcps_DataReaderWriter31", type=dcps_LivelinessQosPolicy, multiplicity=Multiplicity(0, 1))
    }
)
ownership32: BinaryAssociation = BinaryAssociation(
    name="ownership32",
    ends={
        Property(name="dcps_OwnershipQosPolicy", type=dcps_DataReaderWriter, multiplicity=Multiplicity(1, 1)),
        Property(name="dcps_DataReaderWriter33", type=dcps_OwnershipQosPolicy, multiplicity=Multiplicity(0, 1))
    }
)
reliability34: BinaryAssociation = BinaryAssociation(
    name="reliability34",
    ends={
        Property(name="dcps_ReliabilityQosPolicy", type=dcps_DataReaderWriter, multiplicity=Multiplicity(1, 1)),
        Property(name="dcps_DataReaderWriter35", type=dcps_ReliabilityQosPolicy, multiplicity=Multiplicity(0, 1))
    }
)
resource_limits36: BinaryAssociation = BinaryAssociation(
    name="resource_limits36",
    ends={
        Property(name="dcps_ResourceLimitsQosPolicy", type=dcps_DataReaderWriter, multiplicity=Multiplicity(1, 1)),
        Property(name="dcps_DataReaderWriter37", type=dcps_ResourceLimitsQosPolicy, multiplicity=Multiplicity(0, 1))
    }
)
user_data38: BinaryAssociation = BinaryAssociation(
    name="user_data38",
    ends={
        Property(name="dcps_UserDataQosPolicy40", type=dcps_DataReaderWriter, multiplicity=Multiplicity(1, 1)),
        Property(name="dcps_DataReaderWriter39", type=dcps_UserDataQosPolicy, multiplicity=Multiplicity(0, 1))
    }
)
reader_data_lifecycle41: BinaryAssociation = BinaryAssociation(
    name="reader_data_lifecycle41",
    ends={
        Property(name="dcps_ReaderDataLifecycleQosPolicy", type=dcps_DataReader, multiplicity=Multiplicity(1, 1)),
        Property(name="dcps_DataReader42", type=dcps_ReaderDataLifecycleQosPolicy, multiplicity=Multiplicity(0, 1))
    }
)
time_based_filter43: BinaryAssociation = BinaryAssociation(
    name="time_based_filter43",
    ends={
        Property(name="dcps_TimeBasedFilterQosPolicy", type=dcps_DataReader, multiplicity=Multiplicity(1, 1)),
        Property(name="dcps_DataReader44", type=dcps_TimeBasedFilterQosPolicy, multiplicity=Multiplicity(0, 1))
    }
)
topic45: BinaryAssociation = BinaryAssociation(
    name="topic45",
    ends={
        Property(name="dcps_TopicDescription", type=dcps_DataReader, multiplicity=Multiplicity(1, 1)),
        Property(name="dcps_DataReader46", type=dcps_TopicDescription, multiplicity=Multiplicity(1, 1))
    }
)
durability_service47: BinaryAssociation = BinaryAssociation(
    name="durability_service47",
    ends={
        Property(name="dcps_DurabilityServiceQosPolicy", type=dcps_DataWriter, multiplicity=Multiplicity(1, 1)),
        Property(name="dcps_DataWriter48", type=dcps_DurabilityServiceQosPolicy, multiplicity=Multiplicity(0, 1))
    }
)
ownership_strength49: BinaryAssociation = BinaryAssociation(
    name="ownership_strength49",
    ends={
        Property(name="dcps_OwnershipStrengthQosPolicy", type=dcps_DataWriter, multiplicity=Multiplicity(1, 1)),
        Property(name="dcps_DataWriter50", type=dcps_OwnershipStrengthQosPolicy, multiplicity=Multiplicity(0, 1))
    }
)
transport_priority51: BinaryAssociation = BinaryAssociation(
    name="transport_priority51",
    ends={
        Property(name="dcps_TransportPriorityQosPolicy", type=dcps_DataWriter, multiplicity=Multiplicity(1, 1)),
        Property(name="dcps_DataWriter52", type=dcps_TransportPriorityQosPolicy, multiplicity=Multiplicity(0, 1))
    }
)
writer_data_lifecycle53: BinaryAssociation = BinaryAssociation(
    name="writer_data_lifecycle53",
    ends={
        Property(name="dcps_WriterDataLifecycleQosPolicy", type=dcps_DataWriter, multiplicity=Multiplicity(1, 1)),
        Property(name="dcps_DataWriter54", type=dcps_WriterDataLifecycleQosPolicy, multiplicity=Multiplicity(0, 1))
    }
)
lifespan55: BinaryAssociation = BinaryAssociation(
    name="lifespan55",
    ends={
        Property(name="dcps_LifespanQosPolicy", type=dcps_DataWriter, multiplicity=Multiplicity(1, 1)),
        Property(name="dcps_DataWriter56", type=dcps_LifespanQosPolicy, multiplicity=Multiplicity(0, 1))
    }
)
topic57: BinaryAssociation = BinaryAssociation(
    name="topic57",
    ends={
        Property(name="dcps_Topic", type=dcps_DataWriter, multiplicity=Multiplicity(1, 1)),
        Property(name="dcps_DataWriter58", type=dcps_Topic, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_dcps_Domain_Entity = Generalization(general=Entity, specific=dcps_Domain)
gen_dcps_DomainParticipant_DomainEntity = Generalization(general=DomainEntity, specific=dcps_DomainParticipant)
gen_dcps_PublisherSubscriber_DomainEntity = Generalization(general=DomainEntity, specific=dcps_PublisherSubscriber)
gen_dcps_Subscriber_PublisherSubscriber = Generalization(general=PublisherSubscriber, specific=dcps_Subscriber)
gen_dcps_Publisher_PublisherSubscriber = Generalization(general=PublisherSubscriber, specific=dcps_Publisher)
gen_dcps_DataReaderWriter_DomainEntity = Generalization(general=DomainEntity, specific=dcps_DataReaderWriter)
gen_dcps_DataReader_DataReaderWriter = Generalization(general=DataReaderWriter, specific=dcps_DataReader)
gen_dcps_DataWriter_DataReaderWriter = Generalization(general=DataReaderWriter, specific=dcps_DataWriter)

# Domain Model
domain_model = DomainModel(
    name="dcps",
    types={dcps_PublisherSubscriber, dcps_Domain, Entity, dcps_DomainParticipant, DomainEntity, dcps_Publisher, dcps_Subscriber, dcps_EntityFactoryQosPolicy, dcps_UserDataQosPolicy, dcps_GroupDataQosPolicy, dcps_PresentationQosPolicy, dcps_PartitionQosPolicy, PublisherSubscriber, dcps_DataReader, dcps_DataWriter, dcps_DataReaderWriter, dcps_DeadlineQosPolicy, dcps_DestinationOrderQosPolicy, dcps_DurabilityQosPolicy, dcps_HistoryQosPolicy, dcps_LatencyBudgetQosPolicy, dcps_LivelinessQosPolicy, dcps_OwnershipQosPolicy, dcps_ReliabilityQosPolicy, dcps_ResourceLimitsQosPolicy, DataReaderWriter, dcps_ReaderDataLifecycleQosPolicy, dcps_TimeBasedFilterQosPolicy, dcps_TopicDescription, dcps_DurabilityServiceQosPolicy, dcps_OwnershipStrengthQosPolicy, dcps_TransportPriorityQosPolicy, dcps_WriterDataLifecycleQosPolicy, dcps_LifespanQosPolicy, dcps_Topic},
    associations={domain0, publishers1, subscribers3, entity_factory5, user_data7, entity_factory9, group_data11, presentation13, partition15, readers17, writers19, deadline21, destination_order22, durability24, history26, latency_budget28, liveliness30, ownership32, reliability34, resource_limits36, user_data38, reader_data_lifecycle41, time_based_filter43, topic45, durability_service47, ownership_strength49, transport_priority51, writer_data_lifecycle53, lifespan55, topic57},
    generalizations={gen_dcps_Domain_Entity, gen_dcps_DomainParticipant_DomainEntity, gen_dcps_PublisherSubscriber_DomainEntity, gen_dcps_Subscriber_PublisherSubscriber, gen_dcps_Publisher_PublisherSubscriber, gen_dcps_DataReaderWriter_DomainEntity, gen_dcps_DataReader_DataReaderWriter, gen_dcps_DataWriter_DataReaderWriter},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)