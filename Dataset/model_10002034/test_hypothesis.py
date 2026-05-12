import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ShoppingCart,
    Category,
    AdvSearch,
    Search,
    BookSet,
    Administrator,
    Book,
    BooksOrder,
    Customer,
    SessionManager,
    User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_shoppingcart_is_not_abstract():
    assert not inspect.isabstract(ShoppingCart)


def test_shoppingcart_constructor_exists():
    assert callable(ShoppingCart.__init__)


def test_shoppingcart_constructor_args():
    sig = inspect.signature(ShoppingCart.__init__)
    params = list(sig.parameters.keys())
    assert "customerID" in params, "Missing parameter 'customerID'"
    assert "price" in params, "Missing parameter 'price'"
    assert "orderID" in params, "Missing parameter 'orderID'"

def test_shoppingcart_has_customerID():
    assert hasattr(ShoppingCart, "customerID")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "customerID" in klass.__dict__:
            descriptor = klass.__dict__["customerID"]
            break
    assert isinstance(descriptor, property)

def test_shoppingcart_has_price():
    assert hasattr(ShoppingCart, "price")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_shoppingcart_has_orderID():
    assert hasattr(ShoppingCart, "orderID")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "orderID" in klass.__dict__:
            descriptor = klass.__dict__["orderID"]
            break
    assert isinstance(descriptor, property)



def test_category_is_not_abstract():
    assert not inspect.isabstract(Category)


def test_category_constructor_exists():
    assert callable(Category.__init__)


def test_category_constructor_args():
    sig = inspect.signature(Category.__init__)
    params = list(sig.parameters.keys())
    assert "categoryID" in params, "Missing parameter 'categoryID'"
    assert "categoryName" in params, "Missing parameter 'categoryName'"

def test_category_has_categoryID():
    assert hasattr(Category, "categoryID")
    descriptor = None
    for klass in Category.__mro__:
        if "categoryID" in klass.__dict__:
            descriptor = klass.__dict__["categoryID"]
            break
    assert isinstance(descriptor, property)

def test_category_has_categoryName():
    assert hasattr(Category, "categoryName")
    descriptor = None
    for klass in Category.__mro__:
        if "categoryName" in klass.__dict__:
            descriptor = klass.__dict__["categoryName"]
            break
    assert isinstance(descriptor, property)



def test_advsearch_is_not_abstract():
    assert not inspect.isabstract(AdvSearch)


def test_advsearch_constructor_exists():
    assert callable(AdvSearch.__init__)


def test_advsearch_constructor_args():
    sig = inspect.signature(AdvSearch.__init__)
    params = list(sig.parameters.keys())
    assert "bookHighCost" in params, "Missing parameter 'bookHighCost'"
    assert "bookLowCost" in params, "Missing parameter 'bookLowCost'"
    assert "categoryID" in params, "Missing parameter 'categoryID'"
    assert "bookTitle" in params, "Missing parameter 'bookTitle'"
    assert "bookAuthor" in params, "Missing parameter 'bookAuthor'"

def test_advsearch_has_bookHighCost():
    assert hasattr(AdvSearch, "bookHighCost")
    descriptor = None
    for klass in AdvSearch.__mro__:
        if "bookHighCost" in klass.__dict__:
            descriptor = klass.__dict__["bookHighCost"]
            break
    assert isinstance(descriptor, property)

def test_advsearch_has_bookLowCost():
    assert hasattr(AdvSearch, "bookLowCost")
    descriptor = None
    for klass in AdvSearch.__mro__:
        if "bookLowCost" in klass.__dict__:
            descriptor = klass.__dict__["bookLowCost"]
            break
    assert isinstance(descriptor, property)

def test_advsearch_has_categoryID():
    assert hasattr(AdvSearch, "categoryID")
    descriptor = None
    for klass in AdvSearch.__mro__:
        if "categoryID" in klass.__dict__:
            descriptor = klass.__dict__["categoryID"]
            break
    assert isinstance(descriptor, property)

