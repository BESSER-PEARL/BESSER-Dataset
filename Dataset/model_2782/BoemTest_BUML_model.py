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
AnEnumeration: Enumeration = Enumeration(
    name="AnEnumeration",
    literals={
            EnumerationLiteral(name="LITERAL0"),
			EnumerationLiteral(name="LITERAL1"),
			EnumerationLiteral(name="LITERAL2")
    }
)

# Classes
BoemTest_A = Class(name="BoemTest::A")
NamedElement = Class(name="NamedElement")
BoemTest_Node = Class(name="BoemTest::Node")
BoemTest_B = Class(name="BoemTest::B")
A = Class(name="A")
BoemTest_BNode = Class(name="BoemTest::BNode")
BoemTest_C = Class(name="BoemTest::C")
B = Class(name="B")
BoemTest_NamedElement = Class(name="BoemTest::NamedElement", is_abstract=True)

# BoemTest_A class attributes and methods

# NamedElement class attributes and methods

# BoemTest_Node class attributes and methods

# BoemTest_B class attributes and methods
BoemTest_B_enumAttr: Property = Property(name="enumAttr", type=StringType)
BoemTest_B.attributes={BoemTest_B_enumAttr}

# A class attributes and methods

# BoemTest_BNode class attributes and methods

# BoemTest_C class attributes and methods

# B class attributes and methods

# BoemTest_NamedElement class attributes and methods
BoemTest_NamedElement_name: Property = Property(name="name", type=StringType)
BoemTest_NamedElement.attributes={BoemTest_NamedElement_name}

# Relationships
childrenNode2A1: BinaryAssociation = BinaryAssociation(
    name="childrenNode2A1",
    ends={
        Property(name="BoemTest_Node3", type=BoemTest_A, multiplicity=Multiplicity(1, 1)),
        Property(name="BoemTest_A2", type=BoemTest_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childNodeA4: BinaryAssociation = BinaryAssociation(
    name="childNodeA4",
    ends={
        Property(name="BoemTest_Node6", type=BoemTest_A, multiplicity=Multiplicity(1, 1)),
        Property(name="BoemTest_A5", type=BoemTest_Node, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referencesNodeA7: BinaryAssociation = BinaryAssociation(
    name="referencesNodeA7",
    ends={
        Property(name="BoemTest_Node9", type=BoemTest_A, multiplicity=Multiplicity(1, 1)),
        Property(name="BoemTest_A8", type=BoemTest_Node, multiplicity=Multiplicity(0, 9999))
    }
)
referenceNodeA10: BinaryAssociation = BinaryAssociation(
    name="referenceNodeA10",
    ends={
        Property(name="BoemTest_Node12", type=BoemTest_A, multiplicity=Multiplicity(1, 1)),
        Property(name="BoemTest_A11", type=BoemTest_Node, multiplicity=Multiplicity(0, 1))
    }
)
childrenNodeA0: BinaryAssociation = BinaryAssociation(
    name="childrenNodeA0",
    ends={
        Property(name="BoemTest_Node", type=BoemTest_A, multiplicity=Multiplicity(1, 1)),
        Property(name="BoemTest_A", type=BoemTest_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childrenNodeC23: BinaryAssociation = BinaryAssociation(
    name="childrenNodeC23",
    ends={
        Property(name="BoemTest_Node24", type=BoemTest_C, multiplicity=Multiplicity(1, 1)),
        Property(name="BoemTest_C", type=BoemTest_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childNodeC25: BinaryAssociation = BinaryAssociation(
    name="childNodeC25",
    ends={
        Property(name="BoemTest_Node27", type=BoemTest_C, multiplicity=Multiplicity(1, 1)),
        Property(name="BoemTest_C26", type=BoemTest_Node, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referencesNodeC28: BinaryAssociation = BinaryAssociation(
    name="referencesNodeC28",
    ends={
        Property(name="BoemTest_Node30", type=BoemTest_C, multiplicity=Multiplicity(1, 1)),
        Property(name="BoemTest_C29", type=BoemTest_Node, multiplicity=Multiplicity(0, 9999))
    }
)
autoContainementA14: BinaryAssociation = BinaryAssociation(
    name="autoContainementA14",
    ends={
        Property(name="BoemTest_A15", type=BoemTest_A, multiplicity=Multiplicity(1, 1)),
        Property(name="BoemTest_A13", type=BoemTest_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childrenNodeB16: BinaryAssociation = BinaryAssociation(
    name="childrenNodeB16",
    ends={
        Property(name="BoemTest_Node17", type=BoemTest_B, multiplicity=Multiplicity(1, 1)),
        Property(name="BoemTest_B", type=BoemTest_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childNodeB18: BinaryAssociation = BinaryAssociation(
    name="childNodeB18",
    ends={
        Property(name="BoemTest_Node20", type=BoemTest_B, multiplicity=Multiplicity(1, 1)),
        Property(name="BoemTest_B19", type=BoemTest_Node, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
childrenNodeBNode21: BinaryAssociation = BinaryAssociation(
    name="childrenNodeBNode21",
    ends={
        Property(name="BoemTest_BNode", type=BoemTest_B, multiplicity=Multiplicity(1, 1)),
        Property(name="BoemTest_B22", type=BoemTest_BNode, multiplicity=Multiplicity(0, 1))
    }
)
referenceNodeC31: BinaryAssociation = BinaryAssociation(
    name="referenceNodeC31",
    ends={
        Property(name="BoemTest_Node33", type=BoemTest_C, multiplicity=Multiplicity(1, 1)),
        Property(name="BoemTest_C32", type=BoemTest_Node, multiplicity=Multiplicity(0, 1))
    }
)
children35: BinaryAssociation = BinaryAssociation(
    name="children35",
    ends={
        Property(name="BoemTest_Node36", type=BoemTest_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="BoemTest_Node34", type=BoemTest_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_BoemTest_A_NamedElement = Generalization(general=NamedElement, specific=BoemTest_A)
gen_BoemTest_B_A = Generalization(general=A, specific=BoemTest_B)
gen_BoemTest_C_B = Generalization(general=B, specific=BoemTest_C)
gen_BoemTest_Node_NamedElement = Generalization(general=NamedElement, specific=BoemTest_Node)

# Domain Model
domain_model = DomainModel(
    name="BoemTest",
    types={BoemTest_A, NamedElement, BoemTest_Node, BoemTest_B, A, BoemTest_BNode, BoemTest_C, B, BoemTest_NamedElement, AnEnumeration},
    associations={childrenNode2A1, childNodeA4, referencesNodeA7, referenceNodeA10, childrenNodeA0, childrenNodeC23, childNodeC25, referencesNodeC28, autoContainementA14, childrenNodeB16, childNodeB18, childrenNodeBNode21, referenceNodeC31, children35},
    generalizations={gen_BoemTest_A_NamedElement, gen_BoemTest_B_A, gen_BoemTest_C_B, gen_BoemTest_Node_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)