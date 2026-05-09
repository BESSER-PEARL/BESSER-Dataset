import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ddsMetamodel::DdsHost,
    DdsReadCondition,
    ddsMetamodel::QueryCondition,
    DdsStatusCondition,
    ddsMetamodel::DdsDataReaderStatusCondition,
    ddsMetamodel::DdsPublisherStatusCondition,
    ddsMetamodel::DdsTopicStatusCondition,
    ddsMetamodel::DdsDomainParticipantStatusCondition,
    ddsMetamodel::DdsDataWriterStatusCondition,
    ddsMetamodel::DdsSubscriberStatusCondition,
    ddsMetamodel::GuardCondition,
    ddsMetamodel::DdsStatusCondition,
    ddsMetamodel::DdsReadCondition,
    ddsMetamodel::DdsGroupDataQos,
    ddsMetamodel::DdsDataWriterLifecycleQos,
    ddsMetamodel::DdsPartitionQos,
    ddsMetamodel::DdsTimeBasedFilterQos,
    ddsMetamodel::DdsDataReaderLifecycleQos,
    ddsMetamodel::DdsPresentationQos,
    ddsMetamodel::DdsDuration,
    ddsMetamodel::DdsOwnershipStrengthQos,
    ddsMetamodel::DdsDestinationOrderQos,
    ddsMetamodel::DdsReliabilityQos,
    ddsMetamodel::DdsOwnershipQos,
    ddsMetamodel::DdsLivelinessQos,
    ddsMetamodel::DdsLatencyBudgetQos,
    ddsMetamodel::DdsDurabilityServiceQos,
    ddsMetamodel::DdsDurabilityQos,
    ddsMetamodel::DdsTopicDataQos,
    ddsMetamodel::DdsEntityFactoryQos,
    ddsMetamodel::DdsUserDataQos,
    DdsQosProfile,
    ddsMetamodel::DdsDeadlineQos,
    ddsMetamodel::DdsLifespan,
    ddsMetamodel::DdsTransportPriorityQos,
    ddsMetamodel::DdsResourceLimits,
    ddsMetamodel::DdsHistoryQos,
    ddsMetamodel::DdsSystem,
    ddsMetamodel::DdsDataModule,
    ddsMetamodel::DdsDataWriterQosProfile,
    ddsMetamodel::DdsDataWriterListener,
    ddsMetamodel::DdsPublisherQosProfile,
    ddsMetamodel::DdsPublisherListener,
    ddsMetamodel::DdsDataWriter,
    ddsMetamodel::DdsDataReaderQosProfile,
    ddsMetamodel::DdsStructuredField,
    ddsMetamodel::DdsDataField,
    ddsMetamodel::DdsDataReader,
    ddsMetamodel::DdsQosProfile,
    ddsMetamodel::DdsDataStructure,
    ddsMetamodel::DdsTopicQosProfile,
    ddsMetamodel::DdsTopicListener,
    ddsMetamodel::DdsTopic,
    ddsMetamodel::DdsDomainParticipantListener,
    ddsMetamodel::DdsDomainParticipantQosProfile,
    ddsMetamodel::DdsPublisher,
    ddsMetamodel::DdsSubscriber,
    ddsMetamodel::DdsWaitSet,
    ddsMetamodel::DdsDomainParticipant,
    ddsMetamodel::DdsApplication,
    ddsMetamodel::DdsDataReaderListener,
    ddsMetamodel::DdsSubscriberQosProfile,
    ddsMetamodel::DdsSubscriberListener,
    TopicStatus,
    DurabilityQosPolicyKind,
    SampleStateKind,
    OwnershipQosPolicyKind,
    DestinationOrderQosPolicyKind,
    ReliabilityQosPolicyKind,
    DataWriterStatus,
    InstanceStateKind,
    DomainParticipantStatus,
    DataReaderStatus,
    HistoryQosPolicyKind,
    InvalidSampleVisibilityQosPolicy,
    SubscriberStatus,
    PresentationQosPolicyAccessScopeKind,
    LivelinessQosPolicyKind,
    PublisherStatus,
    ViewStateKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ddsmetamodel::ddshost_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsHost)


def test_ddsmetamodel::ddshost_constructor_exists():
    assert callable(ddsMetamodel::DdsHost.__init__)


def test_ddsmetamodel::ddshost_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsHost.__init__)
    params = list(sig.parameters.keys())
    assert "hostName" in params, "Missing parameter 'hostName'"

def test_ddsmetamodel::ddshost_has_hostName():
    assert hasattr(ddsMetamodel::DdsHost, "hostName")
    descriptor = None
    for klass in ddsMetamodel::DdsHost.__mro__:
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



def test_ddsmetamodel::querycondition_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::QueryCondition)


def test_ddsmetamodel::querycondition_constructor_exists():
    assert callable(ddsMetamodel::QueryCondition.__init__)


def test_ddsmetamodel::querycondition_constructor_args():
    sig = inspect.signature(ddsMetamodel::QueryCondition.__init__)
    params = list(sig.parameters.keys())
    assert "queryParameters" in params, "Missing parameter 'queryParameters'"
    assert "query" in params, "Missing parameter 'query'"

def test_ddsmetamodel::querycondition_has_queryParameters():
    assert hasattr(ddsMetamodel::QueryCondition, "queryParameters")
    descriptor = None
    for klass in ddsMetamodel::QueryCondition.__mro__:
        if "queryParameters" in klass.__dict__:
            descriptor = klass.__dict__["queryParameters"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel::querycondition_has_query():
    assert hasattr(ddsMetamodel::QueryCondition, "query")
    descriptor = None
    for klass in ddsMetamodel::QueryCondition.__mro__:
        if "query" in klass.__dict__:
            descriptor = klass.__dict__["query"]
            break
    assert isinstance(descriptor, property)



def test_ddsstatuscondition_is_not_abstract():
    assert not inspect.isabstract(DdsStatusCondition)


def test_ddsstatuscondition_constructor_exists():
    assert callable(DdsStatusCondition.__init__)


def test_ddsstatuscondition_constructor_args():
    sig = inspect.signature(DdsStatusCondition.__init__)
    params = list(sig.parameters.keys())



def test_ddsmetamodel::ddsdatareaderstatuscondition_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsDataReaderStatusCondition)


def test_ddsmetamodel::ddsdatareaderstatuscondition_constructor_exists():
    assert callable(ddsMetamodel::DdsDataReaderStatusCondition.__init__)


def test_ddsmetamodel::ddsdatareaderstatuscondition_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsDataReaderStatusCondition.__init__)
    params = list(sig.parameters.keys())
    assert "enabled_status" in params, "Missing parameter 'enabled_status'"

def test_ddsmetamodel::ddsdatareaderstatuscondition_has_enabled_status():
    assert hasattr(ddsMetamodel::DdsDataReaderStatusCondition, "enabled_status")
    descriptor = None
    for klass in ddsMetamodel::DdsDataReaderStatusCondition.__mro__:
        if "enabled_status" in klass.__dict__:
            descriptor = klass.__dict__["enabled_status"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddspublisherstatuscondition_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsPublisherStatusCondition)


def test_ddsmetamodel::ddspublisherstatuscondition_constructor_exists():
    assert callable(ddsMetamodel::DdsPublisherStatusCondition.__init__)


def test_ddsmetamodel::ddspublisherstatuscondition_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsPublisherStatusCondition.__init__)
    params = list(sig.parameters.keys())
    assert "enabled_status" in params, "Missing parameter 'enabled_status'"

def test_ddsmetamodel::ddspublisherstatuscondition_has_enabled_status():
    assert hasattr(ddsMetamodel::DdsPublisherStatusCondition, "enabled_status")
    descriptor = None
    for klass in ddsMetamodel::DdsPublisherStatusCondition.__mro__:
        if "enabled_status" in klass.__dict__:
            descriptor = klass.__dict__["enabled_status"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddstopicstatuscondition_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsTopicStatusCondition)


def test_ddsmetamodel::ddstopicstatuscondition_constructor_exists():
    assert callable(ddsMetamodel::DdsTopicStatusCondition.__init__)


def test_ddsmetamodel::ddstopicstatuscondition_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsTopicStatusCondition.__init__)
    params = list(sig.parameters.keys())
    assert "enabled_status" in params, "Missing parameter 'enabled_status'"

def test_ddsmetamodel::ddstopicstatuscondition_has_enabled_status():
    assert hasattr(ddsMetamodel::DdsTopicStatusCondition, "enabled_status")
    descriptor = None
    for klass in ddsMetamodel::DdsTopicStatusCondition.__mro__:
        if "enabled_status" in klass.__dict__:
            descriptor = klass.__dict__["enabled_status"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddsdomainparticipantstatuscondition_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsDomainParticipantStatusCondition)


def test_ddsmetamodel::ddsdomainparticipantstatuscondition_constructor_exists():
    assert callable(ddsMetamodel::DdsDomainParticipantStatusCondition.__init__)


def test_ddsmetamodel::ddsdomainparticipantstatuscondition_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsDomainParticipantStatusCondition.__init__)
    params = list(sig.parameters.keys())
    assert "enabled_status" in params, "Missing parameter 'enabled_status'"

def test_ddsmetamodel::ddsdomainparticipantstatuscondition_has_enabled_status():
    assert hasattr(ddsMetamodel::DdsDomainParticipantStatusCondition, "enabled_status")
    descriptor = None
    for klass in ddsMetamodel::DdsDomainParticipantStatusCondition.__mro__:
        if "enabled_status" in klass.__dict__:
            descriptor = klass.__dict__["enabled_status"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddsdatawriterstatuscondition_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsDataWriterStatusCondition)


def test_ddsmetamodel::ddsdatawriterstatuscondition_constructor_exists():
    assert callable(ddsMetamodel::DdsDataWriterStatusCondition.__init__)


def test_ddsmetamodel::ddsdatawriterstatuscondition_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsDataWriterStatusCondition.__init__)
    params = list(sig.parameters.keys())
    assert "enabled_status" in params, "Missing parameter 'enabled_status'"

def test_ddsmetamodel::ddsdatawriterstatuscondition_has_enabled_status():
    assert hasattr(ddsMetamodel::DdsDataWriterStatusCondition, "enabled_status")
    descriptor = None
    for klass in ddsMetamodel::DdsDataWriterStatusCondition.__mro__:
        if "enabled_status" in klass.__dict__:
            descriptor = klass.__dict__["enabled_status"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddssubscriberstatuscondition_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsSubscriberStatusCondition)


def test_ddsmetamodel::ddssubscriberstatuscondition_constructor_exists():
    assert callable(ddsMetamodel::DdsSubscriberStatusCondition.__init__)


def test_ddsmetamodel::ddssubscriberstatuscondition_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsSubscriberStatusCondition.__init__)
    params = list(sig.parameters.keys())
    assert "enabled_status" in params, "Missing parameter 'enabled_status'"

def test_ddsmetamodel::ddssubscriberstatuscondition_has_enabled_status():
    assert hasattr(ddsMetamodel::DdsSubscriberStatusCondition, "enabled_status")
    descriptor = None
    for klass in ddsMetamodel::DdsSubscriberStatusCondition.__mro__:
        if "enabled_status" in klass.__dict__:
            descriptor = klass.__dict__["enabled_status"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::guardcondition_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::GuardCondition)


def test_ddsmetamodel::guardcondition_constructor_exists():
    assert callable(ddsMetamodel::GuardCondition.__init__)


def test_ddsmetamodel::guardcondition_constructor_args():
    sig = inspect.signature(ddsMetamodel::GuardCondition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ddsmetamodel::guardcondition_has_name():
    assert hasattr(ddsMetamodel::GuardCondition, "name")
    descriptor = None
    for klass in ddsMetamodel::GuardCondition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddsstatuscondition_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsStatusCondition)


def test_ddsmetamodel::ddsstatuscondition_constructor_exists():
    assert callable(ddsMetamodel::DdsStatusCondition.__init__)


def test_ddsmetamodel::ddsstatuscondition_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsStatusCondition.__init__)
    params = list(sig.parameters.keys())



def test_ddsmetamodel::ddsreadcondition_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsReadCondition)


def test_ddsmetamodel::ddsreadcondition_constructor_exists():
    assert callable(ddsMetamodel::DdsReadCondition.__init__)


def test_ddsmetamodel::ddsreadcondition_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsReadCondition.__init__)
    params = list(sig.parameters.keys())
    assert "sample_state_mask" in params, "Missing parameter 'sample_state_mask'"
    assert "view_state_mask" in params, "Missing parameter 'view_state_mask'"
    assert "instance_state_mask" in params, "Missing parameter 'instance_state_mask'"

