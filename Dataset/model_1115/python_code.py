from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class statechart_Variable:

    def __init__(self, name: str, type: str, statechart_Variable: "statechart_Model" = None, statechart_Variable7: "statechart_Node" = None):
        self.name = name
        self.type = type
        self.statechart_Variable = statechart_Variable
        self.statechart_Variable7 = statechart_Variable7
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statechart_Variable(self):
        return self.__statechart_Variable

    @statechart_Variable.setter
    def statechart_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Variable__statechart_Variable", None)
        self.__statechart_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechart_Model4"):
                opp_val = getattr(old_value, "statechart_Model4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechart_Model4"):
                opp_val = getattr(value, "statechart_Model4", None)
                if opp_val is None:
                    setattr(value, "statechart_Model4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statechart_Variable7(self):
        return self.__statechart_Variable7

    @statechart_Variable7.setter
    def statechart_Variable7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Variable__statechart_Variable7", None)
        self.__statechart_Variable7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechart_Node6"):
                opp_val = getattr(old_value, "statechart_Node6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechart_Node6"):
                opp_val = getattr(value, "statechart_Node6", None)
                if opp_val is None:
                    setattr(value, "statechart_Node6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statechart_Transition:

    def __init__(self, TE: str, name: str, metadata: str, statechart_Transition: "statechart_Model" = None, statechart_Transition14: "statechart_Node" = None, statechart_Transition17: "statechart_Node" = None):
        self.TE = TE
        self.name = name
        self.metadata = metadata
        self.statechart_Transition = statechart_Transition
        self.statechart_Transition14 = statechart_Transition14
        self.statechart_Transition17 = statechart_Transition17
        
    @property
    def metadata(self) -> str:
        return self.__metadata

    @metadata.setter
    def metadata(self, metadata: str):
        self.__metadata = metadata

    @property
    def TE(self) -> str:
        return self.__TE

    @TE.setter
    def TE(self, TE: str):
        self.__TE = TE

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statechart_Transition(self):
        return self.__statechart_Transition

    @statechart_Transition.setter
    def statechart_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Transition__statechart_Transition", None)
        self.__statechart_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechart_Model2"):
                opp_val = getattr(old_value, "statechart_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechart_Model2"):
                opp_val = getattr(value, "statechart_Model2", None)
                if opp_val is None:
                    setattr(value, "statechart_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statechart_Transition17(self):
        return self.__statechart_Transition17

    @statechart_Transition17.setter
    def statechart_Transition17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Transition__statechart_Transition17", None)
        self.__statechart_Transition17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechart_Node18"):
                opp_val = getattr(old_value, "statechart_Node18", None)
                if opp_val == self:
                    setattr(old_value, "statechart_Node18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechart_Node18"):
                opp_val = getattr(value, "statechart_Node18", None)
                setattr(value, "statechart_Node18", self)

    @property
    def statechart_Transition14(self):
        return self.__statechart_Transition14

    @statechart_Transition14.setter
    def statechart_Transition14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Transition__statechart_Transition14", None)
        self.__statechart_Transition14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechart_Node15"):
                opp_val = getattr(old_value, "statechart_Node15", None)
                if opp_val == self:
                    setattr(old_value, "statechart_Node15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechart_Node15"):
                opp_val = getattr(value, "statechart_Node15", None)
                setattr(value, "statechart_Node15", self)

class statechart_Node:

    def __init__(self, name: str, actions: str, metadata: str, label: str, type: str, activity: str, statechart_Node: "statechart_Model" = None, Node12: "statechart_Node" = None, Children: "statechart_Node" = None, statechart_Node15: "statechart_Transition" = None, statechart_Node18: "statechart_Transition" = None, statechart_Node6: set["statechart_Variable"] = None, Node: "statechart_Node" = None, Father: set["statechart_Node"] = None):
        self.name = name
        self.actions = actions
        self.metadata = metadata
        self.label = label
        self.type = type
        self.activity = activity
        self.statechart_Node = statechart_Node
        self.Node12 = Node12
        self.Children = Children
        self.statechart_Node15 = statechart_Node15
        self.statechart_Node18 = statechart_Node18
        self.statechart_Node6 = statechart_Node6 if statechart_Node6 is not None else set()
        self.Node = Node
        self.Father = Father if Father is not None else set()
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def metadata(self) -> str:
        return self.__metadata

    @metadata.setter
    def metadata(self, metadata: str):
        self.__metadata = metadata

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def activity(self) -> str:
        return self.__activity

    @activity.setter
    def activity(self, activity: str):
        self.__activity = activity

    @property
    def actions(self) -> str:
        return self.__actions

    @actions.setter
    def actions(self, actions: str):
        self.__actions = actions

    @property
    def statechart_Node18(self):
        return self.__statechart_Node18

    @statechart_Node18.setter
    def statechart_Node18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Node__statechart_Node18", None)
        self.__statechart_Node18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechart_Transition17"):
                opp_val = getattr(old_value, "statechart_Transition17", None)
                if opp_val == self:
                    setattr(old_value, "statechart_Transition17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechart_Transition17"):
                opp_val = getattr(value, "statechart_Transition17", None)
                setattr(value, "statechart_Transition17", self)

    @property
    def Father(self):
        return self.__Father

    @Father.setter
    def Father(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Node__Father", None)
        self.__Father = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Node"):
                    opp_val = getattr(item, "Node", None)
                    
                    if opp_val == self:
                        setattr(item, "Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Node"):
                    opp_val = getattr(item, "Node", None)
                    
                    setattr(item, "Node", self)
                    

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Father"):
                opp_val = getattr(old_value, "Father", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Father"):
                opp_val = getattr(value, "Father", None)
                if opp_val is None:
                    setattr(value, "Father", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statechart_Node6(self):
        return self.__statechart_Node6

    @statechart_Node6.setter
    def statechart_Node6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Node__statechart_Node6", None)
        self.__statechart_Node6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statechart_Variable7"):
                    opp_val = getattr(item, "statechart_Variable7", None)
                    
                    if opp_val == self:
                        setattr(item, "statechart_Variable7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statechart_Variable7"):
                    opp_val = getattr(item, "statechart_Variable7", None)
                    
                    setattr(item, "statechart_Variable7", self)
                    

    @property
    def Children(self):
        return self.__Children

    @Children.setter
    def Children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Node__Children", None)
        self.__Children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node12"):
                opp_val = getattr(old_value, "Node12", None)
                if opp_val == self:
                    setattr(old_value, "Node12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node12"):
                opp_val = getattr(value, "Node12", None)
                setattr(value, "Node12", self)

    @property
    def Node12(self):
        return self.__Node12

    @Node12.setter
    def Node12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Node__Node12", None)
        self.__Node12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Children"):
                opp_val = getattr(old_value, "Children", None)
                if opp_val == self:
                    setattr(old_value, "Children", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Children"):
                opp_val = getattr(value, "Children", None)
                setattr(value, "Children", self)

    @property
    def statechart_Node(self):
        return self.__statechart_Node

    @statechart_Node.setter
    def statechart_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Node__statechart_Node", None)
        self.__statechart_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechart_Model"):
                opp_val = getattr(old_value, "statechart_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechart_Model"):
                opp_val = getattr(value, "statechart_Model", None)
                if opp_val is None:
                    setattr(value, "statechart_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statechart_Node15(self):
        return self.__statechart_Node15

    @statechart_Node15.setter
    def statechart_Node15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Node__statechart_Node15", None)
        self.__statechart_Node15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechart_Transition14"):
                opp_val = getattr(old_value, "statechart_Transition14", None)
                if opp_val == self:
                    setattr(old_value, "statechart_Transition14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechart_Transition14"):
                opp_val = getattr(value, "statechart_Transition14", None)
                setattr(value, "statechart_Transition14", self)

class statechart_Model:

    def __init__(self, name: str, description: str, metadata: str, statechart_Model: set["statechart_Node"] = None, statechart_Model2: set["statechart_Transition"] = None, statechart_Model4: set["statechart_Variable"] = None):
        self.name = name
        self.description = description
        self.metadata = metadata
        self.statechart_Model = statechart_Model if statechart_Model is not None else set()
        self.statechart_Model2 = statechart_Model2 if statechart_Model2 is not None else set()
        self.statechart_Model4 = statechart_Model4 if statechart_Model4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metadata(self) -> str:
        return self.__metadata

    @metadata.setter
    def metadata(self, metadata: str):
        self.__metadata = metadata

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def statechart_Model4(self):
        return self.__statechart_Model4

    @statechart_Model4.setter
    def statechart_Model4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Model__statechart_Model4", None)
        self.__statechart_Model4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statechart_Variable"):
                    opp_val = getattr(item, "statechart_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "statechart_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statechart_Variable"):
                    opp_val = getattr(item, "statechart_Variable", None)
                    
                    setattr(item, "statechart_Variable", self)
                    

    @property
    def statechart_Model(self):
        return self.__statechart_Model

    @statechart_Model.setter
    def statechart_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Model__statechart_Model", None)
        self.__statechart_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statechart_Node"):
                    opp_val = getattr(item, "statechart_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "statechart_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statechart_Node"):
                    opp_val = getattr(item, "statechart_Node", None)
                    
                    setattr(item, "statechart_Node", self)
                    

    @property
    def statechart_Model2(self):
        return self.__statechart_Model2

    @statechart_Model2.setter
    def statechart_Model2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Model__statechart_Model2", None)
        self.__statechart_Model2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statechart_Transition"):
                    opp_val = getattr(item, "statechart_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "statechart_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statechart_Transition"):
                    opp_val = getattr(item, "statechart_Transition", None)
                    
                    setattr(item, "statechart_Transition", self)
                    
