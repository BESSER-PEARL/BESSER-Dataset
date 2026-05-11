import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    uppaal::UrgentType,
    uppaal::TransitionType,
    uppaal::TemplateType,
    uppaal::LocationType,
    uppaal::TargetType,
    uppaal::SourceType,
    uppaal::ParameterType,
    uppaal::NtaType,
    uppaal::NameType,
    uppaal::NailType,
    uppaal::DocumentRoot,
    uppaal::CommittedType,
    uppaal::LabelType,
    uppaal::InitType,
    uppaal::EStringToStringMapEntry,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uppaal::urgenttype_is_not_abstract():
    assert not inspect.isabstract(uppaal::UrgentType)


def test_uppaal::urgenttype_constructor_exists():
    assert callable(uppaal::UrgentType.__init__)


def test_uppaal::urgenttype_constructor_args():
    sig = inspect.signature(uppaal::UrgentType.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::transitiontype_is_not_abstract():
    assert not inspect.isabstract(uppaal::TransitionType)


def test_uppaal::transitiontype_constructor_exists():
    assert callable(uppaal::TransitionType.__init__)


def test_uppaal::transitiontype_constructor_args():
    sig = inspect.signature(uppaal::TransitionType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"
    assert "color" in params, "Missing parameter 'color'"

def test_uppaal::transitiontype_has_id():
    assert hasattr(uppaal::TransitionType, "id")
    descriptor = None
    for klass in uppaal::TransitionType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::transitiontype_has_y():
    assert hasattr(uppaal::TransitionType, "y")
    descriptor = None
    for klass in uppaal::TransitionType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::transitiontype_has_x():
    assert hasattr(uppaal::TransitionType, "x")
    descriptor = None
    for klass in uppaal::TransitionType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::transitiontype_has_color():
    assert hasattr(uppaal::TransitionType, "color")
    descriptor = None
    for klass in uppaal::TransitionType.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::templatetype_is_not_abstract():
    assert not inspect.isabstract(uppaal::TemplateType)


def test_uppaal::templatetype_constructor_exists():
    assert callable(uppaal::TemplateType.__init__)


def test_uppaal::templatetype_constructor_args():
    sig = inspect.signature(uppaal::TemplateType.__init__)
    params = list(sig.parameters.keys())
    assert "declaration" in params, "Missing parameter 'declaration'"

def test_uppaal::templatetype_has_declaration():
    assert hasattr(uppaal::TemplateType, "declaration")
    descriptor = None
    for klass in uppaal::TemplateType.__mro__:
        if "declaration" in klass.__dict__:
            descriptor = klass.__dict__["declaration"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::locationtype_is_not_abstract():
    assert not inspect.isabstract(uppaal::LocationType)


def test_uppaal::locationtype_constructor_exists():
    assert callable(uppaal::LocationType.__init__)


def test_uppaal::locationtype_constructor_args():
    sig = inspect.signature(uppaal::LocationType.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "id" in params, "Missing parameter 'id'"
    assert "color" in params, "Missing parameter 'color'"
    assert "x" in params, "Missing parameter 'x'"

def test_uppaal::locationtype_has_y():
    assert hasattr(uppaal::LocationType, "y")
    descriptor = None
    for klass in uppaal::LocationType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::locationtype_has_id():
    assert hasattr(uppaal::LocationType, "id")
    descriptor = None
    for klass in uppaal::LocationType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::locationtype_has_color():
    assert hasattr(uppaal::LocationType, "color")
    descriptor = None
    for klass in uppaal::LocationType.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::locationtype_has_x():
    assert hasattr(uppaal::LocationType, "x")
    descriptor = None
    for klass in uppaal::LocationType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::targettype_is_not_abstract():
    assert not inspect.isabstract(uppaal::TargetType)


def test_uppaal::targettype_constructor_exists():
    assert callable(uppaal::TargetType.__init__)


def test_uppaal::targettype_constructor_args():
    sig = inspect.signature(uppaal::TargetType.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"

def test_uppaal::targettype_has_ref():
    assert hasattr(uppaal::TargetType, "ref")
    descriptor = None
    for klass in uppaal::TargetType.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::sourcetype_is_not_abstract():
    assert not inspect.isabstract(uppaal::SourceType)


def test_uppaal::sourcetype_constructor_exists():
    assert callable(uppaal::SourceType.__init__)


def test_uppaal::sourcetype_constructor_args():
    sig = inspect.signature(uppaal::SourceType.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"

def test_uppaal::sourcetype_has_ref():
    assert hasattr(uppaal::SourceType, "ref")
    descriptor = None
    for klass in uppaal::SourceType.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::parametertype_is_not_abstract():
    assert not inspect.isabstract(uppaal::ParameterType)


def test_uppaal::parametertype_constructor_exists():
    assert callable(uppaal::ParameterType.__init__)


def test_uppaal::parametertype_constructor_args():
    sig = inspect.signature(uppaal::ParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_uppaal::parametertype_has_y():
    assert hasattr(uppaal::ParameterType, "y")
    descriptor = None
    for klass in uppaal::ParameterType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::parametertype_has_x():
    assert hasattr(uppaal::ParameterType, "x")
    descriptor = None
    for klass in uppaal::ParameterType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::parametertype_has_mixed():
    assert hasattr(uppaal::ParameterType, "mixed")
    descriptor = None
    for klass in uppaal::ParameterType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::ntatype_is_not_abstract():
    assert not inspect.isabstract(uppaal::NtaType)


def test_uppaal::ntatype_constructor_exists():
    assert callable(uppaal::NtaType.__init__)


def test_uppaal::ntatype_constructor_args():
    sig = inspect.signature(uppaal::NtaType.__init__)
    params = list(sig.parameters.keys())
    assert "system" in params, "Missing parameter 'system'"
    assert "instantiation" in params, "Missing parameter 'instantiation'"
    assert "declaration" in params, "Missing parameter 'declaration'"
    assert "imports" in params, "Missing parameter 'imports'"

def test_uppaal::ntatype_has_system():
    assert hasattr(uppaal::NtaType, "system")
    descriptor = None
    for klass in uppaal::NtaType.__mro__:
        if "system" in klass.__dict__:
            descriptor = klass.__dict__["system"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::ntatype_has_instantiation():
    assert hasattr(uppaal::NtaType, "instantiation")
    descriptor = None
    for klass in uppaal::NtaType.__mro__:
        if "instantiation" in klass.__dict__:
            descriptor = klass.__dict__["instantiation"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::ntatype_has_declaration():
    assert hasattr(uppaal::NtaType, "declaration")
    descriptor = None
    for klass in uppaal::NtaType.__mro__:
        if "declaration" in klass.__dict__:
            descriptor = klass.__dict__["declaration"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::ntatype_has_imports():
    assert hasattr(uppaal::NtaType, "imports")
    descriptor = None
    for klass in uppaal::NtaType.__mro__:
        if "imports" in klass.__dict__:
            descriptor = klass.__dict__["imports"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::nametype_is_not_abstract():
    assert not inspect.isabstract(uppaal::NameType)


def test_uppaal::nametype_constructor_exists():
    assert callable(uppaal::NameType.__init__)


def test_uppaal::nametype_constructor_args():
    sig = inspect.signature(uppaal::NameType.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_uppaal::nametype_has_y():
    assert hasattr(uppaal::NameType, "y")
    descriptor = None
    for klass in uppaal::NameType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::nametype_has_x():
    assert hasattr(uppaal::NameType, "x")
    descriptor = None
    for klass in uppaal::NameType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::nametype_has_mixed():
    assert hasattr(uppaal::NameType, "mixed")
    descriptor = None
    for klass in uppaal::NameType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::nailtype_is_not_abstract():
    assert not inspect.isabstract(uppaal::NailType)


def test_uppaal::nailtype_constructor_exists():
    assert callable(uppaal::NailType.__init__)


def test_uppaal::nailtype_constructor_args():
    sig = inspect.signature(uppaal::NailType.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_uppaal::nailtype_has_x():
    assert hasattr(uppaal::NailType, "x")
    descriptor = None
    for klass in uppaal::NailType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::nailtype_has_y():
    assert hasattr(uppaal::NailType, "y")
    descriptor = None
    for klass in uppaal::NailType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::documentroot_is_not_abstract():
    assert not inspect.isabstract(uppaal::DocumentRoot)


def test_uppaal::documentroot_constructor_exists():
    assert callable(uppaal::DocumentRoot.__init__)


def test_uppaal::documentroot_constructor_args():
    sig = inspect.signature(uppaal::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "system" in params, "Missing parameter 'system'"
    assert "instantiation" in params, "Missing parameter 'instantiation'"
    assert "declaration" in params, "Missing parameter 'declaration'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "imports" in params, "Missing parameter 'imports'"

def test_uppaal::documentroot_has_system():
    assert hasattr(uppaal::DocumentRoot, "system")
    descriptor = None
    for klass in uppaal::DocumentRoot.__mro__:
        if "system" in klass.__dict__:
            descriptor = klass.__dict__["system"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::documentroot_has_instantiation():
    assert hasattr(uppaal::DocumentRoot, "instantiation")
    descriptor = None
    for klass in uppaal::DocumentRoot.__mro__:
        if "instantiation" in klass.__dict__:
            descriptor = klass.__dict__["instantiation"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::documentroot_has_declaration():
    assert hasattr(uppaal::DocumentRoot, "declaration")
    descriptor = None
    for klass in uppaal::DocumentRoot.__mro__:
        if "declaration" in klass.__dict__:
            descriptor = klass.__dict__["declaration"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::documentroot_has_mixed():
    assert hasattr(uppaal::DocumentRoot, "mixed")
    descriptor = None
    for klass in uppaal::DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::documentroot_has_imports():
    assert hasattr(uppaal::DocumentRoot, "imports")
    descriptor = None
    for klass in uppaal::DocumentRoot.__mro__:
        if "imports" in klass.__dict__:
            descriptor = klass.__dict__["imports"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::committedtype_is_not_abstract():
    assert not inspect.isabstract(uppaal::CommittedType)


def test_uppaal::committedtype_constructor_exists():
    assert callable(uppaal::CommittedType.__init__)


def test_uppaal::committedtype_constructor_args():
    sig = inspect.signature(uppaal::CommittedType.__init__)
    params = list(sig.parameters.keys())



def test_uppaal::labeltype_is_not_abstract():
    assert not inspect.isabstract(uppaal::LabelType)


def test_uppaal::labeltype_constructor_exists():
    assert callable(uppaal::LabelType.__init__)


def test_uppaal::labeltype_constructor_args():
    sig = inspect.signature(uppaal::LabelType.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "y" in params, "Missing parameter 'y'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_uppaal::labeltype_has_x():
    assert hasattr(uppaal::LabelType, "x")
    descriptor = None
    for klass in uppaal::LabelType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::labeltype_has_mixed():
    assert hasattr(uppaal::LabelType, "mixed")
    descriptor = None
    for klass in uppaal::LabelType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::labeltype_has_y():
    assert hasattr(uppaal::LabelType, "y")
    descriptor = None
    for klass in uppaal::LabelType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_uppaal::labeltype_has_kind():
    assert hasattr(uppaal::LabelType, "kind")
    descriptor = None
    for klass in uppaal::LabelType.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::inittype_is_not_abstract():
    assert not inspect.isabstract(uppaal::InitType)


def test_uppaal::inittype_constructor_exists():
    assert callable(uppaal::InitType.__init__)


def test_uppaal::inittype_constructor_args():
    sig = inspect.signature(uppaal::InitType.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"

def test_uppaal::inittype_has_ref():
    assert hasattr(uppaal::InitType, "ref")
    descriptor = None
    for klass in uppaal::InitType.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_uppaal::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(uppaal::EStringToStringMapEntry)


def test_uppaal::estringtostringmapentry_constructor_exists():
    assert callable(uppaal::EStringToStringMapEntry.__init__)


def test_uppaal::estringtostringmapentry_constructor_args():
    sig = inspect.signature(uppaal::EStringToStringMapEntry.__init__)
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
uppaal::UrgentType_strategy = st.builds(
    uppaal::UrgentType,
)
uppaal::TransitionType_strategy = st.builds(
    uppaal::TransitionType,
    id=
        safe_text,
    y=
        safe_text,
    x=
        safe_text,
    color=
        safe_text
)
uppaal::TemplateType_strategy = st.builds(
    uppaal::TemplateType,
    declaration=
        safe_text
)
uppaal::LocationType_strategy = st.builds(
    uppaal::LocationType,
    y=
        safe_text,
    id=
        safe_text,
    color=
        safe_text,
    x=
        safe_text
)
uppaal::TargetType_strategy = st.builds(
    uppaal::TargetType,
    ref=
        safe_text
)
uppaal::SourceType_strategy = st.builds(
    uppaal::SourceType,
    ref=
        safe_text
)
uppaal::ParameterType_strategy = st.builds(
    uppaal::ParameterType,
    y=
        safe_text,
    x=
        safe_text,
    mixed=
        safe_text
)
uppaal::NtaType_strategy = st.builds(
    uppaal::NtaType,
    system=
        safe_text,
    instantiation=
        safe_text,
    declaration=
        safe_text,
    imports=
        safe_text
)
uppaal::NameType_strategy = st.builds(
    uppaal::NameType,
    y=
        safe_text,
    x=
        safe_text,
    mixed=
        safe_text
)
uppaal::NailType_strategy = st.builds(
    uppaal::NailType,
    x=
        safe_text,
    y=
        safe_text
)
uppaal::DocumentRoot_strategy = st.builds(
    uppaal::DocumentRoot,
    system=
        safe_text,
    instantiation=
        safe_text,
    declaration=
        safe_text,
    mixed=
        safe_text,
    imports=
        safe_text
)
uppaal::CommittedType_strategy = st.builds(
    uppaal::CommittedType,
)
uppaal::LabelType_strategy = st.builds(
    uppaal::LabelType,
    x=
        safe_text,
    mixed=
        safe_text,
    y=
        safe_text,
    kind=
        safe_text
)
uppaal::InitType_strategy = st.builds(
    uppaal::InitType,
    ref=
        safe_text
)
uppaal::EStringToStringMapEntry_strategy = st.builds(
    uppaal::EStringToStringMapEntry,
)

@given(instance=uppaal::UrgentType_strategy)
@settings(max_examples=50)
def test_uppaal::urgenttype_instantiation(instance):
    assert isinstance(instance, uppaal::UrgentType)

@given(instance=uppaal::TransitionType_strategy)
@settings(max_examples=50)
def test_uppaal::transitiontype_instantiation(instance):
    assert isinstance(instance, uppaal::TransitionType)

@given(instance=uppaal::TransitionType_strategy)
def test_uppaal::transitiontype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=uppaal::TransitionType_strategy)
def test_uppaal::transitiontype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=uppaal::TransitionType_strategy)
def test_uppaal::transitiontype_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=uppaal::TransitionType_strategy)
def test_uppaal::transitiontype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=uppaal::TransitionType_strategy)
def test_uppaal::transitiontype_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=uppaal::TransitionType_strategy)
def test_uppaal::transitiontype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=uppaal::TransitionType_strategy)
def test_uppaal::transitiontype_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=uppaal::TransitionType_strategy)
def test_uppaal::transitiontype_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=uppaal::TemplateType_strategy)
@settings(max_examples=50)
def test_uppaal::templatetype_instantiation(instance):
    assert isinstance(instance, uppaal::TemplateType)

@given(instance=uppaal::TemplateType_strategy)
def test_uppaal::templatetype_declaration_type(instance):
    assert isinstance(instance.declaration, str)


@given(instance=uppaal::TemplateType_strategy)
def test_uppaal::templatetype_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original

@given(instance=uppaal::LocationType_strategy)
@settings(max_examples=50)
def test_uppaal::locationtype_instantiation(instance):
    assert isinstance(instance, uppaal::LocationType)

@given(instance=uppaal::LocationType_strategy)
def test_uppaal::locationtype_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=uppaal::LocationType_strategy)
def test_uppaal::locationtype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=uppaal::LocationType_strategy)
def test_uppaal::locationtype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=uppaal::LocationType_strategy)
def test_uppaal::locationtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=uppaal::LocationType_strategy)
def test_uppaal::locationtype_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=uppaal::LocationType_strategy)
def test_uppaal::locationtype_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=uppaal::LocationType_strategy)
def test_uppaal::locationtype_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=uppaal::LocationType_strategy)
def test_uppaal::locationtype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=uppaal::TargetType_strategy)
@settings(max_examples=50)
def test_uppaal::targettype_instantiation(instance):
    assert isinstance(instance, uppaal::TargetType)

@given(instance=uppaal::TargetType_strategy)
def test_uppaal::targettype_ref_type(instance):
    assert isinstance(instance.ref, str)


@given(instance=uppaal::TargetType_strategy)
def test_uppaal::targettype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=uppaal::SourceType_strategy)
@settings(max_examples=50)
def test_uppaal::sourcetype_instantiation(instance):
    assert isinstance(instance, uppaal::SourceType)

@given(instance=uppaal::SourceType_strategy)
def test_uppaal::sourcetype_ref_type(instance):
    assert isinstance(instance.ref, str)


@given(instance=uppaal::SourceType_strategy)
def test_uppaal::sourcetype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=uppaal::ParameterType_strategy)
@settings(max_examples=50)
def test_uppaal::parametertype_instantiation(instance):
    assert isinstance(instance, uppaal::ParameterType)

@given(instance=uppaal::ParameterType_strategy)
def test_uppaal::parametertype_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=uppaal::ParameterType_strategy)
def test_uppaal::parametertype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=uppaal::ParameterType_strategy)
def test_uppaal::parametertype_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=uppaal::ParameterType_strategy)
def test_uppaal::parametertype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=uppaal::ParameterType_strategy)
def test_uppaal::parametertype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=uppaal::ParameterType_strategy)
def test_uppaal::parametertype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=uppaal::NtaType_strategy)
@settings(max_examples=50)
def test_uppaal::ntatype_instantiation(instance):
    assert isinstance(instance, uppaal::NtaType)

