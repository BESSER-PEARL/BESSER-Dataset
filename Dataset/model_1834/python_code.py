from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class dcps_Topic:

    pass
class dcps_LifespanQosPolicy:

    pass
class dcps_WriterDataLifecycleQosPolicy:

    pass
class dcps_TransportPriorityQosPolicy:

    pass
class dcps_OwnershipStrengthQosPolicy:

    pass
class dcps_DurabilityServiceQosPolicy:

    pass
class dcps_TopicDescription:

    pass
class dcps_TimeBasedFilterQosPolicy:

    pass
class dcps_ReaderDataLifecycleQosPolicy:

    pass
class DataReaderWriter:

    pass
class dcps_ResourceLimitsQosPolicy:

    pass
class dcps_ReliabilityQosPolicy:

    pass
class dcps_OwnershipQosPolicy:

    pass
class dcps_LivelinessQosPolicy:

    pass
class dcps_LatencyBudgetQosPolicy:

    pass
class dcps_HistoryQosPolicy:

    pass
class dcps_DurabilityQosPolicy:

    pass
class dcps_DestinationOrderQosPolicy:

    pass
class dcps_DeadlineQosPolicy:

    pass
class dcps_DataWriter(DataReaderWriter):

    pass
class dcps_DataReader(DataReaderWriter):

    pass
class PublisherSubscriber:

    pass
class dcps_PartitionQosPolicy:

    pass
class dcps_PresentationQosPolicy:

    pass
class dcps_GroupDataQosPolicy:

    pass
class dcps_UserDataQosPolicy:

    pass
class dcps_EntityFactoryQosPolicy:

    pass
class dcps_Subscriber(PublisherSubscriber):

    pass
class dcps_Publisher(PublisherSubscriber):

    pass
class DomainEntity:

    pass
