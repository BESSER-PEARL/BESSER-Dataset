import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ArtefactPortInstance,
    NodePortInstance,
    NodePort,
    NodeInstance,
    ArtefactInstance,
    Node,
    Artefact,
    Provider,
    WithProperties,
    cloudml::core::Provider,
    cloudml::core::NodePortInstance,
    cloudml::core::ArtefactPort,
    cloudml::core::NodePort,
    cloudml::core::DeploymentModel,
    cloudml::core::ArtefactPortInstance,
    cloudml::core::NodeInstance,
    cloudml::core::ArtefactInstance,
    cloudml::core::Node,
    cloudml::core::Resource,
    Property,
    NamedElement,
    cloudml::core::Composite,
    cloudml::core::WithProperties,
    cloudml::core::Property,
    CloudMLElement,
    cloudml::core::NamedElement,
    cloudml::core::CloudMLElement,
    Resource,
    ArtefactPort,
    cloudml::core::Artefact,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_artefactportinstance_is_not_abstract():
    assert not inspect.isabstract(ArtefactPortInstance)


def test_artefactportinstance_constructor_exists():
    assert callable(ArtefactPortInstance.__init__)


def test_artefactportinstance_constructor_args():
    sig = inspect.signature(ArtefactPortInstance.__init__)
    params = list(sig.parameters.keys())



def test_nodeportinstance_is_not_abstract():
    assert not inspect.isabstract(NodePortInstance)


def test_nodeportinstance_constructor_exists():
    assert callable(NodePortInstance.__init__)


def test_nodeportinstance_constructor_args():
    sig = inspect.signature(NodePortInstance.__init__)
    params = list(sig.parameters.keys())



def test_nodeport_is_not_abstract():
    assert not inspect.isabstract(NodePort)


def test_nodeport_constructor_exists():
    assert callable(NodePort.__init__)


def test_nodeport_constructor_args():
    sig = inspect.signature(NodePort.__init__)
    params = list(sig.parameters.keys())



def test_nodeinstance_is_not_abstract():
    assert not inspect.isabstract(NodeInstance)


def test_nodeinstance_constructor_exists():
    assert callable(NodeInstance.__init__)


def test_nodeinstance_constructor_args():
    sig = inspect.signature(NodeInstance.__init__)
    params = list(sig.parameters.keys())



def test_artefactinstance_is_not_abstract():
    assert not inspect.isabstract(ArtefactInstance)


def test_artefactinstance_constructor_exists():
    assert callable(ArtefactInstance.__init__)