@given(instance=uppaal::NtaType_strategy)
def test_uppaal::ntatype_system_type(instance):
    assert isinstance(instance.system, str)


@given(instance=uppaal::NtaType_strategy)
def test_uppaal::ntatype_system_setter(instance):
    original = instance.system
    instance.system = original
    assert instance.system == original

@given(instance=uppaal::NtaType_strategy)
def test_uppaal::ntatype_instantiation_type(instance):
    assert isinstance(instance.instantiation, str)


@given(instance=uppaal::NtaType_strategy)
def test_uppaal::ntatype_instantiation_setter(instance):
    original = instance.instantiation
    instance.instantiation = original
    assert instance.instantiation == original

@given(instance=uppaal::NtaType_strategy)
def test_uppaal::ntatype_declaration_type(instance):
    assert isinstance(instance.declaration, str)


@given(instance=uppaal::NtaType_strategy)
def test_uppaal::ntatype_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original

@given(instance=uppaal::NtaType_strategy)
def test_uppaal::ntatype_imports_type(instance):
    assert isinstance(instance.imports, str)


@given(instance=uppaal::NtaType_strategy)
def test_uppaal::ntatype_imports_setter(instance):
    original = instance.imports
    instance.imports = original
    assert instance.imports == original

@given(instance=uppaal::NameType_strategy)
@settings(max_examples=50)
def test_uppaal::nametype_instantiation(instance):
    assert isinstance(instance, uppaal::NameType)

