from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class LivelinessQosPolicyKind(Enum):
    AUTOMATIC_LIVELINESS_QOS = "AUTOMATIC_LIVELINESS_QOS"
    MANUAL_LIVELINESS_QOS = "MANUAL_LIVELINESS_QOS"
    MANUAL_BY_PARTICIPANT_LIVELINESS_QOS = "MANUAL_BY_PARTICIPANT_LIVELINESS_QOS"
    MANUAL_BY_TOPIC_LIVELINESS_QOS = "MANUAL_BY_TOPIC_LIVELINESS_QOS"
class SubscriberStatus(Enum):
    DATA_ON_READERS_STATUS = "DATA_ON_READERS_STATUS"
    DATA_AVAILABLE_STATUS = "DATA_AVAILABLE_STATUS"
    LIVELINESS_CHANGED_STATUS = "LIVELINESS_CHANGED_STATUS"
    REQUESTED_DEADLINE_MISSED_STATUS = "REQUESTED_DEADLINE_MISSED_STATUS"
    REQUESTED_INCOMPATIBLE_QOS_STATUS = "REQUESTED_INCOMPATIBLE_QOS_STATUS"
    SAMPLE_LOST_STATUS = "SAMPLE_LOST_STATUS"
    SAMPLE_REJECTED_STATUS = "SAMPLE_REJECTED_STATUS"
    SUBSCRIPTION_MATCHED_STATUS = "SUBSCRIPTION_MATCHED_STATUS"
class HistoryQosPolicyKind(Enum):
    KEEP_LAST_HISTORY_QOS = "KEEP_LAST_HISTORY_QOS"
    KEEP_ALL_HISTORY_QOS = "KEEP_ALL_HISTORY_QOS"
class DestinationOrderQosPolicyKind(Enum):
    BY_RECEPTION_TIMESTAMP_DESTINATIONORDER_QOS = "BY_RECEPTION_TIMESTAMP_DESTINATIONORDER_QOS"
    BY_SOURCE_TIMESTAMP_DESTINATIONORDER_QOS = "BY_SOURCE_TIMESTAMP_DESTINATIONORDER_QOS"
class ReliabilityQosPolicyKind(Enum):
    RELIABLE_RELIABILITY_QOS = "RELIABLE_RELIABILITY_QOS"
    BEST_EFFORT_RELIABILITY_QOS = "BEST_EFFORT_RELIABILITY_QOS"
class ViewStateKind(Enum):
    NEW_VIEW_STATE = "NEW_VIEW_STATE"
    NOT_NEW_VIEW_STATE = "NOT_NEW_VIEW_STATE"
    ANY_VIEW_STATE = "ANY_VIEW_STATE"
class DataWriterStatus(Enum):
    LIVELINESS_LOST_STATUS = "LIVELINESS_LOST_STATUS"
    OFFERED_DEADLINE_MISSED_STATUS = "OFFERED_DEADLINE_MISSED_STATUS"
    OFFERED_INCOMPATIBLE_QOS_STATUS = "OFFERED_INCOMPATIBLE_QOS_STATUS"
    PUBLICATION_MATCHED_STATUS = "PUBLICATION_MATCHED_STATUS"
class DomainParticipantStatus(Enum):
    INCONSISTENT_TOPIC_STATUS = "INCONSISTENT_TOPIC_STATUS"
    LIVELINESS_LOST_STATUS = "LIVELINESS_LOST_STATUS"
    OFFERED_DEADLINE_MISSED_STATUS = "OFFERED_DEADLINE_MISSED_STATUS"
    OFFERED_INCOMPATIBLE_QOS_STATUS = "OFFERED_INCOMPATIBLE_QOS_STATUS"
    PUBLICATION_MATCHED_STATUS = "PUBLICATION_MATCHED_STATUS"
    SAMPLE_REJECTED_STATUS = "SAMPLE_REJECTED_STATUS"
    LIVELINESS_CHANGED_STATUS = "LIVELINESS_CHANGED_STATUS"
    REQUESTED_DEADLINE_MISSED_STATUS = "REQUESTED_DEADLINE_MISSED_STATUS"
    REQUESTED_INCOMPATIBLE_QOS_STATUS = "REQUESTED_INCOMPATIBLE_QOS_STATUS"
    DATA_AVAILABLE_STATUS = "DATA_AVAILABLE_STATUS"
    SAMPLE_LOST_STATUS = "SAMPLE_LOST_STATUS"
    SUBSCRIPTION_MATCHED_STATUS = "SUBSCRIPTION_MATCHED_STATUS"
    DATA_ON_READERS_STATUS = "DATA_ON_READERS_STATUS"
class TopicStatus(Enum):
    INCONSISTENT_TOPIC_STATUS = "INCONSISTENT_TOPIC_STATUS"
class InvalidSampleVisibilityQosPolicy(Enum):
    NO_INVALID_SAMPLES = "NO_INVALID_SAMPLES"
    MINIMUM_INVALID_SAMPLES = "MINIMUM_INVALID_SAMPLES"
    ALL_INVALID_SAMPLES = "ALL_INVALID_SAMPLES"
class OwnershipQosPolicyKind(Enum):
    SHARED_OWNERSHIP_QOS = "SHARED_OWNERSHIP_QOS"
    EXCLUSIVE_OWNERSHIP_QOS = "EXCLUSIVE_OWNERSHIP_QOS"
class PublisherStatus(Enum):
    LIVELINESS_LOST_STATUS = "LIVELINESS_LOST_STATUS"
    OFFERED_DEADLINE_MISSED_STATUS = "OFFERED_DEADLINE_MISSED_STATUS"
    OFFERED_INCOMPATIBLE_QOS_STATUS = "OFFERED_INCOMPATIBLE_QOS_STATUS"
    PUBLICATION_MATCHED_STATUS = "PUBLICATION_MATCHED_STATUS"
class DataReaderStatus(Enum):
    DATA_AVAILABLE_STATUS = "DATA_AVAILABLE_STATUS"
    LIVELINESS_CHANGED_STATUS = "LIVELINESS_CHANGED_STATUS"
    SAMPLE_REJECTED_STATUS = "SAMPLE_REJECTED_STATUS"
    REQUESTED_DEADLINE_MISSED_STATUS = "REQUESTED_DEADLINE_MISSED_STATUS"
    REQUESTED_INCOMPATIBLE_QOS_STATUS = "REQUESTED_INCOMPATIBLE_QOS_STATUS"
    SAMPLE_LOST_STATUS = "SAMPLE_LOST_STATUS"
    SUBSCRIPTION_MATCHED_STATUS = "SUBSCRIPTION_MATCHED_STATUS"
class InstanceStateKind(Enum):
    ALIVE_INSTANCE_STATE = "ALIVE_INSTANCE_STATE"
    NOT_ALIVE_DISPOSED_INSTANCE_STATE = "NOT_ALIVE_DISPOSED_INSTANCE_STATE"
    NOT_ALIVE_NO_WRITERS_INSTANCE_STATE = "NOT_ALIVE_NO_WRITERS_INSTANCE_STATE"
    ANY_INSTANCE_STATE = "ANY_INSTANCE_STATE"
class PresentationQosPolicyAccessScopeKind(Enum):
    INSTANCE_PRESENTATION_QOS = "INSTANCE_PRESENTATION_QOS"
    TOPIC_PRESENTATION_QOS = "TOPIC_PRESENTATION_QOS"
    GROUP_PRESENTATION_QOS = "GROUP_PRESENTATION_QOS"
class DurabilityQosPolicyKind(Enum):
    VOLATILE_DURABILITY_QOS = "VOLATILE_DURABILITY_QOS"
    TRANSIENT_LOCAL_DURABILITY_QOS = "TRANSIENT_LOCAL_DURABILITY_QOS"
    TRANSIENT_DURABILITY_QOS = "TRANSIENT_DURABILITY_QOS"
    PERSISTENT_DURABILITY_QOS = "PERSISTENT_DURABILITY_QOS"
class SampleStateKind(Enum):
    READ_SAMPLE_STATE = "READ_SAMPLE_STATE"
    NOT_READ_SAMPLE_STATE = "NOT_READ_SAMPLE_STATE"
    ANY_READ_SAMPLE_STATE = "ANY_READ_SAMPLE_STATE"


############################################
# Definition of Classes
############################################

class ddsMetamodel_DdsHost:

    def __init__(self, hostName: str, ddsMetamodel_DdsHost: "ddsMetamodel_DdsSystem" = None, ddsMetamodel_DdsHost244: set["ddsMetamodel_DdsApplication"] = None):
        self.hostName = hostName
        self.ddsMetamodel_DdsHost = ddsMetamodel_DdsHost
        self.ddsMetamodel_DdsHost244 = ddsMetamodel_DdsHost244 if ddsMetamodel_DdsHost244 is not None else set()
        
    @property
    def hostName(self) -> str:
        return self.__hostName

    @hostName.setter
    def hostName(self, hostName: str):
        self.__hostName = hostName

    @property
    def ddsMetamodel_DdsHost244(self):
        return self.__ddsMetamodel_DdsHost244

    @ddsMetamodel_DdsHost244.setter
    def ddsMetamodel_DdsHost244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsHost__ddsMetamodel_DdsHost244", None)
        self.__ddsMetamodel_DdsHost244 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ddsMetamodel_DdsApplication245"):
                    opp_val = getattr(item, "ddsMetamodel_DdsApplication245", None)
                    
                    if opp_val == self:
                        setattr(item, "ddsMetamodel_DdsApplication245", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ddsMetamodel_DdsApplication245"):
                    opp_val = getattr(item, "ddsMetamodel_DdsApplication245", None)
                    
                    setattr(item, "ddsMetamodel_DdsApplication245", self)
                    

    @property
    def ddsMetamodel_DdsHost(self):
        return self.__ddsMetamodel_DdsHost

    @ddsMetamodel_DdsHost.setter
    def ddsMetamodel_DdsHost(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsHost__ddsMetamodel_DdsHost", None)
        self.__ddsMetamodel_DdsHost = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsSystem"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsSystem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsSystem"):
                opp_val = getattr(value, "ddsMetamodel_DdsSystem", None)
                if opp_val is None:
                    setattr(value, "ddsMetamodel_DdsSystem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DdsReadCondition:

    pass
class ddsMetamodel_QueryCondition(DdsReadCondition):

    def __init__(self, query: str, queryParameters: str):
        self.query = query
        self.queryParameters = queryParameters
        
    @property
    def queryParameters(self) -> str:
        return self.__queryParameters

    @queryParameters.setter
    def queryParameters(self, queryParameters: str):
        self.__queryParameters = queryParameters

    @property
    def query(self) -> str:
        return self.__query

    @query.setter
    def query(self, query: str):
        self.__query = query

class DdsStatusCondition:

    pass
class ddsMetamodel_DdsTopicStatusCondition(DdsStatusCondition):

    def __init__(self, enabled_status: str, ddsMetamodel_DdsTopicStatusCondition: "ddsMetamodel_DdsTopic" = None):
        self.enabled_status = enabled_status
        self.ddsMetamodel_DdsTopicStatusCondition = ddsMetamodel_DdsTopicStatusCondition
        
    @property
    def enabled_status(self) -> str:
        return self.__enabled_status

    @enabled_status.setter
    def enabled_status(self, enabled_status: str):
        self.__enabled_status = enabled_status

    @property
    def ddsMetamodel_DdsTopicStatusCondition(self):
        return self.__ddsMetamodel_DdsTopicStatusCondition

    @ddsMetamodel_DdsTopicStatusCondition.setter
    def ddsMetamodel_DdsTopicStatusCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsTopicStatusCondition__ddsMetamodel_DdsTopicStatusCondition", None)
        self.__ddsMetamodel_DdsTopicStatusCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsTopic234"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsTopic234", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsTopic234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsTopic234"):
                opp_val = getattr(value, "ddsMetamodel_DdsTopic234", None)
                setattr(value, "ddsMetamodel_DdsTopic234", self)

class ddsMetamodel_DdsDataReaderStatusCondition(DdsStatusCondition):

    def __init__(self, enabled_status: str, ddsMetamodel_DdsDataReaderStatusCondition: "ddsMetamodel_DdsDataReader" = None):
        self.enabled_status = enabled_status
        self.ddsMetamodel_DdsDataReaderStatusCondition = ddsMetamodel_DdsDataReaderStatusCondition
        
    @property
    def enabled_status(self) -> str:
        return self.__enabled_status

    @enabled_status.setter
    def enabled_status(self, enabled_status: str):
        self.__enabled_status = enabled_status

    @property
    def ddsMetamodel_DdsDataReaderStatusCondition(self):
        return self.__ddsMetamodel_DdsDataReaderStatusCondition

    @ddsMetamodel_DdsDataReaderStatusCondition.setter
    def ddsMetamodel_DdsDataReaderStatusCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataReaderStatusCondition__ddsMetamodel_DdsDataReaderStatusCondition", None)
        self.__ddsMetamodel_DdsDataReaderStatusCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataReader232"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataReader232", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataReader232", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataReader232"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataReader232", None)
                setattr(value, "ddsMetamodel_DdsDataReader232", self)

class ddsMetamodel_DdsDataWriterStatusCondition(DdsStatusCondition):

    def __init__(self, enabled_status: str, ddsMetamodel_DdsDataWriterStatusCondition: "ddsMetamodel_DdsDataWriter" = None):
        self.enabled_status = enabled_status
        self.ddsMetamodel_DdsDataWriterStatusCondition = ddsMetamodel_DdsDataWriterStatusCondition
        
    @property
    def enabled_status(self) -> str:
        return self.__enabled_status

    @enabled_status.setter
    def enabled_status(self, enabled_status: str):
        self.__enabled_status = enabled_status

    @property
    def ddsMetamodel_DdsDataWriterStatusCondition(self):
        return self.__ddsMetamodel_DdsDataWriterStatusCondition

    @ddsMetamodel_DdsDataWriterStatusCondition.setter
    def ddsMetamodel_DdsDataWriterStatusCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataWriterStatusCondition__ddsMetamodel_DdsDataWriterStatusCondition", None)
        self.__ddsMetamodel_DdsDataWriterStatusCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataWriter230"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataWriter230", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataWriter230", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataWriter230"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataWriter230", None)
                setattr(value, "ddsMetamodel_DdsDataWriter230", self)

class ddsMetamodel_DdsDomainParticipantStatusCondition(DdsStatusCondition):

    def __init__(self, enabled_status: str, ddsMetamodel_DdsDomainParticipantStatusCondition: "ddsMetamodel_DdsDomainParticipant" = None):
        self.enabled_status = enabled_status
        self.ddsMetamodel_DdsDomainParticipantStatusCondition = ddsMetamodel_DdsDomainParticipantStatusCondition
        
    @property
    def enabled_status(self) -> str:
        return self.__enabled_status

    @enabled_status.setter
    def enabled_status(self, enabled_status: str):
        self.__enabled_status = enabled_status

    @property
    def ddsMetamodel_DdsDomainParticipantStatusCondition(self):
        return self.__ddsMetamodel_DdsDomainParticipantStatusCondition

    @ddsMetamodel_DdsDomainParticipantStatusCondition.setter
    def ddsMetamodel_DdsDomainParticipantStatusCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDomainParticipantStatusCondition__ddsMetamodel_DdsDomainParticipantStatusCondition", None)
        self.__ddsMetamodel_DdsDomainParticipantStatusCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDomainParticipant224"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDomainParticipant224", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDomainParticipant224", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDomainParticipant224"):
                opp_val = getattr(value, "ddsMetamodel_DdsDomainParticipant224", None)
                setattr(value, "ddsMetamodel_DdsDomainParticipant224", self)

class ddsMetamodel_DdsSubscriberStatusCondition(DdsStatusCondition):

    def __init__(self, enabled_status: str, ddsMetamodel_DdsSubscriberStatusCondition: "ddsMetamodel_DdsSubscriber" = None):
        self.enabled_status = enabled_status
        self.ddsMetamodel_DdsSubscriberStatusCondition = ddsMetamodel_DdsSubscriberStatusCondition
        
    @property
    def enabled_status(self) -> str:
        return self.__enabled_status

    @enabled_status.setter
    def enabled_status(self, enabled_status: str):
        self.__enabled_status = enabled_status

    @property
    def ddsMetamodel_DdsSubscriberStatusCondition(self):
        return self.__ddsMetamodel_DdsSubscriberStatusCondition

    @ddsMetamodel_DdsSubscriberStatusCondition.setter
    def ddsMetamodel_DdsSubscriberStatusCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsSubscriberStatusCondition__ddsMetamodel_DdsSubscriberStatusCondition", None)
        self.__ddsMetamodel_DdsSubscriberStatusCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsSubscriber228"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsSubscriber228", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsSubscriber228", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsSubscriber228"):
                opp_val = getattr(value, "ddsMetamodel_DdsSubscriber228", None)
                setattr(value, "ddsMetamodel_DdsSubscriber228", self)

class ddsMetamodel_DdsPublisherStatusCondition(DdsStatusCondition):

    def __init__(self, enabled_status: str, ddsMetamodel_DdsPublisherStatusCondition: "ddsMetamodel_DdsPublisher" = None):
        self.enabled_status = enabled_status
        self.ddsMetamodel_DdsPublisherStatusCondition = ddsMetamodel_DdsPublisherStatusCondition
        
    @property
    def enabled_status(self) -> str:
        return self.__enabled_status

    @enabled_status.setter
    def enabled_status(self, enabled_status: str):
        self.__enabled_status = enabled_status

    @property
    def ddsMetamodel_DdsPublisherStatusCondition(self):
        return self.__ddsMetamodel_DdsPublisherStatusCondition

    @ddsMetamodel_DdsPublisherStatusCondition.setter
    def ddsMetamodel_DdsPublisherStatusCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsPublisherStatusCondition__ddsMetamodel_DdsPublisherStatusCondition", None)
        self.__ddsMetamodel_DdsPublisherStatusCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsPublisher226"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsPublisher226", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsPublisher226", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsPublisher226"):
                opp_val = getattr(value, "ddsMetamodel_DdsPublisher226", None)
                setattr(value, "ddsMetamodel_DdsPublisher226", self)

