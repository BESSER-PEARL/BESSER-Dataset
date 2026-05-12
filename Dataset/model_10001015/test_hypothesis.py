import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    User,
    Cart,
    Appliances,
    Electronics,
    Ornaments,
    Payment_Interface,
    CreditCardPayment,
    DebitCardPayment,
    PaymentFactory,
    Seller,
    ShippingInfo,
    ProductListHelper,
    WishList,
    Order,
    List_Product_,
    Product,
    Customer,
    Guest,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "userId" in params, "Missing parameter 'userId'"

def test_user_has_userId():
    assert hasattr(User, "userId")
    descriptor = None
    for klass in User.__mro__:
        if "userId" in klass.__dict__:
            descriptor = klass.__dict__["userId"]
            break
    assert isinstance(descriptor, property)



def test_cart_is_not_abstract():
    assert not inspect.isabstract(Cart)


def test_cart_constructor_exists():
    assert callable(Cart.__init__)


def test_cart_constructor_args():
    sig = inspect.signature(Cart.__init__)
    params = list(sig.parameters.keys())



def test_appliances_is_not_abstract():
    assert not inspect.isabstract(Appliances)


def test_appliances_constructor_exists():
    assert callable(Appliances.__init__)


def test_appliances_constructor_args():
    sig = inspect.signature(Appliances.__init__)
    params = list(sig.parameters.keys())



def test_electronics_is_not_abstract():
    assert not inspect.isabstract(Electronics)


def test_electronics_constructor_exists():
    assert callable(Electronics.__init__)


def test_electronics_constructor_args():
    sig = inspect.signature(Electronics.__init__)
    params = list(sig.parameters.keys())



def test_ornaments_is_not_abstract():
    assert not inspect.isabstract(Ornaments)


def test_ornaments_constructor_exists():
    assert callable(Ornaments.__init__)


