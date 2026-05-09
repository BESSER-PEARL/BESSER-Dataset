import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    flat11::UrgentType,
    flat11::TransitionType,
    flat11::LabelType,
    flat11::TemplateType,
    flat11::TargetType,
    flat11::SourceType,
    flat11::ParameterType,
    flat11::NtaType,
    flat11::NameType,
    flat11::NailType,
    flat11::LocationType,
    flat11::InitType,
    flat11::EStringToStringMapEntry,
    flat11::DocumentRoot,
    flat11::CommittedType,
    KindType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_flat11::urgenttype_is_not_abstract():
    assert not inspect.isabstract(flat11::UrgentType)


def test_flat11::urgenttype_constructor_exists():
    assert callable(flat11::UrgentType.__init__)


def test_flat11::urgenttype_constructor_args():
    sig = inspect.signature(flat11::UrgentType.__init__)
    params = list(sig.parameters.keys())



def test_flat11::transitiontype_is_not_abstract():
    assert not inspect.isabstract(flat11::TransitionType)


def test_flat11::transitiontype_constructor_exists():
    assert callable(flat11::TransitionType.__init__)


def test_flat11::transitiontype_constructor_args():
    sig = inspect.signature(flat11::TransitionType.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"
    assert "controllable" in params, "Missing parameter 'controllable'"
    assert "id" in params, "Missing parameter 'id'"
    assert "action" in params, "Missing parameter 'action'"

def test_flat11::transitiontype_has_color():
    assert hasattr(flat11::TransitionType, "color")
    descriptor = None
    for klass in flat11::TransitionType.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_flat11::transitiontype_has_x():
    assert hasattr(flat11::TransitionType, "x")
    descriptor = None
    for klass in flat11::TransitionType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_flat11::transitiontype_has_y():
    assert hasattr(flat11::TransitionType, "y")
    descriptor = None
    for klass in flat11::TransitionType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_flat11::transitiontype_has_controllable():
    assert hasattr(flat11::TransitionType, "controllable")
    descriptor = None
    for klass in flat11::TransitionType.__mro__:
        if "controllable" in klass.__dict__:
            descriptor = klass.__dict__["controllable"]
            break
    assert isinstance(descriptor, property)

def test_flat11::transitiontype_has_id():
    assert hasattr(flat11::TransitionType, "id")
    descriptor = None
    for klass in flat11::TransitionType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_flat11::transitiontype_has_action():
    assert hasattr(flat11::TransitionType, "action")
    descriptor = None
    for klass in flat11::TransitionType.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)



def test_flat11::labeltype_is_not_abstract():
    assert not inspect.isabstract(flat11::LabelType)


def test_flat11::labeltype_constructor_exists():
    assert callable(flat11::LabelType.__init__)


