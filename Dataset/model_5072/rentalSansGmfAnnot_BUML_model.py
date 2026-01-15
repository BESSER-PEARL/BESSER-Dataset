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
StreetType: Enumeration = Enumeration(
    name="StreetType",
    literals={
            EnumerationLiteral(name="Street"),
			EnumerationLiteral(name="Road")
    }
)

# Classes
rental_RentalAgency = Class(name="rental::RentalAgency")
rental_RentalObject = Class(name="rental::RentalObject")
rental_Customer = Class(name="rental::Customer")
rental_Rental = Class(name="rental::Rental")

# rental_RentalAgency class attributes and methods
rental_RentalAgency_name: Property = Property(name="name", type=StringType)
rental_RentalAgency_m_book: Method = Method(name="book", parameters={Parameter(name='to'), Parameter(name='customer'), Parameter(name='from'), Parameter(name='rentedObject')}, type=StringType)
rental_RentalAgency_m_addCustomer: Method = Method(name="addCustomer", parameters={Parameter(name='customer')})
rental_RentalAgency_m_addObject: Method = Method(name="addObject", parameters={Parameter(name='object')})
rental_RentalAgency_m_removeCustomer: Method = Method(name="removeCustomer", parameters={Parameter(name='customer')})
rental_RentalAgency_m_removeObject: Method = Method(name="removeObject", parameters={Parameter(name='object')})
rental_RentalAgency_m_isAvailable: Method = Method(name="isAvailable", parameters={Parameter(name='from'), Parameter(name='rentedObject'), Parameter(name='to')}, type=BooleanType)
rental_RentalAgency.attributes={rental_RentalAgency_name}
rental_RentalAgency.methods={rental_RentalAgency_m_removeObject, rental_RentalAgency_m_removeCustomer, rental_RentalAgency_m_addCustomer, rental_RentalAgency_m_addObject, rental_RentalAgency_m_isAvailable, rental_RentalAgency_m_book}

# rental_RentalObject class attributes and methods
rental_RentalObject_ID: Property = Property(name="ID", type=StringType)
rental_RentalObject_name: Property = Property(name="name", type=StringType)
rental_RentalObject_picture: Property = Property(name="picture", type=StringType)
rental_RentalObject_m_rent: Method = Method(name="rent", parameters={Parameter(name='customer')}, type=StringType)
rental_RentalObject.attributes={rental_RentalObject_picture, rental_RentalObject_name, rental_RentalObject_ID}
rental_RentalObject.methods={rental_RentalObject_m_rent}

# rental_Customer class attributes and methods
rental_Customer_firstName: Property = Property(name="firstName", type=StringType)
rental_Customer_lastName: Property = Property(name="lastName", type=StringType)
rental_Customer_m_getDisplayName: Method = Method(name="getDisplayName", parameters={}, type=StringType)
rental_Customer.attributes={rental_Customer_firstName, rental_Customer_lastName}
rental_Customer.methods={rental_Customer_m_getDisplayName}

# rental_Rental class attributes and methods
rental_Rental_startDate: Property = Property(name="startDate", type=DateType)
rental_Rental_endDate: Property = Property(name="endDate", type=DateType)
rental_Rental_m_nbDaysBooked: Method = Method(name="nbDaysBooked", parameters={}, type=IntegerType)
rental_Rental.attributes={rental_Rental_endDate, rental_Rental_startDate}
rental_Rental.methods={rental_Rental_m_nbDaysBooked}

# Relationships
objectsToRent0: BinaryAssociation = BinaryAssociation(
    name="objectsToRent0",
    ends={
        Property(name="RentalObject", type=rental_RentalAgency, multiplicity=Multiplicity(1, 1)),
        Property(name="parentAgency", type=rental_RentalObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
customers1: BinaryAssociation = BinaryAssociation(
    name="customers1",
    ends={
        Property(name="Customer", type=rental_RentalAgency, multiplicity=Multiplicity(1, 1)),
        Property(name="parentAgency2", type=rental_Customer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rentals3: BinaryAssociation = BinaryAssociation(
    name="rentals3",
    ends={
        Property(name="Rental", type=rental_RentalAgency, multiplicity=Multiplicity(1, 1)),
        Property(name="parentAgency4", type=rental_Rental, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentAgency5: BinaryAssociation = BinaryAssociation(
    name="parentAgency5",
    ends={
        Property(name="RentalAgency", type=rental_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="customers", type=rental_RentalAgency, multiplicity=Multiplicity(1, 1))
    }
)
parentAgency6: BinaryAssociation = BinaryAssociation(
    name="parentAgency6",
    ends={
        Property(name="RentalAgency7", type=rental_RentalObject, multiplicity=Multiplicity(1, 1)),
        Property(name="objectsToRent", type=rental_RentalAgency, multiplicity=Multiplicity(1, 1))
    }
)
customer8: BinaryAssociation = BinaryAssociation(
    name="customer8",
    ends={
        Property(name="rental_Customer", type=rental_Rental, multiplicity=Multiplicity(1, 1)),
        Property(name="rental_Rental", type=rental_Customer, multiplicity=Multiplicity(1, 1))
    }
)
rentedObject9: BinaryAssociation = BinaryAssociation(
    name="rentedObject9",
    ends={
        Property(name="rental_RentalObject", type=rental_Rental, multiplicity=Multiplicity(1, 1)),
        Property(name="rental_Rental10", type=rental_RentalObject, multiplicity=Multiplicity(0, 1))
    }
)
parentAgency11: BinaryAssociation = BinaryAssociation(
    name="parentAgency11",
    ends={
        Property(name="RentalAgency12", type=rental_Rental, multiplicity=Multiplicity(1, 1)),
        Property(name="rentals", type=rental_RentalAgency, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="rental",
    types={rental_RentalAgency, rental_RentalObject, rental_Customer, rental_Rental, StreetType},
    associations={objectsToRent0, customers1, rentals3, parentAgency5, parentAgency6, customer8, rentedObject9, parentAgency11},
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