import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Customer,
    FlashSale,
    BaseDateInformation,
    Role,
    User,
    Product,
    Order,
    OnlineShop,
    Category,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "CustomerName" in params, "Missing parameter 'CustomerName'"
    assert "Gender" in params, "Missing parameter 'Gender'"
    assert "Phone" in params, "Missing parameter 'Phone'"
    assert "CustomerID" in params, "Missing parameter 'CustomerID'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "Address" in params, "Missing parameter 'Address'"

def test_customer_has_CustomerName():
    assert hasattr(Customer, "CustomerName")
    descriptor = None
    for klass in Customer.__mro__:
        if "CustomerName" in klass.__dict__:
            descriptor = klass.__dict__["CustomerName"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Gender():
    assert hasattr(Customer, "Gender")
    descriptor = None
    for klass in Customer.__mro__:
        if "Gender" in klass.__dict__:
            descriptor = klass.__dict__["Gender"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Phone():
    assert hasattr(Customer, "Phone")
    descriptor = None
    for klass in Customer.__mro__:
        if "Phone" in klass.__dict__:
            descriptor = klass.__dict__["Phone"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_CustomerID():
    assert hasattr(Customer, "CustomerID")
    descriptor = None
    for klass in Customer.__mro__:
        if "CustomerID" in klass.__dict__:
            descriptor = klass.__dict__["CustomerID"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Email():
    assert hasattr(Customer, "Email")
    descriptor = None
    for klass in Customer.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Address():
    assert hasattr(Customer, "Address")
    descriptor = None
    for klass in Customer.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)



def test_flashsale_is_not_abstract():
    assert not inspect.isabstract(FlashSale)


def test_flashsale_constructor_exists():
    assert callable(FlashSale.__init__)


def test_flashsale_constructor_args():
    sig = inspect.signature(FlashSale.__init__)
    params = list(sig.parameters.keys())
    assert "OnlineShopID" in params, "Missing parameter 'OnlineShopID'"
    assert "FlashSaleID" in params, "Missing parameter 'FlashSaleID'"
    assert "FlashSaleName" in params, "Missing parameter 'FlashSaleName'"
    assert "Description" in params, "Missing parameter 'Description'"
    assert "DiscountAmount" in params, "Missing parameter 'DiscountAmount'"
    assert "DiscountPercent" in params, "Missing parameter 'DiscountPercent'"

def test_flashsale_has_OnlineShopID():
    assert hasattr(FlashSale, "OnlineShopID")
    descriptor = None
    for klass in FlashSale.__mro__:
        if "OnlineShopID" in klass.__dict__:
            descriptor = klass.__dict__["OnlineShopID"]
            break
    assert isinstance(descriptor, property)

def test_flashsale_has_FlashSaleID():
    assert hasattr(FlashSale, "FlashSaleID")
    descriptor = None
    for klass in FlashSale.__mro__:
        if "FlashSaleID" in klass.__dict__:
            descriptor = klass.__dict__["FlashSaleID"]
            break
    assert isinstance(descriptor, property)

def test_flashsale_has_FlashSaleName():
    assert hasattr(FlashSale, "FlashSaleName")
    descriptor = None
    for klass in FlashSale.__mro__:
        if "FlashSaleName" in klass.__dict__:
            descriptor = klass.__dict__["FlashSaleName"]
            break
    assert isinstance(descriptor, property)

def test_flashsale_has_Description():
    assert hasattr(FlashSale, "Description")
    descriptor = None
    for klass in FlashSale.__mro__:
        if "Description" in klass.__dict__:
            descriptor = klass.__dict__["Description"]
            break
    assert isinstance(descriptor, property)

def test_flashsale_has_DiscountAmount():
    assert hasattr(FlashSale, "DiscountAmount")
    descriptor = None
    for klass in FlashSale.__mro__:
        if "DiscountAmount" in klass.__dict__:
            descriptor = klass.__dict__["DiscountAmount"]
            break
    assert isinstance(descriptor, property)

def test_flashsale_has_DiscountPercent():
    assert hasattr(FlashSale, "DiscountPercent")
    descriptor = None
    for klass in FlashSale.__mro__:
        if "DiscountPercent" in klass.__dict__:
            descriptor = klass.__dict__["DiscountPercent"]
            break
    assert isinstance(descriptor, property)



def test_basedateinformation_is_not_abstract():
    assert not inspect.isabstract(BaseDateInformation)


def test_basedateinformation_constructor_exists():
    assert callable(BaseDateInformation.__init__)


def test_basedateinformation_constructor_args():
    sig = inspect.signature(BaseDateInformation.__init__)
    params = list(sig.parameters.keys())
    assert "LastModifedBy" in params, "Missing parameter 'LastModifedBy'"
    assert "LastModifedDate" in params, "Missing parameter 'LastModifedDate'"
    assert "CreateDate" in params, "Missing parameter 'CreateDate'"
    assert "CreatedBy" in params, "Missing parameter 'CreatedBy'"

def test_basedateinformation_has_LastModifedBy():
    assert hasattr(BaseDateInformation, "LastModifedBy")
    descriptor = None
    for klass in BaseDateInformation.__mro__:
        if "LastModifedBy" in klass.__dict__:
            descriptor = klass.__dict__["LastModifedBy"]
            break
    assert isinstance(descriptor, property)

def test_basedateinformation_has_LastModifedDate():
    assert hasattr(BaseDateInformation, "LastModifedDate")
    descriptor = None
    for klass in BaseDateInformation.__mro__:
        if "LastModifedDate" in klass.__dict__:
            descriptor = klass.__dict__["LastModifedDate"]
            break
    assert isinstance(descriptor, property)

def test_basedateinformation_has_CreateDate():
    assert hasattr(BaseDateInformation, "CreateDate")
    descriptor = None
    for klass in BaseDateInformation.__mro__:
        if "CreateDate" in klass.__dict__:
            descriptor = klass.__dict__["CreateDate"]
            break
    assert isinstance(descriptor, property)

def test_basedateinformation_has_CreatedBy():
    assert hasattr(BaseDateInformation, "CreatedBy")
    descriptor = None
    for klass in BaseDateInformation.__mro__:
        if "CreatedBy" in klass.__dict__:
            descriptor = klass.__dict__["CreatedBy"]
            break
    assert isinstance(descriptor, property)



def test_role_is_not_abstract():
    assert not inspect.isabstract(Role)


def test_role_constructor_exists():
    assert callable(Role.__init__)


def test_role_constructor_args():
    sig = inspect.signature(Role.__init__)
    params = list(sig.parameters.keys())
    assert "Description" in params, "Missing parameter 'Description'"
    assert "isActive" in params, "Missing parameter 'isActive'"
    assert "RoleName" in params, "Missing parameter 'RoleName'"
    assert "RoleID" in params, "Missing parameter 'RoleID'"

def test_role_has_Description():
    assert hasattr(Role, "Description")
    descriptor = None
    for klass in Role.__mro__:
        if "Description" in klass.__dict__:
            descriptor = klass.__dict__["Description"]
            break
    assert isinstance(descriptor, property)

def test_role_has_isActive():
    assert hasattr(Role, "isActive")
    descriptor = None
    for klass in Role.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)

def test_role_has_RoleName():
    assert hasattr(Role, "RoleName")
    descriptor = None
    for klass in Role.__mro__:
        if "RoleName" in klass.__dict__:
            descriptor = klass.__dict__["RoleName"]
            break
    assert isinstance(descriptor, property)

def test_role_has_RoleID():
    assert hasattr(Role, "RoleID")
    descriptor = None
    for klass in Role.__mro__:
        if "RoleID" in klass.__dict__:
            descriptor = klass.__dict__["RoleID"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "RegisterDate" in params, "Missing parameter 'RegisterDate'"
    assert "UserID" in params, "Missing parameter 'UserID'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Username" in params, "Missing parameter 'Username'"
    assert "RoleID" in params, "Missing parameter 'RoleID'"
    assert "isActive" in params, "Missing parameter 'isActive'"

def test_user_has_RegisterDate():
    assert hasattr(User, "RegisterDate")
    descriptor = None
    for klass in User.__mro__:
        if "RegisterDate" in klass.__dict__:
            descriptor = klass.__dict__["RegisterDate"]
            break
    assert isinstance(descriptor, property)

def test_user_has_UserID():
    assert hasattr(User, "UserID")
    descriptor = None
    for klass in User.__mro__:
        if "UserID" in klass.__dict__:
            descriptor = klass.__dict__["UserID"]
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

def test_user_has_Username():
    assert hasattr(User, "Username")
    descriptor = None
    for klass in User.__mro__:
        if "Username" in klass.__dict__:
            descriptor = klass.__dict__["Username"]
            break
    assert isinstance(descriptor, property)

def test_user_has_RoleID():
    assert hasattr(User, "RoleID")
    descriptor = None
    for klass in User.__mro__:
        if "RoleID" in klass.__dict__:
            descriptor = klass.__dict__["RoleID"]
            break
    assert isinstance(descriptor, property)

def test_user_has_isActive():
    assert hasattr(User, "isActive")
    descriptor = None
    for klass in User.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)



def test_product_is_not_abstract():
    assert not inspect.isabstract(Product)


def test_product_constructor_exists():
    assert callable(Product.__init__)


def test_product_constructor_args():
    sig = inspect.signature(Product.__init__)
    params = list(sig.parameters.keys())
    assert "Price" in params, "Missing parameter 'Price'"
    assert "Image" in params, "Missing parameter 'Image'"
    assert "CategoryID" in params, "Missing parameter 'CategoryID'"
    assert "OnlineShopID" in params, "Missing parameter 'OnlineShopID'"
    assert "ProductID" in params, "Missing parameter 'ProductID'"
    assert "ProductName" in params, "Missing parameter 'ProductName'"
    assert "isActive" in params, "Missing parameter 'isActive'"
    assert "Description" in params, "Missing parameter 'Description'"

def test_product_has_Price():
    assert hasattr(Product, "Price")
    descriptor = None
    for klass in Product.__mro__:
        if "Price" in klass.__dict__:
            descriptor = klass.__dict__["Price"]
            break
    assert isinstance(descriptor, property)

def test_product_has_Image():
    assert hasattr(Product, "Image")
    descriptor = None
    for klass in Product.__mro__:
        if "Image" in klass.__dict__:
            descriptor = klass.__dict__["Image"]
            break
    assert isinstance(descriptor, property)

def test_product_has_CategoryID():
    assert hasattr(Product, "CategoryID")
    descriptor = None
    for klass in Product.__mro__:
        if "CategoryID" in klass.__dict__:
            descriptor = klass.__dict__["CategoryID"]
            break
    assert isinstance(descriptor, property)

def test_product_has_OnlineShopID():
    assert hasattr(Product, "OnlineShopID")
    descriptor = None
    for klass in Product.__mro__:
        if "OnlineShopID" in klass.__dict__:
            descriptor = klass.__dict__["OnlineShopID"]
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

def test_product_has_ProductName():
    assert hasattr(Product, "ProductName")
    descriptor = None
    for klass in Product.__mro__:
        if "ProductName" in klass.__dict__:
            descriptor = klass.__dict__["ProductName"]
            break
    assert isinstance(descriptor, property)

def test_product_has_isActive():
    assert hasattr(Product, "isActive")
    descriptor = None
    for klass in Product.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
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



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "Status" in params, "Missing parameter 'Status'"
    assert "ShopOnlineID" in params, "Missing parameter 'ShopOnlineID'"
    assert "UserID" in params, "Missing parameter 'UserID'"
    assert "OrderID" in params, "Missing parameter 'OrderID'"
    assert "OrderDate" in params, "Missing parameter 'OrderDate'"
    assert "OrderCustomerID" in params, "Missing parameter 'OrderCustomerID'"
    assert "TotalDiscount" in params, "Missing parameter 'TotalDiscount'"
    assert "ReceiveCustomerID" in params, "Missing parameter 'ReceiveCustomerID'"
    assert "TotalPrice" in params, "Missing parameter 'TotalPrice'"

def test_order_has_Status():
    assert hasattr(Order, "Status")
    descriptor = None
    for klass in Order.__mro__:
        if "Status" in klass.__dict__:
            descriptor = klass.__dict__["Status"]
            break
    assert isinstance(descriptor, property)

def test_order_has_ShopOnlineID():
    assert hasattr(Order, "ShopOnlineID")
    descriptor = None
    for klass in Order.__mro__:
        if "ShopOnlineID" in klass.__dict__:
            descriptor = klass.__dict__["ShopOnlineID"]
            break
    assert isinstance(descriptor, property)

def test_order_has_UserID():
    assert hasattr(Order, "UserID")
    descriptor = None
    for klass in Order.__mro__:
        if "UserID" in klass.__dict__:
            descriptor = klass.__dict__["UserID"]
            break
    assert isinstance(descriptor, property)

def test_order_has_OrderID():
    assert hasattr(Order, "OrderID")
    descriptor = None
    for klass in Order.__mro__:
        if "OrderID" in klass.__dict__:
            descriptor = klass.__dict__["OrderID"]
            break
    assert isinstance(descriptor, property)

def test_order_has_OrderDate():
    assert hasattr(Order, "OrderDate")
    descriptor = None
    for klass in Order.__mro__:
        if "OrderDate" in klass.__dict__:
            descriptor = klass.__dict__["OrderDate"]
            break
    assert isinstance(descriptor, property)

def test_order_has_OrderCustomerID():
    assert hasattr(Order, "OrderCustomerID")
    descriptor = None
    for klass in Order.__mro__:
        if "OrderCustomerID" in klass.__dict__:
            descriptor = klass.__dict__["OrderCustomerID"]
            break
    assert isinstance(descriptor, property)

def test_order_has_TotalDiscount():
    assert hasattr(Order, "TotalDiscount")
    descriptor = None
    for klass in Order.__mro__:
        if "TotalDiscount" in klass.__dict__:
            descriptor = klass.__dict__["TotalDiscount"]
            break
    assert isinstance(descriptor, property)

def test_order_has_ReceiveCustomerID():
    assert hasattr(Order, "ReceiveCustomerID")
    descriptor = None
    for klass in Order.__mro__:
        if "ReceiveCustomerID" in klass.__dict__:
            descriptor = klass.__dict__["ReceiveCustomerID"]
            break
    assert isinstance(descriptor, property)

def test_order_has_TotalPrice():
    assert hasattr(Order, "TotalPrice")
    descriptor = None
    for klass in Order.__mro__:
        if "TotalPrice" in klass.__dict__:
            descriptor = klass.__dict__["TotalPrice"]
            break
    assert isinstance(descriptor, property)



def test_onlineshop_is_not_abstract():
    assert not inspect.isabstract(OnlineShop)


def test_onlineshop_constructor_exists():
    assert callable(OnlineShop.__init__)


def test_onlineshop_constructor_args():
    sig = inspect.signature(OnlineShop.__init__)
    params = list(sig.parameters.keys())
    assert "OnlineShopName" in params, "Missing parameter 'OnlineShopName'"
    assert "OnlineShopID" in params, "Missing parameter 'OnlineShopID'"
    assert "isActive" in params, "Missing parameter 'isActive'"
    assert "ShopCategoryID" in params, "Missing parameter 'ShopCategoryID'"

def test_onlineshop_has_OnlineShopName():
    assert hasattr(OnlineShop, "OnlineShopName")
    descriptor = None
    for klass in OnlineShop.__mro__:
        if "OnlineShopName" in klass.__dict__:
            descriptor = klass.__dict__["OnlineShopName"]
            break
    assert isinstance(descriptor, property)

def test_onlineshop_has_OnlineShopID():
    assert hasattr(OnlineShop, "OnlineShopID")
    descriptor = None
    for klass in OnlineShop.__mro__:
        if "OnlineShopID" in klass.__dict__:
            descriptor = klass.__dict__["OnlineShopID"]
            break
    assert isinstance(descriptor, property)

def test_onlineshop_has_isActive():
    assert hasattr(OnlineShop, "isActive")
    descriptor = None
    for klass in OnlineShop.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)

def test_onlineshop_has_ShopCategoryID():
    assert hasattr(OnlineShop, "ShopCategoryID")
    descriptor = None
    for klass in OnlineShop.__mro__:
        if "ShopCategoryID" in klass.__dict__:
            descriptor = klass.__dict__["ShopCategoryID"]
            break
    assert isinstance(descriptor, property)



def test_category_is_not_abstract():
    assert not inspect.isabstract(Category)


def test_category_constructor_exists():
    assert callable(Category.__init__)


def test_category_constructor_args():
    sig = inspect.signature(Category.__init__)
    params = list(sig.parameters.keys())
    assert "Description" in params, "Missing parameter 'Description'"
    assert "CategoryName" in params, "Missing parameter 'CategoryName'"
    assert "CategoryID" in params, "Missing parameter 'CategoryID'"
    assert "isActive" in params, "Missing parameter 'isActive'"

def test_category_has_Description():
    assert hasattr(Category, "Description")
    descriptor = None
    for klass in Category.__mro__:
        if "Description" in klass.__dict__:
            descriptor = klass.__dict__["Description"]
            break
    assert isinstance(descriptor, property)

def test_category_has_CategoryName():
    assert hasattr(Category, "CategoryName")
    descriptor = None
    for klass in Category.__mro__:
        if "CategoryName" in klass.__dict__:
            descriptor = klass.__dict__["CategoryName"]
            break
    assert isinstance(descriptor, property)

def test_category_has_CategoryID():
    assert hasattr(Category, "CategoryID")
    descriptor = None
    for klass in Category.__mro__:
        if "CategoryID" in klass.__dict__:
            descriptor = klass.__dict__["CategoryID"]
            break
    assert isinstance(descriptor, property)

def test_category_has_isActive():
    assert hasattr(Category, "isActive")
    descriptor = None
    for klass in Category.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
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
Customer_strategy = st.builds(
    Customer,
    CustomerName=
        safe_text,
    Gender=
        st.integers(),
    Phone=
        safe_text,
    CustomerID=
        st.integers(),
    Email=
        safe_text,
    Address=
        safe_text
)
FlashSale_strategy = st.builds(
    FlashSale,
    OnlineShopID=
        st.integers(),
    FlashSaleID=
        st.integers(),
    FlashSaleName=
        safe_text,
    Description=
        safe_text,
    DiscountAmount=
        st.integers(),
    DiscountPercent=
        st.integers()
)
BaseDateInformation_strategy = st.builds(
    BaseDateInformation,
    LastModifedBy=
        safe_text,
    LastModifedDate=
        safe_text,
    CreateDate=
        safe_text,
    CreatedBy=
        safe_text
)
Role_strategy = st.builds(
    Role,
    Description=
        safe_text,
    isActive=
        st.booleans(),
    RoleName=
        safe_text,
    RoleID=
        st.integers()
)
User_strategy = st.builds(
    User,
    RegisterDate=
        safe_text,
    UserID=
        safe_text,
    Password=
        safe_text,
    Username=
        safe_text,
    RoleID=
        st.integers(),
    isActive=
        st.booleans()
)
Product_strategy = st.builds(
    Product,
    Price=
        safe_text,
    Image=
        safe_text,
    CategoryID=
        st.integers(),
    OnlineShopID=
        st.integers(),
    ProductID=
        st.integers(),
    ProductName=
        safe_text,
    isActive=
        st.booleans(),
    Description=
        safe_text
)
Order_strategy = st.builds(
    Order,
    Status=
        st.booleans(),
    ShopOnlineID=
        st.integers(),
    UserID=
        st.integers(),
    OrderID=
        st.integers(),
    OrderDate=
        safe_text,
    OrderCustomerID=
        st.integers(),
    TotalDiscount=
        safe_text,
    ReceiveCustomerID=
        st.integers(),
    TotalPrice=
        safe_text
)
OnlineShop_strategy = st.builds(
    OnlineShop,
    OnlineShopName=
        safe_text,
    OnlineShopID=
        st.integers(),
    isActive=
        st.booleans(),
    ShopCategoryID=
        st.integers()
)
Category_strategy = st.builds(
    Category,
    Description=
        safe_text,
    CategoryName=
        safe_text,
    CategoryID=
        st.integers(),
    isActive=
        st.booleans()
)

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_CustomerName_setter(instance):
    original = instance.CustomerName
    instance.CustomerName = original
    assert instance.CustomerName == original



@given(instance=Customer_strategy)
def test_customer_Gender_setter(instance):
    original = instance.Gender
    instance.Gender = original
    assert instance.Gender == original



@given(instance=Customer_strategy)
def test_customer_Phone_setter(instance):
    original = instance.Phone
    instance.Phone = original
    assert instance.Phone == original



@given(instance=Customer_strategy)
def test_customer_CustomerID_setter(instance):
    original = instance.CustomerID
    instance.CustomerID = original
    assert instance.CustomerID == original



@given(instance=Customer_strategy)
def test_customer_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Customer_strategy)
def test_customer_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original

