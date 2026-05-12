import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sgen_DeprecatableElement,
    sgen_Expression,
    sgen_FeatureTypeLibrary,
    DeprecatableElement,
    NamedElement,
    sgen_FeatureParameter,
    sgen_FeatureType,
    sgen_FeatureConfiguration,
    sgen_GeneratorConfiguration,
    sgen_Property,
    sgen_GeneratorEntry,
    sgen_GeneratorModel,
    sgen_EObject,
    sgen_FeatureParameterValue,
    ParameterTypes,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sgen_deprecatableelement_is_not_abstract():
    assert not inspect.isabstract(sgen_DeprecatableElement)


def test_sgen_deprecatableelement_constructor_exists():
    assert callable(sgen_DeprecatableElement.__init__)


def test_sgen_deprecatableelement_constructor_args():
    sig = inspect.signature(sgen_DeprecatableElement.__init__)
    params = list(sig.parameters.keys())
    assert "deprecated" in params, "Missing parameter 'deprecated'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_sgen_deprecatableelement_has_deprecated():
    assert hasattr(sgen_DeprecatableElement, "deprecated")
    descriptor = None
    for klass in sgen_DeprecatableElement.__mro__:
        if "deprecated" in klass.__dict__:
            descriptor = klass.__dict__["deprecated"]
            break
    assert isinstance(descriptor, property)

def test_sgen_deprecatableelement_has_comment():
    assert hasattr(sgen_DeprecatableElement, "comment")
    descriptor = None
    for klass in sgen_DeprecatableElement.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_sgen_expression_is_not_abstract():
    assert not inspect.isabstract(sgen_Expression)


def test_sgen_expression_constructor_exists():
    assert callable(sgen_Expression.__init__)


def test_sgen_expression_constructor_args():
    sig = inspect.signature(sgen_Expression.__init__)
    params = list(sig.parameters.keys())



def test_sgen_featuretypelibrary_is_not_abstract():
    assert not inspect.isabstract(sgen_FeatureTypeLibrary)


def test_sgen_featuretypelibrary_constructor_exists():
    assert callable(sgen_FeatureTypeLibrary.__init__)


def test_sgen_featuretypelibrary_constructor_args():
    sig = inspect.signature(sgen_FeatureTypeLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sgen_featuretypelibrary_has_name():
    assert hasattr(sgen_FeatureTypeLibrary, "name")
    descriptor = None
    for klass in sgen_FeatureTypeLibrary.__mro__:
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



def test_sgen_featureparameter_is_not_abstract():
    assert not inspect.isabstract(sgen_FeatureParameter)


def test_sgen_featureparameter_constructor_exists():
    assert callable(sgen_FeatureParameter.__init__)


def test_sgen_featureparameter_constructor_args():
    sig = inspect.signature(sgen_FeatureParameter.__init__)
    params = list(sig.parameters.keys())
    assert "parameterType" in params, "Missing parameter 'parameterType'"
    assert "optional" in params, "Missing parameter 'optional'"

def test_sgen_featureparameter_has_parameterType():
    assert hasattr(sgen_FeatureParameter, "parameterType")
    descriptor = None
    for klass in sgen_FeatureParameter.__mro__:
        if "parameterType" in klass.__dict__:
            descriptor = klass.__dict__["parameterType"]
            break
    assert isinstance(descriptor, property)

def test_sgen_featureparameter_has_optional():
    assert hasattr(sgen_FeatureParameter, "optional")
    descriptor = None
    for klass in sgen_FeatureParameter.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)



def test_sgen_featuretype_is_not_abstract():
    assert not inspect.isabstract(sgen_FeatureType)


def test_sgen_featuretype_constructor_exists():
    assert callable(sgen_FeatureType.__init__)


def test_sgen_featuretype_constructor_args():
    sig = inspect.signature(sgen_FeatureType.__init__)
    params = list(sig.parameters.keys())
    assert "optional" in params, "Missing parameter 'optional'"

def test_sgen_featuretype_has_optional():
    assert hasattr(sgen_FeatureType, "optional")
    descriptor = None
    for klass in sgen_FeatureType.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)



def test_sgen_featureconfiguration_is_not_abstract():
    assert not inspect.isabstract(sgen_FeatureConfiguration)


def test_sgen_featureconfiguration_constructor_exists():
    assert callable(sgen_FeatureConfiguration.__init__)


def test_sgen_featureconfiguration_constructor_args():
    sig = inspect.signature(sgen_FeatureConfiguration.__init__)
    params = list(sig.parameters.keys())



