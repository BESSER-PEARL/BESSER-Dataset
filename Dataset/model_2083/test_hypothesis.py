import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    UATMM::structure::Connector,
    Connector,
    UATMM::structure::Spare,
    UATMM::structure::SAND,
    UATMM::structure::SOR,
    UATMM::structure::Weighted,
    UATMM::structure::XOR,
    UATMM::structure::PAND,
    UATMM::structure::OR,
    UATMM::structure::FDEP,
    UATMM::structure::KofN,
    UATMM::structure::TAND,
    UATMM::structure::AND,
    UATMM::structure::Node,
    UATMM::structure::AttackTree,
    UATMM::structure::TreeMetaData,
    UATMM::structure::Edge,
    UATMM::structure::RDEP,
    EdgeKind,
    RoleType,
    Nature,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uatmm::structure::connector_is_not_abstract():
    assert not inspect.isabstract(UATMM::structure::Connector)


def test_uatmm::structure::connector_constructor_exists():
    assert callable(UATMM::structure::Connector.__init__)


def test_uatmm::structure::connector_constructor_args():
    sig = inspect.signature(UATMM::structure::Connector.__init__)
    params = list(sig.parameters.keys())



def test_connector_is_not_abstract():
    assert not inspect.isabstract(Connector)


def test_connector_constructor_exists():
    assert callable(Connector.__init__)


def test_connector_constructor_args():
    sig = inspect.signature(Connector.__init__)
    params = list(sig.parameters.keys())



def test_uatmm::structure::spare_is_not_abstract():
    assert not inspect.isabstract(UATMM::structure::Spare)


def test_uatmm::structure::spare_constructor_exists():
    assert callable(UATMM::structure::Spare.__init__)


def test_uatmm::structure::spare_constructor_args():
    sig = inspect.signature(UATMM::structure::Spare.__init__)
    params = list(sig.parameters.keys())



def test_uatmm::structure::sand_is_not_abstract():
    assert not inspect.isabstract(UATMM::structure::SAND)


def test_uatmm::structure::sand_constructor_exists():
    assert callable(UATMM::structure::SAND.__init__)


def test_uatmm::structure::sand_constructor_args():
    sig = inspect.signature(UATMM::structure::SAND.__init__)
    params = list(sig.parameters.keys())



def test_uatmm::structure::sor_is_not_abstract():
    assert not inspect.isabstract(UATMM::structure::SOR)


def test_uatmm::structure::sor_constructor_exists():
    assert callable(UATMM::structure::SOR.__init__)


def test_uatmm::structure::sor_constructor_args():
    sig = inspect.signature(UATMM::structure::SOR.__init__)
    params = list(sig.parameters.keys())



def test_uatmm::structure::weighted_is_not_abstract():
    assert not inspect.isabstract(UATMM::structure::Weighted)


def test_uatmm::structure::weighted_constructor_exists():
    assert callable(UATMM::structure::Weighted.__init__)


def test_uatmm::structure::weighted_constructor_args():
    sig = inspect.signature(UATMM::structure::Weighted.__init__)
    params = list(sig.parameters.keys())
    assert "Treshold" in params, "Missing parameter 'Treshold'"
    assert "Weights" in params, "Missing parameter 'Weights'"

def test_uatmm::structure::weighted_has_Treshold():
    assert hasattr(UATMM::structure::Weighted, "Treshold")
    descriptor = None
    for klass in UATMM::structure::Weighted.__mro__:
        if "Treshold" in klass.__dict__:
            descriptor = klass.__dict__["Treshold"]
            break
    assert isinstance(descriptor, property)

def test_uatmm::structure::weighted_has_Weights():
    assert hasattr(UATMM::structure::Weighted, "Weights")
    descriptor = None
    for klass in UATMM::structure::Weighted.__mro__:
        if "Weights" in klass.__dict__:
            descriptor = klass.__dict__["Weights"]
            break
    assert isinstance(descriptor, property)



def test_uatmm::structure::xor_is_not_abstract():
    assert not inspect.isabstract(UATMM::structure::XOR)


def test_uatmm::structure::xor_constructor_exists():
    assert callable(UATMM::structure::XOR.__init__)


def test_uatmm::structure::xor_constructor_args():
    sig = inspect.signature(UATMM::structure::XOR.__init__)
    params = list(sig.parameters.keys())



