import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from python_code import (
    Sistem_Peminjaman_Dana_Pegawai,
    Transaksi_Peminjaman,
    Data_Peminjaman,
    Data_Pegawai,
    account_Account,
    account_CheckingAccount,
    account_CertificatesOfDepositAccount,
    account_SavingsAccount,
    transaction_TransferTransaction,
    transaction_WithdrawTransaction,
    transaction_DepositTransaction,
    transaction_Transaction,
    Login,
    Customer,
    account_AccountType,
    transaction_TransactionType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sistem_peminjaman_dana_pegawai_is_not_abstract():
    assert not inspect.isabstract(Sistem_Peminjaman_Dana_Pegawai)


def test_sistem_peminjaman_dana_pegawai_constructor_exists():
    assert callable(Sistem_Peminjaman_Dana_Pegawai.__init__)


def test_sistem_peminjaman_dana_pegawai_constructor_args():
    sig = inspect.signature(Sistem_Peminjaman_Dana_Pegawai.__init__)
    params = list(sig.parameters.keys())



def test_transaksi_peminjaman_is_not_abstract():
    assert not inspect.isabstract(Transaksi_Peminjaman)


def test_transaksi_peminjaman_constructor_exists():
    assert callable(Transaksi_Peminjaman.__init__)


def test_transaksi_peminjaman_constructor_args():
    sig = inspect.signature(Transaksi_Peminjaman.__init__)
    params = list(sig.parameters.keys())
    assert "NIK" in params, "Missing parameter 'NIK'"
    assert "Namakaryawan" in params, "Missing parameter 'Namakaryawan'"
    assert "keterangan" in params, "Missing parameter 'keterangan'"
    assert "Tanggalpinjam" in params, "Missing parameter 'Tanggalpinjam'"
    assert "Nopeminjaman" in params, "Missing parameter 'Nopeminjaman'"
    assert "jumlahpinjam" in params, "Missing parameter 'jumlahpinjam'"
    assert "NPK" in params, "Missing parameter 'NPK'"

def test_transaksi_peminjaman_has_NIK():
    assert hasattr(Transaksi_Peminjaman, "NIK")
    descriptor = None
    for klass in Transaksi_Peminjaman.__mro__:
        if "NIK" in klass.__dict__:
            descriptor = klass.__dict__["NIK"]
            break
    assert isinstance(descriptor, property)

def test_transaksi_peminjaman_has_Namakaryawan():
    assert hasattr(Transaksi_Peminjaman, "Namakaryawan")
    descriptor = None
    for klass in Transaksi_Peminjaman.__mro__:
        if "Namakaryawan" in klass.__dict__:
            descriptor = klass.__dict__["Namakaryawan"]
            break
    assert isinstance(descriptor, property)

def test_transaksi_peminjaman_has_keterangan():
    assert hasattr(Transaksi_Peminjaman, "keterangan")
    descriptor = None
    for klass in Transaksi_Peminjaman.__mro__:
        if "keterangan" in klass.__dict__:
            descriptor = klass.__dict__["keterangan"]
            break
    assert isinstance(descriptor, property)

def test_transaksi_peminjaman_has_Tanggalpinjam():
    assert hasattr(Transaksi_Peminjaman, "Tanggalpinjam")
    descriptor = None
    for klass in Transaksi_Peminjaman.__mro__:
        if "Tanggalpinjam" in klass.__dict__:
            descriptor = klass.__dict__["Tanggalpinjam"]
            break
    assert isinstance(descriptor, property)

def test_transaksi_peminjaman_has_Nopeminjaman():
    assert hasattr(Transaksi_Peminjaman, "Nopeminjaman")
    descriptor = None
    for klass in Transaksi_Peminjaman.__mro__:
        if "Nopeminjaman" in klass.__dict__:
            descriptor = klass.__dict__["Nopeminjaman"]
            break
    assert isinstance(descriptor, property)

def test_transaksi_peminjaman_has_jumlahpinjam():
    assert hasattr(Transaksi_Peminjaman, "jumlahpinjam")
    descriptor = None
    for klass in Transaksi_Peminjaman.__mro__:
        if "jumlahpinjam" in klass.__dict__:
            descriptor = klass.__dict__["jumlahpinjam"]
            break
    assert isinstance(descriptor, property)

def test_transaksi_peminjaman_has_NPK():
    assert hasattr(Transaksi_Peminjaman, "NPK")
    descriptor = None
    for klass in Transaksi_Peminjaman.__mro__:
        if "NPK" in klass.__dict__:
            descriptor = klass.__dict__["NPK"]
            break
    assert isinstance(descriptor, property)



def test_data_peminjaman_is_not_abstract():
    assert not inspect.isabstract(Data_Peminjaman)


def test_data_peminjaman_constructor_exists():
    assert callable(Data_Peminjaman.__init__)


def test_data_peminjaman_constructor_args():
    sig = inspect.signature(Data_Peminjaman.__init__)
    params = list(sig.parameters.keys())
    assert "Namakaryawan" in params, "Missing parameter 'Namakaryawan'"
    assert "keterangan" in params, "Missing parameter 'keterangan'"
    assert "NPK" in params, "Missing parameter 'NPK'"
    assert "Tanggalpinjam" in params, "Missing parameter 'Tanggalpinjam'"
    assert "jumlahpinjam" in params, "Missing parameter 'jumlahpinjam'"
    assert "NIK" in params, "Missing parameter 'NIK'"

def test_data_peminjaman_has_Namakaryawan():
    assert hasattr(Data_Peminjaman, "Namakaryawan")
    descriptor = None
    for klass in Data_Peminjaman.__mro__:
        if "Namakaryawan" in klass.__dict__:
            descriptor = klass.__dict__["Namakaryawan"]
            break
    assert isinstance(descriptor, property)

def test_data_peminjaman_has_keterangan():
    assert hasattr(Data_Peminjaman, "keterangan")
    descriptor = None
    for klass in Data_Peminjaman.__mro__:
        if "keterangan" in klass.__dict__:
            descriptor = klass.__dict__["keterangan"]
            break
    assert isinstance(descriptor, property)

def test_data_peminjaman_has_NPK():
    assert hasattr(Data_Peminjaman, "NPK")
    descriptor = None
    for klass in Data_Peminjaman.__mro__:
        if "NPK" in klass.__dict__:
            descriptor = klass.__dict__["NPK"]
            break
    assert isinstance(descriptor, property)

def test_data_peminjaman_has_Tanggalpinjam():
    assert hasattr(Data_Peminjaman, "Tanggalpinjam")
    descriptor = None
    for klass in Data_Peminjaman.__mro__:
        if "Tanggalpinjam" in klass.__dict__:
            descriptor = klass.__dict__["Tanggalpinjam"]
            break
    assert isinstance(descriptor, property)

def test_data_peminjaman_has_jumlahpinjam():
    assert hasattr(Data_Peminjaman, "jumlahpinjam")
    descriptor = None
    for klass in Data_Peminjaman.__mro__:
        if "jumlahpinjam" in klass.__dict__:
            descriptor = klass.__dict__["jumlahpinjam"]
            break
    assert isinstance(descriptor, property)

def test_data_peminjaman_has_NIK():
    assert hasattr(Data_Peminjaman, "NIK")
    descriptor = None
    for klass in Data_Peminjaman.__mro__:
        if "NIK" in klass.__dict__:
            descriptor = klass.__dict__["NIK"]
            break
    assert isinstance(descriptor, property)



def test_data_pegawai_is_not_abstract():
    assert not inspect.isabstract(Data_Pegawai)


def test_data_pegawai_constructor_exists():
    assert callable(Data_Pegawai.__init__)


def test_data_pegawai_constructor_args():
    sig = inspect.signature(Data_Pegawai.__init__)
    params = list(sig.parameters.keys())
    assert "NIK" in params, "Missing parameter 'NIK'"
    assert "tempatlahir" in params, "Missing parameter 'tempatlahir'"
    assert "Namakaryawan" in params, "Missing parameter 'Namakaryawan'"
    assert "alamat" in params, "Missing parameter 'alamat'"
    assert "tanggallahir" in params, "Missing parameter 'tanggallahir'"
    assert "status" in params, "Missing parameter 'status'"

def test_data_pegawai_has_NIK():
    assert hasattr(Data_Pegawai, "NIK")
    descriptor = None
    for klass in Data_Pegawai.__mro__:
        if "NIK" in klass.__dict__:
            descriptor = klass.__dict__["NIK"]
            break
    assert isinstance(descriptor, property)

def test_data_pegawai_has_tempatlahir():
    assert hasattr(Data_Pegawai, "tempatlahir")
    descriptor = None
    for klass in Data_Pegawai.__mro__:
        if "tempatlahir" in klass.__dict__:
            descriptor = klass.__dict__["tempatlahir"]
            break
    assert isinstance(descriptor, property)

def test_data_pegawai_has_Namakaryawan():
    assert hasattr(Data_Pegawai, "Namakaryawan")
    descriptor = None
    for klass in Data_Pegawai.__mro__:
        if "Namakaryawan" in klass.__dict__:
            descriptor = klass.__dict__["Namakaryawan"]
            break
    assert isinstance(descriptor, property)

def test_data_pegawai_has_alamat():
    assert hasattr(Data_Pegawai, "alamat")
    descriptor = None
    for klass in Data_Pegawai.__mro__:
        if "alamat" in klass.__dict__:
            descriptor = klass.__dict__["alamat"]
            break
    assert isinstance(descriptor, property)

def test_data_pegawai_has_tanggallahir():
    assert hasattr(Data_Pegawai, "tanggallahir")
    descriptor = None
    for klass in Data_Pegawai.__mro__:
        if "tanggallahir" in klass.__dict__:
            descriptor = klass.__dict__["tanggallahir"]
            break
    assert isinstance(descriptor, property)

def test_data_pegawai_has_status():
    assert hasattr(Data_Pegawai, "status")
    descriptor = None
    for klass in Data_Pegawai.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_account_account_is_not_abstract():
    assert not inspect.isabstract(account_Account)


def test_account_account_constructor_exists():
    assert callable(account_Account.__init__)


def test_account_account_constructor_args():
    sig = inspect.signature(account_Account.__init__)
    params = list(sig.parameters.keys())
    assert "accountNo" in params, "Missing parameter 'accountNo'"
    assert "type" in params, "Missing parameter 'type'"
    assert "balance" in params, "Missing parameter 'balance'"

def test_account_account_has_accountNo():
    assert hasattr(account_Account, "accountNo")
    descriptor = None
    for klass in account_Account.__mro__:
        if "accountNo" in klass.__dict__:
            descriptor = klass.__dict__["accountNo"]
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

def test_account_account_has_balance():
    assert hasattr(account_Account, "balance")
    descriptor = None
    for klass in account_Account.__mro__:
        if "balance" in klass.__dict__:
            descriptor = klass.__dict__["balance"]
            break
    assert isinstance(descriptor, property)



def test_account_checkingaccount_is_not_abstract():
    assert not inspect.isabstract(account_CheckingAccount)


def test_account_checkingaccount_constructor_exists():
    assert callable(account_CheckingAccount.__init__)


def test_account_checkingaccount_constructor_args():
    sig = inspect.signature(account_CheckingAccount.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_account_checkingaccount_has_name():
    assert hasattr(account_CheckingAccount, "name")
    descriptor = None
    for klass in account_CheckingAccount.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_account_certificatesofdepositaccount_is_not_abstract():
    assert not inspect.isabstract(account_CertificatesOfDepositAccount)


def test_account_certificatesofdepositaccount_constructor_exists():
    assert callable(account_CertificatesOfDepositAccount.__init__)


def test_account_certificatesofdepositaccount_constructor_args():
    sig = inspect.signature(account_CertificatesOfDepositAccount.__init__)
    params = list(sig.parameters.keys())
    assert "interestRate" in params, "Missing parameter 'interestRate'"
    assert "timePeriod" in params, "Missing parameter 'timePeriod'"

def test_account_certificatesofdepositaccount_has_interestRate():
    assert hasattr(account_CertificatesOfDepositAccount, "interestRate")
    descriptor = None
    for klass in account_CertificatesOfDepositAccount.__mro__:
        if "interestRate" in klass.__dict__:
            descriptor = klass.__dict__["interestRate"]
            break
    assert isinstance(descriptor, property)

def test_account_certificatesofdepositaccount_has_timePeriod():
    assert hasattr(account_CertificatesOfDepositAccount, "timePeriod")
    descriptor = None
    for klass in account_CertificatesOfDepositAccount.__mro__:
        if "timePeriod" in klass.__dict__:
            descriptor = klass.__dict__["timePeriod"]
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



def test_transaction_transfertransaction_is_not_abstract():
    assert not inspect.isabstract(transaction_TransferTransaction)


def test_transaction_transfertransaction_constructor_exists():
    assert callable(transaction_TransferTransaction.__init__)


def test_transaction_transfertransaction_constructor_args():
    sig = inspect.signature(transaction_TransferTransaction.__init__)
    params = list(sig.parameters.keys())
    assert "sourceAccount" in params, "Missing parameter 'sourceAccount'"
    assert "targetAccount" in params, "Missing parameter 'targetAccount'"

def test_transaction_transfertransaction_has_sourceAccount():
    assert hasattr(transaction_TransferTransaction, "sourceAccount")
    descriptor = None
    for klass in transaction_TransferTransaction.__mro__:
        if "sourceAccount" in klass.__dict__:
            descriptor = klass.__dict__["sourceAccount"]
            break
    assert isinstance(descriptor, property)

def test_transaction_transfertransaction_has_targetAccount():
    assert hasattr(transaction_TransferTransaction, "targetAccount")
    descriptor = None
    for klass in transaction_TransferTransaction.__mro__:
        if "targetAccount" in klass.__dict__:
            descriptor = klass.__dict__["targetAccount"]
            break
    assert isinstance(descriptor, property)



def test_transaction_withdrawtransaction_is_not_abstract():
    assert not inspect.isabstract(transaction_WithdrawTransaction)


def test_transaction_withdrawtransaction_constructor_exists():
    assert callable(transaction_WithdrawTransaction.__init__)


def test_transaction_withdrawtransaction_constructor_args():
    sig = inspect.signature(transaction_WithdrawTransaction.__init__)
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
    assert "amount" in params, "Missing parameter 'amount'"
    assert "id" in params, "Missing parameter 'id'"
    assert "type" in params, "Missing parameter 'type'"
    assert "transactionTime" in params, "Missing parameter 'transactionTime'"

def test_transaction_transaction_has_amount():
    assert hasattr(transaction_Transaction, "amount")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_transaction_transaction_has_id():
    assert hasattr(transaction_Transaction, "id")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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

def test_transaction_transaction_has_transactionTime():
    assert hasattr(transaction_Transaction, "transactionTime")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "transactionTime" in klass.__dict__:
            descriptor = klass.__dict__["transactionTime"]
            break
    assert isinstance(descriptor, property)



def test_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_login_constructor_exists():
    assert callable(Login.__init__)


def test_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "securityAnswer" in params, "Missing parameter 'securityAnswer'"
    assert "password" in params, "Missing parameter 'password'"
    assert "securityQuestion" in params, "Missing parameter 'securityQuestion'"
    assert "username" in params, "Missing parameter 'username'"
    assert "lastLoginTime" in params, "Missing parameter 'lastLoginTime'"

def test_login_has_securityAnswer():
    assert hasattr(Login, "securityAnswer")
    descriptor = None
    for klass in Login.__mro__:
        if "securityAnswer" in klass.__dict__:
            descriptor = klass.__dict__["securityAnswer"]
            break
    assert isinstance(descriptor, property)

def test_login_has_password():
    assert hasattr(Login, "password")
    descriptor = None
    for klass in Login.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_login_has_securityQuestion():
    assert hasattr(Login, "securityQuestion")
    descriptor = None
    for klass in Login.__mro__:
        if "securityQuestion" in klass.__dict__:
            descriptor = klass.__dict__["securityQuestion"]
            break
    assert isinstance(descriptor, property)

def test_login_has_username():
    assert hasattr(Login, "username")
    descriptor = None
    for klass in Login.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_login_has_lastLoginTime():
    assert hasattr(Login, "lastLoginTime")
    descriptor = None
    for klass in Login.__mro__:
        if "lastLoginTime" in klass.__dict__:
            descriptor = klass.__dict__["lastLoginTime"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "emailAddress" in params, "Missing parameter 'emailAddress'"
    assert "address" in params, "Missing parameter 'address'"
    assert "name" in params, "Missing parameter 'name'"
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"

def test_customer_has_emailAddress():
    assert hasattr(Customer, "emailAddress")
    descriptor = None
    for klass in Customer.__mro__:
        if "emailAddress" in klass.__dict__:
            descriptor = klass.__dict__["emailAddress"]
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

def test_customer_has_name():
    assert hasattr(Customer, "name")
    descriptor = None
    for klass in Customer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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

def test_customer_has_dateOfBirth():
    assert hasattr(Customer, "dateOfBirth")
    descriptor = None
    for klass in Customer.__mro__:
        if "dateOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["dateOfBirth"]
            break
    assert isinstance(descriptor, property)

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
Sistem_Peminjaman_Dana_Pegawai_strategy = st.builds(
    Sistem_Peminjaman_Dana_Pegawai,
)
Transaksi_Peminjaman_strategy = st.builds(
    Transaksi_Peminjaman,
    NIK=
        st.integers(),
    Namakaryawan=
        safe_text,
    keterangan=
        safe_text,
    Tanggalpinjam=
        st.dates(),
    Nopeminjaman=
        st.integers(),
    jumlahpinjam=
        safe_text,
    NPK=
        st.integers()
)
Data_Peminjaman_strategy = st.builds(
    Data_Peminjaman,
    Namakaryawan=
        safe_text,
    keterangan=
        safe_text,
    NPK=
        st.integers(),
    Tanggalpinjam=
        st.dates(),
    jumlahpinjam=
        safe_text,
    NIK=
        st.integers()
)
Data_Pegawai_strategy = st.builds(
    Data_Pegawai,
    NIK=
        st.integers(),
    tempatlahir=
        safe_text,
    Namakaryawan=
        safe_text,
    alamat=
        safe_text,
    tanggallahir=
        st.dates(),
    status=
        safe_text
)
account_Account_strategy = st.builds(
    account_Account,
    accountNo=
        safe_text,
    type=
        st.none(),
    balance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
account_CheckingAccount_strategy = st.builds(
    account_CheckingAccount,
    name=
        safe_text
)
account_CertificatesOfDepositAccount_strategy = st.builds(
    account_CertificatesOfDepositAccount,
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    timePeriod=
        st.integers()
)
account_SavingsAccount_strategy = st.builds(
    account_SavingsAccount,
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
transaction_TransferTransaction_strategy = st.builds(
    transaction_TransferTransaction,
    sourceAccount=
        st.none(),
    targetAccount=
        st.none()
)
transaction_WithdrawTransaction_strategy = st.builds(
    transaction_WithdrawTransaction,
)
transaction_DepositTransaction_strategy = st.builds(
    transaction_DepositTransaction,
)
transaction_Transaction_strategy = st.builds(
    transaction_Transaction,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    id=
        st.integers(),
    type=
        st.none(),
    transactionTime=
        st.dates()
)
Login_strategy = st.builds(
    Login,
    securityAnswer=
        safe_text,
    password=
        safe_text,
    securityQuestion=
        safe_text,
    username=
        safe_text,
    lastLoginTime=
        st.dates()
)
Customer_strategy = st.builds(
    Customer,
    emailAddress=
        safe_text,
    address=
        safe_text,
    name=
        safe_text,
    phoneNumber=
        safe_text,
    dateOfBirth=
        st.dates()
)

@given(instance=Sistem_Peminjaman_Dana_Pegawai_strategy)
@settings(max_examples=50)
def test_sistem_peminjaman_dana_pegawai_instantiation(instance):
    assert isinstance(instance, Sistem_Peminjaman_Dana_Pegawai)

@given(instance=Transaksi_Peminjaman_strategy)
@settings(max_examples=50)
def test_transaksi_peminjaman_instantiation(instance):
    assert isinstance(instance, Transaksi_Peminjaman)

@given(instance=Transaksi_Peminjaman_strategy)
def test_transaksi_peminjaman_NIK_type(instance):
    assert isinstance(instance.NIK, int)


@given(instance=Transaksi_Peminjaman_strategy)
def test_transaksi_peminjaman_NIK_setter(instance):
    original = instance.NIK
    instance.NIK = original
    assert instance.NIK == original

@given(instance=Transaksi_Peminjaman_strategy)
def test_transaksi_peminjaman_Namakaryawan_type(instance):
    assert isinstance(instance.Namakaryawan, str)


@given(instance=Transaksi_Peminjaman_strategy)
def test_transaksi_peminjaman_Namakaryawan_setter(instance):
    original = instance.Namakaryawan
    instance.Namakaryawan = original
    assert instance.Namakaryawan == original

@given(instance=Transaksi_Peminjaman_strategy)
def test_transaksi_peminjaman_keterangan_type(instance):
    assert isinstance(instance.keterangan, str)


@given(instance=Transaksi_Peminjaman_strategy)
def test_transaksi_peminjaman_keterangan_setter(instance):
    original = instance.keterangan
    instance.keterangan = original
    assert instance.keterangan == original

@given(instance=Transaksi_Peminjaman_strategy)
def test_transaksi_peminjaman_Tanggalpinjam_type(instance):
    assert isinstance(instance.Tanggalpinjam, date)


@given(instance=Transaksi_Peminjaman_strategy)
def test_transaksi_peminjaman_Tanggalpinjam_setter(instance):
    original = instance.Tanggalpinjam
    instance.Tanggalpinjam = original
    assert instance.Tanggalpinjam == original

@given(instance=Transaksi_Peminjaman_strategy)
def test_transaksi_peminjaman_Nopeminjaman_type(instance):
    assert isinstance(instance.Nopeminjaman, int)


@given(instance=Transaksi_Peminjaman_strategy)
def test_transaksi_peminjaman_Nopeminjaman_setter(instance):
    original = instance.Nopeminjaman
    instance.Nopeminjaman = original
    assert instance.Nopeminjaman == original

@given(instance=Transaksi_Peminjaman_strategy)
def test_transaksi_peminjaman_jumlahpinjam_type(instance):
    assert isinstance(instance.jumlahpinjam, str)


@given(instance=Transaksi_Peminjaman_strategy)
def test_transaksi_peminjaman_jumlahpinjam_setter(instance):
    original = instance.jumlahpinjam
    instance.jumlahpinjam = original
    assert instance.jumlahpinjam == original

@given(instance=Transaksi_Peminjaman_strategy)
def test_transaksi_peminjaman_NPK_type(instance):
    assert isinstance(instance.NPK, int)


@given(instance=Transaksi_Peminjaman_strategy)
def test_transaksi_peminjaman_NPK_setter(instance):
    original = instance.NPK
    instance.NPK = original
    assert instance.NPK == original

@given(instance=Data_Peminjaman_strategy)
@settings(max_examples=50)
def test_data_peminjaman_instantiation(instance):
    assert isinstance(instance, Data_Peminjaman)

@given(instance=Data_Peminjaman_strategy)
def test_data_peminjaman_Namakaryawan_type(instance):
    assert isinstance(instance.Namakaryawan, str)


@given(instance=Data_Peminjaman_strategy)
def test_data_peminjaman_Namakaryawan_setter(instance):
    original = instance.Namakaryawan
    instance.Namakaryawan = original
    assert instance.Namakaryawan == original

@given(instance=Data_Peminjaman_strategy)
def test_data_peminjaman_keterangan_type(instance):
    assert isinstance(instance.keterangan, str)


@given(instance=Data_Peminjaman_strategy)
def test_data_peminjaman_keterangan_setter(instance):
    original = instance.keterangan
    instance.keterangan = original
    assert instance.keterangan == original

@given(instance=Data_Peminjaman_strategy)
def test_data_peminjaman_NPK_type(instance):
    assert isinstance(instance.NPK, int)


@given(instance=Data_Peminjaman_strategy)
def test_data_peminjaman_NPK_setter(instance):
    original = instance.NPK
    instance.NPK = original
    assert instance.NPK == original

@given(instance=Data_Peminjaman_strategy)
def test_data_peminjaman_Tanggalpinjam_type(instance):
    assert isinstance(instance.Tanggalpinjam, date)


@given(instance=Data_Peminjaman_strategy)
def test_data_peminjaman_Tanggalpinjam_setter(instance):
    original = instance.Tanggalpinjam
    instance.Tanggalpinjam = original
    assert instance.Tanggalpinjam == original

@given(instance=Data_Peminjaman_strategy)
def test_data_peminjaman_jumlahpinjam_type(instance):
    assert isinstance(instance.jumlahpinjam, str)


@given(instance=Data_Peminjaman_strategy)
def test_data_peminjaman_jumlahpinjam_setter(instance):
    original = instance.jumlahpinjam
    instance.jumlahpinjam = original
    assert instance.jumlahpinjam == original

@given(instance=Data_Peminjaman_strategy)
def test_data_peminjaman_NIK_type(instance):
    assert isinstance(instance.NIK, int)


@given(instance=Data_Peminjaman_strategy)
def test_data_peminjaman_NIK_setter(instance):
    original = instance.NIK
    instance.NIK = original
    assert instance.NIK == original

@given(instance=Data_Pegawai_strategy)
@settings(max_examples=50)
def test_data_pegawai_instantiation(instance):
    assert isinstance(instance, Data_Pegawai)

@given(instance=Data_Pegawai_strategy)
def test_data_pegawai_NIK_type(instance):
    assert isinstance(instance.NIK, int)


@given(instance=Data_Pegawai_strategy)
def test_data_pegawai_NIK_setter(instance):
    original = instance.NIK
    instance.NIK = original
    assert instance.NIK == original

@given(instance=Data_Pegawai_strategy)
def test_data_pegawai_tempatlahir_type(instance):
    assert isinstance(instance.tempatlahir, str)


@given(instance=Data_Pegawai_strategy)
def test_data_pegawai_tempatlahir_setter(instance):
    original = instance.tempatlahir
    instance.tempatlahir = original
    assert instance.tempatlahir == original

@given(instance=Data_Pegawai_strategy)
def test_data_pegawai_Namakaryawan_type(instance):
    assert isinstance(instance.Namakaryawan, str)


@given(instance=Data_Pegawai_strategy)
def test_data_pegawai_Namakaryawan_setter(instance):
    original = instance.Namakaryawan
    instance.Namakaryawan = original
    assert instance.Namakaryawan == original

@given(instance=Data_Pegawai_strategy)
def test_data_pegawai_alamat_type(instance):
    assert isinstance(instance.alamat, str)


@given(instance=Data_Pegawai_strategy)
def test_data_pegawai_alamat_setter(instance):
    original = instance.alamat
    instance.alamat = original
    assert instance.alamat == original

@given(instance=Data_Pegawai_strategy)
def test_data_pegawai_tanggallahir_type(instance):
    assert isinstance(instance.tanggallahir, date)


@given(instance=Data_Pegawai_strategy)
def test_data_pegawai_tanggallahir_setter(instance):
    original = instance.tanggallahir
    instance.tanggallahir = original
    assert instance.tanggallahir == original

@given(instance=Data_Pegawai_strategy)
def test_data_pegawai_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=Data_Pegawai_strategy)
def test_data_pegawai_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=account_Account_strategy)
@settings(max_examples=50)
def test_account_account_instantiation(instance):
    assert isinstance(instance, account_Account)

@given(instance=account_Account_strategy)
def test_account_account_accountNo_type(instance):
    assert isinstance(instance.accountNo, str)


@given(instance=account_Account_strategy)
def test_account_account_accountNo_setter(instance):
    original = instance.accountNo
    instance.accountNo = original
    assert instance.accountNo == original

@given(instance=account_Account_strategy)
def test_account_account_type_type(instance):
    assert isinstance(instance.type, account_accounttype)


@given(instance=account_Account_strategy)
def test_account_account_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=account_Account_strategy)
def test_account_account_balance_type(instance):
    assert isinstance(instance.balance, float)


@given(instance=account_Account_strategy)
def test_account_account_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original

@given(instance=account_CheckingAccount_strategy)
@settings(max_examples=50)
def test_account_checkingaccount_instantiation(instance):
    assert isinstance(instance, account_CheckingAccount)

@given(instance=account_CheckingAccount_strategy)
def test_account_checkingaccount_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=account_CheckingAccount_strategy)
def test_account_checkingaccount_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=account_CertificatesOfDepositAccount_strategy)
@settings(max_examples=50)
def test_account_certificatesofdepositaccount_instantiation(instance):
    assert isinstance(instance, account_CertificatesOfDepositAccount)

