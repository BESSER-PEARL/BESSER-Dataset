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
Vendedor = Class(name="Vendedor")
Pago = Class(name="Pago")
Venta = Class(name="Venta")
Cuenta = Class(name="Cuenta")
Login = Class(name="Login")
Orden = Class(name="Orden")
ItemOrden = Class(name="ItemOrden")
Licor = Class(name="Licor")

# Vendedor class attributes and methods
Vendedor_address: Property = Property(name="address", type=StringType)
Vendedor_phone: Property = Property(name="phone", type=StringType)
Vendedor_email: Property = Property(name="email", type=StringType)
Vendedor.attributes={Vendedor_email, Vendedor_phone, Vendedor_address}

# Pago class attributes and methods
Pago_paidDate: Property = Property(name="paidDate", type=DateType)
Pago_total: Property = Property(name="total", type=FloatType)
Pago_details: Property = Property(name="details", type=StringType)
Pago.attributes={Pago_total, Pago_paidDate, Pago_details}

# Venta class attributes and methods
Venta_creationDate: Property = Property(name="creationDate", type=DateType)
Venta.attributes={Venta_creationDate}

# Cuenta class attributes and methods
Cuenta_billingAddress: Property = Property(name="billingAddress", type=StringType)
Cuenta_open: Property = Property(name="open", type=DateType)
Cuenta_closed: Property = Property(name="closed", type=DateType)
Cuenta_isClosed: Property = Property(name="isClosed", type=BooleanType)
Cuenta.attributes={Cuenta_billingAddress, Cuenta_closed, Cuenta_open, Cuenta_isClosed}

# Login class attributes and methods
Login_login: Property = Property(name="login", type=StringType)
Login_password: Property = Property(name="password", type=StringType)
Login_state: Property = Property(name="state", type=StringType)
Login.attributes={Login_password, Login_state, Login_login}

# Orden class attributes and methods
Orden_number: Property = Property(name="number", type=IntegerType)
Orden_ordered: Property = Property(name="ordered", type=DateType)
Orden_shipped: Property = Property(name="shipped", type=BooleanType)
Orden_shipTo: Property = Property(name="shipTo", type=StringType)
Orden_total: Property = Property(name="total", type=FloatType)
Orden_status: Property = Property(name="status", type=StringType)
Orden.attributes={Orden_shipped, Orden_shipTo, Orden_number, Orden_ordered, Orden_total, Orden_status}

# ItemOrden class attributes and methods
ItemOrden_quantity: Property = Property(name="quantity", type=IntegerType)
ItemOrden_price: Property = Property(name="price", type=FloatType)
ItemOrden.attributes={ItemOrden_quantity, ItemOrden_price}

# Licor class attributes and methods
Licor_name: Property = Property(name="name", type=StringType)
Licor_description: Property = Property(name="description", type=StringType)
Licor.attributes={Licor_description, Licor_name}

# Relationships
Payment_Order: BinaryAssociation = BinaryAssociation(
    name="Payment_Order",
    ends={
        Property(name="Orden18", type=Orden, multiplicity=Multiplicity(1, 1)),
        Property(name="payment19", type=Pago, multiplicity=Multiplicity(0, 1))
    }
)
Account_Payment: BinaryAssociation = BinaryAssociation(
    name="Account_Payment",
    ends={
        Property(name="p0", type=Pago, multiplicity=Multiplicity(0, 9999)),
        Property(name="acc1", type=Cuenta, multiplicity=Multiplicity(1, 1))
    }
)
WebUser_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="WebUser_ShoppingCart",
    ends={
        Property(name="Venta2", type=Venta, multiplicity=Multiplicity(0, 1)),
        Property(name="UsuarioWeb3", type=Login, multiplicity=Multiplicity(1, 1))
    }
)
WebUser_Customer: BinaryAssociation = BinaryAssociation(
    name="WebUser_Customer",
    ends={
        Property(name="Vendedor4", type=Vendedor, multiplicity=Multiplicity(1, 1)),
        Property(name="UsuarioWeb5", type=Login, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Account: BinaryAssociation = BinaryAssociation(
    name="Customer_Account",
    ends={
        Property(name="Cuenta6", type=Cuenta, multiplicity=Multiplicity(1, 1)),
        Property(name="Vendedor7", type=Vendedor, multiplicity=Multiplicity(1, 1))
    }
)
Account_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="Account_ShoppingCart",
    ends={
        Property(name="cart8", type=Venta, multiplicity=Multiplicity(1, 1)),
        Property(name="Cuenta9", type=Cuenta, multiplicity=Multiplicity(1, 1))
    }
)
ShoppingCart_LineItem: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_LineItem",
    ends={
        Property(name="items10", type=ItemOrden, multiplicity=Multiplicity(1, 1)),
        Property(name="sc11", type=Venta, multiplicity=Multiplicity(1, 1))
    }
)
Product_LineItem: BinaryAssociation = BinaryAssociation(
    name="Product_LineItem",
    ends={
        Property(name="lineItems12", type=ItemOrden, multiplicity=Multiplicity(0, 9999)),
        Property(name="Producto13", type=Licor, multiplicity=Multiplicity(1, 1))
    }
)
Order_LineItem: BinaryAssociation = BinaryAssociation(
    name="Order_LineItem",
    ends={
        Property(name="items14", type=ItemOrden, multiplicity=Multiplicity(1, 9999)),
        Property(name="order15", type=Orden, multiplicity=Multiplicity(0, 1))
    }
)
Account_Order: BinaryAssociation = BinaryAssociation(
    name="Account_Order",
    ends={
        Property(name="Orden16", type=Orden, multiplicity=Multiplicity(0, 9999)),
        Property(name="Cuenta17", type=Cuenta, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_2b96ca54_5207_4e6a_9b99_d90ed61f195a",
    types={Vendedor, Pago, Venta, Cuenta, Login, Orden, ItemOrden, Licor},
    associations={Payment_Order, Account_Payment, WebUser_ShoppingCart, WebUser_Customer, Customer_Account, Account_ShoppingCart, ShoppingCart_LineItem, Product_LineItem, Order_LineItem, Account_Order},
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