@given(instance=FlashSale_strategy)
@settings(max_examples=50)
def test_flashsale_instantiation(instance):
    assert isinstance(instance, FlashSale)



@given(instance=FlashSale_strategy)
def test_flashsale_OnlineShopID_setter(instance):
    original = instance.OnlineShopID
    instance.OnlineShopID = original
    assert instance.OnlineShopID == original



@given(instance=FlashSale_strategy)
def test_flashsale_FlashSaleID_setter(instance):
    original = instance.FlashSaleID
    instance.FlashSaleID = original
    assert instance.FlashSaleID == original



@given(instance=FlashSale_strategy)
def test_flashsale_FlashSaleName_setter(instance):
    original = instance.FlashSaleName
    instance.FlashSaleName = original
    assert instance.FlashSaleName == original



@given(instance=FlashSale_strategy)
def test_flashsale_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original



@given(instance=FlashSale_strategy)
def test_flashsale_DiscountAmount_setter(instance):
    original = instance.DiscountAmount
    instance.DiscountAmount = original
    assert instance.DiscountAmount == original



@given(instance=FlashSale_strategy)
def test_flashsale_DiscountPercent_setter(instance):
    original = instance.DiscountPercent
    instance.DiscountPercent = original
    assert instance.DiscountPercent == original

