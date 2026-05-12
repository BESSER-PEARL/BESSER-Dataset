import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ExternalAccount,
    TransferTransaction,
    Transaction3,
    Account2,
    Transaction1,
    Account1,
    Transaction2,
    Transaction,
    Account,
    String,
    loan_LoanApplicationFile,
    loan_Loan,
    loan_LoanApplication,
    account_Account,
    account_SavingsAccount,
    transaction_LoanPayment,
    transaction_Payee,
    transaction_ExternalAccount,
    transaction_PaybillsTransaction,
    transaction_TransferTransaction,
    transaction_DepositTransaction,
    transaction_Transaction,
    User,
    Profile,
    transaction_TransactionType,
    account_AccountType,
    loan_LoanStatus,
    loan_ApplicationStatus,
    TransactionType,
    loan_LoanType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_externalaccount_is_not_abstract():
    assert not inspect.isabstract(ExternalAccount)


def test_externalaccount_constructor_exists():
    assert callable(ExternalAccount.__init__)


def test_externalaccount_constructor_args():
    sig = inspect.signature(ExternalAccount.__init__)
    params = list(sig.parameters.keys())
    assert "routingNum" in params, "Missing parameter 'routingNum'"
    assert "associatedAccount" in params, "Missing parameter 'associatedAccount'"
    assert "accountNum" in params, "Missing parameter 'accountNum'"

def test_externalaccount_has_routingNum():
    assert hasattr(ExternalAccount, "routingNum")
    descriptor = None
    for klass in ExternalAccount.__mro__:
        if "routingNum" in klass.__dict__:
            descriptor = klass.__dict__["routingNum"]
            break
    assert isinstance(descriptor, property)

def test_externalaccount_has_associatedAccount():
    assert hasattr(ExternalAccount, "associatedAccount")
    descriptor = None
    for klass in ExternalAccount.__mro__:
        if "associatedAccount" in klass.__dict__:
            descriptor = klass.__dict__["associatedAccount"]
            break
    assert isinstance(descriptor, property)

def test_externalaccount_has_accountNum():
    assert hasattr(ExternalAccount, "accountNum")
    descriptor = None
    for klass in ExternalAccount.__mro__:
        if "accountNum" in klass.__dict__:
            descriptor = klass.__dict__["accountNum"]
            break
    assert isinstance(descriptor, property)



def test_transfertransaction_is_not_abstract():
    assert not inspect.isabstract(TransferTransaction)


def test_transfertransaction_constructor_exists():
    assert callable(TransferTransaction.__init__)


def test_transfertransaction_constructor_args():
    sig = inspect.signature(TransferTransaction.__init__)
    params = list(sig.parameters.keys())



def test_transaction3_is_not_abstract():
    assert not inspect.isabstract(Transaction3)


def test_transaction3_constructor_exists():
    assert callable(Transaction3.__init__)


def test_transaction3_constructor_args():
    sig = inspect.signature(Transaction3.__init__)
    params = list(sig.parameters.keys())
    assert "destinationAccountNum" in params, "Missing parameter 'destinationAccountNum'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "time" in params, "Missing parameter 'time'"
    assert "transactionID" in params, "Missing parameter 'transactionID'"
    assert "type" in params, "Missing parameter 'type'"
    assert "sourceAccountNum" in params, "Missing parameter 'sourceAccountNum'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "description" in params, "Missing parameter 'description'"

def test_transaction3_has_destinationAccountNum():
    assert hasattr(Transaction3, "destinationAccountNum")
    descriptor = None
    for klass in Transaction3.__mro__:
        if "destinationAccountNum" in klass.__dict__:
            descriptor = klass.__dict__["destinationAccountNum"]
            break
    assert isinstance(descriptor, property)

def test_transaction3_has_amount():
    assert hasattr(Transaction3, "amount")
    descriptor = None
    for klass in Transaction3.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_transaction3_has_time():
    assert hasattr(Transaction3, "time")
    descriptor = None
    for klass in Transaction3.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_transaction3_has_transactionID():
    assert hasattr(Transaction3, "transactionID")
    descriptor = None
    for klass in Transaction3.__mro__:
        if "transactionID" in klass.__dict__:
            descriptor = klass.__dict__["transactionID"]
            break
    assert isinstance(descriptor, property)

def test_transaction3_has_type():
    assert hasattr(Transaction3, "type")
    descriptor = None
    for klass in Transaction3.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_transaction3_has_sourceAccountNum():
    assert hasattr(Transaction3, "sourceAccountNum")
    descriptor = None
    for klass in Transaction3.__mro__:
        if "sourceAccountNum" in klass.__dict__:
            descriptor = klass.__dict__["sourceAccountNum"]
            break
    assert isinstance(descriptor, property)

def test_transaction3_has_comment():
    assert hasattr(Transaction3, "comment")
    descriptor = None
    for klass in Transaction3.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_transaction3_has_description():
    assert hasattr(Transaction3, "description")
    descriptor = None
    for klass in Transaction3.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_account2_is_not_abstract():
    assert not inspect.isabstract(Account2)


def test_account2_constructor_exists():
    assert callable(Account2.__init__)


def test_account2_constructor_args():
    sig = inspect.signature(Account2.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "pin" in params, "Missing parameter 'pin'"
    assert "userID" in params, "Missing parameter 'userID'"
    assert "accountNum" in params, "Missing parameter 'accountNum'"
    assert "balance" in params, "Missing parameter 'balance'"

def test_account2_has_type():
    assert hasattr(Account2, "type")
    descriptor = None
    for klass in Account2.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_account2_has_pin():
    assert hasattr(Account2, "pin")
    descriptor = None
    for klass in Account2.__mro__:
        if "pin" in klass.__dict__:
            descriptor = klass.__dict__["pin"]
            break
    assert isinstance(descriptor, property)

def test_account2_has_userID():
    assert hasattr(Account2, "userID")
    descriptor = None
    for klass in Account2.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)

def test_account2_has_accountNum():
    assert hasattr(Account2, "accountNum")
    descriptor = None
    for klass in Account2.__mro__:
        if "accountNum" in klass.__dict__:
            descriptor = klass.__dict__["accountNum"]
            break
    assert isinstance(descriptor, property)

def test_account2_has_balance():
    assert hasattr(Account2, "balance")
    descriptor = None
    for klass in Account2.__mro__:
        if "balance" in klass.__dict__:
            descriptor = klass.__dict__["balance"]
            break
    assert isinstance(descriptor, property)



def test_transaction1_is_not_abstract():
    assert not inspect.isabstract(Transaction1)


def test_transaction1_constructor_exists():
    assert callable(Transaction1.__init__)


def test_transaction1_constructor_args():
    sig = inspect.signature(Transaction1.__init__)
    params = list(sig.parameters.keys())
    assert "destinationAccountNum" in params, "Missing parameter 'destinationAccountNum'"
    assert "type" in params, "Missing parameter 'type'"
    assert "description" in params, "Missing parameter 'description'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "transactionID" in params, "Missing parameter 'transactionID'"
    assert "time" in params, "Missing parameter 'time'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "sourceAccountNum" in params, "Missing parameter 'sourceAccountNum'"

def test_transaction1_has_destinationAccountNum():
    assert hasattr(Transaction1, "destinationAccountNum")
    descriptor = None
    for klass in Transaction1.__mro__:
        if "destinationAccountNum" in klass.__dict__:
            descriptor = klass.__dict__["destinationAccountNum"]
            break
    assert isinstance(descriptor, property)

