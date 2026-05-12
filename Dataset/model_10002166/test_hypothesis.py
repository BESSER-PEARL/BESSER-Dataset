import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Estring_Interface,
    online_shopping_Order_Detail,
    online_shopping_Delivertiony_Informa,
    online_shopping_Payment,
    online_shopping_Product,
    online_shopping_Category,
    online_shopping_Shopping_Card,
    online_shopping_Customer,
    online_shopping_Orders,
    online_shopping_Session_manager,
    online_shopping_Deoartment,
    online_shopping_Administrator,
    online_shopping_Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_estring_interface_is_not_abstract():
    assert not inspect.isabstract(Estring_Interface)


def test_estring_interface_constructor_exists():
    assert callable(Estring_Interface.__init__)


def test_estring_interface_constructor_args():
    sig = inspect.signature(Estring_Interface.__init__)
    params = list(sig.parameters.keys())



def test_online_shopping_order_detail_is_not_abstract():
    assert not inspect.isabstract(online_shopping_Order_Detail)


def test_online_shopping_order_detail_constructor_exists():
    assert callable(online_shopping_Order_Detail.__init__)


def test_online_shopping_order_detail_constructor_args():
    sig = inspect.signature(online_shopping_Order_Detail.__init__)
    params = list(sig.parameters.keys())
    assert "Quantity" in params, "Missing parameter 'Quantity'"
    assert "unit_Cost" in params, "Missing parameter 'unit_Cost'"
    assert "Subtotal" in params, "Missing parameter 'Subtotal'"
    assert "Product_Name" in params, "Missing parameter 'Product_Name'"
    assert "Order_ID" in params, "Missing parameter 'Order_ID'"
    assert "Product_ID" in params, "Missing parameter 'Product_ID'"

