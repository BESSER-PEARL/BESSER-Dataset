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
Model_Tile = Class(name="Model_Tile")
Model_Chunk = Class(name="Model_Chunk")
Model_World = Class(name="Model_World")
Model_WorldGenerator = Class(name="Model_WorldGenerator")
View_View = Class(name="View_View")
View_Renderer_Interface = Class(name="View_Renderer_Interface")
View_SDLRenderer = Class(name="View_SDLRenderer")
View_Interface_Interface = Class(name="View_Interface_Interface")
View_Texture_Interface = Class(name="View_Texture_Interface")
View_SDLTexture = Class(name="View_SDLTexture")
View_SDLCamera = Class(name="View_SDLCamera")
View_Camera_Interface = Class(name="View_Camera_Interface")
Controller_Parser = Class(name="Controller_Parser")
Controller_SDLInputController = Class(name="Controller_SDLInputController")
Controller_InputController_Interface = Class(name="Controller_InputController_Interface")
Controller_Controller = Class(name="Controller_Controller")
Controller_Event_union_ = Class(name="Controller_Event_union_")
Controller_EventManager = Class(name="Controller_EventManager")
Table1 = Class(name="Table1")
Table2 = Class(name="Table2")
trans_Table = Class(name="trans_Table")
Table3 = Class(name="Table3")
AbstractProperty = Class(name="AbstractProperty", is_abstract=True)
Entity = Class(name="Entity")
AbstractBehavior = Class(name="AbstractBehavior", is_abstract=True)

# Model_Tile class attributes and methods
Model_Tile_type: Property = Property(name="type", type=IntegerType)
Model_Tile_mod: Property = Property(name="mod", type=IntegerType)
Model_Tile_id: Property = Property(name="id", type=IntegerType)
Model_Tile_position: Property = Property(name="position", type=StringType)
Model_Tile.attributes={Model_Tile_mod, Model_Tile_type, Model_Tile_position, Model_Tile_id}

# Model_Chunk class attributes and methods

# Model_World class attributes and methods

# Model_WorldGenerator class attributes and methods

# View_View class attributes and methods
View_View_worldAccess: Property = Property(name="worldAccess", type=Model_World)
View_View_renderer: Property = Property(name="renderer", type=View_Renderer_Interface)
View_View.attributes={View_View_worldAccess, View_View_renderer}

# View_Renderer_Interface class attributes and methods

# View_SDLRenderer class attributes and methods
View_SDLRenderer_viewPointer: Property = Property(name="viewPointer", type=View_View)
View_SDLRenderer_tileset: Property = Property(name="tileset", type=View_SDLTexture)
View_SDLRenderer_camera: Property = Property(name="camera", type=View_SDLCamera)
View_SDLRenderer_window: Property = Property(name="window", type=StringType)
View_SDLRenderer_renderer: Property = Property(name="renderer", type=StringType)
View_SDLRenderer.attributes={View_SDLRenderer_tileset, View_SDLRenderer_renderer, View_SDLRenderer_viewPointer, View_SDLRenderer_window, View_SDLRenderer_camera}

# View_Interface_Interface class attributes and methods

# View_Texture_Interface class attributes and methods

# View_SDLTexture class attributes and methods

# View_SDLCamera class attributes and methods

# View_Camera_Interface class attributes and methods

# Controller_Parser class attributes and methods

# Controller_SDLInputController class attributes and methods
Controller_SDLInputController_controllerPointer: Property = Property(name="controllerPointer", type=Controller_Controller)
Controller_SDLInputController_eventList: Property = Property(name="eventList", type=StringType)
Controller_SDLInputController.attributes={Controller_SDLInputController_controllerPointer, Controller_SDLInputController_eventList}

# Controller_InputController_Interface class attributes and methods

# Controller_Controller class attributes and methods
Controller_Controller_worldAccess: Property = Property(name="worldAccess", type=Model_World)
Controller_Controller_viewAccess: Property = Property(name="viewAccess", type=View_View)
Controller_Controller_inputController: Property = Property(name="inputController", type=Controller_InputController_Interface)
Controller_Controller_eventManager: Property = Property(name="eventManager", type=Controller_EventManager)
Controller_Controller_attribute: Property = Property(name="attribute", type=StringType)
Controller_Controller.attributes={Controller_Controller_inputController, Controller_Controller_worldAccess, Controller_Controller_eventManager, Controller_Controller_viewAccess, Controller_Controller_attribute}

