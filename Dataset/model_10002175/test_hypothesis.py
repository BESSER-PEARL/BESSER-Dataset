import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    DepositTransaction2,
    TransferTransaction2,
    WithdrawTransaction2,
    ATM_Card2,
    Transaction2,
    Bank2,
    Savings_Account2,
    Account2_Interface,
    Customer2,
    DepositTransaction,
    TransferTransaction,
    WithdrawTransaction,
    ATM_Card,
    Transaction,
    Bank,
    Savings_Account,
    Account_Interface,
    Customer,
    TransactionType2,
    TransactionType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_deposittransaction2_is_not_abstract():
    assert not inspect.isabstract(DepositTransaction2)


def test_deposittransaction2_constructor_exists():
    assert callable(DepositTransaction2.__init__)


def test_deposittransaction2_constructor_args():
    sig = inspect.signature(DepositTransaction2.__init__)
    params = list(sig.parameters.keys())



def test_transfertransaction2_is_not_abstract():
    assert not inspect.isabstract(TransferTransaction2)


def test_transfertransaction2_constructor_exists():
    assert callable(TransferTransaction2.__init__)


def test_transfertransaction2_constructor_args():
    sig = inspect.signature(TransferTransaction2.__init__)
    params = list(sig.parameters.keys())
    assert "targetAccount" in params, "Missing parameter 'targetAccount'"
    assert "sourceAccount" in params, "Missing parameter 'sourceAccount'"

def test_transfertransaction2_has_targetAccount():
    assert hasattr(TransferTransaction2, "targetAccount")
    descriptor = None
    for klass in TransferTransaction2.__mro__:
        if "targetAccount" in klass.__dict__:
            descriptor = klass.__dict__["targetAccount"]
            break
    assert isinstance(descriptor, property)

def test_transfertransaction2_has_sourceAccount():
    assert hasattr(TransferTransaction2, "sourceAccount")
    descriptor = None
    for klass in TransferTransaction2.__mro__:
        if "sourceAccount" in klass.__dict__:
            descriptor = klass.__dict__["sourceAccount"]
            break
    assert isinstance(descriptor, property)



def test_withdrawtransaction2_is_not_abstract():
    assert not inspect.isabstract(WithdrawTransaction2)


def test_withdrawtransaction2_constructor_exists():
    assert callable(WithdrawTransaction2.__init__)


def test_withdrawtransaction2_constructor_args():
    sig = inspect.signature(WithdrawTransaction2.__init__)
    params = list(sig.parameters.keys())



def test_atm_card2_is_not_abstract():
    assert not inspect.isabstract(ATM_Card2)


def test_atm_card2_constructor_exists():
    assert callable(ATM_Card2.__init__)


def test_atm_card2_constructor_args():
    sig = inspect.signature(ATM_Card2.__init__)
    params = list(sig.parameters.keys())
    assert "cardNumber" in params, "Missing parameter 'cardNumber'"
    assert "pin" in params, "Missing parameter 'pin'"

def test_atm_card2_has_cardNumber():
    assert hasattr(ATM_Card2, "cardNumber")
    descriptor = None
    for klass in ATM_Card2.__mro__:
        if "cardNumber" in klass.__dict__:
            descriptor = klass.__dict__["cardNumber"]
            break
    assert isinstance(descriptor, property)

def test_atm_card2_has_pin():
    assert hasattr(ATM_Card2, "pin")
    descriptor = None
    for klass in ATM_Card2.__mro__:
        if "pin" in klass.__dict__:
            descriptor = klass.__dict__["pin"]
            break
    assert isinstance(descriptor, property)



def test_transaction2_is_not_abstract():
    assert not inspect.isabstract(Transaction2)


def test_transaction2_constructor_exists():
    assert callable(Transaction2.__init__)