@given(instance=BaseDateInformation_strategy)
@settings(max_examples=50)
def test_basedateinformation_instantiation(instance):
    assert isinstance(instance, BaseDateInformation)



@given(instance=BaseDateInformation_strategy)
def test_basedateinformation_LastModifedBy_setter(instance):
    original = instance.LastModifedBy
    instance.LastModifedBy = original
    assert instance.LastModifedBy == original



@given(instance=BaseDateInformation_strategy)
def test_basedateinformation_LastModifedDate_setter(instance):
    original = instance.LastModifedDate
    instance.LastModifedDate = original
    assert instance.LastModifedDate == original



@given(instance=BaseDateInformation_strategy)
def test_basedateinformation_CreateDate_setter(instance):
    original = instance.CreateDate
    instance.CreateDate = original
    assert instance.CreateDate == original



@given(instance=BaseDateInformation_strategy)
def test_basedateinformation_CreatedBy_setter(instance):
    original = instance.CreatedBy
    instance.CreatedBy = original
    assert instance.CreatedBy == original

@given(instance=Role_strategy)
@settings(max_examples=50)
def test_role_instantiation(instance):
    assert isinstance(instance, Role)



@given(instance=Role_strategy)
def test_role_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original



@given(instance=Role_strategy)
def test_role_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original



