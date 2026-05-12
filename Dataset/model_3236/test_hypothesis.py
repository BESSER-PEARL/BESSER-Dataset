import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    UppaalFlat11_UrgentType,
    UppaalFlat11_TargetType,
    UppaalFlat11_SourceType,
    UppaalFlat11_ParameterType,
    UppaalFlat11_EStringToStringMapEntry,
    UppaalFlat11_NtaType,
    UppaalFlat11_NameType,
    UppaalFlat11_NailType,
    UppaalFlat11_LocationType,
    UppaalFlat11_LabelType,
    UppaalFlat11_TransitionType,
    UppaalFlat11_InitType,
    UppaalFlat11_TemplateType,
    UppaalFlat11_DocumentRoot,
    UppaalFlat11_CommittedType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uppaalflat11_urgenttype_is_not_abstract():
    assert not inspect.isabstract(UppaalFlat11_UrgentType)


def test_uppaalflat11_urgenttype_constructor_exists():
    assert callable(UppaalFlat11_UrgentType.__init__)


def test_uppaalflat11_urgenttype_constructor_args():
    sig = inspect.signature(UppaalFlat11_UrgentType.__init__)
    params = list(sig.parameters.keys())



def test_uppaalflat11_targettype_is_not_abstract():
    assert not inspect.isabstract(UppaalFlat11_TargetType)


def test_uppaalflat11_targettype_constructor_exists():
    assert callable(UppaalFlat11_TargetType.__init__)


