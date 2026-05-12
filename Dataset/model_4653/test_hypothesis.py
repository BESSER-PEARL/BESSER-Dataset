import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    di_Style,
    di_View,
    di_DocumentRoot,
    di_EStringToStringMapEntry,
    View,
    di_Node,
    di_Diagram,
    di_Connector,
    di_Bendpoint,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_di_style_is_not_abstract():
    assert not inspect.isabstract(di_Style)


def test_di_style_constructor_exists():
    assert callable(di_Style.__init__)


def test_di_style_constructor_args():
    sig = inspect.signature(di_Style.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_di_style_has_value():
    assert hasattr(di_Style, "value")
    descriptor = None
    for klass in di_Style.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_di_style_has_name():
    assert hasattr(di_Style, "name")
    descriptor = None
    for klass in di_Style.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_di_view_is_not_abstract():
    assert not inspect.isabstract(di_View)


def test_di_view_constructor_exists():
    assert callable(di_View.__init__)


def test_di_view_constructor_args():
    sig = inspect.signature(di_View.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "context" in params, "Missing parameter 'context'"
    assert "targetConnector" in params, "Missing parameter 'targetConnector'"
    assert "sourceConnector" in params, "Missing parameter 'sourceConnector'"
    assert "definition" in params, "Missing parameter 'definition'"

def test_di_view_has_id():
    assert hasattr(di_View, "id")
    descriptor = None
    for klass in di_View.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_di_view_has_context():
    assert hasattr(di_View, "context")
    descriptor = None
    for klass in di_View.__mro__:
        if "context" in klass.__dict__:
            descriptor = klass.__dict__["context"]
            break
    assert isinstance(descriptor, property)

def test_di_view_has_targetConnector():
    assert hasattr(di_View, "targetConnector")
    descriptor = None
    for klass in di_View.__mro__:
        if "targetConnector" in klass.__dict__:
            descriptor = klass.__dict__["targetConnector"]
            break
    assert isinstance(descriptor, property)

def test_di_view_has_sourceConnector():
    assert hasattr(di_View, "sourceConnector")
    descriptor = None
    for klass in di_View.__mro__:
        if "sourceConnector" in klass.__dict__:
            descriptor = klass.__dict__["sourceConnector"]
            break
    assert isinstance(descriptor, property)

def test_di_view_has_definition():
    assert hasattr(di_View, "definition")
    descriptor = None
    for klass in di_View.__mro__:
        if "definition" in klass.__dict__:
            descriptor = klass.__dict__["definition"]
            break
    assert isinstance(descriptor, property)



def test_di_documentroot_is_not_abstract():
    assert not inspect.isabstract(di_DocumentRoot)


def test_di_documentroot_constructor_exists():
    assert callable(di_DocumentRoot.__init__)


def test_di_documentroot_constructor_args():
    sig = inspect.signature(di_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_di_documentroot_has_mixed():
    assert hasattr(di_DocumentRoot, "mixed")
    descriptor = None
    for klass in di_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_di_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(di_EStringToStringMapEntry)


def test_di_estringtostringmapentry_constructor_exists():
    assert callable(di_EStringToStringMapEntry.__init__)


def test_di_estringtostringmapentry_constructor_args():
    sig = inspect.signature(di_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_view_is_not_abstract():
    assert not inspect.isabstract(View)


def test_view_constructor_exists():
    assert callable(View.__init__)


def test_view_constructor_args():
    sig = inspect.signature(View.__init__)
    params = list(sig.parameters.keys())



def test_di_node_is_not_abstract():
    assert not inspect.isabstract(di_Node)


def test_di_node_constructor_exists():
    assert callable(di_Node.__init__)


def test_di_node_constructor_args():
    sig = inspect.signature(di_Node.__init__)
    params = list(sig.parameters.keys())



def test_di_diagram_is_not_abstract():
    assert not inspect.isabstract(di_Diagram)


def test_di_diagram_constructor_exists():
    assert callable(di_Diagram.__init__)


def test_di_diagram_constructor_args():
    sig = inspect.signature(di_Diagram.__init__)
    params = list(sig.parameters.keys())



def test_di_connector_is_not_abstract():
    assert not inspect.isabstract(di_Connector)


def test_di_connector_constructor_exists():
    assert callable(di_Connector.__init__)


def test_di_connector_constructor_args():
    sig = inspect.signature(di_Connector.__init__)
    params = list(sig.parameters.keys())
    assert "target" in params, "Missing parameter 'target'"
    assert "source" in params, "Missing parameter 'source'"

def test_di_connector_has_target():
    assert hasattr(di_Connector, "target")
    descriptor = None
    for klass in di_Connector.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)

def test_di_connector_has_source():
    assert hasattr(di_Connector, "source")
    descriptor = None
    for klass in di_Connector.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)



def test_di_bendpoint_is_not_abstract():
    assert not inspect.isabstract(di_Bendpoint)


def test_di_bendpoint_constructor_exists():
    assert callable(di_Bendpoint.__init__)


def test_di_bendpoint_constructor_args():
    sig = inspect.signature(di_Bendpoint.__init__)
    params = list(sig.parameters.keys())
    assert "targetX" in params, "Missing parameter 'targetX'"
    assert "sourceY" in params, "Missing parameter 'sourceY'"
    assert "targetY" in params, "Missing parameter 'targetY'"
    assert "sourceX" in params, "Missing parameter 'sourceX'"

def test_di_bendpoint_has_targetX():
    assert hasattr(di_Bendpoint, "targetX")
    descriptor = None
    for klass in di_Bendpoint.__mro__:
        if "targetX" in klass.__dict__:
            descriptor = klass.__dict__["targetX"]
            break
    assert isinstance(descriptor, property)

def test_di_bendpoint_has_sourceY():
    assert hasattr(di_Bendpoint, "sourceY")
    descriptor = None
    for klass in di_Bendpoint.__mro__:
        if "sourceY" in klass.__dict__:
            descriptor = klass.__dict__["sourceY"]
            break
    assert isinstance(descriptor, property)

def test_di_bendpoint_has_targetY():
    assert hasattr(di_Bendpoint, "targetY")
    descriptor = None
    for klass in di_Bendpoint.__mro__:
        if "targetY" in klass.__dict__:
            descriptor = klass.__dict__["targetY"]
            break
    assert isinstance(descriptor, property)

def test_di_bendpoint_has_sourceX():
    assert hasattr(di_Bendpoint, "sourceX")
    descriptor = None
    for klass in di_Bendpoint.__mro__:
        if "sourceX" in klass.__dict__:
            descriptor = klass.__dict__["sourceX"]
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
di_Style_strategy = st.builds(
    di_Style,
    value=
        safe_text,
    name=
        safe_text
)
di_View_strategy = st.builds(
    di_View,
    id=
        safe_text,
    context=
        safe_text,
    targetConnector=
        safe_text,
    sourceConnector=
        safe_text,
    definition=
        safe_text
)
di_DocumentRoot_strategy = st.builds(
    di_DocumentRoot,
    mixed=
        safe_text
)
di_EStringToStringMapEntry_strategy = st.builds(
    di_EStringToStringMapEntry,
)
View_strategy = st.builds(
    View,
)
di_Node_strategy = st.builds(
    di_Node,
)
di_Diagram_strategy = st.builds(
    di_Diagram,
)
di_Connector_strategy = st.builds(
    di_Connector,
    target=
        safe_text,
    source=
        safe_text
)
di_Bendpoint_strategy = st.builds(
    di_Bendpoint,
    targetX=
        safe_text,
    sourceY=
        safe_text,
    targetY=
        safe_text,
    sourceX=
        safe_text
)

@given(instance=di_Style_strategy)
@settings(max_examples=50)
def test_di_style_instantiation(instance):
    assert isinstance(instance, di_Style)



@given(instance=di_Style_strategy)
def test_di_style_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=di_Style_strategy)
def test_di_style_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=di_View_strategy)
@settings(max_examples=50)
def test_di_view_instantiation(instance):
    assert isinstance(instance, di_View)



