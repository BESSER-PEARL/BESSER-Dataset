import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Management_Director,
    GiftCard,
    Ticket,
    Fashion,
    Taxi,
    Travel,
    Flight,
    TransportationProduct,
    Product,
    Class,
    techStaff_DeveloperTest,
    techStaff_DatabaseAdminTest,
    techStaff_Developer,
    techStaff_DatabaseAdmin,
    Staff_Employee,
    Management_ManagerTest,
    Management_DirectorTest,
    Management_Manager,
    CardType,
    Size,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_management_director_is_not_abstract():
    assert not inspect.isabstract(Management_Director)


def test_management_director_constructor_exists():
    assert callable(Management_Director.__init__)


def test_management_director_constructor_args():
    sig = inspect.signature(Management_Director.__init__)
    params = list(sig.parameters.keys())
    assert "budget" in params, "Missing parameter 'budget'"

def test_management_director_has_budget():
    assert hasattr(Management_Director, "budget")
    descriptor = None
    for klass in Management_Director.__mro__:
        if "budget" in klass.__dict__:
            descriptor = klass.__dict__["budget"]
            break
    assert isinstance(descriptor, property)



def test_giftcard_is_not_abstract():
    assert not inspect.isabstract(GiftCard)


def test_giftcard_constructor_exists():
    assert callable(GiftCard.__init__)


def test_giftcard_constructor_args():
    sig = inspect.signature(GiftCard.__init__)
    params = list(sig.parameters.keys())
    assert "isPresent" in params, "Missing parameter 'isPresent'"
    assert "cardType" in params, "Missing parameter 'cardType'"

def test_giftcard_has_isPresent():
    assert hasattr(GiftCard, "isPresent")
    descriptor = None
    for klass in GiftCard.__mro__:
        if "isPresent" in klass.__dict__:
            descriptor = klass.__dict__["isPresent"]
            break
    assert isinstance(descriptor, property)

def test_giftcard_has_cardType():
    assert hasattr(GiftCard, "cardType")
    descriptor = None
    for klass in GiftCard.__mro__:
        if "cardType" in klass.__dict__:
            descriptor = klass.__dict__["cardType"]
            break
    assert isinstance(descriptor, property)



def test_ticket_is_not_abstract():
    assert not inspect.isabstract(Ticket)


def test_ticket_constructor_exists():
    assert callable(Ticket.__init__)


def test_ticket_constructor_args():
    sig = inspect.signature(Ticket.__init__)
    params = list(sig.parameters.keys())
    assert "eventCountry" in params, "Missing parameter 'eventCountry'"
    assert "isLastMinute" in params, "Missing parameter 'isLastMinute'"
    assert "eventCity" in params, "Missing parameter 'eventCity'"

def test_ticket_has_eventCountry():
    assert hasattr(Ticket, "eventCountry")
    descriptor = None
    for klass in Ticket.__mro__:
        if "eventCountry" in klass.__dict__:
            descriptor = klass.__dict__["eventCountry"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_isLastMinute():
    assert hasattr(Ticket, "isLastMinute")
    descriptor = None
    for klass in Ticket.__mro__:
        if "isLastMinute" in klass.__dict__:
            descriptor = klass.__dict__["isLastMinute"]
            break
    assert isinstance(descriptor, property)

def test_ticket_has_eventCity():
    assert hasattr(Ticket, "eventCity")
    descriptor = None
    for klass in Ticket.__mro__:
        if "eventCity" in klass.__dict__:
            descriptor = klass.__dict__["eventCity"]
            break
    assert isinstance(descriptor, property)



def test_fashion_is_not_abstract():
    assert not inspect.isabstract(Fashion)


def test_fashion_constructor_exists():
    assert callable(Fashion.__init__)


def test_fashion_constructor_args():
    sig = inspect.signature(Fashion.__init__)
    params = list(sig.parameters.keys())
    assert "increaseBy" in params, "Missing parameter 'increaseBy'"
    assert "size" in params, "Missing parameter 'size'"
    assert "category" in params, "Missing parameter 'category'"

def test_fashion_has_increaseBy():
    assert hasattr(Fashion, "increaseBy")
    descriptor = None
    for klass in Fashion.__mro__:
        if "increaseBy" in klass.__dict__:
            descriptor = klass.__dict__["increaseBy"]
            break
    assert isinstance(descriptor, property)

def test_fashion_has_size():
    assert hasattr(Fashion, "size")
    descriptor = None
    for klass in Fashion.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_fashion_has_category():
    assert hasattr(Fashion, "category")
    descriptor = None
    for klass in Fashion.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)