@given(instance=Role_strategy)
def test_role_RoleName_setter(instance):
    original = instance.RoleName
    instance.RoleName = original
    assert instance.RoleName == original



@given(instance=Role_strategy)
def test_role_RoleID_setter(instance):
    original = instance.RoleID
    instance.RoleID = original
    assert instance.RoleID == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_RegisterDate_setter(instance):
    original = instance.RegisterDate
    instance.RegisterDate = original
    assert instance.RegisterDate == original



@given(instance=User_strategy)
def test_user_UserID_setter(instance):
    original = instance.UserID
    instance.UserID = original
    assert instance.UserID == original



@given(instance=User_strategy)
def test_user_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=User_strategy)
def test_user_Username_setter(instance):
    original = instance.Username
    instance.Username = original
    assert instance.Username == original



@given(instance=User_strategy)
def test_user_RoleID_setter(instance):
    original = instance.RoleID
    instance.RoleID = original
    assert instance.RoleID == original



@given(instance=User_strategy)
def test_user_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original

@given(instance=Product_strategy)
@settings(max_examples=50)
def test_product_instantiation(instance):
    assert isinstance(instance, Product)



@given(instance=Product_strategy)
def test_product_Price_setter(instance):
    original = instance.Price
    instance.Price = original
    assert instance.Price == original



