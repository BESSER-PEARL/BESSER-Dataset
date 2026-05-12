import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    admin,
    orderdetail,
    order,
    role,
    pembeli1,
    vendor,
    user,
    kategori,
    barang,
    penjual,
    Kategori,
    Produk,
    Shippinginfo,
    Orderdetail,
    Order,
    Cart,
    pembeli,
    Admin,
    User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_admin_is_not_abstract():
    assert not inspect.isabstract(admin)


def test_admin_constructor_exists():
    assert callable(admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(admin.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "username" in params, "Missing parameter 'username'"
    assert "id" in params, "Missing parameter 'id'"

def test_admin_has_password():
    assert hasattr(admin, "password")
    descriptor = None
    for klass in admin.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_username():
    assert hasattr(admin, "username")
    descriptor = None
    for klass in admin.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_id():
    assert hasattr(admin, "id")
    descriptor = None
    for klass in admin.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_orderdetail_is_not_abstract():
    assert not inspect.isabstract(orderdetail)


def test_orderdetail_constructor_exists():
    assert callable(orderdetail.__init__)


def test_orderdetail_constructor_args():
    sig = inspect.signature(orderdetail.__init__)
    params = list(sig.parameters.keys())
    assert "order_id" in params, "Missing parameter 'order_id'"
    assert "total" in params, "Missing parameter 'total'"
    assert "barang_id" in params, "Missing parameter 'barang_id'"

def test_orderdetail_has_order_id():
    assert hasattr(orderdetail, "order_id")
    descriptor = None
    for klass in orderdetail.__mro__:
        if "order_id" in klass.__dict__:
            descriptor = klass.__dict__["order_id"]
            break
    assert isinstance(descriptor, property)

def test_orderdetail_has_total():
    assert hasattr(orderdetail, "total")
    descriptor = None
    for klass in orderdetail.__mro__:
        if "total" in klass.__dict__:
            descriptor = klass.__dict__["total"]
            break
    assert isinstance(descriptor, property)

def test_orderdetail_has_barang_id():
    assert hasattr(orderdetail, "barang_id")
    descriptor = None
    for klass in orderdetail.__mro__:
        if "barang_id" in klass.__dict__:
            descriptor = klass.__dict__["barang_id"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(order)


def test_order_constructor_exists():
    assert callable(order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(order.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "dateorder" in params, "Missing parameter 'dateorder'"
    assert "id_user" in params, "Missing parameter 'id_user'"
    assert "order_id" in params, "Missing parameter 'order_id'"

def test_order_has_status():
    assert hasattr(order, "status")
    descriptor = None
    for klass in order.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_order_has_dateorder():
    assert hasattr(order, "dateorder")
    descriptor = None
    for klass in order.__mro__:
        if "dateorder" in klass.__dict__:
            descriptor = klass.__dict__["dateorder"]
            break
    assert isinstance(descriptor, property)

def test_order_has_id_user():
    assert hasattr(order, "id_user")
    descriptor = None
    for klass in order.__mro__:
        if "id_user" in klass.__dict__:
            descriptor = klass.__dict__["id_user"]
            break
    assert isinstance(descriptor, property)

def test_order_has_order_id():
    assert hasattr(order, "order_id")
    descriptor = None
    for klass in order.__mro__:
        if "order_id" in klass.__dict__:
            descriptor = klass.__dict__["order_id"]
            break
    assert isinstance(descriptor, property)



def test_role_is_not_abstract():
    assert not inspect.isabstract(role)


def test_role_constructor_exists():
    assert callable(role.__init__)


def test_role_constructor_args():
    sig = inspect.signature(role.__init__)
    params = list(sig.parameters.keys())
    assert "nama_role" in params, "Missing parameter 'nama_role'"
    assert "deskripsi_role" in params, "Missing parameter 'deskripsi_role'"
    assert "id" in params, "Missing parameter 'id'"

def test_role_has_nama_role():
    assert hasattr(role, "nama_role")
    descriptor = None
    for klass in role.__mro__:
        if "nama_role" in klass.__dict__:
            descriptor = klass.__dict__["nama_role"]
            break
    assert isinstance(descriptor, property)

def test_role_has_deskripsi_role():
    assert hasattr(role, "deskripsi_role")
    descriptor = None
    for klass in role.__mro__:
        if "deskripsi_role" in klass.__dict__:
            descriptor = klass.__dict__["deskripsi_role"]
            break
    assert isinstance(descriptor, property)

def test_role_has_id():
    assert hasattr(role, "id")
    descriptor = None
    for klass in role.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_pembeli1_is_not_abstract():
    assert not inspect.isabstract(pembeli1)


def test_pembeli1_constructor_exists():
    assert callable(pembeli1.__init__)


def test_pembeli1_constructor_args():
    sig = inspect.signature(pembeli1.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id_role" in params, "Missing parameter 'id_role'"
    assert "password" in params, "Missing parameter 'password'"
    assert "address" in params, "Missing parameter 'address'"
    assert "id" in params, "Missing parameter 'id'"
    assert "mail" in params, "Missing parameter 'mail'"
    assert "username" in params, "Missing parameter 'username'"

def test_pembeli1_has_name():
    assert hasattr(pembeli1, "name")
    descriptor = None
    for klass in pembeli1.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_pembeli1_has_id_role():
    assert hasattr(pembeli1, "id_role")
    descriptor = None
    for klass in pembeli1.__mro__:
        if "id_role" in klass.__dict__:
            descriptor = klass.__dict__["id_role"]
            break
    assert isinstance(descriptor, property)

def test_pembeli1_has_password():
    assert hasattr(pembeli1, "password")
    descriptor = None
    for klass in pembeli1.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_pembeli1_has_address():
    assert hasattr(pembeli1, "address")
    descriptor = None
    for klass in pembeli1.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_pembeli1_has_id():
    assert hasattr(pembeli1, "id")
    descriptor = None
    for klass in pembeli1.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_pembeli1_has_mail():
    assert hasattr(pembeli1, "mail")
    descriptor = None
    for klass in pembeli1.__mro__:
        if "mail" in klass.__dict__:
            descriptor = klass.__dict__["mail"]
            break
    assert isinstance(descriptor, property)

def test_pembeli1_has_username():
    assert hasattr(pembeli1, "username")
    descriptor = None
    for klass in pembeli1.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)



def test_vendor_is_not_abstract():
    assert not inspect.isabstract(vendor)


def test_vendor_constructor_exists():
    assert callable(vendor.__init__)


def test_vendor_constructor_args():
    sig = inspect.signature(vendor.__init__)
    params = list(sig.parameters.keys())
    assert "id_role" in params, "Missing parameter 'id_role'"
    assert "bank" in params, "Missing parameter 'bank'"
    assert "bussinessname" in params, "Missing parameter 'bussinessname'"
    assert "address" in params, "Missing parameter 'address'"
    assert "shippinginfo" in params, "Missing parameter 'shippinginfo'"
    assert "username" in params, "Missing parameter 'username'"
    assert "name" in params, "Missing parameter 'name'"
    assert "mail" in params, "Missing parameter 'mail'"
    assert "id" in params, "Missing parameter 'id'"
    assert "password" in params, "Missing parameter 'password'"

def test_vendor_has_id_role():
    assert hasattr(vendor, "id_role")
    descriptor = None
    for klass in vendor.__mro__:
        if "id_role" in klass.__dict__:
            descriptor = klass.__dict__["id_role"]
            break
    assert isinstance(descriptor, property)

def test_vendor_has_bank():
    assert hasattr(vendor, "bank")
    descriptor = None
    for klass in vendor.__mro__:
        if "bank" in klass.__dict__:
            descriptor = klass.__dict__["bank"]
            break
    assert isinstance(descriptor, property)

def test_vendor_has_bussinessname():
    assert hasattr(vendor, "bussinessname")
    descriptor = None
    for klass in vendor.__mro__:
        if "bussinessname" in klass.__dict__:
            descriptor = klass.__dict__["bussinessname"]
            break
    assert isinstance(descriptor, property)

def test_vendor_has_address():
    assert hasattr(vendor, "address")
    descriptor = None
    for klass in vendor.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_vendor_has_shippinginfo():
    assert hasattr(vendor, "shippinginfo")
    descriptor = None
    for klass in vendor.__mro__:
        if "shippinginfo" in klass.__dict__:
            descriptor = klass.__dict__["shippinginfo"]
            break
    assert isinstance(descriptor, property)

def test_vendor_has_username():
    assert hasattr(vendor, "username")
    descriptor = None
    for klass in vendor.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_vendor_has_name():
    assert hasattr(vendor, "name")
    descriptor = None
    for klass in vendor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_vendor_has_mail():
    assert hasattr(vendor, "mail")
    descriptor = None
    for klass in vendor.__mro__:
        if "mail" in klass.__dict__:
            descriptor = klass.__dict__["mail"]
            break
    assert isinstance(descriptor, property)

def test_vendor_has_id():
    assert hasattr(vendor, "id")
    descriptor = None
    for klass in vendor.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_vendor_has_password():
    assert hasattr(vendor, "password")
    descriptor = None
    for klass in vendor.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(user)


def test_user_constructor_exists():
    assert callable(user.__init__)


def test_user_constructor_args():
    sig = inspect.signature(user.__init__)
    params = list(sig.parameters.keys())
    assert "id_role" in params, "Missing parameter 'id_role'"
    assert "id_order" in params, "Missing parameter 'id_order'"
    assert "id_user" in params, "Missing parameter 'id_user'"

def test_user_has_id_role():
    assert hasattr(user, "id_role")
    descriptor = None
    for klass in user.__mro__:
        if "id_role" in klass.__dict__:
            descriptor = klass.__dict__["id_role"]
            break
    assert isinstance(descriptor, property)

def test_user_has_id_order():
    assert hasattr(user, "id_order")
    descriptor = None
    for klass in user.__mro__:
        if "id_order" in klass.__dict__:
            descriptor = klass.__dict__["id_order"]
            break
    assert isinstance(descriptor, property)

def test_user_has_id_user():
    assert hasattr(user, "id_user")
    descriptor = None
    for klass in user.__mro__:
        if "id_user" in klass.__dict__:
            descriptor = klass.__dict__["id_user"]
            break
    assert isinstance(descriptor, property)



def test_kategori_is_not_abstract():
    assert not inspect.isabstract(kategori)


def test_kategori_constructor_exists():
    assert callable(kategori.__init__)


def test_kategori_constructor_args():
    sig = inspect.signature(kategori.__init__)
    params = list(sig.parameters.keys())
    assert "nama_kategori" in params, "Missing parameter 'nama_kategori'"
    assert "id" in params, "Missing parameter 'id'"
    assert "deskripsi_kategori" in params, "Missing parameter 'deskripsi_kategori'"

def test_kategori_has_nama_kategori():
    assert hasattr(kategori, "nama_kategori")
    descriptor = None
    for klass in kategori.__mro__:
        if "nama_kategori" in klass.__dict__:
            descriptor = klass.__dict__["nama_kategori"]
            break
    assert isinstance(descriptor, property)

def test_kategori_has_id():
    assert hasattr(kategori, "id")
    descriptor = None
    for klass in kategori.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_kategori_has_deskripsi_kategori():
    assert hasattr(kategori, "deskripsi_kategori")
    descriptor = None
    for klass in kategori.__mro__:
        if "deskripsi_kategori" in klass.__dict__:
            descriptor = klass.__dict__["deskripsi_kategori"]
            break
    assert isinstance(descriptor, property)



def test_barang_is_not_abstract():
    assert not inspect.isabstract(barang)


def test_barang_constructor_exists():
    assert callable(barang.__init__)


def test_barang_constructor_args():
    sig = inspect.signature(barang.__init__)
    params = list(sig.parameters.keys())
    assert "harga_barang" in params, "Missing parameter 'harga_barang'"
    assert "id_kategori" in params, "Missing parameter 'id_kategori'"
    assert "deskripsi_barang" in params, "Missing parameter 'deskripsi_barang'"
    assert "nama_barang" in params, "Missing parameter 'nama_barang'"
    assert "id" in params, "Missing parameter 'id'"

def test_barang_has_harga_barang():
    assert hasattr(barang, "harga_barang")
    descriptor = None
    for klass in barang.__mro__:
        if "harga_barang" in klass.__dict__:
            descriptor = klass.__dict__["harga_barang"]
            break
    assert isinstance(descriptor, property)

def test_barang_has_id_kategori():
    assert hasattr(barang, "id_kategori")
    descriptor = None
    for klass in barang.__mro__:
        if "id_kategori" in klass.__dict__:
            descriptor = klass.__dict__["id_kategori"]
            break
    assert isinstance(descriptor, property)

def test_barang_has_deskripsi_barang():
    assert hasattr(barang, "deskripsi_barang")
    descriptor = None
    for klass in barang.__mro__:
        if "deskripsi_barang" in klass.__dict__:
            descriptor = klass.__dict__["deskripsi_barang"]
            break
    assert isinstance(descriptor, property)

def test_barang_has_nama_barang():
    assert hasattr(barang, "nama_barang")
    descriptor = None
    for klass in barang.__mro__:
        if "nama_barang" in klass.__dict__:
            descriptor = klass.__dict__["nama_barang"]
            break
    assert isinstance(descriptor, property)

def test_barang_has_id():
    assert hasattr(barang, "id")
    descriptor = None
    for klass in barang.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_penjual_is_not_abstract():
    assert not inspect.isabstract(penjual)


def test_penjual_constructor_exists():
    assert callable(penjual.__init__)


def test_penjual_constructor_args():
    sig = inspect.signature(penjual.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "bussinessname" in params, "Missing parameter 'bussinessname'"
    assert "bank" in params, "Missing parameter 'bank'"
    assert "shippinginfo" in params, "Missing parameter 'shippinginfo'"
    assert "name" in params, "Missing parameter 'name'"
    assert "mail" in params, "Missing parameter 'mail'"
    assert "password" in params, "Missing parameter 'password'"
    assert "username" in params, "Missing parameter 'username'"
    assert "address" in params, "Missing parameter 'address'"

def test_penjual_has_id():
    assert hasattr(penjual, "id")
    descriptor = None
    for klass in penjual.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_penjual_has_bussinessname():
    assert hasattr(penjual, "bussinessname")
    descriptor = None
    for klass in penjual.__mro__:
        if "bussinessname" in klass.__dict__:
            descriptor = klass.__dict__["bussinessname"]
            break
    assert isinstance(descriptor, property)

def test_penjual_has_bank():
    assert hasattr(penjual, "bank")
    descriptor = None
    for klass in penjual.__mro__:
        if "bank" in klass.__dict__:
            descriptor = klass.__dict__["bank"]
            break
    assert isinstance(descriptor, property)

def test_penjual_has_shippinginfo():
    assert hasattr(penjual, "shippinginfo")
    descriptor = None
    for klass in penjual.__mro__:
        if "shippinginfo" in klass.__dict__:
            descriptor = klass.__dict__["shippinginfo"]
            break
    assert isinstance(descriptor, property)

def test_penjual_has_name():
    assert hasattr(penjual, "name")
    descriptor = None
    for klass in penjual.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_penjual_has_mail():
    assert hasattr(penjual, "mail")
    descriptor = None
    for klass in penjual.__mro__:
        if "mail" in klass.__dict__:
            descriptor = klass.__dict__["mail"]
            break
    assert isinstance(descriptor, property)

def test_penjual_has_password():
    assert hasattr(penjual, "password")
    descriptor = None
    for klass in penjual.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_penjual_has_username():
    assert hasattr(penjual, "username")
    descriptor = None
    for klass in penjual.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_penjual_has_address():
    assert hasattr(penjual, "address")
    descriptor = None
    for klass in penjual.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_kategori_is_not_abstract():
    assert not inspect.isabstract(Kategori)


def test_kategori_constructor_exists():
    assert callable(Kategori.__init__)


def test_kategori_constructor_args():
    sig = inspect.signature(Kategori.__init__)
    params = list(sig.parameters.keys())
    assert "productid" in params, "Missing parameter 'productid'"
    assert "desc" in params, "Missing parameter 'desc'"
    assert "name" in params, "Missing parameter 'name'"
    assert "idkategori" in params, "Missing parameter 'idkategori'"

def test_kategori_has_productid():
    assert hasattr(Kategori, "productid")
    descriptor = None
    for klass in Kategori.__mro__:
        if "productid" in klass.__dict__:
            descriptor = klass.__dict__["productid"]
            break
    assert isinstance(descriptor, property)

def test_kategori_has_desc():
    assert hasattr(Kategori, "desc")
    descriptor = None
    for klass in Kategori.__mro__:
        if "desc" in klass.__dict__:
            descriptor = klass.__dict__["desc"]
            break
    assert isinstance(descriptor, property)

def test_kategori_has_name():
    assert hasattr(Kategori, "name")
    descriptor = None
    for klass in Kategori.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_kategori_has_idkategori():
    assert hasattr(Kategori, "idkategori")
    descriptor = None
    for klass in Kategori.__mro__:
        if "idkategori" in klass.__dict__:
            descriptor = klass.__dict__["idkategori"]
            break
    assert isinstance(descriptor, property)



def test_produk_is_not_abstract():
    assert not inspect.isabstract(Produk)


def test_produk_constructor_exists():
    assert callable(Produk.__init__)


def test_produk_constructor_args():
    sig = inspect.signature(Produk.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "productid" in params, "Missing parameter 'productid'"
    assert "idkategori" in params, "Missing parameter 'idkategori'"
    assert "price" in params, "Missing parameter 'price'"
    assert "desc" in params, "Missing parameter 'desc'"

def test_produk_has_name():
    assert hasattr(Produk, "name")
    descriptor = None
    for klass in Produk.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_produk_has_productid():
    assert hasattr(Produk, "productid")
    descriptor = None
    for klass in Produk.__mro__:
        if "productid" in klass.__dict__:
            descriptor = klass.__dict__["productid"]
            break
    assert isinstance(descriptor, property)

def test_produk_has_idkategori():
    assert hasattr(Produk, "idkategori")
    descriptor = None
    for klass in Produk.__mro__:
        if "idkategori" in klass.__dict__:
            descriptor = klass.__dict__["idkategori"]
            break
    assert isinstance(descriptor, property)

def test_produk_has_price():
    assert hasattr(Produk, "price")
    descriptor = None
    for klass in Produk.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_produk_has_desc():
    assert hasattr(Produk, "desc")
    descriptor = None
    for klass in Produk.__mro__:
        if "desc" in klass.__dict__:
            descriptor = klass.__dict__["desc"]
            break
    assert isinstance(descriptor, property)



def test_shippinginfo_is_not_abstract():
    assert not inspect.isabstract(Shippinginfo)


def test_shippinginfo_constructor_exists():
    assert callable(Shippinginfo.__init__)


def test_shippinginfo_constructor_args():
    sig = inspect.signature(Shippinginfo.__init__)
    params = list(sig.parameters.keys())
    assert "region" in params, "Missing parameter 'region'"
    assert "shippingid" in params, "Missing parameter 'shippingid'"
    assert "type" in params, "Missing parameter 'type'"
    assert "total" in params, "Missing parameter 'total'"
    assert "cost" in params, "Missing parameter 'cost'"

def test_shippinginfo_has_region():
    assert hasattr(Shippinginfo, "region")
    descriptor = None
    for klass in Shippinginfo.__mro__:
        if "region" in klass.__dict__:
            descriptor = klass.__dict__["region"]
            break
    assert isinstance(descriptor, property)

def test_shippinginfo_has_shippingid():
    assert hasattr(Shippinginfo, "shippingid")
    descriptor = None
    for klass in Shippinginfo.__mro__:
        if "shippingid" in klass.__dict__:
            descriptor = klass.__dict__["shippingid"]
            break
    assert isinstance(descriptor, property)

def test_shippinginfo_has_type():
    assert hasattr(Shippinginfo, "type")
    descriptor = None
    for klass in Shippinginfo.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_shippinginfo_has_total():
    assert hasattr(Shippinginfo, "total")
    descriptor = None
    for klass in Shippinginfo.__mro__:
        if "total" in klass.__dict__:
            descriptor = klass.__dict__["total"]
            break
    assert isinstance(descriptor, property)

def test_shippinginfo_has_cost():
    assert hasattr(Shippinginfo, "cost")
    descriptor = None
    for klass in Shippinginfo.__mro__:
        if "cost" in klass.__dict__:
            descriptor = klass.__dict__["cost"]
            break
    assert isinstance(descriptor, property)



def test_orderdetail_is_not_abstract():
    assert not inspect.isabstract(Orderdetail)


def test_orderdetail_constructor_exists():
    assert callable(Orderdetail.__init__)


def test_orderdetail_constructor_args():
    sig = inspect.signature(Orderdetail.__init__)
    params = list(sig.parameters.keys())
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "productid" in params, "Missing parameter 'productid'"
    assert "cost" in params, "Missing parameter 'cost'"
    assert "orderid" in params, "Missing parameter 'orderid'"
    assert "total" in params, "Missing parameter 'total'"

def test_orderdetail_has_quantity():
    assert hasattr(Orderdetail, "quantity")
    descriptor = None
    for klass in Orderdetail.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_orderdetail_has_productid():
    assert hasattr(Orderdetail, "productid")
    descriptor = None
    for klass in Orderdetail.__mro__:
        if "productid" in klass.__dict__:
            descriptor = klass.__dict__["productid"]
            break
    assert isinstance(descriptor, property)

def test_orderdetail_has_cost():
    assert hasattr(Orderdetail, "cost")
    descriptor = None
    for klass in Orderdetail.__mro__:
        if "cost" in klass.__dict__:
            descriptor = klass.__dict__["cost"]
            break
    assert isinstance(descriptor, property)

def test_orderdetail_has_orderid():
    assert hasattr(Orderdetail, "orderid")
    descriptor = None
    for klass in Orderdetail.__mro__:
        if "orderid" in klass.__dict__:
            descriptor = klass.__dict__["orderid"]
            break
    assert isinstance(descriptor, property)

def test_orderdetail_has_total():
    assert hasattr(Orderdetail, "total")
    descriptor = None
    for klass in Orderdetail.__mro__:
        if "total" in klass.__dict__:
            descriptor = klass.__dict__["total"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "orderid" in params, "Missing parameter 'orderid'"
    assert "dateorder" in params, "Missing parameter 'dateorder'"
    assert "status" in params, "Missing parameter 'status'"
    assert "datedeliver" in params, "Missing parameter 'datedeliver'"
    assert "shippingid" in params, "Missing parameter 'shippingid'"
    assert "customerid" in params, "Missing parameter 'customerid'"

def test_order_has_orderid():
    assert hasattr(Order, "orderid")
    descriptor = None
    for klass in Order.__mro__:
        if "orderid" in klass.__dict__:
            descriptor = klass.__dict__["orderid"]
            break
    assert isinstance(descriptor, property)

def test_order_has_dateorder():
    assert hasattr(Order, "dateorder")
    descriptor = None
    for klass in Order.__mro__:
        if "dateorder" in klass.__dict__:
            descriptor = klass.__dict__["dateorder"]
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

def test_order_has_datedeliver():
    assert hasattr(Order, "datedeliver")
    descriptor = None
    for klass in Order.__mro__:
        if "datedeliver" in klass.__dict__:
            descriptor = klass.__dict__["datedeliver"]
            break
    assert isinstance(descriptor, property)

def test_order_has_shippingid():
    assert hasattr(Order, "shippingid")
    descriptor = None
    for klass in Order.__mro__:
        if "shippingid" in klass.__dict__:
            descriptor = klass.__dict__["shippingid"]
            break
    assert isinstance(descriptor, property)

def test_order_has_customerid():
    assert hasattr(Order, "customerid")
    descriptor = None
    for klass in Order.__mro__:
        if "customerid" in klass.__dict__:
            descriptor = klass.__dict__["customerid"]
            break
    assert isinstance(descriptor, property)



def test_cart_is_not_abstract():
    assert not inspect.isabstract(Cart)


def test_cart_constructor_exists():
    assert callable(Cart.__init__)


def test_cart_constructor_args():
    sig = inspect.signature(Cart.__init__)
    params = list(sig.parameters.keys())
    assert "cartid" in params, "Missing parameter 'cartid'"
    assert "productid" in params, "Missing parameter 'productid'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "date" in params, "Missing parameter 'date'"

def test_cart_has_cartid():
    assert hasattr(Cart, "cartid")
    descriptor = None
    for klass in Cart.__mro__:
        if "cartid" in klass.__dict__:
            descriptor = klass.__dict__["cartid"]
            break
    assert isinstance(descriptor, property)

def test_cart_has_productid():
    assert hasattr(Cart, "productid")
    descriptor = None
    for klass in Cart.__mro__:
        if "productid" in klass.__dict__:
            descriptor = klass.__dict__["productid"]
            break
    assert isinstance(descriptor, property)

def test_cart_has_quantity():
    assert hasattr(Cart, "quantity")
    descriptor = None
    for klass in Cart.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_cart_has_date():
    assert hasattr(Cart, "date")
    descriptor = None
    for klass in Cart.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_pembeli_is_not_abstract():
    assert not inspect.isabstract(pembeli)


def test_pembeli_constructor_exists():
    assert callable(pembeli.__init__)


def test_pembeli_constructor_args():
    sig = inspect.signature(pembeli.__init__)
    params = list(sig.parameters.keys())
    assert "mail" in params, "Missing parameter 'mail'"
    assert "shippinginfo" in params, "Missing parameter 'shippinginfo'"
    assert "id" in params, "Missing parameter 'id'"
    assert "address" in params, "Missing parameter 'address'"
    assert "name" in params, "Missing parameter 'name'"
    assert "password" in params, "Missing parameter 'password'"
    assert "username" in params, "Missing parameter 'username'"

def test_pembeli_has_mail():
    assert hasattr(pembeli, "mail")
    descriptor = None
    for klass in pembeli.__mro__:
        if "mail" in klass.__dict__:
            descriptor = klass.__dict__["mail"]
            break
    assert isinstance(descriptor, property)

def test_pembeli_has_shippinginfo():
    assert hasattr(pembeli, "shippinginfo")
    descriptor = None
    for klass in pembeli.__mro__:
        if "shippinginfo" in klass.__dict__:
            descriptor = klass.__dict__["shippinginfo"]
            break
    assert isinstance(descriptor, property)

def test_pembeli_has_id():
    assert hasattr(pembeli, "id")
    descriptor = None
    for klass in pembeli.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_pembeli_has_address():
    assert hasattr(pembeli, "address")
    descriptor = None
    for klass in pembeli.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_pembeli_has_name():
    assert hasattr(pembeli, "name")
    descriptor = None
    for klass in pembeli.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_pembeli_has_password():
    assert hasattr(pembeli, "password")
    descriptor = None
    for klass in pembeli.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_pembeli_has_username():
    assert hasattr(pembeli, "username")
    descriptor = None
    for klass in pembeli.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "mail" in params, "Missing parameter 'mail'"
    assert "name" in params, "Missing parameter 'name'"

def test_admin_has_mail():
    assert hasattr(Admin, "mail")
    descriptor = None
    for klass in Admin.__mro__:
        if "mail" in klass.__dict__:
            descriptor = klass.__dict__["mail"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_name():
    assert hasattr(Admin, "name")
    descriptor = None
    for klass in Admin.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "id" in params, "Missing parameter 'id'"

def test_user_has_password():
    assert hasattr(User, "password")
    descriptor = None
    for klass in User.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_user_has_id():
    assert hasattr(User, "id")
    descriptor = None
    for klass in User.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
admin_strategy = st.builds(
    admin,
    password=
        safe_text,
    username=
        safe_text,
    id=
        st.integers()
)
orderdetail_strategy = st.builds(
    orderdetail,
    order_id=
        st.integers(),
    total=
        safe_text,
    barang_id=
        st.integers()
)
order_strategy = st.builds(
    order,
    status=
        safe_text,
    dateorder=
        safe_text,
    id_user=
        st.integers(),
    order_id=
        st.integers()
)
role_strategy = st.builds(
    role,
    nama_role=
        safe_text,
    deskripsi_role=
        safe_text,
    id=
        st.integers()
)
pembeli1_strategy = st.builds(
    pembeli1,
    name=
        safe_text,
    id_role=
        st.integers(),
    password=
        safe_text,
    address=
        safe_text,
    id=
        st.integers(),
    mail=
        safe_text,
    username=
        safe_text
)
vendor_strategy = st.builds(
    vendor,
    id_role=
        st.integers(),
    bank=
        safe_text,
    bussinessname=
        safe_text,
    address=
        safe_text,
    shippinginfo=
        safe_text,
    username=
        safe_text,
    name=
        safe_text,
    mail=
        safe_text,
    id=
        st.integers(),
    password=
        safe_text
)
user_strategy = st.builds(
    user,
    id_role=
        st.integers(),
    id_order=
        st.integers(),
    id_user=
        st.integers()
)
kategori_strategy = st.builds(
    kategori,
    nama_kategori=
        safe_text,
    id=
        st.integers(),
    deskripsi_kategori=
        safe_text
)
barang_strategy = st.builds(
    barang,
    harga_barang=
        st.integers(),
    id_kategori=
        st.integers(),
    deskripsi_barang=
        safe_text,
    nama_barang=
        safe_text,
    id=
        st.integers()
)
penjual_strategy = st.builds(
    penjual,
    id=
        safe_text,
    bussinessname=
        safe_text,
    bank=
        safe_text,
    shippinginfo=
        safe_text,
    name=
        safe_text,
    mail=
        safe_text,
    password=
        safe_text,
    username=
        safe_text,
    address=
        safe_text
)
Kategori_strategy = st.builds(
    Kategori,
    productid=
        safe_text,
    desc=
        safe_text,
    name=
        safe_text,
    idkategori=
        safe_text
)
Produk_strategy = st.builds(
    Produk,
    name=
        safe_text,
    productid=
        safe_text,
    idkategori=
        safe_text,
    price=
        safe_text,
    desc=
        safe_text
)
Shippinginfo_strategy = st.builds(
    Shippinginfo,
    region=
        safe_text,
    shippingid=
        safe_text,
    type=
        safe_text,
    total=
        safe_text,
    cost=
        safe_text
)
Orderdetail_strategy = st.builds(
    Orderdetail,
    quantity=
        safe_text,
    productid=
        safe_text,
    cost=
        safe_text,
    orderid=
        safe_text,
    total=
        safe_text
)
Order_strategy = st.builds(
    Order,
    orderid=
        safe_text,
    dateorder=
        safe_text,
    status=
        safe_text,
    datedeliver=
        safe_text,
    shippingid=
        safe_text,
    customerid=
        safe_text
)
Cart_strategy = st.builds(
    Cart,
    cartid=
        safe_text,
    productid=
        safe_text,
    quantity=
        safe_text,
    date=
        safe_text
)
pembeli_strategy = st.builds(
    pembeli,
    mail=
        safe_text,
    shippinginfo=
        safe_text,
    id=
        safe_text,
    address=
        safe_text,
    name=
        safe_text,
    password=
        safe_text,
    username=
        safe_text
)
Admin_strategy = st.builds(
    Admin,
    mail=
        safe_text,
    name=
        safe_text
)
User_strategy = st.builds(
    User,
    password=
        safe_text,
    id=
        safe_text
)

@given(instance=admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, admin)



@given(instance=admin_strategy)
def test_admin_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=admin_strategy)
def test_admin_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=admin_strategy)
def test_admin_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=orderdetail_strategy)
@settings(max_examples=50)
def test_orderdetail_instantiation(instance):
    assert isinstance(instance, orderdetail)



@given(instance=orderdetail_strategy)
def test_orderdetail_order_id_setter(instance):
    original = instance.order_id
    instance.order_id = original
    assert instance.order_id == original



@given(instance=orderdetail_strategy)
def test_orderdetail_total_setter(instance):
    original = instance.total
    instance.total = original
    assert instance.total == original



@given(instance=orderdetail_strategy)
def test_orderdetail_barang_id_setter(instance):
    original = instance.barang_id
    instance.barang_id = original
    assert instance.barang_id == original

@given(instance=order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, order)



@given(instance=order_strategy)
def test_order_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=order_strategy)
def test_order_dateorder_setter(instance):
    original = instance.dateorder
    instance.dateorder = original
    assert instance.dateorder == original



@given(instance=order_strategy)
def test_order_id_user_setter(instance):
    original = instance.id_user
    instance.id_user = original
    assert instance.id_user == original



@given(instance=order_strategy)
def test_order_order_id_setter(instance):
    original = instance.order_id
    instance.order_id = original
    assert instance.order_id == original

@given(instance=role_strategy)
@settings(max_examples=50)
def test_role_instantiation(instance):
    assert isinstance(instance, role)



@given(instance=role_strategy)
def test_role_nama_role_setter(instance):
    original = instance.nama_role
    instance.nama_role = original
    assert instance.nama_role == original



@given(instance=role_strategy)
def test_role_deskripsi_role_setter(instance):
    original = instance.deskripsi_role
    instance.deskripsi_role = original
    assert instance.deskripsi_role == original



@given(instance=role_strategy)
def test_role_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=pembeli1_strategy)
@settings(max_examples=50)
def test_pembeli1_instantiation(instance):
    assert isinstance(instance, pembeli1)



@given(instance=pembeli1_strategy)
def test_pembeli1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=pembeli1_strategy)
def test_pembeli1_id_role_setter(instance):
    original = instance.id_role
    instance.id_role = original
    assert instance.id_role == original



@given(instance=pembeli1_strategy)
def test_pembeli1_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=pembeli1_strategy)
def test_pembeli1_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=pembeli1_strategy)
def test_pembeli1_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=pembeli1_strategy)
def test_pembeli1_mail_setter(instance):
    original = instance.mail
    instance.mail = original
    assert instance.mail == original



