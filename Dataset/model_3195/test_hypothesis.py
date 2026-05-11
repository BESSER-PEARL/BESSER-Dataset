import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Uppaal::TemplateType,
    Uppaal::TransitionType,
    Uppaal::TargetType,
    Uppaal::SystemType,
    Uppaal::SourceType,
    Uppaal::ParameterType,
    Uppaal::NtaType,
    Uppaal::NameType,
    Uppaal::NailType,
    Uppaal::LocationType,
    Uppaal::LabelType,
    Uppaal::InstantiationType,
    Uppaal::InitType,
    Uppaal::ImportsType,
    Uppaal::EStringToStringMapEntry,
    Uppaal::DocumentRoot,
    Uppaal::DeclarationType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uppaal::templatetype_is_not_abstract():
    assert not inspect.isabstract(Uppaal::TemplateType)


def test_uppaal::templatetype_constructor_exists():
    assert callable(Uppaal::TemplateType.__init__)


def test_uppaal::templatetype_constructor_args():
    sig = inspect.signature(Uppaal::TemplateType.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::transitiontype_is_not_abstract():
    assert not inspect.isabstract(Uppaal::TransitionType)


def test_uppaal::transitiontype_constructor_exists():
    assert callable(Uppaal::TransitionType.__init__)


def test_uppaal::transitiontype_constructor_args():
    sig = inspect.signature(Uppaal::TransitionType.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "x" in params, "Missing parameter 'x'"
    assert "id" in params, "Missing parameter 'id'"
    assert "y" in params, "Missing parameter 'y'"

def test_uppaal::transitiontype_has_color():
    assert hasattr(Uppaal::TransitionType, "color")
    descriptor = None
    for klass in Uppaal::TransitionType.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::transitiontype_has_x():
    assert hasattr(Uppaal::TransitionType, "x")
    descriptor = None
    for klass in Uppaal::TransitionType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::transitiontype_has_id():
    assert hasattr(Uppaal::TransitionType, "id")
    descriptor = None
    for klass in Uppaal::TransitionType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::transitiontype_has_y():
    assert hasattr(Uppaal::TransitionType, "y")
    descriptor = None
    for klass in Uppaal::TransitionType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::targettype_is_not_abstract():
    assert not inspect.isabstract(Uppaal::TargetType)


def test_uppaal::targettype_constructor_exists():
    assert callable(Uppaal::TargetType.__init__)


def test_uppaal::targettype_constructor_args():
    sig = inspect.signature(Uppaal::TargetType.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"

def test_uppaal::targettype_has_ref():
    assert hasattr(Uppaal::TargetType, "ref")
    descriptor = None
    for klass in Uppaal::TargetType.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::systemtype_is_not_abstract():
    assert not inspect.isabstract(Uppaal::SystemType)


def test_uppaal::systemtype_constructor_exists():
    assert callable(Uppaal::SystemType.__init__)


def test_uppaal::systemtype_constructor_args():
    sig = inspect.signature(Uppaal::SystemType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_uppaal::systemtype_has_mixed():
    assert hasattr(Uppaal::SystemType, "mixed")
    descriptor = None
    for klass in Uppaal::SystemType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::sourcetype_is_not_abstract():
    assert not inspect.isabstract(Uppaal::SourceType)


def test_uppaal::sourcetype_constructor_exists():
    assert callable(Uppaal::SourceType.__init__)


def test_uppaal::sourcetype_constructor_args():
    sig = inspect.signature(Uppaal::SourceType.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"

def test_uppaal::sourcetype_has_ref():
    assert hasattr(Uppaal::SourceType, "ref")
    descriptor = None
    for klass in Uppaal::SourceType.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::parametertype_is_not_abstract():
    assert not inspect.isabstract(Uppaal::ParameterType)


def test_uppaal::parametertype_constructor_exists():
    assert callable(Uppaal::ParameterType.__init__)


def test_uppaal::parametertype_constructor_args():
    sig = inspect.signature(Uppaal::ParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_uppaal::parametertype_has_x():
    assert hasattr(Uppaal::ParameterType, "x")
    descriptor = None
    for klass in Uppaal::ParameterType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::parametertype_has_y():
    assert hasattr(Uppaal::ParameterType, "y")
    descriptor = None
    for klass in Uppaal::ParameterType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::parametertype_has_mixed():
    assert hasattr(Uppaal::ParameterType, "mixed")
    descriptor = None
    for klass in Uppaal::ParameterType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::ntatype_is_not_abstract():
    assert not inspect.isabstract(Uppaal::NtaType)


def test_uppaal::ntatype_constructor_exists():
    assert callable(Uppaal::NtaType.__init__)


def test_uppaal::ntatype_constructor_args():
    sig = inspect.signature(Uppaal::NtaType.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::nametype_is_not_abstract():
    assert not inspect.isabstract(Uppaal::NameType)


def test_uppaal::nametype_constructor_exists():
    assert callable(Uppaal::NameType.__init__)


def test_uppaal::nametype_constructor_args():
    sig = inspect.signature(Uppaal::NameType.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "x" in params, "Missing parameter 'x'"

def test_uppaal::nametype_has_y():
    assert hasattr(Uppaal::NameType, "y")
    descriptor = None
    for klass in Uppaal::NameType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::nametype_has_mixed():
    assert hasattr(Uppaal::NameType, "mixed")
    descriptor = None
    for klass in Uppaal::NameType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::nametype_has_x():
    assert hasattr(Uppaal::NameType, "x")
    descriptor = None
    for klass in Uppaal::NameType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::nailtype_is_not_abstract():
    assert not inspect.isabstract(Uppaal::NailType)


def test_uppaal::nailtype_constructor_exists():
    assert callable(Uppaal::NailType.__init__)


def test_uppaal::nailtype_constructor_args():
    sig = inspect.signature(Uppaal::NailType.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_uppaal::nailtype_has_x():
    assert hasattr(Uppaal::NailType, "x")
    descriptor = None
    for klass in Uppaal::NailType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::nailtype_has_y():
    assert hasattr(Uppaal::NailType, "y")
    descriptor = None
    for klass in Uppaal::NailType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::locationtype_is_not_abstract():
    assert not inspect.isabstract(Uppaal::LocationType)


def test_uppaal::locationtype_constructor_exists():
    assert callable(Uppaal::LocationType.__init__)


def test_uppaal::locationtype_constructor_args():
    sig = inspect.signature(Uppaal::LocationType.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "color" in params, "Missing parameter 'color'"
    assert "x" in params, "Missing parameter 'x'"
    assert "committed" in params, "Missing parameter 'committed'"
    assert "id" in params, "Missing parameter 'id'"
    assert "urgent" in params, "Missing parameter 'urgent'"

def test_uppaal::locationtype_has_y():
    assert hasattr(Uppaal::LocationType, "y")
    descriptor = None
    for klass in Uppaal::LocationType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::locationtype_has_color():
    assert hasattr(Uppaal::LocationType, "color")
    descriptor = None
    for klass in Uppaal::LocationType.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::locationtype_has_x():
    assert hasattr(Uppaal::LocationType, "x")
    descriptor = None
    for klass in Uppaal::LocationType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::locationtype_has_committed():
    assert hasattr(Uppaal::LocationType, "committed")
    descriptor = None
    for klass in Uppaal::LocationType.__mro__:
        if "committed" in klass.__dict__:
            descriptor = klass.__dict__["committed"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::locationtype_has_id():
    assert hasattr(Uppaal::LocationType, "id")
    descriptor = None
    for klass in Uppaal::LocationType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::locationtype_has_urgent():
    assert hasattr(Uppaal::LocationType, "urgent")
    descriptor = None
    for klass in Uppaal::LocationType.__mro__:
        if "urgent" in klass.__dict__:
            descriptor = klass.__dict__["urgent"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::labeltype_is_not_abstract():
    assert not inspect.isabstract(Uppaal::LabelType)


def test_uppaal::labeltype_constructor_exists():
    assert callable(Uppaal::LabelType.__init__)


def test_uppaal::labeltype_constructor_args():
    sig = inspect.signature(Uppaal::LabelType.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "kind" in params, "Missing parameter 'kind'"
    assert "x" in params, "Missing parameter 'x'"

def test_uppaal::labeltype_has_y():
    assert hasattr(Uppaal::LabelType, "y")
    descriptor = None
    for klass in Uppaal::LabelType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::labeltype_has_mixed():
    assert hasattr(Uppaal::LabelType, "mixed")
    descriptor = None
    for klass in Uppaal::LabelType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::labeltype_has_kind():
    assert hasattr(Uppaal::LabelType, "kind")
    descriptor = None
    for klass in Uppaal::LabelType.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::labeltype_has_x():
    assert hasattr(Uppaal::LabelType, "x")
    descriptor = None
    for klass in Uppaal::LabelType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::instantiationtype_is_not_abstract():
    assert not inspect.isabstract(Uppaal::InstantiationType)


def test_uppaal::instantiationtype_constructor_exists():
    assert callable(Uppaal::InstantiationType.__init__)


def test_uppaal::instantiationtype_constructor_args():
    sig = inspect.signature(Uppaal::InstantiationType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_uppaal::instantiationtype_has_mixed():
    assert hasattr(Uppaal::InstantiationType, "mixed")
    descriptor = None
    for klass in Uppaal::InstantiationType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::inittype_is_not_abstract():
    assert not inspect.isabstract(Uppaal::InitType)


def test_uppaal::inittype_constructor_exists():
    assert callable(Uppaal::InitType.__init__)


def test_uppaal::inittype_constructor_args():
    sig = inspect.signature(Uppaal::InitType.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"

def test_uppaal::inittype_has_ref():
    assert hasattr(Uppaal::InitType, "ref")
    descriptor = None
    for klass in Uppaal::InitType.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::importstype_is_not_abstract():
    assert not inspect.isabstract(Uppaal::ImportsType)


def test_uppaal::importstype_constructor_exists():
    assert callable(Uppaal::ImportsType.__init__)


def test_uppaal::importstype_constructor_args():
    sig = inspect.signature(Uppaal::ImportsType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_uppaal::importstype_has_mixed():
    assert hasattr(Uppaal::ImportsType, "mixed")
    descriptor = None
    for klass in Uppaal::ImportsType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(Uppaal::EStringToStringMapEntry)


def test_uppaal::estringtostringmapentry_constructor_exists():
    assert callable(Uppaal::EStringToStringMapEntry.__init__)


def test_uppaal::estringtostringmapentry_constructor_args():
    sig = inspect.signature(Uppaal::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::documentroot_is_not_abstract():
    assert not inspect.isabstract(Uppaal::DocumentRoot)


def test_uppaal::documentroot_constructor_exists():
    assert callable(Uppaal::DocumentRoot.__init__)


def test_uppaal::documentroot_constructor_args():
    sig = inspect.signature(Uppaal::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "urgent" in params, "Missing parameter 'urgent'"
    assert "committed" in params, "Missing parameter 'committed'"

def test_uppaal::documentroot_has_mixed():
    assert hasattr(Uppaal::DocumentRoot, "mixed")
    descriptor = None
    for klass in Uppaal::DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::documentroot_has_urgent():
    assert hasattr(Uppaal::DocumentRoot, "urgent")
    descriptor = None
    for klass in Uppaal::DocumentRoot.__mro__:
        if "urgent" in klass.__dict__:
            descriptor = klass.__dict__["urgent"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::documentroot_has_committed():
    assert hasattr(Uppaal::DocumentRoot, "committed")
    descriptor = None
    for klass in Uppaal::DocumentRoot.__mro__:
        if "committed" in klass.__dict__:
            descriptor = klass.__dict__["committed"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::declarationtype_is_not_abstract():
    assert not inspect.isabstract(Uppaal::DeclarationType)


def test_uppaal::declarationtype_constructor_exists():
    assert callable(Uppaal::DeclarationType.__init__)


def test_uppaal::declarationtype_constructor_args():
    sig = inspect.signature(Uppaal::DeclarationType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_uppaal::declarationtype_has_mixed():
    assert hasattr(Uppaal::DeclarationType, "mixed")
    descriptor = None
    for klass in Uppaal::DeclarationType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
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
Uppaal::TemplateType_strategy = st.builds(
    Uppaal::TemplateType,
)
Uppaal::TransitionType_strategy = st.builds(
    Uppaal::TransitionType,
    color=
        safe_text,
    x=
        safe_text,
    id=
        safe_text,
    y=
        safe_text
)
Uppaal::TargetType_strategy = st.builds(
    Uppaal::TargetType,
    ref=
        safe_text
)
Uppaal::SystemType_strategy = st.builds(
    Uppaal::SystemType,
    mixed=
        safe_text
)
Uppaal::SourceType_strategy = st.builds(
    Uppaal::SourceType,
    ref=
        safe_text
)
Uppaal::ParameterType_strategy = st.builds(
    Uppaal::ParameterType,
    x=
        safe_text,
    y=
        safe_text,
    mixed=
        safe_text
)
Uppaal::NtaType_strategy = st.builds(
    Uppaal::NtaType,
)
Uppaal::NameType_strategy = st.builds(
    Uppaal::NameType,
    y=
        safe_text,
    mixed=
        safe_text,
    x=
        safe_text
)
Uppaal::NailType_strategy = st.builds(
    Uppaal::NailType,
    x=
        safe_text,
    y=
        safe_text
)
Uppaal::LocationType_strategy = st.builds(
    Uppaal::LocationType,
    y=
        safe_text,
    color=
        safe_text,
    x=
        safe_text,
    committed=
        safe_text,
    id=
        safe_text,
    urgent=
        safe_text
)
Uppaal::LabelType_strategy = st.builds(
    Uppaal::LabelType,
    y=
        safe_text,
    mixed=
        safe_text,
    kind=
        safe_text,
    x=
        safe_text
)
Uppaal::InstantiationType_strategy = st.builds(
    Uppaal::InstantiationType,
    mixed=
        safe_text
)
Uppaal::InitType_strategy = st.builds(
    Uppaal::InitType,
    ref=
        safe_text
)
Uppaal::ImportsType_strategy = st.builds(
    Uppaal::ImportsType,
    mixed=
        safe_text
)
Uppaal::EStringToStringMapEntry_strategy = st.builds(
    Uppaal::EStringToStringMapEntry,
)
Uppaal::DocumentRoot_strategy = st.builds(
    Uppaal::DocumentRoot,
    mixed=
        safe_text,
    urgent=
        safe_text,
    committed=
        safe_text
)
Uppaal::DeclarationType_strategy = st.builds(
    Uppaal::DeclarationType,
    mixed=
        safe_text
)

@given(instance=Uppaal::TemplateType_strategy)
@settings(max_examples=50)
def test_uppaal::templatetype_instantiation(instance):
    assert isinstance(instance, Uppaal::TemplateType)

@given(instance=Uppaal::TransitionType_strategy)
@settings(max_examples=50)
def test_uppaal::transitiontype_instantiation(instance):
    assert isinstance(instance, Uppaal::TransitionType)

@given(instance=Uppaal::TransitionType_strategy)
def test_uppaal::transitiontype_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=Uppaal::TransitionType_strategy)
def test_uppaal::transitiontype_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=Uppaal::TransitionType_strategy)
def test_uppaal::transitiontype_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=Uppaal::TransitionType_strategy)
def test_uppaal::transitiontype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=Uppaal::TransitionType_strategy)
def test_uppaal::transitiontype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=Uppaal::TransitionType_strategy)
def test_uppaal::transitiontype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Uppaal::TransitionType_strategy)
def test_uppaal::transitiontype_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=Uppaal::TransitionType_strategy)
def test_uppaal::transitiontype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=Uppaal::TargetType_strategy)
@settings(max_examples=50)
def test_uppaal::targettype_instantiation(instance):
    assert isinstance(instance, Uppaal::TargetType)

@given(instance=Uppaal::TargetType_strategy)
def test_uppaal::targettype_ref_type(instance):
    assert isinstance(instance.ref, str)


@given(instance=Uppaal::TargetType_strategy)
def test_uppaal::targettype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=Uppaal::SystemType_strategy)
@settings(max_examples=50)
def test_uppaal::systemtype_instantiation(instance):
    assert isinstance(instance, Uppaal::SystemType)

@given(instance=Uppaal::SystemType_strategy)
def test_uppaal::systemtype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Uppaal::SystemType_strategy)
def test_uppaal::systemtype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Uppaal::SourceType_strategy)
@settings(max_examples=50)
def test_uppaal::sourcetype_instantiation(instance):
    assert isinstance(instance, Uppaal::SourceType)

@given(instance=Uppaal::SourceType_strategy)
def test_uppaal::sourcetype_ref_type(instance):
    assert isinstance(instance.ref, str)


@given(instance=Uppaal::SourceType_strategy)
def test_uppaal::sourcetype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=Uppaal::ParameterType_strategy)
@settings(max_examples=50)
def test_uppaal::parametertype_instantiation(instance):
    assert isinstance(instance, Uppaal::ParameterType)

@given(instance=Uppaal::ParameterType_strategy)
def test_uppaal::parametertype_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=Uppaal::ParameterType_strategy)
def test_uppaal::parametertype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=Uppaal::ParameterType_strategy)
def test_uppaal::parametertype_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=Uppaal::ParameterType_strategy)
def test_uppaal::parametertype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=Uppaal::ParameterType_strategy)
def test_uppaal::parametertype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Uppaal::ParameterType_strategy)
def test_uppaal::parametertype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Uppaal::NtaType_strategy)
@settings(max_examples=50)
def test_uppaal::ntatype_instantiation(instance):
    assert isinstance(instance, Uppaal::NtaType)

@given(instance=Uppaal::NameType_strategy)
@settings(max_examples=50)
def test_uppaal::nametype_instantiation(instance):
    assert isinstance(instance, Uppaal::NameType)

@given(instance=Uppaal::NameType_strategy)
def test_uppaal::nametype_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=Uppaal::NameType_strategy)
def test_uppaal::nametype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=Uppaal::NameType_strategy)
def test_uppaal::nametype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Uppaal::NameType_strategy)
def test_uppaal::nametype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Uppaal::NameType_strategy)
def test_uppaal::nametype_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=Uppaal::NameType_strategy)
def test_uppaal::nametype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=Uppaal::NailType_strategy)
@settings(max_examples=50)
def test_uppaal::nailtype_instantiation(instance):
    assert isinstance(instance, Uppaal::NailType)

