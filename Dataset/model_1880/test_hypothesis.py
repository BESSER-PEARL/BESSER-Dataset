import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Transaction,
    budgeting_CardTransaction,
    budgeting_CashTransaction,
    ActualEntry,
    budgeting_ActualTransactionEntry,
    budgeting_ActualAmountEntry,
    BudgetEntry,
    budgeting_BudgetFactorEntry,
    budgeting_BudgetAmountEntry,
    Category,
    budgeting_ExpenseCategory,
    budgeting_IncomeCategory,
    budgeting_Transaction,
    budgeting_ActualEntry,
    budgeting_BudgetEntry,
    budgeting_Month,
    BudgetingFile,
    budgeting_Year,
    budgeting_Library,
    budgeting_BudgetingFile,
    budgeting_Category,
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



def test_budgeting_cardtransaction_is_not_abstract():
    assert not inspect.isabstract(budgeting_CardTransaction)


def test_budgeting_cardtransaction_constructor_exists():
    assert callable(budgeting_CardTransaction.__init__)


def test_budgeting_cardtransaction_constructor_args():
    sig = inspect.signature(budgeting_CardTransaction.__init__)
    params = list(sig.parameters.keys())
    assert "day" in params, "Missing parameter 'day'"
    assert "from_" in params, "Missing parameter 'from_'"

def test_budgeting_cardtransaction_has_day():
    assert hasattr(budgeting_CardTransaction, "day")
    descriptor = None
    for klass in budgeting_CardTransaction.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)

def test_budgeting_cardtransaction_has_from_():
    assert hasattr(budgeting_CardTransaction, "from_")
    descriptor = None
    for klass in budgeting_CardTransaction.__mro__:
        if "from_" in klass.__dict__:
            descriptor = klass.__dict__["from_"]
            break
    assert isinstance(descriptor, property)



def test_budgeting_cashtransaction_is_not_abstract():
    assert not inspect.isabstract(budgeting_CashTransaction)


def test_budgeting_cashtransaction_constructor_exists():
    assert callable(budgeting_CashTransaction.__init__)


def test_budgeting_cashtransaction_constructor_args():
    sig = inspect.signature(budgeting_CashTransaction.__init__)
    params = list(sig.parameters.keys())
    assert "day" in params, "Missing parameter 'day'"

def test_budgeting_cashtransaction_has_day():
    assert hasattr(budgeting_CashTransaction, "day")
    descriptor = None
    for klass in budgeting_CashTransaction.__mro__:
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



def test_budgeting_actualtransactionentry_is_not_abstract():
    assert not inspect.isabstract(budgeting_ActualTransactionEntry)


def test_budgeting_actualtransactionentry_constructor_exists():
    assert callable(budgeting_ActualTransactionEntry.__init__)


def test_budgeting_actualtransactionentry_constructor_args():
    sig = inspect.signature(budgeting_ActualTransactionEntry.__init__)
    params = list(sig.parameters.keys())



def test_budgeting_actualamountentry_is_not_abstract():
    assert not inspect.isabstract(budgeting_ActualAmountEntry)


def test_budgeting_actualamountentry_constructor_exists():
    assert callable(budgeting_ActualAmountEntry.__init__)


