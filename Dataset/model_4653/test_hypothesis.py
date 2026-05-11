import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    di::Style,
    di::View,
    di::DocumentRoot,
    di::EStringToStringMapEntry,
    View,
    di::Node,
    di::Diagram,
    di::Connector,
    di::Bendpoint,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_di::style_is_not_abstract():
    assert not inspect.isabstract(di::Style)


def test_di::style_constructor_exists():
    assert callable(di::Style.__init__)


def test_di::style_constructor_args():
    sig = inspect.signature(di::Style.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_di::style_has_value():
    assert hasattr(di::Style, "value")
    descriptor = None
    for klass in di::Style.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_di::style_has_name():
    assert hasattr(di::Style, "name")
    descriptor = None
    for klass in di::Style.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_di::view_is_not_abstract():
    assert not inspect.isabstract(di::View)


def test_di::view_constructor_exists():
    assert callable(di::View.__init__)


def test_di::view_constructor_args():
    sig = inspect.signature(di::View.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "sourceConnector" in params, "Missing parameter 'sourceConnector'"
    assert "definition" in params, "Missing parameter 'definition'"
    assert "targetConnector" in params, "Missing parameter 'targetConnector'"
    assert "context" in params, "Missing parameter 'context'"

def test_di::view_has_id():
    assert hasattr(di::View, "id")
    descriptor = None
    for klass in di::View.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_di::view_has_sourceConnector():
    assert hasattr(di::View, "sourceConnector")
    descriptor = None
    for klass in di::View.__mro__:
        if "sourceConnector" in klass.__dict__:
            descriptor = klass.__dict__["sourceConnector"]
            break
    assert isinstance(descriptor, property)

def test_di::view_has_definition():
    assert hasattr(di::View, "definition")
    descriptor = None
    for klass in di::View.__mro__:
        if "definition" in klass.__dict__:
            descriptor = klass.__dict__["definition"]
            break
    assert isinstance(descriptor, property)

def test_di::view_has_targetConnector():
    assert hasattr(di::View, "targetConnector")
    descriptor = None
    for klass in di::View.__mro__:
        if "targetConnector" in klass.__dict__:
            descriptor = klass.__dict__["targetConnector"]
            break
    assert isinstance(descriptor, property)

def test_di::view_has_context():
    assert hasattr(di::View, "context")
    descriptor = None
    for klass in di::View.__mro__:
        if "context" in klass.__dict__:
            descriptor = klass.__dict__["context"]
            break
    assert isinstance(descriptor, property)



def test_di::documentroot_is_not_abstract():
    assert not inspect.isabstract(di::DocumentRoot)


def test_di::documentroot_constructor_exists():
    assert callable(di::DocumentRoot.__init__)


def test_di::documentroot_constructor_args():
    sig = inspect.signature(di::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_di::documentroot_has_mixed():
    assert hasattr(di::DocumentRoot, "mixed")
    descriptor = None
    for klass in di::DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_di::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(di::EStringToStringMapEntry)


def test_di::estringtostringmapentry_constructor_exists():
    assert callable(di::EStringToStringMapEntry.__init__)


def test_di::estringtostringmapentry_constructor_args():
    sig = inspect.signature(di::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_view_is_not_abstract():
    assert not inspect.isabstract(View)


def test_view_constructor_exists():
    assert callable(View.__init__)


def test_view_constructor_args():
    sig = inspect.signature(View.__init__)
    params = list(sig.parameters.keys())



def test_di::node_is_not_abstract():
    assert not inspect.isabstract(di::Node)


def test_di::node_constructor_exists():
    assert callable(di::Node.__init__)


def test_di::node_constructor_args():
    sig = inspect.signature(di::Node.__init__)
    params = list(sig.parameters.keys())



def test_di::diagram_is_not_abstract():
    assert not inspect.isabstract(di::Diagram)


def test_di::diagram_constructor_exists():
    assert callable(di::Diagram.__init__)


def test_di::diagram_constructor_args():
    sig = inspect.signature(di::Diagram.__init__)
    params = list(sig.parameters.keys())



def test_di::connector_is_not_abstract():
    assert not inspect.isabstract(di::Connector)


def test_di::connector_constructor_exists():
    assert callable(di::Connector.__init__)


def test_di::connector_constructor_args():
    sig = inspect.signature(di::Connector.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"
    assert "target" in params, "Missing parameter 'target'"

def test_di::connector_has_source():
    assert hasattr(di::Connector, "source")
    descriptor = None
    for klass in di::Connector.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_di::connector_has_target():
    assert hasattr(di::Connector, "target")
    descriptor = None
    for klass in di::Connector.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)



def test_di::bendpoint_is_not_abstract():
    assert not inspect.isabstract(di::Bendpoint)


def test_di::bendpoint_constructor_exists():
    assert callable(di::Bendpoint.__init__)


def test_di::bendpoint_constructor_args():
    sig = inspect.signature(di::Bendpoint.__init__)
    params = list(sig.parameters.keys())
    assert "sourceX" in params, "Missing parameter 'sourceX'"
    assert "sourceY" in params, "Missing parameter 'sourceY'"
    assert "targetX" in params, "Missing parameter 'targetX'"
    assert "targetY" in params, "Missing parameter 'targetY'"

def test_di::bendpoint_has_sourceX():
    assert hasattr(di::Bendpoint, "sourceX")
    descriptor = None
    for klass in di::Bendpoint.__mro__:
        if "sourceX" in klass.__dict__:
            descriptor = klass.__dict__["sourceX"]
            break
    assert isinstance(descriptor, property)

def test_di::bendpoint_has_sourceY():
    assert hasattr(di::Bendpoint, "sourceY")
    descriptor = None
    for klass in di::Bendpoint.__mro__:
        if "sourceY" in klass.__dict__:
            descriptor = klass.__dict__["sourceY"]
            break
    assert isinstance(descriptor, property)

def test_di::bendpoint_has_targetX():
    assert hasattr(di::Bendpoint, "targetX")
    descriptor = None
    for klass in di::Bendpoint.__mro__:
        if "targetX" in klass.__dict__:
            descriptor = klass.__dict__["targetX"]
            break
    assert isinstance(descriptor, property)

def test_di::bendpoint_has_targetY():
    assert hasattr(di::Bendpoint, "targetY")
    descriptor = None
    for klass in di::Bendpoint.__mro__:
        if "targetY" in klass.__dict__:
            descriptor = klass.__dict__["targetY"]
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
di::Style_strategy = st.builds(
    di::Style,
    value=
        safe_text,
    name=
        safe_text
)
di::View_strategy = st.builds(
    di::View,
    id=
        safe_text,
    sourceConnector=
        safe_text,
    definition=
        safe_text,
    targetConnector=
        safe_text,
    context=
        safe_text
)
di::DocumentRoot_strategy = st.builds(
    di::DocumentRoot,
    mixed=
        safe_text
)
di::EStringToStringMapEntry_strategy = st.builds(
    di::EStringToStringMapEntry,
)
View_strategy = st.builds(
    View,
)
di::Node_strategy = st.builds(
    di::Node,
)
di::Diagram_strategy = st.builds(
    di::Diagram,
)
di::Connector_strategy = st.builds(
    di::Connector,
    source=
        safe_text,
    target=
        safe_text
)
di::Bendpoint_strategy = st.builds(
    di::Bendpoint,
    sourceX=
        safe_text,
    sourceY=
        safe_text,
    targetX=
        safe_text,
    targetY=
        safe_text
)

@given(instance=di::Style_strategy)
@settings(max_examples=50)
def test_di::style_instantiation(instance):
    assert isinstance(instance, di::Style)

@given(instance=di::Style_strategy)
def test_di::style_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=di::Style_strategy)
def test_di::style_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=di::Style_strategy)
def test_di::style_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=di::Style_strategy)
def test_di::style_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=di::View_strategy)
@settings(max_examples=50)
def test_di::view_instantiation(instance):
    assert isinstance(instance, di::View)

