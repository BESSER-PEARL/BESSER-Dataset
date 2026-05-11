import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Relation,
    specializationModel::RelationFeature,
    specializationModel::RelationFG,
    specializationModel::Node,
    specializationModel::TypedValue,
    Node,
    specializationModel::FeatureGroup,
    specializationModel::Relation,
    specializationModel::Project,
    specializationModel::Feature,
    ValueType,
    FeatureGroupType,
    ConfigState,
    FeatureType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_relation_is_not_abstract():
    assert not inspect.isabstract(Relation)


def test_relation_constructor_exists():
    assert callable(Relation.__init__)


def test_relation_constructor_args():
    sig = inspect.signature(Relation.__init__)
    params = list(sig.parameters.keys())



def test_specializationmodel::relationfeature_is_not_abstract():
    assert not inspect.isabstract(specializationModel::RelationFeature)


def test_specializationmodel::relationfeature_constructor_exists():
    assert callable(specializationModel::RelationFeature.__init__)


def test_specializationmodel::relationfeature_constructor_args():
    sig = inspect.signature(specializationModel::RelationFeature.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "type" in params, "Missing parameter 'type'"

def test_specializationmodel::relationfeature_has_upperBound():
    assert hasattr(specializationModel::RelationFeature, "upperBound")
    descriptor = None
    for klass in specializationModel::RelationFeature.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)

def test_specializationmodel::relationfeature_has_lowerBound():
    assert hasattr(specializationModel::RelationFeature, "lowerBound")
    descriptor = None
    for klass in specializationModel::RelationFeature.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_specializationmodel::relationfeature_has_type():
    assert hasattr(specializationModel::RelationFeature, "type")
    descriptor = None
    for klass in specializationModel::RelationFeature.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_specializationmodel::relationfg_is_not_abstract():
    assert not inspect.isabstract(specializationModel::RelationFG)


def test_specializationmodel::relationfg_constructor_exists():
    assert callable(specializationModel::RelationFG.__init__)


def test_specializationmodel::relationfg_constructor_args():
    sig = inspect.signature(specializationModel::RelationFG.__init__)
    params = list(sig.parameters.keys())



def test_specializationmodel::node_is_not_abstract():
    assert not inspect.isabstract(specializationModel::Node)


def test_specializationmodel::node_constructor_exists():
    assert callable(specializationModel::Node.__init__)


def test_specializationmodel::node_constructor_args():
    sig = inspect.signature(specializationModel::Node.__init__)
    params = list(sig.parameters.keys())



def test_specializationmodel::typedvalue_is_not_abstract():
    assert not inspect.isabstract(specializationModel::TypedValue)


def test_specializationmodel::typedvalue_constructor_exists():
    assert callable(specializationModel::TypedValue.__init__)


def test_specializationmodel::typedvalue_constructor_args():
    sig = inspect.signature(specializationModel::TypedValue.__init__)
    params = list(sig.parameters.keys())
    assert "integerValue" in params, "Missing parameter 'integerValue'"
    assert "stringValue" in params, "Missing parameter 'stringValue'"
    assert "floatValue" in params, "Missing parameter 'floatValue'"

def test_specializationmodel::typedvalue_has_integerValue():
    assert hasattr(specializationModel::TypedValue, "integerValue")
    descriptor = None
    for klass in specializationModel::TypedValue.__mro__:
        if "integerValue" in klass.__dict__:
            descriptor = klass.__dict__["integerValue"]
            break
    assert isinstance(descriptor, property)

def test_specializationmodel::typedvalue_has_stringValue():
    assert hasattr(specializationModel::TypedValue, "stringValue")
    descriptor = None
    for klass in specializationModel::TypedValue.__mro__:
        if "stringValue" in klass.__dict__:
            descriptor = klass.__dict__["stringValue"]
            break
    assert isinstance(descriptor, property)

