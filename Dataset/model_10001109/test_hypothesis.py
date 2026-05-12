import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from python_code import (
    Controllers_ProductController,
    Controllers_OrderController,
    Controllers_ShoppingCartController,
    Models_ShippingInfo,
    Models_cartItem,
    Models_Product,
    Models_LoginLog,
    Models_User,
    Models_Order,
    Models_LineItem,
    Models_Customer,
    Models_ShoppingCart,
    dao_ShoppingCartDao_Interface,
    dao_OrderDao_Interface,
    dao_CartItemDao_Interface,
    dao_ShippingInfoDao_Interface,
    dao_LineItemDao_Interface,
    dao_CustomerDao_Interface,
    dao_ProductDao_Interface,
    Models_OrderStatus,
    Models_ShippingType,
    Models_ShoppingCartStatus,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_controllers_productcontroller_is_not_abstract():
    assert not inspect.isabstract(Controllers_ProductController)


def test_controllers_productcontroller_constructor_exists():
    assert callable(Controllers_ProductController.__init__)


def test_controllers_productcontroller_constructor_args():
    sig = inspect.signature(Controllers_ProductController.__init__)
    params = list(sig.parameters.keys())



def test_controllers_ordercontroller_is_not_abstract():
    assert not inspect.isabstract(Controllers_OrderController)


def test_controllers_ordercontroller_constructor_exists():
    assert callable(Controllers_OrderController.__init__)


def test_controllers_ordercontroller_constructor_args():
    sig = inspect.signature(Controllers_OrderController.__init__)
    params = list(sig.parameters.keys())



def test_controllers_shoppingcartcontroller_is_not_abstract():
    assert not inspect.isabstract(Controllers_ShoppingCartController)


def test_controllers_shoppingcartcontroller_constructor_exists():
    assert callable(Controllers_ShoppingCartController.__init__)


def test_controllers_shoppingcartcontroller_constructor_args():
    sig = inspect.signature(Controllers_ShoppingCartController.__init__)
    params = list(sig.parameters.keys())



def test_models_shippinginfo_is_not_abstract():
    assert not inspect.isabstract(Models_ShippingInfo)


def test_models_shippinginfo_constructor_exists():
    assert callable(Models_ShippingInfo.__init__)


def test_models_shippinginfo_constructor_args():
    sig = inspect.signature(Models_ShippingInfo.__init__)
    params = list(sig.parameters.keys())
    assert "shippingtype" in params, "Missing parameter 'shippingtype'"
    assert "shippingcost" in params, "Missing parameter 'shippingcost'"
    assert "shippingid" in params, "Missing parameter 'shippingid'"
    assert "shippingregionid" in params, "Missing parameter 'shippingregionid'"

def test_models_shippinginfo_has_shippingtype():
    assert hasattr(Models_ShippingInfo, "shippingtype")
    descriptor = None
    for klass in Models_ShippingInfo.__mro__:
        if "shippingtype" in klass.__dict__:
            descriptor = klass.__dict__["shippingtype"]
            break
    assert isinstance(descriptor, property)

def test_models_shippinginfo_has_shippingcost():
    assert hasattr(Models_ShippingInfo, "shippingcost")
    descriptor = None
    for klass in Models_ShippingInfo.__mro__:
        if "shippingcost" in klass.__dict__:
            descriptor = klass.__dict__["shippingcost"]
            break
    assert isinstance(descriptor, property)

def test_models_shippinginfo_has_shippingid():
    assert hasattr(Models_ShippingInfo, "shippingid")
    descriptor = None
    for klass in Models_ShippingInfo.__mro__:
        if "shippingid" in klass.__dict__:
            descriptor = klass.__dict__["shippingid"]
            break
    assert isinstance(descriptor, property)

def test_models_shippinginfo_has_shippingregionid():
    assert hasattr(Models_ShippingInfo, "shippingregionid")
    descriptor = None
    for klass in Models_ShippingInfo.__mro__:
        if "shippingregionid" in klass.__dict__:
            descriptor = klass.__dict__["shippingregionid"]
            break
    assert isinstance(descriptor, property)



def test_models_cartitem_is_not_abstract():
    assert not inspect.isabstract(Models_cartItem)


def test_models_cartitem_constructor_exists():
    assert callable(Models_cartItem.__init__)


def test_models_cartitem_constructor_args():
    sig = inspect.signature(Models_cartItem.__init__)
    params = list(sig.parameters.keys())
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "cartId" in params, "Missing parameter 'cartId'"
    assert "name" in params, "Missing parameter 'name'"
    assert "subtotal" in params, "Missing parameter 'subtotal'"
    assert "unitcost" in params, "Missing parameter 'unitcost'"
    assert "deleted" in params, "Missing parameter 'deleted'"

def test_models_cartitem_has_quantity():
    assert hasattr(Models_cartItem, "quantity")
    descriptor = None
    for klass in Models_cartItem.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_models_cartitem_has_cartId():
    assert hasattr(Models_cartItem, "cartId")
    descriptor = None
    for klass in Models_cartItem.__mro__:
        if "cartId" in klass.__dict__:
            descriptor = klass.__dict__["cartId"]
            break
    assert isinstance(descriptor, property)

def test_models_cartitem_has_name():
    assert hasattr(Models_cartItem, "name")
    descriptor = None
    for klass in Models_cartItem.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_models_cartitem_has_subtotal():
    assert hasattr(Models_cartItem, "subtotal")
    descriptor = None
    for klass in Models_cartItem.__mro__:
        if "subtotal" in klass.__dict__:
            descriptor = klass.__dict__["subtotal"]
            break
    assert isinstance(descriptor, property)

def test_models_cartitem_has_unitcost():
    assert hasattr(Models_cartItem, "unitcost")
    descriptor = None
    for klass in Models_cartItem.__mro__:
        if "unitcost" in klass.__dict__:
            descriptor = klass.__dict__["unitcost"]
            break
    assert isinstance(descriptor, property)

def test_models_cartitem_has_deleted():
    assert hasattr(Models_cartItem, "deleted")
    descriptor = None
    for klass in Models_cartItem.__mro__:
        if "deleted" in klass.__dict__:
            descriptor = klass.__dict__["deleted"]
            break
    assert isinstance(descriptor, property)



def test_models_product_is_not_abstract():
    assert not inspect.isabstract(Models_Product)


def test_models_product_constructor_exists():
    assert callable(Models_Product.__init__)


def test_models_product_constructor_args():
    sig = inspect.signature(Models_Product.__init__)
    params = list(sig.parameters.keys())
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "imagefilename" in params, "Missing parameter 'imagefilename'"
    assert "productname" in params, "Missing parameter 'productname'"
    assert "productid" in params, "Missing parameter 'productid'"
    assert "price" in params, "Missing parameter 'price'"

def test_models_product_has_quantity():
    assert hasattr(Models_Product, "quantity")
    descriptor = None
    for klass in Models_Product.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_models_product_has_imagefilename():
    assert hasattr(Models_Product, "imagefilename")
    descriptor = None
    for klass in Models_Product.__mro__:
        if "imagefilename" in klass.__dict__:
            descriptor = klass.__dict__["imagefilename"]
            break
    assert isinstance(descriptor, property)

def test_models_product_has_productname():
    assert hasattr(Models_Product, "productname")
    descriptor = None
    for klass in Models_Product.__mro__:
        if "productname" in klass.__dict__:
            descriptor = klass.__dict__["productname"]
            break
    assert isinstance(descriptor, property)

def test_models_product_has_productid():
    assert hasattr(Models_Product, "productid")
    descriptor = None
    for klass in Models_Product.__mro__:
        if "productid" in klass.__dict__:
            descriptor = klass.__dict__["productid"]
            break
    assert isinstance(descriptor, property)

def test_models_product_has_price():
    assert hasattr(Models_Product, "price")
    descriptor = None
    for klass in Models_Product.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)



