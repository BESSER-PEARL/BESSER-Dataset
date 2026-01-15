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
StyleKind: Enumeration = Enumeration(
    name="StyleKind",
    literals={
            EnumerationLiteral(name="Style1"),
			EnumerationLiteral(name="Style2")
    }
)

# Classes
abcd_Model = Class(name="abcd::Model")
NamedElt = Class(name="NamedElt")
abcd_A = Class(name="abcd::A")
abcd_Other = Class(name="abcd::Other")
abcd_NamedElt = Class(name="abcd::NamedElt", is_abstract=True)
A = Class(name="A")
abcd_C1 = Class(name="abcd::C1")
abcd_B = Class(name="abcd::B")
abcd_C = Class(name="abcd::C")
abcd_D = Class(name="abcd::D", is_abstract=True)
B = Class(name="B")
abcd_D3_B_C = Class(name="abcd::D3::B::C")
D3_B = Class(name="D3::B")
C = Class(name="C")
abcd_C2 = Class(name="abcd::C2")
abcd_D1 = Class(name="abcd::D1")
D = Class(name="D")
abcd_D2 = Class(name="abcd::D2")
abcd_D3 = Class(name="abcd::D3")
abcd_D3_B = Class(name="abcd::D3::B")
D3 = Class(name="D3")

# abcd_Model class attributes and methods
abcd_Model_style: Property = Property(name="style", type=StringType)
abcd_Model.attributes={abcd_Model_style}

# NamedElt class attributes and methods

# abcd_A class attributes and methods
abcd_A_aBooleanAttr: Property = Property(name="aBooleanAttr", type=StringType)
abcd_A_anIntegerAttr: Property = Property(name="anIntegerAttr", type=IntegerType)
abcd_A.attributes={abcd_A_aBooleanAttr, abcd_A_anIntegerAttr}

# abcd_Other class attributes and methods

# abcd_NamedElt class attributes and methods
abcd_NamedElt_name: Property = Property(name="name", type=StringType)
abcd_NamedElt.attributes={abcd_NamedElt_name}

# A class attributes and methods

# abcd_C1 class attributes and methods
abcd_C1_propOfC1: Property = Property(name="propOfC1", type=StringType)
abcd_C1.attributes={abcd_C1_propOfC1}

# abcd_B class attributes and methods
abcd_B_propOfB: Property = Property(name="propOfB", type=StringType)
abcd_B.attributes={abcd_B_propOfB}

# abcd_C class attributes and methods
abcd_C_propOfC: Property = Property(name="propOfC", type=StringType)
abcd_C.attributes={abcd_C_propOfC}

# abcd_D class attributes and methods
abcd_D_propOfD: Property = Property(name="propOfD", type=StringType)
abcd_D.attributes={abcd_D_propOfD}

# B class attributes and methods

# abcd_D3_B_C class attributes and methods

# D3_B class attributes and methods

# C class attributes and methods

# abcd_C2 class attributes and methods
abcd_C2_propOfC2: Property = Property(name="propOfC2", type=StringType)
abcd_C2.attributes={abcd_C2_propOfC2}

# abcd_D1 class attributes and methods
abcd_D1_commonOfD: Property = Property(name="commonOfD", type=StringType)
abcd_D1.attributes={abcd_D1_commonOfD}

# D class attributes and methods

# abcd_D2 class attributes and methods
abcd_D2_commonOfD: Property = Property(name="commonOfD", type=StringType)
abcd_D2.attributes={abcd_D2_commonOfD}

# abcd_D3 class attributes and methods
abcd_D3_commonOfD: Property = Property(name="commonOfD", type=StringType)
abcd_D3.attributes={abcd_D3_commonOfD}

# abcd_D3_B class attributes and methods

# D3 class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="abcd_A", type=abcd_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="abcd_Model", type=abcd_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
others1: BinaryAssociation = BinaryAssociation(
    name="others1",
    ends={
        Property(name="abcd_Other", type=abcd_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="abcd_Model2", type=abcd_Other, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
optionalA3: BinaryAssociation = BinaryAssociation(
    name="optionalA3",
    ends={
        Property(name="abcd_A5", type=abcd_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="abcd_Model4", type=abcd_A, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
optionalB6: BinaryAssociation = BinaryAssociation(
    name="optionalB6",
    ends={
        Property(name="abcd_B", type=abcd_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="abcd_Model7", type=abcd_B, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
optionalC8: BinaryAssociation = BinaryAssociation(
    name="optionalC8",
    ends={
        Property(name="abcd_C", type=abcd_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="abcd_Model9", type=abcd_C, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
optionalD10: BinaryAssociation = BinaryAssociation(
    name="optionalD10",
    ends={
        Property(name="abcd_D", type=abcd_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="abcd_Model11", type=abcd_D, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children13: BinaryAssociation = BinaryAssociation(
    name="children13",
    ends={
        Property(name="abcd_A14", type=abcd_A, multiplicity=Multiplicity(1, 1)),
        Property(name="abcd_A12", type=abcd_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_abcd_Model_NamedElt = Generalization(general=NamedElt, specific=abcd_Model)
gen_abcd_B_A = Generalization(general=A, specific=abcd_B)
gen_abcd_C_A = Generalization(general=A, specific=abcd_C)
gen_abcd_A_NamedElt = Generalization(general=NamedElt, specific=abcd_A)
gen_abcd_D3_B_D3 = Generalization(general=D3, specific=abcd_D3_B)
gen_abcd_D3_B_B = Generalization(general=B, specific=abcd_D3_B)
gen_abcd_D3_B_C_D3_B = Generalization(general=D3_B, specific=abcd_D3_B_C)
gen_abcd_D3_B_C_C = Generalization(general=C, specific=abcd_D3_B_C)
gen_abcd_Other_NamedElt = Generalization(general=NamedElt, specific=abcd_Other)
gen_abcd_C1_C = Generalization(general=C, specific=abcd_C1)
gen_abcd_C2_C = Generalization(general=C, specific=abcd_C2)
gen_abcd_D_A = Generalization(general=A, specific=abcd_D)
gen_abcd_D1_D = Generalization(general=D, specific=abcd_D1)
gen_abcd_D2_D = Generalization(general=D, specific=abcd_D2)
gen_abcd_D3_D = Generalization(general=D, specific=abcd_D3)

# Domain Model
domain_model = DomainModel(
    name="abcd",
    types={abcd_Model, NamedElt, abcd_A, abcd_Other, abcd_NamedElt, A, abcd_C1, abcd_B, abcd_C, abcd_D, B, abcd_D3_B_C, D3_B, C, abcd_C2, abcd_D1, D, abcd_D2, abcd_D3, abcd_D3_B, D3, StyleKind},
    associations={elements0, others1, optionalA3, optionalB6, optionalC8, optionalD10, children13},
    generalizations={gen_abcd_Model_NamedElt, gen_abcd_B_A, gen_abcd_C_A, gen_abcd_A_NamedElt, gen_abcd_D3_B_D3, gen_abcd_D3_B_B, gen_abcd_D3_B_C_D3_B, gen_abcd_D3_B_C_C, gen_abcd_Other_NamedElt, gen_abcd_C1_C, gen_abcd_C2_C, gen_abcd_D_A, gen_abcd_D1_D, gen_abcd_D2_D, gen_abcd_D3_D},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)