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
mm3_Library = Class(name="mm3::Library")
mm3_Member = Class(name="mm3::Member")
mm3_Film = Class(name="mm3::Film")
mm3_Book = Class(name="mm3::Book")

# mm3_Library class attributes and methods
mm3_Library_name: Property = Property(name="name", type=StringType)
mm3_Library.attributes={mm3_Library_name}

# mm3_Member class attributes and methods
mm3_Member_name: Property = Property(name="name", type=StringType)
mm3_Member.attributes={mm3_Member_name}

# mm3_Film class attributes and methods
mm3_Film_name: Property = Property(name="name", type=StringType)
mm3_Film.attributes={mm3_Film_name}

# mm3_Book class attributes and methods
mm3_Book_name: Property = Property(name="name", type=StringType)
mm3_Book.attributes={mm3_Book_name}

# Relationships
books1: BinaryAssociation = BinaryAssociation(
    name="books1",
    ends={
        Property(name="mm3_Book", type=mm3_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="mm3_Library2", type=mm3_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
films3: BinaryAssociation = BinaryAssociation(
    name="films3",
    ends={
        Property(name="mm3_Film", type=mm3_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="mm3_Library4", type=mm3_Film, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members0: BinaryAssociation = BinaryAssociation(
    name="members0",
    ends={
        Property(name="mm3_Member", type=mm3_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="mm3_Library", type=mm3_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bookLoans5: BinaryAssociation = BinaryAssociation(
    name="bookLoans5",
    ends={
        Property(name="mm3_Book7", type=mm3_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="mm3_Member6", type=mm3_Book, multiplicity=Multiplicity(0, 9999))
    }
)
filmLoans8: BinaryAssociation = BinaryAssociation(
    name="filmLoans8",
    ends={
        Property(name="mm3_Film10", type=mm3_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="mm3_Member9", type=mm3_Film, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="mm3",
    types={mm3_Library, mm3_Member, mm3_Film, mm3_Book},
    associations={books1, films3, members0, bookLoans5, filmLoans8},
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