@given(instance=Product_strategy)
def test_product_Image_setter(instance):
    original = instance.Image
    instance.Image = original
    assert instance.Image == original



@given(instance=Product_strategy)
def test_product_CategoryID_setter(instance):
    original = instance.CategoryID
    instance.CategoryID = original
    assert instance.CategoryID == original



@given(instance=Product_strategy)
def test_product_OnlineShopID_setter(instance):
    original = instance.OnlineShopID
    instance.OnlineShopID = original
    assert instance.OnlineShopID == original



@given(instance=Product_strategy)
def test_product_ProductID_setter(instance):
    original = instance.ProductID
    instance.ProductID = original
    assert instance.ProductID == original



@given(instance=Product_strategy)
def test_product_ProductName_setter(instance):
    original = instance.ProductName
    instance.ProductName = original
    assert instance.ProductName == original



@given(instance=Product_strategy)
def test_product_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original



@given(instance=Product_strategy)
def test_product_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original



@given(instance=Order_strategy)
def test_order_ShopOnlineID_setter(instance):
    original = instance.ShopOnlineID
    instance.ShopOnlineID = original
    assert instance.ShopOnlineID == original



@given(instance=Order_strategy)
def test_order_UserID_setter(instance):
    original = instance.UserID
    instance.UserID = original
    assert instance.UserID == original



