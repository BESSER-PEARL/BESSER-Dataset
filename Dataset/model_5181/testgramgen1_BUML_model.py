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
testgramgen1_System = Class(name="testgramgen1::System")
testgramgen1_Component = Class(name="testgramgen1::Component")
testgramgen1_DerivedComponent = Class(name="testgramgen1::DerivedComponent")
testgramgen1_Node = Class(name="testgramgen1::Node", is_abstract=True)
testgramgen1_A = Class(name="testgramgen1::A")
Node = Class(name="Node")
CNamedElement = Class(name="CNamedElement")
testgramgen1_ProtoLink = Class(name="testgramgen1::ProtoLink")
testgramgen1_C = Class(name="testgramgen1::C")
testgramgen1_CNamedElement = Class(name="testgramgen1::CNamedElement", is_abstract=True)
testgramgen1_D = Class(name="testgramgen1::D")
testgramgen1_B = Class(name="testgramgen1::B")
Component = Class(name="Component")
testgramgen1_DerivedLink = Class(name="testgramgen1::DerivedLink")
ProtoLink = Class(name="ProtoLink")

# testgramgen1_System class attributes and methods

# testgramgen1_Component class attributes and methods

# testgramgen1_DerivedComponent class attributes and methods

# testgramgen1_Node class attributes and methods

# testgramgen1_A class attributes and methods

# Node class attributes and methods

# CNamedElement class attributes and methods

# testgramgen1_ProtoLink class attributes and methods

# testgramgen1_C class attributes and methods

# testgramgen1_CNamedElement class attributes and methods
testgramgen1_CNamedElement_name: Property = Property(name="name", type=StringType)
testgramgen1_CNamedElement.attributes={testgramgen1_CNamedElement_name}

# testgramgen1_D class attributes and methods

# testgramgen1_B class attributes and methods

# Component class attributes and methods

# testgramgen1_DerivedLink class attributes and methods

# ProtoLink class attributes and methods

# Relationships
components0: BinaryAssociation = BinaryAssociation(
    name="components0",
    ends={
        Property(name="testgramgen1_Component", type=testgramgen1_System, multiplicity=Multiplicity(1, 1)),
        Property(name="testgramgen1_System", type=testgramgen1_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
anodes1: BinaryAssociation = BinaryAssociation(
    name="anodes1",
    ends={
        Property(name="testgramgen1_Node", type=testgramgen1_System, multiplicity=Multiplicity(1, 1)),
        Property(name="testgramgen1_System2", type=testgramgen1_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
links3: BinaryAssociation = BinaryAssociation(
    name="links3",
    ends={
        Property(name="testgramgen1_ProtoLink", type=testgramgen1_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="testgramgen1_Component4", type=testgramgen1_ProtoLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
src5: BinaryAssociation = BinaryAssociation(
    name="src5",
    ends={
        Property(name="testgramgen1_Component7", type=testgramgen1_ProtoLink, multiplicity=Multiplicity(1, 1)),
        Property(name="testgramgen1_ProtoLink6", type=testgramgen1_Component, multiplicity=Multiplicity(0, 1))
    }
)
trg8: BinaryAssociation = BinaryAssociation(
    name="trg8",
    ends={
        Property(name="testgramgen1_Node10", type=testgramgen1_ProtoLink, multiplicity=Multiplicity(1, 1)),
        Property(name="testgramgen1_ProtoLink9", type=testgramgen1_Node, multiplicity=Multiplicity(0, 1))
    }
)
from11: BinaryAssociation = BinaryAssociation(
    name="from11",
    ends={
        Property(name="testgramgen1_Component12", type=testgramgen1_DerivedLink, multiplicity=Multiplicity(1, 1)),
        Property(name="testgramgen1_DerivedLink", type=testgramgen1_Component, multiplicity=Multiplicity(0, 1))
    }
)
to13: BinaryAssociation = BinaryAssociation(
    name="to13",
    ends={
        Property(name="testgramgen1_B", type=testgramgen1_DerivedLink, multiplicity=Multiplicity(1, 1)),
        Property(name="testgramgen1_DerivedLink14", type=testgramgen1_B, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_testgramgen1_DerivedComponent_Component = Generalization(general=Component, specific=testgramgen1_DerivedComponent)
gen_testgramgen1_A_Node = Generalization(general=Node, specific=testgramgen1_A)
gen_testgramgen1_Component_CNamedElement = Generalization(general=CNamedElement, specific=testgramgen1_Component)
gen_testgramgen1_C_CNamedElement = Generalization(general=CNamedElement, specific=testgramgen1_C)
gen_testgramgen1_C_Node = Generalization(general=Node, specific=testgramgen1_C)
gen_testgramgen1_D_Node = Generalization(general=Node, specific=testgramgen1_D)
gen_testgramgen1_B_Node = Generalization(general=Node, specific=testgramgen1_B)
gen_testgramgen1_ProtoLink_Component = Generalization(general=Component, specific=testgramgen1_ProtoLink)
gen_testgramgen1_DerivedLink_ProtoLink = Generalization(general=ProtoLink, specific=testgramgen1_DerivedLink)
gen_testgramgen1_DerivedLink_CNamedElement = Generalization(general=CNamedElement, specific=testgramgen1_DerivedLink)

# Domain Model
domain_model = DomainModel(
    name="testgramgen1",
    types={testgramgen1_System, testgramgen1_Component, testgramgen1_DerivedComponent, testgramgen1_Node, testgramgen1_A, Node, CNamedElement, testgramgen1_ProtoLink, testgramgen1_C, testgramgen1_CNamedElement, testgramgen1_D, testgramgen1_B, Component, testgramgen1_DerivedLink, ProtoLink},
    associations={components0, anodes1, links3, src5, trg8, from11, to13},
    generalizations={gen_testgramgen1_DerivedComponent_Component, gen_testgramgen1_A_Node, gen_testgramgen1_Component_CNamedElement, gen_testgramgen1_C_CNamedElement, gen_testgramgen1_C_Node, gen_testgramgen1_D_Node, gen_testgramgen1_B_Node, gen_testgramgen1_ProtoLink_Component, gen_testgramgen1_DerivedLink_ProtoLink, gen_testgramgen1_DerivedLink_CNamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)