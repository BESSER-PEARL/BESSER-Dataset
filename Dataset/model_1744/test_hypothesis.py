import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    model::TargetObject,
    model::PrimaryObject,
    model::MappedLibrary,
    model::Location,
    model::Library,
    model::Book,
    model::Person,
    model::ETypes,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model::targetobject_is_not_abstract():
    assert not inspect.isabstract(model::TargetObject)


def test_model::targetobject_constructor_exists():
    assert callable(model::TargetObject.__init__)


def test_model::targetobject_constructor_args():
    sig = inspect.signature(model::TargetObject.__init__)
    params = list(sig.parameters.keys())
    assert "singleAttribute" in params, "Missing parameter 'singleAttribute'"
    assert "arrayAttribute" in params, "Missing parameter 'arrayAttribute'"

def test_model::targetobject_has_singleAttribute():
    assert hasattr(model::TargetObject, "singleAttribute")
    descriptor = None
    for klass in model::TargetObject.__mro__:
        if "singleAttribute" in klass.__dict__:
            descriptor = klass.__dict__["singleAttribute"]
            break
    assert isinstance(descriptor, property)

def test_model::targetobject_has_arrayAttribute():
    assert hasattr(model::TargetObject, "arrayAttribute")
    descriptor = None
    for klass in model::TargetObject.__mro__:
        if "arrayAttribute" in klass.__dict__:
            descriptor = klass.__dict__["arrayAttribute"]
            break
    assert isinstance(descriptor, property)



def test_model::primaryobject_is_not_abstract():
    assert not inspect.isabstract(model::PrimaryObject)


def test_model::primaryobject_constructor_exists():
    assert callable(model::PrimaryObject.__init__)


def test_model::primaryobject_constructor_args():
    sig = inspect.signature(model::PrimaryObject.__init__)
    params = list(sig.parameters.keys())
    assert "featureMapAttributeCollection" in params, "Missing parameter 'featureMapAttributeCollection'"
    assert "featureMapAttributeType2" in params, "Missing parameter 'featureMapAttributeType2'"
    assert "featureMapReferenceCollection" in params, "Missing parameter 'featureMapReferenceCollection'"
    assert "name" in params, "Missing parameter 'name'"
    assert "featureMapAttributeType1" in params, "Missing parameter 'featureMapAttributeType1'"

def test_model::primaryobject_has_featureMapAttributeCollection():
    assert hasattr(model::PrimaryObject, "featureMapAttributeCollection")
    descriptor = None
    for klass in model::PrimaryObject.__mro__:
        if "featureMapAttributeCollection" in klass.__dict__:
            descriptor = klass.__dict__["featureMapAttributeCollection"]
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

def test_model::primaryobject_has_featureMapReferenceCollection():
    assert hasattr(model::PrimaryObject, "featureMapReferenceCollection")
    descriptor = None
    for klass in model::PrimaryObject.__mro__:
        if "featureMapReferenceCollection" in klass.__dict__:
            descriptor = klass.__dict__["featureMapReferenceCollection"]
            break
    assert isinstance(descriptor, property)

def test_model::primaryobject_has_name():
    assert hasattr(model::PrimaryObject, "name")
    descriptor = None
    for klass in model::PrimaryObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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



def test_model::mappedlibrary_is_not_abstract():
    assert not inspect.isabstract(model::MappedLibrary)


def test_model::mappedlibrary_constructor_exists():
    assert callable(model::MappedLibrary.__init__)


