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
CUSTOMER_Actor = Class(name="CUSTOMER_Actor")
VISITS_THE_WEBSITE_UseCase = Class(name="VISITS_THE_WEBSITE_UseCase")
CREATES_THE_WEBSITE_UseCase = Class(name="CREATES_THE_WEBSITE_UseCase")
SELECTS_THE_ITEMS_SERVICE_UseCase = Class(name="SELECTS_THE_ITEMS_SERVICE_UseCase")
ADDS_ITEMS_SERVICE_TO_CART_UseCase = Class(name="ADDS_ITEMS_SERVICE_TO_CART_UseCase")
SELECTS_THE_MODE_OF_PAYMENT_UseCase = Class(name="SELECTS_THE_MODE_OF_PAYMENT_UseCase")
PAYS_THE_BILL_UseCase = Class(name="PAYS_THE_BILL_UseCase")
DELIVERS_THE_PRODUCT_UseCase = Class(name="DELIVERS_THE_PRODUCT_UseCase")
SUPPORT_AND_FEEDBACK_UseCase = Class(name="SUPPORT_AND_FEEDBACK_UseCase")
WEB_DEVELOPER_Actor = Class(name="WEB_DEVELOPER_Actor")
ADMINISTRATOR_Actor = Class(name="ADMINISTRATOR_Actor")
MAINTAINS_THE_PRODUCTS_SERVICES_UseCase = Class(name="MAINTAINS_THE_PRODUCTS_SERVICES_UseCase")
Customer = Class(name="Customer")
Order = Class(name="Order")
Product = Class(name="Product")
Warehouse = Class(name="Warehouse")
Transaction = Class(name="Transaction")
Shipment = Class(name="Shipment")
Customercare = Class(name="Customercare")
Feedback = Class(name="Feedback")
Cancelorder = Class(name="Cancelorder")

# CUSTOMER_Actor class attributes and methods

# VISITS_THE_WEBSITE_UseCase class attributes and methods

# CREATES_THE_WEBSITE_UseCase class attributes and methods

# SELECTS_THE_ITEMS_SERVICE_UseCase class attributes and methods

# ADDS_ITEMS_SERVICE_TO_CART_UseCase class attributes and methods

# SELECTS_THE_MODE_OF_PAYMENT_UseCase class attributes and methods

# PAYS_THE_BILL_UseCase class attributes and methods

# DELIVERS_THE_PRODUCT_UseCase class attributes and methods

# SUPPORT_AND_FEEDBACK_UseCase class attributes and methods

# WEB_DEVELOPER_Actor class attributes and methods

# ADMINISTRATOR_Actor class attributes and methods

# MAINTAINS_THE_PRODUCTS_SERVICES_UseCase class attributes and methods

# Customer class attributes and methods
Customer_name: Property = Property(name="name", type=StringType)
Customer_id: Property = Property(name="id", type=IntegerType)
Customer_mailid: Property = Property(name="mailid", type=StringType)
Customer_address: Property = Property(name="address", type=StringType)
Customer_phoneno: Property = Property(name="phoneno", type=IntegerType)
Customer.attributes={Customer_address, Customer_phoneno, Customer_mailid, Customer_id, Customer_name}

# Order class attributes and methods
Order_item: Property = Property(name="item", type=StringType)
Order_quantity: Property = Property(name="quantity", type=IntegerType)
Order_list: Property = Property(name="list", type=StringType)
Order.attributes={Order_quantity, Order_item, Order_list}

# Product class attributes and methods
Product_name: Property = Property(name="name", type=StringType)
Product_id: Property = Property(name="id", type=IntegerType)
Product_type: Property = Property(name="type", type=StringType)
Product.attributes={Product_id, Product_name, Product_type}

# Warehouse class attributes and methods
Warehouse_database: Property = Property(name="database", type=StringType)
Warehouse_location: Property = Property(name="location", type=StringType)
Warehouse.attributes={Warehouse_database, Warehouse_location}

# Transaction class attributes and methods
Transaction_cashondelivery: Property = Property(name="cashondelivery", type=IntegerType)
Transaction_debitcard: Property = Property(name="debitcard", type=IntegerType)
Transaction_creditcard: Property = Property(name="creditcard", type=IntegerType)
Transaction.attributes={Transaction_debitcard, Transaction_cashondelivery, Transaction_creditcard}

# Shipment class attributes and methods
Shipment_packing: Property = Property(name="packing", type=StringType)
Shipment.attributes={Shipment_packing}

