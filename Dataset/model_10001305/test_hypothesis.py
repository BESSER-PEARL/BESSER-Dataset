import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Vendor,
    UserAddress,
    Promos,
    Product,
    OrderProcess,
    ShoppingCart,
    Regular_Members,
    Premium_Members,
    UserName,
    User_Account,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_vendor_is_not_abstract():
    assert not inspect.isabstract(Vendor)


def test_vendor_constructor_exists():
    assert callable(Vendor.__init__)


def test_vendor_constructor_args():
    sig = inspect.signature(Vendor.__init__)
    params = list(sig.parameters.keys())
    assert "Contact_Number" in params, "Missing parameter 'Contact_Number'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "VendorID" in params, "Missing parameter 'VendorID'"
    assert "Address" in params, "Missing parameter 'Address'"

def test_vendor_has_Contact_Number():
    assert hasattr(Vendor, "Contact_Number")
    descriptor = None
    for klass in Vendor.__mro__:
        if "Contact_Number" in klass.__dict__:
            descriptor = klass.__dict__["Contact_Number"]
            break
    assert isinstance(descriptor, property)

def test_vendor_has_Email():
    assert hasattr(Vendor, "Email")
    descriptor = None
    for klass in Vendor.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_vendor_has_Name():
    assert hasattr(Vendor, "Name")
    descriptor = None
    for klass in Vendor.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_vendor_has_VendorID():
    assert hasattr(Vendor, "VendorID")
    descriptor = None
    for klass in Vendor.__mro__:
        if "VendorID" in klass.__dict__:
            descriptor = klass.__dict__["VendorID"]
            break
    assert isinstance(descriptor, property)

def test_vendor_has_Address():
    assert hasattr(Vendor, "Address")
    descriptor = None
    for klass in Vendor.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)



def test_useraddress_is_not_abstract():
    assert not inspect.isabstract(UserAddress)


def test_useraddress_constructor_exists():
    assert callable(UserAddress.__init__)


def test_useraddress_constructor_args():
    sig = inspect.signature(UserAddress.__init__)
    params = list(sig.parameters.keys())
    assert "City" in params, "Missing parameter 'City'"
    assert "StreetName" in params, "Missing parameter 'StreetName'"
    assert "StreetNum" in params, "Missing parameter 'StreetNum'"
    assert "PostCode" in params, "Missing parameter 'PostCode'"

def test_useraddress_has_City():
    assert hasattr(UserAddress, "City")
    descriptor = None
    for klass in UserAddress.__mro__:
        if "City" in klass.__dict__:
            descriptor = klass.__dict__["City"]
            break
    assert isinstance(descriptor, property)

def test_useraddress_has_StreetName():
    assert hasattr(UserAddress, "StreetName")
    descriptor = None
    for klass in UserAddress.__mro__:
        if "StreetName" in klass.__dict__:
            descriptor = klass.__dict__["StreetName"]
            break
    assert isinstance(descriptor, property)

def test_useraddress_has_StreetNum():
    assert hasattr(UserAddress, "StreetNum")
    descriptor = None
    for klass in UserAddress.__mro__:
        if "StreetNum" in klass.__dict__:
            descriptor = klass.__dict__["StreetNum"]
            break
    assert isinstance(descriptor, property)

def test_useraddress_has_PostCode():
    assert hasattr(UserAddress, "PostCode")
    descriptor = None
    for klass in UserAddress.__mro__:
        if "PostCode" in klass.__dict__:
            descriptor = klass.__dict__["PostCode"]
            break
    assert isinstance(descriptor, property)



def test_promos_is_not_abstract():
    assert not inspect.isabstract(Promos)


def test_promos_constructor_exists():
    assert callable(Promos.__init__)