@given(instance=uppaal::NameType_strategy)
def test_uppaal::nametype_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=uppaal::NameType_strategy)
def test_uppaal::nametype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=uppaal::NameType_strategy)
def test_uppaal::nametype_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=uppaal::NameType_strategy)
def test_uppaal::nametype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=uppaal::NameType_strategy)
def test_uppaal::nametype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=uppaal::NameType_strategy)
def test_uppaal::nametype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=uppaal::NailType_strategy)
@settings(max_examples=50)
def test_uppaal::nailtype_instantiation(instance):
    assert isinstance(instance, uppaal::NailType)

@given(instance=uppaal::NailType_strategy)
def test_uppaal::nailtype_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=uppaal::NailType_strategy)
def test_uppaal::nailtype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=uppaal::NailType_strategy)
def test_uppaal::nailtype_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=uppaal::NailType_strategy)
def test_uppaal::nailtype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=uppaal::DocumentRoot_strategy)
@settings(max_examples=50)
def test_uppaal::documentroot_instantiation(instance):
    assert isinstance(instance, uppaal::DocumentRoot)

@given(instance=uppaal::DocumentRoot_strategy)
def test_uppaal::documentroot_system_type(instance):
    assert isinstance(instance.system, str)


@given(instance=uppaal::DocumentRoot_strategy)
def test_uppaal::documentroot_system_setter(instance):
    original = instance.system
    instance.system = original
    assert instance.system == original

