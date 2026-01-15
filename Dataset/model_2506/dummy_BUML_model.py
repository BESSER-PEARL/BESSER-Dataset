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

# Enumerations
EnumExample: Enumeration = Enumeration(
    name="EnumExample",
    literals={
            EnumerationLiteral(name="value1"),
			EnumerationLiteral(name="value2"),
			EnumerationLiteral(name="value3")
    }
)

# Classes
dummy_F = Class(name="dummy::F")
E = Class(name="E")
dummy_G = Class(name="dummy::G")
dummy_A = Class(name="dummy::A")
dummy_B = Class(name="dummy::B")
dummy_D = Class(name="dummy::D")
dummy_E = Class(name="dummy::E", is_abstract=True)
dummy_C = Class(name="dummy::C")

# dummy_F class attributes and methods
dummy_F_fString: Property = Property(name="fString", type=StringType)
dummy_F_fDouble: Property = Property(name="fDouble", type=FloatType)
dummy_F.attributes={dummy_F_fString, dummy_F_fDouble}

# E class attributes and methods

# dummy_G class attributes and methods
dummy_G_gString: Property = Property(name="gString", type=StringType)
dummy_G.attributes={dummy_G_gString}

# dummy_A class attributes and methods
dummy_A_x: Property = Property(name="x", type=FloatType)
dummy_A_en: Property = Property(name="en", type=StringType)
dummy_A.attributes={dummy_A_en, dummy_A_x}

# dummy_B class attributes and methods
dummy_B_y: Property = Property(name="y", type=FloatType)
dummy_B_z: Property = Property(name="z", type=FloatType)
dummy_B.attributes={dummy_B_z, dummy_B_y}

# dummy_D class attributes and methods
dummy_D_name: Property = Property(name="name", type=StringType)
dummy_D_l: Property = Property(name="l", type=FloatType)
dummy_D_m: Property = Property(name="m", type=FloatType)
dummy_D.attributes={dummy_D_m, dummy_D_l, dummy_D_name}

# dummy_E class attributes and methods
dummy_E_eName: Property = Property(name="eName", type=StringType)
dummy_E.attributes={dummy_E_eName}

# dummy_C class attributes and methods
dummy_C_k: Property = Property(name="k", type=FloatType)
dummy_C.attributes={dummy_C_k}

# Relationships
b0: BinaryAssociation = BinaryAssociation(
    name="b0",
    ends={
        Property(name="dummy_B", type=dummy_A, multiplicity=Multiplicity(1, 1)),
        Property(name="dummy_A", type=dummy_B, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ds1: BinaryAssociation = BinaryAssociation(
    name="ds1",
    ends={
        Property(name="dummy_D", type=dummy_A, multiplicity=Multiplicity(1, 1)),
        Property(name="dummy_A2", type=dummy_D, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
e3: BinaryAssociation = BinaryAssociation(
    name="e3",
    ends={
        Property(name="dummy_E", type=dummy_A, multiplicity=Multiplicity(1, 1)),
        Property(name="dummy_A4", type=dummy_E, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
c5: BinaryAssociation = BinaryAssociation(
    name="c5",
    ends={
        Property(name="dummy_C", type=dummy_B, multiplicity=Multiplicity(1, 1)),
        Property(name="dummy_B6", type=dummy_C, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_dummy_F_E = Generalization(general=E, specific=dummy_F)
gen_dummy_G_E = Generalization(general=E, specific=dummy_G)

# Domain Model
domain_model = DomainModel(
    name="dummy",
    types={dummy_F, E, dummy_G, dummy_A, dummy_B, dummy_D, dummy_E, dummy_C, EnumExample},
    associations={b0, ds1, e3, c5},
    generalizations={gen_dummy_F_E, gen_dummy_G_E},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)