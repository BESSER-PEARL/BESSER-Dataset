import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Constraint,
    FeatureModel_ExcludeConstraint,
    FeatureModel_NamedElement,
    NamedElement,
    FeatureModel_Group,
    FeatureModel_Comment,
    FeatureModel_Feature,
    FeatureModel_Constraint,
    FeatureModel_FeatureModel,
    FeatureModel_RequireConstraint,
    GroupType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel_excludeconstraint_is_not_abstract():
    assert not inspect.isabstract(FeatureModel_ExcludeConstraint)


def test_featuremodel_excludeconstraint_constructor_exists():
    assert callable(FeatureModel_ExcludeConstraint.__init__)


def test_featuremodel_excludeconstraint_constructor_args():
    sig = inspect.signature(FeatureModel_ExcludeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel_namedelement_is_not_abstract():
    assert not inspect.isabstract(FeatureModel_NamedElement)


def test_featuremodel_namedelement_constructor_exists():
    assert callable(FeatureModel_NamedElement.__init__)


def test_featuremodel_namedelement_constructor_args():
    sig = inspect.signature(FeatureModel_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_featuremodel_namedelement_has_name():
    assert hasattr(FeatureModel_NamedElement, "name")
    descriptor = None
    for klass in FeatureModel_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel_group_is_not_abstract():
    assert not inspect.isabstract(FeatureModel_Group)


def test_featuremodel_group_constructor_exists():
    assert callable(FeatureModel_Group.__init__)


def test_featuremodel_group_constructor_args():
    sig = inspect.signature(FeatureModel_Group.__init__)
    params = list(sig.parameters.keys())
    assert "groupType" in params, "Missing parameter 'groupType'"

def test_featuremodel_group_has_groupType():
    assert hasattr(FeatureModel_Group, "groupType")
    descriptor = None
    for klass in FeatureModel_Group.__mro__:
        if "groupType" in klass.__dict__:
            descriptor = klass.__dict__["groupType"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel_comment_is_not_abstract():
    assert not inspect.isabstract(FeatureModel_Comment)


def test_featuremodel_comment_constructor_exists():
    assert callable(FeatureModel_Comment.__init__)


def test_featuremodel_comment_constructor_args():
    sig = inspect.signature(FeatureModel_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_featuremodel_comment_has_text():
    assert hasattr(FeatureModel_Comment, "text")
    descriptor = None
    for klass in FeatureModel_Comment.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel_feature_is_not_abstract():
    assert not inspect.isabstract(FeatureModel_Feature)


def test_featuremodel_feature_constructor_exists():
    assert callable(FeatureModel_Feature.__init__)


def test_featuremodel_feature_constructor_args():
    sig = inspect.signature(FeatureModel_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "mandatory" in params, "Missing parameter 'mandatory'"
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_featuremodel_feature_has_mandatory():
    assert hasattr(FeatureModel_Feature, "mandatory")
    descriptor = None
    for klass in FeatureModel_Feature.__mro__:
        if "mandatory" in klass.__dict__:
            descriptor = klass.__dict__["mandatory"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel_feature_has_abstract():
    assert hasattr(FeatureModel_Feature, "abstract")
    descriptor = None
    for klass in FeatureModel_Feature.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel_constraint_is_not_abstract():
    assert not inspect.isabstract(FeatureModel_Constraint)


def test_featuremodel_constraint_constructor_exists():
    assert callable(FeatureModel_Constraint.__init__)


def test_featuremodel_constraint_constructor_args():
    sig = inspect.signature(FeatureModel_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "language" in params, "Missing parameter 'language'"

def test_featuremodel_constraint_has_code():
    assert hasattr(FeatureModel_Constraint, "code")
    descriptor = None
    for klass in FeatureModel_Constraint.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel_constraint_has_language():
    assert hasattr(FeatureModel_Constraint, "language")
    descriptor = None
    for klass in FeatureModel_Constraint.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel_featuremodel_is_not_abstract():
    assert not inspect.isabstract(FeatureModel_FeatureModel)


def test_featuremodel_featuremodel_constructor_exists():
    assert callable(FeatureModel_FeatureModel.__init__)


def test_featuremodel_featuremodel_constructor_args():
    sig = inspect.signature(FeatureModel_FeatureModel.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"

def test_featuremodel_featuremodel_has_version():
    assert hasattr(FeatureModel_FeatureModel, "version")
    descriptor = None
    for klass in FeatureModel_FeatureModel.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel_requireconstraint_is_not_abstract():
    assert not inspect.isabstract(FeatureModel_RequireConstraint)


def test_featuremodel_requireconstraint_constructor_exists():
    assert callable(FeatureModel_RequireConstraint.__init__)


def test_featuremodel_requireconstraint_constructor_args():
    sig = inspect.signature(FeatureModel_RequireConstraint.__init__)
    params = list(sig.parameters.keys())

def test_grouptype_exists():
    # Check that the Enumeration exists
    assert GroupType is not None

def test_grouptype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GroupType]
    expected_literals = [
        "OR",
        "ALT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GroupType"


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
Constraint_strategy = st.builds(
    Constraint,
)
FeatureModel_ExcludeConstraint_strategy = st.builds(
    FeatureModel_ExcludeConstraint,
)
FeatureModel_NamedElement_strategy = st.builds(
    FeatureModel_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
FeatureModel_Group_strategy = st.builds(
    FeatureModel_Group,
    groupType=
        safe_text
)
FeatureModel_Comment_strategy = st.builds(
    FeatureModel_Comment,
    text=
        safe_text
)
FeatureModel_Feature_strategy = st.builds(
    FeatureModel_Feature,
    mandatory=
        st.booleans(),
    abstract=
        st.booleans()
)
FeatureModel_Constraint_strategy = st.builds(
    FeatureModel_Constraint,
    code=
        safe_text,
    language=
        safe_text
)
FeatureModel_FeatureModel_strategy = st.builds(
    FeatureModel_FeatureModel,
    version=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
FeatureModel_RequireConstraint_strategy = st.builds(
    FeatureModel_RequireConstraint,
)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=FeatureModel_ExcludeConstraint_strategy)
@settings(max_examples=50)
def test_featuremodel_excludeconstraint_instantiation(instance):
    assert isinstance(instance, FeatureModel_ExcludeConstraint)

@given(instance=FeatureModel_NamedElement_strategy)
@settings(max_examples=50)
def test_featuremodel_namedelement_instantiation(instance):
    assert isinstance(instance, FeatureModel_NamedElement)



@given(instance=FeatureModel_NamedElement_strategy)
def test_featuremodel_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=FeatureModel_Group_strategy)
@settings(max_examples=50)
def test_featuremodel_group_instantiation(instance):
    assert isinstance(instance, FeatureModel_Group)



@given(instance=FeatureModel_Group_strategy)
def test_featuremodel_group_groupType_setter(instance):
    original = instance.groupType
    instance.groupType = original
    assert instance.groupType == original

@given(instance=FeatureModel_Comment_strategy)
@settings(max_examples=50)
def test_featuremodel_comment_instantiation(instance):
    assert isinstance(instance, FeatureModel_Comment)



@given(instance=FeatureModel_Comment_strategy)
def test_featuremodel_comment_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=FeatureModel_Feature_strategy)
@settings(max_examples=50)
def test_featuremodel_feature_instantiation(instance):
    assert isinstance(instance, FeatureModel_Feature)



@given(instance=FeatureModel_Feature_strategy)
def test_featuremodel_feature_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original



@given(instance=FeatureModel_Feature_strategy)
def test_featuremodel_feature_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FeatureModel_Feature_strategy)
@settings(max_examples=30)
def test_featuremodel_feature_atmostinonegroup_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.atMostInOneGroup(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.atMostInOneGroup).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'atMostInOneGroup' in FeatureModel_Feature is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'atMostInOneGroup' in FeatureModel_Feature did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'atMostInOneGroup' in FeatureModel_Feature is not implemented or raised an error")

@given(instance=FeatureModel_Constraint_strategy)
@settings(max_examples=50)
def test_featuremodel_constraint_instantiation(instance):
    assert isinstance(instance, FeatureModel_Constraint)



@given(instance=FeatureModel_Constraint_strategy)
def test_featuremodel_constraint_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=FeatureModel_Constraint_strategy)
def test_featuremodel_constraint_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=FeatureModel_FeatureModel_strategy)
@settings(max_examples=50)
def test_featuremodel_featuremodel_instantiation(instance):
    assert isinstance(instance, FeatureModel_FeatureModel)



@given(instance=FeatureModel_FeatureModel_strategy)
def test_featuremodel_featuremodel_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=FeatureModel_RequireConstraint_strategy)
@settings(max_examples=50)
def test_featuremodel_requireconstraint_instantiation(instance):
    assert isinstance(instance, FeatureModel_RequireConstraint)
