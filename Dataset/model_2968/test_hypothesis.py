import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ASD_Annotation,
    ASD_NamedElement,
    InfoType,
    ASD_InfoTypeImported,
    NamedElement,
    ASD_Assertion,
    ASD_Message,
    ASD_InfoType,
    ASD_Profile,
    ASD_AssertionSet,
    ASD_Operation,
    ASD_ServiceDescription,
    EEnumlogicalType,
    EEnumOp,
    EEnumIntention,
    EEnumSubset,
    EEnumValueType,
    EEnumDimensionType,
    EEnumMes,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_asd_annotation_is_not_abstract():
    assert not inspect.isabstract(ASD_Annotation)


def test_asd_annotation_constructor_exists():
    assert callable(ASD_Annotation.__init__)


def test_asd_annotation_constructor_args():
    sig = inspect.signature(ASD_Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_asd_annotation_has_value():
    assert hasattr(ASD_Annotation, "value")
    descriptor = None
    for klass in ASD_Annotation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_asd_annotation_has_key():
    assert hasattr(ASD_Annotation, "key")
    descriptor = None
    for klass in ASD_Annotation.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_asd_namedelement_is_not_abstract():
    assert not inspect.isabstract(ASD_NamedElement)


def test_asd_namedelement_constructor_exists():
    assert callable(ASD_NamedElement.__init__)


def test_asd_namedelement_constructor_args():
    sig = inspect.signature(ASD_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_asd_namedelement_has_name():
    assert hasattr(ASD_NamedElement, "name")
    descriptor = None
    for klass in ASD_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_infotype_is_not_abstract():
    assert not inspect.isabstract(InfoType)


def test_infotype_constructor_exists():
    assert callable(InfoType.__init__)


def test_infotype_constructor_args():
    sig = inspect.signature(InfoType.__init__)
    params = list(sig.parameters.keys())



def test_asd_infotypeimported_is_not_abstract():
    assert not inspect.isabstract(ASD_InfoTypeImported)


def test_asd_infotypeimported_constructor_exists():
    assert callable(ASD_InfoTypeImported.__init__)


def test_asd_infotypeimported_constructor_args():
    sig = inspect.signature(ASD_InfoTypeImported.__init__)
    params = list(sig.parameters.keys())
    assert "url" in params, "Missing parameter 'url'"

def test_asd_infotypeimported_has_url():
    assert hasattr(ASD_InfoTypeImported, "url")
    descriptor = None
    for klass in ASD_InfoTypeImported.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_asd_assertion_is_not_abstract():
    assert not inspect.isabstract(ASD_Assertion)


def test_asd_assertion_constructor_exists():
    assert callable(ASD_Assertion.__init__)


def test_asd_assertion_constructor_args():
    sig = inspect.signature(ASD_Assertion.__init__)
    params = list(sig.parameters.keys())
    assert "maxVal" in params, "Missing parameter 'maxVal'"
    assert "lType" in params, "Missing parameter 'lType'"
    assert "subset" in params, "Missing parameter 'subset'"
    assert "dimensionType" in params, "Missing parameter 'dimensionType'"
    assert "role" in params, "Missing parameter 'role'"
    assert "dimension" in params, "Missing parameter 'dimension'"
    assert "minVal" in params, "Missing parameter 'minVal'"

def test_asd_assertion_has_maxVal():
    assert hasattr(ASD_Assertion, "maxVal")
    descriptor = None
    for klass in ASD_Assertion.__mro__:
        if "maxVal" in klass.__dict__:
            descriptor = klass.__dict__["maxVal"]
            break
    assert isinstance(descriptor, property)

def test_asd_assertion_has_lType():
    assert hasattr(ASD_Assertion, "lType")
    descriptor = None
    for klass in ASD_Assertion.__mro__:
        if "lType" in klass.__dict__:
            descriptor = klass.__dict__["lType"]
            break
    assert isinstance(descriptor, property)

def test_asd_assertion_has_subset():
    assert hasattr(ASD_Assertion, "subset")
    descriptor = None
    for klass in ASD_Assertion.__mro__:
        if "subset" in klass.__dict__:
            descriptor = klass.__dict__["subset"]
            break
    assert isinstance(descriptor, property)

def test_asd_assertion_has_dimensionType():
    assert hasattr(ASD_Assertion, "dimensionType")
    descriptor = None
    for klass in ASD_Assertion.__mro__:
        if "dimensionType" in klass.__dict__:
            descriptor = klass.__dict__["dimensionType"]
            break
    assert isinstance(descriptor, property)

def test_asd_assertion_has_role():
    assert hasattr(ASD_Assertion, "role")
    descriptor = None
    for klass in ASD_Assertion.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)

def test_asd_assertion_has_dimension():
    assert hasattr(ASD_Assertion, "dimension")
    descriptor = None
    for klass in ASD_Assertion.__mro__:
        if "dimension" in klass.__dict__:
            descriptor = klass.__dict__["dimension"]
            break
    assert isinstance(descriptor, property)

def test_asd_assertion_has_minVal():
    assert hasattr(ASD_Assertion, "minVal")
    descriptor = None
    for klass in ASD_Assertion.__mro__:
        if "minVal" in klass.__dict__:
            descriptor = klass.__dict__["minVal"]
            break
    assert isinstance(descriptor, property)



def test_asd_message_is_not_abstract():
    assert not inspect.isabstract(ASD_Message)


def test_asd_message_constructor_exists():
    assert callable(ASD_Message.__init__)


def test_asd_message_constructor_args():
    sig = inspect.signature(ASD_Message.__init__)
    params = list(sig.parameters.keys())
    assert "role" in params, "Missing parameter 'role'"
    assert "subset" in params, "Missing parameter 'subset'"

def test_asd_message_has_role():
    assert hasattr(ASD_Message, "role")
    descriptor = None
    for klass in ASD_Message.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)

