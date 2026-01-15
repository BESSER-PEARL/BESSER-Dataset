from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class expansionmodel_DiagramExpansion:

    def __init__(self, ID: str, expansionmodel_DiagramExpansion: set["expansionmodel_UseContext"] = None, expansionmodel_DiagramExpansion20: set["expansionmodel_GraphicalElementLibrary"] = None):
        self.ID = ID
        self.expansionmodel_DiagramExpansion = expansionmodel_DiagramExpansion if expansionmodel_DiagramExpansion is not None else set()
        self.expansionmodel_DiagramExpansion20 = expansionmodel_DiagramExpansion20 if expansionmodel_DiagramExpansion20 is not None else set()
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def expansionmodel_DiagramExpansion(self):
        return self.__expansionmodel_DiagramExpansion

    @expansionmodel_DiagramExpansion.setter
    def expansionmodel_DiagramExpansion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expansionmodel_DiagramExpansion__expansionmodel_DiagramExpansion", None)
        self.__expansionmodel_DiagramExpansion = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "expansionmodel_UseContext18"):
                    opp_val = getattr(item, "expansionmodel_UseContext18", None)
                    
                    if opp_val == self:
                        setattr(item, "expansionmodel_UseContext18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "expansionmodel_UseContext18"):
                    opp_val = getattr(item, "expansionmodel_UseContext18", None)
                    
                    setattr(item, "expansionmodel_UseContext18", self)
                    

    @property
    def expansionmodel_DiagramExpansion20(self):
        return self.__expansionmodel_DiagramExpansion20

    @expansionmodel_DiagramExpansion20.setter
    def expansionmodel_DiagramExpansion20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expansionmodel_DiagramExpansion__expansionmodel_DiagramExpansion20", None)
        self.__expansionmodel_DiagramExpansion20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "expansionmodel_GraphicalElementLibrary21"):
                    opp_val = getattr(item, "expansionmodel_GraphicalElementLibrary21", None)
                    
                    if opp_val == self:
                        setattr(item, "expansionmodel_GraphicalElementLibrary21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "expansionmodel_GraphicalElementLibrary21"):
                    opp_val = getattr(item, "expansionmodel_GraphicalElementLibrary21", None)
                    
                    setattr(item, "expansionmodel_GraphicalElementLibrary21", self)
                    

class Representation:

    pass
class expansionmodel_GMFT_BasedRepresentation(Representation):

    def __init__(self, reusedID: str, expansionmodel_GMFT_BasedRepresentation: "expansionmodel_UseContext" = None):
        self.reusedID = reusedID
        self.expansionmodel_GMFT_BasedRepresentation = expansionmodel_GMFT_BasedRepresentation
        
    @property
    def reusedID(self) -> str:
        return self.__reusedID

    @reusedID.setter
    def reusedID(self, reusedID: str):
        self.__reusedID = reusedID

    @property
    def expansionmodel_GMFT_BasedRepresentation(self):
        return self.__expansionmodel_GMFT_BasedRepresentation

    @expansionmodel_GMFT_BasedRepresentation.setter
    def expansionmodel_GMFT_BasedRepresentation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expansionmodel_GMFT_BasedRepresentation__expansionmodel_GMFT_BasedRepresentation", None)
        self.__expansionmodel_GMFT_BasedRepresentation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expansionmodel_UseContext16"):
                opp_val = getattr(old_value, "expansionmodel_UseContext16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expansionmodel_UseContext16"):
                opp_val = getattr(value, "expansionmodel_UseContext16", None)
                if opp_val is None:
                    setattr(value, "expansionmodel_UseContext16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class expansionmodel_GraphicalElementLibrary:

    def __init__(self, name: str, expansionmodel_GraphicalElementLibrary: set["expansionmodel_RepresentationKind"] = None, expansionmodel_GraphicalElementLibrary11: set["expansionmodel_AbstractRepresentation"] = None, expansionmodel_GraphicalElementLibrary21: "expansionmodel_DiagramExpansion" = None):
        self.name = name
        self.expansionmodel_GraphicalElementLibrary = expansionmodel_GraphicalElementLibrary if expansionmodel_GraphicalElementLibrary is not None else set()
        self.expansionmodel_GraphicalElementLibrary11 = expansionmodel_GraphicalElementLibrary11 if expansionmodel_GraphicalElementLibrary11 is not None else set()
        self.expansionmodel_GraphicalElementLibrary21 = expansionmodel_GraphicalElementLibrary21
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def expansionmodel_GraphicalElementLibrary21(self):
        return self.__expansionmodel_GraphicalElementLibrary21

    @expansionmodel_GraphicalElementLibrary21.setter
    def expansionmodel_GraphicalElementLibrary21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expansionmodel_GraphicalElementLibrary__expansionmodel_GraphicalElementLibrary21", None)
        self.__expansionmodel_GraphicalElementLibrary21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expansionmodel_DiagramExpansion20"):
                opp_val = getattr(old_value, "expansionmodel_DiagramExpansion20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expansionmodel_DiagramExpansion20"):
                opp_val = getattr(value, "expansionmodel_DiagramExpansion20", None)
                if opp_val is None:
                    setattr(value, "expansionmodel_DiagramExpansion20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def expansionmodel_GraphicalElementLibrary11(self):
        return self.__expansionmodel_GraphicalElementLibrary11

    @expansionmodel_GraphicalElementLibrary11.setter
    def expansionmodel_GraphicalElementLibrary11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expansionmodel_GraphicalElementLibrary__expansionmodel_GraphicalElementLibrary11", None)
        self.__expansionmodel_GraphicalElementLibrary11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "expansionmodel_AbstractRepresentation12"):
                    opp_val = getattr(item, "expansionmodel_AbstractRepresentation12", None)
                    
                    if opp_val == self:
                        setattr(item, "expansionmodel_AbstractRepresentation12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "expansionmodel_AbstractRepresentation12"):
                    opp_val = getattr(item, "expansionmodel_AbstractRepresentation12", None)
                    
                    setattr(item, "expansionmodel_AbstractRepresentation12", self)
                    

    @property
    def expansionmodel_GraphicalElementLibrary(self):
        return self.__expansionmodel_GraphicalElementLibrary

    @expansionmodel_GraphicalElementLibrary.setter
    def expansionmodel_GraphicalElementLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expansionmodel_GraphicalElementLibrary__expansionmodel_GraphicalElementLibrary", None)
        self.__expansionmodel_GraphicalElementLibrary = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "expansionmodel_RepresentationKind9"):
                    opp_val = getattr(item, "expansionmodel_RepresentationKind9", None)
                    
                    if opp_val == self:
                        setattr(item, "expansionmodel_RepresentationKind9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "expansionmodel_RepresentationKind9"):
                    opp_val = getattr(item, "expansionmodel_RepresentationKind9", None)
                    
                    setattr(item, "expansionmodel_RepresentationKind9", self)
                    

class expansionmodel_UseContext:

    def __init__(self, diagramType: str, name: str, expansionmodel_UseContext: set["expansionmodel_Representation"] = None, expansionmodel_UseContext16: set["expansionmodel_GMFT_BasedRepresentation"] = None, expansionmodel_UseContext18: "expansionmodel_DiagramExpansion" = None):
        self.diagramType = diagramType
        self.name = name
        self.expansionmodel_UseContext = expansionmodel_UseContext if expansionmodel_UseContext is not None else set()
        self.expansionmodel_UseContext16 = expansionmodel_UseContext16 if expansionmodel_UseContext16 is not None else set()
        self.expansionmodel_UseContext18 = expansionmodel_UseContext18
        
    @property
    def diagramType(self) -> str:
        return self.__diagramType

    @diagramType.setter
    def diagramType(self, diagramType: str):
        self.__diagramType = diagramType

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def expansionmodel_UseContext(self):
        return self.__expansionmodel_UseContext

    @expansionmodel_UseContext.setter
    def expansionmodel_UseContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expansionmodel_UseContext__expansionmodel_UseContext", None)
        self.__expansionmodel_UseContext = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "expansionmodel_Representation14"):
                    opp_val = getattr(item, "expansionmodel_Representation14", None)
                    
                    if opp_val == self:
                        setattr(item, "expansionmodel_Representation14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "expansionmodel_Representation14"):
                    opp_val = getattr(item, "expansionmodel_Representation14", None)
                    
                    setattr(item, "expansionmodel_Representation14", self)
                    

    @property
    def expansionmodel_UseContext16(self):
        return self.__expansionmodel_UseContext16

    @expansionmodel_UseContext16.setter
    def expansionmodel_UseContext16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expansionmodel_UseContext__expansionmodel_UseContext16", None)
        self.__expansionmodel_UseContext16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "expansionmodel_GMFT_BasedRepresentation"):
                    opp_val = getattr(item, "expansionmodel_GMFT_BasedRepresentation", None)
                    
                    if opp_val == self:
                        setattr(item, "expansionmodel_GMFT_BasedRepresentation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "expansionmodel_GMFT_BasedRepresentation"):
                    opp_val = getattr(item, "expansionmodel_GMFT_BasedRepresentation", None)
                    
                    setattr(item, "expansionmodel_GMFT_BasedRepresentation", self)
                    

    @property
    def expansionmodel_UseContext18(self):
        return self.__expansionmodel_UseContext18

    @expansionmodel_UseContext18.setter
    def expansionmodel_UseContext18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expansionmodel_UseContext__expansionmodel_UseContext18", None)
        self.__expansionmodel_UseContext18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expansionmodel_DiagramExpansion"):
                opp_val = getattr(old_value, "expansionmodel_DiagramExpansion", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expansionmodel_DiagramExpansion"):
                opp_val = getattr(value, "expansionmodel_DiagramExpansion", None)
                if opp_val is None:
                    setattr(value, "expansionmodel_DiagramExpansion", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class expansionmodel_RepresentationKind:

    def __init__(self, editPartQualifiedName: str, name: str, viewFactory: str, expansionmodel_RepresentationKind: "expansionmodel_AbstractRepresentation" = None, expansionmodel_RepresentationKind9: "expansionmodel_GraphicalElementLibrary" = None):
        self.editPartQualifiedName = editPartQualifiedName
        self.name = name
        self.viewFactory = viewFactory
        self.expansionmodel_RepresentationKind = expansionmodel_RepresentationKind
        self.expansionmodel_RepresentationKind9 = expansionmodel_RepresentationKind9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def editPartQualifiedName(self) -> str:
        return self.__editPartQualifiedName

    @editPartQualifiedName.setter
    def editPartQualifiedName(self, editPartQualifiedName: str):
        self.__editPartQualifiedName = editPartQualifiedName

    @property
    def viewFactory(self) -> str:
        return self.__viewFactory

    @viewFactory.setter
    def viewFactory(self, viewFactory: str):
        self.__viewFactory = viewFactory

    @property
    def expansionmodel_RepresentationKind(self):
        return self.__expansionmodel_RepresentationKind

    @expansionmodel_RepresentationKind.setter
    def expansionmodel_RepresentationKind(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expansionmodel_RepresentationKind__expansionmodel_RepresentationKind", None)
        self.__expansionmodel_RepresentationKind = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expansionmodel_AbstractRepresentation"):
                opp_val = getattr(old_value, "expansionmodel_AbstractRepresentation", None)
                if opp_val == self:
                    setattr(old_value, "expansionmodel_AbstractRepresentation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expansionmodel_AbstractRepresentation"):
                opp_val = getattr(value, "expansionmodel_AbstractRepresentation", None)
                setattr(value, "expansionmodel_AbstractRepresentation", self)

    @property
    def expansionmodel_RepresentationKind9(self):
        return self.__expansionmodel_RepresentationKind9

    @expansionmodel_RepresentationKind9.setter
    def expansionmodel_RepresentationKind9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expansionmodel_RepresentationKind__expansionmodel_RepresentationKind9", None)
        self.__expansionmodel_RepresentationKind9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expansionmodel_GraphicalElementLibrary"):
                opp_val = getattr(old_value, "expansionmodel_GraphicalElementLibrary", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expansionmodel_GraphicalElementLibrary"):
                opp_val = getattr(value, "expansionmodel_GraphicalElementLibrary", None)
                if opp_val is None:
                    setattr(value, "expansionmodel_GraphicalElementLibrary", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class expansionmodel_AbstractRepresentation(ABC):

    def __init__(self, editPartQualifiedName: str, name: str, viewFactory: str, expansionmodel_AbstractRepresentation: "expansionmodel_RepresentationKind" = None, expansionmodel_AbstractRepresentation12: "expansionmodel_GraphicalElementLibrary" = None):
        self.editPartQualifiedName = editPartQualifiedName
        self.name = name
        self.viewFactory = viewFactory
        self.expansionmodel_AbstractRepresentation = expansionmodel_AbstractRepresentation
        self.expansionmodel_AbstractRepresentation12 = expansionmodel_AbstractRepresentation12
        
    @property
    def viewFactory(self) -> str:
        return self.__viewFactory

    @viewFactory.setter
    def viewFactory(self, viewFactory: str):
        self.__viewFactory = viewFactory

    @property
    def editPartQualifiedName(self) -> str:
        return self.__editPartQualifiedName

    @editPartQualifiedName.setter
    def editPartQualifiedName(self, editPartQualifiedName: str):
        self.__editPartQualifiedName = editPartQualifiedName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def expansionmodel_AbstractRepresentation12(self):
        return self.__expansionmodel_AbstractRepresentation12

    @expansionmodel_AbstractRepresentation12.setter
    def expansionmodel_AbstractRepresentation12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expansionmodel_AbstractRepresentation__expansionmodel_AbstractRepresentation12", None)
        self.__expansionmodel_AbstractRepresentation12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expansionmodel_GraphicalElementLibrary11"):
                opp_val = getattr(old_value, "expansionmodel_GraphicalElementLibrary11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expansionmodel_GraphicalElementLibrary11"):
                opp_val = getattr(value, "expansionmodel_GraphicalElementLibrary11", None)
                if opp_val is None:
                    setattr(value, "expansionmodel_GraphicalElementLibrary11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def expansionmodel_AbstractRepresentation(self):
        return self.__expansionmodel_AbstractRepresentation

    @expansionmodel_AbstractRepresentation.setter
    def expansionmodel_AbstractRepresentation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expansionmodel_AbstractRepresentation__expansionmodel_AbstractRepresentation", None)
        self.__expansionmodel_AbstractRepresentation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expansionmodel_RepresentationKind"):
                opp_val = getattr(old_value, "expansionmodel_RepresentationKind", None)
                if opp_val == self:
                    setattr(old_value, "expansionmodel_RepresentationKind", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expansionmodel_RepresentationKind"):
                opp_val = getattr(value, "expansionmodel_RepresentationKind", None)
                setattr(value, "expansionmodel_RepresentationKind", self)

    def validate(self, context: str, diagnostic: str) -> bool:
        # TODO: Implement validate method
        pass

class AbstractRepresentation:

    pass
class expansionmodel_InducedRepresentation(AbstractRepresentation):

    def __init__(self, hint: str, expansionmodel_InducedRepresentation: "expansionmodel_Representation" = None, expansionmodel_InducedRepresentation6: set["expansionmodel_Representation"] = None):
        self.hint = hint
        self.expansionmodel_InducedRepresentation = expansionmodel_InducedRepresentation
        self.expansionmodel_InducedRepresentation6 = expansionmodel_InducedRepresentation6 if expansionmodel_InducedRepresentation6 is not None else set()
        
    @property
    def hint(self) -> str:
        return self.__hint

    @hint.setter
    def hint(self, hint: str):
        self.__hint = hint

    @property
    def expansionmodel_InducedRepresentation(self):
        return self.__expansionmodel_InducedRepresentation

    @expansionmodel_InducedRepresentation.setter
    def expansionmodel_InducedRepresentation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expansionmodel_InducedRepresentation__expansionmodel_InducedRepresentation", None)
        self.__expansionmodel_InducedRepresentation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expansionmodel_Representation"):
                opp_val = getattr(old_value, "expansionmodel_Representation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expansionmodel_Representation"):
                opp_val = getattr(value, "expansionmodel_Representation", None)
                if opp_val is None:
                    setattr(value, "expansionmodel_Representation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def expansionmodel_InducedRepresentation6(self):
        return self.__expansionmodel_InducedRepresentation6

    @expansionmodel_InducedRepresentation6.setter
    def expansionmodel_InducedRepresentation6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expansionmodel_InducedRepresentation__expansionmodel_InducedRepresentation6", None)
        self.__expansionmodel_InducedRepresentation6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "expansionmodel_Representation7"):
                    opp_val = getattr(item, "expansionmodel_Representation7", None)
                    
                    if opp_val == self:
                        setattr(item, "expansionmodel_Representation7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "expansionmodel_Representation7"):
                    opp_val = getattr(item, "expansionmodel_Representation7", None)
                    
                    setattr(item, "expansionmodel_Representation7", self)
                    

class expansionmodel_Representation(AbstractRepresentation):

    def __init__(self, graphicalElementType: str, expansionmodel_Representation: set["expansionmodel_InducedRepresentation"] = None, expansionmodel_Representation3: "expansionmodel_Representation" = None, expansionmodel_Representation1: set["expansionmodel_Representation"] = None, expansionmodel_Representation7: "expansionmodel_InducedRepresentation" = None, expansionmodel_Representation14: "expansionmodel_UseContext" = None):
        self.graphicalElementType = graphicalElementType
        self.expansionmodel_Representation = expansionmodel_Representation if expansionmodel_Representation is not None else set()
        self.expansionmodel_Representation3 = expansionmodel_Representation3
        self.expansionmodel_Representation1 = expansionmodel_Representation1 if expansionmodel_Representation1 is not None else set()
        self.expansionmodel_Representation7 = expansionmodel_Representation7
        self.expansionmodel_Representation14 = expansionmodel_Representation14
        
    @property
    def graphicalElementType(self) -> str:
        return self.__graphicalElementType

    @graphicalElementType.setter
    def graphicalElementType(self, graphicalElementType: str):
        self.__graphicalElementType = graphicalElementType

    @property
    def expansionmodel_Representation7(self):
        return self.__expansionmodel_Representation7

    @expansionmodel_Representation7.setter
    def expansionmodel_Representation7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expansionmodel_Representation__expansionmodel_Representation7", None)
        self.__expansionmodel_Representation7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expansionmodel_InducedRepresentation6"):
                opp_val = getattr(old_value, "expansionmodel_InducedRepresentation6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expansionmodel_InducedRepresentation6"):
                opp_val = getattr(value, "expansionmodel_InducedRepresentation6", None)
                if opp_val is None:
                    setattr(value, "expansionmodel_InducedRepresentation6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def expansionmodel_Representation14(self):
        return self.__expansionmodel_Representation14

    @expansionmodel_Representation14.setter
    def expansionmodel_Representation14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expansionmodel_Representation__expansionmodel_Representation14", None)
        self.__expansionmodel_Representation14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expansionmodel_UseContext"):
                opp_val = getattr(old_value, "expansionmodel_UseContext", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expansionmodel_UseContext"):
                opp_val = getattr(value, "expansionmodel_UseContext", None)
                if opp_val is None:
                    setattr(value, "expansionmodel_UseContext", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def expansionmodel_Representation(self):
        return self.__expansionmodel_Representation

    @expansionmodel_Representation.setter
    def expansionmodel_Representation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expansionmodel_Representation__expansionmodel_Representation", None)
        self.__expansionmodel_Representation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "expansionmodel_InducedRepresentation"):
                    opp_val = getattr(item, "expansionmodel_InducedRepresentation", None)
                    
                    if opp_val == self:
                        setattr(item, "expansionmodel_InducedRepresentation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "expansionmodel_InducedRepresentation"):
                    opp_val = getattr(item, "expansionmodel_InducedRepresentation", None)
                    
                    setattr(item, "expansionmodel_InducedRepresentation", self)
                    

    @property
    def expansionmodel_Representation3(self):
        return self.__expansionmodel_Representation3

    @expansionmodel_Representation3.setter
    def expansionmodel_Representation3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expansionmodel_Representation__expansionmodel_Representation3", None)
        self.__expansionmodel_Representation3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expansionmodel_Representation1"):
                opp_val = getattr(old_value, "expansionmodel_Representation1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expansionmodel_Representation1"):
                opp_val = getattr(value, "expansionmodel_Representation1", None)
                if opp_val is None:
                    setattr(value, "expansionmodel_Representation1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def expansionmodel_Representation1(self):
        return self.__expansionmodel_Representation1

    @expansionmodel_Representation1.setter
    def expansionmodel_Representation1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expansionmodel_Representation__expansionmodel_Representation1", None)
        self.__expansionmodel_Representation1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "expansionmodel_Representation3"):
                    opp_val = getattr(item, "expansionmodel_Representation3", None)
                    
                    if opp_val == self:
                        setattr(item, "expansionmodel_Representation3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "expansionmodel_Representation3"):
                    opp_val = getattr(item, "expansionmodel_Representation3", None)
                    
                    setattr(item, "expansionmodel_Representation3", self)
                    
