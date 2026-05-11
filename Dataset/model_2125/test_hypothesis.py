import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    test::ConfigurationModel,
    test::TestModel,
    test::AddressModel,
    Gender,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test::configurationmodel_is_not_abstract():
    assert not inspect.isabstract(test::ConfigurationModel)


def test_test::configurationmodel_constructor_exists():
    assert callable(test::ConfigurationModel.__init__)


def test_test::configurationmodel_constructor_args():
    sig = inspect.signature(test::ConfigurationModel.__init__)
    params = list(sig.parameters.keys())



def test_test::testmodel_is_not_abstract():
    assert not inspect.isabstract(test::TestModel)


def test_test::testmodel_constructor_exists():
    assert callable(test::TestModel.__init__)


def test_test::testmodel_constructor_args():
    sig = inspect.signature(test::TestModel.__init__)
    params = list(sig.parameters.keys())
    assert "birthDate" in params, "Missing parameter 'birthDate'"
    assert "name" in params, "Missing parameter 'name'"
    assert "gender" in params, "Missing parameter 'gender'"
    assert "age" in params, "Missing parameter 'age'"
    assert "accountBalance" in params, "Missing parameter 'accountBalance'"
    assert "childCount" in params, "Missing parameter 'childCount'"
    assert "isSelectable" in params, "Missing parameter 'isSelectable'"
    assert "overdrawAccount" in params, "Missing parameter 'overdrawAccount'"

def test_test::testmodel_has_birthDate():
    assert hasattr(test::TestModel, "birthDate")
    descriptor = None
    for klass in test::TestModel.__mro__:
        if "birthDate" in klass.__dict__:
            descriptor = klass.__dict__["birthDate"]
            break
    assert isinstance(descriptor, property)

def test_test::testmodel_has_name():
    assert hasattr(test::TestModel, "name")
    descriptor = None
    for klass in test::TestModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_test::testmodel_has_gender():
    assert hasattr(test::TestModel, "gender")
    descriptor = None
    for klass in test::TestModel.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)

def test_test::testmodel_has_age():
    assert hasattr(test::TestModel, "age")
    descriptor = None
    for klass in test::TestModel.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_test::testmodel_has_accountBalance():
    assert hasattr(test::TestModel, "accountBalance")
    descriptor = None
    for klass in test::TestModel.__mro__:
        if "accountBalance" in klass.__dict__:
            descriptor = klass.__dict__["accountBalance"]
            break
    assert isinstance(descriptor, property)

def test_test::testmodel_has_childCount():
    assert hasattr(test::TestModel, "childCount")
    descriptor = None
    for klass in test::TestModel.__mro__:
        if "childCount" in klass.__dict__:
            descriptor = klass.__dict__["childCount"]
            break
    assert isinstance(descriptor, property)

def test_test::testmodel_has_isSelectable():
    assert hasattr(test::TestModel, "isSelectable")
    descriptor = None
    for klass in test::TestModel.__mro__:
        if "isSelectable" in klass.__dict__:
            descriptor = klass.__dict__["isSelectable"]
            break
    assert isinstance(descriptor, property)

def test_test::testmodel_has_overdrawAccount():
    assert hasattr(test::TestModel, "overdrawAccount")
    descriptor = None
    for klass in test::TestModel.__mro__:
        if "overdrawAccount" in klass.__dict__:
            descriptor = klass.__dict__["overdrawAccount"]
            break
    assert isinstance(descriptor, property)



def test_test::addressmodel_is_not_abstract():
    assert not inspect.isabstract(test::AddressModel)


def test_test::addressmodel_constructor_exists():
    assert callable(test::AddressModel.__init__)


