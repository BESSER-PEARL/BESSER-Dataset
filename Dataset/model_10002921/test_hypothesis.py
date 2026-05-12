import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Hall_book,
    View_and_place_order,
    Decoration_book,
    Catering_book,
    View_and_update,
    Hall,
    Decoration,
    Catering,
    Admin,
    User,
    void,
    LOGIN,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hall_book_is_not_abstract():
    assert not inspect.isabstract(Hall_book)


def test_hall_book_constructor_exists():
    assert callable(Hall_book.__init__)


def test_hall_book_constructor_args():
    sig = inspect.signature(Hall_book.__init__)
    params = list(sig.parameters.keys())
    assert "get_room_type" in params, "Missing parameter 'get_room_type'"
    assert "cost_per_day" in params, "Missing parameter 'cost_per_day'"
    assert "get_hall_no" in params, "Missing parameter 'get_hall_no'"

def test_hall_book_has_get_room_type():
    assert hasattr(Hall_book, "get_room_type")
    descriptor = None
    for klass in Hall_book.__mro__:
        if "get_room_type" in klass.__dict__:
            descriptor = klass.__dict__["get_room_type"]
            break
    assert isinstance(descriptor, property)

def test_hall_book_has_cost_per_day():
    assert hasattr(Hall_book, "cost_per_day")
    descriptor = None
    for klass in Hall_book.__mro__:
        if "cost_per_day" in klass.__dict__:
            descriptor = klass.__dict__["cost_per_day"]
            break
    assert isinstance(descriptor, property)

def test_hall_book_has_get_hall_no():
    assert hasattr(Hall_book, "get_hall_no")
    descriptor = None
    for klass in Hall_book.__mro__:
        if "get_hall_no" in klass.__dict__:
            descriptor = klass.__dict__["get_hall_no"]
            break
    assert isinstance(descriptor, property)



def test_view_and_place_order_is_not_abstract():
    assert not inspect.isabstract(View_and_place_order)


def test_view_and_place_order_constructor_exists():
    assert callable(View_and_place_order.__init__)


def test_view_and_place_order_constructor_args():
    sig = inspect.signature(View_and_place_order.__init__)
    params = list(sig.parameters.keys())
    assert "place_order" in params, "Missing parameter 'place_order'"
    assert "order_view" in params, "Missing parameter 'order_view'"

def test_view_and_place_order_has_place_order():
    assert hasattr(View_and_place_order, "place_order")
    descriptor = None
    for klass in View_and_place_order.__mro__:
        if "place_order" in klass.__dict__:
            descriptor = klass.__dict__["place_order"]
            break
    assert isinstance(descriptor, property)

def test_view_and_place_order_has_order_view():
    assert hasattr(View_and_place_order, "order_view")
    descriptor = None
    for klass in View_and_place_order.__mro__:
        if "order_view" in klass.__dict__:
            descriptor = klass.__dict__["order_view"]
            break
    assert isinstance(descriptor, property)



def test_decoration_book_is_not_abstract():
    assert not inspect.isabstract(Decoration_book)


def test_decoration_book_constructor_exists():
    assert callable(Decoration_book.__init__)


def test_decoration_book_constructor_args():
    sig = inspect.signature(Decoration_book.__init__)
    params = list(sig.parameters.keys())
    assert "Square_feet" in params, "Missing parameter 'Square_feet'"
    assert "cost" in params, "Missing parameter 'cost'"
    assert "Decor_type" in params, "Missing parameter 'Decor_type'"

def test_decoration_book_has_Square_feet():
    assert hasattr(Decoration_book, "Square_feet")
    descriptor = None
    for klass in Decoration_book.__mro__:
        if "Square_feet" in klass.__dict__:
            descriptor = klass.__dict__["Square_feet"]
            break
    assert isinstance(descriptor, property)

def test_decoration_book_has_cost():
    assert hasattr(Decoration_book, "cost")
    descriptor = None
    for klass in Decoration_book.__mro__:
        if "cost" in klass.__dict__:
            descriptor = klass.__dict__["cost"]
            break
    assert isinstance(descriptor, property)

