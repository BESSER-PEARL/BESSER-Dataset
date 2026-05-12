import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Products,
    Farmer_produces,
    Order,
    rating___review,
    Administrator,
    AccountInfo,
    Farmer,
    Retailer_Cart,
    User,
    Retailer,
    CardInfo,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_products_is_not_abstract():
    assert not inspect.isabstract(Products)


def test_products_constructor_exists():
    assert callable(Products.__init__)


def test_products_constructor_args():
    sig = inspect.signature(Products.__init__)
    params = list(sig.parameters.keys())
    assert "reviews" in params, "Missing parameter 'reviews'"
    assert "farmerID" in params, "Missing parameter 'farmerID'"
    assert "inventoryID" in params, "Missing parameter 'inventoryID'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "name" in params, "Missing parameter 'name'"
    assert "selling_price" in params, "Missing parameter 'selling_price'"
    assert "discount" in params, "Missing parameter 'discount'"
    assert "description" in params, "Missing parameter 'description'"
    assert "rating" in params, "Missing parameter 'rating'"

def test_products_has_reviews():
    assert hasattr(Products, "reviews")
    descriptor = None
    for klass in Products.__mro__:
        if "reviews" in klass.__dict__:
            descriptor = klass.__dict__["reviews"]
            break
    assert isinstance(descriptor, property)

def test_products_has_farmerID():
    assert hasattr(Products, "farmerID")
    descriptor = None
    for klass in Products.__mro__:
        if "farmerID" in klass.__dict__:
            descriptor = klass.__dict__["farmerID"]
            break
    assert isinstance(descriptor, property)

def test_products_has_inventoryID():
    assert hasattr(Products, "inventoryID")
    descriptor = None
    for klass in Products.__mro__:
        if "inventoryID" in klass.__dict__:
            descriptor = klass.__dict__["inventoryID"]
            break
    assert isinstance(descriptor, property)

def test_products_has_ID():
    assert hasattr(Products, "ID")
    descriptor = None
    for klass in Products.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_products_has_name():
    assert hasattr(Products, "name")
    descriptor = None
    for klass in Products.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_products_has_selling_price():
    assert hasattr(Products, "selling_price")
    descriptor = None
    for klass in Products.__mro__:
        if "selling_price" in klass.__dict__:
            descriptor = klass.__dict__["selling_price"]
            break
    assert isinstance(descriptor, property)

def test_products_has_discount():
    assert hasattr(Products, "discount")
    descriptor = None
    for klass in Products.__mro__:
        if "discount" in klass.__dict__:
            descriptor = klass.__dict__["discount"]
            break
    assert isinstance(descriptor, property)

def test_products_has_description():
    assert hasattr(Products, "description")
    descriptor = None
    for klass in Products.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_products_has_rating():
    assert hasattr(Products, "rating")
    descriptor = None
    for klass in Products.__mro__:
        if "rating" in klass.__dict__:
            descriptor = klass.__dict__["rating"]
            break
    assert isinstance(descriptor, property)



def test_farmer_produces_is_not_abstract():
    assert not inspect.isabstract(Farmer_produces)


def test_farmer_produces_constructor_exists():
    assert callable(Farmer_produces.__init__)


def test_farmer_produces_constructor_args():
    sig = inspect.signature(Farmer_produces.__init__)
    params = list(sig.parameters.keys())
    assert "farmerID" in params, "Missing parameter 'farmerID'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "productList" in params, "Missing parameter 'productList'"

def test_farmer_produces_has_farmerID():
    assert hasattr(Farmer_produces, "farmerID")
    descriptor = None
    for klass in Farmer_produces.__mro__:
        if "farmerID" in klass.__dict__:
            descriptor = klass.__dict__["farmerID"]
            break
    assert isinstance(descriptor, property)

