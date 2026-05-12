import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    uppaal_UrgentType,
    uppaal_TransitionType,
    uppaal_TemplateType,
    uppaal_LocationType,
    uppaal_TargetType,
    uppaal_SourceType,
    uppaal_ParameterType,
    uppaal_NtaType,
    uppaal_NameType,
    uppaal_NailType,
    uppaal_DocumentRoot,
    uppaal_CommittedType,
    uppaal_LabelType,
    uppaal_InitType,
    uppaal_EStringToStringMapEntry,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uppaal_urgenttype_is_not_abstract():
    assert not inspect.isabstract(uppaal_UrgentType)


def test_uppaal_urgenttype_constructor_exists():
    assert callable(uppaal_UrgentType.__init__)


def test_uppaal_urgenttype_constructor_args():
    sig = inspect.signature(uppaal_UrgentType.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_transitiontype_is_not_abstract():
    assert not inspect.isabstract(uppaal_TransitionType)


def test_uppaal_transitiontype_constructor_exists():
    assert callable(uppaal_TransitionType.__init__)


def test_uppaal_transitiontype_constructor_args():
    sig = inspect.signature(uppaal_TransitionType.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "id" in params, "Missing parameter 'id'"
    assert "x" in params, "Missing parameter 'x'"
    assert "color" in params, "Missing parameter 'color'"

def test_uppaal_transitiontype_has_y():
    assert hasattr(uppaal_TransitionType, "y")
    descriptor = None
    for klass in uppaal_TransitionType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_transitiontype_has_id():
    assert hasattr(uppaal_TransitionType, "id")
    descriptor = None
    for klass in uppaal_TransitionType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_transitiontype_has_x():
    assert hasattr(uppaal_TransitionType, "x")
    descriptor = None
    for klass in uppaal_TransitionType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_transitiontype_has_color():
    assert hasattr(uppaal_TransitionType, "color")
    descriptor = None
    for klass in uppaal_TransitionType.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_templatetype_is_not_abstract():
    assert not inspect.isabstract(uppaal_TemplateType)


def test_uppaal_templatetype_constructor_exists():
    assert callable(uppaal_TemplateType.__init__)


def test_uppaal_templatetype_constructor_args():
    sig = inspect.signature(uppaal_TemplateType.__init__)
    params = list(sig.parameters.keys())
    assert "declaration" in params, "Missing parameter 'declaration'"

def test_uppaal_templatetype_has_declaration():
    assert hasattr(uppaal_TemplateType, "declaration")
    descriptor = None
    for klass in uppaal_TemplateType.__mro__:
        if "declaration" in klass.__dict__:
            descriptor = klass.__dict__["declaration"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_locationtype_is_not_abstract():
    assert not inspect.isabstract(uppaal_LocationType)


def test_uppaal_locationtype_constructor_exists():
    assert callable(uppaal_LocationType.__init__)


def test_uppaal_locationtype_constructor_args():
    sig = inspect.signature(uppaal_LocationType.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "id" in params, "Missing parameter 'id'"
    assert "color" in params, "Missing parameter 'color'"
    assert "x" in params, "Missing parameter 'x'"

def test_uppaal_locationtype_has_y():
    assert hasattr(uppaal_LocationType, "y")
    descriptor = None
    for klass in uppaal_LocationType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_locationtype_has_id():
    assert hasattr(uppaal_LocationType, "id")
    descriptor = None
    for klass in uppaal_LocationType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_locationtype_has_color():
    assert hasattr(uppaal_LocationType, "color")
    descriptor = None
    for klass in uppaal_LocationType.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_locationtype_has_x():
    assert hasattr(uppaal_LocationType, "x")
    descriptor = None
    for klass in uppaal_LocationType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_targettype_is_not_abstract():
    assert not inspect.isabstract(uppaal_TargetType)


def test_uppaal_targettype_constructor_exists():
    assert callable(uppaal_TargetType.__init__)


def test_uppaal_targettype_constructor_args():
    sig = inspect.signature(uppaal_TargetType.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"

def test_uppaal_targettype_has_ref():
    assert hasattr(uppaal_TargetType, "ref")
    descriptor = None
    for klass in uppaal_TargetType.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_sourcetype_is_not_abstract():
    assert not inspect.isabstract(uppaal_SourceType)


def test_uppaal_sourcetype_constructor_exists():
    assert callable(uppaal_SourceType.__init__)


def test_uppaal_sourcetype_constructor_args():
    sig = inspect.signature(uppaal_SourceType.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"

def test_uppaal_sourcetype_has_ref():
    assert hasattr(uppaal_SourceType, "ref")
    descriptor = None
    for klass in uppaal_SourceType.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_parametertype_is_not_abstract():
    assert not inspect.isabstract(uppaal_ParameterType)


def test_uppaal_parametertype_constructor_exists():
    assert callable(uppaal_ParameterType.__init__)


def test_uppaal_parametertype_constructor_args():
    sig = inspect.signature(uppaal_ParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_uppaal_parametertype_has_y():
    assert hasattr(uppaal_ParameterType, "y")
    descriptor = None
    for klass in uppaal_ParameterType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_parametertype_has_x():
    assert hasattr(uppaal_ParameterType, "x")
    descriptor = None
    for klass in uppaal_ParameterType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_parametertype_has_mixed():
    assert hasattr(uppaal_ParameterType, "mixed")
    descriptor = None
    for klass in uppaal_ParameterType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_ntatype_is_not_abstract():
    assert not inspect.isabstract(uppaal_NtaType)


def test_uppaal_ntatype_constructor_exists():
    assert callable(uppaal_NtaType.__init__)


def test_uppaal_ntatype_constructor_args():
    sig = inspect.signature(uppaal_NtaType.__init__)
    params = list(sig.parameters.keys())
    assert "declaration" in params, "Missing parameter 'declaration'"
    assert "system" in params, "Missing parameter 'system'"
    assert "instantiation" in params, "Missing parameter 'instantiation'"
    assert "imports" in params, "Missing parameter 'imports'"

def test_uppaal_ntatype_has_declaration():
    assert hasattr(uppaal_NtaType, "declaration")
    descriptor = None
    for klass in uppaal_NtaType.__mro__:
        if "declaration" in klass.__dict__:
            descriptor = klass.__dict__["declaration"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_ntatype_has_system():
    assert hasattr(uppaal_NtaType, "system")
    descriptor = None
    for klass in uppaal_NtaType.__mro__:
        if "system" in klass.__dict__:
            descriptor = klass.__dict__["system"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_ntatype_has_instantiation():
    assert hasattr(uppaal_NtaType, "instantiation")
    descriptor = None
    for klass in uppaal_NtaType.__mro__:
        if "instantiation" in klass.__dict__:
            descriptor = klass.__dict__["instantiation"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_ntatype_has_imports():
    assert hasattr(uppaal_NtaType, "imports")
    descriptor = None
    for klass in uppaal_NtaType.__mro__:
        if "imports" in klass.__dict__:
            descriptor = klass.__dict__["imports"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_nametype_is_not_abstract():
    assert not inspect.isabstract(uppaal_NameType)


def test_uppaal_nametype_constructor_exists():
    assert callable(uppaal_NameType.__init__)


def test_uppaal_nametype_constructor_args():
    sig = inspect.signature(uppaal_NameType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_uppaal_nametype_has_mixed():
    assert hasattr(uppaal_NameType, "mixed")
    descriptor = None
    for klass in uppaal_NameType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_nametype_has_y():
    assert hasattr(uppaal_NameType, "y")
    descriptor = None
    for klass in uppaal_NameType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_nametype_has_x():
    assert hasattr(uppaal_NameType, "x")
    descriptor = None
    for klass in uppaal_NameType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_nailtype_is_not_abstract():
    assert not inspect.isabstract(uppaal_NailType)


def test_uppaal_nailtype_constructor_exists():
    assert callable(uppaal_NailType.__init__)


def test_uppaal_nailtype_constructor_args():
    sig = inspect.signature(uppaal_NailType.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_uppaal_nailtype_has_x():
    assert hasattr(uppaal_NailType, "x")
    descriptor = None
    for klass in uppaal_NailType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_nailtype_has_y():
    assert hasattr(uppaal_NailType, "y")
    descriptor = None
    for klass in uppaal_NailType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_documentroot_is_not_abstract():
    assert not inspect.isabstract(uppaal_DocumentRoot)


def test_uppaal_documentroot_constructor_exists():
    assert callable(uppaal_DocumentRoot.__init__)


def test_uppaal_documentroot_constructor_args():
    sig = inspect.signature(uppaal_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "instantiation" in params, "Missing parameter 'instantiation'"
    assert "imports" in params, "Missing parameter 'imports'"
    assert "declaration" in params, "Missing parameter 'declaration'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "system" in params, "Missing parameter 'system'"

def test_uppaal_documentroot_has_instantiation():
    assert hasattr(uppaal_DocumentRoot, "instantiation")
    descriptor = None
    for klass in uppaal_DocumentRoot.__mro__:
        if "instantiation" in klass.__dict__:
            descriptor = klass.__dict__["instantiation"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_documentroot_has_imports():
    assert hasattr(uppaal_DocumentRoot, "imports")
    descriptor = None
    for klass in uppaal_DocumentRoot.__mro__:
        if "imports" in klass.__dict__:
            descriptor = klass.__dict__["imports"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_documentroot_has_declaration():
    assert hasattr(uppaal_DocumentRoot, "declaration")
    descriptor = None
    for klass in uppaal_DocumentRoot.__mro__:
        if "declaration" in klass.__dict__:
            descriptor = klass.__dict__["declaration"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_documentroot_has_mixed():
    assert hasattr(uppaal_DocumentRoot, "mixed")
    descriptor = None
    for klass in uppaal_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_documentroot_has_system():
    assert hasattr(uppaal_DocumentRoot, "system")
    descriptor = None
    for klass in uppaal_DocumentRoot.__mro__:
        if "system" in klass.__dict__:
            descriptor = klass.__dict__["system"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_committedtype_is_not_abstract():
    assert not inspect.isabstract(uppaal_CommittedType)


def test_uppaal_committedtype_constructor_exists():
    assert callable(uppaal_CommittedType.__init__)


def test_uppaal_committedtype_constructor_args():
    sig = inspect.signature(uppaal_CommittedType.__init__)
    params = list(sig.parameters.keys())



def test_uppaal_labeltype_is_not_abstract():
    assert not inspect.isabstract(uppaal_LabelType)


def test_uppaal_labeltype_constructor_exists():
    assert callable(uppaal_LabelType.__init__)


def test_uppaal_labeltype_constructor_args():
    sig = inspect.signature(uppaal_LabelType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_uppaal_labeltype_has_mixed():
    assert hasattr(uppaal_LabelType, "mixed")
    descriptor = None
    for klass in uppaal_LabelType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_labeltype_has_x():
    assert hasattr(uppaal_LabelType, "x")
    descriptor = None
    for klass in uppaal_LabelType.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_labeltype_has_y():
    assert hasattr(uppaal_LabelType, "y")
    descriptor = None
    for klass in uppaal_LabelType.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_uppaal_labeltype_has_kind():
    assert hasattr(uppaal_LabelType, "kind")
    descriptor = None
    for klass in uppaal_LabelType.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_inittype_is_not_abstract():
    assert not inspect.isabstract(uppaal_InitType)


def test_uppaal_inittype_constructor_exists():
    assert callable(uppaal_InitType.__init__)


def test_uppaal_inittype_constructor_args():
    sig = inspect.signature(uppaal_InitType.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"

def test_uppaal_inittype_has_ref():
    assert hasattr(uppaal_InitType, "ref")
    descriptor = None
    for klass in uppaal_InitType.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_uppaal_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(uppaal_EStringToStringMapEntry)


def test_uppaal_estringtostringmapentry_constructor_exists():
    assert callable(uppaal_EStringToStringMapEntry.__init__)


def test_uppaal_estringtostringmapentry_constructor_args():
    sig = inspect.signature(uppaal_EStringToStringMapEntry.__init__)
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
uppaal_UrgentType_strategy = st.builds(
    uppaal_UrgentType,
)
uppaal_TransitionType_strategy = st.builds(
    uppaal_TransitionType,
    y=
        safe_text,
    id=
        safe_text,
    x=
        safe_text,
    color=
        safe_text
)
uppaal_TemplateType_strategy = st.builds(
    uppaal_TemplateType,
    declaration=
        safe_text
)
uppaal_LocationType_strategy = st.builds(
    uppaal_LocationType,
    y=
        safe_text,
    id=
        safe_text,
    color=
        safe_text,
    x=
        safe_text
)
uppaal_TargetType_strategy = st.builds(
    uppaal_TargetType,
    ref=
        safe_text
)
uppaal_SourceType_strategy = st.builds(
    uppaal_SourceType,
    ref=
        safe_text
)
uppaal_ParameterType_strategy = st.builds(
    uppaal_ParameterType,
    y=
        safe_text,
    x=
        safe_text,
    mixed=
        safe_text
)
uppaal_NtaType_strategy = st.builds(
    uppaal_NtaType,
    declaration=
        safe_text,
    system=
        safe_text,
    instantiation=
        safe_text,
    imports=
        safe_text
)
uppaal_NameType_strategy = st.builds(
    uppaal_NameType,
    mixed=
        safe_text,
    y=
        safe_text,
    x=
        safe_text
)
uppaal_NailType_strategy = st.builds(
    uppaal_NailType,
    x=
        safe_text,
    y=
        safe_text
)
uppaal_DocumentRoot_strategy = st.builds(
    uppaal_DocumentRoot,
    instantiation=
        safe_text,
    imports=
        safe_text,
    declaration=
        safe_text,
    mixed=
        safe_text,
    system=
        safe_text
)
uppaal_CommittedType_strategy = st.builds(
    uppaal_CommittedType,
)
uppaal_LabelType_strategy = st.builds(
    uppaal_LabelType,
    mixed=
        safe_text,
    x=
        safe_text,
    y=
        safe_text,
    kind=
        safe_text
)
uppaal_InitType_strategy = st.builds(
    uppaal_InitType,
    ref=
        safe_text
)
uppaal_EStringToStringMapEntry_strategy = st.builds(
    uppaal_EStringToStringMapEntry,
)

@given(instance=uppaal_UrgentType_strategy)
@settings(max_examples=50)
def test_uppaal_urgenttype_instantiation(instance):
    assert isinstance(instance, uppaal_UrgentType)

@given(instance=uppaal_TransitionType_strategy)
@settings(max_examples=50)
def test_uppaal_transitiontype_instantiation(instance):
    assert isinstance(instance, uppaal_TransitionType)



@given(instance=uppaal_TransitionType_strategy)
def test_uppaal_transitiontype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=uppaal_TransitionType_strategy)
def test_uppaal_transitiontype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=uppaal_TransitionType_strategy)
def test_uppaal_transitiontype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=uppaal_TransitionType_strategy)
def test_uppaal_transitiontype_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=uppaal_TemplateType_strategy)
@settings(max_examples=50)
def test_uppaal_templatetype_instantiation(instance):
    assert isinstance(instance, uppaal_TemplateType)



@given(instance=uppaal_TemplateType_strategy)
def test_uppaal_templatetype_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original

@given(instance=uppaal_LocationType_strategy)
@settings(max_examples=50)
def test_uppaal_locationtype_instantiation(instance):
    assert isinstance(instance, uppaal_LocationType)



@given(instance=uppaal_LocationType_strategy)
def test_uppaal_locationtype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=uppaal_LocationType_strategy)
def test_uppaal_locationtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=uppaal_LocationType_strategy)
def test_uppaal_locationtype_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=uppaal_LocationType_strategy)
def test_uppaal_locationtype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=uppaal_TargetType_strategy)
@settings(max_examples=50)
def test_uppaal_targettype_instantiation(instance):
    assert isinstance(instance, uppaal_TargetType)



@given(instance=uppaal_TargetType_strategy)
def test_uppaal_targettype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=uppaal_SourceType_strategy)
@settings(max_examples=50)
def test_uppaal_sourcetype_instantiation(instance):
    assert isinstance(instance, uppaal_SourceType)



@given(instance=uppaal_SourceType_strategy)
def test_uppaal_sourcetype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=uppaal_ParameterType_strategy)
@settings(max_examples=50)
def test_uppaal_parametertype_instantiation(instance):
    assert isinstance(instance, uppaal_ParameterType)



@given(instance=uppaal_ParameterType_strategy)
def test_uppaal_parametertype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=uppaal_ParameterType_strategy)
def test_uppaal_parametertype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=uppaal_ParameterType_strategy)
def test_uppaal_parametertype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=uppaal_NtaType_strategy)
@settings(max_examples=50)
def test_uppaal_ntatype_instantiation(instance):
    assert isinstance(instance, uppaal_NtaType)



@given(instance=uppaal_NtaType_strategy)
def test_uppaal_ntatype_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original



@given(instance=uppaal_NtaType_strategy)
def test_uppaal_ntatype_system_setter(instance):
    original = instance.system
    instance.system = original
    assert instance.system == original



@given(instance=uppaal_NtaType_strategy)
def test_uppaal_ntatype_instantiation_setter(instance):
    original = instance.instantiation
    instance.instantiation = original
    assert instance.instantiation == original



@given(instance=uppaal_NtaType_strategy)
def test_uppaal_ntatype_imports_setter(instance):
    original = instance.imports
    instance.imports = original
    assert instance.imports == original

@given(instance=uppaal_NameType_strategy)
@settings(max_examples=50)
def test_uppaal_nametype_instantiation(instance):
    assert isinstance(instance, uppaal_NameType)



@given(instance=uppaal_NameType_strategy)
def test_uppaal_nametype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=uppaal_NameType_strategy)
def test_uppaal_nametype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=uppaal_NameType_strategy)
def test_uppaal_nametype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=uppaal_NailType_strategy)
@settings(max_examples=50)
def test_uppaal_nailtype_instantiation(instance):
    assert isinstance(instance, uppaal_NailType)



@given(instance=uppaal_NailType_strategy)
def test_uppaal_nailtype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=uppaal_NailType_strategy)
def test_uppaal_nailtype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=uppaal_DocumentRoot_strategy)
@settings(max_examples=50)
def test_uppaal_documentroot_instantiation(instance):
    assert isinstance(instance, uppaal_DocumentRoot)



@given(instance=uppaal_DocumentRoot_strategy)
def test_uppaal_documentroot_instantiation_setter(instance):
    original = instance.instantiation
    instance.instantiation = original
    assert instance.instantiation == original



@given(instance=uppaal_DocumentRoot_strategy)
def test_uppaal_documentroot_imports_setter(instance):
    original = instance.imports
    instance.imports = original
    assert instance.imports == original



@given(instance=uppaal_DocumentRoot_strategy)
def test_uppaal_documentroot_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original



@given(instance=uppaal_DocumentRoot_strategy)
def test_uppaal_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=uppaal_DocumentRoot_strategy)
def test_uppaal_documentroot_system_setter(instance):
    original = instance.system
    instance.system = original
    assert instance.system == original

@given(instance=uppaal_CommittedType_strategy)
@settings(max_examples=50)
def test_uppaal_committedtype_instantiation(instance):
    assert isinstance(instance, uppaal_CommittedType)

@given(instance=uppaal_LabelType_strategy)
@settings(max_examples=50)
def test_uppaal_labeltype_instantiation(instance):
    assert isinstance(instance, uppaal_LabelType)



@given(instance=uppaal_LabelType_strategy)
def test_uppaal_labeltype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=uppaal_LabelType_strategy)
def test_uppaal_labeltype_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=uppaal_LabelType_strategy)
def test_uppaal_labeltype_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=uppaal_LabelType_strategy)
def test_uppaal_labeltype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=uppaal_InitType_strategy)
@settings(max_examples=50)
def test_uppaal_inittype_instantiation(instance):
    assert isinstance(instance, uppaal_InitType)



@given(instance=uppaal_InitType_strategy)
def test_uppaal_inittype_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=uppaal_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_uppaal_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, uppaal_EStringToStringMapEntry)
