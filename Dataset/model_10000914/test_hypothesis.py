import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Direccion,
    Personas,
    Login1,
    Cliente,
    gerente,
    Class,
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
    transaction_TransactionType,
    account_AccountType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_direccion_is_not_abstract():
    assert not inspect.isabstract(Direccion)


def test_direccion_constructor_exists():
    assert callable(Direccion.__init__)


def test_direccion_constructor_args():
    sig = inspect.signature(Direccion.__init__)
    params = list(sig.parameters.keys())
    assert "municipio" in params, "Missing parameter 'municipio'"
    assert "estado" in params, "Missing parameter 'estado'"
    assert "zona" in params, "Missing parameter 'zona'"
    assert "tipo" in params, "Missing parameter 'tipo'"
    assert "cp" in params, "Missing parameter 'cp'"
    assert "idMunicipio" in params, "Missing parameter 'idMunicipio'"
    assert "idEstado" in params, "Missing parameter 'idEstado'"
    assert "asentamiento" in params, "Missing parameter 'asentamiento'"
    assert "ciudad" in params, "Missing parameter 'ciudad'"
    assert "idDireccion" in params, "Missing parameter 'idDireccion'"

def test_direccion_has_municipio():
    assert hasattr(Direccion, "municipio")
    descriptor = None
    for klass in Direccion.__mro__:
        if "municipio" in klass.__dict__:
            descriptor = klass.__dict__["municipio"]
            break
    assert isinstance(descriptor, property)

def test_direccion_has_estado():
    assert hasattr(Direccion, "estado")
    descriptor = None
    for klass in Direccion.__mro__:
        if "estado" in klass.__dict__:
            descriptor = klass.__dict__["estado"]
            break
    assert isinstance(descriptor, property)

def test_direccion_has_zona():
    assert hasattr(Direccion, "zona")
    descriptor = None
    for klass in Direccion.__mro__:
        if "zona" in klass.__dict__:
            descriptor = klass.__dict__["zona"]
            break
    assert isinstance(descriptor, property)

def test_direccion_has_tipo():
    assert hasattr(Direccion, "tipo")
    descriptor = None
    for klass in Direccion.__mro__:
        if "tipo" in klass.__dict__:
            descriptor = klass.__dict__["tipo"]
            break
    assert isinstance(descriptor, property)

def test_direccion_has_cp():
    assert hasattr(Direccion, "cp")
    descriptor = None
    for klass in Direccion.__mro__:
        if "cp" in klass.__dict__:
            descriptor = klass.__dict__["cp"]
            break
    assert isinstance(descriptor, property)

def test_direccion_has_idMunicipio():
    assert hasattr(Direccion, "idMunicipio")
    descriptor = None
    for klass in Direccion.__mro__:
        if "idMunicipio" in klass.__dict__:
            descriptor = klass.__dict__["idMunicipio"]
            break
    assert isinstance(descriptor, property)

def test_direccion_has_idEstado():
    assert hasattr(Direccion, "idEstado")
    descriptor = None
    for klass in Direccion.__mro__:
        if "idEstado" in klass.__dict__:
            descriptor = klass.__dict__["idEstado"]
            break
    assert isinstance(descriptor, property)

def test_direccion_has_asentamiento():
    assert hasattr(Direccion, "asentamiento")
    descriptor = None
    for klass in Direccion.__mro__:
        if "asentamiento" in klass.__dict__:
            descriptor = klass.__dict__["asentamiento"]
            break
    assert isinstance(descriptor, property)

def test_direccion_has_ciudad():
    assert hasattr(Direccion, "ciudad")
    descriptor = None
    for klass in Direccion.__mro__:
        if "ciudad" in klass.__dict__:
            descriptor = klass.__dict__["ciudad"]
            break
    assert isinstance(descriptor, property)

def test_direccion_has_idDireccion():
    assert hasattr(Direccion, "idDireccion")
    descriptor = None
    for klass in Direccion.__mro__:
        if "idDireccion" in klass.__dict__:
            descriptor = klass.__dict__["idDireccion"]
            break
    assert isinstance(descriptor, property)



