import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Building,
    Elevator_Button,
    Floor_Button,
    Data,
    People,
    Button,
    Door,
    Elevator,
    ElevatorController,
    ClassC,
    BankAccount,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_building_is_not_abstract():
    assert not inspect.isabstract(Building)


def test_building_constructor_exists():
    assert callable(Building.__init__)


def test_building_constructor_args():
    sig = inspect.signature(Building.__init__)
    params = list(sig.parameters.keys())



def test_elevator_button_is_not_abstract():
    assert not inspect.isabstract(Elevator_Button)


def test_elevator_button_constructor_exists():
    assert callable(Elevator_Button.__init__)


def test_elevator_button_constructor_args():
    sig = inspect.signature(Elevator_Button.__init__)
    params = list(sig.parameters.keys())



def test_floor_button_is_not_abstract():
    assert not inspect.isabstract(Floor_Button)


def test_floor_button_constructor_exists():
    assert callable(Floor_Button.__init__)


def test_floor_button_constructor_args():
    sig = inspect.signature(Floor_Button.__init__)
    params = list(sig.parameters.keys())



def test_data_is_not_abstract():
    assert not inspect.isabstract(Data)


def test_data_constructor_exists():
    assert callable(Data.__init__)


def test_data_constructor_args():
    sig = inspect.signature(Data.__init__)
    params = list(sig.parameters.keys())



def test_people_is_not_abstract():
    assert not inspect.isabstract(People)


def test_people_constructor_exists():
    assert callable(People.__init__)


def test_people_constructor_args():
    sig = inspect.signature(People.__init__)
    params = list(sig.parameters.keys())



def test_button_is_not_abstract():
    assert not inspect.isabstract(Button)


def test_button_constructor_exists():
    assert callable(Button.__init__)


def test_button_constructor_args():
    sig = inspect.signature(Button.__init__)
    params = list(sig.parameters.keys())



def test_door_is_not_abstract():
    assert not inspect.isabstract(Door)


def test_door_constructor_exists():
    assert callable(Door.__init__)


def test_door_constructor_args():
    sig = inspect.signature(Door.__init__)
    params = list(sig.parameters.keys())



def test_elevator_is_not_abstract():
    assert not inspect.isabstract(Elevator)


def test_elevator_constructor_exists():
    assert callable(Elevator.__init__)


def test_elevator_constructor_args():
    sig = inspect.signature(Elevator.__init__)
    params = list(sig.parameters.keys())



def test_elevatorcontroller_is_not_abstract():
    assert not inspect.isabstract(ElevatorController)


def test_elevatorcontroller_constructor_exists():
    assert callable(ElevatorController.__init__)


def test_elevatorcontroller_constructor_args():
    sig = inspect.signature(ElevatorController.__init__)
    params = list(sig.parameters.keys())



def test_classc_is_not_abstract():
    assert not inspect.isabstract(ClassC)


def test_classc_constructor_exists():
    assert callable(ClassC.__init__)


def test_classc_constructor_args():
    sig = inspect.signature(ClassC.__init__)
    params = list(sig.parameters.keys())
    assert "privateAttribute" in params, "Missing parameter 'privateAttribute'"
    assert "packageAttribute" in params, "Missing parameter 'packageAttribute'"
    assert "publicAttribute" in params, "Missing parameter 'publicAttribute'"
    assert "protectedAttribute" in params, "Missing parameter 'protectedAttribute'"

def test_classc_has_privateAttribute():
    assert hasattr(ClassC, "privateAttribute")
    descriptor = None
    for klass in ClassC.__mro__:
        if "privateAttribute" in klass.__dict__:
            descriptor = klass.__dict__["privateAttribute"]
            break
    assert isinstance(descriptor, property)

def test_classc_has_packageAttribute():
    assert hasattr(ClassC, "packageAttribute")
    descriptor = None
    for klass in ClassC.__mro__:
        if "packageAttribute" in klass.__dict__:
            descriptor = klass.__dict__["packageAttribute"]
            break
    assert isinstance(descriptor, property)

def test_classc_has_publicAttribute():
    assert hasattr(ClassC, "publicAttribute")
    descriptor = None
    for klass in ClassC.__mro__:
        if "publicAttribute" in klass.__dict__:
            descriptor = klass.__dict__["publicAttribute"]
            break
    assert isinstance(descriptor, property)

def test_classc_has_protectedAttribute():
    assert hasattr(ClassC, "protectedAttribute")
    descriptor = None
    for klass in ClassC.__mro__:
        if "protectedAttribute" in klass.__dict__:
            descriptor = klass.__dict__["protectedAttribute"]
            break
    assert isinstance(descriptor, property)



