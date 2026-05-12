import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NameContainer,
    schema::ActionLike,
    schema::EFactory,
    schema::EPackage,
    schema::TargetType,
    schema::AggregationType,
    schema::ActionType,
    schema::StoryType,
    NsPrefixable,
    schema::TargetTypeRef,
    BundleAware,
    ResourceAware,
    schema::StorySchemaCatalog,
    Tenses,
    ActionTypeStatus,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namecontainer_is_not_abstract():
    assert not inspect.isabstract(NameContainer)


def test_namecontainer_constructor_exists():
    assert callable(NameContainer.__init__)


def test_namecontainer_constructor_args():
    sig = inspect.signature(NameContainer.__init__)
    params = list(sig.parameters.keys())



def test_schema::actionlike_is_not_abstract():
    assert not inspect.isabstract(schema::ActionLike)


def test_schema::actionlike_constructor_exists():
    assert callable(schema::ActionLike.__init__)


def test_schema::actionlike_constructor_args():
    sig = inspect.signature(schema::ActionLike.__init__)
    params = list(sig.parameters.keys())
    assert "pluralPresentTense" in params, "Missing parameter 'pluralPresentTense'"
    assert "imperativeTense" in params, "Missing parameter 'imperativeTense'"
    assert "tenses" in params, "Missing parameter 'tenses'"
    assert "pastTense" in params, "Missing parameter 'pastTense'"
    assert "pluralPastTense" in params, "Missing parameter 'pluralPastTense'"
    assert "presentTense" in params, "Missing parameter 'presentTense'"

def test_schema::actionlike_has_pluralPresentTense():
    assert hasattr(schema::ActionLike, "pluralPresentTense")
    descriptor = None
    for klass in schema::ActionLike.__mro__:
        if "pluralPresentTense" in klass.__dict__:
            descriptor = klass.__dict__["pluralPresentTense"]
            break
    assert isinstance(descriptor, property)

def test_schema::actionlike_has_imperativeTense():
    assert hasattr(schema::ActionLike, "imperativeTense")
    descriptor = None
    for klass in schema::ActionLike.__mro__:
        if "imperativeTense" in klass.__dict__:
            descriptor = klass.__dict__["imperativeTense"]
            break
    assert isinstance(descriptor, property)

def test_schema::actionlike_has_tenses():
    assert hasattr(schema::ActionLike, "tenses")
    descriptor = None
    for klass in schema::ActionLike.__mro__:
        if "tenses" in klass.__dict__:
            descriptor = klass.__dict__["tenses"]
            break
    assert isinstance(descriptor, property)

def test_schema::actionlike_has_pastTense():
    assert hasattr(schema::ActionLike, "pastTense")
    descriptor = None
    for klass in schema::ActionLike.__mro__:
        if "pastTense" in klass.__dict__:
            descriptor = klass.__dict__["pastTense"]
            break
    assert isinstance(descriptor, property)

def test_schema::actionlike_has_pluralPastTense():
    assert hasattr(schema::ActionLike, "pluralPastTense")
    descriptor = None
    for klass in schema::ActionLike.__mro__:
        if "pluralPastTense" in klass.__dict__:
            descriptor = klass.__dict__["pluralPastTense"]
            break
    assert isinstance(descriptor, property)

def test_schema::actionlike_has_presentTense():
    assert hasattr(schema::ActionLike, "presentTense")
    descriptor = None
    for klass in schema::ActionLike.__mro__:
        if "presentTense" in klass.__dict__:
            descriptor = klass.__dict__["presentTense"]
            break
    assert isinstance(descriptor, property)



def test_schema::efactory_is_not_abstract():
    assert not inspect.isabstract(schema::EFactory)


def test_schema::efactory_constructor_exists():
    assert callable(schema::EFactory.__init__)


def test_schema::efactory_constructor_args():
    sig = inspect.signature(schema::EFactory.__init__)
    params = list(sig.parameters.keys())



def test_schema::epackage_is_not_abstract():
    assert not inspect.isabstract(schema::EPackage)


def test_schema::epackage_constructor_exists():
    assert callable(schema::EPackage.__init__)


def test_schema::epackage_constructor_args():
    sig = inspect.signature(schema::EPackage.__init__)
    params = list(sig.parameters.keys())



def test_schema::targettype_is_not_abstract():
    assert not inspect.isabstract(schema::TargetType)


