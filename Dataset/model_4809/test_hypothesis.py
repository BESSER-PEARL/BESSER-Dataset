import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    model::EStringToStringMapEntry,
    model::ObjectWithMap,
    model::AbstractType,
    model::Container,
    model::Node,
    AbstractType,
    model::ConcreteTypeTwo,
    model::ConcreteTypeOne,
    model::TargetObject,
    model::PrimaryObject,
    model::Address,
    model::User,
    model::ETypes,
    Sex,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(model::EStringToStringMapEntry)


def test_model::estringtostringmapentry_constructor_exists():
    assert callable(model::EStringToStringMapEntry.__init__)


def test_model::estringtostringmapentry_constructor_args():
    sig = inspect.signature(model::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_model::objectwithmap_is_not_abstract():
    assert not inspect.isabstract(model::ObjectWithMap)


def test_model::objectwithmap_constructor_exists():
    assert callable(model::ObjectWithMap.__init__)


def test_model::objectwithmap_constructor_args():
    sig = inspect.signature(model::ObjectWithMap.__init__)
    params = list(sig.parameters.keys())



def test_model::abstracttype_is_not_abstract():
    assert not inspect.isabstract(model::AbstractType)


def test_model::abstracttype_constructor_exists():
    assert callable(model::AbstractType.__init__)


def test_model::abstracttype_constructor_args():
    sig = inspect.signature(model::AbstractType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model::abstracttype_has_name():
    assert hasattr(model::AbstractType, "name")
    descriptor = None
    for klass in model::AbstractType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model::container_is_not_abstract():
    assert not inspect.isabstract(model::Container)


def test_model::container_constructor_exists():
    assert callable(model::Container.__init__)


def test_model::container_constructor_args():
    sig = inspect.signature(model::Container.__init__)
    params = list(sig.parameters.keys())



def test_model::node_is_not_abstract():
    assert not inspect.isabstract(model::Node)


def test_model::node_constructor_exists():
    assert callable(model::Node.__init__)


def test_model::node_constructor_args():
    sig = inspect.signature(model::Node.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_model::node_has_label():
    assert hasattr(model::Node, "label")
    descriptor = None
    for klass in model::Node.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_abstracttype_is_not_abstract():
    assert not inspect.isabstract(AbstractType)


def test_abstracttype_constructor_exists():
    assert callable(AbstractType.__init__)


def test_abstracttype_constructor_args():
    sig = inspect.signature(AbstractType.__init__)
    params = list(sig.parameters.keys())



def test_model::concretetypetwo_is_not_abstract():
    assert not inspect.isabstract(model::ConcreteTypeTwo)


def test_model::concretetypetwo_constructor_exists():
    assert callable(model::ConcreteTypeTwo.__init__)


def test_model::concretetypetwo_constructor_args():
    sig = inspect.signature(model::ConcreteTypeTwo.__init__)
    params = list(sig.parameters.keys())
    assert "propTypeTwo" in params, "Missing parameter 'propTypeTwo'"

def test_model::concretetypetwo_has_propTypeTwo():
    assert hasattr(model::ConcreteTypeTwo, "propTypeTwo")
    descriptor = None
    for klass in model::ConcreteTypeTwo.__mro__:
        if "propTypeTwo" in klass.__dict__:
            descriptor = klass.__dict__["propTypeTwo"]
            break
    assert isinstance(descriptor, property)



def test_model::concretetypeone_is_not_abstract():
    assert not inspect.isabstract(model::ConcreteTypeOne)


def test_model::concretetypeone_constructor_exists():
    assert callable(model::ConcreteTypeOne.__init__)


def test_model::concretetypeone_constructor_args():
    sig = inspect.signature(model::ConcreteTypeOne.__init__)
    params = list(sig.parameters.keys())
    assert "propTypeOne" in params, "Missing parameter 'propTypeOne'"

def test_model::concretetypeone_has_propTypeOne():
    assert hasattr(model::ConcreteTypeOne, "propTypeOne")
    descriptor = None
    for klass in model::ConcreteTypeOne.__mro__:
        if "propTypeOne" in klass.__dict__:
            descriptor = klass.__dict__["propTypeOne"]
            break
    assert isinstance(descriptor, property)



def test_model::targetobject_is_not_abstract():
    assert not inspect.isabstract(model::TargetObject)


def test_model::targetobject_constructor_exists():
    assert callable(model::TargetObject.__init__)


def test_model::targetobject_constructor_args():
    sig = inspect.signature(model::TargetObject.__init__)
    params = list(sig.parameters.keys())
    assert "arrayAttribute" in params, "Missing parameter 'arrayAttribute'"
    assert "singleAttribute" in params, "Missing parameter 'singleAttribute'"

def test_model::targetobject_has_arrayAttribute():
    assert hasattr(model::TargetObject, "arrayAttribute")
    descriptor = None
    for klass in model::TargetObject.__mro__:
        if "arrayAttribute" in klass.__dict__:
            descriptor = klass.__dict__["arrayAttribute"]
            break
    assert isinstance(descriptor, property)

def test_model::targetobject_has_singleAttribute():
    assert hasattr(model::TargetObject, "singleAttribute")
    descriptor = None
    for klass in model::TargetObject.__mro__:
        if "singleAttribute" in klass.__dict__:
            descriptor = klass.__dict__["singleAttribute"]
            break
    assert isinstance(descriptor, property)



def test_model::primaryobject_is_not_abstract():
    assert not inspect.isabstract(model::PrimaryObject)


def test_model::primaryobject_constructor_exists():
    assert callable(model::PrimaryObject.__init__)


def test_model::primaryobject_constructor_args():
    sig = inspect.signature(model::PrimaryObject.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "unsettableAttribute" in params, "Missing parameter 'unsettableAttribute'"
    assert "featureMapReferenceCollection" in params, "Missing parameter 'featureMapReferenceCollection'"
    assert "unsettableAttributeWithNonNullDefault" in params, "Missing parameter 'unsettableAttributeWithNonNullDefault'"
    assert "featureMapAttributeCollection" in params, "Missing parameter 'featureMapAttributeCollection'"
    assert "featureMapAttributeType1" in params, "Missing parameter 'featureMapAttributeType1'"
    assert "idAttribute" in params, "Missing parameter 'idAttribute'"
    assert "featureMapAttributeType2" in params, "Missing parameter 'featureMapAttributeType2'"

def test_model::primaryobject_has_name():
    assert hasattr(model::PrimaryObject, "name")
    descriptor = None
    for klass in model::PrimaryObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model::primaryobject_has_unsettableAttribute():
    assert hasattr(model::PrimaryObject, "unsettableAttribute")
    descriptor = None
    for klass in model::PrimaryObject.__mro__:
        if "unsettableAttribute" in klass.__dict__:
            descriptor = klass.__dict__["unsettableAttribute"]
            break
    assert isinstance(descriptor, property)

def test_model::primaryobject_has_featureMapReferenceCollection():
    assert hasattr(model::PrimaryObject, "featureMapReferenceCollection")
    descriptor = None
    for klass in model::PrimaryObject.__mro__:
        if "featureMapReferenceCollection" in klass.__dict__:
            descriptor = klass.__dict__["featureMapReferenceCollection"]
            break
    assert isinstance(descriptor, property)

def test_model::primaryobject_has_unsettableAttributeWithNonNullDefault():
    assert hasattr(model::PrimaryObject, "unsettableAttributeWithNonNullDefault")
    descriptor = None
    for klass in model::PrimaryObject.__mro__:
        if "unsettableAttributeWithNonNullDefault" in klass.__dict__:
            descriptor = klass.__dict__["unsettableAttributeWithNonNullDefault"]
            break
    assert isinstance(descriptor, property)

def test_model::primaryobject_has_featureMapAttributeCollection():
    assert hasattr(model::PrimaryObject, "featureMapAttributeCollection")
    descriptor = None
    for klass in model::PrimaryObject.__mro__:
        if "featureMapAttributeCollection" in klass.__dict__:
            descriptor = klass.__dict__["featureMapAttributeCollection"]
            break
    assert isinstance(descriptor, property)

def test_model::primaryobject_has_featureMapAttributeType1():
    assert hasattr(model::PrimaryObject, "featureMapAttributeType1")
    descriptor = None
    for klass in model::PrimaryObject.__mro__:
        if "featureMapAttributeType1" in klass.__dict__:
            descriptor = klass.__dict__["featureMapAttributeType1"]
            break
    assert isinstance(descriptor, property)

def test_model::primaryobject_has_idAttribute():
    assert hasattr(model::PrimaryObject, "idAttribute")
    descriptor = None
    for klass in model::PrimaryObject.__mro__:
        if "idAttribute" in klass.__dict__:
            descriptor = klass.__dict__["idAttribute"]
            break
    assert isinstance(descriptor, property)

def test_model::primaryobject_has_featureMapAttributeType2():
    assert hasattr(model::PrimaryObject, "featureMapAttributeType2")
    descriptor = None
    for klass in model::PrimaryObject.__mro__:
        if "featureMapAttributeType2" in klass.__dict__:
            descriptor = klass.__dict__["featureMapAttributeType2"]
            break
    assert isinstance(descriptor, property)



def test_model::address_is_not_abstract():
    assert not inspect.isabstract(model::Address)


def test_model::address_constructor_exists():
    assert callable(model::Address.__init__)


def test_model::address_constructor_args():
    sig = inspect.signature(model::Address.__init__)
    params = list(sig.parameters.keys())
    assert "street" in params, "Missing parameter 'street'"
    assert "addId" in params, "Missing parameter 'addId'"
    assert "city" in params, "Missing parameter 'city'"
    assert "number" in params, "Missing parameter 'number'"

def test_model::address_has_street():
    assert hasattr(model::Address, "street")
    descriptor = None
    for klass in model::Address.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_model::address_has_addId():
    assert hasattr(model::Address, "addId")
    descriptor = None
    for klass in model::Address.__mro__:
        if "addId" in klass.__dict__:
            descriptor = klass.__dict__["addId"]
            break
    assert isinstance(descriptor, property)

def test_model::address_has_city():
    assert hasattr(model::Address, "city")
    descriptor = None
    for klass in model::Address.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_model::address_has_number():
    assert hasattr(model::Address, "number")
    descriptor = None
    for klass in model::Address.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_model::user_is_not_abstract():
    assert not inspect.isabstract(model::User)


def test_model::user_constructor_exists():
    assert callable(model::User.__init__)


def test_model::user_constructor_args():
    sig = inspect.signature(model::User.__init__)
    params = list(sig.parameters.keys())
    assert "birthDate" in params, "Missing parameter 'birthDate'"
    assert "sex" in params, "Missing parameter 'sex'"
    assert "userId" in params, "Missing parameter 'userId'"
    assert "name" in params, "Missing parameter 'name'"

def test_model::user_has_birthDate():
    assert hasattr(model::User, "birthDate")
    descriptor = None
    for klass in model::User.__mro__:
        if "birthDate" in klass.__dict__:
            descriptor = klass.__dict__["birthDate"]
            break
    assert isinstance(descriptor, property)

def test_model::user_has_sex():
    assert hasattr(model::User, "sex")
    descriptor = None
    for klass in model::User.__mro__:
        if "sex" in klass.__dict__:
            descriptor = klass.__dict__["sex"]
            break
    assert isinstance(descriptor, property)

def test_model::user_has_userId():
    assert hasattr(model::User, "userId")
    descriptor = None
    for klass in model::User.__mro__:
        if "userId" in klass.__dict__:
            descriptor = klass.__dict__["userId"]
            break
    assert isinstance(descriptor, property)

def test_model::user_has_name():
    assert hasattr(model::User, "name")
    descriptor = None
    for klass in model::User.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model::etypes_is_not_abstract():
    assert not inspect.isabstract(model::ETypes)


def test_model::etypes_constructor_exists():
    assert callable(model::ETypes.__init__)


def test_model::etypes_constructor_args():
    sig = inspect.signature(model::ETypes.__init__)
    params = list(sig.parameters.keys())
    assert "eString" in params, "Missing parameter 'eString'"
    assert "eByte" in params, "Missing parameter 'eByte'"
    assert "eLong" in params, "Missing parameter 'eLong'"
    assert "uris" in params, "Missing parameter 'uris'"
    assert "eBigDecimal" in params, "Missing parameter 'eBigDecimal'"
    assert "eBigInteger" in params, "Missing parameter 'eBigInteger'"
    assert "eDoubles" in params, "Missing parameter 'eDoubles'"
    assert "eInts" in params, "Missing parameter 'eInts'"
    assert "eDate" in params, "Missing parameter 'eDate'"
    assert "eInt" in params, "Missing parameter 'eInt'"
    assert "eFloat" in params, "Missing parameter 'eFloat'"
    assert "eBooleans" in params, "Missing parameter 'eBooleans'"
    assert "eBoolean" in params, "Missing parameter 'eBoolean'"
    assert "doubleValue" in params, "Missing parameter 'doubleValue'"
    assert "eByteArray" in params, "Missing parameter 'eByteArray'"
    assert "eStrings" in params, "Missing parameter 'eStrings'"
    assert "eShort" in params, "Missing parameter 'eShort'"
    assert "eChar" in params, "Missing parameter 'eChar'"
    assert "eDouble" in params, "Missing parameter 'eDouble'"

def test_model::etypes_has_eString():
    assert hasattr(model::ETypes, "eString")
    descriptor = None
    for klass in model::ETypes.__mro__:
        if "eString" in klass.__dict__:
            descriptor = klass.__dict__["eString"]
            break
    assert isinstance(descriptor, property)

def test_model::etypes_has_eByte():
    assert hasattr(model::ETypes, "eByte")
    descriptor = None
    for klass in model::ETypes.__mro__:
        if "eByte" in klass.__dict__:
            descriptor = klass.__dict__["eByte"]
            break
    assert isinstance(descriptor, property)

def test_model::etypes_has_eLong():
    assert hasattr(model::ETypes, "eLong")
    descriptor = None
    for klass in model::ETypes.__mro__:
        if "eLong" in klass.__dict__:
            descriptor = klass.__dict__["eLong"]
            break
    assert isinstance(descriptor, property)

def test_model::etypes_has_uris():
    assert hasattr(model::ETypes, "uris")
    descriptor = None
    for klass in model::ETypes.__mro__:
        if "uris" in klass.__dict__:
            descriptor = klass.__dict__["uris"]
            break
    assert isinstance(descriptor, property)

def test_model::etypes_has_eBigDecimal():
    assert hasattr(model::ETypes, "eBigDecimal")
    descriptor = None
    for klass in model::ETypes.__mro__:
        if "eBigDecimal" in klass.__dict__:
            descriptor = klass.__dict__["eBigDecimal"]
            break
    assert isinstance(descriptor, property)

def test_model::etypes_has_eBigInteger():
    assert hasattr(model::ETypes, "eBigInteger")
    descriptor = None
    for klass in model::ETypes.__mro__:
        if "eBigInteger" in klass.__dict__:
            descriptor = klass.__dict__["eBigInteger"]
            break
    assert isinstance(descriptor, property)

def test_model::etypes_has_eDoubles():
    assert hasattr(model::ETypes, "eDoubles")
    descriptor = None
    for klass in model::ETypes.__mro__:
        if "eDoubles" in klass.__dict__:
            descriptor = klass.__dict__["eDoubles"]
            break
    assert isinstance(descriptor, property)

def test_model::etypes_has_eInts():
    assert hasattr(model::ETypes, "eInts")
    descriptor = None
    for klass in model::ETypes.__mro__:
        if "eInts" in klass.__dict__:
            descriptor = klass.__dict__["eInts"]
            break
    assert isinstance(descriptor, property)

def test_model::etypes_has_eDate():
    assert hasattr(model::ETypes, "eDate")
    descriptor = None
    for klass in model::ETypes.__mro__:
        if "eDate" in klass.__dict__:
            descriptor = klass.__dict__["eDate"]
            break
    assert isinstance(descriptor, property)

def test_model::etypes_has_eInt():
    assert hasattr(model::ETypes, "eInt")
    descriptor = None
    for klass in model::ETypes.__mro__:
        if "eInt" in klass.__dict__:
            descriptor = klass.__dict__["eInt"]
            break
    assert isinstance(descriptor, property)

def test_model::etypes_has_eFloat():
    assert hasattr(model::ETypes, "eFloat")
    descriptor = None
    for klass in model::ETypes.__mro__:
        if "eFloat" in klass.__dict__:
            descriptor = klass.__dict__["eFloat"]
            break
    assert isinstance(descriptor, property)

def test_model::etypes_has_eBooleans():
    assert hasattr(model::ETypes, "eBooleans")
    descriptor = None
    for klass in model::ETypes.__mro__:
        if "eBooleans" in klass.__dict__:
            descriptor = klass.__dict__["eBooleans"]
            break
    assert isinstance(descriptor, property)

def test_model::etypes_has_eBoolean():
    assert hasattr(model::ETypes, "eBoolean")
    descriptor = None
    for klass in model::ETypes.__mro__:
        if "eBoolean" in klass.__dict__:
            descriptor = klass.__dict__["eBoolean"]
            break
    assert isinstance(descriptor, property)

def test_model::etypes_has_doubleValue():
    assert hasattr(model::ETypes, "doubleValue")
    descriptor = None
    for klass in model::ETypes.__mro__:
        if "doubleValue" in klass.__dict__:
            descriptor = klass.__dict__["doubleValue"]
            break
    assert isinstance(descriptor, property)

def test_model::etypes_has_eByteArray():
    assert hasattr(model::ETypes, "eByteArray")
    descriptor = None
    for klass in model::ETypes.__mro__:
        if "eByteArray" in klass.__dict__:
            descriptor = klass.__dict__["eByteArray"]
            break
    assert isinstance(descriptor, property)

def test_model::etypes_has_eStrings():
    assert hasattr(model::ETypes, "eStrings")
    descriptor = None
    for klass in model::ETypes.__mro__:
        if "eStrings" in klass.__dict__:
            descriptor = klass.__dict__["eStrings"]
            break
    assert isinstance(descriptor, property)

def test_model::etypes_has_eShort():
    assert hasattr(model::ETypes, "eShort")
    descriptor = None
    for klass in model::ETypes.__mro__:
        if "eShort" in klass.__dict__:
            descriptor = klass.__dict__["eShort"]
            break
    assert isinstance(descriptor, property)

def test_model::etypes_has_eChar():
    assert hasattr(model::ETypes, "eChar")
    descriptor = None
    for klass in model::ETypes.__mro__:
        if "eChar" in klass.__dict__:
            descriptor = klass.__dict__["eChar"]
            break
    assert isinstance(descriptor, property)

def test_model::etypes_has_eDouble():
    assert hasattr(model::ETypes, "eDouble")
    descriptor = None
    for klass in model::ETypes.__mro__:
        if "eDouble" in klass.__dict__:
            descriptor = klass.__dict__["eDouble"]
            break
    assert isinstance(descriptor, property)

def test_sex_exists():
    # Check that the Enumeration exists
    assert Sex is not None

def test_sex_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Sex]
    expected_literals = [
        "FEMALE",
        "MALE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Sex"


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
model::EStringToStringMapEntry_strategy = st.builds(
    model::EStringToStringMapEntry,
)
model::ObjectWithMap_strategy = st.builds(
    model::ObjectWithMap,
)
model::AbstractType_strategy = st.builds(
    model::AbstractType,
    name=
        safe_text
)
model::Container_strategy = st.builds(
    model::Container,
)
model::Node_strategy = st.builds(
    model::Node,
    label=
        safe_text
)
AbstractType_strategy = st.builds(
    AbstractType,
)
model::ConcreteTypeTwo_strategy = st.builds(
    model::ConcreteTypeTwo,
    propTypeTwo=
        safe_text
)
model::ConcreteTypeOne_strategy = st.builds(
    model::ConcreteTypeOne,
    propTypeOne=
        safe_text
)
model::TargetObject_strategy = st.builds(
    model::TargetObject,
    arrayAttribute=
        safe_text,
    singleAttribute=
        safe_text
)
model::PrimaryObject_strategy = st.builds(
    model::PrimaryObject,
    name=
        safe_text,
    unsettableAttribute=
        safe_text,
    featureMapReferenceCollection=
        safe_text,
    unsettableAttributeWithNonNullDefault=
        safe_text,
    featureMapAttributeCollection=
        safe_text,
    featureMapAttributeType1=
        safe_text,
    idAttribute=
        safe_text,
    featureMapAttributeType2=
        safe_text
)
model::Address_strategy = st.builds(
    model::Address,
    street=
        safe_text,
    addId=
        safe_text,
    city=
        safe_text,
    number=
        safe_text
)
model::User_strategy = st.builds(
    model::User,
    birthDate=
        st.dates(),
    sex=
        safe_text,
    userId=
        safe_text,
    name=
        safe_text
)
model::ETypes_strategy = st.builds(
    model::ETypes,
    eString=
        safe_text,
    eByte=
        safe_text,
    eLong=
        safe_text,
    uris=
        safe_text,
    eBigDecimal=
        safe_text,
    eBigInteger=
        safe_text,
    eDoubles=
        safe_text,
    eInts=
        st.integers(),
    eDate=
        st.dates(),
    eInt=
        st.integers(),
    eFloat=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    eBooleans=
        safe_text,
    eBoolean=
        st.booleans(),
    doubleValue=
        safe_text,
    eByteArray=
        safe_text,
    eStrings=
        safe_text,
    eShort=
        safe_text,
    eChar=
        safe_text,
    eDouble=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=model::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_model::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, model::EStringToStringMapEntry)

@given(instance=model::ObjectWithMap_strategy)
@settings(max_examples=50)
def test_model::objectwithmap_instantiation(instance):
    assert isinstance(instance, model::ObjectWithMap)

@given(instance=model::AbstractType_strategy)
@settings(max_examples=50)
def test_model::abstracttype_instantiation(instance):
    assert isinstance(instance, model::AbstractType)

@given(instance=model::AbstractType_strategy)
def test_model::abstracttype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::AbstractType_strategy)
def test_model::abstracttype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::Container_strategy)
@settings(max_examples=50)
def test_model::container_instantiation(instance):
    assert isinstance(instance, model::Container)

@given(instance=model::Node_strategy)
@settings(max_examples=50)
def test_model::node_instantiation(instance):
    assert isinstance(instance, model::Node)

@given(instance=model::Node_strategy)
def test_model::node_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=model::Node_strategy)
def test_model::node_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=AbstractType_strategy)
@settings(max_examples=50)
def test_abstracttype_instantiation(instance):
    assert isinstance(instance, AbstractType)

