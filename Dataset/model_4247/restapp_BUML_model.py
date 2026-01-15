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
restapp_model_Employee = Class(name="restapp::model::Employee")
restapp_model_User = Class(name="restapp::model::User")
Employee = Class(name="Employee")
restapp_model_Category = Class(name="restapp::model::Category")
restapp_model_Price = Class(name="restapp::model::Price")
Product = Class(name="Product")
restapp_model_Purchase = Class(name="restapp::model::Purchase")
Provider = Class(name="Provider")
User = Class(name="User")
restapp_model_Provider = Class(name="restapp::model::Provider")
restapp_model_ProductsPurchase = Class(name="restapp::model::ProductsPurchase")
restapp_model_Product = Class(name="restapp::model::Product")
Category = Class(name="Category")
PhysicalCard = Class(name="PhysicalCard")
restapp_model_ProductsCard = Class(name="restapp::model::ProductsCard")
Card = Class(name="Card")
Purchase = Class(name="Purchase")
restapp_model_PhysicalCard = Class(name="restapp::model::PhysicalCard")
restapp_model_Card = Class(name="restapp::model::Card")

# restapp_model_Employee class attributes and methods
restapp_model_Employee_id: Property = Property(name="id", type=IntegerType)
restapp_model_Employee_name: Property = Property(name="name", type=StringType)
restapp_model_Employee_rg: Property = Property(name="rg", type=StringType)
restapp_model_Employee_cpf: Property = Property(name="cpf", type=StringType)
restapp_model_Employee_address: Property = Property(name="address", type=StringType)
restapp_model_Employee_zipcode: Property = Property(name="zipcode", type=StringType)
restapp_model_Employee_phone: Property = Property(name="phone", type=StringType)
restapp_model_Employee_mobile: Property = Property(name="mobile", type=StringType)
restapp_model_Employee_working: Property = Property(name="working", type=BooleanType)
restapp_model_Employee_contracted: Property = Property(name="contracted", type=DateType)
restapp_model_Employee_fired: Property = Property(name="fired", type=DateType)
restapp_model_Employee_salary: Property = Property(name="salary", type=FloatType)
restapp_model_Employee_comission: Property = Property(name="comission", type=FloatType)
restapp_model_Employee_status: Property = Property(name="status", type=IntegerType)
restapp_model_Employee.attributes={restapp_model_Employee_fired, restapp_model_Employee_phone, restapp_model_Employee_zipcode, restapp_model_Employee_comission, restapp_model_Employee_status, restapp_model_Employee_mobile, restapp_model_Employee_name, restapp_model_Employee_contracted, restapp_model_Employee_working, restapp_model_Employee_id, restapp_model_Employee_salary, restapp_model_Employee_rg, restapp_model_Employee_cpf, restapp_model_Employee_address}

# restapp_model_User class attributes and methods
restapp_model_User_id: Property = Property(name="id", type=IntegerType)
restapp_model_User_user: Property = Property(name="user", type=StringType)
restapp_model_User_password: Property = Property(name="password", type=StringType)
restapp_model_User_status: Property = Property(name="status", type=IntegerType)
restapp_model_User.attributes={restapp_model_User_status, restapp_model_User_password, restapp_model_User_id, restapp_model_User_user}

# Employee class attributes and methods

# restapp_model_Category class attributes and methods
restapp_model_Category_id: Property = Property(name="id", type=IntegerType)
restapp_model_Category_name: Property = Property(name="name", type=StringType)
restapp_model_Category_description: Property = Property(name="description", type=StringType)
restapp_model_Category_status: Property = Property(name="status", type=IntegerType)
restapp_model_Category.attributes={restapp_model_Category_id, restapp_model_Category_description, restapp_model_Category_name, restapp_model_Category_status}

# restapp_model_Price class attributes and methods
restapp_model_Price_id: Property = Property(name="id", type=IntegerType)
restapp_model_Price_value: Property = Property(name="value", type=FloatType)
restapp_model_Price_date: Property = Property(name="date", type=DateType)
restapp_model_Price.attributes={restapp_model_Price_date, restapp_model_Price_value, restapp_model_Price_id}

# Product class attributes and methods

