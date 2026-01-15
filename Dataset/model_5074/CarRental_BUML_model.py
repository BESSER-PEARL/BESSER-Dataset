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
CarGroupKind: Enumeration = Enumeration(
    name="CarGroupKind",
    literals={
            EnumerationLiteral(name="compact"),
			EnumerationLiteral(name="intermediate"),
			EnumerationLiteral(name="luxury")
    }
)

# Classes
CarRental_Person = Class(name="CarRental::Person")
CarRental_Customer = Class(name="CarRental::Customer")
Person = Class(name="Person")
CarRental_Rental = Class(name="CarRental::Rental")
CarRental_Employee = Class(name="CarRental::Employee")
CarRental_Branch = Class(name="CarRental::Branch")
CarRental_Car = Class(name="CarRental::Car")
CarRental_CarGroup = Class(name="CarRental::CarGroup")
CarRental_ServiceDepot = Class(name="CarRental::ServiceDepot")
CarRental_Check = Class(name="CarRental::Check")

# CarRental_Person class attributes and methods
CarRental_Person_firstname: Property = Property(name="firstname", type=StringType)
CarRental_Person_lastname: Property = Property(name="lastname", type=StringType)
CarRental_Person_age: Property = Property(name="age", type=IntegerType)
CarRental_Person_isMarried: Property = Property(name="isMarried", type=BooleanType)
CarRental_Person_m_email: Method = Method(name="email", parameters={}, type=StringType)
CarRental_Person_m_updateAge: Method = Method(name="updateAge", parameters={Parameter(name='newAge')})
CarRental_Person.attributes={CarRental_Person_isMarried, CarRental_Person_lastname, CarRental_Person_age, CarRental_Person_firstname}
CarRental_Person.methods={CarRental_Person_m_updateAge, CarRental_Person_m_email}

# CarRental_Customer class attributes and methods
CarRental_Customer_address: Property = Property(name="address", type=StringType)
CarRental_Customer.attributes={CarRental_Customer_address}

# Person class attributes and methods

# CarRental_Rental class attributes and methods
CarRental_Rental_untilDate: Property = Property(name="untilDate", type=StringType)
CarRental_Rental_framDate: Property = Property(name="framDate", type=StringType)
CarRental_Rental.attributes={CarRental_Rental_framDate, CarRental_Rental_untilDate}

# CarRental_Employee class attributes and methods
CarRental_Employee_salary: Property = Property(name="salary", type=FloatType)
CarRental_Employee_m_raiseSalary: Method = Method(name="raiseSalary", parameters={Parameter(name='amount')}, type=FloatType)
CarRental_Employee.attributes={CarRental_Employee_salary}
CarRental_Employee.methods={CarRental_Employee_m_raiseSalary}

# CarRental_Branch class attributes and methods
CarRental_Branch_location: Property = Property(name="location", type=StringType)
CarRental_Branch.attributes={CarRental_Branch_location}

# CarRental_Car class attributes and methods
CarRental_Car_id: Property = Property(name="id", type=StringType)
CarRental_Car.attributes={CarRental_Car_id}

# CarRental_CarGroup class attributes and methods
CarRental_CarGroup_kind: Property = Property(name="kind", type=StringType)
CarRental_CarGroup.attributes={CarRental_CarGroup_kind}

# CarRental_ServiceDepot class attributes and methods
CarRental_ServiceDepot_location: Property = Property(name="location", type=StringType)
CarRental_ServiceDepot.attributes={CarRental_ServiceDepot_location}

# CarRental_Check class attributes and methods
CarRental_Check_description: Property = Property(name="description", type=StringType)
CarRental_Check.attributes={CarRental_Check_description}

