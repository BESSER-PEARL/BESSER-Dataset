import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Transaction,
    budgeting::CardTransaction,
    budgeting::CashTransaction,
    ActualEntry,
    budgeting::ActualTransactionEntry,
    budgeting::ActualAmountEntry,
    BudgetEntry,
    budgeting::BudgetFactorEntry,
    budgeting::BudgetAmountEntry,
    Category,
    budgeting::ExpenseCategory,
    budgeting::IncomeCategory,
    budgeting::Transaction,
    budgeting::ActualEntry,
    budgeting::BudgetEntry,
    budgeting::Month,
    BudgetingFile,
    budgeting::Year,
    budgeting::Library,
    budgeting::BudgetingFile,
    budgeting::Category,
    MonthEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_transaction_is_not_abstract():
    assert not inspect.isabstract(Transaction)


def test_transaction_constructor_exists():
    assert callable(Transaction.__init__)


def test_transaction_constructor_args():
    sig = inspect.signature(Transaction.__init__)
    params = list(sig.parameters.keys())



def test_budgeting::cardtransaction_is_not_abstract():
    assert not inspect.isabstract(budgeting::CardTransaction)


def test_budgeting::cardtransaction_constructor_exists():
    assert callable(budgeting::CardTransaction.__init__)


def test_budgeting::cardtransaction_constructor_args():
    sig = inspect.signature(budgeting::CardTransaction.__init__)
    params = list(sig.parameters.keys())
    assert "day" in params, "Missing parameter 'day'"
    assert "from_" in params, "Missing parameter 'from_'"

def test_budgeting::cardtransaction_has_day():
    assert hasattr(budgeting::CardTransaction, "day")
    descriptor = None
    for klass in budgeting::CardTransaction.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)

def test_budgeting::cardtransaction_has_from_():
    assert hasattr(budgeting::CardTransaction, "from_")
    descriptor = None
    for klass in budgeting::CardTransaction.__mro__:
        if "from_" in klass.__dict__:
            descriptor = klass.__dict__["from_"]
            break
    assert isinstance(descriptor, property)



def test_budgeting::cashtransaction_is_not_abstract():
    assert not inspect.isabstract(budgeting::CashTransaction)


def test_budgeting::cashtransaction_constructor_exists():
    assert callable(budgeting::CashTransaction.__init__)


def test_budgeting::cashtransaction_constructor_args():
    sig = inspect.signature(budgeting::CashTransaction.__init__)
    params = list(sig.parameters.keys())
    assert "day" in params, "Missing parameter 'day'"

def test_budgeting::cashtransaction_has_day():
    assert hasattr(budgeting::CashTransaction, "day")
    descriptor = None
    for klass in budgeting::CashTransaction.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)



def test_actualentry_is_not_abstract():
    assert not inspect.isabstract(ActualEntry)


def test_actualentry_constructor_exists():
    assert callable(ActualEntry.__init__)


def test_actualentry_constructor_args():
    sig = inspect.signature(ActualEntry.__init__)
    params = list(sig.parameters.keys())



def test_budgeting::actualtransactionentry_is_not_abstract():
    assert not inspect.isabstract(budgeting::ActualTransactionEntry)


def test_budgeting::actualtransactionentry_constructor_exists():
    assert callable(budgeting::ActualTransactionEntry.__init__)


def test_budgeting::actualtransactionentry_constructor_args():
    sig = inspect.signature(budgeting::ActualTransactionEntry.__init__)
    params = list(sig.parameters.keys())



def test_budgeting::actualamountentry_is_not_abstract():
    assert not inspect.isabstract(budgeting::ActualAmountEntry)


def test_budgeting::actualamountentry_constructor_exists():
    assert callable(budgeting::ActualAmountEntry.__init__)


