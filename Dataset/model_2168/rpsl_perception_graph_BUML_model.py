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
rpslPerceptionGraphMetaModel_PerceptionGraph = Class(name="rpslPerceptionGraphMetaModel::PerceptionGraph")
rpslPerceptionGraphMetaModel_Element = Class(name="rpslPerceptionGraphMetaModel::Element")
rpslPerceptionGraphMetaModel_Prototype = Class(name="rpslPerceptionGraphMetaModel::Prototype")
rpslPerceptionGraphMetaModel_Component = Class(name="rpslPerceptionGraphMetaModel::Component")
rpslPerceptionGraphMetaModel_Leaf = Class(name="rpslPerceptionGraphMetaModel::Leaf")
Element = Class(name="Element")
rpslPerceptionGraphMetaModel_Node = Class(name="rpslPerceptionGraphMetaModel::Node")
rpslPerceptionGraphMetaModel_Connection = Class(name="rpslPerceptionGraphMetaModel::Connection")
rpslPerceptionGraphMetaModel_InputPort = Class(name="rpslPerceptionGraphMetaModel::InputPort")
rpslPerceptionGraphMetaModel_OutputPort = Class(name="rpslPerceptionGraphMetaModel::OutputPort")

# rpslPerceptionGraphMetaModel_PerceptionGraph class attributes and methods
rpslPerceptionGraphMetaModel_PerceptionGraph_name: Property = Property(name="name", type=StringType)
rpslPerceptionGraphMetaModel_PerceptionGraph_uuid: Property = Property(name="uuid", type=StringType)
rpslPerceptionGraphMetaModel_PerceptionGraph_doc: Property = Property(name="doc", type=StringType)
rpslPerceptionGraphMetaModel_PerceptionGraph.attributes={rpslPerceptionGraphMetaModel_PerceptionGraph_uuid, rpslPerceptionGraphMetaModel_PerceptionGraph_doc, rpslPerceptionGraphMetaModel_PerceptionGraph_name}

# rpslPerceptionGraphMetaModel_Element class attributes and methods
rpslPerceptionGraphMetaModel_Element_name: Property = Property(name="name", type=StringType)
rpslPerceptionGraphMetaModel_Element_doc: Property = Property(name="doc", type=StringType)
rpslPerceptionGraphMetaModel_Element.attributes={rpslPerceptionGraphMetaModel_Element_name, rpslPerceptionGraphMetaModel_Element_doc}

# rpslPerceptionGraphMetaModel_Prototype class attributes and methods

# rpslPerceptionGraphMetaModel_Component class attributes and methods

# rpslPerceptionGraphMetaModel_Leaf class attributes and methods

# Element class attributes and methods

# rpslPerceptionGraphMetaModel_Node class attributes and methods

# rpslPerceptionGraphMetaModel_Connection class attributes and methods

# rpslPerceptionGraphMetaModel_InputPort class attributes and methods

# rpslPerceptionGraphMetaModel_OutputPort class attributes and methods

# Relationships
element0: BinaryAssociation = BinaryAssociation(
    name="element0",
    ends={
        Property(name="rpslPerceptionGraphMetaModel_PerceptionGraph", type=rpslPerceptionGraphMetaModel_Element, multiplicity=Multiplicity(1, 9999), is_composite=True),
        Property(name="rpslPerceptionGraphMetaModel_Element", type=rpslPerceptionGraphMetaModel_PerceptionGraph, multiplicity=Multiplicity(1, 1))
    }
)
perception_graph_property_prototype1: BinaryAssociation = BinaryAssociation(
    name="perception_graph_property_prototype1",
    ends={
        Property(name="rpslPerceptionGraphMetaModel_Prototype", type=rpslPerceptionGraphMetaModel_PerceptionGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="rpslPerceptionGraphMetaModel_PerceptionGraph2", type=rpslPerceptionGraphMetaModel_Prototype, multiplicity=Multiplicity(0, 9999))
    }
)
component3: BinaryAssociation = BinaryAssociation(
    name="component3",
    ends={
        Property(name="rpslPerceptionGraphMetaModel_Component", type=rpslPerceptionGraphMetaModel_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="rpslPerceptionGraphMetaModel_Element4", type=rpslPerceptionGraphMetaModel_Component, multiplicity=Multiplicity(1, 1))
    }
)
connection5: BinaryAssociation = BinaryAssociation(
    name="connection5",
    ends={
        Property(name="rpslPerceptionGraphMetaModel_Connection", type=rpslPerceptionGraphMetaModel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="rpslPerceptionGraphMetaModel_Node", type=rpslPerceptionGraphMetaModel_Connection, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
element6: BinaryAssociation = BinaryAssociation(
    name="element6",
    ends={
        Property(name="rpslPerceptionGraphMetaModel_Element8", type=rpslPerceptionGraphMetaModel_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="rpslPerceptionGraphMetaModel_Connection7", type=rpslPerceptionGraphMetaModel_Element, multiplicity=Multiplicity(1, 1))
    }
)
sink9: BinaryAssociation = BinaryAssociation(
    name="sink9",
    ends={
        Property(name="rpslPerceptionGraphMetaModel_InputPort", type=rpslPerceptionGraphMetaModel_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="rpslPerceptionGraphMetaModel_Connection10", type=rpslPerceptionGraphMetaModel_InputPort, multiplicity=Multiplicity(1, 1))
    }
)
src11: BinaryAssociation = BinaryAssociation(
    name="src11",
    ends={
        Property(name="rpslPerceptionGraphMetaModel_OutputPort", type=rpslPerceptionGraphMetaModel_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="rpslPerceptionGraphMetaModel_Connection12", type=rpslPerceptionGraphMetaModel_OutputPort, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_rpslPerceptionGraphMetaModel_Leaf_Element = Generalization(general=Element, specific=rpslPerceptionGraphMetaModel_Leaf)
gen_rpslPerceptionGraphMetaModel_Node_Element = Generalization(general=Element, specific=rpslPerceptionGraphMetaModel_Node)

# Domain Model
domain_model = DomainModel(
    name="rpslPerceptionGraphMetaModel",
    types={rpslPerceptionGraphMetaModel_PerceptionGraph, rpslPerceptionGraphMetaModel_Element, rpslPerceptionGraphMetaModel_Prototype, rpslPerceptionGraphMetaModel_Component, rpslPerceptionGraphMetaModel_Leaf, Element, rpslPerceptionGraphMetaModel_Node, rpslPerceptionGraphMetaModel_Connection, rpslPerceptionGraphMetaModel_InputPort, rpslPerceptionGraphMetaModel_OutputPort},
    associations={element0, perception_graph_property_prototype1, component3, connection5, element6, sink9, src11},
    generalizations={gen_rpslPerceptionGraphMetaModel_Leaf_Element, gen_rpslPerceptionGraphMetaModel_Node_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)