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
extralazy_Book = Class(name="extralazy::Book")
extralazy_Writer = Class(name="extralazy::Writer")

# extralazy_Book class attributes and methods
extralazy_Book_title: Property = Property(name="title", type=StringType)
extralazy_Book_subTitles: Property = Property(name="subTitles", type=StringType)
extralazy_Book.attributes={extralazy_Book_subTitles, extralazy_Book_title}

# extralazy_Writer class attributes and methods
extralazy_Writer_name: Property = Property(name="name", type=StringType)
extralazy_Writer.attributes={extralazy_Writer_name}

# Relationships
authors0: BinaryAssociation = BinaryAssociation(
    name="authors0",
    ends={
        Property(name="extralazy_Writer", type=extralazy_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="extralazy_Book", type=extralazy_Writer, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="extralazy",
    types={extralazy_Book, extralazy_Writer},
    associations={authors0},
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