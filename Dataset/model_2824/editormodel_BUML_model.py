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
editormodel_Diagram = Class(name="editormodel::Diagram", is_abstract=True)
NamedElementModel = Class(name="NamedElementModel")
editormodel_CoreModel = Class(name="editormodel::CoreModel")
editormodel_Note = Class(name="editormodel::Note")
editormodel_VisualModel = Class(name="editormodel::VisualModel")
editormodel_Folder = Class(name="editormodel::Folder")
editormodel_FlabotFileModel = Class(name="editormodel::FlabotFileModel")
ExtensibleElement = Class(name="ExtensibleElement")
editormodel_Dimension = Class(name="editormodel::Dimension")
Adapter = Class(name="Adapter")
editormodel_EObject = Class(name="editormodel::EObject")
editormodel_Point = Class(name="editormodel::Point")
editormodel_NodeVisualModel = Class(name="editormodel::NodeVisualModel")
editormodel_Color = Class(name="editormodel::Color")
editormodel_Adapter = Class(name="editormodel::Adapter", is_abstract=True)
editormodel_ConnectionBendpoint = Class(name="editormodel::ConnectionBendpoint")
editormodel_ConnectionVisualModel = Class(name="editormodel::ConnectionVisualModel")
NodeVisualModel = Class(name="NodeVisualModel")
VisualModel = Class(name="VisualModel")
editormodel_EStringToEObjectMapEntry = Class(name="editormodel::EStringToEObjectMapEntry")
editormodel_VisualDiagramJump = Class(name="editormodel::VisualDiagramJump")

# editormodel_Diagram class attributes and methods
editormodel_Diagram_gridEnabled: Property = Property(name="gridEnabled", type=StringType)
editormodel_Diagram_snapToGeometryEnabled: Property = Property(name="snapToGeometryEnabled", type=StringType)
editormodel_Diagram.attributes={editormodel_Diagram_gridEnabled, editormodel_Diagram_snapToGeometryEnabled}

# NamedElementModel class attributes and methods

# editormodel_CoreModel class attributes and methods

# editormodel_Note class attributes and methods

# editormodel_VisualModel class attributes and methods
editormodel_VisualModel_lineStyle: Property = Property(name="lineStyle", type=IntegerType)
editormodel_VisualModel_lineWidth: Property = Property(name="lineWidth", type=IntegerType)
editormodel_VisualModel_detailLevel: Property = Property(name="detailLevel", type=IntegerType)
editormodel_VisualModel.attributes={editormodel_VisualModel_detailLevel, editormodel_VisualModel_lineWidth, editormodel_VisualModel_lineStyle}

# editormodel_Folder class attributes and methods
editormodel_Folder_name: Property = Property(name="name", type=StringType)
editormodel_Folder.attributes={editormodel_Folder_name}

# editormodel_FlabotFileModel class attributes and methods
editormodel_FlabotFileModel_id: Property = Property(name="id", type=StringType)
editormodel_FlabotFileModel_version: Property = Property(name="version", type=StringType)
editormodel_FlabotFileModel_name: Property = Property(name="name", type=StringType)
editormodel_FlabotFileModel_provider: Property = Property(name="provider", type=StringType)
editormodel_FlabotFileModel.attributes={editormodel_FlabotFileModel_provider, editormodel_FlabotFileModel_version, editormodel_FlabotFileModel_id, editormodel_FlabotFileModel_name}

# ExtensibleElement class attributes and methods

# editormodel_Dimension class attributes and methods
editormodel_Dimension_width: Property = Property(name="width", type=IntegerType)
editormodel_Dimension_height: Property = Property(name="height", type=IntegerType)
editormodel_Dimension.attributes={editormodel_Dimension_width, editormodel_Dimension_height}

# Adapter class attributes and methods

# editormodel_EObject class attributes and methods

# editormodel_Point class attributes and methods
editormodel_Point_x: Property = Property(name="x", type=IntegerType)
editormodel_Point_y: Property = Property(name="y", type=IntegerType)
editormodel_Point.attributes={editormodel_Point_x, editormodel_Point_y}

# editormodel_NodeVisualModel class attributes and methods
editormodel_NodeVisualModel_rotation: Property = Property(name="rotation", type=StringType)
editormodel_NodeVisualModel.attributes={editormodel_NodeVisualModel_rotation}

