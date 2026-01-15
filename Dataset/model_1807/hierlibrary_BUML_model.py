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
hierarchy_HierLibrary = Class(name="hierarchy::HierLibrary")
hierarchy_Fiction = Class(name="hierarchy::Fiction")
hierarchy_NonFiction = Class(name="hierarchy::NonFiction")
hierarchy_Book = Class(name="hierarchy::Book")

# hierarchy_HierLibrary class attributes and methods
hierarchy_HierLibrary_Name: Property = Property(name="Name", type=StringType)
hierarchy_HierLibrary.attributes={hierarchy_HierLibrary_Name}

# hierarchy_Fiction class attributes and methods
hierarchy_Fiction_Name: Property = Property(name="Name", type=StringType)
hierarchy_Fiction.attributes={hierarchy_Fiction_Name}

# hierarchy_NonFiction class attributes and methods
hierarchy_NonFiction_Name: Property = Property(name="Name", type=StringType)
hierarchy_NonFiction.attributes={hierarchy_NonFiction_Name}

# hierarchy_Book class attributes and methods
hierarchy_Book_Name: Property = Property(name="Name", type=StringType)
hierarchy_Book_genre: Property = Property(name="genre", type=StringType)
hierarchy_Book.attributes={hierarchy_Book_genre, hierarchy_Book_Name}

# Relationships
fiction0: BinaryAssociation = BinaryAssociation(
    name="fiction0",
    ends={
        Property(name="hierarchy_Fiction", type=hierarchy_HierLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="hierarchy_HierLibrary", type=hierarchy_Fiction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
members3: BinaryAssociation = BinaryAssociation(
    name="members3",
    ends={
        Property(name="hierarchy_Book", type=hierarchy_Fiction, multiplicity=Multiplicity(1, 1)),
        Property(name="hierarchy_Fiction4", type=hierarchy_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members5: BinaryAssociation = BinaryAssociation(
    name="members5",
    ends={
        Property(name="hierarchy_Book7", type=hierarchy_NonFiction, multiplicity=Multiplicity(1, 1)),
        Property(name="hierarchy_NonFiction6", type=hierarchy_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nonfiction1: BinaryAssociation = BinaryAssociation(
    name="nonfiction1",
    ends={
        Property(name="hierarchy_NonFiction", type=hierarchy_HierLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="hierarchy_HierLibrary2", type=hierarchy_NonFiction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="hierarchy",
    types={hierarchy_HierLibrary, hierarchy_Fiction, hierarchy_NonFiction, hierarchy_Book},
    associations={fiction0, members3, members5, nonfiction1},
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