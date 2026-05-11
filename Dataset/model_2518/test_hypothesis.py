import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    model6::UnsettableAttributes,
    model6::EmptyStringDefaultUnsettable,
    model6::EmptyStringDefault,
    model6::HasNillableAttribute,
    model6::CanReferenceLegacy,
    model6::G,
    model6::F,
    model6::E,
    model6::EObject,
    model6::C,
    model6::B,
    model6::D,
    model6::A,
    model6::PropertiesMapEntryValue,
    model6::Holdable,
    Holdable,
    model6::Thing,
    model6::Holder,
    model6::MyEnumListUnsettable,
    model6::MyEnumList,
    model6::BaseObject,
    model6::Root,
    model6::PropertiesMapEntry,
    model6::PropertiesMap,
    model6::UnorderedList,
    BaseObject,
    model6::ContainmentObject,
    model6::ReferenceObject,
    MyEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model6::unsettableattributes_is_not_abstract():
    assert not inspect.isabstract(model6::UnsettableAttributes)


def test_model6::unsettableattributes_constructor_exists():
    assert callable(model6::UnsettableAttributes.__init__)


def test_model6::unsettableattributes_constructor_args():
    sig = inspect.signature(model6::UnsettableAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "attrShort" in params, "Missing parameter 'attrShort'"
    assert "attrCharacterObject" in params, "Missing parameter 'attrCharacterObject'"
    assert "attrChar" in params, "Missing parameter 'attrChar'"
    assert "attrFloat" in params, "Missing parameter 'attrFloat'"
    assert "attrBoolean" in params, "Missing parameter 'attrBoolean'"
    assert "attrJavaClass" in params, "Missing parameter 'attrJavaClass'"
    assert "attrBigDecimal" in params, "Missing parameter 'attrBigDecimal'"
    assert "attrBigInteger" in params, "Missing parameter 'attrBigInteger'"
    assert "attrByte" in params, "Missing parameter 'attrByte'"
    assert "attrString" in params, "Missing parameter 'attrString'"
    assert "attrIntegerObject" in params, "Missing parameter 'attrIntegerObject'"
    assert "attrBooleanObject" in params, "Missing parameter 'attrBooleanObject'"
    assert "attrDoubleObject" in params, "Missing parameter 'attrDoubleObject'"
    assert "attrLong" in params, "Missing parameter 'attrLong'"
    assert "attrByteObject" in params, "Missing parameter 'attrByteObject'"
    assert "attrJavaObject" in params, "Missing parameter 'attrJavaObject'"
    assert "attrFloatObject" in params, "Missing parameter 'attrFloatObject'"
    assert "attrDate" in params, "Missing parameter 'attrDate'"
    assert "attrShortObject" in params, "Missing parameter 'attrShortObject'"
    assert "attrByteArray" in params, "Missing parameter 'attrByteArray'"
    assert "attrInt" in params, "Missing parameter 'attrInt'"
    assert "attrLongObject" in params, "Missing parameter 'attrLongObject'"
    assert "attrDouble" in params, "Missing parameter 'attrDouble'"

def test_model6::unsettableattributes_has_attrShort():
    assert hasattr(model6::UnsettableAttributes, "attrShort")
    descriptor = None
    for klass in model6::UnsettableAttributes.__mro__:
        if "attrShort" in klass.__dict__:
            descriptor = klass.__dict__["attrShort"]
            break
    assert isinstance(descriptor, property)

def test_model6::unsettableattributes_has_attrCharacterObject():
    assert hasattr(model6::UnsettableAttributes, "attrCharacterObject")
    descriptor = None
    for klass in model6::UnsettableAttributes.__mro__:
        if "attrCharacterObject" in klass.__dict__:
            descriptor = klass.__dict__["attrCharacterObject"]
            break
    assert isinstance(descriptor, property)

def test_model6::unsettableattributes_has_attrChar():
    assert hasattr(model6::UnsettableAttributes, "attrChar")
    descriptor = None
    for klass in model6::UnsettableAttributes.__mro__:
        if "attrChar" in klass.__dict__:
            descriptor = klass.__dict__["attrChar"]
            break
    assert isinstance(descriptor, property)

def test_model6::unsettableattributes_has_attrFloat():
    assert hasattr(model6::UnsettableAttributes, "attrFloat")
    descriptor = None
    for klass in model6::UnsettableAttributes.__mro__:
        if "attrFloat" in klass.__dict__:
            descriptor = klass.__dict__["attrFloat"]
            break
    assert isinstance(descriptor, property)

def test_model6::unsettableattributes_has_attrBoolean():
    assert hasattr(model6::UnsettableAttributes, "attrBoolean")
    descriptor = None
    for klass in model6::UnsettableAttributes.__mro__:
        if "attrBoolean" in klass.__dict__:
            descriptor = klass.__dict__["attrBoolean"]
            break
    assert isinstance(descriptor, property)

def test_model6::unsettableattributes_has_attrJavaClass():
    assert hasattr(model6::UnsettableAttributes, "attrJavaClass")
    descriptor = None
    for klass in model6::UnsettableAttributes.__mro__:
        if "attrJavaClass" in klass.__dict__:
            descriptor = klass.__dict__["attrJavaClass"]
            break
    assert isinstance(descriptor, property)

def test_model6::unsettableattributes_has_attrBigDecimal():
    assert hasattr(model6::UnsettableAttributes, "attrBigDecimal")
    descriptor = None
    for klass in model6::UnsettableAttributes.__mro__:
        if "attrBigDecimal" in klass.__dict__:
            descriptor = klass.__dict__["attrBigDecimal"]
            break
    assert isinstance(descriptor, property)

def test_model6::unsettableattributes_has_attrBigInteger():
    assert hasattr(model6::UnsettableAttributes, "attrBigInteger")
    descriptor = None
    for klass in model6::UnsettableAttributes.__mro__:
        if "attrBigInteger" in klass.__dict__:
            descriptor = klass.__dict__["attrBigInteger"]
            break
    assert isinstance(descriptor, property)

def test_model6::unsettableattributes_has_attrByte():
    assert hasattr(model6::UnsettableAttributes, "attrByte")
    descriptor = None
    for klass in model6::UnsettableAttributes.__mro__:
        if "attrByte" in klass.__dict__:
            descriptor = klass.__dict__["attrByte"]
            break
    assert isinstance(descriptor, property)

def test_model6::unsettableattributes_has_attrString():
    assert hasattr(model6::UnsettableAttributes, "attrString")
    descriptor = None
    for klass in model6::UnsettableAttributes.__mro__:
        if "attrString" in klass.__dict__:
            descriptor = klass.__dict__["attrString"]
            break
    assert isinstance(descriptor, property)

def test_model6::unsettableattributes_has_attrIntegerObject():
    assert hasattr(model6::UnsettableAttributes, "attrIntegerObject")
    descriptor = None
    for klass in model6::UnsettableAttributes.__mro__:
        if "attrIntegerObject" in klass.__dict__:
            descriptor = klass.__dict__["attrIntegerObject"]
            break
    assert isinstance(descriptor, property)

def test_model6::unsettableattributes_has_attrBooleanObject():
    assert hasattr(model6::UnsettableAttributes, "attrBooleanObject")
    descriptor = None
    for klass in model6::UnsettableAttributes.__mro__:
        if "attrBooleanObject" in klass.__dict__:
            descriptor = klass.__dict__["attrBooleanObject"]
            break
    assert isinstance(descriptor, property)

def test_model6::unsettableattributes_has_attrDoubleObject():
    assert hasattr(model6::UnsettableAttributes, "attrDoubleObject")
    descriptor = None
    for klass in model6::UnsettableAttributes.__mro__:
        if "attrDoubleObject" in klass.__dict__:
            descriptor = klass.__dict__["attrDoubleObject"]
            break
    assert isinstance(descriptor, property)

def test_model6::unsettableattributes_has_attrLong():
    assert hasattr(model6::UnsettableAttributes, "attrLong")
    descriptor = None
    for klass in model6::UnsettableAttributes.__mro__:
        if "attrLong" in klass.__dict__:
            descriptor = klass.__dict__["attrLong"]
            break
    assert isinstance(descriptor, property)

def test_model6::unsettableattributes_has_attrByteObject():
    assert hasattr(model6::UnsettableAttributes, "attrByteObject")
    descriptor = None
    for klass in model6::UnsettableAttributes.__mro__:
        if "attrByteObject" in klass.__dict__:
            descriptor = klass.__dict__["attrByteObject"]
            break
    assert isinstance(descriptor, property)

def test_model6::unsettableattributes_has_attrJavaObject():
    assert hasattr(model6::UnsettableAttributes, "attrJavaObject")
    descriptor = None
    for klass in model6::UnsettableAttributes.__mro__:
        if "attrJavaObject" in klass.__dict__:
            descriptor = klass.__dict__["attrJavaObject"]
            break
    assert isinstance(descriptor, property)

def test_model6::unsettableattributes_has_attrFloatObject():
    assert hasattr(model6::UnsettableAttributes, "attrFloatObject")
    descriptor = None
    for klass in model6::UnsettableAttributes.__mro__:
        if "attrFloatObject" in klass.__dict__:
            descriptor = klass.__dict__["attrFloatObject"]
            break
    assert isinstance(descriptor, property)

def test_model6::unsettableattributes_has_attrDate():
    assert hasattr(model6::UnsettableAttributes, "attrDate")
    descriptor = None
    for klass in model6::UnsettableAttributes.__mro__:
        if "attrDate" in klass.__dict__:
            descriptor = klass.__dict__["attrDate"]
            break
    assert isinstance(descriptor, property)

def test_model6::unsettableattributes_has_attrShortObject():
    assert hasattr(model6::UnsettableAttributes, "attrShortObject")
    descriptor = None
    for klass in model6::UnsettableAttributes.__mro__:
        if "attrShortObject" in klass.__dict__:
            descriptor = klass.__dict__["attrShortObject"]
            break
    assert isinstance(descriptor, property)

def test_model6::unsettableattributes_has_attrByteArray():
    assert hasattr(model6::UnsettableAttributes, "attrByteArray")
    descriptor = None
    for klass in model6::UnsettableAttributes.__mro__:
        if "attrByteArray" in klass.__dict__:
            descriptor = klass.__dict__["attrByteArray"]
            break
    assert isinstance(descriptor, property)

def test_model6::unsettableattributes_has_attrInt():
    assert hasattr(model6::UnsettableAttributes, "attrInt")
    descriptor = None
    for klass in model6::UnsettableAttributes.__mro__:
        if "attrInt" in klass.__dict__:
            descriptor = klass.__dict__["attrInt"]
            break
    assert isinstance(descriptor, property)

def test_model6::unsettableattributes_has_attrLongObject():
    assert hasattr(model6::UnsettableAttributes, "attrLongObject")
    descriptor = None
    for klass in model6::UnsettableAttributes.__mro__:
        if "attrLongObject" in klass.__dict__:
            descriptor = klass.__dict__["attrLongObject"]
            break
    assert isinstance(descriptor, property)

def test_model6::unsettableattributes_has_attrDouble():
    assert hasattr(model6::UnsettableAttributes, "attrDouble")
    descriptor = None
    for klass in model6::UnsettableAttributes.__mro__:
        if "attrDouble" in klass.__dict__:
            descriptor = klass.__dict__["attrDouble"]
            break
    assert isinstance(descriptor, property)



def test_model6::emptystringdefaultunsettable_is_not_abstract():
    assert not inspect.isabstract(model6::EmptyStringDefaultUnsettable)


def test_model6::emptystringdefaultunsettable_constructor_exists():
    assert callable(model6::EmptyStringDefaultUnsettable.__init__)


def test_model6::emptystringdefaultunsettable_constructor_args():
    sig = inspect.signature(model6::EmptyStringDefaultUnsettable.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_model6::emptystringdefaultunsettable_has_attribute():
    assert hasattr(model6::EmptyStringDefaultUnsettable, "attribute")
    descriptor = None
    for klass in model6::EmptyStringDefaultUnsettable.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_model6::emptystringdefault_is_not_abstract():
    assert not inspect.isabstract(model6::EmptyStringDefault)


def test_model6::emptystringdefault_constructor_exists():
    assert callable(model6::EmptyStringDefault.__init__)


def test_model6::emptystringdefault_constructor_args():
    sig = inspect.signature(model6::EmptyStringDefault.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_model6::emptystringdefault_has_attribute():
    assert hasattr(model6::EmptyStringDefault, "attribute")
    descriptor = None
    for klass in model6::EmptyStringDefault.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_model6::hasnillableattribute_is_not_abstract():
    assert not inspect.isabstract(model6::HasNillableAttribute)


def test_model6::hasnillableattribute_constructor_exists():
    assert callable(model6::HasNillableAttribute.__init__)


def test_model6::hasnillableattribute_constructor_args():
    sig = inspect.signature(model6::HasNillableAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "nillable" in params, "Missing parameter 'nillable'"

def test_model6::hasnillableattribute_has_nillable():
    assert hasattr(model6::HasNillableAttribute, "nillable")
    descriptor = None
    for klass in model6::HasNillableAttribute.__mro__:
        if "nillable" in klass.__dict__:
            descriptor = klass.__dict__["nillable"]
            break
    assert isinstance(descriptor, property)



def test_model6::canreferencelegacy_is_not_abstract():
    assert not inspect.isabstract(model6::CanReferenceLegacy)


def test_model6::canreferencelegacy_constructor_exists():
    assert callable(model6::CanReferenceLegacy.__init__)


def test_model6::canreferencelegacy_constructor_args():
    sig = inspect.signature(model6::CanReferenceLegacy.__init__)
    params = list(sig.parameters.keys())



def test_model6::g_is_not_abstract():
    assert not inspect.isabstract(model6::G)


def test_model6::g_constructor_exists():
    assert callable(model6::G.__init__)


def test_model6::g_constructor_args():
    sig = inspect.signature(model6::G.__init__)
    params = list(sig.parameters.keys())
    assert "dummy" in params, "Missing parameter 'dummy'"

def test_model6::g_has_dummy():
    assert hasattr(model6::G, "dummy")
    descriptor = None
    for klass in model6::G.__mro__:
        if "dummy" in klass.__dict__:
            descriptor = klass.__dict__["dummy"]
            break
    assert isinstance(descriptor, property)



def test_model6::f_is_not_abstract():
    assert not inspect.isabstract(model6::F)


def test_model6::f_constructor_exists():
    assert callable(model6::F.__init__)


def test_model6::f_constructor_args():
    sig = inspect.signature(model6::F.__init__)
    params = list(sig.parameters.keys())



def test_model6::e_is_not_abstract():
    assert not inspect.isabstract(model6::E)


def test_model6::e_constructor_exists():
    assert callable(model6::E.__init__)


def test_model6::e_constructor_args():
    sig = inspect.signature(model6::E.__init__)
    params = list(sig.parameters.keys())



def test_model6::eobject_is_not_abstract():
    assert not inspect.isabstract(model6::EObject)


def test_model6::eobject_constructor_exists():
    assert callable(model6::EObject.__init__)


def test_model6::eobject_constructor_args():
    sig = inspect.signature(model6::EObject.__init__)
    params = list(sig.parameters.keys())



def test_model6::c_is_not_abstract():
    assert not inspect.isabstract(model6::C)


def test_model6::c_constructor_exists():
    assert callable(model6::C.__init__)


def test_model6::c_constructor_args():
    sig = inspect.signature(model6::C.__init__)
    params = list(sig.parameters.keys())



def test_model6::b_is_not_abstract():
    assert not inspect.isabstract(model6::B)


def test_model6::b_constructor_exists():
    assert callable(model6::B.__init__)


def test_model6::b_constructor_args():
    sig = inspect.signature(model6::B.__init__)
    params = list(sig.parameters.keys())



def test_model6::d_is_not_abstract():
    assert not inspect.isabstract(model6::D)


def test_model6::d_constructor_exists():
    assert callable(model6::D.__init__)


def test_model6::d_constructor_args():
    sig = inspect.signature(model6::D.__init__)
    params = list(sig.parameters.keys())



def test_model6::a_is_not_abstract():
    assert not inspect.isabstract(model6::A)


def test_model6::a_constructor_exists():
    assert callable(model6::A.__init__)


def test_model6::a_constructor_args():
    sig = inspect.signature(model6::A.__init__)
    params = list(sig.parameters.keys())



def test_model6::propertiesmapentryvalue_is_not_abstract():
    assert not inspect.isabstract(model6::PropertiesMapEntryValue)


def test_model6::propertiesmapentryvalue_constructor_exists():
    assert callable(model6::PropertiesMapEntryValue.__init__)


def test_model6::propertiesmapentryvalue_constructor_args():
    sig = inspect.signature(model6::PropertiesMapEntryValue.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_model6::propertiesmapentryvalue_has_label():
    assert hasattr(model6::PropertiesMapEntryValue, "label")
    descriptor = None
    for klass in model6::PropertiesMapEntryValue.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_model6::holdable_is_not_abstract():
    assert not inspect.isabstract(model6::Holdable)


def test_model6::holdable_constructor_exists():
    assert callable(model6::Holdable.__init__)


def test_model6::holdable_constructor_args():
    sig = inspect.signature(model6::Holdable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model6::holdable_has_name():
    assert hasattr(model6::Holdable, "name")
    descriptor = None
    for klass in model6::Holdable.__mro__:
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



def test_model6::thing_is_not_abstract():
    assert not inspect.isabstract(model6::Thing)


def test_model6::thing_constructor_exists():
    assert callable(model6::Thing.__init__)


def test_model6::thing_constructor_args():
    sig = inspect.signature(model6::Thing.__init__)
    params = list(sig.parameters.keys())



def test_model6::holder_is_not_abstract():
    assert not inspect.isabstract(model6::Holder)


def test_model6::holder_constructor_exists():
    assert callable(model6::Holder.__init__)


def test_model6::holder_constructor_args():
    sig = inspect.signature(model6::Holder.__init__)
    params = list(sig.parameters.keys())



def test_model6::myenumlistunsettable_is_not_abstract():
    assert not inspect.isabstract(model6::MyEnumListUnsettable)


def test_model6::myenumlistunsettable_constructor_exists():
    assert callable(model6::MyEnumListUnsettable.__init__)


def test_model6::myenumlistunsettable_constructor_args():
    sig = inspect.signature(model6::MyEnumListUnsettable.__init__)
    params = list(sig.parameters.keys())
    assert "myEnum" in params, "Missing parameter 'myEnum'"

def test_model6::myenumlistunsettable_has_myEnum():
    assert hasattr(model6::MyEnumListUnsettable, "myEnum")
    descriptor = None
    for klass in model6::MyEnumListUnsettable.__mro__:
        if "myEnum" in klass.__dict__:
            descriptor = klass.__dict__["myEnum"]
            break
    assert isinstance(descriptor, property)



def test_model6::myenumlist_is_not_abstract():
    assert not inspect.isabstract(model6::MyEnumList)


def test_model6::myenumlist_constructor_exists():
    assert callable(model6::MyEnumList.__init__)


def test_model6::myenumlist_constructor_args():
    sig = inspect.signature(model6::MyEnumList.__init__)
    params = list(sig.parameters.keys())
    assert "myEnum" in params, "Missing parameter 'myEnum'"

def test_model6::myenumlist_has_myEnum():
    assert hasattr(model6::MyEnumList, "myEnum")
    descriptor = None
    for klass in model6::MyEnumList.__mro__:
        if "myEnum" in klass.__dict__:
            descriptor = klass.__dict__["myEnum"]
            break
    assert isinstance(descriptor, property)



def test_model6::baseobject_is_not_abstract():
    assert not inspect.isabstract(model6::BaseObject)


def test_model6::baseobject_constructor_exists():
    assert callable(model6::BaseObject.__init__)


def test_model6::baseobject_constructor_args():
    sig = inspect.signature(model6::BaseObject.__init__)
    params = list(sig.parameters.keys())
    assert "attributeOptional" in params, "Missing parameter 'attributeOptional'"
    assert "attributeList" in params, "Missing parameter 'attributeList'"
    assert "attributeRequired" in params, "Missing parameter 'attributeRequired'"

def test_model6::baseobject_has_attributeOptional():
    assert hasattr(model6::BaseObject, "attributeOptional")
    descriptor = None
    for klass in model6::BaseObject.__mro__:
        if "attributeOptional" in klass.__dict__:
            descriptor = klass.__dict__["attributeOptional"]
            break
    assert isinstance(descriptor, property)

def test_model6::baseobject_has_attributeList():
    assert hasattr(model6::BaseObject, "attributeList")
    descriptor = None
    for klass in model6::BaseObject.__mro__:
        if "attributeList" in klass.__dict__:
            descriptor = klass.__dict__["attributeList"]
            break
    assert isinstance(descriptor, property)

def test_model6::baseobject_has_attributeRequired():
    assert hasattr(model6::BaseObject, "attributeRequired")
    descriptor = None
    for klass in model6::BaseObject.__mro__:
        if "attributeRequired" in klass.__dict__:
            descriptor = klass.__dict__["attributeRequired"]
            break
    assert isinstance(descriptor, property)



def test_model6::root_is_not_abstract():
    assert not inspect.isabstract(model6::Root)


def test_model6::root_constructor_exists():
    assert callable(model6::Root.__init__)


def test_model6::root_constructor_args():
    sig = inspect.signature(model6::Root.__init__)
    params = list(sig.parameters.keys())



def test_model6::propertiesmapentry_is_not_abstract():
    assert not inspect.isabstract(model6::PropertiesMapEntry)


def test_model6::propertiesmapentry_constructor_exists():
    assert callable(model6::PropertiesMapEntry.__init__)


def test_model6::propertiesmapentry_constructor_args():
    sig = inspect.signature(model6::PropertiesMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_model6::propertiesmapentry_has_key():
    assert hasattr(model6::PropertiesMapEntry, "key")
    descriptor = None
    for klass in model6::PropertiesMapEntry.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_model6::propertiesmap_is_not_abstract():
    assert not inspect.isabstract(model6::PropertiesMap)


def test_model6::propertiesmap_constructor_exists():
    assert callable(model6::PropertiesMap.__init__)


def test_model6::propertiesmap_constructor_args():
    sig = inspect.signature(model6::PropertiesMap.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_model6::propertiesmap_has_label():
    assert hasattr(model6::PropertiesMap, "label")
    descriptor = None
    for klass in model6::PropertiesMap.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_model6::unorderedlist_is_not_abstract():
    assert not inspect.isabstract(model6::UnorderedList)


def test_model6::unorderedlist_constructor_exists():
    assert callable(model6::UnorderedList.__init__)


def test_model6::unorderedlist_constructor_args():
    sig = inspect.signature(model6::UnorderedList.__init__)
    params = list(sig.parameters.keys())



def test_baseobject_is_not_abstract():
    assert not inspect.isabstract(BaseObject)


def test_baseobject_constructor_exists():
    assert callable(BaseObject.__init__)


def test_baseobject_constructor_args():
    sig = inspect.signature(BaseObject.__init__)
    params = list(sig.parameters.keys())



def test_model6::containmentobject_is_not_abstract():
    assert not inspect.isabstract(model6::ContainmentObject)


def test_model6::containmentobject_constructor_exists():
    assert callable(model6::ContainmentObject.__init__)


def test_model6::containmentobject_constructor_args():
    sig = inspect.signature(model6::ContainmentObject.__init__)
    params = list(sig.parameters.keys())



def test_model6::referenceobject_is_not_abstract():
    assert not inspect.isabstract(model6::ReferenceObject)


def test_model6::referenceobject_constructor_exists():
    assert callable(model6::ReferenceObject.__init__)


def test_model6::referenceobject_constructor_args():
    sig = inspect.signature(model6::ReferenceObject.__init__)
    params = list(sig.parameters.keys())

def test_myenum_exists():
    # Check that the Enumeration exists
    assert MyEnum is not None

def test_myenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MyEnum]
    expected_literals = [
        "ONE",
        "THREE",
        "ZERO",
        "TWO",
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
model6::UnsettableAttributes_strategy = st.builds(
    model6::UnsettableAttributes,
    attrShort=
        safe_text,
    attrCharacterObject=
        safe_text,
    attrChar=
        safe_text,
    attrFloat=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    attrBoolean=
        st.booleans(),
    attrJavaClass=
        safe_text,
    attrBigDecimal=
        safe_text,
    attrBigInteger=
        safe_text,
    attrByte=
        safe_text,
    attrString=
        safe_text,
    attrIntegerObject=
        safe_text,
    attrBooleanObject=
        safe_text,
    attrDoubleObject=
        safe_text,
    attrLong=
        safe_text,
    attrByteObject=
        safe_text,
    attrJavaObject=
        safe_text,
    attrFloatObject=
        safe_text,
    attrDate=
        st.dates(),
    attrShortObject=
        safe_text,
    attrByteArray=
        safe_text,
    attrInt=
        st.integers(),
    attrLongObject=
        safe_text,
    attrDouble=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
model6::EmptyStringDefaultUnsettable_strategy = st.builds(
    model6::EmptyStringDefaultUnsettable,
    attribute=
        safe_text
)
model6::EmptyStringDefault_strategy = st.builds(
    model6::EmptyStringDefault,
    attribute=
        safe_text
)
model6::HasNillableAttribute_strategy = st.builds(
    model6::HasNillableAttribute,
    nillable=
        safe_text
)
model6::CanReferenceLegacy_strategy = st.builds(
    model6::CanReferenceLegacy,
)
model6::G_strategy = st.builds(
    model6::G,
    dummy=
        safe_text
)
model6::F_strategy = st.builds(
    model6::F,
)
model6::E_strategy = st.builds(
    model6::E,
)
model6::EObject_strategy = st.builds(
    model6::EObject,
)
model6::C_strategy = st.builds(
    model6::C,
)
model6::B_strategy = st.builds(
    model6::B,
)
model6::D_strategy = st.builds(
    model6::D,
)
model6::A_strategy = st.builds(
    model6::A,
)
model6::PropertiesMapEntryValue_strategy = st.builds(
    model6::PropertiesMapEntryValue,
    label=
        safe_text
)
model6::Holdable_strategy = st.builds(
    model6::Holdable,
    name=
        safe_text
)
Holdable_strategy = st.builds(
    Holdable,
)
model6::Thing_strategy = st.builds(
    model6::Thing,
)
model6::Holder_strategy = st.builds(
    model6::Holder,
)
model6::MyEnumListUnsettable_strategy = st.builds(
    model6::MyEnumListUnsettable,
    myEnum=
        safe_text
)
model6::MyEnumList_strategy = st.builds(
    model6::MyEnumList,
    myEnum=
        safe_text
)
model6::BaseObject_strategy = st.builds(
    model6::BaseObject,
    attributeOptional=
        safe_text,
    attributeList=
        safe_text,
    attributeRequired=
        safe_text
)
model6::Root_strategy = st.builds(
    model6::Root,
)
model6::PropertiesMapEntry_strategy = st.builds(
    model6::PropertiesMapEntry,
    key=
        safe_text
)
model6::PropertiesMap_strategy = st.builds(
    model6::PropertiesMap,
    label=
        safe_text
)
model6::UnorderedList_strategy = st.builds(
    model6::UnorderedList,
)
BaseObject_strategy = st.builds(
    BaseObject,
)
model6::ContainmentObject_strategy = st.builds(
    model6::ContainmentObject,
)
model6::ReferenceObject_strategy = st.builds(
    model6::ReferenceObject,
)

@given(instance=model6::UnsettableAttributes_strategy)
@settings(max_examples=50)
def test_model6::unsettableattributes_instantiation(instance):
    assert isinstance(instance, model6::UnsettableAttributes)

@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrShort_type(instance):
    assert isinstance(instance.attrShort, str)


@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrShort_setter(instance):
    original = instance.attrShort
    instance.attrShort = original
    assert instance.attrShort == original

@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrCharacterObject_type(instance):
    assert isinstance(instance.attrCharacterObject, str)


@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrCharacterObject_setter(instance):
    original = instance.attrCharacterObject
    instance.attrCharacterObject = original
    assert instance.attrCharacterObject == original

@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrChar_type(instance):
    assert isinstance(instance.attrChar, str)


@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrChar_setter(instance):
    original = instance.attrChar
    instance.attrChar = original
    assert instance.attrChar == original

@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrFloat_type(instance):
    assert isinstance(instance.attrFloat, float)


@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrFloat_setter(instance):
    original = instance.attrFloat
    instance.attrFloat = original
    assert instance.attrFloat == original

@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrBoolean_type(instance):
    assert isinstance(instance.attrBoolean, bool)


@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrBoolean_setter(instance):
    original = instance.attrBoolean
    instance.attrBoolean = original
    assert instance.attrBoolean == original

@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrJavaClass_type(instance):
    assert isinstance(instance.attrJavaClass, str)


@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrJavaClass_setter(instance):
    original = instance.attrJavaClass
    instance.attrJavaClass = original
    assert instance.attrJavaClass == original

@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrBigDecimal_type(instance):
    assert isinstance(instance.attrBigDecimal, str)


@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrBigDecimal_setter(instance):
    original = instance.attrBigDecimal
    instance.attrBigDecimal = original
    assert instance.attrBigDecimal == original

@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrBigInteger_type(instance):
    assert isinstance(instance.attrBigInteger, str)


@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrBigInteger_setter(instance):
    original = instance.attrBigInteger
    instance.attrBigInteger = original
    assert instance.attrBigInteger == original

@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrByte_type(instance):
    assert isinstance(instance.attrByte, str)


@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrByte_setter(instance):
    original = instance.attrByte
    instance.attrByte = original
    assert instance.attrByte == original

@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrString_type(instance):
    assert isinstance(instance.attrString, str)


@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrString_setter(instance):
    original = instance.attrString
    instance.attrString = original
    assert instance.attrString == original

@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrIntegerObject_type(instance):
    assert isinstance(instance.attrIntegerObject, str)


@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrIntegerObject_setter(instance):
    original = instance.attrIntegerObject
    instance.attrIntegerObject = original
    assert instance.attrIntegerObject == original

@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrBooleanObject_type(instance):
    assert isinstance(instance.attrBooleanObject, str)


@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrBooleanObject_setter(instance):
    original = instance.attrBooleanObject
    instance.attrBooleanObject = original
    assert instance.attrBooleanObject == original

@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrDoubleObject_type(instance):
    assert isinstance(instance.attrDoubleObject, str)


@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrDoubleObject_setter(instance):
    original = instance.attrDoubleObject
    instance.attrDoubleObject = original
    assert instance.attrDoubleObject == original

@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrLong_type(instance):
    assert isinstance(instance.attrLong, str)


@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrLong_setter(instance):
    original = instance.attrLong
    instance.attrLong = original
    assert instance.attrLong == original

@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrByteObject_type(instance):
    assert isinstance(instance.attrByteObject, str)


@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrByteObject_setter(instance):
    original = instance.attrByteObject
    instance.attrByteObject = original
    assert instance.attrByteObject == original

@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrJavaObject_type(instance):
    assert isinstance(instance.attrJavaObject, str)


@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrJavaObject_setter(instance):
    original = instance.attrJavaObject
    instance.attrJavaObject = original
    assert instance.attrJavaObject == original

@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrFloatObject_type(instance):
    assert isinstance(instance.attrFloatObject, str)


@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrFloatObject_setter(instance):
    original = instance.attrFloatObject
    instance.attrFloatObject = original
    assert instance.attrFloatObject == original

@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrDate_type(instance):
    assert isinstance(instance.attrDate, date)


@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrDate_setter(instance):
    original = instance.attrDate
    instance.attrDate = original
    assert instance.attrDate == original

@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrShortObject_type(instance):
    assert isinstance(instance.attrShortObject, str)


@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrShortObject_setter(instance):
    original = instance.attrShortObject
    instance.attrShortObject = original
    assert instance.attrShortObject == original

@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrByteArray_type(instance):
    assert isinstance(instance.attrByteArray, str)


@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrByteArray_setter(instance):
    original = instance.attrByteArray
    instance.attrByteArray = original
    assert instance.attrByteArray == original

@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrInt_type(instance):
    assert isinstance(instance.attrInt, int)


@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrInt_setter(instance):
    original = instance.attrInt
    instance.attrInt = original
    assert instance.attrInt == original

@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrLongObject_type(instance):
    assert isinstance(instance.attrLongObject, str)


@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrLongObject_setter(instance):
    original = instance.attrLongObject
    instance.attrLongObject = original
    assert instance.attrLongObject == original

@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrDouble_type(instance):
    assert isinstance(instance.attrDouble, float)


@given(instance=model6::UnsettableAttributes_strategy)
def test_model6::unsettableattributes_attrDouble_setter(instance):
    original = instance.attrDouble
    instance.attrDouble = original
    assert instance.attrDouble == original

@given(instance=model6::EmptyStringDefaultUnsettable_strategy)
@settings(max_examples=50)
def test_model6::emptystringdefaultunsettable_instantiation(instance):
    assert isinstance(instance, model6::EmptyStringDefaultUnsettable)

@given(instance=model6::EmptyStringDefaultUnsettable_strategy)
def test_model6::emptystringdefaultunsettable_attribute_type(instance):
    assert isinstance(instance.attribute, str)


@given(instance=model6::EmptyStringDefaultUnsettable_strategy)
def test_model6::emptystringdefaultunsettable_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=model6::EmptyStringDefault_strategy)
@settings(max_examples=50)
def test_model6::emptystringdefault_instantiation(instance):
    assert isinstance(instance, model6::EmptyStringDefault)

@given(instance=model6::EmptyStringDefault_strategy)
def test_model6::emptystringdefault_attribute_type(instance):
    assert isinstance(instance.attribute, str)


@given(instance=model6::EmptyStringDefault_strategy)
def test_model6::emptystringdefault_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=model6::HasNillableAttribute_strategy)
@settings(max_examples=50)
def test_model6::hasnillableattribute_instantiation(instance):
    assert isinstance(instance, model6::HasNillableAttribute)

@given(instance=model6::HasNillableAttribute_strategy)
def test_model6::hasnillableattribute_nillable_type(instance):
    assert isinstance(instance.nillable, str)


@given(instance=model6::HasNillableAttribute_strategy)
def test_model6::hasnillableattribute_nillable_setter(instance):
    original = instance.nillable
    instance.nillable = original
    assert instance.nillable == original

@given(instance=model6::CanReferenceLegacy_strategy)
@settings(max_examples=50)
def test_model6::canreferencelegacy_instantiation(instance):
    assert isinstance(instance, model6::CanReferenceLegacy)

@given(instance=model6::G_strategy)
@settings(max_examples=50)
def test_model6::g_instantiation(instance):
    assert isinstance(instance, model6::G)

@given(instance=model6::G_strategy)
def test_model6::g_dummy_type(instance):
    assert isinstance(instance.dummy, str)


@given(instance=model6::G_strategy)
def test_model6::g_dummy_setter(instance):
    original = instance.dummy
    instance.dummy = original
    assert instance.dummy == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model6::G_strategy)
@settings(max_examples=30)
def test_model6::g_isattributemodified_changes_state(instance):
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
        assert has_statements, f"Function 'isAttributeModified' in model6::G is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isAttributeModified' in model6::G did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isAttributeModified' in model6::G is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model6::G_strategy)
@settings(max_examples=30)
def test_model6::g_islistmodified_changes_state(instance):
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
        assert has_statements, f"Function 'isListModified' in model6::G is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isListModified' in model6::G did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isListModified' in model6::G is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model6::G_strategy)
@settings(max_examples=30)
def test_model6::g_isreferencemodified_changes_state(instance):
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
        assert has_statements, f"Function 'isReferenceModified' in model6::G is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isReferenceModified' in model6::G did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isReferenceModified' in model6::G is not implemented or raised an error")

@given(instance=model6::F_strategy)
@settings(max_examples=50)
def test_model6::f_instantiation(instance):
    assert isinstance(instance, model6::F)

@given(instance=model6::E_strategy)
@settings(max_examples=50)
def test_model6::e_instantiation(instance):
    assert isinstance(instance, model6::E)

@given(instance=model6::EObject_strategy)
@settings(max_examples=50)
def test_model6::eobject_instantiation(instance):
    assert isinstance(instance, model6::EObject)

@given(instance=model6::C_strategy)
@settings(max_examples=50)
def test_model6::c_instantiation(instance):
    assert isinstance(instance, model6::C)

@given(instance=model6::B_strategy)
@settings(max_examples=50)
def test_model6::b_instantiation(instance):
    assert isinstance(instance, model6::B)

@given(instance=model6::D_strategy)
@settings(max_examples=50)
def test_model6::d_instantiation(instance):
    assert isinstance(instance, model6::D)

@given(instance=model6::A_strategy)
@settings(max_examples=50)
def test_model6::a_instantiation(instance):
    assert isinstance(instance, model6::A)

@given(instance=model6::PropertiesMapEntryValue_strategy)
@settings(max_examples=50)
def test_model6::propertiesmapentryvalue_instantiation(instance):
    assert isinstance(instance, model6::PropertiesMapEntryValue)

@given(instance=model6::PropertiesMapEntryValue_strategy)
def test_model6::propertiesmapentryvalue_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=model6::PropertiesMapEntryValue_strategy)
def test_model6::propertiesmapentryvalue_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=model6::Holdable_strategy)
@settings(max_examples=50)
def test_model6::holdable_instantiation(instance):
    assert isinstance(instance, model6::Holdable)

@given(instance=model6::Holdable_strategy)
def test_model6::holdable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model6::Holdable_strategy)
def test_model6::holdable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Holdable_strategy)
@settings(max_examples=50)
def test_holdable_instantiation(instance):
    assert isinstance(instance, Holdable)

@given(instance=model6::Thing_strategy)
@settings(max_examples=50)
def test_model6::thing_instantiation(instance):
    assert isinstance(instance, model6::Thing)

@given(instance=model6::Holder_strategy)
@settings(max_examples=50)
def test_model6::holder_instantiation(instance):
    assert isinstance(instance, model6::Holder)

@given(instance=model6::MyEnumListUnsettable_strategy)
@settings(max_examples=50)
def test_model6::myenumlistunsettable_instantiation(instance):
    assert isinstance(instance, model6::MyEnumListUnsettable)

@given(instance=model6::MyEnumListUnsettable_strategy)
def test_model6::myenumlistunsettable_myEnum_type(instance):
    assert isinstance(instance.myEnum, str)


@given(instance=model6::MyEnumListUnsettable_strategy)
def test_model6::myenumlistunsettable_myEnum_setter(instance):
    original = instance.myEnum
    instance.myEnum = original
    assert instance.myEnum == original

@given(instance=model6::MyEnumList_strategy)
@settings(max_examples=50)
def test_model6::myenumlist_instantiation(instance):
    assert isinstance(instance, model6::MyEnumList)

@given(instance=model6::MyEnumList_strategy)
def test_model6::myenumlist_myEnum_type(instance):
    assert isinstance(instance.myEnum, str)


@given(instance=model6::MyEnumList_strategy)
def test_model6::myenumlist_myEnum_setter(instance):
    original = instance.myEnum
    instance.myEnum = original
    assert instance.myEnum == original

@given(instance=model6::BaseObject_strategy)
@settings(max_examples=50)
def test_model6::baseobject_instantiation(instance):
    assert isinstance(instance, model6::BaseObject)

@given(instance=model6::BaseObject_strategy)
def test_model6::baseobject_attributeOptional_type(instance):
    assert isinstance(instance.attributeOptional, str)


@given(instance=model6::BaseObject_strategy)
def test_model6::baseobject_attributeOptional_setter(instance):
    original = instance.attributeOptional
    instance.attributeOptional = original
    assert instance.attributeOptional == original

@given(instance=model6::BaseObject_strategy)
def test_model6::baseobject_attributeList_type(instance):
    assert isinstance(instance.attributeList, str)


@given(instance=model6::BaseObject_strategy)
def test_model6::baseobject_attributeList_setter(instance):
    original = instance.attributeList
    instance.attributeList = original
    assert instance.attributeList == original

@given(instance=model6::BaseObject_strategy)
def test_model6::baseobject_attributeRequired_type(instance):
    assert isinstance(instance.attributeRequired, str)


@given(instance=model6::BaseObject_strategy)
def test_model6::baseobject_attributeRequired_setter(instance):
    original = instance.attributeRequired
    instance.attributeRequired = original
    assert instance.attributeRequired == original

@given(instance=model6::Root_strategy)
@settings(max_examples=50)
def test_model6::root_instantiation(instance):
    assert isinstance(instance, model6::Root)

@given(instance=model6::PropertiesMapEntry_strategy)
@settings(max_examples=50)
def test_model6::propertiesmapentry_instantiation(instance):
    assert isinstance(instance, model6::PropertiesMapEntry)

@given(instance=model6::PropertiesMapEntry_strategy)
def test_model6::propertiesmapentry_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=model6::PropertiesMapEntry_strategy)
def test_model6::propertiesmapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=model6::PropertiesMap_strategy)
@settings(max_examples=50)
def test_model6::propertiesmap_instantiation(instance):
    assert isinstance(instance, model6::PropertiesMap)

@given(instance=model6::PropertiesMap_strategy)
def test_model6::propertiesmap_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=model6::PropertiesMap_strategy)
def test_model6::propertiesmap_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=model6::UnorderedList_strategy)
@settings(max_examples=50)
def test_model6::unorderedlist_instantiation(instance):
    assert isinstance(instance, model6::UnorderedList)

@given(instance=BaseObject_strategy)
@settings(max_examples=50)
def test_baseobject_instantiation(instance):
    assert isinstance(instance, BaseObject)

@given(instance=model6::ContainmentObject_strategy)
@settings(max_examples=50)
def test_model6::containmentobject_instantiation(instance):
    assert isinstance(instance, model6::ContainmentObject)

@given(instance=model6::ReferenceObject_strategy)
@settings(max_examples=50)
def test_model6::referenceobject_instantiation(instance):
    assert isinstance(instance, model6::ReferenceObject)
