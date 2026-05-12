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
Bibtex_LiteratureDb = Class(name="Bibtex_LiteratureDb")
Bibtex_Author = Class(name="Bibtex_Author")
Bibtex_Entry = Class(name="Bibtex_Entry")

# Bibtex_LiteratureDb class attributes and methods
Bibtex_LiteratureDb_name: Property = Property(name="name", type=StringType)
Bibtex_LiteratureDb.attributes={Bibtex_LiteratureDb_name}

# Bibtex_Author class attributes and methods
Bibtex_Author_name: Property = Property(name="name", type=StringType)
Bibtex_Author.attributes={Bibtex_Author_name}

# Bibtex_Entry class attributes and methods
Bibtex_Entry_title: Property = Property(name="title", type=StringType)
Bibtex_Entry_id: Property = Property(name="id", type=StringType)
Bibtex_Entry.attributes={Bibtex_Entry_id, Bibtex_Entry_title}

# Relationships
entries1: BinaryAssociation = BinaryAssociation(
    name="entries1",
    ends={
        Property(name="Entry", type=Bibtex_LiteratureDb, multiplicity=Multiplicity(1, 1)),
        Property(name="literaturedb2", type=Bibtex_Entry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
author3: BinaryAssociation = BinaryAssociation(
    name="author3",
    ends={
        Property(name="Author4", type=Bibtex_Entry, multiplicity=Multiplicity(1, 1)),
        Property(name="publications", type=Bibtex_Author, multiplicity=Multiplicity(0, 9999))
    }
)
literaturedb5: BinaryAssociation = BinaryAssociation(
    name="literaturedb5",
    ends={
        Property(name="LiteratureDb", type=Bibtex_Entry, multiplicity=Multiplicity(1, 1)),
        Property(name="entries", type=Bibtex_LiteratureDb, multiplicity=Multiplicity(1, 1))
    }
)
publications6: BinaryAssociation = BinaryAssociation(
    name="publications6",
    ends={
        Property(name="Entry7", type=Bibtex_Author, multiplicity=Multiplicity(1, 1)),
        Property(name="author", type=Bibtex_Entry, multiplicity=Multiplicity(0, 9999))
    }
)
literaturedb8: BinaryAssociation = BinaryAssociation(
    name="literaturedb8",
    ends={
        Property(name="LiteratureDb10", type=Bibtex_Author, multiplicity=Multiplicity(1, 1)),
        Property(name="author9", type=Bibtex_LiteratureDb, multiplicity=Multiplicity(1, 1))
    }
)
author0: BinaryAssociation = BinaryAssociation(
    name="author0",
    ends={
        Property(name="Author", type=Bibtex_LiteratureDb, multiplicity=Multiplicity(1, 1)),
        Property(name="literaturedb", type=Bibtex_Author, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Bibtex",
    types={Bibtex_LiteratureDb, Bibtex_Author, Bibtex_Entry},
    associations={entries1, author3, literaturedb5, publications6, literaturedb8, author0},
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