@given(instance=model::ConcreteTypeTwo_strategy)
@settings(max_examples=50)
def test_model::concretetypetwo_instantiation(instance):
    assert isinstance(instance, model::ConcreteTypeTwo)

@given(instance=model::ConcreteTypeTwo_strategy)
def test_model::concretetypetwo_propTypeTwo_type(instance):
    assert isinstance(instance.propTypeTwo, str)


@given(instance=model::ConcreteTypeTwo_strategy)
def test_model::concretetypetwo_propTypeTwo_setter(instance):
    original = instance.propTypeTwo
    instance.propTypeTwo = original
    assert instance.propTypeTwo == original

@given(instance=model::ConcreteTypeOne_strategy)
@settings(max_examples=50)
def test_model::concretetypeone_instantiation(instance):
    assert isinstance(instance, model::ConcreteTypeOne)

@given(instance=model::ConcreteTypeOne_strategy)
def test_model::concretetypeone_propTypeOne_type(instance):
    assert isinstance(instance.propTypeOne, str)


@given(instance=model::ConcreteTypeOne_strategy)
def test_model::concretetypeone_propTypeOne_setter(instance):
    original = instance.propTypeOne
    instance.propTypeOne = original
    assert instance.propTypeOne == original

@given(instance=model::TargetObject_strategy)
@settings(max_examples=50)
def test_model::targetobject_instantiation(instance):
    assert isinstance(instance, model::TargetObject)