@given(instance=account_CertificatesOfDepositAccount_strategy)
def test_account_certificatesofdepositaccount_interestRate_type(instance):
    assert isinstance(instance.interestRate, float)


@given(instance=account_CertificatesOfDepositAccount_strategy)
def test_account_certificatesofdepositaccount_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original

@given(instance=account_CertificatesOfDepositAccount_strategy)
def test_account_certificatesofdepositaccount_timePeriod_type(instance):
    assert isinstance(instance.timePeriod, int)


@given(instance=account_CertificatesOfDepositAccount_strategy)
def test_account_certificatesofdepositaccount_timePeriod_setter(instance):
    original = instance.timePeriod
    instance.timePeriod = original
    assert instance.timePeriod == original

@given(instance=account_SavingsAccount_strategy)
@settings(max_examples=50)
def test_account_savingsaccount_instantiation(instance):
    assert isinstance(instance, account_SavingsAccount)

@given(instance=account_SavingsAccount_strategy)
def test_account_savingsaccount_interestRate_type(instance):
    assert isinstance(instance.interestRate, float)


@given(instance=account_SavingsAccount_strategy)
def test_account_savingsaccount_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original

@given(instance=transaction_TransferTransaction_strategy)
@settings(max_examples=50)
def test_transaction_transfertransaction_instantiation(instance):
    assert isinstance(instance, transaction_TransferTransaction)