def test_farmer_produces_has_ID():
    assert hasattr(Farmer_produces, "ID")
    descriptor = None
    for klass in Farmer_produces.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_farmer_produces_has_productList():
    assert hasattr(Farmer_produces, "productList")
    descriptor = None
    for klass in Farmer_produces.__mro__:
        if "productList" in klass.__dict__:
            descriptor = klass.__dict__["productList"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "transactionID" in params, "Missing parameter 'transactionID'"
    assert "cardDetails" in params, "Missing parameter 'cardDetails'"
    assert "productDetails" in params, "Missing parameter 'productDetails'"
    assert "purchaseDate" in params, "Missing parameter 'purchaseDate'"

def test_order_has_transactionID():
    assert hasattr(Order, "transactionID")
    descriptor = None
    for klass in Order.__mro__:
        if "transactionID" in klass.__dict__:
            descriptor = klass.__dict__["transactionID"]
            break
    assert isinstance(descriptor, property)

def test_order_has_cardDetails():
    assert hasattr(Order, "cardDetails")
    descriptor = None
    for klass in Order.__mro__:
        if "cardDetails" in klass.__dict__:
            descriptor = klass.__dict__["cardDetails"]
            break
    assert isinstance(descriptor, property)

def test_order_has_productDetails():
    assert hasattr(Order, "productDetails")
    descriptor = None
    for klass in Order.__mro__:
        if "productDetails" in klass.__dict__:
            descriptor = klass.__dict__["productDetails"]
            break
    assert isinstance(descriptor, property)

def test_order_has_purchaseDate():
    assert hasattr(Order, "purchaseDate")
    descriptor = None
    for klass in Order.__mro__:
        if "purchaseDate" in klass.__dict__:
            descriptor = klass.__dict__["purchaseDate"]
            break
    assert isinstance(descriptor, property)



def test_rating___review_is_not_abstract():
    assert not inspect.isabstract(rating___review)


def test_rating___review_constructor_exists():
    assert callable(rating___review.__init__)


def test_rating___review_constructor_args():
    sig = inspect.signature(rating___review.__init__)
    params = list(sig.parameters.keys())
    assert "rating" in params, "Missing parameter 'rating'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "retailerID" in params, "Missing parameter 'retailerID'"
    assert "reviews" in params, "Missing parameter 'reviews'"
    assert "inventoryID" in params, "Missing parameter 'inventoryID'"
    assert "name" in params, "Missing parameter 'name'"

def test_rating___review_has_rating():
    assert hasattr(rating___review, "rating")
    descriptor = None
    for klass in rating___review.__mro__:
        if "rating" in klass.__dict__:
            descriptor = klass.__dict__["rating"]
            break
    assert isinstance(descriptor, property)

def test_rating___review_has_ID():
    assert hasattr(rating___review, "ID")
    descriptor = None
    for klass in rating___review.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_rating___review_has_retailerID():
    assert hasattr(rating___review, "retailerID")
    descriptor = None
    for klass in rating___review.__mro__:
        if "retailerID" in klass.__dict__:
            descriptor = klass.__dict__["retailerID"]
            break
    assert isinstance(descriptor, property)

def test_rating___review_has_reviews():
    assert hasattr(rating___review, "reviews")
    descriptor = None
    for klass in rating___review.__mro__:
        if "reviews" in klass.__dict__:
            descriptor = klass.__dict__["reviews"]
            break
    assert isinstance(descriptor, property)

def test_rating___review_has_inventoryID():
    assert hasattr(rating___review, "inventoryID")
    descriptor = None
    for klass in rating___review.__mro__:
        if "inventoryID" in klass.__dict__:
            descriptor = klass.__dict__["inventoryID"]
            break
    assert isinstance(descriptor, property)

def test_rating___review_has_name():
    assert hasattr(rating___review, "name")
    descriptor = None
    for klass in rating___review.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_administrator_is_not_abstract():
    assert not inspect.isabstract(Administrator)


def test_administrator_constructor_exists():
    assert callable(Administrator.__init__)


def test_administrator_constructor_args():
    sig = inspect.signature(Administrator.__init__)
    params = list(sig.parameters.keys())
    assert "emailId" in params, "Missing parameter 'emailId'"
    assert "phone" in params, "Missing parameter 'phone'"
    assert "userId" in params, "Missing parameter 'userId'"
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"
    assert "adminType" in params, "Missing parameter 'adminType'"
    assert "name" in params, "Missing parameter 'name'"
    assert "address" in params, "Missing parameter 'address'"

def test_administrator_has_emailId():
    assert hasattr(Administrator, "emailId")
    descriptor = None
    for klass in Administrator.__mro__:
        if "emailId" in klass.__dict__:
            descriptor = klass.__dict__["emailId"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_phone():
    assert hasattr(Administrator, "phone")
    descriptor = None
    for klass in Administrator.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_userId():
    assert hasattr(Administrator, "userId")
    descriptor = None
    for klass in Administrator.__mro__:
        if "userId" in klass.__dict__:
            descriptor = klass.__dict__["userId"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_dateOfBirth():
    assert hasattr(Administrator, "dateOfBirth")
    descriptor = None
    for klass in Administrator.__mro__:
        if "dateOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["dateOfBirth"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_adminType():
    assert hasattr(Administrator, "adminType")
    descriptor = None
    for klass in Administrator.__mro__:
        if "adminType" in klass.__dict__:
            descriptor = klass.__dict__["adminType"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_name():
    assert hasattr(Administrator, "name")
    descriptor = None
    for klass in Administrator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_address():
    assert hasattr(Administrator, "address")
    descriptor = None
    for klass in Administrator.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_accountinfo_is_not_abstract():
    assert not inspect.isabstract(AccountInfo)


def test_accountinfo_constructor_exists():
    assert callable(AccountInfo.__init__)


def test_accountinfo_constructor_args():
    sig = inspect.signature(AccountInfo.__init__)
    params = list(sig.parameters.keys())
    assert "bankBranch" in params, "Missing parameter 'bankBranch'"
    assert "accountNumber" in params, "Missing parameter 'accountNumber'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "name" in params, "Missing parameter 'name'"
    assert "routingNumber" in params, "Missing parameter 'routingNumber'"
    assert "bankName" in params, "Missing parameter 'bankName'"

def test_accountinfo_has_bankBranch():
    assert hasattr(AccountInfo, "bankBranch")
    descriptor = None
    for klass in AccountInfo.__mro__:
        if "bankBranch" in klass.__dict__:
            descriptor = klass.__dict__["bankBranch"]
            break
    assert isinstance(descriptor, property)

def test_accountinfo_has_accountNumber():
    assert hasattr(AccountInfo, "accountNumber")
    descriptor = None
    for klass in AccountInfo.__mro__:
        if "accountNumber" in klass.__dict__:
            descriptor = klass.__dict__["accountNumber"]
            break
    assert isinstance(descriptor, property)

def test_accountinfo_has_ID():
    assert hasattr(AccountInfo, "ID")
    descriptor = None
    for klass in AccountInfo.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_accountinfo_has_name():
    assert hasattr(AccountInfo, "name")
    descriptor = None
    for klass in AccountInfo.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_accountinfo_has_routingNumber():
    assert hasattr(AccountInfo, "routingNumber")
    descriptor = None
    for klass in AccountInfo.__mro__:
        if "routingNumber" in klass.__dict__:
            descriptor = klass.__dict__["routingNumber"]
            break
    assert isinstance(descriptor, property)

def test_accountinfo_has_bankName():
    assert hasattr(AccountInfo, "bankName")
    descriptor = None
    for klass in AccountInfo.__mro__:
        if "bankName" in klass.__dict__:
            descriptor = klass.__dict__["bankName"]
            break
    assert isinstance(descriptor, property)



def test_farmer_is_not_abstract():
    assert not inspect.isabstract(Farmer)


def test_farmer_constructor_exists():
    assert callable(Farmer.__init__)


def test_farmer_constructor_args():
    sig = inspect.signature(Farmer.__init__)
    params = list(sig.parameters.keys())
    assert "accountInfoID" in params, "Missing parameter 'accountInfoID'"
    assert "emailId" in params, "Missing parameter 'emailId'"
    assert "phone" in params, "Missing parameter 'phone'"
    assert "name" in params, "Missing parameter 'name'"
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"
    assert "userId" in params, "Missing parameter 'userId'"
    assert "type" in params, "Missing parameter 'type'"
    assert "CardInfo" in params, "Missing parameter 'CardInfo'"
    assert "address" in params, "Missing parameter 'address'"

def test_farmer_has_accountInfoID():
    assert hasattr(Farmer, "accountInfoID")
    descriptor = None
    for klass in Farmer.__mro__:
        if "accountInfoID" in klass.__dict__:
            descriptor = klass.__dict__["accountInfoID"]
            break
    assert isinstance(descriptor, property)

def test_farmer_has_emailId():
    assert hasattr(Farmer, "emailId")
    descriptor = None
    for klass in Farmer.__mro__:
        if "emailId" in klass.__dict__:
            descriptor = klass.__dict__["emailId"]
            break
    assert isinstance(descriptor, property)

def test_farmer_has_phone():
    assert hasattr(Farmer, "phone")
    descriptor = None
    for klass in Farmer.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)

def test_farmer_has_name():
    assert hasattr(Farmer, "name")
    descriptor = None
    for klass in Farmer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_farmer_has_dateOfBirth():
    assert hasattr(Farmer, "dateOfBirth")
    descriptor = None
    for klass in Farmer.__mro__:
        if "dateOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["dateOfBirth"]
            break
    assert isinstance(descriptor, property)

def test_farmer_has_userId():
    assert hasattr(Farmer, "userId")
    descriptor = None
    for klass in Farmer.__mro__:
        if "userId" in klass.__dict__:
            descriptor = klass.__dict__["userId"]
            break
    assert isinstance(descriptor, property)

def test_farmer_has_type():
    assert hasattr(Farmer, "type")
    descriptor = None
    for klass in Farmer.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_farmer_has_CardInfo():
    assert hasattr(Farmer, "CardInfo")
    descriptor = None
    for klass in Farmer.__mro__:
        if "CardInfo" in klass.__dict__:
            descriptor = klass.__dict__["CardInfo"]
            break
    assert isinstance(descriptor, property)

def test_farmer_has_address():
    assert hasattr(Farmer, "address")
    descriptor = None
    for klass in Farmer.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_retailer_cart_is_not_abstract():
    assert not inspect.isabstract(Retailer_Cart)


def test_retailer_cart_constructor_exists():
    assert callable(Retailer_Cart.__init__)


def test_retailer_cart_constructor_args():
    sig = inspect.signature(Retailer_Cart.__init__)
    params = list(sig.parameters.keys())
    assert "userID" in params, "Missing parameter 'userID'"
    assert "quantity___product" in params, "Missing parameter 'quantity___product'"
    assert "product" in params, "Missing parameter 'product'"

def test_retailer_cart_has_userID():
    assert hasattr(Retailer_Cart, "userID")
    descriptor = None
    for klass in Retailer_Cart.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)

def test_retailer_cart_has_quantity___product():
    assert hasattr(Retailer_Cart, "quantity___product")
    descriptor = None
    for klass in Retailer_Cart.__mro__:
        if "quantity___product" in klass.__dict__:
            descriptor = klass.__dict__["quantity___product"]
            break
    assert isinstance(descriptor, property)

def test_retailer_cart_has_product():
    assert hasattr(Retailer_Cart, "product")
    descriptor = None
    for klass in Retailer_Cart.__mro__:
        if "product" in klass.__dict__:
            descriptor = klass.__dict__["product"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "userName" in params, "Missing parameter 'userName'"
    assert "Id" in params, "Missing parameter 'Id'"
    assert "userType" in params, "Missing parameter 'userType'"
    assert "password" in params, "Missing parameter 'password'"

def test_user_has_userName():
    assert hasattr(User, "userName")
    descriptor = None
    for klass in User.__mro__:
        if "userName" in klass.__dict__:
            descriptor = klass.__dict__["userName"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Id():
    assert hasattr(User, "Id")
    descriptor = None
    for klass in User.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_user_has_userType():
    assert hasattr(User, "userType")
    descriptor = None
    for klass in User.__mro__:
        if "userType" in klass.__dict__:
            descriptor = klass.__dict__["userType"]
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



def test_retailer_is_not_abstract():
    assert not inspect.isabstract(Retailer)


def test_retailer_constructor_exists():
    assert callable(Retailer.__init__)


def test_retailer_constructor_args():
    sig = inspect.signature(Retailer.__init__)
    params = list(sig.parameters.keys())
    assert "userId" in params, "Missing parameter 'userId'"
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"
    assert "Photo" in params, "Missing parameter 'Photo'"
    assert "address" in params, "Missing parameter 'address'"
    assert "emailId" in params, "Missing parameter 'emailId'"
    assert "phone" in params, "Missing parameter 'phone'"
    assert "CardInfo" in params, "Missing parameter 'CardInfo'"
    assert "name" in params, "Missing parameter 'name'"

def test_retailer_has_userId():
    assert hasattr(Retailer, "userId")
    descriptor = None
    for klass in Retailer.__mro__:
        if "userId" in klass.__dict__:
            descriptor = klass.__dict__["userId"]
            break
    assert isinstance(descriptor, property)

def test_retailer_has_dateOfBirth():
    assert hasattr(Retailer, "dateOfBirth")
    descriptor = None
    for klass in Retailer.__mro__:
        if "dateOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["dateOfBirth"]
            break
    assert isinstance(descriptor, property)

def test_retailer_has_Photo():
    assert hasattr(Retailer, "Photo")
    descriptor = None
    for klass in Retailer.__mro__:
        if "Photo" in klass.__dict__:
            descriptor = klass.__dict__["Photo"]
            break
    assert isinstance(descriptor, property)

def test_retailer_has_address():
    assert hasattr(Retailer, "address")
    descriptor = None
    for klass in Retailer.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_retailer_has_emailId():
    assert hasattr(Retailer, "emailId")
    descriptor = None
    for klass in Retailer.__mro__:
        if "emailId" in klass.__dict__:
            descriptor = klass.__dict__["emailId"]
            break
    assert isinstance(descriptor, property)

def test_retailer_has_phone():
    assert hasattr(Retailer, "phone")
    descriptor = None
    for klass in Retailer.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)

def test_retailer_has_CardInfo():
    assert hasattr(Retailer, "CardInfo")
    descriptor = None
    for klass in Retailer.__mro__:
        if "CardInfo" in klass.__dict__:
            descriptor = klass.__dict__["CardInfo"]
            break
    assert isinstance(descriptor, property)

def test_retailer_has_name():
    assert hasattr(Retailer, "name")
    descriptor = None
    for klass in Retailer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cardinfo_is_not_abstract():
    assert not inspect.isabstract(CardInfo)


def test_cardinfo_constructor_exists():
    assert callable(CardInfo.__init__)


def test_cardinfo_constructor_args():
    sig = inspect.signature(CardInfo.__init__)
    params = list(sig.parameters.keys())
    assert "billingAddress" in params, "Missing parameter 'billingAddress'"
    assert "CVV" in params, "Missing parameter 'CVV'"
    assert "expiryDate" in params, "Missing parameter 'expiryDate'"
    assert "name" in params, "Missing parameter 'name'"
    assert "number" in params, "Missing parameter 'number'"
    assert "ID" in params, "Missing parameter 'ID'"

def test_cardinfo_has_billingAddress():
    assert hasattr(CardInfo, "billingAddress")
    descriptor = None
    for klass in CardInfo.__mro__:
        if "billingAddress" in klass.__dict__:
            descriptor = klass.__dict__["billingAddress"]
            break
    assert isinstance(descriptor, property)

def test_cardinfo_has_CVV():
    assert hasattr(CardInfo, "CVV")
    descriptor = None
    for klass in CardInfo.__mro__:
        if "CVV" in klass.__dict__:
            descriptor = klass.__dict__["CVV"]
            break
    assert isinstance(descriptor, property)

def test_cardinfo_has_expiryDate():
    assert hasattr(CardInfo, "expiryDate")
    descriptor = None
    for klass in CardInfo.__mro__:
        if "expiryDate" in klass.__dict__:
            descriptor = klass.__dict__["expiryDate"]
            break
    assert isinstance(descriptor, property)

def test_cardinfo_has_name():
    assert hasattr(CardInfo, "name")
    descriptor = None
    for klass in CardInfo.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cardinfo_has_number():
    assert hasattr(CardInfo, "number")
    descriptor = None
    for klass in CardInfo.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_cardinfo_has_ID():
    assert hasattr(CardInfo, "ID")
    descriptor = None
    for klass in CardInfo.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
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
Products_strategy = st.builds(
    Products,
    reviews=
        safe_text,
    farmerID=
        safe_text,
    inventoryID=
        safe_text,
    ID=
        st.integers(),
    name=
        safe_text,
    selling_price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    discount=
        st.integers(),
    description=
        safe_text,
    rating=
        st.integers()
)
Farmer_produces_strategy = st.builds(
    Farmer_produces,
    farmerID=
        st.integers(),
    ID=
        st.integers(),
    productList=
        safe_text
)
Order_strategy = st.builds(
    Order,
    transactionID=
        st.integers(),
    cardDetails=
        safe_text,
    productDetails=
        safe_text,
    purchaseDate=
        st.dates()
)
rating___review_strategy = st.builds(
    rating___review,
    rating=
        st.integers(),
    ID=
        st.integers(),
    retailerID=
        safe_text,
    reviews=
        safe_text,
    inventoryID=
        safe_text,
    name=
        safe_text
)
Administrator_strategy = st.builds(
    Administrator,
    emailId=
        safe_text,
    phone=
        st.integers(),
    userId=
        st.integers(),
    dateOfBirth=
        st.dates(),
    adminType=
        safe_text,
    name=
        safe_text,
    address=
        safe_text
)
AccountInfo_strategy = st.builds(
    AccountInfo,
    bankBranch=
        safe_text,
    accountNumber=
        st.integers(),
    ID=
        st.integers(),
    name=
        safe_text,
    routingNumber=
        st.integers(),
    bankName=
        safe_text
)
Farmer_strategy = st.builds(
    Farmer,
    accountInfoID=
        st.integers(),
    emailId=
        safe_text,
    phone=
        st.integers(),
    name=
        safe_text,
    dateOfBirth=
        st.dates(),
    userId=
        st.integers(),
    type=
        safe_text,
    CardInfo=
        safe_text,
    address=
        safe_text
)
Retailer_Cart_strategy = st.builds(
    Retailer_Cart,
    userID=
        st.integers(),
    quantity___product=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    product=
        st.none()
)
User_strategy = st.builds(
    User,
    userName=
        safe_text,
    Id=
        st.integers(),
    userType=
        safe_text,
    password=
        safe_text
)
Retailer_strategy = st.builds(
    Retailer,
    userId=
        st.integers(),
    dateOfBirth=
        st.dates(),
    Photo=
        safe_text,
    address=
        safe_text,
    emailId=
        safe_text,
    phone=
        st.integers(),
    CardInfo=
        st.integers(),
    name=
        safe_text
)
CardInfo_strategy = st.builds(
    CardInfo,
    billingAddress=
        safe_text,
    CVV=
        st.integers(),
    expiryDate=
        st.dates(),
    name=
        safe_text,
    number=
        st.integers(),
    ID=
        st.integers()
)

@given(instance=Products_strategy)
@settings(max_examples=50)
def test_products_instantiation(instance):
    assert isinstance(instance, Products)



@given(instance=Products_strategy)
def test_products_reviews_setter(instance):
    original = instance.reviews
    instance.reviews = original
    assert instance.reviews == original



@given(instance=Products_strategy)
def test_products_farmerID_setter(instance):
    original = instance.farmerID
    instance.farmerID = original
    assert instance.farmerID == original



@given(instance=Products_strategy)
def test_products_inventoryID_setter(instance):
    original = instance.inventoryID
    instance.inventoryID = original
    assert instance.inventoryID == original



@given(instance=Products_strategy)
def test_products_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Products_strategy)
def test_products_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Products_strategy)
def test_products_selling_price_setter(instance):
    original = instance.selling_price
    instance.selling_price = original
    assert instance.selling_price == original



@given(instance=Products_strategy)
def test_products_discount_setter(instance):
    original = instance.discount
    instance.discount = original
    assert instance.discount == original



@given(instance=Products_strategy)
def test_products_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Products_strategy)
def test_products_rating_setter(instance):
    original = instance.rating
    instance.rating = original
    assert instance.rating == original

