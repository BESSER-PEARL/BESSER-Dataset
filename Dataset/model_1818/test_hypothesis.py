import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ddsMetamodel_DdsLifespan,
    ddsMetamodel_DdsTransportPriorityQos,
    ddsMetamodel_DdsResourceLimits,
    ddsMetamodel_DdsHistoryQos,
    ddsMetamodel_DdsSystem,
    ddsMetamodel_DdsDataModule,
    ddsMetamodel_DdsDataWriterListener,
    ddsMetamodel_DdsPublisherListener,
    ddsMetamodel_DdsDataWriter,
    ddsMetamodel_DdsStructuredField,
    ddsMetamodel_DdsDataField,
    ddsMetamodel_DdsDataReader,
    ddsMetamodel_DdsQosProfile,
    ddsMetamodel_DdsDataStructure,
    ddsMetamodel_DdsTopicListener,
    ddsMetamodel_DdsTopic,
    ddsMetamodel_DdsDomainParticipantListener,
    ddsMetamodel_DdsPublisher,
    ddsMetamodel_DdsSubscriber,
    ddsMetamodel_DdsWaitSet,
    ddsMetamodel_DdsDomainParticipant,
    ddsMetamodel_DdsApplication,
    ddsMetamodel_DdsDataReaderListener,
    ddsMetamodel_DdsSubscriberListener,
    ddsMetamodel_DdsHost,
    DdsReadCondition,
    ddsMetamodel_QueryCondition,
    DdsStatusCondition,
    ddsMetamodel_DdsPublisherStatusCondition,
    ddsMetamodel_DdsTopicStatusCondition,
    ddsMetamodel_DdsDataReaderStatusCondition,
    ddsMetamodel_DdsDomainParticipantStatusCondition,
    ddsMetamodel_DdsDataWriterStatusCondition,
    ddsMetamodel_DdsSubscriberStatusCondition,
    ddsMetamodel_GuardCondition,
    ddsMetamodel_DdsStatusCondition,
    ddsMetamodel_DdsReadCondition,
    ddsMetamodel_DdsGroupDataQos,
    ddsMetamodel_DdsDataWriterLifecycleQos,
    ddsMetamodel_DdsPartitionQos,
    ddsMetamodel_DdsTimeBasedFilterQos,
    ddsMetamodel_DdsDataReaderLifecycleQos,
    ddsMetamodel_DdsPresentationQos,
    ddsMetamodel_DdsDuration,
    ddsMetamodel_DdsOwnershipStrengthQos,
    ddsMetamodel_DdsDestinationOrderQos,
    ddsMetamodel_DdsReliabilityQos,
    ddsMetamodel_DdsOwnershipQos,
    ddsMetamodel_DdsLivelinessQos,
    ddsMetamodel_DdsLatencyBudgetQos,
    ddsMetamodel_DdsDurabilityServiceQos,
    ddsMetamodel_DdsDurabilityQos,
    ddsMetamodel_DdsTopicDataQos,
    ddsMetamodel_DdsEntityFactoryQos,
    ddsMetamodel_DdsUserDataQos,
    DdsQosProfile,
    ddsMetamodel_DdsDomainParticipantQosProfile,
    ddsMetamodel_DdsPublisherQosProfile,
    ddsMetamodel_DdsSubscriberQosProfile,
    ddsMetamodel_DdsDataReaderQosProfile,
    ddsMetamodel_DdsDataWriterQosProfile,
    ddsMetamodel_DdsTopicQosProfile,
    ddsMetamodel_DdsDeadlineQos,
    DataReaderStatus,
    DestinationOrderQosPolicyKind,
    SampleStateKind,
    SubscriberStatus,
    ViewStateKind,
    ReliabilityQosPolicyKind,
    OwnershipQosPolicyKind,
    DomainParticipantStatus,
    DataWriterStatus,
    LivelinessQosPolicyKind,
    DurabilityQosPolicyKind,
    InvalidSampleVisibilityQosPolicy,
    TopicStatus,
    HistoryQosPolicyKind,
    PublisherStatus,
    InstanceStateKind,
    PresentationQosPolicyAccessScopeKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ddsmetamodel_ddslifespan_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsLifespan)


def test_ddsmetamodel_ddslifespan_constructor_exists():
    assert callable(ddsMetamodel_DdsLifespan.__init__)


def test_ddsmetamodel_ddslifespan_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsLifespan.__init__)
    params = list(sig.parameters.keys())



def test_ddsmetamodel_ddstransportpriorityqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsTransportPriorityQos)


def test_ddsmetamodel_ddstransportpriorityqos_constructor_exists():
    assert callable(ddsMetamodel_DdsTransportPriorityQos.__init__)


def test_ddsmetamodel_ddstransportpriorityqos_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsTransportPriorityQos.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ddsmetamodel_ddstransportpriorityqos_has_value():
    assert hasattr(ddsMetamodel_DdsTransportPriorityQos, "value")
    descriptor = None
    for klass in ddsMetamodel_DdsTransportPriorityQos.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddsresourcelimits_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsResourceLimits)


def test_ddsmetamodel_ddsresourcelimits_constructor_exists():
    assert callable(ddsMetamodel_DdsResourceLimits.__init__)


def test_ddsmetamodel_ddsresourcelimits_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsResourceLimits.__init__)
    params = list(sig.parameters.keys())
    assert "max_samples_per_instances" in params, "Missing parameter 'max_samples_per_instances'"
    assert "max_instances" in params, "Missing parameter 'max_instances'"
    assert "max_samples" in params, "Missing parameter 'max_samples'"

def test_ddsmetamodel_ddsresourcelimits_has_max_samples_per_instances():
    assert hasattr(ddsMetamodel_DdsResourceLimits, "max_samples_per_instances")
    descriptor = None
    for klass in ddsMetamodel_DdsResourceLimits.__mro__:
        if "max_samples_per_instances" in klass.__dict__:
            descriptor = klass.__dict__["max_samples_per_instances"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel_ddsresourcelimits_has_max_instances():
    assert hasattr(ddsMetamodel_DdsResourceLimits, "max_instances")
    descriptor = None
    for klass in ddsMetamodel_DdsResourceLimits.__mro__:
        if "max_instances" in klass.__dict__:
            descriptor = klass.__dict__["max_instances"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel_ddsresourcelimits_has_max_samples():
    assert hasattr(ddsMetamodel_DdsResourceLimits, "max_samples")
    descriptor = None
    for klass in ddsMetamodel_DdsResourceLimits.__mro__:
        if "max_samples" in klass.__dict__:
            descriptor = klass.__dict__["max_samples"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddshistoryqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsHistoryQos)


def test_ddsmetamodel_ddshistoryqos_constructor_exists():
    assert callable(ddsMetamodel_DdsHistoryQos.__init__)


def test_ddsmetamodel_ddshistoryqos_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsHistoryQos.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "depth" in params, "Missing parameter 'depth'"

def test_ddsmetamodel_ddshistoryqos_has_kind():
    assert hasattr(ddsMetamodel_DdsHistoryQos, "kind")
    descriptor = None
    for klass in ddsMetamodel_DdsHistoryQos.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel_ddshistoryqos_has_depth():
    assert hasattr(ddsMetamodel_DdsHistoryQos, "depth")
    descriptor = None
    for klass in ddsMetamodel_DdsHistoryQos.__mro__:
        if "depth" in klass.__dict__:
            descriptor = klass.__dict__["depth"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddssystem_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsSystem)


def test_ddsmetamodel_ddssystem_constructor_exists():
    assert callable(ddsMetamodel_DdsSystem.__init__)


def test_ddsmetamodel_ddssystem_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsSystem.__init__)
    params = list(sig.parameters.keys())
    assert "systemName" in params, "Missing parameter 'systemName'"

def test_ddsmetamodel_ddssystem_has_systemName():
    assert hasattr(ddsMetamodel_DdsSystem, "systemName")
    descriptor = None
    for klass in ddsMetamodel_DdsSystem.__mro__:
        if "systemName" in klass.__dict__:
            descriptor = klass.__dict__["systemName"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddsdatamodule_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsDataModule)


def test_ddsmetamodel_ddsdatamodule_constructor_exists():
    assert callable(ddsMetamodel_DdsDataModule.__init__)


def test_ddsmetamodel_ddsdatamodule_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsDataModule.__init__)
    params = list(sig.parameters.keys())
    assert "moduleName" in params, "Missing parameter 'moduleName'"

def test_ddsmetamodel_ddsdatamodule_has_moduleName():
    assert hasattr(ddsMetamodel_DdsDataModule, "moduleName")
    descriptor = None
    for klass in ddsMetamodel_DdsDataModule.__mro__:
        if "moduleName" in klass.__dict__:
            descriptor = klass.__dict__["moduleName"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddsdatawriterlistener_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsDataWriterListener)


def test_ddsmetamodel_ddsdatawriterlistener_constructor_exists():
    assert callable(ddsMetamodel_DdsDataWriterListener.__init__)


def test_ddsmetamodel_ddsdatawriterlistener_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsDataWriterListener.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "listenedStatus" in params, "Missing parameter 'listenedStatus'"

def test_ddsmetamodel_ddsdatawriterlistener_has_name():
    assert hasattr(ddsMetamodel_DdsDataWriterListener, "name")
    descriptor = None
    for klass in ddsMetamodel_DdsDataWriterListener.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel_ddsdatawriterlistener_has_listenedStatus():
    assert hasattr(ddsMetamodel_DdsDataWriterListener, "listenedStatus")
    descriptor = None
    for klass in ddsMetamodel_DdsDataWriterListener.__mro__:
        if "listenedStatus" in klass.__dict__:
            descriptor = klass.__dict__["listenedStatus"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddspublisherlistener_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsPublisherListener)


def test_ddsmetamodel_ddspublisherlistener_constructor_exists():
    assert callable(ddsMetamodel_DdsPublisherListener.__init__)


def test_ddsmetamodel_ddspublisherlistener_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsPublisherListener.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "listenedStatus" in params, "Missing parameter 'listenedStatus'"

def test_ddsmetamodel_ddspublisherlistener_has_name():
    assert hasattr(ddsMetamodel_DdsPublisherListener, "name")
    descriptor = None
    for klass in ddsMetamodel_DdsPublisherListener.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel_ddspublisherlistener_has_listenedStatus():
    assert hasattr(ddsMetamodel_DdsPublisherListener, "listenedStatus")
    descriptor = None
    for klass in ddsMetamodel_DdsPublisherListener.__mro__:
        if "listenedStatus" in klass.__dict__:
            descriptor = klass.__dict__["listenedStatus"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddsdatawriter_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsDataWriter)


def test_ddsmetamodel_ddsdatawriter_constructor_exists():
    assert callable(ddsMetamodel_DdsDataWriter.__init__)


def test_ddsmetamodel_ddsdatawriter_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsDataWriter.__init__)
    params = list(sig.parameters.keys())
    assert "dataWriterName" in params, "Missing parameter 'dataWriterName'"

def test_ddsmetamodel_ddsdatawriter_has_dataWriterName():
    assert hasattr(ddsMetamodel_DdsDataWriter, "dataWriterName")
    descriptor = None
    for klass in ddsMetamodel_DdsDataWriter.__mro__:
        if "dataWriterName" in klass.__dict__:
            descriptor = klass.__dict__["dataWriterName"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddsstructuredfield_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsStructuredField)


def test_ddsmetamodel_ddsstructuredfield_constructor_exists():
    assert callable(ddsMetamodel_DdsStructuredField.__init__)


def test_ddsmetamodel_ddsstructuredfield_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsStructuredField.__init__)
    params = list(sig.parameters.keys())
    assert "fieldName" in params, "Missing parameter 'fieldName'"
    assert "maxMultiplicity" in params, "Missing parameter 'maxMultiplicity'"
    assert "isKey" in params, "Missing parameter 'isKey'"

