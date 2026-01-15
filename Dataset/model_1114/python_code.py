from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class stateChart_Model:

    def __init__(self, name: str, description: str, metadata: str, stateChart_Model: set["stateChart_Node"] = None, stateChart_Model14: set["stateChart_Variable"] = None, stateChart_Model17: set["stateChart_Transition"] = None):
        self.name = name
        self.description = description
        self.metadata = metadata
        self.stateChart_Model = stateChart_Model if stateChart_Model is not None else set()
        self.stateChart_Model14 = stateChart_Model14 if stateChart_Model14 is not None else set()
        self.stateChart_Model17 = stateChart_Model17 if stateChart_Model17 is not None else set()
        
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
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stateChart_Model(self):
        return self.__stateChart_Model

    @stateChart_Model.setter
    def stateChart_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateChart_Model__stateChart_Model", None)
        self.__stateChart_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stateChart_Node12"):
                    opp_val = getattr(item, "stateChart_Node12", None)
                    
                    if opp_val == self:
                        setattr(item, "stateChart_Node12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stateChart_Node12"):
                    opp_val = getattr(item, "stateChart_Node12", None)
                    
                    setattr(item, "stateChart_Node12", self)
                    

    @property
    def stateChart_Model14(self):
        return self.__stateChart_Model14

    @stateChart_Model14.setter
    def stateChart_Model14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateChart_Model__stateChart_Model14", None)
        self.__stateChart_Model14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stateChart_Variable15"):
                    opp_val = getattr(item, "stateChart_Variable15", None)
                    
                    if opp_val == self:
                        setattr(item, "stateChart_Variable15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stateChart_Variable15"):
                    opp_val = getattr(item, "stateChart_Variable15", None)
                    
                    setattr(item, "stateChart_Variable15", self)
                    

    @property
    def stateChart_Model17(self):
        return self.__stateChart_Model17

    @stateChart_Model17.setter
    def stateChart_Model17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateChart_Model__stateChart_Model17", None)
        self.__stateChart_Model17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stateChart_Transition18"):
                    opp_val = getattr(item, "stateChart_Transition18", None)
                    
                    if opp_val == self:
                        setattr(item, "stateChart_Transition18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stateChart_Transition18"):
                    opp_val = getattr(item, "stateChart_Transition18", None)
                    
                    setattr(item, "stateChart_Transition18", self)
                    

