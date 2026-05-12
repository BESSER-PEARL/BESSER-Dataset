import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SubCategory,
    OrderItem,
    FavoriteItem,
    CouponCode,
    Category,
    Item,
    Order,
    User,
    BaseEntity,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_subcategory_is_not_abstract():
    assert not inspect.isabstract(SubCategory)


def test_subcategory_constructor_exists():
    assert callable(SubCategory.__init__)


def test_subcategory_constructor_args():
    sig = inspect.signature(SubCategory.__init__)
    params = list(sig.parameters.keys())
    assert "RusName" in params, "Missing parameter 'RusName'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "CategoryId" in params, "Missing parameter 'CategoryId'"

def test_subcategory_has_RusName():
    assert hasattr(SubCategory, "RusName")
    descriptor = None
    for klass in SubCategory.__mro__:
        if "RusName" in klass.__dict__:
            descriptor = klass.__dict__["RusName"]
            break
    assert isinstance(descriptor, property)

def test_subcategory_has_Name():
    assert hasattr(SubCategory, "Name")
    descriptor = None
    for klass in SubCategory.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_subcategory_has_CategoryId():
    assert hasattr(SubCategory, "CategoryId")
    descriptor = None
    for klass in SubCategory.__mro__:
        if "CategoryId" in klass.__dict__:
            descriptor = klass.__dict__["CategoryId"]
            break
    assert isinstance(descriptor, property)



def test_orderitem_is_not_abstract():
    assert not inspect.isabstract(OrderItem)


def test_orderitem_constructor_exists():
    assert callable(OrderItem.__init__)


def test_orderitem_constructor_args():
    sig = inspect.signature(OrderItem.__init__)
    params = list(sig.parameters.keys())
    assert "Price" in params, "Missing parameter 'Price'"
    assert "Amount" in params, "Missing parameter 'Amount'"
    assert "ItemId" in params, "Missing parameter 'ItemId'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "OrderId" in params, "Missing parameter 'OrderId'"

def test_orderitem_has_Price():
    assert hasattr(OrderItem, "Price")
    descriptor = None
    for klass in OrderItem.__mro__:
        if "Price" in klass.__dict__:
            descriptor = klass.__dict__["Price"]
            break
    assert isinstance(descriptor, property)

def test_orderitem_has_Amount():
    assert hasattr(OrderItem, "Amount")
    descriptor = None
    for klass in OrderItem.__mro__:
        if "Amount" in klass.__dict__:
            descriptor = klass.__dict__["Amount"]
            break
    assert isinstance(descriptor, property)

def test_orderitem_has_ItemId():
    assert hasattr(OrderItem, "ItemId")
    descriptor = None
    for klass in OrderItem.__mro__:
        if "ItemId" in klass.__dict__:
            descriptor = klass.__dict__["ItemId"]
            break
    assert isinstance(descriptor, property)

def test_orderitem_has_Name():
    assert hasattr(OrderItem, "Name")
    descriptor = None
    for klass in OrderItem.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_orderitem_has_OrderId():
    assert hasattr(OrderItem, "OrderId")
    descriptor = None
    for klass in OrderItem.__mro__:
        if "OrderId" in klass.__dict__:
            descriptor = klass.__dict__["OrderId"]
            break
    assert isinstance(descriptor, property)



def test_favoriteitem_is_not_abstract():
    assert not inspect.isabstract(FavoriteItem)


def test_favoriteitem_constructor_exists():
    assert callable(FavoriteItem.__init__)


def test_favoriteitem_constructor_args():
    sig = inspect.signature(FavoriteItem.__init__)
    params = list(sig.parameters.keys())
    assert "UserId" in params, "Missing parameter 'UserId'"
    assert "ItemId" in params, "Missing parameter 'ItemId'"

def test_favoriteitem_has_UserId():
    assert hasattr(FavoriteItem, "UserId")
    descriptor = None
    for klass in FavoriteItem.__mro__:
        if "UserId" in klass.__dict__:
            descriptor = klass.__dict__["UserId"]
            break
    assert isinstance(descriptor, property)

def test_favoriteitem_has_ItemId():
    assert hasattr(FavoriteItem, "ItemId")
    descriptor = None
    for klass in FavoriteItem.__mro__:
        if "ItemId" in klass.__dict__:
            descriptor = klass.__dict__["ItemId"]
            break
    assert isinstance(descriptor, property)