@given(instance=pembeli1_strategy)
def test_pembeli1_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original

@given(instance=vendor_strategy)
@settings(max_examples=50)
def test_vendor_instantiation(instance):
    assert isinstance(instance, vendor)



@given(instance=vendor_strategy)
def test_vendor_id_role_setter(instance):
    original = instance.id_role
    instance.id_role = original
    assert instance.id_role == original



@given(instance=vendor_strategy)
def test_vendor_bank_setter(instance):
    original = instance.bank
    instance.bank = original
    assert instance.bank == original



@given(instance=vendor_strategy)
def test_vendor_bussinessname_setter(instance):
    original = instance.bussinessname
    instance.bussinessname = original
    assert instance.bussinessname == original



@given(instance=vendor_strategy)
def test_vendor_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=vendor_strategy)
def test_vendor_shippinginfo_setter(instance):
    original = instance.shippinginfo
    instance.shippinginfo = original
    assert instance.shippinginfo == original



@given(instance=vendor_strategy)
def test_vendor_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=vendor_strategy)
def test_vendor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=vendor_strategy)
def test_vendor_mail_setter(instance):
    original = instance.mail
    instance.mail = original
    assert instance.mail == original



@given(instance=vendor_strategy)
def test_vendor_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=vendor_strategy)
def test_vendor_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=user_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, user)