def test_ddsmetamodel_ddsstructuredfield_has_fieldName():
    assert hasattr(ddsMetamodel_DdsStructuredField, "fieldName")
    descriptor = None
    for klass in ddsMetamodel_DdsStructuredField.__mro__:
        if "fieldName" in klass.__dict__:
            descriptor = klass.__dict__["fieldName"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel_ddsstructuredfield_has_maxMultiplicity():
    assert hasattr(ddsMetamodel_DdsStructuredField, "maxMultiplicity")
    descriptor = None
    for klass in ddsMetamodel_DdsStructuredField.__mro__:
        if "maxMultiplicity" in klass.__dict__:
            descriptor = klass.__dict__["maxMultiplicity"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel_ddsstructuredfield_has_isKey():
    assert hasattr(ddsMetamodel_DdsStructuredField, "isKey")
    descriptor = None
    for klass in ddsMetamodel_DdsStructuredField.__mro__:
        if "isKey" in klass.__dict__:
            descriptor = klass.__dict__["isKey"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddsdatafield_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsDataField)


def test_ddsmetamodel_ddsdatafield_constructor_exists():
    assert callable(ddsMetamodel_DdsDataField.__init__)


def test_ddsmetamodel_ddsdatafield_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsDataField.__init__)
    params = list(sig.parameters.keys())
    assert "maxMultiplicity" in params, "Missing parameter 'maxMultiplicity'"
    assert "fieldType" in params, "Missing parameter 'fieldType'"
    assert "fieldName" in params, "Missing parameter 'fieldName'"
    assert "isKey" in params, "Missing parameter 'isKey'"

def test_ddsmetamodel_ddsdatafield_has_maxMultiplicity():
    assert hasattr(ddsMetamodel_DdsDataField, "maxMultiplicity")
    descriptor = None
    for klass in ddsMetamodel_DdsDataField.__mro__:
        if "maxMultiplicity" in klass.__dict__:
            descriptor = klass.__dict__["maxMultiplicity"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel_ddsdatafield_has_fieldType():
    assert hasattr(ddsMetamodel_DdsDataField, "fieldType")
    descriptor = None
    for klass in ddsMetamodel_DdsDataField.__mro__:
        if "fieldType" in klass.__dict__:
            descriptor = klass.__dict__["fieldType"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel_ddsdatafield_has_fieldName():
    assert hasattr(ddsMetamodel_DdsDataField, "fieldName")
    descriptor = None
    for klass in ddsMetamodel_DdsDataField.__mro__:
        if "fieldName" in klass.__dict__:
            descriptor = klass.__dict__["fieldName"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel_ddsdatafield_has_isKey():
    assert hasattr(ddsMetamodel_DdsDataField, "isKey")
    descriptor = None
    for klass in ddsMetamodel_DdsDataField.__mro__:
        if "isKey" in klass.__dict__:
            descriptor = klass.__dict__["isKey"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddsdatareader_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsDataReader)


def test_ddsmetamodel_ddsdatareader_constructor_exists():
    assert callable(ddsMetamodel_DdsDataReader.__init__)


def test_ddsmetamodel_ddsdatareader_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsDataReader.__init__)
    params = list(sig.parameters.keys())
    assert "dataReaderName" in params, "Missing parameter 'dataReaderName'"

def test_ddsmetamodel_ddsdatareader_has_dataReaderName():
    assert hasattr(ddsMetamodel_DdsDataReader, "dataReaderName")
    descriptor = None
    for klass in ddsMetamodel_DdsDataReader.__mro__:
        if "dataReaderName" in klass.__dict__:
            descriptor = klass.__dict__["dataReaderName"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddsqosprofile_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsQosProfile)


def test_ddsmetamodel_ddsqosprofile_constructor_exists():
    assert callable(ddsMetamodel_DdsQosProfile.__init__)


def test_ddsmetamodel_ddsqosprofile_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsQosProfile.__init__)
    params = list(sig.parameters.keys())
    assert "profileName" in params, "Missing parameter 'profileName'"

def test_ddsmetamodel_ddsqosprofile_has_profileName():
    assert hasattr(ddsMetamodel_DdsQosProfile, "profileName")
    descriptor = None
    for klass in ddsMetamodel_DdsQosProfile.__mro__:
        if "profileName" in klass.__dict__:
            descriptor = klass.__dict__["profileName"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddsdatastructure_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsDataStructure)


def test_ddsmetamodel_ddsdatastructure_constructor_exists():
    assert callable(ddsMetamodel_DdsDataStructure.__init__)


def test_ddsmetamodel_ddsdatastructure_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsDataStructure.__init__)
    params = list(sig.parameters.keys())
    assert "structureName" in params, "Missing parameter 'structureName'"

def test_ddsmetamodel_ddsdatastructure_has_structureName():
    assert hasattr(ddsMetamodel_DdsDataStructure, "structureName")
    descriptor = None
    for klass in ddsMetamodel_DdsDataStructure.__mro__:
        if "structureName" in klass.__dict__:
            descriptor = klass.__dict__["structureName"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddstopiclistener_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsTopicListener)


def test_ddsmetamodel_ddstopiclistener_constructor_exists():
    assert callable(ddsMetamodel_DdsTopicListener.__init__)


def test_ddsmetamodel_ddstopiclistener_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsTopicListener.__init__)
    params = list(sig.parameters.keys())
    assert "listenedStatus" in params, "Missing parameter 'listenedStatus'"
    assert "name" in params, "Missing parameter 'name'"

def test_ddsmetamodel_ddstopiclistener_has_listenedStatus():
    assert hasattr(ddsMetamodel_DdsTopicListener, "listenedStatus")
    descriptor = None
    for klass in ddsMetamodel_DdsTopicListener.__mro__:
        if "listenedStatus" in klass.__dict__:
            descriptor = klass.__dict__["listenedStatus"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel_ddstopiclistener_has_name():
    assert hasattr(ddsMetamodel_DdsTopicListener, "name")
    descriptor = None
    for klass in ddsMetamodel_DdsTopicListener.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddstopic_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsTopic)


def test_ddsmetamodel_ddstopic_constructor_exists():
    assert callable(ddsMetamodel_DdsTopic.__init__)


def test_ddsmetamodel_ddstopic_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsTopic.__init__)
    params = list(sig.parameters.keys())
    assert "topicName" in params, "Missing parameter 'topicName'"

def test_ddsmetamodel_ddstopic_has_topicName():
    assert hasattr(ddsMetamodel_DdsTopic, "topicName")
    descriptor = None
    for klass in ddsMetamodel_DdsTopic.__mro__:
        if "topicName" in klass.__dict__:
            descriptor = klass.__dict__["topicName"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddsdomainparticipantlistener_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsDomainParticipantListener)


def test_ddsmetamodel_ddsdomainparticipantlistener_constructor_exists():
    assert callable(ddsMetamodel_DdsDomainParticipantListener.__init__)


def test_ddsmetamodel_ddsdomainparticipantlistener_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsDomainParticipantListener.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "listenedStatus" in params, "Missing parameter 'listenedStatus'"

def test_ddsmetamodel_ddsdomainparticipantlistener_has_name():
    assert hasattr(ddsMetamodel_DdsDomainParticipantListener, "name")
    descriptor = None
    for klass in ddsMetamodel_DdsDomainParticipantListener.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel_ddsdomainparticipantlistener_has_listenedStatus():
    assert hasattr(ddsMetamodel_DdsDomainParticipantListener, "listenedStatus")
    descriptor = None
    for klass in ddsMetamodel_DdsDomainParticipantListener.__mro__:
        if "listenedStatus" in klass.__dict__:
            descriptor = klass.__dict__["listenedStatus"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddspublisher_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsPublisher)


def test_ddsmetamodel_ddspublisher_constructor_exists():
    assert callable(ddsMetamodel_DdsPublisher.__init__)


def test_ddsmetamodel_ddspublisher_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsPublisher.__init__)
    params = list(sig.parameters.keys())
    assert "publisherName" in params, "Missing parameter 'publisherName'"

def test_ddsmetamodel_ddspublisher_has_publisherName():
    assert hasattr(ddsMetamodel_DdsPublisher, "publisherName")
    descriptor = None
    for klass in ddsMetamodel_DdsPublisher.__mro__:
        if "publisherName" in klass.__dict__:
            descriptor = klass.__dict__["publisherName"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddssubscriber_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsSubscriber)


def test_ddsmetamodel_ddssubscriber_constructor_exists():
    assert callable(ddsMetamodel_DdsSubscriber.__init__)


def test_ddsmetamodel_ddssubscriber_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsSubscriber.__init__)
    params = list(sig.parameters.keys())
    assert "subscriberName" in params, "Missing parameter 'subscriberName'"

def test_ddsmetamodel_ddssubscriber_has_subscriberName():
    assert hasattr(ddsMetamodel_DdsSubscriber, "subscriberName")
    descriptor = None
    for klass in ddsMetamodel_DdsSubscriber.__mro__:
        if "subscriberName" in klass.__dict__:
            descriptor = klass.__dict__["subscriberName"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddswaitset_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsWaitSet)


def test_ddsmetamodel_ddswaitset_constructor_exists():
    assert callable(ddsMetamodel_DdsWaitSet.__init__)


def test_ddsmetamodel_ddswaitset_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsWaitSet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ddsmetamodel_ddswaitset_has_name():
    assert hasattr(ddsMetamodel_DdsWaitSet, "name")
    descriptor = None
    for klass in ddsMetamodel_DdsWaitSet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddsdomainparticipant_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsDomainParticipant)


def test_ddsmetamodel_ddsdomainparticipant_constructor_exists():
    assert callable(ddsMetamodel_DdsDomainParticipant.__init__)


def test_ddsmetamodel_ddsdomainparticipant_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsDomainParticipant.__init__)
    params = list(sig.parameters.keys())
    assert "domainParticipantName" in params, "Missing parameter 'domainParticipantName'"
    assert "domainId" in params, "Missing parameter 'domainId'"

def test_ddsmetamodel_ddsdomainparticipant_has_domainParticipantName():
    assert hasattr(ddsMetamodel_DdsDomainParticipant, "domainParticipantName")
    descriptor = None
    for klass in ddsMetamodel_DdsDomainParticipant.__mro__:
        if "domainParticipantName" in klass.__dict__:
            descriptor = klass.__dict__["domainParticipantName"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel_ddsdomainparticipant_has_domainId():
    assert hasattr(ddsMetamodel_DdsDomainParticipant, "domainId")
    descriptor = None
    for klass in ddsMetamodel_DdsDomainParticipant.__mro__:
        if "domainId" in klass.__dict__:
            descriptor = klass.__dict__["domainId"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddsapplication_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsApplication)


def test_ddsmetamodel_ddsapplication_constructor_exists():
    assert callable(ddsMetamodel_DdsApplication.__init__)


def test_ddsmetamodel_ddsapplication_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsApplication.__init__)
    params = list(sig.parameters.keys())
    assert "applicationName" in params, "Missing parameter 'applicationName'"

def test_ddsmetamodel_ddsapplication_has_applicationName():
    assert hasattr(ddsMetamodel_DdsApplication, "applicationName")
    descriptor = None
    for klass in ddsMetamodel_DdsApplication.__mro__:
        if "applicationName" in klass.__dict__:
            descriptor = klass.__dict__["applicationName"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddsdatareaderlistener_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsDataReaderListener)


def test_ddsmetamodel_ddsdatareaderlistener_constructor_exists():
    assert callable(ddsMetamodel_DdsDataReaderListener.__init__)


def test_ddsmetamodel_ddsdatareaderlistener_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsDataReaderListener.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "listenedStatus" in params, "Missing parameter 'listenedStatus'"

def test_ddsmetamodel_ddsdatareaderlistener_has_name():
    assert hasattr(ddsMetamodel_DdsDataReaderListener, "name")
    descriptor = None
    for klass in ddsMetamodel_DdsDataReaderListener.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel_ddsdatareaderlistener_has_listenedStatus():
    assert hasattr(ddsMetamodel_DdsDataReaderListener, "listenedStatus")
    descriptor = None
    for klass in ddsMetamodel_DdsDataReaderListener.__mro__:
        if "listenedStatus" in klass.__dict__:
            descriptor = klass.__dict__["listenedStatus"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddssubscriberlistener_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsSubscriberListener)


