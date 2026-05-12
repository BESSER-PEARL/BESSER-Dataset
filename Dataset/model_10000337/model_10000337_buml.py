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
UserState: Enumeration = Enumeration(
    name="UserState",
    literals={
            
    }
)

# Classes
Empleado = Class(name="Empleado")
cliente = Class(name="cliente")
lugar = Class(name="lugar")
Consulta = Class(name="Consulta")
producto = Class(name="producto")
venta = Class(name="venta")
provvedor = Class(name="provvedor")

# Empleado class attributes and methods
Empleado_address: Property = Property(name="address", type=StringType)
Empleado_phone: Property = Property(name="phone", type=StringType)
Empleado_email: Property = Property(name="email", type=StringType)
Empleado.attributes={Empleado_address, Empleado_email, Empleado_phone}

# cliente class attributes and methods
cliente_paidDate: Property = Property(name="paidDate", type=DateType)
cliente_total: Property = Property(name="total", type=FloatType)
cliente_details: Property = Property(name="details", type=StringType)
cliente.attributes={cliente_paidDate, cliente_details, cliente_total}

# lugar class attributes and methods
lugar_Id_lugar: Property = Property(name="Id_lugar", type=IntegerType)
lugar_nombre: Property = Property(name="nombre", type=IntegerType)
lugar_attribute: Property = Property(name="attribute", type=StringType)
lugar.attributes={lugar_attribute, lugar_nombre, lugar_Id_lugar}

# Consulta class attributes and methods
Consulta_Administrador: Property = Property(name="Administrador", type=IntegerType)
Consulta_nombre: Property = Property(name="nombre", type=StringType)
Consulta_telefono: Property = Property(name="telefono", type=IntegerType)
Consulta_mail: Property = Property(name="mail", type=IntegerType)
Consulta.attributes={Consulta_mail, Consulta_Administrador, Consulta_telefono, Consulta_nombre}

# producto class attributes and methods
producto_number: Property = Property(name="number", type=IntegerType)
producto_ordered: Property = Property(name="ordered", type=DateType)
producto_shipped: Property = Property(name="shipped", type=BooleanType)
producto_shipTo: Property = Property(name="shipTo", type=StringType)
producto_total: Property = Property(name="total", type=FloatType)
producto_status: Property = Property(name="status", type=StringType)
producto.attributes={producto_shipped, producto_status, producto_total, producto_shipTo, producto_number, producto_ordered}

# venta class attributes and methods
venta_quantity: Property = Property(name="quantity", type=IntegerType)
venta_price: Property = Property(name="price", type=FloatType)
venta.attributes={venta_quantity, venta_price}

# provvedor class attributes and methods
provvedor_name: Property = Property(name="name", type=StringType)
provvedor_description: Property = Property(name="description", type=StringType)
provvedor.attributes={provvedor_description, provvedor_name}

# Relationships
WebUser_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="WebUser_ShoppingCart",
    ends={
        Property(name="shoppingCart0", type=lugar, multiplicity=Multiplicity(0, 1)),
        Property(name="webUser1", type=Consulta, multiplicity=Multiplicity(1, 1))
    }
)
ShoppingCart_LineItem: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_LineItem",
    ends={
        Property(name="items2", type=venta, multiplicity=Multiplicity(1, 1)),
        Property(name="sc3", type=lugar, multiplicity=Multiplicity(1, 1))
    }
)
Order_LineItem: BinaryAssociation = BinaryAssociation(
    name="Order_LineItem",
    ends={
        Property(name="items4", type=venta, multiplicity=Multiplicity(1, 9999)),
        Property(name="order5", type=producto, multiplicity=Multiplicity(0, 1))
    }
)
Payment_Order: BinaryAssociation = BinaryAssociation(
    name="Payment_Order",
    ends={
        Property(name="order6", type=producto, multiplicity=Multiplicity(1, 1)),
        Property(name="payment7", type=cliente, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_2a33b199_e41c_4891_85ab_ff7fa7fb9694",
    types={Empleado, cliente, lugar, Consulta, producto, venta, provvedor, UserState},
    associations={WebUser_ShoppingCart, ShoppingCart_LineItem, Order_LineItem, Payment_Order},
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