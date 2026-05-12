####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
GUI_Screen = Class(name="GUI_Screen")
Customer_Customer = Class(name="Customer_Customer")
Customer_Payment = Class(name="Customer_Payment")
Shopping_Cart_ShoppingCart = Class(name="Shopping_Cart_ShoppingCart")
Shopping_Cart_Checkout = Class(name="Shopping_Cart_Checkout")
Customer_Customer1 = Class(name="Customer_Customer1")
Customer_User = Class(name="Customer_User")
Customer_Account = Class(name="Customer_Account")
Customer_Payment1 = Class(name="Customer_Payment1")
Cart_ShoppingCart = Class(name="Cart_ShoppingCart")
Cart_Checkout = Class(name="Cart_Checkout")
Product_Item = Class(name="Product_Item")
Product_Item_Type = Class(name="Product_Item_Type")
Product_Item_Specification = Class(name="Product_Item_Specification")

# GUI_Screen class attributes and methods
GUI_Screen_id: Property = Property(name="id", type=IntegerType)
GUI_Screen_Message: Property = Property(name="Message", type=StringType)
GUI_Screen_Exit__: Property = Property(name="Exit__", type=StringType)
GUI_Screen_Error__: Property = Property(name="Error__", type=StringType)
GUI_Screen_DisplayList__: Property = Property(name="DisplayList__", type=IntegerType)
GUI_Screen.attributes={GUI_Screen_Exit__, GUI_Screen_id, GUI_Screen_DisplayList__, GUI_Screen_Message, GUI_Screen_Error__}

# Customer_Customer class attributes and methods
Customer_Customer_firstname: Property = Property(name="firstname", type=StringType)
Customer_Customer_lastname: Property = Property(name="lastname", type=StringType)
Customer_Customer_emailAddress: Property = Property(name="emailAddress", type=StringType)
Customer_Customer_id: Property = Property(name="id", type=IntegerType)
Customer_Customer_login: Property = Property(name="login", type=StringType)
Customer_Customer_password: Property = Property(name="password", type=StringType)
Customer_Customer_Message: Property = Property(name="Message", type=StringType)
Customer_Customer.attributes={Customer_Customer_lastname, Customer_Customer_password, Customer_Customer_Message, Customer_Customer_login, Customer_Customer_firstname, Customer_Customer_id, Customer_Customer_emailAddress}

# Customer_Payment class attributes and methods
Customer_Payment_Paymentid: Property = Property(name="Paymentid", type=IntegerType)
Customer_Payment_login: Property = Property(name="login", type=StringType)
Customer_Payment_ApplPay: Property = Property(name="ApplPay", type=IntegerType)
Customer_Payment_CustomerId: Property = Property(name="CustomerId", type=StringType)
Customer_Payment_PayPal: Property = Property(name="PayPal", type=IntegerType)
Customer_Payment_Payment__: Property = Property(name="Payment__", type=FloatType)
Customer_Payment.attributes={Customer_Payment_login, Customer_Payment_Paymentid, Customer_Payment_PayPal, Customer_Payment_ApplPay, Customer_Payment_CustomerId, Customer_Payment_Payment__}

# Shopping_Cart_ShoppingCart class attributes and methods
Shopping_Cart_ShoppingCart_id: Property = Property(name="id", type=IntegerType)
Shopping_Cart_ShoppingCart_creationDate: Property = Property(name="creationDate", type=DateType)
Shopping_Cart_ShoppingCart_CheckoutID: Property = Property(name="CheckoutID", type=IntegerType)
Shopping_Cart_ShoppingCart_AddOrder: Property = Property(name="AddOrder", type=IntegerType)
Shopping_Cart_ShoppingCart_RemoveOrder: Property = Property(name="RemoveOrder", type=IntegerType)
Shopping_Cart_ShoppingCart_UpdateOrder: Property = Property(name="UpdateOrder", type=IntegerType)
Shopping_Cart_ShoppingCart_GetTotal__: Property = Property(name="GetTotal__", type=FloatType)
Shopping_Cart_ShoppingCart.attributes={Shopping_Cart_ShoppingCart_UpdateOrder, Shopping_Cart_ShoppingCart_id, Shopping_Cart_ShoppingCart_GetTotal__, Shopping_Cart_ShoppingCart_AddOrder, Shopping_Cart_ShoppingCart_CheckoutID, Shopping_Cart_ShoppingCart_RemoveOrder, Shopping_Cart_ShoppingCart_creationDate}