def test_uatmm::structure::pand_is_not_abstract():
    assert not inspect.isabstract(UATMM::structure::PAND)


def test_uatmm::structure::pand_constructor_exists():
    assert callable(UATMM::structure::PAND.__init__)


def test_uatmm::structure::pand_constructor_args():
    sig = inspect.signature(UATMM::structure::PAND.__init__)
    params = list(sig.parameters.keys())



def test_uatmm::structure::or_is_not_abstract():
    assert not inspect.isabstract(UATMM::structure::OR)


def test_uatmm::structure::or_constructor_exists():
    assert callable(UATMM::structure::OR.__init__)


def test_uatmm::structure::or_constructor_args():
    sig = inspect.signature(UATMM::structure::OR.__init__)
    params = list(sig.parameters.keys())



def test_uatmm::structure::fdep_is_not_abstract():
    assert not inspect.isabstract(UATMM::structure::FDEP)


def test_uatmm::structure::fdep_constructor_exists():
    assert callable(UATMM::structure::FDEP.__init__)


def test_uatmm::structure::fdep_constructor_args():
    sig = inspect.signature(UATMM::structure::FDEP.__init__)
    params = list(sig.parameters.keys())



def test_uatmm::structure::kofn_is_not_abstract():
    assert not inspect.isabstract(UATMM::structure::KofN)


def test_uatmm::structure::kofn_constructor_exists():
    assert callable(UATMM::structure::KofN.__init__)


def test_uatmm::structure::kofn_constructor_args():
    sig = inspect.signature(UATMM::structure::KofN.__init__)
    params = list(sig.parameters.keys())
    assert "Threshold" in params, "Missing parameter 'Threshold'"

def test_uatmm::structure::kofn_has_Threshold():
    assert hasattr(UATMM::structure::KofN, "Threshold")
    descriptor = None
    for klass in UATMM::structure::KofN.__mro__:
        if "Threshold" in klass.__dict__:
            descriptor = klass.__dict__["Threshold"]
            break
    assert isinstance(descriptor, property)



def test_uatmm::structure::tand_is_not_abstract():
    assert not inspect.isabstract(UATMM::structure::TAND)


def test_uatmm::structure::tand_constructor_exists():
    assert callable(UATMM::structure::TAND.__init__)


def test_uatmm::structure::tand_constructor_args():
    sig = inspect.signature(UATMM::structure::TAND.__init__)
    params = list(sig.parameters.keys())



def test_uatmm::structure::and_is_not_abstract():
    assert not inspect.isabstract(UATMM::structure::AND)


def test_uatmm::structure::and_constructor_exists():
    assert callable(UATMM::structure::AND.__init__)


def test_uatmm::structure::and_constructor_args():
    sig = inspect.signature(UATMM::structure::AND.__init__)
    params = list(sig.parameters.keys())



def test_uatmm::structure::node_is_not_abstract():
    assert not inspect.isabstract(UATMM::structure::Node)


def test_uatmm::structure::node_constructor_exists():
    assert callable(UATMM::structure::Node.__init__)


def test_uatmm::structure::node_constructor_args():
    sig = inspect.signature(UATMM::structure::Node.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "role" in params, "Missing parameter 'role'"
    assert "nature" in params, "Missing parameter 'nature'"
    assert "label" in params, "Missing parameter 'label'"

def test_uatmm::structure::node_has_id():
    assert hasattr(UATMM::structure::Node, "id")
    descriptor = None
    for klass in UATMM::structure::Node.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_uatmm::structure::node_has_role():
    assert hasattr(UATMM::structure::Node, "role")
    descriptor = None
    for klass in UATMM::structure::Node.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)

def test_uatmm::structure::node_has_nature():
    assert hasattr(UATMM::structure::Node, "nature")
    descriptor = None
    for klass in UATMM::structure::Node.__mro__:
        if "nature" in klass.__dict__:
            descriptor = klass.__dict__["nature"]
            break
    assert isinstance(descriptor, property)

def test_uatmm::structure::node_has_label():
    assert hasattr(UATMM::structure::Node, "label")
    descriptor = None
    for klass in UATMM::structure::Node.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_uatmm::structure::attacktree_is_not_abstract():
    assert not inspect.isabstract(UATMM::structure::AttackTree)


def test_uatmm::structure::attacktree_constructor_exists():
    assert callable(UATMM::structure::AttackTree.__init__)