def test_promos_constructor_args():
    sig = inspect.signature(Promos.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "EndDate" in params, "Missing parameter 'EndDate'"
    assert "Discount" in params, "Missing parameter 'Discount'"
    assert "PromoCode" in params, "Missing parameter 'PromoCode'"
    assert "StartDate" in params, "Missing parameter 'StartDate'"

def test_promos_has_Name():
    assert hasattr(Promos, "Name")
    descriptor = None
    for klass in Promos.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_promos_has_EndDate():
    assert hasattr(Promos, "EndDate")
    descriptor = None
    for klass in Promos.__mro__:
        if "EndDate" in klass.__dict__:
            descriptor = klass.__dict__["EndDate"]
            break
    assert isinstance(descriptor, property)

def test_promos_has_Discount():
    assert hasattr(Promos, "Discount")
    descriptor = None
    for klass in Promos.__mro__:
        if "Discount" in klass.__dict__:
            descriptor = klass.__dict__["Discount"]
            break
    assert isinstance(descriptor, property)

def test_promos_has_PromoCode():
    assert hasattr(Promos, "PromoCode")
    descriptor = None
    for klass in Promos.__mro__:
        if "PromoCode" in klass.__dict__:
            descriptor = klass.__dict__["PromoCode"]
            break
    assert isinstance(descriptor, property)

def test_promos_has_StartDate():
    assert hasattr(Promos, "StartDate")
    descriptor = None
    for klass in Promos.__mro__:
        if "StartDate" in klass.__dict__:
            descriptor = klass.__dict__["StartDate"]
            break
    assert isinstance(descriptor, property)



def test_product_is_not_abstract():
    assert not inspect.isabstract(Product)


def test_product_constructor_exists():
    assert callable(Product.__init__)


def test_product_constructor_args():
    sig = inspect.signature(Product.__init__)
    params = list(sig.parameters.keys())
    assert "InventoryQuantity" in params, "Missing parameter 'InventoryQuantity'"
    assert "Description" in params, "Missing parameter 'Description'"
    assert "VendorID" in params, "Missing parameter 'VendorID'"
    assert "ProductID" in params, "Missing parameter 'ProductID'"
    assert "InventoryMinQuantity" in params, "Missing parameter 'InventoryMinQuantity'"

def test_product_has_InventoryQuantity():
    assert hasattr(Product, "InventoryQuantity")
    descriptor = None
    for klass in Product.__mro__:
        if "InventoryQuantity" in klass.__dict__:
            descriptor = klass.__dict__["InventoryQuantity"]
            break
    assert isinstance(descriptor, property)

def test_product_has_Description():
    assert hasattr(Product, "Description")
    descriptor = None
    for klass in Product.__mro__:
        if "Description" in klass.__dict__:
            descriptor = klass.__dict__["Description"]
            break
    assert isinstance(descriptor, property)

def test_product_has_VendorID():
    assert hasattr(Product, "VendorID")
    descriptor = None
    for klass in Product.__mro__:
        if "VendorID" in klass.__dict__:
            descriptor = klass.__dict__["VendorID"]
            break
    assert isinstance(descriptor, property)

def test_product_has_ProductID():
    assert hasattr(Product, "ProductID")
    descriptor = None
    for klass in Product.__mro__:
        if "ProductID" in klass.__dict__:
            descriptor = klass.__dict__["ProductID"]
            break
    assert isinstance(descriptor, property)

def test_product_has_InventoryMinQuantity():
    assert hasattr(Product, "InventoryMinQuantity")
    descriptor = None
    for klass in Product.__mro__:
        if "InventoryMinQuantity" in klass.__dict__:
            descriptor = klass.__dict__["InventoryMinQuantity"]
            break
    assert isinstance(descriptor, property)



def test_orderprocess_is_not_abstract():
    assert not inspect.isabstract(OrderProcess)


def test_orderprocess_constructor_exists():
    assert callable(OrderProcess.__init__)


def test_orderprocess_constructor_args():
    sig = inspect.signature(OrderProcess.__init__)
    params = list(sig.parameters.keys())
    assert "PromoCode" in params, "Missing parameter 'PromoCode'"
    assert "UserID" in params, "Missing parameter 'UserID'"
    assert "OrderID" in params, "Missing parameter 'OrderID'"
    assert "OrderPickUp" in params, "Missing parameter 'OrderPickUp'"
    assert "Total" in params, "Missing parameter 'Total'"
    assert "IsMember" in params, "Missing parameter 'IsMember'"
    assert "MemberShipPayment" in params, "Missing parameter 'MemberShipPayment'"

def test_orderprocess_has_PromoCode():
    assert hasattr(OrderProcess, "PromoCode")
    descriptor = None
    for klass in OrderProcess.__mro__:
        if "PromoCode" in klass.__dict__:
            descriptor = klass.__dict__["PromoCode"]
            break
    assert isinstance(descriptor, property)

def test_orderprocess_has_UserID():
    assert hasattr(OrderProcess, "UserID")
    descriptor = None
    for klass in OrderProcess.__mro__:
        if "UserID" in klass.__dict__:
            descriptor = klass.__dict__["UserID"]
            break
    assert isinstance(descriptor, property)

def test_orderprocess_has_OrderID():
    assert hasattr(OrderProcess, "OrderID")
    descriptor = None
    for klass in OrderProcess.__mro__:
        if "OrderID" in klass.__dict__:
            descriptor = klass.__dict__["OrderID"]
            break
    assert isinstance(descriptor, property)

def test_orderprocess_has_OrderPickUp():
    assert hasattr(OrderProcess, "OrderPickUp")
    descriptor = None
    for klass in OrderProcess.__mro__:
        if "OrderPickUp" in klass.__dict__:
            descriptor = klass.__dict__["OrderPickUp"]
            break
    assert isinstance(descriptor, property)

def test_orderprocess_has_Total():
    assert hasattr(OrderProcess, "Total")
    descriptor = None
    for klass in OrderProcess.__mro__:
        if "Total" in klass.__dict__:
            descriptor = klass.__dict__["Total"]
            break
    assert isinstance(descriptor, property)

def test_orderprocess_has_IsMember():
    assert hasattr(OrderProcess, "IsMember")
    descriptor = None
    for klass in OrderProcess.__mro__:
        if "IsMember" in klass.__dict__:
            descriptor = klass.__dict__["IsMember"]
            break
    assert isinstance(descriptor, property)

def test_orderprocess_has_MemberShipPayment():
    assert hasattr(OrderProcess, "MemberShipPayment")
    descriptor = None
    for klass in OrderProcess.__mro__:
        if "MemberShipPayment" in klass.__dict__:
            descriptor = klass.__dict__["MemberShipPayment"]
            break
    assert isinstance(descriptor, property)



def test_shoppingcart_is_not_abstract():
    assert not inspect.isabstract(ShoppingCart)


def test_shoppingcart_constructor_exists():
    assert callable(ShoppingCart.__init__)


def test_shoppingcart_constructor_args():
    sig = inspect.signature(ShoppingCart.__init__)
    params = list(sig.parameters.keys())
    assert "ShoppingCartID" in params, "Missing parameter 'ShoppingCartID'"
    assert "ProductID" in params, "Missing parameter 'ProductID'"
    assert "Quantity" in params, "Missing parameter 'Quantity'"
    assert "Total" in params, "Missing parameter 'Total'"
    assert "OrderID" in params, "Missing parameter 'OrderID'"
    assert "UserID" in params, "Missing parameter 'UserID'"
    assert "Promo" in params, "Missing parameter 'Promo'"

def test_shoppingcart_has_ShoppingCartID():
    assert hasattr(ShoppingCart, "ShoppingCartID")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "ShoppingCartID" in klass.__dict__:
            descriptor = klass.__dict__["ShoppingCartID"]
            break
    assert isinstance(descriptor, property)

def test_shoppingcart_has_ProductID():
    assert hasattr(ShoppingCart, "ProductID")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "ProductID" in klass.__dict__:
            descriptor = klass.__dict__["ProductID"]
            break
    assert isinstance(descriptor, property)

def test_shoppingcart_has_Quantity():
    assert hasattr(ShoppingCart, "Quantity")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "Quantity" in klass.__dict__:
            descriptor = klass.__dict__["Quantity"]
            break
    assert isinstance(descriptor, property)

def test_shoppingcart_has_Total():
    assert hasattr(ShoppingCart, "Total")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "Total" in klass.__dict__:
            descriptor = klass.__dict__["Total"]
            break
    assert isinstance(descriptor, property)

def test_shoppingcart_has_OrderID():
    assert hasattr(ShoppingCart, "OrderID")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "OrderID" in klass.__dict__:
            descriptor = klass.__dict__["OrderID"]
            break
    assert isinstance(descriptor, property)

def test_shoppingcart_has_UserID():
    assert hasattr(ShoppingCart, "UserID")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "UserID" in klass.__dict__:
            descriptor = klass.__dict__["UserID"]
            break
    assert isinstance(descriptor, property)

def test_shoppingcart_has_Promo():
    assert hasattr(ShoppingCart, "Promo")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "Promo" in klass.__dict__:
            descriptor = klass.__dict__["Promo"]
            break
    assert isinstance(descriptor, property)



def test_regular_members_is_not_abstract():
    assert not inspect.isabstract(Regular_Members)


def test_regular_members_constructor_exists():
    assert callable(Regular_Members.__init__)


def test_regular_members_constructor_args():
    sig = inspect.signature(Regular_Members.__init__)
    params = list(sig.parameters.keys())
    assert "TrialStartDate" in params, "Missing parameter 'TrialStartDate'"
    assert "TriedPremium" in params, "Missing parameter 'TriedPremium'"

def test_regular_members_has_TrialStartDate():
    assert hasattr(Regular_Members, "TrialStartDate")
    descriptor = None
    for klass in Regular_Members.__mro__:
        if "TrialStartDate" in klass.__dict__:
            descriptor = klass.__dict__["TrialStartDate"]
            break
    assert isinstance(descriptor, property)

def test_regular_members_has_TriedPremium():
    assert hasattr(Regular_Members, "TriedPremium")
    descriptor = None
    for klass in Regular_Members.__mro__:
        if "TriedPremium" in klass.__dict__:
            descriptor = klass.__dict__["TriedPremium"]
            break
    assert isinstance(descriptor, property)



def test_premium_members_is_not_abstract():
    assert not inspect.isabstract(Premium_Members)


def test_premium_members_constructor_exists():
    assert callable(Premium_Members.__init__)


def test_premium_members_constructor_args():
    sig = inspect.signature(Premium_Members.__init__)
    params = list(sig.parameters.keys())
    assert "MembershipEndDate" in params, "Missing parameter 'MembershipEndDate'"
    assert "PromoCode" in params, "Missing parameter 'PromoCode'"
    assert "MembershipStartDate" in params, "Missing parameter 'MembershipStartDate'"

def test_premium_members_has_MembershipEndDate():
    assert hasattr(Premium_Members, "MembershipEndDate")
    descriptor = None
    for klass in Premium_Members.__mro__:
        if "MembershipEndDate" in klass.__dict__:
            descriptor = klass.__dict__["MembershipEndDate"]
            break
    assert isinstance(descriptor, property)

def test_premium_members_has_PromoCode():
    assert hasattr(Premium_Members, "PromoCode")
    descriptor = None
    for klass in Premium_Members.__mro__:
        if "PromoCode" in klass.__dict__:
            descriptor = klass.__dict__["PromoCode"]
            break
    assert isinstance(descriptor, property)

def test_premium_members_has_MembershipStartDate():
    assert hasattr(Premium_Members, "MembershipStartDate")
    descriptor = None
    for klass in Premium_Members.__mro__:
        if "MembershipStartDate" in klass.__dict__:
            descriptor = klass.__dict__["MembershipStartDate"]
            break
    assert isinstance(descriptor, property)



def test_username_is_not_abstract():
    assert not inspect.isabstract(UserName)


def test_username_constructor_exists():
    assert callable(UserName.__init__)


def test_username_constructor_args():
    sig = inspect.signature(UserName.__init__)
    params = list(sig.parameters.keys())
    assert "LastName" in params, "Missing parameter 'LastName'"
    assert "FirstName" in params, "Missing parameter 'FirstName'"

def test_username_has_LastName():
    assert hasattr(UserName, "LastName")
    descriptor = None
    for klass in UserName.__mro__:
        if "LastName" in klass.__dict__:
            descriptor = klass.__dict__["LastName"]
            break
    assert isinstance(descriptor, property)

def test_username_has_FirstName():
    assert hasattr(UserName, "FirstName")
    descriptor = None
    for klass in UserName.__mro__:
        if "FirstName" in klass.__dict__:
            descriptor = klass.__dict__["FirstName"]
            break
    assert isinstance(descriptor, property)



def test_user_account_is_not_abstract():
    assert not inspect.isabstract(User_Account)


def test_user_account_constructor_exists():
    assert callable(User_Account.__init__)


def test_user_account_constructor_args():
    sig = inspect.signature(User_Account.__init__)
    params = list(sig.parameters.keys())
    assert "UserID" in params, "Missing parameter 'UserID'"
    assert "DateOfBirth" in params, "Missing parameter 'DateOfBirth'"
    assert "RegDate" in params, "Missing parameter 'RegDate'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "FullName" in params, "Missing parameter 'FullName'"
    assert "UserAddress" in params, "Missing parameter 'UserAddress'"

def test_user_account_has_UserID():
    assert hasattr(User_Account, "UserID")
    descriptor = None
    for klass in User_Account.__mro__:
        if "UserID" in klass.__dict__:
            descriptor = klass.__dict__["UserID"]
            break
    assert isinstance(descriptor, property)

def test_user_account_has_DateOfBirth():
    assert hasattr(User_Account, "DateOfBirth")
    descriptor = None
    for klass in User_Account.__mro__:
        if "DateOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["DateOfBirth"]
            break
    assert isinstance(descriptor, property)

def test_user_account_has_RegDate():
    assert hasattr(User_Account, "RegDate")
    descriptor = None
    for klass in User_Account.__mro__:
        if "RegDate" in klass.__dict__:
            descriptor = klass.__dict__["RegDate"]
            break
    assert isinstance(descriptor, property)

def test_user_account_has_Email():
    assert hasattr(User_Account, "Email")
    descriptor = None
    for klass in User_Account.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_user_account_has_FullName():
    assert hasattr(User_Account, "FullName")
    descriptor = None
    for klass in User_Account.__mro__:
        if "FullName" in klass.__dict__:
            descriptor = klass.__dict__["FullName"]
            break
    assert isinstance(descriptor, property)

def test_user_account_has_UserAddress():
    assert hasattr(User_Account, "UserAddress")
    descriptor = None
    for klass in User_Account.__mro__:
        if "UserAddress" in klass.__dict__:
            descriptor = klass.__dict__["UserAddress"]
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
Vendor_strategy = st.builds(
    Vendor,
    Contact_Number=
        st.integers(),
    Email=
        safe_text,
    Name=
        safe_text,
    VendorID=
        st.integers(),
    Address=
        safe_text
)
UserAddress_strategy = st.builds(
    UserAddress,
    City=
        safe_text,
    StreetName=
        safe_text,
    StreetNum=
        st.integers(),
    PostCode=
        safe_text
)
Promos_strategy = st.builds(
    Promos,
    Name=
        safe_text,
    EndDate=
        safe_text,
    Discount=
        safe_text,
    PromoCode=
        safe_text,
    StartDate=
        safe_text
)
Product_strategy = st.builds(
    Product,
    InventoryQuantity=
        st.integers(),
    Description=
        safe_text,
    VendorID=
        st.integers(),
    ProductID=
        st.integers(),
    InventoryMinQuantity=
        st.integers()
)
OrderProcess_strategy = st.builds(
    OrderProcess,
    PromoCode=
        safe_text,
    UserID=
        st.integers(),
    OrderID=
        st.integers(),
    OrderPickUp=
        st.integers(),
    Total=
        safe_text,
    IsMember=
        st.integers(),
    MemberShipPayment=
        st.integers()
)
ShoppingCart_strategy = st.builds(
    ShoppingCart,
    ShoppingCartID=
        st.integers(),
    ProductID=
        st.integers(),
    Quantity=
        st.integers(),
    Total=
        safe_text,
    OrderID=
        st.integers(),
    UserID=
        safe_text,
    Promo=
        st.none()
)
Regular_Members_strategy = st.builds(
    Regular_Members,
    TrialStartDate=
        safe_text,
    TriedPremium=
        st.integers()
)
Premium_Members_strategy = st.builds(
    Premium_Members,
    MembershipEndDate=
        safe_text,
    PromoCode=
        safe_text,
    MembershipStartDate=
        safe_text
)
UserName_strategy = st.builds(
    UserName,
    LastName=
        safe_text,
    FirstName=
        safe_text
)
User_Account_strategy = st.builds(
    User_Account,
    UserID=
        safe_text,
    DateOfBirth=
        safe_text,
    RegDate=
        safe_text,
    Email=
        safe_text,
    FullName=
        safe_text,
    UserAddress=
        safe_text
)

@given(instance=Vendor_strategy)
@settings(max_examples=50)
def test_vendor_instantiation(instance):
    assert isinstance(instance, Vendor)



@given(instance=Vendor_strategy)
def test_vendor_Contact_Number_setter(instance):
    original = instance.Contact_Number
    instance.Contact_Number = original
    assert instance.Contact_Number == original



@given(instance=Vendor_strategy)
def test_vendor_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Vendor_strategy)
def test_vendor_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Vendor_strategy)
def test_vendor_VendorID_setter(instance):
    original = instance.VendorID
    instance.VendorID = original
    assert instance.VendorID == original



