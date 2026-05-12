from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class KudaType(Enum):
    MAIN = "MAIN"
    PUBLISH = "PUBLISH"
    TIPO = "TIPO"
class Mtype(Enum):
    KUDA = "KUDA"
    KOBE = "KOBE"
class KobeType(Enum):
    KORA = "KORA"
    MAIN = "MAIN"
    AUSW = "AUSW"
class KudaReplicate(Enum):
    PUBLISH = "PUBLISH"
    PUBLISHSTV = "PUBLISHSTV"
    DWH = "DWH"
    SNAP = "SNAP"
class LockSchema(Enum):
    DATAPAGES = "DATAPAGES"
    DATAROWS = "DATAROWS"
    ALLPAGES = "ALLPAGES"
class PhysicalDatabase(Enum):
    PDB_ABFRAGE_ARCHIV = "PDB_ABFRAGE_ARCHIV"
    PDB_ABFRAGE_BUCH_STAMM = "PDB_ABFRAGE_BUCH_STAMM"
    PDB_ABFRAGE_ETV = "PDB_ABFRAGE_ETV"
    PDB_ABFRAGE_FZK = "PDB_ABFRAGE_FZK"
    PDB_ABFRAGE_MON = "PDB_ABFRAGE_MON"
    PDB_ABFRAGE_PKT_STAMM = "PDB_ABFRAGE_PKT_STAMM"
    PDB_ABFRAGE_VSTI = "PDB_ABFRAGE_VSTI"
    PDB_AUSW_KOBE_ARCHIV = "PDB_AUSW_KOBE_ARCHIV"
    PDB_AUSW_KOBE_BUCH_STAMM = "PDB_AUSW_KOBE_BUCH_STAMM"
    PDB_AUSW_KOBE_MON = "PDB_AUSW_KOBE_MON"
    PDB_AUSW_KOBE_PKT_STAMM = "PDB_AUSW_KOBE_PKT_STAMM"
    PDB_AUSW_KOBE_STATISTIK = "PDB_AUSW_KOBE_STATISTIK"
    PDB_KOBE_AUSW_ADMIN = "PDB_KOBE_AUSW_ADMIN"
    PDB_KOBE_DATA = "PDB_KOBE_DATA"
    PDB_KOBE_DEZ_STAMM = "PDB_KOBE_DEZ_STAMM"
    PDB_KOBE_KNDTEST = "PDB_KOBE_KNDTEST"
    PDB_KOBE_PMON = "PDB_KOBE_PMON"
    PDB_KOBE_STAMM = "PDB_KOBE_STAMM"
    PDB_KOBE_STEUERUNG = "PDB_KOBE_STEUERUNG"
    PDB_KOBE_GLOBAL = "PDB_KOBE_GLOBAL"
    PDB_KUDA_TRANS_TRANSIT = "PDB_KUDA_TRANS_TRANSIT"
    PDB_MANDANT_BUCH_PROV = "PDB_MANDANT_BUCH_PROV"
    PDB_MANDANT_BUCH_STAMM = "PDB_MANDANT_BUCH_STAMM"
    PDB_MANDANT_MON = "PDB_MANDANT_MON"
    PDB_MANDANT_PKT_DATA = "PDB_MANDANT_PKT_DATA"
    PDB_MANDANT_PKT_STAMM = "PDB_MANDANT_PKT_STAMM"
    PDB_MANDANT_TAG = "PDB_MANDANT_TAG"
    PDB_MANDANT_TAG_A = "PDB_MANDANT_TAG_A"
    PDB_PART_AUFT = "PDB_PART_AUFT"
    PDB_PART_BUCH_PROV = "PDB_PART_BUCH_PROV"
    PDB_PART_BUCH_STAMM = "PDB_PART_BUCH_STAMM"
    PDB_PART_JAHR = "PDB_PART_JAHR"
    PDB_PART_MON = "PDB_PART_MON"
    PDB_PART_PKT_DATA = "PDB_PART_PKT_DATA"
    PDB_PART_PKT_STAMM = "PDB_PART_PKT_STAMM"
    PDB_PART_TAG = "PDB_PART_TAG"
    PDB_PART_TAG_A = "PDB_PART_TAG_A"


############################################
# Definition of Classes
############################################

class dbmodel_ClassOrDuplicate:

    def __init__(self, name: str, abbrev: str, reps: str):
        self.name = name
        self.abbrev = abbrev
        self.reps = reps
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def reps(self):
        return self.__reps

    @reps.setter
    def reps(self, reps: str):
        self.__reps = reps


    @property
    def abbrev(self):
        return self.__abbrev

    @abbrev.setter
    def abbrev(self, abbrev: str):
        self.__abbrev = abbrev


class dbmodel_Stype:

    pass
class dbmodel_Type:

    pass