def test_ddsmetamodel::ddsreadcondition_has_sample_state_mask():
    assert hasattr(ddsMetamodel::DdsReadCondition, "sample_state_mask")
    descriptor = None
    for klass in ddsMetamodel::DdsReadCondition.__mro__:
        if "sample_state_mask" in klass.__dict__:
            descriptor = klass.__dict__["sample_state_mask"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel::ddsreadcondition_has_view_state_mask():
    assert hasattr(ddsMetamodel::DdsReadCondition, "view_state_mask")
    descriptor = None
    for klass in ddsMetamodel::DdsReadCondition.__mro__:
        if "view_state_mask" in klass.__dict__:
            descriptor = klass.__dict__["view_state_mask"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel::ddsreadcondition_has_instance_state_mask():
    assert hasattr(ddsMetamodel::DdsReadCondition, "instance_state_mask")
    descriptor = None
    for klass in ddsMetamodel::DdsReadCondition.__mro__:
        if "instance_state_mask" in klass.__dict__:
            descriptor = klass.__dict__["instance_state_mask"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddsgroupdataqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsGroupDataQos)


def test_ddsmetamodel::ddsgroupdataqos_constructor_exists():
    assert callable(ddsMetamodel::DdsGroupDataQos.__init__)


def test_ddsmetamodel::ddsgroupdataqos_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsGroupDataQos.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ddsmetamodel::ddsgroupdataqos_has_value():
    assert hasattr(ddsMetamodel::DdsGroupDataQos, "value")
    descriptor = None
    for klass in ddsMetamodel::DdsGroupDataQos.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddsdatawriterlifecycleqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsDataWriterLifecycleQos)


def test_ddsmetamodel::ddsdatawriterlifecycleqos_constructor_exists():
    assert callable(ddsMetamodel::DdsDataWriterLifecycleQos.__init__)


def test_ddsmetamodel::ddsdatawriterlifecycleqos_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsDataWriterLifecycleQos.__init__)
    params = list(sig.parameters.keys())
    assert "autodispose_unregistered_instances" in params, "Missing parameter 'autodispose_unregistered_instances'"

def test_ddsmetamodel::ddsdatawriterlifecycleqos_has_autodispose_unregistered_instances():
    assert hasattr(ddsMetamodel::DdsDataWriterLifecycleQos, "autodispose_unregistered_instances")
    descriptor = None
    for klass in ddsMetamodel::DdsDataWriterLifecycleQos.__mro__:
        if "autodispose_unregistered_instances" in klass.__dict__:
            descriptor = klass.__dict__["autodispose_unregistered_instances"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddspartitionqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsPartitionQos)


def test_ddsmetamodel::ddspartitionqos_constructor_exists():
    assert callable(ddsMetamodel::DdsPartitionQos.__init__)


def test_ddsmetamodel::ddspartitionqos_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsPartitionQos.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ddsmetamodel::ddspartitionqos_has_name():
    assert hasattr(ddsMetamodel::DdsPartitionQos, "name")
    descriptor = None
    for klass in ddsMetamodel::DdsPartitionQos.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddstimebasedfilterqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsTimeBasedFilterQos)


def test_ddsmetamodel::ddstimebasedfilterqos_constructor_exists():
    assert callable(ddsMetamodel::DdsTimeBasedFilterQos.__init__)


def test_ddsmetamodel::ddstimebasedfilterqos_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsTimeBasedFilterQos.__init__)
    params = list(sig.parameters.keys())



def test_ddsmetamodel::ddsdatareaderlifecycleqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsDataReaderLifecycleQos)


def test_ddsmetamodel::ddsdatareaderlifecycleqos_constructor_exists():
    assert callable(ddsMetamodel::DdsDataReaderLifecycleQos.__init__)


def test_ddsmetamodel::ddsdatareaderlifecycleqos_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsDataReaderLifecycleQos.__init__)
    params = list(sig.parameters.keys())
    assert "enable_invalid_samples" in params, "Missing parameter 'enable_invalid_samples'"
    assert "autopurge_dispose_all" in params, "Missing parameter 'autopurge_dispose_all'"

def test_ddsmetamodel::ddsdatareaderlifecycleqos_has_enable_invalid_samples():
    assert hasattr(ddsMetamodel::DdsDataReaderLifecycleQos, "enable_invalid_samples")
    descriptor = None
    for klass in ddsMetamodel::DdsDataReaderLifecycleQos.__mro__:
        if "enable_invalid_samples" in klass.__dict__:
            descriptor = klass.__dict__["enable_invalid_samples"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel::ddsdatareaderlifecycleqos_has_autopurge_dispose_all():
    assert hasattr(ddsMetamodel::DdsDataReaderLifecycleQos, "autopurge_dispose_all")
    descriptor = None
    for klass in ddsMetamodel::DdsDataReaderLifecycleQos.__mro__:
        if "autopurge_dispose_all" in klass.__dict__:
            descriptor = klass.__dict__["autopurge_dispose_all"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddspresentationqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsPresentationQos)


def test_ddsmetamodel::ddspresentationqos_constructor_exists():
    assert callable(ddsMetamodel::DdsPresentationQos.__init__)


def test_ddsmetamodel::ddspresentationqos_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsPresentationQos.__init__)
    params = list(sig.parameters.keys())
    assert "ordered_access" in params, "Missing parameter 'ordered_access'"
    assert "coherent_access" in params, "Missing parameter 'coherent_access'"
    assert "access_scope" in params, "Missing parameter 'access_scope'"

def test_ddsmetamodel::ddspresentationqos_has_ordered_access():
    assert hasattr(ddsMetamodel::DdsPresentationQos, "ordered_access")
    descriptor = None
    for klass in ddsMetamodel::DdsPresentationQos.__mro__:
        if "ordered_access" in klass.__dict__:
            descriptor = klass.__dict__["ordered_access"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel::ddspresentationqos_has_coherent_access():
    assert hasattr(ddsMetamodel::DdsPresentationQos, "coherent_access")
    descriptor = None
    for klass in ddsMetamodel::DdsPresentationQos.__mro__:
        if "coherent_access" in klass.__dict__:
            descriptor = klass.__dict__["coherent_access"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel::ddspresentationqos_has_access_scope():
    assert hasattr(ddsMetamodel::DdsPresentationQos, "access_scope")
    descriptor = None
    for klass in ddsMetamodel::DdsPresentationQos.__mro__:
        if "access_scope" in klass.__dict__:
            descriptor = klass.__dict__["access_scope"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddsduration_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsDuration)


def test_ddsmetamodel::ddsduration_constructor_exists():
    assert callable(ddsMetamodel::DdsDuration.__init__)


def test_ddsmetamodel::ddsduration_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsDuration.__init__)
    params = list(sig.parameters.keys())
    assert "sec" in params, "Missing parameter 'sec'"
    assert "nanoSec" in params, "Missing parameter 'nanoSec'"

def test_ddsmetamodel::ddsduration_has_sec():
    assert hasattr(ddsMetamodel::DdsDuration, "sec")
    descriptor = None
    for klass in ddsMetamodel::DdsDuration.__mro__:
        if "sec" in klass.__dict__:
            descriptor = klass.__dict__["sec"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel::ddsduration_has_nanoSec():
    assert hasattr(ddsMetamodel::DdsDuration, "nanoSec")
    descriptor = None
    for klass in ddsMetamodel::DdsDuration.__mro__:
        if "nanoSec" in klass.__dict__:
            descriptor = klass.__dict__["nanoSec"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddsownershipstrengthqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsOwnershipStrengthQos)


def test_ddsmetamodel::ddsownershipstrengthqos_constructor_exists():
    assert callable(ddsMetamodel::DdsOwnershipStrengthQos.__init__)


def test_ddsmetamodel::ddsownershipstrengthqos_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsOwnershipStrengthQos.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ddsmetamodel::ddsownershipstrengthqos_has_value():
    assert hasattr(ddsMetamodel::DdsOwnershipStrengthQos, "value")
    descriptor = None
    for klass in ddsMetamodel::DdsOwnershipStrengthQos.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddsdestinationorderqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsDestinationOrderQos)


def test_ddsmetamodel::ddsdestinationorderqos_constructor_exists():
    assert callable(ddsMetamodel::DdsDestinationOrderQos.__init__)


def test_ddsmetamodel::ddsdestinationorderqos_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsDestinationOrderQos.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_ddsmetamodel::ddsdestinationorderqos_has_kind():
    assert hasattr(ddsMetamodel::DdsDestinationOrderQos, "kind")
    descriptor = None
    for klass in ddsMetamodel::DdsDestinationOrderQos.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddsreliabilityqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsReliabilityQos)


def test_ddsmetamodel::ddsreliabilityqos_constructor_exists():
    assert callable(ddsMetamodel::DdsReliabilityQos.__init__)


def test_ddsmetamodel::ddsreliabilityqos_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsReliabilityQos.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_ddsmetamodel::ddsreliabilityqos_has_kind():
    assert hasattr(ddsMetamodel::DdsReliabilityQos, "kind")
    descriptor = None
    for klass in ddsMetamodel::DdsReliabilityQos.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddsownershipqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsOwnershipQos)


def test_ddsmetamodel::ddsownershipqos_constructor_exists():
    assert callable(ddsMetamodel::DdsOwnershipQos.__init__)


def test_ddsmetamodel::ddsownershipqos_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsOwnershipQos.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_ddsmetamodel::ddsownershipqos_has_kind():
    assert hasattr(ddsMetamodel::DdsOwnershipQos, "kind")
    descriptor = None
    for klass in ddsMetamodel::DdsOwnershipQos.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddslivelinessqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsLivelinessQos)


def test_ddsmetamodel::ddslivelinessqos_constructor_exists():
    assert callable(ddsMetamodel::DdsLivelinessQos.__init__)


def test_ddsmetamodel::ddslivelinessqos_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsLivelinessQos.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_ddsmetamodel::ddslivelinessqos_has_kind():
    assert hasattr(ddsMetamodel::DdsLivelinessQos, "kind")
    descriptor = None
    for klass in ddsMetamodel::DdsLivelinessQos.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddslatencybudgetqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsLatencyBudgetQos)


def test_ddsmetamodel::ddslatencybudgetqos_constructor_exists():
    assert callable(ddsMetamodel::DdsLatencyBudgetQos.__init__)


def test_ddsmetamodel::ddslatencybudgetqos_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsLatencyBudgetQos.__init__)
    params = list(sig.parameters.keys())



def test_ddsmetamodel::ddsdurabilityserviceqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsDurabilityServiceQos)


def test_ddsmetamodel::ddsdurabilityserviceqos_constructor_exists():
    assert callable(ddsMetamodel::DdsDurabilityServiceQos.__init__)


def test_ddsmetamodel::ddsdurabilityserviceqos_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsDurabilityServiceQos.__init__)
    params = list(sig.parameters.keys())
    assert "max_samples" in params, "Missing parameter 'max_samples'"
    assert "max_samples_per_instances" in params, "Missing parameter 'max_samples_per_instances'"
    assert "max_instances" in params, "Missing parameter 'max_instances'"
    assert "history_kind" in params, "Missing parameter 'history_kind'"
    assert "history_depth" in params, "Missing parameter 'history_depth'"

def test_ddsmetamodel::ddsdurabilityserviceqos_has_max_samples():
    assert hasattr(ddsMetamodel::DdsDurabilityServiceQos, "max_samples")
    descriptor = None
    for klass in ddsMetamodel::DdsDurabilityServiceQos.__mro__:
        if "max_samples" in klass.__dict__:
            descriptor = klass.__dict__["max_samples"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel::ddsdurabilityserviceqos_has_max_samples_per_instances():
    assert hasattr(ddsMetamodel::DdsDurabilityServiceQos, "max_samples_per_instances")
    descriptor = None
    for klass in ddsMetamodel::DdsDurabilityServiceQos.__mro__:
        if "max_samples_per_instances" in klass.__dict__:
            descriptor = klass.__dict__["max_samples_per_instances"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel::ddsdurabilityserviceqos_has_max_instances():
    assert hasattr(ddsMetamodel::DdsDurabilityServiceQos, "max_instances")
    descriptor = None
    for klass in ddsMetamodel::DdsDurabilityServiceQos.__mro__:
        if "max_instances" in klass.__dict__:
            descriptor = klass.__dict__["max_instances"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel::ddsdurabilityserviceqos_has_history_kind():
    assert hasattr(ddsMetamodel::DdsDurabilityServiceQos, "history_kind")
    descriptor = None
    for klass in ddsMetamodel::DdsDurabilityServiceQos.__mro__:
        if "history_kind" in klass.__dict__:
            descriptor = klass.__dict__["history_kind"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel::ddsdurabilityserviceqos_has_history_depth():
    assert hasattr(ddsMetamodel::DdsDurabilityServiceQos, "history_depth")
    descriptor = None
    for klass in ddsMetamodel::DdsDurabilityServiceQos.__mro__:
        if "history_depth" in klass.__dict__:
            descriptor = klass.__dict__["history_depth"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddsdurabilityqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsDurabilityQos)


def test_ddsmetamodel::ddsdurabilityqos_constructor_exists():
    assert callable(ddsMetamodel::DdsDurabilityQos.__init__)


def test_ddsmetamodel::ddsdurabilityqos_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsDurabilityQos.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_ddsmetamodel::ddsdurabilityqos_has_kind():
    assert hasattr(ddsMetamodel::DdsDurabilityQos, "kind")
    descriptor = None
    for klass in ddsMetamodel::DdsDurabilityQos.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddstopicdataqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsTopicDataQos)


def test_ddsmetamodel::ddstopicdataqos_constructor_exists():
    assert callable(ddsMetamodel::DdsTopicDataQos.__init__)


def test_ddsmetamodel::ddstopicdataqos_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsTopicDataQos.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ddsmetamodel::ddstopicdataqos_has_value():
    assert hasattr(ddsMetamodel::DdsTopicDataQos, "value")
    descriptor = None
    for klass in ddsMetamodel::DdsTopicDataQos.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddsentityfactoryqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsEntityFactoryQos)


def test_ddsmetamodel::ddsentityfactoryqos_constructor_exists():
    assert callable(ddsMetamodel::DdsEntityFactoryQos.__init__)


def test_ddsmetamodel::ddsentityfactoryqos_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsEntityFactoryQos.__init__)
    params = list(sig.parameters.keys())
    assert "autoenable_created_entities" in params, "Missing parameter 'autoenable_created_entities'"

def test_ddsmetamodel::ddsentityfactoryqos_has_autoenable_created_entities():
    assert hasattr(ddsMetamodel::DdsEntityFactoryQos, "autoenable_created_entities")
    descriptor = None
    for klass in ddsMetamodel::DdsEntityFactoryQos.__mro__:
        if "autoenable_created_entities" in klass.__dict__:
            descriptor = klass.__dict__["autoenable_created_entities"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddsuserdataqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsUserDataQos)


def test_ddsmetamodel::ddsuserdataqos_constructor_exists():
    assert callable(ddsMetamodel::DdsUserDataQos.__init__)


def test_ddsmetamodel::ddsuserdataqos_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsUserDataQos.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ddsmetamodel::ddsuserdataqos_has_value():
    assert hasattr(ddsMetamodel::DdsUserDataQos, "value")
    descriptor = None
    for klass in ddsMetamodel::DdsUserDataQos.__mro__:
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



def test_ddsmetamodel::ddsdeadlineqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsDeadlineQos)