@given(instance=model::TargetObject_strategy)
def test_model::targetobject_arrayAttribute_type(instance):
    assert isinstance(instance.arrayAttribute, str)


@given(instance=model::TargetObject_strategy)
def test_model::targetobject_arrayAttribute_setter(instance):
    original = instance.arrayAttribute
    instance.arrayAttribute = original
    assert instance.arrayAttribute == original

@given(instance=model::TargetObject_strategy)
def test_model::targetobject_singleAttribute_type(instance):
    assert isinstance(instance.singleAttribute, str)


@given(instance=model::TargetObject_strategy)
def test_model::targetobject_singleAttribute_setter(instance):
    original = instance.singleAttribute
    instance.singleAttribute = original
    assert instance.singleAttribute == original

@given(instance=model::PrimaryObject_strategy)
@settings(max_examples=50)
def test_model::primaryobject_instantiation(instance):
    assert isinstance(instance, model::PrimaryObject)

@given(instance=model::PrimaryObject_strategy)
def test_model::primaryobject_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::PrimaryObject_strategy)
def test_model::primaryobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::PrimaryObject_strategy)
def test_model::primaryobject_unsettableAttribute_type(instance):
    assert isinstance(instance.unsettableAttribute, str)


@given(instance=model::PrimaryObject_strategy)
def test_model::primaryobject_unsettableAttribute_setter(instance):
    original = instance.unsettableAttribute
    instance.unsettableAttribute = original
    assert instance.unsettableAttribute == original