@given(instance=Uppaal::NailType_strategy)
def test_uppaal::nailtype_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=Uppaal::NailType_strategy)
def test_uppaal::nailtype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=Uppaal::NailType_strategy)
def test_uppaal::nailtype_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=Uppaal::NailType_strategy)
def test_uppaal::nailtype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=Uppaal::LocationType_strategy)
@settings(max_examples=50)
def test_uppaal::locationtype_instantiation(instance):
    assert isinstance(instance, Uppaal::LocationType)

@given(instance=Uppaal::LocationType_strategy)
def test_uppaal::locationtype_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=Uppaal::LocationType_strategy)
def test_uppaal::locationtype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=Uppaal::LocationType_strategy)
def test_uppaal::locationtype_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=Uppaal::LocationType_strategy)
def test_uppaal::locationtype_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=Uppaal::LocationType_strategy)
def test_uppaal::locationtype_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=Uppaal::LocationType_strategy)
def test_uppaal::locationtype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=Uppaal::LocationType_strategy)
def test_uppaal::locationtype_committed_type(instance):
    assert isinstance(instance.committed, str)


@given(instance=Uppaal::LocationType_strategy)
def test_uppaal::locationtype_committed_setter(instance):
    original = instance.committed
    instance.committed = original
    assert instance.committed == original

