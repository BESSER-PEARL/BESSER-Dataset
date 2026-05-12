import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    model6_UnsettableAttributes,
    model6_EmptyStringDefaultUnsettable,
    model6_EmptyStringDefault,
    model6_HasNillableAttribute,
    model6_CanReferenceLegacy,
    model6_G,
    model6_F,
    model6_E,
    model6_EObject,
    model6_C,
    model6_B,
    model6_D,
    model6_A,
    model6_PropertiesMapEntryValue,
    model6_Holdable,
    Holdable,
    model6_Thing,
    model6_Holder,
    model6_MyEnumListUnsettable,
    model6_MyEnumList,
    model6_BaseObject,
    model6_Root,
    model6_PropertiesMapEntry,
    model6_PropertiesMap,
    model6_UnorderedList,
    BaseObject,
    model6_ContainmentObject,
    model6_ReferenceObject,
    MyEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model6_unsettableattributes_is_not_abstract():
    assert not inspect.isabstract(model6_UnsettableAttributes)


def test_model6_unsettableattributes_constructor_exists():
    assert callable(model6_UnsettableAttributes.__init__)


def test_model6_unsettableattributes_constructor_args():
    sig = inspect.signature(model6_UnsettableAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "attrBoolean" in params, "Missing parameter 'attrBoolean'"
    assert "attrFloatObject" in params, "Missing parameter 'attrFloatObject'"
    assert "attrChar" in params, "Missing parameter 'attrChar'"
    assert "attrIntegerObject" in params, "Missing parameter 'attrIntegerObject'"
    assert "attrDouble" in params, "Missing parameter 'attrDouble'"
    assert "attrJavaObject" in params, "Missing parameter 'attrJavaObject'"
    assert "attrCharacterObject" in params, "Missing parameter 'attrCharacterObject'"
    assert "attrBigInteger" in params, "Missing parameter 'attrBigInteger'"
    assert "attrJavaClass" in params, "Missing parameter 'attrJavaClass'"
    assert "attrDate" in params, "Missing parameter 'attrDate'"
    assert "attrByteObject" in params, "Missing parameter 'attrByteObject'"
    assert "attrLongObject" in params, "Missing parameter 'attrLongObject'"
    assert "attrLong" in params, "Missing parameter 'attrLong'"
    assert "attrFloat" in params, "Missing parameter 'attrFloat'"
    assert "attrShortObject" in params, "Missing parameter 'attrShortObject'"
    assert "attrBigDecimal" in params, "Missing parameter 'attrBigDecimal'"
    assert "attrByte" in params, "Missing parameter 'attrByte'"
    assert "attrByteArray" in params, "Missing parameter 'attrByteArray'"
    assert "attrBooleanObject" in params, "Missing parameter 'attrBooleanObject'"
    assert "attrString" in params, "Missing parameter 'attrString'"
    assert "attrShort" in params, "Missing parameter 'attrShort'"
    assert "attrInt" in params, "Missing parameter 'attrInt'"
    assert "attrDoubleObject" in params, "Missing parameter 'attrDoubleObject'"

def test_model6_unsettableattributes_has_attrBoolean():
    assert hasattr(model6_UnsettableAttributes, "attrBoolean")
    descriptor = None
    for klass in model6_UnsettableAttributes.__mro__:
        if "attrBoolean" in klass.__dict__:
            descriptor = klass.__dict__["attrBoolean"]
            break
    assert isinstance(descriptor, property)

def test_model6_unsettableattributes_has_attrFloatObject():
    assert hasattr(model6_UnsettableAttributes, "attrFloatObject")
    descriptor = None
    for klass in model6_UnsettableAttributes.__mro__:
        if "attrFloatObject" in klass.__dict__:
            descriptor = klass.__dict__["attrFloatObject"]
            break
    assert isinstance(descriptor, property)

def test_model6_unsettableattributes_has_attrChar():
    assert hasattr(model6_UnsettableAttributes, "attrChar")
    descriptor = None
    for klass in model6_UnsettableAttributes.__mro__:
        if "attrChar" in klass.__dict__:
            descriptor = klass.__dict__["attrChar"]
            break
    assert isinstance(descriptor, property)

def test_model6_unsettableattributes_has_attrIntegerObject():
    assert hasattr(model6_UnsettableAttributes, "attrIntegerObject")
    descriptor = None
    for klass in model6_UnsettableAttributes.__mro__:
        if "attrIntegerObject" in klass.__dict__:
            descriptor = klass.__dict__["attrIntegerObject"]
            break
    assert isinstance(descriptor, property)

def test_model6_unsettableattributes_has_attrDouble():
    assert hasattr(model6_UnsettableAttributes, "attrDouble")
    descriptor = None
    for klass in model6_UnsettableAttributes.__mro__:
        if "attrDouble" in klass.__dict__:
            descriptor = klass.__dict__["attrDouble"]
            break
    assert isinstance(descriptor, property)

def test_model6_unsettableattributes_has_attrJavaObject():
    assert hasattr(model6_UnsettableAttributes, "attrJavaObject")
    descriptor = None
    for klass in model6_UnsettableAttributes.__mro__:
        if "attrJavaObject" in klass.__dict__:
            descriptor = klass.__dict__["attrJavaObject"]
            break
    assert isinstance(descriptor, property)

def test_model6_unsettableattributes_has_attrCharacterObject():
    assert hasattr(model6_UnsettableAttributes, "attrCharacterObject")
    descriptor = None
    for klass in model6_UnsettableAttributes.__mro__:
        if "attrCharacterObject" in klass.__dict__:
            descriptor = klass.__dict__["attrCharacterObject"]
            break
    assert isinstance(descriptor, property)

def test_model6_unsettableattributes_has_attrBigInteger():
    assert hasattr(model6_UnsettableAttributes, "attrBigInteger")
    descriptor = None
    for klass in model6_UnsettableAttributes.__mro__:
        if "attrBigInteger" in klass.__dict__:
            descriptor = klass.__dict__["attrBigInteger"]
            break
    assert isinstance(descriptor, property)

def test_model6_unsettableattributes_has_attrJavaClass():
    assert hasattr(model6_UnsettableAttributes, "attrJavaClass")
    descriptor = None
    for klass in model6_UnsettableAttributes.__mro__:
        if "attrJavaClass" in klass.__dict__:
            descriptor = klass.__dict__["attrJavaClass"]
            break
    assert isinstance(descriptor, property)

def test_model6_unsettableattributes_has_attrDate():
    assert hasattr(model6_UnsettableAttributes, "attrDate")
    descriptor = None
    for klass in model6_UnsettableAttributes.__mro__:
        if "attrDate" in klass.__dict__:
            descriptor = klass.__dict__["attrDate"]
            break
    assert isinstance(descriptor, property)

def test_model6_unsettableattributes_has_attrByteObject():
    assert hasattr(model6_UnsettableAttributes, "attrByteObject")
    descriptor = None
    for klass in model6_UnsettableAttributes.__mro__:
        if "attrByteObject" in klass.__dict__:
            descriptor = klass.__dict__["attrByteObject"]
            break
    assert isinstance(descriptor, property)

def test_model6_unsettableattributes_has_attrLongObject():
    assert hasattr(model6_UnsettableAttributes, "attrLongObject")
    descriptor = None
    for klass in model6_UnsettableAttributes.__mro__:
        if "attrLongObject" in klass.__dict__:
            descriptor = klass.__dict__["attrLongObject"]
            break
    assert isinstance(descriptor, property)

def test_model6_unsettableattributes_has_attrLong():
    assert hasattr(model6_UnsettableAttributes, "attrLong")
    descriptor = None
    for klass in model6_UnsettableAttributes.__mro__:
        if "attrLong" in klass.__dict__:
            descriptor = klass.__dict__["attrLong"]
            break
    assert isinstance(descriptor, property)

def test_model6_unsettableattributes_has_attrFloat():
    assert hasattr(model6_UnsettableAttributes, "attrFloat")
    descriptor = None
    for klass in model6_UnsettableAttributes.__mro__:
        if "attrFloat" in klass.__dict__:
            descriptor = klass.__dict__["attrFloat"]
            break
    assert isinstance(descriptor, property)

def test_model6_unsettableattributes_has_attrShortObject():
    assert hasattr(model6_UnsettableAttributes, "attrShortObject")
    descriptor = None
    for klass in model6_UnsettableAttributes.__mro__:
        if "attrShortObject" in klass.__dict__:
            descriptor = klass.__dict__["attrShortObject"]
            break
    assert isinstance(descriptor, property)

def test_model6_unsettableattributes_has_attrBigDecimal():
    assert hasattr(model6_UnsettableAttributes, "attrBigDecimal")
    descriptor = None
    for klass in model6_UnsettableAttributes.__mro__:
        if "attrBigDecimal" in klass.__dict__:
            descriptor = klass.__dict__["attrBigDecimal"]
            break
    assert isinstance(descriptor, property)

def test_model6_unsettableattributes_has_attrByte():
    assert hasattr(model6_UnsettableAttributes, "attrByte")
    descriptor = None
    for klass in model6_UnsettableAttributes.__mro__:
        if "attrByte" in klass.__dict__:
            descriptor = klass.__dict__["attrByte"]
            break
    assert isinstance(descriptor, property)

def test_model6_unsettableattributes_has_attrByteArray():
    assert hasattr(model6_UnsettableAttributes, "attrByteArray")
    descriptor = None
    for klass in model6_UnsettableAttributes.__mro__:
        if "attrByteArray" in klass.__dict__:
            descriptor = klass.__dict__["attrByteArray"]
            break
    assert isinstance(descriptor, property)

def test_model6_unsettableattributes_has_attrBooleanObject():
    assert hasattr(model6_UnsettableAttributes, "attrBooleanObject")
    descriptor = None
    for klass in model6_UnsettableAttributes.__mro__:
        if "attrBooleanObject" in klass.__dict__:
            descriptor = klass.__dict__["attrBooleanObject"]
            break
    assert isinstance(descriptor, property)

def test_model6_unsettableattributes_has_attrString():
    assert hasattr(model6_UnsettableAttributes, "attrString")
    descriptor = None
    for klass in model6_UnsettableAttributes.__mro__:
        if "attrString" in klass.__dict__:
            descriptor = klass.__dict__["attrString"]
            break
    assert isinstance(descriptor, property)

def test_model6_unsettableattributes_has_attrShort():
    assert hasattr(model6_UnsettableAttributes, "attrShort")
    descriptor = None
    for klass in model6_UnsettableAttributes.__mro__:
        if "attrShort" in klass.__dict__:
            descriptor = klass.__dict__["attrShort"]
            break
    assert isinstance(descriptor, property)

def test_model6_unsettableattributes_has_attrInt():
    assert hasattr(model6_UnsettableAttributes, "attrInt")
    descriptor = None
    for klass in model6_UnsettableAttributes.__mro__:
        if "attrInt" in klass.__dict__:
            descriptor = klass.__dict__["attrInt"]
            break
    assert isinstance(descriptor, property)

def test_model6_unsettableattributes_has_attrDoubleObject():
    assert hasattr(model6_UnsettableAttributes, "attrDoubleObject")
    descriptor = None
    for klass in model6_UnsettableAttributes.__mro__:
        if "attrDoubleObject" in klass.__dict__:
            descriptor = klass.__dict__["attrDoubleObject"]
            break
    assert isinstance(descriptor, property)



def test_model6_emptystringdefaultunsettable_is_not_abstract():
    assert not inspect.isabstract(model6_EmptyStringDefaultUnsettable)


def test_model6_emptystringdefaultunsettable_constructor_exists():
    assert callable(model6_EmptyStringDefaultUnsettable.__init__)


def test_model6_emptystringdefaultunsettable_constructor_args():
    sig = inspect.signature(model6_EmptyStringDefaultUnsettable.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_model6_emptystringdefaultunsettable_has_attribute():
    assert hasattr(model6_EmptyStringDefaultUnsettable, "attribute")
    descriptor = None
    for klass in model6_EmptyStringDefaultUnsettable.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_model6_emptystringdefault_is_not_abstract():
    assert not inspect.isabstract(model6_EmptyStringDefault)


def test_model6_emptystringdefault_constructor_exists():
    assert callable(model6_EmptyStringDefault.__init__)


def test_model6_emptystringdefault_constructor_args():
    sig = inspect.signature(model6_EmptyStringDefault.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_model6_emptystringdefault_has_attribute():
    assert hasattr(model6_EmptyStringDefault, "attribute")
    descriptor = None
    for klass in model6_EmptyStringDefault.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_model6_hasnillableattribute_is_not_abstract():
    assert not inspect.isabstract(model6_HasNillableAttribute)


def test_model6_hasnillableattribute_constructor_exists():
    assert callable(model6_HasNillableAttribute.__init__)


def test_model6_hasnillableattribute_constructor_args():
    sig = inspect.signature(model6_HasNillableAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "nillable" in params, "Missing parameter 'nillable'"

def test_model6_hasnillableattribute_has_nillable():
    assert hasattr(model6_HasNillableAttribute, "nillable")
    descriptor = None
    for klass in model6_HasNillableAttribute.__mro__:
        if "nillable" in klass.__dict__:
            descriptor = klass.__dict__["nillable"]
            break
    assert isinstance(descriptor, property)



def test_model6_canreferencelegacy_is_not_abstract():
    assert not inspect.isabstract(model6_CanReferenceLegacy)


def test_model6_canreferencelegacy_constructor_exists():
    assert callable(model6_CanReferenceLegacy.__init__)


def test_model6_canreferencelegacy_constructor_args():
    sig = inspect.signature(model6_CanReferenceLegacy.__init__)
    params = list(sig.parameters.keys())



def test_model6_g_is_not_abstract():
    assert not inspect.isabstract(model6_G)


def test_model6_g_constructor_exists():
    assert callable(model6_G.__init__)


def test_model6_g_constructor_args():
    sig = inspect.signature(model6_G.__init__)
    params = list(sig.parameters.keys())
    assert "dummy" in params, "Missing parameter 'dummy'"

def test_model6_g_has_dummy():
    assert hasattr(model6_G, "dummy")
    descriptor = None
    for klass in model6_G.__mro__:
        if "dummy" in klass.__dict__:
            descriptor = klass.__dict__["dummy"]
            break
    assert isinstance(descriptor, property)



def test_model6_f_is_not_abstract():
    assert not inspect.isabstract(model6_F)


def test_model6_f_constructor_exists():
    assert callable(model6_F.__init__)


def test_model6_f_constructor_args():
    sig = inspect.signature(model6_F.__init__)
    params = list(sig.parameters.keys())



def test_model6_e_is_not_abstract():
    assert not inspect.isabstract(model6_E)


def test_model6_e_constructor_exists():
    assert callable(model6_E.__init__)


def test_model6_e_constructor_args():
    sig = inspect.signature(model6_E.__init__)
    params = list(sig.parameters.keys())



def test_model6_eobject_is_not_abstract():
    assert not inspect.isabstract(model6_EObject)


def test_model6_eobject_constructor_exists():
    assert callable(model6_EObject.__init__)


def test_model6_eobject_constructor_args():
    sig = inspect.signature(model6_EObject.__init__)
    params = list(sig.parameters.keys())



def test_model6_c_is_not_abstract():
    assert not inspect.isabstract(model6_C)


def test_model6_c_constructor_exists():
    assert callable(model6_C.__init__)


def test_model6_c_constructor_args():
    sig = inspect.signature(model6_C.__init__)
    params = list(sig.parameters.keys())



def test_model6_b_is_not_abstract():
    assert not inspect.isabstract(model6_B)


def test_model6_b_constructor_exists():
    assert callable(model6_B.__init__)


def test_model6_b_constructor_args():
    sig = inspect.signature(model6_B.__init__)
    params = list(sig.parameters.keys())



def test_model6_d_is_not_abstract():
    assert not inspect.isabstract(model6_D)


def test_model6_d_constructor_exists():
    assert callable(model6_D.__init__)


def test_model6_d_constructor_args():
    sig = inspect.signature(model6_D.__init__)
    params = list(sig.parameters.keys())



def test_model6_a_is_not_abstract():
    assert not inspect.isabstract(model6_A)


def test_model6_a_constructor_exists():
    assert callable(model6_A.__init__)


def test_model6_a_constructor_args():
    sig = inspect.signature(model6_A.__init__)
    params = list(sig.parameters.keys())



def test_model6_propertiesmapentryvalue_is_not_abstract():
    assert not inspect.isabstract(model6_PropertiesMapEntryValue)


def test_model6_propertiesmapentryvalue_constructor_exists():
    assert callable(model6_PropertiesMapEntryValue.__init__)


def test_model6_propertiesmapentryvalue_constructor_args():
    sig = inspect.signature(model6_PropertiesMapEntryValue.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_model6_propertiesmapentryvalue_has_label():
    assert hasattr(model6_PropertiesMapEntryValue, "label")
    descriptor = None
    for klass in model6_PropertiesMapEntryValue.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_model6_holdable_is_not_abstract():
    assert not inspect.isabstract(model6_Holdable)


def test_model6_holdable_constructor_exists():
    assert callable(model6_Holdable.__init__)


def test_model6_holdable_constructor_args():
    sig = inspect.signature(model6_Holdable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model6_holdable_has_name():
    assert hasattr(model6_Holdable, "name")
    descriptor = None
    for klass in model6_Holdable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_holdable_is_not_abstract():
    assert not inspect.isabstract(Holdable)


def test_holdable_constructor_exists():
    assert callable(Holdable.__init__)


def test_holdable_constructor_args():
    sig = inspect.signature(Holdable.__init__)
    params = list(sig.parameters.keys())



def test_model6_thing_is_not_abstract():
    assert not inspect.isabstract(model6_Thing)


def test_model6_thing_constructor_exists():
    assert callable(model6_Thing.__init__)


def test_model6_thing_constructor_args():
    sig = inspect.signature(model6_Thing.__init__)
    params = list(sig.parameters.keys())



def test_model6_holder_is_not_abstract():
    assert not inspect.isabstract(model6_Holder)


def test_model6_holder_constructor_exists():
    assert callable(model6_Holder.__init__)


def test_model6_holder_constructor_args():
    sig = inspect.signature(model6_Holder.__init__)
    params = list(sig.parameters.keys())



def test_model6_myenumlistunsettable_is_not_abstract():
    assert not inspect.isabstract(model6_MyEnumListUnsettable)


def test_model6_myenumlistunsettable_constructor_exists():
    assert callable(model6_MyEnumListUnsettable.__init__)


def test_model6_myenumlistunsettable_constructor_args():
    sig = inspect.signature(model6_MyEnumListUnsettable.__init__)
    params = list(sig.parameters.keys())
    assert "myEnum" in params, "Missing parameter 'myEnum'"

def test_model6_myenumlistunsettable_has_myEnum():
    assert hasattr(model6_MyEnumListUnsettable, "myEnum")
    descriptor = None
    for klass in model6_MyEnumListUnsettable.__mro__:
        if "myEnum" in klass.__dict__:
            descriptor = klass.__dict__["myEnum"]
            break
    assert isinstance(descriptor, property)



def test_model6_myenumlist_is_not_abstract():
    assert not inspect.isabstract(model6_MyEnumList)


def test_model6_myenumlist_constructor_exists():
    assert callable(model6_MyEnumList.__init__)


def test_model6_myenumlist_constructor_args():
    sig = inspect.signature(model6_MyEnumList.__init__)
    params = list(sig.parameters.keys())
    assert "myEnum" in params, "Missing parameter 'myEnum'"

def test_model6_myenumlist_has_myEnum():
    assert hasattr(model6_MyEnumList, "myEnum")
    descriptor = None
    for klass in model6_MyEnumList.__mro__:
        if "myEnum" in klass.__dict__:
            descriptor = klass.__dict__["myEnum"]
            break
    assert isinstance(descriptor, property)



def test_model6_baseobject_is_not_abstract():
    assert not inspect.isabstract(model6_BaseObject)


def test_model6_baseobject_constructor_exists():
    assert callable(model6_BaseObject.__init__)


def test_model6_baseobject_constructor_args():
    sig = inspect.signature(model6_BaseObject.__init__)
    params = list(sig.parameters.keys())
    assert "attributeList" in params, "Missing parameter 'attributeList'"
    assert "attributeOptional" in params, "Missing parameter 'attributeOptional'"
    assert "attributeRequired" in params, "Missing parameter 'attributeRequired'"

def test_model6_baseobject_has_attributeList():
    assert hasattr(model6_BaseObject, "attributeList")
    descriptor = None
    for klass in model6_BaseObject.__mro__:
        if "attributeList" in klass.__dict__:
            descriptor = klass.__dict__["attributeList"]
            break
    assert isinstance(descriptor, property)

def test_model6_baseobject_has_attributeOptional():
    assert hasattr(model6_BaseObject, "attributeOptional")
    descriptor = None
    for klass in model6_BaseObject.__mro__:
        if "attributeOptional" in klass.__dict__:
            descriptor = klass.__dict__["attributeOptional"]
            break
    assert isinstance(descriptor, property)

def test_model6_baseobject_has_attributeRequired():
    assert hasattr(model6_BaseObject, "attributeRequired")
    descriptor = None
    for klass in model6_BaseObject.__mro__:
        if "attributeRequired" in klass.__dict__:
            descriptor = klass.__dict__["attributeRequired"]
            break
    assert isinstance(descriptor, property)



def test_model6_root_is_not_abstract():
    assert not inspect.isabstract(model6_Root)


def test_model6_root_constructor_exists():
    assert callable(model6_Root.__init__)


def test_model6_root_constructor_args():
    sig = inspect.signature(model6_Root.__init__)
    params = list(sig.parameters.keys())



def test_model6_propertiesmapentry_is_not_abstract():
    assert not inspect.isabstract(model6_PropertiesMapEntry)


def test_model6_propertiesmapentry_constructor_exists():
    assert callable(model6_PropertiesMapEntry.__init__)


def test_model6_propertiesmapentry_constructor_args():
    sig = inspect.signature(model6_PropertiesMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_model6_propertiesmapentry_has_key():
    assert hasattr(model6_PropertiesMapEntry, "key")
    descriptor = None
    for klass in model6_PropertiesMapEntry.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_model6_propertiesmap_is_not_abstract():
    assert not inspect.isabstract(model6_PropertiesMap)


def test_model6_propertiesmap_constructor_exists():
    assert callable(model6_PropertiesMap.__init__)


def test_model6_propertiesmap_constructor_args():
    sig = inspect.signature(model6_PropertiesMap.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_model6_propertiesmap_has_label():
    assert hasattr(model6_PropertiesMap, "label")
    descriptor = None
    for klass in model6_PropertiesMap.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_model6_unorderedlist_is_not_abstract():
    assert not inspect.isabstract(model6_UnorderedList)


def test_model6_unorderedlist_constructor_exists():
    assert callable(model6_UnorderedList.__init__)


def test_model6_unorderedlist_constructor_args():
    sig = inspect.signature(model6_UnorderedList.__init__)
    params = list(sig.parameters.keys())



def test_baseobject_is_not_abstract():
    assert not inspect.isabstract(BaseObject)


def test_baseobject_constructor_exists():
    assert callable(BaseObject.__init__)


def test_baseobject_constructor_args():
    sig = inspect.signature(BaseObject.__init__)
    params = list(sig.parameters.keys())



def test_model6_containmentobject_is_not_abstract():
    assert not inspect.isabstract(model6_ContainmentObject)


def test_model6_containmentobject_constructor_exists():
    assert callable(model6_ContainmentObject.__init__)


def test_model6_containmentobject_constructor_args():
    sig = inspect.signature(model6_ContainmentObject.__init__)
    params = list(sig.parameters.keys())



def test_model6_referenceobject_is_not_abstract():
    assert not inspect.isabstract(model6_ReferenceObject)


def test_model6_referenceobject_constructor_exists():
    assert callable(model6_ReferenceObject.__init__)


def test_model6_referenceobject_constructor_args():
    sig = inspect.signature(model6_ReferenceObject.__init__)
    params = list(sig.parameters.keys())

def test_myenum_exists():
    # Check that the Enumeration exists
    assert MyEnum is not None

def test_myenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MyEnum]
    expected_literals = [
        "TWO",
        "ZERO",
        "ONE",
        "THREE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MyEnum"


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
model6_UnsettableAttributes_strategy = st.builds(
    model6_UnsettableAttributes,
    attrBoolean=
        st.booleans(),
    attrFloatObject=
        safe_text,
    attrChar=
        safe_text,
    attrIntegerObject=
        safe_text,
    attrDouble=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    attrJavaObject=
        safe_text,
    attrCharacterObject=
        safe_text,
    attrBigInteger=
        safe_text,
    attrJavaClass=
        safe_text,
    attrDate=
        st.dates(),
    attrByteObject=
        safe_text,
    attrLongObject=
        safe_text,
    attrLong=
        safe_text,
    attrFloat=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    attrShortObject=
        safe_text,
    attrBigDecimal=
        safe_text,
    attrByte=
        safe_text,
    attrByteArray=
        safe_text,
    attrBooleanObject=
        safe_text,
    attrString=
        safe_text,
    attrShort=
        safe_text,
    attrInt=
        st.integers(),
    attrDoubleObject=
        safe_text
)
model6_EmptyStringDefaultUnsettable_strategy = st.builds(
    model6_EmptyStringDefaultUnsettable,
    attribute=
        safe_text
)
model6_EmptyStringDefault_strategy = st.builds(
    model6_EmptyStringDefault,
    attribute=
        safe_text
)
model6_HasNillableAttribute_strategy = st.builds(
    model6_HasNillableAttribute,
    nillable=
        safe_text
)
model6_CanReferenceLegacy_strategy = st.builds(
    model6_CanReferenceLegacy,
)
model6_G_strategy = st.builds(
    model6_G,
    dummy=
        safe_text
)
model6_F_strategy = st.builds(
    model6_F,
)
model6_E_strategy = st.builds(
    model6_E,
)
model6_EObject_strategy = st.builds(
    model6_EObject,
)
model6_C_strategy = st.builds(
    model6_C,
)
model6_B_strategy = st.builds(
    model6_B,
)
model6_D_strategy = st.builds(
    model6_D,
)
model6_A_strategy = st.builds(
    model6_A,
)
model6_PropertiesMapEntryValue_strategy = st.builds(
    model6_PropertiesMapEntryValue,
    label=
        safe_text
)
model6_Holdable_strategy = st.builds(
    model6_Holdable,
    name=
        safe_text
)
Holdable_strategy = st.builds(
    Holdable,
)
model6_Thing_strategy = st.builds(
    model6_Thing,
)
model6_Holder_strategy = st.builds(
    model6_Holder,
)
model6_MyEnumListUnsettable_strategy = st.builds(
    model6_MyEnumListUnsettable,
    myEnum=
        safe_text
)
model6_MyEnumList_strategy = st.builds(
    model6_MyEnumList,
    myEnum=
        safe_text
)
model6_BaseObject_strategy = st.builds(
    model6_BaseObject,
    attributeList=
        safe_text,
    attributeOptional=
        safe_text,
    attributeRequired=
        safe_text
)
model6_Root_strategy = st.builds(
    model6_Root,
)
model6_PropertiesMapEntry_strategy = st.builds(
    model6_PropertiesMapEntry,
    key=
        safe_text
)
model6_PropertiesMap_strategy = st.builds(
    model6_PropertiesMap,
    label=
        safe_text
)
model6_UnorderedList_strategy = st.builds(
    model6_UnorderedList,
)
BaseObject_strategy = st.builds(
    BaseObject,
)
model6_ContainmentObject_strategy = st.builds(
    model6_ContainmentObject,
)
model6_ReferenceObject_strategy = st.builds(
    model6_ReferenceObject,
)

@given(instance=model6_UnsettableAttributes_strategy)
@settings(max_examples=50)
def test_model6_unsettableattributes_instantiation(instance):
    assert isinstance(instance, model6_UnsettableAttributes)



@given(instance=model6_UnsettableAttributes_strategy)
def test_model6_unsettableattributes_attrBoolean_setter(instance):
    original = instance.attrBoolean
    instance.attrBoolean = original
    assert instance.attrBoolean == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_model6_unsettableattributes_attrFloatObject_setter(instance):
    original = instance.attrFloatObject
    instance.attrFloatObject = original
    assert instance.attrFloatObject == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_model6_unsettableattributes_attrChar_setter(instance):
    original = instance.attrChar
    instance.attrChar = original
    assert instance.attrChar == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_model6_unsettableattributes_attrIntegerObject_setter(instance):
    original = instance.attrIntegerObject
    instance.attrIntegerObject = original
    assert instance.attrIntegerObject == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_model6_unsettableattributes_attrDouble_setter(instance):
    original = instance.attrDouble
    instance.attrDouble = original
    assert instance.attrDouble == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_model6_unsettableattributes_attrJavaObject_setter(instance):
    original = instance.attrJavaObject
    instance.attrJavaObject = original
    assert instance.attrJavaObject == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_model6_unsettableattributes_attrCharacterObject_setter(instance):
    original = instance.attrCharacterObject
    instance.attrCharacterObject = original
    assert instance.attrCharacterObject == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_model6_unsettableattributes_attrBigInteger_setter(instance):
    original = instance.attrBigInteger
    instance.attrBigInteger = original
    assert instance.attrBigInteger == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_model6_unsettableattributes_attrJavaClass_setter(instance):
    original = instance.attrJavaClass
    instance.attrJavaClass = original
    assert instance.attrJavaClass == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_model6_unsettableattributes_attrDate_setter(instance):
    original = instance.attrDate
    instance.attrDate = original
    assert instance.attrDate == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_model6_unsettableattributes_attrByteObject_setter(instance):
    original = instance.attrByteObject
    instance.attrByteObject = original
    assert instance.attrByteObject == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_model6_unsettableattributes_attrLongObject_setter(instance):
    original = instance.attrLongObject
    instance.attrLongObject = original
    assert instance.attrLongObject == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_model6_unsettableattributes_attrLong_setter(instance):
    original = instance.attrLong
    instance.attrLong = original
    assert instance.attrLong == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_model6_unsettableattributes_attrFloat_setter(instance):
    original = instance.attrFloat
    instance.attrFloat = original
    assert instance.attrFloat == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_model6_unsettableattributes_attrShortObject_setter(instance):
    original = instance.attrShortObject
    instance.attrShortObject = original
    assert instance.attrShortObject == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_model6_unsettableattributes_attrBigDecimal_setter(instance):
    original = instance.attrBigDecimal
    instance.attrBigDecimal = original
    assert instance.attrBigDecimal == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_model6_unsettableattributes_attrByte_setter(instance):
    original = instance.attrByte
    instance.attrByte = original
    assert instance.attrByte == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_model6_unsettableattributes_attrByteArray_setter(instance):
    original = instance.attrByteArray
    instance.attrByteArray = original
    assert instance.attrByteArray == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_model6_unsettableattributes_attrBooleanObject_setter(instance):
    original = instance.attrBooleanObject
    instance.attrBooleanObject = original
    assert instance.attrBooleanObject == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_model6_unsettableattributes_attrString_setter(instance):
    original = instance.attrString
    instance.attrString = original
    assert instance.attrString == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_model6_unsettableattributes_attrShort_setter(instance):
    original = instance.attrShort
    instance.attrShort = original
    assert instance.attrShort == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_model6_unsettableattributes_attrInt_setter(instance):
    original = instance.attrInt
    instance.attrInt = original
    assert instance.attrInt == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_model6_unsettableattributes_attrDoubleObject_setter(instance):
    original = instance.attrDoubleObject
    instance.attrDoubleObject = original
    assert instance.attrDoubleObject == original

@given(instance=model6_EmptyStringDefaultUnsettable_strategy)
@settings(max_examples=50)
def test_model6_emptystringdefaultunsettable_instantiation(instance):
    assert isinstance(instance, model6_EmptyStringDefaultUnsettable)



@given(instance=model6_EmptyStringDefaultUnsettable_strategy)
def test_model6_emptystringdefaultunsettable_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=model6_EmptyStringDefault_strategy)
@settings(max_examples=50)
def test_model6_emptystringdefault_instantiation(instance):
    assert isinstance(instance, model6_EmptyStringDefault)



@given(instance=model6_EmptyStringDefault_strategy)
def test_model6_emptystringdefault_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=model6_HasNillableAttribute_strategy)
@settings(max_examples=50)
def test_model6_hasnillableattribute_instantiation(instance):
    assert isinstance(instance, model6_HasNillableAttribute)



@given(instance=model6_HasNillableAttribute_strategy)
def test_model6_hasnillableattribute_nillable_setter(instance):
    original = instance.nillable
    instance.nillable = original
    assert instance.nillable == original

@given(instance=model6_CanReferenceLegacy_strategy)
@settings(max_examples=50)
def test_model6_canreferencelegacy_instantiation(instance):
    assert isinstance(instance, model6_CanReferenceLegacy)

@given(instance=model6_G_strategy)
@settings(max_examples=50)
def test_model6_g_instantiation(instance):
    assert isinstance(instance, model6_G)



@given(instance=model6_G_strategy)
def test_model6_g_dummy_setter(instance):
    original = instance.dummy
    instance.dummy = original
    assert instance.dummy == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model6_G_strategy)
@settings(max_examples=30)
def test_model6_g_isattributemodified_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isAttributeModified()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isAttributeModified).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isAttributeModified' in model6_G is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isAttributeModified' in model6_G did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isAttributeModified' in model6_G is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model6_G_strategy)
@settings(max_examples=30)
def test_model6_g_islistmodified_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isListModified()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isListModified).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isListModified' in model6_G is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isListModified' in model6_G did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isListModified' in model6_G is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model6_G_strategy)
@settings(max_examples=30)
def test_model6_g_isreferencemodified_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isReferenceModified()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isReferenceModified).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isReferenceModified' in model6_G is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isReferenceModified' in model6_G did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isReferenceModified' in model6_G is not implemented or raised an error")

@given(instance=model6_F_strategy)
@settings(max_examples=50)
def test_model6_f_instantiation(instance):
    assert isinstance(instance, model6_F)

@given(instance=model6_E_strategy)
@settings(max_examples=50)
def test_model6_e_instantiation(instance):
    assert isinstance(instance, model6_E)

@given(instance=model6_EObject_strategy)
@settings(max_examples=50)
def test_model6_eobject_instantiation(instance):
    assert isinstance(instance, model6_EObject)

@given(instance=model6_C_strategy)
@settings(max_examples=50)
def test_model6_c_instantiation(instance):
    assert isinstance(instance, model6_C)

@given(instance=model6_B_strategy)
@settings(max_examples=50)
def test_model6_b_instantiation(instance):
    assert isinstance(instance, model6_B)

@given(instance=model6_D_strategy)
@settings(max_examples=50)
def test_model6_d_instantiation(instance):
    assert isinstance(instance, model6_D)

@given(instance=model6_A_strategy)
@settings(max_examples=50)
def test_model6_a_instantiation(instance):
    assert isinstance(instance, model6_A)

@given(instance=model6_PropertiesMapEntryValue_strategy)
@settings(max_examples=50)
def test_model6_propertiesmapentryvalue_instantiation(instance):
    assert isinstance(instance, model6_PropertiesMapEntryValue)



@given(instance=model6_PropertiesMapEntryValue_strategy)
def test_model6_propertiesmapentryvalue_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=model6_Holdable_strategy)
@settings(max_examples=50)
def test_model6_holdable_instantiation(instance):
    assert isinstance(instance, model6_Holdable)



@given(instance=model6_Holdable_strategy)
def test_model6_holdable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Holdable_strategy)
@settings(max_examples=50)
def test_holdable_instantiation(instance):
    assert isinstance(instance, Holdable)