def test_ddsmetamodel_ddssubscriberlistener_constructor_exists():
    assert callable(ddsMetamodel_DdsSubscriberListener.__init__)


def test_ddsmetamodel_ddssubscriberlistener_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsSubscriberListener.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "listenedStatus" in params, "Missing parameter 'listenedStatus'"

def test_ddsmetamodel_ddssubscriberlistener_has_name():
    assert hasattr(ddsMetamodel_DdsSubscriberListener, "name")
    descriptor = None
    for klass in ddsMetamodel_DdsSubscriberListener.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel_ddssubscriberlistener_has_listenedStatus():
    assert hasattr(ddsMetamodel_DdsSubscriberListener, "listenedStatus")
    descriptor = None
    for klass in ddsMetamodel_DdsSubscriberListener.__mro__:
        if "listenedStatus" in klass.__dict__:
            descriptor = klass.__dict__["listenedStatus"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddshost_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsHost)


def test_ddsmetamodel_ddshost_constructor_exists():
    assert callable(ddsMetamodel_DdsHost.__init__)


def test_ddsmetamodel_ddshost_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsHost.__init__)
    params = list(sig.parameters.keys())
    assert "hostName" in params, "Missing parameter 'hostName'"

def test_ddsmetamodel_ddshost_has_hostName():
    assert hasattr(ddsMetamodel_DdsHost, "hostName")
    descriptor = None
    for klass in ddsMetamodel_DdsHost.__mro__:
        if "hostName" in klass.__dict__:
            descriptor = klass.__dict__["hostName"]
            break
    assert isinstance(descriptor, property)



def test_ddsreadcondition_is_not_abstract():
    assert not inspect.isabstract(DdsReadCondition)


def test_ddsreadcondition_constructor_exists():
    assert callable(DdsReadCondition.__init__)


def test_ddsreadcondition_constructor_args():
    sig = inspect.signature(DdsReadCondition.__init__)
    params = list(sig.parameters.keys())



def test_ddsmetamodel_querycondition_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_QueryCondition)


def test_ddsmetamodel_querycondition_constructor_exists():
    assert callable(ddsMetamodel_QueryCondition.__init__)


def test_ddsmetamodel_querycondition_constructor_args():
    sig = inspect.signature(ddsMetamodel_QueryCondition.__init__)
    params = list(sig.parameters.keys())
    assert "query" in params, "Missing parameter 'query'"
    assert "queryParameters" in params, "Missing parameter 'queryParameters'"

def test_ddsmetamodel_querycondition_has_query():
    assert hasattr(ddsMetamodel_QueryCondition, "query")
    descriptor = None
    for klass in ddsMetamodel_QueryCondition.__mro__:
        if "query" in klass.__dict__:
            descriptor = klass.__dict__["query"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel_querycondition_has_queryParameters():
    assert hasattr(ddsMetamodel_QueryCondition, "queryParameters")
    descriptor = None
    for klass in ddsMetamodel_QueryCondition.__mro__:
        if "queryParameters" in klass.__dict__:
            descriptor = klass.__dict__["queryParameters"]
            break
    assert isinstance(descriptor, property)



def test_ddsstatuscondition_is_not_abstract():
    assert not inspect.isabstract(DdsStatusCondition)


def test_ddsstatuscondition_constructor_exists():
    assert callable(DdsStatusCondition.__init__)


def test_ddsstatuscondition_constructor_args():
    sig = inspect.signature(DdsStatusCondition.__init__)
    params = list(sig.parameters.keys())



def test_ddsmetamodel_ddspublisherstatuscondition_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsPublisherStatusCondition)


def test_ddsmetamodel_ddspublisherstatuscondition_constructor_exists():
    assert callable(ddsMetamodel_DdsPublisherStatusCondition.__init__)


def test_ddsmetamodel_ddspublisherstatuscondition_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsPublisherStatusCondition.__init__)
    params = list(sig.parameters.keys())
    assert "enabled_status" in params, "Missing parameter 'enabled_status'"

def test_ddsmetamodel_ddspublisherstatuscondition_has_enabled_status():
    assert hasattr(ddsMetamodel_DdsPublisherStatusCondition, "enabled_status")
    descriptor = None
    for klass in ddsMetamodel_DdsPublisherStatusCondition.__mro__:
        if "enabled_status" in klass.__dict__:
            descriptor = klass.__dict__["enabled_status"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddstopicstatuscondition_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsTopicStatusCondition)


def test_ddsmetamodel_ddstopicstatuscondition_constructor_exists():
    assert callable(ddsMetamodel_DdsTopicStatusCondition.__init__)


def test_ddsmetamodel_ddstopicstatuscondition_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsTopicStatusCondition.__init__)
    params = list(sig.parameters.keys())
    assert "enabled_status" in params, "Missing parameter 'enabled_status'"

def test_ddsmetamodel_ddstopicstatuscondition_has_enabled_status():
    assert hasattr(ddsMetamodel_DdsTopicStatusCondition, "enabled_status")
    descriptor = None
    for klass in ddsMetamodel_DdsTopicStatusCondition.__mro__:
        if "enabled_status" in klass.__dict__:
            descriptor = klass.__dict__["enabled_status"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddsdatareaderstatuscondition_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsDataReaderStatusCondition)


def test_ddsmetamodel_ddsdatareaderstatuscondition_constructor_exists():
    assert callable(ddsMetamodel_DdsDataReaderStatusCondition.__init__)


def test_ddsmetamodel_ddsdatareaderstatuscondition_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsDataReaderStatusCondition.__init__)
    params = list(sig.parameters.keys())
    assert "enabled_status" in params, "Missing parameter 'enabled_status'"

def test_ddsmetamodel_ddsdatareaderstatuscondition_has_enabled_status():
    assert hasattr(ddsMetamodel_DdsDataReaderStatusCondition, "enabled_status")
    descriptor = None
    for klass in ddsMetamodel_DdsDataReaderStatusCondition.__mro__:
        if "enabled_status" in klass.__dict__:
            descriptor = klass.__dict__["enabled_status"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddsdomainparticipantstatuscondition_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsDomainParticipantStatusCondition)


def test_ddsmetamodel_ddsdomainparticipantstatuscondition_constructor_exists():
    assert callable(ddsMetamodel_DdsDomainParticipantStatusCondition.__init__)


def test_ddsmetamodel_ddsdomainparticipantstatuscondition_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsDomainParticipantStatusCondition.__init__)
    params = list(sig.parameters.keys())
    assert "enabled_status" in params, "Missing parameter 'enabled_status'"

def test_ddsmetamodel_ddsdomainparticipantstatuscondition_has_enabled_status():
    assert hasattr(ddsMetamodel_DdsDomainParticipantStatusCondition, "enabled_status")
    descriptor = None
    for klass in ddsMetamodel_DdsDomainParticipantStatusCondition.__mro__:
        if "enabled_status" in klass.__dict__:
            descriptor = klass.__dict__["enabled_status"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddsdatawriterstatuscondition_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsDataWriterStatusCondition)


def test_ddsmetamodel_ddsdatawriterstatuscondition_constructor_exists():
    assert callable(ddsMetamodel_DdsDataWriterStatusCondition.__init__)


def test_ddsmetamodel_ddsdatawriterstatuscondition_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsDataWriterStatusCondition.__init__)
    params = list(sig.parameters.keys())
    assert "enabled_status" in params, "Missing parameter 'enabled_status'"

def test_ddsmetamodel_ddsdatawriterstatuscondition_has_enabled_status():
    assert hasattr(ddsMetamodel_DdsDataWriterStatusCondition, "enabled_status")
    descriptor = None
    for klass in ddsMetamodel_DdsDataWriterStatusCondition.__mro__:
        if "enabled_status" in klass.__dict__:
            descriptor = klass.__dict__["enabled_status"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddssubscriberstatuscondition_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsSubscriberStatusCondition)


def test_ddsmetamodel_ddssubscriberstatuscondition_constructor_exists():
    assert callable(ddsMetamodel_DdsSubscriberStatusCondition.__init__)


def test_ddsmetamodel_ddssubscriberstatuscondition_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsSubscriberStatusCondition.__init__)
    params = list(sig.parameters.keys())
    assert "enabled_status" in params, "Missing parameter 'enabled_status'"

def test_ddsmetamodel_ddssubscriberstatuscondition_has_enabled_status():
    assert hasattr(ddsMetamodel_DdsSubscriberStatusCondition, "enabled_status")
    descriptor = None
    for klass in ddsMetamodel_DdsSubscriberStatusCondition.__mro__:
        if "enabled_status" in klass.__dict__:
            descriptor = klass.__dict__["enabled_status"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_guardcondition_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_GuardCondition)


def test_ddsmetamodel_guardcondition_constructor_exists():
    assert callable(ddsMetamodel_GuardCondition.__init__)


def test_ddsmetamodel_guardcondition_constructor_args():
    sig = inspect.signature(ddsMetamodel_GuardCondition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ddsmetamodel_guardcondition_has_name():
    assert hasattr(ddsMetamodel_GuardCondition, "name")
    descriptor = None
    for klass in ddsMetamodel_GuardCondition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddsstatuscondition_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsStatusCondition)


def test_ddsmetamodel_ddsstatuscondition_constructor_exists():
    assert callable(ddsMetamodel_DdsStatusCondition.__init__)


def test_ddsmetamodel_ddsstatuscondition_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsStatusCondition.__init__)
    params = list(sig.parameters.keys())



def test_ddsmetamodel_ddsreadcondition_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsReadCondition)


def test_ddsmetamodel_ddsreadcondition_constructor_exists():
    assert callable(ddsMetamodel_DdsReadCondition.__init__)


def test_ddsmetamodel_ddsreadcondition_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsReadCondition.__init__)
    params = list(sig.parameters.keys())
    assert "instance_state_mask" in params, "Missing parameter 'instance_state_mask'"
    assert "sample_state_mask" in params, "Missing parameter 'sample_state_mask'"
    assert "view_state_mask" in params, "Missing parameter 'view_state_mask'"

def test_ddsmetamodel_ddsreadcondition_has_instance_state_mask():
    assert hasattr(ddsMetamodel_DdsReadCondition, "instance_state_mask")
    descriptor = None
    for klass in ddsMetamodel_DdsReadCondition.__mro__:
        if "instance_state_mask" in klass.__dict__:
            descriptor = klass.__dict__["instance_state_mask"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel_ddsreadcondition_has_sample_state_mask():
    assert hasattr(ddsMetamodel_DdsReadCondition, "sample_state_mask")
    descriptor = None
    for klass in ddsMetamodel_DdsReadCondition.__mro__:
        if "sample_state_mask" in klass.__dict__:
            descriptor = klass.__dict__["sample_state_mask"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel_ddsreadcondition_has_view_state_mask():
    assert hasattr(ddsMetamodel_DdsReadCondition, "view_state_mask")
    descriptor = None
    for klass in ddsMetamodel_DdsReadCondition.__mro__:
        if "view_state_mask" in klass.__dict__:
            descriptor = klass.__dict__["view_state_mask"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddsgroupdataqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsGroupDataQos)


def test_ddsmetamodel_ddsgroupdataqos_constructor_exists():
    assert callable(ddsMetamodel_DdsGroupDataQos.__init__)


def test_ddsmetamodel_ddsgroupdataqos_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsGroupDataQos.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ddsmetamodel_ddsgroupdataqos_has_value():
    assert hasattr(ddsMetamodel_DdsGroupDataQos, "value")
    descriptor = None
    for klass in ddsMetamodel_DdsGroupDataQos.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddsdatawriterlifecycleqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsDataWriterLifecycleQos)


def test_ddsmetamodel_ddsdatawriterlifecycleqos_constructor_exists():
    assert callable(ddsMetamodel_DdsDataWriterLifecycleQos.__init__)


def test_ddsmetamodel_ddsdatawriterlifecycleqos_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsDataWriterLifecycleQos.__init__)
    params = list(sig.parameters.keys())
    assert "autodispose_unregistered_instances" in params, "Missing parameter 'autodispose_unregistered_instances'"

