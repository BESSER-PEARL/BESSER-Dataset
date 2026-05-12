import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    model_EStringToStringMapEntry,
    model_ObjectWithMap,
    model_AbstractType,
    model_Container,
    model_Node,
    AbstractType,
    model_ConcreteTypeTwo,
    model_ConcreteTypeOne,
    model_TargetObject,
    model_PrimaryObject,
    model_Address,
    model_User,
    model_ETypes,
    Sex,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(model_EStringToStringMapEntry)


def test_model_estringtostringmapentry_constructor_exists():
    assert callable(model_EStringToStringMapEntry.__init__)


def test_model_estringtostringmapentry_constructor_args():
    sig = inspect.signature(model_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_model_objectwithmap_is_not_abstract():
    assert not inspect.isabstract(model_ObjectWithMap)


def test_model_objectwithmap_constructor_exists():
    assert callable(model_ObjectWithMap.__init__)


def test_model_objectwithmap_constructor_args():
    sig = inspect.signature(model_ObjectWithMap.__init__)
    params = list(sig.parameters.keys())



def test_model_abstracttype_is_not_abstract():
    assert not inspect.isabstract(model_AbstractType)


def test_model_abstracttype_constructor_exists():
    assert callable(model_AbstractType.__init__)


def test_model_abstracttype_constructor_args():
    sig = inspect.signature(model_AbstractType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_abstracttype_has_name():
    assert hasattr(model_AbstractType, "name")
    descriptor = None
    for klass in model_AbstractType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model_container_is_not_abstract():
    assert not inspect.isabstract(model_Container)


def test_model_container_constructor_exists():
    assert callable(model_Container.__init__)


def test_model_container_constructor_args():
    sig = inspect.signature(model_Container.__init__)
    params = list(sig.parameters.keys())



def test_model_node_is_not_abstract():
    assert not inspect.isabstract(model_Node)


def test_model_node_constructor_exists():
    assert callable(model_Node.__init__)


def test_model_node_constructor_args():
    sig = inspect.signature(model_Node.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_model_node_has_label():
    assert hasattr(model_Node, "label")
    descriptor = None
    for klass in model_Node.__mro__:
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



def test_model_concretetypetwo_is_not_abstract():
    assert not inspect.isabstract(model_ConcreteTypeTwo)


def test_model_concretetypetwo_constructor_exists():
    assert callable(model_ConcreteTypeTwo.__init__)


def test_model_concretetypetwo_constructor_args():
    sig = inspect.signature(model_ConcreteTypeTwo.__init__)
    params = list(sig.parameters.keys())
    assert "propTypeTwo" in params, "Missing parameter 'propTypeTwo'"

def test_model_concretetypetwo_has_propTypeTwo():
    assert hasattr(model_ConcreteTypeTwo, "propTypeTwo")
    descriptor = None
    for klass in model_ConcreteTypeTwo.__mro__:
        if "propTypeTwo" in klass.__dict__:
            descriptor = klass.__dict__["propTypeTwo"]
            break
    assert isinstance(descriptor, property)



def test_model_concretetypeone_is_not_abstract():
    assert not inspect.isabstract(model_ConcreteTypeOne)


def test_model_concretetypeone_constructor_exists():
    assert callable(model_ConcreteTypeOne.__init__)


def test_model_concretetypeone_constructor_args():
    sig = inspect.signature(model_ConcreteTypeOne.__init__)
    params = list(sig.parameters.keys())
    assert "propTypeOne" in params, "Missing parameter 'propTypeOne'"

def test_model_concretetypeone_has_propTypeOne():
    assert hasattr(model_ConcreteTypeOne, "propTypeOne")
    descriptor = None
    for klass in model_ConcreteTypeOne.__mro__:
        if "propTypeOne" in klass.__dict__:
            descriptor = klass.__dict__["propTypeOne"]
            break
    assert isinstance(descriptor, property)



def test_model_targetobject_is_not_abstract():
    assert not inspect.isabstract(model_TargetObject)


def test_model_targetobject_constructor_exists():
    assert callable(model_TargetObject.__init__)


def test_model_targetobject_constructor_args():
    sig = inspect.signature(model_TargetObject.__init__)
    params = list(sig.parameters.keys())
    assert "arrayAttribute" in params, "Missing parameter 'arrayAttribute'"
    assert "singleAttribute" in params, "Missing parameter 'singleAttribute'"

def test_model_targetobject_has_arrayAttribute():
    assert hasattr(model_TargetObject, "arrayAttribute")
    descriptor = None
    for klass in model_TargetObject.__mro__:
        if "arrayAttribute" in klass.__dict__:
            descriptor = klass.__dict__["arrayAttribute"]
            break
    assert isinstance(descriptor, property)

def test_model_targetobject_has_singleAttribute():
    assert hasattr(model_TargetObject, "singleAttribute")
    descriptor = None
    for klass in model_TargetObject.__mro__:
        if "singleAttribute" in klass.__dict__:
            descriptor = klass.__dict__["singleAttribute"]
            break
    assert isinstance(descriptor, property)



def test_model_primaryobject_is_not_abstract():
    assert not inspect.isabstract(model_PrimaryObject)


def test_model_primaryobject_constructor_exists():
    assert callable(model_PrimaryObject.__init__)


def test_model_primaryobject_constructor_args():
    sig = inspect.signature(model_PrimaryObject.__init__)
    params = list(sig.parameters.keys())
    assert "idAttribute" in params, "Missing parameter 'idAttribute'"
    assert "featureMapAttributeType1" in params, "Missing parameter 'featureMapAttributeType1'"
    assert "unsettableAttribute" in params, "Missing parameter 'unsettableAttribute'"
    assert "featureMapAttributeType2" in params, "Missing parameter 'featureMapAttributeType2'"
    assert "featureMapReferenceCollection" in params, "Missing parameter 'featureMapReferenceCollection'"
    assert "featureMapAttributeCollection" in params, "Missing parameter 'featureMapAttributeCollection'"
    assert "unsettableAttributeWithNonNullDefault" in params, "Missing parameter 'unsettableAttributeWithNonNullDefault'"
    assert "name" in params, "Missing parameter 'name'"

def test_model_primaryobject_has_idAttribute():
    assert hasattr(model_PrimaryObject, "idAttribute")
    descriptor = None
    for klass in model_PrimaryObject.__mro__:
        if "idAttribute" in klass.__dict__:
            descriptor = klass.__dict__["idAttribute"]
            break
    assert isinstance(descriptor, property)

def test_model_primaryobject_has_featureMapAttributeType1():
    assert hasattr(model_PrimaryObject, "featureMapAttributeType1")
    descriptor = None
    for klass in model_PrimaryObject.__mro__:
        if "featureMapAttributeType1" in klass.__dict__:
            descriptor = klass.__dict__["featureMapAttributeType1"]
            break
    assert isinstance(descriptor, property)

def test_model_primaryobject_has_unsettableAttribute():
    assert hasattr(model_PrimaryObject, "unsettableAttribute")
    descriptor = None
    for klass in model_PrimaryObject.__mro__:
        if "unsettableAttribute" in klass.__dict__:
            descriptor = klass.__dict__["unsettableAttribute"]
            break
    assert isinstance(descriptor, property)

def test_model_primaryobject_has_featureMapAttributeType2():
    assert hasattr(model_PrimaryObject, "featureMapAttributeType2")
    descriptor = None
    for klass in model_PrimaryObject.__mro__:
        if "featureMapAttributeType2" in klass.__dict__:
            descriptor = klass.__dict__["featureMapAttributeType2"]
            break
    assert isinstance(descriptor, property)

def test_model_primaryobject_has_featureMapReferenceCollection():
    assert hasattr(model_PrimaryObject, "featureMapReferenceCollection")
    descriptor = None
    for klass in model_PrimaryObject.__mro__:
        if "featureMapReferenceCollection" in klass.__dict__:
            descriptor = klass.__dict__["featureMapReferenceCollection"]
            break
    assert isinstance(descriptor, property)

def test_model_primaryobject_has_featureMapAttributeCollection():
    assert hasattr(model_PrimaryObject, "featureMapAttributeCollection")
    descriptor = None
    for klass in model_PrimaryObject.__mro__:
        if "featureMapAttributeCollection" in klass.__dict__:
            descriptor = klass.__dict__["featureMapAttributeCollection"]
            break
    assert isinstance(descriptor, property)

def test_model_primaryobject_has_unsettableAttributeWithNonNullDefault():
    assert hasattr(model_PrimaryObject, "unsettableAttributeWithNonNullDefault")
    descriptor = None
    for klass in model_PrimaryObject.__mro__:
        if "unsettableAttributeWithNonNullDefault" in klass.__dict__:
            descriptor = klass.__dict__["unsettableAttributeWithNonNullDefault"]
            break
    assert isinstance(descriptor, property)

def test_model_primaryobject_has_name():
    assert hasattr(model_PrimaryObject, "name")
    descriptor = None
    for klass in model_PrimaryObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model_address_is_not_abstract():
    assert not inspect.isabstract(model_Address)


def test_model_address_constructor_exists():
    assert callable(model_Address.__init__)


def test_model_address_constructor_args():
    sig = inspect.signature(model_Address.__init__)
    params = list(sig.parameters.keys())
    assert "street" in params, "Missing parameter 'street'"
    assert "number" in params, "Missing parameter 'number'"
    assert "addId" in params, "Missing parameter 'addId'"
    assert "city" in params, "Missing parameter 'city'"

def test_model_address_has_street():
    assert hasattr(model_Address, "street")
    descriptor = None
    for klass in model_Address.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_model_address_has_number():
    assert hasattr(model_Address, "number")
    descriptor = None
    for klass in model_Address.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_model_address_has_addId():
    assert hasattr(model_Address, "addId")
    descriptor = None
    for klass in model_Address.__mro__:
        if "addId" in klass.__dict__:
            descriptor = klass.__dict__["addId"]
            break
    assert isinstance(descriptor, property)

def test_model_address_has_city():
    assert hasattr(model_Address, "city")
    descriptor = None
    for klass in model_Address.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)



def test_model_user_is_not_abstract():
    assert not inspect.isabstract(model_User)


def test_model_user_constructor_exists():
    assert callable(model_User.__init__)


def test_model_user_constructor_args():
    sig = inspect.signature(model_User.__init__)
    params = list(sig.parameters.keys())
    assert "userId" in params, "Missing parameter 'userId'"
    assert "name" in params, "Missing parameter 'name'"
    assert "sex" in params, "Missing parameter 'sex'"
    assert "birthDate" in params, "Missing parameter 'birthDate'"

def test_model_user_has_userId():
    assert hasattr(model_User, "userId")
    descriptor = None
    for klass in model_User.__mro__:
        if "userId" in klass.__dict__:
            descriptor = klass.__dict__["userId"]
            break
    assert isinstance(descriptor, property)

def test_model_user_has_name():
    assert hasattr(model_User, "name")
    descriptor = None
    for klass in model_User.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model_user_has_sex():
    assert hasattr(model_User, "sex")
    descriptor = None
    for klass in model_User.__mro__:
        if "sex" in klass.__dict__:
            descriptor = klass.__dict__["sex"]
            break
    assert isinstance(descriptor, property)

def test_model_user_has_birthDate():
    assert hasattr(model_User, "birthDate")
    descriptor = None
    for klass in model_User.__mro__:
        if "birthDate" in klass.__dict__:
            descriptor = klass.__dict__["birthDate"]
            break
    assert isinstance(descriptor, property)



def test_model_etypes_is_not_abstract():
    assert not inspect.isabstract(model_ETypes)


def test_model_etypes_constructor_exists():
    assert callable(model_ETypes.__init__)


def test_model_etypes_constructor_args():
    sig = inspect.signature(model_ETypes.__init__)
    params = list(sig.parameters.keys())
    assert "eByte" in params, "Missing parameter 'eByte'"
    assert "eString" in params, "Missing parameter 'eString'"
    assert "eBoolean" in params, "Missing parameter 'eBoolean'"
    assert "eBigInteger" in params, "Missing parameter 'eBigInteger'"
    assert "eDate" in params, "Missing parameter 'eDate'"
    assert "eDouble" in params, "Missing parameter 'eDouble'"
    assert "eFloat" in params, "Missing parameter 'eFloat'"
    assert "eShort" in params, "Missing parameter 'eShort'"
    assert "uris" in params, "Missing parameter 'uris'"
    assert "eStrings" in params, "Missing parameter 'eStrings'"
    assert "eBooleans" in params, "Missing parameter 'eBooleans'"
    assert "eByteArray" in params, "Missing parameter 'eByteArray'"
    assert "eDoubles" in params, "Missing parameter 'eDoubles'"
    assert "eBigDecimal" in params, "Missing parameter 'eBigDecimal'"
    assert "eInts" in params, "Missing parameter 'eInts'"
    assert "eInt" in params, "Missing parameter 'eInt'"
    assert "eChar" in params, "Missing parameter 'eChar'"
    assert "doubleValue" in params, "Missing parameter 'doubleValue'"
    assert "eLong" in params, "Missing parameter 'eLong'"

def test_model_etypes_has_eByte():
    assert hasattr(model_ETypes, "eByte")
    descriptor = None
    for klass in model_ETypes.__mro__:
        if "eByte" in klass.__dict__:
            descriptor = klass.__dict__["eByte"]
            break
    assert isinstance(descriptor, property)

def test_model_etypes_has_eString():
    assert hasattr(model_ETypes, "eString")
    descriptor = None
    for klass in model_ETypes.__mro__:
        if "eString" in klass.__dict__:
            descriptor = klass.__dict__["eString"]
            break
    assert isinstance(descriptor, property)

def test_model_etypes_has_eBoolean():
    assert hasattr(model_ETypes, "eBoolean")
    descriptor = None
    for klass in model_ETypes.__mro__:
        if "eBoolean" in klass.__dict__:
            descriptor = klass.__dict__["eBoolean"]
            break
    assert isinstance(descriptor, property)

def test_model_etypes_has_eBigInteger():
    assert hasattr(model_ETypes, "eBigInteger")
    descriptor = None
    for klass in model_ETypes.__mro__:
        if "eBigInteger" in klass.__dict__:
            descriptor = klass.__dict__["eBigInteger"]
            break
    assert isinstance(descriptor, property)

def test_model_etypes_has_eDate():
    assert hasattr(model_ETypes, "eDate")
    descriptor = None
    for klass in model_ETypes.__mro__:
        if "eDate" in klass.__dict__:
            descriptor = klass.__dict__["eDate"]
            break
    assert isinstance(descriptor, property)

def test_model_etypes_has_eDouble():
    assert hasattr(model_ETypes, "eDouble")
    descriptor = None
    for klass in model_ETypes.__mro__:
        if "eDouble" in klass.__dict__:
            descriptor = klass.__dict__["eDouble"]
            break
    assert isinstance(descriptor, property)

def test_model_etypes_has_eFloat():
    assert hasattr(model_ETypes, "eFloat")
    descriptor = None
    for klass in model_ETypes.__mro__:
        if "eFloat" in klass.__dict__:
            descriptor = klass.__dict__["eFloat"]
            break
    assert isinstance(descriptor, property)

def test_model_etypes_has_eShort():
    assert hasattr(model_ETypes, "eShort")
    descriptor = None
    for klass in model_ETypes.__mro__:
        if "eShort" in klass.__dict__:
            descriptor = klass.__dict__["eShort"]
            break
    assert isinstance(descriptor, property)

def test_model_etypes_has_uris():
    assert hasattr(model_ETypes, "uris")
    descriptor = None
    for klass in model_ETypes.__mro__:
        if "uris" in klass.__dict__:
            descriptor = klass.__dict__["uris"]
            break
    assert isinstance(descriptor, property)

def test_model_etypes_has_eStrings():
    assert hasattr(model_ETypes, "eStrings")
    descriptor = None
    for klass in model_ETypes.__mro__:
        if "eStrings" in klass.__dict__:
            descriptor = klass.__dict__["eStrings"]
            break
    assert isinstance(descriptor, property)

def test_model_etypes_has_eBooleans():
    assert hasattr(model_ETypes, "eBooleans")
    descriptor = None
    for klass in model_ETypes.__mro__:
        if "eBooleans" in klass.__dict__:
            descriptor = klass.__dict__["eBooleans"]
            break
    assert isinstance(descriptor, property)

def test_model_etypes_has_eByteArray():
    assert hasattr(model_ETypes, "eByteArray")
    descriptor = None
    for klass in model_ETypes.__mro__:
        if "eByteArray" in klass.__dict__:
            descriptor = klass.__dict__["eByteArray"]
            break
    assert isinstance(descriptor, property)

def test_model_etypes_has_eDoubles():
    assert hasattr(model_ETypes, "eDoubles")
    descriptor = None
    for klass in model_ETypes.__mro__:
        if "eDoubles" in klass.__dict__:
            descriptor = klass.__dict__["eDoubles"]
            break
    assert isinstance(descriptor, property)

def test_model_etypes_has_eBigDecimal():
    assert hasattr(model_ETypes, "eBigDecimal")
    descriptor = None
    for klass in model_ETypes.__mro__:
        if "eBigDecimal" in klass.__dict__:
            descriptor = klass.__dict__["eBigDecimal"]
            break
    assert isinstance(descriptor, property)

def test_model_etypes_has_eInts():
    assert hasattr(model_ETypes, "eInts")
    descriptor = None
    for klass in model_ETypes.__mro__:
        if "eInts" in klass.__dict__:
            descriptor = klass.__dict__["eInts"]
            break
    assert isinstance(descriptor, property)

def test_model_etypes_has_eInt():
    assert hasattr(model_ETypes, "eInt")
    descriptor = None
    for klass in model_ETypes.__mro__:
        if "eInt" in klass.__dict__:
            descriptor = klass.__dict__["eInt"]
            break
    assert isinstance(descriptor, property)

def test_model_etypes_has_eChar():
    assert hasattr(model_ETypes, "eChar")
    descriptor = None
    for klass in model_ETypes.__mro__:
        if "eChar" in klass.__dict__:
            descriptor = klass.__dict__["eChar"]
            break
    assert isinstance(descriptor, property)

def test_model_etypes_has_doubleValue():
    assert hasattr(model_ETypes, "doubleValue")
    descriptor = None
    for klass in model_ETypes.__mro__:
        if "doubleValue" in klass.__dict__:
            descriptor = klass.__dict__["doubleValue"]
            break
    assert isinstance(descriptor, property)

def test_model_etypes_has_eLong():
    assert hasattr(model_ETypes, "eLong")
    descriptor = None
    for klass in model_ETypes.__mro__:
        if "eLong" in klass.__dict__:
            descriptor = klass.__dict__["eLong"]
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
model_EStringToStringMapEntry_strategy = st.builds(
    model_EStringToStringMapEntry,
)
model_ObjectWithMap_strategy = st.builds(
    model_ObjectWithMap,
)
model_AbstractType_strategy = st.builds(
    model_AbstractType,
    name=
        safe_text
)
model_Container_strategy = st.builds(
    model_Container,
)
model_Node_strategy = st.builds(
    model_Node,
    label=
        safe_text
)
AbstractType_strategy = st.builds(
    AbstractType,
)
model_ConcreteTypeTwo_strategy = st.builds(
    model_ConcreteTypeTwo,
    propTypeTwo=
        safe_text
)
model_ConcreteTypeOne_strategy = st.builds(
    model_ConcreteTypeOne,
    propTypeOne=
        safe_text
)
model_TargetObject_strategy = st.builds(
    model_TargetObject,
    arrayAttribute=
        safe_text,
    singleAttribute=
        safe_text
)
model_PrimaryObject_strategy = st.builds(
    model_PrimaryObject,
    idAttribute=
        safe_text,
    featureMapAttributeType1=
        safe_text,
    unsettableAttribute=
        safe_text,
    featureMapAttributeType2=
        safe_text,
    featureMapReferenceCollection=
        safe_text,
    featureMapAttributeCollection=
        safe_text,
    unsettableAttributeWithNonNullDefault=
        safe_text,
    name=
        safe_text
)
model_Address_strategy = st.builds(
    model_Address,
    street=
        safe_text,
    number=
        safe_text,
    addId=
        safe_text,
    city=
        safe_text
)
model_User_strategy = st.builds(
    model_User,
    userId=
        safe_text,
    name=
        safe_text,
    sex=
        safe_text,
    birthDate=
        st.dates()
)
model_ETypes_strategy = st.builds(
    model_ETypes,
    eByte=
        safe_text,
    eString=
        safe_text,
    eBoolean=
        st.booleans(),
    eBigInteger=
        safe_text,
    eDate=
        st.dates(),
    eDouble=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    eFloat=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    eShort=
        safe_text,
    uris=
        safe_text,
    eStrings=
        safe_text,
    eBooleans=
        safe_text,
    eByteArray=
        safe_text,
    eDoubles=
        safe_text,
    eBigDecimal=
        safe_text,
    eInts=
        st.integers(),
    eInt=
        st.integers(),
    eChar=
        safe_text,
    doubleValue=
        safe_text,
    eLong=
        safe_text
)

@given(instance=model_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_model_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, model_EStringToStringMapEntry)

@given(instance=model_ObjectWithMap_strategy)
@settings(max_examples=50)
def test_model_objectwithmap_instantiation(instance):
    assert isinstance(instance, model_ObjectWithMap)

@given(instance=model_AbstractType_strategy)
@settings(max_examples=50)
def test_model_abstracttype_instantiation(instance):
    assert isinstance(instance, model_AbstractType)



@given(instance=model_AbstractType_strategy)
def test_model_abstracttype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model_Container_strategy)
@settings(max_examples=50)
def test_model_container_instantiation(instance):
    assert isinstance(instance, model_Container)

@given(instance=model_Node_strategy)
@settings(max_examples=50)
def test_model_node_instantiation(instance):
    assert isinstance(instance, model_Node)



@given(instance=model_Node_strategy)
def test_model_node_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=AbstractType_strategy)
@settings(max_examples=50)
def test_abstracttype_instantiation(instance):
    assert isinstance(instance, AbstractType)

