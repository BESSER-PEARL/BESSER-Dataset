import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    UppaalFlat11::SourceType,
    UppaalFlat11::ParameterType,
    UppaalFlat11::NtaType,
    UppaalFlat11::NameType,
    UppaalFlat11::NailType,
    UppaalFlat11::UrgentType,
    UppaalFlat11::TransitionType,
    UppaalFlat11::TemplateType,
    UppaalFlat11::TargetType,
    UppaalFlat11::EStringToStringMapEntry,
    UppaalFlat11::LocationType,
    UppaalFlat11::LabelType,
    UppaalFlat11::InitType,
    UppaalFlat11::DocumentRoot,
    UppaalFlat11::CommittedType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uppaalflat11::sourcetype_is_not_abstract():
    assert not inspect.isabstract(UppaalFlat11::SourceType)


def test_uppaalflat11::sourcetype_constructor_exists():
    assert callable(UppaalFlat11::SourceType.__init__)


def test_uppaalflat11::sourcetype_constructor_args():
    sig = inspect.signature(UppaalFlat11::SourceType.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"

def test_uppaalflat11::sourcetype_has_ref():
    assert hasattr(UppaalFlat11::SourceType, "ref")
    descriptor = None
    for klass in UppaalFlat11::SourceType.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_uppaalflat11::parametertype_is_not_abstract():
    assert not inspect.isabstract(UppaalFlat11::ParameterType)


def test_uppaalflat11::parametertype_constructor_exists():
    assert callable(UppaalFlat11::ParameterType.__init__)


def test_uppaalflat11::parametertype_constructor_args():
    sig = inspect.signature(UppaalFlat11::ParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_uppaalflat11::parametertype_has_mixed():
    assert hasattr(UppaalFlat11::ParameterType, "mixed")
    descriptor = None
    for klass in UppaalFlat11::ParameterType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11::parametertype_has_y():
    assert hasattr(UppaalFlat11::ParameterType, "y")
    descriptor = None
    for klass in UppaalFlat11::ParameterType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11::parametertype_has_x():
    assert hasattr(UppaalFlat11::ParameterType, "x")
    descriptor = None
    for klass in UppaalFlat11::ParameterType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_uppaalflat11::ntatype_is_not_abstract():
    assert not inspect.isabstract(UppaalFlat11::NtaType)


def test_uppaalflat11::ntatype_constructor_exists():
    assert callable(UppaalFlat11::NtaType.__init__)


def test_uppaalflat11::ntatype_constructor_args():
    sig = inspect.signature(UppaalFlat11::NtaType.__init__)
    params = list(sig.parameters.keys())
    assert "imports" in params, "Missing parameter 'imports'"
    assert "instantiation" in params, "Missing parameter 'instantiation'"
    assert "system" in params, "Missing parameter 'system'"
    assert "declaration" in params, "Missing parameter 'declaration'"

def test_uppaalflat11::ntatype_has_imports():
    assert hasattr(UppaalFlat11::NtaType, "imports")
    descriptor = None
    for klass in UppaalFlat11::NtaType.__mro__:
        if "imports" in klass.__dict__:
            descriptor = klass.__dict__["imports"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11::ntatype_has_instantiation():
    assert hasattr(UppaalFlat11::NtaType, "instantiation")
    descriptor = None
    for klass in UppaalFlat11::NtaType.__mro__:
        if "instantiation" in klass.__dict__:
            descriptor = klass.__dict__["instantiation"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11::ntatype_has_system():
    assert hasattr(UppaalFlat11::NtaType, "system")
    descriptor = None
    for klass in UppaalFlat11::NtaType.__mro__:
        if "system" in klass.__dict__:
            descriptor = klass.__dict__["system"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11::ntatype_has_declaration():
    assert hasattr(UppaalFlat11::NtaType, "declaration")
    descriptor = None
    for klass in UppaalFlat11::NtaType.__mro__:
        if "declaration" in klass.__dict__:
            descriptor = klass.__dict__["declaration"]
            break
    assert isinstance(descriptor, property)



def test_uppaalflat11::nametype_is_not_abstract():
    assert not inspect.isabstract(UppaalFlat11::NameType)


def test_uppaalflat11::nametype_constructor_exists():
    assert callable(UppaalFlat11::NameType.__init__)


def test_uppaalflat11::nametype_constructor_args():
    sig = inspect.signature(UppaalFlat11::NameType.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_uppaalflat11::nametype_has_y():
    assert hasattr(UppaalFlat11::NameType, "y")
    descriptor = None
    for klass in UppaalFlat11::NameType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11::nametype_has_x():
    assert hasattr(UppaalFlat11::NameType, "x")
    descriptor = None
    for klass in UppaalFlat11::NameType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11::nametype_has_mixed():
    assert hasattr(UppaalFlat11::NameType, "mixed")
    descriptor = None
    for klass in UppaalFlat11::NameType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_uppaalflat11::nailtype_is_not_abstract():
    assert not inspect.isabstract(UppaalFlat11::NailType)


def test_uppaalflat11::nailtype_constructor_exists():
    assert callable(UppaalFlat11::NailType.__init__)


def test_uppaalflat11::nailtype_constructor_args():
    sig = inspect.signature(UppaalFlat11::NailType.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_uppaalflat11::nailtype_has_y():
    assert hasattr(UppaalFlat11::NailType, "y")
    descriptor = None
    for klass in UppaalFlat11::NailType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11::nailtype_has_x():
    assert hasattr(UppaalFlat11::NailType, "x")
    descriptor = None
    for klass in UppaalFlat11::NailType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_uppaalflat11::urgenttype_is_not_abstract():
    assert not inspect.isabstract(UppaalFlat11::UrgentType)


def test_uppaalflat11::urgenttype_constructor_exists():
    assert callable(UppaalFlat11::UrgentType.__init__)


def test_uppaalflat11::urgenttype_constructor_args():
    sig = inspect.signature(UppaalFlat11::UrgentType.__init__)
    params = list(sig.parameters.keys())



def test_uppaalflat11::transitiontype_is_not_abstract():
    assert not inspect.isabstract(UppaalFlat11::TransitionType)


def test_uppaalflat11::transitiontype_constructor_exists():
    assert callable(UppaalFlat11::TransitionType.__init__)


def test_uppaalflat11::transitiontype_constructor_args():
    sig = inspect.signature(UppaalFlat11::TransitionType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "y" in params, "Missing parameter 'y'"
    assert "color" in params, "Missing parameter 'color'"
    assert "x" in params, "Missing parameter 'x'"

def test_uppaalflat11::transitiontype_has_id():
    assert hasattr(UppaalFlat11::TransitionType, "id")
    descriptor = None
    for klass in UppaalFlat11::TransitionType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11::transitiontype_has_y():
    assert hasattr(UppaalFlat11::TransitionType, "y")
    descriptor = None
    for klass in UppaalFlat11::TransitionType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11::transitiontype_has_color():
    assert hasattr(UppaalFlat11::TransitionType, "color")
    descriptor = None
    for klass in UppaalFlat11::TransitionType.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11::transitiontype_has_x():
    assert hasattr(UppaalFlat11::TransitionType, "x")
    descriptor = None
    for klass in UppaalFlat11::TransitionType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_uppaalflat11::templatetype_is_not_abstract():
    assert not inspect.isabstract(UppaalFlat11::TemplateType)


def test_uppaalflat11::templatetype_constructor_exists():
    assert callable(UppaalFlat11::TemplateType.__init__)


def test_uppaalflat11::templatetype_constructor_args():
    sig = inspect.signature(UppaalFlat11::TemplateType.__init__)
    params = list(sig.parameters.keys())
    assert "declaration" in params, "Missing parameter 'declaration'"

def test_uppaalflat11::templatetype_has_declaration():
    assert hasattr(UppaalFlat11::TemplateType, "declaration")
    descriptor = None
    for klass in UppaalFlat11::TemplateType.__mro__:
        if "declaration" in klass.__dict__:
            descriptor = klass.__dict__["declaration"]
            break
    assert isinstance(descriptor, property)



def test_uppaalflat11::targettype_is_not_abstract():
    assert not inspect.isabstract(UppaalFlat11::TargetType)


def test_uppaalflat11::targettype_constructor_exists():
    assert callable(UppaalFlat11::TargetType.__init__)


def test_uppaalflat11::targettype_constructor_args():
    sig = inspect.signature(UppaalFlat11::TargetType.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"

def test_uppaalflat11::targettype_has_ref():
    assert hasattr(UppaalFlat11::TargetType, "ref")
    descriptor = None
    for klass in UppaalFlat11::TargetType.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_uppaalflat11::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(UppaalFlat11::EStringToStringMapEntry)


def test_uppaalflat11::estringtostringmapentry_constructor_exists():
    assert callable(UppaalFlat11::EStringToStringMapEntry.__init__)


def test_uppaalflat11::estringtostringmapentry_constructor_args():
    sig = inspect.signature(UppaalFlat11::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_uppaalflat11::locationtype_is_not_abstract():
    assert not inspect.isabstract(UppaalFlat11::LocationType)


def test_uppaalflat11::locationtype_constructor_exists():
    assert callable(UppaalFlat11::LocationType.__init__)


def test_uppaalflat11::locationtype_constructor_args():
    sig = inspect.signature(UppaalFlat11::LocationType.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"
    assert "color" in params, "Missing parameter 'color'"
    assert "id" in params, "Missing parameter 'id'"

def test_uppaalflat11::locationtype_has_x():
    assert hasattr(UppaalFlat11::LocationType, "x")
    descriptor = None
    for klass in UppaalFlat11::LocationType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11::locationtype_has_y():
    assert hasattr(UppaalFlat11::LocationType, "y")
    descriptor = None
    for klass in UppaalFlat11::LocationType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11::locationtype_has_color():
    assert hasattr(UppaalFlat11::LocationType, "color")
    descriptor = None
    for klass in UppaalFlat11::LocationType.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11::locationtype_has_id():
    assert hasattr(UppaalFlat11::LocationType, "id")
    descriptor = None
    for klass in UppaalFlat11::LocationType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_uppaalflat11::labeltype_is_not_abstract():
    assert not inspect.isabstract(UppaalFlat11::LabelType)


def test_uppaalflat11::labeltype_constructor_exists():
    assert callable(UppaalFlat11::LabelType.__init__)


def test_uppaalflat11::labeltype_constructor_args():
    sig = inspect.signature(UppaalFlat11::LabelType.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_uppaalflat11::labeltype_has_kind():
    assert hasattr(UppaalFlat11::LabelType, "kind")
    descriptor = None
    for klass in UppaalFlat11::LabelType.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11::labeltype_has_y():
    assert hasattr(UppaalFlat11::LabelType, "y")
    descriptor = None
    for klass in UppaalFlat11::LabelType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11::labeltype_has_x():
    assert hasattr(UppaalFlat11::LabelType, "x")
    descriptor = None
    for klass in UppaalFlat11::LabelType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11::labeltype_has_mixed():
    assert hasattr(UppaalFlat11::LabelType, "mixed")
    descriptor = None
    for klass in UppaalFlat11::LabelType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_uppaalflat11::inittype_is_not_abstract():
    assert not inspect.isabstract(UppaalFlat11::InitType)


def test_uppaalflat11::inittype_constructor_exists():
    assert callable(UppaalFlat11::InitType.__init__)


def test_uppaalflat11::inittype_constructor_args():
    sig = inspect.signature(UppaalFlat11::InitType.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"

def test_uppaalflat11::inittype_has_ref():
    assert hasattr(UppaalFlat11::InitType, "ref")
    descriptor = None
    for klass in UppaalFlat11::InitType.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_uppaalflat11::documentroot_is_not_abstract():
    assert not inspect.isabstract(UppaalFlat11::DocumentRoot)


def test_uppaalflat11::documentroot_constructor_exists():
    assert callable(UppaalFlat11::DocumentRoot.__init__)


def test_uppaalflat11::documentroot_constructor_args():
    sig = inspect.signature(UppaalFlat11::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "declaration" in params, "Missing parameter 'declaration'"
    assert "imports" in params, "Missing parameter 'imports'"
    assert "instantiation" in params, "Missing parameter 'instantiation'"
    assert "system" in params, "Missing parameter 'system'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_uppaalflat11::documentroot_has_declaration():
    assert hasattr(UppaalFlat11::DocumentRoot, "declaration")
    descriptor = None
    for klass in UppaalFlat11::DocumentRoot.__mro__:
        if "declaration" in klass.__dict__:
            descriptor = klass.__dict__["declaration"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11::documentroot_has_imports():
    assert hasattr(UppaalFlat11::DocumentRoot, "imports")
    descriptor = None
    for klass in UppaalFlat11::DocumentRoot.__mro__:
        if "imports" in klass.__dict__:
            descriptor = klass.__dict__["imports"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11::documentroot_has_instantiation():
    assert hasattr(UppaalFlat11::DocumentRoot, "instantiation")
    descriptor = None
    for klass in UppaalFlat11::DocumentRoot.__mro__:
        if "instantiation" in klass.__dict__:
            descriptor = klass.__dict__["instantiation"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11::documentroot_has_system():
    assert hasattr(UppaalFlat11::DocumentRoot, "system")
    descriptor = None
    for klass in UppaalFlat11::DocumentRoot.__mro__:
        if "system" in klass.__dict__:
            descriptor = klass.__dict__["system"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11::documentroot_has_mixed():
    assert hasattr(UppaalFlat11::DocumentRoot, "mixed")
    descriptor = None
    for klass in UppaalFlat11::DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_uppaalflat11::committedtype_is_not_abstract():
    assert not inspect.isabstract(UppaalFlat11::CommittedType)


def test_uppaalflat11::committedtype_constructor_exists():
    assert callable(UppaalFlat11::CommittedType.__init__)


def test_uppaalflat11::committedtype_constructor_args():
    sig = inspect.signature(UppaalFlat11::CommittedType.__init__)
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
UppaalFlat11::SourceType_strategy = st.builds(
    UppaalFlat11::SourceType,
    ref=
        safe_text
)
UppaalFlat11::ParameterType_strategy = st.builds(
    UppaalFlat11::ParameterType,
    mixed=
        safe_text,
    y=
        safe_text,
    x=
        safe_text
)
UppaalFlat11::NtaType_strategy = st.builds(
    UppaalFlat11::NtaType,
    imports=
        safe_text,
    instantiation=
        safe_text,
    system=
        safe_text,
    declaration=
        safe_text
)
UppaalFlat11::NameType_strategy = st.builds(
    UppaalFlat11::NameType,
    y=
        safe_text,
    x=
        safe_text,
    mixed=
        safe_text
)
UppaalFlat11::NailType_strategy = st.builds(
    UppaalFlat11::NailType,
    y=
        safe_text,
    x=
        safe_text
)
UppaalFlat11::UrgentType_strategy = st.builds(
    UppaalFlat11::UrgentType,
)
UppaalFlat11::TransitionType_strategy = st.builds(
    UppaalFlat11::TransitionType,
    id=
        safe_text,
    y=
        safe_text,
    color=
        safe_text,
    x=
        safe_text
)
UppaalFlat11::TemplateType_strategy = st.builds(
    UppaalFlat11::TemplateType,
    declaration=
        safe_text
)
UppaalFlat11::TargetType_strategy = st.builds(
    UppaalFlat11::TargetType,
    ref=
        safe_text
)
UppaalFlat11::EStringToStringMapEntry_strategy = st.builds(
    UppaalFlat11::EStringToStringMapEntry,
)
UppaalFlat11::LocationType_strategy = st.builds(
    UppaalFlat11::LocationType,
    x=
        safe_text,
    y=
        safe_text,
    color=
        safe_text,
    id=
        safe_text
)
UppaalFlat11::LabelType_strategy = st.builds(
    UppaalFlat11::LabelType,
    kind=
        safe_text,
    y=
        safe_text,
    x=
        safe_text,
    mixed=
        safe_text
)
UppaalFlat11::InitType_strategy = st.builds(
    UppaalFlat11::InitType,
    ref=
        safe_text
)
UppaalFlat11::DocumentRoot_strategy = st.builds(
    UppaalFlat11::DocumentRoot,
    declaration=
        safe_text,
    imports=
        safe_text,
    instantiation=
        safe_text,
    system=
        safe_text,
    mixed=
        safe_text
)
UppaalFlat11::CommittedType_strategy = st.builds(
    UppaalFlat11::CommittedType,
)

@given(instance=UppaalFlat11::SourceType_strategy)
@settings(max_examples=50)
def test_uppaalflat11::sourcetype_instantiation(instance):
    assert isinstance(instance, UppaalFlat11::SourceType)

@given(instance=UppaalFlat11::SourceType_strategy)
def test_uppaalflat11::sourcetype_ref_type(instance):
    assert isinstance(instance.ref, str)


@given(instance=UppaalFlat11::SourceType_strategy)
def test_uppaalflat11::sourcetype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=UppaalFlat11::ParameterType_strategy)
@settings(max_examples=50)
def test_uppaalflat11::parametertype_instantiation(instance):
    assert isinstance(instance, UppaalFlat11::ParameterType)

@given(instance=UppaalFlat11::ParameterType_strategy)
def test_uppaalflat11::parametertype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=UppaalFlat11::ParameterType_strategy)
def test_uppaalflat11::parametertype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=UppaalFlat11::ParameterType_strategy)
def test_uppaalflat11::parametertype_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=UppaalFlat11::ParameterType_strategy)
def test_uppaalflat11::parametertype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=UppaalFlat11::ParameterType_strategy)
def test_uppaalflat11::parametertype_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=UppaalFlat11::ParameterType_strategy)
def test_uppaalflat11::parametertype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=UppaalFlat11::NtaType_strategy)
@settings(max_examples=50)
def test_uppaalflat11::ntatype_instantiation(instance):
    assert isinstance(instance, UppaalFlat11::NtaType)

@given(instance=UppaalFlat11::NtaType_strategy)
def test_uppaalflat11::ntatype_imports_type(instance):
    assert isinstance(instance.imports, str)


@given(instance=UppaalFlat11::NtaType_strategy)
def test_uppaalflat11::ntatype_imports_setter(instance):
    original = instance.imports
    instance.imports = original
    assert instance.imports == original

@given(instance=UppaalFlat11::NtaType_strategy)
def test_uppaalflat11::ntatype_instantiation_type(instance):
    assert isinstance(instance.instantiation, str)


@given(instance=UppaalFlat11::NtaType_strategy)
def test_uppaalflat11::ntatype_instantiation_setter(instance):
    original = instance.instantiation
    instance.instantiation = original
    assert instance.instantiation == original

@given(instance=UppaalFlat11::NtaType_strategy)
def test_uppaalflat11::ntatype_system_type(instance):
    assert isinstance(instance.system, str)


@given(instance=UppaalFlat11::NtaType_strategy)
def test_uppaalflat11::ntatype_system_setter(instance):
    original = instance.system
    instance.system = original
    assert instance.system == original

@given(instance=UppaalFlat11::NtaType_strategy)
def test_uppaalflat11::ntatype_declaration_type(instance):
    assert isinstance(instance.declaration, str)


@given(instance=UppaalFlat11::NtaType_strategy)
def test_uppaalflat11::ntatype_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original

@given(instance=UppaalFlat11::NameType_strategy)
@settings(max_examples=50)
def test_uppaalflat11::nametype_instantiation(instance):
    assert isinstance(instance, UppaalFlat11::NameType)

@given(instance=UppaalFlat11::NameType_strategy)
def test_uppaalflat11::nametype_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=UppaalFlat11::NameType_strategy)
def test_uppaalflat11::nametype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=UppaalFlat11::NameType_strategy)
def test_uppaalflat11::nametype_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=UppaalFlat11::NameType_strategy)
def test_uppaalflat11::nametype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=UppaalFlat11::NameType_strategy)
def test_uppaalflat11::nametype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=UppaalFlat11::NameType_strategy)
def test_uppaalflat11::nametype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=UppaalFlat11::NailType_strategy)
@settings(max_examples=50)
def test_uppaalflat11::nailtype_instantiation(instance):
    assert isinstance(instance, UppaalFlat11::NailType)

@given(instance=UppaalFlat11::NailType_strategy)
def test_uppaalflat11::nailtype_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=UppaalFlat11::NailType_strategy)
def test_uppaalflat11::nailtype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=UppaalFlat11::NailType_strategy)
def test_uppaalflat11::nailtype_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=UppaalFlat11::NailType_strategy)
def test_uppaalflat11::nailtype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=UppaalFlat11::UrgentType_strategy)
@settings(max_examples=50)
def test_uppaalflat11::urgenttype_instantiation(instance):
    assert isinstance(instance, UppaalFlat11::UrgentType)

@given(instance=UppaalFlat11::TransitionType_strategy)
@settings(max_examples=50)
def test_uppaalflat11::transitiontype_instantiation(instance):
    assert isinstance(instance, UppaalFlat11::TransitionType)

@given(instance=UppaalFlat11::TransitionType_strategy)
def test_uppaalflat11::transitiontype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=UppaalFlat11::TransitionType_strategy)
def test_uppaalflat11::transitiontype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=UppaalFlat11::TransitionType_strategy)
def test_uppaalflat11::transitiontype_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=UppaalFlat11::TransitionType_strategy)
def test_uppaalflat11::transitiontype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=UppaalFlat11::TransitionType_strategy)
def test_uppaalflat11::transitiontype_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=UppaalFlat11::TransitionType_strategy)
def test_uppaalflat11::transitiontype_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=UppaalFlat11::TransitionType_strategy)
def test_uppaalflat11::transitiontype_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=UppaalFlat11::TransitionType_strategy)
def test_uppaalflat11::transitiontype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=UppaalFlat11::TemplateType_strategy)
@settings(max_examples=50)
def test_uppaalflat11::templatetype_instantiation(instance):
    assert isinstance(instance, UppaalFlat11::TemplateType)

