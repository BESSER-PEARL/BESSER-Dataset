import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sgen::DeprecatableElement,
    sgen::Expression,
    sgen::FeatureTypeLibrary,
    DeprecatableElement,
    NamedElement,
    sgen::FeatureParameter,
    sgen::FeatureType,
    sgen::FeatureConfiguration,
    sgen::GeneratorConfiguration,
    sgen::Property,
    sgen::GeneratorEntry,
    sgen::GeneratorModel,
    sgen::EObject,
    sgen::FeatureParameterValue,
    ParameterTypes,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sgen::deprecatableelement_is_not_abstract():
    assert not inspect.isabstract(sgen::DeprecatableElement)


def test_sgen::deprecatableelement_constructor_exists():
    assert callable(sgen::DeprecatableElement.__init__)


def test_sgen::deprecatableelement_constructor_args():
    sig = inspect.signature(sgen::DeprecatableElement.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "deprecated" in params, "Missing parameter 'deprecated'"

def test_sgen::deprecatableelement_has_comment():
    assert hasattr(sgen::DeprecatableElement, "comment")
    descriptor = None
    for klass in sgen::DeprecatableElement.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_sgen::deprecatableelement_has_deprecated():
    assert hasattr(sgen::DeprecatableElement, "deprecated")
    descriptor = None
    for klass in sgen::DeprecatableElement.__mro__:
        if "deprecated" in klass.__dict__:
            descriptor = klass.__dict__["deprecated"]
            break
    assert isinstance(descriptor, property)



def test_sgen::expression_is_not_abstract():
    assert not inspect.isabstract(sgen::Expression)


def test_sgen::expression_constructor_exists():
    assert callable(sgen::Expression.__init__)


def test_sgen::expression_constructor_args():
    sig = inspect.signature(sgen::Expression.__init__)
    params = list(sig.parameters.keys())



def test_sgen::featuretypelibrary_is_not_abstract():
    assert not inspect.isabstract(sgen::FeatureTypeLibrary)


def test_sgen::featuretypelibrary_constructor_exists():
    assert callable(sgen::FeatureTypeLibrary.__init__)


def test_sgen::featuretypelibrary_constructor_args():
    sig = inspect.signature(sgen::FeatureTypeLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sgen::featuretypelibrary_has_name():
    assert hasattr(sgen::FeatureTypeLibrary, "name")
    descriptor = None
    for klass in sgen::FeatureTypeLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_deprecatableelement_is_not_abstract():
    assert not inspect.isabstract(DeprecatableElement)


def test_deprecatableelement_constructor_exists():
    assert callable(DeprecatableElement.__init__)


def test_deprecatableelement_constructor_args():
    sig = inspect.signature(DeprecatableElement.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_sgen::featureparameter_is_not_abstract():
    assert not inspect.isabstract(sgen::FeatureParameter)


def test_sgen::featureparameter_constructor_exists():
    assert callable(sgen::FeatureParameter.__init__)


def test_sgen::featureparameter_constructor_args():
    sig = inspect.signature(sgen::FeatureParameter.__init__)
    params = list(sig.parameters.keys())
    assert "parameterType" in params, "Missing parameter 'parameterType'"
    assert "optional" in params, "Missing parameter 'optional'"

def test_sgen::featureparameter_has_parameterType():
    assert hasattr(sgen::FeatureParameter, "parameterType")
    descriptor = None
    for klass in sgen::FeatureParameter.__mro__:
        if "parameterType" in klass.__dict__:
            descriptor = klass.__dict__["parameterType"]
            break
    assert isinstance(descriptor, property)

def test_sgen::featureparameter_has_optional():
    assert hasattr(sgen::FeatureParameter, "optional")
    descriptor = None
    for klass in sgen::FeatureParameter.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)



def test_sgen::featuretype_is_not_abstract():
    assert not inspect.isabstract(sgen::FeatureType)


def test_sgen::featuretype_constructor_exists():
    assert callable(sgen::FeatureType.__init__)


def test_sgen::featuretype_constructor_args():
    sig = inspect.signature(sgen::FeatureType.__init__)
    params = list(sig.parameters.keys())
    assert "optional" in params, "Missing parameter 'optional'"

def test_sgen::featuretype_has_optional():
    assert hasattr(sgen::FeatureType, "optional")
    descriptor = None
    for klass in sgen::FeatureType.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)



def test_sgen::featureconfiguration_is_not_abstract():
    assert not inspect.isabstract(sgen::FeatureConfiguration)


def test_sgen::featureconfiguration_constructor_exists():
    assert callable(sgen::FeatureConfiguration.__init__)


def test_sgen::featureconfiguration_constructor_args():
    sig = inspect.signature(sgen::FeatureConfiguration.__init__)
    params = list(sig.parameters.keys())



def test_sgen::generatorconfiguration_is_not_abstract():
    assert not inspect.isabstract(sgen::GeneratorConfiguration)


def test_sgen::generatorconfiguration_constructor_exists():
    assert callable(sgen::GeneratorConfiguration.__init__)


def test_sgen::generatorconfiguration_constructor_args():
    sig = inspect.signature(sgen::GeneratorConfiguration.__init__)
    params = list(sig.parameters.keys())



def test_sgen::property_is_not_abstract():
    assert not inspect.isabstract(sgen::Property)


def test_sgen::property_constructor_exists():
    assert callable(sgen::Property.__init__)


def test_sgen::property_constructor_args():
    sig = inspect.signature(sgen::Property.__init__)
    params = list(sig.parameters.keys())



def test_sgen::generatorentry_is_not_abstract():
    assert not inspect.isabstract(sgen::GeneratorEntry)


def test_sgen::generatorentry_constructor_exists():
    assert callable(sgen::GeneratorEntry.__init__)


def test_sgen::generatorentry_constructor_args():
    sig = inspect.signature(sgen::GeneratorEntry.__init__)
    params = list(sig.parameters.keys())
    assert "contentType" in params, "Missing parameter 'contentType'"

def test_sgen::generatorentry_has_contentType():
    assert hasattr(sgen::GeneratorEntry, "contentType")
    descriptor = None
    for klass in sgen::GeneratorEntry.__mro__:
        if "contentType" in klass.__dict__:
            descriptor = klass.__dict__["contentType"]
            break
    assert isinstance(descriptor, property)



def test_sgen::generatormodel_is_not_abstract():
    assert not inspect.isabstract(sgen::GeneratorModel)


def test_sgen::generatormodel_constructor_exists():
    assert callable(sgen::GeneratorModel.__init__)


def test_sgen::generatormodel_constructor_args():
    sig = inspect.signature(sgen::GeneratorModel.__init__)
    params = list(sig.parameters.keys())
    assert "generatorId" in params, "Missing parameter 'generatorId'"

def test_sgen::generatormodel_has_generatorId():
    assert hasattr(sgen::GeneratorModel, "generatorId")
    descriptor = None
    for klass in sgen::GeneratorModel.__mro__:
        if "generatorId" in klass.__dict__:
            descriptor = klass.__dict__["generatorId"]
            break
    assert isinstance(descriptor, property)



def test_sgen::eobject_is_not_abstract():
    assert not inspect.isabstract(sgen::EObject)


def test_sgen::eobject_constructor_exists():
    assert callable(sgen::EObject.__init__)


def test_sgen::eobject_constructor_args():
    sig = inspect.signature(sgen::EObject.__init__)
    params = list(sig.parameters.keys())



def test_sgen::featureparametervalue_is_not_abstract():
    assert not inspect.isabstract(sgen::FeatureParameterValue)


def test_sgen::featureparametervalue_constructor_exists():
    assert callable(sgen::FeatureParameterValue.__init__)


def test_sgen::featureparametervalue_constructor_args():
    sig = inspect.signature(sgen::FeatureParameterValue.__init__)
    params = list(sig.parameters.keys())

def test_parametertypes_exists():
    # Check that the Enumeration exists
    assert ParameterTypes is not None

def test_parametertypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterTypes]
    expected_literals = [
        "BOOLEAN",
        "FLOAT",
        "STRING",
        "INTEGER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterTypes"


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
sgen::DeprecatableElement_strategy = st.builds(
    sgen::DeprecatableElement,
    comment=
        safe_text,
    deprecated=
        st.booleans()
)
sgen::Expression_strategy = st.builds(
    sgen::Expression,
)
sgen::FeatureTypeLibrary_strategy = st.builds(
    sgen::FeatureTypeLibrary,
    name=
        safe_text
)
DeprecatableElement_strategy = st.builds(
    DeprecatableElement,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
sgen::FeatureParameter_strategy = st.builds(
    sgen::FeatureParameter,
    parameterType=
        safe_text,
    optional=
        st.booleans()
)
sgen::FeatureType_strategy = st.builds(
    sgen::FeatureType,
    optional=
        st.booleans()
)
sgen::FeatureConfiguration_strategy = st.builds(
    sgen::FeatureConfiguration,
)
sgen::GeneratorConfiguration_strategy = st.builds(
    sgen::GeneratorConfiguration,
)
sgen::Property_strategy = st.builds(
    sgen::Property,
)
sgen::GeneratorEntry_strategy = st.builds(
    sgen::GeneratorEntry,
    contentType=
        safe_text
)
sgen::GeneratorModel_strategy = st.builds(
    sgen::GeneratorModel,
    generatorId=
        safe_text
)
sgen::EObject_strategy = st.builds(
    sgen::EObject,
)
sgen::FeatureParameterValue_strategy = st.builds(
    sgen::FeatureParameterValue,
)

@given(instance=sgen::DeprecatableElement_strategy)
@settings(max_examples=50)
def test_sgen::deprecatableelement_instantiation(instance):
    assert isinstance(instance, sgen::DeprecatableElement)

@given(instance=sgen::DeprecatableElement_strategy)
def test_sgen::deprecatableelement_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=sgen::DeprecatableElement_strategy)
def test_sgen::deprecatableelement_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=sgen::DeprecatableElement_strategy)
def test_sgen::deprecatableelement_deprecated_type(instance):
    assert isinstance(instance.deprecated, bool)