class dcps_DataReaderWriter(DomainEntity):

    def __init__(self, copyFromTopicQos: bool, dcps_DataReaderWriter: "dcps_DeadlineQosPolicy" = None, dcps_DataReaderWriter23: "dcps_DestinationOrderQosPolicy" = None, dcps_DataReaderWriter25: "dcps_DurabilityQosPolicy" = None, dcps_DataReaderWriter27: "dcps_HistoryQosPolicy" = None, dcps_DataReaderWriter29: "dcps_LatencyBudgetQosPolicy" = None, dcps_DataReaderWriter31: "dcps_LivelinessQosPolicy" = None, dcps_DataReaderWriter33: "dcps_OwnershipQosPolicy" = None, dcps_DataReaderWriter35: "dcps_ReliabilityQosPolicy" = None, dcps_DataReaderWriter37: "dcps_ResourceLimitsQosPolicy" = None, dcps_DataReaderWriter39: "dcps_UserDataQosPolicy" = None):
        self.copyFromTopicQos = copyFromTopicQos
        self.dcps_DataReaderWriter = dcps_DataReaderWriter
        self.dcps_DataReaderWriter23 = dcps_DataReaderWriter23
        self.dcps_DataReaderWriter25 = dcps_DataReaderWriter25
        self.dcps_DataReaderWriter27 = dcps_DataReaderWriter27
        self.dcps_DataReaderWriter29 = dcps_DataReaderWriter29
        self.dcps_DataReaderWriter31 = dcps_DataReaderWriter31
        self.dcps_DataReaderWriter33 = dcps_DataReaderWriter33
        self.dcps_DataReaderWriter35 = dcps_DataReaderWriter35
        self.dcps_DataReaderWriter37 = dcps_DataReaderWriter37
        self.dcps_DataReaderWriter39 = dcps_DataReaderWriter39
        
    @property
    def copyFromTopicQos(self) -> bool:
        return self.__copyFromTopicQos

    @copyFromTopicQos.setter
    def copyFromTopicQos(self, copyFromTopicQos: bool):
        self.__copyFromTopicQos = copyFromTopicQos

    @property
    def dcps_DataReaderWriter35(self):
        return self.__dcps_DataReaderWriter35

    @dcps_DataReaderWriter35.setter
    def dcps_DataReaderWriter35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcps_DataReaderWriter__dcps_DataReaderWriter35", None)
        self.__dcps_DataReaderWriter35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dcps_ReliabilityQosPolicy"):
                opp_val = getattr(old_value, "dcps_ReliabilityQosPolicy", None)
                if opp_val == self:
                    setattr(old_value, "dcps_ReliabilityQosPolicy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dcps_ReliabilityQosPolicy"):
                opp_val = getattr(value, "dcps_ReliabilityQosPolicy", None)
                setattr(value, "dcps_ReliabilityQosPolicy", self)

    @property
    def dcps_DataReaderWriter23(self):
        return self.__dcps_DataReaderWriter23

    @dcps_DataReaderWriter23.setter
    def dcps_DataReaderWriter23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcps_DataReaderWriter__dcps_DataReaderWriter23", None)
        self.__dcps_DataReaderWriter23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dcps_DestinationOrderQosPolicy"):
                opp_val = getattr(old_value, "dcps_DestinationOrderQosPolicy", None)
                if opp_val == self:
                    setattr(old_value, "dcps_DestinationOrderQosPolicy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dcps_DestinationOrderQosPolicy"):
                opp_val = getattr(value, "dcps_DestinationOrderQosPolicy", None)
                setattr(value, "dcps_DestinationOrderQosPolicy", self)

    @property
    def dcps_DataReaderWriter25(self):
        return self.__dcps_DataReaderWriter25

    @dcps_DataReaderWriter25.setter
    def dcps_DataReaderWriter25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcps_DataReaderWriter__dcps_DataReaderWriter25", None)
        self.__dcps_DataReaderWriter25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dcps_DurabilityQosPolicy"):
                opp_val = getattr(old_value, "dcps_DurabilityQosPolicy", None)
                if opp_val == self:
                    setattr(old_value, "dcps_DurabilityQosPolicy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dcps_DurabilityQosPolicy"):
                opp_val = getattr(value, "dcps_DurabilityQosPolicy", None)
                setattr(value, "dcps_DurabilityQosPolicy", self)

    @property
    def dcps_DataReaderWriter27(self):
        return self.__dcps_DataReaderWriter27

    @dcps_DataReaderWriter27.setter
    def dcps_DataReaderWriter27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcps_DataReaderWriter__dcps_DataReaderWriter27", None)
        self.__dcps_DataReaderWriter27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dcps_HistoryQosPolicy"):
                opp_val = getattr(old_value, "dcps_HistoryQosPolicy", None)
                if opp_val == self:
                    setattr(old_value, "dcps_HistoryQosPolicy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dcps_HistoryQosPolicy"):
                opp_val = getattr(value, "dcps_HistoryQosPolicy", None)
                setattr(value, "dcps_HistoryQosPolicy", self)

    @property
    def dcps_DataReaderWriter33(self):
        return self.__dcps_DataReaderWriter33

    @dcps_DataReaderWriter33.setter
    def dcps_DataReaderWriter33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcps_DataReaderWriter__dcps_DataReaderWriter33", None)
        self.__dcps_DataReaderWriter33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dcps_OwnershipQosPolicy"):
                opp_val = getattr(old_value, "dcps_OwnershipQosPolicy", None)
                if opp_val == self:
                    setattr(old_value, "dcps_OwnershipQosPolicy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dcps_OwnershipQosPolicy"):
                opp_val = getattr(value, "dcps_OwnershipQosPolicy", None)
                setattr(value, "dcps_OwnershipQosPolicy", self)

    @property
    def dcps_DataReaderWriter(self):
        return self.__dcps_DataReaderWriter

    @dcps_DataReaderWriter.setter
    def dcps_DataReaderWriter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcps_DataReaderWriter__dcps_DataReaderWriter", None)
        self.__dcps_DataReaderWriter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dcps_DeadlineQosPolicy"):
                opp_val = getattr(old_value, "dcps_DeadlineQosPolicy", None)
                if opp_val == self:
                    setattr(old_value, "dcps_DeadlineQosPolicy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dcps_DeadlineQosPolicy"):
                opp_val = getattr(value, "dcps_DeadlineQosPolicy", None)
                setattr(value, "dcps_DeadlineQosPolicy", self)

    @property
    def dcps_DataReaderWriter37(self):
        return self.__dcps_DataReaderWriter37

    @dcps_DataReaderWriter37.setter
    def dcps_DataReaderWriter37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcps_DataReaderWriter__dcps_DataReaderWriter37", None)
        self.__dcps_DataReaderWriter37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dcps_ResourceLimitsQosPolicy"):
                opp_val = getattr(old_value, "dcps_ResourceLimitsQosPolicy", None)
                if opp_val == self:
                    setattr(old_value, "dcps_ResourceLimitsQosPolicy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dcps_ResourceLimitsQosPolicy"):
                opp_val = getattr(value, "dcps_ResourceLimitsQosPolicy", None)
                setattr(value, "dcps_ResourceLimitsQosPolicy", self)

    @property
    def dcps_DataReaderWriter29(self):
        return self.__dcps_DataReaderWriter29

    @dcps_DataReaderWriter29.setter
    def dcps_DataReaderWriter29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcps_DataReaderWriter__dcps_DataReaderWriter29", None)
        self.__dcps_DataReaderWriter29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dcps_LatencyBudgetQosPolicy"):
                opp_val = getattr(old_value, "dcps_LatencyBudgetQosPolicy", None)
                if opp_val == self:
                    setattr(old_value, "dcps_LatencyBudgetQosPolicy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dcps_LatencyBudgetQosPolicy"):
                opp_val = getattr(value, "dcps_LatencyBudgetQosPolicy", None)
                setattr(value, "dcps_LatencyBudgetQosPolicy", self)

    @property
    def dcps_DataReaderWriter39(self):
        return self.__dcps_DataReaderWriter39

    @dcps_DataReaderWriter39.setter
    def dcps_DataReaderWriter39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcps_DataReaderWriter__dcps_DataReaderWriter39", None)
        self.__dcps_DataReaderWriter39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dcps_UserDataQosPolicy40"):
                opp_val = getattr(old_value, "dcps_UserDataQosPolicy40", None)
                if opp_val == self:
                    setattr(old_value, "dcps_UserDataQosPolicy40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dcps_UserDataQosPolicy40"):
                opp_val = getattr(value, "dcps_UserDataQosPolicy40", None)
                setattr(value, "dcps_UserDataQosPolicy40", self)

    @property
    def dcps_DataReaderWriter31(self):
        return self.__dcps_DataReaderWriter31

    @dcps_DataReaderWriter31.setter
    def dcps_DataReaderWriter31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcps_DataReaderWriter__dcps_DataReaderWriter31", None)
        self.__dcps_DataReaderWriter31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dcps_LivelinessQosPolicy"):
                opp_val = getattr(old_value, "dcps_LivelinessQosPolicy", None)
                if opp_val == self:
                    setattr(old_value, "dcps_LivelinessQosPolicy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dcps_LivelinessQosPolicy"):
                opp_val = getattr(value, "dcps_LivelinessQosPolicy", None)
                setattr(value, "dcps_LivelinessQosPolicy", self)