def test_uatmm::structure::attacktree_constructor_args():
    sig = inspect.signature(UATMM::structure::AttackTree.__init__)
    params = list(sig.parameters.keys())



def test_uatmm::structure::treemetadata_is_not_abstract():
    assert not inspect.isabstract(UATMM::structure::TreeMetaData)


def test_uatmm::structure::treemetadata_constructor_exists():
    assert callable(UATMM::structure::TreeMetaData.__init__)


def test_uatmm::structure::treemetadata_constructor_args():
    sig = inspect.signature(UATMM::structure::TreeMetaData.__init__)
    params = list(sig.parameters.keys())
    assert "Value" in params, "Missing parameter 'Value'"
    assert "Key" in params, "Missing parameter 'Key'"

def test_uatmm::structure::treemetadata_has_Value():
    assert hasattr(UATMM::structure::TreeMetaData, "Value")
    descriptor = None
    for klass in UATMM::structure::TreeMetaData.__mro__:
        if "Value" in klass.__dict__:
            descriptor = klass.__dict__["Value"]
            break
    assert isinstance(descriptor, property)

def test_uatmm::structure::treemetadata_has_Key():
    assert hasattr(UATMM::structure::TreeMetaData, "Key")
    descriptor = None
    for klass in UATMM::structure::TreeMetaData.__mro__:
        if "Key" in klass.__dict__:
            descriptor = klass.__dict__["Key"]
            break
    assert isinstance(descriptor, property)



def test_uatmm::structure::edge_is_not_abstract():
    assert not inspect.isabstract(UATMM::structure::Edge)


def test_uatmm::structure::edge_constructor_exists():
    assert callable(UATMM::structure::Edge.__init__)


