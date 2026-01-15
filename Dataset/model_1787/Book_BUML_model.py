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
a_Model = Class(name="a::Model")
a_A = Class(name="a::A")
a_Book = Class(name="a::Book")

# a_Model class attributes and methods

# a_A class attributes and methods
a_A_name: Property = Property(name="name", type=StringType)
a_A.attributes={a_A_name}

# a_Book class attributes and methods
a_Book_title: Property = Property(name="title", type=StringType)
a_Book_author: Property = Property(name="author", type=StringType)
a_Book_published: Property = Property(name="published", type=StringType)
a_Book.attributes={a_Book_title, a_Book_published, a_Book_author}

# Relationships
a0: BinaryAssociation = BinaryAssociation(
    name="a0",
    ends={
        Property(name="a_A", type=a_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="a_Model", type=a_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
x1: BinaryAssociation = BinaryAssociation(
    name="x1",
    ends={
        Property(name="a_Book", type=a_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="a_Model2", type=a_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="a",
    types={a_Model, a_A, a_Book},
    associations={a0, x1},
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