@given(instance=Uppaal::LocationType_strategy)
def test_uppaal::locationtype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=Uppaal::LocationType_strategy)
def test_uppaal::locationtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Uppaal::LocationType_strategy)
def test_uppaal::locationtype_urgent_type(instance):
    assert isinstance(instance.urgent, str)


@given(instance=Uppaal::LocationType_strategy)
def test_uppaal::locationtype_urgent_setter(instance):
    original = instance.urgent
    instance.urgent = original
    assert instance.urgent == original

@given(instance=Uppaal::LabelType_strategy)
@settings(max_examples=50)
def test_uppaal::labeltype_instantiation(instance):
    assert isinstance(instance, Uppaal::LabelType)

@given(instance=Uppaal::LabelType_strategy)
def test_uppaal::labeltype_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=Uppaal::LabelType_strategy)
def test_uppaal::labeltype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=Uppaal::LabelType_strategy)
def test_uppaal::labeltype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Uppaal::LabelType_strategy)
def test_uppaal::labeltype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Uppaal::LabelType_strategy)
def test_uppaal::labeltype_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=Uppaal::LabelType_strategy)
def test_uppaal::labeltype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=Uppaal::LabelType_strategy)
def test_uppaal::labeltype_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=Uppaal::LabelType_strategy)
def test_uppaal::labeltype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=Uppaal::InstantiationType_strategy)
@settings(max_examples=50)
def test_uppaal::instantiationtype_instantiation(instance):
    assert isinstance(instance, Uppaal::InstantiationType)

