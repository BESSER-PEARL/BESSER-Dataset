import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    RequirementSourceConf_Scope,
    RequirementSourceConf_MappingElement,
    RequirementSourceConf_EStringToStringMapEntry,
    RequirementSourceConf_RequirementSource,
    RequirementSourceConf_RequirementSources,
    RequirementSourceConf_RequirementsContainer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_requirementsourceconf_scope_is_not_abstract():
    assert not inspect.isabstract(RequirementSourceConf_Scope)


def test_requirementsourceconf_scope_constructor_exists():
    assert callable(RequirementSourceConf_Scope.__init__)


def test_requirementsourceconf_scope_constructor_args():
    sig = inspect.signature(RequirementSourceConf_Scope.__init__)
    params = list(sig.parameters.keys())



def test_requirementsourceconf_mappingelement_is_not_abstract():
    assert not inspect.isabstract(RequirementSourceConf_MappingElement)


def test_requirementsourceconf_mappingelement_constructor_exists():
    assert callable(RequirementSourceConf_MappingElement.__init__)


def test_requirementsourceconf_mappingelement_constructor_args():
    sig = inspect.signature(RequirementSourceConf_MappingElement.__init__)
    params = list(sig.parameters.keys())



def test_requirementsourceconf_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(RequirementSourceConf_EStringToStringMapEntry)


def test_requirementsourceconf_estringtostringmapentry_constructor_exists():
    assert callable(RequirementSourceConf_EStringToStringMapEntry.__init__)


