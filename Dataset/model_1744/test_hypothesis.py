import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    model_TargetObject,
    model_PrimaryObject,
    model_MappedLibrary,
    model_Location,
    model_Library,
    model_Book,
    model_Person,
    model_ETypes,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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
    assert "name" in params, "Missing parameter 'name'"
    assert "featureMapReferenceCollection" in params, "Missing parameter 'featureMapReferenceCollection'"
    assert "featureMapAttributeType1" in params, "Missing parameter 'featureMapAttributeType1'"
    assert "featureMapAttributeType2" in params, "Missing parameter 'featureMapAttributeType2'"
    assert "featureMapAttributeCollection" in params, "Missing parameter 'featureMapAttributeCollection'"

def test_model_primaryobject_has_name():
    assert hasattr(model_PrimaryObject, "name")
    descriptor = None
    for klass in model_PrimaryObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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

def test_model_primaryobject_has_featureMapAttributeType1():
    assert hasattr(model_PrimaryObject, "featureMapAttributeType1")
    descriptor = None
    for klass in model_PrimaryObject.__mro__:
        if "featureMapAttributeType1" in klass.__dict__:
            descriptor = klass.__dict__["featureMapAttributeType1"]
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

def test_model_primaryobject_has_featureMapAttributeCollection():
    assert hasattr(model_PrimaryObject, "featureMapAttributeCollection")
    descriptor = None
    for klass in model_PrimaryObject.__mro__:
        if "featureMapAttributeCollection" in klass.__dict__:
            descriptor = klass.__dict__["featureMapAttributeCollection"]
            break
    assert isinstance(descriptor, property)



def test_model_mappedlibrary_is_not_abstract():
    assert not inspect.isabstract(model_MappedLibrary)


def test_model_mappedlibrary_constructor_exists():
    assert callable(model_MappedLibrary.__init__)


