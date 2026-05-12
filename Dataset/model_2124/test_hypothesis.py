import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TestCategoryBase,
    TestCategoryBeanAbstract,
    dmf_DObject,
    tests_TestCategoryExtends,
    tests_TestCategoryBeanConcrete,
    tests_ExternalTestType,
    DObject,
    tests_TestCategoryBeanA,
    tests_EReferenceTest,
    tests_TestCategoryReferenceArray,
    tests_TestCategoryIntrinsicArray,
    tests_TestCategoryBeanB,
    tests_TestMassParameters,
    tests_TestCategoryBase,
    tests_TestCategoryComposition,
    tests_TestParameter,
    tests_TestCategoryBeanAbstract,
    tests_TestCategoryCompositionArray,
    tests_TestCrossLinkedParametersWithCalculation,
    tests_TestCategoryReference,
    tests_TestCategoryAllProperty,
    EnumTestEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testcategorybase_is_not_abstract():
    assert not inspect.isabstract(TestCategoryBase)


def test_testcategorybase_constructor_exists():
    assert callable(TestCategoryBase.__init__)


def test_testcategorybase_constructor_args():
    sig = inspect.signature(TestCategoryBase.__init__)
    params = list(sig.parameters.keys())



def test_testcategorybeanabstract_is_not_abstract():
    assert not inspect.isabstract(TestCategoryBeanAbstract)


def test_testcategorybeanabstract_constructor_exists():
    assert callable(TestCategoryBeanAbstract.__init__)


def test_testcategorybeanabstract_constructor_args():
    sig = inspect.signature(TestCategoryBeanAbstract.__init__)
    params = list(sig.parameters.keys())



def test_dmf_dobject_is_not_abstract():
    assert not inspect.isabstract(dmf_DObject)


def test_dmf_dobject_constructor_exists():
    assert callable(dmf_DObject.__init__)


def test_dmf_dobject_constructor_args():
    sig = inspect.signature(dmf_DObject.__init__)
    params = list(sig.parameters.keys())



def test_tests_testcategoryextends_is_not_abstract():
    assert not inspect.isabstract(tests_TestCategoryExtends)


def test_tests_testcategoryextends_constructor_exists():
    assert callable(tests_TestCategoryExtends.__init__)


def test_tests_testcategoryextends_constructor_args():
    sig = inspect.signature(tests_TestCategoryExtends.__init__)
    params = list(sig.parameters.keys())
    assert "testExtendsProperty" in params, "Missing parameter 'testExtendsProperty'"

def test_tests_testcategoryextends_has_testExtendsProperty():
    assert hasattr(tests_TestCategoryExtends, "testExtendsProperty")
    descriptor = None
    for klass in tests_TestCategoryExtends.__mro__:
        if "testExtendsProperty" in klass.__dict__:
            descriptor = klass.__dict__["testExtendsProperty"]
            break
    assert isinstance(descriptor, property)



def test_tests_testcategorybeanconcrete_is_not_abstract():
    assert not inspect.isabstract(tests_TestCategoryBeanConcrete)


def test_tests_testcategorybeanconcrete_constructor_exists():
    assert callable(tests_TestCategoryBeanConcrete.__init__)


def test_tests_testcategorybeanconcrete_constructor_args():
    sig = inspect.signature(tests_TestCategoryBeanConcrete.__init__)
    params = list(sig.parameters.keys())



def test_tests_externaltesttype_is_not_abstract():
    assert not inspect.isabstract(tests_ExternalTestType)


def test_tests_externaltesttype_constructor_exists():
    assert callable(tests_ExternalTestType.__init__)


def test_tests_externaltesttype_constructor_args():
    sig = inspect.signature(tests_ExternalTestType.__init__)
    params = list(sig.parameters.keys())



def test_dobject_is_not_abstract():
    assert not inspect.isabstract(DObject)


def test_dobject_constructor_exists():
    assert callable(DObject.__init__)


def test_dobject_constructor_args():
    sig = inspect.signature(DObject.__init__)
    params = list(sig.parameters.keys())



def test_tests_testcategorybeana_is_not_abstract():
    assert not inspect.isabstract(tests_TestCategoryBeanA)