@given(instance=model::PrimaryObject_strategy)
def test_model::primaryobject_featureMapReferenceCollection_type(instance):
    assert isinstance(instance.featureMapReferenceCollection, str)


@given(instance=model::PrimaryObject_strategy)
def test_model::primaryobject_featureMapReferenceCollection_setter(instance):
    original = instance.featureMapReferenceCollection
    instance.featureMapReferenceCollection = original
    assert instance.featureMapReferenceCollection == original

@given(instance=model::PrimaryObject_strategy)
def test_model::primaryobject_unsettableAttributeWithNonNullDefault_type(instance):
    assert isinstance(instance.unsettableAttributeWithNonNullDefault, str)


@given(instance=model::PrimaryObject_strategy)
def test_model::primaryobject_unsettableAttributeWithNonNullDefault_setter(instance):
    original = instance.unsettableAttributeWithNonNullDefault
    instance.unsettableAttributeWithNonNullDefault = original
    assert instance.unsettableAttributeWithNonNullDefault == original

@given(instance=model::PrimaryObject_strategy)
def test_model::primaryobject_featureMapAttributeCollection_type(instance):
    assert isinstance(instance.featureMapAttributeCollection, str)


@given(instance=model::PrimaryObject_strategy)
def test_model::primaryobject_featureMapAttributeCollection_setter(instance):
    original = instance.featureMapAttributeCollection
    instance.featureMapAttributeCollection = original
    assert instance.featureMapAttributeCollection == original

