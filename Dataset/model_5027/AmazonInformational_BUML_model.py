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
amazoninformational_Package = Class(name="amazoninformational::Package")
amazoninformational_Customer = Class(name="amazoninformational::Customer")
amazoninformational_Payment = Class(name="amazoninformational::Payment")
amazoninformational_Order = Class(name="amazoninformational::Order")
amazoninformational_Product = Class(name="amazoninformational::Product")
amazoninformational_Shipment = Class(name="amazoninformational::Shipment")
amazoninformational_Invoice = Class(name="amazoninformational::Invoice")

# amazoninformational_Package class attributes and methods
amazoninformational_Package_location: Property = Property(name="location", type=StringType)
amazoninformational_Package.attributes={amazoninformational_Package_location}

# amazoninformational_Customer class attributes and methods
amazoninformational_Customer_inGoodStanding: Property = Property(name="inGoodStanding", type=BooleanType)
amazoninformational_Customer_creditLimit: Property = Property(name="creditLimit", type=FloatType)
amazoninformational_Customer_consummedCredit: Property = Property(name="consummedCredit", type=FloatType)
amazoninformational_Customer_address: Property = Property(name="address", type=StringType)
amazoninformational_Customer_isVIP: Property = Property(name="isVIP", type=BooleanType)
amazoninformational_Customer.attributes={amazoninformational_Customer_creditLimit, amazoninformational_Customer_address, amazoninformational_Customer_consummedCredit, amazoninformational_Customer_isVIP, amazoninformational_Customer_inGoodStanding}

# amazoninformational_Payment class attributes and methods

# amazoninformational_Order class attributes and methods
amazoninformational_Order_status: Property = Property(name="status", type=StringType)
amazoninformational_Order_totalAmount: Property = Property(name="totalAmount", type=FloatType)
amazoninformational_Order.attributes={amazoninformational_Order_status, amazoninformational_Order_totalAmount}

# amazoninformational_Product class attributes and methods
amazoninformational_Product_onHand: Property = Property(name="onHand", type=IntegerType)
amazoninformational_Product.attributes={amazoninformational_Product_onHand}

# amazoninformational_Shipment class attributes and methods

# amazoninformational_Invoice class attributes and methods

# Relationships
invoice2: BinaryAssociation = BinaryAssociation(
    name="invoice2",
    ends={
        Property(name="order3", type=amazoninformational_Invoice, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="Invoice", type=amazoninformational_Order, multiplicity=Multiplicity(1, 1))
    }
)
packages4: BinaryAssociation = BinaryAssociation(
    name="packages4",
    ends={
        Property(name="Package", type=amazoninformational_Order, multiplicity=Multiplicity(1, 1)),
        Property(name="order5", type=amazoninformational_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
customer6: BinaryAssociation = BinaryAssociation(
    name="customer6",
    ends={
        Property(name="amazoninformational_Customer", type=amazoninformational_Order, multiplicity=Multiplicity(1, 1)),
        Property(name="amazoninformational_Order7", type=amazoninformational_Customer, multiplicity=Multiplicity(0, 1))
    }
)
products8: BinaryAssociation = BinaryAssociation(
    name="products8",
    ends={
        Property(name="amazoninformational_Product9", type=amazoninformational_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="amazoninformational_Package", type=amazoninformational_Product, multiplicity=Multiplicity(0, 1))
    }
)
order10: BinaryAssociation = BinaryAssociation(
    name="order10",
    ends={
        Property(name="Order", type=amazoninformational_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="packages", type=amazoninformational_Order, multiplicity=Multiplicity(1, 1))
    }
)
package11: BinaryAssociation = BinaryAssociation(
    name="package11",
    ends={
        Property(name="amazoninformational_Package12", type=amazoninformational_Shipment, multiplicity=Multiplicity(1, 1)),
        Property(name="amazoninformational_Shipment", type=amazoninformational_Package, multiplicity=Multiplicity(1, 9999))
    }
)
order13: BinaryAssociation = BinaryAssociation(
    name="order13",
    ends={
        Property(name="Order14", type=amazoninformational_Shipment, multiplicity=Multiplicity(1, 1)),
        Property(name="shipment", type=amazoninformational_Order, multiplicity=Multiplicity(0, 1))
    }
)
order15: BinaryAssociation = BinaryAssociation(
    name="order15",
    ends={
        Property(name="Order16", type=amazoninformational_Invoice, multiplicity=Multiplicity(1, 1)),
        Property(name="invoice", type=amazoninformational_Order, multiplicity=Multiplicity(1, 1))
    }
)
payment17: BinaryAssociation = BinaryAssociation(
    name="payment17",
    ends={
        Property(name="amazoninformational_Payment", type=amazoninformational_Invoice, multiplicity=Multiplicity(1, 1)),
        Property(name="amazoninformational_Invoice", type=amazoninformational_Payment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
products0: BinaryAssociation = BinaryAssociation(
    name="products0",
    ends={
        Property(name="amazoninformational_Product", type=amazoninformational_Order, multiplicity=Multiplicity(1, 1)),
        Property(name="amazoninformational_Order", type=amazoninformational_Product, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
shipment1: BinaryAssociation = BinaryAssociation(
    name="shipment1",
    ends={
        Property(name="Shipment", type=amazoninformational_Order, multiplicity=Multiplicity(1, 1)),
        Property(name="order", type=amazoninformational_Shipment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="amazoninformational",
    types={amazoninformational_Package, amazoninformational_Customer, amazoninformational_Payment, amazoninformational_Order, amazoninformational_Product, amazoninformational_Shipment, amazoninformational_Invoice},
    associations={invoice2, packages4, customer6, products8, order10, package11, order13, order15, payment17, products0, shipment1},
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