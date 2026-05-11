import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Relation,
    featureModel::RelationFeature,
    featureModel::RelationFG,
    featureModel::Relation,
    featureModel::Project,
    featureModel::Node,
    featureModel::TypedValue,
    Node,
    featureModel::FeatureGroup,
    featureModel::Feature,
    FeatureGroupType,
    ValueType,
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



def test_featuremodel::relationfeature_is_not_abstract():
    assert not inspect.isabstract(featureModel::RelationFeature)


def test_featuremodel::relationfeature_constructor_exists():
    assert callable(featureModel::RelationFeature.__init__)


def test_featuremodel::relationfeature_constructor_args():
    sig = inspect.signature(featureModel::RelationFeature.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "type" in params, "Missing parameter 'type'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_featuremodel::relationfeature_has_lowerBound():
    assert hasattr(featureModel::RelationFeature, "lowerBound")
    descriptor = None
    for klass in featureModel::RelationFeature.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel::relationfeature_has_type():
    assert hasattr(featureModel::RelationFeature, "type")
    descriptor = None
    for klass in featureModel::RelationFeature.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel::relationfeature_has_upperBound():
    assert hasattr(featureModel::RelationFeature, "upperBound")
    descriptor = None
    for klass in featureModel::RelationFeature.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel::relationfg_is_not_abstract():
    assert not inspect.isabstract(featureModel::RelationFG)


def test_featuremodel::relationfg_constructor_exists():
    assert callable(featureModel::RelationFG.__init__)


def test_featuremodel::relationfg_constructor_args():
    sig = inspect.signature(featureModel::RelationFG.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::relation_is_not_abstract():
    assert not inspect.isabstract(featureModel::Relation)


def test_featuremodel::relation_constructor_exists():
    assert callable(featureModel::Relation.__init__)


def test_featuremodel::relation_constructor_args():
    sig = inspect.signature(featureModel::Relation.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::project_is_not_abstract():
    assert not inspect.isabstract(featureModel::Project)


def test_featuremodel::project_constructor_exists():
    assert callable(featureModel::Project.__init__)


def test_featuremodel::project_constructor_args():
    sig = inspect.signature(featureModel::Project.__init__)
    params = list(sig.parameters.keys())
    assert "nameConfigFile" in params, "Missing parameter 'nameConfigFile'"
    assert "nameConstraintsFile" in params, "Missing parameter 'nameConstraintsFile'"
    assert "numberOfProducts" in params, "Missing parameter 'numberOfProducts'"
    assert "validatedTEF" in params, "Missing parameter 'validatedTEF'"
    assert "validatedOCL" in params, "Missing parameter 'validatedOCL'"

def test_featuremodel::project_has_nameConfigFile():
    assert hasattr(featureModel::Project, "nameConfigFile")
    descriptor = None
    for klass in featureModel::Project.__mro__:
        if "nameConfigFile" in klass.__dict__:
            descriptor = klass.__dict__["nameConfigFile"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel::project_has_nameConstraintsFile():
    assert hasattr(featureModel::Project, "nameConstraintsFile")
    descriptor = None
    for klass in featureModel::Project.__mro__:
        if "nameConstraintsFile" in klass.__dict__:
            descriptor = klass.__dict__["nameConstraintsFile"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel::project_has_numberOfProducts():
    assert hasattr(featureModel::Project, "numberOfProducts")
    descriptor = None
    for klass in featureModel::Project.__mro__:
        if "numberOfProducts" in klass.__dict__:
            descriptor = klass.__dict__["numberOfProducts"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel::project_has_validatedTEF():
    assert hasattr(featureModel::Project, "validatedTEF")
    descriptor = None
    for klass in featureModel::Project.__mro__:
        if "validatedTEF" in klass.__dict__:
            descriptor = klass.__dict__["validatedTEF"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel::project_has_validatedOCL():
    assert hasattr(featureModel::Project, "validatedOCL")
    descriptor = None
    for klass in featureModel::Project.__mro__:
        if "validatedOCL" in klass.__dict__:
            descriptor = klass.__dict__["validatedOCL"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel::node_is_not_abstract():
    assert not inspect.isabstract(featureModel::Node)


def test_featuremodel::node_constructor_exists():
    assert callable(featureModel::Node.__init__)


def test_featuremodel::node_constructor_args():
    sig = inspect.signature(featureModel::Node.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::typedvalue_is_not_abstract():
    assert not inspect.isabstract(featureModel::TypedValue)


def test_featuremodel::typedvalue_constructor_exists():
    assert callable(featureModel::TypedValue.__init__)


def test_featuremodel::typedvalue_constructor_args():
    sig = inspect.signature(featureModel::TypedValue.__init__)
    params = list(sig.parameters.keys())
    assert "integerValue" in params, "Missing parameter 'integerValue'"
    assert "floatValue" in params, "Missing parameter 'floatValue'"
    assert "stringValue" in params, "Missing parameter 'stringValue'"

def test_featuremodel::typedvalue_has_integerValue():
    assert hasattr(featureModel::TypedValue, "integerValue")
    descriptor = None
    for klass in featureModel::TypedValue.__mro__:
        if "integerValue" in klass.__dict__:
            descriptor = klass.__dict__["integerValue"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel::typedvalue_has_floatValue():
    assert hasattr(featureModel::TypedValue, "floatValue")
    descriptor = None
    for klass in featureModel::TypedValue.__mro__:
        if "floatValue" in klass.__dict__:
            descriptor = klass.__dict__["floatValue"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel::typedvalue_has_stringValue():
    assert hasattr(featureModel::TypedValue, "stringValue")
    descriptor = None
    for klass in featureModel::TypedValue.__mro__:
        if "stringValue" in klass.__dict__:
            descriptor = klass.__dict__["stringValue"]
            break
    assert isinstance(descriptor, property)



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::featuregroup_is_not_abstract():
    assert not inspect.isabstract(featureModel::FeatureGroup)


def test_featuremodel::featuregroup_constructor_exists():
    assert callable(featureModel::FeatureGroup.__init__)


def test_featuremodel::featuregroup_constructor_args():
    sig = inspect.signature(featureModel::FeatureGroup.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "type" in params, "Missing parameter 'type'"

def test_featuremodel::featuregroup_has_lowerBound():
    assert hasattr(featureModel::FeatureGroup, "lowerBound")
    descriptor = None
    for klass in featureModel::FeatureGroup.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel::featuregroup_has_upperBound():
    assert hasattr(featureModel::FeatureGroup, "upperBound")
    descriptor = None
    for klass in featureModel::FeatureGroup.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel::featuregroup_has_type():
    assert hasattr(featureModel::FeatureGroup, "type")
    descriptor = None
    for klass in featureModel::FeatureGroup.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel::feature_is_not_abstract():
    assert not inspect.isabstract(featureModel::Feature)


def test_featuremodel::feature_constructor_exists():
    assert callable(featureModel::Feature.__init__)


def test_featuremodel::feature_constructor_args():
    sig = inspect.signature(featureModel::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "valueType" in params, "Missing parameter 'valueType'"
    assert "name" in params, "Missing parameter 'name'"

def test_featuremodel::feature_has_valueType():
    assert hasattr(featureModel::Feature, "valueType")
    descriptor = None
    for klass in featureModel::Feature.__mro__:
        if "valueType" in klass.__dict__:
            descriptor = klass.__dict__["valueType"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel::feature_has_name():
    assert hasattr(featureModel::Feature, "name")
    descriptor = None
    for klass in featureModel::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

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

def test_valuetype_exists():
    # Check that the Enumeration exists
    assert ValueType is not None

def test_valuetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ValueType]
    expected_literals = [
        "FLOAT",
        "INTEGER",
        "NONE",
        "STRING",
        "FEATURE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ValueType"

def test_featuretype_exists():
    # Check that the Enumeration exists
    assert FeatureType is not None

def test_featuretype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FeatureType]
    expected_literals = [
        "OPTIONAL",
        "MANDATORY",
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
featureModel::RelationFeature_strategy = st.builds(
    featureModel::RelationFeature,
    lowerBound=
        st.integers(),
    type=
        safe_text,
    upperBound=
        st.integers()
)
featureModel::RelationFG_strategy = st.builds(
    featureModel::RelationFG,
)
featureModel::Relation_strategy = st.builds(
    featureModel::Relation,
)
featureModel::Project_strategy = st.builds(
    featureModel::Project,
    nameConfigFile=
        safe_text,
    nameConstraintsFile=
        safe_text,
    numberOfProducts=
        st.integers(),
    validatedTEF=
        st.booleans(),
    validatedOCL=
        st.booleans()
)
featureModel::Node_strategy = st.builds(
    featureModel::Node,
)
featureModel::TypedValue_strategy = st.builds(
    featureModel::TypedValue,
    integerValue=
        safe_text,
    floatValue=
        safe_text,
    stringValue=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
featureModel::FeatureGroup_strategy = st.builds(
    featureModel::FeatureGroup,
    lowerBound=
        st.integers(),
    upperBound=
        st.integers(),
    type=
        safe_text
)
featureModel::Feature_strategy = st.builds(
    featureModel::Feature,
    valueType=
        safe_text,
    name=
        safe_text
)

@given(instance=Relation_strategy)
@settings(max_examples=50)
def test_relation_instantiation(instance):
    assert isinstance(instance, Relation)

@given(instance=featureModel::RelationFeature_strategy)
@settings(max_examples=50)
def test_featuremodel::relationfeature_instantiation(instance):
    assert isinstance(instance, featureModel::RelationFeature)

@given(instance=featureModel::RelationFeature_strategy)
def test_featuremodel::relationfeature_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, int)


@given(instance=featureModel::RelationFeature_strategy)
def test_featuremodel::relationfeature_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=featureModel::RelationFeature_strategy)
def test_featuremodel::relationfeature_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=featureModel::RelationFeature_strategy)
def test_featuremodel::relationfeature_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=featureModel::RelationFeature_strategy)
def test_featuremodel::relationfeature_upperBound_type(instance):
    assert isinstance(instance.upperBound, int)


@given(instance=featureModel::RelationFeature_strategy)
def test_featuremodel::relationfeature_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=featureModel::RelationFG_strategy)
@settings(max_examples=50)
def test_featuremodel::relationfg_instantiation(instance):
    assert isinstance(instance, featureModel::RelationFG)

@given(instance=featureModel::Relation_strategy)
@settings(max_examples=50)
def test_featuremodel::relation_instantiation(instance):
    assert isinstance(instance, featureModel::Relation)

@given(instance=featureModel::Project_strategy)
@settings(max_examples=50)
def test_featuremodel::project_instantiation(instance):
    assert isinstance(instance, featureModel::Project)

@given(instance=featureModel::Project_strategy)
def test_featuremodel::project_nameConfigFile_type(instance):
    assert isinstance(instance.nameConfigFile, str)


@given(instance=featureModel::Project_strategy)
def test_featuremodel::project_nameConfigFile_setter(instance):
    original = instance.nameConfigFile
    instance.nameConfigFile = original
    assert instance.nameConfigFile == original

@given(instance=featureModel::Project_strategy)
def test_featuremodel::project_nameConstraintsFile_type(instance):
    assert isinstance(instance.nameConstraintsFile, str)


@given(instance=featureModel::Project_strategy)
def test_featuremodel::project_nameConstraintsFile_setter(instance):
    original = instance.nameConstraintsFile
    instance.nameConstraintsFile = original
    assert instance.nameConstraintsFile == original

@given(instance=featureModel::Project_strategy)
def test_featuremodel::project_numberOfProducts_type(instance):
    assert isinstance(instance.numberOfProducts, int)


@given(instance=featureModel::Project_strategy)
def test_featuremodel::project_numberOfProducts_setter(instance):
    original = instance.numberOfProducts
    instance.numberOfProducts = original
    assert instance.numberOfProducts == original

@given(instance=featureModel::Project_strategy)
def test_featuremodel::project_validatedTEF_type(instance):
    assert isinstance(instance.validatedTEF, bool)


@given(instance=featureModel::Project_strategy)
def test_featuremodel::project_validatedTEF_setter(instance):
    original = instance.validatedTEF
    instance.validatedTEF = original
    assert instance.validatedTEF == original

@given(instance=featureModel::Project_strategy)
def test_featuremodel::project_validatedOCL_type(instance):
    assert isinstance(instance.validatedOCL, bool)


@given(instance=featureModel::Project_strategy)
def test_featuremodel::project_validatedOCL_setter(instance):
    original = instance.validatedOCL
    instance.validatedOCL = original
    assert instance.validatedOCL == original

@given(instance=featureModel::Node_strategy)
@settings(max_examples=50)
def test_featuremodel::node_instantiation(instance):
    assert isinstance(instance, featureModel::Node)

@given(instance=featureModel::TypedValue_strategy)
@settings(max_examples=50)
def test_featuremodel::typedvalue_instantiation(instance):
    assert isinstance(instance, featureModel::TypedValue)

@given(instance=featureModel::TypedValue_strategy)
def test_featuremodel::typedvalue_integerValue_type(instance):
    assert isinstance(instance.integerValue, str)


@given(instance=featureModel::TypedValue_strategy)
def test_featuremodel::typedvalue_integerValue_setter(instance):
    original = instance.integerValue
    instance.integerValue = original
    assert instance.integerValue == original

@given(instance=featureModel::TypedValue_strategy)
def test_featuremodel::typedvalue_floatValue_type(instance):
    assert isinstance(instance.floatValue, str)


@given(instance=featureModel::TypedValue_strategy)
def test_featuremodel::typedvalue_floatValue_setter(instance):
    original = instance.floatValue
    instance.floatValue = original
    assert instance.floatValue == original

@given(instance=featureModel::TypedValue_strategy)
def test_featuremodel::typedvalue_stringValue_type(instance):
    assert isinstance(instance.stringValue, str)


@given(instance=featureModel::TypedValue_strategy)
def test_featuremodel::typedvalue_stringValue_setter(instance):
    original = instance.stringValue
    instance.stringValue = original
    assert instance.stringValue == original

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=featureModel::FeatureGroup_strategy)
@settings(max_examples=50)
def test_featuremodel::featuregroup_instantiation(instance):
    assert isinstance(instance, featureModel::FeatureGroup)

@given(instance=featureModel::FeatureGroup_strategy)
def test_featuremodel::featuregroup_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, int)


@given(instance=featureModel::FeatureGroup_strategy)
def test_featuremodel::featuregroup_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=featureModel::FeatureGroup_strategy)
def test_featuremodel::featuregroup_upperBound_type(instance):
    assert isinstance(instance.upperBound, int)


@given(instance=featureModel::FeatureGroup_strategy)
def test_featuremodel::featuregroup_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=featureModel::FeatureGroup_strategy)
def test_featuremodel::featuregroup_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=featureModel::FeatureGroup_strategy)
def test_featuremodel::featuregroup_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=featureModel::Feature_strategy)
@settings(max_examples=50)
def test_featuremodel::feature_instantiation(instance):
    assert isinstance(instance, featureModel::Feature)

@given(instance=featureModel::Feature_strategy)
def test_featuremodel::feature_valueType_type(instance):
    assert isinstance(instance.valueType, str)


@given(instance=featureModel::Feature_strategy)
def test_featuremodel::feature_valueType_setter(instance):
    original = instance.valueType
    instance.valueType = original
    assert instance.valueType == original

@given(instance=featureModel::Feature_strategy)
def test_featuremodel::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=featureModel::Feature_strategy)
def test_featuremodel::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