@given(instance=model::PrimaryObject_strategy)
def test_model::primaryobject_featureMapAttributeType1_type(instance):
    assert isinstance(instance.featureMapAttributeType1, str)


@given(instance=model::PrimaryObject_strategy)
def test_model::primaryobject_featureMapAttributeType1_setter(instance):
    original = instance.featureMapAttributeType1
    instance.featureMapAttributeType1 = original
    assert instance.featureMapAttributeType1 == original

@given(instance=model::PrimaryObject_strategy)
def test_model::primaryobject_idAttribute_type(instance):
    assert isinstance(instance.idAttribute, str)


@given(instance=model::PrimaryObject_strategy)
def test_model::primaryobject_idAttribute_setter(instance):
    original = instance.idAttribute
    instance.idAttribute = original
    assert instance.idAttribute == original

@given(instance=model::PrimaryObject_strategy)
def test_model::primaryobject_featureMapAttributeType2_type(instance):
    assert isinstance(instance.featureMapAttributeType2, str)


@given(instance=model::PrimaryObject_strategy)
def test_model::primaryobject_featureMapAttributeType2_setter(instance):
    original = instance.featureMapAttributeType2
    instance.featureMapAttributeType2 = original
    assert instance.featureMapAttributeType2 == original

@given(instance=model::Address_strategy)
@settings(max_examples=50)
def test_model::address_instantiation(instance):
    assert isinstance(instance, model::Address)