@given(instance=transaction_TransferTransaction_strategy)
def test_transaction_transfertransaction_sourceAccount_type(instance):
    assert isinstance(instance.sourceAccount, account_account)


@given(instance=transaction_TransferTransaction_strategy)
def test_transaction_transfertransaction_sourceAccount_setter(instance):
    original = instance.sourceAccount
    instance.sourceAccount = original
    assert instance.sourceAccount == original

@given(instance=transaction_TransferTransaction_strategy)
def test_transaction_transfertransaction_targetAccount_type(instance):
    assert isinstance(instance.targetAccount, account_account)


@given(instance=transaction_TransferTransaction_strategy)
def test_transaction_transfertransaction_targetAccount_setter(instance):
    original = instance.targetAccount
    instance.targetAccount = original
    assert instance.targetAccount == original

@given(instance=transaction_WithdrawTransaction_strategy)
@settings(max_examples=50)
def test_transaction_withdrawtransaction_instantiation(instance):
    assert isinstance(instance, transaction_WithdrawTransaction)

@given(instance=transaction_DepositTransaction_strategy)
@settings(max_examples=50)
def test_transaction_deposittransaction_instantiation(instance):
    assert isinstance(instance, transaction_DepositTransaction)

@given(instance=transaction_Transaction_strategy)
@settings(max_examples=50)
def test_transaction_transaction_instantiation(instance):
    assert isinstance(instance, transaction_Transaction)