def test_models_loginlog_is_not_abstract():
    assert not inspect.isabstract(Models_LoginLog)


def test_models_loginlog_constructor_exists():
    assert callable(Models_LoginLog.__init__)


def test_models_loginlog_constructor_args():
    sig = inspect.signature(Models_LoginLog.__init__)
    params = list(sig.parameters.keys())
    assert "lastLoginDate" in params, "Missing parameter 'lastLoginDate'"
    assert "id" in params, "Missing parameter 'id'"
    assert "user_id" in params, "Missing parameter 'user_id'"
    assert "isLogin" in params, "Missing parameter 'isLogin'"

def test_models_loginlog_has_lastLoginDate():
    assert hasattr(Models_LoginLog, "lastLoginDate")
    descriptor = None
    for klass in Models_LoginLog.__mro__:
        if "lastLoginDate" in klass.__dict__:
            descriptor = klass.__dict__["lastLoginDate"]
            break
    assert isinstance(descriptor, property)

def test_models_loginlog_has_id():
    assert hasattr(Models_LoginLog, "id")
    descriptor = None
    for klass in Models_LoginLog.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_models_loginlog_has_user_id():
    assert hasattr(Models_LoginLog, "user_id")
    descriptor = None
    for klass in Models_LoginLog.__mro__:
        if "user_id" in klass.__dict__:
            descriptor = klass.__dict__["user_id"]
            break
    assert isinstance(descriptor, property)

def test_models_loginlog_has_isLogin():
    assert hasattr(Models_LoginLog, "isLogin")
    descriptor = None
    for klass in Models_LoginLog.__mro__:
        if "isLogin" in klass.__dict__:
            descriptor = klass.__dict__["isLogin"]
            break
    assert isinstance(descriptor, property)



def test_models_user_is_not_abstract():
    assert not inspect.isabstract(Models_User)


def test_models_user_constructor_exists():
    assert callable(Models_User.__init__)


def test_models_user_constructor_args():
    sig = inspect.signature(Models_User.__init__)
    params = list(sig.parameters.keys())
    assert "UserId" in params, "Missing parameter 'UserId'"
    assert "password" in params, "Missing parameter 'password'"
    assert "email" in params, "Missing parameter 'email'"

def test_models_user_has_UserId():
    assert hasattr(Models_User, "UserId")
    descriptor = None
    for klass in Models_User.__mro__:
        if "UserId" in klass.__dict__:
            descriptor = klass.__dict__["UserId"]
            break
    assert isinstance(descriptor, property)

def test_models_user_has_password():
    assert hasattr(Models_User, "password")
    descriptor = None
    for klass in Models_User.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_models_user_has_email():
    assert hasattr(Models_User, "email")
    descriptor = None
    for klass in Models_User.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)



def test_models_order_is_not_abstract():
    assert not inspect.isabstract(Models_Order)


def test_models_order_constructor_exists():
    assert callable(Models_Order.__init__)


