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
VISITS_ECOMMERCE_TAB_UseCase = Class(name="VISITS_ECOMMERCE_TAB_UseCase")
SELECTS_THE_ITEMS_SERVICE_UseCase = Class(name="SELECTS_THE_ITEMS_SERVICE_UseCase")
ADDS_ITEMS_SERVICE_TO_CART_UseCase = Class(name="ADDS_ITEMS_SERVICE_TO_CART_UseCase")
SELECTS_THE_MODE_OF_PAYMENT_UseCase = Class(name="SELECTS_THE_MODE_OF_PAYMENT_UseCase")
PAYS_THE_BILL_UseCase = Class(name="PAYS_THE_BILL_UseCase")
DELIVERS_THE_PRODUCT_UseCase = Class(name="DELIVERS_THE_PRODUCT_UseCase")
SUPPORT_AND_FEEDBACK_UseCase = Class(name="SUPPORT_AND_FEEDBACK_UseCase")
ADMINISTRATOR_Actor = Class(name="ADMINISTRATOR_Actor")
MAINTAINS_THE_PRODUCTS_SERVICES_UseCase = Class(name="MAINTAINS_THE_PRODUCTS_SERVICES_UseCase")
Customer = Class(name="Customer")
Order = Class(name="Order")
Product = Class(name="Product")
Warehouse = Class(name="Warehouse")
Transaction = Class(name="Transaction")

# CUSTOMER_Actor class attributes and methods

# VISITS_ECOMMERCE_TAB_UseCase class attributes and methods

# SELECTS_THE_ITEMS_SERVICE_UseCase class attributes and methods

# ADDS_ITEMS_SERVICE_TO_CART_UseCase class attributes and methods

# SELECTS_THE_MODE_OF_PAYMENT_UseCase class attributes and methods

# PAYS_THE_BILL_UseCase class attributes and methods

# DELIVERS_THE_PRODUCT_UseCase class attributes and methods

# SUPPORT_AND_FEEDBACK_UseCase class attributes and methods

# ADMINISTRATOR_Actor class attributes and methods

# MAINTAINS_THE_PRODUCTS_SERVICES_UseCase class attributes and methods

# Customer class attributes and methods
Customer_name: Property = Property(name="name", type=StringType)
Customer_id: Property = Property(name="id", type=IntegerType)
Customer_mailid: Property = Property(name="mailid", type=StringType)
Customer_address: Property = Property(name="address", type=StringType)
Customer_phoneno: Property = Property(name="phoneno", type=IntegerType)
Customer.attributes={Customer_mailid, Customer_phoneno, Customer_name, Customer_id, Customer_address}

# Order class attributes and methods
Order_item: Property = Property(name="item", type=StringType)
Order_quantity: Property = Property(name="quantity", type=IntegerType)
Order_list: Property = Property(name="list", type=StringType)
Order_attribute: Property = Property(name="attribute", type=StringType)
Order.attributes={Order_attribute, Order_quantity, Order_item, Order_list}

# Product class attributes and methods
Product_name: Property = Property(name="name", type=StringType)
Product_id: Property = Property(name="id", type=IntegerType)
Product_type: Property = Property(name="type", type=StringType)
Product.attributes={Product_type, Product_id, Product_name}

# Warehouse class attributes and methods
Warehouse_database: Property = Property(name="database", type=StringType)
Warehouse_location: Property = Property(name="location", type=StringType)
Warehouse.attributes={Warehouse_database, Warehouse_location}

# Transaction class attributes and methods
Transaction_cashondelivery: Property = Property(name="cashondelivery", type=IntegerType)
Transaction_debitcard: Property = Property(name="debitcard", type=IntegerType)
Transaction_creditcard: Property = Property(name="creditcard", type=IntegerType)
Transaction.attributes={Transaction_creditcard, Transaction_debitcard, Transaction_cashondelivery}