def test_personas_is_not_abstract():
    assert not inspect.isabstract(Personas)


def test_personas_constructor_exists():
    assert callable(Personas.__init__)


def test_personas_constructor_args():
    sig = inspect.signature(Personas.__init__)
    params = list(sig.parameters.keys())
    assert "aMaterno" in params, "Missing parameter 'aMaterno'"
    assert "aPaterno" in params, "Missing parameter 'aPaterno'"
    assert "estado" in params, "Missing parameter 'estado'"
    assert "idPersona" in params, "Missing parameter 'idPersona'"
    assert "telefono" in params, "Missing parameter 'telefono'"
    assert "nombre" in params, "Missing parameter 'nombre'"

def test_personas_has_aMaterno():
    assert hasattr(Personas, "aMaterno")
    descriptor = None
    for klass in Personas.__mro__:
        if "aMaterno" in klass.__dict__:
            descriptor = klass.__dict__["aMaterno"]
            break
    assert isinstance(descriptor, property)

def test_personas_has_aPaterno():
    assert hasattr(Personas, "aPaterno")
    descriptor = None
    for klass in Personas.__mro__:
        if "aPaterno" in klass.__dict__:
            descriptor = klass.__dict__["aPaterno"]
            break
    assert isinstance(descriptor, property)

def test_personas_has_estado():
    assert hasattr(Personas, "estado")
    descriptor = None
    for klass in Personas.__mro__:
        if "estado" in klass.__dict__:
            descriptor = klass.__dict__["estado"]
            break
    assert isinstance(descriptor, property)

def test_personas_has_idPersona():
    assert hasattr(Personas, "idPersona")
    descriptor = None
    for klass in Personas.__mro__:
        if "idPersona" in klass.__dict__:
            descriptor = klass.__dict__["idPersona"]
            break
    assert isinstance(descriptor, property)

def test_personas_has_telefono():
    assert hasattr(Personas, "telefono")
    descriptor = None
    for klass in Personas.__mro__:
        if "telefono" in klass.__dict__:
            descriptor = klass.__dict__["telefono"]
            break
    assert isinstance(descriptor, property)

def test_personas_has_nombre():
    assert hasattr(Personas, "nombre")
    descriptor = None
    for klass in Personas.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)



def test_login1_is_not_abstract():
    assert not inspect.isabstract(Login1)


def test_login1_constructor_exists():
    assert callable(Login1.__init__)


def test_login1_constructor_args():
    sig = inspect.signature(Login1.__init__)
    params = list(sig.parameters.keys())
    assert "usuario" in params, "Missing parameter 'usuario'"
    assert "password" in params, "Missing parameter 'password'"

def test_login1_has_usuario():
    assert hasattr(Login1, "usuario")
    descriptor = None
    for klass in Login1.__mro__:
        if "usuario" in klass.__dict__:
            descriptor = klass.__dict__["usuario"]
            break
    assert isinstance(descriptor, property)

def test_login1_has_password():
    assert hasattr(Login1, "password")
    descriptor = None
    for klass in Login1.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)



def test_cliente_is_not_abstract():
    assert not inspect.isabstract(Cliente)


def test_cliente_constructor_exists():
    assert callable(Cliente.__init__)


def test_cliente_constructor_args():
    sig = inspect.signature(Cliente.__init__)
    params = list(sig.parameters.keys())
    assert "idAval" in params, "Missing parameter 'idAval'"
    assert "idDireccion" in params, "Missing parameter 'idDireccion'"
    assert "idPersona" in params, "Missing parameter 'idPersona'"
    assert "fechaInicio" in params, "Missing parameter 'fechaInicio'"
    assert "idPrestamo" in params, "Missing parameter 'idPrestamo'"
    assert "noTarjeta" in params, "Missing parameter 'noTarjeta'"
    assert "idCliente" in params, "Missing parameter 'idCliente'"
    assert "contactoReferencia" in params, "Missing parameter 'contactoReferencia'"
    assert "idDiaPago" in params, "Missing parameter 'idDiaPago'"

