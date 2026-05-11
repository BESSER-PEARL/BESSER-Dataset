import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PeerToPeerPlatform,
    ddsm::KafkaCluster,
    ddsm::ZookeeperCluster,
    ddsm::CassandraCluster,
    ddsm::DDSM,
    MasterSlavePlatform,
    ddsm::HDFSCluster,
    ddsm::YarnCluster,
    ddsm::SparkCluster,
    ddsm::StormCluster,
    ddsm::Crontab,
    InternalComponent,
    ddsm::PeerNode,
    ddsm::MasterNode,
    ddsm::MasterSlavePlatform,
    ddsm::SlaveNode,
    ddsm::PeersQuorum,
    ddsm::PeerToPeerPlatform,
    ddsm::ClientNode,
    ExecutionPlatform,
    Port,
    ExternalComponent,
    ddsm::VM,
    ddsm::Artifact,
    ddsm::Property,
    ddsm::RequiredExecutionPlatform,
    ddsm::RequiredPort,
    Component,
    ddsm::ExternalComponent,
    ddsm::InternalComponent,
    ddsm::ProvidedExecutionPlatform,
    ddsm::ProvidedPort,
    CloudElement,
    ddsm::Port,
    ddsm::ExecutionPlatform,
    ddsm::Provider,
    ddsm::Relationship,
    ddsm::ExecutionBinding,
    ddsm::JobSubmission,
    ddsm::Component,
    ddsm::Resource,
    ddsm::CloudElement,
    ProviderType,
    VMSize,
    Language,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_peertopeerplatform_is_not_abstract():
    assert not inspect.isabstract(PeerToPeerPlatform)


def test_peertopeerplatform_constructor_exists():
    assert callable(PeerToPeerPlatform.__init__)


def test_peertopeerplatform_constructor_args():
    sig = inspect.signature(PeerToPeerPlatform.__init__)
    params = list(sig.parameters.keys())



def test_ddsm::kafkacluster_is_not_abstract():
    assert not inspect.isabstract(ddsm::KafkaCluster)


def test_ddsm::kafkacluster_constructor_exists():
    assert callable(ddsm::KafkaCluster.__init__)


def test_ddsm::kafkacluster_constructor_args():
    sig = inspect.signature(ddsm::KafkaCluster.__init__)
    params = list(sig.parameters.keys())



def test_ddsm::zookeepercluster_is_not_abstract():
    assert not inspect.isabstract(ddsm::ZookeeperCluster)


def test_ddsm::zookeepercluster_constructor_exists():
    assert callable(ddsm::ZookeeperCluster.__init__)


def test_ddsm::zookeepercluster_constructor_args():
    sig = inspect.signature(ddsm::ZookeeperCluster.__init__)
    params = list(sig.parameters.keys())
    assert "syncLimit" in params, "Missing parameter 'syncLimit'"
    assert "initLimit" in params, "Missing parameter 'initLimit'"
    assert "tickTime" in params, "Missing parameter 'tickTime'"

