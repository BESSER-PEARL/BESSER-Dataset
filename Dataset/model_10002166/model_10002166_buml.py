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
online_shopping_Person = Class(name="online_shopping_Person")
online_shopping_Administrator = Class(name="online_shopping_Administrator")
online_shopping_Deoartment = Class(name="online_shopping_Deoartment")
online_shopping_Session_manager = Class(name="online_shopping_Session_manager")
online_shopping_Orders = Class(name="online_shopping_Orders")
online_shopping_Customer = Class(name="online_shopping_Customer")
online_shopping_Shopping_Card = Class(name="online_shopping_Shopping_Card")
online_shopping_Category = Class(name="online_shopping_Category")
online_shopping_Product = Class(name="online_shopping_Product")
online_shopping_Payment = Class(name="online_shopping_Payment")
online_shopping_Delivertiony_Informa = Class(name="online_shopping_Delivertiony_Informa")
online_shopping_Order_Detail = Class(name="online_shopping_Order_Detail")
Estring_Interface = Class(name="Estring_Interface")

# online_shopping_Person class attributes and methods
online_shopping_Person_Person_ID: Property = Property(name="Person_ID", type=Estring_Interface)
online_shopping_Person_Person_Password: Property = Property(name="Person_Password", type=Estring_Interface)
online_shopping_Person_Login_Status: Property = Property(name="Login_Status", type=Estring_Interface)
online_shopping_Person.attributes={online_shopping_Person_Person_ID, online_shopping_Person_Person_Password, online_shopping_Person_Login_Status}

# online_shopping_Administrator class attributes and methods
online_shopping_Administrator_Name: Property = Property(name="Name", type=Estring_Interface)
online_shopping_Administrator_Email: Property = Property(name="Email", type=Estring_Interface)
online_shopping_Administrator.attributes={online_shopping_Administrator_Email, online_shopping_Administrator_Name}

# online_shopping_Deoartment class attributes and methods
online_shopping_Deoartment_Department_ID: Property = Property(name="Department_ID", type=StringType)
online_shopping_Deoartment_Name: Property = Property(name="Name", type=StringType)
online_shopping_Deoartment_Description: Property = Property(name="Description", type=StringType)
online_shopping_Deoartment.attributes={online_shopping_Deoartment_Description, online_shopping_Deoartment_Name, online_shopping_Deoartment_Department_ID}

# online_shopping_Session_manager class attributes and methods
online_shopping_Session_manager_Person_ID: Property = Property(name="Person_ID", type=Estring_Interface)
online_shopping_Session_manager_Department_Name: Property = Property(name="Department_Name", type=Estring_Interface)
online_shopping_Session_manager.attributes={online_shopping_Session_manager_Department_Name, online_shopping_Session_manager_Person_ID}

# online_shopping_Orders class attributes and methods
online_shopping_Orders_Order_ID: Property = Property(name="Order_ID", type=IntegerType)
online_shopping_Orders_Date_Created: Property = Property(name="Date_Created", type=Estring_Interface)
online_shopping_Orders_Datw_Shipping: Property = Property(name="Datw_Shipping", type=Estring_Interface)
online_shopping_Orders_Customer_Name: Property = Property(name="Customer_Name", type=Estring_Interface)
online_shopping_Orders_Customer_ID: Property = Property(name="Customer_ID", type=Estring_Interface)
online_shopping_Orders.attributes={online_shopping_Orders_Order_ID, online_shopping_Orders_Customer_Name, online_shopping_Orders_Datw_Shipping, online_shopping_Orders_Date_Created, online_shopping_Orders_Customer_ID}

# online_shopping_Customer class attributes and methods
online_shopping_Customer_Name: Property = Property(name="Name", type=Estring_Interface)
online_shopping_Customer_Address: Property = Property(name="Address", type=Estring_Interface)
online_shopping_Customer_E_mail: Property = Property(name="E_mail", type=Estring_Interface)
online_shopping_Customer_Phone: Property = Property(name="Phone", type=StringType)
online_shopping_Customer_Shippinginfo: Property = Property(name="Shippinginfo", type=Estring_Interface)
online_shopping_Customer.attributes={online_shopping_Customer_E_mail, online_shopping_Customer_Name, online_shopping_Customer_Phone, online_shopping_Customer_Shippinginfo, online_shopping_Customer_Address}

