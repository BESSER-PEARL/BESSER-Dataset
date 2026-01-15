from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class GraphWiki_Graph:

    def __init__(self, name: str, GraphWiki_Graph16: set["GraphWiki_Edge"] = None, GraphWiki_Graph: set["GraphWiki_Node"] = None):
        self.name = name
        self.GraphWiki_Graph16 = GraphWiki_Graph16 if GraphWiki_Graph16 is not None else set()
        self.GraphWiki_Graph = GraphWiki_Graph if GraphWiki_Graph is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def GraphWiki_Graph16(self):
        return self.__GraphWiki_Graph16

    @GraphWiki_Graph16.setter
    def GraphWiki_Graph16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphWiki_Graph__GraphWiki_Graph16", None)
        self.__GraphWiki_Graph16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GraphWiki_Edge17"):
                    opp_val = getattr(item, "GraphWiki_Edge17", None)
                    
                    if opp_val == self:
                        setattr(item, "GraphWiki_Edge17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GraphWiki_Edge17"):
                    opp_val = getattr(item, "GraphWiki_Edge17", None)
                    
                    setattr(item, "GraphWiki_Edge17", self)
                    

    @property
    def GraphWiki_Graph(self):
        return self.__GraphWiki_Graph

    @GraphWiki_Graph.setter
    def GraphWiki_Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphWiki_Graph__GraphWiki_Graph", None)
        self.__GraphWiki_Graph = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GraphWiki_Node14"):
                    opp_val = getattr(item, "GraphWiki_Node14", None)
                    
                    if opp_val == self:
                        setattr(item, "GraphWiki_Node14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GraphWiki_Node14"):
                    opp_val = getattr(item, "GraphWiki_Node14", None)
                    
                    setattr(item, "GraphWiki_Node14", self)
                    

