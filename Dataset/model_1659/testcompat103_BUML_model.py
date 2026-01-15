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
testcompat103_Thing = Class(name="testcompat103::Thing")
testcompat103_Foo = Class(name="testcompat103::Foo")
testcompat103_EClass0 = Class(name="testcompat103::EClass0")
testcompat103_EClass2 = Class(name="testcompat103::EClass2")
testcompat103_World = Class(name="testcompat103::World", is_abstract=True)
NamedElement = Class(name="NamedElement")
testcompat103_RelatedTo = Class(name="testcompat103::RelatedTo")
testcompat103_NamedElement = Class(name="testcompat103::NamedElement", is_abstract=True)
EClass0 = Class(name="EClass0")
testcompat103_EClass3 = Class(name="testcompat103::EClass3")
World = Class(name="World")
testcompat103_EClass1 = Class(name="testcompat103::EClass1")

# testcompat103_Thing class attributes and methods
testcompat103_Thing_id: Property = Property(name="id", type=IntegerType)
testcompat103_Thing.attributes={testcompat103_Thing_id}

# testcompat103_Foo class attributes and methods

# testcompat103_EClass0 class attributes and methods

# testcompat103_EClass2 class attributes and methods

# testcompat103_World class attributes and methods

# NamedElement class attributes and methods

# testcompat103_RelatedTo class attributes and methods
testcompat103_RelatedTo_since: Property = Property(name="since", type=StringType)
testcompat103_RelatedTo.attributes={testcompat103_RelatedTo_since}

# testcompat103_NamedElement class attributes and methods
testcompat103_NamedElement_name: Property = Property(name="name", type=StringType)
testcompat103_NamedElement.attributes={testcompat103_NamedElement_name}

# EClass0 class attributes and methods

# testcompat103_EClass3 class attributes and methods

# World class attributes and methods

# testcompat103_EClass1 class attributes and methods

# Relationships
things0: BinaryAssociation = BinaryAssociation(
    name="things0",
    ends={
        Property(name="testcompat103_Thing", type=testcompat103_World, multiplicity=Multiplicity(1, 1)),
        Property(name="testcompat103_World", type=testcompat103_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foos1: BinaryAssociation = BinaryAssociation(
    name="foos1",
    ends={
        Property(name="testcompat103_Foo", type=testcompat103_World, multiplicity=Multiplicity(1, 1)),
        Property(name="testcompat103_World2", type=testcompat103_Foo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ec0s3: BinaryAssociation = BinaryAssociation(
    name="ec0s3",
    ends={
        Property(name="testcompat103_EClass0", type=testcompat103_World, multiplicity=Multiplicity(1, 1)),
        Property(name="testcompat103_World4", type=testcompat103_EClass0, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ec2s5: BinaryAssociation = BinaryAssociation(
    name="ec2s5",
    ends={
        Property(name="testcompat103_EClass2", type=testcompat103_World, multiplicity=Multiplicity(1, 1)),
        Property(name="testcompat103_World6", type=testcompat103_EClass2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing8: BinaryAssociation = BinaryAssociation(
    name="fromThing8",
    ends={
        Property(name="Thing", type=testcompat103_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=testcompat103_Thing, multiplicity=Multiplicity(0, 1))
    }
)
toThing9: BinaryAssociation = BinaryAssociation(
    name="toThing9",
    ends={
        Property(name="testcompat103_Thing10", type=testcompat103_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="testcompat103_RelatedTo", type=testcompat103_Thing, multiplicity=Multiplicity(0, 1))
    }
)
relations7: BinaryAssociation = BinaryAssociation(
    name="relations7",
    ends={
        Property(name="RelatedTo", type=testcompat103_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=testcompat103_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
e1s11: BinaryAssociation = BinaryAssociation(
    name="e1s11",
    ends={
        Property(name="testcompat103_EClass1", type=testcompat103_EClass0, multiplicity=Multiplicity(1, 1)),
        Property(name="testcompat103_EClass012", type=testcompat103_EClass1, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subs14: BinaryAssociation = BinaryAssociation(
    name="subs14",
    ends={
        Property(name="testcompat103_EClass3", type=testcompat103_EClass3, multiplicity=Multiplicity(1, 1)),
        Property(name="testcompat103_EClass313", type=testcompat103_EClass3, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_testcompat103_World_NamedElement = Generalization(general=NamedElement, specific=testcompat103_World)
gen_testcompat103_RelatedTo_NamedElement = Generalization(general=NamedElement, specific=testcompat103_RelatedTo)
gen_testcompat103_Foo_NamedElement = Generalization(general=NamedElement, specific=testcompat103_Foo)
gen_testcompat103_Thing_NamedElement = Generalization(general=NamedElement, specific=testcompat103_Thing)
gen_testcompat103_EClass2_EClass0 = Generalization(general=EClass0, specific=testcompat103_EClass2)
gen_testcompat103_EClass3_World = Generalization(general=World, specific=testcompat103_EClass3)
gen_testcompat103_EClass0_NamedElement = Generalization(general=NamedElement, specific=testcompat103_EClass0)
gen_testcompat103_EClass1_NamedElement = Generalization(general=NamedElement, specific=testcompat103_EClass1)

# Domain Model
domain_model = DomainModel(
    name="testcompat103",
    types={testcompat103_Thing, testcompat103_Foo, testcompat103_EClass0, testcompat103_EClass2, testcompat103_World, NamedElement, testcompat103_RelatedTo, testcompat103_NamedElement, EClass0, testcompat103_EClass3, World, testcompat103_EClass1},
    associations={things0, foos1, ec0s3, ec2s5, fromThing8, toThing9, relations7, e1s11, subs14},
    generalizations={gen_testcompat103_World_NamedElement, gen_testcompat103_RelatedTo_NamedElement, gen_testcompat103_Foo_NamedElement, gen_testcompat103_Thing_NamedElement, gen_testcompat103_EClass2_EClass0, gen_testcompat103_EClass3_World, gen_testcompat103_EClass0_NamedElement, gen_testcompat103_EClass1_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)