# online_shopping_Shopping_Card class attributes and methods
online_shopping_Shopping_Card_Produced_Id: Property = Property(name="Produced_Id", type=StringType)
online_shopping_Shopping_Card_Cart_ID: Property = Property(name="Cart_ID", type=StringType)
online_shopping_Shopping_Card_Date_Added: Property = Property(name="Date_Added", type=StringType)
online_shopping_Shopping_Card_Quantity: Property = Property(name="Quantity", type=StringType)
online_shopping_Shopping_Card.attributes={online_shopping_Shopping_Card_Produced_Id, online_shopping_Shopping_Card_Date_Added, online_shopping_Shopping_Card_Quantity, online_shopping_Shopping_Card_Cart_ID}

# online_shopping_Category class attributes and methods
online_shopping_Category_Category_ID: Property = Property(name="Category_ID", type=StringType)
online_shopping_Category_Department_ID: Property = Property(name="Department_ID", type=StringType)
online_shopping_Category_Catemegory_Name: Property = Property(name="Catemegory_Name", type=Estring_Interface)
online_shopping_Category_Description: Property = Property(name="Description", type=Estring_Interface)
online_shopping_Category.attributes={online_shopping_Category_Department_ID, online_shopping_Category_Category_ID, online_shopping_Category_Catemegory_Name, online_shopping_Category_Description}

# online_shopping_Product class attributes and methods
online_shopping_Product_Price: Property = Property(name="Price", type=StringType)
online_shopping_Product_Image_File_Name: Property = Property(name="Image_File_Name", type=Estring_Interface)
online_shopping_Product_Product_ID: Property = Property(name="Product_ID", type=StringType)
online_shopping_Product_Name: Property = Property(name="Name", type=Estring_Interface)
online_shopping_Product_Description: Property = Property(name="Description", type=Estring_Interface)
online_shopping_Product.attributes={online_shopping_Product_Image_File_Name, online_shopping_Product_Name, online_shopping_Product_Product_ID, online_shopping_Product_Price, online_shopping_Product_Description}

# online_shopping_Payment class attributes and methods
online_shopping_Payment_Catch_Pay: Property = Property(name="Catch_Pay", type=StringType)
online_shopping_Payment_Online_Pay: Property = Property(name="Online_Pay", type=StringType)
online_shopping_Payment.attributes={online_shopping_Payment_Online_Pay, online_shopping_Payment_Catch_Pay}

# online_shopping_Delivertiony_Informa class attributes and methods
online_shopping_Delivertiony_Informa_Delivery_Address: Property = Property(name="Delivery_Address", type=Estring_Interface)
online_shopping_Delivertiony_Informa_Other_Delivery_Address: Property = Property(name="Other_Delivery_Address", type=Estring_Interface)
online_shopping_Delivertiony_Informa_Delivery_Phone: Property = Property(name="Delivery_Phone", type=StringType)
online_shopping_Delivertiony_Informa_Receiver_Name: Property = Property(name="Receiver_Name", type=Estring_Interface)
online_shopping_Delivertiony_Informa.attributes={online_shopping_Delivertiony_Informa_Delivery_Address, online_shopping_Delivertiony_Informa_Receiver_Name, online_shopping_Delivertiony_Informa_Other_Delivery_Address, online_shopping_Delivertiony_Informa_Delivery_Phone}

# online_shopping_Order_Detail class attributes and methods
online_shopping_Order_Detail_Order_ID: Property = Property(name="Order_ID", type=StringType)
online_shopping_Order_Detail_Product_ID: Property = Property(name="Product_ID", type=StringType)
online_shopping_Order_Detail_Product_Name: Property = Property(name="Product_Name", type=Estring_Interface)
online_shopping_Order_Detail_unit_Cost: Property = Property(name="unit_Cost", type=StringType)
online_shopping_Order_Detail_Quantity: Property = Property(name="Quantity", type=StringType)
online_shopping_Order_Detail_Subtotal: Property = Property(name="Subtotal", type=StringType)
online_shopping_Order_Detail.attributes={online_shopping_Order_Detail_unit_Cost, online_shopping_Order_Detail_Product_ID, online_shopping_Order_Detail_Order_ID, online_shopping_Order_Detail_Quantity, online_shopping_Order_Detail_Subtotal, online_shopping_Order_Detail_Product_Name}

# Estring_Interface class attributes and methods