def test_couponcode_is_not_abstract():
    assert not inspect.isabstract(CouponCode)


def test_couponcode_constructor_exists():
    assert callable(CouponCode.__init__)


def test_couponcode_constructor_args():
    sig = inspect.signature(CouponCode.__init__)
    params = list(sig.parameters.keys())
    assert "ExpiryDate" in params, "Missing parameter 'ExpiryDate'"
    assert "UserId" in params, "Missing parameter 'UserId'"
    assert "Discount" in params, "Missing parameter 'Discount'"
    assert "Code" in params, "Missing parameter 'Code'"

def test_couponcode_has_ExpiryDate():
    assert hasattr(CouponCode, "ExpiryDate")
    descriptor = None
    for klass in CouponCode.__mro__:
        if "ExpiryDate" in klass.__dict__:
            descriptor = klass.__dict__["ExpiryDate"]
            break
    assert isinstance(descriptor, property)

def test_couponcode_has_UserId():
    assert hasattr(CouponCode, "UserId")
    descriptor = None
    for klass in CouponCode.__mro__:
        if "UserId" in klass.__dict__:
            descriptor = klass.__dict__["UserId"]
            break
    assert isinstance(descriptor, property)

def test_couponcode_has_Discount():
    assert hasattr(CouponCode, "Discount")
    descriptor = None
    for klass in CouponCode.__mro__:
        if "Discount" in klass.__dict__:
            descriptor = klass.__dict__["Discount"]
            break
    assert isinstance(descriptor, property)

def test_couponcode_has_Code():
    assert hasattr(CouponCode, "Code")
    descriptor = None
    for klass in CouponCode.__mro__:
        if "Code" in klass.__dict__:
            descriptor = klass.__dict__["Code"]
            break
    assert isinstance(descriptor, property)



def test_category_is_not_abstract():
    assert not inspect.isabstract(Category)


def test_category_constructor_exists():
    assert callable(Category.__init__)


