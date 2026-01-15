from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Node:

    pass
class processModels_Task(Node):

    def __init__(self):
        
    def name(self) -> str:
        # TODO: Implement name method
        pass

class processModels_Node(ABC):

    pass
class processModels_ProcessModel:

    def __init__(self):
        
    def terminatingTasks(self) -> str:
        # TODO: Implement terminatingTasks method
        pass

    def edges(self) -> str:
        # TODO: Implement edges method
        pass

    def nodes(self) -> str:
        # TODO: Implement nodes method
        pass

class processModels_FlowEdge:

    def __init__(self):
        
    def output(self) -> Node:
        # TODO: Implement output method
        pass

    def input(self) -> Node:
        # TODO: Implement input method
        pass

class Task:

    pass
class processModels_CompositeTask(Task):

    pass