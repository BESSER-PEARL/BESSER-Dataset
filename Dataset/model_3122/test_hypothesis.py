import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    class::diagramm::RefPackage,
    RefAssociation,
    class::diagramm::Association,
    class::diagramm::RefMethod,
    class::diagramm::RefAttribute,
    RefClass,
    class::diagramm::Class,
    RefPackage,
    RefParameter,
    class::diagramm::Parameter,
    RefAttribute,
    class::diagramm::Attribute,
    class::diagramm::RefDataType,
    class::diagramm::RefParameter,
    RefMethod,
    class::diagramm::Method,
    RefDataType,
    class::diagramm::DataType,
    class::diagramm::RefClass,
    class::diagramm::RefAssociation,
    class::diagramm::Package,
    ModifierType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_class::diagramm::refpackage_is_not_abstract():
    assert not inspect.isabstract(class::diagramm::RefPackage)


def test_class::diagramm::refpackage_constructor_exists():
    assert callable(class::diagramm::RefPackage.__init__)


def test_class::diagramm::refpackage_constructor_args():
    sig = inspect.signature(class::diagramm::RefPackage.__init__)
    params = list(sig.parameters.keys())



def test_refassociation_is_not_abstract():
    assert not inspect.isabstract(RefAssociation)


def test_refassociation_constructor_exists():
    assert callable(RefAssociation.__init__)


def test_refassociation_constructor_args():
    sig = inspect.signature(RefAssociation.__init__)
    params = list(sig.parameters.keys())



def test_class::diagramm::association_is_not_abstract():
    assert not inspect.isabstract(class::diagramm::Association)


def test_class::diagramm::association_constructor_exists():
    assert callable(class::diagramm::Association.__init__)


def test_class::diagramm::association_constructor_args():
    sig = inspect.signature(class::diagramm::Association.__init__)
    params = list(sig.parameters.keys())
    assert "minCardinality" in params, "Missing parameter 'minCardinality'"
    assert "isAggregation" in params, "Missing parameter 'isAggregation'"
    assert "name" in params, "Missing parameter 'name'"
    assert "maxCardinality" in params, "Missing parameter 'maxCardinality'"

def test_class::diagramm::association_has_minCardinality():
    assert hasattr(class::diagramm::Association, "minCardinality")
    descriptor = None
    for klass in class::diagramm::Association.__mro__:
        if "minCardinality" in klass.__dict__:
            descriptor = klass.__dict__["minCardinality"]
            break
    assert isinstance(descriptor, property)

def test_class::diagramm::association_has_isAggregation():
    assert hasattr(class::diagramm::Association, "isAggregation")
    descriptor = None
    for klass in class::diagramm::Association.__mro__:
        if "isAggregation" in klass.__dict__:
            descriptor = klass.__dict__["isAggregation"]
            break
    assert isinstance(descriptor, property)

def test_class::diagramm::association_has_name():
    assert hasattr(class::diagramm::Association, "name")
    descriptor = None
    for klass in class::diagramm::Association.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_class::diagramm::association_has_maxCardinality():
    assert hasattr(class::diagramm::Association, "maxCardinality")
    descriptor = None
    for klass in class::diagramm::Association.__mro__:
        if "maxCardinality" in klass.__dict__:
            descriptor = klass.__dict__["maxCardinality"]
            break
    assert isinstance(descriptor, property)



def test_class::diagramm::refmethod_is_not_abstract():
    assert not inspect.isabstract(class::diagramm::RefMethod)


def test_class::diagramm::refmethod_constructor_exists():
    assert callable(class::diagramm::RefMethod.__init__)


def test_class::diagramm::refmethod_constructor_args():
    sig = inspect.signature(class::diagramm::RefMethod.__init__)
    params = list(sig.parameters.keys())



def test_class::diagramm::refattribute_is_not_abstract():
    assert not inspect.isabstract(class::diagramm::RefAttribute)


def test_class::diagramm::refattribute_constructor_exists():
    assert callable(class::diagramm::RefAttribute.__init__)


def test_class::diagramm::refattribute_constructor_args():
    sig = inspect.signature(class::diagramm::RefAttribute.__init__)
    params = list(sig.parameters.keys())



def test_refclass_is_not_abstract():
    assert not inspect.isabstract(RefClass)