@given(instance=user_strategy)
def test_user_id_role_setter(instance):
    original = instance.id_role
    instance.id_role = original
    assert instance.id_role == original



@given(instance=user_strategy)
def test_user_id_order_setter(instance):
    original = instance.id_order
    instance.id_order = original
    assert instance.id_order == original



@given(instance=user_strategy)
def test_user_id_user_setter(instance):
    original = instance.id_user
    instance.id_user = original
    assert instance.id_user == original

@given(instance=kategori_strategy)
@settings(max_examples=50)
def test_kategori_instantiation(instance):
    assert isinstance(instance, kategori)



@given(instance=kategori_strategy)
def test_kategori_nama_kategori_setter(instance):
    original = instance.nama_kategori
    instance.nama_kategori = original
    assert instance.nama_kategori == original



@given(instance=kategori_strategy)
def test_kategori_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=kategori_strategy)
def test_kategori_deskripsi_kategori_setter(instance):
    original = instance.deskripsi_kategori
    instance.deskripsi_kategori = original
    assert instance.deskripsi_kategori == original

@given(instance=barang_strategy)
@settings(max_examples=50)
def test_barang_instantiation(instance):
    assert isinstance(instance, barang)



@given(instance=barang_strategy)
def test_barang_harga_barang_setter(instance):
    original = instance.harga_barang
    instance.harga_barang = original
    assert instance.harga_barang == original