def test_model_mappedlibrary_constructor_args():
    sig = inspect.signature(model_MappedLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "books" in params, "Missing parameter 'books'"

def test_model_mappedlibrary_has_books():
    assert hasattr(model_MappedLibrary, "books")
    descriptor = None
    for klass in model_MappedLibrary.__mro__:
        if "books" in klass.__dict__:
            descriptor = klass.__dict__["books"]
            break
    assert isinstance(descriptor, property)



def test_model_location_is_not_abstract():
    assert not inspect.isabstract(model_Location)


def test_model_location_constructor_exists():
    assert callable(model_Location.__init__)


def test_model_location_constructor_args():
    sig = inspect.signature(model_Location.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "id" in params, "Missing parameter 'id'"

def test_model_location_has_address():
    assert hasattr(model_Location, "address")
    descriptor = None
    for klass in model_Location.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_model_location_has_id():
    assert hasattr(model_Location, "id")
    descriptor = None
    for klass in model_Location.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_model_library_is_not_abstract():
    assert not inspect.isabstract(model_Library)


def test_model_library_constructor_exists():
    assert callable(model_Library.__init__)


def test_model_library_constructor_args():
    sig = inspect.signature(model_Library.__init__)
    params = list(sig.parameters.keys())



def test_model_book_is_not_abstract():
    assert not inspect.isabstract(model_Book)


def test_model_book_constructor_exists():
    assert callable(model_Book.__init__)


def test_model_book_constructor_args():
    sig = inspect.signature(model_Book.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"
    assert "tags" in params, "Missing parameter 'tags'"
    assert "title" in params, "Missing parameter 'title'"

def test_model_book_has_data():
    assert hasattr(model_Book, "data")
    descriptor = None
    for klass in model_Book.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)

def test_model_book_has_tags():
    assert hasattr(model_Book, "tags")
    descriptor = None
    for klass in model_Book.__mro__:
        if "tags" in klass.__dict__:
            descriptor = klass.__dict__["tags"]
            break
    assert isinstance(descriptor, property)

def test_model_book_has_title():
    assert hasattr(model_Book, "title")
    descriptor = None
    for klass in model_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_model_person_is_not_abstract():
    assert not inspect.isabstract(model_Person)


def test_model_person_constructor_exists():
    assert callable(model_Person.__init__)


def test_model_person_constructor_args():
    sig = inspect.signature(model_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_person_has_name():
    assert hasattr(model_Person, "name")
    descriptor = None
    for klass in model_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model_etypes_is_not_abstract():
    assert not inspect.isabstract(model_ETypes)


def test_model_etypes_constructor_exists():
    assert callable(model_ETypes.__init__)


def test_model_etypes_constructor_args():
    sig = inspect.signature(model_ETypes.__init__)
    params = list(sig.parameters.keys())
    assert "eLong" in params, "Missing parameter 'eLong'"
    assert "eByteArray" in params, "Missing parameter 'eByteArray'"
    assert "eFloat" in params, "Missing parameter 'eFloat'"
    assert "eInt" in params, "Missing parameter 'eInt'"
    assert "eDouble" in params, "Missing parameter 'eDouble'"
    assert "uris" in params, "Missing parameter 'uris'"
    assert "eDate" in params, "Missing parameter 'eDate'"
    assert "eByte" in params, "Missing parameter 'eByte'"
    assert "eString" in params, "Missing parameter 'eString'"
    assert "eShort" in params, "Missing parameter 'eShort'"
    assert "eBigInteger" in params, "Missing parameter 'eBigInteger'"
    assert "eBoolean" in params, "Missing parameter 'eBoolean'"
    assert "eChar" in params, "Missing parameter 'eChar'"
    assert "eBigDecimal" in params, "Missing parameter 'eBigDecimal'"

def test_model_etypes_has_eLong():
    assert hasattr(model_ETypes, "eLong")
    descriptor = None
    for klass in model_ETypes.__mro__:
        if "eLong" in klass.__dict__:
            descriptor = klass.__dict__["eLong"]
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

def test_model_etypes_has_eFloat():
    assert hasattr(model_ETypes, "eFloat")
    descriptor = None
    for klass in model_ETypes.__mro__:
        if "eFloat" in klass.__dict__:
            descriptor = klass.__dict__["eFloat"]
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

def test_model_etypes_has_eDouble():
    assert hasattr(model_ETypes, "eDouble")
    descriptor = None
    for klass in model_ETypes.__mro__:
        if "eDouble" in klass.__dict__:
            descriptor = klass.__dict__["eDouble"]
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

def test_model_etypes_has_eDate():
    assert hasattr(model_ETypes, "eDate")
    descriptor = None
    for klass in model_ETypes.__mro__:
        if "eDate" in klass.__dict__:
            descriptor = klass.__dict__["eDate"]
            break
    assert isinstance(descriptor, property)

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

def test_model_etypes_has_eShort():
    assert hasattr(model_ETypes, "eShort")
    descriptor = None
    for klass in model_ETypes.__mro__:
        if "eShort" in klass.__dict__:
            descriptor = klass.__dict__["eShort"]
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

def test_model_etypes_has_eBoolean():
    assert hasattr(model_ETypes, "eBoolean")
    descriptor = None
    for klass in model_ETypes.__mro__:
        if "eBoolean" in klass.__dict__:
            descriptor = klass.__dict__["eBoolean"]
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

def test_model_etypes_has_eBigDecimal():
    assert hasattr(model_ETypes, "eBigDecimal")
    descriptor = None
    for klass in model_ETypes.__mro__:
        if "eBigDecimal" in klass.__dict__:
            descriptor = klass.__dict__["eBigDecimal"]
            break
    assert isinstance(descriptor, property)


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
model_TargetObject_strategy = st.builds(
    model_TargetObject,
    arrayAttribute=
        safe_text,
    singleAttribute=
        safe_text
)
model_PrimaryObject_strategy = st.builds(
    model_PrimaryObject,
    name=
        safe_text,
    featureMapReferenceCollection=
        safe_text,
    featureMapAttributeType1=
        safe_text,
    featureMapAttributeType2=
        safe_text,
    featureMapAttributeCollection=
        safe_text
)
model_MappedLibrary_strategy = st.builds(
    model_MappedLibrary,
    books=
        safe_text
)
model_Location_strategy = st.builds(
    model_Location,
    address=
        safe_text,
    id=
        safe_text
)
model_Library_strategy = st.builds(
    model_Library,
)
model_Book_strategy = st.builds(
    model_Book,
    data=
        safe_text,
    tags=
        safe_text,
    title=
        safe_text
)
model_Person_strategy = st.builds(
    model_Person,
    name=
        safe_text
)
model_ETypes_strategy = st.builds(
    model_ETypes,
    eLong=
        safe_text,
    eByteArray=
        safe_text,
    eFloat=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    eInt=
        st.integers(),
    eDouble=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    uris=
        safe_text,
    eDate=
        st.dates(),
    eByte=
        safe_text,
    eString=
        safe_text,
    eShort=
        safe_text,
    eBigInteger=
        safe_text,
    eBoolean=
        st.booleans(),
    eChar=
        safe_text,
    eBigDecimal=
        safe_text
)

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
def test_model_primaryobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=model_PrimaryObject_strategy)
def test_model_primaryobject_featureMapReferenceCollection_setter(instance):
    original = instance.featureMapReferenceCollection
    instance.featureMapReferenceCollection = original
    assert instance.featureMapReferenceCollection == original



@given(instance=model_PrimaryObject_strategy)
def test_model_primaryobject_featureMapAttributeType1_setter(instance):
    original = instance.featureMapAttributeType1
    instance.featureMapAttributeType1 = original
    assert instance.featureMapAttributeType1 == original



@given(instance=model_PrimaryObject_strategy)
def test_model_primaryobject_featureMapAttributeType2_setter(instance):
    original = instance.featureMapAttributeType2
    instance.featureMapAttributeType2 = original
    assert instance.featureMapAttributeType2 == original



@given(instance=model_PrimaryObject_strategy)
def test_model_primaryobject_featureMapAttributeCollection_setter(instance):
    original = instance.featureMapAttributeCollection
    instance.featureMapAttributeCollection = original
    assert instance.featureMapAttributeCollection == original

@given(instance=model_MappedLibrary_strategy)
@settings(max_examples=50)
def test_model_mappedlibrary_instantiation(instance):
    assert isinstance(instance, model_MappedLibrary)



@given(instance=model_MappedLibrary_strategy)
def test_model_mappedlibrary_books_setter(instance):
    original = instance.books
    instance.books = original
    assert instance.books == original

@given(instance=model_Location_strategy)
@settings(max_examples=50)
def test_model_location_instantiation(instance):
    assert isinstance(instance, model_Location)



@given(instance=model_Location_strategy)
def test_model_location_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=model_Location_strategy)
def test_model_location_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=model_Library_strategy)
@settings(max_examples=50)
def test_model_library_instantiation(instance):
    assert isinstance(instance, model_Library)