@given(instance=Vendor_strategy)
def test_vendor_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original

@given(instance=UserAddress_strategy)
@settings(max_examples=50)
def test_useraddress_instantiation(instance):
    assert isinstance(instance, UserAddress)



@given(instance=UserAddress_strategy)
def test_useraddress_City_setter(instance):
    original = instance.City
    instance.City = original
    assert instance.City == original



@given(instance=UserAddress_strategy)
def test_useraddress_StreetName_setter(instance):
    original = instance.StreetName
    instance.StreetName = original
    assert instance.StreetName == original



@given(instance=UserAddress_strategy)
def test_useraddress_StreetNum_setter(instance):
    original = instance.StreetNum
    instance.StreetNum = original
    assert instance.StreetNum == original



@given(instance=UserAddress_strategy)
def test_useraddress_PostCode_setter(instance):
    original = instance.PostCode
    instance.PostCode = original
    assert instance.PostCode == original

@given(instance=Promos_strategy)
@settings(max_examples=50)
def test_promos_instantiation(instance):
    assert isinstance(instance, Promos)



@given(instance=Promos_strategy)
def test_promos_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Promos_strategy)
def test_promos_EndDate_setter(instance):
    original = instance.EndDate
    instance.EndDate = original
    assert instance.EndDate == original