def test_models_order_constructor_args():
    sig = inspect.signature(Models_Order.__init__)
    params = list(sig.parameters.keys())
    assert "shippingInfoId" in params, "Missing parameter 'shippingInfoId'"
    assert "dateCreated" in params, "Missing parameter 'dateCreated'"
    assert "dateShipped" in params, "Missing parameter 'dateShipped'"
    assert "customerid" in params, "Missing parameter 'customerid'"
    assert "orderID" in params, "Missing parameter 'orderID'"
    assert "status" in params, "Missing parameter 'status'"

def test_models_order_has_shippingInfoId():
    assert hasattr(Models_Order, "shippingInfoId")
    descriptor = None
    for klass in Models_Order.__mro__:
        if "shippingInfoId" in klass.__dict__:
            descriptor = klass.__dict__["shippingInfoId"]
            break
    assert isinstance(descriptor, property)

def test_models_order_has_dateCreated():
    assert hasattr(Models_Order, "dateCreated")
    descriptor = None
    for klass in Models_Order.__mro__:
        if "dateCreated" in klass.__dict__:
            descriptor = klass.__dict__["dateCreated"]
            break
    assert isinstance(descriptor, property)

def test_models_order_has_dateShipped():
    assert hasattr(Models_Order, "dateShipped")
    descriptor = None
    for klass in Models_Order.__mro__:
        if "dateShipped" in klass.__dict__:
            descriptor = klass.__dict__["dateShipped"]
            break
    assert isinstance(descriptor, property)

def test_models_order_has_customerid():
    assert hasattr(Models_Order, "customerid")
    descriptor = None
    for klass in Models_Order.__mro__:
        if "customerid" in klass.__dict__:
            descriptor = klass.__dict__["customerid"]
            break
    assert isinstance(descriptor, property)

def test_models_order_has_orderID():
    assert hasattr(Models_Order, "orderID")
    descriptor = None
    for klass in Models_Order.__mro__:
        if "orderID" in klass.__dict__:
            descriptor = klass.__dict__["orderID"]
            break
    assert isinstance(descriptor, property)

def test_models_order_has_status():
    assert hasattr(Models_Order, "status")
    descriptor = None
    for klass in Models_Order.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_models_lineitem_is_not_abstract():
    assert not inspect.isabstract(Models_LineItem)


def test_models_lineitem_constructor_exists():
    assert callable(Models_LineItem.__init__)


def test_models_lineitem_constructor_args():
    sig = inspect.signature(Models_LineItem.__init__)
    params = list(sig.parameters.keys())
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "unitcost" in params, "Missing parameter 'unitcost'"
    assert "productid" in params, "Missing parameter 'productid'"
    assert "productname" in params, "Missing parameter 'productname'"
    assert "orderId" in params, "Missing parameter 'orderId'"
    assert "subtotal" in params, "Missing parameter 'subtotal'"

def test_models_lineitem_has_quantity():
    assert hasattr(Models_LineItem, "quantity")
    descriptor = None
    for klass in Models_LineItem.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_models_lineitem_has_unitcost():
    assert hasattr(Models_LineItem, "unitcost")
    descriptor = None
    for klass in Models_LineItem.__mro__:
        if "unitcost" in klass.__dict__:
            descriptor = klass.__dict__["unitcost"]
            break
    assert isinstance(descriptor, property)

def test_models_lineitem_has_productid():
    assert hasattr(Models_LineItem, "productid")
    descriptor = None
    for klass in Models_LineItem.__mro__:
        if "productid" in klass.__dict__:
            descriptor = klass.__dict__["productid"]
            break
    assert isinstance(descriptor, property)

def test_models_lineitem_has_productname():
    assert hasattr(Models_LineItem, "productname")
    descriptor = None
    for klass in Models_LineItem.__mro__:
        if "productname" in klass.__dict__:
            descriptor = klass.__dict__["productname"]
            break
    assert isinstance(descriptor, property)

def test_models_lineitem_has_orderId():
    assert hasattr(Models_LineItem, "orderId")
    descriptor = None
    for klass in Models_LineItem.__mro__:
        if "orderId" in klass.__dict__:
            descriptor = klass.__dict__["orderId"]
            break
    assert isinstance(descriptor, property)

def test_models_lineitem_has_subtotal():
    assert hasattr(Models_LineItem, "subtotal")
    descriptor = None
    for klass in Models_LineItem.__mro__:
        if "subtotal" in klass.__dict__:
            descriptor = klass.__dict__["subtotal"]
            break
    assert isinstance(descriptor, property)



def test_models_customer_is_not_abstract():
    assert not inspect.isabstract(Models_Customer)


def test_models_customer_constructor_exists():
    assert callable(Models_Customer.__init__)


def test_models_customer_constructor_args():
    sig = inspect.signature(Models_Customer.__init__)
    params = list(sig.parameters.keys())
    assert "shippinginfo" in params, "Missing parameter 'shippinginfo'"
    assert "address" in params, "Missing parameter 'address'"
    assert "phoneno" in params, "Missing parameter 'phoneno'"
    assert "coustomername" in params, "Missing parameter 'coustomername'"
    assert "deleted" in params, "Missing parameter 'deleted'"
    assert "creditcardinfo" in params, "Missing parameter 'creditcardinfo'"

def test_models_customer_has_shippinginfo():
    assert hasattr(Models_Customer, "shippinginfo")
    descriptor = None
    for klass in Models_Customer.__mro__:
        if "shippinginfo" in klass.__dict__:
            descriptor = klass.__dict__["shippinginfo"]
            break
    assert isinstance(descriptor, property)