# Controller_Event_union_ class attributes and methods
Controller_Event_union__eventType: Property = Property(name="eventType", type=StringType)
Controller_Event_union__EventEmpty: Property = Property(name="EventEmpty", type=StringType)
Controller_Event_union__EvenkKeyboard: Property = Property(name="EvenkKeyboard", type=StringType)
Controller_Event_union__EventMouseButton: Property = Property(name="EventMouseButton", type=StringType)
Controller_Event_union__EventMouseMotion: Property = Property(name="EventMouseMotion", type=StringType)
Controller_Event_union__EventMouseWheel: Property = Property(name="EventMouseWheel", type=StringType)
Controller_Event_union__EventQuit: Property = Property(name="EventQuit", type=StringType)
Controller_Event_union_.attributes={Controller_Event_union__eventType, Controller_Event_union__EventMouseButton, Controller_Event_union__EventMouseWheel, Controller_Event_union__EventEmpty, Controller_Event_union__EventMouseMotion, Controller_Event_union__EventQuit, Controller_Event_union__EvenkKeyboard}

# Controller_EventManager class attributes and methods
Controller_EventManager_eventQueue: Property = Property(name="eventQueue", type=StringType)
Controller_EventManager_queueLock: Property = Property(name="queueLock", type=BooleanType)
Controller_EventManager.attributes={Controller_EventManager_eventQueue, Controller_EventManager_queueLock}

# Table1 class attributes and methods
Table1_ID: Property = Property(name="ID", type=StringType)
Table1_table3ID: Property = Property(name="table3ID", type=StringType)
Table1_table1ID: Property = Property(name="table1ID", type=StringType)
Table1.attributes={Table1_ID, Table1_table1ID, Table1_table3ID}

# Table2 class attributes and methods
Table2_ID: Property = Property(name="ID", type=StringType)
Table2.attributes={Table2_ID}

# trans_Table class attributes and methods
trans_Table_table1ID: Property = Property(name="table1ID", type=StringType)
trans_Table_table2ID: Property = Property(name="table2ID", type=StringType)
trans_Table.attributes={trans_Table_table1ID, trans_Table_table2ID}

# Table3 class attributes and methods
Table3_ID: Property = Property(name="ID", type=StringType)
Table3.attributes={Table3_ID}

# AbstractProperty class attributes and methods

# Entity class attributes and methods
Entity_properties: Property = Property(name="properties", type=AbstractProperty)
Entity_behaviors: Property = Property(name="behaviors", type=AbstractBehavior)
Entity.attributes={Entity_properties, Entity_behaviors}

# AbstractBehavior class attributes and methods

