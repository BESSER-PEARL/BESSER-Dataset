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
Cliente = Class(name="Cliente")
Pago = Class(name="Pago")
ShoppingCart = Class(name="ShoppingCart")
Toma_de_pedido = Class(name="Toma_de_pedido")
WebADM = Class(name="WebADM")
Order = Class(name="Order")
Lineamiento = Class(name="Lineamiento")
Entrega_producto = Class(name="Entrega_producto")

# Cliente class attributes and methods
Cliente_Asunto: Property = Property(name="Asunto", type=StringType)
Cliente_Ciudad: Property = Property(name="Ciudad", type=StringType)
Cliente_Nombre: Property = Property(name="Nombre", type=StringType)
Cliente.attributes={Cliente_Ciudad, Cliente_Asunto, Cliente_Nombre}

# Pago class attributes and methods
Pago_Contra_entrega: Property = Property(name="Contra_entrega", type=DateType)
Pago_PSI: Property = Property(name="PSI", type=FloatType)
Pago.attributes={Pago_PSI, Pago_Contra_entrega}

# ShoppingCart class attributes and methods
ShoppingCart_creationDate: Property = Property(name="creationDate", type=DateType)
ShoppingCart.attributes={ShoppingCart_creationDate}

# Toma_de_pedido class attributes and methods
Toma_de_pedido_Tipo_de_elemnto: Property = Property(name="Tipo_de_elemnto", type=StringType)
Toma_de_pedido_Despacho: Property = Property(name="Despacho", type=DateType)
Toma_de_pedido.attributes={Toma_de_pedido_Tipo_de_elemnto, Toma_de_pedido_Despacho}

# WebADM class attributes and methods
WebADM_login: Property = Property(name="login", type=StringType)
WebADM_password: Property = Property(name="password", type=StringType)
WebADM_state: Property = Property(name="state", type=StringType)
WebADM.attributes={WebADM_state, WebADM_login, WebADM_password}

# Order class attributes and methods
Order_number: Property = Property(name="number", type=IntegerType)
Order_ordered: Property = Property(name="ordered", type=DateType)
Order_total: Property = Property(name="total", type=FloatType)
Order_status: Property = Property(name="status", type=StringType)
Order.attributes={Order_total, Order_status, Order_number, Order_ordered}

# Lineamiento class attributes and methods
Lineamiento_Cantidad: Property = Property(name="Cantidad", type=IntegerType)
Lineamiento_Costo: Property = Property(name="Costo", type=FloatType)
Lineamiento.attributes={Lineamiento_Cantidad, Lineamiento_Costo}

# Entrega_producto class attributes and methods
Entrega_producto_Email_confirmaci_n: Property = Property(name="Email_confirmaci_n", type=StringType)
Entrega_producto_Agradecimiento: Property = Property(name="Agradecimiento", type=StringType)
Entrega_producto.attributes={Entrega_producto_Agradecimiento, Entrega_producto_Email_confirmaci_n}

# Relationships
Account_Payment: BinaryAssociation = BinaryAssociation(
    name="Account_Payment",
    ends={
        Property(name="p0", type=Pago, multiplicity=Multiplicity(0, 9999)),
        Property(name="acc1", type=Toma_de_pedido, multiplicity=Multiplicity(1, 1))
    }
)
WebUser_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="WebUser_ShoppingCart",
    ends={
        Property(name="shoppingCart2", type=ShoppingCart, multiplicity=Multiplicity(0, 1)),
        Property(name="webUser3", type=WebADM, multiplicity=Multiplicity(1, 1))
    }
)
WebUser_Customer: BinaryAssociation = BinaryAssociation(
    name="WebUser_Customer",
    ends={
        Property(name="customer4", type=Cliente, multiplicity=Multiplicity(1, 1)),
        Property(name="webUser5", type=WebADM, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Account: BinaryAssociation = BinaryAssociation(
    name="Customer_Account",
    ends={
        Property(name="account6", type=Toma_de_pedido, multiplicity=Multiplicity(1, 1)),
        Property(name="customer7", type=Cliente, multiplicity=Multiplicity(1, 1))
    }
)
Account_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="Account_ShoppingCart",
    ends={
        Property(name="cart8", type=Lineamiento, multiplicity=Multiplicity(1, 1)),
        Property(name="account9", type=Toma_de_pedido, multiplicity=Multiplicity(1, 1))
    }
)
ShoppingCart_LineItem: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_LineItem",
    ends={
        Property(name="items10", type=Lineamiento, multiplicity=Multiplicity(1, 1)),
        Property(name="sc11", type=ShoppingCart, multiplicity=Multiplicity(1, 1))
    }
)
Product_LineItem: BinaryAssociation = BinaryAssociation(
    name="Product_LineItem",
    ends={
        Property(name="lineItems12", type=Lineamiento, multiplicity=Multiplicity(0, 9999)),
        Property(name="product13", type=Entrega_producto, multiplicity=Multiplicity(1, 1))
    }
)
Order_LineItem: BinaryAssociation = BinaryAssociation(
    name="Order_LineItem",
    ends={
        Property(name="items14", type=Lineamiento, multiplicity=Multiplicity(1, 9999)),
        Property(name="order15", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
Account_Order: BinaryAssociation = BinaryAssociation(
    name="Account_Order",
    ends={
        Property(name="order16", type=Order, multiplicity=Multiplicity(0, 9999)),
        Property(name="account17", type=Toma_de_pedido, multiplicity=Multiplicity(1, 1))
    }
)
Payment_Order: BinaryAssociation = BinaryAssociation(
    name="Payment_Order",
    ends={
        Property(name="order18", type=Order, multiplicity=Multiplicity(1, 1)),
        Property(name="payment19", type=Pago, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_24f4043f_298c_4f75_b255_f4069b4b9cbf",
    types={Cliente, Pago, ShoppingCart, Toma_de_pedido, WebADM, Order, Lineamiento, Entrega_producto},
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