@given(instance=barang_strategy)
def test_barang_id_kategori_setter(instance):
    original = instance.id_kategori
    instance.id_kategori = original
    assert instance.id_kategori == original



@given(instance=barang_strategy)
def test_barang_deskripsi_barang_setter(instance):
    original = instance.deskripsi_barang
    instance.deskripsi_barang = original
    assert instance.deskripsi_barang == original



@given(instance=barang_strategy)
def test_barang_nama_barang_setter(instance):
    original = instance.nama_barang
    instance.nama_barang = original
    assert instance.nama_barang == original



@given(instance=barang_strategy)
def test_barang_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=penjual_strategy)
@settings(max_examples=50)
def test_penjual_instantiation(instance):
    assert isinstance(instance, penjual)



@given(instance=penjual_strategy)
def test_penjual_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=penjual_strategy)
def test_penjual_bussinessname_setter(instance):
    original = instance.bussinessname
    instance.bussinessname = original
    assert instance.bussinessname == original



@given(instance=penjual_strategy)
def test_penjual_bank_setter(instance):
    original = instance.bank
    instance.bank = original
    assert instance.bank == original



@given(instance=penjual_strategy)
def test_penjual_shippinginfo_setter(instance):
    original = instance.shippinginfo
    instance.shippinginfo = original
    assert instance.shippinginfo == original