@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_amount_type(instance):
    assert isinstance(instance.amount, float)


@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_type_type(instance):
    assert isinstance(instance.type, transaction_transactiontype)


@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_transactionTime_type(instance):
    assert isinstance(instance.transactionTime, date)


@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_transactionTime_setter(instance):
    original = instance.transactionTime
    instance.transactionTime = original
    assert instance.transactionTime == original

@given(instance=Login_strategy)
@settings(max_examples=50)
def test_login_instantiation(instance):
    assert isinstance(instance, Login)

@given(instance=Login_strategy)
def test_login_securityAnswer_type(instance):
    assert isinstance(instance.securityAnswer, str)


@given(instance=Login_strategy)
def test_login_securityAnswer_setter(instance):
    original = instance.securityAnswer
    instance.securityAnswer = original
    assert instance.securityAnswer == original

@given(instance=Login_strategy)
def test_login_password_type(instance):
    assert isinstance(instance.password, str)


@given(instance=Login_strategy)
def test_login_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=Login_strategy)
def test_login_securityQuestion_type(instance):
    assert isinstance(instance.securityQuestion, str)


@given(instance=Login_strategy)
def test_login_securityQuestion_setter(instance):
    original = instance.securityQuestion
    instance.securityQuestion = original
    assert instance.securityQuestion == original