def test_requirementsourceconf_estringtostringmapentry_constructor_args():
    sig = inspect.signature(RequirementSourceConf_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_requirementsourceconf_requirementsource_is_not_abstract():
    assert not inspect.isabstract(RequirementSourceConf_RequirementSource)


def test_requirementsourceconf_requirementsource_constructor_exists():
    assert callable(RequirementSourceConf_RequirementSource.__init__)


def test_requirementsourceconf_requirementsource_constructor_args():
    sig = inspect.signature(RequirementSourceConf_RequirementSource.__init__)
    params = list(sig.parameters.keys())
    assert "repositoryURI" in params, "Missing parameter 'repositoryURI'"
    assert "dataModelURI" in params, "Missing parameter 'dataModelURI'"
    assert "destinationURI" in params, "Missing parameter 'destinationURI'"
    assert "name" in params, "Missing parameter 'name'"
    assert "connectorId" in params, "Missing parameter 'connectorId'"

def test_requirementsourceconf_requirementsource_has_repositoryURI():
    assert hasattr(RequirementSourceConf_RequirementSource, "repositoryURI")
    descriptor = None
    for klass in RequirementSourceConf_RequirementSource.__mro__:
        if "repositoryURI" in klass.__dict__:
            descriptor = klass.__dict__["repositoryURI"]
            break
    assert isinstance(descriptor, property)

def test_requirementsourceconf_requirementsource_has_dataModelURI():
    assert hasattr(RequirementSourceConf_RequirementSource, "dataModelURI")
    descriptor = None
    for klass in RequirementSourceConf_RequirementSource.__mro__:
        if "dataModelURI" in klass.__dict__:
            descriptor = klass.__dict__["dataModelURI"]
            break
    assert isinstance(descriptor, property)

def test_requirementsourceconf_requirementsource_has_destinationURI():
    assert hasattr(RequirementSourceConf_RequirementSource, "destinationURI")
    descriptor = None
    for klass in RequirementSourceConf_RequirementSource.__mro__:
        if "destinationURI" in klass.__dict__:
            descriptor = klass.__dict__["destinationURI"]
            break
    assert isinstance(descriptor, property)

def test_requirementsourceconf_requirementsource_has_name():
    assert hasattr(RequirementSourceConf_RequirementSource, "name")
    descriptor = None
    for klass in RequirementSourceConf_RequirementSource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_requirementsourceconf_requirementsource_has_connectorId():
    assert hasattr(RequirementSourceConf_RequirementSource, "connectorId")
    descriptor = None
    for klass in RequirementSourceConf_RequirementSource.__mro__:
        if "connectorId" in klass.__dict__:
            descriptor = klass.__dict__["connectorId"]
            break
    assert isinstance(descriptor, property)



def test_requirementsourceconf_requirementsources_is_not_abstract():
    assert not inspect.isabstract(RequirementSourceConf_RequirementSources)


def test_requirementsourceconf_requirementsources_constructor_exists():
    assert callable(RequirementSourceConf_RequirementSources.__init__)


def test_requirementsourceconf_requirementsources_constructor_args():
    sig = inspect.signature(RequirementSourceConf_RequirementSources.__init__)
    params = list(sig.parameters.keys())



def test_requirementsourceconf_requirementscontainer_is_not_abstract():
    assert not inspect.isabstract(RequirementSourceConf_RequirementsContainer)


def test_requirementsourceconf_requirementscontainer_constructor_exists():
    assert callable(RequirementSourceConf_RequirementsContainer.__init__)


def test_requirementsourceconf_requirementscontainer_constructor_args():
    sig = inspect.signature(RequirementSourceConf_RequirementsContainer.__init__)
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
RequirementSourceConf_Scope_strategy = st.builds(
    RequirementSourceConf_Scope,
)
RequirementSourceConf_MappingElement_strategy = st.builds(
    RequirementSourceConf_MappingElement,
)
RequirementSourceConf_EStringToStringMapEntry_strategy = st.builds(
    RequirementSourceConf_EStringToStringMapEntry,
)
RequirementSourceConf_RequirementSource_strategy = st.builds(
    RequirementSourceConf_RequirementSource,
    repositoryURI=
        safe_text,
    dataModelURI=
        safe_text,
    destinationURI=
        safe_text,
    name=
        safe_text,
    connectorId=
        safe_text
)
RequirementSourceConf_RequirementSources_strategy = st.builds(
    RequirementSourceConf_RequirementSources,
)
RequirementSourceConf_RequirementsContainer_strategy = st.builds(
    RequirementSourceConf_RequirementsContainer,
)

@given(instance=RequirementSourceConf_Scope_strategy)
@settings(max_examples=50)
def test_requirementsourceconf_scope_instantiation(instance):
    assert isinstance(instance, RequirementSourceConf_Scope)

@given(instance=RequirementSourceConf_MappingElement_strategy)
@settings(max_examples=50)
def test_requirementsourceconf_mappingelement_instantiation(instance):
    assert isinstance(instance, RequirementSourceConf_MappingElement)

@given(instance=RequirementSourceConf_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_requirementsourceconf_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, RequirementSourceConf_EStringToStringMapEntry)

@given(instance=RequirementSourceConf_RequirementSource_strategy)
@settings(max_examples=50)
def test_requirementsourceconf_requirementsource_instantiation(instance):
    assert isinstance(instance, RequirementSourceConf_RequirementSource)



@given(instance=RequirementSourceConf_RequirementSource_strategy)
def test_requirementsourceconf_requirementsource_repositoryURI_setter(instance):
    original = instance.repositoryURI
    instance.repositoryURI = original
    assert instance.repositoryURI == original



@given(instance=RequirementSourceConf_RequirementSource_strategy)
def test_requirementsourceconf_requirementsource_dataModelURI_setter(instance):
    original = instance.dataModelURI
    instance.dataModelURI = original
    assert instance.dataModelURI == original



@given(instance=RequirementSourceConf_RequirementSource_strategy)
def test_requirementsourceconf_requirementsource_destinationURI_setter(instance):
    original = instance.destinationURI
    instance.destinationURI = original
    assert instance.destinationURI == original



@given(instance=RequirementSourceConf_RequirementSource_strategy)
def test_requirementsourceconf_requirementsource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=RequirementSourceConf_RequirementSource_strategy)
def test_requirementsourceconf_requirementsource_connectorId_setter(instance):
    original = instance.connectorId
    instance.connectorId = original
    assert instance.connectorId == original

@given(instance=RequirementSourceConf_RequirementSources_strategy)
@settings(max_examples=50)
def test_requirementsourceconf_requirementsources_instantiation(instance):
    assert isinstance(instance, RequirementSourceConf_RequirementSources)

@given(instance=RequirementSourceConf_RequirementsContainer_strategy)
@settings(max_examples=50)
def test_requirementsourceconf_requirementscontainer_instantiation(instance):
    assert isinstance(instance, RequirementSourceConf_RequirementsContainer)
