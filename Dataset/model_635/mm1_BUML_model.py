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
mm1_Library = Class(name="mm1::Library")
mm1_Member = Class(name="mm1::Member")
mm1_Book = Class(name="mm1::Book")

# mm1_Library class attributes and methods
mm1_Library_name: Property = Property(name="name", type=StringType)
mm1_Library.attributes={mm1_Library_name}

# mm1_Member class attributes and methods
mm1_Member_name: Property = Property(name="name", type=StringType)
mm1_Member.attributes={mm1_Member_name}

# mm1_Book class attributes and methods
mm1_Book_name: Property = Property(name="name", type=StringType)
mm1_Book.attributes={mm1_Book_name}

# Relationships
loans3: BinaryAssociation = BinaryAssociation(
    name="loans3",
    ends={
        Property(name="mm1_Book5", type=mm1_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="mm1_Member4", type=mm1_Book, multiplicity=Multiplicity(0, 9999))
    }
)
members0: BinaryAssociation = BinaryAssociation(
    name="members0",
    ends={
        Property(name="mm1_Member", type=mm1_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="mm1_Library", type=mm1_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books1: BinaryAssociation = BinaryAssociation(
    name="books1",
    ends={
        Property(name="mm1_Book", type=mm1_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="mm1_Library2", type=mm1_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="mm1",
    types={mm1_Library, mm1_Member, mm1_Book},
    associations={loans3, members0, books1},
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