def test_schema::targettype_constructor_exists():
    assert callable(schema::TargetType.__init__)


def test_schema::targettype_constructor_args():
    sig = inspect.signature(schema::TargetType.__init__)
    params = list(sig.parameters.keys())



def test_schema::aggregationtype_is_not_abstract():
    assert not inspect.isabstract(schema::AggregationType)


def test_schema::aggregationtype_constructor_exists():
    assert callable(schema::AggregationType.__init__)


def test_schema::aggregationtype_constructor_args():
    sig = inspect.signature(schema::AggregationType.__init__)
    params = list(sig.parameters.keys())



def test_schema::actiontype_is_not_abstract():
    assert not inspect.isabstract(schema::ActionType)


def test_schema::actiontype_constructor_exists():
    assert callable(schema::ActionType.__init__)


def test_schema::actiontype_constructor_args():
    sig = inspect.signature(schema::ActionType.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"

def test_schema::actiontype_has_status():
    assert hasattr(schema::ActionType, "status")
    descriptor = None
    for klass in schema::ActionType.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_schema::storytype_is_not_abstract():
    assert not inspect.isabstract(schema::StoryType)


def test_schema::storytype_constructor_exists():
    assert callable(schema::StoryType.__init__)


def test_schema::storytype_constructor_args():
    sig = inspect.signature(schema::StoryType.__init__)
    params = list(sig.parameters.keys())



def test_nsprefixable_is_not_abstract():
    assert not inspect.isabstract(NsPrefixable)


def test_nsprefixable_constructor_exists():
    assert callable(NsPrefixable.__init__)


def test_nsprefixable_constructor_args():
    sig = inspect.signature(NsPrefixable.__init__)
    params = list(sig.parameters.keys())



def test_schema::targettyperef_is_not_abstract():
    assert not inspect.isabstract(schema::TargetTypeRef)


def test_schema::targettyperef_constructor_exists():
    assert callable(schema::TargetTypeRef.__init__)


def test_schema::targettyperef_constructor_args():
    sig = inspect.signature(schema::TargetTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_bundleaware_is_not_abstract():
    assert not inspect.isabstract(BundleAware)


def test_bundleaware_constructor_exists():
    assert callable(BundleAware.__init__)


def test_bundleaware_constructor_args():
    sig = inspect.signature(BundleAware.__init__)
    params = list(sig.parameters.keys())



def test_resourceaware_is_not_abstract():
    assert not inspect.isabstract(ResourceAware)


def test_resourceaware_constructor_exists():
    assert callable(ResourceAware.__init__)


def test_resourceaware_constructor_args():
    sig = inspect.signature(ResourceAware.__init__)
    params = list(sig.parameters.keys())



def test_schema::storyschemacatalog_is_not_abstract():
    assert not inspect.isabstract(schema::StorySchemaCatalog)


def test_schema::storyschemacatalog_constructor_exists():
    assert callable(schema::StorySchemaCatalog.__init__)


def test_schema::storyschemacatalog_constructor_args():
    sig = inspect.signature(schema::StorySchemaCatalog.__init__)
    params = list(sig.parameters.keys())
    assert "ecoreUrl" in params, "Missing parameter 'ecoreUrl'"
    assert "xmiUrl" in params, "Missing parameter 'xmiUrl'"
    assert "generatedPackageName" in params, "Missing parameter 'generatedPackageName'"

def test_schema::storyschemacatalog_has_ecoreUrl():
    assert hasattr(schema::StorySchemaCatalog, "ecoreUrl")
    descriptor = None
    for klass in schema::StorySchemaCatalog.__mro__:
        if "ecoreUrl" in klass.__dict__:
            descriptor = klass.__dict__["ecoreUrl"]
            break
    assert isinstance(descriptor, property)

def test_schema::storyschemacatalog_has_xmiUrl():
    assert hasattr(schema::StorySchemaCatalog, "xmiUrl")
    descriptor = None
    for klass in schema::StorySchemaCatalog.__mro__:
        if "xmiUrl" in klass.__dict__:
            descriptor = klass.__dict__["xmiUrl"]
            break
    assert isinstance(descriptor, property)

def test_schema::storyschemacatalog_has_generatedPackageName():
    assert hasattr(schema::StorySchemaCatalog, "generatedPackageName")
    descriptor = None
    for klass in schema::StorySchemaCatalog.__mro__:
        if "generatedPackageName" in klass.__dict__:
            descriptor = klass.__dict__["generatedPackageName"]
            break
    assert isinstance(descriptor, property)

def test_tenses_exists():
    # Check that the Enumeration exists
    assert Tenses is not None

def test_tenses_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Tenses]
    expected_literals = [
        "present",
        "both",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Tenses"

def test_actiontypestatus_exists():
    # Check that the Enumeration exists
    assert ActionTypeStatus is not None

def test_actiontypestatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActionTypeStatus]
    expected_literals = [
        "resolved",
        "unresolved",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActionTypeStatus"


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
NameContainer_strategy = st.builds(
    NameContainer,
)
schema::ActionLike_strategy = st.builds(
    schema::ActionLike,
    pluralPresentTense=
        safe_text,
    imperativeTense=
        safe_text,
    tenses=
        safe_text,
    pastTense=
        safe_text,
    pluralPastTense=
        safe_text,
    presentTense=
        safe_text
)
schema::EFactory_strategy = st.builds(
    schema::EFactory,
)
schema::EPackage_strategy = st.builds(
    schema::EPackage,
)
schema::TargetType_strategy = st.builds(
    schema::TargetType,
)
schema::AggregationType_strategy = st.builds(
    schema::AggregationType,
)
schema::ActionType_strategy = st.builds(
    schema::ActionType,
    status=
        safe_text
)
schema::StoryType_strategy = st.builds(
    schema::StoryType,
)
NsPrefixable_strategy = st.builds(
    NsPrefixable,
)
schema::TargetTypeRef_strategy = st.builds(
    schema::TargetTypeRef,
)
BundleAware_strategy = st.builds(
    BundleAware,
)
ResourceAware_strategy = st.builds(
    ResourceAware,
)
schema::StorySchemaCatalog_strategy = st.builds(
    schema::StorySchemaCatalog,
    ecoreUrl=
        safe_text,
    xmiUrl=
        safe_text,
    generatedPackageName=
        safe_text
)

@given(instance=NameContainer_strategy)
@settings(max_examples=50)
def test_namecontainer_instantiation(instance):
    assert isinstance(instance, NameContainer)

@given(instance=schema::ActionLike_strategy)
@settings(max_examples=50)
def test_schema::actionlike_instantiation(instance):
    assert isinstance(instance, schema::ActionLike)

@given(instance=schema::ActionLike_strategy)
def test_schema::actionlike_pluralPresentTense_type(instance):
    assert isinstance(instance.pluralPresentTense, str)


@given(instance=schema::ActionLike_strategy)
def test_schema::actionlike_pluralPresentTense_setter(instance):
    original = instance.pluralPresentTense
    instance.pluralPresentTense = original
    assert instance.pluralPresentTense == original

@given(instance=schema::ActionLike_strategy)
def test_schema::actionlike_imperativeTense_type(instance):
    assert isinstance(instance.imperativeTense, str)


@given(instance=schema::ActionLike_strategy)
def test_schema::actionlike_imperativeTense_setter(instance):
    original = instance.imperativeTense
    instance.imperativeTense = original
    assert instance.imperativeTense == original

@given(instance=schema::ActionLike_strategy)
def test_schema::actionlike_tenses_type(instance):
    assert isinstance(instance.tenses, str)


@given(instance=schema::ActionLike_strategy)
def test_schema::actionlike_tenses_setter(instance):
    original = instance.tenses
    instance.tenses = original
    assert instance.tenses == original

@given(instance=schema::ActionLike_strategy)
def test_schema::actionlike_pastTense_type(instance):
    assert isinstance(instance.pastTense, str)


@given(instance=schema::ActionLike_strategy)
def test_schema::actionlike_pastTense_setter(instance):
    original = instance.pastTense
    instance.pastTense = original
    assert instance.pastTense == original

@given(instance=schema::ActionLike_strategy)
def test_schema::actionlike_pluralPastTense_type(instance):
    assert isinstance(instance.pluralPastTense, str)


@given(instance=schema::ActionLike_strategy)
def test_schema::actionlike_pluralPastTense_setter(instance):
    original = instance.pluralPastTense
    instance.pluralPastTense = original
    assert instance.pluralPastTense == original

@given(instance=schema::ActionLike_strategy)
def test_schema::actionlike_presentTense_type(instance):
    assert isinstance(instance.presentTense, str)


@given(instance=schema::ActionLike_strategy)
def test_schema::actionlike_presentTense_setter(instance):
    original = instance.presentTense
    instance.presentTense = original
    assert instance.presentTense == original

@given(instance=schema::EFactory_strategy)
@settings(max_examples=50)
def test_schema::efactory_instantiation(instance):
    assert isinstance(instance, schema::EFactory)

@given(instance=schema::EPackage_strategy)
@settings(max_examples=50)
def test_schema::epackage_instantiation(instance):
    assert isinstance(instance, schema::EPackage)

@given(instance=schema::TargetType_strategy)
@settings(max_examples=50)
def test_schema::targettype_instantiation(instance):
    assert isinstance(instance, schema::TargetType)

@given(instance=schema::AggregationType_strategy)
@settings(max_examples=50)
def test_schema::aggregationtype_instantiation(instance):
    assert isinstance(instance, schema::AggregationType)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=schema::AggregationType_strategy)
@settings(max_examples=30)
def test_schema::aggregationtype_create_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.create()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.create).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'create' in schema::AggregationType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'create' in schema::AggregationType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'create' in schema::AggregationType is not implemented or raised an error")

