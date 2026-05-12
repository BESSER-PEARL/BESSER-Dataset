import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

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
    assert "VendorID" in params, "Missing parameter 'VendorID'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "Address" in params, "Missing parameter 'Address'"

def test_vendor_has_Contact_Number():
    assert hasattr(Vendor, "Contact_Number")
    descriptor = None
    for klass in Vendor.__mro__:
        if "Contact_Number" in klass.__dict__:
            descriptor = klass.__dict__["Contact_Number"]
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

def test_vendor_has_Name():
    assert hasattr(Vendor, "Name")
    descriptor = None
    for klass in Vendor.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
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
    assert "StreetName" in params, "Missing parameter 'StreetName'"
    assert "StreetNum" in params, "Missing parameter 'StreetNum'"
    assert "PostCode" in params, "Missing parameter 'PostCode'"
    assert "City" in params, "Missing parameter 'City'"

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

def test_useraddress_has_City():
    assert hasattr(UserAddress, "City")
    descriptor = None
    for klass in UserAddress.__mro__:
        if "City" in klass.__dict__:
            descriptor = klass.__dict__["City"]
            break
    assert isinstance(descriptor, property)



def test_promos_is_not_abstract():
    assert not inspect.isabstract(Promos)


def test_promos_constructor_exists():
    assert callable(Promos.__init__)


def test_promos_constructor_args():
    sig = inspect.signature(Promos.__init__)
    params = list(sig.parameters.keys())
    assert "PromoCode" in params, "Missing parameter 'PromoCode'"
    assert "StartDate" in params, "Missing parameter 'StartDate'"
    assert "Discount" in params, "Missing parameter 'Discount'"
    assert "EndDate" in params, "Missing parameter 'EndDate'"
    assert "Name" in params, "Missing parameter 'Name'"

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

def test_promos_has_Discount():
    assert hasattr(Promos, "Discount")
    descriptor = None
    for klass in Promos.__mro__:
        if "Discount" in klass.__dict__:
            descriptor = klass.__dict__["Discount"]
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

def test_promos_has_Name():
    assert hasattr(Promos, "Name")
    descriptor = None
    for klass in Promos.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_product_is_not_abstract():
    assert not inspect.isabstract(Product)


def test_product_constructor_exists():
    assert callable(Product.__init__)


def test_product_constructor_args():
    sig = inspect.signature(Product.__init__)
    params = list(sig.parameters.keys())
    assert "InventoryMinQuantity" in params, "Missing parameter 'InventoryMinQuantity'"
    assert "Description" in params, "Missing parameter 'Description'"
    assert "VendorID" in params, "Missing parameter 'VendorID'"
    assert "InventoryQuantity" in params, "Missing parameter 'InventoryQuantity'"
    assert "ProductID" in params, "Missing parameter 'ProductID'"

def test_product_has_InventoryMinQuantity():
    assert hasattr(Product, "InventoryMinQuantity")
    descriptor = None
    for klass in Product.__mro__:
        if "InventoryMinQuantity" in klass.__dict__:
            descriptor = klass.__dict__["InventoryMinQuantity"]
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

def test_product_has_InventoryQuantity():
    assert hasattr(Product, "InventoryQuantity")
    descriptor = None
    for klass in Product.__mro__:
        if "InventoryQuantity" in klass.__dict__:
            descriptor = klass.__dict__["InventoryQuantity"]
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



def test_orderprocess_is_not_abstract():
    assert not inspect.isabstract(OrderProcess)


def test_orderprocess_constructor_exists():
    assert callable(OrderProcess.__init__)


def test_orderprocess_constructor_args():
    sig = inspect.signature(OrderProcess.__init__)
    params = list(sig.parameters.keys())
    assert "OrderPickUp" in params, "Missing parameter 'OrderPickUp'"
    assert "UserID" in params, "Missing parameter 'UserID'"
    assert "Total" in params, "Missing parameter 'Total'"
    assert "PromoCode" in params, "Missing parameter 'PromoCode'"
    assert "MemberShipPayment" in params, "Missing parameter 'MemberShipPayment'"
    assert "IsMember" in params, "Missing parameter 'IsMember'"
    assert "OrderID" in params, "Missing parameter 'OrderID'"

