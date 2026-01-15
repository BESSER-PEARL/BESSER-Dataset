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
content_D = Class(name="content::D")
content_F = Class(name="content::F")
content_E = Class(name="content::E")
content_A = Class(name="content::A")
content_G = Class(name="content::G")
W = Class(name="W")
content_B = Class(name="content::B")
content_C = Class(name="content::C")
content_J = Class(name="content::J")
content_W = Class(name="content::W")
content_H = Class(name="content::H")
content_I = Class(name="content::I")
content_Q = Class(name="content::Q")
content_R = Class(name="content::R")
content_P = Class(name="content::P")
content_M = Class(name="content::M")
content_N = Class(name="content::N")

# content_D class attributes and methods

# content_F class attributes and methods

# content_E class attributes and methods

# content_A class attributes and methods

# content_G class attributes and methods

# W class attributes and methods

# content_B class attributes and methods

# content_C class attributes and methods

# content_J class attributes and methods
content_J_linkName: Property = Property(name="linkName", type=StringType)
content_J_cardinality: Property = Property(name="cardinality", type=IntegerType)
content_J.attributes={content_J_cardinality, content_J_linkName}

# content_W class attributes and methods
content_W_name: Property = Property(name="name", type=StringType)
content_W.attributes={content_W_name}

# content_H class attributes and methods

# content_I class attributes and methods

# content_Q class attributes and methods

# content_R class attributes and methods

# content_P class attributes and methods

# content_M class attributes and methods

# content_N class attributes and methods