@given(instance=model::Address_strategy)
def test_model::address_street_type(instance):
    assert isinstance(instance.street, str)


@given(instance=model::Address_strategy)
def test_model::address_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original

@given(instance=model::Address_strategy)
def test_model::address_addId_type(instance):
    assert isinstance(instance.addId, str)


@given(instance=model::Address_strategy)
def test_model::address_addId_setter(instance):
    original = instance.addId
    instance.addId = original
    assert instance.addId == original

@given(instance=model::Address_strategy)
def test_model::address_city_type(instance):
    assert isinstance(instance.city, str)


@given(instance=model::Address_strategy)
def test_model::address_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original

@given(instance=model::Address_strategy)
def test_model::address_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=model::Address_strategy)
def test_model::address_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=model::User_strategy)
@settings(max_examples=50)
def test_model::user_instantiation(instance):
    assert isinstance(instance, model::User)

@given(instance=model::User_strategy)
def test_model::user_birthDate_type(instance):
    assert isinstance(instance.birthDate, date)


@given(instance=model::User_strategy)
def test_model::user_birthDate_setter(instance):
    original = instance.birthDate
    instance.birthDate = original
    assert instance.birthDate == original

@given(instance=model::User_strategy)
def test_model::user_sex_type(instance):
    assert isinstance(instance.sex, str)