class GraphWiki_Revision:

    def __init__(self, user: str, date: str, text_id: int, GraphWiki_Revision: "GraphWiki_Wiki" = None, GraphWiki_Revision20: "GraphWiki_Node" = None, Revision: "GraphWiki_Node" = None, revisions: "GraphWiki_Node" = None):
        self.user = user
        self.date = date
        self.text_id = text_id
        self.GraphWiki_Revision = GraphWiki_Revision
        self.GraphWiki_Revision20 = GraphWiki_Revision20
        self.Revision = Revision
        self.revisions = revisions
        
    @property
    def date(self) -> str:
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def text_id(self) -> int:
        return self.__text_id

    @text_id.setter
    def text_id(self, text_id: int):
        self.__text_id = text_id

    @property
    def user(self) -> str:
        return self.__user

    @user.setter
    def user(self, user: str):
        self.__user = user

    @property
    def GraphWiki_Revision(self):
        return self.__GraphWiki_Revision

    @GraphWiki_Revision.setter
    def GraphWiki_Revision(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphWiki_Revision__GraphWiki_Revision", None)
        self.__GraphWiki_Revision = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphWiki_Wiki12"):
                opp_val = getattr(old_value, "GraphWiki_Wiki12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphWiki_Wiki12"):
                opp_val = getattr(value, "GraphWiki_Wiki12", None)
                if opp_val is None:
                    setattr(value, "GraphWiki_Wiki12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def GraphWiki_Revision20(self):
        return self.__GraphWiki_Revision20

    @GraphWiki_Revision20.setter
    def GraphWiki_Revision20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphWiki_Revision__GraphWiki_Revision20", None)
        self.__GraphWiki_Revision20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphWiki_Node19"):
                opp_val = getattr(old_value, "GraphWiki_Node19", None)
                if opp_val == self:
                    setattr(old_value, "GraphWiki_Node19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphWiki_Node19"):
                opp_val = getattr(value, "GraphWiki_Node19", None)
                setattr(value, "GraphWiki_Node19", self)

    @property
    def Revision(self):
        return self.__Revision

    @Revision.setter
    def Revision(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphWiki_Revision__Revision", None)
        self.__Revision = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "node"):
                opp_val = getattr(old_value, "node", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "node"):
                opp_val = getattr(value, "node", None)
                if opp_val is None:
                    setattr(value, "node", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def revisions(self):
        return self.__revisions

    @revisions.setter
    def revisions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphWiki_Revision__revisions", None)
        self.__revisions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node"):
                opp_val = getattr(old_value, "Node", None)
                if opp_val == self:
                    setattr(old_value, "Node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node"):
                opp_val = getattr(value, "Node", None)
                setattr(value, "Node", self)

class GraphWiki_Edge:

    def __init__(self, type: str, GraphWiki_Edge17: "GraphWiki_Graph" = None, GraphWiki_Edge: "GraphWiki_Wiki" = None, GraphWiki_Edge23: "GraphWiki_Node" = None, GraphWiki_Edge26: "GraphWiki_Node" = None):
        self.type = type
        self.GraphWiki_Edge17 = GraphWiki_Edge17
        self.GraphWiki_Edge = GraphWiki_Edge
        self.GraphWiki_Edge23 = GraphWiki_Edge23
        self.GraphWiki_Edge26 = GraphWiki_Edge26
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def GraphWiki_Edge(self):
        return self.__GraphWiki_Edge

    @GraphWiki_Edge.setter
    def GraphWiki_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphWiki_Edge__GraphWiki_Edge", None)
        self.__GraphWiki_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphWiki_Wiki10"):
                opp_val = getattr(old_value, "GraphWiki_Wiki10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphWiki_Wiki10"):
                opp_val = getattr(value, "GraphWiki_Wiki10", None)
                if opp_val is None:
                    setattr(value, "GraphWiki_Wiki10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def GraphWiki_Edge26(self):
        return self.__GraphWiki_Edge26

    @GraphWiki_Edge26.setter
    def GraphWiki_Edge26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphWiki_Edge__GraphWiki_Edge26", None)
        self.__GraphWiki_Edge26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphWiki_Node27"):
                opp_val = getattr(old_value, "GraphWiki_Node27", None)
                if opp_val == self:
                    setattr(old_value, "GraphWiki_Node27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphWiki_Node27"):
                opp_val = getattr(value, "GraphWiki_Node27", None)
                setattr(value, "GraphWiki_Node27", self)

    @property
    def GraphWiki_Edge23(self):
        return self.__GraphWiki_Edge23

    @GraphWiki_Edge23.setter
    def GraphWiki_Edge23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphWiki_Edge__GraphWiki_Edge23", None)
        self.__GraphWiki_Edge23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphWiki_Node24"):
                opp_val = getattr(old_value, "GraphWiki_Node24", None)
                if opp_val == self:
                    setattr(old_value, "GraphWiki_Node24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphWiki_Node24"):
                opp_val = getattr(value, "GraphWiki_Node24", None)
                setattr(value, "GraphWiki_Node24", self)

    @property
    def GraphWiki_Edge17(self):
        return self.__GraphWiki_Edge17

    @GraphWiki_Edge17.setter
    def GraphWiki_Edge17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphWiki_Edge__GraphWiki_Edge17", None)
        self.__GraphWiki_Edge17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphWiki_Graph16"):
                opp_val = getattr(old_value, "GraphWiki_Graph16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphWiki_Graph16"):
                opp_val = getattr(value, "GraphWiki_Graph16", None)
                if opp_val is None:
                    setattr(value, "GraphWiki_Graph16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class GraphWiki_Node:

    def __init__(self, editions: int, title: str, type: str, node_id: int, visits: int, node_namespace: int, GraphWiki_Node: "GraphWiki_Wiki" = None, GraphWiki_Node14: "GraphWiki_Graph" = None, GraphWiki_Node24: "GraphWiki_Edge" = None, GraphWiki_Node19: "GraphWiki_Revision" = None, node: set["GraphWiki_Revision"] = None, GraphWiki_Node27: "GraphWiki_Edge" = None, Node: "GraphWiki_Revision" = None):
        self.editions = editions
        self.title = title
        self.type = type
        self.node_id = node_id
        self.visits = visits
        self.node_namespace = node_namespace
        self.GraphWiki_Node = GraphWiki_Node
        self.GraphWiki_Node14 = GraphWiki_Node14
        self.GraphWiki_Node24 = GraphWiki_Node24
        self.GraphWiki_Node19 = GraphWiki_Node19
        self.node = node if node is not None else set()
        self.GraphWiki_Node27 = GraphWiki_Node27
        self.Node = Node
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def visits(self) -> int:
        return self.__visits

    @visits.setter
    def visits(self, visits: int):
        self.__visits = visits

    @property
    def node_id(self) -> int:
        return self.__node_id

    @node_id.setter
    def node_id(self, node_id: int):
        self.__node_id = node_id

    @property
    def editions(self) -> int:
        return self.__editions

    @editions.setter
    def editions(self, editions: int):
        self.__editions = editions

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def node_namespace(self) -> int:
        return self.__node_namespace

    @node_namespace.setter
    def node_namespace(self, node_namespace: int):
        self.__node_namespace = node_namespace

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphWiki_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "revisions"):
                opp_val = getattr(old_value, "revisions", None)
                if opp_val == self:
                    setattr(old_value, "revisions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "revisions"):
                opp_val = getattr(value, "revisions", None)
                setattr(value, "revisions", self)

    @property
    def GraphWiki_Node14(self):
        return self.__GraphWiki_Node14

    @GraphWiki_Node14.setter
    def GraphWiki_Node14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphWiki_Node__GraphWiki_Node14", None)
        self.__GraphWiki_Node14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphWiki_Graph"):
                opp_val = getattr(old_value, "GraphWiki_Graph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphWiki_Graph"):
                opp_val = getattr(value, "GraphWiki_Graph", None)
                if opp_val is None:
                    setattr(value, "GraphWiki_Graph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def node(self):
        return self.__node

    @node.setter
    def node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphWiki_Node__node", None)
        self.__node = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Revision"):
                    opp_val = getattr(item, "Revision", None)
                    
                    if opp_val == self:
                        setattr(item, "Revision", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Revision"):
                    opp_val = getattr(item, "Revision", None)
                    
                    setattr(item, "Revision", self)
                    

    @property
    def GraphWiki_Node19(self):
        return self.__GraphWiki_Node19

    @GraphWiki_Node19.setter
    def GraphWiki_Node19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphWiki_Node__GraphWiki_Node19", None)
        self.__GraphWiki_Node19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphWiki_Revision20"):
                opp_val = getattr(old_value, "GraphWiki_Revision20", None)
                if opp_val == self:
                    setattr(old_value, "GraphWiki_Revision20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphWiki_Revision20"):
                opp_val = getattr(value, "GraphWiki_Revision20", None)
                setattr(value, "GraphWiki_Revision20", self)

    @property
    def GraphWiki_Node27(self):
        return self.__GraphWiki_Node27

    @GraphWiki_Node27.setter
    def GraphWiki_Node27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphWiki_Node__GraphWiki_Node27", None)
        self.__GraphWiki_Node27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphWiki_Edge26"):
                opp_val = getattr(old_value, "GraphWiki_Edge26", None)
                if opp_val == self:
                    setattr(old_value, "GraphWiki_Edge26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphWiki_Edge26"):
                opp_val = getattr(value, "GraphWiki_Edge26", None)
                setattr(value, "GraphWiki_Edge26", self)

    @property
    def GraphWiki_Node(self):
        return self.__GraphWiki_Node

    @GraphWiki_Node.setter
    def GraphWiki_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphWiki_Node__GraphWiki_Node", None)
        self.__GraphWiki_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphWiki_Wiki8"):
                opp_val = getattr(old_value, "GraphWiki_Wiki8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphWiki_Wiki8"):
                opp_val = getattr(value, "GraphWiki_Wiki8", None)
                if opp_val is None:
                    setattr(value, "GraphWiki_Wiki8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def GraphWiki_Node24(self):
        return self.__GraphWiki_Node24

    @GraphWiki_Node24.setter
    def GraphWiki_Node24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphWiki_Node__GraphWiki_Node24", None)
        self.__GraphWiki_Node24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphWiki_Edge23"):
                opp_val = getattr(old_value, "GraphWiki_Edge23", None)
                if opp_val == self:
                    setattr(old_value, "GraphWiki_Edge23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphWiki_Edge23"):
                opp_val = getattr(value, "GraphWiki_Edge23", None)
                setattr(value, "GraphWiki_Edge23", self)

class Graph:

    pass
class GraphWiki_IndexGraph(Graph):

    pass
class GraphWiki_Wiki:

    def __init__(self, title: str, GraphWiki_Wiki: "GraphWiki_IndexGraph" = None, GraphWiki_Wiki2: "GraphWiki_CategoryGraph" = None, GraphWiki_Wiki4: "GraphWiki_ArticleGraph" = None, GraphWiki_Wiki6: "GraphWiki_ClassificationGraph" = None, GraphWiki_Wiki8: set["GraphWiki_Node"] = None, GraphWiki_Wiki10: set["GraphWiki_Edge"] = None, GraphWiki_Wiki12: set["GraphWiki_Revision"] = None):
        self.title = title
        self.GraphWiki_Wiki = GraphWiki_Wiki
        self.GraphWiki_Wiki2 = GraphWiki_Wiki2
        self.GraphWiki_Wiki4 = GraphWiki_Wiki4
        self.GraphWiki_Wiki6 = GraphWiki_Wiki6
        self.GraphWiki_Wiki8 = GraphWiki_Wiki8 if GraphWiki_Wiki8 is not None else set()
        self.GraphWiki_Wiki10 = GraphWiki_Wiki10 if GraphWiki_Wiki10 is not None else set()
        self.GraphWiki_Wiki12 = GraphWiki_Wiki12 if GraphWiki_Wiki12 is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def GraphWiki_Wiki12(self):
        return self.__GraphWiki_Wiki12

    @GraphWiki_Wiki12.setter
    def GraphWiki_Wiki12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphWiki_Wiki__GraphWiki_Wiki12", None)
        self.__GraphWiki_Wiki12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GraphWiki_Revision"):
                    opp_val = getattr(item, "GraphWiki_Revision", None)
                    
                    if opp_val == self:
                        setattr(item, "GraphWiki_Revision", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GraphWiki_Revision"):
                    opp_val = getattr(item, "GraphWiki_Revision", None)
                    
                    setattr(item, "GraphWiki_Revision", self)
                    

    @property
    def GraphWiki_Wiki6(self):
        return self.__GraphWiki_Wiki6

    @GraphWiki_Wiki6.setter
    def GraphWiki_Wiki6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphWiki_Wiki__GraphWiki_Wiki6", None)
        self.__GraphWiki_Wiki6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphWiki_ClassificationGraph"):
                opp_val = getattr(old_value, "GraphWiki_ClassificationGraph", None)
                if opp_val == self:
                    setattr(old_value, "GraphWiki_ClassificationGraph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphWiki_ClassificationGraph"):
                opp_val = getattr(value, "GraphWiki_ClassificationGraph", None)
                setattr(value, "GraphWiki_ClassificationGraph", self)

    @property
    def GraphWiki_Wiki8(self):
        return self.__GraphWiki_Wiki8

    @GraphWiki_Wiki8.setter
    def GraphWiki_Wiki8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphWiki_Wiki__GraphWiki_Wiki8", None)
        self.__GraphWiki_Wiki8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GraphWiki_Node"):
                    opp_val = getattr(item, "GraphWiki_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "GraphWiki_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GraphWiki_Node"):
                    opp_val = getattr(item, "GraphWiki_Node", None)
                    
                    setattr(item, "GraphWiki_Node", self)
                    

    @property
    def GraphWiki_Wiki2(self):
        return self.__GraphWiki_Wiki2

    @GraphWiki_Wiki2.setter
    def GraphWiki_Wiki2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphWiki_Wiki__GraphWiki_Wiki2", None)
        self.__GraphWiki_Wiki2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphWiki_CategoryGraph"):
                opp_val = getattr(old_value, "GraphWiki_CategoryGraph", None)
                if opp_val == self:
                    setattr(old_value, "GraphWiki_CategoryGraph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphWiki_CategoryGraph"):
                opp_val = getattr(value, "GraphWiki_CategoryGraph", None)
                setattr(value, "GraphWiki_CategoryGraph", self)

    @property
    def GraphWiki_Wiki(self):
        return self.__GraphWiki_Wiki

    @GraphWiki_Wiki.setter
    def GraphWiki_Wiki(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphWiki_Wiki__GraphWiki_Wiki", None)
        self.__GraphWiki_Wiki = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphWiki_IndexGraph"):
                opp_val = getattr(old_value, "GraphWiki_IndexGraph", None)
                if opp_val == self:
                    setattr(old_value, "GraphWiki_IndexGraph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphWiki_IndexGraph"):
                opp_val = getattr(value, "GraphWiki_IndexGraph", None)
                setattr(value, "GraphWiki_IndexGraph", self)

    @property
    def GraphWiki_Wiki10(self):
        return self.__GraphWiki_Wiki10

    @GraphWiki_Wiki10.setter
    def GraphWiki_Wiki10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphWiki_Wiki__GraphWiki_Wiki10", None)
        self.__GraphWiki_Wiki10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GraphWiki_Edge"):
                    opp_val = getattr(item, "GraphWiki_Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "GraphWiki_Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GraphWiki_Edge"):
                    opp_val = getattr(item, "GraphWiki_Edge", None)
                    
                    setattr(item, "GraphWiki_Edge", self)
                    

    @property
    def GraphWiki_Wiki4(self):
        return self.__GraphWiki_Wiki4

    @GraphWiki_Wiki4.setter
    def GraphWiki_Wiki4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphWiki_Wiki__GraphWiki_Wiki4", None)
        self.__GraphWiki_Wiki4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphWiki_ArticleGraph"):
                opp_val = getattr(old_value, "GraphWiki_ArticleGraph", None)
                if opp_val == self:
                    setattr(old_value, "GraphWiki_ArticleGraph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphWiki_ArticleGraph"):
                opp_val = getattr(value, "GraphWiki_ArticleGraph", None)
                setattr(value, "GraphWiki_ArticleGraph", self)

class GraphWiki_ClassificationGraph(Graph):

    pass
class GraphWiki_ArticleGraph(Graph):

    pass
class GraphWiki_CategoryGraph(Graph):

    pass