def test_ddsmetamodel::ddsdeadlineqos_constructor_exists():
    assert callable(ddsMetamodel::DdsDeadlineQos.__init__)


def test_ddsmetamodel::ddsdeadlineqos_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsDeadlineQos.__init__)
    params = list(sig.parameters.keys())



def test_ddsmetamodel::ddslifespan_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsLifespan)


def test_ddsmetamodel::ddslifespan_constructor_exists():
    assert callable(ddsMetamodel::DdsLifespan.__init__)


def test_ddsmetamodel::ddslifespan_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsLifespan.__init__)
    params = list(sig.parameters.keys())



def test_ddsmetamodel::ddstransportpriorityqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsTransportPriorityQos)


def test_ddsmetamodel::ddstransportpriorityqos_constructor_exists():
    assert callable(ddsMetamodel::DdsTransportPriorityQos.__init__)


def test_ddsmetamodel::ddstransportpriorityqos_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsTransportPriorityQos.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ddsmetamodel::ddstransportpriorityqos_has_value():
    assert hasattr(ddsMetamodel::DdsTransportPriorityQos, "value")
    descriptor = None
    for klass in ddsMetamodel::DdsTransportPriorityQos.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddsresourcelimits_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsResourceLimits)


def test_ddsmetamodel::ddsresourcelimits_constructor_exists():
    assert callable(ddsMetamodel::DdsResourceLimits.__init__)


def test_ddsmetamodel::ddsresourcelimits_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsResourceLimits.__init__)
    params = list(sig.parameters.keys())
    assert "max_instances" in params, "Missing parameter 'max_instances'"
    assert "max_samples" in params, "Missing parameter 'max_samples'"
    assert "max_samples_per_instances" in params, "Missing parameter 'max_samples_per_instances'"

def test_ddsmetamodel::ddsresourcelimits_has_max_instances():
    assert hasattr(ddsMetamodel::DdsResourceLimits, "max_instances")
    descriptor = None
    for klass in ddsMetamodel::DdsResourceLimits.__mro__:
        if "max_instances" in klass.__dict__:
            descriptor = klass.__dict__["max_instances"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel::ddsresourcelimits_has_max_samples():
    assert hasattr(ddsMetamodel::DdsResourceLimits, "max_samples")
    descriptor = None
    for klass in ddsMetamodel::DdsResourceLimits.__mro__:
        if "max_samples" in klass.__dict__:
            descriptor = klass.__dict__["max_samples"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel::ddsresourcelimits_has_max_samples_per_instances():
    assert hasattr(ddsMetamodel::DdsResourceLimits, "max_samples_per_instances")
    descriptor = None
    for klass in ddsMetamodel::DdsResourceLimits.__mro__:
        if "max_samples_per_instances" in klass.__dict__:
            descriptor = klass.__dict__["max_samples_per_instances"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddshistoryqos_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsHistoryQos)


def test_ddsmetamodel::ddshistoryqos_constructor_exists():
    assert callable(ddsMetamodel::DdsHistoryQos.__init__)


def test_ddsmetamodel::ddshistoryqos_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsHistoryQos.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "depth" in params, "Missing parameter 'depth'"

def test_ddsmetamodel::ddshistoryqos_has_kind():
    assert hasattr(ddsMetamodel::DdsHistoryQos, "kind")
    descriptor = None
    for klass in ddsMetamodel::DdsHistoryQos.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel::ddshistoryqos_has_depth():
    assert hasattr(ddsMetamodel::DdsHistoryQos, "depth")
    descriptor = None
    for klass in ddsMetamodel::DdsHistoryQos.__mro__:
        if "depth" in klass.__dict__:
            descriptor = klass.__dict__["depth"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddssystem_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsSystem)


def test_ddsmetamodel::ddssystem_constructor_exists():
    assert callable(ddsMetamodel::DdsSystem.__init__)


def test_ddsmetamodel::ddssystem_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsSystem.__init__)
    params = list(sig.parameters.keys())
    assert "systemName" in params, "Missing parameter 'systemName'"

def test_ddsmetamodel::ddssystem_has_systemName():
    assert hasattr(ddsMetamodel::DdsSystem, "systemName")
    descriptor = None
    for klass in ddsMetamodel::DdsSystem.__mro__:
        if "systemName" in klass.__dict__:
            descriptor = klass.__dict__["systemName"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddsdatamodule_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsDataModule)


def test_ddsmetamodel::ddsdatamodule_constructor_exists():
    assert callable(ddsMetamodel::DdsDataModule.__init__)


def test_ddsmetamodel::ddsdatamodule_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsDataModule.__init__)
    params = list(sig.parameters.keys())
    assert "moduleName" in params, "Missing parameter 'moduleName'"

def test_ddsmetamodel::ddsdatamodule_has_moduleName():
    assert hasattr(ddsMetamodel::DdsDataModule, "moduleName")
    descriptor = None
    for klass in ddsMetamodel::DdsDataModule.__mro__:
        if "moduleName" in klass.__dict__:
            descriptor = klass.__dict__["moduleName"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddsdatawriterqosprofile_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsDataWriterQosProfile)


def test_ddsmetamodel::ddsdatawriterqosprofile_constructor_exists():
    assert callable(ddsMetamodel::DdsDataWriterQosProfile.__init__)


def test_ddsmetamodel::ddsdatawriterqosprofile_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsDataWriterQosProfile.__init__)
    params = list(sig.parameters.keys())



def test_ddsmetamodel::ddsdatawriterlistener_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsDataWriterListener)


def test_ddsmetamodel::ddsdatawriterlistener_constructor_exists():
    assert callable(ddsMetamodel::DdsDataWriterListener.__init__)


def test_ddsmetamodel::ddsdatawriterlistener_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsDataWriterListener.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "listenedStatus" in params, "Missing parameter 'listenedStatus'"

def test_ddsmetamodel::ddsdatawriterlistener_has_name():
    assert hasattr(ddsMetamodel::DdsDataWriterListener, "name")
    descriptor = None
    for klass in ddsMetamodel::DdsDataWriterListener.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel::ddsdatawriterlistener_has_listenedStatus():
    assert hasattr(ddsMetamodel::DdsDataWriterListener, "listenedStatus")
    descriptor = None
    for klass in ddsMetamodel::DdsDataWriterListener.__mro__:
        if "listenedStatus" in klass.__dict__:
            descriptor = klass.__dict__["listenedStatus"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddspublisherqosprofile_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsPublisherQosProfile)


def test_ddsmetamodel::ddspublisherqosprofile_constructor_exists():
    assert callable(ddsMetamodel::DdsPublisherQosProfile.__init__)


def test_ddsmetamodel::ddspublisherqosprofile_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsPublisherQosProfile.__init__)
    params = list(sig.parameters.keys())



def test_ddsmetamodel::ddspublisherlistener_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsPublisherListener)


def test_ddsmetamodel::ddspublisherlistener_constructor_exists():
    assert callable(ddsMetamodel::DdsPublisherListener.__init__)


def test_ddsmetamodel::ddspublisherlistener_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsPublisherListener.__init__)
    params = list(sig.parameters.keys())
    assert "listenedStatus" in params, "Missing parameter 'listenedStatus'"
    assert "name" in params, "Missing parameter 'name'"

def test_ddsmetamodel::ddspublisherlistener_has_listenedStatus():
    assert hasattr(ddsMetamodel::DdsPublisherListener, "listenedStatus")
    descriptor = None
    for klass in ddsMetamodel::DdsPublisherListener.__mro__:
        if "listenedStatus" in klass.__dict__:
            descriptor = klass.__dict__["listenedStatus"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel::ddspublisherlistener_has_name():
    assert hasattr(ddsMetamodel::DdsPublisherListener, "name")
    descriptor = None
    for klass in ddsMetamodel::DdsPublisherListener.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddsdatawriter_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsDataWriter)


def test_ddsmetamodel::ddsdatawriter_constructor_exists():
    assert callable(ddsMetamodel::DdsDataWriter.__init__)


def test_ddsmetamodel::ddsdatawriter_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsDataWriter.__init__)
    params = list(sig.parameters.keys())
    assert "dataWriterName" in params, "Missing parameter 'dataWriterName'"

def test_ddsmetamodel::ddsdatawriter_has_dataWriterName():
    assert hasattr(ddsMetamodel::DdsDataWriter, "dataWriterName")
    descriptor = None
    for klass in ddsMetamodel::DdsDataWriter.__mro__:
        if "dataWriterName" in klass.__dict__:
            descriptor = klass.__dict__["dataWriterName"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddsdatareaderqosprofile_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsDataReaderQosProfile)


def test_ddsmetamodel::ddsdatareaderqosprofile_constructor_exists():
    assert callable(ddsMetamodel::DdsDataReaderQosProfile.__init__)


def test_ddsmetamodel::ddsdatareaderqosprofile_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsDataReaderQosProfile.__init__)
    params = list(sig.parameters.keys())



def test_ddsmetamodel::ddsstructuredfield_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsStructuredField)


def test_ddsmetamodel::ddsstructuredfield_constructor_exists():
    assert callable(ddsMetamodel::DdsStructuredField.__init__)


def test_ddsmetamodel::ddsstructuredfield_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsStructuredField.__init__)
    params = list(sig.parameters.keys())
    assert "isKey" in params, "Missing parameter 'isKey'"
    assert "fieldName" in params, "Missing parameter 'fieldName'"
    assert "maxMultiplicity" in params, "Missing parameter 'maxMultiplicity'"

def test_ddsmetamodel::ddsstructuredfield_has_isKey():
    assert hasattr(ddsMetamodel::DdsStructuredField, "isKey")
    descriptor = None
    for klass in ddsMetamodel::DdsStructuredField.__mro__:
        if "isKey" in klass.__dict__:
            descriptor = klass.__dict__["isKey"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel::ddsstructuredfield_has_fieldName():
    assert hasattr(ddsMetamodel::DdsStructuredField, "fieldName")
    descriptor = None
    for klass in ddsMetamodel::DdsStructuredField.__mro__:
        if "fieldName" in klass.__dict__:
            descriptor = klass.__dict__["fieldName"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel::ddsstructuredfield_has_maxMultiplicity():
    assert hasattr(ddsMetamodel::DdsStructuredField, "maxMultiplicity")
    descriptor = None
    for klass in ddsMetamodel::DdsStructuredField.__mro__:
        if "maxMultiplicity" in klass.__dict__:
            descriptor = klass.__dict__["maxMultiplicity"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddsdatafield_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsDataField)


def test_ddsmetamodel::ddsdatafield_constructor_exists():
    assert callable(ddsMetamodel::DdsDataField.__init__)


def test_ddsmetamodel::ddsdatafield_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsDataField.__init__)
    params = list(sig.parameters.keys())
    assert "fieldType" in params, "Missing parameter 'fieldType'"
    assert "maxMultiplicity" in params, "Missing parameter 'maxMultiplicity'"
    assert "fieldName" in params, "Missing parameter 'fieldName'"
    assert "isKey" in params, "Missing parameter 'isKey'"

def test_ddsmetamodel::ddsdatafield_has_fieldType():
    assert hasattr(ddsMetamodel::DdsDataField, "fieldType")
    descriptor = None
    for klass in ddsMetamodel::DdsDataField.__mro__:
        if "fieldType" in klass.__dict__:
            descriptor = klass.__dict__["fieldType"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel::ddsdatafield_has_maxMultiplicity():
    assert hasattr(ddsMetamodel::DdsDataField, "maxMultiplicity")
    descriptor = None
    for klass in ddsMetamodel::DdsDataField.__mro__:
        if "maxMultiplicity" in klass.__dict__:
            descriptor = klass.__dict__["maxMultiplicity"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel::ddsdatafield_has_fieldName():
    assert hasattr(ddsMetamodel::DdsDataField, "fieldName")
    descriptor = None
    for klass in ddsMetamodel::DdsDataField.__mro__:
        if "fieldName" in klass.__dict__:
            descriptor = klass.__dict__["fieldName"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel::ddsdatafield_has_isKey():
    assert hasattr(ddsMetamodel::DdsDataField, "isKey")
    descriptor = None
    for klass in ddsMetamodel::DdsDataField.__mro__:
        if "isKey" in klass.__dict__:
            descriptor = klass.__dict__["isKey"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddsdatareader_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsDataReader)


def test_ddsmetamodel::ddsdatareader_constructor_exists():
    assert callable(ddsMetamodel::DdsDataReader.__init__)


def test_ddsmetamodel::ddsdatareader_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsDataReader.__init__)
    params = list(sig.parameters.keys())
    assert "dataReaderName" in params, "Missing parameter 'dataReaderName'"

def test_ddsmetamodel::ddsdatareader_has_dataReaderName():
    assert hasattr(ddsMetamodel::DdsDataReader, "dataReaderName")
    descriptor = None
    for klass in ddsMetamodel::DdsDataReader.__mro__:
        if "dataReaderName" in klass.__dict__:
            descriptor = klass.__dict__["dataReaderName"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddsqosprofile_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsQosProfile)


def test_ddsmetamodel::ddsqosprofile_constructor_exists():
    assert callable(ddsMetamodel::DdsQosProfile.__init__)


def test_ddsmetamodel::ddsqosprofile_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsQosProfile.__init__)
    params = list(sig.parameters.keys())
    assert "profileName" in params, "Missing parameter 'profileName'"

def test_ddsmetamodel::ddsqosprofile_has_profileName():
    assert hasattr(ddsMetamodel::DdsQosProfile, "profileName")
    descriptor = None
    for klass in ddsMetamodel::DdsQosProfile.__mro__:
        if "profileName" in klass.__dict__:
            descriptor = klass.__dict__["profileName"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddsdatastructure_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsDataStructure)


def test_ddsmetamodel::ddsdatastructure_constructor_exists():
    assert callable(ddsMetamodel::DdsDataStructure.__init__)


def test_ddsmetamodel::ddsdatastructure_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsDataStructure.__init__)
    params = list(sig.parameters.keys())
    assert "structureName" in params, "Missing parameter 'structureName'"

def test_ddsmetamodel::ddsdatastructure_has_structureName():
    assert hasattr(ddsMetamodel::DdsDataStructure, "structureName")
    descriptor = None
    for klass in ddsMetamodel::DdsDataStructure.__mro__:
        if "structureName" in klass.__dict__:
            descriptor = klass.__dict__["structureName"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddstopicqosprofile_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsTopicQosProfile)


def test_ddsmetamodel::ddstopicqosprofile_constructor_exists():
    assert callable(ddsMetamodel::DdsTopicQosProfile.__init__)


def test_ddsmetamodel::ddstopicqosprofile_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsTopicQosProfile.__init__)
    params = list(sig.parameters.keys())



