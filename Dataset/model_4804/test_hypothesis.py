import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    model_IServiceTypeID,
    model_IHost,
    model_INetwork,
    model_IServiceID,
    model_IServiceInfo,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model_iservicetypeid_is_not_abstract():
    assert not inspect.isabstract(model_IServiceTypeID)


def test_model_iservicetypeid_constructor_exists():
    assert callable(model_IServiceTypeID.__init__)


def test_model_iservicetypeid_constructor_args():
    sig = inspect.signature(model_IServiceTypeID.__init__)
    params = list(sig.parameters.keys())
    assert "ecfNamingAuthority" in params, "Missing parameter 'ecfNamingAuthority'"
    assert "ecfServiceName" in params, "Missing parameter 'ecfServiceName'"
    assert "ecfServices" in params, "Missing parameter 'ecfServices'"
    assert "ecfServiceTypeID" in params, "Missing parameter 'ecfServiceTypeID'"
    assert "ecfProtocols" in params, "Missing parameter 'ecfProtocols'"
    assert "ecfScopes" in params, "Missing parameter 'ecfScopes'"

def test_model_iservicetypeid_has_ecfNamingAuthority():
    assert hasattr(model_IServiceTypeID, "ecfNamingAuthority")
    descriptor = None
    for klass in model_IServiceTypeID.__mro__:
        if "ecfNamingAuthority" in klass.__dict__:
            descriptor = klass.__dict__["ecfNamingAuthority"]
            break
    assert isinstance(descriptor, property)

def test_model_iservicetypeid_has_ecfServiceName():
    assert hasattr(model_IServiceTypeID, "ecfServiceName")
    descriptor = None
    for klass in model_IServiceTypeID.__mro__:
        if "ecfServiceName" in klass.__dict__:
            descriptor = klass.__dict__["ecfServiceName"]
            break
    assert isinstance(descriptor, property)

def test_model_iservicetypeid_has_ecfServices():
    assert hasattr(model_IServiceTypeID, "ecfServices")
    descriptor = None
    for klass in model_IServiceTypeID.__mro__:
        if "ecfServices" in klass.__dict__:
            descriptor = klass.__dict__["ecfServices"]
            break
    assert isinstance(descriptor, property)

def test_model_iservicetypeid_has_ecfServiceTypeID():
    assert hasattr(model_IServiceTypeID, "ecfServiceTypeID")
    descriptor = None
    for klass in model_IServiceTypeID.__mro__:
        if "ecfServiceTypeID" in klass.__dict__:
            descriptor = klass.__dict__["ecfServiceTypeID"]
            break
    assert isinstance(descriptor, property)

def test_model_iservicetypeid_has_ecfProtocols():
    assert hasattr(model_IServiceTypeID, "ecfProtocols")
    descriptor = None
    for klass in model_IServiceTypeID.__mro__:
        if "ecfProtocols" in klass.__dict__:
            descriptor = klass.__dict__["ecfProtocols"]
            break
    assert isinstance(descriptor, property)

def test_model_iservicetypeid_has_ecfScopes():
    assert hasattr(model_IServiceTypeID, "ecfScopes")
    descriptor = None
    for klass in model_IServiceTypeID.__mro__:
        if "ecfScopes" in klass.__dict__:
            descriptor = klass.__dict__["ecfScopes"]
            break
    assert isinstance(descriptor, property)



def test_model_ihost_is_not_abstract():
    assert not inspect.isabstract(model_IHost)


def test_model_ihost_constructor_exists():
    assert callable(model_IHost.__init__)


