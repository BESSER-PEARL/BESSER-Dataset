from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Label:

    pass
class cpndefinition_CPNInscription(Label):

    def __init__(self, text: str):
        self.text = text
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


class CPNInscription:

    pass
class cpndefinition_Sort(CPNInscription):

    pass
class Page:

    pass
class cpndefinition_Page(Page):

    pass
class cpndefinition_Guard(CPNInscription):

    pass
class Transition:

    pass
class cpndefinition_Transition(Transition):

    pass
class cpndefinition_ArcExpression(CPNInscription):

    pass
class Arc:

    pass
class cpndefinition_Arc(Arc):

    pass
class cpndefinition_InitialMarking(CPNInscription):

    pass
class Place:

    pass
class cpndefinition_Place(Place):

    pass
class PetriNetType:

    pass
class cpndefinition_CPN(PetriNetType):

    pass