def test_model::mappedlibrary_constructor_args():
    sig = inspect.signature(model::MappedLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "books" in params, "Missing parameter 'books'"

def test_model::mappedlibrary_has_books():
    assert hasattr(model::MappedLibrary, "books")
    descriptor = None
    for klass in model::MappedLibrary.__mro__:
        if "books" in klass.__dict__:
            descriptor = klass.__dict__["books"]
            break
    assert isinstance(descriptor, property)



def test_model::location_is_not_abstract():
    assert not inspect.isabstract(model::Location)


def test_model::location_constructor_exists():
    assert callable(model::Location.__init__)


def test_model::location_constructor_args():
    sig = inspect.signature(model::Location.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "id" in params, "Missing parameter 'id'"

def test_model::location_has_address():
    assert hasattr(model::Location, "address")
    descriptor = None
    for klass in model::Location.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_model::location_has_id():
    assert hasattr(model::Location, "id")
    descriptor = None
    for klass in model::Location.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_model::library_is_not_abstract():
    assert not inspect.isabstract(model::Library)


def test_model::library_constructor_exists():
    assert callable(model::Library.__init__)


def test_model::library_constructor_args():
    sig = inspect.signature(model::Library.__init__)
    params = list(sig.parameters.keys())



def test_model::book_is_not_abstract():
    assert not inspect.isabstract(model::Book)


def test_model::book_constructor_exists():
    assert callable(model::Book.__init__)


def test_model::book_constructor_args():
    sig = inspect.signature(model::Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "tags" in params, "Missing parameter 'tags'"
    assert "data" in params, "Missing parameter 'data'"

def test_model::book_has_title():
    assert hasattr(model::Book, "title")
    descriptor = None
    for klass in model::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_model::book_has_tags():
    assert hasattr(model::Book, "tags")
    descriptor = None
    for klass in model::Book.__mro__:
        if "tags" in klass.__dict__:
            descriptor = klass.__dict__["tags"]
            break
    assert isinstance(descriptor, property)

def test_model::book_has_data():
    assert hasattr(model::Book, "data")
    descriptor = None
    for klass in model::Book.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)



def test_model::person_is_not_abstract():
    assert not inspect.isabstract(model::Person)


def test_model::person_constructor_exists():
    assert callable(model::Person.__init__)


def test_model::person_constructor_args():
    sig = inspect.signature(model::Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model::person_has_name():
    assert hasattr(model::Person, "name")
    descriptor = None
    for klass in model::Person.__mro__:
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
    assert "eBigInteger" in params, "Missing parameter 'eBigInteger'"
    assert "eByte" in params, "Missing parameter 'eByte'"
    assert "eString" in params, "Missing parameter 'eString'"
    assert "eDate" in params, "Missing parameter 'eDate'"
    assert "eBigDecimal" in params, "Missing parameter 'eBigDecimal'"
    assert "uris" in params, "Missing parameter 'uris'"
    assert "eLong" in params, "Missing parameter 'eLong'"
    assert "eShort" in params, "Missing parameter 'eShort'"
    assert "eFloat" in params, "Missing parameter 'eFloat'"
    assert "eInt" in params, "Missing parameter 'eInt'"
    assert "eByteArray" in params, "Missing parameter 'eByteArray'"
    assert "eDouble" in params, "Missing parameter 'eDouble'"
    assert "eChar" in params, "Missing parameter 'eChar'"
    assert "eBoolean" in params, "Missing parameter 'eBoolean'"

def test_model::etypes_has_eBigInteger():
    assert hasattr(model::ETypes, "eBigInteger")
    descriptor = None
    for klass in model::ETypes.__mro__:
        if "eBigInteger" in klass.__dict__:
            descriptor = klass.__dict__["eBigInteger"]
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

def test_model::etypes_has_eString():
    assert hasattr(model::ETypes, "eString")
    descriptor = None
    for klass in model::ETypes.__mro__:
        if "eString" in klass.__dict__:
            descriptor = klass.__dict__["eString"]
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

def test_model::etypes_has_eBigDecimal():
    assert hasattr(model::ETypes, "eBigDecimal")
    descriptor = None
    for klass in model::ETypes.__mro__:
        if "eBigDecimal" in klass.__dict__:
            descriptor = klass.__dict__["eBigDecimal"]
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

def test_model::etypes_has_eLong():
    assert hasattr(model::ETypes, "eLong")
    descriptor = None
    for klass in model::ETypes.__mro__:
        if "eLong" in klass.__dict__:
            descriptor = klass.__dict__["eLong"]
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

def test_model::etypes_has_eFloat():
    assert hasattr(model::ETypes, "eFloat")
    descriptor = None
    for klass in model::ETypes.__mro__:
        if "eFloat" in klass.__dict__:
            descriptor = klass.__dict__["eFloat"]
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

def test_model::etypes_has_eByteArray():
    assert hasattr(model::ETypes, "eByteArray")
    descriptor = None
    for klass in model::ETypes.__mro__:
        if "eByteArray" in klass.__dict__:
            descriptor = klass.__dict__["eByteArray"]
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

def test_model::etypes_has_eChar():
    assert hasattr(model::ETypes, "eChar")
    descriptor = None
    for klass in model::ETypes.__mro__:
        if "eChar" in klass.__dict__:
            descriptor = klass.__dict__["eChar"]
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
model::TargetObject_strategy = st.builds(
    model::TargetObject,
    singleAttribute=
        safe_text,
    arrayAttribute=
        safe_text
)
model::PrimaryObject_strategy = st.builds(
    model::PrimaryObject,
    featureMapAttributeCollection=
        safe_text,
    featureMapAttributeType2=
        safe_text,
    featureMapReferenceCollection=
        safe_text,
    name=
        safe_text,
    featureMapAttributeType1=
        safe_text
)
model::MappedLibrary_strategy = st.builds(
    model::MappedLibrary,
    books=
        safe_text
)
model::Location_strategy = st.builds(
    model::Location,
    address=
        safe_text,
    id=
        safe_text
)
model::Library_strategy = st.builds(
    model::Library,
)
model::Book_strategy = st.builds(
    model::Book,
    title=
        safe_text,
    tags=
        safe_text,
    data=
        safe_text
)
model::Person_strategy = st.builds(
    model::Person,
    name=
        safe_text
)
model::ETypes_strategy = st.builds(
    model::ETypes,
    eBigInteger=
        safe_text,
    eByte=
        safe_text,
    eString=
        safe_text,
    eDate=
        st.dates(),
    eBigDecimal=
        safe_text,
    uris=
        safe_text,
    eLong=
        safe_text,
    eShort=
        safe_text,
    eFloat=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    eInt=
        st.integers(),
    eByteArray=
        safe_text,
    eDouble=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    eChar=
        safe_text,
    eBoolean=
        st.booleans()
)

@given(instance=model::TargetObject_strategy)
@settings(max_examples=50)
def test_model::targetobject_instantiation(instance):
    assert isinstance(instance, model::TargetObject)

@given(instance=model::TargetObject_strategy)
def test_model::targetobject_singleAttribute_type(instance):
    assert isinstance(instance.singleAttribute, str)


@given(instance=model::TargetObject_strategy)
def test_model::targetobject_singleAttribute_setter(instance):
    original = instance.singleAttribute
    instance.singleAttribute = original
    assert instance.singleAttribute == original

@given(instance=model::TargetObject_strategy)
def test_model::targetobject_arrayAttribute_type(instance):
    assert isinstance(instance.arrayAttribute, str)


@given(instance=model::TargetObject_strategy)
def test_model::targetobject_arrayAttribute_setter(instance):
    original = instance.arrayAttribute
    instance.arrayAttribute = original
    assert instance.arrayAttribute == original

@given(instance=model::PrimaryObject_strategy)
@settings(max_examples=50)
def test_model::primaryobject_instantiation(instance):
    assert isinstance(instance, model::PrimaryObject)

@given(instance=model::PrimaryObject_strategy)
def test_model::primaryobject_featureMapAttributeCollection_type(instance):
    assert isinstance(instance.featureMapAttributeCollection, str)


@given(instance=model::PrimaryObject_strategy)
def test_model::primaryobject_featureMapAttributeCollection_setter(instance):
    original = instance.featureMapAttributeCollection
    instance.featureMapAttributeCollection = original
    assert instance.featureMapAttributeCollection == original

@given(instance=model::PrimaryObject_strategy)
def test_model::primaryobject_featureMapAttributeType2_type(instance):
    assert isinstance(instance.featureMapAttributeType2, str)


@given(instance=model::PrimaryObject_strategy)
def test_model::primaryobject_featureMapAttributeType2_setter(instance):
    original = instance.featureMapAttributeType2
    instance.featureMapAttributeType2 = original
    assert instance.featureMapAttributeType2 == original

@given(instance=model::PrimaryObject_strategy)
def test_model::primaryobject_featureMapReferenceCollection_type(instance):
    assert isinstance(instance.featureMapReferenceCollection, str)


@given(instance=model::PrimaryObject_strategy)
def test_model::primaryobject_featureMapReferenceCollection_setter(instance):
    original = instance.featureMapReferenceCollection
    instance.featureMapReferenceCollection = original
    assert instance.featureMapReferenceCollection == original

@given(instance=model::PrimaryObject_strategy)
def test_model::primaryobject_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::PrimaryObject_strategy)
def test_model::primaryobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::PrimaryObject_strategy)
def test_model::primaryobject_featureMapAttributeType1_type(instance):
    assert isinstance(instance.featureMapAttributeType1, str)


@given(instance=model::PrimaryObject_strategy)
def test_model::primaryobject_featureMapAttributeType1_setter(instance):
    original = instance.featureMapAttributeType1
    instance.featureMapAttributeType1 = original
    assert instance.featureMapAttributeType1 == original

@given(instance=model::MappedLibrary_strategy)
@settings(max_examples=50)
def test_model::mappedlibrary_instantiation(instance):
    assert isinstance(instance, model::MappedLibrary)

@given(instance=model::MappedLibrary_strategy)
def test_model::mappedlibrary_books_type(instance):
    assert isinstance(instance.books, str)


@given(instance=model::MappedLibrary_strategy)
def test_model::mappedlibrary_books_setter(instance):
    original = instance.books
    instance.books = original
    assert instance.books == original

@given(instance=model::Location_strategy)
@settings(max_examples=50)
def test_model::location_instantiation(instance):
    assert isinstance(instance, model::Location)

@given(instance=model::Location_strategy)
def test_model::location_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=model::Location_strategy)
def test_model::location_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=model::Location_strategy)
def test_model::location_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=model::Location_strategy)
def test_model::location_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=model::Library_strategy)
@settings(max_examples=50)
def test_model::library_instantiation(instance):
    assert isinstance(instance, model::Library)