def test_tests_testcategorybeana_constructor_exists():
    assert callable(tests_TestCategoryBeanA.__init__)


def test_tests_testcategorybeana_constructor_args():
    sig = inspect.signature(tests_TestCategoryBeanA.__init__)
    params = list(sig.parameters.keys())



def test_tests_ereferencetest_is_not_abstract():
    assert not inspect.isabstract(tests_EReferenceTest)


def test_tests_ereferencetest_constructor_exists():
    assert callable(tests_EReferenceTest.__init__)


def test_tests_ereferencetest_constructor_args():
    sig = inspect.signature(tests_EReferenceTest.__init__)
    params = list(sig.parameters.keys())



def test_tests_testcategoryreferencearray_is_not_abstract():
    assert not inspect.isabstract(tests_TestCategoryReferenceArray)


def test_tests_testcategoryreferencearray_constructor_exists():
    assert callable(tests_TestCategoryReferenceArray.__init__)


def test_tests_testcategoryreferencearray_constructor_args():
    sig = inspect.signature(tests_TestCategoryReferenceArray.__init__)
    params = list(sig.parameters.keys())



def test_tests_testcategoryintrinsicarray_is_not_abstract():
    assert not inspect.isabstract(tests_TestCategoryIntrinsicArray)


def test_tests_testcategoryintrinsicarray_constructor_exists():
    assert callable(tests_TestCategoryIntrinsicArray.__init__)


def test_tests_testcategoryintrinsicarray_constructor_args():
    sig = inspect.signature(tests_TestCategoryIntrinsicArray.__init__)
    params = list(sig.parameters.keys())
    assert "testStringArrayStatic" in params, "Missing parameter 'testStringArrayStatic'"
    assert "testStringArrayDynamic" in params, "Missing parameter 'testStringArrayDynamic'"

def test_tests_testcategoryintrinsicarray_has_testStringArrayStatic():
    assert hasattr(tests_TestCategoryIntrinsicArray, "testStringArrayStatic")
    descriptor = None
    for klass in tests_TestCategoryIntrinsicArray.__mro__:
        if "testStringArrayStatic" in klass.__dict__:
            descriptor = klass.__dict__["testStringArrayStatic"]
            break
    assert isinstance(descriptor, property)

def test_tests_testcategoryintrinsicarray_has_testStringArrayDynamic():
    assert hasattr(tests_TestCategoryIntrinsicArray, "testStringArrayDynamic")
    descriptor = None
    for klass in tests_TestCategoryIntrinsicArray.__mro__:
        if "testStringArrayDynamic" in klass.__dict__:
            descriptor = klass.__dict__["testStringArrayDynamic"]
            break
    assert isinstance(descriptor, property)



def test_tests_testcategorybeanb_is_not_abstract():
    assert not inspect.isabstract(tests_TestCategoryBeanB)


def test_tests_testcategorybeanb_constructor_exists():
    assert callable(tests_TestCategoryBeanB.__init__)


def test_tests_testcategorybeanb_constructor_args():
    sig = inspect.signature(tests_TestCategoryBeanB.__init__)
    params = list(sig.parameters.keys())



def test_tests_testmassparameters_is_not_abstract():
    assert not inspect.isabstract(tests_TestMassParameters)


def test_tests_testmassparameters_constructor_exists():
    assert callable(tests_TestMassParameters.__init__)


def test_tests_testmassparameters_constructor_args():
    sig = inspect.signature(tests_TestMassParameters.__init__)
    params = list(sig.parameters.keys())



def test_tests_testcategorybase_is_not_abstract():
    assert not inspect.isabstract(tests_TestCategoryBase)


def test_tests_testcategorybase_constructor_exists():
    assert callable(tests_TestCategoryBase.__init__)


def test_tests_testcategorybase_constructor_args():
    sig = inspect.signature(tests_TestCategoryBase.__init__)
    params = list(sig.parameters.keys())
    assert "testBaseProperty" in params, "Missing parameter 'testBaseProperty'"