def test_online_shopping_order_detail_has_Quantity():
    assert hasattr(online_shopping_Order_Detail, "Quantity")
    descriptor = None
    for klass in online_shopping_Order_Detail.__mro__:
        if "Quantity" in klass.__dict__:
            descriptor = klass.__dict__["Quantity"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_order_detail_has_unit_Cost():
    assert hasattr(online_shopping_Order_Detail, "unit_Cost")
    descriptor = None
    for klass in online_shopping_Order_Detail.__mro__:
        if "unit_Cost" in klass.__dict__:
            descriptor = klass.__dict__["unit_Cost"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_order_detail_has_Subtotal():
    assert hasattr(online_shopping_Order_Detail, "Subtotal")
    descriptor = None
    for klass in online_shopping_Order_Detail.__mro__:
        if "Subtotal" in klass.__dict__:
            descriptor = klass.__dict__["Subtotal"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_order_detail_has_Product_Name():
    assert hasattr(online_shopping_Order_Detail, "Product_Name")
    descriptor = None
    for klass in online_shopping_Order_Detail.__mro__:
        if "Product_Name" in klass.__dict__:
            descriptor = klass.__dict__["Product_Name"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_order_detail_has_Order_ID():
    assert hasattr(online_shopping_Order_Detail, "Order_ID")
    descriptor = None
    for klass in online_shopping_Order_Detail.__mro__:
        if "Order_ID" in klass.__dict__:
            descriptor = klass.__dict__["Order_ID"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_order_detail_has_Product_ID():
    assert hasattr(online_shopping_Order_Detail, "Product_ID")
    descriptor = None
    for klass in online_shopping_Order_Detail.__mro__:
        if "Product_ID" in klass.__dict__:
            descriptor = klass.__dict__["Product_ID"]
            break
    assert isinstance(descriptor, property)



def test_online_shopping_delivertiony_informa_is_not_abstract():
    assert not inspect.isabstract(online_shopping_Delivertiony_Informa)


def test_online_shopping_delivertiony_informa_constructor_exists():
    assert callable(online_shopping_Delivertiony_Informa.__init__)


def test_online_shopping_delivertiony_informa_constructor_args():
    sig = inspect.signature(online_shopping_Delivertiony_Informa.__init__)
    params = list(sig.parameters.keys())
    assert "Receiver_Name" in params, "Missing parameter 'Receiver_Name'"
    assert "Other_Delivery_Address" in params, "Missing parameter 'Other_Delivery_Address'"
    assert "Delivery_Address" in params, "Missing parameter 'Delivery_Address'"
    assert "Delivery_Phone" in params, "Missing parameter 'Delivery_Phone'"

def test_online_shopping_delivertiony_informa_has_Receiver_Name():
    assert hasattr(online_shopping_Delivertiony_Informa, "Receiver_Name")
    descriptor = None
    for klass in online_shopping_Delivertiony_Informa.__mro__:
        if "Receiver_Name" in klass.__dict__:
            descriptor = klass.__dict__["Receiver_Name"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_delivertiony_informa_has_Other_Delivery_Address():
    assert hasattr(online_shopping_Delivertiony_Informa, "Other_Delivery_Address")
    descriptor = None
    for klass in online_shopping_Delivertiony_Informa.__mro__:
        if "Other_Delivery_Address" in klass.__dict__:
            descriptor = klass.__dict__["Other_Delivery_Address"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_delivertiony_informa_has_Delivery_Address():
    assert hasattr(online_shopping_Delivertiony_Informa, "Delivery_Address")
    descriptor = None
    for klass in online_shopping_Delivertiony_Informa.__mro__:
        if "Delivery_Address" in klass.__dict__:
            descriptor = klass.__dict__["Delivery_Address"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_delivertiony_informa_has_Delivery_Phone():
    assert hasattr(online_shopping_Delivertiony_Informa, "Delivery_Phone")
    descriptor = None
    for klass in online_shopping_Delivertiony_Informa.__mro__:
        if "Delivery_Phone" in klass.__dict__:
            descriptor = klass.__dict__["Delivery_Phone"]
            break
    assert isinstance(descriptor, property)



def test_online_shopping_payment_is_not_abstract():
    assert not inspect.isabstract(online_shopping_Payment)


def test_online_shopping_payment_constructor_exists():
    assert callable(online_shopping_Payment.__init__)


def test_online_shopping_payment_constructor_args():
    sig = inspect.signature(online_shopping_Payment.__init__)
    params = list(sig.parameters.keys())
    assert "Catch_Pay" in params, "Missing parameter 'Catch_Pay'"
    assert "Online_Pay" in params, "Missing parameter 'Online_Pay'"

def test_online_shopping_payment_has_Catch_Pay():
    assert hasattr(online_shopping_Payment, "Catch_Pay")
    descriptor = None
    for klass in online_shopping_Payment.__mro__:
        if "Catch_Pay" in klass.__dict__:
            descriptor = klass.__dict__["Catch_Pay"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_payment_has_Online_Pay():
    assert hasattr(online_shopping_Payment, "Online_Pay")
    descriptor = None
    for klass in online_shopping_Payment.__mro__:
        if "Online_Pay" in klass.__dict__:
            descriptor = klass.__dict__["Online_Pay"]
            break
    assert isinstance(descriptor, property)



def test_online_shopping_product_is_not_abstract():
    assert not inspect.isabstract(online_shopping_Product)


def test_online_shopping_product_constructor_exists():
    assert callable(online_shopping_Product.__init__)


def test_online_shopping_product_constructor_args():
    sig = inspect.signature(online_shopping_Product.__init__)
    params = list(sig.parameters.keys())
    assert "Image_File_Name" in params, "Missing parameter 'Image_File_Name'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Price" in params, "Missing parameter 'Price'"
    assert "Description" in params, "Missing parameter 'Description'"
    assert "Product_ID" in params, "Missing parameter 'Product_ID'"

def test_online_shopping_product_has_Image_File_Name():
    assert hasattr(online_shopping_Product, "Image_File_Name")
    descriptor = None
    for klass in online_shopping_Product.__mro__:
        if "Image_File_Name" in klass.__dict__:
            descriptor = klass.__dict__["Image_File_Name"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_product_has_Name():
    assert hasattr(online_shopping_Product, "Name")
    descriptor = None
    for klass in online_shopping_Product.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_product_has_Price():
    assert hasattr(online_shopping_Product, "Price")
    descriptor = None
    for klass in online_shopping_Product.__mro__:
        if "Price" in klass.__dict__:
            descriptor = klass.__dict__["Price"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_product_has_Description():
    assert hasattr(online_shopping_Product, "Description")
    descriptor = None
    for klass in online_shopping_Product.__mro__:
        if "Description" in klass.__dict__:
            descriptor = klass.__dict__["Description"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_product_has_Product_ID():
    assert hasattr(online_shopping_Product, "Product_ID")
    descriptor = None
    for klass in online_shopping_Product.__mro__:
        if "Product_ID" in klass.__dict__:
            descriptor = klass.__dict__["Product_ID"]
            break
    assert isinstance(descriptor, property)



def test_online_shopping_category_is_not_abstract():
    assert not inspect.isabstract(online_shopping_Category)


def test_online_shopping_category_constructor_exists():
    assert callable(online_shopping_Category.__init__)


def test_online_shopping_category_constructor_args():
    sig = inspect.signature(online_shopping_Category.__init__)
    params = list(sig.parameters.keys())
    assert "Category_ID" in params, "Missing parameter 'Category_ID'"
    assert "Department_ID" in params, "Missing parameter 'Department_ID'"
    assert "Description" in params, "Missing parameter 'Description'"
    assert "Catemegory_Name" in params, "Missing parameter 'Catemegory_Name'"

def test_online_shopping_category_has_Category_ID():
    assert hasattr(online_shopping_Category, "Category_ID")
    descriptor = None
    for klass in online_shopping_Category.__mro__:
        if "Category_ID" in klass.__dict__:
            descriptor = klass.__dict__["Category_ID"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_category_has_Department_ID():
    assert hasattr(online_shopping_Category, "Department_ID")
    descriptor = None
    for klass in online_shopping_Category.__mro__:
        if "Department_ID" in klass.__dict__:
            descriptor = klass.__dict__["Department_ID"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_category_has_Description():
    assert hasattr(online_shopping_Category, "Description")
    descriptor = None
    for klass in online_shopping_Category.__mro__:
        if "Description" in klass.__dict__:
            descriptor = klass.__dict__["Description"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_category_has_Catemegory_Name():
    assert hasattr(online_shopping_Category, "Catemegory_Name")
    descriptor = None
    for klass in online_shopping_Category.__mro__:
        if "Catemegory_Name" in klass.__dict__:
            descriptor = klass.__dict__["Catemegory_Name"]
            break
    assert isinstance(descriptor, property)



def test_online_shopping_shopping_card_is_not_abstract():
    assert not inspect.isabstract(online_shopping_Shopping_Card)


def test_online_shopping_shopping_card_constructor_exists():
    assert callable(online_shopping_Shopping_Card.__init__)


def test_online_shopping_shopping_card_constructor_args():
    sig = inspect.signature(online_shopping_Shopping_Card.__init__)
    params = list(sig.parameters.keys())
    assert "Date_Added" in params, "Missing parameter 'Date_Added'"
    assert "Quantity" in params, "Missing parameter 'Quantity'"
    assert "Produced_Id" in params, "Missing parameter 'Produced_Id'"
    assert "Cart_ID" in params, "Missing parameter 'Cart_ID'"

def test_online_shopping_shopping_card_has_Date_Added():
    assert hasattr(online_shopping_Shopping_Card, "Date_Added")
    descriptor = None
    for klass in online_shopping_Shopping_Card.__mro__:
        if "Date_Added" in klass.__dict__:
            descriptor = klass.__dict__["Date_Added"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_shopping_card_has_Quantity():
    assert hasattr(online_shopping_Shopping_Card, "Quantity")
    descriptor = None
    for klass in online_shopping_Shopping_Card.__mro__:
        if "Quantity" in klass.__dict__:
            descriptor = klass.__dict__["Quantity"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_shopping_card_has_Produced_Id():
    assert hasattr(online_shopping_Shopping_Card, "Produced_Id")
    descriptor = None
    for klass in online_shopping_Shopping_Card.__mro__:
        if "Produced_Id" in klass.__dict__:
            descriptor = klass.__dict__["Produced_Id"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_shopping_card_has_Cart_ID():
    assert hasattr(online_shopping_Shopping_Card, "Cart_ID")
    descriptor = None
    for klass in online_shopping_Shopping_Card.__mro__:
        if "Cart_ID" in klass.__dict__:
            descriptor = klass.__dict__["Cart_ID"]
            break
    assert isinstance(descriptor, property)



def test_online_shopping_customer_is_not_abstract():
    assert not inspect.isabstract(online_shopping_Customer)


def test_online_shopping_customer_constructor_exists():
    assert callable(online_shopping_Customer.__init__)


def test_online_shopping_customer_constructor_args():
    sig = inspect.signature(online_shopping_Customer.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Shippinginfo" in params, "Missing parameter 'Shippinginfo'"
    assert "Phone" in params, "Missing parameter 'Phone'"
    assert "E_mail" in params, "Missing parameter 'E_mail'"

def test_online_shopping_customer_has_Name():
    assert hasattr(online_shopping_Customer, "Name")
    descriptor = None
    for klass in online_shopping_Customer.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_customer_has_Address():
    assert hasattr(online_shopping_Customer, "Address")
    descriptor = None
    for klass in online_shopping_Customer.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_customer_has_Shippinginfo():
    assert hasattr(online_shopping_Customer, "Shippinginfo")
    descriptor = None
    for klass in online_shopping_Customer.__mro__:
        if "Shippinginfo" in klass.__dict__:
            descriptor = klass.__dict__["Shippinginfo"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_customer_has_Phone():
    assert hasattr(online_shopping_Customer, "Phone")
    descriptor = None
    for klass in online_shopping_Customer.__mro__:
        if "Phone" in klass.__dict__:
            descriptor = klass.__dict__["Phone"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_customer_has_E_mail():
    assert hasattr(online_shopping_Customer, "E_mail")
    descriptor = None
    for klass in online_shopping_Customer.__mro__:
        if "E_mail" in klass.__dict__:
            descriptor = klass.__dict__["E_mail"]
            break
    assert isinstance(descriptor, property)



def test_online_shopping_orders_is_not_abstract():
    assert not inspect.isabstract(online_shopping_Orders)


def test_online_shopping_orders_constructor_exists():
    assert callable(online_shopping_Orders.__init__)


def test_online_shopping_orders_constructor_args():
    sig = inspect.signature(online_shopping_Orders.__init__)
    params = list(sig.parameters.keys())
    assert "Customer_Name" in params, "Missing parameter 'Customer_Name'"
    assert "Date_Created" in params, "Missing parameter 'Date_Created'"
    assert "Customer_ID" in params, "Missing parameter 'Customer_ID'"
    assert "Order_ID" in params, "Missing parameter 'Order_ID'"
    assert "Datw_Shipping" in params, "Missing parameter 'Datw_Shipping'"

def test_online_shopping_orders_has_Customer_Name():
    assert hasattr(online_shopping_Orders, "Customer_Name")
    descriptor = None
    for klass in online_shopping_Orders.__mro__:
        if "Customer_Name" in klass.__dict__:
            descriptor = klass.__dict__["Customer_Name"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_orders_has_Date_Created():
    assert hasattr(online_shopping_Orders, "Date_Created")
    descriptor = None
    for klass in online_shopping_Orders.__mro__:
        if "Date_Created" in klass.__dict__:
            descriptor = klass.__dict__["Date_Created"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_orders_has_Customer_ID():
    assert hasattr(online_shopping_Orders, "Customer_ID")
    descriptor = None
    for klass in online_shopping_Orders.__mro__:
        if "Customer_ID" in klass.__dict__:
            descriptor = klass.__dict__["Customer_ID"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_orders_has_Order_ID():
    assert hasattr(online_shopping_Orders, "Order_ID")
    descriptor = None
    for klass in online_shopping_Orders.__mro__:
        if "Order_ID" in klass.__dict__:
            descriptor = klass.__dict__["Order_ID"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_orders_has_Datw_Shipping():
    assert hasattr(online_shopping_Orders, "Datw_Shipping")
    descriptor = None
    for klass in online_shopping_Orders.__mro__:
        if "Datw_Shipping" in klass.__dict__:
            descriptor = klass.__dict__["Datw_Shipping"]
            break
    assert isinstance(descriptor, property)



def test_online_shopping_session_manager_is_not_abstract():
    assert not inspect.isabstract(online_shopping_Session_manager)


def test_online_shopping_session_manager_constructor_exists():
    assert callable(online_shopping_Session_manager.__init__)


def test_online_shopping_session_manager_constructor_args():
    sig = inspect.signature(online_shopping_Session_manager.__init__)
    params = list(sig.parameters.keys())
    assert "Department_Name" in params, "Missing parameter 'Department_Name'"
    assert "Person_ID" in params, "Missing parameter 'Person_ID'"

def test_online_shopping_session_manager_has_Department_Name():
    assert hasattr(online_shopping_Session_manager, "Department_Name")
    descriptor = None
    for klass in online_shopping_Session_manager.__mro__:
        if "Department_Name" in klass.__dict__:
            descriptor = klass.__dict__["Department_Name"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_session_manager_has_Person_ID():
    assert hasattr(online_shopping_Session_manager, "Person_ID")
    descriptor = None
    for klass in online_shopping_Session_manager.__mro__:
        if "Person_ID" in klass.__dict__:
            descriptor = klass.__dict__["Person_ID"]
            break
    assert isinstance(descriptor, property)



def test_online_shopping_deoartment_is_not_abstract():
    assert not inspect.isabstract(online_shopping_Deoartment)


def test_online_shopping_deoartment_constructor_exists():
    assert callable(online_shopping_Deoartment.__init__)


def test_online_shopping_deoartment_constructor_args():
    sig = inspect.signature(online_shopping_Deoartment.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Description" in params, "Missing parameter 'Description'"
    assert "Department_ID" in params, "Missing parameter 'Department_ID'"

def test_online_shopping_deoartment_has_Name():
    assert hasattr(online_shopping_Deoartment, "Name")
    descriptor = None
    for klass in online_shopping_Deoartment.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_deoartment_has_Description():
    assert hasattr(online_shopping_Deoartment, "Description")
    descriptor = None
    for klass in online_shopping_Deoartment.__mro__:
        if "Description" in klass.__dict__:
            descriptor = klass.__dict__["Description"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_deoartment_has_Department_ID():
    assert hasattr(online_shopping_Deoartment, "Department_ID")
    descriptor = None
    for klass in online_shopping_Deoartment.__mro__:
        if "Department_ID" in klass.__dict__:
            descriptor = klass.__dict__["Department_ID"]
            break
    assert isinstance(descriptor, property)



def test_online_shopping_administrator_is_not_abstract():
    assert not inspect.isabstract(online_shopping_Administrator)


def test_online_shopping_administrator_constructor_exists():
    assert callable(online_shopping_Administrator.__init__)


def test_online_shopping_administrator_constructor_args():
    sig = inspect.signature(online_shopping_Administrator.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Email" in params, "Missing parameter 'Email'"

def test_online_shopping_administrator_has_Name():
    assert hasattr(online_shopping_Administrator, "Name")
    descriptor = None
    for klass in online_shopping_Administrator.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_administrator_has_Email():
    assert hasattr(online_shopping_Administrator, "Email")
    descriptor = None
    for klass in online_shopping_Administrator.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)



def test_online_shopping_person_is_not_abstract():
    assert not inspect.isabstract(online_shopping_Person)


def test_online_shopping_person_constructor_exists():
    assert callable(online_shopping_Person.__init__)


def test_online_shopping_person_constructor_args():
    sig = inspect.signature(online_shopping_Person.__init__)
    params = list(sig.parameters.keys())
    assert "Person_Password" in params, "Missing parameter 'Person_Password'"
    assert "Login_Status" in params, "Missing parameter 'Login_Status'"
    assert "Person_ID" in params, "Missing parameter 'Person_ID'"

def test_online_shopping_person_has_Person_Password():
    assert hasattr(online_shopping_Person, "Person_Password")
    descriptor = None
    for klass in online_shopping_Person.__mro__:
        if "Person_Password" in klass.__dict__:
            descriptor = klass.__dict__["Person_Password"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_person_has_Login_Status():
    assert hasattr(online_shopping_Person, "Login_Status")
    descriptor = None
    for klass in online_shopping_Person.__mro__:
        if "Login_Status" in klass.__dict__:
            descriptor = klass.__dict__["Login_Status"]
            break
    assert isinstance(descriptor, property)

def test_online_shopping_person_has_Person_ID():
    assert hasattr(online_shopping_Person, "Person_ID")
    descriptor = None
    for klass in online_shopping_Person.__mro__:
        if "Person_ID" in klass.__dict__:
            descriptor = klass.__dict__["Person_ID"]
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
Estring_Interface_strategy = st.builds(
    Estring_Interface,
)
online_shopping_Order_Detail_strategy = st.builds(
    online_shopping_Order_Detail,
    Quantity=
        safe_text,
    unit_Cost=
        safe_text,
    Subtotal=
        safe_text,
    Product_Name=
        st.none(),
    Order_ID=
        safe_text,
    Product_ID=
        safe_text
)
online_shopping_Delivertiony_Informa_strategy = st.builds(
    online_shopping_Delivertiony_Informa,
    Receiver_Name=
        st.none(),
    Other_Delivery_Address=
        st.none(),
    Delivery_Address=
        st.none(),
    Delivery_Phone=
        safe_text
)
online_shopping_Payment_strategy = st.builds(
    online_shopping_Payment,
    Catch_Pay=
        safe_text,
    Online_Pay=
        safe_text
)
online_shopping_Product_strategy = st.builds(
    online_shopping_Product,
    Image_File_Name=
        st.none(),
    Name=
        st.none(),
    Price=
        safe_text,
    Description=
        st.none(),
    Product_ID=
        safe_text
)
online_shopping_Category_strategy = st.builds(
    online_shopping_Category,
    Category_ID=
        safe_text,
    Department_ID=
        safe_text,
    Description=
        st.none(),
    Catemegory_Name=
        st.none()
)
online_shopping_Shopping_Card_strategy = st.builds(
    online_shopping_Shopping_Card,
    Date_Added=
        safe_text,
    Quantity=
        safe_text,
    Produced_Id=
        safe_text,
    Cart_ID=
        safe_text
)
online_shopping_Customer_strategy = st.builds(
    online_shopping_Customer,
    Name=
        st.none(),
    Address=
        st.none(),
    Shippinginfo=
        st.none(),
    Phone=
        safe_text,
    E_mail=
        st.none()
)
online_shopping_Orders_strategy = st.builds(
    online_shopping_Orders,
    Customer_Name=
        st.none(),
    Date_Created=
        st.none(),
    Customer_ID=
        st.none(),
    Order_ID=
        st.integers(),
    Datw_Shipping=
        st.none()
)
online_shopping_Session_manager_strategy = st.builds(
    online_shopping_Session_manager,
    Department_Name=
        st.none(),
    Person_ID=
        st.none()
)
online_shopping_Deoartment_strategy = st.builds(
    online_shopping_Deoartment,
    Name=
        safe_text,
    Description=
        safe_text,
    Department_ID=
        safe_text
)
online_shopping_Administrator_strategy = st.builds(
    online_shopping_Administrator,
    Name=
        st.none(),
    Email=
        st.none()
)
online_shopping_Person_strategy = st.builds(
    online_shopping_Person,
    Person_Password=
        st.none(),
    Login_Status=
        st.none(),
    Person_ID=
        st.none()
)

@given(instance=Estring_Interface_strategy)
@settings(max_examples=50)
def test_estring_interface_instantiation(instance):
    assert isinstance(instance, Estring_Interface)

@given(instance=online_shopping_Order_Detail_strategy)
@settings(max_examples=50)
def test_online_shopping_order_detail_instantiation(instance):
    assert isinstance(instance, online_shopping_Order_Detail)



@given(instance=online_shopping_Order_Detail_strategy)
def test_online_shopping_order_detail_Quantity_setter(instance):
    original = instance.Quantity
    instance.Quantity = original
    assert instance.Quantity == original



@given(instance=online_shopping_Order_Detail_strategy)
def test_online_shopping_order_detail_unit_Cost_setter(instance):
    original = instance.unit_Cost
    instance.unit_Cost = original
    assert instance.unit_Cost == original



@given(instance=online_shopping_Order_Detail_strategy)
def test_online_shopping_order_detail_Subtotal_setter(instance):
    original = instance.Subtotal
    instance.Subtotal = original
    assert instance.Subtotal == original



@given(instance=online_shopping_Order_Detail_strategy)
def test_online_shopping_order_detail_Product_Name_setter(instance):
    original = instance.Product_Name
    instance.Product_Name = original
    assert instance.Product_Name == original



@given(instance=online_shopping_Order_Detail_strategy)
def test_online_shopping_order_detail_Order_ID_setter(instance):
    original = instance.Order_ID
    instance.Order_ID = original
    assert instance.Order_ID == original



@given(instance=online_shopping_Order_Detail_strategy)
def test_online_shopping_order_detail_Product_ID_setter(instance):
    original = instance.Product_ID
    instance.Product_ID = original
    assert instance.Product_ID == original

@given(instance=online_shopping_Delivertiony_Informa_strategy)
@settings(max_examples=50)
def test_online_shopping_delivertiony_informa_instantiation(instance):
    assert isinstance(instance, online_shopping_Delivertiony_Informa)



@given(instance=online_shopping_Delivertiony_Informa_strategy)
def test_online_shopping_delivertiony_informa_Receiver_Name_setter(instance):
    original = instance.Receiver_Name
    instance.Receiver_Name = original
    assert instance.Receiver_Name == original



@given(instance=online_shopping_Delivertiony_Informa_strategy)
def test_online_shopping_delivertiony_informa_Other_Delivery_Address_setter(instance):
    original = instance.Other_Delivery_Address
    instance.Other_Delivery_Address = original
    assert instance.Other_Delivery_Address == original



@given(instance=online_shopping_Delivertiony_Informa_strategy)
def test_online_shopping_delivertiony_informa_Delivery_Address_setter(instance):
    original = instance.Delivery_Address
    instance.Delivery_Address = original
    assert instance.Delivery_Address == original



@given(instance=online_shopping_Delivertiony_Informa_strategy)
def test_online_shopping_delivertiony_informa_Delivery_Phone_setter(instance):
    original = instance.Delivery_Phone
    instance.Delivery_Phone = original
    assert instance.Delivery_Phone == original

@given(instance=online_shopping_Payment_strategy)
@settings(max_examples=50)
def test_online_shopping_payment_instantiation(instance):
    assert isinstance(instance, online_shopping_Payment)



@given(instance=online_shopping_Payment_strategy)
def test_online_shopping_payment_Catch_Pay_setter(instance):
    original = instance.Catch_Pay
    instance.Catch_Pay = original
    assert instance.Catch_Pay == original



@given(instance=online_shopping_Payment_strategy)
def test_online_shopping_payment_Online_Pay_setter(instance):
    original = instance.Online_Pay
    instance.Online_Pay = original
    assert instance.Online_Pay == original

@given(instance=online_shopping_Product_strategy)
@settings(max_examples=50)
def test_online_shopping_product_instantiation(instance):
    assert isinstance(instance, online_shopping_Product)



@given(instance=online_shopping_Product_strategy)
def test_online_shopping_product_Image_File_Name_setter(instance):
    original = instance.Image_File_Name
    instance.Image_File_Name = original
    assert instance.Image_File_Name == original



@given(instance=online_shopping_Product_strategy)
def test_online_shopping_product_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=online_shopping_Product_strategy)
def test_online_shopping_product_Price_setter(instance):
    original = instance.Price
    instance.Price = original
    assert instance.Price == original



@given(instance=online_shopping_Product_strategy)
def test_online_shopping_product_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original



@given(instance=online_shopping_Product_strategy)
def test_online_shopping_product_Product_ID_setter(instance):
    original = instance.Product_ID
    instance.Product_ID = original
    assert instance.Product_ID == original

@given(instance=online_shopping_Category_strategy)
@settings(max_examples=50)
def test_online_shopping_category_instantiation(instance):
    assert isinstance(instance, online_shopping_Category)



@given(instance=online_shopping_Category_strategy)
def test_online_shopping_category_Category_ID_setter(instance):
    original = instance.Category_ID
    instance.Category_ID = original
    assert instance.Category_ID == original



@given(instance=online_shopping_Category_strategy)
def test_online_shopping_category_Department_ID_setter(instance):
    original = instance.Department_ID
    instance.Department_ID = original
    assert instance.Department_ID == original



@given(instance=online_shopping_Category_strategy)
def test_online_shopping_category_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original



@given(instance=online_shopping_Category_strategy)
def test_online_shopping_category_Catemegory_Name_setter(instance):
    original = instance.Catemegory_Name
    instance.Catemegory_Name = original
    assert instance.Catemegory_Name == original

@given(instance=online_shopping_Shopping_Card_strategy)
@settings(max_examples=50)
def test_online_shopping_shopping_card_instantiation(instance):
    assert isinstance(instance, online_shopping_Shopping_Card)



@given(instance=online_shopping_Shopping_Card_strategy)
def test_online_shopping_shopping_card_Date_Added_setter(instance):
    original = instance.Date_Added
    instance.Date_Added = original
    assert instance.Date_Added == original



@given(instance=online_shopping_Shopping_Card_strategy)
def test_online_shopping_shopping_card_Quantity_setter(instance):
    original = instance.Quantity
    instance.Quantity = original
    assert instance.Quantity == original



@given(instance=online_shopping_Shopping_Card_strategy)
def test_online_shopping_shopping_card_Produced_Id_setter(instance):
    original = instance.Produced_Id
    instance.Produced_Id = original
    assert instance.Produced_Id == original



@given(instance=online_shopping_Shopping_Card_strategy)
def test_online_shopping_shopping_card_Cart_ID_setter(instance):
    original = instance.Cart_ID
    instance.Cart_ID = original
    assert instance.Cart_ID == original

@given(instance=online_shopping_Customer_strategy)
@settings(max_examples=50)
def test_online_shopping_customer_instantiation(instance):
    assert isinstance(instance, online_shopping_Customer)



@given(instance=online_shopping_Customer_strategy)
def test_online_shopping_customer_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=online_shopping_Customer_strategy)
def test_online_shopping_customer_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=online_shopping_Customer_strategy)
def test_online_shopping_customer_Shippinginfo_setter(instance):
    original = instance.Shippinginfo
    instance.Shippinginfo = original
    assert instance.Shippinginfo == original



@given(instance=online_shopping_Customer_strategy)
def test_online_shopping_customer_Phone_setter(instance):
    original = instance.Phone
    instance.Phone = original
    assert instance.Phone == original



@given(instance=online_shopping_Customer_strategy)
def test_online_shopping_customer_E_mail_setter(instance):
    original = instance.E_mail
    instance.E_mail = original
    assert instance.E_mail == original

@given(instance=online_shopping_Orders_strategy)
@settings(max_examples=50)
def test_online_shopping_orders_instantiation(instance):
    assert isinstance(instance, online_shopping_Orders)



@given(instance=online_shopping_Orders_strategy)
def test_online_shopping_orders_Customer_Name_setter(instance):
    original = instance.Customer_Name
    instance.Customer_Name = original
    assert instance.Customer_Name == original



@given(instance=online_shopping_Orders_strategy)
def test_online_shopping_orders_Date_Created_setter(instance):
    original = instance.Date_Created
    instance.Date_Created = original
    assert instance.Date_Created == original



@given(instance=online_shopping_Orders_strategy)
def test_online_shopping_orders_Customer_ID_setter(instance):
    original = instance.Customer_ID
    instance.Customer_ID = original
    assert instance.Customer_ID == original



@given(instance=online_shopping_Orders_strategy)
def test_online_shopping_orders_Order_ID_setter(instance):
    original = instance.Order_ID
    instance.Order_ID = original
    assert instance.Order_ID == original



@given(instance=online_shopping_Orders_strategy)
def test_online_shopping_orders_Datw_Shipping_setter(instance):
    original = instance.Datw_Shipping
    instance.Datw_Shipping = original
    assert instance.Datw_Shipping == original

@given(instance=online_shopping_Session_manager_strategy)
@settings(max_examples=50)
def test_online_shopping_session_manager_instantiation(instance):
    assert isinstance(instance, online_shopping_Session_manager)



@given(instance=online_shopping_Session_manager_strategy)
def test_online_shopping_session_manager_Department_Name_setter(instance):
    original = instance.Department_Name
    instance.Department_Name = original
    assert instance.Department_Name == original



@given(instance=online_shopping_Session_manager_strategy)
def test_online_shopping_session_manager_Person_ID_setter(instance):
    original = instance.Person_ID
    instance.Person_ID = original
    assert instance.Person_ID == original

@given(instance=online_shopping_Deoartment_strategy)
@settings(max_examples=50)
def test_online_shopping_deoartment_instantiation(instance):
    assert isinstance(instance, online_shopping_Deoartment)



@given(instance=online_shopping_Deoartment_strategy)
def test_online_shopping_deoartment_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=online_shopping_Deoartment_strategy)
def test_online_shopping_deoartment_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original



@given(instance=online_shopping_Deoartment_strategy)
def test_online_shopping_deoartment_Department_ID_setter(instance):
    original = instance.Department_ID
    instance.Department_ID = original
    assert instance.Department_ID == original

@given(instance=online_shopping_Administrator_strategy)
@settings(max_examples=50)
def test_online_shopping_administrator_instantiation(instance):
    assert isinstance(instance, online_shopping_Administrator)



@given(instance=online_shopping_Administrator_strategy)
def test_online_shopping_administrator_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=online_shopping_Administrator_strategy)
def test_online_shopping_administrator_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original

@given(instance=online_shopping_Person_strategy)
@settings(max_examples=50)
def test_online_shopping_person_instantiation(instance):
    assert isinstance(instance, online_shopping_Person)



@given(instance=online_shopping_Person_strategy)
def test_online_shopping_person_Person_Password_setter(instance):
    original = instance.Person_Password
    instance.Person_Password = original
    assert instance.Person_Password == original



@given(instance=online_shopping_Person_strategy)
def test_online_shopping_person_Login_Status_setter(instance):
    original = instance.Login_Status
    instance.Login_Status = original
    assert instance.Login_Status == original



@given(instance=online_shopping_Person_strategy)
def test_online_shopping_person_Person_ID_setter(instance):
    original = instance.Person_ID
    instance.Person_ID = original
    assert instance.Person_ID == original
