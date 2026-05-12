import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    kreq103_Ffff,
    kreq103_Gggg,
    kreq103_Cccc,
    kreq103_Bbbb,
    ComponentPosition,
    ComponentType,
    BasicFlowTransformationType,
    RequirementOrigin,
    CategoryType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_kreq103_ffff_is_not_abstract():
    assert not inspect.isabstract(kreq103_Ffff)


def test_kreq103_ffff_constructor_exists():
    assert callable(kreq103_Ffff.__init__)


def test_kreq103_ffff_constructor_args():
    sig = inspect.signature(kreq103_Ffff.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_kreq103_ffff_has_id():
    assert hasattr(kreq103_Ffff, "id")
    descriptor = None
    for klass in kreq103_Ffff.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_kreq103_gggg_is_not_abstract():
    assert not inspect.isabstract(kreq103_Gggg)


def test_kreq103_gggg_constructor_exists():
    assert callable(kreq103_Gggg.__init__)


def test_kreq103_gggg_constructor_args():
    sig = inspect.signature(kreq103_Gggg.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_kreq103_gggg_has_id():
    assert hasattr(kreq103_Gggg, "id")
    descriptor = None
    for klass in kreq103_Gggg.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_kreq103_cccc_is_not_abstract():
    assert not inspect.isabstract(kreq103_Cccc)


def test_kreq103_cccc_constructor_exists():
    assert callable(kreq103_Cccc.__init__)


def test_kreq103_cccc_constructor_args():
    sig = inspect.signature(kreq103_Cccc.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_kreq103_cccc_has_id():
    assert hasattr(kreq103_Cccc, "id")
    descriptor = None
    for klass in kreq103_Cccc.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_kreq103_bbbb_is_not_abstract():
    assert not inspect.isabstract(kreq103_Bbbb)


def test_kreq103_bbbb_constructor_exists():
    assert callable(kreq103_Bbbb.__init__)


def test_kreq103_bbbb_constructor_args():
    sig = inspect.signature(kreq103_Bbbb.__init__)
    params = list(sig.parameters.keys())

def test_componentposition_exists():
    # Check that the Enumeration exists
    assert ComponentPosition is not None

def test_componentposition_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComponentPosition]
    expected_literals = [
        "Not_yet_defined",
        "Environmental_context",
        "Local",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComponentPosition"

def test_componenttype_exists():
    # Check that the Enumeration exists
    assert ComponentType is not None

def test_componenttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComponentType]
    expected_literals = [
        "Organization_Unit",
        "Role",
        "Information_system",
        "Process",
        "Operational_system",
        "Tool",
        "Other",
        "Serrvice",
        "Logical_component",
        "Site",
        "Actor",
        "Physical_component",
        "Activity",
        "System",
        "Not_yet_desighed",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComponentType"

def test_basicflowtransformationtype_exists():
    # Check that the Enumeration exists
    assert BasicFlowTransformationType is not None

def test_basicflowtransformationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BasicFlowTransformationType]
    expected_literals = [
        "Check_Verify_Validate",
        "Measure",
        "Decide",
        "EEnumLiteral0",
        "Transiform",
        "Store",
        "Wait",
        "Control",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BasicFlowTransformationType"

def test_requirementorigin_exists():
    # Check that the Enumeration exists
    assert RequirementOrigin is not None

def test_requirementorigin_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RequirementOrigin]
    expected_literals = [
        "Derived",
        "DesignChoise_induced",
        "Originating",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RequirementOrigin"

def test_categorytype_exists():
    # Check that the Enumeration exists
    assert CategoryType is not None

def test_categorytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CategoryType]
    expected_literals = [
        "Functional",
        "Operational",
        "Non_Functional",
        "Interface",
        "VandV",
        "Constraints",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CategoryType"


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
kreq103_Ffff_strategy = st.builds(
    kreq103_Ffff,
    id=
        safe_text
)
kreq103_Gggg_strategy = st.builds(
    kreq103_Gggg,
    id=
        safe_text
)
kreq103_Cccc_strategy = st.builds(
    kreq103_Cccc,
    id=
        safe_text
)
kreq103_Bbbb_strategy = st.builds(
    kreq103_Bbbb,
)

@given(instance=kreq103_Ffff_strategy)
@settings(max_examples=50)
def test_kreq103_ffff_instantiation(instance):
    assert isinstance(instance, kreq103_Ffff)



@given(instance=kreq103_Ffff_strategy)
def test_kreq103_ffff_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=kreq103_Gggg_strategy)
@settings(max_examples=50)
def test_kreq103_gggg_instantiation(instance):
    assert isinstance(instance, kreq103_Gggg)



@given(instance=kreq103_Gggg_strategy)
def test_kreq103_gggg_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=kreq103_Cccc_strategy)
@settings(max_examples=50)
def test_kreq103_cccc_instantiation(instance):
    assert isinstance(instance, kreq103_Cccc)



@given(instance=kreq103_Cccc_strategy)
def test_kreq103_cccc_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=kreq103_Bbbb_strategy)
@settings(max_examples=50)
def test_kreq103_bbbb_instantiation(instance):
    assert isinstance(instance, kreq103_Bbbb)