def test_transaction1_has_type():
    assert hasattr(Transaction1, "type")
    descriptor = None
    for klass in Transaction1.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_transaction1_has_description():
    assert hasattr(Transaction1, "description")
    descriptor = None
    for klass in Transaction1.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_transaction1_has_amount():
    assert hasattr(Transaction1, "amount")
    descriptor = None
    for klass in Transaction1.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_transaction1_has_transactionID():
    assert hasattr(Transaction1, "transactionID")
    descriptor = None
    for klass in Transaction1.__mro__:
        if "transactionID" in klass.__dict__:
            descriptor = klass.__dict__["transactionID"]
            break
    assert isinstance(descriptor, property)

def test_transaction1_has_time():
    assert hasattr(Transaction1, "time")
    descriptor = None
    for klass in Transaction1.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_transaction1_has_comment():
    assert hasattr(Transaction1, "comment")
    descriptor = None
    for klass in Transaction1.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_transaction1_has_sourceAccountNum():
    assert hasattr(Transaction1, "sourceAccountNum")
    descriptor = None
    for klass in Transaction1.__mro__:
        if "sourceAccountNum" in klass.__dict__:
            descriptor = klass.__dict__["sourceAccountNum"]
            break
    assert isinstance(descriptor, property)



def test_account1_is_not_abstract():
    assert not inspect.isabstract(Account1)


def test_account1_constructor_exists():
    assert callable(Account1.__init__)


def test_account1_constructor_args():
    sig = inspect.signature(Account1.__init__)
    params = list(sig.parameters.keys())
    assert "balance" in params, "Missing parameter 'balance'"
    assert "type" in params, "Missing parameter 'type'"
    assert "pin" in params, "Missing parameter 'pin'"
    assert "accountNum" in params, "Missing parameter 'accountNum'"
    assert "userID" in params, "Missing parameter 'userID'"

def test_account1_has_balance():
    assert hasattr(Account1, "balance")
    descriptor = None
    for klass in Account1.__mro__:
        if "balance" in klass.__dict__:
            descriptor = klass.__dict__["balance"]
            break
    assert isinstance(descriptor, property)

def test_account1_has_type():
    assert hasattr(Account1, "type")
    descriptor = None
    for klass in Account1.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_account1_has_pin():
    assert hasattr(Account1, "pin")
    descriptor = None
    for klass in Account1.__mro__:
        if "pin" in klass.__dict__:
            descriptor = klass.__dict__["pin"]
            break
    assert isinstance(descriptor, property)

def test_account1_has_accountNum():
    assert hasattr(Account1, "accountNum")
    descriptor = None
    for klass in Account1.__mro__:
        if "accountNum" in klass.__dict__:
            descriptor = klass.__dict__["accountNum"]
            break
    assert isinstance(descriptor, property)

def test_account1_has_userID():
    assert hasattr(Account1, "userID")
    descriptor = None
    for klass in Account1.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)



def test_transaction2_is_not_abstract():
    assert not inspect.isabstract(Transaction2)


def test_transaction2_constructor_exists():
    assert callable(Transaction2.__init__)


def test_transaction2_constructor_args():
    sig = inspect.signature(Transaction2.__init__)
    params = list(sig.parameters.keys())
    assert "sourceAccountNum" in params, "Missing parameter 'sourceAccountNum'"
    assert "type" in params, "Missing parameter 'type'"
    assert "time" in params, "Missing parameter 'time'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "description" in params, "Missing parameter 'description'"
    assert "transactionID" in params, "Missing parameter 'transactionID'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "destinationAccountNum" in params, "Missing parameter 'destinationAccountNum'"

def test_transaction2_has_sourceAccountNum():
    assert hasattr(Transaction2, "sourceAccountNum")
    descriptor = None
    for klass in Transaction2.__mro__:
        if "sourceAccountNum" in klass.__dict__:
            descriptor = klass.__dict__["sourceAccountNum"]
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

def test_transaction2_has_time():
    assert hasattr(Transaction2, "time")
    descriptor = None
    for klass in Transaction2.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_transaction2_has_amount():
    assert hasattr(Transaction2, "amount")
    descriptor = None
    for klass in Transaction2.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_transaction2_has_description():
    assert hasattr(Transaction2, "description")
    descriptor = None
    for klass in Transaction2.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_transaction2_has_transactionID():
    assert hasattr(Transaction2, "transactionID")
    descriptor = None
    for klass in Transaction2.__mro__:
        if "transactionID" in klass.__dict__:
            descriptor = klass.__dict__["transactionID"]
            break
    assert isinstance(descriptor, property)

def test_transaction2_has_comment():
    assert hasattr(Transaction2, "comment")
    descriptor = None
    for klass in Transaction2.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_transaction2_has_destinationAccountNum():
    assert hasattr(Transaction2, "destinationAccountNum")
    descriptor = None
    for klass in Transaction2.__mro__:
        if "destinationAccountNum" in klass.__dict__:
            descriptor = klass.__dict__["destinationAccountNum"]
            break
    assert isinstance(descriptor, property)



def test_transaction_is_not_abstract():
    assert not inspect.isabstract(Transaction)


def test_transaction_constructor_exists():
    assert callable(Transaction.__init__)


def test_transaction_constructor_args():
    sig = inspect.signature(Transaction.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "transactionID" in params, "Missing parameter 'transactionID'"
    assert "time" in params, "Missing parameter 'time'"
    assert "sourceAccountNum" in params, "Missing parameter 'sourceAccountNum'"
    assert "destinationAccountNum" in params, "Missing parameter 'destinationAccountNum'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "type" in params, "Missing parameter 'type'"

def test_transaction_has_description():
    assert hasattr(Transaction, "description")
    descriptor = None
    for klass in Transaction.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_transaction_has_comment():
    assert hasattr(Transaction, "comment")
    descriptor = None
    for klass in Transaction.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_transaction_has_transactionID():
    assert hasattr(Transaction, "transactionID")
    descriptor = None
    for klass in Transaction.__mro__:
        if "transactionID" in klass.__dict__:
            descriptor = klass.__dict__["transactionID"]
            break
    assert isinstance(descriptor, property)

def test_transaction_has_time():
    assert hasattr(Transaction, "time")
    descriptor = None
    for klass in Transaction.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_transaction_has_sourceAccountNum():
    assert hasattr(Transaction, "sourceAccountNum")
    descriptor = None
    for klass in Transaction.__mro__:
        if "sourceAccountNum" in klass.__dict__:
            descriptor = klass.__dict__["sourceAccountNum"]
            break
    assert isinstance(descriptor, property)

def test_transaction_has_destinationAccountNum():
    assert hasattr(Transaction, "destinationAccountNum")
    descriptor = None
    for klass in Transaction.__mro__:
        if "destinationAccountNum" in klass.__dict__:
            descriptor = klass.__dict__["destinationAccountNum"]
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



def test_account_is_not_abstract():
    assert not inspect.isabstract(Account)


def test_account_constructor_exists():
    assert callable(Account.__init__)


def test_account_constructor_args():
    sig = inspect.signature(Account.__init__)
    params = list(sig.parameters.keys())
    assert "balance" in params, "Missing parameter 'balance'"
    assert "pin" in params, "Missing parameter 'pin'"
    assert "type" in params, "Missing parameter 'type'"
    assert "userID" in params, "Missing parameter 'userID'"
    assert "accountNum" in params, "Missing parameter 'accountNum'"

def test_account_has_balance():
    assert hasattr(Account, "balance")
    descriptor = None
    for klass in Account.__mro__:
        if "balance" in klass.__dict__:
            descriptor = klass.__dict__["balance"]
            break
    assert isinstance(descriptor, property)

def test_account_has_pin():
    assert hasattr(Account, "pin")
    descriptor = None
    for klass in Account.__mro__:
        if "pin" in klass.__dict__:
            descriptor = klass.__dict__["pin"]
            break
    assert isinstance(descriptor, property)

def test_account_has_type():
    assert hasattr(Account, "type")
    descriptor = None
    for klass in Account.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_account_has_userID():
    assert hasattr(Account, "userID")
    descriptor = None
    for klass in Account.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)