@given(instance=model_ConcreteTypeTwo_strategy)
@settings(max_examples=50)
def test_model_concretetypetwo_instantiation(instance):
    assert isinstance(instance, model_ConcreteTypeTwo)



@given(instance=model_ConcreteTypeTwo_strategy)
def test_model_concretetypetwo_propTypeTwo_setter(instance):
    original = instance.propTypeTwo
    instance.propTypeTwo = original
    assert instance.propTypeTwo == original

@given(instance=model_ConcreteTypeOne_strategy)
@settings(max_examples=50)
def test_model_concretetypeone_instantiation(instance):
    assert isinstance(instance, model_ConcreteTypeOne)



@given(instance=model_ConcreteTypeOne_strategy)
def test_model_concretetypeone_propTypeOne_setter(instance):
    original = instance.propTypeOne
    instance.propTypeOne = original
    assert instance.propTypeOne == original

@given(instance=model_TargetObject_strategy)
@settings(max_examples=50)
def test_model_targetobject_instantiation(instance):
    assert isinstance(instance, model_TargetObject)



@given(instance=model_TargetObject_strategy)
def test_model_targetobject_arrayAttribute_setter(instance):
    original = instance.arrayAttribute
    instance.arrayAttribute = original
    assert instance.arrayAttribute == original