def test_uatmm::structure::edge_constructor_args():
    sig = inspect.signature(UATMM::structure::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "edgeKind" in params, "Missing parameter 'edgeKind'"

def test_uatmm::structure::edge_has_edgeKind():
    assert hasattr(UATMM::structure::Edge, "edgeKind")
    descriptor = None
    for klass in UATMM::structure::Edge.__mro__:
        if "edgeKind" in klass.__dict__:
            descriptor = klass.__dict__["edgeKind"]
            break
    assert isinstance(descriptor, property)



def test_uatmm::structure::rdep_is_not_abstract():
    assert not inspect.isabstract(UATMM::structure::RDEP)


def test_uatmm::structure::rdep_constructor_exists():
    assert callable(UATMM::structure::RDEP.__init__)


def test_uatmm::structure::rdep_constructor_args():
    sig = inspect.signature(UATMM::structure::RDEP.__init__)
    params = list(sig.parameters.keys())
    assert "factor" in params, "Missing parameter 'factor'"

def test_uatmm::structure::rdep_has_factor():
    assert hasattr(UATMM::structure::RDEP, "factor")
    descriptor = None
    for klass in UATMM::structure::RDEP.__mro__:
        if "factor" in klass.__dict__:
            descriptor = klass.__dict__["factor"]
            break
    assert isinstance(descriptor, property)

def test_edgekind_exists():
    # Check that the Enumeration exists
    assert EdgeKind is not None

def test_edgekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EdgeKind]
    expected_literals = [
        "TRIGGER",
        "DEPENDENCY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EdgeKind"

def test_roletype_exists():
    # Check that the Enumeration exists
    assert RoleType is not None

def test_roletype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RoleType]
    expected_literals = [
        "Counteracting",
        "Contributing",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RoleType"

def test_nature_exists():
    # Check that the Enumeration exists
    assert Nature is not None

def test_nature_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Nature]
    expected_literals = [
        "Fault",
        "Attack",
        "Hybrid",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Nature"


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
UATMM::structure::Connector_strategy = st.builds(
    UATMM::structure::Connector,
)
Connector_strategy = st.builds(
    Connector,
)
UATMM::structure::Spare_strategy = st.builds(
    UATMM::structure::Spare,
)
UATMM::structure::SAND_strategy = st.builds(
    UATMM::structure::SAND,
)
UATMM::structure::SOR_strategy = st.builds(
    UATMM::structure::SOR,
)
UATMM::structure::Weighted_strategy = st.builds(
    UATMM::structure::Weighted,
    Treshold=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Weights=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
UATMM::structure::XOR_strategy = st.builds(
    UATMM::structure::XOR,
)
UATMM::structure::PAND_strategy = st.builds(
    UATMM::structure::PAND,
)
UATMM::structure::OR_strategy = st.builds(
    UATMM::structure::OR,
)
UATMM::structure::FDEP_strategy = st.builds(
    UATMM::structure::FDEP,
)
UATMM::structure::KofN_strategy = st.builds(
    UATMM::structure::KofN,
    Threshold=
        st.integers()
)
UATMM::structure::TAND_strategy = st.builds(
    UATMM::structure::TAND,
)
UATMM::structure::AND_strategy = st.builds(
    UATMM::structure::AND,
)
UATMM::structure::Node_strategy = st.builds(
    UATMM::structure::Node,
    id=
        safe_text,
    role=
        safe_text,
    nature=
        safe_text,
    label=
        safe_text
)
UATMM::structure::AttackTree_strategy = st.builds(
    UATMM::structure::AttackTree,
)
UATMM::structure::TreeMetaData_strategy = st.builds(
    UATMM::structure::TreeMetaData,
    Value=
        safe_text,
    Key=
        safe_text
)
UATMM::structure::Edge_strategy = st.builds(
    UATMM::structure::Edge,
    edgeKind=
        safe_text
)
UATMM::structure::RDEP_strategy = st.builds(
    UATMM::structure::RDEP,
    factor=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=UATMM::structure::Connector_strategy)
@settings(max_examples=50)
def test_uatmm::structure::connector_instantiation(instance):
    assert isinstance(instance, UATMM::structure::Connector)

@given(instance=Connector_strategy)
@settings(max_examples=50)
def test_connector_instantiation(instance):
    assert isinstance(instance, Connector)

@given(instance=UATMM::structure::Spare_strategy)
@settings(max_examples=50)
def test_uatmm::structure::spare_instantiation(instance):
    assert isinstance(instance, UATMM::structure::Spare)

@given(instance=UATMM::structure::SAND_strategy)
@settings(max_examples=50)
def test_uatmm::structure::sand_instantiation(instance):
    assert isinstance(instance, UATMM::structure::SAND)

@given(instance=UATMM::structure::SOR_strategy)
@settings(max_examples=50)
def test_uatmm::structure::sor_instantiation(instance):
    assert isinstance(instance, UATMM::structure::SOR)

@given(instance=UATMM::structure::Weighted_strategy)
@settings(max_examples=50)
def test_uatmm::structure::weighted_instantiation(instance):
    assert isinstance(instance, UATMM::structure::Weighted)

@given(instance=UATMM::structure::Weighted_strategy)
def test_uatmm::structure::weighted_Treshold_type(instance):
    assert isinstance(instance.Treshold, float)


@given(instance=UATMM::structure::Weighted_strategy)
def test_uatmm::structure::weighted_Treshold_setter(instance):
    original = instance.Treshold
    instance.Treshold = original
    assert instance.Treshold == original

@given(instance=UATMM::structure::Weighted_strategy)
def test_uatmm::structure::weighted_Weights_type(instance):
    assert isinstance(instance.Weights, float)


@given(instance=UATMM::structure::Weighted_strategy)
def test_uatmm::structure::weighted_Weights_setter(instance):
    original = instance.Weights
    instance.Weights = original
    assert instance.Weights == original

@given(instance=UATMM::structure::XOR_strategy)
@settings(max_examples=50)
def test_uatmm::structure::xor_instantiation(instance):
    assert isinstance(instance, UATMM::structure::XOR)

@given(instance=UATMM::structure::PAND_strategy)
@settings(max_examples=50)
def test_uatmm::structure::pand_instantiation(instance):
    assert isinstance(instance, UATMM::structure::PAND)

@given(instance=UATMM::structure::OR_strategy)
@settings(max_examples=50)
def test_uatmm::structure::or_instantiation(instance):
    assert isinstance(instance, UATMM::structure::OR)

@given(instance=UATMM::structure::FDEP_strategy)
@settings(max_examples=50)
def test_uatmm::structure::fdep_instantiation(instance):
    assert isinstance(instance, UATMM::structure::FDEP)

@given(instance=UATMM::structure::KofN_strategy)
@settings(max_examples=50)
def test_uatmm::structure::kofn_instantiation(instance):
    assert isinstance(instance, UATMM::structure::KofN)

@given(instance=UATMM::structure::KofN_strategy)
def test_uatmm::structure::kofn_Threshold_type(instance):
    assert isinstance(instance.Threshold, int)


@given(instance=UATMM::structure::KofN_strategy)
def test_uatmm::structure::kofn_Threshold_setter(instance):
    original = instance.Threshold
    instance.Threshold = original
    assert instance.Threshold == original

@given(instance=UATMM::structure::TAND_strategy)
@settings(max_examples=50)
def test_uatmm::structure::tand_instantiation(instance):
    assert isinstance(instance, UATMM::structure::TAND)

@given(instance=UATMM::structure::AND_strategy)
@settings(max_examples=50)
def test_uatmm::structure::and_instantiation(instance):
    assert isinstance(instance, UATMM::structure::AND)

@given(instance=UATMM::structure::Node_strategy)
@settings(max_examples=50)
def test_uatmm::structure::node_instantiation(instance):
    assert isinstance(instance, UATMM::structure::Node)

@given(instance=UATMM::structure::Node_strategy)
def test_uatmm::structure::node_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=UATMM::structure::Node_strategy)
def test_uatmm::structure::node_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=UATMM::structure::Node_strategy)
def test_uatmm::structure::node_role_type(instance):
    assert isinstance(instance.role, str)