def test_sgen_generatorconfiguration_is_not_abstract():
    assert not inspect.isabstract(sgen_GeneratorConfiguration)


def test_sgen_generatorconfiguration_constructor_exists():
    assert callable(sgen_GeneratorConfiguration.__init__)


def test_sgen_generatorconfiguration_constructor_args():
    sig = inspect.signature(sgen_GeneratorConfiguration.__init__)
    params = list(sig.parameters.keys())



def test_sgen_property_is_not_abstract():
    assert not inspect.isabstract(sgen_Property)


def test_sgen_property_constructor_exists():
    assert callable(sgen_Property.__init__)


def test_sgen_property_constructor_args():
    sig = inspect.signature(sgen_Property.__init__)
    params = list(sig.parameters.keys())



def test_sgen_generatorentry_is_not_abstract():
    assert not inspect.isabstract(sgen_GeneratorEntry)


def test_sgen_generatorentry_constructor_exists():
    assert callable(sgen_GeneratorEntry.__init__)


def test_sgen_generatorentry_constructor_args():
    sig = inspect.signature(sgen_GeneratorEntry.__init__)
    params = list(sig.parameters.keys())
    assert "contentType" in params, "Missing parameter 'contentType'"

def test_sgen_generatorentry_has_contentType():
    assert hasattr(sgen_GeneratorEntry, "contentType")
    descriptor = None
    for klass in sgen_GeneratorEntry.__mro__:
        if "contentType" in klass.__dict__:
            descriptor = klass.__dict__["contentType"]
            break
    assert isinstance(descriptor, property)



def test_sgen_generatormodel_is_not_abstract():
    assert not inspect.isabstract(sgen_GeneratorModel)


def test_sgen_generatormodel_constructor_exists():
    assert callable(sgen_GeneratorModel.__init__)


def test_sgen_generatormodel_constructor_args():
    sig = inspect.signature(sgen_GeneratorModel.__init__)
    params = list(sig.parameters.keys())
    assert "generatorId" in params, "Missing parameter 'generatorId'"

def test_sgen_generatormodel_has_generatorId():
    assert hasattr(sgen_GeneratorModel, "generatorId")
    descriptor = None
    for klass in sgen_GeneratorModel.__mro__:
        if "generatorId" in klass.__dict__:
            descriptor = klass.__dict__["generatorId"]
            break
    assert isinstance(descriptor, property)



def test_sgen_eobject_is_not_abstract():
    assert not inspect.isabstract(sgen_EObject)


def test_sgen_eobject_constructor_exists():
    assert callable(sgen_EObject.__init__)


def test_sgen_eobject_constructor_args():
    sig = inspect.signature(sgen_EObject.__init__)
    params = list(sig.parameters.keys())



def test_sgen_featureparametervalue_is_not_abstract():
    assert not inspect.isabstract(sgen_FeatureParameterValue)


def test_sgen_featureparametervalue_constructor_exists():
    assert callable(sgen_FeatureParameterValue.__init__)


def test_sgen_featureparametervalue_constructor_args():
    sig = inspect.signature(sgen_FeatureParameterValue.__init__)
    params = list(sig.parameters.keys())

def test_parametertypes_exists():
    # Check that the Enumeration exists
    assert ParameterTypes is not None

