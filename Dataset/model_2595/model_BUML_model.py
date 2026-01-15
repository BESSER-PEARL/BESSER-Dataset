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
root_ClassA = Class(name="root::ClassA")
root_subpackage_ClassB = Class(name="root::subpackage::ClassB")
SuperB = Class(name="SuperB")
root_subpackage_SuperB = Class(name="root::subpackage::SuperB")
root_subpackage_SubA = Class(name="root::subpackage::SubA")
ClassB = Class(name="ClassB")

# root_ClassA class attributes and methods

# root_subpackage_ClassB class attributes and methods

# SuperB class attributes and methods

# root_subpackage_SuperB class attributes and methods

# root_subpackage_SubA class attributes and methods

# ClassB class attributes and methods

# Generalizations
gen_root_subpackage_ClassB_SuperB = Generalization(general=SuperB, specific=root_subpackage_ClassB)
gen_root_subpackage_SubA_ClassB = Generalization(general=ClassB, specific=root_subpackage_SubA)

# Domain Model
domain_model = DomainModel(
    name="root",
    types={root_ClassA, root_subpackage_ClassB, SuperB, root_subpackage_SuperB, root_subpackage_SubA, ClassB},
    associations={},
    generalizations={gen_root_subpackage_ClassB_SuperB, gen_root_subpackage_SubA_ClassB},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)