def test_orderprocess_has_OrderPickUp():
    assert hasattr(OrderProcess, "OrderPickUp")
    descriptor = None
    for klass in OrderProcess.__mro__:
        if "OrderPickUp" in klass.__dict__:
            descriptor = klass.__dict__["OrderPickUp"]
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

def test_orderprocess_has_Total():
    assert hasattr(OrderProcess, "Total")
    descriptor = None
    for klass in OrderProcess.__mro__:
        if "Total" in klass.__dict__:
            descriptor = klass.__dict__["Total"]
            break
    assert isinstance(descriptor, property)

def test_orderprocess_has_PromoCode():
    assert hasattr(OrderProcess, "PromoCode")
    descriptor = None
    for klass in OrderProcess.__mro__:
        if "PromoCode" in klass.__dict__:
            descriptor = klass.__dict__["PromoCode"]
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

def test_orderprocess_has_IsMember():
    assert hasattr(OrderProcess, "IsMember")
    descriptor = None
    for klass in OrderProcess.__mro__:
        if "IsMember" in klass.__dict__:
            descriptor = klass.__dict__["IsMember"]
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



def test_shoppingcart_is_not_abstract():
    assert not inspect.isabstract(ShoppingCart)


def test_shoppingcart_constructor_exists():
    assert callable(ShoppingCart.__init__)


def test_shoppingcart_constructor_args():
    sig = inspect.signature(ShoppingCart.__init__)
    params = list(sig.parameters.keys())
    assert "Promo" in params, "Missing parameter 'Promo'"
    assert "ShoppingCartID" in params, "Missing parameter 'ShoppingCartID'"
    assert "Quantity" in params, "Missing parameter 'Quantity'"
    assert "UserID" in params, "Missing parameter 'UserID'"
    assert "OrderID" in params, "Missing parameter 'OrderID'"
    assert "Total" in params, "Missing parameter 'Total'"
    assert "ProductID" in params, "Missing parameter 'ProductID'"

def test_shoppingcart_has_Promo():
    assert hasattr(ShoppingCart, "Promo")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "Promo" in klass.__dict__:
            descriptor = klass.__dict__["Promo"]
            break
    assert isinstance(descriptor, property)

def test_shoppingcart_has_ShoppingCartID():
    assert hasattr(ShoppingCart, "ShoppingCartID")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "ShoppingCartID" in klass.__dict__:
            descriptor = klass.__dict__["ShoppingCartID"]
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

def test_shoppingcart_has_UserID():
    assert hasattr(ShoppingCart, "UserID")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "UserID" in klass.__dict__:
            descriptor = klass.__dict__["UserID"]
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

def test_shoppingcart_has_Total():
    assert hasattr(ShoppingCart, "Total")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "Total" in klass.__dict__:
            descriptor = klass.__dict__["Total"]
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



def test_regular_members_is_not_abstract():
    assert not inspect.isabstract(Regular_Members)


def test_regular_members_constructor_exists():
    assert callable(Regular_Members.__init__)


def test_regular_members_constructor_args():
    sig = inspect.signature(Regular_Members.__init__)
    params = list(sig.parameters.keys())
    assert "TriedPremium" in params, "Missing parameter 'TriedPremium'"
    assert "TrialStartDate" in params, "Missing parameter 'TrialStartDate'"

def test_regular_members_has_TriedPremium():
    assert hasattr(Regular_Members, "TriedPremium")
    descriptor = None
    for klass in Regular_Members.__mro__:
        if "TriedPremium" in klass.__dict__:
            descriptor = klass.__dict__["TriedPremium"]
            break
    assert isinstance(descriptor, property)

def test_regular_members_has_TrialStartDate():
    assert hasattr(Regular_Members, "TrialStartDate")
    descriptor = None
    for klass in Regular_Members.__mro__:
        if "TrialStartDate" in klass.__dict__:
            descriptor = klass.__dict__["TrialStartDate"]
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
    assert "MembershipStartDate" in params, "Missing parameter 'MembershipStartDate'"
    assert "PromoCode" in params, "Missing parameter 'PromoCode'"

