import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Admin,
    DetailOrder,
    Orders,
    DetailCart,
    Cart,
    Inventory,
    Size,
    Color,
    Banner,
    Gallery,
    Type,
    Collection,
    Products,
    User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "UserName" in params, "Missing parameter 'UserName'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "AdminInfo" in params, "Missing parameter 'AdminInfo'"
    assert "Password" in params, "Missing parameter 'Password'"

def test_admin_has_UserName():
    assert hasattr(Admin, "UserName")
    descriptor = None
    for klass in Admin.__mro__:
        if "UserName" in klass.__dict__:
            descriptor = klass.__dict__["UserName"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_ID():
    assert hasattr(Admin, "ID")
    descriptor = None
    for klass in Admin.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_AdminInfo():
    assert hasattr(Admin, "AdminInfo")
    descriptor = None
    for klass in Admin.__mro__:
        if "AdminInfo" in klass.__dict__:
            descriptor = klass.__dict__["AdminInfo"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_Password():
    assert hasattr(Admin, "Password")
    descriptor = None
    for klass in Admin.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)



def test_detailorder_is_not_abstract():
    assert not inspect.isabstract(DetailOrder)


def test_detailorder_constructor_exists():
    assert callable(DetailOrder.__init__)


def test_detailorder_constructor_args():
    sig = inspect.signature(DetailOrder.__init__)
    params = list(sig.parameters.keys())
    assert "ProductID" in params, "Missing parameter 'ProductID'"
    assert "DetailOrderInfo" in params, "Missing parameter 'DetailOrderInfo'"
    assert "OrderID" in params, "Missing parameter 'OrderID'"
    assert "DetailOrderID" in params, "Missing parameter 'DetailOrderID'"

def test_detailorder_has_ProductID():
    assert hasattr(DetailOrder, "ProductID")
    descriptor = None
    for klass in DetailOrder.__mro__:
        if "ProductID" in klass.__dict__:
            descriptor = klass.__dict__["ProductID"]
            break
    assert isinstance(descriptor, property)

def test_detailorder_has_DetailOrderInfo():
    assert hasattr(DetailOrder, "DetailOrderInfo")
    descriptor = None
    for klass in DetailOrder.__mro__:
        if "DetailOrderInfo" in klass.__dict__:
            descriptor = klass.__dict__["DetailOrderInfo"]
            break
    assert isinstance(descriptor, property)

def test_detailorder_has_OrderID():
    assert hasattr(DetailOrder, "OrderID")
    descriptor = None
    for klass in DetailOrder.__mro__:
        if "OrderID" in klass.__dict__:
            descriptor = klass.__dict__["OrderID"]
            break
    assert isinstance(descriptor, property)

def test_detailorder_has_DetailOrderID():
    assert hasattr(DetailOrder, "DetailOrderID")
    descriptor = None
    for klass in DetailOrder.__mro__:
        if "DetailOrderID" in klass.__dict__:
            descriptor = klass.__dict__["DetailOrderID"]
            break
    assert isinstance(descriptor, property)



def test_orders_is_not_abstract():
    assert not inspect.isabstract(Orders)


def test_orders_constructor_exists():
    assert callable(Orders.__init__)


def test_orders_constructor_args():
    sig = inspect.signature(Orders.__init__)
    params = list(sig.parameters.keys())
    assert "OrderID" in params, "Missing parameter 'OrderID'"
    assert "DeliInfo" in params, "Missing parameter 'DeliInfo'"
    assert "OrderInfo" in params, "Missing parameter 'OrderInfo'"
    assert "UserID" in params, "Missing parameter 'UserID'"

def test_orders_has_OrderID():
    assert hasattr(Orders, "OrderID")
    descriptor = None
    for klass in Orders.__mro__:
        if "OrderID" in klass.__dict__:
            descriptor = klass.__dict__["OrderID"]
            break
    assert isinstance(descriptor, property)

def test_orders_has_DeliInfo():
    assert hasattr(Orders, "DeliInfo")
    descriptor = None
    for klass in Orders.__mro__:
        if "DeliInfo" in klass.__dict__:
            descriptor = klass.__dict__["DeliInfo"]
            break
    assert isinstance(descriptor, property)

def test_orders_has_OrderInfo():
    assert hasattr(Orders, "OrderInfo")
    descriptor = None
    for klass in Orders.__mro__:
        if "OrderInfo" in klass.__dict__:
            descriptor = klass.__dict__["OrderInfo"]
            break
    assert isinstance(descriptor, property)

def test_orders_has_UserID():
    assert hasattr(Orders, "UserID")
    descriptor = None
    for klass in Orders.__mro__:
        if "UserID" in klass.__dict__:
            descriptor = klass.__dict__["UserID"]
            break
    assert isinstance(descriptor, property)



def test_detailcart_is_not_abstract():
    assert not inspect.isabstract(DetailCart)


def test_detailcart_constructor_exists():
    assert callable(DetailCart.__init__)


def test_detailcart_constructor_args():
    sig = inspect.signature(DetailCart.__init__)
    params = list(sig.parameters.keys())
    assert "DetailCartID" in params, "Missing parameter 'DetailCartID'"
    assert "DetailCartInfo" in params, "Missing parameter 'DetailCartInfo'"
    assert "ProductID" in params, "Missing parameter 'ProductID'"
    assert "CartID" in params, "Missing parameter 'CartID'"

def test_detailcart_has_DetailCartID():
    assert hasattr(DetailCart, "DetailCartID")
    descriptor = None
    for klass in DetailCart.__mro__:
        if "DetailCartID" in klass.__dict__:
            descriptor = klass.__dict__["DetailCartID"]
            break
    assert isinstance(descriptor, property)

def test_detailcart_has_DetailCartInfo():
    assert hasattr(DetailCart, "DetailCartInfo")
    descriptor = None
    for klass in DetailCart.__mro__:
        if "DetailCartInfo" in klass.__dict__:
            descriptor = klass.__dict__["DetailCartInfo"]
            break
    assert isinstance(descriptor, property)

def test_detailcart_has_ProductID():
    assert hasattr(DetailCart, "ProductID")
    descriptor = None
    for klass in DetailCart.__mro__:
        if "ProductID" in klass.__dict__:
            descriptor = klass.__dict__["ProductID"]
            break
    assert isinstance(descriptor, property)

def test_detailcart_has_CartID():
    assert hasattr(DetailCart, "CartID")
    descriptor = None
    for klass in DetailCart.__mro__:
        if "CartID" in klass.__dict__:
            descriptor = klass.__dict__["CartID"]
            break
    assert isinstance(descriptor, property)



def test_cart_is_not_abstract():
    assert not inspect.isabstract(Cart)


def test_cart_constructor_exists():
    assert callable(Cart.__init__)


def test_cart_constructor_args():
    sig = inspect.signature(Cart.__init__)
    params = list(sig.parameters.keys())
    assert "CartID" in params, "Missing parameter 'CartID'"
    assert "CartInfo" in params, "Missing parameter 'CartInfo'"

def test_cart_has_CartID():
    assert hasattr(Cart, "CartID")
    descriptor = None
    for klass in Cart.__mro__:
        if "CartID" in klass.__dict__:
            descriptor = klass.__dict__["CartID"]
            break
    assert isinstance(descriptor, property)

def test_cart_has_CartInfo():
    assert hasattr(Cart, "CartInfo")
    descriptor = None
    for klass in Cart.__mro__:
        if "CartInfo" in klass.__dict__:
            descriptor = klass.__dict__["CartInfo"]
            break
    assert isinstance(descriptor, property)



def test_inventory_is_not_abstract():
    assert not inspect.isabstract(Inventory)


def test_inventory_constructor_exists():
    assert callable(Inventory.__init__)


def test_inventory_constructor_args():
    sig = inspect.signature(Inventory.__init__)
    params = list(sig.parameters.keys())
    assert "ColorID" in params, "Missing parameter 'ColorID'"
    assert "ProductID" in params, "Missing parameter 'ProductID'"
    assert "SizeID" in params, "Missing parameter 'SizeID'"
    assert "InStock" in params, "Missing parameter 'InStock'"

def test_inventory_has_ColorID():
    assert hasattr(Inventory, "ColorID")
    descriptor = None
    for klass in Inventory.__mro__:
        if "ColorID" in klass.__dict__:
            descriptor = klass.__dict__["ColorID"]
            break
    assert isinstance(descriptor, property)

def test_inventory_has_ProductID():
    assert hasattr(Inventory, "ProductID")
    descriptor = None
    for klass in Inventory.__mro__:
        if "ProductID" in klass.__dict__:
            descriptor = klass.__dict__["ProductID"]
            break
    assert isinstance(descriptor, property)

def test_inventory_has_SizeID():
    assert hasattr(Inventory, "SizeID")
    descriptor = None
    for klass in Inventory.__mro__:
        if "SizeID" in klass.__dict__:
            descriptor = klass.__dict__["SizeID"]
            break
    assert isinstance(descriptor, property)

def test_inventory_has_InStock():
    assert hasattr(Inventory, "InStock")
    descriptor = None
    for klass in Inventory.__mro__:
        if "InStock" in klass.__dict__:
            descriptor = klass.__dict__["InStock"]
            break
    assert isinstance(descriptor, property)



def test_size_is_not_abstract():
    assert not inspect.isabstract(Size)


def test_size_constructor_exists():
    assert callable(Size.__init__)


def test_size_constructor_args():
    sig = inspect.signature(Size.__init__)
    params = list(sig.parameters.keys())
    assert "SizeID" in params, "Missing parameter 'SizeID'"
    assert "SizeName" in params, "Missing parameter 'SizeName'"

def test_size_has_SizeID():
    assert hasattr(Size, "SizeID")
    descriptor = None
    for klass in Size.__mro__:
        if "SizeID" in klass.__dict__:
            descriptor = klass.__dict__["SizeID"]
            break
    assert isinstance(descriptor, property)

def test_size_has_SizeName():
    assert hasattr(Size, "SizeName")
    descriptor = None
    for klass in Size.__mro__:
        if "SizeName" in klass.__dict__:
            descriptor = klass.__dict__["SizeName"]
            break
    assert isinstance(descriptor, property)



def test_color_is_not_abstract():
    assert not inspect.isabstract(Color)


def test_color_constructor_exists():
    assert callable(Color.__init__)


def test_color_constructor_args():
    sig = inspect.signature(Color.__init__)
    params = list(sig.parameters.keys())
    assert "ColorName" in params, "Missing parameter 'ColorName'"
    assert "ColorID" in params, "Missing parameter 'ColorID'"

def test_color_has_ColorName():
    assert hasattr(Color, "ColorName")
    descriptor = None
    for klass in Color.__mro__:
        if "ColorName" in klass.__dict__:
            descriptor = klass.__dict__["ColorName"]
            break
    assert isinstance(descriptor, property)

def test_color_has_ColorID():
    assert hasattr(Color, "ColorID")
    descriptor = None
    for klass in Color.__mro__:
        if "ColorID" in klass.__dict__:
            descriptor = klass.__dict__["ColorID"]
            break
    assert isinstance(descriptor, property)



def test_banner_is_not_abstract():
    assert not inspect.isabstract(Banner)


def test_banner_constructor_exists():
    assert callable(Banner.__init__)


def test_banner_constructor_args():
    sig = inspect.signature(Banner.__init__)
    params = list(sig.parameters.keys())
    assert "BannerInfo" in params, "Missing parameter 'BannerInfo'"
    assert "IsShow" in params, "Missing parameter 'IsShow'"
    assert "DateStart" in params, "Missing parameter 'DateStart'"
    assert "Image" in params, "Missing parameter 'Image'"
    assert "BannerID" in params, "Missing parameter 'BannerID'"
    assert "DateEnd" in params, "Missing parameter 'DateEnd'"

def test_banner_has_BannerInfo():
    assert hasattr(Banner, "BannerInfo")
    descriptor = None
    for klass in Banner.__mro__:
        if "BannerInfo" in klass.__dict__:
            descriptor = klass.__dict__["BannerInfo"]
            break
    assert isinstance(descriptor, property)

def test_banner_has_IsShow():
    assert hasattr(Banner, "IsShow")
    descriptor = None
    for klass in Banner.__mro__:
        if "IsShow" in klass.__dict__:
            descriptor = klass.__dict__["IsShow"]
            break
    assert isinstance(descriptor, property)

def test_banner_has_DateStart():
    assert hasattr(Banner, "DateStart")
    descriptor = None
    for klass in Banner.__mro__:
        if "DateStart" in klass.__dict__:
            descriptor = klass.__dict__["DateStart"]
            break
    assert isinstance(descriptor, property)

def test_banner_has_Image():
    assert hasattr(Banner, "Image")
    descriptor = None
    for klass in Banner.__mro__:
        if "Image" in klass.__dict__:
            descriptor = klass.__dict__["Image"]
            break
    assert isinstance(descriptor, property)

def test_banner_has_BannerID():
    assert hasattr(Banner, "BannerID")
    descriptor = None
    for klass in Banner.__mro__:
        if "BannerID" in klass.__dict__:
            descriptor = klass.__dict__["BannerID"]
            break
    assert isinstance(descriptor, property)

def test_banner_has_DateEnd():
    assert hasattr(Banner, "DateEnd")
    descriptor = None
    for klass in Banner.__mro__:
        if "DateEnd" in klass.__dict__:
            descriptor = klass.__dict__["DateEnd"]
            break
    assert isinstance(descriptor, property)



def test_gallery_is_not_abstract():
    assert not inspect.isabstract(Gallery)


def test_gallery_constructor_exists():
    assert callable(Gallery.__init__)


def test_gallery_constructor_args():
    sig = inspect.signature(Gallery.__init__)
    params = list(sig.parameters.keys())
    assert "ProductID" in params, "Missing parameter 'ProductID'"
    assert "GalleryName" in params, "Missing parameter 'GalleryName'"
    assert "GalleryID" in params, "Missing parameter 'GalleryID'"
    assert "DateCreate" in params, "Missing parameter 'DateCreate'"
    assert "Image" in params, "Missing parameter 'Image'"

def test_gallery_has_ProductID():
    assert hasattr(Gallery, "ProductID")
    descriptor = None
    for klass in Gallery.__mro__:
        if "ProductID" in klass.__dict__:
            descriptor = klass.__dict__["ProductID"]
            break
    assert isinstance(descriptor, property)

def test_gallery_has_GalleryName():
    assert hasattr(Gallery, "GalleryName")
    descriptor = None
    for klass in Gallery.__mro__:
        if "GalleryName" in klass.__dict__:
            descriptor = klass.__dict__["GalleryName"]
            break
    assert isinstance(descriptor, property)

def test_gallery_has_GalleryID():
    assert hasattr(Gallery, "GalleryID")
    descriptor = None
    for klass in Gallery.__mro__:
        if "GalleryID" in klass.__dict__:
            descriptor = klass.__dict__["GalleryID"]
            break
    assert isinstance(descriptor, property)

def test_gallery_has_DateCreate():
    assert hasattr(Gallery, "DateCreate")
    descriptor = None
    for klass in Gallery.__mro__:
        if "DateCreate" in klass.__dict__:
            descriptor = klass.__dict__["DateCreate"]
            break
    assert isinstance(descriptor, property)

def test_gallery_has_Image():
    assert hasattr(Gallery, "Image")
    descriptor = None
    for klass in Gallery.__mro__:
        if "Image" in klass.__dict__:
            descriptor = klass.__dict__["Image"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())
    assert "TypeID" in params, "Missing parameter 'TypeID'"
    assert "TypeName" in params, "Missing parameter 'TypeName'"

def test_type_has_TypeID():
    assert hasattr(Type, "TypeID")
    descriptor = None
    for klass in Type.__mro__:
        if "TypeID" in klass.__dict__:
            descriptor = klass.__dict__["TypeID"]
            break
    assert isinstance(descriptor, property)

def test_type_has_TypeName():
    assert hasattr(Type, "TypeName")
    descriptor = None
    for klass in Type.__mro__:
        if "TypeName" in klass.__dict__:
            descriptor = klass.__dict__["TypeName"]
            break
    assert isinstance(descriptor, property)



def test_collection_is_not_abstract():
    assert not inspect.isabstract(Collection)


def test_collection_constructor_exists():
    assert callable(Collection.__init__)


def test_collection_constructor_args():
    sig = inspect.signature(Collection.__init__)
    params = list(sig.parameters.keys())
    assert "CollectionName" in params, "Missing parameter 'CollectionName'"
    assert "CollectionID" in params, "Missing parameter 'CollectionID'"

def test_collection_has_CollectionName():
    assert hasattr(Collection, "CollectionName")
    descriptor = None
    for klass in Collection.__mro__:
        if "CollectionName" in klass.__dict__:
            descriptor = klass.__dict__["CollectionName"]
            break
    assert isinstance(descriptor, property)

def test_collection_has_CollectionID():
    assert hasattr(Collection, "CollectionID")
    descriptor = None
    for klass in Collection.__mro__:
        if "CollectionID" in klass.__dict__:
            descriptor = klass.__dict__["CollectionID"]
            break
    assert isinstance(descriptor, property)



def test_products_is_not_abstract():
    assert not inspect.isabstract(Products)


def test_products_constructor_exists():
    assert callable(Products.__init__)


def test_products_constructor_args():
    sig = inspect.signature(Products.__init__)
    params = list(sig.parameters.keys())
    assert "ProductID" in params, "Missing parameter 'ProductID'"
    assert "CollectionID" in params, "Missing parameter 'CollectionID'"
    assert "InStock" in params, "Missing parameter 'InStock'"
    assert "TypeID1" in params, "Missing parameter 'TypeID1'"
    assert "TypeID" in params, "Missing parameter 'TypeID'"
    assert "ProductInfo" in params, "Missing parameter 'ProductInfo'"
    assert "Index" in params, "Missing parameter 'Index'"
    assert "DateCreate" in params, "Missing parameter 'DateCreate'"

def test_products_has_ProductID():
    assert hasattr(Products, "ProductID")
    descriptor = None
    for klass in Products.__mro__:
        if "ProductID" in klass.__dict__:
            descriptor = klass.__dict__["ProductID"]
            break
    assert isinstance(descriptor, property)

def test_products_has_CollectionID():
    assert hasattr(Products, "CollectionID")
    descriptor = None
    for klass in Products.__mro__:
        if "CollectionID" in klass.__dict__:
            descriptor = klass.__dict__["CollectionID"]
            break
    assert isinstance(descriptor, property)

def test_products_has_InStock():
    assert hasattr(Products, "InStock")
    descriptor = None
    for klass in Products.__mro__:
        if "InStock" in klass.__dict__:
            descriptor = klass.__dict__["InStock"]
            break
    assert isinstance(descriptor, property)

def test_products_has_TypeID1():
    assert hasattr(Products, "TypeID1")
    descriptor = None
    for klass in Products.__mro__:
        if "TypeID1" in klass.__dict__:
            descriptor = klass.__dict__["TypeID1"]
            break
    assert isinstance(descriptor, property)

def test_products_has_TypeID():
    assert hasattr(Products, "TypeID")
    descriptor = None
    for klass in Products.__mro__:
        if "TypeID" in klass.__dict__:
            descriptor = klass.__dict__["TypeID"]
            break
    assert isinstance(descriptor, property)

def test_products_has_ProductInfo():
    assert hasattr(Products, "ProductInfo")
    descriptor = None
    for klass in Products.__mro__:
        if "ProductInfo" in klass.__dict__:
            descriptor = klass.__dict__["ProductInfo"]
            break
    assert isinstance(descriptor, property)

def test_products_has_Index():
    assert hasattr(Products, "Index")
    descriptor = None
    for klass in Products.__mro__:
        if "Index" in klass.__dict__:
            descriptor = klass.__dict__["Index"]
            break
    assert isinstance(descriptor, property)

def test_products_has_DateCreate():
    assert hasattr(Products, "DateCreate")
    descriptor = None
    for klass in Products.__mro__:
        if "DateCreate" in klass.__dict__:
            descriptor = klass.__dict__["DateCreate"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "UserName" in params, "Missing parameter 'UserName'"
    assert "Point" in params, "Missing parameter 'Point'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "UserInfo" in params, "Missing parameter 'UserInfo'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Phone" in params, "Missing parameter 'Phone'"

def test_user_has_UserName():
    assert hasattr(User, "UserName")
    descriptor = None
    for klass in User.__mro__:
        if "UserName" in klass.__dict__:
            descriptor = klass.__dict__["UserName"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Point():
    assert hasattr(User, "Point")
    descriptor = None
    for klass in User.__mro__:
        if "Point" in klass.__dict__:
            descriptor = klass.__dict__["Point"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Email():
    assert hasattr(User, "Email")
    descriptor = None
    for klass in User.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Password():
    assert hasattr(User, "Password")
    descriptor = None
    for klass in User.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_user_has_UserInfo():
    assert hasattr(User, "UserInfo")
    descriptor = None
    for klass in User.__mro__:
        if "UserInfo" in klass.__dict__:
            descriptor = klass.__dict__["UserInfo"]
            break
    assert isinstance(descriptor, property)

def test_user_has_ID():
    assert hasattr(User, "ID")
    descriptor = None
    for klass in User.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Phone():
    assert hasattr(User, "Phone")
    descriptor = None
    for klass in User.__mro__:
        if "Phone" in klass.__dict__:
            descriptor = klass.__dict__["Phone"]
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
Admin_strategy = st.builds(
    Admin,
    UserName=
        safe_text,
    ID=
        st.integers(),
    AdminInfo=
        safe_text,
    Password=
        safe_text
)
DetailOrder_strategy = st.builds(
    DetailOrder,
    ProductID=
        st.integers(),
    DetailOrderInfo=
        safe_text,
    OrderID=
        st.integers(),
    DetailOrderID=
        st.integers()
)
Orders_strategy = st.builds(
    Orders,
    OrderID=
        st.integers(),
    DeliInfo=
        safe_text,
    OrderInfo=
        safe_text,
    UserID=
        st.integers()
)
DetailCart_strategy = st.builds(
    DetailCart,
    DetailCartID=
        st.integers(),
    DetailCartInfo=
        safe_text,
    ProductID=
        st.integers(),
    CartID=
        st.integers()
)
Cart_strategy = st.builds(
    Cart,
    CartID=
        st.integers(),
    CartInfo=
        safe_text
)
Inventory_strategy = st.builds(
    Inventory,
    ColorID=
        st.integers(),
    ProductID=
        st.integers(),
    SizeID=
        st.integers(),
    InStock=
        st.integers()
)
Size_strategy = st.builds(
    Size,
    SizeID=
        st.integers(),
    SizeName=
        safe_text
)
Color_strategy = st.builds(
    Color,
    ColorName=
        safe_text,
    ColorID=
        safe_text
)
Banner_strategy = st.builds(
    Banner,
    BannerInfo=
        safe_text,
    IsShow=
        st.integers(),
    DateStart=
        safe_text,
    Image=
        safe_text,
    BannerID=
        st.integers(),
    DateEnd=
        safe_text
)
Gallery_strategy = st.builds(
    Gallery,
    ProductID=
        st.integers(),
    GalleryName=
        safe_text,
    GalleryID=
        st.integers(),
    DateCreate=
        safe_text,
    Image=
        safe_text
)
Type_strategy = st.builds(
    Type,
    TypeID=
        st.integers(),
    TypeName=
        safe_text
)
Collection_strategy = st.builds(
    Collection,
    CollectionName=
        safe_text,
    CollectionID=
        st.integers()
)
Products_strategy = st.builds(
    Products,
    ProductID=
        st.integers(),
    CollectionID=
        st.integers(),
    InStock=
        st.integers(),
    TypeID1=
        st.integers(),
    TypeID=
        st.integers(),
    ProductInfo=
        safe_text,
    Index=
        st.integers(),
    DateCreate=
        safe_text
)
User_strategy = st.builds(
    User,
    UserName=
        safe_text,
    Point=
        st.integers(),
    Email=
        safe_text,
    Password=
        safe_text,
    UserInfo=
        safe_text,
    ID=
        st.integers(),
    Phone=
        st.integers()
)

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)



@given(instance=Admin_strategy)
def test_admin_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original



@given(instance=Admin_strategy)
def test_admin_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Admin_strategy)
def test_admin_AdminInfo_setter(instance):
    original = instance.AdminInfo
    instance.AdminInfo = original
    assert instance.AdminInfo == original



@given(instance=Admin_strategy)
def test_admin_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original

@given(instance=DetailOrder_strategy)
@settings(max_examples=50)
def test_detailorder_instantiation(instance):
    assert isinstance(instance, DetailOrder)



@given(instance=DetailOrder_strategy)
def test_detailorder_ProductID_setter(instance):
    original = instance.ProductID
    instance.ProductID = original
    assert instance.ProductID == original



@given(instance=DetailOrder_strategy)
def test_detailorder_DetailOrderInfo_setter(instance):
    original = instance.DetailOrderInfo
    instance.DetailOrderInfo = original
    assert instance.DetailOrderInfo == original



@given(instance=DetailOrder_strategy)
def test_detailorder_OrderID_setter(instance):
    original = instance.OrderID
    instance.OrderID = original
    assert instance.OrderID == original



@given(instance=DetailOrder_strategy)
def test_detailorder_DetailOrderID_setter(instance):
    original = instance.DetailOrderID
    instance.DetailOrderID = original
    assert instance.DetailOrderID == original

@given(instance=Orders_strategy)
@settings(max_examples=50)
def test_orders_instantiation(instance):
    assert isinstance(instance, Orders)



@given(instance=Orders_strategy)
def test_orders_OrderID_setter(instance):
    original = instance.OrderID
    instance.OrderID = original
    assert instance.OrderID == original



@given(instance=Orders_strategy)
def test_orders_DeliInfo_setter(instance):
    original = instance.DeliInfo
    instance.DeliInfo = original
    assert instance.DeliInfo == original



@given(instance=Orders_strategy)
def test_orders_OrderInfo_setter(instance):
    original = instance.OrderInfo
    instance.OrderInfo = original
    assert instance.OrderInfo == original



@given(instance=Orders_strategy)
def test_orders_UserID_setter(instance):
    original = instance.UserID
    instance.UserID = original
    assert instance.UserID == original

@given(instance=DetailCart_strategy)
@settings(max_examples=50)
def test_detailcart_instantiation(instance):
    assert isinstance(instance, DetailCart)



@given(instance=DetailCart_strategy)
def test_detailcart_DetailCartID_setter(instance):
    original = instance.DetailCartID
    instance.DetailCartID = original
    assert instance.DetailCartID == original



@given(instance=DetailCart_strategy)
def test_detailcart_DetailCartInfo_setter(instance):
    original = instance.DetailCartInfo
    instance.DetailCartInfo = original
    assert instance.DetailCartInfo == original



@given(instance=DetailCart_strategy)
def test_detailcart_ProductID_setter(instance):
    original = instance.ProductID
    instance.ProductID = original
    assert instance.ProductID == original



@given(instance=DetailCart_strategy)
def test_detailcart_CartID_setter(instance):
    original = instance.CartID
    instance.CartID = original
    assert instance.CartID == original

@given(instance=Cart_strategy)
@settings(max_examples=50)
def test_cart_instantiation(instance):
    assert isinstance(instance, Cart)



@given(instance=Cart_strategy)
def test_cart_CartID_setter(instance):
    original = instance.CartID
    instance.CartID = original
    assert instance.CartID == original



@given(instance=Cart_strategy)
def test_cart_CartInfo_setter(instance):
    original = instance.CartInfo
    instance.CartInfo = original
    assert instance.CartInfo == original

@given(instance=Inventory_strategy)
@settings(max_examples=50)
def test_inventory_instantiation(instance):
    assert isinstance(instance, Inventory)



@given(instance=Inventory_strategy)
def test_inventory_ColorID_setter(instance):
    original = instance.ColorID
    instance.ColorID = original
    assert instance.ColorID == original



@given(instance=Inventory_strategy)
def test_inventory_ProductID_setter(instance):
    original = instance.ProductID
    instance.ProductID = original
    assert instance.ProductID == original



@given(instance=Inventory_strategy)
def test_inventory_SizeID_setter(instance):
    original = instance.SizeID
    instance.SizeID = original
    assert instance.SizeID == original



@given(instance=Inventory_strategy)
def test_inventory_InStock_setter(instance):
    original = instance.InStock
    instance.InStock = original
    assert instance.InStock == original

@given(instance=Size_strategy)
@settings(max_examples=50)
def test_size_instantiation(instance):
    assert isinstance(instance, Size)



@given(instance=Size_strategy)
def test_size_SizeID_setter(instance):
    original = instance.SizeID
    instance.SizeID = original
    assert instance.SizeID == original



@given(instance=Size_strategy)
def test_size_SizeName_setter(instance):
    original = instance.SizeName
    instance.SizeName = original
    assert instance.SizeName == original

@given(instance=Color_strategy)
@settings(max_examples=50)
def test_color_instantiation(instance):
    assert isinstance(instance, Color)



@given(instance=Color_strategy)
def test_color_ColorName_setter(instance):
    original = instance.ColorName
    instance.ColorName = original
    assert instance.ColorName == original



@given(instance=Color_strategy)
def test_color_ColorID_setter(instance):
    original = instance.ColorID
    instance.ColorID = original
    assert instance.ColorID == original

@given(instance=Banner_strategy)
@settings(max_examples=50)
def test_banner_instantiation(instance):
    assert isinstance(instance, Banner)



@given(instance=Banner_strategy)
def test_banner_BannerInfo_setter(instance):
    original = instance.BannerInfo
    instance.BannerInfo = original
    assert instance.BannerInfo == original



@given(instance=Banner_strategy)
def test_banner_IsShow_setter(instance):
    original = instance.IsShow
    instance.IsShow = original
    assert instance.IsShow == original



@given(instance=Banner_strategy)
def test_banner_DateStart_setter(instance):
    original = instance.DateStart
    instance.DateStart = original
    assert instance.DateStart == original



@given(instance=Banner_strategy)
def test_banner_Image_setter(instance):
    original = instance.Image
    instance.Image = original
    assert instance.Image == original



@given(instance=Banner_strategy)
def test_banner_BannerID_setter(instance):
    original = instance.BannerID
    instance.BannerID = original
    assert instance.BannerID == original



@given(instance=Banner_strategy)
def test_banner_DateEnd_setter(instance):
    original = instance.DateEnd
    instance.DateEnd = original
    assert instance.DateEnd == original

@given(instance=Gallery_strategy)
@settings(max_examples=50)
def test_gallery_instantiation(instance):
    assert isinstance(instance, Gallery)



@given(instance=Gallery_strategy)
def test_gallery_ProductID_setter(instance):
    original = instance.ProductID
    instance.ProductID = original
    assert instance.ProductID == original



@given(instance=Gallery_strategy)
def test_gallery_GalleryName_setter(instance):
    original = instance.GalleryName
    instance.GalleryName = original
    assert instance.GalleryName == original



@given(instance=Gallery_strategy)
def test_gallery_GalleryID_setter(instance):
    original = instance.GalleryID
    instance.GalleryID = original
    assert instance.GalleryID == original



@given(instance=Gallery_strategy)
def test_gallery_DateCreate_setter(instance):
    original = instance.DateCreate
    instance.DateCreate = original
    assert instance.DateCreate == original



@given(instance=Gallery_strategy)
def test_gallery_Image_setter(instance):
    original = instance.Image
    instance.Image = original
    assert instance.Image == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)



@given(instance=Type_strategy)
def test_type_TypeID_setter(instance):
    original = instance.TypeID
    instance.TypeID = original
    assert instance.TypeID == original



@given(instance=Type_strategy)
def test_type_TypeName_setter(instance):
    original = instance.TypeName
    instance.TypeName = original
    assert instance.TypeName == original

@given(instance=Collection_strategy)
@settings(max_examples=50)
def test_collection_instantiation(instance):
    assert isinstance(instance, Collection)



@given(instance=Collection_strategy)
def test_collection_CollectionName_setter(instance):
    original = instance.CollectionName
    instance.CollectionName = original
    assert instance.CollectionName == original



@given(instance=Collection_strategy)
def test_collection_CollectionID_setter(instance):
    original = instance.CollectionID
    instance.CollectionID = original
    assert instance.CollectionID == original

@given(instance=Products_strategy)
@settings(max_examples=50)
def test_products_instantiation(instance):
    assert isinstance(instance, Products)



@given(instance=Products_strategy)
def test_products_ProductID_setter(instance):
    original = instance.ProductID
    instance.ProductID = original
    assert instance.ProductID == original



@given(instance=Products_strategy)
def test_products_CollectionID_setter(instance):
    original = instance.CollectionID
    instance.CollectionID = original
    assert instance.CollectionID == original



@given(instance=Products_strategy)
def test_products_InStock_setter(instance):
    original = instance.InStock
    instance.InStock = original
    assert instance.InStock == original



@given(instance=Products_strategy)
def test_products_TypeID1_setter(instance):
    original = instance.TypeID1
    instance.TypeID1 = original
    assert instance.TypeID1 == original



@given(instance=Products_strategy)
def test_products_TypeID_setter(instance):
    original = instance.TypeID
    instance.TypeID = original
    assert instance.TypeID == original



@given(instance=Products_strategy)
def test_products_ProductInfo_setter(instance):
    original = instance.ProductInfo
    instance.ProductInfo = original
    assert instance.ProductInfo == original



@given(instance=Products_strategy)
def test_products_Index_setter(instance):
    original = instance.Index
    instance.Index = original
    assert instance.Index == original



@given(instance=Products_strategy)
def test_products_DateCreate_setter(instance):
    original = instance.DateCreate
    instance.DateCreate = original
    assert instance.DateCreate == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original



@given(instance=User_strategy)
def test_user_Point_setter(instance):
    original = instance.Point
    instance.Point = original
    assert instance.Point == original



@given(instance=User_strategy)
def test_user_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=User_strategy)
def test_user_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=User_strategy)
def test_user_UserInfo_setter(instance):
    original = instance.UserInfo
    instance.UserInfo = original
    assert instance.UserInfo == original



@given(instance=User_strategy)
def test_user_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=User_strategy)
def test_user_Phone_setter(instance):
    original = instance.Phone
    instance.Phone = original
    assert instance.Phone == original
