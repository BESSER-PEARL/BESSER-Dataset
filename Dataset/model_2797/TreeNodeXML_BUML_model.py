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
TreeNodeXML_XMLTreeNode = Class(name="TreeNodeXML::XMLTreeNode")
TreeNodeXML_TreeNodeAtom = Class(name="TreeNodeXML::TreeNodeAtom")

# TreeNodeXML_XMLTreeNode class attributes and methods
TreeNodeXML_XMLTreeNode_LocalName: Property = Property(name="LocalName", type=StringType)
TreeNodeXML_XMLTreeNode_ElementText: Property = Property(name="ElementText", type=StringType)
TreeNodeXML_XMLTreeNode_m_addTreeNodeAtom: Method = Method(name="addTreeNodeAtom", parameters={Parameter(name='nodeAtom')})
TreeNodeXML_XMLTreeNode_m_addChild: Method = Method(name="addChild", parameters={Parameter(name='newChild')})
TreeNodeXML_XMLTreeNode.attributes={TreeNodeXML_XMLTreeNode_LocalName, TreeNodeXML_XMLTreeNode_ElementText}
TreeNodeXML_XMLTreeNode.methods={TreeNodeXML_XMLTreeNode_m_addChild, TreeNodeXML_XMLTreeNode_m_addTreeNodeAtom}

# TreeNodeXML_TreeNodeAtom class attributes and methods
TreeNodeXML_TreeNodeAtom_AttributeLocalName: Property = Property(name="AttributeLocalName", type=StringType)
TreeNodeXML_TreeNodeAtom_AttributeValue: Property = Property(name="AttributeValue", type=StringType)
TreeNodeXML_TreeNodeAtom.attributes={TreeNodeXML_TreeNodeAtom_AttributeLocalName, TreeNodeXML_TreeNodeAtom_AttributeValue}

# Relationships
children1: BinaryAssociation = BinaryAssociation(
    name="children1",
    ends={
        Property(name="TreeNodeXML_XMLTreeNode", type=TreeNodeXML_XMLTreeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="TreeNodeXML_XMLTreeNode0", type=TreeNodeXML_XMLTreeNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values2: BinaryAssociation = BinaryAssociation(
    name="values2",
    ends={
        Property(name="TreeNodeXML_TreeNodeAtom", type=TreeNodeXML_XMLTreeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="TreeNodeXML_XMLTreeNode3", type=TreeNodeXML_TreeNodeAtom, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="TreeNodeXML",
    types={TreeNodeXML_XMLTreeNode, TreeNodeXML_TreeNodeAtom},
    associations={children1, values2},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)