def test_models_customer_has_address():
    assert hasattr(Models_Customer, "address")
    descriptor = None
    for klass in Models_Customer.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_models_customer_has_phoneno():
    assert hasattr(Models_Customer, "phoneno")
    descriptor = None
    for klass in Models_Customer.__mro__:
        if "phoneno" in klass.__dict__:
            descriptor = klass.__dict__["phoneno"]
            break
    assert isinstance(descriptor, property)

def test_models_customer_has_coustomername():
    assert hasattr(Models_Customer, "coustomername")
    descriptor = None
    for klass in Models_Customer.__mro__:
        if "coustomername" in klass.__dict__:
            descriptor = klass.__dict__["coustomername"]
            break
    assert isinstance(descriptor, property)

def test_models_customer_has_deleted():
    assert hasattr(Models_Customer, "deleted")
    descriptor = None
    for klass in Models_Customer.__mro__:
        if "deleted" in klass.__dict__:
            descriptor = klass.__dict__["deleted"]
            break
    assert isinstance(descriptor, property)

def test_models_customer_has_creditcardinfo():
    assert hasattr(Models_Customer, "creditcardinfo")
    descriptor = None
    for klass in Models_Customer.__mro__:
        if "creditcardinfo" in klass.__dict__:
            descriptor = klass.__dict__["creditcardinfo"]
            break
    assert isinstance(descriptor, property)



def test_models_shoppingcart_is_not_abstract():
    assert not inspect.isabstract(Models_ShoppingCart)


def test_models_shoppingcart_constructor_exists():
    assert callable(Models_ShoppingCart.__init__)


def test_models_shoppingcart_constructor_args():
    sig = inspect.signature(Models_ShoppingCart.__init__)
    params = list(sig.parameters.keys())
    assert "dateAdded" in params, "Missing parameter 'dateAdded'"
    assert "status" in params, "Missing parameter 'status'"
    assert "deleted" in params, "Missing parameter 'deleted'"
    assert "cartId" in params, "Missing parameter 'cartId'"
    assert "customerId" in params, "Missing parameter 'customerId'"

def test_models_shoppingcart_has_dateAdded():
    assert hasattr(Models_ShoppingCart, "dateAdded")
    descriptor = None
    for klass in Models_ShoppingCart.__mro__:
        if "dateAdded" in klass.__dict__:
            descriptor = klass.__dict__["dateAdded"]
            break
    assert isinstance(descriptor, property)

def test_models_shoppingcart_has_status():
    assert hasattr(Models_ShoppingCart, "status")
    descriptor = None
    for klass in Models_ShoppingCart.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_models_shoppingcart_has_deleted():
    assert hasattr(Models_ShoppingCart, "deleted")
    descriptor = None
    for klass in Models_ShoppingCart.__mro__:
        if "deleted" in klass.__dict__:
            descriptor = klass.__dict__["deleted"]
            break
    assert isinstance(descriptor, property)

def test_models_shoppingcart_has_cartId():
    assert hasattr(Models_ShoppingCart, "cartId")
    descriptor = None
    for klass in Models_ShoppingCart.__mro__:
        if "cartId" in klass.__dict__:
            descriptor = klass.__dict__["cartId"]
            break
    assert isinstance(descriptor, property)

def test_models_shoppingcart_has_customerId():
    assert hasattr(Models_ShoppingCart, "customerId")
    descriptor = None
    for klass in Models_ShoppingCart.__mro__:
        if "customerId" in klass.__dict__:
            descriptor = klass.__dict__["customerId"]
            break
    assert isinstance(descriptor, property)



def test_dao_shoppingcartdao_interface_is_not_abstract():
    assert not inspect.isabstract(dao_ShoppingCartDao_Interface)


def test_dao_shoppingcartdao_interface_constructor_exists():
    assert callable(dao_ShoppingCartDao_Interface.__init__)


def test_dao_shoppingcartdao_interface_constructor_args():
    sig = inspect.signature(dao_ShoppingCartDao_Interface.__init__)
    params = list(sig.parameters.keys())



def test_dao_orderdao_interface_is_not_abstract():
    assert not inspect.isabstract(dao_OrderDao_Interface)


def test_dao_orderdao_interface_constructor_exists():
    assert callable(dao_OrderDao_Interface.__init__)


def test_dao_orderdao_interface_constructor_args():
    sig = inspect.signature(dao_OrderDao_Interface.__init__)
    params = list(sig.parameters.keys())



def test_dao_cartitemdao_interface_is_not_abstract():
    assert not inspect.isabstract(dao_CartItemDao_Interface)


def test_dao_cartitemdao_interface_constructor_exists():
    assert callable(dao_CartItemDao_Interface.__init__)


def test_dao_cartitemdao_interface_constructor_args():
    sig = inspect.signature(dao_CartItemDao_Interface.__init__)
    params = list(sig.parameters.keys())



def test_dao_shippinginfodao_interface_is_not_abstract():
    assert not inspect.isabstract(dao_ShippingInfoDao_Interface)


def test_dao_shippinginfodao_interface_constructor_exists():
    assert callable(dao_ShippingInfoDao_Interface.__init__)


def test_dao_shippinginfodao_interface_constructor_args():
    sig = inspect.signature(dao_ShippingInfoDao_Interface.__init__)
    params = list(sig.parameters.keys())