@given(instance=model_TargetObject_strategy)
def test_model_targetobject_singleAttribute_setter(instance):
    original = instance.singleAttribute
    instance.singleAttribute = original
    assert instance.singleAttribute == original

@given(instance=model_PrimaryObject_strategy)
@settings(max_examples=50)
def test_model_primaryobject_instantiation(instance):
    assert isinstance(instance, model_PrimaryObject)



@given(instance=model_PrimaryObject_strategy)
def test_model_primaryobject_idAttribute_setter(instance):
    original = instance.idAttribute
    instance.idAttribute = original
    assert instance.idAttribute == original



@given(instance=model_PrimaryObject_strategy)
def test_model_primaryobject_featureMapAttributeType1_setter(instance):
    original = instance.featureMapAttributeType1
    instance.featureMapAttributeType1 = original
    assert instance.featureMapAttributeType1 == original



@given(instance=model_PrimaryObject_strategy)
def test_model_primaryobject_unsettableAttribute_setter(instance):
    original = instance.unsettableAttribute
    instance.unsettableAttribute = original
    assert instance.unsettableAttribute == original



@given(instance=model_PrimaryObject_strategy)
def test_model_primaryobject_featureMapAttributeType2_setter(instance):
    original = instance.featureMapAttributeType2
    instance.featureMapAttributeType2 = original
    assert instance.featureMapAttributeType2 == original