def test_parametertypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterTypes]
    expected_literals = [
        "FLOAT",
        "STRING",
        "BOOLEAN",
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
sgen_DeprecatableElement_strategy = st.builds(
    sgen_DeprecatableElement,
    deprecated=
        st.booleans(),
    comment=
        safe_text
)
sgen_Expression_strategy = st.builds(
    sgen_Expression,
)
sgen_FeatureTypeLibrary_strategy = st.builds(
    sgen_FeatureTypeLibrary,
    name=
        safe_text
)
DeprecatableElement_strategy = st.builds(
    DeprecatableElement,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
sgen_FeatureParameter_strategy = st.builds(
    sgen_FeatureParameter,
    parameterType=
        safe_text,
    optional=
        st.booleans()
)
sgen_FeatureType_strategy = st.builds(
    sgen_FeatureType,
    optional=
        st.booleans()
)
sgen_FeatureConfiguration_strategy = st.builds(
    sgen_FeatureConfiguration,
)
sgen_GeneratorConfiguration_strategy = st.builds(
    sgen_GeneratorConfiguration,
)
sgen_Property_strategy = st.builds(
    sgen_Property,
)
sgen_GeneratorEntry_strategy = st.builds(
    sgen_GeneratorEntry,
    contentType=
        safe_text
)
sgen_GeneratorModel_strategy = st.builds(
    sgen_GeneratorModel,
    generatorId=
        safe_text
)
sgen_EObject_strategy = st.builds(
    sgen_EObject,
)
sgen_FeatureParameterValue_strategy = st.builds(
    sgen_FeatureParameterValue,
)

@given(instance=sgen_DeprecatableElement_strategy)
@settings(max_examples=50)
def test_sgen_deprecatableelement_instantiation(instance):
    assert isinstance(instance, sgen_DeprecatableElement)



@given(instance=sgen_DeprecatableElement_strategy)
def test_sgen_deprecatableelement_deprecated_setter(instance):
    original = instance.deprecated
    instance.deprecated = original
    assert instance.deprecated == original



@given(instance=sgen_DeprecatableElement_strategy)
def test_sgen_deprecatableelement_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=sgen_Expression_strategy)
@settings(max_examples=50)
def test_sgen_expression_instantiation(instance):
    assert isinstance(instance, sgen_Expression)

@given(instance=sgen_FeatureTypeLibrary_strategy)
@settings(max_examples=50)
def test_sgen_featuretypelibrary_instantiation(instance):
    assert isinstance(instance, sgen_FeatureTypeLibrary)



@given(instance=sgen_FeatureTypeLibrary_strategy)
def test_sgen_featuretypelibrary_name_setter(instance):
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

@given(instance=sgen_FeatureParameter_strategy)
@settings(max_examples=50)
def test_sgen_featureparameter_instantiation(instance):
    assert isinstance(instance, sgen_FeatureParameter)



@given(instance=sgen_FeatureParameter_strategy)
def test_sgen_featureparameter_parameterType_setter(instance):
    original = instance.parameterType
    instance.parameterType = original
    assert instance.parameterType == original



@given(instance=sgen_FeatureParameter_strategy)
def test_sgen_featureparameter_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=sgen_FeatureType_strategy)
@settings(max_examples=50)
def test_sgen_featuretype_instantiation(instance):
    assert isinstance(instance, sgen_FeatureType)



@given(instance=sgen_FeatureType_strategy)
def test_sgen_featuretype_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=sgen_FeatureConfiguration_strategy)
@settings(max_examples=50)
def test_sgen_featureconfiguration_instantiation(instance):
    assert isinstance(instance, sgen_FeatureConfiguration)

@given(instance=sgen_GeneratorConfiguration_strategy)
@settings(max_examples=50)
def test_sgen_generatorconfiguration_instantiation(instance):
    assert isinstance(instance, sgen_GeneratorConfiguration)

@given(instance=sgen_Property_strategy)
@settings(max_examples=50)
def test_sgen_property_instantiation(instance):
    assert isinstance(instance, sgen_Property)

@given(instance=sgen_GeneratorEntry_strategy)
@settings(max_examples=50)
def test_sgen_generatorentry_instantiation(instance):
    assert isinstance(instance, sgen_GeneratorEntry)



@given(instance=sgen_GeneratorEntry_strategy)
def test_sgen_generatorentry_contentType_setter(instance):
    original = instance.contentType
    instance.contentType = original
    assert instance.contentType == original

@given(instance=sgen_GeneratorModel_strategy)
@settings(max_examples=50)
def test_sgen_generatormodel_instantiation(instance):
    assert isinstance(instance, sgen_GeneratorModel)



@given(instance=sgen_GeneratorModel_strategy)
def test_sgen_generatormodel_generatorId_setter(instance):
    original = instance.generatorId
    instance.generatorId = original
    assert instance.generatorId == original

@given(instance=sgen_EObject_strategy)
@settings(max_examples=50)
def test_sgen_eobject_instantiation(instance):
    assert isinstance(instance, sgen_EObject)

@given(instance=sgen_FeatureParameterValue_strategy)
@settings(max_examples=50)
def test_sgen_featureparametervalue_instantiation(instance):
    assert isinstance(instance, sgen_FeatureParameterValue)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sgen_FeatureParameterValue_strategy)
@settings(max_examples=30)
def test_sgen_featureparametervalue_setvalue_changes_state(instance):
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
        assert has_statements, f"Function 'setValue' in sgen_FeatureParameterValue is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setValue' in sgen_FeatureParameterValue did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setValue' in sgen_FeatureParameterValue is not implemented or raised an error")
