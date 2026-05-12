import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Category,
    Customer,
    Book,
    Administrator,
    Bank_Mobile_Money_Agent_Actor,
    Confirm_Payment_UseCase,
    Edit_Book_UseCase,
    Add_Book_UseCase,
    Administrator_Actor,
    Logout_UseCase,
    Make_Payment_UseCase,
    Add_book__to_cart_UseCase,
    Search_Book_UseCase,
    Log_in_UseCase,
    Sign_up_UseCase,
    Customer_Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
    assert "email" in params, "Missing parameter 'email'"
    assert "CustomerID" in params, "Missing parameter 'CustomerID'"

def test_customer_has_username():
    assert hasattr(Customer, "username")
    descriptor = None
    for klass in Customer.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
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

def test_customer_has_CustomerID():
    assert hasattr(Customer, "CustomerID")
    descriptor = None
    for klass in Customer.__mro__:
        if "CustomerID" in klass.__dict__:
            descriptor = klass.__dict__["CustomerID"]
            break
    assert isinstance(descriptor, property)



def test_book_is_not_abstract():
    assert not inspect.isabstract(Book)


def test_book_constructor_exists():
    assert callable(Book.__init__)


def test_book_constructor_args():
    sig = inspect.signature(Book.__init__)
    params = list(sig.parameters.keys())
    assert "author" in params, "Missing parameter 'author'"
    assert "title" in params, "Missing parameter 'title'"
    assert "category" in params, "Missing parameter 'category'"
    assert "price" in params, "Missing parameter 'price'"
    assert "bookID" in params, "Missing parameter 'bookID'"
    assert "description" in params, "Missing parameter 'description'"

def test_book_has_author():
    assert hasattr(Book, "author")
    descriptor = None
    for klass in Book.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_book_has_title():
    assert hasattr(Book, "title")
    descriptor = None
    for klass in Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_book_has_category():
    assert hasattr(Book, "category")
    descriptor = None
    for klass in Book.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
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

def test_book_has_bookID():
    assert hasattr(Book, "bookID")
    descriptor = None
    for klass in Book.__mro__:
        if "bookID" in klass.__dict__:
            descriptor = klass.__dict__["bookID"]
            break
    assert isinstance(descriptor, property)

def test_book_has_description():
    assert hasattr(Book, "description")
    descriptor = None
    for klass in Book.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
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
    assert "name" in params, "Missing parameter 'name'"

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

def test_administrator_has_name():
    assert hasattr(Administrator, "name")
    descriptor = None
    for klass in Administrator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bank_mobile_money_agent_actor_is_not_abstract():
    assert not inspect.isabstract(Bank_Mobile_Money_Agent_Actor)


def test_bank_mobile_money_agent_actor_constructor_exists():
    assert callable(Bank_Mobile_Money_Agent_Actor.__init__)


def test_bank_mobile_money_agent_actor_constructor_args():
    sig = inspect.signature(Bank_Mobile_Money_Agent_Actor.__init__)
    params = list(sig.parameters.keys())



def test_confirm_payment_usecase_is_not_abstract():
    assert not inspect.isabstract(Confirm_Payment_UseCase)


def test_confirm_payment_usecase_constructor_exists():
    assert callable(Confirm_Payment_UseCase.__init__)