def test_transaction2_constructor_args():
    sig = inspect.signature(Transaction2.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"
    assert "transactionTime" in params, "Missing parameter 'transactionTime'"
    assert "type" in params, "Missing parameter 'type'"
    assert "id" in params, "Missing parameter 'id'"

def test_transaction2_has_amount():
    assert hasattr(Transaction2, "amount")
    descriptor = None
    for klass in Transaction2.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_transaction2_has_transactionTime():
    assert hasattr(Transaction2, "transactionTime")
    descriptor = None
    for klass in Transaction2.__mro__:
        if "transactionTime" in klass.__dict__:
            descriptor = klass.__dict__["transactionTime"]
            break
    assert isinstance(descriptor, property)

def test_transaction2_has_type():
    assert hasattr(Transaction2, "type")
    descriptor = None
    for klass in Transaction2.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_transaction2_has_id():
    assert hasattr(Transaction2, "id")
    descriptor = None
    for klass in Transaction2.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_bank2_is_not_abstract():
    assert not inspect.isabstract(Bank2)


def test_bank2_constructor_exists():
    assert callable(Bank2.__init__)


def test_bank2_constructor_args():
    sig = inspect.signature(Bank2.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "code" in params, "Missing parameter 'code'"

def test_bank2_has_address():
    assert hasattr(Bank2, "address")
    descriptor = None
    for klass in Bank2.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_bank2_has_code():
    assert hasattr(Bank2, "code")
    descriptor = None
    for klass in Bank2.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_savings_account2_is_not_abstract():
    assert not inspect.isabstract(Savings_Account2)


def test_savings_account2_constructor_exists():
    assert callable(Savings_Account2.__init__)


def test_savings_account2_constructor_args():
    sig = inspect.signature(Savings_Account2.__init__)
    params = list(sig.parameters.keys())
    assert "balance" in params, "Missing parameter 'balance'"
    assert "accountNumber" in params, "Missing parameter 'accountNumber'"

def test_savings_account2_has_balance():
    assert hasattr(Savings_Account2, "balance")
    descriptor = None
    for klass in Savings_Account2.__mro__:
        if "balance" in klass.__dict__:
            descriptor = klass.__dict__["balance"]
            break
    assert isinstance(descriptor, property)

def test_savings_account2_has_accountNumber():
    assert hasattr(Savings_Account2, "accountNumber")
    descriptor = None
    for klass in Savings_Account2.__mro__:
        if "accountNumber" in klass.__dict__:
            descriptor = klass.__dict__["accountNumber"]
            break
    assert isinstance(descriptor, property)



def test_account2_interface_is_not_abstract():
    assert not inspect.isabstract(Account2_Interface)


def test_account2_interface_constructor_exists():
    assert callable(Account2_Interface.__init__)


def test_account2_interface_constructor_args():
    sig = inspect.signature(Account2_Interface.__init__)
    params = list(sig.parameters.keys())



def test_customer2_is_not_abstract():
    assert not inspect.isabstract(Customer2)


def test_customer2_constructor_exists():
    assert callable(Customer2.__init__)


def test_customer2_constructor_args():
    sig = inspect.signature(Customer2.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"
    assert "emailAddress" in params, "Missing parameter 'emailAddress'"
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"
    assert "name" in params, "Missing parameter 'name'"

def test_customer2_has_address():
    assert hasattr(Customer2, "address")
    descriptor = None
    for klass in Customer2.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_customer2_has_dateOfBirth():
    assert hasattr(Customer2, "dateOfBirth")
    descriptor = None
    for klass in Customer2.__mro__:
        if "dateOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["dateOfBirth"]
            break
    assert isinstance(descriptor, property)

def test_customer2_has_emailAddress():
    assert hasattr(Customer2, "emailAddress")
    descriptor = None
    for klass in Customer2.__mro__:
        if "emailAddress" in klass.__dict__:
            descriptor = klass.__dict__["emailAddress"]
            break
    assert isinstance(descriptor, property)

def test_customer2_has_phoneNumber():
    assert hasattr(Customer2, "phoneNumber")
    descriptor = None
    for klass in Customer2.__mro__:
        if "phoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["phoneNumber"]
            break
    assert isinstance(descriptor, property)

def test_customer2_has_name():
    assert hasattr(Customer2, "name")
    descriptor = None
    for klass in Customer2.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_deposittransaction_is_not_abstract():
    assert not inspect.isabstract(DepositTransaction)


def test_deposittransaction_constructor_exists():
    assert callable(DepositTransaction.__init__)


def test_deposittransaction_constructor_args():
    sig = inspect.signature(DepositTransaction.__init__)
    params = list(sig.parameters.keys())



def test_transfertransaction_is_not_abstract():
    assert not inspect.isabstract(TransferTransaction)


def test_transfertransaction_constructor_exists():
    assert callable(TransferTransaction.__init__)


def test_transfertransaction_constructor_args():
    sig = inspect.signature(TransferTransaction.__init__)
    params = list(sig.parameters.keys())
    assert "sourceAccount" in params, "Missing parameter 'sourceAccount'"
    assert "targetAccount" in params, "Missing parameter 'targetAccount'"

def test_transfertransaction_has_sourceAccount():
    assert hasattr(TransferTransaction, "sourceAccount")
    descriptor = None
    for klass in TransferTransaction.__mro__:
        if "sourceAccount" in klass.__dict__:
            descriptor = klass.__dict__["sourceAccount"]
            break
    assert isinstance(descriptor, property)

def test_transfertransaction_has_targetAccount():
    assert hasattr(TransferTransaction, "targetAccount")
    descriptor = None
    for klass in TransferTransaction.__mro__:
        if "targetAccount" in klass.__dict__:
            descriptor = klass.__dict__["targetAccount"]
            break
    assert isinstance(descriptor, property)



def test_withdrawtransaction_is_not_abstract():
    assert not inspect.isabstract(WithdrawTransaction)


def test_withdrawtransaction_constructor_exists():
    assert callable(WithdrawTransaction.__init__)


def test_withdrawtransaction_constructor_args():
    sig = inspect.signature(WithdrawTransaction.__init__)
    params = list(sig.parameters.keys())



def test_atm_card_is_not_abstract():
    assert not inspect.isabstract(ATM_Card)


def test_atm_card_constructor_exists():
    assert callable(ATM_Card.__init__)


def test_atm_card_constructor_args():
    sig = inspect.signature(ATM_Card.__init__)
    params = list(sig.parameters.keys())
    assert "cardNumber" in params, "Missing parameter 'cardNumber'"
    assert "pin" in params, "Missing parameter 'pin'"

def test_atm_card_has_cardNumber():
    assert hasattr(ATM_Card, "cardNumber")
    descriptor = None
    for klass in ATM_Card.__mro__:
        if "cardNumber" in klass.__dict__:
            descriptor = klass.__dict__["cardNumber"]
            break
    assert isinstance(descriptor, property)

def test_atm_card_has_pin():
    assert hasattr(ATM_Card, "pin")
    descriptor = None
    for klass in ATM_Card.__mro__:
        if "pin" in klass.__dict__:
            descriptor = klass.__dict__["pin"]
            break
    assert isinstance(descriptor, property)



def test_transaction_is_not_abstract():
    assert not inspect.isabstract(Transaction)


def test_transaction_constructor_exists():
    assert callable(Transaction.__init__)


def test_transaction_constructor_args():
    sig = inspect.signature(Transaction.__init__)
    params = list(sig.parameters.keys())
    assert "transactionTime" in params, "Missing parameter 'transactionTime'"
    assert "id" in params, "Missing parameter 'id'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "type" in params, "Missing parameter 'type'"

def test_transaction_has_transactionTime():
    assert hasattr(Transaction, "transactionTime")
    descriptor = None
    for klass in Transaction.__mro__:
        if "transactionTime" in klass.__dict__:
            descriptor = klass.__dict__["transactionTime"]
            break
    assert isinstance(descriptor, property)

def test_transaction_has_id():
    assert hasattr(Transaction, "id")
    descriptor = None
    for klass in Transaction.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_transaction_has_amount():
    assert hasattr(Transaction, "amount")
    descriptor = None
    for klass in Transaction.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_transaction_has_type():
    assert hasattr(Transaction, "type")
    descriptor = None
    for klass in Transaction.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_bank_is_not_abstract():
    assert not inspect.isabstract(Bank)


def test_bank_constructor_exists():
    assert callable(Bank.__init__)


def test_bank_constructor_args():
    sig = inspect.signature(Bank.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "address" in params, "Missing parameter 'address'"

def test_bank_has_code():
    assert hasattr(Bank, "code")
    descriptor = None
    for klass in Bank.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_bank_has_address():
    assert hasattr(Bank, "address")
    descriptor = None
    for klass in Bank.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_savings_account_is_not_abstract():
    assert not inspect.isabstract(Savings_Account)


def test_savings_account_constructor_exists():
    assert callable(Savings_Account.__init__)


def test_savings_account_constructor_args():
    sig = inspect.signature(Savings_Account.__init__)
    params = list(sig.parameters.keys())
    assert "balance" in params, "Missing parameter 'balance'"
    assert "accountNumber" in params, "Missing parameter 'accountNumber'"

def test_savings_account_has_balance():
    assert hasattr(Savings_Account, "balance")
    descriptor = None
    for klass in Savings_Account.__mro__:
        if "balance" in klass.__dict__:
            descriptor = klass.__dict__["balance"]
            break
    assert isinstance(descriptor, property)

def test_savings_account_has_accountNumber():
    assert hasattr(Savings_Account, "accountNumber")
    descriptor = None
    for klass in Savings_Account.__mro__:
        if "accountNumber" in klass.__dict__:
            descriptor = klass.__dict__["accountNumber"]
            break
    assert isinstance(descriptor, property)



def test_account_interface_is_not_abstract():
    assert not inspect.isabstract(Account_Interface)


def test_account_interface_constructor_exists():
    assert callable(Account_Interface.__init__)


def test_account_interface_constructor_args():
    sig = inspect.signature(Account_Interface.__init__)
    params = list(sig.parameters.keys())



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "emailAddress" in params, "Missing parameter 'emailAddress'"
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"
    assert "address" in params, "Missing parameter 'address'"
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"

def test_customer_has_name():
    assert hasattr(Customer, "name")
    descriptor = None
    for klass in Customer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_emailAddress():
    assert hasattr(Customer, "emailAddress")
    descriptor = None
    for klass in Customer.__mro__:
        if "emailAddress" in klass.__dict__:
            descriptor = klass.__dict__["emailAddress"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_phoneNumber():
    assert hasattr(Customer, "phoneNumber")
    descriptor = None
    for klass in Customer.__mro__:
        if "phoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["phoneNumber"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_address():
    assert hasattr(Customer, "address")
    descriptor = None
    for klass in Customer.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_dateOfBirth():
    assert hasattr(Customer, "dateOfBirth")
    descriptor = None
    for klass in Customer.__mro__:
        if "dateOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["dateOfBirth"]
            break
    assert isinstance(descriptor, property)

def test_transactiontype2_exists():
    # Check that the Enumeration exists
    assert TransactionType2 is not None

def test_transactiontype2_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TransactionType2]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransactionType2"

def test_transactiontype_exists():
    # Check that the Enumeration exists
    assert TransactionType is not None

def test_transactiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TransactionType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransactionType"


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
DepositTransaction2_strategy = st.builds(
    DepositTransaction2,
)
TransferTransaction2_strategy = st.builds(
    TransferTransaction2,
    targetAccount=
        safe_text,
    sourceAccount=
        safe_text
)
WithdrawTransaction2_strategy = st.builds(
    WithdrawTransaction2,
)
ATM_Card2_strategy = st.builds(
    ATM_Card2,
    cardNumber=
        safe_text,
    pin=
        safe_text
)
Transaction2_strategy = st.builds(
    Transaction2,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    transactionTime=
        st.dates(),
    type=
        st.none(),
    id=
        st.integers()
)
Bank2_strategy = st.builds(
    Bank2,
    address=
        safe_text,
    code=
        safe_text
)
Savings_Account2_strategy = st.builds(
    Savings_Account2,
    balance=
        st.integers(),
    accountNumber=
        safe_text
)
Account2_Interface_strategy = st.builds(
    Account2_Interface,
)
Customer2_strategy = st.builds(
    Customer2,
    address=
        safe_text,
    dateOfBirth=
        st.dates(),
    emailAddress=
        safe_text,
    phoneNumber=
        safe_text,
    name=
        safe_text
)
DepositTransaction_strategy = st.builds(
    DepositTransaction,
)
TransferTransaction_strategy = st.builds(
    TransferTransaction,
    sourceAccount=
        safe_text,
    targetAccount=
        safe_text
)
WithdrawTransaction_strategy = st.builds(
    WithdrawTransaction,
)
ATM_Card_strategy = st.builds(
    ATM_Card,
    cardNumber=
        safe_text,
    pin=
        safe_text
)
Transaction_strategy = st.builds(
    Transaction,
    transactionTime=
        st.dates(),
    id=
        st.integers(),
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    type=
        st.none()
)
Bank_strategy = st.builds(
    Bank,
    code=
        safe_text,
    address=
        safe_text
)
Savings_Account_strategy = st.builds(
    Savings_Account,
    balance=
        st.integers(),
    accountNumber=
        safe_text
)
Account_Interface_strategy = st.builds(
    Account_Interface,
)
Customer_strategy = st.builds(
    Customer,
    name=
        safe_text,
    emailAddress=
        safe_text,
    phoneNumber=
        safe_text,
    address=
        safe_text,
    dateOfBirth=
        st.dates()
)

@given(instance=DepositTransaction2_strategy)
@settings(max_examples=50)
def test_deposittransaction2_instantiation(instance):
    assert isinstance(instance, DepositTransaction2)

@given(instance=TransferTransaction2_strategy)
@settings(max_examples=50)
def test_transfertransaction2_instantiation(instance):
    assert isinstance(instance, TransferTransaction2)



@given(instance=TransferTransaction2_strategy)
def test_transfertransaction2_targetAccount_setter(instance):
    original = instance.targetAccount
    instance.targetAccount = original
    assert instance.targetAccount == original



@given(instance=TransferTransaction2_strategy)
def test_transfertransaction2_sourceAccount_setter(instance):
    original = instance.sourceAccount
    instance.sourceAccount = original
    assert instance.sourceAccount == original

@given(instance=WithdrawTransaction2_strategy)
@settings(max_examples=50)
def test_withdrawtransaction2_instantiation(instance):
    assert isinstance(instance, WithdrawTransaction2)

@given(instance=ATM_Card2_strategy)
@settings(max_examples=50)
def test_atm_card2_instantiation(instance):
    assert isinstance(instance, ATM_Card2)



@given(instance=ATM_Card2_strategy)
def test_atm_card2_cardNumber_setter(instance):
    original = instance.cardNumber
    instance.cardNumber = original
    assert instance.cardNumber == original



@given(instance=ATM_Card2_strategy)
def test_atm_card2_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original

@given(instance=Transaction2_strategy)
@settings(max_examples=50)
def test_transaction2_instantiation(instance):
    assert isinstance(instance, Transaction2)



@given(instance=Transaction2_strategy)
def test_transaction2_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Transaction2_strategy)
def test_transaction2_transactionTime_setter(instance):
    original = instance.transactionTime
    instance.transactionTime = original
    assert instance.transactionTime == original



@given(instance=Transaction2_strategy)
def test_transaction2_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Transaction2_strategy)
def test_transaction2_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Bank2_strategy)
@settings(max_examples=50)
def test_bank2_instantiation(instance):
    assert isinstance(instance, Bank2)



@given(instance=Bank2_strategy)
def test_bank2_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Bank2_strategy)
def test_bank2_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=Savings_Account2_strategy)
@settings(max_examples=50)
def test_savings_account2_instantiation(instance):
    assert isinstance(instance, Savings_Account2)