@given(instance=model6_Thing_strategy)
@settings(max_examples=50)
def test_model6_thing_instantiation(instance):
    assert isinstance(instance, model6_Thing)

@given(instance=model6_Holder_strategy)
@settings(max_examples=50)
def test_model6_holder_instantiation(instance):
    assert isinstance(instance, model6_Holder)

@given(instance=model6_MyEnumListUnsettable_strategy)
@settings(max_examples=50)
def test_model6_myenumlistunsettable_instantiation(instance):
    assert isinstance(instance, model6_MyEnumListUnsettable)



@given(instance=model6_MyEnumListUnsettable_strategy)
def test_model6_myenumlistunsettable_myEnum_setter(instance):
    original = instance.myEnum
    instance.myEnum = original
    assert instance.myEnum == original

@given(instance=model6_MyEnumList_strategy)
@settings(max_examples=50)
def test_model6_myenumlist_instantiation(instance):
    assert isinstance(instance, model6_MyEnumList)



@given(instance=model6_MyEnumList_strategy)
def test_model6_myenumlist_myEnum_setter(instance):
    original = instance.myEnum
    instance.myEnum = original
    assert instance.myEnum == original

@given(instance=model6_BaseObject_strategy)
@settings(max_examples=50)
def test_model6_baseobject_instantiation(instance):
    assert isinstance(instance, model6_BaseObject)



