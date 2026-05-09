from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class processModels_FlowEdge:

    def __init__(self):
        
        pass
    def output(self) :
        # TODO: Implement output method
        pass

    def input(self) :
        # TODO: Implement input method
        pass

class Task:

    pass
class processModels_CompositeTask(Task):

    pass
class Node:

    pass
class processModels_Task(Node):

    def __init__(self):
        
        pass
    def name(self) :
        # TODO: Implement name method
        pass

class processModels_Node(ABC):

    pass
class processModels_ProcessModel:

    def __init__(self):
        
        pass
    def edges(self) :
        # TODO: Implement edges method
        pass

    def nodes(self) :
        # TODO: Implement nodes method
        pass

    def terminatingTasks(self) :
        # TODO: Implement terminatingTasks method
        pass