def test_tests_testcategorybase_has_testBaseProperty():
    assert hasattr(tests_TestCategoryBase, "testBaseProperty")
    descriptor = None
    for klass in tests_TestCategoryBase.__mro__:
        if "testBaseProperty" in klass.__dict__:
            descriptor = klass.__dict__["testBaseProperty"]
            break
    assert isinstance(descriptor, property)



def test_tests_testcategorycomposition_is_not_abstract():
    assert not inspect.isabstract(tests_TestCategoryComposition)


def test_tests_testcategorycomposition_constructor_exists():
    assert callable(tests_TestCategoryComposition.__init__)


def test_tests_testcategorycomposition_constructor_args():
    sig = inspect.signature(tests_TestCategoryComposition.__init__)
    params = list(sig.parameters.keys())



def test_tests_testparameter_is_not_abstract():
    assert not inspect.isabstract(tests_TestParameter)


def test_tests_testparameter_constructor_exists():
    assert callable(tests_TestParameter.__init__)


def test_tests_testparameter_constructor_args():
    sig = inspect.signature(tests_TestParameter.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"

def test_tests_testparameter_has_defaultValue():
    assert hasattr(tests_TestParameter, "defaultValue")
    descriptor = None
    for klass in tests_TestParameter.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)



def test_tests_testcategorybeanabstract_is_not_abstract():
    assert not inspect.isabstract(tests_TestCategoryBeanAbstract)


def test_tests_testcategorybeanabstract_constructor_exists():
    assert callable(tests_TestCategoryBeanAbstract.__init__)


def test_tests_testcategorybeanabstract_constructor_args():
    sig = inspect.signature(tests_TestCategoryBeanAbstract.__init__)
    params = list(sig.parameters.keys())



def test_tests_testcategorycompositionarray_is_not_abstract():
    assert not inspect.isabstract(tests_TestCategoryCompositionArray)


def test_tests_testcategorycompositionarray_constructor_exists():
    assert callable(tests_TestCategoryCompositionArray.__init__)


def test_tests_testcategorycompositionarray_constructor_args():
    sig = inspect.signature(tests_TestCategoryCompositionArray.__init__)
    params = list(sig.parameters.keys())



def test_tests_testcrosslinkedparameterswithcalculation_is_not_abstract():
    assert not inspect.isabstract(tests_TestCrossLinkedParametersWithCalculation)


def test_tests_testcrosslinkedparameterswithcalculation_constructor_exists():
    assert callable(tests_TestCrossLinkedParametersWithCalculation.__init__)


def test_tests_testcrosslinkedparameterswithcalculation_constructor_args():
    sig = inspect.signature(tests_TestCrossLinkedParametersWithCalculation.__init__)
    params = list(sig.parameters.keys())
    assert "calcedTrl" in params, "Missing parameter 'calcedTrl'"

def test_tests_testcrosslinkedparameterswithcalculation_has_calcedTrl():
    assert hasattr(tests_TestCrossLinkedParametersWithCalculation, "calcedTrl")
    descriptor = None
    for klass in tests_TestCrossLinkedParametersWithCalculation.__mro__:
        if "calcedTrl" in klass.__dict__:
            descriptor = klass.__dict__["calcedTrl"]
            break
    assert isinstance(descriptor, property)



def test_tests_testcategoryreference_is_not_abstract():
    assert not inspect.isabstract(tests_TestCategoryReference)


def test_tests_testcategoryreference_constructor_exists():
    assert callable(tests_TestCategoryReference.__init__)


def test_tests_testcategoryreference_constructor_args():
    sig = inspect.signature(tests_TestCategoryReference.__init__)
    params = list(sig.parameters.keys())



def test_tests_testcategoryallproperty_is_not_abstract():
    assert not inspect.isabstract(tests_TestCategoryAllProperty)


def test_tests_testcategoryallproperty_constructor_exists():
    assert callable(tests_TestCategoryAllProperty.__init__)


def test_tests_testcategoryallproperty_constructor_args():
    sig = inspect.signature(tests_TestCategoryAllProperty.__init__)
    params = list(sig.parameters.keys())
    assert "testEnum" in params, "Missing parameter 'testEnum'"
    assert "testBool" in params, "Missing parameter 'testBool'"
    assert "testFloat" in params, "Missing parameter 'testFloat'"
    assert "testInt" in params, "Missing parameter 'testInt'"
    assert "testResource" in params, "Missing parameter 'testResource'"
    assert "testString" in params, "Missing parameter 'testString'"