def test_flat11::labeltype_constructor_args():
    sig = inspect.signature(flat11::LabelType.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "kind" in params, "Missing parameter 'kind'"
    assert "value" in params, "Missing parameter 'value'"
    assert "y" in params, "Missing parameter 'y'"

def test_flat11::labeltype_has_x():
    assert hasattr(flat11::LabelType, "x")
    descriptor = None
    for klass in flat11::LabelType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_flat11::labeltype_has_kind():
    assert hasattr(flat11::LabelType, "kind")
    descriptor = None
    for klass in flat11::LabelType.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_flat11::labeltype_has_value():
    assert hasattr(flat11::LabelType, "value")
    descriptor = None
    for klass in flat11::LabelType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_flat11::labeltype_has_y():
    assert hasattr(flat11::LabelType, "y")
    descriptor = None
    for klass in flat11::LabelType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_flat11::templatetype_is_not_abstract():
    assert not inspect.isabstract(flat11::TemplateType)


def test_flat11::templatetype_constructor_exists():
    assert callable(flat11::TemplateType.__init__)


def test_flat11::templatetype_constructor_args():
    sig = inspect.signature(flat11::TemplateType.__init__)
    params = list(sig.parameters.keys())
    assert "declaration" in params, "Missing parameter 'declaration'"

def test_flat11::templatetype_has_declaration():
    assert hasattr(flat11::TemplateType, "declaration")
    descriptor = None
    for klass in flat11::TemplateType.__mro__:
        if "declaration" in klass.__dict__:
            descriptor = klass.__dict__["declaration"]
            break
    assert isinstance(descriptor, property)



def test_flat11::targettype_is_not_abstract():
    assert not inspect.isabstract(flat11::TargetType)


def test_flat11::targettype_constructor_exists():
    assert callable(flat11::TargetType.__init__)


def test_flat11::targettype_constructor_args():
    sig = inspect.signature(flat11::TargetType.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"

def test_flat11::targettype_has_ref():
    assert hasattr(flat11::TargetType, "ref")
    descriptor = None
    for klass in flat11::TargetType.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_flat11::sourcetype_is_not_abstract():
    assert not inspect.isabstract(flat11::SourceType)


def test_flat11::sourcetype_constructor_exists():
    assert callable(flat11::SourceType.__init__)


def test_flat11::sourcetype_constructor_args():
    sig = inspect.signature(flat11::SourceType.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"

def test_flat11::sourcetype_has_ref():
    assert hasattr(flat11::SourceType, "ref")
    descriptor = None
    for klass in flat11::SourceType.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_flat11::parametertype_is_not_abstract():
    assert not inspect.isabstract(flat11::ParameterType)


def test_flat11::parametertype_constructor_exists():
    assert callable(flat11::ParameterType.__init__)


def test_flat11::parametertype_constructor_args():
    sig = inspect.signature(flat11::ParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "value" in params, "Missing parameter 'value'"
    assert "x" in params, "Missing parameter 'x'"

def test_flat11::parametertype_has_y():
    assert hasattr(flat11::ParameterType, "y")
    descriptor = None
    for klass in flat11::ParameterType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_flat11::parametertype_has_value():
    assert hasattr(flat11::ParameterType, "value")
    descriptor = None
    for klass in flat11::ParameterType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_flat11::parametertype_has_x():
    assert hasattr(flat11::ParameterType, "x")
    descriptor = None
    for klass in flat11::ParameterType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_flat11::ntatype_is_not_abstract():
    assert not inspect.isabstract(flat11::NtaType)


def test_flat11::ntatype_constructor_exists():
    assert callable(flat11::NtaType.__init__)


def test_flat11::ntatype_constructor_args():
    sig = inspect.signature(flat11::NtaType.__init__)
    params = list(sig.parameters.keys())
    assert "imports" in params, "Missing parameter 'imports'"
    assert "declaration" in params, "Missing parameter 'declaration'"
    assert "instantiation" in params, "Missing parameter 'instantiation'"
    assert "system" in params, "Missing parameter 'system'"

def test_flat11::ntatype_has_imports():
    assert hasattr(flat11::NtaType, "imports")
    descriptor = None
    for klass in flat11::NtaType.__mro__:
        if "imports" in klass.__dict__:
            descriptor = klass.__dict__["imports"]
            break
    assert isinstance(descriptor, property)

def test_flat11::ntatype_has_declaration():
    assert hasattr(flat11::NtaType, "declaration")
    descriptor = None
    for klass in flat11::NtaType.__mro__:
        if "declaration" in klass.__dict__:
            descriptor = klass.__dict__["declaration"]
            break
    assert isinstance(descriptor, property)

def test_flat11::ntatype_has_instantiation():
    assert hasattr(flat11::NtaType, "instantiation")
    descriptor = None
    for klass in flat11::NtaType.__mro__:
        if "instantiation" in klass.__dict__:
            descriptor = klass.__dict__["instantiation"]
            break
    assert isinstance(descriptor, property)

def test_flat11::ntatype_has_system():
    assert hasattr(flat11::NtaType, "system")
    descriptor = None
    for klass in flat11::NtaType.__mro__:
        if "system" in klass.__dict__:
            descriptor = klass.__dict__["system"]
            break
    assert isinstance(descriptor, property)



def test_flat11::nametype_is_not_abstract():
    assert not inspect.isabstract(flat11::NameType)


def test_flat11::nametype_constructor_exists():
    assert callable(flat11::NameType.__init__)


def test_flat11::nametype_constructor_args():
    sig = inspect.signature(flat11::NameType.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"
    assert "value" in params, "Missing parameter 'value'"

def test_flat11::nametype_has_x():
    assert hasattr(flat11::NameType, "x")
    descriptor = None
    for klass in flat11::NameType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_flat11::nametype_has_y():
    assert hasattr(flat11::NameType, "y")
    descriptor = None
    for klass in flat11::NameType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_flat11::nametype_has_value():
    assert hasattr(flat11::NameType, "value")
    descriptor = None
    for klass in flat11::NameType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_flat11::nailtype_is_not_abstract():
    assert not inspect.isabstract(flat11::NailType)


def test_flat11::nailtype_constructor_exists():
    assert callable(flat11::NailType.__init__)


def test_flat11::nailtype_constructor_args():
    sig = inspect.signature(flat11::NailType.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_flat11::nailtype_has_y():
    assert hasattr(flat11::NailType, "y")
    descriptor = None
    for klass in flat11::NailType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_flat11::nailtype_has_x():
    assert hasattr(flat11::NailType, "x")
    descriptor = None
    for klass in flat11::NailType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_flat11::locationtype_is_not_abstract():
    assert not inspect.isabstract(flat11::LocationType)


def test_flat11::locationtype_constructor_exists():
    assert callable(flat11::LocationType.__init__)


def test_flat11::locationtype_constructor_args():
    sig = inspect.signature(flat11::LocationType.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "color" in params, "Missing parameter 'color'"
    assert "x" in params, "Missing parameter 'x'"
    assert "id" in params, "Missing parameter 'id'"

def test_flat11::locationtype_has_y():
    assert hasattr(flat11::LocationType, "y")
    descriptor = None
    for klass in flat11::LocationType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_flat11::locationtype_has_color():
    assert hasattr(flat11::LocationType, "color")
    descriptor = None
    for klass in flat11::LocationType.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_flat11::locationtype_has_x():
    assert hasattr(flat11::LocationType, "x")
    descriptor = None
    for klass in flat11::LocationType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_flat11::locationtype_has_id():
    assert hasattr(flat11::LocationType, "id")
    descriptor = None
    for klass in flat11::LocationType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_flat11::inittype_is_not_abstract():
    assert not inspect.isabstract(flat11::InitType)


def test_flat11::inittype_constructor_exists():
    assert callable(flat11::InitType.__init__)


def test_flat11::inittype_constructor_args():
    sig = inspect.signature(flat11::InitType.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"

def test_flat11::inittype_has_ref():
    assert hasattr(flat11::InitType, "ref")
    descriptor = None
    for klass in flat11::InitType.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_flat11::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(flat11::EStringToStringMapEntry)


def test_flat11::estringtostringmapentry_constructor_exists():
    assert callable(flat11::EStringToStringMapEntry.__init__)


def test_flat11::estringtostringmapentry_constructor_args():
    sig = inspect.signature(flat11::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_flat11::documentroot_is_not_abstract():
    assert not inspect.isabstract(flat11::DocumentRoot)


def test_flat11::documentroot_constructor_exists():
    assert callable(flat11::DocumentRoot.__init__)


def test_flat11::documentroot_constructor_args():
    sig = inspect.signature(flat11::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "instantiation" in params, "Missing parameter 'instantiation'"
    assert "declaration" in params, "Missing parameter 'declaration'"
    assert "system" in params, "Missing parameter 'system'"
    assert "imports" in params, "Missing parameter 'imports'"

def test_flat11::documentroot_has_mixed():
    assert hasattr(flat11::DocumentRoot, "mixed")
    descriptor = None
    for klass in flat11::DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_flat11::documentroot_has_instantiation():
    assert hasattr(flat11::DocumentRoot, "instantiation")
    descriptor = None
    for klass in flat11::DocumentRoot.__mro__:
        if "instantiation" in klass.__dict__:
            descriptor = klass.__dict__["instantiation"]
            break
    assert isinstance(descriptor, property)

def test_flat11::documentroot_has_declaration():
    assert hasattr(flat11::DocumentRoot, "declaration")
    descriptor = None
    for klass in flat11::DocumentRoot.__mro__:
        if "declaration" in klass.__dict__:
            descriptor = klass.__dict__["declaration"]
            break
    assert isinstance(descriptor, property)

def test_flat11::documentroot_has_system():
    assert hasattr(flat11::DocumentRoot, "system")
    descriptor = None
    for klass in flat11::DocumentRoot.__mro__:
        if "system" in klass.__dict__:
            descriptor = klass.__dict__["system"]
            break
    assert isinstance(descriptor, property)

def test_flat11::documentroot_has_imports():
    assert hasattr(flat11::DocumentRoot, "imports")
    descriptor = None
    for klass in flat11::DocumentRoot.__mro__:
        if "imports" in klass.__dict__:
            descriptor = klass.__dict__["imports"]
            break
    assert isinstance(descriptor, property)



def test_flat11::committedtype_is_not_abstract():
    assert not inspect.isabstract(flat11::CommittedType)


def test_flat11::committedtype_constructor_exists():
    assert callable(flat11::CommittedType.__init__)


def test_flat11::committedtype_constructor_args():
    sig = inspect.signature(flat11::CommittedType.__init__)
    params = list(sig.parameters.keys())

def test_kindtype_exists():
    # Check that the Enumeration exists
    assert KindType is not None

def test_kindtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in KindType]
    expected_literals = [
        "synchronisation",
        "select",
        "comments",
        "invariant",
        "assignment",
        "guard",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in KindType"


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
flat11::UrgentType_strategy = st.builds(
    flat11::UrgentType,
)
flat11::TransitionType_strategy = st.builds(
    flat11::TransitionType,
    color=
        safe_text,
    x=
        safe_text,
    y=
        safe_text,
    controllable=
        safe_text,
    id=
        safe_text,
    action=
        safe_text
)
flat11::LabelType_strategy = st.builds(
    flat11::LabelType,
    x=
        safe_text,
    kind=
        safe_text,
    value=
        safe_text,
    y=
        safe_text
)
flat11::TemplateType_strategy = st.builds(
    flat11::TemplateType,
    declaration=
        safe_text
)
flat11::TargetType_strategy = st.builds(
    flat11::TargetType,
    ref=
        safe_text
)
flat11::SourceType_strategy = st.builds(
    flat11::SourceType,
    ref=
        safe_text
)
flat11::ParameterType_strategy = st.builds(
    flat11::ParameterType,
    y=
        safe_text,
    value=
        safe_text,
    x=
        safe_text
)
flat11::NtaType_strategy = st.builds(
    flat11::NtaType,
    imports=
        safe_text,
    declaration=
        safe_text,
    instantiation=
        safe_text,
    system=
        safe_text
)
flat11::NameType_strategy = st.builds(
    flat11::NameType,
    x=
        safe_text,
    y=
        safe_text,
    value=
        safe_text
)
flat11::NailType_strategy = st.builds(
    flat11::NailType,
    y=
        safe_text,
    x=
        safe_text
)
flat11::LocationType_strategy = st.builds(
    flat11::LocationType,
    y=
        safe_text,
    color=
        safe_text,
    x=
        safe_text,
    id=
        safe_text
)
flat11::InitType_strategy = st.builds(
    flat11::InitType,
    ref=
        safe_text
)
flat11::EStringToStringMapEntry_strategy = st.builds(
    flat11::EStringToStringMapEntry,
)
flat11::DocumentRoot_strategy = st.builds(
    flat11::DocumentRoot,
    mixed=
        safe_text,
    instantiation=
        safe_text,
    declaration=
        safe_text,
    system=
        safe_text,
    imports=
        safe_text
)
flat11::CommittedType_strategy = st.builds(
    flat11::CommittedType,
)

@given(instance=flat11::UrgentType_strategy)
@settings(max_examples=50)
def test_flat11::urgenttype_instantiation(instance):
    assert isinstance(instance, flat11::UrgentType)

@given(instance=flat11::TransitionType_strategy)
@settings(max_examples=50)
def test_flat11::transitiontype_instantiation(instance):
    assert isinstance(instance, flat11::TransitionType)

@given(instance=flat11::TransitionType_strategy)
def test_flat11::transitiontype_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=flat11::TransitionType_strategy)
def test_flat11::transitiontype_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=flat11::TransitionType_strategy)
def test_flat11::transitiontype_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=flat11::TransitionType_strategy)
def test_flat11::transitiontype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=flat11::TransitionType_strategy)
def test_flat11::transitiontype_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=flat11::TransitionType_strategy)
def test_flat11::transitiontype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=flat11::TransitionType_strategy)
def test_flat11::transitiontype_controllable_type(instance):
    assert isinstance(instance.controllable, str)


@given(instance=flat11::TransitionType_strategy)
def test_flat11::transitiontype_controllable_setter(instance):
    original = instance.controllable
    instance.controllable = original
    assert instance.controllable == original

@given(instance=flat11::TransitionType_strategy)
def test_flat11::transitiontype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=flat11::TransitionType_strategy)
def test_flat11::transitiontype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=flat11::TransitionType_strategy)
def test_flat11::transitiontype_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=flat11::TransitionType_strategy)
def test_flat11::transitiontype_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=flat11::LabelType_strategy)
@settings(max_examples=50)
def test_flat11::labeltype_instantiation(instance):
    assert isinstance(instance, flat11::LabelType)