def test_dao_lineitemdao_interface_is_not_abstract():
    assert not inspect.isabstract(dao_LineItemDao_Interface)


def test_dao_lineitemdao_interface_constructor_exists():
    assert callable(dao_LineItemDao_Interface.__init__)


def test_dao_lineitemdao_interface_constructor_args():
    sig = inspect.signature(dao_LineItemDao_Interface.__init__)
    params = list(sig.parameters.keys())



def test_dao_customerdao_interface_is_not_abstract():
    assert not inspect.isabstract(dao_CustomerDao_Interface)


def test_dao_customerdao_interface_constructor_exists():
    assert callable(dao_CustomerDao_Interface.__init__)


def test_dao_customerdao_interface_constructor_args():
    sig = inspect.signature(dao_CustomerDao_Interface.__init__)
    params = list(sig.parameters.keys())



def test_dao_productdao_interface_is_not_abstract():
    assert not inspect.isabstract(dao_ProductDao_Interface)


def test_dao_productdao_interface_constructor_exists():
    assert callable(dao_ProductDao_Interface.__init__)


def test_dao_productdao_interface_constructor_args():
    sig = inspect.signature(dao_ProductDao_Interface.__init__)
    params = list(sig.parameters.keys())

def test_models_orderstatus_exists():
    # Check that the Enumeration exists
    assert Models_OrderStatus is not None

def test_models_orderstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Models_OrderStatus]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Models_OrderStatus"

def test_models_shippingtype_exists():
    # Check that the Enumeration exists
    assert Models_ShippingType is not None

def test_models_shippingtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Models_ShippingType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Models_ShippingType"

def test_models_shoppingcartstatus_exists():
    # Check that the Enumeration exists
    assert Models_ShoppingCartStatus is not None

def test_models_shoppingcartstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Models_ShoppingCartStatus]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Models_ShoppingCartStatus"


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
Controllers_ProductController_strategy = st.builds(
    Controllers_ProductController,
)
Controllers_OrderController_strategy = st.builds(
    Controllers_OrderController,
)
Controllers_ShoppingCartController_strategy = st.builds(
    Controllers_ShoppingCartController,
)
Models_ShippingInfo_strategy = st.builds(
    Models_ShippingInfo,
    shippingtype=
        safe_text,
    shippingcost=
        st.integers(),
    shippingid=
        st.integers(),
    shippingregionid=
        st.integers()
)
Models_cartItem_strategy = st.builds(
    Models_cartItem,
    quantity=
        st.integers(),
    cartId=
        st.integers(),
    name=
        safe_text,
    subtotal=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    unitcost=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    deleted=
        st.booleans()
)
Models_Product_strategy = st.builds(
    Models_Product,
    quantity=
        st.integers(),
    imagefilename=
        safe_text,
    productname=
        safe_text,
    productid=
        st.integers(),
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Models_LoginLog_strategy = st.builds(
    Models_LoginLog,
    lastLoginDate=
        st.dates(),
    id=
        st.integers(),
    user_id=
        st.integers(),
    isLogin=
        st.booleans()
)
Models_User_strategy = st.builds(
    Models_User,
    UserId=
        safe_text,
    password=
        safe_text,
    email=
        safe_text
)
Models_Order_strategy = st.builds(
    Models_Order,
    shippingInfoId=
        st.integers(),
    dateCreated=
        st.dates(),
    dateShipped=
        safe_text,
    customerid=
        st.integers(),
    orderID=
        st.integers(),
    status=
        safe_text
)
Models_LineItem_strategy = st.builds(
    Models_LineItem,
    quantity=
        st.integers(),
    unitcost=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    productid=
        st.integers(),
    productname=
        safe_text,
    orderId=
        st.integers(),
    subtotal=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Models_Customer_strategy = st.builds(
    Models_Customer,
    shippinginfo=
        safe_text,
    address=
        safe_text,
    phoneno=
        st.integers(),
    coustomername=
        safe_text,
    deleted=
        st.booleans(),
    creditcardinfo=
        safe_text
)
Models_ShoppingCart_strategy = st.builds(
    Models_ShoppingCart,
    dateAdded=
        st.integers(),
    status=
        st.integers(),
    deleted=
        st.booleans(),
    cartId=
        st.integers(),
    customerId=
        st.integers()
)
dao_ShoppingCartDao_Interface_strategy = st.builds(
    dao_ShoppingCartDao_Interface,
)
dao_OrderDao_Interface_strategy = st.builds(
    dao_OrderDao_Interface,
)
dao_CartItemDao_Interface_strategy = st.builds(
    dao_CartItemDao_Interface,
)
dao_ShippingInfoDao_Interface_strategy = st.builds(
    dao_ShippingInfoDao_Interface,
)
dao_LineItemDao_Interface_strategy = st.builds(
    dao_LineItemDao_Interface,
)
dao_CustomerDao_Interface_strategy = st.builds(
    dao_CustomerDao_Interface,
)
dao_ProductDao_Interface_strategy = st.builds(
    dao_ProductDao_Interface,
)

@given(instance=Controllers_ProductController_strategy)
@settings(max_examples=50)
def test_controllers_productcontroller_instantiation(instance):
    assert isinstance(instance, Controllers_ProductController)

@given(instance=Controllers_OrderController_strategy)
@settings(max_examples=50)
def test_controllers_ordercontroller_instantiation(instance):
    assert isinstance(instance, Controllers_OrderController)

@given(instance=Controllers_ShoppingCartController_strategy)
@settings(max_examples=50)
def test_controllers_shoppingcartcontroller_instantiation(instance):
    assert isinstance(instance, Controllers_ShoppingCartController)

@given(instance=Models_ShippingInfo_strategy)
@settings(max_examples=50)
def test_models_shippinginfo_instantiation(instance):
    assert isinstance(instance, Models_ShippingInfo)

@given(instance=Models_ShippingInfo_strategy)
def test_models_shippinginfo_shippingtype_type(instance):
    assert isinstance(instance.shippingtype, str)


@given(instance=Models_ShippingInfo_strategy)
def test_models_shippinginfo_shippingtype_setter(instance):
    original = instance.shippingtype
    instance.shippingtype = original
    assert instance.shippingtype == original

@given(instance=Models_ShippingInfo_strategy)
def test_models_shippinginfo_shippingcost_type(instance):
    assert isinstance(instance.shippingcost, int)


@given(instance=Models_ShippingInfo_strategy)
def test_models_shippinginfo_shippingcost_setter(instance):
    original = instance.shippingcost
    instance.shippingcost = original
    assert instance.shippingcost == original

@given(instance=Models_ShippingInfo_strategy)
def test_models_shippinginfo_shippingid_type(instance):
    assert isinstance(instance.shippingid, int)


@given(instance=Models_ShippingInfo_strategy)
def test_models_shippinginfo_shippingid_setter(instance):
    original = instance.shippingid
    instance.shippingid = original
    assert instance.shippingid == original

@given(instance=Models_ShippingInfo_strategy)
def test_models_shippinginfo_shippingregionid_type(instance):
    assert isinstance(instance.shippingregionid, int)


@given(instance=Models_ShippingInfo_strategy)
def test_models_shippinginfo_shippingregionid_setter(instance):
    original = instance.shippingregionid
    instance.shippingregionid = original
    assert instance.shippingregionid == original

@given(instance=Models_cartItem_strategy)
@settings(max_examples=50)
def test_models_cartitem_instantiation(instance):
    assert isinstance(instance, Models_cartItem)

@given(instance=Models_cartItem_strategy)
def test_models_cartitem_quantity_type(instance):
    assert isinstance(instance.quantity, int)


@given(instance=Models_cartItem_strategy)
def test_models_cartitem_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original

@given(instance=Models_cartItem_strategy)
def test_models_cartitem_cartId_type(instance):
    assert isinstance(instance.cartId, int)


@given(instance=Models_cartItem_strategy)
def test_models_cartitem_cartId_setter(instance):
    original = instance.cartId
    instance.cartId = original
    assert instance.cartId == original

@given(instance=Models_cartItem_strategy)
def test_models_cartitem_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Models_cartItem_strategy)
def test_models_cartitem_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Models_cartItem_strategy)
def test_models_cartitem_subtotal_type(instance):
    assert isinstance(instance.subtotal, float)


