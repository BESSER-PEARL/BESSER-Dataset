from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class grammar_RHS:

    pass
class grammar_ConnexionInstruction:

    def __init__(self, m: str, ConnexionInstruction: "grammar_Embedding" = None, instructions: "grammar_Embedding" = None, grammar_ConnexionInstruction: "grammar_Node" = None):
        self.m = m
        self.ConnexionInstruction = ConnexionInstruction
        self.instructions = instructions
        self.grammar_ConnexionInstruction = grammar_ConnexionInstruction
        
    @property
    def m(self) -> str:
        return self.__m

    @m.setter
    def m(self, m: str):
        self.__m = m

    @property
    def grammar_ConnexionInstruction(self):
        return self.__grammar_ConnexionInstruction

    @grammar_ConnexionInstruction.setter
    def grammar_ConnexionInstruction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grammar_ConnexionInstruction__grammar_ConnexionInstruction", None)
        self.__grammar_ConnexionInstruction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grammar_Node18"):
                opp_val = getattr(old_value, "grammar_Node18", None)
                if opp_val == self:
                    setattr(old_value, "grammar_Node18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grammar_Node18"):
                opp_val = getattr(value, "grammar_Node18", None)
                setattr(value, "grammar_Node18", self)

    @property
    def instructions(self):
        return self.__instructions

    @instructions.setter
    def instructions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grammar_ConnexionInstruction__instructions", None)
        self.__instructions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Embedding16"):
                opp_val = getattr(old_value, "Embedding16", None)
                if opp_val == self:
                    setattr(old_value, "Embedding16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Embedding16"):
                opp_val = getattr(value, "Embedding16", None)
                setattr(value, "Embedding16", self)

    @property
    def ConnexionInstruction(self):
        return self.__ConnexionInstruction

    @ConnexionInstruction.setter
    def ConnexionInstruction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grammar_ConnexionInstruction__ConnexionInstruction", None)
        self.__ConnexionInstruction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentEmbedding"):
                opp_val = getattr(old_value, "parentEmbedding", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentEmbedding"):
                opp_val = getattr(value, "parentEmbedding", None)
                if opp_val is None:
                    setattr(value, "parentEmbedding", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class grammar_Graph:

    pass
class grammar_Node:

    pass
class grammar_Embedding:

    pass
class grammar_LHS:

    pass
class grammar_Rule:

    def __init__(self, name: str, priority: int, Rule: "grammar_Grammar" = None, rules: "grammar_Grammar" = None, parentRule: "grammar_LHS" = None, parentRule4: "grammar_RHS" = None, ParentRule: "grammar_Embedding" = None, Rule7: "grammar_LHS" = None, Rule10: "grammar_RHS" = None, Rule13: "grammar_Embedding" = None):
        self.name = name
        self.priority = priority
        self.Rule = Rule
        self.rules = rules
        self.parentRule = parentRule
        self.parentRule4 = parentRule4
        self.ParentRule = ParentRule
        self.Rule7 = Rule7
        self.Rule10 = Rule10
        self.Rule13 = Rule13
        
    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Rule(self):
        return self.__Rule

    @Rule.setter
    def Rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grammar_Rule__Rule", None)
        self.__Rule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentGrammar"):
                opp_val = getattr(old_value, "parentGrammar", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentGrammar"):
                opp_val = getattr(value, "parentGrammar", None)
                if opp_val is None:
                    setattr(value, "parentGrammar", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Rule13(self):
        return self.__Rule13

    @Rule13.setter
    def Rule13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grammar_Rule__Rule13", None)
        self.__Rule13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EmbeddingMechanism"):
                opp_val = getattr(old_value, "EmbeddingMechanism", None)
                if opp_val == self:
                    setattr(old_value, "EmbeddingMechanism", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EmbeddingMechanism"):
                opp_val = getattr(value, "EmbeddingMechanism", None)
                setattr(value, "EmbeddingMechanism", self)

    @property
    def Rule10(self):
        return self.__Rule10

    @Rule10.setter
    def Rule10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grammar_Rule__Rule10", None)
        self.__Rule10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rhs"):
                opp_val = getattr(old_value, "rhs", None)
                if opp_val == self:
                    setattr(old_value, "rhs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rhs"):
                opp_val = getattr(value, "rhs", None)
                setattr(value, "rhs", self)

    @property
    def ParentRule(self):
        return self.__ParentRule

    @ParentRule.setter
    def ParentRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grammar_Rule__ParentRule", None)
        self.__ParentRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Embedding"):
                opp_val = getattr(old_value, "Embedding", None)
                if opp_val == self:
                    setattr(old_value, "Embedding", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Embedding"):
                opp_val = getattr(value, "Embedding", None)
                setattr(value, "Embedding", self)

    @property
    def parentRule4(self):
        return self.__parentRule4

    @parentRule4.setter
    def parentRule4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grammar_Rule__parentRule4", None)
        self.__parentRule4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RHS"):
                opp_val = getattr(old_value, "RHS", None)
                if opp_val == self:
                    setattr(old_value, "RHS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RHS"):
                opp_val = getattr(value, "RHS", None)
                setattr(value, "RHS", self)

    @property
    def Rule7(self):
        return self.__Rule7

    @Rule7.setter
    def Rule7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grammar_Rule__Rule7", None)
        self.__Rule7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lhs"):
                opp_val = getattr(old_value, "lhs", None)
                if opp_val == self:
                    setattr(old_value, "lhs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lhs"):
                opp_val = getattr(value, "lhs", None)
                setattr(value, "lhs", self)

    @property
    def parentRule(self):
        return self.__parentRule

    @parentRule.setter
    def parentRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grammar_Rule__parentRule", None)
        self.__parentRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LHS"):
                opp_val = getattr(old_value, "LHS", None)
                if opp_val == self:
                    setattr(old_value, "LHS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LHS"):
                opp_val = getattr(value, "LHS", None)
                setattr(value, "LHS", self)

    @property
    def rules(self):
        return self.__rules

    @rules.setter
    def rules(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grammar_Rule__rules", None)
        self.__rules = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Grammar"):
                opp_val = getattr(old_value, "Grammar", None)
                if opp_val == self:
                    setattr(old_value, "Grammar", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Grammar"):
                opp_val = getattr(value, "Grammar", None)
                setattr(value, "Grammar", self)

class Named:

    pass
class grammar_Grammar(Named):

    pass