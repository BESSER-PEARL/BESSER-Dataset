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
EnumA: Enumeration = Enumeration(
    name="EnumA",
    literals={
            EnumerationLiteral(name="CASE1"),
			EnumerationLiteral(name="CASE2")
    }
)

# Classes
testoperationbody_Main = Class(name="testoperationbody::Main")
testoperationbody_Parent = Class(name="testoperationbody::Parent", is_abstract=True)
testoperationbody_ChildA = Class(name="testoperationbody::ChildA")
Parent = Class(name="Parent")
testoperationbody_ConceptA = Class(name="testoperationbody::ConceptA")
testoperationbody_ChildB = Class(name="testoperationbody::ChildB")

# testoperationbody_Main class attributes and methods
testoperationbody_Main_listint: Property = Property(name="listint", type=IntegerType)
testoperationbody_Main_singlebool: Property = Property(name="singlebool", type=BooleanType)
testoperationbody_Main.attributes={testoperationbody_Main_singlebool, testoperationbody_Main_listint}

# testoperationbody_Parent class attributes and methods

# testoperationbody_ChildA class attributes and methods
testoperationbody_ChildA_value: Property = Property(name="value", type=StringType)
testoperationbody_ChildA.attributes={testoperationbody_ChildA_value}

# Parent class attributes and methods

# testoperationbody_ConceptA class attributes and methods

# testoperationbody_ChildB class attributes and methods

# Relationships
singleconcepta1: BinaryAssociation = BinaryAssociation(
    name="singleconcepta1",
    ends={
        Property(name="testoperationbody_ConceptA3", type=testoperationbody_Main, multiplicity=Multiplicity(1, 1)),
        Property(name="testoperationbody_Main2", type=testoperationbody_ConceptA, multiplicity=Multiplicity(0, 1))
    }
)
children4: BinaryAssociation = BinaryAssociation(
    name="children4",
    ends={
        Property(name="testoperationbody_Parent", type=testoperationbody_Main, multiplicity=Multiplicity(1, 1)),
        Property(name="testoperationbody_Main5", type=testoperationbody_Parent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listconcepta0: BinaryAssociation = BinaryAssociation(
    name="listconcepta0",
    ends={
        Property(name="testoperationbody_ConceptA", type=testoperationbody_Main, multiplicity=Multiplicity(1, 1)),
        Property(name="testoperationbody_Main", type=testoperationbody_ConceptA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_testoperationbody_ChildA_Parent = Generalization(general=Parent, specific=testoperationbody_ChildA)
gen_testoperationbody_ChildB_Parent = Generalization(general=Parent, specific=testoperationbody_ChildB)

# Domain Model
domain_model = DomainModel(
    name="testoperationbody",
    types={testoperationbody_Main, testoperationbody_Parent, testoperationbody_ChildA, Parent, testoperationbody_ConceptA, testoperationbody_ChildB, EnumA},
    associations={singleconcepta1, children4, listconcepta0},
    generalizations={gen_testoperationbody_ChildA_Parent, gen_testoperationbody_ChildB_Parent},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)