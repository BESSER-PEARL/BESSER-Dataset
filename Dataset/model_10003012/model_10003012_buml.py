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
Payment = Class(name="Payment")
Carro_de_Compras = Class(name="Carro_de_Compras")
Account = Class(name="Account")
Cliente = Class(name="Cliente")
Order = Class(name="Order")
Product = Class(name="Product")

# Payment class attributes and methods
Payment_paidDate: Property = Property(name="paidDate", type=DateType)
Payment_total: Property = Property(name="total", type=FloatType)
Payment_details: Property = Property(name="details", type=StringType)
Payment.attributes={Payment_details, Payment_total, Payment_paidDate}

# Carro_de_Compras class attributes and methods
Carro_de_Compras_IdCarro: Property = Property(name="IdCarro", type=IntegerType)
Carro_de_Compras_Producto: Property = Property(name="Producto", type=StringType)
Carro_de_Compras_Precio: Property = Property(name="Precio", type=IntegerType)
Carro_de_Compras_Cantidad: Property = Property(name="Cantidad", type=IntegerType)
Carro_de_Compras.attributes={Carro_de_Compras_IdCarro, Carro_de_Compras_Precio, Carro_de_Compras_Producto, Carro_de_Compras_Cantidad}

# Account class attributes and methods
Account_billingAddress: Property = Property(name="billingAddress", type=StringType)
Account_open: Property = Property(name="open", type=DateType)
Account_closed: Property = Property(name="closed", type=DateType)
Account_isClosed: Property = Property(name="isClosed", type=BooleanType)
Account.attributes={Account_billingAddress, Account_closed, Account_isClosed, Account_open}

# Cliente class attributes and methods
Cliente_Nombre: Property = Property(name="Nombre", type=StringType)
Cliente_email: Property = Property(name="email", type=StringType)
Cliente_Contacto: Property = Property(name="Contacto", type=IntegerType)
Cliente_Direcci_n: Property = Property(name="Direcci_n", type=StringType)
Cliente.attributes={Cliente_Nombre, Cliente_Contacto, Cliente_Direcci_n, Cliente_email}

# Order class attributes and methods
Order_number: Property = Property(name="number", type=IntegerType)
Order_ordered: Property = Property(name="ordered", type=DateType)
Order_shipped: Property = Property(name="shipped", type=BooleanType)
Order_shipTo: Property = Property(name="shipTo", type=StringType)
Order_total: Property = Property(name="total", type=FloatType)
Order_status: Property = Property(name="status", type=StringType)
Order.attributes={Order_shipped, Order_number, Order_status, Order_ordered, Order_shipTo, Order_total}

# Product class attributes and methods
Product_id: Property = Property(name="id", type=IntegerType)
Product_name: Property = Property(name="name", type=StringType)
Product_description: Property = Property(name="description", type=StringType)
Product.attributes={Product_name, Product_id, Product_description}

# Relationships
Payment_Order: BinaryAssociation = BinaryAssociation(
    name="Payment_Order",
    ends={
        Property(name="order8", type=Order, multiplicity=Multiplicity(1, 1)),
        Property(name="payment9", type=Payment, multiplicity=Multiplicity(0, 1))
    }
)
Account_Payment: BinaryAssociation = BinaryAssociation(
    name="Account_Payment",
    ends={
        Property(name="p0", type=Payment, multiplicity=Multiplicity(0, 9999)),
        Property(name="acc1", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
WebUser_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="WebUser_ShoppingCart",
    ends={
        Property(name="shoppingCart2", type=Carro_de_Compras, multiplicity=Multiplicity(0, 1)),
        Property(name="webUser3", type=Cliente, multiplicity=Multiplicity(1, 1))
    }
)
Account_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="Account_ShoppingCart",
    ends={
        Property(name="cart4", type=Carro_de_Compras, multiplicity=Multiplicity(1, 1)),
        Property(name="account5", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
Account_Order: BinaryAssociation = BinaryAssociation(
    name="Account_Order",
    ends={
        Property(name="order6", type=Order, multiplicity=Multiplicity(0, 9999)),
        Property(name="account7", type=Account, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="f51fd8af_292f_44c7_8a63_b9fc80cb4ab7",
    types={Payment, Carro_de_Compras, Account, Cliente, Order, Product},
    associations={Payment_Order, Account_Payment, WebUser_ShoppingCart, Account_ShoppingCart, Account_Order},
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