# Relationships
ds3: BinaryAssociation = BinaryAssociation(
    name="ds3",
    ends={
        Property(name="content_D", type=content_A, multiplicity=Multiplicity(1, 1)),
        Property(name="content_A4", type=content_D, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fs5: BinaryAssociation = BinaryAssociation(
    name="fs5",
    ends={
        Property(name="content_F", type=content_A, multiplicity=Multiplicity(1, 1)),
        Property(name="content_A6", type=content_F, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
es7: BinaryAssociation = BinaryAssociation(
    name="es7",
    ends={
        Property(name="content_E", type=content_A, multiplicity=Multiplicity(1, 1)),
        Property(name="content_A8", type=content_E, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nested10: BinaryAssociation = BinaryAssociation(
    name="nested10",
    ends={
        Property(name="content_A11", type=content_A, multiplicity=Multiplicity(1, 1)),
        Property(name="content_A9", type=content_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bs0: BinaryAssociation = BinaryAssociation(
    name="bs0",
    ends={
        Property(name="content_B", type=content_A, multiplicity=Multiplicity(1, 1)),
        Property(name="content_A", type=content_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cs1: BinaryAssociation = BinaryAssociation(
    name="cs1",
    ends={
        Property(name="content_C", type=content_A, multiplicity=Multiplicity(1, 1)),
        Property(name="content_A2", type=content_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
js17: BinaryAssociation = BinaryAssociation(
    name="js17",
    ends={
        Property(name="content_J", type=content_F, multiplicity=Multiplicity(1, 1)),
        Property(name="content_F18", type=content_J, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hs19: BinaryAssociation = BinaryAssociation(
    name="hs19",
    ends={
        Property(name="content_H", type=content_G, multiplicity=Multiplicity(1, 1)),
        Property(name="content_G20", type=content_H, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
is21: BinaryAssociation = BinaryAssociation(
    name="is21",
    ends={
        Property(name="content_I", type=content_G, multiplicity=Multiplicity(1, 1)),
        Property(name="content_G22", type=content_I, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qs23: BinaryAssociation = BinaryAssociation(
    name="qs23",
    ends={
        Property(name="content_Q", type=content_G, multiplicity=Multiplicity(1, 1)),
        Property(name="content_G24", type=content_Q, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gs12: BinaryAssociation = BinaryAssociation(
    name="gs12",
    ends={
        Property(name="content_G", type=content_C, multiplicity=Multiplicity(1, 1)),
        Property(name="content_C13", type=content_G, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
e14: BinaryAssociation = BinaryAssociation(
    name="e14",
    ends={
        Property(name="content_E16", type=content_D, multiplicity=Multiplicity(1, 1)),
        Property(name="content_D15", type=content_E, multiplicity=Multiplicity(0, 1))
    }
)
q28: BinaryAssociation = BinaryAssociation(
    name="q28",
    ends={
        Property(name="content_Q30", type=content_H, multiplicity=Multiplicity(1, 1)),
        Property(name="content_H29", type=content_Q, multiplicity=Multiplicity(0, 1))
    }
)
r31: BinaryAssociation = BinaryAssociation(
    name="r31",
    ends={
        Property(name="content_R", type=content_H, multiplicity=Multiplicity(1, 1)),
        Property(name="content_H32", type=content_R, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ps33: BinaryAssociation = BinaryAssociation(
    name="ps33",
    ends={
        Property(name="content_P", type=content_I, multiplicity=Multiplicity(1, 1)),
        Property(name="content_I34", type=content_P, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
h35: BinaryAssociation = BinaryAssociation(
    name="h35",
    ends={
        Property(name="content_H37", type=content_J, multiplicity=Multiplicity(1, 1)),
        Property(name="content_J36", type=content_H, multiplicity=Multiplicity(0, 1))
    }
)
eh25: BinaryAssociation = BinaryAssociation(
    name="eh25",
    ends={
        Property(name="content_E27", type=content_H, multiplicity=Multiplicity(1, 1)),
        Property(name="content_H26", type=content_E, multiplicity=Multiplicity(0, 1))
    }
)
qs42: BinaryAssociation = BinaryAssociation(
    name="qs42",
    ends={
        Property(name="content_Q44", type=content_P, multiplicity=Multiplicity(1, 1)),
        Property(name="content_P43", type=content_Q, multiplicity=Multiplicity(0, 9999))
    }
)
p45: BinaryAssociation = BinaryAssociation(
    name="p45",
    ends={
        Property(name="content_P47", type=content_R, multiplicity=Multiplicity(1, 1)),
        Property(name="content_R46", type=content_P, multiplicity=Multiplicity(0, 1))
    }
)
as38: BinaryAssociation = BinaryAssociation(
    name="as38",
    ends={
        Property(name="content_A39", type=content_M, multiplicity=Multiplicity(1, 1)),
        Property(name="content_M", type=content_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ns40: BinaryAssociation = BinaryAssociation(
    name="ns40",
    ends={
        Property(name="content_N", type=content_M, multiplicity=Multiplicity(1, 1)),
        Property(name="content_M41", type=content_N, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_content_B_W = Generalization(general=W, specific=content_B)
gen_content_C_W = Generalization(general=W, specific=content_C)
gen_content_A_W = Generalization(general=W, specific=content_A)
gen_content_F_W = Generalization(general=W, specific=content_F)
gen_content_G_W = Generalization(general=W, specific=content_G)
gen_content_D_W = Generalization(general=W, specific=content_D)
gen_content_E_W = Generalization(general=W, specific=content_E)
gen_content_I_W = Generalization(general=W, specific=content_I)
gen_content_J_W = Generalization(general=W, specific=content_J)
gen_content_H_W = Generalization(general=W, specific=content_H)
gen_content_P_W = Generalization(general=W, specific=content_P)
gen_content_Q_W = Generalization(general=W, specific=content_Q)
gen_content_R_W = Generalization(general=W, specific=content_R)
gen_content_M_W = Generalization(general=W, specific=content_M)
gen_content_N_W = Generalization(general=W, specific=content_N)

# Domain Model
domain_model = DomainModel(
    name="content",
    types={content_D, content_F, content_E, content_A, content_G, W, content_B, content_C, content_J, content_W, content_H, content_I, content_Q, content_R, content_P, content_M, content_N},
    associations={ds3, fs5, es7, nested10, bs0, cs1, js17, hs19, is21, qs23, gs12, e14, q28, r31, ps33, h35, eh25, qs42, p45, as38, ns40},
    generalizations={gen_content_B_W, gen_content_C_W, gen_content_A_W, gen_content_F_W, gen_content_G_W, gen_content_D_W, gen_content_E_W, gen_content_I_W, gen_content_J_W, gen_content_H_W, gen_content_P_W, gen_content_Q_W, gen_content_R_W, gen_content_M_W, gen_content_N_W},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)