@given(instance=model::Book_strategy)
@settings(max_examples=50)
def test_model::book_instantiation(instance):
    assert isinstance(instance, model::Book)

@given(instance=model::Book_strategy)
def test_model::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=model::Book_strategy)
def test_model::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=model::Book_strategy)
def test_model::book_tags_type(instance):
    assert isinstance(instance.tags, str)


@given(instance=model::Book_strategy)
def test_model::book_tags_setter(instance):
    original = instance.tags
    instance.tags = original
    assert instance.tags == original

@given(instance=model::Book_strategy)
def test_model::book_data_type(instance):
    assert isinstance(instance.data, str)


@given(instance=model::Book_strategy)
def test_model::book_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=model::Person_strategy)
@settings(max_examples=50)
def test_model::person_instantiation(instance):
    assert isinstance(instance, model::Person)

@given(instance=model::Person_strategy)
def test_model::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::Person_strategy)
def test_model::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::ETypes_strategy)
@settings(max_examples=50)
def test_model::etypes_instantiation(instance):
    assert isinstance(instance, model::ETypes)

@given(instance=model::ETypes_strategy)
def test_model::etypes_eBigInteger_type(instance):
    assert isinstance(instance.eBigInteger, str)


@given(instance=model::ETypes_strategy)
def test_model::etypes_eBigInteger_setter(instance):
    original = instance.eBigInteger
    instance.eBigInteger = original
    assert instance.eBigInteger == original