def test_decoration_book_has_Decor_type():
    assert hasattr(Decoration_book, "Decor_type")
    descriptor = None
    for klass in Decoration_book.__mro__:
        if "Decor_type" in klass.__dict__:
            descriptor = klass.__dict__["Decor_type"]
            break
    assert isinstance(descriptor, property)



def test_catering_book_is_not_abstract():
    assert not inspect.isabstract(Catering_book)


def test_catering_book_constructor_exists():
    assert callable(Catering_book.__init__)


def test_catering_book_constructor_args():
    sig = inspect.signature(Catering_book.__init__)
    params = list(sig.parameters.keys())
    assert "get_cost" in params, "Missing parameter 'get_cost'"
    assert "get_menu" in params, "Missing parameter 'get_menu'"

def test_catering_book_has_get_cost():
    assert hasattr(Catering_book, "get_cost")
    descriptor = None
    for klass in Catering_book.__mro__:
        if "get_cost" in klass.__dict__:
            descriptor = klass.__dict__["get_cost"]
            break
    assert isinstance(descriptor, property)

def test_catering_book_has_get_menu():
    assert hasattr(Catering_book, "get_menu")
    descriptor = None
    for klass in Catering_book.__mro__:
        if "get_menu" in klass.__dict__:
            descriptor = klass.__dict__["get_menu"]
            break
    assert isinstance(descriptor, property)



def test_view_and_update_is_not_abstract():
    assert not inspect.isabstract(View_and_update)


def test_view_and_update_constructor_exists():
    assert callable(View_and_update.__init__)


def test_view_and_update_constructor_args():
    sig = inspect.signature(View_and_update.__init__)
    params = list(sig.parameters.keys())
    assert "update_order" in params, "Missing parameter 'update_order'"
    assert "order_view" in params, "Missing parameter 'order_view'"

def test_view_and_update_has_update_order():
    assert hasattr(View_and_update, "update_order")
    descriptor = None
    for klass in View_and_update.__mro__:
        if "update_order" in klass.__dict__:
            descriptor = klass.__dict__["update_order"]
            break
    assert isinstance(descriptor, property)

def test_view_and_update_has_order_view():
    assert hasattr(View_and_update, "order_view")
    descriptor = None
    for klass in View_and_update.__mro__:
        if "order_view" in klass.__dict__:
            descriptor = klass.__dict__["order_view"]
            break
    assert isinstance(descriptor, property)



def test_hall_is_not_abstract():
    assert not inspect.isabstract(Hall)


def test_hall_constructor_exists():
    assert callable(Hall.__init__)


def test_hall_constructor_args():
    sig = inspect.signature(Hall.__init__)
    params = list(sig.parameters.keys())
    assert "cost_per_day" in params, "Missing parameter 'cost_per_day'"
    assert "get_hall_no" in params, "Missing parameter 'get_hall_no'"
    assert "get_room_type" in params, "Missing parameter 'get_room_type'"

def test_hall_has_cost_per_day():
    assert hasattr(Hall, "cost_per_day")
    descriptor = None
    for klass in Hall.__mro__:
        if "cost_per_day" in klass.__dict__:
            descriptor = klass.__dict__["cost_per_day"]
            break
    assert isinstance(descriptor, property)

def test_hall_has_get_hall_no():
    assert hasattr(Hall, "get_hall_no")
    descriptor = None
    for klass in Hall.__mro__:
        if "get_hall_no" in klass.__dict__:
            descriptor = klass.__dict__["get_hall_no"]
            break
    assert isinstance(descriptor, property)

def test_hall_has_get_room_type():
    assert hasattr(Hall, "get_room_type")
    descriptor = None
    for klass in Hall.__mro__:
        if "get_room_type" in klass.__dict__:
            descriptor = klass.__dict__["get_room_type"]
            break
    assert isinstance(descriptor, property)



def test_decoration_is_not_abstract():
    assert not inspect.isabstract(Decoration)


def test_decoration_constructor_exists():
    assert callable(Decoration.__init__)


def test_decoration_constructor_args():
    sig = inspect.signature(Decoration.__init__)
    params = list(sig.parameters.keys())
    assert "Decor_type" in params, "Missing parameter 'Decor_type'"
    assert "cost" in params, "Missing parameter 'cost'"
    assert "Square_feet" in params, "Missing parameter 'Square_feet'"

