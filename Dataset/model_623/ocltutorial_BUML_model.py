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
ocltutorial_Member = Class(name="ocltutorial::Member")
ocltutorial_Loans = Class(name="ocltutorial::Loans")
ocltutorial_Library = Class(name="ocltutorial::Library")
ocltutorial_Book = Class(name="ocltutorial::Book")

# ocltutorial_Member class attributes and methods
ocltutorial_Member_name: Property = Property(name="name", type=StringType)
ocltutorial_Member.attributes={ocltutorial_Member_name}

# ocltutorial_Loans class attributes and methods
ocltutorial_Loans_date: Property = Property(name="date", type=DateType)
ocltutorial_Loans.attributes={ocltutorial_Loans_date}

# ocltutorial_Library class attributes and methods

# ocltutorial_Book class attributes and methods
ocltutorial_Book_name: Property = Property(name="name", type=StringType)
ocltutorial_Book_copies: Property = Property(name="copies", type=StringType)
ocltutorial_Book.attributes={ocltutorial_Book_copies, ocltutorial_Book_name}

# Relationships
members1: BinaryAssociation = BinaryAssociation(
    name="members1",
    ends={
        Property(name="Member", type=ocltutorial_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library2", type=ocltutorial_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loans3: BinaryAssociation = BinaryAssociation(
    name="loans3",
    ends={
        Property(name="ocltutorial_Loans", type=ocltutorial_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="ocltutorial_Library", type=ocltutorial_Loans, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="Book", type=ocltutorial_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library", type=ocltutorial_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
member5: BinaryAssociation = BinaryAssociation(
    name="member5",
    ends={
        Property(name="ocltutorial_Member", type=ocltutorial_Loans, multiplicity=Multiplicity(1, 1)),
        Property(name="ocltutorial_Loans6", type=ocltutorial_Member, multiplicity=Multiplicity(1, 1))
    }
)
library4: BinaryAssociation = BinaryAssociation(
    name="library4",
    ends={
        Property(name="Library", type=ocltutorial_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=ocltutorial_Library, multiplicity=Multiplicity(0, 1))
    }
)
library9: BinaryAssociation = BinaryAssociation(
    name="library9",
    ends={
        Property(name="Library10", type=ocltutorial_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="members", type=ocltutorial_Library, multiplicity=Multiplicity(0, 1))
    }
)
book7: BinaryAssociation = BinaryAssociation(
    name="book7",
    ends={
        Property(name="ocltutorial_Book", type=ocltutorial_Loans, multiplicity=Multiplicity(1, 1)),
        Property(name="ocltutorial_Loans8", type=ocltutorial_Book, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="ocltutorial",
    types={ocltutorial_Member, ocltutorial_Loans, ocltutorial_Library, ocltutorial_Book},
    associations={members1, loans3, books0, member5, library4, library9, book7},
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