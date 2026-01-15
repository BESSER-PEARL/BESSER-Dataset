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
emfrelations_ConceptA0 = Class(name="emfrelations::ConceptA0")
emfrelations_ConceptB0 = Class(name="emfrelations::ConceptB0")
emfrelations_ConceptA1 = Class(name="emfrelations::ConceptA1")
emfrelations_ConceptB1 = Class(name="emfrelations::ConceptB1")
emfrelations_ConceptA2 = Class(name="emfrelations::ConceptA2")
emfrelations_ConceptB2 = Class(name="emfrelations::ConceptB2")
emfrelations_ConceptA3 = Class(name="emfrelations::ConceptA3")
emfrelations_ConceptA4 = Class(name="emfrelations::ConceptA4")
emfrelations_ConceptB4 = Class(name="emfrelations::ConceptB4")
emfrelations_ConceptA5 = Class(name="emfrelations::ConceptA5")
emfrelations_ConceptB5 = Class(name="emfrelations::ConceptB5")
emfrelations_ConceptA8 = Class(name="emfrelations::ConceptA8")
emfrelations_ConceptB8 = Class(name="emfrelations::ConceptB8")
emfrelations_ConceptB3 = Class(name="emfrelations::ConceptB3")
emfrelations_ConceptA10 = Class(name="emfrelations::ConceptA10")
emfrelations_ConceptB10 = Class(name="emfrelations::ConceptB10")
emfrelations_ConceptA11 = Class(name="emfrelations::ConceptA11")
emfrelations_ConceptB11 = Class(name="emfrelations::ConceptB11")
emfrelations_ConceptA9 = Class(name="emfrelations::ConceptA9")
emfrelations_ConceptB9 = Class(name="emfrelations::ConceptB9")

# emfrelations_ConceptA0 class attributes and methods

# emfrelations_ConceptB0 class attributes and methods

# emfrelations_ConceptA1 class attributes and methods

# emfrelations_ConceptB1 class attributes and methods

# emfrelations_ConceptA2 class attributes and methods

# emfrelations_ConceptB2 class attributes and methods

# emfrelations_ConceptA3 class attributes and methods

# emfrelations_ConceptA4 class attributes and methods

# emfrelations_ConceptB4 class attributes and methods

# emfrelations_ConceptA5 class attributes and methods

# emfrelations_ConceptB5 class attributes and methods

# emfrelations_ConceptA8 class attributes and methods

# emfrelations_ConceptB8 class attributes and methods

# emfrelations_ConceptB3 class attributes and methods

# emfrelations_ConceptA10 class attributes and methods

# emfrelations_ConceptB10 class attributes and methods

# emfrelations_ConceptA11 class attributes and methods

# emfrelations_ConceptB11 class attributes and methods

# emfrelations_ConceptA9 class attributes and methods

# emfrelations_ConceptB9 class attributes and methods