@given(instance=model6_BaseObject_strategy)
def test_model6_baseobject_attributeList_setter(instance):
    original = instance.attributeList
    instance.attributeList = original
    assert instance.attributeList == original



@given(instance=model6_BaseObject_strategy)
def test_model6_baseobject_attributeOptional_setter(instance):
    original = instance.attributeOptional
    instance.attributeOptional = original
    assert instance.attributeOptional == original



@given(instance=model6_BaseObject_strategy)
def test_model6_baseobject_attributeRequired_setter(instance):
    original = instance.attributeRequired
    instance.attributeRequired = original
    assert instance.attributeRequired == original

@given(instance=model6_Root_strategy)
@settings(max_examples=50)
def test_model6_root_instantiation(instance):
    assert isinstance(instance, model6_Root)

@given(instance=model6_PropertiesMapEntry_strategy)
@settings(max_examples=50)
def test_model6_propertiesmapentry_instantiation(instance):
    assert isinstance(instance, model6_PropertiesMapEntry)



@given(instance=model6_PropertiesMapEntry_strategy)
def test_model6_propertiesmapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=model6_PropertiesMap_strategy)
@settings(max_examples=50)
def test_model6_propertiesmap_instantiation(instance):
    assert isinstance(instance, model6_PropertiesMap)



@given(instance=model6_PropertiesMap_strategy)
def test_model6_propertiesmap_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=model6_UnorderedList_strategy)
@settings(max_examples=50)
def test_model6_unorderedlist_instantiation(instance):
    assert isinstance(instance, model6_UnorderedList)

@given(instance=BaseObject_strategy)
@settings(max_examples=50)
def test_baseobject_instantiation(instance):
    assert isinstance(instance, BaseObject)

@given(instance=model6_ContainmentObject_strategy)
@settings(max_examples=50)
def test_model6_containmentobject_instantiation(instance):
    assert isinstance(instance, model6_ContainmentObject)

@given(instance=model6_ReferenceObject_strategy)
@settings(max_examples=50)
def test_model6_referenceobject_instantiation(instance):
    assert isinstance(instance, model6_ReferenceObject)