@given(instance=Promos_strategy)
def test_promos_Discount_setter(instance):
    original = instance.Discount
    instance.Discount = original
    assert instance.Discount == original



@given(instance=Promos_strategy)
def test_promos_PromoCode_setter(instance):
    original = instance.PromoCode
    instance.PromoCode = original
    assert instance.PromoCode == original



@given(instance=Promos_strategy)
def test_promos_StartDate_setter(instance):
    original = instance.StartDate
    instance.StartDate = original
    assert instance.StartDate == original

@given(instance=Product_strategy)
@settings(max_examples=50)
def test_product_instantiation(instance):
    assert isinstance(instance, Product)



@given(instance=Product_strategy)
def test_product_InventoryQuantity_setter(instance):
    original = instance.InventoryQuantity
    instance.InventoryQuantity = original
    assert instance.InventoryQuantity == original



@given(instance=Product_strategy)
def test_product_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original



@given(instance=Product_strategy)
def test_product_VendorID_setter(instance):
    original = instance.VendorID
    instance.VendorID = original
    assert instance.VendorID == original



@given(instance=Product_strategy)
def test_product_ProductID_setter(instance):
    original = instance.ProductID
    instance.ProductID = original
    assert instance.ProductID == original



@given(instance=Product_strategy)
def test_product_InventoryMinQuantity_setter(instance):
    original = instance.InventoryMinQuantity
    instance.InventoryMinQuantity = original
    assert instance.InventoryMinQuantity == original

