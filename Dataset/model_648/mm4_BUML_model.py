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
mm4_Library = Class(name="mm4::Library")
mm4_Member = Class(name="mm4::Member")
mm4_Medium = Class(name="mm4::Medium")

# mm4_Library class attributes and methods
mm4_Library_name: Property = Property(name="name", type=StringType)
mm4_Library.attributes={mm4_Library_name}

# mm4_Member class attributes and methods
mm4_Member_name: Property = Property(name="name", type=StringType)
mm4_Member.attributes={mm4_Member_name}

# mm4_Medium class attributes and methods
mm4_Medium_name: Property = Property(name="name", type=StringType)
mm4_Medium_type: Property = Property(name="type", type=StringType)
mm4_Medium.attributes={mm4_Medium_name, mm4_Medium_type}

# Relationships
members0: BinaryAssociation = BinaryAssociation(
    name="members0",
    ends={
        Property(name="mm4_Member", type=mm4_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="mm4_Library", type=mm4_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mediums1: BinaryAssociation = BinaryAssociation(
    name="mediums1",
    ends={
        Property(name="mm4_Medium", type=mm4_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="mm4_Library2", type=mm4_Medium, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loans3: BinaryAssociation = BinaryAssociation(
    name="loans3",
    ends={
        Property(name="mm4_Medium5", type=mm4_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="mm4_Member4", type=mm4_Medium, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="mm4",
    types={mm4_Library, mm4_Member, mm4_Medium},
    associations={members0, mediums1, loans3},
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