@given(instance=model::ETypes_strategy)
def test_model::etypes_eByte_type(instance):
    assert isinstance(instance.eByte, str)


@given(instance=model::ETypes_strategy)
def test_model::etypes_eByte_setter(instance):
    original = instance.eByte
    instance.eByte = original
    assert instance.eByte == original

@given(instance=model::ETypes_strategy)
def test_model::etypes_eString_type(instance):
    assert isinstance(instance.eString, str)


@given(instance=model::ETypes_strategy)
def test_model::etypes_eString_setter(instance):
    original = instance.eString
    instance.eString = original
    assert instance.eString == original

@given(instance=model::ETypes_strategy)
def test_model::etypes_eDate_type(instance):
    assert isinstance(instance.eDate, date)


@given(instance=model::ETypes_strategy)
def test_model::etypes_eDate_setter(instance):
    original = instance.eDate
    instance.eDate = original
    assert instance.eDate == original

@given(instance=model::ETypes_strategy)
def test_model::etypes_eBigDecimal_type(instance):
    assert isinstance(instance.eBigDecimal, str)


@given(instance=model::ETypes_strategy)
def test_model::etypes_eBigDecimal_setter(instance):
    original = instance.eBigDecimal
    instance.eBigDecimal = original
    assert instance.eBigDecimal == original