@given(instance=di::View_strategy)
def test_di::view_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=di::View_strategy)
def test_di::view_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=di::View_strategy)
def test_di::view_sourceConnector_type(instance):
    assert isinstance(instance.sourceConnector, str)


@given(instance=di::View_strategy)
def test_di::view_sourceConnector_setter(instance):
    original = instance.sourceConnector
    instance.sourceConnector = original
    assert instance.sourceConnector == original

@given(instance=di::View_strategy)
def test_di::view_definition_type(instance):
    assert isinstance(instance.definition, str)


@given(instance=di::View_strategy)
def test_di::view_definition_setter(instance):
    original = instance.definition
    instance.definition = original
    assert instance.definition == original

@given(instance=di::View_strategy)
def test_di::view_targetConnector_type(instance):
    assert isinstance(instance.targetConnector, str)


@given(instance=di::View_strategy)
def test_di::view_targetConnector_setter(instance):
    original = instance.targetConnector
    instance.targetConnector = original
    assert instance.targetConnector == original

@given(instance=di::View_strategy)
def test_di::view_context_type(instance):
    assert isinstance(instance.context, str)


@given(instance=di::View_strategy)
def test_di::view_context_setter(instance):
    original = instance.context
    instance.context = original
    assert instance.context == original

@given(instance=di::DocumentRoot_strategy)
@settings(max_examples=50)
def test_di::documentroot_instantiation(instance):
    assert isinstance(instance, di::DocumentRoot)

