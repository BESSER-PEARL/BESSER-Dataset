import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Search,
    library_ByAuthor,
    library_ByYear,
    library_Author,
    Command,
    library_Add,
    library_Remove,
    library_Check,
    library_Return,
    library_Lend,
    library_ShowUserAccount,
    library_AddUser,
    library_Show,
    library_AddAuthor,
    library_Search,
    library_Command,
    library_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_search_is_not_abstract():
    assert not inspect.isabstract(Search)


def test_search_constructor_exists():
    assert callable(Search.__init__)


def test_search_constructor_args():
    sig = inspect.signature(Search.__init__)
    params = list(sig.parameters.keys())



def test_library_byauthor_is_not_abstract():
    assert not inspect.isabstract(library_ByAuthor)


def test_library_byauthor_constructor_exists():
    assert callable(library_ByAuthor.__init__)


def test_library_byauthor_constructor_args():
    sig = inspect.signature(library_ByAuthor.__init__)
    params = list(sig.parameters.keys())



def test_library_byyear_is_not_abstract():
    assert not inspect.isabstract(library_ByYear)


def test_library_byyear_constructor_exists():
    assert callable(library_ByYear.__init__)


def test_library_byyear_constructor_args():
    sig = inspect.signature(library_ByYear.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"

def test_library_byyear_has_year():
    assert hasattr(library_ByYear, "year")
    descriptor = None
    for klass in library_ByYear.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_library_author_is_not_abstract():
    assert not inspect.isabstract(library_Author)


def test_library_author_constructor_exists():
    assert callable(library_Author.__init__)


def test_library_author_constructor_args():
    sig = inspect.signature(library_Author.__init__)
    params = list(sig.parameters.keys())
    assert "secondname" in params, "Missing parameter 'secondname'"
    assert "firstname" in params, "Missing parameter 'firstname'"

def test_library_author_has_secondname():
    assert hasattr(library_Author, "secondname")
    descriptor = None
    for klass in library_Author.__mro__:
        if "secondname" in klass.__dict__:
            descriptor = klass.__dict__["secondname"]
            break
    assert isinstance(descriptor, property)

def test_library_author_has_firstname():
    assert hasattr(library_Author, "firstname")
    descriptor = None
    for klass in library_Author.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)



def test_command_is_not_abstract():
    assert not inspect.isabstract(Command)


def test_command_constructor_exists():
    assert callable(Command.__init__)


def test_command_constructor_args():
    sig = inspect.signature(Command.__init__)
    params = list(sig.parameters.keys())



def test_library_add_is_not_abstract():
    assert not inspect.isabstract(library_Add)


def test_library_add_constructor_exists():
    assert callable(library_Add.__init__)


def test_library_add_constructor_args():
    sig = inspect.signature(library_Add.__init__)
    params = list(sig.parameters.keys())
    assert "isbn" in params, "Missing parameter 'isbn'"
    assert "year" in params, "Missing parameter 'year'"
    assert "title" in params, "Missing parameter 'title'"

def test_library_add_has_isbn():
    assert hasattr(library_Add, "isbn")
    descriptor = None
    for klass in library_Add.__mro__:
        if "isbn" in klass.__dict__:
            descriptor = klass.__dict__["isbn"]
            break
    assert isinstance(descriptor, property)

def test_library_add_has_year():
    assert hasattr(library_Add, "year")
    descriptor = None
    for klass in library_Add.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_library_add_has_title():
    assert hasattr(library_Add, "title")
    descriptor = None
    for klass in library_Add.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_library_remove_is_not_abstract():
    assert not inspect.isabstract(library_Remove)


def test_library_remove_constructor_exists():
    assert callable(library_Remove.__init__)


def test_library_remove_constructor_args():
    sig = inspect.signature(library_Remove.__init__)
    params = list(sig.parameters.keys())
    assert "isbn" in params, "Missing parameter 'isbn'"

def test_library_remove_has_isbn():
    assert hasattr(library_Remove, "isbn")
    descriptor = None
    for klass in library_Remove.__mro__:
        if "isbn" in klass.__dict__:
            descriptor = klass.__dict__["isbn"]
            break
    assert isinstance(descriptor, property)



def test_library_check_is_not_abstract():
    assert not inspect.isabstract(library_Check)


def test_library_check_constructor_exists():
    assert callable(library_Check.__init__)


def test_library_check_constructor_args():
    sig = inspect.signature(library_Check.__init__)
    params = list(sig.parameters.keys())
    assert "isbn" in params, "Missing parameter 'isbn'"