def test_test::addressmodel_constructor_args():
    sig = inspect.signature(test::AddressModel.__init__)
    params = list(sig.parameters.keys())
    assert "zipCode" in params, "Missing parameter 'zipCode'"
    assert "validTo" in params, "Missing parameter 'validTo'"
    assert "validFrom" in params, "Missing parameter 'validFrom'"
    assert "houseNumber" in params, "Missing parameter 'houseNumber'"
    assert "differentPostAddress" in params, "Missing parameter 'differentPostAddress'"
    assert "street" in params, "Missing parameter 'street'"

def test_test::addressmodel_has_zipCode():
    assert hasattr(test::AddressModel, "zipCode")
    descriptor = None
    for klass in test::AddressModel.__mro__:
        if "zipCode" in klass.__dict__:
            descriptor = klass.__dict__["zipCode"]
            break
    assert isinstance(descriptor, property)

def test_test::addressmodel_has_validTo():
    assert hasattr(test::AddressModel, "validTo")
    descriptor = None
    for klass in test::AddressModel.__mro__:
        if "validTo" in klass.__dict__:
            descriptor = klass.__dict__["validTo"]
            break
    assert isinstance(descriptor, property)

def test_test::addressmodel_has_validFrom():
    assert hasattr(test::AddressModel, "validFrom")
    descriptor = None
    for klass in test::AddressModel.__mro__:
        if "validFrom" in klass.__dict__:
            descriptor = klass.__dict__["validFrom"]
            break
    assert isinstance(descriptor, property)

def test_test::addressmodel_has_houseNumber():
    assert hasattr(test::AddressModel, "houseNumber")
    descriptor = None
    for klass in test::AddressModel.__mro__:
        if "houseNumber" in klass.__dict__:
            descriptor = klass.__dict__["houseNumber"]
            break
    assert isinstance(descriptor, property)

def test_test::addressmodel_has_differentPostAddress():
    assert hasattr(test::AddressModel, "differentPostAddress")
    descriptor = None
    for klass in test::AddressModel.__mro__:
        if "differentPostAddress" in klass.__dict__:
            descriptor = klass.__dict__["differentPostAddress"]
            break
    assert isinstance(descriptor, property)

def test_test::addressmodel_has_street():
    assert hasattr(test::AddressModel, "street")
    descriptor = None
    for klass in test::AddressModel.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_gender_exists():
    # Check that the Enumeration exists
    assert Gender is not None

def test_gender_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Gender]
    expected_literals = [
        "UNKNOWN",
        "MALE",
        "FEMALE",
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
test::ConfigurationModel_strategy = st.builds(
    test::ConfigurationModel,
)
test::TestModel_strategy = st.builds(
    test::TestModel,
    birthDate=
        st.dates(),
    name=
        safe_text,
    gender=
        safe_text,
    age=
        st.integers(),
    accountBalance=
        safe_text,
    childCount=
        safe_text,
    isSelectable=
        safe_text,
    overdrawAccount=
        safe_text
)
test::AddressModel_strategy = st.builds(
    test::AddressModel,
    zipCode=
        safe_text,
    validTo=
        st.dates(),
    validFrom=
        st.dates(),
    houseNumber=
        safe_text,
    differentPostAddress=
        st.booleans(),
    street=
        safe_text
)

@given(instance=test::ConfigurationModel_strategy)
@settings(max_examples=50)
def test_test::configurationmodel_instantiation(instance):
    assert isinstance(instance, test::ConfigurationModel)

@given(instance=test::TestModel_strategy)
@settings(max_examples=50)
def test_test::testmodel_instantiation(instance):
    assert isinstance(instance, test::TestModel)

@given(instance=test::TestModel_strategy)
def test_test::testmodel_birthDate_type(instance):
    assert isinstance(instance.birthDate, date)


@given(instance=test::TestModel_strategy)
def test_test::testmodel_birthDate_setter(instance):
    original = instance.birthDate
    instance.birthDate = original
    assert instance.birthDate == original

@given(instance=test::TestModel_strategy)
def test_test::testmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=test::TestModel_strategy)
def test_test::testmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=test::TestModel_strategy)
def test_test::testmodel_gender_type(instance):
    assert isinstance(instance.gender, str)