@given(instance=model_PrimaryObject_strategy)
def test_model_primaryobject_featureMapReferenceCollection_setter(instance):
    original = instance.featureMapReferenceCollection
    instance.featureMapReferenceCollection = original
    assert instance.featureMapReferenceCollection == original



@given(instance=model_PrimaryObject_strategy)
def test_model_primaryobject_featureMapAttributeCollection_setter(instance):
    original = instance.featureMapAttributeCollection
    instance.featureMapAttributeCollection = original
    assert instance.featureMapAttributeCollection == original



@given(instance=model_PrimaryObject_strategy)
def test_model_primaryobject_unsettableAttributeWithNonNullDefault_setter(instance):
    original = instance.unsettableAttributeWithNonNullDefault
    instance.unsettableAttributeWithNonNullDefault = original
    assert instance.unsettableAttributeWithNonNullDefault == original



@given(instance=model_PrimaryObject_strategy)
def test_model_primaryobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model_Address_strategy)
@settings(max_examples=50)
def test_model_address_instantiation(instance):
    assert isinstance(instance, model_Address)



@given(instance=model_Address_strategy)
def test_model_address_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original



@given(instance=model_Address_strategy)
def test_model_address_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=model_Address_strategy)
def test_model_address_addId_setter(instance):
    original = instance.addId
    instance.addId = original
    assert instance.addId == original