@given(instance=uppaal::DocumentRoot_strategy)
def test_uppaal::documentroot_instantiation_type(instance):
    assert isinstance(instance.instantiation, str)


@given(instance=uppaal::DocumentRoot_strategy)
def test_uppaal::documentroot_instantiation_setter(instance):
    original = instance.instantiation
    instance.instantiation = original
    assert instance.instantiation == original

@given(instance=uppaal::DocumentRoot_strategy)
def test_uppaal::documentroot_declaration_type(instance):
    assert isinstance(instance.declaration, str)


@given(instance=uppaal::DocumentRoot_strategy)
def test_uppaal::documentroot_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original

@given(instance=uppaal::DocumentRoot_strategy)
def test_uppaal::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=uppaal::DocumentRoot_strategy)
def test_uppaal::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=uppaal::DocumentRoot_strategy)
def test_uppaal::documentroot_imports_type(instance):
    assert isinstance(instance.imports, str)


@given(instance=uppaal::DocumentRoot_strategy)
def test_uppaal::documentroot_imports_setter(instance):
    original = instance.imports
    instance.imports = original
    assert instance.imports == original

@given(instance=uppaal::CommittedType_strategy)
@settings(max_examples=50)
def test_uppaal::committedtype_instantiation(instance):
    assert isinstance(instance, uppaal::CommittedType)

@given(instance=uppaal::LabelType_strategy)
@settings(max_examples=50)
def test_uppaal::labeltype_instantiation(instance):
    assert isinstance(instance, uppaal::LabelType)

@given(instance=uppaal::LabelType_strategy)
def test_uppaal::labeltype_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=uppaal::LabelType_strategy)
def test_uppaal::labeltype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=uppaal::LabelType_strategy)
def test_uppaal::labeltype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=uppaal::LabelType_strategy)
def test_uppaal::labeltype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=uppaal::LabelType_strategy)
def test_uppaal::labeltype_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=uppaal::LabelType_strategy)
def test_uppaal::labeltype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=uppaal::LabelType_strategy)
def test_uppaal::labeltype_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=uppaal::LabelType_strategy)
def test_uppaal::labeltype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=uppaal::InitType_strategy)
@settings(max_examples=50)
def test_uppaal::inittype_instantiation(instance):
    assert isinstance(instance, uppaal::InitType)

@given(instance=uppaal::InitType_strategy)
def test_uppaal::inittype_ref_type(instance):
    assert isinstance(instance.ref, str)


@given(instance=uppaal::InitType_strategy)
def test_uppaal::inittype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=uppaal::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_uppaal::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, uppaal::EStringToStringMapEntry)
