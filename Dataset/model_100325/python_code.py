from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class LabeledElement:

    pass
class PNML_Name(LabeledElement):

    pass
class Label:

    pass
class NetContentElement:

    pass
class PNML_Transition(NetContentElement):

    pass
class PNML_Place(NetContentElement):

    pass
class IdedElement:

    pass
class PNML_NetElement(IdedElement):

    pass
class NetElement:

    pass
class URI:

    pass
class LocatedElement:

    pass
class PNML_LabeledElement(LocatedElement):

    pass
class PNML_PNMLDocument(LocatedElement):

    pass
class PNML_Label(LocatedElement):

    def __init__(self, text: str, labels: "LabeledElement" = None):
        self.text = text
        self.labels = labels
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def labels(self):
        return self.__labels

    @labels.setter
    def labels(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_Label__labels", None)
        self.__labels = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LabeledElement"):
                opp_val = getattr(old_value, "LabeledElement", None)
                if opp_val == self:
                    setattr(old_value, "LabeledElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LabeledElement"):
                opp_val = getattr(value, "LabeledElement", None)
                setattr(value, "LabeledElement", self)

class PNML_URI(LocatedElement):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class PNML_IdedElement(LocatedElement):

    def __init__(self, id: str):
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


class PNML_NetContent(LocatedElement):

    pass
class Name:

    pass
class NetContent:

    pass
class PNML_Arc(IdedElement, NetContent):

    pass
class PNML_NetContentElement(IdedElement, NetContent):

    pass
class PNMLDocument:

    pass
class PNML_LocatedElement(ABC):

    def __init__(self, location: str):
        self.location = location
        
        pass
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