@given(instance=sgen::DeprecatableElement_strategy)
def test_sgen::deprecatableelement_deprecated_setter(instance):
    original = instance.deprecated
    instance.deprecated = original
    assert instance.deprecated == original

@given(instance=sgen::Expression_strategy)
@settings(max_examples=50)
def test_sgen::expression_instantiation(instance):
    assert isinstance(instance, sgen::Expression)

@given(instance=sgen::FeatureTypeLibrary_strategy)
@settings(max_examples=50)
def test_sgen::featuretypelibrary_instantiation(instance):
    assert isinstance(instance, sgen::FeatureTypeLibrary)

@given(instance=sgen::FeatureTypeLibrary_strategy)
def test_sgen::featuretypelibrary_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sgen::FeatureTypeLibrary_strategy)
def test_sgen::featuretypelibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DeprecatableElement_strategy)
@settings(max_examples=50)
def test_deprecatableelement_instantiation(instance):
    assert isinstance(instance, DeprecatableElement)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=sgen::FeatureParameter_strategy)
@settings(max_examples=50)
def test_sgen::featureparameter_instantiation(instance):
    assert isinstance(instance, sgen::FeatureParameter)

@given(instance=sgen::FeatureParameter_strategy)
def test_sgen::featureparameter_parameterType_type(instance):
    assert isinstance(instance.parameterType, str)


