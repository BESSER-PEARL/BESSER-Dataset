import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    emfta::Gate,
    emfta::Event,
    emfta::FTAModel,
    EventType,
    GateType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_emfta::gate_is_not_abstract():
    assert not inspect.isabstract(emfta::Gate)


def test_emfta::gate_constructor_exists():
    assert callable(emfta::Gate.__init__)


def test_emfta::gate_constructor_args():
    sig = inspect.signature(emfta::Gate.__init__)
    params = list(sig.parameters.keys())
    assert "nbOccurrences" in params, "Missing parameter 'nbOccurrences'"
    assert "description" in params, "Missing parameter 'description'"
    assert "type" in params, "Missing parameter 'type'"

def test_emfta::gate_has_nbOccurrences():
    assert hasattr(emfta::Gate, "nbOccurrences")
    descriptor = None
    for klass in emfta::Gate.__mro__:
        if "nbOccurrences" in klass.__dict__:
            descriptor = klass.__dict__["nbOccurrences"]
            break
    assert isinstance(descriptor, property)

def test_emfta::gate_has_description():
    assert hasattr(emfta::Gate, "description")
    descriptor = None
    for klass in emfta::Gate.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_emfta::gate_has_type():
    assert hasattr(emfta::Gate, "type")
    descriptor = None
    for klass in emfta::Gate.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_emfta::event_is_not_abstract():
    assert not inspect.isabstract(emfta::Event)


def test_emfta::event_constructor_exists():
    assert callable(emfta::Event.__init__)


def test_emfta::event_constructor_args():
    sig = inspect.signature(emfta::Event.__init__)
    params = list(sig.parameters.keys())
    assert "referenceCount" in params, "Missing parameter 'referenceCount'"
    assert "type" in params, "Missing parameter 'type'"
    assert "description" in params, "Missing parameter 'description'"
    assert "probability" in params, "Missing parameter 'probability'"
    assert "relatedObject" in params, "Missing parameter 'relatedObject'"
    assert "name" in params, "Missing parameter 'name'"

def test_emfta::event_has_referenceCount():
    assert hasattr(emfta::Event, "referenceCount")
    descriptor = None
    for klass in emfta::Event.__mro__:
        if "referenceCount" in klass.__dict__:
            descriptor = klass.__dict__["referenceCount"]
            break
    assert isinstance(descriptor, property)

def test_emfta::event_has_type():
    assert hasattr(emfta::Event, "type")
    descriptor = None
    for klass in emfta::Event.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_emfta::event_has_description():
    assert hasattr(emfta::Event, "description")
    descriptor = None
    for klass in emfta::Event.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_emfta::event_has_probability():
    assert hasattr(emfta::Event, "probability")
    descriptor = None
    for klass in emfta::Event.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)

def test_emfta::event_has_relatedObject():
    assert hasattr(emfta::Event, "relatedObject")
    descriptor = None
    for klass in emfta::Event.__mro__:
        if "relatedObject" in klass.__dict__:
            descriptor = klass.__dict__["relatedObject"]
            break
    assert isinstance(descriptor, property)

def test_emfta::event_has_name():
    assert hasattr(emfta::Event, "name")
    descriptor = None
    for klass in emfta::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emfta::ftamodel_is_not_abstract():
    assert not inspect.isabstract(emfta::FTAModel)


def test_emfta::ftamodel_constructor_exists():
    assert callable(emfta::FTAModel.__init__)