@given(instance=UATMM::structure::Node_strategy)
def test_uatmm::structure::node_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original

@given(instance=UATMM::structure::Node_strategy)
def test_uatmm::structure::node_nature_type(instance):
    assert isinstance(instance.nature, str)


@given(instance=UATMM::structure::Node_strategy)
def test_uatmm::structure::node_nature_setter(instance):
    original = instance.nature
    instance.nature = original
    assert instance.nature == original

@given(instance=UATMM::structure::Node_strategy)
def test_uatmm::structure::node_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=UATMM::structure::Node_strategy)
def test_uatmm::structure::node_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=UATMM::structure::AttackTree_strategy)
@settings(max_examples=50)
def test_uatmm::structure::attacktree_instantiation(instance):
    assert isinstance(instance, UATMM::structure::AttackTree)

@given(instance=UATMM::structure::TreeMetaData_strategy)
@settings(max_examples=50)
def test_uatmm::structure::treemetadata_instantiation(instance):
    assert isinstance(instance, UATMM::structure::TreeMetaData)

@given(instance=UATMM::structure::TreeMetaData_strategy)
def test_uatmm::structure::treemetadata_Value_type(instance):
    assert isinstance(instance.Value, str)


@given(instance=UATMM::structure::TreeMetaData_strategy)
def test_uatmm::structure::treemetadata_Value_setter(instance):
    original = instance.Value
    instance.Value = original
    assert instance.Value == original

@given(instance=UATMM::structure::TreeMetaData_strategy)
def test_uatmm::structure::treemetadata_Key_type(instance):
    assert isinstance(instance.Key, str)


@given(instance=UATMM::structure::TreeMetaData_strategy)
def test_uatmm::structure::treemetadata_Key_setter(instance):
    original = instance.Key
    instance.Key = original
    assert instance.Key == original

@given(instance=UATMM::structure::Edge_strategy)
@settings(max_examples=50)
def test_uatmm::structure::edge_instantiation(instance):
    assert isinstance(instance, UATMM::structure::Edge)

@given(instance=UATMM::structure::Edge_strategy)
def test_uatmm::structure::edge_edgeKind_type(instance):
    assert isinstance(instance.edgeKind, str)


@given(instance=UATMM::structure::Edge_strategy)
def test_uatmm::structure::edge_edgeKind_setter(instance):
    original = instance.edgeKind
    instance.edgeKind = original
    assert instance.edgeKind == original

@given(instance=UATMM::structure::RDEP_strategy)
@settings(max_examples=50)
def test_uatmm::structure::rdep_instantiation(instance):
    assert isinstance(instance, UATMM::structure::RDEP)

@given(instance=UATMM::structure::RDEP_strategy)
def test_uatmm::structure::rdep_factor_type(instance):
    assert isinstance(instance.factor, float)


@given(instance=UATMM::structure::RDEP_strategy)
def test_uatmm::structure::rdep_factor_setter(instance):
    original = instance.factor
    instance.factor = original
    assert instance.factor == original