def test_confirm_payment_usecase_constructor_args():
    sig = inspect.signature(Confirm_Payment_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_edit_book_usecase_is_not_abstract():
    assert not inspect.isabstract(Edit_Book_UseCase)


def test_edit_book_usecase_constructor_exists():
    assert callable(Edit_Book_UseCase.__init__)


def test_edit_book_usecase_constructor_args():
    sig = inspect.signature(Edit_Book_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_add_book_usecase_is_not_abstract():
    assert not inspect.isabstract(Add_Book_UseCase)


def test_add_book_usecase_constructor_exists():
    assert callable(Add_Book_UseCase.__init__)


def test_add_book_usecase_constructor_args():
    sig = inspect.signature(Add_Book_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_administrator_actor_is_not_abstract():
    assert not inspect.isabstract(Administrator_Actor)


def test_administrator_actor_constructor_exists():
    assert callable(Administrator_Actor.__init__)


def test_administrator_actor_constructor_args():
    sig = inspect.signature(Administrator_Actor.__init__)
    params = list(sig.parameters.keys())



def test_logout_usecase_is_not_abstract():
    assert not inspect.isabstract(Logout_UseCase)


def test_logout_usecase_constructor_exists():
    assert callable(Logout_UseCase.__init__)


def test_logout_usecase_constructor_args():
    sig = inspect.signature(Logout_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_make_payment_usecase_is_not_abstract():
    assert not inspect.isabstract(Make_Payment_UseCase)


def test_make_payment_usecase_constructor_exists():
    assert callable(Make_Payment_UseCase.__init__)


def test_make_payment_usecase_constructor_args():
    sig = inspect.signature(Make_Payment_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_add_book__to_cart_usecase_is_not_abstract():
    assert not inspect.isabstract(Add_book__to_cart_UseCase)


def test_add_book__to_cart_usecase_constructor_exists():
    assert callable(Add_book__to_cart_UseCase.__init__)


def test_add_book__to_cart_usecase_constructor_args():
    sig = inspect.signature(Add_book__to_cart_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_search_book_usecase_is_not_abstract():
    assert not inspect.isabstract(Search_Book_UseCase)


def test_search_book_usecase_constructor_exists():
    assert callable(Search_Book_UseCase.__init__)


def test_search_book_usecase_constructor_args():
    sig = inspect.signature(Search_Book_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_log_in_usecase_is_not_abstract():
    assert not inspect.isabstract(Log_in_UseCase)


def test_log_in_usecase_constructor_exists():
    assert callable(Log_in_UseCase.__init__)


def test_log_in_usecase_constructor_args():
    sig = inspect.signature(Log_in_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_sign_up_usecase_is_not_abstract():
    assert not inspect.isabstract(Sign_up_UseCase)


def test_sign_up_usecase_constructor_exists():
    assert callable(Sign_up_UseCase.__init__)


def test_sign_up_usecase_constructor_args():
    sig = inspect.signature(Sign_up_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_customer_actor_is_not_abstract():
    assert not inspect.isabstract(Customer_Actor)


def test_customer_actor_constructor_exists():
    assert callable(Customer_Actor.__init__)


def test_customer_actor_constructor_args():
    sig = inspect.signature(Customer_Actor.__init__)
    params = list(sig.parameters.keys())


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
Category_strategy = st.builds(
    Category,
    categoryID=
        st.integers(),
    categoryName=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    username=
        safe_text,
    email=
        safe_text,
    CustomerID=
        st.integers()
)
Book_strategy = st.builds(
    Book,
    author=
        safe_text,
    title=
        safe_text,
    category=
        st.none(),
    price=
        st.integers(),
    bookID=
        st.integers(),
    description=
        safe_text
)
Administrator_strategy = st.builds(
    Administrator,
    adminID=
        st.integers(),
    email=
        safe_text,
    name=
        safe_text
)
Bank_Mobile_Money_Agent_Actor_strategy = st.builds(
    Bank_Mobile_Money_Agent_Actor,
)
Confirm_Payment_UseCase_strategy = st.builds(
    Confirm_Payment_UseCase,
)
Edit_Book_UseCase_strategy = st.builds(
    Edit_Book_UseCase,
)
Add_Book_UseCase_strategy = st.builds(
    Add_Book_UseCase,
)
Administrator_Actor_strategy = st.builds(
    Administrator_Actor,
)
Logout_UseCase_strategy = st.builds(
    Logout_UseCase,
)
Make_Payment_UseCase_strategy = st.builds(
    Make_Payment_UseCase,
)
Add_book__to_cart_UseCase_strategy = st.builds(
    Add_book__to_cart_UseCase,
)
Search_Book_UseCase_strategy = st.builds(
    Search_Book_UseCase,
)
Log_in_UseCase_strategy = st.builds(
    Log_in_UseCase,
)
Sign_up_UseCase_strategy = st.builds(
    Sign_up_UseCase,
)
Customer_Actor_strategy = st.builds(
    Customer_Actor,
)

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

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Customer_strategy)
def test_customer_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Customer_strategy)
def test_customer_CustomerID_setter(instance):
    original = instance.CustomerID
    instance.CustomerID = original
    assert instance.CustomerID == original

@given(instance=Book_strategy)
@settings(max_examples=50)
def test_book_instantiation(instance):
    assert isinstance(instance, Book)



@given(instance=Book_strategy)
def test_book_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=Book_strategy)
def test_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=Book_strategy)
def test_book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=Book_strategy)
def test_book_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Book_strategy)
def test_book_bookID_setter(instance):
    original = instance.bookID
    instance.bookID = original
    assert instance.bookID == original



@given(instance=Book_strategy)
def test_book_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

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
def test_administrator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Bank_Mobile_Money_Agent_Actor_strategy)
@settings(max_examples=50)
def test_bank_mobile_money_agent_actor_instantiation(instance):
    assert isinstance(instance, Bank_Mobile_Money_Agent_Actor)

@given(instance=Confirm_Payment_UseCase_strategy)
@settings(max_examples=50)
def test_confirm_payment_usecase_instantiation(instance):
    assert isinstance(instance, Confirm_Payment_UseCase)

@given(instance=Edit_Book_UseCase_strategy)
@settings(max_examples=50)
def test_edit_book_usecase_instantiation(instance):
    assert isinstance(instance, Edit_Book_UseCase)

@given(instance=Add_Book_UseCase_strategy)
@settings(max_examples=50)
def test_add_book_usecase_instantiation(instance):
    assert isinstance(instance, Add_Book_UseCase)

@given(instance=Administrator_Actor_strategy)
@settings(max_examples=50)
def test_administrator_actor_instantiation(instance):
    assert isinstance(instance, Administrator_Actor)

@given(instance=Logout_UseCase_strategy)
@settings(max_examples=50)
def test_logout_usecase_instantiation(instance):
    assert isinstance(instance, Logout_UseCase)

@given(instance=Make_Payment_UseCase_strategy)
@settings(max_examples=50)
def test_make_payment_usecase_instantiation(instance):
    assert isinstance(instance, Make_Payment_UseCase)

@given(instance=Add_book__to_cart_UseCase_strategy)
@settings(max_examples=50)
def test_add_book__to_cart_usecase_instantiation(instance):
    assert isinstance(instance, Add_book__to_cart_UseCase)

@given(instance=Search_Book_UseCase_strategy)
@settings(max_examples=50)
def test_search_book_usecase_instantiation(instance):
    assert isinstance(instance, Search_Book_UseCase)

@given(instance=Log_in_UseCase_strategy)
@settings(max_examples=50)
def test_log_in_usecase_instantiation(instance):
    assert isinstance(instance, Log_in_UseCase)

@given(instance=Sign_up_UseCase_strategy)
@settings(max_examples=50)
def test_sign_up_usecase_instantiation(instance):
    assert isinstance(instance, Sign_up_UseCase)

@given(instance=Customer_Actor_strategy)
@settings(max_examples=50)
def test_customer_actor_instantiation(instance):
    assert isinstance(instance, Customer_Actor)