def test_ddsmetamodel_ddsdatawriterlifecycleqos_has_autodispose_unregistered_instances():
    assert hasattr(ddsMetamodel_DdsDataWriterLifecycleQos, "autodispose_unregistered_instances")
    descriptor = None
    for klass in ddsMetamodel_DdsDataWriterLifecycleQos.__mro__:
        if "autodispose_unregistered_instances" in klass.__dict__:
            descriptor = klass.__dict__["autodispose_unregistered_instances"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddspartitionqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsPartitionQos)


def test_ddsmetamodel_ddspartitionqos_constructor_exists():
    assert callable(ddsMetamodel_DdsPartitionQos.__init__)


def test_ddsmetamodel_ddspartitionqos_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsPartitionQos.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ddsmetamodel_ddspartitionqos_has_name():
    assert hasattr(ddsMetamodel_DdsPartitionQos, "name")
    descriptor = None
    for klass in ddsMetamodel_DdsPartitionQos.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddstimebasedfilterqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsTimeBasedFilterQos)


def test_ddsmetamodel_ddstimebasedfilterqos_constructor_exists():
    assert callable(ddsMetamodel_DdsTimeBasedFilterQos.__init__)


def test_ddsmetamodel_ddstimebasedfilterqos_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsTimeBasedFilterQos.__init__)
    params = list(sig.parameters.keys())



def test_ddsmetamodel_ddsdatareaderlifecycleqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsDataReaderLifecycleQos)


def test_ddsmetamodel_ddsdatareaderlifecycleqos_constructor_exists():
    assert callable(ddsMetamodel_DdsDataReaderLifecycleQos.__init__)


def test_ddsmetamodel_ddsdatareaderlifecycleqos_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsDataReaderLifecycleQos.__init__)
    params = list(sig.parameters.keys())
    assert "enable_invalid_samples" in params, "Missing parameter 'enable_invalid_samples'"
    assert "autopurge_dispose_all" in params, "Missing parameter 'autopurge_dispose_all'"

def test_ddsmetamodel_ddsdatareaderlifecycleqos_has_enable_invalid_samples():
    assert hasattr(ddsMetamodel_DdsDataReaderLifecycleQos, "enable_invalid_samples")
    descriptor = None
    for klass in ddsMetamodel_DdsDataReaderLifecycleQos.__mro__:
        if "enable_invalid_samples" in klass.__dict__:
            descriptor = klass.__dict__["enable_invalid_samples"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel_ddsdatareaderlifecycleqos_has_autopurge_dispose_all():
    assert hasattr(ddsMetamodel_DdsDataReaderLifecycleQos, "autopurge_dispose_all")
    descriptor = None
    for klass in ddsMetamodel_DdsDataReaderLifecycleQos.__mro__:
        if "autopurge_dispose_all" in klass.__dict__:
            descriptor = klass.__dict__["autopurge_dispose_all"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddspresentationqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsPresentationQos)


def test_ddsmetamodel_ddspresentationqos_constructor_exists():
    assert callable(ddsMetamodel_DdsPresentationQos.__init__)


def test_ddsmetamodel_ddspresentationqos_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsPresentationQos.__init__)
    params = list(sig.parameters.keys())
    assert "coherent_access" in params, "Missing parameter 'coherent_access'"
    assert "access_scope" in params, "Missing parameter 'access_scope'"
    assert "ordered_access" in params, "Missing parameter 'ordered_access'"

def test_ddsmetamodel_ddspresentationqos_has_coherent_access():
    assert hasattr(ddsMetamodel_DdsPresentationQos, "coherent_access")
    descriptor = None
    for klass in ddsMetamodel_DdsPresentationQos.__mro__:
        if "coherent_access" in klass.__dict__:
            descriptor = klass.__dict__["coherent_access"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel_ddspresentationqos_has_access_scope():
    assert hasattr(ddsMetamodel_DdsPresentationQos, "access_scope")
    descriptor = None
    for klass in ddsMetamodel_DdsPresentationQos.__mro__:
        if "access_scope" in klass.__dict__:
            descriptor = klass.__dict__["access_scope"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel_ddspresentationqos_has_ordered_access():
    assert hasattr(ddsMetamodel_DdsPresentationQos, "ordered_access")
    descriptor = None
    for klass in ddsMetamodel_DdsPresentationQos.__mro__:
        if "ordered_access" in klass.__dict__:
            descriptor = klass.__dict__["ordered_access"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddsduration_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsDuration)


def test_ddsmetamodel_ddsduration_constructor_exists():
    assert callable(ddsMetamodel_DdsDuration.__init__)


def test_ddsmetamodel_ddsduration_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsDuration.__init__)
    params = list(sig.parameters.keys())
    assert "nanoSec" in params, "Missing parameter 'nanoSec'"
    assert "sec" in params, "Missing parameter 'sec'"

def test_ddsmetamodel_ddsduration_has_nanoSec():
    assert hasattr(ddsMetamodel_DdsDuration, "nanoSec")
    descriptor = None
    for klass in ddsMetamodel_DdsDuration.__mro__:
        if "nanoSec" in klass.__dict__:
            descriptor = klass.__dict__["nanoSec"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel_ddsduration_has_sec():
    assert hasattr(ddsMetamodel_DdsDuration, "sec")
    descriptor = None
    for klass in ddsMetamodel_DdsDuration.__mro__:
        if "sec" in klass.__dict__:
            descriptor = klass.__dict__["sec"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddsownershipstrengthqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsOwnershipStrengthQos)


def test_ddsmetamodel_ddsownershipstrengthqos_constructor_exists():
    assert callable(ddsMetamodel_DdsOwnershipStrengthQos.__init__)


def test_ddsmetamodel_ddsownershipstrengthqos_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsOwnershipStrengthQos.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ddsmetamodel_ddsownershipstrengthqos_has_value():
    assert hasattr(ddsMetamodel_DdsOwnershipStrengthQos, "value")
    descriptor = None
    for klass in ddsMetamodel_DdsOwnershipStrengthQos.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddsdestinationorderqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsDestinationOrderQos)


def test_ddsmetamodel_ddsdestinationorderqos_constructor_exists():
    assert callable(ddsMetamodel_DdsDestinationOrderQos.__init__)


def test_ddsmetamodel_ddsdestinationorderqos_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsDestinationOrderQos.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_ddsmetamodel_ddsdestinationorderqos_has_kind():
    assert hasattr(ddsMetamodel_DdsDestinationOrderQos, "kind")
    descriptor = None
    for klass in ddsMetamodel_DdsDestinationOrderQos.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddsreliabilityqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsReliabilityQos)


def test_ddsmetamodel_ddsreliabilityqos_constructor_exists():
    assert callable(ddsMetamodel_DdsReliabilityQos.__init__)


def test_ddsmetamodel_ddsreliabilityqos_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsReliabilityQos.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_ddsmetamodel_ddsreliabilityqos_has_kind():
    assert hasattr(ddsMetamodel_DdsReliabilityQos, "kind")
    descriptor = None
    for klass in ddsMetamodel_DdsReliabilityQos.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddsownershipqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsOwnershipQos)


def test_ddsmetamodel_ddsownershipqos_constructor_exists():
    assert callable(ddsMetamodel_DdsOwnershipQos.__init__)


def test_ddsmetamodel_ddsownershipqos_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsOwnershipQos.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_ddsmetamodel_ddsownershipqos_has_kind():
    assert hasattr(ddsMetamodel_DdsOwnershipQos, "kind")
    descriptor = None
    for klass in ddsMetamodel_DdsOwnershipQos.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddslivelinessqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsLivelinessQos)


def test_ddsmetamodel_ddslivelinessqos_constructor_exists():
    assert callable(ddsMetamodel_DdsLivelinessQos.__init__)


def test_ddsmetamodel_ddslivelinessqos_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsLivelinessQos.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_ddsmetamodel_ddslivelinessqos_has_kind():
    assert hasattr(ddsMetamodel_DdsLivelinessQos, "kind")
    descriptor = None
    for klass in ddsMetamodel_DdsLivelinessQos.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddslatencybudgetqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsLatencyBudgetQos)


def test_ddsmetamodel_ddslatencybudgetqos_constructor_exists():
    assert callable(ddsMetamodel_DdsLatencyBudgetQos.__init__)


def test_ddsmetamodel_ddslatencybudgetqos_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsLatencyBudgetQos.__init__)
    params = list(sig.parameters.keys())



def test_ddsmetamodel_ddsdurabilityserviceqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsDurabilityServiceQos)


def test_ddsmetamodel_ddsdurabilityserviceqos_constructor_exists():
    assert callable(ddsMetamodel_DdsDurabilityServiceQos.__init__)


def test_ddsmetamodel_ddsdurabilityserviceqos_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsDurabilityServiceQos.__init__)
    params = list(sig.parameters.keys())
    assert "history_depth" in params, "Missing parameter 'history_depth'"
    assert "max_samples_per_instances" in params, "Missing parameter 'max_samples_per_instances'"
    assert "history_kind" in params, "Missing parameter 'history_kind'"
    assert "max_instances" in params, "Missing parameter 'max_instances'"
    assert "max_samples" in params, "Missing parameter 'max_samples'"

def test_ddsmetamodel_ddsdurabilityserviceqos_has_history_depth():
    assert hasattr(ddsMetamodel_DdsDurabilityServiceQos, "history_depth")
    descriptor = None
    for klass in ddsMetamodel_DdsDurabilityServiceQos.__mro__:
        if "history_depth" in klass.__dict__:
            descriptor = klass.__dict__["history_depth"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel_ddsdurabilityserviceqos_has_max_samples_per_instances():
    assert hasattr(ddsMetamodel_DdsDurabilityServiceQos, "max_samples_per_instances")
    descriptor = None
    for klass in ddsMetamodel_DdsDurabilityServiceQos.__mro__:
        if "max_samples_per_instances" in klass.__dict__:
            descriptor = klass.__dict__["max_samples_per_instances"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel_ddsdurabilityserviceqos_has_history_kind():
    assert hasattr(ddsMetamodel_DdsDurabilityServiceQos, "history_kind")
    descriptor = None
    for klass in ddsMetamodel_DdsDurabilityServiceQos.__mro__:
        if "history_kind" in klass.__dict__:
            descriptor = klass.__dict__["history_kind"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel_ddsdurabilityserviceqos_has_max_instances():
    assert hasattr(ddsMetamodel_DdsDurabilityServiceQos, "max_instances")
    descriptor = None
    for klass in ddsMetamodel_DdsDurabilityServiceQos.__mro__:
        if "max_instances" in klass.__dict__:
            descriptor = klass.__dict__["max_instances"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel_ddsdurabilityserviceqos_has_max_samples():
    assert hasattr(ddsMetamodel_DdsDurabilityServiceQos, "max_samples")
    descriptor = None
    for klass in ddsMetamodel_DdsDurabilityServiceQos.__mro__:
        if "max_samples" in klass.__dict__:
            descriptor = klass.__dict__["max_samples"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddsdurabilityqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsDurabilityQos)


def test_ddsmetamodel_ddsdurabilityqos_constructor_exists():
    assert callable(ddsMetamodel_DdsDurabilityQos.__init__)


def test_ddsmetamodel_ddsdurabilityqos_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsDurabilityQos.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_ddsmetamodel_ddsdurabilityqos_has_kind():
    assert hasattr(ddsMetamodel_DdsDurabilityQos, "kind")
    descriptor = None
    for klass in ddsMetamodel_DdsDurabilityQos.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddstopicdataqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsTopicDataQos)


def test_ddsmetamodel_ddstopicdataqos_constructor_exists():
    assert callable(ddsMetamodel_DdsTopicDataQos.__init__)


def test_ddsmetamodel_ddstopicdataqos_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsTopicDataQos.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ddsmetamodel_ddstopicdataqos_has_value():
    assert hasattr(ddsMetamodel_DdsTopicDataQos, "value")
    descriptor = None
    for klass in ddsMetamodel_DdsTopicDataQos.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddsentityfactoryqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsEntityFactoryQos)


def test_ddsmetamodel_ddsentityfactoryqos_constructor_exists():
    assert callable(ddsMetamodel_DdsEntityFactoryQos.__init__)


def test_ddsmetamodel_ddsentityfactoryqos_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsEntityFactoryQos.__init__)
    params = list(sig.parameters.keys())
    assert "autoenable_created_entities" in params, "Missing parameter 'autoenable_created_entities'"

def test_ddsmetamodel_ddsentityfactoryqos_has_autoenable_created_entities():
    assert hasattr(ddsMetamodel_DdsEntityFactoryQos, "autoenable_created_entities")
    descriptor = None
    for klass in ddsMetamodel_DdsEntityFactoryQos.__mro__:
        if "autoenable_created_entities" in klass.__dict__:
            descriptor = klass.__dict__["autoenable_created_entities"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel_ddsuserdataqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsUserDataQos)


def test_ddsmetamodel_ddsuserdataqos_constructor_exists():
    assert callable(ddsMetamodel_DdsUserDataQos.__init__)


def test_ddsmetamodel_ddsuserdataqos_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsUserDataQos.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ddsmetamodel_ddsuserdataqos_has_value():
    assert hasattr(ddsMetamodel_DdsUserDataQos, "value")
    descriptor = None
    for klass in ddsMetamodel_DdsUserDataQos.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ddsqosprofile_is_not_abstract():
    assert not inspect.isabstract(DdsQosProfile)


def test_ddsqosprofile_constructor_exists():
    assert callable(DdsQosProfile.__init__)


def test_ddsqosprofile_constructor_args():
    sig = inspect.signature(DdsQosProfile.__init__)
    params = list(sig.parameters.keys())



def test_ddsmetamodel_ddsdomainparticipantqosprofile_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsDomainParticipantQosProfile)


def test_ddsmetamodel_ddsdomainparticipantqosprofile_constructor_exists():
    assert callable(ddsMetamodel_DdsDomainParticipantQosProfile.__init__)


def test_ddsmetamodel_ddsdomainparticipantqosprofile_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsDomainParticipantQosProfile.__init__)
    params = list(sig.parameters.keys())



def test_ddsmetamodel_ddspublisherqosprofile_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsPublisherQosProfile)


def test_ddsmetamodel_ddspublisherqosprofile_constructor_exists():
    assert callable(ddsMetamodel_DdsPublisherQosProfile.__init__)


def test_ddsmetamodel_ddspublisherqosprofile_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsPublisherQosProfile.__init__)
    params = list(sig.parameters.keys())



def test_ddsmetamodel_ddssubscriberqosprofile_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsSubscriberQosProfile)


def test_ddsmetamodel_ddssubscriberqosprofile_constructor_exists():
    assert callable(ddsMetamodel_DdsSubscriberQosProfile.__init__)


def test_ddsmetamodel_ddssubscriberqosprofile_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsSubscriberQosProfile.__init__)
    params = list(sig.parameters.keys())



def test_ddsmetamodel_ddsdatareaderqosprofile_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsDataReaderQosProfile)


def test_ddsmetamodel_ddsdatareaderqosprofile_constructor_exists():
    assert callable(ddsMetamodel_DdsDataReaderQosProfile.__init__)


def test_ddsmetamodel_ddsdatareaderqosprofile_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsDataReaderQosProfile.__init__)
    params = list(sig.parameters.keys())



def test_ddsmetamodel_ddsdatawriterqosprofile_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsDataWriterQosProfile)


def test_ddsmetamodel_ddsdatawriterqosprofile_constructor_exists():
    assert callable(ddsMetamodel_DdsDataWriterQosProfile.__init__)


def test_ddsmetamodel_ddsdatawriterqosprofile_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsDataWriterQosProfile.__init__)
    params = list(sig.parameters.keys())



def test_ddsmetamodel_ddstopicqosprofile_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsTopicQosProfile)


def test_ddsmetamodel_ddstopicqosprofile_constructor_exists():
    assert callable(ddsMetamodel_DdsTopicQosProfile.__init__)


def test_ddsmetamodel_ddstopicqosprofile_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsTopicQosProfile.__init__)
    params = list(sig.parameters.keys())



def test_ddsmetamodel_ddsdeadlineqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel_DdsDeadlineQos)


def test_ddsmetamodel_ddsdeadlineqos_constructor_exists():
    assert callable(ddsMetamodel_DdsDeadlineQos.__init__)


def test_ddsmetamodel_ddsdeadlineqos_constructor_args():
    sig = inspect.signature(ddsMetamodel_DdsDeadlineQos.__init__)
    params = list(sig.parameters.keys())

def test_datareaderstatus_exists():
    # Check that the Enumeration exists
    assert DataReaderStatus is not None

