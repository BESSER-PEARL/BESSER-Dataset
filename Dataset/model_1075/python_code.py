from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Arc:

    pass
class PetriNet_Arc(ABC):

    pass
class PetriNet_PTArc(Arc):

    pass
class PetriNet_Net:

    pass
class PetriNet_Place:

    pass
class PetriNet_Transition:

    pass
class PetriNet_TPArc(Arc):

    pass