def test_ornaments_constructor_args():
    sig = inspect.signature(Ornaments.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_ornaments_has_Name():
    assert hasattr(Ornaments, "Name")
    descriptor = None
    for klass in Ornaments.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_payment_interface_is_not_abstract():
    assert not inspect.isabstract(Payment_Interface)


def test_payment_interface_constructor_exists():
    assert callable(Payment_Interface.__init__)


def test_payment_interface_constructor_args():
    sig = inspect.signature(Payment_Interface.__init__)
    params = list(sig.parameters.keys())



def test_creditcardpayment_is_not_abstract():
    assert not inspect.isabstract(CreditCardPayment)


def test_creditcardpayment_constructor_exists():
    assert callable(CreditCardPayment.__init__)


def test_creditcardpayment_constructor_args():
    sig = inspect.signature(CreditCardPayment.__init__)
    params = list(sig.parameters.keys())



def test_debitcardpayment_is_not_abstract():
    assert not inspect.isabstract(DebitCardPayment)


def test_debitcardpayment_constructor_exists():
    assert callable(DebitCardPayment.__init__)


def test_debitcardpayment_constructor_args():
    sig = inspect.signature(DebitCardPayment.__init__)
    params = list(sig.parameters.keys())



def test_paymentfactory_is_not_abstract():
    assert not inspect.isabstract(PaymentFactory)


def test_paymentfactory_constructor_exists():
    assert callable(PaymentFactory.__init__)


def test_paymentfactory_constructor_args():
    sig = inspect.signature(PaymentFactory.__init__)
    params = list(sig.parameters.keys())



def test_seller_is_not_abstract():
    assert not inspect.isabstract(Seller)


def test_seller_constructor_exists():
    assert callable(Seller.__init__)


def test_seller_constructor_args():
    sig = inspect.signature(Seller.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "rating" in params, "Missing parameter 'rating'"
    assert "sellerId" in params, "Missing parameter 'sellerId'"

def test_seller_has_name():
    assert hasattr(Seller, "name")
    descriptor = None
    for klass in Seller.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_seller_has_rating():
    assert hasattr(Seller, "rating")
    descriptor = None
    for klass in Seller.__mro__:
        if "rating" in klass.__dict__:
            descriptor = klass.__dict__["rating"]
            break
    assert isinstance(descriptor, property)

def test_seller_has_sellerId():
    assert hasattr(Seller, "sellerId")
    descriptor = None
    for klass in Seller.__mro__:
        if "sellerId" in klass.__dict__:
            descriptor = klass.__dict__["sellerId"]
            break
    assert isinstance(descriptor, property)



def test_shippinginfo_is_not_abstract():
    assert not inspect.isabstract(ShippingInfo)


def test_shippinginfo_constructor_exists():
    assert callable(ShippingInfo.__init__)


def test_shippinginfo_constructor_args():
    sig = inspect.signature(ShippingInfo.__init__)
    params = list(sig.parameters.keys())
    assert "shippingCharges" in params, "Missing parameter 'shippingCharges'"
    assert "deliveryAddress" in params, "Missing parameter 'deliveryAddress'"
    assert "estimatedDeliveryDate" in params, "Missing parameter 'estimatedDeliveryDate'"
    assert "deliveryType" in params, "Missing parameter 'deliveryType'"

def test_shippinginfo_has_shippingCharges():
    assert hasattr(ShippingInfo, "shippingCharges")
    descriptor = None
    for klass in ShippingInfo.__mro__:
        if "shippingCharges" in klass.__dict__:
            descriptor = klass.__dict__["shippingCharges"]
            break
    assert isinstance(descriptor, property)

def test_shippinginfo_has_deliveryAddress():
    assert hasattr(ShippingInfo, "deliveryAddress")
    descriptor = None
    for klass in ShippingInfo.__mro__:
        if "deliveryAddress" in klass.__dict__:
            descriptor = klass.__dict__["deliveryAddress"]
            break
    assert isinstance(descriptor, property)

def test_shippinginfo_has_estimatedDeliveryDate():
    assert hasattr(ShippingInfo, "estimatedDeliveryDate")
    descriptor = None
    for klass in ShippingInfo.__mro__:
        if "estimatedDeliveryDate" in klass.__dict__:
            descriptor = klass.__dict__["estimatedDeliveryDate"]
            break
    assert isinstance(descriptor, property)

def test_shippinginfo_has_deliveryType():
    assert hasattr(ShippingInfo, "deliveryType")
    descriptor = None
    for klass in ShippingInfo.__mro__:
        if "deliveryType" in klass.__dict__:
            descriptor = klass.__dict__["deliveryType"]
            break
    assert isinstance(descriptor, property)



def test_productlisthelper_is_not_abstract():
    assert not inspect.isabstract(ProductListHelper)


def test_productlisthelper_constructor_exists():
    assert callable(ProductListHelper.__init__)


def test_productlisthelper_constructor_args():
    sig = inspect.signature(ProductListHelper.__init__)
    params = list(sig.parameters.keys())



def test_wishlist_is_not_abstract():
    assert not inspect.isabstract(WishList)


def test_wishlist_constructor_exists():
    assert callable(WishList.__init__)


def test_wishlist_constructor_args():
    sig = inspect.signature(WishList.__init__)
    params = list(sig.parameters.keys())



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "items" in params, "Missing parameter 'items'"
    assert "deliveryDate" in params, "Missing parameter 'deliveryDate'"
    assert "status" in params, "Missing parameter 'status'"
    assert "orderedOn" in params, "Missing parameter 'orderedOn'"
    assert "orderTotalAmount" in params, "Missing parameter 'orderTotalAmount'"
    assert "shippingId" in params, "Missing parameter 'shippingId'"
    assert "orderId" in params, "Missing parameter 'orderId'"
    assert "noOfItem" in params, "Missing parameter 'noOfItem'"

def test_order_has_items():
    assert hasattr(Order, "items")
    descriptor = None
    for klass in Order.__mro__:
        if "items" in klass.__dict__:
            descriptor = klass.__dict__["items"]
            break
    assert isinstance(descriptor, property)

def test_order_has_deliveryDate():
    assert hasattr(Order, "deliveryDate")
    descriptor = None
    for klass in Order.__mro__:
        if "deliveryDate" in klass.__dict__:
            descriptor = klass.__dict__["deliveryDate"]
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

def test_order_has_orderedOn():
    assert hasattr(Order, "orderedOn")
    descriptor = None
    for klass in Order.__mro__:
        if "orderedOn" in klass.__dict__:
            descriptor = klass.__dict__["orderedOn"]
            break
    assert isinstance(descriptor, property)

def test_order_has_orderTotalAmount():
    assert hasattr(Order, "orderTotalAmount")
    descriptor = None
    for klass in Order.__mro__:
        if "orderTotalAmount" in klass.__dict__:
            descriptor = klass.__dict__["orderTotalAmount"]
            break
    assert isinstance(descriptor, property)

def test_order_has_shippingId():
    assert hasattr(Order, "shippingId")
    descriptor = None
    for klass in Order.__mro__:
        if "shippingId" in klass.__dict__:
            descriptor = klass.__dict__["shippingId"]
            break
    assert isinstance(descriptor, property)

def test_order_has_orderId():
    assert hasattr(Order, "orderId")
    descriptor = None
    for klass in Order.__mro__:
        if "orderId" in klass.__dict__:
            descriptor = klass.__dict__["orderId"]
            break
    assert isinstance(descriptor, property)

def test_order_has_noOfItem():
    assert hasattr(Order, "noOfItem")
    descriptor = None
    for klass in Order.__mro__:
        if "noOfItem" in klass.__dict__:
            descriptor = klass.__dict__["noOfItem"]
            break
    assert isinstance(descriptor, property)



def test_list_product__is_not_abstract():
    assert not inspect.isabstract(List_Product_)


def test_list_product__constructor_exists():
    assert callable(List_Product_.__init__)


def test_list_product__constructor_args():
    sig = inspect.signature(List_Product_.__init__)
    params = list(sig.parameters.keys())



def test_product_is_not_abstract():
    assert not inspect.isabstract(Product)


def test_product_constructor_exists():
    assert callable(Product.__init__)


def test_product_constructor_args():
    sig = inspect.signature(Product.__init__)
    params = list(sig.parameters.keys())
    assert "productId" in params, "Missing parameter 'productId'"
    assert "productName" in params, "Missing parameter 'productName'"
    assert "description" in params, "Missing parameter 'description'"
    assert "rating" in params, "Missing parameter 'rating'"
    assert "image" in params, "Missing parameter 'image'"
    assert "sellerInfo" in params, "Missing parameter 'sellerInfo'"
    assert "price" in params, "Missing parameter 'price'"

def test_product_has_productId():
    assert hasattr(Product, "productId")
    descriptor = None
    for klass in Product.__mro__:
        if "productId" in klass.__dict__:
            descriptor = klass.__dict__["productId"]
            break
    assert isinstance(descriptor, property)

def test_product_has_productName():
    assert hasattr(Product, "productName")
    descriptor = None
    for klass in Product.__mro__:
        if "productName" in klass.__dict__:
            descriptor = klass.__dict__["productName"]
            break
    assert isinstance(descriptor, property)

def test_product_has_description():
    assert hasattr(Product, "description")
    descriptor = None
    for klass in Product.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_product_has_rating():
    assert hasattr(Product, "rating")
    descriptor = None
    for klass in Product.__mro__:
        if "rating" in klass.__dict__:
            descriptor = klass.__dict__["rating"]
            break
    assert isinstance(descriptor, property)

def test_product_has_image():
    assert hasattr(Product, "image")
    descriptor = None
    for klass in Product.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)

def test_product_has_sellerInfo():
    assert hasattr(Product, "sellerInfo")
    descriptor = None
    for klass in Product.__mro__:
        if "sellerInfo" in klass.__dict__:
            descriptor = klass.__dict__["sellerInfo"]
            break
    assert isinstance(descriptor, property)

def test_product_has_price():
    assert hasattr(Product, "price")
    descriptor = None
    for klass in Product.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "phoneNo" in params, "Missing parameter 'phoneNo'"
    assert "address" in params, "Missing parameter 'address'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "user_name" in params, "Missing parameter 'user_name'"

def test_customer_has_phoneNo():
    assert hasattr(Customer, "phoneNo")
    descriptor = None
    for klass in Customer.__mro__:
        if "phoneNo" in klass.__dict__:
            descriptor = klass.__dict__["phoneNo"]
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

def test_customer_has_lastName():
    assert hasattr(Customer, "lastName")
    descriptor = None
    for klass in Customer.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_firstName():
    assert hasattr(Customer, "firstName")
    descriptor = None
    for klass in Customer.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_user_name():
    assert hasattr(Customer, "user_name")
    descriptor = None
    for klass in Customer.__mro__:
        if "user_name" in klass.__dict__:
            descriptor = klass.__dict__["user_name"]
            break
    assert isinstance(descriptor, property)



def test_guest_is_not_abstract():
    assert not inspect.isabstract(Guest)


def test_guest_constructor_exists():
    assert callable(Guest.__init__)


def test_guest_constructor_args():
    sig = inspect.signature(Guest.__init__)
    params = list(sig.parameters.keys())


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
User_strategy = st.builds(
    User,
    userId=
        st.integers()
)
Cart_strategy = st.builds(
    Cart,
)
Appliances_strategy = st.builds(
    Appliances,
)
Electronics_strategy = st.builds(
    Electronics,
)
Ornaments_strategy = st.builds(
    Ornaments,
    Name=
        safe_text
)
Payment_Interface_strategy = st.builds(
    Payment_Interface,
)
CreditCardPayment_strategy = st.builds(
    CreditCardPayment,
)
DebitCardPayment_strategy = st.builds(
    DebitCardPayment,
)
PaymentFactory_strategy = st.builds(
    PaymentFactory,
)
Seller_strategy = st.builds(
    Seller,
    name=
        safe_text,
    rating=
        safe_text,
    sellerId=
        safe_text
)
ShippingInfo_strategy = st.builds(
    ShippingInfo,
    shippingCharges=
        st.integers(),
    deliveryAddress=
        safe_text,
    estimatedDeliveryDate=
        safe_text,
    deliveryType=
        safe_text
)
ProductListHelper_strategy = st.builds(
    ProductListHelper,
)
WishList_strategy = st.builds(
    WishList,
)
Order_strategy = st.builds(
    Order,
    items=
        st.none(),
    deliveryDate=
        st.integers(),
    status=
        safe_text,
    orderedOn=
        safe_text,
    orderTotalAmount=
        st.integers(),
    shippingId=
        st.integers(),
    orderId=
        st.integers(),
    noOfItem=
        st.integers()
)
List_Product__strategy = st.builds(
    List_Product_,
)
Product_strategy = st.builds(
    Product,
    productId=
        st.integers(),
    productName=
        safe_text,
    description=
        safe_text,
    rating=
        st.integers(),
    image=
        safe_text,
    sellerInfo=
        st.none(),
    price=
        st.integers()
)
Customer_strategy = st.builds(
    Customer,
    phoneNo=
        st.integers(),
    address=
        safe_text,
    lastName=
        safe_text,
    firstName=
        safe_text,
    user_name=
        safe_text
)
Guest_strategy = st.builds(
    Guest,
)

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original

@given(instance=Cart_strategy)
@settings(max_examples=50)
def test_cart_instantiation(instance):
    assert isinstance(instance, Cart)

@given(instance=Appliances_strategy)
@settings(max_examples=50)
def test_appliances_instantiation(instance):
    assert isinstance(instance, Appliances)

@given(instance=Electronics_strategy)
@settings(max_examples=50)
def test_electronics_instantiation(instance):
    assert isinstance(instance, Electronics)

@given(instance=Ornaments_strategy)
@settings(max_examples=50)
def test_ornaments_instantiation(instance):
    assert isinstance(instance, Ornaments)



@given(instance=Ornaments_strategy)
def test_ornaments_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Payment_Interface_strategy)
@settings(max_examples=50)
def test_payment_interface_instantiation(instance):
    assert isinstance(instance, Payment_Interface)