def test_bankaccount_is_not_abstract():
    assert not inspect.isabstract(BankAccount)


def test_bankaccount_constructor_exists():
    assert callable(BankAccount.__init__)


def test_bankaccount_constructor_args():
    sig = inspect.signature(BankAccount.__init__)
    params = list(sig.parameters.keys())
    assert "balance" in params, "Missing parameter 'balance'"
    assert "ownerName" in params, "Missing parameter 'ownerName'"

def test_bankaccount_has_balance():
    assert hasattr(BankAccount, "balance")
    descriptor = None
    for klass in BankAccount.__mro__:
        if "balance" in klass.__dict__:
            descriptor = klass.__dict__["balance"]
            break
    assert isinstance(descriptor, property)

def test_bankaccount_has_ownerName():
    assert hasattr(BankAccount, "ownerName")
    descriptor = None
    for klass in BankAccount.__mro__:
        if "ownerName" in klass.__dict__:
            descriptor = klass.__dict__["ownerName"]
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
Building_strategy = st.builds(
    Building,
)
Elevator_Button_strategy = st.builds(
    Elevator_Button,
)
Floor_Button_strategy = st.builds(
    Floor_Button,
)
Data_strategy = st.builds(
    Data,
)
People_strategy = st.builds(
    People,
)
Button_strategy = st.builds(
    Button,
)
Door_strategy = st.builds(
    Door,
)
Elevator_strategy = st.builds(
    Elevator,
)
ElevatorController_strategy = st.builds(
    ElevatorController,
)
ClassC_strategy = st.builds(
    ClassC,
    privateAttribute=
        st.integers(),
    packageAttribute=
        safe_text,
    publicAttribute=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    protectedAttribute=
        safe_text
)
BankAccount_strategy = st.builds(
    BankAccount,
    balance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    ownerName=
        safe_text
)

@given(instance=Building_strategy)
@settings(max_examples=50)
def test_building_instantiation(instance):
    assert isinstance(instance, Building)

@given(instance=Elevator_Button_strategy)
@settings(max_examples=50)
def test_elevator_button_instantiation(instance):
    assert isinstance(instance, Elevator_Button)

@given(instance=Floor_Button_strategy)
@settings(max_examples=50)
def test_floor_button_instantiation(instance):
    assert isinstance(instance, Floor_Button)

@given(instance=Data_strategy)
@settings(max_examples=50)
def test_data_instantiation(instance):
    assert isinstance(instance, Data)

@given(instance=People_strategy)
@settings(max_examples=50)
def test_people_instantiation(instance):
    assert isinstance(instance, People)

@given(instance=Button_strategy)
@settings(max_examples=50)
def test_button_instantiation(instance):
    assert isinstance(instance, Button)

@given(instance=Door_strategy)
@settings(max_examples=50)
def test_door_instantiation(instance):
    assert isinstance(instance, Door)

@given(instance=Elevator_strategy)
@settings(max_examples=50)
def test_elevator_instantiation(instance):
    assert isinstance(instance, Elevator)

@given(instance=ElevatorController_strategy)
@settings(max_examples=50)
def test_elevatorcontroller_instantiation(instance):
    assert isinstance(instance, ElevatorController)

@given(instance=ClassC_strategy)
@settings(max_examples=50)
def test_classc_instantiation(instance):
    assert isinstance(instance, ClassC)



@given(instance=ClassC_strategy)
def test_classc_privateAttribute_setter(instance):
    original = instance.privateAttribute
    instance.privateAttribute = original
    assert instance.privateAttribute == original



@given(instance=ClassC_strategy)
def test_classc_packageAttribute_setter(instance):
    original = instance.packageAttribute
    instance.packageAttribute = original
    assert instance.packageAttribute == original



@given(instance=ClassC_strategy)
def test_classc_publicAttribute_setter(instance):
    original = instance.publicAttribute
    instance.publicAttribute = original
    assert instance.publicAttribute == original



@given(instance=ClassC_strategy)
def test_classc_protectedAttribute_setter(instance):
    original = instance.protectedAttribute
    instance.protectedAttribute = original
    assert instance.protectedAttribute == original

@given(instance=BankAccount_strategy)
@settings(max_examples=50)
def test_bankaccount_instantiation(instance):
    assert isinstance(instance, BankAccount)



@given(instance=BankAccount_strategy)
def test_bankaccount_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original



@given(instance=BankAccount_strategy)
def test_bankaccount_ownerName_setter(instance):
    original = instance.ownerName
    instance.ownerName = original
    assert instance.ownerName == original
