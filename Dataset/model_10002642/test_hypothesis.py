import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Generate_bill_external,
    Maintain_car_information_external,
    View_daily_rental_reports_external,
    View_monthly_rental_reports_external,
    Book_external,
    Select_car_external,
    Search_car_external,
    Register_external,
    Login_external,
    Pay_bill_external,
    UseCase_UseCase,
    MyClass,
    Manager_Actor,
    Employee_Actor,
    Insurance_company_Actor,
    Customer_Actor,
    Car_Rental_Component,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_generate_bill_external_is_not_abstract():
    assert not inspect.isabstract(Generate_bill_external)


def test_generate_bill_external_constructor_exists():
    assert callable(Generate_bill_external.__init__)


def test_generate_bill_external_constructor_args():
    sig = inspect.signature(Generate_bill_external.__init__)
    params = list(sig.parameters.keys())



def test_maintain_car_information_external_is_not_abstract():
    assert not inspect.isabstract(Maintain_car_information_external)


def test_maintain_car_information_external_constructor_exists():
    assert callable(Maintain_car_information_external.__init__)


def test_maintain_car_information_external_constructor_args():
    sig = inspect.signature(Maintain_car_information_external.__init__)
    params = list(sig.parameters.keys())



def test_view_daily_rental_reports_external_is_not_abstract():
    assert not inspect.isabstract(View_daily_rental_reports_external)


def test_view_daily_rental_reports_external_constructor_exists():
    assert callable(View_daily_rental_reports_external.__init__)


def test_view_daily_rental_reports_external_constructor_args():
    sig = inspect.signature(View_daily_rental_reports_external.__init__)
    params = list(sig.parameters.keys())



def test_view_monthly_rental_reports_external_is_not_abstract():
    assert not inspect.isabstract(View_monthly_rental_reports_external)


def test_view_monthly_rental_reports_external_constructor_exists():
    assert callable(View_monthly_rental_reports_external.__init__)


def test_view_monthly_rental_reports_external_constructor_args():
    sig = inspect.signature(View_monthly_rental_reports_external.__init__)
    params = list(sig.parameters.keys())



def test_book_external_is_not_abstract():
    assert not inspect.isabstract(Book_external)


def test_book_external_constructor_exists():
    assert callable(Book_external.__init__)


def test_book_external_constructor_args():
    sig = inspect.signature(Book_external.__init__)
    params = list(sig.parameters.keys())



def test_select_car_external_is_not_abstract():
    assert not inspect.isabstract(Select_car_external)


def test_select_car_external_constructor_exists():
    assert callable(Select_car_external.__init__)


def test_select_car_external_constructor_args():
    sig = inspect.signature(Select_car_external.__init__)
    params = list(sig.parameters.keys())



def test_search_car_external_is_not_abstract():
    assert not inspect.isabstract(Search_car_external)


def test_search_car_external_constructor_exists():
    assert callable(Search_car_external.__init__)


def test_search_car_external_constructor_args():
    sig = inspect.signature(Search_car_external.__init__)
    params = list(sig.parameters.keys())



def test_register_external_is_not_abstract():
    assert not inspect.isabstract(Register_external)


def test_register_external_constructor_exists():
    assert callable(Register_external.__init__)


def test_register_external_constructor_args():
    sig = inspect.signature(Register_external.__init__)
    params = list(sig.parameters.keys())



def test_login_external_is_not_abstract():
    assert not inspect.isabstract(Login_external)


def test_login_external_constructor_exists():
    assert callable(Login_external.__init__)


def test_login_external_constructor_args():
    sig = inspect.signature(Login_external.__init__)
    params = list(sig.parameters.keys())



def test_pay_bill_external_is_not_abstract():
    assert not inspect.isabstract(Pay_bill_external)


def test_pay_bill_external_constructor_exists():
    assert callable(Pay_bill_external.__init__)


def test_pay_bill_external_constructor_args():
    sig = inspect.signature(Pay_bill_external.__init__)
    params = list(sig.parameters.keys())



def test_usecase_usecase_is_not_abstract():
    assert not inspect.isabstract(UseCase_UseCase)


def test_usecase_usecase_constructor_exists():
    assert callable(UseCase_UseCase.__init__)


