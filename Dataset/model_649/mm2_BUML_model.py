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
mm2_Member = Class(name="mm2::Member")
mm2_Medium = Class(name="mm2::Medium")
mm2_Library = Class(name="mm2::Library")
mm2_Category = Class(name="mm2::Category")

# mm2_Member class attributes and methods
mm2_Member_name: Property = Property(name="name", type=StringType)
mm2_Member.attributes={mm2_Member_name}

# mm2_Medium class attributes and methods
mm2_Medium_name: Property = Property(name="name", type=StringType)
mm2_Medium_type: Property = Property(name="type", type=StringType)
mm2_Medium.attributes={mm2_Medium_type, mm2_Medium_name}

# mm2_Library class attributes and methods
mm2_Library_name: Property = Property(name="name", type=StringType)
mm2_Library.attributes={mm2_Library_name}

# mm2_Category class attributes and methods
mm2_Category_name: Property = Property(name="name", type=StringType)
mm2_Category.attributes={mm2_Category_name}

# Relationships
members0: BinaryAssociation = BinaryAssociation(
    name="members0",
    ends={
        Property(name="mm2_Member", type=mm2_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="mm2_Library", type=mm2_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mediums1: BinaryAssociation = BinaryAssociation(
    name="mediums1",
    ends={
        Property(name="mm2_Medium", type=mm2_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="mm2_Library2", type=mm2_Medium, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
categories3: BinaryAssociation = BinaryAssociation(
    name="categories3",
    ends={
        Property(name="mm2_Category", type=mm2_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="mm2_Library4", type=mm2_Category, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
categories6: BinaryAssociation = BinaryAssociation(
    name="categories6",
    ends={
        Property(name="mm2_Category7", type=mm2_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="mm2_Category5", type=mm2_Category, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mediums8: BinaryAssociation = BinaryAssociation(
    name="mediums8",
    ends={
        Property(name="mm2_Medium10", type=mm2_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="mm2_Category9", type=mm2_Medium, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loans11: BinaryAssociation = BinaryAssociation(
    name="loans11",
    ends={
        Property(name="mm2_Medium13", type=mm2_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="mm2_Member12", type=mm2_Medium, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="mm2",
    types={mm2_Member, mm2_Medium, mm2_Library, mm2_Category},
    associations={members0, mediums1, categories3, categories6, mediums8, loans11},
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