def test_premium_members_has_MembershipEndDate():
    assert hasattr(Premium_Members, "MembershipEndDate")
    descriptor = None
    for klass in Premium_Members.__mro__:
        if "MembershipEndDate" in klass.__dict__:
            descriptor = klass.__dict__["MembershipEndDate"]
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

def test_premium_members_has_PromoCode():
    assert hasattr(Premium_Members, "PromoCode")
    descriptor = None
    for klass in Premium_Members.__mro__:
        if "PromoCode" in klass.__dict__:
            descriptor = klass.__dict__["PromoCode"]
            break
    assert isinstance(descriptor, property)



def test_username_is_not_abstract():
    assert not inspect.isabstract(UserName)


def test_username_constructor_exists():
    assert callable(UserName.__init__)


def test_username_constructor_args():
    sig = inspect.signature(UserName.__init__)
    params = list(sig.parameters.keys())
    assert "FirstName" in params, "Missing parameter 'FirstName'"
    assert "LastName" in params, "Missing parameter 'LastName'"

def test_username_has_FirstName():
    assert hasattr(UserName, "FirstName")
    descriptor = None
    for klass in UserName.__mro__:
        if "FirstName" in klass.__dict__:
            descriptor = klass.__dict__["FirstName"]
            break
    assert isinstance(descriptor, property)

def test_username_has_LastName():
    assert hasattr(UserName, "LastName")
    descriptor = None
    for klass in UserName.__mro__:
        if "LastName" in klass.__dict__:
            descriptor = klass.__dict__["LastName"]
            break
    assert isinstance(descriptor, property)



def test_user_account_is_not_abstract():
    assert not inspect.isabstract(User_Account)


def test_user_account_constructor_exists():
    assert callable(User_Account.__init__)


def test_user_account_constructor_args():
    sig = inspect.signature(User_Account.__init__)
    params = list(sig.parameters.keys())
    assert "FullName" in params, "Missing parameter 'FullName'"
    assert "DateOfBirth" in params, "Missing parameter 'DateOfBirth'"
    assert "RegDate" in params, "Missing parameter 'RegDate'"
    assert "UserAddress" in params, "Missing parameter 'UserAddress'"
    assert "UserID" in params, "Missing parameter 'UserID'"
    assert "Email" in params, "Missing parameter 'Email'"

def test_user_account_has_FullName():
    assert hasattr(User_Account, "FullName")
    descriptor = None
    for klass in User_Account.__mro__:
        if "FullName" in klass.__dict__:
            descriptor = klass.__dict__["FullName"]
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

def test_user_account_has_UserAddress():
    assert hasattr(User_Account, "UserAddress")
    descriptor = None
    for klass in User_Account.__mro__:
        if "UserAddress" in klass.__dict__:
            descriptor = klass.__dict__["UserAddress"]
            break
    assert isinstance(descriptor, property)

def test_user_account_has_UserID():
    assert hasattr(User_Account, "UserID")
    descriptor = None
    for klass in User_Account.__mro__:
        if "UserID" in klass.__dict__:
            descriptor = klass.__dict__["UserID"]
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
    VendorID=
        st.integers(),
    Name=
        safe_text,
    Email=
        safe_text,
    Address=
        safe_text
)
UserAddress_strategy = st.builds(
    UserAddress,
    StreetName=
        safe_text,
    StreetNum=
        st.integers(),
    PostCode=
        safe_text,
    City=
        safe_text
)
Promos_strategy = st.builds(
    Promos,
    PromoCode=
        safe_text,
    StartDate=
        safe_text,
    Discount=
        safe_text,
    EndDate=
        safe_text,
    Name=
        safe_text
)
Product_strategy = st.builds(
    Product,
    InventoryMinQuantity=
        st.integers(),
    Description=
        safe_text,
    VendorID=
        st.integers(),
    InventoryQuantity=
        st.integers(),
    ProductID=
        st.integers()
)
OrderProcess_strategy = st.builds(
    OrderProcess,
    OrderPickUp=
        st.integers(),
    UserID=
        st.integers(),
    Total=
        safe_text,
    PromoCode=
        safe_text,
    MemberShipPayment=
        st.integers(),
    IsMember=
        st.integers(),
    OrderID=
        st.integers()
)
ShoppingCart_strategy = st.builds(
    ShoppingCart,
    Promo=
        st.none(),
    ShoppingCartID=
        st.integers(),
    Quantity=
        st.integers(),
    UserID=
        safe_text,
    OrderID=
        st.integers(),
    Total=
        safe_text,
    ProductID=
        st.integers()
)
Regular_Members_strategy = st.builds(
    Regular_Members,
    TriedPremium=
        st.integers(),
    TrialStartDate=
        safe_text
)
Premium_Members_strategy = st.builds(
    Premium_Members,
    MembershipEndDate=
        safe_text,
    MembershipStartDate=
        safe_text,
    PromoCode=
        safe_text
)
UserName_strategy = st.builds(
    UserName,
    FirstName=
        safe_text,
    LastName=
        safe_text
)
User_Account_strategy = st.builds(
    User_Account,
    FullName=
        safe_text,
    DateOfBirth=
        safe_text,
    RegDate=
        safe_text,
    UserAddress=
        safe_text,
    UserID=
        safe_text,
    Email=
        safe_text
)