@given(instance=Savings_Account2_strategy)
def test_savings_account2_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original



@given(instance=Savings_Account2_strategy)
def test_savings_account2_accountNumber_setter(instance):
    original = instance.accountNumber
    instance.accountNumber = original
    assert instance.accountNumber == original

@given(instance=Account2_Interface_strategy)
@settings(max_examples=50)
def test_account2_interface_instantiation(instance):
    assert isinstance(instance, Account2_Interface)

@given(instance=Customer2_strategy)
@settings(max_examples=50)
def test_customer2_instantiation(instance):
    assert isinstance(instance, Customer2)



@given(instance=Customer2_strategy)
def test_customer2_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Customer2_strategy)
def test_customer2_dateOfBirth_setter(instance):
    original = instance.dateOfBirth
    instance.dateOfBirth = original
    assert instance.dateOfBirth == original



@given(instance=Customer2_strategy)
def test_customer2_emailAddress_setter(instance):
    original = instance.emailAddress
    instance.emailAddress = original
    assert instance.emailAddress == original



@given(instance=Customer2_strategy)
def test_customer2_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original



@given(instance=Customer2_strategy)
def test_customer2_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DepositTransaction_strategy)
@settings(max_examples=50)
def test_deposittransaction_instantiation(instance):
    assert isinstance(instance, DepositTransaction)