@given(instance=Farmer_produces_strategy)
@settings(max_examples=50)
def test_farmer_produces_instantiation(instance):
    assert isinstance(instance, Farmer_produces)



@given(instance=Farmer_produces_strategy)
def test_farmer_produces_farmerID_setter(instance):
    original = instance.farmerID
    instance.farmerID = original
    assert instance.farmerID == original



@given(instance=Farmer_produces_strategy)
def test_farmer_produces_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Farmer_produces_strategy)
def test_farmer_produces_productList_setter(instance):
    original = instance.productList
    instance.productList = original
    assert instance.productList == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_transactionID_setter(instance):
    original = instance.transactionID
    instance.transactionID = original
    assert instance.transactionID == original



@given(instance=Order_strategy)
def test_order_cardDetails_setter(instance):
    original = instance.cardDetails
    instance.cardDetails = original
    assert instance.cardDetails == original



@given(instance=Order_strategy)
def test_order_productDetails_setter(instance):
    original = instance.productDetails
    instance.productDetails = original
    assert instance.productDetails == original



@given(instance=Order_strategy)
def test_order_purchaseDate_setter(instance):
    original = instance.purchaseDate
    instance.purchaseDate = original
    assert instance.purchaseDate == original

@given(instance=rating___review_strategy)
@settings(max_examples=50)
def test_rating___review_instantiation(instance):
    assert isinstance(instance, rating___review)



