import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    test_ConfigurationModel,
    test_TestModel,
    test_AddressModel,
    Gender,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test_configurationmodel_is_not_abstract():
    assert not inspect.isabstract(test_ConfigurationModel)


def test_test_configurationmodel_constructor_exists():
    assert callable(test_ConfigurationModel.__init__)


def test_test_configurationmodel_constructor_args():
    sig = inspect.signature(test_ConfigurationModel.__init__)
    params = list(sig.parameters.keys())



def test_test_testmodel_is_not_abstract():
    assert not inspect.isabstract(test_TestModel)


def test_test_testmodel_constructor_exists():
    assert callable(test_TestModel.__init__)


def test_test_testmodel_constructor_args():
    sig = inspect.signature(test_TestModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "childCount" in params, "Missing parameter 'childCount'"
    assert "overdrawAccount" in params, "Missing parameter 'overdrawAccount'"
    assert "accountBalance" in params, "Missing parameter 'accountBalance'"
    assert "birthDate" in params, "Missing parameter 'birthDate'"
    assert "gender" in params, "Missing parameter 'gender'"
    assert "isSelectable" in params, "Missing parameter 'isSelectable'"
    assert "age" in params, "Missing parameter 'age'"

def test_test_testmodel_has_name():
    assert hasattr(test_TestModel, "name")
    descriptor = None
    for klass in test_TestModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_test_testmodel_has_childCount():
    assert hasattr(test_TestModel, "childCount")
    descriptor = None
    for klass in test_TestModel.__mro__:
        if "childCount" in klass.__dict__:
            descriptor = klass.__dict__["childCount"]
            break
    assert isinstance(descriptor, property)

def test_test_testmodel_has_overdrawAccount():
    assert hasattr(test_TestModel, "overdrawAccount")
    descriptor = None
    for klass in test_TestModel.__mro__:
        if "overdrawAccount" in klass.__dict__:
            descriptor = klass.__dict__["overdrawAccount"]
            break
    assert isinstance(descriptor, property)

def test_test_testmodel_has_accountBalance():
    assert hasattr(test_TestModel, "accountBalance")
    descriptor = None
    for klass in test_TestModel.__mro__:
        if "accountBalance" in klass.__dict__:
            descriptor = klass.__dict__["accountBalance"]
            break
    assert isinstance(descriptor, property)

def test_test_testmodel_has_birthDate():
    assert hasattr(test_TestModel, "birthDate")
    descriptor = None
    for klass in test_TestModel.__mro__:
        if "birthDate" in klass.__dict__:
            descriptor = klass.__dict__["birthDate"]
            break
    assert isinstance(descriptor, property)

def test_test_testmodel_has_gender():
    assert hasattr(test_TestModel, "gender")
    descriptor = None
    for klass in test_TestModel.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)

def test_test_testmodel_has_isSelectable():
    assert hasattr(test_TestModel, "isSelectable")
    descriptor = None
    for klass in test_TestModel.__mro__:
        if "isSelectable" in klass.__dict__:
            descriptor = klass.__dict__["isSelectable"]
            break
    assert isinstance(descriptor, property)

def test_test_testmodel_has_age():
    assert hasattr(test_TestModel, "age")
    descriptor = None
    for klass in test_TestModel.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)



def test_test_addressmodel_is_not_abstract():
    assert not inspect.isabstract(test_AddressModel)


def test_test_addressmodel_constructor_exists():
    assert callable(test_AddressModel.__init__)


def test_test_addressmodel_constructor_args():
    sig = inspect.signature(test_AddressModel.__init__)
    params = list(sig.parameters.keys())
    assert "zipCode" in params, "Missing parameter 'zipCode'"
    assert "validTo" in params, "Missing parameter 'validTo'"
    assert "street" in params, "Missing parameter 'street'"
    assert "validFrom" in params, "Missing parameter 'validFrom'"
    assert "differentPostAddress" in params, "Missing parameter 'differentPostAddress'"
    assert "houseNumber" in params, "Missing parameter 'houseNumber'"

def test_test_addressmodel_has_zipCode():
    assert hasattr(test_AddressModel, "zipCode")
    descriptor = None
    for klass in test_AddressModel.__mro__:
        if "zipCode" in klass.__dict__:
            descriptor = klass.__dict__["zipCode"]
            break
    assert isinstance(descriptor, property)

def test_test_addressmodel_has_validTo():
    assert hasattr(test_AddressModel, "validTo")
    descriptor = None
    for klass in test_AddressModel.__mro__:
        if "validTo" in klass.__dict__:
            descriptor = klass.__dict__["validTo"]
            break
    assert isinstance(descriptor, property)

