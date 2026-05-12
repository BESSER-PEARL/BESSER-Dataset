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
Store = Class(name="Store")
Menu = Class(name="Menu")
Product = Class(name="Product")
Sales_Line_Item = Class(name="Sales_Line_Item")
Sale = Class(name="Sale")
Register = Class(name="Register")
CardReader = Class(name="CardReader")
Card = Class(name="Card")
SUID = Class(name="SUID")
Payment = Class(name="Payment")
customerDatabase = Class(name="customerDatabase")
Food = Class(name="Food")
Order = Class(name="Order")
Drink = Class(name="Drink")
Manager = Class(name="Manager")

# Store class attributes and methods
Store_Address: Property = Property(name="Address", type=StringType)
Store_Name: Property = Property(name="Name", type=StringType)
Store.attributes={Store_Address, Store_Name}

# Menu class attributes and methods
Menu__attr: Property = Property(name="_attr", type=StringType)
Menu.attributes={Menu__attr}

# Product class attributes and methods
Product_name: Property = Property(name="name", type=StringType)
Product_description: Property = Property(name="description", type=StringType)
Product_itemID: Property = Property(name="itemID", type=IntegerType)
Product_price: Property = Property(name="price", type=StringType)
Product.attributes={Product_price, Product_itemID, Product_name, Product_description}

# Sales_Line_Item class attributes and methods
Sales_Line_Item_Quantity: Property = Property(name="Quantity", type=IntegerType)
Sales_Line_Item.attributes={Sales_Line_Item_Quantity}

# Sale class attributes and methods
Sale_Date: Property = Property(name="Date", type=StringType)
Sale_Time: Property = Property(name="Time", type=StringType)
Sale_isComplete: Property = Property(name="isComplete", type=BooleanType)
Sale.attributes={Sale_Date, Sale_Time, Sale_isComplete}

# Register class attributes and methods
Register_attribute: Property = Property(name="attribute", type=StringType)
Register.attributes={Register_attribute}

# CardReader class attributes and methods
CardReader_attribute: Property = Property(name="attribute", type=StringType)
CardReader.attributes={CardReader_attribute}

# Card class attributes and methods
Card_isCredit: Property = Property(name="isCredit", type=BooleanType)
Card_isDebit: Property = Property(name="isDebit", type=BooleanType)
Card_cardNumber: Property = Property(name="cardNumber", type=IntegerType)
Card_cardholderName: Property = Property(name="cardholderName", type=StringType)
Card_cardSN: Property = Property(name="cardSN", type=IntegerType)
Card.attributes={Card_isDebit, Card_cardNumber, Card_cardSN, Card_cardholderName, Card_isCredit}

# SUID class attributes and methods
SUID_ID: Property = Property(name="ID", type=IntegerType)
SUID_studentName: Property = Property(name="studentName", type=StringType)
SUID_suFOODBal: Property = Property(name="suFOODBal", type=StringType)
SUID.attributes={SUID_suFOODBal, SUID_ID, SUID_studentName}

# Payment class attributes and methods
Payment_amount: Property = Property(name="amount", type=StringType)
Payment.attributes={Payment_amount}

# customerDatabase class attributes and methods
customerDatabase_customerName: Property = Property(name="customerName", type=StringType)
customerDatabase_paymentHistory: Property = Property(name="paymentHistory", type=StringType)
customerDatabase_SUID: Property = Property(name="SUID", type=IntegerType)
customerDatabase_creditCardNum: Property = Property(name="creditCardNum", type=IntegerType)
customerDatabase.attributes={customerDatabase_creditCardNum, customerDatabase_paymentHistory, customerDatabase_SUID, customerDatabase_customerName}

# Food class attributes and methods
Food_name: Property = Property(name="name", type=StringType)
Food_price: Property = Property(name="price", type=StringType)
Food_quantity: Property = Property(name="quantity", type=IntegerType)
Food_attribute: Property = Property(name="attribute", type=StringType)
Food.attributes={Food_price, Food_quantity, Food_name, Food_attribute}

# Order class attributes and methods
Order_customer: Property = Property(name="customer", type=StringType)
Order_foodName: Property = Property(name="foodName", type=StringType)
Order_foodPrice: Property = Property(name="foodPrice", type=IntegerType)
Order_drinkName: Property = Property(name="drinkName", type=StringType)
Order_drinkPrice: Property = Property(name="drinkPrice", type=IntegerType)
Order.attributes={Order_customer, Order_foodName, Order_foodPrice, Order_drinkPrice, Order_drinkName}

# Drink class attributes and methods
Drink_name: Property = Property(name="name", type=StringType)
Drink_price: Property = Property(name="price", type=StringType)
Drink_quantity: Property = Property(name="quantity", type=IntegerType)
Drink.attributes={Drink_name, Drink_price, Drink_quantity}

# Manager class attributes and methods
Manager_name: Property = Property(name="name", type=StringType)
Manager_password: Property = Property(name="password", type=StringType)
Manager.attributes={Manager_password, Manager_name}

