import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Relation,
    featureModel_RelationFeature,
    featureModel_RelationFG,
    featureModel_Relation,
    featureModel_Project,
    featureModel_Node,
    featureModel_TypedValue,
    Node,
    featureModel_FeatureGroup,
    featureModel_Feature,
    ValueType,
    FeatureType,
    FeatureGroupType,
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



def test_featuremodel_relationfeature_is_not_abstract():
    assert not inspect.isabstract(featureModel_RelationFeature)


def test_featuremodel_relationfeature_constructor_exists():
    assert callable(featureModel_RelationFeature.__init__)


def test_featuremodel_relationfeature_constructor_args():
    sig = inspect.signature(featureModel_RelationFeature.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "type" in params, "Missing parameter 'type'"

def test_featuremodel_relationfeature_has_lowerBound():
    assert hasattr(featureModel_RelationFeature, "lowerBound")
    descriptor = None
    for klass in featureModel_RelationFeature.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel_relationfeature_has_upperBound():
    assert hasattr(featureModel_RelationFeature, "upperBound")
    descriptor = None
    for klass in featureModel_RelationFeature.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel_relationfeature_has_type():
    assert hasattr(featureModel_RelationFeature, "type")
    descriptor = None
    for klass in featureModel_RelationFeature.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel_relationfg_is_not_abstract():
    assert not inspect.isabstract(featureModel_RelationFG)


def test_featuremodel_relationfg_constructor_exists():
    assert callable(featureModel_RelationFG.__init__)


def test_featuremodel_relationfg_constructor_args():
    sig = inspect.signature(featureModel_RelationFG.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel_relation_is_not_abstract():
    assert not inspect.isabstract(featureModel_Relation)


def test_featuremodel_relation_constructor_exists():
    assert callable(featureModel_Relation.__init__)


def test_featuremodel_relation_constructor_args():
    sig = inspect.signature(featureModel_Relation.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel_project_is_not_abstract():
    assert not inspect.isabstract(featureModel_Project)


def test_featuremodel_project_constructor_exists():
    assert callable(featureModel_Project.__init__)


def test_featuremodel_project_constructor_args():
    sig = inspect.signature(featureModel_Project.__init__)
    params = list(sig.parameters.keys())
    assert "nameConstraintsFile" in params, "Missing parameter 'nameConstraintsFile'"
    assert "nameConfigFile" in params, "Missing parameter 'nameConfigFile'"
    assert "validatedOCL" in params, "Missing parameter 'validatedOCL'"
    assert "numberOfProducts" in params, "Missing parameter 'numberOfProducts'"
    assert "validatedTEF" in params, "Missing parameter 'validatedTEF'"

def test_featuremodel_project_has_nameConstraintsFile():
    assert hasattr(featureModel_Project, "nameConstraintsFile")
    descriptor = None
    for klass in featureModel_Project.__mro__:
        if "nameConstraintsFile" in klass.__dict__:
            descriptor = klass.__dict__["nameConstraintsFile"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel_project_has_nameConfigFile():
    assert hasattr(featureModel_Project, "nameConfigFile")
    descriptor = None
    for klass in featureModel_Project.__mro__:
        if "nameConfigFile" in klass.__dict__:
            descriptor = klass.__dict__["nameConfigFile"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel_project_has_validatedOCL():
    assert hasattr(featureModel_Project, "validatedOCL")
    descriptor = None
    for klass in featureModel_Project.__mro__:
        if "validatedOCL" in klass.__dict__:
            descriptor = klass.__dict__["validatedOCL"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel_project_has_numberOfProducts():
    assert hasattr(featureModel_Project, "numberOfProducts")
    descriptor = None
    for klass in featureModel_Project.__mro__:
        if "numberOfProducts" in klass.__dict__:
            descriptor = klass.__dict__["numberOfProducts"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel_project_has_validatedTEF():
    assert hasattr(featureModel_Project, "validatedTEF")
    descriptor = None
    for klass in featureModel_Project.__mro__:
        if "validatedTEF" in klass.__dict__:
            descriptor = klass.__dict__["validatedTEF"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel_node_is_not_abstract():
    assert not inspect.isabstract(featureModel_Node)


def test_featuremodel_node_constructor_exists():
    assert callable(featureModel_Node.__init__)


def test_featuremodel_node_constructor_args():
    sig = inspect.signature(featureModel_Node.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel_typedvalue_is_not_abstract():
    assert not inspect.isabstract(featureModel_TypedValue)


def test_featuremodel_typedvalue_constructor_exists():
    assert callable(featureModel_TypedValue.__init__)


def test_featuremodel_typedvalue_constructor_args():
    sig = inspect.signature(featureModel_TypedValue.__init__)
    params = list(sig.parameters.keys())
    assert "floatValue" in params, "Missing parameter 'floatValue'"
    assert "stringValue" in params, "Missing parameter 'stringValue'"
    assert "integerValue" in params, "Missing parameter 'integerValue'"

def test_featuremodel_typedvalue_has_floatValue():
    assert hasattr(featureModel_TypedValue, "floatValue")
    descriptor = None
    for klass in featureModel_TypedValue.__mro__:
        if "floatValue" in klass.__dict__:
            descriptor = klass.__dict__["floatValue"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel_typedvalue_has_stringValue():
    assert hasattr(featureModel_TypedValue, "stringValue")
    descriptor = None
    for klass in featureModel_TypedValue.__mro__:
        if "stringValue" in klass.__dict__:
            descriptor = klass.__dict__["stringValue"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel_typedvalue_has_integerValue():
    assert hasattr(featureModel_TypedValue, "integerValue")
    descriptor = None
    for klass in featureModel_TypedValue.__mro__:
        if "integerValue" in klass.__dict__:
            descriptor = klass.__dict__["integerValue"]
            break
    assert isinstance(descriptor, property)



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel_featuregroup_is_not_abstract():
    assert not inspect.isabstract(featureModel_FeatureGroup)


def test_featuremodel_featuregroup_constructor_exists():
    assert callable(featureModel_FeatureGroup.__init__)


def test_featuremodel_featuregroup_constructor_args():
    sig = inspect.signature(featureModel_FeatureGroup.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "type" in params, "Missing parameter 'type'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"

def test_featuremodel_featuregroup_has_upperBound():
    assert hasattr(featureModel_FeatureGroup, "upperBound")
    descriptor = None
    for klass in featureModel_FeatureGroup.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel_featuregroup_has_type():
    assert hasattr(featureModel_FeatureGroup, "type")
    descriptor = None
    for klass in featureModel_FeatureGroup.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel_featuregroup_has_lowerBound():
    assert hasattr(featureModel_FeatureGroup, "lowerBound")
    descriptor = None
    for klass in featureModel_FeatureGroup.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel_feature_is_not_abstract():
    assert not inspect.isabstract(featureModel_Feature)


def test_featuremodel_feature_constructor_exists():
    assert callable(featureModel_Feature.__init__)


def test_featuremodel_feature_constructor_args():
    sig = inspect.signature(featureModel_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "valueType" in params, "Missing parameter 'valueType'"
    assert "name" in params, "Missing parameter 'name'"

def test_featuremodel_feature_has_valueType():
    assert hasattr(featureModel_Feature, "valueType")
    descriptor = None
    for klass in featureModel_Feature.__mro__:
        if "valueType" in klass.__dict__:
            descriptor = klass.__dict__["valueType"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel_feature_has_name():
    assert hasattr(featureModel_Feature, "name")
    descriptor = None
    for klass in featureModel_Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_valuetype_exists():
    # Check that the Enumeration exists
    assert ValueType is not None

def test_valuetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ValueType]
    expected_literals = [
        "STRING",
        "NONE",
        "FEATURE",
        "FLOAT",
        "INTEGER",
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
        "MANDATORY",
        "SIMPLE",
        "OPTIONAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FeatureType"

def test_featuregrouptype_exists():
    # Check that the Enumeration exists
    assert FeatureGroupType is not None

def test_featuregrouptype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FeatureGroupType]
    expected_literals = [
        "ORGROUP",
        "SIMPLEGROUP",
        "XORGROUP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FeatureGroupType"


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
featureModel_RelationFeature_strategy = st.builds(
    featureModel_RelationFeature,
    lowerBound=
        st.integers(),
    upperBound=
        st.integers(),
    type=
        safe_text
)
featureModel_RelationFG_strategy = st.builds(
    featureModel_RelationFG,
)
featureModel_Relation_strategy = st.builds(
    featureModel_Relation,
)
featureModel_Project_strategy = st.builds(
    featureModel_Project,
    nameConstraintsFile=
        safe_text,
    nameConfigFile=
        safe_text,
    validatedOCL=
        st.booleans(),
    numberOfProducts=
        st.integers(),
    validatedTEF=
        st.booleans()
)
featureModel_Node_strategy = st.builds(
    featureModel_Node,
)
featureModel_TypedValue_strategy = st.builds(
    featureModel_TypedValue,
    floatValue=
        safe_text,
    stringValue=
        safe_text,
    integerValue=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
featureModel_FeatureGroup_strategy = st.builds(
    featureModel_FeatureGroup,
    upperBound=
        st.integers(),
    type=
        safe_text,
    lowerBound=
        st.integers()
)
featureModel_Feature_strategy = st.builds(
    featureModel_Feature,
    valueType=
        safe_text,
    name=
        safe_text
)

@given(instance=Relation_strategy)
@settings(max_examples=50)
def test_relation_instantiation(instance):
    assert isinstance(instance, Relation)

@given(instance=featureModel_RelationFeature_strategy)
@settings(max_examples=50)
def test_featuremodel_relationfeature_instantiation(instance):
    assert isinstance(instance, featureModel_RelationFeature)



@given(instance=featureModel_RelationFeature_strategy)
def test_featuremodel_relationfeature_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original



@given(instance=featureModel_RelationFeature_strategy)
def test_featuremodel_relationfeature_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original



@given(instance=featureModel_RelationFeature_strategy)
def test_featuremodel_relationfeature_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=featureModel_RelationFG_strategy)
@settings(max_examples=50)
def test_featuremodel_relationfg_instantiation(instance):
    assert isinstance(instance, featureModel_RelationFG)

@given(instance=featureModel_Relation_strategy)
@settings(max_examples=50)
def test_featuremodel_relation_instantiation(instance):
    assert isinstance(instance, featureModel_Relation)

@given(instance=featureModel_Project_strategy)
@settings(max_examples=50)
def test_featuremodel_project_instantiation(instance):
    assert isinstance(instance, featureModel_Project)



@given(instance=featureModel_Project_strategy)
def test_featuremodel_project_nameConstraintsFile_setter(instance):
    original = instance.nameConstraintsFile
    instance.nameConstraintsFile = original
    assert instance.nameConstraintsFile == original



@given(instance=featureModel_Project_strategy)
def test_featuremodel_project_nameConfigFile_setter(instance):
    original = instance.nameConfigFile
    instance.nameConfigFile = original
    assert instance.nameConfigFile == original



@given(instance=featureModel_Project_strategy)
def test_featuremodel_project_validatedOCL_setter(instance):
    original = instance.validatedOCL
    instance.validatedOCL = original
    assert instance.validatedOCL == original



@given(instance=featureModel_Project_strategy)
def test_featuremodel_project_numberOfProducts_setter(instance):
    original = instance.numberOfProducts
    instance.numberOfProducts = original
    assert instance.numberOfProducts == original



@given(instance=featureModel_Project_strategy)
def test_featuremodel_project_validatedTEF_setter(instance):
    original = instance.validatedTEF
    instance.validatedTEF = original
    assert instance.validatedTEF == original

@given(instance=featureModel_Node_strategy)
@settings(max_examples=50)
def test_featuremodel_node_instantiation(instance):
    assert isinstance(instance, featureModel_Node)

@given(instance=featureModel_TypedValue_strategy)
@settings(max_examples=50)
def test_featuremodel_typedvalue_instantiation(instance):
    assert isinstance(instance, featureModel_TypedValue)



@given(instance=featureModel_TypedValue_strategy)
def test_featuremodel_typedvalue_floatValue_setter(instance):
    original = instance.floatValue
    instance.floatValue = original
    assert instance.floatValue == original



@given(instance=featureModel_TypedValue_strategy)
def test_featuremodel_typedvalue_stringValue_setter(instance):
    original = instance.stringValue
    instance.stringValue = original
    assert instance.stringValue == original



@given(instance=featureModel_TypedValue_strategy)
def test_featuremodel_typedvalue_integerValue_setter(instance):
    original = instance.integerValue
    instance.integerValue = original
    assert instance.integerValue == original

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=featureModel_FeatureGroup_strategy)
@settings(max_examples=50)
def test_featuremodel_featuregroup_instantiation(instance):
    assert isinstance(instance, featureModel_FeatureGroup)



@given(instance=featureModel_FeatureGroup_strategy)
def test_featuremodel_featuregroup_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original



@given(instance=featureModel_FeatureGroup_strategy)
def test_featuremodel_featuregroup_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=featureModel_FeatureGroup_strategy)
def test_featuremodel_featuregroup_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=featureModel_Feature_strategy)
@settings(max_examples=50)
def test_featuremodel_feature_instantiation(instance):
    assert isinstance(instance, featureModel_Feature)



@given(instance=featureModel_Feature_strategy)
def test_featuremodel_feature_valueType_setter(instance):
    original = instance.valueType
    instance.valueType = original
    assert instance.valueType == original



@given(instance=featureModel_Feature_strategy)
def test_featuremodel_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