class dcps_DomainParticipant(DomainEntity):

    pass
class Entity:

    pass
class dcps_Domain(Entity):

    def __init__(self, domainId: str, dcps_Domain: "dcps_DomainParticipant" = None):
        self.domainId = domainId
        self.dcps_Domain = dcps_Domain
        
    @property
    def domainId(self) -> str:
        return self.__domainId

    @domainId.setter
    def domainId(self, domainId: str):
        self.__domainId = domainId

    @property
    def dcps_Domain(self):
        return self.__dcps_Domain

    @dcps_Domain.setter
    def dcps_Domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcps_Domain__dcps_Domain", None)
        self.__dcps_Domain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dcps_DomainParticipant"):
                opp_val = getattr(old_value, "dcps_DomainParticipant", None)
                if opp_val == self:
                    setattr(old_value, "dcps_DomainParticipant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dcps_DomainParticipant"):
                opp_val = getattr(value, "dcps_DomainParticipant", None)
                setattr(value, "dcps_DomainParticipant", self)

class dcps_PublisherSubscriber(DomainEntity):

    def __init__(self, transportId: int, dcps_PublisherSubscriber: "dcps_EntityFactoryQosPolicy" = None, dcps_PublisherSubscriber12: "dcps_GroupDataQosPolicy" = None, dcps_PublisherSubscriber14: "dcps_PresentationQosPolicy" = None, dcps_PublisherSubscriber16: "dcps_PartitionQosPolicy" = None):
        self.transportId = transportId
        self.dcps_PublisherSubscriber = dcps_PublisherSubscriber
        self.dcps_PublisherSubscriber12 = dcps_PublisherSubscriber12
        self.dcps_PublisherSubscriber14 = dcps_PublisherSubscriber14
        self.dcps_PublisherSubscriber16 = dcps_PublisherSubscriber16
        
    @property
    def transportId(self) -> int:
        return self.__transportId

    @transportId.setter
    def transportId(self, transportId: int):
        self.__transportId = transportId

    @property
    def dcps_PublisherSubscriber(self):
        return self.__dcps_PublisherSubscriber

    @dcps_PublisherSubscriber.setter
    def dcps_PublisherSubscriber(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcps_PublisherSubscriber__dcps_PublisherSubscriber", None)
        self.__dcps_PublisherSubscriber = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dcps_EntityFactoryQosPolicy10"):
                opp_val = getattr(old_value, "dcps_EntityFactoryQosPolicy10", None)
                if opp_val == self:
                    setattr(old_value, "dcps_EntityFactoryQosPolicy10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dcps_EntityFactoryQosPolicy10"):
                opp_val = getattr(value, "dcps_EntityFactoryQosPolicy10", None)
                setattr(value, "dcps_EntityFactoryQosPolicy10", self)

    @property
    def dcps_PublisherSubscriber12(self):
        return self.__dcps_PublisherSubscriber12

    @dcps_PublisherSubscriber12.setter
    def dcps_PublisherSubscriber12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcps_PublisherSubscriber__dcps_PublisherSubscriber12", None)
        self.__dcps_PublisherSubscriber12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dcps_GroupDataQosPolicy"):
                opp_val = getattr(old_value, "dcps_GroupDataQosPolicy", None)
                if opp_val == self:
                    setattr(old_value, "dcps_GroupDataQosPolicy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dcps_GroupDataQosPolicy"):
                opp_val = getattr(value, "dcps_GroupDataQosPolicy", None)
                setattr(value, "dcps_GroupDataQosPolicy", self)

    @property
    def dcps_PublisherSubscriber14(self):
        return self.__dcps_PublisherSubscriber14

    @dcps_PublisherSubscriber14.setter
    def dcps_PublisherSubscriber14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcps_PublisherSubscriber__dcps_PublisherSubscriber14", None)
        self.__dcps_PublisherSubscriber14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dcps_PresentationQosPolicy"):
                opp_val = getattr(old_value, "dcps_PresentationQosPolicy", None)
                if opp_val == self:
                    setattr(old_value, "dcps_PresentationQosPolicy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dcps_PresentationQosPolicy"):
                opp_val = getattr(value, "dcps_PresentationQosPolicy", None)
                setattr(value, "dcps_PresentationQosPolicy", self)

    @property
    def dcps_PublisherSubscriber16(self):
        return self.__dcps_PublisherSubscriber16

    @dcps_PublisherSubscriber16.setter
    def dcps_PublisherSubscriber16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcps_PublisherSubscriber__dcps_PublisherSubscriber16", None)
        self.__dcps_PublisherSubscriber16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dcps_PartitionQosPolicy"):
                opp_val = getattr(old_value, "dcps_PartitionQosPolicy", None)
                if opp_val == self:
                    setattr(old_value, "dcps_PartitionQosPolicy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dcps_PartitionQosPolicy"):
                opp_val = getattr(value, "dcps_PartitionQosPolicy", None)
                setattr(value, "dcps_PartitionQosPolicy", self)