def test_taxi_is_not_abstract():
    assert not inspect.isabstract(Taxi)


def test_taxi_constructor_exists():
    assert callable(Taxi.__init__)


def test_taxi_constructor_args():
    sig = inspect.signature(Taxi.__init__)
    params = list(sig.parameters.keys())
    assert "isVip" in params, "Missing parameter 'isVip'"

def test_taxi_has_isVip():
    assert hasattr(Taxi, "isVip")
    descriptor = None
    for klass in Taxi.__mro__:
        if "isVip" in klass.__dict__:
            descriptor = klass.__dict__["isVip"]
            break
    assert isinstance(descriptor, property)



def test_travel_is_not_abstract():
    assert not inspect.isabstract(Travel)


def test_travel_constructor_exists():
    assert callable(Travel.__init__)


def test_travel_constructor_args():
    sig = inspect.signature(Travel.__init__)
    params = list(sig.parameters.keys())



def test_flight_is_not_abstract():
    assert not inspect.isabstract(Flight)


def test_flight_constructor_exists():
    assert callable(Flight.__init__)


def test_flight_constructor_args():
    sig = inspect.signature(Flight.__init__)
    params = list(sig.parameters.keys())
    assert "hasConnection" in params, "Missing parameter 'hasConnection'"

def test_flight_has_hasConnection():
    assert hasattr(Flight, "hasConnection")
    descriptor = None
    for klass in Flight.__mro__:
        if "hasConnection" in klass.__dict__:
            descriptor = klass.__dict__["hasConnection"]
            break
    assert isinstance(descriptor, property)



def test_transportationproduct_is_not_abstract():
    assert not inspect.isabstract(TransportationProduct)


def test_transportationproduct_constructor_exists():
    assert callable(TransportationProduct.__init__)


def test_transportationproduct_constructor_args():
    sig = inspect.signature(TransportationProduct.__init__)
    params = list(sig.parameters.keys())
    assert "destination" in params, "Missing parameter 'destination'"
    assert "source" in params, "Missing parameter 'source'"
    assert "distance" in params, "Missing parameter 'distance'"

def test_transportationproduct_has_destination():
    assert hasattr(TransportationProduct, "destination")
    descriptor = None
    for klass in TransportationProduct.__mro__:
        if "destination" in klass.__dict__:
            descriptor = klass.__dict__["destination"]
            break
    assert isinstance(descriptor, property)

def test_transportationproduct_has_source():
    assert hasattr(TransportationProduct, "source")
    descriptor = None
    for klass in TransportationProduct.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_transportationproduct_has_distance():
    assert hasattr(TransportationProduct, "distance")
    descriptor = None
    for klass in TransportationProduct.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)



def test_product_is_not_abstract():
    assert not inspect.isabstract(Product)


def test_product_constructor_exists():
    assert callable(Product.__init__)


def test_product_constructor_args():
    sig = inspect.signature(Product.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "creationDate" in params, "Missing parameter 'creationDate'"
    assert "supportDiscount" in params, "Missing parameter 'supportDiscount'"
    assert "price" in params, "Missing parameter 'price'"

def test_product_has_title():
    assert hasattr(Product, "title")
    descriptor = None
    for klass in Product.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_product_has_creationDate():
    assert hasattr(Product, "creationDate")
    descriptor = None
    for klass in Product.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)

def test_product_has_supportDiscount():
    assert hasattr(Product, "supportDiscount")
    descriptor = None
    for klass in Product.__mro__:
        if "supportDiscount" in klass.__dict__:
            descriptor = klass.__dict__["supportDiscount"]
            break
    assert isinstance(descriptor, property)

