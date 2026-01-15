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
writers_Catalog = Class(name="writers::Catalog")
writers_Writer = Class(name="writers::Writer")
writers_Book = Class(name="writers::Book")

# writers_Catalog class attributes and methods

# writers_Writer class attributes and methods
writers_Writer_name: Property = Property(name="name", type=StringType)
writers_Writer.attributes={writers_Writer_name}

# writers_Book class attributes and methods

# Relationships
writers0: BinaryAssociation = BinaryAssociation(
    name="writers0",
    ends={
        Property(name="writers_Writer", type=writers_Catalog, multiplicity=Multiplicity(1, 1)),
        Property(name="writers_Catalog", type=writers_Writer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books1: BinaryAssociation = BinaryAssociation(
    name="books1",
    ends={
        Property(name="books.ecoreBook", type=writers_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=writers_Book, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="writers",
    types={writers_Catalog, writers_Writer, writers_Book},
    associations={writers0, books1},
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