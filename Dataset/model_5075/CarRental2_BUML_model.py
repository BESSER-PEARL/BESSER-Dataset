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
CarRental2_Person = Class(name="CarRental2::Person", is_abstract=True)
CarRental2_Customer = Class(name="CarRental2::Customer")
Person = Class(name="Person")
CarRental2_Rental = Class(name="CarRental2::Rental")
CarRental2_Employee = Class(name="CarRental2::Employee")
CarRental2_Branch = Class(name="CarRental2::Branch")
CarRental2_CarGroup = Class(name="CarRental2::CarGroup")
CarRental2_Car = Class(name="CarRental2::Car")
CarRental2_TernaryRelationMaintenance = Class(name="CarRental2::TernaryRelationMaintenance")
CarRental2_ServiceDepot = Class(name="CarRental2::ServiceDepot")
CarRental2_Check = Class(name="CarRental2::Check")

# CarRental2_Person class attributes and methods
CarRental2_Person_firstname: Property = Property(name="firstname", type=IntegerType)
CarRental2_Person_lastname: Property = Property(name="lastname", type=IntegerType)
CarRental2_Person_age: Property = Property(name="age", type=IntegerType)
CarRental2_Person_isMarried: Property = Property(name="isMarried", type=BooleanType)
CarRental2_Person_m_fullname: Method = Method(name="fullname", parameters={Parameter(name='prefix')}, type=StringType)
CarRental2_Person.attributes={CarRental2_Person_age, CarRental2_Person_lastname, CarRental2_Person_firstname, CarRental2_Person_isMarried}
CarRental2_Person.methods={CarRental2_Person_m_fullname}

# CarRental2_Customer class attributes and methods
CarRental2_Customer_address: Property = Property(name="address", type=IntegerType)
CarRental2_Customer.attributes={CarRental2_Customer_address}

# Person class attributes and methods

# CarRental2_Rental class attributes and methods
CarRental2_Rental_fromDate: Property = Property(name="fromDate", type=IntegerType)
CarRental2_Rental_untilDate: Property = Property(name="untilDate", type=IntegerType)
CarRental2_Rental.attributes={CarRental2_Rental_fromDate, CarRental2_Rental_untilDate}

# CarRental2_Employee class attributes and methods
CarRental2_Employee_salary: Property = Property(name="salary", type=IntegerType)
CarRental2_Employee_m_raiseSalary: Method = Method(name="raiseSalary", parameters={Parameter(name='amount')}, type=IntegerType)
CarRental2_Employee.attributes={CarRental2_Employee_salary}
CarRental2_Employee.methods={CarRental2_Employee_m_raiseSalary}

# CarRental2_Branch class attributes and methods
CarRental2_Branch_location: Property = Property(name="location", type=IntegerType)
CarRental2_Branch_m_rentalsForDate: Method = Method(name="rentalsForDate", parameters={})
CarRental2_Branch.attributes={CarRental2_Branch_location}
CarRental2_Branch.methods={CarRental2_Branch_m_rentalsForDate}

# CarRental2_CarGroup class attributes and methods
CarRental2_CarGroup_kind: Property = Property(name="kind", type=IntegerType)
CarRental2_CarGroup.attributes={CarRental2_CarGroup_kind}

# CarRental2_Car class attributes and methods
CarRental2_Car_id: Property = Property(name="id", type=IntegerType)
CarRental2_Car_m_description: Method = Method(name="description", parameters={}, type=StringType)
CarRental2_Car.attributes={CarRental2_Car_id}
CarRental2_Car.methods={CarRental2_Car_m_description}

# CarRental2_TernaryRelationMaintenance class attributes and methods

# CarRental2_ServiceDepot class attributes and methods
CarRental2_ServiceDepot_location: Property = Property(name="location", type=IntegerType)
CarRental2_ServiceDepot.attributes={CarRental2_ServiceDepot_location}

# CarRental2_Check class attributes and methods
CarRental2_Check_description: Property = Property(name="description", type=IntegerType)
CarRental2_Check.attributes={CarRental2_Check_description}

