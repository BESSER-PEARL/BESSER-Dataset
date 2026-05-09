from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class petrinet_metamodel_Arc(ABC):

    def __init__(self, weight: int, petrinet_metamodel_Arc: "petrinet_metamodel_PetriNet" = None):
        self.weight = weight
        self.petrinet_metamodel_Arc = petrinet_metamodel_Arc
        
        pass
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight


    @property
    def petrinet_metamodel_Arc(self):
        return self.__petrinet_metamodel_Arc

    @petrinet_metamodel_Arc.setter
    def petrinet_metamodel_Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_metamodel_Arc__petrinet_metamodel_Arc", None)
        self.__petrinet_metamodel_Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_metamodel_PetriNet"):
                opp_val = getattr(old_value, "petrinet_metamodel_PetriNet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_metamodel_PetriNet"):
                opp_val = getattr(value, "petrinet_metamodel_PetriNet", None)
                if opp_val is None:
                    setattr(value, "petrinet_metamodel_PetriNet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Element:

    pass
class petrinet_metamodel_Transition(Element):

    pass
class petrinet_metamodel_Place(Element):

    def __init__(self, radius: int, fill_colour: str, coordinates: int, Place17: "petrinet_metamodel_PlaceToTransArc" = None, Place: "petrinet_metamodel_PetriNet" = None, target: set["petrinet_metamodel_TransToPlaceArc"] = None, source: set["petrinet_metamodel_PlaceToTransArc"] = None, Place25: "petrinet_metamodel_TransToPlaceArc" = None, places: "petrinet_metamodel_PetriNet" = None):
        self.radius = radius
        self.fill_colour = fill_colour
        self.coordinates = coordinates
        self.Place17 = Place17
        self.Place = Place
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        self.Place25 = Place25
        self.places = places
        
        pass
    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius: int):
        self.__radius = radius


    @property
    def fill_colour(self):
        return self.__fill_colour

    @fill_colour.setter
    def fill_colour(self, fill_colour: str):
        self.__fill_colour = fill_colour


    @property
    def coordinates(self):
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, coordinates: int):
        self.__coordinates = coordinates


    @property
    def Place(self):
        return self.__Place

    @Place.setter
    def Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_metamodel_Place__Place", None)
        self.__Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet"):
                opp_val = getattr(old_value, "petrinet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet"):
                opp_val = getattr(value, "petrinet", None)
                if opp_val is None:
                    setattr(value, "petrinet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Place25(self):
        return self.__Place25

    @Place25.setter
    def Place25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_metamodel_Place__Place25", None)
        self.__Place25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incoming24"):
                opp_val = getattr(old_value, "incoming24", None)
                if opp_val == self:
                    setattr(old_value, "incoming24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incoming24"):
                opp_val = getattr(value, "incoming24", None)
                setattr(value, "incoming24", self)

    @property
    def places(self):
        return self.__places

    @places.setter
    def places(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_metamodel_Place__places", None)
        self.__places = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet"):
                opp_val = getattr(old_value, "PetriNet", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet"):
                opp_val = getattr(value, "PetriNet", None)
                setattr(value, "PetriNet", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_metamodel_Place__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TransToPlaceArc"):
                    opp_val = getattr(item, "TransToPlaceArc", None)
                    
                    if opp_val == self:
                        setattr(item, "TransToPlaceArc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TransToPlaceArc"):
                    opp_val = getattr(item, "TransToPlaceArc", None)
                    
                    setattr(item, "TransToPlaceArc", self)
                    

    @property
    def Place17(self):
        return self.__Place17

    @Place17.setter
    def Place17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_metamodel_Place__Place17", None)
        self.__Place17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoing"):
                opp_val = getattr(old_value, "outgoing", None)
                if opp_val == self:
                    setattr(old_value, "outgoing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoing"):
                opp_val = getattr(value, "outgoing", None)
                setattr(value, "outgoing", self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_metamodel_Place__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PlaceToTransArc"):
                    opp_val = getattr(item, "PlaceToTransArc", None)
                    
                    if opp_val == self:
                        setattr(item, "PlaceToTransArc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PlaceToTransArc"):
                    opp_val = getattr(item, "PlaceToTransArc", None)
                    
                    setattr(item, "PlaceToTransArc", self)
                    

class petrinet_metamodel_PetriNet(Element):

    pass
class petrinet_metamodel_Element(ABC):

    def __init__(self, comments: str, name: str):
        self.comments = comments
        self.name = name
        
        pass
    @property
    def comments(self):
        return self.__comments

    @comments.setter
    def comments(self, comments: str):
        self.__comments = comments


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Arc:

    pass
class petrinet_metamodel_TransToPlaceArc(Arc):

    pass
class petrinet_metamodel_PlaceToTransArc(Arc):

    pass
class petrinet_metamodel_Rectangle:

    def __init__(self, start_end_coordinates: int, rectangle: "petrinet_metamodel_Transition" = None, Rectangle: "petrinet_metamodel_Transition" = None):
        self.start_end_coordinates = start_end_coordinates
        self.rectangle = rectangle
        self.Rectangle = Rectangle
        
        pass
    @property
    def start_end_coordinates(self):
        return self.__start_end_coordinates

    @start_end_coordinates.setter
    def start_end_coordinates(self, start_end_coordinates: int):
        self.__start_end_coordinates = start_end_coordinates


    @property
    def Rectangle(self):
        return self.__Rectangle

    @Rectangle.setter
    def Rectangle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_metamodel_Rectangle__Rectangle", None)
        self.__Rectangle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "belongs_to"):
                opp_val = getattr(old_value, "belongs_to", None)
                if opp_val == self:
                    setattr(old_value, "belongs_to", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "belongs_to"):
                opp_val = getattr(value, "belongs_to", None)
                setattr(value, "belongs_to", self)

    @property
    def rectangle(self):
        return self.__rectangle

    @rectangle.setter
    def rectangle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_metamodel_Rectangle__rectangle", None)
        self.__rectangle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Transition27"):
                opp_val = getattr(old_value, "Transition27", None)
                if opp_val == self:
                    setattr(old_value, "Transition27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Transition27"):
                opp_val = getattr(value, "Transition27", None)
                setattr(value, "Transition27", self)