def test_asd_message_has_subset():
    assert hasattr(ASD_Message, "subset")
    descriptor = None
    for klass in ASD_Message.__mro__:
        if "subset" in klass.__dict__:
            descriptor = klass.__dict__["subset"]
            break
    assert isinstance(descriptor, property)



def test_asd_infotype_is_not_abstract():
    assert not inspect.isabstract(ASD_InfoType)


def test_asd_infotype_constructor_exists():
    assert callable(ASD_InfoType.__init__)


def test_asd_infotype_constructor_args():
    sig = inspect.signature(ASD_InfoType.__init__)
    params = list(sig.parameters.keys())
    assert "subset" in params, "Missing parameter 'subset'"
    assert "valueType" in params, "Missing parameter 'valueType'"
    assert "valueRange" in params, "Missing parameter 'valueRange'"

def test_asd_infotype_has_subset():
    assert hasattr(ASD_InfoType, "subset")
    descriptor = None
    for klass in ASD_InfoType.__mro__:
        if "subset" in klass.__dict__:
            descriptor = klass.__dict__["subset"]
            break
    assert isinstance(descriptor, property)

def test_asd_infotype_has_valueType():
    assert hasattr(ASD_InfoType, "valueType")
    descriptor = None
    for klass in ASD_InfoType.__mro__:
        if "valueType" in klass.__dict__:
            descriptor = klass.__dict__["valueType"]
            break
    assert isinstance(descriptor, property)

def test_asd_infotype_has_valueRange():
    assert hasattr(ASD_InfoType, "valueRange")
    descriptor = None
    for klass in ASD_InfoType.__mro__:
        if "valueRange" in klass.__dict__:
            descriptor = klass.__dict__["valueRange"]
            break
    assert isinstance(descriptor, property)



def test_asd_profile_is_not_abstract():
    assert not inspect.isabstract(ASD_Profile)


def test_asd_profile_constructor_exists():
    assert callable(ASD_Profile.__init__)


def test_asd_profile_constructor_args():
    sig = inspect.signature(ASD_Profile.__init__)
    params = list(sig.parameters.keys())



def test_asd_assertionset_is_not_abstract():
    assert not inspect.isabstract(ASD_AssertionSet)


def test_asd_assertionset_constructor_exists():
    assert callable(ASD_AssertionSet.__init__)


def test_asd_assertionset_constructor_args():
    sig = inspect.signature(ASD_AssertionSet.__init__)
    params = list(sig.parameters.keys())
    assert "lType" in params, "Missing parameter 'lType'"

def test_asd_assertionset_has_lType():
    assert hasattr(ASD_AssertionSet, "lType")
    descriptor = None
    for klass in ASD_AssertionSet.__mro__:
        if "lType" in klass.__dict__:
            descriptor = klass.__dict__["lType"]
            break
    assert isinstance(descriptor, property)



def test_asd_operation_is_not_abstract():
    assert not inspect.isabstract(ASD_Operation)