@given(instance=Login_strategy)
def test_login_username_type(instance):
    assert isinstance(instance.username, str)


@given(instance=Login_strategy)
def test_login_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original

@given(instance=Login_strategy)
def test_login_lastLoginTime_type(instance):
    assert isinstance(instance.lastLoginTime, date)


@given(instance=Login_strategy)
def test_login_lastLoginTime_setter(instance):
    original = instance.lastLoginTime
    instance.lastLoginTime = original
    assert instance.lastLoginTime == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)

@given(instance=Customer_strategy)
def test_customer_emailAddress_type(instance):
    assert isinstance(instance.emailAddress, str)


@given(instance=Customer_strategy)
def test_customer_emailAddress_setter(instance):
    original = instance.emailAddress
    instance.emailAddress = original
    assert instance.emailAddress == original

@given(instance=Customer_strategy)
def test_customer_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=Customer_strategy)
def test_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=Customer_strategy)
def test_customer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Customer_strategy)
def test_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Customer_strategy)
def test_customer_phoneNumber_type(instance):
    assert isinstance(instance.phoneNumber, str)


@given(instance=Customer_strategy)
def test_customer_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original

@given(instance=Customer_strategy)
def test_customer_dateOfBirth_type(instance):
    assert isinstance(instance.dateOfBirth, date)


@given(instance=Customer_strategy)
def test_customer_dateOfBirth_setter(instance):
    original = instance.dateOfBirth
    instance.dateOfBirth = original
    assert instance.dateOfBirth == original
