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
TestB: Enumeration = Enumeration(
    name="TestB",
    literals={
            
    }
)

TestA: Enumeration = Enumeration(
    name="TestA",
    literals={
            
    }
)

# Classes
nonemf_Serializable = Class(name="nonemf::Serializable", is_abstract=True)
nonemf_MySerializableClass = Class(name="nonemf::MySerializableClass")
Serializable = Class(name="Serializable")
nonemf_B = Class(name="nonemf::B")
nonemf_A = Class(name="nonemf::A")

# nonemf_Serializable class attributes and methods

# nonemf_MySerializableClass class attributes and methods
nonemf_MySerializableClass_somethingInteresting: Property = Property(name="somethingInteresting", type=StringType)
nonemf_MySerializableClass.attributes={nonemf_MySerializableClass_somethingInteresting}

# Serializable class attributes and methods

# nonemf_B class attributes and methods

# nonemf_A class attributes and methods

# Generalizations
gen_nonemf_MySerializableClass_Serializable = Generalization(general=Serializable, specific=nonemf_MySerializableClass)

# Domain Model
domain_model = DomainModel(
    name="nonemf",
    types={nonemf_Serializable, nonemf_MySerializableClass, Serializable, nonemf_B, nonemf_A, TestB, TestA},
    associations={},
    generalizations={gen_nonemf_MySerializableClass_Serializable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)