@given(instance=OrderProcess_strategy)
@settings(max_examples=50)
def test_orderprocess_instantiation(instance):
    assert isinstance(instance, OrderProcess)



@given(instance=OrderProcess_strategy)
def test_orderprocess_PromoCode_setter(instance):
    original = instance.PromoCode
    instance.PromoCode = original
    assert instance.PromoCode == original



@given(instance=OrderProcess_strategy)
def test_orderprocess_UserID_setter(instance):
    original = instance.UserID
    instance.UserID = original
    assert instance.UserID == original



@given(instance=OrderProcess_strategy)
def test_orderprocess_OrderID_setter(instance):
    original = instance.OrderID
    instance.OrderID = original
    assert instance.OrderID == original



@given(instance=OrderProcess_strategy)
def test_orderprocess_OrderPickUp_setter(instance):
    original = instance.OrderPickUp
    instance.OrderPickUp = original
    assert instance.OrderPickUp == original



@given(instance=OrderProcess_strategy)
def test_orderprocess_Total_setter(instance):
    original = instance.Total
    instance.Total = original
    assert instance.Total == original



@given(instance=OrderProcess_strategy)
def test_orderprocess_IsMember_setter(instance):
    original = instance.IsMember
    instance.IsMember = original
    assert instance.IsMember == original