def test_test_addressmodel_has_street():
    assert hasattr(test_AddressModel, "street")
    descriptor = None
    for klass in test_AddressModel.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_test_addressmodel_has_validFrom():
    assert hasattr(test_AddressModel, "validFrom")
    descriptor = None
    for klass in test_AddressModel.__mro__:
        if "validFrom" in klass.__dict__:
            descriptor = klass.__dict__["validFrom"]
            break
    assert isinstance(descriptor, property)

def test_test_addressmodel_has_differentPostAddress():
    assert hasattr(test_AddressModel, "differentPostAddress")
    descriptor = None
    for klass in test_AddressModel.__mro__:
        if "differentPostAddress" in klass.__dict__:
            descriptor = klass.__dict__["differentPostAddress"]
            break
    assert isinstance(descriptor, property)

def test_test_addressmodel_has_houseNumber():
    assert hasattr(test_AddressModel, "houseNumber")
    descriptor = None
    for klass in test_AddressModel.__mro__:
        if "houseNumber" in klass.__dict__:
            descriptor = klass.__dict__["houseNumber"]
            break
    assert isinstance(descriptor, property)

def test_gender_exists():
    # Check that the Enumeration exists
    assert Gender is not None

def test_gender_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Gender]
    expected_literals = [
        "MALE",
        "FEMALE",
        "UNKNOWN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Gender"


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
test_ConfigurationModel_strategy = st.builds(
    test_ConfigurationModel,
)
test_TestModel_strategy = st.builds(
    test_TestModel,
    name=
        safe_text,
    childCount=
        safe_text,
    overdrawAccount=
        safe_text,
    accountBalance=
        safe_text,
    birthDate=
        st.dates(),
    gender=
        safe_text,
    isSelectable=
        safe_text,
    age=
        st.integers()
)
test_AddressModel_strategy = st.builds(
    test_AddressModel,
    zipCode=
        safe_text,
    validTo=
        st.dates(),
    street=
        safe_text,
    validFrom=
        st.dates(),
    differentPostAddress=
        st.booleans(),
    houseNumber=
        safe_text
)

@given(instance=test_ConfigurationModel_strategy)
@settings(max_examples=50)
def test_test_configurationmodel_instantiation(instance):
    assert isinstance(instance, test_ConfigurationModel)

@given(instance=test_TestModel_strategy)
@settings(max_examples=50)
def test_test_testmodel_instantiation(instance):
    assert isinstance(instance, test_TestModel)



@given(instance=test_TestModel_strategy)
def test_test_testmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=test_TestModel_strategy)
def test_test_testmodel_childCount_setter(instance):
    original = instance.childCount
    instance.childCount = original
    assert instance.childCount == original



@given(instance=test_TestModel_strategy)
def test_test_testmodel_overdrawAccount_setter(instance):
    original = instance.overdrawAccount
    instance.overdrawAccount = original
    assert instance.overdrawAccount == original



@given(instance=test_TestModel_strategy)
def test_test_testmodel_accountBalance_setter(instance):
    original = instance.accountBalance
    instance.accountBalance = original
    assert instance.accountBalance == original



@given(instance=test_TestModel_strategy)
def test_test_testmodel_birthDate_setter(instance):
    original = instance.birthDate
    instance.birthDate = original
    assert instance.birthDate == original



@given(instance=test_TestModel_strategy)
def test_test_testmodel_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=test_TestModel_strategy)
def test_test_testmodel_isSelectable_setter(instance):
    original = instance.isSelectable
    instance.isSelectable = original
    assert instance.isSelectable == original



@given(instance=test_TestModel_strategy)
def test_test_testmodel_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=test_AddressModel_strategy)
@settings(max_examples=50)
def test_test_addressmodel_instantiation(instance):
    assert isinstance(instance, test_AddressModel)



@given(instance=test_AddressModel_strategy)
def test_test_addressmodel_zipCode_setter(instance):
    original = instance.zipCode
    instance.zipCode = original
    assert instance.zipCode == original



@given(instance=test_AddressModel_strategy)
def test_test_addressmodel_validTo_setter(instance):
    original = instance.validTo
    instance.validTo = original
    assert instance.validTo == original



@given(instance=test_AddressModel_strategy)
def test_test_addressmodel_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original



@given(instance=test_AddressModel_strategy)
def test_test_addressmodel_validFrom_setter(instance):
    original = instance.validFrom
    instance.validFrom = original
    assert instance.validFrom == original



@given(instance=test_AddressModel_strategy)
def test_test_addressmodel_differentPostAddress_setter(instance):
    original = instance.differentPostAddress
    instance.differentPostAddress = original
    assert instance.differentPostAddress == original



@given(instance=test_AddressModel_strategy)
def test_test_addressmodel_houseNumber_setter(instance):
    original = instance.houseNumber
    instance.houseNumber = original
    assert instance.houseNumber == original
