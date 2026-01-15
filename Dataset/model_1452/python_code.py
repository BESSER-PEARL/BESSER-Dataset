from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class tree_Diagram:

    pass
class tree_Edge:

    pass
class tree_Node:

    def __init__(self, name: str, tree_Node: "tree_Diagram" = None, tree_Node5: "tree_Node" = None, tree_Node3: set["tree_Node"] = None, tree_Node8: "tree_Edge" = None, tree_Node11: "tree_Edge" = None):
        self.name = name
        self.tree_Node = tree_Node
        self.tree_Node5 = tree_Node5
        self.tree_Node3 = tree_Node3 if tree_Node3 is not None else set()
        self.tree_Node8 = tree_Node8
        self.tree_Node11 = tree_Node11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tree_Node3(self):
        return self.__tree_Node3

    @tree_Node3.setter
    def tree_Node3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_Node__tree_Node3", None)
        self.__tree_Node3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tree_Node5"):
                    opp_val = getattr(item, "tree_Node5", None)
                    
                    if opp_val == self:
                        setattr(item, "tree_Node5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tree_Node5"):
                    opp_val = getattr(item, "tree_Node5", None)
                    
                    setattr(item, "tree_Node5", self)
                    

    @property
    def tree_Node8(self):
        return self.__tree_Node8

    @tree_Node8.setter
    def tree_Node8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_Node__tree_Node8", None)
        self.__tree_Node8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tree_Edge7"):
                opp_val = getattr(old_value, "tree_Edge7", None)
                if opp_val == self:
                    setattr(old_value, "tree_Edge7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tree_Edge7"):
                opp_val = getattr(value, "tree_Edge7", None)
                setattr(value, "tree_Edge7", self)

    @property
    def tree_Node5(self):
        return self.__tree_Node5

    @tree_Node5.setter
    def tree_Node5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_Node__tree_Node5", None)
        self.__tree_Node5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tree_Node3"):
                opp_val = getattr(old_value, "tree_Node3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tree_Node3"):
                opp_val = getattr(value, "tree_Node3", None)
                if opp_val is None:
                    setattr(value, "tree_Node3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tree_Node11(self):
        return self.__tree_Node11

    @tree_Node11.setter
    def tree_Node11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_Node__tree_Node11", None)
        self.__tree_Node11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tree_Edge10"):
                opp_val = getattr(old_value, "tree_Edge10", None)
                if opp_val == self:
                    setattr(old_value, "tree_Edge10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tree_Edge10"):
                opp_val = getattr(value, "tree_Edge10", None)
                setattr(value, "tree_Edge10", self)

    @property
    def tree_Node(self):
        return self.__tree_Node

    @tree_Node.setter
    def tree_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_Node__tree_Node", None)
        self.__tree_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tree_Diagram"):
                opp_val = getattr(old_value, "tree_Diagram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tree_Diagram"):
                opp_val = getattr(value, "tree_Diagram", None)
                if opp_val is None:
                    setattr(value, "tree_Diagram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
