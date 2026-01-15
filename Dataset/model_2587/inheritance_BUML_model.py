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
Subclass2 = Class(name="Subclass2")
inheritance_Subclass2 = Class(name="inheritance::Subclass2")
Superclass = Class(name="Superclass")
inheritance_Superclass = Class(name="inheritance::Superclass")
inheritance_Subclass1 = Class(name="inheritance::Subclass1")
inheritance_Sub2Subclass = Class(name="inheritance::Sub2Subclass")
Subclass3 = Class(name="Subclass3")
inheritance_Sub3Subclass = Class(name="inheritance::Sub3Subclass")
inheritance_Sub1Subclass = Class(name="inheritance::Sub1Subclass")
Subclass1 = Class(name="Subclass1")
inheritance_Subclass3 = Class(name="inheritance::Subclass3")

# Subclass2 class attributes and methods

# inheritance_Subclass2 class attributes and methods

# Superclass class attributes and methods

# inheritance_Superclass class attributes and methods

# inheritance_Subclass1 class attributes and methods

# inheritance_Sub2Subclass class attributes and methods

# Subclass3 class attributes and methods

# inheritance_Sub3Subclass class attributes and methods

# inheritance_Sub1Subclass class attributes and methods

# Subclass1 class attributes and methods

# inheritance_Subclass3 class attributes and methods

# Generalizations
gen_inheritance_Subclass1_Subclass2 = Generalization(general=Subclass2, specific=inheritance_Subclass1)
gen_inheritance_Subclass2_Superclass = Generalization(general=Superclass, specific=inheritance_Subclass2)
gen_inheritance_Sub2Subclass_Subclass3 = Generalization(general=Subclass3, specific=inheritance_Sub2Subclass)
gen_inheritance_Sub3Subclass_Subclass3 = Generalization(general=Subclass3, specific=inheritance_Sub3Subclass)
gen_inheritance_Sub1Subclass_Subclass1 = Generalization(general=Subclass1, specific=inheritance_Sub1Subclass)
gen_inheritance_Subclass3_Superclass = Generalization(general=Superclass, specific=inheritance_Subclass3)

# Domain Model
domain_model = DomainModel(
    name="inheritance",
    types={Subclass2, inheritance_Subclass2, Superclass, inheritance_Superclass, inheritance_Subclass1, inheritance_Sub2Subclass, Subclass3, inheritance_Sub3Subclass, inheritance_Sub1Subclass, Subclass1, inheritance_Subclass3},
    associations={},
    generalizations={gen_inheritance_Subclass1_Subclass2, gen_inheritance_Subclass2_Superclass, gen_inheritance_Sub2Subclass_Subclass3, gen_inheritance_Sub3Subclass_Subclass3, gen_inheritance_Sub1Subclass_Subclass1, gen_inheritance_Subclass3_Superclass},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)