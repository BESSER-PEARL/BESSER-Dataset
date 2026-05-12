from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class AbstractBehavior(ABC):

    pass


class Entity:

    def __init__(self, properties: AbstractProperty, behaviors: AbstractBehavior, abstractProperty34: set["AbstractProperty"] = None, abstractBehavior36: set["AbstractBehavior"] = None):
        self.properties = properties
        self.behaviors = behaviors
        self.abstractProperty34 = abstractProperty34 if abstractProperty34 is not None else set()
        self.abstractBehavior36 = abstractBehavior36 if abstractBehavior36 is not None else set()
        
        pass
    @property
    def properties(self):
        return self.__properties
    @properties.setter
    def properties(self, properties: AbstractProperty):
        self.__properties = properties

    @property
    def behaviors(self):
        return self.__behaviors
    @behaviors.setter
    def behaviors(self, behaviors: AbstractBehavior):
        self.__behaviors = behaviors

    @property
    def abstractProperty34(self):
        return self.__abstractProperty34
    @abstractProperty34.setter
    def abstractProperty34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Entity__abstractProperty34", None)
        self.__abstractProperty34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "entity35"):
                    opp_val = getattr(item, "entity35", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "entity35"):
                    opp_val = getattr(item, "entity35", None)
                    
                    if opp_val is None:
                        setattr(item, "entity35", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def abstractBehavior36(self):
        return self.__abstractBehavior36
    @abstractBehavior36.setter
    def abstractBehavior36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Entity__abstractBehavior36", None)
        self.__abstractBehavior36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "entity37"):
                    opp_val = getattr(item, "entity37", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "entity37"):
                    opp_val = getattr(item, "entity37", None)
                    
                    if opp_val is None:
                        setattr(item, "entity37", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class AbstractProperty(ABC):

    pass


class Table3:

    def __init__(self, ID: str):
        self.ID = ID
        
        pass
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID



class trans_Table:

    def __init__(self, table1ID: str, table2ID: str):
        self.table1ID = table1ID
        self.table2ID = table2ID
        
        pass
    @property
    def table2ID(self):
        return self.__table2ID
    @table2ID.setter
    def table2ID(self, table2ID: str):
        self.__table2ID = table2ID

    @property
    def table1ID(self):
        return self.__table1ID
    @table1ID.setter
    def table1ID(self, table1ID: str):
        self.__table1ID = table1ID



class Table2:

    def __init__(self, ID: str):
        self.ID = ID
        
        pass
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID



class Table1:

    def __init__(self, ID: str, table3ID: str, table1ID: str, table132: "Table1" = None, table133: "Table1" = None):
        self.ID = ID
        self.table3ID = table3ID
        self.table1ID = table1ID
        self.table132 = table132
        self.table133 = table133
        
        pass
    @property
    def table3ID(self):
        return self.__table3ID
    @table3ID.setter
    def table3ID(self, table3ID: str):
        self.__table3ID = table3ID

    @property
    def table1ID(self):
        return self.__table1ID
    @table1ID.setter
    def table1ID(self, table1ID: str):
        self.__table1ID = table1ID

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def table132(self):
        return self.__table132
    @table132.setter
    def table132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Table1__table132", None)
        self.__table132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table133"):
                opp_val = getattr(old_value, "table133", None)
                if opp_val == self:
                    setattr(old_value, "table133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table133"):
                opp_val = getattr(value, "table133", None)
                setattr(value, "table133", self)

    @property
    def table133(self):
        return self.__table133
    @table133.setter
    def table133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Table1__table133", None)
        self.__table133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table132"):
                opp_val = getattr(old_value, "table132", None)
                if opp_val == self:
                    setattr(old_value, "table132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table132"):
                opp_val = getattr(value, "table132", None)
                setattr(value, "table132", self)



class Controller_EventManager:

    def __init__(self, eventQueue: str, queueLock: bool, controller26: set["Controller_Controller"] = None, event_union_28: set["Controller_Event_union_"] = None):
        self.eventQueue = eventQueue
        self.queueLock = queueLock
        self.controller26 = controller26 if controller26 is not None else set()
        self.event_union_28 = event_union_28 if event_union_28 is not None else set()
        
        pass
    @property
    def eventQueue(self):
        return self.__eventQueue
    @eventQueue.setter
    def eventQueue(self, eventQueue: str):
        self.__eventQueue = eventQueue

    @property
    def queueLock(self):
        return self.__queueLock
    @queueLock.setter
    def queueLock(self, queueLock: bool):
        self.__queueLock = queueLock

    @property
    def controller26(self):
        return self.__controller26
    @controller26.setter
    def controller26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Controller_EventManager__controller26", None)
        self.__controller26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eventManager27"):
                    opp_val = getattr(item, "eventManager27", None)
                    
                    if opp_val == self:
                        setattr(item, "eventManager27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eventManager27"):
                    opp_val = getattr(item, "eventManager27", None)
                    
                    setattr(item, "eventManager27", self)
                    

    @property
    def event_union_28(self):
        return self.__event_union_28
    @event_union_28.setter
    def event_union_28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Controller_EventManager__event_union_28", None)
        self.__event_union_28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eventManager29"):
                    opp_val = getattr(item, "eventManager29", None)
                    
                    if opp_val == self:
                        setattr(item, "eventManager29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eventManager29"):
                    opp_val = getattr(item, "eventManager29", None)
                    
                    setattr(item, "eventManager29", self)
                    



class Controller_Event_union_:

    def __init__(self, eventType: str, EventEmpty: str, EvenkKeyboard: str, EventMouseButton: str, EventMouseMotion: str, EventMouseWheel: str, EventQuit: str, eventManager29: "Controller_EventManager" = None):
        self.eventType = eventType
        self.EventEmpty = EventEmpty
        self.EvenkKeyboard = EvenkKeyboard
        self.EventMouseButton = EventMouseButton
        self.EventMouseMotion = EventMouseMotion
        self.EventMouseWheel = EventMouseWheel
        self.EventQuit = EventQuit
        self.eventManager29 = eventManager29
        
        pass
    @property
    def EventEmpty(self):
        return self.__EventEmpty
    @EventEmpty.setter
    def EventEmpty(self, EventEmpty: str):
        self.__EventEmpty = EventEmpty

    @property
    def EvenkKeyboard(self):
        return self.__EvenkKeyboard
    @EvenkKeyboard.setter
    def EvenkKeyboard(self, EvenkKeyboard: str):
        self.__EvenkKeyboard = EvenkKeyboard

    @property
    def EventMouseButton(self):
        return self.__EventMouseButton
    @EventMouseButton.setter
    def EventMouseButton(self, EventMouseButton: str):
        self.__EventMouseButton = EventMouseButton

    @property
    def EventMouseMotion(self):
        return self.__EventMouseMotion
    @EventMouseMotion.setter
    def EventMouseMotion(self, EventMouseMotion: str):
        self.__EventMouseMotion = EventMouseMotion

    @property
    def eventType(self):
        return self.__eventType
    @eventType.setter
    def eventType(self, eventType: str):
        self.__eventType = eventType

    @property
    def EventQuit(self):
        return self.__EventQuit
    @EventQuit.setter
    def EventQuit(self, EventQuit: str):
        self.__EventQuit = EventQuit

    @property
    def EventMouseWheel(self):
        return self.__EventMouseWheel
    @EventMouseWheel.setter
    def EventMouseWheel(self, EventMouseWheel: str):
        self.__EventMouseWheel = EventMouseWheel

    @property
    def eventManager29(self):
        return self.__eventManager29
    @eventManager29.setter
    def eventManager29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Controller_Event_union___eventManager29", None)
        self.__eventManager29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "event_union_28"):
                opp_val = getattr(old_value, "event_union_28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "event_union_28"):
                opp_val = getattr(value, "event_union_28", None)
                if opp_val is None:
                    setattr(value, "event_union_28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Controller_Controller:

    def __init__(self, worldAccess: Model_World, viewAccess: View_View, inputController: Controller_InputController_Interface, eventManager: Controller_EventManager, attribute: str, inputController23: "Controller_InputController_Interface" = None, view24: "View_View" = None, eventManager27: "Controller_EventManager" = None, world30: "Model_World" = None):
        self.worldAccess = worldAccess
        self.viewAccess = viewAccess
        self.inputController = inputController
        self.eventManager = eventManager
        self.attribute = attribute
        self.inputController23 = inputController23
        self.view24 = view24
        self.eventManager27 = eventManager27
        self.world30 = world30
        
        pass
    @property
    def inputController(self):
        return self.__inputController
    @inputController.setter
    def inputController(self, inputController: Controller_InputController_Interface):
        self.__inputController = inputController

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def eventManager(self):
        return self.__eventManager
    @eventManager.setter
    def eventManager(self, eventManager: Controller_EventManager):
        self.__eventManager = eventManager

    @property
    def worldAccess(self):
        return self.__worldAccess
    @worldAccess.setter
    def worldAccess(self, worldAccess: Model_World):
        self.__worldAccess = worldAccess

    @property
    def viewAccess(self):
        return self.__viewAccess
    @viewAccess.setter
    def viewAccess(self, viewAccess: View_View):
        self.__viewAccess = viewAccess

    @property
    def view24(self):
        return self.__view24
    @view24.setter
    def view24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Controller_Controller__view24", None)
        self.__view24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "controller25"):
                opp_val = getattr(old_value, "controller25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "controller25"):
                opp_val = getattr(value, "controller25", None)
                if opp_val is None:
                    setattr(value, "controller25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eventManager27(self):
        return self.__eventManager27
    @eventManager27.setter
    def eventManager27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Controller_Controller__eventManager27", None)
        self.__eventManager27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "controller26"):
                opp_val = getattr(old_value, "controller26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "controller26"):
                opp_val = getattr(value, "controller26", None)
                if opp_val is None:
                    setattr(value, "controller26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def inputController23(self):
        return self.__inputController23
    @inputController23.setter
    def inputController23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Controller_Controller__inputController23", None)
        self.__inputController23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "controller22"):
                opp_val = getattr(old_value, "controller22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "controller22"):
                opp_val = getattr(value, "controller22", None)
                if opp_val is None:
                    setattr(value, "controller22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def world30(self):
        return self.__world30
    @world30.setter
    def world30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Controller_Controller__world30", None)
        self.__world30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "controller31"):
                opp_val = getattr(old_value, "controller31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "controller31"):
                opp_val = getattr(value, "controller31", None)
                if opp_val is None:
                    setattr(value, "controller31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Controller_InputController_Interface:

    pass


class Controller_SDLInputController:

    def __init__(self, controllerPointer: Controller_Controller, eventList: str):
        self.controllerPointer = controllerPointer
        self.eventList = eventList
        
        pass
    @property
    def controllerPointer(self):
        return self.__controllerPointer
    @controllerPointer.setter
    def controllerPointer(self, controllerPointer: Controller_Controller):
        self.__controllerPointer = controllerPointer

    @property
    def eventList(self):
        return self.__eventList
    @eventList.setter
    def eventList(self, eventList: str):
        self.__eventList = eventList



class Controller_Parser:

    pass


class View_Camera_Interface:

    pass


class View_SDLCamera:

    pass


class View_SDLTexture:

    pass


class View_Texture_Interface:

    pass


class View_Interface_Interface:

    pass


class View_SDLRenderer:

    def __init__(self, viewPointer: View_View, tileset: View_SDLTexture, camera: View_SDLCamera, window: str, renderer: str, sDLCamera20: "View_SDLCamera" = None, renderer15: "View_Renderer_Interface" = None, sDLTexture16: set["View_SDLTexture"] = None):
        self.viewPointer = viewPointer
        self.tileset = tileset
        self.camera = camera
        self.window = window
        self.renderer = renderer
        self.sDLCamera20 = sDLCamera20
        self.renderer15 = renderer15
        self.sDLTexture16 = sDLTexture16 if sDLTexture16 is not None else set()
        
        pass
    @property
    def renderer(self):
        return self.__renderer
    @renderer.setter
    def renderer(self, renderer: str):
        self.__renderer = renderer

    @property
    def viewPointer(self):
        return self.__viewPointer
    @viewPointer.setter
    def viewPointer(self, viewPointer: View_View):
        self.__viewPointer = viewPointer

    @property
    def window(self):
        return self.__window
    @window.setter
    def window(self, window: str):
        self.__window = window

    @property
    def camera(self):
        return self.__camera
    @camera.setter
    def camera(self, camera: View_SDLCamera):
        self.__camera = camera

    @property
    def tileset(self):
        return self.__tileset
    @tileset.setter
    def tileset(self, tileset: View_SDLTexture):
        self.__tileset = tileset

    @property
    def sDLCamera20(self):
        return self.__sDLCamera20
    @sDLCamera20.setter
    def sDLCamera20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_View_SDLRenderer__sDLCamera20", None)
        self.__sDLCamera20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sDLRenderer21"):
                opp_val = getattr(old_value, "sDLRenderer21", None)
                if opp_val == self:
                    setattr(old_value, "sDLRenderer21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sDLRenderer21"):
                opp_val = getattr(value, "sDLRenderer21", None)
                setattr(value, "sDLRenderer21", self)

    @property
    def renderer15(self):
        return self.__renderer15
    @renderer15.setter
    def renderer15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_View_SDLRenderer__renderer15", None)
        self.__renderer15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sDLRenderer14"):
                opp_val = getattr(old_value, "sDLRenderer14", None)
                if opp_val == self:
                    setattr(old_value, "sDLRenderer14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sDLRenderer14"):
                opp_val = getattr(value, "sDLRenderer14", None)
                setattr(value, "sDLRenderer14", self)

    @property
    def sDLTexture16(self):
        return self.__sDLTexture16
    @sDLTexture16.setter
    def sDLTexture16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_View_SDLRenderer__sDLTexture16", None)
        self.__sDLTexture16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sDLRenderer17"):
                    opp_val = getattr(item, "sDLRenderer17", None)
                    
                    if opp_val == self:
                        setattr(item, "sDLRenderer17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sDLRenderer17"):
                    opp_val = getattr(item, "sDLRenderer17", None)
                    
                    setattr(item, "sDLRenderer17", self)
                    



class View_Renderer_Interface:

    pass


class View_View:

    def __init__(self, worldAccess: Model_World, renderer: View_Renderer_Interface, controller25: set["Controller_Controller"] = None, world7: "Model_World" = None, renderer10: "View_Renderer_Interface" = None, camera19: "View_SDLCamera" = None):
        self.worldAccess = worldAccess
        self.renderer = renderer
        self.controller25 = controller25 if controller25 is not None else set()
        self.world7 = world7
        self.renderer10 = renderer10
        self.camera19 = camera19
        
        pass
    @property
    def worldAccess(self):
        return self.__worldAccess
    @worldAccess.setter
    def worldAccess(self, worldAccess: Model_World):
        self.__worldAccess = worldAccess

    @property
    def renderer(self):
        return self.__renderer
    @renderer.setter
    def renderer(self, renderer: View_Renderer_Interface):
        self.__renderer = renderer

    @property
    def camera19(self):
        return self.__camera19
    @camera19.setter
    def camera19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_View_View__camera19", None)
        self.__camera19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "view18"):
                opp_val = getattr(old_value, "view18", None)
                if opp_val == self:
                    setattr(old_value, "view18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "view18"):
                opp_val = getattr(value, "view18", None)
                setattr(value, "view18", self)

    @property
    def world7(self):
        return self.__world7
    @world7.setter
    def world7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_View_View__world7", None)
        self.__world7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "renderer6"):
                opp_val = getattr(old_value, "renderer6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "renderer6"):
                opp_val = getattr(value, "renderer6", None)
                if opp_val is None:
                    setattr(value, "renderer6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def controller25(self):
        return self.__controller25
    @controller25.setter
    def controller25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_View_View__controller25", None)
        self.__controller25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "view24"):
                    opp_val = getattr(item, "view24", None)
                    
                    if opp_val == self:
                        setattr(item, "view24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "view24"):
                    opp_val = getattr(item, "view24", None)
                    
                    setattr(item, "view24", self)
                    

    @property
    def renderer10(self):
        return self.__renderer10
    @renderer10.setter
    def renderer10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_View_View__renderer10", None)
        self.__renderer10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "view11"):
                opp_val = getattr(old_value, "view11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "view11"):
                opp_val = getattr(value, "view11", None)
                if opp_val is None:
                    setattr(value, "view11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Model_WorldGenerator:

    pass


class Model_World:

    pass


class Model_Chunk:

    pass


class Model_Tile:

    def __init__(self, type: int, mod: int, id: int, position: str, chunk3: "Model_Chunk" = None):
        self.type = type
        self.mod = mod
        self.id = id
        self.position = position
        self.chunk3 = chunk3
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: int):
        self.__type = type

    @property
    def mod(self):
        return self.__mod
    @mod.setter
    def mod(self, mod: int):
        self.__mod = mod

    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def chunk3(self):
        return self.__chunk3
    @chunk3.setter
    def chunk3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model_Tile__chunk3", None)
        self.__chunk3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tile2"):
                opp_val = getattr(old_value, "tile2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tile2"):
                opp_val = getattr(value, "tile2", None)
                if opp_val is None:
                    setattr(value, "tile2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