def test_datareaderstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataReaderStatus]
    expected_literals = [
        "SUBSCRIPTION_MATCHED_STATUS",
        "DATA_AVAILABLE_STATUS",
        "SAMPLE_REJECTED_STATUS",
        "LIVELINESS_CHANGED_STATUS",
        "REQUESTED_DEADLINE_MISSED_STATUS",
        "SAMPLE_LOST_STATUS",
        "REQUESTED_INCOMPATIBLE_QOS_STATUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataReaderStatus"

def test_destinationorderqospolicykind_exists():
    # Check that the Enumeration exists
    assert DestinationOrderQosPolicyKind is not None

def test_destinationorderqospolicykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DestinationOrderQosPolicyKind]
    expected_literals = [
        "BY_RECEPTION_TIMESTAMP_DESTINATIONORDER_QOS",
        "BY_SOURCE_TIMESTAMP_DESTINATIONORDER_QOS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DestinationOrderQosPolicyKind"

def test_samplestatekind_exists():
    # Check that the Enumeration exists
    assert SampleStateKind is not None

def test_samplestatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SampleStateKind]
    expected_literals = [
        "READ_SAMPLE_STATE",
        "ANY_READ_SAMPLE_STATE",
        "NOT_READ_SAMPLE_STATE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SampleStateKind"

def test_subscriberstatus_exists():
    # Check that the Enumeration exists
    assert SubscriberStatus is not None

def test_subscriberstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SubscriberStatus]
    expected_literals = [
        "SAMPLE_REJECTED_STATUS",
        "REQUESTED_DEADLINE_MISSED_STATUS",
        "LIVELINESS_CHANGED_STATUS",
        "DATA_ON_READERS_STATUS",
        "DATA_AVAILABLE_STATUS",
        "REQUESTED_INCOMPATIBLE_QOS_STATUS",
        "SAMPLE_LOST_STATUS",
        "SUBSCRIPTION_MATCHED_STATUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SubscriberStatus"

def test_viewstatekind_exists():
    # Check that the Enumeration exists
    assert ViewStateKind is not None

def test_viewstatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ViewStateKind]
    expected_literals = [
        "NOT_NEW_VIEW_STATE",
        "ANY_VIEW_STATE",
        "NEW_VIEW_STATE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ViewStateKind"

def test_reliabilityqospolicykind_exists():
    # Check that the Enumeration exists
    assert ReliabilityQosPolicyKind is not None

def test_reliabilityqospolicykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReliabilityQosPolicyKind]
    expected_literals = [
        "BEST_EFFORT_RELIABILITY_QOS",
        "RELIABLE_RELIABILITY_QOS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReliabilityQosPolicyKind"

def test_ownershipqospolicykind_exists():
    # Check that the Enumeration exists
    assert OwnershipQosPolicyKind is not None

def test_ownershipqospolicykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OwnershipQosPolicyKind]
    expected_literals = [
        "SHARED_OWNERSHIP_QOS",
        "EXCLUSIVE_OWNERSHIP_QOS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OwnershipQosPolicyKind"

def test_domainparticipantstatus_exists():
    # Check that the Enumeration exists
    assert DomainParticipantStatus is not None

def test_domainparticipantstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DomainParticipantStatus]
    expected_literals = [
        "SAMPLE_REJECTED_STATUS",
        "PUBLICATION_MATCHED_STATUS",
        "REQUESTED_DEADLINE_MISSED_STATUS",
        "OFFERED_INCOMPATIBLE_QOS_STATUS",
        "REQUESTED_INCOMPATIBLE_QOS_STATUS",
        "DATA_ON_READERS_STATUS",
        "OFFERED_DEADLINE_MISSED_STATUS",
        "LIVELINESS_CHANGED_STATUS",
        "INCONSISTENT_TOPIC_STATUS",
        "SUBSCRIPTION_MATCHED_STATUS",
        "DATA_AVAILABLE_STATUS",
        "LIVELINESS_LOST_STATUS",
        "SAMPLE_LOST_STATUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DomainParticipantStatus"

def test_datawriterstatus_exists():
    # Check that the Enumeration exists
    assert DataWriterStatus is not None

def test_datawriterstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataWriterStatus]
    expected_literals = [
        "OFFERED_DEADLINE_MISSED_STATUS",
        "OFFERED_INCOMPATIBLE_QOS_STATUS",
        "LIVELINESS_LOST_STATUS",
        "PUBLICATION_MATCHED_STATUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataWriterStatus"

def test_livelinessqospolicykind_exists():
    # Check that the Enumeration exists
    assert LivelinessQosPolicyKind is not None

def test_livelinessqospolicykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LivelinessQosPolicyKind]
    expected_literals = [
        "MANUAL_BY_TOPIC_LIVELINESS_QOS",
        "AUTOMATIC_LIVELINESS_QOS",
        "MANUAL_LIVELINESS_QOS",
        "MANUAL_BY_PARTICIPANT_LIVELINESS_QOS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LivelinessQosPolicyKind"

def test_durabilityqospolicykind_exists():
    # Check that the Enumeration exists
    assert DurabilityQosPolicyKind is not None

def test_durabilityqospolicykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DurabilityQosPolicyKind]
    expected_literals = [
        "VOLATILE_DURABILITY_QOS",
        "TRANSIENT_LOCAL_DURABILITY_QOS",
        "PERSISTENT_DURABILITY_QOS",
        "TRANSIENT_DURABILITY_QOS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DurabilityQosPolicyKind"

def test_invalidsamplevisibilityqospolicy_exists():
    # Check that the Enumeration exists
    assert InvalidSampleVisibilityQosPolicy is not None

def test_invalidsamplevisibilityqospolicy_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InvalidSampleVisibilityQosPolicy]
    expected_literals = [
        "MINIMUM_INVALID_SAMPLES",
        "NO_INVALID_SAMPLES",
        "ALL_INVALID_SAMPLES",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InvalidSampleVisibilityQosPolicy"

def test_topicstatus_exists():
    # Check that the Enumeration exists
    assert TopicStatus is not None

def test_topicstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TopicStatus]
    expected_literals = [
        "INCONSISTENT_TOPIC_STATUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TopicStatus"

def test_historyqospolicykind_exists():
    # Check that the Enumeration exists
    assert HistoryQosPolicyKind is not None

def test_historyqospolicykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HistoryQosPolicyKind]
    expected_literals = [
        "KEEP_LAST_HISTORY_QOS",
        "KEEP_ALL_HISTORY_QOS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HistoryQosPolicyKind"

def test_publisherstatus_exists():
    # Check that the Enumeration exists
    assert PublisherStatus is not None

def test_publisherstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PublisherStatus]
    expected_literals = [
        "OFFERED_DEADLINE_MISSED_STATUS",
        "OFFERED_INCOMPATIBLE_QOS_STATUS",
        "PUBLICATION_MATCHED_STATUS",
        "LIVELINESS_LOST_STATUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PublisherStatus"

def test_instancestatekind_exists():
    # Check that the Enumeration exists
    assert InstanceStateKind is not None

def test_instancestatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InstanceStateKind]
    expected_literals = [
        "NOT_ALIVE_NO_WRITERS_INSTANCE_STATE",
        "ANY_INSTANCE_STATE",
        "ALIVE_INSTANCE_STATE",
        "NOT_ALIVE_DISPOSED_INSTANCE_STATE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InstanceStateKind"

def test_presentationqospolicyaccessscopekind_exists():
    # Check that the Enumeration exists
    assert PresentationQosPolicyAccessScopeKind is not None

def test_presentationqospolicyaccessscopekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PresentationQosPolicyAccessScopeKind]
    expected_literals = [
        "INSTANCE_PRESENTATION_QOS",
        "TOPIC_PRESENTATION_QOS",
        "GROUP_PRESENTATION_QOS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PresentationQosPolicyAccessScopeKind"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
ddsMetamodel_DdsLifespan_strategy = st.builds(
    ddsMetamodel_DdsLifespan,
)
ddsMetamodel_DdsTransportPriorityQos_strategy = st.builds(
    ddsMetamodel_DdsTransportPriorityQos,
    value=
        safe_text
)
ddsMetamodel_DdsResourceLimits_strategy = st.builds(
    ddsMetamodel_DdsResourceLimits,
    max_samples_per_instances=
        safe_text,
    max_instances=
        safe_text,
    max_samples=
        safe_text
)
ddsMetamodel_DdsHistoryQos_strategy = st.builds(
    ddsMetamodel_DdsHistoryQos,
    kind=
        safe_text,
    depth=
        safe_text
)
ddsMetamodel_DdsSystem_strategy = st.builds(
    ddsMetamodel_DdsSystem,
    systemName=
        safe_text
)
ddsMetamodel_DdsDataModule_strategy = st.builds(
    ddsMetamodel_DdsDataModule,
    moduleName=
        safe_text
)
ddsMetamodel_DdsDataWriterListener_strategy = st.builds(
    ddsMetamodel_DdsDataWriterListener,
    name=
        safe_text,
    listenedStatus=
        safe_text
)
ddsMetamodel_DdsPublisherListener_strategy = st.builds(
    ddsMetamodel_DdsPublisherListener,
    name=
        safe_text,
    listenedStatus=
        safe_text
)
ddsMetamodel_DdsDataWriter_strategy = st.builds(
    ddsMetamodel_DdsDataWriter,
    dataWriterName=
        safe_text
)
ddsMetamodel_DdsStructuredField_strategy = st.builds(
    ddsMetamodel_DdsStructuredField,
    fieldName=
        safe_text,
    maxMultiplicity=
        st.integers(),
    isKey=
        st.booleans()
)
ddsMetamodel_DdsDataField_strategy = st.builds(
    ddsMetamodel_DdsDataField,
    maxMultiplicity=
        st.integers(),
    fieldType=
        safe_text,
    fieldName=
        safe_text,
    isKey=
        st.booleans()
)
ddsMetamodel_DdsDataReader_strategy = st.builds(
    ddsMetamodel_DdsDataReader,
    dataReaderName=
        safe_text
)
ddsMetamodel_DdsQosProfile_strategy = st.builds(
    ddsMetamodel_DdsQosProfile,
    profileName=
        safe_text
)
ddsMetamodel_DdsDataStructure_strategy = st.builds(
    ddsMetamodel_DdsDataStructure,
    structureName=
        safe_text
)
ddsMetamodel_DdsTopicListener_strategy = st.builds(
    ddsMetamodel_DdsTopicListener,
    listenedStatus=
        safe_text,
    name=
        safe_text
)
ddsMetamodel_DdsTopic_strategy = st.builds(
    ddsMetamodel_DdsTopic,
    topicName=
        safe_text
)
ddsMetamodel_DdsDomainParticipantListener_strategy = st.builds(
    ddsMetamodel_DdsDomainParticipantListener,
    name=
        safe_text,
    listenedStatus=
        safe_text
)
ddsMetamodel_DdsPublisher_strategy = st.builds(
    ddsMetamodel_DdsPublisher,
    publisherName=
        safe_text
)
ddsMetamodel_DdsSubscriber_strategy = st.builds(
    ddsMetamodel_DdsSubscriber,
    subscriberName=
        safe_text
)
ddsMetamodel_DdsWaitSet_strategy = st.builds(
    ddsMetamodel_DdsWaitSet,
    name=
        safe_text
)
ddsMetamodel_DdsDomainParticipant_strategy = st.builds(
    ddsMetamodel_DdsDomainParticipant,
    domainParticipantName=
        safe_text,
    domainId=
        st.integers()
)
ddsMetamodel_DdsApplication_strategy = st.builds(
    ddsMetamodel_DdsApplication,
    applicationName=
        safe_text
)
ddsMetamodel_DdsDataReaderListener_strategy = st.builds(
    ddsMetamodel_DdsDataReaderListener,
    name=
        safe_text,
    listenedStatus=
        safe_text
)
ddsMetamodel_DdsSubscriberListener_strategy = st.builds(
    ddsMetamodel_DdsSubscriberListener,
    name=
        safe_text,
    listenedStatus=
        safe_text
)
ddsMetamodel_DdsHost_strategy = st.builds(
    ddsMetamodel_DdsHost,
    hostName=
        safe_text
)
DdsReadCondition_strategy = st.builds(
    DdsReadCondition,
)
ddsMetamodel_QueryCondition_strategy = st.builds(
    ddsMetamodel_QueryCondition,
    query=
        safe_text,
    queryParameters=
        safe_text
)
DdsStatusCondition_strategy = st.builds(
    DdsStatusCondition,
)
ddsMetamodel_DdsPublisherStatusCondition_strategy = st.builds(
    ddsMetamodel_DdsPublisherStatusCondition,
    enabled_status=
        safe_text
)
ddsMetamodel_DdsTopicStatusCondition_strategy = st.builds(
    ddsMetamodel_DdsTopicStatusCondition,
    enabled_status=
        safe_text
)
ddsMetamodel_DdsDataReaderStatusCondition_strategy = st.builds(
    ddsMetamodel_DdsDataReaderStatusCondition,
    enabled_status=
        safe_text
)
ddsMetamodel_DdsDomainParticipantStatusCondition_strategy = st.builds(
    ddsMetamodel_DdsDomainParticipantStatusCondition,
    enabled_status=
        safe_text
)
ddsMetamodel_DdsDataWriterStatusCondition_strategy = st.builds(
    ddsMetamodel_DdsDataWriterStatusCondition,
    enabled_status=
        safe_text
)
ddsMetamodel_DdsSubscriberStatusCondition_strategy = st.builds(
    ddsMetamodel_DdsSubscriberStatusCondition,
    enabled_status=
        safe_text
)
ddsMetamodel_GuardCondition_strategy = st.builds(
    ddsMetamodel_GuardCondition,
    name=
        safe_text
)
ddsMetamodel_DdsStatusCondition_strategy = st.builds(
    ddsMetamodel_DdsStatusCondition,
)
ddsMetamodel_DdsReadCondition_strategy = st.builds(
    ddsMetamodel_DdsReadCondition,
    instance_state_mask=
        safe_text,
    sample_state_mask=
        safe_text,
    view_state_mask=
        safe_text
)
ddsMetamodel_DdsGroupDataQos_strategy = st.builds(
    ddsMetamodel_DdsGroupDataQos,
    value=
        safe_text
)
ddsMetamodel_DdsDataWriterLifecycleQos_strategy = st.builds(
    ddsMetamodel_DdsDataWriterLifecycleQos,
    autodispose_unregistered_instances=
        st.booleans()
)
ddsMetamodel_DdsPartitionQos_strategy = st.builds(
    ddsMetamodel_DdsPartitionQos,
    name=
        safe_text
)
ddsMetamodel_DdsTimeBasedFilterQos_strategy = st.builds(
    ddsMetamodel_DdsTimeBasedFilterQos,
)
ddsMetamodel_DdsDataReaderLifecycleQos_strategy = st.builds(
    ddsMetamodel_DdsDataReaderLifecycleQos,
    enable_invalid_samples=
        st.booleans(),
    autopurge_dispose_all=
        st.booleans()
)
ddsMetamodel_DdsPresentationQos_strategy = st.builds(
    ddsMetamodel_DdsPresentationQos,
    coherent_access=
        st.booleans(),
    access_scope=
        safe_text,
    ordered_access=
        st.booleans()
)
ddsMetamodel_DdsDuration_strategy = st.builds(
    ddsMetamodel_DdsDuration,
    nanoSec=
        safe_text,
    sec=
        safe_text
)
ddsMetamodel_DdsOwnershipStrengthQos_strategy = st.builds(
    ddsMetamodel_DdsOwnershipStrengthQos,
    value=
        safe_text
)
ddsMetamodel_DdsDestinationOrderQos_strategy = st.builds(
    ddsMetamodel_DdsDestinationOrderQos,
    kind=
        safe_text
)
ddsMetamodel_DdsReliabilityQos_strategy = st.builds(
    ddsMetamodel_DdsReliabilityQos,
    kind=
        safe_text
)
ddsMetamodel_DdsOwnershipQos_strategy = st.builds(
    ddsMetamodel_DdsOwnershipQos,
    kind=
        safe_text
)
ddsMetamodel_DdsLivelinessQos_strategy = st.builds(
    ddsMetamodel_DdsLivelinessQos,
    kind=
        safe_text
)
ddsMetamodel_DdsLatencyBudgetQos_strategy = st.builds(
    ddsMetamodel_DdsLatencyBudgetQos,
)
ddsMetamodel_DdsDurabilityServiceQos_strategy = st.builds(
    ddsMetamodel_DdsDurabilityServiceQos,
    history_depth=
        safe_text,
    max_samples_per_instances=
        safe_text,
    history_kind=
        safe_text,
    max_instances=
        safe_text,
    max_samples=
        safe_text
)
ddsMetamodel_DdsDurabilityQos_strategy = st.builds(
    ddsMetamodel_DdsDurabilityQos,
    kind=
        safe_text
)
ddsMetamodel_DdsTopicDataQos_strategy = st.builds(
    ddsMetamodel_DdsTopicDataQos,
    value=
        safe_text
)
ddsMetamodel_DdsEntityFactoryQos_strategy = st.builds(
    ddsMetamodel_DdsEntityFactoryQos,
    autoenable_created_entities=
        st.booleans()
)
ddsMetamodel_DdsUserDataQos_strategy = st.builds(
    ddsMetamodel_DdsUserDataQos,
    value=
        safe_text
)
DdsQosProfile_strategy = st.builds(
    DdsQosProfile,
)
ddsMetamodel_DdsDomainParticipantQosProfile_strategy = st.builds(
    ddsMetamodel_DdsDomainParticipantQosProfile,
)
ddsMetamodel_DdsPublisherQosProfile_strategy = st.builds(
    ddsMetamodel_DdsPublisherQosProfile,
)
ddsMetamodel_DdsSubscriberQosProfile_strategy = st.builds(
    ddsMetamodel_DdsSubscriberQosProfile,
)
ddsMetamodel_DdsDataReaderQosProfile_strategy = st.builds(
    ddsMetamodel_DdsDataReaderQosProfile,
)
ddsMetamodel_DdsDataWriterQosProfile_strategy = st.builds(
    ddsMetamodel_DdsDataWriterQosProfile,
)
ddsMetamodel_DdsTopicQosProfile_strategy = st.builds(
    ddsMetamodel_DdsTopicQosProfile,
)
ddsMetamodel_DdsDeadlineQos_strategy = st.builds(
    ddsMetamodel_DdsDeadlineQos,
)

@given(instance=ddsMetamodel_DdsLifespan_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddslifespan_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsLifespan)

@given(instance=ddsMetamodel_DdsTransportPriorityQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddstransportpriorityqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsTransportPriorityQos)



@given(instance=ddsMetamodel_DdsTransportPriorityQos_strategy)
def test_ddsmetamodel_ddstransportpriorityqos_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ddsMetamodel_DdsResourceLimits_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsresourcelimits_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsResourceLimits)



