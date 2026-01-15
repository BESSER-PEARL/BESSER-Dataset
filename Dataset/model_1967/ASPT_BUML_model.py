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
ASPT_TraceModel = Class(name="ASPT::TraceModel")
ASPT_TraceLink = Class(name="ASPT::TraceLink")
ASPT_TraceElement = Class(name="ASPT::TraceElement")
TraceElement = Class(name="TraceElement")
ASPT_TraceNode = Class(name="ASPT::TraceNode")
ASPT_TraceProp = Class(name="ASPT::TraceProp")
ASPT_TraceEdge = Class(name="ASPT::TraceEdge")
ASPT_TraceNbNode = Class(name="ASPT::TraceNbNode")
TraceNode = Class(name="TraceNode")
ASPT_TraceNbProp = Class(name="ASPT::TraceNbProp")
TraceProp = Class(name="TraceProp")
ASPT_TraceNbEdge = Class(name="ASPT::TraceNbEdge")
TraceEdge = Class(name="TraceEdge")

# ASPT_TraceModel class attributes and methods
ASPT_TraceModel_ID: Property = Property(name="ID", type=StringType)
ASPT_TraceModel_MMS: Property = Property(name="MMS", type=StringType)
ASPT_TraceModel.attributes={ASPT_TraceModel_MMS, ASPT_TraceModel_ID}

# ASPT_TraceLink class attributes and methods
ASPT_TraceLink_relation: Property = Property(name="relation", type=StringType)
ASPT_TraceLink_idref: Property = Property(name="idref", type=StringType)
ASPT_TraceLink_idrefx: Property = Property(name="idrefx", type=StringType)
ASPT_TraceLink.attributes={ASPT_TraceLink_idref, ASPT_TraceLink_idrefx, ASPT_TraceLink_relation}

# ASPT_TraceElement class attributes and methods
ASPT_TraceElement_metamodel: Property = Property(name="metamodel", type=StringType)
ASPT_TraceElement_id: Property = Property(name="id", type=StringType)
ASPT_TraceElement_idx: Property = Property(name="idx", type=StringType)
ASPT_TraceElement_type: Property = Property(name="type", type=StringType)
ASPT_TraceElement.attributes={ASPT_TraceElement_metamodel, ASPT_TraceElement_type, ASPT_TraceElement_id, ASPT_TraceElement_idx}

# TraceElement class attributes and methods

# ASPT_TraceNode class attributes and methods

# ASPT_TraceProp class attributes and methods
ASPT_TraceProp_idp: Property = Property(name="idp", type=StringType)
ASPT_TraceProp_idpx: Property = Property(name="idpx", type=StringType)
ASPT_TraceProp_value: Property = Property(name="value", type=StringType)
ASPT_TraceProp.attributes={ASPT_TraceProp_value, ASPT_TraceProp_idp, ASPT_TraceProp_idpx}

# ASPT_TraceEdge class attributes and methods
ASPT_TraceEdge_ids: Property = Property(name="ids", type=StringType)
ASPT_TraceEdge_idsx: Property = Property(name="idsx", type=StringType)
ASPT_TraceEdge_idt: Property = Property(name="idt", type=StringType)
ASPT_TraceEdge_idtx: Property = Property(name="idtx", type=StringType)
ASPT_TraceEdge.attributes={ASPT_TraceEdge_ids, ASPT_TraceEdge_idtx, ASPT_TraceEdge_idsx, ASPT_TraceEdge_idt}

# ASPT_TraceNbNode class attributes and methods

# TraceNode class attributes and methods

# ASPT_TraceNbProp class attributes and methods

# TraceProp class attributes and methods

# ASPT_TraceNbEdge class attributes and methods

# TraceEdge class attributes and methods

# Relationships
tracelinks0: BinaryAssociation = BinaryAssociation(
    name="tracelinks0",
    ends={
        Property(name="ASPT_TraceLink", type=ASPT_TraceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="ASPT_TraceModel", type=ASPT_TraceLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
traceelements1: BinaryAssociation = BinaryAssociation(
    name="traceelements1",
    ends={
        Property(name="ASPT_TraceElement", type=ASPT_TraceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="ASPT_TraceModel2", type=ASPT_TraceElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_ASPT_TraceLink_TraceElement = Generalization(general=TraceElement, specific=ASPT_TraceLink)
gen_ASPT_TraceNode_TraceElement = Generalization(general=TraceElement, specific=ASPT_TraceNode)
gen_ASPT_TraceProp_TraceElement = Generalization(general=TraceElement, specific=ASPT_TraceProp)
gen_ASPT_TraceEdge_TraceElement = Generalization(general=TraceElement, specific=ASPT_TraceEdge)
gen_ASPT_TraceNbNode_TraceNode = Generalization(general=TraceNode, specific=ASPT_TraceNbNode)
gen_ASPT_TraceNbProp_TraceProp = Generalization(general=TraceProp, specific=ASPT_TraceNbProp)
gen_ASPT_TraceNbEdge_TraceEdge = Generalization(general=TraceEdge, specific=ASPT_TraceNbEdge)

# Domain Model
domain_model = DomainModel(
    name="ASPT",
    types={ASPT_TraceModel, ASPT_TraceLink, ASPT_TraceElement, TraceElement, ASPT_TraceNode, ASPT_TraceProp, ASPT_TraceEdge, ASPT_TraceNbNode, TraceNode, ASPT_TraceNbProp, TraceProp, ASPT_TraceNbEdge, TraceEdge},
    associations={tracelinks0, traceelements1},
    generalizations={gen_ASPT_TraceLink_TraceElement, gen_ASPT_TraceNode_TraceElement, gen_ASPT_TraceProp_TraceElement, gen_ASPT_TraceEdge_TraceElement, gen_ASPT_TraceNbNode_TraceNode, gen_ASPT_TraceNbProp_TraceProp, gen_ASPT_TraceNbEdge_TraceEdge},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)