def test_advsearch_has_bookTitle():
    assert hasattr(AdvSearch, "bookTitle")
    descriptor = None
    for klass in AdvSearch.__mro__:
        if "bookTitle" in klass.__dict__:
            descriptor = klass.__dict__["bookTitle"]
            break
    assert isinstance(descriptor, property)

def test_advsearch_has_bookAuthor():
    assert hasattr(AdvSearch, "bookAuthor")
    descriptor = None
    for klass in AdvSearch.__mro__:
        if "bookAuthor" in klass.__dict__:
            descriptor = klass.__dict__["bookAuthor"]
            break
    assert isinstance(descriptor, property)



def test_search_is_not_abstract():
    assert not inspect.isabstract(Search)


def test_search_constructor_exists():
    assert callable(Search.__init__)


def test_search_constructor_args():
    sig = inspect.signature(Search.__init__)
    params = list(sig.parameters.keys())
    assert "bookTitle" in params, "Missing parameter 'bookTitle'"
    assert "categoryID" in params, "Missing parameter 'categoryID'"

def test_search_has_bookTitle():
    assert hasattr(Search, "bookTitle")
    descriptor = None
    for klass in Search.__mro__:
        if "bookTitle" in klass.__dict__:
            descriptor = klass.__dict__["bookTitle"]
            break
    assert isinstance(descriptor, property)

def test_search_has_categoryID():
    assert hasattr(Search, "categoryID")
    descriptor = None
    for klass in Search.__mro__:
        if "categoryID" in klass.__dict__:
            descriptor = klass.__dict__["categoryID"]
            break
    assert isinstance(descriptor, property)



def test_bookset_is_not_abstract():
    assert not inspect.isabstract(BookSet)


def test_bookset_constructor_exists():
    assert callable(BookSet.__init__)


def test_bookset_constructor_args():
    sig = inspect.signature(BookSet.__init__)
    params = list(sig.parameters.keys())
    assert "bookName" in params, "Missing parameter 'bookName'"
    assert "bookID" in params, "Missing parameter 'bookID'"

def test_bookset_has_bookName():
    assert hasattr(BookSet, "bookName")
    descriptor = None
    for klass in BookSet.__mro__:
        if "bookName" in klass.__dict__:
            descriptor = klass.__dict__["bookName"]
            break
    assert isinstance(descriptor, property)

def test_bookset_has_bookID():
    assert hasattr(BookSet, "bookID")
    descriptor = None
    for klass in BookSet.__mro__:
        if "bookID" in klass.__dict__:
            descriptor = klass.__dict__["bookID"]
            break
    assert isinstance(descriptor, property)



def test_administrator_is_not_abstract():
    assert not inspect.isabstract(Administrator)


def test_administrator_constructor_exists():
    assert callable(Administrator.__init__)


def test_administrator_constructor_args():
    sig = inspect.signature(Administrator.__init__)
    params = list(sig.parameters.keys())
    assert "adminID" in params, "Missing parameter 'adminID'"
    assert "email" in params, "Missing parameter 'email'"
    assert "phoneNo" in params, "Missing parameter 'phoneNo'"
    assert "name" in params, "Missing parameter 'name'"
    assert "password" in params, "Missing parameter 'password'"