def test_category_constructor_args():
    sig = inspect.signature(Category.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "RusName" in params, "Missing parameter 'RusName'"

def test_category_has_Name():
    assert hasattr(Category, "Name")
    descriptor = None
    for klass in Category.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_category_has_RusName():
    assert hasattr(Category, "RusName")
    descriptor = None
    for klass in Category.__mro__:
        if "RusName" in klass.__dict__:
            descriptor = klass.__dict__["RusName"]
            break
    assert isinstance(descriptor, property)



def test_item_is_not_abstract():
    assert not inspect.isabstract(Item)


def test_item_constructor_exists():
    assert callable(Item.__init__)


def test_item_constructor_args():
    sig = inspect.signature(Item.__init__)
    params = list(sig.parameters.keys())
    assert "Price" in params, "Missing parameter 'Price'"
    assert "Brand" in params, "Missing parameter 'Brand'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Discount" in params, "Missing parameter 'Discount'"
    assert "Sex" in params, "Missing parameter 'Sex'"
    assert "Description" in params, "Missing parameter 'Description'"
    assert "MinPreviewImagePath" in params, "Missing parameter 'MinPreviewImagePath'"
    assert "ImagePath2" in params, "Missing parameter 'ImagePath2'"
    assert "PreviewImagePath" in params, "Missing parameter 'PreviewImagePath'"
    assert "ImagePath3" in params, "Missing parameter 'ImagePath3'"
    assert "Color" in params, "Missing parameter 'Color'"
    assert "Size" in params, "Missing parameter 'Size'"
    assert "Amount" in params, "Missing parameter 'Amount'"
    assert "ImagePath1" in params, "Missing parameter 'ImagePath1'"
    assert "Status" in params, "Missing parameter 'Status'"
    assert "CategoryId" in params, "Missing parameter 'CategoryId'"
    assert "SubCategoryId" in params, "Missing parameter 'SubCategoryId'"

def test_item_has_Price():
    assert hasattr(Item, "Price")
    descriptor = None
    for klass in Item.__mro__:
        if "Price" in klass.__dict__:
            descriptor = klass.__dict__["Price"]
            break
    assert isinstance(descriptor, property)

def test_item_has_Brand():
    assert hasattr(Item, "Brand")
    descriptor = None
    for klass in Item.__mro__:
        if "Brand" in klass.__dict__:
            descriptor = klass.__dict__["Brand"]
            break
    assert isinstance(descriptor, property)

def test_item_has_Name():
    assert hasattr(Item, "Name")
    descriptor = None
    for klass in Item.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_item_has_Discount():
    assert hasattr(Item, "Discount")
    descriptor = None
    for klass in Item.__mro__:
        if "Discount" in klass.__dict__:
            descriptor = klass.__dict__["Discount"]
            break
    assert isinstance(descriptor, property)

def test_item_has_Sex():
    assert hasattr(Item, "Sex")
    descriptor = None
    for klass in Item.__mro__:
        if "Sex" in klass.__dict__:
            descriptor = klass.__dict__["Sex"]
            break
    assert isinstance(descriptor, property)

def test_item_has_Description():
    assert hasattr(Item, "Description")
    descriptor = None
    for klass in Item.__mro__:
        if "Description" in klass.__dict__:
            descriptor = klass.__dict__["Description"]
            break
    assert isinstance(descriptor, property)

def test_item_has_MinPreviewImagePath():
    assert hasattr(Item, "MinPreviewImagePath")
    descriptor = None
    for klass in Item.__mro__:
        if "MinPreviewImagePath" in klass.__dict__:
            descriptor = klass.__dict__["MinPreviewImagePath"]
            break
    assert isinstance(descriptor, property)

def test_item_has_ImagePath2():
    assert hasattr(Item, "ImagePath2")
    descriptor = None
    for klass in Item.__mro__:
        if "ImagePath2" in klass.__dict__:
            descriptor = klass.__dict__["ImagePath2"]
            break
    assert isinstance(descriptor, property)

def test_item_has_PreviewImagePath():
    assert hasattr(Item, "PreviewImagePath")
    descriptor = None
    for klass in Item.__mro__:
        if "PreviewImagePath" in klass.__dict__:
            descriptor = klass.__dict__["PreviewImagePath"]
            break
    assert isinstance(descriptor, property)

def test_item_has_ImagePath3():
    assert hasattr(Item, "ImagePath3")
    descriptor = None
    for klass in Item.__mro__:
        if "ImagePath3" in klass.__dict__:
            descriptor = klass.__dict__["ImagePath3"]
            break
    assert isinstance(descriptor, property)

def test_item_has_Color():
    assert hasattr(Item, "Color")
    descriptor = None
    for klass in Item.__mro__:
        if "Color" in klass.__dict__:
            descriptor = klass.__dict__["Color"]
            break
    assert isinstance(descriptor, property)

def test_item_has_Size():
    assert hasattr(Item, "Size")
    descriptor = None
    for klass in Item.__mro__:
        if "Size" in klass.__dict__:
            descriptor = klass.__dict__["Size"]
            break
    assert isinstance(descriptor, property)

def test_item_has_Amount():
    assert hasattr(Item, "Amount")
    descriptor = None
    for klass in Item.__mro__:
        if "Amount" in klass.__dict__:
            descriptor = klass.__dict__["Amount"]
            break
    assert isinstance(descriptor, property)

def test_item_has_ImagePath1():
    assert hasattr(Item, "ImagePath1")
    descriptor = None
    for klass in Item.__mro__:
        if "ImagePath1" in klass.__dict__:
            descriptor = klass.__dict__["ImagePath1"]
            break
    assert isinstance(descriptor, property)

def test_item_has_Status():
    assert hasattr(Item, "Status")
    descriptor = None
    for klass in Item.__mro__:
        if "Status" in klass.__dict__:
            descriptor = klass.__dict__["Status"]
            break
    assert isinstance(descriptor, property)

def test_item_has_CategoryId():
    assert hasattr(Item, "CategoryId")
    descriptor = None
    for klass in Item.__mro__:
        if "CategoryId" in klass.__dict__:
            descriptor = klass.__dict__["CategoryId"]
            break
    assert isinstance(descriptor, property)

def test_item_has_SubCategoryId():
    assert hasattr(Item, "SubCategoryId")
    descriptor = None
    for klass in Item.__mro__:
        if "SubCategoryId" in klass.__dict__:
            descriptor = klass.__dict__["SubCategoryId"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "CodeId" in params, "Missing parameter 'CodeId'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "UserId" in params, "Missing parameter 'UserId'"
    assert "Comment" in params, "Missing parameter 'Comment'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "PhoneNumber" in params, "Missing parameter 'PhoneNumber'"
    assert "TotalPrice" in params, "Missing parameter 'TotalPrice'"
    assert "Status" in params, "Missing parameter 'Status'"

def test_order_has_CodeId():
    assert hasattr(Order, "CodeId")
    descriptor = None
    for klass in Order.__mro__:
        if "CodeId" in klass.__dict__:
            descriptor = klass.__dict__["CodeId"]
            break
    assert isinstance(descriptor, property)

def test_order_has_Email():
    assert hasattr(Order, "Email")
    descriptor = None
    for klass in Order.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_order_has_UserId():
    assert hasattr(Order, "UserId")
    descriptor = None
    for klass in Order.__mro__:
        if "UserId" in klass.__dict__:
            descriptor = klass.__dict__["UserId"]
            break
    assert isinstance(descriptor, property)

def test_order_has_Comment():
    assert hasattr(Order, "Comment")
    descriptor = None
    for klass in Order.__mro__:
        if "Comment" in klass.__dict__:
            descriptor = klass.__dict__["Comment"]
            break
    assert isinstance(descriptor, property)

def test_order_has_Name():
    assert hasattr(Order, "Name")
    descriptor = None
    for klass in Order.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_order_has_Address():
    assert hasattr(Order, "Address")
    descriptor = None
    for klass in Order.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_order_has_PhoneNumber():
    assert hasattr(Order, "PhoneNumber")
    descriptor = None
    for klass in Order.__mro__:
        if "PhoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["PhoneNumber"]
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

def test_order_has_Status():
    assert hasattr(Order, "Status")
    descriptor = None
    for klass in Order.__mro__:
        if "Status" in klass.__dict__:
            descriptor = klass.__dict__["Status"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Login" in params, "Missing parameter 'Login'"
    assert "PhoneNumber" in params, "Missing parameter 'PhoneNumber'"
    assert "Role" in params, "Missing parameter 'Role'"
    assert "LastName" in params, "Missing parameter 'LastName'"
    assert "FirstName" in params, "Missing parameter 'FirstName'"
    assert "Email" in params, "Missing parameter 'Email'"

def test_user_has_Password():
    assert hasattr(User, "Password")
    descriptor = None
    for klass in User.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Login():
    assert hasattr(User, "Login")
    descriptor = None
    for klass in User.__mro__:
        if "Login" in klass.__dict__:
            descriptor = klass.__dict__["Login"]
            break
    assert isinstance(descriptor, property)

def test_user_has_PhoneNumber():
    assert hasattr(User, "PhoneNumber")
    descriptor = None
    for klass in User.__mro__:
        if "PhoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["PhoneNumber"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Role():
    assert hasattr(User, "Role")
    descriptor = None
    for klass in User.__mro__:
        if "Role" in klass.__dict__:
            descriptor = klass.__dict__["Role"]
            break
    assert isinstance(descriptor, property)

def test_user_has_LastName():
    assert hasattr(User, "LastName")
    descriptor = None
    for klass in User.__mro__:
        if "LastName" in klass.__dict__:
            descriptor = klass.__dict__["LastName"]
            break
    assert isinstance(descriptor, property)

def test_user_has_FirstName():
    assert hasattr(User, "FirstName")
    descriptor = None
    for klass in User.__mro__:
        if "FirstName" in klass.__dict__:
            descriptor = klass.__dict__["FirstName"]
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



def test_baseentity_is_not_abstract():
    assert not inspect.isabstract(BaseEntity)


def test_baseentity_constructor_exists():
    assert callable(BaseEntity.__init__)


def test_baseentity_constructor_args():
    sig = inspect.signature(BaseEntity.__init__)
    params = list(sig.parameters.keys())
    assert "Id" in params, "Missing parameter 'Id'"
    assert "UpdatedBy" in params, "Missing parameter 'UpdatedBy'"
    assert "Active" in params, "Missing parameter 'Active'"
    assert "UpdatedDate" in params, "Missing parameter 'UpdatedDate'"
    assert "CreatedBy" in params, "Missing parameter 'CreatedBy'"
    assert "CreatedDate" in params, "Missing parameter 'CreatedDate'"

def test_baseentity_has_Id():
    assert hasattr(BaseEntity, "Id")
    descriptor = None
    for klass in BaseEntity.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_baseentity_has_UpdatedBy():
    assert hasattr(BaseEntity, "UpdatedBy")
    descriptor = None
    for klass in BaseEntity.__mro__:
        if "UpdatedBy" in klass.__dict__:
            descriptor = klass.__dict__["UpdatedBy"]
            break
    assert isinstance(descriptor, property)

def test_baseentity_has_Active():
    assert hasattr(BaseEntity, "Active")
    descriptor = None
    for klass in BaseEntity.__mro__:
        if "Active" in klass.__dict__:
            descriptor = klass.__dict__["Active"]
            break
    assert isinstance(descriptor, property)

def test_baseentity_has_UpdatedDate():
    assert hasattr(BaseEntity, "UpdatedDate")
    descriptor = None
    for klass in BaseEntity.__mro__:
        if "UpdatedDate" in klass.__dict__:
            descriptor = klass.__dict__["UpdatedDate"]
            break
    assert isinstance(descriptor, property)

def test_baseentity_has_CreatedBy():
    assert hasattr(BaseEntity, "CreatedBy")
    descriptor = None
    for klass in BaseEntity.__mro__:
        if "CreatedBy" in klass.__dict__:
            descriptor = klass.__dict__["CreatedBy"]
            break
    assert isinstance(descriptor, property)

def test_baseentity_has_CreatedDate():
    assert hasattr(BaseEntity, "CreatedDate")
    descriptor = None
    for klass in BaseEntity.__mro__:
        if "CreatedDate" in klass.__dict__:
            descriptor = klass.__dict__["CreatedDate"]
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
SubCategory_strategy = st.builds(
    SubCategory,
    RusName=
        safe_text,
    Name=
        safe_text,
    CategoryId=
        safe_text
)
OrderItem_strategy = st.builds(
    OrderItem,
    Price=
        safe_text,
    Amount=
        st.integers(),
    ItemId=
        safe_text,
    Name=
        safe_text,
    OrderId=
        safe_text
)
FavoriteItem_strategy = st.builds(
    FavoriteItem,
    UserId=
        safe_text,
    ItemId=
        safe_text
)
CouponCode_strategy = st.builds(
    CouponCode,
    ExpiryDate=
        safe_text,
    UserId=
        safe_text,
    Discount=
        st.integers(),
    Code=
        safe_text
)
Category_strategy = st.builds(
    Category,
    Name=
        safe_text,
    RusName=
        safe_text
)
Item_strategy = st.builds(
    Item,
    Price=
        safe_text,
    Brand=
        safe_text,
    Name=
        safe_text,
    Discount=
        safe_text,
    Sex=
        st.integers(),
    Description=
        safe_text,
    MinPreviewImagePath=
        safe_text,
    ImagePath2=
        safe_text,
    PreviewImagePath=
        safe_text,
    ImagePath3=
        safe_text,
    Color=
        safe_text,
    Size=
        safe_text,
    Amount=
        st.integers(),
    ImagePath1=
        safe_text,
    Status=
        st.integers(),
    CategoryId=
        safe_text,
    SubCategoryId=
        safe_text
)
Order_strategy = st.builds(
    Order,
    CodeId=
        safe_text,
    Email=
        safe_text,
    UserId=
        safe_text,
    Comment=
        safe_text,
    Name=
        safe_text,
    Address=
        safe_text,
    PhoneNumber=
        safe_text,
    TotalPrice=
        safe_text,
    Status=
        st.integers()
)
User_strategy = st.builds(
    User,
    Password=
        safe_text,
    Login=
        safe_text,
    PhoneNumber=
        safe_text,
    Role=
        st.integers(),
    LastName=
        safe_text,
    FirstName=
        safe_text,
    Email=
        safe_text
)
BaseEntity_strategy = st.builds(
    BaseEntity,
    Id=
        safe_text,
    UpdatedBy=
        safe_text,
    Active=
        st.booleans(),
    UpdatedDate=
        safe_text,
    CreatedBy=
        safe_text,
    CreatedDate=
        safe_text
)

@given(instance=SubCategory_strategy)
@settings(max_examples=50)
def test_subcategory_instantiation(instance):
    assert isinstance(instance, SubCategory)



@given(instance=SubCategory_strategy)
def test_subcategory_RusName_setter(instance):
    original = instance.RusName
    instance.RusName = original
    assert instance.RusName == original



@given(instance=SubCategory_strategy)
def test_subcategory_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=SubCategory_strategy)
def test_subcategory_CategoryId_setter(instance):
    original = instance.CategoryId
    instance.CategoryId = original
    assert instance.CategoryId == original

@given(instance=OrderItem_strategy)
@settings(max_examples=50)
def test_orderitem_instantiation(instance):
    assert isinstance(instance, OrderItem)



@given(instance=OrderItem_strategy)
def test_orderitem_Price_setter(instance):
    original = instance.Price
    instance.Price = original
    assert instance.Price == original



@given(instance=OrderItem_strategy)
def test_orderitem_Amount_setter(instance):
    original = instance.Amount
    instance.Amount = original
    assert instance.Amount == original



@given(instance=OrderItem_strategy)
def test_orderitem_ItemId_setter(instance):
    original = instance.ItemId
    instance.ItemId = original
    assert instance.ItemId == original



@given(instance=OrderItem_strategy)
def test_orderitem_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=OrderItem_strategy)
def test_orderitem_OrderId_setter(instance):
    original = instance.OrderId
    instance.OrderId = original
    assert instance.OrderId == original

@given(instance=FavoriteItem_strategy)
@settings(max_examples=50)
def test_favoriteitem_instantiation(instance):
    assert isinstance(instance, FavoriteItem)



@given(instance=FavoriteItem_strategy)
def test_favoriteitem_UserId_setter(instance):
    original = instance.UserId
    instance.UserId = original
    assert instance.UserId == original



@given(instance=FavoriteItem_strategy)
def test_favoriteitem_ItemId_setter(instance):
    original = instance.ItemId
    instance.ItemId = original
    assert instance.ItemId == original

@given(instance=CouponCode_strategy)
@settings(max_examples=50)
def test_couponcode_instantiation(instance):
    assert isinstance(instance, CouponCode)



@given(instance=CouponCode_strategy)
def test_couponcode_ExpiryDate_setter(instance):
    original = instance.ExpiryDate
    instance.ExpiryDate = original
    assert instance.ExpiryDate == original



@given(instance=CouponCode_strategy)
def test_couponcode_UserId_setter(instance):
    original = instance.UserId
    instance.UserId = original
    assert instance.UserId == original



@given(instance=CouponCode_strategy)
def test_couponcode_Discount_setter(instance):
    original = instance.Discount
    instance.Discount = original
    assert instance.Discount == original



@given(instance=CouponCode_strategy)
def test_couponcode_Code_setter(instance):
    original = instance.Code
    instance.Code = original
    assert instance.Code == original

@given(instance=Category_strategy)
@settings(max_examples=50)
def test_category_instantiation(instance):
    assert isinstance(instance, Category)



@given(instance=Category_strategy)
def test_category_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Category_strategy)
def test_category_RusName_setter(instance):
    original = instance.RusName
    instance.RusName = original
    assert instance.RusName == original

