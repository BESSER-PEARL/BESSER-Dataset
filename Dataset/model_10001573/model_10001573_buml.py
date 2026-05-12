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

# Enumerations
CustomerType: Enumeration = Enumeration(
    name="CustomerType",
    literals={
            
    }
)

Enumeration_: Enumeration = Enumeration(
    name="Enumeration",
    literals={
            
    }
)

# Classes
PremiumCustomer = Class(name="PremiumCustomer")
Payment = Class(name="Payment")
SalesPerson = Class(name="SalesPerson")
Order = Class(name="Order")
LZUser2 = Class(name="LZUser2")
ShoppingCart = Class(name="ShoppingCart")
Item = Class(name="Item")
RegularCustomer = Class(name="RegularCustomer")
CustomerHandler = Class(name="CustomerHandler")
PurchaseAmountSlab = Class(name="PurchaseAmountSlab")
RegularDiscountSlab = Class(name="RegularDiscountSlab")
PremiumDiscountSlab = Class(name="PremiumDiscountSlab")
Customer = Class(name="Customer")

# PremiumCustomer class attributes and methods
PremiumCustomer_RadixClient: Property = Property(name="RadixClient", type=StringType)
PremiumCustomer_log: Property = Property(name="log", type=StringType)
PremiumCustomer_email: Property = Property(name="email", type=StringType)
PremiumCustomer.attributes={PremiumCustomer_email, PremiumCustomer_RadixClient, PremiumCustomer_log}

# Payment class attributes and methods
Payment_paidDate: Property = Property(name="paidDate", type=DateType)
Payment_total: Property = Property(name="total", type=FloatType)
Payment_details: Property = Property(name="details", type=StringType)
Payment.attributes={Payment_paidDate, Payment_details, Payment_total}

# SalesPerson class attributes and methods
SalesPerson_populate: Property = Property(name="populate", type=StringType)
SalesPerson_password: Property = Property(name="password", type=StringType)
SalesPerson_state: Property = Property(name="state", type=CustomerType)
SalesPerson.attributes={SalesPerson_password, SalesPerson_state, SalesPerson_populate}

# Order class attributes and methods
Order_number: Property = Property(name="number", type=IntegerType)
Order_ordered: Property = Property(name="ordered", type=DateType)
Order_shipped: Property = Property(name="shipped", type=BooleanType)
Order_shipTo: Property = Property(name="shipTo", type=StringType)
Order_total: Property = Property(name="total", type=FloatType)
Order_status: Property = Property(name="status", type=StringType)
Order.attributes={Order_number, Order_total, Order_shipTo, Order_shipped, Order_ordered, Order_status}

# LZUser2 class attributes and methods
LZUser2_populate: Property = Property(name="populate", type=StringType)
LZUser2_password: Property = Property(name="password", type=StringType)
LZUser2_state: Property = Property(name="state", type=CustomerType)
LZUser2.attributes={LZUser2_state, LZUser2_password, LZUser2_populate}

# ShoppingCart class attributes and methods
ShoppingCart__attr: Property = Property(name="_attr", type=DateType)
ShoppingCart_Items_list_: Property = Property(name="Items_list_", type=Item)
ShoppingCart.attributes={ShoppingCart__attr, ShoppingCart_Items_list_}

# Item class attributes and methods
Item_quantity: Property = Property(name="quantity", type=IntegerType)
Item_price: Property = Property(name="price", type=FloatType)
Item_name: Property = Property(name="name", type=StringType)
Item.attributes={Item_quantity, Item_price, Item_name}

# RegularCustomer class attributes and methods
RegularCustomer_RadixClient: Property = Property(name="RadixClient", type=StringType)
RegularCustomer_log: Property = Property(name="log", type=StringType)
RegularCustomer_email: Property = Property(name="email", type=StringType)
RegularCustomer.attributes={RegularCustomer_log, RegularCustomer_email, RegularCustomer_RadixClient}

# CustomerHandler class attributes and methods
CustomerHandler_populate: Property = Property(name="populate", type=StringType)
CustomerHandler_password: Property = Property(name="password", type=StringType)
CustomerHandler_state: Property = Property(name="state", type=CustomerType)
CustomerHandler.attributes={CustomerHandler_populate, CustomerHandler_state, CustomerHandler_password}

# PurchaseAmountSlab class attributes and methods
PurchaseAmountSlab_from: Property = Property(name="from", type=FloatType)
PurchaseAmountSlab_discount: Property = Property(name="discount", type=FloatType)
PurchaseAmountSlab_to: Property = Property(name="to", type=FloatType)
PurchaseAmountSlab.attributes={PurchaseAmountSlab_from, PurchaseAmountSlab_discount, PurchaseAmountSlab_to}

# RegularDiscountSlab class attributes and methods
RegularDiscountSlab_RadixClient: Property = Property(name="RadixClient", type=StringType)
RegularDiscountSlab_log: Property = Property(name="log", type=StringType)
RegularDiscountSlab_email: Property = Property(name="email", type=StringType)
RegularDiscountSlab_attribute: Property = Property(name="attribute", type=StringType)
RegularDiscountSlab_RegularSlab_list__: Property = Property(name="RegularSlab_list__", type=PurchaseAmountSlab)
RegularDiscountSlab__attr: Property = Property(name="_attr", type=StringType)
RegularDiscountSlab_attribute2: Property = Property(name="attribute2", type=StringType)
RegularDiscountSlab_RegularSlab_list_: Property = Property(name="RegularSlab_list_", type=PurchaseAmountSlab)
RegularDiscountSlab.attributes={RegularDiscountSlab_log, RegularDiscountSlab_attribute2, RegularDiscountSlab_RegularSlab_list_, RegularDiscountSlab_RegularSlab_list__, RegularDiscountSlab_email, RegularDiscountSlab__attr, RegularDiscountSlab_RadixClient, RegularDiscountSlab_attribute}