@given(instance=CreditCardPayment_strategy)
@settings(max_examples=50)
def test_creditcardpayment_instantiation(instance):
    assert isinstance(instance, CreditCardPayment)

@given(instance=DebitCardPayment_strategy)
@settings(max_examples=50)
def test_debitcardpayment_instantiation(instance):
    assert isinstance(instance, DebitCardPayment)

@given(instance=PaymentFactory_strategy)
@settings(max_examples=50)
def test_paymentfactory_instantiation(instance):
    assert isinstance(instance, PaymentFactory)

@given(instance=Seller_strategy)
@settings(max_examples=50)
def test_seller_instantiation(instance):
    assert isinstance(instance, Seller)



@given(instance=Seller_strategy)
def test_seller_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Seller_strategy)
def test_seller_rating_setter(instance):
    original = instance.rating
    instance.rating = original
    assert instance.rating == original



@given(instance=Seller_strategy)
def test_seller_sellerId_setter(instance):
    original = instance.sellerId
    instance.sellerId = original
    assert instance.sellerId == original

@given(instance=ShippingInfo_strategy)
@settings(max_examples=50)
def test_shippinginfo_instantiation(instance):
    assert isinstance(instance, ShippingInfo)



@given(instance=ShippingInfo_strategy)
def test_shippinginfo_shippingCharges_setter(instance):
    original = instance.shippingCharges
    instance.shippingCharges = original
    assert instance.shippingCharges == original



