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
mm2_Book = Class(name="mm2::Book")
mm2_Library = Class(name="mm2::Library")
mm2_Member = Class(name="mm2::Member")
mm2_Loan = Class(name="mm2::Loan")

# mm2_Book class attributes and methods
mm2_Book_name: Property = Property(name="name", type=StringType)
mm2_Book.attributes={mm2_Book_name}

# mm2_Library class attributes and methods
mm2_Library_name: Property = Property(name="name", type=StringType)
mm2_Library.attributes={mm2_Library_name}

# mm2_Member class attributes and methods
mm2_Member_name: Property = Property(name="name", type=StringType)
mm2_Member.attributes={mm2_Member_name}

# mm2_Loan class attributes and methods
mm2_Loan_name: Property = Property(name="name", type=StringType)
mm2_Loan.attributes={mm2_Loan_name}

# Relationships
members0: BinaryAssociation = BinaryAssociation(
    name="members0",
    ends={
        Property(name="mm2_Member", type=mm2_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="mm2_Library", type=mm2_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books1: BinaryAssociation = BinaryAssociation(
    name="books1",
    ends={
        Property(name="mm2_Book", type=mm2_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="mm2_Library2", type=mm2_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loans3: BinaryAssociation = BinaryAssociation(
    name="loans3",
    ends={
        Property(name="mm2_Loan", type=mm2_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="mm2_Library4", type=mm2_Loan, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
book5: BinaryAssociation = BinaryAssociation(
    name="book5",
    ends={
        Property(name="Book", type=mm2_Loan, multiplicity=Multiplicity(1, 1)),
        Property(name="loans", type=mm2_Book, multiplicity=Multiplicity(1, 1))
    }
)
member6: BinaryAssociation = BinaryAssociation(
    name="member6",
    ends={
        Property(name="Member", type=mm2_Loan, multiplicity=Multiplicity(1, 1)),
        Property(name="loans7", type=mm2_Member, multiplicity=Multiplicity(1, 1))
    }
)
loans8: BinaryAssociation = BinaryAssociation(
    name="loans8",
    ends={
        Property(name="Loan", type=mm2_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="member", type=mm2_Loan, multiplicity=Multiplicity(0, 9999))
    }
)
loans9: BinaryAssociation = BinaryAssociation(
    name="loans9",
    ends={
        Property(name="Loan10", type=mm2_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="book", type=mm2_Loan, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="mm2",
    types={mm2_Book, mm2_Library, mm2_Member, mm2_Loan},
    associations={members0, books1, loans3, book5, member6, loans8, loans9},
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