@given(instance=Item_strategy)
@settings(max_examples=50)
def test_item_instantiation(instance):
    assert isinstance(instance, Item)



@given(instance=Item_strategy)
def test_item_Price_setter(instance):
    original = instance.Price
    instance.Price = original
    assert instance.Price == original



@given(instance=Item_strategy)
def test_item_Brand_setter(instance):
    original = instance.Brand
    instance.Brand = original
    assert instance.Brand == original



@given(instance=Item_strategy)
def test_item_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Item_strategy)
def test_item_Discount_setter(instance):
    original = instance.Discount
    instance.Discount = original
    assert instance.Discount == original



@given(instance=Item_strategy)
def test_item_Sex_setter(instance):
    original = instance.Sex
    instance.Sex = original
    assert instance.Sex == original



@given(instance=Item_strategy)
def test_item_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original



@given(instance=Item_strategy)
def test_item_MinPreviewImagePath_setter(instance):
    original = instance.MinPreviewImagePath
    instance.MinPreviewImagePath = original
    assert instance.MinPreviewImagePath == original



@given(instance=Item_strategy)
def test_item_ImagePath2_setter(instance):
    original = instance.ImagePath2
    instance.ImagePath2 = original
    assert instance.ImagePath2 == original



@given(instance=Item_strategy)
def test_item_PreviewImagePath_setter(instance):
    original = instance.PreviewImagePath
    instance.PreviewImagePath = original
    assert instance.PreviewImagePath == original