def test_cliente_has_idAval():
    assert hasattr(Cliente, "idAval")
    descriptor = None
    for klass in Cliente.__mro__:
        if "idAval" in klass.__dict__:
            descriptor = klass.__dict__["idAval"]
            break
    assert isinstance(descriptor, property)

def test_cliente_has_idDireccion():
    assert hasattr(Cliente, "idDireccion")
    descriptor = None
    for klass in Cliente.__mro__:
        if "idDireccion" in klass.__dict__:
            descriptor = klass.__dict__["idDireccion"]
            break
    assert isinstance(descriptor, property)

def test_cliente_has_idPersona():
    assert hasattr(Cliente, "idPersona")
    descriptor = None
    for klass in Cliente.__mro__:
        if "idPersona" in klass.__dict__:
            descriptor = klass.__dict__["idPersona"]
            break
    assert isinstance(descriptor, property)

def test_cliente_has_fechaInicio():
    assert hasattr(Cliente, "fechaInicio")
    descriptor = None
    for klass in Cliente.__mro__:
        if "fechaInicio" in klass.__dict__:
            descriptor = klass.__dict__["fechaInicio"]
            break
    assert isinstance(descriptor, property)

def test_cliente_has_idPrestamo():
    assert hasattr(Cliente, "idPrestamo")
    descriptor = None
    for klass in Cliente.__mro__:
        if "idPrestamo" in klass.__dict__:
            descriptor = klass.__dict__["idPrestamo"]
            break
    assert isinstance(descriptor, property)

def test_cliente_has_noTarjeta():
    assert hasattr(Cliente, "noTarjeta")
    descriptor = None
    for klass in Cliente.__mro__:
        if "noTarjeta" in klass.__dict__:
            descriptor = klass.__dict__["noTarjeta"]
            break
    assert isinstance(descriptor, property)

def test_cliente_has_idCliente():
    assert hasattr(Cliente, "idCliente")
    descriptor = None
    for klass in Cliente.__mro__:
        if "idCliente" in klass.__dict__:
            descriptor = klass.__dict__["idCliente"]
            break
    assert isinstance(descriptor, property)

def test_cliente_has_contactoReferencia():
    assert hasattr(Cliente, "contactoReferencia")
    descriptor = None
    for klass in Cliente.__mro__:
        if "contactoReferencia" in klass.__dict__:
            descriptor = klass.__dict__["contactoReferencia"]
            break
    assert isinstance(descriptor, property)

def test_cliente_has_idDiaPago():
    assert hasattr(Cliente, "idDiaPago")
    descriptor = None
    for klass in Cliente.__mro__:
        if "idDiaPago" in klass.__dict__:
            descriptor = klass.__dict__["idDiaPago"]
            break
    assert isinstance(descriptor, property)



def test_gerente_is_not_abstract():
    assert not inspect.isabstract(gerente)


def test_gerente_constructor_exists():
    assert callable(gerente.__init__)


def test_gerente_constructor_args():
    sig = inspect.signature(gerente.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "idZona" in params, "Missing parameter 'idZona'"
    assert "idGerente" in params, "Missing parameter 'idGerente'"
    assert "idUsuario" in params, "Missing parameter 'idUsuario'"
    assert "idPersona" in params, "Missing parameter 'idPersona'"

def test_gerente_has_id():
    assert hasattr(gerente, "id")
    descriptor = None
    for klass in gerente.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_gerente_has_idZona():
    assert hasattr(gerente, "idZona")
    descriptor = None
    for klass in gerente.__mro__:
        if "idZona" in klass.__dict__:
            descriptor = klass.__dict__["idZona"]
            break
    assert isinstance(descriptor, property)

def test_gerente_has_idGerente():
    assert hasattr(gerente, "idGerente")
    descriptor = None
    for klass in gerente.__mro__:
        if "idGerente" in klass.__dict__:
            descriptor = klass.__dict__["idGerente"]
            break
    assert isinstance(descriptor, property)

def test_gerente_has_idUsuario():
    assert hasattr(gerente, "idUsuario")
    descriptor = None
    for klass in gerente.__mro__:
        if "idUsuario" in klass.__dict__:
            descriptor = klass.__dict__["idUsuario"]
            break
    assert isinstance(descriptor, property)

def test_gerente_has_idPersona():
    assert hasattr(gerente, "idPersona")
    descriptor = None
    for klass in gerente.__mro__:
        if "idPersona" in klass.__dict__:
            descriptor = klass.__dict__["idPersona"]
            break
    assert isinstance(descriptor, property)



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())
    assert "attribute2" in params, "Missing parameter 'attribute2'"
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_class_has_attribute2():
    assert hasattr(Class, "attribute2")
    descriptor = None
    for klass in Class.__mro__:
        if "attribute2" in klass.__dict__:
            descriptor = klass.__dict__["attribute2"]
            break
    assert isinstance(descriptor, property)