def test_account_has_accountNum():
    assert hasattr(Account, "accountNum")
    descriptor = None
    for klass in Account.__mro__:
        if "accountNum" in klass.__dict__:
            descriptor = klass.__dict__["accountNum"]
            break
    assert isinstance(descriptor, property)



def test_string_is_not_abstract():
    assert not inspect.isabstract(String)


def test_string_constructor_exists():
    assert callable(String.__init__)


def test_string_constructor_args():
    sig = inspect.signature(String.__init__)
    params = list(sig.parameters.keys())



def test_loan_loanapplicationfile_is_not_abstract():
    assert not inspect.isabstract(loan_LoanApplicationFile)


def test_loan_loanapplicationfile_constructor_exists():
    assert callable(loan_LoanApplicationFile.__init__)


def test_loan_loanapplicationfile_constructor_args():
    sig = inspect.signature(loan_LoanApplicationFile.__init__)
    params = list(sig.parameters.keys())
    assert "fileID" in params, "Missing parameter 'fileID'"
    assert "applicationID" in params, "Missing parameter 'applicationID'"

def test_loan_loanapplicationfile_has_fileID():
    assert hasattr(loan_LoanApplicationFile, "fileID")
    descriptor = None
    for klass in loan_LoanApplicationFile.__mro__:
        if "fileID" in klass.__dict__:
            descriptor = klass.__dict__["fileID"]
            break
    assert isinstance(descriptor, property)

def test_loan_loanapplicationfile_has_applicationID():
    assert hasattr(loan_LoanApplicationFile, "applicationID")
    descriptor = None
    for klass in loan_LoanApplicationFile.__mro__:
        if "applicationID" in klass.__dict__:
            descriptor = klass.__dict__["applicationID"]
            break
    assert isinstance(descriptor, property)



def test_loan_loan_is_not_abstract():
    assert not inspect.isabstract(loan_Loan)


def test_loan_loan_constructor_exists():
    assert callable(loan_Loan.__init__)


def test_loan_loan_constructor_args():
    sig = inspect.signature(loan_Loan.__init__)
    params = list(sig.parameters.keys())
    assert "interestRate" in params, "Missing parameter 'interestRate'"
    assert "userID" in params, "Missing parameter 'userID'"
    assert "term" in params, "Missing parameter 'term'"
    assert "type" in params, "Missing parameter 'type'"
    assert "submissionTime" in params, "Missing parameter 'submissionTime'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "status" in params, "Missing parameter 'status'"
    assert "loanID" in params, "Missing parameter 'loanID'"

def test_loan_loan_has_interestRate():
    assert hasattr(loan_Loan, "interestRate")
    descriptor = None
    for klass in loan_Loan.__mro__:
        if "interestRate" in klass.__dict__:
            descriptor = klass.__dict__["interestRate"]
            break
    assert isinstance(descriptor, property)

def test_loan_loan_has_userID():
    assert hasattr(loan_Loan, "userID")
    descriptor = None
    for klass in loan_Loan.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)

def test_loan_loan_has_term():
    assert hasattr(loan_Loan, "term")
    descriptor = None
    for klass in loan_Loan.__mro__:
        if "term" in klass.__dict__:
            descriptor = klass.__dict__["term"]
            break
    assert isinstance(descriptor, property)

def test_loan_loan_has_type():
    assert hasattr(loan_Loan, "type")
    descriptor = None
    for klass in loan_Loan.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_loan_loan_has_submissionTime():
    assert hasattr(loan_Loan, "submissionTime")
    descriptor = None
    for klass in loan_Loan.__mro__:
        if "submissionTime" in klass.__dict__:
            descriptor = klass.__dict__["submissionTime"]
            break
    assert isinstance(descriptor, property)

def test_loan_loan_has_amount():
    assert hasattr(loan_Loan, "amount")
    descriptor = None
    for klass in loan_Loan.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_loan_loan_has_status():
    assert hasattr(loan_Loan, "status")
    descriptor = None
    for klass in loan_Loan.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_loan_loan_has_loanID():
    assert hasattr(loan_Loan, "loanID")
    descriptor = None
    for klass in loan_Loan.__mro__:
        if "loanID" in klass.__dict__:
            descriptor = klass.__dict__["loanID"]
            break
    assert isinstance(descriptor, property)



def test_loan_loanapplication_is_not_abstract():
    assert not inspect.isabstract(loan_LoanApplication)


def test_loan_loanapplication_constructor_exists():
    assert callable(loan_LoanApplication.__init__)


def test_loan_loanapplication_constructor_args():
    sig = inspect.signature(loan_LoanApplication.__init__)
    params = list(sig.parameters.keys())
    assert "submissionTime" in params, "Missing parameter 'submissionTime'"
    assert "interestRate" in params, "Missing parameter 'interestRate'"
    assert "status" in params, "Missing parameter 'status'"
    assert "applicationID" in params, "Missing parameter 'applicationID'"
    assert "userID" in params, "Missing parameter 'userID'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "term" in params, "Missing parameter 'term'"
    assert "type" in params, "Missing parameter 'type'"

def test_loan_loanapplication_has_submissionTime():
    assert hasattr(loan_LoanApplication, "submissionTime")
    descriptor = None
    for klass in loan_LoanApplication.__mro__:
        if "submissionTime" in klass.__dict__:
            descriptor = klass.__dict__["submissionTime"]
            break
    assert isinstance(descriptor, property)

def test_loan_loanapplication_has_interestRate():
    assert hasattr(loan_LoanApplication, "interestRate")
    descriptor = None
    for klass in loan_LoanApplication.__mro__:
        if "interestRate" in klass.__dict__:
            descriptor = klass.__dict__["interestRate"]
            break
    assert isinstance(descriptor, property)

def test_loan_loanapplication_has_status():
    assert hasattr(loan_LoanApplication, "status")
    descriptor = None
    for klass in loan_LoanApplication.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_loan_loanapplication_has_applicationID():
    assert hasattr(loan_LoanApplication, "applicationID")
    descriptor = None
    for klass in loan_LoanApplication.__mro__:
        if "applicationID" in klass.__dict__:
            descriptor = klass.__dict__["applicationID"]
            break
    assert isinstance(descriptor, property)

def test_loan_loanapplication_has_userID():
    assert hasattr(loan_LoanApplication, "userID")
    descriptor = None
    for klass in loan_LoanApplication.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)

def test_loan_loanapplication_has_amount():
    assert hasattr(loan_LoanApplication, "amount")
    descriptor = None
    for klass in loan_LoanApplication.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_loan_loanapplication_has_term():
    assert hasattr(loan_LoanApplication, "term")
    descriptor = None
    for klass in loan_LoanApplication.__mro__:
        if "term" in klass.__dict__:
            descriptor = klass.__dict__["term"]
            break
    assert isinstance(descriptor, property)

def test_loan_loanapplication_has_type():
    assert hasattr(loan_LoanApplication, "type")
    descriptor = None
    for klass in loan_LoanApplication.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_account_account_is_not_abstract():
    assert not inspect.isabstract(account_Account)


def test_account_account_constructor_exists():
    assert callable(account_Account.__init__)