def test_product_has_price():
    assert hasattr(Product, "price")
    descriptor = None
    for klass in Product.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_techstaff_developertest_is_not_abstract():
    assert not inspect.isabstract(techStaff_DeveloperTest)


def test_techstaff_developertest_constructor_exists():
    assert callable(techStaff_DeveloperTest.__init__)


def test_techstaff_developertest_constructor_args():
    sig = inspect.signature(techStaff_DeveloperTest.__init__)
    params = list(sig.parameters.keys())



def test_techstaff_databaseadmintest_is_not_abstract():
    assert not inspect.isabstract(techStaff_DatabaseAdminTest)


def test_techstaff_databaseadmintest_constructor_exists():
    assert callable(techStaff_DatabaseAdminTest.__init__)


def test_techstaff_databaseadmintest_constructor_args():
    sig = inspect.signature(techStaff_DatabaseAdminTest.__init__)
    params = list(sig.parameters.keys())



def test_techstaff_developer_is_not_abstract():
    assert not inspect.isabstract(techStaff_Developer)


def test_techstaff_developer_constructor_exists():
    assert callable(techStaff_Developer.__init__)


def test_techstaff_developer_constructor_args():
    sig = inspect.signature(techStaff_Developer.__init__)
    params = list(sig.parameters.keys())



def test_techstaff_databaseadmin_is_not_abstract():
    assert not inspect.isabstract(techStaff_DatabaseAdmin)


def test_techstaff_databaseadmin_constructor_exists():
    assert callable(techStaff_DatabaseAdmin.__init__)


def test_techstaff_databaseadmin_constructor_args():
    sig = inspect.signature(techStaff_DatabaseAdmin.__init__)
    params = list(sig.parameters.keys())



def test_staff_employee_is_not_abstract():
    assert not inspect.isabstract(Staff_Employee)


def test_staff_employee_constructor_exists():
    assert callable(Staff_Employee.__init__)


def test_staff_employee_constructor_args():
    sig = inspect.signature(Staff_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "nationalInsurance" in params, "Missing parameter 'nationalInsurance'"
    assert "name" in params, "Missing parameter 'name'"
    assert "salary" in params, "Missing parameter 'salary'"

def test_staff_employee_has_nationalInsurance():
    assert hasattr(Staff_Employee, "nationalInsurance")
    descriptor = None
    for klass in Staff_Employee.__mro__:
        if "nationalInsurance" in klass.__dict__:
            descriptor = klass.__dict__["nationalInsurance"]
            break
    assert isinstance(descriptor, property)

def test_staff_employee_has_name():
    assert hasattr(Staff_Employee, "name")
    descriptor = None
    for klass in Staff_Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_staff_employee_has_salary():
    assert hasattr(Staff_Employee, "salary")
    descriptor = None
    for klass in Staff_Employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)



def test_management_managertest_is_not_abstract():
    assert not inspect.isabstract(Management_ManagerTest)


def test_management_managertest_constructor_exists():
    assert callable(Management_ManagerTest.__init__)


def test_management_managertest_constructor_args():
    sig = inspect.signature(Management_ManagerTest.__init__)
    params = list(sig.parameters.keys())



def test_management_directortest_is_not_abstract():
    assert not inspect.isabstract(Management_DirectorTest)


def test_management_directortest_constructor_exists():
    assert callable(Management_DirectorTest.__init__)


def test_management_directortest_constructor_args():
    sig = inspect.signature(Management_DirectorTest.__init__)
    params = list(sig.parameters.keys())



def test_management_manager_is_not_abstract():
    assert not inspect.isabstract(Management_Manager)


def test_management_manager_constructor_exists():
    assert callable(Management_Manager.__init__)


def test_management_manager_constructor_args():
    sig = inspect.signature(Management_Manager.__init__)
    params = list(sig.parameters.keys())
    assert "deptName" in params, "Missing parameter 'deptName'"