class dbmodel_IndexRef:

    def __init__(self, isPrimkey: bool, clustered: bool, dbmodel_IndexRef: "dbmodel_Index" = None, dbmodel_IndexRef42: "dbmodel_Attribute" = None, dbmodel_IndexRef46: "dbmodel_Pdb" = None):
        self.isPrimkey = isPrimkey
        self.clustered = clustered
        self.dbmodel_IndexRef = dbmodel_IndexRef
        self.dbmodel_IndexRef42 = dbmodel_IndexRef42
        self.dbmodel_IndexRef46 = dbmodel_IndexRef46
        
        pass
    @property
    def clustered(self):
        return self.__clustered

    @clustered.setter
    def clustered(self, clustered: bool):
        self.__clustered = clustered


    @property
    def isPrimkey(self):
        return self.__isPrimkey

    @isPrimkey.setter
    def isPrimkey(self, isPrimkey: bool):
        self.__isPrimkey = isPrimkey


    @property
    def dbmodel_IndexRef46(self):
        return self.__dbmodel_IndexRef46

    @dbmodel_IndexRef46.setter
    def dbmodel_IndexRef46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_IndexRef__dbmodel_IndexRef46", None)
        self.__dbmodel_IndexRef46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbmodel_Pdb45"):
                opp_val = getattr(old_value, "dbmodel_Pdb45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbmodel_Pdb45"):
                opp_val = getattr(value, "dbmodel_Pdb45", None)
                if opp_val is None:
                    setattr(value, "dbmodel_Pdb45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbmodel_IndexRef42(self):
        return self.__dbmodel_IndexRef42

    @dbmodel_IndexRef42.setter
    def dbmodel_IndexRef42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_IndexRef__dbmodel_IndexRef42", None)
        self.__dbmodel_IndexRef42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbmodel_Attribute43"):
                opp_val = getattr(old_value, "dbmodel_Attribute43", None)
                if opp_val == self:
                    setattr(old_value, "dbmodel_Attribute43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbmodel_Attribute43"):
                opp_val = getattr(value, "dbmodel_Attribute43", None)
                setattr(value, "dbmodel_Attribute43", self)

    @property
    def dbmodel_IndexRef(self):
        return self.__dbmodel_IndexRef

    @dbmodel_IndexRef.setter
    def dbmodel_IndexRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_IndexRef__dbmodel_IndexRef", None)
        self.__dbmodel_IndexRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbmodel_Index40"):
                opp_val = getattr(old_value, "dbmodel_Index40", None)
                if opp_val == self:
                    setattr(old_value, "dbmodel_Index40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbmodel_Index40"):
                opp_val = getattr(value, "dbmodel_Index40", None)
                setattr(value, "dbmodel_Index40", self)

class dbmodel_Primkey:

    pass
class dbmodel_Attribute:

    def __init__(self, name: str, descr: str, foreign: bool, exttable: str, extattr: str, immutable: bool, nullOK: bool, kuko: bool, kukoindex: bool, kukoonly: bool, shared: bool, isPublic: bool, optional: bool, archiv: bool, aName: str, sybident: bool, isInDB: bool, dbmodel_Attribute53: "dbmodel_StructShare" = None, dbmodel_Attribute32: "dbmodel_Attribute" = None, dbmodel_Attribute30: "dbmodel_Attribute" = None, dbmodel_Attribute35: "dbmodel_Primkey" = None, dbmodel_Attribute22: "dbmodel_Ltype" = None, dbmodel_Attribute25: "dbmodel_Attribute" = None, dbmodel_Attribute23: "dbmodel_Attribute" = None, dbmodel_Attribute27: set["dbmodel_StructShare"] = None, dbmodel_Attribute29: set["dbmodel_StructOverride"] = None, dbmodel_Attribute: "dbmodel_Class" = None, dbmodel_Attribute38: "dbmodel_Index" = None, dbmodel_Attribute43: "dbmodel_IndexRef" = None):
        self.name = name
        self.descr = descr
        self.foreign = foreign
        self.exttable = exttable
        self.extattr = extattr
        self.immutable = immutable
        self.nullOK = nullOK
        self.kuko = kuko
        self.kukoindex = kukoindex
        self.kukoonly = kukoonly
        self.shared = shared
        self.isPublic = isPublic
        self.optional = optional
        self.archiv = archiv
        self.aName = aName
        self.sybident = sybident
        self.isInDB = isInDB
        self.dbmodel_Attribute53 = dbmodel_Attribute53
        self.dbmodel_Attribute32 = dbmodel_Attribute32
        self.dbmodel_Attribute30 = dbmodel_Attribute30
        self.dbmodel_Attribute35 = dbmodel_Attribute35
        self.dbmodel_Attribute22 = dbmodel_Attribute22
        self.dbmodel_Attribute25 = dbmodel_Attribute25
        self.dbmodel_Attribute23 = dbmodel_Attribute23
        self.dbmodel_Attribute27 = dbmodel_Attribute27 if dbmodel_Attribute27 is not None else set()
        self.dbmodel_Attribute29 = dbmodel_Attribute29 if dbmodel_Attribute29 is not None else set()
        self.dbmodel_Attribute = dbmodel_Attribute
        self.dbmodel_Attribute38 = dbmodel_Attribute38
        self.dbmodel_Attribute43 = dbmodel_Attribute43
        
        pass
    @property
    def descr(self):
        return self.__descr

    @descr.setter
    def descr(self, descr: str):
        self.__descr = descr


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def kukoindex(self):
        return self.__kukoindex

    @kukoindex.setter
    def kukoindex(self, kukoindex: bool):
        self.__kukoindex = kukoindex


    @property
    def aName(self):
        return self.__aName

    @aName.setter
    def aName(self, aName: str):
        self.__aName = aName


    @property
    def sybident(self):
        return self.__sybident

    @sybident.setter
    def sybident(self, sybident: bool):
        self.__sybident = sybident


    @property
    def extattr(self):
        return self.__extattr

    @extattr.setter
    def extattr(self, extattr: str):
        self.__extattr = extattr


    @property
    def foreign(self):
        return self.__foreign

    @foreign.setter
    def foreign(self, foreign: bool):
        self.__foreign = foreign


    @property
    def isInDB(self):
        return self.__isInDB

    @isInDB.setter
    def isInDB(self, isInDB: bool):
        self.__isInDB = isInDB


    @property
    def nullOK(self):
        return self.__nullOK

    @nullOK.setter
    def nullOK(self, nullOK: bool):
        self.__nullOK = nullOK


    @property
    def shared(self):
        return self.__shared

    @shared.setter
    def shared(self, shared: bool):
        self.__shared = shared


    @property
    def optional(self):
        return self.__optional

    @optional.setter
    def optional(self, optional: bool):
        self.__optional = optional


    @property
    def kuko(self):
        return self.__kuko

    @kuko.setter
    def kuko(self, kuko: bool):
        self.__kuko = kuko


    @property
    def archiv(self):
        return self.__archiv

    @archiv.setter
    def archiv(self, archiv: bool):
        self.__archiv = archiv


    @property
    def exttable(self):
        return self.__exttable

    @exttable.setter
    def exttable(self, exttable: str):
        self.__exttable = exttable


    @property
    def isPublic(self):
        return self.__isPublic

    @isPublic.setter
    def isPublic(self, isPublic: bool):
        self.__isPublic = isPublic


    @property
    def immutable(self):
        return self.__immutable

    @immutable.setter
    def immutable(self, immutable: bool):
        self.__immutable = immutable


    @property
    def kukoonly(self):
        return self.__kukoonly

    @kukoonly.setter
    def kukoonly(self, kukoonly: bool):
        self.__kukoonly = kukoonly


    @property
    def dbmodel_Attribute43(self):
        return self.__dbmodel_Attribute43

    @dbmodel_Attribute43.setter
    def dbmodel_Attribute43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_Attribute__dbmodel_Attribute43", None)
        self.__dbmodel_Attribute43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbmodel_IndexRef42"):
                opp_val = getattr(old_value, "dbmodel_IndexRef42", None)
                if opp_val == self:
                    setattr(old_value, "dbmodel_IndexRef42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbmodel_IndexRef42"):
                opp_val = getattr(value, "dbmodel_IndexRef42", None)
                setattr(value, "dbmodel_IndexRef42", self)

    @property
    def dbmodel_Attribute22(self):
        return self.__dbmodel_Attribute22

    @dbmodel_Attribute22.setter
    def dbmodel_Attribute22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_Attribute__dbmodel_Attribute22", None)
        self.__dbmodel_Attribute22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbmodel_Ltype"):
                opp_val = getattr(old_value, "dbmodel_Ltype", None)
                if opp_val == self:
                    setattr(old_value, "dbmodel_Ltype", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbmodel_Ltype"):
                opp_val = getattr(value, "dbmodel_Ltype", None)
                setattr(value, "dbmodel_Ltype", self)

    @property
    def dbmodel_Attribute(self):
        return self.__dbmodel_Attribute

    @dbmodel_Attribute.setter
    def dbmodel_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_Attribute__dbmodel_Attribute", None)
        self.__dbmodel_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbmodel_Class11"):
                opp_val = getattr(old_value, "dbmodel_Class11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbmodel_Class11"):
                opp_val = getattr(value, "dbmodel_Class11", None)
                if opp_val is None:
                    setattr(value, "dbmodel_Class11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbmodel_Attribute53(self):
        return self.__dbmodel_Attribute53

    @dbmodel_Attribute53.setter
    def dbmodel_Attribute53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_Attribute__dbmodel_Attribute53", None)
        self.__dbmodel_Attribute53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbmodel_StructShare52"):
                opp_val = getattr(old_value, "dbmodel_StructShare52", None)
                if opp_val == self:
                    setattr(old_value, "dbmodel_StructShare52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbmodel_StructShare52"):
                opp_val = getattr(value, "dbmodel_StructShare52", None)
                setattr(value, "dbmodel_StructShare52", self)

    @property
    def dbmodel_Attribute35(self):
        return self.__dbmodel_Attribute35

    @dbmodel_Attribute35.setter
    def dbmodel_Attribute35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_Attribute__dbmodel_Attribute35", None)
        self.__dbmodel_Attribute35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbmodel_Primkey34"):
                opp_val = getattr(old_value, "dbmodel_Primkey34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbmodel_Primkey34"):
                opp_val = getattr(value, "dbmodel_Primkey34", None)
                if opp_val is None:
                    setattr(value, "dbmodel_Primkey34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbmodel_Attribute30(self):
        return self.__dbmodel_Attribute30

    @dbmodel_Attribute30.setter
    def dbmodel_Attribute30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_Attribute__dbmodel_Attribute30", None)
        self.__dbmodel_Attribute30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbmodel_Attribute32"):
                opp_val = getattr(old_value, "dbmodel_Attribute32", None)
                if opp_val == self:
                    setattr(old_value, "dbmodel_Attribute32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbmodel_Attribute32"):
                opp_val = getattr(value, "dbmodel_Attribute32", None)
                setattr(value, "dbmodel_Attribute32", self)

    @property
    def dbmodel_Attribute23(self):
        return self.__dbmodel_Attribute23

    @dbmodel_Attribute23.setter
    def dbmodel_Attribute23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_Attribute__dbmodel_Attribute23", None)
        self.__dbmodel_Attribute23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbmodel_Attribute25"):
                opp_val = getattr(old_value, "dbmodel_Attribute25", None)
                if opp_val == self:
                    setattr(old_value, "dbmodel_Attribute25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbmodel_Attribute25"):
                opp_val = getattr(value, "dbmodel_Attribute25", None)
                setattr(value, "dbmodel_Attribute25", self)

    @property
    def dbmodel_Attribute32(self):
        return self.__dbmodel_Attribute32

    @dbmodel_Attribute32.setter
    def dbmodel_Attribute32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_Attribute__dbmodel_Attribute32", None)
        self.__dbmodel_Attribute32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbmodel_Attribute30"):
                opp_val = getattr(old_value, "dbmodel_Attribute30", None)
                if opp_val == self:
                    setattr(old_value, "dbmodel_Attribute30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbmodel_Attribute30"):
                opp_val = getattr(value, "dbmodel_Attribute30", None)
                setattr(value, "dbmodel_Attribute30", self)

    @property
    def dbmodel_Attribute25(self):
        return self.__dbmodel_Attribute25

    @dbmodel_Attribute25.setter
    def dbmodel_Attribute25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_Attribute__dbmodel_Attribute25", None)
        self.__dbmodel_Attribute25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbmodel_Attribute23"):
                opp_val = getattr(old_value, "dbmodel_Attribute23", None)
                if opp_val == self:
                    setattr(old_value, "dbmodel_Attribute23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbmodel_Attribute23"):
                opp_val = getattr(value, "dbmodel_Attribute23", None)
                setattr(value, "dbmodel_Attribute23", self)

    @property
    def dbmodel_Attribute38(self):
        return self.__dbmodel_Attribute38

    @dbmodel_Attribute38.setter
    def dbmodel_Attribute38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_Attribute__dbmodel_Attribute38", None)
        self.__dbmodel_Attribute38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbmodel_Index37"):
                opp_val = getattr(old_value, "dbmodel_Index37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbmodel_Index37"):
                opp_val = getattr(value, "dbmodel_Index37", None)
                if opp_val is None:
                    setattr(value, "dbmodel_Index37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbmodel_Attribute29(self):
        return self.__dbmodel_Attribute29

    @dbmodel_Attribute29.setter
    def dbmodel_Attribute29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_Attribute__dbmodel_Attribute29", None)
        self.__dbmodel_Attribute29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbmodel_StructOverride"):
                    opp_val = getattr(item, "dbmodel_StructOverride", None)
                    
                    if opp_val == self:
                        setattr(item, "dbmodel_StructOverride", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbmodel_StructOverride"):
                    opp_val = getattr(item, "dbmodel_StructOverride", None)
                    
                    setattr(item, "dbmodel_StructOverride", self)
                    

    @property
    def dbmodel_Attribute27(self):
        return self.__dbmodel_Attribute27

    @dbmodel_Attribute27.setter
    def dbmodel_Attribute27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_Attribute__dbmodel_Attribute27", None)
        self.__dbmodel_Attribute27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbmodel_StructShare"):
                    opp_val = getattr(item, "dbmodel_StructShare", None)
                    
                    if opp_val == self:
                        setattr(item, "dbmodel_StructShare", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbmodel_StructShare"):
                    opp_val = getattr(item, "dbmodel_StructShare", None)
                    
                    setattr(item, "dbmodel_StructShare", self)
                    

class dbmodel_StructOverride:

    def __init__(self, altname: str, dbmodel_StructOverride50: "dbmodel_Stype" = None, dbmodel_StructOverride: "dbmodel_Attribute" = None):
        self.altname = altname
        self.dbmodel_StructOverride50 = dbmodel_StructOverride50
        self.dbmodel_StructOverride = dbmodel_StructOverride
        
        pass
    @property
    def altname(self):
        return self.__altname

    @altname.setter
    def altname(self, altname: str):
        self.__altname = altname


    @property
    def dbmodel_StructOverride(self):
        return self.__dbmodel_StructOverride

    @dbmodel_StructOverride.setter
    def dbmodel_StructOverride(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_StructOverride__dbmodel_StructOverride", None)
        self.__dbmodel_StructOverride = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbmodel_Attribute29"):
                opp_val = getattr(old_value, "dbmodel_Attribute29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbmodel_Attribute29"):
                opp_val = getattr(value, "dbmodel_Attribute29", None)
                if opp_val is None:
                    setattr(value, "dbmodel_Attribute29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbmodel_StructOverride50(self):
        return self.__dbmodel_StructOverride50

    @dbmodel_StructOverride50.setter
    def dbmodel_StructOverride50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_StructOverride__dbmodel_StructOverride50", None)
        self.__dbmodel_StructOverride50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbmodel_Stype"):
                opp_val = getattr(old_value, "dbmodel_Stype", None)
                if opp_val == self:
                    setattr(old_value, "dbmodel_Stype", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbmodel_Stype"):
                opp_val = getattr(value, "dbmodel_Stype", None)
                setattr(value, "dbmodel_Stype", self)

class dbmodel_StructShare:

    pass
class dbmodel_Ltype:

    pass
class dbmodel_Pdb:

    def __init__(self, name: str, lockSchema: str, tablePartitioning: int, dbmodel_Pdb: "dbmodel_Class" = None, dbmodel_Pdb45: set["dbmodel_IndexRef"] = None):
        self.name = name
        self.lockSchema = lockSchema
        self.tablePartitioning = tablePartitioning
        self.dbmodel_Pdb = dbmodel_Pdb
        self.dbmodel_Pdb45 = dbmodel_Pdb45 if dbmodel_Pdb45 is not None else set()
        
        pass
    @property
    def tablePartitioning(self):
        return self.__tablePartitioning

    @tablePartitioning.setter
    def tablePartitioning(self, tablePartitioning: int):
        self.__tablePartitioning = tablePartitioning


    @property
    def lockSchema(self):
        return self.__lockSchema

    @lockSchema.setter
    def lockSchema(self, lockSchema: str):
        self.__lockSchema = lockSchema


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def dbmodel_Pdb(self):
        return self.__dbmodel_Pdb

    @dbmodel_Pdb.setter
    def dbmodel_Pdb(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_Pdb__dbmodel_Pdb", None)
        self.__dbmodel_Pdb = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbmodel_Class17"):
                opp_val = getattr(old_value, "dbmodel_Class17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbmodel_Class17"):
                opp_val = getattr(value, "dbmodel_Class17", None)
                if opp_val is None:
                    setattr(value, "dbmodel_Class17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbmodel_Pdb45(self):
        return self.__dbmodel_Pdb45

    @dbmodel_Pdb45.setter
    def dbmodel_Pdb45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_Pdb__dbmodel_Pdb45", None)
        self.__dbmodel_Pdb45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbmodel_IndexRef46"):
                    opp_val = getattr(item, "dbmodel_IndexRef46", None)
                    
                    if opp_val == self:
                        setattr(item, "dbmodel_IndexRef46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbmodel_IndexRef46"):
                    opp_val = getattr(item, "dbmodel_IndexRef46", None)
                    
                    setattr(item, "dbmodel_IndexRef46", self)
                    

class dbmodel_Index:

    def __init__(self, kuko: bool, name: str, unique: bool, dbmodel_Index: "dbmodel_Class" = None, dbmodel_Index37: set["dbmodel_Attribute"] = None, dbmodel_Index40: "dbmodel_IndexRef" = None):
        self.kuko = kuko
        self.name = name
        self.unique = unique
        self.dbmodel_Index = dbmodel_Index
        self.dbmodel_Index37 = dbmodel_Index37 if dbmodel_Index37 is not None else set()
        self.dbmodel_Index40 = dbmodel_Index40
        
        pass
    @property
    def kuko(self):
        return self.__kuko

    @kuko.setter
    def kuko(self, kuko: bool):
        self.__kuko = kuko


    @property
    def unique(self):
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def dbmodel_Index37(self):
        return self.__dbmodel_Index37

    @dbmodel_Index37.setter
    def dbmodel_Index37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_Index__dbmodel_Index37", None)
        self.__dbmodel_Index37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbmodel_Attribute38"):
                    opp_val = getattr(item, "dbmodel_Attribute38", None)
                    
                    if opp_val == self:
                        setattr(item, "dbmodel_Attribute38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbmodel_Attribute38"):
                    opp_val = getattr(item, "dbmodel_Attribute38", None)
                    
                    setattr(item, "dbmodel_Attribute38", self)
                    

    @property
    def dbmodel_Index40(self):
        return self.__dbmodel_Index40

    @dbmodel_Index40.setter
    def dbmodel_Index40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_Index__dbmodel_Index40", None)
        self.__dbmodel_Index40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbmodel_IndexRef"):
                opp_val = getattr(old_value, "dbmodel_IndexRef", None)
                if opp_val == self:
                    setattr(old_value, "dbmodel_IndexRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbmodel_IndexRef"):
                opp_val = getattr(value, "dbmodel_IndexRef", None)
                setattr(value, "dbmodel_IndexRef", self)

    @property
    def dbmodel_Index(self):
        return self.__dbmodel_Index

    @dbmodel_Index.setter
    def dbmodel_Index(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_Index__dbmodel_Index", None)
        self.__dbmodel_Index = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbmodel_Class15"):
                opp_val = getattr(old_value, "dbmodel_Class15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbmodel_Class15"):
                opp_val = getattr(value, "dbmodel_Class15", None)
                if opp_val is None:
                    setattr(value, "dbmodel_Class15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dbmodel_DbModel:

    def __init__(self, kudaType: str, kobeType: str, version: str, doAll: bool, name: str, mtype: str, dbmodel_DbModel: set["dbmodel_Import"] = None, dbmodel_DbModel2: set["dbmodel_Subject"] = None, dbmodel_DbModel4: set["dbmodel_Class"] = None, dbmodel_DbModel6: set["dbmodel_Duplicate"] = None):
        self.kudaType = kudaType
        self.kobeType = kobeType
        self.version = version
        self.doAll = doAll
        self.name = name
        self.mtype = mtype
        self.dbmodel_DbModel = dbmodel_DbModel if dbmodel_DbModel is not None else set()
        self.dbmodel_DbModel2 = dbmodel_DbModel2 if dbmodel_DbModel2 is not None else set()
        self.dbmodel_DbModel4 = dbmodel_DbModel4 if dbmodel_DbModel4 is not None else set()
        self.dbmodel_DbModel6 = dbmodel_DbModel6 if dbmodel_DbModel6 is not None else set()
        
        pass
    @property
    def doAll(self):
        return self.__doAll

    @doAll.setter
    def doAll(self, doAll: bool):
        self.__doAll = doAll


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def kudaType(self):
        return self.__kudaType

    @kudaType.setter
    def kudaType(self, kudaType: str):
        self.__kudaType = kudaType


    @property
    def kobeType(self):
        return self.__kobeType

    @kobeType.setter
    def kobeType(self, kobeType: str):
        self.__kobeType = kobeType


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def mtype(self):
        return self.__mtype

    @mtype.setter
    def mtype(self, mtype: str):
        self.__mtype = mtype


    @property
    def dbmodel_DbModel(self):
        return self.__dbmodel_DbModel

    @dbmodel_DbModel.setter
    def dbmodel_DbModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_DbModel__dbmodel_DbModel", None)
        self.__dbmodel_DbModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbmodel_Import"):
                    opp_val = getattr(item, "dbmodel_Import", None)
                    
                    if opp_val == self:
                        setattr(item, "dbmodel_Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbmodel_Import"):
                    opp_val = getattr(item, "dbmodel_Import", None)
                    
                    setattr(item, "dbmodel_Import", self)
                    

    @property
    def dbmodel_DbModel4(self):
        return self.__dbmodel_DbModel4

    @dbmodel_DbModel4.setter
    def dbmodel_DbModel4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_DbModel__dbmodel_DbModel4", None)
        self.__dbmodel_DbModel4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbmodel_Class"):
                    opp_val = getattr(item, "dbmodel_Class", None)
                    
                    if opp_val == self:
                        setattr(item, "dbmodel_Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbmodel_Class"):
                    opp_val = getattr(item, "dbmodel_Class", None)
                    
                    setattr(item, "dbmodel_Class", self)
                    

    @property
    def dbmodel_DbModel6(self):
        return self.__dbmodel_DbModel6

    @dbmodel_DbModel6.setter
    def dbmodel_DbModel6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_DbModel__dbmodel_DbModel6", None)
        self.__dbmodel_DbModel6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbmodel_Duplicate"):
                    opp_val = getattr(item, "dbmodel_Duplicate", None)
                    
                    if opp_val == self:
                        setattr(item, "dbmodel_Duplicate", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbmodel_Duplicate"):
                    opp_val = getattr(item, "dbmodel_Duplicate", None)
                    
                    setattr(item, "dbmodel_Duplicate", self)
                    

    @property
    def dbmodel_DbModel2(self):
        return self.__dbmodel_DbModel2

    @dbmodel_DbModel2.setter
    def dbmodel_DbModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_DbModel__dbmodel_DbModel2", None)
        self.__dbmodel_DbModel2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbmodel_Subject"):
                    opp_val = getattr(item, "dbmodel_Subject", None)
                    
                    if opp_val == self:
                        setattr(item, "dbmodel_Subject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbmodel_Subject"):
                    opp_val = getattr(item, "dbmodel_Subject", None)
                    
                    setattr(item, "dbmodel_Subject", self)
                    

class ClassOrDuplicate:

    pass
class dbmodel_Duplicate(ClassOrDuplicate):

    pass
class dbmodel_Class(ClassOrDuplicate):

    def __init__(self, descr: str, noDBio: bool, publish: bool, vmaj: int, vmin: int, pubspec: bool, pubname: str, whereclause: str, aName: str, archivIndex: str, dbmodel_Class: "dbmodel_DbModel" = None, dbmodel_Class8: "dbmodel_Subject" = None, dbmodel_Class15: set["dbmodel_Index"] = None, dbmodel_Class17: set["dbmodel_Pdb"] = None, dbmodel_Class20: "dbmodel_Duplicate" = None, dbmodel_Class11: set["dbmodel_Attribute"] = None, dbmodel_Class13: "dbmodel_Primkey" = None):
        self.descr = descr
        self.noDBio = noDBio
        self.publish = publish
        self.vmaj = vmaj
        self.vmin = vmin
        self.pubspec = pubspec
        self.pubname = pubname
        self.whereclause = whereclause
        self.aName = aName
        self.archivIndex = archivIndex
        self.dbmodel_Class = dbmodel_Class
        self.dbmodel_Class8 = dbmodel_Class8
        self.dbmodel_Class15 = dbmodel_Class15 if dbmodel_Class15 is not None else set()
        self.dbmodel_Class17 = dbmodel_Class17 if dbmodel_Class17 is not None else set()
        self.dbmodel_Class20 = dbmodel_Class20
        self.dbmodel_Class11 = dbmodel_Class11 if dbmodel_Class11 is not None else set()
        self.dbmodel_Class13 = dbmodel_Class13
        
        pass
    @property
    def aName(self):
        return self.__aName

    @aName.setter
    def aName(self, aName: str):
        self.__aName = aName


    @property
    def descr(self):
        return self.__descr

    @descr.setter
    def descr(self, descr: str):
        self.__descr = descr


    @property
    def whereclause(self):
        return self.__whereclause

    @whereclause.setter
    def whereclause(self, whereclause: str):
        self.__whereclause = whereclause


    @property
    def archivIndex(self):
        return self.__archivIndex

    @archivIndex.setter
    def archivIndex(self, archivIndex: str):
        self.__archivIndex = archivIndex


    @property
    def pubspec(self):
        return self.__pubspec

    @pubspec.setter
    def pubspec(self, pubspec: bool):
        self.__pubspec = pubspec


    @property
    def noDBio(self):
        return self.__noDBio

    @noDBio.setter
    def noDBio(self, noDBio: bool):
        self.__noDBio = noDBio


    @property
    def vmaj(self):
        return self.__vmaj

    @vmaj.setter
    def vmaj(self, vmaj: int):
        self.__vmaj = vmaj


    @property
    def publish(self):
        return self.__publish

    @publish.setter
    def publish(self, publish: bool):
        self.__publish = publish


    @property
    def pubname(self):
        return self.__pubname

    @pubname.setter
    def pubname(self, pubname: str):
        self.__pubname = pubname


    @property
    def vmin(self):
        return self.__vmin

    @vmin.setter
    def vmin(self, vmin: int):
        self.__vmin = vmin


    @property
    def dbmodel_Class15(self):
        return self.__dbmodel_Class15

    @dbmodel_Class15.setter
    def dbmodel_Class15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_Class__dbmodel_Class15", None)
        self.__dbmodel_Class15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbmodel_Index"):
                    opp_val = getattr(item, "dbmodel_Index", None)
                    
                    if opp_val == self:
                        setattr(item, "dbmodel_Index", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbmodel_Index"):
                    opp_val = getattr(item, "dbmodel_Index", None)
                    
                    setattr(item, "dbmodel_Index", self)
                    

    @property
    def dbmodel_Class(self):
        return self.__dbmodel_Class

    @dbmodel_Class.setter
    def dbmodel_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_Class__dbmodel_Class", None)
        self.__dbmodel_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbmodel_DbModel4"):
                opp_val = getattr(old_value, "dbmodel_DbModel4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbmodel_DbModel4"):
                opp_val = getattr(value, "dbmodel_DbModel4", None)
                if opp_val is None:
                    setattr(value, "dbmodel_DbModel4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbmodel_Class11(self):
        return self.__dbmodel_Class11

    @dbmodel_Class11.setter
    def dbmodel_Class11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_Class__dbmodel_Class11", None)
        self.__dbmodel_Class11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbmodel_Attribute"):
                    opp_val = getattr(item, "dbmodel_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "dbmodel_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbmodel_Attribute"):
                    opp_val = getattr(item, "dbmodel_Attribute", None)
                    
                    setattr(item, "dbmodel_Attribute", self)
                    

    @property
    def dbmodel_Class13(self):
        return self.__dbmodel_Class13

    @dbmodel_Class13.setter
    def dbmodel_Class13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_Class__dbmodel_Class13", None)
        self.__dbmodel_Class13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbmodel_Primkey"):
                opp_val = getattr(old_value, "dbmodel_Primkey", None)
                if opp_val == self:
                    setattr(old_value, "dbmodel_Primkey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbmodel_Primkey"):
                opp_val = getattr(value, "dbmodel_Primkey", None)
                setattr(value, "dbmodel_Primkey", self)

    @property
    def dbmodel_Class8(self):
        return self.__dbmodel_Class8

    @dbmodel_Class8.setter
    def dbmodel_Class8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_Class__dbmodel_Class8", None)
        self.__dbmodel_Class8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbmodel_Subject9"):
                opp_val = getattr(old_value, "dbmodel_Subject9", None)
                if opp_val == self:
                    setattr(old_value, "dbmodel_Subject9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbmodel_Subject9"):
                opp_val = getattr(value, "dbmodel_Subject9", None)
                setattr(value, "dbmodel_Subject9", self)

    @property
    def dbmodel_Class17(self):
        return self.__dbmodel_Class17

    @dbmodel_Class17.setter
    def dbmodel_Class17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_Class__dbmodel_Class17", None)
        self.__dbmodel_Class17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbmodel_Pdb"):
                    opp_val = getattr(item, "dbmodel_Pdb", None)
                    
                    if opp_val == self:
                        setattr(item, "dbmodel_Pdb", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbmodel_Pdb"):
                    opp_val = getattr(item, "dbmodel_Pdb", None)
                    
                    setattr(item, "dbmodel_Pdb", self)
                    

    @property
    def dbmodel_Class20(self):
        return self.__dbmodel_Class20

    @dbmodel_Class20.setter
    def dbmodel_Class20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_Class__dbmodel_Class20", None)
        self.__dbmodel_Class20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbmodel_Duplicate19"):
                opp_val = getattr(old_value, "dbmodel_Duplicate19", None)
                if opp_val == self:
                    setattr(old_value, "dbmodel_Duplicate19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbmodel_Duplicate19"):
                opp_val = getattr(value, "dbmodel_Duplicate19", None)
                setattr(value, "dbmodel_Duplicate19", self)

class dbmodel_Subject:

    def __init__(self, name: str, dbmodel_Subject: "dbmodel_DbModel" = None, dbmodel_Subject9: "dbmodel_Class" = None):
        self.name = name
        self.dbmodel_Subject = dbmodel_Subject
        self.dbmodel_Subject9 = dbmodel_Subject9
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def dbmodel_Subject(self):
        return self.__dbmodel_Subject

    @dbmodel_Subject.setter
    def dbmodel_Subject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_Subject__dbmodel_Subject", None)
        self.__dbmodel_Subject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbmodel_DbModel2"):
                opp_val = getattr(old_value, "dbmodel_DbModel2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbmodel_DbModel2"):
                opp_val = getattr(value, "dbmodel_DbModel2", None)
                if opp_val is None:
                    setattr(value, "dbmodel_DbModel2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbmodel_Subject9(self):
        return self.__dbmodel_Subject9

    @dbmodel_Subject9.setter
    def dbmodel_Subject9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_Subject__dbmodel_Subject9", None)
        self.__dbmodel_Subject9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbmodel_Class8"):
                opp_val = getattr(old_value, "dbmodel_Class8", None)
                if opp_val == self:
                    setattr(old_value, "dbmodel_Class8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbmodel_Class8"):
                opp_val = getattr(value, "dbmodel_Class8", None)
                setattr(value, "dbmodel_Class8", self)

class dbmodel_Import:

    def __init__(self, importedNamespace: str, dbmodel_Import: "dbmodel_DbModel" = None):
        self.importedNamespace = importedNamespace
        self.dbmodel_Import = dbmodel_Import
        
        pass
    @property
    def importedNamespace(self):
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace


    @property
    def dbmodel_Import(self):
        return self.__dbmodel_Import

    @dbmodel_Import.setter
    def dbmodel_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmodel_Import__dbmodel_Import", None)
        self.__dbmodel_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbmodel_DbModel"):
                opp_val = getattr(old_value, "dbmodel_DbModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbmodel_DbModel"):
                opp_val = getattr(value, "dbmodel_DbModel", None)
                if opp_val is None:
                    setattr(value, "dbmodel_DbModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