@given(instance=model_Address_strategy)
def test_model_address_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original

@given(instance=model_User_strategy)
@settings(max_examples=50)
def test_model_user_instantiation(instance):
    assert isinstance(instance, model_User)



@given(instance=model_User_strategy)
def test_model_user_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original



@given(instance=model_User_strategy)
def test_model_user_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=model_User_strategy)
def test_model_user_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original



@given(instance=model_User_strategy)
def test_model_user_birthDate_setter(instance):
    original = instance.birthDate
    instance.birthDate = original
    assert instance.birthDate == original

@given(instance=model_ETypes_strategy)
@settings(max_examples=50)
def test_model_etypes_instantiation(instance):
    assert isinstance(instance, model_ETypes)



@given(instance=model_ETypes_strategy)
def test_model_etypes_eByte_setter(instance):
    original = instance.eByte
    instance.eByte = original
    assert instance.eByte == original



@given(instance=model_ETypes_strategy)
def test_model_etypes_eString_setter(instance):
    original = instance.eString
    instance.eString = original
    assert instance.eString == original



@given(instance=model_ETypes_strategy)
def test_model_etypes_eBoolean_setter(instance):
    original = instance.eBoolean
    instance.eBoolean = original
    assert instance.eBoolean == original



@given(instance=model_ETypes_strategy)
def test_model_etypes_eBigInteger_setter(instance):
    original = instance.eBigInteger
    instance.eBigInteger = original
    assert instance.eBigInteger == original