@given(instance=rating___review_strategy)
def test_rating___review_rating_setter(instance):
    original = instance.rating
    instance.rating = original
    assert instance.rating == original



@given(instance=rating___review_strategy)
def test_rating___review_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=rating___review_strategy)
def test_rating___review_retailerID_setter(instance):
    original = instance.retailerID
    instance.retailerID = original
    assert instance.retailerID == original



@given(instance=rating___review_strategy)
def test_rating___review_reviews_setter(instance):
    original = instance.reviews
    instance.reviews = original
    assert instance.reviews == original



@given(instance=rating___review_strategy)
def test_rating___review_inventoryID_setter(instance):
    original = instance.inventoryID
    instance.inventoryID = original
    assert instance.inventoryID == original



@given(instance=rating___review_strategy)
def test_rating___review_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Administrator_strategy)
@settings(max_examples=50)
def test_administrator_instantiation(instance):
    assert isinstance(instance, Administrator)



@given(instance=Administrator_strategy)
def test_administrator_emailId_setter(instance):
    original = instance.emailId
    instance.emailId = original
    assert instance.emailId == original



@given(instance=Administrator_strategy)
def test_administrator_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=Administrator_strategy)
def test_administrator_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original



@given(instance=Administrator_strategy)
def test_administrator_dateOfBirth_setter(instance):
    original = instance.dateOfBirth
    instance.dateOfBirth = original
    assert instance.dateOfBirth == original