@given(instance=Models_cartItem_strategy)
def test_models_cartitem_subtotal_setter(instance):
    original = instance.subtotal
    instance.subtotal = original
    assert instance.subtotal == original

@given(instance=Models_cartItem_strategy)
def test_models_cartitem_unitcost_type(instance):
    assert isinstance(instance.unitcost, float)


@given(instance=Models_cartItem_strategy)
def test_models_cartitem_unitcost_setter(instance):
    original = instance.unitcost
    instance.unitcost = original
    assert instance.unitcost == original

@given(instance=Models_cartItem_strategy)
def test_models_cartitem_deleted_type(instance):
    assert isinstance(instance.deleted, bool)


@given(instance=Models_cartItem_strategy)
def test_models_cartitem_deleted_setter(instance):
    original = instance.deleted
    instance.deleted = original
    assert instance.deleted == original

@given(instance=Models_Product_strategy)
@settings(max_examples=50)
def test_models_product_instantiation(instance):
    assert isinstance(instance, Models_Product)

@given(instance=Models_Product_strategy)
def test_models_product_quantity_type(instance):
    assert isinstance(instance.quantity, int)


@given(instance=Models_Product_strategy)
def test_models_product_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original

@given(instance=Models_Product_strategy)
def test_models_product_imagefilename_type(instance):
    assert isinstance(instance.imagefilename, str)


@given(instance=Models_Product_strategy)
def test_models_product_imagefilename_setter(instance):
    original = instance.imagefilename
    instance.imagefilename = original
    assert instance.imagefilename == original

@given(instance=Models_Product_strategy)
def test_models_product_productname_type(instance):
    assert isinstance(instance.productname, str)


@given(instance=Models_Product_strategy)
def test_models_product_productname_setter(instance):
    original = instance.productname
    instance.productname = original
    assert instance.productname == original

@given(instance=Models_Product_strategy)
def test_models_product_productid_type(instance):
    assert isinstance(instance.productid, int)


@given(instance=Models_Product_strategy)
def test_models_product_productid_setter(instance):
    original = instance.productid
    instance.productid = original
    assert instance.productid == original

@given(instance=Models_Product_strategy)
def test_models_product_price_type(instance):
    assert isinstance(instance.price, float)


@given(instance=Models_Product_strategy)
def test_models_product_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=Models_LoginLog_strategy)
@settings(max_examples=50)
def test_models_loginlog_instantiation(instance):
    assert isinstance(instance, Models_LoginLog)

@given(instance=Models_LoginLog_strategy)
def test_models_loginlog_lastLoginDate_type(instance):
    assert isinstance(instance.lastLoginDate, date)