def test_account_account_constructor_args():
    sig = inspect.signature(account_Account.__init__)
    params = list(sig.parameters.keys())
    assert "userID" in params, "Missing parameter 'userID'"
    assert "accountNum" in params, "Missing parameter 'accountNum'"
    assert "type" in params, "Missing parameter 'type'"
    assert "pin" in params, "Missing parameter 'pin'"
    assert "balance" in params, "Missing parameter 'balance'"

def test_account_account_has_userID():
    assert hasattr(account_Account, "userID")
    descriptor = None
    for klass in account_Account.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)

def test_account_account_has_accountNum():
    assert hasattr(account_Account, "accountNum")
    descriptor = None
    for klass in account_Account.__mro__:
        if "accountNum" in klass.__dict__:
            descriptor = klass.__dict__["accountNum"]
            break
    assert isinstance(descriptor, property)

def test_account_account_has_type():
    assert hasattr(account_Account, "type")
    descriptor = None
    for klass in account_Account.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_account_account_has_pin():
    assert hasattr(account_Account, "pin")
    descriptor = None
    for klass in account_Account.__mro__:
        if "pin" in klass.__dict__:
            descriptor = klass.__dict__["pin"]
            break
    assert isinstance(descriptor, property)

def test_account_account_has_balance():
    assert hasattr(account_Account, "balance")
    descriptor = None
    for klass in account_Account.__mro__:
        if "balance" in klass.__dict__:
            descriptor = klass.__dict__["balance"]
            break
    assert isinstance(descriptor, property)



def test_account_savingsaccount_is_not_abstract():
    assert not inspect.isabstract(account_SavingsAccount)


def test_account_savingsaccount_constructor_exists():
    assert callable(account_SavingsAccount.__init__)


def test_account_savingsaccount_constructor_args():
    sig = inspect.signature(account_SavingsAccount.__init__)
    params = list(sig.parameters.keys())
    assert "interestRate" in params, "Missing parameter 'interestRate'"

def test_account_savingsaccount_has_interestRate():
    assert hasattr(account_SavingsAccount, "interestRate")
    descriptor = None
    for klass in account_SavingsAccount.__mro__:
        if "interestRate" in klass.__dict__:
            descriptor = klass.__dict__["interestRate"]
            break
    assert isinstance(descriptor, property)



def test_transaction_loanpayment_is_not_abstract():
    assert not inspect.isabstract(transaction_LoanPayment)


def test_transaction_loanpayment_constructor_exists():
    assert callable(transaction_LoanPayment.__init__)


def test_transaction_loanpayment_constructor_args():
    sig = inspect.signature(transaction_LoanPayment.__init__)
    params = list(sig.parameters.keys())
    assert "interest" in params, "Missing parameter 'interest'"
    assert "principal" in params, "Missing parameter 'principal'"
    assert "loanID" in params, "Missing parameter 'loanID'"

def test_transaction_loanpayment_has_interest():
    assert hasattr(transaction_LoanPayment, "interest")
    descriptor = None
    for klass in transaction_LoanPayment.__mro__:
        if "interest" in klass.__dict__:
            descriptor = klass.__dict__["interest"]
            break
    assert isinstance(descriptor, property)

def test_transaction_loanpayment_has_principal():
    assert hasattr(transaction_LoanPayment, "principal")
    descriptor = None
    for klass in transaction_LoanPayment.__mro__:
        if "principal" in klass.__dict__:
            descriptor = klass.__dict__["principal"]
            break
    assert isinstance(descriptor, property)

def test_transaction_loanpayment_has_loanID():
    assert hasattr(transaction_LoanPayment, "loanID")
    descriptor = None
    for klass in transaction_LoanPayment.__mro__:
        if "loanID" in klass.__dict__:
            descriptor = klass.__dict__["loanID"]
            break
    assert isinstance(descriptor, property)



def test_transaction_payee_is_not_abstract():
    assert not inspect.isabstract(transaction_Payee)


def test_transaction_payee_constructor_exists():
    assert callable(transaction_Payee.__init__)


def test_transaction_payee_constructor_args():
    sig = inspect.signature(transaction_Payee.__init__)
    params = list(sig.parameters.keys())
    assert "userID" in params, "Missing parameter 'userID'"
    assert "address2" in params, "Missing parameter 'address2'"
    assert "zipcode" in params, "Missing parameter 'zipcode'"
    assert "country" in params, "Missing parameter 'country'"
    assert "city" in params, "Missing parameter 'city'"
    assert "state" in params, "Missing parameter 'state'"
    assert "email" in params, "Missing parameter 'email'"
    assert "name" in params, "Missing parameter 'name'"
    assert "phoneNum" in params, "Missing parameter 'phoneNum'"
    assert "address1" in params, "Missing parameter 'address1'"
    assert "accountNum" in params, "Missing parameter 'accountNum'"

def test_transaction_payee_has_userID():
    assert hasattr(transaction_Payee, "userID")
    descriptor = None
    for klass in transaction_Payee.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)

def test_transaction_payee_has_address2():
    assert hasattr(transaction_Payee, "address2")
    descriptor = None
    for klass in transaction_Payee.__mro__:
        if "address2" in klass.__dict__:
            descriptor = klass.__dict__["address2"]
            break
    assert isinstance(descriptor, property)

def test_transaction_payee_has_zipcode():
    assert hasattr(transaction_Payee, "zipcode")
    descriptor = None
    for klass in transaction_Payee.__mro__:
        if "zipcode" in klass.__dict__:
            descriptor = klass.__dict__["zipcode"]
            break
    assert isinstance(descriptor, property)

def test_transaction_payee_has_country():
    assert hasattr(transaction_Payee, "country")
    descriptor = None
    for klass in transaction_Payee.__mro__:
        if "country" in klass.__dict__:
            descriptor = klass.__dict__["country"]
            break
    assert isinstance(descriptor, property)

def test_transaction_payee_has_city():
    assert hasattr(transaction_Payee, "city")
    descriptor = None
    for klass in transaction_Payee.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_transaction_payee_has_state():
    assert hasattr(transaction_Payee, "state")
    descriptor = None
    for klass in transaction_Payee.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_transaction_payee_has_email():
    assert hasattr(transaction_Payee, "email")
    descriptor = None
    for klass in transaction_Payee.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_transaction_payee_has_name():
    assert hasattr(transaction_Payee, "name")
    descriptor = None
    for klass in transaction_Payee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_transaction_payee_has_phoneNum():
    assert hasattr(transaction_Payee, "phoneNum")
    descriptor = None
    for klass in transaction_Payee.__mro__:
        if "phoneNum" in klass.__dict__:
            descriptor = klass.__dict__["phoneNum"]
            break
    assert isinstance(descriptor, property)

def test_transaction_payee_has_address1():
    assert hasattr(transaction_Payee, "address1")
    descriptor = None
    for klass in transaction_Payee.__mro__:
        if "address1" in klass.__dict__:
            descriptor = klass.__dict__["address1"]
            break
    assert isinstance(descriptor, property)

def test_transaction_payee_has_accountNum():
    assert hasattr(transaction_Payee, "accountNum")
    descriptor = None
    for klass in transaction_Payee.__mro__:
        if "accountNum" in klass.__dict__:
            descriptor = klass.__dict__["accountNum"]
            break
    assert isinstance(descriptor, property)



def test_transaction_externalaccount_is_not_abstract():
    assert not inspect.isabstract(transaction_ExternalAccount)


def test_transaction_externalaccount_constructor_exists():
    assert callable(transaction_ExternalAccount.__init__)