@given(instance=test::TestModel_strategy)
def test_test::testmodel_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original

@given(instance=test::TestModel_strategy)
def test_test::testmodel_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=test::TestModel_strategy)
def test_test::testmodel_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=test::TestModel_strategy)
def test_test::testmodel_accountBalance_type(instance):
    assert isinstance(instance.accountBalance, str)


@given(instance=test::TestModel_strategy)
def test_test::testmodel_accountBalance_setter(instance):
    original = instance.accountBalance
    instance.accountBalance = original
    assert instance.accountBalance == original

@given(instance=test::TestModel_strategy)
def test_test::testmodel_childCount_type(instance):
    assert isinstance(instance.childCount, str)


@given(instance=test::TestModel_strategy)
def test_test::testmodel_childCount_setter(instance):
    original = instance.childCount
    instance.childCount = original
    assert instance.childCount == original

@given(instance=test::TestModel_strategy)
def test_test::testmodel_isSelectable_type(instance):
    assert isinstance(instance.isSelectable, str)


@given(instance=test::TestModel_strategy)
def test_test::testmodel_isSelectable_setter(instance):
    original = instance.isSelectable
    instance.isSelectable = original
    assert instance.isSelectable == original

@given(instance=test::TestModel_strategy)
def test_test::testmodel_overdrawAccount_type(instance):
    assert isinstance(instance.overdrawAccount, str)


@given(instance=test::TestModel_strategy)
def test_test::testmodel_overdrawAccount_setter(instance):
    original = instance.overdrawAccount
    instance.overdrawAccount = original
    assert instance.overdrawAccount == original

@given(instance=test::AddressModel_strategy)
@settings(max_examples=50)
def test_test::addressmodel_instantiation(instance):
    assert isinstance(instance, test::AddressModel)

@given(instance=test::AddressModel_strategy)
def test_test::addressmodel_zipCode_type(instance):
    assert isinstance(instance.zipCode, str)


@given(instance=test::AddressModel_strategy)
def test_test::addressmodel_zipCode_setter(instance):
    original = instance.zipCode
    instance.zipCode = original
    assert instance.zipCode == original

@given(instance=test::AddressModel_strategy)
def test_test::addressmodel_validTo_type(instance):
    assert isinstance(instance.validTo, date)


@given(instance=test::AddressModel_strategy)
def test_test::addressmodel_validTo_setter(instance):
    original = instance.validTo
    instance.validTo = original
    assert instance.validTo == original

@given(instance=test::AddressModel_strategy)
def test_test::addressmodel_validFrom_type(instance):
    assert isinstance(instance.validFrom, date)


@given(instance=test::AddressModel_strategy)
def test_test::addressmodel_validFrom_setter(instance):
    original = instance.validFrom
    instance.validFrom = original
    assert instance.validFrom == original

@given(instance=test::AddressModel_strategy)
def test_test::addressmodel_houseNumber_type(instance):
    assert isinstance(instance.houseNumber, str)


@given(instance=test::AddressModel_strategy)
def test_test::addressmodel_houseNumber_setter(instance):
    original = instance.houseNumber
    instance.houseNumber = original
    assert instance.houseNumber == original

@given(instance=test::AddressModel_strategy)
def test_test::addressmodel_differentPostAddress_type(instance):
    assert isinstance(instance.differentPostAddress, bool)


@given(instance=test::AddressModel_strategy)
def test_test::addressmodel_differentPostAddress_setter(instance):
    original = instance.differentPostAddress
    instance.differentPostAddress = original
    assert instance.differentPostAddress == original

@given(instance=test::AddressModel_strategy)
def test_test::addressmodel_street_type(instance):
    assert isinstance(instance.street, str)


@given(instance=test::AddressModel_strategy)
def test_test::addressmodel_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original