# editormodel_Color class attributes and methods
editormodel_Color_red: Property = Property(name="red", type=IntegerType)
editormodel_Color_green: Property = Property(name="green", type=IntegerType)
editormodel_Color_blue: Property = Property(name="blue", type=IntegerType)
editormodel_Color.attributes={editormodel_Color_red, editormodel_Color_blue, editormodel_Color_green}

# editormodel_Adapter class attributes and methods

# editormodel_ConnectionBendpoint class attributes and methods
editormodel_ConnectionBendpoint_weight: Property = Property(name="weight", type=FloatType)
editormodel_ConnectionBendpoint.attributes={editormodel_ConnectionBendpoint_weight}

# editormodel_ConnectionVisualModel class attributes and methods
editormodel_ConnectionVisualModel_sourceTerminal: Property = Property(name="sourceTerminal", type=StringType)
editormodel_ConnectionVisualModel_targetTerminal: Property = Property(name="targetTerminal", type=StringType)
editormodel_ConnectionVisualModel.attributes={editormodel_ConnectionVisualModel_targetTerminal, editormodel_ConnectionVisualModel_sourceTerminal}

# NodeVisualModel class attributes and methods

# VisualModel class attributes and methods

# editormodel_EStringToEObjectMapEntry class attributes and methods
editormodel_EStringToEObjectMapEntry_key: Property = Property(name="key", type=StringType)
editormodel_EStringToEObjectMapEntry.attributes={editormodel_EStringToEObjectMapEntry_key}

# editormodel_VisualDiagramJump class attributes and methods
editormodel_VisualDiagramJump_to: Property = Property(name="to", type=StringType)
editormodel_VisualDiagramJump.attributes={editormodel_VisualDiagramJump_to}