# Shopping_Cart_Checkout class attributes and methods
Shopping_Cart_Checkout_Paymentid: Property = Property(name="Paymentid", type=IntegerType)
Shopping_Cart_Checkout_CheckoutID: Property = Property(name="CheckoutID", type=IntegerType)
Shopping_Cart_Checkout_billingMethod: Property = Property(name="billingMethod", type=StringType)
Shopping_Cart_Checkout_CustomerID: Property = Property(name="CustomerID", type=StringType)
Shopping_Cart_Checkout_Checkout__: Property = Property(name="Checkout__", type=FloatType)
Shopping_Cart_Checkout.attributes={Shopping_Cart_Checkout_Paymentid, Shopping_Cart_Checkout_Checkout__, Shopping_Cart_Checkout_CheckoutID, Shopping_Cart_Checkout_billingMethod, Shopping_Cart_Checkout_CustomerID}

# Customer_Customer1 class attributes and methods
Customer_Customer1_userId: Property = Property(name="userId", type=StringType)
Customer_Customer1_PaymentMet__: Property = Property(name="PaymentMet__", type=FloatType)
Customer_Customer1_Account__: Property = Property(name="Account__", type=StringType)
Customer_Customer1_select__: Property = Property(name="select__", type=StringType)
Customer_Customer1.attributes={Customer_Customer1_userId, Customer_Customer1_PaymentMet__, Customer_Customer1_select__, Customer_Customer1_Account__}

# Customer_User class attributes and methods
Customer_User_Addresschange__: Property = Property(name="Addresschange__", type=StringType)
Customer_User_userid__: Property = Property(name="userid__", type=StringType)
Customer_User.attributes={Customer_User_Addresschange__, Customer_User_userid__}

# Customer_Account class attributes and methods
Customer_Account_Login__: Property = Property(name="Login__", type=StringType)
Customer_Account_account__: Property = Property(name="account__", type=StringType)
Customer_Account.attributes={Customer_Account_account__, Customer_Account_Login__}

# Customer_Payment1 class attributes and methods
Customer_Payment1_PayBill__: Property = Property(name="PayBill__", type=StringType)
Customer_Payment1_Auth__: Property = Property(name="Auth__", type=BooleanType)
Customer_Payment1_ID: Property = Property(name="ID", type=Customer_Account)
Customer_Payment1.attributes={Customer_Payment1_PayBill__, Customer_Payment1_ID, Customer_Payment1_Auth__}

# Cart_ShoppingCart class attributes and methods
Cart_ShoppingCart_id: Property = Property(name="id", type=IntegerType)
Cart_ShoppingCart_creationDate: Property = Property(name="creationDate", type=DateType)
Cart_ShoppingCart_CheckoutID: Property = Property(name="CheckoutID", type=IntegerType)
Cart_ShoppingCart_AddCart: Property = Property(name="AddCart", type=IntegerType)
Cart_ShoppingCart_RemoveOrder: Property = Property(name="RemoveOrder", type=IntegerType)
Cart_ShoppingCart_UpdateOrder: Property = Property(name="UpdateOrder", type=IntegerType)
Cart_ShoppingCart_GetTotal__: Property = Property(name="GetTotal__", type=FloatType)
Cart_ShoppingCart.attributes={Cart_ShoppingCart_RemoveOrder, Cart_ShoppingCart_id, Cart_ShoppingCart_CheckoutID, Cart_ShoppingCart_creationDate, Cart_ShoppingCart_AddCart, Cart_ShoppingCart_GetTotal__, Cart_ShoppingCart_UpdateOrder}