def test_emfta::ftamodel_constructor_args():
    sig = inspect.signature(emfta::FTAModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "comments" in params, "Missing parameter 'comments'"
    assert "description" in params, "Missing parameter 'description'"

def test_emfta::ftamodel_has_name():
    assert hasattr(emfta::FTAModel, "name")
    descriptor = None
    for klass in emfta::FTAModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_emfta::ftamodel_has_comments():
    assert hasattr(emfta::FTAModel, "comments")
    descriptor = None
    for klass in emfta::FTAModel.__mro__:
        if "comments" in klass.__dict__:
            descriptor = klass.__dict__["comments"]
            break
    assert isinstance(descriptor, property)

def test_emfta::ftamodel_has_description():
    assert hasattr(emfta::FTAModel, "description")
    descriptor = None
    for klass in emfta::FTAModel.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_eventtype_exists():
    # Check that the Enumeration exists
    assert EventType is not None

def test_eventtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EventType]
    expected_literals = [
        "Undevelopped",
        "Intermediate",
        "Conditioning",
        "External",
        "Basic",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EventType"

def test_gatetype_exists():
    # Check that the Enumeration exists
    assert GateType is not None

def test_gatetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GateType]
    expected_literals = [
        "PRIORITY_AND",
        "PRIORITY_OR",
        "INTERMEDIATE",
        "XOR",
        "AND",
        "ORMORE",
        "INHIBIT",
        "OR",
        "ORLESS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GateType"


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
emfta::Gate_strategy = st.builds(
    emfta::Gate,
    nbOccurrences=
        st.integers(),
    description=
        safe_text,
    type=
        safe_text
)
emfta::Event_strategy = st.builds(
    emfta::Event,
    referenceCount=
        st.integers(),
    type=
        safe_text,
    description=
        safe_text,
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    relatedObject=
        safe_text,
    name=
        safe_text
)
emfta::FTAModel_strategy = st.builds(
    emfta::FTAModel,
    name=
        safe_text,
    comments=
        safe_text,
    description=
        safe_text
)

@given(instance=emfta::Gate_strategy)
@settings(max_examples=50)
def test_emfta::gate_instantiation(instance):
    assert isinstance(instance, emfta::Gate)

@given(instance=emfta::Gate_strategy)
def test_emfta::gate_nbOccurrences_type(instance):
    assert isinstance(instance.nbOccurrences, int)


@given(instance=emfta::Gate_strategy)
def test_emfta::gate_nbOccurrences_setter(instance):
    original = instance.nbOccurrences
    instance.nbOccurrences = original
    assert instance.nbOccurrences == original

@given(instance=emfta::Gate_strategy)
def test_emfta::gate_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=emfta::Gate_strategy)
def test_emfta::gate_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=emfta::Gate_strategy)
def test_emfta::gate_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=emfta::Gate_strategy)
def test_emfta::gate_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=emfta::Event_strategy)
@settings(max_examples=50)
def test_emfta::event_instantiation(instance):
    assert isinstance(instance, emfta::Event)

@given(instance=emfta::Event_strategy)
def test_emfta::event_referenceCount_type(instance):
    assert isinstance(instance.referenceCount, int)


@given(instance=emfta::Event_strategy)
def test_emfta::event_referenceCount_setter(instance):
    original = instance.referenceCount
    instance.referenceCount = original
    assert instance.referenceCount == original

@given(instance=emfta::Event_strategy)
def test_emfta::event_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=emfta::Event_strategy)
def test_emfta::event_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=emfta::Event_strategy)
def test_emfta::event_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=emfta::Event_strategy)
def test_emfta::event_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=emfta::Event_strategy)
def test_emfta::event_probability_type(instance):
    assert isinstance(instance.probability, float)


@given(instance=emfta::Event_strategy)
def test_emfta::event_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original

@given(instance=emfta::Event_strategy)
def test_emfta::event_relatedObject_type(instance):
    assert isinstance(instance.relatedObject, str)


@given(instance=emfta::Event_strategy)
def test_emfta::event_relatedObject_setter(instance):
    original = instance.relatedObject
    instance.relatedObject = original
    assert instance.relatedObject == original

@given(instance=emfta::Event_strategy)
def test_emfta::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=emfta::Event_strategy)
def test_emfta::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=emfta::FTAModel_strategy)
@settings(max_examples=50)
def test_emfta::ftamodel_instantiation(instance):
    assert isinstance(instance, emfta::FTAModel)

@given(instance=emfta::FTAModel_strategy)
def test_emfta::ftamodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=emfta::FTAModel_strategy)
def test_emfta::ftamodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=emfta::FTAModel_strategy)
def test_emfta::ftamodel_comments_type(instance):
    assert isinstance(instance.comments, str)


@given(instance=emfta::FTAModel_strategy)
def test_emfta::ftamodel_comments_setter(instance):
    original = instance.comments
    instance.comments = original
    assert instance.comments == original

@given(instance=emfta::FTAModel_strategy)
def test_emfta::ftamodel_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=emfta::FTAModel_strategy)
def test_emfta::ftamodel_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original