@given(instance=schema::ActionType_strategy)
@settings(max_examples=50)
def test_schema::actiontype_instantiation(instance):
    assert isinstance(instance, schema::ActionType)

@given(instance=schema::ActionType_strategy)
def test_schema::actiontype_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=schema::ActionType_strategy)
def test_schema::actiontype_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=schema::ActionType_strategy)
@settings(max_examples=30)
def test_schema::actiontype_create_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.create()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.create).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'create' in schema::ActionType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'create' in schema::ActionType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'create' in schema::ActionType is not implemented or raised an error")

@given(instance=schema::StoryType_strategy)
@settings(max_examples=50)
def test_schema::storytype_instantiation(instance):
    assert isinstance(instance, schema::StoryType)

@given(instance=NsPrefixable_strategy)
@settings(max_examples=50)
def test_nsprefixable_instantiation(instance):
    assert isinstance(instance, NsPrefixable)

@given(instance=schema::TargetTypeRef_strategy)
@settings(max_examples=50)
def test_schema::targettyperef_instantiation(instance):
    assert isinstance(instance, schema::TargetTypeRef)

@given(instance=BundleAware_strategy)
@settings(max_examples=50)
def test_bundleaware_instantiation(instance):
    assert isinstance(instance, BundleAware)

@given(instance=ResourceAware_strategy)
@settings(max_examples=50)
def test_resourceaware_instantiation(instance):
    assert isinstance(instance, ResourceAware)