@given(instance=Vendor_strategy)
@settings(max_examples=50)
def test_vendor_instantiation(instance):
    assert isinstance(instance, Vendor)

@given(instance=Vendor_strategy)
def test_vendor_Contact_Number_type(instance):
    assert isinstance(instance.Contact_Number, int)


@given(instance=Vendor_strategy)
def test_vendor_Contact_Number_setter(instance):
    original = instance.Contact_Number
    instance.Contact_Number = original
    assert instance.Contact_Number == original

@given(instance=Vendor_strategy)
def test_vendor_VendorID_type(instance):
    assert isinstance(instance.VendorID, int)


@given(instance=Vendor_strategy)
def test_vendor_VendorID_setter(instance):
    original = instance.VendorID
    instance.VendorID = original
    assert instance.VendorID == original

@given(instance=Vendor_strategy)
def test_vendor_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=Vendor_strategy)
def test_vendor_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Vendor_strategy)
def test_vendor_Email_type(instance):
    assert isinstance(instance.Email, str)


@given(instance=Vendor_strategy)
def test_vendor_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original

@given(instance=Vendor_strategy)
def test_vendor_Address_type(instance):
    assert isinstance(instance.Address, str)


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
def test_useraddress_StreetName_type(instance):
    assert isinstance(instance.StreetName, str)


@given(instance=UserAddress_strategy)
def test_useraddress_StreetName_setter(instance):
    original = instance.StreetName
    instance.StreetName = original
    assert instance.StreetName == original

@given(instance=UserAddress_strategy)
def test_useraddress_StreetNum_type(instance):
    assert isinstance(instance.StreetNum, int)


@given(instance=UserAddress_strategy)
def test_useraddress_StreetNum_setter(instance):
    original = instance.StreetNum
    instance.StreetNum = original
    assert instance.StreetNum == original

@given(instance=UserAddress_strategy)
def test_useraddress_PostCode_type(instance):
    assert isinstance(instance.PostCode, str)


@given(instance=UserAddress_strategy)
def test_useraddress_PostCode_setter(instance):
    original = instance.PostCode
    instance.PostCode = original
    assert instance.PostCode == original

@given(instance=UserAddress_strategy)
def test_useraddress_City_type(instance):
    assert isinstance(instance.City, str)


@given(instance=UserAddress_strategy)
def test_useraddress_City_setter(instance):
    original = instance.City
    instance.City = original
    assert instance.City == original

@given(instance=Promos_strategy)
@settings(max_examples=50)
def test_promos_instantiation(instance):
    assert isinstance(instance, Promos)

@given(instance=Promos_strategy)
def test_promos_PromoCode_type(instance):
    assert isinstance(instance.PromoCode, str)


@given(instance=Promos_strategy)
def test_promos_PromoCode_setter(instance):
    original = instance.PromoCode
    instance.PromoCode = original
    assert instance.PromoCode == original

@given(instance=Promos_strategy)
def test_promos_StartDate_type(instance):
    assert isinstance(instance.StartDate, str)