def test_model_ihost_constructor_args():
    sig = inspect.signature(model_IHost.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "address" in params, "Missing parameter 'address'"

def test_model_ihost_has_name():
    assert hasattr(model_IHost, "name")
    descriptor = None
    for klass in model_IHost.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model_ihost_has_address():
    assert hasattr(model_IHost, "address")
    descriptor = None
    for klass in model_IHost.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_model_inetwork_is_not_abstract():
    assert not inspect.isabstract(model_INetwork)


def test_model_inetwork_constructor_exists():
    assert callable(model_INetwork.__init__)


def test_model_inetwork_constructor_args():
    sig = inspect.signature(model_INetwork.__init__)
    params = list(sig.parameters.keys())



def test_model_iserviceid_is_not_abstract():
    assert not inspect.isabstract(model_IServiceID)


def test_model_iserviceid_constructor_exists():
    assert callable(model_IServiceID.__init__)


def test_model_iserviceid_constructor_args():
    sig = inspect.signature(model_IServiceID.__init__)
    params = list(sig.parameters.keys())
    assert "ecfServiceName" in params, "Missing parameter 'ecfServiceName'"
    assert "ecfServiceID" in params, "Missing parameter 'ecfServiceID'"

def test_model_iserviceid_has_ecfServiceName():
    assert hasattr(model_IServiceID, "ecfServiceName")
    descriptor = None
    for klass in model_IServiceID.__mro__:
        if "ecfServiceName" in klass.__dict__:
            descriptor = klass.__dict__["ecfServiceName"]
            break
    assert isinstance(descriptor, property)

def test_model_iserviceid_has_ecfServiceID():
    assert hasattr(model_IServiceID, "ecfServiceID")
    descriptor = None
    for klass in model_IServiceID.__mro__:
        if "ecfServiceID" in klass.__dict__:
            descriptor = klass.__dict__["ecfServiceID"]
            break
    assert isinstance(descriptor, property)



def test_model_iserviceinfo_is_not_abstract():
    assert not inspect.isabstract(model_IServiceInfo)


def test_model_iserviceinfo_constructor_exists():
    assert callable(model_IServiceInfo.__init__)


def test_model_iserviceinfo_constructor_args():
    sig = inspect.signature(model_IServiceInfo.__init__)
    params = list(sig.parameters.keys())
    assert "ecfServiceInfo" in params, "Missing parameter 'ecfServiceInfo'"
    assert "ecfPriority" in params, "Missing parameter 'ecfPriority'"
    assert "ecfName" in params, "Missing parameter 'ecfName'"
    assert "ecfWeight" in params, "Missing parameter 'ecfWeight'"
    assert "ecfLocation" in params, "Missing parameter 'ecfLocation'"

def test_model_iserviceinfo_has_ecfServiceInfo():
    assert hasattr(model_IServiceInfo, "ecfServiceInfo")
    descriptor = None
    for klass in model_IServiceInfo.__mro__:
        if "ecfServiceInfo" in klass.__dict__:
            descriptor = klass.__dict__["ecfServiceInfo"]
            break
    assert isinstance(descriptor, property)

def test_model_iserviceinfo_has_ecfPriority():
    assert hasattr(model_IServiceInfo, "ecfPriority")
    descriptor = None
    for klass in model_IServiceInfo.__mro__:
        if "ecfPriority" in klass.__dict__:
            descriptor = klass.__dict__["ecfPriority"]
            break
    assert isinstance(descriptor, property)

def test_model_iserviceinfo_has_ecfName():
    assert hasattr(model_IServiceInfo, "ecfName")
    descriptor = None
    for klass in model_IServiceInfo.__mro__:
        if "ecfName" in klass.__dict__:
            descriptor = klass.__dict__["ecfName"]
            break
    assert isinstance(descriptor, property)

def test_model_iserviceinfo_has_ecfWeight():
    assert hasattr(model_IServiceInfo, "ecfWeight")
    descriptor = None
    for klass in model_IServiceInfo.__mro__:
        if "ecfWeight" in klass.__dict__:
            descriptor = klass.__dict__["ecfWeight"]
            break
    assert isinstance(descriptor, property)

def test_model_iserviceinfo_has_ecfLocation():
    assert hasattr(model_IServiceInfo, "ecfLocation")
    descriptor = None
    for klass in model_IServiceInfo.__mro__:
        if "ecfLocation" in klass.__dict__:
            descriptor = klass.__dict__["ecfLocation"]
            break
    assert isinstance(descriptor, property)


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
model_IServiceTypeID_strategy = st.builds(
    model_IServiceTypeID,
    ecfNamingAuthority=
        safe_text,
    ecfServiceName=
        safe_text,
    ecfServices=
        safe_text,
    ecfServiceTypeID=
        safe_text,
    ecfProtocols=
        safe_text,
    ecfScopes=
        safe_text
)
model_IHost_strategy = st.builds(
    model_IHost,
    name=
        safe_text,
    address=
        safe_text
)
model_INetwork_strategy = st.builds(
    model_INetwork,
)
model_IServiceID_strategy = st.builds(
    model_IServiceID,
    ecfServiceName=
        safe_text,
    ecfServiceID=
        safe_text
)
model_IServiceInfo_strategy = st.builds(
    model_IServiceInfo,
    ecfServiceInfo=
        safe_text,
    ecfPriority=
        st.integers(),
    ecfName=
        safe_text,
    ecfWeight=
        st.integers(),
    ecfLocation=
        safe_text
)

@given(instance=model_IServiceTypeID_strategy)
@settings(max_examples=50)
def test_model_iservicetypeid_instantiation(instance):
    assert isinstance(instance, model_IServiceTypeID)



@given(instance=model_IServiceTypeID_strategy)
def test_model_iservicetypeid_ecfNamingAuthority_setter(instance):
    original = instance.ecfNamingAuthority
    instance.ecfNamingAuthority = original
    assert instance.ecfNamingAuthority == original



@given(instance=model_IServiceTypeID_strategy)
def test_model_iservicetypeid_ecfServiceName_setter(instance):
    original = instance.ecfServiceName
    instance.ecfServiceName = original
    assert instance.ecfServiceName == original



@given(instance=model_IServiceTypeID_strategy)
def test_model_iservicetypeid_ecfServices_setter(instance):
    original = instance.ecfServices
    instance.ecfServices = original
    assert instance.ecfServices == original



@given(instance=model_IServiceTypeID_strategy)
def test_model_iservicetypeid_ecfServiceTypeID_setter(instance):
    original = instance.ecfServiceTypeID
    instance.ecfServiceTypeID = original
    assert instance.ecfServiceTypeID == original



@given(instance=model_IServiceTypeID_strategy)
def test_model_iservicetypeid_ecfProtocols_setter(instance):
    original = instance.ecfProtocols
    instance.ecfProtocols = original
    assert instance.ecfProtocols == original



@given(instance=model_IServiceTypeID_strategy)
def test_model_iservicetypeid_ecfScopes_setter(instance):
    original = instance.ecfScopes
    instance.ecfScopes = original
    assert instance.ecfScopes == original

@given(instance=model_IHost_strategy)
@settings(max_examples=50)
def test_model_ihost_instantiation(instance):
    assert isinstance(instance, model_IHost)



@given(instance=model_IHost_strategy)
def test_model_ihost_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=model_IHost_strategy)
def test_model_ihost_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=model_INetwork_strategy)
@settings(max_examples=50)
def test_model_inetwork_instantiation(instance):
    assert isinstance(instance, model_INetwork)

