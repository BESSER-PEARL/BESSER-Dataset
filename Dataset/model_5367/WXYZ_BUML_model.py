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
wxyz_Y1 = Class(name="wxyz::Y1")
wxyz_Y2 = Class(name="wxyz::Y2")
wxyz_Z = Class(name="wxyz::Z")
Y = Class(name="Y")
wxyz_Z1 = Class(name="wxyz::Z1")
wxyz_Z2 = Class(name="wxyz::Z2")
wxyz_Z3 = Class(name="wxyz::Z3")
wxyz_NamedElt = Class(name="wxyz::NamedElt", is_abstract=True)
wxyz_Model = Class(name="wxyz::Model")
NamedElt = Class(name="NamedElt")
wxyz_W = Class(name="wxyz::W")
wxyz_Other = Class(name="wxyz::Other")
wxyz_X = Class(name="wxyz::X")
W = Class(name="W")
wxyz_Y = Class(name="wxyz::Y")
X = Class(name="X")

# wxyz_Y1 class attributes and methods

# wxyz_Y2 class attributes and methods

# wxyz_Z class attributes and methods
wxyz_Z_propOfZ: Property = Property(name="propOfZ", type=StringType)
wxyz_Z.attributes={wxyz_Z_propOfZ}

# Y class attributes and methods

# wxyz_Z1 class attributes and methods

# wxyz_Z2 class attributes and methods

# wxyz_Z3 class attributes and methods

# wxyz_NamedElt class attributes and methods
wxyz_NamedElt_name: Property = Property(name="name", type=StringType)
wxyz_NamedElt.attributes={wxyz_NamedElt_name}

# wxyz_Model class attributes and methods

# NamedElt class attributes and methods

# wxyz_W class attributes and methods
wxyz_W_propOfW: Property = Property(name="propOfW", type=StringType)
wxyz_W.attributes={wxyz_W_propOfW}

# wxyz_Other class attributes and methods

# wxyz_X class attributes and methods
wxyz_X_propOfX: Property = Property(name="propOfX", type=StringType)
wxyz_X.attributes={wxyz_X_propOfX}

# W class attributes and methods

# wxyz_Y class attributes and methods
wxyz_Y_propOfY: Property = Property(name="propOfY", type=StringType)
wxyz_Y.attributes={wxyz_Y_propOfY}

# X class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="wxyz_W", type=wxyz_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="wxyz_Model", type=wxyz_W, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
others1: BinaryAssociation = BinaryAssociation(
    name="others1",
    ends={
        Property(name="wxyz_Other", type=wxyz_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="wxyz_Model2", type=wxyz_Other, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
optionalX3: BinaryAssociation = BinaryAssociation(
    name="optionalX3",
    ends={
        Property(name="wxyz_X", type=wxyz_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="wxyz_Model4", type=wxyz_X, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children6: BinaryAssociation = BinaryAssociation(
    name="children6",
    ends={
        Property(name="wxyz_W7", type=wxyz_W, multiplicity=Multiplicity(1, 1)),
        Property(name="wxyz_W5", type=wxyz_W, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_wxyz_Y1_X = Generalization(general=X, specific=wxyz_Y1)
gen_wxyz_Y2_X = Generalization(general=X, specific=wxyz_Y2)
gen_wxyz_Z_Y = Generalization(general=Y, specific=wxyz_Z)
gen_wxyz_Z1_Y = Generalization(general=Y, specific=wxyz_Z1)
gen_wxyz_Z2_Y = Generalization(general=Y, specific=wxyz_Z2)
gen_wxyz_Z3_Y = Generalization(general=Y, specific=wxyz_Z3)
gen_wxyz_Other_NamedElt = Generalization(general=NamedElt, specific=wxyz_Other)
gen_wxyz_Model_NamedElt = Generalization(general=NamedElt, specific=wxyz_Model)
gen_wxyz_W_NamedElt = Generalization(general=NamedElt, specific=wxyz_W)
gen_wxyz_X_W = Generalization(general=W, specific=wxyz_X)
gen_wxyz_Y_X = Generalization(general=X, specific=wxyz_Y)

# Domain Model
domain_model = DomainModel(
    name="wxyz",
    types={wxyz_Y1, wxyz_Y2, wxyz_Z, Y, wxyz_Z1, wxyz_Z2, wxyz_Z3, wxyz_NamedElt, wxyz_Model, NamedElt, wxyz_W, wxyz_Other, wxyz_X, W, wxyz_Y, X},
    associations={elements0, others1, optionalX3, children6},
    generalizations={gen_wxyz_Y1_X, gen_wxyz_Y2_X, gen_wxyz_Z_Y, gen_wxyz_Z1_Y, gen_wxyz_Z2_Y, gen_wxyz_Z3_Y, gen_wxyz_Other_NamedElt, gen_wxyz_Model_NamedElt, gen_wxyz_W_NamedElt, gen_wxyz_X_W, gen_wxyz_Y_X},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)