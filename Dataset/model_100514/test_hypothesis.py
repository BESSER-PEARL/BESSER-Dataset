import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    RequirementSourceConf::Scope,
    RequirementSourceConf::MappingElement,
    RequirementSourceConf::EStringToStringMapEntry,
    RequirementSourceConf::RequirementSource,
    RequirementSourceConf::RequirementSources,
    RequirementSourceConf::RequirementsContainer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_requirementsourceconf::scope_is_not_abstract():
    assert not inspect.isabstract(RequirementSourceConf::Scope)


def test_requirementsourceconf::scope_constructor_exists():
    assert callable(RequirementSourceConf::Scope.__init__)


def test_requirementsourceconf::scope_constructor_args():
    sig = inspect.signature(RequirementSourceConf::Scope.__init__)
    params = list(sig.parameters.keys())



def test_requirementsourceconf::mappingelement_is_not_abstract():
    assert not inspect.isabstract(RequirementSourceConf::MappingElement)


def test_requirementsourceconf::mappingelement_constructor_exists():
    assert callable(RequirementSourceConf::MappingElement.__init__)


def test_requirementsourceconf::mappingelement_constructor_args():
    sig = inspect.signature(RequirementSourceConf::MappingElement.__init__)
    params = list(sig.parameters.keys())



def test_requirementsourceconf::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(RequirementSourceConf::EStringToStringMapEntry)


def test_requirementsourceconf::estringtostringmapentry_constructor_exists():
    assert callable(RequirementSourceConf::EStringToStringMapEntry.__init__)


