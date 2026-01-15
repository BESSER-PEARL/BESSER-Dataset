from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class rules_NodeRelation:

    def __init__(self, relation: str, lowerBound: int, upperBound: int, relationTgt: str, NodeRelation: "rules_Node" = None, relatedNodes: "rules_Node" = None, rules_NodeRelation: "rules_Node" = None):
        self.relation = relation
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.relationTgt = relationTgt
        self.NodeRelation = NodeRelation
        self.relatedNodes = relatedNodes
        self.rules_NodeRelation = rules_NodeRelation
        
    @property
    def relationTgt(self) -> str:
        return self.__relationTgt

    @relationTgt.setter
    def relationTgt(self, relationTgt: str):
        self.__relationTgt = relationTgt

    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def relation(self) -> str:
        return self.__relation

    @relation.setter
    def relation(self, relation: str):
        self.__relation = relation

    @property
    def relatedNodes(self):
        return self.__relatedNodes

    @relatedNodes.setter
    def relatedNodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rules_NodeRelation__relatedNodes", None)
        self.__relatedNodes = value
        
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

    @property
    def NodeRelation(self):
        return self.__NodeRelation

    @NodeRelation.setter
    def NodeRelation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rules_NodeRelation__NodeRelation", None)
        self.__NodeRelation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rules_NodeRelation(self):
        return self.__rules_NodeRelation

    @rules_NodeRelation.setter
    def rules_NodeRelation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rules_NodeRelation__rules_NodeRelation", None)
        self.__rules_NodeRelation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rules_Node17"):
                opp_val = getattr(old_value, "rules_Node17", None)
                if opp_val == self:
                    setattr(old_value, "rules_Node17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rules_Node17"):
                opp_val = getattr(value, "rules_Node17", None)
                setattr(value, "rules_Node17", self)