def test_library_check_has_isbn():
    assert hasattr(library_Check, "isbn")
    descriptor = None
    for klass in library_Check.__mro__:
        if "isbn" in klass.__dict__:
            descriptor = klass.__dict__["isbn"]
            break
    assert isinstance(descriptor, property)



def test_library_return_is_not_abstract():
    assert not inspect.isabstract(library_Return)


def test_library_return_constructor_exists():
    assert callable(library_Return.__init__)


def test_library_return_constructor_args():
    sig = inspect.signature(library_Return.__init__)
    params = list(sig.parameters.keys())
    assert "secondname" in params, "Missing parameter 'secondname'"
    assert "isbn" in params, "Missing parameter 'isbn'"
    assert "firstname" in params, "Missing parameter 'firstname'"

def test_library_return_has_secondname():
    assert hasattr(library_Return, "secondname")
    descriptor = None
    for klass in library_Return.__mro__:
        if "secondname" in klass.__dict__:
            descriptor = klass.__dict__["secondname"]
            break
    assert isinstance(descriptor, property)

def test_library_return_has_isbn():
    assert hasattr(library_Return, "isbn")
    descriptor = None
    for klass in library_Return.__mro__:
        if "isbn" in klass.__dict__:
            descriptor = klass.__dict__["isbn"]
            break
    assert isinstance(descriptor, property)

def test_library_return_has_firstname():
    assert hasattr(library_Return, "firstname")
    descriptor = None
    for klass in library_Return.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)



def test_library_lend_is_not_abstract():
    assert not inspect.isabstract(library_Lend)


def test_library_lend_constructor_exists():
    assert callable(library_Lend.__init__)


def test_library_lend_constructor_args():
    sig = inspect.signature(library_Lend.__init__)
    params = list(sig.parameters.keys())
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "isbn" in params, "Missing parameter 'isbn'"
    assert "secondname" in params, "Missing parameter 'secondname'"

def test_library_lend_has_firstname():
    assert hasattr(library_Lend, "firstname")
    descriptor = None
    for klass in library_Lend.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_library_lend_has_isbn():
    assert hasattr(library_Lend, "isbn")
    descriptor = None
    for klass in library_Lend.__mro__:
        if "isbn" in klass.__dict__:
            descriptor = klass.__dict__["isbn"]
            break
    assert isinstance(descriptor, property)

def test_library_lend_has_secondname():
    assert hasattr(library_Lend, "secondname")
    descriptor = None
    for klass in library_Lend.__mro__:
        if "secondname" in klass.__dict__:
            descriptor = klass.__dict__["secondname"]
            break
    assert isinstance(descriptor, property)



def test_library_showuseraccount_is_not_abstract():
    assert not inspect.isabstract(library_ShowUserAccount)


def test_library_showuseraccount_constructor_exists():
    assert callable(library_ShowUserAccount.__init__)


def test_library_showuseraccount_constructor_args():
    sig = inspect.signature(library_ShowUserAccount.__init__)
    params = list(sig.parameters.keys())
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "secondname" in params, "Missing parameter 'secondname'"

def test_library_showuseraccount_has_firstname():
    assert hasattr(library_ShowUserAccount, "firstname")
    descriptor = None
    for klass in library_ShowUserAccount.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_library_showuseraccount_has_secondname():
    assert hasattr(library_ShowUserAccount, "secondname")
    descriptor = None
    for klass in library_ShowUserAccount.__mro__:
        if "secondname" in klass.__dict__:
            descriptor = klass.__dict__["secondname"]
            break
    assert isinstance(descriptor, property)



def test_library_adduser_is_not_abstract():
    assert not inspect.isabstract(library_AddUser)


def test_library_adduser_constructor_exists():
    assert callable(library_AddUser.__init__)


def test_library_adduser_constructor_args():
    sig = inspect.signature(library_AddUser.__init__)
    params = list(sig.parameters.keys())
    assert "secondname" in params, "Missing parameter 'secondname'"
    assert "age" in params, "Missing parameter 'age'"
    assert "firstname" in params, "Missing parameter 'firstname'"

def test_library_adduser_has_secondname():
    assert hasattr(library_AddUser, "secondname")
    descriptor = None
    for klass in library_AddUser.__mro__:
        if "secondname" in klass.__dict__:
            descriptor = klass.__dict__["secondname"]
            break
    assert isinstance(descriptor, property)

def test_library_adduser_has_age():
    assert hasattr(library_AddUser, "age")
    descriptor = None
    for klass in library_AddUser.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_library_adduser_has_firstname():
    assert hasattr(library_AddUser, "firstname")
    descriptor = None
    for klass in library_AddUser.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)