def test_usecase_usecase_constructor_args():
    sig = inspect.signature(UseCase_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_myclass_is_not_abstract():
    assert not inspect.isabstract(MyClass)


def test_myclass_constructor_exists():
    assert callable(MyClass.__init__)


def test_myclass_constructor_args():
    sig = inspect.signature(MyClass.__init__)
    params = list(sig.parameters.keys())



def test_manager_actor_is_not_abstract():
    assert not inspect.isabstract(Manager_Actor)


def test_manager_actor_constructor_exists():
    assert callable(Manager_Actor.__init__)


def test_manager_actor_constructor_args():
    sig = inspect.signature(Manager_Actor.__init__)
    params = list(sig.parameters.keys())



def test_employee_actor_is_not_abstract():
    assert not inspect.isabstract(Employee_Actor)


def test_employee_actor_constructor_exists():
    assert callable(Employee_Actor.__init__)


def test_employee_actor_constructor_args():
    sig = inspect.signature(Employee_Actor.__init__)
    params = list(sig.parameters.keys())



def test_insurance_company_actor_is_not_abstract():
    assert not inspect.isabstract(Insurance_company_Actor)


def test_insurance_company_actor_constructor_exists():
    assert callable(Insurance_company_Actor.__init__)


def test_insurance_company_actor_constructor_args():
    sig = inspect.signature(Insurance_company_Actor.__init__)
    params = list(sig.parameters.keys())



def test_customer_actor_is_not_abstract():
    assert not inspect.isabstract(Customer_Actor)


def test_customer_actor_constructor_exists():
    assert callable(Customer_Actor.__init__)


def test_customer_actor_constructor_args():
    sig = inspect.signature(Customer_Actor.__init__)
    params = list(sig.parameters.keys())



def test_car_rental_component_is_not_abstract():
    assert not inspect.isabstract(Car_Rental_Component)


def test_car_rental_component_constructor_exists():
    assert callable(Car_Rental_Component.__init__)


def test_car_rental_component_constructor_args():
    sig = inspect.signature(Car_Rental_Component.__init__)
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
Generate_bill_external_strategy = st.builds(
    Generate_bill_external,
)
Maintain_car_information_external_strategy = st.builds(
    Maintain_car_information_external,
)
View_daily_rental_reports_external_strategy = st.builds(
    View_daily_rental_reports_external,
)
View_monthly_rental_reports_external_strategy = st.builds(
    View_monthly_rental_reports_external,
)
Book_external_strategy = st.builds(
    Book_external,
)
Select_car_external_strategy = st.builds(
    Select_car_external,
)
Search_car_external_strategy = st.builds(
    Search_car_external,
)
Register_external_strategy = st.builds(
    Register_external,
)
Login_external_strategy = st.builds(
    Login_external,
)
Pay_bill_external_strategy = st.builds(
    Pay_bill_external,
)
UseCase_UseCase_strategy = st.builds(
    UseCase_UseCase,
)
MyClass_strategy = st.builds(
    MyClass,
)
Manager_Actor_strategy = st.builds(
    Manager_Actor,
)
Employee_Actor_strategy = st.builds(
    Employee_Actor,
)
Insurance_company_Actor_strategy = st.builds(
    Insurance_company_Actor,
)
Customer_Actor_strategy = st.builds(
    Customer_Actor,
)
Car_Rental_Component_strategy = st.builds(
    Car_Rental_Component,
)

@given(instance=Generate_bill_external_strategy)
@settings(max_examples=50)
def test_generate_bill_external_instantiation(instance):
    assert isinstance(instance, Generate_bill_external)

@given(instance=Maintain_car_information_external_strategy)
@settings(max_examples=50)
def test_maintain_car_information_external_instantiation(instance):
    assert isinstance(instance, Maintain_car_information_external)

@given(instance=View_daily_rental_reports_external_strategy)
@settings(max_examples=50)
def test_view_daily_rental_reports_external_instantiation(instance):
    assert isinstance(instance, View_daily_rental_reports_external)

@given(instance=View_monthly_rental_reports_external_strategy)
@settings(max_examples=50)
def test_view_monthly_rental_reports_external_instantiation(instance):
    assert isinstance(instance, View_monthly_rental_reports_external)

@given(instance=Book_external_strategy)
@settings(max_examples=50)
def test_book_external_instantiation(instance):
    assert isinstance(instance, Book_external)

@given(instance=Select_car_external_strategy)
@settings(max_examples=50)
def test_select_car_external_instantiation(instance):
    assert isinstance(instance, Select_car_external)

@given(instance=Search_car_external_strategy)
@settings(max_examples=50)
def test_search_car_external_instantiation(instance):
    assert isinstance(instance, Search_car_external)

@given(instance=Register_external_strategy)
@settings(max_examples=50)
def test_register_external_instantiation(instance):
    assert isinstance(instance, Register_external)

@given(instance=Login_external_strategy)
@settings(max_examples=50)
def test_login_external_instantiation(instance):
    assert isinstance(instance, Login_external)

@given(instance=Pay_bill_external_strategy)
@settings(max_examples=50)
def test_pay_bill_external_instantiation(instance):
    assert isinstance(instance, Pay_bill_external)

@given(instance=UseCase_UseCase_strategy)
@settings(max_examples=50)
def test_usecase_usecase_instantiation(instance):
    assert isinstance(instance, UseCase_UseCase)

@given(instance=MyClass_strategy)
@settings(max_examples=50)
def test_myclass_instantiation(instance):
    assert isinstance(instance, MyClass)

@given(instance=Manager_Actor_strategy)
@settings(max_examples=50)
def test_manager_actor_instantiation(instance):
    assert isinstance(instance, Manager_Actor)

@given(instance=Employee_Actor_strategy)
@settings(max_examples=50)
def test_employee_actor_instantiation(instance):
    assert isinstance(instance, Employee_Actor)

@given(instance=Insurance_company_Actor_strategy)
@settings(max_examples=50)
def test_insurance_company_actor_instantiation(instance):
    assert isinstance(instance, Insurance_company_Actor)

@given(instance=Customer_Actor_strategy)
@settings(max_examples=50)
def test_customer_actor_instantiation(instance):
    assert isinstance(instance, Customer_Actor)

@given(instance=Car_Rental_Component_strategy)
@settings(max_examples=50)
def test_car_rental_component_instantiation(instance):
    assert isinstance(instance, Car_Rental_Component)
