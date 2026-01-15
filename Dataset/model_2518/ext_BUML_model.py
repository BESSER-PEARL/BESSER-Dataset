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
ext_ExtE = Class(name="ext::ExtE")
E = Class(name="E")
ext_F = Class(name="ext::F")

# ext_ExtE class attributes and methods
ext_ExtE_value: Property = Property(name="value", type=IntegerType)
ext_ExtE.attributes={ext_ExtE_value}

# E class attributes and methods

# ext_F class attributes and methods
ext_F_id: Property = Property(name="id", type=StringType)
ext_F.attributes={ext_F_id}

# Relationships
e1: BinaryAssociation = BinaryAssociation(
    name="e1",
    ends={
        Property(name="ExtE", type=ext_F, multiplicity=Multiplicity(1, 1)),
        Property(name="f", type=ext_ExtE, multiplicity=Multiplicity(1, 1))
    }
)
f0: BinaryAssociation = BinaryAssociation(
    name="f0",
    ends={
        Property(name="F", type=ext_ExtE, multiplicity=Multiplicity(1, 1)),
        Property(name="e", type=ext_F, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_ext_ExtE_E = Generalization(general=E, specific=ext_ExtE)

# Domain Model
domain_model = DomainModel(
    name="ext",
    types={ext_ExtE, E, ext_F},
    associations={e1, f0},
    generalizations={gen_ext_ExtE_E},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)