def test_refclass_constructor_exists():
    assert callable(RefClass.__init__)


def test_refclass_constructor_args():
    sig = inspect.signature(RefClass.__init__)
    params = list(sig.parameters.keys())



def test_class::diagramm::class_is_not_abstract():
    assert not inspect.isabstract(class::diagramm::Class)


def test_class::diagramm::class_constructor_exists():
    assert callable(class::diagramm::Class.__init__)


def test_class::diagramm::class_constructor_args():
    sig = inspect.signature(class::diagramm::Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "modifier" in params, "Missing parameter 'modifier'"

def test_class::diagramm::class_has_name():
    assert hasattr(class::diagramm::Class, "name")
    descriptor = None
    for klass in class::diagramm::Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_class::diagramm::class_has_modifier():
    assert hasattr(class::diagramm::Class, "modifier")
    descriptor = None
    for klass in class::diagramm::Class.__mro__:
        if "modifier" in klass.__dict__:
            descriptor = klass.__dict__["modifier"]
            break
    assert isinstance(descriptor, property)



def test_refpackage_is_not_abstract():
    assert not inspect.isabstract(RefPackage)


def test_refpackage_constructor_exists():
    assert callable(RefPackage.__init__)


def test_refpackage_constructor_args():
    sig = inspect.signature(RefPackage.__init__)
    params = list(sig.parameters.keys())



def test_refparameter_is_not_abstract():
    assert not inspect.isabstract(RefParameter)


def test_refparameter_constructor_exists():
    assert callable(RefParameter.__init__)


def test_refparameter_constructor_args():
    sig = inspect.signature(RefParameter.__init__)
    params = list(sig.parameters.keys())



def test_class::diagramm::parameter_is_not_abstract():
    assert not inspect.isabstract(class::diagramm::Parameter)


def test_class::diagramm::parameter_constructor_exists():
    assert callable(class::diagramm::Parameter.__init__)


def test_class::diagramm::parameter_constructor_args():
    sig = inspect.signature(class::diagramm::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_class::diagramm::parameter_has_name():
    assert hasattr(class::diagramm::Parameter, "name")
    descriptor = None
    for klass in class::diagramm::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_refattribute_is_not_abstract():
    assert not inspect.isabstract(RefAttribute)


def test_refattribute_constructor_exists():
    assert callable(RefAttribute.__init__)


def test_refattribute_constructor_args():
    sig = inspect.signature(RefAttribute.__init__)
    params = list(sig.parameters.keys())



def test_class::diagramm::attribute_is_not_abstract():
    assert not inspect.isabstract(class::diagramm::Attribute)


def test_class::diagramm::attribute_constructor_exists():
    assert callable(class::diagramm::Attribute.__init__)


def test_class::diagramm::attribute_constructor_args():
    sig = inspect.signature(class::diagramm::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "modifier" in params, "Missing parameter 'modifier'"
    assert "name" in params, "Missing parameter 'name'"

def test_class::diagramm::attribute_has_modifier():
    assert hasattr(class::diagramm::Attribute, "modifier")
    descriptor = None
    for klass in class::diagramm::Attribute.__mro__:
        if "modifier" in klass.__dict__:
            descriptor = klass.__dict__["modifier"]
            break
    assert isinstance(descriptor, property)

def test_class::diagramm::attribute_has_name():
    assert hasattr(class::diagramm::Attribute, "name")
    descriptor = None
    for klass in class::diagramm::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_class::diagramm::refdatatype_is_not_abstract():
    assert not inspect.isabstract(class::diagramm::RefDataType)


def test_class::diagramm::refdatatype_constructor_exists():
    assert callable(class::diagramm::RefDataType.__init__)


def test_class::diagramm::refdatatype_constructor_args():
    sig = inspect.signature(class::diagramm::RefDataType.__init__)
    params = list(sig.parameters.keys())



def test_class::diagramm::refparameter_is_not_abstract():
    assert not inspect.isabstract(class::diagramm::RefParameter)


def test_class::diagramm::refparameter_constructor_exists():
    assert callable(class::diagramm::RefParameter.__init__)


def test_class::diagramm::refparameter_constructor_args():
    sig = inspect.signature(class::diagramm::RefParameter.__init__)
    params = list(sig.parameters.keys())



def test_refmethod_is_not_abstract():
    assert not inspect.isabstract(RefMethod)


def test_refmethod_constructor_exists():
    assert callable(RefMethod.__init__)


def test_refmethod_constructor_args():
    sig = inspect.signature(RefMethod.__init__)
    params = list(sig.parameters.keys())



def test_class::diagramm::method_is_not_abstract():
    assert not inspect.isabstract(class::diagramm::Method)


def test_class::diagramm::method_constructor_exists():
    assert callable(class::diagramm::Method.__init__)


def test_class::diagramm::method_constructor_args():
    sig = inspect.signature(class::diagramm::Method.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "modifier" in params, "Missing parameter 'modifier'"

def test_class::diagramm::method_has_name():
    assert hasattr(class::diagramm::Method, "name")
    descriptor = None
    for klass in class::diagramm::Method.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_class::diagramm::method_has_modifier():
    assert hasattr(class::diagramm::Method, "modifier")
    descriptor = None
    for klass in class::diagramm::Method.__mro__:
        if "modifier" in klass.__dict__:
            descriptor = klass.__dict__["modifier"]
            break
    assert isinstance(descriptor, property)



def test_refdatatype_is_not_abstract():
    assert not inspect.isabstract(RefDataType)


def test_refdatatype_constructor_exists():
    assert callable(RefDataType.__init__)


def test_refdatatype_constructor_args():
    sig = inspect.signature(RefDataType.__init__)
    params = list(sig.parameters.keys())



def test_class::diagramm::datatype_is_not_abstract():
    assert not inspect.isabstract(class::diagramm::DataType)


def test_class::diagramm::datatype_constructor_exists():
    assert callable(class::diagramm::DataType.__init__)


def test_class::diagramm::datatype_constructor_args():
    sig = inspect.signature(class::diagramm::DataType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_class::diagramm::datatype_has_name():
    assert hasattr(class::diagramm::DataType, "name")
    descriptor = None
    for klass in class::diagramm::DataType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_class::diagramm::refclass_is_not_abstract():
    assert not inspect.isabstract(class::diagramm::RefClass)


def test_class::diagramm::refclass_constructor_exists():
    assert callable(class::diagramm::RefClass.__init__)


def test_class::diagramm::refclass_constructor_args():
    sig = inspect.signature(class::diagramm::RefClass.__init__)
    params = list(sig.parameters.keys())



def test_class::diagramm::refassociation_is_not_abstract():
    assert not inspect.isabstract(class::diagramm::RefAssociation)


def test_class::diagramm::refassociation_constructor_exists():
    assert callable(class::diagramm::RefAssociation.__init__)


def test_class::diagramm::refassociation_constructor_args():
    sig = inspect.signature(class::diagramm::RefAssociation.__init__)
    params = list(sig.parameters.keys())



def test_class::diagramm::package_is_not_abstract():
    assert not inspect.isabstract(class::diagramm::Package)


def test_class::diagramm::package_constructor_exists():
    assert callable(class::diagramm::Package.__init__)


def test_class::diagramm::package_constructor_args():
    sig = inspect.signature(class::diagramm::Package.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_class::diagramm::package_has_name():
    assert hasattr(class::diagramm::Package, "name")
    descriptor = None
    for klass in class::diagramm::Package.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_modifiertype_exists():
    # Check that the Enumeration exists
    assert ModifierType is not None

def test_modifiertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ModifierType]
    expected_literals = [
        "abstract",
        "public",
        "static",
        "protected",
        "private",
        "final",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ModifierType"


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
class::diagramm::RefPackage_strategy = st.builds(
    class::diagramm::RefPackage,
)
RefAssociation_strategy = st.builds(
    RefAssociation,
)
class::diagramm::Association_strategy = st.builds(
    class::diagramm::Association,
    minCardinality=
        st.integers(),
    isAggregation=
        st.booleans(),
    name=
        safe_text,
    maxCardinality=
        st.integers()
)
class::diagramm::RefMethod_strategy = st.builds(
    class::diagramm::RefMethod,
)
class::diagramm::RefAttribute_strategy = st.builds(
    class::diagramm::RefAttribute,
)
RefClass_strategy = st.builds(
    RefClass,
)
class::diagramm::Class_strategy = st.builds(
    class::diagramm::Class,
    name=
        safe_text,
    modifier=
        safe_text
)
RefPackage_strategy = st.builds(
    RefPackage,
)
RefParameter_strategy = st.builds(
    RefParameter,
)
class::diagramm::Parameter_strategy = st.builds(
    class::diagramm::Parameter,
    name=
        safe_text
)
RefAttribute_strategy = st.builds(
    RefAttribute,
)
class::diagramm::Attribute_strategy = st.builds(
    class::diagramm::Attribute,
    modifier=
        safe_text,
    name=
        safe_text
)
class::diagramm::RefDataType_strategy = st.builds(
    class::diagramm::RefDataType,
)
class::diagramm::RefParameter_strategy = st.builds(
    class::diagramm::RefParameter,
)
RefMethod_strategy = st.builds(
    RefMethod,
)
class::diagramm::Method_strategy = st.builds(
    class::diagramm::Method,
    name=
        safe_text,
    modifier=
        safe_text
)
RefDataType_strategy = st.builds(
    RefDataType,
)
class::diagramm::DataType_strategy = st.builds(
    class::diagramm::DataType,
    name=
        safe_text
)
class::diagramm::RefClass_strategy = st.builds(
    class::diagramm::RefClass,
)
class::diagramm::RefAssociation_strategy = st.builds(
    class::diagramm::RefAssociation,
)
class::diagramm::Package_strategy = st.builds(
    class::diagramm::Package,
    name=
        safe_text
)

@given(instance=class::diagramm::RefPackage_strategy)
@settings(max_examples=50)
def test_class::diagramm::refpackage_instantiation(instance):
    assert isinstance(instance, class::diagramm::RefPackage)

@given(instance=RefAssociation_strategy)
@settings(max_examples=50)
def test_refassociation_instantiation(instance):
    assert isinstance(instance, RefAssociation)

@given(instance=class::diagramm::Association_strategy)
@settings(max_examples=50)
def test_class::diagramm::association_instantiation(instance):
    assert isinstance(instance, class::diagramm::Association)

@given(instance=class::diagramm::Association_strategy)
def test_class::diagramm::association_minCardinality_type(instance):
    assert isinstance(instance.minCardinality, int)


@given(instance=class::diagramm::Association_strategy)
def test_class::diagramm::association_minCardinality_setter(instance):
    original = instance.minCardinality
    instance.minCardinality = original
    assert instance.minCardinality == original

@given(instance=class::diagramm::Association_strategy)
def test_class::diagramm::association_isAggregation_type(instance):
    assert isinstance(instance.isAggregation, bool)


@given(instance=class::diagramm::Association_strategy)
def test_class::diagramm::association_isAggregation_setter(instance):
    original = instance.isAggregation
    instance.isAggregation = original
    assert instance.isAggregation == original

@given(instance=class::diagramm::Association_strategy)
def test_class::diagramm::association_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=class::diagramm::Association_strategy)
def test_class::diagramm::association_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=class::diagramm::Association_strategy)
def test_class::diagramm::association_maxCardinality_type(instance):
    assert isinstance(instance.maxCardinality, int)


@given(instance=class::diagramm::Association_strategy)
def test_class::diagramm::association_maxCardinality_setter(instance):
    original = instance.maxCardinality
    instance.maxCardinality = original
    assert instance.maxCardinality == original

@given(instance=class::diagramm::RefMethod_strategy)
@settings(max_examples=50)
def test_class::diagramm::refmethod_instantiation(instance):
    assert isinstance(instance, class::diagramm::RefMethod)

@given(instance=class::diagramm::RefAttribute_strategy)
@settings(max_examples=50)
def test_class::diagramm::refattribute_instantiation(instance):
    assert isinstance(instance, class::diagramm::RefAttribute)

@given(instance=RefClass_strategy)
@settings(max_examples=50)
def test_refclass_instantiation(instance):
    assert isinstance(instance, RefClass)

@given(instance=class::diagramm::Class_strategy)
@settings(max_examples=50)
def test_class::diagramm::class_instantiation(instance):
    assert isinstance(instance, class::diagramm::Class)

@given(instance=class::diagramm::Class_strategy)
def test_class::diagramm::class_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=class::diagramm::Class_strategy)
def test_class::diagramm::class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=class::diagramm::Class_strategy)
def test_class::diagramm::class_modifier_type(instance):
    assert isinstance(instance.modifier, str)


@given(instance=class::diagramm::Class_strategy)
def test_class::diagramm::class_modifier_setter(instance):
    original = instance.modifier
    instance.modifier = original
    assert instance.modifier == original

@given(instance=RefPackage_strategy)
@settings(max_examples=50)
def test_refpackage_instantiation(instance):
    assert isinstance(instance, RefPackage)

@given(instance=RefParameter_strategy)
@settings(max_examples=50)
def test_refparameter_instantiation(instance):
    assert isinstance(instance, RefParameter)

@given(instance=class::diagramm::Parameter_strategy)
@settings(max_examples=50)
def test_class::diagramm::parameter_instantiation(instance):
    assert isinstance(instance, class::diagramm::Parameter)

@given(instance=class::diagramm::Parameter_strategy)
def test_class::diagramm::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=class::diagramm::Parameter_strategy)
def test_class::diagramm::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RefAttribute_strategy)
@settings(max_examples=50)
def test_refattribute_instantiation(instance):
    assert isinstance(instance, RefAttribute)