def test_class_has_attribute():
    assert hasattr(Class, "attribute")
    descriptor = None
    for klass in Class.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
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
    assert "balance" in params, "Missing parameter 'balance'"
    assert "type" in params, "Missing parameter 'type'"

def test_account_account_has_accountNo():
    assert hasattr(account_Account, "accountNo")
    descriptor = None
    for klass in account_Account.__mro__:
        if "accountNo" in klass.__dict__:
            descriptor = klass.__dict__["accountNo"]
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

def test_account_account_has_type():
    assert hasattr(account_Account, "type")
    descriptor = None
    for klass in account_Account.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
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
    assert "timePeriod" in params, "Missing parameter 'timePeriod'"
    assert "interestRate" in params, "Missing parameter 'interestRate'"

def test_account_certificatesofdepositaccount_has_timePeriod():
    assert hasattr(account_CertificatesOfDepositAccount, "timePeriod")
    descriptor = None
    for klass in account_CertificatesOfDepositAccount.__mro__:
        if "timePeriod" in klass.__dict__:
            descriptor = klass.__dict__["timePeriod"]
            break
    assert isinstance(descriptor, property)

def test_account_certificatesofdepositaccount_has_interestRate():
    assert hasattr(account_CertificatesOfDepositAccount, "interestRate")
    descriptor = None
    for klass in account_CertificatesOfDepositAccount.__mro__:
        if "interestRate" in klass.__dict__:
            descriptor = klass.__dict__["interestRate"]
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
    assert "targetAccount" in params, "Missing parameter 'targetAccount'"
    assert "sourceAccount" in params, "Missing parameter 'sourceAccount'"

def test_transaction_transfertransaction_has_targetAccount():
    assert hasattr(transaction_TransferTransaction, "targetAccount")
    descriptor = None
    for klass in transaction_TransferTransaction.__mro__:
        if "targetAccount" in klass.__dict__:
            descriptor = klass.__dict__["targetAccount"]
            break
    assert isinstance(descriptor, property)

def test_transaction_transfertransaction_has_sourceAccount():
    assert hasattr(transaction_TransferTransaction, "sourceAccount")
    descriptor = None
    for klass in transaction_TransferTransaction.__mro__:
        if "sourceAccount" in klass.__dict__:
            descriptor = klass.__dict__["sourceAccount"]
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
    assert "transactionTime" in params, "Missing parameter 'transactionTime'"
    assert "type" in params, "Missing parameter 'type'"

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

def test_transaction_transaction_has_transactionTime():
    assert hasattr(transaction_Transaction, "transactionTime")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "transactionTime" in klass.__dict__:
            descriptor = klass.__dict__["transactionTime"]
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



def test_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_login_constructor_exists():
    assert callable(Login.__init__)


def test_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "lastLoginTime" in params, "Missing parameter 'lastLoginTime'"
    assert "securityAnswer" in params, "Missing parameter 'securityAnswer'"
    assert "username" in params, "Missing parameter 'username'"
    assert "securityQuestion" in params, "Missing parameter 'securityQuestion'"

def test_login_has_password():
    assert hasattr(Login, "password")
    descriptor = None
    for klass in Login.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
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

def test_login_has_securityAnswer():
    assert hasattr(Login, "securityAnswer")
    descriptor = None
    for klass in Login.__mro__:
        if "securityAnswer" in klass.__dict__:
            descriptor = klass.__dict__["securityAnswer"]
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