@given(instance=Models_LoginLog_strategy)
def test_models_loginlog_lastLoginDate_setter(instance):
    original = instance.lastLoginDate
    instance.lastLoginDate = original
    assert instance.lastLoginDate == original

@given(instance=Models_LoginLog_strategy)
def test_models_loginlog_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=Models_LoginLog_strategy)
def test_models_loginlog_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Models_LoginLog_strategy)
def test_models_loginlog_user_id_type(instance):
    assert isinstance(instance.user_id, int)


@given(instance=Models_LoginLog_strategy)
def test_models_loginlog_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original

@given(instance=Models_LoginLog_strategy)
def test_models_loginlog_isLogin_type(instance):
    assert isinstance(instance.isLogin, bool)


@given(instance=Models_LoginLog_strategy)
def test_models_loginlog_isLogin_setter(instance):
    original = instance.isLogin
    instance.isLogin = original
    assert instance.isLogin == original

@given(instance=Models_User_strategy)
@settings(max_examples=50)
def test_models_user_instantiation(instance):
    assert isinstance(instance, Models_User)

@given(instance=Models_User_strategy)
def test_models_user_UserId_type(instance):
    assert isinstance(instance.UserId, str)


@given(instance=Models_User_strategy)
def test_models_user_UserId_setter(instance):
    original = instance.UserId
    instance.UserId = original
    assert instance.UserId == original

@given(instance=Models_User_strategy)
def test_models_user_password_type(instance):
    assert isinstance(instance.password, str)


@given(instance=Models_User_strategy)
def test_models_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=Models_User_strategy)
def test_models_user_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=Models_User_strategy)
def test_models_user_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=Models_Order_strategy)
@settings(max_examples=50)
def test_models_order_instantiation(instance):
    assert isinstance(instance, Models_Order)

@given(instance=Models_Order_strategy)
def test_models_order_shippingInfoId_type(instance):
    assert isinstance(instance.shippingInfoId, int)


@given(instance=Models_Order_strategy)
def test_models_order_shippingInfoId_setter(instance):
    original = instance.shippingInfoId
    instance.shippingInfoId = original
    assert instance.shippingInfoId == original

@given(instance=Models_Order_strategy)
def test_models_order_dateCreated_type(instance):
    assert isinstance(instance.dateCreated, date)


@given(instance=Models_Order_strategy)
def test_models_order_dateCreated_setter(instance):
    original = instance.dateCreated
    instance.dateCreated = original
    assert instance.dateCreated == original

@given(instance=Models_Order_strategy)
def test_models_order_dateShipped_type(instance):
    assert isinstance(instance.dateShipped, str)


@given(instance=Models_Order_strategy)
def test_models_order_dateShipped_setter(instance):
    original = instance.dateShipped
    instance.dateShipped = original
    assert instance.dateShipped == original

@given(instance=Models_Order_strategy)
def test_models_order_customerid_type(instance):
    assert isinstance(instance.customerid, int)


@given(instance=Models_Order_strategy)
def test_models_order_customerid_setter(instance):
    original = instance.customerid
    instance.customerid = original
    assert instance.customerid == original

@given(instance=Models_Order_strategy)
def test_models_order_orderID_type(instance):
    assert isinstance(instance.orderID, int)


@given(instance=Models_Order_strategy)
def test_models_order_orderID_setter(instance):
    original = instance.orderID
    instance.orderID = original
    assert instance.orderID == original

@given(instance=Models_Order_strategy)
def test_models_order_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=Models_Order_strategy)
def test_models_order_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=Models_LineItem_strategy)
@settings(max_examples=50)
def test_models_lineitem_instantiation(instance):
    assert isinstance(instance, Models_LineItem)

@given(instance=Models_LineItem_strategy)
def test_models_lineitem_quantity_type(instance):
    assert isinstance(instance.quantity, int)


@given(instance=Models_LineItem_strategy)
def test_models_lineitem_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original

@given(instance=Models_LineItem_strategy)
def test_models_lineitem_unitcost_type(instance):
    assert isinstance(instance.unitcost, float)


@given(instance=Models_LineItem_strategy)
def test_models_lineitem_unitcost_setter(instance):
    original = instance.unitcost
    instance.unitcost = original
    assert instance.unitcost == original

@given(instance=Models_LineItem_strategy)
def test_models_lineitem_productid_type(instance):
    assert isinstance(instance.productid, int)


@given(instance=Models_LineItem_strategy)
def test_models_lineitem_productid_setter(instance):
    original = instance.productid
    instance.productid = original
    assert instance.productid == original

@given(instance=Models_LineItem_strategy)
def test_models_lineitem_productname_type(instance):
    assert isinstance(instance.productname, str)


@given(instance=Models_LineItem_strategy)
def test_models_lineitem_productname_setter(instance):
    original = instance.productname
    instance.productname = original
    assert instance.productname == original

@given(instance=Models_LineItem_strategy)
def test_models_lineitem_orderId_type(instance):
    assert isinstance(instance.orderId, int)


@given(instance=Models_LineItem_strategy)
def test_models_lineitem_orderId_setter(instance):
    original = instance.orderId
    instance.orderId = original
    assert instance.orderId == original

@given(instance=Models_LineItem_strategy)
def test_models_lineitem_subtotal_type(instance):
    assert isinstance(instance.subtotal, float)


