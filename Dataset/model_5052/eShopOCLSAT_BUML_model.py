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
eShop_Customer = Class(name="eShop::Customer")
eShop_Portal = Class(name="eShop::Portal")
eShop_Sale = Class(name="eShop::Sale")
eShop_GoldCustomer = Class(name="eShop::GoldCustomer")
Customer = Class(name="Customer")
eShop_SaleLine = Class(name="eShop::SaleLine")
eShop_Product = Class(name="eShop::Product")

# eShop_Customer class attributes and methods
eShop_Customer_name: Property = Property(name="name", type=IntegerType)
eShop_Customer_m_newCustomer: Method = Method(name="newCustomer", parameters={Parameter(name='name'), Parameter(name='p')}, type=StringType)
eShop_Customer.attributes={eShop_Customer_name}
eShop_Customer.methods={eShop_Customer_m_newCustomer}

# eShop_Portal class attributes and methods
eShop_Portal_name: Property = Property(name="name", type=StringType)
eShop_Portal_url: Property = Property(name="url", type=StringType)
eShop_Portal_m_removeGoldCategory: Method = Method(name="removeGoldCategory", parameters={Parameter(name='c')})
eShop_Portal.attributes={eShop_Portal_name, eShop_Portal_url}
eShop_Portal.methods={eShop_Portal_m_removeGoldCategory}

# eShop_Sale class attributes and methods
eShop_Sale_amount: Property = Property(name="amount", type=IntegerType)
eShop_Sale_id: Property = Property(name="id", type=IntegerType)
eShop_Sale_paid: Property = Property(name="paid", type=BooleanType)
eShop_Sale_m_addSaleLine: Method = Method(name="addSaleLine", parameters={Parameter(name='p'), Parameter(name='quantity')}, type=StringType)
eShop_Sale.attributes={eShop_Sale_paid, eShop_Sale_id, eShop_Sale_amount}
eShop_Sale.methods={eShop_Sale_m_addSaleLine}

# eShop_GoldCustomer class attributes and methods

# Customer class attributes and methods

# eShop_SaleLine class attributes and methods
eShop_SaleLine_quantity: Property = Property(name="quantity", type=IntegerType)
eShop_SaleLine.attributes={eShop_SaleLine_quantity}

# eShop_Product class attributes and methods
eShop_Product_price: Property = Property(name="price", type=IntegerType)
eShop_Product_stock: Property = Property(name="stock", type=IntegerType)
eShop_Product.attributes={eShop_Product_stock, eShop_Product_price}

# Relationships
portal0: BinaryAssociation = BinaryAssociation(
    name="portal0",
    ends={
        Property(name="Portal", type=eShop_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="customers", type=eShop_Portal, multiplicity=Multiplicity(1, 1))
    }
)
sale1: BinaryAssociation = BinaryAssociation(
    name="sale1",
    ends={
        Property(name="Sale", type=eShop_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="purchaser", type=eShop_Sale, multiplicity=Multiplicity(0, 9999))
    }
)
purchaser3: BinaryAssociation = BinaryAssociation(
    name="purchaser3",
    ends={
        Property(name="Customer4", type=eShop_Sale, multiplicity=Multiplicity(1, 1)),
        Property(name="sale", type=eShop_Customer, multiplicity=Multiplicity(1, 1))
    }
)
lines5: BinaryAssociation = BinaryAssociation(
    name="lines5",
    ends={
        Property(name="SaleLine", type=eShop_Sale, multiplicity=Multiplicity(1, 1)),
        Property(name="sale6", type=eShop_SaleLine, multiplicity=Multiplicity(0, 9999))
    }
)
sale7: BinaryAssociation = BinaryAssociation(
    name="sale7",
    ends={
        Property(name="Sale8", type=eShop_SaleLine, multiplicity=Multiplicity(1, 1)),
        Property(name="lines", type=eShop_Sale, multiplicity=Multiplicity(0, 1))
    }
)
product9: BinaryAssociation = BinaryAssociation(
    name="product9",
    ends={
        Property(name="Product", type=eShop_SaleLine, multiplicity=Multiplicity(1, 1)),
        Property(name="salesLines", type=eShop_Product, multiplicity=Multiplicity(1, 1))
    }
)
salesLines10: BinaryAssociation = BinaryAssociation(
    name="salesLines10",
    ends={
        Property(name="SaleLine11", type=eShop_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="product", type=eShop_SaleLine, multiplicity=Multiplicity(0, 9999))
    }
)
customers2: BinaryAssociation = BinaryAssociation(
    name="customers2",
    ends={
        Property(name="Customer", type=eShop_Portal, multiplicity=Multiplicity(1, 1)),
        Property(name="portal", type=eShop_Customer, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_eShop_GoldCustomer_Customer = Generalization(general=Customer, specific=eShop_GoldCustomer)

# Domain Model
domain_model = DomainModel(
    name="eShop",
    types={eShop_Customer, eShop_Portal, eShop_Sale, eShop_GoldCustomer, Customer, eShop_SaleLine, eShop_Product},
    associations={portal0, sale1, purchaser3, lines5, sale7, product9, salesLines10, customers2},
    generalizations={gen_eShop_GoldCustomer_Customer},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)