@given(instance=ddsMetamodel_DdsResourceLimits_strategy)
def test_ddsmetamodel_ddsresourcelimits_max_samples_per_instances_setter(instance):
    original = instance.max_samples_per_instances
    instance.max_samples_per_instances = original
    assert instance.max_samples_per_instances == original



@given(instance=ddsMetamodel_DdsResourceLimits_strategy)
def test_ddsmetamodel_ddsresourcelimits_max_instances_setter(instance):
    original = instance.max_instances
    instance.max_instances = original
    assert instance.max_instances == original



@given(instance=ddsMetamodel_DdsResourceLimits_strategy)
def test_ddsmetamodel_ddsresourcelimits_max_samples_setter(instance):
    original = instance.max_samples
    instance.max_samples = original
    assert instance.max_samples == original

@given(instance=ddsMetamodel_DdsHistoryQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddshistoryqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsHistoryQos)



@given(instance=ddsMetamodel_DdsHistoryQos_strategy)
def test_ddsmetamodel_ddshistoryqos_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=ddsMetamodel_DdsHistoryQos_strategy)
def test_ddsmetamodel_ddshistoryqos_depth_setter(instance):
    original = instance.depth
    instance.depth = original
    assert instance.depth == original

@given(instance=ddsMetamodel_DdsSystem_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddssystem_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsSystem)



@given(instance=ddsMetamodel_DdsSystem_strategy)
def test_ddsmetamodel_ddssystem_systemName_setter(instance):
    original = instance.systemName
    instance.systemName = original
    assert instance.systemName == original

@given(instance=ddsMetamodel_DdsDataModule_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsdatamodule_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsDataModule)



@given(instance=ddsMetamodel_DdsDataModule_strategy)
def test_ddsmetamodel_ddsdatamodule_moduleName_setter(instance):
    original = instance.moduleName
    instance.moduleName = original
    assert instance.moduleName == original

@given(instance=ddsMetamodel_DdsDataWriterListener_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsdatawriterlistener_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsDataWriterListener)



@given(instance=ddsMetamodel_DdsDataWriterListener_strategy)
def test_ddsmetamodel_ddsdatawriterlistener_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ddsMetamodel_DdsDataWriterListener_strategy)
def test_ddsmetamodel_ddsdatawriterlistener_listenedStatus_setter(instance):
    original = instance.listenedStatus
    instance.listenedStatus = original
    assert instance.listenedStatus == original

@given(instance=ddsMetamodel_DdsPublisherListener_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddspublisherlistener_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsPublisherListener)



@given(instance=ddsMetamodel_DdsPublisherListener_strategy)
def test_ddsmetamodel_ddspublisherlistener_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ddsMetamodel_DdsPublisherListener_strategy)
def test_ddsmetamodel_ddspublisherlistener_listenedStatus_setter(instance):
    original = instance.listenedStatus
    instance.listenedStatus = original
    assert instance.listenedStatus == original

@given(instance=ddsMetamodel_DdsDataWriter_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsdatawriter_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsDataWriter)



@given(instance=ddsMetamodel_DdsDataWriter_strategy)
def test_ddsmetamodel_ddsdatawriter_dataWriterName_setter(instance):
    original = instance.dataWriterName
    instance.dataWriterName = original
    assert instance.dataWriterName == original

@given(instance=ddsMetamodel_DdsStructuredField_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsstructuredfield_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsStructuredField)



@given(instance=ddsMetamodel_DdsStructuredField_strategy)
def test_ddsmetamodel_ddsstructuredfield_fieldName_setter(instance):
    original = instance.fieldName
    instance.fieldName = original
    assert instance.fieldName == original



@given(instance=ddsMetamodel_DdsStructuredField_strategy)
def test_ddsmetamodel_ddsstructuredfield_maxMultiplicity_setter(instance):
    original = instance.maxMultiplicity
    instance.maxMultiplicity = original
    assert instance.maxMultiplicity == original



@given(instance=ddsMetamodel_DdsStructuredField_strategy)
def test_ddsmetamodel_ddsstructuredfield_isKey_setter(instance):
    original = instance.isKey
    instance.isKey = original
    assert instance.isKey == original

@given(instance=ddsMetamodel_DdsDataField_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsdatafield_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsDataField)



@given(instance=ddsMetamodel_DdsDataField_strategy)
def test_ddsmetamodel_ddsdatafield_maxMultiplicity_setter(instance):
    original = instance.maxMultiplicity
    instance.maxMultiplicity = original
    assert instance.maxMultiplicity == original



@given(instance=ddsMetamodel_DdsDataField_strategy)
def test_ddsmetamodel_ddsdatafield_fieldType_setter(instance):
    original = instance.fieldType
    instance.fieldType = original
    assert instance.fieldType == original



@given(instance=ddsMetamodel_DdsDataField_strategy)
def test_ddsmetamodel_ddsdatafield_fieldName_setter(instance):
    original = instance.fieldName
    instance.fieldName = original
    assert instance.fieldName == original



@given(instance=ddsMetamodel_DdsDataField_strategy)
def test_ddsmetamodel_ddsdatafield_isKey_setter(instance):
    original = instance.isKey
    instance.isKey = original
    assert instance.isKey == original

@given(instance=ddsMetamodel_DdsDataReader_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsdatareader_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsDataReader)



@given(instance=ddsMetamodel_DdsDataReader_strategy)
def test_ddsmetamodel_ddsdatareader_dataReaderName_setter(instance):
    original = instance.dataReaderName
    instance.dataReaderName = original
    assert instance.dataReaderName == original

@given(instance=ddsMetamodel_DdsQosProfile_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsqosprofile_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsQosProfile)



@given(instance=ddsMetamodel_DdsQosProfile_strategy)
def test_ddsmetamodel_ddsqosprofile_profileName_setter(instance):
    original = instance.profileName
    instance.profileName = original
    assert instance.profileName == original

@given(instance=ddsMetamodel_DdsDataStructure_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsdatastructure_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsDataStructure)



@given(instance=ddsMetamodel_DdsDataStructure_strategy)
def test_ddsmetamodel_ddsdatastructure_structureName_setter(instance):
    original = instance.structureName
    instance.structureName = original
    assert instance.structureName == original

@given(instance=ddsMetamodel_DdsTopicListener_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddstopiclistener_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsTopicListener)



@given(instance=ddsMetamodel_DdsTopicListener_strategy)
def test_ddsmetamodel_ddstopiclistener_listenedStatus_setter(instance):
    original = instance.listenedStatus
    instance.listenedStatus = original
    assert instance.listenedStatus == original



@given(instance=ddsMetamodel_DdsTopicListener_strategy)
def test_ddsmetamodel_ddstopiclistener_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ddsMetamodel_DdsTopic_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddstopic_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsTopic)



@given(instance=ddsMetamodel_DdsTopic_strategy)
def test_ddsmetamodel_ddstopic_topicName_setter(instance):
    original = instance.topicName
    instance.topicName = original
    assert instance.topicName == original

@given(instance=ddsMetamodel_DdsDomainParticipantListener_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsdomainparticipantlistener_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsDomainParticipantListener)



@given(instance=ddsMetamodel_DdsDomainParticipantListener_strategy)
def test_ddsmetamodel_ddsdomainparticipantlistener_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ddsMetamodel_DdsDomainParticipantListener_strategy)
def test_ddsmetamodel_ddsdomainparticipantlistener_listenedStatus_setter(instance):
    original = instance.listenedStatus
    instance.listenedStatus = original
    assert instance.listenedStatus == original

@given(instance=ddsMetamodel_DdsPublisher_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddspublisher_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsPublisher)



@given(instance=ddsMetamodel_DdsPublisher_strategy)
def test_ddsmetamodel_ddspublisher_publisherName_setter(instance):
    original = instance.publisherName
    instance.publisherName = original
    assert instance.publisherName == original

@given(instance=ddsMetamodel_DdsSubscriber_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddssubscriber_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsSubscriber)



@given(instance=ddsMetamodel_DdsSubscriber_strategy)
def test_ddsmetamodel_ddssubscriber_subscriberName_setter(instance):
    original = instance.subscriberName
    instance.subscriberName = original
    assert instance.subscriberName == original

@given(instance=ddsMetamodel_DdsWaitSet_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddswaitset_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsWaitSet)



@given(instance=ddsMetamodel_DdsWaitSet_strategy)
def test_ddsmetamodel_ddswaitset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ddsMetamodel_DdsDomainParticipant_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsdomainparticipant_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsDomainParticipant)



@given(instance=ddsMetamodel_DdsDomainParticipant_strategy)
def test_ddsmetamodel_ddsdomainparticipant_domainParticipantName_setter(instance):
    original = instance.domainParticipantName
    instance.domainParticipantName = original
    assert instance.domainParticipantName == original



@given(instance=ddsMetamodel_DdsDomainParticipant_strategy)
def test_ddsmetamodel_ddsdomainparticipant_domainId_setter(instance):
    original = instance.domainId
    instance.domainId = original
    assert instance.domainId == original

@given(instance=ddsMetamodel_DdsApplication_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsapplication_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsApplication)



@given(instance=ddsMetamodel_DdsApplication_strategy)
def test_ddsmetamodel_ddsapplication_applicationName_setter(instance):
    original = instance.applicationName
    instance.applicationName = original
    assert instance.applicationName == original

@given(instance=ddsMetamodel_DdsDataReaderListener_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsdatareaderlistener_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsDataReaderListener)



@given(instance=ddsMetamodel_DdsDataReaderListener_strategy)
def test_ddsmetamodel_ddsdatareaderlistener_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ddsMetamodel_DdsDataReaderListener_strategy)
def test_ddsmetamodel_ddsdatareaderlistener_listenedStatus_setter(instance):
    original = instance.listenedStatus
    instance.listenedStatus = original
    assert instance.listenedStatus == original

@given(instance=ddsMetamodel_DdsSubscriberListener_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddssubscriberlistener_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsSubscriberListener)



@given(instance=ddsMetamodel_DdsSubscriberListener_strategy)
def test_ddsmetamodel_ddssubscriberlistener_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ddsMetamodel_DdsSubscriberListener_strategy)
def test_ddsmetamodel_ddssubscriberlistener_listenedStatus_setter(instance):
    original = instance.listenedStatus
    instance.listenedStatus = original
    assert instance.listenedStatus == original

@given(instance=ddsMetamodel_DdsHost_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddshost_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsHost)



@given(instance=ddsMetamodel_DdsHost_strategy)
def test_ddsmetamodel_ddshost_hostName_setter(instance):
    original = instance.hostName
    instance.hostName = original
    assert instance.hostName == original

@given(instance=DdsReadCondition_strategy)
@settings(max_examples=50)
def test_ddsreadcondition_instantiation(instance):
    assert isinstance(instance, DdsReadCondition)

@given(instance=ddsMetamodel_QueryCondition_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_querycondition_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_QueryCondition)



@given(instance=ddsMetamodel_QueryCondition_strategy)
def test_ddsmetamodel_querycondition_query_setter(instance):
    original = instance.query
    instance.query = original
    assert instance.query == original



@given(instance=ddsMetamodel_QueryCondition_strategy)
def test_ddsmetamodel_querycondition_queryParameters_setter(instance):
    original = instance.queryParameters
    instance.queryParameters = original
    assert instance.queryParameters == original

@given(instance=DdsStatusCondition_strategy)
@settings(max_examples=50)
def test_ddsstatuscondition_instantiation(instance):
    assert isinstance(instance, DdsStatusCondition)

@given(instance=ddsMetamodel_DdsPublisherStatusCondition_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddspublisherstatuscondition_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsPublisherStatusCondition)