class stateChart_Transition:

    def __init__(self, TE: str, name: str, metadata: str, stateChart_Transition: "stateChart_Node" = None, stateChart_Transition10: "stateChart_Node" = None, stateChart_Transition18: "stateChart_Model" = None, stateChart_Transition20: "stateChart_Node" = None, stateChart_Transition23: "stateChart_Node" = None):
        self.TE = TE
        self.name = name
        self.metadata = metadata
        self.stateChart_Transition = stateChart_Transition
        self.stateChart_Transition10 = stateChart_Transition10
        self.stateChart_Transition18 = stateChart_Transition18
        self.stateChart_Transition20 = stateChart_Transition20
        self.stateChart_Transition23 = stateChart_Transition23
        
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
    def metadata(self) -> str:
        return self.__metadata

    @metadata.setter
    def metadata(self, metadata: str):
        self.__metadata = metadata

    @property
    def stateChart_Transition18(self):
        return self.__stateChart_Transition18

    @stateChart_Transition18.setter
    def stateChart_Transition18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateChart_Transition__stateChart_Transition18", None)
        self.__stateChart_Transition18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateChart_Model17"):
                opp_val = getattr(old_value, "stateChart_Model17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateChart_Model17"):
                opp_val = getattr(value, "stateChart_Model17", None)
                if opp_val is None:
                    setattr(value, "stateChart_Model17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stateChart_Transition23(self):
        return self.__stateChart_Transition23

    @stateChart_Transition23.setter
    def stateChart_Transition23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateChart_Transition__stateChart_Transition23", None)
        self.__stateChart_Transition23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateChart_Node24"):
                opp_val = getattr(old_value, "stateChart_Node24", None)
                if opp_val == self:
                    setattr(old_value, "stateChart_Node24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateChart_Node24"):
                opp_val = getattr(value, "stateChart_Node24", None)
                setattr(value, "stateChart_Node24", self)

    @property
    def stateChart_Transition20(self):
        return self.__stateChart_Transition20

    @stateChart_Transition20.setter
    def stateChart_Transition20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateChart_Transition__stateChart_Transition20", None)
        self.__stateChart_Transition20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateChart_Node21"):
                opp_val = getattr(old_value, "stateChart_Node21", None)
                if opp_val == self:
                    setattr(old_value, "stateChart_Node21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateChart_Node21"):
                opp_val = getattr(value, "stateChart_Node21", None)
                setattr(value, "stateChart_Node21", self)

    @property
    def stateChart_Transition10(self):
        return self.__stateChart_Transition10

    @stateChart_Transition10.setter
    def stateChart_Transition10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateChart_Transition__stateChart_Transition10", None)
        self.__stateChart_Transition10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateChart_Node9"):
                opp_val = getattr(old_value, "stateChart_Node9", None)
                if opp_val == self:
                    setattr(old_value, "stateChart_Node9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateChart_Node9"):
                opp_val = getattr(value, "stateChart_Node9", None)
                setattr(value, "stateChart_Node9", self)

    @property
    def stateChart_Transition(self):
        return self.__stateChart_Transition

    @stateChart_Transition.setter
    def stateChart_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateChart_Transition__stateChart_Transition", None)
        self.__stateChart_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateChart_Node7"):
                opp_val = getattr(old_value, "stateChart_Node7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateChart_Node7"):
                opp_val = getattr(value, "stateChart_Node7", None)
                if opp_val is None:
                    setattr(value, "stateChart_Node7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class stateChart_Node:

    def __init__(self, name: str, label: str, type: str, activity: str, actions: str, metadata: str, stateChart_Node: set["stateChart_Variable"] = None, Node: "stateChart_Node" = None, Father: set["stateChart_Node"] = None, Node5: "stateChart_Node" = None, Children: "stateChart_Node" = None, stateChart_Node7: set["stateChart_Transition"] = None, stateChart_Node9: "stateChart_Transition" = None, stateChart_Node12: "stateChart_Model" = None, stateChart_Node21: "stateChart_Transition" = None, stateChart_Node24: "stateChart_Transition" = None):
        self.name = name
        self.label = label
        self.type = type
        self.activity = activity
        self.actions = actions
        self.metadata = metadata
        self.stateChart_Node = stateChart_Node if stateChart_Node is not None else set()
        self.Node = Node
        self.Father = Father if Father is not None else set()
        self.Node5 = Node5
        self.Children = Children
        self.stateChart_Node7 = stateChart_Node7 if stateChart_Node7 is not None else set()
        self.stateChart_Node9 = stateChart_Node9
        self.stateChart_Node12 = stateChart_Node12
        self.stateChart_Node21 = stateChart_Node21
        self.stateChart_Node24 = stateChart_Node24
        
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
    def actions(self) -> str:
        return self.__actions

    @actions.setter
    def actions(self, actions: str):
        self.__actions = actions

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def activity(self) -> str:
        return self.__activity

    @activity.setter
    def activity(self, activity: str):
        self.__activity = activity

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Node5(self):
        return self.__Node5

    @Node5.setter
    def Node5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateChart_Node__Node5", None)
        self.__Node5 = value
        
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
    def stateChart_Node21(self):
        return self.__stateChart_Node21

    @stateChart_Node21.setter
    def stateChart_Node21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateChart_Node__stateChart_Node21", None)
        self.__stateChart_Node21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateChart_Transition20"):
                opp_val = getattr(old_value, "stateChart_Transition20", None)
                if opp_val == self:
                    setattr(old_value, "stateChart_Transition20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateChart_Transition20"):
                opp_val = getattr(value, "stateChart_Transition20", None)
                setattr(value, "stateChart_Transition20", self)

    @property
    def Children(self):
        return self.__Children

    @Children.setter
    def Children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateChart_Node__Children", None)
        self.__Children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node5"):
                opp_val = getattr(old_value, "Node5", None)
                if opp_val == self:
                    setattr(old_value, "Node5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node5"):
                opp_val = getattr(value, "Node5", None)
                setattr(value, "Node5", self)

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateChart_Node__Node", None)
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
    def stateChart_Node12(self):
        return self.__stateChart_Node12

    @stateChart_Node12.setter
    def stateChart_Node12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateChart_Node__stateChart_Node12", None)
        self.__stateChart_Node12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateChart_Model"):
                opp_val = getattr(old_value, "stateChart_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateChart_Model"):
                opp_val = getattr(value, "stateChart_Model", None)
                if opp_val is None:
                    setattr(value, "stateChart_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stateChart_Node7(self):
        return self.__stateChart_Node7

    @stateChart_Node7.setter
    def stateChart_Node7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateChart_Node__stateChart_Node7", None)
        self.__stateChart_Node7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stateChart_Transition"):
                    opp_val = getattr(item, "stateChart_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "stateChart_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stateChart_Transition"):
                    opp_val = getattr(item, "stateChart_Transition", None)
                    
                    setattr(item, "stateChart_Transition", self)
                    

    @property
    def Father(self):
        return self.__Father

    @Father.setter
    def Father(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateChart_Node__Father", None)
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
    def stateChart_Node(self):
        return self.__stateChart_Node

    @stateChart_Node.setter
    def stateChart_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateChart_Node__stateChart_Node", None)
        self.__stateChart_Node = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stateChart_Variable"):
                    opp_val = getattr(item, "stateChart_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "stateChart_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stateChart_Variable"):
                    opp_val = getattr(item, "stateChart_Variable", None)
                    
                    setattr(item, "stateChart_Variable", self)
                    

    @property
    def stateChart_Node9(self):
        return self.__stateChart_Node9

    @stateChart_Node9.setter
    def stateChart_Node9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateChart_Node__stateChart_Node9", None)
        self.__stateChart_Node9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateChart_Transition10"):
                opp_val = getattr(old_value, "stateChart_Transition10", None)
                if opp_val == self:
                    setattr(old_value, "stateChart_Transition10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateChart_Transition10"):
                opp_val = getattr(value, "stateChart_Transition10", None)
                setattr(value, "stateChart_Transition10", self)

    @property
    def stateChart_Node24(self):
        return self.__stateChart_Node24

    @stateChart_Node24.setter
    def stateChart_Node24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateChart_Node__stateChart_Node24", None)
        self.__stateChart_Node24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateChart_Transition23"):
                opp_val = getattr(old_value, "stateChart_Transition23", None)
                if opp_val == self:
                    setattr(old_value, "stateChart_Transition23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateChart_Transition23"):
                opp_val = getattr(value, "stateChart_Transition23", None)
                setattr(value, "stateChart_Transition23", self)

class stateChart_Variable:

    def __init__(self, name: str, type: str, stateChart_Variable: "stateChart_Node" = None, stateChart_Variable15: "stateChart_Model" = None):
        self.name = name
        self.type = type
        self.stateChart_Variable = stateChart_Variable
        self.stateChart_Variable15 = stateChart_Variable15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def stateChart_Variable(self):
        return self.__stateChart_Variable

    @stateChart_Variable.setter
    def stateChart_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateChart_Variable__stateChart_Variable", None)
        self.__stateChart_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateChart_Node"):
                opp_val = getattr(old_value, "stateChart_Node", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateChart_Node"):
                opp_val = getattr(value, "stateChart_Node", None)
                if opp_val is None:
                    setattr(value, "stateChart_Node", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stateChart_Variable15(self):
        return self.__stateChart_Variable15

    @stateChart_Variable15.setter
    def stateChart_Variable15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateChart_Variable__stateChart_Variable15", None)
        self.__stateChart_Variable15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateChart_Model14"):
                opp_val = getattr(old_value, "stateChart_Model14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateChart_Model14"):
                opp_val = getattr(value, "stateChart_Model14", None)
                if opp_val is None:
                    setattr(value, "stateChart_Model14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
