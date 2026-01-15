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
tutorial_Book = Class(name="tutorial::Book")
tutorial_Loan = Class(name="tutorial::Loan")
tutorial_Library = Class(name="tutorial::Library")
tutorial_Member = Class(name="tutorial::Member")

# tutorial_Book class attributes and methods
tutorial_Book_name: Property = Property(name="name", type=StringType)
tutorial_Book_copies: Property = Property(name="copies", type=StringType)
tutorial_Book_m_isAvailable: Method = Method(name="isAvailable", parameters={}, type=BooleanType)
tutorial_Book.attributes={tutorial_Book_name, tutorial_Book_copies}
tutorial_Book.methods={tutorial_Book_m_isAvailable}

# tutorial_Loan class attributes and methods

# tutorial_Library class attributes and methods
tutorial_Library_name: Property = Property(name="name", type=StringType)
tutorial_Library.attributes={tutorial_Library_name}

# tutorial_Member class attributes and methods
tutorial_Member_name: Property = Property(name="name", type=StringType)
tutorial_Member.attributes={tutorial_Member_name}

# Relationships
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="Book", type=tutorial_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library", type=tutorial_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loans1: BinaryAssociation = BinaryAssociation(
    name="loans1",
    ends={
        Property(name="tutorial_Loan", type=tutorial_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="tutorial_Library", type=tutorial_Loan, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
library6: BinaryAssociation = BinaryAssociation(
    name="library6",
    ends={
        Property(name="Library", type=tutorial_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=tutorial_Library, multiplicity=Multiplicity(1, 1))
    }
)
library7: BinaryAssociation = BinaryAssociation(
    name="library7",
    ends={
        Property(name="Library8", type=tutorial_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="members", type=tutorial_Library, multiplicity=Multiplicity(1, 1))
    }
)
members2: BinaryAssociation = BinaryAssociation(
    name="members2",
    ends={
        Property(name="Member", type=tutorial_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library3", type=tutorial_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loans4: BinaryAssociation = BinaryAssociation(
    name="loans4",
    ends={
        Property(name="tutorial_Loan5", type=tutorial_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="tutorial_Book", type=tutorial_Loan, multiplicity=Multiplicity(0, 9999))
    }
)
book9: BinaryAssociation = BinaryAssociation(
    name="book9",
    ends={
        Property(name="tutorial_Book11", type=tutorial_Loan, multiplicity=Multiplicity(1, 1)),
        Property(name="tutorial_Loan10", type=tutorial_Book, multiplicity=Multiplicity(1, 1))
    }
)
member12: BinaryAssociation = BinaryAssociation(
    name="member12",
    ends={
        Property(name="tutorial_Member", type=tutorial_Loan, multiplicity=Multiplicity(1, 1)),
        Property(name="tutorial_Loan13", type=tutorial_Member, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="tutorial",
    types={tutorial_Book, tutorial_Loan, tutorial_Library, tutorial_Member},
    associations={books0, loans1, library6, library7, members2, loans4, book9, member12},
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