class ddsMetamodel_GuardCondition:

    def __init__(self, name: str, ddsMetamodel_GuardCondition: "ddsMetamodel_DdsWaitSet" = None):
        self.name = name
        self.ddsMetamodel_GuardCondition = ddsMetamodel_GuardCondition
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ddsMetamodel_GuardCondition(self):
        return self.__ddsMetamodel_GuardCondition

    @ddsMetamodel_GuardCondition.setter
    def ddsMetamodel_GuardCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_GuardCondition__ddsMetamodel_GuardCondition", None)
        self.__ddsMetamodel_GuardCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsWaitSet214"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsWaitSet214", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsWaitSet214"):
                opp_val = getattr(value, "ddsMetamodel_DdsWaitSet214", None)
                if opp_val is None:
                    setattr(value, "ddsMetamodel_DdsWaitSet214", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ddsMetamodel_DdsStatusCondition:

    pass
class ddsMetamodel_DdsReadCondition:

    def __init__(self, instance_state_mask: str, sample_state_mask: str, view_state_mask: str, ddsMetamodel_DdsReadCondition: "ddsMetamodel_DdsWaitSet" = None, ddsMetamodel_DdsReadCondition216: "ddsMetamodel_DdsDataReader" = None):
        self.instance_state_mask = instance_state_mask
        self.sample_state_mask = sample_state_mask
        self.view_state_mask = view_state_mask
        self.ddsMetamodel_DdsReadCondition = ddsMetamodel_DdsReadCondition
        self.ddsMetamodel_DdsReadCondition216 = ddsMetamodel_DdsReadCondition216
        
    @property
    def view_state_mask(self) -> str:
        return self.__view_state_mask

    @view_state_mask.setter
    def view_state_mask(self, view_state_mask: str):
        self.__view_state_mask = view_state_mask

    @property
    def instance_state_mask(self) -> str:
        return self.__instance_state_mask

    @instance_state_mask.setter
    def instance_state_mask(self, instance_state_mask: str):
        self.__instance_state_mask = instance_state_mask

    @property
    def sample_state_mask(self) -> str:
        return self.__sample_state_mask

    @sample_state_mask.setter
    def sample_state_mask(self, sample_state_mask: str):
        self.__sample_state_mask = sample_state_mask

    @property
    def ddsMetamodel_DdsReadCondition216(self):
        return self.__ddsMetamodel_DdsReadCondition216

    @ddsMetamodel_DdsReadCondition216.setter
    def ddsMetamodel_DdsReadCondition216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsReadCondition__ddsMetamodel_DdsReadCondition216", None)
        self.__ddsMetamodel_DdsReadCondition216 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataReader217"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataReader217", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataReader217", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataReader217"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataReader217", None)
                setattr(value, "ddsMetamodel_DdsDataReader217", self)

    @property
    def ddsMetamodel_DdsReadCondition(self):
        return self.__ddsMetamodel_DdsReadCondition

    @ddsMetamodel_DdsReadCondition.setter
    def ddsMetamodel_DdsReadCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsReadCondition__ddsMetamodel_DdsReadCondition", None)
        self.__ddsMetamodel_DdsReadCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsWaitSet211"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsWaitSet211", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsWaitSet211"):
                opp_val = getattr(value, "ddsMetamodel_DdsWaitSet211", None)
                if opp_val is None:
                    setattr(value, "ddsMetamodel_DdsWaitSet211", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ddsMetamodel_DdsGroupDataQos:

    def __init__(self, value: str, ddsMetamodel_DdsGroupDataQos: "ddsMetamodel_DdsPublisherQosProfile" = None, ddsMetamodel_DdsGroupDataQos164: "ddsMetamodel_DdsSubscriberQosProfile" = None):
        self.value = value
        self.ddsMetamodel_DdsGroupDataQos = ddsMetamodel_DdsGroupDataQos
        self.ddsMetamodel_DdsGroupDataQos164 = ddsMetamodel_DdsGroupDataQos164
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def ddsMetamodel_DdsGroupDataQos164(self):
        return self.__ddsMetamodel_DdsGroupDataQos164

    @ddsMetamodel_DdsGroupDataQos164.setter
    def ddsMetamodel_DdsGroupDataQos164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsGroupDataQos__ddsMetamodel_DdsGroupDataQos164", None)
        self.__ddsMetamodel_DdsGroupDataQos164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsSubscriberQosProfile163"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsSubscriberQosProfile163", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsSubscriberQosProfile163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsSubscriberQosProfile163"):
                opp_val = getattr(value, "ddsMetamodel_DdsSubscriberQosProfile163", None)
                setattr(value, "ddsMetamodel_DdsSubscriberQosProfile163", self)

    @property
    def ddsMetamodel_DdsGroupDataQos(self):
        return self.__ddsMetamodel_DdsGroupDataQos

    @ddsMetamodel_DdsGroupDataQos.setter
    def ddsMetamodel_DdsGroupDataQos(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsGroupDataQos__ddsMetamodel_DdsGroupDataQos", None)
        self.__ddsMetamodel_DdsGroupDataQos = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsPublisherQosProfile113"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsPublisherQosProfile113", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsPublisherQosProfile113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsPublisherQosProfile113"):
                opp_val = getattr(value, "ddsMetamodel_DdsPublisherQosProfile113", None)
                setattr(value, "ddsMetamodel_DdsPublisherQosProfile113", self)

class ddsMetamodel_DdsDataReaderLifecycleQos:

    def __init__(self, autopurge_dispose_all: bool, enable_invalid_samples: bool, ddsMetamodel_DdsDataReaderLifecycleQos: "ddsMetamodel_DdsDuration" = None, ddsMetamodel_DdsDataReaderLifecycleQos110: "ddsMetamodel_DdsDuration" = None, ddsMetamodel_DdsDataReaderLifecycleQos209: "ddsMetamodel_DdsDataReaderQosProfile" = None):
        self.autopurge_dispose_all = autopurge_dispose_all
        self.enable_invalid_samples = enable_invalid_samples
        self.ddsMetamodel_DdsDataReaderLifecycleQos = ddsMetamodel_DdsDataReaderLifecycleQos
        self.ddsMetamodel_DdsDataReaderLifecycleQos110 = ddsMetamodel_DdsDataReaderLifecycleQos110
        self.ddsMetamodel_DdsDataReaderLifecycleQos209 = ddsMetamodel_DdsDataReaderLifecycleQos209
        
    @property
    def enable_invalid_samples(self) -> bool:
        return self.__enable_invalid_samples

    @enable_invalid_samples.setter
    def enable_invalid_samples(self, enable_invalid_samples: bool):
        self.__enable_invalid_samples = enable_invalid_samples

    @property
    def autopurge_dispose_all(self) -> bool:
        return self.__autopurge_dispose_all

    @autopurge_dispose_all.setter
    def autopurge_dispose_all(self, autopurge_dispose_all: bool):
        self.__autopurge_dispose_all = autopurge_dispose_all

    @property
    def ddsMetamodel_DdsDataReaderLifecycleQos(self):
        return self.__ddsMetamodel_DdsDataReaderLifecycleQos

    @ddsMetamodel_DdsDataReaderLifecycleQos.setter
    def ddsMetamodel_DdsDataReaderLifecycleQos(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataReaderLifecycleQos__ddsMetamodel_DdsDataReaderLifecycleQos", None)
        self.__ddsMetamodel_DdsDataReaderLifecycleQos = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDuration108"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDuration108", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDuration108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDuration108"):
                opp_val = getattr(value, "ddsMetamodel_DdsDuration108", None)
                setattr(value, "ddsMetamodel_DdsDuration108", self)

    @property
    def ddsMetamodel_DdsDataReaderLifecycleQos110(self):
        return self.__ddsMetamodel_DdsDataReaderLifecycleQos110

    @ddsMetamodel_DdsDataReaderLifecycleQos110.setter
    def ddsMetamodel_DdsDataReaderLifecycleQos110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataReaderLifecycleQos__ddsMetamodel_DdsDataReaderLifecycleQos110", None)
        self.__ddsMetamodel_DdsDataReaderLifecycleQos110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDuration111"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDuration111", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDuration111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDuration111"):
                opp_val = getattr(value, "ddsMetamodel_DdsDuration111", None)
                setattr(value, "ddsMetamodel_DdsDuration111", self)

    @property
    def ddsMetamodel_DdsDataReaderLifecycleQos209(self):
        return self.__ddsMetamodel_DdsDataReaderLifecycleQos209

    @ddsMetamodel_DdsDataReaderLifecycleQos209.setter
    def ddsMetamodel_DdsDataReaderLifecycleQos209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataReaderLifecycleQos__ddsMetamodel_DdsDataReaderLifecycleQos209", None)
        self.__ddsMetamodel_DdsDataReaderLifecycleQos209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataReaderQosProfile208"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataReaderQosProfile208", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataReaderQosProfile208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataReaderQosProfile208"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataReaderQosProfile208", None)
                setattr(value, "ddsMetamodel_DdsDataReaderQosProfile208", self)

class ddsMetamodel_DdsDataWriterLifecycleQos:

    def __init__(self, autodispose_unregistered_instances: bool, ddsMetamodel_DdsDataWriterLifecycleQos: "ddsMetamodel_DdsDuration" = None, ddsMetamodel_DdsDataWriterLifecycleQos105: "ddsMetamodel_DdsDuration" = None, ddsMetamodel_DdsDataWriterLifecycleQos161: "ddsMetamodel_DdsDataWriterQosProfile" = None):
        self.autodispose_unregistered_instances = autodispose_unregistered_instances
        self.ddsMetamodel_DdsDataWriterLifecycleQos = ddsMetamodel_DdsDataWriterLifecycleQos
        self.ddsMetamodel_DdsDataWriterLifecycleQos105 = ddsMetamodel_DdsDataWriterLifecycleQos105
        self.ddsMetamodel_DdsDataWriterLifecycleQos161 = ddsMetamodel_DdsDataWriterLifecycleQos161
        
    @property
    def autodispose_unregistered_instances(self) -> bool:
        return self.__autodispose_unregistered_instances

    @autodispose_unregistered_instances.setter
    def autodispose_unregistered_instances(self, autodispose_unregistered_instances: bool):
        self.__autodispose_unregistered_instances = autodispose_unregistered_instances

    @property
    def ddsMetamodel_DdsDataWriterLifecycleQos105(self):
        return self.__ddsMetamodel_DdsDataWriterLifecycleQos105

    @ddsMetamodel_DdsDataWriterLifecycleQos105.setter
    def ddsMetamodel_DdsDataWriterLifecycleQos105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataWriterLifecycleQos__ddsMetamodel_DdsDataWriterLifecycleQos105", None)
        self.__ddsMetamodel_DdsDataWriterLifecycleQos105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDuration106"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDuration106", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDuration106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDuration106"):
                opp_val = getattr(value, "ddsMetamodel_DdsDuration106", None)
                setattr(value, "ddsMetamodel_DdsDuration106", self)

    @property
    def ddsMetamodel_DdsDataWriterLifecycleQos(self):
        return self.__ddsMetamodel_DdsDataWriterLifecycleQos

    @ddsMetamodel_DdsDataWriterLifecycleQos.setter
    def ddsMetamodel_DdsDataWriterLifecycleQos(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataWriterLifecycleQos__ddsMetamodel_DdsDataWriterLifecycleQos", None)
        self.__ddsMetamodel_DdsDataWriterLifecycleQos = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDuration103"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDuration103", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDuration103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDuration103"):
                opp_val = getattr(value, "ddsMetamodel_DdsDuration103", None)
                setattr(value, "ddsMetamodel_DdsDuration103", self)

    @property
    def ddsMetamodel_DdsDataWriterLifecycleQos161(self):
        return self.__ddsMetamodel_DdsDataWriterLifecycleQos161

    @ddsMetamodel_DdsDataWriterLifecycleQos161.setter
    def ddsMetamodel_DdsDataWriterLifecycleQos161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataWriterLifecycleQos__ddsMetamodel_DdsDataWriterLifecycleQos161", None)
        self.__ddsMetamodel_DdsDataWriterLifecycleQos161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile160"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile160", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataWriterQosProfile160"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataWriterQosProfile160", None)
                setattr(value, "ddsMetamodel_DdsDataWriterQosProfile160", self)

class ddsMetamodel_DdsPartitionQos:

    def __init__(self, name: str, ddsMetamodel_DdsPartitionQos: "ddsMetamodel_DdsPublisherQosProfile" = None, ddsMetamodel_DdsPartitionQos173: "ddsMetamodel_DdsSubscriberQosProfile" = None):
        self.name = name
        self.ddsMetamodel_DdsPartitionQos = ddsMetamodel_DdsPartitionQos
        self.ddsMetamodel_DdsPartitionQos173 = ddsMetamodel_DdsPartitionQos173
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ddsMetamodel_DdsPartitionQos173(self):
        return self.__ddsMetamodel_DdsPartitionQos173

    @ddsMetamodel_DdsPartitionQos173.setter
    def ddsMetamodel_DdsPartitionQos173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsPartitionQos__ddsMetamodel_DdsPartitionQos173", None)
        self.__ddsMetamodel_DdsPartitionQos173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsSubscriberQosProfile172"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsSubscriberQosProfile172", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsSubscriberQosProfile172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsSubscriberQosProfile172"):
                opp_val = getattr(value, "ddsMetamodel_DdsSubscriberQosProfile172", None)
                setattr(value, "ddsMetamodel_DdsSubscriberQosProfile172", self)

    @property
    def ddsMetamodel_DdsPartitionQos(self):
        return self.__ddsMetamodel_DdsPartitionQos

    @ddsMetamodel_DdsPartitionQos.setter
    def ddsMetamodel_DdsPartitionQos(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsPartitionQos__ddsMetamodel_DdsPartitionQos", None)
        self.__ddsMetamodel_DdsPartitionQos = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsPublisherQosProfile120"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsPublisherQosProfile120", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsPublisherQosProfile120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsPublisherQosProfile120"):
                opp_val = getattr(value, "ddsMetamodel_DdsPublisherQosProfile120", None)
                setattr(value, "ddsMetamodel_DdsPublisherQosProfile120", self)

class ddsMetamodel_DdsTimeBasedFilterQos:

    pass
class ddsMetamodel_DdsOwnershipStrengthQos:

    def __init__(self, value: str, ddsMetamodel_DdsOwnershipStrengthQos: "ddsMetamodel_DdsDataWriterQosProfile" = None):
        self.value = value
        self.ddsMetamodel_DdsOwnershipStrengthQos = ddsMetamodel_DdsOwnershipStrengthQos
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def ddsMetamodel_DdsOwnershipStrengthQos(self):
        return self.__ddsMetamodel_DdsOwnershipStrengthQos

    @ddsMetamodel_DdsOwnershipStrengthQos.setter
    def ddsMetamodel_DdsOwnershipStrengthQos(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsOwnershipStrengthQos__ddsMetamodel_DdsOwnershipStrengthQos", None)
        self.__ddsMetamodel_DdsOwnershipStrengthQos = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile137"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile137", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataWriterQosProfile137"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataWriterQosProfile137", None)
                setattr(value, "ddsMetamodel_DdsDataWriterQosProfile137", self)

class ddsMetamodel_DdsPresentationQos:

    def __init__(self, access_scope: str, coherent_access: bool, ordered_access: bool, ddsMetamodel_DdsPresentationQos: "ddsMetamodel_DdsPublisherQosProfile" = None, ddsMetamodel_DdsPresentationQos170: "ddsMetamodel_DdsSubscriberQosProfile" = None):
        self.access_scope = access_scope
        self.coherent_access = coherent_access
        self.ordered_access = ordered_access
        self.ddsMetamodel_DdsPresentationQos = ddsMetamodel_DdsPresentationQos
        self.ddsMetamodel_DdsPresentationQos170 = ddsMetamodel_DdsPresentationQos170
        
    @property
    def ordered_access(self) -> bool:
        return self.__ordered_access

    @ordered_access.setter
    def ordered_access(self, ordered_access: bool):
        self.__ordered_access = ordered_access

    @property
    def access_scope(self) -> str:
        return self.__access_scope

    @access_scope.setter
    def access_scope(self, access_scope: str):
        self.__access_scope = access_scope

    @property
    def coherent_access(self) -> bool:
        return self.__coherent_access

    @coherent_access.setter
    def coherent_access(self, coherent_access: bool):
        self.__coherent_access = coherent_access

    @property
    def ddsMetamodel_DdsPresentationQos170(self):
        return self.__ddsMetamodel_DdsPresentationQos170

    @ddsMetamodel_DdsPresentationQos170.setter
    def ddsMetamodel_DdsPresentationQos170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsPresentationQos__ddsMetamodel_DdsPresentationQos170", None)
        self.__ddsMetamodel_DdsPresentationQos170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsSubscriberQosProfile169"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsSubscriberQosProfile169", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsSubscriberQosProfile169", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsSubscriberQosProfile169"):
                opp_val = getattr(value, "ddsMetamodel_DdsSubscriberQosProfile169", None)
                setattr(value, "ddsMetamodel_DdsSubscriberQosProfile169", self)

    @property
    def ddsMetamodel_DdsPresentationQos(self):
        return self.__ddsMetamodel_DdsPresentationQos

    @ddsMetamodel_DdsPresentationQos.setter
    def ddsMetamodel_DdsPresentationQos(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsPresentationQos__ddsMetamodel_DdsPresentationQos", None)
        self.__ddsMetamodel_DdsPresentationQos = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsPublisherQosProfile118"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsPublisherQosProfile118", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsPublisherQosProfile118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsPublisherQosProfile118"):
                opp_val = getattr(value, "ddsMetamodel_DdsPublisherQosProfile118", None)
                setattr(value, "ddsMetamodel_DdsPublisherQosProfile118", self)

class ddsMetamodel_DdsDuration:

    def __init__(self, sec: str, nanoSec: str, ddsMetamodel_DdsDuration: "ddsMetamodel_DdsDurabilityServiceQos" = None, ddsMetamodel_DdsDuration87: "ddsMetamodel_DdsDeadlineQos" = None, ddsMetamodel_DdsDuration90: "ddsMetamodel_DdsLatencyBudgetQos" = None, ddsMetamodel_DdsDuration95: "ddsMetamodel_DdsTimeBasedFilterQos" = None, ddsMetamodel_DdsDuration98: "ddsMetamodel_DdsReliabilityQos" = None, ddsMetamodel_DdsDuration93: "ddsMetamodel_DdsLivelinessQos" = None, ddsMetamodel_DdsDuration101: "ddsMetamodel_DdsLifespan" = None, ddsMetamodel_DdsDuration103: "ddsMetamodel_DdsDataWriterLifecycleQos" = None, ddsMetamodel_DdsDuration106: "ddsMetamodel_DdsDataWriterLifecycleQos" = None, ddsMetamodel_DdsDuration111: "ddsMetamodel_DdsDataReaderLifecycleQos" = None, ddsMetamodel_DdsDuration108: "ddsMetamodel_DdsDataReaderLifecycleQos" = None):
        self.sec = sec
        self.nanoSec = nanoSec
        self.ddsMetamodel_DdsDuration = ddsMetamodel_DdsDuration
        self.ddsMetamodel_DdsDuration87 = ddsMetamodel_DdsDuration87
        self.ddsMetamodel_DdsDuration90 = ddsMetamodel_DdsDuration90
        self.ddsMetamodel_DdsDuration95 = ddsMetamodel_DdsDuration95
        self.ddsMetamodel_DdsDuration98 = ddsMetamodel_DdsDuration98
        self.ddsMetamodel_DdsDuration93 = ddsMetamodel_DdsDuration93
        self.ddsMetamodel_DdsDuration101 = ddsMetamodel_DdsDuration101
        self.ddsMetamodel_DdsDuration103 = ddsMetamodel_DdsDuration103
        self.ddsMetamodel_DdsDuration106 = ddsMetamodel_DdsDuration106
        self.ddsMetamodel_DdsDuration111 = ddsMetamodel_DdsDuration111
        self.ddsMetamodel_DdsDuration108 = ddsMetamodel_DdsDuration108
        
    @property
    def sec(self) -> str:
        return self.__sec

    @sec.setter
    def sec(self, sec: str):
        self.__sec = sec

    @property
    def nanoSec(self) -> str:
        return self.__nanoSec

    @nanoSec.setter
    def nanoSec(self, nanoSec: str):
        self.__nanoSec = nanoSec

    @property
    def ddsMetamodel_DdsDuration95(self):
        return self.__ddsMetamodel_DdsDuration95

    @ddsMetamodel_DdsDuration95.setter
    def ddsMetamodel_DdsDuration95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDuration__ddsMetamodel_DdsDuration95", None)
        self.__ddsMetamodel_DdsDuration95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsTimeBasedFilterQos"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsTimeBasedFilterQos", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsTimeBasedFilterQos", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsTimeBasedFilterQos"):
                opp_val = getattr(value, "ddsMetamodel_DdsTimeBasedFilterQos", None)
                setattr(value, "ddsMetamodel_DdsTimeBasedFilterQos", self)

    @property
    def ddsMetamodel_DdsDuration93(self):
        return self.__ddsMetamodel_DdsDuration93

    @ddsMetamodel_DdsDuration93.setter
    def ddsMetamodel_DdsDuration93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDuration__ddsMetamodel_DdsDuration93", None)
        self.__ddsMetamodel_DdsDuration93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsLivelinessQos92"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsLivelinessQos92", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsLivelinessQos92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsLivelinessQos92"):
                opp_val = getattr(value, "ddsMetamodel_DdsLivelinessQos92", None)
                setattr(value, "ddsMetamodel_DdsLivelinessQos92", self)

    @property
    def ddsMetamodel_DdsDuration90(self):
        return self.__ddsMetamodel_DdsDuration90

    @ddsMetamodel_DdsDuration90.setter
    def ddsMetamodel_DdsDuration90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDuration__ddsMetamodel_DdsDuration90", None)
        self.__ddsMetamodel_DdsDuration90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsLatencyBudgetQos89"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsLatencyBudgetQos89", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsLatencyBudgetQos89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsLatencyBudgetQos89"):
                opp_val = getattr(value, "ddsMetamodel_DdsLatencyBudgetQos89", None)
                setattr(value, "ddsMetamodel_DdsLatencyBudgetQos89", self)

    @property
    def ddsMetamodel_DdsDuration87(self):
        return self.__ddsMetamodel_DdsDuration87

    @ddsMetamodel_DdsDuration87.setter
    def ddsMetamodel_DdsDuration87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDuration__ddsMetamodel_DdsDuration87", None)
        self.__ddsMetamodel_DdsDuration87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDeadlineQos86"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDeadlineQos86", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDeadlineQos86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDeadlineQos86"):
                opp_val = getattr(value, "ddsMetamodel_DdsDeadlineQos86", None)
                setattr(value, "ddsMetamodel_DdsDeadlineQos86", self)

    @property
    def ddsMetamodel_DdsDuration106(self):
        return self.__ddsMetamodel_DdsDuration106

    @ddsMetamodel_DdsDuration106.setter
    def ddsMetamodel_DdsDuration106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDuration__ddsMetamodel_DdsDuration106", None)
        self.__ddsMetamodel_DdsDuration106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataWriterLifecycleQos105"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataWriterLifecycleQos105", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataWriterLifecycleQos105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataWriterLifecycleQos105"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataWriterLifecycleQos105", None)
                setattr(value, "ddsMetamodel_DdsDataWriterLifecycleQos105", self)

    @property
    def ddsMetamodel_DdsDuration111(self):
        return self.__ddsMetamodel_DdsDuration111

    @ddsMetamodel_DdsDuration111.setter
    def ddsMetamodel_DdsDuration111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDuration__ddsMetamodel_DdsDuration111", None)
        self.__ddsMetamodel_DdsDuration111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataReaderLifecycleQos110"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataReaderLifecycleQos110", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataReaderLifecycleQos110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataReaderLifecycleQos110"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataReaderLifecycleQos110", None)
                setattr(value, "ddsMetamodel_DdsDataReaderLifecycleQos110", self)

    @property
    def ddsMetamodel_DdsDuration103(self):
        return self.__ddsMetamodel_DdsDuration103

    @ddsMetamodel_DdsDuration103.setter
    def ddsMetamodel_DdsDuration103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDuration__ddsMetamodel_DdsDuration103", None)
        self.__ddsMetamodel_DdsDuration103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataWriterLifecycleQos"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataWriterLifecycleQos", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataWriterLifecycleQos", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataWriterLifecycleQos"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataWriterLifecycleQos", None)
                setattr(value, "ddsMetamodel_DdsDataWriterLifecycleQos", self)

    @property
    def ddsMetamodel_DdsDuration101(self):
        return self.__ddsMetamodel_DdsDuration101

    @ddsMetamodel_DdsDuration101.setter
    def ddsMetamodel_DdsDuration101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDuration__ddsMetamodel_DdsDuration101", None)
        self.__ddsMetamodel_DdsDuration101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsLifespan100"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsLifespan100", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsLifespan100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsLifespan100"):
                opp_val = getattr(value, "ddsMetamodel_DdsLifespan100", None)
                setattr(value, "ddsMetamodel_DdsLifespan100", self)

    @property
    def ddsMetamodel_DdsDuration(self):
        return self.__ddsMetamodel_DdsDuration

    @ddsMetamodel_DdsDuration.setter
    def ddsMetamodel_DdsDuration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDuration__ddsMetamodel_DdsDuration", None)
        self.__ddsMetamodel_DdsDuration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDurabilityServiceQos84"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDurabilityServiceQos84", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDurabilityServiceQos84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDurabilityServiceQos84"):
                opp_val = getattr(value, "ddsMetamodel_DdsDurabilityServiceQos84", None)
                setattr(value, "ddsMetamodel_DdsDurabilityServiceQos84", self)

    @property
    def ddsMetamodel_DdsDuration98(self):
        return self.__ddsMetamodel_DdsDuration98

    @ddsMetamodel_DdsDuration98.setter
    def ddsMetamodel_DdsDuration98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDuration__ddsMetamodel_DdsDuration98", None)
        self.__ddsMetamodel_DdsDuration98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsReliabilityQos97"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsReliabilityQos97", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsReliabilityQos97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsReliabilityQos97"):
                opp_val = getattr(value, "ddsMetamodel_DdsReliabilityQos97", None)
                setattr(value, "ddsMetamodel_DdsReliabilityQos97", self)

    @property
    def ddsMetamodel_DdsDuration108(self):
        return self.__ddsMetamodel_DdsDuration108

    @ddsMetamodel_DdsDuration108.setter
    def ddsMetamodel_DdsDuration108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDuration__ddsMetamodel_DdsDuration108", None)
        self.__ddsMetamodel_DdsDuration108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataReaderLifecycleQos"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataReaderLifecycleQos", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataReaderLifecycleQos", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataReaderLifecycleQos"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataReaderLifecycleQos", None)
                setattr(value, "ddsMetamodel_DdsDataReaderLifecycleQos", self)

class ddsMetamodel_DdsOwnershipQos:

    def __init__(self, kind: str, ddsMetamodel_DdsOwnershipQos: "ddsMetamodel_DdsTopicQosProfile" = None, ddsMetamodel_DdsOwnershipQos135: "ddsMetamodel_DdsDataWriterQosProfile" = None, ddsMetamodel_DdsOwnershipQos191: "ddsMetamodel_DdsDataReaderQosProfile" = None):
        self.kind = kind
        self.ddsMetamodel_DdsOwnershipQos = ddsMetamodel_DdsOwnershipQos
        self.ddsMetamodel_DdsOwnershipQos135 = ddsMetamodel_DdsOwnershipQos135
        self.ddsMetamodel_DdsOwnershipQos191 = ddsMetamodel_DdsOwnershipQos191
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def ddsMetamodel_DdsOwnershipQos(self):
        return self.__ddsMetamodel_DdsOwnershipQos

    @ddsMetamodel_DdsOwnershipQos.setter
    def ddsMetamodel_DdsOwnershipQos(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsOwnershipQos__ddsMetamodel_DdsOwnershipQos", None)
        self.__ddsMetamodel_DdsOwnershipQos = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsTopicQosProfile68"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsTopicQosProfile68", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsTopicQosProfile68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsTopicQosProfile68"):
                opp_val = getattr(value, "ddsMetamodel_DdsTopicQosProfile68", None)
                setattr(value, "ddsMetamodel_DdsTopicQosProfile68", self)

    @property
    def ddsMetamodel_DdsOwnershipQos135(self):
        return self.__ddsMetamodel_DdsOwnershipQos135

    @ddsMetamodel_DdsOwnershipQos135.setter
    def ddsMetamodel_DdsOwnershipQos135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsOwnershipQos__ddsMetamodel_DdsOwnershipQos135", None)
        self.__ddsMetamodel_DdsOwnershipQos135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile134"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile134", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataWriterQosProfile134"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataWriterQosProfile134", None)
                setattr(value, "ddsMetamodel_DdsDataWriterQosProfile134", self)

    @property
    def ddsMetamodel_DdsOwnershipQos191(self):
        return self.__ddsMetamodel_DdsOwnershipQos191

    @ddsMetamodel_DdsOwnershipQos191.setter
    def ddsMetamodel_DdsOwnershipQos191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsOwnershipQos__ddsMetamodel_DdsOwnershipQos191", None)
        self.__ddsMetamodel_DdsOwnershipQos191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataReaderQosProfile190"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataReaderQosProfile190", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataReaderQosProfile190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataReaderQosProfile190"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataReaderQosProfile190", None)
                setattr(value, "ddsMetamodel_DdsDataReaderQosProfile190", self)