# Relationships
conceptb12: BinaryAssociation = BinaryAssociation(
    name="conceptb12",
    ends={
        Property(name="ConceptB1", type=emfrelations_ConceptA1, multiplicity=Multiplicity(1, 1)),
        Property(name="concepta1", type=emfrelations_ConceptB1, multiplicity=Multiplicity(0, 9999))
    }
)
concepta13: BinaryAssociation = BinaryAssociation(
    name="concepta13",
    ends={
        Property(name="ConceptA1", type=emfrelations_ConceptB1, multiplicity=Multiplicity(1, 1)),
        Property(name="conceptb1", type=emfrelations_ConceptA1, multiplicity=Multiplicity(0, 1))
    }
)
conceptb24: BinaryAssociation = BinaryAssociation(
    name="conceptb24",
    ends={
        Property(name="ConceptB2", type=emfrelations_ConceptA2, multiplicity=Multiplicity(1, 1)),
        Property(name="concepta2", type=emfrelations_ConceptB2, multiplicity=Multiplicity(0, 1))
    }
)
concepta25: BinaryAssociation = BinaryAssociation(
    name="concepta25",
    ends={
        Property(name="ConceptA2", type=emfrelations_ConceptB2, multiplicity=Multiplicity(1, 1)),
        Property(name="conceptb2", type=emfrelations_ConceptA2, multiplicity=Multiplicity(0, 9999))
    }
)
conceptb00: BinaryAssociation = BinaryAssociation(
    name="conceptb00",
    ends={
        Property(name="ConceptB0", type=emfrelations_ConceptA0, multiplicity=Multiplicity(1, 1)),
        Property(name="concepta0", type=emfrelations_ConceptB0, multiplicity=Multiplicity(0, 1))
    }
)
concepta01: BinaryAssociation = BinaryAssociation(
    name="concepta01",
    ends={
        Property(name="ConceptA0", type=emfrelations_ConceptB0, multiplicity=Multiplicity(1, 1)),
        Property(name="conceptb0", type=emfrelations_ConceptA0, multiplicity=Multiplicity(0, 1))
    }
)
conceptb48: BinaryAssociation = BinaryAssociation(
    name="conceptb48",
    ends={
        Property(name="ConceptB4", type=emfrelations_ConceptA4, multiplicity=Multiplicity(1, 1)),
        Property(name="concepta4", type=emfrelations_ConceptB4, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
concepta49: BinaryAssociation = BinaryAssociation(
    name="concepta49",
    ends={
        Property(name="ConceptA4", type=emfrelations_ConceptB4, multiplicity=Multiplicity(1, 1)),
        Property(name="conceptb4", type=emfrelations_ConceptA4, multiplicity=Multiplicity(0, 1))
    }
)
conceptb510: BinaryAssociation = BinaryAssociation(
    name="conceptb510",
    ends={
        Property(name="ConceptB5", type=emfrelations_ConceptA5, multiplicity=Multiplicity(1, 1)),
        Property(name="concepta5", type=emfrelations_ConceptB5, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
concepta511: BinaryAssociation = BinaryAssociation(
    name="concepta511",
    ends={
        Property(name="ConceptA5", type=emfrelations_ConceptB5, multiplicity=Multiplicity(1, 1)),
        Property(name="conceptb5", type=emfrelations_ConceptA5, multiplicity=Multiplicity(0, 1))
    }
)
conceptb36: BinaryAssociation = BinaryAssociation(
    name="conceptb36",
    ends={
        Property(name="ConceptB3", type=emfrelations_ConceptA3, multiplicity=Multiplicity(1, 1)),
        Property(name="concepta3", type=emfrelations_ConceptB3, multiplicity=Multiplicity(0, 9999))
    }
)
concepta37: BinaryAssociation = BinaryAssociation(
    name="concepta37",
    ends={
        Property(name="ConceptA3", type=emfrelations_ConceptB3, multiplicity=Multiplicity(1, 1)),
        Property(name="conceptb3", type=emfrelations_ConceptA3, multiplicity=Multiplicity(0, 9999))
    }
)
conceptb1014: BinaryAssociation = BinaryAssociation(
    name="conceptb1014",
    ends={
        Property(name="emfrelations_ConceptB10", type=emfrelations_ConceptA10, multiplicity=Multiplicity(1, 1)),
        Property(name="emfrelations_ConceptA10", type=emfrelations_ConceptB10, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conceptb1115: BinaryAssociation = BinaryAssociation(
    name="conceptb1115",
    ends={
        Property(name="emfrelations_ConceptB11", type=emfrelations_ConceptA11, multiplicity=Multiplicity(1, 1)),
        Property(name="emfrelations_ConceptA11", type=emfrelations_ConceptB11, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conceptb812: BinaryAssociation = BinaryAssociation(
    name="conceptb812",
    ends={
        Property(name="emfrelations_ConceptB8", type=emfrelations_ConceptA8, multiplicity=Multiplicity(1, 1)),
        Property(name="emfrelations_ConceptA8", type=emfrelations_ConceptB8, multiplicity=Multiplicity(0, 1))
    }
)
conceptb913: BinaryAssociation = BinaryAssociation(
    name="conceptb913",
    ends={
        Property(name="emfrelations_ConceptB9", type=emfrelations_ConceptA9, multiplicity=Multiplicity(1, 1)),
        Property(name="emfrelations_ConceptA9", type=emfrelations_ConceptB9, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="emfrelations",
    types={emfrelations_ConceptA0, emfrelations_ConceptB0, emfrelations_ConceptA1, emfrelations_ConceptB1, emfrelations_ConceptA2, emfrelations_ConceptB2, emfrelations_ConceptA3, emfrelations_ConceptA4, emfrelations_ConceptB4, emfrelations_ConceptA5, emfrelations_ConceptB5, emfrelations_ConceptA8, emfrelations_ConceptB8, emfrelations_ConceptB3, emfrelations_ConceptA10, emfrelations_ConceptB10, emfrelations_ConceptA11, emfrelations_ConceptB11, emfrelations_ConceptA9, emfrelations_ConceptB9},
    associations={conceptb12, concepta13, conceptb24, concepta25, conceptb00, concepta01, conceptb48, concepta49, conceptb510, concepta511, conceptb36, concepta37, conceptb1014, conceptb1115, conceptb812, conceptb913},
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