@given(instance=Promos_strategy)
def test_promos_StartDate_setter(instance):
    original = instance.StartDate
    instance.StartDate = original
    assert instance.StartDate == original

@given(instance=Promos_strategy)
def test_promos_Discount_type(instance):
    assert isinstance(instance.Discount, str)


@given(instance=Promos_strategy)
def test_promos_Discount_setter(instance):
    original = instance.Discount
    instance.Discount = original
    assert instance.Discount == original

@given(instance=Promos_strategy)
def test_promos_EndDate_type(instance):
    assert isinstance(instance.EndDate, str)


@given(instance=Promos_strategy)
def test_promos_EndDate_setter(instance):
    original = instance.EndDate
    instance.EndDate = original
    assert instance.EndDate == original

@given(instance=Promos_strategy)
def test_promos_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=Promos_strategy)
def test_promos_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Product_strategy)
@settings(max_examples=50)
def test_product_instantiation(instance):
    assert isinstance(instance, Product)

@given(instance=Product_strategy)
def test_product_InventoryMinQuantity_type(instance):
    assert isinstance(instance.InventoryMinQuantity, int)


@given(instance=Product_strategy)
def test_product_InventoryMinQuantity_setter(instance):
    original = instance.InventoryMinQuantity
    instance.InventoryMinQuantity = original
    assert instance.InventoryMinQuantity == original

@given(instance=Product_strategy)
def test_product_Description_type(instance):
    assert isinstance(instance.Description, str)


@given(instance=Product_strategy)
def test_product_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original

@given(instance=Product_strategy)
def test_product_VendorID_type(instance):
    assert isinstance(instance.VendorID, int)


@given(instance=Product_strategy)
def test_product_VendorID_setter(instance):
    original = instance.VendorID
    instance.VendorID = original
    assert instance.VendorID == original

@given(instance=Product_strategy)
def test_product_InventoryQuantity_type(instance):
    assert isinstance(instance.InventoryQuantity, int)


@given(instance=Product_strategy)
def test_product_InventoryQuantity_setter(instance):
    original = instance.InventoryQuantity
    instance.InventoryQuantity = original
    assert instance.InventoryQuantity == original

@given(instance=Product_strategy)
def test_product_ProductID_type(instance):
    assert isinstance(instance.ProductID, int)


@given(instance=Product_strategy)
def test_product_ProductID_setter(instance):
    original = instance.ProductID
    instance.ProductID = original
    assert instance.ProductID == original

@given(instance=OrderProcess_strategy)
@settings(max_examples=50)
def test_orderprocess_instantiation(instance):
    assert isinstance(instance, OrderProcess)

@given(instance=OrderProcess_strategy)
def test_orderprocess_OrderPickUp_type(instance):
    assert isinstance(instance.OrderPickUp, int)


@given(instance=OrderProcess_strategy)
def test_orderprocess_OrderPickUp_setter(instance):
    original = instance.OrderPickUp
    instance.OrderPickUp = original
    assert instance.OrderPickUp == original

@given(instance=OrderProcess_strategy)
def test_orderprocess_UserID_type(instance):
    assert isinstance(instance.UserID, int)


@given(instance=OrderProcess_strategy)
def test_orderprocess_UserID_setter(instance):
    original = instance.UserID
    instance.UserID = original
    assert instance.UserID == original

@given(instance=OrderProcess_strategy)
def test_orderprocess_Total_type(instance):
    assert isinstance(instance.Total, str)


@given(instance=OrderProcess_strategy)
def test_orderprocess_Total_setter(instance):
    original = instance.Total
    instance.Total = original
    assert instance.Total == original

@given(instance=OrderProcess_strategy)
def test_orderprocess_PromoCode_type(instance):
    assert isinstance(instance.PromoCode, str)


@given(instance=OrderProcess_strategy)
def test_orderprocess_PromoCode_setter(instance):
    original = instance.PromoCode
    instance.PromoCode = original
    assert instance.PromoCode == original

@given(instance=OrderProcess_strategy)
def test_orderprocess_MemberShipPayment_type(instance):
    assert isinstance(instance.MemberShipPayment, int)