# Relationships
rental0: BinaryAssociation = BinaryAssociation(
    name="rental0",
    ends={
        Property(name="Rental", type=CarRental_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="customer", type=CarRental_Rental, multiplicity=Multiplicity(0, 9999))
    }
)
managedBranch1: BinaryAssociation = BinaryAssociation(
    name="managedBranch1",
    ends={
        Property(name="CarRental_Branch", type=CarRental_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="CarRental_Employee", type=CarRental_Branch, multiplicity=Multiplicity(0, 1))
    }
)
employer2: BinaryAssociation = BinaryAssociation(
    name="employer2",
    ends={
        Property(name="CarRental_Branch4", type=CarRental_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="CarRental_Employee3", type=CarRental_Branch, multiplicity=Multiplicity(1, 1))
    }
)
manager5: BinaryAssociation = BinaryAssociation(
    name="manager5",
    ends={
        Property(name="CarRental_Employee7", type=CarRental_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="CarRental_Branch6", type=CarRental_Employee, multiplicity=Multiplicity(1, 1))
    }
)
employee8: BinaryAssociation = BinaryAssociation(
    name="employee8",
    ends={
        Property(name="CarRental_Employee10", type=CarRental_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="CarRental_Branch9", type=CarRental_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
car11: BinaryAssociation = BinaryAssociation(
    name="car11",
    ends={
        Property(name="Car", type=CarRental_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="branch", type=CarRental_Car, multiplicity=Multiplicity(0, 9999))
    }
)
carGroup12: BinaryAssociation = BinaryAssociation(
    name="carGroup12",
    ends={
        Property(name="CarGroup", type=CarRental_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="branch13", type=CarRental_CarGroup, multiplicity=Multiplicity(0, 9999))
    }
)
rental14: BinaryAssociation = BinaryAssociation(
    name="rental14",
    ends={
        Property(name="Rental16", type=CarRental_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="branch15", type=CarRental_Rental, multiplicity=Multiplicity(0, 9999))
    }
)
car17: BinaryAssociation = BinaryAssociation(
    name="car17",
    ends={
        Property(name="Car18", type=CarRental_Rental, multiplicity=Multiplicity(1, 1)),
        Property(name="rental", type=CarRental_Car, multiplicity=Multiplicity(0, 1))
    }
)
customer19: BinaryAssociation = BinaryAssociation(
    name="customer19",
    ends={
        Property(name="Customer", type=CarRental_Rental, multiplicity=Multiplicity(1, 1)),
        Property(name="rental20", type=CarRental_Customer, multiplicity=Multiplicity(1, 1))
    }
)
branch21: BinaryAssociation = BinaryAssociation(
    name="branch21",
    ends={
        Property(name="Branch", type=CarRental_Rental, multiplicity=Multiplicity(1, 1)),
        Property(name="rental22", type=CarRental_Branch, multiplicity=Multiplicity(1, 1))
    }
)
carGroup23: BinaryAssociation = BinaryAssociation(
    name="carGroup23",
    ends={
        Property(name="CarGroup25", type=CarRental_Rental, multiplicity=Multiplicity(1, 1)),
        Property(name="rental24", type=CarRental_CarGroup, multiplicity=Multiplicity(1, 1))
    }
)
branch26: BinaryAssociation = BinaryAssociation(
    name="branch26",
    ends={
        Property(name="Branch27", type=CarRental_CarGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="carGroup", type=CarRental_Branch, multiplicity=Multiplicity(0, 9999))
    }
)
car28: BinaryAssociation = BinaryAssociation(
    name="car28",
    ends={
        Property(name="Car30", type=CarRental_CarGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="carGroup29", type=CarRental_Car, multiplicity=Multiplicity(0, 9999))
    }
)
rental31: BinaryAssociation = BinaryAssociation(
    name="rental31",
    ends={
        Property(name="Rental33", type=CarRental_CarGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="carGroup32", type=CarRental_Rental, multiplicity=Multiplicity(0, 9999))
    }
)
higher35: BinaryAssociation = BinaryAssociation(
    name="higher35",
    ends={
        Property(name="CarGroup36", type=CarRental_CarGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="lower", type=CarRental_CarGroup, multiplicity=Multiplicity(0, 1))
    }
)
lower38: BinaryAssociation = BinaryAssociation(
    name="lower38",
    ends={
        Property(name="CarGroup39", type=CarRental_CarGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="higher", type=CarRental_CarGroup, multiplicity=Multiplicity(0, 1))
    }
)
branch40: BinaryAssociation = BinaryAssociation(
    name="branch40",
    ends={
        Property(name="Branch41", type=CarRental_Car, multiplicity=Multiplicity(1, 1)),
        Property(name="car", type=CarRental_Branch, multiplicity=Multiplicity(1, 1))
    }
)
carGroup42: BinaryAssociation = BinaryAssociation(
    name="carGroup42",
    ends={
        Property(name="CarGroup44", type=CarRental_Car, multiplicity=Multiplicity(1, 1)),
        Property(name="car43", type=CarRental_CarGroup, multiplicity=Multiplicity(1, 1))
    }
)
rental45: BinaryAssociation = BinaryAssociation(
    name="rental45",
    ends={
        Property(name="Rental47", type=CarRental_Car, multiplicity=Multiplicity(1, 1)),
        Property(name="car46", type=CarRental_Rental, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_CarRental_Customer_Person = Generalization(general=Person, specific=CarRental_Customer)
gen_CarRental_Employee_Person = Generalization(general=Person, specific=CarRental_Employee)

# Domain Model
domain_model = DomainModel(
    name="CarRental",
    types={CarRental_Person, CarRental_Customer, Person, CarRental_Rental, CarRental_Employee, CarRental_Branch, CarRental_Car, CarRental_CarGroup, CarRental_ServiceDepot, CarRental_Check, CarGroupKind},
    associations={rental0, managedBranch1, employer2, manager5, employee8, car11, carGroup12, rental14, car17, customer19, branch21, carGroup23, branch26, car28, rental31, higher35, lower38, branch40, carGroup42, rental45},
    generalizations={gen_CarRental_Customer_Person, gen_CarRental_Employee_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)