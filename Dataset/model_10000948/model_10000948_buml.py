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
OrderStatus: Enumeration = Enumeration(
    name="OrderStatus",
    literals={
            
    }
)

# Classes
Payment = Class(name="Payment")
WebUser = Class(name="WebUser")
Order = Class(name="Order")

# Payment class attributes and methods
Payment_paidDate: Property = Property(name="paidDate", type=DateType)
Payment_total: Property = Property(name="total", type=FloatType)
Payment_details: Property = Property(name="details", type=StringType)
Payment.attributes={Payment_details, Payment_total, Payment_paidDate}

# WebUser class attributes and methods
WebUser_login: Property = Property(name="login", type=StringType)
WebUser_password: Property = Property(name="password", type=StringType)
WebUser_state: Property = Property(name="state", type=StringType)
WebUser.attributes={WebUser_login, WebUser_password, WebUser_state}

# Order class attributes and methods
Order_number: Property = Property(name="number", type=IntegerType)
Order_ordered: Property = Property(name="ordered", type=DateType)
Order_shipped: Property = Property(name="shipped", type=BooleanType)
Order_shipTo: Property = Property(name="shipTo", type=StringType)
Order_total: Property = Property(name="total", type=FloatType)
Order_status: Property = Property(name="status", type=OrderStatus)
Order.attributes={Order_status, Order_total, Order_shipTo, Order_shipped, Order_ordered, Order_number}

# Relationships
Payment_Order: BinaryAssociation = BinaryAssociation(
    name="Payment_Order",
    ends={
        Property(name="order0", type=Order, multiplicity=Multiplicity(1, 1)),
        Property(name="payment1", type=Payment, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_735ce9aa_d88d_4661_8b37_0d39840e0c15",
    types={Payment, WebUser, Order, OrderStatus},
    associations={Payment_Order},
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