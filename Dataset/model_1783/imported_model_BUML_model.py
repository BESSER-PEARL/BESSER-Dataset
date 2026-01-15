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
E: Enumeration = Enumeration(
    name="E",
    literals={
            EnumerationLiteral(name="A"),
			EnumerationLiteral(name="B"),
			EnumerationLiteral(name="C")
    }
)

# Classes
imported_model_Library = Class(name="imported::model::Library")
imported_model_Book = Class(name="imported::model::Book")

# imported_model_Library class attributes and methods

# imported_model_Book class attributes and methods
imported_model_Book_pages: Property = Property(name="pages", type=IntegerType)
imported_model_Book.attributes={imported_model_Book_pages}

# Relationships
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="imported_model_Book", type=imported_model_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="imported_model_Library", type=imported_model_Book, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="imported_model",
    types={imported_model_Library, imported_model_Book, E},
    associations={books0},
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