def test_login_has_securityQuestion():
    assert hasattr(Login, "securityQuestion")
    descriptor = None
    for klass in Login.__mro__:
        if "securityQuestion" in klass.__dict__:
            descriptor = klass.__dict__["securityQuestion"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"
    assert "name" in params, "Missing parameter 'name'"
    assert "emailAddress" in params, "Missing parameter 'emailAddress'"
    assert "address" in params, "Missing parameter 'address'"
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"

def test_customer_has_dateOfBirth():
    assert hasattr(Customer, "dateOfBirth")
    descriptor = None
    for klass in Customer.__mro__:
        if "dateOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["dateOfBirth"]
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

def test_customer_has_phoneNumber():
    assert hasattr(Customer, "phoneNumber")
    descriptor = None
    for klass in Customer.__mro__:
        if "phoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["phoneNumber"]
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
Direccion_strategy = st.builds(
    Direccion,
    municipio=
        safe_text,
    estado=
        safe_text,
    zona=
        safe_text,
    tipo=
        safe_text,
    cp=
        st.integers(),
    idMunicipio=
        st.integers(),
    idEstado=
        st.integers(),
    asentamiento=
        safe_text,
    ciudad=
        safe_text,
    idDireccion=
        st.integers()
)
Personas_strategy = st.builds(
    Personas,
    aMaterno=
        safe_text,
    aPaterno=
        safe_text,
    estado=
        safe_text,
    idPersona=
        st.integers(),
    telefono=
        safe_text,
    nombre=
        safe_text
)
Login1_strategy = st.builds(
    Login1,
    usuario=
        safe_text,
    password=
        safe_text
)
Cliente_strategy = st.builds(
    Cliente,
    idAval=
        st.integers(),
    idDireccion=
        st.integers(),
    idPersona=
        st.integers(),
    fechaInicio=
        st.dates(),
    idPrestamo=
        st.integers(),
    noTarjeta=
        safe_text,
    idCliente=
        st.integers(),
    contactoReferencia=
        safe_text,
    idDiaPago=
        st.integers()
)
gerente_strategy = st.builds(
    gerente,
    id=
        safe_text,
    idZona=
        st.integers(),
    idGerente=
        st.integers(),
    idUsuario=
        st.integers(),
    idPersona=
        safe_text
)
Class_strategy = st.builds(
    Class,
    attribute2=
        safe_text,
    attribute=
        safe_text
)
account_Account_strategy = st.builds(
    account_Account,
    accountNo=
        safe_text,
    balance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    type=
        st.none()
)
account_CheckingAccount_strategy = st.builds(
    account_CheckingAccount,
    name=
        safe_text
)
account_CertificatesOfDepositAccount_strategy = st.builds(
    account_CertificatesOfDepositAccount,
    timePeriod=
        st.integers(),
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
account_SavingsAccount_strategy = st.builds(
    account_SavingsAccount,
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
transaction_TransferTransaction_strategy = st.builds(
    transaction_TransferTransaction,
    targetAccount=
        st.none(),
    sourceAccount=
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
    transactionTime=
        st.dates(),
    type=
        st.none()
)
Login_strategy = st.builds(
    Login,
    password=
        safe_text,
    lastLoginTime=
        st.dates(),
    securityAnswer=
        safe_text,
    username=
        safe_text,
    securityQuestion=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    dateOfBirth=
        st.dates(),
    name=
        safe_text,
    emailAddress=
        safe_text,
    address=
        safe_text,
    phoneNumber=
        safe_text
)

@given(instance=Direccion_strategy)
@settings(max_examples=50)
def test_direccion_instantiation(instance):
    assert isinstance(instance, Direccion)



@given(instance=Direccion_strategy)
def test_direccion_municipio_setter(instance):
    original = instance.municipio
    instance.municipio = original
    assert instance.municipio == original



@given(instance=Direccion_strategy)
def test_direccion_estado_setter(instance):
    original = instance.estado
    instance.estado = original
    assert instance.estado == original



@given(instance=Direccion_strategy)
def test_direccion_zona_setter(instance):
    original = instance.zona
    instance.zona = original
    assert instance.zona == original



@given(instance=Direccion_strategy)
def test_direccion_tipo_setter(instance):
    original = instance.tipo
    instance.tipo = original
    assert instance.tipo == original



@given(instance=Direccion_strategy)
def test_direccion_cp_setter(instance):
    original = instance.cp
    instance.cp = original
    assert instance.cp == original



@given(instance=Direccion_strategy)
def test_direccion_idMunicipio_setter(instance):
    original = instance.idMunicipio
    instance.idMunicipio = original
    assert instance.idMunicipio == original



@given(instance=Direccion_strategy)
def test_direccion_idEstado_setter(instance):
    original = instance.idEstado
    instance.idEstado = original
    assert instance.idEstado == original



@given(instance=Direccion_strategy)
def test_direccion_asentamiento_setter(instance):
    original = instance.asentamiento
    instance.asentamiento = original
    assert instance.asentamiento == original



@given(instance=Direccion_strategy)
def test_direccion_ciudad_setter(instance):
    original = instance.ciudad
    instance.ciudad = original
    assert instance.ciudad == original



@given(instance=Direccion_strategy)
def test_direccion_idDireccion_setter(instance):
    original = instance.idDireccion
    instance.idDireccion = original
    assert instance.idDireccion == original

@given(instance=Personas_strategy)
@settings(max_examples=50)
def test_personas_instantiation(instance):
    assert isinstance(instance, Personas)



@given(instance=Personas_strategy)
def test_personas_aMaterno_setter(instance):
    original = instance.aMaterno
    instance.aMaterno = original
    assert instance.aMaterno == original



@given(instance=Personas_strategy)
def test_personas_aPaterno_setter(instance):
    original = instance.aPaterno
    instance.aPaterno = original
    assert instance.aPaterno == original



@given(instance=Personas_strategy)
def test_personas_estado_setter(instance):
    original = instance.estado
    instance.estado = original
    assert instance.estado == original



@given(instance=Personas_strategy)
def test_personas_idPersona_setter(instance):
    original = instance.idPersona
    instance.idPersona = original
    assert instance.idPersona == original



@given(instance=Personas_strategy)
def test_personas_telefono_setter(instance):
    original = instance.telefono
    instance.telefono = original
    assert instance.telefono == original



@given(instance=Personas_strategy)
def test_personas_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original

@given(instance=Login1_strategy)
@settings(max_examples=50)
def test_login1_instantiation(instance):
    assert isinstance(instance, Login1)



@given(instance=Login1_strategy)
def test_login1_usuario_setter(instance):
    original = instance.usuario
    instance.usuario = original
    assert instance.usuario == original



@given(instance=Login1_strategy)
def test_login1_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=Cliente_strategy)
@settings(max_examples=50)
def test_cliente_instantiation(instance):
    assert isinstance(instance, Cliente)



@given(instance=Cliente_strategy)
def test_cliente_idAval_setter(instance):
    original = instance.idAval
    instance.idAval = original
    assert instance.idAval == original



@given(instance=Cliente_strategy)
def test_cliente_idDireccion_setter(instance):
    original = instance.idDireccion
    instance.idDireccion = original
    assert instance.idDireccion == original



@given(instance=Cliente_strategy)
def test_cliente_idPersona_setter(instance):
    original = instance.idPersona
    instance.idPersona = original
    assert instance.idPersona == original



@given(instance=Cliente_strategy)
def test_cliente_fechaInicio_setter(instance):
    original = instance.fechaInicio
    instance.fechaInicio = original
    assert instance.fechaInicio == original



@given(instance=Cliente_strategy)
def test_cliente_idPrestamo_setter(instance):
    original = instance.idPrestamo
    instance.idPrestamo = original
    assert instance.idPrestamo == original



@given(instance=Cliente_strategy)
def test_cliente_noTarjeta_setter(instance):
    original = instance.noTarjeta
    instance.noTarjeta = original
    assert instance.noTarjeta == original



@given(instance=Cliente_strategy)
def test_cliente_idCliente_setter(instance):
    original = instance.idCliente
    instance.idCliente = original
    assert instance.idCliente == original



@given(instance=Cliente_strategy)
def test_cliente_contactoReferencia_setter(instance):
    original = instance.contactoReferencia
    instance.contactoReferencia = original
    assert instance.contactoReferencia == original



@given(instance=Cliente_strategy)
def test_cliente_idDiaPago_setter(instance):
    original = instance.idDiaPago
    instance.idDiaPago = original
    assert instance.idDiaPago == original

@given(instance=gerente_strategy)
@settings(max_examples=50)
def test_gerente_instantiation(instance):
    assert isinstance(instance, gerente)



@given(instance=gerente_strategy)
def test_gerente_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=gerente_strategy)
def test_gerente_idZona_setter(instance):
    original = instance.idZona
    instance.idZona = original
    assert instance.idZona == original



@given(instance=gerente_strategy)
def test_gerente_idGerente_setter(instance):
    original = instance.idGerente
    instance.idGerente = original
    assert instance.idGerente == original



@given(instance=gerente_strategy)
def test_gerente_idUsuario_setter(instance):
    original = instance.idUsuario
    instance.idUsuario = original
    assert instance.idUsuario == original



@given(instance=gerente_strategy)
def test_gerente_idPersona_setter(instance):
    original = instance.idPersona
    instance.idPersona = original
    assert instance.idPersona == original

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)