@given(instance=model_ETypes_strategy)
def test_model_etypes_eDate_setter(instance):
    original = instance.eDate
    instance.eDate = original
    assert instance.eDate == original



@given(instance=model_ETypes_strategy)
def test_model_etypes_eDouble_setter(instance):
    original = instance.eDouble
    instance.eDouble = original
    assert instance.eDouble == original



@given(instance=model_ETypes_strategy)
def test_model_etypes_eFloat_setter(instance):
    original = instance.eFloat
    instance.eFloat = original
    assert instance.eFloat == original



@given(instance=model_ETypes_strategy)
def test_model_etypes_eShort_setter(instance):
    original = instance.eShort
    instance.eShort = original
    assert instance.eShort == original



@given(instance=model_ETypes_strategy)
def test_model_etypes_uris_setter(instance):
    original = instance.uris
    instance.uris = original
    assert instance.uris == original



@given(instance=model_ETypes_strategy)
def test_model_etypes_eStrings_setter(instance):
    original = instance.eStrings
    instance.eStrings = original
    assert instance.eStrings == original



@given(instance=model_ETypes_strategy)
def test_model_etypes_eBooleans_setter(instance):
    original = instance.eBooleans
    instance.eBooleans = original
    assert instance.eBooleans == original



@given(instance=model_ETypes_strategy)
def test_model_etypes_eByteArray_setter(instance):
    original = instance.eByteArray
    instance.eByteArray = original
    assert instance.eByteArray == original