def test_ddsmetamodel::ddstopiclistener_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsTopicListener)


def test_ddsmetamodel::ddstopiclistener_constructor_exists():
    assert callable(ddsMetamodel::DdsTopicListener.__init__)


def test_ddsmetamodel::ddstopiclistener_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsTopicListener.__init__)
    params = list(sig.parameters.keys())
    assert "listenedStatus" in params, "Missing parameter 'listenedStatus'"
    assert "name" in params, "Missing parameter 'name'"

def test_ddsmetamodel::ddstopiclistener_has_listenedStatus():
    assert hasattr(ddsMetamodel::DdsTopicListener, "listenedStatus")
    descriptor = None
    for klass in ddsMetamodel::DdsTopicListener.__mro__:
        if "listenedStatus" in klass.__dict__:
            descriptor = klass.__dict__["listenedStatus"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel::ddstopiclistener_has_name():
    assert hasattr(ddsMetamodel::DdsTopicListener, "name")
    descriptor = None
    for klass in ddsMetamodel::DdsTopicListener.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddstopic_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsTopic)


def test_ddsmetamodel::ddstopic_constructor_exists():
    assert callable(ddsMetamodel::DdsTopic.__init__)


def test_ddsmetamodel::ddstopic_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsTopic.__init__)
    params = list(sig.parameters.keys())
    assert "topicName" in params, "Missing parameter 'topicName'"

def test_ddsmetamodel::ddstopic_has_topicName():
    assert hasattr(ddsMetamodel::DdsTopic, "topicName")
    descriptor = None
    for klass in ddsMetamodel::DdsTopic.__mro__:
        if "topicName" in klass.__dict__:
            descriptor = klass.__dict__["topicName"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddsdomainparticipantlistener_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsDomainParticipantListener)


def test_ddsmetamodel::ddsdomainparticipantlistener_constructor_exists():
    assert callable(ddsMetamodel::DdsDomainParticipantListener.__init__)


def test_ddsmetamodel::ddsdomainparticipantlistener_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsDomainParticipantListener.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "listenedStatus" in params, "Missing parameter 'listenedStatus'"

def test_ddsmetamodel::ddsdomainparticipantlistener_has_name():
    assert hasattr(ddsMetamodel::DdsDomainParticipantListener, "name")
    descriptor = None
    for klass in ddsMetamodel::DdsDomainParticipantListener.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel::ddsdomainparticipantlistener_has_listenedStatus():
    assert hasattr(ddsMetamodel::DdsDomainParticipantListener, "listenedStatus")
    descriptor = None
    for klass in ddsMetamodel::DdsDomainParticipantListener.__mro__:
        if "listenedStatus" in klass.__dict__:
            descriptor = klass.__dict__["listenedStatus"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddsdomainparticipantqosprofile_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsDomainParticipantQosProfile)


def test_ddsmetamodel::ddsdomainparticipantqosprofile_constructor_exists():
    assert callable(ddsMetamodel::DdsDomainParticipantQosProfile.__init__)


def test_ddsmetamodel::ddsdomainparticipantqosprofile_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsDomainParticipantQosProfile.__init__)
    params = list(sig.parameters.keys())



def test_ddsmetamodel::ddspublisher_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsPublisher)


def test_ddsmetamodel::ddspublisher_constructor_exists():
    assert callable(ddsMetamodel::DdsPublisher.__init__)


def test_ddsmetamodel::ddspublisher_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsPublisher.__init__)
    params = list(sig.parameters.keys())
    assert "publisherName" in params, "Missing parameter 'publisherName'"

def test_ddsmetamodel::ddspublisher_has_publisherName():
    assert hasattr(ddsMetamodel::DdsPublisher, "publisherName")
    descriptor = None
    for klass in ddsMetamodel::DdsPublisher.__mro__:
        if "publisherName" in klass.__dict__:
            descriptor = klass.__dict__["publisherName"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddssubscriber_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsSubscriber)


def test_ddsmetamodel::ddssubscriber_constructor_exists():
    assert callable(ddsMetamodel::DdsSubscriber.__init__)


def test_ddsmetamodel::ddssubscriber_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsSubscriber.__init__)
    params = list(sig.parameters.keys())
    assert "subscriberName" in params, "Missing parameter 'subscriberName'"

def test_ddsmetamodel::ddssubscriber_has_subscriberName():
    assert hasattr(ddsMetamodel::DdsSubscriber, "subscriberName")
    descriptor = None
    for klass in ddsMetamodel::DdsSubscriber.__mro__:
        if "subscriberName" in klass.__dict__:
            descriptor = klass.__dict__["subscriberName"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddswaitset_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsWaitSet)


def test_ddsmetamodel::ddswaitset_constructor_exists():
    assert callable(ddsMetamodel::DdsWaitSet.__init__)


def test_ddsmetamodel::ddswaitset_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsWaitSet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ddsmetamodel::ddswaitset_has_name():
    assert hasattr(ddsMetamodel::DdsWaitSet, "name")
    descriptor = None
    for klass in ddsMetamodel::DdsWaitSet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddsdomainparticipant_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsDomainParticipant)


def test_ddsmetamodel::ddsdomainparticipant_constructor_exists():
    assert callable(ddsMetamodel::DdsDomainParticipant.__init__)


def test_ddsmetamodel::ddsdomainparticipant_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsDomainParticipant.__init__)
    params = list(sig.parameters.keys())
    assert "domainParticipantName" in params, "Missing parameter 'domainParticipantName'"
    assert "domainId" in params, "Missing parameter 'domainId'"

def test_ddsmetamodel::ddsdomainparticipant_has_domainParticipantName():
    assert hasattr(ddsMetamodel::DdsDomainParticipant, "domainParticipantName")
    descriptor = None
    for klass in ddsMetamodel::DdsDomainParticipant.__mro__:
        if "domainParticipantName" in klass.__dict__:
            descriptor = klass.__dict__["domainParticipantName"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel::ddsdomainparticipant_has_domainId():
    assert hasattr(ddsMetamodel::DdsDomainParticipant, "domainId")
    descriptor = None
    for klass in ddsMetamodel::DdsDomainParticipant.__mro__:
        if "domainId" in klass.__dict__:
            descriptor = klass.__dict__["domainId"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddsapplication_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsApplication)


def test_ddsmetamodel::ddsapplication_constructor_exists():
    assert callable(ddsMetamodel::DdsApplication.__init__)


def test_ddsmetamodel::ddsapplication_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsApplication.__init__)
    params = list(sig.parameters.keys())
    assert "applicationName" in params, "Missing parameter 'applicationName'"

def test_ddsmetamodel::ddsapplication_has_applicationName():
    assert hasattr(ddsMetamodel::DdsApplication, "applicationName")
    descriptor = None
    for klass in ddsMetamodel::DdsApplication.__mro__:
        if "applicationName" in klass.__dict__:
            descriptor = klass.__dict__["applicationName"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddsdatareaderlistener_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsDataReaderListener)


def test_ddsmetamodel::ddsdatareaderlistener_constructor_exists():
    assert callable(ddsMetamodel::DdsDataReaderListener.__init__)


def test_ddsmetamodel::ddsdatareaderlistener_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsDataReaderListener.__init__)
    params = list(sig.parameters.keys())
    assert "listenedStatus" in params, "Missing parameter 'listenedStatus'"
    assert "name" in params, "Missing parameter 'name'"

def test_ddsmetamodel::ddsdatareaderlistener_has_listenedStatus():
    assert hasattr(ddsMetamodel::DdsDataReaderListener, "listenedStatus")
    descriptor = None
    for klass in ddsMetamodel::DdsDataReaderListener.__mro__:
        if "listenedStatus" in klass.__dict__:
            descriptor = klass.__dict__["listenedStatus"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel::ddsdatareaderlistener_has_name():
    assert hasattr(ddsMetamodel::DdsDataReaderListener, "name")
    descriptor = None
    for klass in ddsMetamodel::DdsDataReaderListener.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ddsmetamodel::ddssubscriberqosprofile_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsSubscriberQosProfile)


def test_ddsmetamodel::ddssubscriberqosprofile_constructor_exists():
    assert callable(ddsMetamodel::DdsSubscriberQosProfile.__init__)


def test_ddsmetamodel::ddssubscriberqosprofile_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsSubscriberQosProfile.__init__)
    params = list(sig.parameters.keys())



def test_ddsmetamodel::ddssubscriberlistener_is_not_abstract():
    assert not inspect.isabstract(ddsMetamodel::DdsSubscriberListener)


def test_ddsmetamodel::ddssubscriberlistener_constructor_exists():
    assert callable(ddsMetamodel::DdsSubscriberListener.__init__)