def test_tests_testcategoryallproperty_has_testEnum():
    assert hasattr(tests_TestCategoryAllProperty, "testEnum")
    descriptor = None
    for klass in tests_TestCategoryAllProperty.__mro__:
        if "testEnum" in klass.__dict__:
            descriptor = klass.__dict__["testEnum"]
            break
    assert isinstance(descriptor, property)

def test_tests_testcategoryallproperty_has_testBool():
    assert hasattr(tests_TestCategoryAllProperty, "testBool")
    descriptor = None
    for klass in tests_TestCategoryAllProperty.__mro__:
        if "testBool" in klass.__dict__:
            descriptor = klass.__dict__["testBool"]
            break
    assert isinstance(descriptor, property)

def test_tests_testcategoryallproperty_has_testFloat():
    assert hasattr(tests_TestCategoryAllProperty, "testFloat")
    descriptor = None
    for klass in tests_TestCategoryAllProperty.__mro__:
        if "testFloat" in klass.__dict__:
            descriptor = klass.__dict__["testFloat"]
            break
    assert isinstance(descriptor, property)

def test_tests_testcategoryallproperty_has_testInt():
    assert hasattr(tests_TestCategoryAllProperty, "testInt")
    descriptor = None
    for klass in tests_TestCategoryAllProperty.__mro__:
        if "testInt" in klass.__dict__:
            descriptor = klass.__dict__["testInt"]
            break
    assert isinstance(descriptor, property)

def test_tests_testcategoryallproperty_has_testResource():
    assert hasattr(tests_TestCategoryAllProperty, "testResource")
    descriptor = None
    for klass in tests_TestCategoryAllProperty.__mro__:
        if "testResource" in klass.__dict__:
            descriptor = klass.__dict__["testResource"]
            break
    assert isinstance(descriptor, property)

def test_tests_testcategoryallproperty_has_testString():
    assert hasattr(tests_TestCategoryAllProperty, "testString")
    descriptor = None
    for klass in tests_TestCategoryAllProperty.__mro__:
        if "testString" in klass.__dict__:
            descriptor = klass.__dict__["testString"]
            break
    assert isinstance(descriptor, property)

def test_enumtestenum_exists():
    # Check that the Enumeration exists
    assert EnumTestEnum is not None

