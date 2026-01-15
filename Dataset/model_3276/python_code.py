from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class sm_Observation:

    def __init__(self, time: str, Observation: "sm_StateMachine" = None, mark: "sm_State" = None, marks: "sm_StateMachine" = None, Observation13: "sm_State" = None):
        self.time = time
        self.Observation = Observation
        self.mark = mark
        self.marks = marks
        self.Observation13 = Observation13
        
    @property
    def time(self) -> str:
        return self.__time

    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def Observation(self):
        return self.__Observation

    @Observation.setter
    def Observation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Observation__Observation", None)
        self.__Observation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph8"):
                opp_val = getattr(old_value, "graph8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph8"):
                opp_val = getattr(value, "graph8", None)
                if opp_val is None:
                    setattr(value, "graph8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Observation__mark", None)
        self.__mark = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State23"):
                opp_val = getattr(old_value, "State23", None)
                if opp_val == self:
                    setattr(old_value, "State23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State23"):
                opp_val = getattr(value, "State23", None)
                setattr(value, "State23", self)

    @property
    def Observation13(self):
        return self.__Observation13

    @Observation13.setter
    def Observation13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Observation__Observation13", None)
        self.__Observation13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "node"):
                opp_val = getattr(old_value, "node", None)
                if opp_val == self:
                    setattr(old_value, "node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "node"):
                opp_val = getattr(value, "node", None)
                setattr(value, "node", self)

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Observation__marks", None)
        self.__marks = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine25"):
                opp_val = getattr(old_value, "StateMachine25", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine25"):
                opp_val = getattr(value, "StateMachine25", None)
                setattr(value, "StateMachine25", self)

class sm_Transition:

    def __init__(self, name: str, Transition: "sm_StateMachine" = None, edges: "sm_StateMachine" = None, sm_Transition: "sm_State" = None, sm_Transition18: "sm_State" = None):
        self.name = name
        self.Transition = Transition
        self.edges = edges
        self.sm_Transition = sm_Transition
        self.sm_Transition18 = sm_Transition18
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sm_Transition(self):
        return self.__sm_Transition

    @sm_Transition.setter
    def sm_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Transition__sm_Transition", None)
        self.__sm_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_State16"):
                opp_val = getattr(old_value, "sm_State16", None)
                if opp_val == self:
                    setattr(old_value, "sm_State16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_State16"):
                opp_val = getattr(value, "sm_State16", None)
                setattr(value, "sm_State16", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph6"):
                opp_val = getattr(old_value, "graph6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph6"):
                opp_val = getattr(value, "graph6", None)
                if opp_val is None:
                    setattr(value, "graph6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sm_Transition18(self):
        return self.__sm_Transition18

    @sm_Transition18.setter
    def sm_Transition18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Transition__sm_Transition18", None)
        self.__sm_Transition18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_State19"):
                opp_val = getattr(old_value, "sm_State19", None)
                if opp_val == self:
                    setattr(old_value, "sm_State19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_State19"):
                opp_val = getattr(value, "sm_State19", None)
                setattr(value, "sm_State19", self)

    @property
    def edges(self):
        return self.__edges

    @edges.setter
    def edges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Transition__edges", None)
        self.__edges = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine21"):
                opp_val = getattr(old_value, "StateMachine21", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine21"):
                opp_val = getattr(value, "StateMachine21", None)
                setattr(value, "StateMachine21", self)

class sm_State:

    def __init__(self, name: str, sm_State: "sm_StateMachine" = None, sm_State3: "sm_StateMachine" = None, State: "sm_StateMachine" = None, sm_State10: set["sm_StateMachine"] = None, State23: "sm_Observation" = None, node: "sm_Observation" = None, nodes: "sm_StateMachine" = None, sm_State16: "sm_Transition" = None, sm_State19: "sm_Transition" = None):
        self.name = name
        self.sm_State = sm_State
        self.sm_State3 = sm_State3
        self.State = State
        self.sm_State10 = sm_State10 if sm_State10 is not None else set()
        self.State23 = State23
        self.node = node
        self.nodes = nodes
        self.sm_State16 = sm_State16
        self.sm_State19 = sm_State19
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph"):
                opp_val = getattr(old_value, "graph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph"):
                opp_val = getattr(value, "graph", None)
                if opp_val is None:
                    setattr(value, "graph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sm_State19(self):
        return self.__sm_State19

    @sm_State19.setter
    def sm_State19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_State__sm_State19", None)
        self.__sm_State19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_Transition18"):
                opp_val = getattr(old_value, "sm_Transition18", None)
                if opp_val == self:
                    setattr(old_value, "sm_Transition18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_Transition18"):
                opp_val = getattr(value, "sm_Transition18", None)
                setattr(value, "sm_Transition18", self)

    @property
    def sm_State16(self):
        return self.__sm_State16

    @sm_State16.setter
    def sm_State16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_State__sm_State16", None)
        self.__sm_State16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_Transition"):
                opp_val = getattr(old_value, "sm_Transition", None)
                if opp_val == self:
                    setattr(old_value, "sm_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_Transition"):
                opp_val = getattr(value, "sm_Transition", None)
                setattr(value, "sm_Transition", self)

    @property
    def State23(self):
        return self.__State23

    @State23.setter
    def State23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_State__State23", None)
        self.__State23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mark"):
                opp_val = getattr(old_value, "mark", None)
                if opp_val == self:
                    setattr(old_value, "mark", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mark"):
                opp_val = getattr(value, "mark", None)
                setattr(value, "mark", self)

    @property
    def sm_State10(self):
        return self.__sm_State10

    @sm_State10.setter
    def sm_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_State__sm_State10", None)
        self.__sm_State10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sm_StateMachine11"):
                    opp_val = getattr(item, "sm_StateMachine11", None)
                    
                    if opp_val == self:
                        setattr(item, "sm_StateMachine11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sm_StateMachine11"):
                    opp_val = getattr(item, "sm_StateMachine11", None)
                    
                    setattr(item, "sm_StateMachine11", self)
                    

    @property
    def sm_State3(self):
        return self.__sm_State3

    @sm_State3.setter
    def sm_State3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_State__sm_State3", None)
        self.__sm_State3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_StateMachine2"):
                opp_val = getattr(old_value, "sm_StateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_StateMachine2"):
                opp_val = getattr(value, "sm_StateMachine2", None)
                if opp_val is None:
                    setattr(value, "sm_StateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sm_State(self):
        return self.__sm_State

    @sm_State.setter
    def sm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_State__sm_State", None)
        self.__sm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_StateMachine"):
                opp_val = getattr(old_value, "sm_StateMachine", None)
                if opp_val == self:
                    setattr(old_value, "sm_StateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_StateMachine"):
                opp_val = getattr(value, "sm_StateMachine", None)
                setattr(value, "sm_StateMachine", self)

    @property
    def nodes(self):
        return self.__nodes

    @nodes.setter
    def nodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_State__nodes", None)
        self.__nodes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine"):
                opp_val = getattr(old_value, "StateMachine", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine"):
                opp_val = getattr(value, "StateMachine", None)
                setattr(value, "StateMachine", self)

    @property
    def node(self):
        return self.__node

    @node.setter
    def node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_State__node", None)
        self.__node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Observation13"):
                opp_val = getattr(old_value, "Observation13", None)
                if opp_val == self:
                    setattr(old_value, "Observation13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Observation13"):
                opp_val = getattr(value, "Observation13", None)
                setattr(value, "Observation13", self)

class sm_StateMachine:

    def __init__(self, name: str, sm_StateMachine: "sm_State" = None, sm_StateMachine2: set["sm_State"] = None, graph: set["sm_State"] = None, graph6: set["sm_Transition"] = None, graph8: set["sm_Observation"] = None, sm_StateMachine11: "sm_State" = None, StateMachine21: "sm_Transition" = None, StateMachine25: "sm_Observation" = None, StateMachine: "sm_State" = None):
        self.name = name
        self.sm_StateMachine = sm_StateMachine
        self.sm_StateMachine2 = sm_StateMachine2 if sm_StateMachine2 is not None else set()
        self.graph = graph if graph is not None else set()
        self.graph6 = graph6 if graph6 is not None else set()
        self.graph8 = graph8 if graph8 is not None else set()
        self.sm_StateMachine11 = sm_StateMachine11
        self.StateMachine21 = StateMachine21
        self.StateMachine25 = StateMachine25
        self.StateMachine = StateMachine
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def graph6(self):
        return self.__graph6

    @graph6.setter
    def graph6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_StateMachine__graph6", None)
        self.__graph6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    setattr(item, "Transition", self)
                    

    @property
    def graph(self):
        return self.__graph

    @graph.setter
    def graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_StateMachine__graph", None)
        self.__graph = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "State"):
                    opp_val = getattr(item, "State", None)
                    
                    if opp_val == self:
                        setattr(item, "State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "State"):
                    opp_val = getattr(item, "State", None)
                    
                    setattr(item, "State", self)
                    

    @property
    def graph8(self):
        return self.__graph8

    @graph8.setter
    def graph8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_StateMachine__graph8", None)
        self.__graph8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Observation"):
                    opp_val = getattr(item, "Observation", None)
                    
                    if opp_val == self:
                        setattr(item, "Observation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Observation"):
                    opp_val = getattr(item, "Observation", None)
                    
                    setattr(item, "Observation", self)
                    

    @property
    def StateMachine(self):
        return self.__StateMachine

    @StateMachine.setter
    def StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_StateMachine__StateMachine", None)
        self.__StateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nodes"):
                opp_val = getattr(old_value, "nodes", None)
                if opp_val == self:
                    setattr(old_value, "nodes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nodes"):
                opp_val = getattr(value, "nodes", None)
                setattr(value, "nodes", self)

    @property
    def StateMachine21(self):
        return self.__StateMachine21

    @StateMachine21.setter
    def StateMachine21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_StateMachine__StateMachine21", None)
        self.__StateMachine21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edges"):
                opp_val = getattr(old_value, "edges", None)
                if opp_val == self:
                    setattr(old_value, "edges", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edges"):
                opp_val = getattr(value, "edges", None)
                setattr(value, "edges", self)

    @property
    def sm_StateMachine11(self):
        return self.__sm_StateMachine11

    @sm_StateMachine11.setter
    def sm_StateMachine11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_StateMachine__sm_StateMachine11", None)
        self.__sm_StateMachine11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_State10"):
                opp_val = getattr(old_value, "sm_State10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_State10"):
                opp_val = getattr(value, "sm_State10", None)
                if opp_val is None:
                    setattr(value, "sm_State10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sm_StateMachine2(self):
        return self.__sm_StateMachine2

    @sm_StateMachine2.setter
    def sm_StateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_StateMachine__sm_StateMachine2", None)
        self.__sm_StateMachine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sm_State3"):
                    opp_val = getattr(item, "sm_State3", None)
                    
                    if opp_val == self:
                        setattr(item, "sm_State3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sm_State3"):
                    opp_val = getattr(item, "sm_State3", None)
                    
                    setattr(item, "sm_State3", self)
                    

    @property
    def StateMachine25(self):
        return self.__StateMachine25

    @StateMachine25.setter
    def StateMachine25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_StateMachine__StateMachine25", None)
        self.__StateMachine25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "marks"):
                opp_val = getattr(old_value, "marks", None)
                if opp_val == self:
                    setattr(old_value, "marks", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "marks"):
                opp_val = getattr(value, "marks", None)
                setattr(value, "marks", self)

    @property
    def sm_StateMachine(self):
        return self.__sm_StateMachine

    @sm_StateMachine.setter
    def sm_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_StateMachine__sm_StateMachine", None)
        self.__sm_StateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_State"):
                opp_val = getattr(old_value, "sm_State", None)
                if opp_val == self:
                    setattr(old_value, "sm_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_State"):
                opp_val = getattr(value, "sm_State", None)
                setattr(value, "sm_State", self)