def test_specializationmodel::typedvalue_has_floatValue():
    assert hasattr(specializationModel::TypedValue, "floatValue")
    descriptor = None
    for klass in specializationModel::TypedValue.__mro__:
        if "floatValue" in klass.__dict__:
            descriptor = klass.__dict__["floatValue"]
            break
    assert isinstance(descriptor, property)



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_specializationmodel::featuregroup_is_not_abstract():
    assert not inspect.isabstract(specializationModel::FeatureGroup)


def test_specializationmodel::featuregroup_constructor_exists():
    assert callable(specializationModel::FeatureGroup.__init__)


def test_specializationmodel::featuregroup_constructor_args():
    sig = inspect.signature(specializationModel::FeatureGroup.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "type" in params, "Missing parameter 'type'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_specializationmodel::featuregroup_has_lowerBound():
    assert hasattr(specializationModel::FeatureGroup, "lowerBound")
    descriptor = None
    for klass in specializationModel::FeatureGroup.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_specializationmodel::featuregroup_has_type():
    assert hasattr(specializationModel::FeatureGroup, "type")
    descriptor = None
    for klass in specializationModel::FeatureGroup.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_specializationmodel::featuregroup_has_upperBound():
    assert hasattr(specializationModel::FeatureGroup, "upperBound")
    descriptor = None
    for klass in specializationModel::FeatureGroup.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_specializationmodel::relation_is_not_abstract():
    assert not inspect.isabstract(specializationModel::Relation)


def test_specializationmodel::relation_constructor_exists():
    assert callable(specializationModel::Relation.__init__)


def test_specializationmodel::relation_constructor_args():
    sig = inspect.signature(specializationModel::Relation.__init__)
    params = list(sig.parameters.keys())



def test_specializationmodel::project_is_not_abstract():
    assert not inspect.isabstract(specializationModel::Project)


def test_specializationmodel::project_constructor_exists():
    assert callable(specializationModel::Project.__init__)


def test_specializationmodel::project_constructor_args():
    sig = inspect.signature(specializationModel::Project.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfProducts" in params, "Missing parameter 'numberOfProducts'"
    assert "infiniteDomain" in params, "Missing parameter 'infiniteDomain'"
    assert "featureModelURI" in params, "Missing parameter 'featureModelURI'"
    assert "nameConfigFile" in params, "Missing parameter 'nameConfigFile'"
    assert "nameConstraintsFile" in params, "Missing parameter 'nameConstraintsFile'"
    assert "userConstraintsState" in params, "Missing parameter 'userConstraintsState'"

def test_specializationmodel::project_has_numberOfProducts():
    assert hasattr(specializationModel::Project, "numberOfProducts")
    descriptor = None
    for klass in specializationModel::Project.__mro__:
        if "numberOfProducts" in klass.__dict__:
            descriptor = klass.__dict__["numberOfProducts"]
            break
    assert isinstance(descriptor, property)

def test_specializationmodel::project_has_infiniteDomain():
    assert hasattr(specializationModel::Project, "infiniteDomain")
    descriptor = None
    for klass in specializationModel::Project.__mro__:
        if "infiniteDomain" in klass.__dict__:
            descriptor = klass.__dict__["infiniteDomain"]
            break
    assert isinstance(descriptor, property)

def test_specializationmodel::project_has_featureModelURI():
    assert hasattr(specializationModel::Project, "featureModelURI")
    descriptor = None
    for klass in specializationModel::Project.__mro__:
        if "featureModelURI" in klass.__dict__:
            descriptor = klass.__dict__["featureModelURI"]
            break
    assert isinstance(descriptor, property)

def test_specializationmodel::project_has_nameConfigFile():
    assert hasattr(specializationModel::Project, "nameConfigFile")
    descriptor = None
    for klass in specializationModel::Project.__mro__:
        if "nameConfigFile" in klass.__dict__:
            descriptor = klass.__dict__["nameConfigFile"]
            break
    assert isinstance(descriptor, property)

def test_specializationmodel::project_has_nameConstraintsFile():
    assert hasattr(specializationModel::Project, "nameConstraintsFile")
    descriptor = None
    for klass in specializationModel::Project.__mro__:
        if "nameConstraintsFile" in klass.__dict__:
            descriptor = klass.__dict__["nameConstraintsFile"]
            break
    assert isinstance(descriptor, property)

def test_specializationmodel::project_has_userConstraintsState():
    assert hasattr(specializationModel::Project, "userConstraintsState")
    descriptor = None
    for klass in specializationModel::Project.__mro__:
        if "userConstraintsState" in klass.__dict__:
            descriptor = klass.__dict__["userConstraintsState"]
            break
    assert isinstance(descriptor, property)



def test_specializationmodel::feature_is_not_abstract():
    assert not inspect.isabstract(specializationModel::Feature)


def test_specializationmodel::feature_constructor_exists():
    assert callable(specializationModel::Feature.__init__)


def test_specializationmodel::feature_constructor_args():
    sig = inspect.signature(specializationModel::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "realName" in params, "Missing parameter 'realName'"
    assert "state" in params, "Missing parameter 'state'"
    assert "name" in params, "Missing parameter 'name'"
    assert "valueType" in params, "Missing parameter 'valueType'"

def test_specializationmodel::feature_has_realName():
    assert hasattr(specializationModel::Feature, "realName")
    descriptor = None
    for klass in specializationModel::Feature.__mro__:
        if "realName" in klass.__dict__:
            descriptor = klass.__dict__["realName"]
            break
    assert isinstance(descriptor, property)

def test_specializationmodel::feature_has_state():
    assert hasattr(specializationModel::Feature, "state")
    descriptor = None
    for klass in specializationModel::Feature.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_specializationmodel::feature_has_name():
    assert hasattr(specializationModel::Feature, "name")
    descriptor = None
    for klass in specializationModel::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_specializationmodel::feature_has_valueType():
    assert hasattr(specializationModel::Feature, "valueType")
    descriptor = None
    for klass in specializationModel::Feature.__mro__:
        if "valueType" in klass.__dict__:
            descriptor = klass.__dict__["valueType"]
            break
    assert isinstance(descriptor, property)

def test_valuetype_exists():
    # Check that the Enumeration exists
    assert ValueType is not None

def test_valuetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ValueType]
    expected_literals = [
        "FLOAT",
        "STRING",
        "FEATURE",
        "INTEGER",
        "NONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ValueType"

def test_featuregrouptype_exists():
    # Check that the Enumeration exists
    assert FeatureGroupType is not None

def test_featuregrouptype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FeatureGroupType]
    expected_literals = [
        "SIMPLEGROUP",
        "ORGROUP",
        "XORGROUP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FeatureGroupType"

def test_configstate_exists():
    # Check that the Enumeration exists
    assert ConfigState is not None

def test_configstate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConfigState]
    expected_literals = [
        "UNDECIDED",
        "USER_ELIMINATED",
        "USER_SELECTED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConfigState"

def test_featuretype_exists():
    # Check that the Enumeration exists
    assert FeatureType is not None

def test_featuretype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FeatureType]
    expected_literals = [
        "MANDATORY",
        "OPTIONAL",
        "SIMPLE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FeatureType"


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
Relation_strategy = st.builds(
    Relation,
)
specializationModel::RelationFeature_strategy = st.builds(
    specializationModel::RelationFeature,
    upperBound=
        st.integers(),
    lowerBound=
        st.integers(),
    type=
        safe_text
)
specializationModel::RelationFG_strategy = st.builds(
    specializationModel::RelationFG,
)
specializationModel::Node_strategy = st.builds(
    specializationModel::Node,
)
specializationModel::TypedValue_strategy = st.builds(
    specializationModel::TypedValue,
    integerValue=
        safe_text,
    stringValue=
        safe_text,
    floatValue=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
specializationModel::FeatureGroup_strategy = st.builds(
    specializationModel::FeatureGroup,
    lowerBound=
        st.integers(),
    type=
        safe_text,
    upperBound=
        st.integers()
)
specializationModel::Relation_strategy = st.builds(
    specializationModel::Relation,
)
specializationModel::Project_strategy = st.builds(
    specializationModel::Project,
    numberOfProducts=
        st.integers(),
    infiniteDomain=
        st.booleans(),
    featureModelURI=
        safe_text,
    nameConfigFile=
        safe_text,
    nameConstraintsFile=
        safe_text,
    userConstraintsState=
        st.booleans()
)
specializationModel::Feature_strategy = st.builds(
    specializationModel::Feature,
    realName=
        safe_text,
    state=
        safe_text,
    name=
        safe_text,
    valueType=
        safe_text
)

@given(instance=Relation_strategy)
@settings(max_examples=50)
def test_relation_instantiation(instance):
    assert isinstance(instance, Relation)

@given(instance=specializationModel::RelationFeature_strategy)
@settings(max_examples=50)
def test_specializationmodel::relationfeature_instantiation(instance):
    assert isinstance(instance, specializationModel::RelationFeature)

@given(instance=specializationModel::RelationFeature_strategy)
def test_specializationmodel::relationfeature_upperBound_type(instance):
    assert isinstance(instance.upperBound, int)


@given(instance=specializationModel::RelationFeature_strategy)
def test_specializationmodel::relationfeature_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=specializationModel::RelationFeature_strategy)
def test_specializationmodel::relationfeature_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, int)


@given(instance=specializationModel::RelationFeature_strategy)
def test_specializationmodel::relationfeature_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=specializationModel::RelationFeature_strategy)
def test_specializationmodel::relationfeature_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=specializationModel::RelationFeature_strategy)
def test_specializationmodel::relationfeature_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=specializationModel::RelationFG_strategy)
@settings(max_examples=50)
def test_specializationmodel::relationfg_instantiation(instance):
    assert isinstance(instance, specializationModel::RelationFG)