def test_requirementsourceconf::estringtostringmapentry_constructor_args():
    sig = inspect.signature(RequirementSourceConf::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_requirementsourceconf::requirementsource_is_not_abstract():
    assert not inspect.isabstract(RequirementSourceConf::RequirementSource)


def test_requirementsourceconf::requirementsource_constructor_exists():
    assert callable(RequirementSourceConf::RequirementSource.__init__)


def test_requirementsourceconf::requirementsource_constructor_args():
    sig = inspect.signature(RequirementSourceConf::RequirementSource.__init__)
    params = list(sig.parameters.keys())
    assert "repositoryURI" in params, "Missing parameter 'repositoryURI'"
    assert "dataModelURI" in params, "Missing parameter 'dataModelURI'"
    assert "name" in params, "Missing parameter 'name'"
    assert "destinationURI" in params, "Missing parameter 'destinationURI'"
    assert "connectorId" in params, "Missing parameter 'connectorId'"

def test_requirementsourceconf::requirementsource_has_repositoryURI():
    assert hasattr(RequirementSourceConf::RequirementSource, "repositoryURI")
    descriptor = None
    for klass in RequirementSourceConf::RequirementSource.__mro__:
        if "repositoryURI" in klass.__dict__:
            descriptor = klass.__dict__["repositoryURI"]
            break
    assert isinstance(descriptor, property)

def test_requirementsourceconf::requirementsource_has_dataModelURI():
    assert hasattr(RequirementSourceConf::RequirementSource, "dataModelURI")
    descriptor = None
    for klass in RequirementSourceConf::RequirementSource.__mro__:
        if "dataModelURI" in klass.__dict__:
            descriptor = klass.__dict__["dataModelURI"]
            break
    assert isinstance(descriptor, property)

def test_requirementsourceconf::requirementsource_has_name():
    assert hasattr(RequirementSourceConf::RequirementSource, "name")
    descriptor = None
    for klass in RequirementSourceConf::RequirementSource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_requirementsourceconf::requirementsource_has_destinationURI():
    assert hasattr(RequirementSourceConf::RequirementSource, "destinationURI")
    descriptor = None
    for klass in RequirementSourceConf::RequirementSource.__mro__:
        if "destinationURI" in klass.__dict__:
            descriptor = klass.__dict__["destinationURI"]
            break
    assert isinstance(descriptor, property)

def test_requirementsourceconf::requirementsource_has_connectorId():
    assert hasattr(RequirementSourceConf::RequirementSource, "connectorId")
    descriptor = None
    for klass in RequirementSourceConf::RequirementSource.__mro__:
        if "connectorId" in klass.__dict__:
            descriptor = klass.__dict__["connectorId"]
            break
    assert isinstance(descriptor, property)



def test_requirementsourceconf::requirementsources_is_not_abstract():
    assert not inspect.isabstract(RequirementSourceConf::RequirementSources)


def test_requirementsourceconf::requirementsources_constructor_exists():
    assert callable(RequirementSourceConf::RequirementSources.__init__)


def test_requirementsourceconf::requirementsources_constructor_args():
    sig = inspect.signature(RequirementSourceConf::RequirementSources.__init__)
    params = list(sig.parameters.keys())



def test_requirementsourceconf::requirementscontainer_is_not_abstract():
    assert not inspect.isabstract(RequirementSourceConf::RequirementsContainer)


def test_requirementsourceconf::requirementscontainer_constructor_exists():
    assert callable(RequirementSourceConf::RequirementsContainer.__init__)


def test_requirementsourceconf::requirementscontainer_constructor_args():
    sig = inspect.signature(RequirementSourceConf::RequirementsContainer.__init__)
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
RequirementSourceConf::Scope_strategy = st.builds(
    RequirementSourceConf::Scope,
)
RequirementSourceConf::MappingElement_strategy = st.builds(
    RequirementSourceConf::MappingElement,
)
RequirementSourceConf::EStringToStringMapEntry_strategy = st.builds(
    RequirementSourceConf::EStringToStringMapEntry,
)
RequirementSourceConf::RequirementSource_strategy = st.builds(
    RequirementSourceConf::RequirementSource,
    repositoryURI=
        safe_text,
    dataModelURI=
        safe_text,
    name=
        safe_text,
    destinationURI=
        safe_text,
    connectorId=
        safe_text
)
RequirementSourceConf::RequirementSources_strategy = st.builds(
    RequirementSourceConf::RequirementSources,
)
RequirementSourceConf::RequirementsContainer_strategy = st.builds(
    RequirementSourceConf::RequirementsContainer,
)

@given(instance=RequirementSourceConf::Scope_strategy)
@settings(max_examples=50)
def test_requirementsourceconf::scope_instantiation(instance):
    assert isinstance(instance, RequirementSourceConf::Scope)

@given(instance=RequirementSourceConf::MappingElement_strategy)
@settings(max_examples=50)
def test_requirementsourceconf::mappingelement_instantiation(instance):
    assert isinstance(instance, RequirementSourceConf::MappingElement)

@given(instance=RequirementSourceConf::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_requirementsourceconf::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, RequirementSourceConf::EStringToStringMapEntry)

@given(instance=RequirementSourceConf::RequirementSource_strategy)
@settings(max_examples=50)
def test_requirementsourceconf::requirementsource_instantiation(instance):
    assert isinstance(instance, RequirementSourceConf::RequirementSource)

@given(instance=RequirementSourceConf::RequirementSource_strategy)
def test_requirementsourceconf::requirementsource_repositoryURI_type(instance):
    assert isinstance(instance.repositoryURI, str)


@given(instance=RequirementSourceConf::RequirementSource_strategy)
def test_requirementsourceconf::requirementsource_repositoryURI_setter(instance):
    original = instance.repositoryURI
    instance.repositoryURI = original
    assert instance.repositoryURI == original

@given(instance=RequirementSourceConf::RequirementSource_strategy)
def test_requirementsourceconf::requirementsource_dataModelURI_type(instance):
    assert isinstance(instance.dataModelURI, str)


@given(instance=RequirementSourceConf::RequirementSource_strategy)
def test_requirementsourceconf::requirementsource_dataModelURI_setter(instance):
    original = instance.dataModelURI
    instance.dataModelURI = original
    assert instance.dataModelURI == original

@given(instance=RequirementSourceConf::RequirementSource_strategy)
def test_requirementsourceconf::requirementsource_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=RequirementSourceConf::RequirementSource_strategy)
def test_requirementsourceconf::requirementsource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RequirementSourceConf::RequirementSource_strategy)
def test_requirementsourceconf::requirementsource_destinationURI_type(instance):
    assert isinstance(instance.destinationURI, str)


@given(instance=RequirementSourceConf::RequirementSource_strategy)
def test_requirementsourceconf::requirementsource_destinationURI_setter(instance):
    original = instance.destinationURI
    instance.destinationURI = original
    assert instance.destinationURI == original

@given(instance=RequirementSourceConf::RequirementSource_strategy)
def test_requirementsourceconf::requirementsource_connectorId_type(instance):
    assert isinstance(instance.connectorId, str)


@given(instance=RequirementSourceConf::RequirementSource_strategy)
def test_requirementsourceconf::requirementsource_connectorId_setter(instance):
    original = instance.connectorId
    instance.connectorId = original
    assert instance.connectorId == original

@given(instance=RequirementSourceConf::RequirementSources_strategy)
@settings(max_examples=50)
def test_requirementsourceconf::requirementsources_instantiation(instance):
    assert isinstance(instance, RequirementSourceConf::RequirementSources)

@given(instance=RequirementSourceConf::RequirementsContainer_strategy)
@settings(max_examples=50)
def test_requirementsourceconf::requirementscontainer_instantiation(instance):
    assert isinstance(instance, RequirementSourceConf::RequirementsContainer)