@given(instance=model_ETypes_strategy)
def test_model_etypes_eDoubles_setter(instance):
    original = instance.eDoubles
    instance.eDoubles = original
    assert instance.eDoubles == original



@given(instance=model_ETypes_strategy)
def test_model_etypes_eBigDecimal_setter(instance):
    original = instance.eBigDecimal
    instance.eBigDecimal = original
    assert instance.eBigDecimal == original



@given(instance=model_ETypes_strategy)
def test_model_etypes_eInts_setter(instance):
    original = instance.eInts
    instance.eInts = original
    assert instance.eInts == original



@given(instance=model_ETypes_strategy)
def test_model_etypes_eInt_setter(instance):
    original = instance.eInt
    instance.eInt = original
    assert instance.eInt == original



@given(instance=model_ETypes_strategy)
def test_model_etypes_eChar_setter(instance):
    original = instance.eChar
    instance.eChar = original
    assert instance.eChar == original



@given(instance=model_ETypes_strategy)
def test_model_etypes_doubleValue_setter(instance):
    original = instance.doubleValue
    instance.doubleValue = original
    assert instance.doubleValue == original



@given(instance=model_ETypes_strategy)
def test_model_etypes_eLong_setter(instance):
    original = instance.eLong
    instance.eLong = original
    assert instance.eLong == original