@given(instance=Administrator_strategy)
def test_administrator_adminType_setter(instance):
    original = instance.adminType
    instance.adminType = original
    assert instance.adminType == original



@given(instance=Administrator_strategy)
def test_administrator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Administrator_strategy)
def test_administrator_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=AccountInfo_strategy)
@settings(max_examples=50)
def test_accountinfo_instantiation(instance):
    assert isinstance(instance, AccountInfo)



@given(instance=AccountInfo_strategy)
def test_accountinfo_bankBranch_setter(instance):
    original = instance.bankBranch
    instance.bankBranch = original
    assert instance.bankBranch == original



@given(instance=AccountInfo_strategy)
def test_accountinfo_accountNumber_setter(instance):
    original = instance.accountNumber
    instance.accountNumber = original
    assert instance.accountNumber == original



@given(instance=AccountInfo_strategy)
def test_accountinfo_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=AccountInfo_strategy)
def test_accountinfo_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=AccountInfo_strategy)
def test_accountinfo_routingNumber_setter(instance):
    original = instance.routingNumber
    instance.routingNumber = original
    assert instance.routingNumber == original



@given(instance=AccountInfo_strategy)
def test_accountinfo_bankName_setter(instance):
    original = instance.bankName
    instance.bankName = original
    assert instance.bankName == original

