import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sunBooks_EStringToStringMapEntry,
    sunBooks_DocumentRoot,
    sunBooks_PromotionType,
    sunBooks_BookType,
    sunBooks_CollectionType,
    sunBooks_AuthorsType,
    sunBooks_BooksType,
    BookCategoryType,
    BookCategoryType1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sunbooks_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(sunBooks_EStringToStringMapEntry)


def test_sunbooks_estringtostringmapentry_constructor_exists():
    assert callable(sunBooks_EStringToStringMapEntry.__init__)


def test_sunbooks_estringtostringmapentry_constructor_args():
    sig = inspect.signature(sunBooks_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_sunbooks_documentroot_is_not_abstract():
    assert not inspect.isabstract(sunBooks_DocumentRoot)


def test_sunbooks_documentroot_constructor_exists():
    assert callable(sunBooks_DocumentRoot.__init__)


def test_sunbooks_documentroot_constructor_args():
    sig = inspect.signature(sunBooks_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_sunbooks_documentroot_has_mixed():
    assert hasattr(sunBooks_DocumentRoot, "mixed")
    descriptor = None
    for klass in sunBooks_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_sunbooks_promotiontype_is_not_abstract():
    assert not inspect.isabstract(sunBooks_PromotionType)


def test_sunbooks_promotiontype_constructor_exists():
    assert callable(sunBooks_PromotionType.__init__)


def test_sunbooks_promotiontype_constructor_args():
    sig = inspect.signature(sunBooks_PromotionType.__init__)
    params = list(sig.parameters.keys())
    assert "discount" in params, "Missing parameter 'discount'"
    assert "none" in params, "Missing parameter 'none'"

def test_sunbooks_promotiontype_has_discount():
    assert hasattr(sunBooks_PromotionType, "discount")
    descriptor = None
    for klass in sunBooks_PromotionType.__mro__:
        if "discount" in klass.__dict__:
            descriptor = klass.__dict__["discount"]
            break
    assert isinstance(descriptor, property)

def test_sunbooks_promotiontype_has_none():
    assert hasattr(sunBooks_PromotionType, "none")
    descriptor = None
    for klass in sunBooks_PromotionType.__mro__:
        if "none" in klass.__dict__:
            descriptor = klass.__dict__["none"]
            break
    assert isinstance(descriptor, property)



def test_sunbooks_booktype_is_not_abstract():
    assert not inspect.isabstract(sunBooks_BookType)


def test_sunbooks_booktype_constructor_exists():
    assert callable(sunBooks_BookType.__init__)


def test_sunbooks_booktype_constructor_args():
    sig = inspect.signature(sunBooks_BookType.__init__)
    params = list(sig.parameters.keys())
    assert "publicationDate" in params, "Missing parameter 'publicationDate'"
    assert "name" in params, "Missing parameter 'name'"
    assert "iSBN" in params, "Missing parameter 'iSBN'"
    assert "itemId" in params, "Missing parameter 'itemId'"
    assert "bookCategory" in params, "Missing parameter 'bookCategory'"
    assert "price" in params, "Missing parameter 'price'"
    assert "description" in params, "Missing parameter 'description'"

def test_sunbooks_booktype_has_publicationDate():
    assert hasattr(sunBooks_BookType, "publicationDate")
    descriptor = None
    for klass in sunBooks_BookType.__mro__:
        if "publicationDate" in klass.__dict__:
            descriptor = klass.__dict__["publicationDate"]
            break
    assert isinstance(descriptor, property)

def test_sunbooks_booktype_has_name():
    assert hasattr(sunBooks_BookType, "name")
    descriptor = None
    for klass in sunBooks_BookType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sunbooks_booktype_has_iSBN():
    assert hasattr(sunBooks_BookType, "iSBN")
    descriptor = None
    for klass in sunBooks_BookType.__mro__:
        if "iSBN" in klass.__dict__:
            descriptor = klass.__dict__["iSBN"]
            break
    assert isinstance(descriptor, property)

def test_sunbooks_booktype_has_itemId():
    assert hasattr(sunBooks_BookType, "itemId")
    descriptor = None
    for klass in sunBooks_BookType.__mro__:
        if "itemId" in klass.__dict__:
            descriptor = klass.__dict__["itemId"]
            break
    assert isinstance(descriptor, property)

def test_sunbooks_booktype_has_bookCategory():
    assert hasattr(sunBooks_BookType, "bookCategory")
    descriptor = None
    for klass in sunBooks_BookType.__mro__:
        if "bookCategory" in klass.__dict__:
            descriptor = klass.__dict__["bookCategory"]
            break
    assert isinstance(descriptor, property)

def test_sunbooks_booktype_has_price():
    assert hasattr(sunBooks_BookType, "price")
    descriptor = None
    for klass in sunBooks_BookType.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_sunbooks_booktype_has_description():
    assert hasattr(sunBooks_BookType, "description")
    descriptor = None
    for klass in sunBooks_BookType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_sunbooks_collectiontype_is_not_abstract():
    assert not inspect.isabstract(sunBooks_CollectionType)


def test_sunbooks_collectiontype_constructor_exists():
    assert callable(sunBooks_CollectionType.__init__)


def test_sunbooks_collectiontype_constructor_args():
    sig = inspect.signature(sunBooks_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_sunbooks_authorstype_is_not_abstract():
    assert not inspect.isabstract(sunBooks_AuthorsType)


def test_sunbooks_authorstype_constructor_exists():
    assert callable(sunBooks_AuthorsType.__init__)


def test_sunbooks_authorstype_constructor_args():
    sig = inspect.signature(sunBooks_AuthorsType.__init__)
    params = list(sig.parameters.keys())
    assert "authorName" in params, "Missing parameter 'authorName'"

def test_sunbooks_authorstype_has_authorName():
    assert hasattr(sunBooks_AuthorsType, "authorName")
    descriptor = None
    for klass in sunBooks_AuthorsType.__mro__:
        if "authorName" in klass.__dict__:
            descriptor = klass.__dict__["authorName"]
            break
    assert isinstance(descriptor, property)



def test_sunbooks_bookstype_is_not_abstract():
    assert not inspect.isabstract(sunBooks_BooksType)


def test_sunbooks_bookstype_constructor_exists():
    assert callable(sunBooks_BooksType.__init__)


def test_sunbooks_bookstype_constructor_args():
    sig = inspect.signature(sunBooks_BooksType.__init__)
    params = list(sig.parameters.keys())

def test_bookcategorytype_exists():
    # Check that the Enumeration exists
    assert BookCategoryType is not None

def test_bookcategorytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BookCategoryType]
    expected_literals = [
        "other",
        "fiction",
        "novel",
        "magazine",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BookCategoryType"

def test_bookcategorytype1_exists():
    # Check that the Enumeration exists
    assert BookCategoryType1 is not None

def test_bookcategorytype1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BookCategoryType1]
    expected_literals = [
        "novel",
        "fiction",
        "other",
        "magazine",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BookCategoryType1"


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
sunBooks_EStringToStringMapEntry_strategy = st.builds(
    sunBooks_EStringToStringMapEntry,
)
sunBooks_DocumentRoot_strategy = st.builds(
    sunBooks_DocumentRoot,
    mixed=
        safe_text
)
sunBooks_PromotionType_strategy = st.builds(
    sunBooks_PromotionType,
    discount=
        safe_text,
    none=
        safe_text
)
sunBooks_BookType_strategy = st.builds(
    sunBooks_BookType,
    publicationDate=
        safe_text,
    name=
        safe_text,
    iSBN=
        safe_text,
    itemId=
        safe_text,
    bookCategory=
        safe_text,
    price=
        safe_text,
    description=
        safe_text
)
sunBooks_CollectionType_strategy = st.builds(
    sunBooks_CollectionType,
)
sunBooks_AuthorsType_strategy = st.builds(
    sunBooks_AuthorsType,
    authorName=
        safe_text
)
sunBooks_BooksType_strategy = st.builds(
    sunBooks_BooksType,
)

@given(instance=sunBooks_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_sunbooks_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, sunBooks_EStringToStringMapEntry)

@given(instance=sunBooks_DocumentRoot_strategy)
@settings(max_examples=50)
def test_sunbooks_documentroot_instantiation(instance):
    assert isinstance(instance, sunBooks_DocumentRoot)



@given(instance=sunBooks_DocumentRoot_strategy)
def test_sunbooks_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=sunBooks_PromotionType_strategy)
@settings(max_examples=50)
def test_sunbooks_promotiontype_instantiation(instance):
    assert isinstance(instance, sunBooks_PromotionType)



@given(instance=sunBooks_PromotionType_strategy)
def test_sunbooks_promotiontype_discount_setter(instance):
    original = instance.discount
    instance.discount = original
    assert instance.discount == original



@given(instance=sunBooks_PromotionType_strategy)
def test_sunbooks_promotiontype_none_setter(instance):
    original = instance.none
    instance.none = original
    assert instance.none == original

@given(instance=sunBooks_BookType_strategy)
@settings(max_examples=50)
def test_sunbooks_booktype_instantiation(instance):
    assert isinstance(instance, sunBooks_BookType)



@given(instance=sunBooks_BookType_strategy)
def test_sunbooks_booktype_publicationDate_setter(instance):
    original = instance.publicationDate
    instance.publicationDate = original
    assert instance.publicationDate == original



@given(instance=sunBooks_BookType_strategy)
def test_sunbooks_booktype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=sunBooks_BookType_strategy)
def test_sunbooks_booktype_iSBN_setter(instance):
    original = instance.iSBN
    instance.iSBN = original
    assert instance.iSBN == original



@given(instance=sunBooks_BookType_strategy)
def test_sunbooks_booktype_itemId_setter(instance):
    original = instance.itemId
    instance.itemId = original
    assert instance.itemId == original



@given(instance=sunBooks_BookType_strategy)
def test_sunbooks_booktype_bookCategory_setter(instance):
    original = instance.bookCategory
    instance.bookCategory = original
    assert instance.bookCategory == original



@given(instance=sunBooks_BookType_strategy)
def test_sunbooks_booktype_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=sunBooks_BookType_strategy)
def test_sunbooks_booktype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=sunBooks_CollectionType_strategy)
@settings(max_examples=50)
def test_sunbooks_collectiontype_instantiation(instance):
    assert isinstance(instance, sunBooks_CollectionType)

@given(instance=sunBooks_AuthorsType_strategy)
@settings(max_examples=50)
def test_sunbooks_authorstype_instantiation(instance):
    assert isinstance(instance, sunBooks_AuthorsType)



@given(instance=sunBooks_AuthorsType_strategy)
def test_sunbooks_authorstype_authorName_setter(instance):
    original = instance.authorName
    instance.authorName = original
    assert instance.authorName == original

@given(instance=sunBooks_BooksType_strategy)
@settings(max_examples=50)
def test_sunbooks_bookstype_instantiation(instance):
    assert isinstance(instance, sunBooks_BooksType)