@given(instance=penjual_strategy)
def test_penjual_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=penjual_strategy)
def test_penjual_mail_setter(instance):
    original = instance.mail
    instance.mail = original
    assert instance.mail == original



@given(instance=penjual_strategy)
def test_penjual_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=penjual_strategy)
def test_penjual_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=penjual_strategy)
def test_penjual_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=Kategori_strategy)
@settings(max_examples=50)
def test_kategori_instantiation(instance):
    assert isinstance(instance, Kategori)



@given(instance=Kategori_strategy)
def test_kategori_productid_setter(instance):
    original = instance.productid
    instance.productid = original
    assert instance.productid == original



@given(instance=Kategori_strategy)
def test_kategori_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original



@given(instance=Kategori_strategy)
def test_kategori_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Kategori_strategy)
def test_kategori_idkategori_setter(instance):
    original = instance.idkategori
    instance.idkategori = original
    assert instance.idkategori == original

@given(instance=Produk_strategy)
@settings(max_examples=50)
def test_produk_instantiation(instance):
    assert isinstance(instance, Produk)



@given(instance=Produk_strategy)
def test_produk_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Produk_strategy)
def test_produk_productid_setter(instance):
    original = instance.productid
    instance.productid = original
    assert instance.productid == original



@given(instance=Produk_strategy)
def test_produk_idkategori_setter(instance):
    original = instance.idkategori
    instance.idkategori = original
    assert instance.idkategori == original