@given(instance=flat11::LabelType_strategy)
def test_flat11::labeltype_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=flat11::LabelType_strategy)
def test_flat11::labeltype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=flat11::LabelType_strategy)
def test_flat11::labeltype_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=flat11::LabelType_strategy)
def test_flat11::labeltype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=flat11::LabelType_strategy)
def test_flat11::labeltype_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=flat11::LabelType_strategy)
def test_flat11::labeltype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=flat11::LabelType_strategy)
def test_flat11::labeltype_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=flat11::LabelType_strategy)
def test_flat11::labeltype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=flat11::TemplateType_strategy)
@settings(max_examples=50)
def test_flat11::templatetype_instantiation(instance):
    assert isinstance(instance, flat11::TemplateType)

@given(instance=flat11::TemplateType_strategy)
def test_flat11::templatetype_declaration_type(instance):
    assert isinstance(instance.declaration, str)


@given(instance=flat11::TemplateType_strategy)
def test_flat11::templatetype_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original

@given(instance=flat11::TargetType_strategy)
@settings(max_examples=50)
def test_flat11::targettype_instantiation(instance):
    assert isinstance(instance, flat11::TargetType)

@given(instance=flat11::TargetType_strategy)
def test_flat11::targettype_ref_type(instance):
    assert isinstance(instance.ref, str)