@given(instance=class::diagramm::Attribute_strategy)
@settings(max_examples=50)
def test_class::diagramm::attribute_instantiation(instance):
    assert isinstance(instance, class::diagramm::Attribute)

@given(instance=class::diagramm::Attribute_strategy)
def test_class::diagramm::attribute_modifier_type(instance):
    assert isinstance(instance.modifier, str)


@given(instance=class::diagramm::Attribute_strategy)
def test_class::diagramm::attribute_modifier_setter(instance):
    original = instance.modifier
    instance.modifier = original
    assert instance.modifier == original

@given(instance=class::diagramm::Attribute_strategy)
def test_class::diagramm::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=class::diagramm::Attribute_strategy)
def test_class::diagramm::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=class::diagramm::RefDataType_strategy)
@settings(max_examples=50)
def test_class::diagramm::refdatatype_instantiation(instance):
    assert isinstance(instance, class::diagramm::RefDataType)

@given(instance=class::diagramm::RefParameter_strategy)
@settings(max_examples=50)
def test_class::diagramm::refparameter_instantiation(instance):
    assert isinstance(instance, class::diagramm::RefParameter)

@given(instance=RefMethod_strategy)
@settings(max_examples=50)
def test_refmethod_instantiation(instance):
    assert isinstance(instance, RefMethod)