# Cart_Checkout class attributes and methods
Cart_Checkout_Paymentid: Property = Property(name="Paymentid", type=IntegerType)
Cart_Checkout_CheckoutID: Property = Property(name="CheckoutID", type=IntegerType)
Cart_Checkout_billingMethod: Property = Property(name="billingMethod", type=StringType)
Cart_Checkout_CustomerID: Property = Property(name="CustomerID", type=StringType)
Cart_Checkout_PayBill__: Property = Property(name="PayBill__", type=Customer_Account)
Cart_Checkout.attributes={Cart_Checkout_CheckoutID, Cart_Checkout_billingMethod, Cart_Checkout_CustomerID, Cart_Checkout_PayBill__, Cart_Checkout_Paymentid}

# Product_Item class attributes and methods
Product_Item_quantity: Property = Property(name="quantity", type=IntegerType)
Product_Item_list__: Property = Property(name="list__", type=FloatType)
Product_Item_id: Property = Property(name="id", type=IntegerType)
Product_Item_OutofStock__: Property = Property(name="OutofStock__", type=StringType)
Product_Item_totalcost__: Property = Property(name="totalcost__", type=StringType)
Product_Item.attributes={Product_Item_list__, Product_Item_id, Product_Item_OutofStock__, Product_Item_totalcost__, Product_Item_quantity}

# Product_Item_Type class attributes and methods
Product_Item_Type_quantity: Property = Property(name="quantity", type=IntegerType)
Product_Item_Type_price: Property = Property(name="price", type=FloatType)
Product_Item_Type_id: Property = Property(name="id", type=IntegerType)
Product_Item_Type_ItemType__: Property = Property(name="ItemType__", type=StringType)
Product_Item_Type_Avail__: Property = Property(name="Avail__", type=StringType)
Product_Item_Type.attributes={Product_Item_Type_ItemType__, Product_Item_Type_price, Product_Item_Type_quantity, Product_Item_Type_Avail__, Product_Item_Type_id}

# Product_Item_Specification class attributes and methods
Product_Item_Specification_quantity: Property = Property(name="quantity", type=IntegerType)
Product_Item_Specification_price: Property = Property(name="price", type=FloatType)
Product_Item_Specification_id: Property = Property(name="id", type=IntegerType)
Product_Item_Specification_ItemSpecs__: Property = Property(name="ItemSpecs__", type=StringType)
Product_Item_Specification_Brand__: Property = Property(name="Brand__", type=StringType)
Product_Item_Specification.attributes={Product_Item_Specification_ItemSpecs__, Product_Item_Specification_Brand__, Product_Item_Specification_price, Product_Item_Specification_quantity, Product_Item_Specification_id}

