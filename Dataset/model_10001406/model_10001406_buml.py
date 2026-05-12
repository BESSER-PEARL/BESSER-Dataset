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
StatusulUtilizatorilor: Enumeration = Enumeration(
    name="StatusulUtilizatorilor",
    literals={
            
    }
)

Starea_comenzii: Enumeration = Enumeration(
    name="Starea_comenzii",
    literals={
            
    }
)

# Classes
client = Class(name="client")
Plata = Class(name="Plata")
Cosul_de_cumparaturi = Class(name="Cosul_de_cumparaturi")
cont = Class(name="cont")
WebUser = Class(name="WebUser")
Ordin = Class(name="Ordin")
LineItem = Class(name="LineItem")
Produse = Class(name="Produse")

# client class attributes and methods
client_address: Property = Property(name="address", type=StringType)
client_phone: Property = Property(name="phone", type=StringType)
client_email: Property = Property(name="email", type=StringType)
client.attributes={client_address, client_email, client_phone}

# Plata class attributes and methods
Plata_paidDate: Property = Property(name="paidDate", type=DateType)
Plata_total: Property = Property(name="total", type=FloatType)
Plata_details: Property = Property(name="details", type=StringType)
Plata.attributes={Plata_total, Plata_paidDate, Plata_details}

# Cosul_de_cumparaturi class attributes and methods
Cosul_de_cumparaturi_creationDate: Property = Property(name="creationDate", type=DateType)
Cosul_de_cumparaturi.attributes={Cosul_de_cumparaturi_creationDate}

# cont class attributes and methods
cont_billingAddress: Property = Property(name="billingAddress", type=StringType)
cont_open: Property = Property(name="open", type=DateType)
cont_closed: Property = Property(name="closed", type=DateType)
cont_isClosed: Property = Property(name="isClosed", type=BooleanType)
cont.attributes={cont_open, cont_isClosed, cont_closed, cont_billingAddress}

# WebUser class attributes and methods
WebUser_login: Property = Property(name="login", type=StringType)
WebUser_password: Property = Property(name="password", type=StringType)
WebUser_state: Property = Property(name="state", type=StatusulUtilizatorilor)
WebUser.attributes={WebUser_login, WebUser_state, WebUser_password}

# Ordin class attributes and methods
Ordin_number: Property = Property(name="number", type=IntegerType)
Ordin_ordered: Property = Property(name="ordered", type=DateType)
Ordin_shipped: Property = Property(name="shipped", type=BooleanType)
Ordin_shipTo: Property = Property(name="shipTo", type=StringType)
Ordin_total: Property = Property(name="total", type=FloatType)
Ordin_status: Property = Property(name="status", type=Starea_comenzii)
Ordin.attributes={Ordin_ordered, Ordin_number, Ordin_status, Ordin_total, Ordin_shipTo, Ordin_shipped}

# LineItem class attributes and methods
LineItem_quantity: Property = Property(name="quantity", type=IntegerType)
LineItem_price: Property = Property(name="price", type=FloatType)
LineItem.attributes={LineItem_quantity, LineItem_price}

# Produse class attributes and methods
Produse_name: Property = Property(name="name", type=StringType)
Produse_description: Property = Property(name="description", type=StringType)
Produse.attributes={Produse_name, Produse_description}

# Relationships
Account_Payment: BinaryAssociation = BinaryAssociation(
    name="Account_Payment",
    ends={
        Property(name="p0", type=Plata, multiplicity=Multiplicity(0, 9999)),
        Property(name="acc1", type=cont, multiplicity=Multiplicity(1, 1))
    }
)
WebUser_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="WebUser_ShoppingCart",
    ends={
        Property(name="Cosul_de_cumparaturi2", type=Cosul_de_cumparaturi, multiplicity=Multiplicity(0, 1)),
        Property(name="webUser3", type=WebUser, multiplicity=Multiplicity(1, 1))
    }
)
WebUser_Customer: BinaryAssociation = BinaryAssociation(
    name="WebUser_Customer",
    ends={
        Property(name="client4", type=client, multiplicity=Multiplicity(1, 1)),
        Property(name="webUser5", type=WebUser, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Account: BinaryAssociation = BinaryAssociation(
    name="Customer_Account",
    ends={
        Property(name="cont6", type=cont, multiplicity=Multiplicity(1, 1)),
        Property(name="client7", type=client, multiplicity=Multiplicity(1, 1))
    }
)
Account_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="Account_ShoppingCart",
    ends={
        Property(name="cart8", type=Cosul_de_cumparaturi, multiplicity=Multiplicity(1, 1)),
        Property(name="cont9", type=cont, multiplicity=Multiplicity(1, 1))
    }
)
ShoppingCart_LineItem: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_LineItem",
    ends={
        Property(name="articole10", type=LineItem, multiplicity=Multiplicity(1, 1)),
        Property(name="sc11", type=Cosul_de_cumparaturi, multiplicity=Multiplicity(1, 1))
    }
)
Product_LineItem: BinaryAssociation = BinaryAssociation(
    name="Product_LineItem",
    ends={
        Property(name="elemente_de_linie12", type=LineItem, multiplicity=Multiplicity(0, 9999)),
        Property(name="product13", type=Produse, multiplicity=Multiplicity(1, 1))
    }
)
Order_LineItem: BinaryAssociation = BinaryAssociation(
    name="Order_LineItem",
    ends={
        Property(name="articole14", type=LineItem, multiplicity=Multiplicity(1, 9999)),
        Property(name="order15", type=Ordin, multiplicity=Multiplicity(0, 1))
    }
)
Account_Order: BinaryAssociation = BinaryAssociation(
    name="Account_Order",
    ends={
        Property(name="ordin16", type=Ordin, multiplicity=Multiplicity(0, 9999)),
        Property(name="cont17", type=cont, multiplicity=Multiplicity(1, 1))
    }
)
Payment_Order: BinaryAssociation = BinaryAssociation(
    name="Payment_Order",
    ends={
        Property(name="ordin18", type=Ordin, multiplicity=Multiplicity(1, 1)),
        Property(name="payment19", type=Plata, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_53x30EihEeqonN_RS9oRzw",
    types={client, Plata, Cosul_de_cumparaturi, cont, WebUser, Ordin, LineItem, Produse, StatusulUtilizatorilor, Starea_comenzii},
    associations={Account_Payment, WebUser_ShoppingCart, WebUser_Customer, Customer_Account, Account_ShoppingCart, ShoppingCart_LineItem, Product_LineItem, Order_LineItem, Account_Order, Payment_Order},
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