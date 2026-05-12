import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Khoa,
    BoMon,
    Order,
    SinhVien,
    Account,
    ConNguoi,
    Payment,
    Customer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_khoa_is_not_abstract():
    assert not inspect.isabstract(Khoa)


def test_khoa_constructor_exists():
    assert callable(Khoa.__init__)


def test_khoa_constructor_args():
    sig = inspect.signature(Khoa.__init__)
    params = list(sig.parameters.keys())
    assert "tenkhoa" in params, "Missing parameter 'tenkhoa'"
    assert "makhoa" in params, "Missing parameter 'makhoa'"

def test_khoa_has_tenkhoa():
    assert hasattr(Khoa, "tenkhoa")
    descriptor = None
    for klass in Khoa.__mro__:
        if "tenkhoa" in klass.__dict__:
            descriptor = klass.__dict__["tenkhoa"]
            break
    assert isinstance(descriptor, property)

def test_khoa_has_makhoa():
    assert hasattr(Khoa, "makhoa")
    descriptor = None
    for klass in Khoa.__mro__:
        if "makhoa" in klass.__dict__:
            descriptor = klass.__dict__["makhoa"]
            break
    assert isinstance(descriptor, property)



def test_bomon_is_not_abstract():
    assert not inspect.isabstract(BoMon)


def test_bomon_constructor_exists():
    assert callable(BoMon.__init__)


def test_bomon_constructor_args():
    sig = inspect.signature(BoMon.__init__)
    params = list(sig.parameters.keys())
    assert "tenbomon" in params, "Missing parameter 'tenbomon'"
    assert "mabomon" in params, "Missing parameter 'mabomon'"

def test_bomon_has_tenbomon():
    assert hasattr(BoMon, "tenbomon")
    descriptor = None
    for klass in BoMon.__mro__:
        if "tenbomon" in klass.__dict__:
            descriptor = klass.__dict__["tenbomon"]
            break
    assert isinstance(descriptor, property)