def test_decoration_has_Decor_type():
    assert hasattr(Decoration, "Decor_type")
    descriptor = None
    for klass in Decoration.__mro__:
        if "Decor_type" in klass.__dict__:
            descriptor = klass.__dict__["Decor_type"]
            break
    assert isinstance(descriptor, property)

def test_decoration_has_cost():
    assert hasattr(Decoration, "cost")
    descriptor = None
    for klass in Decoration.__mro__:
        if "cost" in klass.__dict__:
            descriptor = klass.__dict__["cost"]
            break
    assert isinstance(descriptor, property)

def test_decoration_has_Square_feet():
    assert hasattr(Decoration, "Square_feet")
    descriptor = None
    for klass in Decoration.__mro__:
        if "Square_feet" in klass.__dict__:
            descriptor = klass.__dict__["Square_feet"]
            break
    assert isinstance(descriptor, property)



def test_catering_is_not_abstract():
    assert not inspect.isabstract(Catering)


def test_catering_constructor_exists():
    assert callable(Catering.__init__)


def test_catering_constructor_args():
    sig = inspect.signature(Catering.__init__)
    params = list(sig.parameters.keys())
    assert "get_menu" in params, "Missing parameter 'get_menu'"
    assert "get_cost" in params, "Missing parameter 'get_cost'"

def test_catering_has_get_menu():
    assert hasattr(Catering, "get_menu")
    descriptor = None
    for klass in Catering.__mro__:
        if "get_menu" in klass.__dict__:
            descriptor = klass.__dict__["get_menu"]
            break
    assert isinstance(descriptor, property)

def test_catering_has_get_cost():
    assert hasattr(Catering, "get_cost")
    descriptor = None
    for klass in Catering.__mro__:
        if "get_cost" in klass.__dict__:
            descriptor = klass.__dict__["get_cost"]
            break
    assert isinstance(descriptor, property)



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "userName" in params, "Missing parameter 'userName'"
    assert "password" in params, "Missing parameter 'password'"
    assert "userID" in params, "Missing parameter 'userID'"

def test_admin_has_userName():
    assert hasattr(Admin, "userName")
    descriptor = None
    for klass in Admin.__mro__:
        if "userName" in klass.__dict__:
            descriptor = klass.__dict__["userName"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_password():
    assert hasattr(Admin, "password")
    descriptor = None
    for klass in Admin.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_userID():
    assert hasattr(Admin, "userID")
    descriptor = None
    for klass in Admin.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "userName" in params, "Missing parameter 'userName'"
    assert "password" in params, "Missing parameter 'password'"
    assert "userID" in params, "Missing parameter 'userID'"

def test_user_has_userName():
    assert hasattr(User, "userName")
    descriptor = None
    for klass in User.__mro__:
        if "userName" in klass.__dict__:
            descriptor = klass.__dict__["userName"]
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

def test_user_has_userID():
    assert hasattr(User, "userID")
    descriptor = None
    for klass in User.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)



def test_void_is_not_abstract():
    assert not inspect.isabstract(void)


def test_void_constructor_exists():
    assert callable(void.__init__)


def test_void_constructor_args():
    sig = inspect.signature(void.__init__)
    params = list(sig.parameters.keys())



def test_login_is_not_abstract():
    assert not inspect.isabstract(LOGIN)


def test_login_constructor_exists():
    assert callable(LOGIN.__init__)


def test_login_constructor_args():
    sig = inspect.signature(LOGIN.__init__)
    params = list(sig.parameters.keys())
    assert "user_Name" in params, "Missing parameter 'user_Name'"
    assert "l_Name" in params, "Missing parameter 'l_Name'"
    assert "password" in params, "Missing parameter 'password'"
    assert "f_Name" in params, "Missing parameter 'f_Name'"

def test_login_has_user_Name():
    assert hasattr(LOGIN, "user_Name")
    descriptor = None
    for klass in LOGIN.__mro__:
        if "user_Name" in klass.__dict__:
            descriptor = klass.__dict__["user_Name"]
            break
    assert isinstance(descriptor, property)

