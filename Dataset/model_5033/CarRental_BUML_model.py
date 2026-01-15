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
CarRentalModel_Agency = Class(name="CarRentalModel::Agency")
CarRentalModel_Craft = Class(name="CarRentalModel::Craft", is_abstract=True)
CarRentalModel_CarRental = Class(name="CarRentalModel::CarRental")
CarRentalModel_Customer = Class(name="CarRentalModel::Customer")
CarRentalModel_Order = Class(name="CarRentalModel::Order")
CarRentalModel_VipCustomer = Class(name="CarRentalModel::VipCustomer")
Customer = Class(name="Customer")
CarRentalModel_Motorcycle = Class(name="CarRentalModel::Motorcycle")
Craft = Class(name="Craft")
CarRentalModel_Automobile = Class(name="CarRentalModel::Automobile")

# CarRentalModel_Agency class attributes and methods
CarRentalModel_Agency_street: Property = Property(name="street", type=StringType)
CarRentalModel_Agency_place: Property = Property(name="place", type=StringType)
CarRentalModel_Agency_zip: Property = Property(name="zip", type=IntegerType)
CarRentalModel_Agency.attributes={CarRentalModel_Agency_street, CarRentalModel_Agency_place, CarRentalModel_Agency_zip}

# CarRentalModel_Craft class attributes and methods
CarRentalModel_Craft_vin: Property = Property(name="vin", type=IntegerType)
CarRentalModel_Craft_charge: Property = Property(name="charge", type=FloatType)
CarRentalModel_Craft_licenseNo: Property = Property(name="licenseNo", type=StringType)
CarRentalModel_Craft.attributes={CarRentalModel_Craft_charge, CarRentalModel_Craft_vin, CarRentalModel_Craft_licenseNo}

# CarRentalModel_CarRental class attributes and methods

# CarRentalModel_Customer class attributes and methods
CarRentalModel_Customer_identifier: Property = Property(name="identifier", type=StringType)
CarRentalModel_Customer_lastname: Property = Property(name="lastname", type=StringType)
CarRentalModel_Customer_surname: Property = Property(name="surname", type=StringType)
CarRentalModel_Customer.attributes={CarRentalModel_Customer_lastname, CarRentalModel_Customer_identifier, CarRentalModel_Customer_surname}

# CarRentalModel_Order class attributes and methods
CarRentalModel_Order_orderDate: Property = Property(name="orderDate", type=DateType)
CarRentalModel_Order_price: Property = Property(name="price", type=FloatType)
CarRentalModel_Order.attributes={CarRentalModel_Order_price, CarRentalModel_Order_orderDate}

# CarRentalModel_VipCustomer class attributes and methods
CarRentalModel_VipCustomer_discount: Property = Property(name="discount", type=FloatType)
CarRentalModel_VipCustomer.attributes={CarRentalModel_VipCustomer_discount}

# Customer class attributes and methods

# CarRentalModel_Motorcycle class attributes and methods
CarRentalModel_Motorcycle_cm3: Property = Property(name="cm3", type=IntegerType)
CarRentalModel_Motorcycle.attributes={CarRentalModel_Motorcycle_cm3}

# Craft class attributes and methods

# CarRentalModel_Automobile class attributes and methods
CarRentalModel_Automobile_isCabrio: Property = Property(name="isCabrio", type=BooleanType)
CarRentalModel_Automobile.attributes={CarRentalModel_Automobile_isCabrio}

# Relationships
agencies1: BinaryAssociation = BinaryAssociation(
    name="agencies1",
    ends={
        Property(name="CarRentalModel_Agency", type=CarRentalModel_CarRental, multiplicity=Multiplicity(1, 1)),
        Property(name="CarRentalModel_CarRental2", type=CarRentalModel_Agency, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
crafts3: BinaryAssociation = BinaryAssociation(
    name="crafts3",
    ends={
        Property(name="CarRentalModel_Craft", type=CarRentalModel_CarRental, multiplicity=Multiplicity(1, 1)),
        Property(name="CarRentalModel_CarRental4", type=CarRentalModel_Craft, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
mainAgency5: BinaryAssociation = BinaryAssociation(
    name="mainAgency5",
    ends={
        Property(name="CarRentalModel_Agency7", type=CarRentalModel_CarRental, multiplicity=Multiplicity(1, 1)),
        Property(name="CarRentalModel_CarRental6", type=CarRentalModel_Agency, multiplicity=Multiplicity(1, 1))
    }
)
customer0: BinaryAssociation = BinaryAssociation(
    name="customer0",
    ends={
        Property(name="CarRentalModel_Customer", type=CarRentalModel_CarRental, multiplicity=Multiplicity(1, 1)),
        Property(name="CarRentalModel_CarRental", type=CarRentalModel_Customer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bestellungen8: BinaryAssociation = BinaryAssociation(
    name="bestellungen8",
    ends={
        Property(name="Order", type=CarRentalModel_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="customer", type=CarRentalModel_Order, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
craft9: BinaryAssociation = BinaryAssociation(
    name="craft9",
    ends={
        Property(name="Craft", type=CarRentalModel_Order, multiplicity=Multiplicity(1, 1)),
        Property(name="rentBy", type=CarRentalModel_Craft, multiplicity=Multiplicity(1, 1))
    }
)
customer10: BinaryAssociation = BinaryAssociation(
    name="customer10",
    ends={
        Property(name="Customer", type=CarRentalModel_Order, multiplicity=Multiplicity(1, 1)),
        Property(name="bestellungen", type=CarRentalModel_Customer, multiplicity=Multiplicity(1, 1))
    }
)
rentBy11: BinaryAssociation = BinaryAssociation(
    name="rentBy11",
    ends={
        Property(name="Order12", type=CarRentalModel_Craft, multiplicity=Multiplicity(1, 1)),
        Property(name="craft", type=CarRentalModel_Order, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_CarRentalModel_VipCustomer_Customer = Generalization(general=Customer, specific=CarRentalModel_VipCustomer)
gen_CarRentalModel_Motorcycle_Craft = Generalization(general=Craft, specific=CarRentalModel_Motorcycle)
gen_CarRentalModel_Automobile_Craft = Generalization(general=Craft, specific=CarRentalModel_Automobile)

# Domain Model
domain_model = DomainModel(
    name="CarRentalModel",
    types={CarRentalModel_Agency, CarRentalModel_Craft, CarRentalModel_CarRental, CarRentalModel_Customer, CarRentalModel_Order, CarRentalModel_VipCustomer, Customer, CarRentalModel_Motorcycle, Craft, CarRentalModel_Automobile},
    associations={agencies1, crafts3, mainAgency5, customer0, bestellungen8, craft9, customer10, rentBy11},
    generalizations={gen_CarRentalModel_VipCustomer_Customer, gen_CarRentalModel_Motorcycle_Craft, gen_CarRentalModel_Automobile_Craft},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)