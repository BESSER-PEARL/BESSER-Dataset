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
itemflow101_Port = Class(name="itemflow101_Port", is_abstract=True)
itemflow101_Function = Class(name="itemflow101_Function")
ProcessNode = Class(name="ProcessNode")
itemflow101_Flow = Class(name="itemflow101_Flow")
itemflow101_OutputPort = Class(name="itemflow101_OutputPort")
itemflow101_InputPort = Class(name="itemflow101_InputPort")
itemflow101_Description = Class(name="itemflow101_Description")
itemflow101_Item = Class(name="itemflow101_Item")
Port = Class(name="Port")
itemflow101_ProcessNode = Class(name="itemflow101_ProcessNode", is_abstract=True)

# itemflow101_Port class attributes and methods
itemflow101_Port_id: Property = Property(name="id", type=StringType)
itemflow101_Port.attributes={itemflow101_Port_id}

# itemflow101_Function class attributes and methods

# ProcessNode class attributes and methods

# itemflow101_Flow class attributes and methods

# itemflow101_OutputPort class attributes and methods

# itemflow101_InputPort class attributes and methods

# itemflow101_Description class attributes and methods
itemflow101_Description_content: Property = Property(name="content", type=StringType)
itemflow101_Description.attributes={itemflow101_Description_content}

# itemflow101_Item class attributes and methods
itemflow101_Item_name: Property = Property(name="name", type=StringType)
itemflow101_Item.attributes={itemflow101_Item_name}

# Port class attributes and methods

# itemflow101_ProcessNode class attributes and methods
itemflow101_ProcessNode_label: Property = Property(name="label", type=StringType)
itemflow101_ProcessNode.attributes={itemflow101_ProcessNode_label}

# Relationships
items13: BinaryAssociation = BinaryAssociation(
    name="items13",
    ends={
        Property(name="itemflow101_Item", type=itemflow101_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="itemflow101_Flow14", type=itemflow101_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
flows0: BinaryAssociation = BinaryAssociation(
    name="flows0",
    ends={
        Property(name="itemflow101_Flow", type=itemflow101_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="itemflow101_Function", type=itemflow101_Flow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
decompositions2: BinaryAssociation = BinaryAssociation(
    name="decompositions2",
    ends={
        Property(name="itemflow101_Function3", type=itemflow101_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="itemflow101_Function1", type=itemflow101_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputPorts4: BinaryAssociation = BinaryAssociation(
    name="outputPorts4",
    ends={
        Property(name="itemflow101_OutputPort", type=itemflow101_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="itemflow101_Function5", type=itemflow101_OutputPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputPorts6: BinaryAssociation = BinaryAssociation(
    name="inputPorts6",
    ends={
        Property(name="itemflow101_InputPort", type=itemflow101_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="itemflow101_Function7", type=itemflow101_InputPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
descriptions8: BinaryAssociation = BinaryAssociation(
    name="descriptions8",
    ends={
        Property(name="itemflow101_Description", type=itemflow101_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="itemflow101_Function9", type=itemflow101_Description, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputflowEdge10: BinaryAssociation = BinaryAssociation(
    name="inputflowEdge10",
    ends={
        Property(name="itemflow101_InputPort12", type=itemflow101_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="itemflow101_Flow11", type=itemflow101_InputPort, multiplicity=Multiplicity(0, 9999))
    }
)
outputflowEdge15: BinaryAssociation = BinaryAssociation(
    name="outputflowEdge15",
    ends={
        Property(name="itemflow101_Flow17", type=itemflow101_OutputPort, multiplicity=Multiplicity(1, 1)),
        Property(name="itemflow101_OutputPort16", type=itemflow101_Flow, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_itemflow101_Function_ProcessNode = Generalization(general=ProcessNode, specific=itemflow101_Function)
gen_itemflow101_Flow_ProcessNode = Generalization(general=ProcessNode, specific=itemflow101_Flow)
gen_itemflow101_OutputPort_Port = Generalization(general=Port, specific=itemflow101_OutputPort)
gen_itemflow101_InputPort_Port = Generalization(general=Port, specific=itemflow101_InputPort)

# Domain Model
domain_model = DomainModel(
    name="itemflow101",
    types={itemflow101_Port, itemflow101_Function, ProcessNode, itemflow101_Flow, itemflow101_OutputPort, itemflow101_InputPort, itemflow101_Description, itemflow101_Item, Port, itemflow101_ProcessNode},
    associations={items13, flows0, decompositions2, outputPorts4, inputPorts6, descriptions8, inputflowEdge10, outputflowEdge15},
    generalizations={gen_itemflow101_Function_ProcessNode, gen_itemflow101_Flow_ProcessNode, gen_itemflow101_OutputPort_Port, gen_itemflow101_InputPort_Port},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)