# Relationships
Register_Store: BinaryAssociation = BinaryAssociation(
    name="Register_Store",
    ends={
        Property(name="store0", type=Store, multiplicity=Multiplicity(1, 1)),
        Property(name="register1", type=Register, multiplicity=Multiplicity(1, 1))
    }
)
Store_Menu: BinaryAssociation = BinaryAssociation(
    name="Store_Menu",
    ends={
        Property(name="menu2", type=Menu, multiplicity=Multiplicity(1, 1)),
        Property(name="store3", type=Store, multiplicity=Multiplicity(1, 1))
    }
)
Menu_Product: BinaryAssociation = BinaryAssociation(
    name="Menu_Product",
    ends={
        Property(name="product4", type=Product, multiplicity=Multiplicity(1, 9999)),
        Property(name="menu5", type=Menu, multiplicity=Multiplicity(1, 1))
    }
)
Register_Sale: BinaryAssociation = BinaryAssociation(
    name="Register_Sale",
    ends={
        Property(name="sale6", type=Sale, multiplicity=Multiplicity(1, 1)),
        Property(name="register7", type=Register, multiplicity=Multiplicity(1, 1))
    }
)
Sale_Payment: BinaryAssociation = BinaryAssociation(
    name="Sale_Payment",
    ends={
        Property(name="payment8", type=Payment, multiplicity=Multiplicity(1, 1)),
        Property(name="sale9", type=Sale, multiplicity=Multiplicity(1, 1))
    }
)
Sale_Sales_Line_Item: BinaryAssociation = BinaryAssociation(
    name="Sale_Sales_Line_Item",
    ends={
        Property(name="sales_Line_Item10", type=Sales_Line_Item, multiplicity=Multiplicity(1, 9999)),
        Property(name="sale11", type=Sale, multiplicity=Multiplicity(1, 1))
    }
)
Payment_Order: BinaryAssociation = BinaryAssociation(
    name="Payment_Order",
    ends={
        Property(name="order12", type=Order, multiplicity=Multiplicity(1, 1)),
        Property(name="payment13", type=Payment, multiplicity=Multiplicity(1, 1))
    }
)
Sales_Line_Item_Food: BinaryAssociation = BinaryAssociation(
    name="Sales_Line_Item_Food",
    ends={
        Property(name="food14", type=Food, multiplicity=Multiplicity(0, 9999)),
        Property(name="sales_Line_Item15", type=Sales_Line_Item, multiplicity=Multiplicity(1, 1))
    }
)
Sales_Line_Item_Drink: BinaryAssociation = BinaryAssociation(
    name="Sales_Line_Item_Drink",
    ends={
        Property(name="drink16", type=Drink, multiplicity=Multiplicity(0, 9999)),
        Property(name="sales_Line_Item17", type=Sales_Line_Item, multiplicity=Multiplicity(1, 1))
    }
)
Sale_CardReader: BinaryAssociation = BinaryAssociation(
    name="Sale_CardReader",
    ends={
        Property(name="cardReader18", type=CardReader, multiplicity=Multiplicity(1, 1)),
        Property(name="sale19", type=Sale, multiplicity=Multiplicity(1, 1))
    }
)
customerDatabase_Card: BinaryAssociation = BinaryAssociation(
    name="customerDatabase_Card",
    ends={
        Property(name="card20", type=Card, multiplicity=Multiplicity(1, 9999)),
        Property(name="customerDatabase21", type=customerDatabase, multiplicity=Multiplicity(0, 1))
    }
)
SUID_Card: BinaryAssociation = BinaryAssociation(
    name="SUID_Card",
    ends={
        Property(name="card22", type=Card, multiplicity=Multiplicity(0, 1)),
        Property(name="sUID23", type=SUID, multiplicity=Multiplicity(0, 9999))
    }
)
SUID_Payment: BinaryAssociation = BinaryAssociation(
    name="SUID_Payment",
    ends={
        Property(name="payment24", type=Payment, multiplicity=Multiplicity(0, 1)),
        Property(name="sUID25", type=SUID, multiplicity=Multiplicity(0, 9999))
    }
)
Product_Sales_Line_Item: BinaryAssociation = BinaryAssociation(
    name="Product_Sales_Line_Item",
    ends={
        Property(name="sales_Line_Item26", type=Sales_Line_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="product27", type=Product, multiplicity=Multiplicity(1, 1))
    }
)
Manager_Menu: BinaryAssociation = BinaryAssociation(
    name="Manager_Menu",
    ends={
        Property(name="menu28", type=Menu, multiplicity=Multiplicity(0, 1)),
        Property(name="manager29", type=Manager, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_QG1SwNCOEeirsuDAiyq68g",
    types={Store, Menu, Product, Sales_Line_Item, Sale, Register, CardReader, Card, SUID, Payment, customerDatabase, Food, Order, Drink, Manager},
    associations={Register_Store, Store_Menu, Menu_Product, Register_Sale, Sale_Payment, Sale_Sales_Line_Item, Payment_Order, Sales_Line_Item_Food, Sales_Line_Item_Drink, Sale_CardReader, customerDatabase_Card, SUID_Card, SUID_Payment, Product_Sales_Line_Item, Manager_Menu},
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