def test_asd_operation_constructor_exists():
    assert callable(ASD_Operation.__init__)


def test_asd_operation_constructor_args():
    sig = inspect.signature(ASD_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "messagePattern" in params, "Missing parameter 'messagePattern'"

def test_asd_operation_has_messagePattern():
    assert hasattr(ASD_Operation, "messagePattern")
    descriptor = None
    for klass in ASD_Operation.__mro__:
        if "messagePattern" in klass.__dict__:
            descriptor = klass.__dict__["messagePattern"]
            break
    assert isinstance(descriptor, property)



def test_asd_servicedescription_is_not_abstract():
    assert not inspect.isabstract(ASD_ServiceDescription)


def test_asd_servicedescription_constructor_exists():
    assert callable(ASD_ServiceDescription.__init__)


def test_asd_servicedescription_constructor_args():
    sig = inspect.signature(ASD_ServiceDescription.__init__)
    params = list(sig.parameters.keys())

def test_eenumlogicaltype_exists():
    # Check that the Enumeration exists
    assert EEnumlogicalType is not None

def test_eenumlogicaltype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EEnumlogicalType]
    expected_literals = [
        "AND",
        "OR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EEnumlogicalType"

def test_eenumop_exists():
    # Check that the Enumeration exists
    assert EEnumOp is not None

def test_eenumop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EEnumOp]
    expected_literals = [
        "oneway",
        "requestresponse",
        "solicitresponse",
        "notification",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EEnumOp"

def test_eenumintention_exists():
    # Check that the Enumeration exists
    assert EEnumIntention is not None

def test_eenumintention_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EEnumIntention]
    expected_literals = [
        "expectation",
        "offering",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EEnumIntention"

def test_eenumsubset_exists():
    # Check that the Enumeration exists
    assert EEnumSubset is not None

def test_eenumsubset_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EEnumSubset]
    expected_literals = [
        "req",
        "off",
        "pro",
        "exp",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EEnumSubset"

def test_eenumvaluetype_exists():
    # Check that the Enumeration exists
    assert EEnumValueType is not None

def test_eenumvaluetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EEnumValueType]
    expected_literals = [
        "date",
        "double",
        "int",
        "string",
        "float",
        "document",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EEnumValueType"

def test_eenumdimensiontype_exists():
    # Check that the Enumeration exists
    assert EEnumDimensionType is not None

def test_eenumdimensiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EEnumDimensionType]
    expected_literals = [
        "antitonic",
        "monotonic",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EEnumDimensionType"

def test_eenummes_exists():
    # Check that the Enumeration exists
    assert EEnumMes is not None

def test_eenummes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EEnumMes]
    expected_literals = [
        "input",
        "fault",
        "output",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EEnumMes"


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
ASD_Annotation_strategy = st.builds(
    ASD_Annotation,
    value=
        safe_text,
    key=
        safe_text
)
ASD_NamedElement_strategy = st.builds(
    ASD_NamedElement,
    name=
        safe_text
)
InfoType_strategy = st.builds(
    InfoType,
)
ASD_InfoTypeImported_strategy = st.builds(
    ASD_InfoTypeImported,
    url=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
ASD_Assertion_strategy = st.builds(
    ASD_Assertion,
    maxVal=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    lType=
        safe_text,
    subset=
        safe_text,
    dimensionType=
        safe_text,
    role=
        safe_text,
    dimension=
        safe_text,
    minVal=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ASD_Message_strategy = st.builds(
    ASD_Message,
    role=
        safe_text,
    subset=
        safe_text
)
ASD_InfoType_strategy = st.builds(
    ASD_InfoType,
    subset=
        safe_text,
    valueType=
        safe_text,
    valueRange=
        safe_text
)
ASD_Profile_strategy = st.builds(
    ASD_Profile,
)
ASD_AssertionSet_strategy = st.builds(
    ASD_AssertionSet,
    lType=
        safe_text
)
ASD_Operation_strategy = st.builds(
    ASD_Operation,
    messagePattern=
        safe_text
)
ASD_ServiceDescription_strategy = st.builds(
    ASD_ServiceDescription,
)

@given(instance=ASD_Annotation_strategy)
@settings(max_examples=50)
def test_asd_annotation_instantiation(instance):
    assert isinstance(instance, ASD_Annotation)



@given(instance=ASD_Annotation_strategy)
def test_asd_annotation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=ASD_Annotation_strategy)
def test_asd_annotation_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=ASD_NamedElement_strategy)
@settings(max_examples=50)
def test_asd_namedelement_instantiation(instance):
    assert isinstance(instance, ASD_NamedElement)



@given(instance=ASD_NamedElement_strategy)
def test_asd_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=InfoType_strategy)
@settings(max_examples=50)
def test_infotype_instantiation(instance):
    assert isinstance(instance, InfoType)