@given(instance=Produk_strategy)
def test_produk_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Produk_strategy)
def test_produk_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original

@given(instance=Shippinginfo_strategy)
@settings(max_examples=50)
def test_shippinginfo_instantiation(instance):
    assert isinstance(instance, Shippinginfo)



@given(instance=Shippinginfo_strategy)
def test_shippinginfo_region_setter(instance):
    original = instance.region
    instance.region = original
    assert instance.region == original



@given(instance=Shippinginfo_strategy)
def test_shippinginfo_shippingid_setter(instance):
    original = instance.shippingid
    instance.shippingid = original
    assert instance.shippingid == original



@given(instance=Shippinginfo_strategy)
def test_shippinginfo_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Shippinginfo_strategy)
def test_shippinginfo_total_setter(instance):
    original = instance.total
    instance.total = original
    assert instance.total == original



@given(instance=Shippinginfo_strategy)
def test_shippinginfo_cost_setter(instance):
    original = instance.cost
    instance.cost = original
    assert instance.cost == original

@given(instance=Orderdetail_strategy)
@settings(max_examples=50)
def test_orderdetail_instantiation(instance):
    assert isinstance(instance, Orderdetail)



@given(instance=Orderdetail_strategy)
def test_orderdetail_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=Orderdetail_strategy)
def test_orderdetail_productid_setter(instance):
    original = instance.productid
    instance.productid = original
    assert instance.productid == original