@given(instance=ShippingInfo_strategy)
def test_shippinginfo_deliveryAddress_setter(instance):
    original = instance.deliveryAddress
    instance.deliveryAddress = original
    assert instance.deliveryAddress == original



@given(instance=ShippingInfo_strategy)
def test_shippinginfo_estimatedDeliveryDate_setter(instance):
    original = instance.estimatedDeliveryDate
    instance.estimatedDeliveryDate = original
    assert instance.estimatedDeliveryDate == original



@given(instance=ShippingInfo_strategy)
def test_shippinginfo_deliveryType_setter(instance):
    original = instance.deliveryType
    instance.deliveryType = original
    assert instance.deliveryType == original

@given(instance=ProductListHelper_strategy)
@settings(max_examples=50)
def test_productlisthelper_instantiation(instance):
    assert isinstance(instance, ProductListHelper)

@given(instance=WishList_strategy)
@settings(max_examples=50)
def test_wishlist_instantiation(instance):
    assert isinstance(instance, WishList)

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_items_setter(instance):
    original = instance.items
    instance.items = original
    assert instance.items == original



@given(instance=Order_strategy)
def test_order_deliveryDate_setter(instance):
    original = instance.deliveryDate
    instance.deliveryDate = original
    assert instance.deliveryDate == original