def test_administrator_has_adminID():
    assert hasattr(Administrator, "adminID")
    descriptor = None
    for klass in Administrator.__mro__:
        if "adminID" in klass.__dict__:
            descriptor = klass.__dict__["adminID"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_email():
    assert hasattr(Administrator, "email")
    descriptor = None
    for klass in Administrator.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_phoneNo():
    assert hasattr(Administrator, "phoneNo")
    descriptor = None
    for klass in Administrator.__mro__:
        if "phoneNo" in klass.__dict__:
            descriptor = klass.__dict__["phoneNo"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_name():
    assert hasattr(Administrator, "name")
    descriptor = None
    for klass in Administrator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_password():
    assert hasattr(Administrator, "password")
    descriptor = None
    for klass in Administrator.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)



def test_book_is_not_abstract():
    assert not inspect.isabstract(Book)


def test_book_constructor_exists():
    assert callable(Book.__init__)


def test_book_constructor_args():
    sig = inspect.signature(Book.__init__)
    params = list(sig.parameters.keys())
    assert "authorName" in params, "Missing parameter 'authorName'"
    assert "price" in params, "Missing parameter 'price'"
    assert "imageURL" in params, "Missing parameter 'imageURL'"
    assert "bookName" in params, "Missing parameter 'bookName'"
    assert "bookID" in params, "Missing parameter 'bookID'"
    assert "categoryID" in params, "Missing parameter 'categoryID'"
    assert "productURL" in params, "Missing parameter 'productURL'"
    assert "notes" in params, "Missing parameter 'notes'"
    assert "rating" in params, "Missing parameter 'rating'"

def test_book_has_authorName():
    assert hasattr(Book, "authorName")
    descriptor = None
    for klass in Book.__mro__:
        if "authorName" in klass.__dict__:
            descriptor = klass.__dict__["authorName"]
            break
    assert isinstance(descriptor, property)

def test_book_has_price():
    assert hasattr(Book, "price")
    descriptor = None
    for klass in Book.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_book_has_imageURL():
    assert hasattr(Book, "imageURL")
    descriptor = None
    for klass in Book.__mro__:
        if "imageURL" in klass.__dict__:
            descriptor = klass.__dict__["imageURL"]
            break
    assert isinstance(descriptor, property)

def test_book_has_bookName():
    assert hasattr(Book, "bookName")
    descriptor = None
    for klass in Book.__mro__:
        if "bookName" in klass.__dict__:
            descriptor = klass.__dict__["bookName"]
            break
    assert isinstance(descriptor, property)

def test_book_has_bookID():
    assert hasattr(Book, "bookID")
    descriptor = None
    for klass in Book.__mro__:
        if "bookID" in klass.__dict__:
            descriptor = klass.__dict__["bookID"]
            break
    assert isinstance(descriptor, property)

def test_book_has_categoryID():
    assert hasattr(Book, "categoryID")
    descriptor = None
    for klass in Book.__mro__:
        if "categoryID" in klass.__dict__:
            descriptor = klass.__dict__["categoryID"]
            break
    assert isinstance(descriptor, property)

def test_book_has_productURL():
    assert hasattr(Book, "productURL")
    descriptor = None
    for klass in Book.__mro__:
        if "productURL" in klass.__dict__:
            descriptor = klass.__dict__["productURL"]
            break
    assert isinstance(descriptor, property)

def test_book_has_notes():
    assert hasattr(Book, "notes")
    descriptor = None
    for klass in Book.__mro__:
        if "notes" in klass.__dict__:
            descriptor = klass.__dict__["notes"]
            break
    assert isinstance(descriptor, property)

def test_book_has_rating():
    assert hasattr(Book, "rating")
    descriptor = None
    for klass in Book.__mro__:
        if "rating" in klass.__dict__:
            descriptor = klass.__dict__["rating"]
            break
    assert isinstance(descriptor, property)



def test_booksorder_is_not_abstract():
    assert not inspect.isabstract(BooksOrder)


def test_booksorder_constructor_exists():
    assert callable(BooksOrder.__init__)


def test_booksorder_constructor_args():
    sig = inspect.signature(BooksOrder.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "customerID" in params, "Missing parameter 'customerID'"
    assert "orderID" in params, "Missing parameter 'orderID'"

def test_booksorder_has_price():
    assert hasattr(BooksOrder, "price")
    descriptor = None
    for klass in BooksOrder.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_booksorder_has_quantity():
    assert hasattr(BooksOrder, "quantity")
    descriptor = None
    for klass in BooksOrder.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_booksorder_has_customerID():
    assert hasattr(BooksOrder, "customerID")
    descriptor = None
    for klass in BooksOrder.__mro__:
        if "customerID" in klass.__dict__:
            descriptor = klass.__dict__["customerID"]
            break
    assert isinstance(descriptor, property)

def test_booksorder_has_orderID():
    assert hasattr(BooksOrder, "orderID")
    descriptor = None
    for klass in BooksOrder.__mro__:
        if "orderID" in klass.__dict__:
            descriptor = klass.__dict__["orderID"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "phoneNo" in params, "Missing parameter 'phoneNo'"
    assert "name" in params, "Missing parameter 'name'"
    assert "CCinfo" in params, "Missing parameter 'CCinfo'"
    assert "customerID" in params, "Missing parameter 'customerID'"
    assert "address" in params, "Missing parameter 'address'"
    assert "password" in params, "Missing parameter 'password'"
    assert "email" in params, "Missing parameter 'email'"

def test_customer_has_phoneNo():
    assert hasattr(Customer, "phoneNo")
    descriptor = None
    for klass in Customer.__mro__:
        if "phoneNo" in klass.__dict__:
            descriptor = klass.__dict__["phoneNo"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_name():
    assert hasattr(Customer, "name")
    descriptor = None
    for klass in Customer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_CCinfo():
    assert hasattr(Customer, "CCinfo")
    descriptor = None
    for klass in Customer.__mro__:
        if "CCinfo" in klass.__dict__:
            descriptor = klass.__dict__["CCinfo"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_customerID():
    assert hasattr(Customer, "customerID")
    descriptor = None
    for klass in Customer.__mro__:
        if "customerID" in klass.__dict__:
            descriptor = klass.__dict__["customerID"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_address():
    assert hasattr(Customer, "address")
    descriptor = None
    for klass in Customer.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_password():
    assert hasattr(Customer, "password")
    descriptor = None
    for klass in Customer.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_email():
    assert hasattr(Customer, "email")
    descriptor = None
    for klass in Customer.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)



def test_sessionmanager_is_not_abstract():
    assert not inspect.isabstract(SessionManager)


def test_sessionmanager_constructor_exists():
    assert callable(SessionManager.__init__)


def test_sessionmanager_constructor_args():
    sig = inspect.signature(SessionManager.__init__)
    params = list(sig.parameters.keys())
    assert "userID" in params, "Missing parameter 'userID'"
    assert "categoryName" in params, "Missing parameter 'categoryName'"

def test_sessionmanager_has_userID():
    assert hasattr(SessionManager, "userID")
    descriptor = None
    for klass in SessionManager.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)

def test_sessionmanager_has_categoryName():
    assert hasattr(SessionManager, "categoryName")
    descriptor = None
    for klass in SessionManager.__mro__:
        if "categoryName" in klass.__dict__:
            descriptor = klass.__dict__["categoryName"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "loginStatus" in params, "Missing parameter 'loginStatus'"
    assert "userID" in params, "Missing parameter 'userID'"
    assert "password" in params, "Missing parameter 'password'"

def test_user_has_loginStatus():
    assert hasattr(User, "loginStatus")
    descriptor = None
    for klass in User.__mro__:
        if "loginStatus" in klass.__dict__:
            descriptor = klass.__dict__["loginStatus"]
            break
    assert isinstance(descriptor, property)

def test_user_has_userID():
    assert hasattr(User, "userID")
    descriptor = None
    for klass in User.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)

def test_user_has_password():
    assert hasattr(User, "password")
    descriptor = None
    for klass in User.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
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
ShoppingCart_strategy = st.builds(
    ShoppingCart,
    customerID=
        st.integers(),
    price=
        safe_text,
    orderID=
        st.integers()
)
Category_strategy = st.builds(
    Category,
    categoryID=
        st.integers(),
    categoryName=
        safe_text
)
AdvSearch_strategy = st.builds(
    AdvSearch,
    bookHighCost=
        safe_text,
    bookLowCost=
        safe_text,
    categoryID=
        safe_text,
    bookTitle=
        safe_text,
    bookAuthor=
        safe_text
)
Search_strategy = st.builds(
    Search,
    bookTitle=
        safe_text,
    categoryID=
        safe_text
)
BookSet_strategy = st.builds(
    BookSet,
    bookName=
        safe_text,
    bookID=
        st.integers()
)
Administrator_strategy = st.builds(
    Administrator,
    adminID=
        st.integers(),
    email=
        safe_text,
    phoneNo=
        safe_text,
    name=
        safe_text,
    password=
        safe_text
)
Book_strategy = st.builds(
    Book,
    authorName=
        safe_text,
    price=
        safe_text,
    imageURL=
        safe_text,
    bookName=
        safe_text,
    bookID=
        st.integers(),
    categoryID=
        st.integers(),
    productURL=
        safe_text,
    notes=
        safe_text,
    rating=
        st.integers()
)
BooksOrder_strategy = st.builds(
    BooksOrder,
    price=
        safe_text,
    quantity=
        st.integers(),
    customerID=
        st.integers(),
    orderID=
        st.integers()
)
Customer_strategy = st.builds(
    Customer,
    phoneNo=
        st.integers(),
    name=
        safe_text,
    CCinfo=
        safe_text,
    customerID=
        safe_text,
    address=
        safe_text,
    password=
        safe_text,
    email=
        safe_text
)
SessionManager_strategy = st.builds(
    SessionManager,
    userID=
        st.integers(),
    categoryName=
        safe_text
)
User_strategy = st.builds(
    User,
    loginStatus=
        safe_text,
    userID=
        st.integers(),
    password=
        safe_text
)

@given(instance=ShoppingCart_strategy)
@settings(max_examples=50)
def test_shoppingcart_instantiation(instance):
    assert isinstance(instance, ShoppingCart)



@given(instance=ShoppingCart_strategy)
def test_shoppingcart_customerID_setter(instance):
    original = instance.customerID
    instance.customerID = original
    assert instance.customerID == original



@given(instance=ShoppingCart_strategy)
def test_shoppingcart_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=ShoppingCart_strategy)
def test_shoppingcart_orderID_setter(instance):
    original = instance.orderID
    instance.orderID = original
    assert instance.orderID == original

@given(instance=Category_strategy)
@settings(max_examples=50)
def test_category_instantiation(instance):
    assert isinstance(instance, Category)



@given(instance=Category_strategy)
def test_category_categoryID_setter(instance):
    original = instance.categoryID
    instance.categoryID = original
    assert instance.categoryID == original



@given(instance=Category_strategy)
def test_category_categoryName_setter(instance):
    original = instance.categoryName
    instance.categoryName = original
    assert instance.categoryName == original

@given(instance=AdvSearch_strategy)
@settings(max_examples=50)
def test_advsearch_instantiation(instance):
    assert isinstance(instance, AdvSearch)



@given(instance=AdvSearch_strategy)
def test_advsearch_bookHighCost_setter(instance):
    original = instance.bookHighCost
    instance.bookHighCost = original
    assert instance.bookHighCost == original



@given(instance=AdvSearch_strategy)
def test_advsearch_bookLowCost_setter(instance):
    original = instance.bookLowCost
    instance.bookLowCost = original
    assert instance.bookLowCost == original



@given(instance=AdvSearch_strategy)
def test_advsearch_categoryID_setter(instance):
    original = instance.categoryID
    instance.categoryID = original
    assert instance.categoryID == original



@given(instance=AdvSearch_strategy)
def test_advsearch_bookTitle_setter(instance):
    original = instance.bookTitle
    instance.bookTitle = original
    assert instance.bookTitle == original



@given(instance=AdvSearch_strategy)
def test_advsearch_bookAuthor_setter(instance):
    original = instance.bookAuthor
    instance.bookAuthor = original
    assert instance.bookAuthor == original

@given(instance=Search_strategy)
@settings(max_examples=50)
def test_search_instantiation(instance):
    assert isinstance(instance, Search)



@given(instance=Search_strategy)
def test_search_bookTitle_setter(instance):
    original = instance.bookTitle
    instance.bookTitle = original
    assert instance.bookTitle == original



@given(instance=Search_strategy)
def test_search_categoryID_setter(instance):
    original = instance.categoryID
    instance.categoryID = original
    assert instance.categoryID == original

@given(instance=BookSet_strategy)
@settings(max_examples=50)
def test_bookset_instantiation(instance):
    assert isinstance(instance, BookSet)



@given(instance=BookSet_strategy)
def test_bookset_bookName_setter(instance):
    original = instance.bookName
    instance.bookName = original
    assert instance.bookName == original



@given(instance=BookSet_strategy)
def test_bookset_bookID_setter(instance):
    original = instance.bookID
    instance.bookID = original
    assert instance.bookID == original

@given(instance=Administrator_strategy)
@settings(max_examples=50)
def test_administrator_instantiation(instance):
    assert isinstance(instance, Administrator)



@given(instance=Administrator_strategy)
def test_administrator_adminID_setter(instance):
    original = instance.adminID
    instance.adminID = original
    assert instance.adminID == original



@given(instance=Administrator_strategy)
def test_administrator_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Administrator_strategy)
def test_administrator_phoneNo_setter(instance):
    original = instance.phoneNo
    instance.phoneNo = original
    assert instance.phoneNo == original



@given(instance=Administrator_strategy)
def test_administrator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Administrator_strategy)
def test_administrator_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=Book_strategy)
@settings(max_examples=50)
def test_book_instantiation(instance):
    assert isinstance(instance, Book)