@given(instance=Class_strategy)
def test_class_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original



@given(instance=Class_strategy)
def test_class_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=account_Account_strategy)
@settings(max_examples=50)
def test_account_account_instantiation(instance):
    assert isinstance(instance, account_Account)



@given(instance=account_Account_strategy)
def test_account_account_accountNo_setter(instance):
    original = instance.accountNo
    instance.accountNo = original
    assert instance.accountNo == original



@given(instance=account_Account_strategy)
def test_account_account_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original



@given(instance=account_Account_strategy)
def test_account_account_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=account_CheckingAccount_strategy)
@settings(max_examples=50)
def test_account_checkingaccount_instantiation(instance):
    assert isinstance(instance, account_CheckingAccount)



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
def test_account_certificatesofdepositaccount_timePeriod_setter(instance):
    original = instance.timePeriod
    instance.timePeriod = original
    assert instance.timePeriod == original



@given(instance=account_CertificatesOfDepositAccount_strategy)
def test_account_certificatesofdepositaccount_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original

@given(instance=account_SavingsAccount_strategy)
@settings(max_examples=50)
def test_account_savingsaccount_instantiation(instance):
    assert isinstance(instance, account_SavingsAccount)



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
def test_transaction_transfertransaction_targetAccount_setter(instance):
    original = instance.targetAccount
    instance.targetAccount = original
    assert instance.targetAccount == original



