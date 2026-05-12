import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    flat11_UrgentType,
    flat11_TransitionType,
    flat11_LabelType,
    flat11_TemplateType,
    flat11_TargetType,
    flat11_SourceType,
    flat11_ParameterType,
    flat11_NtaType,
    flat11_NameType,
    flat11_NailType,
    flat11_LocationType,
    flat11_InitType,
    flat11_EStringToStringMapEntry,
    flat11_DocumentRoot,
    flat11_CommittedType,
    KindType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_flat11_urgenttype_is_not_abstract():
    assert not inspect.isabstract(flat11_UrgentType)


def test_flat11_urgenttype_constructor_exists():
    assert callable(flat11_UrgentType.__init__)


def test_flat11_urgenttype_constructor_args():
    sig = inspect.signature(flat11_UrgentType.__init__)
    params = list(sig.parameters.keys())



def test_flat11_transitiontype_is_not_abstract():
    assert not inspect.isabstract(flat11_TransitionType)


def test_flat11_transitiontype_constructor_exists():
    assert callable(flat11_TransitionType.__init__)


def test_flat11_transitiontype_constructor_args():
    sig = inspect.signature(flat11_TransitionType.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"
    assert "controllable" in params, "Missing parameter 'controllable'"
    assert "action" in params, "Missing parameter 'action'"
    assert "id" in params, "Missing parameter 'id'"

def test_flat11_transitiontype_has_color():
    assert hasattr(flat11_TransitionType, "color")
    descriptor = None
    for klass in flat11_TransitionType.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_flat11_transitiontype_has_x():
    assert hasattr(flat11_TransitionType, "x")
    descriptor = None
    for klass in flat11_TransitionType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_flat11_transitiontype_has_y():
    assert hasattr(flat11_TransitionType, "y")
    descriptor = None
    for klass in flat11_TransitionType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_flat11_transitiontype_has_controllable():
    assert hasattr(flat11_TransitionType, "controllable")
    descriptor = None
    for klass in flat11_TransitionType.__mro__:
        if "controllable" in klass.__dict__:
            descriptor = klass.__dict__["controllable"]
            break
    assert isinstance(descriptor, property)

def test_flat11_transitiontype_has_action():
    assert hasattr(flat11_TransitionType, "action")
    descriptor = None
    for klass in flat11_TransitionType.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_flat11_transitiontype_has_id():
    assert hasattr(flat11_TransitionType, "id")
    descriptor = None
    for klass in flat11_TransitionType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_flat11_labeltype_is_not_abstract():
    assert not inspect.isabstract(flat11_LabelType)


def test_flat11_labeltype_constructor_exists():
    assert callable(flat11_LabelType.__init__)


def test_flat11_labeltype_constructor_args():
    sig = inspect.signature(flat11_LabelType.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "value" in params, "Missing parameter 'value'"
    assert "kind" in params, "Missing parameter 'kind'"
    assert "x" in params, "Missing parameter 'x'"

def test_flat11_labeltype_has_y():
    assert hasattr(flat11_LabelType, "y")
    descriptor = None
    for klass in flat11_LabelType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_flat11_labeltype_has_value():
    assert hasattr(flat11_LabelType, "value")
    descriptor = None
    for klass in flat11_LabelType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_flat11_labeltype_has_kind():
    assert hasattr(flat11_LabelType, "kind")
    descriptor = None
    for klass in flat11_LabelType.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_flat11_labeltype_has_x():
    assert hasattr(flat11_LabelType, "x")
    descriptor = None
    for klass in flat11_LabelType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_flat11_templatetype_is_not_abstract():
    assert not inspect.isabstract(flat11_TemplateType)


def test_flat11_templatetype_constructor_exists():
    assert callable(flat11_TemplateType.__init__)


def test_flat11_templatetype_constructor_args():
    sig = inspect.signature(flat11_TemplateType.__init__)
    params = list(sig.parameters.keys())
    assert "declaration" in params, "Missing parameter 'declaration'"

def test_flat11_templatetype_has_declaration():
    assert hasattr(flat11_TemplateType, "declaration")
    descriptor = None
    for klass in flat11_TemplateType.__mro__:
        if "declaration" in klass.__dict__:
            descriptor = klass.__dict__["declaration"]
            break
    assert isinstance(descriptor, property)



def test_flat11_targettype_is_not_abstract():
    assert not inspect.isabstract(flat11_TargetType)


def test_flat11_targettype_constructor_exists():
    assert callable(flat11_TargetType.__init__)


def test_flat11_targettype_constructor_args():
    sig = inspect.signature(flat11_TargetType.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"

def test_flat11_targettype_has_ref():
    assert hasattr(flat11_TargetType, "ref")
    descriptor = None
    for klass in flat11_TargetType.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_flat11_sourcetype_is_not_abstract():
    assert not inspect.isabstract(flat11_SourceType)


def test_flat11_sourcetype_constructor_exists():
    assert callable(flat11_SourceType.__init__)


def test_flat11_sourcetype_constructor_args():
    sig = inspect.signature(flat11_SourceType.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"

def test_flat11_sourcetype_has_ref():
    assert hasattr(flat11_SourceType, "ref")
    descriptor = None
    for klass in flat11_SourceType.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_flat11_parametertype_is_not_abstract():
    assert not inspect.isabstract(flat11_ParameterType)


def test_flat11_parametertype_constructor_exists():
    assert callable(flat11_ParameterType.__init__)


def test_flat11_parametertype_constructor_args():
    sig = inspect.signature(flat11_ParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_flat11_parametertype_has_value():
    assert hasattr(flat11_ParameterType, "value")
    descriptor = None
    for klass in flat11_ParameterType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_flat11_parametertype_has_y():
    assert hasattr(flat11_ParameterType, "y")
    descriptor = None
    for klass in flat11_ParameterType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_flat11_parametertype_has_x():
    assert hasattr(flat11_ParameterType, "x")
    descriptor = None
    for klass in flat11_ParameterType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_flat11_ntatype_is_not_abstract():
    assert not inspect.isabstract(flat11_NtaType)


def test_flat11_ntatype_constructor_exists():
    assert callable(flat11_NtaType.__init__)


def test_flat11_ntatype_constructor_args():
    sig = inspect.signature(flat11_NtaType.__init__)
    params = list(sig.parameters.keys())
    assert "instantiation" in params, "Missing parameter 'instantiation'"
    assert "imports" in params, "Missing parameter 'imports'"
    assert "system" in params, "Missing parameter 'system'"
    assert "declaration" in params, "Missing parameter 'declaration'"

def test_flat11_ntatype_has_instantiation():
    assert hasattr(flat11_NtaType, "instantiation")
    descriptor = None
    for klass in flat11_NtaType.__mro__:
        if "instantiation" in klass.__dict__:
            descriptor = klass.__dict__["instantiation"]
            break
    assert isinstance(descriptor, property)

def test_flat11_ntatype_has_imports():
    assert hasattr(flat11_NtaType, "imports")
    descriptor = None
    for klass in flat11_NtaType.__mro__:
        if "imports" in klass.__dict__:
            descriptor = klass.__dict__["imports"]
            break
    assert isinstance(descriptor, property)

def test_flat11_ntatype_has_system():
    assert hasattr(flat11_NtaType, "system")
    descriptor = None
    for klass in flat11_NtaType.__mro__:
        if "system" in klass.__dict__:
            descriptor = klass.__dict__["system"]
            break
    assert isinstance(descriptor, property)

def test_flat11_ntatype_has_declaration():
    assert hasattr(flat11_NtaType, "declaration")
    descriptor = None
    for klass in flat11_NtaType.__mro__:
        if "declaration" in klass.__dict__:
            descriptor = klass.__dict__["declaration"]
            break
    assert isinstance(descriptor, property)



def test_flat11_nametype_is_not_abstract():
    assert not inspect.isabstract(flat11_NameType)


def test_flat11_nametype_constructor_exists():
    assert callable(flat11_NameType.__init__)


def test_flat11_nametype_constructor_args():
    sig = inspect.signature(flat11_NameType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_flat11_nametype_has_value():
    assert hasattr(flat11_NameType, "value")
    descriptor = None
    for klass in flat11_NameType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_flat11_nametype_has_x():
    assert hasattr(flat11_NameType, "x")
    descriptor = None
    for klass in flat11_NameType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_flat11_nametype_has_y():
    assert hasattr(flat11_NameType, "y")
    descriptor = None
    for klass in flat11_NameType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_flat11_nailtype_is_not_abstract():
    assert not inspect.isabstract(flat11_NailType)


def test_flat11_nailtype_constructor_exists():
    assert callable(flat11_NailType.__init__)


def test_flat11_nailtype_constructor_args():
    sig = inspect.signature(flat11_NailType.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_flat11_nailtype_has_y():
    assert hasattr(flat11_NailType, "y")
    descriptor = None
    for klass in flat11_NailType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_flat11_nailtype_has_x():
    assert hasattr(flat11_NailType, "x")
    descriptor = None
    for klass in flat11_NailType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_flat11_locationtype_is_not_abstract():
    assert not inspect.isabstract(flat11_LocationType)


def test_flat11_locationtype_constructor_exists():
    assert callable(flat11_LocationType.__init__)


def test_flat11_locationtype_constructor_args():
    sig = inspect.signature(flat11_LocationType.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "id" in params, "Missing parameter 'id'"
    assert "y" in params, "Missing parameter 'y'"
    assert "color" in params, "Missing parameter 'color'"

def test_flat11_locationtype_has_x():
    assert hasattr(flat11_LocationType, "x")
    descriptor = None
    for klass in flat11_LocationType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_flat11_locationtype_has_id():
    assert hasattr(flat11_LocationType, "id")
    descriptor = None
    for klass in flat11_LocationType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_flat11_locationtype_has_y():
    assert hasattr(flat11_LocationType, "y")
    descriptor = None
    for klass in flat11_LocationType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_flat11_locationtype_has_color():
    assert hasattr(flat11_LocationType, "color")
    descriptor = None
    for klass in flat11_LocationType.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_flat11_inittype_is_not_abstract():
    assert not inspect.isabstract(flat11_InitType)


def test_flat11_inittype_constructor_exists():
    assert callable(flat11_InitType.__init__)


def test_flat11_inittype_constructor_args():
    sig = inspect.signature(flat11_InitType.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"

def test_flat11_inittype_has_ref():
    assert hasattr(flat11_InitType, "ref")
    descriptor = None
    for klass in flat11_InitType.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_flat11_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(flat11_EStringToStringMapEntry)


def test_flat11_estringtostringmapentry_constructor_exists():
    assert callable(flat11_EStringToStringMapEntry.__init__)


def test_flat11_estringtostringmapentry_constructor_args():
    sig = inspect.signature(flat11_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_flat11_documentroot_is_not_abstract():
    assert not inspect.isabstract(flat11_DocumentRoot)


def test_flat11_documentroot_constructor_exists():
    assert callable(flat11_DocumentRoot.__init__)


def test_flat11_documentroot_constructor_args():
    sig = inspect.signature(flat11_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "system" in params, "Missing parameter 'system'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "imports" in params, "Missing parameter 'imports'"
    assert "instantiation" in params, "Missing parameter 'instantiation'"
    assert "declaration" in params, "Missing parameter 'declaration'"

def test_flat11_documentroot_has_system():
    assert hasattr(flat11_DocumentRoot, "system")
    descriptor = None
    for klass in flat11_DocumentRoot.__mro__:
        if "system" in klass.__dict__:
            descriptor = klass.__dict__["system"]
            break
    assert isinstance(descriptor, property)

def test_flat11_documentroot_has_mixed():
    assert hasattr(flat11_DocumentRoot, "mixed")
    descriptor = None
    for klass in flat11_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_flat11_documentroot_has_imports():
    assert hasattr(flat11_DocumentRoot, "imports")
    descriptor = None
    for klass in flat11_DocumentRoot.__mro__:
        if "imports" in klass.__dict__:
            descriptor = klass.__dict__["imports"]
            break
    assert isinstance(descriptor, property)

def test_flat11_documentroot_has_instantiation():
    assert hasattr(flat11_DocumentRoot, "instantiation")
    descriptor = None
    for klass in flat11_DocumentRoot.__mro__:
        if "instantiation" in klass.__dict__:
            descriptor = klass.__dict__["instantiation"]
            break
    assert isinstance(descriptor, property)

def test_flat11_documentroot_has_declaration():
    assert hasattr(flat11_DocumentRoot, "declaration")
    descriptor = None
    for klass in flat11_DocumentRoot.__mro__:
        if "declaration" in klass.__dict__:
            descriptor = klass.__dict__["declaration"]
            break
    assert isinstance(descriptor, property)



def test_flat11_committedtype_is_not_abstract():
    assert not inspect.isabstract(flat11_CommittedType)


def test_flat11_committedtype_constructor_exists():
    assert callable(flat11_CommittedType.__init__)


def test_flat11_committedtype_constructor_args():
    sig = inspect.signature(flat11_CommittedType.__init__)
    params = list(sig.parameters.keys())

def test_kindtype_exists():
    # Check that the Enumeration exists
    assert KindType is not None

def test_kindtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in KindType]
    expected_literals = [
        "select",
        "guard",
        "invariant",
        "synchronisation",
        "assignment",
        "comments",
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
flat11_UrgentType_strategy = st.builds(
    flat11_UrgentType,
)
flat11_TransitionType_strategy = st.builds(
    flat11_TransitionType,
    color=
        safe_text,
    x=
        safe_text,
    y=
        safe_text,
    controllable=
        safe_text,
    action=
        safe_text,
    id=
        safe_text
)
flat11_LabelType_strategy = st.builds(
    flat11_LabelType,
    y=
        safe_text,
    value=
        safe_text,
    kind=
        safe_text,
    x=
        safe_text
)
flat11_TemplateType_strategy = st.builds(
    flat11_TemplateType,
    declaration=
        safe_text
)
flat11_TargetType_strategy = st.builds(
    flat11_TargetType,
    ref=
        safe_text
)
flat11_SourceType_strategy = st.builds(
    flat11_SourceType,
    ref=
        safe_text
)
flat11_ParameterType_strategy = st.builds(
    flat11_ParameterType,
    value=
        safe_text,
    y=
        safe_text,
    x=
        safe_text
)
flat11_NtaType_strategy = st.builds(
    flat11_NtaType,
    instantiation=
        safe_text,
    imports=
        safe_text,
    system=
        safe_text,
    declaration=
        safe_text
)
flat11_NameType_strategy = st.builds(
    flat11_NameType,
    value=
        safe_text,
    x=
        safe_text,
    y=
        safe_text
)
flat11_NailType_strategy = st.builds(
    flat11_NailType,
    y=
        safe_text,
    x=
        safe_text
)
flat11_LocationType_strategy = st.builds(
    flat11_LocationType,
    x=
        safe_text,
    id=
        safe_text,
    y=
        safe_text,
    color=
        safe_text
)
flat11_InitType_strategy = st.builds(
    flat11_InitType,
    ref=
        safe_text
)
flat11_EStringToStringMapEntry_strategy = st.builds(
    flat11_EStringToStringMapEntry,
)
flat11_DocumentRoot_strategy = st.builds(
    flat11_DocumentRoot,
    system=
        safe_text,
    mixed=
        safe_text,
    imports=
        safe_text,
    instantiation=
        safe_text,
    declaration=
        safe_text
)
flat11_CommittedType_strategy = st.builds(
    flat11_CommittedType,
)

@given(instance=flat11_UrgentType_strategy)
@settings(max_examples=50)
def test_flat11_urgenttype_instantiation(instance):
    assert isinstance(instance, flat11_UrgentType)

@given(instance=flat11_TransitionType_strategy)
@settings(max_examples=50)
def test_flat11_transitiontype_instantiation(instance):
    assert isinstance(instance, flat11_TransitionType)



@given(instance=flat11_TransitionType_strategy)
def test_flat11_transitiontype_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=flat11_TransitionType_strategy)
def test_flat11_transitiontype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=flat11_TransitionType_strategy)
def test_flat11_transitiontype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=flat11_TransitionType_strategy)
def test_flat11_transitiontype_controllable_setter(instance):
    original = instance.controllable
    instance.controllable = original
    assert instance.controllable == original



@given(instance=flat11_TransitionType_strategy)
def test_flat11_transitiontype_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original



@given(instance=flat11_TransitionType_strategy)
def test_flat11_transitiontype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=flat11_LabelType_strategy)
@settings(max_examples=50)
def test_flat11_labeltype_instantiation(instance):
    assert isinstance(instance, flat11_LabelType)



@given(instance=flat11_LabelType_strategy)
def test_flat11_labeltype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=flat11_LabelType_strategy)
def test_flat11_labeltype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=flat11_LabelType_strategy)
def test_flat11_labeltype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=flat11_LabelType_strategy)
def test_flat11_labeltype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=flat11_TemplateType_strategy)
@settings(max_examples=50)
def test_flat11_templatetype_instantiation(instance):
    assert isinstance(instance, flat11_TemplateType)



@given(instance=flat11_TemplateType_strategy)
def test_flat11_templatetype_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original

@given(instance=flat11_TargetType_strategy)
@settings(max_examples=50)
def test_flat11_targettype_instantiation(instance):
    assert isinstance(instance, flat11_TargetType)



@given(instance=flat11_TargetType_strategy)
def test_flat11_targettype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=flat11_SourceType_strategy)
@settings(max_examples=50)
def test_flat11_sourcetype_instantiation(instance):
    assert isinstance(instance, flat11_SourceType)



@given(instance=flat11_SourceType_strategy)
def test_flat11_sourcetype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=flat11_ParameterType_strategy)
@settings(max_examples=50)
def test_flat11_parametertype_instantiation(instance):
    assert isinstance(instance, flat11_ParameterType)



@given(instance=flat11_ParameterType_strategy)
def test_flat11_parametertype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=flat11_ParameterType_strategy)
def test_flat11_parametertype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=flat11_ParameterType_strategy)
def test_flat11_parametertype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=flat11_NtaType_strategy)
@settings(max_examples=50)
def test_flat11_ntatype_instantiation(instance):
    assert isinstance(instance, flat11_NtaType)