@given(instance=Book_strategy)
def test_book_authorName_setter(instance):
    original = instance.authorName
    instance.authorName = original
    assert instance.authorName == original



@given(instance=Book_strategy)
def test_book_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Book_strategy)
def test_book_imageURL_setter(instance):
    original = instance.imageURL
    instance.imageURL = original
    assert instance.imageURL == original



@given(instance=Book_strategy)
def test_book_bookName_setter(instance):
    original = instance.bookName
    instance.bookName = original
    assert instance.bookName == original



@given(instance=Book_strategy)
def test_book_bookID_setter(instance):
    original = instance.bookID
    instance.bookID = original
    assert instance.bookID == original



@given(instance=Book_strategy)
def test_book_categoryID_setter(instance):
    original = instance.categoryID
    instance.categoryID = original
    assert instance.categoryID == original



@given(instance=Book_strategy)
def test_book_productURL_setter(instance):
    original = instance.productURL
    instance.productURL = original
    assert instance.productURL == original



@given(instance=Book_strategy)
def test_book_notes_setter(instance):
    original = instance.notes
    instance.notes = original
    assert instance.notes == original



@given(instance=Book_strategy)
def test_book_rating_setter(instance):
    original = instance.rating
    instance.rating = original
    assert instance.rating == original

@given(instance=BooksOrder_strategy)
@settings(max_examples=50)
def test_booksorder_instantiation(instance):
    assert isinstance(instance, BooksOrder)



