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
project_Person = Class(name="project::Person")
project_CommitterShip = Class(name="project::CommitterShip")
project_Foundation = Class(name="project::Foundation")
project_Project = Class(name="project::Project")

# project_Person class attributes and methods
project_Person_lastname: Property = Property(name="lastname", type=StringType)
project_Person_firstname: Property = Property(name="firstname", type=StringType)
project_Person_email: Property = Property(name="email", type=StringType)
project_Person_image: Property = Property(name="image", type=StringType)
project_Person.attributes={project_Person_firstname, project_Person_lastname, project_Person_image, project_Person_email}

# project_CommitterShip class attributes and methods
project_CommitterShip_start: Property = Property(name="start", type=DateType)
project_CommitterShip_end: Property = Property(name="end", type=DateType)
project_CommitterShip.attributes={project_CommitterShip_start, project_CommitterShip_end}

# project_Foundation class attributes and methods

# project_Project class attributes and methods
project_Project_shortname: Property = Property(name="shortname", type=StringType)
project_Project_longname: Property = Property(name="longname", type=StringType)
project_Project_devmail: Property = Property(name="devmail", type=StringType)
project_Project_homepage: Property = Property(name="homepage", type=StringType)
project_Project_start: Property = Property(name="start", type=DateType)
project_Project_end: Property = Property(name="end", type=DateType)
project_Project.attributes={project_Project_start, project_Project_longname, project_Project_devmail, project_Project_end, project_Project_homepage, project_Project_shortname}

# Relationships
projects0: BinaryAssociation = BinaryAssociation(
    name="projects0",
    ends={
        Property(name="project_Project", type=project_Foundation, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Foundation", type=project_Project, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
persons1: BinaryAssociation = BinaryAssociation(
    name="persons1",
    ends={
        Property(name="project_Person", type=project_Foundation, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Foundation2", type=project_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subprojects4: BinaryAssociation = BinaryAssociation(
    name="subprojects4",
    ends={
        Property(name="Project", type=project_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=project_Project, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
project12: BinaryAssociation = BinaryAssociation(
    name="project12",
    ends={
        Property(name="Project13", type=project_CommitterShip, multiplicity=Multiplicity(1, 1)),
        Property(name="committers", type=project_Project, multiplicity=Multiplicity(0, 1))
    }
)
person14: BinaryAssociation = BinaryAssociation(
    name="person14",
    ends={
        Property(name="Person", type=project_CommitterShip, multiplicity=Multiplicity(1, 1)),
        Property(name="committerships", type=project_Person, multiplicity=Multiplicity(0, 1))
    }
)
committers5: BinaryAssociation = BinaryAssociation(
    name="committers5",
    ends={
        Property(name="CommitterShip", type=project_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="project", type=project_CommitterShip, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent7: BinaryAssociation = BinaryAssociation(
    name="parent7",
    ends={
        Property(name="Project8", type=project_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="subprojects", type=project_Project, multiplicity=Multiplicity(0, 1))
    }
)
projectleads9: BinaryAssociation = BinaryAssociation(
    name="projectleads9",
    ends={
        Property(name="project_Person11", type=project_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="project_Project10", type=project_Person, multiplicity=Multiplicity(0, 9999))
    }
)
committerships15: BinaryAssociation = BinaryAssociation(
    name="committerships15",
    ends={
        Property(name="CommitterShip16", type=project_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="person", type=project_CommitterShip, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="project",
    types={project_Person, project_CommitterShip, project_Foundation, project_Project},
    associations={projects0, persons1, subprojects4, project12, person14, committers5, parent7, projectleads9, committerships15},
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