@given(instance=flat11::TargetType_strategy)
def test_flat11::targettype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=flat11::SourceType_strategy)
@settings(max_examples=50)
def test_flat11::sourcetype_instantiation(instance):
    assert isinstance(instance, flat11::SourceType)

@given(instance=flat11::SourceType_strategy)
def test_flat11::sourcetype_ref_type(instance):
    assert isinstance(instance.ref, str)


@given(instance=flat11::SourceType_strategy)
def test_flat11::sourcetype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=flat11::ParameterType_strategy)
@settings(max_examples=50)
def test_flat11::parametertype_instantiation(instance):
    assert isinstance(instance, flat11::ParameterType)

@given(instance=flat11::ParameterType_strategy)
def test_flat11::parametertype_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=flat11::ParameterType_strategy)
def test_flat11::parametertype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=flat11::ParameterType_strategy)
def test_flat11::parametertype_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=flat11::ParameterType_strategy)
def test_flat11::parametertype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=flat11::ParameterType_strategy)
def test_flat11::parametertype_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=flat11::ParameterType_strategy)
def test_flat11::parametertype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=flat11::NtaType_strategy)
@settings(max_examples=50)
def test_flat11::ntatype_instantiation(instance):
    assert isinstance(instance, flat11::NtaType)

@given(instance=flat11::NtaType_strategy)
def test_flat11::ntatype_imports_type(instance):
    assert isinstance(instance.imports, str)