@given(instance=Orderdetail_strategy)
def test_orderdetail_cost_setter(instance):
    original = instance.cost
    instance.cost = original
    assert instance.cost == original



@given(instance=Orderdetail_strategy)
def test_orderdetail_orderid_setter(instance):
    original = instance.orderid
    instance.orderid = original
    assert instance.orderid == original



@given(instance=Orderdetail_strategy)
def test_orderdetail_total_setter(instance):
    original = instance.total
    instance.total = original
    assert instance.total == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_orderid_setter(instance):
    original = instance.orderid
    instance.orderid = original
    assert instance.orderid == original



@given(instance=Order_strategy)
def test_order_dateorder_setter(instance):
    original = instance.dateorder
    instance.dateorder = original
    assert instance.dateorder == original



@given(instance=Order_strategy)
def test_order_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Order_strategy)
def test_order_datedeliver_setter(instance):
    original = instance.datedeliver
    instance.datedeliver = original
    assert instance.datedeliver == original



@given(instance=Order_strategy)
def test_order_shippingid_setter(instance):
    original = instance.shippingid
    instance.shippingid = original
    assert instance.shippingid == original



@given(instance=Order_strategy)
def test_order_customerid_setter(instance):
    original = instance.customerid
    instance.customerid = original
    assert instance.customerid == original