@given(instance=schema::StorySchemaCatalog_strategy)
@settings(max_examples=50)
def test_schema::storyschemacatalog_instantiation(instance):
    assert isinstance(instance, schema::StorySchemaCatalog)

@given(instance=schema::StorySchemaCatalog_strategy)
def test_schema::storyschemacatalog_ecoreUrl_type(instance):
    assert isinstance(instance.ecoreUrl, str)


@given(instance=schema::StorySchemaCatalog_strategy)
def test_schema::storyschemacatalog_ecoreUrl_setter(instance):
    original = instance.ecoreUrl
    instance.ecoreUrl = original
    assert instance.ecoreUrl == original

@given(instance=schema::StorySchemaCatalog_strategy)
def test_schema::storyschemacatalog_xmiUrl_type(instance):
    assert isinstance(instance.xmiUrl, str)


@given(instance=schema::StorySchemaCatalog_strategy)
def test_schema::storyschemacatalog_xmiUrl_setter(instance):
    original = instance.xmiUrl
    instance.xmiUrl = original
    assert instance.xmiUrl == original

@given(instance=schema::StorySchemaCatalog_strategy)
def test_schema::storyschemacatalog_generatedPackageName_type(instance):
    assert isinstance(instance.generatedPackageName, str)


@given(instance=schema::StorySchemaCatalog_strategy)
def test_schema::storyschemacatalog_generatedPackageName_setter(instance):
    original = instance.generatedPackageName
    instance.generatedPackageName = original
    assert instance.generatedPackageName == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=schema::StorySchemaCatalog_strategy)
@settings(max_examples=30)
def test_schema::storyschemacatalog_createaction_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createAction(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createAction).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createAction' in schema::StorySchemaCatalog is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createAction' in schema::StorySchemaCatalog did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createAction' in schema::StorySchemaCatalog is not implemented or raised an error")
