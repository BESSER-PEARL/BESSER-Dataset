from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ArchimateTechnology_Relationship(ABC):

    pass
class Relationship:

    pass
class ArchimateTechnology_Association(Relationship):

    pass
class ArchimateTechnology_Realization(Relationship):

    pass
class ArchimateTechnology_Specialization(Relationship):

    pass
class ArchimateTechnology_Flow(Relationship):

    pass
class ArchimateTechnology_Access(Relationship):

    pass
class ArchimateTechnology_Assignment(Relationship):

    pass
class ArchimateTechnology_UsedBy(Relationship):

    pass
class ArchimateTechnology_Aggregation(Relationship):

    pass
class ArchimateTechnology_Triggering(Relationship):

    pass
class ArchimateTechnology_Composition(Relationship):

    pass
class ArchimateTechnology_Junction(Relationship):

    pass
class NodeElement:

    pass
class ArchimateTechnology_CommunicationPath(NodeElement):

    pass
class ArchimateTechnology_Grouping(NodeElement):

    pass
class ArchimateTechnology_InfrastructureService(NodeElement):

    pass
class ArchimateTechnology_Device(NodeElement):

    pass
class ArchimateTechnology_Artifact(NodeElement):

    pass
class ArchimateTechnology_InfrastructureInterface(NodeElement):

    pass
class ArchimateTechnology_Network(NodeElement):

    pass
class ArchimateTechnology_SystemSoftware(NodeElement):

    pass
class ArchimateTechnology_InfrastructureFunction(NodeElement):

    pass
class ArchimateTechnology_Node(NodeElement):

    pass
class ArchimateTechnology_NodeElement(ABC):

    pass