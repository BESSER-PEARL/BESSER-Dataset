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
amazoninformational_Order = Class(name="amazoninformational::Order")
amazoninformational_Product = Class(name="amazoninformational::Product")
amazoninformational_Shipment = Class(name="amazoninformational::Shipment")
amazoninformational_Payment = Class(name="amazoninformational::Payment")
amazoninformational_Invoice = Class(name="amazoninformational::Invoice")
amazoninformational_Package = Class(name="amazoninformational::Package")

# amazoninformational_Order class attributes and methods

# amazoninformational_Product class attributes and methods
amazoninformational_Product_onHand: Property = Property(name="onHand", type=IntegerType)
amazoninformational_Product.attributes={amazoninformational_Product_onHand}

# amazoninformational_Shipment class attributes and methods

# amazoninformational_Payment class attributes and methods

# amazoninformational_Invoice class attributes and methods

# amazoninformational_Package class attributes and methods

# Relationships
products0: BinaryAssociation = BinaryAssociation(
    name="products0",
    ends={
        Property(name="amazoninformational_Product", type=amazoninformational_Order, multiplicity=Multiplicity(1, 1)),
        Property(name="amazoninformational_Order", type=amazoninformational_Product, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
order13: BinaryAssociation = BinaryAssociation(
    name="order13",
    ends={
        Property(name="Order14", type=amazoninformational_Invoice, multiplicity=Multiplicity(1, 1)),
        Property(name="invoice", type=amazoninformational_Order, multiplicity=Multiplicity(1, 1))
    }
)
payment15: BinaryAssociation = BinaryAssociation(
    name="payment15",
    ends={
        Property(name="amazoninformational_Payment", type=amazoninformational_Invoice, multiplicity=Multiplicity(1, 1)),
        Property(name="amazoninformational_Invoice", type=amazoninformational_Payment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shipment1: BinaryAssociation = BinaryAssociation(
    name="shipment1",
    ends={
        Property(name="Shipment", type=amazoninformational_Order, multiplicity=Multiplicity(1, 1)),
        Property(name="order", type=amazoninformational_Shipment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
invoice2: BinaryAssociation = BinaryAssociation(
    name="invoice2",
    ends={
        Property(name="Invoice", type=amazoninformational_Order, multiplicity=Multiplicity(1, 1)),
        Property(name="order3", type=amazoninformational_Invoice, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
packages4: BinaryAssociation = BinaryAssociation(
    name="packages4",
    ends={
        Property(name="Package", type=amazoninformational_Order, multiplicity=Multiplicity(1, 1)),
        Property(name="order5", type=amazoninformational_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
products6: BinaryAssociation = BinaryAssociation(
    name="products6",
    ends={
        Property(name="amazoninformational_Product7", type=amazoninformational_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="amazoninformational_Package", type=amazoninformational_Product, multiplicity=Multiplicity(0, 1))
    }
)
order8: BinaryAssociation = BinaryAssociation(
    name="order8",
    ends={
        Property(name="Order", type=amazoninformational_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="packages", type=amazoninformational_Order, multiplicity=Multiplicity(1, 1))
    }
)
package9: BinaryAssociation = BinaryAssociation(
    name="package9",
    ends={
        Property(name="amazoninformational_Package10", type=amazoninformational_Shipment, multiplicity=Multiplicity(1, 1)),
        Property(name="amazoninformational_Shipment", type=amazoninformational_Package, multiplicity=Multiplicity(0, 9999))
    }
)
order11: BinaryAssociation = BinaryAssociation(
    name="order11",
    ends={
        Property(name="Order12", type=amazoninformational_Shipment, multiplicity=Multiplicity(1, 1)),
        Property(name="shipment", type=amazoninformational_Order, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="amazoninformational",
    types={amazoninformational_Order, amazoninformational_Product, amazoninformational_Shipment, amazoninformational_Payment, amazoninformational_Invoice, amazoninformational_Package},
    associations={products0, order13, payment15, shipment1, invoice2, packages4, products6, order8, package9, order11},
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