# Customercare class attributes and methods
Customercare_no: Property = Property(name="no", type=IntegerType)
Customercare_address: Property = Property(name="address", type=StringType)
Customercare.attributes={Customercare_no, Customercare_address}

# Feedback class attributes and methods
Feedback_customername: Property = Property(name="customername", type=StringType)
Feedback_id: Property = Property(name="id", type=IntegerType)
Feedback_phoneno: Property = Property(name="phoneno", type=IntegerType)
Feedback.attributes={Feedback_id, Feedback_customername, Feedback_phoneno}

# Cancelorder class attributes and methods
Cancelorder_item: Property = Property(name="item", type=StringType)
Cancelorder_quantity: Property = Property(name="quantity", type=IntegerType)
Cancelorder.attributes={Cancelorder_quantity, Cancelorder_item}

# Relationships
CREATES_THE_WEBSITE_WEB_DEVELOPER: BinaryAssociation = BinaryAssociation(
    name="CREATES_THE_WEBSITE_WEB_DEVELOPER",
    ends={
        Property(name="wEB_DEVELOPER0", type=WEB_DEVELOPER_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="cREATES_THE_WEBSITE1", type=CREATES_THE_WEBSITE_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
CUSTOMER_VISITS_THE_WEBSITE: BinaryAssociation = BinaryAssociation(
    name="CUSTOMER_VISITS_THE_WEBSITE",
    ends={
        Property(name="vISITS_THE_WEBSITE2", type=VISITS_THE_WEBSITE_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="cUSTOMER3", type=CUSTOMER_Actor, multiplicity=Multiplicity(0, 1))
    }
)
CUSTOMER_SELECTS_THE_ITEMS_SERVICE: BinaryAssociation = BinaryAssociation(
    name="CUSTOMER_SELECTS_THE_ITEMS_SERVICE",
    ends={
        Property(name="sELECTS_THE_ITEMS_SERVICE4", type=SELECTS_THE_ITEMS_SERVICE_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="cUSTOMER5", type=CUSTOMER_Actor, multiplicity=Multiplicity(0, 1))
    }
)
CUSTOMER_ADDS_ITEMS_SERVICE_TO_CART: BinaryAssociation = BinaryAssociation(
    name="CUSTOMER_ADDS_ITEMS_SERVICE_TO_CART",
    ends={
        Property(name="aDDS_ITEMS_SERVICE_TO_CART6", type=ADDS_ITEMS_SERVICE_TO_CART_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="cUSTOMER7", type=CUSTOMER_Actor, multiplicity=Multiplicity(0, 1))
    }
)
CUSTOMER_SELECTS_THE_MODE_OF_PAYMENT: BinaryAssociation = BinaryAssociation(
    name="CUSTOMER_SELECTS_THE_MODE_OF_PAYMENT",
    ends={
        Property(name="sELECTS_THE_MODE_OF_PAYMENT8", type=SELECTS_THE_MODE_OF_PAYMENT_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="cUSTOMER9", type=CUSTOMER_Actor, multiplicity=Multiplicity(0, 1))
    }
)
CUSTOMER_PAYS_THE_BILL: BinaryAssociation = BinaryAssociation(
    name="CUSTOMER_PAYS_THE_BILL",
    ends={
        Property(name="pAYS_THE_BILL10", type=PAYS_THE_BILL_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="cUSTOMER11", type=CUSTOMER_Actor, multiplicity=Multiplicity(0, 1))
    }
)
CUSTOMER_SUPPORT_AND_FEEDBACK: BinaryAssociation = BinaryAssociation(
    name="CUSTOMER_SUPPORT_AND_FEEDBACK",
    ends={
        Property(name="sUPPORT_AND_FEEDBACK12", type=SUPPORT_AND_FEEDBACK_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="cUSTOMER13", type=CUSTOMER_Actor, multiplicity=Multiplicity(0, 1))
    }
)
SELECTS_THE_MODE_OF_PAYMENT_ADMINISTRATOR: BinaryAssociation = BinaryAssociation(
    name="SELECTS_THE_MODE_OF_PAYMENT_ADMINISTRATOR",
    ends={
        Property(name="aDMINISTRATOR14", type=ADMINISTRATOR_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="sELECTS_THE_MODE_OF_PAYMENT15", type=SELECTS_THE_MODE_OF_PAYMENT_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
PAYS_THE_BILL_ADMINISTRATOR: BinaryAssociation = BinaryAssociation(
    name="PAYS_THE_BILL_ADMINISTRATOR",
    ends={
        Property(name="aDMINISTRATOR16", type=ADMINISTRATOR_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="pAYS_THE_BILL17", type=PAYS_THE_BILL_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
DELIVERS_THE_PRODUCT_ADMINISTRATOR: BinaryAssociation = BinaryAssociation(
    name="DELIVERS_THE_PRODUCT_ADMINISTRATOR",
    ends={
        Property(name="aDMINISTRATOR18", type=ADMINISTRATOR_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="dELIVERS_THE_PRODUCT19", type=DELIVERS_THE_PRODUCT_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
MAINTAINS_THE_PRODUCTS_SERVICES_ADMINISTRATOR: BinaryAssociation = BinaryAssociation(
    name="MAINTAINS_THE_PRODUCTS_SERVICES_ADMINISTRATOR",
    ends={
        Property(name="aDMINISTRATOR20", type=ADMINISTRATOR_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="mAINTAINS_THE_PRODUCTS_SERVICES21", type=MAINTAINS_THE_PRODUCTS_SERVICES_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
SUPPORT_AND_FEEDBACK_ADMINISTRATOR: BinaryAssociation = BinaryAssociation(
    name="SUPPORT_AND_FEEDBACK_ADMINISTRATOR",
    ends={
        Property(name="aDMINISTRATOR22", type=ADMINISTRATOR_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="sUPPORT_AND_FEEDBACK23", type=SUPPORT_AND_FEEDBACK_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
ORDER_PRODUCT: BinaryAssociation = BinaryAssociation(
    name="ORDER_PRODUCT",
    ends={
        Property(name="pRODUCT24", type=Product, multiplicity=Multiplicity(1, 9999)),
        Property(name="oRDER25", type=Order, multiplicity=Multiplicity(1, 9999))
    }
)
Customer_Customercare: BinaryAssociation = BinaryAssociation(
    name="Customer_Customercare",
    ends={
        Property(name="customercare26", type=Customercare, multiplicity=Multiplicity(1, 9999)),
        Property(name="customer27", type=Customer, multiplicity=Multiplicity(1, 9999))
    }
)
Warehouse_Shipment: BinaryAssociation = BinaryAssociation(
    name="Warehouse_Shipment",
    ends={
        Property(name="shipment28", type=Shipment, multiplicity=Multiplicity(0, 9999)),
        Property(name="warehouse29", type=Warehouse, multiplicity=Multiplicity(1, 9999))
    }
)
Product_Warehouse: BinaryAssociation = BinaryAssociation(
    name="Product_Warehouse",
    ends={
        Property(name="warehouse30", type=Warehouse, multiplicity=Multiplicity(1, 9999)),
        Property(name="product31", type=Product, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="ed5b961d_dd12_4876_bd35_bf09f3a4fda5",
    types={CUSTOMER_Actor, VISITS_THE_WEBSITE_UseCase, CREATES_THE_WEBSITE_UseCase, SELECTS_THE_ITEMS_SERVICE_UseCase, ADDS_ITEMS_SERVICE_TO_CART_UseCase, SELECTS_THE_MODE_OF_PAYMENT_UseCase, PAYS_THE_BILL_UseCase, DELIVERS_THE_PRODUCT_UseCase, SUPPORT_AND_FEEDBACK_UseCase, WEB_DEVELOPER_Actor, ADMINISTRATOR_Actor, MAINTAINS_THE_PRODUCTS_SERVICES_UseCase, Customer, Order, Product, Warehouse, Transaction, Shipment, Customercare, Feedback, Cancelorder},
    associations={CREATES_THE_WEBSITE_WEB_DEVELOPER, CUSTOMER_VISITS_THE_WEBSITE, CUSTOMER_SELECTS_THE_ITEMS_SERVICE, CUSTOMER_ADDS_ITEMS_SERVICE_TO_CART, CUSTOMER_SELECTS_THE_MODE_OF_PAYMENT, CUSTOMER_PAYS_THE_BILL, CUSTOMER_SUPPORT_AND_FEEDBACK, SELECTS_THE_MODE_OF_PAYMENT_ADMINISTRATOR, PAYS_THE_BILL_ADMINISTRATOR, DELIVERS_THE_PRODUCT_ADMINISTRATOR, MAINTAINS_THE_PRODUCTS_SERVICES_ADMINISTRATOR, SUPPORT_AND_FEEDBACK_ADMINISTRATOR, ORDER_PRODUCT, Customer_Customercare, Warehouse_Shipment, Product_Warehouse},
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