def test_transaction_externalaccount_constructor_args():
    sig = inspect.signature(transaction_ExternalAccount.__init__)
    params = list(sig.parameters.keys())
    assert "routingNum" in params, "Missing parameter 'routingNum'"
    assert "accountNum" in params, "Missing parameter 'accountNum'"
    assert "associatedAccount" in params, "Missing parameter 'associatedAccount'"

def test_transaction_externalaccount_has_routingNum():
    assert hasattr(transaction_ExternalAccount, "routingNum")
    descriptor = None
    for klass in transaction_ExternalAccount.__mro__:
        if "routingNum" in klass.__dict__:
            descriptor = klass.__dict__["routingNum"]
            break
    assert isinstance(descriptor, property)

def test_transaction_externalaccount_has_accountNum():
    assert hasattr(transaction_ExternalAccount, "accountNum")
    descriptor = None
    for klass in transaction_ExternalAccount.__mro__:
        if "accountNum" in klass.__dict__:
            descriptor = klass.__dict__["accountNum"]
            break
    assert isinstance(descriptor, property)

def test_transaction_externalaccount_has_associatedAccount():
    assert hasattr(transaction_ExternalAccount, "associatedAccount")
    descriptor = None
    for klass in transaction_ExternalAccount.__mro__:
        if "associatedAccount" in klass.__dict__:
            descriptor = klass.__dict__["associatedAccount"]
            break
    assert isinstance(descriptor, property)



def test_transaction_paybillstransaction_is_not_abstract():
    assert not inspect.isabstract(transaction_PaybillsTransaction)


def test_transaction_paybillstransaction_constructor_exists():
    assert callable(transaction_PaybillsTransaction.__init__)


def test_transaction_paybillstransaction_constructor_args():
    sig = inspect.signature(transaction_PaybillsTransaction.__init__)
    params = list(sig.parameters.keys())



def test_transaction_transfertransaction_is_not_abstract():
    assert not inspect.isabstract(transaction_TransferTransaction)


def test_transaction_transfertransaction_constructor_exists():
    assert callable(transaction_TransferTransaction.__init__)


def test_transaction_transfertransaction_constructor_args():
    sig = inspect.signature(transaction_TransferTransaction.__init__)
    params = list(sig.parameters.keys())



def test_transaction_deposittransaction_is_not_abstract():
    assert not inspect.isabstract(transaction_DepositTransaction)


def test_transaction_deposittransaction_constructor_exists():
    assert callable(transaction_DepositTransaction.__init__)


def test_transaction_deposittransaction_constructor_args():
    sig = inspect.signature(transaction_DepositTransaction.__init__)
    params = list(sig.parameters.keys())



def test_transaction_transaction_is_not_abstract():
    assert not inspect.isabstract(transaction_Transaction)


def test_transaction_transaction_constructor_exists():
    assert callable(transaction_Transaction.__init__)


def test_transaction_transaction_constructor_args():
    sig = inspect.signature(transaction_Transaction.__init__)
    params = list(sig.parameters.keys())
    assert "transactionID" in params, "Missing parameter 'transactionID'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "type" in params, "Missing parameter 'type'"
    assert "destinationAccountNum" in params, "Missing parameter 'destinationAccountNum'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "sourceAccountNum" in params, "Missing parameter 'sourceAccountNum'"
    assert "time" in params, "Missing parameter 'time'"
    assert "description" in params, "Missing parameter 'description'"

def test_transaction_transaction_has_transactionID():
    assert hasattr(transaction_Transaction, "transactionID")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "transactionID" in klass.__dict__:
            descriptor = klass.__dict__["transactionID"]
            break
    assert isinstance(descriptor, property)

def test_transaction_transaction_has_amount():
    assert hasattr(transaction_Transaction, "amount")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_transaction_transaction_has_type():
    assert hasattr(transaction_Transaction, "type")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_transaction_transaction_has_destinationAccountNum():
    assert hasattr(transaction_Transaction, "destinationAccountNum")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "destinationAccountNum" in klass.__dict__:
            descriptor = klass.__dict__["destinationAccountNum"]
            break
    assert isinstance(descriptor, property)

def test_transaction_transaction_has_comment():
    assert hasattr(transaction_Transaction, "comment")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_transaction_transaction_has_sourceAccountNum():
    assert hasattr(transaction_Transaction, "sourceAccountNum")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "sourceAccountNum" in klass.__dict__:
            descriptor = klass.__dict__["sourceAccountNum"]
            break
    assert isinstance(descriptor, property)

def test_transaction_transaction_has_time():
    assert hasattr(transaction_Transaction, "time")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_transaction_transaction_has_description():
    assert hasattr(transaction_Transaction, "description")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "lastLoginTime" in params, "Missing parameter 'lastLoginTime'"
    assert "password" in params, "Missing parameter 'password'"
    assert "userID" in params, "Missing parameter 'userID'"
    assert "username" in params, "Missing parameter 'username'"

def test_user_has_lastLoginTime():
    assert hasattr(User, "lastLoginTime")
    descriptor = None
    for klass in User.__mro__:
        if "lastLoginTime" in klass.__dict__:
            descriptor = klass.__dict__["lastLoginTime"]
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

def test_user_has_username():
    assert hasattr(User, "username")
    descriptor = None
    for klass in User.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)



def test_profile_is_not_abstract():
    assert not inspect.isabstract(Profile)


def test_profile_constructor_exists():
    assert callable(Profile.__init__)


def test_profile_constructor_args():
    sig = inspect.signature(Profile.__init__)
    params = list(sig.parameters.keys())
    assert "state" in params, "Missing parameter 'state'"
    assert "country" in params, "Missing parameter 'country'"
    assert "zipcode" in params, "Missing parameter 'zipcode'"
    assert "address1" in params, "Missing parameter 'address1'"
    assert "address2" in params, "Missing parameter 'address2'"
    assert "userID" in params, "Missing parameter 'userID'"
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "email" in params, "Missing parameter 'email'"
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "IDType" in params, "Missing parameter 'IDType'"
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"
    assert "IDNum" in params, "Missing parameter 'IDNum'"
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"
    assert "city" in params, "Missing parameter 'city'"

