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
TypeA_ListElement = Class(name="TypeA::ListElement")
AA = Class(name="AA")
TypeA_AA = Class(name="TypeA::AA", is_abstract=True)
TypeA_B = Class(name="TypeA::B")
TypeA_C = Class(name="TypeA::C")
B = Class(name="B")
TypeA_D = Class(name="TypeA::D")
TypeA_ObjectX = Class(name="TypeA::ObjectX")
TypeA_ObjectY = Class(name="TypeA::ObjectY")
TypeA_ObjectR = Class(name="TypeA::ObjectR")
ObjectX = Class(name="ObjectX")
ObjectR = Class(name="ObjectR")
TypeA_ObjectS = Class(name="TypeA::ObjectS")

# TypeA_ListElement class attributes and methods
TypeA_ListElement_nameListElement: Property = Property(name="nameListElement", type=StringType)
TypeA_ListElement.attributes={TypeA_ListElement_nameListElement}

# AA class attributes and methods

# TypeA_AA class attributes and methods
TypeA_AA_nameA: Property = Property(name="nameA", type=StringType)
TypeA_AA.attributes={TypeA_AA_nameA}

# TypeA_B class attributes and methods
TypeA_B_nameB: Property = Property(name="nameB", type=StringType)
TypeA_B.attributes={TypeA_B_nameB}

# TypeA_C class attributes and methods
TypeA_C_nameC: Property = Property(name="nameC", type=StringType)
TypeA_C.attributes={TypeA_C_nameC}

# B class attributes and methods

# TypeA_D class attributes and methods
TypeA_D_nameD: Property = Property(name="nameD", type=StringType)
TypeA_D.attributes={TypeA_D_nameD}

# TypeA_ObjectX class attributes and methods
TypeA_ObjectX_nameX: Property = Property(name="nameX", type=StringType)
TypeA_ObjectX.attributes={TypeA_ObjectX_nameX}

# TypeA_ObjectY class attributes and methods
TypeA_ObjectY_nameY: Property = Property(name="nameY", type=StringType)
TypeA_ObjectY.attributes={TypeA_ObjectY_nameY}

# TypeA_ObjectR class attributes and methods
TypeA_ObjectR_nameR: Property = Property(name="nameR", type=StringType)
TypeA_ObjectR.attributes={TypeA_ObjectR_nameR}

# ObjectX class attributes and methods

# ObjectR class attributes and methods

# TypeA_ObjectS class attributes and methods
TypeA_ObjectS_nameS: Property = Property(name="nameS", type=StringType)
TypeA_ObjectS.attributes={TypeA_ObjectS_nameS}

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="AA", type=TypeA_ListElement, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeA_ListElement", type=AA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xyElements1: BinaryAssociation = BinaryAssociation(
    name="xyElements1",
    ends={
        Property(name="ObjectX", type=TypeA_ListElement, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeA_ListElement2", type=ObjectX, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rsElements3: BinaryAssociation = BinaryAssociation(
    name="rsElements3",
    ends={
        Property(name="ObjectR", type=TypeA_ListElement, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeA_ListElement4", type=ObjectR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_TypeA_B_AA = Generalization(general=AA, specific=TypeA_B)
gen_TypeA_C_B = Generalization(general=B, specific=TypeA_C)
gen_TypeA_D_AA = Generalization(general=AA, specific=TypeA_D)
gen_TypeA_ObjectY_ObjectX = Generalization(general=ObjectX, specific=TypeA_ObjectY)
gen_TypeA_ObjectS_ObjectR = Generalization(general=ObjectR, specific=TypeA_ObjectS)

# Domain Model
domain_model = DomainModel(
    name="TypeA",
    types={TypeA_ListElement, AA, TypeA_AA, TypeA_B, TypeA_C, B, TypeA_D, TypeA_ObjectX, TypeA_ObjectY, TypeA_ObjectR, ObjectX, ObjectR, TypeA_ObjectS},
    associations={elements0, xyElements1, rsElements3},
    generalizations={gen_TypeA_B_AA, gen_TypeA_C_B, gen_TypeA_D_AA, gen_TypeA_ObjectY_ObjectX, gen_TypeA_ObjectS_ObjectR},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)