@given(instance=TransferTransaction_strategy)
@settings(max_examples=50)
def test_transfertransaction_instantiation(instance):
    assert isinstance(instance, TransferTransaction)



@given(instance=TransferTransaction_strategy)
def test_transfertransaction_sourceAccount_setter(instance):
    original = instance.sourceAccount
    instance.sourceAccount = original
    assert instance.sourceAccount == original



@given(instance=TransferTransaction_strategy)
def test_transfertransaction_targetAccount_setter(instance):
    original = instance.targetAccount
    instance.targetAccount = original
    assert instance.targetAccount == original

@given(instance=WithdrawTransaction_strategy)
@settings(max_examples=50)
def test_withdrawtransaction_instantiation(instance):
    assert isinstance(instance, WithdrawTransaction)

@given(instance=ATM_Card_strategy)
@settings(max_examples=50)
def test_atm_card_instantiation(instance):
    assert isinstance(instance, ATM_Card)



@given(instance=ATM_Card_strategy)
def test_atm_card_cardNumber_setter(instance):
    original = instance.cardNumber
    instance.cardNumber = original
    assert instance.cardNumber == original



@given(instance=ATM_Card_strategy)
def test_atm_card_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original

@given(instance=Transaction_strategy)
@settings(max_examples=50)
def test_transaction_instantiation(instance):
    assert isinstance(instance, Transaction)