@given(instance=flat11::NtaType_strategy)
def test_flat11::ntatype_imports_setter(instance):
    original = instance.imports
    instance.imports = original
    assert instance.imports == original

@given(instance=flat11::NtaType_strategy)
def test_flat11::ntatype_declaration_type(instance):
    assert isinstance(instance.declaration, str)


@given(instance=flat11::NtaType_strategy)
def test_flat11::ntatype_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original

@given(instance=flat11::NtaType_strategy)
def test_flat11::ntatype_instantiation_type(instance):
    assert isinstance(instance.instantiation, str)


@given(instance=flat11::NtaType_strategy)
def test_flat11::ntatype_instantiation_setter(instance):
    original = instance.instantiation
    instance.instantiation = original
    assert instance.instantiation == original

@given(instance=flat11::NtaType_strategy)
def test_flat11::ntatype_system_type(instance):
    assert isinstance(instance.system, str)


@given(instance=flat11::NtaType_strategy)
def test_flat11::ntatype_system_setter(instance):
    original = instance.system
    instance.system = original
    assert instance.system == original

@given(instance=flat11::NameType_strategy)
@settings(max_examples=50)
def test_flat11::nametype_instantiation(instance):
    assert isinstance(instance, flat11::NameType)

@given(instance=flat11::NameType_strategy)
def test_flat11::nametype_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=flat11::NameType_strategy)
def test_flat11::nametype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=flat11::NameType_strategy)
def test_flat11::nametype_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=flat11::NameType_strategy)
def test_flat11::nametype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=flat11::NameType_strategy)
def test_flat11::nametype_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=flat11::NameType_strategy)
def test_flat11::nametype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=flat11::NailType_strategy)
@settings(max_examples=50)
def test_flat11::nailtype_instantiation(instance):
    assert isinstance(instance, flat11::NailType)