def test_budgeting_actualamountentry_constructor_args():
    sig = inspect.signature(budgeting_ActualAmountEntry.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"

def test_budgeting_actualamountentry_has_amount():
    assert hasattr(budgeting_ActualAmountEntry, "amount")
    descriptor = None
    for klass in budgeting_ActualAmountEntry.__mro__:
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



def test_budgeting_budgetfactorentry_is_not_abstract():
    assert not inspect.isabstract(budgeting_BudgetFactorEntry)


def test_budgeting_budgetfactorentry_constructor_exists():
    assert callable(budgeting_BudgetFactorEntry.__init__)


def test_budgeting_budgetfactorentry_constructor_args():
    sig = inspect.signature(budgeting_BudgetFactorEntry.__init__)
    params = list(sig.parameters.keys())
    assert "factor" in params, "Missing parameter 'factor'"

def test_budgeting_budgetfactorentry_has_factor():
    assert hasattr(budgeting_BudgetFactorEntry, "factor")
    descriptor = None
    for klass in budgeting_BudgetFactorEntry.__mro__:
        if "factor" in klass.__dict__:
            descriptor = klass.__dict__["factor"]
            break
    assert isinstance(descriptor, property)



def test_budgeting_budgetamountentry_is_not_abstract():
    assert not inspect.isabstract(budgeting_BudgetAmountEntry)


def test_budgeting_budgetamountentry_constructor_exists():
    assert callable(budgeting_BudgetAmountEntry.__init__)


def test_budgeting_budgetamountentry_constructor_args():
    sig = inspect.signature(budgeting_BudgetAmountEntry.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"

def test_budgeting_budgetamountentry_has_amount():
    assert hasattr(budgeting_BudgetAmountEntry, "amount")
    descriptor = None
    for klass in budgeting_BudgetAmountEntry.__mro__:
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



def test_budgeting_expensecategory_is_not_abstract():
    assert not inspect.isabstract(budgeting_ExpenseCategory)


def test_budgeting_expensecategory_constructor_exists():
    assert callable(budgeting_ExpenseCategory.__init__)


def test_budgeting_expensecategory_constructor_args():
    sig = inspect.signature(budgeting_ExpenseCategory.__init__)
    params = list(sig.parameters.keys())
    assert "patterns" in params, "Missing parameter 'patterns'"

def test_budgeting_expensecategory_has_patterns():
    assert hasattr(budgeting_ExpenseCategory, "patterns")
    descriptor = None
    for klass in budgeting_ExpenseCategory.__mro__:
        if "patterns" in klass.__dict__:
            descriptor = klass.__dict__["patterns"]
            break
    assert isinstance(descriptor, property)



def test_budgeting_incomecategory_is_not_abstract():
    assert not inspect.isabstract(budgeting_IncomeCategory)


def test_budgeting_incomecategory_constructor_exists():
    assert callable(budgeting_IncomeCategory.__init__)


def test_budgeting_incomecategory_constructor_args():
    sig = inspect.signature(budgeting_IncomeCategory.__init__)
    params = list(sig.parameters.keys())



def test_budgeting_transaction_is_not_abstract():
    assert not inspect.isabstract(budgeting_Transaction)


def test_budgeting_transaction_constructor_exists():
    assert callable(budgeting_Transaction.__init__)


def test_budgeting_transaction_constructor_args():
    sig = inspect.signature(budgeting_Transaction.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"

def test_budgeting_transaction_has_amount():
    assert hasattr(budgeting_Transaction, "amount")
    descriptor = None
    for klass in budgeting_Transaction.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_budgeting_actualentry_is_not_abstract():
    assert not inspect.isabstract(budgeting_ActualEntry)


def test_budgeting_actualentry_constructor_exists():
    assert callable(budgeting_ActualEntry.__init__)


def test_budgeting_actualentry_constructor_args():
    sig = inspect.signature(budgeting_ActualEntry.__init__)
    params = list(sig.parameters.keys())



def test_budgeting_budgetentry_is_not_abstract():
    assert not inspect.isabstract(budgeting_BudgetEntry)


def test_budgeting_budgetentry_constructor_exists():
    assert callable(budgeting_BudgetEntry.__init__)


def test_budgeting_budgetentry_constructor_args():
    sig = inspect.signature(budgeting_BudgetEntry.__init__)
    params = list(sig.parameters.keys())



def test_budgeting_month_is_not_abstract():
    assert not inspect.isabstract(budgeting_Month)


def test_budgeting_month_constructor_exists():
    assert callable(budgeting_Month.__init__)


def test_budgeting_month_constructor_args():
    sig = inspect.signature(budgeting_Month.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_budgeting_month_has_name():
    assert hasattr(budgeting_Month, "name")
    descriptor = None
    for klass in budgeting_Month.__mro__:
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



def test_budgeting_year_is_not_abstract():
    assert not inspect.isabstract(budgeting_Year)


def test_budgeting_year_constructor_exists():
    assert callable(budgeting_Year.__init__)


def test_budgeting_year_constructor_args():
    sig = inspect.signature(budgeting_Year.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_budgeting_year_has_name():
    assert hasattr(budgeting_Year, "name")
    descriptor = None
    for klass in budgeting_Year.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_budgeting_library_is_not_abstract():
    assert not inspect.isabstract(budgeting_Library)


def test_budgeting_library_constructor_exists():
    assert callable(budgeting_Library.__init__)


def test_budgeting_library_constructor_args():
    sig = inspect.signature(budgeting_Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_budgeting_library_has_name():
    assert hasattr(budgeting_Library, "name")
    descriptor = None
    for klass in budgeting_Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_budgeting_budgetingfile_is_not_abstract():
    assert not inspect.isabstract(budgeting_BudgetingFile)


def test_budgeting_budgetingfile_constructor_exists():
    assert callable(budgeting_BudgetingFile.__init__)


def test_budgeting_budgetingfile_constructor_args():
    sig = inspect.signature(budgeting_BudgetingFile.__init__)
    params = list(sig.parameters.keys())



def test_budgeting_category_is_not_abstract():
    assert not inspect.isabstract(budgeting_Category)


def test_budgeting_category_constructor_exists():
    assert callable(budgeting_Category.__init__)


def test_budgeting_category_constructor_args():
    sig = inspect.signature(budgeting_Category.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_budgeting_category_has_name():
    assert hasattr(budgeting_Category, "name")
    descriptor = None
    for klass in budgeting_Category.__mro__:
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
        "JANUARY",
        "APRIL",
        "DECEMBER",
        "MAY",
        "MARCH",
        "JULY",
        "AUGUST",
        "NOVEMBER",
        "OCTOBER",
        "SEPTEMBER",
        "JUNE",
        "FEBRUARY",
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
budgeting_CardTransaction_strategy = st.builds(
    budgeting_CardTransaction,
    day=
        st.integers(),
    from_=
        safe_text
)
budgeting_CashTransaction_strategy = st.builds(
    budgeting_CashTransaction,
    day=
        safe_text
)
ActualEntry_strategy = st.builds(
    ActualEntry,
)
budgeting_ActualTransactionEntry_strategy = st.builds(
    budgeting_ActualTransactionEntry,
)
budgeting_ActualAmountEntry_strategy = st.builds(
    budgeting_ActualAmountEntry,
    amount=
        safe_text
)
BudgetEntry_strategy = st.builds(
    BudgetEntry,
)
budgeting_BudgetFactorEntry_strategy = st.builds(
    budgeting_BudgetFactorEntry,
    factor=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
budgeting_BudgetAmountEntry_strategy = st.builds(
    budgeting_BudgetAmountEntry,
    amount=
        safe_text
)
Category_strategy = st.builds(
    Category,
)
budgeting_ExpenseCategory_strategy = st.builds(
    budgeting_ExpenseCategory,
    patterns=
        safe_text
)
budgeting_IncomeCategory_strategy = st.builds(
    budgeting_IncomeCategory,
)
budgeting_Transaction_strategy = st.builds(
    budgeting_Transaction,
    amount=
        safe_text
)
budgeting_ActualEntry_strategy = st.builds(
    budgeting_ActualEntry,
)
budgeting_BudgetEntry_strategy = st.builds(
    budgeting_BudgetEntry,
)
budgeting_Month_strategy = st.builds(
    budgeting_Month,
    name=
        safe_text
)
BudgetingFile_strategy = st.builds(
    BudgetingFile,
)
budgeting_Year_strategy = st.builds(
    budgeting_Year,
    name=
        st.integers()
)
budgeting_Library_strategy = st.builds(
    budgeting_Library,
    name=
        safe_text
)
budgeting_BudgetingFile_strategy = st.builds(
    budgeting_BudgetingFile,
)
budgeting_Category_strategy = st.builds(
    budgeting_Category,
    name=
        safe_text
)

@given(instance=Transaction_strategy)
@settings(max_examples=50)
def test_transaction_instantiation(instance):
    assert isinstance(instance, Transaction)

@given(instance=budgeting_CardTransaction_strategy)
@settings(max_examples=50)
def test_budgeting_cardtransaction_instantiation(instance):
    assert isinstance(instance, budgeting_CardTransaction)



@given(instance=budgeting_CardTransaction_strategy)
def test_budgeting_cardtransaction_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original



@given(instance=budgeting_CardTransaction_strategy)
def test_budgeting_cardtransaction_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original

@given(instance=budgeting_CashTransaction_strategy)
@settings(max_examples=50)
def test_budgeting_cashtransaction_instantiation(instance):
    assert isinstance(instance, budgeting_CashTransaction)



@given(instance=budgeting_CashTransaction_strategy)
def test_budgeting_cashtransaction_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original

@given(instance=ActualEntry_strategy)
@settings(max_examples=50)
def test_actualentry_instantiation(instance):
    assert isinstance(instance, ActualEntry)

@given(instance=budgeting_ActualTransactionEntry_strategy)
@settings(max_examples=50)
def test_budgeting_actualtransactionentry_instantiation(instance):
    assert isinstance(instance, budgeting_ActualTransactionEntry)

@given(instance=budgeting_ActualAmountEntry_strategy)
@settings(max_examples=50)
def test_budgeting_actualamountentry_instantiation(instance):
    assert isinstance(instance, budgeting_ActualAmountEntry)



@given(instance=budgeting_ActualAmountEntry_strategy)
def test_budgeting_actualamountentry_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=BudgetEntry_strategy)
@settings(max_examples=50)
def test_budgetentry_instantiation(instance):
    assert isinstance(instance, BudgetEntry)

@given(instance=budgeting_BudgetFactorEntry_strategy)
@settings(max_examples=50)
def test_budgeting_budgetfactorentry_instantiation(instance):
    assert isinstance(instance, budgeting_BudgetFactorEntry)



@given(instance=budgeting_BudgetFactorEntry_strategy)
def test_budgeting_budgetfactorentry_factor_setter(instance):
    original = instance.factor
    instance.factor = original
    assert instance.factor == original

@given(instance=budgeting_BudgetAmountEntry_strategy)
@settings(max_examples=50)
def test_budgeting_budgetamountentry_instantiation(instance):
    assert isinstance(instance, budgeting_BudgetAmountEntry)



@given(instance=budgeting_BudgetAmountEntry_strategy)
def test_budgeting_budgetamountentry_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=Category_strategy)
@settings(max_examples=50)
def test_category_instantiation(instance):
    assert isinstance(instance, Category)

@given(instance=budgeting_ExpenseCategory_strategy)
@settings(max_examples=50)
def test_budgeting_expensecategory_instantiation(instance):
    assert isinstance(instance, budgeting_ExpenseCategory)



@given(instance=budgeting_ExpenseCategory_strategy)
def test_budgeting_expensecategory_patterns_setter(instance):
    original = instance.patterns
    instance.patterns = original
    assert instance.patterns == original

@given(instance=budgeting_IncomeCategory_strategy)
@settings(max_examples=50)
def test_budgeting_incomecategory_instantiation(instance):
    assert isinstance(instance, budgeting_IncomeCategory)

@given(instance=budgeting_Transaction_strategy)
@settings(max_examples=50)
def test_budgeting_transaction_instantiation(instance):
    assert isinstance(instance, budgeting_Transaction)



@given(instance=budgeting_Transaction_strategy)
def test_budgeting_transaction_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=budgeting_ActualEntry_strategy)
@settings(max_examples=50)
def test_budgeting_actualentry_instantiation(instance):
    assert isinstance(instance, budgeting_ActualEntry)

@given(instance=budgeting_BudgetEntry_strategy)
@settings(max_examples=50)
def test_budgeting_budgetentry_instantiation(instance):
    assert isinstance(instance, budgeting_BudgetEntry)

@given(instance=budgeting_Month_strategy)
@settings(max_examples=50)
def test_budgeting_month_instantiation(instance):
    assert isinstance(instance, budgeting_Month)



@given(instance=budgeting_Month_strategy)
def test_budgeting_month_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BudgetingFile_strategy)
@settings(max_examples=50)
def test_budgetingfile_instantiation(instance):
    assert isinstance(instance, BudgetingFile)

@given(instance=budgeting_Year_strategy)
@settings(max_examples=50)
def test_budgeting_year_instantiation(instance):
    assert isinstance(instance, budgeting_Year)



@given(instance=budgeting_Year_strategy)
def test_budgeting_year_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=budgeting_Library_strategy)
@settings(max_examples=50)
def test_budgeting_library_instantiation(instance):
    assert isinstance(instance, budgeting_Library)



@given(instance=budgeting_Library_strategy)
def test_budgeting_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=budgeting_BudgetingFile_strategy)
@settings(max_examples=50)
def test_budgeting_budgetingfile_instantiation(instance):
    assert isinstance(instance, budgeting_BudgetingFile)

@given(instance=budgeting_Category_strategy)
@settings(max_examples=50)
def test_budgeting_category_instantiation(instance):
    assert isinstance(instance, budgeting_Category)



@given(instance=budgeting_Category_strategy)
def test_budgeting_category_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