@given(instance=model::ETypes_strategy)
def test_model::etypes_uris_type(instance):
    assert isinstance(instance.uris, str)


@given(instance=model::ETypes_strategy)
def test_model::etypes_uris_setter(instance):
    original = instance.uris
    instance.uris = original
    assert instance.uris == original

@given(instance=model::ETypes_strategy)
def test_model::etypes_eLong_type(instance):
    assert isinstance(instance.eLong, str)


@given(instance=model::ETypes_strategy)
def test_model::etypes_eLong_setter(instance):
    original = instance.eLong
    instance.eLong = original
    assert instance.eLong == original

@given(instance=model::ETypes_strategy)
def test_model::etypes_eShort_type(instance):
    assert isinstance(instance.eShort, str)


@given(instance=model::ETypes_strategy)
def test_model::etypes_eShort_setter(instance):
    original = instance.eShort
    instance.eShort = original
    assert instance.eShort == original

@given(instance=model::ETypes_strategy)
def test_model::etypes_eFloat_type(instance):
    assert isinstance(instance.eFloat, float)


@given(instance=model::ETypes_strategy)
def test_model::etypes_eFloat_setter(instance):
    original = instance.eFloat
    instance.eFloat = original
    assert instance.eFloat == original

@given(instance=model::ETypes_strategy)
def test_model::etypes_eInt_type(instance):
    assert isinstance(instance.eInt, int)


@given(instance=model::ETypes_strategy)
def test_model::etypes_eInt_setter(instance):
    original = instance.eInt
    instance.eInt = original
    assert instance.eInt == original

@given(instance=model::ETypes_strategy)
def test_model::etypes_eByteArray_type(instance):
    assert isinstance(instance.eByteArray, str)


@given(instance=model::ETypes_strategy)
def test_model::etypes_eByteArray_setter(instance):
    original = instance.eByteArray
    instance.eByteArray = original
    assert instance.eByteArray == original

@given(instance=model::ETypes_strategy)
def test_model::etypes_eDouble_type(instance):
    assert isinstance(instance.eDouble, float)


@given(instance=model::ETypes_strategy)
def test_model::etypes_eDouble_setter(instance):
    original = instance.eDouble
    instance.eDouble = original
    assert instance.eDouble == original

@given(instance=model::ETypes_strategy)
def test_model::etypes_eChar_type(instance):
    assert isinstance(instance.eChar, str)


@given(instance=model::ETypes_strategy)
def test_model::etypes_eChar_setter(instance):
    original = instance.eChar
    instance.eChar = original
    assert instance.eChar == original

@given(instance=model::ETypes_strategy)
def test_model::etypes_eBoolean_type(instance):
    assert isinstance(instance.eBoolean, bool)


@given(instance=model::ETypes_strategy)
def test_model::etypes_eBoolean_setter(instance):
    original = instance.eBoolean
    instance.eBoolean = original
    assert instance.eBoolean == original
