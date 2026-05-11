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
di_Bendpoint = Class(name="di_Bendpoint")
di_Connector = Class(name="di_Connector")
View = Class(name="View")
di_EStringToStringMapEntry = Class(name="di_EStringToStringMapEntry")
di_Diagram = Class(name="di_Diagram")
di_DocumentRoot = Class(name="di_DocumentRoot")
di_View = Class(name="di_View", is_abstract=True)
di_Node = Class(name="di_Node")
di_Style = Class(name="di_Style")

# di_Bendpoint class attributes and methods
di_Bendpoint_sourceX: Property = Property(name="sourceX", type=StringType)
di_Bendpoint_sourceY: Property = Property(name="sourceY", type=StringType)
di_Bendpoint_targetX: Property = Property(name="targetX", type=StringType)
di_Bendpoint_targetY: Property = Property(name="targetY", type=StringType)
di_Bendpoint.attributes={di_Bendpoint_sourceX, di_Bendpoint_targetY, di_Bendpoint_targetX, di_Bendpoint_sourceY}

# di_Connector class attributes and methods
di_Connector_source: Property = Property(name="source", type=StringType)
di_Connector_target: Property = Property(name="target", type=StringType)
di_Connector.attributes={di_Connector_source, di_Connector_target}

# View class attributes and methods

# di_EStringToStringMapEntry class attributes and methods

# di_Diagram class attributes and methods

# di_DocumentRoot class attributes and methods
di_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
di_DocumentRoot.attributes={di_DocumentRoot_mixed}

# di_View class attributes and methods
di_View_id: Property = Property(name="id", type=StringType)
di_View_context: Property = Property(name="context", type=StringType)
di_View_definition: Property = Property(name="definition", type=StringType)
di_View_sourceConnector: Property = Property(name="sourceConnector", type=StringType)
di_View_targetConnector: Property = Property(name="targetConnector", type=StringType)
di_View.attributes={di_View_targetConnector, di_View_definition, di_View_sourceConnector, di_View_context, di_View_id}

# di_Node class attributes and methods

# di_Style class attributes and methods
di_Style_name: Property = Property(name="name", type=StringType)
di_Style_value: Property = Property(name="value", type=StringType)
di_Style.attributes={di_Style_name, di_Style_value}

# Relationships
bendpoint0: BinaryAssociation = BinaryAssociation(
    name="bendpoint0",
    ends={
        Property(name="di_Bendpoint", type=di_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="di_Connector", type=di_Bendpoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xMLNSPrefixMap3: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap3",
    ends={
        Property(name="di_EStringToStringMapEntry", type=di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DocumentRoot", type=di_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connector1: BinaryAssociation = BinaryAssociation(
    name="connector1",
    ends={
        Property(name="di_Connector2", type=di_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="di_Diagram", type=di_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
view13: BinaryAssociation = BinaryAssociation(
    name="view13",
    ends={
        Property(name="di_View", type=di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DocumentRoot14", type=di_View, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation4: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation4",
    ends={
        Property(name="di_EStringToStringMapEntry6", type=di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DocumentRoot5", type=di_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bendpoint7: BinaryAssociation = BinaryAssociation(
    name="bendpoint7",
    ends={
        Property(name="di_Bendpoint9", type=di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DocumentRoot8", type=di_Bendpoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connector10: BinaryAssociation = BinaryAssociation(
    name="connector10",
    ends={
        Property(name="di_Connector12", type=di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DocumentRoot11", type=di_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
diagram15: BinaryAssociation = BinaryAssociation(
    name="diagram15",
    ends={
        Property(name="di_Diagram17", type=di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DocumentRoot16", type=di_Diagram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node18: BinaryAssociation = BinaryAssociation(
    name="node18",
    ends={
        Property(name="di_Node", type=di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DocumentRoot19", type=di_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
style20: BinaryAssociation = BinaryAssociation(
    name="style20",
    ends={
        Property(name="di_Style", type=di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DocumentRoot21", type=di_Style, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
style22: BinaryAssociation = BinaryAssociation(
    name="style22",
    ends={
        Property(name="di_Style24", type=di_View, multiplicity=Multiplicity(1, 1)),
        Property(name="di_View23", type=di_Style, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
child25: BinaryAssociation = BinaryAssociation(
    name="child25",
    ends={
        Property(name="di_Node27", type=di_View, multiplicity=Multiplicity(1, 1)),
        Property(name="di_View26", type=di_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_di_Connector_View = Generalization(general=View, specific=di_Connector)
gen_di_Diagram_View = Generalization(general=View, specific=di_Diagram)
gen_di_Node_View = Generalization(general=View, specific=di_Node)

# Domain Model
domain_model = DomainModel(
    name="di",
    types={di_Bendpoint, di_Connector, View, di_EStringToStringMapEntry, di_Diagram, di_DocumentRoot, di_View, di_Node, di_Style},
    associations={bendpoint0, xMLNSPrefixMap3, connector1, view13, xSISchemaLocation4, bendpoint7, connector10, diagram15, node18, style20, style22, child25},
    generalizations={gen_di_Connector_View, gen_di_Diagram_View, gen_di_Node_View},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)