@given(instance=flat11_NtaType_strategy)
def test_flat11_ntatype_instantiation_setter(instance):
    original = instance.instantiation
    instance.instantiation = original
    assert instance.instantiation == original



@given(instance=flat11_NtaType_strategy)
def test_flat11_ntatype_imports_setter(instance):
    original = instance.imports
    instance.imports = original
    assert instance.imports == original



@given(instance=flat11_NtaType_strategy)
def test_flat11_ntatype_system_setter(instance):
    original = instance.system
    instance.system = original
    assert instance.system == original



@given(instance=flat11_NtaType_strategy)
def test_flat11_ntatype_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original

@given(instance=flat11_NameType_strategy)
@settings(max_examples=50)
def test_flat11_nametype_instantiation(instance):
    assert isinstance(instance, flat11_NameType)



@given(instance=flat11_NameType_strategy)
def test_flat11_nametype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=flat11_NameType_strategy)
def test_flat11_nametype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=flat11_NameType_strategy)
def test_flat11_nametype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=flat11_NailType_strategy)
@settings(max_examples=50)
def test_flat11_nailtype_instantiation(instance):
    assert isinstance(instance, flat11_NailType)



@given(instance=flat11_NailType_strategy)
def test_flat11_nailtype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=flat11_NailType_strategy)
def test_flat11_nailtype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=flat11_LocationType_strategy)
@settings(max_examples=50)
def test_flat11_locationtype_instantiation(instance):
    assert isinstance(instance, flat11_LocationType)