@given(instance=OrderProcess_strategy)
def test_orderprocess_MemberShipPayment_setter(instance):
    original = instance.MemberShipPayment
    instance.MemberShipPayment = original
    assert instance.MemberShipPayment == original

@given(instance=ShoppingCart_strategy)
@settings(max_examples=50)
def test_shoppingcart_instantiation(instance):
    assert isinstance(instance, ShoppingCart)



@given(instance=ShoppingCart_strategy)
def test_shoppingcart_ShoppingCartID_setter(instance):
    original = instance.ShoppingCartID
    instance.ShoppingCartID = original
    assert instance.ShoppingCartID == original



@given(instance=ShoppingCart_strategy)
def test_shoppingcart_ProductID_setter(instance):
    original = instance.ProductID
    instance.ProductID = original
    assert instance.ProductID == original



@given(instance=ShoppingCart_strategy)
def test_shoppingcart_Quantity_setter(instance):
    original = instance.Quantity
    instance.Quantity = original
    assert instance.Quantity == original



@given(instance=ShoppingCart_strategy)
def test_shoppingcart_Total_setter(instance):
    original = instance.Total
    instance.Total = original
    assert instance.Total == original



@given(instance=ShoppingCart_strategy)
def test_shoppingcart_OrderID_setter(instance):
    original = instance.OrderID
    instance.OrderID = original
    assert instance.OrderID == original