@given(instance=OrderProcess_strategy)
def test_orderprocess_MemberShipPayment_setter(instance):
    original = instance.MemberShipPayment
    instance.MemberShipPayment = original
    assert instance.MemberShipPayment == original

@given(instance=OrderProcess_strategy)
def test_orderprocess_IsMember_type(instance):
    assert isinstance(instance.IsMember, int)


@given(instance=OrderProcess_strategy)
def test_orderprocess_IsMember_setter(instance):
    original = instance.IsMember
    instance.IsMember = original
    assert instance.IsMember == original

@given(instance=OrderProcess_strategy)
def test_orderprocess_OrderID_type(instance):
    assert isinstance(instance.OrderID, int)


@given(instance=OrderProcess_strategy)
def test_orderprocess_OrderID_setter(instance):
    original = instance.OrderID
    instance.OrderID = original
    assert instance.OrderID == original

@given(instance=ShoppingCart_strategy)
@settings(max_examples=50)
def test_shoppingcart_instantiation(instance):
    assert isinstance(instance, ShoppingCart)

@given(instance=ShoppingCart_strategy)
def test_shoppingcart_Promo_type(instance):
    assert isinstance(instance.Promo, promos)


@given(instance=ShoppingCart_strategy)
def test_shoppingcart_Promo_setter(instance):
    original = instance.Promo
    instance.Promo = original
    assert instance.Promo == original

@given(instance=ShoppingCart_strategy)
def test_shoppingcart_ShoppingCartID_type(instance):
    assert isinstance(instance.ShoppingCartID, int)


@given(instance=ShoppingCart_strategy)
def test_shoppingcart_ShoppingCartID_setter(instance):
    original = instance.ShoppingCartID
    instance.ShoppingCartID = original
    assert instance.ShoppingCartID == original

@given(instance=ShoppingCart_strategy)
def test_shoppingcart_Quantity_type(instance):
    assert isinstance(instance.Quantity, int)


@given(instance=ShoppingCart_strategy)
def test_shoppingcart_Quantity_setter(instance):
    original = instance.Quantity
    instance.Quantity = original
    assert instance.Quantity == original

@given(instance=ShoppingCart_strategy)
def test_shoppingcart_UserID_type(instance):
    assert isinstance(instance.UserID, str)


@given(instance=ShoppingCart_strategy)
def test_shoppingcart_UserID_setter(instance):
    original = instance.UserID
    instance.UserID = original
    assert instance.UserID == original

@given(instance=ShoppingCart_strategy)
def test_shoppingcart_OrderID_type(instance):
    assert isinstance(instance.OrderID, int)


@given(instance=ShoppingCart_strategy)
def test_shoppingcart_OrderID_setter(instance):
    original = instance.OrderID
    instance.OrderID = original
    assert instance.OrderID == original

@given(instance=ShoppingCart_strategy)
def test_shoppingcart_Total_type(instance):
    assert isinstance(instance.Total, str)


@given(instance=ShoppingCart_strategy)
def test_shoppingcart_Total_setter(instance):
    original = instance.Total
    instance.Total = original
    assert instance.Total == original

@given(instance=ShoppingCart_strategy)
def test_shoppingcart_ProductID_type(instance):
    assert isinstance(instance.ProductID, int)


@given(instance=ShoppingCart_strategy)
def test_shoppingcart_ProductID_setter(instance):
    original = instance.ProductID
    instance.ProductID = original
    assert instance.ProductID == original

@given(instance=Regular_Members_strategy)
@settings(max_examples=50)
def test_regular_members_instantiation(instance):
    assert isinstance(instance, Regular_Members)

@given(instance=Regular_Members_strategy)
def test_regular_members_TriedPremium_type(instance):
    assert isinstance(instance.TriedPremium, int)


@given(instance=Regular_Members_strategy)
def test_regular_members_TriedPremium_setter(instance):
    original = instance.TriedPremium
    instance.TriedPremium = original
    assert instance.TriedPremium == original

@given(instance=Regular_Members_strategy)
def test_regular_members_TrialStartDate_type(instance):
    assert isinstance(instance.TrialStartDate, str)