def test_ddsmetamodel::ddssubscriberlistener_constructor_args():
    sig = inspect.signature(ddsMetamodel::DdsSubscriberListener.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "listenedStatus" in params, "Missing parameter 'listenedStatus'"

def test_ddsmetamodel::ddssubscriberlistener_has_name():
    assert hasattr(ddsMetamodel::DdsSubscriberListener, "name")
    descriptor = None
    for klass in ddsMetamodel::DdsSubscriberListener.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ddsmetamodel::ddssubscriberlistener_has_listenedStatus():
    assert hasattr(ddsMetamodel::DdsSubscriberListener, "listenedStatus")
    descriptor = None
    for klass in ddsMetamodel::DdsSubscriberListener.__mro__:
        if "listenedStatus" in klass.__dict__:
            descriptor = klass.__dict__["listenedStatus"]
            break
    assert isinstance(descriptor, property)

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

def test_durabilityqospolicykind_exists():
    # Check that the Enumeration exists
    assert DurabilityQosPolicyKind is not None

def test_durabilityqospolicykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DurabilityQosPolicyKind]
    expected_literals = [
        "TRANSIENT_LOCAL_DURABILITY_QOS",
        "PERSISTENT_DURABILITY_QOS",
        "TRANSIENT_DURABILITY_QOS",
        "VOLATILE_DURABILITY_QOS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DurabilityQosPolicyKind"

def test_samplestatekind_exists():
    # Check that the Enumeration exists
    assert SampleStateKind is not None

def test_samplestatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SampleStateKind]
    expected_literals = [
        "ANY_READ_SAMPLE_STATE",
        "NOT_READ_SAMPLE_STATE",
        "READ_SAMPLE_STATE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SampleStateKind"

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

def test_destinationorderqospolicykind_exists():
    # Check that the Enumeration exists
    assert DestinationOrderQosPolicyKind is not None

def test_destinationorderqospolicykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DestinationOrderQosPolicyKind]
    expected_literals = [
        "BY_SOURCE_TIMESTAMP_DESTINATIONORDER_QOS",
        "BY_RECEPTION_TIMESTAMP_DESTINATIONORDER_QOS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DestinationOrderQosPolicyKind"

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

def test_datawriterstatus_exists():
    # Check that the Enumeration exists
    assert DataWriterStatus is not None

def test_datawriterstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataWriterStatus]
    expected_literals = [
        "OFFERED_DEADLINE_MISSED_STATUS",
        "PUBLICATION_MATCHED_STATUS",
        "OFFERED_INCOMPATIBLE_QOS_STATUS",
        "LIVELINESS_LOST_STATUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataWriterStatus"

def test_instancestatekind_exists():
    # Check that the Enumeration exists
    assert InstanceStateKind is not None

def test_instancestatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InstanceStateKind]
    expected_literals = [
        "ALIVE_INSTANCE_STATE",
        "NOT_ALIVE_DISPOSED_INSTANCE_STATE",
        "ANY_INSTANCE_STATE",
        "NOT_ALIVE_NO_WRITERS_INSTANCE_STATE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InstanceStateKind"

def test_domainparticipantstatus_exists():
    # Check that the Enumeration exists
    assert DomainParticipantStatus is not None

def test_domainparticipantstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DomainParticipantStatus]
    expected_literals = [
        "PUBLICATION_MATCHED_STATUS",
        "LIVELINESS_LOST_STATUS",
        "SAMPLE_LOST_STATUS",
        "SAMPLE_REJECTED_STATUS",
        "REQUESTED_INCOMPATIBLE_QOS_STATUS",
        "DATA_ON_READERS_STATUS",
        "OFFERED_DEADLINE_MISSED_STATUS",
        "DATA_AVAILABLE_STATUS",
        "INCONSISTENT_TOPIC_STATUS",
        "REQUESTED_DEADLINE_MISSED_STATUS",
        "SUBSCRIPTION_MATCHED_STATUS",
        "OFFERED_INCOMPATIBLE_QOS_STATUS",
        "LIVELINESS_CHANGED_STATUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DomainParticipantStatus"

def test_datareaderstatus_exists():
    # Check that the Enumeration exists
    assert DataReaderStatus is not None

def test_datareaderstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataReaderStatus]
    expected_literals = [
        "SUBSCRIPTION_MATCHED_STATUS",
        "LIVELINESS_CHANGED_STATUS",
        "REQUESTED_INCOMPATIBLE_QOS_STATUS",
        "REQUESTED_DEADLINE_MISSED_STATUS",
        "SAMPLE_REJECTED_STATUS",
        "SAMPLE_LOST_STATUS",
        "DATA_AVAILABLE_STATUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataReaderStatus"

def test_historyqospolicykind_exists():
    # Check that the Enumeration exists
    assert HistoryQosPolicyKind is not None

def test_historyqospolicykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HistoryQosPolicyKind]
    expected_literals = [
        "KEEP_ALL_HISTORY_QOS",
        "KEEP_LAST_HISTORY_QOS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HistoryQosPolicyKind"

def test_invalidsamplevisibilityqospolicy_exists():
    # Check that the Enumeration exists
    assert InvalidSampleVisibilityQosPolicy is not None

def test_invalidsamplevisibilityqospolicy_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InvalidSampleVisibilityQosPolicy]
    expected_literals = [
        "ALL_INVALID_SAMPLES",
        "NO_INVALID_SAMPLES",
        "MINIMUM_INVALID_SAMPLES",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InvalidSampleVisibilityQosPolicy"

def test_subscriberstatus_exists():
    # Check that the Enumeration exists
    assert SubscriberStatus is not None

def test_subscriberstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SubscriberStatus]
    expected_literals = [
        "SAMPLE_LOST_STATUS",
        "SUBSCRIPTION_MATCHED_STATUS",
        "LIVELINESS_CHANGED_STATUS",
        "REQUESTED_DEADLINE_MISSED_STATUS",
        "REQUESTED_INCOMPATIBLE_QOS_STATUS",
        "DATA_AVAILABLE_STATUS",
        "DATA_ON_READERS_STATUS",
        "SAMPLE_REJECTED_STATUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SubscriberStatus"

def test_presentationqospolicyaccessscopekind_exists():
    # Check that the Enumeration exists
    assert PresentationQosPolicyAccessScopeKind is not None

def test_presentationqospolicyaccessscopekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PresentationQosPolicyAccessScopeKind]
    expected_literals = [
        "GROUP_PRESENTATION_QOS",
        "INSTANCE_PRESENTATION_QOS",
        "TOPIC_PRESENTATION_QOS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PresentationQosPolicyAccessScopeKind"

def test_livelinessqospolicykind_exists():
    # Check that the Enumeration exists
    assert LivelinessQosPolicyKind is not None

def test_livelinessqospolicykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LivelinessQosPolicyKind]
    expected_literals = [
        "MANUAL_BY_TOPIC_LIVELINESS_QOS",
        "MANUAL_LIVELINESS_QOS",
        "MANUAL_BY_PARTICIPANT_LIVELINESS_QOS",
        "AUTOMATIC_LIVELINESS_QOS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LivelinessQosPolicyKind"

def test_publisherstatus_exists():
    # Check that the Enumeration exists
    assert PublisherStatus is not None

def test_publisherstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PublisherStatus]
    expected_literals = [
        "LIVELINESS_LOST_STATUS",
        "OFFERED_DEADLINE_MISSED_STATUS",
        "OFFERED_INCOMPATIBLE_QOS_STATUS",
        "PUBLICATION_MATCHED_STATUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PublisherStatus"

def test_viewstatekind_exists():
    # Check that the Enumeration exists
    assert ViewStateKind is not None

def test_viewstatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ViewStateKind]
    expected_literals = [
        "NEW_VIEW_STATE",
        "NOT_NEW_VIEW_STATE",
        "ANY_VIEW_STATE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ViewStateKind"


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
ddsMetamodel::DdsHost_strategy = st.builds(
    ddsMetamodel::DdsHost,
    hostName=
        safe_text
)
DdsReadCondition_strategy = st.builds(
    DdsReadCondition,
)
ddsMetamodel::QueryCondition_strategy = st.builds(
    ddsMetamodel::QueryCondition,
    queryParameters=
        safe_text,
    query=
        safe_text
)
DdsStatusCondition_strategy = st.builds(
    DdsStatusCondition,
)
ddsMetamodel::DdsDataReaderStatusCondition_strategy = st.builds(
    ddsMetamodel::DdsDataReaderStatusCondition,
    enabled_status=
        safe_text
)
ddsMetamodel::DdsPublisherStatusCondition_strategy = st.builds(
    ddsMetamodel::DdsPublisherStatusCondition,
    enabled_status=
        safe_text
)
ddsMetamodel::DdsTopicStatusCondition_strategy = st.builds(
    ddsMetamodel::DdsTopicStatusCondition,
    enabled_status=
        safe_text
)
ddsMetamodel::DdsDomainParticipantStatusCondition_strategy = st.builds(
    ddsMetamodel::DdsDomainParticipantStatusCondition,
    enabled_status=
        safe_text
)
ddsMetamodel::DdsDataWriterStatusCondition_strategy = st.builds(
    ddsMetamodel::DdsDataWriterStatusCondition,
    enabled_status=
        safe_text
)
ddsMetamodel::DdsSubscriberStatusCondition_strategy = st.builds(
    ddsMetamodel::DdsSubscriberStatusCondition,
    enabled_status=
        safe_text
)
ddsMetamodel::GuardCondition_strategy = st.builds(
    ddsMetamodel::GuardCondition,
    name=
        safe_text
)
ddsMetamodel::DdsStatusCondition_strategy = st.builds(
    ddsMetamodel::DdsStatusCondition,
)
ddsMetamodel::DdsReadCondition_strategy = st.builds(
    ddsMetamodel::DdsReadCondition,
    sample_state_mask=
        safe_text,
    view_state_mask=
        safe_text,
    instance_state_mask=
        safe_text
)
ddsMetamodel::DdsGroupDataQos_strategy = st.builds(
    ddsMetamodel::DdsGroupDataQos,
    value=
        safe_text
)
ddsMetamodel::DdsDataWriterLifecycleQos_strategy = st.builds(
    ddsMetamodel::DdsDataWriterLifecycleQos,
    autodispose_unregistered_instances=
        st.booleans()
)
ddsMetamodel::DdsPartitionQos_strategy = st.builds(
    ddsMetamodel::DdsPartitionQos,
    name=
        safe_text
)
ddsMetamodel::DdsTimeBasedFilterQos_strategy = st.builds(
    ddsMetamodel::DdsTimeBasedFilterQos,
)
ddsMetamodel::DdsDataReaderLifecycleQos_strategy = st.builds(
    ddsMetamodel::DdsDataReaderLifecycleQos,
    enable_invalid_samples=
        st.booleans(),
    autopurge_dispose_all=
        st.booleans()
)
ddsMetamodel::DdsPresentationQos_strategy = st.builds(
    ddsMetamodel::DdsPresentationQos,
    ordered_access=
        st.booleans(),
    coherent_access=
        st.booleans(),
    access_scope=
        safe_text
)
ddsMetamodel::DdsDuration_strategy = st.builds(
    ddsMetamodel::DdsDuration,
    sec=
        safe_text,
    nanoSec=
        safe_text
)
ddsMetamodel::DdsOwnershipStrengthQos_strategy = st.builds(
    ddsMetamodel::DdsOwnershipStrengthQos,
    value=
        safe_text
)
ddsMetamodel::DdsDestinationOrderQos_strategy = st.builds(
    ddsMetamodel::DdsDestinationOrderQos,
    kind=
        safe_text
)
ddsMetamodel::DdsReliabilityQos_strategy = st.builds(
    ddsMetamodel::DdsReliabilityQos,
    kind=
        safe_text
)
ddsMetamodel::DdsOwnershipQos_strategy = st.builds(
    ddsMetamodel::DdsOwnershipQos,
    kind=
        safe_text
)
ddsMetamodel::DdsLivelinessQos_strategy = st.builds(
    ddsMetamodel::DdsLivelinessQos,
    kind=
        safe_text
)
ddsMetamodel::DdsLatencyBudgetQos_strategy = st.builds(
    ddsMetamodel::DdsLatencyBudgetQos,
)
ddsMetamodel::DdsDurabilityServiceQos_strategy = st.builds(
    ddsMetamodel::DdsDurabilityServiceQos,
    max_samples=
        safe_text,
    max_samples_per_instances=
        safe_text,
    max_instances=
        safe_text,
    history_kind=
        safe_text,
    history_depth=
        safe_text
)
ddsMetamodel::DdsDurabilityQos_strategy = st.builds(
    ddsMetamodel::DdsDurabilityQos,
    kind=
        safe_text
)
ddsMetamodel::DdsTopicDataQos_strategy = st.builds(
    ddsMetamodel::DdsTopicDataQos,
    value=
        safe_text
)
ddsMetamodel::DdsEntityFactoryQos_strategy = st.builds(
    ddsMetamodel::DdsEntityFactoryQos,
    autoenable_created_entities=
        st.booleans()
)
ddsMetamodel::DdsUserDataQos_strategy = st.builds(
    ddsMetamodel::DdsUserDataQos,
    value=
        safe_text
)
DdsQosProfile_strategy = st.builds(
    DdsQosProfile,
)
ddsMetamodel::DdsDeadlineQos_strategy = st.builds(
    ddsMetamodel::DdsDeadlineQos,
)
ddsMetamodel::DdsLifespan_strategy = st.builds(
    ddsMetamodel::DdsLifespan,
)
ddsMetamodel::DdsTransportPriorityQos_strategy = st.builds(
    ddsMetamodel::DdsTransportPriorityQos,
    value=
        safe_text
)
ddsMetamodel::DdsResourceLimits_strategy = st.builds(
    ddsMetamodel::DdsResourceLimits,
    max_instances=
        safe_text,
    max_samples=
        safe_text,
    max_samples_per_instances=
        safe_text
)
ddsMetamodel::DdsHistoryQos_strategy = st.builds(
    ddsMetamodel::DdsHistoryQos,
    kind=
        safe_text,
    depth=
        safe_text
)
ddsMetamodel::DdsSystem_strategy = st.builds(
    ddsMetamodel::DdsSystem,
    systemName=
        safe_text
)
ddsMetamodel::DdsDataModule_strategy = st.builds(
    ddsMetamodel::DdsDataModule,
    moduleName=
        safe_text
)
ddsMetamodel::DdsDataWriterQosProfile_strategy = st.builds(
    ddsMetamodel::DdsDataWriterQosProfile,
)
ddsMetamodel::DdsDataWriterListener_strategy = st.builds(
    ddsMetamodel::DdsDataWriterListener,
    name=
        safe_text,
    listenedStatus=
        safe_text
)
ddsMetamodel::DdsPublisherQosProfile_strategy = st.builds(
    ddsMetamodel::DdsPublisherQosProfile,
)
ddsMetamodel::DdsPublisherListener_strategy = st.builds(
    ddsMetamodel::DdsPublisherListener,
    listenedStatus=
        safe_text,
    name=
        safe_text
)
ddsMetamodel::DdsDataWriter_strategy = st.builds(
    ddsMetamodel::DdsDataWriter,
    dataWriterName=
        safe_text
)
ddsMetamodel::DdsDataReaderQosProfile_strategy = st.builds(
    ddsMetamodel::DdsDataReaderQosProfile,
)
ddsMetamodel::DdsStructuredField_strategy = st.builds(
    ddsMetamodel::DdsStructuredField,
    isKey=
        st.booleans(),
    fieldName=
        safe_text,
    maxMultiplicity=
        st.integers()
)
ddsMetamodel::DdsDataField_strategy = st.builds(
    ddsMetamodel::DdsDataField,
    fieldType=
        safe_text,
    maxMultiplicity=
        st.integers(),
    fieldName=
        safe_text,
    isKey=
        st.booleans()
)
ddsMetamodel::DdsDataReader_strategy = st.builds(
    ddsMetamodel::DdsDataReader,
    dataReaderName=
        safe_text
)
ddsMetamodel::DdsQosProfile_strategy = st.builds(
    ddsMetamodel::DdsQosProfile,
    profileName=
        safe_text
)
ddsMetamodel::DdsDataStructure_strategy = st.builds(
    ddsMetamodel::DdsDataStructure,
    structureName=
        safe_text
)
ddsMetamodel::DdsTopicQosProfile_strategy = st.builds(
    ddsMetamodel::DdsTopicQosProfile,
)
ddsMetamodel::DdsTopicListener_strategy = st.builds(
    ddsMetamodel::DdsTopicListener,
    listenedStatus=
        safe_text,
    name=
        safe_text
)
ddsMetamodel::DdsTopic_strategy = st.builds(
    ddsMetamodel::DdsTopic,
    topicName=
        safe_text
)
ddsMetamodel::DdsDomainParticipantListener_strategy = st.builds(
    ddsMetamodel::DdsDomainParticipantListener,
    name=
        safe_text,
    listenedStatus=
        safe_text
)
ddsMetamodel::DdsDomainParticipantQosProfile_strategy = st.builds(
    ddsMetamodel::DdsDomainParticipantQosProfile,
)
ddsMetamodel::DdsPublisher_strategy = st.builds(
    ddsMetamodel::DdsPublisher,
    publisherName=
        safe_text
)
ddsMetamodel::DdsSubscriber_strategy = st.builds(
    ddsMetamodel::DdsSubscriber,
    subscriberName=
        safe_text
)
ddsMetamodel::DdsWaitSet_strategy = st.builds(
    ddsMetamodel::DdsWaitSet,
    name=
        safe_text
)
ddsMetamodel::DdsDomainParticipant_strategy = st.builds(
    ddsMetamodel::DdsDomainParticipant,
    domainParticipantName=
        safe_text,
    domainId=
        st.integers()
)
ddsMetamodel::DdsApplication_strategy = st.builds(
    ddsMetamodel::DdsApplication,
    applicationName=
        safe_text
)
ddsMetamodel::DdsDataReaderListener_strategy = st.builds(
    ddsMetamodel::DdsDataReaderListener,
    listenedStatus=
        safe_text,
    name=
        safe_text
)
ddsMetamodel::DdsSubscriberQosProfile_strategy = st.builds(
    ddsMetamodel::DdsSubscriberQosProfile,
)
ddsMetamodel::DdsSubscriberListener_strategy = st.builds(
    ddsMetamodel::DdsSubscriberListener,
    name=
        safe_text,
    listenedStatus=
        safe_text
)

@given(instance=ddsMetamodel::DdsHost_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddshost_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsHost)

@given(instance=ddsMetamodel::DdsHost_strategy)
def test_ddsmetamodel::ddshost_hostName_type(instance):
    assert isinstance(instance.hostName, str)


@given(instance=ddsMetamodel::DdsHost_strategy)
def test_ddsmetamodel::ddshost_hostName_setter(instance):
    original = instance.hostName
    instance.hostName = original
    assert instance.hostName == original

@given(instance=DdsReadCondition_strategy)
@settings(max_examples=50)
def test_ddsreadcondition_instantiation(instance):
    assert isinstance(instance, DdsReadCondition)

@given(instance=ddsMetamodel::QueryCondition_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::querycondition_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::QueryCondition)

@given(instance=ddsMetamodel::QueryCondition_strategy)
def test_ddsmetamodel::querycondition_queryParameters_type(instance):
    assert isinstance(instance.queryParameters, str)


@given(instance=ddsMetamodel::QueryCondition_strategy)
def test_ddsmetamodel::querycondition_queryParameters_setter(instance):
    original = instance.queryParameters
    instance.queryParameters = original
    assert instance.queryParameters == original

@given(instance=ddsMetamodel::QueryCondition_strategy)
def test_ddsmetamodel::querycondition_query_type(instance):
    assert isinstance(instance.query, str)


@given(instance=ddsMetamodel::QueryCondition_strategy)
def test_ddsmetamodel::querycondition_query_setter(instance):
    original = instance.query
    instance.query = original
    assert instance.query == original

@given(instance=DdsStatusCondition_strategy)
@settings(max_examples=50)
def test_ddsstatuscondition_instantiation(instance):
    assert isinstance(instance, DdsStatusCondition)

@given(instance=ddsMetamodel::DdsDataReaderStatusCondition_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsdatareaderstatuscondition_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsDataReaderStatusCondition)

@given(instance=ddsMetamodel::DdsDataReaderStatusCondition_strategy)
def test_ddsmetamodel::ddsdatareaderstatuscondition_enabled_status_type(instance):
    assert isinstance(instance.enabled_status, str)


@given(instance=ddsMetamodel::DdsDataReaderStatusCondition_strategy)
def test_ddsmetamodel::ddsdatareaderstatuscondition_enabled_status_setter(instance):
    original = instance.enabled_status
    instance.enabled_status = original
    assert instance.enabled_status == original

@given(instance=ddsMetamodel::DdsPublisherStatusCondition_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddspublisherstatuscondition_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsPublisherStatusCondition)

@given(instance=ddsMetamodel::DdsPublisherStatusCondition_strategy)
def test_ddsmetamodel::ddspublisherstatuscondition_enabled_status_type(instance):
    assert isinstance(instance.enabled_status, str)


@given(instance=ddsMetamodel::DdsPublisherStatusCondition_strategy)
def test_ddsmetamodel::ddspublisherstatuscondition_enabled_status_setter(instance):
    original = instance.enabled_status
    instance.enabled_status = original
    assert instance.enabled_status == original

@given(instance=ddsMetamodel::DdsTopicStatusCondition_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddstopicstatuscondition_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsTopicStatusCondition)

@given(instance=ddsMetamodel::DdsTopicStatusCondition_strategy)
def test_ddsmetamodel::ddstopicstatuscondition_enabled_status_type(instance):
    assert isinstance(instance.enabled_status, str)


@given(instance=ddsMetamodel::DdsTopicStatusCondition_strategy)
def test_ddsmetamodel::ddstopicstatuscondition_enabled_status_setter(instance):
    original = instance.enabled_status
    instance.enabled_status = original
    assert instance.enabled_status == original

@given(instance=ddsMetamodel::DdsDomainParticipantStatusCondition_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsdomainparticipantstatuscondition_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsDomainParticipantStatusCondition)

@given(instance=ddsMetamodel::DdsDomainParticipantStatusCondition_strategy)
def test_ddsmetamodel::ddsdomainparticipantstatuscondition_enabled_status_type(instance):
    assert isinstance(instance.enabled_status, str)


@given(instance=ddsMetamodel::DdsDomainParticipantStatusCondition_strategy)
def test_ddsmetamodel::ddsdomainparticipantstatuscondition_enabled_status_setter(instance):
    original = instance.enabled_status
    instance.enabled_status = original
    assert instance.enabled_status == original

@given(instance=ddsMetamodel::DdsDataWriterStatusCondition_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsdatawriterstatuscondition_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsDataWriterStatusCondition)

@given(instance=ddsMetamodel::DdsDataWriterStatusCondition_strategy)
def test_ddsmetamodel::ddsdatawriterstatuscondition_enabled_status_type(instance):
    assert isinstance(instance.enabled_status, str)


@given(instance=ddsMetamodel::DdsDataWriterStatusCondition_strategy)
def test_ddsmetamodel::ddsdatawriterstatuscondition_enabled_status_setter(instance):
    original = instance.enabled_status
    instance.enabled_status = original
    assert instance.enabled_status == original

@given(instance=ddsMetamodel::DdsSubscriberStatusCondition_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddssubscriberstatuscondition_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsSubscriberStatusCondition)

@given(instance=ddsMetamodel::DdsSubscriberStatusCondition_strategy)
def test_ddsmetamodel::ddssubscriberstatuscondition_enabled_status_type(instance):
    assert isinstance(instance.enabled_status, str)


@given(instance=ddsMetamodel::DdsSubscriberStatusCondition_strategy)
def test_ddsmetamodel::ddssubscriberstatuscondition_enabled_status_setter(instance):
    original = instance.enabled_status
    instance.enabled_status = original
    assert instance.enabled_status == original

@given(instance=ddsMetamodel::GuardCondition_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::guardcondition_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::GuardCondition)

@given(instance=ddsMetamodel::GuardCondition_strategy)
def test_ddsmetamodel::guardcondition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ddsMetamodel::GuardCondition_strategy)
def test_ddsmetamodel::guardcondition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ddsMetamodel::DdsStatusCondition_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsstatuscondition_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsStatusCondition)

