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
Publication_Publication = Class(name="Publication_Publication")

# Publication_Publication class attributes and methods
Publication_Publication_title: Property = Property(name="title", type=StringType)
Publication_Publication_authors: Property = Property(name="authors", type=StringType)
Publication_Publication_nbPages: Property = Property(name="nbPages", type=StringType)
Publication_Publication.attributes={Publication_Publication_title, Publication_Publication_authors, Publication_Publication_nbPages}

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={Publication_Publication},
    associations={},
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