@given(instance=specializationModel::Node_strategy)
@settings(max_examples=50)
def test_specializationmodel::node_instantiation(instance):
    assert isinstance(instance, specializationModel::Node)

@given(instance=specializationModel::TypedValue_strategy)
@settings(max_examples=50)
def test_specializationmodel::typedvalue_instantiation(instance):
    assert isinstance(instance, specializationModel::TypedValue)

@given(instance=specializationModel::TypedValue_strategy)
def test_specializationmodel::typedvalue_integerValue_type(instance):
    assert isinstance(instance.integerValue, str)


@given(instance=specializationModel::TypedValue_strategy)
def test_specializationmodel::typedvalue_integerValue_setter(instance):
    original = instance.integerValue
    instance.integerValue = original
    assert instance.integerValue == original

@given(instance=specializationModel::TypedValue_strategy)
def test_specializationmodel::typedvalue_stringValue_type(instance):
    assert isinstance(instance.stringValue, str)


@given(instance=specializationModel::TypedValue_strategy)
def test_specializationmodel::typedvalue_stringValue_setter(instance):
    original = instance.stringValue
    instance.stringValue = original
    assert instance.stringValue == original

@given(instance=specializationModel::TypedValue_strategy)
def test_specializationmodel::typedvalue_floatValue_type(instance):
    assert isinstance(instance.floatValue, str)