@given(instance=ddsMetamodel::DdsReadCondition_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsreadcondition_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsReadCondition)

@given(instance=ddsMetamodel::DdsReadCondition_strategy)
def test_ddsmetamodel::ddsreadcondition_sample_state_mask_type(instance):
    assert isinstance(instance.sample_state_mask, str)


@given(instance=ddsMetamodel::DdsReadCondition_strategy)
def test_ddsmetamodel::ddsreadcondition_sample_state_mask_setter(instance):
    original = instance.sample_state_mask
    instance.sample_state_mask = original
    assert instance.sample_state_mask == original

@given(instance=ddsMetamodel::DdsReadCondition_strategy)
def test_ddsmetamodel::ddsreadcondition_view_state_mask_type(instance):
    assert isinstance(instance.view_state_mask, str)


@given(instance=ddsMetamodel::DdsReadCondition_strategy)
def test_ddsmetamodel::ddsreadcondition_view_state_mask_setter(instance):
    original = instance.view_state_mask
    instance.view_state_mask = original
    assert instance.view_state_mask == original

@given(instance=ddsMetamodel::DdsReadCondition_strategy)
def test_ddsmetamodel::ddsreadcondition_instance_state_mask_type(instance):
    assert isinstance(instance.instance_state_mask, str)


@given(instance=ddsMetamodel::DdsReadCondition_strategy)
def test_ddsmetamodel::ddsreadcondition_instance_state_mask_setter(instance):
    original = instance.instance_state_mask
    instance.instance_state_mask = original
    assert instance.instance_state_mask == original

@given(instance=ddsMetamodel::DdsGroupDataQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsgroupdataqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsGroupDataQos)

@given(instance=ddsMetamodel::DdsGroupDataQos_strategy)
def test_ddsmetamodel::ddsgroupdataqos_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ddsMetamodel::DdsGroupDataQos_strategy)
def test_ddsmetamodel::ddsgroupdataqos_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ddsMetamodel::DdsDataWriterLifecycleQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsdatawriterlifecycleqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsDataWriterLifecycleQos)

@given(instance=ddsMetamodel::DdsDataWriterLifecycleQos_strategy)
def test_ddsmetamodel::ddsdatawriterlifecycleqos_autodispose_unregistered_instances_type(instance):
    assert isinstance(instance.autodispose_unregistered_instances, bool)


@given(instance=ddsMetamodel::DdsDataWriterLifecycleQos_strategy)
def test_ddsmetamodel::ddsdatawriterlifecycleqos_autodispose_unregistered_instances_setter(instance):
    original = instance.autodispose_unregistered_instances
    instance.autodispose_unregistered_instances = original
    assert instance.autodispose_unregistered_instances == original

@given(instance=ddsMetamodel::DdsPartitionQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddspartitionqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsPartitionQos)

@given(instance=ddsMetamodel::DdsPartitionQos_strategy)
def test_ddsmetamodel::ddspartitionqos_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ddsMetamodel::DdsPartitionQos_strategy)
def test_ddsmetamodel::ddspartitionqos_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ddsMetamodel::DdsTimeBasedFilterQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddstimebasedfilterqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsTimeBasedFilterQos)

@given(instance=ddsMetamodel::DdsDataReaderLifecycleQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsdatareaderlifecycleqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsDataReaderLifecycleQos)

@given(instance=ddsMetamodel::DdsDataReaderLifecycleQos_strategy)
def test_ddsmetamodel::ddsdatareaderlifecycleqos_enable_invalid_samples_type(instance):
    assert isinstance(instance.enable_invalid_samples, bool)


@given(instance=ddsMetamodel::DdsDataReaderLifecycleQos_strategy)
def test_ddsmetamodel::ddsdatareaderlifecycleqos_enable_invalid_samples_setter(instance):
    original = instance.enable_invalid_samples
    instance.enable_invalid_samples = original
    assert instance.enable_invalid_samples == original

@given(instance=ddsMetamodel::DdsDataReaderLifecycleQos_strategy)
def test_ddsmetamodel::ddsdatareaderlifecycleqos_autopurge_dispose_all_type(instance):
    assert isinstance(instance.autopurge_dispose_all, bool)


@given(instance=ddsMetamodel::DdsDataReaderLifecycleQos_strategy)
def test_ddsmetamodel::ddsdatareaderlifecycleqos_autopurge_dispose_all_setter(instance):
    original = instance.autopurge_dispose_all
    instance.autopurge_dispose_all = original
    assert instance.autopurge_dispose_all == original

@given(instance=ddsMetamodel::DdsPresentationQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddspresentationqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsPresentationQos)

@given(instance=ddsMetamodel::DdsPresentationQos_strategy)
def test_ddsmetamodel::ddspresentationqos_ordered_access_type(instance):
    assert isinstance(instance.ordered_access, bool)


@given(instance=ddsMetamodel::DdsPresentationQos_strategy)
def test_ddsmetamodel::ddspresentationqos_ordered_access_setter(instance):
    original = instance.ordered_access
    instance.ordered_access = original
    assert instance.ordered_access == original