@given(instance=Item_strategy)
def test_item_ImagePath3_setter(instance):
    original = instance.ImagePath3
    instance.ImagePath3 = original
    assert instance.ImagePath3 == original



@given(instance=Item_strategy)
def test_item_Color_setter(instance):
    original = instance.Color
    instance.Color = original
    assert instance.Color == original



@given(instance=Item_strategy)
def test_item_Size_setter(instance):
    original = instance.Size
    instance.Size = original
    assert instance.Size == original



@given(instance=Item_strategy)
def test_item_Amount_setter(instance):
    original = instance.Amount
    instance.Amount = original
    assert instance.Amount == original



@given(instance=Item_strategy)
def test_item_ImagePath1_setter(instance):
    original = instance.ImagePath1
    instance.ImagePath1 = original
    assert instance.ImagePath1 == original



@given(instance=Item_strategy)
def test_item_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original



@given(instance=Item_strategy)
def test_item_CategoryId_setter(instance):
    original = instance.CategoryId
    instance.CategoryId = original
    assert instance.CategoryId == original



@given(instance=Item_strategy)
def test_item_SubCategoryId_setter(instance):
    original = instance.SubCategoryId
    instance.SubCategoryId = original
    assert instance.SubCategoryId == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_CodeId_setter(instance):
    original = instance.CodeId
    instance.CodeId = original
    assert instance.CodeId == original