# restapp_model_Purchase class attributes and methods
restapp_model_Purchase_id: Property = Property(name="id", type=IntegerType)
restapp_model_Purchase_date: Property = Property(name="date", type=DateType)
restapp_model_Purchase_totalValue: Property = Property(name="totalValue", type=FloatType)
restapp_model_Purchase_discount: Property = Property(name="discount", type=IntegerType)
restapp_model_Purchase_totalWithDiscount: Property = Property(name="totalWithDiscount", type=FloatType)
restapp_model_Purchase.attributes={restapp_model_Purchase_totalWithDiscount, restapp_model_Purchase_totalValue, restapp_model_Purchase_discount, restapp_model_Purchase_date, restapp_model_Purchase_id}

# Provider class attributes and methods

# User class attributes and methods

# restapp_model_Provider class attributes and methods
restapp_model_Provider_id: Property = Property(name="id", type=IntegerType)
restapp_model_Provider_name: Property = Property(name="name", type=StringType)
restapp_model_Provider_phone: Property = Property(name="phone", type=StringType)
restapp_model_Provider_CNPJ: Property = Property(name="CNPJ", type=StringType)
restapp_model_Provider_Address: Property = Property(name="Address", type=StringType)
restapp_model_Provider_contact: Property = Property(name="contact", type=StringType)
restapp_model_Provider.attributes={restapp_model_Provider_phone, restapp_model_Provider_name, restapp_model_Provider_contact, restapp_model_Provider_CNPJ, restapp_model_Provider_Address, restapp_model_Provider_id}

# restapp_model_ProductsPurchase class attributes and methods
restapp_model_ProductsPurchase_quantity: Property = Property(name="quantity", type=IntegerType)
restapp_model_ProductsPurchase_unityValue: Property = Property(name="unityValue", type=FloatType)
restapp_model_ProductsPurchase_unityDiscount: Property = Property(name="unityDiscount", type=IntegerType)
restapp_model_ProductsPurchase_unityValueWithDiscount: Property = Property(name="unityValueWithDiscount", type=FloatType)
restapp_model_ProductsPurchase.attributes={restapp_model_ProductsPurchase_unityDiscount, restapp_model_ProductsPurchase_unityValue, restapp_model_ProductsPurchase_unityValueWithDiscount, restapp_model_ProductsPurchase_quantity}

# restapp_model_Product class attributes and methods
restapp_model_Product_id: Property = Property(name="id", type=IntegerType)
restapp_model_Product_name: Property = Property(name="name", type=StringType)
restapp_model_Product_description: Property = Property(name="description", type=StringType)
restapp_model_Product_stock: Property = Property(name="stock", type=IntegerType)
restapp_model_Product_status: Property = Property(name="status", type=IntegerType)
restapp_model_Product.attributes={restapp_model_Product_status, restapp_model_Product_id, restapp_model_Product_stock, restapp_model_Product_description, restapp_model_Product_name}

# Category class attributes and methods

# PhysicalCard class attributes and methods

# restapp_model_ProductsCard class attributes and methods
restapp_model_ProductsCard_id: Property = Property(name="id", type=IntegerType)
restapp_model_ProductsCard_date: Property = Property(name="date", type=DateType)
restapp_model_ProductsCard.attributes={restapp_model_ProductsCard_id, restapp_model_ProductsCard_date}

# Card class attributes and methods

# Purchase class attributes and methods

# restapp_model_PhysicalCard class attributes and methods
restapp_model_PhysicalCard_id: Property = Property(name="id", type=IntegerType)
restapp_model_PhysicalCard_number: Property = Property(name="number", type=IntegerType)
restapp_model_PhysicalCard_status: Property = Property(name="status", type=IntegerType)
restapp_model_PhysicalCard.attributes={restapp_model_PhysicalCard_number, restapp_model_PhysicalCard_status, restapp_model_PhysicalCard_id}

# restapp_model_Card class attributes and methods
restapp_model_Card_id: Property = Property(name="id", type=IntegerType)
restapp_model_Card_sellDate: Property = Property(name="sellDate", type=DateType)
restapp_model_Card_totalValue: Property = Property(name="totalValue", type=FloatType)
restapp_model_Card_discount: Property = Property(name="discount", type=IntegerType)
restapp_model_Card_totalValueWithDiscount: Property = Property(name="totalValueWithDiscount", type=FloatType)
restapp_model_Card_payedValue: Property = Property(name="payedValue", type=FloatType)
restapp_model_Card_change: Property = Property(name="change", type=FloatType)
restapp_model_Card.attributes={restapp_model_Card_totalValue, restapp_model_Card_payedValue, restapp_model_Card_id, restapp_model_Card_discount, restapp_model_Card_totalValueWithDiscount, restapp_model_Card_change, restapp_model_Card_sellDate}

