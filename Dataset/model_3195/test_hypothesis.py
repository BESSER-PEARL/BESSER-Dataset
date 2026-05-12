import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Uppaal_TemplateType,
    Uppaal_TransitionType,
    Uppaal_TargetType,
    Uppaal_SystemType,
    Uppaal_SourceType,
    Uppaal_ParameterType,
    Uppaal_NtaType,
    Uppaal_NameType,
    Uppaal_NailType,
    Uppaal_LocationType,
    Uppaal_LabelType,
    Uppaal_InstantiationType,
    Uppaal_InitType,
    Uppaal_ImportsType,
    Uppaal_EStringToStringMapEntry,
    Uppaal_DocumentRoot,
    Uppaal_DeclarationType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uppaal_templatetype_is_not_abstract():
    assert not inspect.isabstract(Uppaal_TemplateType)


def test_uppaal_templatetype_constructor_exists():
    assert callable(Uppaal_TemplateType.__init__)


def test_uppaal_templatetype_constructor_args():
    sig = inspect.signature(Uppaal_TemplateType.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_transitiontype_is_not_abstract():
    assert not inspect.isabstract(Uppaal_TransitionType)


def test_uppaal_transitiontype_constructor_exists():
    assert callable(Uppaal_TransitionType.__init__)


def test_uppaal_transitiontype_constructor_args():
    sig = inspect.signature(Uppaal_TransitionType.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"
    assert "color" in params, "Missing parameter 'color'"
    assert "id" in params, "Missing parameter 'id'"

def test_uppaal_transitiontype_has_y():
    assert hasattr(Uppaal_TransitionType, "y")
    descriptor = None
    for klass in Uppaal_TransitionType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_transitiontype_has_x():
    assert hasattr(Uppaal_TransitionType, "x")
    descriptor = None
    for klass in Uppaal_TransitionType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_transitiontype_has_color():
    assert hasattr(Uppaal_TransitionType, "color")
    descriptor = None
    for klass in Uppaal_TransitionType.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_transitiontype_has_id():
    assert hasattr(Uppaal_TransitionType, "id")
    descriptor = None
    for klass in Uppaal_TransitionType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_targettype_is_not_abstract():
    assert not inspect.isabstract(Uppaal_TargetType)


def test_uppaal_targettype_constructor_exists():
    assert callable(Uppaal_TargetType.__init__)


def test_uppaal_targettype_constructor_args():
    sig = inspect.signature(Uppaal_TargetType.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"

def test_uppaal_targettype_has_ref():
    assert hasattr(Uppaal_TargetType, "ref")
    descriptor = None
    for klass in Uppaal_TargetType.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_systemtype_is_not_abstract():
    assert not inspect.isabstract(Uppaal_SystemType)


def test_uppaal_systemtype_constructor_exists():
    assert callable(Uppaal_SystemType.__init__)


def test_uppaal_systemtype_constructor_args():
    sig = inspect.signature(Uppaal_SystemType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_uppaal_systemtype_has_mixed():
    assert hasattr(Uppaal_SystemType, "mixed")
    descriptor = None
    for klass in Uppaal_SystemType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_sourcetype_is_not_abstract():
    assert not inspect.isabstract(Uppaal_SourceType)


def test_uppaal_sourcetype_constructor_exists():
    assert callable(Uppaal_SourceType.__init__)


def test_uppaal_sourcetype_constructor_args():
    sig = inspect.signature(Uppaal_SourceType.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"

def test_uppaal_sourcetype_has_ref():
    assert hasattr(Uppaal_SourceType, "ref")
    descriptor = None
    for klass in Uppaal_SourceType.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_parametertype_is_not_abstract():
    assert not inspect.isabstract(Uppaal_ParameterType)


def test_uppaal_parametertype_constructor_exists():
    assert callable(Uppaal_ParameterType.__init__)


def test_uppaal_parametertype_constructor_args():
    sig = inspect.signature(Uppaal_ParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "x" in params, "Missing parameter 'x'"

def test_uppaal_parametertype_has_y():
    assert hasattr(Uppaal_ParameterType, "y")
    descriptor = None
    for klass in Uppaal_ParameterType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_parametertype_has_mixed():
    assert hasattr(Uppaal_ParameterType, "mixed")
    descriptor = None
    for klass in Uppaal_ParameterType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_parametertype_has_x():
    assert hasattr(Uppaal_ParameterType, "x")
    descriptor = None
    for klass in Uppaal_ParameterType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_ntatype_is_not_abstract():
    assert not inspect.isabstract(Uppaal_NtaType)


def test_uppaal_ntatype_constructor_exists():
    assert callable(Uppaal_NtaType.__init__)


def test_uppaal_ntatype_constructor_args():
    sig = inspect.signature(Uppaal_NtaType.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_nametype_is_not_abstract():
    assert not inspect.isabstract(Uppaal_NameType)


def test_uppaal_nametype_constructor_exists():
    assert callable(Uppaal_NameType.__init__)


def test_uppaal_nametype_constructor_args():
    sig = inspect.signature(Uppaal_NameType.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "x" in params, "Missing parameter 'x'"

def test_uppaal_nametype_has_y():
    assert hasattr(Uppaal_NameType, "y")
    descriptor = None
    for klass in Uppaal_NameType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_nametype_has_mixed():
    assert hasattr(Uppaal_NameType, "mixed")
    descriptor = None
    for klass in Uppaal_NameType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_nametype_has_x():
    assert hasattr(Uppaal_NameType, "x")
    descriptor = None
    for klass in Uppaal_NameType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_nailtype_is_not_abstract():
    assert not inspect.isabstract(Uppaal_NailType)


def test_uppaal_nailtype_constructor_exists():
    assert callable(Uppaal_NailType.__init__)


def test_uppaal_nailtype_constructor_args():
    sig = inspect.signature(Uppaal_NailType.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_uppaal_nailtype_has_x():
    assert hasattr(Uppaal_NailType, "x")
    descriptor = None
    for klass in Uppaal_NailType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_nailtype_has_y():
    assert hasattr(Uppaal_NailType, "y")
    descriptor = None
    for klass in Uppaal_NailType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_locationtype_is_not_abstract():
    assert not inspect.isabstract(Uppaal_LocationType)


def test_uppaal_locationtype_constructor_exists():
    assert callable(Uppaal_LocationType.__init__)


def test_uppaal_locationtype_constructor_args():
    sig = inspect.signature(Uppaal_LocationType.__init__)
    params = list(sig.parameters.keys())
    assert "urgent" in params, "Missing parameter 'urgent'"
    assert "color" in params, "Missing parameter 'color'"
    assert "committed" in params, "Missing parameter 'committed'"
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"
    assert "id" in params, "Missing parameter 'id'"

def test_uppaal_locationtype_has_urgent():
    assert hasattr(Uppaal_LocationType, "urgent")
    descriptor = None
    for klass in Uppaal_LocationType.__mro__:
        if "urgent" in klass.__dict__:
            descriptor = klass.__dict__["urgent"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_locationtype_has_color():
    assert hasattr(Uppaal_LocationType, "color")
    descriptor = None
    for klass in Uppaal_LocationType.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_locationtype_has_committed():
    assert hasattr(Uppaal_LocationType, "committed")
    descriptor = None
    for klass in Uppaal_LocationType.__mro__:
        if "committed" in klass.__dict__:
            descriptor = klass.__dict__["committed"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_locationtype_has_y():
    assert hasattr(Uppaal_LocationType, "y")
    descriptor = None
    for klass in Uppaal_LocationType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_locationtype_has_x():
    assert hasattr(Uppaal_LocationType, "x")
    descriptor = None
    for klass in Uppaal_LocationType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_locationtype_has_id():
    assert hasattr(Uppaal_LocationType, "id")
    descriptor = None
    for klass in Uppaal_LocationType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_labeltype_is_not_abstract():
    assert not inspect.isabstract(Uppaal_LabelType)


def test_uppaal_labeltype_constructor_exists():
    assert callable(Uppaal_LabelType.__init__)


def test_uppaal_labeltype_constructor_args():
    sig = inspect.signature(Uppaal_LabelType.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"
    assert "kind" in params, "Missing parameter 'kind'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_uppaal_labeltype_has_y():
    assert hasattr(Uppaal_LabelType, "y")
    descriptor = None
    for klass in Uppaal_LabelType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_labeltype_has_x():
    assert hasattr(Uppaal_LabelType, "x")
    descriptor = None
    for klass in Uppaal_LabelType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_labeltype_has_kind():
    assert hasattr(Uppaal_LabelType, "kind")
    descriptor = None
    for klass in Uppaal_LabelType.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_labeltype_has_mixed():
    assert hasattr(Uppaal_LabelType, "mixed")
    descriptor = None
    for klass in Uppaal_LabelType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_instantiationtype_is_not_abstract():
    assert not inspect.isabstract(Uppaal_InstantiationType)


def test_uppaal_instantiationtype_constructor_exists():
    assert callable(Uppaal_InstantiationType.__init__)


def test_uppaal_instantiationtype_constructor_args():
    sig = inspect.signature(Uppaal_InstantiationType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_uppaal_instantiationtype_has_mixed():
    assert hasattr(Uppaal_InstantiationType, "mixed")
    descriptor = None
    for klass in Uppaal_InstantiationType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_inittype_is_not_abstract():
    assert not inspect.isabstract(Uppaal_InitType)


def test_uppaal_inittype_constructor_exists():
    assert callable(Uppaal_InitType.__init__)


def test_uppaal_inittype_constructor_args():
    sig = inspect.signature(Uppaal_InitType.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"

def test_uppaal_inittype_has_ref():
    assert hasattr(Uppaal_InitType, "ref")
    descriptor = None
    for klass in Uppaal_InitType.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_importstype_is_not_abstract():
    assert not inspect.isabstract(Uppaal_ImportsType)


def test_uppaal_importstype_constructor_exists():
    assert callable(Uppaal_ImportsType.__init__)


def test_uppaal_importstype_constructor_args():
    sig = inspect.signature(Uppaal_ImportsType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_uppaal_importstype_has_mixed():
    assert hasattr(Uppaal_ImportsType, "mixed")
    descriptor = None
    for klass in Uppaal_ImportsType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(Uppaal_EStringToStringMapEntry)


def test_uppaal_estringtostringmapentry_constructor_exists():
    assert callable(Uppaal_EStringToStringMapEntry.__init__)


def test_uppaal_estringtostringmapentry_constructor_args():
    sig = inspect.signature(Uppaal_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_documentroot_is_not_abstract():
    assert not inspect.isabstract(Uppaal_DocumentRoot)


def test_uppaal_documentroot_constructor_exists():
    assert callable(Uppaal_DocumentRoot.__init__)


def test_uppaal_documentroot_constructor_args():
    sig = inspect.signature(Uppaal_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "committed" in params, "Missing parameter 'committed'"
    assert "urgent" in params, "Missing parameter 'urgent'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_uppaal_documentroot_has_committed():
    assert hasattr(Uppaal_DocumentRoot, "committed")
    descriptor = None
    for klass in Uppaal_DocumentRoot.__mro__:
        if "committed" in klass.__dict__:
            descriptor = klass.__dict__["committed"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_documentroot_has_urgent():
    assert hasattr(Uppaal_DocumentRoot, "urgent")
    descriptor = None
    for klass in Uppaal_DocumentRoot.__mro__:
        if "urgent" in klass.__dict__:
            descriptor = klass.__dict__["urgent"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_documentroot_has_mixed():
    assert hasattr(Uppaal_DocumentRoot, "mixed")
    descriptor = None
    for klass in Uppaal_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_declarationtype_is_not_abstract():
    assert not inspect.isabstract(Uppaal_DeclarationType)


def test_uppaal_declarationtype_constructor_exists():
    assert callable(Uppaal_DeclarationType.__init__)


def test_uppaal_declarationtype_constructor_args():
    sig = inspect.signature(Uppaal_DeclarationType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_uppaal_declarationtype_has_mixed():
    assert hasattr(Uppaal_DeclarationType, "mixed")
    descriptor = None
    for klass in Uppaal_DeclarationType.__mro__:
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
Uppaal_TemplateType_strategy = st.builds(
    Uppaal_TemplateType,
)
Uppaal_TransitionType_strategy = st.builds(
    Uppaal_TransitionType,
    y=
        safe_text,
    x=
        safe_text,
    color=
        safe_text,
    id=
        safe_text
)
Uppaal_TargetType_strategy = st.builds(
    Uppaal_TargetType,
    ref=
        safe_text
)
Uppaal_SystemType_strategy = st.builds(
    Uppaal_SystemType,
    mixed=
        safe_text
)
Uppaal_SourceType_strategy = st.builds(
    Uppaal_SourceType,
    ref=
        safe_text
)
Uppaal_ParameterType_strategy = st.builds(
    Uppaal_ParameterType,
    y=
        safe_text,
    mixed=
        safe_text,
    x=
        safe_text
)
Uppaal_NtaType_strategy = st.builds(
    Uppaal_NtaType,
)
Uppaal_NameType_strategy = st.builds(
    Uppaal_NameType,
    y=
        safe_text,
    mixed=
        safe_text,
    x=
        safe_text
)
Uppaal_NailType_strategy = st.builds(
    Uppaal_NailType,
    x=
        safe_text,
    y=
        safe_text
)
Uppaal_LocationType_strategy = st.builds(
    Uppaal_LocationType,
    urgent=
        safe_text,
    color=
        safe_text,
    committed=
        safe_text,
    y=
        safe_text,
    x=
        safe_text,
    id=
        safe_text
)
Uppaal_LabelType_strategy = st.builds(
    Uppaal_LabelType,
    y=
        safe_text,
    x=
        safe_text,
    kind=
        safe_text,
    mixed=
        safe_text
)
Uppaal_InstantiationType_strategy = st.builds(
    Uppaal_InstantiationType,
    mixed=
        safe_text
)
Uppaal_InitType_strategy = st.builds(
    Uppaal_InitType,
    ref=
        safe_text
)
Uppaal_ImportsType_strategy = st.builds(
    Uppaal_ImportsType,
    mixed=
        safe_text
)
Uppaal_EStringToStringMapEntry_strategy = st.builds(
    Uppaal_EStringToStringMapEntry,
)
Uppaal_DocumentRoot_strategy = st.builds(
    Uppaal_DocumentRoot,
    committed=
        safe_text,
    urgent=
        safe_text,
    mixed=
        safe_text
)
Uppaal_DeclarationType_strategy = st.builds(
    Uppaal_DeclarationType,
    mixed=
        safe_text
)

@given(instance=Uppaal_TemplateType_strategy)
@settings(max_examples=50)
def test_uppaal_templatetype_instantiation(instance):
    assert isinstance(instance, Uppaal_TemplateType)

@given(instance=Uppaal_TransitionType_strategy)
@settings(max_examples=50)
def test_uppaal_transitiontype_instantiation(instance):
    assert isinstance(instance, Uppaal_TransitionType)



@given(instance=Uppaal_TransitionType_strategy)
def test_uppaal_transitiontype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=Uppaal_TransitionType_strategy)
def test_uppaal_transitiontype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=Uppaal_TransitionType_strategy)
def test_uppaal_transitiontype_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=Uppaal_TransitionType_strategy)
def test_uppaal_transitiontype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Uppaal_TargetType_strategy)
@settings(max_examples=50)
def test_uppaal_targettype_instantiation(instance):
    assert isinstance(instance, Uppaal_TargetType)



@given(instance=Uppaal_TargetType_strategy)
def test_uppaal_targettype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=Uppaal_SystemType_strategy)
@settings(max_examples=50)
def test_uppaal_systemtype_instantiation(instance):
    assert isinstance(instance, Uppaal_SystemType)



@given(instance=Uppaal_SystemType_strategy)
def test_uppaal_systemtype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Uppaal_SourceType_strategy)
@settings(max_examples=50)
def test_uppaal_sourcetype_instantiation(instance):
    assert isinstance(instance, Uppaal_SourceType)



@given(instance=Uppaal_SourceType_strategy)
def test_uppaal_sourcetype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=Uppaal_ParameterType_strategy)
@settings(max_examples=50)
def test_uppaal_parametertype_instantiation(instance):
    assert isinstance(instance, Uppaal_ParameterType)



@given(instance=Uppaal_ParameterType_strategy)
def test_uppaal_parametertype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=Uppaal_ParameterType_strategy)
def test_uppaal_parametertype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=Uppaal_ParameterType_strategy)
def test_uppaal_parametertype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=Uppaal_NtaType_strategy)
@settings(max_examples=50)
def test_uppaal_ntatype_instantiation(instance):
    assert isinstance(instance, Uppaal_NtaType)

@given(instance=Uppaal_NameType_strategy)
@settings(max_examples=50)
def test_uppaal_nametype_instantiation(instance):
    assert isinstance(instance, Uppaal_NameType)



@given(instance=Uppaal_NameType_strategy)
def test_uppaal_nametype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=Uppaal_NameType_strategy)
def test_uppaal_nametype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=Uppaal_NameType_strategy)
def test_uppaal_nametype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=Uppaal_NailType_strategy)
@settings(max_examples=50)
def test_uppaal_nailtype_instantiation(instance):
    assert isinstance(instance, Uppaal_NailType)



@given(instance=Uppaal_NailType_strategy)
def test_uppaal_nailtype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=Uppaal_NailType_strategy)
def test_uppaal_nailtype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=Uppaal_LocationType_strategy)
@settings(max_examples=50)
def test_uppaal_locationtype_instantiation(instance):
    assert isinstance(instance, Uppaal_LocationType)



@given(instance=Uppaal_LocationType_strategy)
def test_uppaal_locationtype_urgent_setter(instance):
    original = instance.urgent
    instance.urgent = original
    assert instance.urgent == original



@given(instance=Uppaal_LocationType_strategy)
def test_uppaal_locationtype_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=Uppaal_LocationType_strategy)
def test_uppaal_locationtype_committed_setter(instance):
    original = instance.committed
    instance.committed = original
    assert instance.committed == original



@given(instance=Uppaal_LocationType_strategy)
def test_uppaal_locationtype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=Uppaal_LocationType_strategy)
def test_uppaal_locationtype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=Uppaal_LocationType_strategy)
def test_uppaal_locationtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Uppaal_LabelType_strategy)
@settings(max_examples=50)
def test_uppaal_labeltype_instantiation(instance):
    assert isinstance(instance, Uppaal_LabelType)



@given(instance=Uppaal_LabelType_strategy)
def test_uppaal_labeltype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=Uppaal_LabelType_strategy)
def test_uppaal_labeltype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=Uppaal_LabelType_strategy)
def test_uppaal_labeltype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=Uppaal_LabelType_strategy)
def test_uppaal_labeltype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Uppaal_InstantiationType_strategy)
@settings(max_examples=50)
def test_uppaal_instantiationtype_instantiation(instance):
    assert isinstance(instance, Uppaal_InstantiationType)



