from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class dfg_DfgEdge:

    def __init__(self, label: str, dfg_DfgEdge8: "dfg_DfgVertex" = None, dfg_DfgEdge: "dfg_DfgGraph" = None, dfg_DfgEdge10: "dfg_DfgVertex" = None, dfg_DfgEdge13: "dfg_DfgVertex" = None):
        self.label = label
        self.dfg_DfgEdge8 = dfg_DfgEdge8
        self.dfg_DfgEdge = dfg_DfgEdge
        self.dfg_DfgEdge10 = dfg_DfgEdge10
        self.dfg_DfgEdge13 = dfg_DfgEdge13
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def dfg_DfgEdge8(self):
        return self.__dfg_DfgEdge8

    @dfg_DfgEdge8.setter
    def dfg_DfgEdge8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfg_DfgEdge__dfg_DfgEdge8", None)
        self.__dfg_DfgEdge8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dfg_DfgVertex7"):
                opp_val = getattr(old_value, "dfg_DfgVertex7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dfg_DfgVertex7"):
                opp_val = getattr(value, "dfg_DfgVertex7", None)
                if opp_val is None:
                    setattr(value, "dfg_DfgVertex7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dfg_DfgEdge10(self):
        return self.__dfg_DfgEdge10

    @dfg_DfgEdge10.setter
    def dfg_DfgEdge10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfg_DfgEdge__dfg_DfgEdge10", None)
        self.__dfg_DfgEdge10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dfg_DfgVertex11"):
                opp_val = getattr(old_value, "dfg_DfgVertex11", None)
                if opp_val == self:
                    setattr(old_value, "dfg_DfgVertex11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dfg_DfgVertex11"):
                opp_val = getattr(value, "dfg_DfgVertex11", None)
                setattr(value, "dfg_DfgVertex11", self)

    @property
    def dfg_DfgEdge(self):
        return self.__dfg_DfgEdge

    @dfg_DfgEdge.setter
    def dfg_DfgEdge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfg_DfgEdge__dfg_DfgEdge", None)
        self.__dfg_DfgEdge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dfg_DfgGraph2"):
                opp_val = getattr(old_value, "dfg_DfgGraph2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dfg_DfgGraph2"):
                opp_val = getattr(value, "dfg_DfgGraph2", None)
                if opp_val is None:
                    setattr(value, "dfg_DfgGraph2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dfg_DfgEdge13(self):
        return self.__dfg_DfgEdge13

    @dfg_DfgEdge13.setter
    def dfg_DfgEdge13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfg_DfgEdge__dfg_DfgEdge13", None)
        self.__dfg_DfgEdge13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dfg_DfgVertex14"):
                opp_val = getattr(old_value, "dfg_DfgVertex14", None)
                if opp_val == self:
                    setattr(old_value, "dfg_DfgVertex14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dfg_DfgVertex14"):
                opp_val = getattr(value, "dfg_DfgVertex14", None)
                setattr(value, "dfg_DfgVertex14", self)

class dfg_DfgVertex:

    def __init__(self, mappings: str, dfg_DfgVertex5: "dfg_DfgVertex" = None, dfg_DfgVertex3: set["dfg_DfgVertex"] = None, dfg_DfgVertex7: set["dfg_DfgEdge"] = None, dfg_DfgVertex: "dfg_DfgGraph" = None, dfg_DfgVertex11: "dfg_DfgEdge" = None, dfg_DfgVertex14: "dfg_DfgEdge" = None):
        self.mappings = mappings
        self.dfg_DfgVertex5 = dfg_DfgVertex5
        self.dfg_DfgVertex3 = dfg_DfgVertex3 if dfg_DfgVertex3 is not None else set()
        self.dfg_DfgVertex7 = dfg_DfgVertex7 if dfg_DfgVertex7 is not None else set()
        self.dfg_DfgVertex = dfg_DfgVertex
        self.dfg_DfgVertex11 = dfg_DfgVertex11
        self.dfg_DfgVertex14 = dfg_DfgVertex14
        
    @property
    def mappings(self) -> str:
        return self.__mappings

    @mappings.setter
    def mappings(self, mappings: str):
        self.__mappings = mappings

    @property
    def dfg_DfgVertex14(self):
        return self.__dfg_DfgVertex14

    @dfg_DfgVertex14.setter
    def dfg_DfgVertex14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfg_DfgVertex__dfg_DfgVertex14", None)
        self.__dfg_DfgVertex14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dfg_DfgEdge13"):
                opp_val = getattr(old_value, "dfg_DfgEdge13", None)
                if opp_val == self:
                    setattr(old_value, "dfg_DfgEdge13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dfg_DfgEdge13"):
                opp_val = getattr(value, "dfg_DfgEdge13", None)
                setattr(value, "dfg_DfgEdge13", self)

    @property
    def dfg_DfgVertex5(self):
        return self.__dfg_DfgVertex5

    @dfg_DfgVertex5.setter
    def dfg_DfgVertex5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfg_DfgVertex__dfg_DfgVertex5", None)
        self.__dfg_DfgVertex5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dfg_DfgVertex3"):
                opp_val = getattr(old_value, "dfg_DfgVertex3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dfg_DfgVertex3"):
                opp_val = getattr(value, "dfg_DfgVertex3", None)
                if opp_val is None:
                    setattr(value, "dfg_DfgVertex3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dfg_DfgVertex11(self):
        return self.__dfg_DfgVertex11

    @dfg_DfgVertex11.setter
    def dfg_DfgVertex11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfg_DfgVertex__dfg_DfgVertex11", None)
        self.__dfg_DfgVertex11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dfg_DfgEdge10"):
                opp_val = getattr(old_value, "dfg_DfgEdge10", None)
                if opp_val == self:
                    setattr(old_value, "dfg_DfgEdge10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dfg_DfgEdge10"):
                opp_val = getattr(value, "dfg_DfgEdge10", None)
                setattr(value, "dfg_DfgEdge10", self)

    @property
    def dfg_DfgVertex3(self):
        return self.__dfg_DfgVertex3

    @dfg_DfgVertex3.setter
    def dfg_DfgVertex3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfg_DfgVertex__dfg_DfgVertex3", None)
        self.__dfg_DfgVertex3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dfg_DfgVertex5"):
                    opp_val = getattr(item, "dfg_DfgVertex5", None)
                    
                    if opp_val == self:
                        setattr(item, "dfg_DfgVertex5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dfg_DfgVertex5"):
                    opp_val = getattr(item, "dfg_DfgVertex5", None)
                    
                    setattr(item, "dfg_DfgVertex5", self)
                    

    @property
    def dfg_DfgVertex(self):
        return self.__dfg_DfgVertex

    @dfg_DfgVertex.setter
    def dfg_DfgVertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfg_DfgVertex__dfg_DfgVertex", None)
        self.__dfg_DfgVertex = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dfg_DfgGraph"):
                opp_val = getattr(old_value, "dfg_DfgGraph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dfg_DfgGraph"):
                opp_val = getattr(value, "dfg_DfgGraph", None)
                if opp_val is None:
                    setattr(value, "dfg_DfgGraph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dfg_DfgVertex7(self):
        return self.__dfg_DfgVertex7

    @dfg_DfgVertex7.setter
    def dfg_DfgVertex7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfg_DfgVertex__dfg_DfgVertex7", None)
        self.__dfg_DfgVertex7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dfg_DfgEdge8"):
                    opp_val = getattr(item, "dfg_DfgEdge8", None)
                    
                    if opp_val == self:
                        setattr(item, "dfg_DfgEdge8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dfg_DfgEdge8"):
                    opp_val = getattr(item, "dfg_DfgEdge8", None)
                    
                    setattr(item, "dfg_DfgEdge8", self)
                    

class dfg_DfgGraph:

    pass