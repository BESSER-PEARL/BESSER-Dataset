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
creditcard = Class(name="creditcard")
customer = Class(name="customer")
shoppingcart = Class(name="shoppingcart")
itemtopurchase = Class(name="itemtopurchase")
preferredcustomer = Class(name="preferredcustomer")
customer_Actor = Class(name="customer_Actor")
shoppingcart_Actor = Class(name="shoppingcart_Actor")
purchase_UseCase = Class(name="purchase_UseCase")
placeorder_UseCase = Class(name="placeorder_UseCase")
cancelorder_UseCase = Class(name="cancelorder_UseCase")
selectsitem_UseCase = Class(name="selectsitem_UseCase")
checks_availability_of_item_UseCase = Class(name="checks_availability_of_item_UseCase")
asks_feedback_UseCase = Class(name="asks_feedback_UseCase")
requests_to_rate_the_website_UseCase = Class(name="requests_to_rate_the_website_UseCase")
gives_feedback_UseCase = Class(name="gives_feedback_UseCase")

# creditcard class attributes and methods
creditcard_issuer: Property = Property(name="issuer", type=StringType)
creditcard_number: Property = Property(name="number", type=IntegerType)
creditcard_expirationdate: Property = Property(name="expirationdate", type=DateType)
creditcard.attributes={creditcard_expirationdate, creditcard_number, creditcard_issuer}

# customer class attributes and methods
customer_name: Property = Property(name="name", type=StringType)
customer_addresstobill: Property = Property(name="addresstobill", type=IntegerType)
customer_addresstoship: Property = Property(name="addresstoship", type=IntegerType)
customer.attributes={customer_addresstobill, customer_name, customer_addresstoship}

# shoppingcart class attributes and methods
shoppingcart_subtotal: Property = Property(name="subtotal", type=IntegerType)
shoppingcart_salestax: Property = Property(name="salestax", type=IntegerType)
shoppingcart_total: Property = Property(name="total", type=IntegerType)
shoppingcart.attributes={shoppingcart_total, shoppingcart_salestax, shoppingcart_subtotal}

# itemtopurchase class attributes and methods
itemtopurchase_quantity: Property = Property(name="quantity", type=IntegerType)
itemtopurchase_itemtopurchase: Property = Property(name="itemtopurchase", type=IntegerType)
itemtopurchase.attributes={itemtopurchase_itemtopurchase, itemtopurchase_quantity}

# preferredcustomer class attributes and methods
preferredcustomer_discount: Property = Property(name="discount", type=IntegerType)
preferredcustomer.attributes={preferredcustomer_discount}

# customer_Actor class attributes and methods

# shoppingcart_Actor class attributes and methods

# purchase_UseCase class attributes and methods

# placeorder_UseCase class attributes and methods

# cancelorder_UseCase class attributes and methods

# selectsitem_UseCase class attributes and methods

# checks_availability_of_item_UseCase class attributes and methods

# asks_feedback_UseCase class attributes and methods

# requests_to_rate_the_website_UseCase class attributes and methods

# gives_feedback_UseCase class attributes and methods

# Relationships
shoppingcart_itemtopurchase: BinaryAssociation = BinaryAssociation(
    name="shoppingcart_itemtopurchase",
    ends={
        Property(name="itemtopurchase0", type=itemtopurchase, multiplicity=Multiplicity(0, 1)),
        Property(name="shoppingcart1", type=shoppingcart, multiplicity=Multiplicity(0, 1))
    }
)
creditcard_customer: BinaryAssociation = BinaryAssociation(
    name="creditcard_customer",
    ends={
        Property(name="customer2", type=customer, multiplicity=Multiplicity(0, 1)),
        Property(name="creditcard3", type=creditcard, multiplicity=Multiplicity(0, 1))
    }
)
customer_purchase: BinaryAssociation = BinaryAssociation(
    name="customer_purchase",
    ends={
        Property(name="purchase4", type=purchase_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer5", type=customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
shoppingcart_placeorder: BinaryAssociation = BinaryAssociation(
    name="shoppingcart_placeorder",
    ends={
        Property(name="placeorder6", type=placeorder_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="shoppingcart7", type=shoppingcart_Actor, multiplicity=Multiplicity(0, 1))
    }
)
shoppingcart_cancelorder: BinaryAssociation = BinaryAssociation(
    name="shoppingcart_cancelorder",
    ends={
        Property(name="cancelorder8", type=cancelorder_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="shoppingcart9", type=shoppingcart_Actor, multiplicity=Multiplicity(0, 1))
    }
)
customer_checks_availability_of_item: BinaryAssociation = BinaryAssociation(
    name="customer_checks_availability_of_item",
    ends={
        Property(name="checks_availability_of_item10", type=checks_availability_of_item_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer11", type=customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
selectsitem_customer: BinaryAssociation = BinaryAssociation(
    name="selectsitem_customer",
    ends={
        Property(name="customer12", type=customer_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="selectsitem13", type=selectsitem_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
shoppingcart_asks_feedback: BinaryAssociation = BinaryAssociation(
    name="shoppingcart_asks_feedback",
    ends={
        Property(name="asks_feedback14", type=asks_feedback_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="shoppingcart15", type=shoppingcart_Actor, multiplicity=Multiplicity(0, 1))
    }
)
shoppingcart_requests_to_rate_the_website: BinaryAssociation = BinaryAssociation(
    name="shoppingcart_requests_to_rate_the_website",
    ends={
        Property(name="requests_to_rate_the_website16", type=requests_to_rate_the_website_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="shoppingcart17", type=shoppingcart_Actor, multiplicity=Multiplicity(0, 1))
    }
)
shoppingcart_gives_feedback: BinaryAssociation = BinaryAssociation(
    name="shoppingcart_gives_feedback",
    ends={
        Property(name="gives_feedback18", type=gives_feedback_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="shoppingcart19", type=shoppingcart_Actor, multiplicity=Multiplicity(0, 1))
    }
)
gives_feedback_customer: BinaryAssociation = BinaryAssociation(
    name="gives_feedback_customer",
    ends={
        Property(name="customer20", type=customer_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="gives_feedback21", type=gives_feedback_UseCase, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="be027e97_a4e1_44b2_8eae_f0c48a42c1c1",
    types={creditcard, customer, shoppingcart, itemtopurchase, preferredcustomer, customer_Actor, shoppingcart_Actor, purchase_UseCase, placeorder_UseCase, cancelorder_UseCase, selectsitem_UseCase, checks_availability_of_item_UseCase, asks_feedback_UseCase, requests_to_rate_the_website_UseCase, gives_feedback_UseCase},
    associations={shoppingcart_itemtopurchase, creditcard_customer, customer_purchase, shoppingcart_placeorder, shoppingcart_cancelorder, customer_checks_availability_of_item, selectsitem_customer, shoppingcart_asks_feedback, shoppingcart_requests_to_rate_the_website, shoppingcart_gives_feedback, gives_feedback_customer},
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