@given(instance=Order_strategy)
def test_order_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Order_strategy)
def test_order_orderedOn_setter(instance):
    original = instance.orderedOn
    instance.orderedOn = original
    assert instance.orderedOn == original



@given(instance=Order_strategy)
def test_order_orderTotalAmount_setter(instance):
    original = instance.orderTotalAmount
    instance.orderTotalAmount = original
    assert instance.orderTotalAmount == original



@given(instance=Order_strategy)
def test_order_shippingId_setter(instance):
    original = instance.shippingId
    instance.shippingId = original
    assert instance.shippingId == original



@given(instance=Order_strategy)
def test_order_orderId_setter(instance):
    original = instance.orderId
    instance.orderId = original
    assert instance.orderId == original



@given(instance=Order_strategy)
def test_order_noOfItem_setter(instance):
    original = instance.noOfItem
    instance.noOfItem = original
    assert instance.noOfItem == original

@given(instance=List_Product__strategy)
@settings(max_examples=50)
def test_list_product__instantiation(instance):
    assert isinstance(instance, List_Product_)

@given(instance=Product_strategy)
@settings(max_examples=50)
def test_product_instantiation(instance):
    assert isinstance(instance, Product)



@given(instance=Product_strategy)
def test_product_productId_setter(instance):
    original = instance.productId
    instance.productId = original
    assert instance.productId == original



@given(instance=Product_strategy)
def test_product_productName_setter(instance):
    original = instance.productName
    instance.productName = original
    assert instance.productName == original



@given(instance=Product_strategy)
def test_product_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Product_strategy)
def test_product_rating_setter(instance):
    original = instance.rating
    instance.rating = original
    assert instance.rating == original



@given(instance=Product_strategy)
def test_product_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original



@given(instance=Product_strategy)
def test_product_sellerInfo_setter(instance):
    original = instance.sellerInfo
    instance.sellerInfo = original
    assert instance.sellerInfo == original



@given(instance=Product_strategy)
def test_product_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_phoneNo_setter(instance):
    original = instance.phoneNo
    instance.phoneNo = original
    assert instance.phoneNo == original



@given(instance=Customer_strategy)
def test_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Customer_strategy)
def test_customer_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=Customer_strategy)
def test_customer_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=Customer_strategy)
def test_customer_user_name_setter(instance):
    original = instance.user_name
    instance.user_name = original
    assert instance.user_name == original

@given(instance=Guest_strategy)
@settings(max_examples=50)
def test_guest_instantiation(instance):
    assert isinstance(instance, Guest)
