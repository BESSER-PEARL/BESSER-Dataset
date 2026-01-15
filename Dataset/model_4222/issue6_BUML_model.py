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
organization_Employee = Class(name="organization::Employee")
ABase = Class(name="ABase")
organization_Company = Class(name="organization::Company")
organization_Department = Class(name="organization::Department")
organization_ABase = Class(name="organization::ABase", is_abstract=True)
organization_core_Cass = Class(name="organization::core::Cass")

# organization_Employee class attributes and methods
organization_Employee_name: Property = Property(name="name", type=StringType)
organization_Employee.attributes={organization_Employee_name}

# ABase class attributes and methods

# organization_Company class attributes and methods
organization_Company_name: Property = Property(name="name", type=StringType)
organization_Company.attributes={organization_Company_name}

# organization_Department class attributes and methods
organization_Department_number: Property = Property(name="number", type=IntegerType)
organization_Department.attributes={organization_Department_number}

# organization_ABase class attributes and methods
organization_ABase_id: Property = Property(name="id", type=StringType)
organization_ABase.attributes={organization_ABase_id}

# organization_core_Cass class attributes and methods

# Relationships
department0: BinaryAssociation = BinaryAssociation(
    name="department0",
    ends={
        Property(name="organization_Department", type=organization_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="organization_Company", type=organization_Department, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
employees1: BinaryAssociation = BinaryAssociation(
    name="employees1",
    ends={
        Property(name="organization_Employee", type=organization_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="organization_Department2", type=organization_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_organization_Employee_ABase = Generalization(general=ABase, specific=organization_Employee)
gen_organization_Company_ABase = Generalization(general=ABase, specific=organization_Company)
gen_organization_Department_ABase = Generalization(general=ABase, specific=organization_Department)

# Domain Model
domain_model = DomainModel(
    name="organization",
    types={organization_Employee, ABase, organization_Company, organization_Department, organization_ABase, organization_core_Cass},
    associations={department0, employees1},
    generalizations={gen_organization_Employee_ABase, gen_organization_Company_ABase, gen_organization_Department_ABase},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)