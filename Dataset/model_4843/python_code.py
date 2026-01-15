from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Relationship:

    pass
class ArchimateApplication_Aggregation(Relationship):

    pass
class ArchimateApplication_Access(Relationship):

    pass
class ArchimateApplication_UsedBy(Relationship):

    pass
class ArchimateApplication_Composition(Relationship):

    pass
class ArchimateApplication_Assignment(Relationship):

    pass
class ArchimateApplication_Realization(Relationship):

    pass
class ArchimateApplication_Flow(Relationship):

    pass
class ArchimateApplication_Association(Relationship):

    pass
class ArchimateApplication_Specialization(Relationship):

    pass
class ArchimateApplication_Triggering(Relationship):

    pass
class NodeElement:

    pass
class ArchimateApplication_ApplicationFunction(NodeElement):

    pass
class ArchimateApplication_Grouping(NodeElement):

    pass
class ArchimateApplication_ApplicationInteraction(NodeElement):

    pass
class ArchimateApplication_DataObject(NodeElement):

    pass
class ArchimateApplication_ApplicationCollaboration(NodeElement):

    pass
class ArchimateApplication_ApplicationService(NodeElement):

    pass
class ArchimateApplication_ApplicationInterface(NodeElement):

    pass
class ArchimateApplication_ApplicationComponent(NodeElement):

    pass
class ArchimateApplication_NodeElement(ABC):

    pass
class ArchimateApplication_Relationship(ABC):

    pass
class ArchimateApplication_Junction(NodeElement):

    pass