# Relationships
Camera_View: BinaryAssociation = BinaryAssociation(
    name="Camera_View",
    ends={
        Property(name="view18", type=View_View, multiplicity=Multiplicity(1, 1)),
        Property(name="camera19", type=View_SDLCamera, multiplicity=Multiplicity(1, 1))
    }
)
SDLRenderer_SDLCamera: BinaryAssociation = BinaryAssociation(
    name="SDLRenderer_SDLCamera",
    ends={
        Property(name="sDLCamera20", type=View_SDLCamera, multiplicity=Multiplicity(1, 1)),
        Property(name="sDLRenderer21", type=View_SDLRenderer, multiplicity=Multiplicity(1, 1))
    }
)
InputController_Controller: BinaryAssociation = BinaryAssociation(
    name="InputController_Controller",
    ends={
        Property(name="controller22", type=Controller_Controller, multiplicity=Multiplicity(0, 9999)),
        Property(name="inputController23", type=Controller_InputController_Interface, multiplicity=Multiplicity(1, 1))
    }
)
Controller_View: BinaryAssociation = BinaryAssociation(
    name="Controller_View",
    ends={
        Property(name="view24", type=View_View, multiplicity=Multiplicity(1, 1)),
        Property(name="controller25", type=Controller_Controller, multiplicity=Multiplicity(0, 9999))
    }
)
EventManager_Controller: BinaryAssociation = BinaryAssociation(
    name="EventManager_Controller",
    ends={
        Property(name="controller26", type=Controller_Controller, multiplicity=Multiplicity(0, 9999)),
        Property(name="eventManager27", type=Controller_EventManager, multiplicity=Multiplicity(1, 1))
    }
)
EventManager_Event_union_: BinaryAssociation = BinaryAssociation(
    name="EventManager_Event_union_",
    ends={
        Property(name="event_union_28", type=Controller_Event_union_, multiplicity=Multiplicity(0, 9999)),
        Property(name="eventManager29", type=Controller_EventManager, multiplicity=Multiplicity(1, 1))
    }
)
Controller_World: BinaryAssociation = BinaryAssociation(
    name="Controller_World",
    ends={
        Property(name="world30", type=Model_World, multiplicity=Multiplicity(1, 1)),
        Property(name="controller31", type=Controller_Controller, multiplicity=Multiplicity(0, 9999))
    }
)
Table1_Table1: BinaryAssociation = BinaryAssociation(
    name="Table1_Table1",
    ends={
        Property(name="table132", type=Table1, multiplicity=Multiplicity(0, 1)),
        Property(name="table133", type=Table1, multiplicity=Multiplicity(0, 1))
    }
)
Entity_AbstractProperty: BinaryAssociation = BinaryAssociation(
    name="Entity_AbstractProperty",
    ends={
        Property(name="abstractProperty34", type=AbstractProperty, multiplicity=Multiplicity(0, 9999)),
        Property(name="entity35", type=Entity, multiplicity=Multiplicity(0, 9999))
    }
)
Entity_AbstractBehavior: BinaryAssociation = BinaryAssociation(
    name="Entity_AbstractBehavior",
    ends={
        Property(name="abstractBehavior36", type=AbstractBehavior, multiplicity=Multiplicity(0, 9999)),
        Property(name="entity37", type=Entity, multiplicity=Multiplicity(0, 9999))
    }
)
World_Chunk: BinaryAssociation = BinaryAssociation(
    name="World_Chunk",
    ends={
        Property(name="chunk0", type=Model_Chunk, multiplicity=Multiplicity(1, 9999)),
        Property(name="world1", type=Model_World, multiplicity=Multiplicity(1, 1))
    }
)
Chunk_Tile: BinaryAssociation = BinaryAssociation(
    name="Chunk_Tile",
    ends={
        Property(name="tile2", type=Model_Tile, multiplicity=Multiplicity(0, 9999)),
        Property(name="chunk3", type=Model_Chunk, multiplicity=Multiplicity(1, 1))
    }
)
World_Chunk2: BinaryAssociation = BinaryAssociation(
    name="World_Chunk2",
    ends={
        Property(name="chunk4", type=Model_Chunk, multiplicity=Multiplicity(9, 9)),
        Property(name="world5", type=Model_World, multiplicity=Multiplicity(1, 1))
    }
)
World_Renderer: BinaryAssociation = BinaryAssociation(
    name="World_Renderer",
    ends={
        Property(name="renderer6", type=View_View, multiplicity=Multiplicity(0, 9999)),
        Property(name="world7", type=Model_World, multiplicity=Multiplicity(1, 1))
    }
)
WorldGenertor_World: BinaryAssociation = BinaryAssociation(
    name="WorldGenertor_World",
    ends={
        Property(name="world8", type=Model_World, multiplicity=Multiplicity(1, 1)),
        Property(name="worldGenertor9", type=Model_WorldGenerator, multiplicity=Multiplicity(0, 9999))
    }
)
View_Renderer: BinaryAssociation = BinaryAssociation(
    name="View_Renderer",
    ends={
        Property(name="renderer10", type=View_Renderer_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="view11", type=View_View, multiplicity=Multiplicity(0, 9999))
    }
)
Renderer_Texture: BinaryAssociation = BinaryAssociation(
    name="Renderer_Texture",
    ends={
        Property(name="texture12", type=View_Texture_Interface, multiplicity=Multiplicity(0, 9999)),
        Property(name="renderer13", type=View_Renderer_Interface, multiplicity=Multiplicity(1, 1))
    }
)
Renderer_SDLRenderer: BinaryAssociation = BinaryAssociation(
    name="Renderer_SDLRenderer",
    ends={
        Property(name="sDLRenderer14", type=View_SDLRenderer, multiplicity=Multiplicity(0, 1)),
        Property(name="renderer15", type=View_Renderer_Interface, multiplicity=Multiplicity(0, 1))
    }
)
SDLRenderer_SDLTexture: BinaryAssociation = BinaryAssociation(
    name="SDLRenderer_SDLTexture",
    ends={
        Property(name="sDLTexture16", type=View_SDLTexture, multiplicity=Multiplicity(1, 9999)),
        Property(name="sDLRenderer17", type=View_SDLRenderer, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_DyDa8IwpEemq7_yOQcm9ow",
    types={Model_Tile, Model_Chunk, Model_World, Model_WorldGenerator, View_View, View_Renderer_Interface, View_SDLRenderer, View_Interface_Interface, View_Texture_Interface, View_SDLTexture, View_SDLCamera, View_Camera_Interface, Controller_Parser, Controller_SDLInputController, Controller_InputController_Interface, Controller_Controller, Controller_Event_union_, Controller_EventManager, Table1, Table2, trans_Table, Table3, AbstractProperty, Entity, AbstractBehavior},
    associations={Camera_View, SDLRenderer_SDLCamera, InputController_Controller, Controller_View, EventManager_Controller, EventManager_Event_union_, Controller_World, Table1_Table1, Entity_AbstractProperty, Entity_AbstractBehavior, World_Chunk, Chunk_Tile, World_Chunk2, World_Renderer, WorldGenertor_World, View_Renderer, Renderer_Texture, Renderer_SDLRenderer, SDLRenderer_SDLTexture},
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