@given(instance=flat11_LocationType_strategy)
def test_flat11_locationtype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=flat11_LocationType_strategy)
def test_flat11_locationtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=flat11_LocationType_strategy)
def test_flat11_locationtype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=flat11_LocationType_strategy)
def test_flat11_locationtype_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=flat11_InitType_strategy)
@settings(max_examples=50)
def test_flat11_inittype_instantiation(instance):
    assert isinstance(instance, flat11_InitType)



@given(instance=flat11_InitType_strategy)
def test_flat11_inittype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=flat11_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_flat11_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, flat11_EStringToStringMapEntry)

@given(instance=flat11_DocumentRoot_strategy)
@settings(max_examples=50)
def test_flat11_documentroot_instantiation(instance):
    assert isinstance(instance, flat11_DocumentRoot)



@given(instance=flat11_DocumentRoot_strategy)
def test_flat11_documentroot_system_setter(instance):
    original = instance.system
    instance.system = original
    assert instance.system == original



@given(instance=flat11_DocumentRoot_strategy)
def test_flat11_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=flat11_DocumentRoot_strategy)
def test_flat11_documentroot_imports_setter(instance):
    original = instance.imports
    instance.imports = original
    assert instance.imports == original



@given(instance=flat11_DocumentRoot_strategy)
def test_flat11_documentroot_instantiation_setter(instance):
    original = instance.instantiation
    instance.instantiation = original
    assert instance.instantiation == original



@given(instance=flat11_DocumentRoot_strategy)
def test_flat11_documentroot_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original

@given(instance=flat11_CommittedType_strategy)
@settings(max_examples=50)
def test_flat11_committedtype_instantiation(instance):
    assert isinstance(instance, flat11_CommittedType)