@given(instance=Cart_strategy)
@settings(max_examples=50)
def test_cart_instantiation(instance):
    assert isinstance(instance, Cart)



@given(instance=Cart_strategy)
def test_cart_cartid_setter(instance):
    original = instance.cartid
    instance.cartid = original
    assert instance.cartid == original



@given(instance=Cart_strategy)
def test_cart_productid_setter(instance):
    original = instance.productid
    instance.productid = original
    assert instance.productid == original



@given(instance=Cart_strategy)
def test_cart_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=Cart_strategy)
def test_cart_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=pembeli_strategy)
@settings(max_examples=50)
def test_pembeli_instantiation(instance):
    assert isinstance(instance, pembeli)



@given(instance=pembeli_strategy)
def test_pembeli_mail_setter(instance):
    original = instance.mail
    instance.mail = original
    assert instance.mail == original



@given(instance=pembeli_strategy)
def test_pembeli_shippinginfo_setter(instance):
    original = instance.shippinginfo
    instance.shippinginfo = original
    assert instance.shippinginfo == original



@given(instance=pembeli_strategy)
def test_pembeli_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=pembeli_strategy)
def test_pembeli_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=pembeli_strategy)
def test_pembeli_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=pembeli_strategy)
def test_pembeli_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=pembeli_strategy)
def test_pembeli_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)



@given(instance=Admin_strategy)
def test_admin_mail_setter(instance):
    original = instance.mail
    instance.mail = original
    assert instance.mail == original



@given(instance=Admin_strategy)
def test_admin_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=User_strategy)
def test_user_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