# Relationships
Payment_Customer: BinaryAssociation = BinaryAssociation(
    name="Payment_Customer",
    ends={
        Property(name="Payment_Customer_00", type=Customer_Customer, multiplicity=Multiplicity(0, 1)),
        Property(name="Payment_Customer_11", type=Customer_Payment, multiplicity=Multiplicity(0, 1))
    }
)
Customer_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="Customer_ShoppingCart",
    ends={
        Property(name="Customer_ShoppingCart_02", type=Shopping_Cart_ShoppingCart, multiplicity=Multiplicity(1, 1)),
        Property(name="Customer_ShoppingCart_13", type=Customer_Customer, multiplicity=Multiplicity(0, 1))
    }
)
Payment_Checkout: BinaryAssociation = BinaryAssociation(
    name="Payment_Checkout",
    ends={
        Property(name="Payment_Checkout_04", type=Shopping_Cart_Checkout, multiplicity=Multiplicity(1, 1)),
        Property(name="Payment_Checkout_15", type=Customer_Payment, multiplicity=Multiplicity(1, 9999))
    }
)
ShoppingCart_Checkout: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_Checkout",
    ends={
        Property(name="ShoppingCart_Checkout_06", type=Shopping_Cart_Checkout, multiplicity=Multiplicity(1, 9999)),
        Property(name="ShoppingCart_Checkout_17", type=Shopping_Cart_ShoppingCart, multiplicity=Multiplicity(1, 1))
    }
)
Payment_Customer1: BinaryAssociation = BinaryAssociation(
    name="Payment_Customer1",
    ends={
        Property(name="Payment_Customer_08", type=Customer_Customer1, multiplicity=Multiplicity(1, 9999)),
        Property(name="Payment_Customer_19", type=Customer_Payment1, multiplicity=Multiplicity(0, 1))
    }
)
ShoppingCart_Checkout1: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_Checkout1",
    ends={
        Property(name="ShoppingCart_Checkout_010", type=Cart_Checkout, multiplicity=Multiplicity(1, 9999)),
        Property(name="ShoppingCart_Checkout_111", type=Cart_ShoppingCart, multiplicity=Multiplicity(1, 1))
    }
)
ShoppingCart_Customer: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_Customer",
    ends={
        Property(name="ShoppingCart_Customer_012", type=Customer_Customer1, multiplicity=Multiplicity(0, 1)),
        Property(name="ShoppingCart_Customer_113", type=Cart_ShoppingCart, multiplicity=Multiplicity(1, 1))
    }
)
Checkout_Payment: BinaryAssociation = BinaryAssociation(
    name="Checkout_Payment",
    ends={
        Property(name="Checkout_Payment_014", type=Customer_Payment1, multiplicity=Multiplicity(1, 9999)),
        Property(name="Checkout_Payment_115", type=Cart_Checkout, multiplicity=Multiplicity(1, 1))
    }
)
Item_Specification_Item: BinaryAssociation = BinaryAssociation(
    name="Item_Specification_Item",
    ends={
        Property(name="Item_Specification_Item_016", type=Product_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="Item_Specification_Item_117", type=Product_Item_Specification, multiplicity=Multiplicity(1, 9999))
    }
)
Item_Type_Item: BinaryAssociation = BinaryAssociation(
    name="Item_Type_Item",
    ends={
        Property(name="Item_Type_Item_018", type=Product_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="Item_Type_Item_119", type=Product_Item_Type, multiplicity=Multiplicity(1, 9999))
    }
)
Item_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="Item_ShoppingCart",
    ends={
        Property(name="Item_ShoppingCart_020", type=Cart_ShoppingCart, multiplicity=Multiplicity(0, 1)),
        Property(name="Item_ShoppingCart_121", type=Product_Item, multiplicity=Multiplicity(1, 9999))
    }
)
GUI_Screen_Account: BinaryAssociation = BinaryAssociation(
    name="GUI_Screen_Account",
    ends={
        Property(name="GUI_Screen_Account_022", type=Customer_Account, multiplicity=Multiplicity(0, 1)),
        Property(name="GUI_Screen_Account_123", type=GUI_Screen, multiplicity=Multiplicity(0, 1))
    }
)
GUI_Screen_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="GUI_Screen_ShoppingCart",
    ends={
        Property(name="GUI_Screen_ShoppingCart_024", type=Cart_ShoppingCart, multiplicity=Multiplicity(0, 1)),
        Property(name="GUI_Screen_ShoppingCart_125", type=GUI_Screen, multiplicity=Multiplicity(0, 1))
    }
)
GUI_Screen_Item: BinaryAssociation = BinaryAssociation(
    name="GUI_Screen_Item",
    ends={
        Property(name="GUI_Screen_Item_026", type=Product_Item, multiplicity=Multiplicity(0, 1)),
        Property(name="GUI_Screen_Item_127", type=GUI_Screen, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="d0ed3e28_ae24_4dc3_bcf7_bd98e2a96ce6",
    types={GUI_Screen, Customer_Customer, Customer_Payment, Shopping_Cart_ShoppingCart, Shopping_Cart_Checkout, Customer_Customer1, Customer_User, Customer_Account, Customer_Payment1, Cart_ShoppingCart, Cart_Checkout, Product_Item, Product_Item_Type, Product_Item_Specification},
    associations={Payment_Customer, Customer_ShoppingCart, Payment_Checkout, ShoppingCart_Checkout, Payment_Customer1, ShoppingCart_Checkout1, ShoppingCart_Customer, Checkout_Payment, Item_Specification_Item, Item_Type_Item, Item_ShoppingCart, GUI_Screen_Account, GUI_Screen_ShoppingCart, GUI_Screen_Item},
    generalizations={},
    metadata=None
)

###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)