def test_profile_has_state():
    assert hasattr(Profile, "state")
    descriptor = None
    for klass in Profile.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_country():
    assert hasattr(Profile, "country")
    descriptor = None
    for klass in Profile.__mro__:
        if "country" in klass.__dict__:
            descriptor = klass.__dict__["country"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_zipcode():
    assert hasattr(Profile, "zipcode")
    descriptor = None
    for klass in Profile.__mro__:
        if "zipcode" in klass.__dict__:
            descriptor = klass.__dict__["zipcode"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_address1():
    assert hasattr(Profile, "address1")
    descriptor = None
    for klass in Profile.__mro__:
        if "address1" in klass.__dict__:
            descriptor = klass.__dict__["address1"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_address2():
    assert hasattr(Profile, "address2")
    descriptor = None
    for klass in Profile.__mro__:
        if "address2" in klass.__dict__:
            descriptor = klass.__dict__["address2"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_userID():
    assert hasattr(Profile, "userID")
    descriptor = None
    for klass in Profile.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_lastname():
    assert hasattr(Profile, "lastname")
    descriptor = None
    for klass in Profile.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_email():
    assert hasattr(Profile, "email")
    descriptor = None
    for klass in Profile.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_firstname():
    assert hasattr(Profile, "firstname")
    descriptor = None
    for klass in Profile.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_IDType():
    assert hasattr(Profile, "IDType")
    descriptor = None
    for klass in Profile.__mro__:
        if "IDType" in klass.__dict__:
            descriptor = klass.__dict__["IDType"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_phoneNumber():
    assert hasattr(Profile, "phoneNumber")
    descriptor = None
    for klass in Profile.__mro__:
        if "phoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["phoneNumber"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_IDNum():
    assert hasattr(Profile, "IDNum")
    descriptor = None
    for klass in Profile.__mro__:
        if "IDNum" in klass.__dict__:
            descriptor = klass.__dict__["IDNum"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_dateOfBirth():
    assert hasattr(Profile, "dateOfBirth")
    descriptor = None
    for klass in Profile.__mro__:
        if "dateOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["dateOfBirth"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_city():
    assert hasattr(Profile, "city")
    descriptor = None
    for klass in Profile.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_transaction_transactiontype_exists():
    # Check that the Enumeration exists
    assert transaction_TransactionType is not None

def test_transaction_transactiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in transaction_TransactionType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in transaction_TransactionType"

def test_account_accounttype_exists():
    # Check that the Enumeration exists
    assert account_AccountType is not None

def test_account_accounttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in account_AccountType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in account_AccountType"

def test_loan_loanstatus_exists():
    # Check that the Enumeration exists
    assert loan_LoanStatus is not None

def test_loan_loanstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in loan_LoanStatus]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in loan_LoanStatus"

def test_loan_applicationstatus_exists():
    # Check that the Enumeration exists
    assert loan_ApplicationStatus is not None

def test_loan_applicationstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in loan_ApplicationStatus]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in loan_ApplicationStatus"

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

def test_loan_loantype_exists():
    # Check that the Enumeration exists
    assert loan_LoanType is not None

def test_loan_loantype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in loan_LoanType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in loan_LoanType"


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
ExternalAccount_strategy = st.builds(
    ExternalAccount,
    routingNum=
        safe_text,
    associatedAccount=
        safe_text,
    accountNum=
        safe_text
)
TransferTransaction_strategy = st.builds(
    TransferTransaction,
)
Transaction3_strategy = st.builds(
    Transaction3,
    destinationAccountNum=
        safe_text,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    time=
        safe_text,
    transactionID=
        safe_text,
    type=
        st.none(),
    sourceAccountNum=
        safe_text,
    comment=
        safe_text,
    description=
        safe_text
)
Account2_strategy = st.builds(
    Account2,
    type=
        st.none(),
    pin=
        safe_text,
    userID=
        safe_text,
    accountNum=
        safe_text,
    balance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Transaction1_strategy = st.builds(
    Transaction1,
    destinationAccountNum=
        safe_text,
    type=
        st.none(),
    description=
        safe_text,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    transactionID=
        safe_text,
    time=
        safe_text,
    comment=
        safe_text,
    sourceAccountNum=
        safe_text
)
Account1_strategy = st.builds(
    Account1,
    balance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    type=
        st.none(),
    pin=
        safe_text,
    accountNum=
        safe_text,
    userID=
        safe_text
)
Transaction2_strategy = st.builds(
    Transaction2,
    sourceAccountNum=
        safe_text,
    type=
        st.none(),
    time=
        safe_text,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    description=
        safe_text,
    transactionID=
        safe_text,
    comment=
        safe_text,
    destinationAccountNum=
        safe_text
)
Transaction_strategy = st.builds(
    Transaction,
    description=
        safe_text,
    comment=
        safe_text,
    transactionID=
        safe_text,
    time=
        safe_text,
    sourceAccountNum=
        safe_text,
    destinationAccountNum=
        safe_text,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    type=
        st.none()
)
Account_strategy = st.builds(
    Account,
    balance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    pin=
        safe_text,
    type=
        st.none(),
    userID=
        safe_text,
    accountNum=
        safe_text
)
String_strategy = st.builds(
    String,
)
loan_LoanApplicationFile_strategy = st.builds(
    loan_LoanApplicationFile,
    fileID=
        safe_text,
    applicationID=
        safe_text
)
loan_Loan_strategy = st.builds(
    loan_Loan,
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    userID=
        safe_text,
    term=
        st.integers(),
    type=
        st.none(),
    submissionTime=
        safe_text,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    status=
        st.none(),
    loanID=
        safe_text
)
loan_LoanApplication_strategy = st.builds(
    loan_LoanApplication,
    submissionTime=
        safe_text,
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    status=
        st.none(),
    applicationID=
        safe_text,
    userID=
        safe_text,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    term=
        st.integers(),
    type=
        st.none()
)
account_Account_strategy = st.builds(
    account_Account,
    userID=
        safe_text,
    accountNum=
        safe_text,
    type=
        st.none(),
    pin=
        safe_text,
    balance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
account_SavingsAccount_strategy = st.builds(
    account_SavingsAccount,
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
transaction_LoanPayment_strategy = st.builds(
    transaction_LoanPayment,
    interest=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    principal=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    loanID=
        safe_text
)
transaction_Payee_strategy = st.builds(
    transaction_Payee,
    userID=
        safe_text,
    address2=
        safe_text,
    zipcode=
        safe_text,
    country=
        safe_text,
    city=
        safe_text,
    state=
        safe_text,
    email=
        safe_text,
    name=
        safe_text,
    phoneNum=
        safe_text,
    address1=
        safe_text,
    accountNum=
        safe_text
)
transaction_ExternalAccount_strategy = st.builds(
    transaction_ExternalAccount,
    routingNum=
        safe_text,
    accountNum=
        safe_text,
    associatedAccount=
        safe_text
)
transaction_PaybillsTransaction_strategy = st.builds(
    transaction_PaybillsTransaction,
)
transaction_TransferTransaction_strategy = st.builds(
    transaction_TransferTransaction,
)
transaction_DepositTransaction_strategy = st.builds(
    transaction_DepositTransaction,
)
transaction_Transaction_strategy = st.builds(
    transaction_Transaction,
    transactionID=
        safe_text,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    type=
        st.none(),
    destinationAccountNum=
        safe_text,
    comment=
        safe_text,
    sourceAccountNum=
        safe_text,
    time=
        safe_text,
    description=
        safe_text
)
User_strategy = st.builds(
    User,
    lastLoginTime=
        safe_text,
    password=
        safe_text,
    userID=
        safe_text,
    username=
        safe_text
)
Profile_strategy = st.builds(
    Profile,
    state=
        safe_text,
    country=
        safe_text,
    zipcode=
        safe_text,
    address1=
        safe_text,
    address2=
        safe_text,
    userID=
        safe_text,
    lastname=
        safe_text,
    email=
        safe_text,
    firstname=
        safe_text,
    IDType=
        st.integers(),
    phoneNumber=
        safe_text,
    IDNum=
        safe_text,
    dateOfBirth=
        st.dates(),
    city=
        safe_text
)

@given(instance=ExternalAccount_strategy)
@settings(max_examples=50)
def test_externalaccount_instantiation(instance):
    assert isinstance(instance, ExternalAccount)



@given(instance=ExternalAccount_strategy)
def test_externalaccount_routingNum_setter(instance):
    original = instance.routingNum
    instance.routingNum = original
    assert instance.routingNum == original



@given(instance=ExternalAccount_strategy)
def test_externalaccount_associatedAccount_setter(instance):
    original = instance.associatedAccount
    instance.associatedAccount = original
    assert instance.associatedAccount == original



@given(instance=ExternalAccount_strategy)
def test_externalaccount_accountNum_setter(instance):
    original = instance.accountNum
    instance.accountNum = original
    assert instance.accountNum == original

@given(instance=TransferTransaction_strategy)
@settings(max_examples=50)
def test_transfertransaction_instantiation(instance):
    assert isinstance(instance, TransferTransaction)

@given(instance=Transaction3_strategy)
@settings(max_examples=50)
def test_transaction3_instantiation(instance):
    assert isinstance(instance, Transaction3)



@given(instance=Transaction3_strategy)
def test_transaction3_destinationAccountNum_setter(instance):
    original = instance.destinationAccountNum
    instance.destinationAccountNum = original
    assert instance.destinationAccountNum == original



@given(instance=Transaction3_strategy)
def test_transaction3_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Transaction3_strategy)
def test_transaction3_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=Transaction3_strategy)
def test_transaction3_transactionID_setter(instance):
    original = instance.transactionID
    instance.transactionID = original
    assert instance.transactionID == original



@given(instance=Transaction3_strategy)
def test_transaction3_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Transaction3_strategy)
def test_transaction3_sourceAccountNum_setter(instance):
    original = instance.sourceAccountNum
    instance.sourceAccountNum = original
    assert instance.sourceAccountNum == original



@given(instance=Transaction3_strategy)
def test_transaction3_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=Transaction3_strategy)
def test_transaction3_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=Account2_strategy)
@settings(max_examples=50)
def test_account2_instantiation(instance):
    assert isinstance(instance, Account2)



@given(instance=Account2_strategy)
def test_account2_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Account2_strategy)
def test_account2_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original



@given(instance=Account2_strategy)
def test_account2_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=Account2_strategy)
def test_account2_accountNum_setter(instance):
    original = instance.accountNum
    instance.accountNum = original
    assert instance.accountNum == original