@given(instance=specializationModel::TypedValue_strategy)
def test_specializationmodel::typedvalue_floatValue_setter(instance):
    original = instance.floatValue
    instance.floatValue = original
    assert instance.floatValue == original

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=specializationModel::FeatureGroup_strategy)
@settings(max_examples=50)
def test_specializationmodel::featuregroup_instantiation(instance):
    assert isinstance(instance, specializationModel::FeatureGroup)

@given(instance=specializationModel::FeatureGroup_strategy)
def test_specializationmodel::featuregroup_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, int)


@given(instance=specializationModel::FeatureGroup_strategy)
def test_specializationmodel::featuregroup_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=specializationModel::FeatureGroup_strategy)
def test_specializationmodel::featuregroup_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=specializationModel::FeatureGroup_strategy)
def test_specializationmodel::featuregroup_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=specializationModel::FeatureGroup_strategy)
def test_specializationmodel::featuregroup_upperBound_type(instance):
    assert isinstance(instance.upperBound, int)


@given(instance=specializationModel::FeatureGroup_strategy)
def test_specializationmodel::featuregroup_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=specializationModel::Relation_strategy)
@settings(max_examples=50)
def test_specializationmodel::relation_instantiation(instance):
    assert isinstance(instance, specializationModel::Relation)