def test_management_manager_has_deptName():
    assert hasattr(Management_Manager, "deptName")
    descriptor = None
    for klass in Management_Manager.__mro__:
        if "deptName" in klass.__dict__:
            descriptor = klass.__dict__["deptName"]
            break
    assert isinstance(descriptor, property)

def test_cardtype_exists():
    # Check that the Enumeration exists
    assert CardType is not None

def test_cardtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CardType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CardType"

def test_size_exists():
    # Check that the Enumeration exists
    assert Size is not None

def test_size_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Size]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Size"


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
Management_Director_strategy = st.builds(
    Management_Director,
    budget=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
GiftCard_strategy = st.builds(
    GiftCard,
    isPresent=
        st.booleans(),
    cardType=
        st.none()
)
Ticket_strategy = st.builds(
    Ticket,
    eventCountry=
        safe_text,
    isLastMinute=
        st.booleans(),
    eventCity=
        safe_text
)
Fashion_strategy = st.builds(
    Fashion,
    increaseBy=
        st.integers(),
    size=
        st.none(),
    category=
        safe_text
)
Taxi_strategy = st.builds(
    Taxi,
    isVip=
        st.booleans()
)
Travel_strategy = st.builds(
    Travel,
)
Flight_strategy = st.builds(
    Flight,
    hasConnection=
        st.booleans()
)
TransportationProduct_strategy = st.builds(
    TransportationProduct,
    destination=
        safe_text,
    source=
        safe_text,
    distance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Product_strategy = st.builds(
    Product,
    title=
        safe_text,
    creationDate=
        st.dates(),
    supportDiscount=
        st.booleans(),
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Class_strategy = st.builds(
    Class,
)
techStaff_DeveloperTest_strategy = st.builds(
    techStaff_DeveloperTest,
)
techStaff_DatabaseAdminTest_strategy = st.builds(
    techStaff_DatabaseAdminTest,
)
techStaff_Developer_strategy = st.builds(
    techStaff_Developer,
)
techStaff_DatabaseAdmin_strategy = st.builds(
    techStaff_DatabaseAdmin,
)
Staff_Employee_strategy = st.builds(
    Staff_Employee,
    nationalInsurance=
        safe_text,
    name=
        safe_text,
    salary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Management_ManagerTest_strategy = st.builds(
    Management_ManagerTest,
)
Management_DirectorTest_strategy = st.builds(
    Management_DirectorTest,
)
Management_Manager_strategy = st.builds(
    Management_Manager,
    deptName=
        safe_text
)

@given(instance=Management_Director_strategy)
@settings(max_examples=50)
def test_management_director_instantiation(instance):
    assert isinstance(instance, Management_Director)



@given(instance=Management_Director_strategy)
def test_management_director_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original

@given(instance=GiftCard_strategy)
@settings(max_examples=50)
def test_giftcard_instantiation(instance):
    assert isinstance(instance, GiftCard)



@given(instance=GiftCard_strategy)
def test_giftcard_isPresent_setter(instance):
    original = instance.isPresent
    instance.isPresent = original
    assert instance.isPresent == original



@given(instance=GiftCard_strategy)
def test_giftcard_cardType_setter(instance):
    original = instance.cardType
    instance.cardType = original
    assert instance.cardType == original

@given(instance=Ticket_strategy)
@settings(max_examples=50)
def test_ticket_instantiation(instance):
    assert isinstance(instance, Ticket)



@given(instance=Ticket_strategy)
def test_ticket_eventCountry_setter(instance):
    original = instance.eventCountry
    instance.eventCountry = original
    assert instance.eventCountry == original



@given(instance=Ticket_strategy)
def test_ticket_isLastMinute_setter(instance):
    original = instance.isLastMinute
    instance.isLastMinute = original
    assert instance.isLastMinute == original



@given(instance=Ticket_strategy)
def test_ticket_eventCity_setter(instance):
    original = instance.eventCity
    instance.eventCity = original
    assert instance.eventCity == original

@given(instance=Fashion_strategy)
@settings(max_examples=50)
def test_fashion_instantiation(instance):
    assert isinstance(instance, Fashion)



@given(instance=Fashion_strategy)
def test_fashion_increaseBy_setter(instance):
    original = instance.increaseBy
    instance.increaseBy = original
    assert instance.increaseBy == original



@given(instance=Fashion_strategy)
def test_fashion_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=Fashion_strategy)
def test_fashion_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=Taxi_strategy)
@settings(max_examples=50)
def test_taxi_instantiation(instance):
    assert isinstance(instance, Taxi)



@given(instance=Taxi_strategy)
def test_taxi_isVip_setter(instance):
    original = instance.isVip
    instance.isVip = original
    assert instance.isVip == original

@given(instance=Travel_strategy)
@settings(max_examples=50)
def test_travel_instantiation(instance):
    assert isinstance(instance, Travel)

@given(instance=Flight_strategy)
@settings(max_examples=50)
def test_flight_instantiation(instance):
    assert isinstance(instance, Flight)



@given(instance=Flight_strategy)
def test_flight_hasConnection_setter(instance):
    original = instance.hasConnection
    instance.hasConnection = original
    assert instance.hasConnection == original

@given(instance=TransportationProduct_strategy)
@settings(max_examples=50)
def test_transportationproduct_instantiation(instance):
    assert isinstance(instance, TransportationProduct)



@given(instance=TransportationProduct_strategy)
def test_transportationproduct_destination_setter(instance):
    original = instance.destination
    instance.destination = original
    assert instance.destination == original



@given(instance=TransportationProduct_strategy)
def test_transportationproduct_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original



@given(instance=TransportationProduct_strategy)
def test_transportationproduct_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=Product_strategy)
@settings(max_examples=50)
def test_product_instantiation(instance):
    assert isinstance(instance, Product)



@given(instance=Product_strategy)
def test_product_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=Product_strategy)
def test_product_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original