@given(instance=model_Book_strategy)
@settings(max_examples=50)
def test_model_book_instantiation(instance):
    assert isinstance(instance, model_Book)



@given(instance=model_Book_strategy)
def test_model_book_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original



@given(instance=model_Book_strategy)
def test_model_book_tags_setter(instance):
    original = instance.tags
    instance.tags = original
    assert instance.tags == original



@given(instance=model_Book_strategy)
def test_model_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=model_Person_strategy)
@settings(max_examples=50)
def test_model_person_instantiation(instance):
    assert isinstance(instance, model_Person)



@given(instance=model_Person_strategy)
def test_model_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model_ETypes_strategy)
@settings(max_examples=50)
def test_model_etypes_instantiation(instance):
    assert isinstance(instance, model_ETypes)



@given(instance=model_ETypes_strategy)
def test_model_etypes_eLong_setter(instance):
    original = instance.eLong
    instance.eLong = original
    assert instance.eLong == original



@given(instance=model_ETypes_strategy)
def test_model_etypes_eByteArray_setter(instance):
    original = instance.eByteArray
    instance.eByteArray = original
    assert instance.eByteArray == original



@given(instance=model_ETypes_strategy)
def test_model_etypes_eFloat_setter(instance):
    original = instance.eFloat
    instance.eFloat = original
    assert instance.eFloat == original



@given(instance=model_ETypes_strategy)
def test_model_etypes_eInt_setter(instance):
    original = instance.eInt
    instance.eInt = original
    assert instance.eInt == original



@given(instance=model_ETypes_strategy)
def test_model_etypes_eDouble_setter(instance):
    original = instance.eDouble
    instance.eDouble = original
    assert instance.eDouble == original



@given(instance=model_ETypes_strategy)
def test_model_etypes_uris_setter(instance):
    original = instance.uris
    instance.uris = original
    assert instance.uris == original



@given(instance=model_ETypes_strategy)
def test_model_etypes_eDate_setter(instance):
    original = instance.eDate
    instance.eDate = original
    assert instance.eDate == original



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
def test_model_etypes_eShort_setter(instance):
    original = instance.eShort
    instance.eShort = original
    assert instance.eShort == original



@given(instance=model_ETypes_strategy)
def test_model_etypes_eBigInteger_setter(instance):
    original = instance.eBigInteger
    instance.eBigInteger = original
    assert instance.eBigInteger == original



@given(instance=model_ETypes_strategy)
def test_model_etypes_eBoolean_setter(instance):
    original = instance.eBoolean
    instance.eBoolean = original
    assert instance.eBoolean == original



@given(instance=model_ETypes_strategy)
def test_model_etypes_eChar_setter(instance):
    original = instance.eChar
    instance.eChar = original
    assert instance.eChar == original



@given(instance=model_ETypes_strategy)
def test_model_etypes_eBigDecimal_setter(instance):
    original = instance.eBigDecimal
    instance.eBigDecimal = original
    assert instance.eBigDecimal == original
