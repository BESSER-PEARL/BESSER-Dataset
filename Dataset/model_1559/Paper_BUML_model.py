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
Paper_Papers = Class(name="Paper::Papers")
Paper_Paper = Class(name="Paper::Paper")
Paper_Author = Class(name="Paper::Author")

# Paper_Papers class attributes and methods

# Paper_Paper class attributes and methods
Paper_Paper_title: Property = Property(name="title", type=StringType)
Paper_Paper.attributes={Paper_Paper_title}

# Paper_Author class attributes and methods
Paper_Author_firstname: Property = Property(name="firstname", type=StringType)
Paper_Author_lastname: Property = Property(name="lastname", type=StringType)
Paper_Author_email: Property = Property(name="email", type=StringType)
Paper_Author.attributes={Paper_Author_email, Paper_Author_lastname, Paper_Author_firstname}

# Relationships
papers0: BinaryAssociation = BinaryAssociation(
    name="papers0",
    ends={
        Property(name="Paper_Paper", type=Paper_Papers, multiplicity=Multiplicity(1, 1)),
        Property(name="Paper_Papers", type=Paper_Paper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors1: BinaryAssociation = BinaryAssociation(
    name="authors1",
    ends={
        Property(name="Paper_Author", type=Paper_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="Paper_Paper2", type=Paper_Author, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Paper",
    types={Paper_Papers, Paper_Paper, Paper_Author},
    associations={papers0, authors1},
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