@given(instance=Transaction_strategy)
def test_transaction_transactionTime_setter(instance):
    original = instance.transactionTime
    instance.transactionTime = original
    assert instance.transactionTime == original



@given(instance=Transaction_strategy)
def test_transaction_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Transaction_strategy)
def test_transaction_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Transaction_strategy)
def test_transaction_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Bank_strategy)
@settings(max_examples=50)
def test_bank_instantiation(instance):
    assert isinstance(instance, Bank)



@given(instance=Bank_strategy)
def test_bank_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=Bank_strategy)
def test_bank_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=Savings_Account_strategy)
@settings(max_examples=50)
def test_savings_account_instantiation(instance):
    assert isinstance(instance, Savings_Account)



@given(instance=Savings_Account_strategy)
def test_savings_account_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original



@given(instance=Savings_Account_strategy)
def test_savings_account_accountNumber_setter(instance):
    original = instance.accountNumber
    instance.accountNumber = original
    assert instance.accountNumber == original

@given(instance=Account_Interface_strategy)
@settings(max_examples=50)
def test_account_interface_instantiation(instance):
    assert isinstance(instance, Account_Interface)

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Customer_strategy)
def test_customer_emailAddress_setter(instance):
    original = instance.emailAddress
    instance.emailAddress = original
    assert instance.emailAddress == original



@given(instance=Customer_strategy)
def test_customer_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original



@given(instance=Customer_strategy)
def test_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Customer_strategy)
def test_customer_dateOfBirth_setter(instance):
    original = instance.dateOfBirth
    instance.dateOfBirth = original
    assert instance.dateOfBirth == original
