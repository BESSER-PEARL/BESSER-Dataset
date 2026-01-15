from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class familytree_Member:

    def __init__(self, name: str, age: int, familytree_Member: "familytree_FamilyTree" = None, Member: "familytree_Member" = None, parents: set["familytree_Member"] = None, Member5: "familytree_Member" = None, children: set["familytree_Member"] = None):
        self.name = name
        self.age = age
        self.familytree_Member = familytree_Member
        self.Member = Member
        self.parents = parents if parents is not None else set()
        self.Member5 = Member5
        self.children = children if children is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familytree_Member__children", None)
        self.__children = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Member5"):
                    opp_val = getattr(item, "Member5", None)
                    
                    if opp_val == self:
                        setattr(item, "Member5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Member5"):
                    opp_val = getattr(item, "Member5", None)
                    
                    setattr(item, "Member5", self)
                    

    @property
    def Member(self):
        return self.__Member

    @Member.setter
    def Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familytree_Member__Member", None)
        self.__Member = value
        
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
    def Member5(self):
        return self.__Member5

    @Member5.setter
    def Member5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familytree_Member__Member5", None)
        self.__Member5 = value
        
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
    def parents(self):
        return self.__parents

    @parents.setter
    def parents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familytree_Member__parents", None)
        self.__parents = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Member"):
                    opp_val = getattr(item, "Member", None)
                    
                    if opp_val == self:
                        setattr(item, "Member", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Member"):
                    opp_val = getattr(item, "Member", None)
                    
                    setattr(item, "Member", self)
                    

    @property
    def familytree_Member(self):
        return self.__familytree_Member

    @familytree_Member.setter
    def familytree_Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familytree_Member__familytree_Member", None)
        self.__familytree_Member = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "familytree_FamilyTree"):
                opp_val = getattr(old_value, "familytree_FamilyTree", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "familytree_FamilyTree"):
                opp_val = getattr(value, "familytree_FamilyTree", None)
                if opp_val is None:
                    setattr(value, "familytree_FamilyTree", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class familytree_FamilyTree:

    pass