@given(instance=model::User_strategy)
def test_model::user_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original

@given(instance=model::User_strategy)
def test_model::user_userId_type(instance):
    assert isinstance(instance.userId, str)


@given(instance=model::User_strategy)
def test_model::user_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original

@given(instance=model::User_strategy)
def test_model::user_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::User_strategy)
def test_model::user_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::ETypes_strategy)
@settings(max_examples=50)
def test_model::etypes_instantiation(instance):
    assert isinstance(instance, model::ETypes)

@given(instance=model::ETypes_strategy)
def test_model::etypes_eString_type(instance):
    assert isinstance(instance.eString, str)


@given(instance=model::ETypes_strategy)
def test_model::etypes_eString_setter(instance):
    original = instance.eString
    instance.eString = original
    assert instance.eString == original

@given(instance=model::ETypes_strategy)
def test_model::etypes_eByte_type(instance):
    assert isinstance(instance.eByte, str)


@given(instance=model::ETypes_strategy)
def test_model::etypes_eByte_setter(instance):
    original = instance.eByte
    instance.eByte = original
    assert instance.eByte == original

@given(instance=model::ETypes_strategy)
def test_model::etypes_eLong_type(instance):
    assert isinstance(instance.eLong, str)


@given(instance=model::ETypes_strategy)
def test_model::etypes_eLong_setter(instance):
    original = instance.eLong
    instance.eLong = original
    assert instance.eLong == original

@given(instance=model::ETypes_strategy)
def test_model::etypes_uris_type(instance):
    assert isinstance(instance.uris, str)


@given(instance=model::ETypes_strategy)
def test_model::etypes_uris_setter(instance):
    original = instance.uris
    instance.uris = original
    assert instance.uris == original

@given(instance=model::ETypes_strategy)
def test_model::etypes_eBigDecimal_type(instance):
    assert isinstance(instance.eBigDecimal, str)


@given(instance=model::ETypes_strategy)
def test_model::etypes_eBigDecimal_setter(instance):
    original = instance.eBigDecimal
    instance.eBigDecimal = original
    assert instance.eBigDecimal == original