@given(instance=Uppaal_InstantiationType_strategy)
def test_uppaal_instantiationtype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Uppaal_InitType_strategy)
@settings(max_examples=50)
def test_uppaal_inittype_instantiation(instance):
    assert isinstance(instance, Uppaal_InitType)



@given(instance=Uppaal_InitType_strategy)
def test_uppaal_inittype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=Uppaal_ImportsType_strategy)
@settings(max_examples=50)
def test_uppaal_importstype_instantiation(instance):
    assert isinstance(instance, Uppaal_ImportsType)



@given(instance=Uppaal_ImportsType_strategy)
def test_uppaal_importstype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Uppaal_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_uppaal_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, Uppaal_EStringToStringMapEntry)

@given(instance=Uppaal_DocumentRoot_strategy)
@settings(max_examples=50)
def test_uppaal_documentroot_instantiation(instance):
    assert isinstance(instance, Uppaal_DocumentRoot)



@given(instance=Uppaal_DocumentRoot_strategy)
def test_uppaal_documentroot_committed_setter(instance):
    original = instance.committed
    instance.committed = original
    assert instance.committed == original



@given(instance=Uppaal_DocumentRoot_strategy)
def test_uppaal_documentroot_urgent_setter(instance):
    original = instance.urgent
    instance.urgent = original
    assert instance.urgent == original



@given(instance=Uppaal_DocumentRoot_strategy)
def test_uppaal_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Uppaal_DeclarationType_strategy)
@settings(max_examples=50)
def test_uppaal_declarationtype_instantiation(instance):
    assert isinstance(instance, Uppaal_DeclarationType)



@given(instance=Uppaal_DeclarationType_strategy)
def test_uppaal_declarationtype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original