@given(instance=Farmer_strategy)
@settings(max_examples=50)
def test_farmer_instantiation(instance):
    assert isinstance(instance, Farmer)



@given(instance=Farmer_strategy)
def test_farmer_accountInfoID_setter(instance):
    original = instance.accountInfoID
    instance.accountInfoID = original
    assert instance.accountInfoID == original



@given(instance=Farmer_strategy)
def test_farmer_emailId_setter(instance):
    original = instance.emailId
    instance.emailId = original
    assert instance.emailId == original



@given(instance=Farmer_strategy)
def test_farmer_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=Farmer_strategy)
def test_farmer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Farmer_strategy)
def test_farmer_dateOfBirth_setter(instance):
    original = instance.dateOfBirth
    instance.dateOfBirth = original
    assert instance.dateOfBirth == original



@given(instance=Farmer_strategy)
def test_farmer_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original



@given(instance=Farmer_strategy)
def test_farmer_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Farmer_strategy)
def test_farmer_CardInfo_setter(instance):
    original = instance.CardInfo
    instance.CardInfo = original
    assert instance.CardInfo == original



@given(instance=Farmer_strategy)
def test_farmer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=Retailer_Cart_strategy)
@settings(max_examples=50)
def test_retailer_cart_instantiation(instance):
    assert isinstance(instance, Retailer_Cart)



