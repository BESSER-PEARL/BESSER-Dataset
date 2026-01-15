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
office_OfficeModel = Class(name="office::OfficeModel")
NamedElement = Class(name="NamedElement")
office_OfficeElement = Class(name="office::OfficeElement", is_abstract=True)
office_Employee = Class(name="office::Employee")
OfficeElement = Class(name="OfficeElement")
office_Office = Class(name="office::Office")
office_NamedElement = Class(name="office::NamedElement", is_abstract=True)

# office_OfficeModel class attributes and methods

# NamedElement class attributes and methods

# office_OfficeElement class attributes and methods

# office_Employee class attributes and methods
office_Employee_title: Property = Property(name="title", type=StringType)
office_Employee.attributes={office_Employee_title}

# OfficeElement class attributes and methods

# office_Office class attributes and methods

# office_NamedElement class attributes and methods
office_NamedElement_name: Property = Property(name="name", type=StringType)
office_NamedElement.attributes={office_NamedElement_name}

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="office_OfficeElement", type=office_OfficeModel, multiplicity=Multiplicity(1, 1)),
        Property(name="office_OfficeModel", type=office_OfficeElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
worksIn1: BinaryAssociation = BinaryAssociation(
    name="worksIn1",
    ends={
        Property(name="Office", type=office_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employees", type=office_Office, multiplicity=Multiplicity(1, 1))
    }
)
worksWith3: BinaryAssociation = BinaryAssociation(
    name="worksWith3",
    ends={
        Property(name="office_Employee", type=office_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="office_Employee2", type=office_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
employees4: BinaryAssociation = BinaryAssociation(
    name="employees4",
    ends={
        Property(name="Employee", type=office_Office, multiplicity=Multiplicity(1, 1)),
        Property(name="worksIn", type=office_Employee, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_office_OfficeModel_NamedElement = Generalization(general=NamedElement, specific=office_OfficeModel)
gen_office_Employee_OfficeElement = Generalization(general=OfficeElement, specific=office_Employee)
gen_office_Office_OfficeElement = Generalization(general=OfficeElement, specific=office_Office)
gen_office_OfficeElement_NamedElement = Generalization(general=NamedElement, specific=office_OfficeElement)

# Domain Model
domain_model = DomainModel(
    name="office",
    types={office_OfficeModel, NamedElement, office_OfficeElement, office_Employee, OfficeElement, office_Office, office_NamedElement},
    associations={elements0, worksIn1, worksWith3, employees4},
    generalizations={gen_office_OfficeModel_NamedElement, gen_office_Employee_OfficeElement, gen_office_Office_OfficeElement, gen_office_OfficeElement_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)