@given(instance=Account2_strategy)
def test_account2_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original

@given(instance=Transaction1_strategy)
@settings(max_examples=50)
def test_transaction1_instantiation(instance):
    assert isinstance(instance, Transaction1)



@given(instance=Transaction1_strategy)
def test_transaction1_destinationAccountNum_setter(instance):
    original = instance.destinationAccountNum
    instance.destinationAccountNum = original
    assert instance.destinationAccountNum == original



@given(instance=Transaction1_strategy)
def test_transaction1_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Transaction1_strategy)
def test_transaction1_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Transaction1_strategy)
def test_transaction1_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Transaction1_strategy)
def test_transaction1_transactionID_setter(instance):
    original = instance.transactionID
    instance.transactionID = original
    assert instance.transactionID == original



@given(instance=Transaction1_strategy)
def test_transaction1_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=Transaction1_strategy)
def test_transaction1_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=Transaction1_strategy)
def test_transaction1_sourceAccountNum_setter(instance):
    original = instance.sourceAccountNum
    instance.sourceAccountNum = original
    assert instance.sourceAccountNum == original

@given(instance=Account1_strategy)
@settings(max_examples=50)
def test_account1_instantiation(instance):
    assert isinstance(instance, Account1)



@given(instance=Account1_strategy)
def test_account1_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original



@given(instance=Account1_strategy)
def test_account1_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Account1_strategy)
def test_account1_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original



@given(instance=Account1_strategy)
def test_account1_accountNum_setter(instance):
    original = instance.accountNum
    instance.accountNum = original
    assert instance.accountNum == original



@given(instance=Account1_strategy)
def test_account1_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original

@given(instance=Transaction2_strategy)
@settings(max_examples=50)
def test_transaction2_instantiation(instance):
    assert isinstance(instance, Transaction2)



@given(instance=Transaction2_strategy)
def test_transaction2_sourceAccountNum_setter(instance):
    original = instance.sourceAccountNum
    instance.sourceAccountNum = original
    assert instance.sourceAccountNum == original



@given(instance=Transaction2_strategy)
def test_transaction2_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Transaction2_strategy)
def test_transaction2_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=Transaction2_strategy)
def test_transaction2_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Transaction2_strategy)
def test_transaction2_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Transaction2_strategy)
def test_transaction2_transactionID_setter(instance):
    original = instance.transactionID
    instance.transactionID = original
    assert instance.transactionID == original



@given(instance=Transaction2_strategy)
def test_transaction2_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=Transaction2_strategy)
def test_transaction2_destinationAccountNum_setter(instance):
    original = instance.destinationAccountNum
    instance.destinationAccountNum = original
    assert instance.destinationAccountNum == original

@given(instance=Transaction_strategy)
@settings(max_examples=50)
def test_transaction_instantiation(instance):
    assert isinstance(instance, Transaction)



@given(instance=Transaction_strategy)
def test_transaction_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Transaction_strategy)
def test_transaction_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=Transaction_strategy)
def test_transaction_transactionID_setter(instance):
    original = instance.transactionID
    instance.transactionID = original
    assert instance.transactionID == original



@given(instance=Transaction_strategy)
def test_transaction_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=Transaction_strategy)
def test_transaction_sourceAccountNum_setter(instance):
    original = instance.sourceAccountNum
    instance.sourceAccountNum = original
    assert instance.sourceAccountNum == original



@given(instance=Transaction_strategy)
def test_transaction_destinationAccountNum_setter(instance):
    original = instance.destinationAccountNum
    instance.destinationAccountNum = original
    assert instance.destinationAccountNum == original



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

@given(instance=Account_strategy)
@settings(max_examples=50)
def test_account_instantiation(instance):
    assert isinstance(instance, Account)



@given(instance=Account_strategy)
def test_account_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original



@given(instance=Account_strategy)
def test_account_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original



@given(instance=Account_strategy)
def test_account_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Account_strategy)
def test_account_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=Account_strategy)
def test_account_accountNum_setter(instance):
    original = instance.accountNum
    instance.accountNum = original
    assert instance.accountNum == original

@given(instance=String_strategy)
@settings(max_examples=50)
def test_string_instantiation(instance):
    assert isinstance(instance, String)

@given(instance=loan_LoanApplicationFile_strategy)
@settings(max_examples=50)
def test_loan_loanapplicationfile_instantiation(instance):
    assert isinstance(instance, loan_LoanApplicationFile)



@given(instance=loan_LoanApplicationFile_strategy)
def test_loan_loanapplicationfile_fileID_setter(instance):
    original = instance.fileID
    instance.fileID = original
    assert instance.fileID == original



@given(instance=loan_LoanApplicationFile_strategy)
def test_loan_loanapplicationfile_applicationID_setter(instance):
    original = instance.applicationID
    instance.applicationID = original
    assert instance.applicationID == original

@given(instance=loan_Loan_strategy)
@settings(max_examples=50)
def test_loan_loan_instantiation(instance):
    assert isinstance(instance, loan_Loan)



@given(instance=loan_Loan_strategy)
def test_loan_loan_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original



@given(instance=loan_Loan_strategy)
def test_loan_loan_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=loan_Loan_strategy)
def test_loan_loan_term_setter(instance):
    original = instance.term
    instance.term = original
    assert instance.term == original



@given(instance=loan_Loan_strategy)
def test_loan_loan_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=loan_Loan_strategy)
def test_loan_loan_submissionTime_setter(instance):
    original = instance.submissionTime
    instance.submissionTime = original
    assert instance.submissionTime == original



@given(instance=loan_Loan_strategy)
def test_loan_loan_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=loan_Loan_strategy)
def test_loan_loan_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=loan_Loan_strategy)
def test_loan_loan_loanID_setter(instance):
    original = instance.loanID
    instance.loanID = original
    assert instance.loanID == original

@given(instance=loan_LoanApplication_strategy)
@settings(max_examples=50)
def test_loan_loanapplication_instantiation(instance):
    assert isinstance(instance, loan_LoanApplication)



@given(instance=loan_LoanApplication_strategy)
def test_loan_loanapplication_submissionTime_setter(instance):
    original = instance.submissionTime
    instance.submissionTime = original
    assert instance.submissionTime == original



@given(instance=loan_LoanApplication_strategy)
def test_loan_loanapplication_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original