def test_artefactinstance_constructor_args():
    sig = inspect.signature(ArtefactInstance.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_artefact_is_not_abstract():
    assert not inspect.isabstract(Artefact)


def test_artefact_constructor_exists():
    assert callable(Artefact.__init__)


def test_artefact_constructor_args():
    sig = inspect.signature(Artefact.__init__)
    params = list(sig.parameters.keys())



def test_provider_is_not_abstract():
    assert not inspect.isabstract(Provider)


def test_provider_constructor_exists():
    assert callable(Provider.__init__)


def test_provider_constructor_args():
    sig = inspect.signature(Provider.__init__)
    params = list(sig.parameters.keys())



def test_withproperties_is_not_abstract():
    assert not inspect.isabstract(WithProperties)


def test_withproperties_constructor_exists():
    assert callable(WithProperties.__init__)


def test_withproperties_constructor_args():
    sig = inspect.signature(WithProperties.__init__)
    params = list(sig.parameters.keys())



def test_cloudml::core::provider_is_not_abstract():
    assert not inspect.isabstract(cloudml::core::Provider)


def test_cloudml::core::provider_constructor_exists():
    assert callable(cloudml::core::Provider.__init__)


def test_cloudml::core::provider_constructor_args():
    sig = inspect.signature(cloudml::core::Provider.__init__)
    params = list(sig.parameters.keys())
    assert "credentials" in params, "Missing parameter 'credentials'"

def test_cloudml::core::provider_has_credentials():
    assert hasattr(cloudml::core::Provider, "credentials")
    descriptor = None
    for klass in cloudml::core::Provider.__mro__:
        if "credentials" in klass.__dict__:
            descriptor = klass.__dict__["credentials"]
            break
    assert isinstance(descriptor, property)



def test_cloudml::core::nodeportinstance_is_not_abstract():
    assert not inspect.isabstract(cloudml::core::NodePortInstance)


def test_cloudml::core::nodeportinstance_constructor_exists():
    assert callable(cloudml::core::NodePortInstance.__init__)


def test_cloudml::core::nodeportinstance_constructor_args():
    sig = inspect.signature(cloudml::core::NodePortInstance.__init__)
    params = list(sig.parameters.keys())



def test_cloudml::core::artefactport_is_not_abstract():
    assert not inspect.isabstract(cloudml::core::ArtefactPort)


def test_cloudml::core::artefactport_constructor_exists():
    assert callable(cloudml::core::ArtefactPort.__init__)


def test_cloudml::core::artefactport_constructor_args():
    sig = inspect.signature(cloudml::core::ArtefactPort.__init__)
    params = list(sig.parameters.keys())
    assert "portNumber" in params, "Missing parameter 'portNumber'"

def test_cloudml::core::artefactport_has_portNumber():
    assert hasattr(cloudml::core::ArtefactPort, "portNumber")
    descriptor = None
    for klass in cloudml::core::ArtefactPort.__mro__:
        if "portNumber" in klass.__dict__:
            descriptor = klass.__dict__["portNumber"]
            break
    assert isinstance(descriptor, property)



def test_cloudml::core::nodeport_is_not_abstract():
    assert not inspect.isabstract(cloudml::core::NodePort)


def test_cloudml::core::nodeport_constructor_exists():
    assert callable(cloudml::core::NodePort.__init__)


def test_cloudml::core::nodeport_constructor_args():
    sig = inspect.signature(cloudml::core::NodePort.__init__)
    params = list(sig.parameters.keys())



def test_cloudml::core::deploymentmodel_is_not_abstract():
    assert not inspect.isabstract(cloudml::core::DeploymentModel)


def test_cloudml::core::deploymentmodel_constructor_exists():
    assert callable(cloudml::core::DeploymentModel.__init__)


def test_cloudml::core::deploymentmodel_constructor_args():
    sig = inspect.signature(cloudml::core::DeploymentModel.__init__)
    params = list(sig.parameters.keys())



def test_cloudml::core::artefactportinstance_is_not_abstract():
    assert not inspect.isabstract(cloudml::core::ArtefactPortInstance)


def test_cloudml::core::artefactportinstance_constructor_exists():
    assert callable(cloudml::core::ArtefactPortInstance.__init__)


def test_cloudml::core::artefactportinstance_constructor_args():
    sig = inspect.signature(cloudml::core::ArtefactPortInstance.__init__)
    params = list(sig.parameters.keys())



def test_cloudml::core::nodeinstance_is_not_abstract():
    assert not inspect.isabstract(cloudml::core::NodeInstance)


def test_cloudml::core::nodeinstance_constructor_exists():
    assert callable(cloudml::core::NodeInstance.__init__)


def test_cloudml::core::nodeinstance_constructor_args():
    sig = inspect.signature(cloudml::core::NodeInstance.__init__)
    params = list(sig.parameters.keys())
    assert "publicAddress" in params, "Missing parameter 'publicAddress'"

def test_cloudml::core::nodeinstance_has_publicAddress():
    assert hasattr(cloudml::core::NodeInstance, "publicAddress")
    descriptor = None
    for klass in cloudml::core::NodeInstance.__mro__:
        if "publicAddress" in klass.__dict__:
            descriptor = klass.__dict__["publicAddress"]
            break
    assert isinstance(descriptor, property)



def test_cloudml::core::artefactinstance_is_not_abstract():
    assert not inspect.isabstract(cloudml::core::ArtefactInstance)


def test_cloudml::core::artefactinstance_constructor_exists():
    assert callable(cloudml::core::ArtefactInstance.__init__)


def test_cloudml::core::artefactinstance_constructor_args():
    sig = inspect.signature(cloudml::core::ArtefactInstance.__init__)
    params = list(sig.parameters.keys())



def test_cloudml::core::node_is_not_abstract():
    assert not inspect.isabstract(cloudml::core::Node)


def test_cloudml::core::node_constructor_exists():
    assert callable(cloudml::core::Node.__init__)


def test_cloudml::core::node_constructor_args():
    sig = inspect.signature(cloudml::core::Node.__init__)
    params = list(sig.parameters.keys())
    assert "imageID" in params, "Missing parameter 'imageID'"
    assert "location" in params, "Missing parameter 'location'"
    assert "minRam" in params, "Missing parameter 'minRam'"
    assert "privateKey" in params, "Missing parameter 'privateKey'"
    assert "minCore" in params, "Missing parameter 'minCore'"
    assert "OS" in params, "Missing parameter 'OS'"
    assert "groupName" in params, "Missing parameter 'groupName'"
    assert "is64os" in params, "Missing parameter 'is64os'"
    assert "securityGroup" in params, "Missing parameter 'securityGroup'"
    assert "sshKey" in params, "Missing parameter 'sshKey'"
    assert "minDisk" in params, "Missing parameter 'minDisk'"

def test_cloudml::core::node_has_imageID():
    assert hasattr(cloudml::core::Node, "imageID")
    descriptor = None
    for klass in cloudml::core::Node.__mro__:
        if "imageID" in klass.__dict__:
            descriptor = klass.__dict__["imageID"]
            break
    assert isinstance(descriptor, property)

def test_cloudml::core::node_has_location():
    assert hasattr(cloudml::core::Node, "location")
    descriptor = None
    for klass in cloudml::core::Node.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_cloudml::core::node_has_minRam():
    assert hasattr(cloudml::core::Node, "minRam")
    descriptor = None
    for klass in cloudml::core::Node.__mro__:
        if "minRam" in klass.__dict__:
            descriptor = klass.__dict__["minRam"]
            break
    assert isinstance(descriptor, property)

def test_cloudml::core::node_has_privateKey():
    assert hasattr(cloudml::core::Node, "privateKey")
    descriptor = None
    for klass in cloudml::core::Node.__mro__:
        if "privateKey" in klass.__dict__:
            descriptor = klass.__dict__["privateKey"]
            break
    assert isinstance(descriptor, property)

def test_cloudml::core::node_has_minCore():
    assert hasattr(cloudml::core::Node, "minCore")
    descriptor = None
    for klass in cloudml::core::Node.__mro__:
        if "minCore" in klass.__dict__:
            descriptor = klass.__dict__["minCore"]
            break
    assert isinstance(descriptor, property)

def test_cloudml::core::node_has_OS():
    assert hasattr(cloudml::core::Node, "OS")
    descriptor = None
    for klass in cloudml::core::Node.__mro__:
        if "OS" in klass.__dict__:
            descriptor = klass.__dict__["OS"]
            break
    assert isinstance(descriptor, property)

def test_cloudml::core::node_has_groupName():
    assert hasattr(cloudml::core::Node, "groupName")
    descriptor = None
    for klass in cloudml::core::Node.__mro__:
        if "groupName" in klass.__dict__:
            descriptor = klass.__dict__["groupName"]
            break
    assert isinstance(descriptor, property)

def test_cloudml::core::node_has_is64os():
    assert hasattr(cloudml::core::Node, "is64os")
    descriptor = None
    for klass in cloudml::core::Node.__mro__:
        if "is64os" in klass.__dict__:
            descriptor = klass.__dict__["is64os"]
            break
    assert isinstance(descriptor, property)

def test_cloudml::core::node_has_securityGroup():
    assert hasattr(cloudml::core::Node, "securityGroup")
    descriptor = None
    for klass in cloudml::core::Node.__mro__:
        if "securityGroup" in klass.__dict__:
            descriptor = klass.__dict__["securityGroup"]
            break
    assert isinstance(descriptor, property)

def test_cloudml::core::node_has_sshKey():
    assert hasattr(cloudml::core::Node, "sshKey")
    descriptor = None
    for klass in cloudml::core::Node.__mro__:
        if "sshKey" in klass.__dict__:
            descriptor = klass.__dict__["sshKey"]
            break
    assert isinstance(descriptor, property)

def test_cloudml::core::node_has_minDisk():
    assert hasattr(cloudml::core::Node, "minDisk")
    descriptor = None
    for klass in cloudml::core::Node.__mro__:
        if "minDisk" in klass.__dict__:
            descriptor = klass.__dict__["minDisk"]
            break
    assert isinstance(descriptor, property)



def test_cloudml::core::resource_is_not_abstract():
    assert not inspect.isabstract(cloudml::core::Resource)


def test_cloudml::core::resource_constructor_exists():
    assert callable(cloudml::core::Resource.__init__)


def test_cloudml::core::resource_constructor_args():
    sig = inspect.signature(cloudml::core::Resource.__init__)
    params = list(sig.parameters.keys())
    assert "startCommand" in params, "Missing parameter 'startCommand'"
    assert "deployingCommand" in params, "Missing parameter 'deployingCommand'"
    assert "configurationCommand" in params, "Missing parameter 'configurationCommand'"
    assert "retrievingCommand" in params, "Missing parameter 'retrievingCommand'"

def test_cloudml::core::resource_has_startCommand():
    assert hasattr(cloudml::core::Resource, "startCommand")
    descriptor = None
    for klass in cloudml::core::Resource.__mro__:
        if "startCommand" in klass.__dict__:
            descriptor = klass.__dict__["startCommand"]
            break
    assert isinstance(descriptor, property)

def test_cloudml::core::resource_has_deployingCommand():
    assert hasattr(cloudml::core::Resource, "deployingCommand")
    descriptor = None
    for klass in cloudml::core::Resource.__mro__:
        if "deployingCommand" in klass.__dict__:
            descriptor = klass.__dict__["deployingCommand"]
            break
    assert isinstance(descriptor, property)

def test_cloudml::core::resource_has_configurationCommand():
    assert hasattr(cloudml::core::Resource, "configurationCommand")
    descriptor = None
    for klass in cloudml::core::Resource.__mro__:
        if "configurationCommand" in klass.__dict__:
            descriptor = klass.__dict__["configurationCommand"]
            break
    assert isinstance(descriptor, property)

def test_cloudml::core::resource_has_retrievingCommand():
    assert hasattr(cloudml::core::Resource, "retrievingCommand")
    descriptor = None
    for klass in cloudml::core::Resource.__mro__:
        if "retrievingCommand" in klass.__dict__:
            descriptor = klass.__dict__["retrievingCommand"]
            break
    assert isinstance(descriptor, property)



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_cloudml::core::composite_is_not_abstract():
    assert not inspect.isabstract(cloudml::core::Composite)


def test_cloudml::core::composite_constructor_exists():
    assert callable(cloudml::core::Composite.__init__)


def test_cloudml::core::composite_constructor_args():
    sig = inspect.signature(cloudml::core::Composite.__init__)
    params = list(sig.parameters.keys())



def test_cloudml::core::withproperties_is_not_abstract():
    assert not inspect.isabstract(cloudml::core::WithProperties)


def test_cloudml::core::withproperties_constructor_exists():
    assert callable(cloudml::core::WithProperties.__init__)


def test_cloudml::core::withproperties_constructor_args():
    sig = inspect.signature(cloudml::core::WithProperties.__init__)
    params = list(sig.parameters.keys())



def test_cloudml::core::property_is_not_abstract():
    assert not inspect.isabstract(cloudml::core::Property)


def test_cloudml::core::property_constructor_exists():
    assert callable(cloudml::core::Property.__init__)


def test_cloudml::core::property_constructor_args():
    sig = inspect.signature(cloudml::core::Property.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cloudml::core::property_has_value():
    assert hasattr(cloudml::core::Property, "value")
    descriptor = None
    for klass in cloudml::core::Property.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cloudmlelement_is_not_abstract():
    assert not inspect.isabstract(CloudMLElement)


def test_cloudmlelement_constructor_exists():
    assert callable(CloudMLElement.__init__)


def test_cloudmlelement_constructor_args():
    sig = inspect.signature(CloudMLElement.__init__)
    params = list(sig.parameters.keys())



def test_cloudml::core::namedelement_is_not_abstract():
    assert not inspect.isabstract(cloudml::core::NamedElement)


def test_cloudml::core::namedelement_constructor_exists():
    assert callable(cloudml::core::NamedElement.__init__)


def test_cloudml::core::namedelement_constructor_args():
    sig = inspect.signature(cloudml::core::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cloudml::core::namedelement_has_name():
    assert hasattr(cloudml::core::NamedElement, "name")
    descriptor = None
    for klass in cloudml::core::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cloudml::core::cloudmlelement_is_not_abstract():
    assert not inspect.isabstract(cloudml::core::CloudMLElement)


def test_cloudml::core::cloudmlelement_constructor_exists():
    assert callable(cloudml::core::CloudMLElement.__init__)


def test_cloudml::core::cloudmlelement_constructor_args():
    sig = inspect.signature(cloudml::core::CloudMLElement.__init__)
    params = list(sig.parameters.keys())



def test_resource_is_not_abstract():
    assert not inspect.isabstract(Resource)


def test_resource_constructor_exists():
    assert callable(Resource.__init__)


def test_resource_constructor_args():
    sig = inspect.signature(Resource.__init__)
    params = list(sig.parameters.keys())



def test_artefactport_is_not_abstract():
    assert not inspect.isabstract(ArtefactPort)


def test_artefactport_constructor_exists():
    assert callable(ArtefactPort.__init__)


def test_artefactport_constructor_args():
    sig = inspect.signature(ArtefactPort.__init__)
    params = list(sig.parameters.keys())



def test_cloudml::core::artefact_is_not_abstract():
    assert not inspect.isabstract(cloudml::core::Artefact)


def test_cloudml::core::artefact_constructor_exists():
    assert callable(cloudml::core::Artefact.__init__)


def test_cloudml::core::artefact_constructor_args():
    sig = inspect.signature(cloudml::core::Artefact.__init__)
    params = list(sig.parameters.keys())


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
ArtefactPortInstance_strategy = st.builds(
    ArtefactPortInstance,
)
NodePortInstance_strategy = st.builds(
    NodePortInstance,
)
NodePort_strategy = st.builds(
    NodePort,
)
NodeInstance_strategy = st.builds(
    NodeInstance,
)
ArtefactInstance_strategy = st.builds(
    ArtefactInstance,
)
Node_strategy = st.builds(
    Node,
)
Artefact_strategy = st.builds(
    Artefact,
)
Provider_strategy = st.builds(
    Provider,
)
WithProperties_strategy = st.builds(
    WithProperties,
)
cloudml::core::Provider_strategy = st.builds(
    cloudml::core::Provider,
    credentials=
        safe_text
)
cloudml::core::NodePortInstance_strategy = st.builds(
    cloudml::core::NodePortInstance,
)
cloudml::core::ArtefactPort_strategy = st.builds(
    cloudml::core::ArtefactPort,
    portNumber=
        st.integers()
)
cloudml::core::NodePort_strategy = st.builds(
    cloudml::core::NodePort,
)
cloudml::core::DeploymentModel_strategy = st.builds(
    cloudml::core::DeploymentModel,
)
cloudml::core::ArtefactPortInstance_strategy = st.builds(
    cloudml::core::ArtefactPortInstance,
)
cloudml::core::NodeInstance_strategy = st.builds(
    cloudml::core::NodeInstance,
    publicAddress=
        safe_text
)
cloudml::core::ArtefactInstance_strategy = st.builds(
    cloudml::core::ArtefactInstance,
)
cloudml::core::Node_strategy = st.builds(
    cloudml::core::Node,
    imageID=
        safe_text,
    location=
        safe_text,
    minRam=
        st.integers(),
    privateKey=
        safe_text,
    minCore=
        st.integers(),
    OS=
        safe_text,
    groupName=
        safe_text,
    is64os=
        st.booleans(),
    securityGroup=
        safe_text,
    sshKey=
        safe_text,
    minDisk=
        st.integers()
)
cloudml::core::Resource_strategy = st.builds(
    cloudml::core::Resource,
    startCommand=
        safe_text,
    deployingCommand=
        safe_text,
    configurationCommand=
        safe_text,
    retrievingCommand=
        safe_text
)
Property_strategy = st.builds(
    Property,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
cloudml::core::Composite_strategy = st.builds(
    cloudml::core::Composite,
)
cloudml::core::WithProperties_strategy = st.builds(
    cloudml::core::WithProperties,
)
cloudml::core::Property_strategy = st.builds(
    cloudml::core::Property,
    value=
        safe_text
)
CloudMLElement_strategy = st.builds(
    CloudMLElement,
)
cloudml::core::NamedElement_strategy = st.builds(
    cloudml::core::NamedElement,
    name=
        safe_text
)
cloudml::core::CloudMLElement_strategy = st.builds(
    cloudml::core::CloudMLElement,
)
Resource_strategy = st.builds(
    Resource,
)
ArtefactPort_strategy = st.builds(
    ArtefactPort,
)
cloudml::core::Artefact_strategy = st.builds(
    cloudml::core::Artefact,
)

@given(instance=ArtefactPortInstance_strategy)
@settings(max_examples=50)
def test_artefactportinstance_instantiation(instance):
    assert isinstance(instance, ArtefactPortInstance)

@given(instance=NodePortInstance_strategy)
@settings(max_examples=50)
def test_nodeportinstance_instantiation(instance):
    assert isinstance(instance, NodePortInstance)

@given(instance=NodePort_strategy)
@settings(max_examples=50)
def test_nodeport_instantiation(instance):
    assert isinstance(instance, NodePort)

@given(instance=NodeInstance_strategy)
@settings(max_examples=50)
def test_nodeinstance_instantiation(instance):
    assert isinstance(instance, NodeInstance)

@given(instance=ArtefactInstance_strategy)
@settings(max_examples=50)
def test_artefactinstance_instantiation(instance):
    assert isinstance(instance, ArtefactInstance)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=Artefact_strategy)
@settings(max_examples=50)
def test_artefact_instantiation(instance):
    assert isinstance(instance, Artefact)

@given(instance=Provider_strategy)
@settings(max_examples=50)
def test_provider_instantiation(instance):
    assert isinstance(instance, Provider)

@given(instance=WithProperties_strategy)
@settings(max_examples=50)
def test_withproperties_instantiation(instance):
    assert isinstance(instance, WithProperties)

@given(instance=cloudml::core::Provider_strategy)
@settings(max_examples=50)
def test_cloudml::core::provider_instantiation(instance):
    assert isinstance(instance, cloudml::core::Provider)

@given(instance=cloudml::core::Provider_strategy)
def test_cloudml::core::provider_credentials_type(instance):
    assert isinstance(instance.credentials, str)


@given(instance=cloudml::core::Provider_strategy)
def test_cloudml::core::provider_credentials_setter(instance):
    original = instance.credentials
    instance.credentials = original
    assert instance.credentials == original

@given(instance=cloudml::core::NodePortInstance_strategy)
@settings(max_examples=50)
def test_cloudml::core::nodeportinstance_instantiation(instance):
    assert isinstance(instance, cloudml::core::NodePortInstance)

@given(instance=cloudml::core::ArtefactPort_strategy)
@settings(max_examples=50)
def test_cloudml::core::artefactport_instantiation(instance):
    assert isinstance(instance, cloudml::core::ArtefactPort)

@given(instance=cloudml::core::ArtefactPort_strategy)
def test_cloudml::core::artefactport_portNumber_type(instance):
    assert isinstance(instance.portNumber, int)


@given(instance=cloudml::core::ArtefactPort_strategy)
def test_cloudml::core::artefactport_portNumber_setter(instance):
    original = instance.portNumber
    instance.portNumber = original
    assert instance.portNumber == original

@given(instance=cloudml::core::NodePort_strategy)
@settings(max_examples=50)
def test_cloudml::core::nodeport_instantiation(instance):
    assert isinstance(instance, cloudml::core::NodePort)

@given(instance=cloudml::core::DeploymentModel_strategy)
@settings(max_examples=50)
def test_cloudml::core::deploymentmodel_instantiation(instance):
    assert isinstance(instance, cloudml::core::DeploymentModel)

@given(instance=cloudml::core::ArtefactPortInstance_strategy)
@settings(max_examples=50)
def test_cloudml::core::artefactportinstance_instantiation(instance):
    assert isinstance(instance, cloudml::core::ArtefactPortInstance)

@given(instance=cloudml::core::NodeInstance_strategy)
@settings(max_examples=50)
def test_cloudml::core::nodeinstance_instantiation(instance):
    assert isinstance(instance, cloudml::core::NodeInstance)

@given(instance=cloudml::core::NodeInstance_strategy)
def test_cloudml::core::nodeinstance_publicAddress_type(instance):
    assert isinstance(instance.publicAddress, str)


@given(instance=cloudml::core::NodeInstance_strategy)
def test_cloudml::core::nodeinstance_publicAddress_setter(instance):
    original = instance.publicAddress
    instance.publicAddress = original
    assert instance.publicAddress == original

@given(instance=cloudml::core::ArtefactInstance_strategy)
@settings(max_examples=50)
def test_cloudml::core::artefactinstance_instantiation(instance):
    assert isinstance(instance, cloudml::core::ArtefactInstance)

@given(instance=cloudml::core::Node_strategy)
@settings(max_examples=50)
def test_cloudml::core::node_instantiation(instance):
    assert isinstance(instance, cloudml::core::Node)

@given(instance=cloudml::core::Node_strategy)
def test_cloudml::core::node_imageID_type(instance):
    assert isinstance(instance.imageID, str)


@given(instance=cloudml::core::Node_strategy)
def test_cloudml::core::node_imageID_setter(instance):
    original = instance.imageID
    instance.imageID = original
    assert instance.imageID == original

@given(instance=cloudml::core::Node_strategy)
def test_cloudml::core::node_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=cloudml::core::Node_strategy)
def test_cloudml::core::node_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=cloudml::core::Node_strategy)
def test_cloudml::core::node_minRam_type(instance):
    assert isinstance(instance.minRam, int)


@given(instance=cloudml::core::Node_strategy)
def test_cloudml::core::node_minRam_setter(instance):
    original = instance.minRam
    instance.minRam = original
    assert instance.minRam == original

@given(instance=cloudml::core::Node_strategy)
def test_cloudml::core::node_privateKey_type(instance):
    assert isinstance(instance.privateKey, str)


@given(instance=cloudml::core::Node_strategy)
def test_cloudml::core::node_privateKey_setter(instance):
    original = instance.privateKey
    instance.privateKey = original
    assert instance.privateKey == original

@given(instance=cloudml::core::Node_strategy)
def test_cloudml::core::node_minCore_type(instance):
    assert isinstance(instance.minCore, int)


@given(instance=cloudml::core::Node_strategy)
def test_cloudml::core::node_minCore_setter(instance):
    original = instance.minCore
    instance.minCore = original
    assert instance.minCore == original

@given(instance=cloudml::core::Node_strategy)
def test_cloudml::core::node_OS_type(instance):
    assert isinstance(instance.OS, str)


@given(instance=cloudml::core::Node_strategy)
def test_cloudml::core::node_OS_setter(instance):
    original = instance.OS
    instance.OS = original
    assert instance.OS == original

@given(instance=cloudml::core::Node_strategy)
def test_cloudml::core::node_groupName_type(instance):
    assert isinstance(instance.groupName, str)


@given(instance=cloudml::core::Node_strategy)
def test_cloudml::core::node_groupName_setter(instance):
    original = instance.groupName
    instance.groupName = original
    assert instance.groupName == original

@given(instance=cloudml::core::Node_strategy)
def test_cloudml::core::node_is64os_type(instance):
    assert isinstance(instance.is64os, bool)


@given(instance=cloudml::core::Node_strategy)
def test_cloudml::core::node_is64os_setter(instance):
    original = instance.is64os
    instance.is64os = original
    assert instance.is64os == original

@given(instance=cloudml::core::Node_strategy)
def test_cloudml::core::node_securityGroup_type(instance):
    assert isinstance(instance.securityGroup, str)


@given(instance=cloudml::core::Node_strategy)
def test_cloudml::core::node_securityGroup_setter(instance):
    original = instance.securityGroup
    instance.securityGroup = original
    assert instance.securityGroup == original

@given(instance=cloudml::core::Node_strategy)
def test_cloudml::core::node_sshKey_type(instance):
    assert isinstance(instance.sshKey, str)


@given(instance=cloudml::core::Node_strategy)
def test_cloudml::core::node_sshKey_setter(instance):
    original = instance.sshKey
    instance.sshKey = original
    assert instance.sshKey == original

@given(instance=cloudml::core::Node_strategy)
def test_cloudml::core::node_minDisk_type(instance):
    assert isinstance(instance.minDisk, int)


@given(instance=cloudml::core::Node_strategy)
def test_cloudml::core::node_minDisk_setter(instance):
    original = instance.minDisk
    instance.minDisk = original
    assert instance.minDisk == original

@given(instance=cloudml::core::Resource_strategy)
@settings(max_examples=50)
def test_cloudml::core::resource_instantiation(instance):
    assert isinstance(instance, cloudml::core::Resource)

@given(instance=cloudml::core::Resource_strategy)
def test_cloudml::core::resource_startCommand_type(instance):
    assert isinstance(instance.startCommand, str)


@given(instance=cloudml::core::Resource_strategy)
def test_cloudml::core::resource_startCommand_setter(instance):
    original = instance.startCommand
    instance.startCommand = original
    assert instance.startCommand == original

@given(instance=cloudml::core::Resource_strategy)
def test_cloudml::core::resource_deployingCommand_type(instance):
    assert isinstance(instance.deployingCommand, str)


@given(instance=cloudml::core::Resource_strategy)
def test_cloudml::core::resource_deployingCommand_setter(instance):
    original = instance.deployingCommand
    instance.deployingCommand = original
    assert instance.deployingCommand == original

@given(instance=cloudml::core::Resource_strategy)
def test_cloudml::core::resource_configurationCommand_type(instance):
    assert isinstance(instance.configurationCommand, str)


@given(instance=cloudml::core::Resource_strategy)
def test_cloudml::core::resource_configurationCommand_setter(instance):
    original = instance.configurationCommand
    instance.configurationCommand = original
    assert instance.configurationCommand == original

@given(instance=cloudml::core::Resource_strategy)
def test_cloudml::core::resource_retrievingCommand_type(instance):
    assert isinstance(instance.retrievingCommand, str)


@given(instance=cloudml::core::Resource_strategy)
def test_cloudml::core::resource_retrievingCommand_setter(instance):
    original = instance.retrievingCommand
    instance.retrievingCommand = original
    assert instance.retrievingCommand == original

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=cloudml::core::Composite_strategy)
@settings(max_examples=50)
def test_cloudml::core::composite_instantiation(instance):
    assert isinstance(instance, cloudml::core::Composite)