@given(instance=class::diagramm::Method_strategy)
@settings(max_examples=50)
def test_class::diagramm::method_instantiation(instance):
    assert isinstance(instance, class::diagramm::Method)

@given(instance=class::diagramm::Method_strategy)
def test_class::diagramm::method_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=class::diagramm::Method_strategy)
def test_class::diagramm::method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=class::diagramm::Method_strategy)
def test_class::diagramm::method_modifier_type(instance):
    assert isinstance(instance.modifier, str)


@given(instance=class::diagramm::Method_strategy)
def test_class::diagramm::method_modifier_setter(instance):
    original = instance.modifier
    instance.modifier = original
    assert instance.modifier == original

@given(instance=RefDataType_strategy)
@settings(max_examples=50)
def test_refdatatype_instantiation(instance):
    assert isinstance(instance, RefDataType)

@given(instance=class::diagramm::DataType_strategy)
@settings(max_examples=50)
def test_class::diagramm::datatype_instantiation(instance):
    assert isinstance(instance, class::diagramm::DataType)

@given(instance=class::diagramm::DataType_strategy)
def test_class::diagramm::datatype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=class::diagramm::DataType_strategy)
def test_class::diagramm::datatype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=class::diagramm::RefClass_strategy)
@settings(max_examples=50)
def test_class::diagramm::refclass_instantiation(instance):
    assert isinstance(instance, class::diagramm::RefClass)

@given(instance=class::diagramm::RefAssociation_strategy)
@settings(max_examples=50)
def test_class::diagramm::refassociation_instantiation(instance):
    assert isinstance(instance, class::diagramm::RefAssociation)

@given(instance=class::diagramm::Package_strategy)
@settings(max_examples=50)
def test_class::diagramm::package_instantiation(instance):
    assert isinstance(instance, class::diagramm::Package)

@given(instance=class::diagramm::Package_strategy)
def test_class::diagramm::package_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=class::diagramm::Package_strategy)
def test_class::diagramm::package_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
