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
refact_A = Class(name="refact::A")
refact_B = Class(name="refact::B")
refact_E = Class(name="refact::E")
refact_Named = Class(name="refact::Named")
Named = Class(name="Named")
refact_D = Class(name="refact::D")
refact_C = Class(name="refact::C")

# refact_A class attributes and methods

# refact_B class attributes and methods

# refact_E class attributes and methods

# refact_Named class attributes and methods
refact_Named_name: Property = Property(name="name", type=StringType)
refact_Named.attributes={refact_Named_name}

# Named class attributes and methods

# refact_D class attributes and methods

# refact_C class attributes and methods

# Relationships
Bs0: BinaryAssociation = BinaryAssociation(
    name="Bs0",
    ends={
        Property(name="refact_B", type=refact_A, multiplicity=Multiplicity(1, 1)),
        Property(name="refact_A", type=refact_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
es1: BinaryAssociation = BinaryAssociation(
    name="es1",
    ends={
        Property(name="refact_E", type=refact_A, multiplicity=Multiplicity(1, 1)),
        Property(name="refact_A2", type=refact_E, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ds3: BinaryAssociation = BinaryAssociation(
    name="ds3",
    ends={
        Property(name="refact_D", type=refact_B, multiplicity=Multiplicity(1, 1)),
        Property(name="refact_B4", type=refact_D, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
es5: BinaryAssociation = BinaryAssociation(
    name="es5",
    ends={
        Property(name="refact_E7", type=refact_B, multiplicity=Multiplicity(1, 1)),
        Property(name="refact_B6", type=refact_E, multiplicity=Multiplicity(0, 9999))
    }
)
cs8: BinaryAssociation = BinaryAssociation(
    name="cs8",
    ends={
        Property(name="refact_C", type=refact_B, multiplicity=Multiplicity(1, 1)),
        Property(name="refact_B9", type=refact_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c_input10: BinaryAssociation = BinaryAssociation(
    name="c_input10",
    ends={
        Property(name="refact_B12", type=refact_C, multiplicity=Multiplicity(1, 1)),
        Property(name="refact_C11", type=refact_B, multiplicity=Multiplicity(0, 1))
    }
)
c_outputs13: BinaryAssociation = BinaryAssociation(
    name="c_outputs13",
    ends={
        Property(name="refact_B15", type=refact_C, multiplicity=Multiplicity(1, 1)),
        Property(name="refact_C14", type=refact_B, multiplicity=Multiplicity(0, 9999))
    }
)
e16: BinaryAssociation = BinaryAssociation(
    name="e16",
    ends={
        Property(name="refact_E18", type=refact_D, multiplicity=Multiplicity(1, 1)),
        Property(name="refact_D17", type=refact_E, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_refact_C_Named = Generalization(general=Named, specific=refact_C)
gen_refact_B_Named = Generalization(general=Named, specific=refact_B)
gen_refact_D_Named = Generalization(general=Named, specific=refact_D)
gen_refact_E_Named = Generalization(general=Named, specific=refact_E)

# Domain Model
domain_model = DomainModel(
    name="refact",
    types={refact_A, refact_B, refact_E, refact_Named, Named, refact_D, refact_C},
    associations={Bs0, es1, ds3, es5, cs8, c_input10, c_outputs13, e16},
    generalizations={gen_refact_C_Named, gen_refact_B_Named, gen_refact_D_Named, gen_refact_E_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)