# Relationships
CUSTOMER_VISITS_THE_WEBSITE: BinaryAssociation = BinaryAssociation(
    name="CUSTOMER_VISITS_THE_WEBSITE",
    ends={
        Property(name="vISITS_THE_WEBSITE0", type=VISITS_ECOMMERCE_TAB_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="cUSTOMER1", type=CUSTOMER_Actor, multiplicity=Multiplicity(0, 1))
    }
)
CUSTOMER_SELECTS_THE_ITEMS_SERVICE: BinaryAssociation = BinaryAssociation(
    name="CUSTOMER_SELECTS_THE_ITEMS_SERVICE",
    ends={
        Property(name="sELECTS_THE_ITEMS_SERVICE2", type=SELECTS_THE_ITEMS_SERVICE_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="cUSTOMER3", type=CUSTOMER_Actor, multiplicity=Multiplicity(0, 1))
    }
)
CUSTOMER_ADDS_ITEMS_SERVICE_TO_CART: BinaryAssociation = BinaryAssociation(
    name="CUSTOMER_ADDS_ITEMS_SERVICE_TO_CART",
    ends={
        Property(name="aDDS_ITEMS_SERVICE_TO_CART4", type=ADDS_ITEMS_SERVICE_TO_CART_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="cUSTOMER5", type=CUSTOMER_Actor, multiplicity=Multiplicity(0, 1))
    }
)
CUSTOMER_SELECTS_THE_MODE_OF_PAYMENT: BinaryAssociation = BinaryAssociation(
    name="CUSTOMER_SELECTS_THE_MODE_OF_PAYMENT",
    ends={
        Property(name="sELECTS_THE_MODE_OF_PAYMENT6", type=SELECTS_THE_MODE_OF_PAYMENT_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="cUSTOMER7", type=CUSTOMER_Actor, multiplicity=Multiplicity(0, 1))
    }
)
CUSTOMER_PAYS_THE_BILL: BinaryAssociation = BinaryAssociation(
    name="CUSTOMER_PAYS_THE_BILL",
    ends={
        Property(name="pAYS_THE_BILL8", type=PAYS_THE_BILL_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="cUSTOMER9", type=CUSTOMER_Actor, multiplicity=Multiplicity(0, 1))
    }
)
CUSTOMER_SUPPORT_AND_FEEDBACK: BinaryAssociation = BinaryAssociation(
    name="CUSTOMER_SUPPORT_AND_FEEDBACK",
    ends={
        Property(name="sUPPORT_AND_FEEDBACK10", type=SUPPORT_AND_FEEDBACK_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="cUSTOMER11", type=CUSTOMER_Actor, multiplicity=Multiplicity(0, 1))
    }
)
SELECTS_THE_MODE_OF_PAYMENT_ADMINISTRATOR: BinaryAssociation = BinaryAssociation(
    name="SELECTS_THE_MODE_OF_PAYMENT_ADMINISTRATOR",
    ends={
        Property(name="aDMINISTRATOR12", type=ADMINISTRATOR_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="sELECTS_THE_MODE_OF_PAYMENT13", type=SELECTS_THE_MODE_OF_PAYMENT_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
PAYS_THE_BILL_ADMINISTRATOR: BinaryAssociation = BinaryAssociation(
    name="PAYS_THE_BILL_ADMINISTRATOR",
    ends={
        Property(name="aDMINISTRATOR14", type=ADMINISTRATOR_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="pAYS_THE_BILL15", type=PAYS_THE_BILL_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
DELIVERS_THE_PRODUCT_ADMINISTRATOR: BinaryAssociation = BinaryAssociation(
    name="DELIVERS_THE_PRODUCT_ADMINISTRATOR",
    ends={
        Property(name="aDMINISTRATOR16", type=ADMINISTRATOR_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="dELIVERS_THE_PRODUCT17", type=DELIVERS_THE_PRODUCT_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
MAINTAINS_THE_PRODUCTS_SERVICES_ADMINISTRATOR: BinaryAssociation = BinaryAssociation(
    name="MAINTAINS_THE_PRODUCTS_SERVICES_ADMINISTRATOR",
    ends={
        Property(name="aDMINISTRATOR18", type=ADMINISTRATOR_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="mAINTAINS_THE_PRODUCTS_SERVICES19", type=MAINTAINS_THE_PRODUCTS_SERVICES_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
SUPPORT_AND_FEEDBACK_ADMINISTRATOR: BinaryAssociation = BinaryAssociation(
    name="SUPPORT_AND_FEEDBACK_ADMINISTRATOR",
    ends={
        Property(name="aDMINISTRATOR20", type=ADMINISTRATOR_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="sUPPORT_AND_FEEDBACK21", type=SUPPORT_AND_FEEDBACK_UseCase, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_8c2cf10a_7464_49eb_b181_29b2df51bab2",
    types={CUSTOMER_Actor, VISITS_ECOMMERCE_TAB_UseCase, SELECTS_THE_ITEMS_SERVICE_UseCase, ADDS_ITEMS_SERVICE_TO_CART_UseCase, SELECTS_THE_MODE_OF_PAYMENT_UseCase, PAYS_THE_BILL_UseCase, DELIVERS_THE_PRODUCT_UseCase, SUPPORT_AND_FEEDBACK_UseCase, ADMINISTRATOR_Actor, MAINTAINS_THE_PRODUCTS_SERVICES_UseCase, Customer, Order, Product, Warehouse, Transaction},
    associations={CUSTOMER_VISITS_THE_WEBSITE, CUSTOMER_SELECTS_THE_ITEMS_SERVICE, CUSTOMER_ADDS_ITEMS_SERVICE_TO_CART, CUSTOMER_SELECTS_THE_MODE_OF_PAYMENT, CUSTOMER_PAYS_THE_BILL, CUSTOMER_SUPPORT_AND_FEEDBACK, SELECTS_THE_MODE_OF_PAYMENT_ADMINISTRATOR, PAYS_THE_BILL_ADMINISTRATOR, DELIVERS_THE_PRODUCT_ADMINISTRATOR, MAINTAINS_THE_PRODUCTS_SERVICES_ADMINISTRATOR, SUPPORT_AND_FEEDBACK_ADMINISTRATOR},
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