@given(instance=Retailer_Cart_strategy)
def test_retailer_cart_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=Retailer_Cart_strategy)
def test_retailer_cart_quantity___product_setter(instance):
    original = instance.quantity___product
    instance.quantity___product = original
    assert instance.quantity___product == original



@given(instance=Retailer_Cart_strategy)
def test_retailer_cart_product_setter(instance):
    original = instance.product
    instance.product = original
    assert instance.product == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original



@given(instance=User_strategy)
def test_user_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=User_strategy)
def test_user_userType_setter(instance):
    original = instance.userType
    instance.userType = original
    assert instance.userType == original



@given(instance=User_strategy)
def test_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=Retailer_strategy)
@settings(max_examples=50)
def test_retailer_instantiation(instance):
    assert isinstance(instance, Retailer)



@given(instance=Retailer_strategy)
def test_retailer_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original



@given(instance=Retailer_strategy)
def test_retailer_dateOfBirth_setter(instance):
    original = instance.dateOfBirth
    instance.dateOfBirth = original
    assert instance.dateOfBirth == original



@given(instance=Retailer_strategy)
def test_retailer_Photo_setter(instance):
    original = instance.Photo
    instance.Photo = original
    assert instance.Photo == original



@given(instance=Retailer_strategy)
def test_retailer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Retailer_strategy)
def test_retailer_emailId_setter(instance):
    original = instance.emailId
    instance.emailId = original
    assert instance.emailId == original



@given(instance=Retailer_strategy)
def test_retailer_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=Retailer_strategy)
def test_retailer_CardInfo_setter(instance):
    original = instance.CardInfo
    instance.CardInfo = original
    assert instance.CardInfo == original



@given(instance=Retailer_strategy)
def test_retailer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CardInfo_strategy)
@settings(max_examples=50)
def test_cardinfo_instantiation(instance):
    assert isinstance(instance, CardInfo)



@given(instance=CardInfo_strategy)
def test_cardinfo_billingAddress_setter(instance):
    original = instance.billingAddress
    instance.billingAddress = original
    assert instance.billingAddress == original



@given(instance=CardInfo_strategy)
def test_cardinfo_CVV_setter(instance):
    original = instance.CVV
    instance.CVV = original
    assert instance.CVV == original



@given(instance=CardInfo_strategy)
def test_cardinfo_expiryDate_setter(instance):
    original = instance.expiryDate
    instance.expiryDate = original
    assert instance.expiryDate == original



@given(instance=CardInfo_strategy)
def test_cardinfo_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=CardInfo_strategy)
def test_cardinfo_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=CardInfo_strategy)
def test_cardinfo_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original
