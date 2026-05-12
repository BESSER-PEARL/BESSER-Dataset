from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class nupn_EStringToStringMapEntry:

    pass
class nupn_NUPNToolspecificType:

    def __init__(self, tool: str, version: str, mixed: str, nupn_NUPNToolspecificType: "nupn_SizeType" = None, nupn_NUPNToolspecificType3: "nupn_StructureType" = None, nupn_NUPNToolspecificType6: set["nupn_EStringToStringMapEntry"] = None, nupn_NUPNToolspecificType8: set["nupn_EStringToStringMapEntry"] = None):
        self.tool = tool
        self.version = version
        self.mixed = mixed
        self.nupn_NUPNToolspecificType = nupn_NUPNToolspecificType
        self.nupn_NUPNToolspecificType3 = nupn_NUPNToolspecificType3
        self.nupn_NUPNToolspecificType6 = nupn_NUPNToolspecificType6 if nupn_NUPNToolspecificType6 is not None else set()
        self.nupn_NUPNToolspecificType8 = nupn_NUPNToolspecificType8 if nupn_NUPNToolspecificType8 is not None else set()
        
        pass
    @property
    def tool(self):
        return self.__tool

    @tool.setter
    def tool(self, tool: str):
        self.__tool = tool


    @property
    def mixed(self):
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def nupn_NUPNToolspecificType3(self):
        return self.__nupn_NUPNToolspecificType3

    @nupn_NUPNToolspecificType3.setter
    def nupn_NUPNToolspecificType3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nupn_NUPNToolspecificType__nupn_NUPNToolspecificType3", None)
        self.__nupn_NUPNToolspecificType3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nupn_StructureType4"):
                opp_val = getattr(old_value, "nupn_StructureType4", None)
                if opp_val == self:
                    setattr(old_value, "nupn_StructureType4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nupn_StructureType4"):
                opp_val = getattr(value, "nupn_StructureType4", None)
                setattr(value, "nupn_StructureType4", self)

    @property
    def nupn_NUPNToolspecificType6(self):
        return self.__nupn_NUPNToolspecificType6

    @nupn_NUPNToolspecificType6.setter
    def nupn_NUPNToolspecificType6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nupn_NUPNToolspecificType__nupn_NUPNToolspecificType6", None)
        self.__nupn_NUPNToolspecificType6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nupn_EStringToStringMapEntry"):
                    opp_val = getattr(item, "nupn_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "nupn_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nupn_EStringToStringMapEntry"):
                    opp_val = getattr(item, "nupn_EStringToStringMapEntry", None)
                    
                    setattr(item, "nupn_EStringToStringMapEntry", self)
                    

    @property
    def nupn_NUPNToolspecificType8(self):
        return self.__nupn_NUPNToolspecificType8

    @nupn_NUPNToolspecificType8.setter
    def nupn_NUPNToolspecificType8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nupn_NUPNToolspecificType__nupn_NUPNToolspecificType8", None)
        self.__nupn_NUPNToolspecificType8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nupn_EStringToStringMapEntry9"):
                    opp_val = getattr(item, "nupn_EStringToStringMapEntry9", None)
                    
                    if opp_val == self:
                        setattr(item, "nupn_EStringToStringMapEntry9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nupn_EStringToStringMapEntry9"):
                    opp_val = getattr(item, "nupn_EStringToStringMapEntry9", None)
                    
                    setattr(item, "nupn_EStringToStringMapEntry9", self)
                    

    @property
    def nupn_NUPNToolspecificType(self):
        return self.__nupn_NUPNToolspecificType

    @nupn_NUPNToolspecificType.setter
    def nupn_NUPNToolspecificType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nupn_NUPNToolspecificType__nupn_NUPNToolspecificType", None)
        self.__nupn_NUPNToolspecificType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nupn_SizeType"):
                opp_val = getattr(old_value, "nupn_SizeType", None)
                if opp_val == self:
                    setattr(old_value, "nupn_SizeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nupn_SizeType"):
                opp_val = getattr(value, "nupn_SizeType", None)
                setattr(value, "nupn_SizeType", self)

class nupn_UnitType:

    def __init__(self, id: str, places: str, subunits: str, nupn_UnitType: "nupn_StructureType" = None):
        self.id = id
        self.places = places
        self.subunits = subunits
        self.nupn_UnitType = nupn_UnitType
        
        pass
    @property
    def places(self):
        return self.__places

    @places.setter
    def places(self, places: str):
        self.__places = places


    @property
    def subunits(self):
        return self.__subunits

    @subunits.setter
    def subunits(self, subunits: str):
        self.__subunits = subunits


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def nupn_UnitType(self):
        return self.__nupn_UnitType

    @nupn_UnitType.setter
    def nupn_UnitType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nupn_UnitType__nupn_UnitType", None)
        self.__nupn_UnitType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nupn_StructureType"):
                opp_val = getattr(old_value, "nupn_StructureType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nupn_StructureType"):
                opp_val = getattr(value, "nupn_StructureType", None)
                if opp_val is None:
                    setattr(value, "nupn_StructureType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class nupn_SizeType:

    def __init__(self, transitions: str, arcs: str, places: str, nupn_SizeType: "nupn_NUPNToolspecificType" = None):
        self.transitions = transitions
        self.arcs = arcs
        self.places = places
        self.nupn_SizeType = nupn_SizeType
        
        pass
    @property
    def places(self):
        return self.__places

    @places.setter
    def places(self, places: str):
        self.__places = places


    @property
    def arcs(self):
        return self.__arcs

    @arcs.setter
    def arcs(self, arcs: str):
        self.__arcs = arcs


    @property
    def transitions(self):
        return self.__transitions

    @transitions.setter
    def transitions(self, transitions: str):
        self.__transitions = transitions


    @property
    def nupn_SizeType(self):
        return self.__nupn_SizeType

    @nupn_SizeType.setter
    def nupn_SizeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nupn_SizeType__nupn_SizeType", None)
        self.__nupn_SizeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nupn_NUPNToolspecificType"):
                opp_val = getattr(old_value, "nupn_NUPNToolspecificType", None)
                if opp_val == self:
                    setattr(old_value, "nupn_NUPNToolspecificType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nupn_NUPNToolspecificType"):
                opp_val = getattr(value, "nupn_NUPNToolspecificType", None)
                setattr(value, "nupn_NUPNToolspecificType", self)

class nupn_StructureType:

    def __init__(self, safe: str, units: str, root: str, nupn_StructureType: set["nupn_UnitType"] = None, nupn_StructureType4: "nupn_NUPNToolspecificType" = None):
        self.safe = safe
        self.units = units
        self.root = root
        self.nupn_StructureType = nupn_StructureType if nupn_StructureType is not None else set()
        self.nupn_StructureType4 = nupn_StructureType4
        
        pass
    @property
    def units(self):
        return self.__units

    @units.setter
    def units(self, units: str):
        self.__units = units


    @property
    def safe(self):
        return self.__safe

    @safe.setter
    def safe(self, safe: str):
        self.__safe = safe


    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, root: str):
        self.__root = root


    @property
    def nupn_StructureType4(self):
        return self.__nupn_StructureType4

    @nupn_StructureType4.setter
    def nupn_StructureType4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nupn_StructureType__nupn_StructureType4", None)
        self.__nupn_StructureType4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nupn_NUPNToolspecificType3"):
                opp_val = getattr(old_value, "nupn_NUPNToolspecificType3", None)
                if opp_val == self:
                    setattr(old_value, "nupn_NUPNToolspecificType3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nupn_NUPNToolspecificType3"):
                opp_val = getattr(value, "nupn_NUPNToolspecificType3", None)
                setattr(value, "nupn_NUPNToolspecificType3", self)

    @property
    def nupn_StructureType(self):
        return self.__nupn_StructureType

    @nupn_StructureType.setter
    def nupn_StructureType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nupn_StructureType__nupn_StructureType", None)
        self.__nupn_StructureType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nupn_UnitType"):
                    opp_val = getattr(item, "nupn_UnitType", None)
                    
                    if opp_val == self:
                        setattr(item, "nupn_UnitType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nupn_UnitType"):
                    opp_val = getattr(item, "nupn_UnitType", None)
                    
                    setattr(item, "nupn_UnitType", self)
                    