def test_library_show_is_not_abstract():
    assert not inspect.isabstract(library_Show)


def test_library_show_constructor_exists():
    assert callable(library_Show.__init__)


def test_library_show_constructor_args():
    sig = inspect.signature(library_Show.__init__)
    params = list(sig.parameters.keys())
    assert "what" in params, "Missing parameter 'what'"

def test_library_show_has_what():
    assert hasattr(library_Show, "what")
    descriptor = None
    for klass in library_Show.__mro__:
        if "what" in klass.__dict__:
            descriptor = klass.__dict__["what"]
            break
    assert isinstance(descriptor, property)



def test_library_addauthor_is_not_abstract():
    assert not inspect.isabstract(library_AddAuthor)


def test_library_addauthor_constructor_exists():
    assert callable(library_AddAuthor.__init__)


def test_library_addauthor_constructor_args():
    sig = inspect.signature(library_AddAuthor.__init__)
    params = list(sig.parameters.keys())
    assert "isbn" in params, "Missing parameter 'isbn'"

def test_library_addauthor_has_isbn():
    assert hasattr(library_AddAuthor, "isbn")
    descriptor = None
    for klass in library_AddAuthor.__mro__:
        if "isbn" in klass.__dict__:
            descriptor = klass.__dict__["isbn"]
            break
    assert isinstance(descriptor, property)



def test_library_search_is_not_abstract():
    assert not inspect.isabstract(library_Search)


def test_library_search_constructor_exists():
    assert callable(library_Search.__init__)


def test_library_search_constructor_args():
    sig = inspect.signature(library_Search.__init__)
    params = list(sig.parameters.keys())



def test_library_command_is_not_abstract():
    assert not inspect.isabstract(library_Command)


def test_library_command_constructor_exists():
    assert callable(library_Command.__init__)


def test_library_command_constructor_args():
    sig = inspect.signature(library_Command.__init__)
    params = list(sig.parameters.keys())



def test_library_model_is_not_abstract():
    assert not inspect.isabstract(library_Model)


def test_library_model_constructor_exists():
    assert callable(library_Model.__init__)


def test_library_model_constructor_args():
    sig = inspect.signature(library_Model.__init__)
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
Search_strategy = st.builds(
    Search,
)
library_ByAuthor_strategy = st.builds(
    library_ByAuthor,
)
library_ByYear_strategy = st.builds(
    library_ByYear,
    year=
        safe_text
)
library_Author_strategy = st.builds(
    library_Author,
    secondname=
        safe_text,
    firstname=
        safe_text
)
Command_strategy = st.builds(
    Command,
)
library_Add_strategy = st.builds(
    library_Add,
    isbn=
        safe_text,
    year=
        safe_text,
    title=
        safe_text
)
library_Remove_strategy = st.builds(
    library_Remove,
    isbn=
        safe_text
)
library_Check_strategy = st.builds(
    library_Check,
    isbn=
        safe_text
)
library_Return_strategy = st.builds(
    library_Return,
    secondname=
        safe_text,
    isbn=
        safe_text,
    firstname=
        safe_text
)
library_Lend_strategy = st.builds(
    library_Lend,
    firstname=
        safe_text,
    isbn=
        safe_text,
    secondname=
        safe_text
)
library_ShowUserAccount_strategy = st.builds(
    library_ShowUserAccount,
    firstname=
        safe_text,
    secondname=
        safe_text
)
library_AddUser_strategy = st.builds(
    library_AddUser,
    secondname=
        safe_text,
    age=
        safe_text,
    firstname=
        safe_text
)
library_Show_strategy = st.builds(
    library_Show,
    what=
        safe_text
)
library_AddAuthor_strategy = st.builds(
    library_AddAuthor,
    isbn=
        safe_text
)
library_Search_strategy = st.builds(
    library_Search,
)
library_Command_strategy = st.builds(
    library_Command,
)
library_Model_strategy = st.builds(
    library_Model,
)

@given(instance=Search_strategy)
@settings(max_examples=50)
def test_search_instantiation(instance):
    assert isinstance(instance, Search)

@given(instance=library_ByAuthor_strategy)
@settings(max_examples=50)
def test_library_byauthor_instantiation(instance):
    assert isinstance(instance, library_ByAuthor)

@given(instance=library_ByYear_strategy)
@settings(max_examples=50)
def test_library_byyear_instantiation(instance):
    assert isinstance(instance, library_ByYear)



@given(instance=library_ByYear_strategy)
def test_library_byyear_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=library_Author_strategy)
@settings(max_examples=50)
def test_library_author_instantiation(instance):
    assert isinstance(instance, library_Author)