@given(instance=ddsMetamodel_DdsPublisherStatusCondition_strategy)
def test_ddsmetamodel_ddspublisherstatuscondition_enabled_status_setter(instance):
    original = instance.enabled_status
    instance.enabled_status = original
    assert instance.enabled_status == original

@given(instance=ddsMetamodel_DdsTopicStatusCondition_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddstopicstatuscondition_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsTopicStatusCondition)



@given(instance=ddsMetamodel_DdsTopicStatusCondition_strategy)
def test_ddsmetamodel_ddstopicstatuscondition_enabled_status_setter(instance):
    original = instance.enabled_status
    instance.enabled_status = original
    assert instance.enabled_status == original

@given(instance=ddsMetamodel_DdsDataReaderStatusCondition_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsdatareaderstatuscondition_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsDataReaderStatusCondition)



@given(instance=ddsMetamodel_DdsDataReaderStatusCondition_strategy)
def test_ddsmetamodel_ddsdatareaderstatuscondition_enabled_status_setter(instance):
    original = instance.enabled_status
    instance.enabled_status = original
    assert instance.enabled_status == original

@given(instance=ddsMetamodel_DdsDomainParticipantStatusCondition_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsdomainparticipantstatuscondition_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsDomainParticipantStatusCondition)



@given(instance=ddsMetamodel_DdsDomainParticipantStatusCondition_strategy)
def test_ddsmetamodel_ddsdomainparticipantstatuscondition_enabled_status_setter(instance):
    original = instance.enabled_status
    instance.enabled_status = original
    assert instance.enabled_status == original

@given(instance=ddsMetamodel_DdsDataWriterStatusCondition_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsdatawriterstatuscondition_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsDataWriterStatusCondition)



@given(instance=ddsMetamodel_DdsDataWriterStatusCondition_strategy)
def test_ddsmetamodel_ddsdatawriterstatuscondition_enabled_status_setter(instance):
    original = instance.enabled_status
    instance.enabled_status = original
    assert instance.enabled_status == original

@given(instance=ddsMetamodel_DdsSubscriberStatusCondition_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddssubscriberstatuscondition_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsSubscriberStatusCondition)



@given(instance=ddsMetamodel_DdsSubscriberStatusCondition_strategy)
def test_ddsmetamodel_ddssubscriberstatuscondition_enabled_status_setter(instance):
    original = instance.enabled_status
    instance.enabled_status = original
    assert instance.enabled_status == original

@given(instance=ddsMetamodel_GuardCondition_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_guardcondition_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_GuardCondition)



@given(instance=ddsMetamodel_GuardCondition_strategy)
def test_ddsmetamodel_guardcondition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ddsMetamodel_DdsStatusCondition_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsstatuscondition_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsStatusCondition)

@given(instance=ddsMetamodel_DdsReadCondition_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsreadcondition_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsReadCondition)



@given(instance=ddsMetamodel_DdsReadCondition_strategy)
def test_ddsmetamodel_ddsreadcondition_instance_state_mask_setter(instance):
    original = instance.instance_state_mask
    instance.instance_state_mask = original
    assert instance.instance_state_mask == original



@given(instance=ddsMetamodel_DdsReadCondition_strategy)
def test_ddsmetamodel_ddsreadcondition_sample_state_mask_setter(instance):
    original = instance.sample_state_mask
    instance.sample_state_mask = original
    assert instance.sample_state_mask == original



@given(instance=ddsMetamodel_DdsReadCondition_strategy)
def test_ddsmetamodel_ddsreadcondition_view_state_mask_setter(instance):
    original = instance.view_state_mask
    instance.view_state_mask = original
    assert instance.view_state_mask == original

@given(instance=ddsMetamodel_DdsGroupDataQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsgroupdataqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsGroupDataQos)



@given(instance=ddsMetamodel_DdsGroupDataQos_strategy)
def test_ddsmetamodel_ddsgroupdataqos_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ddsMetamodel_DdsDataWriterLifecycleQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsdatawriterlifecycleqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsDataWriterLifecycleQos)



@given(instance=ddsMetamodel_DdsDataWriterLifecycleQos_strategy)
def test_ddsmetamodel_ddsdatawriterlifecycleqos_autodispose_unregistered_instances_setter(instance):
    original = instance.autodispose_unregistered_instances
    instance.autodispose_unregistered_instances = original
    assert instance.autodispose_unregistered_instances == original

@given(instance=ddsMetamodel_DdsPartitionQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddspartitionqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsPartitionQos)



@given(instance=ddsMetamodel_DdsPartitionQos_strategy)
def test_ddsmetamodel_ddspartitionqos_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ddsMetamodel_DdsTimeBasedFilterQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddstimebasedfilterqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsTimeBasedFilterQos)

@given(instance=ddsMetamodel_DdsDataReaderLifecycleQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsdatareaderlifecycleqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsDataReaderLifecycleQos)



@given(instance=ddsMetamodel_DdsDataReaderLifecycleQos_strategy)
def test_ddsmetamodel_ddsdatareaderlifecycleqos_enable_invalid_samples_setter(instance):
    original = instance.enable_invalid_samples
    instance.enable_invalid_samples = original
    assert instance.enable_invalid_samples == original



@given(instance=ddsMetamodel_DdsDataReaderLifecycleQos_strategy)
def test_ddsmetamodel_ddsdatareaderlifecycleqos_autopurge_dispose_all_setter(instance):
    original = instance.autopurge_dispose_all
    instance.autopurge_dispose_all = original
    assert instance.autopurge_dispose_all == original

@given(instance=ddsMetamodel_DdsPresentationQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddspresentationqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsPresentationQos)



@given(instance=ddsMetamodel_DdsPresentationQos_strategy)
def test_ddsmetamodel_ddspresentationqos_coherent_access_setter(instance):
    original = instance.coherent_access
    instance.coherent_access = original
    assert instance.coherent_access == original



@given(instance=ddsMetamodel_DdsPresentationQos_strategy)
def test_ddsmetamodel_ddspresentationqos_access_scope_setter(instance):
    original = instance.access_scope
    instance.access_scope = original
    assert instance.access_scope == original



@given(instance=ddsMetamodel_DdsPresentationQos_strategy)
def test_ddsmetamodel_ddspresentationqos_ordered_access_setter(instance):
    original = instance.ordered_access
    instance.ordered_access = original
    assert instance.ordered_access == original

@given(instance=ddsMetamodel_DdsDuration_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsduration_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsDuration)



@given(instance=ddsMetamodel_DdsDuration_strategy)
def test_ddsmetamodel_ddsduration_nanoSec_setter(instance):
    original = instance.nanoSec
    instance.nanoSec = original
    assert instance.nanoSec == original



@given(instance=ddsMetamodel_DdsDuration_strategy)
def test_ddsmetamodel_ddsduration_sec_setter(instance):
    original = instance.sec
    instance.sec = original
    assert instance.sec == original

@given(instance=ddsMetamodel_DdsOwnershipStrengthQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsownershipstrengthqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsOwnershipStrengthQos)



@given(instance=ddsMetamodel_DdsOwnershipStrengthQos_strategy)
def test_ddsmetamodel_ddsownershipstrengthqos_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ddsMetamodel_DdsDestinationOrderQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsdestinationorderqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsDestinationOrderQos)



@given(instance=ddsMetamodel_DdsDestinationOrderQos_strategy)
def test_ddsmetamodel_ddsdestinationorderqos_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=ddsMetamodel_DdsReliabilityQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsreliabilityqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsReliabilityQos)



@given(instance=ddsMetamodel_DdsReliabilityQos_strategy)
def test_ddsmetamodel_ddsreliabilityqos_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=ddsMetamodel_DdsOwnershipQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsownershipqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsOwnershipQos)



@given(instance=ddsMetamodel_DdsOwnershipQos_strategy)
def test_ddsmetamodel_ddsownershipqos_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=ddsMetamodel_DdsLivelinessQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddslivelinessqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsLivelinessQos)



@given(instance=ddsMetamodel_DdsLivelinessQos_strategy)
def test_ddsmetamodel_ddslivelinessqos_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=ddsMetamodel_DdsLatencyBudgetQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddslatencybudgetqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsLatencyBudgetQos)

@given(instance=ddsMetamodel_DdsDurabilityServiceQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsdurabilityserviceqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsDurabilityServiceQos)



@given(instance=ddsMetamodel_DdsDurabilityServiceQos_strategy)
def test_ddsmetamodel_ddsdurabilityserviceqos_history_depth_setter(instance):
    original = instance.history_depth
    instance.history_depth = original
    assert instance.history_depth == original



@given(instance=ddsMetamodel_DdsDurabilityServiceQos_strategy)
def test_ddsmetamodel_ddsdurabilityserviceqos_max_samples_per_instances_setter(instance):
    original = instance.max_samples_per_instances
    instance.max_samples_per_instances = original
    assert instance.max_samples_per_instances == original



@given(instance=ddsMetamodel_DdsDurabilityServiceQos_strategy)
def test_ddsmetamodel_ddsdurabilityserviceqos_history_kind_setter(instance):
    original = instance.history_kind
    instance.history_kind = original
    assert instance.history_kind == original



@given(instance=ddsMetamodel_DdsDurabilityServiceQos_strategy)
def test_ddsmetamodel_ddsdurabilityserviceqos_max_instances_setter(instance):
    original = instance.max_instances
    instance.max_instances = original
    assert instance.max_instances == original



@given(instance=ddsMetamodel_DdsDurabilityServiceQos_strategy)
def test_ddsmetamodel_ddsdurabilityserviceqos_max_samples_setter(instance):
    original = instance.max_samples
    instance.max_samples = original
    assert instance.max_samples == original

@given(instance=ddsMetamodel_DdsDurabilityQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsdurabilityqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsDurabilityQos)



@given(instance=ddsMetamodel_DdsDurabilityQos_strategy)
def test_ddsmetamodel_ddsdurabilityqos_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=ddsMetamodel_DdsTopicDataQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddstopicdataqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsTopicDataQos)



@given(instance=ddsMetamodel_DdsTopicDataQos_strategy)
def test_ddsmetamodel_ddstopicdataqos_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ddsMetamodel_DdsEntityFactoryQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsentityfactoryqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsEntityFactoryQos)



@given(instance=ddsMetamodel_DdsEntityFactoryQos_strategy)
def test_ddsmetamodel_ddsentityfactoryqos_autoenable_created_entities_setter(instance):
    original = instance.autoenable_created_entities
    instance.autoenable_created_entities = original
    assert instance.autoenable_created_entities == original

@given(instance=ddsMetamodel_DdsUserDataQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsuserdataqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsUserDataQos)



@given(instance=ddsMetamodel_DdsUserDataQos_strategy)
def test_ddsmetamodel_ddsuserdataqos_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=DdsQosProfile_strategy)
@settings(max_examples=50)
def test_ddsqosprofile_instantiation(instance):
    assert isinstance(instance, DdsQosProfile)

@given(instance=ddsMetamodel_DdsDomainParticipantQosProfile_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsdomainparticipantqosprofile_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsDomainParticipantQosProfile)

@given(instance=ddsMetamodel_DdsPublisherQosProfile_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddspublisherqosprofile_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsPublisherQosProfile)

@given(instance=ddsMetamodel_DdsSubscriberQosProfile_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddssubscriberqosprofile_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsSubscriberQosProfile)

@given(instance=ddsMetamodel_DdsDataReaderQosProfile_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsdatareaderqosprofile_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsDataReaderQosProfile)

@given(instance=ddsMetamodel_DdsDataWriterQosProfile_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsdatawriterqosprofile_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsDataWriterQosProfile)

@given(instance=ddsMetamodel_DdsTopicQosProfile_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddstopicqosprofile_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsTopicQosProfile)

@given(instance=ddsMetamodel_DdsDeadlineQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel_ddsdeadlineqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel_DdsDeadlineQos)