def test_login_has_l_Name():
    assert hasattr(LOGIN, "l_Name")
    descriptor = None
    for klass in LOGIN.__mro__:
        if "l_Name" in klass.__dict__:
            descriptor = klass.__dict__["l_Name"]
            break
    assert isinstance(descriptor, property)

def test_login_has_password():
    assert hasattr(LOGIN, "password")
    descriptor = None
    for klass in LOGIN.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_login_has_f_Name():
    assert hasattr(LOGIN, "f_Name")
    descriptor = None
    for klass in LOGIN.__mro__:
        if "f_Name" in klass.__dict__:
            descriptor = klass.__dict__["f_Name"]
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
Hall_book_strategy = st.builds(
    Hall_book,
    get_room_type=
        safe_text,
    cost_per_day=
        safe_text,
    get_hall_no=
        safe_text
)
View_and_place_order_strategy = st.builds(
    View_and_place_order,
    place_order=
        st.none(),
    order_view=
        st.none()
)
Decoration_book_strategy = st.builds(
    Decoration_book,
    Square_feet=
        safe_text,
    cost=
        safe_text,
    Decor_type=
        st.none()
)
Catering_book_strategy = st.builds(
    Catering_book,
    get_cost=
        safe_text,
    get_menu=
        safe_text
)
View_and_update_strategy = st.builds(
    View_and_update,
    update_order=
        st.none(),
    order_view=
        st.none()
)
Hall_strategy = st.builds(
    Hall,
    cost_per_day=
        safe_text,
    get_hall_no=
        safe_text,
    get_room_type=
        safe_text
)
Decoration_strategy = st.builds(
    Decoration,
    Decor_type=
        st.none(),
    cost=
        safe_text,
    Square_feet=
        safe_text
)
Catering_strategy = st.builds(
    Catering,
    get_menu=
        safe_text,
    get_cost=
        safe_text
)
Admin_strategy = st.builds(
    Admin,
    userName=
        safe_text,
    password=
        safe_text,
    userID=
        st.integers()
)
User_strategy = st.builds(
    User,
    userName=
        safe_text,
    password=
        safe_text,
    userID=
        st.integers()
)
void_strategy = st.builds(
    void,
)
LOGIN_strategy = st.builds(
    LOGIN,
    user_Name=
        safe_text,
    l_Name=
        safe_text,
    password=
        safe_text,
    f_Name=
        safe_text
)

@given(instance=Hall_book_strategy)
@settings(max_examples=50)
def test_hall_book_instantiation(instance):
    assert isinstance(instance, Hall_book)



@given(instance=Hall_book_strategy)
def test_hall_book_get_room_type_setter(instance):
    original = instance.get_room_type
    instance.get_room_type = original
    assert instance.get_room_type == original



@given(instance=Hall_book_strategy)
def test_hall_book_cost_per_day_setter(instance):
    original = instance.cost_per_day
    instance.cost_per_day = original
    assert instance.cost_per_day == original



@given(instance=Hall_book_strategy)
def test_hall_book_get_hall_no_setter(instance):
    original = instance.get_hall_no
    instance.get_hall_no = original
    assert instance.get_hall_no == original

@given(instance=View_and_place_order_strategy)
@settings(max_examples=50)
def test_view_and_place_order_instantiation(instance):
    assert isinstance(instance, View_and_place_order)



@given(instance=View_and_place_order_strategy)
def test_view_and_place_order_place_order_setter(instance):
    original = instance.place_order
    instance.place_order = original
    assert instance.place_order == original



@given(instance=View_and_place_order_strategy)
def test_view_and_place_order_order_view_setter(instance):
    original = instance.order_view
    instance.order_view = original
    assert instance.order_view == original

@given(instance=Decoration_book_strategy)
@settings(max_examples=50)
def test_decoration_book_instantiation(instance):
    assert isinstance(instance, Decoration_book)



@given(instance=Decoration_book_strategy)
def test_decoration_book_Square_feet_setter(instance):
    original = instance.Square_feet
    instance.Square_feet = original
    assert instance.Square_feet == original



@given(instance=Decoration_book_strategy)
def test_decoration_book_cost_setter(instance):
    original = instance.cost
    instance.cost = original
    assert instance.cost == original