@given(instance=BooksOrder_strategy)
def test_booksorder_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=BooksOrder_strategy)
def test_booksorder_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=BooksOrder_strategy)
def test_booksorder_customerID_setter(instance):
    original = instance.customerID
    instance.customerID = original
    assert instance.customerID == original



@given(instance=BooksOrder_strategy)
def test_booksorder_orderID_setter(instance):
    original = instance.orderID
    instance.orderID = original
    assert instance.orderID == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_phoneNo_setter(instance):
    original = instance.phoneNo
    instance.phoneNo = original
    assert instance.phoneNo == original



@given(instance=Customer_strategy)
def test_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Customer_strategy)
def test_customer_CCinfo_setter(instance):
    original = instance.CCinfo
    instance.CCinfo = original
    assert instance.CCinfo == original



@given(instance=Customer_strategy)
def test_customer_customerID_setter(instance):
    original = instance.customerID
    instance.customerID = original
    assert instance.customerID == original



@given(instance=Customer_strategy)
def test_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Customer_strategy)
def test_customer_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Customer_strategy)
def test_customer_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=SessionManager_strategy)
@settings(max_examples=50)
def test_sessionmanager_instantiation(instance):
    assert isinstance(instance, SessionManager)



@given(instance=SessionManager_strategy)
def test_sessionmanager_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=SessionManager_strategy)
def test_sessionmanager_categoryName_setter(instance):
    original = instance.categoryName
    instance.categoryName = original
    assert instance.categoryName == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_loginStatus_setter(instance):
    original = instance.loginStatus
    instance.loginStatus = original
    assert instance.loginStatus == original



@given(instance=User_strategy)
def test_user_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=User_strategy)
def test_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original