@given(instance=flat11::NailType_strategy)
def test_flat11::nailtype_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=flat11::NailType_strategy)
def test_flat11::nailtype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=flat11::NailType_strategy)
def test_flat11::nailtype_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=flat11::NailType_strategy)
def test_flat11::nailtype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=flat11::LocationType_strategy)
@settings(max_examples=50)
def test_flat11::locationtype_instantiation(instance):
    assert isinstance(instance, flat11::LocationType)

@given(instance=flat11::LocationType_strategy)
def test_flat11::locationtype_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=flat11::LocationType_strategy)
def test_flat11::locationtype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=flat11::LocationType_strategy)
def test_flat11::locationtype_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=flat11::LocationType_strategy)
def test_flat11::locationtype_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=flat11::LocationType_strategy)
def test_flat11::locationtype_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=flat11::LocationType_strategy)
def test_flat11::locationtype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=flat11::LocationType_strategy)
def test_flat11::locationtype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=flat11::LocationType_strategy)
def test_flat11::locationtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=flat11::InitType_strategy)
@settings(max_examples=50)
def test_flat11::inittype_instantiation(instance):
    assert isinstance(instance, flat11::InitType)

@given(instance=flat11::InitType_strategy)
def test_flat11::inittype_ref_type(instance):
    assert isinstance(instance.ref, str)


@given(instance=flat11::InitType_strategy)
def test_flat11::inittype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=flat11::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_flat11::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, flat11::EStringToStringMapEntry)

@given(instance=flat11::DocumentRoot_strategy)
@settings(max_examples=50)
def test_flat11::documentroot_instantiation(instance):
    assert isinstance(instance, flat11::DocumentRoot)

@given(instance=flat11::DocumentRoot_strategy)
def test_flat11::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=flat11::DocumentRoot_strategy)
def test_flat11::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=flat11::DocumentRoot_strategy)
def test_flat11::documentroot_instantiation_type(instance):
    assert isinstance(instance.instantiation, str)


@given(instance=flat11::DocumentRoot_strategy)
def test_flat11::documentroot_instantiation_setter(instance):
    original = instance.instantiation
    instance.instantiation = original
    assert instance.instantiation == original

@given(instance=flat11::DocumentRoot_strategy)
def test_flat11::documentroot_declaration_type(instance):
    assert isinstance(instance.declaration, str)


@given(instance=flat11::DocumentRoot_strategy)
def test_flat11::documentroot_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original

@given(instance=flat11::DocumentRoot_strategy)
def test_flat11::documentroot_system_type(instance):
    assert isinstance(instance.system, str)


@given(instance=flat11::DocumentRoot_strategy)
def test_flat11::documentroot_system_setter(instance):
    original = instance.system
    instance.system = original
    assert instance.system == original

@given(instance=flat11::DocumentRoot_strategy)
def test_flat11::documentroot_imports_type(instance):
    assert isinstance(instance.imports, str)


@given(instance=flat11::DocumentRoot_strategy)
def test_flat11::documentroot_imports_setter(instance):
    original = instance.imports
    instance.imports = original
    assert instance.imports == original

@given(instance=flat11::CommittedType_strategy)
@settings(max_examples=50)
def test_flat11::committedtype_instantiation(instance):
    assert isinstance(instance, flat11::CommittedType)