# Relationships
Shopping_Card_Customer: BinaryAssociation = BinaryAssociation(
    name="Shopping_Card_Customer",
    ends={
        Property(name="Shopping_Card_Customer_00", type=online_shopping_Customer, multiplicity=Multiplicity(0, 1)),
        Property(name="shopping_Card1", type=online_shopping_Shopping_Card, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Shopping_Card: BinaryAssociation = BinaryAssociation(
    name="Customer_Shopping_Card",
    ends={
        Property(name="Customer_Shopping_Card_02", type=online_shopping_Shopping_Card, multiplicity=Multiplicity(0, 9999)),
        Property(name="Customer_Shopping_Card_13", type=online_shopping_Customer, multiplicity=Multiplicity(1, 1))
    }
)
Session_manager_Deoartment: BinaryAssociation = BinaryAssociation(
    name="Session_manager_Deoartment",
    ends={
        Property(name="Session_manager_Deoartment_04", type=online_shopping_Deoartment, multiplicity=Multiplicity(1, 1)),
        Property(name="Session_manager_Deoartment_15", type=online_shopping_Session_manager, multiplicity=Multiplicity(1, 1))
    }
)
Deoartment_Category: BinaryAssociation = BinaryAssociation(
    name="Deoartment_Category",
    ends={
        Property(name="Deoartment_Category_06", type=online_shopping_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="Deoartment_Category_17", type=online_shopping_Deoartment, multiplicity=Multiplicity(1, 1))
    }
)
Category_Product: BinaryAssociation = BinaryAssociation(
    name="Category_Product",
    ends={
        Property(name="Category_Product_08", type=online_shopping_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="Category_Product_19", type=online_shopping_Category, multiplicity=Multiplicity(1, 1))
    }
)
Session_manager_Person: BinaryAssociation = BinaryAssociation(
    name="Session_manager_Person",
    ends={
        Property(name="Session_manager_Person_010", type=online_shopping_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="Session_manager_Person_111", type=online_shopping_Session_manager, multiplicity=Multiplicity(1, 1))
    }
)
Shopping_Card_Product: BinaryAssociation = BinaryAssociation(
    name="Shopping_Card_Product",
    ends={
        Property(name="Shopping_Card_Product_012", type=online_shopping_Product, multiplicity=Multiplicity(0, 9999)),
        Property(name="Shopping_Card_Product_113", type=online_shopping_Shopping_Card, multiplicity=Multiplicity(0, 9999))
    }
)
Product_Order_Detail: BinaryAssociation = BinaryAssociation(
    name="Product_Order_Detail",
    ends={
        Property(name="order_Detail14", type=online_shopping_Order_Detail, multiplicity=Multiplicity(0, 9999)),
        Property(name="product15", type=online_shopping_Product, multiplicity=Multiplicity(1, 1))
    }
)
Orders_Order_Detail: BinaryAssociation = BinaryAssociation(
    name="Orders_Order_Detail",
    ends={
        Property(name="Orders_Order_Detail_016", type=online_shopping_Order_Detail, multiplicity=Multiplicity(1, 1)),
        Property(name="Orders_Order_Detail_117", type=online_shopping_Orders, multiplicity=Multiplicity(1, 1))
    }
)
Orders_Delivertiony_Informa: BinaryAssociation = BinaryAssociation(
    name="Orders_Delivertiony_Informa",
    ends={
        Property(name="Orders_Delivertiony_Informa_018", type=online_shopping_Delivertiony_Informa, multiplicity=Multiplicity(1, 1)),
        Property(name="Orders_Delivertiony_Informa_119", type=online_shopping_Orders, multiplicity=Multiplicity(1, 1))
    }
)
Shopping_Card_Payment: BinaryAssociation = BinaryAssociation(
    name="Shopping_Card_Payment",
    ends={
        Property(name="Shopping_Card_Payment_020", type=online_shopping_Payment, multiplicity=Multiplicity(1, 1)),
        Property(name="Shopping_Card_Payment_121", type=online_shopping_Shopping_Card, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Orders: BinaryAssociation = BinaryAssociation(
    name="Customer_Orders",
    ends={
        Property(name="Customer_Orders_022", type=online_shopping_Orders, multiplicity=Multiplicity(0, 9999)),
        Property(name="Customer_Orders_123", type=online_shopping_Customer, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_tt9s4I9CEemqpd237shV0A",
    types={online_shopping_Person, online_shopping_Administrator, online_shopping_Deoartment, online_shopping_Session_manager, online_shopping_Orders, online_shopping_Customer, online_shopping_Shopping_Card, online_shopping_Category, online_shopping_Product, online_shopping_Payment, online_shopping_Delivertiony_Informa, online_shopping_Order_Detail, Estring_Interface},
    associations={Shopping_Card_Customer, Customer_Shopping_Card, Session_manager_Deoartment, Deoartment_Category, Category_Product, Session_manager_Person, Shopping_Card_Product, Product_Order_Detail, Orders_Order_Detail, Orders_Delivertiony_Informa, Shopping_Card_Payment, Customer_Orders},
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