# Relationships
coreModel5: BinaryAssociation = BinaryAssociation(
    name="coreModel5",
    ends={
        Property(name="file", type=editormodel_CoreModel, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="coremodel.ecoreCoreModel", type=editormodel_FlabotFileModel, multiplicity=Multiplicity(1, 1))
    }
)
diagrams6: BinaryAssociation = BinaryAssociation(
    name="diagrams6",
    ends={
        Property(name="editormodel_Diagram7", type=editormodel_FlabotFileModel, multiplicity=Multiplicity(1, 1)),
        Property(name="editormodel_FlabotFileModel", type=editormodel_Diagram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedFiles9: BinaryAssociation = BinaryAssociation(
    name="importedFiles9",
    ends={
        Property(name="editormodel_FlabotFileModel10", type=editormodel_FlabotFileModel, multiplicity=Multiplicity(1, 1)),
        Property(name="editormodel_FlabotFileModel8", type=editormodel_FlabotFileModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
coreModel0: BinaryAssociation = BinaryAssociation(
    name="coreModel0",
    ends={
        Property(name="editormodel_CoreModel", type=editormodel_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="editormodel_Diagram", type=editormodel_CoreModel, multiplicity=Multiplicity(0, 1))
    }
)
notes1: BinaryAssociation = BinaryAssociation(
    name="notes1",
    ends={
        Property(name="editormodel_Note", type=editormodel_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="editormodel_Diagram2", type=editormodel_Note, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children3: BinaryAssociation = BinaryAssociation(
    name="children3",
    ends={
        Property(name="VisualModel", type=editormodel_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram", type=editormodel_VisualModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
folder4: BinaryAssociation = BinaryAssociation(
    name="folder4",
    ends={
        Property(name="Folder", type=editormodel_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagrams", type=editormodel_Folder, multiplicity=Multiplicity(0, 1))
    }
)
location23: BinaryAssociation = BinaryAssociation(
    name="location23",
    ends={
        Property(name="editormodel_VisualModel24", type=editormodel_Point, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="editormodel_Point", type=editormodel_VisualModel, multiplicity=Multiplicity(1, 1))
    }
)
size25: BinaryAssociation = BinaryAssociation(
    name="size25",
    ends={
        Property(name="editormodel_Dimension", type=editormodel_VisualModel, multiplicity=Multiplicity(1, 1)),
        Property(name="editormodel_VisualModel26", type=editormodel_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
diagram27: BinaryAssociation = BinaryAssociation(
    name="diagram27",
    ends={
        Property(name="Diagram", type=editormodel_VisualModel, multiplicity=Multiplicity(1, 1)),
        Property(name="children28", type=editormodel_Diagram, multiplicity=Multiplicity(0, 1))
    }
)
folder11: BinaryAssociation = BinaryAssociation(
    name="folder11",
    ends={
        Property(name="editormodel_Folder", type=editormodel_FlabotFileModel, multiplicity=Multiplicity(1, 1)),
        Property(name="editormodel_FlabotFileModel12", type=editormodel_Folder, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
openDiagrams13: BinaryAssociation = BinaryAssociation(
    name="openDiagrams13",
    ends={
        Property(name="editormodel_Diagram15", type=editormodel_FlabotFileModel, multiplicity=Multiplicity(1, 1)),
        Property(name="editormodel_FlabotFileModel14", type=editormodel_Diagram, multiplicity=Multiplicity(0, 9999))
    }
)
children17: BinaryAssociation = BinaryAssociation(
    name="children17",
    ends={
        Property(name="VisualModel18", type=editormodel_VisualModel, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=editormodel_VisualModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent20: BinaryAssociation = BinaryAssociation(
    name="parent20",
    ends={
        Property(name="VisualModel21", type=editormodel_VisualModel, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=editormodel_VisualModel, multiplicity=Multiplicity(0, 1))
    }
)
semanticModel22: BinaryAssociation = BinaryAssociation(
    name="semanticModel22",
    ends={
        Property(name="editormodel_EObject", type=editormodel_VisualModel, multiplicity=Multiplicity(1, 1)),
        Property(name="editormodel_VisualModel", type=editormodel_EObject, multiplicity=Multiplicity(0, 1))
    }
)
bendpoints39: BinaryAssociation = BinaryAssociation(
    name="bendpoints39",
    ends={
        Property(name="editormodel_ConnectionBendpoint40", type=editormodel_ConnectionVisualModel, multiplicity=Multiplicity(1, 1)),
        Property(name="editormodel_ConnectionVisualModel", type=editormodel_ConnectionBendpoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source41: BinaryAssociation = BinaryAssociation(
    name="source41",
    ends={
        Property(name="NodeVisualModel", type=editormodel_ConnectionVisualModel, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceConnections", type=editormodel_NodeVisualModel, multiplicity=Multiplicity(0, 1))
    }
)
backgroundColor29: BinaryAssociation = BinaryAssociation(
    name="backgroundColor29",
    ends={
        Property(name="editormodel_Color", type=editormodel_VisualModel, multiplicity=Multiplicity(1, 1)),
        Property(name="editormodel_VisualModel30", type=editormodel_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
foregroundColor31: BinaryAssociation = BinaryAssociation(
    name="foregroundColor31",
    ends={
        Property(name="editormodel_Color33", type=editormodel_VisualModel, multiplicity=Multiplicity(1, 1)),
        Property(name="editormodel_VisualModel32", type=editormodel_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
firstRelativeDimension34: BinaryAssociation = BinaryAssociation(
    name="firstRelativeDimension34",
    ends={
        Property(name="editormodel_Dimension35", type=editormodel_ConnectionBendpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="editormodel_ConnectionBendpoint", type=editormodel_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
secondRelativeDimension36: BinaryAssociation = BinaryAssociation(
    name="secondRelativeDimension36",
    ends={
        Property(name="editormodel_Dimension38", type=editormodel_ConnectionBendpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="editormodel_ConnectionBendpoint37", type=editormodel_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target42: BinaryAssociation = BinaryAssociation(
    name="target42",
    ends={
        Property(name="NodeVisualModel43", type=editormodel_ConnectionVisualModel, multiplicity=Multiplicity(1, 1)),
        Property(name="targetConnections", type=editormodel_NodeVisualModel, multiplicity=Multiplicity(0, 1))
    }
)
sourceConnections44: BinaryAssociation = BinaryAssociation(
    name="sourceConnections44",
    ends={
        Property(name="ConnectionVisualModel", type=editormodel_NodeVisualModel, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=editormodel_ConnectionVisualModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value59: BinaryAssociation = BinaryAssociation(
    name="value59",
    ends={
        Property(name="editormodel_EObject60", type=editormodel_EStringToEObjectMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="editormodel_EStringToEObjectMapEntry", type=editormodel_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetConnections45: BinaryAssociation = BinaryAssociation(
    name="targetConnections45",
    ends={
        Property(name="ConnectionVisualModel46", type=editormodel_NodeVisualModel, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=editormodel_ConnectionVisualModel, multiplicity=Multiplicity(0, 9999))
    }
)
sourceDiagram61: BinaryAssociation = BinaryAssociation(
    name="sourceDiagram61",
    ends={
        Property(name="editormodel_Diagram62", type=editormodel_VisualDiagramJump, multiplicity=Multiplicity(1, 1)),
        Property(name="editormodel_VisualDiagramJump", type=editormodel_Diagram, multiplicity=Multiplicity(0, 1))
    }
)
targetDiagram63: BinaryAssociation = BinaryAssociation(
    name="targetDiagram63",
    ends={
        Property(name="editormodel_Diagram65", type=editormodel_VisualDiagramJump, multiplicity=Multiplicity(1, 1)),
        Property(name="editormodel_VisualDiagramJump64", type=editormodel_Diagram, multiplicity=Multiplicity(0, 1))
    }
)
folders48: BinaryAssociation = BinaryAssociation(
    name="folders48",
    ends={
        Property(name="Folder50", type=editormodel_Folder, multiplicity=Multiplicity(1, 1)),
        Property(name="parent49", type=editormodel_Folder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
diagrams51: BinaryAssociation = BinaryAssociation(
    name="diagrams51",
    ends={
        Property(name="Diagram52", type=editormodel_Folder, multiplicity=Multiplicity(1, 1)),
        Property(name="folder", type=editormodel_Diagram, multiplicity=Multiplicity(0, 9999))
    }
)
parent54: BinaryAssociation = BinaryAssociation(
    name="parent54",
    ends={
        Property(name="Folder55", type=editormodel_Folder, multiplicity=Multiplicity(1, 1)),
        Property(name="folders", type=editormodel_Folder, multiplicity=Multiplicity(0, 1))
    }
)
fileModel56: BinaryAssociation = BinaryAssociation(
    name="fileModel56",
    ends={
        Property(name="editormodel_FlabotFileModel58", type=editormodel_Folder, multiplicity=Multiplicity(1, 1)),
        Property(name="editormodel_Folder57", type=editormodel_FlabotFileModel, multiplicity=Multiplicity(0, 1))
    }
)
targetVisualNode66: BinaryAssociation = BinaryAssociation(
    name="targetVisualNode66",
    ends={
        Property(name="editormodel_NodeVisualModel", type=editormodel_VisualDiagramJump, multiplicity=Multiplicity(1, 1)),
        Property(name="editormodel_VisualDiagramJump67", type=editormodel_NodeVisualModel, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_editormodel_Diagram_NamedElementModel = Generalization(general=NamedElementModel, specific=editormodel_Diagram)
gen_editormodel_FlabotFileModel_ExtensibleElement = Generalization(general=ExtensibleElement, specific=editormodel_FlabotFileModel)
gen_editormodel_VisualModel_Adapter = Generalization(general=Adapter, specific=editormodel_VisualModel)
gen_editormodel_ConnectionVisualModel_NodeVisualModel = Generalization(general=NodeVisualModel, specific=editormodel_ConnectionVisualModel)
gen_editormodel_NodeVisualModel_VisualModel = Generalization(general=VisualModel, specific=editormodel_NodeVisualModel)
gen_editormodel_VisualDiagramJump_NodeVisualModel = Generalization(general=NodeVisualModel, specific=editormodel_VisualDiagramJump)

# Domain Model
domain_model = DomainModel(
    name="editormodel",
    types={editormodel_Diagram, NamedElementModel, editormodel_CoreModel, editormodel_Note, editormodel_VisualModel, editormodel_Folder, editormodel_FlabotFileModel, ExtensibleElement, editormodel_Dimension, Adapter, editormodel_EObject, editormodel_Point, editormodel_NodeVisualModel, editormodel_Color, editormodel_Adapter, editormodel_ConnectionBendpoint, editormodel_ConnectionVisualModel, NodeVisualModel, VisualModel, editormodel_EStringToEObjectMapEntry, editormodel_VisualDiagramJump},
    associations={coreModel5, diagrams6, importedFiles9, coreModel0, notes1, children3, folder4, location23, size25, diagram27, folder11, openDiagrams13, children17, parent20, semanticModel22, bendpoints39, source41, backgroundColor29, foregroundColor31, firstRelativeDimension34, secondRelativeDimension36, target42, sourceConnections44, value59, targetConnections45, sourceDiagram61, targetDiagram63, folders48, diagrams51, parent54, fileModel56, targetVisualNode66},
    generalizations={gen_editormodel_Diagram_NamedElementModel, gen_editormodel_FlabotFileModel_ExtensibleElement, gen_editormodel_VisualModel_Adapter, gen_editormodel_ConnectionVisualModel_NodeVisualModel, gen_editormodel_NodeVisualModel_VisualModel, gen_editormodel_VisualDiagramJump_NodeVisualModel},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)