@given(instance=Order_strategy)
def test_order_OrderID_setter(instance):
    original = instance.OrderID
    instance.OrderID = original
    assert instance.OrderID == original



@given(instance=Order_strategy)
def test_order_OrderDate_setter(instance):
    original = instance.OrderDate
    instance.OrderDate = original
    assert instance.OrderDate == original



@given(instance=Order_strategy)
def test_order_OrderCustomerID_setter(instance):
    original = instance.OrderCustomerID
    instance.OrderCustomerID = original
    assert instance.OrderCustomerID == original



@given(instance=Order_strategy)
def test_order_TotalDiscount_setter(instance):
    original = instance.TotalDiscount
    instance.TotalDiscount = original
    assert instance.TotalDiscount == original



@given(instance=Order_strategy)
def test_order_ReceiveCustomerID_setter(instance):
    original = instance.ReceiveCustomerID
    instance.ReceiveCustomerID = original
    assert instance.ReceiveCustomerID == original



@given(instance=Order_strategy)
def test_order_TotalPrice_setter(instance):
    original = instance.TotalPrice
    instance.TotalPrice = original
    assert instance.TotalPrice == original

@given(instance=OnlineShop_strategy)
@settings(max_examples=50)
def test_onlineshop_instantiation(instance):
    assert isinstance(instance, OnlineShop)