# Relationships
Booking_Rental0: BinaryAssociation = BinaryAssociation(
    name="Booking_Rental0",
    ends={
        Property(name="Rental", type=CarRental2_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="Booking_Customer", type=CarRental2_Rental, multiplicity=Multiplicity(0, 9999))
    }
)
Management_Branch_role_managedBranch1: BinaryAssociation = BinaryAssociation(
    name="Management_Branch_role_managedBranch1",
    ends={
        Property(name="Branch", type=CarRental2_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="Management_Employee_role_manager", type=CarRental2_Branch, multiplicity=Multiplicity(0, 1))
    }
)
Employment_Branch_role_employer2: BinaryAssociation = BinaryAssociation(
    name="Employment_Branch_role_employer2",
    ends={
        Property(name="Branch3", type=CarRental2_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="Employment_Employee_role_employee", type=CarRental2_Branch, multiplicity=Multiplicity(1, 1))
    }
)
Offers_CarGroup8: BinaryAssociation = BinaryAssociation(
    name="Offers_CarGroup8",
    ends={
        Property(name="CarGroup", type=CarRental2_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="Offers_Branch", type=CarRental2_CarGroup, multiplicity=Multiplicity(0, 9999))
    }
)
Provider_Rental9: BinaryAssociation = BinaryAssociation(
    name="Provider_Rental9",
    ends={
        Property(name="Rental10", type=CarRental2_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="Provider_Branch", type=CarRental2_Rental, multiplicity=Multiplicity(0, 9999))
    }
)
Booking_Customer11: BinaryAssociation = BinaryAssociation(
    name="Booking_Customer11",
    ends={
        Property(name="Customer", type=CarRental2_Rental, multiplicity=Multiplicity(1, 1)),
        Property(name="Booking_Rental", type=CarRental2_Customer, multiplicity=Multiplicity(1, 1))
    }
)
Provider_Branch12: BinaryAssociation = BinaryAssociation(
    name="Provider_Branch12",
    ends={
        Property(name="Branch13", type=CarRental2_Rental, multiplicity=Multiplicity(1, 1)),
        Property(name="Provider_Rental", type=CarRental2_Branch, multiplicity=Multiplicity(1, 1))
    }
)
Reservation_CarGroup14: BinaryAssociation = BinaryAssociation(
    name="Reservation_CarGroup14",
    ends={
        Property(name="CarGroup15", type=CarRental2_Rental, multiplicity=Multiplicity(1, 1)),
        Property(name="Reservation_Rental", type=CarRental2_CarGroup, multiplicity=Multiplicity(1, 1))
    }
)
Assignment_Car16: BinaryAssociation = BinaryAssociation(
    name="Assignment_Car16",
    ends={
        Property(name="Car17", type=CarRental2_Rental, multiplicity=Multiplicity(1, 1)),
        Property(name="Assignment_Rental", type=CarRental2_Car, multiplicity=Multiplicity(0, 1))
    }
)
Offers_Branch18: BinaryAssociation = BinaryAssociation(
    name="Offers_Branch18",
    ends={
        Property(name="Branch19", type=CarRental2_CarGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="Offers_CarGroup", type=CarRental2_Branch, multiplicity=Multiplicity(0, 9999))
    }
)
Classification_Car20: BinaryAssociation = BinaryAssociation(
    name="Classification_Car20",
    ends={
        Property(name="Car21", type=CarRental2_CarGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="Classification_CarGroup", type=CarRental2_Car, multiplicity=Multiplicity(0, 9999))
    }
)
Reservation_Rental22: BinaryAssociation = BinaryAssociation(
    name="Reservation_Rental22",
    ends={
        Property(name="Rental23", type=CarRental2_CarGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="Reservation_CarGroup", type=CarRental2_Rental, multiplicity=Multiplicity(0, 9999))
    }
)
Quality_CarGroup_role_lower25: BinaryAssociation = BinaryAssociation(
    name="Quality_CarGroup_role_lower25",
    ends={
        Property(name="CarGroup26", type=CarRental2_CarGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="Quality_CarGroup_role_higher", type=CarRental2_CarGroup, multiplicity=Multiplicity(0, 1))
    }
)
Quality_CarGroup_role_higher28: BinaryAssociation = BinaryAssociation(
    name="Quality_CarGroup_role_higher28",
    ends={
        Property(name="CarGroup29", type=CarRental2_CarGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="Quality_CarGroup_role_lower", type=CarRental2_CarGroup, multiplicity=Multiplicity(0, 1))
    }
)
Management_Employee_role_manager4: BinaryAssociation = BinaryAssociation(
    name="Management_Employee_role_manager4",
    ends={
        Property(name="Employee", type=CarRental2_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="Management_Branch_role_managedBranch", type=CarRental2_Employee, multiplicity=Multiplicity(1, 1))
    }
)
Employment_Employee_role_employee5: BinaryAssociation = BinaryAssociation(
    name="Employment_Employee_role_employee5",
    ends={
        Property(name="Employee6", type=CarRental2_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="Employment_Branch_role_employer", type=CarRental2_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
Fleet_Car7: BinaryAssociation = BinaryAssociation(
    name="Fleet_Car7",
    ends={
        Property(name="Car", type=CarRental2_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="Fleet_Branch", type=CarRental2_Car, multiplicity=Multiplicity(0, 9999))
    }
)
Assignment_Rental34: BinaryAssociation = BinaryAssociation(
    name="Assignment_Rental34",
    ends={
        Property(name="Assignment_Car", type=CarRental2_Rental, multiplicity=Multiplicity(0, 1)),
        Property(name="Rental35", type=CarRental2_Car, multiplicity=Multiplicity(1, 1))
    }
)
toMaintenance36: BinaryAssociation = BinaryAssociation(
    name="toMaintenance36",
    ends={
        Property(name="TernaryRelationMaintenance", type=CarRental2_Car, multiplicity=Multiplicity(1, 1)),
        Property(name="toCar", type=CarRental2_TernaryRelationMaintenance, multiplicity=Multiplicity(0, 9999))
    }
)
toMaintenance37: BinaryAssociation = BinaryAssociation(
    name="toMaintenance37",
    ends={
        Property(name="TernaryRelationMaintenance38", type=CarRental2_ServiceDepot, multiplicity=Multiplicity(1, 1)),
        Property(name="toServiceDepot", type=CarRental2_TernaryRelationMaintenance, multiplicity=Multiplicity(0, 9999))
    }
)
toMaintenance39: BinaryAssociation = BinaryAssociation(
    name="toMaintenance39",
    ends={
        Property(name="TernaryRelationMaintenance40", type=CarRental2_Check, multiplicity=Multiplicity(1, 1)),
        Property(name="toCheck", type=CarRental2_TernaryRelationMaintenance, multiplicity=Multiplicity(0, 9999))
    }
)
toServiceDepot41: BinaryAssociation = BinaryAssociation(
    name="toServiceDepot41",
    ends={
        Property(name="ServiceDepot", type=CarRental2_TernaryRelationMaintenance, multiplicity=Multiplicity(1, 1)),
        Property(name="toMaintenance", type=CarRental2_ServiceDepot, multiplicity=Multiplicity(1, 1))
    }
)
toCheck42: BinaryAssociation = BinaryAssociation(
    name="toCheck42",
    ends={
        Property(name="Check", type=CarRental2_TernaryRelationMaintenance, multiplicity=Multiplicity(1, 1)),
        Property(name="toMaintenance43", type=CarRental2_Check, multiplicity=Multiplicity(1, 1))
    }
)
toCar44: BinaryAssociation = BinaryAssociation(
    name="toCar44",
    ends={
        Property(name="Car46", type=CarRental2_TernaryRelationMaintenance, multiplicity=Multiplicity(1, 1)),
        Property(name="toMaintenance45", type=CarRental2_Car, multiplicity=Multiplicity(1, 1))
    }
)
Fleet_Branch30: BinaryAssociation = BinaryAssociation(
    name="Fleet_Branch30",
    ends={
        Property(name="Branch31", type=CarRental2_Car, multiplicity=Multiplicity(1, 1)),
        Property(name="Fleet_Car", type=CarRental2_Branch, multiplicity=Multiplicity(1, 1))
    }
)
Classification_CarGroup32: BinaryAssociation = BinaryAssociation(
    name="Classification_CarGroup32",
    ends={
        Property(name="CarGroup33", type=CarRental2_Car, multiplicity=Multiplicity(1, 1)),
        Property(name="Classification_Car", type=CarRental2_CarGroup, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_CarRental2_Customer_Person = Generalization(general=Person, specific=CarRental2_Customer)
gen_CarRental2_Employee_Person = Generalization(general=Person, specific=CarRental2_Employee)

# Domain Model
domain_model = DomainModel(
    name="CarRental2",
    types={CarRental2_Person, CarRental2_Customer, Person, CarRental2_Rental, CarRental2_Employee, CarRental2_Branch, CarRental2_CarGroup, CarRental2_Car, CarRental2_TernaryRelationMaintenance, CarRental2_ServiceDepot, CarRental2_Check},
    associations={Booking_Rental0, Management_Branch_role_managedBranch1, Employment_Branch_role_employer2, Offers_CarGroup8, Provider_Rental9, Booking_Customer11, Provider_Branch12, Reservation_CarGroup14, Assignment_Car16, Offers_Branch18, Classification_Car20, Reservation_Rental22, Quality_CarGroup_role_lower25, Quality_CarGroup_role_higher28, Management_Employee_role_manager4, Employment_Employee_role_employee5, Fleet_Car7, Assignment_Rental34, toMaintenance36, toMaintenance37, toMaintenance39, toServiceDepot41, toCheck42, toCar44, Fleet_Branch30, Classification_CarGroup32},
    generalizations={gen_CarRental2_Customer_Person, gen_CarRental2_Employee_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)