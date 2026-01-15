from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Graph:

    pass
class wiki_IndexGraph(Graph):

    pass
class wiki_Wiki:

    def __init__(self, title: str, wiki_Wiki2: "wiki_CategoryGraph" = None, wiki_Wiki4: "wiki_ArticleGraph" = None, wiki_Wiki6: "wiki_ClassificationGraph" = None, wiki_Wiki8: set["wiki_Node"] = None, wiki_Wiki10: set["wiki_Edge"] = None, wiki_Wiki12: set["wiki_Revision"] = None, wiki_Wiki: "wiki_IndexGraph" = None):
        self.title = title
        self.wiki_Wiki2 = wiki_Wiki2
        self.wiki_Wiki4 = wiki_Wiki4
        self.wiki_Wiki6 = wiki_Wiki6
        self.wiki_Wiki8 = wiki_Wiki8 if wiki_Wiki8 is not None else set()
        self.wiki_Wiki10 = wiki_Wiki10 if wiki_Wiki10 is not None else set()
        self.wiki_Wiki12 = wiki_Wiki12 if wiki_Wiki12 is not None else set()
        self.wiki_Wiki = wiki_Wiki
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def wiki_Wiki4(self):
        return self.__wiki_Wiki4

    @wiki_Wiki4.setter
    def wiki_Wiki4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wiki_Wiki__wiki_Wiki4", None)
        self.__wiki_Wiki4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wiki_ArticleGraph"):
                opp_val = getattr(old_value, "wiki_ArticleGraph", None)
                if opp_val == self:
                    setattr(old_value, "wiki_ArticleGraph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wiki_ArticleGraph"):
                opp_val = getattr(value, "wiki_ArticleGraph", None)
                setattr(value, "wiki_ArticleGraph", self)

    @property
    def wiki_Wiki(self):
        return self.__wiki_Wiki

    @wiki_Wiki.setter
    def wiki_Wiki(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wiki_Wiki__wiki_Wiki", None)
        self.__wiki_Wiki = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wiki_IndexGraph"):
                opp_val = getattr(old_value, "wiki_IndexGraph", None)
                if opp_val == self:
                    setattr(old_value, "wiki_IndexGraph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wiki_IndexGraph"):
                opp_val = getattr(value, "wiki_IndexGraph", None)
                setattr(value, "wiki_IndexGraph", self)

    @property
    def wiki_Wiki12(self):
        return self.__wiki_Wiki12

    @wiki_Wiki12.setter
    def wiki_Wiki12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wiki_Wiki__wiki_Wiki12", None)
        self.__wiki_Wiki12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wiki_Revision"):
                    opp_val = getattr(item, "wiki_Revision", None)
                    
                    if opp_val == self:
                        setattr(item, "wiki_Revision", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wiki_Revision"):
                    opp_val = getattr(item, "wiki_Revision", None)
                    
                    setattr(item, "wiki_Revision", self)
                    

    @property
    def wiki_Wiki2(self):
        return self.__wiki_Wiki2

    @wiki_Wiki2.setter
    def wiki_Wiki2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wiki_Wiki__wiki_Wiki2", None)
        self.__wiki_Wiki2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wiki_CategoryGraph"):
                opp_val = getattr(old_value, "wiki_CategoryGraph", None)
                if opp_val == self:
                    setattr(old_value, "wiki_CategoryGraph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wiki_CategoryGraph"):
                opp_val = getattr(value, "wiki_CategoryGraph", None)
                setattr(value, "wiki_CategoryGraph", self)

    @property
    def wiki_Wiki8(self):
        return self.__wiki_Wiki8

    @wiki_Wiki8.setter
    def wiki_Wiki8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wiki_Wiki__wiki_Wiki8", None)
        self.__wiki_Wiki8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wiki_Node"):
                    opp_val = getattr(item, "wiki_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "wiki_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wiki_Node"):
                    opp_val = getattr(item, "wiki_Node", None)
                    
                    setattr(item, "wiki_Node", self)
                    

    @property
    def wiki_Wiki6(self):
        return self.__wiki_Wiki6

    @wiki_Wiki6.setter
    def wiki_Wiki6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wiki_Wiki__wiki_Wiki6", None)
        self.__wiki_Wiki6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wiki_ClassificationGraph"):
                opp_val = getattr(old_value, "wiki_ClassificationGraph", None)
                if opp_val == self:
                    setattr(old_value, "wiki_ClassificationGraph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wiki_ClassificationGraph"):
                opp_val = getattr(value, "wiki_ClassificationGraph", None)
                setattr(value, "wiki_ClassificationGraph", self)

    @property
    def wiki_Wiki10(self):
        return self.__wiki_Wiki10

    @wiki_Wiki10.setter
    def wiki_Wiki10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wiki_Wiki__wiki_Wiki10", None)
        self.__wiki_Wiki10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wiki_Edge"):
                    opp_val = getattr(item, "wiki_Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "wiki_Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wiki_Edge"):
                    opp_val = getattr(item, "wiki_Edge", None)
                    
                    setattr(item, "wiki_Edge", self)
                    

class wiki_Graph:

    def __init__(self, name: str, wiki_Graph: set["wiki_Node"] = None, wiki_Graph16: set["wiki_Edge"] = None):
        self.name = name
        self.wiki_Graph = wiki_Graph if wiki_Graph is not None else set()
        self.wiki_Graph16 = wiki_Graph16 if wiki_Graph16 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def wiki_Graph16(self):
        return self.__wiki_Graph16

    @wiki_Graph16.setter
    def wiki_Graph16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wiki_Graph__wiki_Graph16", None)
        self.__wiki_Graph16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wiki_Edge17"):
                    opp_val = getattr(item, "wiki_Edge17", None)
                    
                    if opp_val == self:
                        setattr(item, "wiki_Edge17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wiki_Edge17"):
                    opp_val = getattr(item, "wiki_Edge17", None)
                    
                    setattr(item, "wiki_Edge17", self)
                    

    @property
    def wiki_Graph(self):
        return self.__wiki_Graph

    @wiki_Graph.setter
    def wiki_Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wiki_Graph__wiki_Graph", None)
        self.__wiki_Graph = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wiki_Node14"):
                    opp_val = getattr(item, "wiki_Node14", None)
                    
                    if opp_val == self:
                        setattr(item, "wiki_Node14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wiki_Node14"):
                    opp_val = getattr(item, "wiki_Node14", None)
                    
                    setattr(item, "wiki_Node14", self)
                    

class wiki_Revision:

    def __init__(self, user: str, date: str, text_id: int, wiki_Revision: "wiki_Wiki" = None, revisions: "wiki_Node" = None, wiki_Revision20: "wiki_Node" = None, Revision: "wiki_Node" = None):
        self.user = user
        self.date = date
        self.text_id = text_id
        self.wiki_Revision = wiki_Revision
        self.revisions = revisions
        self.wiki_Revision20 = wiki_Revision20
        self.Revision = Revision
        
    @property
    def user(self) -> str:
        return self.__user

    @user.setter
    def user(self, user: str):
        self.__user = user

    @property
    def text_id(self) -> int:
        return self.__text_id

    @text_id.setter
    def text_id(self, text_id: int):
        self.__text_id = text_id

    @property
    def date(self) -> str:
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def wiki_Revision(self):
        return self.__wiki_Revision

    @wiki_Revision.setter
    def wiki_Revision(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wiki_Revision__wiki_Revision", None)
        self.__wiki_Revision = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wiki_Wiki12"):
                opp_val = getattr(old_value, "wiki_Wiki12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wiki_Wiki12"):
                opp_val = getattr(value, "wiki_Wiki12", None)
                if opp_val is None:
                    setattr(value, "wiki_Wiki12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def wiki_Revision20(self):
        return self.__wiki_Revision20

    @wiki_Revision20.setter
    def wiki_Revision20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wiki_Revision__wiki_Revision20", None)
        self.__wiki_Revision20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wiki_Node19"):
                opp_val = getattr(old_value, "wiki_Node19", None)
                if opp_val == self:
                    setattr(old_value, "wiki_Node19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wiki_Node19"):
                opp_val = getattr(value, "wiki_Node19", None)
                setattr(value, "wiki_Node19", self)

    @property
    def Revision(self):
        return self.__Revision

    @Revision.setter
    def Revision(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wiki_Revision__Revision", None)
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
        old_value = getattr(self, f"_wiki_Revision__revisions", None)
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

class wiki_Edge:

    def __init__(self, type: str, wiki_Edge: "wiki_Wiki" = None, wiki_Edge17: "wiki_Graph" = None, wiki_Edge24: "wiki_Node" = None, wiki_Edge27: "wiki_Node" = None):
        self.type = type
        self.wiki_Edge = wiki_Edge
        self.wiki_Edge17 = wiki_Edge17
        self.wiki_Edge24 = wiki_Edge24
        self.wiki_Edge27 = wiki_Edge27
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def wiki_Edge27(self):
        return self.__wiki_Edge27

    @wiki_Edge27.setter
    def wiki_Edge27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wiki_Edge__wiki_Edge27", None)
        self.__wiki_Edge27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wiki_Node28"):
                opp_val = getattr(old_value, "wiki_Node28", None)
                if opp_val == self:
                    setattr(old_value, "wiki_Node28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wiki_Node28"):
                opp_val = getattr(value, "wiki_Node28", None)
                setattr(value, "wiki_Node28", self)

    @property
    def wiki_Edge24(self):
        return self.__wiki_Edge24

    @wiki_Edge24.setter
    def wiki_Edge24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wiki_Edge__wiki_Edge24", None)
        self.__wiki_Edge24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wiki_Node25"):
                opp_val = getattr(old_value, "wiki_Node25", None)
                if opp_val == self:
                    setattr(old_value, "wiki_Node25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wiki_Node25"):
                opp_val = getattr(value, "wiki_Node25", None)
                setattr(value, "wiki_Node25", self)

    @property
    def wiki_Edge17(self):
        return self.__wiki_Edge17

    @wiki_Edge17.setter
    def wiki_Edge17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wiki_Edge__wiki_Edge17", None)
        self.__wiki_Edge17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wiki_Graph16"):
                opp_val = getattr(old_value, "wiki_Graph16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wiki_Graph16"):
                opp_val = getattr(value, "wiki_Graph16", None)
                if opp_val is None:
                    setattr(value, "wiki_Graph16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def wiki_Edge(self):
        return self.__wiki_Edge

    @wiki_Edge.setter
    def wiki_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wiki_Edge__wiki_Edge", None)
        self.__wiki_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wiki_Wiki10"):
                opp_val = getattr(old_value, "wiki_Wiki10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wiki_Wiki10"):
                opp_val = getattr(value, "wiki_Wiki10", None)
                if opp_val is None:
                    setattr(value, "wiki_Wiki10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class wiki_Node:

    def __init__(self, title: str, editions: int, node_id: int, visits: int, node_namespace: int, type: str, wiki_Node: "wiki_Wiki" = None, wiki_Node14: "wiki_Graph" = None, node: set["wiki_Revision"] = None, Node: "wiki_Revision" = None, wiki_Node25: "wiki_Edge" = None, wiki_Node28: "wiki_Edge" = None, wiki_Node19: "wiki_Revision" = None):
        self.title = title
        self.editions = editions
        self.node_id = node_id
        self.visits = visits
        self.node_namespace = node_namespace
        self.type = type
        self.wiki_Node = wiki_Node
        self.wiki_Node14 = wiki_Node14
        self.node = node if node is not None else set()
        self.Node = Node
        self.wiki_Node25 = wiki_Node25
        self.wiki_Node28 = wiki_Node28
        self.wiki_Node19 = wiki_Node19
        
    @property
    def node_namespace(self) -> int:
        return self.__node_namespace

    @node_namespace.setter
    def node_namespace(self, node_namespace: int):
        self.__node_namespace = node_namespace

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

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
    def editions(self) -> int:
        return self.__editions

    @editions.setter
    def editions(self, editions: int):
        self.__editions = editions

    @property
    def node_id(self) -> int:
        return self.__node_id

    @node_id.setter
    def node_id(self, node_id: int):
        self.__node_id = node_id

    @property
    def wiki_Node19(self):
        return self.__wiki_Node19

    @wiki_Node19.setter
    def wiki_Node19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wiki_Node__wiki_Node19", None)
        self.__wiki_Node19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wiki_Revision20"):
                opp_val = getattr(old_value, "wiki_Revision20", None)
                if opp_val == self:
                    setattr(old_value, "wiki_Revision20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wiki_Revision20"):
                opp_val = getattr(value, "wiki_Revision20", None)
                setattr(value, "wiki_Revision20", self)

    @property
    def wiki_Node25(self):
        return self.__wiki_Node25

    @wiki_Node25.setter
    def wiki_Node25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wiki_Node__wiki_Node25", None)
        self.__wiki_Node25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wiki_Edge24"):
                opp_val = getattr(old_value, "wiki_Edge24", None)
                if opp_val == self:
                    setattr(old_value, "wiki_Edge24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wiki_Edge24"):
                opp_val = getattr(value, "wiki_Edge24", None)
                setattr(value, "wiki_Edge24", self)

    @property
    def wiki_Node(self):
        return self.__wiki_Node

    @wiki_Node.setter
    def wiki_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wiki_Node__wiki_Node", None)
        self.__wiki_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wiki_Wiki8"):
                opp_val = getattr(old_value, "wiki_Wiki8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wiki_Wiki8"):
                opp_val = getattr(value, "wiki_Wiki8", None)
                if opp_val is None:
                    setattr(value, "wiki_Wiki8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wiki_Node__Node", None)
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
    def node(self):
        return self.__node

    @node.setter
    def node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wiki_Node__node", None)
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
    def wiki_Node14(self):
        return self.__wiki_Node14

    @wiki_Node14.setter
    def wiki_Node14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wiki_Node__wiki_Node14", None)
        self.__wiki_Node14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wiki_Graph"):
                opp_val = getattr(old_value, "wiki_Graph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wiki_Graph"):
                opp_val = getattr(value, "wiki_Graph", None)
                if opp_val is None:
                    setattr(value, "wiki_Graph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def wiki_Node28(self):
        return self.__wiki_Node28

    @wiki_Node28.setter
    def wiki_Node28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wiki_Node__wiki_Node28", None)
        self.__wiki_Node28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wiki_Edge27"):
                opp_val = getattr(old_value, "wiki_Edge27", None)
                if opp_val == self:
                    setattr(old_value, "wiki_Edge27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wiki_Edge27"):
                opp_val = getattr(value, "wiki_Edge27", None)
                setattr(value, "wiki_Edge27", self)

class wiki_ClassificationGraph(Graph):

    pass
class wiki_ArticleGraph(Graph):

    pass
class wiki_CategoryGraph(Graph):

    pass