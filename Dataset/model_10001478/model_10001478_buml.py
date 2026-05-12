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
Customer = Class(name="Customer")
Online_Order_and_CC_Processing = Class(name="Online_Order_and_CC_Processing")
createOrder = Class(name="createOrder")
updatePayment = Class(name="updatePayment")
viewOrder = Class(name="viewOrder")
deleteOrder = Class(name="deleteOrder")
Customer_Actor = Class(name="Customer_Actor")
Online_Order_and_CC_processing_Actor = Class(name="Online_Order_and_CC_processing_Actor")
Store_POS_System = Class(name="Store_POS_System")
chefTicket = Class(name="chefTicket")

# Customer class attributes and methods
Customer_name: Property = Property(name="name", type=StringType)
Customer_location: Property = Property(name="location", type=StringType)
Customer.attributes={Customer_name, Customer_location}

# Online_Order_and_CC_Processing class attributes and methods
Online_Order_and_CC_Processing_order: Property = Property(name="order", type=StringType)
Online_Order_and_CC_Processing_payment: Property = Property(name="payment", type=StringType)
Online_Order_and_CC_Processing_paymentApproved: Property = Property(name="paymentApproved", type=BooleanType)
Online_Order_and_CC_Processing.attributes={Online_Order_and_CC_Processing_paymentApproved, Online_Order_and_CC_Processing_payment, Online_Order_and_CC_Processing_order}

# createOrder class attributes and methods
createOrder_orderedItems: Property = Property(name="orderedItems", type=StringType)
createOrder.attributes={createOrder_orderedItems}

# updatePayment class attributes and methods
updatePayment_paymentInformation: Property = Property(name="paymentInformation", type=StringType)
updatePayment.attributes={updatePayment_paymentInformation}

# viewOrder class attributes and methods

# deleteOrder class attributes and methods

# Customer_Actor class attributes and methods

# Online_Order_and_CC_processing_Actor class attributes and methods

# Store_POS_System class attributes and methods
Store_POS_System_print: Property = Property(name="print", type=StringType)
Store_POS_System.attributes={Store_POS_System_print}

# chefTicket class attributes and methods

# Relationships
Customer_Online_Order_and_CC_Processing: BinaryAssociation = BinaryAssociation(
    name="Customer_Online_Order_and_CC_Processing",
    ends={
        Property(name="Online_Order_and_CC_Processing0", type=Online_Order_and_CC_Processing, multiplicity=Multiplicity(0, 1)),
        Property(name="customer1", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
Customer_createOrder: BinaryAssociation = BinaryAssociation(
    name="Customer_createOrder",
    ends={
        Property(name="createOrder22", type=createOrder, multiplicity=Multiplicity(0, 1)),
        Property(name="customer3", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
Customer_updatePayment: BinaryAssociation = BinaryAssociation(
    name="Customer_updatePayment",
    ends={
        Property(name="updatePayment24", type=updatePayment, multiplicity=Multiplicity(0, 1)),
        Property(name="customer5", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
Customer_deleteOrder: BinaryAssociation = BinaryAssociation(
    name="Customer_deleteOrder",
    ends={
        Property(name="deleteOrder26", type=deleteOrder, multiplicity=Multiplicity(0, 1)),
        Property(name="customer7", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
chefTicket_Store_POS_System: BinaryAssociation = BinaryAssociation(
    name="chefTicket_Store_POS_System",
    ends={
        Property(name="store_POS_System8", type=Store_POS_System, multiplicity=Multiplicity(0, 1)),
        Property(name="chefTicket29", type=chefTicket, multiplicity=Multiplicity(0, 1))
    }
)
Online_Order_and_CC_Processing_chefTicket: BinaryAssociation = BinaryAssociation(
    name="Online_Order_and_CC_Processing_chefTicket",
    ends={
        Property(name="chefTicket210", type=chefTicket, multiplicity=Multiplicity(0, 1)),
        Property(name="online_Order_and_CC_Processing11", type=Online_Order_and_CC_Processing, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_9a0zQKfsEemHhtAJ6lmxLQ",
    types={Customer, Online_Order_and_CC_Processing, createOrder, updatePayment, viewOrder, deleteOrder, Customer_Actor, Online_Order_and_CC_processing_Actor, Store_POS_System, chefTicket},
    associations={Customer_Online_Order_and_CC_Processing, Customer_createOrder, Customer_updatePayment, Customer_deleteOrder, chefTicket_Store_POS_System, Online_Order_and_CC_Processing_chefTicket},
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