class rules_Node:

    def __init__(self, type: str, rules_Node: "rules_Rule" = None, rules_Node10: "rules_Rule" = None, rules_Node13: "rules_Rule" = None, source: set["rules_NodeRelation"] = None, Node: "rules_NodeRelation" = None, rules_Node17: "rules_NodeRelation" = None):
        self.type = type
        self.rules_Node = rules_Node
        self.rules_Node10 = rules_Node10
        self.rules_Node13 = rules_Node13
        self.source = source if source is not None else set()
        self.Node = Node
        self.rules_Node17 = rules_Node17
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rules_Node__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NodeRelation"):
                    opp_val = getattr(item, "NodeRelation", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeRelation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeRelation"):
                    opp_val = getattr(item, "NodeRelation", None)
                    
                    setattr(item, "NodeRelation", self)
                    

    @property
    def rules_Node(self):
        return self.__rules_Node

    @rules_Node.setter
    def rules_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rules_Node__rules_Node", None)
        self.__rules_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rules_Rule7"):
                opp_val = getattr(old_value, "rules_Rule7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rules_Rule7"):
                opp_val = getattr(value, "rules_Rule7", None)
                if opp_val is None:
                    setattr(value, "rules_Rule7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rules_Node13(self):
        return self.__rules_Node13

    @rules_Node13.setter
    def rules_Node13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rules_Node__rules_Node13", None)
        self.__rules_Node13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rules_Rule12"):
                opp_val = getattr(old_value, "rules_Rule12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rules_Rule12"):
                opp_val = getattr(value, "rules_Rule12", None)
                if opp_val is None:
                    setattr(value, "rules_Rule12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rules_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relatedNodes"):
                opp_val = getattr(old_value, "relatedNodes", None)
                if opp_val == self:
                    setattr(old_value, "relatedNodes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relatedNodes"):
                opp_val = getattr(value, "relatedNodes", None)
                setattr(value, "relatedNodes", self)

    @property
    def rules_Node10(self):
        return self.__rules_Node10

    @rules_Node10.setter
    def rules_Node10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rules_Node__rules_Node10", None)
        self.__rules_Node10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rules_Rule9"):
                opp_val = getattr(old_value, "rules_Rule9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rules_Rule9"):
                opp_val = getattr(value, "rules_Rule9", None)
                if opp_val is None:
                    setattr(value, "rules_Rule9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rules_Node17(self):
        return self.__rules_Node17

    @rules_Node17.setter
    def rules_Node17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rules_Node__rules_Node17", None)
        self.__rules_Node17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rules_NodeRelation"):
                opp_val = getattr(old_value, "rules_NodeRelation", None)
                if opp_val == self:
                    setattr(old_value, "rules_NodeRelation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rules_NodeRelation"):
                opp_val = getattr(value, "rules_NodeRelation", None)
                setattr(value, "rules_NodeRelation", self)

class rules_Rule:

    def __init__(self, name: str, Rule: "rules_Rule" = None, parents: set["rules_Rule"] = None, rules_Rule: "rules_RulesLattice" = None, Rule5: "rules_Rule" = None, children: set["rules_Rule"] = None, rules_Rule7: set["rules_Node"] = None, rules_Rule9: set["rules_Node"] = None, rules_Rule12: set["rules_Node"] = None):
        self.name = name
        self.Rule = Rule
        self.parents = parents if parents is not None else set()
        self.rules_Rule = rules_Rule
        self.Rule5 = Rule5
        self.children = children if children is not None else set()
        self.rules_Rule7 = rules_Rule7 if rules_Rule7 is not None else set()
        self.rules_Rule9 = rules_Rule9 if rules_Rule9 is not None else set()
        self.rules_Rule12 = rules_Rule12 if rules_Rule12 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rules_Rule9(self):
        return self.__rules_Rule9

    @rules_Rule9.setter
    def rules_Rule9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rules_Rule__rules_Rule9", None)
        self.__rules_Rule9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rules_Node10"):
                    opp_val = getattr(item, "rules_Node10", None)
                    
                    if opp_val == self:
                        setattr(item, "rules_Node10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rules_Node10"):
                    opp_val = getattr(item, "rules_Node10", None)
                    
                    setattr(item, "rules_Node10", self)
                    

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rules_Rule__children", None)
        self.__children = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Rule5"):
                    opp_val = getattr(item, "Rule5", None)
                    
                    if opp_val == self:
                        setattr(item, "Rule5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Rule5"):
                    opp_val = getattr(item, "Rule5", None)
                    
                    setattr(item, "Rule5", self)
                    

    @property
    def Rule(self):
        return self.__Rule

    @Rule.setter
    def Rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rules_Rule__Rule", None)
        self.__Rule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parents"):
                opp_val = getattr(old_value, "parents", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parents"):
                opp_val = getattr(value, "parents", None)
                if opp_val is None:
                    setattr(value, "parents", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rules_Rule(self):
        return self.__rules_Rule

    @rules_Rule.setter
    def rules_Rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rules_Rule__rules_Rule", None)
        self.__rules_Rule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rules_RulesLattice"):
                opp_val = getattr(old_value, "rules_RulesLattice", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rules_RulesLattice"):
                opp_val = getattr(value, "rules_RulesLattice", None)
                if opp_val is None:
                    setattr(value, "rules_RulesLattice", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parents(self):
        return self.__parents

    @parents.setter
    def parents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rules_Rule__parents", None)
        self.__parents = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Rule"):
                    opp_val = getattr(item, "Rule", None)
                    
                    if opp_val == self:
                        setattr(item, "Rule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Rule"):
                    opp_val = getattr(item, "Rule", None)
                    
                    setattr(item, "Rule", self)
                    

    @property
    def Rule5(self):
        return self.__Rule5

    @Rule5.setter
    def Rule5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rules_Rule__Rule5", None)
        self.__Rule5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "children"):
                opp_val = getattr(old_value, "children", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "children"):
                opp_val = getattr(value, "children", None)
                if opp_val is None:
                    setattr(value, "children", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rules_Rule12(self):
        return self.__rules_Rule12

    @rules_Rule12.setter
    def rules_Rule12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rules_Rule__rules_Rule12", None)
        self.__rules_Rule12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rules_Node13"):
                    opp_val = getattr(item, "rules_Node13", None)
                    
                    if opp_val == self:
                        setattr(item, "rules_Node13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rules_Node13"):
                    opp_val = getattr(item, "rules_Node13", None)
                    
                    setattr(item, "rules_Node13", self)
                    

    @property
    def rules_Rule7(self):
        return self.__rules_Rule7

    @rules_Rule7.setter
    def rules_Rule7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rules_Rule__rules_Rule7", None)
        self.__rules_Rule7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rules_Node"):
                    opp_val = getattr(item, "rules_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "rules_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rules_Node"):
                    opp_val = getattr(item, "rules_Node", None)
                    
                    setattr(item, "rules_Node", self)
                    

class rules_RulesLattice:

    def __init__(self, source: str, target: str, rules_RulesLattice: set["rules_Rule"] = None):
        self.source = source
        self.target = target
        self.rules_RulesLattice = rules_RulesLattice if rules_RulesLattice is not None else set()
        
    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

    @property
    def rules_RulesLattice(self):
        return self.__rules_RulesLattice

    @rules_RulesLattice.setter
    def rules_RulesLattice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rules_RulesLattice__rules_RulesLattice", None)
        self.__rules_RulesLattice = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rules_Rule"):
                    opp_val = getattr(item, "rules_Rule", None)
                    
                    if opp_val == self:
                        setattr(item, "rules_Rule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rules_Rule"):
                    opp_val = getattr(item, "rules_Rule", None)
                    
                    setattr(item, "rules_Rule", self)
                    