@given(instance=OnlineShop_strategy)
def test_onlineshop_OnlineShopName_setter(instance):
    original = instance.OnlineShopName
    instance.OnlineShopName = original
    assert instance.OnlineShopName == original



@given(instance=OnlineShop_strategy)
def test_onlineshop_OnlineShopID_setter(instance):
    original = instance.OnlineShopID
    instance.OnlineShopID = original
    assert instance.OnlineShopID == original



@given(instance=OnlineShop_strategy)
def test_onlineshop_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original



@given(instance=OnlineShop_strategy)
def test_onlineshop_ShopCategoryID_setter(instance):
    original = instance.ShopCategoryID
    instance.ShopCategoryID = original
    assert instance.ShopCategoryID == original

@given(instance=Category_strategy)
@settings(max_examples=50)
def test_category_instantiation(instance):
    assert isinstance(instance, Category)



@given(instance=Category_strategy)
def test_category_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original



@given(instance=Category_strategy)
def test_category_CategoryName_setter(instance):
    original = instance.CategoryName
    instance.CategoryName = original
    assert instance.CategoryName == original



@given(instance=Category_strategy)
def test_category_CategoryID_setter(instance):
    original = instance.CategoryID
    instance.CategoryID = original
    assert instance.CategoryID == original



@given(instance=Category_strategy)
def test_category_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original