@given(instance=Product_strategy)
def test_product_supportDiscount_setter(instance):
    original = instance.supportDiscount
    instance.supportDiscount = original
    assert instance.supportDiscount == original



@given(instance=Product_strategy)
def test_product_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=techStaff_DeveloperTest_strategy)
@settings(max_examples=50)
def test_techstaff_developertest_instantiation(instance):
    assert isinstance(instance, techStaff_DeveloperTest)

@given(instance=techStaff_DatabaseAdminTest_strategy)
@settings(max_examples=50)
def test_techstaff_databaseadmintest_instantiation(instance):
    assert isinstance(instance, techStaff_DatabaseAdminTest)

@given(instance=techStaff_Developer_strategy)
@settings(max_examples=50)
def test_techstaff_developer_instantiation(instance):
    assert isinstance(instance, techStaff_Developer)

@given(instance=techStaff_DatabaseAdmin_strategy)
@settings(max_examples=50)
def test_techstaff_databaseadmin_instantiation(instance):
    assert isinstance(instance, techStaff_DatabaseAdmin)

@given(instance=Staff_Employee_strategy)
@settings(max_examples=50)
def test_staff_employee_instantiation(instance):
    assert isinstance(instance, Staff_Employee)



@given(instance=Staff_Employee_strategy)
def test_staff_employee_nationalInsurance_setter(instance):
    original = instance.nationalInsurance
    instance.nationalInsurance = original
    assert instance.nationalInsurance == original



@given(instance=Staff_Employee_strategy)
def test_staff_employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Staff_Employee_strategy)
def test_staff_employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original

@given(instance=Management_ManagerTest_strategy)
@settings(max_examples=50)
def test_management_managertest_instantiation(instance):
    assert isinstance(instance, Management_ManagerTest)

@given(instance=Management_DirectorTest_strategy)
@settings(max_examples=50)
def test_management_directortest_instantiation(instance):
    assert isinstance(instance, Management_DirectorTest)

@given(instance=Management_Manager_strategy)
@settings(max_examples=50)
def test_management_manager_instantiation(instance):
    assert isinstance(instance, Management_Manager)



@given(instance=Management_Manager_strategy)
def test_management_manager_deptName_setter(instance):
    original = instance.deptName
    instance.deptName = original
    assert instance.deptName == original
