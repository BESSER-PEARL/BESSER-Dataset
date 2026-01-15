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
attroverridesecondarytable_Country = Class(name="attroverridesecondarytable::Country")
attroverridesecondarytable_Person = Class(name="attroverridesecondarytable::Person")
attroverridesecondarytable_Employee = Class(name="attroverridesecondarytable::Employee")
Person = Class(name="Person")
attroverridesecondarytable_NonEmployee = Class(name="attroverridesecondarytable::NonEmployee")
attroverridesecondarytable_Address = Class(name="attroverridesecondarytable::Address")

# attroverridesecondarytable_Country class attributes and methods
attroverridesecondarytable_Country_name: Property = Property(name="name", type=StringType)
attroverridesecondarytable_Country.attributes={attroverridesecondarytable_Country_name}

# attroverridesecondarytable_Person class attributes and methods
attroverridesecondarytable_Person_name: Property = Property(name="name", type=StringType)
attroverridesecondarytable_Person_age: Property = Property(name="age", type=IntegerType)
attroverridesecondarytable_Person.attributes={attroverridesecondarytable_Person_name, attroverridesecondarytable_Person_age}

# attroverridesecondarytable_Employee class attributes and methods
attroverridesecondarytable_Employee_employeeNumber: Property = Property(name="employeeNumber", type=StringType)
attroverridesecondarytable_Employee.attributes={attroverridesecondarytable_Employee_employeeNumber}

# Person class attributes and methods

# attroverridesecondarytable_NonEmployee class attributes and methods

# attroverridesecondarytable_Address class attributes and methods
attroverridesecondarytable_Address_city: Property = Property(name="city", type=StringType)
attroverridesecondarytable_Address_name: Property = Property(name="name", type=StringType)
attroverridesecondarytable_Address_street: Property = Property(name="street", type=StringType)
attroverridesecondarytable_Address.attributes={attroverridesecondarytable_Address_street, attroverridesecondarytable_Address_name, attroverridesecondarytable_Address_city}

# Relationships
country0: BinaryAssociation = BinaryAssociation(
    name="country0",
    ends={
        Property(name="attroverridesecondarytable_Country", type=attroverridesecondarytable_Address, multiplicity=Multiplicity(1, 1)),
        Property(name="attroverridesecondarytable_Address", type=attroverridesecondarytable_Country, multiplicity=Multiplicity(0, 1))
    }
)
address1: BinaryAssociation = BinaryAssociation(
    name="address1",
    ends={
        Property(name="attroverridesecondarytable_Address2", type=attroverridesecondarytable_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="attroverridesecondarytable_Employee", type=attroverridesecondarytable_Address, multiplicity=Multiplicity(0, 1))
    }
)
address3: BinaryAssociation = BinaryAssociation(
    name="address3",
    ends={
        Property(name="attroverridesecondarytable_Address4", type=attroverridesecondarytable_NonEmployee, multiplicity=Multiplicity(1, 1)),
        Property(name="attroverridesecondarytable_NonEmployee", type=attroverridesecondarytable_Address, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_attroverridesecondarytable_Employee_Person = Generalization(general=Person, specific=attroverridesecondarytable_Employee)
gen_attroverridesecondarytable_NonEmployee_Person = Generalization(general=Person, specific=attroverridesecondarytable_NonEmployee)

# Domain Model
domain_model = DomainModel(
    name="attroverridesecondarytable",
    types={attroverridesecondarytable_Country, attroverridesecondarytable_Person, attroverridesecondarytable_Employee, Person, attroverridesecondarytable_NonEmployee, attroverridesecondarytable_Address},
    associations={country0, address1, address3},
    generalizations={gen_attroverridesecondarytable_Employee_Person, gen_attroverridesecondarytable_NonEmployee_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)