@given(instance=model::ETypes_strategy)
def test_model::etypes_eBigInteger_type(instance):
    assert isinstance(instance.eBigInteger, str)


@given(instance=model::ETypes_strategy)
def test_model::etypes_eBigInteger_setter(instance):
    original = instance.eBigInteger
    instance.eBigInteger = original
    assert instance.eBigInteger == original

@given(instance=model::ETypes_strategy)
def test_model::etypes_eDoubles_type(instance):
    assert isinstance(instance.eDoubles, str)


@given(instance=model::ETypes_strategy)
def test_model::etypes_eDoubles_setter(instance):
    original = instance.eDoubles
    instance.eDoubles = original
    assert instance.eDoubles == original

@given(instance=model::ETypes_strategy)
def test_model::etypes_eInts_type(instance):
    assert isinstance(instance.eInts, int)


@given(instance=model::ETypes_strategy)
def test_model::etypes_eInts_setter(instance):
    original = instance.eInts
    instance.eInts = original
    assert instance.eInts == original

@given(instance=model::ETypes_strategy)
def test_model::etypes_eDate_type(instance):
    assert isinstance(instance.eDate, date)


@given(instance=model::ETypes_strategy)
def test_model::etypes_eDate_setter(instance):
    original = instance.eDate
    instance.eDate = original
    assert instance.eDate == original

@given(instance=model::ETypes_strategy)
def test_model::etypes_eInt_type(instance):
    assert isinstance(instance.eInt, int)


@given(instance=model::ETypes_strategy)
def test_model::etypes_eInt_setter(instance):
    original = instance.eInt
    instance.eInt = original
    assert instance.eInt == original

@given(instance=model::ETypes_strategy)
def test_model::etypes_eFloat_type(instance):
    assert isinstance(instance.eFloat, float)


@given(instance=model::ETypes_strategy)
def test_model::etypes_eFloat_setter(instance):
    original = instance.eFloat
    instance.eFloat = original
    assert instance.eFloat == original

@given(instance=model::ETypes_strategy)
def test_model::etypes_eBooleans_type(instance):
    assert isinstance(instance.eBooleans, str)


@given(instance=model::ETypes_strategy)
def test_model::etypes_eBooleans_setter(instance):
    original = instance.eBooleans
    instance.eBooleans = original
    assert instance.eBooleans == original

@given(instance=model::ETypes_strategy)
def test_model::etypes_eBoolean_type(instance):
    assert isinstance(instance.eBoolean, bool)


@given(instance=model::ETypes_strategy)
def test_model::etypes_eBoolean_setter(instance):
    original = instance.eBoolean
    instance.eBoolean = original
    assert instance.eBoolean == original

@given(instance=model::ETypes_strategy)
def test_model::etypes_doubleValue_type(instance):
    assert isinstance(instance.doubleValue, str)


@given(instance=model::ETypes_strategy)
def test_model::etypes_doubleValue_setter(instance):
    original = instance.doubleValue
    instance.doubleValue = original
    assert instance.doubleValue == original

@given(instance=model::ETypes_strategy)
def test_model::etypes_eByteArray_type(instance):
    assert isinstance(instance.eByteArray, str)


@given(instance=model::ETypes_strategy)
def test_model::etypes_eByteArray_setter(instance):
    original = instance.eByteArray
    instance.eByteArray = original
    assert instance.eByteArray == original

@given(instance=model::ETypes_strategy)
def test_model::etypes_eStrings_type(instance):
    assert isinstance(instance.eStrings, str)


@given(instance=model::ETypes_strategy)
def test_model::etypes_eStrings_setter(instance):
    original = instance.eStrings
    instance.eStrings = original
    assert instance.eStrings == original

@given(instance=model::ETypes_strategy)
def test_model::etypes_eShort_type(instance):
    assert isinstance(instance.eShort, str)


@given(instance=model::ETypes_strategy)
def test_model::etypes_eShort_setter(instance):
    original = instance.eShort
    instance.eShort = original
    assert instance.eShort == original

@given(instance=model::ETypes_strategy)
def test_model::etypes_eChar_type(instance):
    assert isinstance(instance.eChar, str)


@given(instance=model::ETypes_strategy)
def test_model::etypes_eChar_setter(instance):
    original = instance.eChar
    instance.eChar = original
    assert instance.eChar == original

@given(instance=model::ETypes_strategy)
def test_model::etypes_eDouble_type(instance):
    assert isinstance(instance.eDouble, float)


@given(instance=model::ETypes_strategy)
def test_model::etypes_eDouble_setter(instance):
    original = instance.eDouble
    instance.eDouble = original
    assert instance.eDouble == original
