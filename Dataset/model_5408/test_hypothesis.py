import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    emfta_Gate,
    emfta_Event,
    emfta_FTAModel,
    GateType,
    EventType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_emfta_gate_is_not_abstract():
    assert not inspect.isabstract(emfta_Gate)


def test_emfta_gate_constructor_exists():
    assert callable(emfta_Gate.__init__)


def test_emfta_gate_constructor_args():
    sig = inspect.signature(emfta_Gate.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "nbOccurrences" in params, "Missing parameter 'nbOccurrences'"
    assert "type" in params, "Missing parameter 'type'"

def test_emfta_gate_has_description():
    assert hasattr(emfta_Gate, "description")
    descriptor = None
    for klass in emfta_Gate.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_emfta_gate_has_nbOccurrences():
    assert hasattr(emfta_Gate, "nbOccurrences")
    descriptor = None
    for klass in emfta_Gate.__mro__:
        if "nbOccurrences" in klass.__dict__:
            descriptor = klass.__dict__["nbOccurrences"]
            break
    assert isinstance(descriptor, property)

def test_emfta_gate_has_type():
    assert hasattr(emfta_Gate, "type")
    descriptor = None
    for klass in emfta_Gate.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_emfta_event_is_not_abstract():
    assert not inspect.isabstract(emfta_Event)


def test_emfta_event_constructor_exists():
    assert callable(emfta_Event.__init__)


def test_emfta_event_constructor_args():
    sig = inspect.signature(emfta_Event.__init__)
    params = list(sig.parameters.keys())
    assert "referenceCount" in params, "Missing parameter 'referenceCount'"
    assert "description" in params, "Missing parameter 'description'"
    assert "relatedObject" in params, "Missing parameter 'relatedObject'"
    assert "probability" in params, "Missing parameter 'probability'"
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_emfta_event_has_referenceCount():
    assert hasattr(emfta_Event, "referenceCount")
    descriptor = None
    for klass in emfta_Event.__mro__:
        if "referenceCount" in klass.__dict__:
            descriptor = klass.__dict__["referenceCount"]
            break
    assert isinstance(descriptor, property)

def test_emfta_event_has_description():
    assert hasattr(emfta_Event, "description")
    descriptor = None
    for klass in emfta_Event.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_emfta_event_has_relatedObject():
    assert hasattr(emfta_Event, "relatedObject")
    descriptor = None
    for klass in emfta_Event.__mro__:
        if "relatedObject" in klass.__dict__:
            descriptor = klass.__dict__["relatedObject"]
            break
    assert isinstance(descriptor, property)

def test_emfta_event_has_probability():
    assert hasattr(emfta_Event, "probability")
    descriptor = None
    for klass in emfta_Event.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)

def test_emfta_event_has_name():
    assert hasattr(emfta_Event, "name")
    descriptor = None
    for klass in emfta_Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_emfta_event_has_type():
    assert hasattr(emfta_Event, "type")
    descriptor = None
    for klass in emfta_Event.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_emfta_ftamodel_is_not_abstract():
    assert not inspect.isabstract(emfta_FTAModel)


def test_emfta_ftamodel_constructor_exists():
    assert callable(emfta_FTAModel.__init__)


def test_emfta_ftamodel_constructor_args():
    sig = inspect.signature(emfta_FTAModel.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "comments" in params, "Missing parameter 'comments'"

def test_emfta_ftamodel_has_description():
    assert hasattr(emfta_FTAModel, "description")
    descriptor = None
    for klass in emfta_FTAModel.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_emfta_ftamodel_has_name():
    assert hasattr(emfta_FTAModel, "name")
    descriptor = None
    for klass in emfta_FTAModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_emfta_ftamodel_has_comments():
    assert hasattr(emfta_FTAModel, "comments")
    descriptor = None
    for klass in emfta_FTAModel.__mro__:
        if "comments" in klass.__dict__:
            descriptor = klass.__dict__["comments"]
            break
    assert isinstance(descriptor, property)

def test_gatetype_exists():
    # Check that the Enumeration exists
    assert GateType is not None

def test_gatetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GateType]
    expected_literals = [
        "ORLESS",
        "OR",
        "PRIORITY_OR",
        "PRIORITY_AND",
        "INHIBIT",
        "AND",
        "ORMORE",
        "INTERMEDIATE",
        "XOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GateType"

def test_eventtype_exists():
    # Check that the Enumeration exists
    assert EventType is not None

def test_eventtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EventType]
    expected_literals = [
        "Undevelopped",
        "Basic",
        "External",
        "Conditioning",
        "Intermediate",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EventType"


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
emfta_Gate_strategy = st.builds(
    emfta_Gate,
    description=
        safe_text,
    nbOccurrences=
        st.integers(),
    type=
        safe_text
)
emfta_Event_strategy = st.builds(
    emfta_Event,
    referenceCount=
        st.integers(),
    description=
        safe_text,
    relatedObject=
        safe_text,
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text,
    type=
        safe_text
)
emfta_FTAModel_strategy = st.builds(
    emfta_FTAModel,
    description=
        safe_text,
    name=
        safe_text,
    comments=
        safe_text
)

@given(instance=emfta_Gate_strategy)
@settings(max_examples=50)
def test_emfta_gate_instantiation(instance):
    assert isinstance(instance, emfta_Gate)



@given(instance=emfta_Gate_strategy)
def test_emfta_gate_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=emfta_Gate_strategy)
def test_emfta_gate_nbOccurrences_setter(instance):
    original = instance.nbOccurrences
    instance.nbOccurrences = original
    assert instance.nbOccurrences == original



@given(instance=emfta_Gate_strategy)
def test_emfta_gate_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=emfta_Event_strategy)
@settings(max_examples=50)
def test_emfta_event_instantiation(instance):
    assert isinstance(instance, emfta_Event)



@given(instance=emfta_Event_strategy)
def test_emfta_event_referenceCount_setter(instance):
    original = instance.referenceCount
    instance.referenceCount = original
    assert instance.referenceCount == original



@given(instance=emfta_Event_strategy)
def test_emfta_event_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=emfta_Event_strategy)
def test_emfta_event_relatedObject_setter(instance):
    original = instance.relatedObject
    instance.relatedObject = original
    assert instance.relatedObject == original



@given(instance=emfta_Event_strategy)
def test_emfta_event_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original



@given(instance=emfta_Event_strategy)
def test_emfta_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=emfta_Event_strategy)
def test_emfta_event_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=emfta_FTAModel_strategy)
@settings(max_examples=50)
def test_emfta_ftamodel_instantiation(instance):
    assert isinstance(instance, emfta_FTAModel)



@given(instance=emfta_FTAModel_strategy)
def test_emfta_ftamodel_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=emfta_FTAModel_strategy)
def test_emfta_ftamodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=emfta_FTAModel_strategy)
def test_emfta_ftamodel_comments_setter(instance):
    original = instance.comments
    instance.comments = original
    assert instance.comments == original