@given(instance=Models_LineItem_strategy)
def test_models_lineitem_subtotal_setter(instance):
    original = instance.subtotal
    instance.subtotal = original
    assert instance.subtotal == original

@given(instance=Models_Customer_strategy)
@settings(max_examples=50)
def test_models_customer_instantiation(instance):
    assert isinstance(instance, Models_Customer)

@given(instance=Models_Customer_strategy)
def test_models_customer_shippinginfo_type(instance):
    assert isinstance(instance.shippinginfo, str)


@given(instance=Models_Customer_strategy)
def test_models_customer_shippinginfo_setter(instance):
    original = instance.shippinginfo
    instance.shippinginfo = original
    assert instance.shippinginfo == original

@given(instance=Models_Customer_strategy)
def test_models_customer_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=Models_Customer_strategy)
def test_models_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=Models_Customer_strategy)
def test_models_customer_phoneno_type(instance):
    assert isinstance(instance.phoneno, int)


@given(instance=Models_Customer_strategy)
def test_models_customer_phoneno_setter(instance):
    original = instance.phoneno
    instance.phoneno = original
    assert instance.phoneno == original

@given(instance=Models_Customer_strategy)
def test_models_customer_coustomername_type(instance):
    assert isinstance(instance.coustomername, str)


@given(instance=Models_Customer_strategy)
def test_models_customer_coustomername_setter(instance):
    original = instance.coustomername
    instance.coustomername = original
    assert instance.coustomername == original

@given(instance=Models_Customer_strategy)
def test_models_customer_deleted_type(instance):
    assert isinstance(instance.deleted, bool)


@given(instance=Models_Customer_strategy)
def test_models_customer_deleted_setter(instance):
    original = instance.deleted
    instance.deleted = original
    assert instance.deleted == original

@given(instance=Models_Customer_strategy)
def test_models_customer_creditcardinfo_type(instance):
    assert isinstance(instance.creditcardinfo, str)


@given(instance=Models_Customer_strategy)
def test_models_customer_creditcardinfo_setter(instance):
    original = instance.creditcardinfo
    instance.creditcardinfo = original
    assert instance.creditcardinfo == original

@given(instance=Models_ShoppingCart_strategy)
@settings(max_examples=50)
def test_models_shoppingcart_instantiation(instance):
    assert isinstance(instance, Models_ShoppingCart)

@given(instance=Models_ShoppingCart_strategy)
def test_models_shoppingcart_dateAdded_type(instance):
    assert isinstance(instance.dateAdded, int)


@given(instance=Models_ShoppingCart_strategy)
def test_models_shoppingcart_dateAdded_setter(instance):
    original = instance.dateAdded
    instance.dateAdded = original
    assert instance.dateAdded == original

@given(instance=Models_ShoppingCart_strategy)
def test_models_shoppingcart_status_type(instance):
    assert isinstance(instance.status, int)


@given(instance=Models_ShoppingCart_strategy)
def test_models_shoppingcart_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=Models_ShoppingCart_strategy)
def test_models_shoppingcart_deleted_type(instance):
    assert isinstance(instance.deleted, bool)


@given(instance=Models_ShoppingCart_strategy)
def test_models_shoppingcart_deleted_setter(instance):
    original = instance.deleted
    instance.deleted = original
    assert instance.deleted == original

@given(instance=Models_ShoppingCart_strategy)
def test_models_shoppingcart_cartId_type(instance):
    assert isinstance(instance.cartId, int)


@given(instance=Models_ShoppingCart_strategy)
def test_models_shoppingcart_cartId_setter(instance):
    original = instance.cartId
    instance.cartId = original
    assert instance.cartId == original

@given(instance=Models_ShoppingCart_strategy)
def test_models_shoppingcart_customerId_type(instance):
    assert isinstance(instance.customerId, int)


@given(instance=Models_ShoppingCart_strategy)
def test_models_shoppingcart_customerId_setter(instance):
    original = instance.customerId
    instance.customerId = original
    assert instance.customerId == original

@given(instance=dao_ShoppingCartDao_Interface_strategy)
@settings(max_examples=50)
def test_dao_shoppingcartdao_interface_instantiation(instance):
    assert isinstance(instance, dao_ShoppingCartDao_Interface)

@given(instance=dao_OrderDao_Interface_strategy)
@settings(max_examples=50)
def test_dao_orderdao_interface_instantiation(instance):
    assert isinstance(instance, dao_OrderDao_Interface)

@given(instance=dao_CartItemDao_Interface_strategy)
@settings(max_examples=50)
def test_dao_cartitemdao_interface_instantiation(instance):
    assert isinstance(instance, dao_CartItemDao_Interface)

@given(instance=dao_ShippingInfoDao_Interface_strategy)
@settings(max_examples=50)
def test_dao_shippinginfodao_interface_instantiation(instance):
    assert isinstance(instance, dao_ShippingInfoDao_Interface)

@given(instance=dao_LineItemDao_Interface_strategy)
@settings(max_examples=50)
def test_dao_lineitemdao_interface_instantiation(instance):
    assert isinstance(instance, dao_LineItemDao_Interface)

@given(instance=dao_CustomerDao_Interface_strategy)
@settings(max_examples=50)
def test_dao_customerdao_interface_instantiation(instance):
    assert isinstance(instance, dao_CustomerDao_Interface)

@given(instance=dao_ProductDao_Interface_strategy)
@settings(max_examples=50)
def test_dao_productdao_interface_instantiation(instance):
    assert isinstance(instance, dao_ProductDao_Interface)