@given(instance=di::DocumentRoot_strategy)
def test_di::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=di::DocumentRoot_strategy)
def test_di::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=di::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_di::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, di::EStringToStringMapEntry)

@given(instance=View_strategy)
@settings(max_examples=50)
def test_view_instantiation(instance):
    assert isinstance(instance, View)

@given(instance=di::Node_strategy)
@settings(max_examples=50)
def test_di::node_instantiation(instance):
    assert isinstance(instance, di::Node)

@given(instance=di::Diagram_strategy)
@settings(max_examples=50)
def test_di::diagram_instantiation(instance):
    assert isinstance(instance, di::Diagram)

@given(instance=di::Connector_strategy)
@settings(max_examples=50)
def test_di::connector_instantiation(instance):
    assert isinstance(instance, di::Connector)

@given(instance=di::Connector_strategy)
def test_di::connector_source_type(instance):
    assert isinstance(instance.source, str)


@given(instance=di::Connector_strategy)
def test_di::connector_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=di::Connector_strategy)
def test_di::connector_target_type(instance):
    assert isinstance(instance.target, str)


@given(instance=di::Connector_strategy)
def test_di::connector_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original

@given(instance=di::Bendpoint_strategy)
@settings(max_examples=50)
def test_di::bendpoint_instantiation(instance):
    assert isinstance(instance, di::Bendpoint)

@given(instance=di::Bendpoint_strategy)
def test_di::bendpoint_sourceX_type(instance):
    assert isinstance(instance.sourceX, str)


@given(instance=di::Bendpoint_strategy)
def test_di::bendpoint_sourceX_setter(instance):
    original = instance.sourceX
    instance.sourceX = original
    assert instance.sourceX == original

@given(instance=di::Bendpoint_strategy)
def test_di::bendpoint_sourceY_type(instance):
    assert isinstance(instance.sourceY, str)


@given(instance=di::Bendpoint_strategy)
def test_di::bendpoint_sourceY_setter(instance):
    original = instance.sourceY
    instance.sourceY = original
    assert instance.sourceY == original

@given(instance=di::Bendpoint_strategy)
def test_di::bendpoint_targetX_type(instance):
    assert isinstance(instance.targetX, str)


@given(instance=di::Bendpoint_strategy)
def test_di::bendpoint_targetX_setter(instance):
    original = instance.targetX
    instance.targetX = original
    assert instance.targetX == original

@given(instance=di::Bendpoint_strategy)
def test_di::bendpoint_targetY_type(instance):
    assert isinstance(instance.targetY, str)


@given(instance=di::Bendpoint_strategy)
def test_di::bendpoint_targetY_setter(instance):
    original = instance.targetY
    instance.targetY = original
    assert instance.targetY == original