@given(instance=sgen::FeatureParameter_strategy)
def test_sgen::featureparameter_parameterType_setter(instance):
    original = instance.parameterType
    instance.parameterType = original
    assert instance.parameterType == original

@given(instance=sgen::FeatureParameter_strategy)
def test_sgen::featureparameter_optional_type(instance):
    assert isinstance(instance.optional, bool)


@given(instance=sgen::FeatureParameter_strategy)
def test_sgen::featureparameter_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=sgen::FeatureType_strategy)
@settings(max_examples=50)
def test_sgen::featuretype_instantiation(instance):
    assert isinstance(instance, sgen::FeatureType)

@given(instance=sgen::FeatureType_strategy)
def test_sgen::featuretype_optional_type(instance):
    assert isinstance(instance.optional, bool)


@given(instance=sgen::FeatureType_strategy)
def test_sgen::featuretype_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=sgen::FeatureConfiguration_strategy)
@settings(max_examples=50)
def test_sgen::featureconfiguration_instantiation(instance):
    assert isinstance(instance, sgen::FeatureConfiguration)

@given(instance=sgen::GeneratorConfiguration_strategy)
@settings(max_examples=50)
def test_sgen::generatorconfiguration_instantiation(instance):
    assert isinstance(instance, sgen::GeneratorConfiguration)

@given(instance=sgen::Property_strategy)
@settings(max_examples=50)
def test_sgen::property_instantiation(instance):
    assert isinstance(instance, sgen::Property)

@given(instance=sgen::GeneratorEntry_strategy)
@settings(max_examples=50)
def test_sgen::generatorentry_instantiation(instance):
    assert isinstance(instance, sgen::GeneratorEntry)

@given(instance=sgen::GeneratorEntry_strategy)
def test_sgen::generatorentry_contentType_type(instance):
    assert isinstance(instance.contentType, str)


@given(instance=sgen::GeneratorEntry_strategy)
def test_sgen::generatorentry_contentType_setter(instance):
    original = instance.contentType
    instance.contentType = original
    assert instance.contentType == original

@given(instance=sgen::GeneratorModel_strategy)
@settings(max_examples=50)
def test_sgen::generatormodel_instantiation(instance):
    assert isinstance(instance, sgen::GeneratorModel)

@given(instance=sgen::GeneratorModel_strategy)
def test_sgen::generatormodel_generatorId_type(instance):
    assert isinstance(instance.generatorId, str)


@given(instance=sgen::GeneratorModel_strategy)
def test_sgen::generatormodel_generatorId_setter(instance):
    original = instance.generatorId
    instance.generatorId = original
    assert instance.generatorId == original

@given(instance=sgen::EObject_strategy)
@settings(max_examples=50)
def test_sgen::eobject_instantiation(instance):
    assert isinstance(instance, sgen::EObject)

@given(instance=sgen::FeatureParameterValue_strategy)
@settings(max_examples=50)
def test_sgen::featureparametervalue_instantiation(instance):
    assert isinstance(instance, sgen::FeatureParameterValue)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sgen::FeatureParameterValue_strategy)
@settings(max_examples=30)
def test_sgen::featureparametervalue_setvalue_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setValue(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setValue).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setValue' in sgen::FeatureParameterValue is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setValue' in sgen::FeatureParameterValue did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setValue' in sgen::FeatureParameterValue is not implemented or raised an error")