# Relationships
newEReference10: BinaryAssociation = BinaryAssociation(
    name="newEReference10",
    ends={
        Property(name="Employee", type=restapp_model_User, multiplicity=Multiplicity(1, 1)),
        Property(name="restapp_model_User", type=Employee, multiplicity=Multiplicity(0, 1))
    }
)
newEReference11: BinaryAssociation = BinaryAssociation(
    name="newEReference11",
    ends={
        Property(name="Category", type=restapp_model_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="restapp_model_Product", type=Category, multiplicity=Multiplicity(0, 1))
    }
)
newEReference2: BinaryAssociation = BinaryAssociation(
    name="newEReference2",
    ends={
        Property(name="Product", type=restapp_model_Price, multiplicity=Multiplicity(1, 1)),
        Property(name="restapp_model_Price", type=Product, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
newEReference13: BinaryAssociation = BinaryAssociation(
    name="newEReference13",
    ends={
        Property(name="Provider", type=restapp_model_Purchase, multiplicity=Multiplicity(1, 1)),
        Property(name="restapp_model_Purchase", type=Provider, multiplicity=Multiplicity(0, 1))
    }
)
newEReference24: BinaryAssociation = BinaryAssociation(
    name="newEReference24",
    ends={
        Property(name="User", type=restapp_model_Purchase, multiplicity=Multiplicity(1, 1)),
        Property(name="restapp_model_Purchase5", type=User, multiplicity=Multiplicity(0, 1))
    }
)
newEReference110: BinaryAssociation = BinaryAssociation(
    name="newEReference110",
    ends={
        Property(name="PhysicalCard", type=restapp_model_Card, multiplicity=Multiplicity(1, 1)),
        Property(name="restapp_model_Card", type=PhysicalCard, multiplicity=Multiplicity(0, 1))
    }
)
newEReference111: BinaryAssociation = BinaryAssociation(
    name="newEReference111",
    ends={
        Property(name="Product12", type=restapp_model_ProductsCard, multiplicity=Multiplicity(1, 1)),
        Property(name="restapp_model_ProductsCard", type=Product, multiplicity=Multiplicity(0, 1))
    }
)
newEReference213: BinaryAssociation = BinaryAssociation(
    name="newEReference213",
    ends={
        Property(name="Card", type=restapp_model_ProductsCard, multiplicity=Multiplicity(1, 1)),
        Property(name="restapp_model_ProductsCard14", type=Card, multiplicity=Multiplicity(0, 1))
    }
)
newEReference315: BinaryAssociation = BinaryAssociation(
    name="newEReference315",
    ends={
        Property(name="User17", type=restapp_model_ProductsCard, multiplicity=Multiplicity(1, 1)),
        Property(name="restapp_model_ProductsCard16", type=User, multiplicity=Multiplicity(0, 1))
    }
)
newEReference16: BinaryAssociation = BinaryAssociation(
    name="newEReference16",
    ends={
        Property(name="Purchase", type=restapp_model_ProductsPurchase, multiplicity=Multiplicity(1, 1)),
        Property(name="restapp_model_ProductsPurchase", type=Purchase, multiplicity=Multiplicity(0, 1))
    }
)
newEReference27: BinaryAssociation = BinaryAssociation(
    name="newEReference27",
    ends={
        Property(name="Product9", type=restapp_model_ProductsPurchase, multiplicity=Multiplicity(1, 1)),
        Property(name="restapp_model_ProductsPurchase8", type=Product, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="restapp",
    types={restapp_model_Employee, restapp_model_User, Employee, restapp_model_Category, restapp_model_Price, Product, restapp_model_Purchase, Provider, User, restapp_model_Provider, restapp_model_ProductsPurchase, restapp_model_Product, Category, PhysicalCard, restapp_model_ProductsCard, Card, Purchase, restapp_model_PhysicalCard, restapp_model_Card},
    associations={newEReference10, newEReference11, newEReference2, newEReference13, newEReference24, newEReference110, newEReference111, newEReference213, newEReference315, newEReference16, newEReference27},
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