@given(instance=specializationModel::Project_strategy)
@settings(max_examples=50)
def test_specializationmodel::project_instantiation(instance):
    assert isinstance(instance, specializationModel::Project)

@given(instance=specializationModel::Project_strategy)
def test_specializationmodel::project_numberOfProducts_type(instance):
    assert isinstance(instance.numberOfProducts, int)


@given(instance=specializationModel::Project_strategy)
def test_specializationmodel::project_numberOfProducts_setter(instance):
    original = instance.numberOfProducts
    instance.numberOfProducts = original
    assert instance.numberOfProducts == original

@given(instance=specializationModel::Project_strategy)
def test_specializationmodel::project_infiniteDomain_type(instance):
    assert isinstance(instance.infiniteDomain, bool)


@given(instance=specializationModel::Project_strategy)
def test_specializationmodel::project_infiniteDomain_setter(instance):
    original = instance.infiniteDomain
    instance.infiniteDomain = original
    assert instance.infiniteDomain == original

@given(instance=specializationModel::Project_strategy)
def test_specializationmodel::project_featureModelURI_type(instance):
    assert isinstance(instance.featureModelURI, str)


@given(instance=specializationModel::Project_strategy)
def test_specializationmodel::project_featureModelURI_setter(instance):
    original = instance.featureModelURI
    instance.featureModelURI = original
    assert instance.featureModelURI == original

@given(instance=specializationModel::Project_strategy)
def test_specializationmodel::project_nameConfigFile_type(instance):
    assert isinstance(instance.nameConfigFile, str)


@given(instance=specializationModel::Project_strategy)
def test_specializationmodel::project_nameConfigFile_setter(instance):
    original = instance.nameConfigFile
    instance.nameConfigFile = original
    assert instance.nameConfigFile == original

@given(instance=specializationModel::Project_strategy)
def test_specializationmodel::project_nameConstraintsFile_type(instance):
    assert isinstance(instance.nameConstraintsFile, str)


@given(instance=specializationModel::Project_strategy)
def test_specializationmodel::project_nameConstraintsFile_setter(instance):
    original = instance.nameConstraintsFile
    instance.nameConstraintsFile = original
    assert instance.nameConstraintsFile == original

@given(instance=specializationModel::Project_strategy)
def test_specializationmodel::project_userConstraintsState_type(instance):
    assert isinstance(instance.userConstraintsState, bool)


@given(instance=specializationModel::Project_strategy)
def test_specializationmodel::project_userConstraintsState_setter(instance):
    original = instance.userConstraintsState
    instance.userConstraintsState = original
    assert instance.userConstraintsState == original

@given(instance=specializationModel::Feature_strategy)
@settings(max_examples=50)
def test_specializationmodel::feature_instantiation(instance):
    assert isinstance(instance, specializationModel::Feature)

@given(instance=specializationModel::Feature_strategy)
def test_specializationmodel::feature_realName_type(instance):
    assert isinstance(instance.realName, str)


@given(instance=specializationModel::Feature_strategy)
def test_specializationmodel::feature_realName_setter(instance):
    original = instance.realName
    instance.realName = original
    assert instance.realName == original

@given(instance=specializationModel::Feature_strategy)
def test_specializationmodel::feature_state_type(instance):
    assert isinstance(instance.state, str)


@given(instance=specializationModel::Feature_strategy)
def test_specializationmodel::feature_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=specializationModel::Feature_strategy)
def test_specializationmodel::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=specializationModel::Feature_strategy)
def test_specializationmodel::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=specializationModel::Feature_strategy)
def test_specializationmodel::feature_valueType_type(instance):
    assert isinstance(instance.valueType, str)


@given(instance=specializationModel::Feature_strategy)
def test_specializationmodel::feature_valueType_setter(instance):
    original = instance.valueType
    instance.valueType = original
    assert instance.valueType == original