def test_enumtestenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EnumTestEnum]
    expected_literals = [
        "MEDIUM",
        "HIGH",
        "INCREDIBLE",
        "LOW",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EnumTestEnum"


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
TestCategoryBase_strategy = st.builds(
    TestCategoryBase,
)
TestCategoryBeanAbstract_strategy = st.builds(
    TestCategoryBeanAbstract,
)
dmf_DObject_strategy = st.builds(
    dmf_DObject,
)
tests_TestCategoryExtends_strategy = st.builds(
    tests_TestCategoryExtends,
    testExtendsProperty=
        st.integers()
)
tests_TestCategoryBeanConcrete_strategy = st.builds(
    tests_TestCategoryBeanConcrete,
)
tests_ExternalTestType_strategy = st.builds(
    tests_ExternalTestType,
)
DObject_strategy = st.builds(
    DObject,
)
tests_TestCategoryBeanA_strategy = st.builds(
    tests_TestCategoryBeanA,
)
tests_EReferenceTest_strategy = st.builds(
    tests_EReferenceTest,
)
tests_TestCategoryReferenceArray_strategy = st.builds(
    tests_TestCategoryReferenceArray,
)
tests_TestCategoryIntrinsicArray_strategy = st.builds(
    tests_TestCategoryIntrinsicArray,
    testStringArrayStatic=
        safe_text,
    testStringArrayDynamic=
        safe_text
)
tests_TestCategoryBeanB_strategy = st.builds(
    tests_TestCategoryBeanB,
)
tests_TestMassParameters_strategy = st.builds(
    tests_TestMassParameters,
)
tests_TestCategoryBase_strategy = st.builds(
    tests_TestCategoryBase,
    testBaseProperty=
        st.integers()
)
tests_TestCategoryComposition_strategy = st.builds(
    tests_TestCategoryComposition,
)
tests_TestParameter_strategy = st.builds(
    tests_TestParameter,
    defaultValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
tests_TestCategoryBeanAbstract_strategy = st.builds(
    tests_TestCategoryBeanAbstract,
)
tests_TestCategoryCompositionArray_strategy = st.builds(
    tests_TestCategoryCompositionArray,
)
tests_TestCrossLinkedParametersWithCalculation_strategy = st.builds(
    tests_TestCrossLinkedParametersWithCalculation,
    calcedTrl=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
tests_TestCategoryReference_strategy = st.builds(
    tests_TestCategoryReference,
)
tests_TestCategoryAllProperty_strategy = st.builds(
    tests_TestCategoryAllProperty,
    testEnum=
        safe_text,
    testBool=
        st.booleans(),
    testFloat=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    testInt=
        st.integers(),
    testResource=
        safe_text,
    testString=
        safe_text
)

@given(instance=TestCategoryBase_strategy)
@settings(max_examples=50)
def test_testcategorybase_instantiation(instance):
    assert isinstance(instance, TestCategoryBase)

@given(instance=TestCategoryBeanAbstract_strategy)
@settings(max_examples=50)
def test_testcategorybeanabstract_instantiation(instance):
    assert isinstance(instance, TestCategoryBeanAbstract)

@given(instance=dmf_DObject_strategy)
@settings(max_examples=50)
def test_dmf_dobject_instantiation(instance):
    assert isinstance(instance, dmf_DObject)

@given(instance=tests_TestCategoryExtends_strategy)
@settings(max_examples=50)
def test_tests_testcategoryextends_instantiation(instance):
    assert isinstance(instance, tests_TestCategoryExtends)



@given(instance=tests_TestCategoryExtends_strategy)
def test_tests_testcategoryextends_testExtendsProperty_setter(instance):
    original = instance.testExtendsProperty
    instance.testExtendsProperty = original
    assert instance.testExtendsProperty == original

@given(instance=tests_TestCategoryBeanConcrete_strategy)
@settings(max_examples=50)
def test_tests_testcategorybeanconcrete_instantiation(instance):
    assert isinstance(instance, tests_TestCategoryBeanConcrete)

@given(instance=tests_ExternalTestType_strategy)
@settings(max_examples=50)
def test_tests_externaltesttype_instantiation(instance):
    assert isinstance(instance, tests_ExternalTestType)

@given(instance=DObject_strategy)
@settings(max_examples=50)
def test_dobject_instantiation(instance):
    assert isinstance(instance, DObject)

@given(instance=tests_TestCategoryBeanA_strategy)
@settings(max_examples=50)
def test_tests_testcategorybeana_instantiation(instance):
    assert isinstance(instance, tests_TestCategoryBeanA)

@given(instance=tests_EReferenceTest_strategy)
@settings(max_examples=50)
def test_tests_ereferencetest_instantiation(instance):
    assert isinstance(instance, tests_EReferenceTest)

@given(instance=tests_TestCategoryReferenceArray_strategy)
@settings(max_examples=50)
def test_tests_testcategoryreferencearray_instantiation(instance):
    assert isinstance(instance, tests_TestCategoryReferenceArray)

@given(instance=tests_TestCategoryIntrinsicArray_strategy)
@settings(max_examples=50)
def test_tests_testcategoryintrinsicarray_instantiation(instance):
    assert isinstance(instance, tests_TestCategoryIntrinsicArray)



@given(instance=tests_TestCategoryIntrinsicArray_strategy)
def test_tests_testcategoryintrinsicarray_testStringArrayStatic_setter(instance):
    original = instance.testStringArrayStatic
    instance.testStringArrayStatic = original
    assert instance.testStringArrayStatic == original



@given(instance=tests_TestCategoryIntrinsicArray_strategy)
def test_tests_testcategoryintrinsicarray_testStringArrayDynamic_setter(instance):
    original = instance.testStringArrayDynamic
    instance.testStringArrayDynamic = original
    assert instance.testStringArrayDynamic == original

@given(instance=tests_TestCategoryBeanB_strategy)
@settings(max_examples=50)
def test_tests_testcategorybeanb_instantiation(instance):
    assert isinstance(instance, tests_TestCategoryBeanB)

@given(instance=tests_TestMassParameters_strategy)
@settings(max_examples=50)
def test_tests_testmassparameters_instantiation(instance):
    assert isinstance(instance, tests_TestMassParameters)

@given(instance=tests_TestCategoryBase_strategy)
@settings(max_examples=50)
def test_tests_testcategorybase_instantiation(instance):
    assert isinstance(instance, tests_TestCategoryBase)



@given(instance=tests_TestCategoryBase_strategy)
def test_tests_testcategorybase_testBaseProperty_setter(instance):
    original = instance.testBaseProperty
    instance.testBaseProperty = original
    assert instance.testBaseProperty == original

@given(instance=tests_TestCategoryComposition_strategy)
@settings(max_examples=50)
def test_tests_testcategorycomposition_instantiation(instance):
    assert isinstance(instance, tests_TestCategoryComposition)

@given(instance=tests_TestParameter_strategy)
@settings(max_examples=50)
def test_tests_testparameter_instantiation(instance):
    assert isinstance(instance, tests_TestParameter)



@given(instance=tests_TestParameter_strategy)
def test_tests_testparameter_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=tests_TestCategoryBeanAbstract_strategy)
@settings(max_examples=50)
def test_tests_testcategorybeanabstract_instantiation(instance):
    assert isinstance(instance, tests_TestCategoryBeanAbstract)

@given(instance=tests_TestCategoryCompositionArray_strategy)
@settings(max_examples=50)
def test_tests_testcategorycompositionarray_instantiation(instance):
    assert isinstance(instance, tests_TestCategoryCompositionArray)

@given(instance=tests_TestCrossLinkedParametersWithCalculation_strategy)
@settings(max_examples=50)
def test_tests_testcrosslinkedparameterswithcalculation_instantiation(instance):
    assert isinstance(instance, tests_TestCrossLinkedParametersWithCalculation)



@given(instance=tests_TestCrossLinkedParametersWithCalculation_strategy)
def test_tests_testcrosslinkedparameterswithcalculation_calcedTrl_setter(instance):
    original = instance.calcedTrl
    instance.calcedTrl = original
    assert instance.calcedTrl == original

@given(instance=tests_TestCategoryReference_strategy)
@settings(max_examples=50)
def test_tests_testcategoryreference_instantiation(instance):
    assert isinstance(instance, tests_TestCategoryReference)

@given(instance=tests_TestCategoryAllProperty_strategy)
@settings(max_examples=50)
def test_tests_testcategoryallproperty_instantiation(instance):
    assert isinstance(instance, tests_TestCategoryAllProperty)



@given(instance=tests_TestCategoryAllProperty_strategy)
def test_tests_testcategoryallproperty_testEnum_setter(instance):
    original = instance.testEnum
    instance.testEnum = original
    assert instance.testEnum == original



@given(instance=tests_TestCategoryAllProperty_strategy)
def test_tests_testcategoryallproperty_testBool_setter(instance):
    original = instance.testBool
    instance.testBool = original
    assert instance.testBool == original



@given(instance=tests_TestCategoryAllProperty_strategy)
def test_tests_testcategoryallproperty_testFloat_setter(instance):
    original = instance.testFloat
    instance.testFloat = original
    assert instance.testFloat == original



@given(instance=tests_TestCategoryAllProperty_strategy)
def test_tests_testcategoryallproperty_testInt_setter(instance):
    original = instance.testInt
    instance.testInt = original
    assert instance.testInt == original



@given(instance=tests_TestCategoryAllProperty_strategy)
def test_tests_testcategoryallproperty_testResource_setter(instance):
    original = instance.testResource
    instance.testResource = original
    assert instance.testResource == original



@given(instance=tests_TestCategoryAllProperty_strategy)
def test_tests_testcategoryallproperty_testString_setter(instance):
    original = instance.testString
    instance.testString = original
    assert instance.testString == original
