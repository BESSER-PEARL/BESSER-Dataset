from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Port:

    pass
class ComponentLanguageShallow_OutPort(Port):

    pass
class ComponentLanguageShallow_InPort(Port):

    pass
class ComponentLanguageShallow_Connector:

    pass
class ComponentLanguageShallow_Port(ABC):

    pass
class ComponentLanguageShallow_Component:

    pass