@given(instance=UppaalFlat11::TemplateType_strategy)
def test_uppaalflat11::templatetype_declaration_type(instance):
    assert isinstance(instance.declaration, str)


@given(instance=UppaalFlat11::TemplateType_strategy)
def test_uppaalflat11::templatetype_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original

@given(instance=UppaalFlat11::TargetType_strategy)
@settings(max_examples=50)
def test_uppaalflat11::targettype_instantiation(instance):
    assert isinstance(instance, UppaalFlat11::TargetType)

@given(instance=UppaalFlat11::TargetType_strategy)
def test_uppaalflat11::targettype_ref_type(instance):
    assert isinstance(instance.ref, str)


@given(instance=UppaalFlat11::TargetType_strategy)
def test_uppaalflat11::targettype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=UppaalFlat11::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_uppaalflat11::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, UppaalFlat11::EStringToStringMapEntry)

@given(instance=UppaalFlat11::LocationType_strategy)
@settings(max_examples=50)
def test_uppaalflat11::locationtype_instantiation(instance):
    assert isinstance(instance, UppaalFlat11::LocationType)

@given(instance=UppaalFlat11::LocationType_strategy)
def test_uppaalflat11::locationtype_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=UppaalFlat11::LocationType_strategy)
def test_uppaalflat11::locationtype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=UppaalFlat11::LocationType_strategy)
def test_uppaalflat11::locationtype_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=UppaalFlat11::LocationType_strategy)
def test_uppaalflat11::locationtype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=UppaalFlat11::LocationType_strategy)
def test_uppaalflat11::locationtype_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=UppaalFlat11::LocationType_strategy)
def test_uppaalflat11::locationtype_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=UppaalFlat11::LocationType_strategy)
def test_uppaalflat11::locationtype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=UppaalFlat11::LocationType_strategy)
def test_uppaalflat11::locationtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=UppaalFlat11::LabelType_strategy)
@settings(max_examples=50)
def test_uppaalflat11::labeltype_instantiation(instance):
    assert isinstance(instance, UppaalFlat11::LabelType)