@given(instance=library_Author_strategy)
def test_library_author_secondname_setter(instance):
    original = instance.secondname
    instance.secondname = original
    assert instance.secondname == original



@given(instance=library_Author_strategy)
def test_library_author_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original

@given(instance=Command_strategy)
@settings(max_examples=50)
def test_command_instantiation(instance):
    assert isinstance(instance, Command)

@given(instance=library_Add_strategy)
@settings(max_examples=50)
def test_library_add_instantiation(instance):
    assert isinstance(instance, library_Add)



@given(instance=library_Add_strategy)
def test_library_add_isbn_setter(instance):
    original = instance.isbn
    instance.isbn = original
    assert instance.isbn == original



@given(instance=library_Add_strategy)
def test_library_add_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=library_Add_strategy)
def test_library_add_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=library_Remove_strategy)
@settings(max_examples=50)
def test_library_remove_instantiation(instance):
    assert isinstance(instance, library_Remove)



@given(instance=library_Remove_strategy)
def test_library_remove_isbn_setter(instance):
    original = instance.isbn
    instance.isbn = original
    assert instance.isbn == original

@given(instance=library_Check_strategy)
@settings(max_examples=50)
def test_library_check_instantiation(instance):
    assert isinstance(instance, library_Check)



@given(instance=library_Check_strategy)
def test_library_check_isbn_setter(instance):
    original = instance.isbn
    instance.isbn = original
    assert instance.isbn == original

@given(instance=library_Return_strategy)
@settings(max_examples=50)
def test_library_return_instantiation(instance):
    assert isinstance(instance, library_Return)



@given(instance=library_Return_strategy)
def test_library_return_secondname_setter(instance):
    original = instance.secondname
    instance.secondname = original
    assert instance.secondname == original



@given(instance=library_Return_strategy)
def test_library_return_isbn_setter(instance):
    original = instance.isbn
    instance.isbn = original
    assert instance.isbn == original



@given(instance=library_Return_strategy)
def test_library_return_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original

@given(instance=library_Lend_strategy)
@settings(max_examples=50)
def test_library_lend_instantiation(instance):
    assert isinstance(instance, library_Lend)



@given(instance=library_Lend_strategy)
def test_library_lend_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original



@given(instance=library_Lend_strategy)
def test_library_lend_isbn_setter(instance):
    original = instance.isbn
    instance.isbn = original
    assert instance.isbn == original



@given(instance=library_Lend_strategy)
def test_library_lend_secondname_setter(instance):
    original = instance.secondname
    instance.secondname = original
    assert instance.secondname == original

@given(instance=library_ShowUserAccount_strategy)
@settings(max_examples=50)
def test_library_showuseraccount_instantiation(instance):
    assert isinstance(instance, library_ShowUserAccount)



@given(instance=library_ShowUserAccount_strategy)
def test_library_showuseraccount_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original



@given(instance=library_ShowUserAccount_strategy)
def test_library_showuseraccount_secondname_setter(instance):
    original = instance.secondname
    instance.secondname = original
    assert instance.secondname == original

@given(instance=library_AddUser_strategy)
@settings(max_examples=50)
def test_library_adduser_instantiation(instance):
    assert isinstance(instance, library_AddUser)



@given(instance=library_AddUser_strategy)
def test_library_adduser_secondname_setter(instance):
    original = instance.secondname
    instance.secondname = original
    assert instance.secondname == original



@given(instance=library_AddUser_strategy)
def test_library_adduser_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=library_AddUser_strategy)
def test_library_adduser_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original

@given(instance=library_Show_strategy)
@settings(max_examples=50)
def test_library_show_instantiation(instance):
    assert isinstance(instance, library_Show)



@given(instance=library_Show_strategy)
def test_library_show_what_setter(instance):
    original = instance.what
    instance.what = original
    assert instance.what == original

@given(instance=library_AddAuthor_strategy)
@settings(max_examples=50)
def test_library_addauthor_instantiation(instance):
    assert isinstance(instance, library_AddAuthor)



@given(instance=library_AddAuthor_strategy)
def test_library_addauthor_isbn_setter(instance):
    original = instance.isbn
    instance.isbn = original
    assert instance.isbn == original

@given(instance=library_Search_strategy)
@settings(max_examples=50)
def test_library_search_instantiation(instance):
    assert isinstance(instance, library_Search)

@given(instance=library_Command_strategy)
@settings(max_examples=50)
def test_library_command_instantiation(instance):
    assert isinstance(instance, library_Command)

@given(instance=library_Model_strategy)
@settings(max_examples=50)
def test_library_model_instantiation(instance):
    assert isinstance(instance, library_Model)