@given(instance=transaction_TransferTransaction_strategy)
def test_transaction_transfertransaction_sourceAccount_setter(instance):
    original = instance.sourceAccount
    instance.sourceAccount = original
    assert instance.sourceAccount == original

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
def test_transaction_transaction_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_transactionTime_setter(instance):
    original = instance.transactionTime
    instance.transactionTime = original
    assert instance.transactionTime == original



@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Login_strategy)
@settings(max_examples=50)
def test_login_instantiation(instance):
    assert isinstance(instance, Login)



@given(instance=Login_strategy)
def test_login_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Login_strategy)
def test_login_lastLoginTime_setter(instance):
    original = instance.lastLoginTime
    instance.lastLoginTime = original
    assert instance.lastLoginTime == original



@given(instance=Login_strategy)
def test_login_securityAnswer_setter(instance):
    original = instance.securityAnswer
    instance.securityAnswer = original
    assert instance.securityAnswer == original



@given(instance=Login_strategy)
def test_login_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Login_strategy)
def test_login_securityQuestion_setter(instance):
    original = instance.securityQuestion
    instance.securityQuestion = original
    assert instance.securityQuestion == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_dateOfBirth_setter(instance):
    original = instance.dateOfBirth
    instance.dateOfBirth = original
    assert instance.dateOfBirth == original



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
def test_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Customer_strategy)
def test_customer_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original