@given(instance=model_IServiceID_strategy)
@settings(max_examples=50)
def test_model_iserviceid_instantiation(instance):
    assert isinstance(instance, model_IServiceID)



@given(instance=model_IServiceID_strategy)
def test_model_iserviceid_ecfServiceName_setter(instance):
    original = instance.ecfServiceName
    instance.ecfServiceName = original
    assert instance.ecfServiceName == original



@given(instance=model_IServiceID_strategy)
def test_model_iserviceid_ecfServiceID_setter(instance):
    original = instance.ecfServiceID
    instance.ecfServiceID = original
    assert instance.ecfServiceID == original

@given(instance=model_IServiceInfo_strategy)
@settings(max_examples=50)
def test_model_iserviceinfo_instantiation(instance):
    assert isinstance(instance, model_IServiceInfo)



@given(instance=model_IServiceInfo_strategy)
def test_model_iserviceinfo_ecfServiceInfo_setter(instance):
    original = instance.ecfServiceInfo
    instance.ecfServiceInfo = original
    assert instance.ecfServiceInfo == original



@given(instance=model_IServiceInfo_strategy)
def test_model_iserviceinfo_ecfPriority_setter(instance):
    original = instance.ecfPriority
    instance.ecfPriority = original
    assert instance.ecfPriority == original



@given(instance=model_IServiceInfo_strategy)
def test_model_iserviceinfo_ecfName_setter(instance):
    original = instance.ecfName
    instance.ecfName = original
    assert instance.ecfName == original



@given(instance=model_IServiceInfo_strategy)
def test_model_iserviceinfo_ecfWeight_setter(instance):
    original = instance.ecfWeight
    instance.ecfWeight = original
    assert instance.ecfWeight == original



@given(instance=model_IServiceInfo_strategy)
def test_model_iserviceinfo_ecfLocation_setter(instance):
    original = instance.ecfLocation
    instance.ecfLocation = original
    assert instance.ecfLocation == original