def test_bomon_has_mabomon():
    assert hasattr(BoMon, "mabomon")
    descriptor = None
    for klass in BoMon.__mro__:
        if "mabomon" in klass.__dict__:
            descriptor = klass.__dict__["mabomon"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "shipTo" in params, "Missing parameter 'shipTo'"
    assert "number" in params, "Missing parameter 'number'"
    assert "shipped" in params, "Missing parameter 'shipped'"
    assert "status" in params, "Missing parameter 'status'"
    assert "ordered" in params, "Missing parameter 'ordered'"
    assert "total" in params, "Missing parameter 'total'"

def test_order_has_shipTo():
    assert hasattr(Order, "shipTo")
    descriptor = None
    for klass in Order.__mro__:
        if "shipTo" in klass.__dict__:
            descriptor = klass.__dict__["shipTo"]
            break
    assert isinstance(descriptor, property)

def test_order_has_number():
    assert hasattr(Order, "number")
    descriptor = None
    for klass in Order.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_order_has_shipped():
    assert hasattr(Order, "shipped")
    descriptor = None
    for klass in Order.__mro__:
        if "shipped" in klass.__dict__:
            descriptor = klass.__dict__["shipped"]
            break
    assert isinstance(descriptor, property)

def test_order_has_status():
    assert hasattr(Order, "status")
    descriptor = None
    for klass in Order.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_order_has_ordered():
    assert hasattr(Order, "ordered")
    descriptor = None
    for klass in Order.__mro__:
        if "ordered" in klass.__dict__:
            descriptor = klass.__dict__["ordered"]
            break
    assert isinstance(descriptor, property)

def test_order_has_total():
    assert hasattr(Order, "total")
    descriptor = None
    for klass in Order.__mro__:
        if "total" in klass.__dict__:
            descriptor = klass.__dict__["total"]
            break
    assert isinstance(descriptor, property)



def test_sinhvien_is_not_abstract():
    assert not inspect.isabstract(SinhVien)


def test_sinhvien_constructor_exists():
    assert callable(SinhVien.__init__)


def test_sinhvien_constructor_args():
    sig = inspect.signature(SinhVien.__init__)
    params = list(sig.parameters.keys())
    assert "lop" in params, "Missing parameter 'lop'"
    assert "nganhhoc" in params, "Missing parameter 'nganhhoc'"
    assert "bomon" in params, "Missing parameter 'bomon'"
    assert "MSSV" in params, "Missing parameter 'MSSV'"

def test_sinhvien_has_lop():
    assert hasattr(SinhVien, "lop")
    descriptor = None
    for klass in SinhVien.__mro__:
        if "lop" in klass.__dict__:
            descriptor = klass.__dict__["lop"]
            break
    assert isinstance(descriptor, property)

def test_sinhvien_has_nganhhoc():
    assert hasattr(SinhVien, "nganhhoc")
    descriptor = None
    for klass in SinhVien.__mro__:
        if "nganhhoc" in klass.__dict__:
            descriptor = klass.__dict__["nganhhoc"]
            break
    assert isinstance(descriptor, property)

def test_sinhvien_has_bomon():
    assert hasattr(SinhVien, "bomon")
    descriptor = None
    for klass in SinhVien.__mro__:
        if "bomon" in klass.__dict__:
            descriptor = klass.__dict__["bomon"]
            break
    assert isinstance(descriptor, property)

def test_sinhvien_has_MSSV():
    assert hasattr(SinhVien, "MSSV")
    descriptor = None
    for klass in SinhVien.__mro__:
        if "MSSV" in klass.__dict__:
            descriptor = klass.__dict__["MSSV"]
            break
    assert isinstance(descriptor, property)



def test_account_is_not_abstract():
    assert not inspect.isabstract(Account)


def test_account_constructor_exists():
    assert callable(Account.__init__)


def test_account_constructor_args():
    sig = inspect.signature(Account.__init__)
    params = list(sig.parameters.keys())
    assert "isClosed" in params, "Missing parameter 'isClosed'"
    assert "open" in params, "Missing parameter 'open'"
    assert "closed" in params, "Missing parameter 'closed'"
    assert "billingAddress" in params, "Missing parameter 'billingAddress'"

def test_account_has_isClosed():
    assert hasattr(Account, "isClosed")
    descriptor = None
    for klass in Account.__mro__:
        if "isClosed" in klass.__dict__:
            descriptor = klass.__dict__["isClosed"]
            break
    assert isinstance(descriptor, property)

def test_account_has_open():
    assert hasattr(Account, "open")
    descriptor = None
    for klass in Account.__mro__:
        if "open" in klass.__dict__:
            descriptor = klass.__dict__["open"]
            break
    assert isinstance(descriptor, property)

def test_account_has_closed():
    assert hasattr(Account, "closed")
    descriptor = None
    for klass in Account.__mro__:
        if "closed" in klass.__dict__:
            descriptor = klass.__dict__["closed"]
            break
    assert isinstance(descriptor, property)

def test_account_has_billingAddress():
    assert hasattr(Account, "billingAddress")
    descriptor = None
    for klass in Account.__mro__:
        if "billingAddress" in klass.__dict__:
            descriptor = klass.__dict__["billingAddress"]
            break
    assert isinstance(descriptor, property)



def test_connguoi_is_not_abstract():
    assert not inspect.isabstract(ConNguoi)


def test_connguoi_constructor_exists():
    assert callable(ConNguoi.__init__)


def test_connguoi_constructor_args():
    sig = inspect.signature(ConNguoi.__init__)
    params = list(sig.parameters.keys())
    assert "CMND" in params, "Missing parameter 'CMND'"
    assert "diachi" in params, "Missing parameter 'diachi'"
    assert "ngaysinh" in params, "Missing parameter 'ngaysinh'"
    assert "hoten" in params, "Missing parameter 'hoten'"
    assert "gioitinh" in params, "Missing parameter 'gioitinh'"

def test_connguoi_has_CMND():
    assert hasattr(ConNguoi, "CMND")
    descriptor = None
    for klass in ConNguoi.__mro__:
        if "CMND" in klass.__dict__:
            descriptor = klass.__dict__["CMND"]
            break
    assert isinstance(descriptor, property)

def test_connguoi_has_diachi():
    assert hasattr(ConNguoi, "diachi")
    descriptor = None
    for klass in ConNguoi.__mro__:
        if "diachi" in klass.__dict__:
            descriptor = klass.__dict__["diachi"]
            break
    assert isinstance(descriptor, property)

def test_connguoi_has_ngaysinh():
    assert hasattr(ConNguoi, "ngaysinh")
    descriptor = None
    for klass in ConNguoi.__mro__:
        if "ngaysinh" in klass.__dict__:
            descriptor = klass.__dict__["ngaysinh"]
            break
    assert isinstance(descriptor, property)

def test_connguoi_has_hoten():
    assert hasattr(ConNguoi, "hoten")
    descriptor = None
    for klass in ConNguoi.__mro__:
        if "hoten" in klass.__dict__:
            descriptor = klass.__dict__["hoten"]
            break
    assert isinstance(descriptor, property)

def test_connguoi_has_gioitinh():
    assert hasattr(ConNguoi, "gioitinh")
    descriptor = None
    for klass in ConNguoi.__mro__:
        if "gioitinh" in klass.__dict__:
            descriptor = klass.__dict__["gioitinh"]
            break
    assert isinstance(descriptor, property)



def test_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "paidDate" in params, "Missing parameter 'paidDate'"
    assert "total" in params, "Missing parameter 'total'"
    assert "details" in params, "Missing parameter 'details'"

def test_payment_has_paidDate():
    assert hasattr(Payment, "paidDate")
    descriptor = None
    for klass in Payment.__mro__:
        if "paidDate" in klass.__dict__:
            descriptor = klass.__dict__["paidDate"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_total():
    assert hasattr(Payment, "total")
    descriptor = None
    for klass in Payment.__mro__:
        if "total" in klass.__dict__:
            descriptor = klass.__dict__["total"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_details():
    assert hasattr(Payment, "details")
    descriptor = None
    for klass in Payment.__mro__:
        if "details" in klass.__dict__:
            descriptor = klass.__dict__["details"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "phone" in params, "Missing parameter 'phone'"
    assert "email" in params, "Missing parameter 'email'"
    assert "address" in params, "Missing parameter 'address'"

def test_customer_has_phone():
    assert hasattr(Customer, "phone")
    descriptor = None
    for klass in Customer.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_email():
    assert hasattr(Customer, "email")
    descriptor = None
    for klass in Customer.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
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
Khoa_strategy = st.builds(
    Khoa,
    tenkhoa=
        safe_text,
    makhoa=
        safe_text
)
BoMon_strategy = st.builds(
    BoMon,
    tenbomon=
        safe_text,
    mabomon=
        safe_text
)
Order_strategy = st.builds(
    Order,
    shipTo=
        safe_text,
    number=
        st.integers(),
    shipped=
        st.booleans(),
    status=
        safe_text,
    ordered=
        st.dates(),
    total=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
SinhVien_strategy = st.builds(
    SinhVien,
    lop=
        safe_text,
    nganhhoc=
        safe_text,
    bomon=
        safe_text,
    MSSV=
        safe_text
)
Account_strategy = st.builds(
    Account,
    isClosed=
        st.booleans(),
    open=
        st.dates(),
    closed=
        st.dates(),
    billingAddress=
        safe_text
)
ConNguoi_strategy = st.builds(
    ConNguoi,
    CMND=
        safe_text,
    diachi=
        safe_text,
    ngaysinh=
        st.dates(),
    hoten=
        safe_text,
    gioitinh=
        st.booleans()
)
Payment_strategy = st.builds(
    Payment,
    paidDate=
        st.dates(),
    total=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    details=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    phone=
        safe_text,
    email=
        safe_text,
    address=
        safe_text
)

@given(instance=Khoa_strategy)
@settings(max_examples=50)
def test_khoa_instantiation(instance):
    assert isinstance(instance, Khoa)



@given(instance=Khoa_strategy)
def test_khoa_tenkhoa_setter(instance):
    original = instance.tenkhoa
    instance.tenkhoa = original
    assert instance.tenkhoa == original



@given(instance=Khoa_strategy)
def test_khoa_makhoa_setter(instance):
    original = instance.makhoa
    instance.makhoa = original
    assert instance.makhoa == original

@given(instance=BoMon_strategy)
@settings(max_examples=50)
def test_bomon_instantiation(instance):
    assert isinstance(instance, BoMon)



@given(instance=BoMon_strategy)
def test_bomon_tenbomon_setter(instance):
    original = instance.tenbomon
    instance.tenbomon = original
    assert instance.tenbomon == original



@given(instance=BoMon_strategy)
def test_bomon_mabomon_setter(instance):
    original = instance.mabomon
    instance.mabomon = original
    assert instance.mabomon == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_shipTo_setter(instance):
    original = instance.shipTo
    instance.shipTo = original
    assert instance.shipTo == original



@given(instance=Order_strategy)
def test_order_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=Order_strategy)
def test_order_shipped_setter(instance):
    original = instance.shipped
    instance.shipped = original
    assert instance.shipped == original



@given(instance=Order_strategy)
def test_order_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Order_strategy)
def test_order_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original



@given(instance=Order_strategy)
def test_order_total_setter(instance):
    original = instance.total
    instance.total = original
    assert instance.total == original

@given(instance=SinhVien_strategy)
@settings(max_examples=50)
def test_sinhvien_instantiation(instance):
    assert isinstance(instance, SinhVien)



@given(instance=SinhVien_strategy)
def test_sinhvien_lop_setter(instance):
    original = instance.lop
    instance.lop = original
    assert instance.lop == original



@given(instance=SinhVien_strategy)
def test_sinhvien_nganhhoc_setter(instance):
    original = instance.nganhhoc
    instance.nganhhoc = original
    assert instance.nganhhoc == original



@given(instance=SinhVien_strategy)
def test_sinhvien_bomon_setter(instance):
    original = instance.bomon
    instance.bomon = original
    assert instance.bomon == original



@given(instance=SinhVien_strategy)
def test_sinhvien_MSSV_setter(instance):
    original = instance.MSSV
    instance.MSSV = original
    assert instance.MSSV == original

@given(instance=Account_strategy)
@settings(max_examples=50)
def test_account_instantiation(instance):
    assert isinstance(instance, Account)



@given(instance=Account_strategy)
def test_account_isClosed_setter(instance):
    original = instance.isClosed
    instance.isClosed = original
    assert instance.isClosed == original



@given(instance=Account_strategy)
def test_account_open_setter(instance):
    original = instance.open
    instance.open = original
    assert instance.open == original



@given(instance=Account_strategy)
def test_account_closed_setter(instance):
    original = instance.closed
    instance.closed = original
    assert instance.closed == original



@given(instance=Account_strategy)
def test_account_billingAddress_setter(instance):
    original = instance.billingAddress
    instance.billingAddress = original
    assert instance.billingAddress == original

@given(instance=ConNguoi_strategy)
@settings(max_examples=50)
def test_connguoi_instantiation(instance):
    assert isinstance(instance, ConNguoi)



@given(instance=ConNguoi_strategy)
def test_connguoi_CMND_setter(instance):
    original = instance.CMND
    instance.CMND = original
    assert instance.CMND == original



@given(instance=ConNguoi_strategy)
def test_connguoi_diachi_setter(instance):
    original = instance.diachi
    instance.diachi = original
    assert instance.diachi == original



@given(instance=ConNguoi_strategy)
def test_connguoi_ngaysinh_setter(instance):
    original = instance.ngaysinh
    instance.ngaysinh = original
    assert instance.ngaysinh == original



@given(instance=ConNguoi_strategy)
def test_connguoi_hoten_setter(instance):
    original = instance.hoten
    instance.hoten = original
    assert instance.hoten == original



@given(instance=ConNguoi_strategy)
def test_connguoi_gioitinh_setter(instance):
    original = instance.gioitinh
    instance.gioitinh = original
    assert instance.gioitinh == original

@given(instance=Payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, Payment)



@given(instance=Payment_strategy)
def test_payment_paidDate_setter(instance):
    original = instance.paidDate
    instance.paidDate = original
    assert instance.paidDate == original



@given(instance=Payment_strategy)
def test_payment_total_setter(instance):
    original = instance.total
    instance.total = original
    assert instance.total == original



@given(instance=Payment_strategy)
def test_payment_details_setter(instance):
    original = instance.details
    instance.details = original
    assert instance.details == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=Customer_strategy)
def test_customer_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Customer_strategy)
def test_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original
