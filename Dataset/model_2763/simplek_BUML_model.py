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
simplek_Base = Class(name="simplek::Base")
simplek_Content = Class(name="simplek::Content")
simplek_A = Class(name="simplek::A")
simplek_B = Class(name="simplek::B")

# simplek_Base class attributes and methods

# simplek_Content class attributes and methods
simplek_Content_name: Property = Property(name="name", type=StringType)
simplek_Content.attributes={simplek_Content_name}

# simplek_A class attributes and methods
simplek_A_name: Property = Property(name="name", type=StringType)
simplek_A.attributes={simplek_A_name}

# simplek_B class attributes and methods
simplek_B_name: Property = Property(name="name", type=StringType)
simplek_B.attributes={simplek_B_name}

# Relationships
contents0: BinaryAssociation = BinaryAssociation(
    name="contents0",
    ends={
        Property(name="simplek_Content", type=simplek_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="simplek_Base", type=simplek_Content, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
as1: BinaryAssociation = BinaryAssociation(
    name="as1",
    ends={
        Property(name="simplek_A", type=simplek_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="simplek_Content2", type=simplek_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bs3: BinaryAssociation = BinaryAssociation(
    name="bs3",
    ends={
        Property(name="simplek_B", type=simplek_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="simplek_Content4", type=simplek_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="simplek",
    types={simplek_Base, simplek_Content, simplek_A, simplek_B},
    associations={contents0, as1, bs3},
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