@given(instance=UppaalFlat11::LabelType_strategy)
def test_uppaalflat11::labeltype_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=UppaalFlat11::LabelType_strategy)
def test_uppaalflat11::labeltype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=UppaalFlat11::LabelType_strategy)
def test_uppaalflat11::labeltype_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=UppaalFlat11::LabelType_strategy)
def test_uppaalflat11::labeltype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=UppaalFlat11::LabelType_strategy)
def test_uppaalflat11::labeltype_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=UppaalFlat11::LabelType_strategy)
def test_uppaalflat11::labeltype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=UppaalFlat11::LabelType_strategy)
def test_uppaalflat11::labeltype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=UppaalFlat11::LabelType_strategy)
def test_uppaalflat11::labeltype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=UppaalFlat11::InitType_strategy)
@settings(max_examples=50)
def test_uppaalflat11::inittype_instantiation(instance):
    assert isinstance(instance, UppaalFlat11::InitType)

@given(instance=UppaalFlat11::InitType_strategy)
def test_uppaalflat11::inittype_ref_type(instance):
    assert isinstance(instance.ref, str)


@given(instance=UppaalFlat11::InitType_strategy)
def test_uppaalflat11::inittype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=UppaalFlat11::DocumentRoot_strategy)
@settings(max_examples=50)
def test_uppaalflat11::documentroot_instantiation(instance):
    assert isinstance(instance, UppaalFlat11::DocumentRoot)