@given(instance=loan_LoanApplication_strategy)
def test_loan_loanapplication_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=loan_LoanApplication_strategy)
def test_loan_loanapplication_applicationID_setter(instance):
    original = instance.applicationID
    instance.applicationID = original
    assert instance.applicationID == original



@given(instance=loan_LoanApplication_strategy)
def test_loan_loanapplication_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=loan_LoanApplication_strategy)
def test_loan_loanapplication_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=loan_LoanApplication_strategy)
def test_loan_loanapplication_term_setter(instance):
    original = instance.term
    instance.term = original
    assert instance.term == original



@given(instance=loan_LoanApplication_strategy)
def test_loan_loanapplication_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=account_Account_strategy)
@settings(max_examples=50)
def test_account_account_instantiation(instance):
    assert isinstance(instance, account_Account)



@given(instance=account_Account_strategy)
def test_account_account_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=account_Account_strategy)
def test_account_account_accountNum_setter(instance):
    original = instance.accountNum
    instance.accountNum = original
    assert instance.accountNum == original



@given(instance=account_Account_strategy)
def test_account_account_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=account_Account_strategy)
def test_account_account_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original



@given(instance=account_Account_strategy)
def test_account_account_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original

@given(instance=account_SavingsAccount_strategy)
@settings(max_examples=50)
def test_account_savingsaccount_instantiation(instance):
    assert isinstance(instance, account_SavingsAccount)



@given(instance=account_SavingsAccount_strategy)
def test_account_savingsaccount_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original

@given(instance=transaction_LoanPayment_strategy)
@settings(max_examples=50)
def test_transaction_loanpayment_instantiation(instance):
    assert isinstance(instance, transaction_LoanPayment)



@given(instance=transaction_LoanPayment_strategy)
def test_transaction_loanpayment_interest_setter(instance):
    original = instance.interest
    instance.interest = original
    assert instance.interest == original



@given(instance=transaction_LoanPayment_strategy)
def test_transaction_loanpayment_principal_setter(instance):
    original = instance.principal
    instance.principal = original
    assert instance.principal == original



@given(instance=transaction_LoanPayment_strategy)
def test_transaction_loanpayment_loanID_setter(instance):
    original = instance.loanID
    instance.loanID = original
    assert instance.loanID == original

@given(instance=transaction_Payee_strategy)
@settings(max_examples=50)
def test_transaction_payee_instantiation(instance):
    assert isinstance(instance, transaction_Payee)



@given(instance=transaction_Payee_strategy)
def test_transaction_payee_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=transaction_Payee_strategy)
def test_transaction_payee_address2_setter(instance):
    original = instance.address2
    instance.address2 = original
    assert instance.address2 == original



@given(instance=transaction_Payee_strategy)
def test_transaction_payee_zipcode_setter(instance):
    original = instance.zipcode
    instance.zipcode = original
    assert instance.zipcode == original



@given(instance=transaction_Payee_strategy)
def test_transaction_payee_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original



@given(instance=transaction_Payee_strategy)
def test_transaction_payee_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=transaction_Payee_strategy)
def test_transaction_payee_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original



@given(instance=transaction_Payee_strategy)
def test_transaction_payee_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=transaction_Payee_strategy)
def test_transaction_payee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=transaction_Payee_strategy)
def test_transaction_payee_phoneNum_setter(instance):
    original = instance.phoneNum
    instance.phoneNum = original
    assert instance.phoneNum == original



@given(instance=transaction_Payee_strategy)
def test_transaction_payee_address1_setter(instance):
    original = instance.address1
    instance.address1 = original
    assert instance.address1 == original



@given(instance=transaction_Payee_strategy)
def test_transaction_payee_accountNum_setter(instance):
    original = instance.accountNum
    instance.accountNum = original
    assert instance.accountNum == original

@given(instance=transaction_ExternalAccount_strategy)
@settings(max_examples=50)
def test_transaction_externalaccount_instantiation(instance):
    assert isinstance(instance, transaction_ExternalAccount)



@given(instance=transaction_ExternalAccount_strategy)
def test_transaction_externalaccount_routingNum_setter(instance):
    original = instance.routingNum
    instance.routingNum = original
    assert instance.routingNum == original



@given(instance=transaction_ExternalAccount_strategy)
def test_transaction_externalaccount_accountNum_setter(instance):
    original = instance.accountNum
    instance.accountNum = original
    assert instance.accountNum == original



@given(instance=transaction_ExternalAccount_strategy)
def test_transaction_externalaccount_associatedAccount_setter(instance):
    original = instance.associatedAccount
    instance.associatedAccount = original
    assert instance.associatedAccount == original

@given(instance=transaction_PaybillsTransaction_strategy)
@settings(max_examples=50)
def test_transaction_paybillstransaction_instantiation(instance):
    assert isinstance(instance, transaction_PaybillsTransaction)

@given(instance=transaction_TransferTransaction_strategy)
@settings(max_examples=50)
def test_transaction_transfertransaction_instantiation(instance):
    assert isinstance(instance, transaction_TransferTransaction)

@given(instance=transaction_DepositTransaction_strategy)
@settings(max_examples=50)
def test_transaction_deposittransaction_instantiation(instance):
    assert isinstance(instance, transaction_DepositTransaction)

@given(instance=transaction_Transaction_strategy)
@settings(max_examples=50)
def test_transaction_transaction_instantiation(instance):
    assert isinstance(instance, transaction_Transaction)



@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_transactionID_setter(instance):
    original = instance.transactionID
    instance.transactionID = original
    assert instance.transactionID == original



@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_destinationAccountNum_setter(instance):
    original = instance.destinationAccountNum
    instance.destinationAccountNum = original
    assert instance.destinationAccountNum == original



@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_sourceAccountNum_setter(instance):
    original = instance.sourceAccountNum
    instance.sourceAccountNum = original
    assert instance.sourceAccountNum == original



@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_lastLoginTime_setter(instance):
    original = instance.lastLoginTime
    instance.lastLoginTime = original
    assert instance.lastLoginTime == original



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



@given(instance=User_strategy)
def test_user_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original

@given(instance=Profile_strategy)
@settings(max_examples=50)
def test_profile_instantiation(instance):
    assert isinstance(instance, Profile)



@given(instance=Profile_strategy)
def test_profile_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original



@given(instance=Profile_strategy)
def test_profile_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original



@given(instance=Profile_strategy)
def test_profile_zipcode_setter(instance):
    original = instance.zipcode
    instance.zipcode = original
    assert instance.zipcode == original



@given(instance=Profile_strategy)
def test_profile_address1_setter(instance):
    original = instance.address1
    instance.address1 = original
    assert instance.address1 == original



@given(instance=Profile_strategy)
def test_profile_address2_setter(instance):
    original = instance.address2
    instance.address2 = original
    assert instance.address2 == original



@given(instance=Profile_strategy)
def test_profile_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=Profile_strategy)
def test_profile_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=Profile_strategy)
def test_profile_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Profile_strategy)
def test_profile_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original



@given(instance=Profile_strategy)
def test_profile_IDType_setter(instance):
    original = instance.IDType
    instance.IDType = original
    assert instance.IDType == original



@given(instance=Profile_strategy)
def test_profile_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original



@given(instance=Profile_strategy)
def test_profile_IDNum_setter(instance):
    original = instance.IDNum
    instance.IDNum = original
    assert instance.IDNum == original



@given(instance=Profile_strategy)
def test_profile_dateOfBirth_setter(instance):
    original = instance.dateOfBirth
    instance.dateOfBirth = original
    assert instance.dateOfBirth == original



@given(instance=Profile_strategy)
def test_profile_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original