def test_uppaalflat11_targettype_constructor_args():
    sig = inspect.signature(UppaalFlat11_TargetType.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"

def test_uppaalflat11_targettype_has_ref():
    assert hasattr(UppaalFlat11_TargetType, "ref")
    descriptor = None
    for klass in UppaalFlat11_TargetType.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_uppaalflat11_sourcetype_is_not_abstract():
    assert not inspect.isabstract(UppaalFlat11_SourceType)


def test_uppaalflat11_sourcetype_constructor_exists():
    assert callable(UppaalFlat11_SourceType.__init__)


def test_uppaalflat11_sourcetype_constructor_args():
    sig = inspect.signature(UppaalFlat11_SourceType.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"

def test_uppaalflat11_sourcetype_has_ref():
    assert hasattr(UppaalFlat11_SourceType, "ref")
    descriptor = None
    for klass in UppaalFlat11_SourceType.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_uppaalflat11_parametertype_is_not_abstract():
    assert not inspect.isabstract(UppaalFlat11_ParameterType)


def test_uppaalflat11_parametertype_constructor_exists():
    assert callable(UppaalFlat11_ParameterType.__init__)


def test_uppaalflat11_parametertype_constructor_args():
    sig = inspect.signature(UppaalFlat11_ParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_uppaalflat11_parametertype_has_mixed():
    assert hasattr(UppaalFlat11_ParameterType, "mixed")
    descriptor = None
    for klass in UppaalFlat11_ParameterType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11_parametertype_has_y():
    assert hasattr(UppaalFlat11_ParameterType, "y")
    descriptor = None
    for klass in UppaalFlat11_ParameterType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11_parametertype_has_x():
    assert hasattr(UppaalFlat11_ParameterType, "x")
    descriptor = None
    for klass in UppaalFlat11_ParameterType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_uppaalflat11_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(UppaalFlat11_EStringToStringMapEntry)


def test_uppaalflat11_estringtostringmapentry_constructor_exists():
    assert callable(UppaalFlat11_EStringToStringMapEntry.__init__)


def test_uppaalflat11_estringtostringmapentry_constructor_args():
    sig = inspect.signature(UppaalFlat11_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_uppaalflat11_ntatype_is_not_abstract():
    assert not inspect.isabstract(UppaalFlat11_NtaType)


def test_uppaalflat11_ntatype_constructor_exists():
    assert callable(UppaalFlat11_NtaType.__init__)


def test_uppaalflat11_ntatype_constructor_args():
    sig = inspect.signature(UppaalFlat11_NtaType.__init__)
    params = list(sig.parameters.keys())
    assert "instantiation" in params, "Missing parameter 'instantiation'"
    assert "imports" in params, "Missing parameter 'imports'"
    assert "declaration" in params, "Missing parameter 'declaration'"
    assert "system" in params, "Missing parameter 'system'"

def test_uppaalflat11_ntatype_has_instantiation():
    assert hasattr(UppaalFlat11_NtaType, "instantiation")
    descriptor = None
    for klass in UppaalFlat11_NtaType.__mro__:
        if "instantiation" in klass.__dict__:
            descriptor = klass.__dict__["instantiation"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11_ntatype_has_imports():
    assert hasattr(UppaalFlat11_NtaType, "imports")
    descriptor = None
    for klass in UppaalFlat11_NtaType.__mro__:
        if "imports" in klass.__dict__:
            descriptor = klass.__dict__["imports"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11_ntatype_has_declaration():
    assert hasattr(UppaalFlat11_NtaType, "declaration")
    descriptor = None
    for klass in UppaalFlat11_NtaType.__mro__:
        if "declaration" in klass.__dict__:
            descriptor = klass.__dict__["declaration"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11_ntatype_has_system():
    assert hasattr(UppaalFlat11_NtaType, "system")
    descriptor = None
    for klass in UppaalFlat11_NtaType.__mro__:
        if "system" in klass.__dict__:
            descriptor = klass.__dict__["system"]
            break
    assert isinstance(descriptor, property)



def test_uppaalflat11_nametype_is_not_abstract():
    assert not inspect.isabstract(UppaalFlat11_NameType)


def test_uppaalflat11_nametype_constructor_exists():
    assert callable(UppaalFlat11_NameType.__init__)


def test_uppaalflat11_nametype_constructor_args():
    sig = inspect.signature(UppaalFlat11_NameType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_uppaalflat11_nametype_has_mixed():
    assert hasattr(UppaalFlat11_NameType, "mixed")
    descriptor = None
    for klass in UppaalFlat11_NameType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11_nametype_has_x():
    assert hasattr(UppaalFlat11_NameType, "x")
    descriptor = None
    for klass in UppaalFlat11_NameType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11_nametype_has_y():
    assert hasattr(UppaalFlat11_NameType, "y")
    descriptor = None
    for klass in UppaalFlat11_NameType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_uppaalflat11_nailtype_is_not_abstract():
    assert not inspect.isabstract(UppaalFlat11_NailType)


def test_uppaalflat11_nailtype_constructor_exists():
    assert callable(UppaalFlat11_NailType.__init__)


def test_uppaalflat11_nailtype_constructor_args():
    sig = inspect.signature(UppaalFlat11_NailType.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_uppaalflat11_nailtype_has_x():
    assert hasattr(UppaalFlat11_NailType, "x")
    descriptor = None
    for klass in UppaalFlat11_NailType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11_nailtype_has_y():
    assert hasattr(UppaalFlat11_NailType, "y")
    descriptor = None
    for klass in UppaalFlat11_NailType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_uppaalflat11_locationtype_is_not_abstract():
    assert not inspect.isabstract(UppaalFlat11_LocationType)


def test_uppaalflat11_locationtype_constructor_exists():
    assert callable(UppaalFlat11_LocationType.__init__)


def test_uppaalflat11_locationtype_constructor_args():
    sig = inspect.signature(UppaalFlat11_LocationType.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "id" in params, "Missing parameter 'id'"
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_uppaalflat11_locationtype_has_color():
    assert hasattr(UppaalFlat11_LocationType, "color")
    descriptor = None
    for klass in UppaalFlat11_LocationType.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11_locationtype_has_id():
    assert hasattr(UppaalFlat11_LocationType, "id")
    descriptor = None
    for klass in UppaalFlat11_LocationType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11_locationtype_has_x():
    assert hasattr(UppaalFlat11_LocationType, "x")
    descriptor = None
    for klass in UppaalFlat11_LocationType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11_locationtype_has_y():
    assert hasattr(UppaalFlat11_LocationType, "y")
    descriptor = None
    for klass in UppaalFlat11_LocationType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_uppaalflat11_labeltype_is_not_abstract():
    assert not inspect.isabstract(UppaalFlat11_LabelType)


def test_uppaalflat11_labeltype_constructor_exists():
    assert callable(UppaalFlat11_LabelType.__init__)


def test_uppaalflat11_labeltype_constructor_args():
    sig = inspect.signature(UppaalFlat11_LabelType.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_uppaalflat11_labeltype_has_x():
    assert hasattr(UppaalFlat11_LabelType, "x")
    descriptor = None
    for klass in UppaalFlat11_LabelType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11_labeltype_has_y():
    assert hasattr(UppaalFlat11_LabelType, "y")
    descriptor = None
    for klass in UppaalFlat11_LabelType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11_labeltype_has_mixed():
    assert hasattr(UppaalFlat11_LabelType, "mixed")
    descriptor = None
    for klass in UppaalFlat11_LabelType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11_labeltype_has_kind():
    assert hasattr(UppaalFlat11_LabelType, "kind")
    descriptor = None
    for klass in UppaalFlat11_LabelType.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_uppaalflat11_transitiontype_is_not_abstract():
    assert not inspect.isabstract(UppaalFlat11_TransitionType)


def test_uppaalflat11_transitiontype_constructor_exists():
    assert callable(UppaalFlat11_TransitionType.__init__)


def test_uppaalflat11_transitiontype_constructor_args():
    sig = inspect.signature(UppaalFlat11_TransitionType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "x" in params, "Missing parameter 'x'"
    assert "color" in params, "Missing parameter 'color'"
    assert "y" in params, "Missing parameter 'y'"

def test_uppaalflat11_transitiontype_has_id():
    assert hasattr(UppaalFlat11_TransitionType, "id")
    descriptor = None
    for klass in UppaalFlat11_TransitionType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11_transitiontype_has_x():
    assert hasattr(UppaalFlat11_TransitionType, "x")
    descriptor = None
    for klass in UppaalFlat11_TransitionType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11_transitiontype_has_color():
    assert hasattr(UppaalFlat11_TransitionType, "color")
    descriptor = None
    for klass in UppaalFlat11_TransitionType.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11_transitiontype_has_y():
    assert hasattr(UppaalFlat11_TransitionType, "y")
    descriptor = None
    for klass in UppaalFlat11_TransitionType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_uppaalflat11_inittype_is_not_abstract():
    assert not inspect.isabstract(UppaalFlat11_InitType)


def test_uppaalflat11_inittype_constructor_exists():
    assert callable(UppaalFlat11_InitType.__init__)


def test_uppaalflat11_inittype_constructor_args():
    sig = inspect.signature(UppaalFlat11_InitType.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"

def test_uppaalflat11_inittype_has_ref():
    assert hasattr(UppaalFlat11_InitType, "ref")
    descriptor = None
    for klass in UppaalFlat11_InitType.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_uppaalflat11_templatetype_is_not_abstract():
    assert not inspect.isabstract(UppaalFlat11_TemplateType)


def test_uppaalflat11_templatetype_constructor_exists():
    assert callable(UppaalFlat11_TemplateType.__init__)


def test_uppaalflat11_templatetype_constructor_args():
    sig = inspect.signature(UppaalFlat11_TemplateType.__init__)
    params = list(sig.parameters.keys())
    assert "declaration" in params, "Missing parameter 'declaration'"

def test_uppaalflat11_templatetype_has_declaration():
    assert hasattr(UppaalFlat11_TemplateType, "declaration")
    descriptor = None
    for klass in UppaalFlat11_TemplateType.__mro__:
        if "declaration" in klass.__dict__:
            descriptor = klass.__dict__["declaration"]
            break
    assert isinstance(descriptor, property)



def test_uppaalflat11_documentroot_is_not_abstract():
    assert not inspect.isabstract(UppaalFlat11_DocumentRoot)


def test_uppaalflat11_documentroot_constructor_exists():
    assert callable(UppaalFlat11_DocumentRoot.__init__)


def test_uppaalflat11_documentroot_constructor_args():
    sig = inspect.signature(UppaalFlat11_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "declaration" in params, "Missing parameter 'declaration'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "imports" in params, "Missing parameter 'imports'"
    assert "system" in params, "Missing parameter 'system'"
    assert "instantiation" in params, "Missing parameter 'instantiation'"

def test_uppaalflat11_documentroot_has_declaration():
    assert hasattr(UppaalFlat11_DocumentRoot, "declaration")
    descriptor = None
    for klass in UppaalFlat11_DocumentRoot.__mro__:
        if "declaration" in klass.__dict__:
            descriptor = klass.__dict__["declaration"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11_documentroot_has_mixed():
    assert hasattr(UppaalFlat11_DocumentRoot, "mixed")
    descriptor = None
    for klass in UppaalFlat11_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11_documentroot_has_imports():
    assert hasattr(UppaalFlat11_DocumentRoot, "imports")
    descriptor = None
    for klass in UppaalFlat11_DocumentRoot.__mro__:
        if "imports" in klass.__dict__:
            descriptor = klass.__dict__["imports"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11_documentroot_has_system():
    assert hasattr(UppaalFlat11_DocumentRoot, "system")
    descriptor = None
    for klass in UppaalFlat11_DocumentRoot.__mro__:
        if "system" in klass.__dict__:
            descriptor = klass.__dict__["system"]
            break
    assert isinstance(descriptor, property)

def test_uppaalflat11_documentroot_has_instantiation():
    assert hasattr(UppaalFlat11_DocumentRoot, "instantiation")
    descriptor = None
    for klass in UppaalFlat11_DocumentRoot.__mro__:
        if "instantiation" in klass.__dict__:
            descriptor = klass.__dict__["instantiation"]
            break
    assert isinstance(descriptor, property)



def test_uppaalflat11_committedtype_is_not_abstract():
    assert not inspect.isabstract(UppaalFlat11_CommittedType)


def test_uppaalflat11_committedtype_constructor_exists():
    assert callable(UppaalFlat11_CommittedType.__init__)


def test_uppaalflat11_committedtype_constructor_args():
    sig = inspect.signature(UppaalFlat11_CommittedType.__init__)
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
UppaalFlat11_UrgentType_strategy = st.builds(
    UppaalFlat11_UrgentType,
)
UppaalFlat11_TargetType_strategy = st.builds(
    UppaalFlat11_TargetType,
    ref=
        safe_text
)
UppaalFlat11_SourceType_strategy = st.builds(
    UppaalFlat11_SourceType,
    ref=
        safe_text
)
UppaalFlat11_ParameterType_strategy = st.builds(
    UppaalFlat11_ParameterType,
    mixed=
        safe_text,
    y=
        safe_text,
    x=
        safe_text
)
UppaalFlat11_EStringToStringMapEntry_strategy = st.builds(
    UppaalFlat11_EStringToStringMapEntry,
)
UppaalFlat11_NtaType_strategy = st.builds(
    UppaalFlat11_NtaType,
    instantiation=
        safe_text,
    imports=
        safe_text,
    declaration=
        safe_text,
    system=
        safe_text
)
UppaalFlat11_NameType_strategy = st.builds(
    UppaalFlat11_NameType,
    mixed=
        safe_text,
    x=
        safe_text,
    y=
        safe_text
)
UppaalFlat11_NailType_strategy = st.builds(
    UppaalFlat11_NailType,
    x=
        safe_text,
    y=
        safe_text
)
UppaalFlat11_LocationType_strategy = st.builds(
    UppaalFlat11_LocationType,
    color=
        safe_text,
    id=
        safe_text,
    x=
        safe_text,
    y=
        safe_text
)
UppaalFlat11_LabelType_strategy = st.builds(
    UppaalFlat11_LabelType,
    x=
        safe_text,
    y=
        safe_text,
    mixed=
        safe_text,
    kind=
        safe_text
)
UppaalFlat11_TransitionType_strategy = st.builds(
    UppaalFlat11_TransitionType,
    id=
        safe_text,
    x=
        safe_text,
    color=
        safe_text,
    y=
        safe_text
)
UppaalFlat11_InitType_strategy = st.builds(
    UppaalFlat11_InitType,
    ref=
        safe_text
)
UppaalFlat11_TemplateType_strategy = st.builds(
    UppaalFlat11_TemplateType,
    declaration=
        safe_text
)
UppaalFlat11_DocumentRoot_strategy = st.builds(
    UppaalFlat11_DocumentRoot,
    declaration=
        safe_text,
    mixed=
        safe_text,
    imports=
        safe_text,
    system=
        safe_text,
    instantiation=
        safe_text
)
UppaalFlat11_CommittedType_strategy = st.builds(
    UppaalFlat11_CommittedType,
)

@given(instance=UppaalFlat11_UrgentType_strategy)
@settings(max_examples=50)
def test_uppaalflat11_urgenttype_instantiation(instance):
    assert isinstance(instance, UppaalFlat11_UrgentType)

@given(instance=UppaalFlat11_TargetType_strategy)
@settings(max_examples=50)
def test_uppaalflat11_targettype_instantiation(instance):
    assert isinstance(instance, UppaalFlat11_TargetType)



@given(instance=UppaalFlat11_TargetType_strategy)
def test_uppaalflat11_targettype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=UppaalFlat11_SourceType_strategy)
@settings(max_examples=50)
def test_uppaalflat11_sourcetype_instantiation(instance):
    assert isinstance(instance, UppaalFlat11_SourceType)



@given(instance=UppaalFlat11_SourceType_strategy)
def test_uppaalflat11_sourcetype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=UppaalFlat11_ParameterType_strategy)
@settings(max_examples=50)
def test_uppaalflat11_parametertype_instantiation(instance):
    assert isinstance(instance, UppaalFlat11_ParameterType)



@given(instance=UppaalFlat11_ParameterType_strategy)
def test_uppaalflat11_parametertype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=UppaalFlat11_ParameterType_strategy)
def test_uppaalflat11_parametertype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=UppaalFlat11_ParameterType_strategy)
def test_uppaalflat11_parametertype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=UppaalFlat11_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_uppaalflat11_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, UppaalFlat11_EStringToStringMapEntry)

@given(instance=UppaalFlat11_NtaType_strategy)
@settings(max_examples=50)
def test_uppaalflat11_ntatype_instantiation(instance):
    assert isinstance(instance, UppaalFlat11_NtaType)



@given(instance=UppaalFlat11_NtaType_strategy)
def test_uppaalflat11_ntatype_instantiation_setter(instance):
    original = instance.instantiation
    instance.instantiation = original
    assert instance.instantiation == original



@given(instance=UppaalFlat11_NtaType_strategy)
def test_uppaalflat11_ntatype_imports_setter(instance):
    original = instance.imports
    instance.imports = original
    assert instance.imports == original



@given(instance=UppaalFlat11_NtaType_strategy)
def test_uppaalflat11_ntatype_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original



@given(instance=UppaalFlat11_NtaType_strategy)
def test_uppaalflat11_ntatype_system_setter(instance):
    original = instance.system
    instance.system = original
    assert instance.system == original

@given(instance=UppaalFlat11_NameType_strategy)
@settings(max_examples=50)
def test_uppaalflat11_nametype_instantiation(instance):
    assert isinstance(instance, UppaalFlat11_NameType)



@given(instance=UppaalFlat11_NameType_strategy)
def test_uppaalflat11_nametype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=UppaalFlat11_NameType_strategy)
def test_uppaalflat11_nametype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=UppaalFlat11_NameType_strategy)
def test_uppaalflat11_nametype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=UppaalFlat11_NailType_strategy)
@settings(max_examples=50)
def test_uppaalflat11_nailtype_instantiation(instance):
    assert isinstance(instance, UppaalFlat11_NailType)



@given(instance=UppaalFlat11_NailType_strategy)
def test_uppaalflat11_nailtype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=UppaalFlat11_NailType_strategy)
def test_uppaalflat11_nailtype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=UppaalFlat11_LocationType_strategy)
@settings(max_examples=50)
def test_uppaalflat11_locationtype_instantiation(instance):
    assert isinstance(instance, UppaalFlat11_LocationType)



@given(instance=UppaalFlat11_LocationType_strategy)
def test_uppaalflat11_locationtype_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=UppaalFlat11_LocationType_strategy)
def test_uppaalflat11_locationtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=UppaalFlat11_LocationType_strategy)
def test_uppaalflat11_locationtype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=UppaalFlat11_LocationType_strategy)
def test_uppaalflat11_locationtype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=UppaalFlat11_LabelType_strategy)
@settings(max_examples=50)
def test_uppaalflat11_labeltype_instantiation(instance):
    assert isinstance(instance, UppaalFlat11_LabelType)



@given(instance=UppaalFlat11_LabelType_strategy)
def test_uppaalflat11_labeltype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=UppaalFlat11_LabelType_strategy)
def test_uppaalflat11_labeltype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=UppaalFlat11_LabelType_strategy)
def test_uppaalflat11_labeltype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=UppaalFlat11_LabelType_strategy)
def test_uppaalflat11_labeltype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=UppaalFlat11_TransitionType_strategy)
@settings(max_examples=50)
def test_uppaalflat11_transitiontype_instantiation(instance):
    assert isinstance(instance, UppaalFlat11_TransitionType)



