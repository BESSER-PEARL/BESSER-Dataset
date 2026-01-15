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
multipleinheritence_NewEClass1 = Class(name="multipleinheritence::NewEClass1")
NewEClass2 = Class(name="NewEClass2")
NewEClass3 = Class(name="NewEClass3")
multipleinheritence_NewEClass2 = Class(name="multipleinheritence::NewEClass2")
multipleinheritence_NewEClass3 = Class(name="multipleinheritence::NewEClass3")
NewEClass4 = Class(name="NewEClass4")
NewEClass5 = Class(name="NewEClass5")
multipleinheritence_NewEClass4 = Class(name="multipleinheritence::NewEClass4")
multipleinheritence_NewEClass5 = Class(name="multipleinheritence::NewEClass5")

# multipleinheritence_NewEClass1 class attributes and methods
multipleinheritence_NewEClass1_f1: Property = Property(name="f1", type=IntegerType)
multipleinheritence_NewEClass1.attributes={multipleinheritence_NewEClass1_f1}

# NewEClass2 class attributes and methods

# NewEClass3 class attributes and methods

# multipleinheritence_NewEClass2 class attributes and methods
multipleinheritence_NewEClass2_f2: Property = Property(name="f2", type=IntegerType)
multipleinheritence_NewEClass2.attributes={multipleinheritence_NewEClass2_f2}

# multipleinheritence_NewEClass3 class attributes and methods
multipleinheritence_NewEClass3_f3: Property = Property(name="f3", type=IntegerType)
multipleinheritence_NewEClass3.attributes={multipleinheritence_NewEClass3_f3}

# NewEClass4 class attributes and methods

# NewEClass5 class attributes and methods

# multipleinheritence_NewEClass4 class attributes and methods
multipleinheritence_NewEClass4_f4: Property = Property(name="f4", type=IntegerType)
multipleinheritence_NewEClass4.attributes={multipleinheritence_NewEClass4_f4}

# multipleinheritence_NewEClass5 class attributes and methods
multipleinheritence_NewEClass5_f5: Property = Property(name="f5", type=IntegerType)
multipleinheritence_NewEClass5.attributes={multipleinheritence_NewEClass5_f5}

# Generalizations
gen_multipleinheritence_NewEClass1_NewEClass2 = Generalization(general=NewEClass2, specific=multipleinheritence_NewEClass1)
gen_multipleinheritence_NewEClass1_NewEClass3 = Generalization(general=NewEClass3, specific=multipleinheritence_NewEClass1)
gen_multipleinheritence_NewEClass3_NewEClass4 = Generalization(general=NewEClass4, specific=multipleinheritence_NewEClass3)
gen_multipleinheritence_NewEClass3_NewEClass5 = Generalization(general=NewEClass5, specific=multipleinheritence_NewEClass3)

# Domain Model
domain_model = DomainModel(
    name="multipleinheritence",
    types={multipleinheritence_NewEClass1, NewEClass2, NewEClass3, multipleinheritence_NewEClass2, multipleinheritence_NewEClass3, NewEClass4, NewEClass5, multipleinheritence_NewEClass4, multipleinheritence_NewEClass5},
    associations={},
    generalizations={gen_multipleinheritence_NewEClass1_NewEClass2, gen_multipleinheritence_NewEClass1_NewEClass3, gen_multipleinheritence_NewEClass3_NewEClass4, gen_multipleinheritence_NewEClass3_NewEClass5},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)