def test_ddsm::zookeepercluster_has_syncLimit():
    assert hasattr(ddsm::ZookeeperCluster, "syncLimit")
    descriptor = None
    for klass in ddsm::ZookeeperCluster.__mro__:
        if "syncLimit" in klass.__dict__:
            descriptor = klass.__dict__["syncLimit"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::zookeepercluster_has_initLimit():
    assert hasattr(ddsm::ZookeeperCluster, "initLimit")
    descriptor = None
    for klass in ddsm::ZookeeperCluster.__mro__:
        if "initLimit" in klass.__dict__:
            descriptor = klass.__dict__["initLimit"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::zookeepercluster_has_tickTime():
    assert hasattr(ddsm::ZookeeperCluster, "tickTime")
    descriptor = None
    for klass in ddsm::ZookeeperCluster.__mro__:
        if "tickTime" in klass.__dict__:
            descriptor = klass.__dict__["tickTime"]
            break
    assert isinstance(descriptor, property)



def test_ddsm::cassandracluster_is_not_abstract():
    assert not inspect.isabstract(ddsm::CassandraCluster)


def test_ddsm::cassandracluster_constructor_exists():
    assert callable(ddsm::CassandraCluster.__init__)


def test_ddsm::cassandracluster_constructor_args():
    sig = inspect.signature(ddsm::CassandraCluster.__init__)
    params = list(sig.parameters.keys())



def test_ddsm::ddsm_is_not_abstract():
    assert not inspect.isabstract(ddsm::DDSM)


def test_ddsm::ddsm_constructor_exists():
    assert callable(ddsm::DDSM.__init__)


def test_ddsm::ddsm_constructor_args():
    sig = inspect.signature(ddsm::DDSM.__init__)
    params = list(sig.parameters.keys())
    assert "modelId" in params, "Missing parameter 'modelId'"
    assert "description" in params, "Missing parameter 'description'"

def test_ddsm::ddsm_has_modelId():
    assert hasattr(ddsm::DDSM, "modelId")
    descriptor = None
    for klass in ddsm::DDSM.__mro__:
        if "modelId" in klass.__dict__:
            descriptor = klass.__dict__["modelId"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::ddsm_has_description():
    assert hasattr(ddsm::DDSM, "description")
    descriptor = None
    for klass in ddsm::DDSM.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_masterslaveplatform_is_not_abstract():
    assert not inspect.isabstract(MasterSlavePlatform)


def test_masterslaveplatform_constructor_exists():
    assert callable(MasterSlavePlatform.__init__)


def test_masterslaveplatform_constructor_args():
    sig = inspect.signature(MasterSlavePlatform.__init__)
    params = list(sig.parameters.keys())



def test_ddsm::hdfscluster_is_not_abstract():
    assert not inspect.isabstract(ddsm::HDFSCluster)


def test_ddsm::hdfscluster_constructor_exists():
    assert callable(ddsm::HDFSCluster.__init__)


def test_ddsm::hdfscluster_constructor_args():
    sig = inspect.signature(ddsm::HDFSCluster.__init__)
    params = list(sig.parameters.keys())



def test_ddsm::yarncluster_is_not_abstract():
    assert not inspect.isabstract(ddsm::YarnCluster)


def test_ddsm::yarncluster_constructor_exists():
    assert callable(ddsm::YarnCluster.__init__)


def test_ddsm::yarncluster_constructor_args():
    sig = inspect.signature(ddsm::YarnCluster.__init__)
    params = list(sig.parameters.keys())



def test_ddsm::sparkcluster_is_not_abstract():
    assert not inspect.isabstract(ddsm::SparkCluster)


def test_ddsm::sparkcluster_constructor_exists():
    assert callable(ddsm::SparkCluster.__init__)


def test_ddsm::sparkcluster_constructor_args():
    sig = inspect.signature(ddsm::SparkCluster.__init__)
    params = list(sig.parameters.keys())
    assert "driverCores" in params, "Missing parameter 'driverCores'"
    assert "sparkExecutorMemory" in params, "Missing parameter 'sparkExecutorMemory'"
    assert "maxResultSize" in params, "Missing parameter 'maxResultSize'"
    assert "UIPort" in params, "Missing parameter 'UIPort'"
    assert "driverMemory" in params, "Missing parameter 'driverMemory'"

def test_ddsm::sparkcluster_has_driverCores():
    assert hasattr(ddsm::SparkCluster, "driverCores")
    descriptor = None
    for klass in ddsm::SparkCluster.__mro__:
        if "driverCores" in klass.__dict__:
            descriptor = klass.__dict__["driverCores"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::sparkcluster_has_sparkExecutorMemory():
    assert hasattr(ddsm::SparkCluster, "sparkExecutorMemory")
    descriptor = None
    for klass in ddsm::SparkCluster.__mro__:
        if "sparkExecutorMemory" in klass.__dict__:
            descriptor = klass.__dict__["sparkExecutorMemory"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::sparkcluster_has_maxResultSize():
    assert hasattr(ddsm::SparkCluster, "maxResultSize")
    descriptor = None
    for klass in ddsm::SparkCluster.__mro__:
        if "maxResultSize" in klass.__dict__:
            descriptor = klass.__dict__["maxResultSize"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::sparkcluster_has_UIPort():
    assert hasattr(ddsm::SparkCluster, "UIPort")
    descriptor = None
    for klass in ddsm::SparkCluster.__mro__:
        if "UIPort" in klass.__dict__:
            descriptor = klass.__dict__["UIPort"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::sparkcluster_has_driverMemory():
    assert hasattr(ddsm::SparkCluster, "driverMemory")
    descriptor = None
    for klass in ddsm::SparkCluster.__mro__:
        if "driverMemory" in klass.__dict__:
            descriptor = klass.__dict__["driverMemory"]
            break
    assert isinstance(descriptor, property)



def test_ddsm::stormcluster_is_not_abstract():
    assert not inspect.isabstract(ddsm::StormCluster)


def test_ddsm::stormcluster_constructor_exists():
    assert callable(ddsm::StormCluster.__init__)


def test_ddsm::stormcluster_constructor_args():
    sig = inspect.signature(ddsm::StormCluster.__init__)
    params = list(sig.parameters.keys())
    assert "queueSize" in params, "Missing parameter 'queueSize'"
    assert "cpuCapacity" in params, "Missing parameter 'cpuCapacity'"
    assert "supervisorFrequency" in params, "Missing parameter 'supervisorFrequency'"
    assert "retryInterval" in params, "Missing parameter 'retryInterval'"
    assert "workerStartTimeout" in params, "Missing parameter 'workerStartTimeout'"
    assert "heartbeatFrequency" in params, "Missing parameter 'heartbeatFrequency'"
    assert "retryTimes" in params, "Missing parameter 'retryTimes'"
    assert "memoryCapacity" in params, "Missing parameter 'memoryCapacity'"
    assert "monitorFrequency" in params, "Missing parameter 'monitorFrequency'"
    assert "taskTimeout" in params, "Missing parameter 'taskTimeout'"

def test_ddsm::stormcluster_has_queueSize():
    assert hasattr(ddsm::StormCluster, "queueSize")
    descriptor = None
    for klass in ddsm::StormCluster.__mro__:
        if "queueSize" in klass.__dict__:
            descriptor = klass.__dict__["queueSize"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::stormcluster_has_cpuCapacity():
    assert hasattr(ddsm::StormCluster, "cpuCapacity")
    descriptor = None
    for klass in ddsm::StormCluster.__mro__:
        if "cpuCapacity" in klass.__dict__:
            descriptor = klass.__dict__["cpuCapacity"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::stormcluster_has_supervisorFrequency():
    assert hasattr(ddsm::StormCluster, "supervisorFrequency")
    descriptor = None
    for klass in ddsm::StormCluster.__mro__:
        if "supervisorFrequency" in klass.__dict__:
            descriptor = klass.__dict__["supervisorFrequency"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::stormcluster_has_retryInterval():
    assert hasattr(ddsm::StormCluster, "retryInterval")
    descriptor = None
    for klass in ddsm::StormCluster.__mro__:
        if "retryInterval" in klass.__dict__:
            descriptor = klass.__dict__["retryInterval"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::stormcluster_has_workerStartTimeout():
    assert hasattr(ddsm::StormCluster, "workerStartTimeout")
    descriptor = None
    for klass in ddsm::StormCluster.__mro__:
        if "workerStartTimeout" in klass.__dict__:
            descriptor = klass.__dict__["workerStartTimeout"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::stormcluster_has_heartbeatFrequency():
    assert hasattr(ddsm::StormCluster, "heartbeatFrequency")
    descriptor = None
    for klass in ddsm::StormCluster.__mro__:
        if "heartbeatFrequency" in klass.__dict__:
            descriptor = klass.__dict__["heartbeatFrequency"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::stormcluster_has_retryTimes():
    assert hasattr(ddsm::StormCluster, "retryTimes")
    descriptor = None
    for klass in ddsm::StormCluster.__mro__:
        if "retryTimes" in klass.__dict__:
            descriptor = klass.__dict__["retryTimes"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::stormcluster_has_memoryCapacity():
    assert hasattr(ddsm::StormCluster, "memoryCapacity")
    descriptor = None
    for klass in ddsm::StormCluster.__mro__:
        if "memoryCapacity" in klass.__dict__:
            descriptor = klass.__dict__["memoryCapacity"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::stormcluster_has_monitorFrequency():
    assert hasattr(ddsm::StormCluster, "monitorFrequency")
    descriptor = None
    for klass in ddsm::StormCluster.__mro__:
        if "monitorFrequency" in klass.__dict__:
            descriptor = klass.__dict__["monitorFrequency"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::stormcluster_has_taskTimeout():
    assert hasattr(ddsm::StormCluster, "taskTimeout")
    descriptor = None
    for klass in ddsm::StormCluster.__mro__:
        if "taskTimeout" in klass.__dict__:
            descriptor = klass.__dict__["taskTimeout"]
            break
    assert isinstance(descriptor, property)



def test_ddsm::crontab_is_not_abstract():
    assert not inspect.isabstract(ddsm::Crontab)


def test_ddsm::crontab_constructor_exists():
    assert callable(ddsm::Crontab.__init__)


def test_ddsm::crontab_constructor_args():
    sig = inspect.signature(ddsm::Crontab.__init__)
    params = list(sig.parameters.keys())
    assert "min" in params, "Missing parameter 'min'"
    assert "dayOfWeek" in params, "Missing parameter 'dayOfWeek'"
    assert "month" in params, "Missing parameter 'month'"
    assert "dayOfMonth" in params, "Missing parameter 'dayOfMonth'"
    assert "hour" in params, "Missing parameter 'hour'"

def test_ddsm::crontab_has_min():
    assert hasattr(ddsm::Crontab, "min")
    descriptor = None
    for klass in ddsm::Crontab.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::crontab_has_dayOfWeek():
    assert hasattr(ddsm::Crontab, "dayOfWeek")
    descriptor = None
    for klass in ddsm::Crontab.__mro__:
        if "dayOfWeek" in klass.__dict__:
            descriptor = klass.__dict__["dayOfWeek"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::crontab_has_month():
    assert hasattr(ddsm::Crontab, "month")
    descriptor = None
    for klass in ddsm::Crontab.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::crontab_has_dayOfMonth():
    assert hasattr(ddsm::Crontab, "dayOfMonth")
    descriptor = None
    for klass in ddsm::Crontab.__mro__:
        if "dayOfMonth" in klass.__dict__:
            descriptor = klass.__dict__["dayOfMonth"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::crontab_has_hour():
    assert hasattr(ddsm::Crontab, "hour")
    descriptor = None
    for klass in ddsm::Crontab.__mro__:
        if "hour" in klass.__dict__:
            descriptor = klass.__dict__["hour"]
            break
    assert isinstance(descriptor, property)



def test_internalcomponent_is_not_abstract():
    assert not inspect.isabstract(InternalComponent)


def test_internalcomponent_constructor_exists():
    assert callable(InternalComponent.__init__)


def test_internalcomponent_constructor_args():
    sig = inspect.signature(InternalComponent.__init__)
    params = list(sig.parameters.keys())



def test_ddsm::peernode_is_not_abstract():
    assert not inspect.isabstract(ddsm::PeerNode)


def test_ddsm::peernode_constructor_exists():
    assert callable(ddsm::PeerNode.__init__)


def test_ddsm::peernode_constructor_args():
    sig = inspect.signature(ddsm::PeerNode.__init__)
    params = list(sig.parameters.keys())



def test_ddsm::masternode_is_not_abstract():
    assert not inspect.isabstract(ddsm::MasterNode)


def test_ddsm::masternode_constructor_exists():
    assert callable(ddsm::MasterNode.__init__)


def test_ddsm::masternode_constructor_args():
    sig = inspect.signature(ddsm::MasterNode.__init__)
    params = list(sig.parameters.keys())



def test_ddsm::masterslaveplatform_is_not_abstract():
    assert not inspect.isabstract(ddsm::MasterSlavePlatform)


def test_ddsm::masterslaveplatform_constructor_exists():
    assert callable(ddsm::MasterSlavePlatform.__init__)


def test_ddsm::masterslaveplatform_constructor_args():
    sig = inspect.signature(ddsm::MasterSlavePlatform.__init__)
    params = list(sig.parameters.keys())



def test_ddsm::slavenode_is_not_abstract():
    assert not inspect.isabstract(ddsm::SlaveNode)


def test_ddsm::slavenode_constructor_exists():
    assert callable(ddsm::SlaveNode.__init__)


def test_ddsm::slavenode_constructor_args():
    sig = inspect.signature(ddsm::SlaveNode.__init__)
    params = list(sig.parameters.keys())



def test_ddsm::peersquorum_is_not_abstract():
    assert not inspect.isabstract(ddsm::PeersQuorum)


def test_ddsm::peersquorum_constructor_exists():
    assert callable(ddsm::PeersQuorum.__init__)


def test_ddsm::peersquorum_constructor_args():
    sig = inspect.signature(ddsm::PeersQuorum.__init__)
    params = list(sig.parameters.keys())



def test_ddsm::peertopeerplatform_is_not_abstract():
    assert not inspect.isabstract(ddsm::PeerToPeerPlatform)


def test_ddsm::peertopeerplatform_constructor_exists():
    assert callable(ddsm::PeerToPeerPlatform.__init__)


def test_ddsm::peertopeerplatform_constructor_args():
    sig = inspect.signature(ddsm::PeerToPeerPlatform.__init__)
    params = list(sig.parameters.keys())



def test_ddsm::clientnode_is_not_abstract():
    assert not inspect.isabstract(ddsm::ClientNode)


def test_ddsm::clientnode_constructor_exists():
    assert callable(ddsm::ClientNode.__init__)


def test_ddsm::clientnode_constructor_args():
    sig = inspect.signature(ddsm::ClientNode.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfSubmissions" in params, "Missing parameter 'numberOfSubmissions'"
    assert "skipRunningJob" in params, "Missing parameter 'skipRunningJob'"

def test_ddsm::clientnode_has_numberOfSubmissions():
    assert hasattr(ddsm::ClientNode, "numberOfSubmissions")
    descriptor = None
    for klass in ddsm::ClientNode.__mro__:
        if "numberOfSubmissions" in klass.__dict__:
            descriptor = klass.__dict__["numberOfSubmissions"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::clientnode_has_skipRunningJob():
    assert hasattr(ddsm::ClientNode, "skipRunningJob")
    descriptor = None
    for klass in ddsm::ClientNode.__mro__:
        if "skipRunningJob" in klass.__dict__:
            descriptor = klass.__dict__["skipRunningJob"]
            break
    assert isinstance(descriptor, property)



def test_executionplatform_is_not_abstract():
    assert not inspect.isabstract(ExecutionPlatform)


def test_executionplatform_constructor_exists():
    assert callable(ExecutionPlatform.__init__)


def test_executionplatform_constructor_args():
    sig = inspect.signature(ExecutionPlatform.__init__)
    params = list(sig.parameters.keys())



def test_port_is_not_abstract():
    assert not inspect.isabstract(Port)


def test_port_constructor_exists():
    assert callable(Port.__init__)


def test_port_constructor_args():
    sig = inspect.signature(Port.__init__)
    params = list(sig.parameters.keys())



def test_externalcomponent_is_not_abstract():
    assert not inspect.isabstract(ExternalComponent)


def test_externalcomponent_constructor_exists():
    assert callable(ExternalComponent.__init__)


def test_externalcomponent_constructor_args():
    sig = inspect.signature(ExternalComponent.__init__)
    params = list(sig.parameters.keys())



def test_ddsm::vm_is_not_abstract():
    assert not inspect.isabstract(ddsm::VM)


def test_ddsm::vm_constructor_exists():
    assert callable(ddsm::VM.__init__)


def test_ddsm::vm_constructor_args():
    sig = inspect.signature(ddsm::VM.__init__)
    params = list(sig.parameters.keys())
    assert "providerSpecificTypeName" in params, "Missing parameter 'providerSpecificTypeName'"
    assert "maxRam" in params, "Missing parameter 'maxRam'"
    assert "imageId" in params, "Missing parameter 'imageId'"
    assert "genericSize" in params, "Missing parameter 'genericSize'"
    assert "is64os" in params, "Missing parameter 'is64os'"
    assert "os" in params, "Missing parameter 'os'"
    assert "sshKey" in params, "Missing parameter 'sshKey'"
    assert "minStorage" in params, "Missing parameter 'minStorage'"
    assert "minCores" in params, "Missing parameter 'minCores'"
    assert "maxCores" in params, "Missing parameter 'maxCores'"
    assert "minRam" in params, "Missing parameter 'minRam'"
    assert "publicPorts" in params, "Missing parameter 'publicPorts'"
    assert "publicAddress" in params, "Missing parameter 'publicAddress'"
    assert "instances" in params, "Missing parameter 'instances'"
    assert "maxStorage" in params, "Missing parameter 'maxStorage'"
    assert "privateKey" in params, "Missing parameter 'privateKey'"
    assert "securityGroup" in params, "Missing parameter 'securityGroup'"

def test_ddsm::vm_has_providerSpecificTypeName():
    assert hasattr(ddsm::VM, "providerSpecificTypeName")
    descriptor = None
    for klass in ddsm::VM.__mro__:
        if "providerSpecificTypeName" in klass.__dict__:
            descriptor = klass.__dict__["providerSpecificTypeName"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::vm_has_maxRam():
    assert hasattr(ddsm::VM, "maxRam")
    descriptor = None
    for klass in ddsm::VM.__mro__:
        if "maxRam" in klass.__dict__:
            descriptor = klass.__dict__["maxRam"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::vm_has_imageId():
    assert hasattr(ddsm::VM, "imageId")
    descriptor = None
    for klass in ddsm::VM.__mro__:
        if "imageId" in klass.__dict__:
            descriptor = klass.__dict__["imageId"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::vm_has_genericSize():
    assert hasattr(ddsm::VM, "genericSize")
    descriptor = None
    for klass in ddsm::VM.__mro__:
        if "genericSize" in klass.__dict__:
            descriptor = klass.__dict__["genericSize"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::vm_has_is64os():
    assert hasattr(ddsm::VM, "is64os")
    descriptor = None
    for klass in ddsm::VM.__mro__:
        if "is64os" in klass.__dict__:
            descriptor = klass.__dict__["is64os"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::vm_has_os():
    assert hasattr(ddsm::VM, "os")
    descriptor = None
    for klass in ddsm::VM.__mro__:
        if "os" in klass.__dict__:
            descriptor = klass.__dict__["os"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::vm_has_sshKey():
    assert hasattr(ddsm::VM, "sshKey")
    descriptor = None
    for klass in ddsm::VM.__mro__:
        if "sshKey" in klass.__dict__:
            descriptor = klass.__dict__["sshKey"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::vm_has_minStorage():
    assert hasattr(ddsm::VM, "minStorage")
    descriptor = None
    for klass in ddsm::VM.__mro__:
        if "minStorage" in klass.__dict__:
            descriptor = klass.__dict__["minStorage"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::vm_has_minCores():
    assert hasattr(ddsm::VM, "minCores")
    descriptor = None
    for klass in ddsm::VM.__mro__:
        if "minCores" in klass.__dict__:
            descriptor = klass.__dict__["minCores"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::vm_has_maxCores():
    assert hasattr(ddsm::VM, "maxCores")
    descriptor = None
    for klass in ddsm::VM.__mro__:
        if "maxCores" in klass.__dict__:
            descriptor = klass.__dict__["maxCores"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::vm_has_minRam():
    assert hasattr(ddsm::VM, "minRam")
    descriptor = None
    for klass in ddsm::VM.__mro__:
        if "minRam" in klass.__dict__:
            descriptor = klass.__dict__["minRam"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::vm_has_publicPorts():
    assert hasattr(ddsm::VM, "publicPorts")
    descriptor = None
    for klass in ddsm::VM.__mro__:
        if "publicPorts" in klass.__dict__:
            descriptor = klass.__dict__["publicPorts"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::vm_has_publicAddress():
    assert hasattr(ddsm::VM, "publicAddress")
    descriptor = None
    for klass in ddsm::VM.__mro__:
        if "publicAddress" in klass.__dict__:
            descriptor = klass.__dict__["publicAddress"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::vm_has_instances():
    assert hasattr(ddsm::VM, "instances")
    descriptor = None
    for klass in ddsm::VM.__mro__:
        if "instances" in klass.__dict__:
            descriptor = klass.__dict__["instances"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::vm_has_maxStorage():
    assert hasattr(ddsm::VM, "maxStorage")
    descriptor = None
    for klass in ddsm::VM.__mro__:
        if "maxStorage" in klass.__dict__:
            descriptor = klass.__dict__["maxStorage"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::vm_has_privateKey():
    assert hasattr(ddsm::VM, "privateKey")
    descriptor = None
    for klass in ddsm::VM.__mro__:
        if "privateKey" in klass.__dict__:
            descriptor = klass.__dict__["privateKey"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::vm_has_securityGroup():
    assert hasattr(ddsm::VM, "securityGroup")
    descriptor = None
    for klass in ddsm::VM.__mro__:
        if "securityGroup" in klass.__dict__:
            descriptor = klass.__dict__["securityGroup"]
            break
    assert isinstance(descriptor, property)



def test_ddsm::artifact_is_not_abstract():
    assert not inspect.isabstract(ddsm::Artifact)


def test_ddsm::artifact_constructor_exists():
    assert callable(ddsm::Artifact.__init__)


def test_ddsm::artifact_constructor_args():
    sig = inspect.signature(ddsm::Artifact.__init__)
    params = list(sig.parameters.keys())
    assert "arguments" in params, "Missing parameter 'arguments'"
    assert "language" in params, "Missing parameter 'language'"
    assert "resources" in params, "Missing parameter 'resources'"
    assert "artifactPath" in params, "Missing parameter 'artifactPath'"

def test_ddsm::artifact_has_arguments():
    assert hasattr(ddsm::Artifact, "arguments")
    descriptor = None
    for klass in ddsm::Artifact.__mro__:
        if "arguments" in klass.__dict__:
            descriptor = klass.__dict__["arguments"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::artifact_has_language():
    assert hasattr(ddsm::Artifact, "language")
    descriptor = None
    for klass in ddsm::Artifact.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::artifact_has_resources():
    assert hasattr(ddsm::Artifact, "resources")
    descriptor = None
    for klass in ddsm::Artifact.__mro__:
        if "resources" in klass.__dict__:
            descriptor = klass.__dict__["resources"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::artifact_has_artifactPath():
    assert hasattr(ddsm::Artifact, "artifactPath")
    descriptor = None
    for klass in ddsm::Artifact.__mro__:
        if "artifactPath" in klass.__dict__:
            descriptor = klass.__dict__["artifactPath"]
            break
    assert isinstance(descriptor, property)



def test_ddsm::property_is_not_abstract():
    assert not inspect.isabstract(ddsm::Property)


def test_ddsm::property_constructor_exists():
    assert callable(ddsm::Property.__init__)


def test_ddsm::property_constructor_args():
    sig = inspect.signature(ddsm::Property.__init__)
    params = list(sig.parameters.keys())
    assert "propertyId" in params, "Missing parameter 'propertyId'"
    assert "value" in params, "Missing parameter 'value'"

def test_ddsm::property_has_propertyId():
    assert hasattr(ddsm::Property, "propertyId")
    descriptor = None
    for klass in ddsm::Property.__mro__:
        if "propertyId" in klass.__dict__:
            descriptor = klass.__dict__["propertyId"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::property_has_value():
    assert hasattr(ddsm::Property, "value")
    descriptor = None
    for klass in ddsm::Property.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ddsm::requiredexecutionplatform_is_not_abstract():
    assert not inspect.isabstract(ddsm::RequiredExecutionPlatform)


def test_ddsm::requiredexecutionplatform_constructor_exists():
    assert callable(ddsm::RequiredExecutionPlatform.__init__)


def test_ddsm::requiredexecutionplatform_constructor_args():
    sig = inspect.signature(ddsm::RequiredExecutionPlatform.__init__)
    params = list(sig.parameters.keys())
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"

def test_ddsm::requiredexecutionplatform_has_isMandatory():
    assert hasattr(ddsm::RequiredExecutionPlatform, "isMandatory")
    descriptor = None
    for klass in ddsm::RequiredExecutionPlatform.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)



def test_ddsm::requiredport_is_not_abstract():
    assert not inspect.isabstract(ddsm::RequiredPort)


def test_ddsm::requiredport_constructor_exists():
    assert callable(ddsm::RequiredPort.__init__)


def test_ddsm::requiredport_constructor_args():
    sig = inspect.signature(ddsm::RequiredPort.__init__)
    params = list(sig.parameters.keys())
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"

def test_ddsm::requiredport_has_isMandatory():
    assert hasattr(ddsm::RequiredPort, "isMandatory")
    descriptor = None
    for klass in ddsm::RequiredPort.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)



def test_component_is_not_abstract():
    assert not inspect.isabstract(Component)


def test_component_constructor_exists():
    assert callable(Component.__init__)


def test_component_constructor_args():
    sig = inspect.signature(Component.__init__)
    params = list(sig.parameters.keys())



def test_ddsm::externalcomponent_is_not_abstract():
    assert not inspect.isabstract(ddsm::ExternalComponent)


def test_ddsm::externalcomponent_constructor_exists():
    assert callable(ddsm::ExternalComponent.__init__)


def test_ddsm::externalcomponent_constructor_args():
    sig = inspect.signature(ddsm::ExternalComponent.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "region" in params, "Missing parameter 'region'"
    assert "login" in params, "Missing parameter 'login'"
    assert "serviceType" in params, "Missing parameter 'serviceType'"
    assert "endPoint" in params, "Missing parameter 'endPoint'"
    assert "password" in params, "Missing parameter 'password'"

def test_ddsm::externalcomponent_has_location():
    assert hasattr(ddsm::ExternalComponent, "location")
    descriptor = None
    for klass in ddsm::ExternalComponent.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::externalcomponent_has_region():
    assert hasattr(ddsm::ExternalComponent, "region")
    descriptor = None
    for klass in ddsm::ExternalComponent.__mro__:
        if "region" in klass.__dict__:
            descriptor = klass.__dict__["region"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::externalcomponent_has_login():
    assert hasattr(ddsm::ExternalComponent, "login")
    descriptor = None
    for klass in ddsm::ExternalComponent.__mro__:
        if "login" in klass.__dict__:
            descriptor = klass.__dict__["login"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::externalcomponent_has_serviceType():
    assert hasattr(ddsm::ExternalComponent, "serviceType")
    descriptor = None
    for klass in ddsm::ExternalComponent.__mro__:
        if "serviceType" in klass.__dict__:
            descriptor = klass.__dict__["serviceType"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::externalcomponent_has_endPoint():
    assert hasattr(ddsm::ExternalComponent, "endPoint")
    descriptor = None
    for klass in ddsm::ExternalComponent.__mro__:
        if "endPoint" in klass.__dict__:
            descriptor = klass.__dict__["endPoint"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::externalcomponent_has_password():
    assert hasattr(ddsm::ExternalComponent, "password")
    descriptor = None
    for klass in ddsm::ExternalComponent.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)



def test_ddsm::internalcomponent_is_not_abstract():
    assert not inspect.isabstract(ddsm::InternalComponent)


def test_ddsm::internalcomponent_constructor_exists():
    assert callable(ddsm::InternalComponent.__init__)


def test_ddsm::internalcomponent_constructor_args():
    sig = inspect.signature(ddsm::InternalComponent.__init__)
    params = list(sig.parameters.keys())



def test_ddsm::providedexecutionplatform_is_not_abstract():
    assert not inspect.isabstract(ddsm::ProvidedExecutionPlatform)


def test_ddsm::providedexecutionplatform_constructor_exists():
    assert callable(ddsm::ProvidedExecutionPlatform.__init__)


def test_ddsm::providedexecutionplatform_constructor_args():
    sig = inspect.signature(ddsm::ProvidedExecutionPlatform.__init__)
    params = list(sig.parameters.keys())



def test_ddsm::providedport_is_not_abstract():
    assert not inspect.isabstract(ddsm::ProvidedPort)


def test_ddsm::providedport_constructor_exists():
    assert callable(ddsm::ProvidedPort.__init__)


def test_ddsm::providedport_constructor_args():
    sig = inspect.signature(ddsm::ProvidedPort.__init__)
    params = list(sig.parameters.keys())



def test_cloudelement_is_not_abstract():
    assert not inspect.isabstract(CloudElement)


def test_cloudelement_constructor_exists():
    assert callable(CloudElement.__init__)


def test_cloudelement_constructor_args():
    sig = inspect.signature(CloudElement.__init__)
    params = list(sig.parameters.keys())



def test_ddsm::port_is_not_abstract():
    assert not inspect.isabstract(ddsm::Port)


def test_ddsm::port_constructor_exists():
    assert callable(ddsm::Port.__init__)


def test_ddsm::port_constructor_args():
    sig = inspect.signature(ddsm::Port.__init__)
    params = list(sig.parameters.keys())
    assert "isLocal" in params, "Missing parameter 'isLocal'"
    assert "portNumber" in params, "Missing parameter 'portNumber'"

def test_ddsm::port_has_isLocal():
    assert hasattr(ddsm::Port, "isLocal")
    descriptor = None
    for klass in ddsm::Port.__mro__:
        if "isLocal" in klass.__dict__:
            descriptor = klass.__dict__["isLocal"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::port_has_portNumber():
    assert hasattr(ddsm::Port, "portNumber")
    descriptor = None
    for klass in ddsm::Port.__mro__:
        if "portNumber" in klass.__dict__:
            descriptor = klass.__dict__["portNumber"]
            break
    assert isinstance(descriptor, property)



def test_ddsm::executionplatform_is_not_abstract():
    assert not inspect.isabstract(ddsm::ExecutionPlatform)


def test_ddsm::executionplatform_constructor_exists():
    assert callable(ddsm::ExecutionPlatform.__init__)


def test_ddsm::executionplatform_constructor_args():
    sig = inspect.signature(ddsm::ExecutionPlatform.__init__)
    params = list(sig.parameters.keys())



def test_ddsm::provider_is_not_abstract():
    assert not inspect.isabstract(ddsm::Provider)


def test_ddsm::provider_constructor_exists():
    assert callable(ddsm::Provider.__init__)


def test_ddsm::provider_constructor_args():
    sig = inspect.signature(ddsm::Provider.__init__)
    params = list(sig.parameters.keys())
    assert "credentialsPath" in params, "Missing parameter 'credentialsPath'"
    assert "type" in params, "Missing parameter 'type'"

def test_ddsm::provider_has_credentialsPath():
    assert hasattr(ddsm::Provider, "credentialsPath")
    descriptor = None
    for klass in ddsm::Provider.__mro__:
        if "credentialsPath" in klass.__dict__:
            descriptor = klass.__dict__["credentialsPath"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::provider_has_type():
    assert hasattr(ddsm::Provider, "type")
    descriptor = None
    for klass in ddsm::Provider.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_ddsm::relationship_is_not_abstract():
    assert not inspect.isabstract(ddsm::Relationship)


def test_ddsm::relationship_constructor_exists():
    assert callable(ddsm::Relationship.__init__)


def test_ddsm::relationship_constructor_args():
    sig = inspect.signature(ddsm::Relationship.__init__)
    params = list(sig.parameters.keys())



def test_ddsm::executionbinding_is_not_abstract():
    assert not inspect.isabstract(ddsm::ExecutionBinding)


def test_ddsm::executionbinding_constructor_exists():
    assert callable(ddsm::ExecutionBinding.__init__)


def test_ddsm::executionbinding_constructor_args():
    sig = inspect.signature(ddsm::ExecutionBinding.__init__)
    params = list(sig.parameters.keys())



def test_ddsm::jobsubmission_is_not_abstract():
    assert not inspect.isabstract(ddsm::JobSubmission)


def test_ddsm::jobsubmission_constructor_exists():
    assert callable(ddsm::JobSubmission.__init__)


def test_ddsm::jobsubmission_constructor_args():
    sig = inspect.signature(ddsm::JobSubmission.__init__)
    params = list(sig.parameters.keys())
    assert "mainClass" in params, "Missing parameter 'mainClass'"
    assert "artifactUrl" in params, "Missing parameter 'artifactUrl'"
    assert "applicationArguments" in params, "Missing parameter 'applicationArguments'"

def test_ddsm::jobsubmission_has_mainClass():
    assert hasattr(ddsm::JobSubmission, "mainClass")
    descriptor = None
    for klass in ddsm::JobSubmission.__mro__:
        if "mainClass" in klass.__dict__:
            descriptor = klass.__dict__["mainClass"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::jobsubmission_has_artifactUrl():
    assert hasattr(ddsm::JobSubmission, "artifactUrl")
    descriptor = None
    for klass in ddsm::JobSubmission.__mro__:
        if "artifactUrl" in klass.__dict__:
            descriptor = klass.__dict__["artifactUrl"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::jobsubmission_has_applicationArguments():
    assert hasattr(ddsm::JobSubmission, "applicationArguments")
    descriptor = None
    for klass in ddsm::JobSubmission.__mro__:
        if "applicationArguments" in klass.__dict__:
            descriptor = klass.__dict__["applicationArguments"]
            break
    assert isinstance(descriptor, property)



def test_ddsm::component_is_not_abstract():
    assert not inspect.isabstract(ddsm::Component)


def test_ddsm::component_constructor_exists():
    assert callable(ddsm::Component.__init__)


def test_ddsm::component_constructor_args():
    sig = inspect.signature(ddsm::Component.__init__)
    params = list(sig.parameters.keys())



def test_ddsm::resource_is_not_abstract():
    assert not inspect.isabstract(ddsm::Resource)


def test_ddsm::resource_constructor_exists():
    assert callable(ddsm::Resource.__init__)


def test_ddsm::resource_constructor_args():
    sig = inspect.signature(ddsm::Resource.__init__)
    params = list(sig.parameters.keys())
    assert "resourceId" in params, "Missing parameter 'resourceId'"

def test_ddsm::resource_has_resourceId():
    assert hasattr(ddsm::Resource, "resourceId")
    descriptor = None
    for klass in ddsm::Resource.__mro__:
        if "resourceId" in klass.__dict__:
            descriptor = klass.__dict__["resourceId"]
            break
    assert isinstance(descriptor, property)



def test_ddsm::cloudelement_is_not_abstract():
    assert not inspect.isabstract(ddsm::CloudElement)


def test_ddsm::cloudelement_constructor_exists():
    assert callable(ddsm::CloudElement.__init__)


def test_ddsm::cloudelement_constructor_args():
    sig = inspect.signature(ddsm::CloudElement.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "elementId" in params, "Missing parameter 'elementId'"

def test_ddsm::cloudelement_has_description():
    assert hasattr(ddsm::CloudElement, "description")
    descriptor = None
    for klass in ddsm::CloudElement.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_ddsm::cloudelement_has_elementId():
    assert hasattr(ddsm::CloudElement, "elementId")
    descriptor = None
    for klass in ddsm::CloudElement.__mro__:
        if "elementId" in klass.__dict__:
            descriptor = klass.__dict__["elementId"]
            break
    assert isinstance(descriptor, property)

def test_providertype_exists():
    # Check that the Enumeration exists
    assert ProviderType is not None

def test_providertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProviderType]
    expected_literals = [
        "FCO",
        "Openstack",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProviderType"

def test_vmsize_exists():
    # Check that the Enumeration exists
    assert VMSize is not None

def test_vmsize_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VMSize]
    expected_literals = [
        "Large",
        "Medium",
        "Small",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VMSize"

def test_language_exists():
    # Check that the Enumeration exists
    assert Language is not None

def test_language_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Language]
    expected_literals = [
        "BASH",
        "JAVA",
        "PYTHON",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Language"


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
PeerToPeerPlatform_strategy = st.builds(
    PeerToPeerPlatform,
)
ddsm::KafkaCluster_strategy = st.builds(
    ddsm::KafkaCluster,
)
ddsm::ZookeeperCluster_strategy = st.builds(
    ddsm::ZookeeperCluster,
    syncLimit=
        st.integers(),
    initLimit=
        st.integers(),
    tickTime=
        st.integers()
)
ddsm::CassandraCluster_strategy = st.builds(
    ddsm::CassandraCluster,
)
ddsm::DDSM_strategy = st.builds(
    ddsm::DDSM,
    modelId=
        safe_text,
    description=
        safe_text
)
MasterSlavePlatform_strategy = st.builds(
    MasterSlavePlatform,
)
ddsm::HDFSCluster_strategy = st.builds(
    ddsm::HDFSCluster,
)
ddsm::YarnCluster_strategy = st.builds(
    ddsm::YarnCluster,
)
ddsm::SparkCluster_strategy = st.builds(
    ddsm::SparkCluster,
    driverCores=
        st.integers(),
    sparkExecutorMemory=
        st.integers(),
    maxResultSize=
        st.integers(),
    UIPort=
        st.integers(),
    driverMemory=
        st.integers()
)
ddsm::StormCluster_strategy = st.builds(
    ddsm::StormCluster,
    queueSize=
        st.integers(),
    cpuCapacity=
        st.integers(),
    supervisorFrequency=
        st.integers(),
    retryInterval=
        st.integers(),
    workerStartTimeout=
        st.integers(),
    heartbeatFrequency=
        st.integers(),
    retryTimes=
        st.integers(),
    memoryCapacity=
        st.integers(),
    monitorFrequency=
        st.integers(),
    taskTimeout=
        st.integers()
)
ddsm::Crontab_strategy = st.builds(
    ddsm::Crontab,
    min=
        st.integers(),
    dayOfWeek=
        st.integers(),
    month=
        st.integers(),
    dayOfMonth=
        st.integers(),
    hour=
        st.integers()
)
InternalComponent_strategy = st.builds(
    InternalComponent,
)
ddsm::PeerNode_strategy = st.builds(
    ddsm::PeerNode,
)
ddsm::MasterNode_strategy = st.builds(
    ddsm::MasterNode,
)
ddsm::MasterSlavePlatform_strategy = st.builds(
    ddsm::MasterSlavePlatform,
)
ddsm::SlaveNode_strategy = st.builds(
    ddsm::SlaveNode,
)
ddsm::PeersQuorum_strategy = st.builds(
    ddsm::PeersQuorum,
)
ddsm::PeerToPeerPlatform_strategy = st.builds(
    ddsm::PeerToPeerPlatform,
)
ddsm::ClientNode_strategy = st.builds(
    ddsm::ClientNode,
    numberOfSubmissions=
        st.integers(),
    skipRunningJob=
        st.booleans()
)
ExecutionPlatform_strategy = st.builds(
    ExecutionPlatform,
)
Port_strategy = st.builds(
    Port,
)
ExternalComponent_strategy = st.builds(
    ExternalComponent,
)
ddsm::VM_strategy = st.builds(
    ddsm::VM,
    providerSpecificTypeName=
        safe_text,
    maxRam=
        safe_text,
    imageId=
        safe_text,
    genericSize=
        safe_text,
    is64os=
        safe_text,
    os=
        safe_text,
    sshKey=
        safe_text,
    minStorage=
        safe_text,
    minCores=
        safe_text,
    maxCores=
        safe_text,
    minRam=
        safe_text,
    publicPorts=
        st.integers(),
    publicAddress=
        safe_text,
    instances=
        st.integers(),
    maxStorage=
        safe_text,
    privateKey=
        safe_text,
    securityGroup=
        safe_text
)
ddsm::Artifact_strategy = st.builds(
    ddsm::Artifact,
    arguments=
        safe_text,
    language=
        safe_text,
    resources=
        safe_text,
    artifactPath=
        safe_text
)
ddsm::Property_strategy = st.builds(
    ddsm::Property,
    propertyId=
        safe_text,
    value=
        safe_text
)
ddsm::RequiredExecutionPlatform_strategy = st.builds(
    ddsm::RequiredExecutionPlatform,
    isMandatory=
        st.booleans()
)
ddsm::RequiredPort_strategy = st.builds(
    ddsm::RequiredPort,
    isMandatory=
        st.booleans()
)
Component_strategy = st.builds(
    Component,
)
ddsm::ExternalComponent_strategy = st.builds(
    ddsm::ExternalComponent,
    location=
        safe_text,
    region=
        safe_text,
    login=
        safe_text,
    serviceType=
        safe_text,
    endPoint=
        safe_text,
    password=
        safe_text
)
ddsm::InternalComponent_strategy = st.builds(
    ddsm::InternalComponent,
)
ddsm::ProvidedExecutionPlatform_strategy = st.builds(
    ddsm::ProvidedExecutionPlatform,
)
ddsm::ProvidedPort_strategy = st.builds(
    ddsm::ProvidedPort,
)
CloudElement_strategy = st.builds(
    CloudElement,
)
ddsm::Port_strategy = st.builds(
    ddsm::Port,
    isLocal=
        st.booleans(),
    portNumber=
        safe_text
)
ddsm::ExecutionPlatform_strategy = st.builds(
    ddsm::ExecutionPlatform,
)
ddsm::Provider_strategy = st.builds(
    ddsm::Provider,
    credentialsPath=
        safe_text,
    type=
        safe_text
)
ddsm::Relationship_strategy = st.builds(
    ddsm::Relationship,
)
ddsm::ExecutionBinding_strategy = st.builds(
    ddsm::ExecutionBinding,
)
ddsm::JobSubmission_strategy = st.builds(
    ddsm::JobSubmission,
    mainClass=
        safe_text,
    artifactUrl=
        safe_text,
    applicationArguments=
        safe_text
)
ddsm::Component_strategy = st.builds(
    ddsm::Component,
)
ddsm::Resource_strategy = st.builds(
    ddsm::Resource,
    resourceId=
        safe_text
)
ddsm::CloudElement_strategy = st.builds(
    ddsm::CloudElement,
    description=
        safe_text,
    elementId=
        safe_text
)

@given(instance=PeerToPeerPlatform_strategy)
@settings(max_examples=50)
def test_peertopeerplatform_instantiation(instance):
    assert isinstance(instance, PeerToPeerPlatform)

@given(instance=ddsm::KafkaCluster_strategy)
@settings(max_examples=50)
def test_ddsm::kafkacluster_instantiation(instance):
    assert isinstance(instance, ddsm::KafkaCluster)

@given(instance=ddsm::ZookeeperCluster_strategy)
@settings(max_examples=50)
def test_ddsm::zookeepercluster_instantiation(instance):
    assert isinstance(instance, ddsm::ZookeeperCluster)

@given(instance=ddsm::ZookeeperCluster_strategy)
def test_ddsm::zookeepercluster_syncLimit_type(instance):
    assert isinstance(instance.syncLimit, int)


@given(instance=ddsm::ZookeeperCluster_strategy)
def test_ddsm::zookeepercluster_syncLimit_setter(instance):
    original = instance.syncLimit
    instance.syncLimit = original
    assert instance.syncLimit == original

@given(instance=ddsm::ZookeeperCluster_strategy)
def test_ddsm::zookeepercluster_initLimit_type(instance):
    assert isinstance(instance.initLimit, int)


@given(instance=ddsm::ZookeeperCluster_strategy)
def test_ddsm::zookeepercluster_initLimit_setter(instance):
    original = instance.initLimit
    instance.initLimit = original
    assert instance.initLimit == original

@given(instance=ddsm::ZookeeperCluster_strategy)
def test_ddsm::zookeepercluster_tickTime_type(instance):
    assert isinstance(instance.tickTime, int)


@given(instance=ddsm::ZookeeperCluster_strategy)
def test_ddsm::zookeepercluster_tickTime_setter(instance):
    original = instance.tickTime
    instance.tickTime = original
    assert instance.tickTime == original

@given(instance=ddsm::CassandraCluster_strategy)
@settings(max_examples=50)
def test_ddsm::cassandracluster_instantiation(instance):
    assert isinstance(instance, ddsm::CassandraCluster)

@given(instance=ddsm::DDSM_strategy)
@settings(max_examples=50)
def test_ddsm::ddsm_instantiation(instance):
    assert isinstance(instance, ddsm::DDSM)

@given(instance=ddsm::DDSM_strategy)
def test_ddsm::ddsm_modelId_type(instance):
    assert isinstance(instance.modelId, str)


@given(instance=ddsm::DDSM_strategy)
def test_ddsm::ddsm_modelId_setter(instance):
    original = instance.modelId
    instance.modelId = original
    assert instance.modelId == original

@given(instance=ddsm::DDSM_strategy)
def test_ddsm::ddsm_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=ddsm::DDSM_strategy)
def test_ddsm::ddsm_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=MasterSlavePlatform_strategy)
@settings(max_examples=50)
def test_masterslaveplatform_instantiation(instance):
    assert isinstance(instance, MasterSlavePlatform)

@given(instance=ddsm::HDFSCluster_strategy)
@settings(max_examples=50)
def test_ddsm::hdfscluster_instantiation(instance):
    assert isinstance(instance, ddsm::HDFSCluster)

@given(instance=ddsm::YarnCluster_strategy)
@settings(max_examples=50)
def test_ddsm::yarncluster_instantiation(instance):
    assert isinstance(instance, ddsm::YarnCluster)

@given(instance=ddsm::SparkCluster_strategy)
@settings(max_examples=50)
def test_ddsm::sparkcluster_instantiation(instance):
    assert isinstance(instance, ddsm::SparkCluster)

@given(instance=ddsm::SparkCluster_strategy)
def test_ddsm::sparkcluster_driverCores_type(instance):
    assert isinstance(instance.driverCores, int)


@given(instance=ddsm::SparkCluster_strategy)
def test_ddsm::sparkcluster_driverCores_setter(instance):
    original = instance.driverCores
    instance.driverCores = original
    assert instance.driverCores == original

@given(instance=ddsm::SparkCluster_strategy)
def test_ddsm::sparkcluster_sparkExecutorMemory_type(instance):
    assert isinstance(instance.sparkExecutorMemory, int)


@given(instance=ddsm::SparkCluster_strategy)
def test_ddsm::sparkcluster_sparkExecutorMemory_setter(instance):
    original = instance.sparkExecutorMemory
    instance.sparkExecutorMemory = original
    assert instance.sparkExecutorMemory == original

@given(instance=ddsm::SparkCluster_strategy)
def test_ddsm::sparkcluster_maxResultSize_type(instance):
    assert isinstance(instance.maxResultSize, int)


@given(instance=ddsm::SparkCluster_strategy)
def test_ddsm::sparkcluster_maxResultSize_setter(instance):
    original = instance.maxResultSize
    instance.maxResultSize = original
    assert instance.maxResultSize == original

@given(instance=ddsm::SparkCluster_strategy)
def test_ddsm::sparkcluster_UIPort_type(instance):
    assert isinstance(instance.UIPort, int)


@given(instance=ddsm::SparkCluster_strategy)
def test_ddsm::sparkcluster_UIPort_setter(instance):
    original = instance.UIPort
    instance.UIPort = original
    assert instance.UIPort == original

@given(instance=ddsm::SparkCluster_strategy)
def test_ddsm::sparkcluster_driverMemory_type(instance):
    assert isinstance(instance.driverMemory, int)


@given(instance=ddsm::SparkCluster_strategy)
def test_ddsm::sparkcluster_driverMemory_setter(instance):
    original = instance.driverMemory
    instance.driverMemory = original
    assert instance.driverMemory == original

@given(instance=ddsm::StormCluster_strategy)
@settings(max_examples=50)
def test_ddsm::stormcluster_instantiation(instance):
    assert isinstance(instance, ddsm::StormCluster)

@given(instance=ddsm::StormCluster_strategy)
def test_ddsm::stormcluster_queueSize_type(instance):
    assert isinstance(instance.queueSize, int)


@given(instance=ddsm::StormCluster_strategy)
def test_ddsm::stormcluster_queueSize_setter(instance):
    original = instance.queueSize
    instance.queueSize = original
    assert instance.queueSize == original

@given(instance=ddsm::StormCluster_strategy)
def test_ddsm::stormcluster_cpuCapacity_type(instance):
    assert isinstance(instance.cpuCapacity, int)


@given(instance=ddsm::StormCluster_strategy)
def test_ddsm::stormcluster_cpuCapacity_setter(instance):
    original = instance.cpuCapacity
    instance.cpuCapacity = original
    assert instance.cpuCapacity == original

@given(instance=ddsm::StormCluster_strategy)
def test_ddsm::stormcluster_supervisorFrequency_type(instance):
    assert isinstance(instance.supervisorFrequency, int)


@given(instance=ddsm::StormCluster_strategy)
def test_ddsm::stormcluster_supervisorFrequency_setter(instance):
    original = instance.supervisorFrequency
    instance.supervisorFrequency = original
    assert instance.supervisorFrequency == original

@given(instance=ddsm::StormCluster_strategy)
def test_ddsm::stormcluster_retryInterval_type(instance):
    assert isinstance(instance.retryInterval, int)


@given(instance=ddsm::StormCluster_strategy)
def test_ddsm::stormcluster_retryInterval_setter(instance):
    original = instance.retryInterval
    instance.retryInterval = original
    assert instance.retryInterval == original

@given(instance=ddsm::StormCluster_strategy)
def test_ddsm::stormcluster_workerStartTimeout_type(instance):
    assert isinstance(instance.workerStartTimeout, int)


@given(instance=ddsm::StormCluster_strategy)
def test_ddsm::stormcluster_workerStartTimeout_setter(instance):
    original = instance.workerStartTimeout
    instance.workerStartTimeout = original
    assert instance.workerStartTimeout == original

@given(instance=ddsm::StormCluster_strategy)
def test_ddsm::stormcluster_heartbeatFrequency_type(instance):
    assert isinstance(instance.heartbeatFrequency, int)


@given(instance=ddsm::StormCluster_strategy)
def test_ddsm::stormcluster_heartbeatFrequency_setter(instance):
    original = instance.heartbeatFrequency
    instance.heartbeatFrequency = original
    assert instance.heartbeatFrequency == original

@given(instance=ddsm::StormCluster_strategy)
def test_ddsm::stormcluster_retryTimes_type(instance):
    assert isinstance(instance.retryTimes, int)


@given(instance=ddsm::StormCluster_strategy)
def test_ddsm::stormcluster_retryTimes_setter(instance):
    original = instance.retryTimes
    instance.retryTimes = original
    assert instance.retryTimes == original

@given(instance=ddsm::StormCluster_strategy)
def test_ddsm::stormcluster_memoryCapacity_type(instance):
    assert isinstance(instance.memoryCapacity, int)


@given(instance=ddsm::StormCluster_strategy)
def test_ddsm::stormcluster_memoryCapacity_setter(instance):
    original = instance.memoryCapacity
    instance.memoryCapacity = original
    assert instance.memoryCapacity == original

@given(instance=ddsm::StormCluster_strategy)
def test_ddsm::stormcluster_monitorFrequency_type(instance):
    assert isinstance(instance.monitorFrequency, int)


@given(instance=ddsm::StormCluster_strategy)
def test_ddsm::stormcluster_monitorFrequency_setter(instance):
    original = instance.monitorFrequency
    instance.monitorFrequency = original
    assert instance.monitorFrequency == original

@given(instance=ddsm::StormCluster_strategy)
def test_ddsm::stormcluster_taskTimeout_type(instance):
    assert isinstance(instance.taskTimeout, int)


@given(instance=ddsm::StormCluster_strategy)
def test_ddsm::stormcluster_taskTimeout_setter(instance):
    original = instance.taskTimeout
    instance.taskTimeout = original
    assert instance.taskTimeout == original

@given(instance=ddsm::Crontab_strategy)
@settings(max_examples=50)
def test_ddsm::crontab_instantiation(instance):
    assert isinstance(instance, ddsm::Crontab)

@given(instance=ddsm::Crontab_strategy)
def test_ddsm::crontab_min_type(instance):
    assert isinstance(instance.min, int)


@given(instance=ddsm::Crontab_strategy)
def test_ddsm::crontab_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=ddsm::Crontab_strategy)
def test_ddsm::crontab_dayOfWeek_type(instance):
    assert isinstance(instance.dayOfWeek, int)


@given(instance=ddsm::Crontab_strategy)
def test_ddsm::crontab_dayOfWeek_setter(instance):
    original = instance.dayOfWeek
    instance.dayOfWeek = original
    assert instance.dayOfWeek == original

@given(instance=ddsm::Crontab_strategy)
def test_ddsm::crontab_month_type(instance):
    assert isinstance(instance.month, int)


@given(instance=ddsm::Crontab_strategy)
def test_ddsm::crontab_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=ddsm::Crontab_strategy)
def test_ddsm::crontab_dayOfMonth_type(instance):
    assert isinstance(instance.dayOfMonth, int)


@given(instance=ddsm::Crontab_strategy)
def test_ddsm::crontab_dayOfMonth_setter(instance):
    original = instance.dayOfMonth
    instance.dayOfMonth = original
    assert instance.dayOfMonth == original

@given(instance=ddsm::Crontab_strategy)
def test_ddsm::crontab_hour_type(instance):
    assert isinstance(instance.hour, int)


@given(instance=ddsm::Crontab_strategy)
def test_ddsm::crontab_hour_setter(instance):
    original = instance.hour
    instance.hour = original
    assert instance.hour == original

@given(instance=InternalComponent_strategy)
@settings(max_examples=50)
def test_internalcomponent_instantiation(instance):
    assert isinstance(instance, InternalComponent)

@given(instance=ddsm::PeerNode_strategy)
@settings(max_examples=50)
def test_ddsm::peernode_instantiation(instance):
    assert isinstance(instance, ddsm::PeerNode)

@given(instance=ddsm::MasterNode_strategy)
@settings(max_examples=50)
def test_ddsm::masternode_instantiation(instance):
    assert isinstance(instance, ddsm::MasterNode)

@given(instance=ddsm::MasterSlavePlatform_strategy)
@settings(max_examples=50)
def test_ddsm::masterslaveplatform_instantiation(instance):
    assert isinstance(instance, ddsm::MasterSlavePlatform)

@given(instance=ddsm::SlaveNode_strategy)
@settings(max_examples=50)
def test_ddsm::slavenode_instantiation(instance):
    assert isinstance(instance, ddsm::SlaveNode)

@given(instance=ddsm::PeersQuorum_strategy)
@settings(max_examples=50)
def test_ddsm::peersquorum_instantiation(instance):
    assert isinstance(instance, ddsm::PeersQuorum)

@given(instance=ddsm::PeerToPeerPlatform_strategy)
@settings(max_examples=50)
def test_ddsm::peertopeerplatform_instantiation(instance):
    assert isinstance(instance, ddsm::PeerToPeerPlatform)

@given(instance=ddsm::ClientNode_strategy)
@settings(max_examples=50)
def test_ddsm::clientnode_instantiation(instance):
    assert isinstance(instance, ddsm::ClientNode)

@given(instance=ddsm::ClientNode_strategy)
def test_ddsm::clientnode_numberOfSubmissions_type(instance):
    assert isinstance(instance.numberOfSubmissions, int)


@given(instance=ddsm::ClientNode_strategy)
def test_ddsm::clientnode_numberOfSubmissions_setter(instance):
    original = instance.numberOfSubmissions
    instance.numberOfSubmissions = original
    assert instance.numberOfSubmissions == original

@given(instance=ddsm::ClientNode_strategy)
def test_ddsm::clientnode_skipRunningJob_type(instance):
    assert isinstance(instance.skipRunningJob, bool)


@given(instance=ddsm::ClientNode_strategy)
def test_ddsm::clientnode_skipRunningJob_setter(instance):
    original = instance.skipRunningJob
    instance.skipRunningJob = original
    assert instance.skipRunningJob == original

@given(instance=ExecutionPlatform_strategy)
@settings(max_examples=50)
def test_executionplatform_instantiation(instance):
    assert isinstance(instance, ExecutionPlatform)

@given(instance=Port_strategy)
@settings(max_examples=50)
def test_port_instantiation(instance):
    assert isinstance(instance, Port)

@given(instance=ExternalComponent_strategy)
@settings(max_examples=50)
def test_externalcomponent_instantiation(instance):
    assert isinstance(instance, ExternalComponent)

@given(instance=ddsm::VM_strategy)
@settings(max_examples=50)
def test_ddsm::vm_instantiation(instance):
    assert isinstance(instance, ddsm::VM)

@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_providerSpecificTypeName_type(instance):
    assert isinstance(instance.providerSpecificTypeName, str)


@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_providerSpecificTypeName_setter(instance):
    original = instance.providerSpecificTypeName
    instance.providerSpecificTypeName = original
    assert instance.providerSpecificTypeName == original

@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_maxRam_type(instance):
    assert isinstance(instance.maxRam, str)


@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_maxRam_setter(instance):
    original = instance.maxRam
    instance.maxRam = original
    assert instance.maxRam == original

@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_imageId_type(instance):
    assert isinstance(instance.imageId, str)


@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_imageId_setter(instance):
    original = instance.imageId
    instance.imageId = original
    assert instance.imageId == original

@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_genericSize_type(instance):
    assert isinstance(instance.genericSize, str)


@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_genericSize_setter(instance):
    original = instance.genericSize
    instance.genericSize = original
    assert instance.genericSize == original

@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_is64os_type(instance):
    assert isinstance(instance.is64os, str)


@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_is64os_setter(instance):
    original = instance.is64os
    instance.is64os = original
    assert instance.is64os == original

@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_os_type(instance):
    assert isinstance(instance.os, str)


@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_os_setter(instance):
    original = instance.os
    instance.os = original
    assert instance.os == original

@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_sshKey_type(instance):
    assert isinstance(instance.sshKey, str)


@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_sshKey_setter(instance):
    original = instance.sshKey
    instance.sshKey = original
    assert instance.sshKey == original

@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_minStorage_type(instance):
    assert isinstance(instance.minStorage, str)


@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_minStorage_setter(instance):
    original = instance.minStorage
    instance.minStorage = original
    assert instance.minStorage == original

@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_minCores_type(instance):
    assert isinstance(instance.minCores, str)


@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_minCores_setter(instance):
    original = instance.minCores
    instance.minCores = original
    assert instance.minCores == original

@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_maxCores_type(instance):
    assert isinstance(instance.maxCores, str)


@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_maxCores_setter(instance):
    original = instance.maxCores
    instance.maxCores = original
    assert instance.maxCores == original

@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_minRam_type(instance):
    assert isinstance(instance.minRam, str)


@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_minRam_setter(instance):
    original = instance.minRam
    instance.minRam = original
    assert instance.minRam == original

@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_publicPorts_type(instance):
    assert isinstance(instance.publicPorts, int)


@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_publicPorts_setter(instance):
    original = instance.publicPorts
    instance.publicPorts = original
    assert instance.publicPorts == original

@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_publicAddress_type(instance):
    assert isinstance(instance.publicAddress, str)


@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_publicAddress_setter(instance):
    original = instance.publicAddress
    instance.publicAddress = original
    assert instance.publicAddress == original

@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_instances_type(instance):
    assert isinstance(instance.instances, int)


@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_instances_setter(instance):
    original = instance.instances
    instance.instances = original
    assert instance.instances == original

@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_maxStorage_type(instance):
    assert isinstance(instance.maxStorage, str)


@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_maxStorage_setter(instance):
    original = instance.maxStorage
    instance.maxStorage = original
    assert instance.maxStorage == original

@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_privateKey_type(instance):
    assert isinstance(instance.privateKey, str)


@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_privateKey_setter(instance):
    original = instance.privateKey
    instance.privateKey = original
    assert instance.privateKey == original

@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_securityGroup_type(instance):
    assert isinstance(instance.securityGroup, str)


@given(instance=ddsm::VM_strategy)
def test_ddsm::vm_securityGroup_setter(instance):
    original = instance.securityGroup
    instance.securityGroup = original
    assert instance.securityGroup == original

@given(instance=ddsm::Artifact_strategy)
@settings(max_examples=50)
def test_ddsm::artifact_instantiation(instance):
    assert isinstance(instance, ddsm::Artifact)

@given(instance=ddsm::Artifact_strategy)
def test_ddsm::artifact_arguments_type(instance):
    assert isinstance(instance.arguments, str)


@given(instance=ddsm::Artifact_strategy)
def test_ddsm::artifact_arguments_setter(instance):
    original = instance.arguments
    instance.arguments = original
    assert instance.arguments == original

@given(instance=ddsm::Artifact_strategy)
def test_ddsm::artifact_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=ddsm::Artifact_strategy)
def test_ddsm::artifact_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=ddsm::Artifact_strategy)
def test_ddsm::artifact_resources_type(instance):
    assert isinstance(instance.resources, str)


@given(instance=ddsm::Artifact_strategy)
def test_ddsm::artifact_resources_setter(instance):
    original = instance.resources
    instance.resources = original
    assert instance.resources == original

@given(instance=ddsm::Artifact_strategy)
def test_ddsm::artifact_artifactPath_type(instance):
    assert isinstance(instance.artifactPath, str)


@given(instance=ddsm::Artifact_strategy)
def test_ddsm::artifact_artifactPath_setter(instance):
    original = instance.artifactPath
    instance.artifactPath = original
    assert instance.artifactPath == original

@given(instance=ddsm::Property_strategy)
@settings(max_examples=50)
def test_ddsm::property_instantiation(instance):
    assert isinstance(instance, ddsm::Property)

@given(instance=ddsm::Property_strategy)
def test_ddsm::property_propertyId_type(instance):
    assert isinstance(instance.propertyId, str)


@given(instance=ddsm::Property_strategy)
def test_ddsm::property_propertyId_setter(instance):
    original = instance.propertyId
    instance.propertyId = original
    assert instance.propertyId == original

@given(instance=ddsm::Property_strategy)
def test_ddsm::property_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ddsm::Property_strategy)
def test_ddsm::property_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ddsm::RequiredExecutionPlatform_strategy)
@settings(max_examples=50)
def test_ddsm::requiredexecutionplatform_instantiation(instance):
    assert isinstance(instance, ddsm::RequiredExecutionPlatform)

@given(instance=ddsm::RequiredExecutionPlatform_strategy)
def test_ddsm::requiredexecutionplatform_isMandatory_type(instance):
    assert isinstance(instance.isMandatory, bool)


@given(instance=ddsm::RequiredExecutionPlatform_strategy)
def test_ddsm::requiredexecutionplatform_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=ddsm::RequiredPort_strategy)
@settings(max_examples=50)
def test_ddsm::requiredport_instantiation(instance):
    assert isinstance(instance, ddsm::RequiredPort)

@given(instance=ddsm::RequiredPort_strategy)
def test_ddsm::requiredport_isMandatory_type(instance):
    assert isinstance(instance.isMandatory, bool)


@given(instance=ddsm::RequiredPort_strategy)
def test_ddsm::requiredport_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=Component_strategy)
@settings(max_examples=50)
def test_component_instantiation(instance):
    assert isinstance(instance, Component)

@given(instance=ddsm::ExternalComponent_strategy)
@settings(max_examples=50)
def test_ddsm::externalcomponent_instantiation(instance):
    assert isinstance(instance, ddsm::ExternalComponent)

@given(instance=ddsm::ExternalComponent_strategy)
def test_ddsm::externalcomponent_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=ddsm::ExternalComponent_strategy)
def test_ddsm::externalcomponent_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=ddsm::ExternalComponent_strategy)
def test_ddsm::externalcomponent_region_type(instance):
    assert isinstance(instance.region, str)


@given(instance=ddsm::ExternalComponent_strategy)
def test_ddsm::externalcomponent_region_setter(instance):
    original = instance.region
    instance.region = original
    assert instance.region == original

@given(instance=ddsm::ExternalComponent_strategy)
def test_ddsm::externalcomponent_login_type(instance):
    assert isinstance(instance.login, str)


@given(instance=ddsm::ExternalComponent_strategy)
def test_ddsm::externalcomponent_login_setter(instance):
    original = instance.login
    instance.login = original
    assert instance.login == original

@given(instance=ddsm::ExternalComponent_strategy)
def test_ddsm::externalcomponent_serviceType_type(instance):
    assert isinstance(instance.serviceType, str)


@given(instance=ddsm::ExternalComponent_strategy)
def test_ddsm::externalcomponent_serviceType_setter(instance):
    original = instance.serviceType
    instance.serviceType = original
    assert instance.serviceType == original

@given(instance=ddsm::ExternalComponent_strategy)
def test_ddsm::externalcomponent_endPoint_type(instance):
    assert isinstance(instance.endPoint, str)


@given(instance=ddsm::ExternalComponent_strategy)
def test_ddsm::externalcomponent_endPoint_setter(instance):
    original = instance.endPoint
    instance.endPoint = original
    assert instance.endPoint == original

@given(instance=ddsm::ExternalComponent_strategy)
def test_ddsm::externalcomponent_password_type(instance):
    assert isinstance(instance.password, str)


@given(instance=ddsm::ExternalComponent_strategy)
def test_ddsm::externalcomponent_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=ddsm::InternalComponent_strategy)
@settings(max_examples=50)
def test_ddsm::internalcomponent_instantiation(instance):
    assert isinstance(instance, ddsm::InternalComponent)

@given(instance=ddsm::ProvidedExecutionPlatform_strategy)
@settings(max_examples=50)
def test_ddsm::providedexecutionplatform_instantiation(instance):
    assert isinstance(instance, ddsm::ProvidedExecutionPlatform)

@given(instance=ddsm::ProvidedPort_strategy)
@settings(max_examples=50)
def test_ddsm::providedport_instantiation(instance):
    assert isinstance(instance, ddsm::ProvidedPort)

@given(instance=CloudElement_strategy)
@settings(max_examples=50)
def test_cloudelement_instantiation(instance):
    assert isinstance(instance, CloudElement)

@given(instance=ddsm::Port_strategy)
@settings(max_examples=50)
def test_ddsm::port_instantiation(instance):
    assert isinstance(instance, ddsm::Port)

@given(instance=ddsm::Port_strategy)
def test_ddsm::port_isLocal_type(instance):
    assert isinstance(instance.isLocal, bool)


@given(instance=ddsm::Port_strategy)
def test_ddsm::port_isLocal_setter(instance):
    original = instance.isLocal
    instance.isLocal = original
    assert instance.isLocal == original

@given(instance=ddsm::Port_strategy)
def test_ddsm::port_portNumber_type(instance):
    assert isinstance(instance.portNumber, str)


@given(instance=ddsm::Port_strategy)
def test_ddsm::port_portNumber_setter(instance):
    original = instance.portNumber
    instance.portNumber = original
    assert instance.portNumber == original

@given(instance=ddsm::ExecutionPlatform_strategy)
@settings(max_examples=50)
def test_ddsm::executionplatform_instantiation(instance):
    assert isinstance(instance, ddsm::ExecutionPlatform)

@given(instance=ddsm::Provider_strategy)
@settings(max_examples=50)
def test_ddsm::provider_instantiation(instance):
    assert isinstance(instance, ddsm::Provider)

@given(instance=ddsm::Provider_strategy)
def test_ddsm::provider_credentialsPath_type(instance):
    assert isinstance(instance.credentialsPath, str)


@given(instance=ddsm::Provider_strategy)
def test_ddsm::provider_credentialsPath_setter(instance):
    original = instance.credentialsPath
    instance.credentialsPath = original
    assert instance.credentialsPath == original

@given(instance=ddsm::Provider_strategy)
def test_ddsm::provider_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=ddsm::Provider_strategy)
def test_ddsm::provider_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ddsm::Relationship_strategy)
@settings(max_examples=50)
def test_ddsm::relationship_instantiation(instance):
    assert isinstance(instance, ddsm::Relationship)

@given(instance=ddsm::ExecutionBinding_strategy)
@settings(max_examples=50)
def test_ddsm::executionbinding_instantiation(instance):
    assert isinstance(instance, ddsm::ExecutionBinding)

@given(instance=ddsm::JobSubmission_strategy)
@settings(max_examples=50)
def test_ddsm::jobsubmission_instantiation(instance):
    assert isinstance(instance, ddsm::JobSubmission)

@given(instance=ddsm::JobSubmission_strategy)
def test_ddsm::jobsubmission_mainClass_type(instance):
    assert isinstance(instance.mainClass, str)


@given(instance=ddsm::JobSubmission_strategy)
def test_ddsm::jobsubmission_mainClass_setter(instance):
    original = instance.mainClass
    instance.mainClass = original
    assert instance.mainClass == original

@given(instance=ddsm::JobSubmission_strategy)
def test_ddsm::jobsubmission_artifactUrl_type(instance):
    assert isinstance(instance.artifactUrl, str)


@given(instance=ddsm::JobSubmission_strategy)
def test_ddsm::jobsubmission_artifactUrl_setter(instance):
    original = instance.artifactUrl
    instance.artifactUrl = original
    assert instance.artifactUrl == original

@given(instance=ddsm::JobSubmission_strategy)
def test_ddsm::jobsubmission_applicationArguments_type(instance):
    assert isinstance(instance.applicationArguments, str)


@given(instance=ddsm::JobSubmission_strategy)
def test_ddsm::jobsubmission_applicationArguments_setter(instance):
    original = instance.applicationArguments
    instance.applicationArguments = original
    assert instance.applicationArguments == original

@given(instance=ddsm::Component_strategy)
@settings(max_examples=50)
def test_ddsm::component_instantiation(instance):
    assert isinstance(instance, ddsm::Component)

@given(instance=ddsm::Resource_strategy)
@settings(max_examples=50)
def test_ddsm::resource_instantiation(instance):
    assert isinstance(instance, ddsm::Resource)

@given(instance=ddsm::Resource_strategy)
def test_ddsm::resource_resourceId_type(instance):
    assert isinstance(instance.resourceId, str)


@given(instance=ddsm::Resource_strategy)
def test_ddsm::resource_resourceId_setter(instance):
    original = instance.resourceId
    instance.resourceId = original
    assert instance.resourceId == original

@given(instance=ddsm::CloudElement_strategy)
@settings(max_examples=50)
def test_ddsm::cloudelement_instantiation(instance):
    assert isinstance(instance, ddsm::CloudElement)

@given(instance=ddsm::CloudElement_strategy)
def test_ddsm::cloudelement_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=ddsm::CloudElement_strategy)
def test_ddsm::cloudelement_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=ddsm::CloudElement_strategy)
def test_ddsm::cloudelement_elementId_type(instance):
    assert isinstance(instance.elementId, str)


@given(instance=ddsm::CloudElement_strategy)
def test_ddsm::cloudelement_elementId_setter(instance):
    original = instance.elementId
    instance.elementId = original
    assert instance.elementId == original