@given(instance=di_View_strategy)
def test_di_view_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=di_View_strategy)
def test_di_view_context_setter(instance):
    original = instance.context
    instance.context = original
    assert instance.context == original



@given(instance=di_View_strategy)
def test_di_view_targetConnector_setter(instance):
    original = instance.targetConnector
    instance.targetConnector = original
    assert instance.targetConnector == original



@given(instance=di_View_strategy)
def test_di_view_sourceConnector_setter(instance):
    original = instance.sourceConnector
    instance.sourceConnector = original
    assert instance.sourceConnector == original



@given(instance=di_View_strategy)
def test_di_view_definition_setter(instance):
    original = instance.definition
    instance.definition = original
    assert instance.definition == original

@given(instance=di_DocumentRoot_strategy)
@settings(max_examples=50)
def test_di_documentroot_instantiation(instance):
    assert isinstance(instance, di_DocumentRoot)



@given(instance=di_DocumentRoot_strategy)
def test_di_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=di_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_di_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, di_EStringToStringMapEntry)

@given(instance=View_strategy)
@settings(max_examples=50)
def test_view_instantiation(instance):
    assert isinstance(instance, View)

@given(instance=di_Node_strategy)
@settings(max_examples=50)
def test_di_node_instantiation(instance):
    assert isinstance(instance, di_Node)

@given(instance=di_Diagram_strategy)
@settings(max_examples=50)
def test_di_diagram_instantiation(instance):
    assert isinstance(instance, di_Diagram)

@given(instance=di_Connector_strategy)
@settings(max_examples=50)
def test_di_connector_instantiation(instance):
    assert isinstance(instance, di_Connector)



@given(instance=di_Connector_strategy)
def test_di_connector_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original



@given(instance=di_Connector_strategy)
def test_di_connector_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=di_Bendpoint_strategy)
@settings(max_examples=50)
def test_di_bendpoint_instantiation(instance):
    assert isinstance(instance, di_Bendpoint)



@given(instance=di_Bendpoint_strategy)
def test_di_bendpoint_targetX_setter(instance):
    original = instance.targetX
    instance.targetX = original
    assert instance.targetX == original



@given(instance=di_Bendpoint_strategy)
def test_di_bendpoint_sourceY_setter(instance):
    original = instance.sourceY
    instance.sourceY = original
    assert instance.sourceY == original



@given(instance=di_Bendpoint_strategy)
def test_di_bendpoint_targetY_setter(instance):
    original = instance.targetY
    instance.targetY = original
    assert instance.targetY == original



@given(instance=di_Bendpoint_strategy)
def test_di_bendpoint_sourceX_setter(instance):
    original = instance.sourceX
    instance.sourceX = original
    assert instance.sourceX == original
