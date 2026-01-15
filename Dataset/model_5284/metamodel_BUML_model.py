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
Example_A = Class(name="Example::A")
Example_B = Class(name="Example::B")
Example_Ba = Class(name="Example::Ba")
B = Class(name="B")
Example_Bb = Class(name="Example::Bb")

# Example_A class attributes and methods
Example_A_a: Property = Property(name="a", type=StringType)
Example_A_m_getAs: Method = Method(name="getAs", parameters={}, type=StringType)
Example_A.attributes={Example_A_a}
Example_A.methods={Example_A_m_getAs}

# Example_B class attributes and methods
Example_B_b: Property = Property(name="b", type=StringType)
Example_B_m_getBs: Method = Method(name="getBs", parameters={}, type=StringType)
Example_B.attributes={Example_B_b}
Example_B.methods={Example_B_m_getBs}

# Example_Ba class attributes and methods
Example_Ba_ba: Property = Property(name="ba", type=StringType)
Example_Ba.attributes={Example_Ba_ba}

# B class attributes and methods

# Example_Bb class attributes and methods

# Generalizations
gen_Example_Ba_B = Generalization(general=B, specific=Example_Ba)
gen_Example_Bb_B = Generalization(general=B, specific=Example_Bb)

# Domain Model
domain_model = DomainModel(
    name="Example",
    types={Example_A, Example_B, Example_Ba, B, Example_Bb},
    associations={},
    generalizations={gen_Example_Ba_B, gen_Example_Bb_B},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)