@given(instance=UppaalFlat11_TransitionType_strategy)
def test_uppaalflat11_transitiontype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=UppaalFlat11_TransitionType_strategy)
def test_uppaalflat11_transitiontype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=UppaalFlat11_TransitionType_strategy)
def test_uppaalflat11_transitiontype_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=UppaalFlat11_TransitionType_strategy)
def test_uppaalflat11_transitiontype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=UppaalFlat11_InitType_strategy)
@settings(max_examples=50)
def test_uppaalflat11_inittype_instantiation(instance):
    assert isinstance(instance, UppaalFlat11_InitType)



@given(instance=UppaalFlat11_InitType_strategy)
def test_uppaalflat11_inittype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=UppaalFlat11_TemplateType_strategy)
@settings(max_examples=50)
def test_uppaalflat11_templatetype_instantiation(instance):
    assert isinstance(instance, UppaalFlat11_TemplateType)



@given(instance=UppaalFlat11_TemplateType_strategy)
def test_uppaalflat11_templatetype_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original

@given(instance=UppaalFlat11_DocumentRoot_strategy)
@settings(max_examples=50)
def test_uppaalflat11_documentroot_instantiation(instance):
    assert isinstance(instance, UppaalFlat11_DocumentRoot)



@given(instance=UppaalFlat11_DocumentRoot_strategy)
def test_uppaalflat11_documentroot_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original



@given(instance=UppaalFlat11_DocumentRoot_strategy)
def test_uppaalflat11_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=UppaalFlat11_DocumentRoot_strategy)
def test_uppaalflat11_documentroot_imports_setter(instance):
    original = instance.imports
    instance.imports = original
    assert instance.imports == original



@given(instance=UppaalFlat11_DocumentRoot_strategy)
def test_uppaalflat11_documentroot_system_setter(instance):
    original = instance.system
    instance.system = original
    assert instance.system == original



@given(instance=UppaalFlat11_DocumentRoot_strategy)
def test_uppaalflat11_documentroot_instantiation_setter(instance):
    original = instance.instantiation
    instance.instantiation = original
    assert instance.instantiation == original

@given(instance=UppaalFlat11_CommittedType_strategy)
@settings(max_examples=50)
def test_uppaalflat11_committedtype_instantiation(instance):
    assert isinstance(instance, UppaalFlat11_CommittedType)