# PremiumDiscountSlab class attributes and methods
PremiumDiscountSlab_RadixClient: Property = Property(name="RadixClient", type=StringType)
PremiumDiscountSlab_log: Property = Property(name="log", type=StringType)
PremiumDiscountSlab_email: Property = Property(name="email", type=StringType)
PremiumDiscountSlab_PremiumSlab_list_: Property = Property(name="PremiumSlab_list_", type=PurchaseAmountSlab)
PremiumDiscountSlab.attributes={PremiumDiscountSlab_PremiumSlab_list_, PremiumDiscountSlab_RadixClient, PremiumDiscountSlab_email, PremiumDiscountSlab_log}

# Customer class attributes and methods
Customer_DiscountSlab_list_: Property = Property(name="DiscountSlab_list_", type=PurchaseAmountSlab)
Customer_type: Property = Property(name="type", type=CustomerType)
Customer_shoppingCart: Property = Property(name="shoppingCart", type=ShoppingCart)
Customer.attributes={Customer_type, Customer_DiscountSlab_list_, Customer_shoppingCart}

# Relationships
Account_Payment: BinaryAssociation = BinaryAssociation(
    name="Account_Payment",
    ends={
        Property(name="p0", type=Payment, multiplicity=Multiplicity(0, 9999)),
        Property(name="acc1", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Account: BinaryAssociation = BinaryAssociation(
    name="Customer_Account",
    ends={
        Property(name="account2", type=Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="customer3", type=PremiumCustomer, multiplicity=Multiplicity(1, 1))
    }
)
Account_Order: BinaryAssociation = BinaryAssociation(
    name="Account_Order",
    ends={
        Property(name="order4", type=Order, multiplicity=Multiplicity(0, 9999)),
        Property(name="account5", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Payment_Order: BinaryAssociation = BinaryAssociation(
    name="Payment_Order",
    ends={
        Property(name="order6", type=Order, multiplicity=Multiplicity(1, 1)),
        Property(name="payment7", type=Payment, multiplicity=Multiplicity(0, 1))
    }
)
Item_Item: BinaryAssociation = BinaryAssociation(
    name="Item_Item",
    ends={
        Property(name="item8", type=Item, multiplicity=Multiplicity(0, 1)),
        Property(name="item9", type=Item, multiplicity=Multiplicity(0, 1))
    }
)
ShoppingCart_Item: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_Item",
    ends={
        Property(name="shoppingCart10", type=ShoppingCart, multiplicity=Multiplicity(1, 9999)),
        Property(name="item11", type=Item, multiplicity=Multiplicity(0, 1))
    }
)
PremiumDiscountSlab_PurchaseAmountSlab: BinaryAssociation = BinaryAssociation(
    name="PremiumDiscountSlab_PurchaseAmountSlab",
    ends={
        Property(name="premiumDiscountSlab12", type=PremiumDiscountSlab, multiplicity=Multiplicity(1, 9999)),
        Property(name="purchaseAmountSlab13", type=PurchaseAmountSlab, multiplicity=Multiplicity(0, 1))
    }
)
RegularDiscountSlab_PurchaseAmountSlab: BinaryAssociation = BinaryAssociation(
    name="RegularDiscountSlab_PurchaseAmountSlab",
    ends={
        Property(name="regularDiscountSlab14", type=RegularDiscountSlab, multiplicity=Multiplicity(1, 9999)),
        Property(name="purchaseAmountSlab15", type=PurchaseAmountSlab, multiplicity=Multiplicity(0, 1))
    }
)
CustomerHandler_Customer: BinaryAssociation = BinaryAssociation(
    name="CustomerHandler_Customer",
    ends={
        Property(name="customerHandler16", type=CustomerHandler, multiplicity=Multiplicity(0, 1)),
        Property(name="customer17", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
Customer_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="Customer_ShoppingCart",
    ends={
        Property(name="customer18", type=Customer, multiplicity=Multiplicity(0, 1)),
        Property(name="shoppingCart219", type=ShoppingCart, multiplicity=Multiplicity(0, 1))
    }
)
Customer_ShoppingCart2: BinaryAssociation = BinaryAssociation(
    name="Customer_ShoppingCart2",
    ends={
        Property(name="customer20", type=Customer, multiplicity=Multiplicity(0, 1)),
        Property(name="shoppingCart221", type=ShoppingCart, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Customer: BinaryAssociation = BinaryAssociation(
    name="Customer_Customer",
    ends={
        Property(name="customer22", type=Customer, multiplicity=Multiplicity(0, 1)),
        Property(name="customer23", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
Customer_PurchaseAmountSlab: BinaryAssociation = BinaryAssociation(
    name="Customer_PurchaseAmountSlab",
    ends={
        Property(name="customer24", type=Customer, multiplicity=Multiplicity(0, 1)),
        Property(name="purchaseAmountSlab25", type=PurchaseAmountSlab, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_GfFUoIxQEeq3N_Xh6gsEIQ",
    types={PremiumCustomer, Payment, SalesPerson, Order, LZUser2, ShoppingCart, Item, RegularCustomer, CustomerHandler, PurchaseAmountSlab, RegularDiscountSlab, PremiumDiscountSlab, Customer, CustomerType, Enumeration_},
    associations={Account_Payment, Customer_Account, Account_Order, Payment_Order, Item_Item, ShoppingCart_Item, PremiumDiscountSlab_PurchaseAmountSlab, RegularDiscountSlab_PurchaseAmountSlab, CustomerHandler_Customer, Customer_ShoppingCart, Customer_ShoppingCart2, Customer_Customer, Customer_PurchaseAmountSlab},
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