class ddsMetamodel_DdsLivelinessQos:

    def __init__(self, kind: str, ddsMetamodel_DdsLivelinessQos: "ddsMetamodel_DdsTopicQosProfile" = None, ddsMetamodel_DdsLivelinessQos92: "ddsMetamodel_DdsDuration" = None, ddsMetamodel_DdsLivelinessQos140: "ddsMetamodel_DdsDataWriterQosProfile" = None, ddsMetamodel_DdsLivelinessQos188: "ddsMetamodel_DdsDataReaderQosProfile" = None):
        self.kind = kind
        self.ddsMetamodel_DdsLivelinessQos = ddsMetamodel_DdsLivelinessQos
        self.ddsMetamodel_DdsLivelinessQos92 = ddsMetamodel_DdsLivelinessQos92
        self.ddsMetamodel_DdsLivelinessQos140 = ddsMetamodel_DdsLivelinessQos140
        self.ddsMetamodel_DdsLivelinessQos188 = ddsMetamodel_DdsLivelinessQos188
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def ddsMetamodel_DdsLivelinessQos188(self):
        return self.__ddsMetamodel_DdsLivelinessQos188

    @ddsMetamodel_DdsLivelinessQos188.setter
    def ddsMetamodel_DdsLivelinessQos188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsLivelinessQos__ddsMetamodel_DdsLivelinessQos188", None)
        self.__ddsMetamodel_DdsLivelinessQos188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataReaderQosProfile187"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataReaderQosProfile187", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataReaderQosProfile187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataReaderQosProfile187"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataReaderQosProfile187", None)
                setattr(value, "ddsMetamodel_DdsDataReaderQosProfile187", self)

    @property
    def ddsMetamodel_DdsLivelinessQos140(self):
        return self.__ddsMetamodel_DdsLivelinessQos140

    @ddsMetamodel_DdsLivelinessQos140.setter
    def ddsMetamodel_DdsLivelinessQos140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsLivelinessQos__ddsMetamodel_DdsLivelinessQos140", None)
        self.__ddsMetamodel_DdsLivelinessQos140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile139"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile139", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataWriterQosProfile139"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataWriterQosProfile139", None)
                setattr(value, "ddsMetamodel_DdsDataWriterQosProfile139", self)

    @property
    def ddsMetamodel_DdsLivelinessQos(self):
        return self.__ddsMetamodel_DdsLivelinessQos

    @ddsMetamodel_DdsLivelinessQos.setter
    def ddsMetamodel_DdsLivelinessQos(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsLivelinessQos__ddsMetamodel_DdsLivelinessQos", None)
        self.__ddsMetamodel_DdsLivelinessQos = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsTopicQosProfile66"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsTopicQosProfile66", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsTopicQosProfile66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsTopicQosProfile66"):
                opp_val = getattr(value, "ddsMetamodel_DdsTopicQosProfile66", None)
                setattr(value, "ddsMetamodel_DdsTopicQosProfile66", self)

    @property
    def ddsMetamodel_DdsLivelinessQos92(self):
        return self.__ddsMetamodel_DdsLivelinessQos92

    @ddsMetamodel_DdsLivelinessQos92.setter
    def ddsMetamodel_DdsLivelinessQos92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsLivelinessQos__ddsMetamodel_DdsLivelinessQos92", None)
        self.__ddsMetamodel_DdsLivelinessQos92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDuration93"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDuration93", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDuration93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDuration93"):
                opp_val = getattr(value, "ddsMetamodel_DdsDuration93", None)
                setattr(value, "ddsMetamodel_DdsDuration93", self)

class ddsMetamodel_DdsDeadlineQos:

    pass
class ddsMetamodel_DdsLifespan:

    pass
class ddsMetamodel_DdsTransportPriorityQos:

    def __init__(self, value: str, ddsMetamodel_DdsTransportPriorityQos: "ddsMetamodel_DdsTopicQosProfile" = None, ddsMetamodel_DdsTransportPriorityQos146: "ddsMetamodel_DdsDataWriterQosProfile" = None):
        self.value = value
        self.ddsMetamodel_DdsTransportPriorityQos = ddsMetamodel_DdsTransportPriorityQos
        self.ddsMetamodel_DdsTransportPriorityQos146 = ddsMetamodel_DdsTransportPriorityQos146
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def ddsMetamodel_DdsTransportPriorityQos(self):
        return self.__ddsMetamodel_DdsTransportPriorityQos

    @ddsMetamodel_DdsTransportPriorityQos.setter
    def ddsMetamodel_DdsTransportPriorityQos(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsTransportPriorityQos__ddsMetamodel_DdsTransportPriorityQos", None)
        self.__ddsMetamodel_DdsTransportPriorityQos = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsTopicQosProfile78"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsTopicQosProfile78", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsTopicQosProfile78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsTopicQosProfile78"):
                opp_val = getattr(value, "ddsMetamodel_DdsTopicQosProfile78", None)
                setattr(value, "ddsMetamodel_DdsTopicQosProfile78", self)

    @property
    def ddsMetamodel_DdsTransportPriorityQos146(self):
        return self.__ddsMetamodel_DdsTransportPriorityQos146

    @ddsMetamodel_DdsTransportPriorityQos146.setter
    def ddsMetamodel_DdsTransportPriorityQos146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsTransportPriorityQos__ddsMetamodel_DdsTransportPriorityQos146", None)
        self.__ddsMetamodel_DdsTransportPriorityQos146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile145"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile145", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataWriterQosProfile145"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataWriterQosProfile145", None)
                setattr(value, "ddsMetamodel_DdsDataWriterQosProfile145", self)

class ddsMetamodel_DdsResourceLimits:

    def __init__(self, max_samples: str, max_instances: str, max_samples_per_instances: str, ddsMetamodel_DdsResourceLimits: "ddsMetamodel_DdsTopicQosProfile" = None, ddsMetamodel_DdsResourceLimits158: "ddsMetamodel_DdsDataWriterQosProfile" = None, ddsMetamodel_DdsResourceLimits206: "ddsMetamodel_DdsDataReaderQosProfile" = None):
        self.max_samples = max_samples
        self.max_instances = max_instances
        self.max_samples_per_instances = max_samples_per_instances
        self.ddsMetamodel_DdsResourceLimits = ddsMetamodel_DdsResourceLimits
        self.ddsMetamodel_DdsResourceLimits158 = ddsMetamodel_DdsResourceLimits158
        self.ddsMetamodel_DdsResourceLimits206 = ddsMetamodel_DdsResourceLimits206
        
    @property
    def max_samples(self) -> str:
        return self.__max_samples

    @max_samples.setter
    def max_samples(self, max_samples: str):
        self.__max_samples = max_samples

    @property
    def max_samples_per_instances(self) -> str:
        return self.__max_samples_per_instances

    @max_samples_per_instances.setter
    def max_samples_per_instances(self, max_samples_per_instances: str):
        self.__max_samples_per_instances = max_samples_per_instances

    @property
    def max_instances(self) -> str:
        return self.__max_instances

    @max_instances.setter
    def max_instances(self, max_instances: str):
        self.__max_instances = max_instances

    @property
    def ddsMetamodel_DdsResourceLimits206(self):
        return self.__ddsMetamodel_DdsResourceLimits206

    @ddsMetamodel_DdsResourceLimits206.setter
    def ddsMetamodel_DdsResourceLimits206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsResourceLimits__ddsMetamodel_DdsResourceLimits206", None)
        self.__ddsMetamodel_DdsResourceLimits206 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataReaderQosProfile205"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataReaderQosProfile205", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataReaderQosProfile205", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataReaderQosProfile205"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataReaderQosProfile205", None)
                setattr(value, "ddsMetamodel_DdsDataReaderQosProfile205", self)

    @property
    def ddsMetamodel_DdsResourceLimits(self):
        return self.__ddsMetamodel_DdsResourceLimits

    @ddsMetamodel_DdsResourceLimits.setter
    def ddsMetamodel_DdsResourceLimits(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsResourceLimits__ddsMetamodel_DdsResourceLimits", None)
        self.__ddsMetamodel_DdsResourceLimits = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsTopicQosProfile76"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsTopicQosProfile76", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsTopicQosProfile76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsTopicQosProfile76"):
                opp_val = getattr(value, "ddsMetamodel_DdsTopicQosProfile76", None)
                setattr(value, "ddsMetamodel_DdsTopicQosProfile76", self)

    @property
    def ddsMetamodel_DdsResourceLimits158(self):
        return self.__ddsMetamodel_DdsResourceLimits158

    @ddsMetamodel_DdsResourceLimits158.setter
    def ddsMetamodel_DdsResourceLimits158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsResourceLimits__ddsMetamodel_DdsResourceLimits158", None)
        self.__ddsMetamodel_DdsResourceLimits158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile157"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile157", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataWriterQosProfile157"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataWriterQosProfile157", None)
                setattr(value, "ddsMetamodel_DdsDataWriterQosProfile157", self)

class ddsMetamodel_DdsHistoryQos:

    def __init__(self, kind: str, depth: str, ddsMetamodel_DdsHistoryQos: "ddsMetamodel_DdsTopicQosProfile" = None, ddsMetamodel_DdsHistoryQos155: "ddsMetamodel_DdsDataWriterQosProfile" = None, ddsMetamodel_DdsHistoryQos203: "ddsMetamodel_DdsDataReaderQosProfile" = None):
        self.kind = kind
        self.depth = depth
        self.ddsMetamodel_DdsHistoryQos = ddsMetamodel_DdsHistoryQos
        self.ddsMetamodel_DdsHistoryQos155 = ddsMetamodel_DdsHistoryQos155
        self.ddsMetamodel_DdsHistoryQos203 = ddsMetamodel_DdsHistoryQos203
        
    @property
    def depth(self) -> str:
        return self.__depth

    @depth.setter
    def depth(self, depth: str):
        self.__depth = depth

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def ddsMetamodel_DdsHistoryQos155(self):
        return self.__ddsMetamodel_DdsHistoryQos155

    @ddsMetamodel_DdsHistoryQos155.setter
    def ddsMetamodel_DdsHistoryQos155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsHistoryQos__ddsMetamodel_DdsHistoryQos155", None)
        self.__ddsMetamodel_DdsHistoryQos155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile154"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile154", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataWriterQosProfile154"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataWriterQosProfile154", None)
                setattr(value, "ddsMetamodel_DdsDataWriterQosProfile154", self)

    @property
    def ddsMetamodel_DdsHistoryQos203(self):
        return self.__ddsMetamodel_DdsHistoryQos203

    @ddsMetamodel_DdsHistoryQos203.setter
    def ddsMetamodel_DdsHistoryQos203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsHistoryQos__ddsMetamodel_DdsHistoryQos203", None)
        self.__ddsMetamodel_DdsHistoryQos203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataReaderQosProfile202"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataReaderQosProfile202", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataReaderQosProfile202", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataReaderQosProfile202"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataReaderQosProfile202", None)
                setattr(value, "ddsMetamodel_DdsDataReaderQosProfile202", self)

    @property
    def ddsMetamodel_DdsHistoryQos(self):
        return self.__ddsMetamodel_DdsHistoryQos

    @ddsMetamodel_DdsHistoryQos.setter
    def ddsMetamodel_DdsHistoryQos(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsHistoryQos__ddsMetamodel_DdsHistoryQos", None)
        self.__ddsMetamodel_DdsHistoryQos = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsTopicQosProfile74"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsTopicQosProfile74", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsTopicQosProfile74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsTopicQosProfile74"):
                opp_val = getattr(value, "ddsMetamodel_DdsTopicQosProfile74", None)
                setattr(value, "ddsMetamodel_DdsTopicQosProfile74", self)

class ddsMetamodel_DdsDestinationOrderQos:

    def __init__(self, kind: str, ddsMetamodel_DdsDestinationOrderQos: "ddsMetamodel_DdsTopicQosProfile" = None, ddsMetamodel_DdsDestinationOrderQos152: "ddsMetamodel_DdsDataWriterQosProfile" = None, ddsMetamodel_DdsDestinationOrderQos200: "ddsMetamodel_DdsDataReaderQosProfile" = None):
        self.kind = kind
        self.ddsMetamodel_DdsDestinationOrderQos = ddsMetamodel_DdsDestinationOrderQos
        self.ddsMetamodel_DdsDestinationOrderQos152 = ddsMetamodel_DdsDestinationOrderQos152
        self.ddsMetamodel_DdsDestinationOrderQos200 = ddsMetamodel_DdsDestinationOrderQos200
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def ddsMetamodel_DdsDestinationOrderQos152(self):
        return self.__ddsMetamodel_DdsDestinationOrderQos152

    @ddsMetamodel_DdsDestinationOrderQos152.setter
    def ddsMetamodel_DdsDestinationOrderQos152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDestinationOrderQos__ddsMetamodel_DdsDestinationOrderQos152", None)
        self.__ddsMetamodel_DdsDestinationOrderQos152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile151"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile151", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataWriterQosProfile151"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataWriterQosProfile151", None)
                setattr(value, "ddsMetamodel_DdsDataWriterQosProfile151", self)

    @property
    def ddsMetamodel_DdsDestinationOrderQos(self):
        return self.__ddsMetamodel_DdsDestinationOrderQos

    @ddsMetamodel_DdsDestinationOrderQos.setter
    def ddsMetamodel_DdsDestinationOrderQos(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDestinationOrderQos__ddsMetamodel_DdsDestinationOrderQos", None)
        self.__ddsMetamodel_DdsDestinationOrderQos = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsTopicQosProfile72"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsTopicQosProfile72", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsTopicQosProfile72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsTopicQosProfile72"):
                opp_val = getattr(value, "ddsMetamodel_DdsTopicQosProfile72", None)
                setattr(value, "ddsMetamodel_DdsTopicQosProfile72", self)

    @property
    def ddsMetamodel_DdsDestinationOrderQos200(self):
        return self.__ddsMetamodel_DdsDestinationOrderQos200

    @ddsMetamodel_DdsDestinationOrderQos200.setter
    def ddsMetamodel_DdsDestinationOrderQos200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDestinationOrderQos__ddsMetamodel_DdsDestinationOrderQos200", None)
        self.__ddsMetamodel_DdsDestinationOrderQos200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataReaderQosProfile199"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataReaderQosProfile199", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataReaderQosProfile199", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataReaderQosProfile199"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataReaderQosProfile199", None)
                setattr(value, "ddsMetamodel_DdsDataReaderQosProfile199", self)

class ddsMetamodel_DdsReliabilityQos:

    def __init__(self, kind: str, ddsMetamodel_DdsReliabilityQos: "ddsMetamodel_DdsTopicQosProfile" = None, ddsMetamodel_DdsReliabilityQos97: "ddsMetamodel_DdsDuration" = None, ddsMetamodel_DdsReliabilityQos143: "ddsMetamodel_DdsDataWriterQosProfile" = None, ddsMetamodel_DdsReliabilityQos197: "ddsMetamodel_DdsDataReaderQosProfile" = None):
        self.kind = kind
        self.ddsMetamodel_DdsReliabilityQos = ddsMetamodel_DdsReliabilityQos
        self.ddsMetamodel_DdsReliabilityQos97 = ddsMetamodel_DdsReliabilityQos97
        self.ddsMetamodel_DdsReliabilityQos143 = ddsMetamodel_DdsReliabilityQos143
        self.ddsMetamodel_DdsReliabilityQos197 = ddsMetamodel_DdsReliabilityQos197
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def ddsMetamodel_DdsReliabilityQos143(self):
        return self.__ddsMetamodel_DdsReliabilityQos143

    @ddsMetamodel_DdsReliabilityQos143.setter
    def ddsMetamodel_DdsReliabilityQos143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsReliabilityQos__ddsMetamodel_DdsReliabilityQos143", None)
        self.__ddsMetamodel_DdsReliabilityQos143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile142"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile142", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataWriterQosProfile142"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataWriterQosProfile142", None)
                setattr(value, "ddsMetamodel_DdsDataWriterQosProfile142", self)

    @property
    def ddsMetamodel_DdsReliabilityQos(self):
        return self.__ddsMetamodel_DdsReliabilityQos

    @ddsMetamodel_DdsReliabilityQos.setter
    def ddsMetamodel_DdsReliabilityQos(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsReliabilityQos__ddsMetamodel_DdsReliabilityQos", None)
        self.__ddsMetamodel_DdsReliabilityQos = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsTopicQosProfile70"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsTopicQosProfile70", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsTopicQosProfile70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsTopicQosProfile70"):
                opp_val = getattr(value, "ddsMetamodel_DdsTopicQosProfile70", None)
                setattr(value, "ddsMetamodel_DdsTopicQosProfile70", self)

    @property
    def ddsMetamodel_DdsReliabilityQos197(self):
        return self.__ddsMetamodel_DdsReliabilityQos197

    @ddsMetamodel_DdsReliabilityQos197.setter
    def ddsMetamodel_DdsReliabilityQos197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsReliabilityQos__ddsMetamodel_DdsReliabilityQos197", None)
        self.__ddsMetamodel_DdsReliabilityQos197 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataReaderQosProfile196"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataReaderQosProfile196", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataReaderQosProfile196", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataReaderQosProfile196"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataReaderQosProfile196", None)
                setattr(value, "ddsMetamodel_DdsDataReaderQosProfile196", self)

    @property
    def ddsMetamodel_DdsReliabilityQos97(self):
        return self.__ddsMetamodel_DdsReliabilityQos97

    @ddsMetamodel_DdsReliabilityQos97.setter
    def ddsMetamodel_DdsReliabilityQos97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsReliabilityQos__ddsMetamodel_DdsReliabilityQos97", None)
        self.__ddsMetamodel_DdsReliabilityQos97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDuration98"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDuration98", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDuration98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDuration98"):
                opp_val = getattr(value, "ddsMetamodel_DdsDuration98", None)
                setattr(value, "ddsMetamodel_DdsDuration98", self)

class ddsMetamodel_DdsLatencyBudgetQos:

    pass
class ddsMetamodel_DdsDurabilityServiceQos:

    def __init__(self, history_kind: str, history_depth: str, max_samples: str, max_instances: str, max_samples_per_instances: str, ddsMetamodel_DdsDurabilityServiceQos: "ddsMetamodel_DdsTopicQosProfile" = None, ddsMetamodel_DdsDurabilityServiceQos84: "ddsMetamodel_DdsDuration" = None):
        self.history_kind = history_kind
        self.history_depth = history_depth
        self.max_samples = max_samples
        self.max_instances = max_instances
        self.max_samples_per_instances = max_samples_per_instances
        self.ddsMetamodel_DdsDurabilityServiceQos = ddsMetamodel_DdsDurabilityServiceQos
        self.ddsMetamodel_DdsDurabilityServiceQos84 = ddsMetamodel_DdsDurabilityServiceQos84
        
    @property
    def max_instances(self) -> str:
        return self.__max_instances

    @max_instances.setter
    def max_instances(self, max_instances: str):
        self.__max_instances = max_instances

    @property
    def max_samples_per_instances(self) -> str:
        return self.__max_samples_per_instances

    @max_samples_per_instances.setter
    def max_samples_per_instances(self, max_samples_per_instances: str):
        self.__max_samples_per_instances = max_samples_per_instances

    @property
    def max_samples(self) -> str:
        return self.__max_samples

    @max_samples.setter
    def max_samples(self, max_samples: str):
        self.__max_samples = max_samples

    @property
    def history_kind(self) -> str:
        return self.__history_kind

    @history_kind.setter
    def history_kind(self, history_kind: str):
        self.__history_kind = history_kind

    @property
    def history_depth(self) -> str:
        return self.__history_depth

    @history_depth.setter
    def history_depth(self, history_depth: str):
        self.__history_depth = history_depth

    @property
    def ddsMetamodel_DdsDurabilityServiceQos84(self):
        return self.__ddsMetamodel_DdsDurabilityServiceQos84

    @ddsMetamodel_DdsDurabilityServiceQos84.setter
    def ddsMetamodel_DdsDurabilityServiceQos84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDurabilityServiceQos__ddsMetamodel_DdsDurabilityServiceQos84", None)
        self.__ddsMetamodel_DdsDurabilityServiceQos84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDuration"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDuration", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDuration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDuration"):
                opp_val = getattr(value, "ddsMetamodel_DdsDuration", None)
                setattr(value, "ddsMetamodel_DdsDuration", self)

    @property
    def ddsMetamodel_DdsDurabilityServiceQos(self):
        return self.__ddsMetamodel_DdsDurabilityServiceQos

    @ddsMetamodel_DdsDurabilityServiceQos.setter
    def ddsMetamodel_DdsDurabilityServiceQos(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDurabilityServiceQos__ddsMetamodel_DdsDurabilityServiceQos", None)
        self.__ddsMetamodel_DdsDurabilityServiceQos = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsTopicQosProfile62"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsTopicQosProfile62", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsTopicQosProfile62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsTopicQosProfile62"):
                opp_val = getattr(value, "ddsMetamodel_DdsTopicQosProfile62", None)
                setattr(value, "ddsMetamodel_DdsTopicQosProfile62", self)

class ddsMetamodel_DdsDurabilityQos:

    def __init__(self, kind: str, ddsMetamodel_DdsDurabilityQos: "ddsMetamodel_DdsTopicQosProfile" = None, ddsMetamodel_DdsDurabilityQos126: "ddsMetamodel_DdsDataWriterQosProfile" = None, ddsMetamodel_DdsDurabilityQos179: "ddsMetamodel_DdsDataReaderQosProfile" = None):
        self.kind = kind
        self.ddsMetamodel_DdsDurabilityQos = ddsMetamodel_DdsDurabilityQos
        self.ddsMetamodel_DdsDurabilityQos126 = ddsMetamodel_DdsDurabilityQos126
        self.ddsMetamodel_DdsDurabilityQos179 = ddsMetamodel_DdsDurabilityQos179
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def ddsMetamodel_DdsDurabilityQos179(self):
        return self.__ddsMetamodel_DdsDurabilityQos179

    @ddsMetamodel_DdsDurabilityQos179.setter
    def ddsMetamodel_DdsDurabilityQos179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDurabilityQos__ddsMetamodel_DdsDurabilityQos179", None)
        self.__ddsMetamodel_DdsDurabilityQos179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataReaderQosProfile178"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataReaderQosProfile178", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataReaderQosProfile178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataReaderQosProfile178"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataReaderQosProfile178", None)
                setattr(value, "ddsMetamodel_DdsDataReaderQosProfile178", self)

    @property
    def ddsMetamodel_DdsDurabilityQos126(self):
        return self.__ddsMetamodel_DdsDurabilityQos126

    @ddsMetamodel_DdsDurabilityQos126.setter
    def ddsMetamodel_DdsDurabilityQos126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDurabilityQos__ddsMetamodel_DdsDurabilityQos126", None)
        self.__ddsMetamodel_DdsDurabilityQos126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile125"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile125", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataWriterQosProfile125"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataWriterQosProfile125", None)
                setattr(value, "ddsMetamodel_DdsDataWriterQosProfile125", self)

    @property
    def ddsMetamodel_DdsDurabilityQos(self):
        return self.__ddsMetamodel_DdsDurabilityQos

    @ddsMetamodel_DdsDurabilityQos.setter
    def ddsMetamodel_DdsDurabilityQos(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDurabilityQos__ddsMetamodel_DdsDurabilityQos", None)
        self.__ddsMetamodel_DdsDurabilityQos = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsTopicQosProfile60"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsTopicQosProfile60", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsTopicQosProfile60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsTopicQosProfile60"):
                opp_val = getattr(value, "ddsMetamodel_DdsTopicQosProfile60", None)
                setattr(value, "ddsMetamodel_DdsTopicQosProfile60", self)

class ddsMetamodel_DdsTopicDataQos:

    def __init__(self, value: str, ddsMetamodel_DdsTopicDataQos: "ddsMetamodel_DdsTopicQosProfile" = None):
        self.value = value
        self.ddsMetamodel_DdsTopicDataQos = ddsMetamodel_DdsTopicDataQos
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def ddsMetamodel_DdsTopicDataQos(self):
        return self.__ddsMetamodel_DdsTopicDataQos

    @ddsMetamodel_DdsTopicDataQos.setter
    def ddsMetamodel_DdsTopicDataQos(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsTopicDataQos__ddsMetamodel_DdsTopicDataQos", None)
        self.__ddsMetamodel_DdsTopicDataQos = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsTopicQosProfile58"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsTopicQosProfile58", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsTopicQosProfile58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsTopicQosProfile58"):
                opp_val = getattr(value, "ddsMetamodel_DdsTopicQosProfile58", None)
                setattr(value, "ddsMetamodel_DdsTopicQosProfile58", self)

class ddsMetamodel_DdsEntityFactoryQos:

    def __init__(self, autoenable_created_entities: bool, ddsMetamodel_DdsEntityFactoryQos: "ddsMetamodel_DdsDomainParticipantQosProfile" = None, ddsMetamodel_DdsEntityFactoryQos116: "ddsMetamodel_DdsPublisherQosProfile" = None, ddsMetamodel_DdsEntityFactoryQos167: "ddsMetamodel_DdsSubscriberQosProfile" = None):
        self.autoenable_created_entities = autoenable_created_entities
        self.ddsMetamodel_DdsEntityFactoryQos = ddsMetamodel_DdsEntityFactoryQos
        self.ddsMetamodel_DdsEntityFactoryQos116 = ddsMetamodel_DdsEntityFactoryQos116
        self.ddsMetamodel_DdsEntityFactoryQos167 = ddsMetamodel_DdsEntityFactoryQos167
        
    @property
    def autoenable_created_entities(self) -> bool:
        return self.__autoenable_created_entities

    @autoenable_created_entities.setter
    def autoenable_created_entities(self, autoenable_created_entities: bool):
        self.__autoenable_created_entities = autoenable_created_entities

    @property
    def ddsMetamodel_DdsEntityFactoryQos(self):
        return self.__ddsMetamodel_DdsEntityFactoryQos

    @ddsMetamodel_DdsEntityFactoryQos.setter
    def ddsMetamodel_DdsEntityFactoryQos(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsEntityFactoryQos__ddsMetamodel_DdsEntityFactoryQos", None)
        self.__ddsMetamodel_DdsEntityFactoryQos = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDomainParticipantQosProfile56"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDomainParticipantQosProfile56", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDomainParticipantQosProfile56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDomainParticipantQosProfile56"):
                opp_val = getattr(value, "ddsMetamodel_DdsDomainParticipantQosProfile56", None)
                setattr(value, "ddsMetamodel_DdsDomainParticipantQosProfile56", self)

    @property
    def ddsMetamodel_DdsEntityFactoryQos116(self):
        return self.__ddsMetamodel_DdsEntityFactoryQos116

    @ddsMetamodel_DdsEntityFactoryQos116.setter
    def ddsMetamodel_DdsEntityFactoryQos116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsEntityFactoryQos__ddsMetamodel_DdsEntityFactoryQos116", None)
        self.__ddsMetamodel_DdsEntityFactoryQos116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsPublisherQosProfile115"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsPublisherQosProfile115", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsPublisherQosProfile115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsPublisherQosProfile115"):
                opp_val = getattr(value, "ddsMetamodel_DdsPublisherQosProfile115", None)
                setattr(value, "ddsMetamodel_DdsPublisherQosProfile115", self)

    @property
    def ddsMetamodel_DdsEntityFactoryQos167(self):
        return self.__ddsMetamodel_DdsEntityFactoryQos167

    @ddsMetamodel_DdsEntityFactoryQos167.setter
    def ddsMetamodel_DdsEntityFactoryQos167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsEntityFactoryQos__ddsMetamodel_DdsEntityFactoryQos167", None)
        self.__ddsMetamodel_DdsEntityFactoryQos167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsSubscriberQosProfile166"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsSubscriberQosProfile166", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsSubscriberQosProfile166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsSubscriberQosProfile166"):
                opp_val = getattr(value, "ddsMetamodel_DdsSubscriberQosProfile166", None)
                setattr(value, "ddsMetamodel_DdsSubscriberQosProfile166", self)

class ddsMetamodel_DdsUserDataQos:

    def __init__(self, value: str, ddsMetamodel_DdsUserDataQos: "ddsMetamodel_DdsDomainParticipantQosProfile" = None, ddsMetamodel_DdsUserDataQos123: "ddsMetamodel_DdsDataWriterQosProfile" = None, ddsMetamodel_DdsUserDataQos176: "ddsMetamodel_DdsDataReaderQosProfile" = None):
        self.value = value
        self.ddsMetamodel_DdsUserDataQos = ddsMetamodel_DdsUserDataQos
        self.ddsMetamodel_DdsUserDataQos123 = ddsMetamodel_DdsUserDataQos123
        self.ddsMetamodel_DdsUserDataQos176 = ddsMetamodel_DdsUserDataQos176
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def ddsMetamodel_DdsUserDataQos123(self):
        return self.__ddsMetamodel_DdsUserDataQos123

    @ddsMetamodel_DdsUserDataQos123.setter
    def ddsMetamodel_DdsUserDataQos123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsUserDataQos__ddsMetamodel_DdsUserDataQos123", None)
        self.__ddsMetamodel_DdsUserDataQos123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile122"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile122", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataWriterQosProfile122"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataWriterQosProfile122", None)
                setattr(value, "ddsMetamodel_DdsDataWriterQosProfile122", self)

    @property
    def ddsMetamodel_DdsUserDataQos176(self):
        return self.__ddsMetamodel_DdsUserDataQos176

    @ddsMetamodel_DdsUserDataQos176.setter
    def ddsMetamodel_DdsUserDataQos176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsUserDataQos__ddsMetamodel_DdsUserDataQos176", None)
        self.__ddsMetamodel_DdsUserDataQos176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataReaderQosProfile175"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataReaderQosProfile175", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataReaderQosProfile175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataReaderQosProfile175"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataReaderQosProfile175", None)
                setattr(value, "ddsMetamodel_DdsDataReaderQosProfile175", self)

    @property
    def ddsMetamodel_DdsUserDataQos(self):
        return self.__ddsMetamodel_DdsUserDataQos

    @ddsMetamodel_DdsUserDataQos.setter
    def ddsMetamodel_DdsUserDataQos(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsUserDataQos__ddsMetamodel_DdsUserDataQos", None)
        self.__ddsMetamodel_DdsUserDataQos = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDomainParticipantQosProfile54"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDomainParticipantQosProfile54", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDomainParticipantQosProfile54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDomainParticipantQosProfile54"):
                opp_val = getattr(value, "ddsMetamodel_DdsDomainParticipantQosProfile54", None)
                setattr(value, "ddsMetamodel_DdsDomainParticipantQosProfile54", self)

class DdsQosProfile:

    pass
class ddsMetamodel_DdsDataWriterQosProfile(DdsQosProfile):

    pass
class ddsMetamodel_DdsDataWriterListener:

    def __init__(self, name: str, listenedStatus: str, ddsMetamodel_DdsDataWriterListener: "ddsMetamodel_DdsDataWriter" = None):
        self.name = name
        self.listenedStatus = listenedStatus
        self.ddsMetamodel_DdsDataWriterListener = ddsMetamodel_DdsDataWriterListener
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def listenedStatus(self) -> str:
        return self.__listenedStatus

    @listenedStatus.setter
    def listenedStatus(self, listenedStatus: str):
        self.__listenedStatus = listenedStatus

    @property
    def ddsMetamodel_DdsDataWriterListener(self):
        return self.__ddsMetamodel_DdsDataWriterListener

    @ddsMetamodel_DdsDataWriterListener.setter
    def ddsMetamodel_DdsDataWriterListener(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataWriterListener__ddsMetamodel_DdsDataWriterListener", None)
        self.__ddsMetamodel_DdsDataWriterListener = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataWriter38"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataWriter38", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataWriter38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataWriter38"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataWriter38", None)
                setattr(value, "ddsMetamodel_DdsDataWriter38", self)

class ddsMetamodel_DdsStructuredField:

    def __init__(self, isKey: bool, maxMultiplicity: int, fieldName: str, DdsStructuredField: "ddsMetamodel_DdsDataStructure" = None, ddsMetamodel_DdsStructuredField: "ddsMetamodel_DdsDataStructure" = None, structuredFields: "ddsMetamodel_DdsDataStructure" = None):
        self.isKey = isKey
        self.maxMultiplicity = maxMultiplicity
        self.fieldName = fieldName
        self.DdsStructuredField = DdsStructuredField
        self.ddsMetamodel_DdsStructuredField = ddsMetamodel_DdsStructuredField
        self.structuredFields = structuredFields
        
    @property
    def isKey(self) -> bool:
        return self.__isKey

    @isKey.setter
    def isKey(self, isKey: bool):
        self.__isKey = isKey

    @property
    def maxMultiplicity(self) -> int:
        return self.__maxMultiplicity

    @maxMultiplicity.setter
    def maxMultiplicity(self, maxMultiplicity: int):
        self.__maxMultiplicity = maxMultiplicity

    @property
    def fieldName(self) -> str:
        return self.__fieldName

    @fieldName.setter
    def fieldName(self, fieldName: str):
        self.__fieldName = fieldName

    @property
    def DdsStructuredField(self):
        return self.__DdsStructuredField

    @DdsStructuredField.setter
    def DdsStructuredField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsStructuredField__DdsStructuredField", None)
        self.__DdsStructuredField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataStructure"):
                opp_val = getattr(old_value, "dataStructure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataStructure"):
                opp_val = getattr(value, "dataStructure", None)
                if opp_val is None:
                    setattr(value, "dataStructure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def structuredFields(self):
        return self.__structuredFields

    @structuredFields.setter
    def structuredFields(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsStructuredField__structuredFields", None)
        self.__structuredFields = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DdsDataStructure221"):
                opp_val = getattr(old_value, "DdsDataStructure221", None)
                if opp_val == self:
                    setattr(old_value, "DdsDataStructure221", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DdsDataStructure221"):
                opp_val = getattr(value, "DdsDataStructure221", None)
                setattr(value, "DdsDataStructure221", self)

    @property
    def ddsMetamodel_DdsStructuredField(self):
        return self.__ddsMetamodel_DdsStructuredField

    @ddsMetamodel_DdsStructuredField.setter
    def ddsMetamodel_DdsStructuredField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsStructuredField__ddsMetamodel_DdsStructuredField", None)
        self.__ddsMetamodel_DdsStructuredField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataStructure219"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataStructure219", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataStructure219", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataStructure219"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataStructure219", None)
                setattr(value, "ddsMetamodel_DdsDataStructure219", self)

class ddsMetamodel_DdsDataField:

    def __init__(self, maxMultiplicity: int, fieldType: str, fieldName: str, isKey: bool, ddsMetamodel_DdsDataField: "ddsMetamodel_DdsDataStructure" = None):
        self.maxMultiplicity = maxMultiplicity
        self.fieldType = fieldType
        self.fieldName = fieldName
        self.isKey = isKey
        self.ddsMetamodel_DdsDataField = ddsMetamodel_DdsDataField
        
    @property
    def fieldType(self) -> str:
        return self.__fieldType

    @fieldType.setter
    def fieldType(self, fieldType: str):
        self.__fieldType = fieldType

    @property
    def isKey(self) -> bool:
        return self.__isKey

    @isKey.setter
    def isKey(self, isKey: bool):
        self.__isKey = isKey

    @property
    def maxMultiplicity(self) -> int:
        return self.__maxMultiplicity

    @maxMultiplicity.setter
    def maxMultiplicity(self, maxMultiplicity: int):
        self.__maxMultiplicity = maxMultiplicity

    @property
    def fieldName(self) -> str:
        return self.__fieldName

    @fieldName.setter
    def fieldName(self, fieldName: str):
        self.__fieldName = fieldName

    @property
    def ddsMetamodel_DdsDataField(self):
        return self.__ddsMetamodel_DdsDataField

    @ddsMetamodel_DdsDataField.setter
    def ddsMetamodel_DdsDataField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataField__ddsMetamodel_DdsDataField", None)
        self.__ddsMetamodel_DdsDataField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataStructure49"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataStructure49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataStructure49"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataStructure49", None)
                if opp_val is None:
                    setattr(value, "ddsMetamodel_DdsDataStructure49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ddsMetamodel_DdsSystem:

    def __init__(self, systemName: str, DdsSystem: "ddsMetamodel_DdsDataModule" = None, ddsMetamodel_DdsSystem: set["ddsMetamodel_DdsHost"] = None, ddsMetamodel_DdsSystem237: set["ddsMetamodel_DdsQosProfile"] = None, containingSystem: set["ddsMetamodel_DdsDataModule"] = None, ddsMetamodel_DdsSystem241: set["ddsMetamodel_DdsTopic"] = None):
        self.systemName = systemName
        self.DdsSystem = DdsSystem
        self.ddsMetamodel_DdsSystem = ddsMetamodel_DdsSystem if ddsMetamodel_DdsSystem is not None else set()
        self.ddsMetamodel_DdsSystem237 = ddsMetamodel_DdsSystem237 if ddsMetamodel_DdsSystem237 is not None else set()
        self.containingSystem = containingSystem if containingSystem is not None else set()
        self.ddsMetamodel_DdsSystem241 = ddsMetamodel_DdsSystem241 if ddsMetamodel_DdsSystem241 is not None else set()
        
    @property
    def systemName(self) -> str:
        return self.__systemName

    @systemName.setter
    def systemName(self, systemName: str):
        self.__systemName = systemName

    @property
    def ddsMetamodel_DdsSystem241(self):
        return self.__ddsMetamodel_DdsSystem241

    @ddsMetamodel_DdsSystem241.setter
    def ddsMetamodel_DdsSystem241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsSystem__ddsMetamodel_DdsSystem241", None)
        self.__ddsMetamodel_DdsSystem241 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ddsMetamodel_DdsTopic242"):
                    opp_val = getattr(item, "ddsMetamodel_DdsTopic242", None)
                    
                    if opp_val == self:
                        setattr(item, "ddsMetamodel_DdsTopic242", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ddsMetamodel_DdsTopic242"):
                    opp_val = getattr(item, "ddsMetamodel_DdsTopic242", None)
                    
                    setattr(item, "ddsMetamodel_DdsTopic242", self)
                    

    @property
    def ddsMetamodel_DdsSystem(self):
        return self.__ddsMetamodel_DdsSystem

    @ddsMetamodel_DdsSystem.setter
    def ddsMetamodel_DdsSystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsSystem__ddsMetamodel_DdsSystem", None)
        self.__ddsMetamodel_DdsSystem = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ddsMetamodel_DdsHost"):
                    opp_val = getattr(item, "ddsMetamodel_DdsHost", None)
                    
                    if opp_val == self:
                        setattr(item, "ddsMetamodel_DdsHost", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ddsMetamodel_DdsHost"):
                    opp_val = getattr(item, "ddsMetamodel_DdsHost", None)
                    
                    setattr(item, "ddsMetamodel_DdsHost", self)
                    

    @property
    def containingSystem(self):
        return self.__containingSystem

    @containingSystem.setter
    def containingSystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsSystem__containingSystem", None)
        self.__containingSystem = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DdsDataModule239"):
                    opp_val = getattr(item, "DdsDataModule239", None)
                    
                    if opp_val == self:
                        setattr(item, "DdsDataModule239", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DdsDataModule239"):
                    opp_val = getattr(item, "DdsDataModule239", None)
                    
                    setattr(item, "DdsDataModule239", self)
                    

    @property
    def DdsSystem(self):
        return self.__DdsSystem

    @DdsSystem.setter
    def DdsSystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsSystem__DdsSystem", None)
        self.__DdsSystem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataModules"):
                opp_val = getattr(old_value, "dataModules", None)
                if opp_val == self:
                    setattr(old_value, "dataModules", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataModules"):
                opp_val = getattr(value, "dataModules", None)
                setattr(value, "dataModules", self)

    @property
    def ddsMetamodel_DdsSystem237(self):
        return self.__ddsMetamodel_DdsSystem237

    @ddsMetamodel_DdsSystem237.setter
    def ddsMetamodel_DdsSystem237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsSystem__ddsMetamodel_DdsSystem237", None)
        self.__ddsMetamodel_DdsSystem237 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ddsMetamodel_DdsQosProfile"):
                    opp_val = getattr(item, "ddsMetamodel_DdsQosProfile", None)
                    
                    if opp_val == self:
                        setattr(item, "ddsMetamodel_DdsQosProfile", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ddsMetamodel_DdsQosProfile"):
                    opp_val = getattr(item, "ddsMetamodel_DdsQosProfile", None)
                    
                    setattr(item, "ddsMetamodel_DdsQosProfile", self)
                    

class ddsMetamodel_DdsDataModule:

    def __init__(self, moduleName: str, containerDataModule: set["ddsMetamodel_DdsDataStructure"] = None, DdsDataModule: "ddsMetamodel_DdsDataModule" = None, containingModule: set["ddsMetamodel_DdsDataModule"] = None, dataModules: "ddsMetamodel_DdsSystem" = None, DdsDataModule47: "ddsMetamodel_DdsDataModule" = None, innerModules: "ddsMetamodel_DdsDataModule" = None, DdsDataModule52: "ddsMetamodel_DdsDataStructure" = None, DdsDataModule239: "ddsMetamodel_DdsSystem" = None):
        self.moduleName = moduleName
        self.containerDataModule = containerDataModule if containerDataModule is not None else set()
        self.DdsDataModule = DdsDataModule
        self.containingModule = containingModule if containingModule is not None else set()
        self.dataModules = dataModules
        self.DdsDataModule47 = DdsDataModule47
        self.innerModules = innerModules
        self.DdsDataModule52 = DdsDataModule52
        self.DdsDataModule239 = DdsDataModule239
        
    @property
    def moduleName(self) -> str:
        return self.__moduleName

    @moduleName.setter
    def moduleName(self, moduleName: str):
        self.__moduleName = moduleName

    @property
    def containingModule(self):
        return self.__containingModule

    @containingModule.setter
    def containingModule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataModule__containingModule", None)
        self.__containingModule = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DdsDataModule"):
                    opp_val = getattr(item, "DdsDataModule", None)
                    
                    if opp_val == self:
                        setattr(item, "DdsDataModule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DdsDataModule"):
                    opp_val = getattr(item, "DdsDataModule", None)
                    
                    setattr(item, "DdsDataModule", self)
                    

    @property
    def innerModules(self):
        return self.__innerModules

    @innerModules.setter
    def innerModules(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataModule__innerModules", None)
        self.__innerModules = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DdsDataModule47"):
                opp_val = getattr(old_value, "DdsDataModule47", None)
                if opp_val == self:
                    setattr(old_value, "DdsDataModule47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DdsDataModule47"):
                opp_val = getattr(value, "DdsDataModule47", None)
                setattr(value, "DdsDataModule47", self)

    @property
    def DdsDataModule52(self):
        return self.__DdsDataModule52

    @DdsDataModule52.setter
    def DdsDataModule52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataModule__DdsDataModule52", None)
        self.__DdsDataModule52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataStructures"):
                opp_val = getattr(old_value, "dataStructures", None)
                if opp_val == self:
                    setattr(old_value, "dataStructures", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataStructures"):
                opp_val = getattr(value, "dataStructures", None)
                setattr(value, "dataStructures", self)

    @property
    def containerDataModule(self):
        return self.__containerDataModule

    @containerDataModule.setter
    def containerDataModule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataModule__containerDataModule", None)
        self.__containerDataModule = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DdsDataStructure"):
                    opp_val = getattr(item, "DdsDataStructure", None)
                    
                    if opp_val == self:
                        setattr(item, "DdsDataStructure", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DdsDataStructure"):
                    opp_val = getattr(item, "DdsDataStructure", None)
                    
                    setattr(item, "DdsDataStructure", self)
                    

    @property
    def DdsDataModule(self):
        return self.__DdsDataModule

    @DdsDataModule.setter
    def DdsDataModule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataModule__DdsDataModule", None)
        self.__DdsDataModule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containingModule"):
                opp_val = getattr(old_value, "containingModule", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containingModule"):
                opp_val = getattr(value, "containingModule", None)
                if opp_val is None:
                    setattr(value, "containingModule", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DdsDataModule47(self):
        return self.__DdsDataModule47

    @DdsDataModule47.setter
    def DdsDataModule47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataModule__DdsDataModule47", None)
        self.__DdsDataModule47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "innerModules"):
                opp_val = getattr(old_value, "innerModules", None)
                if opp_val == self:
                    setattr(old_value, "innerModules", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "innerModules"):
                opp_val = getattr(value, "innerModules", None)
                setattr(value, "innerModules", self)

    @property
    def DdsDataModule239(self):
        return self.__DdsDataModule239

    @DdsDataModule239.setter
    def DdsDataModule239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataModule__DdsDataModule239", None)
        self.__DdsDataModule239 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containingSystem"):
                opp_val = getattr(old_value, "containingSystem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containingSystem"):
                opp_val = getattr(value, "containingSystem", None)
                if opp_val is None:
                    setattr(value, "containingSystem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dataModules(self):
        return self.__dataModules

    @dataModules.setter
    def dataModules(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataModule__dataModules", None)
        self.__dataModules = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DdsSystem"):
                opp_val = getattr(old_value, "DdsSystem", None)
                if opp_val == self:
                    setattr(old_value, "DdsSystem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DdsSystem"):
                opp_val = getattr(value, "DdsSystem", None)
                setattr(value, "DdsSystem", self)

class ddsMetamodel_DdsPublisherQosProfile(DdsQosProfile):

    pass
class ddsMetamodel_DdsPublisherListener:

    def __init__(self, listenedStatus: str, name: str, ddsMetamodel_DdsPublisherListener: "ddsMetamodel_DdsPublisher" = None):
        self.listenedStatus = listenedStatus
        self.name = name
        self.ddsMetamodel_DdsPublisherListener = ddsMetamodel_DdsPublisherListener
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def listenedStatus(self) -> str:
        return self.__listenedStatus

    @listenedStatus.setter
    def listenedStatus(self, listenedStatus: str):
        self.__listenedStatus = listenedStatus

    @property
    def ddsMetamodel_DdsPublisherListener(self):
        return self.__ddsMetamodel_DdsPublisherListener

    @ddsMetamodel_DdsPublisherListener.setter
    def ddsMetamodel_DdsPublisherListener(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsPublisherListener__ddsMetamodel_DdsPublisherListener", None)
        self.__ddsMetamodel_DdsPublisherListener = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsPublisher31"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsPublisher31", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsPublisher31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsPublisher31"):
                opp_val = getattr(value, "ddsMetamodel_DdsPublisher31", None)
                setattr(value, "ddsMetamodel_DdsPublisher31", self)

class ddsMetamodel_DdsDataWriter:

    def __init__(self, dataWriterName: str, ddsMetamodel_DdsDataWriter: "ddsMetamodel_DdsPublisher" = None, ddsMetamodel_DdsDataWriter35: "ddsMetamodel_DdsTopic" = None, ddsMetamodel_DdsDataWriter38: "ddsMetamodel_DdsDataWriterListener" = None, ddsMetamodel_DdsDataWriter40: "ddsMetamodel_DdsDataWriterQosProfile" = None, ddsMetamodel_DdsDataWriter230: "ddsMetamodel_DdsDataWriterStatusCondition" = None):
        self.dataWriterName = dataWriterName
        self.ddsMetamodel_DdsDataWriter = ddsMetamodel_DdsDataWriter
        self.ddsMetamodel_DdsDataWriter35 = ddsMetamodel_DdsDataWriter35
        self.ddsMetamodel_DdsDataWriter38 = ddsMetamodel_DdsDataWriter38
        self.ddsMetamodel_DdsDataWriter40 = ddsMetamodel_DdsDataWriter40
        self.ddsMetamodel_DdsDataWriter230 = ddsMetamodel_DdsDataWriter230
        
    @property
    def dataWriterName(self) -> str:
        return self.__dataWriterName

    @dataWriterName.setter
    def dataWriterName(self, dataWriterName: str):
        self.__dataWriterName = dataWriterName

    @property
    def ddsMetamodel_DdsDataWriter(self):
        return self.__ddsMetamodel_DdsDataWriter

    @ddsMetamodel_DdsDataWriter.setter
    def ddsMetamodel_DdsDataWriter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataWriter__ddsMetamodel_DdsDataWriter", None)
        self.__ddsMetamodel_DdsDataWriter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsPublisher29"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsPublisher29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsPublisher29"):
                opp_val = getattr(value, "ddsMetamodel_DdsPublisher29", None)
                if opp_val is None:
                    setattr(value, "ddsMetamodel_DdsPublisher29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ddsMetamodel_DdsDataWriter38(self):
        return self.__ddsMetamodel_DdsDataWriter38

    @ddsMetamodel_DdsDataWriter38.setter
    def ddsMetamodel_DdsDataWriter38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataWriter__ddsMetamodel_DdsDataWriter38", None)
        self.__ddsMetamodel_DdsDataWriter38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataWriterListener"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataWriterListener", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataWriterListener", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataWriterListener"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataWriterListener", None)
                setattr(value, "ddsMetamodel_DdsDataWriterListener", self)

    @property
    def ddsMetamodel_DdsDataWriter40(self):
        return self.__ddsMetamodel_DdsDataWriter40

    @ddsMetamodel_DdsDataWriter40.setter
    def ddsMetamodel_DdsDataWriter40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataWriter__ddsMetamodel_DdsDataWriter40", None)
        self.__ddsMetamodel_DdsDataWriter40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataWriterQosProfile", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataWriterQosProfile"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataWriterQosProfile", None)
                setattr(value, "ddsMetamodel_DdsDataWriterQosProfile", self)

    @property
    def ddsMetamodel_DdsDataWriter35(self):
        return self.__ddsMetamodel_DdsDataWriter35

    @ddsMetamodel_DdsDataWriter35.setter
    def ddsMetamodel_DdsDataWriter35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataWriter__ddsMetamodel_DdsDataWriter35", None)
        self.__ddsMetamodel_DdsDataWriter35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsTopic36"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsTopic36", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsTopic36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsTopic36"):
                opp_val = getattr(value, "ddsMetamodel_DdsTopic36", None)
                setattr(value, "ddsMetamodel_DdsTopic36", self)

    @property
    def ddsMetamodel_DdsDataWriter230(self):
        return self.__ddsMetamodel_DdsDataWriter230

    @ddsMetamodel_DdsDataWriter230.setter
    def ddsMetamodel_DdsDataWriter230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataWriter__ddsMetamodel_DdsDataWriter230", None)
        self.__ddsMetamodel_DdsDataWriter230 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataWriterStatusCondition"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataWriterStatusCondition", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataWriterStatusCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataWriterStatusCondition"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataWriterStatusCondition", None)
                setattr(value, "ddsMetamodel_DdsDataWriterStatusCondition", self)

class ddsMetamodel_DdsDataReaderQosProfile(DdsQosProfile):

    pass
class ddsMetamodel_DdsDataReaderListener:

    def __init__(self, name: str, listenedStatus: str, ddsMetamodel_DdsDataReaderListener: "ddsMetamodel_DdsDataReader" = None):
        self.name = name
        self.listenedStatus = listenedStatus
        self.ddsMetamodel_DdsDataReaderListener = ddsMetamodel_DdsDataReaderListener
        
    @property
    def listenedStatus(self) -> str:
        return self.__listenedStatus

    @listenedStatus.setter
    def listenedStatus(self, listenedStatus: str):
        self.__listenedStatus = listenedStatus

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ddsMetamodel_DdsDataReaderListener(self):
        return self.__ddsMetamodel_DdsDataReaderListener

    @ddsMetamodel_DdsDataReaderListener.setter
    def ddsMetamodel_DdsDataReaderListener(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataReaderListener__ddsMetamodel_DdsDataReaderListener", None)
        self.__ddsMetamodel_DdsDataReaderListener = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataReader24"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataReader24", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataReader24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataReader24"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataReader24", None)
                setattr(value, "ddsMetamodel_DdsDataReader24", self)

class ddsMetamodel_DdsDomainParticipantListener:

    def __init__(self, name: str, listenedStatus: str, ddsMetamodel_DdsDomainParticipantListener: "ddsMetamodel_DdsDomainParticipant" = None):
        self.name = name
        self.listenedStatus = listenedStatus
        self.ddsMetamodel_DdsDomainParticipantListener = ddsMetamodel_DdsDomainParticipantListener
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def listenedStatus(self) -> str:
        return self.__listenedStatus

    @listenedStatus.setter
    def listenedStatus(self, listenedStatus: str):
        self.__listenedStatus = listenedStatus

    @property
    def ddsMetamodel_DdsDomainParticipantListener(self):
        return self.__ddsMetamodel_DdsDomainParticipantListener

    @ddsMetamodel_DdsDomainParticipantListener.setter
    def ddsMetamodel_DdsDomainParticipantListener(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDomainParticipantListener__ddsMetamodel_DdsDomainParticipantListener", None)
        self.__ddsMetamodel_DdsDomainParticipantListener = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDomainParticipant10"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDomainParticipant10", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDomainParticipant10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDomainParticipant10"):
                opp_val = getattr(value, "ddsMetamodel_DdsDomainParticipant10", None)
                setattr(value, "ddsMetamodel_DdsDomainParticipant10", self)

class ddsMetamodel_DdsDomainParticipantQosProfile(DdsQosProfile):

    pass
class ddsMetamodel_DdsSubscriberQosProfile(DdsQosProfile):

    pass
class ddsMetamodel_DdsSubscriberListener:

    def __init__(self, name: str, listenedStatus: str, ddsMetamodel_DdsSubscriberListener: "ddsMetamodel_DdsSubscriber" = None):
        self.name = name
        self.listenedStatus = listenedStatus
        self.ddsMetamodel_DdsSubscriberListener = ddsMetamodel_DdsSubscriberListener
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def listenedStatus(self) -> str:
        return self.__listenedStatus

    @listenedStatus.setter
    def listenedStatus(self, listenedStatus: str):
        self.__listenedStatus = listenedStatus

    @property
    def ddsMetamodel_DdsSubscriberListener(self):
        return self.__ddsMetamodel_DdsSubscriberListener

    @ddsMetamodel_DdsSubscriberListener.setter
    def ddsMetamodel_DdsSubscriberListener(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsSubscriberListener__ddsMetamodel_DdsSubscriberListener", None)
        self.__ddsMetamodel_DdsSubscriberListener = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsSubscriber18"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsSubscriber18", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsSubscriber18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsSubscriber18"):
                opp_val = getattr(value, "ddsMetamodel_DdsSubscriber18", None)
                setattr(value, "ddsMetamodel_DdsSubscriber18", self)

class ddsMetamodel_DdsDataReader:

    def __init__(self, dataReaderName: str, DdsDataReader: "ddsMetamodel_DdsSubscriber" = None, ddsMetamodel_DdsDataReader24: "ddsMetamodel_DdsDataReaderListener" = None, ddsMetamodel_DdsDataReader26: "ddsMetamodel_DdsDataReaderQosProfile" = None, ddsdatareader: "ddsMetamodel_DdsSubscriber" = None, ddsMetamodel_DdsDataReader: "ddsMetamodel_DdsTopic" = None, ddsMetamodel_DdsDataReader217: "ddsMetamodel_DdsReadCondition" = None, ddsMetamodel_DdsDataReader232: "ddsMetamodel_DdsDataReaderStatusCondition" = None):
        self.dataReaderName = dataReaderName
        self.DdsDataReader = DdsDataReader
        self.ddsMetamodel_DdsDataReader24 = ddsMetamodel_DdsDataReader24
        self.ddsMetamodel_DdsDataReader26 = ddsMetamodel_DdsDataReader26
        self.ddsdatareader = ddsdatareader
        self.ddsMetamodel_DdsDataReader = ddsMetamodel_DdsDataReader
        self.ddsMetamodel_DdsDataReader217 = ddsMetamodel_DdsDataReader217
        self.ddsMetamodel_DdsDataReader232 = ddsMetamodel_DdsDataReader232
        
    @property
    def dataReaderName(self) -> str:
        return self.__dataReaderName

    @dataReaderName.setter
    def dataReaderName(self, dataReaderName: str):
        self.__dataReaderName = dataReaderName

    @property
    def ddsMetamodel_DdsDataReader26(self):
        return self.__ddsMetamodel_DdsDataReader26

    @ddsMetamodel_DdsDataReader26.setter
    def ddsMetamodel_DdsDataReader26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataReader__ddsMetamodel_DdsDataReader26", None)
        self.__ddsMetamodel_DdsDataReader26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataReaderQosProfile"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataReaderQosProfile", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataReaderQosProfile", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataReaderQosProfile"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataReaderQosProfile", None)
                setattr(value, "ddsMetamodel_DdsDataReaderQosProfile", self)

    @property
    def DdsDataReader(self):
        return self.__DdsDataReader

    @DdsDataReader.setter
    def DdsDataReader(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataReader__DdsDataReader", None)
        self.__DdsDataReader = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containingSubscriber"):
                opp_val = getattr(old_value, "containingSubscriber", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containingSubscriber"):
                opp_val = getattr(value, "containingSubscriber", None)
                if opp_val is None:
                    setattr(value, "containingSubscriber", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ddsMetamodel_DdsDataReader(self):
        return self.__ddsMetamodel_DdsDataReader

    @ddsMetamodel_DdsDataReader.setter
    def ddsMetamodel_DdsDataReader(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataReader__ddsMetamodel_DdsDataReader", None)
        self.__ddsMetamodel_DdsDataReader = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsTopic22"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsTopic22", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsTopic22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsTopic22"):
                opp_val = getattr(value, "ddsMetamodel_DdsTopic22", None)
                setattr(value, "ddsMetamodel_DdsTopic22", self)

    @property
    def ddsMetamodel_DdsDataReader217(self):
        return self.__ddsMetamodel_DdsDataReader217

    @ddsMetamodel_DdsDataReader217.setter
    def ddsMetamodel_DdsDataReader217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataReader__ddsMetamodel_DdsDataReader217", None)
        self.__ddsMetamodel_DdsDataReader217 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsReadCondition216"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsReadCondition216", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsReadCondition216", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsReadCondition216"):
                opp_val = getattr(value, "ddsMetamodel_DdsReadCondition216", None)
                setattr(value, "ddsMetamodel_DdsReadCondition216", self)

    @property
    def ddsMetamodel_DdsDataReader24(self):
        return self.__ddsMetamodel_DdsDataReader24

    @ddsMetamodel_DdsDataReader24.setter
    def ddsMetamodel_DdsDataReader24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataReader__ddsMetamodel_DdsDataReader24", None)
        self.__ddsMetamodel_DdsDataReader24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataReaderListener"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataReaderListener", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataReaderListener", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataReaderListener"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataReaderListener", None)
                setattr(value, "ddsMetamodel_DdsDataReaderListener", self)

    @property
    def ddsMetamodel_DdsDataReader232(self):
        return self.__ddsMetamodel_DdsDataReader232

    @ddsMetamodel_DdsDataReader232.setter
    def ddsMetamodel_DdsDataReader232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataReader__ddsMetamodel_DdsDataReader232", None)
        self.__ddsMetamodel_DdsDataReader232 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataReaderStatusCondition"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataReaderStatusCondition", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataReaderStatusCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataReaderStatusCondition"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataReaderStatusCondition", None)
                setattr(value, "ddsMetamodel_DdsDataReaderStatusCondition", self)

    @property
    def ddsdatareader(self):
        return self.__ddsdatareader

    @ddsdatareader.setter
    def ddsdatareader(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataReader__ddsdatareader", None)
        self.__ddsdatareader = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DdsSubscriber"):
                opp_val = getattr(old_value, "DdsSubscriber", None)
                if opp_val == self:
                    setattr(old_value, "DdsSubscriber", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DdsSubscriber"):
                opp_val = getattr(value, "DdsSubscriber", None)
                setattr(value, "DdsSubscriber", self)

class ddsMetamodel_DdsQosProfile:

    def __init__(self, profileName: str, ddsMetamodel_DdsQosProfile: "ddsMetamodel_DdsSystem" = None):
        self.profileName = profileName
        self.ddsMetamodel_DdsQosProfile = ddsMetamodel_DdsQosProfile
        
    @property
    def profileName(self) -> str:
        return self.__profileName

    @profileName.setter
    def profileName(self, profileName: str):
        self.__profileName = profileName

    @property
    def ddsMetamodel_DdsQosProfile(self):
        return self.__ddsMetamodel_DdsQosProfile

    @ddsMetamodel_DdsQosProfile.setter
    def ddsMetamodel_DdsQosProfile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsQosProfile__ddsMetamodel_DdsQosProfile", None)
        self.__ddsMetamodel_DdsQosProfile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsSystem237"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsSystem237", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsSystem237"):
                opp_val = getattr(value, "ddsMetamodel_DdsSystem237", None)
                if opp_val is None:
                    setattr(value, "ddsMetamodel_DdsSystem237", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ddsMetamodel_DdsDataStructure:

    def __init__(self, structureName: str, ddsMetamodel_DdsDataStructure: "ddsMetamodel_DdsTopic" = None, DdsDataStructure: "ddsMetamodel_DdsDataModule" = None, ddsMetamodel_DdsDataStructure49: set["ddsMetamodel_DdsDataField"] = None, dataStructure: set["ddsMetamodel_DdsStructuredField"] = None, dataStructures: "ddsMetamodel_DdsDataModule" = None, ddsMetamodel_DdsDataStructure219: "ddsMetamodel_DdsStructuredField" = None, DdsDataStructure221: "ddsMetamodel_DdsStructuredField" = None):
        self.structureName = structureName
        self.ddsMetamodel_DdsDataStructure = ddsMetamodel_DdsDataStructure
        self.DdsDataStructure = DdsDataStructure
        self.ddsMetamodel_DdsDataStructure49 = ddsMetamodel_DdsDataStructure49 if ddsMetamodel_DdsDataStructure49 is not None else set()
        self.dataStructure = dataStructure if dataStructure is not None else set()
        self.dataStructures = dataStructures
        self.ddsMetamodel_DdsDataStructure219 = ddsMetamodel_DdsDataStructure219
        self.DdsDataStructure221 = DdsDataStructure221
        
    @property
    def structureName(self) -> str:
        return self.__structureName

    @structureName.setter
    def structureName(self, structureName: str):
        self.__structureName = structureName

    @property
    def ddsMetamodel_DdsDataStructure219(self):
        return self.__ddsMetamodel_DdsDataStructure219

    @ddsMetamodel_DdsDataStructure219.setter
    def ddsMetamodel_DdsDataStructure219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataStructure__ddsMetamodel_DdsDataStructure219", None)
        self.__ddsMetamodel_DdsDataStructure219 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsStructuredField"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsStructuredField", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsStructuredField", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsStructuredField"):
                opp_val = getattr(value, "ddsMetamodel_DdsStructuredField", None)
                setattr(value, "ddsMetamodel_DdsStructuredField", self)

    @property
    def DdsDataStructure221(self):
        return self.__DdsDataStructure221

    @DdsDataStructure221.setter
    def DdsDataStructure221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataStructure__DdsDataStructure221", None)
        self.__DdsDataStructure221 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structuredFields"):
                opp_val = getattr(old_value, "structuredFields", None)
                if opp_val == self:
                    setattr(old_value, "structuredFields", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structuredFields"):
                opp_val = getattr(value, "structuredFields", None)
                setattr(value, "structuredFields", self)

    @property
    def DdsDataStructure(self):
        return self.__DdsDataStructure

    @DdsDataStructure.setter
    def DdsDataStructure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataStructure__DdsDataStructure", None)
        self.__DdsDataStructure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containerDataModule"):
                opp_val = getattr(old_value, "containerDataModule", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containerDataModule"):
                opp_val = getattr(value, "containerDataModule", None)
                if opp_val is None:
                    setattr(value, "containerDataModule", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ddsMetamodel_DdsDataStructure(self):
        return self.__ddsMetamodel_DdsDataStructure

    @ddsMetamodel_DdsDataStructure.setter
    def ddsMetamodel_DdsDataStructure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataStructure__ddsMetamodel_DdsDataStructure", None)
        self.__ddsMetamodel_DdsDataStructure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsTopic15"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsTopic15", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsTopic15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsTopic15"):
                opp_val = getattr(value, "ddsMetamodel_DdsTopic15", None)
                setattr(value, "ddsMetamodel_DdsTopic15", self)

    @property
    def dataStructures(self):
        return self.__dataStructures

    @dataStructures.setter
    def dataStructures(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataStructure__dataStructures", None)
        self.__dataStructures = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DdsDataModule52"):
                opp_val = getattr(old_value, "DdsDataModule52", None)
                if opp_val == self:
                    setattr(old_value, "DdsDataModule52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DdsDataModule52"):
                opp_val = getattr(value, "DdsDataModule52", None)
                setattr(value, "DdsDataModule52", self)

    @property
    def dataStructure(self):
        return self.__dataStructure

    @dataStructure.setter
    def dataStructure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataStructure__dataStructure", None)
        self.__dataStructure = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DdsStructuredField"):
                    opp_val = getattr(item, "DdsStructuredField", None)
                    
                    if opp_val == self:
                        setattr(item, "DdsStructuredField", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DdsStructuredField"):
                    opp_val = getattr(item, "DdsStructuredField", None)
                    
                    setattr(item, "DdsStructuredField", self)
                    

    @property
    def ddsMetamodel_DdsDataStructure49(self):
        return self.__ddsMetamodel_DdsDataStructure49

    @ddsMetamodel_DdsDataStructure49.setter
    def ddsMetamodel_DdsDataStructure49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDataStructure__ddsMetamodel_DdsDataStructure49", None)
        self.__ddsMetamodel_DdsDataStructure49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ddsMetamodel_DdsDataField"):
                    opp_val = getattr(item, "ddsMetamodel_DdsDataField", None)
                    
                    if opp_val == self:
                        setattr(item, "ddsMetamodel_DdsDataField", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ddsMetamodel_DdsDataField"):
                    opp_val = getattr(item, "ddsMetamodel_DdsDataField", None)
                    
                    setattr(item, "ddsMetamodel_DdsDataField", self)
                    

class ddsMetamodel_DdsTopicQosProfile(DdsQosProfile):

    pass
class ddsMetamodel_DdsTopicListener:

    def __init__(self, name: str, listenedStatus: str, ddsMetamodel_DdsTopicListener: "ddsMetamodel_DdsTopic" = None):
        self.name = name
        self.listenedStatus = listenedStatus
        self.ddsMetamodel_DdsTopicListener = ddsMetamodel_DdsTopicListener
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def listenedStatus(self) -> str:
        return self.__listenedStatus

    @listenedStatus.setter
    def listenedStatus(self, listenedStatus: str):
        self.__listenedStatus = listenedStatus

    @property
    def ddsMetamodel_DdsTopicListener(self):
        return self.__ddsMetamodel_DdsTopicListener

    @ddsMetamodel_DdsTopicListener.setter
    def ddsMetamodel_DdsTopicListener(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsTopicListener__ddsMetamodel_DdsTopicListener", None)
        self.__ddsMetamodel_DdsTopicListener = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsTopic"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsTopic", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsTopic", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsTopic"):
                opp_val = getattr(value, "ddsMetamodel_DdsTopic", None)
                setattr(value, "ddsMetamodel_DdsTopic", self)

class ddsMetamodel_DdsTopic:

    def __init__(self, topicName: str, ddsMetamodel_DdsTopic: "ddsMetamodel_DdsTopicListener" = None, ddsMetamodel_DdsTopic13: "ddsMetamodel_DdsTopicQosProfile" = None, ddsMetamodel_DdsTopic15: "ddsMetamodel_DdsDataStructure" = None, ddsMetamodel_DdsTopic36: "ddsMetamodel_DdsDataWriter" = None, ddsMetamodel_DdsTopic22: "ddsMetamodel_DdsDataReader" = None, ddsMetamodel_DdsTopic234: "ddsMetamodel_DdsTopicStatusCondition" = None, ddsMetamodel_DdsTopic242: "ddsMetamodel_DdsSystem" = None):
        self.topicName = topicName
        self.ddsMetamodel_DdsTopic = ddsMetamodel_DdsTopic
        self.ddsMetamodel_DdsTopic13 = ddsMetamodel_DdsTopic13
        self.ddsMetamodel_DdsTopic15 = ddsMetamodel_DdsTopic15
        self.ddsMetamodel_DdsTopic36 = ddsMetamodel_DdsTopic36
        self.ddsMetamodel_DdsTopic22 = ddsMetamodel_DdsTopic22
        self.ddsMetamodel_DdsTopic234 = ddsMetamodel_DdsTopic234
        self.ddsMetamodel_DdsTopic242 = ddsMetamodel_DdsTopic242
        
    @property
    def topicName(self) -> str:
        return self.__topicName

    @topicName.setter
    def topicName(self, topicName: str):
        self.__topicName = topicName

    @property
    def ddsMetamodel_DdsTopic36(self):
        return self.__ddsMetamodel_DdsTopic36

    @ddsMetamodel_DdsTopic36.setter
    def ddsMetamodel_DdsTopic36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsTopic__ddsMetamodel_DdsTopic36", None)
        self.__ddsMetamodel_DdsTopic36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataWriter35"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataWriter35", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataWriter35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataWriter35"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataWriter35", None)
                setattr(value, "ddsMetamodel_DdsDataWriter35", self)

    @property
    def ddsMetamodel_DdsTopic22(self):
        return self.__ddsMetamodel_DdsTopic22

    @ddsMetamodel_DdsTopic22.setter
    def ddsMetamodel_DdsTopic22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsTopic__ddsMetamodel_DdsTopic22", None)
        self.__ddsMetamodel_DdsTopic22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataReader"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataReader", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataReader", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataReader"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataReader", None)
                setattr(value, "ddsMetamodel_DdsDataReader", self)

    @property
    def ddsMetamodel_DdsTopic234(self):
        return self.__ddsMetamodel_DdsTopic234

    @ddsMetamodel_DdsTopic234.setter
    def ddsMetamodel_DdsTopic234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsTopic__ddsMetamodel_DdsTopic234", None)
        self.__ddsMetamodel_DdsTopic234 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsTopicStatusCondition"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsTopicStatusCondition", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsTopicStatusCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsTopicStatusCondition"):
                opp_val = getattr(value, "ddsMetamodel_DdsTopicStatusCondition", None)
                setattr(value, "ddsMetamodel_DdsTopicStatusCondition", self)

    @property
    def ddsMetamodel_DdsTopic13(self):
        return self.__ddsMetamodel_DdsTopic13

    @ddsMetamodel_DdsTopic13.setter
    def ddsMetamodel_DdsTopic13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsTopic__ddsMetamodel_DdsTopic13", None)
        self.__ddsMetamodel_DdsTopic13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsTopicQosProfile"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsTopicQosProfile", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsTopicQosProfile", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsTopicQosProfile"):
                opp_val = getattr(value, "ddsMetamodel_DdsTopicQosProfile", None)
                setattr(value, "ddsMetamodel_DdsTopicQosProfile", self)

    @property
    def ddsMetamodel_DdsTopic242(self):
        return self.__ddsMetamodel_DdsTopic242

    @ddsMetamodel_DdsTopic242.setter
    def ddsMetamodel_DdsTopic242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsTopic__ddsMetamodel_DdsTopic242", None)
        self.__ddsMetamodel_DdsTopic242 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsSystem241"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsSystem241", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsSystem241"):
                opp_val = getattr(value, "ddsMetamodel_DdsSystem241", None)
                if opp_val is None:
                    setattr(value, "ddsMetamodel_DdsSystem241", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ddsMetamodel_DdsTopic15(self):
        return self.__ddsMetamodel_DdsTopic15

    @ddsMetamodel_DdsTopic15.setter
    def ddsMetamodel_DdsTopic15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsTopic__ddsMetamodel_DdsTopic15", None)
        self.__ddsMetamodel_DdsTopic15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDataStructure"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDataStructure", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDataStructure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDataStructure"):
                opp_val = getattr(value, "ddsMetamodel_DdsDataStructure", None)
                setattr(value, "ddsMetamodel_DdsDataStructure", self)

    @property
    def ddsMetamodel_DdsTopic(self):
        return self.__ddsMetamodel_DdsTopic

    @ddsMetamodel_DdsTopic.setter
    def ddsMetamodel_DdsTopic(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsTopic__ddsMetamodel_DdsTopic", None)
        self.__ddsMetamodel_DdsTopic = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsTopicListener"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsTopicListener", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsTopicListener", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsTopicListener"):
                opp_val = getattr(value, "ddsMetamodel_DdsTopicListener", None)
                setattr(value, "ddsMetamodel_DdsTopicListener", self)

class ddsMetamodel_DdsPublisher:

    def __init__(self, publisherName: str, ddsMetamodel_DdsPublisher: "ddsMetamodel_DdsDomainParticipant" = None, ddsMetamodel_DdsPublisher29: set["ddsMetamodel_DdsDataWriter"] = None, ddsMetamodel_DdsPublisher31: "ddsMetamodel_DdsPublisherListener" = None, ddsMetamodel_DdsPublisher33: "ddsMetamodel_DdsPublisherQosProfile" = None, ddsMetamodel_DdsPublisher226: "ddsMetamodel_DdsPublisherStatusCondition" = None):
        self.publisherName = publisherName
        self.ddsMetamodel_DdsPublisher = ddsMetamodel_DdsPublisher
        self.ddsMetamodel_DdsPublisher29 = ddsMetamodel_DdsPublisher29 if ddsMetamodel_DdsPublisher29 is not None else set()
        self.ddsMetamodel_DdsPublisher31 = ddsMetamodel_DdsPublisher31
        self.ddsMetamodel_DdsPublisher33 = ddsMetamodel_DdsPublisher33
        self.ddsMetamodel_DdsPublisher226 = ddsMetamodel_DdsPublisher226
        
    @property
    def publisherName(self) -> str:
        return self.__publisherName

    @publisherName.setter
    def publisherName(self, publisherName: str):
        self.__publisherName = publisherName

    @property
    def ddsMetamodel_DdsPublisher(self):
        return self.__ddsMetamodel_DdsPublisher

    @ddsMetamodel_DdsPublisher.setter
    def ddsMetamodel_DdsPublisher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsPublisher__ddsMetamodel_DdsPublisher", None)
        self.__ddsMetamodel_DdsPublisher = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDomainParticipant6"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDomainParticipant6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDomainParticipant6"):
                opp_val = getattr(value, "ddsMetamodel_DdsDomainParticipant6", None)
                if opp_val is None:
                    setattr(value, "ddsMetamodel_DdsDomainParticipant6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ddsMetamodel_DdsPublisher31(self):
        return self.__ddsMetamodel_DdsPublisher31

    @ddsMetamodel_DdsPublisher31.setter
    def ddsMetamodel_DdsPublisher31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsPublisher__ddsMetamodel_DdsPublisher31", None)
        self.__ddsMetamodel_DdsPublisher31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsPublisherListener"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsPublisherListener", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsPublisherListener", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsPublisherListener"):
                opp_val = getattr(value, "ddsMetamodel_DdsPublisherListener", None)
                setattr(value, "ddsMetamodel_DdsPublisherListener", self)

    @property
    def ddsMetamodel_DdsPublisher29(self):
        return self.__ddsMetamodel_DdsPublisher29

    @ddsMetamodel_DdsPublisher29.setter
    def ddsMetamodel_DdsPublisher29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsPublisher__ddsMetamodel_DdsPublisher29", None)
        self.__ddsMetamodel_DdsPublisher29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ddsMetamodel_DdsDataWriter"):
                    opp_val = getattr(item, "ddsMetamodel_DdsDataWriter", None)
                    
                    if opp_val == self:
                        setattr(item, "ddsMetamodel_DdsDataWriter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ddsMetamodel_DdsDataWriter"):
                    opp_val = getattr(item, "ddsMetamodel_DdsDataWriter", None)
                    
                    setattr(item, "ddsMetamodel_DdsDataWriter", self)
                    

    @property
    def ddsMetamodel_DdsPublisher33(self):
        return self.__ddsMetamodel_DdsPublisher33

    @ddsMetamodel_DdsPublisher33.setter
    def ddsMetamodel_DdsPublisher33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsPublisher__ddsMetamodel_DdsPublisher33", None)
        self.__ddsMetamodel_DdsPublisher33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsPublisherQosProfile"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsPublisherQosProfile", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsPublisherQosProfile", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsPublisherQosProfile"):
                opp_val = getattr(value, "ddsMetamodel_DdsPublisherQosProfile", None)
                setattr(value, "ddsMetamodel_DdsPublisherQosProfile", self)

    @property
    def ddsMetamodel_DdsPublisher226(self):
        return self.__ddsMetamodel_DdsPublisher226

    @ddsMetamodel_DdsPublisher226.setter
    def ddsMetamodel_DdsPublisher226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsPublisher__ddsMetamodel_DdsPublisher226", None)
        self.__ddsMetamodel_DdsPublisher226 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsPublisherStatusCondition"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsPublisherStatusCondition", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsPublisherStatusCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsPublisherStatusCondition"):
                opp_val = getattr(value, "ddsMetamodel_DdsPublisherStatusCondition", None)
                setattr(value, "ddsMetamodel_DdsPublisherStatusCondition", self)

class ddsMetamodel_DdsSubscriber:

    def __init__(self, subscriberName: str, ddsMetamodel_DdsSubscriber: "ddsMetamodel_DdsDomainParticipant" = None, containingSubscriber: set["ddsMetamodel_DdsDataReader"] = None, ddsMetamodel_DdsSubscriber18: "ddsMetamodel_DdsSubscriberListener" = None, ddsMetamodel_DdsSubscriber20: "ddsMetamodel_DdsSubscriberQosProfile" = None, DdsSubscriber: "ddsMetamodel_DdsDataReader" = None, ddsMetamodel_DdsSubscriber228: "ddsMetamodel_DdsSubscriberStatusCondition" = None):
        self.subscriberName = subscriberName
        self.ddsMetamodel_DdsSubscriber = ddsMetamodel_DdsSubscriber
        self.containingSubscriber = containingSubscriber if containingSubscriber is not None else set()
        self.ddsMetamodel_DdsSubscriber18 = ddsMetamodel_DdsSubscriber18
        self.ddsMetamodel_DdsSubscriber20 = ddsMetamodel_DdsSubscriber20
        self.DdsSubscriber = DdsSubscriber
        self.ddsMetamodel_DdsSubscriber228 = ddsMetamodel_DdsSubscriber228
        
    @property
    def subscriberName(self) -> str:
        return self.__subscriberName

    @subscriberName.setter
    def subscriberName(self, subscriberName: str):
        self.__subscriberName = subscriberName

    @property
    def ddsMetamodel_DdsSubscriber20(self):
        return self.__ddsMetamodel_DdsSubscriber20

    @ddsMetamodel_DdsSubscriber20.setter
    def ddsMetamodel_DdsSubscriber20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsSubscriber__ddsMetamodel_DdsSubscriber20", None)
        self.__ddsMetamodel_DdsSubscriber20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsSubscriberQosProfile"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsSubscriberQosProfile", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsSubscriberQosProfile", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsSubscriberQosProfile"):
                opp_val = getattr(value, "ddsMetamodel_DdsSubscriberQosProfile", None)
                setattr(value, "ddsMetamodel_DdsSubscriberQosProfile", self)

    @property
    def ddsMetamodel_DdsSubscriber228(self):
        return self.__ddsMetamodel_DdsSubscriber228

    @ddsMetamodel_DdsSubscriber228.setter
    def ddsMetamodel_DdsSubscriber228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsSubscriber__ddsMetamodel_DdsSubscriber228", None)
        self.__ddsMetamodel_DdsSubscriber228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsSubscriberStatusCondition"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsSubscriberStatusCondition", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsSubscriberStatusCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsSubscriberStatusCondition"):
                opp_val = getattr(value, "ddsMetamodel_DdsSubscriberStatusCondition", None)
                setattr(value, "ddsMetamodel_DdsSubscriberStatusCondition", self)

    @property
    def ddsMetamodel_DdsSubscriber(self):
        return self.__ddsMetamodel_DdsSubscriber

    @ddsMetamodel_DdsSubscriber.setter
    def ddsMetamodel_DdsSubscriber(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsSubscriber__ddsMetamodel_DdsSubscriber", None)
        self.__ddsMetamodel_DdsSubscriber = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDomainParticipant4"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDomainParticipant4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDomainParticipant4"):
                opp_val = getattr(value, "ddsMetamodel_DdsDomainParticipant4", None)
                if opp_val is None:
                    setattr(value, "ddsMetamodel_DdsDomainParticipant4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def containingSubscriber(self):
        return self.__containingSubscriber

    @containingSubscriber.setter
    def containingSubscriber(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsSubscriber__containingSubscriber", None)
        self.__containingSubscriber = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DdsDataReader"):
                    opp_val = getattr(item, "DdsDataReader", None)
                    
                    if opp_val == self:
                        setattr(item, "DdsDataReader", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DdsDataReader"):
                    opp_val = getattr(item, "DdsDataReader", None)
                    
                    setattr(item, "DdsDataReader", self)
                    

    @property
    def DdsSubscriber(self):
        return self.__DdsSubscriber

    @DdsSubscriber.setter
    def DdsSubscriber(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsSubscriber__DdsSubscriber", None)
        self.__DdsSubscriber = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsdatareader"):
                opp_val = getattr(old_value, "ddsdatareader", None)
                if opp_val == self:
                    setattr(old_value, "ddsdatareader", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsdatareader"):
                opp_val = getattr(value, "ddsdatareader", None)
                setattr(value, "ddsdatareader", self)

    @property
    def ddsMetamodel_DdsSubscriber18(self):
        return self.__ddsMetamodel_DdsSubscriber18

    @ddsMetamodel_DdsSubscriber18.setter
    def ddsMetamodel_DdsSubscriber18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsSubscriber__ddsMetamodel_DdsSubscriber18", None)
        self.__ddsMetamodel_DdsSubscriber18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsSubscriberListener"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsSubscriberListener", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsSubscriberListener", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsSubscriberListener"):
                opp_val = getattr(value, "ddsMetamodel_DdsSubscriberListener", None)
                setattr(value, "ddsMetamodel_DdsSubscriberListener", self)

class ddsMetamodel_DdsWaitSet:

    def __init__(self, name: str, ddsMetamodel_DdsWaitSet: "ddsMetamodel_DdsApplication" = None, ddsMetamodel_DdsWaitSet211: set["ddsMetamodel_DdsReadCondition"] = None, containingWaitset: set["ddsMetamodel_DdsStatusCondition"] = None, ddsMetamodel_DdsWaitSet214: set["ddsMetamodel_GuardCondition"] = None, DdsWaitSet: "ddsMetamodel_DdsStatusCondition" = None):
        self.name = name
        self.ddsMetamodel_DdsWaitSet = ddsMetamodel_DdsWaitSet
        self.ddsMetamodel_DdsWaitSet211 = ddsMetamodel_DdsWaitSet211 if ddsMetamodel_DdsWaitSet211 is not None else set()
        self.containingWaitset = containingWaitset if containingWaitset is not None else set()
        self.ddsMetamodel_DdsWaitSet214 = ddsMetamodel_DdsWaitSet214 if ddsMetamodel_DdsWaitSet214 is not None else set()
        self.DdsWaitSet = DdsWaitSet
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ddsMetamodel_DdsWaitSet(self):
        return self.__ddsMetamodel_DdsWaitSet

    @ddsMetamodel_DdsWaitSet.setter
    def ddsMetamodel_DdsWaitSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsWaitSet__ddsMetamodel_DdsWaitSet", None)
        self.__ddsMetamodel_DdsWaitSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsApplication2"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsApplication2", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsApplication2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsApplication2"):
                opp_val = getattr(value, "ddsMetamodel_DdsApplication2", None)
                setattr(value, "ddsMetamodel_DdsApplication2", self)

    @property
    def ddsMetamodel_DdsWaitSet211(self):
        return self.__ddsMetamodel_DdsWaitSet211

    @ddsMetamodel_DdsWaitSet211.setter
    def ddsMetamodel_DdsWaitSet211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsWaitSet__ddsMetamodel_DdsWaitSet211", None)
        self.__ddsMetamodel_DdsWaitSet211 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ddsMetamodel_DdsReadCondition"):
                    opp_val = getattr(item, "ddsMetamodel_DdsReadCondition", None)
                    
                    if opp_val == self:
                        setattr(item, "ddsMetamodel_DdsReadCondition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ddsMetamodel_DdsReadCondition"):
                    opp_val = getattr(item, "ddsMetamodel_DdsReadCondition", None)
                    
                    setattr(item, "ddsMetamodel_DdsReadCondition", self)
                    

    @property
    def DdsWaitSet(self):
        return self.__DdsWaitSet

    @DdsWaitSet.setter
    def DdsWaitSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsWaitSet__DdsWaitSet", None)
        self.__DdsWaitSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statusConditions"):
                opp_val = getattr(old_value, "statusConditions", None)
                if opp_val == self:
                    setattr(old_value, "statusConditions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statusConditions"):
                opp_val = getattr(value, "statusConditions", None)
                setattr(value, "statusConditions", self)

    @property
    def ddsMetamodel_DdsWaitSet214(self):
        return self.__ddsMetamodel_DdsWaitSet214

    @ddsMetamodel_DdsWaitSet214.setter
    def ddsMetamodel_DdsWaitSet214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsWaitSet__ddsMetamodel_DdsWaitSet214", None)
        self.__ddsMetamodel_DdsWaitSet214 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ddsMetamodel_GuardCondition"):
                    opp_val = getattr(item, "ddsMetamodel_GuardCondition", None)
                    
                    if opp_val == self:
                        setattr(item, "ddsMetamodel_GuardCondition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ddsMetamodel_GuardCondition"):
                    opp_val = getattr(item, "ddsMetamodel_GuardCondition", None)
                    
                    setattr(item, "ddsMetamodel_GuardCondition", self)
                    

    @property
    def containingWaitset(self):
        return self.__containingWaitset

    @containingWaitset.setter
    def containingWaitset(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsWaitSet__containingWaitset", None)
        self.__containingWaitset = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DdsStatusCondition"):
                    opp_val = getattr(item, "DdsStatusCondition", None)
                    
                    if opp_val == self:
                        setattr(item, "DdsStatusCondition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DdsStatusCondition"):
                    opp_val = getattr(item, "DdsStatusCondition", None)
                    
                    setattr(item, "DdsStatusCondition", self)
                    

class ddsMetamodel_DdsDomainParticipant:

    def __init__(self, domainParticipantName: str, domainId: int, ddsMetamodel_DdsDomainParticipant: "ddsMetamodel_DdsApplication" = None, ddsMetamodel_DdsDomainParticipant4: set["ddsMetamodel_DdsSubscriber"] = None, ddsMetamodel_DdsDomainParticipant6: set["ddsMetamodel_DdsPublisher"] = None, ddsMetamodel_DdsDomainParticipant8: "ddsMetamodel_DdsDomainParticipantQosProfile" = None, ddsMetamodel_DdsDomainParticipant10: "ddsMetamodel_DdsDomainParticipantListener" = None, ddsMetamodel_DdsDomainParticipant224: "ddsMetamodel_DdsDomainParticipantStatusCondition" = None):
        self.domainParticipantName = domainParticipantName
        self.domainId = domainId
        self.ddsMetamodel_DdsDomainParticipant = ddsMetamodel_DdsDomainParticipant
        self.ddsMetamodel_DdsDomainParticipant4 = ddsMetamodel_DdsDomainParticipant4 if ddsMetamodel_DdsDomainParticipant4 is not None else set()
        self.ddsMetamodel_DdsDomainParticipant6 = ddsMetamodel_DdsDomainParticipant6 if ddsMetamodel_DdsDomainParticipant6 is not None else set()
        self.ddsMetamodel_DdsDomainParticipant8 = ddsMetamodel_DdsDomainParticipant8
        self.ddsMetamodel_DdsDomainParticipant10 = ddsMetamodel_DdsDomainParticipant10
        self.ddsMetamodel_DdsDomainParticipant224 = ddsMetamodel_DdsDomainParticipant224
        
    @property
    def domainParticipantName(self) -> str:
        return self.__domainParticipantName

    @domainParticipantName.setter
    def domainParticipantName(self, domainParticipantName: str):
        self.__domainParticipantName = domainParticipantName

    @property
    def domainId(self) -> int:
        return self.__domainId

    @domainId.setter
    def domainId(self, domainId: int):
        self.__domainId = domainId

    @property
    def ddsMetamodel_DdsDomainParticipant8(self):
        return self.__ddsMetamodel_DdsDomainParticipant8

    @ddsMetamodel_DdsDomainParticipant8.setter
    def ddsMetamodel_DdsDomainParticipant8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDomainParticipant__ddsMetamodel_DdsDomainParticipant8", None)
        self.__ddsMetamodel_DdsDomainParticipant8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDomainParticipantQosProfile"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDomainParticipantQosProfile", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDomainParticipantQosProfile", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDomainParticipantQosProfile"):
                opp_val = getattr(value, "ddsMetamodel_DdsDomainParticipantQosProfile", None)
                setattr(value, "ddsMetamodel_DdsDomainParticipantQosProfile", self)

    @property
    def ddsMetamodel_DdsDomainParticipant6(self):
        return self.__ddsMetamodel_DdsDomainParticipant6

    @ddsMetamodel_DdsDomainParticipant6.setter
    def ddsMetamodel_DdsDomainParticipant6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDomainParticipant__ddsMetamodel_DdsDomainParticipant6", None)
        self.__ddsMetamodel_DdsDomainParticipant6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ddsMetamodel_DdsPublisher"):
                    opp_val = getattr(item, "ddsMetamodel_DdsPublisher", None)
                    
                    if opp_val == self:
                        setattr(item, "ddsMetamodel_DdsPublisher", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ddsMetamodel_DdsPublisher"):
                    opp_val = getattr(item, "ddsMetamodel_DdsPublisher", None)
                    
                    setattr(item, "ddsMetamodel_DdsPublisher", self)
                    

    @property
    def ddsMetamodel_DdsDomainParticipant10(self):
        return self.__ddsMetamodel_DdsDomainParticipant10

    @ddsMetamodel_DdsDomainParticipant10.setter
    def ddsMetamodel_DdsDomainParticipant10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDomainParticipant__ddsMetamodel_DdsDomainParticipant10", None)
        self.__ddsMetamodel_DdsDomainParticipant10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDomainParticipantListener"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDomainParticipantListener", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDomainParticipantListener", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDomainParticipantListener"):
                opp_val = getattr(value, "ddsMetamodel_DdsDomainParticipantListener", None)
                setattr(value, "ddsMetamodel_DdsDomainParticipantListener", self)

    @property
    def ddsMetamodel_DdsDomainParticipant4(self):
        return self.__ddsMetamodel_DdsDomainParticipant4

    @ddsMetamodel_DdsDomainParticipant4.setter
    def ddsMetamodel_DdsDomainParticipant4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDomainParticipant__ddsMetamodel_DdsDomainParticipant4", None)
        self.__ddsMetamodel_DdsDomainParticipant4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ddsMetamodel_DdsSubscriber"):
                    opp_val = getattr(item, "ddsMetamodel_DdsSubscriber", None)
                    
                    if opp_val == self:
                        setattr(item, "ddsMetamodel_DdsSubscriber", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ddsMetamodel_DdsSubscriber"):
                    opp_val = getattr(item, "ddsMetamodel_DdsSubscriber", None)
                    
                    setattr(item, "ddsMetamodel_DdsSubscriber", self)
                    

    @property
    def ddsMetamodel_DdsDomainParticipant224(self):
        return self.__ddsMetamodel_DdsDomainParticipant224

    @ddsMetamodel_DdsDomainParticipant224.setter
    def ddsMetamodel_DdsDomainParticipant224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDomainParticipant__ddsMetamodel_DdsDomainParticipant224", None)
        self.__ddsMetamodel_DdsDomainParticipant224 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsDomainParticipantStatusCondition"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsDomainParticipantStatusCondition", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsDomainParticipantStatusCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsDomainParticipantStatusCondition"):
                opp_val = getattr(value, "ddsMetamodel_DdsDomainParticipantStatusCondition", None)
                setattr(value, "ddsMetamodel_DdsDomainParticipantStatusCondition", self)

    @property
    def ddsMetamodel_DdsDomainParticipant(self):
        return self.__ddsMetamodel_DdsDomainParticipant

    @ddsMetamodel_DdsDomainParticipant.setter
    def ddsMetamodel_DdsDomainParticipant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsDomainParticipant__ddsMetamodel_DdsDomainParticipant", None)
        self.__ddsMetamodel_DdsDomainParticipant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsApplication"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsApplication", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsApplication"):
                opp_val = getattr(value, "ddsMetamodel_DdsApplication", None)
                if opp_val is None:
                    setattr(value, "ddsMetamodel_DdsApplication", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ddsMetamodel_DdsApplication:

    def __init__(self, applicationName: str, ddsMetamodel_DdsApplication: set["ddsMetamodel_DdsDomainParticipant"] = None, ddsMetamodel_DdsApplication2: "ddsMetamodel_DdsWaitSet" = None, ddsMetamodel_DdsApplication245: "ddsMetamodel_DdsHost" = None):
        self.applicationName = applicationName
        self.ddsMetamodel_DdsApplication = ddsMetamodel_DdsApplication if ddsMetamodel_DdsApplication is not None else set()
        self.ddsMetamodel_DdsApplication2 = ddsMetamodel_DdsApplication2
        self.ddsMetamodel_DdsApplication245 = ddsMetamodel_DdsApplication245
        
    @property
    def applicationName(self) -> str:
        return self.__applicationName

    @applicationName.setter
    def applicationName(self, applicationName: str):
        self.__applicationName = applicationName

    @property
    def ddsMetamodel_DdsApplication245(self):
        return self.__ddsMetamodel_DdsApplication245

    @ddsMetamodel_DdsApplication245.setter
    def ddsMetamodel_DdsApplication245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsApplication__ddsMetamodel_DdsApplication245", None)
        self.__ddsMetamodel_DdsApplication245 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsHost244"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsHost244", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsHost244"):
                opp_val = getattr(value, "ddsMetamodel_DdsHost244", None)
                if opp_val is None:
                    setattr(value, "ddsMetamodel_DdsHost244", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ddsMetamodel_DdsApplication(self):
        return self.__ddsMetamodel_DdsApplication

    @ddsMetamodel_DdsApplication.setter
    def ddsMetamodel_DdsApplication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsApplication__ddsMetamodel_DdsApplication", None)
        self.__ddsMetamodel_DdsApplication = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ddsMetamodel_DdsDomainParticipant"):
                    opp_val = getattr(item, "ddsMetamodel_DdsDomainParticipant", None)
                    
                    if opp_val == self:
                        setattr(item, "ddsMetamodel_DdsDomainParticipant", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ddsMetamodel_DdsDomainParticipant"):
                    opp_val = getattr(item, "ddsMetamodel_DdsDomainParticipant", None)
                    
                    setattr(item, "ddsMetamodel_DdsDomainParticipant", self)
                    

    @property
    def ddsMetamodel_DdsApplication2(self):
        return self.__ddsMetamodel_DdsApplication2

    @ddsMetamodel_DdsApplication2.setter
    def ddsMetamodel_DdsApplication2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddsMetamodel_DdsApplication__ddsMetamodel_DdsApplication2", None)
        self.__ddsMetamodel_DdsApplication2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddsMetamodel_DdsWaitSet"):
                opp_val = getattr(old_value, "ddsMetamodel_DdsWaitSet", None)
                if opp_val == self:
                    setattr(old_value, "ddsMetamodel_DdsWaitSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddsMetamodel_DdsWaitSet"):
                opp_val = getattr(value, "ddsMetamodel_DdsWaitSet", None)
                setattr(value, "ddsMetamodel_DdsWaitSet", self)