@given(instance=ddsMetamodel::DdsPresentationQos_strategy)
def test_ddsmetamodel::ddspresentationqos_coherent_access_type(instance):
    assert isinstance(instance.coherent_access, bool)


@given(instance=ddsMetamodel::DdsPresentationQos_strategy)
def test_ddsmetamodel::ddspresentationqos_coherent_access_setter(instance):
    original = instance.coherent_access
    instance.coherent_access = original
    assert instance.coherent_access == original

@given(instance=ddsMetamodel::DdsPresentationQos_strategy)
def test_ddsmetamodel::ddspresentationqos_access_scope_type(instance):
    assert isinstance(instance.access_scope, str)


@given(instance=ddsMetamodel::DdsPresentationQos_strategy)
def test_ddsmetamodel::ddspresentationqos_access_scope_setter(instance):
    original = instance.access_scope
    instance.access_scope = original
    assert instance.access_scope == original

@given(instance=ddsMetamodel::DdsDuration_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsduration_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsDuration)

@given(instance=ddsMetamodel::DdsDuration_strategy)
def test_ddsmetamodel::ddsduration_sec_type(instance):
    assert isinstance(instance.sec, str)


@given(instance=ddsMetamodel::DdsDuration_strategy)
def test_ddsmetamodel::ddsduration_sec_setter(instance):
    original = instance.sec
    instance.sec = original
    assert instance.sec == original

@given(instance=ddsMetamodel::DdsDuration_strategy)
def test_ddsmetamodel::ddsduration_nanoSec_type(instance):
    assert isinstance(instance.nanoSec, str)


@given(instance=ddsMetamodel::DdsDuration_strategy)
def test_ddsmetamodel::ddsduration_nanoSec_setter(instance):
    original = instance.nanoSec
    instance.nanoSec = original
    assert instance.nanoSec == original

@given(instance=ddsMetamodel::DdsOwnershipStrengthQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsownershipstrengthqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsOwnershipStrengthQos)

@given(instance=ddsMetamodel::DdsOwnershipStrengthQos_strategy)
def test_ddsmetamodel::ddsownershipstrengthqos_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ddsMetamodel::DdsOwnershipStrengthQos_strategy)
def test_ddsmetamodel::ddsownershipstrengthqos_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ddsMetamodel::DdsDestinationOrderQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsdestinationorderqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsDestinationOrderQos)

@given(instance=ddsMetamodel::DdsDestinationOrderQos_strategy)
def test_ddsmetamodel::ddsdestinationorderqos_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=ddsMetamodel::DdsDestinationOrderQos_strategy)
def test_ddsmetamodel::ddsdestinationorderqos_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=ddsMetamodel::DdsReliabilityQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsreliabilityqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsReliabilityQos)

@given(instance=ddsMetamodel::DdsReliabilityQos_strategy)
def test_ddsmetamodel::ddsreliabilityqos_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=ddsMetamodel::DdsReliabilityQos_strategy)
def test_ddsmetamodel::ddsreliabilityqos_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=ddsMetamodel::DdsOwnershipQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsownershipqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsOwnershipQos)

@given(instance=ddsMetamodel::DdsOwnershipQos_strategy)
def test_ddsmetamodel::ddsownershipqos_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=ddsMetamodel::DdsOwnershipQos_strategy)
def test_ddsmetamodel::ddsownershipqos_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=ddsMetamodel::DdsLivelinessQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddslivelinessqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsLivelinessQos)

@given(instance=ddsMetamodel::DdsLivelinessQos_strategy)
def test_ddsmetamodel::ddslivelinessqos_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=ddsMetamodel::DdsLivelinessQos_strategy)
def test_ddsmetamodel::ddslivelinessqos_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=ddsMetamodel::DdsLatencyBudgetQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddslatencybudgetqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsLatencyBudgetQos)

@given(instance=ddsMetamodel::DdsDurabilityServiceQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsdurabilityserviceqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsDurabilityServiceQos)

@given(instance=ddsMetamodel::DdsDurabilityServiceQos_strategy)
def test_ddsmetamodel::ddsdurabilityserviceqos_max_samples_type(instance):
    assert isinstance(instance.max_samples, str)


@given(instance=ddsMetamodel::DdsDurabilityServiceQos_strategy)
def test_ddsmetamodel::ddsdurabilityserviceqos_max_samples_setter(instance):
    original = instance.max_samples
    instance.max_samples = original
    assert instance.max_samples == original

@given(instance=ddsMetamodel::DdsDurabilityServiceQos_strategy)
def test_ddsmetamodel::ddsdurabilityserviceqos_max_samples_per_instances_type(instance):
    assert isinstance(instance.max_samples_per_instances, str)


@given(instance=ddsMetamodel::DdsDurabilityServiceQos_strategy)
def test_ddsmetamodel::ddsdurabilityserviceqos_max_samples_per_instances_setter(instance):
    original = instance.max_samples_per_instances
    instance.max_samples_per_instances = original
    assert instance.max_samples_per_instances == original

@given(instance=ddsMetamodel::DdsDurabilityServiceQos_strategy)
def test_ddsmetamodel::ddsdurabilityserviceqos_max_instances_type(instance):
    assert isinstance(instance.max_instances, str)


@given(instance=ddsMetamodel::DdsDurabilityServiceQos_strategy)
def test_ddsmetamodel::ddsdurabilityserviceqos_max_instances_setter(instance):
    original = instance.max_instances
    instance.max_instances = original
    assert instance.max_instances == original

@given(instance=ddsMetamodel::DdsDurabilityServiceQos_strategy)
def test_ddsmetamodel::ddsdurabilityserviceqos_history_kind_type(instance):
    assert isinstance(instance.history_kind, str)


@given(instance=ddsMetamodel::DdsDurabilityServiceQos_strategy)
def test_ddsmetamodel::ddsdurabilityserviceqos_history_kind_setter(instance):
    original = instance.history_kind
    instance.history_kind = original
    assert instance.history_kind == original

@given(instance=ddsMetamodel::DdsDurabilityServiceQos_strategy)
def test_ddsmetamodel::ddsdurabilityserviceqos_history_depth_type(instance):
    assert isinstance(instance.history_depth, str)


@given(instance=ddsMetamodel::DdsDurabilityServiceQos_strategy)
def test_ddsmetamodel::ddsdurabilityserviceqos_history_depth_setter(instance):
    original = instance.history_depth
    instance.history_depth = original
    assert instance.history_depth == original

@given(instance=ddsMetamodel::DdsDurabilityQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsdurabilityqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsDurabilityQos)

@given(instance=ddsMetamodel::DdsDurabilityQos_strategy)
def test_ddsmetamodel::ddsdurabilityqos_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=ddsMetamodel::DdsDurabilityQos_strategy)
def test_ddsmetamodel::ddsdurabilityqos_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=ddsMetamodel::DdsTopicDataQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddstopicdataqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsTopicDataQos)

@given(instance=ddsMetamodel::DdsTopicDataQos_strategy)
def test_ddsmetamodel::ddstopicdataqos_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ddsMetamodel::DdsTopicDataQos_strategy)
def test_ddsmetamodel::ddstopicdataqos_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ddsMetamodel::DdsEntityFactoryQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsentityfactoryqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsEntityFactoryQos)

@given(instance=ddsMetamodel::DdsEntityFactoryQos_strategy)
def test_ddsmetamodel::ddsentityfactoryqos_autoenable_created_entities_type(instance):
    assert isinstance(instance.autoenable_created_entities, bool)


@given(instance=ddsMetamodel::DdsEntityFactoryQos_strategy)
def test_ddsmetamodel::ddsentityfactoryqos_autoenable_created_entities_setter(instance):
    original = instance.autoenable_created_entities
    instance.autoenable_created_entities = original
    assert instance.autoenable_created_entities == original

@given(instance=ddsMetamodel::DdsUserDataQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsuserdataqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsUserDataQos)

@given(instance=ddsMetamodel::DdsUserDataQos_strategy)
def test_ddsmetamodel::ddsuserdataqos_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ddsMetamodel::DdsUserDataQos_strategy)
def test_ddsmetamodel::ddsuserdataqos_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=DdsQosProfile_strategy)
@settings(max_examples=50)
def test_ddsqosprofile_instantiation(instance):
    assert isinstance(instance, DdsQosProfile)

@given(instance=ddsMetamodel::DdsDeadlineQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsdeadlineqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsDeadlineQos)

@given(instance=ddsMetamodel::DdsLifespan_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddslifespan_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsLifespan)

@given(instance=ddsMetamodel::DdsTransportPriorityQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddstransportpriorityqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsTransportPriorityQos)

@given(instance=ddsMetamodel::DdsTransportPriorityQos_strategy)
def test_ddsmetamodel::ddstransportpriorityqos_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ddsMetamodel::DdsTransportPriorityQos_strategy)
def test_ddsmetamodel::ddstransportpriorityqos_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ddsMetamodel::DdsResourceLimits_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsresourcelimits_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsResourceLimits)

@given(instance=ddsMetamodel::DdsResourceLimits_strategy)
def test_ddsmetamodel::ddsresourcelimits_max_instances_type(instance):
    assert isinstance(instance.max_instances, str)


@given(instance=ddsMetamodel::DdsResourceLimits_strategy)
def test_ddsmetamodel::ddsresourcelimits_max_instances_setter(instance):
    original = instance.max_instances
    instance.max_instances = original
    assert instance.max_instances == original

@given(instance=ddsMetamodel::DdsResourceLimits_strategy)
def test_ddsmetamodel::ddsresourcelimits_max_samples_type(instance):
    assert isinstance(instance.max_samples, str)


@given(instance=ddsMetamodel::DdsResourceLimits_strategy)
def test_ddsmetamodel::ddsresourcelimits_max_samples_setter(instance):
    original = instance.max_samples
    instance.max_samples = original
    assert instance.max_samples == original

@given(instance=ddsMetamodel::DdsResourceLimits_strategy)
def test_ddsmetamodel::ddsresourcelimits_max_samples_per_instances_type(instance):
    assert isinstance(instance.max_samples_per_instances, str)


@given(instance=ddsMetamodel::DdsResourceLimits_strategy)
def test_ddsmetamodel::ddsresourcelimits_max_samples_per_instances_setter(instance):
    original = instance.max_samples_per_instances
    instance.max_samples_per_instances = original
    assert instance.max_samples_per_instances == original

@given(instance=ddsMetamodel::DdsHistoryQos_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddshistoryqos_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsHistoryQos)

@given(instance=ddsMetamodel::DdsHistoryQos_strategy)
def test_ddsmetamodel::ddshistoryqos_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=ddsMetamodel::DdsHistoryQos_strategy)
def test_ddsmetamodel::ddshistoryqos_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=ddsMetamodel::DdsHistoryQos_strategy)
def test_ddsmetamodel::ddshistoryqos_depth_type(instance):
    assert isinstance(instance.depth, str)


@given(instance=ddsMetamodel::DdsHistoryQos_strategy)
def test_ddsmetamodel::ddshistoryqos_depth_setter(instance):
    original = instance.depth
    instance.depth = original
    assert instance.depth == original

@given(instance=ddsMetamodel::DdsSystem_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddssystem_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsSystem)

@given(instance=ddsMetamodel::DdsSystem_strategy)
def test_ddsmetamodel::ddssystem_systemName_type(instance):
    assert isinstance(instance.systemName, str)


@given(instance=ddsMetamodel::DdsSystem_strategy)
def test_ddsmetamodel::ddssystem_systemName_setter(instance):
    original = instance.systemName
    instance.systemName = original
    assert instance.systemName == original

@given(instance=ddsMetamodel::DdsDataModule_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsdatamodule_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsDataModule)

@given(instance=ddsMetamodel::DdsDataModule_strategy)
def test_ddsmetamodel::ddsdatamodule_moduleName_type(instance):
    assert isinstance(instance.moduleName, str)


@given(instance=ddsMetamodel::DdsDataModule_strategy)
def test_ddsmetamodel::ddsdatamodule_moduleName_setter(instance):
    original = instance.moduleName
    instance.moduleName = original
    assert instance.moduleName == original

@given(instance=ddsMetamodel::DdsDataWriterQosProfile_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsdatawriterqosprofile_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsDataWriterQosProfile)

@given(instance=ddsMetamodel::DdsDataWriterListener_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsdatawriterlistener_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsDataWriterListener)

@given(instance=ddsMetamodel::DdsDataWriterListener_strategy)
def test_ddsmetamodel::ddsdatawriterlistener_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ddsMetamodel::DdsDataWriterListener_strategy)
def test_ddsmetamodel::ddsdatawriterlistener_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ddsMetamodel::DdsDataWriterListener_strategy)
def test_ddsmetamodel::ddsdatawriterlistener_listenedStatus_type(instance):
    assert isinstance(instance.listenedStatus, str)


@given(instance=ddsMetamodel::DdsDataWriterListener_strategy)
def test_ddsmetamodel::ddsdatawriterlistener_listenedStatus_setter(instance):
    original = instance.listenedStatus
    instance.listenedStatus = original
    assert instance.listenedStatus == original

@given(instance=ddsMetamodel::DdsPublisherQosProfile_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddspublisherqosprofile_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsPublisherQosProfile)

@given(instance=ddsMetamodel::DdsPublisherListener_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddspublisherlistener_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsPublisherListener)

@given(instance=ddsMetamodel::DdsPublisherListener_strategy)
def test_ddsmetamodel::ddspublisherlistener_listenedStatus_type(instance):
    assert isinstance(instance.listenedStatus, str)