@given(instance=Order_strategy)
def test_order_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Order_strategy)
def test_order_UserId_setter(instance):
    original = instance.UserId
    instance.UserId = original
    assert instance.UserId == original



@given(instance=Order_strategy)
def test_order_Comment_setter(instance):
    original = instance.Comment
    instance.Comment = original
    assert instance.Comment == original



@given(instance=Order_strategy)
def test_order_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Order_strategy)
def test_order_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Order_strategy)
def test_order_PhoneNumber_setter(instance):
    original = instance.PhoneNumber
    instance.PhoneNumber = original
    assert instance.PhoneNumber == original



@given(instance=Order_strategy)
def test_order_TotalPrice_setter(instance):
    original = instance.TotalPrice
    instance.TotalPrice = original
    assert instance.TotalPrice == original



@given(instance=Order_strategy)
def test_order_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=User_strategy)
def test_user_Login_setter(instance):
    original = instance.Login
    instance.Login = original
    assert instance.Login == original



@given(instance=User_strategy)
def test_user_PhoneNumber_setter(instance):
    original = instance.PhoneNumber
    instance.PhoneNumber = original
    assert instance.PhoneNumber == original



@given(instance=User_strategy)
def test_user_Role_setter(instance):
    original = instance.Role
    instance.Role = original
    assert instance.Role == original



