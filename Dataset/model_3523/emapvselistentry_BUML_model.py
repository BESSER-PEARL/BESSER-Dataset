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
emapvselistentry_NewEClass2 = Class(name="emapvselistentry::NewEClass2")
emapvselistentry_NewEClass3 = Class(name="emapvselistentry::NewEClass3")
emapvselistentry_NewEClass4 = Class(name="emapvselistentry::NewEClass4")
emapvselistentry_NewEClass1 = Class(name="emapvselistentry::NewEClass1")
emapvselistentry_NewEClass5 = Class(name="emapvselistentry::NewEClass5")

# emapvselistentry_NewEClass2 class attributes and methods
emapvselistentry_NewEClass2_key: Property = Property(name="key", type=StringType)
emapvselistentry_NewEClass2_value: Property = Property(name="value", type=StringType)
emapvselistentry_NewEClass2.attributes={emapvselistentry_NewEClass2_key, emapvselistentry_NewEClass2_value}

# emapvselistentry_NewEClass3 class attributes and methods
emapvselistentry_NewEClass3_key: Property = Property(name="key", type=StringType)
emapvselistentry_NewEClass3_value: Property = Property(name="value", type=StringType)
emapvselistentry_NewEClass3.attributes={emapvselistentry_NewEClass3_key, emapvselistentry_NewEClass3_value}

# emapvselistentry_NewEClass4 class attributes and methods
emapvselistentry_NewEClass4_key: Property = Property(name="key", type=StringType)
emapvselistentry_NewEClass4_value: Property = Property(name="value", type=StringType)
emapvselistentry_NewEClass4.attributes={emapvselistentry_NewEClass4_key, emapvselistentry_NewEClass4_value}

# emapvselistentry_NewEClass1 class attributes and methods

# emapvselistentry_NewEClass5 class attributes and methods
emapvselistentry_NewEClass5_key: Property = Property(name="key", type=StringType)
emapvselistentry_NewEClass5_value: Property = Property(name="value", type=StringType)
emapvselistentry_NewEClass5.attributes={emapvselistentry_NewEClass5_key, emapvselistentry_NewEClass5_value}

# Relationships
neweclass20: BinaryAssociation = BinaryAssociation(
    name="neweclass20",
    ends={
        Property(name="emapvselistentry_NewEClass2", type=emapvselistentry_NewEClass1, multiplicity=Multiplicity(1, 1)),
        Property(name="emapvselistentry_NewEClass1", type=emapvselistentry_NewEClass2, multiplicity=Multiplicity(0, 9999))
    }
)
neweclass31: BinaryAssociation = BinaryAssociation(
    name="neweclass31",
    ends={
        Property(name="emapvselistentry_NewEClass3", type=emapvselistentry_NewEClass1, multiplicity=Multiplicity(1, 1)),
        Property(name="emapvselistentry_NewEClass12", type=emapvselistentry_NewEClass3, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
neweclass43: BinaryAssociation = BinaryAssociation(
    name="neweclass43",
    ends={
        Property(name="emapvselistentry_NewEClass4", type=emapvselistentry_NewEClass1, multiplicity=Multiplicity(1, 1)),
        Property(name="emapvselistentry_NewEClass14", type=emapvselistentry_NewEClass4, multiplicity=Multiplicity(0, 1))
    }
)
neweclass55: BinaryAssociation = BinaryAssociation(
    name="neweclass55",
    ends={
        Property(name="emapvselistentry_NewEClass5", type=emapvselistentry_NewEClass1, multiplicity=Multiplicity(1, 1)),
        Property(name="emapvselistentry_NewEClass16", type=emapvselistentry_NewEClass5, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="emapvselistentry",
    types={emapvselistentry_NewEClass2, emapvselistentry_NewEClass3, emapvselistentry_NewEClass4, emapvselistentry_NewEClass1, emapvselistentry_NewEClass5},
    associations={neweclass20, neweclass31, neweclass43, neweclass55},
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