@given(instance=ddsMetamodel::DdsPublisherListener_strategy)
def test_ddsmetamodel::ddspublisherlistener_listenedStatus_setter(instance):
    original = instance.listenedStatus
    instance.listenedStatus = original
    assert instance.listenedStatus == original

@given(instance=ddsMetamodel::DdsPublisherListener_strategy)
def test_ddsmetamodel::ddspublisherlistener_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ddsMetamodel::DdsPublisherListener_strategy)
def test_ddsmetamodel::ddspublisherlistener_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ddsMetamodel::DdsDataWriter_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsdatawriter_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsDataWriter)

@given(instance=ddsMetamodel::DdsDataWriter_strategy)
def test_ddsmetamodel::ddsdatawriter_dataWriterName_type(instance):
    assert isinstance(instance.dataWriterName, str)


@given(instance=ddsMetamodel::DdsDataWriter_strategy)
def test_ddsmetamodel::ddsdatawriter_dataWriterName_setter(instance):
    original = instance.dataWriterName
    instance.dataWriterName = original
    assert instance.dataWriterName == original

@given(instance=ddsMetamodel::DdsDataReaderQosProfile_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsdatareaderqosprofile_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsDataReaderQosProfile)

@given(instance=ddsMetamodel::DdsStructuredField_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsstructuredfield_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsStructuredField)

@given(instance=ddsMetamodel::DdsStructuredField_strategy)
def test_ddsmetamodel::ddsstructuredfield_isKey_type(instance):
    assert isinstance(instance.isKey, bool)


@given(instance=ddsMetamodel::DdsStructuredField_strategy)
def test_ddsmetamodel::ddsstructuredfield_isKey_setter(instance):
    original = instance.isKey
    instance.isKey = original
    assert instance.isKey == original

@given(instance=ddsMetamodel::DdsStructuredField_strategy)
def test_ddsmetamodel::ddsstructuredfield_fieldName_type(instance):
    assert isinstance(instance.fieldName, str)


@given(instance=ddsMetamodel::DdsStructuredField_strategy)
def test_ddsmetamodel::ddsstructuredfield_fieldName_setter(instance):
    original = instance.fieldName
    instance.fieldName = original
    assert instance.fieldName == original

@given(instance=ddsMetamodel::DdsStructuredField_strategy)
def test_ddsmetamodel::ddsstructuredfield_maxMultiplicity_type(instance):
    assert isinstance(instance.maxMultiplicity, int)


@given(instance=ddsMetamodel::DdsStructuredField_strategy)
def test_ddsmetamodel::ddsstructuredfield_maxMultiplicity_setter(instance):
    original = instance.maxMultiplicity
    instance.maxMultiplicity = original
    assert instance.maxMultiplicity == original

@given(instance=ddsMetamodel::DdsDataField_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsdatafield_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsDataField)

@given(instance=ddsMetamodel::DdsDataField_strategy)
def test_ddsmetamodel::ddsdatafield_fieldType_type(instance):
    assert isinstance(instance.fieldType, str)


@given(instance=ddsMetamodel::DdsDataField_strategy)
def test_ddsmetamodel::ddsdatafield_fieldType_setter(instance):
    original = instance.fieldType
    instance.fieldType = original
    assert instance.fieldType == original

@given(instance=ddsMetamodel::DdsDataField_strategy)
def test_ddsmetamodel::ddsdatafield_maxMultiplicity_type(instance):
    assert isinstance(instance.maxMultiplicity, int)


@given(instance=ddsMetamodel::DdsDataField_strategy)
def test_ddsmetamodel::ddsdatafield_maxMultiplicity_setter(instance):
    original = instance.maxMultiplicity
    instance.maxMultiplicity = original
    assert instance.maxMultiplicity == original

@given(instance=ddsMetamodel::DdsDataField_strategy)
def test_ddsmetamodel::ddsdatafield_fieldName_type(instance):
    assert isinstance(instance.fieldName, str)


@given(instance=ddsMetamodel::DdsDataField_strategy)
def test_ddsmetamodel::ddsdatafield_fieldName_setter(instance):
    original = instance.fieldName
    instance.fieldName = original
    assert instance.fieldName == original

@given(instance=ddsMetamodel::DdsDataField_strategy)
def test_ddsmetamodel::ddsdatafield_isKey_type(instance):
    assert isinstance(instance.isKey, bool)


@given(instance=ddsMetamodel::DdsDataField_strategy)
def test_ddsmetamodel::ddsdatafield_isKey_setter(instance):
    original = instance.isKey
    instance.isKey = original
    assert instance.isKey == original

@given(instance=ddsMetamodel::DdsDataReader_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsdatareader_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsDataReader)

@given(instance=ddsMetamodel::DdsDataReader_strategy)
def test_ddsmetamodel::ddsdatareader_dataReaderName_type(instance):
    assert isinstance(instance.dataReaderName, str)


@given(instance=ddsMetamodel::DdsDataReader_strategy)
def test_ddsmetamodel::ddsdatareader_dataReaderName_setter(instance):
    original = instance.dataReaderName
    instance.dataReaderName = original
    assert instance.dataReaderName == original

@given(instance=ddsMetamodel::DdsQosProfile_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsqosprofile_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsQosProfile)

@given(instance=ddsMetamodel::DdsQosProfile_strategy)
def test_ddsmetamodel::ddsqosprofile_profileName_type(instance):
    assert isinstance(instance.profileName, str)


@given(instance=ddsMetamodel::DdsQosProfile_strategy)
def test_ddsmetamodel::ddsqosprofile_profileName_setter(instance):
    original = instance.profileName
    instance.profileName = original
    assert instance.profileName == original

@given(instance=ddsMetamodel::DdsDataStructure_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsdatastructure_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsDataStructure)

@given(instance=ddsMetamodel::DdsDataStructure_strategy)
def test_ddsmetamodel::ddsdatastructure_structureName_type(instance):
    assert isinstance(instance.structureName, str)


@given(instance=ddsMetamodel::DdsDataStructure_strategy)
def test_ddsmetamodel::ddsdatastructure_structureName_setter(instance):
    original = instance.structureName
    instance.structureName = original
    assert instance.structureName == original

@given(instance=ddsMetamodel::DdsTopicQosProfile_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddstopicqosprofile_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsTopicQosProfile)

@given(instance=ddsMetamodel::DdsTopicListener_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddstopiclistener_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsTopicListener)

@given(instance=ddsMetamodel::DdsTopicListener_strategy)
def test_ddsmetamodel::ddstopiclistener_listenedStatus_type(instance):
    assert isinstance(instance.listenedStatus, str)


@given(instance=ddsMetamodel::DdsTopicListener_strategy)
def test_ddsmetamodel::ddstopiclistener_listenedStatus_setter(instance):
    original = instance.listenedStatus
    instance.listenedStatus = original
    assert instance.listenedStatus == original

@given(instance=ddsMetamodel::DdsTopicListener_strategy)
def test_ddsmetamodel::ddstopiclistener_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ddsMetamodel::DdsTopicListener_strategy)
def test_ddsmetamodel::ddstopiclistener_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ddsMetamodel::DdsTopic_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddstopic_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsTopic)

@given(instance=ddsMetamodel::DdsTopic_strategy)
def test_ddsmetamodel::ddstopic_topicName_type(instance):
    assert isinstance(instance.topicName, str)


@given(instance=ddsMetamodel::DdsTopic_strategy)
def test_ddsmetamodel::ddstopic_topicName_setter(instance):
    original = instance.topicName
    instance.topicName = original
    assert instance.topicName == original

@given(instance=ddsMetamodel::DdsDomainParticipantListener_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsdomainparticipantlistener_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsDomainParticipantListener)

@given(instance=ddsMetamodel::DdsDomainParticipantListener_strategy)
def test_ddsmetamodel::ddsdomainparticipantlistener_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ddsMetamodel::DdsDomainParticipantListener_strategy)
def test_ddsmetamodel::ddsdomainparticipantlistener_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ddsMetamodel::DdsDomainParticipantListener_strategy)
def test_ddsmetamodel::ddsdomainparticipantlistener_listenedStatus_type(instance):
    assert isinstance(instance.listenedStatus, str)


@given(instance=ddsMetamodel::DdsDomainParticipantListener_strategy)
def test_ddsmetamodel::ddsdomainparticipantlistener_listenedStatus_setter(instance):
    original = instance.listenedStatus
    instance.listenedStatus = original
    assert instance.listenedStatus == original

@given(instance=ddsMetamodel::DdsDomainParticipantQosProfile_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsdomainparticipantqosprofile_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsDomainParticipantQosProfile)

@given(instance=ddsMetamodel::DdsPublisher_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddspublisher_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsPublisher)

@given(instance=ddsMetamodel::DdsPublisher_strategy)
def test_ddsmetamodel::ddspublisher_publisherName_type(instance):
    assert isinstance(instance.publisherName, str)


@given(instance=ddsMetamodel::DdsPublisher_strategy)
def test_ddsmetamodel::ddspublisher_publisherName_setter(instance):
    original = instance.publisherName
    instance.publisherName = original
    assert instance.publisherName == original

@given(instance=ddsMetamodel::DdsSubscriber_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddssubscriber_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsSubscriber)

@given(instance=ddsMetamodel::DdsSubscriber_strategy)
def test_ddsmetamodel::ddssubscriber_subscriberName_type(instance):
    assert isinstance(instance.subscriberName, str)


@given(instance=ddsMetamodel::DdsSubscriber_strategy)
def test_ddsmetamodel::ddssubscriber_subscriberName_setter(instance):
    original = instance.subscriberName
    instance.subscriberName = original
    assert instance.subscriberName == original

@given(instance=ddsMetamodel::DdsWaitSet_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddswaitset_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsWaitSet)

@given(instance=ddsMetamodel::DdsWaitSet_strategy)
def test_ddsmetamodel::ddswaitset_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ddsMetamodel::DdsWaitSet_strategy)
def test_ddsmetamodel::ddswaitset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ddsMetamodel::DdsDomainParticipant_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsdomainparticipant_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsDomainParticipant)

@given(instance=ddsMetamodel::DdsDomainParticipant_strategy)
def test_ddsmetamodel::ddsdomainparticipant_domainParticipantName_type(instance):
    assert isinstance(instance.domainParticipantName, str)


@given(instance=ddsMetamodel::DdsDomainParticipant_strategy)
def test_ddsmetamodel::ddsdomainparticipant_domainParticipantName_setter(instance):
    original = instance.domainParticipantName
    instance.domainParticipantName = original
    assert instance.domainParticipantName == original

@given(instance=ddsMetamodel::DdsDomainParticipant_strategy)
def test_ddsmetamodel::ddsdomainparticipant_domainId_type(instance):
    assert isinstance(instance.domainId, int)


@given(instance=ddsMetamodel::DdsDomainParticipant_strategy)
def test_ddsmetamodel::ddsdomainparticipant_domainId_setter(instance):
    original = instance.domainId
    instance.domainId = original
    assert instance.domainId == original

@given(instance=ddsMetamodel::DdsApplication_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsapplication_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsApplication)

@given(instance=ddsMetamodel::DdsApplication_strategy)
def test_ddsmetamodel::ddsapplication_applicationName_type(instance):
    assert isinstance(instance.applicationName, str)


@given(instance=ddsMetamodel::DdsApplication_strategy)
def test_ddsmetamodel::ddsapplication_applicationName_setter(instance):
    original = instance.applicationName
    instance.applicationName = original
    assert instance.applicationName == original

@given(instance=ddsMetamodel::DdsDataReaderListener_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddsdatareaderlistener_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsDataReaderListener)

@given(instance=ddsMetamodel::DdsDataReaderListener_strategy)
def test_ddsmetamodel::ddsdatareaderlistener_listenedStatus_type(instance):
    assert isinstance(instance.listenedStatus, str)


@given(instance=ddsMetamodel::DdsDataReaderListener_strategy)
def test_ddsmetamodel::ddsdatareaderlistener_listenedStatus_setter(instance):
    original = instance.listenedStatus
    instance.listenedStatus = original
    assert instance.listenedStatus == original

@given(instance=ddsMetamodel::DdsDataReaderListener_strategy)
def test_ddsmetamodel::ddsdatareaderlistener_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ddsMetamodel::DdsDataReaderListener_strategy)
def test_ddsmetamodel::ddsdatareaderlistener_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ddsMetamodel::DdsSubscriberQosProfile_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddssubscriberqosprofile_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsSubscriberQosProfile)

@given(instance=ddsMetamodel::DdsSubscriberListener_strategy)
@settings(max_examples=50)
def test_ddsmetamodel::ddssubscriberlistener_instantiation(instance):
    assert isinstance(instance, ddsMetamodel::DdsSubscriberListener)

@given(instance=ddsMetamodel::DdsSubscriberListener_strategy)
def test_ddsmetamodel::ddssubscriberlistener_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ddsMetamodel::DdsSubscriberListener_strategy)
def test_ddsmetamodel::ddssubscriberlistener_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ddsMetamodel::DdsSubscriberListener_strategy)
def test_ddsmetamodel::ddssubscriberlistener_listenedStatus_type(instance):
    assert isinstance(instance.listenedStatus, str)


@given(instance=ddsMetamodel::DdsSubscriberListener_strategy)
def test_ddsmetamodel::ddssubscriberlistener_listenedStatus_setter(instance):
    original = instance.listenedStatus
    instance.listenedStatus = original
    assert instance.listenedStatus == original