def test_budgeting::actualamountentry_constructor_args():
    sig = inspect.signature(budgeting::ActualAmountEntry.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"

def test_budgeting::actualamountentry_has_amount():
    assert hasattr(budgeting::ActualAmountEntry, "amount")
    descriptor = None
    for klass in budgeting::ActualAmountEntry.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_budgetentry_is_not_abstract():
    assert not inspect.isabstract(BudgetEntry)


def test_budgetentry_constructor_exists():
    assert callable(BudgetEntry.__init__)


def test_budgetentry_constructor_args():
    sig = inspect.signature(BudgetEntry.__init__)
    params = list(sig.parameters.keys())



def test_budgeting::budgetfactorentry_is_not_abstract():
    assert not inspect.isabstract(budgeting::BudgetFactorEntry)


def test_budgeting::budgetfactorentry_constructor_exists():
    assert callable(budgeting::BudgetFactorEntry.__init__)


def test_budgeting::budgetfactorentry_constructor_args():
    sig = inspect.signature(budgeting::BudgetFactorEntry.__init__)
    params = list(sig.parameters.keys())
    assert "factor" in params, "Missing parameter 'factor'"

def test_budgeting::budgetfactorentry_has_factor():
    assert hasattr(budgeting::BudgetFactorEntry, "factor")
    descriptor = None
    for klass in budgeting::BudgetFactorEntry.__mro__:
        if "factor" in klass.__dict__:
            descriptor = klass.__dict__["factor"]
            break
    assert isinstance(descriptor, property)



def test_budgeting::budgetamountentry_is_not_abstract():
    assert not inspect.isabstract(budgeting::BudgetAmountEntry)


def test_budgeting::budgetamountentry_constructor_exists():
    assert callable(budgeting::BudgetAmountEntry.__init__)


def test_budgeting::budgetamountentry_constructor_args():
    sig = inspect.signature(budgeting::BudgetAmountEntry.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"

def test_budgeting::budgetamountentry_has_amount():
    assert hasattr(budgeting::BudgetAmountEntry, "amount")
    descriptor = None
    for klass in budgeting::BudgetAmountEntry.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_category_is_not_abstract():
    assert not inspect.isabstract(Category)


def test_category_constructor_exists():
    assert callable(Category.__init__)


def test_category_constructor_args():
    sig = inspect.signature(Category.__init__)
    params = list(sig.parameters.keys())



def test_budgeting::expensecategory_is_not_abstract():
    assert not inspect.isabstract(budgeting::ExpenseCategory)


def test_budgeting::expensecategory_constructor_exists():
    assert callable(budgeting::ExpenseCategory.__init__)


def test_budgeting::expensecategory_constructor_args():
    sig = inspect.signature(budgeting::ExpenseCategory.__init__)
    params = list(sig.parameters.keys())
    assert "patterns" in params, "Missing parameter 'patterns'"

def test_budgeting::expensecategory_has_patterns():
    assert hasattr(budgeting::ExpenseCategory, "patterns")
    descriptor = None
    for klass in budgeting::ExpenseCategory.__mro__:
        if "patterns" in klass.__dict__:
            descriptor = klass.__dict__["patterns"]
            break
    assert isinstance(descriptor, property)



def test_budgeting::incomecategory_is_not_abstract():
    assert not inspect.isabstract(budgeting::IncomeCategory)


def test_budgeting::incomecategory_constructor_exists():
    assert callable(budgeting::IncomeCategory.__init__)


def test_budgeting::incomecategory_constructor_args():
    sig = inspect.signature(budgeting::IncomeCategory.__init__)
    params = list(sig.parameters.keys())



def test_budgeting::transaction_is_not_abstract():
    assert not inspect.isabstract(budgeting::Transaction)


def test_budgeting::transaction_constructor_exists():
    assert callable(budgeting::Transaction.__init__)


def test_budgeting::transaction_constructor_args():
    sig = inspect.signature(budgeting::Transaction.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"

def test_budgeting::transaction_has_amount():
    assert hasattr(budgeting::Transaction, "amount")
    descriptor = None
    for klass in budgeting::Transaction.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_budgeting::actualentry_is_not_abstract():
    assert not inspect.isabstract(budgeting::ActualEntry)


def test_budgeting::actualentry_constructor_exists():
    assert callable(budgeting::ActualEntry.__init__)


def test_budgeting::actualentry_constructor_args():
    sig = inspect.signature(budgeting::ActualEntry.__init__)
    params = list(sig.parameters.keys())



def test_budgeting::budgetentry_is_not_abstract():
    assert not inspect.isabstract(budgeting::BudgetEntry)


def test_budgeting::budgetentry_constructor_exists():
    assert callable(budgeting::BudgetEntry.__init__)


def test_budgeting::budgetentry_constructor_args():
    sig = inspect.signature(budgeting::BudgetEntry.__init__)
    params = list(sig.parameters.keys())



def test_budgeting::month_is_not_abstract():
    assert not inspect.isabstract(budgeting::Month)


def test_budgeting::month_constructor_exists():
    assert callable(budgeting::Month.__init__)


def test_budgeting::month_constructor_args():
    sig = inspect.signature(budgeting::Month.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_budgeting::month_has_name():
    assert hasattr(budgeting::Month, "name")
    descriptor = None
    for klass in budgeting::Month.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_budgetingfile_is_not_abstract():
    assert not inspect.isabstract(BudgetingFile)


def test_budgetingfile_constructor_exists():
    assert callable(BudgetingFile.__init__)


def test_budgetingfile_constructor_args():
    sig = inspect.signature(BudgetingFile.__init__)
    params = list(sig.parameters.keys())



def test_budgeting::year_is_not_abstract():
    assert not inspect.isabstract(budgeting::Year)


def test_budgeting::year_constructor_exists():
    assert callable(budgeting::Year.__init__)


def test_budgeting::year_constructor_args():
    sig = inspect.signature(budgeting::Year.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_budgeting::year_has_name():
    assert hasattr(budgeting::Year, "name")
    descriptor = None
    for klass in budgeting::Year.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_budgeting::library_is_not_abstract():
    assert not inspect.isabstract(budgeting::Library)


def test_budgeting::library_constructor_exists():
    assert callable(budgeting::Library.__init__)


def test_budgeting::library_constructor_args():
    sig = inspect.signature(budgeting::Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_budgeting::library_has_name():
    assert hasattr(budgeting::Library, "name")
    descriptor = None
    for klass in budgeting::Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_budgeting::budgetingfile_is_not_abstract():
    assert not inspect.isabstract(budgeting::BudgetingFile)


def test_budgeting::budgetingfile_constructor_exists():
    assert callable(budgeting::BudgetingFile.__init__)


def test_budgeting::budgetingfile_constructor_args():
    sig = inspect.signature(budgeting::BudgetingFile.__init__)
    params = list(sig.parameters.keys())



def test_budgeting::category_is_not_abstract():
    assert not inspect.isabstract(budgeting::Category)


def test_budgeting::category_constructor_exists():
    assert callable(budgeting::Category.__init__)


def test_budgeting::category_constructor_args():
    sig = inspect.signature(budgeting::Category.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_budgeting::category_has_name():
    assert hasattr(budgeting::Category, "name")
    descriptor = None
    for klass in budgeting::Category.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_monthenum_exists():
    # Check that the Enumeration exists
    assert MonthEnum is not None

def test_monthenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MonthEnum]
    expected_literals = [
        "JULY",
        "DECEMBER",
        "SEPTEMBER",
        "JANUARY",
        "APRIL",
        "MARCH",
        "NOVEMBER",
        "FEBRUARY",
        "MAY",
        "OCTOBER",
        "AUGUST",
        "JUNE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MonthEnum"


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
Transaction_strategy = st.builds(
    Transaction,
)
budgeting::CardTransaction_strategy = st.builds(
    budgeting::CardTransaction,
    day=
        st.integers(),
    from_=
        safe_text
)
budgeting::CashTransaction_strategy = st.builds(
    budgeting::CashTransaction,
    day=
        safe_text
)
ActualEntry_strategy = st.builds(
    ActualEntry,
)
budgeting::ActualTransactionEntry_strategy = st.builds(
    budgeting::ActualTransactionEntry,
)
budgeting::ActualAmountEntry_strategy = st.builds(
    budgeting::ActualAmountEntry,
    amount=
        safe_text
)
BudgetEntry_strategy = st.builds(
    BudgetEntry,
)
budgeting::BudgetFactorEntry_strategy = st.builds(
    budgeting::BudgetFactorEntry,
    factor=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
budgeting::BudgetAmountEntry_strategy = st.builds(
    budgeting::BudgetAmountEntry,
    amount=
        safe_text
)
Category_strategy = st.builds(
    Category,
)
budgeting::ExpenseCategory_strategy = st.builds(
    budgeting::ExpenseCategory,
    patterns=
        safe_text
)
budgeting::IncomeCategory_strategy = st.builds(
    budgeting::IncomeCategory,
)
budgeting::Transaction_strategy = st.builds(
    budgeting::Transaction,
    amount=
        safe_text
)
budgeting::ActualEntry_strategy = st.builds(
    budgeting::ActualEntry,
)
budgeting::BudgetEntry_strategy = st.builds(
    budgeting::BudgetEntry,
)
budgeting::Month_strategy = st.builds(
    budgeting::Month,
    name=
        safe_text
)
BudgetingFile_strategy = st.builds(
    BudgetingFile,
)
budgeting::Year_strategy = st.builds(
    budgeting::Year,
    name=
        st.integers()
)
budgeting::Library_strategy = st.builds(
    budgeting::Library,
    name=
        safe_text
)
budgeting::BudgetingFile_strategy = st.builds(
    budgeting::BudgetingFile,
)
budgeting::Category_strategy = st.builds(
    budgeting::Category,
    name=
        safe_text
)

@given(instance=Transaction_strategy)
@settings(max_examples=50)
def test_transaction_instantiation(instance):
    assert isinstance(instance, Transaction)

@given(instance=budgeting::CardTransaction_strategy)
@settings(max_examples=50)
def test_budgeting::cardtransaction_instantiation(instance):
    assert isinstance(instance, budgeting::CardTransaction)

@given(instance=budgeting::CardTransaction_strategy)
def test_budgeting::cardtransaction_day_type(instance):
    assert isinstance(instance.day, int)


@given(instance=budgeting::CardTransaction_strategy)
def test_budgeting::cardtransaction_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original

@given(instance=budgeting::CardTransaction_strategy)
def test_budgeting::cardtransaction_from__type(instance):
    assert isinstance(instance.from_, str)


@given(instance=budgeting::CardTransaction_strategy)
def test_budgeting::cardtransaction_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original

@given(instance=budgeting::CashTransaction_strategy)
@settings(max_examples=50)
def test_budgeting::cashtransaction_instantiation(instance):
    assert isinstance(instance, budgeting::CashTransaction)

@given(instance=budgeting::CashTransaction_strategy)
def test_budgeting::cashtransaction_day_type(instance):
    assert isinstance(instance.day, str)


@given(instance=budgeting::CashTransaction_strategy)
def test_budgeting::cashtransaction_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original

@given(instance=ActualEntry_strategy)
@settings(max_examples=50)
def test_actualentry_instantiation(instance):
    assert isinstance(instance, ActualEntry)

@given(instance=budgeting::ActualTransactionEntry_strategy)
@settings(max_examples=50)
def test_budgeting::actualtransactionentry_instantiation(instance):
    assert isinstance(instance, budgeting::ActualTransactionEntry)

@given(instance=budgeting::ActualAmountEntry_strategy)
@settings(max_examples=50)
def test_budgeting::actualamountentry_instantiation(instance):
    assert isinstance(instance, budgeting::ActualAmountEntry)

@given(instance=budgeting::ActualAmountEntry_strategy)
def test_budgeting::actualamountentry_amount_type(instance):
    assert isinstance(instance.amount, str)


@given(instance=budgeting::ActualAmountEntry_strategy)
def test_budgeting::actualamountentry_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=BudgetEntry_strategy)
@settings(max_examples=50)
def test_budgetentry_instantiation(instance):
    assert isinstance(instance, BudgetEntry)

@given(instance=budgeting::BudgetFactorEntry_strategy)
@settings(max_examples=50)
def test_budgeting::budgetfactorentry_instantiation(instance):
    assert isinstance(instance, budgeting::BudgetFactorEntry)

@given(instance=budgeting::BudgetFactorEntry_strategy)
def test_budgeting::budgetfactorentry_factor_type(instance):
    assert isinstance(instance.factor, float)


@given(instance=budgeting::BudgetFactorEntry_strategy)
def test_budgeting::budgetfactorentry_factor_setter(instance):
    original = instance.factor
    instance.factor = original
    assert instance.factor == original

@given(instance=budgeting::BudgetAmountEntry_strategy)
@settings(max_examples=50)
def test_budgeting::budgetamountentry_instantiation(instance):
    assert isinstance(instance, budgeting::BudgetAmountEntry)

@given(instance=budgeting::BudgetAmountEntry_strategy)
def test_budgeting::budgetamountentry_amount_type(instance):
    assert isinstance(instance.amount, str)


@given(instance=budgeting::BudgetAmountEntry_strategy)
def test_budgeting::budgetamountentry_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=Category_strategy)
@settings(max_examples=50)
def test_category_instantiation(instance):
    assert isinstance(instance, Category)

@given(instance=budgeting::ExpenseCategory_strategy)
@settings(max_examples=50)
def test_budgeting::expensecategory_instantiation(instance):
    assert isinstance(instance, budgeting::ExpenseCategory)

@given(instance=budgeting::ExpenseCategory_strategy)
def test_budgeting::expensecategory_patterns_type(instance):
    assert isinstance(instance.patterns, str)


@given(instance=budgeting::ExpenseCategory_strategy)
def test_budgeting::expensecategory_patterns_setter(instance):
    original = instance.patterns
    instance.patterns = original
    assert instance.patterns == original

@given(instance=budgeting::IncomeCategory_strategy)
@settings(max_examples=50)
def test_budgeting::incomecategory_instantiation(instance):
    assert isinstance(instance, budgeting::IncomeCategory)

@given(instance=budgeting::Transaction_strategy)
@settings(max_examples=50)
def test_budgeting::transaction_instantiation(instance):
    assert isinstance(instance, budgeting::Transaction)

@given(instance=budgeting::Transaction_strategy)
def test_budgeting::transaction_amount_type(instance):
    assert isinstance(instance.amount, str)


@given(instance=budgeting::Transaction_strategy)
def test_budgeting::transaction_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=budgeting::ActualEntry_strategy)
@settings(max_examples=50)
def test_budgeting::actualentry_instantiation(instance):
    assert isinstance(instance, budgeting::ActualEntry)

@given(instance=budgeting::BudgetEntry_strategy)
@settings(max_examples=50)
def test_budgeting::budgetentry_instantiation(instance):
    assert isinstance(instance, budgeting::BudgetEntry)

@given(instance=budgeting::Month_strategy)
@settings(max_examples=50)
def test_budgeting::month_instantiation(instance):
    assert isinstance(instance, budgeting::Month)

@given(instance=budgeting::Month_strategy)
def test_budgeting::month_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=budgeting::Month_strategy)
def test_budgeting::month_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BudgetingFile_strategy)
@settings(max_examples=50)
def test_budgetingfile_instantiation(instance):
    assert isinstance(instance, BudgetingFile)

@given(instance=budgeting::Year_strategy)
@settings(max_examples=50)
def test_budgeting::year_instantiation(instance):
    assert isinstance(instance, budgeting::Year)

@given(instance=budgeting::Year_strategy)
def test_budgeting::year_name_type(instance):
    assert isinstance(instance.name, int)


@given(instance=budgeting::Year_strategy)
def test_budgeting::year_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=budgeting::Library_strategy)
@settings(max_examples=50)
def test_budgeting::library_instantiation(instance):
    assert isinstance(instance, budgeting::Library)

@given(instance=budgeting::Library_strategy)
def test_budgeting::library_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=budgeting::Library_strategy)
def test_budgeting::library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=budgeting::BudgetingFile_strategy)
@settings(max_examples=50)
def test_budgeting::budgetingfile_instantiation(instance):
    assert isinstance(instance, budgeting::BudgetingFile)

@given(instance=budgeting::Category_strategy)
@settings(max_examples=50)
def test_budgeting::category_instantiation(instance):
    assert isinstance(instance, budgeting::Category)

@given(instance=budgeting::Category_strategy)
def test_budgeting::category_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=budgeting::Category_strategy)
def test_budgeting::category_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