@given(instance=ShoppingCart_strategy)
def test_shoppingcart_UserID_setter(instance):
    original = instance.UserID
    instance.UserID = original
    assert instance.UserID == original



@given(instance=ShoppingCart_strategy)
def test_shoppingcart_Promo_setter(instance):
    original = instance.Promo
    instance.Promo = original
    assert instance.Promo == original

@given(instance=Regular_Members_strategy)
@settings(max_examples=50)
def test_regular_members_instantiation(instance):
    assert isinstance(instance, Regular_Members)



@given(instance=Regular_Members_strategy)
def test_regular_members_TrialStartDate_setter(instance):
    original = instance.TrialStartDate
    instance.TrialStartDate = original
    assert instance.TrialStartDate == original



@given(instance=Regular_Members_strategy)
def test_regular_members_TriedPremium_setter(instance):
    original = instance.TriedPremium
    instance.TriedPremium = original
    assert instance.TriedPremium == original

@given(instance=Premium_Members_strategy)
@settings(max_examples=50)
def test_premium_members_instantiation(instance):
    assert isinstance(instance, Premium_Members)



@given(instance=Premium_Members_strategy)
def test_premium_members_MembershipEndDate_setter(instance):
    original = instance.MembershipEndDate
    instance.MembershipEndDate = original
    assert instance.MembershipEndDate == original



@given(instance=Premium_Members_strategy)
def test_premium_members_PromoCode_setter(instance):
    original = instance.PromoCode
    instance.PromoCode = original
    assert instance.PromoCode == original



@given(instance=Premium_Members_strategy)
def test_premium_members_MembershipStartDate_setter(instance):
    original = instance.MembershipStartDate
    instance.MembershipStartDate = original
    assert instance.MembershipStartDate == original

@given(instance=UserName_strategy)
@settings(max_examples=50)
def test_username_instantiation(instance):
    assert isinstance(instance, UserName)



@given(instance=UserName_strategy)
def test_username_LastName_setter(instance):
    original = instance.LastName
    instance.LastName = original
    assert instance.LastName == original



@given(instance=UserName_strategy)
def test_username_FirstName_setter(instance):
    original = instance.FirstName
    instance.FirstName = original
    assert instance.FirstName == original

@given(instance=User_Account_strategy)
@settings(max_examples=50)
def test_user_account_instantiation(instance):
    assert isinstance(instance, User_Account)



@given(instance=User_Account_strategy)
def test_user_account_UserID_setter(instance):
    original = instance.UserID
    instance.UserID = original
    assert instance.UserID == original



@given(instance=User_Account_strategy)
def test_user_account_DateOfBirth_setter(instance):
    original = instance.DateOfBirth
    instance.DateOfBirth = original
    assert instance.DateOfBirth == original



@given(instance=User_Account_strategy)
def test_user_account_RegDate_setter(instance):
    original = instance.RegDate
    instance.RegDate = original
    assert instance.RegDate == original



@given(instance=User_Account_strategy)
def test_user_account_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=User_Account_strategy)
def test_user_account_FullName_setter(instance):
    original = instance.FullName
    instance.FullName = original
    assert instance.FullName == original



@given(instance=User_Account_strategy)
def test_user_account_UserAddress_setter(instance):
    original = instance.UserAddress
    instance.UserAddress = original
    assert instance.UserAddress == original