@given(instance=cloudml::core::WithProperties_strategy)
@settings(max_examples=50)
def test_cloudml::core::withproperties_instantiation(instance):
    assert isinstance(instance, cloudml::core::WithProperties)

@given(instance=cloudml::core::Property_strategy)
@settings(max_examples=50)
def test_cloudml::core::property_instantiation(instance):
    assert isinstance(instance, cloudml::core::Property)

@given(instance=cloudml::core::Property_strategy)
def test_cloudml::core::property_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cloudml::core::Property_strategy)
def test_cloudml::core::property_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=CloudMLElement_strategy)
@settings(max_examples=50)
def test_cloudmlelement_instantiation(instance):
    assert isinstance(instance, CloudMLElement)

@given(instance=cloudml::core::NamedElement_strategy)
@settings(max_examples=50)
def test_cloudml::core::namedelement_instantiation(instance):
    assert isinstance(instance, cloudml::core::NamedElement)

@given(instance=cloudml::core::NamedElement_strategy)
def test_cloudml::core::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cloudml::core::NamedElement_strategy)
def test_cloudml::core::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cloudml::core::CloudMLElement_strategy)
@settings(max_examples=50)
def test_cloudml::core::cloudmlelement_instantiation(instance):
    assert isinstance(instance, cloudml::core::CloudMLElement)

@given(instance=Resource_strategy)
@settings(max_examples=50)
def test_resource_instantiation(instance):
    assert isinstance(instance, Resource)

@given(instance=ArtefactPort_strategy)
@settings(max_examples=50)
def test_artefactport_instantiation(instance):
    assert isinstance(instance, ArtefactPort)

@given(instance=cloudml::core::Artefact_strategy)
@settings(max_examples=50)
def test_cloudml::core::artefact_instantiation(instance):
    assert isinstance(instance, cloudml::core::Artefact)
