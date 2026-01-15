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
dscDiagramModel_AnchorNoteToItem = Class(name="dscDiagramModel::AnchorNoteToItem")
Relationship = Class(name="Relationship")
dscDiagramModel_Transition = Class(name="dscDiagramModel::Transition")
dscDiagramModel_DSCDiagram = Class(name="dscDiagramModel::DSCDiagram")
GenericDiagram = Class(name="GenericDiagram")
dscDiagramModel_StartPoint = Class(name="dscDiagramModel::StartPoint")
Classifier = Class(name="Classifier")
dscDiagramModel_DSCState = Class(name="dscDiagramModel::DSCState")
dscDiagramModel_ShallowHistory = Class(name="dscDiagramModel::ShallowHistory")
dscDiagramModel_DeepHistory = Class(name="dscDiagramModel::DeepHistory")
Container = Class(name="Container")

# dscDiagramModel_AnchorNoteToItem class attributes and methods

# Relationship class attributes and methods

# dscDiagramModel_Transition class attributes and methods
dscDiagramModel_Transition_transitionID: Property = Property(name="transitionID", type=StringType)
dscDiagramModel_Transition_eventID: Property = Property(name="eventID", type=StringType)
dscDiagramModel_Transition_guardID: Property = Property(name="guardID", type=StringType)
dscDiagramModel_Transition_actionID: Property = Property(name="actionID", type=StringType)
dscDiagramModel_Transition_showProperties: Property = Property(name="showProperties", type=BooleanType)
dscDiagramModel_Transition_showTransitionID: Property = Property(name="showTransitionID", type=BooleanType)
dscDiagramModel_Transition_triggeredByEvent: Property = Property(name="triggeredByEvent", type=BooleanType)
dscDiagramModel_Transition.attributes={dscDiagramModel_Transition_transitionID, dscDiagramModel_Transition_showProperties, dscDiagramModel_Transition_actionID, dscDiagramModel_Transition_eventID, dscDiagramModel_Transition_triggeredByEvent, dscDiagramModel_Transition_guardID, dscDiagramModel_Transition_showTransitionID}

# dscDiagramModel_DSCDiagram class attributes and methods
dscDiagramModel_DSCDiagram_eventFile: Property = Property(name="eventFile", type=StringType)
dscDiagramModel_DSCDiagram_guardFile: Property = Property(name="guardFile", type=StringType)
dscDiagramModel_DSCDiagram_actionFile: Property = Property(name="actionFile", type=StringType)
dscDiagramModel_DSCDiagram_diagramVariables: Property = Property(name="diagramVariables", type=StringType)
dscDiagramModel_DSCDiagram_functionFile: Property = Property(name="functionFile", type=StringType)
dscDiagramModel_DSCDiagram.attributes={dscDiagramModel_DSCDiagram_functionFile, dscDiagramModel_DSCDiagram_diagramVariables, dscDiagramModel_DSCDiagram_eventFile, dscDiagramModel_DSCDiagram_actionFile, dscDiagramModel_DSCDiagram_guardFile}

# GenericDiagram class attributes and methods

# dscDiagramModel_StartPoint class attributes and methods

# Classifier class attributes and methods

# dscDiagramModel_DSCState class attributes and methods
dscDiagramModel_DSCState_Variables: Property = Property(name="Variables", type=StringType)
dscDiagramModel_DSCState_isSimple: Property = Property(name="isSimple", type=BooleanType)
dscDiagramModel_DSCState.attributes={dscDiagramModel_DSCState_isSimple, dscDiagramModel_DSCState_Variables}

# dscDiagramModel_ShallowHistory class attributes and methods

# dscDiagramModel_DeepHistory class attributes and methods

# Container class attributes and methods

# Relationships
startPoint5: BinaryAssociation = BinaryAssociation(
    name="startPoint5",
    ends={
        Property(name="StartPoint", type=dscDiagramModel_DSCState, multiplicity=Multiplicity(1, 1)),
        Property(name="compositeState", type=dscDiagramModel_StartPoint, multiplicity=Multiplicity(1, 1))
    }
)
shallowHistory6: BinaryAssociation = BinaryAssociation(
    name="shallowHistory6",
    ends={
        Property(name="ShallowHistory", type=dscDiagramModel_DSCState, multiplicity=Multiplicity(1, 1)),
        Property(name="compositeState7", type=dscDiagramModel_ShallowHistory, multiplicity=Multiplicity(0, 1))
    }
)
deepHistory8: BinaryAssociation = BinaryAssociation(
    name="deepHistory8",
    ends={
        Property(name="DeepHistory", type=dscDiagramModel_DSCState, multiplicity=Multiplicity(1, 1)),
        Property(name="compositeState9", type=dscDiagramModel_DeepHistory, multiplicity=Multiplicity(0, 1))
    }
)
compositeState0: BinaryAssociation = BinaryAssociation(
    name="compositeState0",
    ends={
        Property(name="DSCState", type=dscDiagramModel_StartPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="startPoint", type=dscDiagramModel_DSCState, multiplicity=Multiplicity(1, 1))
    }
)
compositeState1: BinaryAssociation = BinaryAssociation(
    name="compositeState1",
    ends={
        Property(name="DSCState2", type=dscDiagramModel_ShallowHistory, multiplicity=Multiplicity(1, 1)),
        Property(name="shallowHistory", type=dscDiagramModel_DSCState, multiplicity=Multiplicity(1, 1))
    }
)
compositeState3: BinaryAssociation = BinaryAssociation(
    name="compositeState3",
    ends={
        Property(name="DSCState4", type=dscDiagramModel_DeepHistory, multiplicity=Multiplicity(1, 1)),
        Property(name="deepHistory", type=dscDiagramModel_DSCState, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_dscDiagramModel_AnchorNoteToItem_Relationship = Generalization(general=Relationship, specific=dscDiagramModel_AnchorNoteToItem)
gen_dscDiagramModel_Transition_Relationship = Generalization(general=Relationship, specific=dscDiagramModel_Transition)
gen_dscDiagramModel_DSCDiagram_GenericDiagram = Generalization(general=GenericDiagram, specific=dscDiagramModel_DSCDiagram)
gen_dscDiagramModel_StartPoint_Classifier = Generalization(general=Classifier, specific=dscDiagramModel_StartPoint)
gen_dscDiagramModel_ShallowHistory_Classifier = Generalization(general=Classifier, specific=dscDiagramModel_ShallowHistory)
gen_dscDiagramModel_DeepHistory_Classifier = Generalization(general=Classifier, specific=dscDiagramModel_DeepHistory)
gen_dscDiagramModel_DSCState_Container = Generalization(general=Container, specific=dscDiagramModel_DSCState)

# Domain Model
domain_model = DomainModel(
    name="dscDiagramModel",
    types={dscDiagramModel_AnchorNoteToItem, Relationship, dscDiagramModel_Transition, dscDiagramModel_DSCDiagram, GenericDiagram, dscDiagramModel_StartPoint, Classifier, dscDiagramModel_DSCState, dscDiagramModel_ShallowHistory, dscDiagramModel_DeepHistory, Container},
    associations={startPoint5, shallowHistory6, deepHistory8, compositeState0, compositeState1, compositeState3},
    generalizations={gen_dscDiagramModel_AnchorNoteToItem_Relationship, gen_dscDiagramModel_Transition_Relationship, gen_dscDiagramModel_DSCDiagram_GenericDiagram, gen_dscDiagramModel_StartPoint_Classifier, gen_dscDiagramModel_ShallowHistory_Classifier, gen_dscDiagramModel_DeepHistory_Classifier, gen_dscDiagramModel_DSCState_Container},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)