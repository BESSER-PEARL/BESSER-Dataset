from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class links_Root_BA_Element_Link:

    def __init__(self, name: str, links_Root_BA_Element_Link: "links_Root" = None, links_Root_BA_Element_Link24: "links_RootNodeB" = None, links_Root_BA_Element_Link27: "links_RootNodeA" = None):
        self.name = name
        self.links_Root_BA_Element_Link = links_Root_BA_Element_Link
        self.links_Root_BA_Element_Link24 = links_Root_BA_Element_Link24
        self.links_Root_BA_Element_Link27 = links_Root_BA_Element_Link27
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def links_Root_BA_Element_Link27(self):
        return self.__links_Root_BA_Element_Link27

    @links_Root_BA_Element_Link27.setter
    def links_Root_BA_Element_Link27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_links_Root_BA_Element_Link__links_Root_BA_Element_Link27", None)
        self.__links_Root_BA_Element_Link27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "links_RootNodeA28"):
                opp_val = getattr(old_value, "links_RootNodeA28", None)
                if opp_val == self:
                    setattr(old_value, "links_RootNodeA28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "links_RootNodeA28"):
                opp_val = getattr(value, "links_RootNodeA28", None)
                setattr(value, "links_RootNodeA28", self)

    @property
    def links_Root_BA_Element_Link24(self):
        return self.__links_Root_BA_Element_Link24

    @links_Root_BA_Element_Link24.setter
    def links_Root_BA_Element_Link24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_links_Root_BA_Element_Link__links_Root_BA_Element_Link24", None)
        self.__links_Root_BA_Element_Link24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "links_RootNodeB25"):
                opp_val = getattr(old_value, "links_RootNodeB25", None)
                if opp_val == self:
                    setattr(old_value, "links_RootNodeB25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "links_RootNodeB25"):
                opp_val = getattr(value, "links_RootNodeB25", None)
                setattr(value, "links_RootNodeB25", self)

    @property
    def links_Root_BA_Element_Link(self):
        return self.__links_Root_BA_Element_Link

    @links_Root_BA_Element_Link.setter
    def links_Root_BA_Element_Link(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_links_Root_BA_Element_Link__links_Root_BA_Element_Link", None)
        self.__links_Root_BA_Element_Link = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "links_Root6"):
                opp_val = getattr(old_value, "links_Root6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "links_Root6"):
                opp_val = getattr(value, "links_Root6", None)
                if opp_val is None:
                    setattr(value, "links_Root6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class links_RootNodeB:

    pass
class links_RootNodeA:

    pass
class links_Child_AB_Element_Link:

    pass
class links_Root:

    pass
class links_ChildNodeB:

    pass
class links_ChildNodeA:

    pass