@given(instance=ASD_InfoTypeImported_strategy)
@settings(max_examples=50)
def test_asd_infotypeimported_instantiation(instance):
    assert isinstance(instance, ASD_InfoTypeImported)



@given(instance=ASD_InfoTypeImported_strategy)
def test_asd_infotypeimported_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=ASD_Assertion_strategy)
@settings(max_examples=50)
def test_asd_assertion_instantiation(instance):
    assert isinstance(instance, ASD_Assertion)



@given(instance=ASD_Assertion_strategy)
def test_asd_assertion_maxVal_setter(instance):
    original = instance.maxVal
    instance.maxVal = original
    assert instance.maxVal == original



@given(instance=ASD_Assertion_strategy)
def test_asd_assertion_lType_setter(instance):
    original = instance.lType
    instance.lType = original
    assert instance.lType == original



@given(instance=ASD_Assertion_strategy)
def test_asd_assertion_subset_setter(instance):
    original = instance.subset
    instance.subset = original
    assert instance.subset == original



@given(instance=ASD_Assertion_strategy)
def test_asd_assertion_dimensionType_setter(instance):
    original = instance.dimensionType
    instance.dimensionType = original
    assert instance.dimensionType == original



@given(instance=ASD_Assertion_strategy)
def test_asd_assertion_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original



@given(instance=ASD_Assertion_strategy)
def test_asd_assertion_dimension_setter(instance):
    original = instance.dimension
    instance.dimension = original
    assert instance.dimension == original



@given(instance=ASD_Assertion_strategy)
def test_asd_assertion_minVal_setter(instance):
    original = instance.minVal
    instance.minVal = original
    assert instance.minVal == original

@given(instance=ASD_Message_strategy)
@settings(max_examples=50)
def test_asd_message_instantiation(instance):
    assert isinstance(instance, ASD_Message)



@given(instance=ASD_Message_strategy)
def test_asd_message_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original



@given(instance=ASD_Message_strategy)
def test_asd_message_subset_setter(instance):
    original = instance.subset
    instance.subset = original
    assert instance.subset == original

@given(instance=ASD_InfoType_strategy)
@settings(max_examples=50)
def test_asd_infotype_instantiation(instance):
    assert isinstance(instance, ASD_InfoType)



@given(instance=ASD_InfoType_strategy)
def test_asd_infotype_subset_setter(instance):
    original = instance.subset
    instance.subset = original
    assert instance.subset == original



@given(instance=ASD_InfoType_strategy)
def test_asd_infotype_valueType_setter(instance):
    original = instance.valueType
    instance.valueType = original
    assert instance.valueType == original



@given(instance=ASD_InfoType_strategy)
def test_asd_infotype_valueRange_setter(instance):
    original = instance.valueRange
    instance.valueRange = original
    assert instance.valueRange == original

@given(instance=ASD_Profile_strategy)
@settings(max_examples=50)
def test_asd_profile_instantiation(instance):
    assert isinstance(instance, ASD_Profile)

@given(instance=ASD_AssertionSet_strategy)
@settings(max_examples=50)
def test_asd_assertionset_instantiation(instance):
    assert isinstance(instance, ASD_AssertionSet)



@given(instance=ASD_AssertionSet_strategy)
def test_asd_assertionset_lType_setter(instance):
    original = instance.lType
    instance.lType = original
    assert instance.lType == original

@given(instance=ASD_Operation_strategy)
@settings(max_examples=50)
def test_asd_operation_instantiation(instance):
    assert isinstance(instance, ASD_Operation)



@given(instance=ASD_Operation_strategy)
def test_asd_operation_messagePattern_setter(instance):
    original = instance.messagePattern
    instance.messagePattern = original
    assert instance.messagePattern == original

@given(instance=ASD_ServiceDescription_strategy)
@settings(max_examples=50)
def test_asd_servicedescription_instantiation(instance):
    assert isinstance(instance, ASD_ServiceDescription)