@given(instance=Uppaal::InstantiationType_strategy)
def test_uppaal::instantiationtype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Uppaal::InstantiationType_strategy)
def test_uppaal::instantiationtype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Uppaal::InitType_strategy)
@settings(max_examples=50)
def test_uppaal::inittype_instantiation(instance):
    assert isinstance(instance, Uppaal::InitType)

@given(instance=Uppaal::InitType_strategy)
def test_uppaal::inittype_ref_type(instance):
    assert isinstance(instance.ref, str)


@given(instance=Uppaal::InitType_strategy)
def test_uppaal::inittype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=Uppaal::ImportsType_strategy)
@settings(max_examples=50)
def test_uppaal::importstype_instantiation(instance):
    assert isinstance(instance, Uppaal::ImportsType)

@given(instance=Uppaal::ImportsType_strategy)
def test_uppaal::importstype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Uppaal::ImportsType_strategy)
def test_uppaal::importstype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Uppaal::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_uppaal::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, Uppaal::EStringToStringMapEntry)

@given(instance=Uppaal::DocumentRoot_strategy)
@settings(max_examples=50)
def test_uppaal::documentroot_instantiation(instance):
    assert isinstance(instance, Uppaal::DocumentRoot)

@given(instance=Uppaal::DocumentRoot_strategy)
def test_uppaal::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Uppaal::DocumentRoot_strategy)
def test_uppaal::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Uppaal::DocumentRoot_strategy)
def test_uppaal::documentroot_urgent_type(instance):
    assert isinstance(instance.urgent, str)


@given(instance=Uppaal::DocumentRoot_strategy)
def test_uppaal::documentroot_urgent_setter(instance):
    original = instance.urgent
    instance.urgent = original
    assert instance.urgent == original

@given(instance=Uppaal::DocumentRoot_strategy)
def test_uppaal::documentroot_committed_type(instance):
    assert isinstance(instance.committed, str)


@given(instance=Uppaal::DocumentRoot_strategy)
def test_uppaal::documentroot_committed_setter(instance):
    original = instance.committed
    instance.committed = original
    assert instance.committed == original

@given(instance=Uppaal::DeclarationType_strategy)
@settings(max_examples=50)
def test_uppaal::declarationtype_instantiation(instance):
    assert isinstance(instance, Uppaal::DeclarationType)

@given(instance=Uppaal::DeclarationType_strategy)
def test_uppaal::declarationtype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Uppaal::DeclarationType_strategy)
def test_uppaal::declarationtype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original