@given(instance=UppaalFlat11::DocumentRoot_strategy)
def test_uppaalflat11::documentroot_declaration_type(instance):
    assert isinstance(instance.declaration, str)


@given(instance=UppaalFlat11::DocumentRoot_strategy)
def test_uppaalflat11::documentroot_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original

@given(instance=UppaalFlat11::DocumentRoot_strategy)
def test_uppaalflat11::documentroot_imports_type(instance):
    assert isinstance(instance.imports, str)


@given(instance=UppaalFlat11::DocumentRoot_strategy)
def test_uppaalflat11::documentroot_imports_setter(instance):
    original = instance.imports
    instance.imports = original
    assert instance.imports == original

@given(instance=UppaalFlat11::DocumentRoot_strategy)
def test_uppaalflat11::documentroot_instantiation_type(instance):
    assert isinstance(instance.instantiation, str)


@given(instance=UppaalFlat11::DocumentRoot_strategy)
def test_uppaalflat11::documentroot_instantiation_setter(instance):
    original = instance.instantiation
    instance.instantiation = original
    assert instance.instantiation == original

@given(instance=UppaalFlat11::DocumentRoot_strategy)
def test_uppaalflat11::documentroot_system_type(instance):
    assert isinstance(instance.system, str)


@given(instance=UppaalFlat11::DocumentRoot_strategy)
def test_uppaalflat11::documentroot_system_setter(instance):
    original = instance.system
    instance.system = original
    assert instance.system == original

@given(instance=UppaalFlat11::DocumentRoot_strategy)
def test_uppaalflat11::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=UppaalFlat11::DocumentRoot_strategy)
def test_uppaalflat11::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=UppaalFlat11::CommittedType_strategy)
@settings(max_examples=50)
def test_uppaalflat11::committedtype_instantiation(instance):
    assert isinstance(instance, UppaalFlat11::CommittedType)