@given(instance=Decoration_book_strategy)
def test_decoration_book_Decor_type_setter(instance):
    original = instance.Decor_type
    instance.Decor_type = original
    assert instance.Decor_type == original

@given(instance=Catering_book_strategy)
@settings(max_examples=50)
def test_catering_book_instantiation(instance):
    assert isinstance(instance, Catering_book)



@given(instance=Catering_book_strategy)
def test_catering_book_get_cost_setter(instance):
    original = instance.get_cost
    instance.get_cost = original
    assert instance.get_cost == original



@given(instance=Catering_book_strategy)
def test_catering_book_get_menu_setter(instance):
    original = instance.get_menu
    instance.get_menu = original
    assert instance.get_menu == original

@given(instance=View_and_update_strategy)
@settings(max_examples=50)
def test_view_and_update_instantiation(instance):
    assert isinstance(instance, View_and_update)



@given(instance=View_and_update_strategy)
def test_view_and_update_update_order_setter(instance):
    original = instance.update_order
    instance.update_order = original
    assert instance.update_order == original



@given(instance=View_and_update_strategy)
def test_view_and_update_order_view_setter(instance):
    original = instance.order_view
    instance.order_view = original
    assert instance.order_view == original

@given(instance=Hall_strategy)
@settings(max_examples=50)
def test_hall_instantiation(instance):
    assert isinstance(instance, Hall)



@given(instance=Hall_strategy)
def test_hall_cost_per_day_setter(instance):
    original = instance.cost_per_day
    instance.cost_per_day = original
    assert instance.cost_per_day == original



@given(instance=Hall_strategy)
def test_hall_get_hall_no_setter(instance):
    original = instance.get_hall_no
    instance.get_hall_no = original
    assert instance.get_hall_no == original



@given(instance=Hall_strategy)
def test_hall_get_room_type_setter(instance):
    original = instance.get_room_type
    instance.get_room_type = original
    assert instance.get_room_type == original

@given(instance=Decoration_strategy)
@settings(max_examples=50)
def test_decoration_instantiation(instance):
    assert isinstance(instance, Decoration)



@given(instance=Decoration_strategy)
def test_decoration_Decor_type_setter(instance):
    original = instance.Decor_type
    instance.Decor_type = original
    assert instance.Decor_type == original



@given(instance=Decoration_strategy)
def test_decoration_cost_setter(instance):
    original = instance.cost
    instance.cost = original
    assert instance.cost == original



@given(instance=Decoration_strategy)
def test_decoration_Square_feet_setter(instance):
    original = instance.Square_feet
    instance.Square_feet = original
    assert instance.Square_feet == original

@given(instance=Catering_strategy)
@settings(max_examples=50)
def test_catering_instantiation(instance):
    assert isinstance(instance, Catering)



@given(instance=Catering_strategy)
def test_catering_get_menu_setter(instance):
    original = instance.get_menu
    instance.get_menu = original
    assert instance.get_menu == original



@given(instance=Catering_strategy)
def test_catering_get_cost_setter(instance):
    original = instance.get_cost
    instance.get_cost = original
    assert instance.get_cost == original

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)



@given(instance=Admin_strategy)
def test_admin_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original



@given(instance=Admin_strategy)
def test_admin_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Admin_strategy)
def test_admin_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original



@given(instance=User_strategy)
def test_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=User_strategy)
def test_user_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original

@given(instance=void_strategy)
@settings(max_examples=50)
def test_void_instantiation(instance):
    assert isinstance(instance, void)

@given(instance=LOGIN_strategy)
@settings(max_examples=50)
def test_login_instantiation(instance):
    assert isinstance(instance, LOGIN)



@given(instance=LOGIN_strategy)
def test_login_user_Name_setter(instance):
    original = instance.user_Name
    instance.user_Name = original
    assert instance.user_Name == original



@given(instance=LOGIN_strategy)
def test_login_l_Name_setter(instance):
    original = instance.l_Name
    instance.l_Name = original
    assert instance.l_Name == original



@given(instance=LOGIN_strategy)
def test_login_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=LOGIN_strategy)
def test_login_f_Name_setter(instance):
    original = instance.f_Name
    instance.f_Name = original
    assert instance.f_Name == original