@given(instance=User_strategy)
def test_user_LastName_setter(instance):
    original = instance.LastName
    instance.LastName = original
    assert instance.LastName == original



@given(instance=User_strategy)
def test_user_FirstName_setter(instance):
    original = instance.FirstName
    instance.FirstName = original
    assert instance.FirstName == original



@given(instance=User_strategy)
def test_user_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original

@given(instance=BaseEntity_strategy)
@settings(max_examples=50)
def test_baseentity_instantiation(instance):
    assert isinstance(instance, BaseEntity)



@given(instance=BaseEntity_strategy)
def test_baseentity_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=BaseEntity_strategy)
def test_baseentity_UpdatedBy_setter(instance):
    original = instance.UpdatedBy
    instance.UpdatedBy = original
    assert instance.UpdatedBy == original



@given(instance=BaseEntity_strategy)
def test_baseentity_Active_setter(instance):
    original = instance.Active
    instance.Active = original
    assert instance.Active == original



@given(instance=BaseEntity_strategy)
def test_baseentity_UpdatedDate_setter(instance):
    original = instance.UpdatedDate
    instance.UpdatedDate = original
    assert instance.UpdatedDate == original



@given(instance=BaseEntity_strategy)
def test_baseentity_CreatedBy_setter(instance):
    original = instance.CreatedBy
    instance.CreatedBy = original
    assert instance.CreatedBy == original



@given(instance=BaseEntity_strategy)
def test_baseentity_CreatedDate_setter(instance):
    original = instance.CreatedDate
    instance.CreatedDate = original
    assert instance.CreatedDate == original