@given(instance=Regular_Members_strategy)
def test_regular_members_TrialStartDate_setter(instance):
    original = instance.TrialStartDate
    instance.TrialStartDate = original
    assert instance.TrialStartDate == original

@given(instance=Premium_Members_strategy)
@settings(max_examples=50)
def test_premium_members_instantiation(instance):
    assert isinstance(instance, Premium_Members)

@given(instance=Premium_Members_strategy)
def test_premium_members_MembershipEndDate_type(instance):
    assert isinstance(instance.MembershipEndDate, str)


@given(instance=Premium_Members_strategy)
def test_premium_members_MembershipEndDate_setter(instance):
    original = instance.MembershipEndDate
    instance.MembershipEndDate = original
    assert instance.MembershipEndDate == original

@given(instance=Premium_Members_strategy)
def test_premium_members_MembershipStartDate_type(instance):
    assert isinstance(instance.MembershipStartDate, str)


@given(instance=Premium_Members_strategy)
def test_premium_members_MembershipStartDate_setter(instance):
    original = instance.MembershipStartDate
    instance.MembershipStartDate = original
    assert instance.MembershipStartDate == original

@given(instance=Premium_Members_strategy)
def test_premium_members_PromoCode_type(instance):
    assert isinstance(instance.PromoCode, str)


@given(instance=Premium_Members_strategy)
def test_premium_members_PromoCode_setter(instance):
    original = instance.PromoCode
    instance.PromoCode = original
    assert instance.PromoCode == original

@given(instance=UserName_strategy)
@settings(max_examples=50)
def test_username_instantiation(instance):
    assert isinstance(instance, UserName)

@given(instance=UserName_strategy)
def test_username_FirstName_type(instance):
    assert isinstance(instance.FirstName, str)


@given(instance=UserName_strategy)
def test_username_FirstName_setter(instance):
    original = instance.FirstName
    instance.FirstName = original
    assert instance.FirstName == original

@given(instance=UserName_strategy)
def test_username_LastName_type(instance):
    assert isinstance(instance.LastName, str)


@given(instance=UserName_strategy)
def test_username_LastName_setter(instance):
    original = instance.LastName
    instance.LastName = original
    assert instance.LastName == original

@given(instance=User_Account_strategy)
@settings(max_examples=50)
def test_user_account_instantiation(instance):
    assert isinstance(instance, User_Account)

@given(instance=User_Account_strategy)
def test_user_account_FullName_type(instance):
    assert isinstance(instance.FullName, str)


@given(instance=User_Account_strategy)
def test_user_account_FullName_setter(instance):
    original = instance.FullName
    instance.FullName = original
    assert instance.FullName == original

@given(instance=User_Account_strategy)
def test_user_account_DateOfBirth_type(instance):
    assert isinstance(instance.DateOfBirth, str)


@given(instance=User_Account_strategy)
def test_user_account_DateOfBirth_setter(instance):
    original = instance.DateOfBirth
    instance.DateOfBirth = original
    assert instance.DateOfBirth == original

@given(instance=User_Account_strategy)
def test_user_account_RegDate_type(instance):
    assert isinstance(instance.RegDate, str)


@given(instance=User_Account_strategy)
def test_user_account_RegDate_setter(instance):
    original = instance.RegDate
    instance.RegDate = original
    assert instance.RegDate == original

@given(instance=User_Account_strategy)
def test_user_account_UserAddress_type(instance):
    assert isinstance(instance.UserAddress, str)


@given(instance=User_Account_strategy)
def test_user_account_UserAddress_setter(instance):
    original = instance.UserAddress
    instance.UserAddress = original
    assert instance.UserAddress == original

@given(instance=User_Account_strategy)
def test_user_account_UserID_type(instance):
    assert isinstance(instance.UserID, str)


@given(instance=User_Account_strategy)
def test_user_account_UserID_setter(instance):
    original = instance.UserID
    instance.UserID = original
    assert instance.UserID == original

@given(instance=User_Account_strategy)
def test_user_account_Email_type(instance):
    assert isinstance(instance.Email, str)


@given(instance=User_Account_strategy)
def test_user_account_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original
